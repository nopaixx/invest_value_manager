#!/usr/bin/env python3
"""
R1 Prioritizer — Ranks SCORED companies for R1 fundamental analysis.

Reads quality_universe.yaml, filters SCORED entries, ranks by quality and
proximity to entry, and flags earnings gates. Designed to be the first
step in Fase 2.7 R1 processing each session.

When R1_COMPLETE count >= 20 in the universe, auto-filters to distance_to_entry
<= 25% (near-entry focus). Use --include-far to override.

Shows E[CAGR] column for companies with FV + entry_price defined:
  E[CAGR] = (FV/entry)^(1/3) - 1 + dividend_yield

Usage:
  python3 tools/r1_prioritizer.py                       # Top 10 candidates
  python3 tools/r1_prioritizer.py --top 20               # Top 20
  python3 tools/r1_prioritizer.py --exclude-uk           # Skip UK #5 risk
  python3 tools/r1_prioritizer.py --near-entry-only      # Only <20% from entry (forced)
  python3 tools/r1_prioritizer.py --include-far          # Override auto near-entry filter
  python3 tools/r1_prioritizer.py --tier-a-only          # Only QS >= 75
  python3 tools/r1_prioritizer.py --no-ecagr             # Skip E[CAGR] (no yfinance calls)
  python3 tools/r1_prioritizer.py --exclude-fantasy-risk # Filter out price > 150% of FV
  python3 tools/r1_prioritizer.py --pre-flight           # Only E[CAGR]-at-entry >= threshold
  python3 tools/r1_prioritizer.py --advancement          # R1_COMPLETE advancement pipeline (3 sections)
  python3 tools/r1_prioritizer.py --near-entry-advancement  # Quick: advancement near entry only
  python3 tools/r1_prioritizer.py --buyable-now              # Reverse: what's buyable at market TODAY?
  python3 tools/r1_prioritizer.py --stagnation                    # Pipeline stagnation report
"""

import sys
import os
import argparse
from datetime import date, datetime, timedelta

import yaml

import re
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
UNIVERSE_PATH = os.path.join(PROJECT_ROOT, "state", "quality_universe.yaml")
CALENDAR_PATH = os.path.join(PROJECT_ROOT, "state", "calendar.yaml")
SECTORS_DIR = os.path.join(PROJECT_ROOT, "world", "sectors")
CONTINUITY_PATH = os.path.join(PROJECT_ROOT, "state", "session_continuity.yaml")
GRAPH_PATH = os.path.join(SCRIPT_DIR, "smart_money", "graph.json")
SNAPSHOTS_DIR = os.path.join(SCRIPT_DIR, "smart_money", "data", "snapshots")
RESEARCH_DIR = os.path.join(PROJECT_ROOT, "thesis", "research")

# Tickers known to NOT be available on eToro (verified manually)
ETORO_UNAVAILABLE = {
    "MEGP.L",   # ME Group, not on eToro
    "LAGR-B.ST",  # Lagercrantz, not on eToro
    "STF.PA",   # STEF, not on eToro
}

# UK tickers: .L suffix. Already 5 UK positions = concentration risk
UK_SUFFIX = ".L"


def load_universe():
    if not os.path.exists(UNIVERSE_PATH):
        return []
    with open(UNIVERSE_PATH, "r") as f:
        data = yaml.safe_load(f) or {}
    return data.get("quality_universe", {}).get("companies", [])


def load_earnings_tickers(days_ahead=30):
    """Load tickers with earnings in next N days from calendar.yaml."""
    if not os.path.exists(CALENDAR_PATH):
        return {}
    with open(CALENDAR_PATH, "r") as f:
        data = yaml.safe_load(f) or {}

    today = date.today()
    cutoff = today + timedelta(days=days_ahead)
    earnings = {}

    for event in data.get("events", []):
        event_date = event.get("date")
        event_type = event.get("type", "")
        ticker = event.get("ticker", "")

        if not event_date or not ticker:
            continue

        # Parse date
        if isinstance(event_date, date):
            d = event_date
        else:
            try:
                d = datetime.strptime(str(event_date), "%Y-%m-%d").date()
            except (ValueError, TypeError):
                continue

        if today <= d <= cutoff and "earnings" in event_type.lower():
            earnings[ticker] = d

    return earnings


def get_stale_sector_views():
    """Self-contained: parse sector view dates, return dict of filename -> age_days.

    Only includes views with age > 14 days (BORDERLINE+). Also tracks which
    sector labels map to which files for flagging universe companies.
    """
    if not os.path.isdir(SECTORS_DIR):
        return {}, {}

    today = date.today()
    stale = {}  # filename -> age_days

    for f in os.listdir(SECTORS_DIR):
        if not f.endswith(".md") or f == "_TEMPLATE.md":
            continue
        filepath = os.path.join(SECTORS_DIR, f)
        try:
            with open(filepath, "r") as fh:
                header = "".join(fh.readline() for _ in range(10))
        except (OSError, IOError):
            continue
        m = re.search(
            r"(?:Ultima actualizacion|Last Updated|Creado|Updated):\s*(\d{4}-\d{2}-\d{2})",
            header, re.IGNORECASE,
        )
        if m:
            try:
                d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
                age = (today - d).days
                if age > 14:
                    stale[f] = age
            except ValueError:
                pass

    return stale


# Lightweight sector label -> file mapping for stale-sector flagging
_SECTOR_TO_FILE = {
    "Technology": "technology", "Enterprise Software": "technology",
    "Financial Technology": "technology", "Software": "technology",
    "IT Services": "technology", "SaaS": "technology",
    "Health IT/SaaS": "technology", "Software/IT": "technology",
    "Software/ERP": "technology", "Tech/Software": "technology",
    "Industrials": "industrials", "Industrial Conglomerate": "industrials",
    "Specialty Industrial": "industrials", "Basic Materials": "industrials",
    "Specialty Chemicals": "industrials", "specialty-chemicals": "industrials",
    "Industrial Distribution": "industrials",
    "Industrial Equipment / Crane & Lifting": "industrials",
    "Industrial Gases": "industrials", "Industrials/Tools": "industrials",
    "Environmental Services/Facility": "industrials",
    "Testing/Inspection": "testing-inspection-certification",
    "Testing & Inspection": "testing-inspection-certification",
    "Testing/Inspection/Cert": "testing-inspection-certification",
    "Industrial Technology": "industrial-technology",
    "industrial-technology": "industrial-technology",
    "Safety/Environment": "industrial-technology",
    "Measurement/Instruments": "industrial-technology",
    "Scientific Instruments": "industrial-technology",
    "Industrial Automation": "industrial-technology",
    "Building Materials": "building-materials-cement",
    "Cement": "building-materials-cement",
    "Building Materials/Cement": "building-materials-cement",
    "building-products": "building-materials-cement",
    "Pharma": "pharma-healthcare", "Pharmaceuticals": "pharma-healthcare",
    "Healthcare": "pharma-healthcare", "Biotech": "pharma-healthcare",
    "Pharma/Biotech": "pharma-healthcare", "Pharma/Diagnostics": "pharma-healthcare",
    "Pharma/Oncology": "pharma-healthcare", "Pharma/Specialty": "pharma-healthcare",
    "Animal Health": "pharma-healthcare",
    "Healthcare Equipment": "healthcare-equipment",
    "Medical Devices": "healthcare-equipment",
    "Healthcare/Dental": "healthcare-equipment", "Healthcare/MedTech": "healthcare-equipment",
    "Consumer Discretionary": "consumer-discretionary",
    "Consumer Cyclical": "consumer-discretionary",
    "Retail": "consumer-discretionary", "fast-fashion-retail": "consumer-discretionary",
    "Consumer Staples": "consumer-staples", "Consumer Defensive": "consumer-staples",
    "Food & Beverage": "consumer-staples", "Household Products": "consumer-staples",
    "Beverages": "consumer-staples", "Personal Care": "consumer-staples",
    "Luxury": "luxury-goods", "Luxury Goods": "luxury-goods",
    "Insurance": "insurance", "Insurance Broker": "insurance",
    "Insurance/Broker": "insurance", "Insurance (Broker)": "insurance",
    "Insurance Data": "insurance", "Insurance/Specialty": "insurance",
    "Insurance/Specialty P&C": "insurance", "Insurance/Personal Auto": "insurance",
    "specialty-insurance": "insurance",
    "Asset Management": "asset-management",
    "Alternative Asset Management": "asset-management",
    "Financial Services": "asset-management", "asset-management": "asset-management",
    "Financial Data": "financial-data-analytics",
    "Financial Data & Analytics": "financial-data-analytics",
    "Data & Analytics": "financial-data-analytics",
    "Financial Data/Indices": "financial-data-analytics",
    "Information Services": "financial-data-analytics",
    "Research/Advisory": "financial-data-analytics",
    "Business Services": "business-services",
    "Professional Services": "business-services",
    "Pest Control/Business Services": "business-services",
    "HR/Payroll": "hr-payroll-processing",
    "HR & Payroll": "hr-payroll-processing",
    "HR/Payroll Services": "hr-payroll-processing",
    "Payments": "payments-fintech", "Payments/Fintech": "payments-fintech",
    "payments-fintech": "payments-fintech",
    "Digital Marketplaces": "digital-marketplaces",
    "Online Classifieds": "digital-marketplaces",
    "Communication Services": "telecom",
    "Media": "media-publishing", "Media/Publishing": "media-publishing",
    "Telecom": "telecom", "Telecommunications": "telecom",
    "Utilities": "utilities", "Energy": "energy", "Oil & Gas": "energy",
    "Real Estate": "real-estate", "REITs": "real-estate",
    "Property/REIT": "real-estate", "REIT": "real-estate",
    "Defense": "defense-aerospace", "Aerospace & Defense": "defense-aerospace",
    "Defense & Aerospace": "defense-aerospace", "Defense/Aerospace": "defense-aerospace",
    "defense-aerospace": "defense-aerospace",
    "Automotive": "automotive",
    "Self-Service/Vending": "self-service-vending", "Self-Service Vending": "self-service-vending",
    "Vending": "self-service-vending",
    "Environmental/Water": "environmental-water", "Water": "environmental-water",
    "Environmental Services": "environmental-water",
    "Water Treatment/Chemicals": "environmental-water",
    "Waste Management": "environmental-water",
    "Semiconductors": "semiconductors-equipment",
    "Semiconductor Equipment": "semiconductors-equipment",
    "Semiconductors/Equipment": "semiconductors-equipment",
    "Semiconductors/Power": "semiconductors-equipment",
    "Tech/Semiconductor": "semiconductors-equipment",
    "Live Entertainment": "live-entertainment", "Ticketing": "live-entertainment",
    "Security/Access Control": "security-access-control",
    "Shipping": "shipping-services", "shipping-services": "shipping-services",
    "LTL Logistics": "shipping-services", "Transportation": "shipping-services",
    "Commercial Kitchen": "commercial-kitchen-equipment",
    "commercial-kitchen-equipment": "commercial-kitchen-equipment",
    "UK Adviser Platforms": "uk-adviser-platforms",
    "financial-services": "asset-management",
}


def load_cooldowns():
    """Load R1 cooldowns from session_continuity.yaml.

    Returns dict of ticker -> cooldown entry for active (non-expired) cooldowns.
    """
    if not os.path.exists(CONTINUITY_PATH):
        return {}
    try:
        with open(CONTINUITY_PATH, "r") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return {}

    today = date.today()
    cooldowns = {}
    raw = data.get("r1_cooldowns", [])
    # Support both list format [{ticker:, cooldown_until:}] and dict format {TICKER: {date:, ...}}
    if isinstance(raw, dict):
        for ticker, info in raw.items():
            if not ticker or not isinstance(info, dict):
                continue
            cooldown_until = info.get("cooldown_until") or info.get("date", "")
            if not cooldown_until:
                continue
            try:
                cd_date = datetime.strptime(str(cooldown_until), "%Y-%m-%d").date()
                if cd_date > today:
                    cooldowns[ticker] = info
            except (ValueError, TypeError):
                continue
    else:
        for entry in raw:
            if isinstance(entry, str):
                continue
            ticker = entry.get("ticker", "")
            cooldown_until = entry.get("cooldown_until", "")
            if not ticker or not cooldown_until:
                continue
            try:
                cd_date = datetime.strptime(str(cooldown_until), "%Y-%m-%d").date()
                if cd_date > today:
                    cooldowns[ticker] = entry
            except (ValueError, TypeError):
                continue
    return cooldowns


def count_r1_complete(companies):
    """Count R1_COMPLETE long companies in universe (for auto-filter threshold)."""
    return sum(
        1 for c in companies
        if c.get("pipeline_status") == "R1_COMPLETE"
        and c.get("direction", "long") == "long"
    )


def get_dividend_yields(tickers):
    """Batch-fetch dividend yields from yfinance for E[CAGR] calculation.

    Returns dict of ticker -> dividend_yield_pct (e.g., 2.5 for 2.5%).
    Only fetches for tickers that have both fair_value and entry_price.
    Gracefully handles failures.
    """
    import warnings
    warnings.filterwarnings('ignore')

    yields = {}
    if not tickers:
        return yields

    try:
        import yfinance as yf
    except ImportError:
        return yields

    # Map tickers that have different yfinance symbols
    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

    for ticker in tickers:
        yf_ticker = TICKER_MAP.get(ticker, ticker)
        try:
            info = yf.Ticker(yf_ticker).info
            dy = info.get('dividendYield')
            if dy is not None and isinstance(dy, (int, float)) and dy >= 0:
                # yfinance dividendYield is already percentage (e.g., 2.97 = 2.97%)
                yields[ticker] = dy
            else:
                yields[ticker] = 0.0
        except Exception:
            yields[ticker] = 0.0

    return yields


def compute_ecagr(fair_value, entry_price, div_yield_pct):
    """Compute E[CAGR] = (FV/entry)^(1/3) - 1 + dividend_yield.

    Args:
        fair_value: Fair value in native currency
        entry_price: Entry price in native currency
        div_yield_pct: Dividend yield as percentage (e.g., 2.5 for 2.5%)

    Returns:
        E[CAGR] as percentage (e.g., 14.5 for 14.5%), or None if inputs invalid.
    """
    if not fair_value or not entry_price or entry_price <= 0 or fair_value <= 0:
        return None

    # MoS convergence component: (FV/entry)^(1/3) - 1
    ratio = fair_value / entry_price
    mos_cagr = (ratio ** (1.0 / 3.0)) - 1.0

    # Add dividend yield (convert from pct to decimal, then back to pct)
    div_decimal = (div_yield_pct or 0.0) / 100.0
    ecagr = (mos_cagr + div_decimal) * 100.0

    return ecagr


def get_momentum_scores(tickers, period="6mo"):
    """Fetch 6-month price momentum for ranking candidates.

    Returns dict of ticker -> momentum_pct (e.g., -15.0 for -15% over 6 months).
    Negative momentum = stock is falling = better buy opportunity for value.
    Positive momentum = stock rising = trend confirmation for quality.
    """
    import warnings
    warnings.filterwarnings('ignore')

    momentum = {}
    if not tickers:
        return momentum

    try:
        import yfinance as yf
    except ImportError:
        return momentum

    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

    for ticker in tickers:
        yf_ticker = TICKER_MAP.get(ticker, ticker)
        try:
            hist = yf.Ticker(yf_ticker).history(period=period)
            if hist is not None and len(hist) >= 2:
                start_price = hist['Close'].iloc[0]
                end_price = hist['Close'].iloc[-1]
                if start_price > 0:
                    momentum[ticker] = round(((end_price / start_price) - 1) * 100, 1)
        except Exception:
            pass

    return momentum


def rank_candidates(companies, args, auto_near_entry_applied=False):
    """Filter and rank SCORED companies for R1 processing."""
    # Filter: only SCORED, only long direction
    scored = [
        c for c in companies
        if c.get("pipeline_status") == "SCORED"
        and c.get("direction", "long") == "long"
    ]

    # Optional filters
    if args.exclude_uk:
        scored = [c for c in scored if not c["ticker"].endswith(UK_SUFFIX)]

    # Near-entry filtering (manual --near-entry-only OR auto-applied)
    if args.near_entry_only:
        scored = [
            c for c in scored
            if c.get("distance_to_entry") is not None
            and c["distance_to_entry"] <= 20.0
        ]
    elif auto_near_entry_applied and not args.include_far:
        scored = [
            c for c in scored
            if c.get("distance_to_entry") is not None
            and c["distance_to_entry"] <= 25.0
        ]

    if args.tier_a_only:
        scored = [c for c in scored if c.get("tier") == "A"]

    # Fantasy-risk filtering: exclude companies priced > 150% of FV
    if args.exclude_fantasy_risk:
        scored = [
            c for c in scored
            if not (c.get("current_price") and c.get("fair_value") and c["fair_value"] > 0
                    and c["current_price"] / c["fair_value"] > 1.50)
        ]

    # Cooldown filtering (skip recently-analyzed tickers unless price dropped >15%)
    cooled_entries = []
    if not args.ignore_cooldowns:
        cooldowns = load_cooldowns()
        filtered = []
        for c in scored:
            if c["ticker"] in cooldowns:
                cd = cooldowns[c["ticker"]]
                current = c.get("current_price") or c.get("distance_to_entry")
                analysis_price = cd.get("price_at_analysis", 0)
                # Override: if price dropped >15% since analysis, re-enable
                if analysis_price and current and c.get("current_price"):
                    drop = (analysis_price - c["current_price"]) / analysis_price
                    if drop >= 0.15:
                        c["_cooldown_override"] = True
                        filtered.append(c)
                        continue
                cooled_entries.append(cd)
            else:
                filtered.append(c)
        scored = filtered

    # Fetch momentum scores if not --no-ecagr (reuses yfinance session)
    momentum_map = {}
    if not getattr(args, 'no_ecagr', False):
        mtm_tickers = [c["ticker"] for c in scored[:args.top + 5]]  # Only top N+5 to save API calls
        if mtm_tickers:
            momentum_map = get_momentum_scores(mtm_tickers)
    args._momentum_map = momentum_map

    # Sort by composite priority:
    # 1. QS adjusted (desc) -- quality first
    # 2. Distance to entry (asc) -- closer to buy = higher priority
    # 3. Momentum bonus: positive 6mo momentum = small rank boost (tiebreaker)
    # 4. Non-UK bonus (UK companies rank slightly lower due to concentration)
    def sort_key(c):
        qs = c.get("qs_adj") or c.get("qs_tool") or 0
        dist = c.get("distance_to_entry")
        dist_val = dist if dist is not None else 999

        # UK penalty: +50 to distance for sorting purposes
        uk_penalty = 50 if c["ticker"].endswith(UK_SUFFIX) else 0

        # Momentum tiebreaker: positive momentum reduces effective distance by up to 5pts
        mtm = momentum_map.get(c["ticker"], 0)
        mtm_bonus = min(max(mtm / 10, -5), 5)  # cap at +/-5 distance points

        # Primary: QS descending (negate), Secondary: distance ascending (momentum-adjusted)
        return (-qs, dist_val + uk_penalty - mtm_bonus)

    scored.sort(key=sort_key)

    # Store cooled entries for footer display
    args._cooled_entries = cooled_entries

    return scored[:args.top]


def compute_ecagr_at_market(fair_value, current_price, div_yield_pct):
    """Compute E[CAGR] using current market price instead of entry price.

    E[CAGR]-at-market = (FV/current_price)^(1/3) - 1 + dividend_yield

    This answers: "What return would I get if I bought TODAY?"
    """
    if not fair_value or not current_price or current_price <= 0 or fair_value <= 0:
        return None

    ratio = fair_value / current_price
    mos_cagr = (ratio ** (1.0 / 3.0)) - 1.0
    div_decimal = (div_yield_pct or 0.0) / 100.0
    ecagr = (mos_cagr + div_decimal) * 100.0
    return round(ecagr, 1)


def show_advancement_pipeline(companies, near_entry_only=False):
    """Show R1_COMPLETE candidates organized by deployment readiness.

    Three sections:
      A. READY FOR ADVANCEMENT: distance_to_entry <= 20% OR E[CAGR]-at-market >= threshold
      B. APPROACHING: distance_to_entry 20-35%. Monitor zone.
      C. PARKED: distance_to_entry > 35% or FANTASY verdict. Count only.
    """
    r1_complete = [
        c for c in companies
        if c.get("pipeline_status") == "R1_COMPLETE"
        and c.get("direction", "long") == "long"
    ]

    if not r1_complete:
        print("\nNo R1_COMPLETE candidates in universe.")
        return

    # Check which ones already have R2/R3 completed (from session_continuity)
    continuity_r2 = set()
    continuity_r3 = set()
    if os.path.exists(CONTINUITY_PATH):
        try:
            with open(CONTINUITY_PATH, "r") as f:
                cont = yaml.safe_load(f) or {}
            completed = cont.get("completed", {})
            for item in completed.get("r2_completed", []):
                continuity_r2.add(item.get("ticker", ""))
            for item in completed.get("r3_completed", []):
                continuity_r3.add(item.get("ticker", ""))
        except Exception:
            pass

    # Fetch dividend yields for E[CAGR]-at-market computation
    ecagr_tickers = [c["ticker"] for c in r1_complete if c.get("fair_value") and c.get("current_price")]
    div_yields = {}
    if ecagr_tickers:
        print(f"Fetching dividend yields for {len(ecagr_tickers)} R1_COMPLETE tickers...")
        div_yields = get_dividend_yields(ecagr_tickers)

    # Compute E[CAGR]-at-market for each
    ecagr_market = {}  # ticker -> ecagr_pct
    for c in r1_complete:
        ticker = c["ticker"]
        fv = c.get("fair_value")
        cp = c.get("current_price")
        if fv and cp and fv > 0 and cp > 0:
            dy = div_yields.get(ticker, 0.0)
            ecagr = compute_ecagr_at_market(fv, cp, dy)
            if ecagr is not None:
                ecagr_market[ticker] = ecagr

    # Classify into three sections
    section_a = []  # READY FOR ADVANCEMENT
    section_b = []  # APPROACHING
    section_c = []  # PARKED

    for c in r1_complete:
        ticker = c["ticker"]
        dist = c.get("distance_to_entry")
        verdict = c.get("r1_verdict", "")
        ecagr = ecagr_market.get(ticker)
        tier = c.get("tier", "B")
        ecagr_threshold = 12.0 if tier == "A" else 15.0

        # Section A: near entry OR economically viable at current price
        if dist is not None and dist <= 20.0:
            section_a.append(c)
        elif ecagr is not None and ecagr >= ecagr_threshold:
            section_a.append(c)
        # Section B: approaching
        elif dist is not None and 20.0 < dist <= 35.0:
            section_b.append(c)
        # Section C: parked (far away or fantasy)
        else:
            section_c.append(c)

    if near_entry_only:
        # Quick mode: only show section A
        section_b = []
        section_c = []

    today = date.today()
    print(f"\n=== ADVANCEMENT PIPELINE | {today} ===")
    print(f"R1_COMPLETE total: {len(r1_complete)} | Ready: {len(section_a)} | Approaching: {len(section_b)} | Parked: {len(section_c)}")
    print("=" * 130)

    def _get_status(ticker):
        if ticker in continuity_r3:
            return "R3 DONE → R4"
        elif ticker in continuity_r2:
            return "R2 DONE → R3"
        else:
            return "needs R2"

    def _print_section(label, items):
        if not items:
            print(f"\n{label}: None")
            return

        # Sort by E[CAGR]-at-market descending (best opportunities first), then QS
        items.sort(key=lambda c: (
            -(ecagr_market.get(c["ticker"]) or -999),
            -(c.get("qs_adj") or c.get("qs_tool") or 0),
        ))

        print(f"\n{label} ({len(items)}):")
        print(f"{'#':>2} {'Ticker':<14} {'QS':>3} {'Tier':>4} {'Sector':<20} {'Dist%':>7} {'E[CAGR]@mkt':>12} {'Verdict':<12} {'Status'}")
        print("-" * 130)

        for i, c in enumerate(items, 1):
            qs = c.get("qs_adj") or c.get("qs_tool") or "?"
            tier = c.get("tier", "?")
            sector = (c.get("sector") or "Unknown")[:20]
            dist = c.get("distance_to_entry")
            dist_str = f"{dist:+.1f}%" if dist is not None else "N/A"
            ecagr = ecagr_market.get(c["ticker"])
            ecagr_str = f"{ecagr:.1f}%" if ecagr is not None else "-"
            verdict = c.get("r1_verdict", "?")
            ticker = c["ticker"]
            status = _get_status(ticker)

            # Add gate info if present
            gate = c.get("gate") or c.get("pre_execution_condition") or ""
            if gate:
                status += f" (GATE: {gate[:30]})"

            print(f"{i:>2} {ticker:<14} {qs:>3} {tier:>4} {sector:<20} {dist_str:>7} {ecagr_str:>12} {verdict:<12} {status}")

    _print_section("SECTION A — READY FOR ADVANCEMENT (dist<=20% OR E[CAGR]>=threshold)", section_a)
    _print_section("SECTION B — APPROACHING (dist 20-35%)", section_b)

    if section_c:
        print(f"\nSECTION C — PARKED ({len(section_c)} companies, dist>35% or no data):")
        # Just show count + top 5 by QS for reference
        section_c.sort(key=lambda c: -(c.get("qs_adj") or c.get("qs_tool") or 0))
        for c in section_c[:5]:
            qs = c.get("qs_adj") or c.get("qs_tool") or "?"
            dist = c.get("distance_to_entry")
            dist_str = f"{dist:+.1f}%" if dist is not None else "N/A"
            verdict = c.get("r1_verdict", "?")
            print(f"  {c['ticker']:<14} QS {qs:>3} {dist_str:>7} {verdict}")
        if len(section_c) > 5:
            print(f"  ... and {len(section_c) - 5} more")

    print(f"\n  E[CAGR]@mkt = (FV/current_price)^(1/3) - 1 + div_yield. Threshold: >=12% Tier A, >=15% Tier B.")
    print(f"[Pipeline velocity: 1 R1 = 1 unit, 1 R2->R3 = 2 units, 1 R4 = 1 unit. Target: 3+ units/session]")


def show_buyable_now(companies):
    """Reverse pipeline mode: what's buyable at market price TODAY?

    Filters ALL universe companies (any pipeline_status with FV defined) to those where
    E[CAGR]@market exceeds deployment threshold. Answers: "If I had cash to deploy,
    what should I buy RIGHT NOW?"
    """
    # Filter: long direction, has FV and current_price
    candidates = [
        c for c in companies
        if c.get("direction", "long") == "long"
        and c.get("fair_value") and c.get("current_price")
        and c["fair_value"] > 0 and c["current_price"] > 0
    ]

    if not candidates:
        print("\nNo candidates with FV and current price in universe.")
        return

    # Fetch dividend yields for E[CAGR] computation
    tickers = [c["ticker"] for c in candidates]
    print(f"Fetching dividend yields for {len(tickers)} candidates...")
    div_yields = get_dividend_yields(tickers)

    # Compute E[CAGR]@market and filter by threshold
    buyable = []
    for c in candidates:
        ticker = c["ticker"]
        fv = c["fair_value"]
        cp = c["current_price"]
        dy = div_yields.get(ticker, 0.0)
        ecagr = compute_ecagr_at_market(fv, cp, dy)
        if ecagr is None:
            continue

        tier = c.get("tier", "B")
        threshold = 12.0 if tier == "A" else 15.0

        if ecagr >= threshold:
            c["_ecagr_market"] = ecagr
            c["_threshold"] = threshold
            c["_div_yield"] = dy
            buyable.append(c)

    today = date.today()
    print(f"\n=== BUYABLE NOW — Market Price Deployment Candidates | {today} ===")
    print(f"Universe scanned: {len(candidates)} with FV | Buyable: {len(buyable)}")
    print("=" * 140)

    if not buyable:
        print("\nNo candidates meet E[CAGR]@market threshold at current prices.")
        print("  Tier A needs >= 12%, Tier B needs >= 15%.")
        return

    # Sort by E[CAGR] descending
    buyable.sort(key=lambda c: -c["_ecagr_market"])

    print(f"{'#':>2} {'Ticker':<14} {'QS':>3} {'Tier':>4} {'Sector':<20} {'Price':>8} {'FV':>8} {'MoS%':>7} {'E[CAGR]':>8} {'Pipeline':<14} {'Flags'}")
    print("-" * 140)

    for i, c in enumerate(buyable, 1):
        qs = c.get("qs_adj") or c.get("qs_tool") or "?"
        tier = c.get("tier", "?")
        sector = (c.get("sector") or "Unknown")[:20]
        cp = c["current_price"]
        fv = c["fair_value"]
        mos = ((fv - cp) / cp) * 100
        ecagr = c["_ecagr_market"]
        pipeline = c.get("pipeline_status", "?")

        flags = []
        if c["ticker"] in ETORO_UNAVAILABLE:
            flags.append("NO-ETORO")
        if c["ticker"].endswith(UK_SUFFIX):
            flags.append("UK")
        gate = c.get("gate") or c.get("pre_execution_condition") or ""
        if gate:
            flags.append(f"GATE")
        flags_str = " | ".join(flags) if flags else ""

        print(f"{i:>2} {c['ticker']:<14} {qs:>3} {tier:>4} {sector:<20} {cp:>8.1f} {fv:>8.1f} {mos:>+6.1f}% {ecagr:>7.1f}% {pipeline:<14} {flags_str}")

    print("-" * 140)
    print(f"\nE[CAGR]@market = (FV/price)^(1/3) - 1 + div_yield. Thresholds: Tier A >= 12%, Tier B >= 15%.")
    print(f"[Reverse pipeline: these are BUYABLE at today's market price. Apply market-buy-protocol gates.]")


def load_smart_money_signals(tickers):
    """Load smart money signal codes for each ticker from graph.

    Returns dict of ticker -> (code, priority_adj):
      IC = insider cluster buy (+2)
      CV = convergence: 2+ quality funds (+2)
      QA = quiet accumulation (+3)
      FC = founder conviction (+1)
      HW = herd warning (-1)
      SE = short escalation (-2)
      SQ = squeeze risk (0, informational)
    """
    import json
    import networkx as nx

    if not os.path.exists(GRAPH_PATH):
        return {}

    try:
        with open(GRAPH_PATH) as f:
            data = json.load(f)
        G = nx.node_link_graph(data, directed=True, multigraph=True)
    except Exception:
        return {}

    results = {}

    for ticker in tickers:
        if ticker not in G.nodes:
            continue

        codes = []
        adj = 0

        # Gather edges
        holders = []
        shorts = []
        insider_buys_60d = []
        insider_buys_90d = []

        for u, v, k, d in G.in_edges(ticker, data=True, keys=True):
            rel = d.get("relation", "")
            if rel == "holds":
                holders.append((u, d))
            elif rel == "shorts":
                shorts.append((u, d))
            elif rel == "insider_buy":
                buy_date = d.get("date", "")
                if buy_date:
                    try:
                        from datetime import datetime as _dt, date as _d
                        bd = _dt.strptime(str(buy_date)[:10], "%Y-%m-%d").date()
                        days = (_d.today() - bd).days
                        if days <= 60:
                            insider_buys_60d.append((u, d))
                        if days <= 90:
                            insider_buys_90d.append((u, d))
                    except (ValueError, TypeError):
                        pass

        total_si = sum(s[1].get("pct_shares", 0) or 0 for s in shorts)
        quality_holders = [h for h in holders if G.nodes.get(h[0], {}).get("fund_type") in ("value", "quality", "activist")]

        # Insider Cluster Buy
        if len(insider_buys_60d) >= 3:
            codes.append("IC")
            adj += 2

        # Convergence
        if len(quality_holders) >= 2:
            codes.append("CV")
            adj += 2

        # Quiet Accumulation
        if holders and total_si < 3 and insider_buys_90d:
            codes.append("QA")
            adj += 3

        # Founder Conviction
        for _, ed in insider_buys_90d:
            role = (ed.get("role", "") or "").lower()
            value = ed.get("value", 0) or 0
            if value >= 100000 and any(w in role for w in ["ceo", "chief executive", "founder", "chairman"]):
                codes.append("FC")
                adj += 1
                break

        # Herd Warning
        if len(holders) >= 5:
            codes.append("HW")
            adj -= 1

        # Short Escalation
        if total_si > 8 and len(shorts) >= 5:
            codes.append("SE")
            adj -= 2

        # Squeeze Risk
        if total_si > 10 and quality_holders and insider_buys_90d:
            codes.append("SQ")

        if codes:
            results[ticker] = (",".join(codes), adj)

    return results


def _git_file_date(filepath):
    """Get last git commit date for a file. Falls back to mtime."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%aI", "--", filepath],
            capture_output=True, text=True, timeout=10,
            cwd=PROJECT_ROOT,
        )
        iso = result.stdout.strip()
        if iso:
            # Parse ISO date like 2026-03-18T09:34:47+01:00
            return datetime.fromisoformat(iso).date()
    except Exception:
        pass
    # Fallback: file mtime
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.fromtimestamp(mtime).date()
    except Exception:
        return None


def show_stagnation_report():
    """Pipeline stagnation report: scan thesis/research/* for canonical files
    and flag items stuck at a pipeline stage for >14 days."""

    CANONICAL_FILES = [
        ("thesis.md", "R1"),
        ("devils_advocate.md", "R2"),
        ("r3_resolution.md", "R3"),
        ("committee_decision.md", "R4"),
    ]

    today = date.today()

    # Scan all research directories
    if not os.path.isdir(RESEARCH_DIR):
        print("No thesis/research/ directory found.")
        return

    entries = []  # list of dicts: {ticker, files: {stage: date}, current_stage, last_date, days_stale}

    for dirname in sorted(os.listdir(RESEARCH_DIR)):
        dirpath = os.path.join(RESEARCH_DIR, dirname)
        if not os.path.isdir(dirpath) or dirname.startswith("_") or dirname == "ANALYSIS_NOTES":
            continue

        files_found = {}  # stage -> date
        for filename, stage in CANONICAL_FILES:
            fpath = os.path.join(dirpath, filename)
            if os.path.isfile(fpath):
                fdate = _git_file_date(fpath)
                if fdate:
                    files_found[stage] = fdate

        if not files_found:
            continue

        # Determine current stage (highest canonical file present)
        stage_order = ["R1", "R2", "R3", "R4"]
        current_stage = None
        for s in reversed(stage_order):
            if s in files_found:
                current_stage = s
                break

        # Last advancement date = date of the most recent file
        last_date = max(files_found.values())
        days_since = (today - last_date).days

        # Next expected stage
        stage_idx = stage_order.index(current_stage)
        next_stage = stage_order[stage_idx + 1] if stage_idx < len(stage_order) - 1 else None

        entries.append({
            "ticker": dirname,
            "files": files_found,
            "current_stage": current_stage,
            "next_stage": next_stage,
            "last_date": last_date,
            "days_since": days_since,
        })

    # Group by current stage (only those that still need advancement -- not R4)
    stage_groups = {"R1": [], "R2": [], "R3": []}
    r4_complete = []

    for e in entries:
        cs = e["current_stage"]
        if cs == "R4":
            r4_complete.append(e)
        elif cs in stage_groups:
            stage_groups[cs].append(e)

    # Print report
    print(f"PIPELINE STAGNATION REPORT | {today}")
    print("=" * 70)

    for stage in ["R1", "R2", "R3"]:
        next_s = {"R1": "R2", "R2": "R3", "R3": "R4"}[stage]
        items = stage_groups[stage]
        items.sort(key=lambda e: e["days_since"], reverse=True)

        overdue = [e for e in items if e["days_since"] > 14]
        ok = [e for e in items if e["days_since"] <= 14]

        print(f"\n  {stage} without {next_s} ({len(items)}):")
        if not items:
            print(f"    (none)")
            continue

        for e in items:
            ticker = e["ticker"]
            stage_date = e["last_date"].strftime("%Y-%m-%d")
            days = e["days_since"]
            if days > 14:
                label = f"OVERDUE ({days}d)"
            elif days > 10:
                label = f"APPROACHING ({days}d)"
            else:
                label = f"OK ({days}d)"
            print(f"    {ticker:<14} {stage}: {stage_date}  {label}")

    # Conversion funnel
    total_r1 = sum(1 for e in entries if "R1" in e["files"])
    total_r2 = sum(1 for e in entries if "R2" in e["files"])
    total_r3 = sum(1 for e in entries if "R3" in e["files"])
    total_r4 = sum(1 for e in entries if "R4" in e["files"])

    r1_to_r2 = (total_r2 / total_r1 * 100) if total_r1 > 0 else 0
    r2_to_r3 = (total_r3 / total_r2 * 100) if total_r2 > 0 else 0
    r3_to_r4 = (total_r4 / total_r3 * 100) if total_r3 > 0 else 0
    r1_to_r4 = (total_r4 / total_r1 * 100) if total_r1 > 0 else 0

    # Find bottleneck (lowest conversion rate among stages with items)
    rates = []
    if total_r1 > 0:
        rates.append(("R1->R2", r1_to_r2))
    if total_r2 > 0:
        rates.append(("R2->R3", r2_to_r3))
    if total_r3 > 0:
        rates.append(("R3->R4", r3_to_r4))
    bottleneck = min(rates, key=lambda x: x[1]) if rates else ("N/A", 0)

    print(f"\nCONVERSION FUNNEL:")
    print(f"  thesis.md:              {total_r1:>3} companies")
    print(f"  + devils_advocate.md:   {total_r2:>3} companies ({r1_to_r2:.1f}% conversion R1->R2)")
    print(f"  + r3_resolution.md:     {total_r3:>3} companies ({r2_to_r3:.1f}% conversion R2->R3)")
    print(f"  + committee_decision.md:{total_r4:>3} companies ({r3_to_r4:.1f}% conversion R3->R4)")
    print(f"")
    print(f"  Overall R1->R4:         {r1_to_r4:.1f}%")
    print(f"  Bottleneck:             {bottleneck[0]} ({bottleneck[1]:.1f}%)")

    # Overdue summary
    all_overdue = [e for e in entries if e["current_stage"] != "R4" and e["days_since"] > 14]
    if all_overdue:
        all_overdue.sort(key=lambda e: e["days_since"], reverse=True)
        print(f"\nOVERDUE (>14d at current stage):")
        for e in all_overdue:
            next_s = e["next_stage"] or "?"
            print(f"  {e['ticker']:<14} {e['current_stage']} done {e['last_date'].strftime('%Y-%m-%d')} "
                  f"({e['days_since']}d without {next_s})")
    else:
        print(f"\nNo overdue items. All pipeline items within 14d threshold.")

    print(f"\n[Raw data. Pipeline velocity context.]")



def main():
    parser = argparse.ArgumentParser(description="R1 Prioritizer -- Rank SCORED companies for R1 analysis")
    parser.add_argument("--top", type=int, default=10, help="Number of candidates to show (default: 10)")
    parser.add_argument("--exclude-uk", action="store_true", help="Exclude UK tickers (.L)")
    parser.add_argument("--near-entry-only", action="store_true", help="Only show companies within 20%% of entry (forced)")
    parser.add_argument("--include-far", action="store_true", help="Override auto near-entry filter (show all distances)")
    parser.add_argument("--tier-a-only", action="store_true", help="Only show Tier A (QS >= 75)")
    parser.add_argument("--ignore-cooldowns", action="store_true", help="Bypass R1 cooldowns (show all including recently analyzed)")
    parser.add_argument("--advancement", action="store_true", help="Show R1_COMPLETE candidates for R2+ advancement (3 sections)")
    parser.add_argument("--no-ecagr", action="store_true", help="Skip E[CAGR] calculation (avoids yfinance calls)")
    parser.add_argument("--exclude-fantasy-risk", action="store_true", help="Filter out FANTASY-RISK entries (price > 150%% of FV)")
    parser.add_argument("--pre-flight", action="store_true", help="Only show candidates with E[CAGR]-at-entry >= 12%% (worth doing R1)")
    parser.add_argument("--near-entry-advancement", action="store_true", help="Quick check: advancement pipeline candidates near entry")
    parser.add_argument("--buyable-now", action="store_true", help="Reverse mode: what's buyable at market price today? (E[CAGR]@market > threshold)")
    parser.add_argument("--smart-money", action="store_true", help="Add Smart Money overlay from graph signals (insider, convergence, shorts)")
    parser.add_argument("--stagnation", action="store_true", help="Pipeline stagnation report: flag items stuck >14d at current stage")
    args = parser.parse_args()
    args._cooled_entries = []  # populated by rank_candidates

    companies = load_universe()
    if not companies:
        print("Quality Universe is empty.")
        sys.exit(1)

    # --buyable-now mode: reverse pipeline — what's buyable at market today?
    if args.buyable_now:
        show_buyable_now(companies)
        sys.exit(0)

    # --stagnation mode: pipeline stagnation report
    if args.stagnation:
        show_stagnation_report()
        sys.exit(0)

    # --advancement mode: show R1_COMPLETE candidates for R2+ advancement
    if args.advancement or args.near_entry_advancement:
        show_advancement_pipeline(companies, near_entry_only=args.near_entry_advancement)
        sys.exit(0)

    # Count totals
    all_scored = [c for c in companies if c.get("pipeline_status") == "SCORED" and c.get("direction", "long") == "long"]
    total_universe = len([c for c in companies if c.get("direction", "long") == "long"])

    # Auto near-entry filter: when R1_COMPLETE count >= 20, focus on near-entry
    r1_complete_count = count_r1_complete(companies)
    auto_near_entry_applied = False
    if r1_complete_count >= 20 and not args.near_entry_only and not args.include_far:
        auto_near_entry_applied = True

    # Load earnings calendar + stale sector views
    earnings = load_earnings_tickers(30)
    stale_sectors = get_stale_sector_views()

    # Rank
    candidates = rank_candidates(companies, args, auto_near_entry_applied)

    if not candidates:
        msg = f"\nNo SCORED candidates match filters. Total SCORED: {len(all_scored)}/{total_universe}"
        if auto_near_entry_applied:
            msg += "\n  Auto-filter applied (R1_COMPLETE >= 20, distance <= 25%). Use --include-far to see all."
        print(msg)
        sys.exit(0)

    # E[CAGR] computation (only when not --no-ecagr)
    ecagr_map = {}  # ticker -> ecagr_pct
    if not args.no_ecagr:
        # Collect tickers that need E[CAGR] (have both FV and entry_price)
        ecagr_tickers = []
        for c in candidates:
            fv = c.get("fair_value")
            ep = c.get("entry_price")
            if fv and ep and fv > 0 and ep > 0:
                ecagr_tickers.append(c["ticker"])

        # Batch-fetch dividend yields for E[CAGR] calculation
        div_yields = {}
        if ecagr_tickers:
            print(f"Fetching dividend yields for {len(ecagr_tickers)} tickers...")
            div_yields = get_dividend_yields(ecagr_tickers)

        # Compute E[CAGR] for each candidate
        for c in candidates:
            ticker = c["ticker"]
            fv = c.get("fair_value")
            ep = c.get("entry_price")
            if fv and ep and fv > 0 and ep > 0:
                dy = div_yields.get(ticker, 0.0)
                ecagr = compute_ecagr(fv, ep, dy)
                if ecagr is not None:
                    ecagr_map[ticker] = ecagr

    # Pre-flight filter: only show candidates worth investing R1 effort
    if args.pre_flight and ecagr_map:
        pre_flight_candidates = []
        for c in candidates:
            ecagr = ecagr_map.get(c["ticker"])
            if ecagr is None:
                continue  # Skip if no E[CAGR] data
            tier = c.get("tier", "B")
            threshold = 12.0 if tier == "A" else 15.0
            if ecagr >= threshold:
                pre_flight_candidates.append(c)
        candidates = pre_flight_candidates

    if not candidates:
        print("\nNo candidates pass pre-flight E[CAGR] filter.")
        print("  Tier A needs E[CAGR]-at-entry >= 12%, Tier B needs >= 15%.")
        sys.exit(0)

    # Determine if we show E[CAGR] column (at least one computed)
    show_ecagr = len(ecagr_map) > 0

    # Smart money overlay
    sm_signals = {}
    show_sm = False
    if args.smart_money:
        sm_tickers = [c["ticker"] for c in candidates]
        sm_signals = load_smart_money_signals(sm_tickers)
        show_sm = bool(sm_signals)
        if show_sm:
            print(f"\nSmart Money overlay: {len(sm_signals)} tickers with signals")

    # Print header
    today = date.today()
    print(f"\nR1 PRIORITY QUEUE | {today}")
    print(f"SCORED: {len(all_scored)}/{total_universe} long companies need R1")

    if auto_near_entry_applied:
        print(f"Auto-filtered to near-entry (R1_COMPLETE >= 20, dist <= 25%). Use --include-far to see all.")

    col_width = 140 if (show_ecagr and show_sm) else 130 if (show_ecagr or show_sm) else 120
    print("=" * col_width)

    sm_col = f" {'SM':>8}" if show_sm else ""
    ecagr_col = f" {'E[CAGR]':>8}" if show_ecagr else ""
    momentum_map = getattr(args, '_momentum_map', {})
    show_mtm = bool(momentum_map)
    mtm_col = f" {'Mtm6m':>7}" if show_mtm else ""
    if show_mtm:
        col_width += 8
    print(f"{'#':>2} {'Ticker':<12} {'QS':>3} {'Tier':>4} {'Sector':<24} {'Dist%':>7}{ecagr_col}{mtm_col}{sm_col} {'Currency':>8} {'Flags'}")
    print("-" * col_width)

    for i, c in enumerate(candidates, 1):
        qs = c.get("qs_adj") or c.get("qs_tool") or "?"
        tier = c.get("tier", "?")
        sector = (c.get("sector") or "Unknown")[:24]
        dist = c.get("distance_to_entry")
        dist_str = f"{dist:+.1f}%" if dist is not None else "N/A"
        currency = c.get("currency", "USD")

        # E[CAGR] string
        ecagr_val = ecagr_map.get(c["ticker"])
        ecagr_str = f"{ecagr_val:.1f}%" if ecagr_val is not None else "-"

        # Build flags
        flags = []

        # eToro availability
        if c["ticker"] in ETORO_UNAVAILABLE:
            flags.append("NO-ETORO")

        # UK concentration warning
        if c["ticker"].endswith(UK_SUFFIX):
            flags.append("UK#5")

        # Earnings gate
        if c["ticker"] in earnings:
            earn_date = earnings[c["ticker"]]
            flags.append(f"EARNINGS {earn_date.strftime('%b %d')}")

        # Near entry highlight
        if dist is not None and dist <= 15.0:
            flags.append("NEAR-ENTRY")

        # Fantasy-risk: current price far above fair value
        fv = c.get("fair_value")
        cp = c.get("current_price")
        if fv and cp and fv > 0 and cp > 0:
            price_vs_fv = cp / fv
            if price_vs_fv > 1.50:
                flags.append(f"FANTASY-RISK({price_vs_fv:.0%})")
            elif price_vs_fv > 1.25:
                flags.append(f"EXPENSIVE({price_vs_fv:.0%})")

        # Stale score warning
        last_scored = c.get("last_scored")
        if last_scored:
            try:
                scored_date = datetime.strptime(str(last_scored), "%Y-%m-%d").date()
                days_stale = (today - scored_date).days
                if days_stale > 90:
                    flags.append(f"STALE({days_stale}d)")
            except (ValueError, TypeError):
                pass

        # Stale sector view warning
        sector_label = c.get("sector", "")
        sector_file = _SECTOR_TO_FILE.get(sector_label)
        if sector_file:
            sf_name = sector_file + ".md"
            if sf_name in stale_sectors:
                flags.append(f"STALE-SECTOR({stale_sectors[sf_name]}d)")
        elif sector_label:
            # No mapping found -- might be missing sector view
            expected = sector_label.lower().replace("/", "-").replace(" ", "-") + ".md"
            sector_files = set(os.listdir(SECTORS_DIR)) if os.path.isdir(SECTORS_DIR) else set()
            if expected not in sector_files:
                flags.append("NO-SECTOR-VIEW")

        # Smart money signal code
        sm_code = ""
        if show_sm:
            sm_entry = sm_signals.get(c["ticker"])
            sm_code = sm_entry[0] if sm_entry else "-"

        flags_str = " | ".join(flags) if flags else ""

        ecagr_part = f" {ecagr_str:>8}" if show_ecagr else ""
        mtm_val = momentum_map.get(c["ticker"])
        mtm_str = f"{mtm_val:+.0f}%" if mtm_val is not None else "-"
        mtm_part = f" {mtm_str:>7}" if show_mtm else ""
        sm_part = f" {sm_code:>8}" if show_sm else ""
        print(f"{i:>2} {c['ticker']:<12} {qs:>3} {tier:>4} {sector:<24} {dist_str:>7}{ecagr_part}{mtm_part}{sm_part} {currency:>8}  {flags_str}")

    # Summary
    print("-" * col_width)
    print(f"Showing {len(candidates)}/{len(all_scored)} SCORED candidates")

    # Tier breakdown of all scored
    tier_a_scored = sum(1 for c in all_scored if c.get("tier") == "A")
    tier_b_scored = sum(1 for c in all_scored if c.get("tier") == "B")
    near_entry_scored = sum(1 for c in all_scored if c.get("distance_to_entry") is not None and c["distance_to_entry"] <= 20.0)
    uk_scored = sum(1 for c in all_scored if c["ticker"].endswith(UK_SUFFIX))

    print(f"\nAll SCORED breakdown:")
    print(f"  Tier A: {tier_a_scored} | Tier B: {tier_b_scored} | Near entry (<20%%): {near_entry_scored} | UK: {uk_scored}")
    print(f"  R1_COMPLETE in universe: {r1_complete_count}")

    if show_ecagr:
        print(f"\nE[CAGR] = (FV/entry)^(1/3) - 1 + div_yield. Threshold: >=12% Tier A, >=15% Tier B.")

    if show_sm:
        print(f"\nSM codes: IC=insider cluster(+2), CV=convergence(+2), QA=quiet accum(+3), "
              f"FC=founder conviction(+1), HW=herd warning(-1), SE=short escalation(-2), SQ=squeeze risk(0)")

    if earnings:
        earning_scored = [t for t in earnings if any(c["ticker"] == t and c.get("pipeline_status") == "SCORED" for c in companies)]
        if earning_scored:
            print(f"  Earnings gate (next 30d): {', '.join(earning_scored)}")

    # Cooldown footer
    cooled = getattr(args, "_cooled_entries", [])
    if cooled:
        print(f"\nCOOLDOWN SKIPPED ({len(cooled)}):")
        for cd in sorted(cooled, key=lambda x: x.get("cooldown_until", "")):
            t = cd.get("ticker", "?")
            v = cd.get("verdict", "?")
            s = cd.get("session", "?")
            cu = cd.get("cooldown_until", "?")
            print(f"  {t:<14} {v:<14} S{s}  cooldown until {cu}")
        print(f"  [Use --ignore-cooldowns to bypass]")

    # Fantasy rate: % of R1_COMPLETE that are OVERVALUED/FANTASY
    r1_complete_all = [
        c for c in companies
        if c.get("pipeline_status") == "R1_COMPLETE"
        and c.get("direction", "long") == "long"
        and c.get("r1_verdict")
    ]
    if r1_complete_all:
        fantasy_verdicts = sum(1 for c in r1_complete_all if c.get("r1_verdict") in ("OVERVALUED", "FANTASY"))
        fantasy_rate = fantasy_verdicts / len(r1_complete_all) * 100
        rate_label = "ALARM" if fantasy_rate > 50 else "OK"
        print(f"\nFANTASY RATE: {fantasy_rate:.0f}% ({fantasy_verdicts}/{len(r1_complete_all)} R1s → OVERVALUED/FANTASY) [{rate_label}]")
        if fantasy_rate > 50:
            print("  WARNING: >50%. Use --exclude-fantasy-risk or --near-entry-only or --pre-flight to focus.")

    print(f"\n[Raw data. Select 3-5 for R1 processing this session.]")


if __name__ == "__main__":
    main()

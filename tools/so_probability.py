#!/usr/bin/env python3
"""
Standing Order Fill Probability Calculator

Calculates the probability that each standing order will fill within 6 months
using historical volatility and a lognormal distribution model.

For LONG orders: price needs to FALL to trigger (prob of hitting lower barrier)
For SHORT orders: price needs to RISE to trigger (prob of hitting upper barrier)

Uses the reflection principle for barrier-hitting probability of geometric
Brownian motion: P(min S_t <= K) over [0,T] for longs.

Classification:
  REALISTIC  : >40% fill probability
  POSSIBLE   : 20-40%
  BORDERLINE : 10-20%
  FANTASY    : <10%

Usage:
  python3 tools/so_probability.py                # All standing orders
  python3 tools/so_probability.py --active-only  # Only ACTIVE category
  python3 tools/so_probability.py --include-extreme  # Include EXTREME watchlist
  python3 tools/so_probability.py --horizon 12   # 12-month horizon instead of 6
  python3 tools/so_probability.py --freshness    # Thesis freshness check per SO
"""

import sys
import os
import argparse
import math
import subprocess
from datetime import date, datetime

import yaml
import yfinance as yf
from scipy.stats import norm
import numpy as np
import warnings
warnings.filterwarnings('ignore')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
SO_PATH = os.path.join(PROJECT_ROOT, "state", "standing_orders.yaml")
TRACKER_PATH = os.path.join(PROJECT_ROOT, "state", "meta_reflection_tracker.yaml")


def load_standing_orders():
    """Load standing orders from YAML file."""
    if not os.path.exists(SO_PATH):
        print(f"ERROR: {SO_PATH} not found")
        sys.exit(1)
    with open(SO_PATH, "r") as f:
        data = yaml.safe_load(f) or {}
    return data


def parse_trigger_price(trigger_str):
    """Parse trigger string like '<=EUR 295', '<=$88', '<=950 GBp', '<=CHF 80'.

    Returns (price_float, currency_hint) or (None, None) if unparseable.
    """
    if not trigger_str or not isinstance(trigger_str, str):
        return None, None

    # Remove comparison operators
    cleaned = trigger_str.replace("<=", "").replace(">=", "").strip()

    # Try to extract currency and number
    currency_hint = None

    # EUR prefix
    if cleaned.startswith("EUR"):
        currency_hint = "EUR"
        cleaned = cleaned.replace("EUR", "").strip()
    # CHF prefix
    elif cleaned.startswith("CHF"):
        currency_hint = "CHF"
        cleaned = cleaned.replace("CHF", "").strip()
    # USD / $ prefix
    elif cleaned.startswith("$"):
        currency_hint = "USD"
        cleaned = cleaned.replace("$", "").strip()
    # GBp suffix
    elif "GBp" in cleaned or "GBP" in cleaned:
        currency_hint = "GBp"
        cleaned = cleaned.replace("GBp", "").replace("GBP", "").strip()

    # Extract numeric value
    try:
        price = float(cleaned.replace(",", ""))
        return price, currency_hint
    except (ValueError, TypeError):
        return None, None


def get_annualized_volatility(ticker, days=252):
    """Calculate annualized volatility from daily returns.

    Uses 1 year of daily data by default. Falls back to shorter periods.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y", auto_adjust=True)
        if hist.empty or len(hist) < 30:
            # Try 6 months
            hist = stock.history(period="6mo", auto_adjust=True)
        if hist.empty or len(hist) < 20:
            return None

        # Daily log returns
        closes = hist['Close'].dropna()
        if len(closes) < 20:
            return None

        log_returns = np.log(closes / closes.shift(1)).dropna()
        daily_vol = log_returns.std()
        annual_vol = daily_vol * math.sqrt(252)
        return annual_vol

    except Exception:
        return None


def get_current_price(ticker):
    """Get current price via yfinance."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = (
            info.get('currentPrice')
            or info.get('regularMarketPrice')
            or info.get('previousClose')
        )
        currency = info.get('currency', '?')
        return price, currency
    except Exception:
        return None, None


def fill_probability_long(current_price, trigger_price, annual_vol, horizon_years=0.5, drift=-0.0):
    """Calculate probability that stock price hits trigger (below current) within horizon.

    Uses the reflection principle for geometric Brownian motion:
    P(min_{0<=t<=T} S_t <= K) where K < S_0

    For a GBM with drift mu and vol sigma:
    P(min S_t <= K) = N(d1) + exp(2*mu*ln(K/S0)/sigma^2) * N(d2)

    where:
      d1 = (ln(K/S0) - mu*T) / (sigma*sqrt(T))
      d2 = (ln(K/S0) + mu*T) / (sigma*sqrt(T))
      mu = drift - sigma^2/2  (risk-neutral would be r - sigma^2/2)

    We use a slightly negative drift (conservative, reflects that stocks in our
    universe tend to be quality compounders, but we want realistic fill probs).
    """
    if current_price <= 0 or trigger_price <= 0 or annual_vol <= 0:
        return 0.0

    # If already at or below trigger, probability is 100%
    if current_price <= trigger_price:
        return 1.0

    S0 = current_price
    K = trigger_price
    sigma = annual_vol
    T = horizon_years

    # Use near-zero drift (conservative: not assuming stock goes up or down)
    mu = drift

    log_ratio = math.log(K / S0)  # This is negative since K < S0
    sigma_sqrt_T = sigma * math.sqrt(T)

    if sigma_sqrt_T < 1e-10:
        return 0.0

    d1 = (log_ratio - mu * T) / sigma_sqrt_T
    d2 = (log_ratio + mu * T) / sigma_sqrt_T

    # Barrier probability
    if abs(mu) < 1e-10:
        # Simplified formula when drift is ~0
        prob = 2.0 * norm.cdf(d1)
    else:
        exponent = 2.0 * mu * log_ratio / (sigma ** 2)
        # Clamp exponent to avoid overflow
        exponent = max(min(exponent, 50), -50)
        prob = norm.cdf(d1) + math.exp(exponent) * norm.cdf(d2)

    return min(max(prob, 0.0), 1.0)


def fill_probability_short(current_price, trigger_price, annual_vol, horizon_years=0.5, drift=0.0):
    """Calculate probability that stock price hits trigger (above current) within horizon.

    For SHORT orders, trigger_price > current_price.
    P(max_{0<=t<=T} S_t >= K) where K > S_0.

    By symmetry of GBM: P(max S_t >= K) = P(min S_t <= S0^2/K) with adjusted params,
    or directly: use the same reflection principle for the upper barrier.
    """
    if current_price <= 0 or trigger_price <= 0 or annual_vol <= 0:
        return 0.0

    # If already at or above trigger, probability is 100%
    if current_price >= trigger_price:
        return 1.0

    S0 = current_price
    K = trigger_price
    sigma = annual_vol
    T = horizon_years

    mu = drift

    log_ratio = math.log(K / S0)  # Positive since K > S0
    sigma_sqrt_T = sigma * math.sqrt(T)

    if sigma_sqrt_T < 1e-10:
        return 0.0

    # For upper barrier: d1 = (ln(K/S0) - mu*T) / (sigma*sqrt(T))
    # But we need to negate because we want P(max >= K)
    # P(max S_t >= K) = N(-d1') + exp(...) * N(-d2')
    # where d1' = (ln(S0/K) + mu*T) / (sigma*sqrt(T))
    #       d2' = (ln(S0/K) - mu*T) / (sigma*sqrt(T))

    log_ratio_inv = math.log(S0 / K)  # Negative since S0 < K

    d1 = (log_ratio_inv + mu * T) / sigma_sqrt_T
    d2 = (log_ratio_inv - mu * T) / sigma_sqrt_T

    if abs(mu) < 1e-10:
        prob = 2.0 * norm.cdf(d1)
    else:
        exponent = 2.0 * mu * log_ratio_inv / (sigma ** 2)
        exponent = max(min(exponent, 50), -50)
        prob = norm.cdf(d1) + math.exp(exponent) * norm.cdf(d2)

    return min(max(prob, 0.0), 1.0)


def classify_probability(prob_pct):
    """Classify fill probability into categories."""
    if prob_pct >= 40:
        return "REALISTIC"
    elif prob_pct >= 20:
        return "POSSIBLE"
    elif prob_pct >= 10:
        return "BORDERLINE"
    else:
        return "FANTASY"


def process_order(order, horizon_years, is_short=False):
    """Process a single standing order. Returns dict with all computed fields."""
    ticker = order.get("ticker", "?")
    trigger_str = order.get("trigger", "")
    category = order.get("category", "?")
    action = order.get("action", "BUY")

    trigger_price, currency_hint = parse_trigger_price(trigger_str)

    result = {
        "ticker": ticker,
        "action": action,
        "category": category,
        "trigger_str": trigger_str,
        "trigger_price": trigger_price,
        "current_price": None,
        "currency": None,
        "distance_pct": None,
        "annual_vol": None,
        "fill_prob_pct": None,
        "classification": None,
        "stored_prob": order.get("fill_prob_6m"),
        "error": None,
    }

    if trigger_price is None:
        # Check if trigger is conditional (e.g., "CagriSema positive")
        if any(kw in trigger_str.lower() for kw in ["positive", "conditional", "or"]):
            result["error"] = "CONDITIONAL"
        else:
            result["error"] = "UNPARSEABLE"
        return result

    # Get current price
    current_price, currency = get_current_price(ticker)
    if current_price is None:
        result["error"] = "NO_PRICE"
        return result

    result["current_price"] = current_price
    result["currency"] = currency

    # Calculate distance
    if is_short:
        # Short: trigger is above current price
        distance_pct = ((trigger_price - current_price) / current_price) * 100
    else:
        # Long: trigger is below current price (distance is how far price needs to fall)
        distance_pct = ((current_price - trigger_price) / current_price) * 100

    result["distance_pct"] = distance_pct

    # Get volatility
    annual_vol = get_annualized_volatility(ticker)
    if annual_vol is None:
        result["error"] = "NO_VOL"
        return result

    result["annual_vol"] = annual_vol * 100  # Store as percentage

    # Calculate fill probability
    if is_short:
        prob = fill_probability_short(current_price, trigger_price, annual_vol, horizon_years)
    else:
        prob = fill_probability_long(current_price, trigger_price, annual_vol, horizon_years)

    result["fill_prob_pct"] = prob * 100
    result["classification"] = classify_probability(prob * 100)

    return result


# =========================================================================
# FRESHNESS CHECK — thesis staleness per standing order
# =========================================================================

def get_thesis_git_date(ticker):
    """Get the last git commit date for the thesis file behind a standing order.

    Searches in order: thesis/research/{TICKER}/thesis.md,
    thesis/active/{TICKER}/thesis.md, thesis/short/research/{TICKER}/thesis.md.
    Returns (date_obj, age_days, filepath) or (None, None, None).
    """
    candidate_paths = [
        os.path.join(PROJECT_ROOT, "thesis", "research", ticker, "thesis.md"),
        os.path.join(PROJECT_ROOT, "thesis", "active", ticker, "thesis.md"),
        os.path.join(PROJECT_ROOT, "thesis", "short", "research", ticker, "thesis.md"),
    ]

    for filepath in candidate_paths:
        if not os.path.exists(filepath):
            continue
        try:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%aI", "--", filepath],
                capture_output=True, text=True, cwd=PROJECT_ROOT, timeout=10
            )
            date_str = result.stdout.strip()
            if not date_str:
                # File exists but no git history — use file mtime as fallback
                mtime = os.path.getmtime(filepath)
                dt = datetime.fromtimestamp(mtime).date()
                age = (date.today() - dt).days
                return dt, age, filepath
            # Parse ISO date (e.g. 2026-03-21T10:30:00+01:00)
            dt = datetime.fromisoformat(date_str).date()
            age = (date.today() - dt).days
            return dt, age, filepath
        except Exception:
            continue

    return None, None, None


def load_material_events():
    """Load material events from meta_reflection_tracker.yaml.

    Returns list of dicts with keys: ticker, event_date, level, event, status.
    """
    if not os.path.exists(TRACKER_PATH):
        return []
    try:
        with open(TRACKER_PATH, "r") as f:
            data = yaml.safe_load(f) or {}
        return data.get("material_events", []) or []
    except Exception:
        return []


def get_material_events_for_ticker(ticker, material_events, thesis_date):
    """Count material events with status STALE or PARTIAL since thesis_date.

    Returns (total_events_since_thesis, stale_or_partial_count, event_details).
    """
    if thesis_date is None:
        return 0, 0, []

    matching = []
    stale_partial = 0

    for evt in material_events:
        evt_ticker = evt.get("ticker", "")
        if evt_ticker != ticker:
            continue
        evt_date_str = evt.get("event_date", "")
        evt_status = evt.get("status", "")
        evt_level = evt.get("level", "")

        # Parse event date
        try:
            evt_date = datetime.strptime(str(evt_date_str), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue

        # Only count events since thesis was last updated
        if evt_date >= thesis_date:
            detail = {
                "date": evt_date,
                "level": evt_level,
                "event": evt.get("event", ""),
                "status": evt_status,
            }
            matching.append(detail)
            if evt_status in ("STALE", "PARTIAL"):
                stale_partial += 1

    return len(matching), stale_partial, matching


def classify_freshness(age_days, stale_partial_count, has_thesis):
    """Classify thesis freshness for a standing order.

    Returns (classification, is_blocked).
    - FRESH: thesis <14d old, no unresolved material events
    - ACCEPTABLE: thesis 14-30d old, no material events with STALE/PARTIAL
    - STALE: thesis >30d old OR material events pending
    - BLOCKED: thesis >30d AND material events with STALE/PARTIAL status
    - NO_THESIS: no thesis file found
    """
    if not has_thesis:
        return "NO_THESIS", False

    if age_days is None:
        return "UNKNOWN", False

    if age_days > 30 and stale_partial_count > 0:
        return "BLOCKED", True
    elif age_days > 30:
        return "STALE", False
    elif stale_partial_count > 0:
        return "STALE", False
    elif age_days > 14:
        return "ACCEPTABLE", False
    else:
        return "FRESH", False


def run_freshness_check():
    """Run the --freshness report: thesis freshness behind each standing order."""
    data = load_standing_orders()
    long_orders = data.get("standing_orders", []) or []
    short_orders = data.get("short_orders", []) or []

    # Combine all active SOs (skip comments / archived entries which are just YAML comments)
    all_orders = []
    for order in long_orders:
        if isinstance(order, dict) and order.get("ticker"):
            all_orders.append((order, "LONG"))
    for order in short_orders:
        if isinstance(order, dict) and order.get("ticker"):
            all_orders.append((order, "SHORT"))

    material_events = load_material_events()

    today = date.today()
    print(f"SO THESIS FRESHNESS | {today}")
    print("=" * 90)
    print(f"{'Ticker':<12} {'Trigger':<16} {'Thesis Age':<12} {'Mat.Events':<14} {'Freshness'}")
    print("-" * 90)

    results = []
    blocked_details = []

    # Counters
    fresh_count = 0
    acceptable_count = 0
    stale_count = 0
    blocked_count = 0
    no_thesis_count = 0

    for order, side in all_orders:
        ticker = order.get("ticker", "?")
        trigger_str = order.get("trigger", "?")
        category = order.get("category", "?")

        # Get thesis date via git
        thesis_date, age_days, thesis_path = get_thesis_git_date(ticker)

        # Get material events since thesis date
        total_events, stale_partial, event_details = get_material_events_for_ticker(
            ticker, material_events, thesis_date
        )

        has_thesis = thesis_date is not None
        classification, is_blocked = classify_freshness(age_days, stale_partial, has_thesis)

        # Format age string
        if age_days is not None:
            age_str = f"thesis {age_days:>3}d"
        else:
            age_str = "NO THESIS"

        # Format events string
        evt_str = f"{total_events} events"
        if stale_partial > 0:
            evt_str += f" ({stale_partial} STALE)"

        # Format freshness with annotation
        fresh_str = classification
        if is_blocked:
            fresh_str += " <- BLOCK"
        elif classification == "STALE":
            fresh_str += " <- FLAG"
        elif category == "GATED":
            fresh_str += " (GATED)"

        print(f"{ticker:<12} {trigger_str:<16} {age_str:<12} {evt_str:<14} {fresh_str}")

        # Count
        if classification == "FRESH":
            fresh_count += 1
        elif classification == "ACCEPTABLE":
            acceptable_count += 1
        elif classification == "STALE":
            stale_count += 1
        elif classification == "BLOCKED":
            blocked_count += 1
        elif classification == "NO_THESIS":
            no_thesis_count += 1

        # Collect blocked details
        if is_blocked:
            reasons = []
            if age_days is not None and age_days > 30:
                reasons.append(f"thesis {age_days}d old")
            if stale_partial > 0:
                reasons.append(f"{stale_partial} material event(s) with STALE/PARTIAL status")
            for evt in event_details:
                if evt["status"] in ("STALE", "PARTIAL"):
                    reasons.append(f"  ME: {evt['event'][:60]} ({evt['status']})")
            blocked_details.append((ticker, reasons))

        # Also flag STALE with details
        if classification == "STALE" and not is_blocked:
            reasons = []
            if age_days is not None and age_days > 30:
                reasons.append(f"thesis {age_days}d old — consider refreshing before execution")
            if stale_partial > 0:
                for evt in event_details:
                    if evt["status"] in ("STALE", "PARTIAL"):
                        reasons.append(f"  ME: {evt['event'][:60]} ({evt['status']})")
            if reasons:
                blocked_details.append((ticker, reasons))

    # Print blocked/stale details
    if blocked_details:
        print()
        print("FLAGGED SOs (thesis stale or material events pending):")
        for ticker, reasons in blocked_details:
            print(f"  {ticker}:")
            for reason in reasons:
                print(f"    {reason}")

    # Summary
    total = fresh_count + acceptable_count + stale_count + blocked_count + no_thesis_count
    print()
    print("-" * 90)
    print(f"SUMMARY:")
    print(f"  Total SOs: {total}")
    print(f"  FRESH (<14d): {fresh_count}")
    print(f"  ACCEPTABLE (14-30d): {acceptable_count}")
    print(f"  STALE (>30d or mat.events): {stale_count}")
    print(f"  BLOCKED (>30d AND mat.events STALE/PARTIAL): {blocked_count}")
    if no_thesis_count > 0:
        print(f"  NO_THESIS: {no_thesis_count}")
    print()
    print("[Verifiable by human. No AI interpretation needed.]")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Standing Order Fill Probability Calculator"
    )
    parser.add_argument(
        "--active-only", action="store_true",
        help="Only show ACTIVE category orders"
    )
    parser.add_argument(
        "--include-extreme", action="store_true",
        help="Include EXTREME opportunity watchlist"
    )
    parser.add_argument(
        "--horizon", type=float, default=6.0,
        help="Horizon in months (default: 6)"
    )
    parser.add_argument(
        "--ticker", nargs="+",
        help="Only process specific tickers"
    )
    parser.add_argument(
        "--freshness", action="store_true",
        help="Check thesis freshness behind each standing order (no yfinance calls)"
    )
    args = parser.parse_args()

    # Freshness mode: separate report, no yfinance needed
    if args.freshness:
        run_freshness_check()
        return

    horizon_years = args.horizon / 12.0

    data = load_standing_orders()
    long_orders = data.get("standing_orders", [])
    short_orders = data.get("short_orders", []) or []
    extreme_orders = data.get("extreme_opportunity", []) or []

    # Filter categories
    if args.active_only:
        long_orders = [o for o in long_orders if o.get("category") == "ACTIVE"]
        short_orders = [o for o in short_orders if o.get("category") == "ACTIVE"]

    # Filter specific tickers
    if args.ticker:
        tickers_set = set(args.ticker)
        long_orders = [o for o in long_orders if o.get("ticker") in tickers_set]
        short_orders = [o for o in short_orders if o.get("ticker") in tickers_set]
        extreme_orders = [o for o in extreme_orders if o.get("ticker") in tickers_set]

    all_results = []

    # Process long orders
    print(f"Processing {len(long_orders)} long standing orders...")
    for order in long_orders:
        result = process_order(order, horizon_years, is_short=False)
        result["side"] = "LONG"
        all_results.append(result)

    # Process short orders
    if short_orders:
        print(f"Processing {len(short_orders)} short standing orders...")
        for order in short_orders:
            result = process_order(order, horizon_years, is_short=True)
            result["side"] = "SHORT"
            all_results.append(result)

    # Process extreme orders if requested
    extreme_results = []
    if args.include_extreme and extreme_orders:
        print(f"Processing {len(extreme_orders)} extreme opportunity orders...")
        for order in extreme_orders:
            result = process_order(order, horizon_years, is_short=False)
            result["side"] = "LONG"
            result["category"] = "EXTREME"
            extreme_results.append(result)

    # Print results
    today = date.today()
    print()
    print(f"STANDING ORDER FILL PROBABILITY | {today} | Horizon: {args.horizon:.0f} months")
    print("=" * 130)
    print(f"{'Ticker':<12} {'Act':<5} {'Cat':<11} {'Price':>10} {'Trigger':>10} {'Dist%':>7} {'AnnVol%':>8} {'FillProb%':>10} {'Class':<12} {'Stored%':>8}")
    print("-" * 130)

    # Sort: by category priority (ACTIVE first), then by fill probability descending
    cat_order = {"ACTIVE": 0, "GATED": 1, "BORDERLINE": 2, "EXTREME": 3}

    # Separate computable from error results
    computable = [r for r in all_results if r["fill_prob_pct"] is not None]
    errors = [r for r in all_results if r["fill_prob_pct"] is None]

    computable.sort(key=lambda r: (cat_order.get(r["category"], 9), -r["fill_prob_pct"]))

    # Stats
    realistic_count = 0
    possible_count = 0
    borderline_count = 0
    fantasy_count = 0

    for r in computable:
        price_str = f"{r['current_price']:.2f}" if r['current_price'] else "N/A"
        trigger_str = f"{r['trigger_price']:.2f}" if r['trigger_price'] else "N/A"
        dist_str = f"{r['distance_pct']:.1f}" if r['distance_pct'] is not None else "N/A"
        vol_str = f"{r['annual_vol']:.1f}" if r['annual_vol'] is not None else "N/A"
        prob_str = f"{r['fill_prob_pct']:.1f}" if r['fill_prob_pct'] is not None else "N/A"
        stored_str = f"{r['stored_prob']}%" if r['stored_prob'] is not None else "-"
        classification = r['classification'] or "?"

        if classification == "REALISTIC":
            realistic_count += 1
        elif classification == "POSSIBLE":
            possible_count += 1
        elif classification == "BORDERLINE":
            borderline_count += 1
        elif classification == "FANTASY":
            fantasy_count += 1

        print(f"{r['ticker']:<12} {r['action']:<5} {r['category']:<11} {price_str:>10} {trigger_str:>10} {dist_str:>7} {vol_str:>8} {prob_str:>10} {classification:<12} {stored_str:>8}")

    # Print errors
    if errors:
        print()
        print("SKIPPED (could not compute):")
        for r in errors:
            print(f"  {r['ticker']:<12} {r['category']:<11} {r['trigger_str']:<25} {r['error']}")

    # Print extreme section if included
    if extreme_results:
        ext_computable = [r for r in extreme_results if r["fill_prob_pct"] is not None]
        ext_errors = [r for r in extreme_results if r["fill_prob_pct"] is None]

        if ext_computable:
            print()
            print("-" * 130)
            print("EXTREME OPPORTUNITY WATCHLIST (crash-only)")
            print("-" * 130)
            ext_computable.sort(key=lambda r: -r["fill_prob_pct"])
            for r in ext_computable:
                price_str = f"{r['current_price']:.2f}" if r['current_price'] else "N/A"
                trigger_str = f"{r['trigger_price']:.2f}" if r['trigger_price'] else "N/A"
                dist_str = f"{r['distance_pct']:.1f}" if r['distance_pct'] is not None else "N/A"
                vol_str = f"{r['annual_vol']:.1f}" if r['annual_vol'] is not None else "N/A"
                prob_str = f"{r['fill_prob_pct']:.1f}" if r['fill_prob_pct'] is not None else "N/A"
                stored_str = f"{r['stored_prob']}%" if r['stored_prob'] is not None else "-"
                classification = r['classification'] or "?"

                if classification == "REALISTIC":
                    realistic_count += 1
                elif classification == "POSSIBLE":
                    possible_count += 1
                elif classification == "BORDERLINE":
                    borderline_count += 1
                elif classification == "FANTASY":
                    fantasy_count += 1

                print(f"{r['ticker']:<12} {'BUY':<5} {'EXTREME':<11} {price_str:>10} {trigger_str:>10} {dist_str:>7} {vol_str:>8} {prob_str:>10} {classification:<12} {stored_str:>8}")

        if ext_errors:
            for r in ext_errors:
                print(f"  {r['ticker']:<12} EXTREME     {r['trigger_str']:<25} {r['error']}")

    # Summary
    total = len(computable) + len([r for r in extreme_results if r.get("fill_prob_pct") is not None])
    print()
    print("-" * 130)
    print(f"SUMMARY: {total} orders analyzed | "
          f"REALISTIC: {realistic_count} | POSSIBLE: {possible_count} | "
          f"BORDERLINE: {borderline_count} | FANTASY: {fantasy_count}")

    if fantasy_count > total * 0.5 and total > 3:
        print(f"WARNING: {fantasy_count}/{total} orders are FANTASY (<10% fill probability).")
        print("  Consider raising triggers or removing these SOs per Error Pattern #54.")

    print()
    print("[Raw data. Lognormal barrier model. Zero drift assumed (conservative).]")
    print(f"[Model: GBM reflection principle. Horizon: {args.horizon:.0f}mo. Vol: 1yr annualized daily.]")
    print()


if __name__ == "__main__":
    main()

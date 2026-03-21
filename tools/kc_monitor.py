#!/usr/bin/env python3
"""
Kill Condition Monitor v1.1
Parses kill conditions from active thesis files and displays dashboard.
v1.1: Added --health flag for Position Health Score (0-100).

Usage:
    python3 tools/kc_monitor.py                  # All positions
    python3 tools/kc_monitor.py --triggered-only  # Only TRIGGERED/MONITORING KCs
    python3 tools/kc_monitor.py --ticker NVO      # Specific ticker
    python3 tools/kc_monitor.py --compact          # One-line-per-ticker summary
    python3 tools/kc_monitor.py --health           # Position Health Scores (0-100)

Note: KC status derived from thesis files, not live data.
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta

try:
    import yaml
except ImportError:
    yaml = None

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THESIS_DIR = os.path.join(BASE_DIR, "thesis", "active")
SHORT_THESIS_DIR = os.path.join(BASE_DIR, "thesis", "short", "active")
CURRENT_YAML = os.path.join(BASE_DIR, "portfolio", "current.yaml")
TRACKER_YAML = os.path.join(BASE_DIR, "state", "meta_reflection_tracker.yaml")
SM_GRAPH_JSON = os.path.join(BASE_DIR, "tools", "smart_money", "graph.json")

# Status priority for sorting (lower = shown first)
STATUS_PRIORITY = {
    "TRIGGERED": 0,
    "MONITORING": 1,
    "AMBER": 2,
    "PENDING": 3,
    "WATCHING": 4,
    "NEW": 5,
    "DORMANT": 6,
    "OK": 7,
    "CLEAR": 8,
    "UNKNOWN": 9,
}

# Recognized status keywords
STATUS_KEYWORDS = ["TRIGGERED", "MONITORING", "AMBER", "PENDING", "WATCHING",
                   "NEW", "DORMANT", "OK", "CLEAR"]


def read_thesis(ticker_dir):
    """Read thesis.md (or s3_resolution.md / committee_decision.md for shorts) from a ticker directory."""
    # Try thesis.md first, then short thesis files
    for filename in ["thesis.md", "s3_resolution.md", "committee_decision.md"]:
        path = os.path.join(ticker_dir, filename)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
    return None


def extract_ticker(ticker_dir):
    """Extract ticker name from directory path."""
    return os.path.basename(ticker_dir)


def extract_header_kc_info(text):
    """Extract KC mentions from thesis header (lines starting with >)."""
    header_kc = {}
    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith(">"):
            # Stop at first --- (end of header block)
            if line == "---":
                break
            continue
        # Look for KC#N TRIGGERED or similar
        matches = re.finditer(r'KC#(\d+)\s+(TRIGGERED|MONITORING|AMBER|PENDING|WATCHING)', line, re.IGNORECASE)
        for m in matches:
            kc_num = int(m.group(1))
            status = m.group(2).upper()
            header_kc[kc_num] = status
    return header_kc


def find_kc_section(text):
    """Find the Kill Conditions definition section (NOT the status section).
    Returns content between the KC header and the next section/status header/---."""
    lines = text.split("\n")
    kc_start = None
    kc_end = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        if kc_start is None:
            # Match "## Kill Conditions" or "### Kill Conditions" (with optional suffix)
            # but NOT "Kill Conditions Status"
            if re.match(r'^#{2,3}\s+Kill\s+Conditions\b', stripped, re.IGNORECASE):
                if "status" in stripped.lower():
                    continue
                kc_start = i + 1
            continue

        # We found the start. Now find the end.
        # End at: next ## or ### header, "Kill Conditions Status" bold header, or ---
        if re.match(r'^#{2,3}\s+', stripped):
            kc_end = i
            break
        if re.match(r'^\*\*Kill\s+Conditions?\s+Status', stripped, re.IGNORECASE):
            kc_end = i
            break
        if stripped == "---" and i > kc_start + 1:
            kc_end = i
            break

    if kc_start is None:
        return None

    if kc_end is None:
        kc_end = len(lines)

    return "\n".join(lines[kc_start:kc_end])


def find_kc_status_section(text):
    """Find the Kill Conditions Status section and return its content."""
    lines = text.split("\n")
    status_start = None
    status_end = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        if status_start is None:
            # Match "### Kill Conditions Status" or "**Kill Conditions Status"
            if re.match(r'^(?:#{2,3}\s+|\*\*)?Kill\s+Conditions?\s+Status', stripped, re.IGNORECASE):
                status_start = i + 1
            continue

        # Found start, find end
        if re.match(r'^#{2,3}\s+', stripped):
            status_end = i
            break
        if stripped == "---":
            status_end = i
            break

    if status_start is None:
        return None
    if status_end is None:
        status_end = len(lines)

    return "\n".join(lines[status_start:status_end])


def parse_kcs_from_list(section_text):
    """Parse KCs from numbered list format (1. **description** or 1. description)."""
    kcs = []
    if not section_text:
        return kcs

    for line in section_text.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Only match numbered items: "1. description"
        m = re.match(r'^(\d+)\.\s+(.+)', line)
        if not m:
            continue

        kc_num = int(m.group(1))
        desc = m.group(2).strip()

        # Clean description: remove bold markers
        desc = re.sub(r'\*\*', '', desc)

        # Extract inline status if present
        inline_status = "UNKNOWN"
        # Check for explicit TRIGGERED/MONITORING etc. in the line
        # But avoid false positives from description text containing these words in context
        # Only match if it appears as a standalone status indicator
        for kw in STATUS_KEYWORDS:
            # Match status keyword that appears as a standalone word (not part of a description)
            # e.g., "KC#1 TRIGGERED" or "-- TRIGGERED" but not "would signal MONITORING requirement"
            if re.search(r'(?:^|\s|—|--|\.|\()' + kw + r'(?:\s|$|\.|\,|!|—|\))', desc.upper()):
                inline_status = kw
                break

        # Truncate description for display
        # Take first clause before -- or — for cleaner display
        desc_short = desc.split("--")[0].strip() if "--" in desc else desc
        desc_short = desc_short.split("—")[0].strip() if "—" in desc_short else desc_short

        # Remove KC#N: prefix if present (TW format)
        desc_short = re.sub(r'^KC#\d+:\s*', '', desc_short)

        # Remove inline status words from display description
        desc_short = re.sub(r'\s*\(?(TRIGGERED|MONITORING|AMBER|OK|CLEAR|DORMANT|PENDING|WATCHING)\)?[.!]?\s*$',
                            '', desc_short, flags=re.IGNORECASE).strip()

        if len(desc_short) > 80:
            desc_short = desc_short[:77] + "..."

        kcs.append({
            "num": kc_num,
            "description": desc_short,
            "status": inline_status,
            "full_text": desc,
        })

    return kcs


def parse_kcs_from_table(section_text):
    """Parse KCs from table format (| # | Kill Condition | Status | Notes |)."""
    kcs = []
    if not section_text:
        return kcs

    for line in section_text.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue

        cols = [c.strip() for c in line.split("|")]
        cols = [c for c in cols if c]  # Remove empty from leading/trailing |

        if len(cols) < 2:
            continue

        # Skip header row and separator row
        if re.match(r'^-+$', cols[0]) or cols[0] == "#" or cols[0].lower() == "kill condition":
            continue

        # Try to extract KC number from first column
        num_match = re.match(r'(\d+)', cols[0])
        if not num_match:
            continue

        kc_num = int(num_match.group(1))
        desc = re.sub(r'\*\*', '', cols[1]).strip()

        # Status from third column if present
        status = "UNKNOWN"
        if len(cols) >= 3:
            status_raw = re.sub(r'\*\*', '', cols[2]).strip().upper()
            for kw in STATUS_KEYWORDS:
                if kw in status_raw:
                    status = kw
                    break

        # Notes from fourth column if present
        notes = re.sub(r'\*\*', '', cols[3]).strip() if len(cols) > 3 else ""

        # Truncate description
        if len(desc) > 80:
            desc = desc[:77] + "..."

        kcs.append({
            "num": kc_num,
            "description": desc,
            "status": status,
            "full_text": f"{desc} | {notes}" if notes else desc,
        })

    return kcs


def parse_status_section(status_text):
    """Parse KC statuses from a dedicated status section."""
    statuses = {}
    if not status_text:
        return statuses

    for line in status_text.split("\n"):
        line = line.strip()

        # Format: "- KC#1: OK. Details..." or "- KC#1: TRIGGERED. Details..."
        m = re.match(r'^-\s+KC#(\d+):\s*(\w+)', line)
        if m:
            kc_num = int(m.group(1))
            status_word = m.group(2).upper()
            if status_word in STATUS_KEYWORDS:
                statuses[kc_num] = status_word
            continue

        # Table format: "| 1. Description | OK | Notes |"
        if line.startswith("|"):
            cols = [c.strip() for c in line.split("|")]
            cols = [c for c in cols if c]
            if len(cols) >= 2:
                num_match = re.match(r'(\d+)', cols[0])
                if num_match:
                    kc_num = int(num_match.group(1))
                    for col in cols[1:]:
                        col_upper = re.sub(r'\*\*', '', col).strip().upper()
                        for kw in STATUS_KEYWORDS:
                            if kw == col_upper or col_upper.startswith(kw + " ") or col_upper.startswith(kw + "."):
                                statuses[kc_num] = kw
                                break
                        if kc_num in statuses:
                            break

    return statuses


def parse_assessment_line(text):
    """Extract status from assessment lines mentioning specific KCs."""
    statuses = {}
    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("**Assessment") and not line.startswith("**No kill") and not line.lower().startswith("no kill"):
            continue
        for m in re.finditer(r'KC#(\d+)\s*(?:\([^)]*\))?\s*(?:at|is|remains?|—)?\s*(\w+)', line):
            status_word = m.group(2).upper()
            if status_word in STATUS_KEYWORDS:
                statuses[int(m.group(1))] = status_word
    return statuses


def process_ticker(ticker_dir):
    """Process a single ticker directory and return list of KC entries."""
    ticker = extract_ticker(ticker_dir)
    text = read_thesis(ticker_dir)
    if text is None:
        return ticker, []

    # 1. Extract header KC info (e.g., "KC#1 TRIGGERED" in > lines)
    header_kc = extract_header_kc_info(text)

    # 2. Find and parse KC definition section
    kc_section = find_kc_section(text)
    if kc_section is None:
        return ticker, []

    # Determine format: table or list
    has_table = bool(re.search(r'^\|.*\|.*\|', kc_section, re.MULTILINE))

    if has_table:
        kcs = parse_kcs_from_table(kc_section)
    else:
        kcs = parse_kcs_from_list(kc_section)

    if not kcs:
        return ticker, []

    # 3. Find and parse dedicated status section
    status_section = find_kc_status_section(text)
    status_map = parse_status_section(status_section) if status_section else {}

    # 4. Parse assessment lines for additional status clues
    assessment_statuses = parse_assessment_line(kc_section)
    if status_section:
        assessment_statuses.update(parse_assessment_line(status_section))

    # 5. Apply statuses with priority: header > status_section > assessment > inline
    for kc in kcs:
        num = kc["num"]
        final_status = kc["status"]  # inline (lowest priority)

        if num in assessment_statuses:
            final_status = assessment_statuses[num]

        if num in status_map:
            final_status = status_map[num]

        if num in header_kc:
            final_status = header_kc[num]

        # For table-parsed KCs, the table status is authoritative (only header overrides)
        if has_table and kc["status"] != "UNKNOWN":
            final_status = header_kc[num] if num in header_kc else kc["status"]

        kc["status"] = final_status

    return ticker, kcs


def sort_key(kc_entry):
    """Sort KCs by status priority."""
    ticker, kc = kc_entry
    return (STATUS_PRIORITY.get(kc["status"], 99), ticker, kc["num"])


def print_dashboard(all_kcs, triggered_only=False):
    """Print the full dashboard."""
    today = date.today().isoformat()
    print("=" * 80)
    print(f"KILL CONDITION MONITOR — {today}")
    print("=" * 80)
    print(f"Note: KC status derived from thesis files, not live data.")
    print()

    # Flatten and optionally filter
    entries = []
    for ticker, kcs in all_kcs:
        for kc in kcs:
            if triggered_only and kc["status"] not in ("TRIGGERED", "MONITORING", "AMBER"):
                continue
            entries.append((ticker, kc))

    if not entries:
        if triggered_only:
            print("No TRIGGERED or MONITORING kill conditions found.")
        else:
            print("No kill conditions found in any active thesis.")
        return

    entries.sort(key=sort_key)

    print(f"{'Ticker':<10} {'KC#':<5} {'Status':<12} {'Description'}")
    print("-" * 80)

    for ticker, kc in entries:
        status_display = kc["status"]
        if status_display == "TRIGGERED":
            status_display = "TRIGGERED!"

        print(f"{ticker:<10} {kc['num']:<5} {status_display:<12} {kc['description']}")

    print("-" * 80)

    all_total = sum(len(kcs) for _, kcs in all_kcs)
    all_tickers = sum(1 for _, kcs in all_kcs if kcs)

    status_counts = {}
    status_tickers = {}
    for ticker, kc in entries:
        s = kc["status"]
        status_counts[s] = status_counts.get(s, 0) + 1
        if s not in status_tickers:
            status_tickers[s] = set()
        status_tickers[s].add(ticker)

    if triggered_only:
        print(f"\nSHOWING: {len(entries)} flagged KCs (from {all_total} total across {all_tickers} positions)")
    else:
        print(f"\nSUMMARY: {all_tickers} positions, {len(entries)} total KCs")

    for status in ["TRIGGERED", "MONITORING", "AMBER", "PENDING", "WATCHING", "NEW",
                    "DORMANT", "OK", "CLEAR", "UNKNOWN"]:
        if status in status_counts:
            ticker_list = ", ".join(sorted(status_tickers[status]))
            print(f"  {status:<12}: {status_counts[status]:>3}  ({ticker_list})")


def print_compact(all_kcs):
    """Print compact one-line-per-ticker summary."""
    today = date.today().isoformat()
    print(f"KC Monitor [{today}] — Note: status from thesis files, not live data.")
    print()
    print(f"{'Ticker':<10} {'KCs':<5} {'TRIG':<5} {'MON':<5} {'OK+':<5} {'UNK':<5} {'Flags'}")
    print("-" * 70)

    has_any = False
    for ticker, kcs in sorted(all_kcs, key=lambda x: x[0]):
        if not kcs:
            continue
        has_any = True

        total = len(kcs)
        triggered = sum(1 for kc in kcs if kc["status"] == "TRIGGERED")
        monitoring = sum(1 for kc in kcs if kc["status"] in ("MONITORING", "AMBER"))
        ok = sum(1 for kc in kcs if kc["status"] in ("OK", "CLEAR", "DORMANT", "NEW"))
        unknown = sum(1 for kc in kcs if kc["status"] == "UNKNOWN")

        flags = []
        if triggered > 0:
            triggered_nums = [f"KC#{kc['num']}" for kc in kcs if kc["status"] == "TRIGGERED"]
            flags.append(f"TRIG: {','.join(triggered_nums)}")
        if monitoring > 0:
            mon_nums = [f"KC#{kc['num']}" for kc in kcs if kc["status"] in ("MONITORING", "AMBER")]
            flags.append(f"MON: {','.join(mon_nums)}")

        flag_str = " | ".join(flags) if flags else "--"
        print(f"{ticker:<10} {total:<5} {triggered:<5} {monitoring:<5} {ok:<5} {unknown:<5} {flag_str}")

    if not has_any:
        print("No kill conditions found in any active thesis.")
        return

    print("-" * 70)
    all_triggered = [(t, kc) for t, kcs in all_kcs for kc in kcs if kc["status"] == "TRIGGERED"]
    all_monitoring = [(t, kc) for t, kcs in all_kcs for kc in kcs if kc["status"] in ("MONITORING", "AMBER")]
    total_kcs = sum(len(kcs) for _, kcs in all_kcs)
    total_positions = sum(1 for _, kcs in all_kcs if kcs)

    print(f"\n{total_positions} positions, {total_kcs} KCs. "
          f"TRIGGERED: {len(all_triggered)}. MONITORING: {len(all_monitoring)}.")

    if all_triggered:
        for t, kc in all_triggered:
            print(f"  >> {t} KC#{kc['num']}: {kc['description'][:60]}")


# =============================================================================
# POSITION HEALTH SCORE (--health flag)
# =============================================================================

def git_file_date(filepath):
    """Get the last modification date of a file from git log.
    Returns a date object or None if not tracked / error."""
    if not os.path.exists(filepath):
        return None
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%aI", "--", filepath],
            capture_output=True, text=True, timeout=10,
            cwd=BASE_DIR
        )
        if result.returncode == 0 and result.stdout.strip():
            date_str = result.stdout.strip()
            # Parse ISO 8601 date (e.g., "2026-03-17 14:30:00 +0100")
            dt = datetime.fromisoformat(date_str)
            return dt.date()
    except Exception:
        pass
    return None


def load_yaml_file(filepath):
    """Load a YAML file, returning None on error."""
    if yaml is None:
        # Fallback: basic YAML-like parsing not feasible; warn
        return None
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def load_current_positions():
    """Load positions from portfolio/current.yaml.
    Returns dict: ticker -> position_data."""
    data = load_yaml_file(CURRENT_YAML)
    if data is None:
        return {}
    positions = {}
    for pos in data.get("positions", []):
        ticker = pos.get("ticker", "")
        if ticker:
            positions[ticker] = pos
    for pos in data.get("short_positions", []):
        ticker = pos.get("ticker", "")
        if ticker:
            positions[ticker] = pos
    return positions


def extract_fv_from_thesis(thesis_path):
    """Extract Fair Value from thesis header (first 20 lines).
    Returns the raw FV string for comparison, or None."""
    if not os.path.exists(thesis_path):
        return None
    try:
        with open(thesis_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i > 25:
                    break
                line = line.strip()
                # Match: > **Fair Value:** <value>
                m = re.match(r'^>\s*\*\*Fair\s*Value:\*\*\s*(.+)', line, re.IGNORECASE)
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    return None


def normalize_fv_for_comparison(fv_str):
    """Extract the primary numeric FV from a FV string for comparison.
    E.g., '$406 (S181: FTC settled...)' -> ('$', 406.0)
          'EUR 24.0 (S251 recalc...)' -> ('EUR', 24.0)
          '190 GBp (R3 S147c3...)' -> ('GBp', 190.0)
    Returns (currency_hint, numeric_value) or None."""
    if not fv_str:
        return None
    # Try patterns: $NNN, EUR NNN, NNN GBp, NNN GBP
    m = re.match(r'^\$\s*([\d,.]+)', fv_str)
    if m:
        return ("$", float(m.group(1).replace(",", "")))
    m = re.match(r'^EUR\s*([\d,.]+)', fv_str, re.IGNORECASE)
    if m:
        return ("EUR", float(m.group(1).replace(",", "")))
    m = re.match(r'^([\d,.]+)\s*GBp', fv_str, re.IGNORECASE)
    if m:
        return ("GBp", float(m.group(1).replace(",", "")))
    m = re.match(r'^([\d,.]+)\s*DKK', fv_str, re.IGNORECASE)
    if m:
        return ("DKK", float(m.group(1).replace(",", "")))
    # Generic number at start
    m = re.match(r'^[\$€£]?\s*([\d,.]+)', fv_str)
    if m:
        return ("?", float(m.group(1).replace(",", "")))
    return None


def check_fv_consistency(thesis_fv_str, current_fv_str):
    """Check if thesis FV and current.yaml FV are consistent.
    Returns True if they match (same primary numeric value)."""
    t = normalize_fv_for_comparison(thesis_fv_str)
    c = normalize_fv_for_comparison(current_fv_str)
    if t is None or c is None:
        return False
    # Compare numeric values (allow small float tolerance)
    return abs(t[1] - c[1]) < 0.5


def load_tracker_data():
    """Load meta_reflection_tracker.yaml.
    Returns (material_events, open_items) lists."""
    data = load_yaml_file(TRACKER_YAML)
    if data is None:
        return [], []
    material_events = data.get("material_events", []) or []
    open_items = data.get("open_items", []) or []
    return material_events, open_items


def load_sm_graph_edges():
    """Load smart money graph edges. Returns list of edges or empty list."""
    if not os.path.exists(SM_GRAPH_JSON):
        return []
    try:
        with open(SM_GRAPH_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("edges", [])
    except Exception:
        return []


def check_sm_freshness(ticker, sm_edges, cutoff_date):
    """Check if ticker has smart money data added within cutoff_date.
    Returns True if fresh data exists."""
    for edge in sm_edges:
        if edge.get("target") == ticker or edge.get("source") == ticker:
            date_added = edge.get("date_added", "")
            if date_added:
                try:
                    edge_date = datetime.strptime(date_added[:10], "%Y-%m-%d").date()
                    if edge_date >= cutoff_date:
                        return True
                except (ValueError, TypeError):
                    continue
    return False


def calculate_health_scores(ticker_filter=None):
    """Calculate Position Health Score for all active positions.
    Returns list of dicts with score breakdown per ticker."""
    today = date.today()
    positions = load_current_positions()
    material_events, open_items = load_tracker_data()
    sm_edges = load_sm_graph_edges()

    # Build set of active thesis dirs (long + short)
    thesis_dirs = {}
    for d in sorted(glob.glob(os.path.join(THESIS_DIR, "*"))):
        if os.path.isdir(d):
            thesis_dirs[os.path.basename(d)] = d
    for d in sorted(glob.glob(os.path.join(SHORT_THESIS_DIR, "*"))):
        if os.path.isdir(d):
            thesis_dirs[os.path.basename(d)] = d

    # Determine which tickers to score: intersection of positions and thesis dirs
    tickers_to_score = set(positions.keys()) | set(thesis_dirs.keys())
    # Filter only those that have BOTH a position and a thesis dir (or at least a thesis dir)
    tickers_to_score = sorted([t for t in tickers_to_score if t in thesis_dirs])

    if ticker_filter:
        ticker_upper = ticker_filter.upper()
        tickers_to_score = [t for t in tickers_to_score if t.upper() == ticker_upper]

    results = []

    for ticker in tickers_to_score:
        thesis_dir = thesis_dirs.get(ticker, "")
        pos_data = positions.get(ticker, {})
        scores = {}
        details = {}

        # --- Factor 1: thesis.md modified <30d (+20) ---
        thesis_path = os.path.join(thesis_dir, "thesis.md")
        thesis_date = git_file_date(thesis_path)
        if thesis_date and (today - thesis_date).days <= 30:
            scores["thesis"] = 20
            details["thesis"] = f"{(today - thesis_date).days}d ago"
        else:
            scores["thesis"] = 0
            if thesis_date:
                details["thesis"] = f"{(today - thesis_date).days}d STALE"
            else:
                details["thesis"] = "MISSING"

        # --- Factor 2: devils_advocate.md exists and <60d (+15) ---
        da_path = os.path.join(thesis_dir, "devils_advocate.md")
        if not os.path.exists(da_path):
            # Also check alternative names (r2_devils_advocate.md)
            alt_da = os.path.join(thesis_dir, "r2_devils_advocate.md")
            if os.path.exists(alt_da):
                da_path = alt_da
        da_date = git_file_date(da_path)
        if da_date and (today - da_date).days <= 60:
            scores["da"] = 15
            details["da"] = f"{(today - da_date).days}d ago"
        else:
            scores["da"] = 0
            if da_date:
                details["da"] = f"{(today - da_date).days}d STALE"
            elif not os.path.exists(da_path):
                details["da"] = "MISSING"
            else:
                details["da"] = "NO GIT"

        # --- Factor 3: risk_assessment.md exists and <90d (+10) ---
        risk_path = os.path.join(thesis_dir, "risk_assessment.md")
        risk_date = git_file_date(risk_path)
        if risk_date and (today - risk_date).days <= 90:
            scores["risk"] = 10
            details["risk"] = f"{(today - risk_date).days}d ago"
        else:
            scores["risk"] = 0
            if risk_date:
                details["risk"] = f"{(today - risk_date).days}d STALE"
            elif not os.path.exists(risk_path):
                details["risk"] = "MISSING"
            else:
                details["risk"] = "NO GIT"

        # --- Factor 4: KCs reviewed <14d (+10) ---
        # Proxy: thesis.md git date as KC review indicator (KCs live in thesis)
        # A more precise check would parse KC status dates, but thesis mod date is
        # the best available proxy since KC status is updated within thesis.
        kc_date = thesis_date  # KCs are part of thesis
        if kc_date and (today - kc_date).days <= 14:
            scores["kc"] = 10
            details["kc"] = f"{(today - kc_date).days}d ago"
        else:
            scores["kc"] = 0
            if kc_date:
                details["kc"] = f"{(today - kc_date).days}d"
            else:
                details["kc"] = "N/A"

        # --- Factor 5: Material events all COMPLETE for ticker (+15) ---
        ticker_events = [e for e in material_events if e.get("ticker", "") == ticker]
        if not ticker_events:
            # No material events = fully complete (nothing pending)
            scores["events"] = 15
            details["events"] = "none"
        else:
            incomplete = [e for e in ticker_events
                          if e.get("status", "").upper() not in ("COMPLETE", "ACCEPTABLE")]
            if not incomplete:
                scores["events"] = 15
                details["events"] = f"{len(ticker_events)} OK"
            else:
                # Partial credit: proportion of complete events
                complete_count = len(ticker_events) - len(incomplete)
                ratio = complete_count / len(ticker_events) if ticker_events else 0
                scores["events"] = int(15 * ratio)
                statuses = [e.get("status", "?") for e in incomplete]
                details["events"] = f"{len(incomplete)} {'/'.join(set(statuses))}"

        # --- Factor 6: FV consistency (thesis header = current.yaml) (+10) ---
        thesis_fv = extract_fv_from_thesis(os.path.join(thesis_dir, "thesis.md"))
        current_fv = pos_data.get("fair_value", "")
        if thesis_fv and current_fv and check_fv_consistency(thesis_fv, current_fv):
            scores["fv"] = 10
            details["fv"] = "OK"
        elif not thesis_fv:
            scores["fv"] = 0
            details["fv"] = "NO HDR"
        elif not current_fv:
            scores["fv"] = 0
            details["fv"] = "NO CUR"
        else:
            scores["fv"] = 0
            t = normalize_fv_for_comparison(thesis_fv)
            c = normalize_fv_for_comparison(current_fv)
            if t and c:
                details["fv"] = f"MISMATCH {t[1]}!={c[1]}"
            else:
                details["fv"] = "PARSE?"

        # --- Factor 7: No OPEN anomalies in tracker for ticker (+10) ---
        ticker_anomalies = [item for item in open_items
                            if item.get("ticker", "") == ticker
                            and item.get("type", "").upper() == "ANOMALY"
                            and item.get("status", "").upper() == "OPEN"]
        if not ticker_anomalies:
            scores["anom"] = 10
            details["anom"] = "clear"
        else:
            scores["anom"] = 0
            details["anom"] = f"{len(ticker_anomalies)} OPEN"

        # --- Factor 8: SM stock-profile <30d (+10) ---
        sm_cutoff = today - timedelta(days=30)
        if check_sm_freshness(ticker, sm_edges, sm_cutoff):
            scores["sm"] = 10
            details["sm"] = "fresh"
        else:
            scores["sm"] = 0
            details["sm"] = "stale"

        total = sum(scores.values())

        # Determine status tier
        if total >= 80:
            status = "HEALTHY"
        elif total >= 60:
            status = "ACCEPTABLE"
        elif total >= 40:
            status = "STALE"
        else:
            status = "CRITICAL"

        results.append({
            "ticker": ticker,
            "total": total,
            "scores": scores,
            "details": details,
            "status": status,
        })

    # Sort by score ascending (worst first for attention)
    results.sort(key=lambda r: r["total"])
    return results


def generate_recommendations(results):
    """Generate actionable recommendations for positions needing attention."""
    recs = []
    for r in results:
        if r["status"] in ("HEALTHY",):
            continue
        parts = []
        s = r["scores"]
        d = r["details"]
        ticker = r["ticker"]

        if s["thesis"] == 0:
            parts.append(f"thesis {d['thesis']}")
        if s["da"] == 0:
            parts.append(f"DA {d['da']}")
        if s["risk"] == 0:
            parts.append(f"risk_assessment {d['risk']}")
        if s["events"] < 15 and d["events"] != "none":
            parts.append(f"material events {d['events']}")
        if s["fv"] == 0 and d["fv"] not in ("NO CUR",):
            parts.append(f"FV {d['fv']}")
        if s["anom"] == 0:
            parts.append(f"anomalies {d['anom']}")
        if s["sm"] == 0:
            parts.append(f"SM profile {d['sm']}")

        if parts:
            urgency = "RE-EVALUATE URGENTLY" if r["status"] == "CRITICAL" else "Needs attention"
            recs.append(f"  {ticker}: {urgency} -- {', '.join(parts)}")

    return recs


def print_health(results):
    """Print the Position Health Score dashboard."""
    today = date.today().isoformat()

    if not results:
        print("No active positions found for health scoring.")
        return

    print(f"POSITION HEALTH SCORES | {today}")
    print("=" * 105)
    print(f"{'Ticker':<10} {'Score':>5}  {'Thesis':>6} {'DA':>5} {'Risk':>5} "
          f"{'KC':>5} {'Evnts':>5} {'FV':>5} {'Anom':>5} {'SM':>5}  Status")
    print("-" * 105)

    for r in sorted(results, key=lambda x: -x["total"]):  # Best first for display
        s = r["scores"]
        print(f"{r['ticker']:<10} {r['total']:>5}  "
              f"{s['thesis']:>2}/20 "
              f"{s['da']:>2}/15 "
              f"{s['risk']:>2}/10 "
              f"{s['kc']:>2}/10 "
              f"{s['events']:>2}/15 "
              f"{s['fv']:>2}/10 "
              f"{s['anom']:>2}/10 "
              f"{s['sm']:>2}/10  "
              f"{r['status']}")

    print("-" * 105)

    # Summary stats
    avg_score = sum(r["total"] for r in results) / len(results) if results else 0
    critical = [r for r in results if r["status"] == "CRITICAL"]
    stale = [r for r in results if r["status"] == "STALE"]

    print(f"\nPORTFOLIO HEALTH: {avg_score:.0f}/100 (avg)")
    if critical:
        tickers = ", ".join(r["ticker"] for r in critical)
        print(f"CRITICAL: {len(critical)} position(s) need immediate re-evaluation ({tickers})")
    if stale:
        tickers = ", ".join(r["ticker"] for r in stale)
        print(f"STALE: {len(stale)} position(s) need attention this week ({tickers})")

    # Recommendations
    recs = generate_recommendations(results)
    if recs:
        print(f"\nRECOMMENDATIONS:")
        for rec in recs:
            print(rec)

    print(f"\n[Verifiable by human. No AI interpretation needed.]")


def main():
    parser = argparse.ArgumentParser(description="Kill Condition Monitor — parse KC status from active thesis files")
    parser.add_argument("--triggered-only", action="store_true",
                        help="Show only TRIGGERED/MONITORING/AMBER KCs")
    parser.add_argument("--ticker", type=str, default=None,
                        help="Show KCs for specific ticker only")
    parser.add_argument("--compact", action="store_true",
                        help="One-line-per-ticker summary (for session dashboard)")
    parser.add_argument("--health", action="store_true",
                        help="Position Health Score (0-100) per active position")
    args = parser.parse_args()

    # Health mode is independent from KC monitoring
    if args.health:
        if yaml is None:
            print("ERROR: PyYAML required for --health mode. Install: pip install pyyaml")
            sys.exit(1)
        results = calculate_health_scores(ticker_filter=args.ticker)
        print_health(results)
        return

    # Find all active thesis directories (long + short)
    ticker_dirs = sorted(glob.glob(os.path.join(THESIS_DIR, "*")))
    short_dirs = sorted(glob.glob(os.path.join(SHORT_THESIS_DIR, "*")))
    ticker_dirs.extend(short_dirs)
    if not ticker_dirs:
        print(f"No active thesis directories found in {THESIS_DIR}")
        sys.exit(1)

    # Filter by ticker if specified
    if args.ticker:
        ticker_upper = args.ticker.upper()
        ticker_dirs = [d for d in ticker_dirs if extract_ticker(d).upper() == ticker_upper]
        if not ticker_dirs:
            print(f"No active thesis found for ticker: {args.ticker}")
            sys.exit(1)

    # Process all tickers
    all_kcs = []
    for td in ticker_dirs:
        if not os.path.isdir(td):
            continue
        ticker, kcs = process_ticker(td)
        all_kcs.append((ticker, kcs))

    # Display
    if args.compact:
        print_compact(all_kcs)
    else:
        print_dashboard(all_kcs, triggered_only=args.triggered_only)


if __name__ == "__main__":
    main()

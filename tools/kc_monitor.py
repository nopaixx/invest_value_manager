#!/usr/bin/env python3
"""
Kill Condition Monitor v1.0
Parses kill conditions from active thesis files and displays dashboard.

Usage:
    python3 tools/kc_monitor.py                  # All positions
    python3 tools/kc_monitor.py --triggered-only  # Only TRIGGERED/MONITORING KCs
    python3 tools/kc_monitor.py --ticker NVO      # Specific ticker
    python3 tools/kc_monitor.py --compact          # One-line-per-ticker summary

Note: KC status derived from thesis files, not live data.
"""

import argparse
import glob
import os
import re
import sys
from datetime import date

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THESIS_DIR = os.path.join(BASE_DIR, "thesis", "active")
SHORT_THESIS_DIR = os.path.join(BASE_DIR, "thesis", "short", "active")

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


def main():
    parser = argparse.ArgumentParser(description="Kill Condition Monitor — parse KC status from active thesis files")
    parser.add_argument("--triggered-only", action="store_true",
                        help="Show only TRIGGERED/MONITORING/AMBER KCs")
    parser.add_argument("--ticker", type=str, default=None,
                        help="Show KCs for specific ticker only")
    parser.add_argument("--compact", action="store_true",
                        help="One-line-per-ticker summary (for session dashboard)")
    args = parser.parse_args()

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

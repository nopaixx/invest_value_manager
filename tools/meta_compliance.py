#!/usr/bin/env python3
"""
META-REFLECTION COMPLIANCE AUDITOR

Audits whether the orchestrator properly processes meta-reflections from sub-agents.
Provides objective, verifiable metrics for the human owner.

Usage:
    python3 tools/meta_compliance.py
    python3 tools/meta_compliance.py --verbose    # Show all items, not just overdue
    python3 tools/meta_compliance.py --json       # Machine-readable output

Checks:
    1. COVERAGE: DA files vs tracker entries (are items being dropped?)
    2. STALENESS: Open items past deadline or >7d old
    3. PIPELINE BLOCK: Anomalies unresolved but ticker advanced (R3/R4 newer than anomaly)
    4. RESOLUTION QUALITY: Resolved items with empty evidence = rubber-stamping
    5. FRESHNESS: Tracker last modified vs last agent run
    6. WEEKLY STATS: Compliance score with breakdown
"""

import os
import sys
import glob
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# --- Configuration ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKER_PATH = os.path.join(BASE_DIR, "state", "meta_reflection_tracker.yaml")
RESEARCH_DIR = os.path.join(BASE_DIR, "thesis", "research")
ACTIVE_DIR = os.path.join(BASE_DIR, "thesis", "active")

TODAY = datetime.now().date()

# --- YAML parser (minimal, no pyyaml dependency required but preferred) ---
def load_tracker():
    """Load the meta_reflection_tracker.yaml file."""
    if not os.path.exists(TRACKER_PATH):
        return None

    try:
        import yaml
        with open(TRACKER_PATH, 'r') as f:
            return yaml.safe_load(f)
    except ImportError:
        # Fallback: manual parse for essential fields
        return _fallback_parse_tracker()


def _fallback_parse_tracker():
    """Minimal YAML-like parser for the tracker when pyyaml unavailable."""
    items = []
    current_item = {}
    in_open_items = False

    with open(TRACKER_PATH, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith('open_items:'):
                in_open_items = True
                continue
            if not in_open_items:
                continue
            if stripped.startswith('- id:'):
                if current_item:
                    items.append(current_item)
                current_item = {'id': stripped.split(':', 1)[1].strip()}
            elif ':' in stripped and current_item:
                key, val = stripped.split(':', 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                current_item[key] = val
            if stripped.startswith('stats:'):
                in_open_items = False

        if current_item:
            items.append(current_item)

    return {'open_items': items}


# --- Data collection ---
def count_da_files():
    """Count all devils_advocate.md files across research and active dirs."""
    research_das = glob.glob(os.path.join(RESEARCH_DIR, "*", "devils_advocate.md"))
    active_das = glob.glob(os.path.join(ACTIVE_DIR, "*", "devils_advocate.md"))
    return research_das + active_das


def get_r3_r4_files(ticker):
    """Get R3/R4 files for a ticker with their modification dates."""
    files = {}
    for base_dir in [RESEARCH_DIR, ACTIVE_DIR]:
        ticker_dir = os.path.join(base_dir, ticker)
        if not os.path.isdir(ticker_dir):
            continue

        r3_path = os.path.join(ticker_dir, "r3_resolution.md")
        r4_path = os.path.join(ticker_dir, "committee_decision.md")

        if os.path.exists(r3_path):
            files['r3'] = {
                'path': r3_path,
                'mtime': datetime.fromtimestamp(os.path.getmtime(r3_path)).date()
            }
        if os.path.exists(r4_path):
            files['r4'] = {
                'path': r4_path,
                'mtime': datetime.fromtimestamp(os.path.getmtime(r4_path)).date()
            }
    return files


def get_tracker_mtime():
    """Get last modification time of the tracker file."""
    if os.path.exists(TRACKER_PATH):
        return datetime.fromtimestamp(os.path.getmtime(TRACKER_PATH)).date()
    return None


def get_latest_agent_run():
    """Estimate last agent run by checking most recent DA/thesis file modification."""
    latest = None
    for pattern in [
        os.path.join(RESEARCH_DIR, "*", "devils_advocate.md"),
        os.path.join(RESEARCH_DIR, "*", "thesis.md"),
        os.path.join(ACTIVE_DIR, "*", "devils_advocate.md"),
    ]:
        for f in glob.glob(pattern):
            mtime = datetime.fromtimestamp(os.path.getmtime(f)).date()
            if latest is None or mtime > latest:
                latest = mtime
    return latest


def parse_date(date_str):
    """Parse a date string in YYYY-MM-DD format."""
    if not date_str:
        return None
    date_str = str(date_str).strip().strip('"').strip("'")
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def extract_created_date(item):
    """Extract creation date from item source field (e.g., 'HLNE R2 DA (S237)')."""
    # Try created_date field first
    if 'created_date' in item:
        return parse_date(item['created_date'])
    # Try deadline as proxy for when it was created (created = deadline - buffer)
    if 'deadline' in item:
        dl = parse_date(item['deadline'])
        if dl:
            return dl - timedelta(days=30)  # Approximate: created ~30d before deadline
    return None


# --- Checks ---
def check_coverage(da_files, tracker_items):
    """Check 1: DA files vs tracker entries."""
    da_count = len(da_files)
    tracker_count = len(tracker_items)

    # Extract tickers from DA files
    da_tickers = set()
    for f in da_files:
        parts = Path(f).parts
        # ticker is parent directory name
        ticker_idx = -2  # e.g., .../research/HLNE/devils_advocate.md
        if len(parts) > 1:
            da_tickers.add(parts[ticker_idx])

    # Extract tickers from tracker
    tracker_tickers = set()
    for item in tracker_items:
        ticker = item.get('ticker', '')
        if ticker and ticker != 'SYSTEM':
            tracker_tickers.add(ticker)

    # DAs without any tracker entry
    untracked_tickers = da_tickers - tracker_tickers

    coverage_pct = (tracker_count / da_count * 100) if da_count > 0 else 0

    return {
        'da_count': da_count,
        'tracker_count': tracker_count,
        'coverage_pct': coverage_pct,
        'da_tickers': sorted(da_tickers),
        'tracker_tickers': sorted(tracker_tickers),
        'untracked_tickers': sorted(untracked_tickers),
    }


def check_staleness(open_items):
    """Check 2: Open items past deadline or >7d old."""
    overdue = []       # >7 days old
    critical = []      # >14 days old
    approaching = []   # deadline within 7 days

    for item in open_items:
        item_id = item.get('id', '?')
        ticker = item.get('ticker', '?')
        finding = item.get('finding', '')[:60]
        item_type = item.get('type', '?')
        deadline = parse_date(item.get('deadline'))
        created = extract_created_date(item)

        # Days since created
        if created:
            age_days = (TODAY - created).days
        else:
            age_days = None

        # Days until deadline
        if deadline:
            days_to_deadline = (deadline - TODAY).days
        else:
            days_to_deadline = None

        entry = {
            'id': item_id,
            'ticker': ticker,
            'finding': finding,
            'type': item_type,
            'deadline': str(deadline) if deadline else 'none',
            'age_days': age_days,
            'days_to_deadline': days_to_deadline,
        }

        # Check if overdue (past deadline)
        if deadline and days_to_deadline is not None and days_to_deadline < 0:
            critical.append(entry)
        elif deadline and days_to_deadline is not None and days_to_deadline <= 7:
            approaching.append(entry)

        # Check age-based staleness
        if age_days is not None:
            if age_days > 14:
                if entry not in critical:
                    critical.append(entry)
            elif age_days > 7:
                overdue.append(entry)

    return {
        'overdue': overdue,
        'critical': critical,
        'approaching': approaching,
    }


def check_pipeline_violations(open_items):
    """Check 3: Anomalies unresolved but ticker advanced past them."""
    violations = []

    anomaly_items = [i for i in open_items if i.get('type') == 'ANOMALY']

    for item in anomaly_items:
        ticker = item.get('ticker', '')
        if not ticker or ticker == 'SYSTEM':
            continue

        item_id = item.get('id', '?')

        # Get the approximate date of this anomaly
        created = extract_created_date(item)
        if not created:
            continue

        # Check if R3/R4 files exist and are NEWER than the anomaly
        advancement_files = get_r3_r4_files(ticker)

        for stage, info in advancement_files.items():
            if info['mtime'] > created:
                violations.append({
                    'id': item_id,
                    'ticker': ticker,
                    'anomaly_date': str(created),
                    'advancement': stage.upper(),
                    'advancement_date': str(info['mtime']),
                    'finding': item.get('finding', '')[:60],
                })

    return violations


def check_resolution_quality(all_items):
    """Check 4: Resolved items with empty evidence = rubber-stamping."""
    rubber_stamps = []
    good_resolutions = 0

    resolved = [i for i in all_items if i.get('status') == 'RESOLVED']

    for item in resolved:
        answer = item.get('answer', '').strip()
        evidence = item.get('evidence', '').strip()
        resolution = answer or evidence

        if not resolution or len(resolution) < 10:
            rubber_stamps.append({
                'id': item.get('id', '?'),
                'ticker': item.get('ticker', '?'),
                'finding': item.get('finding', '')[:60],
            })
        else:
            good_resolutions += 1

    return {
        'rubber_stamps': rubber_stamps,
        'good_resolutions': good_resolutions,
        'total_resolved': len(resolved),
    }


def check_freshness(tracker_mtime, latest_agent_run):
    """Check 5: Tracker freshness vs latest agent run."""
    if not tracker_mtime or not latest_agent_run:
        return {
            'tracker_mtime': str(tracker_mtime),
            'latest_agent': str(latest_agent_run),
            'gap_days': None,
            'stale': True,
        }

    gap = (latest_agent_run - tracker_mtime).days

    return {
        'tracker_mtime': str(tracker_mtime),
        'latest_agent': str(latest_agent_run),
        'gap_days': gap,
        'stale': gap > 1,  # Tracker should be updated same day or day after agent runs
    }


# --- Compliance score ---
def calculate_compliance_score(coverage, staleness, violations, resolution, freshness):
    """Calculate compliance score 0-100 with deductions."""
    score = 100
    deductions = []

    # Coverage penalty: if DAs >> tracker items
    if coverage['coverage_pct'] < 50:
        penalty = 15
        score -= penalty
        deductions.append(f"-{penalty}: low coverage ({coverage['da_count']} DAs, only {coverage['tracker_count']} tracked)")
    elif coverage['coverage_pct'] < 75:
        penalty = 8
        score -= penalty
        deductions.append(f"-{penalty}: moderate coverage gap ({coverage['coverage_pct']:.0f}%)")

    # Staleness penalties
    n_overdue = len(staleness['overdue'])
    n_critical = len(staleness['critical'])
    if n_critical > 0:
        penalty = min(20, n_critical * 10)
        score -= penalty
        deductions.append(f"-{penalty}: {n_critical} critical items (past deadline or >14d)")
    if n_overdue > 0:
        penalty = min(10, n_overdue * 3)
        score -= penalty
        deductions.append(f"-{penalty}: {n_overdue} overdue items (>7d)")

    # Pipeline violations
    n_violations = len(violations)
    if n_violations > 0:
        penalty = min(25, n_violations * 12)
        score -= penalty
        deductions.append(f"-{penalty}: {n_violations} pipeline violation(s) (advanced despite open anomaly)")

    # Rubber-stamp risk
    n_stamps = len(resolution['rubber_stamps'])
    if n_stamps > 0:
        penalty = min(10, n_stamps * 5)
        score -= penalty
        deductions.append(f"-{penalty}: {n_stamps} rubber-stamp resolution(s) (empty evidence)")

    # Freshness gap
    if freshness.get('stale'):
        gap = freshness.get('gap_days')
        if gap and gap > 3:
            penalty = 10
            score -= penalty
            deductions.append(f"-{penalty}: tracker {gap}d behind latest agent run")
        elif gap and gap > 1:
            penalty = 5
            score -= penalty
            deductions.append(f"-{penalty}: tracker {gap}d behind latest agent run")
        elif gap is None and freshness.get('tracker_mtime') is None:
            penalty = 15
            score -= penalty
            deductions.append(f"-{penalty}: no tracker file found")

    return max(0, score), deductions


# --- Output ---
def print_report(coverage, staleness, violations, resolution, freshness, score, deductions, all_items, verbose=False):
    """Print the compliance audit report."""
    open_items = [i for i in all_items if i.get('status') != 'RESOLVED']
    resolved_items = [i for i in all_items if i.get('status') == 'RESOLVED']

    # Category counts
    categories = {}
    for item in all_items:
        cat = item.get('type', 'UNKNOWN')
        categories[cat] = categories.get(cat, 0) + 1

    print(f"META-REFLECTION COMPLIANCE AUDIT -- {TODAY}")
    print("=" * 56)
    print(f"DAs completed:        {coverage['da_count']}")
    tracker_warning = ""
    if coverage['coverage_pct'] < 50:
        tracker_warning = f"  (COVERAGE: {coverage['coverage_pct']:.1f}% -- WARNING: many items likely untracked)"
    elif coverage['coverage_pct'] < 75:
        tracker_warning = f"  (COVERAGE: {coverage['coverage_pct']:.1f}%)"
    print(f"Tracker items:        {coverage['tracker_count']}{tracker_warning}")
    print(f"  OPEN:               {len(open_items)}")
    print(f"  RESOLVED:           {len(resolved_items)}")
    print(f"  OVERDUE (>7d):      {len(staleness['overdue'])}")
    print(f"  CRITICAL (>14d):    {len(staleness['critical'])}")
    print()

    print(f"PIPELINE VIOLATIONS:  {len(violations)}  ", end="")
    if violations:
        print("(ticker advanced despite open anomaly)")
    else:
        print("(no ticker advanced despite open anomaly)")

    print(f"RUBBER-STAMP RISK:    {len(resolution['rubber_stamps'])}  ", end="")
    if resolution['rubber_stamps']:
        print("(resolutions without evidence)")
    else:
        print("(all resolutions have evidence)")
    print()

    print(f"COMPLIANCE SCORE:     {score}/100")
    for d in deductions:
        print(f"  {d}")
    if not deductions:
        print("  (no deductions)")
    print()

    # Pipeline violations detail
    if violations:
        print("PIPELINE VIOLATIONS:")
        for v in violations:
            print(f"  {v['id']}  {v['ticker']}  anomaly {v['anomaly_date']} but {v['advancement']} on {v['advancement_date']}")
            print(f"         {v['finding']}")
        print()

    # Overdue + critical items
    all_flagged = staleness['critical'] + staleness['overdue'] + staleness['approaching']
    if all_flagged:
        print("FLAGGED ITEMS:")
        # Deduplicate by id
        seen = set()
        for item in all_flagged:
            if item['id'] in seen:
                continue
            seen.add(item['id'])
            label = ""
            if item in staleness['critical']:
                label = "CRITICAL"
            elif item in staleness['overdue']:
                label = "OVERDUE"
            elif item in staleness['approaching']:
                label = "APPROACHING"

            age_str = f"{item['age_days']}d" if item['age_days'] is not None else "?d"
            deadline_str = item['deadline']

            print(f"  {item['id']:8s}  {item['ticker']:12s}  {age_str:>4s}  {item['type']:12s}  deadline {deadline_str}  {label}")
        print()

    # Next deadlines
    deadlines = []
    for item in open_items:
        dl = parse_date(item.get('deadline'))
        if dl:
            deadlines.append((dl, item.get('id', '?'), item.get('ticker', '?'), item.get('finding', '')[:50]))
    deadlines.sort()

    if deadlines:
        print("NEXT DEADLINES:")
        for dl, item_id, ticker, finding in deadlines[:5]:
            days_left = (dl - TODAY).days
            flag = ""
            if days_left < 0:
                flag = " <-- PAST DUE"
            elif days_left <= 7:
                flag = " <-- APPROACHING"
            print(f"  {dl}  {item_id:8s}  {ticker:12s}  {finding}{flag}")
        print()

    # Categories
    if categories:
        print("ITEMS BY CATEGORY:")
        for cat, count in sorted(categories.items()):
            print(f"  {cat:12s}  {count}")
        print()

    # Freshness
    print("FRESHNESS:")
    print(f"  Tracker last modified: {freshness['tracker_mtime']}")
    print(f"  Latest agent output:   {freshness['latest_agent']}")
    if freshness.get('gap_days') is not None:
        gap = freshness['gap_days']
        status = "OK" if gap <= 1 else f"STALE ({gap}d gap)"
        print(f"  Status:                {status}")
    else:
        print(f"  Status:                UNKNOWN")
    print()

    # Untracked tickers
    if coverage['untracked_tickers']:
        print(f"UNTRACKED DA TICKERS ({len(coverage['untracked_tickers'])} DAs without tracker entry):")
        # Show in rows of 8
        tickers = coverage['untracked_tickers']
        for i in range(0, len(tickers), 8):
            chunk = tickers[i:i+8]
            print(f"  {', '.join(chunk)}")
        print()

    # Verbose: all items
    if verbose:
        print("ALL TRACKER ITEMS:")
        print(f"  {'ID':8s}  {'Ticker':12s}  {'Type':12s}  {'Status':10s}  {'Deadline':12s}  Finding")
        print(f"  {'---':8s}  {'---':12s}  {'---':12s}  {'---':10s}  {'---':12s}  ---")
        for item in all_items:
            print(f"  {item.get('id','?'):8s}  {item.get('ticker','?'):12s}  {item.get('type','?'):12s}  "
                  f"{item.get('status','?'):10s}  {str(item.get('deadline','none')):12s}  "
                  f"{item.get('finding','')[:55]}")
        print()

    print("[Verifiable by human. No AI interpretation needed.]")


def print_json_report(coverage, staleness, violations, resolution, freshness, score, deductions, all_items):
    """Print machine-readable JSON output."""
    report = {
        'date': str(TODAY),
        'compliance_score': score,
        'deductions': deductions,
        'coverage': {
            'da_count': coverage['da_count'],
            'tracker_count': coverage['tracker_count'],
            'coverage_pct': round(coverage['coverage_pct'], 1),
            'untracked_tickers': coverage['untracked_tickers'],
        },
        'staleness': {
            'overdue': len(staleness['overdue']),
            'critical': len(staleness['critical']),
            'approaching': len(staleness['approaching']),
        },
        'violations': violations,
        'resolution_quality': {
            'rubber_stamps': len(resolution['rubber_stamps']),
            'good_resolutions': resolution['good_resolutions'],
            'total_resolved': resolution['total_resolved'],
        },
        'freshness': freshness,
        'items': all_items,
    }
    print(json.dumps(report, indent=2, default=str))


# --- Main ---
def main():
    parser = argparse.ArgumentParser(
        description="Meta-reflection compliance auditor. Checks orchestrator compliance with agent meta-reflections."
    )
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="Show all tracker items in detail")
    parser.add_argument('--json', action='store_true',
                        help="Machine-readable JSON output")
    args = parser.parse_args()

    # Load tracker
    tracker_data = load_tracker()
    if tracker_data is None:
        print(f"META-REFLECTION COMPLIANCE AUDIT -- {TODAY}")
        print("=" * 56)
        print("NO TRACKER FOUND at:")
        print(f"  {TRACKER_PATH}")
        print()
        print("COMPLIANCE SCORE: 0/100")
        print("  -100: no meta_reflection_tracker.yaml exists")
        print()
        print("The orchestrator has NO mechanism to track agent meta-reflections.")
        print("Every DA output's anomalies, suggestions, and questions are being silently dropped.")
        print()
        da_files = count_da_files()
        print(f"DAs completed: {len(da_files)} (ALL untracked)")
        print()
        print("[Verifiable by human. No AI interpretation needed.]")
        return

    # Extract items
    all_items = tracker_data.get('open_items', [])
    if all_items is None:
        all_items = []

    open_items = [i for i in all_items if i.get('status') != 'RESOLVED']

    # Run all checks
    da_files = count_da_files()
    coverage = check_coverage(da_files, all_items)
    staleness_result = check_staleness(open_items)
    violations = check_pipeline_violations(open_items)
    resolution = check_resolution_quality(all_items)

    tracker_mtime = get_tracker_mtime()
    latest_agent = get_latest_agent_run()
    freshness = check_freshness(tracker_mtime, latest_agent)

    score, deductions = calculate_compliance_score(
        coverage, staleness_result, violations, resolution, freshness
    )

    # Output
    if args.json:
        print_json_report(coverage, staleness_result, violations, resolution, freshness, score, deductions, all_items)
    else:
        print_report(coverage, staleness_result, violations, resolution, freshness, score, deductions, all_items, verbose=args.verbose)


if __name__ == '__main__':
    main()

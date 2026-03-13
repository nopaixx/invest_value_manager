#!/usr/bin/env python3
"""
Thesis Summary Tool v1.0
Extract thesis headers, KCs, and key metrics in ~20 lines instead of
reading 400-700 line thesis files. Saves 90% of context window.

Usage:
    python3 tools/thesis_summary.py TICKER          # Single ticker
    python3 tools/thesis_summary.py --all            # All active positions
    python3 tools/thesis_summary.py --pipeline       # All research pipeline
    python3 tools/thesis_summary.py --compact        # Ultra-compact one-liner per ticker
    python3 tools/thesis_summary.py --shorts         # Active + research shorts

Note: NO network calls. Reads local files only. Fast.
"""

import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Thesis search paths in priority order
THESIS_PATHS = [
    ('active',         'thesis/active'),
    ('research',       'thesis/research'),
    ('short_active',   'thesis/short/active'),
    ('short_research', 'thesis/short/research'),
]

# KC status keywords and priority
KC_STATUS_KEYWORDS = ["TRIGGERED", "MONITORING", "AMBER", "PENDING", "WATCHING",
                      "NEW", "DORMANT", "OK", "CLEAR"]


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def find_thesis(ticker):
    """Find thesis.md for a ticker. Returns (location_type, full_path, rel_path) or None."""
    for loc_type, subdir in THESIS_PATHS:
        path = os.path.join(BASE_DIR, subdir, ticker, 'thesis.md')
        if os.path.exists(path):
            rel = os.path.join(subdir, ticker, 'thesis.md')
            return loc_type, path, rel
    return None


def get_active_tickers():
    """Get tickers from portfolio/current.yaml."""
    path = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
    if not os.path.exists(path):
        return []
    if yaml:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        tickers = []
        for pos in data.get('positions', []):
            if isinstance(pos, dict) and 'ticker' in pos:
                tickers.append(pos['ticker'])
        for pos in data.get('short_positions', []):
            if isinstance(pos, dict) and 'ticker' in pos:
                tickers.append(pos['ticker'])
        return tickers
    # Fallback: regex parse
    tickers = []
    with open(path, 'r') as f:
        for line in f:
            m = re.match(r'\s*-\s*ticker:\s*(\S+)', line)
            if m:
                tickers.append(m.group(1))
    return tickers


def get_pipeline_tickers():
    """Get tickers from thesis/research/ directories."""
    tickers = []
    research_dir = os.path.join(BASE_DIR, 'thesis', 'research')
    if os.path.isdir(research_dir):
        for name in sorted(os.listdir(research_dir)):
            thesis_path = os.path.join(research_dir, name, 'thesis.md')
            if os.path.isfile(thesis_path) and not name.startswith('_'):
                tickers.append(name)
    return tickers


def get_short_tickers():
    """Get tickers from short thesis directories."""
    tickers = []
    for subdir in ['thesis/short/active', 'thesis/short/research']:
        full_dir = os.path.join(BASE_DIR, subdir)
        if os.path.isdir(full_dir):
            for name in sorted(os.listdir(full_dir)):
                thesis_path = os.path.join(full_dir, name, 'thesis.md')
                if os.path.isfile(thesis_path) and not name.startswith('_'):
                    tickers.append(name)
    return tickers


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_header(content):
    """Parse the thesis header block (lines starting with > before first ---)."""
    header_lines = []
    in_header = False
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('>'):
            in_header = True
            header_lines.append(stripped)
        elif stripped == '---' and in_header:
            break
        elif in_header and not stripped:
            continue  # skip blank lines within header area
        elif in_header and not stripped.startswith('>'):
            # Some headers have non-quote lines mixed in (title, date, etc.)
            if re.match(r'^\*\*', stripped) or re.match(r'^#', stripped):
                header_lines.append(stripped)
            elif stripped == '---':
                break
    return header_lines


def extract_field(header_lines, content, patterns):
    """Extract a field using multiple regex patterns. Search header first, then first 30 lines."""
    header_text = '\n'.join(header_lines)
    for pat in patterns:
        m = re.search(pat, header_text, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    first_lines = '\n'.join(content.split('\n')[:30])
    for pat in patterns:
        m = re.search(pat, first_lines, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None


def extract_fair_value(header_lines, content):
    """Extract Fair Value from thesis."""
    raw = extract_field(header_lines, content, [
        r'\*\*Fair Value:\*\*\s*(.+)',
        r'Fair Value:\s*(.+)',
    ])
    if not raw:
        return 'N/A'
    # Clean: take value before first parenthetical, but keep currency symbol
    m = re.match(r'((?:\$|EUR|SEK|DKK|GBP|GBp)?\s*[\d,]+(?:\.\d+)?\s*(?:GBp|DKK|SEK|EUR)?)', raw)
    if m:
        return m.group(1).strip()
    return raw[:30]


def extract_growth(header_lines, content):
    """Extract Expected Growth from thesis."""
    raw = extract_field(header_lines, content, [
        r'\*\*Expected Growth:\*\*\s*(.+)',
        r'Expected Growth:\s*(.+)',
    ])
    if not raw:
        return 'N/A'
    m = re.search(r'(\d+(?:\.\d+)?)\s*%', raw)
    if m:
        return f"{m.group(1)}%"
    return raw[:15]


def extract_qs(header_lines, content):
    """Extract Quality Score from thesis. Returns (tool_score, adjusted_score, tier).

    Searches the full content for QS Tool/Adjusted blocks (they can be deep in the file),
    but also checks header/first lines for 'Quality Score: NN/100' shorthand."""
    header_text = '\n'.join(header_lines)
    # Search full content for QS Tool / QS Adjusted (the Quality Score section)
    tool_qs = None
    adj_qs = None
    tier = None

    # QS Tool: NN/100 (anywhere in content)
    m = re.search(r'QS Tool:?\s*(\d+)\s*/\s*100', content)
    if m:
        tool_qs = int(m.group(1))

    # QS Adjusted: NN/100 (anywhere in content)
    m = re.search(r'QS Adjusted:?\s*(\d+)\s*/\s*100', content)
    if m:
        adj_qs = int(m.group(1))

    # Fallback: Quality Score: NN/100 in header/first lines
    if not tool_qs and not adj_qs:
        first_area = header_text + '\n' + '\n'.join(content.split('\n')[:15])
        m = re.search(r'\*?\*?Quality Score\*?\*?:?\s*(\d+)\s*/\s*100', first_area, re.IGNORECASE)
        if m:
            tool_qs = int(m.group(1))

    # Tier from header area first, then full content
    first_area = header_text + '\n' + '\n'.join(content.split('\n')[:40])
    m = re.search(r'Tier\s+([A-D])\b', first_area, re.IGNORECASE)
    if m:
        tier = m.group(1).upper()

    # Derive tier if not found
    if not tier:
        score = adj_qs or tool_qs
        if score:
            if score >= 75: tier = 'A'
            elif score >= 55: tier = 'B'
            elif score >= 35: tier = 'C'
            else: tier = 'D'

    return tool_qs, adj_qs, tier


def extract_pipeline_stage(header_lines, content):
    """Extract pipeline stage."""
    return extract_field(header_lines, content, [
        r'Pipeline Stage:\s*(\S+)',
        r'\*\*Pipeline Stage:\*\*\s*(\S+)',
    ]) or 'N/A'


def extract_verdict(header_lines, content):
    """Extract verdict/recommendation."""
    raw = extract_field(header_lines, content, [
        r'\*\*(?:Verdict|Recommendation):\*\*\s*(.+)',
        r'(?:Verdict|Recommendation):\s*(.+)',
    ])
    if not raw:
        return 'N/A'
    m = re.match(r'(HOLD|BUY|SELL|WATCHLIST|WATCH|ADD|TRIM|EXIT|AVOID|RESEARCH|CONDITIONAL\s+\w+)', raw, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    return raw[:20]


def extract_ecagr(content):
    """Extract E[CAGR] from thesis content. Prefer the E[CAGR] Calculation section."""
    # First look for the dedicated E[CAGR] Calculation section
    m = re.search(r'#{2,3}\s+E\[CAGR\]\s+Calculation.*?\n(.*?)(?:\n---|\n#{2,3}\s)', content, re.DOTALL | re.IGNORECASE)
    if m:
        section = m.group(1)
        # Find E[CAGR] value in this section
        m2 = re.search(r'E\[CAGR\]\s*[:=~]+\s*~?(\d+(?:\.\d+)?)\s*%', section, re.IGNORECASE)
        if m2:
            return f"{m2.group(1)}%"

    # Fallback: any E[CAGR] mention in the file
    patterns = [
        r'E\[CAGR\]\s*[:=~]+\s*~?(\d+(?:\.\d+)?)\s*%',
        r'E\[CAGR\]\s*(?:of\s+)?~?\s*(\d+(?:\.\d+)?)\s*%',
        r'E\[CAGR\]@?(?:market|mkt)?\s*[:=~]+\s*~?(\d+(?:\.\d+)?)\s*%',
    ]
    for pat in patterns:
        m = re.search(pat, content, re.IGNORECASE)
        if m:
            return f"{m.group(1)}%"
    return 'N/A'


def _detect_table_format(header_row):
    """Detect KC status table format from header row.
    Returns 'four_col' for | KC# | Condition | Status | Notes |
    or 'three_col' for | Kill Condition | Status | Notes |"""
    if 'KC#' in header_row:
        return 'four_col'
    return 'three_col'


def parse_kc_status_table(content):
    """Parse the Kill Conditions Status table. Handles both 3-col and 4-col formats.
    Returns list of (kc_num, condition, status, notes)."""
    kcs = []
    lines = content.split('\n')
    in_table = False
    header_found = False
    table_format = 'four_col'

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Find the status table section
        if re.match(r'^(?:#{2,3}\s+|\*\*)?Kill\s+Conditions?\s+Status', stripped, re.IGNORECASE):
            header_found = True
            continue

        if not header_found:
            continue

        # Detect table header row and format
        if '|' in stripped and not in_table:
            if 'KC#' in stripped or 'Condition' in stripped or 'Kill Condition' in stripped or 'Status' in stripped:
                table_format = _detect_table_format(stripped)
                in_table = True
                continue
        # Skip separator row
        if re.match(r'^\|[\s\-|]+\|$', stripped):
            in_table = True
            continue

        # End of table
        if in_table and not stripped.startswith('|'):
            if stripped == '' or stripped.startswith('#') or stripped == '---':
                break
            continue

        if not in_table:
            continue

        # Parse table row
        cells = [c.strip() for c in stripped.split('|')]
        cells = [c for c in cells if c]  # remove empty from leading/trailing |

        if len(cells) < 2:
            continue

        if table_format == 'four_col' and len(cells) >= 3:
            # | KC# | Condition | Status | Notes |
            kc_num_raw = cells[0]
            condition = cells[1]
            status_raw = cells[2]
            notes = cells[3] if len(cells) >= 4 else ''
        elif len(cells) >= 2:
            # | Kill Condition (with number) | Status | Notes |
            # e.g. "1. Francia caps" or "13. France 8% social levy tabled"
            kc_num_raw = cells[0]
            status_raw = cells[1]
            notes = cells[2] if len(cells) >= 3 else ''
            # Extract condition from the first cell (strip number prefix)
            condition = re.sub(r'^\d+\.\s*', '', kc_num_raw).strip()
        else:
            continue

        # Extract KC number
        m = re.search(r'(\d+)', kc_num_raw)
        kc_num = int(m.group(1)) if m else 0

        # Extract status keyword (strip bold markers)
        status = 'UNKNOWN'
        status_clean = re.sub(r'\*', '', status_raw).strip()
        for kw in KC_STATUS_KEYWORDS:
            if kw in status_clean.upper():
                status = kw
                break

        # Clean condition: strip bold markers
        condition = re.sub(r'\*\*', '', condition).strip()

        # Truncate for display
        if len(condition) > 40:
            condition = condition[:37] + '...'
        if len(notes) > 50:
            notes = notes[:47] + '...'

        kcs.append((kc_num, condition, status, notes))

    return kcs


def parse_kc_list(content):
    """Fallback: parse KCs from numbered list if no status table exists."""
    kcs = []
    lines = content.split('\n')
    in_kc = False

    for line in lines:
        stripped = line.strip()
        if re.match(r'^#{2,3}\s+Kill\s+Conditions\b', stripped, re.IGNORECASE):
            if 'status' not in stripped.lower():
                in_kc = True
                continue

        if in_kc:
            if re.match(r'^#{2,3}\s+', stripped) or stripped == '---':
                break
            m = re.match(r'^(\d+)\.\s+(.+)', stripped)
            if m:
                kc_num = int(m.group(1))
                desc = re.sub(r'\*\*', '', m.group(2)).strip()
                desc_clean = re.sub(r'^KC#\d+:\s*', '', desc)
                desc_short = desc_clean.split('.')[0] if '.' in desc_clean else desc_clean
                if len(desc_short) > 40:
                    desc_short = desc_short[:37] + '...'
                kcs.append((kc_num, desc_short, 'UNKNOWN', ''))

    return kcs


def _load_current_yaml():
    """Load and cache portfolio/current.yaml."""
    if not hasattr(_load_current_yaml, '_cache'):
        path = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
        if not os.path.exists(path) or not yaml:
            _load_current_yaml._cache = None
        else:
            with open(path, 'r') as f:
                _load_current_yaml._cache = yaml.safe_load(f)
    return _load_current_yaml._cache


def get_exit_plan(ticker):
    """Get exit_plan from portfolio/current.yaml for active positions."""
    data = _load_current_yaml()
    if not data:
        return None
    for pos in data.get('positions', []) + data.get('short_positions', []):
        if isinstance(pos, dict) and pos.get('ticker') == ticker:
            return pos.get('exit_plan')
    return None


def get_last_review(ticker):
    """Get last_review from portfolio/current.yaml."""
    data = _load_current_yaml()
    if not data:
        return None
    for pos in data.get('positions', []) + data.get('short_positions', []):
        if isinstance(pos, dict) and pos.get('ticker') == ticker:
            return pos.get('last_review')
    return None


# ---------------------------------------------------------------------------
# Summary generation
# ---------------------------------------------------------------------------

def summarize_ticker(ticker, verbose=True):
    """Generate summary for a single ticker. Returns dict with all fields."""
    result = find_thesis(ticker)
    if not result:
        return None

    loc_type, full_path, rel_path = result
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    line_count = content.count('\n') + 1
    header_lines = parse_header(content)

    # Extract fields
    fv = extract_fair_value(header_lines, content)
    growth = extract_growth(header_lines, content)
    tool_qs, adj_qs, tier = extract_qs(header_lines, content)
    stage = extract_pipeline_stage(header_lines, content)
    verdict = extract_verdict(header_lines, content)
    ecagr = extract_ecagr(content)

    # Format QS
    if tool_qs and adj_qs and tool_qs != adj_qs:
        qs_str = f"{tool_qs}/{adj_qs}"
    elif adj_qs:
        qs_str = str(adj_qs)
    elif tool_qs:
        qs_str = str(tool_qs)
    else:
        qs_str = 'N/A'
    if tier:
        qs_str += f" (Tier {tier})"

    # KCs
    kcs = parse_kc_status_table(content)
    if not kcs:
        kcs = parse_kc_list(content)

    # Exit plan and last review (active positions only)
    exit_plan = get_exit_plan(ticker) if loc_type in ('active', 'short_active') else None
    last_review = get_last_review(ticker) if loc_type in ('active', 'short_active') else None

    # KC summary stats
    n_triggered = sum(1 for _, _, s, _ in kcs if s == 'TRIGGERED')
    n_monitoring = sum(1 for _, _, s, _ in kcs if s in ('MONITORING', 'AMBER'))
    n_total = len(kcs)

    return {
        'ticker': ticker,
        'rel_path': rel_path,
        'loc_type': loc_type,
        'line_count': line_count,
        'fv': fv,
        'growth': growth,
        'qs_str': qs_str,
        'tier': tier or '?',
        'stage': stage,
        'verdict': verdict,
        'ecagr': ecagr,
        'kcs': kcs,
        'n_triggered': n_triggered,
        'n_monitoring': n_monitoring,
        'n_total': n_total,
        'exit_plan': exit_plan,
        'last_review': last_review,
    }


def print_full(data):
    """Print full summary for one ticker."""
    title = data['ticker']
    print(f"\n=== {title} ===")
    print(f"Location: {data['rel_path']} ({data['line_count']} lines)")
    print(f"FV: {data['fv']} | Growth: {data['growth']} | QS: {data['qs_str']} | Stage: {data['stage']}")
    print(f"E[CAGR]: {data['ecagr']} | Verdict: {data['verdict']}")

    if data['last_review']:
        print(f"Last Review: {data['last_review']}")

    if data['exit_plan']:
        ep = data['exit_plan']
        if len(ep) > 100:
            ep = ep[:97] + '...'
        print(f"Exit Plan: {ep}")

    # Kill Conditions
    if data['kcs']:
        print(f"\nKill Conditions ({data['n_total']}):")
        for kc_num, condition, status, notes in data['kcs']:
            status_marker = ''
            if status == 'TRIGGERED':
                status_marker = ' <<<'
            elif status in ('MONITORING', 'AMBER'):
                status_marker = ' <'

            notes_str = f'  ({notes})' if notes else ''
            print(f"  KC#{kc_num:<2} {condition:<42} {status:<12}{notes_str}{status_marker}")
    else:
        print("\nKill Conditions: None found")

    print()


def print_compact(summaries):
    """Print compact one-liner table for multiple tickers."""
    print(f"\n{'TICKER':<10} {'FV':<12} {'Growth':<8} {'QS':<10} {'Stage':<16} {'E[CAGR]':<10} {'KCs':<8}")
    print('-' * 78)

    for d in summaries:
        # KC summary: {triggered}T/{monitoring}M/{total}
        kc_parts = []
        if d['n_triggered'] > 0:
            kc_parts.append(f"{d['n_triggered']}T")
        if d['n_monitoring'] > 0:
            kc_parts.append(f"{d['n_monitoring']}M")
        kc_parts.append(str(d['n_total']))
        kc_str = '/'.join(kc_parts)

        # QS compact: score/tier
        qs_score = ''
        if d.get('qs_str') and d['qs_str'] != 'N/A':
            qs_score = d['qs_str'].split(' ')[0]  # Just the number part
        tier_letter = d.get('tier', '?')
        qs_compact = f"{qs_score}/{tier_letter}" if qs_score else 'N/A'

        print(f"{d['ticker']:<10} {d['fv']:<12} {d['growth']:<8} {qs_compact:<10} {d['stage']:<16} {d['ecagr']:<10} {kc_str:<8}")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Thesis Summary Tool -- extract key metrics from thesis files without reading full content.'
    )
    parser.add_argument('ticker', nargs='?', help='Ticker to summarize')
    parser.add_argument('--all', action='store_true', help='All active positions')
    parser.add_argument('--pipeline', action='store_true', help='All research pipeline tickers')
    parser.add_argument('--shorts', action='store_true', help='Active + research shorts')
    parser.add_argument('--compact', action='store_true', help='Ultra-compact one-liner per ticker')
    args = parser.parse_args()

    # Determine which tickers to process
    tickers = []
    if args.ticker:
        tickers = [args.ticker]
    elif args.all:
        tickers = get_active_tickers()
        if not tickers:
            print("No active positions found in portfolio/current.yaml")
            sys.exit(1)
    elif args.pipeline:
        tickers = get_pipeline_tickers()
        if not tickers:
            print("No research pipeline tickers found")
            sys.exit(1)
    elif args.shorts:
        tickers = get_short_tickers()
        if not tickers:
            print("No short thesis tickers found")
            sys.exit(1)
    elif args.compact:
        # Default compact to all active
        tickers = get_active_tickers()
        if not tickers:
            print("No active positions found in portfolio/current.yaml")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    # Process tickers
    summaries = []
    not_found = []
    for t in tickers:
        data = summarize_ticker(t)
        if data:
            summaries.append(data)
        else:
            not_found.append(t)

    if not summaries:
        print(f"No thesis files found for: {', '.join(tickers)}")
        sys.exit(1)

    # Output
    if args.compact:
        print_compact(summaries)
    else:
        for d in summaries:
            print_full(d)

    # Warnings
    if not_found:
        print(f"[!] No thesis found for: {', '.join(not_found)}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
FV Accuracy Tracker v2.0 — Measures Fair Value prediction accuracy over time.

Compares historical FV estimates against actual price evolution to measure:
  - Convergence rate (did price move toward FV?)
  - Hit rate (did price reach within 10% of FV within 12 months?)
  - Directional bias (systematic over/under-estimation)
  - Mean Absolute Error
  - Time to convergence
  - Accuracy by QS tier
  - FV revision history (from git)
  - Closed position accuracy (exit price vs FV)

Data sources:
  - thesis/active/*/thesis.md — current FVs
  - thesis/archive/*/thesis.md — historical FVs
  - thesis/research/*/thesis.md — pipeline FVs
  - portfolio/current.yaml — open positions with dates
  - portfolio/history.yaml — closed positions with entry/exit FVs
  - Git history — FV revision timeline per ticker
  - yfinance — historical + current prices

Usage:
  python3 tools/fv_accuracy.py               # Summary report
  python3 tools/fv_accuracy.py --detail       # Per-ticker breakdown
  python3 tools/fv_accuracy.py --bias         # Systematic bias analysis
  python3 tools/fv_accuracy.py --ticker ADBE  # Single ticker deep dive
  python3 tools/fv_accuracy.py --active-only  # Only current portfolio
"""

import sys
import os
import re
import argparse
import subprocess
from datetime import datetime, timedelta, date
from collections import defaultdict

import yaml
import pandas as pd
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'tools'))
from thesis_parser import extract_fair_value, _detect_currency_from_context
from fx_defaults import FX_DEFAULTS

PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
HISTORY_FILE = os.path.join(BASE_DIR, 'portfolio', 'history.yaml')
THESIS_DIRS = [
    os.path.join(BASE_DIR, 'thesis', 'active'),
    os.path.join(BASE_DIR, 'thesis', 'archive'),
    os.path.join(BASE_DIR, 'thesis', 'research'),
]


# ---------------------------------------------------------------------------
# DataFrame helpers
# ---------------------------------------------------------------------------

def _flatten_columns(df):
    """Flatten MultiIndex columns from yfinance download."""
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]
    return df


# ---------------------------------------------------------------------------
# FX utilities
# ---------------------------------------------------------------------------

_fx_cache = {}

def get_fx_rates():
    """Fetch live FX rates with fallbacks."""
    if _fx_cache:
        return _fx_cache
    pairs = {
        'EURUSD': ('EURUSD=X', FX_DEFAULTS.get('EURUSD', 1.16)),
        'GBPUSD': ('GBPUSD=X', FX_DEFAULTS.get('GBPUSD', 1.34)),
        'DKKUSD': ('DKKUSD=X', 0.134),
        'SEKUSD': ('SEKUSD=X', 0.095),
        'CHFUSD': ('CHFUSD=X', FX_DEFAULTS.get('CHFUSD', 1.10)),
        'NOKUSD': ('NOKUSD=X', 0.092),
    }
    for key, (yf_sym, fallback) in pairs.items():
        try:
            t = yf.Ticker(yf_sym)
            info = t.fast_info if hasattr(t, 'fast_info') else t.info
            price = getattr(info, 'last_price', None) or info.get('regularMarketPrice')
            _fx_cache[key] = price if price else fallback
        except Exception:
            _fx_cache[key] = fallback
    return _fx_cache


def infer_currency(ticker):
    """Infer the native trading currency from the ticker suffix."""
    if ticker.endswith('.L'):
        return 'GBp'
    elif ticker.endswith('.PA') or ticker.endswith('.DE') or ticker.endswith('.AS') or ticker.endswith('.MI'):
        return 'EUR'
    elif ticker.endswith('.ST'):
        return 'SEK'
    elif ticker.endswith('.CO'):
        return 'DKK'
    elif ticker.endswith('.SW'):
        return 'CHF'
    elif ticker.endswith('.OL'):
        return 'NOK'
    return 'USD'


# ---------------------------------------------------------------------------
# Git history: track FV revisions over time
# ---------------------------------------------------------------------------

def get_fv_revisions_from_git(ticker):
    """Parse git history to find all FV changes for a ticker's thesis file.

    Returns list of dicts: [{date, fv, fv_text, commit_hash}, ...]
    sorted chronologically (oldest first).
    """
    # Try multiple paths
    paths_to_try = [
        f'thesis/active/{ticker}/thesis.md',
        f'thesis/archive/{ticker}/thesis.md',
        f'thesis/research/{ticker}/thesis.md',
    ]

    revisions = []
    for rel_path in paths_to_try:
        full_path = os.path.join(BASE_DIR, rel_path)
        try:
            result = subprocess.run(
                ['git', 'log', '--follow', '-p', '--', rel_path],
                capture_output=True, text=True, cwd=BASE_DIR, timeout=30
            )
            if result.returncode != 0 or not result.stdout:
                continue

            current_commit = None
            current_date = None

            for line in result.stdout.split('\n'):
                if line.startswith('commit '):
                    current_commit = line.split()[1][:8]
                elif line.startswith('Date:'):
                    try:
                        date_str = line[5:].strip()
                        # Parse git date format: "Fri Mar 7 15:45:30 2026 +0100"
                        dt = datetime.strptime(' '.join(date_str.split()[:5]), '%a %b %d %H:%M:%S %Y')
                        current_date = dt.date()
                    except (ValueError, IndexError):
                        pass
                elif current_date and re.match(r'^\+>?\s*\*{0,2}Fair Value', line):
                    # This is an added FV line
                    fv_text = line.lstrip('+').strip()
                    # Extract the numeric FV
                    m = re.search(r'(?:\$|EUR\s*|GBp?\s*|DKK\s*|SEK\s*)([0-9,]+(?:\.\d+)?)', fv_text)
                    if m:
                        try:
                            fv_val = float(m.group(1).replace(',', ''))
                            if fv_val > 0:
                                # Detect currency from the FV line
                                ccy = 'USD'
                                if 'EUR' in fv_text:
                                    ccy = 'EUR'
                                elif 'GBp' in fv_text.lower() or fv_text.rstrip().endswith('p'):
                                    ccy = 'GBp'
                                elif 'DKK' in fv_text:
                                    ccy = 'DKK'
                                elif 'SEK' in fv_text:
                                    ccy = 'SEK'
                                elif '$' in fv_text:
                                    ccy = 'USD'

                                revisions.append({
                                    'date': current_date,
                                    'fv': fv_val,
                                    'currency': ccy,
                                    'fv_text': fv_text[:80],
                                    'commit': current_commit,
                                })
                        except ValueError:
                            pass

            if revisions:
                break  # Found history in this path

        except (subprocess.TimeoutExpired, Exception):
            continue

    # Deduplicate by (date, fv) and sort chronologically
    seen = set()
    unique = []
    for r in revisions:
        key = (r['date'], r['fv'])
        if key not in seen:
            seen.add(key)
            unique.append(r)
    unique.sort(key=lambda x: x['date'])
    return unique


# ---------------------------------------------------------------------------
# Date extraction from thesis files
# ---------------------------------------------------------------------------

def extract_thesis_date(content):
    """Extract the analysis date from thesis content.
    Searches header area (first 2000 chars) for various date formats.
    Returns the EARLIEST date found (original analysis date)."""
    # Search only the header area to avoid matching dates deep in the document
    header = content[:2000]
    patterns = [
        # Explicit date fields: "Analysis Date:", "Date:", "Fecha:", "Original Date:"
        r'(?:Analysis Date|Original Date|Fecha|\*\*Date\*\*)[:\s*]+(\d{4}-\d{2}-\d{2})',
        # "Original:" field (common in updated theses)
        r'\*\*Original:\*\*\s*(\d{4}-\d{2}-\d{2})',
        r'(?:Original)[:\s]+(\d{4}-\d{2}-\d{2})',
        # R1 header line: "R1 Fundamental Analysis | Date: 2026-02-26" or "R1 ... | 2026-02-23"
        r'R1 Fundamental Analysis\s*\|\s*(?:Date:\s*)?(\d{4}-\d{2}-\d{2})',
        # Generic "Date: YYYY-MM-DD" in blockquote
        r'>\s*(?:\*\*)?Date(?:\*\*)?[:\s]+(\d{4}-\d{2}-\d{2})',
    ]
    dates_found = []
    for pat in patterns:
        for m in re.finditer(pat, header, re.IGNORECASE):
            try:
                d = datetime.strptime(m.group(1), '%Y-%m-%d').date()
                dates_found.append(d)
            except ValueError:
                continue
    if dates_found:
        return min(dates_found)  # Return earliest = original analysis date
    return None


def get_git_first_commit_date(rel_path):
    """Get the date of the first git commit for a file.
    Used as fallback when thesis content has no parseable date.
    Returns datetime.date or None."""
    try:
        result = subprocess.run(
            ['git', 'log', '--follow', '--diff-filter=A', '--format=%ai', '--', rel_path],
            capture_output=True, text=True, cwd=BASE_DIR, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            # Take last line (oldest commit)
            lines = result.stdout.strip().split('\n')
            date_str = lines[-1].strip().split()[0]  # "2026-02-04"
            return datetime.strptime(date_str, '%Y-%m-%d').date()
    except Exception:
        pass
    return None


def extract_quality_score(content):
    """Extract QS from thesis content. Returns (score, tier) or (None, None)."""
    patterns = [
        r'QS\s+(?:Tool[:\s]+)?(\d+)',        # "QS Tool: 74" or "QS Tool 74" or "QS 74"
        r'QS\*{0,2}[:\s]\s*(\d+)',            # "**QS:** 73" or "QS: 73"
        r'Quality Score[:\s]+(\d+)',            # "Quality Score: 74"
        r'QS\s+Tool[:\s]+\s*(\d+)',            # "QS Tool: 74/100"
    ]
    for pat in patterns:
        m = re.search(pat, content, re.IGNORECASE)
        if m:
            score = int(m.group(1))
            if score >= 75:
                tier = 'A'
            elif score >= 55:
                tier = 'B'
            elif score >= 35:
                tier = 'C'
            else:
                tier = 'D'
            return score, tier
    return None, None


def extract_pipeline_stage(content):
    """Extract pipeline stage from thesis content."""
    m = re.search(r'Pipeline\s*(?:Stage)?[:\s]+(\S+)', content, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'Status[:\s]+(R\d_\w+|S\d_\w+|ACTIVE|CLOSED|RESEARCH)', content, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return 'UNKNOWN'


# ---------------------------------------------------------------------------
# Historical price fetching
# ---------------------------------------------------------------------------

_price_cache = {}
_history_cache = {}


def _get_history_range(ticker, start_date, end_date):
    """Download and cache historical data for a ticker."""
    cache_key = (ticker, str(start_date), str(end_date))
    if cache_key in _history_cache:
        return _history_cache[cache_key]
    try:
        data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'),
                          end=end_date.strftime('%Y-%m-%d'), progress=False, auto_adjust=True)
        if data.empty:
            _history_cache[cache_key] = None
            return None
        data = _flatten_columns(data)
        _history_cache[cache_key] = data
        return data
    except Exception:
        _history_cache[cache_key] = None
        return None


def get_price_at_date(ticker, target_date, window_days=7):
    """Get the closing price at or near a target date.
    Returns (price, actual_date) or (None, None)."""
    cache_key = (ticker, str(target_date))
    if cache_key in _price_cache:
        return _price_cache[cache_key]

    start = target_date - timedelta(days=3)
    end = target_date + timedelta(days=window_days)
    data = _get_history_range(ticker, start, end)
    if data is None:
        _price_cache[cache_key] = (None, None)
        return None, None

    try:
        best = None
        best_diff = None
        for d in data.index:
            d_date = d.date() if hasattr(d, 'date') else d
            diff = abs((d_date - target_date).days)
            if best_diff is None or diff < best_diff:
                best_diff = diff
                best = d
        if best is not None:
            price = float(data.loc[best, 'Close'])
            result = (price, best.date() if hasattr(best, 'date') else best)
            _price_cache[cache_key] = result
            return result
    except Exception:
        pass

    _price_cache[cache_key] = (None, None)
    return None, None


def get_current_price(ticker):
    """Get the current/latest price for a ticker."""
    try:
        t = yf.Ticker(ticker)
        info = t.fast_info if hasattr(t, 'fast_info') else t.info
        price = getattr(info, 'last_price', None) or info.get('regularMarketPrice')
        if price:
            return float(price)
        hist = t.history(period='5d')
        if not hist.empty:
            return float(hist['Close'].iloc[-1])
    except Exception:
        pass
    return None


def get_price_range_between(ticker, start_date, end_date):
    """Get high and low price between two dates. Returns (high, low) or (None, None)."""
    data = _get_history_range(ticker, start_date, end_date)
    if data is None:
        return None, None
    try:
        return float(data['High'].max()), float(data['Low'].min())
    except Exception:
        return None, None


def get_first_date_price_reached(ticker, start_date, end_date, target_price, direction='above'):
    """Find first date price reached within threshold of target.
    direction='above' means price >= target * 0.90 (for FV above current price).
    Returns date or None."""
    data = _get_history_range(ticker, start_date, end_date)
    if data is None:
        return None
    try:
        threshold = target_price * 0.90 if direction == 'above' else target_price * 1.10
        for idx in data.index:
            high = float(data.loc[idx, 'High'])
            if direction == 'above' and high >= threshold:
                return idx.date() if hasattr(idx, 'date') else idx
            elif direction == 'below' and float(data.loc[idx, 'Low']) <= threshold:
                return idx.date() if hasattr(idx, 'date') else idx
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# Bulk price prefetch
# ---------------------------------------------------------------------------

def prefetch_all_prices(tickers, earliest_date, today=None):
    """Pre-download full history for all tickers to reduce API calls."""
    if today is None:
        today = date.today()
    for ticker in set(tickers):
        start = earliest_date - timedelta(days=5)
        end = today + timedelta(days=1)
        _get_history_range(ticker, start, end)


# ---------------------------------------------------------------------------
# FV record collection from thesis files
# ---------------------------------------------------------------------------

def collect_thesis_fv_records(ticker_filter=None, active_only=False):
    """Scan thesis directories and collect FV records.
    Returns list of dicts."""
    records = []
    dirs_to_scan = THESIS_DIRS
    if active_only:
        dirs_to_scan = [os.path.join(BASE_DIR, 'thesis', 'active')]

    for thesis_dir in dirs_to_scan:
        if not os.path.isdir(thesis_dir):
            continue
        for ticker_dir in sorted(os.listdir(thesis_dir)):
            if ticker_filter and ticker_dir != ticker_filter:
                continue
            thesis_path = os.path.join(thesis_dir, ticker_dir, 'thesis.md')
            if not os.path.isfile(thesis_path):
                continue

            try:
                with open(thesis_path, 'r') as f:
                    content = f.read()
            except Exception:
                continue

            default_currency = infer_currency(ticker_dir)
            fv, fv_currency = extract_fair_value(content, ticker_dir, default_currency)
            if fv is None:
                continue

            thesis_date = extract_thesis_date(content)
            if thesis_date is None:
                # Fallback: use git first commit date
                rel_path = os.path.relpath(thesis_path, BASE_DIR)
                thesis_date = get_git_first_commit_date(rel_path)
            if thesis_date is None:
                continue

            qs, tier = extract_quality_score(content)
            stage = extract_pipeline_stage(content)
            source = os.path.basename(thesis_dir)

            records.append({
                'ticker': ticker_dir,
                'fv': fv,
                'currency': fv_currency,
                'date_set': thesis_date,
                'qs': qs,
                'tier': tier,
                'pipeline_stage': stage,
                'source': source,
            })

    return records


# ---------------------------------------------------------------------------
# Closed positions from history.yaml
# ---------------------------------------------------------------------------

def collect_closed_position_records(ticker_filter=None):
    """Read closed positions from history.yaml for FV accuracy.
    Returns list of dicts with FV at entry, exit price, etc."""
    if not os.path.isfile(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, 'r') as f:
            data = yaml.safe_load(f)
    except Exception:
        return []

    closed = data.get('closed_positions', [])
    if not closed:
        return []

    records = []
    for pos in closed:
        ticker = pos.get('ticker')
        if ticker_filter and ticker != ticker_filter:
            continue

        fv_at_entry = pos.get('thesis_fv_at_entry')
        if fv_at_entry is None:
            continue

        entry_date_str = pos.get('entry_date')
        exit_date_str = pos.get('exit_date')
        if not entry_date_str or not exit_date_str:
            continue

        try:
            entry_date = datetime.strptime(str(entry_date_str), '%Y-%m-%d').date()
            exit_date = datetime.strptime(str(exit_date_str), '%Y-%m-%d').date()
        except ValueError:
            continue

        # Determine exit price and currency
        exit_price = None
        entry_currency = pos.get('entry_currency', 'USD')
        for key in ['exit_price_usd', 'exit_price_eur', 'exit_price_gbp', 'exit_price']:
            if key in pos and pos[key] is not None:
                exit_price = float(pos[key])
                if 'gbp' in key or 'gbx' in key:
                    entry_currency = 'GBp'
                elif 'eur' in key:
                    entry_currency = 'EUR'
                elif 'usd' in key:
                    entry_currency = 'USD'
                break

        if exit_price is None:
            continue

        # Entry price
        entry_price = None
        for key in ['entry_price_usd', 'entry_price_eur', 'entry_price_gbp', 'entry_price']:
            if key in pos and pos[key] is not None:
                entry_price = float(pos[key])
                break

        qs = pos.get('quality_score')
        tier = None
        if qs is not None:
            if qs >= 75:
                tier = 'A'
            elif qs >= 55:
                tier = 'B'
            elif qs >= 35:
                tier = 'C'
            else:
                tier = 'D'

        # FV revisions (adversarial, v2, v3)
        fv_adversarial = pos.get('thesis_fv_adversarial')
        fv_final = None
        for key in ['thesis_fv_v3', 'thesis_fv_v2', 'thesis_fv_risk_adjusted', 'thesis_fv_adversarial']:
            if key in pos and pos[key] is not None:
                fv_final = float(pos[key])
                break

        records.append({
            'ticker': ticker,
            'name': pos.get('name', ticker),
            'fv_at_entry': float(fv_at_entry),
            'fv_final': fv_final if fv_final else float(fv_at_entry),
            'fv_adversarial': float(fv_adversarial) if fv_adversarial else None,
            'entry_price': entry_price,
            'exit_price': exit_price,
            'entry_date': entry_date,
            'exit_date': exit_date,
            'currency': entry_currency,
            'holding_days': pos.get('holding_days'),
            'pnl_percent': pos.get('pnl_percent'),
            'qs': qs,
            'tier': tier,
            'exit_reason': pos.get('exit_reason', 'unknown'),
            'thesis_correct': pos.get('thesis_accuracy', {}).get('correct') if isinstance(pos.get('thesis_accuracy'), dict) else None,
        })

    return records


# ---------------------------------------------------------------------------
# Accuracy computation for active/thesis FV records
# ---------------------------------------------------------------------------

def compute_accuracy(records, today=None):
    """For each FV record, compute accuracy metrics."""
    if today is None:
        today = date.today()

    # Prefetch prices
    tickers = [r['ticker'] for r in records]
    earliest = min(r['date_set'] for r in records) if records else today
    prefetch_all_prices(tickers, earliest, today)

    results = []
    for rec in records:
        ticker = rec['ticker']
        fv = rec['fv']
        date_set = rec['date_set']

        price_at_set, _ = get_price_at_date(ticker, date_set)
        if price_at_set is None or price_at_set <= 0:
            continue

        mos_at_set = (fv - price_at_set) / price_at_set * 100
        fv_above = fv > price_at_set

        entry = dict(rec)
        entry['price_at_set'] = price_at_set
        entry['mos_at_set'] = mos_at_set
        entry['days_since'] = (today - date_set).days

        # Check intervals: 90d, 180d, 365d
        for days in [90, 180, 365]:
            check_date = date_set + timedelta(days=days)
            if check_date > today:
                entry[f'price_{days}d'] = None
                entry[f'convergence_{days}d'] = None
                entry[f'directional_{days}d'] = None
                continue

            price_check, _ = get_price_at_date(ticker, check_date)
            entry[f'price_{days}d'] = price_check

            if price_check is not None:
                gap_initial = fv - price_at_set
                gap_at_check = fv - price_check
                if abs(gap_initial) > 0.01:
                    convergence = (1 - gap_at_check / gap_initial) * 100
                    entry[f'convergence_{days}d'] = convergence
                    entry[f'directional_{days}d'] = abs(gap_at_check) < abs(gap_initial)
                else:
                    entry[f'convergence_{days}d'] = 0
                    entry[f'directional_{days}d'] = None
            else:
                entry[f'convergence_{days}d'] = None
                entry[f'directional_{days}d'] = None

        # Current price
        current_price = get_current_price(ticker)
        entry['price_current'] = current_price
        if current_price and price_at_set > 0:
            gap_initial = fv - price_at_set
            gap_current = fv - current_price
            if abs(gap_initial) > 0.01:
                entry['convergence_current'] = (1 - gap_current / gap_initial) * 100
                entry['directional_current'] = abs(gap_current) < abs(gap_initial)
            else:
                entry['convergence_current'] = 0
                entry['directional_current'] = None

            # MAE: |FV - current| / FV
            entry['mae'] = abs(fv - current_price) / fv * 100
        else:
            entry['convergence_current'] = None
            entry['directional_current'] = None
            entry['mae'] = None

        # Hit rate: did price ever reach within 10% of FV within 12 months?
        end_check = min(today, date_set + timedelta(days=365))
        high, low = get_price_range_between(ticker, date_set, end_check)

        if high is not None and fv > 0:
            if fv_above:
                entry['hit_fv'] = high >= fv * 0.90
                entry['closest_to_fv_pct'] = max(0, (fv - high) / fv * 100) if high < fv else 0
            else:
                # FV below price — check if price dropped to FV
                entry['hit_fv'] = low <= fv * 1.10 if low else False
                entry['closest_to_fv_pct'] = None
        else:
            entry['hit_fv'] = None
            entry['closest_to_fv_pct'] = None

        # Overshoot: price went past FV
        if high is not None and fv_above and high > fv:
            entry['overshoot'] = True
            entry['overshoot_pct'] = (high - fv) / fv * 100
        else:
            entry['overshoot'] = False
            entry['overshoot_pct'] = 0

        # Time to convergence: first date price hit within 10% of FV
        if fv_above:
            hit_date = get_first_date_price_reached(ticker, date_set, end_check, fv, 'above')
        else:
            hit_date = get_first_date_price_reached(ticker, date_set, end_check, fv, 'below')
        if hit_date:
            entry['days_to_hit'] = (hit_date - date_set).days
        else:
            entry['days_to_hit'] = None

        # Get FV revisions from git
        entry['revisions'] = get_fv_revisions_from_git(ticker)

        results.append(entry)

    return results


# ---------------------------------------------------------------------------
# Aggregate metrics
# ---------------------------------------------------------------------------

def compute_aggregates(results):
    """Compute aggregate accuracy metrics from results."""
    agg = {}
    n = len(results)
    agg['total'] = n

    if n == 0:
        return agg

    ages = [r['days_since'] for r in results]
    agg['avg_age_days'] = sum(ages) / len(ages)

    # Directional accuracy at intervals
    for days in [90, 180, 365]:
        key = f'directional_{days}d'
        valid = [r for r in results if r.get(key) is not None]
        if valid:
            correct = sum(1 for r in valid if r[key])
            agg[f'directional_{days}d'] = (correct, len(valid))
        else:
            agg[f'directional_{days}d'] = None

    valid = [r for r in results if r.get('directional_current') is not None]
    if valid:
        correct = sum(1 for r in valid if r['directional_current'])
        agg['directional_current'] = (correct, len(valid))

    # Convergence at intervals
    for days in [90, 180, 365]:
        key = f'convergence_{days}d'
        valid = [r[key] for r in results if r.get(key) is not None]
        if valid:
            agg[f'convergence_{days}d'] = sum(valid) / len(valid)
        else:
            agg[f'convergence_{days}d'] = None

    valid = [r['convergence_current'] for r in results if r.get('convergence_current') is not None]
    if valid:
        agg['convergence_current'] = sum(valid) / len(valid)

    # Convergence rate: % where >=50% of gap closed (current)
    conv_valid = [r for r in results if r.get('convergence_current') is not None]
    if conv_valid:
        converged = sum(1 for r in conv_valid if r['convergence_current'] >= 50)
        agg['convergence_rate'] = (converged, len(conv_valid))

    # Bias analysis
    bias_vals = []
    for r in results:
        if r.get('price_current') and r['price_current'] > 0:
            bias = (r['fv'] - r['price_current']) / r['price_current'] * 100
            bias_vals.append(bias)
    if bias_vals:
        agg['bias_mean'] = sum(bias_vals) / len(bias_vals)
        agg['bias_median'] = sorted(bias_vals)[len(bias_vals) // 2]
        agg['fv_too_high'] = sum(1 for b in bias_vals if b > 0)
        agg['fv_too_low'] = sum(1 for b in bias_vals if b < 0)
        agg['bias_direction'] = 'BULLISH' if agg['bias_mean'] > 0 else 'BEARISH'
    else:
        agg['bias_mean'] = None
        agg['bias_direction'] = None

    # MoS at set
    mos_vals = [r['mos_at_set'] for r in results]
    agg['avg_mos_at_set'] = sum(mos_vals) / len(mos_vals)

    # Hit rate
    hit_valid = [r for r in results if r.get('hit_fv') is not None]
    if hit_valid:
        hits = sum(1 for r in hit_valid if r['hit_fv'])
        agg['hit_rate'] = (hits, len(hit_valid))

    # Overshoot rate
    os_valid = [r for r in results if r.get('overshoot') is not None]
    if os_valid:
        overshoots = sum(1 for r in os_valid if r['overshoot'])
        agg['overshoot_rate'] = (overshoots, len(os_valid))

    # MAE
    mae_vals = [r['mae'] for r in results if r.get('mae') is not None]
    if mae_vals:
        agg['mae_mean'] = sum(mae_vals) / len(mae_vals)
        agg['mae_median'] = sorted(mae_vals)[len(mae_vals) // 2]

    # Time to convergence
    ttc = [r['days_to_hit'] for r in results if r.get('days_to_hit') is not None]
    if ttc:
        agg['ttc_median'] = sorted(ttc)[len(ttc) // 2]
        agg['ttc_mean'] = sum(ttc) / len(ttc)
        agg['ttc_count'] = len(ttc)

    # By tier
    tier_groups = defaultdict(list)
    for r in results:
        t = r.get('tier', '?')
        if t:
            tier_groups[t].append(r)
    agg['by_tier'] = {}
    for tier_name, tier_results in sorted(tier_groups.items()):
        tier_agg = {}
        tier_agg['count'] = len(tier_results)

        # Convergence rate
        cv = [r for r in tier_results if r.get('convergence_current') is not None]
        if cv:
            converged = sum(1 for r in cv if r['convergence_current'] >= 50)
            tier_agg['convergence_rate'] = f'{converged}/{len(cv)}'

        # Bias
        tb = []
        for r in tier_results:
            if r.get('price_current') and r['price_current'] > 0:
                tb.append((r['fv'] - r['price_current']) / r['price_current'] * 100)
        if tb:
            tier_agg['avg_premium'] = sum(tb) / len(tb)

        # Hit rate
        th = [r for r in tier_results if r.get('hit_fv') is not None]
        if th:
            hits = sum(1 for r in th if r['hit_fv'])
            tier_agg['hit_rate'] = f'{hits}/{len(th)}'

        agg['by_tier'][tier_name] = tier_agg

    return agg


# ---------------------------------------------------------------------------
# Closed positions aggregates
# ---------------------------------------------------------------------------

def compute_closed_aggregates(closed_records):
    """Compute accuracy metrics for closed positions."""
    agg = {}
    n = len(closed_records)
    agg['total'] = n
    if n == 0:
        return agg

    # FV accuracy at exit
    with_fv = [r for r in closed_records if r['fv_at_entry'] is not None and r['exit_price'] is not None]
    if with_fv:
        # How many exited at or above original FV?
        above_fv = sum(1 for r in with_fv if r['exit_price'] >= r['fv_at_entry'] * 0.90)
        agg['exited_near_fv'] = (above_fv, len(with_fv))

        # Average exit vs original FV
        exit_vs_fv = [(r['exit_price'] - r['fv_at_entry']) / r['fv_at_entry'] * 100 for r in with_fv]
        agg['avg_exit_vs_fv'] = sum(exit_vs_fv) / len(exit_vs_fv)

        # FV inflation: how much was original FV above entry price?
        fv_premiums = []
        for r in with_fv:
            if r['entry_price'] and r['entry_price'] > 0:
                premium = (r['fv_at_entry'] - r['entry_price']) / r['entry_price'] * 100
                fv_premiums.append(premium)
        if fv_premiums:
            agg['avg_fv_premium_at_entry'] = sum(fv_premiums) / len(fv_premiums)

        # FV revision impact (original vs final)
        revised = [r for r in with_fv if r['fv_final'] != r['fv_at_entry']]
        if revised:
            avg_revision = sum((r['fv_final'] - r['fv_at_entry']) / r['fv_at_entry'] * 100 for r in revised)
            agg['avg_fv_revision'] = avg_revision / len(revised)
            agg['revised_count'] = len(revised)

    # Thesis accuracy
    correct_known = [r for r in closed_records if r.get('thesis_correct') is not None]
    if correct_known:
        correct = sum(1 for r in correct_known if r['thesis_correct'])
        agg['thesis_correct_rate'] = (correct, len(correct_known))

    # By tier
    tier_groups = defaultdict(list)
    for r in closed_records:
        t = r.get('tier', '?')
        if t:
            tier_groups[t].append(r)
    agg['by_tier'] = {}
    for tier_name, tier_recs in sorted(tier_groups.items()):
        tr = {}
        tr['count'] = len(tier_recs)
        pnls = [r['pnl_percent'] for r in tier_recs if r.get('pnl_percent') is not None]
        if pnls:
            tr['avg_pnl'] = sum(pnls) / len(pnls)
            tr['winners'] = sum(1 for p in pnls if p > 0)
        fv_prems = []
        for r in tier_recs:
            if r['entry_price'] and r['entry_price'] > 0:
                fv_prems.append((r['fv_at_entry'] - r['entry_price']) / r['entry_price'] * 100)
        if fv_prems:
            tr['avg_fv_premium'] = sum(fv_prems) / len(fv_prems)
        agg['by_tier'][tier_name] = tr

    return agg


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def fmt_pct(val, width=7):
    if val is None:
        return 'N/A'.rjust(width)
    return f'{val:+.1f}%'.rjust(width)


def fmt_ratio(tup):
    if tup is None:
        return 'N/A'
    correct, total = tup
    pct = correct / total * 100 if total > 0 else 0
    return f'{correct}/{total} ({pct:.0f}%)'


def print_summary(results, agg, closed_records, closed_agg):
    """Print summary report."""
    today = date.today()
    w = 72
    print()
    print('=' * w)
    print(f'FV ACCURACY REPORT -- {today}')
    print('=' * w)
    print(f'FV estimates tracked: {agg["total"]}')
    if agg['total'] == 0:
        print('No FV records found.')
        return
    print(f'Avg days since FV set: {agg["avg_age_days"]:.0f}')
    print(f'Avg MoS at FV set date: {agg["avg_mos_at_set"]:.1f}%')

    print(f'\nCONVERGENCE (did price move toward FV?):')
    conv_rate = agg.get('convergence_rate')
    if conv_rate:
        c, t = conv_rate
        print(f'  Moved toward FV (>=50% gap closed): {fmt_ratio(conv_rate)}')
    hit = agg.get('hit_rate')
    if hit:
        print(f'  Hit FV (within 10%):                {fmt_ratio(hit)}')
    # Moved away
    if conv_rate:
        away = t - c
        print(f'  Moved AWAY from FV:                 {away}/{t} ({away/t*100:.0f}%)')

    print(f'\nBIAS ANALYSIS:')
    if agg.get('bias_mean') is not None:
        print(f'  FVs too HIGH (optimistic):  {agg["fv_too_high"]}/{len(results)} ({agg["fv_too_high"]/len(results)*100:.0f}%)')
        print(f'  FVs too LOW (conservative): {agg["fv_too_low"]}/{len(results)} ({agg["fv_too_low"]/len(results)*100:.0f}%)')
        print(f'  Avg FV premium over price at set: {agg["avg_mos_at_set"]:+.1f}%')
        print(f'  Avg FV premium over current price: {agg["bias_mean"]:+.1f}%', end='')
        if agg['bias_mean'] > agg['avg_mos_at_set']:
            print('  <- gap WIDENING = overestimation')
        elif agg['bias_mean'] < agg['avg_mos_at_set']:
            print('  <- gap NARROWING = convergence')
        else:
            print()

    if agg.get('mae_mean') is not None:
        print(f'\nACCURACY:')
        print(f'  Mean Absolute Error (|FV-Price|/FV): {agg["mae_mean"]:.1f}%')
        print(f'  Median Absolute Error:               {agg["mae_median"]:.1f}%')

    if agg.get('ttc_count'):
        print(f'\nTIME TO CONVERGENCE (for FVs that were reached):')
        print(f'  Median days: {agg["ttc_median"]:.0f}')
        print(f'  Mean days: {agg["ttc_mean"]:.0f}')
        print(f'  Reached count: {agg["ttc_count"]}/{agg["total"]}')

    if agg.get('by_tier'):
        print(f'\nACCURACY BY TIER:')
        for tier_name, ta in sorted(agg['by_tier'].items()):
            parts = [f'{ta["count"]} estimates']
            if 'convergence_rate' in ta:
                parts.append(f'conv {ta["convergence_rate"]}')
            if 'avg_premium' in ta:
                parts.append(f'avg premium {ta["avg_premium"]:+.1f}%')
            if 'hit_rate' in ta:
                parts.append(f'hit {ta["hit_rate"]}')
            qs_range = {'A': '>=75', 'B': '55-74', 'C': '35-54', 'D': '<35'}.get(tier_name, '?')
            print(f'  Tier {tier_name} (QS {qs_range}): {", ".join(parts)}')

    # Closed positions section
    if closed_agg.get('total', 0) > 0:
        print(f'\nCLOSED POSITIONS ({closed_agg["total"]}):')
        if closed_agg.get('exited_near_fv'):
            print(f'  Exited near/above FV (within 10%): {fmt_ratio(closed_agg["exited_near_fv"])}')
        if closed_agg.get('avg_exit_vs_fv') is not None:
            print(f'  Avg exit vs original FV: {closed_agg["avg_exit_vs_fv"]:+.1f}% (sold {"below" if closed_agg["avg_exit_vs_fv"] < 0 else "above"} FV on average)')
        if closed_agg.get('avg_fv_premium_at_entry') is not None:
            print(f'  Avg FV premium at entry: +{closed_agg["avg_fv_premium_at_entry"]:.1f}%')
        if closed_agg.get('avg_fv_revision') is not None:
            print(f'  Avg FV revision (post-DA): {closed_agg["avg_fv_revision"]:+.1f}% ({closed_agg["revised_count"]} revised)')
        if closed_agg.get('thesis_correct_rate'):
            print(f'  Thesis correct rate: {fmt_ratio(closed_agg["thesis_correct_rate"])}')
        if closed_agg.get('by_tier'):
            print(f'  By tier:')
            for tn, tr in sorted(closed_agg['by_tier'].items()):
                parts = [f'{tr["count"]} positions']
                if 'avg_pnl' in tr:
                    parts.append(f'avg P&L {tr["avg_pnl"]:+.1f}%')
                if 'avg_fv_premium' in tr:
                    parts.append(f'avg FV premium +{tr["avg_fv_premium"]:.0f}%')
                if 'winners' in tr:
                    parts.append(f'{tr["winners"]} winners')
                print(f'    Tier {tn}: {", ".join(parts)}')

    # Best/Worst
    scored = [r for r in results if r.get('convergence_current') is not None]
    if scored:
        sorted_by_conv = sorted(scored, key=lambda x: x['convergence_current'])
        print(f'\nWORST MISSES (lowest convergence):')
        for r in sorted_by_conv[:3]:
            print(f'  {r["ticker"]:<10} FV {r["currency"]} {r["fv"]:.0f}, set {r["date_set"]}, '
                  f'conv {r["convergence_current"]:+.0f}%')
        print(f'\nBEST CALLS (highest convergence):')
        for r in sorted_by_conv[-3:]:
            print(f'  {r["ticker"]:<10} FV {r["currency"]} {r["fv"]:.0f}, set {r["date_set"]}, '
                  f'conv {r["convergence_current"]:+.0f}%')


def print_detail(results, agg, closed_records):
    """Print per-ticker detail table."""
    print_summary(results, agg, closed_records, compute_closed_aggregates(closed_records))

    if not results:
        return

    print(f'\n{"="*110}')
    print(f'PER-TICKER DETAIL')
    print(f'{"="*110}')

    header = (f'{"Ticker":<10} {"FV":>8} {"Ccy":<4} {"Set Date":<11} '
              f'{"P@Set":>8} {"MoS%":>7} {"P@Now":>8} '
              f'{"Conv%":>7} {"MAE%":>7} {"Hit?":>5} {"Tier":<3} {"Revs":>4} {"Stage":<12}')
    print(header)
    print('-' * 110)

    for r in sorted(results, key=lambda x: x['ticker']):
        fv_str = f'{r["fv"]:.0f}'
        p_set = f'{r["price_at_set"]:.2f}'
        mos = f'{r["mos_at_set"]:+.1f}'
        p_now = f'{r["price_current"]:.2f}' if r.get('price_current') else 'N/A'
        conv = f'{r["convergence_current"]:+.1f}' if r.get('convergence_current') is not None else 'N/A'
        mae = f'{r["mae"]:.1f}' if r.get('mae') is not None else 'N/A'
        hit = 'YES' if r.get('hit_fv') else ('NO' if r.get('hit_fv') is False else '?')
        tier = r.get('tier', '?')
        revs = str(len(r.get('revisions', [])))
        stage = r.get('pipeline_stage', '?')[:12]

        print(f'{r["ticker"]:<10} {fv_str:>8} {r["currency"]:<4} {str(r["date_set"]):<11} '
              f'{p_set:>8} {mos:>7} {p_now:>8} '
              f'{conv:>7} {mae:>7} {hit:>5} {tier:<3} {revs:>4} {stage:<12}')

    # Closed positions table
    if closed_records:
        print(f'\n{"="*110}')
        print(f'CLOSED POSITIONS -- FV vs EXIT')
        print(f'{"="*110}')
        header = (f'{"Ticker":<10} {"FV@Entry":>9} {"FV Final":>9} {"Entry":>8} {"Exit":>8} '
                  f'{"Exit/FV%":>8} {"P&L%":>7} {"Days":>5} {"Tier":<3} {"Correct?":>8}')
        print(header)
        print('-' * 110)

        for r in sorted(closed_records, key=lambda x: x['ticker']):
            fv_e = f'{r["fv_at_entry"]:.0f}'
            fv_f = f'{r["fv_final"]:.0f}'
            entry = f'{r["entry_price"]:.2f}' if r.get('entry_price') else 'N/A'
            exit_p = f'{r["exit_price"]:.2f}'
            exit_vs_fv = (r['exit_price'] - r['fv_at_entry']) / r['fv_at_entry'] * 100
            pnl = f'{r["pnl_percent"]:+.1f}' if r.get('pnl_percent') is not None else 'N/A'
            days = str(r.get('holding_days', '?'))
            tier = r.get('tier', '?')
            correct = 'YES' if r.get('thesis_correct') is True else ('NO' if r.get('thesis_correct') is False else '?')

            print(f'{r["ticker"]:<10} {fv_e:>9} {fv_f:>9} {entry:>8} {exit_p:>8} '
                  f'{exit_vs_fv:>+7.1f}% {pnl:>7} {days:>5} {tier:<3} {correct:>8}')


def print_ticker_deep_dive(results, closed_records, ticker):
    """Print detailed analysis for a single ticker."""
    ticker_results = [r for r in results if r['ticker'] == ticker]
    ticker_closed = [r for r in closed_records if r['ticker'] == ticker]

    if not ticker_results and not ticker_closed:
        print(f'No FV records found for {ticker}.')
        return

    print(f'\n{"="*65}')
    print(f'FV ACCURACY DEEP DIVE: {ticker}')
    print(f'{"="*65}')

    if ticker_results:
        r = ticker_results[0]

        print(f'\nCURRENT FV ESTIMATE:')
        print(f'  Fair Value: {r["currency"]} {r["fv"]:.2f}')
        print(f'  Date Set: {r["date_set"]}')
        print(f'  QS: {r.get("qs", "?")} (Tier {r.get("tier", "?")})')
        print(f'  Pipeline Stage: {r.get("pipeline_stage", "?")}')
        print(f'  Source: {r.get("source", "?")}')

        print(f'\nPRICE AT FV SET DATE:')
        print(f'  Price: {r["price_at_set"]:.2f}')
        print(f'  MoS at set: {r["mos_at_set"]:+.1f}%')

        print(f'\nPRICE EVOLUTION:')
        for days in [90, 180, 365]:
            p = r.get(f'price_{days}d')
            if p is not None:
                c = r.get(f'convergence_{days}d', 0)
                d = r.get(f'directional_{days}d')
                change = (p - r['price_at_set']) / r['price_at_set'] * 100
                print(f'  {days}d ({r["date_set"] + timedelta(days=days)}): '
                      f'{p:.2f} ({change:+.1f}%) | '
                      f'conv: {c:+.1f}% | '
                      f'dir: {"CORRECT" if d else "WRONG" if d is False else "?"}')
            else:
                target = r['date_set'] + timedelta(days=days)
                if target > date.today():
                    print(f'  {days}d ({target}): Not yet available')

        if r.get('price_current') is not None:
            p = r['price_current']
            change = (p - r['price_at_set']) / r['price_at_set'] * 100
            gap_to_fv = (r['fv'] - p) / p * 100
            print(f'\n  Current: {p:.2f} ({change:+.1f}% from set)')
            print(f'  Gap to FV: {gap_to_fv:+.1f}%')
            if r.get('convergence_current') is not None:
                print(f'  Convergence: {r["convergence_current"]:+.1f}%')
            if r.get('mae') is not None:
                print(f'  MAE: {r["mae"]:.1f}%')

        print(f'\nFV ACCURACY:')
        if r.get('hit_fv') is not None:
            print(f'  Hit FV (within 10%): {"YES" if r["hit_fv"] else "NO"}')
        if r.get('closest_to_fv_pct') is not None and r['closest_to_fv_pct'] > 0:
            print(f'  Closest approach: {r["closest_to_fv_pct"]:.1f}% away')
        if r.get('days_to_hit') is not None:
            print(f'  Days to hit FV: {r["days_to_hit"]}')
        if r.get('overshoot'):
            print(f'  Overshoot: YES (+{r["overshoot_pct"]:.1f}% past FV)')

        # FV revision history
        revisions = r.get('revisions', [])
        if revisions:
            print(f'\nFV REVISION HISTORY (from git):')
            for rev in revisions:
                print(f'  {rev["date"]}  {rev["currency"]} {rev["fv"]:.0f}  [{rev["commit"]}]  {rev["fv_text"]}')
        else:
            print(f'\nFV REVISION HISTORY: No revisions found in git')

    # Closed position data
    if ticker_closed:
        for cr in ticker_closed:
            print(f'\nCLOSED POSITION:')
            print(f'  Entry: {cr["entry_date"]} at {cr["entry_price"]:.2f}')
            print(f'  Exit: {cr["exit_date"]} at {cr["exit_price"]:.2f}')
            print(f'  FV at entry: {cr["fv_at_entry"]:.0f}')
            print(f'  FV final (post-DA): {cr["fv_final"]:.0f}')
            if cr.get('fv_adversarial'):
                print(f'  FV adversarial: {cr["fv_adversarial"]:.0f}')
            exit_vs_fv = (cr['exit_price'] - cr['fv_at_entry']) / cr['fv_at_entry'] * 100
            print(f'  Exit vs original FV: {exit_vs_fv:+.1f}%')
            print(f'  P&L: {cr.get("pnl_percent", "?")}%')
            print(f'  Holding days: {cr.get("holding_days", "?")}')
            print(f'  Thesis correct: {cr.get("thesis_correct", "?")}')
            print(f'  Exit reason: {cr.get("exit_reason", "?")}')


def print_bias_report(results, agg, closed_records, closed_agg):
    """Print focused bias analysis."""
    today = date.today()
    w = 65
    print(f'\nSYSTEMATIC BIAS ANALYSIS -- {today}')
    print('=' * w)

    if not results:
        print('No data.')
        return

    print(f'Positions analyzed: {agg["total"]}')

    print(f'\nPER-TICKER BIAS (FV vs Current Price):')
    print(f'{"Ticker":<10} {"FV":>8} {"Ccy":<4} {"Current":>8} {"Bias%":>8} {"Dir":<8} {"Tier":<3}')
    print('-' * w)

    biases = []
    for r in sorted(results, key=lambda x: x['ticker']):
        if r.get('price_current') and r['price_current'] > 0:
            bias = (r['fv'] - r['price_current']) / r['price_current'] * 100
            biases.append(bias)
            direction = 'BULLISH' if bias > 0 else 'BEARISH'
            tier = r.get('tier') or '?'
            print(f'{r["ticker"]:<10} {r["fv"]:>8.0f} {r["currency"]:<4} '
                  f'{r["price_current"]:>8.2f} {bias:>+7.1f}% {direction:<8} {tier:<3}')

    if biases:
        print(f'\n{"AGGREGATE":=^{w}}')
        mean_bias = sum(biases) / len(biases)
        median_bias = sorted(biases)[len(biases) // 2]
        bullish = sum(1 for b in biases if b > 0)
        bearish = sum(1 for b in biases if b < 0)
        print(f'  Mean bias: {mean_bias:+.1f}%')
        print(f'  Median bias: {median_bias:+.1f}%')
        print(f'  Bullish FVs: {bullish}/{len(biases)} ({bullish/len(biases)*100:.0f}%)')
        print(f'  Bearish FVs: {bearish}/{len(biases)} ({bearish/len(biases)*100:.0f}%)')

        # By source
        by_source = defaultdict(list)
        for r in results:
            if r.get('price_current') and r['price_current'] > 0:
                b = (r['fv'] - r['price_current']) / r['price_current'] * 100
                by_source[r['source']].append(b)
        if len(by_source) > 1:
            print(f'\n  BIAS BY SOURCE:')
            for src, vals in sorted(by_source.items()):
                m = sum(vals) / len(vals)
                print(f'    {src:12s}: mean {m:+.1f}% ({len(vals)} positions)')

        # By tier
        if agg.get('by_tier'):
            print(f'\n  BIAS BY TIER:')
            for tn, ta in sorted(agg['by_tier'].items()):
                if 'avg_premium' in ta:
                    qs_range = {'A': '>=75', 'B': '55-74', 'C': '35-54'}.get(tn, '?')
                    print(f'    Tier {tn} (QS {qs_range}): avg premium {ta["avg_premium"]:+.1f}%, '
                          f'{ta["count"]} estimates')

    # Closed positions bias analysis
    if closed_records:
        print(f'\n{"CLOSED POSITIONS BIAS":=^{w}}')
        fv_inflations = []
        for cr in closed_records:
            if cr['entry_price'] and cr['entry_price'] > 0:
                inflation = (cr['fv_at_entry'] - cr['entry_price']) / cr['entry_price'] * 100
                fv_inflations.append(inflation)
                if cr.get('fv_final') != cr['fv_at_entry']:
                    revision = (cr['fv_final'] - cr['fv_at_entry']) / cr['fv_at_entry'] * 100
                else:
                    revision = 0
                print(f'  {cr["ticker"]:<10} FV@entry {cr["fv_at_entry"]:>6.0f} '
                      f'FV@final {cr["fv_final"]:>6.0f} '
                      f'rev {revision:>+6.1f}% '
                      f'P&L {cr.get("pnl_percent", 0):>+5.1f}%')

        if fv_inflations:
            avg_inf = sum(fv_inflations) / len(fv_inflations)
            print(f'\n  Avg FV premium over entry: +{avg_inf:.1f}%')
            print(f'  Positions where FV was realistic (exit >= 90% FV): '
                  f'{sum(1 for cr in closed_records if cr["exit_price"] >= cr["fv_at_entry"] * 0.90)}/{len(closed_records)}')
            revised = [cr for cr in closed_records if cr['fv_final'] != cr['fv_at_entry']]
            if revised:
                avg_rev = sum((cr['fv_final'] - cr['fv_at_entry']) / cr['fv_at_entry'] * 100 for cr in revised) / len(revised)
                print(f'  Avg FV revision (DA/re-eval): {avg_rev:+.1f}% ({len(revised)} revised)')
                print(f'  --> Systematic direction: {"downward" if avg_rev < 0 else "upward"} '
                      f'= original FVs {"too optimistic" if avg_rev < 0 else "too conservative"}')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='FV Accuracy Tracker v2.0')
    parser.add_argument('--active-only', action='store_true',
                       help='Only analyze current portfolio positions')
    parser.add_argument('--ticker', type=str, default=None,
                       help='Single ticker deep dive')
    parser.add_argument('--detail', action='store_true',
                       help='Per-ticker breakdown table')
    parser.add_argument('--bias', action='store_true',
                       help='Systematic bias analysis')
    args = parser.parse_args()

    # Collect thesis FV records
    records = collect_thesis_fv_records(
        ticker_filter=args.ticker,
        active_only=args.active_only
    )

    # Collect closed position records
    closed_records = collect_closed_position_records(ticker_filter=args.ticker)

    if not records and not closed_records:
        print('No FV records found in thesis files or history.')
        sys.exit(0)

    # Deduplicate thesis records: prefer active > archive > research
    seen = {}
    priority = {'active': 0, 'archive': 1, 'research': 2}
    for r in records:
        key = r['ticker']
        if key not in seen or priority.get(r['source'], 9) < priority.get(seen[key]['source'], 9):
            seen[key] = r
    records = list(seen.values())

    if records:
        print(f'Scanning {len(records)} thesis FV records + {len(closed_records)} closed positions...')
        results = compute_accuracy(records)
    else:
        results = []

    agg = compute_aggregates(results) if results else {'total': 0}
    closed_agg = compute_closed_aggregates(closed_records)

    if not results and not closed_records:
        print('No valid results (could not fetch prices for any thesis).')
        sys.exit(0)

    if args.ticker:
        print_ticker_deep_dive(results, closed_records, args.ticker)
    elif args.bias:
        print_bias_report(results, agg, closed_records, closed_agg)
    elif args.detail:
        print_detail(results, agg, closed_records)
    else:
        print_summary(results, agg, closed_records, closed_agg)

    print(f'\n[Raw data. Reason from principles.md]')


if __name__ == '__main__':
    main()

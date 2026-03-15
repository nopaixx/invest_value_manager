#!/usr/bin/env python3
"""
DA Calibrator - Interim Devil's Advocate accuracy check.
Loads DA corrections from da_accuracy_tracker.yaml, fetches current prices,
and computes whether the DA was right, excessive, or insufficient.

Usage:
  python3 tools/da_calibrator.py              # Standard report
  python3 tools/da_calibrator.py --detail     # Include distance-to-FV columns

Output: Raw data only. No action recommendations.
"""
import sys
import os
import re
import argparse
from datetime import datetime, date

import yaml
import yfinance as yf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'tools'))
try:
    from fx_defaults import FX_DEFAULTS
except ImportError:
    FX_DEFAULTS = {'EURUSD': 1.16, 'GBPUSD': 1.34, 'CHFUSD': 1.10}
TRACKER_FILE = os.path.join(BASE_DIR, 'learning', 'da_accuracy_tracker.yaml')

# --- Currency parsing ---

def parse_price_string(s):
    """Parse strings like '$394', '277 GBp', 'EUR 38.4', 'CHF 255' into (value, currency).
    Returns (float, str) where currency is one of: USD, GBp, GBP, EUR, CHF, DKK, SEK."""
    if not s or not isinstance(s, str):
        return None, None
    s = s.strip()
    # Try prefix currencies first: $, EUR, CHF, DKK, SEK
    m = re.match(r'^\$\s*([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'
    m = re.match(r'^(EUR|CHF|DKK|SEK)\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(2).replace(',', '')), m.group(1)
    # Suffix: "277 GBp", "200 GBp", "4300 GBp", or just "260p"
    m = re.match(r'^([0-9,]+(?:\.\d+)?)\s*(GBp|GBP|p)$', s)
    if m:
        val = float(m.group(1).replace(',', ''))
        unit = m.group(2)
        if unit in ('GBp', 'p'):
            return val, 'GBp'
        return val, 'GBP'
    return None, None


# --- FX rates ---

def get_fx_rates():
    """Fetch FX rates from yfinance with fallbacks. Returns dict of currency->multiplier_to_USD."""
    pairs = {
        'EUR': ('EURUSD=X', FX_DEFAULTS.get('EURUSD', 1.16)),
        'GBP': ('GBPUSD=X', FX_DEFAULTS.get('GBPUSD', 1.34)),
        'CHF': ('CHFUSD=X', FX_DEFAULTS.get('CHFUSD', 1.10)),
        'DKK': ('DKKUSD=X', 0.14),
        'SEK': ('SEKUSD=X', 0.095),
    }
    rates = {'USD': 1.0, 'GBp': None}  # GBp handled via GBP
    fallbacks_used = []
    for ccy, (yf_pair, fallback) in pairs.items():
        try:
            rate = yf.Ticker(yf_pair).info.get('previousClose')
            if not rate or rate <= 0:
                rate = fallback
                fallbacks_used.append(f"{ccy}/USD={fallback}")
        except Exception:
            rate = fallback
            fallbacks_used.append(f"{ccy}/USD={fallback}")
        rates[ccy] = rate
    # GBp = pence -> divide by 100 to get GBP then multiply
    rates['GBp'] = rates['GBP'] / 100.0
    if fallbacks_used:
        print(f"FX WARNING: Using static fallbacks ({', '.join(fallbacks_used)})")
    return rates


def to_comparable(value, currency, rates):
    """Convert a price to USD for comparison. Returns float or None."""
    if value is None or currency is None:
        return None
    mult = rates.get(currency)
    if mult is None:
        return None
    return value * mult


def get_current_price(ticker):
    """Fetch current price and currency from yfinance. Returns (price, currency) or (None, None)."""
    try:
        info = yf.Ticker(ticker).info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        currency = info.get('currency', None)
        if price is None:
            return None, None
        return float(price), currency
    except Exception:
        return None, None


def classify_verdict(current_usd, pre_da_usd, post_da_usd):
    """Determine interim verdict based on where current price sits relative to pre/post DA FVs."""
    if current_usd is None or pre_da_usd is None or post_da_usd is None:
        return "N/A"
    if current_usd > pre_da_usd:
        return "PRICE ABOVE BOTH"
    dist_pre = abs(current_usd - pre_da_usd)
    dist_post = abs(current_usd - post_da_usd)
    if current_usd < post_da_usd:
        return "DA INSUFFICIENT"
    # current is between post_da and pre_da (or equal)
    if dist_post <= dist_pre:
        return "DA RIGHT"
    else:
        return "DA EXCESSIVE"


def fmt_price(value, currency):
    """Format price with currency for display."""
    if value is None:
        return "N/A"
    if currency == 'USD':
        return f"${value:,.0f}" if value >= 10 else f"${value:,.1f}"
    if currency == 'GBp':
        return f"{value:,.0f}p"
    if currency == 'EUR':
        return f"EUR {value:,.1f}" if value < 100 else f"EUR {value:,.0f}"
    if currency in ('CHF', 'DKK', 'SEK'):
        return f"{currency} {value:,.0f}" if value >= 10 else f"{currency} {value:,.1f}"
    return f"{value:,.2f}"


def main():
    parser = argparse.ArgumentParser(description='DA Calibrator - Interim accuracy check')
    parser.add_argument('--detail', action='store_true', help='Show distance-to-FV columns')
    args = parser.parse_args()

    # Load tracker
    if not os.path.exists(TRACKER_FILE):
        print(f"ERROR: {TRACKER_FILE} not found")
        sys.exit(1)
    with open(TRACKER_FILE, 'r') as f:
        data = yaml.safe_load(f)

    corrections = data.get('corrections', [])
    stats = data.get('stats', {})
    if not corrections:
        print("No corrections found in tracker.")
        sys.exit(0)

    # Get FX rates
    rates = get_fx_rates()

    # Compute first correction date and days since
    dates = []
    for c in corrections:
        if c.get('date'):
            if isinstance(c['date'], date):
                dates.append(c['date'])
            else:
                try:
                    dates.append(datetime.strptime(str(c['date']), '%Y-%m-%d').date())
                except ValueError:
                    pass
    first_date = min(dates) if dates else None
    first_review = stats.get('first_review_due')
    today = date.today()
    days_since = (today - first_date).days if first_date else 0
    if first_review:
        if isinstance(first_review, date):
            review_date = first_review
        else:
            review_date = datetime.strptime(str(first_review), '%Y-%m-%d').date()
        days_to_review = (review_date - today).days
    else:
        review_date = None
        days_to_review = None

    # Process each correction
    results = []
    for c in corrections:
        ticker = c.get('ticker', '?')
        pre_val, pre_ccy = parse_price_string(str(c.get('pre_da_fv', '')))
        post_val, post_ccy = parse_price_string(str(c.get('post_da_fv', '')))
        da_val, da_ccy = parse_price_string(str(c.get('price_at_da', '')))
        correction_pct = c.get('correction_pct', 0)

        current_price, current_ccy = get_current_price(ticker)

        # Normalize current price currency to match DA currency for display
        # yfinance returns GBp for .L tickers which matches our parsing
        display_ccy = pre_ccy or 'USD'

        # Convert all to USD for comparison
        pre_usd = to_comparable(pre_val, pre_ccy, rates)
        post_usd = to_comparable(post_val, post_ccy, rates)
        da_usd = to_comparable(da_val, da_ccy, rates)
        current_usd = to_comparable(current_price, current_ccy, rates) if current_price else None

        # Price move since DA (in native currency if same, else USD)
        if current_usd and da_usd and da_usd != 0:
            move_pct = (current_usd - da_usd) / da_usd * 100
        else:
            move_pct = None

        # Distance to pre-DA and post-DA (in USD terms)
        if current_usd and pre_usd and pre_usd != 0:
            dist_pre_pct = (current_usd - pre_usd) / pre_usd * 100
        else:
            dist_pre_pct = None
        if current_usd and post_usd and post_usd != 0:
            dist_post_pct = (current_usd - post_usd) / post_usd * 100
        else:
            dist_post_pct = None

        verdict = classify_verdict(current_usd, pre_usd, post_usd)

        results.append({
            'ticker': ticker,
            'pre_da_fv': fmt_price(pre_val, pre_ccy),
            'post_da_fv': fmt_price(post_val, post_ccy),
            'correction_pct': correction_pct,
            'price_at_da': fmt_price(da_val, da_ccy),
            'current_price': fmt_price(current_price, current_ccy) if current_price else 'N/A',
            'move_pct': move_pct,
            'dist_pre_pct': dist_pre_pct,
            'dist_post_pct': dist_post_pct,
            'verdict': verdict,
        })

    # --- Output ---
    total = len(results)
    print()
    print("DA CALIBRATION REPORT -- Interim Check")
    print("=" * 60)
    print(f"Total corrections tracked: {total}")
    if first_date:
        print(f"Days since first correction: {days_since}")
    if review_date and days_to_review is not None:
        print(f"Formal review starts: {review_date} ({days_to_review} days away)")
    print()

    # Table header
    if args.detail:
        hdr = f"  {'#':>2} {'Ticker':<10} {'Pre-DA':>10} {'Post-DA':>10} {'DA%':>7} {'Price@DA':>10} {'Current':>10} {'Move%':>7} {'Dist Pre':>9} {'Dist Post':>10} {'Verdict':<18}"
        sep_len = 114
    else:
        hdr = f"  {'#':>2} {'Ticker':<10} {'Pre-DA':>10} {'Post-DA':>10} {'DA%':>7} {'Price@DA':>10} {'Current':>10} {'Move%':>7} {'Verdict':<18}"
        sep_len = 95

    print("INTERIM RESULTS (current price vs DA correction):")
    print(hdr)
    print("  " + "-" * (sep_len - 2))

    for i, r in enumerate(results, 1):
        move_str = f"{r['move_pct']:+.1f}%" if r['move_pct'] is not None else "N/A"
        da_str = f"{r['correction_pct']:+.1f}%"
        if args.detail:
            dist_pre_str = f"{r['dist_pre_pct']:+.1f}%" if r['dist_pre_pct'] is not None else "N/A"
            dist_post_str = f"{r['dist_post_pct']:+.1f}%" if r['dist_post_pct'] is not None else "N/A"
            print(f"  {i:>2} {r['ticker']:<10} {r['pre_da_fv']:>10} {r['post_da_fv']:>10} {da_str:>7} {r['price_at_da']:>10} {r['current_price']:>10} {move_str:>7} {dist_pre_str:>9} {dist_post_str:>10} {r['verdict']:<18}")
        else:
            print(f"  {i:>2} {r['ticker']:<10} {r['pre_da_fv']:>10} {r['post_da_fv']:>10} {da_str:>7} {r['price_at_da']:>10} {r['current_price']:>10} {move_str:>7} {r['verdict']:<18}")

    # Aggregates
    verdicts = [r['verdict'] for r in results]
    valid = [r for r in results if r['verdict'] != 'N/A']
    valid_count = len(valid)
    counts = {}
    for v in ['DA RIGHT', 'DA EXCESSIVE', 'DA INSUFFICIENT', 'PRICE ABOVE BOTH']:
        counts[v] = sum(1 for x in verdicts if x == v)

    moves = [r['move_pct'] for r in results if r['move_pct'] is not None]
    avg_move = sum(moves) / len(moves) if moves else 0

    avg_correction = stats.get('avg_correction_pct', 0)

    print()
    print("AGGREGATE:")
    denom = valid_count if valid_count > 0 else total
    for label, key in [('DA Right', 'DA RIGHT'), ('DA Excessive', 'DA EXCESSIVE'),
                       ('DA Insufficient', 'DA INSUFFICIENT'), ('Price Above Both', 'PRICE ABOVE BOTH')]:
        c = counts[key]
        pct = c / denom * 100 if denom else 0
        print(f"  {label + ':':<22} {c}/{denom} ({pct:.0f}%)")
    na_count = sum(1 for v in verdicts if v == 'N/A')
    if na_count:
        print(f"  {'N/A (no price):':<22} {na_count}")

    print()
    print(f"  Avg DA correction:     {avg_correction:+.1f}%")
    print(f"  Avg price move since DA: {avg_move:+.1f}%")

    # Determine signal
    if valid_count == 0:
        signal = "NO DATA"
    else:
        excessive_pct = counts['DA EXCESSIVE'] / valid_count
        above_pct = counts['PRICE ABOVE BOTH'] / valid_count
        insufficient_pct = counts['DA INSUFFICIENT'] / valid_count
        right_pct = counts['DA RIGHT'] / valid_count

        over_conservative = excessive_pct + above_pct
        under_conservative = insufficient_pct

        if over_conservative >= 0.6:
            signal = "DA OVER-CONSERVATIVE"
        elif under_conservative >= 0.6:
            signal = "DA UNDER-CONSERVATIVE"
        elif right_pct >= 0.5:
            signal = "DA CALIBRATED"
        else:
            signal = "MIXED"

    print()
    print(f"  SIGNAL: {signal}")
    if signal == "DA OVER-CONSERVATIVE":
        print("  If DA Over-Conservative: entries should be RAISED (closer to pre-DA).")
    elif signal == "DA UNDER-CONSERVATIVE":
        print("  If DA Under-Conservative: current entries are correct or need further cuts.")

    # --- Edge Analysis: Our FV vs Consensus vs Actual ---
    # Uses da_independent_fv and consensus_pt_at_da fields (if present in entries)
    edge_entries = []
    for c in corrections:
        consensus = c.get('consensus_pt_at_da')
        da_indep = c.get('da_independent_fv')
        if consensus or da_indep:
            edge_entries.append(c)

    if edge_entries:
        print()
        print("EDGE ANALYSIS (Our FV vs Consensus vs Price):")
        print(f"  {'Ticker':<10} {'Post-DA FV':>12} {'DA Bear FV':>12} {'Consensus':>12} {'Current':>12} {'Edge?':<20}")
        print("  " + "-" * 78)

        edge_wins = 0
        edge_total = 0
        for c in edge_entries:
            ticker = c.get('ticker', '?')
            post_val, post_ccy = parse_price_string(str(c.get('post_da_fv', '')))
            cons_val, cons_ccy = parse_price_string(str(c.get('consensus_pt_at_da', ''))) if c.get('consensus_pt_at_da') else (None, None)
            da_bear_val, da_bear_ccy = parse_price_string(str(c.get('da_independent_fv', ''))) if c.get('da_independent_fv') else (None, None)
            cur_price, cur_ccy = get_current_price(ticker)

            post_usd = to_comparable(post_val, post_ccy, rates) if post_val else None
            cons_usd = to_comparable(cons_val, cons_ccy, rates) if cons_val else None
            cur_usd = to_comparable(cur_price, cur_ccy, rates) if cur_price else None

            # Did our FV predict better than consensus?
            edge_label = "N/A"
            if post_usd and cons_usd and cur_usd:
                edge_total += 1
                our_error = abs(cur_usd - post_usd)
                cons_error = abs(cur_usd - cons_usd)
                if our_error < cons_error:
                    edge_label = "OUR FV CLOSER"
                    edge_wins += 1
                else:
                    edge_label = "CONSENSUS CLOSER"

            post_str = fmt_price(post_val, post_ccy) if post_val else "N/A"
            da_bear_str = fmt_price(da_bear_val, da_bear_ccy) if da_bear_val else "N/A"
            cons_str = fmt_price(cons_val, cons_ccy) if cons_val else "N/A"
            cur_str = fmt_price(cur_price, cur_ccy) if cur_price else "N/A"

            print(f"  {ticker:<10} {post_str:>12} {da_bear_str:>12} {cons_str:>12} {cur_str:>12} {edge_label:<20}")

        if edge_total > 0:
            print(f"\n  Edge win rate: {edge_wins}/{edge_total} ({edge_wins/edge_total*100:.0f}%)")
        print()
    else:
        print()
        print("EDGE ANALYSIS: No entries with consensus_pt_at_da yet. Will populate as DAs include Edge Assessment.")
        print()

    print("[Raw data. No action recommendations.]")


if __name__ == '__main__':
    main()

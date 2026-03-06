#!/usr/bin/env python3
"""
Basket Dashboard — Thematic basket aggregation and health monitoring.

Reads thematic_baskets.yaml + portfolio + thesis data to provide basket-level
metrics, health flags, rotation candidates, and rebalance signals.
Outputs RAW DATA only. No recommendations.

Usage:
  python3 tools/basket_dashboard.py                  # Full report
  python3 tools/basket_dashboard.py --metrics        # Summary table only
  python3 tools/basket_dashboard.py --rotation       # Cross-basket rotation candidates
  python3 tools/basket_dashboard.py --health         # Health flags (single-position, stale, underfunded)
  python3 tools/basket_dashboard.py --rebalance      # Allocation vs meta-portfolio targets
  python3 tools/basket_dashboard.py --lifecycle       # Lifecycle integrity flags (v4.8)
"""
import sys, os, argparse, yaml, warnings
warnings.filterwarnings('ignore')

try:
    import yfinance as yf
except ImportError:
    print("ERROR: yfinance not installed"); sys.exit(1)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'tools'))
from thesis_parser import (extract_growth_rate, read_thesis, find_thesis_path,
                           parse_portfolio_fv, compute_ecagr,
                           convert_fv_to_price_currency)

BASKETS_FILE = os.path.join(BASE, 'state', 'thematic_baskets.yaml')
PORTFOLIO_FILE = os.path.join(BASE, 'portfolio', 'current.yaml')
SYSTEM_FILE = os.path.join(BASE, 'state', 'system.yaml')
TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}


def load_yaml(path):
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR loading {path}: {e}"); return None


def get_fx_rates():
    defaults = {'EURUSD': 1.04, 'GBPEUR': 1.19, 'DKKEUR': 0.134}
    fallbacks, rates = [], {}
    for pair, key, dflt in [('EURUSD=X','EURUSD',1.04),('GBPEUR=X','GBPEUR',1.19),('DKKEUR=X','DKKEUR',0.134)]:
        try:
            v = yf.Ticker(pair).info.get('previousClose')
            if not v: raise ValueError
            rates[key] = v
        except Exception:
            rates[key] = dflt; fallbacks.append(f"{key}={dflt}")
    if fallbacks: print(f"FX WARNING: Static fallback ({', '.join(fallbacks)}).")
    return rates['EURUSD'], rates['GBPEUR'], rates['DKKEUR']


def get_yf_info(ticker):
    try:
        info = yf.Ticker(TICKER_MAP.get(ticker, ticker)).info
        return info if info and 'symbol' in info else None
    except Exception: return None


def get_price(info):
    return (info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')) if info else None


def get_div_yield_pct(info):
    if not info: return 0.0
    dy = info.get('dividendYield')
    return dy if dy and isinstance(dy, (int, float)) and dy >= 0 else 0.0


def price_to_eur(price, curr, eurusd, gbpeur, dkkeur):
    if curr == 'EUR': return price
    if curr == 'USD': return price / eurusd
    if curr in ('GBp','GBX'): return (price / 100) * gbpeur
    if curr == 'GBP': return price * gbpeur
    if curr == 'DKK': return price * dkkeur
    if curr == 'SEK': return price * 0.088
    if curr == 'CHF': return price * 1.06
    return price / eurusd


def load_system_qs():
    data = load_yaml(SYSTEM_FILE)
    if not data: return {}
    ps = data.get('system',{}).get('portfolio_quality_analysis',{}).get('positions',[])
    return {p['ticker']: (p.get('score'), p.get('tier')) for p in ps if p.get('ticker')}


def _extract_growth_from_thesis(ticker):
    thesis_path = find_thesis_path(ticker)
    content = read_thesis(thesis_path)
    return extract_growth_rate(content, ticker)


def get_growth_pct(ticker, info):
    g = _extract_growth_from_thesis(ticker)
    if g is not None: return g * 100
    if info:
        eg = info.get('earningsGrowth')
        if eg and isinstance(eg, (int,float)): return eg * 100
        rg = info.get('revenueGrowth')
        if rg and isinstance(rg, (int,float)): return rg * 100
    return 0.0


# ── Position processing ───────────────────────────────────────────────────────
def process_portfolio(portfolio, eurusd, gbpeur, dkkeur, system_qs):
    """Process all portfolio positions. Returns dict of {ticker: position_data}."""
    results = {}
    for p in portfolio.get('positions', []):
        tk = p['ticker']
        inv_eur = p.get('invested_usd', 0) / eurusd
        fv_raw, fv_curr = parse_portfolio_fv(p.get('fair_value', ''))
        qs, tier = system_qs.get(tk, (None, None))
        conv = (p.get('conviction') or 'medium')[0].upper()
        info = get_yf_info(tk)
        price = get_price(info)
        sc = info.get('currency', 'USD') if info else 'USD'
        dy = get_div_yield_pct(info)
        gp = get_growth_pct(tk, info)
        val_eur = price_to_eur(price, sc, eurusd, gbpeur, dkkeur) * p.get('shares', 0) if price else inv_eur
        fv_c, mos, ecagr = None, None, None
        if fv_raw is not None and price:
            fv_c = convert_fv_to_price_currency(fv_raw, fv_curr, sc, eurusd, gbpeur, dkkeur)
            mos = ((fv_c - price) / price) * 100
            ecagr = compute_ecagr(fv_c, price, gp, dy)
        results[tk] = {
            'ticker': tk, 'ecagr': ecagr, 'mos_pct': mos, 'value_eur': val_eur,
            'qs': qs, 'tier': tier, 'conv': conv, 'price': price, 'inv_eur': inv_eur,
        }
    return results


# ── Basket aggregation ────────────────────────────────────────────────────────
def aggregate_baskets(baskets_data, pos_data, cash_eur):
    """Aggregate position data into basket-level metrics."""
    baskets = baskets_data.get('baskets', [])
    total_portfolio = sum(p['value_eur'] for p in pos_data.values()) + cash_eur

    results = []
    assigned_tickers = set()
    for b in baskets:
        bid = b.get('id', '?')
        name = b.get('name', bid)
        status = b.get('status', '?')
        positions = b.get('positions', [])
        pipeline = b.get('pipeline', [])

        basket_positions = []
        basket_value = 0.0
        ecagr_weighted_sum = 0.0
        ecagr_weight_total = 0.0
        for tk in positions:
            assigned_tickers.add(tk)
            pd = pos_data.get(tk)
            if pd:
                basket_positions.append(pd)
                basket_value += pd['value_eur']
                if pd['ecagr'] is not None:
                    ecagr_weighted_sum += pd['ecagr'] * pd['value_eur']
                    ecagr_weight_total += pd['value_eur']

        basket_ecagr = ecagr_weighted_sum / ecagr_weight_total if ecagr_weight_total > 0 else None
        basket_pct = (basket_value / total_portfolio * 100) if total_portfolio > 0 else 0

        results.append({
            'id': bid,
            'name': name,
            'status': status,
            'positions': positions,
            'pipeline': pipeline,
            'pos_count': len(positions),
            'pipe_count': len(pipeline),
            'value_eur': basket_value,
            'pct_portfolio': basket_pct,
            'ecagr': basket_ecagr,
            'pos_data': basket_positions,
            'kill_conditions': b.get('kill_conditions', []),
            'shared_risks': b.get('shared_risks', []),
        })

    # Unassigned positions
    unassigned = [pd for tk, pd in pos_data.items() if tk not in assigned_tickers]
    if unassigned:
        uval = sum(p['value_eur'] for p in unassigned)
        uw_sum = sum(p['ecagr'] * p['value_eur'] for p in unassigned if p['ecagr'] is not None)
        uw_tot = sum(p['value_eur'] for p in unassigned if p['ecagr'] is not None)
        results.append({
            'id': 'unassigned',
            'name': 'Unassigned',
            'status': '-',
            'positions': [p['ticker'] for p in unassigned],
            'pipeline': [],
            'pos_count': len(unassigned),
            'pipe_count': 0,
            'value_eur': uval,
            'pct_portfolio': (uval / total_portfolio * 100) if total_portfolio > 0 else 0,
            'ecagr': uw_sum / uw_tot if uw_tot > 0 else None,
            'pos_data': unassigned,
            'kill_conditions': [],
            'shared_risks': [],
        })

    return results, total_portfolio


# ── Output functions ──────────────────────────────────────────────────────────
def print_metrics(basket_results, total_portfolio, cash_eur):
    cash_pct = cash_eur / total_portfolio * 100 if total_portfolio > 0 else 0
    print(f"\nTHEMATIC BASKETS DASHBOARD\n{'='*90}")
    print(f"{'Basket':<25} {'Pos':>3} {'Pipe':>4} {'EUR Val':>8} {'%Port':>6} {'E[CAGR]':>8} {'Status':<10}")
    print("-"*90)
    for b in basket_results:
        ec = f"{b['ecagr']:.1f}%" if b['ecagr'] is not None else '  N/A'
        tickers = ', '.join(b['positions'][:4])
        if len(b['positions']) > 4: tickers += '...'
        print(f"{b['name']:<25} {b['pos_count']:>3} {b['pipe_count']:>4} {b['value_eur']:>8,.0f} {b['pct_portfolio']:>5.1f}% {ec:>8} {b['status']:<10}")
        print(f"  {'':25} Positions: {tickers}")
        if b['pipeline']:
            pipe_str = ', '.join(b['pipeline'][:4])
            print(f"  {'':25} Pipeline:  {pipe_str}")
    print("-"*90)
    deployed = total_portfolio - cash_eur
    dep_pct = deployed / total_portfolio * 100 if total_portfolio > 0 else 0
    print(f"{'Cash':<25} {'':>3} {'':>4} {cash_eur:>8,.0f} {cash_pct:>5.1f}%")
    print(f"{'TOTAL':<25} {'':>3} {'':>4} {total_portfolio:>8,.0f} {'100.0':>5}%")
    print(f"\n  Deployed: {dep_pct:.1f}% | Cash: {cash_pct:.1f}%")
    print()


def print_health(basket_results, baskets_data, cash_eur, total_portfolio):
    meta = baskets_data.get('meta_portfolio', {})
    targets = meta.get('target_allocations', [])
    target_map = {t['basket_id']: t for t in targets}
    cash_pct = cash_eur / total_portfolio * 100 if total_portfolio > 0 else 0

    print(f"\nBASKET HEALTH FLAGS\n{'='*70}")
    flags = []

    for b in basket_results:
        bid = b['id']
        # Single-position basket
        if b['pos_count'] == 1 and b['status'] == 'ACTIVE' and b['pipe_count'] == 0:
            flags.append(f"  SINGLE-POS: {b['name']} has 1 position, 0 pipeline — vulnerable")
        elif b['pos_count'] == 1 and b['status'] == 'ACTIVE':
            flags.append(f"  THIN: {b['name']} has 1 position, {b['pipe_count']} pipeline — build priority")

        # Underfunded vs target
        tgt = target_map.get(bid)
        if tgt:
            lo, hi = tgt.get('range_pct', [0, 100])
            if b['pct_portfolio'] < lo:
                flags.append(f"  UNDERFUNDED: {b['name']} at {b['pct_portfolio']:.1f}% vs target [{lo}-{hi}%]")
            elif b['pct_portfolio'] > hi:
                flags.append(f"  OVERFUNDED: {b['name']} at {b['pct_portfolio']:.1f}% vs target [{lo}-{hi}%]")

        # Low E[CAGR] basket
        if b['ecagr'] is not None and b['ecagr'] < 8.0 and b['status'] == 'ACTIVE':
            flags.append(f"  LOW-ECAGR: {b['name']} basket E[CAGR] {b['ecagr']:.1f}% — rotation candidate?")

    # Cash emergency
    cash_tgt = target_map.get('cash', {})
    cash_hi = cash_tgt.get('range_pct', [5, 15])[1] if cash_tgt else 15
    if cash_pct > cash_hi:
        flags.append(f"  CASH-EMERGENCY: {cash_pct:.1f}% cash vs target max {cash_hi}% (P15)")

    # GBP concentration check
    uk_baskets = [b for b in basket_results if 'uk' in b['id'].lower()]
    uk_pct = sum(b['pct_portfolio'] for b in uk_baskets)
    if uk_pct > 30:
        flags.append(f"  GBP-CONCENTRATION: UK baskets at {uk_pct:.1f}% (>30%)")

    if flags:
        for f in flags:
            print(f)
    else:
        print("  No health flags. All baskets within parameters.")
    print()


def print_rebalance(basket_results, baskets_data, cash_eur, total_portfolio):
    meta = baskets_data.get('meta_portfolio', {})
    targets = meta.get('target_allocations', [])
    target_map = {t['basket_id']: t for t in targets}
    cash_pct = cash_eur / total_portfolio * 100 if total_portfolio > 0 else 0

    print(f"\nBASKET REBALANCE ANALYSIS\n{'='*80}")
    print(f"{'Basket':<25} {'Current%':>8} {'Target%':>8} {'Range':>12} {'Delta':>8} {'Action'}")
    print("-"*80)

    for b in basket_results:
        bid = b['id']
        tgt = target_map.get(bid)
        if not tgt: continue
        tp = tgt.get('target_pct', 0)
        lo, hi = tgt.get('range_pct', [0, 100])
        delta = b['pct_portfolio'] - tp
        if b['pct_portfolio'] < lo:
            action = 'UNDERFUNDED'
        elif b['pct_portfolio'] > hi:
            action = 'OVERFUNDED'
        else:
            action = 'OK'
        print(f"{b['name']:<25} {b['pct_portfolio']:>7.1f}% {tp:>7}% {f'[{lo}-{hi}%]':>12} {delta:>+7.1f}% {action}")

    # Cash row
    cash_tgt = target_map.get('cash', {})
    if cash_tgt:
        cp = cash_tgt.get('target_pct', 10)
        clo, chi = cash_tgt.get('range_pct', [5, 15])
        cd = cash_pct - cp
        ca = 'UNDERFUNDED' if cash_pct < clo else ('OVERFUNDED' if cash_pct > chi else 'OK')
        print(f"{'Cash':<25} {cash_pct:>7.1f}% {cp:>7}% {f'[{clo}-{chi}%]':>12} {cd:>+7.1f}% {ca}")

    print("-"*80)

    # Deployment priority
    underfunded = []
    for b in basket_results:
        tgt = target_map.get(b['id'])
        if not tgt: continue
        lo = tgt.get('range_pct', [0, 100])[0]
        if b['pct_portfolio'] < lo and b['ecagr'] is not None:
            gap_eur = (lo - b['pct_portfolio']) / 100 * total_portfolio
            underfunded.append((b, gap_eur))

    if underfunded:
        underfunded.sort(key=lambda x: -x[0]['ecagr'])
        print("\nDEPLOYMENT PRIORITY (underfunded baskets, sorted by E[CAGR]):")
        for b, gap in underfunded:
            print(f"  {b['name']}: E[CAGR] {b['ecagr']:.1f}%, needs ~EUR {gap:,.0f} to reach range minimum")
    print()


def print_lifecycle(basket_results, baskets_data):
    """Check basket lifecycle integrity per v4.8 rules."""
    from datetime import datetime, date
    today = date.today()
    baskets = baskets_data.get('baskets', [])

    print(f"\nBASKET LIFECYCLE INTEGRITY (v4.8)\n{'='*70}")
    flags = []

    for b_yaml in baskets:
        bid = b_yaml.get('id', '?')
        name = b_yaml.get('name', bid)
        status = b_yaml.get('status', '?')
        vitality = b_yaml.get('theme_vitality', '?')
        positions = b_yaml.get('positions', [])
        pipeline = b_yaml.get('pipeline', [])
        deadline_str = b_yaml.get('lifecycle_deadline')
        pos_count = len(positions)
        pipe_count = len(pipeline)

        # Parse deadline
        deadline = None
        days_to_deadline = None
        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                days_to_deadline = (deadline - today).days
            except Exception:
                pass

        # MISLABELED: status doesn't match reality
        if status == 'ACTIVE' and pos_count < 2:
            flags.append(f"  MISLABELED: {name} is '{status}' but has only {pos_count} position(s). Should be RESEARCHING or BUILDING.")
        if status == 'BUILDING' and pos_count == 0:
            flags.append(f"  MISLABELED: {name} is 'BUILDING' with 0 positions. Should be RESEARCHING or IDEA.")

        # STAGNANT: single-position for extended period without progress
        if pos_count == 1 and pipe_count == 0 and status not in ('DECLINING', 'DEAD'):
            flags.append(f"  STAGNANT: {name} has 1 position, 0 pipeline. No path to ACTIVE. Consider KILL.")

        # NO_PATH: building/researching with no pipeline candidates
        if status in ('BUILDING', 'RESEARCHING') and pipe_count == 0:
            flags.append(f"  NO_PATH: {name} is '{status}' with 0 pipeline candidates. Cannot progress without candidates.")

        # DEATH_WATCH: declining theme + single position
        if vitality == 'DECLINING' and pos_count <= 1:
            flags.append(f"  DEATH_WATCH: {name} theme DECLINING with {pos_count} position(s). Evaluate basket death.")

        # DEADLINE: approaching or missed
        if deadline and days_to_deadline is not None:
            if days_to_deadline < 0:
                flags.append(f"  DEADLINE_MISSED: {name} deadline was {deadline_str} ({abs(days_to_deadline)}d ago). ACTION REQUIRED: kill or extend with justification.")
            elif days_to_deadline <= 14:
                flags.append(f"  DEADLINE_NEAR: {name} deadline {deadline_str} ({days_to_deadline}d away). Plan deployment or prepare to kill.")

    if flags:
        for f in flags:
            print(f)
    else:
        print("  All baskets pass lifecycle integrity checks.")
    print()


def print_rotation(basket_results):
    print(f"\nCROSS-BASKET ROTATION CANDIDATES\n{'='*70}")
    active = [b for b in basket_results if b['ecagr'] is not None and b['status'] in ('ACTIVE','-')]
    if len(active) < 2:
        print("  Not enough baskets with E[CAGR] data for rotation analysis.")
        print()
        return

    active.sort(key=lambda x: x['ecagr'])
    worst = active[0]
    best = active[-1]

    if best['ecagr'] - worst['ecagr'] > 3.0:
        print(f"  WORST basket: {worst['name']} at E[CAGR] {worst['ecagr']:.1f}%")
        print(f"  BEST basket:  {best['name']} at E[CAGR] {best['ecagr']:.1f}%")
        print(f"  Gap: {best['ecagr'] - worst['ecagr']:.1f}pp — rotation candidate per P16")
    else:
        print(f"  No cross-basket rotation opportunities (max gap: {best['ecagr'] - worst['ecagr']:.1f}pp, need >3pp)")

    # Per-basket, list worst individual position
    print(f"\n  Per-basket worst position:")
    for b in basket_results:
        if not b['pos_data']: continue
        valid = [p for p in b['pos_data'] if p['ecagr'] is not None]
        if not valid: continue
        worst_pos = min(valid, key=lambda x: x['ecagr'])
        print(f"    {b['name']}: {worst_pos['ticker']} at E[CAGR] {worst_pos['ecagr']:.1f}%")
    print()


def main():
    ap = argparse.ArgumentParser(description='Basket Dashboard')
    ap.add_argument('--metrics', action='store_true', help='Summary table only')
    ap.add_argument('--rotation', action='store_true', help='Cross-basket rotation candidates')
    ap.add_argument('--health', action='store_true', help='Health flags')
    ap.add_argument('--rebalance', action='store_true', help='Allocation vs targets')
    ap.add_argument('--lifecycle', action='store_true', help='Lifecycle integrity flags (v4.8)')
    args = ap.parse_args()

    baskets_data = load_yaml(BASKETS_FILE)
    if not baskets_data:
        print("ERROR: Cannot load state/thematic_baskets.yaml"); sys.exit(1)
    portfolio = load_yaml(PORTFOLIO_FILE)
    if not portfolio:
        print("ERROR: Cannot load portfolio/current.yaml"); sys.exit(1)

    sqs = load_system_qs()
    cash_eur = portfolio.get('cash', {}).get('amount', 0)

    print("Loading FX rates and position data...")
    eurusd, gbpeur, dkkeur = get_fx_rates()
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/EUR={gbpeur:.4f} | DKK/EUR={dkkeur:.4f}")

    pos_data = process_portfolio(portfolio, eurusd, gbpeur, dkkeur, sqs)
    print(f"Processed {len(pos_data)} positions.")

    basket_results, total_portfolio = aggregate_baskets(baskets_data, pos_data, cash_eur)

    show_all = not (args.metrics or args.rotation or args.health or args.rebalance or args.lifecycle)

    if show_all or args.metrics:
        print_metrics(basket_results, total_portfolio, cash_eur)
    if show_all or args.health:
        print_health(basket_results, baskets_data, cash_eur, total_portfolio)
    if show_all or args.rebalance:
        print_rebalance(basket_results, baskets_data, cash_eur, total_portfolio)
    if show_all or args.rotation:
        print_rotation(basket_results)
    if show_all or args.lifecycle:
        print_lifecycle(basket_results, baskets_data)

    print("[Raw data. Reason from principles.md]")
    print()


if __name__ == '__main__':
    main()

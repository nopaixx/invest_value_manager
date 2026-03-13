#!/usr/bin/env python3
"""
Portfolio CAGR Projector - Makes cash drag visible, surfaces market buy / rotation candidates.

Reads portfolio, computes E[CAGR] per position, aggregates weighted portfolio E[CAGR],
quantifies cash drag, scans quality_universe for deployment candidates.
Outputs RAW DATA only. No recommendations.

Usage:
  python3 tools/portfolio_cagr.py                  # Full report
  python3 tools/portfolio_cagr.py --no-universe     # Skip universe scan (faster)
  python3 tools/portfolio_cagr.py --verbose          # Extra detail per position
  python3 tools/portfolio_cagr.py --target-cagr 25   # Override target CAGR (default 30%)
"""
import sys, os, re, argparse, yaml, yfinance as yf, warnings
warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'tools'))
from thesis_parser import (extract_growth_rate, read_thesis, find_thesis_path,
                           parse_portfolio_fv, compute_ecagr,
                           convert_fv_to_price_currency)
from fx_defaults import FX_DEFAULTS

PORTFOLIO_FILE = os.path.join(BASE, 'portfolio', 'current.yaml')
UNIVERSE_FILE = os.path.join(BASE, 'state', 'quality_universe.yaml')
SYSTEM_FILE = os.path.join(BASE, 'state', 'system.yaml')
BASKETS_FILE = os.path.join(BASE, 'state', 'thematic_baskets.yaml')
CASH_YIELD_PCT = 3.0
TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

def load_yaml(path):
    try:
        with open(path, 'r') as f: return yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR loading {path}: {e}"); return None

def get_fx_rates():
    defaults = FX_DEFAULTS
    fallbacks, rates = [], {}
    for pair, key, dflt in [('EURUSD=X','EURUSD',defaults['EURUSD']),('GBPEUR=X','GBPEUR',defaults['GBPEUR']),('DKKEUR=X','DKKEUR',defaults['DKKEUR'])]:
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
    return price / eurusd

def infer_universe_fv_currency(stated_curr, fv_val, stock_curr):
    """Fix universe currency inconsistencies: .L stocks often have GBP/USD but FV in pence."""
    if stock_curr in ('GBp','GBX') and stated_curr in ('GBP','USD','EUR') and fv_val and fv_val > 10:
        return 'GBp'
    return stated_curr

def _extract_growth_from_thesis(ticker):
    """Extract sustainable growth rate from thesis. Returns decimal or None.
    Uses canonical thesis_parser.extract_growth_rate."""
    thesis_path = find_thesis_path(ticker)
    content = read_thesis(thesis_path)
    return extract_growth_rate(content, ticker)

def get_growth_pct(ticker, info):
    """Growth in percent. Thesis first, yfinance fallback. Returns (pct, source)."""
    g = _extract_growth_from_thesis(ticker)
    if g is not None: return g * 100, 'thesis'
    if info:
        eg = info.get('earningsGrowth')
        if eg and isinstance(eg, (int,float)): return eg * 100, 'yf_earn'
        rg = info.get('revenueGrowth')
        if rg and isinstance(rg, (int,float)): return rg * 100, 'yf_rev'
    return 0.0, 'none'


def load_system_qs():
    data = load_yaml(SYSTEM_FILE)
    if not data: return {}
    ps = data.get('system',{}).get('portfolio_quality_analysis',{}).get('positions',[])
    return {p['ticker']: (p.get('score'), p.get('tier')) for p in ps if p.get('ticker')}

# ── Core processing ──────────────────────────────────────────────────────────
def process_positions(portfolio, eurusd, gbpeur, dkkeur, system_qs):
    results = []
    for p in portfolio.get('positions', []):
        tk = p['ticker']
        inv_eur = p.get('invested_usd', 0) / eurusd if 'invested_usd' in p else p.get('invested_eur', 0)
        fv_raw, fv_curr = parse_portfolio_fv(p.get('fair_value', ''))
        qs, tier = system_qs.get(tk, (None, None))
        conv = (p.get('conviction') or 'medium')[0].upper()
        info = get_yf_info(tk)
        price = get_price(info)
        sc = info.get('currency', 'USD') if info else 'USD'
        dy = get_div_yield_pct(info)
        gp, gs = get_growth_pct(tk, info)
        val_eur = price_to_eur(price, sc, eurusd, gbpeur, dkkeur) * p.get('shares', 0) if price else inv_eur
        fv_c, mos, ecagr = None, None, None
        if fv_raw is not None and price:
            fv_c = convert_fv_to_price_currency(fv_raw, fv_curr, sc, eurusd, gbpeur, dkkeur)
            mos = ((fv_c - price) / price) * 100
            ecagr = compute_ecagr(fv_c, price, gp, dy)
        results.append({'ticker': tk, 'ecagr': ecagr, 'mos_pct': mos, 'growth_pct': gp,
                         'growth_src': gs, 'div_yield': dy, 'qs': qs, 'tier': tier, 'conv': conv,
                         'value_eur': val_eur, 'price': price, 'error': None if price else 'No price'})
    return results

def scan_universe(eurusd, gbpeur, dkkeur):
    data = load_yaml(UNIVERSE_FILE)
    if not data: return []
    ok = {'SCORED','R1_COMPLETE','R3_COMPLETE','R4_APPROVED','APPROVED','STANDING_ORDER'}
    results = []
    for c in data.get('quality_universe',{}).get('companies',[]):
        if c.get('direction','long') != 'long': continue
        st = c.get('pipeline_status','')
        if st not in ok: continue
        fv = c.get('fair_value'); curr = c.get('currency','USD')
        if not fv: continue
        tk = c['ticker']
        info = get_yf_info(tk)
        price = get_price(info) or c.get('current_price')
        if not price or price <= 0: continue
        sc = info.get('currency', curr) if info else curr
        dy = get_div_yield_pct(info)
        fv_curr = infer_universe_fv_currency(curr, fv, sc)
        fv_c = convert_fv_to_price_currency(fv, fv_curr, sc, eurusd, gbpeur, dkkeur)
        ratio = fv_c / price
        if ratio > 5 or ratio < 0.2: continue  # sanity: skip currency mismatches
        ecagr = compute_ecagr(fv_c, price, 0.0, dy)  # conservative: no growth
        qs = c.get('qs_adj') or c.get('qs_tool') or 0
        tier = c.get('tier','?')
        threshold = 12.0 if tier == 'A' else 15.0
        if ecagr is None or ecagr < threshold: continue
        mos = ((fv_c - price) / price) * 100
        results.append({'ticker': tk, 'ecagr_market': ecagr, 'price': price, 'fv': fv,
                         'mos_pct': mos, 'qs': qs, 'tier': tier, 'pipeline': st, 'div_yield': dy})
    results.sort(key=lambda x: x['ecagr_market'], reverse=True)
    return results

# ── Output ───────────────────────────────────────────────────────────────────
def print_basket_breakdown(pos, baskets_data, total_portfolio):
    """Print E[CAGR] breakdown by thematic basket."""
    if not baskets_data:
        return
    baskets = baskets_data.get('baskets', [])
    if not baskets:
        return

    pos_map = {r['ticker']: r for r in pos}
    assigned = set()

    print(f"BASKET E[CAGR] BREAKDOWN\n{'-'*72}")
    print(f"  {'Basket':<25} {'Pos':>3} {'EUR Val':>8} {'%Port':>6} {'WtdE[CAGR]':>10}")
    print("  " + "-" * 56)

    for b in baskets:
        positions = b.get('positions', [])
        basket_pos = [pos_map[tk] for tk in positions if tk in pos_map]
        assigned.update(tk for tk in positions if tk in pos_map)

        bval = sum(r['value_eur'] for r in basket_pos)
        bpct = bval / total_portfolio * 100 if total_portfolio > 0 else 0
        w_sum = sum(r['ecagr'] * r['value_eur'] for r in basket_pos if r['ecagr'] is not None)
        w_tot = sum(r['value_eur'] for r in basket_pos if r['ecagr'] is not None)
        becagr = w_sum / w_tot if w_tot > 0 else None
        ec_str = f"{becagr:.1f}%" if becagr is not None else 'N/A'
        print(f"  {b.get('name', b.get('id','?')):<25} {len(basket_pos):>3} {bval:>8,.0f} {bpct:>5.1f}% {ec_str:>10}")

    # Unassigned
    upos = [r for r in pos if r['ticker'] not in assigned]
    if upos:
        uval = sum(r['value_eur'] for r in upos)
        upct = uval / total_portfolio * 100 if total_portfolio > 0 else 0
        uw = sum(r['ecagr'] * r['value_eur'] for r in upos if r['ecagr'] is not None)
        uwt = sum(r['value_eur'] for r in upos if r['ecagr'] is not None)
        uec = uw / uwt if uwt > 0 else None
        uec_str = f"{uec:.1f}%" if uec is not None else 'N/A'
        print(f"  {'Unassigned':<25} {len(upos):>3} {uval:>8,.0f} {upct:>5.1f}% {uec_str:>10}")
    print()


def print_report(pos, univ, cash_eur, eurusd, target, verbose, baskets_data=None):
    tot_val = sum(r['value_eur'] for r in pos)
    ptot = tot_val + cash_eur
    cash_pct = cash_eur / ptot * 100 if ptot > 0 else 0
    dep_pct = 100 - cash_pct

    wsum = sum(r['ecagr'] * r['value_eur'] for r in pos if r['ecagr'] is not None)
    wtot = sum(r['value_eur'] for r in pos if r['ecagr'] is not None)
    pecagr = wsum / wtot if wtot > 0 else 0
    drag = cash_pct / 100 * max(pecagr - CASH_YIELD_PCT, 0)
    blended = dep_pct / 100 * pecagr + cash_pct / 100 * CASH_YIELD_PCT

    print(f"\nPORTFOLIO EXPECTED CAGR PROJECTION\n{'='*72}")
    print(f"Positions:      {len(pos)} ({dep_pct:.1f}% deployed)")
    print(f"Cash:           {cash_pct:.1f}% (EUR {cash_eur:,.0f}) -- COST: ~{drag:.1f}pp/yr drag")
    print(f"Portfolio E[CAGR] (deployed only): {pecagr:.1f}%")
    print(f"Blended E[CAGR] (incl. cash):     {blended:.1f}%")
    print(f"Target: {target:.0f}%+ CAGR")
    print(f"  Gap to target: {blended - target:+.1f}pp\n")

    ranked = sorted(pos, key=lambda r: r['ecagr'] if r['ecagr'] is not None else -999, reverse=True)
    print(f"POSITION RANKING (by E[CAGR], descending)\n{'-'*72}")
    h = f"  {'#':>2} {'Ticker':<10} {'E[CAGR]':>8} {'Size%':>6} {'EUR Val':>8} {'MoS%':>7} {'QS':>3} {'Tier':>4} {'Conv':>4}"
    if verbose: h += f" {'Grw%':>6} {'Yld%':>5} {'Src':>7}"
    print(h); print("  " + "-" * (70 if not verbose else 90))

    for i, r in enumerate(ranked, 1):
        ec = f"{r['ecagr']:.1f}%" if r['ecagr'] is not None else '  N/A'
        sp = r['value_eur'] / ptot * 100 if ptot > 0 else 0
        ms = f"{r['mos_pct']:+.1f}" if r['mos_pct'] is not None else '  N/A'
        qs = str(r['qs']) if r['qs'] is not None else '?'
        ln = f"  {i:>2} {r['ticker']:<10} {ec:>8} {sp:>5.1f}% {r['value_eur']:>8,.0f} {ms:>7} {qs:>3} {r['tier'] or '?':>4} {r['conv']:>4}"
        if verbose:
            gf, df = f"{r['growth_pct']:.1f}", f"{r['div_yield']:.1f}"
            ln += f" {gf:>6} {df:>5} {r['growth_src']:>7}"
        if i == len(ranked) and r['ecagr'] is not None: ln += "  <-- WORST"
        if r['error']: ln += f"  [{r['error']}]"
        print(ln)
    print()

    # Basket breakdown (if --baskets)
    if baskets_data:
        print_basket_breakdown(ranked, baskets_data, ptot)

    if univ is not None:
        ptickers = {r['ticker'] for r in pos}
        uf = [u for u in univ if u['ticker'] not in ptickers]
        print(f"MARKET BUY CANDIDATES (from universe, E[CAGR]@market >= threshold)\n{'-'*72}")
        print(f"  Tier A: >=12% | Tier B: >=15% | Conservative (div yield only, no growth)\n")
        if uf:
            print(f"  {'#':>2} {'Ticker':<10} {'E[CAGR]':>8} {'Price':>10} {'FV':>10} {'MoS%':>7} {'QS':>3} {'Tier':>4} {'Pipeline'}")
            print("  " + "-" * 68)
            for i, u in enumerate(uf[:15], 1):
                print(f"  {i:>2} {u['ticker']:<10} {u['ecagr_market']:.1f}%{' ':>2} {u['price']:>10.2f} {u['fv']:>10.0f} {u['mos_pct']:>+7.1f} {u['qs']:>3} {u['tier']:>4} {u['pipeline']}")
            if len(uf) > 15: print(f"  ... and {len(uf)-15} more")
        else:
            print("  No candidates meet thresholds at current prices.")
        print()

        worst = ranked[-1] if ranked and ranked[-1]['ecagr'] is not None else None
        if worst and uf:
            rots = [u for u in uf if u['ecagr_market'] > worst['ecagr'] + 3.0]
            if rots:
                print(f"ROTATION CANDIDATES (candidate E[CAGR] > worst + 3pp)\n{'-'*72}")
                for rc in rots[:5]:
                    imp = rc['ecagr_market'] - worst['ecagr']
                    print(f"  SELL {worst['ticker']} at {worst['ecagr']:.1f}% -> BUY {rc['ticker']} at {rc['ecagr_market']:.1f}% = +{imp:.1f}pp")
                print()

    if univ is not None and cash_eur > 0:
        ptickers = {r['ticker'] for r in pos}
        dc = [u for u in univ if u['ticker'] not in ptickers]
        print(f"CASH DEPLOYMENT SCENARIO\n{'-'*72}")
        if dc:
            tr = 400; n = min(int(cash_eur * 0.85 / tr), len(dc), 5)
            if n > 0:
                dep = n * tr; rem = cash_eur - dep
                nv = tot_val + dep; nt = nv + rem; ncp = rem / nt * 100
                ds = sum(dc[i]['ecagr_market'] * tr for i in range(n))
                npe = (wsum + ds) / (wtot + n * tr) if (wtot + n * tr) > 0 else 0
                nb = nv / nt * npe + rem / nt * CASH_YIELD_PCT
                nd = ncp / 100 * max(npe - CASH_YIELD_PCT, 0)
                print(f"  EUR {cash_eur:,.0f} -> top {n} at EUR {tr} each = EUR {dep:,.0f}")
                print(f"  Candidates: {', '.join(dc[i]['ticker'] for i in range(n))}")
                print(f"  Remaining cash: EUR {rem:,.0f} ({ncp:.1f}%)")
                print(f"  Projected E[CAGR] after: {npe:.1f}% (vs {pecagr:.1f}% current)")
                print(f"  Blended after:           {nb:.1f}% (vs {blended:.1f}% current)")
                print(f"  Cash drag after:         ~{nd:.1f}pp/yr (vs ~{drag:.1f}pp/yr current)")
            else: print("  Insufficient cash for EUR 400 tranches.")
        else: print("  No viable candidates in universe.")
        print()
    print("[Raw data. Reason from principles.md]\n")

def main():
    ap = argparse.ArgumentParser(description='Portfolio CAGR Projector')
    ap.add_argument('--no-universe', action='store_true', help='Skip universe scan')
    ap.add_argument('--verbose', action='store_true', help='Extra detail per position')
    ap.add_argument('--target-cagr', type=float, default=30.0, help='Target CAGR %%')
    ap.add_argument('--baskets', action='store_true', help='Add basket E[CAGR] breakdown')
    args = ap.parse_args()

    pf = load_yaml(PORTFOLIO_FILE)
    if not pf: print("ERROR: Cannot load portfolio/current.yaml"); sys.exit(1)
    sqs = load_system_qs()
    cash = pf.get('cash',{}).get('amount', 0)
    print("Loading FX rates and position data...")
    eurusd, gbpeur, dkkeur = get_fx_rates()
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/EUR={gbpeur:.4f} | DKK/EUR={dkkeur:.4f}")
    pos = process_positions(pf, eurusd, gbpeur, dkkeur, sqs)
    print(f"Processed {len(pos)} positions.")
    univ = None
    if not args.no_universe:
        print("Scanning quality universe...")
        univ = scan_universe(eurusd, gbpeur, dkkeur)
        print(f"Found {len(univ)} candidates above thresholds.")
    bd = load_yaml(BASKETS_FILE) if args.baskets else None
    print_report(pos, univ, cash, eurusd, args.target_cagr, args.verbose, baskets_data=bd)

if __name__ == '__main__':
    main()

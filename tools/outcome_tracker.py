#!/usr/bin/env python3
"""
Buy Decision Outcome Tracker - How are my buy decisions performing?
Usage:
    python3 tools/outcome_tracker.py              # Full report (active + closed)
    python3 tools/outcome_tracker.py --active-only # Active positions only
Reads portfolio/current.yaml + portfolio/history.yaml. yfinance for live prices.
Output: RAW DATA only.
"""
import argparse, os, sys
from datetime import datetime, date
import yaml, yfinance as yf

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRENT_FILE = os.path.join(BASE, 'portfolio', 'current.yaml')
HISTORY_FILE = os.path.join(BASE, 'portfolio', 'history.yaml')
TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

def load_yaml(path):
    if not os.path.exists(path): return {}
    with open(path, 'r') as f: return yaml.safe_load(f) or {}

def get_fx():
    defs = {'EURUSD': 1.16, 'GBPUSD': 1.33}
    fb, eurusd, gbpusd = [], defs['EURUSD'], defs['GBPUSD']
    for pair, key in [('EURUSD=X', 'EURUSD'), ('GBPUSD=X', 'GBPUSD')]:
        try:
            v = yf.Ticker(pair).info.get('previousClose')
            if v:
                if key == 'EURUSD': eurusd = v
                else: gbpusd = v
            else: fb.append(f"{key}={defs[key]}")
        except Exception: fb.append(f"{key}={defs[key]}")
    if fb: print(f"FX WARNING: Static fallback ({', '.join(fb)}). Amounts may be inaccurate.")
    return eurusd, gbpusd

def to_usd(price, cur, eurusd, gbpusd):
    if cur == 'EUR': return price * eurusd
    if cur in ('GBp', 'GBX'): return (price / 100) * gbpusd
    if cur == 'GBP': return price * gbpusd
    return price

def fetch_price(ticker, eurusd, gbpusd):
    try:
        info = yf.Ticker(TICKER_MAP.get(ticker, ticker)).info
        p = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        cur = info.get('currency', 'USD')
        return (p, cur, to_usd(p, cur, eurusd, gbpusd)) if p else (None, None, None)
    except Exception: return None, None, None

def days_held(ds):
    if not ds: return 0
    try: return (date.today() - datetime.strptime(str(ds), '%Y-%m-%d').date()).days
    except Exception: return 0

def fmt_price(val, cur=''):
    if val is None: return 'N/A'
    if cur in ('GBp', 'GBX'): return f"{val:.0f}p"
    if cur == 'EUR': return f"E{val:.2f}"
    return f"${val:.2f}"

def main():
    ap = argparse.ArgumentParser(description='Buy Decision Outcome Tracker')
    ap.add_argument('--active-only', action='store_true', help='Active positions only')
    args = ap.parse_args()

    current = load_yaml(CURRENT_FILE)
    history = load_yaml(HISTORY_FILE)
    positions = current.get('positions', [])
    closed_list = history.get('closed_positions', []) if not args.active_only else []
    eurusd, gbpusd = get_fx()

    # --- ACTIVE ---
    active_rows, tot_inv_eur, tot_val_eur = [], 0, 0
    for p in positions:
        ticker, shares = p['ticker'], p.get('shares', 0)
        inv_usd, inv_eur_raw = p.get('invested_usd'), p.get('invested_eur')
        if inv_usd: inv_eur = inv_usd / eurusd
        elif inv_eur_raw: inv_eur = inv_eur_raw
        else: continue
        avg_usd = p.get('avg_cost_usd', (inv_usd or 0) / max(shares, 1))
        _, _, price_usd = fetch_price(ticker, eurusd, gbpusd)
        if price_usd is None:
            active_rows.append({'ticker': ticker, 'error': True}); continue
        val_usd = price_usd * shares
        val_eur = val_usd / eurusd
        base = inv_usd or (inv_eur * eurusd)
        pnl_pct = ((val_usd - base) / base * 100) if base else 0
        tot_inv_eur += inv_eur; tot_val_eur += val_eur
        active_rows.append({
            'ticker': ticker, 'avg_usd': avg_usd, 'price_usd': price_usd,
            'pnl_pct': pnl_pct, 'pnl_eur': val_eur - inv_eur,
            'days': days_held(p.get('date_opened')), 'inv_eur': inv_eur,
            'fv': p.get('fair_value', ''), 'error': False
        })

    # --- CLOSED ---
    closed_rows, tot_cl_pnl, cl_wins, cl_losses, cl_even, tot_cl_days = [], 0, 0, 0, 0, 0
    for c in closed_list:
        ticker = c.get('ticker', '?')
        pnl_pct, hd = c.get('pnl_percent', 0), c.get('holding_days', 0)
        reason = c.get('exit_reason', '')
        # Entry/exit display
        ed, xd = '', ''
        if 'entry_price' in c:
            cur = c.get('entry_currency', '')
            ed, xd = fmt_price(c['entry_price'], cur), fmt_price(c.get('exit_price'), cur)
        elif 'entry_price_gbp' in c:
            ed, xd = f"{c['entry_price_gbp']:.0f}p", f"{c.get('exit_price_gbp',0):.0f}p"
        elif 'entry_price_usd' in c:
            ed, xd = f"${c['entry_price_usd']:.2f}", f"${c.get('exit_price_usd',0):.2f}"
        elif 'entry_price_eur' in c:
            ed, xd = f"E{c['entry_price_eur']:.2f}", f"E{c.get('exit_price_eur',0):.2f}"
        pnl_amt = c.get('pnl_amount_eur', c.get('pnl_amount', 0)) or 0
        tot_cl_pnl += pnl_amt; tot_cl_days += hd
        if pnl_pct > 0.05: cl_wins += 1
        elif pnl_pct < -0.05: cl_losses += 1
        else: cl_even += 1
        closed_rows.append({'ticker': ticker, 'entry': ed, 'exit': xd,
                            'pnl_pct': pnl_pct, 'days': hd, 'reason': reason})

    # --- OUTPUT ---
    valid = [r for r in active_rows if not r.get('error')]
    n_a, n_c = len(valid), len(closed_rows)
    print("\nBUY DECISION OUTCOME TRACKER")
    print("=" * 72)
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/USD={gbpusd:.4f}")
    lbl = f"Active: {n_a} positions"
    if not args.active_only: lbl += f" | Closed: {n_c} positions | Total decisions: {n_a+n_c}"
    print(lbl + "\n")

    # Active table
    print("ACTIVE POSITIONS:")
    print(f"  {'#':>2} {'Ticker':<10} {'Entry':>9} {'Current':>9} {'P&L%':>7} {'Days':>5} {'InvEUR':>7} {'FV':>12} {'Status'}")
    print(f"  {'':->2} {'':->10} {'':->9} {'':->9} {'':->7} {'':->5} {'':->7} {'':->12} {'':->6}")
    a_wins = 0
    for i, r in enumerate(active_rows, 1):
        if r.get('error'):
            print(f"  {i:>2} {r['ticker']:<10} {'ERROR':>9}"); continue
        fv_s = r['fv'][:12] if r['fv'] else ''
        if r['pnl_pct'] > 0.05: a_wins += 1
        print(f"  {i:>2} {r['ticker']:<10} ${r['avg_usd']:>8.2f} ${r['price_usd']:>8.2f} {r['pnl_pct']:>+6.1f}% {r['days']:>5} {r['inv_eur']:>7.0f} {fv_s:>12} HOLD")
    a_pnl = tot_val_eur - tot_inv_eur
    a_pct = (a_pnl / tot_inv_eur * 100) if tot_inv_eur else 0
    avg_a_d = (sum(r['days'] for r in valid) / len(valid)) if valid else 0
    print(f"  Active P&L: EUR {a_pnl:+.0f} ({a_pct:+.1f}% weighted avg)\n")

    # Closed table
    if not args.active_only and closed_rows:
        print("CLOSED POSITIONS:")
        print(f"  {'#':>2} {'Ticker':<10} {'Entry':>9} {'Exit':>9} {'P&L%':>7} {'Days':>5} {'Exit Reason'}")
        print(f"  {'':->2} {'':->10} {'':->9} {'':->9} {'':->7} {'':->5} {'':->30}")
        for i, r in enumerate(closed_rows, 1):
            print(f"  {i:>2} {r['ticker']:<10} {r['entry']:>9} {r['exit']:>9} {r['pnl_pct']:>+6.1f}% {r['days']:>5} {r['reason']}")
        wr = (cl_wins / n_c * 100) if n_c else 0
        avg_cd = (tot_cl_days / n_c) if n_c else 0
        print(f"  Closed P&L: EUR {tot_cl_pnl:+.0f} ({wr:.0f}% win rate, avg hold {avg_cd:.0f}d)\n")

    # Aggregate
    print("AGGREGATE:")
    total_pnl = a_pnl + tot_cl_pnl
    total_pct = (total_pnl / tot_inv_eur * 100) if tot_inv_eur else 0
    a_losers = sum(1 for r in valid if r['pnl_pct'] < -0.05)
    tw = a_wins + cl_wins
    td = n_a + n_c
    owr = (tw / td * 100) if td else 0
    print(f"  Total active invested: EUR {tot_inv_eur:,.0f}")
    print(f"  Total P&L (active+closed): EUR {total_pnl:+,.0f} ({total_pct:+.1f}%)")
    print(f"  Win rate: Active {a_wins}/{n_a} + Closed {cl_wins}/{n_c} = {tw}/{td} ({owr:.0f}%)")
    print(f"  Avg hold (active): {avg_a_d:.0f} days")
    if not args.active_only and closed_rows:
        print(f"  Avg hold (closed): {(tot_cl_days/n_c) if n_c else 0:.0f} days")
    # Best/worst
    all_pnl = [(r['ticker'], r['pnl_pct']) for r in valid] + [(r['ticker'], r['pnl_pct']) for r in closed_rows]
    if all_pnl:
        best, worst = max(all_pnl, key=lambda x: x[1]), min(all_pnl, key=lambda x: x[1])
        print(f"  Largest winner:  {best[0]} {best[1]:+.1f}%")
        print(f"  Largest loser:   {worst[0]} {worst[1]:+.1f}%")
    print("\n[Raw data. Track across sessions for calibration.]")

if __name__ == '__main__':
    main()

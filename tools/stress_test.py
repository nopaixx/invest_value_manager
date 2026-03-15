#!/usr/bin/env python3
"""
Portfolio Stress Test — Real betas, Monte Carlo, 2008 GFC scenario, crisis correlations, liquidity.

Usage:
  python3 tools/stress_test.py                       # Full stress test (includes Monte Carlo 10K sims)
  python3 tools/stress_test.py --quick               # Skip Monte Carlo (faster)
  python3 tools/stress_test.py --compare YYYY-MM-DD  # Compare vs specific date's report

Output:
  - Terminal summary with all metrics
  - JSON report saved to reports/stress_test/YYYY-MM-DD.json
  - Delta comparison if previous report exists

Sections:
  1. Real Betas (1Y daily returns vs S&P 500)
  2. Monte Carlo (10K sims, Student-t fat tails, crisis beta amplification)
  3. 2008 GFC Scenario (real sector drawdowns applied to portfolio)
  4. Crisis Correlations (worst 10% S&P days vs normal days)
  5. Liquidity Check (avg daily volume vs position size)
"""

import argparse
import json
import os
import sys
from datetime import datetime, date

import numpy as np
import pandas as pd
import yaml
import yfinance as yf

# =============================================================================
# CONFIGURATION — Position-to-Sector Mapping
# =============================================================================
# Format: 'TICKER': ('sector_key', adjustment_factor, 'rationale')
# adjustment_factor: 1.0 = full sector exposure, <1.0 = partial (different sub-sector)
# Update this dict when portfolio changes.

SECTOR_MAP = {
    'EDEN.PA': ('consumer_disc', 0.60, 'Employee benefits fintech, not pure consumer disc'),
    'ADBE': ('technology', 1.0, 'Software, direct match'),
    'NVO': ('healthcare', 1.0, 'Pharma, direct match'),
    'MONY.L': ('consumer_disc', 0.80, 'Insurance comparison, consumer-facing'),
    'IHP.L': ('financials', 0.35, 'Adviser platform, NOT bank'),
    'HLNE': ('financials', 0.70, 'Alt asset mgmt, PE fundraising correlated'),
    'DOCS': ('healthcare', 0.90, 'Healthcare IT/advertising'),
    'FTNT': ('technology', 0.80, 'Cybersecurity, non-discretionary'),
    'TW': ('financials', 0.40, 'Bond trading, benefits from vol in crisis'),
    'WKL.AS': ('technology', 0.50, 'Legal/tax info, consumer staples behavior'),
    'BZU.MI': ('materials', 1.0, 'Cement, direct match'),
    'CVNA': ('consumer_disc', 1.0, 'Used car retail, full consumer disc exposure'),
}

# 2008 GFC — REAL S&P sector drawdowns (peak-to-trough)
GFC_SECTOR_DRAWDOWNS = {
    'technology': -0.494,
    'healthcare': -0.375,
    'financials': -0.831,
    'consumer_disc': -0.594,
    'industrials': -0.580,
    'energy': -0.521,
    'materials': -0.563,
    'consumer_staples': -0.283,
    'utilities': -0.342,
    'real_estate': -0.680,
    'communication': -0.450,
}

# =============================================================================
# PATHS
# =============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
REPORT_DIR = os.path.join(BASE_DIR, 'reports', 'stress_test')

# =============================================================================
# PORTFOLIO LOADING
# =============================================================================

def load_portfolio():
    """Load portfolio from current.yaml. Returns positions list, short_positions list, cash."""
    with open(PORTFOLIO_FILE, 'r') as f:
        data = yaml.safe_load(f)
    positions = data.get('positions', [])
    short_positions = data.get('short_positions', [])
    cash = data.get('cash', {}).get('amount', 0)
    return positions, short_positions, cash


def get_fx_rates():
    """Get EUR/USD and GBP/USD rates via yfinance with fallbacks."""
    defaults = {'EURUSD': 1.16, 'GBPUSD': 1.33}
    fallbacks = []
    rates = {}
    for pair, default in defaults.items():
        try:
            t = yf.Ticker(f'{pair}=X')
            rate = t.info.get('previousClose') or t.info.get('regularMarketPrice')
            if rate and rate > 0:
                rates[pair] = float(rate)
            else:
                rates[pair] = default
                fallbacks.append(f"{pair}={default}")
        except Exception:
            rates[pair] = default
            fallbacks.append(f"{pair}={default}")
    if fallbacks:
        print(f"  FX WARNING: Using fallback rates ({', '.join(fallbacks)})")
    return rates['EURUSD'], rates['GBPUSD']


def build_position_list(positions, short_positions, eurusd, gbpusd):
    """Build unified list of positions with ticker, shares, weight_usd, direction."""
    items = []
    total_value = 0.0

    for p in positions:
        ticker = p['ticker']
        shares = p['shares']
        # Estimate current value from invested (will be refined with live prices later)
        if 'invested_usd' in p:
            val = p['invested_usd']
        elif 'invested_eur' in p:
            val = p['invested_eur'] * eurusd
        else:
            continue
        items.append({'ticker': ticker, 'shares': shares, 'value_usd': val, 'direction': 'long'})
        total_value += val

    for s in short_positions:
        ticker = s['ticker']
        shares = s['shares']
        val = s.get('entry_price_usd', 0) * shares
        items.append({'ticker': ticker, 'shares': shares, 'value_usd': val, 'direction': 'short'})
        total_value += val

    # Calculate weights
    for item in items:
        item['weight'] = item['value_usd'] / total_value if total_value > 0 else 0

    return items, total_value


# =============================================================================
# 1. REAL BETAS
# =============================================================================

def download_returns(tickers, period='1y'):
    """Download 1Y daily returns for tickers + S&P 500."""
    all_tickers = list(set(tickers + ['^GSPC']))
    print(f"  Downloading {period} data for {len(all_tickers)} tickers...")

    data = yf.download(all_tickers, period=period, progress=False, auto_adjust=True)

    # Handle multi-level columns from yfinance
    if isinstance(data.columns, pd.MultiIndex):
        close = data['Close']
    else:
        # Single ticker case
        close = data[['Close']].copy()
        close.columns = all_tickers[:1]

    # Calculate daily returns
    returns = close.pct_change().dropna()

    # Report missing tickers
    downloaded = set(returns.columns.tolist())
    missing = set(all_tickers) - downloaded
    if missing:
        print(f"  WARNING: Missing data for: {', '.join(missing)}")

    return returns


def calculate_betas(returns, position_list):
    """Calculate beta of each position vs S&P 500."""
    if '^GSPC' not in returns.columns:
        print("  ERROR: S&P 500 data not available for beta calculation")
        return {}

    market = returns['^GSPC']
    market_var = market.var()
    if market_var == 0:
        return {}

    betas = {}
    for item in position_list:
        ticker = item['ticker']
        if ticker in returns.columns:
            cov = returns[ticker].cov(market)
            beta = cov / market_var
            betas[ticker] = {
                'beta': float(beta),
                'weight': item['weight'],
                'direction': item['direction'],
                'annual_vol': float(returns[ticker].std() * np.sqrt(252)),
            }
        else:
            print(f"  WARNING: No return data for {ticker}, using beta=1.0")
            betas[ticker] = {
                'beta': 1.0,
                'weight': item['weight'],
                'direction': item['direction'],
                'annual_vol': 0.20,
            }

    return betas


def portfolio_weighted_beta(betas):
    """Calculate portfolio-weighted beta (shorts contribute negative beta)."""
    weighted_beta = 0.0
    for ticker, info in betas.items():
        sign = 1.0 if info['direction'] == 'long' else -1.0
        weighted_beta += info['weight'] * info['beta'] * sign
    return weighted_beta


# =============================================================================
# 2. MONTE CARLO
# =============================================================================

def run_monte_carlo(betas, market_annual_vol, n_sims=10000, seed=42):
    """
    Monte Carlo simulation using real betas and volatilities.
    Uses Student-t distribution (df=5) for fat tails.
    In crisis (market < -20%), betas amplified by 1.5x.
    Returns dict with percentiles and loss probabilities.
    """
    np.random.seed(seed)

    market_daily_vol = market_annual_vol / np.sqrt(252)

    # Generate market returns from Student-t (df=5) — fatter tails than normal
    # Scale t-distribution to match observed market vol
    t_samples = np.random.standard_t(df=5, size=n_sims)
    # Scale so that std matches market_annual_vol
    # std of t(5) = sqrt(5/3) ~ 1.291
    t_std = np.sqrt(5.0 / 3.0)
    market_returns = t_samples * (market_annual_vol / t_std)

    # Clip extreme draws
    market_returns = np.clip(market_returns, -0.70, 0.50)

    portfolio_returns = np.zeros(n_sims)

    for ticker, info in betas.items():
        beta = info['beta']
        weight = info['weight']
        stock_vol = info['annual_vol']
        sign = 1.0 if info['direction'] == 'long' else -1.0

        # Idiosyncratic vol component
        idio_vol = max(0, stock_vol**2 - (beta * market_annual_vol)**2)
        idio_vol = np.sqrt(idio_vol) if idio_vol > 0 else 0

        # Generate idiosyncratic returns (also Student-t)
        idio_samples = np.random.standard_t(df=5, size=n_sims) * (idio_vol / t_std)

        # In crisis scenarios (market < -20%), amplify beta by 1.5x
        crisis_mask = market_returns < -0.20
        effective_beta = np.where(crisis_mask, beta * 1.5, beta)

        stock_returns = effective_beta * market_returns + idio_samples
        stock_returns = np.clip(stock_returns, -0.90, 1.0)

        portfolio_returns += weight * sign * stock_returns

    # Calculate percentiles
    percentiles = {}
    for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
        percentiles[f'P{p}'] = float(np.percentile(portfolio_returns, p))

    # Loss probabilities
    loss_probs = {}
    for threshold in [10, 20, 30, 40, 50]:
        prob = float(np.mean(portfolio_returns < -threshold / 100))
        loss_probs[f'loss_gt_{threshold}pct'] = prob

    return {
        'percentiles': percentiles,
        'loss_probabilities': loss_probs,
        'mean_return': float(np.mean(portfolio_returns)),
        'median_return': float(np.median(portfolio_returns)),
        'std_return': float(np.std(portfolio_returns)),
        'n_simulations': n_sims,
        'market_annual_vol': float(market_annual_vol),
    }


# =============================================================================
# 3. 2008 GFC SCENARIO
# =============================================================================

def gfc_scenario(betas, position_list):
    """
    Apply 2008 GFC sector drawdowns to portfolio positions.
    Returns per-position and portfolio-weighted drawdown.
    """
    results = []
    portfolio_drawdown = 0.0

    for item in position_list:
        ticker = item['ticker']
        weight = item['weight']
        direction = item['direction']

        mapping = SECTOR_MAP.get(ticker)
        if mapping:
            sector, adj_factor, rationale = mapping
            base_dd = GFC_SECTOR_DRAWDOWNS.get(sector, -0.50)
            adjusted_dd = base_dd * adj_factor
        else:
            # Default: average drawdown
            adjusted_dd = -0.50
            sector = 'unknown'
            adj_factor = 1.0
            rationale = 'No mapping, using -50% default'

        # For shorts, a market crash is beneficial
        if direction == 'short':
            pnl_impact = -adjusted_dd * weight  # positive (we profit from the drop)
        else:
            pnl_impact = adjusted_dd * weight  # negative (we lose)

        portfolio_drawdown += pnl_impact

        results.append({
            'ticker': ticker,
            'direction': direction,
            'sector': sector,
            'weight': float(weight),
            'sector_drawdown': float(base_dd) if mapping else -0.50,
            'adj_factor': float(adj_factor),
            'position_drawdown': float(adjusted_dd),
            'portfolio_impact': float(pnl_impact),
            'rationale': rationale if mapping else 'No mapping',
        })

    return {
        'positions': results,
        'portfolio_drawdown': float(portfolio_drawdown),
    }


# =============================================================================
# 4. CRISIS CORRELATIONS
# =============================================================================

def crisis_correlations(returns):
    """
    Compare pairwise correlations on worst 10% S&P days vs normal days.
    Returns crisis avg correlation, normal avg correlation, and the spike multiplier.
    """
    if '^GSPC' not in returns.columns:
        return {'error': 'No S&P 500 data available'}

    market = returns['^GSPC']
    threshold = market.quantile(0.10)  # worst 10% = below 10th percentile

    crisis_days = returns[market <= threshold]
    normal_days = returns[market > threshold]

    # Get stock columns only (exclude ^GSPC)
    stock_cols = [c for c in returns.columns if c != '^GSPC']

    if len(stock_cols) < 2:
        return {'error': 'Need at least 2 stocks for correlation analysis'}

    crisis_corr = crisis_days[stock_cols].corr()
    normal_corr = normal_days[stock_cols].corr()

    # Average off-diagonal correlation
    n = len(stock_cols)
    mask = np.ones((n, n), dtype=bool)
    np.fill_diagonal(mask, False)

    crisis_avg = float(crisis_corr.where(mask).mean().mean())
    normal_avg = float(normal_corr.where(mask).mean().mean())

    spike = crisis_avg / normal_avg if normal_avg != 0 else float('inf')

    return {
        'crisis_avg_correlation': crisis_avg,
        'normal_avg_correlation': normal_avg,
        'spike_multiplier': float(spike),
        'crisis_days_count': len(crisis_days),
        'normal_days_count': len(normal_days),
        'threshold_return': float(threshold),
    }


# =============================================================================
# 5. LIQUIDITY CHECK
# =============================================================================

def liquidity_check(position_list):
    """
    For each position, get 3-month average daily volume and compare to position size.
    Flag positions where liquidation > 0.5 days at average volume.
    """
    results = []

    for item in position_list:
        ticker = item['ticker']
        shares = item['shares']

        try:
            t = yf.Ticker(ticker)
            hist = t.history(period='3mo')
            if hist.empty or 'Volume' not in hist.columns:
                avg_vol = 0
            else:
                avg_vol = int(hist['Volume'].mean())
        except Exception:
            avg_vol = 0

        days_to_liquidate = shares / avg_vol if avg_vol > 0 else float('inf')

        if avg_vol >= 500_000:
            risk_level = 'LOW'
        elif avg_vol >= 50_000:
            risk_level = 'MEDIUM'
        else:
            risk_level = 'HIGH'

        flagged = days_to_liquidate > 0.5

        results.append({
            'ticker': ticker,
            'shares': float(shares),
            'avg_daily_volume': avg_vol,
            'days_to_liquidate': float(min(days_to_liquidate, 999)),
            'risk_level': risk_level,
            'flagged': flagged,
        })

    return results


# =============================================================================
# REPORTING
# =============================================================================

def save_report(report_data):
    """Save report to JSON file."""
    os.makedirs(REPORT_DIR, exist_ok=True)
    today = date.today().isoformat()
    filepath = os.path.join(REPORT_DIR, f'{today}.json')

    # Convert any remaining numpy types
    def convert(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.bool_,)):
            return bool(obj)
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    with open(filepath, 'w') as f:
        json.dump(report_data, f, indent=2, default=convert)

    return filepath


def load_previous_report(compare_date=None):
    """Load a previous report for comparison. If no date given, find the most recent."""
    if not os.path.isdir(REPORT_DIR):
        return None

    if compare_date:
        filepath = os.path.join(REPORT_DIR, f'{compare_date}.json')
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return None

    # Find most recent
    files = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.json')])
    today_file = f'{date.today().isoformat()}.json'
    # Exclude today's file
    files = [f for f in files if f != today_file]
    if not files:
        return None

    filepath = os.path.join(REPORT_DIR, files[-1])
    with open(filepath, 'r') as f:
        return json.load(f)


def print_delta(label, current, previous, fmt='.1f', invert=False):
    """Print a metric with delta vs previous. invert=True means lower is better."""
    if previous is None:
        return f"  {label}: {current:{fmt}}%"
    delta = current - previous
    if invert:
        arrow = 'BETTER' if delta < 0 else 'WORSE' if delta > 0 else 'SAME'
    else:
        arrow = 'BETTER' if delta > 0 else 'WORSE' if delta < 0 else 'SAME'
    return f"  {label}: {current:{fmt}}%  (prev: {previous:{fmt}}%, delta: {delta:+{fmt}}pp {arrow})"


# =============================================================================
# MAIN OUTPUT
# =============================================================================

def print_results(betas, mc_results, gfc, crisis_corr, liquidity, prev_report, quick_mode):
    """Print formatted summary to stdout."""
    print()
    print("=" * 80)
    print("PORTFOLIO STRESS TEST")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 80)

    # --- Section 1: Real Betas ---
    print()
    print("-" * 80)
    print("1. REAL BETAS (1Y daily returns vs S&P 500)")
    print("-" * 80)
    print(f"  {'Ticker':<10} {'Beta':>6} {'Ann.Vol':>8} {'Weight':>7} {'Dir':>5}")
    print(f"  {'-'*10} {'-'*6} {'-'*8} {'-'*7} {'-'*5}")
    for ticker in sorted(betas.keys()):
        info = betas[ticker]
        d = 'L' if info['direction'] == 'long' else 'S'
        print(f"  {ticker:<10} {info['beta']:>6.2f} {info['annual_vol']*100:>7.1f}% {info['weight']*100:>6.1f}% {d:>5}")

    wb = portfolio_weighted_beta(betas)
    prev_wb = prev_report.get('portfolio_weighted_beta') if prev_report else None
    print()
    if prev_wb is not None:
        delta = wb - prev_wb
        print(f"  Portfolio Weighted Beta: {wb:.3f}  (prev: {prev_wb:.3f}, delta: {delta:+.3f})")
    else:
        print(f"  Portfolio Weighted Beta: {wb:.3f}")

    # --- Section 2: Monte Carlo ---
    print()
    print("-" * 80)
    if quick_mode:
        print("2. MONTE CARLO — SKIPPED (--quick mode)")
    else:
        print(f"2. MONTE CARLO ({mc_results['n_simulations']:,} simulations, Student-t df=5, crisis beta 1.5x)")
        print("-" * 80)

        print()
        print("  Return Percentiles (annual):")
        prev_pct = prev_report.get('monte_carlo', {}).get('percentiles', {}) if prev_report else {}
        for key, val in mc_results['percentiles'].items():
            prev_val = prev_pct.get(key)
            line = print_delta(f"    {key}", val * 100, prev_val * 100 if prev_val else None, fmt='.1f')
            print(line)

        print()
        print("  Loss Probabilities:")
        prev_lp = prev_report.get('monte_carlo', {}).get('loss_probabilities', {}) if prev_report else {}
        for key, val in mc_results['loss_probabilities'].items():
            pct_label = key.replace('loss_gt_', '>').replace('pct', '%')
            prev_val = prev_lp.get(key)
            if prev_val is not None:
                delta = val - prev_val
                arrow = 'BETTER' if delta < 0 else 'WORSE' if delta > 0 else 'SAME'
                print(f"    P(loss {pct_label}): {val*100:.1f}%  (prev: {prev_val*100:.1f}%, delta: {delta*100:+.1f}pp {arrow})")
            else:
                print(f"    P(loss {pct_label}): {val*100:.1f}%")

        print()
        print(f"  Mean return: {mc_results['mean_return']*100:.1f}%")
        print(f"  Std deviation: {mc_results['std_return']*100:.1f}%")
    print("-" * 80)

    # --- Section 3: 2008 GFC ---
    print()
    print("-" * 80)
    print("3. 2008 GFC SCENARIO (real sector drawdowns)")
    print("-" * 80)
    print(f"  {'Ticker':<10} {'Dir':>3} {'Sector':<15} {'Sec.DD':>7} {'AdjF':>5} {'Pos.DD':>7} {'Ptf.Impact':>10}")
    print(f"  {'-'*10} {'-'*3} {'-'*15} {'-'*7} {'-'*5} {'-'*7} {'-'*10}")
    for p in gfc['positions']:
        d = 'L' if p['direction'] == 'long' else 'S'
        print(f"  {p['ticker']:<10} {d:>3} {p['sector']:<15} {p['sector_drawdown']*100:>6.1f}% {p['adj_factor']:>5.2f} {p['position_drawdown']*100:>6.1f}% {p['portfolio_impact']*100:>+9.1f}%")

    prev_gfc_dd = prev_report.get('gfc_scenario', {}).get('portfolio_drawdown') if prev_report else None
    print()
    if prev_gfc_dd is not None:
        delta = gfc['portfolio_drawdown'] - prev_gfc_dd
        arrow = 'BETTER' if delta > 0 else 'WORSE' if delta < 0 else 'SAME'
        print(f"  Portfolio GFC Drawdown: {gfc['portfolio_drawdown']*100:.1f}%  (prev: {prev_gfc_dd*100:.1f}%, delta: {delta*100:+.1f}pp {arrow})")
    else:
        print(f"  Portfolio GFC Drawdown: {gfc['portfolio_drawdown']*100:.1f}%")

    # --- Section 4: Crisis Correlations ---
    print()
    print("-" * 80)
    print("4. CRISIS CORRELATIONS (worst 10% S&P days)")
    print("-" * 80)
    if 'error' in crisis_corr:
        print(f"  {crisis_corr['error']}")
    else:
        print(f"  Crisis days analyzed: {crisis_corr['crisis_days_count']}")
        print(f"  Crisis threshold: {crisis_corr['threshold_return']*100:.2f}% daily return")
        print(f"  Normal avg correlation: {crisis_corr['normal_avg_correlation']:.3f}")
        print(f"  Crisis avg correlation: {crisis_corr['crisis_avg_correlation']:.3f}")

        prev_spike = prev_report.get('crisis_correlations', {}).get('spike_multiplier') if prev_report else None
        spike = crisis_corr['spike_multiplier']
        if prev_spike is not None:
            delta = spike - prev_spike
            arrow = 'WORSE' if delta > 0 else 'BETTER' if delta < 0 else 'SAME'
            print(f"  Spike multiplier: {spike:.2f}x  (prev: {prev_spike:.2f}x, delta: {delta:+.2f}x {arrow})")
        else:
            print(f"  Spike multiplier: {spike:.2f}x")

        if spike > 2.0:
            print("  ** HIGH SPIKE: Portfolio correlations MORE THAN DOUBLE in crisis **")

    # --- Section 5: Liquidity ---
    print()
    print("-" * 80)
    print("5. LIQUIDITY CHECK (3mo avg daily volume)")
    print("-" * 80)
    print(f"  {'Ticker':<10} {'Shares':>10} {'AvgDailyVol':>12} {'DaysToLiq':>10} {'Risk':>6} {'Flag':>5}")
    print(f"  {'-'*10} {'-'*10} {'-'*12} {'-'*10} {'-'*6} {'-'*5}")
    flagged_count = 0
    for liq in liquidity:
        flag = '*' if liq['flagged'] else ''
        if liq['flagged']:
            flagged_count += 1
        dtl = f"{liq['days_to_liquidate']:.2f}" if liq['days_to_liquidate'] < 100 else ">100"
        print(f"  {liq['ticker']:<10} {liq['shares']:>10.2f} {liq['avg_daily_volume']:>12,} {dtl:>10} {liq['risk_level']:>6} {flag:>5}")

    print()
    if flagged_count > 0:
        print(f"  ** {flagged_count} position(s) flagged: liquidation > 0.5 days at avg volume **")
    else:
        print("  All positions can be liquidated within 0.5 days at average volume.")

    # --- Summary ---
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  Portfolio Weighted Beta:  {wb:.3f}")
    print(f"  GFC Scenario Drawdown:   {gfc['portfolio_drawdown']*100:.1f}%")
    if not quick_mode and mc_results:
        print(f"  Monte Carlo P5 (VaR95):  {mc_results['percentiles']['P5']*100:.1f}%")
        print(f"  Monte Carlo P1 (VaR99):  {mc_results['percentiles']['P1']*100:.1f}%")
        print(f"  P(loss >20%):            {mc_results['loss_probabilities']['loss_gt_20pct']*100:.1f}%")
        print(f"  P(loss >30%):            {mc_results['loss_probabilities']['loss_gt_30pct']*100:.1f}%")
    if 'error' not in crisis_corr:
        print(f"  Crisis Correlation Spike: {crisis_corr['spike_multiplier']:.2f}x")
    print(f"  Liquidity Flags:         {flagged_count}")
    print()
    print("[Raw data. Reason from principles.md]")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='Portfolio Stress Test')
    parser.add_argument('--quick', action='store_true', help='Skip Monte Carlo (faster)')
    parser.add_argument('--compare', type=str, metavar='YYYY-MM-DD',
                       help='Compare vs specific date report')
    args = parser.parse_args()

    print("Loading portfolio...")
    positions, short_positions, cash = load_portfolio()
    eurusd, gbpusd = get_fx_rates()
    position_list, total_value = build_position_list(positions, short_positions, eurusd, gbpusd)

    if not position_list:
        print("ERROR: No positions found in portfolio")
        sys.exit(1)

    print(f"  {len(position_list)} positions, total value ~${total_value:,.0f}")

    # Get all tickers
    tickers = [item['ticker'] for item in position_list]

    # Download returns
    print("\nDownloading market data...")
    returns = download_returns(tickers, period='1y')

    # --- 1. Betas ---
    print("\n[1/5] Calculating betas...")
    betas = calculate_betas(returns, position_list)

    # --- 2. Monte Carlo ---
    mc_results = None
    if not args.quick:
        print("[2/5] Running Monte Carlo (10K simulations)...")
        market_vol = float(returns['^GSPC'].std() * np.sqrt(252)) if '^GSPC' in returns.columns else 0.16
        mc_results = run_monte_carlo(betas, market_vol)
    else:
        print("[2/5] Monte Carlo SKIPPED (--quick)")

    # --- 3. GFC Scenario ---
    print("[3/5] Running 2008 GFC scenario...")
    gfc = gfc_scenario(betas, position_list)

    # --- 4. Crisis Correlations ---
    print("[4/5] Calculating crisis correlations...")
    crisis_corr = crisis_correlations(returns)

    # --- 5. Liquidity ---
    print("[5/5] Checking liquidity...")
    liquidity = liquidity_check(position_list)

    # --- Load previous report for comparison ---
    prev_report = load_previous_report(args.compare)
    if prev_report:
        print(f"\n  Loaded previous report: {prev_report.get('date', 'unknown')}")

    # --- Build and save report ---
    report = {
        'date': date.today().isoformat(),
        'positions_count': len(position_list),
        'total_value_usd': float(total_value),
        'portfolio_weighted_beta': float(portfolio_weighted_beta(betas)),
        'betas': {t: {k: v for k, v in info.items()} for t, info in betas.items()},
        'gfc_scenario': {
            'portfolio_drawdown': float(gfc['portfolio_drawdown']),
            'positions': gfc['positions'],
        },
        'crisis_correlations': crisis_corr,
        'liquidity': liquidity,
    }
    if mc_results:
        report['monte_carlo'] = mc_results

    filepath = save_report(report)
    print(f"\n  Report saved to: {filepath}")

    # --- Print formatted output ---
    print_results(betas, mc_results, gfc, crisis_corr, liquidity, prev_report, args.quick)


if __name__ == '__main__':
    main()

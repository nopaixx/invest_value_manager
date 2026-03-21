#!/usr/bin/env python3
"""
Portfolio NAV History -- Reconstructs daily portfolio value from inception to today.

Usage:
    python3 tools/portfolio_nav.py [--verbose] [--no-csv]

Reads:
    - portfolio/current.yaml (active positions + transactions)
    - portfolio/history.yaml (closed positions)

Outputs:
    - Summary metrics to terminal
    - Daily time series to reports/nav_history.csv

Compares portfolio performance vs S&P 500 (EUR-adjusted).
"""

import argparse
import os
import sys
import warnings
from datetime import datetime, timedelta
from collections import defaultdict

import numpy as np
import pandas as pd
import yaml
import yfinance as yf

warnings.filterwarnings('ignore')

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRENT_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
HISTORY_FILE = os.path.join(BASE_DIR, 'portfolio', 'history.yaml')
CSV_OUTPUT = os.path.join(BASE_DIR, 'reports', 'nav_history.csv')

# Import FX defaults
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from fx_defaults import FX_DEFAULTS
except ImportError:
    FX_DEFAULTS = {"EURUSD": 1.16, "GBPUSD": 1.34, "DKKEUR": 0.134, "CHFUSD": 1.10}

# Starting capital
STARTING_CAPITAL_EUR = 10000.0
INCEPTION_DATE = "2026-01-26"
RISK_FREE_RATE = 0.035  # 3.5% annualized


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def clean_num(val, default=0.0):
    """Parse a numeric value that may be prefixed with ~ or contain other chars."""
    if val is None:
        return default
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).replace('~', '').replace(',', '').strip()
    try:
        return float(s)
    except ValueError:
        return default


def parse_transactions(current_data):
    """Extract and normalize all transactions from current.yaml."""
    txns = []
    raw = current_data.get('transactions', [])
    if not raw:
        return txns

    for t in raw:
        date = str(t.get('date', ''))
        action = t.get('action', '').upper()
        ticker = t.get('ticker', '')
        shares = clean_num(t.get('shares', 0))

        # Determine EUR amount
        total_eur = None
        total_usd = None

        if 'total_eur' in t:
            total_eur = clean_num(t['total_eur'])
        if 'total_usd' in t:
            total_usd = clean_num(t['total_usd'])

        txns.append({
            'date': date,
            'action': action,
            'ticker': ticker,
            'shares': shares,
            'total_eur': total_eur,
            'total_usd': total_usd,
            'price_eur': t.get('price_eur'),
            'price_usd': t.get('price_usd'),
            'price_gbp': t.get('price_gbp'),
            'price_gbx': t.get('price_gbx'),
        })

    return txns


def estimate_eur_amount(txn, fx_eurusd=None):
    """Estimate EUR amount for a transaction."""
    if txn['total_eur'] is not None:
        return txn['total_eur']
    if txn['total_usd'] is not None:
        rate = fx_eurusd if fx_eurusd else FX_DEFAULTS['EURUSD']
        return txn['total_usd'] / rate
    # Fallback: estimate from price * shares
    if txn['price_eur']:
        return float(txn['price_eur']) * txn['shares']
    if txn['price_usd']:
        rate = fx_eurusd if fx_eurusd else FX_DEFAULTS['EURUSD']
        return float(txn['price_usd']) * txn['shares'] / rate
    if txn['price_gbp']:
        gbp_total = float(txn['price_gbp']) * txn['shares']
        return gbp_total * FX_DEFAULTS.get('GBPEUR', 1.15)
    if txn['price_gbx']:
        gbp_total = float(txn['price_gbx']) * txn['shares'] / 100.0
        return gbp_total * FX_DEFAULTS.get('GBPEUR', 1.15)
    return 0.0


def build_holdings_timeline(transactions):
    """Build dict: date -> [(ticker, share_delta, eur_amount, is_buy)]."""
    sorted_txns = sorted(transactions, key=lambda x: x['date'])
    changes = defaultdict(list)

    for txn in sorted_txns:
        date = txn['date']
        ticker = txn['ticker']
        action = txn['action']
        shares = txn['shares']
        eur_amt = estimate_eur_amount(txn)

        if action in ('BUY', 'ADD'):
            changes[date].append((ticker, shares, eur_amt, True))
        elif action in ('SELL', 'TRIM'):
            changes[date].append((ticker, -shares, eur_amt, False))
        elif action == 'SHORT':
            changes[date].append((ticker, -shares, eur_amt, True))  # SHORT: spend cash as margin

    return changes


def get_all_tickers(transactions, current_data):
    """Get all unique tickers that were ever held."""
    tickers = set()
    for txn in transactions:
        tickers.add(txn['ticker'])
    for pos in current_data.get('positions', []):
        tickers.add(pos['ticker'])
    for pos in current_data.get('short_positions', []):
        tickers.add(pos['ticker'])
    return tickers


def ticker_currency(ticker):
    """Determine expected currency from ticker suffix."""
    if ticker.endswith('.L'):
        return 'GBp'
    elif ticker.endswith('.PA') or ticker.endswith('.MI') or ticker.endswith('.AS') or ticker.endswith('.DE'):
        return 'EUR'
    elif ticker.endswith('.HE'):
        return 'EUR'
    elif ticker.endswith('.SW'):
        return 'CHF'
    else:
        return 'USD'


def fetch_historical_prices(tickers, start_date, end_date, verbose=False):
    """Fetch daily close prices for all tickers using yfinance batch download."""
    all_data = {}
    ticker_list = list(tickers)
    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

    if verbose:
        print(f"Fetching historical prices for {len(ticker_list)} tickers...")

    # Map tickers
    yf_tickers = [TICKER_MAP.get(t, t) for t in ticker_list]
    reverse_map = {TICKER_MAP.get(t, t): t for t in ticker_list}

    # Batch download
    try:
        data = yf.download(yf_tickers, start=start_date, end=end_date,
                           progress=False, auto_adjust=True, group_by='ticker')
        if data is not None and len(data) > 0:
            if len(yf_tickers) == 1:
                # Single ticker: columns are Price level only
                if isinstance(data.columns, pd.MultiIndex):
                    close = data['Close']
                    if isinstance(close, pd.DataFrame):
                        close = close.iloc[:, 0]
                else:
                    close = data['Close']
                orig = reverse_map.get(yf_tickers[0], yf_tickers[0])
                all_data[orig] = close.dropna()
                if verbose:
                    print(f"  {orig}: {len(all_data[orig])} days")
            else:
                for yf_t in yf_tickers:
                    orig = reverse_map.get(yf_t, yf_t)
                    try:
                        if yf_t in data.columns.get_level_values(0):
                            close = data[yf_t]['Close']
                        elif ('Close', yf_t) in data.columns:
                            close = data['Close'][yf_t]
                        else:
                            if verbose:
                                print(f"  {orig}: NOT IN DATA")
                            continue
                        close = close.dropna()
                        if len(close) > 0:
                            all_data[orig] = close
                            if verbose:
                                print(f"  {orig}: {len(close)} days")
                        else:
                            if verbose:
                                print(f"  {orig}: EMPTY")
                    except Exception as e:
                        if verbose:
                            print(f"  {orig}: ERROR extracting - {e}")
    except Exception as e:
        if verbose:
            print(f"  Batch download failed: {e}")

    # Fallback: individual download for missing tickers
    for t in ticker_list:
        if t not in all_data:
            yf_t = TICKER_MAP.get(t, t)
            try:
                d = yf.download(yf_t, start=start_date, end=end_date,
                                progress=False, auto_adjust=True)
                if d is not None and len(d) > 0:
                    if isinstance(d.columns, pd.MultiIndex):
                        close = d['Close']
                        if isinstance(close, pd.DataFrame):
                            close = close.iloc[:, 0]
                    else:
                        close = d['Close']
                    close = close.dropna()
                    if len(close) > 0:
                        all_data[t] = close
                        if verbose:
                            print(f"  {t} (fallback): {len(close)} days")
            except Exception as e:
                if verbose:
                    print(f"  {t} (fallback): ERROR - {e}")

    return all_data


def fetch_fx_history(start_date, end_date, verbose=False):
    """Fetch daily EUR/USD and GBP/USD rates."""
    fx_data = {}
    pairs = [('EURUSD', 'EURUSD=X'), ('GBPUSD', 'GBPUSD=X'),
             ('DKKUSD', 'DKKUSD=X'), ('CHFUSD', 'CHFUSD=X')]

    for pair, yf_ticker in pairs:
        try:
            data = yf.download(yf_ticker, start=start_date, end=end_date,
                               progress=False, auto_adjust=True)
            if data is not None and len(data) > 0:
                if isinstance(data.columns, pd.MultiIndex):
                    close = data['Close']
                    if isinstance(close, pd.DataFrame):
                        close = close.iloc[:, 0]
                else:
                    close = data['Close']
                fx_data[pair] = close.dropna()
                if verbose:
                    print(f"  FX {pair}: {len(fx_data[pair])} days")
        except Exception as e:
            if verbose:
                print(f"  FX {pair}: ERROR - {e}")

    return fx_data


def price_to_eur(price, ticker_ccy, eurusd, gbpusd, dkkusd=None, chfusd=None):
    """Convert a price in local currency to EUR."""
    if ticker_ccy == 'EUR':
        return price
    elif ticker_ccy == 'USD':
        return price / eurusd if eurusd else price / FX_DEFAULTS['EURUSD']
    elif ticker_ccy == 'GBp':
        gbp = price / 100.0
        usd = gbp * (gbpusd if gbpusd else FX_DEFAULTS['GBPUSD'])
        return usd / (eurusd if eurusd else FX_DEFAULTS['EURUSD'])
    elif ticker_ccy == 'GBP':
        usd = price * (gbpusd if gbpusd else FX_DEFAULTS['GBPUSD'])
        return usd / (eurusd if eurusd else FX_DEFAULTS['EURUSD'])
    elif ticker_ccy == 'DKK':
        if dkkusd:
            usd = price * dkkusd
            return usd / (eurusd if eurusd else FX_DEFAULTS['EURUSD'])
        return price * FX_DEFAULTS.get('DKKEUR', 0.134)
    elif ticker_ccy == 'CHF':
        if chfusd:
            usd = price * chfusd
            return usd / (eurusd if eurusd else FX_DEFAULTS['EURUSD'])
        return price * FX_DEFAULTS.get('CHFUSD', 1.10) / FX_DEFAULTS['EURUSD']
    return price / FX_DEFAULTS['EURUSD']


def reconstruct_nav(transactions, price_data, fx_data, start_date, end_date, verbose=False):
    """Reconstruct daily NAV from transactions and price data."""

    # Build trading date index from all available price data
    all_dates = set()
    for ticker, series in price_data.items():
        all_dates.update(series.index)
    if not all_dates:
        print("ERROR: No price data available.")
        return None

    date_index = sorted(all_dates)
    start_dt = pd.Timestamp(start_date)
    end_dt = pd.Timestamp(end_date)
    date_index = [d for d in date_index if start_dt <= d <= end_dt]

    if not date_index:
        print("ERROR: No trading dates in range.")
        return None

    # Build changes timeline
    changes = build_holdings_timeline(transactions)

    # Forward-fill price data
    price_df = pd.DataFrame(index=date_index)
    for ticker, series in price_data.items():
        price_df[ticker] = series.reindex(date_index).ffill()

    # Forward-fill FX data
    def align_fx(key, default):
        s = fx_data.get(key, pd.Series(dtype=float))
        aligned = s.reindex(date_index).ffill().bfill()
        return aligned.fillna(default)

    eurusd_df = align_fx('EURUSD', FX_DEFAULTS['EURUSD'])
    gbpusd_df = align_fx('GBPUSD', FX_DEFAULTS['GBPUSD'])
    dkkusd_df = align_fx('DKKUSD', 0.145)
    chfusd_df = align_fx('CHFUSD', FX_DEFAULTS.get('CHFUSD', 1.10))

    # Simulate day by day
    holdings = defaultdict(float)  # ticker -> shares (positive=long, negative=short)
    cash_eur = STARTING_CAPITAL_EUR

    nav_records = []

    for dt in date_index:
        date_str = dt.strftime('%Y-%m-%d')

        # Apply transactions for this date
        if date_str in changes:
            for (ticker, share_delta, eur_amt, is_buy) in changes[date_str]:
                if is_buy:
                    holdings[ticker] += share_delta
                    cash_eur -= eur_amt
                else:
                    # SELL/TRIM: shares come out, cash comes in
                    holdings[ticker] += share_delta  # share_delta is negative
                    cash_eur += eur_amt
                    if abs(holdings[ticker]) < 0.001:
                        holdings[ticker] = 0.0

        # Get FX rates for this day
        eurusd = eurusd_df.get(dt, FX_DEFAULTS['EURUSD'])
        gbpusd = gbpusd_df.get(dt, FX_DEFAULTS['GBPUSD'])
        dkkusd = dkkusd_df.get(dt, None)
        chfusd = chfusd_df.get(dt, None)

        if pd.isna(eurusd):
            eurusd = FX_DEFAULTS['EURUSD']
        if pd.isna(gbpusd):
            gbpusd = FX_DEFAULTS['GBPUSD']

        # Calculate positions value in EUR
        long_value_eur = 0.0
        short_liability_eur = 0.0

        for ticker, shares in holdings.items():
            if abs(shares) < 0.0001:
                continue
            if ticker not in price_df.columns:
                continue
            price = price_df.loc[dt, ticker]
            if pd.isna(price):
                continue

            ccy = ticker_currency(ticker)
            val_eur = price_to_eur(price, ccy, eurusd, gbpusd, dkkusd, chfusd) * abs(shares)

            if shares > 0:
                long_value_eur += val_eur
            else:
                # Short: liability = current market value of shorted shares
                short_liability_eur += val_eur

        # NAV = cash + long positions - short liabilities
        # (cash already includes proceeds from short sales)
        total_nav = cash_eur + long_value_eur - short_liability_eur

        nav_records.append({
            'date': dt,
            'portfolio_eur': total_nav,
            'cash_eur': cash_eur,
            'long_value_eur': long_value_eur,
            'short_liability_eur': short_liability_eur,
        })

    return pd.DataFrame(nav_records).set_index('date')


def fetch_sp500_eur(date_index, fx_data, verbose=False):
    """Fetch S&P 500 daily closes converted to EUR."""
    start = date_index[0] - timedelta(days=5)
    end = date_index[-1] + timedelta(days=1)

    try:
        sp = yf.download('^GSPC', start=start.strftime('%Y-%m-%d'),
                         end=end.strftime('%Y-%m-%d'), progress=False, auto_adjust=True)
        if sp is not None and len(sp) > 0:
            if isinstance(sp.columns, pd.MultiIndex):
                close = sp['Close']
                if isinstance(close, pd.DataFrame):
                    close = close.iloc[:, 0]
            else:
                close = sp['Close']

            eurusd_series = fx_data.get('EURUSD', pd.Series(dtype=float))
            eurusd_aligned = eurusd_series.reindex(close.index).ffill().bfill()
            # Fill any remaining NaN with default
            eurusd_aligned = eurusd_aligned.fillna(FX_DEFAULTS['EURUSD'])

            sp_eur = close / eurusd_aligned
            sp_eur = sp_eur.reindex(date_index).ffill()
            return sp_eur
    except Exception as e:
        if verbose:
            print(f"  S&P 500 fetch error: {e}")
    return None


def calculate_metrics(nav_df, sp500_eur, verbose=False):
    """Calculate performance metrics."""
    metrics = {}

    port_start = nav_df['portfolio_eur'].iloc[0]
    port_end = nav_df['portfolio_eur'].iloc[-1]
    metrics['port_start'] = port_start
    metrics['port_end'] = port_end
    metrics['port_return_pct'] = (port_end / port_start - 1) * 100

    nav_df['port_daily_return'] = nav_df['portfolio_eur'].pct_change()

    trading_days = len(nav_df)
    metrics['trading_days'] = trading_days

    daily_vol = nav_df['port_daily_return'].dropna().std()
    metrics['port_volatility_ann'] = daily_vol * np.sqrt(252) * 100

    daily_rf = RISK_FREE_RATE / 252
    excess_returns = nav_df['port_daily_return'].dropna() - daily_rf
    if daily_vol > 0:
        metrics['sharpe_ratio'] = (excess_returns.mean() / daily_vol) * np.sqrt(252)
    else:
        metrics['sharpe_ratio'] = 0.0

    # Max drawdown
    cummax = nav_df['portfolio_eur'].cummax()
    drawdown = (nav_df['portfolio_eur'] - cummax) / cummax
    metrics['max_drawdown_pct'] = drawdown.min() * 100
    dd_idx = drawdown.idxmin()
    metrics['max_drawdown_date'] = dd_idx.strftime('%Y-%m-%d') if pd.notna(dd_idx) else 'N/A'

    # S&P 500 metrics
    if sp500_eur is not None and len(sp500_eur.dropna()) > 1:
        sp_clean = sp500_eur.dropna()
        sp_start = sp_clean.iloc[0]
        sp_end = sp_clean.iloc[-1]
        metrics['sp_return_pct'] = (sp_end / sp_start - 1) * 100
        metrics['alpha_pp'] = metrics['port_return_pct'] - metrics['sp_return_pct']

        sp_daily = sp500_eur.pct_change().dropna()
        sp_vol = sp_daily.std()
        metrics['sp_volatility_ann'] = sp_vol * np.sqrt(252) * 100

        sp_cummax = sp500_eur.cummax()
        sp_dd = (sp500_eur - sp_cummax) / sp_cummax
        metrics['sp_max_drawdown_pct'] = sp_dd.min() * 100
        sp_dd_idx = sp_dd.idxmin()
        metrics['sp_max_drawdown_date'] = sp_dd_idx.strftime('%Y-%m-%d') if pd.notna(sp_dd_idx) else 'N/A'

        # Beta and tracking error
        aligned = pd.DataFrame({
            'port': nav_df['port_daily_return'],
            'sp': sp_daily
        }).dropna()

        if len(aligned) > 5:
            cov = np.cov(aligned['port'], aligned['sp'])
            metrics['beta'] = cov[0, 1] / cov[1, 1] if cov[1, 1] > 0 else 0.0

            tracking_diff = aligned['port'] - aligned['sp']
            metrics['tracking_error'] = tracking_diff.std() * np.sqrt(252) * 100

            if metrics['tracking_error'] > 0:
                metrics['information_ratio'] = (metrics['port_return_pct'] - metrics['sp_return_pct']) / metrics['tracking_error']
            else:
                metrics['information_ratio'] = 0.0
        else:
            metrics['beta'] = 'N/A'
            metrics['tracking_error'] = 'N/A'
            metrics['information_ratio'] = 'N/A'
    else:
        for k in ['sp_return_pct', 'alpha_pp', 'sp_max_drawdown_pct', 'sp_max_drawdown_date',
                   'beta', 'tracking_error', 'information_ratio', 'sp_volatility_ann']:
            metrics[k] = 'N/A'

    return metrics


def save_csv(nav_df, sp500_eur, output_path):
    """Save daily NAV time series to CSV."""
    df = nav_df[['portfolio_eur', 'cash_eur']].copy()

    if sp500_eur is not None:
        df['sp500_eur'] = sp500_eur

    df['portfolio_return_pct'] = df['portfolio_eur'].pct_change() * 100
    if 'sp500_eur' in df.columns:
        df['sp500_return_pct'] = df['sp500_eur'].pct_change() * 100

    df.index.name = 'date'
    df.to_csv(output_path, float_format='%.2f')


def fmt(val, suffix='', decimals=1, plus=False):
    """Format a metric value, handling N/A."""
    if val == 'N/A' or val is None:
        return 'N/A'
    fmt_str = f"{{:{'+' if plus else ''}.{decimals}f}}"
    return fmt_str.format(val) + suffix


def print_summary(metrics, start_date, end_date):
    """Print formatted summary to terminal."""
    print()
    print(f"PORTFOLIO NAV HISTORY -- {start_date} to {end_date}")
    print("=" * 56)
    print(f"Start:  EUR {metrics['port_start']:,.2f}  |  Current: EUR {metrics['port_end']:,.2f}")
    print(f"Portfolio return:    {fmt(metrics['port_return_pct'], '%', plus=True)}")
    print(f"S&P 500 return:      {fmt(metrics.get('sp_return_pct'), '% (EUR-adjusted)', plus=True)}")
    print(f"Alpha:               {fmt(metrics.get('alpha_pp'), 'pp', plus=True)}")
    print(f"Sharpe ratio:        {fmt(metrics['sharpe_ratio'], decimals=2)}")
    print(f"Max drawdown:        {fmt(metrics['max_drawdown_pct'], '%')} ({metrics['max_drawdown_date']})")
    if isinstance(metrics.get('sp_max_drawdown_pct'), (int, float)):
        print(f"S&P max drawdown:    {fmt(metrics['sp_max_drawdown_pct'], '%')} ({metrics['sp_max_drawdown_date']})")
    print(f"Beta vs S&P:         {fmt(metrics.get('beta'), decimals=2)}")
    print(f"Volatility (ann.):   {fmt(metrics['port_volatility_ann'], '%')}")
    if isinstance(metrics.get('sp_volatility_ann'), (int, float)):
        print(f"S&P volatility:      {fmt(metrics['sp_volatility_ann'], '%')}")
    if isinstance(metrics.get('tracking_error'), (int, float)):
        print(f"Tracking error:      {fmt(metrics['tracking_error'], '%')}")
    if isinstance(metrics.get('information_ratio'), (int, float)):
        print(f"Information ratio:   {fmt(metrics['information_ratio'], decimals=2)}")
    print(f"Trading days:        {metrics['trading_days']}")
    print()


def main():
    parser = argparse.ArgumentParser(description='Portfolio NAV History')
    parser.add_argument('--verbose', action='store_true', help='Show detailed progress')
    parser.add_argument('--no-csv', action='store_true', help='Skip CSV output')
    args = parser.parse_args()

    if args.verbose:
        print("Loading portfolio data...")

    current_data = load_yaml(CURRENT_FILE)
    try:
        history_data = load_yaml(HISTORY_FILE)
    except Exception:
        history_data = {}

    transactions = parse_transactions(current_data)
    if not transactions:
        print("ERROR: No transactions found in current.yaml")
        sys.exit(1)

    if args.verbose:
        print(f"Found {len(transactions)} transactions")

    start_date = INCEPTION_DATE
    end_date = datetime.now().strftime('%Y-%m-%d')

    all_tickers = get_all_tickers(transactions, current_data)
    if args.verbose:
        print(f"Tickers to fetch: {sorted(all_tickers)}")

    print("Fetching historical price data...")
    price_data = fetch_historical_prices(all_tickers, start_date, end_date, verbose=args.verbose)
    fx_data = fetch_fx_history(start_date, end_date, verbose=args.verbose)

    if not price_data:
        print("ERROR: Could not fetch any price data.")
        sys.exit(1)

    if args.verbose:
        print("Reconstructing daily NAV...")

    nav_df = reconstruct_nav(transactions, price_data, fx_data, start_date, end_date, verbose=args.verbose)

    if nav_df is None or len(nav_df) == 0:
        print("ERROR: Could not reconstruct NAV.")
        sys.exit(1)

    sp500_eur = fetch_sp500_eur(nav_df.index, fx_data, verbose=args.verbose)

    metrics = calculate_metrics(nav_df, sp500_eur, verbose=args.verbose)

    print_summary(metrics, start_date, end_date)

    if not args.no_csv:
        os.makedirs(os.path.dirname(CSV_OUTPUT), exist_ok=True)
        save_csv(nav_df, sp500_eur, CSV_OUTPUT)
        print(f"CSV saved to {CSV_OUTPUT}")


if __name__ == '__main__':
    main()

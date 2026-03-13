#!/usr/bin/env python3
"""
Canonical thesis file parser — Single Source of Truth.

ALL tools that parse thesis files import from here.
Never duplicate these functions — fix them here, fixed everywhere.

Consumers: forward_return.py, portfolio_cagr.py, effectiveness_tracker.py
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THESIS_ACTIVE_DIR = os.path.join(BASE_DIR, 'thesis', 'active')
THESIS_RESEARCH_DIR = os.path.join(BASE_DIR, 'thesis', 'research')
THESIS_SHORT_DIR = os.path.join(BASE_DIR, 'thesis', 'short', 'active')


# ---------------------------------------------------------------------------
# Thesis file I/O
# ---------------------------------------------------------------------------

def find_thesis_path(ticker):
    """Find thesis.md for a ticker across active/research/short dirs.
    Returns relative path from BASE_DIR, or None."""
    for subdir in ('thesis/active', 'thesis/research', 'thesis/short/active'):
        path = os.path.join(BASE_DIR, subdir, ticker, 'thesis.md')
        if os.path.exists(path):
            return os.path.join(subdir, ticker, 'thesis.md')
    return None


def read_thesis(thesis_path):
    """Read thesis file content. thesis_path is relative to BASE_DIR.
    Returns file content string or None."""
    if not thesis_path:
        return None
    full_path = os.path.join(BASE_DIR, thesis_path)
    if not os.path.exists(full_path):
        return None
    try:
        with open(full_path, 'r') as f:
            return f.read()
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Currency detection (multi-layer context analysis)
# ---------------------------------------------------------------------------

def _detect_currency_from_context(thesis_content, match_obj):
    """Detect the FV currency from the match and surrounding text.
    Returns detected currency string or None."""
    match_text = match_obj.group(0)
    for label, curr in [('EUR', 'EUR'), ('DKK', 'DKK'), ('SEK', 'SEK'),
                        ('$', 'USD'), ('GBp', 'GBp'), ('gbp', 'GBp'), ('GBP', 'GBP')]:
        if label in match_text:
            return curr
    if match_text.rstrip().endswith('p') and not match_text.rstrip().endswith('pp'):
        return 'GBp'

    after_match = thesis_content[match_obj.end():match_obj.end() + 20]
    if re.match(r'\s*SEK\b', after_match):
        return 'SEK'
    if re.match(r'\s*DKK\b', after_match):
        return 'DKK'
    if re.match(r'\s*EUR\b', after_match):
        return 'EUR'
    if re.match(r'\s*GBp\b', after_match, re.IGNORECASE):
        return 'GBp'
    if re.match(r'\s*USD\b', after_match):
        return 'USD'
    if re.match(r'p\b', after_match):
        return 'GBp'

    before_match = thesis_content[max(0, match_obj.start() - 20):match_obj.start()]
    if 'SEK' in before_match:
        return 'SEK'
    if 'DKK' in before_match:
        return 'DKK'
    if '$' in before_match:
        return 'USD'
    if 'EUR' in before_match:
        return 'EUR'

    nearby_start = max(0, match_obj.start() - 100)
    nearby_end = min(len(thesis_content), match_obj.end() + 100)
    nearby = thesis_content[nearby_start:nearby_end]
    for label, curr in [('SEK', 'SEK'), ('DKK', 'DKK'), ('GBp', 'GBp'),
                        ('EUR', 'EUR'), ('$', 'USD')]:
        if label in nearby:
            return curr

    return None


# ---------------------------------------------------------------------------
# Fair Value extraction (22 patterns, most specific first)
# ---------------------------------------------------------------------------

def extract_fair_value(thesis_content, ticker, currency='USD'):
    """Extract fair value from thesis file using multiple patterns.
    Returns (fair_value_in_native_currency, currency_of_fv) or (None, None)."""
    if not thesis_content:
        return None, None

    fv = None
    fv_currency = currency

    bold = r'\*{0,2}'
    curr_prefix = r'(?:\$|EUR\s*|GBP\s*|DKK\s*|SEK\s*)?'
    curr_suffix = r'(?:p|GBp)?'

    patterns = [
        (r'^>?\s*\*\*Fair Value:\*\*\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        (r'\*\*Weighted\s+(?:Avg|Average|FV|Fair Value)\*\*\s*\|[^|]*\|[^|]*\|\s*\*\*\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix + r'\s*\*\*', 'single'),
        (r'\*\*Blended Fair Value\*\*\s*\|[^|]*\|[^|]*\|\s*\*\*\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix + r'\s*\*\*', 'single'),
        (r'Weighted Fair Value[:\s]+' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        (r'Fair Value Consolidado:\s*(?:EUR|USD|\$|GBP|DKK)\s*([0-9,]+(?:\.\d+)?)\s*-\s*([0-9,]+(?:\.\d+)?)', 'range'),
        (bold + r'Blended (?:Base )?Fair Value' + bold + r'[:\s]+' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        (r'Fair Value \(Weighted\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        (r'Fair Value Base \(Weighted\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        (r'Fair Value\s*\((?:v\d+\.?\d*\s*)?Base\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        (r'Fair Value Expected[^:]*:\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        (r'Fair Value Base\s*\|\s*' + curr_prefix + r'[0-9,]+(?:\.\d+)?\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        (r'Fair Value Base\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        (r'Blended Fair Value\s*\(v\d+\.?\d*\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        (r'Conservative Fair Value Range:\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*-\s*([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'range'),
        (r'(?:Base Case FV|FV Base|FV Expected)[:\s]+~?\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        (r'OEY Fair Value[:\s]+~?\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        (r'Fair Value v\d+\.?\d*:\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*-\s*([0-9,]+(?:\.\d+)?)', 'range'),
        (bold + r'Fair Value' + bold + r'[:\s]+' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
    ]

    for pat, pat_type in patterns:
        m = re.search(pat, thesis_content, re.IGNORECASE | re.MULTILINE)
        if m:
            groups = m.groups()
            if pat_type == 'range' and len(groups) >= 2:
                try:
                    v1 = float(groups[0].replace(',', ''))
                    v2 = float(groups[1].replace(',', ''))
                    fv = (v1 + v2) / 2
                except (ValueError, TypeError):
                    continue
            else:
                try:
                    fv = float(groups[0].replace(',', ''))
                except (ValueError, TypeError):
                    continue

            if fv <= 0:
                fv = None
                continue

            detected = _detect_currency_from_context(thesis_content, m)
            if detected:
                fv_currency = detected
            break

    return fv, fv_currency


# ---------------------------------------------------------------------------
# Growth rate extraction (11 patterns)
# ---------------------------------------------------------------------------

def extract_growth_rate(thesis_content, ticker):
    """Extract expected growth rate from thesis.
    Returns growth as a decimal (e.g., 0.08 for 8%), or None."""
    if not thesis_content:
        return None

    patterns = [
        (r'\*{0,2}Expected Growth\*{0,2}[^:\n]*:\*{0,2}\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth Base:\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%', 'range'),
        (r'GP Growth[^:]*:\s*(?:~)?(\d+(?:\.\d+)?)\s*%\s*\(base', 'single'),
        (r'=\s*~?(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%\s*GP growth', 'range'),
        (r'GP CAGR[):\s]+(?:~)?(\d+(?:\.\d+)?)\s*%\s*\(base', 'single'),
        (r'Expected Growth \(GP CAGR\):\s*(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'(?<!Terminal )(?:Expected )?Growth:\s*(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth\s*=.*?(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%', 'range'),
        (r'growth of\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'~?(\d+(?:\.\d+)?)\s*%\s*CAGR\s*\((?:normalized|base)', 'single'),
    ]

    for pat, pat_type in patterns:
        m = re.search(pat, thesis_content, re.IGNORECASE)
        if m:
            groups = m.groups()
            if pat_type == 'range' and len(groups) >= 2:
                try:
                    g1 = float(groups[0])
                    g2 = float(groups[1])
                    growth = (g1 + g2) / 2 / 100
                    if -0.50 <= growth <= 0.50:
                        return growth
                except (ValueError, TypeError):
                    continue
            else:
                try:
                    growth = float(groups[0]) / 100
                    if -0.50 <= growth <= 0.50:
                        return growth
                except (ValueError, TypeError):
                    continue

    return None


# ---------------------------------------------------------------------------
# Dividend yield extraction (from thesis — yfinance preferred in consumers)
# ---------------------------------------------------------------------------

def extract_dividend_yield(thesis_content, ticker):
    """Extract dividend yield from thesis. Returns decimal or None.
    Note: Most consumers use yfinance dividendYield instead."""
    if not thesis_content:
        return None

    patterns = [
        r'Dividend Yield[:\s]+(?:~)?(\d+(?:\.\d+)?)\s*%',
        r'Yield[:\s]+(?:~)?(\d+(?:\.\d+)?)\s*%',
        r'dividend\s+yield\s+of\s+(?:~)?(\d+(?:\.\d+)?)\s*%',
    ]

    for pat in patterns:
        m = re.search(pat, thesis_content, re.IGNORECASE)
        if m:
            try:
                dy = float(m.group(1)) / 100
                if 0 <= dy <= 0.20:
                    return dy
            except (ValueError, TypeError):
                continue
    return None


# ---------------------------------------------------------------------------
# Portfolio YAML FV parser
# ---------------------------------------------------------------------------

def parse_portfolio_fv(fv_string):
    """Parse fair_value field from portfolio/current.yaml.
    Returns (value, currency) or (None, None).

    Examples:
        "$191 (v3.0...)" -> (191.0, 'USD')
        "EUR 35.00 (v3.1...)" -> (35.0, 'EUR')
        "240 GBp (v3.0...)" -> (240.0, 'GBp')
    """
    if not fv_string:
        return None, None
    for pat, curr in [
        (r'\$\s*([0-9,]+(?:\.\d+)?)', 'USD'),
        (r'EUR\s+([0-9,]+(?:\.\d+)?)', 'EUR'),
        (r'([0-9,]+(?:\.\d+)?)\s*GBp', 'GBp'),
        (r'([0-9,]+(?:\.\d+)?)\s*DKK', 'DKK'),
        (r'([0-9,]+(?:\.\d+)?)\s*SEK', 'SEK'),
    ]:
        m = re.match(pat, fv_string)
        if m:
            return float(m.group(1).replace(',', '')), curr
    return None, None


# ---------------------------------------------------------------------------
# E[CAGR] computation
# ---------------------------------------------------------------------------

def compute_ecagr(fv, price, growth_pct, yield_pct):
    """Compute E[CAGR] = (FV/Price)^(1/3) - 1 + growth + div_yield.

    Args:
        fv: Fair value in same currency as price
        price: Current market price
        growth_pct: Expected growth rate as PERCENTAGE (e.g., 8.0 for 8%)
        yield_pct: Dividend yield as PERCENTAGE (e.g., 2.5 for 2.5%)

    Returns:
        E[CAGR] as percentage (e.g., 14.5 for 14.5%), or None if inputs invalid.
    """
    if not fv or not price or price <= 0 or fv <= 0:
        return None
    mos = (fv / price) ** (1.0 / 3.0) - 1.0
    return round((mos + (growth_pct or 0) / 100.0 + (yield_pct or 0) / 100.0) * 100.0, 1)


# ---------------------------------------------------------------------------
# FX conversion utilities
# ---------------------------------------------------------------------------

def convert_fv_to_price_currency(fv, fv_currency, stock_currency, eurusd, gbpeur, dkkeur):
    """Convert fair value to the stock's trading currency for MoS calculation."""
    if fv_currency == stock_currency:
        return fv

    # Convert to EUR first
    fv_eur = fv
    if fv_currency == 'USD':
        fv_eur = fv / eurusd
    elif fv_currency in ('GBp', 'GBX'):
        fv_eur = (fv / 100) * gbpeur
    elif fv_currency == 'GBP':
        fv_eur = fv * gbpeur
    elif fv_currency == 'DKK':
        fv_eur = fv * dkkeur
    elif fv_currency == 'SEK':
        fv_eur = fv * 0.088

    # Convert from EUR to target
    if stock_currency == 'EUR':
        return fv_eur
    elif stock_currency == 'USD':
        return fv_eur * eurusd
    elif stock_currency in ('GBp', 'GBX'):
        return (fv_eur / gbpeur) * 100
    elif stock_currency == 'GBP':
        return fv_eur / gbpeur
    elif stock_currency == 'DKK':
        return fv_eur / dkkeur if dkkeur else fv_eur
    elif stock_currency == 'SEK':
        return fv_eur / 0.088
    return fv_eur

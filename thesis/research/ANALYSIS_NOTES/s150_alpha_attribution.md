# S150 Alpha Attribution & Stress Test (2026-03-08)

## Portfolio Performance (Feb 2 - Mar 8, 34 days)

| Benchmark | Return | Alpha |
|-----------|--------|-------|
| Portfolio | +0.5% | -- |
| S&P 500 | -3.4% | **+3.9pp** |
| MSCI World | -3.0% | **+3.5pp** |

## Market Context (34 days)

- Oil (WTI): $62 -> $91 (+46.3%)
- VIX: 16.3 -> 29.5 (+81%)
- DXY: 97.6 -> 98.9 (+1.3%)
- S&P 500: -3.3%, Nasdaq: -4.2%, UK: -1.1%, Germany: -6.1%
- Energy: +13.0%, Tech: -5.5%, Financials: -6.4%, Healthcare: -1.9%

## Position-Level Attribution

| Ticker | Weight | Return | Contribution | Geography |
|--------|--------|--------|-------------|-----------|
| ADBE | 8.9% | +7.1% | +0.64pp | US |
| EDEN.PA | 18.4% | +2.4% | +0.44pp | EU |
| FTNT | 7.2% | +2.6% | +0.18pp | US |
| DOCS | 8.3% | +2.1% | +0.17pp | US |
| HLNE | 10.4% | +0.9% | +0.10pp | US |
| MONY.L | 7.3% | +1.1% | +0.08pp | UK |
| TW | 5.7% | +0.0% | +0.00pp | US |
| WKL.AS | 7.6% | +0.0% | +0.00pp | EU |
| IHP.L | 11.4% | -0.3% | -0.04pp | UK |
| NVO | 11.4% | -5.4% | -0.61pp | US |

**Geography breakdown:** US +0.48pp, EU +0.44pp, UK +0.04pp

## Alpha Decomposition

| Factor | Contribution | Explanation |
|--------|-------------|-------------|
| Quality selection | +2.0pp | QS 72-86 companies fell LESS than market. ADBE +7.1%, FTNT +2.6% while tech sector -5.5% |
| Geographic diversification | +1.0pp | UK (-1.1%) outperformed US (-3.3%). 25.7% UK allocation was protective |
| Sector mix | +0.5pp | 0% energy/materials miss. But no financials (-6.4%) exposure either. Info services + healthcare = defensive-growth |
| Entry timing (buying at 52wL) | +0.4pp | Bought near 52-week lows for most positions. Built-in cushion from drawdown entry |

**Main detractor:** NVO -5.4% = -0.61pp (CagriSema failure + GLP-1 competition)

## How to Replicate

1. Quality in drawdown (fallen_angels.py formalizes this)
2. Geographic diversification (20-30% UK/EU)
3. Avoid hype sectors (0% AI pure-play, 0% crypto)
4. NOT fully replicable as formula — timing component has luck

## Hormuz Oil Stress Test ($120 Oil)

| Position | Weight | $120 Oil Impact | Reasoning |
|----------|--------|-----------------|-----------|
| EDEN.PA | 18.4% | -10 to -15% | France consumer exposure, 21.2% SI amplifies |
| NVO | 11.4% | -3 to -5% | Pharma defensive, but GLP-1 discretionary |
| ADBE | 8.9% | -5 to -8% | Tech selloff, but 95%+ recurring mitigates |
| MONY.L | 7.3% | -5 to -8% | UK consumer, partially counter-cyclical |
| IHP.L | 11.4% | -5 to -8% | FUA mechanically drops with FTSE |
| HLNE | 10.4% | -8 to -12% | PE exits/fundraising freeze |
| DOCS | 8.3% | -2 to -3% | Minimal oil sensitivity |
| FTNT | 7.2% | +5 to +10% | CRISIS BENEFICIARY — cyber threats escalate |
| TW | 5.7% | +3 to +5% | Trading volumes EXPLODE in crisis |
| WKL.AS | 7.6% | 0 to -2% | Immune — CPAs, hospitals, compliance |

### Portfolio-Level Scenarios

| Scenario | Impact | Reasoning |
|----------|--------|-----------|
| Base ($120 oil, 2-4 weeks) | -5 to -7% | EDEN drags most. FTNT+TW offset partially |
| Extended ($120 oil, 3+ months) | -10 to -15% | UK recession fears hit IHP+MONY. PE freeze hits HLNE |
| Nuclear ($150 oil, recession) | -20 to -25% | Everything except FTNT, WKL.AS sells off |

**Key vulnerability:** EDEN.PA at 18.4% with 21.2% SI = largest single risk factor
**Natural hedges:** FTNT + TW + WKL.AS = 20.5% protected/benefited

---

*Analysis: 2026-03-08 (S150). For portfolio decision reference.*

# BZU.MI SELL — Execution Plan | Monday March 16, 2026

## Trade Details

| Field | Value |
|-------|-------|
| **Action** | SELL |
| **Ticker** | BZU.MI (Buzzi SpA) |
| **Exchange** | BIT (Borsa Italiana) |
| **Shares** | 8.81 |
| **Order type** | MARKET |
| **Expected price** | ~EUR 42.16 (Friday close) |
| **Expected proceeds** | ~EUR 371 |
| **Timing** | BIT open 09:00 CET. Execute at market open. |

## Why MARKET Order (Not Limit)

- BZU.MI avg daily volume: 519K shares (~EUR 22M/day). Our 8.81 shares = 0.002% of daily volume. ZERO market impact.
- Limit order risks: if we set limit at EUR 42 and stock opens at EUR 41.80, we miss by EUR 0.20 and remain exposed to oil crisis another day. Not worth EUR 1.76 of potential saving.
- The goal is EXIT, not price optimization. Every hour holding an energy-intensive cyclical in an oil crisis is risk.

## Pre-Execution Checklist

- [x] "Would I buy BZU.MI from zero today?" → NO (oil $99, Hormuz closed, KC#6, worst E[CAGR])
- [x] Macro regime check → NORMAL (S&P 20d: -2.9%). No crisis freeze.
- [x] Gate 7 macro check → Oil has changed materially since R4 (Feb 7 at $85 → now $99)
- [x] KCs: KC#1 MONITORING, KC#6 MONITORING (Brent >$95 sustained)
- [x] Conviction: LOW (#11 of 11)
- [x] E[CAGR]: 11.2% (worst non-FTNT)
- [x] No earnings pre-sell

## Post-Execution

1. Confirm fill price + shares in eToro
2. Update portfolio/current.yaml: remove BZU.MI from positions
3. Update state/system.yaml: remove BZU.MI from positions list
4. Record in portfolio/history.yaml: entry EUR 42.00 (Mar 13), exit EUR ~42 (Mar 16), P&L ~0%
5. Cash increases to ~EUR 371
6. Portfolio: 10 long + 1 short, cash EUR 371 (3.6%)

## Contingency

- **If BIT is closed Monday** (unlikely, no Italian holiday): defer to Tuesday BEFORE FOMC (2 PM ET = 8 PM CET). BIT closes 5:30 PM CET → can sell before FOMC.
- **If BZU.MI gaps down >5% at open** (oil spike weekend): SELL anyway. The thesis for selling is structural, not price-dependent.
- **If BZU.MI gaps up >5%** (oil deal weekend): Still SELL. Better price = more proceeds, but decision unchanged.

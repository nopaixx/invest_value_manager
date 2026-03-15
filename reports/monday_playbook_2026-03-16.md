# Monday Playbook — March 16, 2026

> **CONTEXT:** US-Israel struck Kharg Island (Iran oil hub) Mar 14. Brent spiked to $150+. War Day 15+. FOMC Tuesday. This is the most volatile week since portfolio inception.

---

## Pre-Market (07:00-09:00 CET)

| Time | Action |
|------|--------|
| 07:00 | Check oil futures (Brent/WTI). If Brent >$130 → expect S&P -3%+ at open. |
| 07:30 | Check EUR/USD, GBP/USD. Crisis = USD strengthens (flight to safety). |
| 08:00 | Check Asian markets (Nikkei, Hang Seng). They open before EU — leading indicator. |
| 08:30 | Run `macro_fragility.py world` for fresh data. Verify oil price vs weekend spike. |
| 08:45 | Pre-BIT open: confirm BZU.MI sell order ready in eToro. |

## BIT Open (09:00 CET) — CRITICAL

**SELL BZU.MI 8.81 shares at MARKET. Do NOT use limit order.**

- Expected price: EUR 38-45 range (volatile, depends on oil open)
- If BZU.MI gaps DOWN -10%+ (EUR 38): SELL anyway. Thesis for selling is structural.
- If BZU.MI gaps UP +5% (EUR 44): SELL anyway. Better price = more proceeds.
- Post-sell: confirm in eToro, note exact price and shares.
- Cash: ~EUR 340-390 depending on fill.

## Post-BZU.MI (09:15-14:30 CET)

| Action | Details |
|--------|---------|
| Run `portfolio_stats.py` | Confirm BZU.MI removed, cash updated, regime check |
| Monitor UK positions | IHP.L, MONY.L — check if LSE reacting to Iran (UK defense benefits, consumer hurts) |
| Monitor EU positions | EDEN.PA, WKL.AS — check EUR/USD impact |
| **DO NOT BUY ANYTHING** | Cash EUR ~370 = dry powder for post-FOMC deployment |
| **DO NOT ADD to CVNA short** | Thesis strengthened but sizing discipline = EUR 93 max |
| **DO NOT change Mar 26 plan** | GDDY is oil-immune. DNLM.L reduced to EUR 200. Plan holds. |

## NYSE Pre-Market (14:00 CET) / Open (15:30 CET)

| Action | Details |
|--------|---------|
| Check S&P futures | If -3%+ → run regime detector. If 20d decline crosses -10% → WARNING. |
| Check CVNA price | Should be DOWN (oil spike = bearish for used car demand) |
| Check FTNT price | May be UP (cybersecurity = crisis beneficiary) |
| Check HLNE price | Most sensitive (beta 1.49). If below $90 → near 52wL watch |
| Check TW price | Should BENEFIT (vol spike → record trading volumes) |
| Run `kc_monitor.py --compact` | Verify no KCs triggered by price moves |
| Run `forward_return.py --active-only` | See how E[CAGR] changes with new prices |

## What NOT To Do Monday

1. **DO NOT panic sell any position.** The portfolio is 96.4% oil-immune post-BZU.MI.
2. **DO NOT buy anything.** FOMC Tuesday = binary event. Wait.
3. **DO NOT increase CVNA short.** Committee approved EUR 100. Discipline.
4. **DO NOT change stop losses.** CVNA stop $370 has 23% buffer. Adequate.
5. **DO NOT make FOMC bets.** The scenarios are modeled. Execute the action tree Tuesday.

## FOMC Prep (Monday Evening)

| Task | Details |
|------|---------|
| Review Section 9 framework | `world/current_view.md` Section 9 — scenarios + action tree |
| Verify probabilities | HAWKISH 40%, NEUTRAL 30%, DOVISH 15%, SHOCK 15% (post-Kharg) |
| Pre-write response templates | For each scenario, have the first 3 actions ready |
| Check oil close | Monday close oil level feeds directly into FOMC dot plot assessment |

## Key Numbers to Watch

| Indicator | Current | Monday Alert Level | Action if Hit |
|-----------|---------|-------------------|---------------|
| Brent crude | ~$103 Fri close | >$130 | Recession risk ELEVATED. DOCS/HLNE most exposed. |
| S&P 500 | 6,632 | <6,300 (-5%) | Multiple SOs trigger but can't execute (capital locked) |
| VIX | 27.19 | >35 | Consider CVNA partial cover (squeeze risk) |
| 10Y yield | 4.29% | >4.50% | Recalculate WACC for all growth positions |
| CVNA | $300.15 | <$280 | Short working well. Let it run. |
| FTNT | $83.44 | >$90 | Exit may get better price. Don't accelerate. |
| BZU.MI | EUR 42.16 | Any price | SELL at market. Don't optimize. |

## End of Day Monday

1. Update `portfolio/current.yaml` — remove BZU.MI, update cash
2. Update `state/system.yaml` — remove BZU.MI from positions
3. Record in `portfolio/history.yaml` — BZU.MI entry/exit/P&L
4. Run `portfolio_stats.py` — final Monday snapshot
5. Prepare for FOMC Tuesday — review action tree one more time

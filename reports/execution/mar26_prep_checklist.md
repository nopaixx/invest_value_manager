# Mar 26 Execution — Tuesday Pre-Flight Checklist

> Date: 2026-03-24 (Tuesday)
> Execution: 2026-03-26 (Wednesday) — 6 trades
> Follow-up: 2026-03-27/28 — ALFA.L (7th trade)
> Prepared: S284

---

## 1. AM Price Check (all 7 tickers)

| # | Ticker | Role | Gate | Last Price | Gate Pass? |
|---|--------|------|------|------------|-----------|
| 1 | MONY.L | SELL | Market | 155.2p | N/A |
| 2 | NVO | TRIM 14.3sh | Market (before ex-div Mar 30) | $37.00 | N/A |
| 3 | FTNT | SELL | Market | $82.62 | N/A |
| 4 | GDDY | BUY EUR 720 | <=\$90 | $84.85 | |
| 5 | DNLM.L | BUY EUR 200 | <=950p | 802p | |
| 6 | ITRK.L | BUY EUR 300 | <=3,700p | 3,638p | |
| 7 | ALFA.L | BUY EUR 400 (Mar 27-28) | <=165p | 151p | |

**Action:** Run `python3 tools/price_checker.py MONY.L NVO FTNT GDDY DNLM.L ITRK.L ALFA.L MEGP.L`

---

## 2. FX Rates

| Pair | Last | Impact |
|------|------|--------|
| EUR/USD | 1.1575 | Affects NVO, FTNT, GDDY proceeds/cost |
| GBP/EUR | 1.1530 | Affects MONY.L, DNLM.L, ITRK.L, ALFA.L proceeds/cost |

**Action:** Record AM rates. If EUR/USD moves >2% from 1.1575, recalculate capital flow.

---

## 3. DNLM.L Final News Check

- [ ] WebSearch "Dunelm news March 24 2026"
- [ ] WebSearch "DNLM.L RNS"
- [ ] Check: any profit warning, trading update, broker downgrade?
- [ ] If MATERIAL negative → SKIP DNLM.L, reallocate EUR 200 to ITRK.L
- Last check (Mar 23): ALL CLEAR

---

## 4. MEGP.L Price — SO 135p Triggered?

- [ ] Price check MEGP.L
- [ ] If <=135p → FLAG for human. Can execute in eToro independently.
- [ ] If >135p → Monitor. SO remains active post-Mar 26 with EUR 644 cash available.
- Last price: 136.6p (1.2% above trigger)

---

## 5. Market Regime Check

- [ ] `python3 tools/macro_fragility.py world` — VIX, S&P, oil, 10Y, DXY
- [ ] If S&P -3%+ overnight → DEFER all 3 BUYS by 1-2 days (sells proceed)
- [ ] If VIX >35 → DEFER buys, reassess regime
- [ ] If oil >$105 Brent → Check EDEN.PA impact, proceed with caution
- [ ] Normal conditions → PROCEED as planned

---

## 6. Thesis Headers — Verification

| Ticker | FV in Header | FV in current.yaml | Match? |
|--------|-------------|-------------------|--------|
| GDDY | $130 | Check | |
| DNLM.L | 1008p | Check | |
| ITRK.L | ~4700p | Check | |
| ALFA.L | 215p | Check | |
| MEGP.L | 180p | Check | |

**Action:** Run `python3 tools/forward_return.py --active-only` and verify GrSrc = "thesis" for all positions.

---

## 7. Standing Orders — Verify All 7 Trades Documented

- [ ] `state/standing_orders.yaml` has GDDY, DNLM.L, ITRK.L as ACTIVE
- [ ] `state/calendar.yaml` has Mar 26 execution plan v2 (6 trades)
- [ ] `state/calendar.yaml` has Mar 27 ALFA.L entry
- [ ] MEGP.L SO 135p is ACTIVE in standing_orders.yaml
- [ ] SPGI SO $380 is ACTIVE in standing_orders.yaml

---

## 8. Capital Flow — Final Calculation

```
SELLS:
  MONY.L: 384 shares x [price] x GBP/EUR = EUR ___
  NVO:    14.3 shares x [price] / EUR/USD = EUR ___
  FTNT:   10.57 shares x [price] / EUR/USD = EUR ___
  Subtotal sells: EUR ___

BUYS:
  GDDY:   EUR 720 (if <=\$90)
  DNLM.L: EUR 200 (if <=950p)
  ITRK.L: EUR 300 (if <=3,700p)
  Subtotal buys: EUR 1,220

Cash before: EUR 424
Cash after Mar 26: EUR ___ (target ~1,044)
Cash after ALFA.L (Mar 27-28): EUR ___ (target ~644)
```

---

## 9. Contingencies — Decision Tree

| Scenario | Action |
|----------|--------|
| GDDY >$90 | SKIP GDDY. Add EUR 720 to: DNLM.L +300 + ITRK.L +420 |
| ITRK.L >3,700p | DEFER ITRK.L. EUR 300 → cash for MEGP.L/SPGI SOs |
| DNLM.L news negative | SKIP DNLM.L. EUR 200 → add to ITRK.L |
| Market crash -3%+ | SELL as planned. DEFER all 3 buys 1-2 days |
| ALFA.L >165p by Mar 27 | DEFER ALFA.L. SO remains active. |

---

## 10. Post-Execution (Mar 26 PM)

- [ ] Verify all 6 trades filled in eToro
- [ ] Record EXACT: shares, prices, FX rates, EUR amounts
- [ ] Report to CIO for portfolio-ops update
- [ ] Update current.yaml + history.yaml
- [ ] Update session_continuity.yaml
- [ ] Run portfolio_stats.py to verify new allocations
- [ ] Run kc_monitor.py --health for updated scores

---

*Checklist prepared S284. Execute Mar 24 AM.*

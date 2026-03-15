# Mar 26 Capital Deployment — Final Trade Confirmation | 2026-03-15

## Prerequisites (verify morning of Mar 26)

- [ ] BZU.MI already sold (Mon Mar 16) — EUR ~371 in cash
- [ ] FOMC outcome processed (Mar 18) — action tree scored
- [ ] ECB outcome processed (Mar 19)
- [ ] BoE outcome processed (Mar 20) + HLNE ex-div captured
- [ ] MONY.L ex-div confirmed Mar 26 (dividend ~EUR 28)
- [ ] GDDY price still ≤$90 (SO trigger)
- [ ] DNLM.L price still ≤950p (SO trigger)
- [ ] No KC triggered on any buy candidate
- [ ] "Would I buy from zero TODAY?" → confirmed for GDDY + DNLM.L

## 4 Trades in Sequence

### TRADE 1: SELL MONY.L

| Field | Value |
|-------|-------|
| Action | SELL |
| Ticker | MONY.L |
| Shares | 384 |
| Order | MARKET |
| Expected price | ~168p |
| Expected proceeds | ~EUR 716 |
| Reason | Selling on ex-div day. Dividend captured. Conviction LOW (#10). Growth 2% = lowest. |
| Post-trade cash | ~EUR 1,087 (371 BZU.MI + 716 MONY.L) |

### TRADE 2: TRIM NVO

| Field | Value |
|-------|-------|
| Action | SELL (partial) |
| Ticker | NVO |
| Shares | 14.3 of 36.2 (keep 21.9) |
| Order | MARKET |
| Expected price | ~$38 |
| Expected proceeds | ~EUR 472 |
| Reason | KC#1 TRIGGERED. Reduce weight 11.7%→~7%. Guide -5% to -13% adjusted sales. |
| FOMC contingency | If DOVISH → trim 10 shares instead of 14.3 (growth re-rates). |
| Post-trade cash | ~EUR 1,559 |

### TRADE 3 (PRIORITY): BUY GDDY

| Field | Value |
|-------|-------|
| Action | BUY |
| Ticker | GDDY |
| Amount | EUR 720 |
| Order | MARKET |
| Expected price | ~$81 (P/E 13.1x) |
| Expected shares | ~10.2 |
| Condition | Price ≤$90 (SO trigger). If >$90 → reallocate to DNLM.L. |
| Pre-flight | S191 COMPLETE. R4 APPROVED. 11/12 KCs CLEAR. Reverse DCF gap 30.6pp. |
| Contrathesis | S211: Even probability-weighted FV $118 gives 21.5% E[CAGR]. BUY CONFIRMED. |
| Post-trade cash | ~EUR 839 |

### TRADE 4: BUY DNLM.L

| Field | Value |
|-------|-------|
| Action | BUY |
| Ticker | DNLM.L (Dunelm Group — UK #1 homewares retailer) |
| Amount | EUR 300 (reduced from EUR 440 per S172 oil stress test) |
| Order | MARKET |
| Expected price | ~864p |
| Expected shares | ~30 |
| Condition | Price ≤950p (SO trigger). |
| Pre-flight | S191 COMPLETE. R4 APPROVED. 8 KCs from committee. 13 insiders $19.9M cluster buy. |
| Note | REDUCED sizing (EUR 440→300) due to recession risk on discretionary B2B (homewares). |
| Post-trade cash | ~EUR 539 (buffer) |

## Post-Execution State

| Metric | Before Mar 26 | After Mar 26 |
|--------|-------------|-------------|
| Positions | 10 long + 1 short | 12 long + 1 short |
| Cash | EUR ~1,087 | EUR ~539 (5.3%) |
| E[CAGR] deployed | ~18.8% | ~19.2% |
| Worst position | FTNT 9.8% | FTNT 9.8% (exit locked April) |
| UK positions | IHP.L only (post-MONY.L sell) | IHP.L + DNLM.L |
| US positions | ADBE, HLNE, DOCS | ADBE, HLNE, DOCS + GDDY |

## FOMC Contingencies

| FOMC Outcome | Mar 26 Change |
|--------------|---------------|
| HAWKISH (50%) | NO CHANGE. GDDY cheaper = better entry. Deploy as planned. |
| NEUTRAL (30%) | NO CHANGE. Execute as designed. |
| DOVISH (10%) | If GDDY >$95 → reallocate EUR 720 to DNLM.L full size. NVO trim 10 not 14.3. |
| SHOCK (10%) | Deploy everything into GDDY (EUR 1,020+). Skip DNLM.L. |

## Confirmation Required

Angel confirms each trade in eToro. CIO (Claude) has pre-approved all 4 trades.
Trades execute in order: SELL → SELL → BUY → BUY (capital must be available before buying).

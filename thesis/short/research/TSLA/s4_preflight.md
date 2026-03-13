# TSLA S4 Pre-Flight — Committee Input Package

> **Prepared:** 2026-03-07 (S145c7) | **For:** Investment Committee (SHORT_APPROVAL mode)
> **Pipeline:** S1 complete → S2 complete → S3 resolved → S4 READY

---

## Summary for Committee

| Parameter | S3 Resolved Value |
|-----------|-------------------|
| **Ticker** | TSLA (Tesla, Inc.) |
| **Direction** | SHORT |
| **FV** | $80 (prob-weighted SOTP: bear $39, base $69, bull $114, tail $185) |
| **Current Price** | $397 | **Overvaluation:** 80% |
| **Entry Zone** | $270-310 (POST Q1 delivery data only) |
| **Decision Gate** | Q1 deliveries <370K → ENTER. Q1 deliveries >400K → DEFER |
| **Stop Loss** | $420 (hard, no exceptions) |
| **Sizing** | EUR 75 (0.75% of portfolio) |
| **Max Duration** | 90 days from entry |
| **Max Loss** | EUR 26 (0.25% of portfolio at stop) |
| **Carry Cost** | EUR 5-6/year (0.05% of NAV) — negligible |
| **Primary Catalyst** | Q1 deliveries (early April) + Q1 earnings (~Apr 21) |
| **QS** | Tool 29 (Tier D) / Adj 35 (Tier C) |
| **Conviction** | 6/10 |

---

## 10 Standard Gates

### Gate 0: Sector View
- Automotive sector view exists at `world/sectors/automotive.md`
- **PASS**

### Gate 1: Quality Score Verification
- QS Tool: 29/100 (Tier D) — lowest in entire coverage universe
- QS Adjusted: 35/100 (Tier C) — +6 for energy business + net cash
- For SHORT thesis: Tier D quality at Tier A+ price = maximum quality-price gap (55 points)
- **PASS** (low QS SUPPORTS short thesis)

### Gate 2: Business Understanding
- Auto: declining deliveries, ROIC 4.6% vs WACC 15%, EPS -75% from peak
- Energy: strong business (48% growth, 30% margins) but ~8% of market cap
- FSD/Robotaxi: unsupervised rides in Austin, Cybercab production started, but $115M projected 2027 revenue
- Optimus: pre-product, "not doing useful work" per Musk
- **PASS** — business understood across all 4 segments

### Gate 3: Valuation Multi-Method
- SOTP (60% weight): $80 probability-weighted
- DCF (20%): $31-45 range (HIGH sensitivity, TV 74.5%)
- Earnings-based (20%): $52 at 25x normalized $2.08 EPS
- Reverse DCF: market implies >50% FCF growth 5yr (historical -6.3%)
- **PASS** — 3 methods, all confirm massive overvaluation

### Gate 4: Kill Conditions Defined
6 KCs defined in S3:
1. Price >$420 → COVER (stop loss)
2. Q1 deliveries >450K → COVER in 5 days
3. Auto GM >22% 2 consecutive quarters → COVER in 30 days
4. FSD approved unsupervised in 5+ US states → COVER in 30 days
5. Carry >8% annualized without active catalyst → COVER
6. 90 days elapsed without catalyst → COVER (hard deadline)
- **PASS**

### Gate 5: Risk Assessment
- Squeeze risk: SI 1.9% (low mechanical, HIGH momentum/options gamma)
- Musk factor: unpredictable tweets, DOGE politics, retail cult
- Macro: if VIX drops to 15 and Fed cuts, growth stocks rally
- Juniper: 50K orders day 1 could reverse Q1 narrative
- Mitigation: EUR 75 sizing (0.75%), $420 stop, Q1 delivery gate, 90-day max
- **PASS** (risks identified and sized for)

### Gate 6: Thesis vs Counter-Analysis
- S1 (bear): FV $52, structural fragility documented
- S2 (bull): FV $80-120, found 3 HIGH-severity S1 weaknesses
- S3 (resolution): FV $80, accepted energy/FSD upgrades, rejected $120 top-end
- Conviction reduced from implicit 8/10 (S1 overconfidence) to 6/10
- **PASS** (adversarial process complete, conflicts resolved)

### Gate 7: Portfolio Fit
- Net exposure: 100% → 99.3% (marginal reduction)
- Gross exposure: 100% → 100.7%
- Sector: Consumer Cyclical (no long exposure in this sector)
- No correlation with existing positions
- **PASS**

### Gate 8: Sizing Consistency
- EUR 75 (0.75%) = conservative end of short sizing precedents
- CVNA S4 approved at EUR 100 (1%) — TSLA smaller due to higher execution risk
- P11 (Asymmetry): max loss 0.25% at stop. Acceptable.
- P1 (Sizing by Conviction): 6/10 conviction × 0.75% = well-calibrated
- **PASS**

### Gate 9: Timing
- Q1 deliveries: early April (25-28 days away)
- Q1 earnings: ~April 21 (~45 days away)
- Catalysts are DATED with specific expected impact
- Decision gate prevents premature entry (wait for Q1 data)
- **PASS**

---

## 3 Short-Specific Gates (10+1, 10+2, 10+3)

### Gate 10+1: Catalyst with Date (P10)
- **Primary:** Q1 delivery report (early April 2026) — expect <370K if thesis holds
- **Secondary:** Q1 earnings (~April 21, 2026) — ROIC, margins, guidance
- Both are DATED, MEASURABLE, and have clear PASS/FAIL criteria
- **PASS**

### Gate 10+2: Asymmetry Check (P11)
- Entry $290 (midpoint) → Stop $420 = 45% upside risk
- Entry $290 → FV $80 = 72% downside (thesis target)
- Risk/Reward at position level: 1:1.6 (favorable)
- At portfolio level: max loss 0.25% vs potential gain ~0.5%
- Tesla has rallied 20%+ in a single week 4x in past year — stop MUST be hard
- **PASS** (asymmetry acceptable at 0.75% sizing)

### Gate 10+3: Carry Budget (P10)
- Annual carry: EUR 5-6 (0.05% of NAV) — negligible
- 90-day max duration = EUR 1.25-1.50 total carry
- No carry budget concern at this sizing
- **PASS**

---

## Resolved Issues from S3

| Issue | Resolution |
|-------|-----------|
| SI discrepancy (1.9% vs ~10%) | **Resolved:** yfinance confirms 1.9% (64.8M shares, 1.1 days to cover). Higher estimates likely include synthetic short exposure via options. Use 1.9% for squeeze assessment. |
| Energy valuation | Raised to $90B (7x rev) from S1's $64B. Industrial growth compounder, not distressed solar. |
| FSD stale data | Updated: Austin unsupervised rides operational, Cybercab production started Feb 2026. |
| Juniper blind spot | Added Q1 delivery DECISION GATE. Do not enter blind. |
| Duration | Tactical 90 days, not structural 6 months. |

---

## Committee Decision Template

```
TSLA SHORT — COMMITTEE DECISION
Date: [Monday/Tuesday]
Gate Results: [10 standard + 3 short-specific]

DECISION: [ ] APPROVE  [ ] CONDITIONAL APPROVE  [ ] REJECT

If APPROVE:
- Entry: $270-310 POST Q1 delivery data (<370K)
- Stop: $420 (HARD)
- Size: EUR 75 (0.75%)
- Duration: 90 days max
- SO to standing_orders.yaml

If CONDITIONAL:
- Conditions: [specify]

If REJECT:
- Reason: [specify]
- Alternative: [OBSERVE / revisit post-Q1]
```

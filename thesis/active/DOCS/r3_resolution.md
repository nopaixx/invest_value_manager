# DOCS R3 Resolution — Reconciling R1 ($32.80) vs R2 DA ($28-30)

> Date: 2026-03-07 (S146c4)
> Orchestrator resolution. R1 fundamental-analyst vs R2 devil's-advocate (S146c3).
> Supersedes R3 from S116 (pre-entry, different DA with 0 HIGH findings).
> **Resolved FV: $30. Growth: 8%. E[CAGR]: 13.8%.**

---

## Context

DOCS is an ACTIVE position: 39.93 shares @ $24.81 avg, ~8% of portfolio. The S146 R2 DA found 3 HIGH-severity challenges (vs 0 HIGH in the S116 DA). This R3 must reconcile.

---

## Three HIGH Findings — Resolution

### HIGH #1: Pharma Digital Ad TAM Growth (5.6% vs 13%)

**R1 claimed:** TAM growing 10-13%/yr (citing 360iResearch, eMarketer older estimates).
**DA found:** eMarketer 2025-2026 shows 5.6% ($24.8B to $26.2B) for all pharma digital.

**Resolution: PARTIALLY ACCEPT. TAM growth is 6-9%, not 13%.**

The DA is right that 13% is overstated. But 5.6% is ALL healthcare+pharma digital (broad definition). Doximity's addressable market is HCP-directed digital pharma advertising — a narrower, faster-growing segment where:
- Pharma is actively shifting from TV/print to digital (structural, not cyclical)
- HCP-directed spend grows faster than DTC digital (physicians are harder to reach)
- 360iResearch broader pharma marketing CAGR is 8.86%

**Resolved TAM growth: 7% (midpoint of 5.6% broad and 8.86% total pharma marketing).**

Impact: DOCS needs ~3pp annual share gains (from 2.5% to ~4% over 3yr) to grow at 10%. At 7% TAM + 1-2pp share gain = 8-9% revenue growth. Achievable with monopoly position but not automatic.

### HIGH #2: 43% Internal Valuation Spread ($28 OEY vs $40 DCF)

**R1 produced:** OEY $28, DCF $40, EV/Sales $34. Weighted $32.80.
**DA flagged:** 43% spread signals model uncertainty. SBC-adjusted OEY of $24 = at market price.

**Resolution: ACCEPT. Reduce DCF and EV/Sales to narrow the spread.**

The 43% spread was driven by R1 using 12% growth in DCF — too high given TAM correction. Recalibrating:

| Method | R1 FV | R3 Adjusted FV | Change | Rationale |
|--------|-------|----------------|--------|-----------|
| OEY (50%) | $28 | $28 | Unchanged | OE-based, not TAM-dependent |
| DCF (30%) | $40 | $35 | -$5 | Growth reduced 12% to 9% |
| EV/Sales (20%) | $34 | $30 | -$4 | Multiple 7-9x (from 8-10x) on lower growth |

**New weighted FV:** $28 * 0.50 + $35 * 0.30 + $30 * 0.20 = $14.00 + $10.50 + $6.00 = **$30.50 -> $30**

New spread: $28 to $35 = 25%. Acceptable.

### HIGH #3: MFN + IRA + DTC = Triple Squeeze (Structural vs Temporary)

**R1 claimed:** MFN is temporary, 6-12 month headwind, pharma budgets normalize.
**DA found:** MFN signed by 14/17 largest pharma. PwC calls it "here to stay." IRA expanding.

**Resolution: PARTIALLY ACCEPT. 12-18 month headwind, not 6-month, but not permanent destruction.**

MFN is structural as a CONCEPT — pharma companies will always face pricing pressure. But the BUDGET IMPACT is cyclical: pharma companies adjust marketing budgets to new margin reality over 4-6 quarters, then spending resumes at new baseline. "Record January bookings" from CEO suggests partial normalization already underway.

Impact: delays growth re-acceleration from H1 FY2027 to H2 FY2027. Already captured in growth adjustment (10% -> 8%).

---

## Growth Input Resolution

| Source | Growth Estimate | Basis |
|--------|----------------|-------|
| R1 thesis | 10% | FY2026 guided 13%, 4yr CAGR 18.4%, conservative 10% |
| DA challenge | 7% | Q4 guide 4%, sell-side 9%, NRR declining |
| Management | 4% (Q4) / 13% (FY) | Q4 likely sandbagged per "record Jan bookings" |
| Sell-side consensus | ~9% | Mean of varied estimates |

**Resolved growth: 8%.**

Rationale:
- TAM 7% + share gains 1-2pp - MFN drag ~1pp = 7-9% net
- NRR at 112% (declining from 118%) supports deceleration but not collapse
- "Record January bookings" suggests Q4 sandbagged — actual FY growth likely 8-10%
- 8% is the midpoint between DA's 7% and R1's 10%
- Conservative enough to survive MFN persistence, generous enough to reflect monopoly

---

## Resolved Fair Value: $30

| Metric | R1 | R3 Resolved | Change |
|--------|-----|-------------|--------|
| FV | $32.80 | **$30** | -8.5% |
| Growth input | 10% | **8%** | -2pp |
| TAM growth assumed | 13% | **7%** | -6pp |
| MFN duration | 6-12 months | **12-18 months** | Extended |
| Valuation spread | 43% | **25%** | Narrowed |

### E[CAGR] at Resolved Values

```
FV = $30 (R3 resolved)
Price = $25.34 (current, Mar 7)
Growth = 8%
Yield = 0%

Capital Appreciation: (30/25.34)^(1/3) - 1 = 5.8%
E[CAGR_3yr] = 5.8% + 8.0% + 0% = 13.8%
```

**E[CAGR] 13.8% > 12% Tier A threshold. Position JUSTIFIED.**

At cost basis $24.81:
```
Capital Appreciation: (30/24.81)^(1/3) - 1 = 6.5%
E[CAGR_3yr] = 6.5% + 8.0% = 14.5%
```

### Scenarios (R3 Revised)

| | Bear (25%) | Base (50%) | Bull (25%) |
|--|-----------|-----------|-----------|
| Revenue CAGR 5yr | 4% | 8% | 14% |
| FCF margin | 35% | 40% | 45% |
| FV | $22 | $30 | $48 |
| At $25.34 | -13% | +18% | +89% |

Expected Value: ($22 * 0.25) + ($30 * 0.50) + ($48 * 0.25) = $5.50 + $15.00 + $12.00 = **$32.50**

Asymmetry: +18% upside (base) / -13% downside (bear) at market. Adequate.

---

## Sizing Resolution

**DA flagged:** Position at 8% vs committee-approved 4%.

**Resolution:** The ADDs were executed via market-buy protocol when E[CAGR] exceeded 12% Tier A threshold (documented in current.yaml notes). At that time, E[CAGR] was 19.0% with 10% growth — justified at 8%.

With R3 adjustments: E[CAGR] drops to 13.8%. Compare to portfolio:
- EDEN.PA 19%: 27.1% E[CAGR] -> justified
- IHP.L 11%: 19.6% E[CAGR] -> justified
- NVO 13%: 23.8% E[CAGR] -> justified
- DOCS 8%: 13.8% E[CAGR] -> on the edge

**Decision: HOLD at 8% through Q4 earnings (~May 2026). Do NOT add.**
- If Q4 BEATS + FY2027 guide >10%: growth back to 10%, FV rises to $33+, position justified
- If Q4 IN-LINE + guide 8-10%: thesis intact, hold 8%
- If Q4 MISSES + guide <8%: TRIM to 5%, revise FV to $25-27

---

## Kill Conditions (R3 Revised — 7 total)

Original 6 KCs maintained. Adding KC#7 per DA recommendation:

1. Net Revenue Retention drops below 100%
2. Physician engagement declines >10% YoY
3. Revenue declines for 2 consecutive FULL fiscal years
4. SBC/Revenue exceeds 15% without offsetting buyback increase
5. Major competitor achieves >30% physician penetration
6. Pharma digital advertising TAM contracts for 2+ years
7. **(NEW) Q4 FY2026 revenue misses below $140M AND FY2027 guide <6%.** Confirms structural growth impairment, not temporary MFN. At 8% position, thesis-breaking.

---

## Action Items

1. Update thesis header: FV $32.80 -> $30. Growth 10% -> 8%.
2. Update current.yaml: FV $32.80 -> $30.
3. Pre-build Q4 earnings framework (Section 9) before May 2026.
4. Do NOT trim or add before Q4. Hold 8%.
5. Monitor NRR — if Q4 shows NRR <108%, growth trajectory worse than 8%.

---

## Pipeline Status

**R1_COMPLETE -> R2_COMPLETE -> R3_COMPLETE**

Next: Q4 FY2026 earnings (~May 2026) is the decision gate.
- BEAT -> validate thesis, potentially R4 for ADD
- MISS -> EXIT protocol evaluation at 8% position

## Velocity: 2 units (R2->R3 advancement)

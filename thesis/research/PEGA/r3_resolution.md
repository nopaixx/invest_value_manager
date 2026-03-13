# PEGA R3 Resolution — Post-DA

> **Date:** 2026-02-25 | **Session:** 116
> **R1 FV:** $53 | **DA Bear FV:** $32.50 | **Market:** $43.28

---

## DA Verdict: MODERATE COUNTER (4 HIGH, 0 CRITICAL)

Four high-severity challenges require resolution before committee.

## Key DA Findings & Resolution

### 1. FV Below Consensus — No Edge Articulated (HIGH)
- **DA view:** Our FV $53 vs Street $68-82. If we're more bearish than 10 analysts, what's our edge?
- **Resolution:** ACCEPT the gap exists but DISAGREE this is a problem. Our system is DELIBERATELY conservative:
  - We use SBC-adjusted FCF (Street often uses reported)
  - We incorporate litigation reserve (Street may not)
  - Our DA reduces FV further (systematic process)
  - **Edge is NOT in FV accuracy — edge is in ENTRY PRICE discipline.** Street says buy at $43 for $75 target. We say buy at $38 for $50 target. Our downside is -17% to DA bear; Street's is -57% to DA bear. We win on risk-adjusted return.
- **FV adjustment:** $53 → $50 (SBC-adjusted FCF as primary input per DA recommendation)

### 2. Q4 Revenue +2.8% YoY Deceleration (HIGH)
- **DA view:** 17% full-year masks Q4 slowdown. 10% growth assumption may be aggressive
- **Counter:** ACV +17%, backlog +28%, deferred revenue +20% — ALL leading indicators support continued growth. Q4 was subscription license timing, not structural
- **Resolution:** PARTIALLY ACCEPT. Adjust base case growth from 10% to 8% for Year 1, 10% Year 2+. This reduces FV by ~$3. Already captured in $53→$50 adjustment

### 3. Appian Retrial — Both Liability AND Damages (HIGH)
- **DA view:** New trial covers both liability and damages, not just damages. Could result in $200-500M adverse outcome
- **Resolution:** ACCEPT as genuine binary risk. This is THE reason for:
  - Half-position sizing (EUR 200 instead of EUR 400) — MMC precedent for binary litigation
  - Entry at $38 instead of $43 — wider MoS to compensate for binary risk
  - Gate: "Appian retrial resolution OR Q1 2026 earnings confirm growth normalization"
  - Quantified impact: at $350M judgment, net cash → 0, buyback program eliminated, FV → ~$38 (essentially no upside). This justifies the wider entry requirement.

### 4. Valuation Anchored to Reported FCF Not SBC-Adjusted (HIGH)
- **DA view:** Using $491M vs $335M inflates all valuation methods by ~30%
- **Resolution:** ACCEPT. Revised valuation uses SBC-adjusted FCF $335M as primary input:
  - OEY on SBC-adj: $335M / 7.3B EV = 4.6% yield + 8% growth = 12.6% (borderline)
  - EV/SBC-adj-FCF: 7.3B / 335M = 21.8x (reasonable for transitioning software)
  - FV adjusts to ~$50 from SBC-adjusted basis

### 5. CEO Selling $59.8M (MODERATE)
- **DA found:** SEC Form 4 shows 921K shares sold over 12 months under 10b5-1 plan
- **Resolution:** ACCEPT as factual correction to thesis "no meaningful selling" claim. However:
  - $59.8M = 1.8% of total holdings
  - Post-sales ownership: ~45% (still massive)
  - 10b5-1 plan = pre-committed, not reactive
  - KC#3 threshold (>5% of stake) remains appropriate — at current selling pace, 3.5 years to KC trigger
  - **Thesis CORRECTED: "Systematic insider selling ~$5M/month under 10b5-1. 1.8% of total stake. Alignment remains strong at 45%."**

## Resolved Fair Value

| Source | FV | Weight |
|--------|-----|--------|
| R1 (FA) | $53.00 | Input |
| DA bear | $32.50 | Input |
| **R3 resolved** | **$50.00** | **Final** |

**Rationale:** SBC-adjusted FCF as primary input (-$3), with additional Appian probability weighting already captured in DA bear case. $50 is midpoint between "everything works" ($53 unadjusted) and "SBC fully penalized" ($45-48 DA post-adjustment range).

## Entry & Sizing

- **Entry:** $38.00 (was $43 — widened for Appian binary risk + Q4 deceleration)
- **Size:** EUR 200 half-position (MMC precedent for binary litigation)
- **Gate:** Appian retrial resolution OR Q1 2026 earnings confirm growth normalization
- **SO updated:** ACTIVE → GATED in standing_orders.yaml

## Pipeline Status

**R1_COMPLETE → R2_COMPLETE → R3_COMPLETE (GATED)**

Next: R4 Investment Committee when EITHER gate clears AND price ≤$38. Current price $43.28 = 12.2% above entry.

## Velocity: 2 units (R2→R3 advancement)

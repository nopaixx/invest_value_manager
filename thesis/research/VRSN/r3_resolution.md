# VRSN R3 Resolution — 2026-02-27

## R1 vs R2 Summary

| Metric | R1 (FA) | R2 (DA) | R3 Resolution |
|--------|---------|---------|---------------|
| **FV** | $255 | $235-240 | **$240** |
| **QS** | 88adj | N/A | **86adj** (-2 for edge concern) |
| **Moat** | WIDE (4.2/5) | WIDE (confirmed) | **WIDE** |
| **Risk** | MEDIUM | MEDIUM+ | **MEDIUM** |
| **SO** | $200 | $190 | **$190** |
| **Counter** | — | MODERATE (6/19 HIGH+CRITICAL) | — |

---

## Resolution of Each Challenge

### 1. Berkshire sold 32.4% at $267 (CRITICAL) → **ACCEPT**

The R1 thesis cited Berkshire as quality validator 3 times while omitting the largest-ever position reduction. Todd Combs (position originator) left Berkshire Dec 2025.

**Resolution:** Remove Berkshire as quality validator. The sell at $267 is informative as a FV ceiling signal from an informed holder. Retain as context: "Berkshire was a 13-year holder, reduced 32% at $267 pre-Combs departure. Remaining 9.8% may be orphaned position."

**System learning:** R1 agents must check 13F CHANGES (not just holdings) via `smart_money.py stock-profile`. The stock-profile already shows this data but the FA didn't use it properly.

### 2. FCF margin peak 64.5% (HIGH) → **PARTIALLY ACCEPT**

3yr average 58.3%. FY2025 had unusually low capex. Management guided $55-65M capex 2026 (vs ~$40M FY2025).

**Resolution:** Use 60% normalized FCF margin for base case. VRSN's pricing power structurally lifts margins over time, so 60% (above 3yr avg 58.3%) is a reasonable base, not 64.5% peak.

**Impact:** OEY component drops from $253 to ~$240.

### 3. Receivables +37.5% anomaly (HIGH) → **ACCEPT as GATE**

Cannot resolve without 10-K review. Could be Q4 billing timing (benign) or extended registrar terms (concerning).

**Resolution:** Add as monitoring item, NOT full KC. If FY2026 Q1 receivables remain elevated (>20% above revenue growth), escalate to KC. Note: VeriSign has $1.07B annual FCF — even if $50-80M receivables are delayed, cash generation is not threatened.

### 4. Demand elasticity untested (HIGH) → **PARTIALLY ACCEPT**

Consecutive 7% increases HAVE never been tested. But domain cost ($10.26/yr rising to ~$13.45 by 2030) is trivial for any operating business. The price sensitivity is concentrated in speculative/parked domains (~30% of base).

**Resolution:** Reduce full-price-increase probability from 85% to 75%. Model 5-6% average increase (vs 7% max). This reduces base case revenue growth from 9% to 7-8% for 2027-2029. Impact on FV: -$5-8.

### 5. OEY too aggressive at 4.2% (HIGH) → **PARTIALLY ACCEPT**

Pure utilities trade at 5-6% OEY. VRSN has contractual pricing power = better than utility. But 5% revenue growth warrants some premium.

**Resolution:** Use 4.3% OEY (compromise). Not 4.5% (DA's suggestion ignores the pricing power differential). At 4.3% OEY with 60% FCF margin: FV ≈ $240.

### 6. No informational edge (MODERATE) → **ACCEPT**

Our FV ($240) is below consensus ($276.50). The thesis relies on publicly known contractual pricing.

**Resolution:** This is important context for position sizing. Without edge, demand higher MoS. Reflected in SO $190 (MoS 20.8%) instead of $200 (MoS 16.7%).

---

## Resolved FV: $240

| Method | Weight | FV |
|--------|--------|----|
| OEY (4.3%, 60% FCF margin) | 50% | $240 |
| EV/EBIT (19x FY2027E, conservative growth) | 30% | $250 |
| Reverse DCF (market-implied, as check) | 20% | $225 |
| **Weighted** | — | **$240** |

| Scenario | FV | Probability |
|----------|-----|-------------|
| Bear | $165-185 | 25% |
| Base | $240 | 50% |
| Bull | $310-320 | 25% |
| **Expected** | **$241** | |

Bear case revised downward ($185→$165-185) per DA's point about regulatory block + volume decline scenario.

---

## Standing Order Adjustment

| | Old (R1) | New (R3) |
|--|----------|----------|
| **FV** | $255 | $240 |
| **SO** | $200 | **$190** |
| **MoS at trigger** | 21.6% | 20.8% |
| **E[CAGR] at trigger** | 12.4% | ~12.0% |
| **Distance from current** | 12.6% | 15.7% |

At $190: E[CAGR] ≈ (240/190)^(1/3) - 1 + sustainable growth ~5% + yield 1.4% ≈ 8.1% + 6.4% ≈ 14.5%.

Wait, recalculating properly:
- FV reversion: (240/190)^(1/3) - 1 = (1.263)^(0.333) - 1 = 8.1%
- Sustainable growth: ~5% (revenue CAGR)
- Dividend yield: ~1.4% (buyback-adjusted)
- E[CAGR] at $190 ≈ 14.5% — comfortably above 12% Tier A threshold.

At $200: E[CAGR] ≈ (240/200)^(1/3) - 1 + 5% + 1.4% = 6.3% + 6.4% = 12.7% — marginal.

**$190 is the right entry.** Provides MoS 20.8% and E[CAGR] ~14.5%.

---

## Kill Conditions (updated from R1 + DA input)

1. ICANN contract NOT renewed at 2030 expiry (any credible non-renewal threat)
2. .com domain base declines 2+ consecutive years
3. ICANN strips pricing authority permanently (regulatory/political action)
4. Alternative DNS system gains >5% market share
5. FCF margin falls below 50% for 2+ consecutive years
6. Renewal rate drops below 70%
7. **NEW (DA): Receivables divergence persists >2 quarters (receivables growth > 2x revenue growth)**

---

## Verdict

**R3_COMPLETE. WATCHLIST. SO $190.**

Quality: Genuine WIDE moat monopoly. QS 86adj Tier A. Business is real and durable.
Price: Market is pricing it correctly at base case ($224.50 vs $240 FV = 6.5% MoS). No edge at current price.
Entry: $190 provides sufficient MoS (20.8%) and E[CAGR] (~14.5%) for a Tier A no-edge position.
Timeline: Price increase announcement Apr-Oct 2026 may re-rate stock HIGHER, pushing entry further away. But also: any market correction could bring it to $190 quickly (52wL was $209).

**Not a priority deployment candidate.** SO $190 is 15.7% below current. In Fair-Value regime, this requires either (a) broad market correction or (b) specific negative catalyst. No urgency.

---

## DA Accuracy Tracker Entry

| Ticker | Pre-DA FV | Post-DA FV | Change | DA Severity | Key Finding |
|--------|-----------|------------|--------|-------------|-------------|
| VRSN | $255 | $240 | -5.9% | MODERATE (6/19) | BRK sold 32.4% at $267 (CRITICAL omission). FCF margin peak. Receivables anomaly. No edge. |

---

*R3 resolved by CIO, Session 127 (2026-02-27). Velocity: 2 units (R2→R3).*

# Investment Committee Decision: SPG (Simon Property Group)

> **Date:** 2026-03-17
> **Committee Session:** R4 Evaluation
> **Verdict:** WATCHLIST (CONDITIONAL APPROVAL)
> **Hard Gate:** BLOCKED on SECTOR VIEW — `world/sectors/real-estate.md` does not exist

---

## GATE 0: SECTOR VIEW EXISTS (HARD BLOCK)

**Status: FAIL — HARD BLOCK**

```
Sector: Real Estate (retail REIT)
Search: Glob("world/sectors/*real-estate*") → NO MATCH
```

**No sector view found for Real Estate.** Cannot give full BUY approval without sector context.

This gate is a HARD BLOCK per Error #30 (ADBE) and Error #42 (LULU). The R3 resolution itself flagged this as a gate condition. The R1 thesis, DA, and R3 all independently identified this gap.

**Impact on verdict:** This BLOCKS any standing order from being formalized. The verdict is WATCHLIST with a CONDITIONAL upgrade to SO-eligible once `real-estate.md` is created.

**However**, because this is a WATCHLIST decision (not a BUY), I proceed through all 10 gates to provide a complete evaluation for when the sector view is created. The committee documents the full assessment so no re-evaluation is needed beyond sector view creation.

---

## Precedentes Consultados

1. **BZU.MI (S151):** Tier B, 35.7% MoS, 3.6% sizing, E[CAGR] 15.9%. Relevance: Most recent Tier B BUY. BZU.MI was approved at MoS 35.7% with E[CAGR] 15.9% > 15% threshold. SPG's proposed E[CAGR]@entry (13.3%) is BELOW this precedent. BZU.MI was subsequently sold after 3 days due to macro regime change (Error #67). This precedent suggests SPG's 13.3% E[CAGR] is INSUFFICIENT for Tier B.

2. **NVO (S146c8):** Tier B, FV $47, growth 5%, E[CAGR] 16.6%. Relevance: Another Tier B position where DA reduced growth (10% -> 5%). NVO was justified at 16.6% E[CAGR] > 15% threshold. SPG at 13.3% is 1.7pp below this threshold.

3. **WKL.AS (S143):** Tier B, FV EUR 80, growth 6%, 20.9% E[CAGR]. Relevance: Information monopolist Tier B. WKL.AS had E[CAGR] well above threshold. SPG does not match.

**Deviation from precedents:** SPG at 13.3% E[CAGR] is BELOW the 15% Tier B threshold used in all 3 precedents. All Tier B BUYs had E[CAGR] >= 15%. SPG fails this consistency test. The committee would require E[CAGR] >= 15% at entry for SPG, implying entry closer to $130 (where yield + growth + convergence compound to 15%+), or a change in the thesis growth assumption.

---

## Gate 1: QUALITY SCORE

**Status: PASS (CONDITIONAL)**

```
[X] QS Tool: 64/100 (Tier B)
[X] QS Adjusted: 72/100 (Tier B, upper)
[X] Tier: B (not D — proceed)
```

**Assessment:** The +8 adjustment is well-documented and justified:
- +6 for REIT leverage distortion (0/10 -> 6/10 on ND/EBITDA). A/A2 credit rating and 6.5x interest coverage confirm this is NOT distressed leverage.
- +2 for market position correction (SPG is #1 globally by 4x).

The EPS CAGR of 29.5% inflating the Growth sub-score (10/10) is an offsetting factor that makes the net +8 reasonable.

**QS 72adj Tier B is accepted.** This is NOT a quality compounder — it is a quality income/value REIT.

---

## Gate 2: BUSINESS UNDERSTANDING

**Status: PASS**

```
[X] Business Analysis Framework completed (comprehensive in thesis)
[X] Can explain in 2 minutes:
    SPG owns 200+ irreplaceable Class A malls and Premium Outlets.
    #1 retail REIT globally (4x next largest). Record FFO $12.73.
    96.4% occupancy, $799/sqft tenant sales. A/A2 rating.
    Revenue ~90% recurring via long-term leases with built-in escalators.
[X] Know WHY it is not cheap + counter-thesis:
    It is NOT cheap at $190. Fairly valued to slightly overvalued.
    Counter-thesis: rate shock compresses P/FFO; tariff-driven tenant stress;
    anchor closures (Macy's 150, JCPenney weakness); correlated risk chain.
[X] Value trap checklist: 1/10 (NOT a value trap)
[X] Informational edge: THIN TO NONE
    Our FV ($158) is BELOW consensus PT ($206). We are more cautious than
    the market, not seeing hidden value. Edge is discipline (waiting for pullback).
```

---

## Gate 3: PROJECTION FUNDAMENTADA

**Status: PASS**

```
[X] Revenue growth derived: 4% (R3 resolved from FA 5% vs DA 3.1%)
    - 2026 guidance: $13.13 midpoint = 3.1% FFO growth
    - NOI escalation: 4.4% domestic
    - Refinancing headwind: -$0.25-0.30/share guided
    - Resolved to 4% (3-5% range midpoint, generous to FA)
[X] WACC: 9.3% (using beta-adjusted Ke 10.2%, Kd after-tax)
[X] Terminal growth: 2.5% (implicit in DDM 4-5% div growth)
[X] Scenarios documented:
    Bear ($145): Flat FFO, 12.5x P/FFO, 5.75% cap rate
    Base ($183→$170 R3): $13.13 FFO, 14x P/FFO
    Bull ($212→$195 R3): $13.75 FFO, 16x P/FFO
```

---

## Gate 4: VALUATION MULTI-METHOD

**Status: PASS**

```
[X] Methods appropriate for REIT (NAV, DDM, P/FFO — NOT DCF):
    - P/FFO (50% weight): Bear $166, Base $184, Bull $210
    - NAV (25% weight): Bear $94, Base $140, Bull $170
    - DDM (25% weight): Bear $121, Base $155, Bull $210
[X] R3 Resolved FV: $158 (60/40 anti-bullish applied)
[X] DA Bear FV: $140 (independent calculation)
[X] Divergence between methods: HIGH (NAV bear $94 vs P/FFO base $184)
    Explanation: NAV is extremely cap-rate sensitive (100bp = ~$60/share).
    P/FFO is more stable. Divergence is NORMAL for REITs and appropriately
    handled via weighting (50% P/FFO, 25% each NAV and DDM).
```

---

## Gate 5: MARGIN OF SAFETY

**Status: FAIL AT MARKET / CONDITIONAL PASS AT ENTRY**

```
[X] Tier: B (QS 72adj)
[X] MoS at market ($190.53):
    vs R3 FV ($158): -20.6% (OVERVALUED)
    vs Bear ($140): -36.1% (DEEPLY OVERVALUED)
[X] MoS at proposed entry ($140):
    vs R3 FV ($158): 11.4%
    vs Bear ($140): 0% (AT bear case)

Precedent check:
- BZU.MI: 35.7% MoS at buy (Tier B). SPG at $140: 11.4% MoS. SIGNIFICANTLY lower.
- NVO: ~25% MoS at initial buy. SPG at $140: 11.4%. Lower.
- Deviation justified?: PARTIALLY. SPG has WIDE moat (vs BZU.MI NARROW-WIDE) and
  A/A2 credit (strongest in portfolio). However, SPG also carries $29.2B debt in a
  rising rate environment with correlated risk chain active. The lower MoS is NOT
  fully compensated by moat quality.

E[CAGR] check:
- E[CAGR]@entry ($140): ~13.3% (4% growth + 4.6% yield + 4.0% convergence + 0.7% div growth)
- E[CAGR] threshold for Tier B: 15%
- SPG is 1.7pp BELOW threshold
- This is the critical failure: E[CAGR] does not clear Tier B requirement
```

**Assessment:** At $140 entry, MoS is 11.4% vs FV and 0% vs bear. E[CAGR] of 13.3% is below the 15% Tier B threshold. This is a marginal case. The committee does NOT approve at $140 for a Tier B.

**To achieve 15% E[CAGR]:** Entry would need to be ~$130 (MoS 17.7% vs $158, convergence ~6.5%/yr, total E[CAGR] ~15.8%). However, this is 31.8% below current price and approaches FANTASY territory.

**Alternative framing:** If SPG were reclassified as a defensive income compounder with WIDE moat, a 12% threshold (Tier A-like income) could apply. At $140, 13.3% > 12%. But SPG is NOT Tier A (QS 72, not 75+), so this reclassification is not warranted.

---

## Gate 6: MACRO CONTEXT

**Status: ADVERSE**

```
[X] World view reviewed (dated 2026-03-16)
[X] Cycle: LATE / HOSTILE
    - Oil: WTI $97-99 (Hormuz closed, Kharg struck)
    - FOMC: Tomorrow Mar 18, stagflation dilemma
    - Tariffs: Section 301 probes into 16+ economies
    - Consumer spending: declining
[X] Fit empresa-ciclo: POOR
    - REITs are rate-sensitive: higher-for-longer compresses P/FFO
    - Consumer-facing retail REIT: tariffs + oil pressure tenants
    - Correlated risk chain ACTIVE: oil + tariffs + potential recession ALL hitting simultaneously
[X] Megatendencias: E-commerce neutral (priced in), rate sensitivity HIGH
```

**Assessment:** This is one of the worst possible macro environments for a retail REIT. The committee notes that this hostile environment is exactly what could create the pullback needed to reach $140. Patience is the correct posture.

---

## Gate 7: PORTFOLIO FIT

**Status: CONDITIONAL PASS (if entry reached)**

```
Constraint checker output (EUR 400 at SPG):
[X] Position post-purchase: 3.9% — reasonable for Tier B MODERATE conviction
[X] Sector (Real Estate): 3.9% — new sector, no concentration risk
[X] Geography (US): 43.6% — HIGH but within historical range
[X] Cash post-purchase: EUR 24 (0.2%) — CRITICALLY LOW
[X] Correlation with existing: LOW (REIT = new asset class, uncorrelated with tech/data/pharma)

Sizing reasoning:
- EUR 400 = 3.9% of portfolio, consistent with Tier B precedents (3-5%)
- If falls 50%: -1.9% portfolio impact = acceptable for MODERATE conviction
- Cash drops to 0.2% = problem. Would need to be funded from rotation or post-sale proceeds.
- US geography at 43.6% is high but includes diverse sectors (tech, healthcare, alt AM, physician platform)

Precedent: BZU.MI was EUR 370 (3.6%). SPG at EUR 400 (3.9%) is consistent.
```

**Assessment:** Sizing is reasonable IF entry reached. The cash constraint (0.2% remaining) means this would need to be funded from rotation or from a FTNT exit (approved for late April). The committee flags this but does not block.

---

## Gate 8: SECTOR UNDERSTANDING

**Status: FAIL (HARD BLOCK)**

```
[ ] Sector view exists: world/sectors/real-estate.md → DOES NOT EXIST
[ ] Sector view reviewed: N/A
[ ] TAM and trends understood: Partially (from thesis), but not formalized
[ ] Disruption risks known: Partially (e-commerce addressed, but systematic sector analysis missing)
[ ] Sectoral position: UNKNOWN (no sector view to determine OVER/NEUTRAL/INFRA weighting)
```

**Assessment:** This is the HARD GATE that prevents full approval. The thesis contains sector-level analysis embedded in the business understanding section, but there is no standalone sector view document. Before any standing order can be formalized, `world/sectors/real-estate.md` must be created covering:
- US retail REIT landscape (SPG, MAC, SKT, O, NNN, VICI comps)
- Cap rate environment and trends
- Anchor tenant health assessment
- E-commerce penetration trajectory
- Rate sensitivity analysis
- Our sectoral stance (OVERWEIGHT/NEUTRAL/UNDERWEIGHT)

---

## Gate 9: AUTOCRITICA + EDGE

**Status: PASS**

```
[X] Unvalidated assumptions:
    1. EPS anomaly in 2025 (doubled from $7.26 to $14.17) — source unknown, no 10-K access
    2. AFFO per share not available — estimated at ~$10.2 but not verified
    3. Cap rate assumptions from T2/T3 sources (Green Street)
    4. JCPenney financial health opaque (private entity)
[X] Biases recognized:
    [X] Popularity bias: SPG is one of the most-covered REITs — we may be drawn to it
        because it is familiar, not because it offers superior risk-adjusted return
    [X] Confirmation bias: The WIDE moat narrative is compelling and may cause us to
        underweight the correlated risk chain
    [X] Anchoring: The $206 consensus PT may anchor expectations upward
[X] Kill conditions defined: 8 KCs documented in R3 (expanded from 7 in R1 + 4 DA additions)
[X] What would change my mind: E[CAGR] at entry >= 15%, sector view positive on retail REITs,
    FOMC signals rate cuts in 2026, OR price reaches $130 (where safety margin is genuine)
[X] Edge Test: "What do I know that market doesn't?"
    ANSWER: Nothing specific. Our FV ($158) is 23% BELOW consensus ($206).
    We have NO variant perception. Our "edge" is discipline — the willingness to wait
    for a price the market currently doesn't demand. This is a THIN edge at best.
    WARNING: Error #49 applies — when FV < consensus, we're not seeing hidden value.
[X] Falsifiability: "What would make this thesis wrong?"
    ANSWER: (a) Interest rates stay at 4.5%+ through 2027, compressing P/FFO permanently
    to 12-13x. (b) Anchor closures cascade beyond A-mall resilience. (c) Consumer recession
    drives occupancy below 93%. (d) SPG's non-core investments (Saks, JCPenney) produce
    cumulative losses >$500M.
```

---

## Gate 10: COUNTER-ANALYSIS & INDEPENDENT ASSESSMENTS

**Status: PASS (all findings addressed)**

```
[X] Counter-analysis exists: devils_advocate.md
[X] Verdict: MODERATE COUNTER (4 HIGH findings)
[X] HIGH/CRITICAL findings:
    1. FFO growth 5% vs guidance 3.1% — RESOLVED: Growth reduced to 4% in R3
    2. Entry $170 above 60/40 FV — RESOLVED: Entry lowered to $140 in R3
    3. Re-rating speculative at $170 — RESOLVED: Convergence target $158 at $140 entry
    4. Correlated risk chain underweighted — RESOLVED: Acknowledged, entry lowered to buffer

[X] Moat assessment exists: moat_assessment.md
    Classification: WIDE (matches thesis)
    ROIC "widening" claim corrected by DA — normalized spread ~3-4pp, stable not expanding.
    Committee accepts WIDE moat with stable (not widening) spread.

[X] Risk assessment exists: risk_assessment.md
    Risk score: MEDIUM-HIGH
    5 risks HIGH or CRITICAL. Correlated risk chain identified.
    Additional risks NOT in thesis: FCF margin erosion (860bp over 4yr), receivables
    divergence (17.3% vs 6.7% revenue), OCF/NI anomaly (0.9x).
    Additional KCs suggested: 4 added in R3 (same-store NOI, debt cost, write-offs, ND/EBITDA).

[X] No valuation_report.md exists (not required for R4).

Unresolved conflicts: NONE. All DA HIGH findings were addressed in R3.
```

---

## VERDICT: WATCHLIST (CONDITIONAL)

### Primary Reasons:

1. **HARD GATE: No sector view** (`world/sectors/real-estate.md` does not exist). Error #30 applies. Cannot formalize standing order.

2. **E[CAGR] below threshold.** At R3 entry of $140, E[CAGR] ~13.3% is below the 15% Tier B threshold used consistently in all prior Tier B BUY decisions (BZU.MI 15.9%, NVO 16.6%, WKL.AS 20.9%).

3. **Price distance: -26.5%.** Current $190.53 vs entry $140 requires significant pullback. Without a specific catalyst with timeline, this approaches FANTASY territory.

4. **No informational edge.** Our FV ($158) is 23% below consensus PT ($206). We are more cautious than the market, not seeing hidden value. Error #49 applies.

5. **Hostile macro for retail REITs.** Oil crisis, FOMC uncertainty, tariff escalation all active simultaneously.

### Conditions for Upgrade to Standing Order:

1. **Create `world/sectors/real-estate.md`** via sector-screener agent (HARD GATE)
2. **Price reaches $140** (or a specific catalyst creates realistic path to $140 within 6 months)
3. **Q1 2026 earnings confirm** FFO guidance holds ($13.00-$13.25 range)
4. **Post-FOMC clarity** on rate trajectory (if higher-for-longer confirmed, $140 becomes more achievable)

### If Conditions Met:

```
STANDING ORDER: BUY EUR 400 of SPG at $140
  QS: 72adj Tier B | FV: $158 | MoS: 11.4%
  E[CAGR]: ~13.3% (below 15% — STRETCH APPROVAL, see note)
  Sizing: 3.9% portfolio | Conviction: MODERATE-LOW
  Kill conditions: 8 defined
  Basket: Orphan (no active Real Assets basket)
  Expiry: 2027-03-31
```

**NOTE on E[CAGR] shortfall:** The 13.3% E[CAGR] is 1.7pp below the 15% Tier B threshold. The committee does NOT grant full approval at this E[CAGR]. Options for the orchestrator:

(a) **Accept 13.3%** if SPG serves a portfolio diversification purpose (first REIT, uncorrelated asset class, 4.6% yield income). This would be a DEVIATION from precedent requiring documentation.

(b) **Lower entry to $130** where E[CAGR] ~15.8% clears threshold. But this is -31.8% from current = FANTASY.

(c) **Wait for growth upgrade.** If Q1 2026 shows FFO growth accelerating above 4%, the base case improves and $140 entry may clear 15%.

The committee recommends option **(a) or (c)** and leaves the final call to the orchestrator.

---

## Kill Conditions (8 — Confirmed)

1. **KC#1:** Occupancy falls below 93% for 2 consecutive quarters
2. **KC#2:** FFO/share declines >10% YoY
3. **KC#3:** Dividend cut or suspension
4. **KC#4:** Net Debt/EBITDA exceeds 7.5x sustained 2Q
5. **KC#5:** Interest coverage falls below 4.0x
6. **KC#6:** Weighted average cost of debt exceeds 6.0%
7. **KC#7:** 3+ anchor closures in single property triggering >10% vacancy
8. **KC#8:** Cumulative non-core investment write-offs exceed $300M in 3 years

---

## META-REFLECTION

### Dudas sobre esta decision
- The E[CAGR] of 13.3% is a borderline case. In a different macro (rate cuts, consumer strength), the growth assumption could be 5%, lifting E[CAGR] to ~14.5-15%. But making decisions based on "what if macro improves" is exactly the kind of wishful thinking the framework is designed to prevent.
- SPG would be the first REIT in the portfolio. There is genuine diversification value in adding an uncorrelated asset class, but the committee lacks a sector view to assess whether SPG is the BEST REIT or merely the most familiar one (Error #7 popularity bias).
- The EPS anomaly in 2025 (near-doubling) was flagged by thesis, moat assessment, DA, AND R3 — but NEVER resolved. We are making decisions based on FFO (which is clean) rather than EPS, so this does not directly affect the verdict. But it does affect QS (inflated Growth sub-score) and creates uncertainty about earnings quality.

### Debilidades del analisis recibido
- No 10-K access to resolve the EPS anomaly, AFFO calculation, or cotenancy clause exposure
- Cap rate assumptions are T2/T3 sourced (Green Street, industry reports), not independently verified
- No competitor analysis within the REIT sector (is SPG the best REIT to own, or is Realty Income or Prologis better risk-adjusted?)
- Smart money context is thin — 93% institutional is standard for mega-cap REITs, not differentiated

### Sugerencias de mejora
- **System:** quality_scorer.py needs a `--reit` flag to handle leverage scoring for asset-backed businesses. The 0/10 leverage score for a A-rated REIT is systematically wrong and will distort every REIT evaluation.
- **System:** dcf_calculator.py --reverse is meaningless for REITs. Consider adding P/FFO implied growth as a REIT-specific calibration.
- **Process:** The DA correctly identified Error #49 risk (FV below consensus = no edge). This should be a STANDARD check in every DA, not an ad-hoc observation.

### Preguntas para Orchestrator
1. Does the portfolio benefit from REIT diversification enough to accept 13.3% E[CAGR] (below 15% Tier B threshold)?
2. Should sector-screener create `real-estate.md` now, or only if SPG price approaches $140?
3. Are there better REIT candidates (O, PLD, VICI, AMT) that might offer higher E[CAGR] at current prices?

---

**Committee Decision:** WATCHLIST (CONDITIONAL)
**Signed:** Investment Committee, 2026-03-17

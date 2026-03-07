# Investment Committee Decision: BZU.MI (Buzzi SpA)

## Date: 2026-03-07
## Committee: R4 Investment Committee (10 Gates)
## Pipeline: R1 (thesis.md) -> R2 (r2_devils_advocate.md) -> R3 (r3_resolution.md) -> R4 (this document)

---

## Precedentes Consultados

1. **RACE.MI**: Tier A (QS 84), MoS 11.9%, sizing 3.4% (EUR 350). THREE WAITS mandate buy at market. E[CAGR] 13.5%. Relevance: Same Italian exchange, similar EUR sizing, recent precedent for E[CAGR]-framework deployment. Outcome: active position.

2. **MORN**: Tier A (QS 78), MoS 17%, sizing 4.3% (EUR 466). First E[CAGR]-framework market buy. E[CAGR] 15.6%. Relevance: similar E[CAGR] range to BZU.MI at entry (15.9%). Outcome: sold for rotation (E[CAGR] declined to 5.1%).

3. **NVO**: Tier A/B (QS 73 now), MoS 38% at initial buy. Sizing 3.4%. Relevance: same QS score as BZU.MI tool (73). Cyclical event-driven entry (guidance shock). Outcome: active, multiple ADDs, position doubled.

**Key consistency observation:** BZU.MI at EUR 42 entry has E[CAGR] 15.9% and QS 73/75adj. This is consistent with MORN precedent (E[CAGR] 15.6%, QS 78) but for a more cyclical company with lower QS. The R3 recommendation to use SO at EUR 42 (not market buy at EUR 43.62) is CONSISTENT with our discipline of not buying below the E[CAGR] threshold at market (14.6% < 15% for Tier B). I do NOT deviate from precedents.

---

## GATE 0: Sector View Exists

```
[X] Sector identified: Building Materials / Cement
[X] Sector view verified: world/sectors/building-materials-cement.md
[X] Sector view date: 2026-03-07 (FRESH, updated today)
[X] Status: NEUTRAL-CAUTELA (cyclical at late-peak, oil shock adds cost pressure)
```

**PASS.** Sector view exists and is current.

---

## GATE 1: Quality Score (CRITICAL)

```
[X] QS Tool: 73/100
[X] QS Adjusted: 75/100 (+2: market position +5, cyclical peak -3)
[X] Tier: Borderline A (75 = minimum threshold)
[X] R3 treatment: Tier B (correct -- borderline QS 75 on a cyclical company near peak margins warrants conservative treatment)
```

**Decision: TREAT AS TIER B.** The QS of 75 is the floor for Tier A. For a cyclical cement company where trailing ROIC is cyclically inflated (FY2024 peak), Tier B treatment is the honest classification. The R1 meta-reflection flagged that gross margin premium (+40pp) may be an accounting artifact -- if corrected, QS drops to 68-70 (firmly Tier B). I apply Tier B MoS and E[CAGR] thresholds (15%).

**PASS** (QS >= 35, not Tier D).

---

## GATE 2: Business Understanding

```
[X] Business Analysis Framework: COMPLETE in thesis.md
[X] 2-minute explanation: Buzzi manufactures cement -- a local commodity with natural monopoly dynamics within 150-300km transport radius. 8 US plants + 36 terminals = unassailable US network. 53% family ownership = maximum alignment. Best margins in industry (38.4% US EBITDA). Net cash EUR 1.1B.
[X] Why it's "cheap": P/E 9.6x reflects PEAK earnings on cyclical margins near highs. Through-cycle P/E is 12-13x = fairly valued, not cheap. Italian listing discount (-1.5x vs peers). Russia exposure (7% revenue).
[X] Contra-tesis: US cement demand declining 2 consecutive years. Margins normalizing from peak. Italian discount may be structural (no English IR, no US listing, limited minority voice). Kerrisdale EUR 85 target is unreliable (39% win rate on longs).
[X] Value trap checklist: 0/10 -- NOT a value trap
[X] Informational advantage: Through-cycle EV/EBIT analysis + buyback data (EUR 258M in 2024, EUR 200M program 2026) that R1 initially missed. Limited edge (~5% vs consensus PT EUR 50.25).
```

**PASS.**

---

## GATE 3: Projections Grounded

```
[X] Revenue growth derived: LFL organic +2-3% (TAM 3.3% CAGR, flat-to-negative US volumes, +3-5% US pricing, flat EU volumes, +2-3% EU pricing). Inorganic from Brazil/UAE already in base.
[X] WACC calculated: 8.5-9.0% (Rf 2.5% + Beta 1.05 * ERP 5.0% = Ke 7.75%, adjusted upward for cyclical risk premium. Debt at 2.6% after-tax. 90/10 equity/debt)
[X] Terminal growth: 2.0-2.5% (cement = GDP-level, conservative)
[X] Scenarios documented:
    - Bear (25%): EBIT EUR 700M, 9x multiple -> FV EUR 40
    - Base (50%): EBIT EUR 850M, 10.5x -> FV EUR 55
    - Bull (25%): EBIT EUR 1,000M, 11.5x -> FV EUR 70
```

**PASS.**

---

## GATE 4: Multi-Method Valuation

```
[X] Method appropriate for Tier B cyclical: Through-cycle EV/EBIT (PRIMARY) + EV/EBITDA normalized (SECONDARY)
    - DCF explicitly rejected as unreliable for cyclicals (71% FV spread, 74.5% TV -- BOTH above reliability thresholds)

[X] Method 1: Through-Cycle EV/EBIT (60% weight)
    - Through-cycle EBIT: EUR 850M (R3 resolution from R1's 875M and R2's 800-850M)
    - Multiple: 10.5x (sector avg 11x, -1.5x Italian discount, +1x best margins, +0.5x net cash, -0.5x Russia)
    - Net cash: EUR 1,000M
    -> FV: EUR 54.70 per share

[X] Method 2: EV/EBITDA Normalized (40% weight)
    - Through-cycle EBITDA: EUR 1,100M (25% margin on EUR 4,400M)
    - Multiple: 9.0x
    - Net cash: EUR 1,000M
    -> FV: EUR 60.10 per share

[X] Weighted FV: EUR 57 (54.70 * 0.60 + 60.10 * 0.40 = 56.86, rounded)
[X] Expected Value: EUR 55 (40 * 0.25 + 55 * 0.50 + 70 * 0.25)
[X] Divergence between methods: 10% (EUR 54.70 vs EUR 60.10) -- acceptable for cyclical
```

**PASS.**

---

## GATE 5: Margin of Safety (Reasoned)

```
[X] Tier: B (cyclical, borderline QS 75, treated conservatively)

At Entry EUR 42 (SO trigger):
[X] MoS vs Weighted FV (EUR 57): +35.7%
[X] MoS vs Expected Value (EUR 55): +30.9%
[X] MoS vs Base Case (EUR 55): +30.9%
[X] MoS vs Bear Case (EUR 40): -4.8% (price ABOVE bear by EUR 2)

At Market EUR 43.62 (current):
[X] MoS vs Weighted FV (EUR 57): +30.7%
[X] MoS vs Expected Value (EUR 55): +26.1%
[X] MoS vs Base Case (EUR 55): +26.1%
[X] MoS vs Bear Case (EUR 40): -8.3%
```

**Reasoning:**

The MoS at entry EUR 42 is 31% vs EV -- this is robust for a Tier B cyclical. However, several factors require explicit consideration:

1. **Cyclical peak risk:** EBITDA margins are normalizing from peak (30% -> ~27% in FY2025). Through-cycle EBIT of EUR 850M is an estimate with inherent uncertainty. If margins revert further (to 22-23% pre-2023 levels), FV could be EUR 45-48. The bear case downside at entry (-4.8% to EUR 40) is limited, which provides comfort.

2. **Precedent comparison:** Tier B buys in this fund have typically had MoS of 20-30%. At EUR 42, MoS 31% is at the top of this range -- appropriate for a cyclical where earnings risk is elevated.

3. **Negative MoS vs Bear:** The stock at EUR 42 is above the bear case of EUR 40. This means in a bear scenario, the downside is ~4.8%. For a cyclical near peak, this is a concern -- but it's offset by: (a) the bear case already models margin reversion to 2021-2022 trough levels, (b) Buzzi's net cash provides balance sheet protection, (c) the EUR 200M buyback program (Feb-Aug 2026) provides a price floor.

4. **Market buy at EUR 43.62:** MoS is 26% vs EV, which is adequate for Tier B. BUT E[CAGR] at market is 14.6% -- below the 15% Tier B threshold. The R3 correctly identified this. The discipline of using E[CAGR] thresholds as deployment gates is a core framework principle. Breaking it for 0.4pp would set a bad precedent.

**Precedent most similar:** MORN at MoS 17% (E[CAGR] 15.6%, Tier A). BZU.MI at entry EUR 42 has BETTER MoS (31%) but LOWER QS (73 vs 78) and MORE cyclical risk. Net: comparable risk-adjusted case.

**Do I deviate from precedent?** NO. The SO at EUR 42 respects the E[CAGR] threshold discipline. I am NOT recommending market buy despite MoS being "adequate" at 26% because E[CAGR] 14.6% < 15% Tier B threshold.

**PASS.**

---

## GATE 6: Macro Context

```
[X] World view reviewed: 2026-03-07 (today)
[X] Cycle: Late-peak + OIL SHOCK ($91-92 WTI). CRISIS ENVIRONMENT.
[X] Iran war Day 7. Hormuz near-total halt. Oil at crisis levels.
[X] Recession probability: 40-55% (elevated)
[X] Inflation re-accelerating: CPI trajectory toward 3.0%+
[X] Building materials sector status: NEUTRAL-CAUTELA

Fit empresa-ciclo:
[X] Cement is PROCYCLICAL -- volumes drop 10-20% in downturns
[X] Oil at $92 = direct cost headwind (energy 10-15% of cement production costs)
[X] BUT: Buzzi has net cash EUR 1.1B (no refinancing risk), best margins (can absorb cost), buyback providing floor
[X] Infrastructure tailwinds (IIJA 60% unspent, German fiscal, PNRR) partially offset cyclical weakness
[X] SO at EUR 42 (not market buy) is the CORRECT approach in crisis -- wait for further weakness

Megatendencias:
- Infrastructure spending: POSITIVE (IIJA, PNRR, German fiscal)
- Oil shock: NEGATIVE short-term (cost), NEUTRAL medium-term (pricing power)
- CBAM: POSITIVE (barrier to EU imports, benefits incumbents)
- AI data centers: MARGINAL positive (2-3% of US demand, not a game-changer)
```

**Assessment:** The macro context reinforces the decision to use SO at EUR 42 rather than market buy. In a crisis environment with oil at $92 and recession probability 40-55%, a cyclical cement company should be bought on weakness, not at current levels. If the crisis deepens, BZU.MI could trade toward EUR 36-40 (52wL EUR 36.50), which would represent an even better entry.

**PASS (for SO at EUR 42; would FAIL for market buy).**

---

## GATE 7: Portfolio Fit (Reasoned)

```
[X] Current price: EUR 43.62 (2026-03-07)
[X] Proposed SO trigger: EUR 42
[X] Proposed sizing: EUR 400 (~3.7% of EUR ~10,800 total portfolio)

Note: constraint_checker.py REPORT failed due to portfolio format issue (RACE.MI, WKL.AS lack invested_usd). Manual calculation below.

Portfolio context (manual):
- Current cash: EUR 1,517 (14.1% of portfolio)
- Total positions: 12 active
- EUR 400 deployment at EUR 42 = cash drops to ~EUR 1,117 (~10.4%)

Position concentration post-buy:
[X] BZU.MI at ~3.7% -- consistent with Tier B precedent range (3-5%)
[X] If falls 50%: -1.85% portfolio impact -- acceptable for Tier B conviction

Sector concentration:
[X] Building Materials / Cement: 0% currently -> 3.7% -- NO sector overlap
[X] This adds geographic diversification (Italy) and sector diversification (building materials) -- both POSITIVE for portfolio construction

Geographic concentration post-buy:
[X] Italy exposure: RACE.MI ~3.2% + BZU.MI 3.7% = ~6.9% Italy -- ACCEPTABLE (Italy is "developed other" per P2, tolerance medium)
[X] BUT: Buzzi has 40% US revenue, 18% Germany, 9% Brazil -- it's a GLOBAL operator. Geographic risk is diversified within the company.

Correlation with existing positions:
[X] LOW correlation. No other building materials or cement positions.
[X] RACE.MI is the only other Italian-listed stock -- but Ferrari (luxury auto) and Buzzi (cement) have essentially zero business correlation
[X] Closest correlation: EDEN.PA (European industrial) -- but different sectors entirely
```

**Precedent sizing similar:** RACE.MI at EUR 350 (3.4%), Tier A. BZU.MI at EUR 400 (3.7%), Tier B. Slightly larger sizing for a lower tier -- justified by HIGHER MoS (31% vs 11.9%) which compensates for lower QS.

**PASS.**

---

## GATE 8: Sector Understanding

```
[X] Sector view exists: world/sectors/building-materials-cement.md
[X] Sector view date: 2026-03-07 (FRESH)
[X] TAM: ~$425B global, 5.7% CAGR
[X] Competitive structure: Regional oligopoly. Top 5 US = 56% of shipments
[X] Barriers to entry: Very High (permitting 5-10yr, EUR 200-300M capex, CBAM)
[X] Disruption risk: LOW (200-year product, no substitute at scale)
[X] M&A activity: Active consolidation (Holcim spinoff, CRH $40B, Heidelberg Burnco)
[X] Sector position: NEUTRAL-CAUTELA (late-peak + oil shock)
[X] Key risk: Cyclicality -- P/E appears low at peak earnings
[X] Oil shock assessment: Direct cost impact (energy 10-15%), pricing power lag 6-12 months, infrastructure spending partially insulated
```

**PASS.**

---

## GATE 9: Self-Critique + Edge

```
Unvalidated assumptions:
[X] 1. Through-cycle EBIT EUR 850M -- most critical assumption. Only 4 years of data. Pre-2021 data would help enormously.
[X] 2. "55% structural / 45% cyclical" split on margin improvement -- estimated, not proven. FY2025 shows margins compressing.
[X] 3. US cement volumes will stabilize (flat) -- could decline further in 2026 (3rd consecutive year)
[X] 4. Italian discount stays at current level -- could widen if family never pursues US listing

Biases recognized:
[X] Popularity bias: Kerrisdale Capital public thesis on this name. I have deliberately REMOVED Kerrisdale as a credibility anchor per R3 resolution. My thesis stands independently.
[X] Confirmation bias: The 12% price decline since R1 makes the stock feel "cheaper" and could bias toward buying. I control for this by maintaining the E[CAGR] threshold discipline (14.6% at market < 15%).
[X] Recency bias: FY2024 peak margins could anchor expectations upward. I control for this with through-cycle EBIT normalization.

Kill conditions:
[X] 1. US EBITDA margin below 30% for 2 consecutive years (structural margin compression)
[X] 2. Net debt exceeds 2x EBITDA (currently net cash -- would signal reckless M&A)
[X] 3. Family ownership drops below 40% (alignment loss)
[X] 4. Russia forced exit with >EUR 500M writedown
[X] 5. ROIC below WACC for 2 consecutive years (through-cycle)

What would make me change my mind:
- FY2025 full results showing US EBITDA margin below 32% AND US volumes -10%+ would suggest the structural thesis is wrong
- Oil sustained above $100 for 6+ months would fundamentally change the cost structure for cement

Edge Test: What do I know that market doesn't?
- LIMITED edge. Our FV (EUR 55 EV) is only ~9% above consensus PT (EUR 50.25). The edge is thin.
- The specific edge is: (a) through-cycle normalization suggests market underestimates sustainable earnings power, (b) the EUR 200M buyback program provides a price floor that not all investors may be pricing in, (c) the SO approach at EUR 42 gives us a better entry than current market if cyclical trough materializes
- HONEST ASSESSMENT: This is NOT a high-conviction edge. It's a moderate-conviction cyclical play.

Falsifiability: What would make this thesis wrong?
- If through-cycle EBIT is EUR 700-750M (not EUR 850M), FV drops to EUR 45-48 and the stock is fairly priced NOW. This is possible if the "structural margin improvement" proves to be fully cyclical.
```

**PASS -- but edge is THIN. This is acknowledged and reflected in conservative entry strategy (SO, not market buy).**

---

## GATE 10: Counter-Analysis & Independent Assessments

```
[X] counter_analysis exists? YES -- r2_devils_advocate.md
[X] moat_assessment.md exists? NO
[X] risk_assessment.md exists? NO
[X] valuation_report.md exists? NO

Counter-analysis verdict: MODERATE COUNTER (3 HIGH / 16 total, 0 CRITICAL)

HIGH severity challenges:
1. Through-cycle EBIT should be EUR 800-850M, not 850-900M
   -> RESOLVED in R3: EBIT reduced to EUR 850M (midpoint), FV reduced EUR 1.50/share
2. US cement demand declining 2 consecutive years, not growing
   -> RESOLVED in R3: US volume assumption downgraded from +0-2% to FLAT. Infrastructure catalyst downgraded from 70%/+5-10% to 50%/+2-5%
3. Cyclical downturn already underway (not hypothetical)
   -> RESOLVED in R3: Acknowledged. Entry strategy maintains EUR 42 SO (not market buy). Bear case raised to EUR 40 (from EUR 39) due to buyback floor.

Unresolved challenges:
- Convertible bond EUR 150M terms unknown -> assessed as LOW severity (1.8% dilution, immaterial)
- US cement pricing softening in late 2025 -> acknowledged as risk, monitored via KC#1

R2 positive finding incorporated:
- EUR 258M shareholder returns in 2024 (EUR 111M dividends + EUR 147M buybacks)
- EUR 200M buyback program authorized Feb 2026
- Shareholder yield increased from 1.4% to 3.5% in E[CAGR] calculation

No CRITICAL unresolved challenges. All HIGH challenges resolved in R3.
```

**PASS.**

---

## VERDICT: APPROVE -- Standing Order at EUR 42

### Recommendation

```
RECOMENDACION: STANDING ORDER EUR 400 de BZU.MI a EUR 42

Quality Score: 73 tool / 75 adjusted -> Tier B treatment (borderline A, cyclical)
Fair Value: EUR 57 weighted, EUR 55 expected value
MoS at entry EUR 42: 31% vs EV (26% vs base)
E[CAGR] at entry EUR 42: 15.9% (ABOVE 15% Tier B threshold)
E[CAGR] at market EUR 43.62: 14.6% (BELOW 15% threshold -- no market buy)
Categoria: Quality Cyclical (Tier B)
Sizing: EUR 400 (~3.7% of portfolio)
Riesgo principal: Through-cycle EBIT normalization uncertainty + macro crisis (oil $92, recession probability 40-55%)
Kill conditions: 5 defined (US EBITDA margin, leverage, family ownership, Russia writedown, ROIC persistence)
Precedent sizing: RACE.MI EUR 350 (3.4%, Tier A), MORN EUR 466 (4.3%, Tier A)
```

### Standing Order Details

| Field | Value |
|-------|-------|
| Ticker | BZU.MI |
| Exchange | Milan (Borsa Italiana) |
| Trigger | EUR 42.00 |
| Amount | EUR 400 |
| Shares (approx) | ~9.52 shares |
| Valid until | July 2026 (H1 2026 earnings) |
| E[CAGR] at trigger | 15.9% |
| MoS at trigger | 31% vs EV |
| Downside to bear | -4.8% (EUR 42 -> EUR 40) |
| Distance from market | -3.7% (EUR 43.62 -> EUR 42.00) |

### Why NOT Market Buy at EUR 43.62

1. E[CAGR] at market (14.6%) is BELOW the 15% Tier B threshold
2. The cycle has NOT troughed: US volumes declining, prices softening, margins compressing
3. Oil at $92 WTI creates additional near-term cost pressure for cement producers
4. 52-week low is EUR 36.50 -- in a recession scenario, EUR 38-40 is reachable
5. EUR 42 is only 3.7% below market -- realistic fill probability given macro headwinds
6. The R3 resolution explicitly recommended SO over market buy, and I concur with the reasoning

### Basket Assignment

BZU.MI remains a **standalone pipeline entry** (no basket). If the SO triggers and we take a position:
- Score CRH, Vulcan Materials, Heidelberg Materials as potential basket companions
- If 2+ score Tier A/B with compelling entry -> propose "Infrastructure Materials" basket
- Until then, BZU.MI is an individual position, not a basket

---

## Summary of Gates

| Gate | Status | Notes |
|------|--------|-------|
| 0. Sector View | PASS | building-materials-cement.md (2026-03-07) |
| 1. Quality Score | PASS | QS 73/75adj, Tier B treatment |
| 2. Business Understanding | PASS | 0/10 value trap, cement oligopoly understood |
| 3. Projections | PASS | Revenue +2-3% organic, WACC 8.5-9.0%, scenarios documented |
| 4. Valuation | PASS | EV/EBIT 60% + EV/EBITDA 40% = EUR 57 FV, EUR 55 EV |
| 5. MoS | PASS | 31% at EUR 42, consistent with Tier B precedents |
| 6. Macro | PASS (for SO) | Crisis environment reinforces SO discipline over market buy |
| 7. Portfolio Fit | PASS | 3.7% sizing, new sector, Italy +3.7% acceptable |
| 8. Sector | PASS | NEUTRAL-CAUTELA, fresh sector view |
| 9. Self-Critique | PASS | Edge thin but acknowledged. Kill conditions defined. |
| 10. Counter-Analysis | PASS | MODERATE COUNTER, all HIGH resolved in R3 |

**VERDICT: 10/10 GATES PASS -> APPROVE with Standing Order EUR 42, EUR 400 sizing**

---

## META-REFLECTION

### Dudas sobre esta decision
- Through-cycle EBIT EUR 850M is the make-or-break assumption with only 4 years of financial data. If the structural margin thesis is wrong and margins revert to pre-2023 levels (22-23%), FV drops to EUR 45-48 and the stock is fairly priced at current levels. The SO at EUR 42 would then have almost zero MoS.
- The edge vs consensus is thin (~9%). This is not a high-conviction information advantage. The investment case relies more on cyclical timing discipline (buy at trough) than on superior information.
- Oil at $92 creates a BINARY risk: if sustained, cement margins compress further and the stock could trade to EUR 36-38 (better entry). If oil normalizes on ceasefire, the stock may recover above EUR 45 before our SO fills. The SO at EUR 42 may end up being a "miss" if oil normalizes quickly.

### Debilidades del analisis recibido
- The R1 missed the EUR 258M buyback data -- this was a material omission caught by the DA. Future R1s for capital-intensive industrials should explicitly check for buyback/shareholder return programs.
- The quality_scorer.py gross margin premium (+40pp) for Buzzi is likely an accounting artifact (cost classification differences in cement). This inflates the moat sub-score by ~7 points. If corrected, QS drops to ~68-70 (firmly Tier B). The tool should flag unreliable GM comparisons for materials companies.
- Pre-2021 financial data would dramatically improve the through-cycle EBIT estimate. The 4-year window (2021-2024) captures a trough AND a peak but does NOT capture a full normal period (2015-2019 would be critical).
- Convertible bond (EUR 150M, May 2025) terms remain unknown. Immaterial at ~1.8% dilution but should be tracked.

### Sugerencias de mejora
- The constraint_checker.py tool crashed on portfolio positions without `invested_usd` (RACE.MI, WKL.AS use `invested_eur`). The tool should handle both EUR and USD invested amounts.
- A through-cycle EV/EBIT calculator tool would be valuable for industrials/cyclicals, automating the normalization that the R1 analyst had to do manually.
- The quality_scorer.py should have a `--cyclical-adjust` flag that averages ROIC/margins over longer periods when available, and flags gross margin comparisons as unreliable for certain sectors.

### Preguntas para Orchestrator
- None. The decision is clear: APPROVE with SO at EUR 42. No escalation needed.

---

Sources:
- R1: thesis/research/BZU.MI/thesis.md (2026-03-05)
- R2: thesis/research/BZU.MI/r2_devils_advocate.md (2026-03-06)
- R3: thesis/research/BZU.MI/r3_resolution.md (2026-03-07)
- Sector: world/sectors/building-materials-cement.md (2026-03-07)
- Portfolio: portfolio/current.yaml (2026-03-07)
- World view: world/current_view.md (2026-03-07)
- Price: BZU.MI EUR 43.62 (2026-03-07, price_checker.py)
- Consistency: consistency_checker.py "BUY BZU.MI 3.7%" -> COHERENT

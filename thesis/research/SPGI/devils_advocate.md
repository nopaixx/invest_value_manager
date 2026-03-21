# Counter-Analysis: SPGI (S&P Global Inc.)

> **DA Verdict:** MODERATE COUNTER
> **Pre-DA FV:** $470 (R3 resolved, was $511 R1, DA MODERATE COUNTER -8.0%)
> **Post-DA FV:** $440 (-6.4% correction from R3 FV)
> **DA Independent Bear FV:** $375 (P/Normalized FCF 24x on $5.2B normalized FCF)
> **Date:** 2026-03-21
> **Thesis Challenged:** R1 thesis dated 2026-02-28, R3 resolution 2026-02-28, R4 committee 2026-03-13

---

## Calibration Anchor

**BEFORE reading thesis:**
- Market at $424.43 implies 14.0% FCF growth for 5 years (reverse DCF).
- Historical FCF CAGR: 29.5% (inflated by 2022 post-merger low base; normalized ~10-12%).
- Revenue growth decelerating: 13.7% (2024) to 7.9% (2025). Guided 6-8% for 2026.
- Current EV/EBIT: 21.6x (tool). P/E: 29.0x.
- DA historical stats: Average correction -15.7%, median -13.0%. Previous SPGI DA (Feb 28) was MODERATE COUNTER, reduced FV $511 to $470 in R3. This is a REFRESH DA given proximity to $420 SO trigger.
- **CRITICAL CONTEXT:** SPGI is R4 APPROVED CONDITIONAL at $420 SO, currently $424.43 -- only 1.0% from trigger. This DA must be THOROUGH because we could be deploying EUR 400 within days.

**Market anchor:** At $424, the market prices 14% FCF growth. SPGI's own revenue guidance is 6-8% + margin expansion ~75bps + buybacks ~3% = implied ~12-13% FCF growth. The market is pricing SLIGHTLY ABOVE management's implied FCF growth trajectory. This is fair-to-slightly-optimistic, not clearly cheap.

---

## Resumen Ejecutivo

This is a REFRESH DA on SPGI, updating the February 28 DA with 3 weeks of additional market information and reflecting the R4 committee's conditional approval at $420. The thesis correctly identifies SPGI as one of the widest-moat businesses in global capital markets (ratings duopoly + index monopoly). The R3 resolution to $470 was reasonable. However, three issues have INTENSIFIED since the original DA: (1) the receivables anomaly (+20% vs +8% revenue) remains UNRESOLVED and the Q1 gate has not yet cleared, (2) the FCF contraction in 2025 ($5.46B vs $5.57B in 2024 despite 8% revenue growth) raises questions about margin expansion sustainability, and (3) the Mobility spinoff creates near-term valuation uncertainty with unquantified stranded costs. At $424, SPGI is at the R4 committee's $420 trigger -- this DA confirms the GATE on Q1 earnings is ESSENTIAL. Do NOT deploy until receivables normalize and FCF trajectory is confirmed.

---

## Asunciones Clave Desafiadas

### 1. "Receivables +20% vs Revenue +8% is probably timing" (KC #8 ALREADY BREACHED)

- **Evidencia en contra:** The R1 thesis flagged this as an "ANOMALY FLAG" but then dismissed it as "could be timing (Q4 issuance surge billed late)." The R3 treated it as a GATE (correct), but the fact remains: the thesis's OWN kill condition #8 ("Receivables growth exceeds revenue growth by >10pp for 2+ quarters") has already hit the threshold in its FIRST observation.
- Narrative_checker.py confirms: Receivables growth 20.0% vs Revenue growth 7.9% = +12.1pp gap. This exceeds the kill condition threshold of >10pp.
- From accounting quality literature: receivables growing 2.5x faster than revenue is a classic red flag for (a) aggressive revenue recognition, (b) deteriorating collection quality, (c) channel stuffing, or (d) extending payment terms to win deals. The Beneish DSRI (Days Sales Receivable Index) threshold for concern is 1.1x; SPGI's implied DSRI is ~1.11x.
- The "Q4 timing" explanation is UNVERIFIED. No 10-Q breakdown confirms this is seasonal. SPGI's FY2024 receivables grew in line with revenue -- this divergence is NEW.
- **Severidad:** HIGH -- This is the single most important data point for the Q1 gate. If Q1 2026 shows receivables normalizing (DSRI < 1.05), the gate clears. If receivables stay elevated, it signals a real quality-of-earnings issue.
- **Resolucion sugerida:** The Q1 gate is CORRECTLY in place. DO NOT remove it. If Q1 shows receivables still growing >10pp above revenue, escalate to KILL condition evaluation. This is NOT negotiable.

### 2. "Revenue growth 7% sustainable (management guided 6-8%)"

- **Evidencia en contra:** Revenue growth trajectory: 11.8% (2023) -> 13.7% (2024) -> 7.9% (2025). The direction is clearly DOWN.
- Management guided 6-8% for 2026. The R3 resolved to 6.5% organic + 0.5% M&A = 7% total. But the composition matters:
  - Market Intelligence (36% of revenue): organic CC growth only 5% in 2025. This is the WEAKEST segment and the LARGEST by revenue. AI-native competitors are explicitly targeting Capital IQ workflows.
  - Ratings (25%): guided "low to mid-single digit" billed issuance growth. After +12% in 2025 (refinancing boom), normalization to 5-6% is reasonable but is a DECELERATION.
  - Only Indices (13% of revenue) is growing >10%, and it is the SMALLEST major segment.
- If MI stays at 5%, Ratings normalizes to 5%, and Indices grows 12%, the BLENDED rate is: (0.36 x 5%) + (0.25 x 5%) + (0.13 x 12%) + (0.14 x 6%) + (0.12 x 8%) = 1.8% + 1.25% + 1.56% + 0.84% + 0.96% = **6.4%**. This is BELOW the R3's 7% assumption.
- S&P Global shares fell as much as 18% on February 10, 2026 after the guidance miss -- the market is clearly concerned about deceleration.
- **Severidad:** MODERATE -- 6.5-7% is achievable if MI stabilizes, but the downside risk is 5.5-6%. The difference between 6% and 7% revenue growth compounds to ~5% FV difference over 5 years.
- **Resolucion sugerida:** Use 6.5% as base case (unchanged from R3). But acknowledge the realistic bear case is 5.5-6%, not 4-5% as the R1 bear scenario assumes.

### 3. "FCF margin will expand from 35.6% to 36.5-37.5%"

- **Evidencia en contra:** FCF DECLINED in 2025: $5.46B vs $5.57B in 2024, despite revenue growing 8%. FCF margin dropped from 39.2% to 35.6% -- a 360bps compression, not expansion.
- Capex/Depreciation ratio rose to 1.8x in 2025 (from 1.3x in 2024), indicating significant reinvestment. This is likely for AI capabilities (Kensho, Spark, Drift AI) and cloud infrastructure.
- The R3 correctly adjusted to 35.5% FCF margin base case (down from R1's 37.5%). But projecting EXPANSION from 35.5% to 37% by 2028 requires capex intensity to DECLINE. If AI investment continues at current pace, FCF margin may stay flat at 35-36%.
- **Severidad:** MODERATE -- The R3 already partially addressed this. But the projection of expansion lacks supporting evidence given the capex trajectory.
- **Resolucion sugerida:** Use 35.5% FCF margin as FLAT assumption through 2028, not expanding. This reduces normalized FCF from ~$5.9B to ~$5.5B, which feeds into OEY valuation.

### 4. "AI ENHANCES data toll-booths, does not disrupt"

- **Evidencia en contra:** This is partially true for Ratings and Indices (which are regulatory/infrastructure monopolies), but questionable for Market Intelligence (36% of revenue). S&P Global's OWN management acknowledged that MI has faced "rising pressure from AI-native data agents that threaten to replace traditional terminals like Capital IQ."
- The competitive response (acquiring Drift AI, enhancing Capital IQ Pro, integrating ProntoNLP) is sensible but represents COST (investment that compressed FCF margin) not REVENUE.
- The real question is whether Capital IQ's 85% retention rate holds as AI alternatives become more capable. If retention drops to 80%, MI revenue growth goes from 5% to ~1-2%, dragging the blended rate below 6%.
- HOWEVER: Ratings (regulatory duopoly) and Indices (network effect monopoly) are genuinely AI-resistant. AI cannot replace the need for an NRSRO-certified credit rating or the S&P 500 brand. The R1 is CORRECT that 62-75% of SPGI's revenue is essentially immune to AI disruption.
- **Severidad:** MODERATE for the company overall, but HIGH for the Market Intelligence segment specifically.
- **Resolucion sugerida:** Monitor MI retention rates and organic growth. If MI organic growth drops below 3% for 2 consecutive quarters, it signals AI displacement is real.

### 5. "Mobility spinoff is value-accretive ($532-639 SOTP)"

- **Evidencia en contra:** The R1 thesis (updated S152) models the Mobility spinoff as generating +$62-169/share in value. But it IGNORES several risks:
  - **Stranded costs:** Management EXCLUDED stranded costs from 2026 guidance, acknowledging they exist but not quantifying them. Typical stranded costs for large spinoffs run 2-5% of spun-off revenue = $35-88M annually for Mobility's $1.75B revenue. For RemainCo, this could be $50-100M in unabsorbed overhead.
  - **Management distraction:** The Form 10 process in Q2 2026 will consume executive attention during a period of growth deceleration.
  - **Separation costs:** Legal, IT, real estate, employee retention packages -- typically 3-5% of spun-off entity revenue = $50-88M one-time.
  - **Multiple risk:** The SOTP assumes RemainCo trades at 25-27x EBIT (up from current 24x). But this requires the market to RE-RATE SPGI upward in a year of decelerating growth. Multiple expansion during growth deceleration is historically RARE.
- The spinoff COULD be positive, but the R1's $586 base SOTP vs $470 current FV suggests 25% hidden value -- this seems aggressive. A more realistic assessment: +$20-40/share net benefit after costs and execution risk.
- **Severidad:** MODERATE -- The spinoff is likely net positive but not as dramatically as the R1 models. The upside is in the FV RANGE, not the BASE case.
- **Resolucion sugerida:** Do not include spinoff premium in FV. Treat it as a CATALYST for potential upside revision post-completion. The $470 FV is already conservative relative to SOTP.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Market Intelligence AI disruption | MI organic growth 5% only, mgmt acknowledges AI-native competitors, Capital IQ under pressure | MODERATE |
| 2 | Ratings normalization | Guided "low to mid-single digit" after +12% in 2025, refi boom fading | LOW |
| 3 | Mobility spinoff execution risk | Stranded costs unquantified, mgmt distraction, multiple expansion unlikely during deceleration | MODERATE |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 4 | FCF contraction despite revenue growth | FCF $5.46B vs $5.57B in 2024. Margin 39.2% to 35.6%. Capex/D&A 1.3x to 1.8x. | MODERATE |
| 5 | No informational edge vs consensus (Error #49) | R3 FV $470, consensus $540-560. 21/21 analysts Buy. Our view IS the market view with lower conviction. | MODERATE |
| 6 | DCF sensitivity extremely high | FV spread 88%, terminal value 74.5% of EV. Point estimates unreliable. | LOW |

### Riesgos No Modelados

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 7 | Receivables anomaly STILL UNRESOLVED | +20% vs +8% revenue = +12.1pp gap. KC#8 threshold already exceeded in first observation. Beneish DSRI 1.11x. | HIGH |
| 8 | Goodwill creep | 55.9% of assets (2022) to 59.6% (2025). Continued M&A adds goodwill without proportional tangible returns. | LOW |
| 9 | Capex intensity rising | 0.8x D&A (2022) to 1.8x (2025). AI investment consuming FCF. If permanent, margin expansion thesis fails. | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 10 | Q1 2026 earnings gate not yet cleared | Late April. Receivables + FCF trajectory are MUST-CONFIRM. Buying before = buying into unresolved uncertainty. | HIGH |
| 11 | Form 10 filing Q2 2026 | Could create short-term selling pressure from index rebalancing, uncertain tax treatment | LOW |

---

## Tabla de Tres Numeros

| Fuente | FV | Metodo |
|--------|-----|--------|
| FA thesis (R3) | $470 | EV/EBIT 24x (40%) + OEY 3.5% (35%) + DCF (25%), post-DA-1 resolution |
| Mercado | $424 | Current price |
| DA bajista | $375 | P/Normalized FCF 24x on $5.2B normalized FCF (35.5% margin on $14.6B 2026E revenue at low-end 6% growth) |

**FA > Market > DA:** Normal configuration. Genuine upside exists between market and FA view ($424 to $470 = 10.7% upside). The debate is about the SIZE of the MoS, not the DIRECTION. At $420 (SO trigger), MoS vs $470 = 10.6%. MoS vs DA bear = -12.0% (above DA bear). This means even the DA's bear case is not dramatically below the SO.

---

## Edge Assessment

- Analyst consensus PT: $540-560 (21 Buy, 0 Sell)
- Post-DA FV: $440
- Gap: $540 consensus vs $440 DA = -18.5% (we are more bearish than consensus)
- Our specific edge: Patience (waiting for $420 vs buying at $450+) + receivables gate (additional safety layer that consensus ignores) + conservative FCF margin assumption (35.5% flat vs consensus projecting expansion)
- If gap <10%: "WARNING: Edge is thin but REAL -- it is execution discipline, not informational advantage."

---

## VJ Ponderado por Probabilidad

Using updated scenario weights:
- Bear ($375, 30% prob): $112.50
- Base ($445, 45% prob): $200.25
- Bull ($560, 25% prob): $140.00
- **Expected Value: $453**

At $420 SO: MoS vs EV = 7.3%. At $424 market: MoS vs EV = 6.4%.

---

## Condiciones de Muerte Propuestas (New/Updated KCs)

- **KC#8 ESCALATION:** If Q1 2026 receivables growth STILL exceeds revenue growth by >10pp, escalate from GATE to active KILL evaluation. Two consecutive quarters of >10pp divergence = SELL signal (quality of earnings deterioration).
- **KC#9 (new):** Market Intelligence organic revenue growth turns negative for 2 consecutive quarters (signals AI displacement of Capital IQ)
- **KC#10 (new):** Post-spinoff RemainCo adjusted operating margin falls below 48% for 2 consecutive quarters (would indicate stranded costs are structural, not transitional)

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | 2 HIGH of 11 total |
| Desafios no resueltos por thesis | 3 (receivables, FCF trajectory, MI competitive position) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

SPGI is an exceptional franchise. The ratings duopoly and index monopoly are IMPENETRABLE for the foreseeable future (62-75% of revenue). The R3 FV of $470 is reasonable but NOT conservative -- it depends on margin expansion that has not materialized in the most recent year. The receivables anomaly is the single most important unresolved issue. The Q1 gate is ESSENTIAL and should NOT be removed under any circumstance.

Post-DA FV adjusted to $440 reflecting: (1) FCF margin flat at 35.5% rather than expanding, (2) revenue growth base case 6.5% rather than 7%, (3) no spinoff premium until completion. The correction from R3's $470 is -6.4%, which is MODEST -- this is a strong franchise where the DA's challenges are mostly about DEGREE of optimism, not DIRECTION of thesis.

**Post-DA FV: $440** (-6.4% from R3's $470)

---

## Recomendacion al Comite

1. **MAINTAIN the Q1 earnings gate.** This is the most important safety mechanism. If receivables normalize AND FCF trajectory is positive, deploy at $420.
2. **If $420 trigger hits BEFORE Q1 earnings (late April):** DO NOT deploy. The R4 committee set this gate for a reason. Wait. Price may drift lower, which would be better. Price may recover, in which case the opportunity cost is acceptable.
3. **If Q1 earnings clear the gate AND price is at/below $420:** Deploy EUR 400 (3.9% position). This is consistent with R4 sizing for borderline E[CAGR].
4. **If Q1 receivables are STILL divergent (+10pp above revenue):** Suspend SO. Downgrade from WATCHLIST to MONITOR. Re-evaluate at Q2 earnings.
5. **Post-DA E[CAGR] at $420:** Using $440 FV: ($440/$420)^(1/3) - 1 + 0.9% div + 3.5% buyback = 1.6% + 4.4% = ~6.0%. Add organic growth tailwind of ~3% not in FV (3-year compound above current trajectory): **~9-10% total E[CAGR]**. This is BELOW our 12% Tier A threshold. The investment case rests on (a) the franchise quality justifying lower E[CAGR], (b) the spinoff catalyst for value unlock, and (c) the position being small (3.9%).

---

## META-REFLECTION

### Dudas
- The biggest question is whether the Q1 earnings gate will clear. If receivables normalize (and I believe they PROBABLY will -- Q4 Ratings billing surge is the most likely explanation), SPGI becomes a clean buy at $420. If they do NOT normalize, the thesis has a genuine quality-of-earnings problem.
- The E[CAGR] at $420 post-DA ($440 FV) is only ~9-10%, which is below our 12% Tier A threshold. The R4 committee accepted 12.1% at R3's $470 FV. At $440, the math no longer works on pure E[CAGR]. The case becomes: "this is a fortress franchise at a fair price that we buy for quality, not discount."
- The previous DA (Feb 28) already covered most of these issues. The R3 resolved them reasonably. This refresh DA confirms the R3's approach was sound but slightly optimistic.

### Anomalias Detectadas
- **Yield anomaly in tool output:** price_checker.py shows 91.0% yield for SPGI, flagged as YIELD_ANOMALY. Actual dividend yield is ~0.9% ($3.88 / $424). This is a known yfinance data bug.
- **Goodwill creep:** 55.9% (2022) to 59.6% (2025) of total assets. The With Intelligence acquisition and other bolt-ons are adding goodwill faster than organic asset growth. Not alarming yet but worth monitoring.
- **FCF margin trajectory is inconsistent with thesis:** 22.5% (2022) -> 28.5% (2023) -> 39.2% (2024) -> 35.6% (2025). The 2024 figure looks like an OUTLIER (possible one-time working capital benefit). The "normalized" FCF margin is probably 33-36%, not 37.5% as R1 projected.

### Sugerencias para el Sistema
- **Receivables/Revenue divergence should be an AUTOMATIC flag in quality_scorer.py or narrative_checker.py**, not just a manual observation. Any ticker where receivables grow >10pp above revenue should get an automatic KC proposal.
- **E[CAGR] calculation should be SPLIT between valuation component and growth component** so that cases like TSM ($329 vs $290 FV, E[CAGR] 21%) are immediately visible as growth-only returns without valuation tailwind.

### Preguntas para el Orquestador
1. At $440 post-DA FV, the E[CAGR] at $420 is only ~9-10%. This is below the 12% Tier A threshold. Should the SO be lowered to $400 (where E[CAGR] would be ~11-12%) or should SPGI be approved at sub-threshold E[CAGR] on franchise quality grounds?
2. If price hits $420 BEFORE Q1 earnings, is the committee's gate binding? Or can the CIO override with conviction?
3. Should the Mobility spinoff catalyst be modeled into FV (which would raise it to ~$490-510) or excluded (which keeps it at $440)?

### Fuentes
- [SPGI Q4 2025 earnings plunge - FinancialContent](https://markets.financialcontent.com/stocks/article/marketminute-2026-2-10-a-crisis-of-expectations-s-and-p-global-shares-plunge-as-2026-outlook-falls-short)
- [SPGI 2026 guidance disappoints - Seeking Alpha](https://seekingalpha.com/news/4549419-sp-global-stock-drops-after-q4-earnings-2026-guidance-disappoint)
- [SPGI Mobility spinoff risks - Globe and Mail](https://www.theglobeandmail.com/investing/markets/stocks/SPGI/pressreleases/33846249/sp-globals-mobility-spin-off-navigating-uncertainties-and-potential-setbacks/)
- [SPGI AI concerns - Reuters/Investing.com](https://www.investing.com/news/economy-news/sp-global-forecasts-2026-profit-below-estimates-shares-plunge-4496477)
- [Capital IQ Pro AI enhancements - PR Newswire](https://www.prnewswire.com/news-releases/sp-global-enhances-capital-iq-pro-with-expanded-fixed-income-biopharma-and-private-markets-data-content-and-ai-capabilities-302711573.html)
- [S&P Global Mobility spinoff details - Stock Titan](https://www.stocktitan.net/news/SPGI/s-p-global-introduces-new-brand-identity-for-mobility-division-as-n4moygz3ndx0.html)
- [Receivables growth red flags - AnalystPrep CFA](https://analystprep.com/cfa-level-1-exam/financial-reporting-and-analysis/accounting-warning-signs/)
- [Credit ratings AI/blockchain - Moody's TIE](https://www.morningstar.com/news/business-wire/20260316806410/moodys-ratings-becomes-first-credit-rating-agency-to-bring-independent-credit-analysis-to-blockchain-financial-infrastructure)
- [AI disruption S&P, Moody's - Scuttleblurb](https://scuttleblurb.substack.com/p/spgi-mco-ai)

---

**Analysis Date:** 2026-03-21
**Framework:** v4.0

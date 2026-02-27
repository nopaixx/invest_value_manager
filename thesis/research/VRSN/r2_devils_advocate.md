# Counter-Analysis: VRSN (VeriSign, Inc.)

## Fecha: 2026-02-27

## Resumen Ejecutivo

The R1 thesis presents VeriSign as an unassailable monopoly with contractual pricing power and a wide moat. While the moat analysis is broadly correct, the thesis contains **several material omissions and optimistic assumptions** that, when challenged, reduce the Fair Value and narrow the margin of safety significantly. The most critical finding is that **Berkshire Hathaway sold 32.4% of its VRSN position in July 2025 at $267** -- a fact the thesis omits while citing the BRK holding as quality validation. Additionally, the thesis underestimates domain base fragility, overstates the sustainability of the FY2025 FCF margin jump, and does not adequately price in the untested demand elasticity of four consecutive 7% annual price increases. The thesis survives at a reduced FV, but the standing order at $200 provides inadequate margin against the bear case.

---

## Phase 0.5: Calibration

**Market Anchor:** At $224.50, the market implies 8.6% FCF growth for 5 years. Historical FCF CAGR is 10.0%. Gap: -1.4pp. The market is pricing VRSN slightly below historical delivery -- not at a significant discount.

**DA Historical Accuracy:** 23 total corrections, average -16.1%, median -14.1%. All negative. No outcomes measured yet (first review Aug 2026). Historical pattern: DA has NEVER increased a FV. This session I must be especially careful to avoid reflexive conservatism while still identifying genuine risks.

**Anchoring Principle:** The FA must prove the MARKET is wrong, not assume it. At $224.50 with implied 8.6% FCF growth, the market is pricing roughly base-case delivery. The FA's FV of $255 requires proving the market is 13.6% too pessimistic. I challenge whether that proof is sufficient.

---

## Asunciones Clave Desafiadas

### 1. Berkshire Hathaway Validates Quality (CRITICAL OMISSION)

- **FA's Claim:** "Berkshire Hathaway holds $2.2B (9.8% of VRSN). This is a top-20 BRK position. They understand franchise value and pricing power better than anyone."
- **Evidencia en contra:** **Berkshire sold 32.4% of its VRSN position on July 30, 2025, dumping 4.3M shares at $266.93.** This is the largest VeriSign reduction in Berkshire's history. Furthermore, **Todd Combs -- the investment manager believed responsible for the VRSN position -- LEFT Berkshire Hathaway in December 2025** to join JPMorgan Chase. Combs' departure raises the question of whether the remaining VRSN position is an orphaned holding under the new Berkshire portfolio management structure (Ted Weschler + Abel).
- **Severidad:** **CRITICAL** -- The thesis uses the Berkshire holding as a primary quality validator (mentioned 3 times). Omitting the largest-ever reduction in BRK's VRSN position, which happened at $267 (above the FA's FV of $255), materially misleads the investment committee. If Berkshire is SELLING at $267, our FV of $255 is not conservative -- it may be generous.
- **Resolucion sugerida:** Remove Berkshire as a quality validator. The signal is now AMBIGUOUS (massive sale at $267 in July, small buyback at $195-207 in Dec 2024, then Combs departed). If anything, Berkshire selling at $267 validates $255 as a CEILING, not a target.

### 2. FY2025 FCF Margin Jump Is Sustainable

- **FA's Claim:** FCF margin expanded from 56.2% to 64.5% (+830bps) and is used as the basis for forward projections.
- **Evidencia en contra:** The trailing 3-year average FCF margin is 58.3%. The +620bps jump (the FA calculates differently in different places) is the largest single-year expansion in VRSN's recent history. Management has guided elevated capex of $55-65M for 2026 (vs ~$40M typical run-rate) for "equipment refresh + AI demand," suggesting the low capex that boosted FY2025 FCF margin was one-time. Additionally, SGA costs rose 11.5% YoY in Q4 2025 vs revenue growth of 7.5% -- early margin compression signal.
- **Severidad:** **HIGH** -- The FA uses OEY at 4.2% as primary method (50% weight), calculated on FY2025 FCF of $1.07B. If FCF margin normalizes to 60% (midpoint of historical range), FY2025 normalized FCF would be ~$994M, reducing OEY-derived FV from $253 to ~$237.
- **Resolucion sugerida:** Use trailing 3-year average FCF margin (58.3%) or midpoint (60%) for base case, NOT the peak FY2025 figure. Use FY2025 as optimistic scenario.

### 3. Receivables +37.5% vs Revenue +6.4% Is Benign

- **FA's Claim:** The thesis acknowledges this anomaly in the meta-reflection but does not adjust FV or risk rating.
- **Evidencia en contra:** A 31pp divergence between receivables growth and revenue growth is a major red flag in any business. For a business with 88% gross margins and supposedly predictable cash flows from domain renewals, this divergence is especially concerning. Possible explanations include: (a) timing of Q4 domain renewal billing cycle, (b) extended payment terms to registrars (potentially to support rebate programs that inflate domain base growth), (c) revenue recognition pull-forward. The risk-identifier correctly flagged this as a suggested kill condition (KC-4). The FA's meta-reflection acknowledges it but does NOT adjust the FV or increase the risk rating.
- **Severidad:** **HIGH** -- Until explained, this casts doubt on revenue quality and FCF sustainability. If registrars are taking longer to pay (or VeriSign is extending terms to maintain domain base growth), the FCF quality is lower than stated.
- **Resolucion sugerida:** The investment committee should GATE this analysis on resolution of the receivables anomaly. Either explain it from 10-K disclosure or treat FCF as potentially overstated.

### 4. Four Consecutive 7% Price Increases (2027-2030) Will Not Destroy Demand

- **FA's Claim:** Revenue growth accelerates to 7-9% in 2027-2029 from contractual price increases. "VeriSign has ALWAYS increased prices to the maximum permitted."
- **Evidencia en contra:** Previous price increases were ONE increase per 6-year cycle (7% once every 6 years). The 2018 amendment changed the structure to allow 7% annually in the final 4 years. This has NEVER BEEN TESTED. Four consecutive 7% increases would raise the wholesale price from $10.26 to $13.45 -- a **31% cumulative increase in 4 years**. Historical evidence from the 2022-2024 period shows: (a) after the Sep 2021 price increase, first-renewal rate dropped to 50% for 2021-vintage registrations, (b) net .com additions dropped from 682K/month average in 2021 to 423K/month in early 2022, (c) the domain base DECLINED for 6 consecutive quarters from Q2 2023 to Q3 2024. The CircleID analysis notes that VeriSign faces "conflicting constraints: protecting revenue and margins threatened by slowdown or decline, while protecting its TLDs by maintaining competitive prices compared with country-code domains and new TLDs."
- **Severidad:** **HIGH** -- The price increases are contractually PERMITTED but not contractually REQUIRED. VeriSign could choose to take less than 7% if demand elasticity is worse than expected. The thesis models the full 7% as 85% probability. Given untested demand elasticity at cumulative 31% increases, this should be 65-70% probability at most. And even if taken, the volume response is uncertain.
- **Resolucion sugerida:** Model a scenario where VeriSign takes 5% instead of 7% (political/demand caution), with volume growth slowing to 1% as price pushes marginal domains to alternative TLDs. This gives ~6% revenue growth in 2027-2029 vs the FA's 9%.

### 5. Domain Base Growth Is Organic and Sustainable

- **FA's Claim:** .com returned to growth in 2025, domain base 173.5M growing at 2.6%.
- **Evidencia en contra:** Multiple sources indicate the 2025 "recovery" was significantly driven by rebate programs. Unstoppable Domains sold .com domains at $5 (below the $10.26 wholesale cost) generating ~20K monthly registrations. Bear analysts (Insider Monkey, Baird) note "YTD 2025 growth has been supported by high-churn registrars leveraging aggressive rebate programs, sometimes offering discounts of up to 50%." VeriSign itself restructured its rebate programs in 2025, suggesting they recognize the quality issue. Additionally, **approximately 30% of .com domains are estimated to be parked/inactive**, and Google's ban on AdSense for parked domains eliminated the economic rationale for a significant fraction of these. First-renewal rates for new registrations hover around 50% -- meaning half of new registrations churn within a year. This is NOT a healthy growth profile.
- **Severidad:** **MODERATE** -- The domain base IS growing, but the quality of growth is questionable. Rebate-driven registrations with 50% first-year churn artificially inflate the headline number. The sustainable growth rate may be closer to 1-1.5% than the 2.6% reported.
- **Resolucion sugerida:** Use 1.0-1.5% sustainable domain growth, not 2.0%. Factor in that rebate-driven registrations create a "treadmill" where VeriSign must spend more on incentives just to maintain the base.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | .com market share declining | .com share fell from ~50% to 42% of total domains over past decade. ngTLDs grew 13.5-15.9% YoY in 2024-2025 vs .com 2.6% | MODERATE |
| 2 | Rebate-driven growth unsustainable | Registrars selling below wholesale ($5 vs $10.26). 50% first-renewal churn on new domains. VeriSign restructured rebate programs acknowledging quality issue | MODERATE |
| 3 | Parked domain vulnerability | ~30% of .com domains estimated parked/inactive. Google AdSense ban eliminates economic rationale for monetization-parked subset | MODERATE |
| 4 | AI structural risk (long-term) | AI agents may increase DNS queries but decrease new domain registrations as businesses move to AI-native platforms. Currently net positive but genuinely uncertain at 5-10yr horizon | LOW |
| 5 | Moat correctly assessed as WIDE | The monopoly IS real. ICANN contract IS presumptive renewal. The regulatory structure IS entrenched. I cannot find credible evidence the moat will crack in 1-5 years | N/A (thesis confirmed) |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 6 | FV $255 anchored to peak FCF margin (64.5%) | Trailing 3yr avg 58.3%. FY2025 jump is largest in history. Elevated 2026 capex ($55-65M) will compress FCF margin. Using normalized FCF reduces FV by ~$15-20 | HIGH |
| 7 | OEY target of 4.2% too aggressive for 5% revenue grower | A monopoly utility with 5% revenue growth should trade at OEY 4.5-5.0%. At OEY 4.5%, FV = $237 (vs FA's $253). At OEY 5.0%, FV = $213 | HIGH |
| 8 | EV/EBIT at 20x on 2027E EBIT assumes full price increases | If price increases are 5% instead of 7%, FY2027E EBIT is $1,220M not $1,285M. At 19x (more appropriate for uncertain pricing power), FV = $247 | MODERATE |
| 9 | FA FV ($255) is BELOW Berkshire's selling price ($267) | If Berkshire -- with direct access to management, 34 years of relationship, and deep franchise understanding -- sold at $267, our FV of $255 may represent the informed ceiling | HIGH |
| 10 | Market is pricing VRSN correctly at base case | Reverse DCF shows implied 8.6% FCF growth vs historical 10%. The gap is only 1.4pp. This is NOT a significantly mispriced security | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 11 | Receivables anomaly unresolved | +37.5% receivables vs +6.4% revenue. No explanation in earnings call. Potential revenue quality deterioration or extended payment terms | HIGH |
| 12 | CEO selling pattern: 63 sells, 0 buys in 5 years | Bidzos has made 63 sale transactions and ZERO purchases in 5 years per SEC Form 4 filings. While holdings remain at 10.6%, the absence of ANY open-market purchases is a mild negative signal | LOW |
| 13 | Political/regulatory risk underweighted | Warren/Nadler NTIA/DOJ letter Nov 2024. Economic Liberties Project policy brief. Coalition letter. The 2018 amendment that enabled pricing power was a TRUMP administration decision. A different political alignment could revisit | MODERATE |
| 14 | Demand elasticity of consecutive 7% increases untested | Never tested in the 34-year history of the contract. Historical single 7% increases caused domain base declines and first-renewal rate drops to 50% | HIGH |
| 15 | Bear case ($185) may be too generous | The FA's bear case assumes 3.5% revenue growth (volume only). But if volume DECLINES 2% and there are no price increases (regulatory block), revenue grows 0-1%. At 16x EBIT on contracted margins, bear = ~$155-165 | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 16 | 7% price increase already priced in | Consensus analysts have $276.50 PT. The ICANN contract terms (including pricing) were publicly known since Nov 2024. The "catalyst" is already in the price | MODERATE |
| 17 | Todd Combs departure creates overhang uncertainty | The investment manager responsible for BRK's VRSN position left Berkshire in Dec 2025. New portfolio managers (Weschler + Abel) may trim "orphaned" positions | LOW |
| 18 | No near-term catalyst before Oct 2026 | First price increase not until Oct 2026. No earnings catalyst (Q4 2025 missed). Stock near 52-week low for a reason | MODERATE |
| 19 | SO at $200 is 10.9% below current price, 4.3% below 52-week low | Achievable with market correction but requires specific negative catalyst. In Fair-Value regime, this may take 3-6+ months | LOW |

---

## Conflictos con Otros Analisis

### Moat Assessment
- **Agreement:** WIDE moat classification is correct. I find no evidence the moat will crack in 1-5 years.
- **Disagreement:** Moat assessor gives QS Adjusted 91 (vs FA's 88). The 3-point discrepancy is minor and immaterial. However, both may overweight the monopoly position in a business with 5% revenue growth.

### Risk Assessment
- **Agreement:** MEDIUM risk rating is appropriate. The risk-identifier correctly identified the receivables anomaly and political risk.
- **Disagreement:** The risk-identifier's bear case analysis notes that if price increases are capped at inflation, the stock could decline 25-40%. The FA's bear case ($185) does not fully incorporate this scenario (using 3.5% growth, not 0-1%).
- **Key point:** The risk-identifier suggested KC-4 (receivables divergence monitoring). The FA's thesis does NOT include this KC. It should be added.

---

## Independent Bear-Case Valuation (Phase 3B)

### Method: Normalized EV/EBIT (Different from FA's primary OEY method)

**Bear assumptions:**
- Revenue growth: 4.0% (FY2026E, partial price increase only), 6.0% (FY2027-2029, 5% price + 1% volume -- below max), 3.0% (FY2030, no price hike year)
- Operating margin: 66.5% (current 67.7% minus SGA cost inflation observed in Q4)
- Normalized FCF margin: 60% (trailing 3yr average = 58.3%, give slight credit for pricing)
- EBIT multiple: 18x (appropriate for a low-growth monopoly utility with political overhang)
- Terminal growth: 2.0%

**Calculation:**
- FY2027E Revenue: $1,723M * 1.04 * 1.06 = $1,897M (conservative vs FA's $1,878M)
- FY2027E EBIT: $1,897M * 66.5% = $1,261M
- EV = 18x * $1,261M = $22.7B
- Net Debt: $1.22B
- Equity = $21.5B
- Shares: 92M
- **DA Bear FV = $234/share**

### Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $255 | OEY (50%) + EV/EBIT (30%) + Reverse DCF (20%) |
| Market | $224.50 | Current price |
| DA bear | $234 | Normalized EV/EBIT 18x on FY2027E with conservative assumptions |
| Berkshire selling price | $267 | Actual transaction Jul 30, 2025 |
| Consensus analyst PT | $276.50 | Mean of 4 analysts |

**Interpretation:** FA ($255) > DA Bear ($234) > Market ($224.50). Normal ordering. But the gap between FA and DA is only $21, and the gap between FA and Market is only $30.50. This is a narrow-upside situation. There is no informational edge -- the FA's FV is 8% below consensus, and the market is pricing roughly base-case delivery.

---

## Edge Assessment

- **Analyst consensus PT:** $276.50 (mean of 4 analysts: 3 Buy, 1 Hold)
- **Post-DA FV:** $240 (adjusted from $255, see below)
- **Gap:** $240 vs $276.50 = -13.2% (we are BELOW consensus)
- **Our specific edge:** The FA claims edge from modeling CONTRACTUAL price increases. But these are publicly known since Nov 2024 and already modeled by sell-side analysts. The consensus PT of $276.50 already incorporates price increases.
- **WARNING: No informational edge identified.** Our FV ($240 post-DA) is below consensus. We are not seeing something the market doesn't -- we are actually MORE cautious than the market. The "edge" claimed by the thesis (contractual price increases) is consensus knowledge.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | 6 of 19 (1 CRITICAL, 5 HIGH) |
| Desafios no resueltos por thesis | 6 (BRK sale, FCF margin, receivables, demand elasticity, FV anchoring, edge) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

**MODERATE COUNTER** -- The thesis has genuine gaps that require resolution before investment committee approval. The moat analysis is correct and the business IS high quality. However:

1. The CRITICAL omission of Berkshire's 32.4% position reduction at $267 invalidates using BRK as a quality validator and suggests our FV may be a ceiling, not a discount price.
2. The FCF margin jump is likely one-time, reducing the OEY-derived FV.
3. The receivables anomaly is unresolved and potentially signals revenue quality deterioration.
4. The demand elasticity of consecutive 7% price increases is untested and the thesis models full implementation at 85% probability.
5. There is NO identifiable informational edge -- our FV is BELOW sell-side consensus.

The thesis does NOT have fatal flaws. VeriSign IS a quality compounder with a genuine monopoly. The question is whether the current price ($224.50) already reflects this quality, and whether the SO at $200 provides sufficient margin of safety given the unresolved risks.

### FV Adjustment Recommendation

| Adjustment | Impact | Rationale |
|------------|--------|-----------|
| FCF margin normalization (64.5% -> 60%) | -$15 | Use trailing 3yr avg, not peak |
| BRK selling price ceiling ($267 anchor) | -$0 | Directional only, no formula adjustment |
| Receivables quality discount | -$0 | Cannot quantify until resolved; flag as GATE |
| Price increase probability (85% -> 70%) | -$5 | Untested consecutive increases + political risk |
| Net adjustment | **-$15 to -$20** | |
| **Post-DA FV** | **$235-240** | Down from $255 |

At Post-DA FV of $240:
- At $224.50 (current): MoS = 6.5% -- INSUFFICIENT for any Tier
- At $200 (SO): MoS = 16.7% -- Low-end acceptable for Tier A monopoly
- E[CAGR] at $200: ~10.5% (below 12% threshold)
- E[CAGR] at $190: ~12.0% (at threshold)

---

## Recomendacion al Investment Committee

1. **RESOLVE receivables anomaly (GATE).** Check 10-K disclosure for explanation. If timing-related, remove concern. If structural, add KC-4.

2. **Acknowledge Berkshire's position reduction.** Do NOT use BRK as quality validator. The signal is ambiguous at best, negative at worst.

3. **Normalize FCF margin.** Use 60% for base case, not 64.5%. This gives FV $235-240.

4. **Consider lowering SO from $200 to $190.** At post-DA FV of $240, a $200 entry gives only 16.7% MoS and ~10.5% E[CAGR] -- below Tier A threshold. At $190, MoS = 20.8% and E[CAGR] = 12.0%.

5. **Acknowledge absence of informational edge.** This is a well-analyzed, well-covered monopoly. Our thesis is NOT differentiated from consensus. This doesn't make it wrong, but it means we should demand higher MoS to compensate for lack of edge.

6. **The quality IS real.** VeriSign is genuinely a Tier A compounder. The moat is wide and durable. I am not challenging the quality -- I am challenging the PRICE at which quality becomes investable. At $190-200 with a post-DA FV of $235-240, this can be a good position. At $225, it is fairly valued.

---

## META-REFLECTION

### Dudas/Incertidumbres
- The receivables anomaly is the single biggest unresolved question. I could not find any management explanation in the Q4 earnings call or 10-K disclosure through web search. This could be entirely benign (Q4 billing timing, registry fee invoicing cycle) or could signal deteriorating registrar payment behavior.
- The Berkshire data point is powerful but requires nuance: Berkshire sold at $267 (likely Combs-driven, pre-departure), then bought a small amount back at $195-207 in Dec 2024 (who initiated this?). The net signal is ambiguous but leans negative given the massive size of the July sale vs the small December purchase.
- I may be underweighting the moat's pricing power resilience. Domain renewals at $10.26/year are genuinely trivial for any operating business. The demand elasticity risk may be concentrated in speculative/parked domains (which arguably SHOULD churn) while core business domains are perfectly inelastic.

### Limitaciones de Este Analisis
- Could not access Seeking Alpha bear case articles (paywall/403). Multiple detailed bear analyses exist that I could not read in full.
- Could not access VeriSign's 10-K to investigate the receivables anomaly directly.
- The parked domain percentage (30%) is an industry estimate, not a VRSN-specific disclosure. VeriSign says only 2% is "parked for monetization" but the broader inactive base is uncertain.
- Demand elasticity for consecutive 7% increases is genuinely untested -- no one knows the answer, including VeriSign management.

### Sugerencias para el Sistema
- For monopoly/utility businesses, the DA should always compare the FA's FV to known institutional selling prices. If Berkshire is selling at $X, our FV should be scrutinized against that number.
- The Berkshire-as-validator pattern is common across our theses. The DA should always check latest 13F for position changes, not just holdings.
- Add automated 13F position change detection to the smart_money tool for tracked funds + stocks in pipeline.

### Preguntas para Orchestrator
1. Can we access the VRSN 10-K (FY2025) to resolve the receivables anomaly? This is the single most impactful unresolved question.
2. Should we adjust the SO from $200 to $190 given post-DA FV of $235-240? At $200 the E[CAGR] is only ~10.5% vs our 12% Tier A threshold.
3. The Berkshire sale at $267 is a CRITICAL omission in the R1 thesis. Should this trigger a review of how our R1 agents use institutional holder data (check for recent CHANGES, not just current holdings)?

---

**Sources consulted:**

- [VeriSign Bear Case Theory (Insider Monkey)](https://www.insidermonkey.com/blog/verisign-inc-vrsn-a-bear-case-theory-1640599/)
- [Warren/Nadler Letter to NTIA/DOJ on VeriSign Pricing](https://www.warren.senate.gov/imo/media/doc/letter_to_ntia_and_doj_re_verisigns_comwebsiteprices.pdf)
- [Economic Liberties: Breaking VeriSign's Monopoly](https://www.economicliberties.us/press-release/ntia-and-doj-must-break-verisigns-monopoly-power-over-domain-names-advocates-urge/)
- [ICANN .com Contract Extension (Nov 2024)](https://domainnamewire.com/2024/11/27/verisign-inks-com-contract-extension-with-icann/)
- [VeriSign .com Price Increases in 2026](https://domainnamewire.com/2025/11/19/verisign-can-increase-com-prices-in-2026/)
- [2025 in Review: .com Returns to Growth](https://domainnamewire.com/2025/12/30/2025-in-review-com-returns-to-growth/)
- [Price Increases for .COM and .NET: Impact Analysis (CircleID)](https://circleid.com/posts/20221007-price-increases-for-.com-and-.net-the-generated-impact-on-performance-of-two-tlds)
- [Domain Industry 2025: Landscape and Key Data](https://circleid.com/posts/domain-industry-2025-current-landscape-and-key-market-data)
- [VeriSign 2025 Performance and 2026 Outlook (ainvest)](https://www.ainvest.com/news/verisign-2025-performance-2026-outlook-assessing-pricing-power-infrastructure-expansion-valuation-realism-2601/)
- [Todd Combs Leaves Berkshire for JPMorgan (CNBC)](https://www.cnbc.com/2025/12/08/berkshire-hathaways-todd-combs-investment-lieutenant-to-buffett-and-geico-ceo-is-leaving-for-jpmorgan.html)
- [Berkshire Hathaway VRSN Transactions (StockCircle)](https://stockcircle.com/portfolio/warren-buffett/vrsn/transactions)
- [VeriSign Q4 2025 Earnings Call (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/02/05/verisign-vrsn-q4-2025-earnings-call-transcript/)
- [VeriSign Business Model 2026 (MacroHint)](https://macrohint.com/verisign-business-model-2026-the-internets-tollbooth/)
- [Hostinger Domain Name Statistics 2026](https://www.hostinger.com/tutorials/domain-name-statistics)
- [CEO Bidzos Insider Selling History (GuruFocus)](https://www.gurufocus.com/insider/5547/d-james-bidzos)
- [Global Domain Report 2025 (SIDN/Openprovider)](https://www.sidn.nl/en/news-and-blogs/global-domain-report-2025-trends-and-sales-in-domains)

# Counter-Analysis: CP (Canadian Pacific Kansas City)

## Fecha: 2026-03-21

## Market Anchor (Fase 0.5 Calibration)

| Metric | Value |
|--------|-------|
| Current Price | $78.24 (T1: price_checker.py) |
| FA Thesis FV | $72 |
| Reverse DCF implied FCF growth | 27.8%/yr for 5 years |
| Historical FCF CAGR (4yr) | -5.7%/yr |
| Gap (implied vs historical) | -33.5pp -- market expects massive FCF acceleration |
| Consensus analyst PT | ~$92-95 USD |

**Key observation:** The reverse DCF shows the market at $78.24 already prices in 27.8% annual FCF growth -- far above the historical -5.7% FCF CAGR. This is a market that is ALREADY pricing in synergy success and volume recovery. The FA's thesis FV of $72 is BELOW market, correctly identifying overvaluation. However, the FA's base case FV of $75 is suspiciously close to the current price -- suggesting the FA may be anchoring to the market rather than deriving independently.

---

## Resumen Ejecutivo

The thesis correctly identifies CPKC as a unique infrastructure asset with a wide moat and properly concludes it is overvalued at $78. The WATCHLIST verdict is sound. However, the thesis contains several vulnerabilities: (1) a +15 point QS adjustment that is the largest in fund history and may be aggressive, (2) understatement of tariff risk given the USMCA review starting July 2026, (3) overly optimistic OR trajectory assumptions, and (4) the $72 FV may still be too generous given the ROIC-WACC spread is only 0.4pp. The thesis survives scrutiny but the entry range of $65-68 may need to be lowered to $58-63.

---

## Asunciones Clave Desafiadas

### 1. QS Adjustment of +15 Points (49 to 64) -- "Merger Distortion" Justification

- **FA's claim:** Tool QS of 49 (Tier C) understates quality because post-merger ROIC is temporarily depressed. Pre-merger CP Rail had ROIC 13-15%. Adjustment justified by goodwill distortion, unique market position, and ROIC persistence history.
- **Evidence against:**
  - This is the LARGEST QS adjustment in the fund's history. Previous adjustments have been +5 to +8 points with strict quantitative justification (Error #43 protocol).
  - The +8 points for "Market Position" is valid -- CPKC is genuinely #1 in tri-national rail. But this is a DATA INPUT issue with the tool (it defaults to 0 for unknown positions), not a quality distortion.
  - The +4 for ROIC Spread relies on FUTURE improvement, not current data. Pre-merger CP Rail ROIC was 13-15%, but the MERGED entity has a fundamentally different capital base ($22B goodwill, $23.4B net debt). There is no guarantee the merged entity achieves pre-merger ROIC levels. The goodwill may represent permanent capital inefficiency if synergies plateau.
  - The +3 for ROIC Persistence uses pre-merger data for a fundamentally different entity. Post-merger, CPKC has 3 years of history: -2.3%, 5.3%, 6.0%. That is NOT persistence of high ROIC.
  - **Current ROIC of 6.0% vs WACC of 8.9% = -2.9pp spread.** Even adjusting for goodwill (ROIC ~10-11%), the spread is 1-2pp. For a Tier B company, this is borderline.
  - FY2025 ROIC improvement from 5.3% to 6.0% is only +70bps. At this rate, ROIC reaches WACC in ~4 years. The thesis assumes acceleration from synergies, but that is speculative.
- **Severidad:** **MODERATE** -- The adjustment direction is correct (tool understates quality for post-merger situations), but the magnitude may be 5-8 points too generous. A more conservative adjustment of +8-10 (to QS 57-59) would keep CP in Tier B but with lower conviction. The practical impact is limited since the thesis already concludes WATCHLIST.
- **Resolucion sugerida:** Committee should evaluate whether the merged entity deserves credit for pre-merger ROIC history. The merged entity is a DIFFERENT company with different capital structure, cost base, and competitive dynamics. QS 57-60 (Tier B) is more defensible than 64.

### 2. Tariff Risk is Understated -- USMCA Review July 2026 is a Material Overhang

- **FA's claim:** ~70% of cross-border rail traffic is USMCA-compliant and therefore exempt from tariffs. Tariff impact is "real but overstated by the market." Nearshoring is a structural tailwind.
- **Evidence against:**
  - **USMCA formal review begins July 2026** -- this is not a routine assessment. The Trump administration is seeking additional concessions, and Mexico/Canada face demands on non-trade issues (migration, fentanyl, defense). The review could result in USMCA modification or termination.
  - **Trump already imposed 25% tariffs on autos/auto parts regardless of USMCA compliance** (March 2025 proclamation). This sets precedent for bypassing USMCA exemptions on specific categories.
  - **Mexico was threatened with 30-35% blanket tariffs** in July 2025 (paused 90 days). The pause mechanism creates recurring uncertainty every quarter.
  - **Auto sector is ~10% of CPKC revenue and "fastest growing post-merger."** The auto tariff exemption bypass directly hits CPKC's growth segment.
  - The FA's 40% probability of "tariff resolution" may be too optimistic. Trump has consistently escalated rather than resolved trade disputes. A more realistic assessment: 20-25% full resolution, 50% status quo (continued uncertainty), 25-30% escalation (USMCA renegotiation with worse terms for rail transit).
  - **FreightWaves warns**: "Tariff noise to stay loud in 2026" -- cross-border freight faces "uneven demand, tariff uncertainty, and operational challenges."
  - Mexico's own 2026 tariff reform (1,400+ new tariffs on non-FTA goods) may indirectly affect supply chains feeding into CPKC's network.
- **Severidad:** **HIGH** -- The USMCA review is the single biggest risk to the thesis and the FA's 40% resolution probability appears optimistic. The tariff uncertainty creates an overhang that may persist through 2026-2027, compressing the multiple the market is willing to pay.
- **Resolucion sugerida:** Committee should stress-test the bear case with USMCA renegotiation resulting in weaker cross-border provisions. The bear case should include a scenario where CPKC's Mexico advantage is partially eroded by higher compliance costs, border delays, and tariff uncertainty reducing shipper willingness to invest in cross-border supply chains.

### 3. Operating Ratio Trajectory -- Is 55-56% by 2028 Realistic?

- **FA's claim:** OR trajectory from 59.9% (FY2025 full year) toward 55-56% by 2028, driven by synergies, volume leverage, and new locomotives.
- **Evidence against:**
  - Q4 2025 OR of 55.9% is a SEASONAL best quarter, not a sustainable run-rate. Q4 is typically the strongest quarter for rail (harvest, holiday shipping). Full-year 2025 was 59.9%.
  - **UNP, the most efficient US Class I, had FY2025 adjusted OR of 59.3%.** CPKC's Q4 of 55.9% beating UNP's full-year suggests either exceptional execution OR a favorable seasonal/one-time quarter. Sustaining Q4 levels as a full-year average requires extraordinary consistency.
  - The claim that CPKC reaches 55-56% OR on a full-year basis would make it the MOST efficient Class I railroad in North America by a significant margin -- surpassing UNP which has been optimizing for decades without merger integration drag.
  - **CSX reported FY2025 OR of 66.8%.** The range across Class I railroads is wide. CPKC achieving best-in-class from a starting point of merger integration is ambitious.
  - Synergy-driven OR improvement faces diminishing returns. The easy savings (headcount reduction, facility consolidation) are captured first. Remaining synergies are revenue-based (harder to realize, dependent on volumes).
  - Rising oil prices ($95-100 WTI per the thesis) directly pressure fuel costs (10-12% of operating costs). While fuel surcharges offset partially, there is always a timing lag and imperfect pass-through.
  - **Labor costs are the largest expense** for railroads. US rail labor negotiations are ongoing and unions are pushing for higher wages and better conditions post-2022 disputes. A 3-4% wage increase across CPKC's workforce would add 100-150bps to OR.
- **Severidad:** **MODERATE** -- Q4 2025's 55.9% OR is impressive but likely represents a peak quarter. Full-year 57-58% by 2028 is more realistic than 55-56%. The thesis's base case EBIT of $6.5B (42% margin on implied ~$15.5B revenue) is achievable but the bull case EBIT of $7.2B is aggressive.
- **Resolucion sugerida:** Use 58% OR as base case rather than 57%, and 60% as bear case rather than 59%. This reduces base case EBIT by ~$150-200M and narrows the FV range modestly.

### 4. Organic Revenue Growth of 5-7% is Optimistic Given Current Freight Environment

- **FA's claim:** 5-7% organic revenue growth from volume (2-3% GDP-linked), pricing (2-3%), market share (0.5-1%), and synergy revenue (0.5-1%).
- **Evidence against:**
  - **FY2025 organic revenue growth was just 3.7%** -- below the thesis's 5-7% range.
  - **US rail volumes in early 2026 are declining**: week ending Feb 7 showed -3.2% carloads, -4.8% total carloads vs prior year. Intermodal -2%.
  - **AAR data shows mixed signals**: January 2026 had some recovery (+4.4% carloads) but February weakened again. The freight recession in LTL/trucking spills into rail.
  - **CPKC's own 2026 guidance is "mid-single-digit RTM growth"** -- which translates to 4-6%, not 5-7%. Revenue growth is typically lower than RTM growth due to mix shifts.
  - The nearshoring tailwind is REAL but SLOW. Mexico FDI takes 2-3 years to translate into rail freight volumes (factory construction, supply chain establishment). This is a 2027-2030 catalyst, not a 2026 catalyst.
  - US industrial production has been flat to declining. Manufacturing PMI remains sub-50 in most readings. The cyclical component of rail volumes faces headwinds.
- **Severidad:** **MODERATE** -- The thesis's growth assumption is modestly aggressive. 4-5% organic revenue growth is more realistic than 5-7% for 2026-2027. This reduces the base case FV by $3-5 per share.
- **Resolucion sugerida:** Adjust organic revenue growth assumption to 4-5% for base case, 2-3% for bear case. The 5-7% range should be reserved for the bull case when tariff resolution and nearshoring materialize simultaneously.

### 5. ROIC-WACC Spread is Dangerously Thin

- **FA's claim:** Pre-merger CP Rail ROIC was 13-15%. Post-merger depression is temporary. Adjusting for goodwill, ROIC is ~10-11% vs WACC 8.9%.
- **Evidence against:**
  - **Reported ROIC: 6.0%. WACC: 8.9%. Spread: -2.9pp.** The company is currently DESTROYING value on its invested capital.
  - Even with the FA's generous goodwill adjustment (removing ~$20B from invested capital), ROIC is ~10-11% vs WACC 8.9% = spread of 1-2pp. This is THIN for an infrastructure company that should have strong pricing power and natural monopoly characteristics.
  - For comparison: UNP's ROIC is typically 15-18%, CNI 12-15%. CPKC's post-merger ROIC is the weakest among Class I railroads.
  - The $22B goodwill is NOT an accounting fiction -- it represents the REAL PRICE PAID for KCS. If CPKC cannot earn adequate returns on the full invested capital (including goodwill), the merger was value-destructive. Adjusting for goodwill is analytically useful but does not change the economic reality of capital deployed.
  - **Interest expense is substantial.** The recent $1.2B debt offering (March 2026) adds to the $23.4B net debt pile. Even with refinancing at slightly lower rates, interest expense consumes ~$1.0-1.1B annually -- a significant drag on returns.
  - **Value creation test:** ROIC > WACC is the minimum threshold for value creation. CPKC fails this test on reported numbers and barely passes on adjusted numbers. A Tier B stock should demonstrate clear value creation, not marginal value creation.
- **Severidad:** **HIGH** -- The thin ROIC-WACC spread means CPKC is not currently earning its cost of capital. The thesis bets on future improvement, but this is not yet demonstrated on the merged capital base. If synergies plateau at current levels or volume growth disappoints, ROIC may remain below WACC for years.
- **Resolucion sugerida:** Committee should require evidence that ROIC is on a clear trajectory to exceed WACC by at least 3pp before approving a buy. The FV should be discounted further to reflect the risk that the merged entity never achieves pre-merger return levels.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | QS +15 adjustment is historically unprecedented and may be +5-8 points too generous | Largest adjustment in fund history; relies on pre-merger data for different entity; current ROIC 6% vs WACC 8.9% | MODERATE |
| 2 | Moat durability -- UNP-NSC merger could create partial competitor | Feb 2026 filing for $85B UNP-NSC merger; if approved with Mexican access, erodes CPKC's unique position | LOW |
| 3 | 19.6% revenue CAGR inflated by merger consolidation; organic growth only 3.7% | QS Growth score 10/10 based on inflated merger CAGR; organic growth modest | MODERATE |
| 4 | Labor cost risk underestimated | US rail unions pushing for higher wages; 3-4% increase adds 100-150bps to OR; not discussed in thesis | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 5 | ROIC-WACC spread of -2.9pp (reported) or +1-2pp (adjusted) is dangerously thin for Tier B | Only Class I railroad with ROIC < WACC; value destruction on reported basis | HIGH |
| 6 | OR trajectory of 55-56% by 2028 would make CPKC best-in-class -- aggressive assumption | Q4 2025 55.9% is seasonal peak; UNP full-year 59.3% after decades of optimization; 57-58% more realistic | MODERATE |
| 7 | Organic revenue growth assumption of 5-7% exceeds actual FY2025 delivery of 3.7% | US rail volumes declining early 2026; CPKC's own guidance is "mid-single-digit" RTM growth | MODERATE |
| 8 | DCF tool output ($16.33) correctly flagged as unreliable -- but this SHOULD inform caution | When a standard DCF produces $16 for a $78 stock, it signals the market is pricing in enormous improvement | LOW |
| 9 | Consensus PT ~$92-95 vs FA FV $72 -- FA is more conservative than consensus but our "edge" is unclear | Gap between our FV and consensus is $20-23; we need to identify what we know that consensus doesn't | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 10 | USMCA review July 2026 is the single biggest risk and is insufficiently stressed | Formal review + Trump seeking concessions + precedent of bypassing USMCA for autos | HIGH |
| 11 | New $1.2B debt offering (March 2026) increases debt load during uncertain environment | $23.4B+ net debt; interest expense ~$1B/yr; leverage 2.9x+ | MODERATE |
| 12 | US rail volumes declining early 2026 -- freight recession risk not reflected in growth assumptions | -3.2% carloads week of Feb 7, -4.8% total; LTL freight recession ongoing | MODERATE |
| 13 | Insider selling detected (14,845 shares Jan 2026) -- minor but thesis claims "no significant selling" | John Kenneth Brooks sold shares Jan 30 2026; thesis states no selling detected | LOW |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 14 | USMCA review in July 2026 creates a 3-6 month window of maximum uncertainty | If entering at $65-68, the USMCA review could push stock to $55-60 | MODERATE |
| 15 | Q1 2026 earnings due April -- early 2026 volume declines may disappoint | February volume data shows weakness; if Q1 misses, stock could gap down to entry zone | LOW |

---

## Independent Bear-Case Valuation

### Method: EV/EBIT with Bear Assumptions

Assumptions:
- FY2026E EBIT: $6.0B (flat vs FY2025, no synergy benefit, tariff headwinds)
- Multiple: 11x (bear case -- trade war discount, below peer average)
- Net Debt: $24.6B (including March 2026 $1.2B offering, partial paydown of existing)
- Shares: 898M

Calculation:
- EV = $6.0B x 11x = $66.0B
- Equity = $66.0B - $24.6B = $41.4B
- FV/share = $41.4B / 898M = **$46**

### Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $72 | EV/EBIT 60% + OEY 40%, anti-bullish-bias weighted |
| Market | $78.24 | Current price |
| DA bear | $46 | EV/EBIT 11x on flat EBIT, including new debt |

**Interpretation:** FA > DA bear, but Market > FA. This is a "correctly identified overvaluation" situation. Both the FA and DA agree the stock is currently overvalued. The debate is about where fair value lies ($46-72 range) and what entry price provides adequate safety.

The FA's entry range of $65-68 falls between DA bear ($46) and FA FV ($72). Given the risks identified above, a more conservative entry of $58-63 may be warranted -- this provides:
- 10-15% MoS vs FA FV of $72
- 26-37% buffer above DA bear of $46
- Achievable on USMCA escalation or Q1 2026 earnings miss

---

## Conflictos con Otros Analisis

No moat_assessment.md or risk_assessment.md files exist for CP. The thesis was produced as a standalone R1 by fundamental-analyst.

**Conflict with QS Tool:** The tool produces QS 49 (Tier C). The FA adjusts to 64 (Tier B). This is a material discrepancy. If QS remains at 49 (Tier C), the required MoS increases to ~30-40% per precedents, implying entry at $43-50 -- far below current levels and potentially too conservative for a genuine infrastructure moat.

**Resolution:** The truth likely lies between the tool's 49 and the FA's 64. QS 55-60 (low Tier B) is defensible, accepting the market position adjustment (+8) and partial ROIC trajectory credit (+3-5) but discounting the ROIC spread adjustment since the merged entity has not yet proven it can earn above WACC.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | 2 of 15 |
| Desafios MODERATE | 9 of 15 |
| Desafios LOW | 4 of 15 |
| Desafios no resueltos por thesis | 5 (tariff depth, ROIC spread concern, OR trajectory, volume decline, entry range) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

**MODERATE COUNTER:** The thesis has legitimate gaps. The WATCHLIST verdict is correct and should be maintained. Key adjustments needed:

1. **Lower QS to 57-60** (from 64) -- still Tier B but with reduced conviction
2. **Lower entry range to $58-63** (from $65-68) -- accounts for USMCA risk and ROIC concerns
3. **Increase bear case probability to 30-35%** (from 25%) -- USMCA review + volume headwinds
4. **Adjust organic growth to 4-5%** (from 5-7%) -- consistent with actual FY2025 delivery and 2026 guidance

## Edge Assessment

- Analyst consensus PT: $92-95 (source: public.com, MarketBeat, TipRanks)
- Post-DA FV: $65-68 (adjusted from FA's $72, incorporating DA bear weighting)
- Gap: -28 to -35% vs consensus
- Our specific edge: We see the USMCA review as a more material risk than consensus, and we are not willing to pay for synergy success that has not yet been demonstrated in ROIC terms. Our conservatism on tariff risk is a differentiator.
- WARNING: Gap vs consensus is large (>25%), which could mean either (a) we have genuine insight about tariff risk, or (b) we are being too conservative about a world-class infrastructure asset. The moat IS wide. The question is pricing.

## Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $72 | EV/EBIT 60% + OEY 40%, anti-bullish-bias weighted |
| Market | $78.24 | Current price |
| DA bear | $46 | EV/EBIT 11x on flat EBIT |

## Recomendacion al Investment Committee

1. **Maintain WATCHLIST verdict** -- the thesis is directionally correct that CP is overvalued at $78.
2. **Lower entry range to $58-63** from $65-68, primarily to account for USMCA review risk (July 2026) which could create a window of significant uncertainty.
3. **Require sector view creation** before advancing to R3/R4 -- no `world/sectors/rail-transport.md` exists (Error #30 hard gate).
4. **Monitor USMCA review developments closely** -- this is the primary catalyst both for risk (escalation) and opportunity (resolution creating entry point).
5. **Reassess QS adjustment magnitude** -- the +15 is directionally correct but likely +5-8 too generous. QS 57-60 is more defensible.
6. **Verify ROIC trajectory** at Q1 2026 earnings -- if ROIC does not improve above 7% (closer to WACC), the value creation thesis weakens materially.
7. **Track US rail volume data weekly** -- if volume declines persist through Q1 2026, the revenue growth assumption needs downward revision.

---

## META-REFLECTION

### Dudas/Incertidumbres
- The QS adjustment debate is genuine -- the tool IS wrong about market position (0/8 for the only tri-national railroad is clearly an error), but how much additional credit for ROIC trajectory is appropriate for a 3-year-old merged entity is subjective.
- My bear case EBIT of $6.0B may be too conservative -- the company has demonstrated strong operational execution. But for a DA bear case, conservatism is the point.
- The USMCA review is a known event with uncertain outcome. My 20-25% resolution probability may itself be too pessimistic or optimistic -- trade negotiations are inherently unpredictable.

### Limitaciones de Este Analisis
- No access to CPKC's 10-K filing for detailed segment revenue breakdown by country
- Limited visibility into actual USMCA compliance rates for CPKC's specific freight mix (the "70% USMCA-compliant" claim from the thesis could not be independently verified)
- Unable to verify the $1.2B synergy run-rate from primary sources (relied on press releases and earnings summaries)

### Sugerencias para el Sistema
- The dcf_calculator.py's reverse mode produces a useful anchor: $78.24 requires 27.8% FCF growth. This should be prominently featured in all theses for post-merger companies where recent FCF is distorted.
- Consider adding a "post-merger adjustment" flag to quality_scorer.py that automatically triggers when a company has completed a major acquisition within 5 years, prompting the analyst to review and adjust.

### Preguntas para Orchestrator
1. Should the USMCA review (July 2026) be added to state/calendar.yaml as a macro event affecting CP? This is the primary catalyst for both risk and entry opportunity.
2. Is a QS adjustment of +15 acceptable under Error #43 protocol, or should this be capped at +10 pending proof of ROIC improvement above WACC?
3. Should we create `world/sectors/rail-transport.md` proactively, or wait until CP advances past WATCHLIST? Error #30 requires it for committee, but creating it now would also benefit any future Class I railroad analysis.

---

Sources consulted:
- [CSIS: USMCA Review 2026](https://www.csis.org/analysis/usmca-review-2026)
- [Brookings: USMCA Forward 2026](https://www.brookings.edu/articles/foreword-usmca-forward-2026/)
- [Baker Institute: Strategic Priorities for USMCA Review](https://www.bakerinstitute.org/research/strategic-priorities-2026-usmca-review)
- [FreightWaves: Tariff noise in 2026](https://www.freightwaves.com/news/borderlands-mexico-tariff-noise-to-stay-loud-in-2026-flexport-warns-importers)
- [CPKC Investor Relations: Record PSR margins](https://investor.cpkcr.com/news/press-release-details/2026/CPKC-showcases-strength-of-Precision-Scheduled-Railroading-delivers-record-margins/default.aspx)
- [Progressive Railroading: CPKC Q4/FY2025 results](https://www.progressiverailroading.com/canadian_pacific_kansas_city/news/CPKCs-Creel-cites-PSR-for-lifting-Q4-full-year-2025-results--76252)
- [Loop Capital cuts CPKC rating on tariff news](https://www.investing.com/news/analyst-ratings/loop-capital-cuts-cpkc-stock-rating-following-tariff-news-93CH-3845598)
- [CPKC $1.2B debt offering March 2026](https://www.prnewswire.com/news-releases/cpkc-announces-us-1-2-billion-debt-offering-302704607.html)
- [Railway News: US rail volume decline Feb 2026](https://railwaynews.net/north-american-rail-reports-u-s-3-2-volume-decline-early-feb.html)
- [MarketBeat: CP insider trades](https://www.marketbeat.com/stocks/TSE/CP/insider-trades/)
- [Ticker Report: CP insider selling 14,845 shares](https://www.tickerreport.com/banking-finance/13347490/insider-selling-canadian-pacific-kansas-city-tsecp-insider-sells-14845-shares-of-stock.html)

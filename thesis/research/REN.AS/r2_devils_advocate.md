# Counter-Analysis: REN.AS (RELX PLC)

## Fecha: 2026-02-20

---

## Resumen Ejecutivo

The R1 thesis for RELX is well-constructed and the business quality is genuinely high. However, the thesis contains several materially optimistic assumptions: (1) the claim that LexisNexis is "#1 in legal information" is contradicted by market share data showing Westlaw at 34% vs Lexis Advance at 8%; (2) the WACC of 7.5% is aggressively low -- the analyst rejected the tool's 9% and substituted a manually derived 7.5% that inflates DCF by ~30%; (3) Open Access regulation is a more imminent threat to Elsevier than the thesis acknowledges, with UK universities already cancelling deals in early 2026; (4) the "AI is a tailwind" narrative, while partially correct, ignores the pricing cannibalization risk from Harvey partnership and the per-seat erosion dynamic documented in our own L-12 lesson. The thesis correctly identifies RELX as a quality compounder but the FV of EUR 33.50 is too generous. Bear-adjusted FV: EUR 26-28.

**Verdict: MODERATE COUNTER (11/19)**

---

## Asunciones Clave Desafiadas

### 1. "LexisNexis is #1 in Legal Information"

- **Thesis claim:** "RELX is #1 in legal information (LexisNexis vs Thomson Reuters Westlaw). Duopoly."
- **Evidence against:** 6sense market share data (2024-2025) shows Westlaw at 33.94% market share vs Lexis Advance at only 8.18%. Casetext (acquired by Thomson Reuters) has 31.04%. LexisNexis is NOT #1 in legal research -- it is a distant third. The "duopoly" narrative is outdated; it is now a three-way race with Clio/vLex entering via $1B acquisition.
- **Nuance:** These market share figures may measure technology adoption (installations/deployments) rather than revenue. RELX's Legal segment generated ~GBP 2.1B in revenue, while Thomson Reuters Legal revenue was ~$3.1B (USD). By revenue, LexisNexis is #2, not #1. The QS adjustment of +7 for market position (claiming 7/8) is overstated if LexisNexis is #2-3 rather than #1.
- **Severity:** HIGH
- **Resolution:** Reduce market position adjustment from +7 to +5 (consistent with #2-3 position). QS Adjusted becomes 76 instead of 78. Still Tier A but LOWER within it. The duopoly is real by revenue but increasingly threatened by AI-native entrants.

### 2. "AI is a Pure Tailwind for RELX"

- **Thesis claim:** "The market is WRONG about RELX and AI. AI is a TAILWIND." and "RELX's data IS the input to AI."
- **Evidence against:**
  - **Per-seat pricing erosion (our own L-12 lesson from ROP DA):** AI agents reduce headcount at law firms. RELX retains the customer (switching costs) but loses seats. Same customer, less revenue. This is EXACTLY the dynamic documented in our decisions_log.yaml lesson from Session 78.
  - **Harvey partnership cannibalization:** Artificial Lawyer analysis shows dual licensing (Harvey + Lexis) could create revenue overlap. If Harvey's $1.2K/seat includes Lexis content access, firms may reduce standalone Lexis subscriptions. The 15-25% cost uplift from bundling means RELX captures LESS per lawyer-hour of research, not more.
  - **Perplexity AI for academic research:** Perplexity Deep Research (launched early 2025) delivers "100+ cited studies, methodologies compared, and gaps identified in under 4 minutes -- slashing weeks of PubMed trawling." While not replacing ScienceDirect for full-text access, it reduces the FREQUENCY of direct database queries, which impacts transactional revenue (34% of RELX total).
  - **Anthropic Claude legal plug-in crash (Feb 3, 2026):** RELX fell 14% in a single day. While Artificial Lawyer calls this "irrational," the market signal is clear: investors see AI as a THREAT, not a tailwind. The stock has not recovered.
- **What the thesis gets right:** RELX's proprietary data is genuinely irreplaceable. 138B legal documents and 21M scientific articles cannot be easily replicated. AI needs this data. The question is not WHETHER AI uses RELX data, but HOW MUCH RELX captures from AI-mediated access vs. direct access.
- **Severity:** HIGH
- **Resolution:** AI is BOTH tailwind and headwind simultaneously. Tailwind: higher-value products, premium pricing. Headwind: fewer seats per firm, intermediation by AI tools, transactional volume decline. Net effect is uncertain. The thesis should model a NEUTRAL AI scenario (not pure tailwind) in the base case. Bull case can include AI tailwind; bear case must include AI threat.

### 3. "WACC of 7.5% is Appropriate"

- **Thesis claim:** "The tool's 9% is too high because it doesn't adjust for RELX's defensive characteristics." Uses manually derived WACC of 7.5% with beta 0.7.
- **Evidence against:**
  - yfinance reports beta 0.21, which the analyst rejects as "too low" and substitutes 0.7. But the thesis's own sensitivity shows FV at 8% WACC = EUR 22.40, and at 7.5% = EUR 26.30. The weighted FV of EUR 33.50 is only achievable because the DCF at 7.5% WACC with 10% growth produces EUR 31.
  - The analyst chose 10% FCF growth for DCF (above historical 8.2% CAGR) AND low WACC (7.5% vs tool's 9%). Both assumptions simultaneously favor bullish outcome.
  - RELX's own credit rating is A- (S&P), A3 (Moody's). The cost of equity for an A-rated company with beta 0.7 in the current environment (UK gilt 4.0%, ERP 5.5%) is reasonable at 7.85%. But the DCF is EXTREMELY sensitive to this: TV is 80.6% of EV. A 50bp WACC increase destroys ~15% of FV.
  - The tool's 9% WACC may include a broader market risk premium that is more appropriate for the current environment (elevated rates, AI uncertainty). Rejecting it without stronger justification is problematic.
- **Severity:** MODERATE
- **Resolution:** Use WACC range 7.5-9.0% with midpoint 8.25%. At WACC 8.25%, growth 8% (historical), DCF FV is approximately EUR 24-25. The earnings-based method at 24x P/E (EUR 35) is more reliable for this type of business, as the thesis acknowledges. Weighted FV should be closer to EUR 30-31 rather than EUR 33.50.

### 4. "Open Access is a Kill Condition, Not a Near-Term Threat"

- **Thesis claim:** Lists Open Access as kill condition #3 but treats it as distant/theoretical.
- **Evidence against:**
  - **UK universities cancelling NOW:** Six UK universities (Sheffield, Lancaster, Surrey, Essex, Kent, Sussex) have already opted out of the new Elsevier deal in early 2026. Sheffield called the deal "financially unsustainable." This is not theoretical -- it is happening.
  - **US OSTP mandate effective 2025-2026:** All US federally funded research must be publicly accessible immediately upon publication, with no embargo period. Implementation deadline was December 31, 2025. This directly undermines Elsevier's subscription revenue for federally funded articles.
  - **University of California boycott:** UC system (the largest US research university system) stopped paying Elsevier subscriptions. While a new deal was eventually reached, the precedent shows even top-tier institutions are willing to walk away.
  - **University of Auckland/NZ:** Disruptions to Elsevier journal access expected in 2026 as deals expire.
  - **Financial pressure:** UK universities sought 5-15% price reductions on GBP 112M annual spend with five major publishers. Universities are in fiscal constraint and academic publishing budgets are being cut.
- **Impact quantification:** STM is ~33% of RELX revenue. If Open Access erodes 15-20% of subscription revenue over 5 years (plausible given regulatory mandates + university opt-outs), that is a 5-7% total revenue headwind. The thesis models STM at 4-5% sustainable growth -- this could become 1-2% or flat.
- **Severity:** HIGH
- **Resolution:** Open Access should be treated as a NEAR-TERM headwind (not just a kill condition). STM growth assumption should be lowered to 2-3% (from 4-5%) in the base case. Kill condition should be more specific: "If >20% of Elsevier's top 100 institutional clients cancel or significantly reduce subscriptions within 24 months."

### 5. "P/E of 24x is Conservative for a Quality Compounder"

- **Thesis claim:** Uses 24x P/E as "conservative end" for earnings-based FV. Cites historical range of 20-35x.
- **Evidence against:**
  - RELX currently trades at 20.9x P/E. The market is assigning this multiple WITH full knowledge of FY2025 results (+7% revenue, +9% AOP, +10% EPS). The market is NOT mispricing ignorantly -- it has seen the results and still prices at 21x.
  - Wolters Kluwer (WKL.AS) trades at ~13x (66% below ATH). If the information services sector is in a structural de-rating, 24x may be the OLD normal, not the NEW fair value.
  - The SaaSpocalypse selloff that began in late 2025 may reflect a PERMANENT re-rating of information services multiples, not a temporary dislocation. AI tools (Perplexity, Claude, ChatGPT) fundamentally change how professionals access information -- even if RELX's data remains essential, the DELIVERY mechanism (and therefore the pricing power) is changing.
  - VRSK trades at 27.5x but has 38% ROIC (vs RELX 23%) and is US-only (no FX risk). MORN trades at ~21x. These are imperfect comps but suggest 20-22x may be the new normal for the sector.
- **Severity:** MODERATE
- **Resolution:** Use 21-23x P/E range instead of 24-26x. At 22x, earnings-based FV = 128.5p * 22 = GBP 28.27 = EUR 32.31. At 21x (current multiple), FV = EUR 30.84. This is a much tighter range and suggests less upside than the thesis claims.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | LexisNexis is #2-3 in legal research, not #1 | 6sense: Westlaw 34%, Casetext 31%, Lexis 8% market share | HIGH |
| 2 | Legal market is fragmenting (3-way race, not duopoly) | Clio acquired vLex ($1B), Harvey at $8B valuation, Thomson Reuters CoCounsel | MODERATE |
| 3 | Elsevier faces real university opt-outs NOW | 6 UK universities cancelled in early 2026, UC system boycott precedent | HIGH |
| 4 | Per-seat pricing erosion from AI (our own L-12 lesson) | AI agents reduce headcount at law firms; same customer, less revenue | HIGH |
| 5 | Harvey partnership may cannibalize Lexis standalone revenue | Artificial Lawyer: dual licensing overlap, 15-25% cost uplift vs standalone | MODERATE |
| 6 | Perplexity/Claude reduce transactional query volume | Perplexity Deep Research: "100+ cited studies in 4 minutes" | MODERATE |
| 7 | CEO succession risk (Engstrom 16+ years, owns 0.065%) | Low insider ownership, long tenure, no public succession plan | LOW |
| 8 | Exhibitions segment is transactional and cyclical (~10% of revenue) | Not a concern per se, but thesis claims it as growth driver | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 9 | WACC 7.5% is aggressively low (tool uses 9%) | DCF TV = 80.6% of EV; 50bp WACC change = ~15% FV swing | MODERATE |
| 10 | FCF growth 10% assumption exceeds historical 8.2% CAGR | Analyst chose bullish growth AND low WACC simultaneously | MODERATE |
| 11 | 24x P/E may be obsolete; sector de-rating to 20-22x | WKL.AS at 13x, RELX at 21x after strong results; market may be right | MODERATE |
| 12 | MoS vs Bear is NEGATIVE (-21.8%) | Price EUR 26.80 is ABOVE bear case EUR 22. No downside cushion | HIGH |
| 13 | E[CAGR] 10.6% is below the 12% Tier A threshold | Thesis acknowledges this but still recommends watchlist at EUR 23-24 | LOW |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 14 | US OSTP mandate eliminates embargo on federal research | Effective Dec 2025; directly undermines subscription revenue for fed-funded articles | HIGH |
| 15 | Goodwill at 54% of assets -- impairment risk if segments deteriorate | If STM or Legal face structural decline, goodwill write-down is material | LOW |
| 16 | Net debt increased 10% to 2.0x EBITDA; buyback of GBP 2.25B in 2026 | 2.0x within target (2.0-2.5x), but leaves little buffer for M&A/downturn | LOW |
| 17 | GBP/EUR FX risk (60% NA revenue in USD, reporting in GBP, listing in EUR) | Triple currency mismatch creates noise and risk for EUR-based portfolio | LOW |
| 18 | Thesis does not disclose customer churn/retention rates | RELX does not publicly report these metrics; cannot validate "95% renewal" claim | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 19 | SaaSpocalypse selloff may not have bottomed | WKL.AS -66%, RELX -46%, IT -70%; sector rotation may continue | MODERATE |
| 20 | No clear near-term catalyst for re-rating | Strong FY2025 results already released; market shrugged (+6% then back down) | MODERATE |
| 21 | Analyst consensus is "Strong Buy" with mean PT GBP 38.33 | If consensus is bullish and stock is still -46%, the market disagrees STRONGLY | MODERATE |

---

## Conflictos con Otros Analisis

No moat_assessment.md, valuation_report.md, or risk_assessment.md were produced for this R1 (only thesis.md). This limits the ability to cross-reference.

**Conflict with system's own lessons:**
- **L-12 (Per-seat pricing risk):** The thesis does NOT mention this lesson, which was identified in Session 78 during the ROP devil's advocate analysis. The lesson explicitly states: "AI agents reduce headcount at customer firms. Software retains the customer but LOSES seats. This is NOT the same as customer churn -- it is SAME customer, LESS revenue." RELX Legal and STM are BOTH per-seat/per-user pricing models that are vulnerable to this dynamic. This should have been flagged.

**Conflict with QS Tool-First principle:**
- The thesis adjusts QS from 73 to 78 (+5). The dominant adjustment is market position (+7 from 0 to 7). But if LexisNexis is #2-3 rather than #1 (as market share data suggests), the adjustment should be +5 (for #3-5 position), not +7 (for #1-2 position). This would make QS Adjusted 76, still Tier A but at the lower boundary.

**Conflict with Error #49 (Anchoring to consensus):**
- The thesis notes analyst mean target EUR 45.25 and says "My FV EUR 33.50 is 26% BELOW analyst consensus." While 26% below consensus sounds independent, the 24x P/E multiple used is still within the historical consensus range. A truly independent valuation should consider whether the historical P/E range (20-35x) is still valid given AI disruption of the business model.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Total desafios | 21 |
| Desafios HIGH | 5 of 21 |
| Desafios MODERATE | 10 of 21 |
| Desafios LOW | 6 of 21 |
| Desafios HIGH/CRITICAL | 5 (no CRITICAL) |
| Desafios no resueltos por thesis | 8 |
| Score | **11/19** |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion

**MODERATE COUNTER:** The thesis has meaningful gaps. The business quality is genuinely high (ROIC +18pp, FCF consistency, 99% conversion), which limits the severity of the counter-thesis. However:

1. The "#1 in legal" claim is factually questionable and inflates the QS adjustment.
2. The "AI is pure tailwind" narrative ignores per-seat cannibalization (our own L-12) and Harvey partnership dynamics.
3. The WACC of 7.5% combined with 10% growth in DCF is a double-optimism that inflates FV by ~15-20%.
4. Open Access is not a distant kill condition -- it is actively eroding Elsevier's subscription base NOW.
5. The MoS vs Bear being negative (-21.8%) means the current price offers ZERO downside protection against the adverse scenario.

The thesis does NOT warrant rejection -- RELX is a quality business with a WIDE moat and strong fundamentals. But the FV of EUR 33.50 is too generous. A more realistic FV is EUR 28-31.

---

## Recomendacion al Investment Committee

### FV Adjustment Recommendation

| Parameter | R1 Thesis | DA Recommendation | Rationale |
|-----------|-----------|-------------------|-----------|
| QS Adjusted | 78 (Tier A) | 76 (Tier A, lower bound) | Market position +5 (not +7); LexisNexis is #2-3, not #1 |
| P/E Multiple | 24x | 22x | Sector de-rating is structural; 21x is current market price, 22x is modest premium |
| WACC | 7.5% | 8.25% (midpoint of 7.5-9.0%) | Tool's 9% may be too high, but 7.5% with 80% TV share is too aggressive |
| FCF Growth | 10% | 8% (historical CAGR) | Using 10% with low WACC is double-optimism |
| STM Growth | 4-5% | 2-3% | Open Access headwinds are real and accelerating |
| AI Impact | Pure tailwind | Neutral (tailwind + headwind) | Per-seat erosion + query intermediation offset premium pricing |

### Bear-Adjusted FV Estimate

Earnings method at 22x P/E: 128.5p * 22 = GBP 28.27 = EUR 32.31
DCF at WACC 8.25%, growth 8%: approximately EUR 24
Weighted (60/40): EUR 28.99

**DA-Adjusted FV: EUR 29.00** (vs thesis EUR 33.50, -13.4% reduction)

At EUR 29.00 FV:
- MoS at current EUR 26.80: 7.6% (INSUFFICIENT for Tier A)
- Entry for 20% MoS: EUR 23.20 (consistent with thesis's EUR 23-24 recommendation, interestingly)
- Entry for 15% MoS (MORN precedent): EUR 24.65

### Items for Committee Resolution

1. **Resolve market position claim:** Is LexisNexis #1 or #2-3? The 6sense data (8% share) vs revenue comparison (#2 by revenue) gives different answers. Committee should decide which metric is relevant for moat assessment.

2. **WACC selection:** Committee must decide between tool's 9%, thesis's 7.5%, or DA's recommended 8.25%. This single parameter swings FV by +/- 30%.

3. **AI scenario in base case:** Should the base case assume AI-neutral (DA recommendation) or AI-tailwind (thesis)? The evidence is genuinely mixed.

4. **Open Access timeline:** Is STM growth 4-5% (thesis) or 2-3% (DA adjusted for OA headwinds)? The UK university cancellations and US OSTP mandate provide concrete evidence for the lower range.

5. **Entry price validation:** Both thesis (EUR 23-24) and DA (EUR 23.20 for 20% MoS) converge on similar entry ranges. The disagreement is on FV, not on entry discipline. The thesis WATCHLIST verdict at EUR 26.80 is CORRECT regardless of FV.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- The 6sense market share data (Westlaw 34%, Lexis 8%) may measure technology deployments rather than revenue. By revenue, LexisNexis Legal is likely $2-3B, making it the clear #2 behind Thomson Reuters Legal at ~$3B. The "market share" framing depends on what is being measured. I flagged this nuance but could not fully resolve it.
- RELX does not publicly disclose customer churn/retention rates. The thesis's claim of ">95% renewal rates" for academic publishers is an industry estimate, not RELX-specific data. Without this metric, the moat durability claim is partially unverifiable.
- The Harvey-LexisNexis pricing dynamics are still evolving. The partnership was announced June 2025 and the pricing impact analysis from Artificial Lawyer is speculative. Actual revenue cannibalization data will not be available until H1 2026 results.

### Limitaciones de Este Analisis
- Could not access Seeking Alpha bear case article (403 blocked). The full bearish analysis from that source would have strengthened the Open Access disruption argument.
- Could not access Morningstar's fair value estimate for RELX. Morningstar's independent FV would have been a useful data point for the valuation challenge.
- Insider trading data was limited -- yfinance may not capture Euronext filings well. A more thorough insider transaction analysis (RNS filings via LSE) would be needed.
- The Exhibitions segment was not deeply challenged because it is ~10% of revenue and not the core investment thesis. A deeper analysis of event industry cyclicality post-COVID could strengthen or weaken this area.

### Sugerencias para el Sistema
- **Per-seat risk tagging:** All thesis documents for information services / per-user-pricing companies should EXPLICITLY address L-12 (per-seat erosion from AI). This was a gap in the R1 thesis.
- **WACC justification standard:** When an analyst rejects the tool's WACC and substitutes their own, the counter-analysis should ALWAYS test with both WACCs and present the range. This prevents single-WACC-dependency in DCF valuations.
- **Market position data source:** 6sense/Datanyze provide market share data that could be systematically checked for the market position adjustment in QS. This would reduce subjectivity in the +0 to +8 scoring.

### Preguntas para Orchestrator
1. The thesis entry target (EUR 23-24) and the DA-adjusted entry (EUR 23.20) converge. Should we proceed to R3 resolution primarily to resolve the FV (EUR 33.50 vs EUR 29.00) and AI scenario question, or is the entry consensus sufficient to proceed directly?
2. Should L-12 (per-seat pricing erosion) be added as a formal kill condition for RELX? It applies to Legal (per-lawyer-seat pricing) and STM (per-user database access) and Risk (per-query transactional).
3. RELX, MORN, and VRSK are all "information services with WIDE moat" in our universe/pipeline. If all three become portfolio positions, we would have ~10-12% in a single sub-sector that faces correlated AI disruption risk. Should this be flagged as a concentration concern?

---

## Sources

- [Seeking Alpha - RELX Academic Publisher Open Access Disruption](https://seekingalpha.com/article/4753259-relx-academic-publisher-ripe-for-disruption-by-open-access)
- [RELX Projects Strong Growth, Quells AI Concerns - Bloomberg](https://www.bloomberg.com/news/articles/2026-02-12/lexisnexis-owner-relx-s-sales-growth-misses-analyst-estimates)
- [LawSites - 10 Legal Tech Trends That Defined 2025](https://www.lawnext.com/2026/01/the-10-legal-tech-trends-that-defined-2025.html)
- [LexisNexis Protege Next Generation](https://www.lawnext.com/2025/12/lexisnexis-unveils-the-next-generation-of-its-protege-general-ai-callling-it-the-most-integrated-legal-ai-workflow-solution.html)
- [Westlaw Market Share in Legal Research - 6sense](https://6sense.com/tech/legal-research/westlaw-market-share)
- [Inside Higher Ed - UK Universities Decline New Elsevier Deal](https://www.insidehighered.com/news/faculty-issues/books-publishing/2026/02/06/uk-universities-decline-new-elsevier-deal)
- [Times Higher Education - Three Major Universities Opt Out of Elsevier Deal](https://www.timeshighereducation.com/news/three-major-research-universities-opt-out-new-elsevier-deal)
- [Three More UK Universities Opt Out of Elsevier Deal](https://www.timeshighereducation.com/news/three-more-uk-universities-opt-out-new-elsevier-deal)
- [Harvey + LexisNexis Pricing Impact - Artificial Lawyer](https://www.artificiallawyer.com/2025/06/30/harvey-lexisnexis-the-potential-pricing-impact/)
- [Claude Crash Impact on LexisNexis is Irrational - Artificial Lawyer](https://www.artificiallawyer.com/2026/02/04/claude-crash-impact-on-thomson-reuters-lexisnexis-is-irrational/)
- [Morningstar - Software Stocks AI Disruption Worries](https://global.morningstar.com/en-nd/markets/software-stocks-are-investors-worrying-too-much-about-ai-disruption)
- [Morningstar - Thomson Reuters RELX Wolters Crushed After Claude Legal Plug-In](https://global.morningstar.com/en-nd/stocks/reuters-relx-wolters-stocks-crushed-after-anthropic-debuts-claude-legal-plug-in)
- [RELX 2025 Results Press Release](https://www.relx.com/media/press-releases/year-2026/relx-2025-results)
- [RELX Credit Ratings](https://www.relx.com/investors/debt-investors/credit-ratings)
- [RELX Sell-Off Opens Door for Re-Rating - JPMorgan via Proactive Investors](https://www.proactiveinvestors.co.uk/companies/news/1085266/relx-sell-off-opens-door-for-re-rating-as-jpmorgan-backs-ai-led-growth-1085266.html)
- [RELX Brokers Back Story Despite AI Fears - Proactive Investors](https://www.proactiveinvestors.co.uk/companies/news/1087342/relx-brokers-back-the-investment-story-despite-ai-fears-targets-cut-on-de-rating-1087342.html)
- [US OSTP Open Access Mandate - White House](https://www.science.org/content/article/white-house-requires-immediate-public-access-all-u-s--funded-research-papers-2025)
- [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [Legal AI Software Evaluation Report 2025 - Yahoo Finance](https://finance.yahoo.com/news/legal-ai-software-company-evaluation-080100081.html)
- [Harvey Revenue and Valuation - Sacra](https://sacra.com/c/harvey/)
- [Gatekeepers of Law: Westlaw and LexisNexis Duopoly](https://www.thebignewsletter.com/p/gatekeepers-of-law-inside-the-westlaw)

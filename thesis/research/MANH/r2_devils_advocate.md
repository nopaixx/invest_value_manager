# Counter-Analysis: MANH (Manhattan Associates)

## Fecha: 2026-02-23

## Calibration Anchor

- **Market price:** $144.27. Market implies 10.9% FCF growth for 5 years.
- **Historical FCF CAGR:** 29.3%. Revenue CAGR: 12.1%.
- **DA historical stats:** 19 corrections, avg -16.7%, median -16.9%. 0 outcomes measured yet. All corrections negative. My corrections have never been insufficient (no data yet to confirm).
- **Analyst consensus PT:** Mean $213, Median $225. Low $160, High $240. 11 analysts, "Buy" consensus.
- **FA thesis FV:** $156 (weighted), base $165, range $125-$195.
- **Anchoring discipline:** The FA must prove the market at $144 is wrong. The market is pricing ~11% FCF growth vs historical 29%. The question is whether 11% is too pessimistic, about right, or too optimistic.

---

## Resumen Ejecutivo

The thesis identifies a genuinely high-quality business (WIDE moat, exceptional ROIC, mission-critical software) at what appears to be a reasonable price. However, the thesis significantly OVERSTATES the fair value through generous growth assumptions, underweights the structural deceleration that is already visible in the numbers, and dismisses several risks too quickly. The revenue deceleration from 21.1% to 12.2% to 3.7% is not merely a "mix distortion" -- it reflects a business approaching mature-state growth as its cloud transition completes. The valuation premium (P/E 40x, EV/EBIT 30x) for a company guiding 5-7% revenue growth is vulnerable to compression. The bear case is significantly more probable than the thesis acknowledges.

**Thesis survives on business quality. Thesis is WEAKENED on valuation and growth trajectory.**

---

## Asunciones Clave Desafiadas

### 1. "Revenue deceleration is mix distortion from cloud transition, not real slowdown"

- **FA claim:** Cloud revenue +20% is the real story. Legacy wind-down creates headline drag. Growth will re-accelerate.
- **Evidence in contra:**
  - Revenue growth trajectory: 21.1% (FY2023) --> 12.2% (FY2024) --> 3.7% (FY2025). This is a CLEAR decelerating trend, not noise.
  - FY2026 guidance: $1.133-1.153B implies 5-7% total growth. Management itself is NOT guiding re-acceleration.
  - Cloud revenue growth, while still 20%+, is on an increasing base. Simple math: cloud was ~$340M in FY2024 and ~$408M in FY2025 (+20%). At $490M in FY2026 (+20%), it adds ~$82M. But total legacy attrition creates a 4pp headwind to total growth per management. Net: ~5-7% total growth, exactly what management guides.
  - Professional services revenue DECLINED 6% YoY in Q4 and 4% full-year. Services = 38% of revenue. This is not "mix distortion" -- it is actual revenue shrinkage in a major segment.
  - The thesis claims "SAP migration wave (300-500 new customers)" as a catalyst but provides no evidence this is materializing at scale. Schneider Electric is one data point. One anecdote is not a trend.
- **Severidad:** **HIGH** -- The thesis narrative of "temporary distortion" is contradicted by 3 years of decelerating revenue AND management's own forward guidance. Growth re-acceleration to 10%+ is a hope, not a base case.
- **Resolucion sugerida:** Re-classify revenue trajectory as "mature growth 5-8%" in base case, not "cloud-driven re-acceleration to 10-12%."

### 2. "ROIC of 397% reflects extraordinary economics"

- **FA claim:** 397% ROIC proves exceptional capital efficiency and wide moat.
- **Evidence in contra:**
  - ROIC of 397% is a mathematical artifact of an asset-light business with minimal invested capital (tangible book value is small or negative). It tells us NOTHING useful about incremental return on new investment.
  - The RELEVANT metric is FCF margin and FCF per dollar of revenue, which the thesis does address (34.6% FCF margin). But citing "397% ROIC" as if it were a meaningful economic indicator is misleading.
  - Many asset-light software companies have "astronomical" ROIC figures. This does not make them 397% better than a company with 20% ROIC. It means the denominator (invested capital) is tiny.
  - More importantly, SBC-adjusted FCF margin is ~24-25%, not 34.6%. The thesis acknowledges this but still uses the headline 34.6% for emotional impact.
  - The 397% ROIC figure is unstable: it was 428% in FY2022, 473% in FY2023, 235% in FY2024, 397% in FY2025. The volatility itself proves this metric is noise, not signal, for this type of business.
- **Severidad:** **LOW** -- The thesis is not actually WRONG about the business being capital-efficient. But using 397% ROIC as a headline figure is misleading and inflates perceived quality. The real metrics (SBC-adjusted FCF margin ~24-25%, expanding) are still excellent.
- **Resolucion sugerida:** De-emphasize ROIC figure. Focus on SBC-adjusted FCF margin as the primary economic indicator.

### 3. "Cloud transition is complete (96% of software revenue) and operating leverage will drive earnings growth above revenue growth"

- **FA claim:** With cloud at 96% of software revenue, the transition is "complete" and margins will expand.
- **Evidence in contra:**
  - If cloud transition is "complete," the exceptional growth catalyst is OVER. The thesis wants it both ways: cloud transition is complete (therefore margins expand) AND cloud growth is 20%+ (therefore growth continues). These are partially contradictory -- if the transition is done, the easy migration revenue dries up.
  - The remaining 4% of non-cloud software revenue is trivial. The future growth engine must be NEW customer acquisition and cross-sell, not migration. New customer acquisition is harder, slower, and more expensive than migrating existing customers.
  - Operating margin guidance for FY2026: 24.1-24.7% GAAP. The thesis cites "34.5-35% adjusted operating margin" but the GAAP figure is what shareholders receive. The ~10pp gap between GAAP and adjusted = SBC.
  - SBC/Revenue trajectory: 7.7% --> 7.7% --> 8.9% --> 10.3%. This is accelerating, not stabilizing. If SBC reaches 12-15%, the "operating leverage" narrative is hollow because real economic profits are diluted.
  - Capex/Depreciation jumped to 2.4x in FY2025 from 0.8-1.4x in prior years. For an "asset-light" company, this is notable. May signal infrastructure build that compresses near-term economics.
- **Severidad:** **MODERATE** -- The operating leverage thesis is plausible but the SBC trend and the "transition complete = growth catalyst over" dynamic are real concerns that the thesis does not adequately address.
- **Resolucion sugerida:** Separate "margin expansion" thesis from "growth" thesis. Margin expansion is likely but at a slower rate. Growth will depend on new customer wins, not migration.

### 4. "AI is net positive for MANH (Agentic AI, warehouse robotics optimization)"

- **FA claim:** MANH is positioned as beneficiary, not victim, of AI disruption. WMS cannot be replaced by AI.
- **Evidence in contra:**
  - The thesis is CORRECT that AI does not replace physical WMS operations. Warehouses need orchestration software.
  - However, AI changes the COMPETITIVE DYNAMICS. According to industry analysis, agentic AI systems already accounted for 17% of total AI value in supply chains in 2025, projected to 29% by 2028. These agents query disparate systems (ERP, WMS, TMS) and trigger actions.
  - The key risk is not "AI replaces WMS" but "AI COMMODITIZES the optimization layer." If AI agents can orchestrate across multiple WMS platforms (or reduce the need for deep WMS-specific customization), the switching costs that protect MANH's moat could erode over 5-10 years.
  - Blue Yonder's AI-driven end-to-end supply chain integration strategy is a direct competitive threat. In Feb 2024, Blue Yonder acquired Flexis AG for manufacturing/supply chain planning. GXO Logistics partnered with Blue Yonder for enhanced WMS capabilities.
  - SAP's supply chain offerings integrate within its ERP ecosystem. For companies already on SAP S/4 HANA, there is a natural pull to keep WMS within the SAP ecosystem rather than use a best-of-breed solution like MANH. The thesis frames SAP migration as positive for MANH, but SAP is building competitive WMS within S/4 HANA.
  - Microsoft Dynamics 365 Supply Chain is marketing AI-driven autonomous manufacturing capabilities. Big tech entry into supply chain software is a long-tail risk.
- **Severidad:** **MODERATE** -- The thesis correctly identifies MANH as short-term AI beneficiary. But the medium-term risk of AI commoditizing the optimization layer and enabling platform-integrated alternatives (SAP, Blue Yonder) is real and under-explored. Timeline: 3-7 years.
- **Resolucion sugerida:** Add kill condition for "AI-driven competitive win rate decline." If win rate drops from 75% to below 60%, AI commoditization thesis is materializing.

### 5. "CEO transition is manageable -- product roadmap is engineering-driven"

- **FA claim:** Eric Clark is capable. Capel stays as Vice-Chairman. Product decisions are institutional.
- **Evidence in contra:**
  - The CEO transition was ABRUPTLY announced on a Monday (Feb 10, 2025) with Capel stepping down TWO DAYS later. This is NOT normal succession planning. Board acknowledged they "maybe missed the mark on this transition."
  - Investors felt "bushwhacked" despite management claims the change had been a formal process for 2+ years. If planned for 2+ years, why the 2-day notice?
  - Clark has ZERO supply chain industry experience. He comes from NTT Data North America (IT services), previously ServiceNow, Dell, HPE. Company leadership said they were looking for "a great athlete" with "high intellect" -- this is generic corporate-speak that does not address domain expertise.
  - The stock fell 11% on the announcement alone. The market is not stupid -- abrupt CEO transitions with outside hires lacking domain expertise are statistically negative for specialized technology companies.
  - Insider ownership at 1.7% is already low. With Capel's departure (and his July 2025 sale of $8.2M in shares), the founder/veteran alignment is diminishing.
  - Clark received large stock grants (34K shares on Feb 4, 2026; 16K shares on Jan 22, 2026 = ~$7M at current prices). His incentive alignment depends entirely on stock performance, not on supply chain domain conviction.
- **Severidad:** **HIGH** -- The thesis significantly underweights CEO transition risk. An abrupt departure with a 2-day notice, an outside hire with no industry experience, and diminishing insider alignment is a MATERIAL concern for a specialized B2B software company where customer relationships and domain expertise matter. The 20-25% probability assigned by the thesis is too low; I would assign 35-40%.
- **Resolucion sugerida:** Increase CEO transition risk probability to 35-40%. Add kill condition: "If Q1/Q2 2026 bookings decelerate below guidance AND attributed to commercial execution, CEO risk is materializing."

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Revenue deceleration is structural, not mix distortion | 3 years of declining growth (21.1% -> 12.2% -> 3.7%). Mgmt guides 5-7%. Services -6% YoY Q4. | HIGH |
| 2 | Cloud transition "completion" removes key growth catalyst | 96% cloud = easy migration revenue is done. Future growth = harder new customer acquisition. | MODERATE |
| 3 | SAP migration "wave" is unproven at scale | One example (Schneider Electric). 300-500 potential customers is theoretical. | MODERATE |
| 4 | SBC rising from 7.7% to 10.3% erodes real economics | SBC-adjusted FCF margin ~24-25% vs headline 34.6%. Gap widening. 10.3% and accelerating. | MODERATE |
| 5 | CEO abrupt departure and outside hire without domain expertise | 2-day transition, "bushwhacked" investors, no supply chain background, Capel sold $8.2M July 2025 | HIGH |
| 6 | Professional services revenue declining (-4% FY, -6% Q4) | Indicates macro sensitivity or implementation delays. 38% of total revenue. | MODERATE |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 7 | P/E 40x for 5-7% revenue grower is premium territory | P/E 40x vs Software sector avg 32.7x. For this growth rate, historical median P/E would be 25-30x. | HIGH |
| 8 | FA's FV $156 relies on growth re-acceleration assumption | OEY calculation uses 10-12% sustainable growth, but mgmt guides 5-7%. | HIGH |
| 9 | DCF tool base case ($114) is more realistic than FA's $165 | Tool uses consistent methodology. FA overrides with optimistic growth assumption. | MODERATE |
| 10 | EV/EBIT 30x current vs FA's "justified" 22-24x is contradictory | Stock already trades at 30x EV/EBIT. FA says 22-24x is justified. This implies OVERVALUED. | HIGH |
| 11 | SBC-adjusted metrics should be primary | OEY on headline FCF = 4.3%. SBC-adjusted OEY = 2.85%. Real return is lower. | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 12 | Short interest rising (+12.4% MoM to 4.7% float) | Informed investors increasing shorts from $1.9M to $2.1M shares. Signal, not noise. | MODERATE |
| 13 | Customer renewal risk period | Seeking Alpha documents "major customer renewal risk period" with tepid topline growth | MODERATE |
| 14 | Insider selling pattern (Capel $8.2M Jul 2025) with zero insider buying at $144 | At -42% from ATH, ZERO open-market purchases from any insider. Only stock grants. | HIGH |
| 15 | AI commoditization of optimization layer (3-7 year risk) | Agentic AI 17% of supply chain value in 2025, projected 29% by 2028 | MODERATE |
| 16 | Blue Yonder + SAP + Microsoft intensifying supply chain AI competition | Blue Yonder acquired Flexis, partnered with GXO. SAP building within S/4. MSFT Dynamics 365. | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 17 | No clear catalyst for re-rating in near-term | SAP migration "wave" is theoretical. Next earnings is Q1 2026 (April). No event to close gap. | MODERATE |
| 18 | Consensus already bullish (mean PT $213, +47% from current) | If consensus is right at $213, FA's $156 FV is BELOW consensus. Our "edge" would be negative. | HIGH |
| 19 | Short interest rising suggests informed skepticism | 4.7% SI, rising 12.4% MoM. Shorts see something at this price. | MODERATE |

---

## Independent Bear-Case Valuation (Phase 3B)

### Method: EV/EBIT Normalized (DIFFERENT from FA's primary OEY method)

**Bear-case assumptions:**
- Revenue growth: 5% (management guided 5-7%, use low end)
- GAAP Operating margin: 24.4% (midpoint of FY2026 GAAP guide 24.1-24.7%)
- FY2026E Revenue: $1.14B (guide midpoint)
- FY2026E GAAP EBIT: $278M (24.4% of $1.14B)
- EV/EBIT multiple: 20x (sector trailing for moderate-growth enterprise software, below MANH's historical 30x+ but above sector median 18x, reflecting quality)
- Terminal growth: 2% (conservative, mature software)

**Calculation:**
```
GAAP EBIT (FY2026E):    $278M
EV/EBIT multiple:        20x (bear)
Enterprise Value:         $5.56B
Plus net cash:           +$241M
Equity Value:            $5.80B
Shares outstanding:      ~61M
FV/share:                $95
```

**Cross-check with DCF tool bear case:** $91 (close alignment validates my bear estimate)

### Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $156 | OEY/Reverse DCF (60%) + EV/EBIT (40%) |
| Market | $144 | Current price |
| DA bear | $95 | EV/EBIT 20x on GAAP FY2026E EBIT |

**Interpretation:** FA $156 > Market $144 > DA $95. Normal pattern. The MoS debate is about distance. At market, there is modest upside if FA is right but significant downside (-34%) if bear materializes. The risk/reward is NOT asymmetric in our favor at $144.

---

## Conflictos con Otros Analisis

No moat_assessment.md or risk_assessment.md files exist for MANH -- R1 was produced by fundamental-analyst only. Key observations:

1. **Thesis internal contradiction (Challenge #10):** The thesis calculates EV/EBIT at 22-24x as "justified" but the stock trades at ~30x EV/EBIT. By the thesis's own metric, MANH is OVERVALUED. The thesis resolves this by pivoting to the OEY/Reverse DCF method (which gives a higher FV of $176) and giving it 60% weight, but this is essentially choosing the method that produces the answer you want.

2. **SBC treatment inconsistency:** The thesis correctly notes SBC-adjusted FCF margin is ~24-25% (not 34.6%) but then uses the headline FCF figure ($374M) in the OEY calculation and subtracts SBC afterwards. The final OEY of 2.85% is honest, but the "FCF CAGR 29.3%" used for historical comparison is based on headline FCF which includes SBC add-backs. SBC-adjusted FCF CAGR would be lower.

3. **FV range width:** $125-$195 is a 56% spread. When uncertainty is this high, anchoring to the midpoint ($156) rather than the low end ($125) is an optimistic choice. At $144 vs $125 low-end, there is only 13% MoS -- barely adequate.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | 5 HIGH of 19 total (26%) |
| Desafios no resueltos por thesis | 7 (revenue structural deceleration, CEO transition depth, EV/EBIT contradiction, insider non-buying, rising short interest, consensus PT vs our FV, SBC trajectory) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

**MODERATE COUNTER:** The thesis identifies a genuinely excellent business. The moat is real. The cloud-native advantage is real. MANH is NOT a value trap. However, the valuation analysis has material gaps: (1) the revenue deceleration is treated as temporary when it may be structural, (2) the CEO transition risk is underweighted, (3) the FV of $156 relies on growth re-acceleration that management itself is not guiding to, and (4) the thesis's own EV/EBIT analysis says the stock is overvalued at current prices, which the thesis then overrides with a more optimistic method. The market at $144 may be approximately right, not materially undervalued.

---

## Edge Assessment

- **Analyst consensus PT:** $213 (mean), $225 (median). Source: 11 analysts via insider_tracker.py
- **Post-DA FV:** $130 (my recommendation -- see below)
- **Gap vs consensus:** -39% (we are MUCH more conservative than consensus)
- **Gap vs FA thesis:** -17% ($130 vs $156)
- **Our specific edge:** The thesis correctly identifies the cloud transition advantage, but the market (at $144) already prices in modest growth and premium quality. Our "edge" would be buying at a genuine discount to intrinsic value, not buying at roughly fair value. At $120 (thesis entry) the edge becomes more credible. At $144, we do not have an informational edge -- we are aligned with the lower end of consensus.
- **WARNING: At $144, the gap between our post-DA FV ($130) and market ($144) is -10%. This suggests the stock is SLIGHTLY OVERVALUED vs our assessment, not undervalued.**

---

## Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $156 | OEY/Reverse DCF (60%) + EV/EBIT (40%) |
| Market | $144 | Current price |
| DA bear | $95 | EV/EBIT 20x on GAAP FY2026E EBIT |

---

## Post-DA Fair Value Recommendation

| Component | FA Thesis | DA Adjustment | Rationale |
|-----------|-----------|---------------|-----------|
| Growth assumption | 10-12% sustainable | 6-8% (mgmt guides 5-7%, allow some upside from cross-sell) | Revenue trajectory and guidance support lower growth |
| EV/EBIT multiple | 22-24x | 20-22x | Premium justified for quality, but less than FA claims given deceleration |
| SBC treatment | FCF $374M, then adjust | SBC-adjusted FCF ~$263M as primary | SBC at 10.3% and rising must be primary metric |
| CEO transition risk | 20-25% probability | 35-40% probability | Abrupt departure, no domain expertise, Capel selling |
| OEY method FV | $176 | $150 | Lower growth reduces FV from Reverse DCF |
| EV/EBIT method FV | $125 | $115 | Lower multiple + GAAP EBIT focus |
| **Weighted FV** | **$156** | **$130** | **Using FA's 60/40 weighting** |

**Post-DA FV: $130** (17% reduction from FA's $156)

This is within the historical DA correction range (avg -16.7%, median -16.9%).

**Actionable entry:** $100-110 (23-15% MoS vs $130 FV), which gives E[CAGR] of 10-13%.
**FA recommended entry was $120**, which provides 7.7% MoS vs post-DA FV $130 -- thin for Tier A by precedent.

---

## Recomendacion al Investment Committee

1. **Resolve the revenue trajectory question BEFORE approving.** The thesis claims "temporary distortion" but 3 years of deceleration + management guidance contradict this. Committee should require explicit evidence of re-acceleration (not just cloud bookings growth, but TOTAL revenue inflection) before approving.

2. **Resolve the CEO transition assessment.** An abrupt 2-day notice departure, an outside hire with zero supply chain domain expertise, and the former CEO selling $8.2M in shares 5 months later is NOT a "Low-Medium" risk. Committee should weight this at 35-40% probability of material impact and monitor Q1 2026 commercial execution metrics closely.

3. **Resolve the internal valuation contradiction.** The thesis's own EV/EBIT analysis produces FV $117-133 (overvalued at $144) while the OEY/Reverse DCF produces $176 (undervalued at $144). These contradicting methods should not be averaged -- the committee should determine which is more reliable for MANH specifically, and weight accordingly.

4. **Lower entry target.** FA recommends $120 entry. Post-DA FV of $130 means $120 entry = only 7.7% MoS. For Tier A precedents (17-38% MoS), consider $100-110 entry instead.

5. **Add kill condition for insider activity.** If no open-market insider purchases occur by end of Q2 2026 (6 months at -42% from ATH), this is a negative signal. Informed insiders choosing not to buy when stock is "cheap" by thesis standards should be a red flag.

6. **Monitor SBC trajectory.** If SBC/Revenue exceeds 12% in FY2026, KC#5 (15%) is approaching and the "operating leverage" thesis is being diluted by employee compensation.

---

## META-REFLECTION

### Dudas/Incertidumbres
- I could not access the Seeking Alpha article on "major customer renewal risk period" due to paywall. This analysis may contain important quantitative data on churn risk and contract renewal cycles that would strengthen or weaken Challenge #13.
- The SAP migration wave is genuinely difficult to assess. If it materializes at the scale the thesis suggests (300-500 new customers), it would be transformative. But I found no independent verification beyond management commentary and one case study (Schneider Electric).
- Short interest at 4.7% is elevated but not extreme. The 12.4% MoM increase is more concerning as a trend than the absolute level.

### Limitaciones de Este Analisis
- No access to earnings call transcripts to verify specific management comments on customer churn, retention rates, or SAP migration pipeline.
- Insider tracker shows mostly stock grants, not open-market transactions. The distinction between grants (compensation) and purchases (conviction) is critical -- grants tell us nothing about insider confidence.
- The WMS market competitive analysis is based on general market reports, not hands-on customer surveys or Gartner shortlist data.

### Sugerencias para el Sistema
- Consider adding a "management quality assessment" sub-score to the QS tool or as a standard section in R1 analysis, specifically for companies undergoing CEO transitions. Current QS tool does not capture this.
- For companies with SBC >8% of revenue, the R1 thesis should ALWAYS present SBC-adjusted metrics as primary, with headline metrics as secondary. This should be a standard requirement, not analyst discretion.

### Preguntas para Orchestrator
1. Given that our post-DA FV ($130) is BELOW market ($144), should MANH proceed to R3/R4 or be parked as OVERVALUED? The business quality is undeniable, but the price may already reflect that quality.
2. The FA's recommended entry of $120 represents only 7.7% MoS vs post-DA FV of $130. This is below ALL Tier A precedents (17-38%). Should we require a deeper discount ($100-110) or accept thin MoS given the exceptional business quality?
3. Should SBC/Revenue trajectory be added as a systematic kill condition for ALL software positions in the portfolio (ADBE, BYIT.L, MANH pipeline)? Currently only MANH KC#5 addresses this.

---

## Sources

- [TIKR: MANH Stock Recovery Analysis](https://www.tikr.com/blog/down-55-from-all-time-highs-can-manhattan-associates-nasdaq-stock-finally-recover-in-2026)
- [Yahoo Finance: Why MANH Shares Are Sliding](https://finance.yahoo.com/news/why-manhattan-associates-manh-shares-200056422.html)
- [FreightWaves: MANH C-suite Change](https://www.freightwaves.com/news/manhattan-associates-sudden-c-suite-change-not-what-it-seemed-executives-say)
- [Nasdaq: CEO Succession and Stock Reaction](https://www.nasdaq.com/articles/manhattan-associates-ceo-eddie-capel-retire-eric-clark-succeed-stock-down)
- [MANH CEO Succession Announcement](https://www.manh.com/about-us/newsroom/press-releases/manhattan-associates-announces-ceo-succession)
- [ManagementCV: MANH CEO Clark Analysis](https://www.managementcv.com/assets/downloads/MANHceoClark021225.pdf)
- [Mordor Intelligence: WMS Market](https://www.mordorintelligence.com/industry-reports/warehouse-management-system-market)
- [MarketsandMarkets: WMS Market](https://www.marketsandmarkets.com/ResearchInsight/warehouse-management-system-market.asp)
- [Seeking Alpha: MANH Customer Renewal Risk](https://seekingalpha.com/article/4852206-manhattan-associates-enters-major-customer-renewal-risk-period)
- [AInvest: MANH Insider Sales Analysis](https://www.ainvest.com/news/manhattan-associates-insider-sales-profit-earnings-surge-subtle-warning-2508/)
- [Simply Wall St: MANH Valuation Assessment](https://simplywall.st/stocks/us/software/nasdaq-manh/manhattan-associates/news/assessing-manhattan-associates-manh-valuation-after-mixed-sh)
- [Public.com: MANH Analyst Ratings](https://public.com/stocks/manh/forecast-price-target)
- [Tech Fund: Manhattan Associates Problems & Winners](https://www.techinvestments.io/p/manhattan-associates-problems-and)
- [Dataiku: Supply Chain AI Trends 2026](https://www.dataiku.com/stories/blog/supply-chain-ai-trends-2026)
- [Prolifics: Agentic AI in Supply Chain](https://prolifics.com/usa/resource-center/blog/agentic-ai-in-supply-chain)
- [Supply Chain Management Review: AI Global Supply Chains](https://www.scmr.com/article/how-ai-is-shifting-global-supply-chains-from-reactive-to-predictive)

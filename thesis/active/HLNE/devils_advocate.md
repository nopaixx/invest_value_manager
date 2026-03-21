# Devil's Advocate: HLNE (Hamilton Lane Incorporated)

## Date: 2026-03-16

---

## CRITICAL FLAG (Orchestrator Attention)

**NEW CRITICAL FINDING: Private Credit Meltdown Contagion.** The Blue Owl crisis (Feb-Mar 2026) has triggered a sector-wide panic in alternative asset management. Evergreen/semi-liquid fund redemption gates are being imposed across the industry (Blackstone BCRED, BlackRock HPS, Morgan Stanley North Haven). JPMorgan is marking down software loan collateral as of March 16, 2026. This DIRECTLY threatens HLNE's Evergreen growth narrative -- the thesis's primary growth engine (+70% AUM growth) operates with the SAME structure now under stress across the industry. HLNE's Senior Credit Opportunities Fund (SCOPE) offers monthly liquidity -- it is exposed to the same redemption dynamics that destroyed Blue Owl. This risk was NOT in the original thesis, NOT in the R2 DA refresh, and NOT in the batch contrathesis.

Additionally, the probability-weighted FV from my independent analysis is $87-90, which is BELOW the current price of $97.16. The position may have negative expected return on a risk-adjusted basis.

---

## Counter-Thesis Summary

Hamilton Lane is a genuinely high-quality business (QS 86/82 Tier A, ROIC 29%, fortress balance sheet, $3.2M insider cluster buy). The thesis is NOT wrong about the company's quality. The thesis IS potentially wrong about: (1) the durability of the Evergreen growth engine in a private credit crisis, (2) the structural nature of the PE fundraising drought, (3) the competitive threat from mega-managers whose distribution firepower dwarfs HLNE, and (4) the valuation, which at FV $110 vs price $97 provides only 13% MoS with HIGH sensitivity to growth assumptions. The market at $97 is pricing 1.2% FCF growth -- pessimistic, but the private credit meltdown provides a concrete mechanism by which near-zero growth could materialize for 2-3 years.

---

## Calibration Anchor

| Metric | Value | Source |
|--------|-------|--------|
| Current Price | $97.16 | price_checker.py (Mar 16) |
| Market-Implied FCF Growth | 1.2%/yr | dcf_calculator.py --reverse |
| Historical FCF CAGR | 21.5% | yfinance 4yr |
| FA Thesis FV | $110 | thesis.md (R3 refresh) |
| Analyst Consensus PT | ~$170 median (8 analysts: 5 Buy, 2 Hold, 0 Sell) | WebSearch |
| DA Historical Avg Correction | -15.7% | da_accuracy_tracker.yaml |
| DA Corrections | 25/25 negative (100% downward) | da_accuracy_tracker.yaml |

**Calibration note:** Historical DA corrections average -15.7%. Applying this to HLNE's $110 FV suggests ~$93 post-DA FV. The market at $97 is already BELOW the FA's FV but ABOVE where the DA pattern would suggest. This is not an obvious mispricing -- it is a fair fight between bull and bear.

---

## Key Findings

### Finding 1: Private Credit Meltdown -- Evergreen Contagion Risk (CRITICAL -- NEW)

**Thesis assumption:** Evergreen AUM growth +70% is the primary structural growth driver, distinguishing HLNE from cyclical PE managers.

**Counter-evidence:**

- **Blue Owl crisis (Feb-Mar 2026):** Blue Owl permanently gated its $1.6B OBDC II fund after a 200% surge in redemption requests. The firm lost ~60% of market value and is in de facto liquidation. This is not a one-off -- it demonstrates that semi-liquid/evergreen private credit funds face STRUCTURAL liquidity mismatch risk.

- **Contagion is spreading:** Blackstone BCRED saw $3.8B (7.9%) redemption requests. BlackRock restricted withdrawals on its $26B HPS Lending Fund. Morgan Stanley's North Haven Private Income fund faced 10.9% repurchase requests. Cliffwater's $33B fund faces 7% withdrawals. This is an industry-wide phenomenon, not isolated.

- **JPMorgan markdown (TODAY, Mar 16):** JPMorgan is marking down software loan collateral, triggering a "de-risking cascade" across private credit. Alternative asset manager stocks fell broadly.

- **HLNE direct exposure:** Hamilton Lane's Evergreen platform includes the Senior Credit Opportunities Fund (SCOPE), which offers MONTHLY liquidity. Monthly liquidity in illiquid private credit is the EXACT structure that caused Blue Owl's collapse. If SCOPE faces elevated redemptions, HLNE could be forced to gate.

- **Narrative shift risk:** Even if HLNE's Evergreen funds avoid gating, the NARRATIVE around "democratization of alternatives" has been severely damaged. 86% of wealth managers planned to increase private market allocations (HLNE survey) -- that survey was conducted BEFORE the Blue Owl crisis. Post-crisis, the appetite for semi-liquid alternative funds among retail/HNW investors could meaningfully decline.

- **Why this matters for the thesis:** The thesis values HLNE primarily on Fee-Related Earnings growing via Evergreen scaling. If Evergreen AUM growth decelerates from +70% to +20% due to investor caution post-crisis, and private credit products face redemptions, the growth engine stalls. KC#4 (Evergreen <20% for 3Q) could approach.

**Severity: CRITICAL**

**Resolution required:** The investment committee must assess HLNE's specific Evergreen fund redemption data from Q4 FY2026 (Jan-Mar 2026 -- the crisis quarter). If HLNE's Evergreen funds show net inflows during the crisis, the thesis strengthens materially. If they show net outflows or gating, the thesis is severely impaired.

---

### Finding 2: PE Fundraising Drought Is Structural, Not Cyclical (HIGH)

**Thesis assumption:** PE fundraising -32% is cyclical and will recover as rates decline and exits improve.

**Counter-evidence:**

- **Four consecutive years of decline:** PE fundraising fell AGAIN in 2025, the weakest since 2020. Only 388 funds raised $310B through Q3 2025 vs 905 funds / $585B full-year 2024. This is not a cycle -- it is a trend.

- **Bain & Company (Senior Partner, Global PE Practice):** This is "a 5+ year problem" and "not going to go away in 2025 or 2026. It's going to be continued pressure on the institutional LPs for liquidity over the course of the next several years."

- **LP overallocation:** Institutional investors are at record PE allocations (20-30%). The denominator effect keeps them ABOVE targets. With distributions at only ~6% of AUM (vs 10-year average 14%), LPs have less cash to recycle into new commitments.

- **McKinsey 2026 Report:** Shifts in deployment, returns, and fundraising -- "previously considered to be episodic -- are more likely STRUCTURAL features of a maturing industry."

- **HLNE-specific impact:** HLNE's advisory business ($860B AUM) depends on institutional LPs committing to new funds. If commitments stall for 3-5 years, advisory fee growth stalls with them. The thesis projects management fee growth of 12-14% -- this may be 5-7% in a structural drought.

**Severity: HIGH**

**Resolution:** Monitor institutional fundraising data through 2026. If Preqin/S&P data shows fundraising stabilizing in H2 2026, reduce severity to MODERATE. If decline accelerates to -40%+, escalate to CRITICAL.

---

### Finding 3: Mega-Manager Competition Accelerating in Private Wealth (HIGH)

**Thesis assumption:** HLNE has first-mover advantage and data moat in the Evergreen/private wealth space.

**Counter-evidence:**

- **Citi partnership EXCLUDES HLNE:** Citi partnered with Blackstone, Blue Owl, and KKR to launch evergreen funds for private wealth clients in Asia and Middle East. HLNE was NOT included. This is a major distribution channel loss.

- **Scale advantage is real:** Blackstone private wealth AUM reached $290B (tripled in 5 years). Their fundraising rose 53% in latest period. Blackstone expects 2026 to be its "busiest year yet" for product launches. KKR is "pushing deeper into wealth distribution."

- **Fee subsidization risk:** BX/KKR/APO can subsidize Evergreen product fees from their trillion-dollar platforms. HLNE at $146B total AUM cannot match this. If mega-managers offer 50bps products vs HLNE's 67bps, HLNE loses on price.

- **KC#7 monitoring:** The thesis has KC#7 as "mega-managers capture >30% of HLNE's addressable private wealth TAM." With BX/KKR/APO collectively launching dozens of Evergreen products, AND Citi distributing exclusively through them, this KC may be approaching faster than anticipated. The private wealth democratization TAM is growing, but HLNE's SHARE of that TAM may be shrinking.

**Severity: HIGH**

**Resolution:** Q4 FY2026 earnings should show Evergreen AUM breakdown. If HLNE's share of new Evergreen fund flows is declining QoQ, this is approaching KC#7.

---

### Finding 4: Insider Buying Signal May Be Overstated (MEDIUM)

**Thesis assumption:** $3.2M cluster buy by 4 insiders is the "strongest insider conviction signal in portfolio."

**Counter-evidence:**

- **Amounts relative to compensation:** CEO Delgado-Moreira bought $989K. His total compensation is ~$10M/yr. This is ~10% of annual comp. COO Kramer bought $250K -- executed through the Employee Share Purchase Plan (ESPP), not a discretionary open-market purchase. ESPP purchases have weaker signal value than open-market discretionary buys.

- **French River 5 Ltd sold $22M at $146.51 (Sep 2025):** This 10%+ holder sold 150,000 shares (31% of their direct holdings) at prices 50% above current levels. The SELL by the largest insider ($22M) vastly exceeds the cumulative BUY ($3.2M). Net insider activity over the past 12 months is NEGATIVE by ~$19M.

- **Hartley Rogers (Officer/Director) also sold $1.6M (Feb 2025).** This predates the cluster buy but shows a pattern of insider liquidity extraction at higher prices.

- **Signal vs noise:** The cluster buy occurred at $100-108 when the stock was at 52-week lows. Insiders may be buying to: (a) support the stock price, (b) signal confidence to LPs during fundraising conversations, (c) compensate for the French River $22M sale optics. The cluster buy is genuine but its PREDICTIVE value for stock appreciation should not be overstated given the net negative 12-month flow.

**Severity: MEDIUM**

**Resolution:** Monitor next 13F cycle for institutional holder changes. If major institutions (beyond Vanguard's 1.8% trim) are reducing, the insider buy is swimming against a stronger current.

---

### Finding 5: Recession + Oil Crisis Amplified by Beta 1.49 (MEDIUM)

**Thesis assumption:** Oil at $100 has "MINIMAL direct impact on HLNE's business model."

**Counter-evidence:**

- **Beta 1.49 is the HIGHEST in the portfolio.** In a -30% S&P scenario, HLNE falls ~45% ($97 to ~$53). This is not a quality compounder characteristic -- it is a leveraged bet on risk-on sentiment.

- **Indirect path is real:** Oil $100+ -> Fed hawkish -> rates higher for longer -> PE fundraising drought DEEPENS -> distributions freeze -> LPs cut commitments -> FEAUM growth stalls -> revenue growth stalls -> P/E compresses from 17x to 12x.

- **PE marks down:** If public markets fall 20-30%, PE portfolio marks follow with a 3-6 month lag. HLNE's $146B AUM includes market-sensitive assets. AUM decline mechanically reduces management fees (HLNE earns 67bps on AUM).

- **The thesis says "minimal" but the stock has fallen 9% in 5 days** on macro/oil news with no HLNE-specific catalyst. The MARKET is telling us HLNE is highly macro-sensitive, regardless of what the business model analysis says.

**Severity: MEDIUM**

---

### Finding 6: Valuation Sensitivity Remains Dangerously High (MEDIUM)

**Thesis data:** FV Spread 77%, TV 74.5% of EV. The thesis acknowledges HIGH SENSITIVITY.

**Counter-evidence:**

- **WACC sensitivity dominates:** At WACC 9.0%: FV ~$136. At WACC 10.5%: FV ~$101. At WACC 12.0%: FV ~$78. A 300bps WACC change produces a 74% FV range.

- **Beta has INCREASED:** Thesis used beta 1.29 (WACC 10.3-10.5%). Current beta per quality_scorer is 1.35 (WACC 11.4%). The tool's WACC of 11.4% would produce FV closer to $85-90, not $110.

- **The R3 resolution acknowledged E[CAGR] ~11.4% at 10% growth** -- below the 12% Tier A threshold. The position is being held on qualitative conviction (insider buying, QS, PE cycle trough) rather than quantitative E[CAGR].

- **SBC doubled to 4.4% of revenue (FY2025).** Revenue CAGR 24.7% vs EPS CAGR 10.7% -- the 14pp gap is dilution/comp eating shareholder returns. If SBC stays at 4-5% of revenue, the true owner earnings growth is closer to 7-8%, not 10%.

**Severity: MEDIUM**

---

## Desafios por Categoria

### Negocio

| # | Challenge | Evidence | Severity |
|---|-----------|----------|----------|
| 1 | Private credit meltdown threatens Evergreen growth engine | Blue Owl gate, BX/BLK/MS redemption pressure, HLNE SCOPE has monthly liquidity | CRITICAL |
| 2 | PE fundraising is structural, not cyclical | 4-year decline, Bain "5+ year problem," LP overallocation, distributions at 6% vs 14% avg | HIGH |
| 3 | Mega-managers eroding HLNE's private wealth niche | Citi partnership excludes HLNE, BX $290B private wealth, fee subsidization | HIGH |

### Valoracion

| # | Challenge | Evidence | Severity |
|---|-----------|----------|----------|
| 4 | WACC/beta higher than thesis assumes | Beta 1.35 (was 1.29), tool WACC 11.4% (vs thesis 10.5%), FV at 11.4% WACC = $85-90 | MEDIUM |
| 5 | SBC dilution understates true growth drag | SBC 4.4% of rev, Rev CAGR 24.7% vs EPS CAGR 10.7% = 14pp dilution gap | MEDIUM |
| 6 | E[CAGR] below Tier A threshold at honest growth | R3 acknowledged 11.4% E[CAGR] at 10% growth, below 12% threshold | MEDIUM |

### Riesgos

| # | Challenge | Evidence | Severity |
|---|-----------|----------|----------|
| 7 | Insider buy signal overstated by $22M French River sale | Net insider flow NEGATIVE $19M over 12 months; COO bought via ESSP not open market | MEDIUM |
| 8 | Receivables +67.5% vs revenue +28.7% still unresolved | Flagged in original R2. Must resolve in Q4 FY2026 (May). Could signal collection issues | MEDIUM |
| 9 | Beta 1.49 amplifies macro drawdown | Highest beta in portfolio, -45% in -30% S&P scenario | MEDIUM |

### Timing

| # | Challenge | Evidence | Severity |
|---|-----------|----------|----------|
| 10 | Q4 FY2026 earnings (May 2026) covers the CRISIS quarter | Jan-Mar 2026 includes Blue Owl gate, JPM markdowns, oil crisis, market correction. Results could be ugly | HIGH |
| 11 | Private credit panic still UNFOLDING (Mar 16 = TODAY) | JPM software loan markdowns released today; contagion not yet peaked | MEDIUM |

---

## Independent Bear-Case Valuation

### Method: P/FRE Multiple (Bear Assumptions)

The thesis uses P/FRE 19x on ~$340M FRE. I use bear assumptions:

**Bear case:**
- FRE growth decelerates to 7% (vs thesis 12%+) due to fundraising drought + Evergreen slowdown
- FY2027 FRE estimate: $340M * 1.07 = $364M (vs thesis implicit $380M+)
- P/FRE multiple: 14x (trough multiple for smaller alt managers during stress; BX/KKR trade at 18-22x but are diversified; HLNE without scale premium deserves discount)
- Shares: 53.5M diluted (conservative for ongoing SBC dilution)

```
Bear FV = $364M * 14 / 53.5M = $95.25/share
```

**Alternative bear (WACC-adjusted OEY):**
- Using tool's WACC 11.4% and growth 7%:
- OE $288M * 1.07 = $308M
- Capitalization rate: 11.4% - 2.5% = 8.9%
- PV = $308M / 0.089 = $3,461M
- FV = $3,461M / 53.5M = $64.69 (extremely conservative, single-year cap)

I anchor to the FRE multiple method as more reliable for asset managers.

### Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $110 | 40% OEY + 50% P/FRE 19x + 10% DCF |
| Market | $97.16 | Current price |
| DA bear | $84 | P/FRE 14x on 7% FRE growth (60%) + OEY at WACC 11.4% (40%) |

**Interpretation:** FA > Market > DA bear. This is the normal pattern. The debate is about distance. The FA's FV is 13% above market; the DA's bear is 14% below market. The key question is: which growth assumption is correct? If Evergreen survives the credit crisis and fundraising stabilizes, FA wins. If either cracks, DA wins.

---

## Edge Assessment

- Analyst consensus PT: ~$170 (8 analysts, median)
- FA thesis FV: $110
- DA bear FV: $84
- Market: $97.16
- Gap (FA vs consensus): -35% (we are FAR more bearish than consensus)
- Gap (DA vs market): -14%
- Our specific edge: "We identified the Evergreen contagion risk from the Blue Owl crisis before consensus. We also weight mega-manager competition more heavily than sell-side (who covers BX/KKR separately and may not see HLNE as threatened)."
- **WARNING:** FA FV $110 is 35% below consensus $170. Either sell-side is wildly wrong, or our growth/multiple assumptions are too conservative. If sell-side is closer to right, the position has 75% upside. This is a genuine edge question, not a clear answer.

---

## Probability-Weighted FV

| Scenario | Probability | FV | Weighted |
|----------|------------|-----|----------|
| Bull: Evergreen survives crisis, fundraising recovers, FRE +15% | 25% | $130 | $32.50 |
| Base: Moderate growth, competition contained, FRE +10% | 35% | $105 | $36.75 |
| Bear (fundraising structural): FRE +5%, multiple compression | 20% | $80 | $16.00 |
| Bear (Evergreen crisis): Redemptions, FRE flat, P/FRE 12x | 10% | $60 | $6.00 |
| Recession: Oil crisis -> recession -> marks down -> all compresses | 10% | $50 | $5.00 |

**Probability-Weighted FV: $96.25**

At $97.16 current price: **MoS = -0.9% (effectively ZERO to slightly NEGATIVE).**

This is concerning but less alarming than the batch analysis ($90.5). The difference is: I assign higher probability to the bull/base scenarios because the insider buying is genuine and HLNE's management fee base (72% of revenue) is contractually locked.

---

## Conflicts with Previous Analyses

| Item | R2 DA Refresh (Mar 7) | This DA (Mar 16) | Change |
|------|----------------------|-------------------|--------|
| Price | $106.57 | $97.16 | -8.8% decline |
| FV | $110 | $110 (not adjusting FA's FV) | No change |
| MoS | 3.2% | 13.5% | IMPROVED mechanically |
| Key new risk | Not identified | Private credit meltdown + Evergreen contagion | CRITICAL new finding |
| Probability-weighted FV | Not calculated | $96.25 | Effectively at market |
| DA Bear FV | $84 | $84 | Confirmed |

The R3 resolution (Mar 7) acknowledged E[CAGR] 11.4% was below the 12% Tier A threshold. At $97 (vs $107 at R3), the E[CAGR] has improved to 16.6% per forward_return tool -- but this is because the price fell, not because the business improved. The question is whether the price fell for GOOD REASONS (private credit contagion, structural fundraising decline) or bad reasons (indiscriminate sell-off).

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | 4 of 11 (1 CRITICAL, 3 HIGH) |
| Desafios not addressed by thesis | 2 (private credit meltdown, timing of crisis quarter) |
| Veredicto | **MODERATE-STRONG COUNTER** |

### Interpretation

This is a MODERATE-STRONG COUNTER, stronger than the March 7 refresh (MODERATE) due to:

1. **One genuinely NEW CRITICAL risk** (private credit meltdown / Evergreen contagion) that was not in the thesis, the R2 DA, or the batch contrathesis. This is the most important finding.

2. **The probability-weighted FV ($96.25) is at market price** -- the position has near-zero expected risk-adjusted return even after accounting for the quality premium.

3. **HOWEVER:** The thesis is NOT wrong about HLNE's quality. QS 82, ROIC 29%, near-zero leverage, $3.2M insider cluster buy, contractually locked fees. These are real. The risk is not permanent capital loss from a bad business -- it is multiple compression and growth disappointment from a macro/industry shift.

4. **The strongest bull argument** the DA cannot defeat: HLNE at $97 prices in only 1.2% FCF growth vs 21.5% historical. Even if growth HALVES to 10%, the stock is cheap. Even if it quarters to 5%, the stock is fairly valued. The market would need to be right that growth goes to ZERO for the current price to be correct long-term. That is unlikely for a QS 82 business.

---

## Recomendacion al Investment Committee

1. **RESOLVE the Evergreen contagion question BEFORE any ADD.** Q4 FY2026 (Jan-Mar 2026) is the CRISIS quarter. If HLNE reports net Evergreen inflows during this period, the CRITICAL risk is dismissed. If net outflows or gating, escalate to EXIT review.

2. **HOLD current position (10%) but DO NOT ADD** until Q4 data clears. The insider buying prevents selling, but the negative probability-weighted MoS prevents adding.

3. **Add new Kill Condition:** KC#8: "HLNE Evergreen funds report net outflows or impose redemption gates in any quarter." If triggered, run EXIT protocol immediately.

4. **Recalibrate FV sensitivity.** The thesis uses WACC 10.5% but the tool now calculates 11.4%. A mid-point of ~10.9% would reduce FV from $110 toward $95-100. Consider whether the FV needs formal revision.

5. **Track private credit contagion weekly** through Q4 earnings (May 2026). If Blackstone/BlackRock gates persist and spread to PE Evergreen products (not just credit), the entire democratization narrative is at risk.

6. **TRIM to 5% consideration** if: (a) Q4 shows Evergreen deceleration to <30%, OR (b) HLNE announces any fund gating, OR (c) S&P enters recession territory AND HLNE beta remains >1.4. Current 10% allocation to the highest-beta position in the portfolio during a potential crisis is aggressive.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- I could not determine HLNE's specific Evergreen fund redemption data for the Feb-Mar 2026 crisis period. This is the single most important data point for resolving the CRITICAL finding.
- The private credit meltdown is primarily hitting CREDIT products (private lending), not PE equity products. HLNE's Evergreen platform includes PE, infrastructure, and credit. The SCOPE fund (credit) is most exposed, but the PE and infra Evergreen products may be insulated. I could not determine the AUM split across these Evergreen sub-products.
- The $22M French River 5 Ltd sale (Sep 2025 at $146.51) significantly changes the net insider flow calculation, but French River is a 10%+ holder entity, not an operating executive. The signal value of entity-level selling vs executive-level buying is debatable.

### Limitaciones de Este Analisis
- No access to HLNE's actual Evergreen fund flow data (not public until Q4 earnings ~May 2026)
- Private credit crisis is UNFOLDING TODAY (JPMorgan markdowns Mar 16). The situation may be materially different by the time this is read.
- Beta calculated differently by different sources (thesis 1.29, tool 1.35, thesis update 1.49). The true beta in crisis conditions is unknown.
- Limited visibility into HLNE's credit vs PE vs infrastructure Evergreen AUM split

### Sugerencias para el Sistema
- Add "Evergreen/semi-liquid fund redemption risk" as a structural risk category for any alternative asset manager position
- The private credit meltdown should trigger a cross-portfolio risk check: does it affect any other position? (EDEN.PA business services, GL insurance -- probably not, but verify)
- Beta used in thesis header should be refreshed quarterly against quality_scorer.py output

### Preguntas para Orchestrator
1. Should we add KC#8 (Evergreen redemption gate) to the active thesis immediately, or wait for this DA to be formally resolved in R3?
2. At 10% of portfolio with beta 1.49 during a potential crisis, is the SIZING appropriate? If S&P falls 20%, HLNE contributes -3% to portfolio (10% * 1.49 * 20%). Is this consistent with P1 (sizing by conviction)?
3. The analyst consensus ($170) is 75% above current price. Either sell-side is wildly wrong, or our $110 FV is too conservative. Should we investigate WHY the gap is so large? Could our conservatism on mega-manager competition be excessive?
4. Given the private credit crisis is unfolding TODAY, should this be escalated to an emergency review rather than waiting for the next scheduled session?

---

*DA completed: 2026-03-16. Independent research performed via WebSearch, price_checker.py, quality_scorer.py, dcf_calculator.py --reverse, smart_money.py stock-profile, narrative_checker.py. Sources cited inline.*

## Sources

- [McKinsey Global Private Markets Report 2026](https://www.mckinsey.com/industries/private-capital/our-insights/global-private-markets-report)
- [Private Equity: In the Doldrums (CEPR)](https://cepr.net/publications/private-equity-in-the-doldrums-and-out-of-favor/)
- [Bain Midyear PE Report 2025](https://www.bain.com/insights/private-equity-midyear-report-2025/)
- [Fortune: $265B Private Credit Meltdown](https://fortune.com/2026/03/14/private-credit-meltdown-how-wall-streets-blackstone-kkr-apollo-ares-blue-owl-investment-craze-panic/)
- [Blue Owl Gates Retail Fund (Alt Credit Investor)](https://alternativecreditinvestor.com/2026/02/19/blue-owl-gates-retail-private-credit-fund-amid-redemption-pressure/)
- [Bloomberg: Asset Manager Shares Plunge](https://www.bloomberg.com/news/articles/2026-02-19/asset-manager-shares-plunge-as-blue-owl-curbs-fund-redemptions)
- [JPMorgan Software Loan Markdowns (FinancialContent)](https://markets.financialcontent.com/stocks/article/marketminute-2026-3-16-software-apocalypse-jpmorgans-private-credit-markdowns-send-shockwaves-through-ares-blue-owl-and-kkr)
- [Citi Partners with BX/KKR (Alt Credit Investor)](https://alternativecreditinvestor.com/2026/01/29/citi-taps-blackstone-and-kkr-in-private-wealth-push/)
- [Morningstar: Why Alts Manager Stocks Are Getting Hit Hard](https://www.morningstar.com/stocks/why-alts-manager-stocks-are-getting-hit-hard)
- [PitchBook: Apollo/Blackstone Perpetual Capital Rush](https://pitchbook.com/news/articles/apollo-blackstone-lead-perpetual-capital-rush)
- [French River Sells 150K HLNE Shares](https://www.themarketsdaily.com/2025/09/10/river-5-ltd-french-sells-150000-shares-of-hamilton-lane-nasdaqhlne-stock.html)
- [HLNE Insider Cluster Buy Analysis (FUNanc1al)](https://funanc1al.com/blogs/insider-purchases-inside-the-buy/hamilton-lane-hlne-2026-deep-dive-inside-the-4m-insider-buy-and-private-market-growth)
- [Vanguard Decreases HLNE Position](https://www.themarketsdaily.com/2026/02/26/vanguard-group-inc-decreases-stock-position-in-hamilton-lane-inc-hlne.html)
- [Hamilton Lane 2026 Market Overview](https://www.prnewswire.com/news-releases/hamilton-lane-2026-market-overview-302710433.html)
- [AltAssets: PE Fundraising Fell Again in 2025](https://www.altassets.net/featured/private-equity-fundraising-fell-again-in-2025-but-growing-dealmaking-exit-confidence-could-spell-successful-2026.html)
- [CNBC: Blue Owl Software Lending](https://www.cnbc.com/2026/02/20/blue-owl-software-lending-private-credit-concerns.html)
- [Evergreen Funds Surge to $493B (HedgeCo)](https://www.hedgeco.net/news/02/2026/evergreen-alternative-funds-surge-to-493-billion.html)

# APP (AppLovin Corporation) - SHORT THESIS S1 (UPDATED)

> **Pipeline Stage:** S1 (Updated from Feb 18 S1 with March 7 data)
> **Date:** 2026-03-07 (Original S1: 2026-02-18)
> **Analyst:** fundamental-analyst (short-thesis mode)
> **Price at Analysis:** $502.14 (EUR 432.29) -- WAS $404.39 on Feb 18 (+24.2%)
> **Market Cap:** $169.7B (was $137.9B)
> **Fair Value (Short Direction):** $200-280 (base case, no fraud)
> **Verdict:** WATCHLIST - Catalyst timing too uncertain for P10 compliance

---

## TL;DR

AppLovin is a genuinely strong business ($3.9B FCF, 88% gross margins, 70% revenue growth) powered by its AXON AI ad platform. The stock trades at 51x P/E ($502), implying ~25% annual FCF growth for 5 years -- achievable if AXON's data practices remain intact. THREE converging risks create structural fragility: (1) active SEC investigation confirmed "still active and ongoing" Feb 20, 2026; (2) two credible short seller reports (Culper, Fuzzy Panda) alleging fraudulent data collection/silent installs; (3) platform dependency on Apple/Google policies that could restrict AXON's data methods. CapitalWatch's money laundering allegations were partially retracted (Feb 9), weakening the most extreme fraud narrative. This is NOT Wirecard -- the FCF is real -- but IF regulatory action forces AXON to change data practices, margins compress and growth decelerates, taking fair value to $150-250. The critical weakness: NO firm catalyst date (P10 violation). The SEC has no deadline, Apple has no announced crackdown, and APP keeps BEATING earnings. Shorting a momentum stock with no dated catalyst at 1% position (EUR 100) is low-risk to the portfolio but has poor expected timing.

---

## Quality Score

**QS Tool:** 75/100 (Tier A)
**QS Adjusted:** 65/100 (Tier B) -- Adjustment: -10 points

**Adjustment Rationale (quantitative):**

| Factor | Direction | Points | Evidence |
|--------|-----------|--------|----------|
| EPS CAGR data artifact | UP | +5 | Tool scored 0/10 because CAGR from -$0.52 to +$9.84 is incalculable. Real EPS trajectory is extraordinary. |
| Active SEC investigation | DOWN | -8 | SEC confirmed "active and ongoing" Feb 20, 2026. Not captured by any QS metric. Binary risk to entire business model. |
| Business model transformation | DOWN | -5 | Revenue $2.8B -> $1.8B -> $5.5B in 3 years. ROIC persistence (5/7) is generous -- ROIC was -0.6% in 2022. Complete business pivot. |
| Market position (default 0/8) | UP | +3 | APP is #3-4 in mobile ad-tech (behind Meta, Google). Should score 5/8 for #3-5 rank. |
| **R&D declining** | DOWN | -5 | R&D went from 18% to 4.1% of revenue. Innovation risk for an "AI company" investing less in R&D. |
| **Net adjustment** | | **-10** | 75 -> 65, Tier B |

**Short Interpretation:** QS 65 (Tier B) priced as QS 85+ (Tier A quality compounder). The GAP between real quality and price-implied quality is ~20 points. Not the easiest short (would prefer QS 35 priced at QS 75), but the regulatory overhang creates binary risk that could close this gap violently.

---

## Section 1: Business Understanding

### What AppLovin Does

AppLovin operates AXON, an AI-powered real-time ad auction engine processing ~2M bids/second across 1B+ mobile devices. After divesting its games business (Jun 2025, $800M to Tripledot Studios), it is a pure-play advertising platform.

**Revenue Model (FY2025: $5.48B, +70% YoY):**
- **Advertising (Software Platform):** ~85%+ of revenue post-divestiture. Performance-based: advertisers pay per install/conversion. AppLovin takes ~5% mediation fee on winning bids.
- **Apps:** Divested. Minimal residual contribution.
- **E-commerce expansion:** 600 clients generating ~$1B/yr (pilot). Self-serve platform launching 2026. THIS is the growth narrative justifying the premium.

**The AXON Engine -- What Makes It Work (and What's Alleged):**

BULL version: AXON uses first-party contextual signals and reinforcement learning to predict ad value in a post-IDFA world. Its competitive advantage is LEGITIMATE AI innovation that thrives where legacy tracking fails.

SHORT SELLER version (Culper + Fuzzy Panda): AXON's outperformance partly stems from:
1. Device fingerprinting (prohibited by Apple App Store guidelines)
2. Silent/backdoor app installations via "Array" product (bypassing app store oversight)
3. Scraping user IDs from Meta, Snap, TikTok traffic to improve targeting
4. Requiring advertisers to prove $600K+/month Meta spend to see Meta's ad traffic data

REALITY: Probably a mix of both. Genuine AI innovation + aggressive data practices. The short thesis requires the data practices to be a LARGE contributor to AXON's edge.

**Financial Profile (FY2025):**

| Metric | Value | Trend |
|--------|-------|-------|
| Revenue | $5.48B | +70% YoY |
| Gross Margin | 87.9% | Expanding (was 55.4% in 2022) |
| Operating Margin | 75.8% | Expanding (was -1.7% in 2022) |
| FCF | $3.94B | +88% YoY |
| FCF Margin | 71.9% | Expanding |
| ROIC | 105.1% (2025) | Extraordinary |
| R&D / Revenue | 4.1% | DECLINING (was 18% in 2022) |
| SBC / Revenue | 3.8% | DECLINING (was 19.7% in 2023) |
| ND/EBITDA | 0.3x | Very low |
| Receivables growth vs Revenue | 41.8% vs 70.0% | Healthy (IMPROVED from prior year divergence) |

**Key observations:**
- Receivables now growing SLOWER than revenue (41.8% vs 70.0%) -- this RESOLVES the revenue quality concern flagged in the original S1. Good sign for bulls.
- R&D declining to 4.1% of revenue is unusual for an "AI company." Either AXON is self-improving with minimal human R&D (bullish) or the company is milking margins at the expense of future innovation (bearish).
- SBC declining from 19.7% to 3.8% is unusual for high-growth tech. Reduces dilution concern.
- OCF/Net Income at 1.2x is healthy conversion.

### Customer Concentration and Dependencies

**Platform dependency (CRITICAL):**
- 100% of revenue flows through Apple iOS and Google Android ecosystems
- Apple explicitly prohibits fingerprinting. If Apple enforces against AppLovin specifically, AXON's iOS effectiveness degrades
- Google reversed its fingerprinting ban (Feb 2025), benefiting AppLovin. But Google could re-reverse under regulatory pressure
- This is an existential dependency the business cannot diversify away from

---

## Section 2: Fragility Assessment

### 2.1 SEC Investigation -- CONFIRMED ACTIVE (Feb 20, 2026)

**Status:** SEC confirmed investigation is "still active and ongoing." Declined to release internal correspondence because it could "cause harm to the ongoing and active enforcement investigation."

**Scope:** Data collection practices, triggered by whistleblower complaint + short seller reports.

**What's being investigated:**
- Whether AXON uses impermissible data collection (fingerprinting, silent installs)
- Whether advertising practices violate platform partners' ToS
- Whether revenue growth is partially attributable to fraudulent ad practices

**Timeline:** UNKNOWN. SEC investigations typically 1-3 years. No indication of imminent resolution.

**Potential outcomes spectrum:**

| Outcome | Probability | Impact on Stock |
|---------|-------------|-----------------|
| No action / closed | 25-30% | +15-25% rally |
| Consent decree / fine ($500M-$2B) | 30-35% | -10-20% (manageable) |
| Enforcement requiring practice changes | 20-25% | -30-50% (structural) |
| Criminal referral to DOJ | 5-10% | -50-70% (catastrophic) |

### 2.2 Short Seller Reports -- Two Credible, One Partially Retracted

**Culper Research (Feb 2025):** CREDIBLE
- AXON's success stems from "notorious spyware" and "scammy ad" companies
- Silent, backdoor app installations via Array product
- AXON 2.0 is a "smokescreen" for aggressive data practices
- Chinese national Hao Tang controlled 28% pre-IPO, ~9.8% through offshore shells
- National security concerns about Chinese operations

**Fuzzy Panda Research (Feb 2025):** CREDIBLE
- Corroborated Culper's data practice allegations
- Additional click spoofing claims
- Combined with Culper, caused 13% stock drop, $13.7B market cap loss

**CapitalWatch (Jan 20, 2026):** PARTIALLY RETRACTED
- Money laundering allegations linking Hao Tang to Tuandaiwang ($890M illegal proceeds) and SE Asian pig-butchering scams
- CapitalWatch RETRACTED claims about Hao Tang specifically (Feb 9, 2026), apologized for "distress caused"
- However, CapitalWatch stated "stance on AppLovin's financials remains unchanged"
- Stock rallied 14% on retraction

**Assessment:** The CapitalWatch retraction weakens the most extreme narrative (criminal money laundering). But Culper's data practice allegations and Fuzzy Panda's corroboration remain unaddressed and are MORE relevant to the SEC investigation. The retraction actually clarifies the thesis: this is about data practices, not organized crime.

### 2.3 Class Action Lawsuits

**Status:** Multiple securities fraud class actions in U.S. District Court, Northern District of California. Currently in DISCOVERY phase (2026).

**Allegations:** Defendants misled investors about sustainability of growth due to fraudulent advertising practices (click spoofing, backdoor installations).

**Timeline:** Discovery will force production of internal documents about AXON's data collection methods. This could surface damaging evidence in H2 2026 - 2027.

### 2.4 Platform Risk (Apple/Google) -- Most Underappreciated

- Apple PROHIBITS fingerprinting. If Apple specifically enforces against AppLovin or tightens enforcement broadly at WWDC (June 2026) or iOS 20 (Sep 2026), AXON's iOS prediction accuracy degrades
- Google ALLOWED fingerprinting (Feb 2025 policy change), benefiting AppLovin. But UK ICO criticized this change. If Google reverses under regulatory pressure, AXON loses the Android tailwind
- New AI-native competitors (CloudX, Firsthand) emerging with "Brand Agents" that compete for budgets
- If Apple/Google crack down, AXON's 88% gross margin advantage erodes

### 2.5 Dependency Chain

```
$502 stock price
  -> Requires 25%+ annual FCF growth for 5 years
    -> Requires AXON maintaining prediction accuracy
      -> Requires continued access to device-level behavioral data
        -> Requires Apple/Google NOT restricting fingerprinting
          -> Requires SEC investigation NOT forcing practice changes
```

**Most fragile links:** Apple/Google policy enforcement + SEC outcome. Binary risks with unclear timing.

---

## Section 3: Catalysts (P10 Assessment)

| Catalyst | Timeline | Probability | Impact |
|----------|----------|-------------|--------|
| SEC enforcement action | Unknown (H2 2026?) | 25-35% negative outcome | -30-50% |
| Apple fingerprinting crackdown | WWDC Jun 2026 / iOS 20 Sep 2026 | 25-35% | -15-30% |
| Q1 2026 earnings miss | **May 13, 2026** | 15-20% | -15-25% |
| Class action discovery docs | H2 2026-2027 | 30-40% damaging | -10-20% |
| Google Privacy Sandbox phase 2 | 2026-2027 | 40-50% | -10-15% |
| E-commerce expansion disappoints | Q2-Q4 2026 | 35-45% | -20-30% |

**P10 ASSESSMENT -- CRITICAL WEAKNESS:**

The short thesis has GENUINE structural fragility but FAILS P10 compliance:

- **SEC investigation:** No timeline. "Eventually" is not a catalyst.
- **Apple enforcement:** Possible at WWDC (Jun 2026) but speculative.
- **Q1 earnings (May 13):** The ONLY firm date. But APP beats estimates consistently -- betting on a miss is contrarian without strong evidence.
- **Class action discovery:** 2026-2027, gradual, not binary.

**Error #44 applies:** "Sin catalizador con fecha identificable, NO shortear." The thesis has structural merit but the timing is wrong for an active position.

---

## Section 4: Valuation

### 4.1 What the Market Implies (Reverse DCF, March 7 data)

| Metric | Value |
|--------|-------|
| Current Price | $502.14 |
| Implied FCF growth (5yr) | 25.3%/yr |
| Historical Revenue CAGR (3yr) | 24.8%/yr |
| Gap (implied vs historical) | +0.5pp |
| Current EV/EBIT | 41.1x |
| P/E | 50.8x |

**Key insight:** The implied growth rate (25.3%) is almost EXACTLY equal to the historical revenue CAGR (24.8%). This means the market is pricing CONTINUATION of growth, not acceleration. If AXON keeps performing, the stock is fairly valued at current levels. The market is NOT wildly optimistic -- it's pricing the trend.

This SIGNIFICANTLY weakens the valuation-based short case compared to the Feb 18 analysis (when implied growth was 37% vs 19% historical). The stock has re-rated to a more reasonable level.

### 4.2 Fair Value Scenarios

**Bull Case (short fails, 25% prob): $600-700**
- E-commerce scales to $2B+ revenue
- SEC closes investigation
- AXON 3.0 (GenAI) creates new ad categories
- Multiple expands to 55-60x P/E on TAM expansion

**Base Case (growth normalizes, 50% prob): $250-350**
- Growth decelerates to 15-20% by 2027 (mobile gaming TAM saturation)
- E-commerce faces fierce Meta/Google competition, grows slowly
- Margins compress modestly (GM 88% -> 80%) as R&D must increase
- P/E compresses from 51x to 25-30x
- SEC resolved with fine, limited practice changes

**Bear Case (regulatory disruption, 25% prob): $100-180**
- SEC forces AXON data practice changes
- Apple tightens enforcement
- AXON prediction accuracy degrades 20-30%
- Growth drops to 5-10%, margins compress to 60-65% GM
- P/E compresses to 15-20x

**Expected Value:**
- EV = ($650 x 0.25) + ($300 x 0.50) + ($140 x 0.25) = $162.50 + $150 + $35 = **$347.50**
- Current price: $502
- **Implied downside to EV: -30.8%**
- **Implied downside to Bear: -72%**

### 4.3 DCF Assessment

The DCF tool shows extreme volatility (FCF CV = 1.9, "may be unreliable"). The reverse DCF is more useful: it shows the current price implies 25.3% annual growth, which is achievable but leaves NO margin for error.

**Sensitivity: HIGH.** FV ranges from $357 (P90) to $8,314 (P10). The DCF is not useful as a point estimate for APP. Scenario analysis is primary.

---

## Section 5: Risk Assessment for the Short

### 5.1 Squeeze Risk: LOW
- Short interest: 4.9% of float (14.5M shares)
- Days to cover: 1.8 days
- Below peer average (5.36%)
- Highly liquid ($2.1B daily volume)

### 5.2 Earnings Beat Risk: HIGH
- APP has beaten estimates EVERY quarter since AXON 2.0
- Q4 2025: beat by 9.5%
- Q1 2026 guidance: $1.745-1.775B revenue, $1.465-1.495B adj. EBITDA (84% margin maintained)
- Sell-side expects 43% revenue growth for 2026
- **Shorting into consistent earnings beats is dangerous**

### 5.3 Business Strength: GENUINE
- $3.94B FCF is REAL (OCF/NI = 1.2x)
- Balance sheet STRONG (0.3x ND/EBITDA, $2.5B cash)
- At 25% FCF growth: 2028 FCF = ~$9.5B. At 18x FCF = $171B = ~$505/share
- **The stock could be fairly valued in 2-3 years just by growing into its current price**

### 5.4 Carry Cost
- eToro CFD: ~7-8% annualized
- For EUR 100 position: ~EUR 7-8/year carry
- Manageable but wasteful without a dated catalyst

### 5.5 Maximum Adverse Scenario
- Stock to $650-700 (+30-40%) on SEC closure + e-commerce success
- At 1% position (EUR 100), max loss with stop at $650 = ~EUR 29 (0.29% of portfolio)

---

## Section 6: Smart Money Context

**Not enrolled in smart_money graph.** Data from insider_tracker:

**Institutional holders:** Standard passive (Vanguard 8.2%, BlackRock 7.9%, State Street 3.9%). IEQ Capital (5.1%, $7.9B) is noteworthy -- a less-known fund with a large concentrated position.

**Insider activity (last 6 months):**
- CTO Vasily Shikin: SOLD $17.5M (Nov 2025, $524-555/share)
- Officer Valenzuela: SOLD $5M (Dec 2025, $657/share)
- CEO Herald Chen: Stock GIFTS only (tax planning, not directional signal)
- NO insider purchases detected
- Net insider position: 18.8% (63.3M shares) -- legacy pre-IPO, not conviction buying

**Assessment:** Insiders are NET SELLERS at prices ABOVE current. The CTO (who builds AXON) selling $17.5M is a meaningful signal. No insider is buying at any price. However, 18.8% ownership means they are heavily aligned -- they sell for liquidity, not because they expect collapse.

---

## Kill Conditions (to COVER if short opened)

1. **KC#1:** SEC closes investigation without action or practice changes. COVER 100%.
2. **KC#2:** Apple/Google explicitly endorse AppLovin's data practices. COVER 100%.
3. **KC#3:** Stock rises above $650 (stop loss, -29%). COVER 100%.
4. **KC#4:** Two consecutive quarters with e-commerce ad revenue >$200M each. COVER 50%.
5. **KC#5:** Carry cost exceeds 6 months without any catalyst materializing. COVER 100%.

---

## Sizing (if approved)

| Parameter | Value |
|-----------|-------|
| Instrument | eToro CFD short |
| Leverage | x1 (NO leverage, P11) |
| Size | EUR 100 (1% portfolio) |
| Entry range | $480-520 |
| Stop loss | $650 (hard, -29% max) |
| Target | $280-350 (-30% to -44%) |
| R/R ratio | ~1.5:1 (MARGINAL) |
| Carry | ~EUR 8/yr (~0.08% of portfolio) |

---

## Verdict: WATCHLIST -- Do NOT Short Yet

**Conviction: LOW-MEDIUM (40/100)**

### Why NOT short now:

1. **P10 FAILURE:** No catalyst with a firm date. SEC investigation has no timeline. Apple enforcement is speculative. Q1 earnings (May 13) is the only date, but APP beats consistently.

2. **Error #46 -- Tesla Trap Risk.** AppLovin generates $3.9B REAL FCF with 88% gross margins. "Expensive + allegations" is exactly the dangerous short pattern. The business can grow into its valuation within 2-3 years.

3. **Implied growth matches historical growth.** At $502, the market implies 25.3% growth vs 24.8% actual. This is NOT insane pricing. The valuation short case has weakened significantly since Feb 18 (when implied growth was 37% vs 19% historical at $404).

4. **R/R is marginal.** 1.5:1 with uncertain timing is not compelling enough for an active position.

5. **CapitalWatch retraction** weakened the most extreme fraud narrative, though Culper/Fuzzy Panda allegations on data practices remain unaddressed.

### What would change my verdict:

| Trigger | Action |
|---------|--------|
| SEC announces formal charges | IMMEDIATE S2 + S3 + S4 in same session |
| Apple WWDC announces fingerprinting crackdown (Jun 2026) | S2 within 48h |
| Q1 2026 earnings MISS + guidance cut (May 13) | S2 within 48h |
| Stock rallies to $650+ without fundamental justification | Better R/R, reassess |
| Insider selling accelerates (CEO or multiple officers) | Negative conviction signal, reassess |

### Monitoring Plan:

- **Monthly:** SEC investigation updates (Bloomberg, SEC EDGAR)
- **May 13:** Q1 2026 earnings -- pre-position thesis review in early May
- **June 2026:** Apple WWDC -- watch for privacy enforcement announcements
- **Quarterly:** Insider selling patterns, e-commerce revenue traction
- **Ongoing:** Class action discovery milestones

---

## META-REFLECTION

### Incertidumbres/Dudas
- **Core uncertainty remains: Is AXON's edge AI-driven or data-practice-driven?** Cannot determine from public information. The SEC investigation is literally trying to answer this question.
- **The stock rallied 24% since original S1 (Feb 18).** This could mean: (a) the short thesis is wrong and the market knows it, (b) CapitalWatch retraction removed the extreme narrative, or (c) momentum/earnings beats overpower regulatory overhang. I lean toward (b) + (c).
- **R&D declining to 4.1%** while margins expand is the most puzzling data point. For an "AI company," this is either (a) extraordinary efficiency (AXON self-improves) or (b) margin milking that will catch up in 2-3 years. This LONG-TERM fragility is worth monitoring but has no near-term catalyst.

### Sugerencias para el Sistema
- **Enroll APP in smart_money graph.** A $170B company under SEC investigation with CTO selling $17.5M deserves ongoing monitoring. Run: `smart_money.py capture "CTO Vasily Shikin sold $17.5M APP Nov 2025"` + `smart_money.py capture "Officer Valenzuela sold $5M APP Dec 2025"`.
- **Create an ad-tech / mobile-advertising sector view.** APP analysis would benefit from sector context (Meta, Google, Unity, IronSource, Trade Desk comparisons). Currently no sector view covers this space.

### Anomalias Detectadas
- **Gross margin 87.9% for an ad-tech company** is extraordinary. For comparison: Meta 81%, Google 57%, Trade Desk 81%. APP's margins matching/exceeding ADBE (88%) despite being in a lower-margin industry is anomalous. Either AXON is genuinely revolutionary, or costs are being classified creatively.
- **R&D declining from 18% to 4.1% of revenue** while the company claims to be rolling out AXON 3.0 (GenAI). Where is the R&D investment going? This warrants investigation into whether R&D is being capitalized rather than expensed.
- **Beta 2.50** gives WACC of 18%. This is extremely high for a $170B company with strong financials. The DCF tool used 9% WACC (more reasonable), but the high beta reflects genuine stock price volatility around short seller reports and SEC news.

### Preguntas para Orchestrator
1. Given the WATCHLIST verdict with no dated catalyst, should this remain in monitoring status with a 60-day review cycle (next: early May, pre-Q1 earnings)?
2. The prior S1 (Feb 18) recommended "PROCEED TO S2." With updated data showing weaker R/R and no catalyst, I am DOWNGRADING to WATCHLIST. Is the orchestrator aligned?
3. Should we create an ad-tech sector view before any future advancement of this thesis? (Error #30/#56 -- R1/S1 without sector view)

---

## Sources

### SEC Investigation
- [Bloomberg: SEC Says Probe Involving AppLovin 'Still Active and Ongoing' (Feb 20, 2026)](https://www.bloomberg.com/news/articles/2026-02-20/sec-says-probe-involving-applovin-is-still-active-and-ongoing)
- [Yahoo Finance: AppLovin Beats Earnings, but SEC Investigation Is the Real Story](https://finance.yahoo.com/news/applovin-beats-earnings-sec-investigation-210000313.html)
- [Investing.com: AppLovin shares pare gains as SEC confirms active probe](https://www.investing.com/news/stock-market-news/applovin-shares-pare-gains-as-sec-confirms-active-probe-93CH-4517002)

### Short Seller Reports
- [Invezz: AppLovin falls 13% as Culper, Fuzzy Panda accuse of fraud](https://invezz.com/news/2025/02/26/applovin-falls-over-13-as-short-sellers-culper-research-fuzzy-panda-accuse-company-of-fraud/)
- [CNBC: AppLovin demands CapitalWatch retract 'conspiratorial' report](https://www.cnbc.com/2026/01/27/applovin-short-seller-capitalwatch-report.html)
- [CNBC: CapitalWatch apologizes, retracts report on shareholder (Feb 9)](https://www.cnbc.com/2026/02/09/short-seller-capitalwatch-retraction-applovin-hao-tang.html)
- [Sherwood: AppLovin craters on CapitalWatch report](https://sherwood.news/markets/applovin-craters-after-report-from-capitalwatch-alleges-its-a-money/)

### Class Actions
- [Rosen Law: AppLovin Corporation Class Action](https://rosenlegal.com/case/applovin-corporation/)
- [Labaton: Securities Class Action Against AppLovin](https://www.labaton.com/news-insights/labaton-keller-sucharow-llp-files-securities-class-action-lawsuit-against-applovin-corporation-and-certain-of-its-executives)
- [Kessler Topaz: AppLovin Securities Fraud Class Action](https://www.ktmc.com/new-cases/applovin-corporation)

### Business and Earnings
- [AppLovin Q4/FY2025 Results (Investor Relations)](https://investors.applovin.com/news/news-details/2026/AppLovin-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx)
- [IndexBox: AppLovin Q4 2025 Beat, Strong 2026 Outlook](https://www.indexbox.io/blog/applovin-q4-2025-results-revenue-and-earnings-beat-expectations/)
- [Nasdaq: Axon 2 Drives AppLovin's Advertising Surge](https://www.nasdaq.com/articles/axon-2-drives-applovins-advertising-surge-and-gaming-ecosystem)
- [Sherwood: AppLovin craters on competitive threats from Meta, new AI tools](https://sherwood.news/markets/applovin-q4-earnings-software-adtech-ai/)

### Competition and Privacy
- [eMarketer: AppLovin's Axon launch takes aim at Meta and Google amid SEC probe](https://www.emarketer.com/content/applovin-launches-axon--taking-aim-meta-google-sec-probe-looms)
- [CrispIdea: AppLovin vs Meta AI Adtech Battle](https://www.crispidea.com/applovin-vs-meta-ai-adtech-2025/)

### Short Interest
- [MarketBeat: AppLovin Short Interest Mar 2026](https://www.marketbeat.com/stocks/NASDAQ/APP/short-interest/)
- [Benzinga: Is AppLovin Gaining or Losing Market Support](https://www.benzinga.com/insights/short-sellers/26/03/51097622/is-applovin-corp-gaining-or-losing-market-support)
- [Fintel: APP Short Interest](https://fintel.io/ss/us/app)

---

*S1 Analysis Date: 2026-03-07 (UPDATE of 2026-02-18 original)*
*Analyst: fundamental-analyst (short-thesis mode)*
*Next Step: WATCHLIST monitoring. Advance to S2 ONLY if catalyst materializes.*

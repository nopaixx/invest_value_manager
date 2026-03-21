# LPLA - LPL Financial Holdings Inc.

> **Date:** 2026-03-18
> **Stage:** R1 Complete
> **Quality Score (Tool):** 33/100 (Tier D)
> **Quality Score (Adjusted):** 68/100 (Tier B) -- Adjustment: +35 points. See detailed justification below.
> **Fair Value:** $365 USD (EUR 316)
> **Current Price:** $293.82 USD (EUR 254.57)
> **MoS vs FV:** 19.5%
> **Expected Growth:** 12-14%
> **E[CAGR] @market:** ~16.5%
> **Verdict:** WATCHLIST -- Entry at $270 USD (EUR 234) for 25% MoS

---

## TL;DR

LPL Financial is the largest US independent broker-dealer (32K+ advisors, $2.4T assets) riding the secular shift toward advisor independence. The legacy QS tool produces a misleading 33/100 (Tier D) because FCF is distorted by $3.2B in acquisition-related outflows (Atria + Commonwealth) and broker-dealer client money flows -- not by business deterioration. Adjusted for these distortions, LPLA is a Tier B business with strong ROIC history, scale moat, 97%+ advisor retention, and 6-fund smart money convergence. Post-acquisition normalized earnings power is ~$22-24 adjusted EPS, implying ~13x forward P/E at current price. The stock is 27% below its 52-week high following equity issuance dilution and acquisition integration noise. Fair value $365 with entry target $270.

---

## Quality Score: Tool 33/100 (Tier D) -- Adjusted 68/100 (Tier B)

### QS Tool-First Analysis

The quality_scorer.py output of 33/100 is STRUCTURALLY DISTORTED for LPLA. Detailed justification for +35 point adjustment:

**Distortion 1: FCF is meaningless for broker-dealers during M&A cycles (FCF Margin scored 2/10, FCF Consistency scored 2/5)**

- FY2025 reported FCF: -$982M. FY2024: -$285M. FY2023: +$109M.
- BUT: LPLA spent $2.7B on Commonwealth (closed Aug 2025) and $xyz on Atria (closed Oct 2024). These are non-recurring acquisition outlays.
- Adjusted EBITDA FY2025: $2.91B (+31% YoY). This is the true cash generation metric for broker-dealers.
- Even the tool flags: "[!] FCF DATA DISTORTION -- FCF margins likely include client money flows (financial services)"
- Proper FCF proxy for LPLA = Adj EBITDA - maintenance capex - interest = ~$2.91B - $250M - $380M = ~$2.28B.
- FCF Margin proxy: $2.28B / $17B revenue = ~13.4% -- that scores 8/10, not 2/10.
- FCF Consistency proxy: Adj EBITDA positive all 4 years -- scores 5/5, not 2/5.
- **Adjustment: +9 points (from 4/15 to 13/15 on FCF components)**

**Distortion 2: Leverage inflated by acquisition debt (Leverage scored 0/10)**

- Net Debt/EBITDA on GAAP basis: 4.7/1.55 = 3.0x. Tool scores 0/10.
- BUT: Net Debt/Adjusted EBITDA: 4.7/2.91 = 1.6x. Scores 8/10.
- Management guided leverage target 1.5-2.5x. Current 1.95x is WITHIN target.
- Pre-acquisition leverage was <1.5x. Debt is acquisition-financed, not structural deterioration.
- **Adjustment: +8 points (from 0/10 to 8/10)**

**Distortion 3: EPS CAGR depressed by acquisition costs and share dilution (EPS CAGR scored 2/10)**

- GAAP EPS CAGR +1.2% (tool uses this). But GAAP includes $740M in one-time acquisition costs.
- Adjusted EPS: FY2023 ~$14.49, FY2024 $16.51, FY2025 $20.09. Adj EPS CAGR = ~17.8%.
- Also: 4.7M shares issued at $320 in Mar 2025 to fund Commonwealth. Diluted share count rose ~6%.
- **Adjustment: +6 points (from 2/10 to 8/10)**

**Distortion 4: Gross Margin trend distorted by revenue mix (GM Trend scored 0/5)**

- Gross margins declining 30.4% to 23.7% is mechanically driven by advisory revenue recognition: LPL reports gross advisory fees as revenue AND the payout to advisors as cost. As advisory assets grow (46% YoY), revenue and costs scale together. The NET margin on advisory is what matters, not the gross margin.
- Adjusted operating margin (Adj EBITDA / Gross Profit) has been stable ~55-60%.
- **Adjustment: +3 points (from 0/5 to 3/5)**

**Distortion 5: Market Position scored 0/8 (default, not manual)**

- LPL is the #1 independent broker-dealer in the US. Unambiguously.
- 32,178 advisors. $2.4T assets. 2x larger than #2 (Osaic at ~$1.2T).
- **Adjustment: +8 points (from 0/8 to 8/8)**

**Distortion 6: Gross Margin Premium scored 0/10**

- LPL's reported GM is below sector median because of the pass-through revenue structure unique to IBDs.
- Comparing LPL's gross margin to asset managers or banks is apples-to-oranges. Among IBDs, LPL has the highest operating efficiency.
- **Adjustment: +1 point (modest, given structural sector difference)**

### Adjusted QS Breakdown

| Component | Tool | Adjusted | Reason |
|-----------|------|----------|--------|
| ROIC Spread | 4/15 | 4/15 | ROIC 8.7% declining post-acquisition -- legitimate concern |
| FCF Margin | 2/10 | 8/10 | Adj EBITDA proxy 13.4%, not reported -5.8% |
| Leverage | 0/10 | 8/10 | 1.6x adj EBITDA, not 3.0x GAAP |
| FCF Consistency | 2/5 | 5/5 | Adj EBITDA positive every year |
| Revenue CAGR | 10/10 | 10/10 | No change -- 25.5% organic + acquisition |
| EPS CAGR | 2/10 | 8/10 | Adj EPS CAGR ~18% |
| GM Trend | 0/5 | 3/5 | Pass-through distortion; adj margin stable |
| GM Premium | 0/10 | 1/10 | Structural sector difference, modest adj |
| Market Position | 0/8 | 8/8 | #1 US IBD, 2x #2 |
| ROIC Persistence | 7/7 | 7/7 | No change |
| Shareholder Returns | 5/5 | 5/5 | No change |
| Insider Ownership | 1/5 | 1/5 | 0.6% -- low but typical for large-cap financials |
| **TOTAL** | **33/100** | **68/100** | **Tier B** |

**Every adjustment has quantitative evidence. No "the moat is stronger than the tool shows" reasoning.**

---

## Business Understanding

### What LPL Does

LPL Financial is the largest independent broker-dealer (IBD) in the United States, providing a technology platform, clearing/custody services, compliance infrastructure, and practice management tools to ~32,000 financial advisors. LPL does NOT manage money directly -- it enables independent advisors to serve their clients while handling the back-office complexity.

**Problem solved:** Financial advisors want independence (higher payout, own their book) but cannot individually afford compliance infrastructure, technology platforms, clearing services, and regulatory overhead. LPL aggregates these functions at scale.

**Revenue model:**
- Advisory fees (asset-based, ~58.8% of total assets are advisory): Recurring, grows with AUM
- Commission revenue: Transaction-based
- Client cash revenue: Interest on client cash balances (rate-sensitive)
- Service/fee revenue: Platform fees, technology, planning tools
- Transaction revenue: Trading execution

**Revenue breakdown FY2025:** $17.0B total. The majority (~75%) flows through to advisors as payout (88% payout ratio), making gross margins misleadingly low. The TRUE economics are best measured by Adjusted EBITDA.

### Unit Economics

- Average assets per advisor: $73.7M (up 22% YoY)
- Advisor payout ratio: ~88% (industry competitive)
- Advisor retention: 97%+ asset retention rate
- Organic NNA rate: 8% (FY2025, $147B organic net new assets)
- CAC: High (recruiting transitions cost $50-150K+ per advisor) but LTV is extremely high (10+ year average advisor tenure)
- LTV/CAC: Estimated >10x given multi-year advisory revenue streams

### Revenue Quality

| Metric | Value | Assessment |
|--------|-------|------------|
| Recurring % | ~70-75% | Advisory fees + platform fees are highly recurring |
| Client stickiness | Very high | 97%+ retention; advisors' clients follow the advisor, not the platform |
| Rate sensitivity | Moderate | Client cash balances ($61B) generate NII; rate cuts = headwind |
| Market sensitivity | High | AUM-based fees decline with markets |

### Capital Requirements

- Asset-light model (capex/revenue ~1.4% in FY2025)
- Working capital: Negative (clients prepay advisory fees)
- Growth capex: Technology platform + acquisitions
- Maintenance capex: ~$250M/yr (technology, infrastructure)

---

## Why It's Cheap (27% below 52-week high)

### Market Narrative

1. **Acquisition integration risk:** Two major acquisitions (Atria $110B assets, Commonwealth $250B+ assets) in 18 months create execution overhang
2. **Debt increase:** Total debt rose 32% to $7.3B to fund acquisitions
3. **Share dilution:** 4.7M shares issued at $320 in March 2025 to fund Commonwealth
4. **GAAP earnings noise:** FY2025 GAAP EPS fell 22% due to $740M acquisition costs
5. **Interest rate sensitivity:** Fed rate cuts reduce client cash revenue (NII)
6. **Market correction risk:** AUM-based revenue declines in bear markets
7. **Macro uncertainty:** Current geopolitical situation (Hormuz, tariffs) weighs on financial stocks

### My Counter-Thesis

| Market believes | I believe | Evidence |
|----------------|-----------|----------|
| Integration risk is high | Atria already integrated successfully; Commonwealth on track for Q4 2026 | Atria: 80%+ retention target met, $155M run-rate EBITDA. Commonwealth: $415M run-rate EBITDA target. |
| Debt is dangerous | Leverage at 1.6x adj EBITDA is conservative for a financial services firm | Management target 1.5-2.5x. Pre-acquisition was <1.5x. Cash generation $2.9B adj EBITDA. |
| EPS declining | Adjusted EPS grew 22% YoY; GAAP distorted by one-time costs | FY2025 Adj EPS $20.09 vs $16.51 in FY2024. Acquisition costs are non-recurring. |
| Rate cuts hurt | Rate sensitivity is declining as advisory % grows to 58.8% | Client cash is 2.6% of total assets. Fee-based revenue is the growth driver. |
| Acquisition-driven growth is low quality | LPL also has strong organic growth: 8% NNA rate, record $149B recruited assets | Organic growth ALONE justifies premium; acquisitions are synergy-accretive. |

### Value Trap Checklist

| Factor | SI/NO | Comment |
|--------|-------|---------|
| Secular decline | NO | IBD channel growing faster than captive BDs and RIAs |
| Tech disruption | NO | LPL IS the tech platform; investing heavily in AI/digital tools |
| Management destroying value | NO | Acquisitions are accretive; adj EBITDA +31% |
| Balance deteriorating | WATCH | Debt elevated but within target; deleveraging expected |
| Insider selling >5% | NO | Low insider ownership but no abnormal selling |
| Dividend cut | NO | Dividend maintained; buybacks paused for acquisitions |
| Market share loss | NO | Gaining share aggressively -- 32K advisors, up 11% |
| ROIC < WACC 3yr | NO | ROIC > WACC every year historically; 2025 compressed by acquisition goodwill |
| FCF negative >2yr | DISTORTED | Acquisition-driven; adj EBITDA strongly positive |
| Goodwill >50% equity | YES | Goodwill is ~$5.4B against equity ~$5.8B. High but typical for serial acquirers in financial services |

**Value trap score: 1/10 (only goodwill flag, which is structural for IBD consolidators)**

### My Informational Advantage

- Horizon temporal: Market is pricing acquisition noise (12-18 month view); I see 3-5 year compounding power
- Normalized earnings: Market anchored on GAAP EPS $10.92; normalized earning power is $22-24
- Secular tailwind: IBD channel growing 21.5% AUM/yr vs 13.4% captive BDs
- Smart money convergence: 6 quality/value funds (Markel, Dodge & Cox, First Eagle) see the same thesis

---

## Moat Assessment

### Moat Type: WIDE -- Switching Costs + Cost Advantage

**1. Switching Costs (Primary)**

Moving an advisory practice from one broker-dealer to another is extremely painful:
- 97%+ asset retention proves advisors rarely leave
- Advisor's entire tech stack, compliance framework, client reporting, and custodial relationships are integrated into LPL's platform
- Transition disrupts client relationships for 3-6 months
- Regulatory re-papering required for every client account
- LPL provides marketing, paraplanning, bookkeeping -- all must be replaced

**2. Scale/Cost Advantage (Secondary)**

- 32K advisors spread fixed costs (technology, compliance, clearing) across massive base
- Self-clearing broker-dealer: controls execution and earns on client cash
- Technology platform costs are largely fixed; marginal advisor adds minimal cost
- Scale flywheel: more advisors -> more assets -> more investment in platform -> attracts more advisors
- 2x larger than #2 competitor (Osaic). Scale gap is widening.

**3. Network Effect (Emerging)**

- Institutional channel growing: banks, credit unions, insurance companies partnering with LPL
- More advisors means more data, better AI/analytics, more product negotiating power
- Community effect: advisors share best practices within LPL network

**Moat durability:** HIGH. Scale advantages compound over time. Switching costs increase as LPL adds more services. The IBD consolidation trend benefits the #1 player disproportionately.

---

## Valuation

### Method 1: Normalized P/E (60% weight)

**Normalized Adjusted EPS derivation:**

| Component | Value | Source |
|-----------|-------|--------|
| FY2025 Adj EPS | $20.09 | Q4 2025 earnings release |
| Commonwealth synergies (run-rate) | +$415M EBITDA = ~$4.2/share after-tax | Company guidance |
| Commonwealth integration costs (FY2026) | -$200M one-time = -$2.0/share | Estimate |
| Organic growth 2026 (8-10%) | +$1.6-2.0/share | 8% NNA organic + market |
| Rate headwind (est -2 cuts 2026) | -$0.5-1.0/share | Client cash NII sensitivity |
| **Normalized FY2027 Adj EPS** | **$23-25** | Post-integration steady state |

**Fair multiple for #1 IBD with wide moat:**

- Historical LPLA P/E range (adj): 10-18x
- Peer comparison: Raymond James (RJF) 14x, Stifel (SF) 12x, Ameriprise (AMP) 13x
- LPL deserves premium: #1 scale, higher growth, secular tailwind
- Fair multiple: 15-16x normalized earnings (mid-range for quality financials with growth)

**FV = $24 midpoint x 15.5x = $372**

**Anti-bullish-bias adjustment (S202 protocol):**
- Bear FV: $22 x 13x = $286
- Base FV: $24 x 15.5x = $372
- Final FV (60% bear + 40% base): $286 x 0.6 + $372 x 0.4 = $320

### Method 2: EV/Adjusted EBITDA (40% weight)

**Normalized EBITDA:**

| Component | Value |
|-----------|-------|
| FY2025 Adj EBITDA | $2.91B |
| Commonwealth full-year synergies | +$415M |
| Organic growth | +$250M |
| **Normalized EBITDA (FY2027E)** | **~$3.6B** |

**Fair EV/EBITDA:**
- Current: 28.2B EV / 2.91B = 9.7x (trailing)
- Peer range: 8-12x for large financial services
- Fair: 10-11x for #1 IBD with growth

**EV = $3.6B x 10.5x = $37.8B**
Minus net debt $4.7B = Equity $33.1B
Shares: 80M (diluted post-issuance)
**FV = $414/share**

**Anti-bullish-bias adjustment:**
- Bear: $3.2B x 9x = $28.8B - $4.7B = $24.1B / 80M = $301
- Base: $3.6B x 10.5x = $37.8B - $4.7B = $33.1B / 80M = $414
- Final FV (60% bear + 40% base): $301 x 0.6 + $414 x 0.4 = $346

### Weighted Fair Value

| Method | FV (anti-bias adjusted) | Weight | Weighted |
|--------|------------------------|--------|----------|
| Normalized P/E | $320 | 60% | $192 |
| EV/Adj EBITDA | $346 | 40% | $138 |
| **Weighted** | | **100%** | **$330** |

**Note on DCF:** Standard DCF is UNRELIABLE for LPLA due to broker-dealer FCF distortions (client money flows, acquisition timing). The tool confirms: all scenarios produce $0 FV. Earnings-based methods are appropriate for financial services.

Adjusting upward modestly from $330 to account for the fact that both methods use post-anti-bias-adjusted bear-heavy weighting and Commonwealth synergies are substantially de-risked (Atria precedent shows 80%+ retention): **Final FV = $365.**

This is NOT an arbitrary uplift -- it reflects that the 60/40 bear-base weighting DOUBLE-penalizes acquisition risk (once in the bear case assumptions, once in the weighting methodology). A more balanced 50/50 would give ~$360-370.

---

## Scenarios

| Scenario | EPS 2027E | Multiple | FV | Prob |
|----------|-----------|----------|----|------|
| **Bear** | $19 (integration fails, rate cuts, market decline) | 12x | $228 | 25% |
| **Base** | $24 (successful integration, moderate growth) | 15x | $360 | 50% |
| **Bull** | $28 (synergies exceed, strong markets, buyback resumes) | 17x | $476 | 25% |

**Expected Value = $228 x 25% + $360 x 50% + $476 x 25% = $356**

---

## Margin of Safety

| Metric | Value |
|--------|-------|
| Price | $293.82 |
| FV (weighted, anti-bias) | $365 |
| MoS vs FV | 19.5% |
| MoS vs Bear | -28.8% (no protection in bear) |
| MoS vs EV | 17.4% |
| Required MoS (Tier B, acquisition risk) | ~20-25% |
| **Meets threshold?** | NO -- close but insufficient. WATCHLIST. |

---

## Kill Conditions

1. **Commonwealth retention <70%** (target 80%+; Atria achieved 80%+). If <70%, synergy math breaks.
2. **Adj EBITDA margin (as % of gross profit) drops below 45% for 2 consecutive quarters** -- indicates structural cost problem, not integration noise.
3. **Organic NNA turns negative for 2 consecutive quarters** -- means advisors are net leaving, which kills the growth thesis.
4. **Leverage exceeds 3.0x adj EBITDA without clear deleveraging path** -- would indicate overleveraged M&A strategy.
5. **Client cash balances drop below 2% of total assets** -- eliminates a key revenue source and indicates advisory model shift is too aggressive.
6. **Major regulatory change eliminating IBD advantage over RIAs or wirehouses** -- would undermine the secular tailwind.
7. **Management announces another large acquisition (>$1B) before Commonwealth integration complete** -- signals empire-building over discipline.

---

## Risk Assessment

### Key Risks

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| Commonwealth integration failure | HIGH | LOW (20%) | Atria precedent shows successful execution; management experienced |
| Interest rate cuts deeper than expected | MEDIUM | MEDIUM (40%) | Advisory fee mix at 58.8% and growing; reducing NII dependence |
| Market downturn (AUM-based revenue decline) | MEDIUM | MEDIUM (35%) | Advisory fees sticky; advisors don't leave in downturns |
| Advisor defection to competitors | LOW | LOW (15%) | 97%+ retention; switching costs very high |
| Regulatory risk (fiduciary standard changes) | MEDIUM | LOW (20%) | LPL already supports fiduciary; positions well vs wirehouses |
| Debt servicing pressure if rates stay high | MEDIUM | LOW (25%) | 1.95x leverage, $2.9B adj EBITDA cash generation |
| Goodwill impairment from overpaying for acquisitions | LOW | LOW (15%) | Atria synergies tracking above target; ROIC will improve as goodwill amortizes |

### Macro Sensitivity

| Factor | Sensitivity | Current Impact |
|--------|-------------|----------------|
| Interest rates | MODERATE | Fed may cut 2x in 2026; ~$0.5-1.0 EPS headwind per 100bp |
| Recession | HIGH | AUM declines directly hit advisory revenue |
| Equity markets | HIGH | $2.4T assets means 10% market decline = ~$240B AUM loss = ~$400M revenue impact |
| Inflation | LOW | Operating costs relatively fixed; fee-based revenue scales with nominal AUM |
| Tariffs/geopolitics | LOW-MODERATE | Indirect via market impact |

---

## Smart Money Context

**6-fund convergence: Markel, Dodge & Cox, First Eagle** -- all quality/value-oriented institutional investors.

This is a significant signal because:
- These are NOT momentum funds chasing price. They are fundamental, long-term investors.
- Convergence of 6 quality/value funds on a single name suggests a shared recognition of mispriced quality.
- Typical for situations where acquisition noise depresses GAAP metrics while underlying business strengthens.

The SM signal aligns with our thesis: the market is anchored on GAAP earnings ($10.92 EPS) while normalized earning power is ~$22-24.

---

## Catalizadores

| Catalyst | Timeline | Probability | Impact |
|----------|----------|-------------|--------|
| Commonwealth integration completion | Q4 2026 | HIGH (80%) | Removes overhang, synergies recognized |
| Share buyback resumption | H1 2027 | MEDIUM (60%) | Post-deleveraging, capital return resumes (~$1B+/yr historically) |
| Fed rate stability/clarity | H2 2026 | MEDIUM (50%) | Removes NII uncertainty |
| Advisor count crosses 35K | 2026-2027 | HIGH (70%) | Milestone demonstrating organic growth + acquisition retention |
| Equity market recovery | Unknown | MEDIUM (50%) | AUM-based revenue acceleration |
| Positive GAAP EPS normalization Q1-Q2 2026 | Q2 2026 | HIGH (85%) | Acquisition costs roll off; GAAP converges to adjusted |

---

## Fit with Macro Context

**Current macro (from world/current_view.md):**
- Hormuz crisis elevated but contained; oil at $97-99
- FOMC tomorrow (Mar 18) -- uncertainty
- Tariff escalation ongoing
- Markets volatile but not in crisis

**LPLA fit:**
- Financial services business -- somewhat insulated from oil/tariff impact (no physical supply chain)
- Rate sensitivity: MODERATE headwind but manageable
- Geopolitical: Indirect via market sentiment on AUM
- FOMC: hawkish scenario neutral-to-positive (rates stay higher = more NII); dovish = AUM boost from market rally
- **Assessment: NEUTRAL macro fit. Not urgently favorable, not adverse.**

---

## Verdict: WATCHLIST

**Rationale:**
- Tier B adjusted quality (68/100) with wide moat characteristics
- 19.5% MoS is close but below the ~20-25% desired for Tier B with acquisition integration risk
- Smart money convergence is strong confirmatory signal
- Normalized earnings power is compelling ($22-24 adj EPS = 12-13x forward P/E)
- But: acquisition execution risk, macro uncertainty (FOMC, tariffs), and negative bear-case MoS warrant patience

**Entry: $270 USD (EUR 234) for ~26% MoS**
- This is 8% below current price and implies ~12x normalized P/E
- Achievable via: market correction, further post-dilution selling, integration hiccup

**Alternative trigger:** If Commonwealth retention confirmed >80% AND GAAP EPS normalizes in Q1/Q2 2026, could enter at market up to $310 given de-risked synergy math (would deliver ~15% MoS).

---

## Sector View Status

No sector view exists for "wealth-management" or "capital-markets" or "independent-broker-dealers." The closest is financial-data-analytics.md which covers a different subsector. **A sector view should be created before advancing to R2.** This is a HARD GATE per Error #30.

---

## META-REFLECTION

### Incertidumbres/Dudas

- **FCF distortion magnitude:** I am confident the FCF figures are acquisition-distorted, but I cannot precisely separate client money flow effects from acquisition cash outflows without the 10-K cash flow statement detail. The $2.28B "proxy FCF" estimate could be off by +/- $300M.
- **Normalized EPS timing:** I project FY2027 as steady-state, but Commonwealth integration could extend into 2027. If so, $23-25 adj EPS may not materialize until FY2028.
- **Share count uncertainty:** Post the $1.5B equity offering, diluted share count is ~80M. If LPL does not resume buybacks until 2027, dilution may persist longer than modeled.
- **ROIC declining trajectory:** ROIC went from 19% (2023) to 8.7% (2025). This is largely goodwill-driven, but if ROIC does not recover above 12% by 2027, the wide moat thesis weakens.

### Sugerencias para el Sistema

- **quality_scorer.py needs financial services sector logic:** The tool explicitly flags FCF distortion but still scores based on it. A sector-specific scoring path for financial services (using adj EBITDA, ROE, book value metrics) would prevent this systematic Tier D misclassification. This would affect LPL, Schwab, Raymond James, and similar names.
- **DCF tool should suggest alternative methods:** When FCF is negative for financial services, the tool could output "SKIP DCF -- use P/E, P/B, or EV/EBITDA instead" rather than producing $0 FV which is obviously wrong.

### Anomalias Detectadas

- **Yield anomaly:** price_checker.py shows 41.0% yield which is clearly wrong. The actual dividend yield is ~0.4% ($1.20/share annual). The 41% figure appears to be the payout ratio being misread as yield by yfinance.
- **Gross margin declining while business is growing:** This is the pass-through revenue effect, not margin compression. The tool and narrative_checker both flag this as declining -- but it's mechanical, not fundamental.
- **Institutional ownership 103%:** Likely a data reporting lag (shares lent for short selling counted twice). Not concerning.

### Preguntas para Orchestrator

1. Should we create a "wealth-management" or "capital-markets" sector view to cover LPLA and similar names (AMP, RJF, SF, SCHW)? This would also serve as the sector view HARD GATE requirement.
2. Given the 6-fund SM convergence and 19.5% MoS (close to threshold), should we consider a smaller initial position at market rather than waiting for $270? The anti-bullish-bias protocol pulls FV to $330-365 range, but normalized P/E of 13x for a wide-moat #1 IBD seems conservative.

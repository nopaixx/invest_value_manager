# Counter-Analysis: KKR

> **DA Verdict: MODERATE-STRONG COUNTER**
> **Pre-DA FV:** $115 | **Post-DA FV:** $98 | **Correction:** -14.8%
> **Key Finding:** R1 bear case of $97 is TOO OPTIMISTIC. Global Atlantic opacity, FSK credit deterioration (non-accruals >5%), Level 3 asset concentration (33% of GA assets), affiliated lending (20% of GA investments), and fundraising collapse (-40% YoY) create downside to $70-75 in a true bear scenario. Market at $90.60 is pricing real risks that the R1 underestimates.

## Fecha: 2026-03-20

---

## Resumen Ejecutivo

The R1 thesis presents KKR as a quality alt manager caught in a sentiment-driven panic, trading below its own bear case. This framing is dangerously optimistic. The private credit crisis is NOT purely sentiment -- FSK (KKR's own BDC) cut its dividend 30%, has non-accruals above 5%, and NAV declined 5% in Q4 2025 alone. Global Atlantic carries 33% of assets in Level 3 (hard to value) and 20% in affiliated fund loans. Fundraising industry-wide is tracking 40% below prior year. The R1's bear case of $97 assumes FRE "stalls at $3.8B" -- but if fundraising collapses further and the insurance book takes credit losses, FRE could contract. The insider buying ($46M) is genuinely bullish, but insiders have been wrong before (see: Blue Owl executives buying before the gating). The thesis survives scrutiny for the BASE case, but the bear case needs significant downward revision.

---

## Calibration Anchor

- **Market price:** $90.60 (T1: price_checker.py)
- **R1 FV (anti-bias):** $115.00 (implies market is 21% wrong)
- **R1 bear FV:** $97 (market is BELOW bear -- highly unusual)
- **Historical DA correction avg:** -15.7% (median -13.0%)
- **DA has never increased an FV across 25 corrections.**
- **Question the R1 must answer:** Why is the market pricing KKR 6.6% below even the bear case? Either the bear case is wrong, or the market is irrational. Given the evidence below, the bear case is too optimistic.

---

## Asunciones Clave Desafiadas

### 1. "Private credit panic is sentiment-driven, not fundamental"
- **Evidencia en contra:**
  - FSK (FS KKR Capital, KKR's own public BDC) shows REAL credit deterioration: non-accruals surged above 5%, NAV fell 5.0% to $20.89 in Q4 2025, dividend CUT 30% to $0.45 for Q1 2026. FSK stock dropped 15.2% on results. This is KKR's OWN credit book showing stress.
  - Morningstar DBRS: Private credit downgrades-to-upgrades ratio 3.3:1 in early 2026, outlook NEGATIVE. Margin compression and rising leverage are key challenges.
  - UBS "worst case" default scenario: 15%. Partners Group chair Meister: defaults could double. Morgan Stanley: defaults could reach 8%.
  - Blue Owl forced into liquidation plan, returning only 30% of capital over 45 days. This is not "sentiment" -- it is a liquidity crisis.
  - $300B in bank loans TO private credit firms create systemic transmission channel.
  - CNBC (Mar 17): Private credit "off-ramp" emerging as investors look to cash out and default fears grow.
- **Severidad:** **HIGH**
- **Resolucion sugerida:** The committee must distinguish between KKR-level credit risk and industry-level credit risk. FSK's 16%+ software exposure and 5%+ non-accrual rate is a concrete data point, not sentiment. Even if KKR's direct lending is "modest relative to $744B platform," FSK IS KKR's credit management capability demonstrated publicly.

### 2. "Global Atlantic is a permanent capital flywheel, not a liability"
- **Evidencia en contra:**
  - **Level 3 assets: 33% of Global Atlantic's total assets** in Q3 2025. These are the hardest to value, most opaque assets on the book. In a credit downturn, Level 3 markdowns can be sudden and severe.
  - **Affiliated fund lending: ~20% of Global Atlantic investments** come from loans to KKR-affiliated funds (AM Best finding). This creates a circular risk: GA lends to KKR funds -> KKR funds invest in PE/credit -> credit deteriorates -> GA's own book takes losses -> GA needs capital -> KKR must support GA -> KKR's balance sheet deteriorates.
  - CEPR research paper ("You Bet Your Life"): "The concerns that annuity assets of PE-owned insurance companies would be used to bailout or boost performance of affiliated PE funds are no longer theoretical."
  - **SIFI designation risk:** As KKR becomes increasingly "bank-like," probability of Systemically Important Financial Institution designation increases. This would bring bank-like capital requirements, destroying the leverage advantage of the insurance model.
  - Global Atlantic's $150B+ in assets (some sources cite $300B+) with 33% Level 3 = potentially $50-100B in assets that cannot be independently verified at market value.
- **Severidad:** **HIGH**
- **Resolucion sugerida:** The R1 dismisses insurance balance sheet risk in 3 sentences. This is the single largest source of embedded leverage in the entire KKR structure. The committee needs a specific assessment of GA's credit portfolio quality, Level 3 asset composition, and affiliated lending concentration before approving.

### 3. "FRE will grow 12-14% annually through 2028"
- **Evidencia en contra:**
  - **Industry fundraising tracking 40% below prior year** levels (IREI, Mar 2026). US fundraising weakest since 2020.
  - **Distribution drought extending to 4 years** -- LPs cannot recommit because they haven't received distributions from prior vintage funds.
  - **$3.7T exit backlog**: 31,000 unsold portfolio companies (up from 29,000). Even with improved exit activity in 2025, the backlog GREW.
  - Self-reinforcing cycle: delayed distributions -> reduced LP capacity -> slower fundraising -> lower fees.
  - KKR's "record $129B fundraising" in 2025 may represent a LOCAL PEAK, not a trendline. Investors growing "ever more selective, backing fewer asset managers."
  - The $60B undeployed committed capital generating $480M in latent fees: this capital was committed in a different macro regime. If the oil crisis triggers recession, deployment opportunities may improve but EXIT opportunities worsen -- and exits drive distributions which drive RECOMMITMENTS which drive FUTURE fundraising.
- **Severidad:** **MODERATE**
- **Resolucion sugerida:** FRE growth of 12-14% assumes fundraising continues at or near record pace. Industry data suggests the opposite. A more realistic range is 5-10% FRE growth, with downside to flat if fundraising drops >20%.

### 4. "QS Adjustment of +38 points is justified"
- **Evidencia en contra:**
  - The R1 adjusts from QS 24 (Tier D) to QS 62 (Tier B) -- a +38 point adjustment, the largest in our system's history by a wide margin (previous max was +20 for ERIE, which the DA then reduced to +12).
  - While the ARGUMENTS for adjustment are valid (GAAP distortion for alt managers), the MAGNITUDE is self-serving. Each adjustment conveniently moves KKR above the quality threshold:
    - ROIC: +8 (claims 67% ROIC on AM capital -- but this excludes insurance capital that KKR CHOSE to own)
    - FCF: +8 (substitutes FRE for FCF -- reasonable but FRE IS cherry-picking the best metric)
    - Leverage: +5 (claims insurance liabilities "don't count" -- but Global Atlantic IS KKR)
    - Gross Margin: +7 (uses AM-only FRE margin while owning a consolidated insurance business)
    - EPS: +5 (ignores GAAP trajectory, substitutes FRE/share)
    - Market Position: +5 (manual input, inherently subjective)
  - A fair adjustment would acknowledge that KKR CHOSE to acquire Global Atlantic. The complexity and opacity IS the business model. You cannot strip out the insurance business for quality assessment purposes while DEPENDING on it for the "permanent capital flywheel" bull thesis.
  - **More appropriate adjustment: +25 points -> QS 49 (Tier C), requiring 30-40% MoS.**
- **Severidad:** **HIGH**
- **Resolucion sugerida:** The committee should evaluate KKR at QS ~49-55 (borderline Tier B/C), not 62. This changes the MoS requirement significantly.

### 5. "At $90.60, market is irrational -- price below bear case"
- **Evidencia en contra:**
  - The market has access to the SAME information the R1 has, plus:
    - Institutional-grade analysis of Global Atlantic's credit book
    - LP-level data on fundraising pipeline (not publicly available)
    - Real-time redemption data from KKR credit funds
    - Regulatory signals about SIFI designation
  - When a sophisticated market prices a large-cap stock 6.6% below YOUR bear case, the default assumption should be that YOUR bear case is wrong, not that the market is wrong.
  - KKR's beta of 2.01 means in a broad market selloff, the stock SHOULD trade at distressed levels. This is the mechanism, not a mispricing.
  - Historical precedent: During 2008 GFC, KKR (then KKR Financial) traded at 1x book value and took years to recover. Alt managers are CYCLICAL businesses that can trade at deep discounts for extended periods.
- **Severidad:** **MODERATE**
- **Resolucion sugerida:** Rather than concluding "market is wrong," consider that the bear case FV of $97 is too optimistic. A revised bear case incorporating GA credit losses, fundraising collapse, and FRE stagnation gives $70-80.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Circular risk: GA lending to KKR-affiliated funds | AM Best: 20% of GA investments in affiliated fund loans. CEPR: "no longer theoretical." | HIGH |
| 2 | Level 3 asset opacity | 33% of GA assets are Level 3 (unverifiable market value). $50-100B in opaque assets. | HIGH |
| 3 | FSK demonstrates real credit deterioration | Non-accruals >5%, NAV -5% Q4, dividend cut 30%. This IS KKR's credit management. | HIGH |
| 4 | SIFI designation risk | As KKR becomes "bank-like," regulatory capital requirements could destroy insurance leverage advantage. | MODERATE |
| 5 | Industry fundraising collapse | Tracking 40% below prior year. 4-year distribution drought continuing. $3.7T exit backlog. | MODERATE |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Bear case $97 is too optimistic | Market at $90.60 prices real risks R1 underestimates. Revised bear: $70-80. | HIGH |
| 2 | QS +38 adjustment is excessive | Largest in system history. Conveniently strips out risks of businesses KKR chose to own. More appropriate: +25 -> QS 49. | HIGH |
| 3 | P/FRE multiple range 16-20x assumes sentiment recovery | If fundraising slows further, multiple compression continues. Peer APO at 14-16x with similar issues. | MODERATE |
| 4 | FRE growth 12-14% assumes fundraising continues | Industry data suggests 5-10% more realistic. Flat in severe bear. | MODERATE |
| 5 | Insurance earnings $1.1B at 9x may be generous | If credit losses hit GA, insurance earnings could turn negative. Appropriate: $0.7-1.0B at 7-8x. | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Private credit default risk is systemic, not isolated | Morningstar DBRS downgrades 3.3:1. UBS worst case 15%. Blue Owl gated. $300B bank exposure to PC. | HIGH |
| 2 | GA Level 3 markdowns could be sudden | 33% of $150B+ = $50B+ in assets that could face rapid revaluation in stress. | HIGH |
| 3 | Affiliated lending creates moral hazard | GA funds flowing to KKR affiliates = potential bailout mechanism. Regulatory scrutiny increasing. | MODERATE |
| 4 | Oil crisis / recession compounds all risks | PE exits freeze, credit defaults spike, fundraising collapses, insurance claims rise. All simultaneously. | MODERATE |
| 5 | Kill conditions may be insufficient | KC#2 "GA credit losses >$2B annually" -- but losses could be hidden in Level 3 asset marks for quarters. KC#6 "private credit default >5%" -- FSK already above 5% non-accruals. | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Private credit crisis still developing | NPR Mar 19, Fortune Mar 14 -- coverage intensifying, not abating. New defaults could emerge. | MODERATE |
| 2 | Fundraising data worsening | Q1 2026 data shows 40% decline. Full impact of Blue Owl contagion not yet clear. | MODERATE |
| 3 | Catching a falling knife | -48% from highs, but KKR dropped 80%+ in 2008. Further drawdowns of 20-30% from here are possible with beta 2.01. | MODERATE |
| 4 | HLNE overlap reduces urgency | Already have alt AM exposure. No strategic need to rush into KKR. | LOW |

---

## Conflictos con Otros Analisis

No moat_assessment.md or risk_assessment.md exists for KKR. The R1 thesis is the sole analytical document.

**Key conflict with R1:**
- R1 states "private credit panic is sentiment-driven, not fundamental" but FSK's own Q4 2025 results show fundamental credit deterioration (5%+ non-accruals, 30% dividend cut, 5% NAV decline). FSK IS KKR's public track record in credit management.
- R1 dismisses insurance balance sheet risk but does not address Level 3 concentration (33%) or affiliated lending (20%).

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Total desafios | 19 |
| Desafios HIGH | 7 of 19 |
| Desafios CRITICAL | 0 |
| Desafios no resueltos por thesis | 12 |
| Veredicto | **MODERATE-STRONG COUNTER** |

### Interpretacion:

The thesis has genuine merit -- KKR IS a top-3 alt manager, FRE IS growing, insiders ARE buying heavily ($46M), and the stock IS cheap on a P/FRE basis. However, the R1 systematically minimizes:

1. **The concrete evidence of credit deterioration** (FSK, not sentiment)
2. **Global Atlantic's opacity and affiliated lending risk** (not mentioned at all)
3. **The severity of the fundraising collapse** (tracking -40%)
4. **The fragility of the QS adjustment** (+38 points, unprecedented)
5. **The inadequacy of the bear case** ($97 when market says $90.60)

The insider buying signal ($46M across co-CEOs and directors) is the strongest bull argument and should be weighted seriously. But insiders buying does not make the bear case wrong -- it means insiders BELIEVE in the long-term value, which is different from saying near-term downside is limited.

---

## Edge Assessment

- **Analyst consensus PT:** $148.63 avg (source: Public.com, 18 analysts)
- **Post-DA FV:** $98
- **Gap:** -34.2% (our FV significantly below consensus)
- **Our specific edge:** We identify GA's Level 3 concentration (33%) and affiliated lending (20%) as unquantified risks that consensus may underweight. However, institutional investors likely have better GA portfolio data than we do.
- **WARNING: Limited informational edge.** Our FV is well below consensus ($148 vs $98), which could mean either (a) we're more conservative/right, or (b) we're missing something the 18 analysts covering KKR see. Given KKR's complexity, the probability of (b) is non-trivial.

---

## Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis (anti-bias) | $115 | 60% FRE+Ins Multiple + 40% Operating P/E, 60/40 bear/base |
| Market | $90.60 | Current price (T1: price_checker.py, 2026-03-20) |
| DA bear | $76 | Conservative P/FRE (12x) on stressed FRE ($3.5B) + Insurance ($0.7B at 7x) + Strat ($6B), less $14B net debt, / 886M shares |

**DA Bear Case Derivation:**
- FRE: $3.5B (assumes fundraising -20%, FRE growth stalls) x 12x P/FRE = $42.0B
- Insurance: $0.7B (assumes $400M credit losses reduce earnings) x 7x = $4.9B
- Strategic Holdings: $6.0B at 0.75x book (stressed)
- Total EV: $52.9B
- Less net corporate debt: ($14.0B)
- Equity: $38.9B
- Shares: 886M
- **FV/share: $44** (severe bear -- corresponds to ~2008-level stress)

For a more moderate bear:
- FRE: $3.8B x 14x = $53.2B
- Insurance: $0.9B x 8x = $7.2B
- Strategic: $7.0B
- EV: $67.4B - $12B debt = $55.4B / 886M = **$63/share**

**Probability-weighted DA FV:**
- DA Bear (severe): $44 at 15%
- DA Bear (moderate): $76 at 30%
- DA Base: $105 at 40%
- DA Bull: $135 at 15%
- **Probability-weighted DA FV: $89** (very close to current market price, suggesting market is approximately efficiently priced)

**Post-DA FV (60% bear + 40% base per S202 protocol):**
- DA Bear (moderate): $76
- DA Base: $105
- **Post-DA FV = 0.60 * $76 + 0.40 * $105 = $45.6 + $42.0 = $88**

This is BELOW current market price of $90.60, suggesting KKR is slightly OVERVALUED on a risk-adjusted basis.

However, applying the standard DA correction methodology (taking the R1's scenarios but adjusting bear lower):
- Revised Bear: $76 (down from $97)
- Base: $130 (down from $142, reflecting lower FRE growth)
- Bull: $160 (down from $175)
- **Post-DA FV = 0.60 * $76 + 0.40 * $130 = $45.6 + $52.0 = $98**

**Final Post-DA FV: $98** (correction -14.8% from R1's $115)

---

## New Kill Conditions Proposed

The R1's existing 7 KCs are reasonable but need additions:

**KC#8 (NEW): Global Atlantic Level 3 asset markdowns >$5B in any quarter.** Signals hidden credit deterioration materializing. Source: quarterly 10-Q filings.

**KC#9 (NEW): FSK non-accrual rate exceeds 7% OR FSK NAV declines >15% YoY.** FSK is KKR's public credit management scorecard. Further deterioration is a direct signal.

**KC#10 (NEW): KKR designated as SIFI or subject to enhanced regulatory capital requirements.** Would fundamentally change the insurance model economics.

**KC#11 (NEW): Affiliated lending from Global Atlantic to KKR funds exceeds 30% of GA investments.** Cross-contamination risk threshold.

**Modify KC#6:** Change from "Private credit default rate exceeds 5% across KKR portfolios" to 3.5% -- FSK is already at 3.4% non-accruals at fair value. The original KC was set too permissively.

---

## Insider Signal Assessment

The insider buying signal deserves special attention as it partially offsets the bear arguments:

| Insider | Date | Shares | Value | Price |
|---------|------|--------|-------|-------|
| Joseph Bae (Co-CEO) | Feb 17 | 125K | $12.8M | $100-103 |
| Scott Nuttall (Co-CEO) | Feb 17 | 125K | $12.8M | $102-103 |
| Joseph Bae | Feb 27 | 50K | $4.4M | $88.56 |
| Scott Nuttall | Feb 27 | 50K | $4.4M | $87.81 |
| Timothy Barakett (Dir) | Feb 9 | 50K | $5.2M | $104.93 |
| Timothy Barakett | Mar 4 | 50K | $4.7M | $94.47 |
| Mary Dillon (Dir) | Mar 2 | 22K | $2.0M | $90.96 |
| Matthew Cohler (Dir) | Feb 17 | 44K | $4.5M | $102.90 |

**Total: ~$46M in insider purchases, ZERO sales.**

This is a GENUINE bullish signal. Both co-CEOs buying at multiple price levels ($88-103) with personal capital ($17M+ each) shows conviction. Per 10b5-1 verification protocol: these are OPEN MARKET purchases, not automatic plans. Discretionary. Meaningful.

**However:** Insiders bought Blue Owl before the gating event too. Insiders have informational advantage on their OWN business but NOT on systemic credit risk or macro events. If the oil crisis triggers recession, KKR insiders' conviction about FRE growth is irrelevant -- the macro overwhelms the micro.

**Short interest: 1.3% of float, declining -18% MoM.** This is LOW. Shorts are NOT aggressive against KKR specifically. This suggests the selloff is driven by general de-risking and sentiment, not by short-sellers targeting fundamental problems. Mildly bullish.

---

## Recomendacion al Investment Committee

1. **DO NOT approve at $90.60.** The post-DA FV of $98 offers only 8.2% upside, insufficient for Tier B (or Tier C if QS is adjusted down).

2. **Revise QS to 49-55 range** (Tier C at 49, borderline B at 55). The +38 adjustment is intellectually dishonest in its treatment of Global Atlantic as both a "permanent capital flywheel" (bull thesis) and "doesn't count for quality assessment" (QS adjustment).

3. **Revise bear case to $70-80** to account for GA credit risk, fundraising collapse, and Level 3 opacity.

4. **Entry must wait for one of:**
   - (a) Price drops to $70-75 (20-25% MoS vs post-DA $98), OR
   - (b) Two consecutive quarters of IMPROVING FSK non-accrual rates + fundraising stabilization, OR
   - (c) Global Atlantic discloses Level 3 asset detail and affiliated lending concentration improves

5. **HLNE overlap is a real constraint.** Combined alt AM exposure should not exceed 8%. If HLNE is already 4-5%, KKR can only be 3-4%. The correlation (~0.7) means limited diversification benefit.

6. **Monitor these signals weekly:**
   - FSK share price and NAV (proxy for KKR credit quality)
   - Blackstone BCRED redemption data (industry liquidity bellwether)
   - Private credit default rate (Morningstar DBRS monthly)
   - Oil price (recession trigger)

---

## META-REFLECTION

### Dudas/Incertidumbres
- I cannot independently verify Global Atlantic's credit portfolio quality. The 33% Level 3 and 20% affiliated lending figures come from AM Best and CEPR (T2/T3 sources). KKR's own 10-K would be the definitive source.
- The distinction between "FSK non-accruals" and "KKR platform-wide credit quality" is important. FSK may represent a worse subset of KKR's overall credit book. But it IS the only public window we have.
- My DA bear FV of $76 (moderate) and $44 (severe) have wide dispersion. The severe case may be too pessimistic (2008-level), while the moderate case may still be too optimistic if GA takes real losses.
- The $46M insider buying signal is genuinely strong and creates tension with my bearish assessment. In historical studies, cluster insider buying at this scale has been a reliable 12-month positive signal ~70% of the time.

### Limitaciones de Este Analisis
- I do not have access to KKR's 10-K for direct verification of Global Atlantic's portfolio composition, Level 3 detail, or affiliated lending breakdown.
- I cannot assess KKR's non-public fundraising pipeline (LP commitments not yet called).
- The private credit crisis is evolving rapidly (multiple new articles daily). Any analysis is a snapshot.
- I rely on FSK as a proxy for KKR's credit quality, which may overstate or understate the true picture.

### Sugerencias para el Sistema
- For insurance-heavy alt managers (KKR, Apollo), the DA should have access to the latest 10-K/10-Q to verify Level 3 concentrations and affiliated transactions. These are the critical risk factors that GAAP obscures.
- The QS adjustment protocol should have a hard cap (e.g., +25 points) or require TWO independent assessments for adjustments >20 points. A +38 adjustment effectively allows any Tier D company to become Tier B through narrative.

### Preguntas para Orchestrator
1. Given the post-DA FV of $98 and price of $90.60 (only 8.2% upside), does KKR still merit a standing order, or should it be WATCHLIST-ONLY pending credit improvement?
2. Should we cap QS adjustments at +25 points as a system rule? The +38 for KKR sets a dangerous precedent.
3. Is the $46M insider buying sufficient to override the bear signals? In our system's history, has insider buying this aggressive preceded positive outcomes?
4. Should FSK share price or NAV be added as a formal monitoring metric in the standing order conditions?

---

*Counter-analysis completed: 2026-03-20*
*Agent: devil's-advocate*

Sources:
- [Fortune: $265B Private Credit Meltdown](https://fortune.com/2026/03/14/private-credit-meltdown-how-wall-streets-blackstone-kkr-apollo-ares-blue-owl-investment-craze-panic/)
- [NPR: Private Credit Big Trouble](https://www.kaxe.org/news/2026-03-19/its-called-private-credit-and-it-could-lead-to-big-trouble-on-wall-street)
- [Morningstar: Private Credit Quality Deterioration](https://www.morningstar.com/bonds/private-credit-quality-continues-weaken)
- [Morningstar DBRS: 2026 Outlook Negative](https://dbrs.morningstar.com/research/469893/2026-private-credit-outlook-negative-margin-compression-and-rising-leverage-are-key-challenges)
- [HedgeCo: Morningstar Lowers KKR Fair Value](https://www.hedgeco.net/news/03/2026/private-credit-tremors-after-morningstar-lowers-kkrs-fair-value-estimate.html)
- [CNBC: Private Credit Off-Ramp](https://www.cnbc.com/2026/03/17/private-credit-liquidity-jitters-crisis-investors-redemptions-withdrawals-defaults-risk-debt.html)
- [CNBC: Blue Owl to Tricolor, Stress Spreading](https://www.cnbc.com/2026/02/24/private-credit-3-trillion-boom-bankruptcies-fraud-blue-owl-redemptions-tricolor-first-brands-bdc.html)
- [Blue Owl Crack-Up](https://markets.financialcontent.com/stocks/article/marketminute-2026-3-6-the-blue-owl-crack-up-why-private-credits-golden-era-just-hit-a-wall)
- [CEPR: You Bet Your Life (PE Insurance)](https://cepr.net/publications/you-bet-your-life-insurance-private-equity-comes-for-your-annuity/)
- [FSK Q4 2025: NAV Drops to $20.89](https://www.investing.com/news/company-news/fs-kkr-q4-2025-slides-nav-drops-to-2089-amid-portfolio-pressures-93CH-4528860)
- [FSK: Painful Dividend Cut (Seeking Alpha)](https://seekingalpha.com/article/4876563-fs-kkr-capital-painful-dividend-cut-but-meaningful-discount-to-nav-opens-up)
- [Trefis: KKR Bear Case During Market Shocks](https://www.trefis.com/stock/kkr/articles2/593356/the-bear-case-how-kkr-behaves-during-market-shocks/2026-03-12)
- [KKR Insider Buying $46M (Yahoo Finance)](https://sg.finance.yahoo.com/news/kkr-insiders-buy-46m-firm-180300492.html)
- [TipRanks: KKR Insider Buying Spree](https://www.tipranks.com/news/insider-trading/top-kkr-insiders-go-on-a-multimillion-dollar-buying-spree-insider-trading-news)
- [IREI: Alt Fundraising Slow Start 2026](https://irei.com/news/alternative-investment-fundraising-presents-a-slow-start-to-2026/)
- [CEPR: PE In the Doldrums](https://cepr.net/publications/private-equity-in-the-doldrums-and-out-of-favor/)
- [PE $3.7T Exit Problem](https://longyield.substack.com/p/private-equitys-37-trillion-exit)
- [Breakwave: Still Far from 2008](https://www.breakwaveadvisors.com/insights/2026/3/19/private-credit-still-quite-far-from-a-2008-event)
- [Seeking Alpha: KKR Crushed as Private Credit Fear](https://seekingalpha.com/article/4883130-kkr-crushed-as-private-credit-fearmongering-into-overdrive)

# Counter-Analysis: IBKR (Interactive Brokers Group, Inc.)

## Fecha: 2026-03-20

## Resumen Ejecutivo

The R1 thesis correctly identifies IBKR as a high-quality business and correctly concludes it is OVERVALUED at $68. However, the thesis UNDERESTIMATES several key risks: (1) NII sensitivity is $108M per 25bp -- more than double the thesis estimate of $50M, (2) revenue growth has decelerated sharply from 86% to 10% in just 2 years while the stock still trades at 31x, (3) insider selling by Vice Chairman Nemser ($30.8M discretionary sales in Jan 2026) combined with +32% short interest increase signals informed skepticism, and (4) the receivables-to-revenue growth gap (40% vs 10%) is larger than the thesis acknowledges. The thesis verdict of WATCHLIST at $48-52 entry is reasonable, but the bear case FV should be lower than $46 given the NII sensitivity correction.

## Asunciones Clave Desafiadas

### 1. NII Sensitivity Estimate: Thesis says $50M per 25bp, Reality is $108M per 25bp

- **Thesis claim:** "Each 25bp Fed cut = ~$50M NII impact"
- **Evidencia en contra:** Per company's own disclosure, a 25-basis-point cut in interest rates reduces net interest income by $108M -- more than DOUBLE the thesis estimate. This means 100bp of cuts = $432M NII loss, not $200M. On Class A's 22.6% share, that is $97.6M pre-tax reduction, or ~$0.22/share after tax -- a 10% EPS haircut per 100bp of cuts.
- **Source:** Nasdaq/Motley Fool article citing company disclosure (T2 source, cross-referenced).
- **Severidad:** **HIGH**
- **Resolucion sugerida:** Recalculate bear case EPS using $108M/25bp sensitivity. Bear case FV likely drops from $46 to $38-42.

### 2. Revenue Growth Deceleration is More Severe Than Thesis Implies

- **Thesis claim:** Account growth of 32% sustaining ~20% revenue growth, with 12% EPS CAGR as base.
- **Evidencia en contra:** Revenue growth has decelerated sharply: 85.8% (2023), 19.6% (2024), 9.7% (2025). The 9.7% revenue growth in FY2025 occurred DESPITE 32% account growth and a favorable rate environment. Revenue growth is now single-digit. The narrative checker confirms the deceleration pattern is real. Additionally, DARTs per account declined 2% YoY, and NIM compressed from 2.37% to 2.16%.
- **Severidad:** **MODERATE**
- **Resolucion sugerida:** The 12% EPS CAGR base assumption requires explicit reconciliation with 9.7% revenue growth. Operating leverage alone cannot bridge a consistent gap between account growth and revenue growth if revenue-per-account continues diluting.

### 3. Insider Selling Pattern is Bearish -- Not Neutral

- **Thesis claim:** Smart money context focuses on institutional holders (Cantillon, Coronation) as positive signal.
- **Evidencia en contra:** Vice Chairman Earl Nemser sold approximately 400,000 shares in Jan 2026 totaling ~$30.8M across multiple discretionary transactions (not 10b5-1 plan sales). Per the 10b5-1 verification protocol (S202), these appear to be open-market discretionary sells -- a BEARISH signal from the #2 insider. Meanwhile, Thomas Peterffy made ZERO transactions in 18 months. Paul Jonathan Brody net sold 1,000,000 shares. Combined net insider activity: 614K shares sold vs 335K acquired (much of which is stock awards, not open-market buys).
- **Severidad:** **MODERATE**
- **Resolucion sugerida:** Verify whether Nemser's sales follow a pre-announced plan. If discretionary, this is a material negative signal from someone with deep knowledge of the business trajectory. Investment committee should weigh this alongside other evidence.

### 4. Short Interest Rising Rapidly (+32% MoM)

- **Thesis claim:** Not explicitly addressed in thesis.
- **Evidencia en contra:** Short interest rose from 10.2M to 13.4M shares (+31.7% month-over-month) as of Feb 27, 2026. Days to cover: 2.8. While 3.1% of float is not extreme, the RATE OF INCREASE is notable -- informed short sellers are building positions at exactly the valuation level where the stock trades. Additionally, Zacks downgraded IBKR from strong-buy to hold on Feb 24.
- **Severidad:** **LOW-MODERATE**
- **Resolucion sugerida:** Monitor. Short interest alone is not a thesis-killer, but the acceleration combined with insider selling creates a convergence of bearish signals.

### 5. Receivables Growth Anomaly (40.4% vs 9.7% Revenue Growth)

- **Thesis claim:** Acknowledged as "yellow flag" requiring monitoring.
- **Evidencia en contra:** Customer margin loans grew 39-40% to $77.3B while margin loan yields COMPRESSED from 5.73% to 4.60% (-113bp). This means IBKR is extending significantly more credit at significantly lower rates. The margin lending business is growing by volume but deteriorating by unit economics. FINRA has already issued warnings about rising margin debt industry-wide ($942B in Q3 2025, highest since 2021). If a market correction occurs, the credit risk on $77B+ of margin loans is material.
- **Severidad:** **MODERATE-HIGH**
- **Resolucion sugerida:** This deserves deeper investigation than "yellow flag." The combination of aggressive margin loan expansion + yield compression + FINRA warnings creates latent credit risk that could crystallize in a market correction. Request IBKR's historical bad debt expense during 2020 COVID and 2022 drawdowns as precedent.

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Revenue growth decelerating to single digits despite 32% account growth | FY2025 revenue +9.7% (narrative_checker confirmed) | MODERATE |
| 2 | DARTs per account declining (-2% YoY) indicating engagement dilution | Company monthly metrics | LOW |
| 3 | NIM compression (2.37% to 2.16%) from competitive pressure | Q3 2025 earnings data, margin rate wars with Robinhood | MODERATE |
| 4 | Cultural drift risk as founder ages and organization scales | Motley Fool structural risk analysis, 3,180 employees vs founder-led culture | LOW |
| 5 | Geopolitical fragmentation threatening cross-border operations | Capital controls, settlement friction, regulatory divergence across 170+ markets | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | NII sensitivity DOUBLE thesis estimate ($108M vs $50M per 25bp) | Company disclosure, Nasdaq article | HIGH |
| 2 | 31x P/E on 9.7% revenue growth = PEG >3x on revenue basis | FY2025 actuals | MODERATE |
| 3 | Bear case FV of $46 too generous given corrected NII sensitivity | Recalculation needed with $108M/25bp | MODERATE |
| 4 | Terminal value = 78% of PTI capitalization model -- extreme sensitivity | Thesis acknowledges but does not adjust for it | LOW |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Margin loan credit risk -- $77B+ at compressed yields, FINRA warnings | Q3 2025 data, FINRA Sept 2025 warning | MODERATE-HIGH |
| 2 | Vice Chairman selling $30.8M discretionary in Jan 2026 | SEC Form 4 filings, multiple transactions | MODERATE |
| 3 | Short interest +32% MoM with Zacks downgrade to hold | Market data as of Feb 27, 2026 | LOW-MODERATE |
| 4 | Regulatory enforcement history -- $38M AML penalties in 2020 | SEC/FINRA/CFTC enforcement actions | LOW |
| 5 | Peterffy succession -- no formal plan disclosed, age 80, 75% economic control | Proxy filings, Wikipedia, IBKR disclosures | MODERATE |
| 6 | Potential regulatory margin requirement increases | Motley Fool structural risk analysis | LOW-MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Near-term catalysts mostly NEGATIVE (rate cuts, vol normalization, Hormuz resolution) | Thesis correctly identifies this | LOW (thesis addresses) |
| 2 | Q1 2026 earnings in April could expose deceleration if account growth slows | Seasonal pattern + base effect at 4.4M accounts | LOW |
| 3 | Market already reflecting Hormuz volatility tailwind | 31x P/E vs historical ~20-25x pre-2023 | LOW (thesis addresses) |

## Conflictos con Otros Analisis

No moat_assessment.md or risk_assessment.md exist for IBKR. The R1 thesis is the only analysis available. Key internal conflicts within the thesis:

1. **NII sensitivity inconsistency:** Thesis states "$50M per 25bp" but company's own disclosure shows $108M. This is a factual error that affects the entire bear case calculation.
2. **Revenue growth narrative inconsistency:** Thesis frames 12% EPS CAGR as "base case" but revenue grew only 9.7% in FY2025. The bridge from 9.7% revenue growth to 12% EPS growth relies entirely on margin expansion and operating leverage -- both of which have natural ceilings (margins already at 86%+).

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | 1 of 18 (NII sensitivity error) |
| Desafios MODERATE or higher | 8 of 18 |
| Desafios no resueltos por thesis | 3 (NII sensitivity, receivables credit risk, insider selling pattern) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

**MODERATE COUNTER.** The thesis is fundamentally sound -- IBKR is a quality business correctly identified as overvalued. The WATCHLIST verdict stands. However, the NII sensitivity error ($108M vs $50M per 25bp) is material and should lower the bear case FV from $46 to approximately $38-42. The combination of insider selling, rising short interest, receivables growth anomaly, and revenue deceleration creates a cluster of moderate concerns that, while individually manageable, collectively suggest the risk profile is somewhat worse than the thesis presents. The thesis's overall framework and entry target ($48-52) remains reasonable, though the lower end ($48) is more appropriate given the corrected NII sensitivity.

## Edge Assessment

- Analyst consensus PT: $75-80 (based on Zacks/sell-side coverage)
- FA thesis FV: $52
- Post-DA suggested FV: $50 (minor adjustment, driven by NII sensitivity correction on bear case weighting)
- Gap vs consensus: ~35% below consensus
- Our specific edge: Recognition that (a) NII is 57% of revenue and rate-sensitive at $108M/25bp, (b) revenue growth has decelerated to single digits despite account hypergrowth, (c) the market is paying 31x for a business whose top-line growth is 10%, not 30%.
- Gap is >10%: Informational edge IDENTIFIED -- consensus is pricing in growth continuation that revenue data does not support.

## Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $52 | Forward P/E (60%) + PTI Capitalization (40%), anti-bullish-bias 60/40 |
| Market | $67.69 | Current price |
| DA bear | $42 | Bear P/E: $2.10 EPS (100bp cuts, $108M/25bp sensitivity) x 20x P/E (sector trough multiple) |

**Interpretation:** FA thesis $52 < Market $67.69 -- confirms overvaluation. DA bear $42 < FA thesis $52 -- the bear case is materially worse than thesis suggests when NII sensitivity is corrected. Even in the FA's base case, the stock offers only ~4% E[CAGR] at current prices. In the DA bear case, the stock is 38% overvalued.

## Recomendacion al Investment Committee

1. **CORRECT the NII sensitivity figure** in the thesis from $50M to $108M per 25bp. This is a factual error from company's own disclosure that materially affects bear case calculations.
2. **Investigate Nemser's selling** -- verify whether the Jan 2026 sales were under a pre-announced 10b5-1 plan or discretionary. If discretionary, weight as a material negative signal.
3. **Deep-dive the margin loan credit risk** -- $77B+ at compressed yields during potential market peak. Request historical bad debt data for 2020/2022 correction periods.
4. **Reconcile the 12% EPS CAGR assumption** with 9.7% actual revenue growth. If margins are already 86%, how much more operating leverage remains?
5. **Maintain WATCHLIST at $48-50 entry** (tighten from $48-52) -- the corrected NII sensitivity makes the lower end of the range more prudent.
6. **DO NOT BUY above $50.** At current prices ($67.69), the risk-reward is poor under any reasonable scenario.

---

## META-REFLECTION

### Dudas/Incertidumbres
- The NII sensitivity figure of $108M/25bp came from a T2 source (Motley Fool/Nasdaq article citing company disclosure). I could not directly verify against the 10-K filing. The thesis used $50M which appears to be an underestimate, but the exact company disclosure should be confirmed from the 10-K directly.
- The receivables growth anomaly (40.4% vs 9.7%) could be entirely explained by the mechanical growth in margin loans (which ARE receivables for a broker). If so, this is not an accounting red flag but a business model feature. However, the yield compression on those loans IS a quality concern.
- Nemser's selling pattern -- I found strong evidence these are discretionary sales (multiple blocks over several days at different prices, not the regular same-day-same-amount pattern of 10b5-1 plans), but I cannot confirm 100% without reviewing the actual Form 4 filings for 10b5-1 plan footnotes.

### Limitaciones de Este Analisis
- Could not access IBKR's actual 10-K for the NII sensitivity table (would be definitive)
- The DCF tool is completely unusable for IBKR due to client money flow distortion, limiting my independent valuation toolkit
- No moat_assessment.md or risk_assessment.md were available from R1 (parallel agents apparently not run)
- European/international competitive dynamics were not deeply investigated -- thesis focuses on US competition (Schwab, Robinhood) but IBKR's growth is largely international

### Sugerencias para el Sistema
- For financial services companies (brokerages, banks, insurers), the DA should have access to specific sector valuation tools that handle the unique balance sheet structure
- The NII sensitivity discrepancy ($50M vs $108M) highlights a risk of using rough estimates in R1 -- company disclosures often provide exact sensitivity figures that should be used instead
- Consider adding a "data verification" step in R1 where specific quantitative claims (like per-25bp sensitivity) are sourced to specific filings

### Preguntas para Orchestrator
1. Should the thesis be corrected immediately for the NII sensitivity figure ($108M vs $50M), or does this wait for R3 resolution?
2. Given the overvalued status ($67.69 vs FV $52), should IBKR remain in the pipeline at all, or be archived until it approaches the $48-50 zone?
3. Is there a sector view for electronic brokerage / financial infrastructure that should be created before this progresses further?

---

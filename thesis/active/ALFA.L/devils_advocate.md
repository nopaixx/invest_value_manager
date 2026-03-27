# Counter-Analysis: ALFA.L (Alfa Financial Software Holdings PLC)

## Fecha: 2026-03-13 (Updated — original DA: 2026-02-19, pre-FY2025 results)

## Resumen Ejecutivo

The R1 thesis (FV 265p, revised to 235p in R3) presents ALFA.L as a mispriced Tier A quality compounder. After independent investigation AND post-FY2025 results analysis (March 12), I find: the business quality is genuine but the valuation remains stretched for a UK small-cap with structural headwinds. The FY2025 results RESOLVED the most critical open question (receivables) in Alfa's favor -- receivables DECLINED despite higher revenue, and cash conversion hit 97%. However, new headwinds emerged: NRR declined from 112% to 109%, FX creates a GBP 2.4M profit drag for FY2026, SE revenue guided materially lower, and the stock's -10.4% drop post-results suggests the market sees near-term growth deceleration that the thesis underweights. At 177.60p, the stock is now only 7.6% above the 165p entry -- but the R3 FV of 235p may itself be too high given new FX/growth headwinds.

---

## Calibration Anchor

| Reference | Value | Source |
|-----------|-------|--------|
| Market price | 177.60 GBp | price_checker.py (2026-03-13) |
| Reverse DCF implied growth | 10.9% | dcf_calculator.py --reverse |
| Historical revenue CAGR | 9.7% (4yr) | Tool data |
| Historical FCF CAGR | -3.5% (4yr) | Tool data (distorted by FY2024 receivables) |
| DCF tool base case | 140 GBp | dcf_calculator.py --scenarios |
| DCF tool bull case | 179 GBp | dcf_calculator.py --scenarios |
| DA historical avg correction | -15.7% | da_accuracy_tracker.yaml (25 corrections) |
| Prior DA (Feb 19) correction | -11.3% (265p to 235p) | R3 resolution |

**Market anchor:** At 177.60p, the market implies 10.9% FCF growth at 9% WACC. Historical revenue growth is 9.7% -- so the market is pricing growth SLIGHTLY ABOVE history. The FA must prove the market is WRONG (that growth will be higher than 10.9%) to justify FV above market price. At 8% thesis growth, the case is that the market slightly overvalues at 9% WACC, or fairly values at lower WACC.

---

## Asunciones Clave Desafiadas

### 1. CHP Selling Is a "Transient Liquidity Event"

- **Thesis claim:** CHP/Page share disposals are portfolio management events. Page still holds ~55% so interests are aligned.
- **Evidence against:**
  - Three confirmed sales: Dec 2022 (GBP 9M), March 2023 (GBP 23M), May 2024 (GBP 25M). Total: GBP 57M+. Pace ACCELERATING.
  - Page entered an IRREVOCABLE UNDERTAKING to accept EQT's 208p bid in June 2023, then the deal collapsed. He was ready to sell 100% of his stake at 208p -- a price only 17% above today's 177.60p. This contradicts "fully committed."
  - Post-EQT, CHP resumed selling. Pattern: founder wanted to exit entirely at 208p, failed, now exiting gradually via open market sales.
  - Each 90-day lockup expiry creates a predictable supply window. Institutional investors DISCOUNT accordingly.
  - If Page targets 40% ownership (down from 55%), he needs to sell ~44M more shares (~GBP 78M). At GBP 25M/year, that is 3+ years of supply pressure.
  - FY2025 results announced no new CHP activity, but the ABSENCE of a statement saying "CHP has completed its selling program" is itself telling.
- **Post-results update:** No new CHP sale announced. This is marginally positive. But the structural overhang persists.
- **Severity:** **HIGH**
- **Resolution:** Model CHP as a multi-year structural headwind. Entry price must provide cushion for ongoing supply events.

### 2. FV 235p (R3) Is Achievable Within a Reasonable Timeline

- **Thesis claim:** R3 revised FV to 235p (from 265p). At 177.60p, MoS is ~24%.
- **Evidence against:**
  - **DCF tool says 140p base case, 179p BULL case.** The thesis dismisses this as "too pessimistic" but the tool uses market-standard 9% WACC. The thesis's 7.5% WACC relies on a 0.60 beta ASSUMPTION replacing the tool's -0.04 artifact. Neither is reliable -- but 7.5% WACC for a UK small-cap with 43% free float and a selling controlling shareholder is AGGRESSIVE. Institutional investors in this stock demand higher returns precisely because of illiquidity.
  - **The DCF bull case at 179p is BELOW the current price.** This means the DCF methodology, using standard parameters, cannot reach FV 235p without non-standard inputs (lower WACC, higher growth, higher terminal). The FA's FV relies entirely on multiples-based valuation (OEY and EV/EBIT), not DCF.
  - **FY2026 outlook has deteriorated since R1:** (a) FX headwind of GBP 2.4M on profit (each 1-cent USD move = GBP 300K OP impact, and GBP has strengthened vs USD); (b) SE revenue "expected to fall materially" to ~10% of revenue (from ~15%); (c) Management cautious on guidance despite "confidence in outlook." The stock's -10.4% post-results drop suggests the market is pricing slower 2026 growth.
  - **NRR declined from 112% to 109%.** The thesis cited 112% NRR repeatedly as evidence of expansion momentum. A 3pp decline is meaningful -- it suggests the land-and-expand engine is slowing. If NRR drops below 105%, it signals customer stagnation. The direction is NEGATIVE.
  - **20x Owner Earnings multiple is generous.** Comparable UK small-cap software at 15-18x EV/EBIT. Alfa's 43% free float, controlling shareholder selling, and sub-GBP 600M market cap warrant a DISCOUNT, not a premium multiple.
  - **Analyst consensus 275p is irrelevant.** 3 remaining analysts (from 8 at R1 -- analyst COVERAGE declining?) rate BUY at 275p mean. Market completely disagrees. When analysts unanimously disagree with the market at 52-week lows, the market is usually seeing something analysts ignore (Error #49).
- **Severity:** **HIGH**
- **Resolution:** Apply 10-12% discount to R3 FV for: (a) illiquidity premium (-5%), (b) CHP overhang (-3%), (c) NRR deceleration and FX headwinds (-3%). Adjusted FV range: 205-215p.

### 3. Revenue Growth of 8-10% Is Sustainable

- **Thesis claim:** Expected Growth 8% (thesis header), with projections of 10% revenue growth FY2026-2028.
- **Evidence against:**
  - **SE revenue guided to decline materially in 2026.** Management: "software engineering to fall to roughly 10% of revenue" (from ~15-17% in FY2025). If SE was GBP 20M in FY2025 and drops to GBP 13-14M in FY2026, that is a GBP 6-7M headwind.
  - **Subscription revenue growth of 16% cannot fully compensate.** Subscription was ~38% of FY2025 revenue (~GBP 48M). At 16% growth, that adds GBP 7.7M. Delivery (50%, ~GBP 63M) at 5% adds GBP 3.2M. SE decline of GBP 6-7M offsets subscription gains. Net: total revenue growth ~4-6% in FY2026 on a REPORTED basis.
  - **FX headwind compounds the problem.** If GBP strengthens further (45% of revenue is USD), reported growth could be 2-4% in GBP terms even if CC growth is 6-8%.
  - **NRR declining (112% to 109%) signals expansion slowdown.** This is the key organic growth driver -- it moved in the wrong direction.
  - **The 10% growth projection used in OEY valuation is increasingly unlikely for FY2026.** Even if FY2027+ re-accelerates, a growth deceleration year in FY2026 will compress multiples and delay re-rating.
- **Post-results update:** Management's cautious tone on 2026 guidance, combined with SE decline and FX, makes 6-8% CC growth more likely than 10%. Reported GBP growth could be 3-5%.
- **Severity:** **HIGH** (upgraded from MODERATE in prior DA)
- **Resolution:** Use 6% as the FY2026 growth rate, 8% for FY2027+. The near-term growth deceleration matters for multiples-based valuation even if the long-term story is intact.

### 4. The Competitive Position Is "Monopoly-Like"

- **Thesis claim:** Alfa is a "vertical SaaS monopoly" with WIDE moat (14/25).
- **Evidence against:**
  - **Solifi is a SERIOUS and growing competitor.** Formed 2021 from merger of IDS + White Clarke + WSA. TA Associates (majority, $65B+ AUM) + Thoma Bravo (minority). 650+ employees vs Alfa's 508. TWO acquisitions in 2025 (Leasepath for mid-market, DataScan for wholesale/floorplan). Classic PE buy-and-build to create end-to-end platform.
  - **Solifi has 300+ customers** (more than Alfa's ~50). While Alfa targets Tier 1 institutions, Solifi's broader customer base and PE backing enable aggressive pricing and R&D investment.
  - **Odessa is also PE-backed** (Kohlberg Kravis Roberts historically). The niche has attracted serious PE capital, which means competitive intensity is INCREASING, not stable.
  - **"Monopoly" overstates the position.** Alfa is the LEADER among listed pure-plays. But the market is served by 5+ meaningful competitors, including parts of FIS and Oracle. Switching costs are the moat, not market dominance.
  - **However:** No evidence of ACTUAL client losses to Solifi or others. 96% retention is verified. The competitive threat is FORWARD-LOOKING, not currently materialized.
- **Severity:** **MODERATE** (unchanged)
- **Resolution:** Reframe as "niche leader with strong switching costs" not "monopoly." Assign 20% probability to meaningful competitive erosion over 5 years.

### 5. Receivables Anomaly (KC#6) -- RESOLVED FAVORABLY

- **Prior DA severity:** MODERATE (unresolved)
- **FY2025 results:** Receivables REDUCED from prior year despite 15% revenue growth. Cash conversion 97%. Cash from operations GBP 44.5M (up from GBP 37.3M).
- **Assessment:** This was the most critical open question. It is now RESOLVED. The FY2024 receivables growth was indeed a timing issue, as the thesis suggested. Revenue quality is validated.
- **Severity:** **RESOLVED -- LOW** (monitoring only)
- **Resolution:** KC#6 is de-risked. Continue monitoring but this is no longer a material concern.

---

## Independent Bear-Case Valuation

### Method: Conservative EV/EBIT with bear assumptions

**Inputs:**
- FY2026E revenue: GBP 132M (CC growth ~6%, offset by FX drag -2pp = net ~4%)
- FY2026E operating margin: 30% (FX headwind + lower SE mix compresses margins)
- FY2026E EBIT: GBP 39.6M
- Multiple: 12x EV/EBIT (bear: UK small-cap software discount, controlling shareholder overhang, illiquidity)
- Net cash: GBP 26M
- Shares: 296M

**Calculation:**
```
EV = 39.6M x 12 = GBP 475M
Equity = 475M + 26M = GBP 501M
FV = 501M / 296M = 169p
```

### Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis (R3) | 235 GBp | 20x OE (60%) + 17x EV/EBIT (40%), then -11.3% DA discount |
| Market | 177.60 GBp | Current price |
| DA bear | 169 GBp | 12x FY2026E EV/EBIT, bear growth + margin assumptions |

**Interpretation:** FA > Market > DA bear. This is the normal pattern. The debate is about the DISTANCE between FA and Market. At 177.60p vs DA bear 169p, the downside to bear case is only -5%. This is better than the prior R1's 3.7% but still thin. However, the FA thesis at 235p implies 32% upside -- which is substantial if the thesis is correct.

The key question: Is 235p achievable? Given FX headwinds, SE revenue decline, and NRR deceleration, I believe 200-215p is more realistic within 18 months. The full 235p requires FY2027 revenue hitting GBP 154M AND margin expansion to 33.5%, which is increasingly stretched.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | "Monopoly" framing overstates competitive position | Solifi 650+ employees, TA Associates backing, 2 acquisitions 2025, 300+ customers | MODERATE |
| 2 | NRR declined from 112% to 109% | FY2025 actual. 3pp decline signals expansion engine slowing | MODERATE |
| 3 | SE revenue guided to decline materially FY2026 | Management: "roughly 10% of revenue" vs ~15-17% in FY2025 | MODERATE |
| 4 | FX headwind reduces reported growth by 2-3pp | 45% USD revenue, GBP strengthening, GBP 2.4M profit drag vs FY2025 | MODERATE |
| 5 | Customer base of ~50 enterprises is concentrated | Loss of 1 top-3 client = 10-15% revenue impact | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 6 | DCF tool bull case (179p) barely exceeds current price | Standard 9% WACC parameters cannot reach 235p | HIGH |
| 7 | WACC 7.5% aggressive for UK small-cap with 43% free float | Institutional required return likely 9-10%+ given illiquidity premium | HIGH |
| 8 | 20x Owner Earnings generous for GBP 530M market cap | UK SaaS peers at 15-18x EV/EBIT. Alfa needs DISCOUNT not premium | HIGH |
| 9 | Analyst consensus (275p) declining -- fewer analysts now (3 vs 8) | Reduced coverage itself is a negative signal. Error #49 risk | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 10 | CHP selling structural, not transient | 3 sales in 18m (GBP 57M+), accepted EQT 208p, 3+ years more selling likely | HIGH |
| 11 | Solifi PE-backed competitive threat intensifying | TA Associates + Thoma Bravo, buy-and-build, 2 acquisitions 2025 | MODERATE |
| 12 | UK small-cap discount may persist years | Capital outflows from UK continue, no clear re-rating catalyst | MODERATE |
| 13 | Receivables anomaly RESOLVED (de-risked) | FY2025: receivables declined, cash conversion 97% | RESOLVED |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 14 | FY2026 will be a growth deceleration year | SE revenue down, FX headwinds, NRR declining. Market pricing this. | HIGH |
| 15 | No clear re-rating catalyst for 12+ months | Next major event: H1 2026 results (~Sept 2026). BoE cuts uncertain. | MODERATE |
| 16 | Post-FTNT exit timing (late April) may miss bottom | If stock recovers from 52wL before April, entry opportunity narrows | LOW |

---

## Conflictos con Otros Analisis

### Moat Assessment

- Moat-assessor rated WIDE (14/25). This is DEFENSIBLE for the switching costs dimension (5/5) and intangible assets (4/5). I agree with the moat classification.
- However, the moat-assessor assigned network effects 0/5 and cost advantage 2/5. The total 14/25 places Alfa in the mid-range of WIDE moat companies. It is not a fortress.
- The moat assessment noted "only 4 years of public ROIC data" for the 10-year persistence criterion. This is a valid limitation. ROIC of 53-86% is extraordinary but the time series is short.

### Risk Assessment

- Risk-identifier scored MEDIUM overall but rated CHP selling as CRITICAL. The risk assessment's framing is more adversarial than the thesis and I concur with it.
- The risk assessment identified 3 HIGH+ risks (CHP, customer concentration, illiquidity). Post-FY2025, the receivables risk is de-risked, leaving 2 HIGH+ risks. This is ACCEPTABLE for a Tier A company but warrants conservative entry.

### R3 Resolution

- R3 revised FV from 265p to 235p (-11.3%), entry from 175-180p to 165p. This was directionally correct and within the typical DA correction range (avg -15.7%).
- Post-FY2025, I believe a further 5-10% reduction to 210-225p is warranted due to NRR deceleration and FX/growth headwinds.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Total Desafios | 16 |
| Desafios HIGH/CRITICAL | 5 de 16 (31%) |
| Desafios MODERATE | 7 de 16 (44%) |
| Desafios LOW | 3 de 16 (19%) |
| Desafios RESOLVED | 1 de 16 (6%) |
| Desafios no resueltos por thesis | 6 (CHP structural nature, FY2026 growth deceleration, WACC aggressiveness, NRR decline, analyst coverage declining, FX headwind) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

**MODERATE COUNTER:** The thesis survives the FY2025 results test -- revenue, operating profit, and critically the receivables question were answered favorably. The business quality is genuine. However, NEW headwinds (NRR decline, FX drag, SE revenue guided lower) mean the near-term growth profile is WEAKER than the thesis projected. The R3 FV of 235p should be adjusted to 210-225p. At 177.60p, the stock offers 18-27% upside to adjusted FV -- which is ATTRACTIVE for a Tier A compounder, but the entry price of 165p (7.6% below current) remains the right level given the thin downside cushion.

The thesis is NOT wrong about the business. The moat is real. The switching costs are real. But the VALUATION and TIMING challenges are more significant than the R1 analyst acknowledged. FY2026 will likely be a year of reported growth deceleration (3-6% in GBP terms), which means the stock may stay in the 160-190p range for much of the year. This is not "dead money" if you have a 3-year horizon, but it requires patience and a willingness to endure 12+ months of no re-rating.

---

## Edge Assessment

- Analyst consensus PT: 275 GBp (3 analysts, declining coverage)
- Post-DA FV: 210-225 GBp
- Gap vs consensus: -18% to -24%
- Gap vs market: +18% to +27%
- Our specific edge: Receivables resolution (confirmed by FY2025 results) + understanding that CHP selling is structural overhang creating a discount on a WIDE-moat business. The market is right that CHP selling depresses price; we believe it creates a BUYING opportunity if entry is low enough.
- **WARNING: Edge is NARROW.** Our FV (210-225p) is BELOW the consensus (275p). We are not more bullish than the sell-side. Our edge is specific: we believe the stock is buyable at ~165p because the CHP overhang creates episodic dips, and the business compounds at 8%+ organically. This is a PATIENCE edge, not an INSIGHT edge.

## Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis (R3) | 235 GBp | 20x OE (60%) + 17x EV/EBIT (40%), -11.3% DA |
| Market | 177.60 GBp | Current price |
| DA bear | 169 GBp | 12x FY2026E EV/EBIT, bear growth + margin assumptions |

## Recomendacion al Investment Committee

1. **Maintain SO at 165p.** The FY2025 results were PASS at low end. Receivables resolved. NRR declining but still above 100%. The 165p entry provides ~22% MoS to DA-adjusted FV of 210-215p and ~5% cushion above DA bear 169p.

2. **Adjust R3 FV to 210-225p** to reflect: (a) NRR decline 112%->109%, (b) FX headwind GBP 2.4M on FY2026 profit, (c) SE revenue material decline guided, (d) illiquidity/CHP overhang discount.

3. **Expected Growth header should be 6% for FY2026, 8% normalized.** The 8% in the thesis header is reasonable for a 3-year average but FY2026 will be below that.

4. **Do NOT market-buy at 177.60p.** While E[CAGR] at 177.60p is attractive (~15-17% vs adjusted FV 215p), the near-term catalysts are NEGATIVE (growth deceleration year, FX drag). The stock dropped 10.4% post-results despite meeting expectations -- the market is telling us something. Wait for: (a) further price weakness to 165p, (b) H1 2026 results confirmation that subscription growth compensates for SE decline.

5. **UK concentration:** Post-MONY.L sale, this would be a 2nd UK position (with IHP.L), not 5th. UK concentration concern is MATERIALLY REDUCED from the original R1 context.

6. **Monitor NRR closely.** If H1 2026 NRR drops below 105%, this is a YELLOW flag. Below 100% = KC#1 triggered.

7. **Solifi competitive intelligence:** Before R4, WebSearch for any Solifi client wins in 2026, particularly in US Auto (Alfa's core growth market).

---

## META-REFLECTION

### Dudas/Incertidumbres
- Could not confirm whether CHP sold shares in H2 2025. The FY2025 results did not mention any CHP activity. If CHP has paused selling, the overhang thesis weakens.
- NRR decline from 112% to 109% -- is this a one-off or a trend? Only H1 2026 will answer this.
- Analyst coverage appears to have declined from 8 to 3 covering analysts. Could not confirm this independently. If true, it signals reduced institutional interest -- negative for re-rating.
- FX sensitivity is high (45% USD revenue) but macro is unpredictable. If GBP weakens (possible in UK recession scenario), it becomes a tailwind instead.

### Limitaciones de Este Analisis
- No access to FY2025 full annual report (not yet published -- only preliminary results announced Mar 12)
- No financial data on Solifi (private) to quantify competitive scale
- No UK short interest data available for ALFA.L
- Limited to 3 analyst research notes (paywalled)

### Sugerencias para el Sistema
- The prior counter-analysis (Feb 19) should be archived and this version should replace it as the current DA
- The thesis header Expected Growth should be updated to reflect the FY2026 growth deceleration (6% near-term, 8% normalized)
- For stocks with controlling shareholders executing serial sales, the system should track the CHP-equivalent ownership % over time as a standard monitoring metric

### Preguntas para Orchestrator
1. Should the R3 FV be formally revised down from 235p to 210-225p given the new FY2025 data (NRR decline, FX headwind, SE guidance)?
2. At 177.60p (7.6% above 165p entry), should we lower the SO slightly (e.g., 160p) to provide better DA bear-case cushion, or keep at 165p?
3. Is the declining analyst coverage (8 to possibly 3) a concern the committee should weigh?
4. Post-MONY.L sale, UK concentration drops from 4 to 1 position. Does this materially change the UK geo-risk calculus for ALFA.L?

---

*Counter-analysis produced independently by devil's-advocate agent. 2026-03-13.*
*Updated with FY2025 full-year results data (announced March 12, 2026).*
*Prior DA: 2026-02-19. R3 resolution applied FV 265p -> 235p (-11.3%).*
*Verdict: MODERATE COUNTER*

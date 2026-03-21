# Counter-Analysis: CBOE (Cboe Global Markets)

> **DA Verdict:** MODERATE COUNTER
> **Pre-DA FV:** $273
> **Post-DA FV:** $255 (-6.6%)
> **DA Independent Bear FV:** $220 (EV/EBIT 15x on normalized EBIT)
> **Date:** 2026-03-17
> **Thesis Challenged:** R1 thesis dated 2026-03-16

---

## Resumen Ejecutivo

The CBOE thesis correctly identifies a high-quality exchange business with genuine monopoly characteristics (SPX/VIX exclusivity). However, the thesis underestimates three material risks: (1) the extreme concentration of revenue growth in 0DTE options (63% of SPX volume), which creates both regulatory and mean-reversion vulnerability; (2) the S&P Dow Jones license expiration in 2032, which is the single most critical dependency for CBOE's crown jewels and was not mentioned; and (3) fee capture compression in multi-listed options (-21% QoQ), which the record volume narrative masks. The thesis FV of $273 is reasonable but slightly generous given that the market at $292 already prices in 5.3% FCF growth (close to guided mid-single-digit). The thesis verdict of WATCHLIST is appropriate -- CBOE is not buyable at current levels.

---

## Asunciones Clave Desafiadas

### 1. "SPX/VIX Monopoly Is Permanent and Unchallenged"

- **FA Assumption:** SPX options at 74% market share and VIX as exclusive Cboe product constitute an irreplaceable monopoly requiring "decades of regulatory change to dislodge."
- **Evidence in Contra:**
  - The SPX options monopoly depends on a LICENSE AGREEMENT with S&P Dow Jones Indices, not on Cboe-owned IP. This license was extended through 2032 (exclusive) / 2033 (non-exclusive). The thesis OMITS this critical dependency entirely.
  - Upon expiration, S&P DJI could license to competing exchanges (CME, Nasdaq, ICE) or demand materially higher royalties. Cboe already pays royalties on SPX and VIX volumes.
  - Historical precedent: CBOE signed a 20-year extension in 2013 (from 2012 expiry). The next renewal negotiation begins ~2030. S&P DJI (owned by S&P Global, $155B market cap) has significant leverage.
  - If S&P DJI demands royalty increases from current levels, it directly compresses Cboe's operating margins on its highest-margin product line.
- **Severidad:** HIGH
- **Resolution:** Add "S&P DJI license expiration 2032" as a kill condition monitoring item. Model royalty increase scenario (e.g., 50% royalty increase impact on EBIT).

### 2. "0DTE Options Are a Sustainable Growth Driver"

- **FA Assumption:** 0DTE options (57% of SPX volume per thesis, now 63% per February 2026 data) are a "genuine innovation driving new participants" representing secular growth.
- **Evidence in Contra:**
  - 0DTE growth from ~15% of SPX volume (2022) to 63% (Feb 2026) is exponential and likely near saturation. The percentage cannot grow indefinitely -- it mathematically approaches 100%.
  - JP Morgan warned that the growing 0DTE segment "may lead to sharp market swings as large as $30 billion" due to delta-hedging feedback effects. This creates systemic risk arguments for regulatory intervention.
  - The SEC published a staff paper specifically studying 0DTE market dynamics ("Hope at a Reasonable Price: Customer Use of Limit Orders in the 0DTE Market"). Regulatory attention is real and growing.
  - OCC has already imposed intraday margin add-on charges specifically for 0DTE risk. SIFMA acknowledges the systemic risks.
  - If 0DTE volumes normalize (from 63% to 40-50% of SPX), the REVENUE impact would be severe since 0DTE contracts generate proportionally more transactions per notional than longer-dated options.
  - The thesis correctly identifies regulatory risk (KC #7) but underestimates probability. Regulatory scrutiny is ACTIVE, not theoretical.
- **Severidad:** HIGH
- **Resolution:** Model a scenario where 0DTE share of SPX volume declines to 40% (from 63%) -- quantify revenue impact. Increase probability weighting on bear case.

### 3. "Revenue Growth of 17% YoY Is Sustainable / Normalizes to Mid-Single-Digit"

- **FA Assumption:** FY2025 revenue growth of +17% normalizes to guided mid-single-digit, implying a stable trajectory.
- **Evidence in Contra:**
  - FY2023 revenue DECLINED 4.7% when VIX was sustained below 15. This proves the business is highly cyclical around volatility levels.
  - FY2025's +17% was driven by an unusually volatile environment (Hormuz crisis, tariff uncertainty, Fed uncertainty). VIX has been 24-26 in March 2026 -- well above historical average of ~18-20.
  - If the geopolitical situation normalizes (Hormuz resolution, tariff deals), VIX could revert to 15-18, compressing volumes by 20-30%.
  - The 75-80% transaction-based revenue mix means that a single low-volatility year (like 2023) can erase 1-2 years of margin expansion gains.
  - The market at $292 prices in 5.3% FCF growth per the reverse DCF -- essentially the guided rate. There is NO margin of safety for execution. If volumes disappoint for even one quarter, the stock re-rates.
- **Severidad:** MODERATE
- **Resolution:** The thesis already addresses this risk. However, the scenario table should weight bear case higher (30-35%) given the elevated volatility baseline that inflates current numbers.

### 4. "Fee Capture Is Stable"

- **FA Assumption:** Thesis does not address revenue per contract / fee capture trends in detail, focusing instead on volume growth.
- **Evidence in Contra:**
  - Multi-listed options fee capture declined 21% QoQ according to analyst commentary, even as volumes hit records. Volume growth is masking pricing erosion.
  - The Options Regulatory Fee (ORF) rate is scheduled to revert from $0.0023 to $0.0017 per contract side in mid-2026, which could reduce fee revenue by ~26% on regulatory fees.
  - Exchange fee competition is real: CME, Nasdaq, and MIAX all compete aggressively on multi-listed options pricing. Cboe's proprietary products (SPX, VIX) are protected, but multi-listed options (~50%+ of total volume) face persistent fee compression.
  - If volume growth decelerates while fee capture continues declining, the revenue effect is multiplicative (lower volume x lower RPC).
- **Severidad:** MODERATE
- **Resolution:** Separate revenue analysis for proprietary products (SPX/VIX -- pricing power intact) vs. multi-listed options (fee compression real). The blended revenue growth masks divergent trends.

### 5. "QS Adjustment of +8 Points Is Justified"

- **FA Assumption:** QS adjusted from 78 (tool) to 86, with +8 for market position (#1 US options exchange, SPX/VIX monopoly).
- **Evidence in Contra:**
  - The tool scored 0/8 on market position because it requires manual input. An adjustment of +8 is the MAXIMUM possible for this factor, implying absolute dominance. While CBOE's SPX/VIX monopoly is real, the overall exchange business is NOT a monopoly: 31% of US options volume means 69% goes elsewhere.
  - The monopoly specifically applies to proprietary index products (SPX, VIX), not to the broader options exchange business. On multi-listed options, CBOE competes directly with 15+ exchanges.
  - A more balanced adjustment would be +5 to +6 (strong market position on proprietary products, competitive on multi-listed), yielding QS 83-84 rather than 86.
  - 0.2% insider ownership should be a -1 to -2 adjustment on capital allocation, which the thesis notes but does not penalize in the QS.
- **Severidad:** LOW
- **Resolution:** QS 83-84 is more defensible than 86. Still Tier A. The functional impact is minimal.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | S&P DJI license dependency omitted | License expires 2032 exclusive, 2033 non-exclusive. SPX/VIX royalties are a material cost. Renewal risk not addressed. | HIGH |
| 2 | 0DTE concentration approaching saturation | 63% of SPX volume is 0DTE (Feb 2026). Growth rate must decelerate mathematically. | MODERATE |
| 3 | Multi-listed options is competitive, not monopolistic | 31% market share, 15+ exchanges compete. Only proprietary products have true moat. | LOW |
| 4 | EU PFOF ban (June 2026) impacts European growth narrative | Cboe adapting with free retail execution service, but regulatory headwind for growth vector thesis cites. | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 5 | Base case EV/EBIT of 20x assumes continued premium | CME at 18-20x, ICE at 20-22x. If CBOE growth normalizes to peer levels, premium is unjustified above 18x. | MODERATE |
| 6 | DCF terminal value is 74.5% of EV (thesis acknowledges) | High sensitivity to terminal growth assumption. 0.5pp change in terminal = ~$25 per share. | LOW |
| 7 | FV of $273 already below market ($292) | Thesis correctly identifies stock as overvalued. No disagreement on direction, but FV may still be generous. | LOW |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 8 | 0DTE regulatory risk is ACTIVE, not theoretical | SEC staff paper published, OCC margin add-ons imposed, SIFMA acknowledges systemic risks, JP Morgan warns of $30B feedback loops. | HIGH |
| 9 | Fee capture declining 21% QoQ in multi-listed | Record volumes masking pricing erosion in competitive segment. | MODERATE |
| 10 | Revenue declined 4.7% in FY2023 when VIX was low | Proves cyclicality. Current elevated VIX (24-26) flatters numbers unsustainably. | MODERATE |
| 11 | FCF margin 35.7% may include client pass-throughs | Thesis acknowledges in meta-reflection. Need 10-K verification. If overstated, FCF-based valuations are inflated. | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 12 | Stock trades at premium to FA's own FV | $292 vs $273 FV = -6.9%. No urgency to deploy. | LOW |
| 13 | Current elevated VIX flatters near-term earnings | Q1 2026 likely strong due to Hormuz/tariffs, but this may be the peak. Buying near-peak earnings is classic value trap timing. | MODERATE |

---

## Conflictos con Otros Analisis

No moat_assessment.md or risk_assessment.md exists for CBOE (only thesis.md from R1).

---

## Independent Bear-Case Valuation (Phase 3B)

### Method: EV/EBIT on Normalized EBIT (different from FA's primary method)

**Step 1: Normalize EBIT**
- FY2025 EBIT implied at ~$1.62B (from EV/EBIT 18.5x on EV $29.9B)
- FY2023 operating margin was 28.2% on revenue that declined 4.7%
- Normalized EBIT (mid-cycle): Use average of FY2023-2025 margins (~29.7%) on FY2025 revenue = $4.7B * 29.7% = $1.40B
- This is more conservative because it blends the low-vol year (2023) with the high-vol year (2025)

**Step 2: Apply bear multiple**
- Sector trailing multiple for exchanges: CME ~18x, ICE ~20x, Nasdaq ~18x
- Bear multiple for CBOE accounting for volume cyclicality and license risk: 15x
- Rationale: 15x is where exchange stocks trade during low-vol environments (CME traded at ~14-16x during 2023's low-vol period)

**Step 3: Calculate**
- EV = $1.40B * 15 = $21.0B
- Equity = $21.0B + $0.63B (net cash) = $21.6B
- FV = $21.6B / 105M shares = **$206**

### Cross-check: DCF Bear Case
- Using growth 3%, WACC 10%, terminal 2%: **$220** (from tool)

### DA Bear FV: $220 (average of $206 EV/EBIT bear and $220 DCF bear, rounded conservatively)

---

## Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis | $273 | 60/40 bear/base blended EV/EBIT + DCF |
| Market | $292 | Current price |
| DA bear | $220 | EV/EBIT 15x on normalized EBIT + DCF bear |

**Interpretation:** FA $273 < Market $292 -- both FA and DA agree stock is overvalued. DA bear at $220 suggests 24.6% downside risk in adverse scenario. Normal pattern: Market > FA > DA. The thesis correctly identifies no current entry opportunity.

---

## Probability-Weighted FV (Post-DA Adjustment)

The FA's probability weights (25/50/25 for bear/base/bull) are reasonable but slightly optimistic given:
- Current VIX at 24-26 is elevated (flattering base case)
- 0DTE regulatory risk is growing (increasing bear probability)
- S&P license renewal is a medium-term overhang

**Adjusted weights:** 30/50/20 (bear/base/bull)

Using FA's scenario FVs with adjusted weights:
- 0.30 * $220 + 0.50 * $287 + 0.20 * $380 = $66 + $143.5 + $76 = **$286**

Using DA-adjusted bear case ($220 vs FA's $220 -- aligned):
- 0.30 * $220 + 0.50 * $273 + 0.20 * $360 = $66 + $136.5 + $72 = **$275**

**Post-DA FV: $255** (applying additional 7% haircut for: license renewal risk not modeled, 0DTE regulatory risk underweighted, FCF margin uncertainty pending 10-K verification)

Rounding conservatively given DA historical average correction of -15.7% vs my -6.6% (this is a WATCHLIST position, not a BUY, so lighter correction is appropriate).

---

## Edge Assessment

- Analyst consensus PT: ~$270-280 range (based on mid-single-digit growth pricing)
- Post-DA FV: $255
- Gap vs consensus: -6% to -9%
- Our specific edge: We identify the S&P DJI license dependency (2032 expiry) as a material risk that most sell-side coverage treats as perpetual. We also quantify 0DTE concentration risk (63% of SPX volume) which most coverage treats as pure tailwind.
- Gap vs consensus is <10%: **WARNING: Informational edge is THIN.** The WATCHLIST verdict is correct -- we do not have sufficient edge to justify a contrarian position at current prices.

---

## Proposed Additional Kill Conditions

| # | Kill Condition | Rationale |
|---|---------------|-----------|
| KC8 | S&P DJI signals unwillingness to renew license on current terms (ANY indication before 2032) | The entire SPX/VIX monopoly rests on this license. Any signal of renegotiation pressure is material. |
| KC9 | SEC proposes formal rulemaking on 0DTE options (not just staff papers or commentary) | Formal rulemaking is the step before restrictions. Would directly threaten 63% of SPX volume. |
| KC10 | Multi-listed options market share falls below 25% (from 31%) | Would indicate competitive erosion in the non-monopoly segment of the business. |

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | 2 of 13 (S&P license omission, 0DTE regulatory risk) |
| Desafios no resueltos por thesis | 3 (license dependency, fee capture compression, 0DTE saturation) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

**MODERATE COUNTER:** The thesis is fundamentally sound -- CBOE is a high-quality business with genuine monopoly characteristics, and the WATCHLIST verdict at current valuation is correct. However, the thesis has three gaps that require attention:

1. **S&P DJI License Dependency (HIGH):** This is the single most important omission. The monopoly on SPX options is a LICENSE, not an owned right. It must be monitored as a kill condition.

2. **0DTE Regulatory Risk (HIGH):** The thesis mentions this but underweights the evidence. Regulatory attention is ACTIVE (SEC staff paper, OCC margin add-ons, SIFMA acknowledgment, JP Morgan systemic risk warnings). The probability assigned to KC #7 should be higher than implied.

3. **Fee Capture Compression (MODERATE):** Record volumes are masking pricing erosion in multi-listed options. The thesis revenue analysis should separate proprietary vs. multi-listed trends.

The thesis does NOT need fundamental revision. The WATCHLIST verdict and $245 entry level are appropriate. The DA adjusts FV from $273 to $255, widening the required pullback from -16% to -12.6% from current price.

---

## Recomendacion al Investment Committee

1. **Add KC8 (S&P DJI license)** to the kill conditions before any future deployment.
2. **Verify FCF margin** against 10-K to confirm $1.68B FCF is not distorted by client pass-throughs.
3. **Monitor 0DTE regulatory developments** quarterly -- any formal SEC rulemaking proposal should trigger immediate re-evaluation.
4. **If CBOE reaches $245 entry**, conduct R3 resolution incorporating these DA findings before execution.
5. **Do not deploy above $245** given thin informational edge and -6.6% DA correction to FV.

---

## META-REFLECTION

### Dudas/Incertidumbres
- **FCF distortion magnitude:** The thesis flagged that FCF margin of 35.7% may include client money flows. I could not verify against the 10-K in this analysis. If true, the DCF bear case ($220) could be LOWER since it starts from $1.68B base FCF.
- **S&P DJI royalty rates:** I could not find the specific royalty rate that CBOE pays S&P DJI for SPX/VIX products. This is material for modeling renewal risk. It may be disclosed in the 10-K.
- **0DTE revenue contribution:** I could not isolate what percentage of CBOE's net revenue comes specifically from 0DTE contracts vs. longer-dated SPX options. This matters for quantifying regulatory impact.

### Limitaciones de Este Analisis
- CBOE is not in the smart money graph -- no institutional flow data beyond basic yfinance holdings
- Short interest report date from yfinance shows 2018-08-31, clearly stale. The 3.0% figure is likely current but unverifiable.
- Could not access 10-K directly to verify FCF composition or royalty expense details
- Fee capture decline figure (21% QoQ) comes from analyst commentary, not from primary filing data

### Sugerencias para el Sistema
- Enroll CBOE in smart_money graph for institutional tracking if added to basket pipeline
- Exchange-sector valuation template needed: gross vs net revenue creates persistent margin calculation confusion
- 0DTE monitoring should be a standing item for any exchange position given regulatory trajectory

### Preguntas para Orchestrator
1. Should CBOE be added to Data & Analytics Monopolies basket pipeline given MODERATE COUNTER verdict?
2. Is the S&P DJI license renewal (2032) sufficiently distant to deprioritize, or should it be treated as a structural overhang on fair value?
3. Given DA average correction is -15.7% but this is only -6.6%, does the committee want a larger haircut to stay calibrated with historical DA corrections?

---

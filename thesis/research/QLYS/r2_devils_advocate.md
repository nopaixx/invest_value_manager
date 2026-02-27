# Counter-Analysis: QLYS (Qualys, Inc.)

## Fecha: 2026-02-27

---

## CALIBRATION (Fase 0.5)

**Market Anchor:** Market at $93.68 implies -2.3% FCF decline for 5 years. Historical FCF CAGR: 9.8%. Gap: 12.1pp.
**DA Historical Stats:** 22 corrections, avg -16.2%, median -15.0%. All corrections negative. No outcomes measured yet (first review Aug 2026). Pattern: DA has NEVER increased a FV.
**Asymmetry:** 4.44x (bull +111% vs bear -25%). Favorable on paper.

**Anchor Principle:** The FA must prove the market is WRONG at $93.68. The market is my starting assumption, not the FA's $128 FV.

---

## Resumen Ejecutivo

The R1 thesis identifies a genuinely high-quality business (ROIC 70%+, FCF margin 45%, net cash) trading at a depressed multiple. However, the thesis **omits a critical historical event** (Microsoft Defender partnership termination in May 2024, which triggered a 10%+ sell-off and a law firm investigation), **materially underestimates the platformization risk** (Tenable -50%, Rapid7 -80% from highs confirm this is structural, not temporary), and **inflates the QS from 64 to 82 with a +18 adjustment that is not fully justified** (the ROIC NaN issue is now resolved by the tool, which scores 81 natively -- the manual +18 was overcompensation). The NRR at 103% and declining, combined with billings deceleration to 5.6% in Q4 (below revenue growth of 10%), signals genuine demand weakening that the thesis acknowledges but insufficiently weights. The thesis FV of $128 is too high; a more defensible range is $95-110.

**Verdict: MODERATE COUNTER**

---

## Asunciones Clave Desafiadas

### 1. QS Adjustment from 64 to 82 (+18 points)

- **FA's claim:** Tool scored 64 due to ROIC NaN bug (FY2025 data missing). Actual ROIC is 70.5%. Adjustment: +15 for ROIC, +5 for market position, -2 for conservatism = +18 net.
- **Evidence against:** When I run `quality_scorer.py QLYS --detailed` TODAY (Feb 27, 2026), the tool's Legacy Score is **81/100 (Tier A)**, with ROIC Spread scoring **15/15** and ROIC Persistence scoring **7/7**. The NaN bug appears resolved. The tool natively scores 81 -- which means the FA's manual adjustment of +18 from 64 would yield 82, which is essentially the same as the tool's current 81. **The issue is not the final number, but the process**: the FA was working from stale tool output (64) and manually adjusting upward by 18 points, which appeared aggressive. The tool now confirms 81, so the QS is reasonable -- but the FA should have flagged the tool staleness rather than applying a large manual override.
- **Residual concern:** Market Position is still 0/8 in the tool (manual assessment needed). The FA scored 5/8. Given that IDC ranks Tenable #1 in device vulnerability and exposure management (not Qualys), and the broader exposure management market sees Qualys as #3-5, 5/8 is generous. I would score 3/8 (+3 points, not +5).
- **Severidad:** **LOW** -- The net QS difference is minor (81 tool vs 82 adjusted). The process was concerning but the outcome is defensible.
- **Resolution:** Accept QS 81 (tool) or 82 (adjusted). Tier A is justified. No material impact on thesis.

### 2. Platformization is a "Manageable" Risk

- **FA's claim:** Qualys has switching costs (18-36 months to migrate), 3 billion+ IPs scanned (data moat), Gartner MQ Leader status, and is expanding into ETM/TotalCloud to become a platform.
- **Evidence against:**
  - **Tenable (TENB) is down 50% from 52wH ($19.38 vs $38.83)** and has no P/E (losses). Tenable is the #1 in VM by IDC, seven consecutive years. If the VM market leader is being destroyed by platformization, Qualys (#2-3) is MORE vulnerable, not less.
  - **Rapid7 (RPD) is down 80% from 52wH ($6.39 vs $30.95)**. This is the third VM specialist, and its near-total collapse confirms platformization is NOT hypothetical -- it is happening NOW and accelerating.
  - **Article "The Platform Paradox" (Jan 2026)** explicitly names Tenable's 52-week low as a direct consequence of platform consolidation. The article notes cybersecurity is in "the most aggressive consolidation phase since the early 2010s."
  - **Google acquired Wiz for $32B, PANW acquired CyberArk for $25B**. These mega-deals confirm that platform vendors are buying capabilities that Qualys is trying to build organically. Qualys's TotalCloud is at 5% of bookings -- it took PANW and CRWD years and billions in M&A to build their platforms.
  - **Microsoft ended its OEM partnership with Qualys for Defender vulnerability scanning (May 2024)**. This was a MATERIAL event that triggered a 10% stock drop and a securities investigation by multiple law firms. **The R1 thesis does NOT mention this event AT ALL.** This is a significant omission -- losing the default VM provider status in the world's largest cloud platform is a structural negative.
  - **CrowdStrike Falcon Exposure Management** integrates with 180+ tools and offers unified RBVM, CAASM, and ITAM from a single console. This is EXACTLY the "we do VM plus everything else" value proposition that erodes Qualys's standalone case.
  - Large-cap vs small-cap divergence in cybersecurity: "Of 12 vendors between $1.1B and $14.9B, ALL 12 saw market cap decline" in 2025 (per sector view). Qualys at $3.4B is firmly in the "loser" category by market cap.
- **Severidad:** **HIGH** -- Platformization is not a hypothetical risk. It is an ongoing structural transformation with concrete evidence (TENB -50%, RPD -80%, MSFT Defender partnership loss). The thesis acknowledges the risk but classifies it as manageable. The evidence suggests it is the DOMINANT force shaping QLYS valuation.
- **Resolution:** The investment committee must assess: Is QLYS on a path to become a platform (like FTNT did), or is it being marginalized like TENB/RPD? The answer depends heavily on ETM/TotalCloud execution. At 5% of bookings, the platform pivot is embryonic.

### 3. NRR at 103% is "Less Relevant" Because of Asset-Based Pricing

- **FA's claim:** NRR is less meaningful for Qualys because growth comes from new customers and new assets, not upselling seats. ARR growth (9.5%) and deferred revenue growth (8%) are better metrics.
- **Evidence against:**
  - NRR of 103% means existing customers are barely growing spend. This IS relevant even for asset-based models -- it means existing customers are not deploying more modules (ETM, TotalCloud, CNAPP) from Qualys. Cross-sell is failing.
  - The NRR declined from 104% to 103% in Q4 2025. This is a small move but the DIRECTION matters -- it signals continued deterioration, not stabilization.
  - Management themselves guided for "stable NRR around 103%" in 2026 -- they are NOT projecting improvement.
  - **Deferred revenue growth at 8% is BELOW revenue growth of 10%**. This is a NEGATIVE leading indicator -- it means future recognized revenue is growing slower than current revenue. The thesis mentions this ($401M, +8% YoY) but does not flag the deceleration from 11.5% (FY2024) to 8% (FY2025) in deferred revenue growth.
  - Billings growth in Q4 2025 was only 5.6% YoY ($204.9M). This is the WEAKEST leading indicator: billings < deferred revenue growth < revenue growth < ARR growth. The pipeline is decelerating layer by layer.
  - **Customer retention "above 90%" is vague.** Management says "comfortably above 90%" for gross retention, but 90% gross retention with 103% NRR implies only ~13% gross expansion from retained customers -- and some of that is pricing, not volume. If gross retention is 92%, net expansion from retained is 11%. Strip out price increases (~2-3%) and organic expansion is 8-9%. That is barely keeping pace with asset growth in existing enterprises.
- **Severidad:** **MODERATE** -- The FA's argument that NRR is less relevant has some merit, but the DIRECTION of all leading indicators (billings, deferred revenue, NRR) is deteriorating. Dismissing NRR entirely misses the signal.
- **Resolution:** The committee should track billings growth as the PRIMARY leading indicator. If Q1 2026 billings growth declines further below 5%, this is a CRITICAL deterioration signal.

### 4. Microsoft Defender Partnership Loss (OMISSION)

- **FA's claim:** The thesis does not mention this event.
- **Evidence:** In January 2024, Qualys and Microsoft announced the sunsetting of their embedded integration for Microsoft Defender for Cloud. Effective May 1, 2024, Microsoft replaced Qualys with its own Microsoft Defender Vulnerability Management (MDVM). This triggered:
  - A 10.45% stock price drop on February 5, 2024 (from ~$188 to $168)
  - Securities investigations by Schall Law Firm, Bronstein Gewirtz & Grossman LLC
  - Morgan Stanley analyst warning that "with Microsoft being one of Qualys' largest customers and partners, top-line risks as potentially material"
- **Impact:** While the financial impact was framed as "mutual" and Qualys maintains a BYOL (Bring Your Own License) model and a Copilot partnership, losing the default VM provider status in Microsoft Defender for Cloud is structurally negative. It validates that hyperscaler native security is not hypothetical -- Microsoft chose to REPLACE Qualys with its own offering. This sets a precedent for AWS and GCP to do the same.
- **Severidad:** **HIGH** -- This is a material historical event that the thesis should have referenced. It directly supports the hyperscaler competition concern and weakens the "switching costs protect us" argument (Microsoft switched away from Qualys for its own platform).
- **Resolution:** The thesis must include this event. The committee should evaluate: (a) what was the actual revenue impact from the MSFT partnership loss? (b) are there similar OEM/partnership arrangements at risk?

### 5. FV of $128 (Weighted) is Anchored to Optimistic DCF

- **FA's claim:** Weighted FV of $128.54 (DCF $124.45 at 60% weight + EV/EBIT 15x at 40% weight). Conservative FV $108.
- **Evidence against:**
  - The DCF uses WACC 9.0% (tool default) but the FA derived WACC of 7.1-7.5%. The choice to use the higher 9.0% provides conservatism, which is appropriate.
  - HOWEVER: Terminal Value is 74.5% of Enterprise Value. The FA correctly identifies this as "HIGH SENSITIVITY" and warns the point estimate is unreliable. Yet the weighted FV of $128 is the point estimate. If TV is 74.5% of EV, the DCF is essentially a terminal value model -- it is pricing year 6+ cash flows, which are the most uncertain.
  - The FA uses FCF growth of 5% for 5 years (from tool default). But billings growth in Q4 was 5.6% and decelerating. If revenue growth is 7-8% (guided), and FCF margin declines from 45% to low-40% (guided), FCF growth could be 4-5% at best. The DCF may be modeling the optimistic end of what management is guiding.
  - The EV/EBIT method uses 15x Non-GAAP EBIT. This is described as "conservative -- below even mature tech multiples of 18-22x." But for a company growing at 7-8% with NRR 103% and platformization risk, 15x Non-GAAP may not be conservative -- it may be fair or even slightly generous.
  - **Comparable: Tenable trades at EV/Revenue ~2.5x and no positive P/E.** Rapid7 at EV/Revenue ~1.7x. These are the closest VM comps. Qualys trades at EV/Revenue ~5.0x -- a 2x premium over its closest peer. The premium is justified by higher margins, but the magnitude may be excessive.
  - **The analyst consensus PT of $138.53** (mean) is higher than the FA's $128. Per Error #49 (anclar FV al consensus), our FV should ideally be INDEPENDENT of consensus. But the FA's FV ($128) is only 7.6% below consensus -- this is not a strong independent view. Our specific edge is unclear.
- **Severidad:** **MODERATE** -- The FV is not egregiously wrong, but it relies heavily on a high-sensitivity DCF and a Non-GAAP multiple. The conservative FV of $108 is more defensible.
- **Resolution:** Anchor to the conservative FV of $108, not the weighted $128. MoS vs $108 at current price $93.68 is only 15.3%, which is below typical Tier A entry points (ADBE entered at 31%, NVO at 38%).

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Platformization destroying VM specialists | TENB -50%, RPD -80%, "ALL 12 mid-cap cyber stocks declined in 2025" | HIGH |
| 2 | Microsoft Defender partnership loss (omitted) | May 2024 sunset, 10% stock drop, law firm investigations, validates hyperscaler threat | HIGH |
| 3 | TotalCloud/ETM platform pivot is embryonic | Only 5% of bookings (from 4%), organic build vs PANW/CRWD M&A-fueled platforms | MODERATE |
| 4 | NRR declining, cross-sell failing | NRR 103% -> guided stable 103%. Existing customers not adopting new modules | MODERATE |
| 5 | Billings deceleration as lead indicator | Q4 billings 5.6% < revenue 10%. Current billings growth FY2025 8% vs 9% FY2024 | MODERATE |
| 6 | Deferred revenue growth decelerating | From 13.9% (2022) to 11.5% (2024) to 8% (FY2025). Pipeline slowing | LOW-MODERATE |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 7 | DCF terminal value 74.5% = unreliable point estimate | FA acknowledges this but still weights DCF at 60%. TV sensitivity dominates | MODERATE |
| 8 | EV/Revenue premium 2x over closest peers | QLYS at 5.0x vs TENB 2.5x, RPD 1.7x. Premium justified by margins but magnitude questionable | LOW-MODERATE |
| 9 | FV $128 only 7.6% below consensus $138 | Weak independent view. Per Error #49, if FV = consensus, no edge | LOW |
| 10 | Conservative FV $108 gives only 15% MoS | Below precedent for Tier A entries (ADBE 31%, NVO 38%, MORN 17%) | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 11 | Hyperscaler native VM proven (MSFT Defender) | Microsoft replaced Qualys with MDVM. AWS Inspector, GCP Security Command Center exist | HIGH |
| 12 | Schall Law Firm / Bronstein investigation | Ongoing since Feb 2024. No resolution found. Securities fraud investigation | LOW |
| 13 | Management low ownership + active selling | CEO 0.7% + selling $669K Jan 2026. CFO selling $2.5M+ in 3 months. Officer selling too | MODERATE |
| 14 | AI commoditization of basic VM scanning | Claude Code Security, AI-orchestrated scanning emerging. Point VM is most automatable function | LOW-MODERATE |
| 15 | Receivables growing faster than revenue | 12.5% vs 9.6% (narrative_checker). Collection cycles lengthening | LOW |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 16 | SaaSpocalypse may not be over | $800B destroyed in software. Macro uncertainty (tariffs, rates) ongoing | MODERATE |
| 17 | Q1 2026 earnings critical (Apr) | If billings decelerate further, stock could re-test 52wL $85 or break lower | LOW-MODERATE |
| 18 | FTNT already approved at $73 -- better risk/reward in same sector | Broader platform, ASIC moat, higher growth. Capital should flow to FTNT first per P16 | MODERATE |

---

## Conflictos con Otros Analisis

**Sector View (cybersecurity.md):** The sector view explicitly states: "Of 12 vendors between $1.1B and $14.9B, ALL 12 saw market cap decline" in 2025. QLYS at $3.4B falls squarely in this category. The sector view also identifies platformization as the "defining trend" and lists QLYS in the "Empresas Objetivo" at ALTA priority but acknowledges it is a point solution specialist. The R1 thesis does not sufficiently reconcile this sector-level risk with its company-level optimism.

**FTNT vs QLYS:** The sector already has FTNT at $79.12 with an SO at $73 (R4 approved). QLYS would add sector concentration in cybersecurity. FTNT is the better platform play. QLYS is the niche VM specialist. If platformization is the dominant trend (which the evidence strongly suggests), capital should flow to the platform winner (FTNT), not the point solution (QLYS).

---

## Independent Bear-Case Valuation (Fase 3B)

### Method: EV/FCF Trailing (different from FA's DCF + EV/EBIT methods)

**Bear assumptions:**
- FY2026 Revenue: $718M (low end of guidance $717-725M)
- FCF margin: 38% (below management's "low-40%" guide, reflecting competitive pricing pressure)
- FCF FY2026E: $273M
- Apply trailing EV/FCF multiple of 12x (bear case for 7% grower with platformization risk)
  - Justification: TENB trades at ~13x EV/FCF on 2025 estimates; QLYS deserves slight discount for slower growth
- EV = 12x * $273M = $3,276M
- Add net cash: $394M
- Equity value: $3,670M
- Shares: 36.0M
- **DA Bear FV: $102/share**

### Method 2: Reverse DCF sanity check

- At market price $93.68, market implies -2.3% FCF decline.
- Management guides 7-8% revenue + "low-40%" FCF margin = FCF of ~$287-305M on ~$720M revenue
- That is FCF flat to +3% growth (from $304M FY2025), NOT -2.3% decline
- So the market IS pricing in worse-than-guided. The question is whether the market is right (platformization accelerating faster than management admits) or wrong.

### Three-Number Table

| Source | FV | Method |
|--------|-----|--------|
| FA thesis (weighted) | $128.54 | DCF 60% + EV/EBIT 40% |
| FA thesis (conservative) | $108 | Adjusted down from weighted |
| Market | $93.68 | Current price |
| DA bear | $102 | EV/FCF 12x on FY2026E bear |
| Analyst consensus | $138.53 | Mean sell-side PT |

**Interpretation:** FA ($128) > Consensus ($138 -- wait, FA is actually below consensus) > DA Conservative ($108) > DA Bear ($102) > Market ($93.68). The market is below even my bear case. This suggests either genuine upside even in the bear case, OR the market is pricing in risks beyond my bear assumptions (accelerated platformization, customer loss, further guidance cuts).

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Total desafios | 18 |
| Desafios HIGH/CRITICAL | 3 HIGH (platformization, MSFT omission, hyperscaler native VM) |
| Desafios MODERATE | 8 |
| Desafios LOW | 7 |
| Desafios no resueltos por thesis | 2 (MSFT Defender loss omitted, platformization severity underweighted) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion

**MODERATE COUNTER:** The thesis has identifiable gaps. The omission of the Microsoft Defender partnership loss is a research oversight that should be corrected. The platformization risk is underweighted given concrete evidence from TENB/RPD stock collapses. However, the core thesis (QLYS is a high-quality business at a depressed valuation) has merit -- the question is whether the depression is temporary (SaaSpocalypse contagion) or structural (VM specialist being marginalized). The FV should be anchored to the conservative estimate ($108), not the weighted estimate ($128). At current price $93.68, this implies 15% upside to conservative FV -- meaningful but not exceptional for a Tier A entry.

---

## Edge Assessment

- **Analyst consensus PT:** $138.53 (mean of 19 analysts; range $113-170)
- **Post-DA FV:** $108 (conservative), $120 (if I split between FA's $128 and my $102)
- **Gap vs consensus:** Post-DA $108 is 22% below consensus $138.53
- **Our specific edge:** We recognize platformization risk more seriously than sell-side (who largely maintain Buy/Hold ratings). We also flag the MSFT Defender loss and billings deceleration trend as leading indicators that consensus may be too optimistic. However, if consensus is already at $138 and we are at $108, our view is MORE bearish than consensus -- not more bullish. **We do not have a clear bullish edge over consensus.**
- **WARNING: Our FV ($108-120) is BELOW consensus ($138). If we are buying because we believe FV is $108 and the market is at $93, our thesis depends on the market being too bearish -- but consensus is more bullish than us. This is an unusual position that warrants extra scrutiny.**

---

## Recommended FV Adjustment

| Item | FA Value | DA Adjustment | Post-DA Value | Reasoning |
|------|----------|---------------|---------------|-----------|
| QS | 82 | -1 | 81 | Tool now scores 81 natively. Market position 3/8 not 5/8 |
| Weighted FV | $128.54 | -$18 to -$23 | $105-110 | Anchor to conservative end. Higher sensitivity DCF. Platformization risk premium |
| Conservative FV | $108 | Accept | $105-108 | Slight haircut for MSFT Defender loss and billings deceleration |
| Bear FV | $101.21 | +$1 | $102 | My independent bear at $102 aligns closely |
| Entry target | $78-82 | Widen to $75-85 | $75-85 | $85 with clear billings improvement; $75 without |

**Post-DA Fair Value: $105-110**
**Recommended entry: $80-85** (MoS 18-24% vs $105-110 post-DA FV)

---

## Recomendacion al Investment Committee

1. **Correct the MSFT Defender omission.** The R1 thesis must include the May 2024 partnership termination, its revenue impact, and the precedent it sets for hyperscaler competition. This is material information.

2. **Weight platformization as the PRIMARY risk, not a secondary one.** TENB -50% and RPD -80% are not noise -- they are the market pricing in structural marginalization of VM point solutions. Qualys's ETM/TotalCloud pivot at 5% of bookings is insufficient evidence of platform viability.

3. **Monitor billings growth as the key leading indicator.** Q4 2025 billings at 5.6% is concerning. If Q1 2026 billings growth drops below 5%, this should trigger a thesis review.

4. **Capital allocation priority: FTNT over QLYS.** Both are cybersecurity, but FTNT is the platform winner and QLYS is the point solution at risk. Deploying in both creates sector concentration with correlated downside but asymmetric upside (FTNT has platform optionality, QLYS does not).

5. **Anchor to conservative FV of $105-110, not $128.** Entry at $80-85 provides adequate MoS. Entry at $91 (current) provides only ~15% MoS to post-DA FV -- below typical Tier A precedents.

6. **Resolve before R4:** (a) What was the actual revenue impact from the MSFT Defender loss in FY2024-2025? (b) Are there other OEM/partnership revenues at risk? (c) What is the Q1 2026 billings growth trajectory?

---

## META-REFLECTION

### Dudas/Incertidumbres
- The market pricing at $93.68 is below my independent bear case of $102. This suggests either the market is overly pessimistic (creating genuine opportunity) or there are risks I have not identified. I cannot fully resolve this.
- The platformization risk is real but the TIMING is uncertain. QLYS could have 3-5 years of profitable operation even if it is slowly losing market position, similar to how CHKP has survived decades of "legacy" status.
- The Schall Law Firm investigation status is unclear -- I could not find a resolution. This could be a non-event (ambulance-chasing) or could surface material issues.
- Gross retention "above 90%" is vague. The difference between 91% and 96% is enormous for long-term compounding. Management's reluctance to give a precise number is itself a yellow flag.

### Limitaciones de Este Analisis
- I could not access the actual Q4 2025 earnings call transcript to verify billings details and management commentary on platformization response
- I do not have Tenable's detailed financial breakdown to do a proper comp analysis (EV/FCF, margins)
- The law firm investigation outcome is not publicly available in my search results
- I could not verify the precise revenue impact of the Microsoft Defender partnership loss on FY2024-2025 results

### Sugerencias para el Sistema
- **R1 thesis checklist should include "material events in past 24 months"** -- the MSFT Defender loss omission could have been prevented by a systematic check of historical news/events
- **VM specialist comps (TENB, RPD) should be mandatory in any QLYS analysis** -- they are the closest peers and their performance is the most relevant valuation anchor
- **Billings vs revenue growth spread should be calculated as a standard metric** -- when billings < revenue growth, it is a negative lead indicator that should be flagged automatically

### Preguntas para Orchestrator
1. Given that FTNT is already R4 approved with SO at $73, does it make sense to advance QLYS through R3/R4? The capital would likely go to FTNT first, and sector concentration argues against both.
2. The market price ($93.68) is below my bear case ($102). Should this be treated as a signal that something is genuinely cheap, or that the market knows something I do not?
3. Should we add a "platformization risk" kill condition -- e.g., if TotalCloud bookings fail to reach 8% of total by FY2027, revisit thesis?

---

## Sources

- [Qualys Q4 2025 Earnings Release](https://www.prnewswire.com/news-releases/qualys-announces-fourth-quarter-and-full-year-2025-financial-results-302680676.html)
- [Why QLYS Is Down 18% After Soft 2026 Outlook (Simply Wall St)](https://simplywall.st/stocks/us/software/nasdaq-qlys/qualys/news/why-qualys-qlys-is-down-180-after-soft-2026-outlook-tempers)
- [The Platform Paradox: Tenable Hits 52-Week Low (FinancialContent)](https://markets.financialcontent.com/wss/article/marketminute-2026-1-5-the-platform-paradox-tenable-hits-52-week-low-as-cybersecurity-giants-crowd-out-the-specialists)
- [Rapid7, Tenable, Qualys Shares Plummet (StockStory)](https://stockstory.org/us/stocks/nasdaq/rpd/news/why-up-down/rapid7-tenable-sentinelone-zscaler-and-qualys-shares-plummet-what-you-need-to-know)
- [Qualys and Microsoft Sunset Embedded Integration (Qualys Blog)](https://blog.qualys.com/product-tech/2024/01/09/qualys-and-microsoft-sunset-embedded-integration-of-qualys-solutions-for-microsoft-defender-for-cloud)
- [Qualys Under Pressure as Microsoft Partnership Ending (TipRanks)](https://www.tipranks.com/news/the-fly/qualys-under-pressure-as-firm-says-microsoft-vulnerability-partnership-ending-2)
- [Schall Law Firm Investigation into Qualys (AccessNewsWire)](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/investigation-into-qualys-inc-by-the-schall-law-firm-encourages-i-888390)
- [Tenable Ranks #1 in IDC VM Market Share (Tenable PR)](https://www.tenable.com/press-releases/tenable-ranks-1-in-device-vulnerability-and-exposure-management)
- [Qualys CFO Sells $873K in Stock (Investing.com)](https://www.investing.com/news/insider-trading-news/qualys-cfo-kim-joo-mi-sells-873k-in-qlys-stock-93CH-4492133)
- [Qualys CEO Sells $341K in Stock (Investing.com)](https://www.investing.com/news/insider-trading-news/thakar-sumedh-s-ceo-of-qualys-sells-341k-in-qlys-stock-93CH-4357519)
- [Qualys Analyst Ratings and Price Targets (Benzinga)](https://www.benzinga.com/quote/QLYS/analyst-ratings)
- [QLYS Short Interest Feb 2026 (MarketBeat)](https://www.marketbeat.com/stocks/NASDAQ/QLYS/short-interest/)
- [Vulnerability Management Market $24B by 2030 (BusinessWire)](https://www.businesswire.com/news/home/20250401039762/en/Vulnerability-Management-Research-Report-2025)
- [CrowdStrike Falcon Exposure Management (CrowdStrike)](https://www.crowdstrike.com/en-us/platform/exposure-management/)
- [Qualys QLYS Q4 2025 Earnings Call Transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/02/06/qualys-qlys-q4-2025-earnings-call-transcript/)

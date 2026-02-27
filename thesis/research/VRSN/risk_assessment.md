# Risk Assessment: VRSN (VeriSign, Inc.)

## Fecha: 2026-02-27

## Risk Score: MEDIUM

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Fundamental | Secular domain base erosion (.com registrations declining) | Media | Alto | HIGH | Price increases offset volume decline; Q4 2025 showed 2.6% base growth reversal |
| 2 | Regulatorio | ICANN/NTIA contract non-renewal or terms change | Baja | Muy Alto | HIGH | Contract extended to 2034 with presumptive renewal; NTIA renewed Nov 2024 |
| 3 | Regulatorio | Political/antitrust intervention on pricing power | Media | Alto | HIGH | Warren/Nadler pressure real but DOJ has known since 2008 without action |
| 4 | Fundamental | AI-driven internet navigation reduces domain relevance | Baja | Muy Alto | HIGH | DNS queries actually doubled due to AI agents; VeriSign positions as "AI infrastructure" |
| 5 | Fundamental | Alternative TLDs (.ai, .io, .shop) erode .com market share | Media | Medio | MEDIUM | nTLDs growing 13.5% YoY but .com still 46% of all domains; brand preference sticky |
| 6 | Valoracion | Berkshire Hathaway further stake reduction signals | Baja | Medio | LOW | Sale was for regulatory threshold (>10%); BH still holds 9.8% and bought more in Dec 2024 |
| 7 | Fundamental | Parked domain non-renewals from Google AdSense shutdown | Baja | Bajo | LOW | VeriSign says <2% of base is parked for monetization; cohort shrinking since 2011 |
| 8 | Financiero | Negative tangible equity from aggressive buybacks | Baja | Bajo | LOW | Interest coverage 14.9x; FCF $1.1B vs $1.8B total debt; debt well-laddered to 2032 |
| 9 | Valoracion | Value trap / dead money at current growth rates | Media | Medio | MEDIUM | Revenue CAGR 5.2%, EPS CAGR 12.3%; 7% price increase starting 2027 is clear catalyst |
| 10 | Fundamental | ICANN April 2026 new gTLD round floods market | Baja | Medio | LOW | 2012 round created 1,200+ gTLDs but .com share barely moved; structural brand preference |
| 11 | Governance | CEO insider selling pattern (consistent, material) | Media | Bajo | LOW | CEO sold $3.78M in Jul-Aug 2025, $1.24M Nov, $1.24M Jan; but holds 10.6% total |
| 12 | Fundamental | .com renewal rate decline below 70% | Baja | Alto | MEDIUM | Current 75%, up from 74% YoY; rising prices from 2027 could pressure; VeriSign guides 1.5-3.5% base growth 2026 |

### Scoring:
- Alta x Alto = CRITICAL
- Alta x Medio OR Media x Alto = HIGH
- Media x Medio = MEDIUM
- Baja x cualquiera OR cualquiera x Bajo = LOW

---

## Top 3 Riesgos Criticos

### 1. Secular Domain Base Erosion + Price Dependency

- **Categoria:** Fundamental
- **Descripcion:** VeriSign's revenue growth model is increasingly dependent on price increases rather than volume growth. The .com domain base declined for 6 consecutive quarters through Q3 2024 before recovering. Even with the Q4 2025 recovery to 173.5M domains (up 2.6% YoY), the long-term trajectory of domain registrations faces headwinds from: (a) market saturation in developed markets, (b) alternative TLDs growing at 13.5% YoY, (c) mobile-first internet reducing direct URL usage, (d) social media platforms as discovery mechanisms. Google's shutdown of AdSense for Domains eliminated the economic rationale for ~2% of the domain base (parked domains).
- **Evidencia:** Domain base declined from ~173M (Q2 2023) to ~169M (Q4 2024) before recovering to 173.5M in Q4 2025. Revenue grew 6.4% in FY2025 driven primarily by the 7% wholesale price increase effective Sep 2024. Without price increases, organic revenue growth would be approximately flat. New gTLDs now at 13.5% YoY growth. VeriSign guides only 1.5-3.5% domain base growth for 2026. .com renewal rate at 75%, slightly below historical norms.
- **Probabilidad:** Media -- domain base has been flat-to-declining over multi-year periods; current recovery may be temporary (driven by "marketing programs" including rebate-driven registrars with high churn). Bear analysts note rebate-driven registrations are unsustainable.
- **Impacto si materializa:** If domain base declines 2-3% annually while price increases are capped at 7% every 4 years: revenue CAGR compresses to ~1-3% (vs current 5-6%). At P/E 25.6x, a re-rating to 20x (appropriate for a low-growth utility) implies ~22% downside ($175 target). If decline accelerates to 5%+ annually, price increases cannot compensate, and revenue actually contracts.
- **Mitigante:** Price increases are contractually guaranteed (7% per year starting 2027 through 2030). Even with flat-to-declining volumes, pricing power alone drives ~5-7% revenue growth during increase years. .com remains the default TLD with enormous switching costs (every .com website, email, and marketing material would need to change). DNS query volume is actually growing (450B daily) driven by AI agents. Deferred revenue grew 8.6% in FY2025, suggesting forward registrations are healthy.
- **Kill condition?:** YES -- If .com renewal rate falls below 70% for 2 consecutive quarters, or if domain base declines >5% in any trailing 12-month period.

### 2. Political/Regulatory Intervention on Pricing Power

- **Categoria:** Regulatorio
- **Descripcion:** VeriSign operates what is effectively a government-designated monopoly. The ICANN .com Registry Agreement allows price increases of up to 7% annually in the final 4 years of each 6-year term (2027-2030 for current contract). However, there is growing political pressure to constrain this pricing power. Senator Elizabeth Warren and Representative Jerry Nadler sent formal letters to NTIA and DOJ arguing VeriSign's pricing constitutes "predatory pricing" at 2x the inflation rate. The American Economic Liberties Project published a detailed policy brief calling for DOJ/NTIA action. A coalition of advocacy groups urged breaking VeriSign's monopoly before the August 2024 contract renewal deadline -- yet NTIA renewed anyway.
- **Evidencia:** Warren/Nadler letter to NTIA/DOJ (Nov 2024). American Economic Liberties Project policy brief (Jul 2024). DOJ acknowledged VeriSign's "significant market power" as early as 2008 but has never acted. NTIA renewed the Cooperative Agreement in November 2024 despite political pressure. The 2024 contract renewal included pricing terms that allow 7% annual increases starting 2027 -- critics call this a "corrupt deal" where ICANN received $20M in exchange for approving price hikes.
- **Probabilidad:** Media -- Political pressure is REAL and growing, but: (a) DOJ has known for 18 years without acting, (b) NTIA just renewed in Nov 2024 WITH the price increase terms, (c) DNS is critical infrastructure and regulators are reluctant to disrupt it, (d) the current administration is not focused on this issue. The risk is more medium-to-long-term: a future administration could impose price caps, mandate competitive bidding, or refuse presumptive renewal.
- **Impacto si materializa:** If price increases are capped at inflation (2-3%) instead of 7%: revenue CAGR drops from ~5-6% to ~2-3% (assuming flat domain base). Stock would re-rate from monopoly compounder (25x P/E) to regulated utility (15-18x P/E), implying 25-40% downside. If the contract is opened to competitive bidding: this is an existential threat, but probability is very low (<5%).
- **Mitigante:** NTIA just renewed (Nov 2024), so no contract risk until 2030 at earliest. Presumptive renewal has been honored every time since 1998. DNS is critical infrastructure -- regulators have strong incentive to maintain stability. VeriSign invests in infrastructure (root servers, DNSSEC, DDoS mitigation) which creates a practical barrier to switching operators. No viable alternative operator has been identified or proposed.
- **Kill condition?:** YES -- If DOJ opens formal antitrust investigation, or if NTIA signals intent not to renew under current terms, or if legislation is introduced with bipartisan support to cap domain pricing.

### 3. AI-Driven Structural Decline in Domain Relevance (Long-Term)

- **Categoria:** Fundamental
- **Descripcion:** The most existential risk to VeriSign is the possibility that AI fundamentally changes how humans navigate the internet, reducing the need for domain names as digital addresses. If AI assistants, chatbots, and voice interfaces become the primary gateway to information and services, users may never type a URL or see a .com domain. Search engines already reduce direct URL navigation; AI could accelerate this trend to obsolescence.
- **Evidencia:** This is largely speculative at current stage. Counter-evidence is strong: VeriSign CEO states AI is having a "positive impact on registrations" and DNS queries have MORE than doubled in 2 years to 450B daily, driven by AI agents that need to access websites to gather data. AI models are trained on web content, which requires domain-based URLs. However, there is a subtle distinction: AI may INCREASE machine-to-machine DNS queries (good for infrastructure load, but VeriSign charges per registration, not per query) while DECREASING human-initiated domain registrations (bad for the registration revenue model). The "SaaSpocalypse" narrative shows how quickly AI disruption fears can destroy software valuations.
- **Probabilidad:** Baja in 1-3 year timeframe. Media in 5-10 year timeframe. The internet's architecture is deeply built on DNS, and replacing it would require a fundamental infrastructure change that takes decades, not years.
- **Impacto si materializa:** If domain registrations enter secular decline of 3-5% annually driven by AI navigation: revenue growth goes negative even with price increases. Terminal value assumptions in any DCF crater. Stock could decline 40-50% as monopoly premium evaporates. However, full obsolescence of .com is highly unlikely -- even in the most aggressive AI scenarios, websites still need addresses.
- **Mitigante:** DNS is infrastructure, not consumer-facing product. AI USES DNS (450B daily queries). Websites still need domains regardless of how users find them. VeriSign is positioning as "digital trust anchor" for combating deepfakes. The company has historically adapted (from SSL certificates to pure registry). Revenue model is per-registration, not per-query, which means even AI-driven query volume doesn't directly help -- but the existence of AI-driven demand for web content preserves the underlying need for domain names.
- **Kill condition?:** NO -- this is a long-term monitoring risk, not a near-term kill condition. Monitor: annual .com new registrations as leading indicator. If new registrations decline >10% YoY for 2 consecutive years, escalate to kill condition.

---

## Additional Risks (Not Top 3, But Material)

### 4. ICANN April 2026 New gTLD Round

- **Categoria:** Fundamental/Competitivo
- **Descripcion:** ICANN opens applications for new generic top-level domains on April 30, 2026. This is the first new round since 2012, which produced 1,200+ new gTLDs. Brand TLDs (.apple, .google) and niche extensions could fragment the domain market.
- **Probabilidad:** Baja impact on .com specifically. The 2012 round produced 1,200+ gTLDs but .com's market share barely moved. The cumulative impact of all new gTLDs over 12 years has been modest.
- **Impacto:** Low-Medium. Even if the 2026 round is large, .com's brand moat (default TLD status, universal recognition, trust) is extraordinarily durable.
- **Mitigante:** .com is the default. New TLDs complement rather than substitute. Many 2012-era gTLDs have negligible adoption.

### 5. Q4 2025 EPS Miss and Revenue Quality Concerns

- **Categoria:** Valoracion
- **Descripcion:** VeriSign reported Q4 2025 EPS of $2.23 vs $2.35 expected (-5.1% miss). While revenue beat slightly ($425.3M vs $424M), the EPS miss raises questions about cost control. Additionally, receivables grew 37.5% vs revenue growth of 6.4% -- a significant divergence that could signal revenue recognition timing issues or customer payment slowdowns.
- **Probabilidad:** Media that cost pressures persist. The receivables divergence warrants investigation.
- **Impacto:** Medium. If margin compression continues, the "prints cash" narrative weakens.
- **Mitigante:** FCF margin actually expanded to 64.5% in FY2025 (vs 56.2% in FY2024). OCF/Net Income of 1.3x is healthy. The EPS miss may be one-off (stock actually rose after report).

### 6. Negative Tangible Equity

- **Categoria:** Financiero
- **Descripcion:** Shareholders' equity is -$2.0B due to $4B+ in cumulative share buybacks exceeding retained earnings. Total debt is $1.8B. This creates a technically negative tangible book value.
- **Probabilidad:** Low for actual financial distress. The negative equity is an accounting artifact of buyback policy, not a sign of business distress.
- **Impacto:** Low. With $1.1B in annual FCF, $580M in cash, and interest coverage of 14.9x, VeriSign has no liquidity concerns. Debt maturities are well-laddered: $550M due 2027, $750M due 2031, $500M due 2032 (just refinanced $500M Apr 2025 maturity at 5.25%).
- **Mitigante:** FCF generously covers all debt service. No covenant risk. The company could stop buybacks and restore positive equity within 2-3 years if needed.

---

## Riesgos NO Mencionados en Thesis

*(No thesis exists yet for VRSN -- this risk assessment is being prepared in parallel with or ahead of fundamental analysis)*

| Riesgo | Severidad | Mencionado en thesis? | Comentario |
|--------|-----------|----------------------|------------|
| Receivables growing 37.5% vs revenue 6.4% | MEDIUM | N/A | Significant divergence -- could signal timing issues or quality deterioration. Must investigate in thesis |
| CEO consistent selling ($3.78M Jul-Aug, $1.24M Nov, $1.24M Jan) | LOW | N/A | Selling is consistent but small vs 10.6% total holding. Pattern rather than signal. |
| Rebate-driven registrations unsustainable | MEDIUM | N/A | Bear analysts note 50% discounts to registrars inflate registration volumes but with high churn |
| Zacks "Strong Sell" downgrade Dec 2025 | LOW | N/A | Single quant-driven downgrade; 3 of 4 analysts rate Buy/Strong Buy |
| Warren/Nadler antitrust pressure | HIGH | N/A | Real political risk to pricing power; DOJ/NTIA aware but inactive for 18 years |
| .com renewal rate at 75% (slightly below historical) | MEDIUM | N/A | If rising prices push renewal rate below 70%, volume decline accelerates |
| Short interest declining (-33.1% MoM to 2.7% of float) | POSITIVE | N/A | Shorts are COVERING, not building. Suggests bearish thesis is weakening |
| AI agents increasing DNS queries (450B daily, 2x in 2 years) | POSITIVE | N/A | Counter-narrative to "domains are obsolete"; AI actually needs DNS infrastructure more |

---

## Kill Conditions Sugeridas

Based on risk assessment findings, these kill conditions should be incorporated into any thesis:

1. **KC-1: .com renewal rate drops below 70% for 2 consecutive quarters.** This would signal that price increases are destroying the installed base faster than new registrations replace it. The current 75% rate has ~5pp of buffer, but the 7% annual price increases starting 2027 could pressure renewals.

2. **KC-2: NTIA or DOJ opens formal antitrust investigation or signals non-renewal of Cooperative Agreement.** While the contract was just renewed (Nov 2024) and extends to 2034, an unexpected policy reversal would be existential. Monitor for: new legislation, DOJ statements, or NTIA communications that deviate from presumptive renewal pattern.

3. **KC-3: Domain base declines >5% in any trailing 12-month period.** This would indicate secular decline is accelerating beyond what price increases can offset. Different from normal cyclical fluctuation (2-3% decline is within historical range).

4. **KC-4: Receivables/Revenue divergence persists for 2+ quarters (>15pp gap).** The Q4 2025 divergence (37.5% receivables growth vs 6.4% revenue growth) needs monitoring. If this is not a timing issue but a structural change in payment patterns or revenue quality, it warrants investigation.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL:** 3 (domain erosion, regulatory/pricing, AI relevance)
- **Riesgos correlacionados?** YES -- Risks #1, #3, and #5 are all facets of the same meta-risk: "is the domain name system becoming less relevant?" If AI reduces domain usage AND alternative TLDs gain share AND regulators cap pricing, the triple impact would be severe. However, current evidence suggests the opposite: AI is INCREASING DNS usage, .com share is stable, and regulators just renewed with pricing power intact.
- **Risk Score Final: MEDIUM**

**Rationale for MEDIUM (not HIGH):**
Despite 3 HIGH-scored individual risks, the mitigants are strong and evidence-based:
- Contract just renewed Nov 2024 to 2034 with pricing power
- Domain base recovered to growth in 2025 after 6 quarters of decline
- AI is driving DNS query volumes UP, not down
- FCF of $1.1B against $1.8B debt = fortress balance sheet
- Short interest declining (-33% MoM) = bears retreating
- Berkshire Hathaway maintaining 9.8% stake and buying in Dec 2024

The risks are REAL but LONG-TERM (5-10 year horizon). In the 1-3 year investment horizon, VeriSign's monopoly is intact, pricing power is contractually guaranteed, and the business model is generating record FCF. The medium-term risk is that the market already prices in the monopoly premium, leaving limited upside if growth disappoints.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **Receivables divergence:** The 37.5% receivables growth vs 6.4% revenue growth is the most concerning data point I found. I could not determine from public sources whether this is a timing issue (Q4 billing cycle), a change in payment terms with registrars, or a genuine quality concern. This needs resolution before finalizing any thesis.
- **Rebate-driven registrations:** Bear analysts claim much of the recent domain base recovery is driven by 50% discounts to registrars, creating high-churn registrations that will reverse. I could not independently verify the magnitude of rebate-driven vs organic registrations. VeriSign's Q4 2025 earnings call mentioned "marketing programs" but did not quantify their contribution.
- **CEO selling pattern:** Bidzos has sold consistently ($3.78M + $1.24M + $1.24M = $6.26M in 7 months). While small vs total holding (10.6%), the consistency and lack of offsetting open-market purchases (only stock awards) is a mild negative signal. Cannot determine if this is planned 10b5-1 sales or discretionary.

### Riesgos que Podrian Estar Subestimados
- **Political/regulatory risk:** I scored this as Media probability because DOJ has been inactive for 18 years. But the CURRENT political environment (populist pressure on monopolies, Warren's persistence, economic liberty coalitions) is different from past cycles. A change in administration or a high-profile domain pricing controversy could accelerate action.
- **Renewal rate sensitivity to price increases:** The 7% annual price increases starting 2027 are unprecedented in frequency. Previous increases were 7% every 4 years. Four consecutive annual 7% increases (2027-2030) would raise the wholesale price from $10.26 to ~$13.45 -- a 31% cumulative increase. The elasticity of domain renewals at these price levels is unknown.

### Discrepancias con Thesis
- No thesis exists yet. This risk assessment should inform the fundamental analysis. Key areas where the thesis MUST address risk findings:
  1. Revenue growth sustainability without volume (price-only growth model)
  2. The receivables/revenue divergence
  3. The political/regulatory environment and how to monitor it
  4. Whether the AI narrative is genuinely positive or a management talking point

### Sugerencias para el Sistema
- For monopoly/regulated businesses like VRSN, the risk assessment should include a dedicated "Regulatory/Political Risk Timeline" that maps: upcoming contract dates, known political opponents, pending legislation, and regulatory body personnel changes. This is more structured than the generic "legal/regulatory" category.
- The receivables/revenue divergence flagged by narrative_checker.py is exactly the kind of signal that should trigger automatic deeper investigation. Consider adding a threshold alert in the tool.

### Preguntas para Orchestrator
1. Is the receivables divergence (37.5% vs 6.4%) a known issue from the Q4 2025 earnings call? If VeriSign explained it, that changes the risk classification.
2. Should the 7% annual price increase schedule (2027-2030) be modeled as a positive catalyst (revenue growth acceleration) or a risk (demand destruction)? My instinct says it is BOTH -- positive for revenue in years 1-2, potentially negative in years 3-4 as elasticity kicks in.
3. The bear case from Insider Monkey and Baird mentions "unsustainable rebate-driven growth." Should the fundamental analyst prioritize verifying this claim from the earnings transcript?

---

**Sources:**

- [VeriSign extends .com contract with ICANN (Nov 2024)](https://webhosting.today/2024/11/28/verisign-extends-com-contract-with-icann/)
- [VeriSign can increase .com prices in 2026](https://domainnamewire.com/2025/11/19/verisign-can-increase-com-prices-in-2026/)
- [Economic Liberties: Reining in VeriSign's Monopoly](https://www.economicliberties.us/wp-content/uploads/2024/07/2024-7-25-Verisign-Policy-Brief-Final.pdf)
- [NTIA/DOJ Must Break VeriSign's Monopoly (Coalition letter)](https://www.economicliberties.us/press-release/ntia-and-doj-must-break-verisigns-monopoly-power-over-domain-names-advocates-urge/)
- [Warren Accuses VeriSign of Monopoly](https://www.pymnts.com/antitrust/2024/warren-accuses-verisign-of-web-domain-registration-monopoly/)
- [The Government Created the Most Profitable Company](https://prospect.org/power/2024-06-27-government-created-most-profitable-company-verisign/)
- [VeriSign Q4 2025: Revenue beats, EPS misses](https://fintool.com/app/research/companies/VRSN/earnings/Q4%202025)
- [VeriSign Q4 2025 slides: domain base grows 2.6%](https://www.investing.com/news/company-news/verisign-q4-2025-slides-domain-base-grows-26-revenue-up-75-despite-eps-miss-93CH-4489136)
- [VeriSign FY2025 Results (Investor Relations)](https://investor.verisign.com/news-releases/news-release-details/verisign-reports-fourth-quarter-and-full-year-2025-results)
- [VeriSign Bear Case Theory](https://finance.yahoo.com/news/verisign-inc-vrsn-bear-case-185945029.html)
- [How VeriSign thinks AI will impact domain names](https://domainnamewire.com/2025/07/29/how-verisign-thanks-ai-will-impact-domain-names/)
- [VeriSign Prints Cash - But Is AI About To Pull The Plug?](https://seekingalpha.com/article/4774457-verisign-prints-cash-but-is-ai-about-to-pull-the-plug)
- [Google's parked domain purge devastates parking revenue](https://domainnamewire.com/2025/09/23/googles-parked-domain-purge-captures-final-advertisers-and-devastates-parking-revenue/)
- [VeriSign clarifies AdSense impact (<2% of base)](https://domainnamewire.com/2025/10/27/verisign-clarifies-how-google-adsense-for-domains-changes-could-affect-its-business/)
- [Berkshire Hathaway VeriSign transactions history](https://stockcircle.com/portfolio/warren-buffett/vrsn/transactions)
- [Insider Selling: VeriSign CEO sells stock](https://www.defenseworld.net/2026/01/18/insider-selling-verisign-nasdaqvrsn-ceo-sells-496560-00-in-stock.html)
- [ICANN 2026 Round: New gTLD Applications](https://newgtldprogram.icann.org/en/application-rounds/round2)
- [Domain name statistics and trends 2026](https://www.hostinger.com/tutorials/domain-name-statistics)
- [TLD Domain Report Feb 2026](https://abtdomain.com/tlds-reports/2026-02/statistics-2026-02-27)
- [VeriSign targets 1.5-3.5% domain base growth for 2026](https://seekingalpha.com/news/4548335-verisign-targets-1_5-percentminus-3_5-percent-domain-name-base-growth-for-2026-as-company)
- [VeriSign $500M senior notes offering (refinancing)](https://www.investing.com/news/sec-filings/verisign-announces-500m-senior-notes-offering-93CH-3920750)
- [NTIA Cooperative Agreement](https://www.ntia.gov/program/verisign-cooperative-agreement)

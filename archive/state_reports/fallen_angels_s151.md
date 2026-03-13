# Fallen Angels Screening — Session 151 (2026-03-13)

> Market context: S&P 500 -4.7% from 52wH, VIX 27.7, Oil $97, correction deepening.
> Screened 188 companies with QS >= 65, drawdown >= 25% from 52wH, ROIC positive.
> Result: 72 fallen angels found. Filtered for sector diversification vs current portfolio.

## Current Portfolio Exposure (for reference)
- **HEAVY**: Tech/SaaS (ADBE, FTNT, GDDY locked), EU Services (EDEN.PA, WKL.AS), UK Platforms (IHP.L, MONY.L)
- **MODERATE**: Pharma (NVO), Financials (HLNE, TW, DOCS)
- **LIGHT/NONE**: Industrials (only BZU.MI cement), Consumer Staples, Energy, Healthcare Equipment, Utilities

## Exclusions
- Current holdings: EDEN.PA, ADBE, NVO, MONY.L, IHP.L, HLNE, DOCS, FTNT, TW, WKL.AS, BZU.MI, CVNA (short)
- Active pipeline/cooldowns: GDDY, DNLM.L, SPGI, KNSL, CPRT, WING, PEGA, QLYS, HALO, CHKP, PAYC, LOPE, SAF.PA, MEDI.OL, VRSN, CMCSA, MSA, ERIE, ANF, MANH, CELH, ALFA.L

---

## TOP 10 FALLEN ANGELS — Ranked by Quality + Drawdown + Sector Diversification

| # | Ticker | Name | QS | Tier | DD% | Price | Sector | ROIC% | Why Interesting |
|---|--------|------|----|------|-----|-------|--------|-------|-----------------|
| 1 | ZTS | Zoetis Inc. | 80 | A | -32.2% | $115.46 | Animal Health | 15.3% | WIDE moat animal pharma. Only pure-play vet pharma at scale. 53% companion animal (secular pet humanization). ZERO portfolio overlap. Fallen from $170 on general pharma selloff but pet spend is non-cyclical. |
| 2 | BEI.DE | Beiersdorf AG | 75 | A | -42.5% | EUR 77.68 | Consumer Staples | 6.6% | German consumer staples (Nivea, Eucerin, La Prairie). ZERO sector exposure. -42% from highs = rare for this quality. Family-controlled (Maxingvest 51%). Defensive business, pricing power, global distribution. |
| 3 | VRSK | Verisk Analytics | 80 | A | -38.4% | $198.04 | Financial Data/Analytics | 16.5% | Data monopoly in insurance analytics. Complements HLNE (different sub-sector). 80% recurring revenue. 38% drawdown rare for this quality moat. ISO/PCS standards create switching costs. |
| 4 | PODD | Insulet Corp. | 66 | B | -33.5% | $236.07 | Healthcare Equipment | 9.4% | Omnipod insulin pump — fills healthcare equipment gap entirely. Duopoly with Medtronic. 33% drawdown on GLP-1 obesity narrative (overdone for Type 1 diabetes). International growth 40%+. |
| 5 | ROP | Roper Technologies | 70 | B | -41.3% | $346.78 | Industrial Technology | 4.2% | Niche industrial software/tech conglomerate. Vertical market monopolies (tolling, water meters, healthcare IT). 70%+ recurring revenue. -41% is unusually deep for a serial acquirer with this track record. |
| 6 | BEAN.SW | Belimo Holding | 75 | A | -28.7% | CHF 695 | Industrial Technology | 17.7% | Swiss HVAC actuator monopolist. 17.7% ROIC. Building energy efficiency secular theme. -29% from highs. Global #1 in damper actuators (70%+ share in key segments). Family ownership. |
| 7 | FDS | FactSet Research Systems | 73 | B | -56.5% | $203.60 | Financial Data | 11.4% | Data & analytics deep value. 56% drawdown = unusual for subscription data business. Complements TW/WKL.AS basket. 95%+ retention rates. Could be Data & Analytics Monopolies 3rd position. |
| 8 | NEU | NewMarket Corp. | 68 | B | -32.6% | $588.08 | Specialty Chemicals | 11.3% | Petroleum additives duopoly (with Lubrizol/Berkshire). Zero analyst coverage = market inefficiency. 90%+ market concentration. Fills Industrials/Materials gap. Family-controlled (Gottwald). Boring, durable, cash-generative. |
| 9 | TEP.L | Telecom Plus (Utility Warehouse) | 67 | B | -36.7% | 1327p | Utilities | 10.6% | UK multi-utility bundler. Fills utilities gap entirely. -37% drawdown. Partners distribute (Avon → Ecotricity model). Capital-light utility disruptor. Different model from traditional utilities. |
| 10 | STMN.SW | Straumann Holding | 72 | B | -29.6% | CHF 81.58 | Healthcare/Dental | 11.1% | Global #1 dental implants. Fills healthcare equipment gap. Premium positioning (Straumann brand). Digital dentistry (iTero competitor). -30% from highs on China volume pricing concerns but company-specific moat intact. |

---

## Honorable Mentions (strong but in sectors we already hold)

| Ticker | Name | QS | DD% | Sector | Note |
|--------|------|----|-----|--------|------|
| RACE.MI | Ferrari | 82/A | -35.7% | Luxury | Already sold S143. At EUR 289 now vs EUR 312 exit. Tempting but E[CAGR] still low. |
| ADP | ADP | 78/A | -36.1% | HR/Payroll | In pipeline (sector view exists). -36% interesting but low growth. |
| RMS.PA | Hermes | 96/A | -28.0% | Luxury | Highest QS in entire universe (96!). At EUR 1,871. But luxury = sector we don't target. |
| MORN | Morningstar | 78/A | -42.5% | Financial Data | Already sold S143. At $181 now vs $164 exit. Would not re-enter at current price. |

## Sector Distribution of Top 10
- **Consumer Staples**: 1 (BEI.DE) — fills gap
- **Animal Health/Pharma**: 1 (ZTS) — different from NVO
- **Financial Data**: 2 (VRSK, FDS) — extends existing basket
- **Healthcare Equipment**: 2 (PODD, STMN.SW) — fills gap
- **Industrial Technology**: 2 (ROP, BEAN.SW) — fills gap
- **Specialty Chemicals**: 1 (NEU) — fills gap
- **Utilities**: 1 (TEP.L) — fills gap

## Next Steps
1. **Immediate R1 candidates (highest priority for sector diversification)**:
   - ZTS (animal health, QS 80 Tier A, -32%)
   - BEI.DE (consumer staples, QS 75 Tier A, -42%)
   - VRSK (data monopoly, QS 80 Tier A, -38%)
2. **Pipeline candidates (strong but need deeper look)**:
   - ROP, BEAN.SW, NEU (industrials gap)
   - PODD, STMN.SW (healthcare equipment gap)
3. **Cash constraint**: Portfolio is 0% cash. These are for rotation candidates or next capital injection.

## Data Source & Methodology
- fallen_angels.py --min-qs 65 --min-drawdown -25 (72 results from 188 scanned)
- dynamic_screener.py --index sp500 --undiscovered (14 results, mostly financials)
- Cross-referenced against r1_cooldowns, current holdings, standing orders
- Prioritized sectors with ZERO or minimal portfolio exposure
- All ROIC positive (no value traps)

---
*Generated: 2026-03-13 | Session 151*

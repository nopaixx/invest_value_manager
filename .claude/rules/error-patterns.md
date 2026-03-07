# Error Patterns — Errores Activos

> Auto-loaded con CLAUDE.md. Solo errores que AUN PUEDEN OCURRIR.
> Archivo completo: `learning/error_patterns_archive.md`

---

## Errores Criticos (mantener numeros originales — error-detector los referencia)

**#3. Hacer manual lo que un agente deberia hacer** (consolida #3, #22, #38, #39, #40)
PASO 0 antes de CUALQUIER tarea: consultar arbol en `agent-protocol.md`. Si hay agente, DELEGAR.
YO ORQUESTO, LOS AGENTES EJECUTAN.

**#7. Popularity bias en stock selection**
SIEMPRE complementar con screening programatico (`dynamic_screener.py --undiscovered`). Si una empresa "me viene a la mente", es sesgo — validar con datos.

**#12. No ejecutar constraint_checker.py antes de BUY/ADD**
SIEMPRE ejecutar `constraint_checker.py CHECK TICKER AMOUNT` antes de recomendar compra.

**#13. No preparar frameworks pre-earnings**
Para CADA posicion con earnings en proximos 7 dias, DEBE existir framework bear/base/bull en la thesis.

**#16. Comprar sin entender el negocio**
Completar `business-analysis-framework` ANTES de cualquier valoracion. Si no puedo explicar el negocio en 2 minutos y por que esta barata, no puedo comprar.

**#18. Depender solo de DCF**
Minimo 2 metodos de valoracion. Seleccionar segun tipo de empresa (ciclica: EV/EBIT, financiera: P/B vs ROE, etc.).

**#29. Sugerir empresas por popularity bias**
ANTES de sugerir: 1) consultar sector views, 2) ejecutar dynamic_screener. SOLO despues puedo sugerir.

**#30. Comprar sin sector view existente** (reincidencia #42)
GATE 0 del Investment Committee: `Glob("world/sectors/*{sector}*")`. Si no existe, STOP.

**#37. Hardcodear reglas en tools/skills**
Tools = DATOS CRUDOS. Skills = FRAMEWORKS. Numeros fijos en codigo me sesgan en el futuro. Usar PRECEDENTES (decisions_log) para consistencia, no hardcoding.

**#41. No completar ciclo post-analisis**
Tras veredicto WATCHLIST/BUY: 1) guardar thesis, 2) actualizar sector view, 3) anadir alerta precio, 4) si BUY: standing order, 5) confirmar al usuario. El analisis NO termina hasta que la alerta esta en el sistema.

**#43. QS de thesis no coincide con quality_scorer.py**
REGLA QS TOOL-FIRST: quality_scorer.py = fuente principal. Thesis muestra AMBOS (QS Tool + QS Ajustado). Ajuste >5 puntos requiere evidencia cuantitativa. Ajustes validos: forward growth deterioration, moat siege, ROIC distortion, insider data incorrect, kill condition approaching.

---

## Errores Short-Specific

**#44. Shortear sin catalizador**
Sin catalizador con fecha identificable → NO shortear. "Esta cara" no es thesis. Precio alto + popularity = trampa clasica. Verificar P10 (Catalizador como Ancla Temporal).

**#45. No cubrir cuando catalizador pasa sin efecto**
Si catalizador pasa y nada cambia → CUBRIR. No esperar "a que eventualmente caiga". El carry sigue corriendo. Cada dia sin catalizador vigente es carry quemado.

**#46. Shortear empresa "cara" sin thesis de fragilidad (Tesla trap)**
Precio alto NO es short thesis. Necesita FRAGILIDAD ESTRUCTURAL documentada: dependencia oculta, modelo de negocio insostenible, cambio regulatorio inminente. Si empresa "me viene a la mente" como short → es sesgo → VALIDAR con datos. Aplica misma disciplina que #7 y #29 para longs.

**#47. Apalancamiento excesivo en shorts**
Razonar sobre leverage desde P1 (Sizing por Conviccion) y P11 (Asimetria Consciente). Consultar precedentes en decisions_log.yaml. El leverage amplifica errores mas que aciertos en shorts por la asimetria natural.

---

## Errores Epistemicos

**#48. Tratar opinion de analista como hecho**
Al leer reportes de analistas, articulos, o noticias: SEPARAR datos primarios de interpretaciones. Un analista que dice "growth is accelerating" es OPINION — verificar contra datos reales (filings, earnings). Clasificar fuente (Nivel 1-4 del critical-thinking skill) ANTES de incorporar. Si mi thesis depende de la conclusion de un tercero sin datos primarios propios, la thesis es fragil. Ver critical-thinking skill: Protocolo Anti-Absorcion de Narrativa.

**#50. Net exposure por omision, no por razonamiento**
Cada sesion DEBE incluir razonamiento explicito sobre exposicion neta (Fase 2.5.6). "No shortear" es valido SOLO si lo razone contra el contexto macro+sectorial actual. Si mi portfolio es 100% long y no documente POR QUE, es decision por omision = error. El short side del sistema NO es opcional — es herramienta que DEBO considerar y aceptar/rechazar explicitamente. Ver: session-protocol Fase 2.5, rotation-engine seccion 4, principles.md P4.

**#49. Anclar Fair Value al consensus price target**
Consensus PT = promedio de opiniones con incentivos mixtos (sell-side necesita volumen). El consensus YA esta en el precio. Si mi FV converge al consensus sin razonamiento independiente, NO tengo ventaja informacional. Derivar FV siempre desde datos primarios (FCF, growth, WACC) con tools propios. Consensus sirve como COMPARACION ("mi FV difiere del consensus en X% porque..."), no como ancla.

---

## Errores Operativos

**#52. No persistir output de pipeline como archivo formal**
Cada ronda del pipeline (R1/S1, R2/S2, R3/S3) DEBE crear un archivo en `thesis/research/TICKER/` o `thesis/short/research/TICKER/`. NUNCA guardar output solo en watchlist.yaml como notas. Archivos minimos por pipeline completado: S1 = thesis.md + moat_assessment.md + risk_assessment.md. R1 = thesis.md. S3/R3 = s3_resolution.md o r3_resolution.md. Error original: CVNA S1 completado en Session 75 sin archivo de thesis — solo notas en watchlist.yaml. Cuando se necesito para S3, el contexto estaba perdido.

**#51. Confundir sesion con dia — incrementar fecha artificialmente**
Session ≠ Dia. Multiples sesiones pueden ocurrir en UN MISMO dia. SIEMPRE obtener fecha real con `date` o `currentDate` del contexto del sistema. NUNCA asumir fecha desde memoria ni incrementar. Al escribir en memory/system.yaml, usar la fecha REAL del sistema. Error recurrente: session N en Feb 18, memory escribia "Feb 19", siguiente sesion escribia "Feb 20" — todo era Feb 18.

---

## Errores de Identidad y Deployment (Session 90)

**#53. Presentar opciones en vez de decidir**
"Prefieres A o B?" cuando deberia ser "Recomiendo A porque X. Si dices no, ajusto." Anti-patron: menu de opciones, bullet points con pros/cons dejando la decision al humano. El CIO decide. El humano confirma. Ver Principio 8 y identity.md.

**#54. Standing orders irrealistas como autoengano**
SOs a -40% del precio actual con <10% probabilidad de fill no son deployment, son ficcion. Cada SO debe tener probabilidad estimada de fill en 6 meses. Si distancia >30% sin catalizador especifico → marcar como FANTASY y separar de SOs reales. 22 SOs con 0 ejecutados en 90 sesiones = el sistema fallo.

**#55. Cash drag por paralisis de analisis**
60% cash durante semanas GARANTIZA underperformance (~4.5pp/yr). Si el pipeline adversarial produce entries inalcanzables, el pipeline esta mal calibrado — no mi decision de actuar. La solucion: Expected Return como metrica de deployment (no solo MoS), modo Fair-Value acepta MoS 5-15% para Tier A. La calidad a precio razonable SIEMPRE bate al cash a 3 anos.

---

## Errores de Contexto Sectorial

**#56. R1 sin sector view fresco**
ANTES de lanzar fundamental-analyst para R1, verificar edad del sector view.
Si >21 dias: ACTUALIZAR primero. Si no existe: CREAR primero (ya cubierto por #30, #56 anade dimension de staleness). `sector_health.py freshness` es la herramienta. `r1_prioritizer.py` muestra flags STALE-SECTOR(Xd) y NO-SECTOR-VIEW automaticamente.

**#57. Basket deployment without per-stock due diligence**
Basket approval does NOT skip per-stock R1-R4. Buying 3 stocks because "the basket is approved" without per-stock thesis = repeat of Jan 26 (2→18 positions in 8 days, 8 sold). Each stock STILL needs: individual QS tool-first, kill conditions, thesis file, SM context, constraint check. Max 2 new positions per session per basket. If any basket position triggers KC within 14 days of buy → entire basket enters REVIEW.

---

## Errores de Integridad de Datos

**#61. FV in current.yaml without documented source (Ghost FV)**
EVERY fair_value field in current.yaml MUST trace to a specific document: thesis header (R1), r3_resolution.md (R3), committee_decision.md (R4), or re-eval with dated reasoning. If the FV says "R3 post-DA" but no R3 file exists, the FV is FABRICATED. This inflates E[CAGR], distorts sizing decisions, and makes the entire portfolio analytics unreliable. Origin: WKL.AS S143 — "EUR 85 R3 post-DA" had no R3 file. True FV was committee EUR 72. Position was sized based on 20.9% E[CAGR] that was actually 11.3%.
FIX: After ANY portfolio-ops write, verify: (1) FV in current.yaml matches thesis header, (2) thesis header matches last formal pipeline output (R3/R4/re-eval). If mismatch → STOP and reconcile before proceeding.

**#62. Thesis file not updated after pipeline advancement**
When R2 (DA) or R3 (resolution) or R4 (committee) changes FV, the thesis.md header MUST be updated. If thesis header still shows R1 FV but committee lowered it, forward_return.py reads the inflated R1 number. Origin: TW thesis showed $155-159 (R1) while R3 resolved to $140; WKL.AS thesis showed EUR 94.28 (R1) while committee said EUR 72.
FIX: Pipeline protocol MUST include "update thesis header" as final step of each round. The `> **Fair Value:**` line is what the parser reads — if it's wrong, everything downstream is wrong.

**#63. Market-buy protocol bypassing committee HARD GATEs**
Market-buy protocol allows buying at market price when E[CAGR] justifies. But it does NOT override committee HARD GATEs (sector view required, earnings gate, etc.). If committee said "WATCHLIST with HARD GATE on sector view" and the position is opened without creating the sector view, the committee was overruled without documentation. Origin: WKL.AS committee required sector view creation (Gate 0 FAIL) — position opened without it.
FIX: Market-buy protocol must check: "Did investment-committee set HARD GATEs? If yes, are they cleared?" If not cleared → cannot market-buy regardless of E[CAGR].

---

## Errores de Inaccion y Racionalizacion

**#58. Inaction disguised as process**
Having cash >25% for >3 sessions while universe contains candidates with E[CAGR] >12% at market price = the system is using process to avoid deployment. "Waiting for DA," "need more analysis," "entries are unrealistic" are symptoms of a system optimized to prevent commission errors while ignoring omission errors. The cost of 54% cash at 4.5pp/yr drag is HIGHER than the cost of buying a Tier A compounder at 5% below FV instead of 15% below. Fix: deploy or document WHY EVERY CANDIDATE is uninvestable. If you can't — deploy.

**#59. Rationalizing a high-conviction error**
When a high-conviction thesis fails: admit quickly, no rationalization. Update error patterns with the signal I ignored. Exit protocol if position open. NEVER retroactively move KC goalposts. Document: "What signal did I ignore? What would I do differently?"

**#60. Passing self-audits while failing objectives (audit theater)**
Cash >25% for >5 sessions while ALL Inaction Audits PASS = the audit is rubber-stamping inaction, not preventing it. The audit was designed to force deployment or document valid reasons. If cash stays high despite passing audits, the audits are finding "valid" reasons that are collectively insufficient. Fix: Cumulative Inaction Audit (Fase 2.5) requires at least ONE of: (a) deployed capital, (b) recalibrated 2+ SOs, (c) scored 3+ new candidates. Passing the session audit while failing the multi-session objective is the most sophisticated form of inaction — the system using its own safeguards as a shield against action. See P18 (Action Bias).

---

## Errores de Datos Silenciosos

**#64. Tool parser bug silently corrupting decision inputs**
Automated tools (thesis_parser.py, forward_return.py, sector_health.py) extract data from thesis files and feed it into portfolio analytics (E[CAGR], sizing, rotation). If the parser extracts WRONG data, ALL downstream decisions are corrupted — and the corruption is SILENT (no error, no warning, just wrong numbers). Origin: DOCS S145 — thesis_parser.py regex matched "Terminal Growth: 2.5%" (DCF terminal rate) instead of actual business growth 10%. This produced E[CAGR] 11.5% (wrong) vs 19.0% (correct). S143c8 TRIM of 7.15 DOCS shares was based on this incorrect E[CAGR]. The trim would have been smaller or zero with correct data. Same session: MONY.L growth fell through to yfinance -0.2% because thesis had range format "5-7%" that didn't match parser regex. Actual growth 1-2%. E[CAGR] showed 10.7% instead of 12.9%.
**WHY THIS IS THE MOST DANGEROUS ERROR CLASS:** Unlike Ghost FV (#61) or thesis staleness (#62), parser bugs produce data that LOOKS correct — the tool runs, outputs a number, the number feeds into decisions. There is no "missing data" warning. The system trusts its own tools implicitly. A human reviewing the output sees a plausible E[CAGR] and acts on it. The error only surfaces when someone manually cross-checks tool output against source data.
FIX: (1) After ANY thesis header edit, run `python3 tools/forward_return.py --active-only` and verify the growth% column matches thesis intent for the edited ticker. (2) When portfolio_cagr.py or forward_return.py shows a position with surprisingly low/high E[CAGR], cross-check the growth input — don't assume the tool is right. (3) Regex patterns in thesis_parser.py must use negative lookbehinds and specific anchoring to avoid matching similar-but-wrong fields (e.g., `(?<!Terminal )Growth`). (4) Periodic audit: compare tool-extracted growth vs thesis-stated growth for all positions (quarterly).

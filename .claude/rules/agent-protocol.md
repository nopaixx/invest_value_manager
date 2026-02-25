# Agent Protocol

> Auto-loaded. Arbol de decision + reglas criticas de agentes.
> Registro completo: `.claude/skills/agent-registry/SKILL.md`

---

## REGLA: TODOS opus. NUNCA haiku/sonnet.

---

## Arbol de Decision (OBLIGATORIO antes de cualquier tarea)

```
Que necesito?
├─ ANALIZAR empresa nueva LONG (buy-pipeline 4 rondas)
│  R1: fundamental-analyst + moat-assessor + risk-identifier (PARALELO) → valuation-specialist
│  R2: devil's-advocate
│  R3: Resolucion conflictos (si necesario)
│  R4: investment-committee (10 gates)
├─ ANALIZAR fragilidad SHORT (short-pipeline 4 rondas)
│  S1: fundamental-analyst (--short-thesis) + moat-assessor + risk-identifier (PARALELO) → valuation-specialist
│  S2: devil's-advocate (BULL case — por que precio podria tener razon?)
│  S3: Resolucion conflictos (si necesario)
│  S4: investment-committee (modo SHORT_APPROVAL — 10+3 gates)
├─ ANALIZAR BASKET (batch thematic R1-R4)
│  Basket R1: sector-view update (ONCE) + SM overlay (ONCE) + per-stock R1s (PARALLEL, max 3-4)
│  Basket R2: theme-level DA (ONCE) + per-stock DAs (PARALLEL)
│  Basket R3: theme + per-stock resolution → thesis/baskets/{id}/r3_resolution.md
│  Basket R4: 10 standard gates per stock + 3 basket gates (correlation, concentration, basket KCs)
│  SAFETY: Max 2 new positions per session per basket. All per-stock gates intact. Error #57.
├─ DESAFIAR thesis → devil's-advocate
├─ RE-EVALUAR posicion long → review-agent
├─ RE-EVALUAR posicion short → review-agent (--short-review)
├─ APROBAR compra/venta → investment-committee (OBLIGATORIO)
├─ APROBAR short/cover → investment-committee modo SHORT_APPROVAL (OBLIGATORIO)
├─ CUBRIR short → cover-protocol skill → investment-committee
├─ BUSCAR en sector → sector-screener
├─ ACTUALIZAR macro → macro-analyst
├─ SIZING → position-calculator
├─ WATCHLIST → watchlist-manager
├─ PORTFOLIO post-trade → portfolio-ops (soporta BUY/SELL/SHORT/COVER)
├─ PERFORMANCE → performance-tracker
├─ REBALANCEO → rebalancer
├─ CALENDARIO → calendar-manager
├─ HEALTH CHECK → health-check
├─ MOVER ficheros → file-system-manager
├─ MEJORAR sistema → system-evolver
└─ CREAR tool Python → quant-tools-dev
```

---

## Instrucciones v4.0 para Agentes de Decision

Al invocar fundamental-analyst, review-agent, investment-committee, incluir:

```
CONTEXTO v4.0:
- Leer learning/principles.md + learning/decisions_log.yaml
- NO limites fijos — razonar desde principios
- Razonamiento explicito. Si se desvia de precedentes, explicar por que.
- Tools = DATOS CRUDOS, no interpretar como warnings/violations
- Indicar si empresa califica Tier A (Principio 9: Quality Gravitation)
```

### Smart Money Context (v3.0 — incluir en R1 y pre-execution)

ANTES de lanzar fundamental-analyst para R1, obtener contexto smart money:

```
1. python3 tools/smart_money.py stock-profile TICKER
   → Holders, shorts, insiders, crowding, co-holdings
2. **IF non-US stock (EU/UK/CH):** Actively search for holder + insider data
   → WebSearch "[TICKER] major shareholders 2026" + "[TICKER] director dealings"
   → Capture findings: python3 tools/smart_money.py capture [results]
   → This step compensates for lack of 13F data on European stocks.
   → Skip ONLY if stock-profile already shows fresh holder data (<30 days).
3. python3 tools/smart_money.py signals --ticker TICKER
   → Actionable signals (convergence, insider cluster, short escalation)
4. Incluir resumen en prompt del agente:
   SMART MONEY CONTEXT:
   - Holders: [list from stock-profile]
   - Shorts: SI [X]% ([N] funds)
   - Insiders: [recent buys/sells]
   - Signals: [from signal engine]
   - Note: datos raw, el agente interpreta en contexto de thesis
```

---

## Verificacion Post-Agente

```
[ ] Output tiene estructura esperada?
[ ] Refleja frameworks de los skills?
[ ] Datos consistentes (FV matches inputs)?
[ ] No hay errores obvios?
[ ] Actualizo ficheros que debia? (releer y verificar)
```

Si falla → re-ejecutar con instruccion mas especifica o corregir + documentar.

---

## Propagacion de Cambios

Cuando hay cambio sistemico:
```
[ ] Que agentes leen/escriben esto? → Actualizar
[ ] Que skills definen el framework? → Actualizar
[ ] file-system-rules conoce ubicacion? [ ] health-check debe verificar?
[ ] CLAUDE.md documenta? [ ] agent-registry actualizado?
```

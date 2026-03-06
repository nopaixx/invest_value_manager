# Session Planner — Dynamic Session Plan Mode

> Auto-activar al inicio de sesion en modo DASHBOARD o WAVE.
> Genera plan de trabajo priorizado basado en estado actual del sistema.
> El CIO llega, evalua, prioriza, presenta, y tras aprobacion, ejecuta.
> **v4.8: CIO con Punch.** Three Questions FIRST (P18). Promise tracking. Basket lifecycle integrity. Action bias.

---

## Cuando se Activa

| Senal del humano | Accion |
|------------------|--------|
| Saludo generico, "trabaja", "wave", "sesion", "autonomo" | **AUTO** — generar plan, presentar, esperar aprobacion |
| "planifica la sesion" o similar | **MANUAL** — generar plan |
| Instruccion directa ("analiza X", "compra Y") | **NO SE ACTIVA** — modo DIRECTO prevalece (plan como contexto mental) |

---

## Inputs Dinamicos (10 fuentes + tools)

### Fuentes de Estado (leer)

| Fuente | Que extraer |
|--------|-------------|
| `state/calendar.yaml` | Earnings proximos 7d, catalysts, deadlines |
| `state/pipeline_tracker.yaml` | Pipelines OVERDUE y DUE TODAY |
| `state/standing_orders.yaml` | SOs near trigger (<10% distancia) |
| `state/watchlist.yaml` | Price alerts, short candidates |
| `state/system.yaml` | Market regime, last session summary, strategic direction |
| `portfolio/current.yaml` | Positions on probation, pending reviews, conviction levels |
| `state/quality_universe.yaml` | SCORED count, stale count, pipeline funnel |
| `state/session_continuity.yaml` | Prior session work, dedup signals, R1 cooldowns, handoff |
| `state/evolution_state.yaml` | Trigger red_count (14 triggers), scheduled reviews due, active experiments |

### Tools Rapidos (ejecutar)

| Tool | Que extraer |
|------|-------------|
| `python3 tools/portfolio_cagr.py` | **P1 DEPLOYMENT**: Portfolio E[CAGR], cash drag, market buy candidates, rotation candidates |
| `python3 tools/forward_return.py --active-only` | Bottom 3 posiciones, rotation candidates, E[CAGR] column |
| `python3 tools/forward_return.py --pipeline-only --deployment-ready` | Pipeline candidates viable for deployment at current prices |
| `python3 tools/sector_health.py freshness --stale-only` | Sectores stale con dependencias de portfolio |
| `python3 tools/r1_prioritizer.py --buyable-now` | Reverse pipeline: what's buyable at market TODAY |
| `python3 tools/r1_prioritizer.py --advancement` | R1_COMPLETE advancement: 3 sections (Ready/Approaching/Parked) + E[CAGR]@mkt |
| `python3 tools/quality_universe.py approaching` | Pipeline entries moving toward entry since last refresh |
| `python3 tools/outcome_tracker.py` | Buy decision outcomes: P&L, win rate, calibration |
| `python3 tools/basket_dashboard.py --health` | **P17 BASKET HEALTH**: theme vitality, allocation, orphan positions, basket pipeline |

---

## Logica de Priorizacion (9 niveles)

| P# | Condicion | Bloque | Ejemplo |
|----|-----------|--------|---------|
| P0 | Kill condition / CRITICAL news alert | URGENTE | Fraude detectado en posicion |
| P1 | **DEPLOYMENT: `portfolio_cagr.py` → market buy candidates → rotation candidates** | URGENTE | Cash 56%, 3 candidates E[CAGR]>15% |
| P1b | **INACTION AUDIT (auto-trigger if cash >25%): top 3 by E[CAGR], specific reason each NOT bought, classify VALID/INVALID** | URGENTE | Cash 54.6%, HLNE not bought = Error #58 |
| P1c | **BASKET HEALTH (P17): any basket with declining theme, orphan positions, or basket KC approaching** | URGENTE | Pharma basket theme declining, 2 orphan positions |
| P2 | Earnings <7d sin framework (posicion activa) | URGENTE | MONY.L FY results Monday |
| P3 | SO triggered o near (<5%) | URGENTE | RACE.MI at 5.3% de entry |
| P4 | R1 processing for BUYABLE candidates — **FAVOR candidates that fill underfunded baskets** (obligatorio 3 velocity units/sesion) | PRIORIDAD NORMAL | Top 5 de r1_prioritizer --buyable-now |
| P1d | **THEME DISCOVERY ESCALATION (v4.8): cash >25% AND baskets <4 active = URGENTE, not P4b** | URGENTE | Cash 40%, only 3 active baskets |
| P4b | **THEME DISCOVERY (P17, weekly or cash >15%): scan for emerging mega-trends, propose basket birth/death** | PRIORIDAD NORMAL | AI infrastructure theme identified, 4 candidates |
| P5 | Position reviews (ongoing health) | PRIORIDAD NORMAL | LULU probation review |
| P6 | Pipelines OVERDUE | PRIORIDAD NORMAL | risk-review 3d overdue |
| P7 | Sector stale con portfolio deps | PRIORIDAD NORMAL | telecom.md 45d old, DTE.DE dep |
| P8 | System maintenance, universe expansion, health check | MANTENIMIENTO | batch_scorer new index |
| P8c | **Cash audit: if cash >10%, WHY? Document or deploy.** | MANTENIMIENTO | Cash 15% sin justificacion |
| P8e | **Evolution: update triggers, process reviews, propose if RED.** If `red_count >= 4` → **URGENTE**. | MANTENIMIENTO (or URGENTE) | 6 RED triggers, exp_001 review due |

**Reglas de clasificacion:**
- P0-P3 → bloque URGENTE (hacer PRIMERO, antes de cualquier wave)
- P1 DEPLOYMENT is now URGENTE, not normal — every session starts with "what can I buy or rotate NOW?"
- **P1b INACTION AUDIT fires AUTOMATICALLY when cash >25%.** Not optional. Not maintenance. URGENTE. Output: "Inaction Audit: [PASS/FAIL]. Cash [X]%. Top 3 not bought because: [reasons]"
- P4-P7 → bloque PRIORIDAD NORMAL (bulk del trabajo de la sesion)
- P8 → bloque MANTENIMIENTO (si queda contexto)
- P8e → Evolution micro-step (SIEMPRE al final — Fase 6)
- P8c → Cash audit (if cash >10%) — mandatory justification
- R1 processing (P4) focuses on BUYABLE candidates first (--buyable-now), FAVORING candidates that fill underfunded baskets
- Net exposure reasoning SIEMPRE aparece — es obligatorio cada sesion (P13)
- Rotation check SIEMPRE aparece — es obligatorio cada sesion (P16)
- **Basket health check SIEMPRE aparece — es obligatorio cada sesion (P17)**
- **Theme discovery (P4b) fires weekly, or when cash >15%, or when any basket is in DECLINE status**

---

## Dedup Logic (via `state/session_continuity.yaml`)

### Same-Day Dedup
Read `session_continuity.yaml` → `session.date` and `skip_if_same_day`:
- Si `session.date == today` Y `vigilance_fresh_until > now` → **SKIP vigilancia**. Mostrar: "News fresh from S[N]. Skipping."
- Si `so_fresh_until > now` → **SKIP SO price check**. Mostrar cached `nearest`.
- Si `rotation_done_today == true` → **SKIP rotation check**. Mostrar: "Rotation done S[N]."

### R1 Dedup
- `r1_prioritizer.py --top 10` already filters cooldowns (reads `session_continuity.yaml` → `r1_cooldowns`)
- Cross-check output vs `completed.r1_completed` to avoid same-session re-analysis

### Handoff
- Incorporate `next_priorities` from previous session as context for P3-P7 classification
- If previous session flagged an evolution proposal with `Apply: NOW`, include as P8e item

---

## Template del Plan

```markdown
## SESSION PLAN — Sesion [N] | [Fecha]

### THREE QUESTIONS (P18 — Fase 0.ZERO)
- **Q1 (Deploy)**: [concrete action to reduce cash toward <10%]
- **Q2 (Baskets)**: [concrete action to fill baskets with <2 positions]
- **Q3 (Proactive)**: [something I'm doing without being asked]
- Promise audit: [N]/[M] promises from last session KEPT. Broken: [list or "none"]

### ESTADO RAPIDO
- Portfolio: [N] posiciones, EUR [X] invested, cash [Y]%
- Market Regime: [Opportunity/Fair-Value/Defensive] — [razonamiento 1 linea]
- P&L: [+/-X.X]%
- Probation: [tickers o "ninguno"]
- Pipeline: [N] SCORED sin R1, [N] near-entry, [N] deployment-ready (E[CAGR]>=threshold)
- Fantasy rate: [X]% ([N]/[M] R1s → OVERVALUED/FANTASY)
- Advancement: Section A [N] ready, [N] approaching

### BASKET HEALTH (P17 — obligatorio)
- Active baskets: [N] | Positions assigned: [N]/[total] | Orphans: [tickers]
- Per basket: [basket-name] [N] positions, E[CAGR] [X]%, theme [ALIVE/DECLINING/DEAD], conviction [HIGH/MED/LOW]
- Basket pipeline: [N] candidates across [N] baskets
- Theme discovery: [last done X days ago / DUE]
- Action needed: [basket births/deaths/rebalancing or "healthy"]

### INACTION AUDIT (auto si cash >25%)
- Cash: [X]% | Top 3: [T1] E[CAGR] [X]% (reason: [VALID/INVALID]), [T2]..., [T3]...
- Verdict: [PASS/FAIL]

### URGENTE (hacer PRIMERO)
1. [P#] [Descripcion] — agentes: [lista] — ~[X]m
2. ...
(Si no hay items urgentes: "Sin urgencias detectadas.")

### PRIORIDAD NORMAL
1. [P#] [Descripcion] — agentes: [lista] — ~[X]m
2. [P4] R1 Processing: [N] candidatos ([tickers]) — fundamental-analyst x[N] paralelo — ~[X]m
3. [P13] Net Exposure Reasoning — macro_fragility + razonamiento — ~5m
...

### MANTENIMIENTO (si queda contexto)
1. [P8] [Descripcion] — ~[X]m
2. [P8e] Evolution micro-step (Fase 6) — ~5m
(Si no hay items: "Sistema saludable.")

### DEDUP APLICADO
- Vigilancia: [FRESH S{N} / DUE]
- SOs: [FRESH S{N} / DUE]
- Rotation: [DONE S{N} / DUE]
- R1 cooldowns: [N] filtered ([tickers])
- Handoff S{N}: [resumen de next_priorities]

### SECUENCIACION
- Wave 1: [items paralelos] — ~[X]m
- Wave 2: [items paralelos, post-Wave-1] — ~[X]m
- Wave 3: [items paralelos, post-Wave-2] — ~[X]m
Total estimado: ~[X]m
```

---

## Restricciones del Plan

1. **Max 4-5 heavy opus agents en paralelo** por wave (7 causa context overflow)
2. **Max 2 yfinance agents simultaneos** (rate limiting)
3. **R1 minimum 3 velocity units/sesion** (L-08) — SIEMPRE en el plan
4. **Net exposure reasoning** obligatorio (P13) — SIEMPRE en el plan
5. **Earnings prep antes de R1** — si hay earnings <7d, va en URGENTE antes de R1 wave
6. **Tools rapidos primero** — los 4 tools de input se ejecutan ANTES de generar el plan
7. **Tiempo realista** — no prometer mas de lo que cabe en contexto (~3-4 waves max)
8. **ANTI-FANTASY PROTOCOL (S105, tooling-enforced S106):**
   - Run `--advancement` FIRST: shows 3 sections (Ready/Approaching/Parked) with E[CAGR]@market
   - If Section A non-empty → prioritize R2→R3 (2 units each)
   - If 0 in Section A → new R1s, but use `--exclude-fantasy-risk` or `--pre-flight` to filter
   - `--pre-flight` shows ONLY candidates with E[CAGR]-at-entry >= threshold (12% Tier A, 15% Tier B)
   - `--exclude-fantasy-risk` filters out companies priced >150% of FV (guaranteed FANTASY R1)
   - **Fantasy rate** now auto-computed in footer. If >50% → system alarm with suggestions
   - R1 candidates MUST be on eToro (check ETORO_UNAVAILABLE in r1_prioritizer.py)
   - Use `quality_universe.py approaching` to catch stocks dropping toward entry between sessions
9. **EARNINGS AUTO-PREP GATE (S105):**
   - For ANY position with earnings <7 days: verify framework exists AND freshness <14 days
   - If framework missing → P1 URGENTE
   - If framework >14 days old → P1 refresh required before earnings

---

## Flujo de Ejecucion

```
1. Leer 7 fuentes de estado (archivos)
2. Ejecutar 3 tools rapidos (forward_return, sector_health, r1_prioritizer)
3. Clasificar items por P0-P8
4. Generar plan con template
5. Presentar plan al humano (plan mode)
6. Humano aprueba / ajusta
7. Ejecutar waves secuencialmente
```

### En Modo DIRECTO

Si el humano da instruccion directa, NO entrar en plan mode formal. Pero:
- Generar plan mental como contexto interno (que mas hay pendiente?)
- Ejecutar la instruccion directa como Wave 1
- Si queda contexto tras la instruccion, proponer siguiente accion basada en prioridades

---

## Lesson Trigger Table (checked during plan generation)

During plan generation, scan these conditions and surface the matching lesson:

| Condition | Lesson | Where to Surface |
|-----------|--------|-----------------|
| `cash > 40%` | L-01: Cash drag | P1 URGENTE |
| `>5 SOs at >25% distance` | L-02: SOs autoengano | SO reality check item |
| `DA adjusts FV >20% → entry unreachable` | L-03: Pipeline letal | Post-R2 resolution |
| `Output contains option menu` | L-04: Cobardia intelectual | Self-check before presenting |
| `No deployment in 3+ sessions AND cash >20%` | L-05: Esperar crash | P1 URGENTE |
| `Evaluating Tier A with MoS <15%` | L-06: Calidad bate cash | Investment committee context |
| `>5 new files created in session` | L-07: Complejidad ≠ calidad | P8 maintenance |
| `velocity_units <3 at session end` | L-08: Velocity cuello botella | Fase 6 reflection |
| `R1_COMPLETE >20 AND <3 ACTIONABLE` | L-09: Advancement > volume | Pipeline decision (P4) |
| `cash >10% for >2 sessions` | L-10: Full deployment mandate | P1 EMERGENCY |
| `cash >25%` | **INACTION AUDIT (Error #58)**: Top 3 E[CAGR], why not bought, VALID/INVALID | P1b URGENTE (auto-fire) |
| `>2 orphan positions (no basket)` | **L-11: Orphan positions = structural gap.** Assign to existing basket or form new one | P1c basket health |
| `any basket theme DECLINING` | **L-12: Dying theme = capital trap.** Evaluate basket death, redeploy to live themes | P1c basket health URGENTE |
| `theme discovery >7 days stale` | **L-13: Discovery stops = fund dies.** Scan for emerging mega-trends | P4b theme discovery |
| `basket count < 3` | **L-14: Insufficient diversification.** Need at least 3 live themes for structural resilience | P4b theme discovery |
| `cash >25% for >5 sessions AND all Inaction Audits PASS` | **L-15: Audit theater.** Self-audits passing while objectives failing. Cumulative Inaction Audit override: must deploy, recalibrate SOs, or score new candidates. See Error #60 and P18. | P1b URGENTE |
| `cash >25% AND baskets <4 ACTIVE` | **Theme Discovery ESCALATION**: cash high + insufficient basket coverage = structural deployment failure. Escalate theme discovery from P4b to P1d URGENTE. Dedicate 1 wave. | P1d URGENTE |

**How to use:** After reading 9 state sources and running tools, scan this table. If condition matches, add the lesson reference to the relevant plan section. Format: `[L-XX] {lesson name} — {action}`

---

## Evolution Session Plan Template

**When to activate full evolution session:**
- Monthly: 1st session of each month
- RED override: `evolution_state.yaml` → `trigger_summary.red_count >= 4`
- Human says: "evolve", "mejora el sistema", "self-improve"
- Scheduled review due: `evolution_state.yaml` → `scheduled_reviews[]` with `due_session <= current`

```markdown
## EVOLUTION SESSION PLAN — Session [N] | [Date]

### TRIGGER STATUS
- Red: [N]/10 — [list RED triggers]
- Experiments measuring: [N] — [list]
- Reviews due: [list or "none"]

### EVOLUTION ITEMS (P8e → URGENTE if red_count >= 4)
1. [Review exp_NNN] Measure [metric] vs baseline. Verdict: [POSITIVE/NEGATIVE/NEUTRAL]
2. [Fix T{N}] {trigger name} — Proposed change: [description]
3. [Backfill] Measure effectiveness of [evo_NNN] from changelog

### REGULAR SESSION ITEMS
[Standard URGENTE / PRIORIDAD NORMAL / MANTENIMIENTO blocks]

### EVOLUTION CLOSE
- Updated evolution_state.yaml triggers: [list changes]
- New experiments: [list or "none"]
- Next review due: S[N+5]
```

---

## NO Hacer

- NO presentar el plan como menu de opciones — es MI recomendacion de trabajo
- NO esperar aprobacion item por item — el plan se aprueba en bloque
- NO incluir mas de 3-4 waves — ser realista con el contexto disponible
- NO ejecutar antes de aprobacion (excepto modo DIRECTO)
- NO incluir items que requieren confirmacion del humano como "trabajo autonomo" — earnings prep si, BUY execution no

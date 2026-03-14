# Pre-Execution Check (Pre-Flight Protocol)

## Principio

Una standing order es una **decision pre-aprobada**, pero el mundo cambia entre la aprobacion y el trigger.
Antes de recomendar ejecucion, SIEMPRE hacer pre-flight check.

---

## Cuando se activa

**Fase 0 de cada sesion** — obligatorio, antes de cualquier otra cosa.

```
1. Chequear precios de TODAS las standing orders (LONG y SHORT)
2. Clasificar cada una:
   LONGS:
   - TRIGGERED: precio <= trigger
   - NEAR: precio acercandose al trigger (razonar sobre contexto)
   - FAR: claramente lejos del trigger
   SHORTS:
   - TRIGGERED: precio >= trigger (shorts se activan cuando el precio SUBE)
   - NEAR: precio acercandose al trigger por arriba
   - FAR: claramente lejos del trigger
3. Para TRIGGERED y NEAR: ejecutar pre-flight
```

---

## THE QUESTION (before any gate runs)

> **"Would I buy this stock TODAY, from zero, with EVERYTHING I know right now?"**

This is NOT a gate. It's a mindset. Gates check boxes. This question forces you to
THINK. If BZU.MI's SO triggered on Mar 13 and you asked this question — cement
company, 30-40% energy cost, oil at $100, Hormuz closed, war day 13 — the answer
is obviously NO. No gate needed. Just honest thinking.

If the answer is NO or HESITANT: **stop**. Do not proceed to gates. The SO is stale
regardless of what the gates say. Re-evaluate the thesis in current context first.

If the answer is YES with conviction: proceed to gates for systematic verification.

Origin: S172 post-mortem. BZU.MI bought Mar 13 (oil $100), sell recommended Mar 14.
The 8 gates all passed because none asked this simple question.

---

## Pre-Flight Checklist (8 gates)

Para cada standing order TRIGGERED o NEAR:

### Gate 1: NEWS CHECK
```
[ ] Buscar noticias del ticker desde la fecha de creacion de la order
[ ] Clasificar: COSMETIC / MINOR / MATERIAL / CRITICAL
[ ] Si MATERIAL o CRITICAL → STOP, re-evaluar antes de ejecutar
[ ] Para SHORTS: noticias POSITIVAS sobre la empresa = alerta (posicion va en contra)
```

### Gate 2: HARD GATES CHECK
```
[ ] Leer campo hard_gates de la standing order (si existe)
[ ] Verificar cada gate:
    - Ejemplo V: DOJ no structural, CCCA no floor vote, rev>=8%, incentives<48%
    - Ejemplo MORN: CRSP thesis update written?
[ ] Si CUALQUIER gate ROJO → NO EJECUTAR
```

### Gate 3: KILL CONDITIONS CHECK
```
[ ] Leer kill conditions de la thesis
[ ] Verificar si alguna se ha activado desde la creacion de la order
[ ] Si KC activada → NO EJECUTAR, presentar evidencia
```

### Gate 4: PORTFOLIO CONSTRAINTS
```
[ ] Para LONGS: python3 tools/constraint_checker.py CHECK TICKER AMOUNT
[ ] Para SHORTS: python3 tools/constraint_checker.py CHECK_SHORT TICKER AMOUNT
[ ] Verificar concentracion sector, geo, posicion individual
[ ] Para SHORTS: verificar net exposure, carry cost proyectado
[ ] Si constraint violation → ajustar sizing o NO EJECUTAR
```

### Gate 5: THESIS VALIDITY
```
[ ] Leer thesis brevemente
[ ] ¿Las asunciones clave siguen siendo ciertas?
[ ] ¿Ha habido earnings entre creacion y ahora? ¿Resultado?
[ ] ¿El QS ha cambiado materialmente?
[ ] Ejecutar: python3 tools/dcf_calculator.py --reverse TICKER
    → ¿El gap entre implicito e historico sigue existiendo?
    → Para LONGS: ¿mercado sigue infravalorando?
    → Para SHORTS: ¿mercado sigue sobrevalorando?
[ ] Verificar last_analysis_date: cuanto mas viejo el analisis, mas importante revalidar
[ ] Si thesis debilitada → NO EJECUTAR, re-evaluar
```

### Gate 6: CAPITAL ALLOCATION (Principios 4 + 9)
```
[ ] ¿Es este el mejor uso de este capital HOY? (Principio 9: Calidad Gravita)
[ ] ¿Hay alternativa de mayor calidad con mejor retorno esperado disponible?
[ ] ¿Cual sera el nivel de cash resultante? ¿Es coherente con el contexto? (Principio 4)
[ ] ¿Tengo pipeline de ideas que necesite reserva de capital?
[ ] Si mejor alternativa existe → ESPERA o REDIRIGE capital
```

### Gate 7: MACRO REGIME CHECK (Error #67 — added S172 post-BZU.MI)
```
[ ] How many days since R4 approval? If >7 days → mandatory macro re-validation
[ ] Run: macro_fragility.py world → compare key indicators vs R4 date
    - Oil: if moved >15% since R4 → check stock's energy sensitivity
    - VIX: if moved >10pts since R4 → check stock's beta/cyclicality
    - 10Y: if moved >50bps since R4 → check stock's rate sensitivity
    - S&P: if moved >5% since R4 → check if correction changes thesis
[ ] Does the stock's sector have DIRECT exposure to the dominant macro event?
    - Energy-intensive + oil crisis → BLOCK
    - Rate-sensitive + rate spike → FLAG
    - Consumer-cyclical + recession → FLAG
[ ] If macro regime changed materially since R4:
    → Re-run investment-committee with updated macro context
    → Do NOT execute stale R4 approval in a new macro regime
[ ] If macro regime unchanged: PASS
```

### Gate 8: SMART MONEY CONTEXT
```
[ ] Run: python3 tools/smart_money.py stock-profile TICKER
[ ] Run: python3 tools/smart_money.py signals --ticker TICKER
[ ] If SI increased >2x since thesis → FLAG for re-eval before execution
[ ] If quality fund EXITED since thesis → FLAG for re-eval before execution
[ ] If insider cluster buy appeared → BOOST confidence (note in presentation)
[ ] If new short >1% appeared → NOTE but don't block
[ ] If SHORT_ESCALATION signal → extra caution, verify thesis assumptions
```

---

## Verdicts

No hay formula mecanica. Razonar sobre la severidad de cada gate:

- **Todos los gates verdes**: Presentar recomendacion al humano con contexto completo
- **Un gate ambiguo** (ej: noticia menor, constraint cerca del limite): Razonar sobre la materialidad. ¿Cambia la tesis? ¿El riesgo es diferente? Presentar con nota explicativa.
- **Gate critico falla** (KC activada, thesis debilitada, hard gate rojo): NO EJECUTAR. Explicar que fallo y que se necesita antes de proceder.
- **Mejor alternativa disponible** (Gate 6): Recomendar redireccion de capital si hay opcion superior con razonamiento explicito.

**Principio 7**: Si la decision es diferente a precedentes similares, documentar POR QUE.

---

## Template de Presentacion al Humano

```
STANDING ORDER TRIGGERED: [TICKER] at $[PRICE] (trigger $[TRIGGER])

PRE-FLIGHT:
  [x] News: Nada material desde [fecha orden]
  [x] Hard Gates: N/A (o: 4/4 verdes)
  [x] Kill Conditions: 0 activadas
  [x] Constraints: OK (sector X%, geo Y%, position Z%)
  [x] Thesis: Intacta

RECOMENDACION: EJECUTA [SHARES] shares a ~$[PRICE]
  Sizing: EUR [AMOUNT] ([X]% del portfolio)
  MoS actual: [X]% (vs [Y]% cuando se creo la order)

¿Confirmas? → Ejecuta en eToro
```

---

## NEAR Triggers

Para orders que se acercan al trigger (razonar sobre que es "cerca" segun contexto:
alta volatilidad = mas margen, earnings inminentes = mas margen, caida rapida = mas atencion):

```
ALERTA: [TICKER] a $[PRICE], trigger $[TRIGGER], [X]% away
  - Pre-flight preparado: [PASS/ISSUES]
  - Si toca manana: listo para ejecutar / necesita [X] primero
  - Considerar: abrir sesion diaria mientras este near
```

---

## Frecuencia de Sesiones Recomendada

| Situacion | Frecuencia |
|-----------|------------|
| Nada near trigger | Cada 2-3 dias |
| 1+ order within 5% | **Diaria** |
| Earnings week (posiciones) | **Diaria** |
| Crisis / crash | **Multiples al dia** |
| Mercado tranquilo, nada near | Semanal OK |

---

## Integracion con Session Protocol

Este skill se ejecuta en **Fase 0** (Calibracion), ANTES de vigilancia:

```
FASE 0: Calibracion v4.0
  → Leer principles.md + precedentes
  → **PRE-EXECUTION CHECK** ← AQUI
  → Self-check: listo para razonar
```

Si hay un TRIGGERED, se convierte en **prioridad maxima** de la sesion.

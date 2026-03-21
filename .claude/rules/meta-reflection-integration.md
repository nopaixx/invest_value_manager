# Meta-Reflection Integration Protocol

> Auto-loaded. Cuando un agente termina, ANTES de usar su output, seguir este checklist.

---

## Checklist Post-Agente (OBLIGATORIO)

```
[ ] Buscar seccion META-REFLECTION en output del agente
[ ] Si tiene DUDAS → Resolverlas antes de actuar. Si son criticas, investigar.
[ ] Si tiene SUGERENCIAS → Implementar ahora si son validas, o documentar por que no.
[ ] Si tiene ANOMALIAS → STOP. Investigar antes de continuar. Puede cambiar la decision.
[ ] Si tiene PREGUNTAS → Responder explicitamente (aunque sea para mi mismo).
[ ] **TRACKER: Añadir CADA item a state/meta_reflection_tracker.yaml** (S275)
```

## Reglas Duras

1. **NUNCA IGNORAR META-REFLECTION.** Es informacion de un especialista que puede ver algo que yo no.
2. **Implementar mejoras validas INMEDIATAMENTE.** No diferir a "luego".
3. **Investigar anomalias ANTES de actuar.** Solo continuar cuando se resuelva.
4. **Si el agente no incluye META-REFLECTION** → Nota para mejorar su prompt.
5. **TRACKER OBLIGATORIO (S275):** Cada item va a `state/meta_reflection_tracker.yaml`. Items OPEN hasta resueltos con evidencia. Weekly audit domingos. Si >20 OPEN, pipeline PAUSE hasta <10.
6. **ANOMALY items bloquean pipeline advancement** para ese ticker hasta investigados.
7. **SUGGESTION items prioridad HIGH** se implementan en 7 dias o se documenta por que no.
8. **Auditoria:** `python3 tools/meta_compliance.py` — humano verifica sin preguntar. Score <60 = pipeline PAUSE.
9. **Resolucion:** AGENTES investigan y resuelven. Script solo AUDITA. Orchestrador ASIGNA items a agentes.

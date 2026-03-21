# Meta-Reflection Rules (S275)
# Complementa .claude/rules/meta-reflection-integration.md
# Estas reglas son VINCULANTES — aprobadas por el humano S275

## Reglas Nuevas (5-9)

5. **TRACKER OBLIGATORIO:** Cada item de meta-reflection va a `state/meta_reflection_tracker.yaml`. Items OPEN hasta resueltos con evidencia. Weekly audit domingos. Si >20 OPEN, pipeline PAUSE hasta <10.

6. **ANOMALY items bloquean pipeline advancement** para ese ticker hasta investigados.

7. **SUGGESTION items prioridad HIGH** se implementan en 7 dias o se documenta por que no.

8. **Auditoria:** `python3 tools/meta_compliance.py` — humano verifica sin preguntar. Score <60 = pipeline PAUSE.

9. **Resolucion:** AGENTES investigan y resuelven items. Script solo AUDITA. Orchestrador ASIGNA items a agentes para resolver.

## Baseline
- Score inicial: 53/100 (2026-03-21)
- Items: 18 (14 OPEN, 4 RESOLVED)
- No backfill — score sube orgánicamente

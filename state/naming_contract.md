# Naming Contract — Thesis File Standards (S276)
# Aprobado por humano. VINCULANTE para todos los agentes.
# Complementa .claude/rules/agent-protocol.md

## 7 Nombres Canónicos (ÚNICOS permitidos)

| Stage | Filename EXACTO | Agente que lo escribe |
|-------|----------------|----------------------|
| R1 | `thesis.md` | fundamental-analyst |
| R1 | `moat_assessment.md` | moat-assessor |
| R1 | `risk_assessment.md` | risk-identifier |
| R2 | `devils_advocate.md` | devils-advocate |
| R3 | `r3_resolution.md` | orchestrador (CIO) |
| R4 | `committee_decision.md` | investment-committee |
| Opt | `earnings_framework.md` | fundamental-analyst |

## Nombres PROHIBIDOS (legacy, no crear nuevos)

- ~~counter_analysis.md~~ → usa `devils_advocate.md`
- ~~r2_devils_advocate.md~~ → usa `devils_advocate.md`
- ~~da_analysis.md~~ → usa `devils_advocate.md`
- ~~adversarial_thesis_review.md~~ → usa `devils_advocate.md`
- ~~r2_bear_case.md~~ → usa `devils_advocate.md`
- ~~fundamental_analysis.md~~ → usa `thesis.md`
- ~~r1_thesis.md~~ → usa `thesis.md`
- ~~valuation_report.md~~ → usa `thesis.md`

## Enforcement

1. **En CADA prompt de agente:** incluir línea exacta
   `OUTPUT: Write to thesis/research/{TICKER}/{filename_exacto}`
2. **Post-agente checklist:** Verificar filename. Si no canónico → RENAME inmediatamente.
3. **meta_compliance.py:** Solo cuenta ficheros con nombres canónicos para coverage.
4. **Ficheros legacy:** Se migran en batch de limpieza. No bloquean pipeline.

## Estructura completa de thesis/research/{TICKER}/

```
thesis/research/TICKER/
├── thesis.md              ← R1 (obligatorio)
├── moat_assessment.md     ← R1 (full pipeline only)
├── risk_assessment.md     ← R1 (full pipeline only)
├── devils_advocate.md     ← R2 (obligatorio pre-R3)
├── r3_resolution.md       ← R3 (obligatorio pre-R4)
├── committee_decision.md  ← R4 (obligatorio pre-SO)
└── earnings_framework.md  ← Opcional (pre-earnings)
```

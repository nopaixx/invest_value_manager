---
name: evolution-protocol
description: Closed-loop system self-improvement. Detect → Propose → Apply → Measure → Validate.
user-invocable: false
disable-model-invocation: false
---

# Evolution Protocol — Closed-Loop Self-Improvement

> System version: v4.6. Last rewrite: Session 108 (2026-02-20).
> Single source of truth for triggers: `state/evolution_state.yaml`
> Changelog archive: `evolution/changelog.yaml`

---

## The Loop

```
DETECT (triggers fire) → PROPOSE (specific change) → APPLY (backup + implement)
        ↑                                                      ↓
        ←── MEASURE (+5 sessions) ←── VALIDATE (+30 sessions) ←┘
                    ↓ if NEGATIVE
                  REVERT or ADJUST
```

**Every evolution follows this loop. No exceptions. No `effectiveness: null` forever.**

---

## Integration Points

### Fase 0.0b — Meta-Consciousness Check (start of session)
1. Read `state/evolution_state.yaml` → `trigger_summary.red_count`
2. If `red_count >= 4` → flag P8e as URGENTE in session plan
3. Check `scheduled_reviews[]` → any `due_session <= current_session`? Add to plan.
4. Quick self-check: "Am I coasting on process?"

### Fase 6 — Evolution Micro-Step (end of session)
1. **Update 10 trigger metrics** with data from this session
2. Recalculate `trigger_summary` (red/yellow/green counts)
3. **Process any due scheduled_reviews** → measure experiment, update verdict
4. If any trigger RED → propose 1 micro-improvement (What/Why/How/Measure/Apply)
5. Register in `evolution_log[]` (keep last 10; older → changelog.yaml)
6. If experiment applied this session → add to `active_experiments[]` + `scheduled_reviews[]`

---

## What Can Be Modified

| Target | Confirmation Required |
|--------|----------------------|
| Skills (.claude/skills/) | Auto (minor) / User (major logic change) |
| Rules (.claude/rules/) | User |
| CLAUDE.md | User |
| State files (state/) | Auto |
| Learning files (learning/) | Auto (minor) / User (principles.md) |
| Tools (tools/) | User |
| Memory files (memory/) | Auto |

**What CANNOT be modified:** settings.json, portfolio/current.yaml (only after human confirms trade).

---

## Experiment Lifecycle

### 1. PROPOSE
- Specific change with hypothesis: "If I do X, metric Y will improve from A to B"
- Identify which trigger(s) it addresses
- Define measure_metric and review_due_session (current + 5)

### 2. APPLY
- Backup modified files in `evolution/backups/{date}-{name}/`
- Implement the change
- Register in `evolution/changelog.yaml` with full entry
- Add to `evolution_state.yaml` → `active_experiments[]`
- Add review to `scheduled_reviews[]`

### 3. MEASURE (+5 sessions)
- At review_due_session: compare current metric vs baseline
- Update experiment `current` field with measured values
- Preliminary verdict: POSITIVE / NEUTRAL / NEGATIVE / INSUFFICIENT_DATA
- If NEGATIVE → propose REVERT or ADJUST, don't wait for deep review
- If INSUFFICIENT_DATA → extend review by 5 sessions (max 1 extension)

### 4. VALIDATE (+30 sessions)
- At deep_review_session: final assessment
- Update `verdict`: VALIDATED / REVERTED / ADJUSTED
- If VALIDATED → update changelog `effectiveness: positive`
- If REVERTED → restore from backup, update changelog `effectiveness: negative`, document why
- If ADJUSTED → document what changed and why, reset measurement cycle
- Archive from `active_experiments[]` to `evolution_log[]`

---

## Changelog Format (evolution/changelog.yaml)

```yaml
- id: evo_NNN
  date: YYYY-MM-DD
  session: NNN
  type: improvement | bugfix | new_feature | removal
  description: "What changed and why"
  files_changed: [list]
  approved_by: user | auto
  experiment_id: exp_NNN  # links to active_experiments
  hypothesis: "If X then Y"
  measure_metric: "T1_fantasy_rate"
  review_due: session_NNN
  effectiveness: null | positive | neutral | negative
  evaluation_date: null | YYYY-MM-DD
  evaluation_notes: null | "What happened"
  reversible: true
  backup_file: "evolution/backups/..."
```

---

## 10 Triggers Quick Reference

| # | Metric | Red | Where Checked |
|---|--------|-----|---------------|
| T1 | R1 Fantasy Rate | >65% | Fase 6, r1_prioritizer footer |
| T2 | Cash % sustained | >40% for 3+ sessions | Session planner P1, Fase 6 |
| T3 | Pipeline Velocity | <1.5 units/session avg | Fase 6 |
| T4 | Error Recurrence | Same error 3x/10 sessions | Fase 6 |
| T5 | Sessions Since Evolution | >5 | Fase 0.0b, Fase 6 |
| T6 | Lessons Cited | 0 in 10 sessions | Fase 6, decisions |
| T7 | Meta-Reflections Processed | <50% | Fase 6 |
| T8 | SO Fill Rate | <5% lifetime | Fase 6 |
| T9 | Changelog Measured | <30% | Fase 6 |
| T10 | Plan Adherence | <50% | Fase 6 |

---

## Self-Reference

This protocol can evolve itself. If T5 (sessions since evolution) fires RED, this protocol is a valid target for improvement. The system improves the system that improves the system.

---

## Security

- Backup ALWAYS before modifying
- Minor changes (typos, metric updates, formatting): auto
- Major changes (logic, new capability, principle modification): require user confirmation
- Everything reversible with backup

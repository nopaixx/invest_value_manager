---
name: rapid-triage
description: "Level 1 rapid triage for pipeline candidates. Quick FV + entry + verdict in ~10 min per company. Pre-filter before full R1."
user-invocable: false
disable-model-invocation: false
---

# Rapid Triage (Level 1 Pipeline)

## Purpose
Quick assessment of universe candidates to determine if they warrant a full R1. This is a PRE-FILTER, not a replacement for R1. Goal: process 4-6 companies per session vs 2-3 full R1s.

## When to Use
- Universe candidates with QS >= 65 that have NO FV calculated yet
- Before committing 45-60 min to a full R1 with 3-4 parallel agents
- During SPRINT sessions focused on pipeline velocity

## Triage Agent Prompt Template

```
RAPID TRIAGE — {TICKER}

You are performing a RAPID triage assessment (Level 1). This is NOT a full R1.
Target: 10 minutes. Be concise but accurate.

INPUTS:
- Ticker: {TICKER}
- QS (from batch_scorer): {QS} / Tier {TIER}
- Sector: {SECTOR}
- Current price: {PRICE} {CURRENCY}
- Sector view: {SECTOR_VIEW_EXISTS? YES/NO}

TASKS (in order):
1. BUSINESS MODEL (2 paragraphs max)
   - What does the company DO? Revenue model. Key customers.
   - What's the MOAT? (1 sentence: wide/narrow/none + why)

2. QUICK FINANCIALS (use narrative_checker.py output if available)
   - Revenue CAGR 3yr
   - EBIT margin trend
   - ROIC vs WACC (directional)
   - FCF conversion
   - Debt/EBITDA

3. VALUATION (2 methods, be quick)
   - Method 1: EV/EBIT or P/E with peer comparison → implied FV
   - Method 2: Reverse DCF → what growth is priced in?
   - Weight → single FV estimate
   - Entry price = FV * (1 - MoS for tier)
     Tier A: 10-15% MoS → entry ~85-90% of FV
     Tier B: 20-25% MoS → entry ~75-80% of FV

4. VERDICT (one of):
   - ACTIONABLE: Price <= entry. Ready for full R1.
   - AT_FV: Price within 15% above entry. Worth monitoring. Set SO.
   - OVERVALUED: Price > FV. Skip.
   - FANTASY: Price > 1.5x FV. Skip and flag.

OUTPUT FORMAT:
```
## {TICKER} Triage | {DATE}
**QS:** {QS} Tier {TIER} | **Price:** {PRICE} | **FV:** {FV} | **Entry:** {ENTRY}
**Verdict:** {VERDICT}

**Business:** {2-paragraph summary}

**Financials:** Rev CAGR {X}%, EBIT margin {X}%, ROIC {X}% vs WACC {X}%, FCF conv {X}%, Debt/EBITDA {X}x

**Valuation:**
- Method 1 ({name}): FV = {X}
- Method 2 ({name}): FV = {X}
- Weighted FV: {X}

**Key Risk:** {1 sentence}
**Catalyst:** {1 sentence or "None identified"}

**Next Step:** {ACTIONABLE → "Full R1" | AT_FV → "SO at {entry}" | OVERVALUED → "Skip" | FANTASY → "Skip, revisit at {price}"}
```

RULES:
- Do NOT launch sub-agents. This is a SINGLE agent task.
- Do NOT write thesis files. Output goes to orchestrator only.
- Use WebSearch for recent financials if needed (max 2 searches).
- Use tools: quality_scorer.py (if QS needs verification), price_checker.py, narrative_checker.py
- Be HONEST about uncertainty. If you can't value it quickly, say so.
- Err toward OVERVALUED verdict when uncertain (reduces fantasy R1s).
```

## Orchestrator Workflow

```
1. Select 4-6 candidates from r1_prioritizer.py (QS >= 65, no FV, not in cooldowns)
2. For each candidate:
   a. price_checker.py TICKER (get current price)
   b. Check sector view exists (Glob)
   c. Launch fundamental-analyst with triage prompt (SEQUENTIAL, not parallel)
   d. Record result in quality_universe.yaml:
      - fair_value, entry_price, pipeline_status, triage_verdict, triage_date
3. For ACTIONABLE: queue for full R1 (next session or this session if bandwidth)
4. For AT_FV: create SO in standing_orders.yaml
5. For OVERVALUED/FANTASY: mark in universe, skip

PIPELINE STATUS MAPPING:
- ACTIONABLE → pipeline_status: TRIAGE_ACTIONABLE
- AT_FV → pipeline_status: TRIAGE_WATCHLIST
- OVERVALUED → pipeline_status: TRIAGE_OVERVALUED
- FANTASY → pipeline_status: TRIAGE_FANTASY
```

## Anti-Patterns
1. **Spending 30+ min on a triage** — if it's taking that long, it's not a triage
2. **Launching 3 agents per triage** — that's an R1, not a triage
3. **Writing thesis files for triages** — output stays in universe, not thesis/
4. **Not checking eToro BEFORE triage** — Gate 0 is tradability
5. **Triaging companies already in cooldown** — check r1_cooldowns first

## Success Metrics
- 4-6 triages per SPRINT session
- Fantasy rate < 30% (pre-filtered candidates)
- Each triage < 15 min wall clock
- Every ACTIONABLE/AT_FV gets an SO within the session

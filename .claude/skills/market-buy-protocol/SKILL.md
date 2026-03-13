# Market Buy Protocol — Aggressive Deployment Skill

> Deploy capital into the highest-quality opportunities at market prices.
> Cash is failure. Quality at reasonable price beats cash at any horizon > 1 year.
> Run `portfolio_cagr.py` FIRST, then apply this protocol to candidates.

---

## When to Use

- Every session as part of P1 DEPLOYMENT check
- When cash > 10% for > 2 sessions (EMERGENCY mode)
- After any SELL (redeploy within 48h)
- When `portfolio_cagr.py` surfaces market buy candidates

---

## Core Logic

```
FOR each candidate in universe with FV defined:
  E[CAGR]@market = (FV/Price)^(1/3) - 1 + growth + yield

  IF E[CAGR]@market > 15% AND QS_adj >= 75 (Tier A):
    -> MARKET BUY candidate

  IF E[CAGR]@market > 18% AND QS_adj >= 55 (Tier B):
    -> MARKET BUY candidate

  IF E[CAGR]@market > E[CAGR] of WORST current position + 3pp:
    -> ROTATION candidate (SELL worst, BUY this)
```

---

## 6 Gates (ALL must pass before presenting to human)

| Gate | Check | Tool |
|------|-------|------|
| G1 | R1 COMPLETE minimum (thesis exists with kill conditions + `> **Expected Growth:**` header line) | Check `pipeline_status` in universe + verify thesis header |
| G2 | No active kill condition approaching | Read thesis kill conditions section |
| G3 | Sector view exists and < 30d old | `sector_health.py freshness` |
| G4 | Portfolio constraints pass (concentration, sector, geo) | `constraint_checker.py CHECK TICKER AMT` |
| G5 | eToro tradable (confirmed) | Check ETORO_UNAVAILABLE in r1_prioritizer.py |
| G6 | Basket context (if in basket): max 2 new per session per basket, no basket KC active | Read `state/thematic_baskets.yaml` |

---

## Speed Protocol

| Pipeline Status | Action | Time |
|----------------|--------|------|
| R3+ COMPLETE | FAST TRACK: present immediately | Same wave |
| R1 COMPLETE only | Run investment-committee (R4) in express mode | Same session |
| SCORED only + QS > 80 | Fast-R1 + R4 express | Same session (2 waves) |
| SCORED + QS 55-80 | Standard R1 pipeline, schedule for next session | Next session |

### Express R4 Mode

When a market buy candidate needs R4 but has R1 complete:
1. Launch investment-committee with note: "EXPRESS MODE — market buy candidate, E[CAGR] X% at current price"
2. Committee evaluates 10 gates with EXISTING R1 data (no new R2 required for express)
3. If 8/10 gates pass: APPROVE for market buy
4. If < 8/10: flag issues, schedule standard R2-R3 for next session

---

## Rotation Protocol

```
EVERY SESSION:
  1. Run forward_return.py --active-only -> identify WORST position by E[CAGR]
  2. Run portfolio_cagr.py -> see market buy candidates
  3. IF best_candidate_ecagr > worst_position_ecagr + 3pp:
     AND best_candidate_qs >= worst_position_qs:
       -> ROTATION CANDIDATE
       -> Present: "SELL [worst] at E[CAGR] X%, BUY [best] at E[CAGR] Y% = +Zpp improvement"
  4. Human confirms -> execute SELL + BUY same session
```

**Rotation is NOT selling at a loss.** Rotation is upgrading expected forward return. A position at +5% P&L with 6% E[CAGR] is WORSE going forward than a new position at 0% P&L with 15% E[CAGR].

---

## Sizing for Market Buys

| Portfolio Cash % | Standard Size | Rationale |
|-----------------|---------------|-----------|
| > 40% | EUR 800-1,200 (8-12% target) | Aggressive deployment to reduce drag |
| 20-40% | EUR 500-800 (5-8%) | Standard sizing |
| 10-20% | EUR 300-500 (3-5%) | Conservative, approaching full deployment |
| < 10% | Only via rotation | No new cash to deploy |

Sizing also considers:
- Conviction (from R1/R3 depth): HIGH = upper range, MEDIUM = mid, LOW = do not market buy
- Concentration: `constraint_checker.py` must pass
- Sector/geo balance: check existing exposure

---

## Anti-Patterns

1. **"Let me wait for earnings"** — If E[CAGR] > 15% and earnings are > 30d away, BUY NOW. Earnings risk is priced in. Waiting 30d costs ~1.2% of E[CAGR].
2. **"The DA hasn't run yet"** — ~~If R1 thesis is solid and E[CAGR] > 18%, the DA correction buffer is built into the threshold gap.~~ **INVALIDATED by S147 DA audit.** All 10 DAs = MODERATE COUNTER. Bias is systematic, not random. No "buffer" exists. **NEW RULE:** Market buy allowed pre-DA ONLY if DA is scheduled within 5 sessions of position opening. If DA not completed by session +5, position enters MANDATORY REVIEW. Track in session_continuity.yaml → promises[].
3. **"Let me get a better price"** — This is L-02 and L-05. If E[CAGR] at current price meets threshold, the price IS good enough.
4. **"I already have 11 positions"** — Rotation handles this. SELL the worst to BUY the best.
5. **"Cash might be needed for a correction"** — Risk is controlled through quality and kill conditions, not cash. (P15)

---

## Output Template

When presenting a market buy recommendation:

```
MARKET BUY RECOMMENDATION
Ticker: [TICKER]
Action: [BUY / ROTATE from WORST]
Price: [current] | FV: [value] | MoS: [X]%
E[CAGR]: [X]% (vs [threshold]% threshold)
QS: [X] (Tier [A/B]) | Pipeline: [R1/R3/R4]
Size: EUR [X] ([Y]% of portfolio)

Gates: G1[PASS] G2[PASS] G3[PASS] G4[PASS] G5[PASS] G6[PASS]
Basket: [basket_name or "unassigned"]

If ROTATION:
  SELL: [worst_ticker] at E[CAGR] [X]%
  BUY: [ticker] at E[CAGR] [Y]%
  Improvement: +[Z]pp forward return

Confirm? (Human executes on eToro)
```

---

## Precedent: MORN Market Buy (S101)

First E[CAGR]-framework market buy. MORN at $160.76:
- E[CAGR] 15.6% >> 12% Tier A threshold
- MoS 17% (below historical 29-38% but justified by Expected Return)
- QS 78 Tier A, 46% insider, zero portfolio overlap
- Result: validates the framework. Deploy-first works when quality is high.

---

---

## STALE Standing Order Evaluation (v4.8)

Standing orders that sit untriggered become stale and must be actively managed.

**Definition:** SO with >15% distance to trigger for >30 days without a specific catalyst with date = STALE.

**Staleness Protocol (Fase 3 of each session):**
```
FOR each SO in standing_orders.yaml:
  distance = (current_price - trigger) / current_price * 100
  age = days since created_date or last_analysis_date

  IF distance > 15% AND age > 30 AND no dated catalyst:
    staleness_status = STALE
    MUST choose ONE:
      (a) RECALIBRATE: Move trigger closer to market. New trigger at MoS ~10-15% for Tier A.
          Requires: thesis still valid, E[CAGR] at new trigger > 12%
      (b) MARKET BUY EVALUATE: If E[CAGR] at CURRENT price > 12% (Tier A) or > 15% (Tier B),
          present market buy to human via market-buy-protocol.
      (c) ARCHIVE: If thesis weakened OR better alternatives exist, archive SO.
          Move to extreme_opportunity[] or cancel entirely.

  IF distance <= 15% OR age <= 30 OR has dated catalyst:
    staleness_status = FRESH
```

**Anti-Patterns:**
- Leaving STALE SOs untouched for months — this is #54 (self-deception)
- "Recalibrating" by moving trigger 1% closer — that's cosmetic, not real
- Keeping 20+ SOs to feel productive when 15 are STALE

**Trigger T12:** If >50% of all SOs are STALE = RED in evolution_state.

---

## Capital Contributions

When new capital is contributed to the portfolio:

1. `basket_dashboard.py --rebalance` → identify most underfunded basket with highest E[CAGR]
2. Within that basket: deploy into highest individual E[CAGR] candidate
3. If no basket underfunded: best universe candidate regardless of basket
4. All 6 gates still apply. Capital contribution does NOT bypass due diligence.

---

**Version:** 1.2 | Updated: 2026-03-02 | Framework v4.8

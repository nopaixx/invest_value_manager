# Post-Mar 26 Execution Plan — Thu-Fri Mar 27-28

> Prepared: S284 (Mar 24). Execute after Mar 26 trades confirmed.

---

## THURSDAY Mar 27 — Day 1 Post-Execution

### Priority 0: Verify & Record (09:00 CET)
- [ ] Confirm ALL 6-7 Mar 26 trades filled in eToro
- [ ] Record EXACT for each: shares, price, FX rate, EUR amount
- [ ] Note any partial fills or price deviations from plan

### Priority 1: portfolio-ops Update (09:30)
- [ ] Update `portfolio/current.yaml`:
  - REMOVE MONY.L (sold)
  - REMOVE FTNT (sold)
  - TRIM NVO (36.2 → 21.9 shares, update invested_usd proportionally)
  - ADD GDDY (new position with exact entry data)
  - ADD DNLM.L (new position)
  - ADD ITRK.L (new position)
  - ADD MEGP.L (if executed — contingent on ≤135p)
  - UPDATE cash balance
- [ ] Update `portfolio/history.yaml`:
  - MONY.L: full exit with P&L, dates, reason
  - FTNT: full exit with P&L, dates, reason
  - NVO: partial trim logged
- [ ] Move thesis files:
  - `thesis/active/MONY.L/` → `thesis/archive/MONY.L/`
  - `thesis/active/FTNT/` → `thesis/archive/FTNT/`
  - `thesis/research/GDDY/` → `thesis/active/GDDY/` (copy thesis.md + DA)
  - `thesis/research/DNLM.L/` → `thesis/active/DNLM.L/`
  - `thesis/research/ITRK.L/` → `thesis/active/ITRK.L/`
  - `thesis/research/MEGP.L/` → `thesis/active/MEGP.L/` (if executed)

### Priority 2: ALFA.L Execution (10:00 — LSE)
- [ ] Verify Mar 26 cash settled (~EUR 800)
- [ ] Price check ALFA.L — still ≤165p?
- [ ] BUY ALFA.L EUR 400 at market
- [ ] Record exact: shares, price, FX rate
- [ ] Update current.yaml + history.yaml
- [ ] Move `thesis/research/ALFA.L/` → `thesis/active/ALFA.L/`

### Priority 3: Starter Position Tracking (11:00)
- [ ] Update `state/session_continuity.yaml` → starter_positions[]:
  ```yaml
  starter_positions:
    - ticker: DNLM.L
      open_date: 2026-03-26
      size_eur: 200
      allocation_pct: 2.0
      90d_deadline: 2026-06-24
      prove_path: "H2 FY2026 recovery → ADD to 5%"
      status: ACTIVE
    - ticker: ITRK.L
      open_date: 2026-03-26
      size_eur: 300
      allocation_pct: 3.0
      90d_deadline: 2026-06-24
      prove_path: "Q1 results + EU AI Act Aug → ADD to 6-7%"
      status: ACTIVE
    - ticker: MEGP.L
      open_date: 2026-03-26
      size_eur: 300
      allocation_pct: 3.0
      90d_deadline: 2026-06-24
      prove_path: "FY2026 H1 laundry ramp → ADD to 5%"
      status: ACTIVE
    - ticker: ALFA.L
      open_date: 2026-03-27
      size_eur: 400
      allocation_pct: 4.0
      90d_deadline: 2026-06-25
      prove_path: "Annual report receivables + NRR → ADD to 7%"
      status: ACTIVE
  ```

### Priority 4: SM OSINT Captures (14:00)
- [ ] GDDY: Capture top holders (Vanguard 12.6%, BlackRock 11.5%, Starboard 2.0%, WCM 2.7%)
- [ ] ITRK.L: Capture holders + verify 4 director buys cluster Mar 13-16
- [ ] DNLM.L: Capture UK holders + insider data
- [ ] MEGP.L: Capture holders (if any tracked) + Crasnianski family 36.5%
- [ ] ALFA.L: Capture holders + CHP selling trend
- [ ] Run `smart_money.py sync-portfolio` to register all new positions

### Priority 5: Thematic Baskets Update (15:00)
- [ ] Update `state/thematic_baskets.yaml`:
  - US Quality Compounders: ADD GDDY (entering)
  - UK Quality Leaders: REMOVE MONY.L, ADD DNLM.L + MEGP.L + ALFA.L
  - D&A Monopolies: ADD ITRK.L (entering, TW replacement candidate)
  - Cybersecurity: REMOVE FTNT → status RESEARCHING (0 positions)

### Priority 6: Commit All Changes (16:00)
- [ ] Single comprehensive commit with all portfolio-ops changes
- [ ] Verify `forward_return.py --active-only` shows correct GrSrc for all new positions

---

## FRIDAY Mar 28 — Day 2 Post-Execution

### Priority 7: Position Health Recalc (09:00)
- [ ] Run `kc_monitor.py --health` — new baseline with 13-14 positions
- [ ] Identify any gaps: new positions missing DA, risk_assessment, etc.
- [ ] Expected: new entries will score lower initially (no position-specific DA in active/)
- [ ] Action: plan which DAs need refreshing for active positions

### Priority 8: Stress Test Post-Restructuring (09:30)
- [ ] Run `stress_test.py` — full Monte Carlo with new portfolio
- [ ] Compare vs pre-Mar 26 baseline (report: 2026-03-23.json)
- [ ] Key metrics to compare:
  - Portfolio beta (was 0.626 — expect change with FTNT exit + 4 new UK positions)
  - P5 VaR (was -30.5%)
  - GFC drawdown (was -37.9%)
  - COVID drawdown (was -31.0%)
  - Most vulnerable position (was HLNE)
- [ ] Save to `reports/stress_test/2026-03-28.json`

### Priority 9: Forward Return New Ranking (10:00)
- [ ] Run `forward_return.py --active-only` — new E[CAGR] ranking
- [ ] Run `portfolio_cagr.py --verbose` — new blended E[CAGR]
- [ ] Compare vs pre-Mar 26 baseline:
  - Deployed E[CAGR]: was 17.8% → target 18.2%+
  - Blended E[CAGR]: was 17.1%
  - Worst position: was FTNT 10.1% → should be TW 13.3%
- [ ] Verify new position E[CAGR] calculations match thesis expectations

### Priority 10: Constraint Check (10:30)
- [ ] Run `constraint_checker.py REPORT --baskets`
- [ ] Check: EDEN.PA still >15%? (HARD TRIM rule)
- [ ] Check: any basket >40% concentration?
- [ ] Check: geographic concentration (UK now 4 positions: IHP.L + DNLM.L + MEGP.L + ALFA.L)
- [ ] Run `correlation_matrix.py` — check new position correlations

### Priority 11: SM Daily Report (11:00)
- [ ] Run full SM pipeline: signals, alerts, crowding, exodus-check
- [ ] Generate 5 charts dated 2026-03-28
- [ ] Write weekly SM report (consolidates Mon-Fri)

### Priority 12: Session Continuity (12:00)
- [ ] Update `state/session_continuity.yaml` with:
  - Mar 26 execution summary (7-8 trades, all filled/any issues)
  - New portfolio composition
  - Starter position deadlines registered
  - Promises for next session
- [ ] Update `state/system.yaml` with new portfolio summary

### Priority 13: LNTH PDUFA Check (14:00 — if Mar 29 is Saturday)
- [ ] LNTH OCTEVY PDUFA due Mar 29
- [ ] If FDA decision published Friday PM: assess impact on pipeline thesis
- [ ] If APPROVED: R3 resolution, reconsider entry $68
- [ ] If REJECTED: FV drops, archive or reduce entry

---

## Additional Items (not in original list)

### 14. Standing Orders Cleanup
- [ ] Archive MONY.L SO (if any)
- [ ] Archive FTNT SO (exit complete)
- [ ] MEGP.L: if executed Mar 26, remove from active SOs
- [ ] ALFA.L: if executed Mar 27, remove from active SOs
- [ ] Verify remaining SOs: SPGI $380, KNSL $355 (gated), HALO $55 (gated)

### 15. Pipeline Tracker Update
- [ ] Update `state/pipeline_tracker.yaml` with:
  - GDDY: R4 → EXECUTED
  - DNLM.L: R4 → EXECUTED
  - ITRK.L: R4 → EXECUTED
  - MEGP.L: R4 → EXECUTED
  - ALFA.L: R4 → EXECUTED
  - MONY.L: ACTIVE → CLOSED
  - FTNT: ACTIVE → CLOSED

### 16. Error Pattern Check
- [ ] Review S284 decisions against error patterns:
  - Error #57: basket deployment without per-stock DD? (all have R4 ✓)
  - Error #12: constraint_checker before each buy? (run post-execution ✓)
  - Error #41: post-analysis cycle complete? (SOs, alerts, thesis filed ✓)

### 17. UK Geographic Concentration Review
- [ ] Post-execution UK = 4 positions (IHP.L + DNLM.L + MEGP.L + ALFA.L)
- [ ] Estimate UK% of portfolio (likely 18-22%)
- [ ] Compare to P2 (geographic diversification) — is this concentration justified?
- [ ] Document reasoning in session output
- [ ] Cross-holding risk: Baillie Gifford holds IHP.L + EDEN.PA — now 4 UK positions amplifies UK-specific risk

### 18. Next Week Preview
- [ ] LNTH PDUFA Mar 29 — pipeline binary event
- [ ] NVO ex-div Mar 30 — verify trim was before ex-div
- [ ] HALO PTAB oral hearings Mar 31
- [ ] TSLA Q1 deliveries Apr 5 — short decision gate
- [ ] Begin CVNA earnings framework prep (due Apr 25)

---

*Plan prepared S284. Execute sequentially Thursday-Friday.*

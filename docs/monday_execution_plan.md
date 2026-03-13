# Monday Execution Plan — 2026-03-10

## TRADE 1: SELL AUTO.L (Market Open)

**Action:** SELL 65 shares AUTO.L at market
**Expected proceeds:** ~GBP 32,162 (~EUR 370 at current FX)
**Reason:** Weakest position (E[CAGR] 12.1%), lowest conviction (LOW), moat under siege (180+ downgrades, Amazon Autos UK threat, CMA monitoring). April pricing event is upside catalyst but asymmetric: if pricing sticks → +10-15% upside; if >200 cancellations → -20% downside.

**Pre-execution checklist:**
- [ ] Confirm AUTO.L market price at open (expect ~495p)
- [ ] Place SELL order in eToro
- [ ] Wait for fill confirmation

## TRADE 2: ADD ADBE (After AUTO.L Fill)

**Action:** BUY ~EUR 370 ADBE at market (~1.3 shares at ~$284)
**Expected cost:** EUR 370 (from AUTO.L proceeds)
**Reason:** +6.1pp E[CAGR] improvement (12.1% → 18.2%). ADBE at 37.5% MoS, QS 76 Tier A, 8.9% → 12.4% of portfolio.

**Pre-execution checklist:**
- [ ] Confirm ADBE pre-market price (expect ~$284)
- [ ] Calculate exact shares affordable from AUTO.L proceeds
- [ ] Place BUY order in eToro
- [ ] Wait for fill confirmation

**Risk note:** ADBE earnings Wed Mar 12. Adding 2 days before earnings is intentional — at 37.5% MoS the buffer absorbs a CONDITIONAL result. Only a FAIL scenario (rev <$5.6B AND NRR <98%) would threaten the thesis.

## POST-TRADE ACTIONS (Claude executes after human confirms)

1. **portfolio-ops agent:** Update current.yaml (remove AUTO.L, update ADBE shares/avg cost)
2. **Update thematic_baskets.yaml:** Remove AUTO.L from uk-digital-platforms basket
3. **Update standing_orders.yaml:** Archive any AUTO.L SOs
4. **Update system.yaml:** Position count 11 → 10
5. **Log in decisions_log.yaml:** ROTATION decision with reasoning
6. **Move thesis:** thesis/active/AUTO.L/ → thesis/archive/AUTO.L/ (sold)
7. **Update sector view:** digital-marketplaces.md — move AUTO.L to closed positions

## FTNT INVESTOR DAY (3:00 PM PT / 12:00 AM CET)

**Parallel with trades.** Process using Section 9 framework (122 lines, thesis lines 214-336).

| Scenario | Key Metrics | FV Impact | Action |
|----------|------------|-----------|--------|
| BULL | SASE ARR >$1B, +35% growth, ASIC roadmap, CVE post-mortem strong | $88 → $95-100 | HOLD, upgrade conviction |
| BASE | Incremental updates, SASE +25-30%, no new guidance | $88 unchanged | ROTATION CANDIDATE remains |
| BEAR | SASE deceleration <25%, no ASIC roadmap, CVE dismissal | $88 → $75-80 | EXIT Protocol immediately |

## RISK CALENDAR THIS WEEK

| Day | Event | Impact | Preparation |
|-----|-------|--------|-------------|
| Mon | FTNT Investor Day 3PM PT | HIGH | Framework ready |
| Tue | US CPI (Feb) | MODERATE | Stress test done: 22.8% HIGH vuln |
| Wed | ADBE Q1 FY2026 earnings | HIGH | Framework 100% ready (130 lines) |
| Thu | ECB rate decision | LOW | No direct portfolio exposure |

---

*Prepared S149 2026-03-08. Execute Monday market open.*

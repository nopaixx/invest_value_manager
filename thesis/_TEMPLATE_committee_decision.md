# Committee Decision: [TICKER] ([Company Name])

> **Date:** YYYY-MM-DD (Session XXX)
> **Verdict:** BUY / BUY CONDITIONAL / WATCHLIST / REJECT
> **R3 FV:** $XXX | **Entry:** $XXX | **E[CAGR]:** X.X%
> **QS:** XXadj Tier X

---

## 10 Gates

| Gate | Result | Key Detail |
|------|--------|------------|
| **0. Sector View** | PASS/FAIL | [sector-file.md exists? date?] |
| **1. Quality Score** | PASS/FAIL | QS XX ≥ 55 (Tier B minimum) |
| **2. Business Understanding** | PASS/FAIL | [Can explain in 2 min why it's cheap?] |
| **3. Projections** | PASS/FAIL | [Growth X%, WACC X%, scenarios documented] |
| **4. Valuation** | PASS/FAIL | [Multi-method? FV convergence?] |
| **5. MoS** | PASS/FAIL | [MoS X% vs X% required for Tier] |
| **6. Macro** | PASS/FAIL/ADVERSE | [Current macro context favorable?] |
| **7. Portfolio Fit** | PASS/FAIL | [Concentration, correlation, cash impact] |
| **8. Sector Alignment** | PASS/FAIL | [Sector status SOBREPONDERAR/NEUTRAL/EVITAR] |
| **9. Autocritica** | PASS/FAIL | [Edge identified? Error patterns checked?] |
| **10. Counter-Analysis** | PASS/FAIL | [DA resolved? All HIGH findings addressed?] |

---

## Gate Details

### Gate 0: Sector View
[Does sector view exist? Is it fresh? Status?]

### Gate 5: Margin of Safety
[E[CAGR] at entry vs threshold. MoS vs bear case. Sufficient?]

### Gate 7: Portfolio Fit
[Run constraint_checker.py CHECK TICKER AMT. Results:]
- Position size: X.X% of portfolio
- Sector concentration: X.X%
- Geographic concentration: X.X%
- Cash post-trade: X.X%
- 50% drawdown impact: -X.Xpp

### Gate 9: Autocritica
- Edge vs market: [What do we see that market doesn't?]
- Error patterns checked: [#7, #12, #16, #29, #30, #43, #49]
- "Would I buy from zero TODAY?": [YES/NO + reasoning]

### Gate 10: Counter-Analysis
- DA verdict: [WEAK/MODERATE/STRONG COUNTER]
- HIGH findings: [count] — all resolved in R3? [YES/NO]
- Unresolved items: [any? if so, what gates/conditions]

---

## Blocking Issues

[List any HARD GATES or FAIL results. What must happen before execution?]

---

## Execution Recommendation

- **Action:** BUY / SO / WATCHLIST
- **Trigger:** $XXX
- **Size:** EUR XXX (X.X% portfolio)
- **Gate:** [pre-execution condition if any]
- **Capital source:** [where EUR comes from]
- **Expiry:** YYYY-MM-DD
- **Post-execution:** [what to monitor]

---

## META-REFLECTION

### Committee Doubts
- [Any uncertainty in the decision]

### System Improvement Suggestions
- [Process gaps discovered during gate evaluation]

### Dissent Record
- [If any gate was borderline, document the reasoning both ways]

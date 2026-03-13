# EXECUTION PLAN — Week of March 9-14, 2026
# Created: S149 (2026-03-08)
# Status: ACTIVE

---

## MONDAY March 10

### 08:00 CET — Market Open
1. **SELL AUTO.L** (65 shares, ~EUR 370)
   - Conviction: LOW. E[CAGR] 12.1% = below portfolio average. April pricing event risk
   - Action: market sell at open. Accept whatever price (expected ~490-500p)
   - Result: cash ~EUR 370, portfolio 10 positions, ~3.0% cash
   - POST-SELL: Confirm execution → update current.yaml + history.yaml via portfolio-ops

2. **Price check all positions** — verify no overnight gaps from Hormuz/weekend developments
   - If any position gaps -5%+: investigate cause before doing anything else
   - If oil >$95: elevated crisis — defer AUTO.L sell to assess

3. **SO proximity check:**
   - GDDY $90 trigger, currently $93.95 (4.4% above) — CONDITIONAL on FTNT outcome
   - BZU.MI EUR 42, currently EUR 43.62 (3.7% above) — watch
   - DNLM.L 950p — watch (but AUTO.L sell means 2 UK positions, room for 3rd)

### 10:00 CET — ORCL earnings review (reported previous evening Mon after close)
- Oracle Q3 FY2026 results — NOT our position, but cloud/enterprise bellwether
- If ORCL misses on cloud growth: NEGATIVE read-through to ADBE (both enterprise software)
- If ORCL beats on cloud: POSITIVE read-through — reduces ADBE earnings anxiety

### 23:00 CET (3:00 PM PT) — FTNT Investor Day
- **LISTEN LIVE** (investor.fortinet.com webcast)
- **5-POINT CHECKLIST:**

| # | Metric | BULL | BEAR | Decision Impact |
|---|--------|------|------|-----------------|
| 1 | Unified SASE ARR | >$1B, growth >35% | <25% or no disclosure | KC#2, growth engine |
| 2 | ASIC SP6 roadmap | Timeline + benchmarks | Silence on next-gen | Core moat validity |
| 3 | FY2027+ revenue trajectory | >12% CAGR, $10B+ path | <10% or no LT guide | E[CAGR] revision |
| 4 | CVE incident response | Transparent post-mortem, retention data | Downplay/ignore | KC#6 monitoring |
| 5 | Platformization attach rate | >4 products/customer, >50% multi-product | Flat at 3.5x | Moat width |

- **DECISION TREE:**

```
FTNT INVESTOR DAY OUTCOME
|
+-- BULL (3+ metrics BULL)
|   → FV $88 → $95-100
|   → HOLD FTNT, raise FV
|   → EUR 370 cash → HOLD as buffer for ADBE Wed
|   → GDDY SO stays at $85-90 passive entry
|
+-- BASE (mixed signals)
|   → FV $88 unchanged
|   → HOLD FTNT, E[CAGR] stays 9.7% (worst in portfolio)
|   → Consider: is 7.5% allocation justified for worst E[CAGR]?
|   → EUR 370 cash → buffer for ADBE Wed
|
+-- BEAR (2+ metrics BEAR)
|   → FV $88 → $75-80
|   → EXIT protocol: SELL FTNT (EUR ~761)
|   → Combined capital: EUR 370 (AUTO.L) + EUR 761 (FTNT) = EUR 1,131
|   → BUY GDDY at market (~$92-95): EUR 720
|   → Remaining EUR 411 → ADD ADBE pre-earnings or hold cash
```

---

## TUESDAY March 11

### 08:00 CET — Post-FTNT assessment
- Process Investor Day outcome using decision tree above
- If BEAR: execute SELL FTNT → BUY GDDY chain
- If BULL/BASE: no action, prepare for ADBE

### 14:30 CET (8:30 AM ET) — US CPI Release (February 2026 data)
- **KEY CONTEXT:** Oil WTI at $90. If CPI comes in HOT (>3.5% YoY or >0.4% MoM):
  - Market will sell off broadly
  - Fed rate cut expectations pushed out
  - Growth stocks (ADBE, DOCS, HLNE, TW) hit hardest
  - BUT: hot CPI = buying opportunity if driven by oil (temporary) not core inflation
- **If CPI COLD (<3.0%):** Market relief rally. No action needed
- **If CPI HOT:** DO NOT PANIC SELL. Hold positions. Consider it opportunity to ADD if ADBE drops pre-earnings
- **RULE:** CPI reaction = DO NOTHING. Never trade CPI day. Wait 24h for dust to settle

---

## WEDNESDAY March 12 — ADBE EARNINGS

### Pre-market
- Price check ADBE. If already below $240 pre-earnings → stronger ADD case post-results
- Verify ADBE earnings framework ready (thesis/active/ADBE/earnings_framework_q1fy26.md — CONFIRMED READY)

### 22:00 CET (4:00 PM ET) — ADBE Q1 FY2026 After Close
- **Framework: thesis/active/ADBE/earnings_framework_q1fy26.md**

| Metric | PASS | CONDITIONAL | FAIL |
|--------|------|-------------|------|
| Revenue | >= $6.25B | $6.15-6.24B | < $6.15B |
| Non-GAAP EPS | >= $5.85 | $5.75-5.84 | < $5.60 |
| DM ARR growth | Sequential improvement | 9-10% | < 8% |
| FY2026 guidance | Maintained/raised | Lowered 1-3% | Cut >5% |
| Gross margin | >= 88.5% | 87.5-88.5% | < 87% |
| FTC reserve | No increase | +$200-500M | > $1B or settlement |
| Firefly/AI | Continued traction | Flat | Declining |

- **DECISION TREE:**

```
ADBE EARNINGS
|
+-- PASS (all metrics within/above guide)
|   → FV $390 confirmed
|   → ADD ADBE with EUR 370 (AUTO.L proceeds) if price < $285
|   → If price > $285 post-earnings: HOLD, keep cash
|   → Proceed to R3 resolution
|
+-- CONDITIONAL (slight miss, 1-2 metrics soft)
|   → FV $350-380 (reassess)
|   → HOLD, no ADD
|   → Monitor Q2 for recovery
|   → Cash stays as buffer
|
+-- FAIL (major miss or guidance cut)
|   → Launch EXIT protocol (6 gates)
|   → FV drops to $280-320
|   → If KC#6 triggered (FTC): EXIT
|   → Cash from ADBE (~EUR 935) + AUTO.L (EUR 370) = EUR 1,305 for redeployment
|   → Candidates: GDDY (R4 approved), BAH (if <$75), BZU.MI (if <EUR 42)
```

---

## THURSDAY-FRIDAY March 13-14

### Post-ADBE processing
- If PASS: complete R3 resolution, update thesis header, portfolio_stats check
- If FAIL: full EXIT protocol, reallocation plan
- Process any other market developments from the week

### Standing order monitoring
- GDDY $90 (currently $93.95 — 4.4% above, volatile week could trigger)
- BZU.MI EUR 42 (3.7% above)
- BAH $75 (8.3% above)

### Other events
- FOUR.L FY2025 Results: Mar 18 (next week, but prepare review framework)
- HLNE ex-dividend: Mar 20 (capture, no action)
- MONY.L ex-dividend: Mar 26 (capture, no action)

---

## CASH DEPLOYMENT SCENARIOS (summary)

| Scenario | Mon | Tue | Wed | Thu | Cash End |
|----------|-----|-----|-----|-----|----------|
| **Base (FTNT neutral, ADBE pass)** | Sell AUTO.L (+370) | Hold | ADD ADBE (-370) | — | 0% |
| **FTNT bear, ADBE pass** | Sell AUTO.L (+370), Sell FTNT (+761) | Buy GDDY (-720) | ADD ADBE (-370) | — | ~0.3% |
| **FTNT bull, ADBE fail** | Sell AUTO.L (+370) | Hold | EXIT ADBE (+935) | Redeploy | TBD |
| **FTNT bear, ADBE fail** | Sell AUTO.L (+370), Sell FTNT (+761) | Buy GDDY (-720) | EXIT ADBE (+935) | Redeploy | TBD |
| **Oil crisis escalation** | Defer all | Assess | Assess | — | 3.0% |

---

## RISK ALERTS

1. **Hormuz re-escalation over weekend** → Oil >$95 = defer AUTO.L sell, assess all positions
2. **CPI hot + ADBE miss** = double hit on growth names. ADBE, DOCS, HLNE most exposed. DO NOT PANIC
3. **GDDY drops to $90 or below** = SO triggered. If FTNT not yet decided → conflict (can't sell FTNT and buy GDDY simultaneously). Resolution: buy GDDY with AUTO.L proceeds if FTNT undecided
4. **BZU.MI drops to EUR 42** = SO triggered. Independent of FTNT/ADBE. Execute if triggered

# Smart Money Daily Report — YYYY-MM-DD

> Generated: YYYY-MM-DD HH:MM CET
> Graph: XXX nodes, X,XXX edges, XXX funds
> Sources: FCA [Xd], AMF [Xd], 13F [Xd], Form4 [Xd]

---

## 1. Data Quality

> Command: `python3 tools/smart_money.py stale`
> Command: `python3 tools/smart_money.py coverage`

| Source | Last Update | Age | Cadence | Status |
|--------|-------------|-----|---------|--------|
| FCA UK shorts | YYYY-MM-DD | Xd | 3d | FRESH / STALE / VERY_STALE |
| AMF France shorts | YYYY-MM-DD | Xd | 3d | FRESH / STALE / VERY_STALE |
| CONSOB Italy shorts | YYYY-MM-DD | Xd | 7d | FRESH / STALE |
| AFM-NL Netherlands | YYYY-MM-DD | Xd | 7d | FRESH / STALE |
| SEC 13F | YYYY-MM-DD | Xd | 90d | OK / DUE |
| SEC Form 4 | YYYY-MM-DD | Xd | 30d | OK / DUE |

**Coverage gaps (portfolio <100%, pipeline SO <67%):**
- [Ticker]: XX% coverage — missing [source]
- [Ticker]: XX% coverage — missing [source]

**Action if ANY source VERY_STALE:** Download + ingest BEFORE continuing. Per S280 HARD RULE.

---

## 2. Portfolio Signals

> Command: `python3 tools/smart_money.py signals --portfolio-only`

| Ticker | Convergence | Insider | Short | Herd Warning | Net Signal |
|--------|------------|---------|-------|-------------|------------|
| ADBE | X funds (names) | $XM buy/sell | X.X% SI | X funds | BULL / BEAR / NEUTRAL |
| EDEN.PA | — | — | X.X% (X funds) | X funds | [signal] |
| NVO | X funds (names) | — | — | X funds | [signal] |
| [etc for each active position] | | | | | |

**Strongest signal:** [ticker] — [description]
**Weakest signal:** [ticker] — [description]
**Changes vs yesterday:** [new signals, exits, reversals]

---

## 3. Exodus Check

> Command: `python3 tools/smart_money.py exodus-check`

| Ticker | Funds Now | Funds Prev | Change | Signal |
|--------|-----------|-----------|--------|--------|
| [ticker] | X | X | +/-X | STABLE / MINOR EXIT / SIGNIFICANT EXIT / ACCUMULATION |

**Verdict:** NO EXODUS / INSTITUTIONAL_EXODUS DETECTED
- Threshold: 3+ positions with fund count decline → INSTITUTIONAL_EXODUS
- If EXODUS: list exiting funds by name per position

---

## 4. Sector Flows

> Command: `python3 tools/smart_money.py sector-flows`

| Sector | New Positions | Exits | Net | Signal |
|--------|--------------|-------|-----|--------|
| Technology | +X | -X | +/-X | ACCUMULATING / DISTRIBUTING / NEUTRAL |
| Healthcare | +X | -X | +/-X | [signal] |
| Financials | +X | -X | +/-X | [signal] |
| [etc] | | | | |

**Notable rotations:** [Fund X exited Sector Y → entered Sector Z]

**Portfolio alignment:**
- Our baskets aligned with: [sectors ACCUMULATING where we're invested]
- Our baskets misaligned with: [sectors DISTRIBUTING where we're invested]

---

## 5. Basket SM Overlay

> Command: `python3 tools/smart_money.py basket-signals`

| Basket | Convergences | Insiders | Shorts | Top Funds | Assessment |
|--------|-------------|----------|--------|-----------|------------|
| US Quality Compounders | X total | $XM | — | [fund names] | STRONGEST / STRONG / Moderate / Limited |
| UK Quality Leaders | X total | $XM | — | [fund names] | [assessment] |
| D&A Monopolies | X total | — | — | [fund names] | [assessment] |
| [etc] | | | | | |

**Strongest basket conviction:** [basket] — [why]
**Weakest basket conviction:** [basket] — [why]

---

## 6. Crowding Risk

> Command: `python3 tools/smart_money.py signals` (filter HERD_WARNING)

| Ticker | Funds Holding | Median Ratio | Risk Level |
|--------|--------------|-------------|------------|
| [ticker] | X funds | X.Xx median | HIGH / MODERATE / LOW |

**Positions with HERD_WARNING in portfolio:**
- [ticker]: X funds hold (X.Xx median) — [implication]

**Change vs yesterday:** [any new HERD_WARNINGs or exits]

---

## 7. Insider Sectors

> Command: `python3 tools/smart_money.py insider-sectors`

| Sector | Insider Buys (60d) | Companies | Signal |
|--------|-------------------|-----------|--------|
| [sector] | X buys | X companies | SECTOR_INSIDER_CLUSTER / Normal |

**SECTOR_INSIDER_CLUSTER details:**
- [sector]: [company1] ([role] $XM), [company2] ([role] $XM), ...

**Portfolio relevance:**
- We hold positions in: [sectors with clusters] ← cluster CONFIRMS / CONTRADICTS
- Pipeline in: [sectors with clusters] ← cluster CONFIRMS / CONTRADICTS

---

## 8. Discovery Auto-Flag

> Command: `python3 tools/smart_money.py discover --auto-flag`

| Ticker | Fund Count | Fund Names | Thesis Status | Priority |
|--------|-----------|-----------|---------------|----------|
| [ticker] | X funds | [names] | NO THESIS → R1 PRIORITY | HIGH / MEDIUM |
| [ticker] | X funds | [names] | R1 exists, no R2 | MEDIUM |

**New R1 priorities (3+ fund convergence, no thesis.md):** X tickers
**Action:** Launch R1 for top X priorities this session

---

## 9. Contrarian Opportunities

> Derived from: exodus-check + signals + sector-flows

**Funds selling what we hold (potential thesis challenge):**
- [fund] exited [our ticker] — [is this signal or noise?]

**Funds buying what we DON'T hold (potential discovery):**
- [fund] initiated [ticker] at $X — [already in pipeline? worth R1?]

**Quality funds disagreeing with each other on same ticker:**
- [fund1] LONG [ticker] vs [fund2] SHORT [ticker] — [what does this mean?]

---

## 10. Actionable Items

| # | Priority | Action | Ticker | Source |
|---|----------|--------|--------|--------|
| 1 | P0 | [Download + ingest stale source] | SYSTEM | Data Quality §1 |
| 2 | P1 | [Launch R1 for auto-flagged discovery] | [ticker] | Discovery §8 |
| 3 | P1 | [Re-evaluate position with exodus signal] | [ticker] | Exodus §3 |
| 4 | P2 | [Investigate insider cluster in sector X] | SECTOR | Insider §7 |
| 5 | P2 | [EU capture for low-coverage position] | [ticker] | Coverage §1 |

---

## META-REFLECTION

### Anomalies Detected
- [Data inconsistency or unexplained pattern found in SM data]

### Suggestions
- [System improvement for SM intelligence pipeline]

### Questions for CIO
- [Decision that requires CIO judgment based on today's SM data]

---

*Command reference for generating this report:*
```bash
python3 tools/smart_money.py stale                    # §1 Data Quality
python3 tools/smart_money.py coverage                 # §1 Coverage
python3 tools/smart_money.py signals --portfolio-only # §2 Portfolio Signals
python3 tools/smart_money.py exodus-check             # §3 Exodus
python3 tools/smart_money.py sector-flows             # §4 Sector Flows
python3 tools/smart_money.py basket-signals           # §5 Basket Overlay
python3 tools/smart_money.py signals                  # §6 Crowding (HERD_WARNING)
python3 tools/smart_money.py insider-sectors          # §7 Insider Sectors
python3 tools/smart_money.py discover --auto-flag     # §8 Discovery
python3 tools/smart_money.py snapshot                 # Save for next day comparison
```

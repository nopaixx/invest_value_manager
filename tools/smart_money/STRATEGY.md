# Smart Money Graph — Strategic Cadence & Roadmap

> Persistent reference for future sessions. Read during Fase 2.5.7.
> Last updated: 2026-02-21 (Session 109)

---

## 1. Session Cadence (every session, Fase 2.5.7)

```
1. smart_money.py stale           -> check freshness of all sources
2. IF stale: refresh              -> download + ingest stale sources
3. smart_money.py alerts          -> changes vs last snapshot
4. IF alerts CRITICAL: stock-profile TICKER  -> deep dive
5. Pre-decision: stock-profile TICKER before any R4/S4 vote
```

**Time budget:** ~2 min (stale check), ~5 min (refresh if needed), ~1 min (alerts scan).

---

## 2. Weekly Cadence

```
1. FCA + AMF download + ingest    (automated via staleness check, cadence 3 days)
2. crowding --top 20              -> crowding risk changes
3. coverage --portfolio-only      -> any new positions missing from graph?
4. metrics                        -> fund centrality shifts
```

---

## 3. Quarterly Cadence (within 60 days of quarter-end)

```
1. download 13f + ingest-13f     -> full 13F refresh (SEC filings lag ~45 days)
2. communities                    -> fund clustering analysis
3. Accuracy audit: snapshot diff vs price performance
4. Fund universe review: new quality funds to track? (tracked_funds.yaml)
5. gc                             -> clean old snapshots (keep 1/quarter)
```

**13F filing deadlines:** Q4 by Feb 14, Q1 by May 15, Q2 by Aug 14, Q3 by Nov 14.

---

## 4. Pre-Decision Overlay (MANDATORY before R4/S4)

### For LONGS:
```
stock-profile TICKER
Evaluate:
  - Short interest: total %, fund count, trend (decreasing = positive)
  - Quality fund holders: which tracked funds hold? position size?
  - Insider activity: net buy/sell last 90 days, cluster buys?
  - Convergence: smart money aligned with thesis?

SIGNALS:
  SHORT_DECREASE + INSIDER_CLUSTER_BUY           -> STRONG BULLISH
  QUALITY_FUND_NEW + LOW_SHORT + INSIDER_BUY     -> QUIET ACCUMULATION
  HIGH_SHORT + QUALITY_FUND_HOLDS + INSIDER_BUY  -> CONTROVERSY (deep dive)
```

### For SHORTS:
```
stock-profile TICKER
Evaluate:
  - Who is long: quality funds holding = RED FLAG (they see value we don't)
  - Short crowding: already 10%+ = squeeze risk
  - Insider signal: insiders buying = STRONG contrary signal

SIGNALS:
  SHORT_INCREASE + INSIDER_SELL + FUND_EXIT      -> STRONG BEARISH (supports short)
  QUALITY_FUND_HOLDS + INSIDER_BUY               -> DO NOT SHORT (smart money disagrees)
```

---

## 5. Data Source Coverage

### Current (Phase 1 — implemented)
| Source | Regulator | Countries | Cadence | Status |
|--------|-----------|-----------|---------|--------|
| FCA UK Shorts | FCA | UK | 3 days | ACTIVE |
| AMF France Shorts | AMF | France | 3 days | ACTIVE |
| SEC 13F Holdings | SEC | US | 90 days | ACTIVE |
| SEC Form 4 Insider | SEC | US | 30 days | CODE EXISTS, NEEDS TESTING |
| yfinance Insider | yfinance | US | on-demand | ACTIVE |

### Next (Phase 2 — when stocks near entry)
| Source | Regulator | Countries | Relevant Tickers |
|--------|-----------|-----------|-------------------|
| AFM Netherlands | AFM | NL | REN.AS (R2), WKL.AS (committee) |
| CONSOB Italy | CONSOB | IT | RACE.MI (SO active) |
| BaFin Germany | BaFin | DE | DTE.DE (portfolio) |

### Later (Phase 3+)
| Source | Description | Value |
|--------|-------------|-------|
| UK Director Dealings | Investegate.co.uk scraping | UK insider buys (MONY, DOM, AUTO, BYIT, IHP) |
| 13D/13G Activist | SEC filings | Activist positions >5% |
| Fund Letters | Fundsmith, Pershing Square, etc. | Thesis intelligence |
| CNMV Spain | Spanish shorts | When .MC stocks near entry |
| FINMA Switzerland | Swiss shorts | When .SW stocks near entry |

---

## 6. Analytics That Become Possible (post mass enrollment)

### Convergence Signals
```
SHORT_DECREASE + INSIDER_CLUSTER_BUY           -> STRONG BULLISH
QUALITY_FUND_NEW + LOW_SHORT + INSIDER_BUY     -> QUIET ACCUMULATION
SHORT_INCREASE + INSIDER_SELL + FUND_EXIT      -> STRONG BEARISH
HIGH_SHORT + QUALITY_FUND_HOLDS + INSIDER_BUY  -> CONTROVERSY (deep dive)
```

### Crowding Risk
```
3+ tracked funds hold same stock + our position -> monitor for synchronized unwind
High short interest + multiple funds short      -> squeeze risk if catalyst positive
```

### Contrarian Signals
```
We hold + smart money exiting                   -> THESIS CHECK (are we wrong?)
We avoid + smart money accumulating             -> SCREENING OPPORTUNITY
Smart money convergence on stock we don't own   -> R1 CANDIDATE
```

### Fund Behavior Patterns (requires 3+ quarters of 13F data)
```
Fund X consistently accumulates before earnings -> follow-on signal
Fund Y reduces before regulatory events         -> risk signal
Cluster of quality funds entering same sector    -> sector rotation signal
```

---

## 7. Graph Maintenance

### Health Metrics (check via `stats`)
| Metric | Healthy | Warning | Action |
|--------|---------|---------|--------|
| Nodes | >100 | <50 | Enroll more stocks |
| Edges | >200 | <100 | Ingest more data |
| Coverage (portfolio) | 100% | <80% | Resolve missing identifiers |
| Staleness (FCA/AMF) | <5 days | >7 days | Download + ingest |
| Staleness (13F) | <100 days | >120 days | Download + ingest |

### Deduplication
Run `dedup-funds` after each FCA/AMF ingest to merge duplicate fund nodes.
Maintain `fund_aliases.yaml` when new duplicates are discovered.

### Garbage Collection
Run `gc` quarterly. Keeps last snapshot per quarter, removes raw files >180 days old.

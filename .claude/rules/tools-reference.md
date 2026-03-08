# Tools Reference

> Auto-loaded. Tools outputan DATOS CRUDOS. No juicios ni recomendaciones.
> Todos incluyen FX fallback warning.

---

## Core Tools

| Tool | Comando | Proposito |
|------|---------|-----------|
| `price_checker.py` | `python3 tools/price_checker.py TICKER1 TICKER2` | Precios via yfinance. UNICA fuente. NUNCA WebSearch. |
| `portfolio_stats.py` | `python3 tools/portfolio_stats.py` | P&L long+short, net/gross exposure, allocation. NUNCA a mano. |
| `effectiveness_tracker.py` | `python3 tools/effectiveness_tracker.py [--summary]` | Win rate, hit rate, Sharpe, attribution. Cada sesion. |
| `quality_scorer.py` | `python3 tools/quality_scorer.py TICKER [--detailed\|--raw]` | Quality Profile + Legacy Score. TOOL-FIRST. |
| `forward_return.py` | `python3 tools/forward_return.py [--active-only\|--pipeline-only\|--deployment-ready\|--basket]` | MoS%, Growth%, Yield%, E[CAGR]@market por posicion. `--deployment-ready` filtra pipeline a E[CAGR]>=threshold. `--basket` agrupa por basket tematico. |
| `quality_universe.py` | `python3 tools/quality_universe.py {report\|actionable\|add\|stale\|coverage\|stats\|archive\|approaching} [--fragility]` | Capital deployment machine. Universe. `approaching`=stocks moving toward entry (delta tracking). |
| `r1_prioritizer.py` | `python3 tools/r1_prioritizer.py [--top N] [--exclude-uk] [--near-entry-only] [--tier-a-only] [--exclude-fantasy-risk] [--pre-flight] [--advancement] [--buyable-now] [--smart-money]` | R1 prioritizer + fantasy gates. `--advancement`=3-section pipeline with E[CAGR]@mkt. `--buyable-now`=reverse mode: what's buyable at market today. `--smart-money`=SM overlay column (IC/CV/QA/FC/HW/SE/SQ signals from graph). Fantasy rate in footer. |
| `constraint_checker.py` | `python3 tools/constraint_checker.py {REPORT\|CHECK TICKER AMT\|CHECK_SHORT TICKER AMT} [--baskets]` | Concentracion, net/gross exposure, drawdown. `--baskets` adds basket concentration. Contexto, no juicio. |
| `correlation_matrix.py` | `python3 tools/correlation_matrix.py` | Correlaciones entre posiciones. |
| `insider_tracker.py` | `python3 tools/insider_tracker.py TICKER [--sections insider,institutional,short,analyst]` | Insider txns, institutional holders, short interest, analyst consensus. Datos crudos. |
| `portfolio_cagr.py` | `python3 tools/portfolio_cagr.py [--verbose] [--no-universe] [--baskets]` | Portfolio E[CAGR] projector. Cash drag, position ranking, market buy candidates, rotation candidates. `--baskets` adds basket breakdown. Run EVERY session P1. |
| `da_calibrator.py` | `python3 tools/da_calibrator.py [--detail]` | DA accuracy interim check. Current prices vs pre/post-DA FVs. Systematic conservatism detection. |
| `outcome_tracker.py` | `python3 tools/outcome_tracker.py [--active-only]` | Buy decision outcome tracker. P&L, days held, win rate for active + closed positions. |
| `basket_dashboard.py` | `python3 tools/basket_dashboard.py [--metrics\|--rotation\|--health\|--rebalance\|--lifecycle]` | Thematic basket aggregation. Metrics, health flags, rotation, allocation vs targets. `--lifecycle` = v4.8 integrity checks (MISLABELED, STAGNANT, NO_PATH, DEATH_WATCH, DEADLINE). |
| `kc_monitor.py` | `python3 tools/kc_monitor.py [--triggered-only\|--ticker TICKER\|--compact]` | Kill condition monitor. Parses KCs from thesis files, shows status dashboard. `--compact` = one-line-per-ticker for session use. Run EVERY session Fase 0. |

## Screening & Valuation

| Tool | Comando | Proposito |
|------|---------|-----------|
| `dynamic_screener.py` | `python3 tools/dynamic_screener.py --index {sp500\|us_all\|europe_all\|...}` | Screening programatico. Anti-bias. `--undiscovered` para small/mid. |
| `batch_scorer.py` | `python3 tools/batch_scorer.py --index {sp500\|...} [--new-only] [--add-to-universe] [--dry-run]` | Mass QS scoring de indices enteros. Discovery. Auto-add a universe. |
| `dcf_calculator.py` | `python3 tools/dcf_calculator.py TICKER [--scenarios] [--sensitivity] [--reverse]` | DCF + scenarios + sensitivity. --reverse = implied expectations (solve for growth). |
| `narrative_checker.py` | `python3 tools/narrative_checker.py TICKER` | Tendencias financieras (margins, R&D, SBC, receivables, FCF). Datos crudos. |
| `opportunity_filter.py` | `python3 tools/opportunity_filter.py --csv FILE [--roic-min N]` | Stage 2 sobre CSV de screener. ROIC, FCF margin, rev CAGR. |

## Fallen Angels & Special Situations

| Tool | Comando | Proposito |
|------|---------|-----------|
| `fallen_angels.py` | `python3 tools/fallen_angels.py [--min-qs 60] [--min-drawdown -35]` | Quality companies at trough. Finds QS>=55 stocks fallen >30% from 52wH with ROIC still positive. Anti-complacency: surfaces opportunities the standard screener misses. |

## Macro & Risk

| Tool | Comando | Proposito |
|------|---------|-----------|
| `macro_fragility.py` | `python3 tools/macro_fragility.py {world\|country CODE\|sector NAME\|full}` | 3-layer macro data: world (VIX, yields, gold, oil, DXY, S&P), country (index, FX, ETF, sector ETFs), sector (ETFs, P/E, top holdings). Datos crudos. |

## Smart Money & Institutional

| Tool | Comando | Proposito |
|------|---------|-----------|
| `smart_money.py` | `python3 tools/smart_money.py {signals\|discover\|discover-funds\|sector-overlay\|capture\|ingest-live\|ingest-consob\|ingest-afm-nl\|refresh\|resolve\|ingest-fca\|ingest-amf\|ingest-13f\|ingest-insider\|coverage\|enroll\|stale\|download\|sync-portfolio\|report\|stock-profile\|who-holds\|crowding\|alerts\|metrics\|communities\|visualize\|snapshot\|stats\|gc}` | Grafo v4.1 Self-Growing OSINT Engine. `signals [--portfolio-only\|--ticker T]` = detect actionable patterns. `discover [--source 13f\|fca\|amf] [--min-funds N]` = anti-bias discovery. `discover-funds [--min-stocks N] [--auto-enroll]` = find untracked funds; `--auto-enroll` adds CIK funds + downloads 13F (max 5). `capture TEXT` = quick natural-language ingest ("Elliott holds 5.2% LULU", "CEO X bought 2.5M ADBE"). `sector-overlay SECTOR` = institutional positioning for sector views. `refresh [--expand\|--full\|--skip-download]` = one-command refresh; `--expand` auto-discovers+enrolls new stocks. `resolve [--retry-failed\|--force]` = identifier resolution. `ingest-insider [--universe\|--all-enrolled]` = insider data. `ingest-live --type {holder\|short\|insider\|mention} --fund F --ticker T [--data JSON]` = session intelligence (use `capture` for quick input). `ingest-13f` = 13F holdings with unresolved CUSIP logging + enhanced CUSIP resolution. `ingest-consob` / `ingest-afm-nl` = IT/NL shorts. `download {fca\|amf\|consob\|afm-nl\|shorts\|13f\|form4\|all}` = data acquisition. `gc` = prune old files + island nodes. `stock-profile TICKER` = mandatory pre-decision. Datos raw — Claude interpreta. |

## Sector Health & Consistency

| Tool | Comando | Proposito |
|------|---------|-----------|
| `sector_health.py` | `python3 tools/sector_health.py {freshness\|coverage\|cascade\|changes\|snapshot\|macro-map}` | Staleness, coverage, cascades, macro deps de sector views. `freshness --stale-only` para alertas. Weekly obligatorio. |
| `consistency_checker.py` | `python3 tools/consistency_checker.py "BUY TICKER N%"` | Compara vs precedentes (decisions_log). ANTES de decisiones. |
| `drift_detector.py` | `python3 tools/drift_detector.py [--verbose]` | Detecta sizing drift, conviction inflation. Cada 14 dias. |
| `system_projection.py` | `python3 tools/system_projection.py [--additions N]` | Monte Carlo 1-10 anos. Fat tails. |

## Indices Disponibles (dynamic_screener / batch_scorer)

US: `sp500`, `sp400`, `russell1000`, `us_all` | EU: `dax40`, `cac40`, `ftse100`, `ftse250`, `stoxx600`, `europe_all`, `nordic` | Otros: `mib40`, `ibex35`, `aex25`, `nikkei225`

## Countries Disponibles (macro_fragility)

`US`, `UK`, `DE`, `FR`, `JP`, `IT`, `ES`, `DK`, `EU`

## Sectors Disponibles (macro_fragility)

`technology`, `healthcare`, `financials`, `energy`, `industrials`, `consumer discretionary`, `consumer staples`, `utilities`, `real estate`, `materials`, `communication`, `semiconductors`, `defense`, `insurance`, `payments`, `biotech`, `pharma`, `luxury`, `telecom`

## Reglas

1. SIEMPRE tools antes de calculos inline
2. Calculo repetido >1x → crear tool (`quant-tools-dev`)
3. Precios SOLO via `price_checker.py`
4. Screening SOLO via `dynamic_screener.py` (screener.py/midcap_screener.py DEPRECATED)
5. Mass QS scoring via `batch_scorer.py` (NOT quality_scorer.py in loop)
6. yfinance: max ~50 tickers/sesion, max 2 agentes yfinance en paralelo

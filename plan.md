# Plan: Smart Money Graph — Implementacion Completa

## Resumen

Construir un sistema de inteligencia "Smart Money" integrado en el sistema de inversion. Captura señales institucionales, short disclosures, insiders, y fund letters desde fuentes publicas gratuitas. Persiste un grafo en disco, genera alertas accionables cada sesion, y produce un HTML interactivo para el humano.

---

## Arquitectura

```
tools/smart_money/
├── scrapers/
│   ├── fca_shorts.py         # UK short positions (XLSX download directo)
│   ├── amf_shorts.py         # France short positions (CSV data.gouv.fr)
│   ├── sec_13f.py            # US institutional holdings (ZIP/TSV EDGAR)
│   ├── sec_form4.py          # US insider transactions (ZIP/TSV EDGAR)
│   └── fund_letters.py      # Top fund quarterly letters (WebFetch)
├── graph/
│   ├── builder.py            # Construye/actualiza el grafo NetworkX
│   ├── signals.py            # Calcula metricas y detecta cambios
│   └── correlation.py        # Capa de correlaciones (evoluciona correlation_matrix.py)
├── visualize.py              # Genera HTML interactivo con pyvis
├── smart_money.py            # CLI principal: python3 tools/smart_money/smart_money.py
└── data/
    ├── graph.gpickle          # Grafo persistido
    ├── shorts/                # Snapshots de short positions
    ├── holdings/              # Snapshots de 13F
    ├── insiders/              # Insider transactions historico
    └── snapshots/             # Grafo snapshots para diff temporal
```

---

## Fases de Implementacion (esta sesion)

### Fase 1: Infraestructura base + Scrapers "faciles"
**Archivos:** `smart_money.py`, `graph/builder.py`, `scrapers/fca_shorts.py`, `scrapers/amf_shorts.py`

1. **CLI principal** (`smart_money.py`):
   - `python3 tools/smart_money/smart_money.py --alerts` → alertas para mis posiciones + pipeline
   - `python3 tools/smart_money/smart_money.py TICKER --full` → todo sobre un ticker
   - `python3 tools/smart_money/smart_money.py --update` → re-scrapeear fuentes y actualizar grafo
   - `python3 tools/smart_money/smart_money.py --visualize` → generar HTML interactivo
   - `python3 tools/smart_money/smart_money.py --stale` → que datos necesitan refresh
   - Output style: mismo formato que tools existentes (boxed sections, columnar, footer raw data)

2. **Graph builder** (`graph/builder.py`):
   - Grafo NetworkX multicapa persistido en pickle
   - Nodos: tickers (activos) + instituciones/fondos + personas (insiders)
   - Aristas tipadas: SHORT_POSITION, HOLDING_13F, INSIDER_BUY, INSIDER_SELL, CORRELATION, FUND_MENTION
   - Cada arista con timestamp + valor + fuente
   - Load/save con versionado temporal (mantener ultimos 4 snapshots para diff)

3. **FCA shorts scraper** (`scrapers/fca_shorts.py`):
   - GET `https://www.fca.org.uk/publication/data/short-positions-daily-update.xlsx`
   - Parse con pandas.read_excel()
   - Filtrar por ISINs de mis posiciones UK (MONY.L, AUTO.L, DOM.L, BYIT.L, IHP.L)
   - Retornar: [{holder, ticker, position_pct, date}]

4. **AMF shorts scraper** (`scrapers/amf_shorts.py`):
   - GET `https://www.data.gouv.fr/api/1/datasets/r/c2539d1c-8531-4937-9cba-3bd8e9786cc5`
   - Parse CSV con pandas
   - Filtrar por ISINs de posiciones FR (EDEN.PA)
   - Retornar mismo formato

### Fase 2: SEC EDGAR (13F + Form 4)
**Archivos:** `scrapers/sec_13f.py`, `scrapers/sec_form4.py`

5. **13F scraper** (`scrapers/sec_13f.py`):
   - Descargar ultimo quarterly ZIP de `https://www.sec.gov/files/dera/data/form-13f/`
   - Parse INFOTABLE.tsv: issuer, CUSIP, value, shares por filer
   - Mapear CUSIP → ticker (mantener tabla de mapeo para mis posiciones US: ADBE, GL, NVO, LULU, MORN)
   - Calcular: cuantos fondos tienen cada posicion, cambios vs trimestre anterior
   - Crowding score = num_holders * avg_position_pct

6. **Form 4 scraper** (`scrapers/sec_form4.py`):
   - Descargar ultimo quarterly ZIP de insider transactions
   - Parse NONDERIV_TRANS.tsv: insider name, ticker, buy/sell, shares, price, date
   - Filtrar por tickers US del portfolio + pipeline
   - Detectar patrones: cluster buys (3+ insiders en 30 dias), large purchases (>$100K)

### Fase 3: Señales y metricas del grafo
**Archivos:** `graph/signals.py`, `graph/correlation.py`

7. **Signals engine** (`graph/signals.py`):
   - Para cada ticker en portfolio + pipeline, calcular:
     - short_pressure: suma de short positions conocidas + delta vs snapshot anterior
     - insider_sentiment: ratio buy/sell ponderado por monto en ultimos 90 dias
     - crowding_score: num fondos 13F con posicion / mediana del universo
     - smart_money_consensus: direccion agregada de fondos con mejor track record historico
   - Detectar ALERTAS:
     - SHORT_INCREASE: short position sube >0.3pp vs ultimo snapshot
     - SHORT_DECREASE: baja >0.3pp (bullish signal)
     - INSIDER_CLUSTER_BUY: 3+ insiders compran en 30 dias
     - INSIDER_LARGE_SELL: venta >$500K por un insider
     - CROWDING_HIGH: >15 fondos top comparten posicion
     - CONVERGENCE: insider buy + short decrease = señal fuerte

8. **Correlation layer** (`graph/correlation.py`):
   - Evolucion de correlation_matrix.py existente
   - Calcular rolling correlations (60d window) entre posiciones
   - Detectar cambios estructurales: par que pasa de baja a alta correlacion
   - Añadir aristas CORRELATION al grafo

### Fase 4: Visualizacion HTML
**Archivo:** `visualize.py`

9. **Generador HTML con pyvis:**
   - Nodos coloreados por tipo: azul=ticker, verde=fondo/institucion, naranja=insider
   - Tamaño de nodo por centralidad (degree o PageRank)
   - Aristas coloreadas por tipo: rojo=short, verde=holding, amarillo=insider_buy
   - Hover tooltip con metricas clave del nodo
   - Filtro por capa (solo shorts, solo holdings, solo insiders)
   - Output: `data/smart_money_graph.html` — abrir en browser
   - Se regenera con `--visualize` flag

### Fase 5: Smart staleness + auto-trigger
**Integrado en:** `smart_money.py`

10. **Staleness detection:**
    - Cada fuente tiene cadencia natural:
      - FCA/AMF shorts: refresh si >3 dias
      - 13F: refresh si nuevo trimestre disponible
      - Form 4: refresh si >7 dias
      - Correlations: refresh si >7 dias
    - `--stale` muestra que necesita refresh
    - `--update` solo refresca lo stale (no todo)
    - Yo (Claude) ejecuto `--stale` en Fase 0 de cada sesion
    - Si algo critico stale (shorts de posicion activa >5 dias), lo refresco automaticamente

### Fase 6: Fund Letters (stretch goal si queda tiempo)
**Archivo:** `scrapers/fund_letters.py`

11. **Fund letter parser:**
    - Lista de URLs conocidas de cartas trimestrales (Greenlight, Pershing Square, etc.)
    - WebFetch + extraccion de tickers mencionados + sentiment
    - Añadir aristas FUND_MENTION al grafo
    - Esto es la parte mas fragil — URLs cambian, formato varia. MVP pragmatico.

---

## Integracion con mi operativa

```
Fase 0 (cada sesion):
  → python3 tools/smart_money/smart_money.py --stale
  → Si stale critico: python3 tools/smart_money/smart_money.py --update
  → python3 tools/smart_money/smart_money.py --alerts
  → Alertas se incorporan a vigilancia

R1/Re-eval (por ticker):
  → python3 tools/smart_money/smart_money.py TICKER --full
  → Contexto institucional alimenta analisis

Visualizacion (cuando humano quiere ver):
  → python3 tools/smart_money/smart_money.py --visualize
  → Abre data/smart_money_graph.html en browser
```

---

## Dependencias nuevas

```bash
pip install pyvis openpyxl
# pyvis: visualizacion HTML interactiva
# openpyxl: leer XLSX de FCA
# requests, pandas, networkx: ya disponibles o stdlib-adjacent
```

Verificar que `requests`, `networkx`, `pandas` estan instalados (probable pero confirmar).

---

## Que NO hago

- No BaFin/CNMV (scraping complejo, Selenium, bajo ROI vs FCA/AMF)
- No NLP de earnings calls (redundante con mi analisis fundamental)
- No job postings de hedge funds (demasiado ruido)
- No dashboard Dash con servidor (pyvis HTML estatico cubre la necesidad visual)
- No trading automatico basado en señales del grafo

---

## Orden de construccion en esta sesion

1. Infraestructura: CLI + graph builder + persistencia
2. FCA shorts scraper (mi posicion mas relevante: 5 UK stocks)
3. AMF shorts scraper (EDEN.PA)
4. SEC 13F scraper (US stocks: ADBE, GL, NVO, LULU, MORN)
5. SEC Form 4 scraper (insiders US)
6. Signals engine (alertas y metricas)
7. Correlation layer
8. Visualizacion pyvis
9. Staleness + integracion operativa
10. Fund letters (si queda tiempo)

Cada fase produce algo usable. Si se corta en fase 5, ya tengo shorts EU + 13F + insiders + alertas.

---

## Riesgos y mitigacion

| Riesgo | Mitigacion |
|--------|-----------|
| FCA cambia URL del XLSX | Fallback: WebSearch para encontrar nueva URL. Alertar en --stale |
| AMF CSV formato cambia | Schema validation al parsear. Alertar si columnas no coinciden |
| EDGAR rate limit (10 req/sec) | Sleep entre requests. Cache local agresivo |
| Grafo crece demasiado | Podar nodos sin conexion a portfolio/pipeline cada 90 dias |
| pyvis no instalado | Graceful degradation: skip visualizacion, todo lo demas funciona |

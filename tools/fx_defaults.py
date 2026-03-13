# FX fallback rates — used when yfinance is unavailable.
# Single source of truth. All tools import from here.

FX_DEFAULTS = {
    "EURUSD": 1.16,
    "GBPEUR": 1.15,
    "DKKEUR": 0.134,
    "USDEUR": 1 / 1.16,
}

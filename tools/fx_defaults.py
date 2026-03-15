# FX fallback rates — used when yfinance is unavailable.
# Single source of truth. All tools import from here.

FX_DEFAULTS = {
    "EURUSD": 1.16,
    "GBPEUR": 1.15,
    "GBPUSD": 1.34,     # GBP/USD = GBPEUR × EURUSD ≈ 1.15 × 1.16 ≈ 1.334
    "CHFUSD": 1.10,     # CHF/USD ≈ EURUSD × 0.95 (CHF tracks EUR closely)
    "DKKEUR": 0.134,
    "USDEUR": 1 / 1.16,
}

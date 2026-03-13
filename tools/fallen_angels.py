#!/usr/bin/env python3
"""Fallen Angels Scanner — Quality companies trading 30%+ below 52-week high.

Reads quality_universe.yaml, filters by QS >= threshold, fetches 52-week high
and current price via yfinance, calculates drawdown, and shows ROIC.

Usage:
    python3 tools/fallen_angels.py
    python3 tools/fallen_angels.py --min-drawdown -40
    python3 tools/fallen_angels.py --min-qs 75
"""

import argparse
import sys
import yaml
import yfinance as yf

UNIVERSE_PATH = "state/quality_universe.yaml"


def load_candidates(min_qs):
    """Load tickers from quality_universe with qs >= min_qs."""
    with open(UNIVERSE_PATH, "r") as f:
        data = yaml.safe_load(f)
    companies = data.get("quality_universe", {}).get("companies", [])
    candidates = []
    for c in companies:
        qs = c.get("qs_adj") or c.get("qs_tool")
        if qs is None or qs < min_qs:
            continue
        candidates.append({
            "ticker": c["ticker"],
            "qs": qs,
            "tier": c.get("tier", "?"),
            "sector": c.get("sector", "Unknown"),
        })
    return candidates


def fetch_market_data(tickers, batch_size=50):
    """Fetch price, 52wH, ROIC for all tickers in batches."""
    results = {}
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i : i + batch_size]
        batch_str = " ".join(batch)
        try:
            data = yf.download(batch_str, period="1y", progress=False, threads=True)
        except Exception:
            continue
        tks = yf.Tickers(batch_str)
        for t in batch:
            try:
                if len(batch) == 1:
                    highs = data["High"]
                    closes = data["Close"]
                else:
                    highs = data["High"][t]
                    closes = data["Close"][t]
                high_52w = float(highs.max())
                current = float(closes.dropna().iloc[-1])
                # ROIC from info
                info = tks.tickers[t].info
                roic = info.get("returnOnCapital") or info.get("returnOnAssets")
                roic_pct = round(roic * 100, 1) if roic else None
                results[t] = {
                    "price": round(current, 2),
                    "high_52w": round(high_52w, 2),
                    "roic": roic_pct,
                }
            except Exception:
                continue
    return results


def main():
    parser = argparse.ArgumentParser(description="Fallen Angels Scanner")
    parser.add_argument("--min-drawdown", type=float, default=-30,
                        help="Min drawdown %% (default: -30, meaning -30%% or worse)")
    parser.add_argument("--min-qs", type=int, default=55,
                        help="Min Quality Score (default: 55)")
    args = parser.parse_args()

    candidates = load_candidates(args.min_qs)
    if not candidates:
        print(f"No companies with QS >= {args.min_qs} in universe.")
        sys.exit(0)

    print(f"Scanning {len(candidates)} companies (QS >= {args.min_qs})...")
    tickers = [c["ticker"] for c in candidates]
    market = fetch_market_data(tickers)

    # Build results with drawdown filter
    rows = []
    for c in candidates:
        t = c["ticker"]
        if t not in market:
            continue
        m = market[t]
        if m["high_52w"] == 0:
            continue
        dd = round((m["price"] - m["high_52w"]) / m["high_52w"] * 100, 1)
        if dd > args.min_drawdown:
            continue
        rows.append({
            "ticker": t,
            "qs": c["qs"],
            "tier": c["tier"],
            "drawdown": dd,
            "price": m["price"],
            "high_52w": m["high_52w"],
            "roic": m["roic"],
            "sector": c["sector"][:22],
        })

    rows.sort(key=lambda r: r["drawdown"])

    if not rows:
        print(f"\nNo fallen angels found (drawdown <= {args.min_drawdown}%, QS >= {args.min_qs}).")
        sys.exit(0)

    # Print table
    hdr = f"{'Ticker':<10} {'QS':>3} {'Tier':>4} {'DD%':>7} {'Price':>10} {'52wH':>10} {'ROIC%':>6} {'Sector':<22}"
    print(f"\n=== FALLEN ANGELS (DD <= {args.min_drawdown}%, QS >= {args.min_qs}) ===")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        roic_str = f"{r['roic']:>5.1f}" if r["roic"] is not None else "  N/A"
        print(f"{r['ticker']:<10} {r['qs']:>3} {r['tier']:>4} {r['drawdown']:>6.1f}% {r['price']:>10.2f} {r['high_52w']:>10.2f} {roic_str}% {r['sector']:<22}")
    print(f"\nTotal: {len(rows)} fallen angels from {len(candidates)} scanned.")


if __name__ == "__main__":
    main()

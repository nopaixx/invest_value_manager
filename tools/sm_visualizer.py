#!/usr/bin/env python3
"""
Smart Money Visualizer — Generates PNG charts from Smart Money graph data.

Produces 5 charts saved to reports/smart_money/images/:
  1. fund_network.png      — Quality Fund -> Portfolio network graph
  2. basket_conviction.png — Basket SM conviction bar chart
  3. short_interest_bars.png — Short interest by position
  4. coverage_heatmap.png  — SM data coverage matrix
  5. position_health.png   — Position health score dashboard

Usage:
  python3 tools/sm_visualizer.py                    # Generate all 5 charts
  python3 tools/sm_visualizer.py --chart fund_network
  python3 tools/sm_visualizer.py --chart basket_conviction
  python3 tools/sm_visualizer.py --chart short_interest
  python3 tools/sm_visualizer.py --chart coverage
  python3 tools/sm_visualizer.py --chart health
  python3 tools/sm_visualizer.py --chart all
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np
import json
import os
import sys
import subprocess
import argparse
import re
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Paths (relative to repo root)
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = REPO_ROOT / 'tools' / 'smart_money' / 'graph.json'
PORTFOLIO_PATH = REPO_ROOT / 'portfolio' / 'current.yaml'
BASKETS_PATH = REPO_ROOT / 'state' / 'thematic_baskets.yaml'
OUTPUT_DIR = REPO_ROOT / 'reports' / 'smart_money' / 'images'

# Pipeline tickers (entering / near-term buys)
PIPELINE_TICKERS = {'GDDY', 'DNLM.L', 'SPGI', 'BCG.L', 'CMCSA', 'ITRK.L'}

# Quality / value fund types we care about
QUALITY_FUND_TYPES = {'quality', 'value', 'activist'}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_graph():
    """Load NetworkX-serialized graph JSON."""
    with open(GRAPH_PATH) as f:
        return json.load(f)


def _parse_yaml_lightweight(path):
    """
    Minimal YAML parser for our specific files — avoids PyYAML dependency.
    Returns raw text. Use specific extractors below.
    """
    with open(path) as f:
        return f.read()


def extract_portfolio_tickers(text):
    """Extract active long + short tickers from current.yaml."""
    longs = []
    shorts = []
    in_positions = False
    in_shorts = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('positions:'):
            in_positions = True
            in_shorts = False
            continue
        if stripped.startswith('short_positions:'):
            in_shorts = True
            in_positions = False
            continue
        if stripped.startswith('transactions:'):
            in_positions = False
            in_shorts = False
            continue
        if (in_positions or in_shorts) and stripped.startswith('- ticker:'):
            ticker = stripped.split(':', 1)[1].strip().strip('"').strip("'")
            if in_positions:
                longs.append(ticker)
            else:
                shorts.append(ticker)
    return longs, shorts


def extract_portfolio_weights(text):
    """Extract intentional_weight per ticker."""
    weights = {}
    current_ticker = None
    in_positions = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('positions:'):
            in_positions = True
            continue
        if stripped.startswith('short_positions:') or stripped.startswith('transactions:'):
            in_positions = False
            continue
        if in_positions and stripped.startswith('- ticker:'):
            current_ticker = stripped.split(':', 1)[1].strip().strip('"').strip("'")
        if in_positions and current_ticker and 'intentional_weight:' in stripped:
            try:
                val = stripped.split(':', 1)[1].strip().split('#')[0].strip()
                weights[current_ticker] = float(val)
            except ValueError:
                pass
    return weights


def extract_baskets(text):
    """Extract basket id, name, status, positions, pipeline from thematic_baskets.yaml."""
    baskets = []
    current = None
    in_positions = False
    in_pipeline = False
    in_entering = False
    in_killed = False

    for line in text.splitlines():
        stripped = line.strip()

        if stripped.startswith('killed_baskets:'):
            in_killed = True
            if current:
                baskets.append(current)
                current = None
            continue

        if in_killed:
            continue

        if stripped.startswith('- id:') and not in_killed:
            if current:
                baskets.append(current)
            current = {
                'id': stripped.split(':', 1)[1].strip(),
                'name': '',
                'status': '',
                'positions': [],
                'pipeline': [],
                'entering': [],
            }
            in_positions = False
            in_pipeline = False
            in_entering = False
            continue

        if current is None:
            continue

        if stripped.startswith('name:'):
            current['name'] = stripped.split(':', 1)[1].strip().strip('"')
        elif stripped.startswith('status:'):
            current['status'] = stripped.split(':', 1)[1].strip().split('#')[0].strip()
        elif stripped.startswith('positions:'):
            in_positions = True
            in_pipeline = False
            in_entering = False
        elif stripped.startswith('entering:'):
            in_entering = True
            in_positions = False
            in_pipeline = False
        elif stripped.startswith('pipeline:'):
            in_pipeline = True
            in_positions = False
            in_entering = False
        elif stripped.startswith('shared_risks:') or stripped.startswith('kill_conditions:') or \
             stripped.startswith('vitality_signals:') or stripped.startswith('thesis:') or \
             stripped.startswith('thesis_file:') or stripped.startswith('sector_views:') or \
             stripped.startswith('last_reviewed:') or stripped.startswith('created:') or \
             stripped.startswith('notes:') or stripped.startswith('theme_vitality:'):
            in_positions = False
            in_pipeline = False
            in_entering = False
        elif stripped.startswith('- ') and not stripped.startswith('- id:'):
            ticker = stripped.lstrip('- ').split('#')[0].strip()
            if ticker and len(ticker) < 12:
                if in_positions:
                    current['positions'].append(ticker)
                elif in_pipeline:
                    current['pipeline'].append(ticker)
                elif in_entering:
                    current['entering'].append(ticker)

    if current:
        baskets.append(current)

    return baskets


def _empty_chart(ax, msg):
    """Draw 'No data' message on an empty chart."""
    ax.text(0.5, 0.5, msg, ha='center', va='center', fontsize=16, color='gray',
            transform=ax.transAxes)
    ax.set_xticks([])
    ax.set_yticks([])


# ---------------------------------------------------------------------------
# Chart 1: Fund Network
# ---------------------------------------------------------------------------

def chart_fund_network(graph_data, portfolio_tickers, short_tickers, weights):
    """Quality Fund -> Portfolio network visualization."""
    try:
        import networkx as nx
    except ImportError:
        print("  [SKIP] networkx not installed. Skipping fund_network.")
        return None

    nodes_by_id = {n['id']: n for n in graph_data['nodes']}

    all_portfolio = set(portfolio_tickers + short_tickers)
    all_relevant = all_portfolio | PIPELINE_TICKERS

    # Find quality/value funds that hold or short our tickers
    fund_edges = []
    for e in graph_data['edges']:
        src = e.get('source', '')
        tgt = e.get('target', '')
        rel = e.get('relation', '')
        src_node = nodes_by_id.get(src, {})

        # Fund -> Stock edges where stock is in our portfolio/pipeline
        if src_node.get('type') == 'fund' and tgt in all_relevant and rel == 'holds':
            ft = src_node.get('fund_type', 'unknown')
            if ft in QUALITY_FUND_TYPES:
                pct = e.get('pct_portfolio', e.get('pct_shares', ''))
                fund_edges.append((src, tgt, pct, src_node.get('full_name', src)))

    if not fund_edges:
        fig, ax = plt.subplots(figsize=(16, 12))
        _empty_chart(ax, "No quality/value fund holdings found\nfor portfolio tickers")
        return fig

    G = nx.DiGraph()

    # Count connections per fund
    fund_conn = defaultdict(int)
    for src, tgt, pct, name in fund_edges:
        fund_conn[src] += 1

    # Add nodes and edges
    for src, tgt, pct, name in fund_edges:
        if not G.has_node(src):
            G.add_node(src, node_type='fund', label=name)
        if not G.has_node(tgt):
            if tgt in set(portfolio_tickers):
                G.add_node(tgt, node_type='portfolio', label=tgt)
            elif tgt in set(short_tickers):
                G.add_node(tgt, node_type='short', label=tgt)
            elif tgt in PIPELINE_TICKERS:
                G.add_node(tgt, node_type='pipeline', label=tgt)
        label = f"{pct}%" if pct else ""
        G.add_edge(src, tgt, label=label)

    fig, ax = plt.subplots(figsize=(16, 12))
    fig.patch.set_facecolor('white')

    pos = nx.spring_layout(G, k=2.5, iterations=50, seed=42)

    # Separate node lists
    fund_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'fund']
    port_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'portfolio']
    pipe_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'pipeline']
    short_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'short']

    # Sizes
    fund_sizes = [300 + fund_conn.get(n, 1) * 200 for n in fund_nodes]
    port_sizes = [300 + weights.get(n, 5) * 60 for n in port_nodes]
    pipe_sizes = [300 for _ in pipe_nodes]
    short_sizes = [300 for _ in short_nodes]

    # Draw edges
    nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.3, arrows=True,
                           arrowstyle='->', arrowsize=12, edge_color='#888888')

    # Draw nodes
    if fund_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=fund_nodes, node_size=fund_sizes,
                               node_color='#4A90D9', node_shape='o', alpha=0.85, ax=ax)
    if port_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=port_nodes, node_size=port_sizes,
                               node_color='#27AE60', node_shape='s', alpha=0.85, ax=ax)
    if pipe_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=pipe_nodes, node_size=pipe_sizes,
                               node_color='#E67E22', node_shape='D', alpha=0.85, ax=ax)
    if short_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=short_nodes, node_size=short_sizes,
                               node_color='#E74C3C', node_shape='v', alpha=0.85, ax=ax)

    # Labels
    labels = {}
    for n, d in G.nodes(data=True):
        lbl = d.get('label', n)
        # Shorten fund names
        if d.get('node_type') == 'fund':
            parts = lbl.split()
            lbl = ' '.join(parts[:2]) if len(parts) > 2 else lbl
        labels[n] = lbl

    nx.draw_networkx_labels(G, pos, labels, font_size=7, font_weight='bold', ax=ax)

    # Edge labels (holding %)
    edge_labels = nx.get_edge_attributes(G, 'label')
    edge_labels = {k: v for k, v in edge_labels.items() if v}
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=6,
                                     font_color='#555555', ax=ax)

    # Legend
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#4A90D9',
               markersize=12, label='Quality/Value Fund'),
        Line2D([0], [0], marker='s', color='w', markerfacecolor='#27AE60',
               markersize=12, label='Portfolio Position'),
        Line2D([0], [0], marker='D', color='w', markerfacecolor='#E67E22',
               markersize=10, label='Pipeline Candidate'),
        Line2D([0], [0], marker='v', color='w', markerfacecolor='#E74C3C',
               markersize=10, label='Short Position'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.9)

    ax.set_title("Smart Money Network -- Quality Fund Holdings in Portfolio",
                 fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    return fig


# ---------------------------------------------------------------------------
# Chart 2: Basket SM Conviction
# ---------------------------------------------------------------------------

def chart_basket_conviction(graph_data, baskets, portfolio_tickers):
    """Basket-level Smart Money conviction bar chart."""
    edges = graph_data['edges']

    # Count convergence + insider signals per ticker
    ticker_signals = defaultdict(int)
    for e in edges:
        tgt = e.get('target', '')
        rel = e.get('relation', '')
        if rel == 'holds':
            ticker_signals[tgt] += 1
        elif rel == 'insider_buy':
            ticker_signals[tgt] += 2  # Weight insider buys higher
        elif rel == 'insider_sell':
            ticker_signals[tgt] -= 1  # Slight negative

    # Aggregate per basket
    basket_names = []
    basket_scores = []
    basket_colors = []

    active_baskets = [b for b in baskets if b['status'] in ('ACTIVE', 'RESEARCHING', 'DEATH_WATCH')]

    for b in active_baskets:
        all_tickers = b['positions'] + b.get('entering', []) + b.get('pipeline', [])
        score = sum(ticker_signals.get(t, 0) for t in all_tickers)
        basket_names.append(b['name'])
        basket_scores.append(max(score, 0))

        if score >= 10:
            basket_colors.append('#27AE60')  # Strong
        elif score >= 3:
            basket_colors.append('#F39C12')  # Moderate
        else:
            basket_colors.append('#E74C3C')  # Limited

    if not basket_names:
        fig, ax = plt.subplots(figsize=(12, 6))
        _empty_chart(ax, "No basket data available")
        return fig

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('white')

    y_pos = range(len(basket_names))
    bars = ax.barh(y_pos, basket_scores, color=basket_colors, edgecolor='white',
                   height=0.6, alpha=0.85)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(basket_names, fontsize=10)
    ax.set_xlabel('SM Signal Score (holds + insider buys - insider sells)', fontsize=10)

    # Annotations
    for i, (bar, score) in enumerate(zip(bars, basket_scores)):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
                f'{score}', va='center', fontsize=10, fontweight='bold')

    # Legend
    legend_elements = [
        mpatches.Patch(color='#27AE60', label='Strong (>=10)'),
        mpatches.Patch(color='#F39C12', label='Moderate (3-9)'),
        mpatches.Patch(color='#E74C3C', label='Limited (<3)'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    ax.set_title("Basket Smart Money Conviction", fontsize=14, fontweight='bold', pad=15)
    ax.grid(axis='x', alpha=0.3)
    ax.invert_yaxis()

    return fig


# ---------------------------------------------------------------------------
# Chart 3: Short Interest Bars
# ---------------------------------------------------------------------------

def chart_short_interest(graph_data, portfolio_tickers, short_tickers):
    """Short interest % per portfolio position."""
    nodes_by_id = {n['id']: n for n in graph_data['nodes']}
    edges = graph_data['edges']

    all_tickers = portfolio_tickers + short_tickers

    # Collect SI data from graph nodes (short_pct_float field)
    si_data = {}
    for t in all_tickers:
        node = nodes_by_id.get(t, {})
        si = node.get('short_pct_float', 0)
        if si:
            si_data[t] = si

    # Also aggregate from 'shorts' edges (sum of pct_shares per ticker)
    si_from_edges = defaultdict(float)
    for e in edges:
        if e.get('relation') == 'shorts' and e.get('target') in all_tickers:
            si_from_edges[e['target']] = max(si_from_edges[e['target']],
                                              e.get('pct_shares', 0))

    # Merge: prefer node-level SI, fallback to edge sum
    merged = {}
    for t in all_tickers:
        if t in si_data and si_data[t] > 0:
            merged[t] = si_data[t]
        elif t in si_from_edges:
            merged[t] = si_from_edges[t]

    if not merged:
        fig, ax = plt.subplots(figsize=(12, 6))
        _empty_chart(ax, "No short interest data available")
        return fig

    # Sort by SI descending
    sorted_tickers = sorted(merged.keys(), key=lambda x: merged[x], reverse=True)
    values = [merged[t] for t in sorted_tickers]

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('white')

    colors = []
    for t in sorted_tickers:
        if t == 'EDEN.PA':
            colors.append('#C0392B')  # Highlighted
        elif t in short_tickers:
            colors.append('#8E44AD')  # Our short
        else:
            colors.append('#E74C3C')

    y_pos = range(len(sorted_tickers))
    bars = ax.barh(y_pos, values, color=colors, edgecolor='white', height=0.6, alpha=0.85)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_tickers, fontsize=10, fontweight='bold')
    ax.set_xlabel('Short Interest %', fontsize=10)

    # Annotations
    for i, (bar, val) in enumerate(zip(bars, values)):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                f'{val:.1f}%', va='center', fontsize=9, fontweight='bold')

    # Special annotation for EDEN.PA
    if 'EDEN.PA' in merged:
        eden_idx = sorted_tickers.index('EDEN.PA')
        # Place annotation to the right of the bar, offset vertically
        ax.annotate('9.38% actual (AMF) vs 23.5% display (stale)',
                     xy=(merged['EDEN.PA'] + 0.3, eden_idx),
                     xytext=(max(values) * 0.5, eden_idx + 1.2),
                     fontsize=8, color='#C0392B', fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.2))

    # Legend
    legend_elements = [
        mpatches.Patch(color='#E74C3C', label='Long position SI'),
        mpatches.Patch(color='#C0392B', label='EDEN.PA (highlighted)'),
        mpatches.Patch(color='#8E44AD', label='Our short position'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    ax.set_title("Portfolio Short Interest Exposure", fontsize=14, fontweight='bold', pad=15)
    ax.grid(axis='x', alpha=0.3)
    ax.invert_yaxis()

    return fig


# ---------------------------------------------------------------------------
# Chart 4: Coverage Heatmap
# ---------------------------------------------------------------------------

def chart_coverage_heatmap(graph_data, portfolio_tickers, short_tickers):
    """SM data coverage matrix: tickers x data sources."""
    edges = graph_data['edges']
    nodes_by_id = {n['id']: n for n in graph_data['nodes']}
    all_tickers = portfolio_tickers + short_tickers

    sources = ['13F / Holders', 'FCA', 'AMF', 'Insider Buy', 'Insider Sell', 'Short %']
    source_keys = ['holds', 'fca', 'amf', 'insider_buy', 'insider_sell', 'shorts']

    # Determine what data exists per ticker
    ticker_data = {t: {sk: False for sk in source_keys} for t in all_tickers}

    for e in edges:
        tgt = e.get('target', '')
        rel = e.get('relation', '')
        ds = e.get('data_source', '')

        if tgt not in ticker_data:
            continue

        if rel == 'holds':
            ticker_data[tgt]['holds'] = True
        elif rel == 'shorts':
            if ds == 'fca':
                ticker_data[tgt]['fca'] = True
            elif ds == 'amf':
                ticker_data[tgt]['amf'] = True
            ticker_data[tgt]['shorts'] = True
        elif rel == 'insider_buy':
            ticker_data[tgt]['insider_buy'] = True
        elif rel == 'insider_sell':
            ticker_data[tgt]['insider_sell'] = True

    # Also check node-level short_pct_float
    for t in all_tickers:
        node = nodes_by_id.get(t, {})
        if node.get('short_pct_float', 0) > 0:
            ticker_data[t]['shorts'] = True

    # Build matrix
    matrix = np.zeros((len(all_tickers), len(sources)))
    for i, t in enumerate(all_tickers):
        for j, sk in enumerate(source_keys):
            if ticker_data.get(t, {}).get(sk, False):
                matrix[i, j] = 1.0  # Data exists (green)
            else:
                matrix[i, j] = 0.0  # Missing (red)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor('white')

    # Custom colormap: red (0) -> green (1)
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(['#E74C3C', '#27AE60'])

    im = ax.imshow(matrix, cmap=cmap, aspect='auto', vmin=0, vmax=1)

    ax.set_xticks(range(len(sources)))
    ax.set_xticklabels(sources, fontsize=10, rotation=30, ha='right')
    ax.set_yticks(range(len(all_tickers)))
    ax.set_yticklabels(all_tickers, fontsize=10, fontweight='bold')

    # Add text labels
    for i in range(len(all_tickers)):
        for j in range(len(sources)):
            val = matrix[i, j]
            text = 'Y' if val == 1.0 else 'N'
            ax.text(j, i, text, ha='center', va='center', fontsize=10,
                    fontweight='bold', color='white')

    # Legend
    legend_elements = [
        mpatches.Patch(color='#27AE60', label='Data exists'),
        mpatches.Patch(color='#E74C3C', label='Missing'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.25, 1),
              fontsize=9)

    ax.set_title("Smart Money Data Coverage -- Portfolio Positions",
                 fontsize=14, fontweight='bold', pad=15)

    return fig


# ---------------------------------------------------------------------------
# Chart 5: Position Health Scores
# ---------------------------------------------------------------------------

def chart_position_health(portfolio_tickers, short_tickers):
    """Position health score dashboard from kc_monitor.py --health."""
    all_tickers = portfolio_tickers + short_tickers
    health_scores = {}

    # Run kc_monitor.py --health and parse the tabular output
    # Format: "Ticker     Score  Thesis    DA  Risk    KC Evnts    FV  Anom    SM  Status"
    try:
        result = subprocess.run(
            ['python3', str(REPO_ROOT / 'tools' / 'kc_monitor.py'), '--health'],
            capture_output=True, text=True, timeout=30,
            cwd=str(REPO_ROOT)
        )
        output = result.stdout

        for line in output.splitlines():
            line = line.strip()
            if not line or line.startswith('=') or line.startswith('-') or \
               line.startswith('POSITION') or line.startswith('PORTFOLIO') or \
               line.startswith('RECOMMENDATIONS') or line.startswith('[') or \
               line.startswith('Ticker') or line.startswith('>>'):
                continue

            # Match lines like: "FTNT         100  20/20 15/15 ..."
            # Ticker is first non-space token, Score is second
            parts = line.split()
            if len(parts) >= 2:
                ticker = parts[0]
                if ticker in all_tickers:
                    try:
                        score = int(parts[1])
                        if 0 <= score <= 100:
                            health_scores[ticker] = score
                    except ValueError:
                        continue
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as exc:
        print(f"  [WARN] kc_monitor.py --health failed: {exc}")

    # Fallback if no data parsed
    if not health_scores:
        for t in all_tickers:
            health_scores[t] = 70  # Default moderate

    # Sort by score ascending (worst at top)
    sorted_tickers = sorted(health_scores.keys(), key=lambda x: health_scores[x])
    scores = [health_scores[t] for t in sorted_tickers]

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('white')

    # Color gradient
    colors = []
    for s in scores:
        if s >= 80:
            colors.append('#27AE60')  # Green
        elif s >= 60:
            colors.append('#F39C12')  # Yellow
        elif s >= 40:
            colors.append('#E67E22')  # Orange
        else:
            colors.append('#E74C3C')  # Red

    y_pos = range(len(sorted_tickers))
    bars = ax.barh(y_pos, scores, color=colors, edgecolor='white', height=0.6, alpha=0.85)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_tickers, fontsize=10, fontweight='bold')
    ax.set_xlabel('Health Score (0-100)', fontsize=10)
    ax.set_xlim(0, 110)

    # Threshold lines
    ax.axvline(x=40, color='#E74C3C', linestyle='--', alpha=0.6, linewidth=1.5)
    ax.axvline(x=60, color='#F39C12', linestyle='--', alpha=0.6, linewidth=1.5)
    ax.text(41, len(sorted_tickers) - 0.5, 'CRITICAL', color='#E74C3C',
            fontsize=8, fontweight='bold', alpha=0.7)
    ax.text(61, len(sorted_tickers) - 0.5, 'STALE', color='#F39C12',
            fontsize=8, fontweight='bold', alpha=0.7)

    # Score annotations
    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                f'{score:.0f}', va='center', fontsize=10, fontweight='bold')

    # Legend
    legend_elements = [
        mpatches.Patch(color='#27AE60', label='Healthy (80+)'),
        mpatches.Patch(color='#F39C12', label='Monitor (60-79)'),
        mpatches.Patch(color='#E67E22', label='Stale (40-59)'),
        mpatches.Patch(color='#E74C3C', label='Critical (<40)'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    ax.set_title("Position Health Scores", fontsize=14, fontweight='bold', pad=15)
    ax.grid(axis='x', alpha=0.3)
    ax.invert_yaxis()

    return fig


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _get_chart_map():
    """Generate date-suffixed filenames for daily snapshots."""
    from datetime import date
    d = date.today().isoformat()
    return {
        'fund_network': f'fund_network_{d}.png',
        'basket_conviction': f'basket_conviction_{d}.png',
        'short_interest': f'short_interest_bars_{d}.png',
        'coverage': f'coverage_heatmap_{d}.png',
        'health': f'position_health_{d}.png',
    }

CHART_MAP = _get_chart_map()


def main():
    parser = argparse.ArgumentParser(
        description='Smart Money Visualizer — generate PNG charts from SM graph data.'
    )
    parser.add_argument('--chart', choices=list(CHART_MAP.keys()) + ['all'],
                        default='all', help='Which chart to generate (default: all)')
    args = parser.parse_args()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load data
    print("Loading data...")
    graph_data = load_graph()
    portfolio_text = _parse_yaml_lightweight(PORTFOLIO_PATH)
    baskets_text = _parse_yaml_lightweight(BASKETS_PATH)

    portfolio_tickers, short_tickers = extract_portfolio_tickers(portfolio_text)
    weights = extract_portfolio_weights(portfolio_text)
    baskets = extract_baskets(baskets_text)

    print(f"  Portfolio: {len(portfolio_tickers)} longs, {len(short_tickers)} shorts")
    print(f"  Baskets: {len(baskets)}")
    print(f"  Graph: {len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges")
    print()

    # Determine which charts to generate
    if args.chart == 'all':
        charts_to_gen = list(CHART_MAP.keys())
    else:
        charts_to_gen = [args.chart]

    plt.style.use('seaborn-v0_8-whitegrid')
    generated = []

    for chart_name in charts_to_gen:
        filename = CHART_MAP[chart_name]
        filepath = OUTPUT_DIR / filename
        print(f"Generating {chart_name}...")

        fig = None
        if chart_name == 'fund_network':
            fig = chart_fund_network(graph_data, portfolio_tickers, short_tickers, weights)
        elif chart_name == 'basket_conviction':
            fig = chart_basket_conviction(graph_data, baskets, portfolio_tickers)
        elif chart_name == 'short_interest':
            fig = chart_short_interest(graph_data, portfolio_tickers, short_tickers)
        elif chart_name == 'coverage':
            fig = chart_coverage_heatmap(graph_data, portfolio_tickers, short_tickers)
        elif chart_name == 'health':
            fig = chart_position_health(portfolio_tickers, short_tickers)

        if fig is not None:
            fig.savefig(str(filepath), dpi=150, bbox_inches='tight', facecolor='white')
            plt.close(fig)
            size_kb = filepath.stat().st_size / 1024
            print(f"  -> {filepath} ({size_kb:.0f} KB)")
            generated.append(str(filepath))
        else:
            print(f"  -> SKIPPED (no data or missing dependency)")

    print()
    print(f"Generated {len(generated)} chart(s):")
    for g in generated:
        print(f"  {g}")


if __name__ == '__main__':
    main()

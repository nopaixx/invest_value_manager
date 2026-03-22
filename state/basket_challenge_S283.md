# Basket Challenge Protocol — S283 (2026-03-22)

> Status: COMPLETED. Findings documented. Reorganization DEFERRED to next week coffee chat.
> Decision: CIO will propose new basket structure based on megatrends, not geography.

## Key Findings

### 1. Geographic baskets are labels, not theses
- 3 of 6 baskets are geographic (US QC, UK QL, EU PP) = 63.5% of portfolio
- 3 of 6 baskets are thematic (D&A, Cyber, Defense) = 21.0% of portfolio
- Geographic baskets were created to organize EXISTING positions, not from conviction
- "UK Quality Leaders" is not a reason to buy IHP.L — IHP.L is bought for adviser platform monopoly

### 2. 50% of baskets are dying or empty
- EU Pricing Power: DEATH_WATCH (1 position, dying Apr 6)
- Cybersecurity: 0 positions post-FTNT exit (April)
- Defense: 0 positions ever, all pipeline overpriced
- Only D&A Monopolies has coherent theme + positions + pipeline

### 3. Zero exposure to 3 strongest megatrends
- AI Infrastructure: 0% (META/TSM/AVGO all overpriced)
- Defense/Cyber: 7.4% → 0% (FTNT exiting)
- Energy Security: 0% (correct — quality filter)

### 4. Baskets did NOT improve any buy/sell decision
- BCG.L: bought for monopoly + E[CAGR], not basket label
- AJB.L: rejected for concentration, not basket analysis
- MONY.L rotation: identified by forward_return.py ranking, not basket
- Baskets organize reporting but don't generate alpha

### 5. Rule for reorganization
Each basket must answer: "What megatrend secular justifies this grouping?"
If the answer is "they're from the same country" → not a basket.

## Proposed Direction (for next week discussion)

Simplify from 6 to ~3-4 thematic baskets + orphans:
- Data Infrastructure Monopolies (keep, STRONGEST)
- Quality Compounders (merge US+UK geographic, theme = quality moat)
- Defense & Cyber (merge, theme = security regime change)
- Orphans: positions justified individually, no forced basket

## Data Points for Reorganization

| Current Basket | Issue | Proposed |
|---------------|-------|----------|
| US Quality Compounders | Geographic label, 3 unrelated businesses | → Quality Compounders (any geo) |
| UK Quality Leaders | Geographic label | → Quality Compounders (any geo) |
| EU Pricing Power | Dying, 1 position | → Kill, EDEN.PA = orphan |
| D&A Monopolies | WORKS — keep as is | → Keep |
| Cybersecurity | 0 positions post-exit | → Merge into Defense & Cyber |
| Defense | 0 positions, strong theme | → Merge into Defense & Cyber |

## Marginal Impact Analysis

| Scenario | Sharpe | Notes |
|----------|--------|-------|
| HLNE→ITRK.L (10%→5%) | +0.023 | Basket label didn't affect this decision |
| EDEN.PA 18%→13% | +0.004 | Concentration rule, not basket analysis |
| Best deployment combo (ITRK.L+CMCSA) | +0.0042 | Discovered by marginal portfolio analysis, not basket |

## Action Items
- [ ] Coffee chat next week: propose final basket structure
- [ ] Each basket must have secular megatrend thesis (not geography)
- [ ] Kill EU Pricing Power formally when Apr 6 arrives
- [ ] Merge Cyber + Defense when FTNT exits
- [ ] Rename US QC + UK QL → Quality Compounders (or kill and use orphans)

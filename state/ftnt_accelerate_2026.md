# FTNT Accelerate 2026 - Post-Event Intelligence Report

> **Date:** 2026-03-13
> **Event:** Fortinet Accelerate 2026 (Las Vegas, March 9-13) + Investor Briefing (March 10, 3pm PT)
> **Position:** 10.57 shares, FV $88, E[CAGR] 9.4% (lowest in portfolio)
> **Purpose:** Answer 5 key questions + assess rotation implications

---

## 1. FY2027 Guidance Update

**ANSWER: NO EXPLICIT FY2027 GUIDANCE PROVIDED.**

The investor briefing reiterated FY2026 guidance only:
- Revenue: $7.5B-$7.7B (+12% YoY)
- Billings: $8.4B-$8.6B (+13% at midpoint)
- Service revenue: $5.05B-$5.15B (+11%)
- Non-GAAP gross margin: 79%-81%
- Non-GAAP operating margin: 33%-36%
- Non-GAAP EPS: $2.94-$3.00
- Rule of 45+ target reaffirmed

Management referenced "continued double-digit growth" but did NOT provide a specific FY2027 revenue number or long-term revenue CAGR target. The thesis estimated ~$9.2B rev by FY2028 based on extrapolation; this was not explicitly confirmed or denied.

**Classification: MINOR** -- No new info, no FV change. The absence of a multi-year guide is a missed opportunity to build conviction, but not bearish. Many cybersecurity companies don't provide 2-year-out guidance.

---

## 2. SASE ARR Update

**ANSWER: NO INCREMENTAL SASE ARR DISCLOSURE BEYOND Q4 NUMBERS.**

What was reiterated:
- Unified SASE billings grew +40% in Q4 2025
- Unified SASE + SecOps combined grew +24% FY2025, now 36% of total billings
- CEO Ken Xie highlighted Sovereign SASE (on-prem deployment) as unique differentiator
- "Doubled the TAM in the SASE market with Sovereign SASE" (Xie quote from earnings)

What was NOT disclosed:
- Specific SASE ARR dollar figure (estimated ~$300M+)
- SASE customer count or net retention rate
- SASE pipeline or booking trajectory for FY2026

**Classification: MINOR** -- SASE momentum confirmed but no NEW data. KC#2 (SASE <15%) remains CLEAR at +40% Q4 growth. Gap persists: no absolute ARR figure disclosed, making independent tracking difficult.

---

## 3. ASIC Roadmap

**ANSWER: ASIC TOUTED BUT NO SPECIFIC NEXT-GEN ROADMAP DISCLOSED.**

What was presented:
- FortiASIC described as "Only Purpose-Built Proprietary ASIC for Secure Computing"
- Current gen accelerates 14 FortiOS functions, supports 2x more applications than previous gen
- $1B+ cumulative ASIC R&D investment referenced (consistent with thesis)
- 60% unit share in firewall market attributed partly to ASIC cost advantage

What was NOT disclosed:
- SP6 or next-generation ASIC timeline
- Specific performance targets for next-gen silicon
- Competitive benchmarks vs custom silicon from Palo Alto (none) or CrowdStrike (software-only)

**Classification: MINOR** -- ASIC moat narrative reinforced but no incremental information. The moat remains intact but no new data to strengthen or weaken the thesis.

---

## 4. CVE/Vulnerability Response

**ANSWER: MIXED -- ADDRESSED BUT CONCERNING NEW DEVELOPMENTS.**

### What Fortinet said at Accelerate:
- CVE-2025/2026 crisis was addressed in the briefing (not ignored -- slight positive)
- No customer churn data disclosed (gap -- we asked for this in our pre-event framework)
- No transparent post-mortem with technical remediation specifics for investors

### What happened in parallel (March 10, 2026 -- SAME DAY as briefing):
- 11 new vulnerabilities disclosed across FortiManager, FortiAnalyzer, FortiSwitchAXFixed, FortiSandbox
- CVE-2025-54820: HIGH severity stack-based buffer overflow in FortiManager (remote unauthenticated RCE)
- CVE-2026-22572: Authentication bypass via alternate path in FortiAnalyzer/FortiManager GUI (bypasses MFA entirely)
- CVE-2026-22629: Authentication lockout bypass via race condition
- **Active exploitation confirmed**: Threat actors exploiting authentication-bypass CVEs (CVE-2025-59718, CVE-2025-59719, CVE-2026-24858) to compromise FortiGate infrastructure
- CISA issued guidance on ongoing exploitation of CVE-2026-24858

### Assessment:
This is the MOST concerning finding. The thesis flagged product security as a non-KC risk based on industry precedent (CrowdStrike/PANW recovered). However:

- The FREQUENCY of CVEs is escalating: not just a one-off incident but a pattern
- Active exploitation on the SAME DAY as investor briefing is bad optics
- MFA bypass (CVE-2026-22572) is a FUNDAMENTAL security failure for a security company
- KC#9 (3rd CISA KEV in 12 months) is approaching -- need to count KEVs precisely

**Classification: MATERIAL** -- Not yet CRITICAL because: (1) patches exist, (2) industry precedent shows recovery, (3) no customer churn data suggesting exodus. But this WEAKENS the moat narrative and is approaching KC#6/#9 territory.

**ACTION: Monitor CISA KEV database for KC#9 count. If 3rd KEV confirmed in 12-month window, thesis review triggered.**

---

## 5. Revenue/Margin Guidance Changes

**ANSWER: NO CHANGES -- FY2026 GUIDANCE REITERATED UNCHANGED.**

| Metric | FY2025 Actual | FY2026 Guide | Status |
|--------|---------------|--------------|--------|
| Revenue | $6.80B (+14%) | $7.5-7.7B (+12%) | Unchanged |
| Billings | $7.67B (+18%) | $8.4-8.6B (+13%) | Unchanged |
| Gross margin | 80.5% | 79-81% | Unchanged |
| Operating margin | ~33% | 33-36% | Unchanged |
| EPS | $2.55 | $2.94-3.00 | Unchanged |

**Classification: MINOR** -- Guidance reiteration is neutral. No raise (missed opportunity given strong Q4), no cut. The deceleration from 14% to 12% revenue growth is already priced in.

---

## Product Announcements (Bonus -- not in original questions)

### FortiOS 8.0 (launched March 10)
- AI-driven security: GenAI app visibility, AI-aware application control, MCP agent-to-agent visibility
- Next-gen SASE: SASE Outpost (extends to customer-controlled locations), Sovereign SASE options, Multipath IPsec
- Quantum-safe: Post-Quantum Cryptography (PQC) certificates, quantum-safe SASE
- AI agents for firewall/SD-WAN configuration (conversational workflows)

### FortiSOC (preview)
- Cloud-delivered unified SOC platform consolidating FortiAnalyzer, FortiSIEM, FortiSOAR, FortiTIP
- Agentic AI capabilities for automated triage, investigation, threat hunting
- Competitive response to CrowdStrike's Charlotte AI and PANW's XSIAM

### FortiEndpoint
- Single-agent architecture spanning ZTNA, SASE, EPP, EDR, DLP
- Consolidation play -- addresses the "83 tools from 29 vendors" problem

**Classification: MINOR/POSITIVE** -- Solid product execution. FortiOS 8.0 is a meaningful release (quantum-safe, sovereign SASE, AI agents). FortiSOC preview positions Fortinet competitively in SecOps. But product announcements at annual conferences are expected, not incremental surprises.

---

## Summary Assessment

| Question | Answer | Classification | FV Impact |
|----------|--------|----------------|-----------|
| FY2027 guidance | Not provided | MINOR | None |
| SASE ARR update | Reiterated Q4 (+40%) | MINOR | None |
| ASIC roadmap | Narrative, no specifics | MINOR | None |
| CVE/vulnerability | MATERIAL -- escalating pattern, active exploitation | MATERIAL | Potential -$3-5 if pattern continues |
| Revenue/margin guidance | Unchanged, reiterated | MINOR | None |

### Overall Event Assessment: NEUTRAL with YELLOW FLAG on security

**FV $88 UNCHANGED.** The event provided no data to raise or lower fair value. Product execution is solid. However:

1. **CVE escalation is the only actionable signal.** The frequency and severity of vulnerabilities is a growing reputational risk for a company whose ENTIRE VALUE PROPOSITION is security. Industry precedent (CRWD, PANW) suggests recovery, but those were single incidents -- Fortinet is showing a PATTERN.

2. **E[CAGR] 9.4% remains lowest in portfolio.** No catalyst from Accelerate to improve this. Q1 earnings May 6 is next inflection point.

3. **Rotation case neither strengthened nor weakened.** FTNT remains "first to go if better candidate matures." The CVE situation adds a small qualitative discount to conviction but is not KC-triggering.

---

## KC Status Post-Accelerate (March 13 update)

| KC# | Condition | Status | Change from pre-event |
|-----|-----------|--------|----------------------|
| 1 | Revenue <8% 2Q | CLEAR | No change |
| 2 | SASE ARR <15% | CLEAR (+40% Q4) | No change |
| 3 | FCF <25% 2Q | CLEAR | No change |
| 4 | Ken Xie departure | CLEAR | No change |
| 5 | Xie <5% ownership | CLEAR (17.4%) | No change |
| 6 | 2nd security incident causing customer attrition | MONITORING | ELEVATED -- pattern of CVEs continuing |
| 7 | Product rev -10% + SASE <15% | CLEAR | No change |
| 8 | Deferred rev <8% 2Q | CLEAR | No change |
| 9 | 3rd CISA KEV in 12mo | MONITORING | Need precise count -- may be APPROACHING |

---

## Next Actions

1. **Count CISA KEVs precisely** -- determine if KC#9 is approaching or triggered
2. **Monitor Q1 earnings May 6** -- next real catalyst for FV change
3. **If better rotation candidate reaches R4** with E[CAGR] >12.4% (FTNT + 3pp) -- FTNT is first rotation out
4. **CVE monitoring** -- set WebSearch alert cadence for "Fortinet CVE CISA" monthly

---

*Report prepared: 2026-03-13. Sources: Fortinet IR, CISA, Help Net Security, Yahoo Finance, Simply Wall St, TradingView, GlobeNewswire.*

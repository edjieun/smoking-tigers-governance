# AI Agent Org Chart
**Smoking Tigers Media Group** (Quorum1 LLC d/b/a Smoking Tigers Media Group)

Status: Draft v1.0
Owner: Ed (Steward)
Reviewed by: Ed, Christine (Executive Council)
Purpose: Governance visibility, usage tracking, cost tracking, audit support
Last Updated: 2026-03-06

---

## 1. Org Chart — Hierarchy & Relationships

```
┌─────────────────────────────────────────┐
│        HUMAN AUTHORITY LAYER            │
│  Ed (Steward) · Christine (Exec Council)│
│                                         │
│  All Class C actions require human      │
│  approval. No agent has autonomous      │
│  authority over governance, finance,    │
│  security, or canonical records.        │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────▼──────────┐
        │       SCOUT         │
        │   Chief of Staff    │
        │   (Orchestrator)    │
        └──┬──────────────┬───┘
           │              │
    ┌──────▼──────┐  ┌────▼────────────┐
    │ EVA (ea)    │  │   DOUG (sysops) │
    │ Executive   │  │ System Ops      │
    │ Assistant   │  │                 │
    └─────────────┘  └─────────────────┘
           │
    ┌──────▼──────────────┐
    │ SERGEANT-AT-ARMS    │
    │       (saa)         │
    │ Governance Enforcer │
    └──────┬──────────────┘
           │
    ┌──────▼──────────────────────┐
    │  SPECIALIST AGENTS          │
    │  · knowledge-ops            │
    │  · governance-ops           │
    └─────────────────────────────┘
```

**Key relationships:**
- Scout is the primary orchestrator. All agent spawning and cross-agent coordination routes through Scout.
- Eva and Doug are specialist agents Scout can spawn directly.
- Sergeant-at-Arms enforces policy boundaries and routes decisions requiring governance review.
- knowledge-ops and governance-ops are task-scoped agents — spawned for specific processing jobs, not persistent.
- All agents operate under human authority. No agent can approve, commit, or finalize without explicit human authorization.

---

## 2. Agent Roster

| Agent | Role | Model | Runtime / Surface | Scope / Authority |
|---|---|---|---|---|
| **Scout** | Chief of Staff — primary orchestrator | Claude Sonnet 4.6 (OpenRouter) | OpenClaw · Mattermost #executive · Webchat | Class A + B drafting; orchestrates other agents; no autonomous governance/financial decisions |
| **Eva (ea)** | Executive Assistant | Claude Sonnet 4.6 (OpenRouter) | OpenClaw · Mattermost | Calendar, notes, reminders, email, Notion; draft-only for any commitment |
| **Doug (sysops)** | System Operations | Claude Sonnet 4.6 (OpenRouter) | OpenClaw · Mattermost | Infrastructure health, monitoring, security review; propose-only for any config changes |
| **Sergeant-at-Arms (saa)** | Governance Enforcer | Claude Sonnet 4.6 (OpenRouter) | OpenClaw · Mattermost | Policy enforcement, decision routing; no approval authority — surfaces issues for human decision |
| **knowledge-ops** | Knowledge Processing | Gemini 2.5 Pro (OpenRouter) | OpenClaw (spawned) | Session transcript processing, memory file construction, knowledge intake; large-context tasks only |
| **governance-ops** | Governance Documentation | Claude Sonnet 4.6 (OpenRouter) | OpenClaw (spawned) | Drafts governance decisions and policies; all outputs are DRAFT until human-approved |

**Infrastructure notes:**
- All models run via **OpenRouter** (cloud-hosted). No local Ollama model inference in production.
- Local Ollama (`nomic-embed-text`) used for **embeddings only** — no generative output.
- Agents bind to **Mattermost bots** on local Mattermost instance (localhost:8065, accessible via Tailscale).
- **OpenClaw** is the agent runtime and orchestrator.

---

## 3. Usage & Cost Tracking

> ⚠️ Actual numbers are TBD. Ed to populate from OpenRouter billing dashboard or connect to real telemetry.

### 3.1 Estimated Calls Per Day (Per Agent)

| Agent | Est. Calls/Day | Notes |
|---|---|---|
| Scout | TBD | Primary orchestrator; likely highest volume |
| Eva (ea) | TBD | Triggered by calendar/note/task requests |
| Doug (sysops) | TBD | Triggered by health checks / incidents |
| Sergeant-at-Arms | TBD | Triggered by policy/decision routing events |
| knowledge-ops | TBD | Batch; not daily — triggered by session processing jobs |
| governance-ops | TBD | Batch; triggered by governance drafting requests |

### 3.2 Model Cost Tier

| Model | Provider | Cost Tier | Notes |
|---|---|---|---|
| Claude Sonnet 4.6 | Anthropic via OpenRouter | Mid (per-token) | Used by Scout, Eva, Doug, saa, governance-ops |
| Gemini 2.5 Pro | Google via OpenRouter | Mid-High (large context) | Used by knowledge-ops; large-context window = higher token volume |
| nomic-embed-text | Ollama (local) | Free (local compute) | Embeddings only; no OpenRouter spend |

### 3.3 Monthly Cost Estimate

| Agent | Model | Est. Monthly Cost |
|---|---|---|
| Scout | Claude Sonnet 4.6 | TBD |
| Eva (ea) | Claude Sonnet 4.6 | TBD |
| Doug (sysops) | Claude Sonnet 4.6 | TBD |
| Sergeant-at-Arms | Claude Sonnet 4.6 | TBD |
| knowledge-ops | Gemini 2.5 Pro | TBD |
| governance-ops | Claude Sonnet 4.6 | TBD |
| **Total** | | **TBD** |

**Tracking recommendation:** Pull from OpenRouter billing API or dashboard monthly. Tag requests by agent name for cost attribution when available.

---

## 4. Audit Notes

> For Christine and any external auditor. Plain language summary of access, data touch, and human gates.

### 4.1 Who Has What Access

| Agent | System Access | Data It Can Touch | Notes |
|---|---|---|---|
| Scout | Mattermost, OpenClaw workspace, Apple integrations (Mac user context) | Workspace files, memory files, governance docs, calendar/notes/reminders | Apple integrations only under the Apple-enabled macOS user. High-sensitivity surface. |
| Eva (ea) | Mattermost, Calendar, Notes, Reminders, Notion | Scheduling data, meeting notes, task lists, email drafts | Draft-only for any external send. No approval authority. |
| Doug (sysops) | Mattermost, system logs, infrastructure tooling | Logs, config files, health metrics | Cannot apply production changes without explicit human authorization. |
| Sergeant-at-Arms | Mattermost | Governance policy files, decision routing | Surfaces issues; cannot approve decisions. |
| knowledge-ops | OpenClaw (spawned) | Session transcripts, memory files, knowledge intake files | Batch processing only; outputs are drafts pending review. |
| governance-ops | OpenClaw (spawned) | Governance documents, policy drafts | All outputs labeled DRAFT. Merge to canonical requires human approval. |

### 4.2 Data Classification Context

- **Apple data** (calendar, notes, iMessage, Keychain) is treated as **high-sensitivity**. Only Scout may access; always requires explicit instruction for any external action.
- **Governance documents** are **canonical** — agents may draft and propose but cannot merge or approve.
- **Memory files** are internal operational records — not external commitments.
- **Session transcripts** processed by knowledge-ops are considered internal operational data.

### 4.3 Human Approval Gates (Non-Negotiable)

The following always require explicit human approval before any agent acts:

| Action | Gate |
|---|---|
| Approving a governance decision | Ed or authorized Council member |
| Merging governance/policy changes to canonical branch | Ed |
| Any financial commitment or budget allocation | Ed (Steward) |
| Sending external communications as official statements | Ed or designated Council member |
| Security policy changes | Ed |
| Production infrastructure changes | Ed |
| Deletion of canonical or source records | Ed |
| Creating or revoking user/system accounts | Ed |
| Changing agent authority or system integrations | Ed |

No agent can mark a decision **Approved**. No agent can infer consent from silence.

### 4.4 What Agents Cannot Do

- Approve decisions
- Assign compensation, RevPoints, or payroll
- Commit legal or contractual obligations
- Publish external communications without instruction
- Self-escalate to premium model usage without authorization
- Silently write to canonical records
- Claim a human approved something if they did not

### 4.5 Audit Trail Gaps (Current State)

| Gap | Risk | Status |
|---|---|---|
| No automated per-agent call logging | Limited post-incident traceability | TBD — OpenRouter attribution tagging in progress |
| No formal incident log for agent errors | Audit gaps if something goes wrong | TBD |
| Apple integration actions not system-logged | Reliance on Scout session context | Accepted risk for now; revisit if Apple surface expands |
| knowledge-ops / governance-ops spawn events not centrally logged | Unclear audit trail for batch jobs | TBD |

---

## 5. Governance Alignment

### 5.1 Governing Policies

This document operates under and is accountable to:

| Policy | Path | Status |
|---|---|---|
| Agent Authority Matrix | `policies/governance/agent-authority-matrix.md` | Draft v1.0 |
| AI Resource Stewardship | `policies/ai/ai-resource-stewardship.md` | Draft v1.0 |

All agent design, capability scoping, and authority boundaries in this document must remain consistent with those policies.

### 5.2 Key Policy Commitments (Summary)

**From Agent Authority Matrix:**
- Every agent action falls into Class A (autonomous assistive), Class B (propose only), or Class C (restricted — requires explicit human authorization each time).
- Agents must not silently write to canonical stores.
- Agents must not invent approvals or infer consent from silence.
- Outputs that are not approved must be labeled: `DRAFT`, `PROPOSED`, `UNCONFIRMED`, or `PENDING APPROVAL`.

**From AI Resource Stewardship:**
- Default routing is Local-First, then escalate by value. Premium model usage is reserved for judgment, synthesis, and high-stakes wording — not clerical work.
- Agents must not self-escalate to premium models without authorization.
- Monthly review of premium model usage patterns is required.
- knowledge-ops using Gemini 2.5 Pro is an approved exception for large-context transcript processing — justified by context window requirements.

### 5.3 Policy Review Triggers

This document and its underlying policies should be reviewed when:
- A new agent is added to the roster
- A new system integration is enabled
- An agent incident or near-miss occurs
- Governance structure changes
- OpenRouter billing spikes unexpectedly

---

## 6. Change Log

| Date | Change | Author |
|---|---|---|
| 2026-03-06 | Initial draft | Scout (subagent) |

---

*This is a working governance document. Plain language, no fluff.*
*All agent outputs, including this document, are DRAFT until reviewed and approved by Ed.*

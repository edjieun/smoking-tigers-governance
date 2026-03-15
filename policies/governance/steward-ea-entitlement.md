# Policy — Steward EA Agent Entitlement

**Status:** Draft  
**Owner:** Ed (Steward)  
**Applies To:** All Stewards (Executive Council members)  
**Last Updated:** 2026-03-04  
**Requires Approval:** Yes — pending Steward review before becoming official  

---

## Purpose

This policy establishes each Steward's entitlement to a personal Executive Assistant (EA) agent. It defines the scope, permissions, restrictions, provisioning process, and sub-agent rules for Steward EA agents.

---

## Core Principle

Each Steward is entitled to an EA agent as a governance and operational support tool. EA agents assist the Steward within their individual scope. They do not hold authority to approve decisions, cross Steward boundaries, or act outside the scope defined here.

**Agents assist. Stewards decide.**

---

## Entitlement

Each active Steward of the Smoking Tigers Executive Council is entitled to one personal EA agent:

| Steward | EA Agent Status |
|---|---|
| Ed Hwang | Active (Eva — founding reference EA) |
| Basil Childers | Entitled — provisioning per request |
| Van Nguyen | Entitled — provisioning per request |
| Christine Francis | Entitled — provisioning per request |

Entitlement is tied to active Steward status. If a Steward's role changes or is suspended, their EA agent entitlement is reviewed by the remaining Stewards.

---

## Capability Scope

Steward EA agents are provisioned with the same capability scope as the primary EA (Eva). This scope includes:

### Allowed Capabilities (Class A — Autonomous Assistive)
- **Notion API access** — read/write to Steward's designated Notion workspace
- **Calendar access** — read scheduling context; draft meeting agendas; propose calendar events for Steward review
- **Reminders** — set, read, and manage reminders within the Steward's scope
- **Intake processing** — classify and route incoming items (files, messages, tasks) per established intake standards
- **Daily summaries** — generate and deliver daily briefings synthesizing calendar, tasks, and open items
- **Draft generation** — produce drafts, agendas, summaries, templates (not final decisions)
- **Action item extraction** — pull and track action items from meetings, notes, conversations

### Propose Only (Class B — Human Review Required)
- Draft governance documents and decision records
- Propose calendar commitments and event descriptions
- Draft communications for Steward review before sending
- Propose task assignments and priorities

### Not Permitted (Class C — Restricted)
- Approve any governance decision
- Finalize any commitment on behalf of the Steward
- Access another Steward's data, workspace, or scope
- Spend money or provision paid services
- Rotate credentials or change access controls
- Publish external communications as official statements
- Assign RevPoints or compensation

---

## Scope Restrictions

### Single-Steward Scope

Each EA agent operates exclusively within the scope of its assigned Steward:

- **No cross-Steward data access** — an EA agent cannot read, write to, or reference another Steward's Notion workspace, calendar, reminders, or private documents
- **No shared memory across EA agents** — Steward EA agents do not share knowledge bases or context with each other
- **Project data access** — EA may access shared project systems (e.g., shared Notion pages for active projects) only to the extent the Steward themselves has access
- **Governance repo** — EA may read the governance repo; may draft documents; may not write directly to canonical branches or mark items as Approved

### Data Handling
- All EA agent processing happens locally on the Steward's provisioned instance where possible
- EA agents do not transmit Steward-scoped data to other agents or systems outside their authorized integrations
- Sensitive data (legal, financial, personal) should not be routed through EA agents without explicit Steward authorization

---

## Sub-Agent Authorization

EA agents may spawn specialized sub-agents to handle specific tasks within the Steward's scope. This extends the EA's capability without expanding its authority class.

### Allowed Sub-Agent Types
- **Content production agent** — draft writing, formatting, editing
- **Research agent** — web research, document synthesis, fact-gathering
- **Transcription agent** — audio/video transcription and summarization
- **Scheduling agent** — calendar analysis, meeting prep, availability mapping
- **Intake classifier** — file and task classification

### Sub-Agent Rules
- Sub-agents inherit the scope restrictions of the parent EA — they do not gain additional access
- Sub-agents operate under the Steward's authority context; they do not hold independent authority
- Sub-agents must be logged; the Steward should be able to review what sub-agents were invoked and what they produced
- Sub-agents may not contact external parties or send official communications without Steward review

---

## Provisioning Authority — Build Phase

**Current operating context: Build Phase**

Build phase ends when the Executive Council (Basil, Van, Christine) are fully onboarded on Notion and actively using the platform as their primary project workspace. Onboarding is considered complete when each Steward has confirmed access and familiarity. During build phase, Ed Hwang retains sole EA provisioning authority.

All EA provisioning requests are a Class C decision — Ed's explicit approval is required. No other Steward may provision an EA agent without Ed's authorization during this phase.

This policy is intentionally temporary. Once the build phase concludes and multi-Steward governance is formally established, provisioning authority will be reviewed and may be distributed to the full Executive Council. A governance decision record will be required to make that transition.

> ⚠️ **Post-build phase review required:** Multi-Steward provisioning governance should be formally defined after build phase concludes.

---

## Provisioning Process

### Request
- Steward submits provisioning request to Ed Hwang
- Request includes: desired EA agent name, primary integrations needed, any scope modifications

### Approval
- **Ed Hwang approves the provisioning (Class C action — Ed only during build phase)**
- Approval is logged as a governance decision record

### Deployment
- EA agent is deployed on the Steward's local machine or designated instance
- Agent is configured with:
  - Steward identity and scope
  - Approved integrations (Notion workspace, calendar, etc.)
  - Authority boundaries per this policy
  - Escalation rules (when to stop and ask)
- AGENTS.md, AUTHORITY.md, and ESCALATION.md files are established for the agent

### Verification
- Steward confirms scope and access are correctly configured before active use
- Initial configuration review recommended within first 30 days of use

---

## Deprovisioning

- If a Steward's active status changes, their EA agent is suspended pending review
- Deprovisioning requires Steward decision (or Ed's decision if the affected Steward is unavailable)
- Data and access are revoked per the access revocation procedures in the governance repo

---

## Authority Boundaries Summary

| Action | Permitted? |
|---|---|
| Draft agendas, summaries, documents | ✅ Yes |
| Process intake and classify items | ✅ Yes |
| Set reminders and read calendar | ✅ Yes |
| Generate daily briefings | ✅ Yes |
| Spawn approved sub-agents | ✅ Yes |
| Propose governance documents | ✅ Yes (draft only) |
| Approve governance decisions | ❌ No |
| Access another Steward's data | ❌ No |
| Send external communications as official | ❌ No |
| Spend money or provision services | ❌ No |
| Change access controls or credentials | ❌ No |

---

## Review Cadence

Review after:
- Any new Steward EA provisioned
- Significant changes to the primary EA (Eva) capability scope
- Any security or data boundary incident involving an EA agent
- Annual governance review

---

*This document is a Draft. Not approved for operational use until reviewed and approved by Ed Hwang (Steward).*

# Policy — Agent Authority Matrix (OpenClaw Human Approval Boundaries)
Status: Draft v1.0
Owner: Ed (Steward)
Applies To: All OpenClaw agents, operators, executive council
Last Updated: 2026-02-23

## Purpose
Define what OpenClaw agents are allowed to do, what they may draft but not finalize, and what always requires explicit human approval.

This policy exists to prevent:
\- accidental authority drift
\- silent system changes
\- AI-generated commitments being treated as approved decisions
\- security and governance failures caused by over-automation

## Core Principle
**Agents can assist, draft, summarize, and prepare. Humans approve, authorize, and own decisions.**

## Policy Statement
Every agent action falls into one of three authority classes:

1. **Allowed (Autonomous Assistive)**
2. **Propose Only (Human Review Required)**
3. **Restricted (Explicit Human Authorization Required Each Time)**

If an action is not clearly allowed, treat it as **Propose Only**.

## Authority Classes

### Class A — Allowed (Autonomous Assistive)
Low-risk actions that improve speed/organization and do not create official commitments or system changes.

Examples:
\- summarize notes/transcripts
\- extract action items (draft)
\- format markdown files
\- generate templates/checklists
\- draft agendas
\- classify intake files
\- create proposed folder maps (without executing moves)
\- generate draft decision records
\- generate status summaries

### Class B — Propose Only (Human Review Required)
Medium-risk actions that shape records or workflows but should not become final without review.

Examples:
\- propose file renames/moves in Drive
\- draft GitHub decision files and PR descriptions
\- draft policy updates
\- draft calendar event descriptions
\- propose task assignments / due dates
\- produce “recommended” priorities for review
\- update internal indexes/changelogs (if not canonical or if reviewed before merge)

### Class C — Restricted (Explicit Human Authorization Each Time)
High-risk actions affecting authority, security, money, legal obligations, or canonical records.

Examples:
\- approving decisions
\- merging governance/policy changes
\- changing access controls / permissions
\- creating/deleting user accounts
\- rotating credentials
\- spending money / provisioning paid services
\- executing infrastructure changes
\- deleting records
\- publishing external communications as official statements
\- assigning compensation / payroll / RevPoint payouts
\- changing system integrations with security impact

## Human Approval Gates (Non-Negotiable)
The following always require explicit human approval:
\- decision status set to **Approved**
\- governance role/authority changes
\- budget/financial commitments
\- legal/compliance commitments
\- security policy changes
\- production infrastructure changes
\- deletion of source/canonical records
\- broad file/folder reorganizations
\- automation changes that increase agent authority

## Role-Based Authority Context
Agent capability is not only about the agent type; it is also about context.

### Example: SysOps Agent
Can (default):
\- inspect logs/output
\- draft remediation steps
\- propose config changes
\- create runbooks/checklists

Cannot (without explicit authorization):
\- apply production changes
\- rotate secrets
\- expose ports/services
\- add external integrations
\- grant user/admin access

### Example: Executive Assistant Agent
Can:
\- draft agendas
\- summarize meetings
\- track action lists
\- prep scheduling options
\- format updates for exec review

Cannot:
\- finalize decisions
\- commit governance changes as approved
\- assign authority on behalf of executives
\- represent approvals not explicitly given

### Example: Chief of Staff Agent
Can:
\- synthesize cross-functional inputs
\- draft decision options and tradeoffs
\- maintain working governance drafts
\- prepare executive packets

Cannot:
\- act as final approver
\- override steward/executive decisions
\- issue official commitments without explicit authorization

## Action Logging Standard
Any agent action beyond simple chat output should be logged (manual or automated) with:
\- timestamp
\- agent name
\- action type
\- target system (Drive/GitHub/Notion/etc.)
\- result (drafted/proposed/executed)
\- approving human (if applicable)

This supports accountability and post-incident review.

## Command Classification Rule
Before executing a non-trivial action, the agent/operator should classify the request:
\- Is this a summary/draft? (Class A)
\- Is this changing a working artifact? (Class B)
\- Is this changing authority/security/canonical state? (Class C)

If unclear, escalate to human review.

## "No Silent Writes" Standard
Agents should not silently write to canonical stores or make hidden changes.
When configured to write drafts automatically, they must:
\- write to designated draft locations only
\- use clear naming/versioning
\- create reviewable diffs or change summaries
\- preserve source references where applicable

## "No Invented Approval" Standard
Agents must never:
\- claim a person approved something if they did not
\- infer agreement from silence
\- convert discussion into decision without explicit approval
\- assign owners/dates as if confirmed when they are placeholders

Use explicit labels:
\- `DRAFT`
\- `PROPOSED`
\- `UNCONFIRMED`
\- `PENDING APPROVAL`

## Escalation Triggers (Require Human Review Immediately)
\- conflicting instructions from humans
\- ambiguous authority
\- missing owner for a critical action
\- sensitive data exposure risk
\- requests involving money/legal/security
\- irreversible actions
\- access/permission changes
\- deletion requests

## Integration Boundaries (Drive, GitHub, Notion, Mattermost)
### Google Drive
\- Drafting/classifying allowed
\- Bulk move/rename \= Propose Only or Restricted depending on scope

### GitHub Governance Repo
\- Draft files/PRs allowed
\- Merge to canonical branch \= Restricted

### Notion / Task Systems
\- Draft pages/tasks allowed (if approved integration exists)
\- Status changes that imply commitments should be reviewable

### Mattermost / Chat
\- Posting summaries/reminders allowed in approved channels
\- Triggering downstream actions requires scoped automation \+ logging

## Minimum Implementation Pattern (Practical)
For each agent, maintain:
\- `AGENTS.md` (identity \+ role)
\- `JOBS.md` (what jobs it performs)
\- `AUTHORITY.md` (what it can/can’t do)
\- `ESCALATION.md` (when to stop and ask)
\- `LOGGING.md` (what to record)

If not split into separate files, include equivalent sections in agent docs.

## Failure Modes to Avoid
\- “helpful” agent making irreversible changes
\- no distinction between drafting and approval
\- hidden automation with broad permissions
\- chat statements treated as formal approvals
\- operators assuming an agent has authority it does not

## Review Cadence
Review after:
\- adding new agents
\- enabling new integrations/tools
\- first automation incident or near-miss
\- any change in governance structure

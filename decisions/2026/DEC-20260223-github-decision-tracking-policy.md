# DEC-20260223-github-decision-tracking-policy

**Decision ID:** DEC-20260223-002
**Title:** Adopt GitHub Decision Tracking Policy
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context

Governance decisions need a transparent, versioned system of record. GitHub was chosen as the canonical ledger, with OpenClaw assisting in drafting and formatting to reduce operator burden while preserving human approval gates.

## Decision

Adopt the GitHub Decision Tracking policy (Draft v1.0). All governance and operational decisions will follow the defined lifecycle: Discussion → Draft → Review → Approve → Publish. Decision records use a required format and naming convention (`/decisions/YYYY/DEC-YYYYMMDD-short-title.md`).

## Rationale

- Prevents decisions from being buried in chat or meeting notes
- Provides traceability and version history
- Keeps executives focused on deciding, not formatting

## Tradeoffs / Risks

- Adds process overhead to decision-making
- Requires operator discipline to maintain records

## Impacts

- All approved decisions must be recorded in the decisions directory
- A decisions index must be maintained
- OpenClaw may draft but cannot approve decisions

## Dependencies

- GitHub repo access for governance operators
- OpenClaw agent configured with governance install mode

## References / Sources

- Policy: `/policies/governance/github-decision-tracking.md`
- Discussion: Mattermost #executive, 2026-02-23

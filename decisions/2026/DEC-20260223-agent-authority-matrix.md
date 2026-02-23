# DEC-20260223-agent-authority-matrix

**Decision ID:** DEC-20260223-009
**Title:** Adopt Agent Authority Matrix Policy
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
OpenClaw agents need clearly defined authority boundaries to prevent accidental authority drift, silent system changes, and AI-generated commitments being treated as approved decisions.

## Decision
Adopt a three-class agent authority matrix (Allowed, Propose Only, Restricted) with explicit human approval gates for high-risk actions.

## Rationale
- Prevents agents from making unauthorized commitments
- Establishes clear escalation triggers
- Supports accountability through action logging

## Tradeoffs / Risks
- May slow down agent workflows that could be safely automated
- Requires ongoing maintenance as new agents and integrations are added

## Impacts
- All agent actions classified into authority classes before execution
- Human approval required for all governance, security, financial, and canonical record changes

## Dependencies
- Individual agent configuration (AGENTS.md, AUTHORITY.md per agent)
- Integration boundaries for Drive, GitHub, Notion, Mattermost

## References / Sources
- Policy: `policies/governance/agent-authority-matrix.md`
- Discussion: Mattermost #executive, 2026-02-23

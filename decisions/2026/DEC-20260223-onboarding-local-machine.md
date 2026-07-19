# DEC-20260223-onboarding-local-machine

**Decision ID:** DEC-20260223-015
**Title:** Adopt Local Machine Onboarding Guide
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
Executive council members running local OpenClaw instances need a structured onboarding process to adopt shared governance while maintaining local autonomy and security boundaries.

## Decision
Adopt an onboarding guide that defines prerequisites, setup steps, governance doc review requirements, agent behavior constraints, and contribution workflow for participating machines.

## Rationale
- Ensures consistent governance adoption across machines
- Prevents common mistakes (secrets in repo, draft-as-approved confusion)
- Establishes safe starting patterns before advanced use

## Tradeoffs / Risks
- Onboarding steps may feel bureaucratic for a small team
- Guide requires updates as tooling and governance evolve

## Impacts
- All participating machines follow a 10-step onboarding checklist
- Agents on local machines must respect governance boundaries before operating

## Dependencies
- README (repo purpose and operating model)
- Agent authority matrix
- AI resource stewardship policy

## References / Sources
- Document: `ONBOARDING-LOCAL-MACHINE.md`
- Discussion: Mattermost #executive, 2026-02-23

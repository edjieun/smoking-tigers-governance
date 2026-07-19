# DEC-20260223-policy-directory-structure

**Decision ID:** DEC-20260223-003
**Title:** Organize Policies into Domain Subdirectories
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context

The governance repo started with a flat `/policies/` directory. As the number of policies grows, a flat structure becomes harder to navigate. The GitHub Decision Tracking policy specifies `/policies/<domain>/<policy-name>.md` as the naming convention.

## Decision

Reorganize existing policies into domain subdirectories:
- `/policies/ai/` — AI resource and model routing policies
- `/policies/governance/` — governance process, roles, decision tracking, status definitions
- `/policies/operations/` — operational policies (RevPoint, etc.)

New policies should be placed in the appropriate domain subdirectory.

## Rationale

- Scales better as policy count grows
- Consistent with the naming convention defined in the decision tracking policy
- Improves discoverability

## Tradeoffs / Risks

- Existing references to flat paths will break (minor — repo is new)

## Impacts

- All existing policies moved to domain subdirs in this commit
- Future policies must use `/policies/<domain>/` structure

## Dependencies

- None

## References / Sources

- Convention defined in: `/policies/governance/github-decision-tracking.md`
- Discussion: Mattermost #executive, 2026-02-23

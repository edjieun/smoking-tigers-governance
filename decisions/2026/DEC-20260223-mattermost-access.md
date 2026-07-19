# DEC-20260223-mattermost-access

**Decision ID:** DEC-20260223-008
**Title:** Adopt Secure Mattermost Access Policy for Executive Council
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
The executive council needs secure, mobile-friendly access to self-hosted Mattermost for governance and operational coordination across a global team.

## Decision
Adopt a Mattermost access policy with tiered access model, private-by-default network access (Tailscale), structured onboarding, and clear data handling rules.

## Rationale
- Enables daily executive coordination with controlled security
- Separates communication access from infrastructure admin access
- Supports mobile use for a global team

## Tradeoffs / Risks
- Tailscale dependency for private access path
- Onboarding friction for non-technical executive members

## Impacts
- All executive council members follow standardized onboarding
- Mattermost access does not grant server or OpenClaw admin rights

## Dependencies
- Tailscale deployment
- Home network architecture
- Agent authority matrix (for OpenClaw/Mattermost interaction boundaries)

## References / Sources
- Policy: `policies/security/mattermost-access.md`
- Discussion: Mattermost #executive, 2026-02-23

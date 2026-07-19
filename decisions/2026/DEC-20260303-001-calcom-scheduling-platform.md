# DEC-20260303-001 — Cal.com Adopted as Scheduling Platform

**Decision ID:** DEC-20260303-001
**Title:** Cal.com Adopted as Scheduling Platform
**Status:** Approved
**Date:** 2026-03-03
**Owner / Approver:** Ed (Steward)

---

## Context

Ed authorized sysops to install Cal.com on the Mac Mini server running in Docker. Sysops completed installation with a dedicated Postgres container and a dedicated Redis container, both isolated from the existing Mattermost network. The installation replaces reliance on third-party scheduling SaaS products for internal and external scheduling needs.

## Decision

Cal.com is the official scheduling platform for Smoking Tigers Media. It runs locally on the Mac Mini server, containerized in Docker and isolated from the Mattermost network.

## Rationale

- Eliminates dependency on third-party scheduling SaaS (e.g., Calendly)
- Integrates with existing local infrastructure and Docker stack
- Supports future Cal.com API integration with EA (Executive Assistant agent)
- Keeps scheduling data on-premises, consistent with privacy-first posture

## Tradeoffs / Risks

- Self-hosted maintenance burden (upgrades, backups, container health)
- Cal.com API integration with EA not yet implemented — future work item
- Requires container health monitoring to maintain scheduling availability

## Impacts

- Sysops: responsible for Cal.com container upkeep and backup inclusion
- EA: future integration target for automated scheduling workflows
- STM: official scheduling tool transitions to Cal.com; third-party SaaS scheduling should be phased out

## Dependencies

- Docker stack on Mac Mini server
- Dedicated Postgres and Redis containers (provisioned)
- Cal.com API integration (future — not a condition of this decision)

## References / Sources

- Sysops installation session: 2026-03-03
- Related: DEC-20260303-002 (Mattermost and Cal.com Tailscale binding)

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-03 | Initial draft | Governance Ops |
| 2026-03-04 | Approved by Ed (Steward) | Ed |

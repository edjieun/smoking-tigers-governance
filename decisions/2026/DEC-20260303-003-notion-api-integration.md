# DEC-20260303-003 — Notion API Integration Adopted for STM Teamspace

**Decision ID:** DEC-20260303-003
**Title:** Notion API Integration Adopted for STM Teamspace
**Status:** Proposed
**Date:** 2026-03-03
**Owner / Approver:** Ed (Steward)

---

## Context

Phase 3 of the Notion Architecture Audit required programmatic API access to the STM Notion workspace. Ed created an Internal Notion Integration scoped exclusively to Smoking Tigers databases (read and write permissions). The integration token has been stored in the EA agent's auth profile. This enables agents to read and write Notion content without manual entry.

## Decision

The Notion API is the official integration method for agent access to the STM Notion workspace. EA (Executive Assistant agent) is the designated Notion operator agent. No other agent may access the STM Notion workspace via API without explicit authorization.

## Rationale

- Enables automated workflows: meeting note creation, task tracking, RP logging, IP registration
- Eliminates manual Notion entry for routine structured data
- Integration is scoped to STM databases only — limits blast radius if token is compromised
- EA is already the designated workflow agent; centralizing Notion access there is consistent with authority matrix

## Tradeoffs / Risks

- API token compromise would grant read/write access to scoped STM databases — token must be rotated if exposed
- Notion API rate limits apply; high-frequency automation may require batching
- Scope creep risk: additional database grants should require explicit authorization
- Agent errors could write bad data to Notion — EA workflows need validation logic

## Impacts

- EA: gains Notion API access; becomes responsible for Notion write operations
- Ed: token owner and rotation authority
- Governance: any expansion of Notion API scope (additional databases) requires a new decision or amendment
- Ops: token stored in EA auth profile — must be included in secret rotation procedures

## Dependencies

- Notion Internal Integration (configured by Ed, 2026-03-03)
- EA auth profile (token stored)
- STM Notion workspace access

## References / Sources

- Phase 3 Notion Architecture Audit: 2026-03-03
- EA auth profile (internal reference — do not log token in governance files)
- Related: DEC-20260302-001 (Notion Intake Lifecycle)

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-03 | Initial draft | Governance Ops |

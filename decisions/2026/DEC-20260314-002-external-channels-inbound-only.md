# DEC-20260314-002 — External Community Channels: Inbound-Only Agent Access

**Decision ID:** DEC-20260314-002
**Title:** External Community Channels: Inbound-Only Agent Access
**Status:** Approved
**Date:** 2026-03-14
**Owner / Approver:** Ed (Steward)

---

## Context

During the Van + Ed strategy session, the question of bidirectional vs. inbound-only agent access for external channels (Telegram, WhatsApp, Signal, Discord, iMessage) was reviewed.

External community channels can have large numbers of participants who have not been granted operator-level access to the ST:AI system. Allowing agents to respond in public community channels would create uncontrolled execution paths and governance risk.

## Decision

**External community channels are inbound-only.** Agents listen and route signals into the ST:AI ops system, but do not respond or take action directly in those channels.

Bidirectional agent interaction (agent reads AND responds/acts) is reserved for:
- Internal channels (Mattermost)
- Individual users who have been explicitly granted operator access

## Rationale

- Community members in external channels have not consented to AI-mediated responses
- Unrestricted bidirectional access in public channels creates execution risk (agents could "fuck shit up" — Ed's words)
- Most community members will interact with outputs via Notion, not directly with the agent layer
- Keeps the governance boundary clean: external = input; Mattermost = operations

## Implementation Notes

- Inbound routing rules to be defined per channel as they are integrated
- Community consent language (TOS) must be updated before any external channel goes live
- Smoking Tigers TOS should be updated in the governance repo to cover multi-channel data ingestion

## Status History

- 2026-03-14: Approved by Ed

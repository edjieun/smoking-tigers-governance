# DEC-20260314-001 — Multi-Channel Comms: Telegram First, WhatsApp Deprioritized

**Decision ID:** DEC-20260314-001
**Title:** Multi-Channel Comms: Telegram First, WhatsApp Deprioritized
**Status:** Approved
**Date:** 2026-03-14
**Owner / Approver:** Ed (Steward)

---

## Context

Ed and Van reviewed the multi-channel comms infrastructure strategy. The goal is to meet community members where they are (WhatsApp, Telegram, Signal, Discord, iMessage) and route inbound signals into the ST:AI ops system.

WhatsApp was evaluated for API risk: unofficial libraries expose Terms of Service violations. Telegram has a first-party bot API with fewer compliance risks and is widely used across the target communities.

## Decision

**Telegram is the first external channel to integrate.** WhatsApp is deprioritized due to TOS risk from unofficial API libraries. Discord is flagged as high-value (ST already has a Smoking Tigers Discord) and should follow Telegram.

Priority order: Telegram → Discord → Signal → iMessage (Nick-specific) → WhatsApp (revisit when official API matures)

## Rationale

- Telegram offers a clean, first-party bot API
- WhatsApp TOS risk is non-trivial for a business operating context
- Discord is already established in the creative/gaming community we are building toward
- iMessage is constrained to Apple users; useful for Nick specifically but not scalable

## Implementation Notes

- External channels are **inbound-only** — agents listen and route, but do not respond directly
- Bidirectional agent access is reserved for internal trusted users via Mattermost
- Credential management: internal ops (Ed/Scout) holds API keys; creator/community manager layer handles channel-level access
- Data retention and community consent (TOS) policies to be defined before launch

## Status History

- 2026-03-14: Approved by Ed

# DEC-20260314-004 — Revenue Points Purchases via TOS Click-Through (Replaces Manual Contracts)

**Decision ID:** DEC-20260314-004
**Title:** Revenue Points Purchases via TOS Click-Through (Replaces Manual Contracts)
**Status:** Approved
**Date:** 2026-03-14
**Owner / Approver:** Ed (Steward)

---

## Context

Currently, revenue points transactions require manual agreement signing, which creates friction and delays. Ed raised the question of whether a TOS click-through on the landing page could serve as the legal agreement for rev points purchases.

## Decision

**Revenue points purchases will use a TOS click-through on the Smoking Tigers website.** When a contributor or investor purchases RP, they agree to the published Terms of Service at point of purchase. This replaces the need for individually executed contracts for standard RP transactions.

## Rationale

- Dramatically reduces friction for onboarding new contributors and investors
- Online payment via TOS is standard practice for similar token/contribution models
- Removes dependency on individual contract execution (which has been causing delays, e.g., Nick's RTPA)
- Keeps the model scalable as the contributor base grows

## Requirements

- Smoking Tigers Terms of Service must be finalized and published before RP sales go live
- TOS must clearly define:
  - What RP are (contribution currency, not equity)
  - USD face value and redemption terms
  - Non-refund / non-transferability terms (if applicable)
  - Governing law
- Stripe integration required for payment processing
- TOS should be versioned in the governance repo

## Action Items

- [ ] Draft Smoking Tigers RP Terms of Service
- [ ] Legal review (Ed or designated steward)
- [ ] Publish to smokingtigers.net at launch
- [ ] Stripe account delivery from SXM (blocking)

## Status History

- 2026-03-14: Approved by Ed

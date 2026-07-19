# DEC-20260314-003 — Smoking Tigers Landing Page: Ownership, Hosting, and Stripe Dependency

**Decision ID:** DEC-20260314-003
**Title:** Smoking Tigers Landing Page: Ownership, Hosting, and Stripe Dependency
**Status:** Approved
**Date:** 2026-03-14
**Owner / Approver:** Ed (Steward)

---

## Context

The Smoking Tigers landing page has been in design/planning. A decision was needed on who owns it, where it lives, and what must be true before it can take payments.

Van has existing Hostinger hosting. The domain smokingtigers.net is registered under Ed's Google Workspace. A Claude Code-generated design exists as the starting point.

## Decision

- **Page owner / webmaster:** Van
- **Hosting:** Hostinger (Van's existing account — fastest path to ship)
- **Domain:** smokingtigers.net (Ed's Google Workspace; DNS to be pointed to Hostinger)
- **Build starting point:** Existing Claude Code design — Ed to hand code to Van
- **Stripe is a hard prerequisite** before any payment functionality goes live

## Rationale

- Van has opinions on the page and the Hostinger account — natural owner
- Using existing infrastructure (Hostinger) avoids new setup time
- smokingtigers.net is already registered; DNS change is a low-friction path
- Stripe is required for online rev points purchases, Nick's next $2500, and all future online payments — must come from SXM before going live

## Requirements Before Launch

1. Ed sends Van the landing page code
2. Van deploys to Hostinger
3. Ed updates DNS: point smokingtigers.net to Hostinger
4. SXM delivers Stripe account + bank account
5. Payments go live via TOS click-through (replaces manual contracts for rev points)

## Open Items

- Rev points TOS language needs to be finalized (click-through replaces manual contracts)
- Potential future integration with Q1.IS for hub pages + login

## Status History

- 2026-03-14: Approved by Ed

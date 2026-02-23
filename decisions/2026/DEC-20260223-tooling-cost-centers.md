# DEC-20260223-tooling-cost-centers

**Decision ID:** DEC-20260223-013
**Title:** Adopt Tooling Cost Centers and Build-vs-Buy Framework
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
As OpenClaw grows, small convenience decisions create hidden costs across SaaS subscriptions, API fees, storage, and operator time. A framework is needed to evaluate and track tooling costs.

## Decision
Adopt a tooling cost center model with structured evaluation questions, build-vs-buy matrix, query budgeting standards, and tool intake process.

## Rationale
- Prevents accidental cost sprawl across integrations
- Provides governance-aware tooling evaluation
- Supports informed build-vs-buy decisions

## Tradeoffs / Risks
- Evaluation overhead may slow adoption of useful tools
- Cost tracking requires ongoing discipline

## Impacts
- All new tools require intake records before adoption
- API-based tools require query budgets and spend caps

## Dependencies
- SysOps agent for operational cost tracking
- LegalOps agent for vendor/terms review support

## References / Sources
- Analysis: `analysis/tooling-cost-centers.md`
- Discussion: Mattermost #executive, 2026-02-23

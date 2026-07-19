# DEC-20260223-ai-resource-stewardship-policy

**Decision ID:** DEC-20260223-001
**Title:** Adopt AI Resource Stewardship and Model Routing Policy
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context

The Smoking Tigers governance model needed a foundational policy for how AI model resources are allocated across human and machine workflows. Without routing discipline, premium hosted model credits are wasted on low-value tasks that local models can handle.

## Decision

Adopt the AI Resource Stewardship and Model Routing policy (Draft v1.0) as the first active policy in the governance repo. All workflows under this governance model must follow a Local-First AI Routing Standard with escalation only when justified by value or risk.

## Rationale

- Preserves scarce premium model credits for high-value work
- Establishes durable operating patterns before scaling
- Aligns with the principle of stewardship over convenience

## Tradeoffs / Risks

- Local models may produce lower-quality outputs on some tasks, requiring human review
- Routing discipline adds a classification step before work begins

## Impacts

- All agents and operators must default to local-first processing
- Premium model use requires justification per escalation criteria

## Dependencies

- Local model infrastructure (Ollama) must be available
- OpenClaw agent configuration must reflect routing rules

## References / Sources

- Policy: `/policies/ai/ai-resource-stewardship.md`
- Discussion: Mattermost #executive, 2026-02-23

# DEC-20260223-knowledge-staging-pipeline

**Decision ID:** DEC-20260223-011
**Title:** Adopt Knowledge Staging Pipeline Workflow
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
Raw inputs (voice memos, transcripts, AI outputs, rough documents) need a repeatable pipeline to become clean, chunked markdown suitable for OpenClaw ingestion and local agent processing.

## Decision
Adopt a local-first knowledge staging pipeline with defined folder structure, processing phases, curation rules, and human review gates.

## Rationale
- Ensures consistent quality of knowledge artifacts
- Optimizes for small local models via proper chunking
- Separates staging from canonical governance workflows

## Tradeoffs / Risks
- Multi-step pipeline adds processing overhead
- Requires discipline in folder and naming conventions

## Impacts
- All raw inputs flow through standardized staging folders
- OpenClaw processes only reviewed, domain-curated staged files

## Dependencies
- Local model runtime (Ollama)
- Governance approval workflows for promoted outputs

## References / Sources
- Workflow: `workflows/knowledge-staging-pipeline.md`
- Discussion: Mattermost #executive, 2026-02-23

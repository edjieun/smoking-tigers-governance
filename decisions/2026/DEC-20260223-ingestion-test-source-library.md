# DEC-20260223-ingestion-test-source-library

**Decision ID:** DEC-20260223-012
**Title:** Adopt Test Document Ingestion and Source Library Workflow
**Status:** Approved
**Date:** 2026-02-23
**Owner / Approver:** Ed (Steward)

## Context
The ingestion pipeline needs real-world validation using test documents before being applied to critical governance materials. A source library pattern supports reusable processing across document types.

## Decision
Adopt a workflow for using test documents (e.g., cookbook OCR pilot) to validate and improve the ingestion pipeline, producing reusable source library artifacts.

## Rationale
- Reduces risk by testing pipeline on non-critical documents first
- Creates reusable patterns for many source types
- Builds automation library from practical experience

## Tradeoffs / Risks
- Side-project test documents may not exercise all production edge cases
- Source library maintenance adds ongoing overhead

## Impacts
- Test documents follow full source registration and derivative tracking
- Processing patterns become reusable automation library entries

## Dependencies
- Knowledge staging pipeline
- OCR tooling (ocrmypdf)

## References / Sources
- Workflow: `workflows/ingestion-test-source-library.md`
- Discussion: Mattermost #executive, 2026-02-23

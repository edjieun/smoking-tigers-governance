# Workflow — Test Document Ingestion and Source Library Development (Cookbook OCR as Pilot Case)
Status: Draft v2.0
Owner: Ed (Steward)
Applies To: Intake testing, document ingestion workflows, OCR/text extraction, source library development
Last Updated: 2026-02-23

## Purpose
Document a practical workflow for using a non-work side project (a Korean cookbook PDF) as a **test document** in the Intake Directory to validate and improve a broader ingestion pipeline.

This workflow is not only about OCR or PDFs.
It is about building a repeatable process for turning mixed source materials into a reusable **source library** that can support:
- local AI workflows
- OpenClaw knowledge staging
- future document processing pipelines
- experimentation and tool validation

The cookbook is a pilot case because it contains real-world challenges:
- scanned content
- OCR variability
- structure extraction needs
- possible multilingual handling
- practical usefulness for testing search, chunking, and cleanup

## Core Principle
**Use real documents (including side projects) to harden the ingestion pipeline before applying it to critical governance/ops materials.**

## Why This Matters
A side-project document can be a safer testing environment for:
- OCR tools
- conversion scripts
- chunking methods
- metadata standards
- source preservation rules
- local agent preprocessing

This reduces risk before applying the same pipeline to work-critical documents.

## Pilot Case (Context)
A Korean cookbook PDF was added to the Intake Directory as a test document.

This was not work-related content, but it is useful as a pipeline test because it can help validate:
- file intake handling
- OCR/searchability
- text extraction quality
- chunking and markdown cleanup
- source library organization
- automation opportunities (scripts/Automator/local agents)

## Design Correction (Updated Endpoint)
The endpoint is **not** just:
- “OCR a PDF”
- “make one searchable file”

The endpoint is:
- a **reusable source library artifact**
- with source preservation, derived outputs, metadata, and processing traceability
- usable for broader ingestion workflows beyond PDF documents

## What This Workflow Produces
This workflow may produce some or all of the following:

### Source Preservation Artifacts
- original source files (images, PDFs, exports)

### Derivative Processing Artifacts
- searchable PDFs
- extracted raw text
- cleaned text
- chunked markdown
- indexing metadata
- processing logs

### Source Library Artifacts
- organized source package
- README / manifest
- quality notes
- reusable examples for future ingestion/testing

## Scope
This document covers:
- using test documents in Intake safely
- OCR as one branch of ingestion
- broader source-library-oriented outputs
- source/derivative separation
- validation and quality checks
- reuse across future document types

This document does **not** cover:
- final publication/redistribution rights
- legal analysis of copyrighted content use
- production-grade multilingual parsing standards (future enhancement)

## Relationship to the Knowledge Staging Pipeline
This workflow is a **feeder** into the broader knowledge staging pipeline.

### This workflow focuses on:
- source handling
- conversion/extraction
- preprocessing artifacts
- test-driven pipeline improvement

### The knowledge staging pipeline focuses on:
- chunked markdown for OpenClaw/local agents
- domain-based staging
- human review and promotion paths

In practice:
- this workflow creates high-quality source derivatives
- the staging pipeline determines what gets routed into operational use

## Source Library Concept (Endpoint)
The final state should resemble a small, reusable source library entry rather than a one-off file.

Each processed source (including side-project test docs) should ideally have:
- preserved originals
- processed derivatives
- metadata/manifest
- quality notes
- processing history
- optional chunked markdown outputs
- clear sensitivity/use notes

This creates a repeatable pattern for many source types, not just cookbooks.

## Recommended Folder Structure (Source Library Oriented)
Use a project-specific processing folder (or source-library batch folder).

Example:
Source-Library/
- `incoming/`
- `sources/`
- `derivatives/`
  - `ocr-pdf/`
  - `extracted-text/`
  - `cleaned-text/`
  - `chunked-md/`
- `metadata/`
- `logs/`
- `archive/`

### Folder Purpose
#### `incoming/`
Landing area for newly added test docs or source files before registration.

#### `sources/`
Preserved originals (never overwritten).
Examples:
- original JPG scans
- merged source PDF
- original downloaded documents

#### `derivatives/ocr-pdf/`
Searchable PDFs and OCR-processed PDF outputs.

#### `derivatives/extracted-text/`
Raw extracted text from OCR PDFs or other converters.

#### `derivatives/cleaned-text/`
Cleaned and corrected text outputs.

#### `derivatives/chunked-md/`
Chunked markdown files for local agent/OpenClaw staging experiments.

#### `metadata/`
README, manifests, language notes, source descriptors, processing status.

#### `logs/`
Command logs, tool versions, QC notes, errors, retries.

#### `archive/`
Retired versions, superseded derivatives, old processing batches.

## Source Registration (New Standard Step)
Before processing, register the source as a library item.

Create a metadata file (example):
- `metadata/source-record.md`

Minimum fields:
- Source Title
- Source Type (scanned PDF, image set, transcript, etc.)
- Origin (where it came from)
- Date added to Intake
- Purpose (test / production / reference)
- Language(s)
- Sensitivity
- Processing goals
- Current status

Example:
- Test document for OCR and ingestion pipeline validation
- Side project / non-work
- Candidate for source-library pattern

## File Naming Convention (Updated)
Use names that support source + derivative tracking.

### Standard Pattern
`YYYY-MM-DD_sourcekey_artifacttype_description_v#.<ext>`

Examples:
- `2026-02-22-korean-cookbook_source_merged_v1.pdf`
- `2026-02-22-korean-cookbook_ocr_searchable_v1.pdf`
- `2026-02-22-korean-cookbook_text_extracted_v1.txt`
- `2026-02-22-korean-cookbook_text_cleaned_v1.txt`
- `2026-02-22-korean-cookbook_chunk_recipe-index_v1.md`

## Ingestion Workflow (Broader Than PDF/OCR)

### Phase 1 — Intake and Source Preservation
Goal: preserve the source and define what the test is for.

Steps:
1. Add document/files to Intake (`incoming/`)
2. Move originals to `sources/`
3. Register source metadata in `metadata/`
4. Define processing objective(s):
   - searchable PDF?
   - extracted text?
   - chunked markdown?
   - pipeline stress test?
   - multilingual test?

### Phase 2 — Format Branching (Choose Processing Path)
Not all sources need OCR.

Choose branch based on source type:

#### Branch A — Scanned Images / Scanned PDF (OCR branch)
Use OCR workflow to create searchable and extractable outputs.

#### Branch B — Text-Based PDF / Doc / Export (No OCR needed)
Extract text directly and normalize.

#### Branch C — Mixed Source Bundle (images + notes + exports)
Process each source type separately, then unify in cleaned/chunked outputs.

#### Branch D — Audio/Transcript Source (future branch)
Transcription and cleanup pipeline, then chunk to markdown.

## OCR Branch (Cookbook Pilot Case)
The Korean cookbook PDF (or source JPGs) follows Branch A.

### OCR Goals
- searchable PDF
- selectable text layer (if quality permits)
- extracted text for cleanup and chunking
- quality notes on OCR performance

### Baseline OCR Command (example)
Use `ocrmypdf` on a source PDF derivative, not the only source copy.

```bash
ocrmypdf "sources/2026-02-22-korean-cookbook_source_merged_v1.pdf" "derivatives/ocr-pdf/2026-02-22-korean-cookbook_ocr_searchable_v1.pdf"

# ADR-001 — Obsidian Adopted as Personal Memory Layer

**Date:** 2026-04-18  
**Status:** Accepted  
**Decision ID:** DEC-20260418-001  
**Authors:** Scout (main), Ed Hwang  

---

## Context

The agent memory architecture required a human-readable, locally-hosted memory layer that:
- Persists across agent sessions
- Is auditable and editable by Ed directly
- Integrates with QMD search for agent context retrieval
- Serves as a template for other team members

Multiple options were considered: Notion, plain filesystem, Logseq, Obsidian.

## Decision

Obsidian vault (`stm-obsidian-vault/ed-vault/`) adopted as the primary personal memory layer for Ed Hwang's workspace.

## Rationale

1. **Local-first** — files live on the Mac Mini, not in a cloud silo
2. **Markdown-native** — QMD can index directly, no export step
3. **Git-tracked** — full history, reversible, shareable as template
4. **Plugin ecosystem** — Smart Connections (semantic search) + Copilot (LM Studio) + Obsidian Git
5. **Human-editable** — Ed can read and write directly without agent mediation

## Consequences

- Eva (ea agent) is the primary writer to all folders except `00-Inbox/`
- Ed writes only to `00-Inbox/` — Eva routes from there
- QMD indexes the vault for agent context
- LM Studio uses vault as local RAG context
- This pattern serves as the template for all team members (STE-128)

## Alternatives Rejected

- **Notion** — cloud-dependent, export friction, not directly indexable by QMD
- **Plain filesystem** — lacks semantic search without additional tooling
- **Logseq** — similar to Obsidian but smaller ecosystem, block-based format less portable

---

_Accepted via governance review. Commit to smoking-tigers-governance._

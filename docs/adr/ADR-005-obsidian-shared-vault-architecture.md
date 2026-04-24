# ADR-005 — Obsidian Shared Vault Architecture

**Status:** Accepted  
**Date:** 2026-04-19  
**Decider:** Ed (Steward)  
**Context:** Personal AI Workspace — Obsidian + LM Studio (STE project)

---

## Context

As part of the Personal AI Workspace project, Smoking Tigers adopted Obsidian as the memory layer for the AI agent stack. The initial design proposed separate per-person vaults. During implementation, a conflict was identified: if each team member has an isolated vault, the EA agent (Eva, Rosie, etc.) would need to sync across separate vaults to access shared org knowledge, introducing latency and duplication.

---

## Decision

Use a **single shared Obsidian vault** (`stm-obsidian-vault/`) with **nested personal sub-vaults** under `members/<name>/`.

### Structure

```
stm-obsidian-vault/
  00-Shared/
    01-Projects/      ← Linear sync (all projects, daily)
    02-People/        ← Notion Team Directory + Google Contacts (weekly)
    04-Governance/    ← GitHub smoking-tigers-governance (daily git pull)
    05-Reference/     ← QMD srv exports (weekly)
  members/
    ed/
      00-Inbox/       ← human write zone
      03-Meetings/    ← meeting notes
      06-Memory/      ← EA memory namespace
      07-Outputs/     ← AI-generated docs
      AGENTS.md
    christine/
      ...             ← same structure, Rosie writes here
    basil/
    van/
  templates/
  README.md
```

### Write Ownership

| Path | Writer |
|---|---|
| `00-Shared/` | EA agents (automated sync) + git |
| `members/<name>/00-Inbox/` | Human only |
| `members/<name>/03-Meetings/` | EA agent + human |
| `members/<name>/06-Memory/` | EA agent only |
| `members/<name>/07-Outputs/` | EA agent |

---

## Rationale

1. **EA immediate access** — Eva operates at the vault root. No sync handoff, no delay. She reads shared org context and writes to the correct personal namespace in one operation.

2. **Single source of truth for org knowledge** — Projects, people, governance, and reference live once in `00-Shared/`. Every team member and every AI model sees the same data.

3. **Personal namespace isolation** — Each member's inbox, memory, and outputs are scoped to `members/<name>/`. No cross-contamination. EA agents can only write to their assigned member's namespace.

4. **LM Studio context** — By opening Obsidian at the vault root, LM Studio (via Smart Connections) indexes both shared org knowledge and personal notes. This gives each person full context without manual configuration.

5. **Scalable pattern** — Adding a new team member is additive: create `members/<name>/`, configure their EA agent path, done. No vault migration, no restructuring.

6. **Rosie / Christine parity** — The same pattern applies to all EA-member pairs. Rosie writes to `members/christine/`, reads `00-Shared/`. Identical architecture, different namespace.

---

## Consequences

- **Positive:** Eva has immediate, zero-latency access to all vault content. No separate sync job needed between EA vault and member vault.
- **Positive:** Shared org knowledge (Linear projects, team directory, governance) is maintained once and available to all.
- **Positive:** LM Studio gives each person AI that knows both the org and their personal context.
- **Neutral:** Obsidian should be opened at the vault root (`stm-obsidian-vault/`), not at the member subfolder, to get full LM Studio context. This is documented in the User Guide.
- **Neutral:** EA agents must be configured with explicit path scoping — they write to `members/<name>/`, never to another member's namespace.
- **Risk (mitigated):** A misconfigured EA could write to the wrong member namespace. Mitigated by explicit path configuration in each agent's AGENTS.md and agentDir config.

---

## Alternatives Considered

### Separate vault per person
Rejected. Eva would need a separate sync process to share org-level knowledge (projects, governance) across vaults. Adds latency and maintenance burden. LM Studio context would be limited to each person's isolated vault.

### Shared vault, flat structure (no members/ subfolder)
Rejected. Without personal namespaces, EA memory and outputs would intermingle across team members, making context retrieval unreliable and creating privacy concerns.

---

## Implementation

- User Guide updated: `stm-obsidian-vault/06-SOPs/personal-ai-workspace-guide.md` (v1.1)
- Vault template updated: `stm-obsidian-vault/templates/personal-vault-template/` (template-v1.1)
- EA agent configs to be updated: `agentDir` and memory paths point to `members/<name>/`

---

## References

- Personal AI Workspace project: <https://linear.app/smoking-tigers/project/personal-ai-workspace-obsidian-lm-studio-1984f67782cd>
- DEC-20260417-001 — QMD and Obsidian as memory layer
- ADR-001 — Agent architecture

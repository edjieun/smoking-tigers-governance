# Naming Conventions — `decisions/` and Governance Documents

Applies to every document in the governance repository. One purpose per prefix so files are findable, sortable, and reviewable at a glance.

## Where things live

| Type | Folder | Prefix | Example |
|---|---|---|---|
| Architecture Decision Record | `decisions/adr/` | `ADR-NNN` | `ADR-004-human-in-the-loop-policy.md` |
| Governance Decision Record | `decisions/YYYY/` | `DEC-YYYYMMDD[-NNN]` | `DEC-20260303-003-notion-api-integration.md` |
| DACI log entry | `decisions/daci/` | `YYYY-MM-DD-<slug>` | `decisions/daci/2026-08-15-agent-harness-repo.md` |
| Decision incident log | `decisions/logs/incidents/` | `YYYY-MM-DD_<slug>.md` | `2026-02-24_sonnetops-agent-removal.md` |
| Standard Operating Procedure | `sops/` | `SOP-NNN-<slug>` | `SOP-001-executing-contracts.md` |
| Policy | `policies/` | `POL-NNN-<slug>` (or semantic) | `policies/security/mattermost-access.md` |
| Role definition | `roles/definitions/` | `ROLE-<slug>` | `roles/definitions/treasurer.md` |
| Template | `templates/` | `TPL-<type-slug>` | `templates/gdr.template.md` |
| Contract / Agreement | `agreements/` | `CTR-YYYY-NNN-<slug>` | `agreements/CTR-2026-003-contributor-agreement.md` |
| Glossary term | `docs/glossary.md` (single file) | `## <Term>` | inline anchor |

## 2. Prefixes and numbering

| Prefix | Meaning | Numbering |
|---|---|---|
| `ADR-NNN` | Architecture Decision Record (technical) | sequential per-record number |
| `DEC-YYYYMMDD` | Governance Decision Record (org-level) | `-NN-` counter if multiple same day; `[‑NNN]` later counter |
| `DACI` | Decision-Accountable-Consulted-Informed log entry | dated + slug |
| `SOP-NNN` | Standard Operating Procedure | sequential, `SOP-001` upward |
| `POL-NNN` | Enforceable policy | optional `[‑NNN]`; often nested by subfolder |
| `ROLE-<slug>` | Role definition | lowercase slug |
| `TPL-<slug>` | Document template | lowercase slug |
| `CTR-YYYY-NNN` | Contract / MOU / agreement | year + sequential number |

## 3. Slug rules

- lowercase, hyphen-separated words
- no spaces, no leading zeros unless part of a number
- keep it short and descriptive of the *subject* (not the status)

Good: `SOP-002-disbursing-funds.md`
Bad: `SOP-2-final-v2-corrected.md`

## 4. Parallels between ADR and GDR

- **ADR** — architectural/technical decisions (system design, tooling, schema). Lives in `decisions/adr/`.
- **GDR** — governance/org decisions (policy, roles, spending, process). Lives in `decisions/YYYY/` with `DEC-` prefix.
- **DACI** — meeting-driven decision records extracted from transcripts (see pipeline below).

Prefer an ADR when the decision is about *how the system works*; a GDR when it is about *how the org governs*. When in doubt, ask the accountable role owner.

## 5. Status values (YAML frontmatter)

`draft` → `proposed` → `active` → `superseded` (never delete; supersede explicitly).
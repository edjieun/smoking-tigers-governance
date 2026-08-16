# decisions/

Governance Decision Records (GDRs), Architecture Decision Records (ADRs), the DACI decision log, and decision-related incident history.

- **Naming conventions:** see [NAMING_CONVENTIONS.md](NAMING_CONVENTIONS.md) — read this first.
- **Decision extraction pipeline:** see [sops/SOP-004-decision-extraction.md](../sops/SOP-004-decision-extraction.md).

## Layout

| Path | Contents |
|---|---|
| `YYYY/` (e.g. `2026/`) | Governance Decision Records, `DEC-YYYYMMDD[-NNN]-<slug>.md` |
| `adr/` | Architecture Decision Records, `ADR-NNN-<slug>.md` |
| `daci/` | DACI log entries extracted from meetings, `YYYY-MM-DD-<slug>.md` |
| `logs/incidents/` | Decision incident log entries |

## Decision record anatomy

Every GDR/ADR carries YAML frontmatter (`id`, `title`, `type`, `status`, `owner`, `authors`) and a body with: **Context → Decision → Consequences**. See `templates/gdr.template.md` for the full template.

## Process

1. Draft (template) → 2. Propose (PR, per `sops/SOP-004-decision-extraction.md`) → 3. Decide (sign-off per `roles/delegation-of-authority.md`) → 4. `active` → 5. supersede when outdated.
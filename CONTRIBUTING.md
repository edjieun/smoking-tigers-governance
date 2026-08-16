# Contributing to the STE Governance Repository

This repository is the shared governance layer for Smoking Tigers Enterprises. Before contributing, read the [User Guide](guides/USER_GUIDE.md) and the [Data Classification & Privacy Policy](guides/PRIVACY_HANDLING.md).

## Ground rules

1. **Zero private data.** This repository is **public**. Never commit internal (L2) or confidential (L3) data, credentials, session memory, or personal files. See `guides/PRIVACY_HANDLING.md`.
2. **Follow the template suite.** Use the templates in `templates/` (policy, proposal, contract/MOU, financial request, SOP, GDR) for new documents.
3. **Decisions go in `decisions/`.** Record governance decisions as GDRs with the naming convention in `decisions/NAMING_CONVENTIONS.md`. ADRs live in `decisions/adr/`.
4. **Sign your commits.** Commits must be cryptographically signed to preserve the audit record. See `guides/GIT_RECORDKEEPING.md`.
5. **Proposals use the template.** Submit proposals via `templates/proposal.template.md` following the issuance workflow in `.github/`.

## Workflow

1. Open an Issue (or Work Package in OpenProject for agent-driven work).
2. For new/changed policy: draft using the matching template, get steward or delegated-role sign-off per `roles/delegation-of-authority.md`.
3. Open a Pull Request — watch `CODEOWNERS` so the right role owners auto-review.
4. CI validates YAML frontmatter and scans for secrets/PII. Resolve any findings.
5. Merge only after approval, then record the decision if material.

## Document metadata

Every policy/SOP/GDR carries YAML frontmatter: `id`, `title`, `type`, `status` (`draft` → `proposed` → `active`), `owner`, `authors`. Keep `status` current as documents evolve.
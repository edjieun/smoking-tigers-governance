# Smoking Tigers Governance Repository

The **governance layer** for Smoking Tigers Enterprises (STE) and its AI-assisted operating system. This public repository holds the shared policies, procedures, roles, decisions, templates, and operating standards that govern the collective.

> **This is a governance repository — not a knowledge dump.** Operational data, personal notes, and private records do not belong here. See [Privacy Handling](guides/PRIVACY_HANDLING.md).

## Repository layout

| Path | Purpose |
|---|---|
| `ai/` | Instructions and guardrails for AI agents operating under STE governance (`AGENT_GUIDE.md`, `system-prompt.md`, `context-index.json`) |
| `charters/` | High-level organizational scopes (board, executive, treasury) |
| `decisions/` | Governance Decision Records (GDRs), ADRs, DACI log, and decision history |
| `financial/` | Financial governance: spending limits, procurement, treasury/multisig, audit |
| `guides/` | User guides and SOPs (onboarding, git recordkeeping, privacy, API conventions) |
| `policies/` | Enforceable policies (data classification, engineering, security) |
| `roles/` | RACI matrix, delegation of authority, role definitions |
| `sops/` | Standard Operating Procedures (numbered) |
| `templates/` | Multi-document template suite (policy, proposal, contract/MOU, financial request, SOP, GDR) |
| `members/` | Member registry and device records (personal files are gitignored) |
| `agreements/` | Agreements, MOUs, invoices |
| `analysis/` | Working analysis documents |

See the [wiki Table of Contents](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ops/wiki/wiki-smoking-tigers-start-here/toc) for the authoritative governance structure.

## Agent harness files

Agent runtime configs, skills, and shared harness templates live in the separate **`edjieun/ste-agent-harness`** repository, governed by the rules here. See the [Agent Harness Guide](ai/AGENT_GUIDE.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

![LICENSE](LICENSE)
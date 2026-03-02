# #knowledge Channel SOP

**Status:** Active v1.0
**Owner:** Ed (Steward)
**Last Updated:** 2026-03-02
**Bot:** Knowledge Ops (`st-build-knowledge-ops-bot`)

---

## Purpose

`#knowledge` is where knowledge work is **completed and documented**.

It is not a discussion channel. It is not a staging area.
It is the output surface for the knowledge pipeline — and the intake surface for manually added data.

---

## Who Uses This Channel

| Actor | Role |
|-------|------|
| Ed (Steward) | Pastes raw project content, signals intake, reviews outputs |
| knowledge-ops bot | Processes intake, posts completed summaries and bibles |
| Scout | Routes completed knowledge work here; coordinates intake |

---

## How to Add Data Manually (Ed's Workflow)

Paste content directly into #knowledge. Lead with a one-line signal so knowledge-ops knows what it is.

### Signal Format

```
[PROJECT] [TYPE] — [brief description]
[content]
```

### Examples

```
TLN OVERVIEW — Trade Like Nick project summary from Notion
[paste content]
```

```
TLN BIBLE — Full knowledge bible draft
[paste content]
```

```
TLN FINANCIALS — RP budget and cash structure (EA to handle)
[paste content]
```

```
STM POLICY — Board meeting notes 2026-03-01
[paste content]
```

### Supported Types

| Type Tag | Meaning | Processed By |
|----------|---------|-------------|
| `OVERVIEW` | Project summary or status | knowledge-ops |
| `BIBLE` | Full project knowledge bible | knowledge-ops |
| `NOTES` | Raw meeting notes or context | knowledge-ops |
| `JOBS` | Atomic job definitions | knowledge-ops |
| `ACTIVATION` | Activation eligibility docs | knowledge-ops → Scout reviews |
| `FINANCIALS` | RP/cash/revenue data | EA only — knowledge-ops flags and defers |
| `POLICY` | Draft policy content | Scout → governance-ops |
| `RAW` | Unclassified dump — classify it for me | knowledge-ops |

---

## What knowledge-ops Posts Here

After processing any intake, knowledge-ops posts a completion summary:

```
✅ [PROJECT] [TYPE] processed — [date]
- Summary: [1-2 lines]
- Artifacts updated: [file paths]
- Activation status: [ELIGIBLE / NOT ELIGIBLE / PARTIAL — missing: X]
- Flagged items: [any restricted content, ambiguities]
- Next: [recommended action if any]
```

For knowledge bibles:
```
📚 [PROJECT] Knowledge Bible updated — [date]
- Version: v[n]
- Sections: [list]
- Location: knowledge-bible/[project]-bible.md
- RAG ready: YES / NO
```

---

## What Happens After a Paste

1. knowledge-ops picks up the content (via HEARTBEAT or Scout trigger)
2. Classifies the content type
3. Processes and writes to governance repo
4. Posts completion summary back here
5. Flags anything requiring Ed's review

Ed does not need to take any action after pasting — unless the summary flags something.

---

## Activation Eligibility Reports

When a project's knowledge reaches sufficient completeness, knowledge-ops posts:

```
🚦 [PROJECT] Activation Eligibility Check — [date]

Tier 1 (Foundation):     ✅ Complete
Tier 2 (Economic):       ⚠️ Partial — missing: cash structure, RTPA
Tier 3 (Governance):     ❌ Not started
Tier 4 (Operations):     ❌ Not started

Status: NOT ELIGIBLE
Next gaps to close: [specific items]
```

These are advisory. Ed approves all activations.

---

## Channel Rules

- **No casual discussion** — use #executive for that
- **No credentials or secrets** — ever
- **Financial/RP data** — always tag `FINANCIALS`; EA handles, not knowledge-ops
- **One project per paste** — don't mix projects in a single message
- **Governance decisions** — route to #governance or signal Scout for promotion

---

## Current Active Projects

| Project | Status | Knowledge Bible |
|---------|--------|----------------|
| Trade Like Nick | Intake in progress | Pending first paste |
| Smoking Tigers AI | Active | `knowledge-bible/STE_Knowledge_Bible_v0.3.md` |

---

## Intake Directory (Alternative to Paste)

If content is too long to paste: drop a `.md` or `.zip` file in `~/Desktop/intake/`
knowledge-ops picks it up on next heartbeat cycle automatically.
Signal in #knowledge what you dropped so the output comes back here.

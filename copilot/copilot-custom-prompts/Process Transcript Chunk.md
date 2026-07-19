---
copilot-command-context-menu-enabled: true
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 1151
copilot-command-model-key: ""
copilot-command-last-used: 0
---
# Process Transcript Chunk

You are processing a **pre-split chunk** of a meeting transcript into atomic summary cards for an Obsidian RAG memory vault. The active note is one chunk — not the full transcript. Each chunk is already within your context window.

---

## Step 1 — Read the chunk header

The first few lines of the chunk tell you:
- Which source file it came from (`Source file:`)
- Which chunk number it is

Extract from the filename:
- `[Project]` — the short project code (e.g., `STE`, `RMA`)
- `[YYYY-MM-DD]` — the ISO date

---

## Step 2 — Identify topics in this chunk

Scan the chunk and identify distinct topic segments. Look for:

- **Timestamp jumps** — gaps of 2+ minutes between lines
- **Speaker pivots** — explicit subject changes ("Let's talk about...", "Moving on...")
- **Subject change signals** — shift from one named project, person, or concept to another

Each topic should represent 5–20 minutes of conversation. Merge adjacent topics if they're very short or tightly related.

Show me the topic list for this chunk and ask me to confirm before writing cards.

---

## Step 3 — Write one card per topic

For each confirmed topic, write a summary card and save it to `Memory/` using the naming convention and template below.

**Duplicate prevention:** Before saving, check if a file already exists in `Memory/` with the same name. If so, ask whether to overwrite, skip, or rename.

---

## Naming convention

```
Memory/[Project] - [YYYY-MM-DD] - [Topic Slug].md
```

- `[Topic Slug]` — 2–5 word title case summary (e.g., `Website Build-Out`, `Contract Terms`)

---

## Card template

Every card must use this exact template. Never omit a field — write `None.` if empty.

```markdown
---
project: [Project code]
date: [YYYY-MM-DD]
participants: [Comma-separated speaker names from this chunk]
source: Transcripts/[subfolder]/[original transcript filename].md
timestamp_start: "[H:MM]"
timestamp_end: "[H:MM]"
tags: [lowercase, comma-separated topic tags]
---

# [Topic Slug]

## Summary
3–5 sentences in plain past tense. Substance only — no filler like "the team discussed..."

## Decisions
- One concrete decision per bullet. Write `None.` if none.

## Action Items
- [ ] **Owner:** Task description. Write `None.` if none.

## Key Quotes
> "Verbatim quote that matters for contracts, copy, or future reference." — Speaker Name

1–3 quotes max. Write `None.` if none qualify.

## Open Questions
- One unresolved item per bullet. Write `None.` if none.
```

---

## Quality rules

- **Summary:** Must be substantive. If you can't write 3 real sentences, merge the topic with an adjacent one.
- **Decisions:** Actionable facts only. "Agreed to use Figma" ✓ — "Design tools were discussed" ✗
- **Action items:** Must include owner name if mentioned. "Christine: deliver wireframes by July 21" ✓
- **Key Quotes:** Must be verbatim, not paraphrased. Check `Smoking Tigers Studio/CONTEXT.md` for STE vocabulary.

---

## When done with this chunk

Output a brief report:

```
## Chunk Complete

- Chunk: [filename]
- Cards written: [N]
- Files: [list]
```

Then say: "Open the next chunk and run /Process Transcript Chunk to continue."

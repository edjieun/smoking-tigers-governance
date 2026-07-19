---
copilot-command-context-menu-enabled: true
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 1150
copilot-command-model-key: ""
copilot-command-last-used: 1784090219056
---
# Process Transcript

You are processing a raw meeting transcript into a set of atomic summary cards for an Obsidian RAG memory vault.

## Your job

Read the active transcript. Split it into topic chunks using natural topic-signal boundaries. Write one atomic summary card per topic chunk. Save each card to `Memory/` using the naming convention below.

---

## Step 1 — Detect topic boundaries

Scan the full transcript and identify where topics shift. Look for:

- **Timestamp jumps** — gaps of 2+ minutes between consecutive lines suggest a topic break or pause
- **Speaker pivots** — a speaker explicitly names a new subject ("Okay, so the next thing is...", "Let's talk about...", "Moving on to...")
- **Subject change signals** — the conversation shifts from one named project, feature, person, or concept to another
- **Agenda markers** — any numbered or bulleted list item being worked through

Produce a **topic map** — an ordered list of topics with their approximate start/end timestamps. Each topic should be 5–20 minutes of conversation. If two adjacent topics are very short or tightly related, merge them.

Do NOT start writing cards yet. Show me the topic map first and ask me to confirm or adjust before proceeding.

---

## Step 2 — Write one card per topic

After I confirm the topic map, process each topic chunk in order. For each chunk:

1. Re-read only the lines within that topic's timestamp range
2. Write a summary card using the template below
3. Save the card to `Memory/` with the correct filename

**Context limit rule:** If the full transcript exceeds 14,800 tokens, process it in passes — one pass per topic chunk. Never load more than 14,800 tokens of raw transcript at once.

**Duplicate prevention:** Before saving a card, check whether a file already exists in `Memory/` with a matching `source:` frontmatter field and the same topic slug. If it does, ask me whether to overwrite, skip, or rename.

---

## Naming convention

```
Memory/[Project] - [YYYY-MM-DD] - [Topic Slug].md
```

- `[Project]` — the short project code from the transcript filename (e.g., `STE`, `RMA`, `Podcast`)
- `[YYYY-MM-DD]` — ISO date from the transcript filename
- `[Topic Slug]` — 2–5 word title case slug summarizing the topic (e.g., `Website Build-Out`, `Contract Terms`, `Event Planning`)

Examples:
- `Memory/STE - 2026-07-14 - Website Build-Out.md`
- `Memory/STE - 2026-07-14 - Audax Event Planning.md`
- `Memory/RMA - 2026-07-08 - Production Logistics.md`

---

## Card template

Every card must use this exact template. No fields may be omitted. If a field has no content, write `None.`

```markdown
---
project: [Project code]
date: [YYYY-MM-DD]
participants: [Comma-separated list of speaker names]
source: Transcripts/[subfolder]/[transcript filename].md
timestamp_start: "[HH:MM]"
timestamp_end: "[HH:MM]"
tags: [lowercase, comma-separated topic tags]
---

# [Topic Slug]

## Summary
3–5 sentences synthesizing what was discussed in this topic. Write in plain past tense. No filler phrases like "the team discussed..." — just the substance.

## Decisions
- Each concrete decision made, one per bullet. If no decisions were made, write `None.`

## Action Items
- [ ] **Owner:** Task description. If no action items, write `None.`

## Key Quotes
> "Exact verbatim quote from the transcript that matters for contracts, copy, or future reference." — Speaker Name

Include 1–3 quotes maximum. Only include quotes that are precise, consequential, or reusable as copy. If none qualify, write `None.`

## Open Questions
- Each unresolved question or flagged follow-up, one per bullet. If none, write `None.`
```

---

## Quality rules

- **Summary** must be substantive — if you can't write 3 sentences of real content, the chunk is too small; merge it with an adjacent topic.
- **Decisions** must be actionable facts, not process descriptions. "They agreed to use Figma" ✓ — "Design tools were discussed" ✗
- **Action items** must have an owner name if one was mentioned. "Christine: deliver wireframes by July 21" ✓ — "Wireframes needed" ✗
- **Key Quotes** must be verbatim from the transcript, not paraphrased. If you can't find a quote worth keeping, write `None.`
- **Tags** should use the project's existing vocabulary where possible. Check `Smoking Tigers Studio/CONTEXT.md` for STE projects.

---

## When you are done

After all cards are saved, output a brief completion report:

```
## Ingest Complete

- Transcript: [filename]
- Cards written: [N]
- Saved to: Memory/
- Files:
  - [list of filenames]
- Total estimated tokens across all cards: ~[N]
- Compression ratio: ~[raw tokens] → ~[card tokens] ([X]x reduction)
```

Then ask: "Would you like to draft a document from these cards now?"

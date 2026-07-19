# Memory — RAG Corpus

This folder contains atomic summary cards extracted from meeting transcripts. It is the **only** folder that should be indexed by your RAG plugin. The `Transcripts/` folder is excluded from indexing.

---

## Structure

Each card is a single `.md` file named:

```
[Project] - [YYYY-MM-DD] - [Topic Slug].md
```

Examples:
- `STE - 2026-07-14 - Website Build-Out.md`
- `STE - 2026-07-14 - Audax Event Planning.md`
- `RMA - 2026-07-08 - Production Logistics.md`

---

## Frontmatter fields

| Field | Description |
|---|---|
| `project` | Short project code: `STE`, `RMA`, `Podcast`, etc. |
| `date` | ISO date of the source meeting: `YYYY-MM-DD` |
| `participants` | Speaker names present in this topic segment |
| `source` | Relative path to the source transcript file |
| `timestamp_start` | Approximate start time of this topic in the recording |
| `timestamp_end` | Approximate end time of this topic in the recording |
| `tags` | Lowercase topic tags for semantic grouping |

---

## How to add new cards

1. Open the transcript you want to process in Obsidian
2. Open Copilot chat
3. Run the **Process Transcript** custom prompt (`copilot/copilot-custom-prompts/Process Transcript.md`)
4. Confirm the topic map when prompted
5. Cards are saved automatically to this folder

---

## How to query

### Project-scoped (default)
Filter by `project` frontmatter in your RAG plugin or Dataview:

```dataview
LIST
FROM "Memory"
WHERE project = "STE"
SORT date DESC
```

### Cross-project (opt-in)
Remove the project filter to retrieve across all projects:

```dataview
LIST
FROM "Memory"
SORT date DESC
```

### By tag
```dataview
LIST
FROM "Memory"
WHERE contains(tags, "website")
```

### All open action items across all projects
```dataview
TASK
FROM "Memory"
WHERE !completed
SORT date DESC
```

---

## Source transcripts

Raw transcripts live in `Transcripts/` and are **excluded from RAG indexing**. Each card links back to its source via the `source` frontmatter field and `timestamp_start`/`timestamp_end` for drill-in if needed.

| Convention | Folder |
|---|---|
| `Transcripts/STE/` | Smoking Tigers Studio sessions |
| `Transcripts/RMA/` | RMA sessions |
| `Transcripts/Podcast/` | Podcast sessions |

---

## Naming conflicts

If two topics from the same meeting share a similar slug, append a number:
- `STE - 2026-07-14 - Website Build-Out.md`
- `STE - 2026-07-14 - Website Build-Out 2.md`

In practice this should be rare — if two chunks feel like the same topic, merge them before writing the card.

---
id: ADR-0005
title: ZeroClaw SQLite Database Schema
status: Draft
date: 2026-07-19
tier: On Premise
op_task: https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-ai-buildout/work_packages/258
---

# ADR-0005: ZeroClaw SQLite Database Schema

## Status
Draft — schema defined, pending implementation

## Context

ZeroClaw uses SQLite as its memory backend. Before adding integrations (email ingestion, journal database, team onboarding), we need a stable schema. Adding tables ad-hoc leads to rebuilds when the model changes.

This ADR defines the canonical schema. Every new data source (email, transcripts, daily notes, URLs) writes to this schema. ZeroClaw's hybrid search (vector + FTS5) indexes the `content` field of all entities.

## Schema

### Core entities (aligned with ADR-0001 domain model)

```sql
-- Members: humans and agents in the system
CREATE TABLE members (
  id          TEXT PRIMARY KEY,        -- e.g. "ed-hwang", "scout"
  name        TEXT NOT NULL,
  email       TEXT,                    -- @quorum.one address
  type        TEXT NOT NULL,           -- "human" | "agent"
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Projects: tracked efforts (matches OP projects)
CREATE TABLE projects (
  id          TEXT PRIMARY KEY,        -- matches OP project identifier
  op_id       INTEGER,                 -- OP project ID (e.g. 12)
  name        TEXT NOT NULL,
  tier        TEXT,                    -- "network" | "on-premise" | "on-device"
  status      TEXT DEFAULT 'active',   -- "active" | "blocked" | "complete"
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Meetings: events that produce transcripts
CREATE TABLE meetings (
  id          TEXT PRIMARY KEY,
  project_id  TEXT REFERENCES projects(id),
  title       TEXT NOT NULL,
  date        DATE NOT NULL,
  source      TEXT,                    -- "fathom" | "google-meet" | "zoom" | "manual"
  source_url  TEXT,                    -- Fathom link or recording URL
  op_wp_id    INTEGER,                 -- OP Milestone WP ID
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Transcripts: raw meeting text, content searchable
CREATE TABLE transcripts (
  id          TEXT PRIMARY KEY,
  meeting_id  TEXT REFERENCES meetings(id),
  content     TEXT NOT NULL,           -- raw transcript text (indexed by FTS5)
  content_vec BLOB,                    -- nomic-embed vector
  mm_post_id  TEXT,                    -- Mattermost post ID where transcript was submitted
  op_wp_id    INTEGER,                 -- OP Task WP ID
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tasks: extracted from transcripts or created directly
CREATE TABLE tasks (
  id          TEXT PRIMARY KEY,
  project_id  TEXT REFERENCES projects(id),
  transcript_id TEXT REFERENCES transcripts(id),
  subject     TEXT NOT NULL,           -- indexed by FTS5
  content     TEXT,
  content_vec BLOB,
  assignee_id TEXT REFERENCES members(id),
  status      TEXT DEFAULT 'open',     -- "open" | "in-progress" | "done" | "blocked"
  due_date    DATE,
  op_wp_id    INTEGER,                 -- OP Task WP ID
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Decisions: agreements extracted from transcripts
CREATE TABLE decisions (
  id            TEXT PRIMARY KEY,
  project_id    TEXT REFERENCES projects(id),
  transcript_id TEXT REFERENCES transcripts(id),
  content       TEXT NOT NULL,         -- indexed by FTS5
  content_vec   BLOB,
  op_wp_id      INTEGER,
  created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Open questions: raised but unresolved
CREATE TABLE open_questions (
  id            TEXT PRIMARY KEY,
  project_id    TEXT REFERENCES projects(id),
  transcript_id TEXT REFERENCES transcripts(id),
  content       TEXT NOT NULL,         -- indexed by FTS5
  content_vec   BLOB,
  resolved_at   DATETIME,
  resolution    TEXT,
  op_wp_id      INTEGER,
  created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Memory cards: atomic summary files (from Memory/ folder)
CREATE TABLE memory_cards (
  id          TEXT PRIMARY KEY,
  project_id  TEXT REFERENCES projects(id),
  title       TEXT NOT NULL,
  content     TEXT NOT NULL,           -- indexed by FTS5
  content_vec BLOB,
  source_file TEXT,                    -- path to .md file in Memory/
  date        DATE,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Journal entries: Ed's daily work record (from Obsidian notes)
CREATE TABLE journal_entries (
  id              TEXT PRIMARY KEY,
  date            DATE NOT NULL UNIQUE,
  session_type    TEXT,                -- "planning" | "execution" | "review" | "grilling"
  summary         TEXT NOT NULL,       -- indexed by FTS5
  summary_vec     BLOB,
  key_decisions   TEXT,                -- JSON array of decision strings
  linked_op_ids   TEXT,                -- JSON array of OP WP IDs
  linked_docs     TEXT,                -- JSON array of doc paths
  source_file     TEXT,                -- path to original YYYY-MM-DD.md
  created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Agent jobs: scheduled + triggered jobs run by Scout
CREATE TABLE agent_jobs (
  id          TEXT PRIMARY KEY,
  name        TEXT NOT NULL,           -- e.g. "openrouter-cost-tracker"
  agent       TEXT,                    -- "scout"
  schedule    TEXT,                    -- cron expression
  last_run    DATETIME,
  last_status TEXT,                    -- "ok" | "error"
  last_output TEXT,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Intake items: URL/email/message-forward inputs
CREATE TABLE intake_items (
  id          TEXT PRIMARY KEY,
  type        TEXT NOT NULL,           -- "url" | "email" | "message" | "file"
  source      TEXT,                    -- originating channel or address
  content     TEXT NOT NULL,           -- raw content, indexed by FTS5
  content_vec BLOB,
  summary     TEXT,                    -- agent-generated summary
  project_id  TEXT REFERENCES projects(id),
  op_wp_id    INTEGER,
  processed_at DATETIME,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### FTS5 virtual tables (search index)

```sql
CREATE VIRTUAL TABLE fts_search USING fts5(
  entity_type,  -- "transcript" | "task" | "decision" | "journal" | "memory_card" | "intake"
  entity_id,
  content,
  tokenize='porter unicode61'
);
```

## Search behavior

ZeroClaw hybrid search: `score = (vector_similarity * 0.7) + (fts5_rank * 0.3)`

When Scout calls `search_memory "what was decided about X"`:
1. Generate embedding via nomic-embed
2. cosine similarity against all `content_vec` fields
3. FTS5 keyword match against `fts_search`
4. Merge and rank by hybrid score
5. Return top N results with entity type + ID

## Migration

Existing OpenClaw memory cards (in `Memory/` folder) → `memory_cards` table via:
```
zeroclaw migrate openclaw --source ~/.openclaw/workspace/ --dry-run
zeroclaw migrate openclaw --source ~/.openclaw/workspace/
```

## Consequences

- All new integrations (email, URL, journal) write to this schema before going live
- Schema changes require a migration script — no ad-hoc ALTER TABLE
- ZeroClaw DB file location: `~/.zeroclaw/data/memory.db` (confirm in config.toml)

## Related

- `ADR-0001`: Domain model — entity definitions match this schema
- `ADR-0003`: ZeroClaw ↔ OpenClaw integration — requires schema to be stable first
- OP #262: Journal schema extension task
- OP #259: Email channel config (depends on intake_items table)

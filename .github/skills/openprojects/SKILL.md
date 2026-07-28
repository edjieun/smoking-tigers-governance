---
name: openprojects
description: "Create, update, or comment on OpenProjects work packages for STE. Use when: creating a new task or WP, logging progress on an open WP, closing a WP, querying open tasks, or turning session output into OP work packages."
argument-hint: "e.g. 'create WP for X' or 'close WP#123' or 'list open WPs'"
---

# OpenProjects Skill

## Connection

```
Base URL:  https://ste-business-server.tailebe6d3.ts.net:8080
Auth:      Basic — base64("apikey:{OPENPROJECTS_COPILOT_API_KEY}")
           ⚠️ Bearer token does NOT work.
Key:       OPENPROJECTS_COPILOT_API_KEY in ~/.ste-secrets/.env
Agent:     Copilot (#10) — copilot.ste.eh@quorum.one
```

```bash
source ~/.ste-secrets/.env
AUTH=$(echo -n "apikey:$OPENPROJECTS_COPILOT_API_KEY" | base64)
```

### Admin operations (user management, etc.)

Use the Scout/admin key for operations requiring elevated permissions (user lock/unlock, admin-only endpoints):

```bash
source ~/.ste-secrets/.env
ADMIN_AUTH=$(echo -n "apikey:$OPENPROJECTS_API_KEY" | base64)
```

- `OPENPROJECTS_API_KEY` = Scout key (ed@quorum.one) — admin-level, used to deploy the OP instance
- `OPENPROJECTS_COPILOT_API_KEY` = Copilot agent key — use for all normal WP operations
- User deletion via API returns 403 (OP design) — use `PATCH /api/v3/users/{id}` with `{"status":"locked"}` to disable accounts

---

## VS Code Extension (bitswar.openproject v2.0.0)

Configured in VS Code user settings (`openproject.base_url` + `openproject.token`).
Token: Ed's personal OP token — dedicated to this extension (created 2026-07-23), stored in VS Code settings only.

**Use the extension for (Ed — manual/GUI):**
- Browse WPs by project, status, or text — live sidebar panel
- Set WP status inline without a terminal

**Use curl API for (Copilot agent actions):**
- Creating WPs
- Posting comments / activities
- Attaching files
- Any programmatic/agent action → always uses `OPENPROJECTS_COPILOT_API_KEY`, never the extension token

> The extension token is Ed's personal credential. Copilot never reads or uses it.

---

## Projects

| ID | Name |
|---|---|
| 3 | STE Operations (catch-all) |
| 6 | STE Website & Community |
| 11 | Camp Audax / The Gathering |
| 12 | Project TigerClaw (ste-ai-buildout) |
| 13 | RMA — New Meeting Flow |
| 14 | RMA Podcast |

**Always ask which project before creating a WP.**

---

## Reference

| Type ID | Label |
|---|---|
| 1 | Task |
| 2 | Milestone |
| 3 | Summary task (phases) |

| Status ID | Label |
|---|---|
| 1 | New |
| 7 | In progress |
| 12 | Closed |
| 13 | On hold |
| 14 | Rejected |

---

## Procedures

### Create WP

1. Ask which project (no default)
2. Draft title + description (see template below), confirm with Ed
3. POST:

```bash
curl -s -X POST \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/projects/{PROJECT_ID}/work_packages" \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json" \
  -d '{"subject":"TITLE","description":{"raw":"DESCRIPTION"},"_links":{"type":{"href":"/api/v3/types/1"}}}'
```

4. Return `OP#<id>` and link: `.../work_packages/<id>`

### Update Status

```bash
# Get lockVersion
curl -s "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/<id>" \
  -H "Authorization: Basic $AUTH" | python3 -c "import sys,json; print(json.load(sys.stdin)['lockVersion'])"

# Patch
curl -s -X PATCH \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/<id>" \
  -H "Authorization: Basic $AUTH" -H "Content-Type: application/json" \
  -d '{"lockVersion":<N>,"_links":{"status":{"href":"/api/v3/statuses/12"}}}'
```

### Post Comment

```bash
curl -s -X POST \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/<id>/activities" \
  -H "Authorization: Basic $AUTH" -H "Content-Type: application/json" \
  -d '{"comment":{"raw":"COMMENT"}}'
```

### Attach File to WP

Files must be stored in the OP database (M1 MacBook server) — NOT saved locally to the Discovery folder.

```bash
curl -s -X POST \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/<id>/attachments" \
  -H "Authorization: Basic $AUTH" \
  -F 'metadata={"fileName":"FILENAME.md","description":{"raw":"DESCRIPTION"}}; type=application/json' \
  -F "file=@/path/to/local/file; type=text/markdown"
```

**File location rule (2026-07-21):** Agent-generated documents must be attached to the relevant OP work package. Do not save as permanent files to `~/Discovery/` — local files are temporary staging only.

### List Open WPs

```bash
curl -s \
  "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/projects/{PROJECT_ID}/work_packages?filters=%5B%7B%22status%22%3A%7B%22operator%22%3A%22o%22%2C%22values%22%3A%5B%5D%7D%7D%5D" \
  -H "Authorization: Basic $AUTH" | python3 -c "
import sys, json
for wp in json.load(sys.stdin).get('_embedded',{}).get('elements',[]):
    print(f'OP#{wp[\"id\"]}  {wp[\"subject\"]}')
"
```

---

## WP Description Template

```
Assignee: [Ed | Agent: Copilot]
Device:   [Mac Mini | M4 Laptop | M1 MacBook | N/A]
Tier:     [Network | On Premise | On Device]
Deadline: [YYYY-MM-DD | next session | TBD]

[One sentence: what done looks like]

Output: [file path or WP link]
```

---

## Rules

- Always ask which project. No default.
- Draft and confirm with Ed before POSTing.
- Use `OPENPROJECTS_COPILOT_API_KEY` for all normal WP operations.
- Use `OPENPROJECTS_API_KEY` (admin) only for user management and admin-only operations.
- The VS Code extension token (Ed's personal) is separate from `OPENPROJECTS_COPILOT_API_KEY`. Never conflate them.
- Every action item gets an OP#ID before the session ends.
- Close WPs when done. No stale "In progress".
- **Files go in OP, not Discovery.** Attach generated documents to the relevant WP. Do not save permanently to `~/Discovery/` — that folder is local working memory only.
- **Where files live (data rules):**
  - Public (GitHub): governance docs, open-source specs, website — things meant to be forked/shared
  - Private (Notion): proprietary content, financial, internal team data
  - Shared (Google Drive): team files, raw media/IP
  - OP database: session outputs, generated docs, attachments referenced in WPs
  - Local (`~/Discovery/`): agent working memory only — not canonical, not shared

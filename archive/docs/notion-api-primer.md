# Notion API — What You Need to Know
> Research for Phase 3 (Notion Architecture Audit) — 2026-03-03

---

## What It Can Do

The Notion API gives programmatic access to your workspace. For our use case:

- **Read databases** — query any database (Projects, Tasks, Meetings, Contributors, etc.)
- **Write to databases** — create/update pages (records) in any database
- **Read page content** — pull the content of any page
- **Search** — search across your entire workspace
- **Users** — list workspace members

This means an agent (EA, knowledge-ops, or a dedicated Notion integration) can:
- Pull the full structure of all your databases to map relational gaps
- Create meeting notes automatically
- Update task status, log RP points, register IP artifacts
- Sync Notion ↔ other systems (GitHub issues, Cal.com events, etc.)

---

## How It Works (Auth)

1. You create a **Notion Integration** at https://www.notion.so/my-integrations
2. It generates an **Internal Integration Token** (secret key)
3. You **share individual pages/databases** with the integration — Notion doesn't give blanket access
4. Any page/database NOT shared with the integration is invisible to it

**Key implication:** You control exactly what the API can see. You share the databases you want agents to touch, nothing else.

---

## What an Audit Looks Like

Once connected, an agent can call `GET /v1/databases/{id}` and get back:
- All property names and types (text, relation, select, date, person, rollup, formula, etc.)
- The **relation** properties — these are the links between databases

This is how we'd identify the gaps you flagged:
- Projects ↔ Meetings (does this relation exist?)
- Meetings ↔ Tasks
- Tasks ↔ Contributors
- Contributors ↔ RevPoints
- IP ↔ Revenue

Without the API, you'd have to manually open each database and check. With it, an agent can map the entire relational structure in one pass.

---

## Rate Limits

- **3 requests/second** per integration
- No hard monthly cap for internal integrations
- Large databases paginate at 100 results per page

Fine for our use case.

---

## What You'd Need to Set Up

1. Go to https://www.notion.so/my-integrations → Create new integration
   - Name: `Smoking Tigers Ops` (or similar)
   - Type: Internal
   - Capabilities: Read content, Update content, Insert content (optionally: Read user info)
   - Copy the **Internal Integration Token**

2. Add the token to OpenClaw secrets (so EA can use it)

3. Share your key databases with the integration:
   - Open each database in Notion → `...` menu → Connections → add your integration
   - At minimum: Projects, Tasks, Meetings, Contributors, RevPoints, IP registry, Revenue

4. EA or knowledge-ops can then run the audit — pull all database schemas, map relations, report gaps

---

## EA Integration Recommendation

EA is the right agent for Notion:
- Scheduling → Cal.com + Notion calendar sync
- Meeting notes → auto-create Notion pages from Cal.com events
- Task tracking → create/update tasks from conversations
- RevPoints → log eligibility chain entries

EA would need the integration token in its auth profile.

---

## Alternatives to the Official API

- **Notion MCP** (Model Context Protocol) — Notion released an official MCP server. If OpenClaw supports MCP tool connections, this is the cleanest path: no custom code, EA gets Notion as a native tool. Worth checking if OpenClaw has MCP support.
- **Zapier/Make** — no-code sync, but less agent-friendly
- **notion-sdk-py / @notionhq/client** — if we ever need a custom script

---

## Bottom Line for Phase 3

To do the Notion Architecture Audit properly:
1. Create the integration (5 min, you do it)
2. Share your key databases with it (10 min)
3. Add the token to EA's config
4. EA runs the audit — maps all properties, relations, gaps — posts report

**Without the API**, Phase 3 has to be done manually (you describe each database to me verbally). That works but is slower and more error-prone.

**Recommendation:** Set up the integration now. It's a one-time 15-minute task that unlocks EA as a real Notion operator going forward.

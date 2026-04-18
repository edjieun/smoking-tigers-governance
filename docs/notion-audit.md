# Notion Architecture Audit — Phase 3
> Completed: 2026-03-03 | 9 databases scanned via API

---

## Databases Found

| Database | ID | Purpose |
|----------|-----|---------|
| Smoking Tigers Strategy DB | 2c56f6ac | Projects / initiatives tracker |
| Meetings | 2af6f6ac | Meeting records |
| Smoking Tigers Documents | 2fc6f6ac | Document registry |
| LLM Models | 30e6f6ac | AI model catalog |
| ST:AI Ops | 30e6f6ac | Agent registry |
| Smoking Tigers Team | 2ef6f6ac | People / contributors |
| TLN Tasks | 2e26f6ac | Trade Like Nick task list |
| Directory | 2af6f6ac | Contact directory |
| Tracking Process - FOW | 40184444 | YouTube/podcast workflow |

---

## Relational Map (What's Connected)

```
Smoking Tigers Strategy DB (Projects)
    ├── → Meetings (bidirectional)
    └── → Smoking Tigers Documents
    
Meetings
    └── → Smoking Tigers Strategy DB (bidirectional)
```

That's it. Two relations total.

---

## Gap Analysis

### What's missing vs. the target architecture

Your goal was:
- Projects ↔ Meetings ✅ exists
- Meetings ↔ Tasks ❌ MISSING — Meetings has no relation to any task DB
- Tasks ↔ Contributors ❌ MISSING — TLN Tasks has no people/relation fields at all
- Contributors ↔ RevPoints ❌ MISSING — no RevPoints database exists
- IP ↔ Revenue ❌ MISSING — no IP registry, no Revenue database

### Detailed findings per database

**Smoking Tigers Strategy DB (Projects)**
- ✅ Has relation to Meetings
- ✅ Has relation to Documents
- ❌ No relation to Tasks
- ❌ No relation to Contributors / Team
- ❌ No Revenue field or relation
- ⚠️ `Owner` is a people field but not linked to Smoking Tigers Team DB (should be a relation, not freeform people picker)

**Meetings**
- ✅ Linked to Projects (bidirectional)
- ❌ No relation to Tasks — can't track what a meeting produces
- ❌ No relation to Contributors / Team DB
- ❌ No Notes field (only a URL to external minutes — fragile)
- ⚠️ `Attendees` is a people picker, not a relation to Team DB

**Smoking Tigers Documents**
- ✅ Linked from Projects
- ❌ No relation back to Projects (one-directional only)
- ❌ No IP classification field
- ❌ No contributor/author relation

**Smoking Tigers Team (Contributors)**
- ❌ No relation to any other database
- ❌ No RevPoints field or relation
- ❌ No role formalization (Role is just rich_text — should be select)
- ❌ No active/inactive status

**TLN Tasks**
- ❌ Only has Name and URL — essentially empty
- ❌ No assignee, no status, no due date, no project relation
- ❌ No relation to Contributors
- This database needs to be built out

**LLM Models / ST:AI Ops**
- Operational reference databases — no relational needs flagged
- ST:AI Ops could benefit from a relation to Team DB (agent owner)

**Directory**
- Separate from Team DB — unclear if these are the same people or external contacts
- ❌ No relation to Projects or Meetings

**Tracking Process - FOW**
- Standalone workflow tracker — well structured for its purpose
- Not connected to Projects or Team DB
- `Host` and `Guest` are people pickers, not relations to Team DB

---

## What Needs to Be Built

### Priority 1 — Core relational gaps

| Gap | Fix |
|-----|-----|
| Tasks DB needs to exist properly | Build out TLN Tasks (or create a unified Tasks DB) with: Assignee (relation to Team), Status, Due Date, Project (relation to Strategy DB) |
| Meetings → Tasks relation | Add relation field to Meetings pointing to Tasks DB |
| Team DB → RevPoints | Create RevPoints DB or add RP tracking to Team DB |
| Tasks → Contributors | Add Assignee as relation to Team DB (not people picker) |

### Priority 2 — Strengthen existing structures

| Issue | Fix |
|-------|-----|
| Owner/Attendees/Assignee are people pickers | Convert to relations pointing to Team DB — enables rollups and cross-DB queries |
| Documents has no IP classification | Add `IP Type` select field (Trademark, Copyright, Trade Secret, Other) |
| Documents → Projects is one-directional | Add reverse relation on Documents side |
| Team DB has no status | Add Active/Inactive status field |
| Team DB Role is rich_text | Convert to select with defined roles |

### Priority 3 — Missing databases

| Database | Purpose |
|----------|---------|
| RevPoints | Track RP issuance, eligibility chain, balance per contributor |
| Revenue | Track income by project/contributor |
| IP Registry | Formal IP artifact log (links to Documents, Projects, Contributors) |
| Tasks (unified) | Replace TLN Tasks with a proper cross-project task tracker |

---

## Recommended Build Order

1. **Fix Team DB** — add status, convert Role to select, establish it as the contributor source of truth
2. **Build Tasks DB** — proper fields, link to Projects + Team
3. **Connect Meetings → Tasks** — one relation field
4. **Convert people pickers to relations** — Owner in Projects, Attendees in Meetings
5. **Build RevPoints DB** — link to Team
6. **Build IP Registry** — link to Documents + Projects
7. **Build Revenue DB** — link to Projects + Contributors

---

## Notes

- EA can now query and update Notion via the API (token configured)
- EA should build out the missing databases and fields — this is Phase 3 execution work
- Governance decisions (what counts as IP, RP eligibility rules) need Steward approval before EA writes policy into Notion structure

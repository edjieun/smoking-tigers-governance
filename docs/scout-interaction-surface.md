# Scout Interaction Surface

Status: Active
Last Updated: 2026-02-23
Owner: Ed (Steward)

## Current Primary Surface

**Mattermost #executive channel** is the primary interaction surface for Scout (AI Chief of Staff).

## Historical Context

The original design used a Notion database called "Scout Inbox" where team members could submit requests. This was described in the founding Scout status report to the team.

As of the governance install session (2026-02-23), the operating model has shifted:
- Scout runs via OpenClaw on the home server
- Primary interaction is through Mattermost (accessible from mobile for all exec council members)
- Notion remains the system of record for project state and operations
- GitHub governance repo is the canonical source for policies and decisions

## Scout Inbox Status

The Notion Scout Inbox is considered **superseded** by the Mattermost integration. It may be archived or repurposed as a log/history surface at Ed's discretion.

## Implications

- Exec council members interact with Scout via Mattermost, not Notion
- Scout reads Notion exports as governed intake batches, not as a live inbox
- The Mattermost-first model aligns with the mobile-friendly access policy (policies/security/mattermost-access.md)

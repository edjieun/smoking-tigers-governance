# Members Registry

This directory contains enrollment records for all machines participating in the
Smoking Tigers governance model.

## What Is a Member

A **member machine** is a local OpenClaw instance that has adopted this
governance repo as its shared operating layer. Each member:

- clones and syncs this governance repo locally
- runs its agents within the authority boundaries defined here
- contributes improvements through the governed PR process

## Enrollment Process

To enroll a new machine:

1. Add your device to `devices.yaml` with the next available DID (e.g. `ste-did-003`)
2. Copy `template.yaml` to `<your-hostname>.yaml` and fill out all fields (include your DID)
3. Create `members/<your-github-username>.md` as your personal user file (see User Files section below)
4. Submit a Pull Request — `<your-hostname>.yaml` and `devices.yaml` changes get committed; `<username>.md` stays local (gitignored)
5. After approval and merge, follow `ONBOARDING-LOCAL-MACHINE.md` to complete setup

## Trust Levels

| Level | Who | Access |
|-------|-----|--------|
| `owner` | Founding steward (Ed) | Full governance authority, approves all PRs |
| `contributor` | Executive council members | May propose policy changes, run full agent suite |
| `observer` | Authorized community operators | Read governance, run local agents within constraints |

## User Files

Each operator maintains a personal user file at `members/<github-username>.md`.
This file contains their identity, preferences, hardware details, and list of registered DIDs.

**These files are gitignored** (`members/*.md`) — they stay on your local machine only.
Never commit them to GitHub or sync them to the shared Drive.

Template: copy `USER.template.md` and save to `members/<your-github-username>.md`.

---

## Device Registry

Full device specs live in `devices.yaml`. Summary:

| DID | Hostname | Operator | Tier | Enrolled |
|-----|----------|----------|------|----------|
| ste-did-001 | eds-mac-mini | edjieun | on-premise | 2026-06-22 |
| ste-did-002 | eds-m4-laptop | edjieun | on-device | 2026-07-28 |

## Active Members

| Hostname | Operator | Trust Level | DID | Joined |
|----------|----------|-------------|-----|--------|
| eds-mac-mini | edjieun | owner | ste-did-001 | 2026-06-22 |
| eds-m4-laptop | edjieun | owner | ste-did-002 | 2026-07-28 |

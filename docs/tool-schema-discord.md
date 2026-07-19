# Tool Schema: Discord
**Type:** Schema Document — Descriptive Only
**Created:** 2026-03-25
**Owner:** Ed (Steward)
**Status:** Draft

---

## Overview

Discord is the community and contributor-facing communication platform for Smoking Tigers. It hosts the primary community server where contributors, supporters, and exec members interact. Agent access is limited and role-specific.

---

## Server (Guild)

- **Name:** Smoking Tigers (assumed)
- **Guild ID:** `954777270428504145`
- **Type:** Private community server

---

## Channel Structure

### Category: GENERAL
| Channel | Type | ID | Purpose |
|---------|------|----|---------|
| #general | Text | `954777270428504148` | Main community channel |
| #contributors | Text | `1483550947404808402` | Contributor announcements / discussion |
| #supporters | Text | `1483550965310161267` | Supporter-tier content |
| #jimmy-ren-reacts | Text | `1486073868396527688` | Jimmy Ren Reacts project channel |

### Category: TRADE LIKE NICK
| Channel | Type | ID | Purpose |
|---------|------|----|---------|
| #tln-contributors | Text | `1484995983334178987` | TLN project contributor coordination |
| #trade-like-nick-content-ideas | Forum | `1483543681406599374` | Content ideas forum (threaded) |

### Category: EXECS
| Channel | Type | ID | Purpose |
|---------|------|----|---------|
| #exec-group | Text | `1483550907361788036` | Shared exec channel |
| #exec-ed | Text | `1485720133031825529` | Ed's private exec channel (EA-connected) |
| #exec-basil | Text | `1485719617958838382` | Basil's private exec channel |
| #exec-christine | Text | `1485719561272561815` | Christine's private exec channel |
| #exec-van | Text | `1485719863996580071` | Van's private exec channel |

### Category: PERSONAL
| Channel | Type | ID | Purpose |
|---------|------|----|---------|
| #pbsm | Text | `975453477931212871` | Personal / private (scope unclear) |

### Category: Voice Channels
| Channel | Type | ID | Purpose |
|---------|------|----|---------|
| #Ed's Private Idaho | Voice | `975453729195188236` | Ed's private voice room |
| #The Office | Voice | `954777270428504149` | Main office voice |
| #Conference Room | Voice | `1016390597394833510` | Meeting voice room |
| #Hangout | Voice | `1026994286379667497` | Casual voice |
| #DGF\|PrivateChannel | Voice | `1071101653928910954` | Private voice |
| #Smoke Break | Voice | `1071106723940671559` | Casual voice |

---

## Roles

| Role | Position | ID | Assigned To |
|------|----------|----|-------------|
| Tigers | 5 | `1071107830007996466` | Core members |
| Rosie | 4 | `1485737297407250475` | Rosie (christine-ea bot) |
| Thyme | 3 | `1485737589565558915` | Agent role |
| Eva | 2 | `1485740407391387829` | EA bot |
| TLN | 1 | `1486151477687877662` | Trade Like Nick participants |
| @everyone | 0 | `954777270428504145` | All members |

---

## Bot / Agent Presence

| Bot Account | OpenClaw Agent | Active Guild | Channels Allowed | Status |
|------------|---------------|-------------|-----------------|--------|
| EA bot | `ea` | `954777270428504145` | `#exec-ed` only | ✅ Active, allowlisted |
| Rosie | `christine-ea` | `954777270428504145` | Not configured | ⚠️ Token exists, no allowlist configured |
| Basil EA | `basil-ea` | None configured | None | ⚠️ Token exists, no guild configured |
| Van EA | `van-ea` | None configured | None | ⚠️ Token exists, no guild configured |
| Default | `main` (Scout) | None | None | Scout does not operate in Discord |

**Global Discord policy:** `groupPolicy: allowlist` — bots only respond in explicitly allowed channels.

---

## How It Connects to Other Tools

| Tool | Connection | Direction |
|------|-----------|-----------|
| OpenClaw | EA bot wired via `ea` account; allowlist-controlled | Inbound (exec-ed) |
| Mattermost | No direct connection — separate platforms | — |
| Notion | No direct connection | — |
| GitHub | No direct connection | — |
| Google Drive | No direct connection | — |

---

## STM vs. Q1 Distinction

| Dimension | STM | Q1 |
|-----------|-----|----|
| Server | Smoking Tigers guild (`954777270428504145`) | Separate Q1 server (not in scope here) |
| Channels | All channels above are STM | Q1 operates its own Discord |
| Agents | EA bots assigned to exec members | No Q1 agent presence configured |

---

## Known Gaps / Open Items

- `christine-ea`, `basil-ea`, and `van-ea` bots have tokens configured but no guild/channel allowlists — they cannot respond to anything
- `#exec-ed` is the only active agent-accessible channel; other exec channels have no agent coverage yet
- No webhook integrations connecting Discord to Mattermost, Notion, or GitHub
- `#pbsm` purpose unclear — needs review
- No formal onboarding flow for new contributors to the Discord server documented
- Role structure is minimal; no formal permission tiers beyond @everyone and named roles

---

## Canonical Role

> Discord is the **community and contributor engagement layer**. It is where contributors, supporters, and exec members interact informally and project-specifically. It is not an operational backend — decisions, records, and artifacts live in GitHub, Notion, and Google Drive.

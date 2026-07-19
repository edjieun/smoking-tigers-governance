---
last-updated: 2026-07-16
status: pending-manual-steps
---

# Mattermost Setup Guide

**Server:** `https://ste-business-server.tailebe6d3.ts.net:8065`
**Admin account:** `edlicious` (ed@quorum.one)

---

## Current State (2026-07-16) — COMPLETE
- ✅ MM server running on M1 (ste-business-server), HTTP 200
- ✅ Team: `smoking-tigers-enterprises` | ID: `onzu1jgfy78wt85dmr9pdo6f9y`
- ✅ Channels created (see Channel Registry below for IDs)
- ✅ Scout added to team + all 4 channels
- ✅ Christine account created (`christine` | ID: `yr3bqxa89bgbtc53u6bbq9xtde`)
- ✅ Christine added to team + #transcripts, #tasks, #decisions
- ✅ Scout #transcripts binding wired in openclaw.json
- ✅ MATTERMOST_TEAM=smoking-tigers-enterprises in vault
- ⚠️ mavin + pmp-team bots still active — deactivate via System Console

---

## Step 1 — Create the Team (MM Web UI)

1. Open `https://ste-business-server.tailebe6d3.ts.net:8065` in browser
2. Log in as `edlicious`
3. Click **Create a Team**
4. Name: `Smoking Tigers` | URL: `smoking-tigers`
5. Set to **Invite Only** (private)

Then get the team ID via API (run in terminal after logging in):
```bash
source ~/.ste-secrets/.env
MM_BASE="https://ste-business-server.tailebe6d3.ts.net:8065"
# Replace <ED_TOKEN> with a personal access token from MM Profile → Security → Personal Access Tokens
curl -sk -H "Authorization: Bearer <ED_TOKEN>" "$MM_BASE/api/v4/teams" | python3 -c "import sys,json; [print(t['name'], t['id']) for t in json.load(sys.stdin)]"
```

Update `MATTERMOST_TEAM` in vault once you have the team slug.

---

## Step 2 — Create 4 Channels (API)

Replace `<TEAM_ID>` and `<ED_TOKEN>` with real values:

```bash
MM_BASE="https://ste-business-server.tailebe6d3.ts.net:8065"
TEAM_ID="<TEAM_ID>"
TOKEN="<ED_TOKEN>"

for ch in "transcripts:Transcripts:Meeting transcripts and pipeline input" \
          "tasks:Tasks:Agent-extracted tasks from meetings" \
          "decisions:Decisions:Agent-extracted decisions from meetings" \
          "agent-logs:Agent Logs:Scout pipeline status errors and job completion"; do
  NAME="${ch%%:*}"; DISPLAY="${ch#*:}"; DISPLAY="${DISPLAY%%:*}"; PURPOSE="${ch##*:}"
  curl -sk -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    "$MM_BASE/api/v4/channels" \
    -d "{\"team_id\":\"$TEAM_ID\",\"name\":\"$NAME\",\"display_name\":\"$DISPLAY\",\"purpose\":\"$PURPOSE\",\"type\":\"O\"}" \
    | python3 -c "import sys,json; c=json.load(sys.stdin); print(c.get('name','ERROR'), c.get('id', c.get('message','')))"
done
```

Save the `#transcripts` channel ID — needed for the Scout binding in `openclaw.json`.

---

## Step 3 — Add Scout to Team + Channels

```bash
# Get Scout's user ID
SCOUT_ID=$(curl -sk -H "Authorization: Bearer $TOKEN" "$MM_BASE/api/v4/users/username/scout" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# Add Scout to team
curl -sk -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$MM_BASE/api/v4/teams/$TEAM_ID/members" \
  -d "{\"team_id\":\"$TEAM_ID\",\"user_id\":\"$SCOUT_ID\"}"

# Add Scout to all 4 channels (get channel IDs first, then):
# curl -sk -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
#   "$MM_BASE/api/v4/channels/<CHANNEL_ID>/members" -d "{\"user_id\":\"$SCOUT_ID\"}"
```

---

## Step 4 — Wire #transcripts Channel to Scout in openclaw.json

After getting the `#transcripts` channel ID, SSH to Mac Mini and add the binding:

```bash
ssh -i ~/.ssh/id_ed25519_mac_mini edhwang@eds-mac-mini "
python3 -c \"
import json
d = json.load(open('/Users/edhwang/.openclaw/openclaw.json'))
d['bindings'].append({
    'agentId': 'main',
    'match': {
        'channel': 'mattermost',
        'peer': {'kind': 'channel', 'id': '<TRANSCRIPTS_CHANNEL_ID>'}
    }
})
json.dump(d, open('/Users/edhwang/.openclaw/openclaw.json','w'), indent=2)
print('BINDING_ADDED')
\""
```

---

## Step 5 — Deactivate Old Bot Accounts

In MM System Console → User Management → Bots:
- Deactivate **mavin** bot
- Deactivate **pmp-team** bot
- Keep **scout** and **scout-cos** active

---

## Step 6 — Create Christine's Account

```bash
curl -sk -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$MM_BASE/api/v4/users" \
  -d '{
    "email": "christine.francis@quorum.one",
    "username": "christine",
    "first_name": "Christine",
    "last_name": "Francis",
    "password": "<TEMP_PASSWORD>"
  }' | python3 -c "import sys,json; u=json.load(sys.stdin); print(u.get('username','ERROR'), u.get('id', u.get('message','')))"
```

Then add Christine to the team and to `#transcripts`, `#tasks`, `#decisions` channels.
Send her the MM URL + temp password via Discord DM.

---

## Step 7 — Update MATTERMOST_TEAM in Vault

Once team is created:
```bash
# On Mac Mini:
ssh -i ~/.ssh/id_ed25519_mac_mini edhwang@eds-mac-mini "
sed -i '' 's|^MATTERMOST_TEAM=.*|MATTERMOST_TEAM=smoking-tigers|' ~/.ste-secrets/.env
cd ~/.ste-secrets && tar czf - .env google/ | openssl enc -aes-256-cbc -pbkdf2 -pass file:/Users/edhwang/.ste-secrets/.passphrase -out ~/ste-secrets-repo/vault.tar.gz.enc
cd ~/ste-secrets-repo && git commit -am 'fix: add MATTERMOST_TEAM' && git push
"
```

---

## Channel Registry

| Channel | ID | Purpose | Who posts | Scout monitors |
|---|---|---|---|---|
| `#transcripts` | `uhyi1xfac7yd9esfytouokko4h` | Raw transcript text or Fathom links — triggers the pipeline | Ed, Christine (all members eventually) | ✅ Yes — bound in openclaw.json |
| `#tasks` | `huq58yfrejffid58ta1wqzinko` | Extracted tasks from meetings, grouped by owner | Scout | No |
| `#decisions` | `93pbu6muep8r5fixz51ppm7cac` | Extracted decisions from meetings | Scout | No |
| `#agent-logs` | `hphi4p6noffbtntq7g6pyrzm7e` | Scout pipeline status, errors, job completion | Scout | No |

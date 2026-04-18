#!/bin/bash
# get-all-agent-sessions.sh
# Outputs session file paths for all active agents for today's memory digest.
# Used by knowledge-ops multi-agent memory digest.

TODAY=$(date +%Y-%m-%d)
AGENTS_DIR="/Users/edlicious/.openclaw/agents"
WORKSPACE="/Users/edlicious/.openclaw/workspace"

echo "DATE=$TODAY"
echo "MEMORY_OUT=${WORKSPACE}/memory/${TODAY}.md"
echo "MEMORY_LONG=${WORKSPACE}/MEMORY.md"
echo "SHARED_MEMORY=${WORKSPACE}/memory/shared.md"
echo "---SESSIONS---"

# List of agents to include in digest
AGENTS=("main" "ea" "sysops" "governance-ops" "sergeant-at-arms" "knowledge-ops" "christine-ea")

for agent in "${AGENTS[@]}"; do
    SESSIONS_JSON="${AGENTS_DIR}/${agent}/sessions/sessions.json"
    if [ ! -f "$SESSIONS_JSON" ]; then
        continue
    fi

    # Get the most recently updated session file for this agent
    python3 -c "
import json, sys, os
from datetime import datetime

with open('$SESSIONS_JSON') as f:
    d = json.load(f)

today = '$TODAY'
best_file = None
best_ts = 0

for key, val in d.items():
    session_file = val.get('sessionFile', '')
    updated_at = val.get('updatedAt', 0)
    if not session_file or not os.path.exists(session_file):
        continue
    # Only include sessions updated today
    session_date = datetime.fromtimestamp(updated_at / 1000).strftime('%Y-%m-%d') if updated_at else ''
    if session_date == today and updated_at > best_ts:
        best_ts = updated_at
        best_file = session_file

if best_file:
    print(f'AGENT=${agent}|FILE={best_file}')
" 2>/dev/null
done

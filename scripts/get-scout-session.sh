#!/bin/bash
# get-scout-session.sh
# Outputs the current Scout primary DM session file path and today's date.
# Used by knowledge-ops memory digest cron.

SESSION_KEY="agent:main:mattermost:direct:w3z1hqmzw78ct8dscrm5itxk6r"
SESSIONS_JSON="/Users/edlicious/.openclaw/agents/main/sessions/sessions.json"

TODAY=$(date +%Y-%m-%d)
SESSION_FILE=$(python3 -c "
import json, sys
with open('$SESSIONS_JSON') as f:
    d = json.load(f)
v = d.get('$SESSION_KEY', {})
print(v.get('sessionFile', ''))
" 2>/dev/null)

echo "DATE=$TODAY"
echo "SESSION_FILE=$SESSION_FILE"
echo "MEMORY_OUT=/Users/edlicious/.openclaw/workspace/memory/${TODAY}.md"
echo "MEMORY_LONG=/Users/edlicious/.openclaw/workspace/MEMORY.md"

#!/bin/zsh
# qmd-embed.sh — Re-embed all qmd collections (generate/update vectors)
# Run after qmd-index.sh to ensure new content is searchable.
# Requires Ollama to be running with nomic-embed-text model available.

set -euo pipefail

LOG_DIR="$HOME/.openclaw/workspace/logs"
LOG_FILE="$LOG_DIR/qmd-embed.log"
mkdir -p "$LOG_DIR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting qmd embed..." >> "$LOG_FILE"

# Check Ollama is up
if ! curl -sf http://127.0.0.1:11434/api/tags > /dev/null 2>&1; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: Ollama not reachable at 127.0.0.1:11434. Aborting." >> "$LOG_FILE"
  exit 1
fi

# Embed all collections
/opt/homebrew/bin/qmd embed >> "$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Embed complete." >> "$LOG_FILE"

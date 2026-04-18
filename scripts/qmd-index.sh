#!/bin/zsh
# qmd-index.sh — Re-index all qmd collections (sync file changes)
# Collections: srv (/Users/edlicious/srv), obsidian-stm (Smoking Tigers vault)
# Run daily or on demand to pick up new/modified markdown files.

set -euo pipefail

LOG_DIR="$HOME/.openclaw/workspace/logs"
LOG_FILE="$LOG_DIR/qmd-index.log"
mkdir -p "$LOG_DIR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting qmd update..." >> "$LOG_FILE"

# Re-index all collections (picks up new, modified, deleted files)
/opt/homebrew/bin/qmd update >> "$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Index complete." >> "$LOG_FILE"

A comprehensive execution script has been engineered to clean up the structural duplicates and establish systematic organization rules for files abandoned in the top-level project root directory.

```
#!/usr/bin/env bash
# ==============================================================================
# WORKSPACE CONSOLIDATION & ROOT CLEANUP ARCHITECTURAL BLUEPRINT
# Targets: Redundancy mitigation, unified agent boundaries, and root organization.
# Revised: 2026-07-27 — safe structure-preserving logic replacing destructive merges
# ==============================================================================

set -euo pipefail

PROJECT_ROOT="$(pwd)"
ADR_DIR="$PROJECT_ROOT/adr"
DECISIONS_DIR="$PROJECT_ROOT/decisions"
GOVERNANCE_DIR="$PROJECT_ROOT/governance"
POLICIES_DIR="$PROJECT_ROOT/policies"
GITHUB_DIR="$PROJECT_ROOT/.github"
COPILOT_DIR="$PROJECT_ROOT/.copilot"

echo "Initializing Project TigerClaw directory optimization..."

# ------------------------------------------------------------------------------
# PHASE 1: REDUNDANCY CONSOLIDATION
# ------------------------------------------------------------------------------

# 1. decisions/ vs adr/ — PRESERVE BOTH. Different document types:
#    - adr/  → ADR-NNN-*.md  (architectural decision records, formal)
#    - decisions/YYYY/ → DEC-YYYYMMDD-*.md  (operational decisions, dated)
#    These must NOT be merged or flattened. Instead, ensure adr/ exists and
#    write a cross-reference README if one doesn't exist yet.
echo "[Consolidation] Verifying decisions/ and adr/ separation..."
mkdir -p "$ADR_DIR"
if [ ! -f "$ADR_DIR/README.md" ]; then
    cat > "$ADR_DIR/README.md" << 'EOF'
# Architecture Decision Records (ADRs)

Formal architectural decisions using ADR-NNN naming.
Operational dated decisions live in `../decisions/YYYY/` using DEC-YYYYMMDD naming.
These are separate document types — do not merge.
EOF
    echo "  -> Created adr/README.md cross-reference stub"
fi

# 2. policies/ → governance/policies/ — PRESERVE SUBCATEGORY STRUCTURE
#    Move policies/ai/, policies/governance/, policies/operations/, policies/security/
#    into governance/policies/ keeping each subfolder intact.
if [ -d "$POLICIES_DIR" ]; then
    echo "[Consolidation] Moving policies/ into governance/policies/ (preserving subcategories)..."
    mkdir -p "$GOVERNANCE_DIR/policies"
    for subdir in "$POLICIES_DIR"/*/; do
        [ -d "$subdir" ] || continue
        subname="$(basename "$subdir")"
        mkdir -p "$GOVERNANCE_DIR/policies/$subname"
        find "$subdir" -type f -exec mv -n {} "$GOVERNANCE_DIR/policies/$subname/" \;
        echo "  -> Moved policies/$subname/ → governance/policies/$subname/"
    done
    # Move any loose files at policies/ root (not in a subdir)
    find "$POLICIES_DIR" -maxdepth 1 -type f -exec mv -n {} "$GOVERNANCE_DIR/policies/" \;
    # Clean up empty source dirs
    find "$POLICIES_DIR" -type d -empty -delete 2>/dev/null || true
    rmdir "$POLICIES_DIR" 2>/dev/null && echo "  -> Removed empty policies/" || echo "  Note: policies/ not empty after move — manual check required"
fi

# 3. .copilot/ — remove only if empty; never touch .github/copilot-instructions.md
if [ -d "$COPILOT_DIR" ]; then
    if [ -z "$(ls -A "$COPILOT_DIR")" ]; then
        rmdir "$COPILOT_DIR"
        echo "[Consolidation] Removed empty .copilot/ directory"
    else
        echo "[Consolidation] .copilot/ is not empty — skipping (manual review required)"
    fi
fi

# ------------------------------------------------------------------------------
# PHASE 2: TOP-LEVEL ROOT SORTING
# ------------------------------------------------------------------------------
echo "[Sorting] Processing detached documents in project root..."

# Canonical agent files — never move these
PROTECTED=("AGENTS.md" "SOUL.md" "USER.md" "IDENTITY.md" "MEMORY.md" "TASKS.md" "TOOLS.md" "HEARTBEAT.md" "README.md" "LICENSE")

is_protected() {
    local fname="$1"
    for p in "${PROTECTED[@]}"; do
        [[ "$(echo "$fname" | tr '[:lower:]' '[:upper:]')" == "$(echo "$p" | tr '[:lower:]' '[:upper:]')" ]] && return 0
    done
    return 1
}

declare -A ROOT_FILE_MAP=(
    ["*charter*.md"]="$PROJECT_ROOT/charters"
    ["*agreement*.md"]="$PROJECT_ROOT/agreements"
    ["*budget*.md"]="$PROJECT_ROOT/finance"
    ["*ledger*.md"]="$PROJECT_ROOT/finance"
    ["*cost*.md"]="$PROJECT_ROOT/finance"
    ["*analysis*.md"]="$PROJECT_ROOT/analysis"
    ["*report*.md"]="$PROJECT_ROOT/analysis"
    ["*transcript*.md"]="$PROJECT_ROOT/Transcripts"
    ["*meeting*.md"]="$PROJECT_ROOT/Transcripts"
    ["*workflow*.md"]="$PROJECT_ROOT/workflows"
    ["*blueprint*.md"]="$PROJECT_ROOT/workflows"
)

for pattern in "${!ROOT_FILE_MAP[@]}"; do
    DEST="${ROOT_FILE_MAP[$pattern]}"
    while IFS= read -r -d '' fpath; do
        fname="$(basename "$fpath")"
        if is_protected "$fname"; then
            echo "  [Protected] Skipping: $fname"
            continue
        fi
        mkdir -p "$DEST"
        mv -n "$fpath" "$DEST/"
        echo "  [Sorted] $fname → ${DEST##*/}/"
    done < <(find "$PROJECT_ROOT" -maxdepth 1 -type f -iname "$pattern" -print0)
done

# ------------------------------------------------------------------------------
# PHASE 3: AGENT LAYER VERIFICATION (read-only)
# ------------------------------------------------------------------------------
echo "[Agent Sync] Verifying baseline system instruction states..."
CORE_AGENT_FILES=("AGENTS.md" "USER.md" "IDENTITY.md" "SOUL.md" "TOOLS.md" "MEMORY.md" "TASKS.md" "HEARTBEAT.md")

ALL_PRESENT=true
for agent_file in "${CORE_AGENT_FILES[@]}"; do
    if [ -f "$PROJECT_ROOT/$agent_file" ]; then
        echo "  ✓ $agent_file"
    else
        echo "  ✗ MISSING: $agent_file"
        ALL_PRESENT=false
    fi
done

if $ALL_PRESENT; then
    echo "[Agent Sync] All core agent files present."
else
    echo "[Agent Sync] WARNING: One or more core agent files missing — review before proceeding."
fi

echo ""
echo "Workspace alignment complete."
```

### Dynamic Root Routing Constraints Added

The organizational logic has been augmented to safely grab isolated files matching core functional footprints out of the top level and place them in their respective homes:

- **Financial Elements:** Files tracking budgets, ledgers, or costs are captured and moved to `finance/`.
- **Operational Transcripts:** Loose meeting details or audio-to-text transcripts are isolated and nested into `transcripts/`.
- **Analysis Logs & Charters:** System engineering reports or initial team charters are redirected into `analysis/` and `charters/` respectively.

Would you like me to construct a template structure for the persistent `user.md` human briefing configuration file to help keep your agent context perfectly personalized across these directories?
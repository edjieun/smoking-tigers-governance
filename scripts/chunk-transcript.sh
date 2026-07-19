#!/usr/bin/env bash
# chunk-transcript.sh
# Strips Fathom metadata from a meeting transcript and splits it into
# token-safe chunks for local model processing (default: 12,000 words per chunk).
#
# Usage:
#   bash scripts/chunk-transcript.sh "Transcripts/STE/STE - 2026-07-07.md"
#
# Output:
#   chunks/STE - 2026-07-07 - chunk-1.md
#   chunks/STE - 2026-07-07 - chunk-2.md
#   ...
#
# Each chunk file includes a header with project, date, and chunk info
# so the prompt has context without needing the original file.

set -euo pipefail

INPUT="${1:-}"
if [[ -z "$INPUT" ]]; then
  echo "Usage: bash scripts/chunk-transcript.sh <path-to-transcript>"
  exit 1
fi

# Resolve to absolute path from repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
INPUT_ABS="$REPO_ROOT/$INPUT"

if [[ ! -f "$INPUT_ABS" ]]; then
  # Try treating INPUT as absolute path
  INPUT_ABS="$INPUT"
fi

if [[ ! -f "$INPUT_ABS" ]]; then
  echo "Error: File not found: $INPUT"
  exit 1
fi

# Extract filename without extension
BASENAME="$(basename "$INPUT_ABS" .md)"

# Words per chunk — 12,000 words ≈ ~10,000 tokens (conservative for 16,384 ctx)
# Leaves ~6,000 tokens for system prompt + output
WORDS_PER_CHUNK=12000

# Output dir
CHUNKS_DIR="$REPO_ROOT/chunks"
mkdir -p "$CHUNKS_DIR"

# Remove existing chunks for this file
rm -f "$CHUNKS_DIR/$BASENAME - chunk-"*.md

echo "Processing: $BASENAME"
echo "Source: $INPUT_ABS"
echo "Output: $CHUNKS_DIR/"
echo ""

# ── Strip Fathom metadata ──────────────────────────────────────────────────
# Remove:
#   - The [VIEW RECORDING - ...] link line
#   - Fathom share URLs embedded in timestamps (keep the @MM:SS part, strip the URL)
#   - Blank lines of 2+ in a row → single blank line
#   - Lines that are only whitespace

# ── Strip Fathom metadata to a temp file ─────────────────────────────────
TMPFILE="$(mktemp /tmp/transcript-stripped.XXXXXX)"
trap 'rm -f "$TMPFILE"' EXIT

grep -v '\[.*VIEW RECORDING.*\]' "$INPUT_ABS" \
  | sed 's|\[@\([0-9:]*\)\]([^)]*) - \*\*\([^*]*\)\*\*|@\1 - **\2**|g' \
  | cat -s \
  | grep -v '^[[:space:]]*$' \
  > "$TMPFILE"

# ── Extract title ─────────────────────────────────────────────────────────
TITLE="$(head -1 "$TMPFILE")"

# ── Split into chunks by word count ──────────────────────────────────────
CHUNK_NUM=1
WORD_COUNT=0
CHUNK_TMP="$(mktemp /tmp/transcript-chunk.XXXXXX)"
trap 'rm -f "$TMPFILE" "$CHUNK_TMP"' EXIT

write_chunk() {
  local num="$1"
  local outfile="$CHUNKS_DIR/$BASENAME - chunk-$num.md"
  {
    echo "<!-- CHUNK $num SOURCE=$INPUT -->"
    echo "<!-- Run /Process Transcript Chunk on this file in Obsidian -->"
    echo ""
    echo "$TITLE"
    echo ""
    cat "$CHUNK_TMP"
  } > "$outfile"
  local words
  words=$(wc -w < "$CHUNK_TMP" | tr -d ' ')
  echo "  Chunk $num: $(basename "$outfile") (~$words words)"
  > "$CHUNK_TMP"  # clear for next chunk
}

while IFS= read -r line; do
  echo "$line" >> "$CHUNK_TMP"
  LINE_WORDS=$(echo "$line" | wc -w | tr -d ' ')
  WORD_COUNT=$((WORD_COUNT + LINE_WORDS))

  if (( WORD_COUNT >= WORDS_PER_CHUNK )); then
    write_chunk "$CHUNK_NUM"
    CHUNK_NUM=$((CHUNK_NUM + 1))
    WORD_COUNT=0
  fi
done < "$TMPFILE"

# Write any remaining content
if [[ -s "$CHUNK_TMP" ]]; then
  write_chunk "$CHUNK_NUM"
fi

TOTAL_CHUNKS=$CHUNK_NUM
echo ""
echo "Done. $TOTAL_CHUNKS chunk(s) written to $CHUNKS_DIR/"
echo ""
echo "Next steps:"
echo "  1. Open each chunk file in Obsidian"
echo "  2. Run /Process Transcript Chunk on each one"
echo "  3. Cards are saved to Memory/ automatically"

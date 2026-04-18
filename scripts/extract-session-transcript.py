#!/usr/bin/env python3
"""
extract-session-transcript.py
Converts a Scout session JSONL file into clean markdown for knowledge-ops to process.

Usage: python3 extract-session-transcript.py <session_file> [output_file]
If output_file is omitted, writes to stdout.
"""

import json
import sys
import re
from datetime import datetime

def extract_transcript(session_file, output_file=None):
    messages = []
    session_date = None

    with open(session_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue

            if d.get('type') == 'message':
                msg = d.get('message', {})
                role = msg.get('role', '')
                content = msg.get('content', '')
                ts = d.get('timestamp', 0)

                if ts and not session_date:
                    try:
                        session_date = datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d')
                    except Exception:
                        pass

                # Extract readable text
                text_parts = []
                if isinstance(content, str):
                    text_parts.append(content)
                elif isinstance(content, list):
                    for block in content:
                        if not isinstance(block, dict):
                            continue
                        btype = block.get('type', '')
                        if btype == 'text':
                            text_parts.append(block.get('text', ''))
                        elif btype == 'tool_use':
                            # Summarize tool calls without full JSON
                            name = block.get('name', '')
                            inp = block.get('input', {})
                            summary = f'[tool_call: {name}'
                            if isinstance(inp, dict):
                                key_args = {k: str(v)[:80] for k, v in list(inp.items())[:3]}
                                if key_args:
                                    summary += f'({", ".join(f"{k}={v}" for k, v in key_args.items())})'
                            summary += ']'
                            text_parts.append(summary)
                        elif btype == 'tool_result':
                            # Skip verbose tool results — not useful for memory
                            pass

                full_text = '\n'.join(t for t in text_parts if t.strip())

                # Filter: only user and assistant turns with actual text
                if role in ('user', 'assistant') and full_text.strip():
                    # Clean up system envelope from user messages
                    clean_text = full_text.strip()
                    if role == 'user':
                        # Strip the System: [...] envelope, keep just Ed's message
                        match = re.search(r'@edlicious:\s*(.+?)(?:\n\nConversation info|$)', clean_text, re.DOTALL)
                        if match:
                            clean_text = match.group(1).strip()

                    messages.append((role, clean_text))

    if not session_date:
        session_date = datetime.now().strftime('%Y-%m-%d')

    # Build output markdown
    lines = [
        f'# Session Transcript — {session_date}',
        f'Extracted from session JSONL for knowledge-ops memory digest.',
        f'Total turns: {len(messages)}',
        '',
        '---',
        '',
    ]

    for role, text in messages:
        label = '**Ed:**' if role == 'user' else '**Scout:**'
        lines.append(f'{label}')
        lines.append(text)
        lines.append('')

    output = '\n'.join(lines)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(output)
        print(f'Transcript written to {output_file} ({len(messages)} turns)')
    else:
        print(output)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 extract-session-transcript.py <session_file> [output_file]')
        sys.exit(1)
    session_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_transcript(session_file, output_file)

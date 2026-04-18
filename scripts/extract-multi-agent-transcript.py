#!/usr/bin/env python3
"""
extract-multi-agent-transcript.py
Converts multiple agent session JSONL files into a single combined markdown transcript
for knowledge-ops multi-agent memory digest.

Usage: python3 extract-multi-agent-transcript.py <output_file> [AGENT1:FILE1] [AGENT2:FILE2] ...
Each agent:file pair is passed as "agentname:/path/to/session.jsonl"
"""

import json
import sys
import re
import os
from datetime import datetime


def extract_agent_transcript(agent_name, session_file):
    """Extract messages from a single agent session JSONL."""
    messages = []

    try:
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
                                name = block.get('name', '')
                                inp = block.get('input', {})
                                summary = f'[tool_call: {name}'
                                if isinstance(inp, dict):
                                    key_args = {k: str(v)[:80] for k, v in list(inp.items())[:3]}
                                    if key_args:
                                        summary += f'({", ".join(f"{k}={v}" for k, v in key_args.items())})'
                                summary += ']'
                                text_parts.append(summary)
                            # Skip tool_result — too verbose

                    full_text = '\n'.join(t for t in text_parts if t.strip())

                    if role in ('user', 'assistant') and full_text.strip():
                        clean_text = full_text.strip()
                        if role == 'user':
                            # Strip system envelope, keep Ed's message
                            match = re.search(r'@edlicious:\s*(.+?)(?:\n\nConversation info|$)', clean_text, re.DOTALL)
                            if match:
                                clean_text = match.group(1).strip()
                            # Also strip heartbeat system messages
                            if clean_text.startswith('System:') and 'heartbeat' in clean_text.lower():
                                continue

                        messages.append((role, clean_text, ts))
    except Exception as e:
        messages.append(('system', f'[Error reading {session_file}: {e}]', 0))

    return messages


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 extract-multi-agent-transcript.py <output_file> [AGENT:FILE ...]')
        sys.exit(1)

    output_file = sys.argv[1]
    agent_files = sys.argv[2:]

    today = datetime.now().strftime('%Y-%m-%d')
    sections = []

    for agent_arg in agent_files:
        if ':' not in agent_arg:
            continue
        agent_name, session_file = agent_arg.split(':', 1)
        if not os.path.exists(session_file):
            continue

        messages = extract_agent_transcript(agent_name, session_file)
        if not messages:
            continue

        lines = [f'## Agent: {agent_name}', f'Session: {os.path.basename(session_file)}', '']
        for role, text, ts in messages:
            if agent_name == 'main':
                label = '**Ed:**' if role == 'user' else '**Scout:**'
            else:
                label = '**Ed:**' if role == 'user' else f'**{agent_name}:**'
            lines.append(label)
            lines.append(text[:2000])  # cap per-message length
            lines.append('')
        sections.append('\n'.join(lines))

    output = f'# Multi-Agent Session Transcript — {today}\n\nFor knowledge-ops memory digest. Total agents: {len(sections)}\n\n---\n\n'
    output += '\n\n---\n\n'.join(sections)

    with open(output_file, 'w') as f:
        f.write(output)

    print(f'Multi-agent transcript written to {output_file} ({len(agent_files)} agents requested, {len(sections)} with activity)')


if __name__ == '__main__':
    main()

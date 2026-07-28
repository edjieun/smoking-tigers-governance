The tech stack for Project TigerClaw / Smoking Tigers AI Ecosystem (Discovery) is organized into a local-first, three-tier architecture (On-Premise, On-Device, and Network):
# AI & Agent Stack

- Agent Framework / Harness: 
	- OpenClaw (Scout): Core autonomous Chief of Staff agent harness running on Mac Mini (port 18789).
	- OpenCode / GitHub Copilot: On-device interactive coding and execution agents.
- Local Inference Servers:
	- LM Studio: OpenAI-compatible local model server on Mac Mini (port 1234).
	- Ollama: Local model runner on Mac Mini (port 11434), hosting qwen2.5 (14B, 7B, 3B instruct) and nomic-embed-text.
- Cloud Models & APIs:
	- -MCP & Agent Tools:OpenRouter / Gemini / Anthropic Claude Opus: Used for high-reasoning tasks or fallbacks when explicitly requested.
	- Hermes MCP (edjieun/hermes-agent): Skill server for autonomous skill learning (Python).
	- Custom MCP Servers: mcp-searxng and mcp-crawl4ai-ts for web search and scraping.
# Business & Application Stack
- Work Tracking: OpenProjects (Ruby/Rails & PostgreSQL running on M1 MacBook, port 8080).
- Team Comms & Agent Input/Output: Mattermost (Go & PostgreSQL running on M1 MacBook, port 8065; #tigerclaw channel as primary agent I/O).
- Financial Ledger: LedgerSMB (Perl & PostgreSQL on M1 MacBook, port 5762).
- Agent Dashboard / UI: Nerve UI (React/TypeScript kanban interface on Mac Mini, port 3080).
- Scheduling: Cal.com (Next.js/Node.js with Postgres & Redis on Mac Mini, port 3000).
- Knowledge & Documentation: Obsidian markdown vaults, local Git repositories (smoking-tigers-governance), and Notion (index layer).
# Memory & Database Stack
- Memory Backend: ZeroClaw (edjieun/zeroclaw) — Single lightweight Rust binary (<5MB) providing hybrid search (SQLite vector cosine embeddings via nomic-embed-text + FTS5 full-text keyword search).
- Databases:
- SQLite: Embedded storage for ZeroClaw and local agent memory.
- PostgreSQL: Docker-managed databases for OpenProjects, Mattermost, LedgerSMB, and Cal.com.
- Redis: In-memory caching for Cal.com.
# Hardware & Infrastructure Stack
- Hardware:
- Mac Mini M4: 24/7 On-Premise server running inference (LM Studio, Ollama), OpenClaw, ZeroClaw, and Nerve UI.
- M1 MacBook: On-Premise server hosting OpenProjects, Mattermost, and LedgerSMB.
- M4 Laptop: Interactive development device (VS Code, OpenCode, Obsidian).
- Networking & Mesh VPN: Tailscale overlay network (connecting all nodes across local LANs securely), Linksys router gateway, T-Mobile 5G ISP.
- Languages & Scripting: Rust, Python 3, TypeScript/Node.js, Bash/Shell, AppleScript (icalBuddy, memo, remindctl).
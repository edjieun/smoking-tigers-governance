# Composio Integration Skill

Access 600+ apps via Composio. Connected via MCP stdio server (`composio-mcp-server`).

## Configuration

- **MCP Server:** `composio-mcp-server` (installed globally via npm)
- **API Key:** stored in OpenClaw config (`mcp.servers.composio.env.COMPOSIO_API_KEY`)
- **Apps enabled:** GitHub, Notion, Discord, Google Drive, Google Calendar, Gmail, Google Docs, Google Sheets

## How It Works

OpenClaw starts `composio-mcp-server` as a stdio MCP server. The server exposes Composio tools for
each configured app. Tools are available to any agent with MCP access.

**Note:** The `composio-mcp-server` uses the Platform (`ak_`) API key and the Composio SDK.
Connections for each app must be established via [app.composio.dev](https://app.composio.dev)
under the matching project before tools will work.

## Adding/Changing Apps

Update `COMPOSIO_APPS` in OpenClaw config:
```
mcp.servers.composio.env.COMPOSIO_APPS = "GITHUB,NOTION,DISCORD,GMAIL,..."
```
Then restart OpenClaw.

## Available App Slugs (reference)
- `GMAIL`, `GOOGLEDRIVE`, `GOOGLECALENDAR`, `GOOGLEDOCS`, `GOOGLESHEETS`, `GOOGLETASKS`
- `GITHUB`, `NOTION`, `DISCORD`, `SLACK`, `LINEAR`, `JIRA`
- Full list: https://app.composio.dev/apps

## Connecting Accounts

1. Go to [app.composio.dev](https://app.composio.dev)
2. Select the correct project
3. Go to Connections → connect each app via OAuth
4. Restart OpenClaw

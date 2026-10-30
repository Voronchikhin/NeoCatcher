# AI agents (MCP)

NeoCatcher lets AI coding agents — Claude Code, Claude Desktop, Cursor, VS Code Copilot and other
[Model Context Protocol](https://modelcontextprotocol.io) clients — work with the traffic it captures. Instead of
copying requests into a chat, ask the agent and it reads them itself:

> *Why does the login call from the emulator fail?*
>
> *Find every request that returned a 5xx in the last few minutes and tell me what they have in common.*
>
> *Make `/api/orders` return a 503 so I can test the retry banner, then turn it off when I'm done.*

## Turn it on

1. Open the NeoCatcher tool window → **Server** tab → **AI agents (MCP)** → **Enable MCP Server**.
   It listens on `http://127.0.0.1:9950/mcp` and starts with the project from then on.
2. Click **Copy Config…** and pick your tool. The copied text contains a private access token.
3. Paste it into your tool as shown below, then restart or reconnect the tool.

=== "Claude Code"

    Run the copied command in a terminal:

    ```bash
    claude mcp add --transport http neocatcher http://127.0.0.1:9950/mcp --header "Authorization: Bearer <token>"
    ```

    Check it with `claude mcp list`, or `/mcp` inside a session.

=== "Cursor"

    Add the copied JSON to `.cursor/mcp.json` in your project, or to `~/.cursor/mcp.json` for all projects:

    ```json
    {
      "mcpServers": {
        "neocatcher": {
          "url": "http://127.0.0.1:9950/mcp",
          "headers": { "Authorization": "Bearer <token>" }
        }
      }
    }
    ```

=== "VS Code"

    Add the copied JSON to `.vscode/mcp.json`:

    ```json
    {
      "servers": {
        "neocatcher": {
          "type": "http",
          "url": "http://127.0.0.1:9950/mcp",
          "headers": { "Authorization": "Bearer <token>" }
        }
      }
    }
    ```

=== "Claude Desktop"

    Claude Desktop starts local commands, so it reaches NeoCatcher's HTTP endpoint through a small bridge. Paste the
    configuration from **Copy Config… → Claude Desktop** into `claude_desktop_config.json` (**Settings → Developer →
    Edit Config**), then quit Claude Desktop completely (tray icon → Quit) and start it again.

    The bridge uses only what the system already has: `sh` and `curl` on macOS and Linux, Windows PowerShell on
    Windows. Nothing to install, no Node.js or Python. The copied configuration looks like this, with the bridge
    script in place of `…`; paste it as it is:

    ```json
    {
      "mcpServers": {
        "neocatcher": {
          "command": "/bin/sh",
          "args": ["-c", "…"],
          "env": {
            "NEOCATCHER_URL": "http://127.0.0.1:9950/mcp",
            "NEOCATCHER_TOKEN": "<token>"
          }
        }
      }
    }
    ```

    On Windows the command is `powershell.exe` and the script comes in the `NEOCATCHER_BRIDGE` variable. The token stays
    in the environment, off the command line.

=== "Other clients"

    Any client that supports the **Streamable HTTP** transport works: URL `http://127.0.0.1:9950/mcp`, header
    `Authorization: Bearer <token>`. Clients that only start local commands use the Claude Desktop configuration:
    its `command`, `args` and `env` work in any of them.

The IDE must be open with the project for the agent to reach NeoCatcher. Start the proxy too — otherwise there is no
traffic to look at.

## What agents can do

Reading is always available:

| Tool | What it does |
| --- | --- |
| `proxy_status` | Proxy state, addresses (127.0.0.1, 10.0.2.2 for emulators), certificate, whether HTTPS is decrypted, request counts |
| `list_clients` | Apps and devices using the proxy, and whether their HTTPS is decrypted |
| `list_requests` | Captured calls, newest first; filter by host, path, method, status range, rules applied |
| `get_exchange` | Headers and bodies of one call, as received and after your rules changed them |
| `search_traffic` | Text search across URLs, headers and bodies |
| `export_curl` | A cURL command that replays a call |
| `list_rules`, `list_breakpoints` | Your rules (with their definitions), breakpoints and paused responses |

Changing NeoCatcher needs your permission and [NeoCatcher Pro](pricing.md): open the server settings (gear icon) and
turn on **Allow agents to change rules, breakpoints and paused responses**. Agents then also get:

| Tool | What it does |
| --- | --- |
| `create_request_rule`, `create_response_rule` | Add a rule, e.g. "make /api/login return 503", "serve /api/orders from mocks/orders.json", "delay search by 3 s" |
| `set_rule_active`, `delete_rule` | Turn rules on or off, delete them |
| `add_response_breakpoint` | Pause matching responses |
| `resume_paused_response`, `abort_paused_response` | Send a paused response on (edited or not) or fail the call |

Rules created by an agent appear in **Request Mappings** / **Response Mappings** right away, and every change is
written to the **Activity** log in the Server tab. Agents use the same rule format as the [YAML/JSON editor](rules.md),
so you can open and adjust their rules like your own.

## Try it

After connecting, ask your agent:

1. *"What does NeoCatcher see?"* — it calls `proxy_status` and `list_clients`.
2. *"Show me the slowest requests and their responses."* — `list_requests` + `get_exchange`.
3. *"Make GET /posts/2 return 503 with a JSON error, I'll test the app, then turn the rule off."* — needs changes
   allowed.

## Security and privacy

- **Local only.** The MCP server listens on `127.0.0.1` and requires the access token. Requests from web pages on
  other origins are rejected.
- **Secrets are redacted** by default: `Authorization`, `Cookie`, `Set-Cookie`, API-key and CSRF headers reach the
  agent as a placeholder. You can reveal them in the server settings.
- **Bodies are sent as captured.** Whatever the agent reads goes to the AI provider that runs it, under that
  provider's terms. NeoCatcher itself sends nothing anywhere.
- **Read-only by default.** Changing tools appear only after you allow them.
- **Revoke access** with **Regenerate token** in the Server tab; every configured tool then needs the new token.
- The token is stored in the IDE's password safe. Don't commit configuration files that contain it.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| The tool says it cannot connect | Open the project in the IDE and check **AI agents (MCP)** says *Listening*. Check the port in the URL matches the server settings. |
| HTTP 401 / "wrong or missing token" | The token changed (regenerated) or was pasted incompletely. Copy the configuration again. |
| "Port 9950 is already in use" | Pick another MCP port in the server settings and copy the configuration again. |
| The agent sees no requests | Start the proxy and send traffic through it — see [Getting started](getting-started.md). |
| Create/delete tools are missing | Allow changes in the server settings (needs Pro), then reconnect the agent: tools are listed once per connection. `proxy_status` reports `changes_need_pro` when only the license is missing. |
| Claude Desktop shows no NeoCatcher tools | Quit it completely and restart. Its MCP log (Settings → Developer) shows why the bridge stopped: *not reachable* means the IDE or the MCP server is off; *refused the request* means the token or port changed, so copy the configuration again. |
| Claude Desktop logs "Failed to spawn process" | The configuration was copied from NeoCatcher 1.0.2 or earlier and runs `npx`, which needs Node.js. Copy the configuration again from 1.0.3 or later. |

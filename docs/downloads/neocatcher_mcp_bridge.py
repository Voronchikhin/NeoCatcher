#!/usr/bin/env python3
"""
Bridges an MCP client that only starts local commands (stdio, e.g. Claude Desktop) to NeoCatcher's
MCP server over HTTP. Standard library only, so it works without Node.js.

Configure the client with:
  command: python
  args:    ["<path>/neocatcher_mcp_bridge.py"]
  env:     NEOCATCHER_MCP_URL (default http://127.0.0.1:9950/mcp), NEOCATCHER_MCP_TOKEN (required)

Each line on stdin is one JSON-RPC message; answers are written to stdout one per line.

The website offers a copy at docs/downloads/ in the public Voronchikhin/NeoCatcher repo; update it there when
this file changes.
"""
import json
import os
import sys
import urllib.error
import urllib.request

URL = os.environ.get("NEOCATCHER_MCP_URL", "http://127.0.0.1:9950/mcp")
TOKEN = os.environ.get("NEOCATCHER_MCP_TOKEN", "")

stdin = open(sys.stdin.fileno(), "r", encoding="utf-8", newline="\n", closefd=False)
stdout = open(sys.stdout.fileno(), "w", encoding="utf-8", newline="\n", closefd=False)


def log(message: str) -> None:
    # stderr ends up in the client's MCP log; stdout is reserved for protocol messages.
    print(f"neocatcher-bridge: {message}", file=sys.stderr, flush=True)


def reply_error(message_id, text: str) -> None:
    if message_id is None:
        return
    stdout.write(json.dumps({"jsonrpc": "2.0", "id": message_id, "error": {"code": -32000, "message": text}}) + "\n")
    stdout.flush()


def forward(line: str) -> None:
    try:
        message_id = json.loads(line).get("id")
    except (ValueError, AttributeError):
        message_id = None
    request = urllib.request.Request(
        URL,
        data=line.encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {TOKEN}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            body = response.read().decode("utf-8")
            if response.status == 200 and body.strip():
                stdout.write(body.strip() + "\n")
                stdout.flush()
    except urllib.error.HTTPError as e:
        hint = {401: "wrong or missing token (NEOCATCHER_MCP_TOKEN)", 403: "origin rejected"}.get(e.code, e.reason)
        log(f"HTTP {e.code}: {hint}")
        reply_error(message_id, f"NeoCatcher MCP server answered HTTP {e.code}: {hint}")
    except (urllib.error.URLError, OSError) as e:
        log(f"cannot reach {URL}: {e}")
        reply_error(message_id, f"NeoCatcher is not reachable at {URL}. Open the project in the IDE and enable "
                                f"the MCP server in NeoCatcher's Server tab. ({e})")


def main() -> None:
    if not TOKEN:
        log("NEOCATCHER_MCP_TOKEN is not set; copy it from NeoCatcher → Server tab → AI agents → Copy Config")
    log(f"forwarding to {URL}")
    for line in stdin:
        line = line.strip()
        if line:
            forward(line)


if __name__ == "__main__":
    main()

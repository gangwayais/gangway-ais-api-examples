#!/bin/sh
# Call one MCP tool with your key. search_ports costs no credits.
. "$(dirname "$0")/_key.sh"
curl -sS -X POST "$BASE/mcp" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer $GANGWAY_KEY" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_ports","arguments":{"query":"Dunkerque"}}}'
echo

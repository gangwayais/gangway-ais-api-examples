#!/bin/sh
# The MCP connector's tools. Listing them needs no key.
curl -sS -X POST "${GANGWAY_BASE_URL:-https://gangwayais.com}/mcp" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
echo

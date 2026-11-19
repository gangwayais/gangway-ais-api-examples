#!/bin/sh
# Add the Gangway AIS MCP connector to Claude Code, with your key in a header.
: "${GANGWAY_KEY:?Set GANGWAY_KEY first, for example: export GANGWAY_KEY=gw_live_...}"
claude mcp add --transport http gangway-ais https://gangwayais.com/mcp \
  --header "Authorization: Bearer $GANGWAY_KEY"

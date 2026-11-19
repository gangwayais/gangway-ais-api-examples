#!/bin/sh
# Service status. Needs no key.
curl -sS "${GANGWAY_BASE_URL:-https://gangwayais.com}/v1/status"
echo

#!/bin/sh
# Waiting times at anchor for a port. 5 credits. Needs Data API access by agreement.
. "$(dirname "$0")/_key.sh"
curl -sS "$BASE/v1/ports/${1:-NLRTM}/waiting" \
  -H "Authorization: Bearer $GANGWAY_KEY"
echo

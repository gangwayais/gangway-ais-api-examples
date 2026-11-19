#!/bin/sh
# Find ports by name or UN/LOCODE. Costs no credits.
. "$(dirname "$0")/_key.sh"
curl -sS -G "$BASE/v1/ports/search" \
  --data-urlencode "q=${1:-Dunkerque}" \
  -H "Authorization: Bearer $GANGWAY_KEY"
echo

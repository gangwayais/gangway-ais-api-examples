#!/bin/sh
# Arrivals at a port over the last 7 days. 1 credit per row returned.
# list can be expected, inport, arrived or departed.
. "$(dirname "$0")/_key.sh"
curl -sS -G "$BASE/v1/ports/${1:-BEANR}/vessels" \
  --data-urlencode "list=${2:-arrived}" \
  --data-urlencode "limit=10" \
  -H "Authorization: Bearer $GANGWAY_KEY"
echo

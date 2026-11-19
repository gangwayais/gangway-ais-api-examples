#!/bin/sh
# Find vessels by name or MMSI prefix. 1 credit per vessel returned.
# Usage: ./search-vessels.sh "VESSEL NAME"
. "$(dirname "$0")/_key.sh"
curl -sS -G "$BASE/v1/vessels/search" \
  --data-urlencode "q=${1:-EXAMPLE}" \
  --data-urlencode "limit=5" \
  -H "Authorization: Bearer $GANGWAY_KEY"
echo

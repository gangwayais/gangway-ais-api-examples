#!/bin/sh
# Vessels in a box as GeoJSON. 1 credit per vessel returned.
# bbox is min_lat,min_lon,max_lat,max_lon. A free key takes a box up to 1 square degree.
. "$(dirname "$0")/_key.sh"
curl -sS -G "$BASE/v1/vessels" \
  --data-urlencode "bbox=${1:-60.2,5.0,60.6,5.6}" \
  --data-urlencode "limit=20" \
  -H "Authorization: Bearer $GANGWAY_KEY"
echo

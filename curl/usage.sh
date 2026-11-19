#!/bin/sh
# Your plan, credits used and left, limits. Costs no credits.
# -i shows the response headers too.
. "$(dirname "$0")/_key.sh"
curl -sS -i "$BASE/v1/usage" \
  -H "Authorization: Bearer $GANGWAY_KEY"
echo

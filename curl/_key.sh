# Sourced by the other scripts. Stops with a clear message when no key is set.
if [ -z "${GANGWAY_KEY:-}" ]; then
  echo "Set GANGWAY_KEY first, for example: export GANGWAY_KEY=gw_live_..." >&2
  echo "Make a key in your account: https://gangwayais.com/account/" >&2
  exit 1
fi
BASE="${GANGWAY_BASE_URL:-https://gangwayais.com}"

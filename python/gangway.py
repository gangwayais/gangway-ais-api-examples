"""A small client for the Gangway AIS Data API, standard library only.

Your key comes from the GANGWAY_KEY environment variable.
Docs: https://gangwayais.com/docs/
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ.get("GANGWAY_BASE_URL", "https://gangwayais.com")


def key():
    k = os.environ.get("GANGWAY_KEY", "").strip()
    if not k:
        sys.exit("Set GANGWAY_KEY first, for example: export GANGWAY_KEY=gw_live_...\n"
                 "Make a key in your account: https://gangwayais.com/account/")
    return k


def get(path, params=None, auth=True):
    """GET a /v1 path and return the JSON answer. Stops with the API's own words on an error."""
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "gangway-ais-examples"})
    if auth:
        req.add_header("Authorization", "Bearer " + key())
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            used = r.headers.get("X-Credits-Used")
            left = r.headers.get("X-Credits-Remaining")
            if used is not None and left is not None:
                print(f"(credits used {used}, left {left})", file=sys.stderr)
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        hint = {401: "The key is missing or not valid.",
                402: "No credits left, or this needs a paid plan.",
                429: f"Too many requests. Wait {e.headers.get('Retry-After', 'a few')} seconds."}.get(e.code, "")
        sys.exit(f"HTTP {e.code} {hint}\n{body}")

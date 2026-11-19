"""Talk to the Gangway AIS MCP connector directly, standard library only.

Most people add the connector to an AI assistant instead (see ../mcp/).
Listing the tools needs no key. Calling one needs GANGWAY_KEY.

Usage: python mcp_client.py            lists the tools
       python mcp_client.py Dunkerque  calls search_ports
"""
import json
import os
import sys
import urllib.error
import urllib.request

URL = os.environ.get("GANGWAY_BASE_URL", "https://gangwayais.com") + "/mcp"


def rpc(method, params=None, key=None):
    body = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST", headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "User-Agent": "gangway-ais-examples"})
    if key:
        req.add_header("Authorization", "Bearer " + key)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            answer = json.load(r)
    except urllib.error.HTTPError as e:
        answer = json.loads(e.read() or b"{}")
        if "error" not in answer:
            sys.exit(f"HTTP {e.code}")
    if "error" in answer:
        sys.exit(answer["error"].get("message", "The connector refused the request."))
    return answer


if len(sys.argv) < 2:
    for t in rpc("tools/list")["result"]["tools"]:
        print(t["name"])
else:
    key = os.environ.get("GANGWAY_KEY", "").strip()
    if not key:
        sys.exit("Set GANGWAY_KEY first, for example: export GANGWAY_KEY=gw_live_...")
    res = rpc("tools/call", {"name": "search_ports", "arguments": {"query": sys.argv[1]}}, key)["result"]
    for part in res["content"]:
        if part["type"] == "text":
            print(part["text"])
    if res.get("isError"):
        sys.exit(1)

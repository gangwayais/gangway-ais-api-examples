"""Service status. Needs no key."""
from gangway import get

s = get("/v1/status", auth=False)
print("Server time:", s["time"])
print(s["notice"])

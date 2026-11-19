"""Find vessels by name or MMSI prefix. 1 credit per vessel returned.

Usage: python search_vessels.py "VESSEL NAME"
"""
import sys
from gangway import get

q = sys.argv[1] if len(sys.argv) > 1 else "EXAMPLE"
answer = get("/v1/vessels/search", {"q": q, "limit": 5})
for f in answer["features"]:
    p = f["properties"]
    if f["geometry"]:
        lon, lat = f["geometry"]["coordinates"]
        where = f"{lat:.4f}, {lon:.4f} at {p['seen']}"
    else:
        where = "position not given"
    print(f"{p['mmsi']}  {p.get('name') or '?':<24} {where}")

"""Vessels in a box as GeoJSON. 1 credit per vessel returned.

bbox is min_lat,min_lon,max_lat,max_lon. A free key takes a box up to 1 square degree.
Usage: python vessels_in_area.py 60.2,5.0,60.6,5.6
"""
import sys
from gangway import get

bbox = sys.argv[1] if len(sys.argv) > 1 else "60.2,5.0,60.6,5.6"
answer = get("/v1/vessels", {"bbox": bbox, "limit": 20})
for f in answer["features"]:
    p = f["properties"]
    lon, lat = f["geometry"]["coordinates"]
    print(f"{p['mmsi']}  {p.get('name') or '?':<24} {lat:.4f}, {lon:.4f}  {p.get('sog')} kn")
if answer.get("truncated"):
    print("More vessels were left out. Raise limit to see them.")

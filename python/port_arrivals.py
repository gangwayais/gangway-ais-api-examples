"""Arrivals at a port over the last 7 days. 1 credit per row returned.

Usage: python port_arrivals.py BEANR arrived
list can be expected, inport, arrived or departed.
"""
import sys
from gangway import get

locode = sys.argv[1] if len(sys.argv) > 1 else "BEANR"
lst = sys.argv[2] if len(sys.argv) > 2 else "arrived"
answer = get(f"/v1/ports/{locode}/vessels", {"list": lst, "limit": 10})
print(answer["port"]["name"], lst)
for row in answer["rows"]:
    print(f"{row.get('when') or '':<22} {row['mmsi']}  {row.get('name') or '?':<24} {row.get('length') or ''} m")

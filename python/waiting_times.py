"""Waiting times at anchor for a port. 5 credits. Needs Data API access by agreement.

Usage: python waiting_times.py NLRTM
"""
import sys
from gangway import get

locode = sys.argv[1] if len(sys.argv) > 1 else "NLRTM"
w = get(f"/v1/ports/{locode}/waiting")
week = w["week"]
if week["enough"]:
    print(f"{w['port']['name']}: median wait {week['median_h']} h, 90th percentile {week['p90_h']} h this week")
else:
    print(f"{w['port']['name']}: too few vessels this week for a figure")

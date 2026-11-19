// Vessels in a box as GeoJSON. 1 credit per vessel returned.
// bbox is min_lat,min_lon,max_lat,max_lon. A free key takes a box up to 1 square degree.
// Usage: node vessels-in-area.mjs 60.2,5.0,60.6,5.6
import { get } from "./gangway.mjs";

const answer = await get("/v1/vessels", { bbox: process.argv[2] || "60.2,5.0,60.6,5.6", limit: 20 });
for (const f of answer.features) {
  const p = f.properties, [lon, lat] = f.geometry.coordinates;
  console.log(`${p.mmsi}  ${(p.name || "?").padEnd(24)} ${lat.toFixed(4)}, ${lon.toFixed(4)}  ${p.sog} kn`);
}
if (answer.truncated) console.log("More vessels were left out. Raise limit to see them.");

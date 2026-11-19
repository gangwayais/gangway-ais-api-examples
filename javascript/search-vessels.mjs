// Find vessels by name or MMSI prefix. 1 credit per vessel returned.
// Usage: node search-vessels.mjs "VESSEL NAME"
import { get } from "./gangway.mjs";

const answer = await get("/v1/vessels/search", { q: process.argv[2] || "EXAMPLE", limit: 5 });
for (const f of answer.features) {
  const p = f.properties;
  const where = f.geometry ? `${f.geometry.coordinates[1].toFixed(4)}, ${f.geometry.coordinates[0].toFixed(4)} at ${p.seen}` : "position not given";
  console.log(`${p.mmsi}  ${(p.name || "?").padEnd(24)} ${where}`);
}

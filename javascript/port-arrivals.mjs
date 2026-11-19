// Arrivals at a port over the last 7 days. 1 credit per row returned.
// Usage: node port-arrivals.mjs BEANR arrived
// list can be expected, inport, arrived or departed.
import { get } from "./gangway.mjs";

const locode = process.argv[2] || "BEANR", list = process.argv[3] || "arrived";
const answer = await get(`/v1/ports/${locode}/vessels`, { list, limit: 10 });
console.log(answer.port.name, list);
for (const row of answer.rows) console.log(`${(row.when || "").padEnd(22)} ${row.mmsi}  ${(row.name || "?").padEnd(24)} ${row.length ?? ""} m`);

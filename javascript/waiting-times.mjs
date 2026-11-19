// Waiting times at anchor for a port. 5 credits. Needs a paid Data API plan.
// Usage: node waiting-times.mjs NLRTM
import { get } from "./gangway.mjs";

const w = await get(`/v1/ports/${process.argv[2] || "NLRTM"}/waiting`);
const { week } = w;
console.log(week.enough
  ? `${w.port.name}: median wait ${week.median_h} h, 90th percentile ${week.p90_h} h this week`
  : `${w.port.name}: too few vessels this week for a figure`);

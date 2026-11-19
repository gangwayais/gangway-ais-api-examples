// A small client for the Gangway AIS Data API. Node 18 or newer, no packages.
// Your key comes from the GANGWAY_KEY environment variable.
// Docs: https://gangwayais.com/docs/

export const BASE = process.env.GANGWAY_BASE_URL || "https://gangwayais.com";

export function key() {
  const k = (process.env.GANGWAY_KEY || "").trim();
  if (!k) {
    console.error("Set GANGWAY_KEY first, for example: export GANGWAY_KEY=gw_live_...");
    console.error("Make a key in your account: https://gangwayais.com/account/");
    process.exit(1);
  }
  return k;
}

// GET a /v1 path and return the JSON answer. Stops with the API's own words on an error.
export async function get(path, params = {}, { auth = true } = {}) {
  const url = new URL(BASE + path);
  for (const [k, v] of Object.entries(params)) if (v != null) url.searchParams.set(k, v);
  const headers = { Accept: "application/json", "User-Agent": "gangway-ais-examples" };
  if (auth) headers.Authorization = `Bearer ${key()}`;
  const r = await fetch(url, { headers });
  if (!r.ok) {
    const hint = { 401: "The key is missing or not valid.", 402: "No credits left, or this needs a paid plan.",
      429: `Too many requests. Wait ${r.headers.get("retry-after") || "a few"} seconds.` }[r.status] || "";
    console.error(`HTTP ${r.status} ${hint}\n${await r.text()}`);
    process.exit(1);
  }
  const used = r.headers.get("x-credits-used"), left = r.headers.get("x-credits-remaining");
  if (used != null && left != null) console.error(`(credits used ${used}, left ${left})`);
  return r.json();
}

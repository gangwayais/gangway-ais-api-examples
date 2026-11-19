// Talk to the Gangway AIS MCP connector directly. Node 18 or newer, no packages.
// Most people add the connector to an AI assistant instead (see ../mcp/).
// Listing the tools needs no key. Calling one needs GANGWAY_KEY.
//
// Usage: node mcp-client.mjs            lists the tools
//        node mcp-client.mjs Dunkerque  calls search_ports

const URL_ = (process.env.GANGWAY_BASE_URL || "https://gangwayais.com") + "/mcp";

async function rpc(method, params, key) {
  const headers = { "Content-Type": "application/json", Accept: "application/json, text/event-stream", "User-Agent": "gangway-ais-examples" };
  if (key) headers.Authorization = `Bearer ${key}`;
  const r = await fetch(URL_, { method: "POST", headers, body: JSON.stringify({ jsonrpc: "2.0", id: 1, method, ...(params && { params }) }) });
  const answer = await r.json().catch(() => ({ error: { message: `HTTP ${r.status}` } }));
  if (answer.error) { console.error(answer.error.message || "The connector refused the request."); process.exit(1); }
  return answer;
}

const query = process.argv[2];
if (!query) {
  const { result } = await rpc("tools/list");
  for (const t of result.tools) console.log(t.name);
} else {
  const key = (process.env.GANGWAY_KEY || "").trim();
  if (!key) { console.error("Set GANGWAY_KEY first, for example: export GANGWAY_KEY=gw_live_..."); process.exit(1); }
  const { result } = await rpc("tools/call", { name: "search_ports", arguments: { query } }, key);
  for (const part of result.content) if (part.type === "text") console.log(part.text);
  if (result.isError) process.exit(1);
}

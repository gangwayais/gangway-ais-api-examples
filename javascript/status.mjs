// Service status. Needs no key.
import { get } from "./gangway.mjs";

const s = await get("/v1/status", {}, { auth: false });
console.log("Server time:", s.time);
console.log(s.notice);

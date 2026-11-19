<p align="center">
  <a href="https://gangwayais.com"><img src="https://gangwayais.com/img/ais-logo-cyan.png" alt="Gangway AIS" width="280"></a>
</p>

# Gangway AIS API examples

Small working examples for the [Gangway AIS](https://gangwayais.com) Data API and MCP connector, in curl, Python and JavaScript. Each one is a single short file you can read in a minute and copy into your own code.

- [Documentation](https://gangwayais.com/docs/) for the full reference of endpoints, parameters and answers
- [Quickstart](https://gangwayais.com/docs/quickstart/)
- [Credits and limits](https://gangwayais.com/docs/credits/)
- [Plans](https://gangwayais.com/#pricing)
- [MCP connector](https://gangwayais.com/docs/mcp/)

## Your key

Make a key in [your account](https://gangwayais.com/account/). The examples read it from the `GANGWAY_KEY` environment variable and never from a file in this repository.

```sh
export GANGWAY_KEY=gw_live_...
```

Or copy `.env.example` to `.env` and load it in your shell. `.env` is in `.gitignore` so it stays out of your commits. Keep your key on your server, never in a web page or an app bundle. If a key leaks, replace it in your account and the old one stops working at once.

Two calls need no key. The service status and the list of MCP tools.

## What is here

| Example | Endpoint | Credits | curl | Python | JavaScript |
|---|---|---|---|---|---|
| Service status | `GET /v1/status` | none, no key | [status.sh](curl/status.sh) | [status.py](python/status.py) | [status.mjs](javascript/status.mjs) |
| Search vessels | `GET /v1/vessels/search` | 1 per vessel | [search-vessels.sh](curl/search-vessels.sh) | [search_vessels.py](python/search_vessels.py) | [search-vessels.mjs](javascript/search-vessels.mjs) |
| Vessels in an area | `GET /v1/vessels` | 1 per vessel | [vessels-in-area.sh](curl/vessels-in-area.sh) | [vessels_in_area.py](python/vessels_in_area.py) | [vessels-in-area.mjs](javascript/vessels-in-area.mjs) |
| Search ports | `GET /v1/ports/search` | none | [search-ports.sh](curl/search-ports.sh) | | |
| Arrivals at a port | `GET /v1/ports/{locode}/vessels` | 1 per row | [port-arrivals.sh](curl/port-arrivals.sh) | [port_arrivals.py](python/port_arrivals.py) | [port-arrivals.mjs](javascript/port-arrivals.mjs) |
| Waiting times at anchor | `GET /v1/ports/{locode}/waiting` | 5, paid plan | [waiting-times.sh](curl/waiting-times.sh) | [waiting_times.py](python/waiting_times.py) | [waiting-times.mjs](javascript/waiting-times.mjs) |
| Your usage | `GET /v1/usage` | none | [usage.sh](curl/usage.sh) | | |
| MCP tools | `POST /mcp` | as the API | [mcp-list-tools.sh](curl/mcp-list-tools.sh), [mcp-call-tool.sh](curl/mcp-call-tool.sh) | [mcp_client.py](python/mcp_client.py) | [mcp-client.mjs](javascript/mcp-client.mjs) |

The waiting times example needs a paid Data API plan. With a free key it answers `402`. The others work with a free key within its limits, which are on the [credits page](https://gangwayais.com/docs/credits/).

## Run them

### curl

```sh
cd curl
./status.sh
./search-vessels.sh "VESSEL NAME"
./vessels-in-area.sh 60.2,5.0,60.6,5.6
./port-arrivals.sh BEANR arrived
```

### Python

Python 3.8 or newer, standard library only. Nothing to install.

```sh
cd python
python3 status.py
python3 search_vessels.py "VESSEL NAME"
python3 vessels_in_area.py 60.2,5.0,60.6,5.6
python3 port_arrivals.py BEANR arrived
```

`gangway.py` is a small client the other files share. It sends your key, prints the credits each answer cost and stops with the API's own message on an error.

On macOS with Python from python.org, run `Install Certificates.command` in the Python folder once if a request fails with `CERTIFICATE_VERIFY_FAILED`.

### JavaScript

Node 18 or newer, no packages.

```sh
cd javascript
node status.mjs
node search-vessels.mjs "VESSEL NAME"
node vessels-in-area.mjs 60.2,5.0,60.6,5.6
node port-arrivals.mjs BEANR arrived
```

## MCP connector

The connector lets an AI assistant answer questions about vessels and ports with your key. It is hosted at `https://gangwayais.com/mcp`. There is nothing to install.

| Client | File |
|---|---|
| Claude Code | [mcp/claude-code.sh](mcp/claude-code.sh) |
| Claude desktop app | [mcp/claude-desktop.json](mcp/claude-desktop.json) |
| Cursor, VS Code, Windsurf and others | [mcp/other-clients.json](mcp/other-clients.json) |

Put your own key in place of `gw_live_...`. A free key answers the tools marked for free accounts on the [MCP page](https://gangwayais.com/docs/mcp/). The other tools need a paid plan.

`python/mcp_client.py` and `javascript/mcp-client.mjs` show the protocol itself. The connector speaks streamable HTTP, takes POST only and gives one JSON answer per request with no sessions.

## Good to know

- Each answer says in its headers what it cost. `X-Credits-Used` and `X-Credits-Remaining`.
- A request that finds nothing or fails costs no credits.
- On `429` wait for the seconds in `Retry-After` before the next request.
- Answers carry an `attribution` field. Keep it when you publish what the API returns.
- Vessel positions come only where we may pass them on. A vessel without one comes with `position_withheld: true`.

## Licence

MIT. See [LICENSE](LICENSE). Copyright Motto Marine International SARL. The licence covers the example code in this repository, not the data the API returns, which is governed by the [Gangway AIS terms](https://gangwayais.com/legal/terms/). The Gangway AIS name and logo are not covered by the licence.

Questions? [desk@gangwayais.com](mailto:desk@gangwayais.com)

<sub>AIS data can be missing, delayed or wrong. Not for navigation.</sub>

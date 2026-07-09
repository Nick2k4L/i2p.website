---
title: "I2PControl JSON-RPC"
description: "Remote router management API via the I2PControl webapp"
slug: "i2pcontrol"
lastUpdated: "2026-07-09"
accurateFor: "2.12.0"
reviewStatus: "needs-review"
---
# I2PControl API Documentation

I2PControl is a **JSON-RPC 2.0** API bundled with the I2P router (since version 0.9.39). It enables authenticated monitoring and control of the router via structured JSON requests.

> **Default password:** `itoopie` — this is the factory default and **should be changed** immediately for security.

---

## 1. Overview & Access

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Implementation</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default Endpoint</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java I2P (2.10.0+)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>http://127.0.0.1:7657/jsonrpc/</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HTTP</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">❌ Must be enabled via WebApps (Router Console)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bundled webapp</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2pd (C++ implementation)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>https://127.0.0.1:7650/</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HTTPS</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Enabled by default</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Legacy plugin behavior</td>
    </tr>
  </tbody>
</table>

In the Java I2P case, you must go to **Router Console → WebApps → I2PControl** and enable it (set to start automatically).  
Once active, all methods require that you first authenticate and receive a session token.

---

## 2. JSON-RPC Format

All requests follow the JSON-RPC 2.0 structure:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "MethodName",
  "params": {
    /* named parameters */
  }
}
```

A successful response includes a `result` field; on failure, an `error` object is returned:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": { /* data */ }
}
```

or

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "error": {
    "code": -32001,
    "message": "Invalid password"
  }
}
```

---

## 3. Authentication Flow

### Request (Authenticate)

```bash
curl -s -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": "1",
        "method": "Authenticate",
        "params": {
          "API": 1,
          "Password": "itoopie"
        }
      }' \
  http://127.0.0.1:7657/jsonrpc/
```

### Successful Response

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    "Token": "a1b2c3d4e5",
    "API": 1
  }
}
```

You must include that `Token` in all subsequent requests in the `params`.

---

## 4. Methods & Endpoints

### 4.1 RouterInfo

Fetches key telemetry about the router.

**Request Example**

```bash
curl -s -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": "2",
        "method": "RouterInfo",
        "params": {
          "Token": "a1b2c3d4e5",
          "i2p.router.version": "",
          "i2p.router.status": "",
          "i2p.router.net.status": "",
          "i2p.router.net.tunnels.participating": "",
          "i2p.router.net.bw.inbound.1s": "",
          "i2p.router.net.bw.outbound.1s": ""
        }
      }' \
  http://127.0.0.1:7657/jsonrpc/
```

Include each desired key in `params` with any value. Only requested keys are returned.

#### Router and Bandwidth Fields

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.status</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Free-format, translated router status intended for display.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.uptime</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Router uptime in milliseconds. Older i2pd versions may return a string.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.version</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Full router version.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.id</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String or null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Local router hash in I2P Base64.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.info</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String or null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Serialized local RouterInfo in I2P Base64.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.clockskew</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long or null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Average peer clock skew in milliseconds.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.news</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Rendered router news entries.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.logs</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Recent buffered router log messages.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.logs.clear</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Clears the router log buffer and returns <code>success</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.status</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Network status code; see the table below.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.used.inbound.total</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Total allocated inbound bytes since startup.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.used.outbound.total</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Total allocated outbound bytes since startup.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.inbound.1s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Current inbound bandwidth in bytes per second.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.inbound.15s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15-second average inbound bandwidth in bytes per second.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.outbound.1s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Current outbound bandwidth in bytes per second.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.outbound.15s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15-second average outbound bandwidth in bytes per second.</td></tr>
  </tbody>
</table>

#### Status Code Enum (`i2p.router.net.status`)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OK</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TESTING</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FIREWALLED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HIDDEN</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">WARN_FIREWALLED_AND_FAST</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">WARN_FIREWALLED_AND_FLOODFILL</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">WARN_FIREWALLED_WITH_INBOUND_TCP</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">WARN_FIREWALLED_WITH_UDP_DISABLED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ERROR_I2CP</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ERROR_CLOCK_SKEW</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ERROR_PRIVATE_TCP_ADDRESS</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ERROR_SYMMETRIC_NAT</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ERROR_UDP_PORT_IN_USE</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">13</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ERROR_NO_ACTIVE_PEERS_CHECK_CONNECTION_AND_FIREWALL</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">14</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ERROR_UDP_DISABLED_AND_TCP_UNSET</td>
    </tr>
  </tbody>
</table>

#### Tunnel Fields

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.shareratio</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Tunnel share ratio.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.participating</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Number of participating tunnels.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.participating.info</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Participating-tunnel details, including peer hashes, tunnel IDs, expiration, message count, rate, and role.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.i2ptunnel</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Summary of all configured I2PTunnel controllers.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.exploratory.inbound</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">int</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Exploratory inbound tunnel count.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.exploratory.outbound</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">int</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Exploratory outbound tunnel count.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.exploratory.info.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Inbound and outbound exploratory-tunnel details.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.client.inbound</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">int</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Client inbound tunnel count.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.client.outbound</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">int</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Client outbound tunnel count.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.client.info.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">All client-tunnel details.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.client.inbound.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Inbound client-tunnel details.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.client.outbound.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Outbound client-tunnel details.</td></tr>
  </tbody>
</table>

Tunnel detail records contain direction, expiration, message count, and structured gateway, participant, and endpoint information. The I2PTunnel summary contains controller name, type, interface, ports, targets, status, destination, encryption, SSL, sharing, outproxy, and description fields when available.

#### NetDB and Peer Fields

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.knownpeers</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Number of known peers, excluding the local router.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.activepeers</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Number of active peers.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.fastpeers</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Number of peers classified as fast.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.highcapacitypeers</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Number of peers classified as high capacity.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.isreseeding</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Whether a reseed is in progress.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.peers</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Known peer hashes in I2P Base64.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.peers.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Known peer hashes in I2P Base64.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.activepeers.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Established peer hashes in I2P Base64.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.peers.info</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Serialized RouterInfo data for known peers.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.activepeers.info</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Serialized RouterInfo data for established peers.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.ntcp.limit</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">int</td><td style="border:1px solid var(--color-border); padding:0.6rem;">NTCP connection limit.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.ssu.limit</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">int</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU connection limit.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.bannedpeers</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Map</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer hashes mapped to expiration, cause, cause code, and transport details.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.netdb.activepeers.stats</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Per-session peer transport, direction, traffic, rate, idle, uptime, and queue statistics.</td></tr>
  </tbody>
</table>

#### Address Book Fields

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.addressbook.private.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Private address book entries.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.addressbook.local.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Local address book entries.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.addressbook.router.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Router address book entries.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.addressbook.published.list</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;Map&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Published address book entries.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.addressbook.subscriptions</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Map</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Subscription file path and entries.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.addressbook.config</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Map</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Address book configuration path and entries.</td></tr>
  </tbody>
</table>

Address book entry maps contain the hostname, Base32 address, Base64 values, public keys, certificate, and full Destination when available.

---

### 4.2 GetRate

Used to fetch rate metrics (e.g. bandwidth, tunnel success) over a given time window.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Stat</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Router RateStat name.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Period</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Rate period in milliseconds.</td></tr>
  </tbody>
</table>

**Request Example**

```bash
curl -s -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": "3",
        "method": "GetRate",
        "params": {
          "Token": "a1b2c3d4e5",
          "Stat": "bw.combined",
          "Period": 60000
        }
      }' \
  http://127.0.0.1:7657/jsonrpc/
```

**Sample Response**

```json
{
  "jsonrpc": "2.0",
  "id": "3",
  "result": {
    "Result": 12345.67
  }
}
```

---

### 4.3 RouterManager

Perform administrative actions.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Result</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Restart</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Initiates an immediate router restart.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>RestartGraceful</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Restarts after participating tunnels expire.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Shutdown</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Initiates an immediate router shutdown.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>ShutdownGraceful</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Shuts down after participating tunnels expire.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Reseed</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Starts a router reseed.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>FindUpdates</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean or String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Blocking. Searches for a signed router update.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Update</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Blocking. Starts a signed router update and returns its final status.</td></tr>
  </tbody>
</table>

**Request Example**

```bash
curl -s -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": "4",
        "method": "RouterManager",
        "params": {
          "Token": "a1b2c3d4e5",
          "Restart": true
        }
      }' \
  http://127.0.0.1:7657/jsonrpc/
```

**Successful Response**

```json
{
  "jsonrpc": "2.0",
  "id": "4",
  "result": {
    "Restart": null
  }
}
```

---

### 4.4 NetworkSetting

Get or set network configuration parameters (ports, upnp, bandwidth share, etc.)

Submit a key with `null` to read its current value, or submit a String to change it.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Accepted Value</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.ntcp.port</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String, 1–65535</td><td style="border:1px solid var(--color-border); padding:0.6rem;">NTCP port; a change requires restart.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.ntcp.hostname</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">NTCP hostname; a change requires restart.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.ntcp.autoip</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>always</code>, <code>true</code>, or <code>false</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">NTCP automatic address selection.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.ssu.port</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String, 1–65535</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU port; a change requires restart.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.ssu.hostname</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU external hostname; a change requires restart.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.ssu.autoip</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>ssu</code>, <code>local,ssu</code>, <code>upnp,ssu</code>, or <code>local,upnp,ssu</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU address-discovery sources.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.ssu.detectedip</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Read-only detected SSU address.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.upnp</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">UPnP setting.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.share</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String, 0–100</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Percentage of bandwidth available for participating tunnels.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.in</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Non-negative integer String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Inbound bandwidth limit in KiB/s.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.out</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Non-negative integer String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Outbound bandwidth limit in KiB/s.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.laptopmode</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Laptop mode setting.</td></tr>
  </tbody>
</table>

**Request Example (get current values)**

```bash
curl -s -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": "5",
        "method": "NetworkSetting",
        "params": {
          "Token": "a1b2c3d4e5",
          "i2p.router.net.ntcp.port": null,
          "i2p.router.net.ssu.port": null,
          "i2p.router.net.bw.share": null,
          "i2p.router.net.upnp": null
        }
      }' \
  http://127.0.0.1:7657/jsonrpc/
```

**Sample Response**

```json
{
  "jsonrpc": "2.0",
  "id": "5",
  "result": {
    "i2p.router.net.ntcp.port": "1234",
    "i2p.router.net.ssu.port": "5678",
    "i2p.router.net.bw.share": "50",
    "i2p.router.net.upnp": "true",
    "SettingsSaved": false,
    "RestartNeeded": false
  }
}
```

> Note: i2pd versions prior to 2.41 may return numeric types instead of strings — clients should handle both.

---

### 4.5 AdvancedSettings

Allows manipulating internal router parameters.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>get</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Returns one setting inside a <code>get</code> result object.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>getAll</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">n/a</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Returns the complete configuration map inside <code>getAll</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>set</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Map&lt;String, String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Updates the supplied settings without removing other keys.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>setAll</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Map&lt;String, String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Destructive:</strong> replaces all settings and removes keys not supplied.</td></tr>
  </tbody>
</table>

Parameter names are case-sensitive and use the lower camel-case spelling shown above.

**Request Example**

```bash
curl -s -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": "6",
        "method": "AdvancedSettings",
        "params": {
          "Token": "a1b2c3d4e5",
          "set": {
            "router.sharePercentage": "75",
            "i2np.flushInterval": "6000"
          }
        }
      }' \
  http://127.0.0.1:7657/jsonrpc/
```

**Response Example**

```json
{
  "jsonrpc": "2.0",
  "id": "6",
  "result": {}
}
```

---

### 4.6 Echo

Echoes a String for debugging and connectivity checks.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Echo</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Value returned as <code>Result</code>.</td></tr>
  </tbody>
</table>

```json
{
  "jsonrpc": "2.0",
  "id": "7",
  "method": "Echo",
  "params": {
    "Token": "a1b2c3d4e5",
    "Echo": "hello"
  }
}
```

```json
{
  "jsonrpc": "2.0",
  "id": "7",
  "result": {
    "Result": "hello"
  }
}
```

---

### 4.7 I2PControl

Manages I2PControl itself. The current Java handler supports password changes.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2pcontrol.password</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Sets a new I2PControl password and revokes existing authentication tokens.</td></tr>
  </tbody>
</table>

The result contains `SettingsSaved`. If the password was changed, the result also contains `"i2pcontrol.password": null`. Listen-address and listen-port settings from the legacy standalone plugin are not active in the current Java handler.

---

### 4.8 AddressBook

Adds or removes address book entries and replaces or updates address book files. Use the `RouterInfo` [address book fields](#address-book-fields) to read entries, subscriptions, and configuration.

Submit one operation per request. `SetConfig` and `SetSubscriptions` are file operations and do not use `Type`, `Hostname`, or `Destination`.

#### Add or Delete an Entry

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Type</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Required. <code>private</code>, <code>local</code>, <code>router</code>, or <code>published</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Hostname</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Required. Hostname to add or delete. Leading and trailing whitespace is removed.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Destination</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Required for addition and deletion. Accepts a full Base64 Destination, a resolvable <code>.i2p</code> or <code>.b32.i2p</code> hostname, or a URL whose host is resolvable.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Delete</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">any</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Optional. Presence of this key selects deletion; its value is ignored.</td></tr>
  </tbody>
</table>

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Backing Store</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Delete Behavior</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>private</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>privatehosts.txt</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Matches hostname and resolved Destination.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>local</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>userhosts.txt</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Matches hostname and resolved Destination.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>router</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>hosts.txt</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Matches hostname and resolved Destination.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>published</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Configured <code>published_addressbook</code> file</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Deletes by hostname after validating the supplied Destination.</td></tr>
  </tbody>
</table>

**Add Request**

```json
{
  "jsonrpc": "2.0",
  "id": "8",
  "method": "AddressBook",
  "params": {
    "Token": "a1b2c3d4e5",
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "<Base64 Destination>"
  }
}
```

**Add Response**

```json
{
  "jsonrpc": "2.0",
  "id": "8",
  "result": {
    "success": true,
    "message": "Added example.i2p in private addressbook"
  }
}
```

To delete the same entry, send the same request with `"Delete": true`. The response uses the same shape and reports whether the entry was removed.

#### Address Book Files

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>SetSubscriptions</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">List&lt;String&gt; or String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Replaces the complete subscriptions file. A String is split at line boundaries. Blank lines, lines beginning with <code>;</code>, and text after <code>#</code> are removed.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>SetConfig</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Map</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Merges keys into <code>addressbook/config.txt</code>. Values are converted to Strings. A null value removes that key. Unmentioned keys are preserved.</td></tr>
  </tbody>
</table>

**SetSubscriptions Request**

```json
{
  "jsonrpc": "2.0",
  "id": "9",
  "method": "AddressBook",
  "params": {
    "Token": "a1b2c3d4e5",
    "SetSubscriptions": [
      "http://example.i2p/hosts.txt",
      "http://example2.i2p/hosts.txt"
    ]
  }
}
```

```json
{
  "jsonrpc": "2.0",
  "id": "9",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/subscriptions.txt"
  }
}
```

**Common SetConfig Keys**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>subscriptions</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Subscriptions file path, relative to the address book directory unless absolute.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>update_delay</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Subscription update interval in hours.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>published_addressbook</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Published address book path.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>router_addressbook</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Router address book path.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>local_addressbook</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Local address book path.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>private_addressbook</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Private address book path.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_host</code>, <code>proxy_port</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">HTTP proxy used to retrieve subscriptions.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>should_publish</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Whether the published address book should be updated.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>etags</code>, <code>last_modified</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Files containing subscription caching metadata.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>log</code>, <code>theme</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Address book log path and UI theme.</td></tr>
  </tbody>
</table>

```json
{
  "jsonrpc": "2.0",
  "id": "10",
  "method": "AddressBook",
  "params": {
    "Token": "a1b2c3d4e5",
    "SetConfig": {
      "update_delay": "12",
      "proxy_host": "127.0.0.1",
      "proxy_port": "4444",
      "should_publish": "true"
    }
  }
}
```

On success, `SetConfig` returns `success: true` and the absolute path of the modified configuration file in `message`.

---

### 4.9 TunnelManager

Creates, edits, inspects, starts, stops, restarts, and deletes I2PTunnel controllers.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Name</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Required tunnel name and identifier.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Action</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>create</code>, <code>edit</code>, <code>get</code>, <code>start</code>, <code>stop</code>, <code>restart</code>, or <code>delete</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>All</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Optional for <code>start</code>, <code>stop</code>, and <code>restart</code>. Applies the action to all controllers.</td></tr>
  </tbody>
</table>

#### Actions and Responses

Action names should be sent in lowercase. `Name` is required for every action. For an all-tunnels action, `Name` is accepted but ignored.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Action</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Behavior</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>create</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Creates and saves a new controller. Starts it in the background when <code>StartOnLoad</code> is true.</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code> and a <code>results</code> list of controller messages.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>edit</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Rebuilds the managed configuration for the existing controller and saves it.</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>get</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reads controller status, destinations, key state, and saved configuration.</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code> and <code>info</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>start</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Starts one controller.</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>stop</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Stops one controller.</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>restart</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Restarts one controller.</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>delete</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Removes the controller and its saved configuration.</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code>.</td></tr>
  </tbody>
</table>

Set `All` to `true` with `start`, `stop`, or `restart` to operate on every controller. A successful all-tunnels response contains `status` and a `results` list returned by the controller group.

#### Supported Tunnel Types

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Category</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Types</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Client</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>client</code>, <code>httpclient</code>, <code>ircclient</code>, <code>socks</code>, <code>socksirc</code>, <code>connectclient</code>, <code>streamrclient</code></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Server</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>server</code>, <code>httpserver</code>, <code>httpbidirserver</code>, <code>ircserver</code>, <code>streamrserver</code></td></tr>
  </tbody>
</table>

#### Create and Edit Parameters

`Type` is required for `create` and ignored for `edit`, which retains the existing controller type.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Tunnel Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Required Configuration</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>client</code>, <code>ircclient</code>, <code>streamrclient</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Port</code> and <code>TargetDestination</code> or <code>Destination</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Connects the local port to a fixed I2P Destination.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>httpclient</code>, <code>socks</code>, <code>socksirc</code>, <code>connectclient</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Port</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">The request or proxy protocol selects the remote destination.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>server</code>, <code>httpserver</code>, <code>ircserver</code>, <code>streamrserver</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TargetPort</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TargetHost</code> defaults to <code>127.0.0.1</code> where applicable.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>httpbidirserver</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TargetPort</code> and <code>Port</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Uses both a service target port and a local bidirectional client port.</td></tr>
  </tbody>
</table>

An `edit` request is not a sparse patch. Supply the complete desired managed configuration. Required ports and destinations must be supplied again, and omitted boolean options may be reset to `false`.

##### Common Parameters

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameter</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type / Range</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Type</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Required for <code>create</code>. Must be one of the supported tunnel types.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>NewName</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Optional new name during <code>edit</code>. The trimmed name must be non-empty and unique.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Port</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">integer, 1–65535</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Local listen port for client and bidirectional HTTP server tunnels.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TargetHost</code> or <code>Host</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Local target host for server tunnels. <code>TargetHost</code> takes precedence.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TargetPort</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">integer, 1–65535</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Local target port for server tunnels.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TargetDestination</code> or <code>Destination</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Fixed remote destination for applicable client types. <code>TargetDestination</code> takes precedence.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>StartOnLoad</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Starts a newly created controller in the background and starts it on future loads.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Description</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Human-readable tunnel description. Omit to remove the existing description during edit.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>ReachableBy</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Local listen interface. Applicable client tunnels default to <code>127.0.0.1</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Shared</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Shares an applicable client tunnel. Ignored for <code>streamrclient</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>UseSSL</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Enables SSL for supported tunnel types.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TunnelLength</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">integer, 0–3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Inbound and outbound tunnel length.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TunnelVariance</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">integer, -2–2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Inbound and outbound tunnel-length variance.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TunnelQuantity</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">integer, 1–6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Inbound and outbound tunnel quantity.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>TunnelBackupQuantity</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">integer, 0–3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Inbound and outbound backup-tunnel quantity.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>SigType</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Signing type name or code. Invalid or unavailable values fall back to the preferred type.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>EncType</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">LeaseSet encryption type or comma-separated types.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>CustomOptions</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Additional comma- or whitespace-separated <code>key=value</code> options. Managed fields cannot be overridden.</td></tr>
  </tbody>
</table>

##### Additional Option Groups

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Group</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Client management</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>ConnectDelay</code>, <code>Profile</code>, <code>DelayOpen</code>, <code>Reduce</code>, <code>ReduceCount</code> (0–9), <code>ReduceTime</code> (0–9999 minutes), <code>Close</code>, <code>CloseTime</code> (0–9999 minutes), <code>NewDest</code>, <code>PersistentClientKey</code>, <code>PrivKeyFile</code></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Client proxy</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>ProxyList</code>, <code>UseOutproxyPlugin</code>, <code>ProxyAuth</code>, <code>ProxyUsername</code>, <code>ProxyPassword</code>, <code>OutproxyAuth</code>, <code>OutproxyUsername</code>, <code>OutproxyPassword</code>, <code>OutproxyType</code>, <code>SSLProxies</code>, <code>JumpList</code></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Client filtering</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>AllowUserAgent</code>, <code>AllowReferer</code>, <code>AllowAccept</code>, <code>AllowInternalSSL</code>, <code>DCC</code>/<code>EnableDCC</code></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Server access</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>WebsiteHostname</code>/<code>SpoofedHost</code>, <code>BlockAccessInProxies</code>, <code>BlockUserAgents</code>, <code>UserAgents</code>, <code>BlockReferers</code>, <code>UniqueLocalAddressPerClient</code>, <code>MultiHoming</code>, <code>AccessOption</code>, <code>AccessList</code>, <code>FilterFilePath</code></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Server limits</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>MaxConcurrentConns</code>, <code>ClientPerMinute</code>, <code>ClientPerHour</code>, <code>ClientPerDay</code>, <code>TotalInPerMinute</code>, <code>TotalInPerHour</code>, <code>TotalInPerDay</code>, <code>PostLimit</code>, <code>PostLimitTime</code>, <code>PerClientPeriod</code>, <code>TotalPeriod</code>, <code>TotalBanTime</code> (all 0–100000)</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Encrypted LeaseSet</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>EncryptLeaseSet</code>, <code>OptionalLookup</code>, <code>LeaseSetClientAuths</code></td></tr>
  </tbody>
</table>

- `NewDest: 1` creates a new Destination when a supported client resumes; `NewDest: 2` enables a persistent client key. `PersistentClientKey: true` is equivalent to mode `2` where supported.
- When enabling `ProxyAuth` for a new configuration, both `ProxyUsername` and `ProxyPassword` are required. `OutproxyAuth` uses `OutproxyUsername` and `OutproxyPassword`.
- `OutproxyType` applies to SOCKS client types. `SSLProxies` and `JumpList` apply to HTTP clients. `DCC` applies to IRC clients.
- `AccessOption: "allow"` enables an allowlist and `AccessOption: "deny"` enables a denylist. `AccessList` supplies the comma- or newline-separated entries.

`EncryptLeaseSet` accepts `disable`, `encrypted (aes)`, `blinded`, `blinded with lookup password`, `encrypted (psk)`, `encrypted with lookup password (psk)`, `encrypted with per-user key (psk)`, `encrypted with lookup password and per-user key (psk)`, `encrypted with per-user key (dh)`, or `encrypted with lookup password and per-user key (dh)`. `LeaseSetClientAuths` is a list of objects containing `Name` and a Base64 `Key` that decodes to 32 bytes.

#### Request Example

```json
{
  "jsonrpc": "2.0",
  "id": "11",
  "method": "TunnelManager",
  "params": {
    "Token": "a1b2c3d4e5",
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7666,
    "TargetDestination": "example.i2p",
    "StartOnLoad": false
  }
}
```

```json
{
  "jsonrpc": "2.0",
  "id": "11",
  "result": {
    "status": "success - created tunnel example-client",
    "results": []
  }
}
```

`results` contains controller messages generated during creation and may be empty.

#### Get Response

```json
{
  "jsonrpc": "2.0",
  "id": "12",
  "method": "TunnelManager",
  "params": {
    "Token": "a1b2c3d4e5",
    "Name": "example-client",
    "Action": "get"
  }
}
```

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Info Field</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>client</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Whether this is a client controller.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>status</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>running</code>, <code>standby</code>, or <code>stopped</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>persistentClientKey</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Whether the controller uses a persistent client key.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>offlineKeys</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">boolean</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Whether the controller uses offline signing keys.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>targetDestination</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String or null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Configured remote destination for a client tunnel.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localDestination</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String or null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Full local Base64 Destination, read from the live controller or private-key file.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>destination</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String or null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alias of <code>localDestination</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>destinationB32</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">String or null</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Base32 hostname for the local Destination.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>rawConfig</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Map&lt;String, String&gt;</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Complete saved controller configuration.</td></tr>
  </tbody>
</table>

```json
{
  "jsonrpc": "2.0",
  "id": "12",
  "result": {
    "status": "success - options for example-client",
    "info": {
      "client": true,
      "status": "stopped",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "example.i2p",
      "localDestination": null,
      "destination": null,
      "destinationB32": null,
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  }
}
```

Destination fields may be null when the controller has no live Destination and no readable private-key file.

> `rawConfig` may contain sensitive tunnel configuration. Do not expose a `get` response to untrusted clients.

#### Start, Stop, Restart, and Delete

These actions require only `Token`, `Name`, and `Action`:

```json
{
  "jsonrpc": "2.0",
  "id": "13",
  "method": "TunnelManager",
  "params": {
    "Token": "a1b2c3d4e5",
    "Name": "example-client",
    "Action": "start"
  }
}
```

The corresponding success messages are `success - starting tunnel NAME`, `success - stopping tunnel NAME`, `success - restarting tunnel NAME`, and `success - deleting tunnel - NAME`.

To restart every controller:

```json
{
  "jsonrpc": "2.0",
  "id": "14",
  "method": "TunnelManager",
  "params": {
    "Token": "a1b2c3d4e5",
    "Name": "unused",
    "Action": "restart",
    "All": true
  }
}
```

Operational failures, such as an unknown action, duplicate name, missing tunnel, or invalid option range, are generally returned in a successful JSON-RPC response with a `result.status` beginning with `error -`. Missing required top-level parameters and authentication failures use the JSON-RPC `error` object.

---

## 5. Error Codes

### Standard JSON-RPC2 Error Codes

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32700</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">JSON parse error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32600</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Invalid request</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32601</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Method not found</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32602</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Invalid parameters</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32603</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Internal error</td>
    </tr>
  </tbody>
</table>

### I2PControl Specific Error Codes

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32001</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Invalid password provided</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32002</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">No authentication token presented</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32003</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Authentication token doesn't exist</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32004</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The provided authentication token was expired and will be removed</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32005</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The version of the I2PControl API used wasn't specified, but is required to be specified</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-32006</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The version of the I2PControl API specified is not supported by I2PControl</td>
    </tr>
  </tbody>
</table>

---

## 6. Usage & Best Practices

- Always include the `Token` parameter (except when authenticating).  
- Change the default password (`itoopie`) upon first use.  
- For Java I2P, ensure the I2PControl webapp is enabled via WebApps.  
- Be prepared for slight variations: some fields may be numbers or strings, depending on I2P version.  
- Wrap long status strings for display-friendly output.

---

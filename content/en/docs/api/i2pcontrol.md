---
title: "I2PControl JSON-RPC"
description: "Remote router management API via the I2PControl webapp"
slug: "i2pcontrol"
lastUpdated: "2026-07-10"
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

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Field</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Direction</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>API</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">I2PControl API version requested by the client. Use <code>1</code>.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Password</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Password used to authenticate with I2PControl.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>API</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Primary API version implemented by the server.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Token</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">String</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Authentication token used for subsequent requests.</td></tr>
  </tbody>
</table>

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
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.status</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Network status code; see the table below.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.inbound.1s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Current inbound bandwidth in bytes per second.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.inbound.15s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15-second average inbound bandwidth in bytes per second.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.outbound.1s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Current outbound bandwidth in bytes per second.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.bw.outbound.15s</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">double</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15-second average outbound bandwidth in bytes per second.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;"><code>i2p.router.net.tunnels.participating</code></td><td style="border:1px solid var(--color-border); padding:0.6rem;">long</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Number of tunnels in which this router is participating.</td></tr>
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
  </tbody>
</table>

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

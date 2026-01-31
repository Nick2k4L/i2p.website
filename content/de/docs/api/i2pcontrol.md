---
title: "I2PControl JSON-RPC"
description: "Remote Router-Verwaltungs-API über die I2PControl-Webapp"
slug: "i2pcontrol"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
reviewStatus: "needs-review"
---

-------------check add stuff--------------

# I2PControl API Dokumentation

I2PControl ist eine **JSON-RPC 2.0** API, die mit dem I2P router (seit Version 0.9.39) mitgeliefert wird. Sie ermöglicht die authentifizierte Überwachung und Steuerung des routers über strukturierte JSON-Anfragen.

> **Standardpasswort:** `itoopie` — dies ist die Werkseinstellung und **sollte sofort geändert werden** aus Sicherheitsgründen.

---

## 1. Übersicht & Zugriff

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
Im Fall von Java I2P müssen Sie zu **Router Console → WebApps → I2PControl** gehen und es aktivieren (auf automatischen Start setzen). Sobald es aktiv ist, erfordern alle Methoden, dass Sie sich zuerst authentifizieren und ein Sitzungstoken erhalten.

---

## 2. JSON-RPC Format

Alle Anfragen folgen der JSON-RPC 2.0 Struktur:

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
Eine erfolgreiche Antwort enthält ein `result`-Feld; bei einem Fehler wird ein `error`-Objekt zurückgegeben:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": { /* data */ }
}
```
oder

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

## 3. Authentifizierungsablauf

### Anfrage (Authentifizieren)

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
### Erfolgreiche Antwort

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
Sie müssen diesen `Token` in allen nachfolgenden Anfragen in den `params` einschließen.

---

## 4. Methoden & Endpunkte

### 4.1 RouterInfo

Ruft wichtige Telemetriedaten über den router ab.

**Anfrage-Beispiel**

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
**Antwortfelder (result)**   Laut der offiziellen Dokumentation (GetI2P):   - `i2p.router.status` (String) — ein für Menschen lesbarer Status   - `i2p.router.uptime` (long) — Millisekunden (oder String für ältere i2pd-Versionen) :contentReference[oaicite:0]{index=0}   - `i2p.router.version` (String) — Versionszeichenkette :contentReference[oaicite:1]{index=1}   - `i2p.router.net.bw.inbound.1s`, `i2p.router.net.bw.inbound.15s` (double) — eingehende Bandbreite in B/s :contentReference[oaicite:2]{index=2}   - `i2p.router.net.bw.outbound.1s`, `i2p.router.net.bw.outbound.15s` (double) — ausgehende Bandbreite in B/s :contentReference[oaicite:3]{index=3}   - `i2p.router.net.status` (long) — numerischer Statuscode (siehe Enum unten) :contentReference[oaicite:4]{index=4}   - `i2p.router.net.tunnels.participating` (long) — Anzahl der teilnehmenden tunnel :contentReference[oaicite:5]{index=5}   - `i2p.router.netdb.activepeers`, `fastpeers`, `highcapacitypeers` (long) — netDB Peer-Statistiken :contentReference[oaicite:6]{index=6}   - `i2p.router.netdb.isreseeding` (boolean) — ob Reseed aktiv ist :contentReference[oaicite:7]{index=7}   - `i2p.router.netdb.knownpeers` (long) — insgesamt bekannte Peers :contentReference[oaicite:8]{index=8}

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
---

### 4.2 GetRate

Wird verwendet, um Ratenmetriken (z.B. Bandbreite, tunnel-Erfolg) über ein bestimmtes Zeitfenster abzurufen.

**Anfrage-Beispiel**

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
**Beispielantwort**

```json
{
  "jsonrpc": "2.0",
  "id": "3",
  "result": {
    "Rate": 12345.67
  }
}
```
---

### 4.3 RouterManager

Administrative Aktionen durchführen.

**Erlaubte Parameter / Methoden**   - `Restart`, `RestartGraceful`   - `Shutdown`, `ShutdownGraceful`   - `Reseed`, `FindUpdates`, `Update` :contentReference[oaicite:10]{index=10}

**Anfrage-Beispiel**

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
**Erfolgreiche Antwort**

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

Netzwerkkonfigurationsparameter abrufen oder festlegen (Ports, UPnP, Bandbreitenanteil, etc.)

**Anfrage-Beispiel (aktuelle Werte abrufen)**

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
**Beispielantwort**

```json
{
  "jsonrpc": "2.0",
  "id": "5",
  "result": {
    "i2p.router.net.ntcp.port": "1234",
    "i2p.router.net.ssu.port": "5678",
    "i2p.router.net.bw.share": "50",
    "i2p.router.net.upnp": "true",
    "SettingsSaved": true,
    "RestartNeeded": false
  }
}
```
> Hinweis: i2pd-Versionen vor 2.41 können numerische Typen anstelle von Strings zurückgeben — Clients sollten beide verarbeiten können. :contentReference[oaicite:11]{index=11}

---

### 4.5 Erweiterte Einstellungen

Ermöglicht die Manipulation interner router-Parameter.

**Anfrage-Beispiel**

```bash
curl -s -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": "6",
        "method": "AdvancedSettings",
        "params": {
          "Token": "a1b2c3d4e5",
          "Set": {
            "router.sharePercentage": "75",
            "i2np.flushInterval": "6000"
          }
        }
      }' \
  http://127.0.0.1:7657/jsonrpc/
```
**Antwort-Beispiel**

```json
{
  "jsonrpc": "2.0",
  "id": "6",
  "result": {
    "Set": {
      "router.sharePercentage": "75",
      "i2np.flushInterval": "6000"
    }
  }
}
```
---

## 5. Fehlercodes

### Standard JSON-RPC2 Fehlercodes

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
### I2PControl spezifische Fehlercodes

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

## 6. Verwendung und bewährte Praktiken

- Fügen Sie immer den `Token`-Parameter hinzu (außer bei der Authentifizierung).
- Ändern Sie das Standardpasswort (`itoopie`) bei der ersten Verwendung.
- Stellen Sie bei Java I2P sicher, dass die I2PControl-Webapp über WebApps aktiviert ist.
- Seien Sie auf geringfügige Abweichungen vorbereitet: einige Felder können je nach I2P-Version Zahlen oder Strings sein.
- Umbrechen Sie lange Status-Strings für eine anzeigefreundliche Ausgabe.

---

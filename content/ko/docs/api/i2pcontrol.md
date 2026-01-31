---
title: "I2PControl JSON-RPC"
description: "I2PControl 웹앱을 통한 원격 router 관리 API"
slug: "i2pcontrol"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
reviewStatus: "needs-review"
---

-------------확인 추가 사항--------------

# I2PControl API 문서

I2PControl은 I2P router와 함께 번들로 제공되는 **JSON-RPC 2.0** API입니다 (버전 0.9.39부터). 구조화된 JSON 요청을 통해 router의 인증된 모니터링 및 제어를 가능하게 합니다.

> **기본 비밀번호:** `itoopie` — 이는 공장 기본값이며 보안을 위해 **즉시 변경해야 합니다**.

---

## 1. 개요 및 접근

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
Java I2P의 경우, **Router Console → WebApps → I2PControl**로 이동하여 활성화해야 합니다(자동으로 시작하도록 설정). 활성화되면 모든 메서드는 먼저 인증하고 세션 토큰을 받아야 합니다.

---

## 2. JSON-RPC 형식

모든 요청은 JSON-RPC 2.0 구조를 따릅니다:

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
성공적인 응답에는 `result` 필드가 포함되고, 실패 시에는 `error` 객체가 반환됩니다:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": { /* data */ }
}
```
또는

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

## 3. 인증 플로우

### 요청 (인증)

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
### 성공적인 응답

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
이후의 모든 요청에서 해당 `Token`을 `params`에 포함해야 합니다.

---

## 4. 메소드 및 엔드포인트

### 4.1 RouterInfo

router에 대한 주요 원격 측정 데이터를 가져옵니다.

**요청 예제**

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
**응답 필드 (result)**   공식 문서(GetI2P)에 따르면:   - `i2p.router.status` (String) — 사람이 읽을 수 있는 상태   - `i2p.router.uptime` (long) — 밀리초 (또는 이전 i2pd의 경우 문자열) :contentReference[oaicite:0]{index=0}   - `i2p.router.version` (String) — 버전 문자열 :contentReference[oaicite:1]{index=1}   - `i2p.router.net.bw.inbound.1s`, `i2p.router.net.bw.inbound.15s` (double) — B/s 단위의 인바운드 대역폭 :contentReference[oaicite:2]{index=2}   - `i2p.router.net.bw.outbound.1s`, `i2p.router.net.bw.outbound.15s` (double) — B/s 단위의 아웃바운드 대역폭 :contentReference[oaicite:3]{index=3}   - `i2p.router.net.status` (long) — 숫자 상태 코드 (아래 enum 참조) :contentReference[oaicite:4]{index=4}   - `i2p.router.net.tunnels.participating` (long) — 참여 중인 tunnel 수 :contentReference[oaicite:5]{index=5}   - `i2p.router.netdb.activepeers`, `fastpeers`, `highcapacitypeers` (long) — netDB 피어 통계 :contentReference[oaicite:6]{index=6}   - `i2p.router.netdb.isreseeding` (boolean) — reseed가 활성화되어 있는지 여부 :contentReference[oaicite:7]{index=7}   - `i2p.router.netdb.knownpeers` (long) — 알려진 총 피어 수 :contentReference[oaicite:8]{index=8}

#### 상태 코드 열거형 (`i2p.router.net.status`)

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

주어진 시간 창에서 속도 메트릭(예: 대역폭, tunnel 성공률)을 가져오는 데 사용됩니다.

**요청 예제**

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
**샘플 응답**

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

관리 작업을 수행합니다.

**허용되는 매개변수 / 메소드**   - `Restart`, `RestartGraceful`   - `Shutdown`, `ShutdownGraceful`   - `Reseed`, `FindUpdates`, `Update` :contentReference[oaicite:10]{index=10}

**요청 예시**

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
**성공적인 응답**

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

네트워크 구성 매개변수(포트, upnp, 대역폭 공유 등)를 가져오거나 설정합니다

**요청 예시 (현재 값 가져오기)**

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
**샘플 응답**

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
> 참고: 2.41 이전 버전의 i2pd는 문자열 대신 숫자 타입을 반환할 수 있습니다 — 클라이언트는 두 가지 모두를 처리해야 합니다. :contentReference[oaicite:11]{index=11}

---

### 4.5 고급 설정

내부 router 매개변수를 조작할 수 있게 합니다.

**요청 예시**

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
**응답 예제**

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

## 5. 오류 코드

### 표준 JSON-RPC2 오류 코드

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
### I2PControl 특정 오류 코드

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

## 6. 사용법 및 모범 사례

- 인증 시를 제외하고 항상 `Token` 매개변수를 포함하세요.
- 첫 사용 시 기본 비밀번호(`itoopie`)를 변경하세요.
- Java I2P의 경우, WebApps를 통해 I2PControl webapp이 활성화되어 있는지 확인하세요.
- 약간의 차이에 대비하세요: I2P 버전에 따라 일부 필드가 숫자 또는 문자열일 수 있습니다.
- 표시 친화적 출력을 위해 긴 상태 문자열을 줄바꿈하세요.

---

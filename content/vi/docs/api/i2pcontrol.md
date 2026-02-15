---
title: "I2PControl JSON-RPC"
description: "API quản lý router từ xa thông qua webapp I2PControl"
slug: "i2pcontrol"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
reviewStatus: "needs-review"
---

-------------kiểm tra thêm nội dung--------------

# Tài liệu API I2PControl

I2PControl là một API **JSON-RPC 2.0** được tích hợp sẵn với I2P router (từ phiên bản 0.9.39). Nó cho phép giám sát và điều khiển router đã được xác thực thông qua các yêu cầu JSON có cấu trúc.

> **Mật khẩu mặc định:** `itoopie` — đây là mật khẩu gốc từ nhà máy và **nên được thay đổi** ngay lập tức để đảm bảo bảo mật.

---

## 1. Tổng quan & Truy cập

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
Trong trường hợp Java I2P, bạn phải vào **Router Console → WebApps → I2PControl** và bật nó (đặt khởi động tự động). Khi đã hoạt động, tất cả các phương thức đều yêu cầu bạn phải xác thực trước và nhận token phiên.

---

## 2. Định dạng JSON-RPC

Tất cả các yêu cầu đều tuân theo cấu trúc JSON-RPC 2.0:

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
Một phản hồi thành công bao gồm trường `result`; khi thất bại, một đối tượng `error` sẽ được trả về:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": { /* data */ }
}
```
hoặc

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

## 3. Luồng Xác thực

### Yêu cầu (Xác thực)

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
  `http://127.0.0.1:7657/jsonrpc/`
```
### Phản hồi thành công

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
Bạn phải bao gồm `Token` đó trong tất cả các yêu cầu tiếp theo trong `params`.

---

## 4. Phương thức & Điểm cuối

### 4.1 RouterInfo

Lấy dữ liệu telemetry chính về router.

**Ví dụ Yêu cầu**

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
  `http://127.0.0.1:7657/jsonrpc/`
```
**Các Trường Phản Hồi (result)** Theo tài liệu chính thức (GetI2P): - `i2p.router.status` (String) — trạng thái có thể đọc được - `i2p.router.uptime` (long) — mili giây (hoặc chuỗi cho i2pd cũ hơn) :contentReference[oaicite:0]{index=0} - `i2p.router.version` (String) — chuỗi phiên bản :contentReference[oaicite:1]{index=1} - `i2p.router.net.bw.inbound.1s`, `i2p.router.net.bw.inbound.15s` (double) — băng thông đến theo B/s :contentReference[oaicite:2]{index=2} - `i2p.router.net.bw.outbound.1s`, `i2p.router.net.bw.outbound.15s` (double) — băng thông đi theo B/s :contentReference[oaicite:3]{index=3} - `i2p.router.net.status` (long) — mã trạng thái số (xem enum bên dưới) :contentReference[oaicite:4]{index=4} - `i2p.router.net.tunnels.participating` (long) — số lượng tunnel tham gia :contentReference[oaicite:5]{index=5} - `i2p.router.netdb.activepeers`, `fastpeers`, `highcapacitypeers` (long) — thống kê peer của netDB :contentReference[oaicite:6]{index=6} - `i2p.router.netdb.isreseeding` (boolean) — có đang thực hiện reseed hay không :contentReference[oaicite:7]{index=7} - `i2p.router.netdb.knownpeers` (long) — tổng số peer đã biết :contentReference[oaicite:8]{index=8}

#### Enum Mã Trạng Thái (`i2p.router.net.status`)

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

Được sử dụng để lấy các chỉ số tốc độ (ví dụ: băng thông, tỷ lệ thành công tunnel) trong một khoảng thời gian nhất định.

**Ví dụ Yêu cầu**

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
  `http://127.0.0.1:7657/jsonrpc/`
```
**Phản hồi mẫu**

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

Thực hiện các hành động quản trị.

**Các tham số / phương thức được phép**   - `Restart`, `RestartGraceful`   - `Shutdown`, `ShutdownGraceful`   - `Reseed`, `FindUpdates`, `Update` :contentReference[oaicite:10]{index=10}

**Ví dụ Request**

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
  `http://127.0.0.1:7657/jsonrpc/`
```
**Phản hồi thành công**

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

Lấy hoặc thiết lập các tham số cấu hình mạng (cổng, upnp, chia sẻ băng thông, v.v.)

**Ví dụ Request (lấy giá trị hiện tại)**

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
  `http://127.0.0.1:7657/jsonrpc/`
```
**Phản Hồi Mẫu**

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
> Lưu ý: các phiên bản i2pd trước 2.41 có thể trả về các kiểu số thay vì chuỗi — client nên xử lý cả hai. :contentReference[oaicite:11]{index=11}

---

### 4.5 Cài đặt Nâng cao

Cho phép thao tác các tham số bên trong router.

**Ví dụ Yêu cầu**

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
  `http://127.0.0.1:7657/jsonrpc/`
```
**Ví dụ Phản hồi**

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

## 5. Mã Lỗi

### Mã Lỗi Chuẩn JSON-RPC2

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
### Mã Lỗi Cụ Thể của I2PControl

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

## 6. Sử dụng & Các phương pháp tốt nhất

- Luôn bao gồm tham số `Token` (trừ khi đang xác thực).  
- Thay đổi mật khẩu mặc định (`itoopie`) khi sử dụng lần đầu.  
- Đối với Java I2P, đảm bảo webapp I2PControl được kích hoạt qua WebApps.  
- Chuẩn bị cho những biến đổi nhỏ: một số trường có thể là số hoặc chuỗi, tùy thuộc vào phiên bản I2P.  
- Ngắt dòng các chuỗi trạng thái dài để hiển thị thân thiện hơn.

---

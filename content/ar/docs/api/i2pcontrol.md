---
title: "I2PControl JSON-RPC"
description: "واجهة برمجة تطبيقات إدارة router عن بُعد عبر تطبيق I2PControl الويب"
slug: "i2pcontrol"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
reviewStatus: "needs-review"
---

-------------تحقق من إضافة الأشياء--------------

# توثيق واجهة برمجة التطبيقات I2PControl

I2PControl هو واجهة برمجة تطبيقات **JSON-RPC 2.0** مدمجة مع router I2P (منذ الإصدار 0.9.39). يمكّن من المراقبة والتحكم المصادق عليه في router عبر طلبات JSON منظمة.

> **كلمة المرور الافتراضية:** `itoopie` — هذه هي القيمة الافتراضية من المصنع و**يجب تغييرها** فوراً لأغراض الأمان.

---

## 1. نظرة عامة والوصول

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
في حالة Java I2P، يجب أن تذهب إلى **Router Console → WebApps → I2PControl** وتفعيله (اضبطه للبدء تلقائياً). بمجرد تنشيطه، تتطلب جميع الطرق أن تقوم أولاً بالمصادقة وتلقي رمز الجلسة.

---

## 2. تنسيق JSON-RPC

جميع الطلبات تتبع بنية JSON-RPC 2.0:

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
تتضمن الاستجابة الناجحة حقل `result`؛ وفي حالة الفشل، يتم إرجاع كائن `error`:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": { /* data */ }
}
```
أو

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

## 3. تدفق المصادقة

### طلب (المصادقة)

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
### استجابة ناجحة

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
يجب أن تتضمن هذا `Token` في جميع الطلبات اللاحقة ضمن `params`.

---

## 4. الطرق والنقاط النهائية

### 4.1 معلومات الموجه (RouterInfo)

يجلب بيانات القياس الرئيسية حول الـ router.

**مثال على الطلب**

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
**حقول الاستجابة (result)**   وفقاً للوثائق الرسمية (GetI2P):   - `i2p.router.status` (String) — حالة قابلة للقراءة البشرية   - `i2p.router.uptime` (long) — بالميلي ثانية (أو نص لإصدارات i2pd الأقدم) :contentReference[oaicite:0]{index=0}   - `i2p.router.version` (String) — نص الإصدار :contentReference[oaicite:1]{index=1}   - `i2p.router.net.bw.inbound.1s`, `i2p.router.net.bw.inbound.15s` (double) — عرض النطاق الداخل بوحدة B/s :contentReference[oaicite:2]{index=2}   - `i2p.router.net.bw.outbound.1s`, `i2p.router.net.bw.outbound.15s` (double) — عرض النطاق الخارج بوحدة B/s :contentReference[oaicite:3]{index=3}   - `i2p.router.net.status` (long) — رمز الحالة الرقمي (انظر التعداد أدناه) :contentReference[oaicite:4]{index=4}   - `i2p.router.net.tunnels.participating` (long) — عدد الأنفاق المشاركة :contentReference[oaicite:5]{index=5}   - `i2p.router.netdb.activepeers`, `fastpeers`, `highcapacitypeers` (long) — إحصائيات النظراء في netDB :contentReference[oaicite:6]{index=6}   - `i2p.router.netdb.isreseeding` (boolean) — ما إذا كانت إعادة البذر نشطة :contentReference[oaicite:7]{index=7}   - `i2p.router.netdb.knownpeers` (long) — إجمالي النظراء المعروفين :contentReference[oaicite:8]{index=8}

#### تعداد رمز الحالة (`i2p.router.net.status`)

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

يُستخدم لجلب مقاييس المعدل (مثل عرض النطاق الترددي، نجاح tunnel) خلال إطار زمني محدد.

**مثال على الطلب**

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
**استجابة نموذجية**

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

تنفيذ الإجراءات الإدارية.

**المعاملات / الطرق المسموحة**   - `Restart`, `RestartGraceful`   - `Shutdown`, `ShutdownGraceful`   - `Reseed`, `FindUpdates`, `Update` :contentReference[oaicite:10]{index=10}

**مثال على الطلب**

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
**الاستجابة الناجحة**

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

الحصول على أو تعيين معاملات تكوين الشبكة (المنافذ، upnp، مشاركة عرض النطاق الترددي، إلخ)

**مثال على الطلب (الحصول على القيم الحالية)**

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
**نموذج الاستجابة**

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
> ملاحظة: إصدارات i2pd السابقة للإصدار 2.41 قد ترجع أنواع رقمية بدلاً من النصوص — يجب على العملاء التعامل مع كلا النوعين. :contentReference[oaicite:11]{index=11}

---

### 4.5 الإعدادات المتقدمة

يسمح بالتلاعب في معاملات router الداخلية.

**مثال على الطلب**

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
**مثال على الاستجابة**

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

## 5. رموز الخطأ

### رموز أخطاء JSON-RPC2 المعيارية

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
### رموز الأخطاء الخاصة بـ I2PControl

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

## 6. الاستخدام وأفضل الممارسات

- قم دائماً بتضمين معامل `Token` (عدا عند المصادقة).
- غيّر كلمة المرور الافتراضية (`itoopie`) عند الاستخدام الأول.
- لـ Java I2P، تأكد من تمكين تطبيق I2PControl عبر WebApps.
- كن مستعداً لاختلافات طفيفة: قد تكون بعض الحقول أرقاماً أو نصوصاً، حسب إصدار I2P.
- قم بلف سلاسل الحالة الطويلة للحصول على مخرجات سهلة القراءة.

---

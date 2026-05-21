---
title: "i2pcontrol-expansion"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "افتح"
toc: true
---

نظرة عامة ========

يُقدِّم هذا الاقتراح معلومات جديدة إلى واجهة برمجة تطبيقات i2pcontrol، مما يتيح مرونة أكبر. تشمل هذه المعلومات: إضافة وحذف واسترجاع وتعديل دفاتر العناوين والخدمات المخفية. كما يُقدِّم هذا الاقتراح مزيدًا من المعلومات حول جهاز التوجيه الخاص بك، مثل الأقران (peers) والأخبار (news) وقاعدة البيانات الشبكية (netdb) والمزيد.

الدافع ==========

السبب وراء هذا الاقتراح هو السماح بمرونة أكبر في واجهة برمجة تطبيقات I2P (API) لتمكين التطبيقات من تنفيذ واجهة إدارية لـ I2P وإدارتها. إن عرض مثل هذه المعلومات على i2pcontrol يتيح للمستخدمين إنشاء تطبيقات أكثر تقدماً وتقديم دعم أفضل للإدارة عن بُعد.

التصميم ======

عندما يتفاعل المستخدمون مع واجهة برمجة تطبيقات i2pcontrol، سيكونون قادرين على الوصول إلى نقاط نهاية جديدة توفر المعلومات المذكورة أعلاه. على سبيل المثال، ستُعرض عبر واجهة برمجة تطبيقات i2pcontrol طرق جديدة هي `TunnelManager` و`AddressBook` التي تسمح للمستخدمين بإدخال معلمات لإنشاء النفق وحذفه واسترجاعه وتعديله، وكذلك دفاتر العناوين. بالإضافة إلى ذلك، ستتضمن الطريقة الموجودة مسبقًا `RouterInfo` معلمات جديدة لعرض معلومات حول الراوتر.

الآثار الأمنية =====================

لا توجد تداعيات أمنية إضافية متوقعة من هذا الاقتراح، لأن المعلومات التي يتم الكشف عنها يمكن الوصول إليها بالفعل من خلال وسائل أخرى. ومع ذلك، من المهم التأكد من وجود آليات مصادقة وتفويض مناسبة للوصول إلى واجهة برمجة تطبيقات i2pcontrol، لمنع الوصول غير المصرح به إلى المعلومات الحساسة أو التحكم في الموجه.

مواصفات واجهة برمجة التطبيقات (API) والأساليب ===========================

جميع الطلبات تتبع هيكل JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
الطريقة - RouterInfo -------------------

أدناه توجد المعاملات الجديدة لطريقة `RouterInfo` وما تُرجعه:

- `i2p.router.news` - يُرجع جميع إدخالات أخبار الموجه.
- `i2p.router.id` - يُرجع تجزئة الموجه كسلسلة Base64، أو `null`.
- `i2p.router.clockskew` - يُرجع متوسط الانحراف الزمني للنُدُد، أو `null`.
- `i2p.router.info` - يُرجع معلومات الموجه (RouterInfo) بشكل تسلسلي كسلسلة Base64، أو `null`.
- `i2p.router.logs` - يُرجع رسائل السجل الحديثة للموجه.
- `i2p.router.logs.clear` - يمسح ذاكرة التخزين المؤقت لسجل الموجه ويعيد `"success"`.

- `i2p.router.net.total.received.bytes` - يُرجع إجمالي البايتات المستلمة منذ بدء التشغيل. *(مُعتمد من i2pd)*
- `i2p.router.net.total.sent.bytes` - يُرجع إجمالي البايتات المرسلة منذ بدء التشغيل. *(مُعتمد من i2pd)*
- `i2p.router.net.total.transit.bytes` - يُرجع إجمالي البايتات العابرة (التي تم توجيهها) منذ بدء التشغيل. *(مُعتمد من i2pd)*
- `i2p.router.net.bw.transit.15s` - يُرجع متوسط عرض النطاق الترددي العابر على مدى 15 ثانية (بايت/ثانية). *(مُعتمد من i2pd)*

- `i2p.router.net.tunnels.shareratio` - يُرجع نسبة مشاركة النفق.
- `i2p.router.net.tunnels.participating.info` - يُرجع معلومات النفق المشاركة.
- `i2p.router.net.tunnels.i2ptunnel` - يُرجع معلومات وحدة تحكم I2PTunnel المُعدة (إحصائيات سريعة للجميع).
- `i2p.router.net.tunnels.exploratory.inbound` - يُرجع عدد النفق الاستكشافي الوارد.
- `i2p.router.net.tunnels.exploratory.outbound` - يُرجع عدد النفق الاستكشافي الصادر.
- `i2p.router.net.tunnels.exploratory.info.list` - يُرجع قائمة معلومات النفق الاستكشافي.
- `i2p.router.net.tunnels.client.inbound` - يُرجع عدد النفق العميل الوارد.
- `i2p.router.net.tunnels.client.outbound` - يُرجع عدد النفق العميل الصادر.
- `i2p.router.net.tunnels.client.info.list` - يُرجع قائمة معلومات نفق العميل.

- `i2p.router.net.status.v6` - يُرجع رمز حالة الشبكة IPv6. *(مُعتمد من i2pd)*
- `i2p.router.net.error` - يُرجع رمز خطأ الشبكة IPv4. *(مُعتمد من i2pd)*
- `i2p.router.net.error.v6` - يُرجع رمز خطأ الشبكة IPv6. *(مُعتمد من i2pd)*
- `i2p.router.net.testing` - يُرجع ما إذا كانت الشبكة IPv4 في حالة اختبار (0 أو 1). *(مُعتمد من i2pd)*
- `i2p.router.net.testing.v6` - يُرجع ما إذا كانت الشبكة IPv6 في حالة اختبار (0 أو 1). *(مُعتمد من i2pd)*

- `i2p.router.net.tunnels.successrate` - يُرجع معدل نجاح إنشاء النفق الحديث (%). *(مُعتمد من i2pd)*
- `i2p.router.net.tunnels.totalsuccessrate` - يُرجع معدل نجاح إنشاء النفق الكلي منذ التشغيل (%). *(مُعتمد من i2pd)*
- `i2p.router.net.tunnels.queue` - يُرجع حجم قائمة انتظار طلبات إنشاء النفق. *(مُعتمد من i2pd)*
- `i2p.router.net.tunnels.tbmqueue` - يُرجع حجم قائمة انتظار رسائل إنشاء النفق (Tunnel Build Message). *(مُعتمد من i2pd)*

- `i2p.router.netdb.peers` - يُرجع قائمة ببصمات الندود المعروفة.
- `i2p.router.netdb.activepeers.info` - يُرجع بيانات RouterInfo بشكل تسلسلي للندود النشطة.
- `i2p.router.netdb.ntcp.limit` - يُرجع حد اتصالات NTCP.
- `i2p.router.netdb.ssu.limit` - يُرجع حد اتصالات SSU.
- `i2p.router.netdb.bannedpeers` - يُرجع الندود المحظورة مع تفاصيل الحظر.
- `i2p.router.netdb.activepeers.list` - يُرجع بصمات الندود النشطة.
- `i2p.router.netdb.peers.list` - يُرجع بصمات الندود المعروفة.
- `i2p.router.netdb.peers.info` - يُرجع بيانات RouterInfo بشكل تسلسلي للندود المعروفة.
- `i2p.router.netdb.activepeers.stats` - يُرجع إحصائيات الندود النشطة.

- `i2p.router.addressbook.private.list` - يُرجع إدخالات دفتر العناوين الخاص.
- `i2p.router.addressbook.local.list` - يُرجع إدخالات دفتر العناوين المحلي.
- `i2p.router.addressbook.router.list` - يُرجع إدخالات دفتر عناوين الراوتر.
- `i2p.router.addressbook.published.list` - يُرجع إدخالات دفتر العناوين المنشورة.
- `i2p.router.addressbook.subscriptions` - يُرجع مسار ملف الاشتراكات والإدخالات.
- `i2p.router.addressbook.config` - يُرجع مسار ملف تهيئة دفتر العناوين والإدخالات.

مثال:

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
إرجاع:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
الطريقة - دفتر العناوين --------------------

بالنسبة لطريقة `AddressBook`، هناك حاجة إلى ثلاثة معلمات/وسائط لإزالة أو إضافة مدخلات إلى دفتر العناوين:

- `Type` - يتوافق مع نوع دفتر العناوين:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - يتوافق مع اسم المضيف أو اسم النطاق المرتبط بسجل دفتر العناوين.
- `Destination` - يتوافق مع الوجهة المرتبطة بسجل دفتر العناوين.
- `Delete` - هذا المعامل اختياري ويُستخدم لحذف سجل من دفتر العناوين. إذا لم يتم توفير هذا المعامل، فستقوم الطريقة بإضافة سجل جديد إلى دفتر العناوين.

مثال:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
لتحرير اشتراكات دفتر العناوين:

- `SetSubscriptions` - يتم استخدام هذا المعلمة لتعيين اشتراكات إدخال دفتر العناوين. وهي تأخذ قائمة من السلاسل كوسيلة إدخال.

مثال:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
لتحرير AddressBookConfig:

- `SetConfig` - تُستخدم هذه المعلمة لتعيين التهيئة لإدخال دفتر العناوين.

يأخذ كائن JSON كوسيلة إدخال، والذي يحتوي على إعدادات التهيئة.

معلمات التهيئة المتاحة/الشائعة:

- `subscriptions` - ملف يحتوي على قائمة عناوين URL للاشتراك.
- `update_delay` - فاصل التحديث بالساعات.
- `published_addressbook` - مسار دفتر العناوين المنشور.
- `router_addressbook` - مسار دفتر عناوين الراوتر.
- `local_addressbook` - مسار دفتر العناوين المحلي.
- `private_addressbook` - مسار دفتر العناوين الخاص.
- `proxy_port` - منفذ eepProxy.
- `proxy_host` - اسم المضيف لـ eepProxy.
- `should_publish` - ما إذا كان سيتم تحديث دفتر العناوين المنشور.
- `etags` - ملف يحتوي على etags لعناوين URL للاشتراك.
- `last_modified` - ملف يحتوي على الطوابع الزمنية لآخر تعديل لعناوين URL للاشتراك.
- `log` - مسار ملف السجل.
- `theme` - السمة.

مثال:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
الطريقة - TunnelManager --------

يُستخدم أسلوب `TunnelManager` لإنشاء وتحرير واسترداد وتشغيل وإيقاف وإعادة تشغيل وحذف وحدات تحكم I2PTunnel.

المعلمات المطلوبة:

- `Name` - اسم النفق. هذا هو معرّف النفق.
- `Action` - الإجراء الذي سيتم تنفيذه:
  - `create`
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

معلمات اختيارية:

- `All` - قيمة منطقية، تحدد ما إذا كان سيتم تطبيق الإجراء على جميع الأنفاق. هذا صحيح فقط للإجراءات `start` و`stop` و`restart`.

أنواع النفق المدعومة لـ `create`:

- `client`
- `httpclient`
- `ircclient`
- `socks`
- `socksirc`
- `connectclient`
- `streamrclient`

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

المعلمات الشائعة لإنشاء/تحرير الأنفاق:

- `Type` - نوع النفق. مطلوب لعملية `create`.
- `NewName` - اسم جديد اختياري عند التعديل.
- `Port` - منفذ الاستماع المحلي.
- `TargetHost` أو `Host` - المضيف الهدف لأنفاق الخادم.
- `TargetPort` - المنفذ الهدف لأنفاق الخادم.
- `TargetDestination` أو `Destination` - الوجهة لأنفاق العميل التي تتطلب واحدة.
- `StartOnLoad` - قيمة منطقية، تحدد ما إذا كان النفق يجب أن يبدأ عند التحميل.
- `Description` - وصف النفق.
- `ReachableBy` - الواجهة/العنوان الذي يستمع إليه النفق.
- `Shared` - قيمة منطقية، تحدد ما إذا كان نفق العميل يجب أن يكون مشتركًا.
- `UseSSL` - قيمة منطقية، لتفعيل SSL حيثما كان مدعومًا.
- `TunnelLength` - طول النفق، من `0` إلى `3`.
- `TunnelVariance` - تباين النفق، من `-2` إلى `2`.
- `TunnelQuantity` - كمية الأنفاق، من `1` إلى `6`.
- `TunnelBackupQuantity` - كمية الأنفاق الاحتياطية، من `0` إلى `3`.
- `SigType` - نوع مفتاح التوقيع.
- `EncType` - نوع التشفير.
- `CustomOptions` - خيارات نفق مخصصة.

خيارات وكيل العميل:

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

خيارات إدارة العميل:

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

خيارات تصفية عميل HTTP:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

خيارات الخادم:

- `WebsiteHostname` أو `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

خيارات LeaseSet:

- `EncryptLeaseSet` - أحد الخيارات التالية:
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

إنشاء مثال:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
مثال التحرير:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
احصل على مثال:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
أمثلة على بدء التشغيل، الإيقاف، إعادة التشغيل، والحذف. تتبع نفس البنية، فقط مع معلمات `Action` مختلفة:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
الطريقة - ClientServicesInfo *(مُعتمدة من i2pd)* -------------------------------------------------

تُرجع طريقة `ClientServicesInfo` معلومات الحالة حول الخدمات العميلة التي تعمل على الموجه. قم بتضمين مفاتيح الخدمة المطلوبة (مع أي قيمة) في `params` لطلب حالة كل خدمة.

المعاملات المدعومة:

- `I2PTunnel` - تُرجع خريطة من أسماء الأنفاق المُهيأة إلى عناوينها، مقسومة إلى كائنين فرعيين: `client` و`server`.
- `HTTPProxy` - تُرجع حالة تفعيل وكيل HTTP وعنوانه.
- `SOCKS` - تُرجع حالة تفعيل وكيل SOCKS وعنوانه.
- `SAM` - تُرجع حالة تفعيل جسر SAM ومعلومات الجلسة النشطة.
- `BOB` - تُرجع حالة تفعيل جسر BOB. (مُهمل في Java I2P؛ يُرجع دائمًا `false`.)
- `I2CP` - تُرجع حالة تفعيل خادم I2CP.

مثال:

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
إرجاع:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
التوافق =============

يجب الحفاظ على التوافق مع واجهة برمجة تطبيقات i2pcontrol الحالية، حيث يتم إضافة الأساليب والمعطيات الجديدة بطريقة لا تتعارض مع الوظائف الحالية. يجب أن تستمر التطبيقات الحالية التي تستخدم واجهة برمجة تطبيقات i2pcontrol في العمل دون الحاجة إلى أي تعديل، في حين يمكن للتطبيقات الجديدة الاستفادة من المعلومات والقدرات الإضافية التي يوفرها هذا الاقتراح.

التنفيذ ==============

Java I2P --------

لم يتم تنفيذ هذا الاقتراح بعد في Java I2P، لكن الكود متاح حاليًا في مستودع [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) ضمن طلب الدمج [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6). تم ذلك للسماح باختبار وتطوير الطرق الجديدة دون التأثير على الكود الحالي. وسيتم دمج التحديث لاحقًا في المستودع الرئيسي لمشروع I2P ضمن الدليل i2pcontrol بمجرد أن يصبح الكود جاهزًا للاستخدام الإنتاجي.

i2pd ----

تُنفَّذ الطرق والمعطيات المُعلَّمة بـ "(مُعتمدة من i2pd)" في i2pd دون تغيير في هذا الاقتراح. لن تتطلب امتدادات i2pd أي تعديل كجزء من هذا الاقتراح. الأجزاء غير المُعلَّمة في هذا الاقتراح غير مُنفَّذة في i2pd.

go-i2p ------

يُحفَّز go-i2p على متابعة هذا الاقتراح من أجل تمكين وتحسين تطبيق وحدة تحكم الموجه الخاص به. وسيعتمد هذا الاقتراح وينفذه في المستقبل.

emissary --------

احتمال اعتماد هذا الاقتراح في إيميساري غير معروف في الوقت الحالي، ولكن من المرجح أن يستفيد إيميساري من هذا الاقتراح بالطرق نفسها التي يستفيد بها غو-آي2بي.

الأداء ===========

لا يتوقع أي تأثير على الأداء.

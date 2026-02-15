---
title: "متتبعات UDP"
description: "مواصفات البروتوكول لإعلانات UDP BitTorrent في I2P"
slug: "udp-announces"
aliases:
  - "/ar/docs/specs/udp-bittorrent-announces"
  - "/ar/docs/specs/udp-bittorrent-announces/"
category: "البروتوكولات"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## نظرة عامة

تتضمن هذه المواصفة البروتوكول الخاص بإعلانات UDP الخاصة ببرنامج bittorrent في I2P. للاطلاع على المواصفة الشاملة لبرنامج bittorrent في I2P، راجع [BitTorrent over I2P](/docs/applications/bittorrent). للحصول على معلومات أساسية وإضافية حول تطوير هذه المواصفة، راجع [Proposal 160](/proposals/160-udp-trackers).

## التصميم

يستخدم هذا الاقتراح repliable datagram2 و repliable datagram3 و raw datagrams، كما هو محدد في [Datagrams](/docs/specs/datagrams). Datagram2 و Datagram3 هما متغيران جديدان من repliable datagrams، محددان في [الاقتراح 163](/proposals/163-datagram2-datagram3). يضيف Datagram2 مقاومة إعادة التشغيل ودعم التوقيع في وضع عدم الاتصال. Datagram3 أصغر من تنسيق datagram القديم، لكن بدون مصادقة.

### BEP 15

للمرجع، تدفق الرسائل المحدد في [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) هو كما يلي:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
مرحلة الاتصال مطلوبة لمنع انتحال عناوين IP. يقوم tracker بإرجاع معرف اتصال يستخدمه العميل في الإعلانات اللاحقة. ينتهي صلاحية معرف الاتصال هذا افتراضياً خلال دقيقة واحدة في العميل، وخلال دقيقتين في tracker.

سيستخدم I2P نفس تدفق الرسائل كما في BEP 15، لسهولة التبني في قواعد أكواد العملاء الموجودة والقادرة على UDP: من أجل الكفاءة، ولأسباب الأمان المناقشة أدناه:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
هذا يوفر احتمالياً توفيراً كبيراً في النطاق الترددي مقارنة بإعلانات البث المباشر (TCP). بينما يكون حجم Datagram2 تقريباً مماثلاً لحجم streaming SYN، فإن الاستجابة الخام أصغر بكثير من streaming SYN ACK. الطلبات اللاحقة تستخدم Datagram3، والاستجابات اللاحقة تكون خام.

طلبات الإعلان هي Datagram3 بحيث لا يحتاج المتتبع إلى الاحتفاظ بجدول تعيين كبير لمعرفات الاتصال إلى وجهة الإعلان أو الـ hash. بدلاً من ذلك، يمكن للمتتبع توليد معرفات الاتصال تشفيرياً من hash المرسل، والطابع الزمني الحالي (بناءً على فترة زمنية معينة)، وقيمة سرية. عند استلام طلب إعلان، يتحقق المتتبع من صحة معرف الاتصال، ثم يستخدم hash مرسل Datagram3 كهدف للإرسال.

### مدة الاتصال

يحدد [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) أن معرف الاتصال ينتهي في دقيقة واحدة عند العميل، وفي دقيقتين عند tracker. وهو غير قابل للتكوين. هذا يحد من مكاسب الكفاءة المحتملة، ما لم يقم العملاء بتجميع الإعلانات للقيام بها جميعاً خلال نافزة زمنية مدتها دقيقة واحدة. i2psnark لا يقوم حالياً بتجميع الإعلانات؛ بل يوزعها، لتجنب الاندفاع في حركة البيانات. يُفيد أن المستخدمين المتقدمين يشغلون آلاف ملفات التورنت في نفس الوقت، واندفاع هذا العدد الكبير من الإعلانات في دقيقة واحدة غير واقعي.

هنا، نقترح توسيع استجابة الاتصال لإضافة حقل اختياري لمدة الاتصال. الافتراضي، في حالة عدم وجوده، هو دقيقة واحدة. وإلا، فإن المدة المحددة بالثواني، سيستخدمها العميل، وسيحافظ المتتبع على معرف الاتصال لدقيقة إضافية.

### التوافق مع BEP 15

يحافظ هذا التصميم على التوافق مع [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) قدر الإمكان لتقليل التغييرات المطلوبة في العملاء والمتتبعات الموجودة.

التغيير المطلوب الوحيد هو تنسيق معلومات النظراء في استجابة الإعلان. إضافة حقل مدة البقاء في استجابة الاتصال غير مطلوبة ولكنها موصى بها بشدة من أجل الكفاءة، كما هو موضح أعلاه.

### تحليل الأمان

هدف مهم لبروتوكول الإعلان UDP هو منع انتحال العناوين. يجب أن يكون العميل موجوداً فعلياً ويحزم leaseset حقيقي. يجب أن يكون لديه أنفاق واردة لاستقبال استجابة الاتصال. يمكن أن تكون هذه الأنفاق بدون قفزات ومبنية فورياً، لكن ذلك سيكشف المنشئ. هذا البروتوكول يحقق ذلك الهدف.

### المشاكل

- هذا البروتوكول لا يدعم الوجهات المخفية، ولكن قد يتم توسيعه للقيام بذلك. انظر أدناه.

## المواصفات

### البروتوكولات والمنافذ

Repliable Datagram2 يستخدم I2CP protocol 19؛ repliable Datagram3 يستخدم I2CP protocol 20؛ raw datagrams تستخدم I2CP protocol 18. قد تكون الطلبات Datagram2 أو Datagram3. الردود دائماً raw. تنسيق repliable datagram الأقدم ("Datagram1") الذي يستخدم I2CP protocol 17 يجب ألا يُستخدم للطلبات أو الردود؛ يجب إسقاطها إذا تم استلامها على منافذ الطلب/الرد. لاحظ أن Datagram1 protocol 17 لا يزال يُستخدم لبروتوكول DHT.

تستخدم الطلبات I2CP "to port" من رابط الإعلان؛ انظر أدناه. يتم اختيار "from port" للطلب من قبل العميل، ولكن يجب أن يكون غير صفر، ومنفذ مختلف عن تلك المستخدمة من قبل DHT، بحيث يمكن تصنيف الاستجابات بسهولة. يجب على أجهزة التتبع رفض الطلبات المستلمة على المنفذ الخاطئ.

تستخدم الاستجابات "منفذ الوجهة" من I2CP من الطلب. "منفذ المصدر" للطلب هو "منفذ الوجهة" من الطلب.

### رابط الإعلان

تنسيق URL للإعلان غير محدد في [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)، ولكن كما في الشبكة العادية، فإن URLs الإعلان UDP تكون بالشكل `udp://host:port/path`. المسار يتم تجاهله وقد يكون فارغاً، لكنه عادة ما يكون `/announce` في الشبكة العادية. يجب أن يكون جزء `:port` موجوداً دائماً، ومع ذلك، إذا تم حذف جزء `:port`، استخدم منفذ I2CP الافتراضي 6969، حيث أنه المنفذ الشائع في الشبكة العادية. قد تكون هناك أيضاً معاملات cgi مُلحقة `&a=b&c=d`، والتي يمكن معالجتها وتقديمها في طلب الإعلان، انظر [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). إذا لم تكن هناك معاملات أو مسار، فيمكن أيضاً حذف الشرطة المائلة الأخيرة `/`، كما هو مضمن في [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

### تنسيقات البيانات المجمعة

جميع القيم ترسل بترتيب البايت الشبكي (big endian). لا تتوقع أن تكون الحزم بحجم معين بالضبط. التحسينات المستقبلية قد تزيد من حجم الحزم.

#### طلب الاتصال

العميل إلى المتتبع. 16 بايت. يجب أن يكون Datagram2 قابل للرد عليه. نفس الشيء كما في [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). بلا تغييرات.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### استجابة الاتصال

من المتتبع إلى العميل. 16 أو 18 بايت. يجب أن تكون خام. نفس ما هو موضح في [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) باستثناء ما هو مذكور أدناه.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
يجب إرسال الاستجابة إلى "منفذ الوجهة" في I2CP الذي تم استقباله كـ "منفذ المصدر" في الطلب.

حقل lifetime اختياري ويشير إلى مدة بقاء العميل connection_id بالثواني. القيمة الافتراضية هي 60، والحد الأدنى إذا تم تحديده هو 60. الحد الأقصى هو 65535 أو حوالي 18 ساعة. يجب على المتتبع الحفاظ على connection_id لمدة 60 ثانية أكثر من مدة بقاء العميل.

#### طلب الإعلان

العميل إلى المتتبع. 98 بايت كحد أدنى. يجب أن يكون Datagram3 قابلاً للرد. نفس ما هو في [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) باستثناء ما هو مذكور أدناه.

الـ connection_id كما تم استقباله في استجابة الاتصال.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
التغييرات من [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- المفتاح (key) يتم تجاهله
- عنوان IP غير مستخدم
- المنفذ (port) على الأرجح يتم تجاهله ولكن يجب أن يكون نفس منفذ I2CP
- قسم الخيارات، إن وُجد، كما هو محدد في [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

يجب إرسال الرد إلى "منفذ الوجهة" في I2CP الذي تم استلامه كـ "منفذ المصدر" للطلب. لا تستخدم المنفذ من طلب الإعلان.

#### استجابة الإعلان

من المتتبع إلى العميل. 20 بايت كحد أدنى. يجب أن يكون خام. نفس الشيء كما في [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) باستثناء ما هو مذكور أدناه.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
التغييرات من [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- بدلاً من 6 بايت IPv4+port أو 18 بايت IPv6+port، نرجع مضاعفات من "الاستجابات المدمجة" 32 بايت مع SHA-256 binary peer hashes. كما هو الحال مع استجابات TCP المدمجة، لا نضمن port.

يجب إرسال الاستجابة إلى "منفذ الوجهة" في I2CP الذي تم استقباله كـ "منفذ المصدر" في الطلب. لا تستخدم المنفذ من طلب الإعلان.

رسائل البيانات I2P لها حد أقصى كبير جداً يبلغ حوالي 64 كيلوبايت؛ ومع ذلك، للتسليم الموثوق، يجب تجنب رسائل البيانات الأكبر من 4 كيلوبايت. لكفاءة النطاق الترددي، يجب على المتتبعات (trackers) على الأرجح تحديد الحد الأقصى للأقران (peers) إلى حوالي 50، مما يقابل حوالي 1600 بايت في الحزمة قبل الحمولة الإضافية في الطبقات المختلفة، ويجب أن يكون ضمن حد حمولة رسالتين في النفق بعد التجزئة.

كما هو الحال في BEP 15، لا يوجد عداد مضمّن لعدد عناوين الأقران (IP/port بالنسبة لـ BEP 15، وhashes هنا) التي ستتبع. وبينما لم يتم التفكير في هذا في BEP 15، يمكن تعريف علامة نهاية الأقران المكونة من جميع الأصفار للإشارة إلى أن معلومات الأقران مكتملة وأن بعض البيانات الإضافية تتبع.

لذلك يكون هذا التمديد ممكناً في المستقبل، يجب على العملاء تجاهل hash من 32 بايت يحتوي على أصفار فقط، وأي بيانات تتبعه. يجب على أجهزة التتبع رفض الإعلانات من hash يحتوي على أصفار فقط، رغم أن هذا الـ hash محظور بالفعل من قِبل router الـ Java.

#### كشط

طلب/استجابة الكشط من [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) غير مطلوب بواسطة هذه المواصفات، ولكن يمكن تنفيذه عند الرغبة، ولا حاجة لأي تغييرات. يجب على العميل الحصول على معرف اتصال أولاً. طلب الكشط هو دائماً Datagram3 قابل للرد. استجابة الكشط هي دائماً خام.

#### استجابة الخطأ

من tracker إلى العميل. 8 بايت كحد أدنى (إذا كانت الرسالة فارغة). يجب أن تكون خام. نفس الشيء كما في [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). لا توجد تغييرات.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## الإضافات

لا يتم تضمين بتات الإضافة أو حقل الإصدار. لا يجب على العملاء والمتتبعات افتراض أن الحزم لها حجم معين. بهذه الطريقة، يمكن إضافة حقول إضافية دون كسر التوافق. يُنصح بتنسيق الإضافات المحدد في [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) إذا كان مطلوباً.

يتم تعديل استجابة الاتصال لإضافة مدة صالحية اختيارية لمعرف الاتصال.

إذا كان دعم الوجهة المعماة مطلوباً، يمكننا إما إضافة العنوان المعمى بحجم 35 بايت إلى نهاية طلب الإعلان، أو طلب الهاشات المعماة في الردود، باستخدام تنسيق [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) (المعاملات لم تُحدد بعد). يمكن إضافة مجموعة عناوين النظراء المعماة بحجم 35 بايت إلى نهاية رد الإعلان، بعد هاش بحجم 32 بايت مكون من أصفار.

## إرشادات التنفيذ

انظر قسم التصميم أعلاه لمناقشة التحديات التي تواجه العملاء والمتتبعات غير المتكاملة وغير I2CP.

### العملاء

بالنسبة لاسم مضيف tracker معين، يجب على العميل تفضيل UDP على HTTP URLs، ويجب ألا يعلن للاثنين معاً.

العملاء الذين لديهم دعم BEP 15 موجود يجب أن يحتاجوا فقط إلى تعديلات صغيرة.

إذا كان العميل يدعم DHT أو بروتوكولات datagram أخرى، فيجب عليه على الأرجح اختيار منفذ مختلف كـ "منفذ المرسل" للطلب حتى تعود الردود إلى ذلك المنفذ ولا تختلط مع رسائل DHT. العميل يتلقى فقط datagrams خام كردود. المتتبعات لن ترسل أبداً datagram2 قابل للرد إلى العميل.

يجب على العملاء الذين لديهم قائمة افتراضية من الـ opentrackers تحديث القائمة لإضافة عناوين UDP بعد أن يُعرف أن الـ opentrackers المعروفة تدعم UDP.

قد يقوم العملاء بتنفيذ إعادة الإرسال للطلبات أو قد لا يقومون بذلك. إعادة الإرسال، في حال تنفيذها، يجب أن تستخدم مهلة زمنية أولية لا تقل عن 15 ثانية، ومضاعفة المهلة الزمنية لكل إعادة إرسال (التراجع الأسي).

يجب على العملاء التراجع بعد تلقي استجابة خطأ.

### المتتبعات

أجهزة التتبع التي تدعم BEP 15 الحالية يجب أن تتطلب تعديلات صغيرة فقط. تختلف هذه المواصفة عن اقتراح 2014، في أن جهاز التتبع يجب أن يدعم استقبال repliable datagram2 و datagram3 على نفس المنفذ.

لتقليل متطلبات موارد المتتبع، تم تصميم هذا البروتوكول للقضاء على أي متطلب يقتضي أن يخزن المتتبع تطابقات الهاشات الخاصة بالعملاء مع معرفات الاتصال للتحقق اللاحق. هذا ممكن لأن حزمة طلب الإعلان هي حزمة Datagram3 قابلة للرد، لذا فهي تحتوي على هاش المرسل.

التنفيذ الموصى به هو:

- تعريف العصر الحالي كالوقت الحالي بدقة مدى حياة الاتصال، `epoch = now / lifetime`.
- تعريف دالة التجميع التشفيرية `H(secret, clienthash, epoch)` التي تولد مخرجات بحجم 8 بايت.
- توليد الثابت العشوائي السري المستخدم لجميع الاتصالات.
- لاستجابات الاتصال، توليد `connection_id = H(secret, clienthash, epoch)`
- لطلبات الإعلان، التحقق من صحة معرف الاتصال المستلم في العصر الحالي من خلال التأكد من `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## المراجع

- **[BEP15]** [BEP 15 - بروتوكول UDP Tracker](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - امتدادات بروتوكول UDP Tracker](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [مواصفات Datagrams](/docs/specs/datagrams)
- **[Prop160]** [اقتراح 160 - UDP Trackers](/proposals/160-udp-trackers)
- **[Prop163]** [اقتراح 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [واجهة برمجة تطبيقات SAMv3](/docs/api/samv3)
- **[SPEC]** [BitTorrent عبر I2P](/docs/applications/bittorrent)

---
title: "عملاء I2P البديلة"
description: "تطبيقات عميل I2P التي يحتفظ بها المجتمع (محدثة لعام 2025)"
slug: "alternative-clients"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

تستخدم التطبيق الرئيسي لعميل I2P لغة **Java**. إذا كنت لا تستطيع أو تفضل عدم استخدام Java على نظام معين، فهناك تطبيقات بديلة لعميل I2P تم تطويرها وصيانتها من قبل أعضاء المجتمع. توفر هذه البرامج نفس الوظائف الأساسية باستخدام لغات برمجة أو أساليب مختلفة.

---

## جدول المقارنة

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Client</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Maturity</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Actively Maintained</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Suitable For</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Java I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes (official)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">General users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Standard full router; includes console, plugins, and tools</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>i2pd</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Low-resource systems, servers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Lightweight, fully compatible with Java I2P, includes web console</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Go-I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, testing</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Early-stage Go implementation; not yet production ready</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Emissary</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, embedded use</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust I2P implementation; embeddable router with eepsite, torrent, IRC and email support</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>I2P+</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable (fork)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Advanced users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Enhanced Java I2P fork with UI and performance improvements</td>
    </tr>
  </tbody>
</table>
---

## i2pd (C++)

**الموقع الإلكتروني:** [https://i2pd.website](https://i2pd.website)

**الوصف:** i2pd (أي *I2P Daemon*) هو عميل I2P كامل المواصفات مُطور بلغة C++. لقد كان مستقراً للاستخدام في الإنتاج لسنوات عديدة (منذ حوالي 2016) ويتم صيانته بنشاط من قبل المجتمع. ينفذ i2pd بروتوكولات وواجهات برمجة التطبيقات الخاصة بشبكة I2P بشكل كامل، مما يجعله متوافقاً تماماً مع شبكة Java I2P. يُستخدم هذا الـ router المكتوب بـ C++ غالباً كبديل خفيف الوزن على الأنظمة التي لا تتوفر فيها بيئة تشغيل Java أو غير مرغوبة. يتضمن i2pd وحدة تحكم مدمجة قائمة على الويب للتكوين والمراقبة. إنه متعدد المنصات ومتاح بصيغ تغليف متعددة — يوجد حتى إصدار Android من i2pd متاح (على سبيل المثال، عبر F-Droid).

---

## Go-I2P (Go)

**المستودع:** [https://github.com/go-i2p/go-i2p](https://github.com/go-i2p/go-i2p)

**الوصف:** Go-I2P هو عميل I2P مكتوب بلغة البرمجة Go. وهو تنفيذ مستقل لـ router الخاص بـ I2P، يهدف إلى الاستفادة من كفاءة وقابلية النقل في Go. المشروع قيد التطوير النشط، ولكنه لا يزال في مرحلة مبكرة وليس مكتمل الميزات بعد. اعتباراً من عام 2025، يُعتبر Go-I2P تجريبياً — يعمل عليه بنشاط مطوري المجتمع، لكن لا يُنصح باستخدامه في بيئة الإنتاج حتى ينضج أكثر. الهدف من Go-I2P هو توفير router حديث وخفيف الوزن لـ I2P مع توافق كامل مع شبكة I2P بمجرد اكتمال التطوير.

---

## Emissary (Rust)

**الموقع الإلكتروني:** [https://altonen.github.io/emissary/](https://altonen.github.io/emissary/)

**الوصف:** Emissary هو تطبيق بلغة Rust لمجموعة بروتوكولات I2P، مصمم ليعمل كـ router قابل للدمج في I2P. يمكن دمجه في التطبيقات الأخرى أو تشغيله بشكل مستقل. يدعم Emissary استضافة eepsite والتورنت وخدمات IRC والبريد الإلكتروني. يتضمن المشروع وثائق شاملة تغطي الإعداد السريع والدمج للمطورين والتكوين المفصل. كونه مشروعاً تجريبياً، فهو قيد التطوير النشط ولا يُنصح باستخدامه في البيئات الإنتاجية بعد.

---

## I2P+ (نسخة Java المتفرعة)

**الموقع الإلكتروني:** [https://i2pplus.github.io](https://i2pplus.github.io)

**الوصف:** I2P+ هو إصدار مُحدَّث مجتمعياً من عميل Java I2P الرسمي. إنه ليس إعادة تنفيذ بلغة جديدة، بل نسخة محسنة من router الـ Java مع ميزات وتحسينات إضافية. يركز I2P+ على تقديم تجربة مستخدم محسنة وأداء أفضل مع الحفاظ على التوافق الكامل مع شبكة I2P الرسمية. يقدم واجهة وحدة تحكم ويب محدثة، وخيارات تكوين أكثر سهولة للمستخدم، وتحسينات متنوعة (على سبيل المثال، تحسين أداء torrent والتعامل الأفضل مع أقران الشبكة، خاصة للـ routers خلف الجدران النارية). يتطلب I2P+ بيئة Java تماماً مثل برنامج I2P الرسمي، لذا فهو ليس حلاً لبيئات غير Java. ومع ذلك، للمستخدمين الذين لديهم Java ويريدون إصداراً بديلاً بقدرات إضافية، يوفر I2P+ خياراً مقنعاً. يتم الحفاظ على هذا الإصدار محدثاً مع إصدارات I2P الرئيسية (مع إضافة "+" إلى رقم الإصدار) ويمكن الحصول عليه من موقع المشروع.

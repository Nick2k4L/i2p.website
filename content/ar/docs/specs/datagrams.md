---
title: "مواصفات Datagram"
description: "مواصفات تنسيقات رسائل I2P datagram بما في ذلك الأنواع الخام والقابلة للرد والمصدقة"
slug: "datagrams"
category: "البروتوكولات"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## نظرة عامة

راجع [وثائق واجهة برمجة التطبيقات Datagrams](/docs/api/datagrams/) للحصول على نظرة عامة حول واجهة برمجة التطبيقات Datagrams.

الأنواع التالية محددة. أرقام البروتوكولات المعيارية مدرجة، ولكن يمكن استخدام أي أرقام بروتوكولات أخرى غير رقم بروتوكول الـ streaming (6)، حسب التطبيق المحدد.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
الدعم لـ Datagram2 و Datagram3 في تطبيقات router والمكتبات المختلفة لم يتم تحديده بعد. تحقق من الوثائق الخاصة بتلك التطبيقات.

### تحديد نوع الرسالة المجمعة

الأنواع الأربعة من datagram لا تتشارك رأس مشترك مع إصدار البروتوكول في نفس المكان. لا يمكن تحديد الحزم حسب النوع بناءً على محتواها. عند استخدام أنواع متعددة في نفس الجلسة، أو نوع واحد مع streaming، يجب على التطبيقات استخدام أرقام البروتوكولات و/أو منافذ I2CP/SAM لتوجيه الحزم الواردة إلى المكان الصحيح. استخدام أرقام البروتوكولات المعيارية سيجعل هذا أسهل. ترك رقم البروتوكول غير محدد (0 أو PROTO_ANY)، حتى لتطبيق datagram فقط، غير مُوصى به لأنه يزيد من احتمالية أخطاء التوجيه ويجعل الترقيات إلى تطبيق متعدد البروتوكولات أصعب. حقول الإصدار في Datagram 2 و 3 مُوفرة فقط كفحص إضافي لأخطاء التوجيه والتغييرات المستقبلية.

### تصميم التطبيق

جميع استخدامات البيانات المجمعة (datagrams) خاصة بالتطبيق.

نظراً لأن البيانات المُصادق عليها تحمل عبئاً إضافياً كبيراً، فإن التطبيق النموذجي يستخدم كلاً من البيانات المُصادق عليها وغير المُصادق عليها. التصميم النموذجي هو إرسال بيانات مُصادق عليها واحدة تحتوي على رمز مميز من العميل إلى الخادم. يرد الخادم ببيانات غير مُصادق عليها تحتوي على نفس الرمز المميز. أي تواصل لاحق، قبل انتهاء مهلة الرمز المميز، يستخدم البيانات الخام.

التطبيقات ترسل وتستقبل datagrams باستخدام أرقام البروتوكول والمنافذ عبر واجهة برمجة التطبيقات [I2CP](/docs/specs/i2cp/) أو [SAMv3](/docs/api/samv3/).

المخططات البيانية (Datagrams) غير موثوقة بطبيعة الحال. يجب على التطبيقات أن تصمم للتسليم غير الموثوق. داخل I2P، التسليم موثوق من قفزة إلى قفزة إذا كانت القفزة التالية قابلة للوصول، حيث أن بروتوكولات النقل NTCP2 و SSU2 توفر الموثوقية. ومع ذلك، التسليم من النهاية إلى النهاية ليس موثوقاً، حيث أن رسائل I2NP قد يتم إسقاطها داخل أي قفزة بسبب حدود الطوابير، انتهاء الصلاحية، المهلة الزمنية، حدود عرض النطاق الترددي، أو القفزات التالية غير القابلة للوصول.

### حجم Datagram

الحد الأقصى الاسمي لحجم رسائل I2NP، بما في ذلك المخططات البيانية، هو 64 كيلوبايت. إن النفقات الإضافية لرسائل garlic encryption والـ tunnel تقلل من هذا الحد إلى حد ما.

ومع ذلك، يجب تجزئة جميع رسائل I2NP إلى رسائل tunnel بحجم 1 كيلوبايت. احتمالية إسقاط رسالة I2NP بحجم n كيلوبايت هي دالة أسية لاحتمالية إسقاط رسالة tunnel واحدة، p ** n. نظراً لأن التجزئة تؤدي إلى انفجار في رسائل tunnel، فإن احتمالية الإسقاط الفعلية أعلى بكثير مما تشير إليه الدالة الأسية، وذلك بسبب حدود الطوابير وإدارة الطوابير النشطة (AQM، CoDel أو ما شابه) في تطبيقات router.

الحد الأقصى الموصى به للحجم النموذجي لضمان التسليم الموثوق هو بضعة كيلوبايت، أو على الأكثر 10 كيلوبايت. مع التحليل الدقيق لأحجام الرؤوس الإضافية في جميع طبقات البروتوكول (باستثناء النقل)، يجب على المطورين تعيين حد أقصى لحجم الحمولة المفيدة بحيث يتناسب تماماً مع رسالة tunnel واحدة أو اثنتين أو ثلاث. هذا سيزيد من الكفاءة والموثوقية إلى أقصى حد. تشمل الرؤوس الإضافية في الطبقات المختلفة رأس gzip، رأس I2NP، رأس رسالة garlic، تشفير garlic، رأس رسالة tunnel، رؤوس تجزئة رسالة tunnel، وغيرها. راجع حسابات streaming MTU في [الاقتراح 144](/proposals/144-ecies-x25519-aead-ratchet/) و ConnectionOptions.java في كود مصدر Java I2P للأمثلة.

### اعتبارات SAM

ترسل التطبيقات وتستقبل datagrams باستخدام أرقام البروتوكول والمنافذ عبر I2CP API أو SAM. يتطلب تحديد أرقام البروتوكول والمنافذ عبر SAM إصدار SAM v3.2 أو أحدث. يتطلب استخدام كل من datagrams والتدفق (UDP وTCP) في نفس جلسة SAM (tunnels) إصدار SAM v3.3 أو أحدث. يتطلب استخدام أنواع متعددة من datagram في نفس جلسة SAM (tunnels) إصدار SAM v3.3 أو أحدث. SAM v3.3 مدعوم فقط من قِبل router I2P الخاص بـ Java في الوقت الحالي.

دعم SAM لـ Datagram2 و Datagram3 في تطبيقات router والمكتبات المختلفة لم يتم تحديده بعد. تحقق من الوثائق الخاصة بتلك التطبيقات.

لاحظ أن الأحجام التي تتجاوز الـ 1500 بايت النموذجية لـ MTU الشبكة ستمنع تطبيقات SAM من نقل حزم غير مجزأة من/إلى خادم SAM، إذا كان التطبيق والخادم على أجهزة كمبيوتر منفصلة. عادةً، هذا ليس هو الحال، حيث يكون كلاهما على localhost، حيث يكون MTU هو 65536 أو أعلى. إذا كان من المتوقع فصل تطبيق SAM على كمبيوتر مختلف عن الخادم، فإن الحد الأقصى للحمولة لـ datagram قابل للرد يكون أقل بقليل من 1 كيلوبايت.

### اعتبارات PQ

إذا تم تنفيذ جزء MLDSA من [الاقتراح 169](/proposals/169-pq-crypto/) الخاص بـ Post-Quantum، فإن الحمولة الإضافية ستزداد بشكل كبير. سيزداد حجم الوجهة + التوقيع من 391 + 64 = 455 بايت إلى حد أدنى قدره 3739 لـ MLDSA44 وحد أقصى قدره 7226 لـ MLDSA87. التأثيرات العملية لهذا لم تُحدد بعد. Datagram3، مع المصادقة المقدمة من router، قد يكون حلاً.

## الرسائل الخام (غير القابلة للرد) {#raw}

الرسائل المجمعة غير القابلة للرد ليس لها عنوان 'من' وغير مصادق عليها. تُسمى أيضاً الرسائل المجمعة "الخام". من الناحية الفنية الصارمة، ليست "رسائل مجمعة" على الإطلاق، بل هي مجرد بيانات خام. لا يتم التعامل معها بواسطة datagram API. ومع ذلك، فإن SAM وفئات I2PTunnel تدعم "الرسائل المجمعة الخام".

رقم بروتوكول I2CP القياسي للرسائل الخام هو PROTO_DATAGRAM_RAW (18).

التنسيق غير محدد هنا، بل يتم تعريفه بواسطة التطبيق. من أجل الاكتمال، نضمّن صورة للتنسيق أدناه.

### التنسيق

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### ملاحظات

الطول العملي محدود بكل من النفقات العامة في الطبقات المختلفة والموثوقية.

## Datagram1 (قابل للرد) {#repliable}

البيانات القابلة للرد تحتوي على عنوان 'من' وتوقيع. هذه تضيف على الأقل 427 بايت من البيانات الإضافية.

رقم بروتوكول I2CP القياسي للرسائل البيانية القابلة للرد هو PROTO_DATAGRAM (17).

### التنسيق

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### ملاحظات

- الطول العملي محدود بكل من النفقات العامة في طبقات مختلفة والموثوقية.
- راجع الملاحظات المهمة حول موثوقية البيانات الكبيرة في [وثائق Datagrams API](/docs/api/datagrams/). للحصول على أفضل النتائج، احصر الحمولة في حوالي 10 كيلو بايت أو أقل.
- تم إعادة تعريف التواقيع للأنواع الأخرى غير DSA_SHA1 في الإصدار 0.9.14.
- التنسيق لا يدعم تضمين كتلة توقيع غير متصلة لـ LS2 (الاقتراح 123). يجب تعريف بروتوكول جديد مع علامات لذلك.

## Datagram2 {#datagram2}

تنسيق Datagram2 محدد كما هو موضح في [الاقتراح 163](/proposals/163-datagram2/). رقم بروتوكول I2CP لـ Datagram2 هو 19.

Datagram2 مخصص ليكون بديلاً عن Datagram1. يضيف الميزات التالية إلى Datagram1:

- منع إعادة التشغيل
- دعم التوقيع دون اتصال
- حقول الأعلام والخيارات لقابلية التوسع

لاحظ أن خوارزمية حساب التوقيع لـ Datagram2 تختلف بشكل كبير عن Datagram1.

### التنسيق

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
الطول الإجمالي: الحد الأدنى 433 + طول البيانات المفيدة؛ الطول النموذجي لمرسلي X25519 وبدون التوقيعات غير المتصلة: 457 + طول البيانات المفيدة. لاحظ أن الرسالة عادةً ما يتم ضغطها باستخدام gzip في طبقة I2CP، مما يؤدي إلى توفير كبير إذا كان وجهة المرسل قابلة للضغط.

ملاحظة: تنسيق التوقيع غير المتصل هو نفسه الموجود في [مواصفات الهياكل المشتركة](/docs/specs/common-structures/) و[مواصفات التدفق](/docs/specs/streaming/).

### التوقيعات

التوقيع يكون على الحقول التالية:

- Prelude: الـ hash بحجم 32 بايت للوجهة المستهدفة (غير مشمول في الـ datagram)
- flags
- options (إذا كانت موجودة)
- offline_signature (إذا كانت موجودة)
- payload

في الرسائل البيانية القابلة للرد، بالنسبة لنوع المفتاح DSA_SHA1، كان التوقيع يتم على hash SHA-256 للحمولة، وليس على الحمولة نفسها؛ هنا، يكون التوقيع دائماً على الحقول المذكورة أعلاه (وليس على الـ hash)، بغض النظر عن نوع المفتاح.

### التحقق من ToHash

يجب على المستقبلين التحقق من التوقيع (باستخدام hash الوجهة الخاص بهم) وإلغاء الرسالة في حالة الفشل، لمنع إعادة التشغيل.

## Datagram3 {#datagram3}

تنسيق Datagram3 كما هو محدد في [الاقتراح 163](/proposals/163-datagram2/). رقم بروتوكول I2CP لـ Datagram3 هو 20.

Datagram3 مُصمم كنسخة محسّنة من الـ raw datagrams. يضيف الميزات التالية إلى الـ raw datagrams:

- قابلية التكرار
- حقول العلامات والخيارات لقابلية التوسيع

Datagram3 غير مُصادق عليه. في اقتراح مستقبلي، قد يتم توفير المصادقة بواسطة طبقة ratchet الخاصة بـ router، وسيتم تمرير حالة المصادقة إلى العميل.

### التنسيق

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
الطول الإجمالي: الحد الأدنى 34 + طول البيانات النافعة.

## المراجع

- [Common](/docs/specs/common-structures/) - مواصفة الهياكل المشتركة
- [DATAGRAMS](/docs/api/datagrams/) - نظرة عامة على واجهة برمجة التطبيقات للرسائل المجمعة
- [I2CP](/docs/specs/i2cp/) - مواصفة I2CP
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - اقتراح ECIES-X25519-AEAD-Ratchet
- [Prop163](/proposals/163-datagram2/) - اقتراح Datagram2 و Datagram3
- [Prop169](/proposals/169-pq-crypto/) - اقتراح التشفير ما بعد الكمي
- [SAMv3](/docs/api/samv3/) - مواصفة SAM v3
- [Streaming](/docs/specs/streaming/) - مواصفة البث المتدفق
- [TRANSPORT](/docs/overview/transport/) - نظرة عامة على النقل
- [TUNMSG](/docs/specs/tunnel-message/#notes) - مواصفة رسالة tunnel

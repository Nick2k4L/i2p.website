---
title: "مواصفات بروتوكول التدفق"
description: "مواصفة بروتوكول I2P streaming الذي يوفر نقل موثوق شبيه بـ TCP"
slug: "streaming"
category: "البروتوكولات"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## نظرة عامة

انظر [مكتبة البث](/docs/api/streaming) للحصول على نظرة عامة حول بروتوكول البث.

## إصدارات البروتوكول

بروتوكول التدفق لا يتضمن حقل إصدار. الإصدارات المدرجة أدناه مخصصة لـ Java I2P. قد تختلف التطبيقات ودعم التشفير الفعلي. لا توجد طريقة لتحديد ما إذا كان الطرف البعيد يدعم أي إصدار أو ميزة معينة. الجدول أدناه مخصص للإرشاد العام حول تواريخ إصدار الميزات المختلفة.

الميزات المدرجة أدناه خاصة بالبروتوكول نفسه. يتم توثيق الخيارات المختلفة للتكوين في [مكتبة Streaming](/docs/api/streaming) إلى جانب إصدار Java I2P الذي تم تنفيذها فيه.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## مواصفات البروتوكول

### تنسيق الحزمة

تنسيق حزمة واحدة في بروتوكول التدفق موضح أدناه. الحد الأدنى لحجم الرأس، بدون NACKs أو بيانات الخيارات، هو 22 بايت.

لا يوجد حقل طول في بروتوكول التدفق. يتم توفير التأطير بواسطة الطبقات السفلى - I2CP و I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 بايت [Integer](/docs/specs/common-structures#integer) : رقم عشوائي يختاره مستقبل الحزمة قبل إرسال أول حزمة رد SYN وثابت طوال عمر الاتصال، أكبر من الصفر. 0 في رسالة SYN المرسلة من قبل منشئ الاتصال، وفي الرسائل اللاحقة، حتى يتم استلام رد SYN، الذي يحتوي على معرف التدفق الخاص بالند.

**receiveStreamId** :: 4 بايت [Integer](/docs/specs/common-structures#integer) : رقم عشوائي يختاره منشئ الحزمة قبل إرسال أول حزمة SYN ويبقى ثابتاً طوال مدة الاتصال، أكبر من الصفر. قد يكون 0 إذا كان غير معروف، على سبيل المثال في حزمة RESET.

**sequenceNum** :: 4 بايت [Integer](/docs/specs/common-structures#integer) : التسلسل لهذه الرسالة، يبدأ من 0 في رسالة SYN، ويزداد بـ 1 في كل رسالة باستثناء رسائل ACK العادية وإعادة الإرسال. إذا كان sequenceNum هو 0 وعلامة SYN غير مضبوطة، فهذه حزمة ACK عادية يجب ألا يتم إرسال ACK لها.

**ackThrough** :: 4 byte [Integer](/docs/specs/common-structures#integer) : أعلى رقم تسلسل حزمة تم استلامها على receiveStreamId. يتم تجاهل هذا الحقل في حزمة الاتصال الأولي (حيث receiveStreamId هو المعرف المجهول) أو إذا تم تعيين علامة NO_ACK. جميع الحزم حتى هذا الرقم التسلسلي وتشمله يتم إقرار استلامها (ACK)، باستثناء تلك المدرجة في NACKs أدناه.

**عدد NACK** :: 1 بايت [Integer](/docs/specs/common-structures#integer) : عدد NACKs بحجم 4 بايت في الحقل التالي، أو 8 عند الاستخدام مع SYNCHRONIZE لمنع إعادة التشغيل اعتباراً من الإصدار 0.9.58؛ انظر أدناه.

**NACKs** :: nc * 4 byte [Integer](/docs/specs/common-structures#integer)s : أرقام التسلسل الأقل من ackThrough التي لم يتم استلامها بعد. إرسال NACK مرتين لحزمة واحدة يُعتبر طلباً لـ "إعادة إرسال سريعة" لتلك الحزمة. يُستخدم أيضاً مع SYNCHRONIZE لمنع إعادة التشغيل اعتباراً من الإصدار 0.9.58؛ انظر أدناه.

**resendDelay** :: 1 بايت [Integer](/docs/specs/common-structures#integer) : كم من الوقت سينتظر منشئ هذه الحزمة قبل إعادة إرسالها (إذا لم يتم تأكيد استلامها بعد). القيمة بالثواني منذ إنشاء الحزمة. يتم تجاهلها حالياً عند الاستقبال.

**flags** :: قيمة 2 بايت : انظر أدناه.

**حجم الخيار** :: 2 بايت [Integer](/docs/specs/common-structures#integer) : عدد البايتات في الحقل التالي

**بيانات الخيار** :: 0 أو أكثر من البايتات : كما هو محدد بواسطة العلامات. انظر أدناه.

**payload** :: حجم الحزمة المتبقي

### حقول الأعلام وبيانات الخيارات

حقل الأعلام أعلاه يحدد بعض البيانات الوصفية حول الحزمة، وبدوره قد يتطلب تضمين بيانات إضافية معينة. الأعلام كما يلي. يجب إضافة أي هياكل بيانات محددة إلى منطقة الخيارات بالترتيب المعطى.

ترتيب البت: 15....0 (15 هو MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### ملاحظات التوقيع متغير الطول

قبل الإصدار 0.9.11، كان التوقيع في حقل الخيار دائماً 40 بايت.

اعتباراً من الإصدار 0.9.11، يكون التوقيع متغير الطول. يتم استنتاج نوع التوقيع وطوله من نوع المفتاح المستخدم في خيار FROM_INCLUDED ومن توثيق [Signature](/docs/specs/common-structures#signature).

اعتبارًا من الإصدار 0.9.39، يتم دعم خيار OFFLINE_SIGNATURE. إذا كان هذا الخيار موجودًا، يتم استخدام [SigningPublicKey](/docs/specs/common-structures#signingpublickey) المؤقت للتحقق من أي حزم موقعة، ويتم استنتاج طول التوقيع ونوعه من SigningPublicKey المؤقت في الخيار.

- عندما تحتوي الحزمة على كل من FROM_INCLUDED و SIGNATURE_INCLUDED (كما في SYNCHRONIZE)، يمكن إجراء الاستنتاج مباشرة.

- عندما لا تحتوي الحزمة على FROM_INCLUDED، يجب استنتاج ذلك من حزمة SYNCHRONIZE سابقة.

- عندما لا تحتوي الحزمة على FROM_INCLUDED، ولم تكن هناك حزمة SYNCHRONIZE سابقة (على سبيل المثال حزمة CLOSE أو RESET شاردة)، يمكن الاستنتاج من طول الخيارات المتبقية (حيث أن SIGNATURE_INCLUDED هو الخيار الأخير)، لكن من المحتمل أن يتم تجاهل الحزمة على أي حال، حيث لا يوجد FROM متاح للتحقق من صحة التوقيع. إذا تم تعريف المزيد من حقول الخيارات في المستقبل، يجب أخذها في الاعتبار.

### منع إعادة التشغيل

لمنع بوب من استخدام هجوم إعادة التشغيل عبر تخزين حزمة SYNCHRONIZE موقعة صالحة مُستقبلة من أليس وإرسالها لاحقاً إلى الضحية تشارلي، يجب على أليس تضمين hash الوجهة الخاص ببوب في حزمة SYNCHRONIZE كما يلي:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
عند استلام SYNCHRONIZE، إذا كان حقل عدد NACK يساوي 8، يجب على Bob تفسير حقل NACKs كـ hash وجهة بحجم 32 بايت، ويجب عليه التحقق من أنه يطابق hash وجهته. كما يجب عليه التحقق من توقيع الحزمة كالمعتاد، حيث أن ذلك يغطي الحزمة بالكامل بما في ذلك حقل عدد NACK وحقل NACKs. إذا كان عدد NACK يساوي 8 وحقل NACKs لا يطابق، يجب على Bob إسقاط الحزمة.

هذا مطلوب للإصدارات 0.9.58 وما أعلى. هذا متوافق مع الإصدارات الأقدم، لأن NACKs غير متوقعة في حزمة SYNCHRONIZE. الوجهات لا تعرف ولا يمكنها معرفة أي إصدار يعمل على الطرف الآخر.

لا حاجة لأي تغيير في حزمة SYNCHRONIZE ACK المرسلة من Bob إلى Alice؛ لا تقم بتضمين NACKs في تلك الحزمة.

## المراجع

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [مكتبة البث](/docs/api/streaming)

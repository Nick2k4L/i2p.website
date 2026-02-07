---
title: "مواصفات إنشاء tunnel"
description: "مواصفات بناء tunnel باستخدام ElGamal لإنشاء الأنفاق باستخدام التلسكوب غير التفاعلي."
slug: "tunnel-creation"
aliases: 
category: "التصميم"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## نظرة عامة

ملاحظة: مُهمل - هذه هي مواصفات إنشاء tunnel باستخدام ElGamal. راجع [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) لمواصفات إنشاء tunnel باستخدام X25519.

هذا المستند يحدد تفاصيل رسائل بناء tunnel المشفرة المستخدمة لإنشاء tunnels باستخدام طريقة "التلسكوب غير التفاعلي". راجع مستند بناء tunnel [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) للحصول على نظرة عامة على العملية، بما في ذلك طرق اختيار وترتيب الأقران.

يتم إنشاء tunnel من خلال رسالة واحدة تمرر عبر مسار الأقران في tunnel، يتم إعادة كتابتها في المكان نفسه، وإرسالها مرة أخرى إلى منشئ tunnel. تتكون رسالة tunnel الواحدة هذه من عدد متغير من السجلات (حتى 8) - واحد لكل قرين محتمل في tunnel. يتم تشفير السجلات الفردية بشكل غير متماثل (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) ليتم قراءتها فقط من قبل قرين محدد على طول المسار، بينما يتم إضافة طبقة إضافية من التشفير المتماثل (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) في كل قفزة بحيث يتم كشف السجل المشفر بشكل غير متماثل فقط في الوقت المناسب.

### عدد السجلات

ليس من الضروري أن تحتوي جميع السجلات على بيانات صالحة. رسالة البناء الخاصة بـ tunnel من 3 قفزات، على سبيل المثال، قد تحتوي على سجلات أكثر لإخفاء الطول الفعلي للـ tunnel عن المشاركين. هناك نوعان من رسائل البناء. رسالة Tunnel Build Message الأصلية ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) تحتوي على 8 سجلات، وهو ما يكفي أكثر من اللازم لأي طول tunnel عملي. رسالة Variable Tunnel Build Message الأحدث ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) تحتوي على 1 إلى 8 سجلات. يمكن للمُرسِل الموازنة بين حجم الرسالة والمقدار المطلوب من إخفاء طول الـ tunnel.

في الشبكة الحالية، معظم الـ tunnels يبلغ طولها 2 أو 3 قفزات. التنفيذ الحالي يستخدم VTBM من 5 سجلات لبناء tunnels بطول 4 قفزات أو أقل، وTBM من 8 سجلات للـ tunnels الأطول. إن VTBM من 5 سجلات (والذي عند تجزئته يناسب ثلاث رسائل tunnel بحجم 1 كيلوبايت) يقلل من حركة الشبكة ويزيد من معدل نجاح البناء، لأن الرسائل الأصغر أقل عرضة للإسقاط.

يجب أن تكون رسالة الرد من نفس النوع والطول مثل رسالة البناء.

### مواصفات سجل الطلب

محدد أيضاً في مواصفات I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

النص الواضح للسجل، مرئي فقط للـ hop المطلوب منه:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
تُستخدم حقول معرف tunnel التالي وهاش هوية router التالي لتحديد القفزة التالية في tunnel، على الرغم من أنه بالنسبة لنقطة نهاية tunnel الصادر، فإنها تحدد أين يجب إرسال رسالة الرد المُعاد كتابتها لإنشاء tunnel. بالإضافة إلى ذلك، يحدد معرف الرسالة التالي معرف الرسالة الذي يجب أن تستخدمه الرسالة (أو الرد).

مفتاح طبقة tunnel ومفتاح tunnel IV ومفتاح الرد و IV الرد هي قيم عشوائية مكونة من 32 بايت لكل منها، يتم إنشاؤها بواسطة المنشئ، للاستخدام في سجل طلب البناء هذا فقط.

يحتوي حقل الأعلام على ما يلي (ترتيب البت: 76543210، البت 7 هو MSB):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
البت 7 يشير إلى أن القفزة ستكون بوابة داخلية (IBGW). البت 6 يشير إلى أن القفزة ستكون نقطة نهاية خارجية (OBEP). إذا لم يتم تعيين أي من البتين، ستكون القفزة مشاركًا وسطيًا. لا يمكن تعيين كلاهما في نفس الوقت.

#### إنشاء سجل الطلب

كل hop يحصل على Tunnel ID عشوائي، غير صفر. يتم ملء Tunnel IDs الحالي والخاص بالhop التالي. كل سجل يحصل على مفتاح tunnel IV عشوائي، ومفتاح reply IV، ومفتاح layer، ومفتاح reply.

#### تشفير سجل الطلب

يتم تشفير سجل النص الواضح هذا بـ ElGamal 2048 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) باستخدام مفتاح التشفير العام للقفزة وتنسيقه في سجل بحجم 528 بايت:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
في السجل المشفر بحجم 512 بايت، تحتوي بيانات ElGamal على البايتات 1-256 و 258-513 من كتلة ElGamal المشفرة بحجم 514 بايت [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). يتم إزالة بايتَي الحشو من الكتلة (البايتات الصفرية في المواقع 0 و 257).

نظرًا لأن النص الواضح يستخدم الحقل الكامل، فلا توجد حاجة لحشو إضافي بعد `SHA256(cleartext) + cleartext`.

يتم بعد ذلك تشفير كل سجل بحجم 528 بايت بشكل تكراري (باستخدام فك تشفير AES، مع مفتاح الرد و IV الرد لكل hop) بحيث تكون هوية الـ router واضحة النص فقط للـ hop المعني.

### معالجة وتشفير القفزات

عندما يستقبل hop رسالة TunnelBuildMessage، فإنه يبحث في السجلات الموجودة بداخلها عن واحد يبدأ بـ identity hash الخاص به (مقطوع إلى 16 بايت). ثم يقوم بفك تشفير كتلة ElGamal من ذلك السجل ويسترجع النص المحمي الواضح. في تلك النقطة، يتأكد من أن طلب tunnel ليس مكرراً عبر تمرير مفتاح الرد AES-256 في مرشح Bloom. الطلبات المكررة أو غير الصالحة يتم إسقاطها. السجلات التي لا تحمل طابع الساعة الحالية، أو الساعة السابقة إذا كان الوقت قريباً من بداية الساعة، يجب إسقاطها. على سبيل المثال، خذ الساعة من timestamp، حولها إلى وقت كامل، ثم إذا كانت أكثر من 65 دقيقة متأخرة أو 5 دقائق متقدمة عن الوقت الحالي، فهي غير صالحة. مرشح Bloom يجب أن يكون له مدة لا تقل عن ساعة واحدة (بالإضافة إلى بضع دقائق، للسماح بانحراف الساعة)، بحيث أن السجلات المكررة في الساعة الحالية التي لا يتم رفضها عبر فحص timestamp الساعة في السجل، سيتم رفضها بواسطة المرشح.

بعد أن يقرروا ما إذا كانوا سيوافقون على المشاركة في tunnel أم لا، يستبدلون السجل الذي كان يحتوي على الطلب بكتلة رد مشفرة. يتم تشفير جميع السجلات الأخرى باستخدام AES-256 [CRYPTO-AES](/docs/specs/cryptography/#aes) مع مفتاح الرد وال IV المضمنين. يتم تشفير كل منها بـ AES/CBC بشكل منفصل باستخدام نفس مفتاح الرد ورد IV. لا يتم استمرار (ربط) وضع CBC عبر السجلات.

كل hop يعرف فقط استجابته الخاصة. إذا وافق، فسيحافظ على tunnel حتى انتهاء صلاحيته، حتى لو لم يتم استخدامه، حيث لا يمكنه معرفة ما إذا كانت جميع hops الأخرى قد وافقت.

#### مواصفة سجل الرد

بعد أن يقرأ الـ hop الحالي سجله، يستبدله بسجل رد يوضح ما إذا كان يوافق على المشاركة في النفق أم لا، وإذا كان لا يوافق، فإنه يصنف سبب الرفض. هذا ببساطة قيمة من 1 بايت، حيث 0x0 تعني أنهم يوافقون على المشاركة في النفق، والقيم الأعلى تعني مستويات أعلى من الرفض.

أكواد الرفض التالية محددة:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

لإخفاء الأسباب الأخرى، مثل إغلاق router، عن الأقران، يستخدم التنفيذ الحالي TUNNEL_REJECT_BANDWIDTH لرفض معظم الطلبات.

يتم تشفير الرد باستخدام مفتاح جلسة AES المُرسل إليه في الكتلة المشفرة، مع إضافة 495 بايت من البيانات العشوائية للوصول إلى حجم السجل الكامل. يتم وضع الحشو قبل بايت الحالة:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
هذا موصوف أيضاً في مواصفات I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

### إعداد رسالة بناء الـ tunnel

عند بناء رسالة Tunnel Build جديدة، يجب أولاً بناء جميع سجلات Build Request وتشفيرها بشكل غير متماثل باستخدام ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). ثم يتم فك تشفير كل سجل مسبقاً باستخدام مفاتيح الرد وIVs الخاصة بالقفزات السابقة في المسار، باستخدام AES [CRYPTO-AES](/docs/specs/cryptography/#aes). يجب تشغيل فك التشفير هذا بترتيب عكسي بحيث تظهر البيانات المشفرة بشكل غير متماثل بوضوح في القفزة الصحيحة بعد أن يقوم سلفها بتشفيرها.

السجلات الزائدة غير المطلوبة للطلبات الفردية يتم ملؤها ببساطة ببيانات عشوائية من قبل المنشئ.

### تسليم رسالة بناء النفق

بالنسبة لل tunnels الصادرة، يتم التسليم مباشرة من منشئ ال tunnel إلى القفزة الأولى، حيث يتم تغليف TunnelBuildMessage كما لو كان المنشئ مجرد قفزة أخرى في ال tunnel. بالنسبة لل tunnels الواردة، يتم التسليم من خلال tunnel صادر موجود. ال tunnel الصادر يكون عمومًا من نفس المجموعة التي ينتمي إليها ال tunnel الجديد الذي يتم بناؤه. إذا لم يكن هناك tunnel صادر متاح في تلك المجموعة، يتم استخدام tunnel استكشافي صادر. عند بدء التشغيل، عندما لا يوجد بعد tunnel استكشافي صادر، يتم استخدام tunnel صادر وهمي من 0 قفزة.

### التعامل مع نقطة نهاية رسالة بناء الـ tunnel

لإنشاء tunnel صادر، عندما يصل الطلب إلى نقطة نهاية صادرة (كما يحدده علامة 'السماح للرسائل لأي شخص')، تتم معالجة الـ hop كالمعتاد، مع تشفير رد مكان السجل وتشفير جميع السجلات الأخرى، ولكن نظراً لعدم وجود 'hop تالي' لتمرير TunnelBuildMessage إليه، فإنه بدلاً من ذلك يضع سجلات الرد المشفرة في TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) أو VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) (يجب أن يتطابق نوع الرسالة وعدد السجلات مع الطلب) ويسلمها إلى tunnel الرد المحدد داخل سجل الطلب. يقوم tunnel الرد هذا بتمرير Tunnel Build Reply Message مرة أخرى إلى منشئ الـ tunnel، تماماً كما هو الحال مع أي رسالة أخرى [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). يقوم منشئ الـ tunnel بعد ذلك بمعالجتها، كما هو موضح أدناه.

تم اختيار tunnel الرد من قبل المنشئ كما يلي: عمومًا يكون tunnel وارد من نفس المجموعة الخاصة بـ tunnel الصادر الجديد الذي يتم بناؤه. إذا لم يكن هناك tunnel وارد متاح في تلك المجموعة، يتم استخدام tunnel استكشافي وارد. عند بدء التشغيل، عندما لا يوجد بعد tunnel استكشافي وارد، يتم استخدام tunnel وارد وهمي بـ 0 قفزة.

لإنشاء tunnel وارد، عندما يصل الطلب إلى نقطة النهاية الواردة (المعروفة أيضاً باسم منشئ tunnel)، لا توجد حاجة لتوليد رسالة رد إنشاء tunnel صريحة، ويقوم router بمعالجة كل من الردود، كما هو موضح أدناه.

### معالجة رسالة رد بناء Tunnel

لمعالجة سجلات الرد، يحتاج المنشئ ببساطة إلى فك تشفير AES لكل سجل بشكل منفرد، باستخدام مفتاح الرد و IV الخاص بكل قفزة في tunnel بعد النظير (بترتيب عكسي). هذا يكشف الرد الذي يحدد ما إذا كانوا يوافقون على المشاركة في tunnel أم لا ولماذا يرفضون. إذا وافق الجميع، يُعتبر tunnel منشأً ويمكن استخدامه فوراً، ولكن إذا رفض أي شخص، فإن tunnel يتم التخلص منه.

يتم تسجيل الموافقات والرفض في ملف تعريف كل peer [PEER-SELECTION](/docs/overview/tunnel-routing/)، لاستخدامها في التقييمات المستقبلية لسعة tunnel الخاصة بالـ peer.

## التاريخ والملاحظات

نشأت هذه الاستراتيجية خلال نقاش على قائمة I2P البريدية بين مايكل روجرز وماثيو توسلاند (toad) وjrandom بخصوص هجوم predecessor. انظر [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)، [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html). تم تقديمها في الإصدار 0.6.1.10 في 16-02-2006، والذي كان آخر مرة تم إجراء تغيير غير متوافق مع الإصدارات السابقة في I2P.

ملاحظات:

- هذا التصميم لا يمنع اثنين من الأقران العدائيين داخل tunnel من وضع علامات على واحد أو أكثر من سجلات الطلب أو الرد لاكتشاف أنهما داخل نفس الـ tunnel، ولكن القيام بذلك يمكن اكتشافه من قبل منشئ الـ tunnel عند قراءة الرد، مما يسبب وضع علامة على الـ tunnel كغير صالح.
- هذا التصميم لا يتضمن إثبات عمل على القسم المشفر بشكل غير متماثل، رغم أن الـ identity hash المكون من 16 بايت يمكن قطعه إلى النصف مع استبدال الجزء الأخير بدالة hashcash بتكلفة تصل إلى 2^64.
- هذا التصميم وحده لا يمنع اثنين من الأقران العدائيين داخل tunnel من استخدام معلومات التوقيت لتحديد ما إذا كانا في نفس الـ tunnel. استخدام تسليم الطلبات المجمّع والمتزامن يمكن أن يساعد (تجميع الطلبات وإرسالها في الدقيقة المتزامنة مع ntp). ومع ذلك، القيام بذلك يتيح للأقران 'وضع علامات' على الطلبات عن طريق تأخيرها واكتشاف التأخير لاحقاً في الـ tunnel، رغم أن إسقاط الطلبات غير المسلمة في نافزة زمنية صغيرة ربما يعمل (رغم أن القيام بذلك سيتطلب درجة عالية من تزامن الساعة). بدلاً من ذلك، ربما يمكن للقفزات الفردية حقن تأخير عشوائي قبل توجيه الطلب؟
- هل هناك أي طرق غير مميتة لوضع علامات على الطلب؟
- الطابع الزمني بدقة ساعة واحدة يُستخدم لمنع إعادة التشغيل. لم يتم فرض هذا القيد حتى الإصدار 0.9.16.

## العمل المستقبلي

- في التنفيذ الحالي، يترك المرسل سجلاً واحداً فارغاً لنفسه. وبالتالي فإن رسالة من n سجل يمكنها فقط بناء tunnel من n-1 قفزة. يبدو أن هذا ضروري للـ inbound tunnels (حيث يمكن للقفزة قبل الأخيرة رؤية بادئة الـ hash للقفزة التالية)، ولكن ليس للـ outbound tunnels. هذا يحتاج إلى بحث والتحقق منه. إذا كان من الممكن استخدام السجل المتبقي دون المساس بإخفاء الهوية، فيجب أن نفعل ذلك.
- مزيد من التحليل لهجمات الوسم والتوقيت المحتملة الموصوفة في الملاحظات أعلاه.
- استخدام VTBM فقط؛ عدم اختيار النظراء القدامى الذين لا يدعمونه.
- Build Request Record لا يحدد عمر tunnel أو انتهاء الصلاحية؛ كل قفزة تنهي صلاحية الـ tunnel بعد 10 دقائق، وهو ثابت مُرمّز في الشبكة بالكامل. يمكننا استخدام بت في حقل العلم وأخذ 4 (أو 8) بايت من الحشو لتحديد عمر أو انتهاء صلاحية. المطالب سيحدد هذا الخيار فقط إذا كان جميع المشاركين يدعمونه.

## المراجع

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - مواصفات BuildRequestRecord
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - تشفير AES
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - تشفير ElGamal
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage

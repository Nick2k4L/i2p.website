---
title: "مواصفات SSU2"
description: "بروتوكول النقل الآمن شبه الموثوق UDP الإصدار 2"
slug: "ssu2"
category: "وسائل النقل"
lastUpdated: "2025-04"
accurateFor: "0.9.65"
---

## الحالة

مكتمل بشكل كبير. راجع [Prop159](/proposals/159-ssu2) للحصول على خلفية وأهداف إضافية، بما في ذلك التحليل الأمني ونماذج التهديد ومراجعة أمان SSU 1 والمشاكل المتعلقة بها ومقتطفات من مواصفات QUIC.

خطة الطرح:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
تتضمن الجلسة الأساسية مرحلة المصافحة ومرحلة البيانات. يتضمن البروتوكول الموسع التتابع واختبار النظير.

## نظرة عامة

تحدد هذه المواصفة بروتوكول اتفاق مفاتيح مُصادق عليه لتحسين مقاومة [SSU](/docs/transport/ssu) لأشكال مختلفة من التحديد الآلي والهجمات.

كما هو الحال مع بروتوكولات النقل الأخرى في I2P، تم تصميم SSU2 للنقل النقطة-إلى-النقطة (router-to-router) لرسائل I2NP. وهو ليس أنبوب بيانات للاستخدام العام. مثل [SSU](/docs/transport/ssu)، يوفر أيضاً خدمتين إضافيتين: التمرير للتغلب على NAT، واختبار النظراء لتحديد إمكانية الوصول الداخلي. كما يوفر خدمة ثالثة غير موجودة في SSU، وهي ترحيل الاتصال عندما يقوم نظير بتغيير عنوان IP أو المنفذ.

## نظرة عامة على التصميم

### ملخص

نعتمد على عدة بروتوكولات موجودة، سواء داخل I2P أو المعايير الخارجية، للحصول على الإلهام والتوجيه وإعادة استخدام الكود:

- نماذج التهديد: من NTCP2 [NTCP2](/docs/specs/ntcp2)، مع تهديدات إضافية كبيرة ذات صلة بنقل UDP كما تم تحليلها بواسطة QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- الخيارات التشفيرية: من [NTCP2](/docs/specs/ntcp2).
- المصافحة: Noise XK من [NTCP2](/docs/specs/ntcp2) و [NOISE](https://noiseprotocol.org/noise.html). تبسيطات كبيرة لـ NTCP2 ممكنة بسبب التغليف (حدود الرسائل المتأصلة) المقدمة بواسطة UDP.
- إخفاء المفتاح المؤقت للمصافحة: مُقتبس من [NTCP2](/docs/specs/ntcp2) لكن باستخدام ChaCha20 من [ECIES](/docs/specs/ecies) بدلاً من AES.
- رؤوس الحزم: مُقتبسة من WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) و QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- إخفاء رؤوس الحزم: مُقتبس من [NTCP2](/docs/specs/ntcp2) لكن باستخدام ChaCha20 من [ECIES](/docs/specs/ecies) بدلاً من AES.
- حماية رؤوس الحزم: مُقتبسة من QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) و [Nonces](https://eprint.iacr.org/2019/624.pdf)
- الرؤوس المستخدمة كبيانات مرتبطة AEAD كما في [ECIES](/docs/specs/ecies).
- ترقيم الحزم: مُقتبس من WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) و QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- الرسائل: مُقتبسة من [SSU](/docs/transport/ssu)
- تجزئة I2NP: مُقتبسة من [SSU](/docs/transport/ssu)
- التتابع واختبار النظير: مُقتبسان من [SSU](/docs/transport/ssu)
- توقيعات بيانات التتابع واختبار النظير: من مواصفات الهياكل المشتركة [Common](/docs/specs/common-structures)
- تنسيق الكتلة: من [NTCP2](/docs/specs/ntcp2) و [ECIES](/docs/specs/ecies).
- الحشو والخيارات: من [NTCP2](/docs/specs/ntcp2) و [ECIES](/docs/specs/ecies).
- إقرارات الاستلام والرفض: مُقتبسة من QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- التحكم في التدفق: سيتم تحديدها لاحقاً

لا توجد عمليات تشفيرية أولية جديدة لم يتم استخدامها في I2P من قبل.

### ضمانات التسليم

كما هو الحال مع وسائل النقل الأخرى في I2P مثل NTCP و NTCP2 و SSU 1، فإن وسيلة النقل هذه ليست مرفقاً عام الغرض لتوصيل تدفق مرتب من البايتات. إنها مصممة لنقل رسائل I2NP. لا يتم توفير تجريد "التدفق".

بالإضافة إلى ذلك، كما هو الحال مع SSU، فإنه يحتوي على تسهيلات إضافية لاجتياز NAT بمساعدة النظراء واختبار قابلية الوصول (الاتصالات الواردة).

بالنسبة لـ SSU 1، فإنه لا يوفر التسليم المرتب لرسائل I2NP. كما أنه لا يوفر التسليم المضمون لرسائل I2NP. من أجل الكفاءة، أو بسبب التسليم غير المرتب لحزم UDP أو فقدان تلك الحزم، قد يتم تسليم رسائل I2NP إلى الطرف البعيد بشكل غير مرتب، أو قد لا يتم تسليمها على الإطلاق. قد يتم إعادة إرسال رسالة I2NP عدة مرات إذا لزم الأمر، لكن التسليم قد يفشل في النهاية دون التسبب في قطع الاتصال الكامل. أيضاً، قد تستمر رسائل I2NP الجديدة في الإرسال حتى أثناء حدوث إعادة الإرسال (استرداد المفقود) لرسائل I2NP أخرى.

هذا البروتوكول لا يمنع بشكل كامل التسليم المكرر لرسائل I2NP. يجب على الـ router أن يفرض انتهاء صلاحية I2NP وأن يستخدم مرشح Bloom أو آلية أخرى مبنية على معرف رسالة I2NP. راجع قسم تكرار رسائل I2NP أدناه.

### إطار عمل بروتوكول Noise

تحدد هذه المواصفة المتطلبات المبنية على إطار عمل بروتوكول Noise [NOISE](https://noiseprotocol.org/noise.html) (المراجعة 33، 2017-10-04). يتمتع Noise بخصائص مماثلة لبروتوكول Station-To-Station [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol)، والذي يشكل الأساس لبروتوكول [SSU](/docs/transport/ssu). في مصطلحات Noise، Alice هي الطرف البادئ، و Bob هو الطرف المجيب.

يعتمد SSU2 على بروتوكول Noise وهو Noise_XK_25519_ChaChaPoly_SHA256. (المعرف الفعلي لدالة اشتقاق المفتاح الأولية هو "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" للإشارة إلى إضافات I2P - انظر قسم KDF 1 أدناه)

ملاحظة: هذا المعرف مختلف عن المستخدم في NTCP2، لأن جميع رسائل المصافحة الثلاث تستخدم الرأس كبيانات مرتبطة.

يستخدم بروتوكول Noise هذا العناصر الأساسية التالية:

- نمط المصافحة: XK أليس ترسل مفتاحها إلى بوب (X) أليس تعرف المفتاح الثابت لبوب مسبقاً (K)
- دالة DH: X25519 X25519 DH بطول مفتاح 32 بايت كما هو محدد في [RFC-7748](https://tools.ietf.org/html/rfc7748).
- دالة التشفير: ChaChaPoly AEAD_CHACHA20_POLY1305 كما هو محدد في [RFC-7539](https://tools.ietf.org/html/rfc7539) القسم 2.8. nonce بحجم 12 بايت، مع تعيين أول 4 بايتات إلى صفر.
- دالة التجزئة: SHA256 تجزئة قياسية بحجم 32 بايت، مستخدمة بالفعل على نطاق واسع في I2P.

### إضافات إلى الإطار

تحدد هذه المواصفة التحسينات التالية لـ Noise_XK_25519_ChaChaPoly_SHA256. هذه التحسينات تتبع بشكل عام الإرشادات الموجودة في القسم 13 من [NOISE](https://noiseprotocol.org/noise.html).

1) رسائل المصافحة (Session Request، Created، Confirmed) تتضمن رأس بحجم 16 أو 32 بايت. 2) رؤوس رسائل المصافحة (Session Request، Created، Confirmed) تُستخدم كمدخل لـ mixHash() قبل التشفير/فك التشفير لربط الرؤوس بالرسالة. 3) الرؤوس مشفرة ومحمية. 4) المفاتيح المؤقتة الواضحة مُبهمة بتشفير ChaCha20 باستخدام مفتاح و IV معروفين. هذا أسرع من elligator2. 5) تنسيق الحمولة محدد للرسائل 1، 2، ومرحلة البيانات. بالطبع، هذا غير محدد في Noise.

تستخدم مرحلة البيانات تشفيراً مشابهاً لمرحلة بيانات Noise، لكنه غير متوافق معها.

## التعريفات

نحدد الدوال التالية التي تتوافق مع الكتل البنائية المشفرة المستخدمة.

ZEROLEN

:   مصفوفة بايت بطول صفر

H(p, d)

:   دالة hash SHA-256 التي تأخذ سلسلة تخصيص p وبيانات d، وتنتج مخرجات بطول 32 بايت. كما هو محدد في [NOISE](https://noiseprotocol.org/noise.html). || أدناه تعني الإلحاق.

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

MixHash(d)

:   دالة hash SHA-256 التي تأخذ hash سابق h وبيانات جديدة d، وتنتج مخرجات بطول 32 بايت. || أدناه تعني إلحاق.

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

STREAM

:   ChaCha20/Poly1305 AEAD كما هو محدد في [RFC-7539](https://tools.ietf.org/html/rfc7539). S_KEY_LEN = 32 و S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

DH

:   نظام اتفاق المفاتيح العامة X25519. مفاتيح خاصة بحجم 32 بايت، مفاتيح عامة بحجم 32 بايت، ينتج مخرجات بحجم 32 بايت. يحتوي على الوظائف التالية:

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

HKDF(salt, ikm, info, n)

:   دالة اشتقاق مفاتيح تشفيرية تأخذ مادة مفتاح إدخال ikm (التي يجب أن تحتوي على إنتروبيا جيدة ولكن ليس مطلوباً أن تكون سلسلة عشوائية موحدة)، وملح بطول 32 بايت، وقيمة 'info' خاصة بالسياق، وتنتج مخرجات بحجم n بايت مناسبة للاستخدام كمادة مفاتيح.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

MixKey(d)

:   استخدم HKDF() مع chainKey سابق وبيانات جديدة d، ويضبط chainKey الجديد و k. كما هو محدد في [NOISE](https://noiseprotocol.org/noise.html).

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## الرسائل

تحتوي كل UDP datagram على رسالة واحدة بالضبط. طول الـ datagram (بعد رؤوس IP و UDP) هو طول الرسالة. الحشو، إن وُجد، يكون موجوداً في كتلة حشو داخل الرسالة. في هذا المستند، نستخدم مصطلحي "datagram" و "packet" بشكل متبادل في الغالب. كل datagram (أو packet) يحتوي على رسالة واحدة (على عكس QUIC، حيث قد يحتوي الـ datagram على عدة QUIC packets). "رأس الحزمة" هو الجزء الذي يأتي بعد رأس IP/UDP.

استثناء: رسالة Session Confirmed فريدة من نوعها في أنه يمكن تقسيمها إلى عدة حزم. راجع قسم Session Confirmed Fragmentation أدناه لمزيد من المعلومات.

جميع رسائل SSU2 يبلغ طولها 40 بايت على الأقل. أي رسالة بطول 1-39 بايت تعتبر غير صالحة. جميع رسائل SSU2 أقل من أو تساوي 1472 (IPv4) أو 1452 (IPv6) بايت في الطول. تعتمد صيغة الرسالة على رسائل Noise، مع تعديلات للتأطير وعدم القابلية للتمييز. التطبيقات التي تستخدم مكتبات Noise القياسية يجب أن تقوم بمعالجة مسبقة للرسائل المستلمة لتحويلها إلى صيغة رسالة Noise القياسية. جميع الحقول المشفرة هي نصوص مشفرة AEAD.

الرسائل التالية محددة:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### إنشاء الجلسة

تسلسل التأسيس المعياري، عندما تمتلك Alice رمزاً صالحاً تم استلامه مسبقاً من Bob، هو كما يلي:

```
Alice Bob

SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
عندما لا تملك Alice رمزًا صالحًا، تكون تسلسل عملية الإنشاء كما يلي:

```
Alice Bob

TokenRequest ---------------------> <--------------------------- Retry SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
عندما تعتقد Alice أن لديها رمز صالح، ولكن Bob يرفضه (ربما لأن Bob أعاد التشغيل)، فإن تسلسل التأسيس يكون كما يلي:

```
Alice Bob

SessionRequest -------------------> <--------------------------- Retry SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
قد يرفض Bob طلب Session أو Token من خلال الرد برسالة Retry تحتوي على كتلة Termination مع رمز السبب. بناءً على رمز السبب، يجب على Alice عدم محاولة طلب آخر لفترة زمنية معينة:

```
Alice Bob

SessionRequest -------------------> <--------------------------- Retry containing a Termination block

or

TokenRequest ---------------------> <--------------------------- Retry containing a Termination block
```
باستخدام مصطلحات Noise، تسلسل التأسيس والبيانات كما يلي: (خصائص أمان الحمولة)

```
XK(s, rs): Authentication Confidentiality

<- s \... -> e, es 0 2 <- e, ee 2 1 -> s, se 2 5 <- 2 5
```
بمجرد إنشاء جلسة، يمكن لأليس وبوب تبادل رسائل البيانات.

### رأس الحزمة

تبدأ جميع الحزم برأس مُشوّش (مُشفّر). يوجد نوعان من الرؤوس، طويل وقصير. لاحظ أن البايتات الثلاثة عشر الأولى (معرف اتصال الوجهة، رقم الحزمة، والنوع) متشابهة لجميع الرؤوس.

#### رأس طويل

الرأس الطويل يبلغ 32 بايت. يُستخدم قبل إنشاء الجلسة، لطلب الرمز المميز، وطلب الجلسة، وإنشاء الجلسة، وإعادة المحاولة. كما يُستخدم أيضاً لرسائل اختبار النظير وخرق الثقب خارج الجلسة.

قبل تشفير الرأس:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+----------+----------+----------+
    | > Packet Number                           | type     | ver      | id       | flag     |
    +-------------------------------------------+----------+----------+----------+----------+
    | > Source Connection ID                                                                |
    +---------------------------------------------------------------------------------------+
    | > Token                                                                               |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, unsigned big endian integer

    type :: The message type = 0, 1, 7, 9, 10, or 11

    ver :: The protocol version, equal to 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: 8 bytes, unsigned big endian integer

    Token :: 8 bytes, unsigned big endian integer
```
#### رأس قصير

الرأس القصير يبلغ 16 بايت. يتم استخدامه لرسائل Session Created ولرسائل البيانات. الرسائل غير المصادق عليها مثل Session Request وRetry وPeer Test ستستخدم دائماً الرأس الطويل.

يتطلب الأمر 16 بايت، لأن المستقبل يجب أن يفك تشفير أول 16 بايت للحصول على نوع الرسالة، ثم يجب أن يفك تشفير 16 بايت إضافية إذا كان في الواقع رأسًا طويلًا، كما يشير إليه نوع الرسالة.

بالنسبة لـ Session Confirmed، قبل تشفير الرأس:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------+------+------+-------------+
    | > Packet Number                   | type | frag | > flags     |
    +-----------------------------------+------+------+-------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, all zeros

    type :: The message type = 2

    frag :: 1 byte fragment info:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number 0-14, big endian bits 3-0: total fragments 1-15, big endian

    flags :: 2 bytes, unused, set to 0 for future compatibility
```
راجع قسم تجزئة الجلسة المؤكدة أدناه للحصول على مزيد من المعلومات حول حقل frag.

لرسائل البيانات، قبل تشفير الرأس:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------+------+------+---------------+
    | > Packet Number                   | type | flag | moreflags     |
    +-----------------------------------+------+------+---------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, unsigned big endian integer

    type :: The message type = 6

    flag :: 1 byte flags:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-1: unused, set to 0 for future compatibility bits 0: when set to 1, immediate ack requested

    moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### ترقيم معرف الاتصال

يجب أن تكون معرفات الاتصال مُولدة عشوائياً. يجب ألا تكون معرفات المصدر والوجهة متطابقة، بحيث لا يستطيع المهاجم الموجود على المسار التقاط الحزمة وإرسالها مرة أخرى إلى المُرسِل الأصلي بشكل يبدو صالحاً. لا تستخدم عداد لتوليد معرفات الاتصال، حتى لا يستطيع المهاجم الموجود على المسار توليد حزمة تبدو صالحة.

على عكس QUIC، نحن لا نغير معرفات الاتصال أثناء أو بعد المصافحة، حتى بعد رسالة إعادة المحاولة. تبقى المعرفات ثابتة من الرسالة الأولى (طلب الرمز المميز أو طلب الجلسة) إلى الرسالة الأخيرة (البيانات مع الإنهاء). بالإضافة إلى ذلك، لا تتغير معرفات الاتصال أثناء أو بعد تحدي المسار أو ترحيل الاتصال.

كما يختلف أيضاً عن QUIC في أن معرفات الاتصال في العناوين مشفرة دائماً على مستوى العنوان. انظر أدناه.

#### ترقيم الحزم

إذا لم يتم إرسال كتلة رقم الحزمة الأولى في المصافحة، يتم ترقيم الحزم داخل جلسة واحدة، لكل اتجاه، بدءاً من 0، إلى حد أقصى قدره (2**32 -1). يجب إنهاء الجلسة وإنشاء جلسة جديدة، قبل إرسال العدد الأقصى من الحزم بوقت كافٍ.

إذا تم إرسال كتلة رقم الحزمة الأولى في المصافحة، فسيتم ترقيم الحزم داخل جلسة واحدة، لذلك الاتجاه، بدءاً من رقم تلك الحزمة. قد يلتف رقم الحزمة أثناء الجلسة. عندما يتم إرسال حد أقصى من 2**32 حزمة، مما يؤدي إلى التفاف رقم الحزمة مرة أخرى إلى رقم الحزمة الأولى، فإن تلك الجلسة لم تعد صالحة. يجب إنهاء الجلسة وإنشاء جلسة جديدة، قبل وقت طويل من إرسال العدد الأقصى من الحزم.

TODO تدوير المفاتيح، تقليل أقصى رقم حزمة؟

يتم إعادة إرسال حزم المصافحة المحددة كمفقودة بالكامل، مع رأس مطابق يتضمن رقم الحزمة. يجب إعادة إرسال رسائل المصافحة Session Request و Session Created و Session Confirmed بنفس رقم الحزمة ونفس المحتوى المشفر، بحيث يتم استخدام نفس hash المتسلسل لتشفير الاستجابة. رسالة Retry لا يتم إرسالها أبداً.

حزم مرحلة البيانات التي يتم تحديد أنها مفقودة لا يعاد إرسالها كاملة أبداً (باستثناء الإنهاء، انظر أدناه). ينطبق الأمر نفسه على الكتل الموجودة داخل الحزم المفقودة. بدلاً من ذلك، يتم إرسال المعلومات التي قد تحملها الكتل مرة أخرى في حزم جديدة حسب الحاجة. حزم البيانات لا يعاد إرسالها أبداً بنفس رقم الحزمة. أي إعادة إرسال لمحتويات الحزمة (سواء بقي المحتوى كما هو أم لا) يجب أن يستخدم رقم الحزمة التالي غير المستخدم.

إعادة إرسال حزمة كاملة غير متغيرة كما هي، بنفس رقم الحزمة، غير مسموح لعدة أسباب. للخلفية انظر QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) القسم 12.3.

- من غير الفعال تخزين الحزم لإعادة الإرسال
- بيانات الحزمة الجديدة تبدو مختلفة لمراقب في المسار، لا يمكن معرفة أنها معاد إرسالها
- الحزمة الجديدة تحصل على كتلة إقرار محدثة ترسل معها، وليس كتلة الإقرار القديمة
- تعيد إرسال ما هو ضروري فقط. بعض الأجزاء قد تكون أعيد إرسالها مرة واحدة بالفعل وتم إقرارها
- يمكنك ملء كل حزمة معاد إرسالها بما تحتاجه إذا كان هناك المزيد في الانتظار
- النقاط النهائية التي تتتبع جميع الحزم الفردية لأغراض اكتشاف التكرارات معرضة لخطر تراكم حالة مفرطة. يمكن تحديد البيانات المطلوبة لاكتشاف التكرارات بالحفاظ على رقم حزمة أدنى يتم إسقاط جميع الحزم تحته فوراً.
- هذا المخطط أكثر مرونة بكثير

تُستخدم الحزم الجديدة لحمل المعلومات التي تم تحديد أنها فُقدت. بشكل عام، يتم إرسال المعلومات مرة أخرى عندما يتم تحديد أن الحزمة التي تحتوي على تلك المعلومات قد فُقدت، ويتوقف الإرسال عندما يتم الإقرار بالحزمة التي تحتوي على تلك المعلومات (تبقى كما هي).

استثناء: يمكن إعادة إرسال حزمة مرحلة البيانات التي تحتوي على كتلة إنهاء كاملة كما هي، ولكن ذلك ليس مطلوباً. راجع قسم إنهاء الجلسة أدناه.

تحتوي الحزم التالية على رقم حزمة عشوائي يتم تجاهله:

- طلب الجلسة
- تم إنشاء الجلسة
- طلب الرمز المميز
- إعادة المحاولة
- اختبار النظير
- ثقب الشبكة

بالنسبة لأليس، يبدأ ترقيم الحزم الصادرة من 0 مع Session Confirmed. بالنسبة لبوب، يبدأ ترقيم الحزم الصادرة من 0 مع أول حزمة Data، والتي يجب أن تكون ACK للـ Session Confirmed. أرقام الحزم في مثال على المصافحة القياسية ستكون:

```
Alice Bob

SessionRequest (r) ------------> <------------- SessionCreated (r) SessionConfirmed (0) ------------> <------------- Data (0) (Ack-only) Data (1) ------------> (May be sent before Ack is received) <------------- Data (1) Data (2) ------------> Data (3) ------------> Data (4) ------------> <------------- Data (2)

r = random packet number (ignored) Token Request, Retry, and Peer Test also have random packet numbers.
```
يجب إعادة إرسال أي رسائل مصافحة (SessionRequest، SessionCreated، أو SessionConfirmed) دون تغيير، مع نفس رقم الحزمة. لا تستخدم مفاتيح مؤقتة مختلفة أو تغير الحمولة عند إعادة إرسال هذه الرسائل.

#### ربط الرأس

يتم دائماً تضمين الرأس (قبل التشويش والحماية) في البيانات المرتبطة لوظيفة AEAD، لربط الرأس بالبيانات تشفيرياً.

#### تشفير الرأس

تشفير الرأس له عدة أهداف. راجع قسم "مناقشة إضافية حول فحص الحزم العميق" أعلاه للخلفية والافتراضات.

- منع DPI عبر الإنترنت من تحديد البروتوكول
- منع الأنماط في سلسلة من الرسائل في نفس الاتصال، باستثناء إعادة إرسال handshake
- منع الأنماط في الرسائل من نفس النوع في اتصالات مختلفة
- منع فك تشفير رؤوس handshake بدون معرفة introduction key الموجود في netDb
- منع تحديد مفاتيح X25519 المؤقتة بدون معرفة introduction key الموجود في netDb
- منع فك تشفير رقم ونوع حزمة مرحلة البيانات من قبل أي مهاجم متصل أو غير متصل
- منع حقن حزم handshake صالحة من قبل مراقب على المسار أو خارج المسار بدون معرفة introduction key الموجود في netDb
- منع حقن حزم البيانات الصالحة من قبل مراقب على المسار أو خارج المسار
- السماح بتصنيف سريع وفعال للحزم الواردة
- توفير مقاومة "الاستطلاع" بحيث لا يكون هناك استجابة لطلب Session Request سيء، أو إذا كان هناك استجابة Retry، فإن الاستجابة غير قابلة للتحديد كـ I2P بدون معرفة introduction key الموجود في netDb
- Destination Connection ID ليس بيانات حرجة، ولا بأس إذا كان بإمكان فك تشفيره من قبل مراقب لديه معرفة بـ introduction key الموجود في netDb
- رقم الحزمة لحزمة مرحلة البيانات هو AEAD nonce وهو بيانات حرجة. يجب ألا يكون قابلاً لفك التشفير من قبل مراقب حتى مع معرفة introduction key الموجود في netDb. انظر [Nonces](https://eprint.iacr.org/2019/624.pdf).

يتم تشفير الرؤوس باستخدام مفاتيح معروفة منشورة في قاعدة بيانات الشبكة أو محسوبة لاحقاً. في مرحلة المصافحة، يكون هذا لمقاومة فحص الحزم العميق فقط، حيث أن المفتاح عام ويتم إعادة استخدام المفتاح والأرقام المستخدمة مرة واحدة، لذا فهو في الواقع مجرد تشويش. لاحظ أن تشفير الرؤوس يُستخدم أيضاً لتشويش المفاتيح المؤقتة X (في طلب الجلسة) و Y (في إنشاء الجلسة).

راجع قسم معالجة الحزم الواردة أدناه للحصول على إرشادات إضافية.

البايتات 0-15 من جميع الرؤوس مشفرة باستخدام مخطط حماية الرأس عن طريق XOR مع البيانات المحسوبة من المفاتيح المعروفة، باستخدام ChaCha20، مشابه لـ QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) و[Nonces](https://eprint.iacr.org/2019/624.pdf). هذا يضمن أن الرأس القصير المشفر والجزء الأول من الرأس الطويل سيظهران عشوائيين.

بالنسبة لـ Session Request و Session Created، يتم تشفير البايتات 16-31 من الـ long header ومفتاح Noise الـ ephemeral المكون من 32 بايت باستخدام ChaCha20. البيانات غير المشفرة عشوائية، لذلك ستبدو البيانات المشفرة عشوائية أيضاً.

بالنسبة للإعادة المحاولة، يتم تشفير البايتات 16-31 من الرأس الطويل باستخدام ChaCha20. البيانات غير المشفرة عشوائية، لذلك ستظهر البيانات المشفرة وكأنها عشوائية.

على عكس مخطط حماية رؤوس QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001)، فإن جميع أجزاء كافة الرؤوس، بما في ذلك معرفات الاتصال للوجهة والمصدر، مشفرة. يركز QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) و [Nonces](https://eprint.iacr.org/2019/624.pdf) بشكل أساسي على تشفير الجزء "الحرج" من الرأس، أي رقم الحزمة (ChaCha20 nonce). بينما يجعل تشفير معرف الجلسة تصنيف الحزم الواردة أكثر تعقيداً قليلاً، إلا أنه يجعل بعض الهجمات أصعب. يحدد QUIC معرفات اتصال مختلفة لمراحل مختلفة، ولتحدي المسار وترحيل الاتصال. هنا نستخدم نفس معرفات الاتصال طوال الوقت، لأنها مشفرة.

هناك سبع مراحل لمفاتيح حماية الرأس:

- طلب الجلسة وطلب الرمز المميز
- تم إنشاء الجلسة
- إعادة المحاولة
- تأكيد الجلسة
- مرحلة البيانات
- اختبار النظير
- ثقب الاتصال

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
تم تصميم تشفير الرؤوس للسماح بالتصنيف السريع للحزم الواردة، دون الحاجة لاستخدام خوارزميات معقدة أو بدائل احتياطية. يتم تحقيق ذلك باستخدام نفس مفتاح k_header_1 لجميع الرسائل الواردة تقريباً. حتى عندما يتغير عنوان IP المصدر أو المنفذ الخاص بالاتصال بسبب تغيير فعلي في عنوان IP أو سلوك NAT، يمكن ربط الحزمة بجلسة معينة بسرعة من خلال بحث واحد باستخدام معرف الاتصال.

لاحظ أن Session Created و Retry هما الرسالتان الوحيدتان اللتان تتطلبان معالجة احتياطية لـ k_header_1 لفك تشفير Connection ID، لأنهما يستخدمان مفتاح التقديم الخاص بالمرسل (Bob). جميع الرسائل الأخرى تستخدم مفتاح التقديم الخاص بالمستقبل لـ k_header_1. المعالجة الاحتياطية تحتاج فقط للبحث عن الاتصالات الصادرة المعلقة حسب IP/port المصدر.

إذا فشلت المعالجة الاحتياطية بواسطة IP/المنفذ المصدر في العثور على اتصال صادر معلق، فقد يكون هناك عدة أسباب:

- ليست رسالة SSU2
- رسالة SSU2 تالفة
- الرد مزيف أو معدل من قبل مهاجم
- Bob لديه NAT متماثل
- Bob غير IP أو المنفذ أثناء معالجة الرسالة
- Bob أرسل الرد عبر واجهة مختلفة

بينما يمكن إجراء معالجة احتياطية إضافية لمحاولة العثور على الاتصال الصادر المعلق وفك تشفير معرف الاتصال باستخدام k_header_1 لذلك الاتصال، فمن المحتمل أن ذلك غير ضروري. إذا كان لدى Bob مشاكل مع NAT الخاص به أو توجيه الحزم، فمن الأفضل على الأرجح السماح للاتصال بالفشل. يعتمد هذا التصميم على احتفاظ نقاط النهاية بعنوان مستقر طوال مدة المصافحة.

راجع قسم التعامل مع الحزم الواردة أدناه للحصول على إرشادات إضافية.

انظر أقسام KDF الفردية أدناه لاشتقاق مفاتيح تشفير الرأس لتلك المرحلة.

#### دالة اشتقاق المفتاح لتشفير الترويسة

```
// incoming encrypted packet

packet = incoming encrypted packet len = packet.length

    // take the next-to-last 12 bytes of the packet iv = packet[len-24:len-13] k_header_1 = header encryption key 1 data = {0, 0, 0, 0, 0, 0, 0, 0} mask = ChaCha20.encrypt(k_header_1, iv, data)

    // encrypt the first part of the header by XORing with the mask packet[0:7] \^= mask[0:7]

    // take the last 12 bytes of the packet iv = packet[len-12:len-1] k_header_2 = header encryption key 2 data = {0, 0, 0, 0, 0, 0, 0, 0} mask = ChaCha20.encrypt(k_header_2, iv, data)

    // encrypt the second part of the header by XORing with the mask packet[8:15] \^= mask[0:7]

    // For Session Request and Session Created only: iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

    // encrypt the third part of the header and the ephemeral key packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])

    // For Retry, Token Request, Peer Test, and Hole Punch only: iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

    // encrypt the third part of the header packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
تستخدم دالة اشتقاق المفاتيح هذه آخر 24 بايت من الحزمة كمتجه التهيئة لعمليتي ChaCha20. نظراً لأن جميع الحزم تنتهي بـ MAC من 16 بايت، فإن هذا يتطلب أن تكون جميع حمولات الحزم 8 بايت كحد أدنى. هذا المتطلب موثق أيضاً في أقسام الرسائل أدناه.

#### التحقق من صحة الرأس

بعد فك تشفير البايتات الثمانية الأولى من الرأس، سيعرف المستقبل معرف الاتصال الوجهة. من هناك، يعرف المستقبل أي مفتاح تشفير رأس يستخدم لباقي الرأس، بناءً على مرحلة المفتاح للجلسة.

فك تشفير الـ 8 بايتات التالية من الرأس سيكشف نوع الرسالة ويمكّن من تحديد ما إذا كان الرأس قصيراً أم طويلاً. إذا كان رأساً طويلاً، يجب على المستقبِل التحقق من صحة حقلي الإصدار وnetid. إذا كان الإصدار != 2، أو netid != القيمة المتوقعة (عادة 2، باستثناء شبكات الاختبار)، يجب على المستقبِل إسقاط الرسالة.

### سلامة الحزم

تحتوي جميع الرسائل على ثلاثة أو أربعة أجزاء:

- رأس الرسالة
- لـ Session Request و Session Created فقط، مفتاح مؤقت
- حمولة مشفرة بـ ChaCha20
- Poly1305 MAC

في جميع الحالات، يتم ربط الرأس (والمفتاح المؤقت إذا كان موجوداً) بـ MAC المصادقة لضمان سلامة الرسالة بأكملها.

- بالنسبة لرسائل المصافحة Session Request و Session Created و Session Confirmed، يتم تطبيق mixHash() على رأس الرسالة قبل مرحلة معالجة Noise
- المفتاح المؤقت، إن وُجد، يكون مغطى بواسطة misHash() المعياري لـ Noise
- بالنسبة للرسائل خارج مصافحة Noise، يُستخدم الرأس كبيانات مرتبطة لتشفير ChaCha20/Poly1305.

يجب على معالجات الحزم الواردة دائماً فك تشفير حمولة ChaCha20 والتحقق من صحة MAC قبل معالجة الرسالة، مع استثناء واحد: للتخفيف من هجمات DoS من الحزم المزيفة العنوان التي تحتوي على رسائل Session Request ظاهرية برمز مميز غير صالح، لا يحتاج المعالج لمحاولة فك التشفير والتحقق من صحة الرسالة كاملة (مما يتطلب عملية DH مكلفة بالإضافة إلى فك تشفير ChaCha20/Poly1305). يمكن للمعالج الرد برسالة Retry باستخدام القيم الموجودة في رأس رسالة Session Request.

### التشفير المصادق عليه

هناك ثلاث حالات منفصلة للتشفير المصادق عليه (CipherStates). واحدة أثناء مرحلة المصافحة، واثنتان (الإرسال والاستقبال) لمرحلة البيانات. كل منها لها مفتاحها الخاص من KDF.

سيتم تمثيل البيانات المشفرة/المعتمدة كـ

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Encrypted and authenticated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

تنسيق البيانات المشفرة والمصادق عليها.

المدخلات لدوال التشفير/فك التشفير:

```
k :: 32 byte cipher key, as generated from KDF


nonce :: Counter-based nonce, 12 bytes.

Starts at 0 and incremented for each message. First four bytes are always zero. Last eight bytes are the counter, little-endian encoded. Maximum value is 2**64 - 2. Connection must be dropped and restarted after it reaches that value. The value 2**64 - 1 must never be sent.

ad :: In handshake phase:

Associated data, 32 bytes. The SHA256 hash of all preceding data. In data phase: The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
مخرجات دالة التشفير، مدخلات دالة فك التشفير:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | ChaCha20 encrypted data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | Poly1305 Message Authentication Code | + (MAC) + | 16 bytes | +----+----+----+----+----+----+----+----+

    encrypted data :: Same size as plaintext data, 0 - 65519 bytes

    MAC :: Poly1305 message authentication code, 16 bytes
```
بالنسبة لـ ChaCha20، ما هو موصوف هنا يتوافق مع [RFC-7539](https://tools.ietf.org/html/rfc7539)، والذي يُستخدم أيضاً بشكل مماثل في TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### ملاحظات

- نظراً لأن ChaCha20 هو شفرة تدفق، فإن النصوص الواضحة لا تحتاج إلى حشو. يتم تجاهل بايتات تدفق المفاتيح الإضافية.
- يتم الاتفاق على مفتاح الشفرة (256 بت) بواسطة SHA256 KDF. تفاصيل KDF لكل رسالة موجودة في أقسام منفصلة أدناه.

#### معالجة أخطاء AEAD

- في جميع الرسائل، يكون حجم رسالة AEAD معروفاً مسبقاً. عند فشل مصادقة AEAD، يجب على المستقبِل إيقاف معالجة الرسائل الإضافية والتخلص من الرسالة.
- يجب على Bob الاحتفاظ بقائمة سوداء لعناوين IP التي تحتوي على إخفاقات متكررة.

### KDF لطلب الجلسة

تُولد دالة اشتقاق المفاتيح (KDF) مفتاح تشفير k لمرحلة المصافحة من نتيجة DH، باستخدام HMAC-SHA256(key, data) كما هو معرف في [RFC-2104](https://tools.ietf.org/html/rfc2104). هذه هي دوال InitializeSymmetric() و MixHash() و MixKey()، تماماً كما هي معرفة في مواصفات Noise.

#### KDF لـ ChainKey الأولي

```
// Define protocol_name.


    Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"

    :   (52 bytes, US-ASCII encoded, no NULL termination).

    // Define Hash h = 32 bytes h = SHA256(protocol_name);

    Define ck = 32 byte chaining key. Copy the h data to ck. Set ck = h

    // MixHash(null prologue) h = SHA256(h);

    // up until here, can all be precalculated by Alice for all outgoing connections

    // Bob's X25519 static keys // bpk is published in routerinfo bsk = GENERATE_PRIVATE() bpk = DERIVE_PUBLIC(bsk)

    // Bob static key // MixHash(bpk) // || below means append h = SHA256(h || bpk);

    // Bob introduction key // bik is published in routerinfo bik = RANDOM(32)

    // up until here, can all be precalculated by Bob for all incoming connections
```
#### KDF لطلب الجلسة

```
// MixHash(header)

h = SHA256(h || header)

    This is the "e" message pattern:

    // Alice's X25519 ephemeral keys aesk = GENERATE_PRIVATE() aepk = DERIVE_PUBLIC(aesk)

    // Alice ephemeral key X // MixHash(aepk) h = SHA256(h || aepk);

    // h is used as the associated data for the AEAD in Session Request // Retain the Hash h for the Session Created KDF

    End of "e" message pattern.

    This is the "es" message pattern:

    // DH(e, rs) == DH(s, re) sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

    // MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) // ChaChaPoly parameters to encrypt/decrypt keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

    // AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

    // retain the chainKey for Session Created KDF

    End of "es" message pattern.

    // Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2 = bik

    // Header encryption keys for next message (Session Created) k_header_1 = bik k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

    // Header encryption keys for next message (Retry) k_header_1 = bik k_header_2 = bik
```
### SessionRequest (النوع 0)

يرسل Alice إلى Bob، إما كأول رسالة في عملية المصافحة، أو كرد على رسالة Retry. يرد Bob برسالة Session Created. الحجم: 80 + حجم البيانات. الحجم الأدنى: 88

إذا لم تكن لدى Alice رمز صالح، يجب على Alice إرسال رسالة Token Request بدلاً من Session Request، لتجنب العبء الإضافي للتشفير غير المتماثل في إنشاء Session Request.

رأس طويل. محتوى Noise: مفتاح Alice المؤقت X حمولة Noise: DateTime وكتل أخرى الحد الأقصى لحجم الحمولة: MTU - 108 (IPv4) أو MTU - 128 (IPv6). لـ 1280 MTU: الحد الأقصى للحمولة هو 1172 (IPv4) أو 1152 (IPv6). لـ 1500 MTU: الحد الأقصى للحمولة هو 1392 (IPv4) أو 1372 (IPv6).

خصائص أمان الحمولة:

```
XK(s, rs): Authentication Confidentiality

-> e, es 0 2

    Authentication: None (0). This payload may have been sent by any party, including an active attacker.

    Confidentiality: 2. Encryption to a known recipient, forward secrecy for sender compromise only, vulnerable to replay. This payload is encrypted based only on DHs involving the recipient's static key pair. If the recipient's static private key is compromised, even at a later date, this payload can be decrypted. This message can also be replayed, since there's no ephemeral contribution from the recipient.

    "e": Alice generates a new ephemeral key pair and stores it in the e

    :   variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "es": A DH is performed between the Alice's ephemeral key pair and the

    :   Bob's static key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
يتم تشفير قيمة X لضمان عدم التمييز والتفرد للحمولة، وهما إجراءان ضروريان لمواجهة فحص الحزم العميق (DPI). نستخدم تشفير ChaCha20 لتحقيق هذا، بدلاً من البدائل الأكثر تعقيداً وبطءً مثل elligator2. التشفير غير المتماثل لمفتاح router العام الخاص ببوب سيكون بطيئاً جداً. يستخدم تشفير ChaCha20 مفتاح intro الخاص ببوب كما هو منشور في قاعدة بيانات الشبكة.

تشفير ChaCha20 مخصص لمقاومة فحص الحزم العميق (DPI) فقط. أي طرف يعرف مفتاح التقديم الخاص ببوب، والذي يتم نشره في قاعدة بيانات الشبكة، قد يفك تشفير الرأس وقيمة X في هذه الرسالة.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | See Header Encryption KDF | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key n=0 + | | +----+----+----+----+----+----+----+----+ | | + X, ChaCha20 encrypted + | with Bob intro key n=0 | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | k defined in KDF for Session Request | + n = 0 + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian

    :   key: Bob's intro key n: 1 data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------------------+-----------+-----------+-----------+-----------+
    | > Packet Number                               | type      | ver       | id        | flag      |
    +-----------------------------------------------+-----------+-----------+-----------+-----------+
    | > Source Connection ID                                                                        |
    +-----------------------------------------------------------------------------------------------+
    | > Token                                                                                       |
    +-----------------------------------------------------------------------------------------------+
    | > X (32 bytes)                                                                                |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    +-----------------------------------------------------------------------------------------------+
    | >                                                                                             |
    | >                                                                                             |
    | > Noise payload (block data)                                                                  |
    | >                                                                                             |
    | > :   (length varies)                                                                         |
    | >                                                                                             |
    | > see below for allowed blocks                                                                |
    |                                                                                               |
    |                                                                                               |
    +-----------------------------------------------------------------------------------------------+

    Destination Connection ID :: Randomly generated by Alice

    id :: 1 byte, the network ID (currently 2, except for test networks)

    ver :: 2

    type :: 0

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random 4 byte number generated by Alice, ignored

    Source Connection ID :: Randomly generated by Alice,

    :   must not be equal to Destination Connection ID

    Token :: 0 if not previously received from Bob

    X :: 32 bytes, X25519 ephemeral key, little endian
```
#### الحمولة

- كتلة DateTime
- كتلة Options (اختيارية)
- كتلة Relay Tag Request (اختيارية)
- كتلة Padding (اختيارية)

الحد الأدنى لحجم الحمولة هو 8 بايت. نظراً لأن كتلة DateTime تبلغ 7 بايت فقط، يجب أن تكون كتلة واحدة أخرى على الأقل موجودة.

#### ملاحظات

- القيمة الفريدة X في كتلة ChaCha20 الأولية تضمن أن النص المشفر مختلف لكل جلسة.
- لتوفير مقاومة التحقق، يجب على Bob ألا يرسل رسالة إعادة محاولة استجابةً لرسالة طلب جلسة ما لم تكن حقول نوع الرسالة وإصدار البروتوكول ومعرف الشبكة في رسالة طلب الجلسة صالحة.
- يجب على Bob رفض الاتصالات حيث تكون قيمة الطابع الزمني بعيدة جداً عن الوقت الحالي. اطلق على أقصى وقت دلتا "D". يجب على Bob الاحتفاظ بذاكرة تخزين مؤقت محلية لقيم المصافحة المستخدمة سابقاً ورفض المكررات، لمنع هجمات إعادة التشغيل. يجب أن تكون للقيم في الذاكرة المؤقتة مدة حياة لا تقل عن 2*D. قيم الذاكرة المؤقتة تعتمد على التنفيذ، ومع ذلك يمكن استخدام القيمة X ذات 32 بايت (أو ما يعادلها المشفر). الرفض عبر إرسال رسالة إعادة محاولة تحتوي على رمز مميز صفر وكتلة إنهاء.
- قد لا يتم إعادة استخدام مفاتيح Diffie-Hellman المؤقتة أبداً، لمنع الهجمات التشفيرية، وسيتم رفض إعادة الاستخدام كهجوم إعادة تشغيل.
- يجب أن تكون خيارات "KE" و "auth" متوافقة، أي أن السر المشترك K يجب أن يكون بالحجم المناسب. إذا تمت إضافة المزيد من خيارات "auth"، فقد يؤدي هذا ضمنياً إلى تغيير معنى علامة "KE" لاستخدام KDF مختلف أو حجم اقتطاع مختلف.
- يجب على Bob التحقق من أن مفتاح Alice المؤقت هو نقطة صالحة على المنحنى هنا.
- يجب أن يقتصر الحشو على كمية معقولة. قد يرفض Bob الاتصالات ذات الحشو المفرط. سيحدد Bob خيارات الحشو الخاصة به في Session Created. إرشادات الحد الأدنى/الأقصى لم تحدد بعد. حجم عشوائي من 0 إلى 31 بايت كحد أدنى؟ (التوزيع لم يحدد بعد، راجع الملحق A.)
- عند معظم الأخطاء، بما في ذلك AEAD وDH وإعادة التشغيل الظاهرة أو فشل التحقق من المفتاح، يجب على Bob إيقاف معالجة الرسائل الإضافية وإسقاط الرسالة دون الرد.
- قد يرسل Bob رسالة إعادة محاولة تحتوي على رمز مميز صفر وكتلة إنهاء برمز سبب انحراف الساعة إذا كان الطابع الزمني في كتلة DateTime منحرفاً جداً.
- تخفيف DoS: DH عملية مكلفة نسبياً. كما هو الحال مع بروتوكول NTCP السابق، يجب على routers اتخاذ جميع التدابير اللازمة لمنع استنزاف المعالج أو الاتصال. ضع حدود على أقصى اتصالات نشطة وأقصى إعدادات اتصال قيد التقدم. فرض مهلات زمنية للقراءة (لكل قراءة والإجمالي لـ "slowloris"). حدد الاتصالات المتكررة أو المتزامنة من نفس المصدر. احتفظ بقوائم سوداء للمصادر التي تفشل باستمرار. لا ترد على فشل AEAD. بدلاً من ذلك، رد برسالة إعادة محاولة قبل عملية DH والتحقق من AEAD.
- حقل "ver": بروتوكول Noise العام والامتدادات وبروتوكول SSU2 بما في ذلك مواصفات الحمولة، مشيراً إلى SSU2. قد يستخدم هذا الحقل للإشارة إلى الدعم للتغييرات المستقبلية.
- يُستخدم حقل معرف الشبكة للتعرف بسرعة على اتصالات الشبكات المتقاطعة. إذا لم يتطابق هذا الحقل مع معرف شبكة Bob، يجب على Bob قطع الاتصال وحجب الاتصالات المستقبلية.
- يجب على Bob إسقاط الرسالة إذا كان معرف اتصال المصدر يساوي معرف اتصال الوجهة.

### KDF لجزء Session Created وجزء Session Confirmed الأول

```
// take h saved from Session Request KDF

// MixHash(ciphertext) h = SHA256(h || encrypted Noise payload from Session Request)

    // MixHash(header) h = SHA256(h || header)

    This is the "e" message pattern:

    // Bob's X25519 ephemeral keys besk = GENERATE_PRIVATE() bepk = DERIVE_PUBLIC(besk)

    // h is from KDF for Session Request // Bob ephemeral key Y // MixHash(bepk) h = SHA256(h || bepk);

    // h is used as the associated data for the AEAD in Session Created // Retain the Hash h for the Session Confirmed KDF

    End of "e" message pattern.

    This is the "ee" message pattern:

    // MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) sharedSecret = DH(aesk, bepk) = DH(besk, aepk) keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

    // AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

    // retain the chaining key ck for Session Confirmed KDF

    End of "ee" message pattern.

    // Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2: See Session Request KDF above

    // Header protection keys for next message (Session Confirmed) k_header_1 = bik k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### SessionCreated (النوع 1)

يرسل Bob إلى Alice، كاستجابة لرسالة Session Request. تستجيب Alice برسالة Session Confirmed. الحجم: 80 + حجم الحمولة. الحد الأدنى للحجم: 88

محتوى Noise: مفتاح Bob المؤقت Y حمولة Noise: DateTime وAddress وكتل أخرى الحد الأقصى لحجم الحمولة: MTU - 108 (IPv4) أو MTU - 128 (IPv6). لـ MTU 1280: الحد الأقصى للحمولة هو 1172 (IPv4) أو 1152 (IPv6). لـ MTU 1500: الحد الأقصى للحمولة هو 1392 (IPv4) أو 1372 (IPv6).

خصائص أمان الحمولة:

```
XK(s, rs): Authentication Confidentiality

<- e, ee 2 1

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 1. Encryption to an ephemeral recipient. This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee"). However, the sender has not authenticated the recipient, so this payload might be sent to any party, including an active attacker.

    "e": Bob generates a new ephemeral key pair and stores it in the e variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
يتم تشفير قيمة Y لضمان عدم التمييز والتفرد للحمولة، والتي تعتبر تدابير مضادة ضرورية لفحص الحزم العميق (DPI). نستخدم تشفير ChaCha20 لتحقيق ذلك، بدلاً من البدائل الأكثر تعقيداً وبطئاً مثل elligator2. التشفير غير المتماثل لمفتاح router العام الخاص بـ Alice سيكون بطيئاً جداً. يستخدم تشفير ChaCha20 مفتاح الدعوة الخاص بـ Bob، كما هو منشور في قاعدة بيانات الشبكة.

تشفير ChaCha20 مخصص لمقاومة فحص الحزم العميق فقط. أي طرف يعرف مفتاح المقدمة الخاص بـ Bob، والذي يتم نشره في قاعدة بيانات الشبكة، والتقط أول 32 بايت من طلب الجلسة، قد يتمكن من فك تشفير قيمة Y في هذه الرسالة.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key and + | derived key, see Header Encryption KDF| +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with derived key n=0 + | See Header Encryption KDF | +----+----+----+----+----+----+----+----+ | | + Y, ChaCha20 encrypted + | with derived key n=0 | + (32 bytes) + | See Header Encryption KDF | + + | | +----+----+----+----+----+----+----+----+ | ChaCha20 data | + Encrypted and authenticated data + | length varies | + k defined in KDF for Session Created + | n = 0; see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian

    :   key: Bob's intro key n: 1 data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير موضحة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+----------+----------+----------+
    | > Packet Number                           | type     | ver      | id       | flag     |
    +-------------------------------------------+----------+----------+----------+----------+
    | > Source Connection ID                                                                |
    +---------------------------------------------------------------------------------------+
    | > Token                                                                               |
    +---------------------------------------------------------------------------------------+
    | > Y (32 bytes)                                                                        |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+
    | >                                                                                     |
    | >                                                                                     |
    | > Noise payload (block data)                                                          |
    | >                                                                                     |
    | > :   (length varies) see below for allowed blocks                                    |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: The Source Connection ID

    :   received from Alice in Session Request

    id :: 1 byte, the network ID (currently 2, except for test networks)

    ver :: 2

    type :: 0

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random 4 byte number generated by Bob, ignored

    Source Connection ID :: The Destination Connection ID

    :   received from Alice in Session Request

    Token :: 0 (unused)

    Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### الحمولة

- كتلة DateTime
- كتلة Address
- كتلة Relay Tag (اختيارية)
- كتلة New Token (غير مُستحسنة، راجع الملاحظة)
- كتلة First Packet Number (اختيارية)
- كتلة Options (اختيارية)
- كتلة Termination (غير مُستحسنة، أرسل في رسالة إعادة محاولة بدلاً من ذلك)
- كتلة Padding (اختيارية)

الحد الأدنى لحجم الحمولة هو 8 بايت. نظرًا لأن كتل DateTime وAddress يبلغ مجموعها أكثر من ذلك، فإن المتطلب يتم الوفاء به بهاتين الكتلتين فقط.

#### ملاحظات

- يجب على أليس التحقق من أن مفتاح بوب المؤقت هو نقطة صالحة على المنحنى هنا.
- يجب أن تكون الحشوة محدودة بكمية معقولة. قد ترفض أليس الاتصالات ذات الحشوة المفرطة. ستحدد أليس خيارات الحشوة الخاصة بها في Session Confirmed. الحد الأدنى/الأقصى للإرشادات غير محدد بعد. حجم عشوائي من 0 إلى 31 بايت كحد أدنى؟ (سيتم تحديد التوزيع، انظر الملحق A.)
- عند أي خطأ، بما في ذلك AEAD، أو DH، أو الطابع الزمني، أو إعادة التشغيل الظاهرة، أو فشل التحقق من المفتاح، يجب على أليس إيقاف معالجة الرسائل الإضافية وإغلاق الاتصال دون الاستجابة.
- يجب على أليس رفض الاتصالات حيث تكون قيمة الطابع الزمني بعيدة جداً عن الوقت الحالي. لنسمي أقصى وقت دلتا "D". يجب على أليس الاحتفاظ بذاكرة تخزين مؤقت محلية لقيم المصافحة المستخدمة سابقاً ورفض المكررات، لمنع هجمات إعادة التشغيل. يجب أن تكون للقيم في ذاكرة التخزين المؤقت مدة حياة لا تقل عن 2*D. قيم ذاكرة التخزين المؤقت تعتمد على التطبيق، ومع ذلك يمكن استخدام قيمة Y البالغة 32 بايت (أو ما يعادلها مشفراً).
- يجب على أليس إسقاط الرسالة إذا كان IP والمنفذ المصدر لا يتطابقان مع IP والمنفذ الوجهة لـ Session Request.
- يجب على أليس إسقاط الرسالة إذا كانت معرفات الاتصال للوجهة والمصدر لا تتطابق مع معرفات الاتصال للمصدر والوجهة لـ Session Request.
- يرسل بوب كتلة relay tag إذا طلبتها أليس في Session Request.
- كتلة New Token غير مستحسنة في Session Created، لأن بوب يجب أن يقوم بالتحقق من Session Confirmed أولاً. انظر قسم Tokens أدناه.

#### المشاكل

- هل نُدرج خيارات الحشو الأدنى/الأقصى هنا؟

### KDF لجزء Session Confirmed الأول، باستخدام Session Created KDF

```
// take h saved from Session Created KDF

// MixHash(ciphertext) h = SHA256(h || encrypted Noise payload from Session Created)

    // MixHash(header) h = SHA256(h || header) // h is used as the associated data for the AEAD in Session Confirmed part 1, below

    This is the "s" message pattern:

    // Alice's X25519 static keys ask = GENERATE_PRIVATE() apk = DERIVE_PUBLIC(ask)

    // AEAD parameters // k is from Session Request n = 1 ad = h ciphertext = ENCRYPT(k, n++, apk, ad)

    // MixHash(ciphertext) h = SHA256(h || ciphertext);

    // h is used as the associated data for the AEAD in Session Confirmed part 2

    End of "s" message pattern.

    // Header encryption keys for this message See Session Confirmed part 2 below
```
### KDF للجزء الثاني من Session Confirmed

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk) sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

// AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2 // MixHash(ciphertext) h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF // retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2: See Session Created KDF above

// Header protection keys for data phase See data phase KDF below
```
### SessionConfirmed (النوع 2)

ترسل Alice إلى Bob، كرد على رسالة Session Created. يستجيب Bob فوراً برسالة Data تحتوي على كتلة ACK. الحجم: 80 + حجم الحمولة. الحد الأدنى للحجم: حوالي 500 (الحد الأدنى لحجم كتلة معلومات router حوالي 420 بايت)

محتوى Noise: المفتاح الثابت لـ Alice جزء حمولة Noise الأول: لا شيء جزء حمولة Noise الثاني: RouterInfo الخاص بـ Alice، وكتل أخرى الحد الأقصى لحجم الحمولة: MTU - 108 (IPv4) أو MTU - 128 (IPv6). لـ MTU 1280: الحد الأقصى للحمولة هو 1172 (IPv4) أو 1152 (IPv6). لـ MTU 1500: الحد الأقصى للحمولة هو 1392 (IPv4) أو 1372 (IPv6).

خصائص أمان الحمولة:

```
XK(s, rs): Authentication Confidentiality

-> s, se 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.

    "s": Alice writes her static public key from the s variable into the message buffer, encrypting it, and hashes the output along with the old h to derive a new h.

    "se": A DH is performed between the Alice's static key pair and the Bob's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
يحتوي هذا على إطارين من ChaChaPoly. الأول هو المفتاح العام الثابت المشفر لأليس. الثاني هو حمولة Noise: RouterInfo المشفر لأليس، والخيارات الاختيارية، والحشو الاختياري. يستخدمان مفاتيح مختلفة، لأن دالة MixKey() يتم استدعاؤها بينهما.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|  Short Header 16 bytes, ChaCha20 |

    + encrypted with Bob intro key and + | derived key, see Header Encryption KDF| +----+----+----+----+----+----+----+----+ | ChaCha20 frame (32 bytes) | + Encrypted and authenticated data + + Alice static key S + | k defined in KDF for Session Created | + n = 1 + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+ | | + Length varies (remainder of packet) + | | + ChaChaPoly frame + | Encrypted and authenticated | + see below for allowed blocks + | | + k defined in KDF for + | Session Confirmed part 2 | + n = 0 + | see KDF for associated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian

    :   inside 48 byte ChaChaPoly frame
```
البيانات غير المشفرة (علامات المصادقة Poly1305 غير مُظهرة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+-------------------------+
    | > Packet Number                                   | type       | frag       | > flags                 |
    +---------------------------------------------------+------------+------------+-------------------------+
    | > S Alice static key (32 bytes)                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Destination Connection ID :: As sent in Session Request,

    :   or one received in Session Confirmed?

    Packet Number :: 0 always, for all fragments, even if retransmitted

    type :: 2

    frag :: 1 byte fragment info:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number 0-14, big endian bits 3-0: total fragments 1-15, big endian

    flags :: 2 bytes, unused, set to 0 for future compatibility

    S :: 32 bytes, Alice's X25519 static key, little endian
```
#### الحمولة

- كتلة RouterInfo (يجب أن تكون الكتلة الأولى)
- كتلة الخيارات (اختيارية)
- كتلة الرمز المميز الجديد (اختيارية)
- كتلة طلب التتابع (اختيارية)
- كتلة اختبار النظير (اختيارية)
- كتلة رقم الحزمة الأولى (اختيارية)
- كتل I2NP أو الجزء الأول أو الأجزاء التالية (اختيارية، لكن ربما لا توجد مساحة)
- كتلة الحشو (اختيارية)

الحد الأدنى لحجم الحمولة هو 8 بايت. نظراً لأن كتلة RouterInfo ستكون أكبر بكثير من ذلك، فإن المتطلب يتم تحقيقه بهذه الكتلة فقط.

#### ملاحظات

- يجب على Bob تنفيذ التحقق المعتاد من Router Info. تأكد من أن نوع التوقيع مدعوم، تحقق من التوقيع، تحقق من أن الطابع الزمني ضمن الحدود المسموحة، وأي فحوصات أخرى ضرورية. انظر أدناه للملاحظات حول التعامل مع Router Infos المجزأة.

- يجب على Bob التحقق من أن المفتاح الثابت لـ Alice المستلم في الإطار الأول يطابق المفتاح الثابت في Router Info. يجب على Bob أولاً البحث في Router Info عن عنوان NTCP أو SSU2 Router مع خيار إصدار (v) مطابق. راجع أقسام Router Info المنشورة وRouter Info غير المنشورة أدناه. راجع أدناه الملاحظات حول التعامل مع Router Infos المجزأة.

- إذا كان لدى Bob إصدار أقدم من RouterInfo الخاص بـ Alice في netdb الخاص به، تحقق من أن المفتاح الثابت في معلومات الـ router هو نفسه في كليهما، إذا كان موجوداً، وإذا كان الإصدار الأقدم أقل من XXX قديماً (انظر وقت تدوير المفتاح أدناه)

- يجب على Bob أن يتحقق من أن المفتاح الثابت لـ Alice هو نقطة صالحة على المنحنى هنا.

- يجب تضمين خيارات لتحديد معاملات الحشو.

- عند حدوث أي خطأ، بما في ذلك فشل AEAD أو RI أو DH أو الطابع الزمني أو التحقق من المفتاح، يجب على Bob إيقاف معالجة الرسائل الإضافية وإغلاق الاتصال دون الرد.

- محتوى إطار الجزء الثاني من الرسالة 3: تنسيق هذا الإطار هو نفس تنسيق إطارات مرحلة البيانات، باستثناء أن طول الإطار يتم إرساله من قبل أليس في طلب الجلسة. انظر أدناه لتنسيق إطار مرحلة البيانات. يجب أن يحتوي الإطار على 1 إلى 4 كتل بالترتيب التالي:

1)  كتلة معلومات router الخاصة بأليس (مطلوبة)   2)  كتلة الخيارات (اختيارية)   3)  كتل I2NP (اختيارية)

4\) كتلة الحشو (اختيارية) يجب ألا يحتوي هذا الإطار أبداً على أي نوع آخر من الكتل. TODO: ماذا عن relay و peer test؟

- كتلة الحشو للجزء الثاني من الرسالة 3 مُوصى بها.

- قد لا تكون هناك مساحة، أو قد تكون هناك مساحة صغيرة فقط، متاحة لكتل I2NP، اعتماداً على MTU وحجم Router Info. لا تتضمن كتل I2NP إذا كان Router Info مجزأ. قد يكون التنفيذ الأبسط هو عدم تضمين كتل I2NP مطلقاً في رسالة Session Confirmed، وإرسال جميع كتل I2NP في رسائل Data اللاحقة. انظر قسم كتلة Router Info أدناه للحد الأقصى لحجم الكتلة.

#### تجزئة الجلسة المؤكدة

يجب أن تحتوي رسالة Session Confirmed على معلومات router الموقعة بالكامل من أليس حتى يتمكن بوب من إجراء عدة فحوصات مطلوبة:

- المفتاح الثابت "s" في RI يطابق المفتاح الثابت في المصافحة
- يجب استخراج مفتاح التعريف "i" في RI والتحقق من صحته، لاستخدامه في مرحلة البيانات
- توقيع RI صالح

للأسف، قد تتجاوز معلومات الـ Router حتى عند ضغطها بـ gzip في كتلة الـ RI حجم الـ MTU. لذلك، قد يتم تجزئة الـ Session Confirmed عبر حزمتين أو أكثر. هذه هي الحالة الوحيدة في بروتوكول SSU2 حيث يتم تجزئة الحمولة المحمية بـ AEAD عبر حزمتين أو أكثر.

يتم بناء الرؤوس لكل حزمة كما يلي:

- جميع العناوين هي عناوين قصيرة بنفس رقم الحزمة 0
- جميع العناوين تحتوي على حقل "frag"، مع رقم الجزء والعدد الإجمالي للأجزاء
- العنوان غير المشفر للجزء 0 هو البيانات المرتبطة (AD) لرسالة "jumbo"
- كل عنوان مشفر باستخدام آخر 24 بايت من البيانات في تلك الحزمة

قم ببناء سلسلة الحزم كما يلي:

- إنشاء كتلة RI واحدة (الجزء 0 من 1 في حقل جزء كتلة RI). نحن لا نستخدم تجزئة كتلة RI، كان ذلك لطريقة بديلة لحل نفس المشكلة.
- إنشاء حمولة "jumbo" مع كتلة RI وأي كتل أخرى ليتم تضمينها
- حساب إجمالي حجم البيانات (غير شامل الرأس)، والذي هو حجم الحمولة + 64 بايت للمفتاح الثابت واثنين من MAC
- حساب المساحة المتاحة في كل حزمة، والتي هي MTU ناقص رأس IP (20 أو 40)، ناقص رأس UDP (8)، ناقص رأس SSU2 القصير (16). إجمالي الحمل الإضافي لكل حزمة هو 44 (IPv4) أو 64 (IPv6).
- حساب عدد الحزم.
- حساب حجم البيانات في الحزمة الأخيرة. يجب أن يكون أكبر من أو يساوي 24 بايت، بحيث يعمل تشفير الرأس. إذا كان صغيراً جداً، إما أضف كتلة حشو، أو زد حجم كتلة الحشو إذا كانت موجودة بالفعل، أو قلل حجم إحدى الحزم الأخرى بحيث تكون الحزمة الأخيرة كبيرة بما فيه الكفاية.
- إنشاء الرأس غير المشفر للحزمة الأولى، مع العدد الإجمالي للأجزاء في حقل frag، وتشفير الحمولة "jumbo" بـ Noise، باستخدام الرأس كـ AD، كالمعتاد.
- تقسيم الحزمة jumbo المشفرة إلى أجزاء
- إضافة رأس غير مشفر لكل جزء 1-n
- تشفير الرأس لكل جزء 0-n. كل رأس يستخدم نفس k_header_1 وk_header_2 كما هو محدد أعلاه في Session Confirmed KDF.
- إرسال جميع الأجزاء

عملية إعادة التجميع:

عندما يستقبل Bob أي رسالة Session Confirmed، يقوم بفك تشفير الرأس (header)، وفحص حقل frag، ويحدد أن رسالة Session Confirmed مجزأة. لا يقوم (ولا يستطيع) بفك تشفير الرسالة حتى يتم استقبال وإعادة تجميع جميع الأجزاء.

- احتفظ بالرأس للجزء 0، حيث يُستخدم كـ Noise AD
- تجاهل الرؤوس للأجزاء الأخرى قبل إعادة التجميع
- أعد تجميع الحمولة "الضخمة"، مع رأس الجزء 0 كـ AD، وفك التشفير باستخدام Noise
- تحقق من صحة كتلة RI كالمعتاد
- انتقل إلى مرحلة البيانات وأرسل ACK 0، كالمعتاد

لا توجد آلية لـ Bob لتأكيد الاستلام للأجزاء الفردية. عندما يستقبل Bob جميع الأجزاء، ويعيد تجميعها، ويفك تشفيرها، ويتحقق من صحة المحتويات، يقوم Bob بعملية split() كالمعتاد، ويدخل مرحلة البيانات، ويرسل ACK لرقم الحزمة 0.

إذا لم تتلق Alice إقرار استلام لحزمة البيانات رقم 0، فيجب عليها إعادة إرسال جميع حزم تأكيد الجلسة كما هي.

أمثلة:

بالنسبة لـ 1500 MTU عبر IPv6، الحد الأقصى للحمولة هو 1372، النفقات العامة لكتلة RI هي 5، الحد الأقصى لحجم بيانات RI (المضغوطة بـ gzip) هو 1367 (بافتراض عدم وجود كتل أخرى). مع حزمتين، النفقات العامة للحزمة الثانية هي 64، لذا يمكنها استيعاب 1436 بايت إضافي من الحمولة. إذن حزمتان كافيتان لـ RI مضغوط يصل إلى 2803 بايت.

أكبر RI مضغوط تم رصده في الشبكة الحالية يبلغ حوالي 1400 بايت؛ لذلك، من الناحية العملية، يجب أن يكون جزأان كافيان، حتى مع الحد الأدنى لـ MTU البالغ 1280. البروتوكول يسمح بحد أقصى 15 جزء.

تحليل الأمان:

تكون سلامة وأمان Session Confirmed المجزأة نفس سلامة وأمان النسخة غير المجزأة. أي تعديل على أي جزء سيتسبب في فشل Noise AEAD بعد إعادة التجميع. تُستخدم رؤوس الأجزاء بعد الجزء 0 فقط لتحديد الجزء. حتى لو كان لدى مهاجم على المسار مفتاح k_header_2 المستخدم لتشفير الرأس (وهو أمر غير محتمل، مُشتق من المصافحة)، فإن هذا لن يسمح للمهاجم بإستبدال جزء صالح.

### KDF لمرحلة البيانات

تستخدم مرحلة البيانات الرأس للبيانات المرتبطة.

يولد KDF مفتاحي تشفير k_ab و k_ba من مفتاح السلسلة ck، باستخدام HMAC-SHA256(key, data) كما هو محدد في [RFC-2104](https://tools.ietf.org/html/rfc2104). هذه هي دالة split()، تماماً كما هو محدد في مواصفات Noise.

```
// split()

// chainKey = from handshake phase keydata = HKDF(chainKey, ZEROLEN, "", 64) k_ab = keydata[0:31] k_ba = keydata[32:63]

    // key is k_ab for Alice to Bob // key is k_ba for Bob to Alice

    keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64) k_data = keydata[0:31] k_header_2 = keydata[32:63]

    // AEAD parameters k = k_data n = 4 byte packet number from header ad = 16 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for data phase // aik = Alice's intro key // bik = Bob's intro key k_header_1 = Receiver's intro key (aik or bik) k_header_2: from above
```
### رسالة البيانات (النوع 6)

حمولة Noise: جميع أنواع الكتل مسموحة. الحد الأقصى لحجم الحمولة: MTU - 60 (IPv4) أو MTU - 80 (IPv6). لـ MTU 1500: الحد الأقصى للحمولة هو 1440 (IPv4) أو 1420 (IPv6).

بدءاً من الجزء الثاني من Session Confirmed، جميع الرسائل تكون داخل حمولة ChaChaPoly مُوثقة ومُشفرة. جميع الحشو يكون داخل الرسالة. داخل الحمولة يوجد تنسيق قياسي مع صفر أو أكثر من "الكتل". كل كتلة لها نوع من بايت واحد وطول من بايتين. الأنواع تشمل التاريخ/الوقت، رسالة I2NP، الخيارات، الإنهاء، والحشو.

ملاحظة: يمكن لـ Bob، ولكن ليس مطلوباً منه، أن يرسل RouterInfo الخاص به إلى Alice كأول رسالة له إلى Alice في مرحلة البيانات.

خصائص أمان الحمولة:

```
XK(s, rs): Authentication Confidentiality

<- 2 5 -> 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### ملاحظات

- يجب على الـ router إسقاط الرسالة عند حدوث خطأ AEAD.

```
+----+----+----+----+----+----+----+----+

|  Short Header 16 bytes, ChaCha20 |

    + encrypted with intro key and + | derived key, see Data Phase KDF | +----+----+----+----+----+----+----+----+ | ChaCha20 data | + Encrypted and authenticated data + | length varies | + k defined in Data Phase KDF + | n = packet number from header | + + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+--------------------------------+
    | > Packet Number                           | type     | > flags                        |
    +-------------------------------------------+----------+--------------------------------+
    | >                                                                                     |
    | >                                                                                     |
    | > Noise payload (block data)                                                          |
    | >                                                                                     |
    | > :   (length varies)                                                                 |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: As specified in session setup

    Packet Number :: 4 byte big endian integer

    type :: 6

    flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### ملاحظات

- الحد الأدنى لحجم الحمولة هو 8 بايت. سيتم استيفاء هذا المتطلب بأي كتلة ACK أو I2NP أو First Fragment أو Follow-on Fragment. إذا لم يتم استيفاء المتطلب، يجب تضمين كتلة Padding.
- كل رقم حزمة يمكن استخدامه مرة واحدة فقط. عند إعادة إرسال رسائل I2NP أو الأجزاء، يجب استخدام رقم حزمة جديد.

### KDF لاختبار النظير

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### اختبار النظير (النوع 7)

يرسل Charlie إلى Alice، وترسل Alice إلى Charlie، لمراحل Peer Test 5-7 فقط. يجب إرسال مراحل Peer Test 1-4 داخل الجلسة باستخدام كتلة Peer Test في رسالة Data. راجع أقسام كتلة Peer Test وعملية Peer Test أدناه للحصول على مزيد من المعلومات.

الحجم: 48 + حجم الحمولة.

حمولة Noise: انظر أدناه.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Alice or Charlie + | intro key | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Alice or Charlie + | intro key | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: See below

    type :: 7

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random number generated by Alice or Charlie

    Source Connection ID :: See below

    Token :: Randomly generated by Alice or Charlie, ignored
```
#### الحمولة

- كتلة DateTime
- كتلة العنوان (مطلوبة للرسائل 6 و 7، انظر الملاحظة أدناه)
- كتلة Peer Test
- كتلة الحشو (اختيارية)

الحد الأدنى لحجم الحمولة هو 8 بايت. وبما أن كتلة Peer Test يبلغ إجماليها أكثر من ذلك، فإن المتطلب يتم الوفاء به بهذه الكتلة فقط.

في الرسائل 5 و 7، قد يكون blok اختبار النظير مطابقاً للكتلة من رسائل الجلسة 3 و 4، والتي تحتوي على الاتفاقية الموقعة من قبل تشارلي، أو قد يتم إعادة إنتاجها. التوقيع اختياري.

في الرسالة 6، قد يكون كتلة Peer Test مطابقة للكتلة من رسائل الجلسة 1 و 2، التي تحتوي على الطلب الموقع من قبل Alice، أو قد يتم إعادة إنتاجها. التوقيع اختياري.

معرفات الاتصال: يتم اشتقاق معرفي الاتصال من test nonce. للرسائل 5 و 7 المرسلة من Charlie إلى Alice، يكون Destination Connection ID عبارة عن نسختين من test nonce بحجم 4 بايت بترتيب big-endian، أي ((nonce << 32) | nonce). Source Connection ID هو عكس Destination Connection ID، أي ~((nonce << 32) | nonce). للرسالة 6 المرسلة من Alice إلى Charlie، يتم تبديل معرفي الاتصال.

محتويات كتلة العنوان:

- في الرسالة 5: غير مطلوب.
- في الرسالة 6: عنوان IP ومنفذ Charlie كما تم اختياره من RI الخاص بـ Charlie.
- في الرسالة 7: عنوان IP ومنفذ Alice الفعلي الذي تم استقبال الرسالة 6 منه.

### KDF للإعادة المحاولة

الشرط لرسالة إعادة المحاولة هو أن Bob غير مطالب بفك تشفير رسالة طلب الجلسة لإنتاج رسالة إعادة محاولة كرد. أيضاً، يجب أن تكون هذه الرسالة سريعة التوليد، باستخدام التشفير المتماثل فقط.

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### إعادة المحاولة (النوع 9)

يرسل Bob إلى Alice، كرد على رسالة Session Request أو Token Request. تستجيب Alice برسالة Session Request جديدة. الحجم: 48 + حجم الحمولة.

يعمل أيضًا كرسالة إنهاء (أي "عدم إعادة المحاولة") إذا تم تضمين كتلة إنهاء.

حمولة الضوضاء: انظر أدناه.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير مُظهرة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: The Source Connection ID

    :   received from Alice in Token Request or Session Request

    Packet Number :: Random number generated by Bob

    type :: 9

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: The Destination Connection ID

    :   received from Alice in Token Request or Session Request

    Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,

    :   or zero if session is rejected and a termination block is included
```
#### الحمولة

- كتلة DateTime
- كتلة Address
- كتلة Options (اختيارية)
- كتلة Termination (اختيارية، إذا تم رفض الجلسة)
- كتلة Padding (اختيارية)

الحد الأدنى لحجم الحمولة هو 8 بايت. نظراً لأن كتل DateTime وAddress يبلغ مجموعهما أكثر من ذلك، فإن المتطلب يتم تحقيقه بهاتين الكتلتين فقط.

#### ملاحظات

- لتوفير مقاومة التحقيق، يجب على router ألا يرسل رسالة Retry استجابة لرسالة Session Request أو Token Request ما لم تكن حقول نوع الرسالة وإصدار البروتوكول ومعرف الشبكة في رسالة الطلب صحيحة.
- لتحديد حجم أي هجوم تضخيم يمكن شنه باستخدام عناوين مصدر مزيفة، يجب ألا تحتوي رسالة Retry على كميات كبيرة من الحشو. يُوصى بأن تكون رسالة Retry لا تزيد عن ثلاثة أضعاف حجم الرسالة التي ترد عليها. بدلاً من ذلك، استخدم طريقة بسيطة مثل إضافة كمية عشوائية من الحشو في النطاق 1-64 بايت.

### KDF لطلب الرمز المميز

يجب أن تكون هذه الرسالة سريعة التوليد، باستخدام التشفير المتماثل فقط.

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### طلب الرمز المميز (النوع 10)

أليس ترسل إلى بوب. بوب يرد برسالة إعادة المحاولة. الحجم: 48 + حجم الحمولة.

إذا لم يكن لدى Alice رمز مميز صالح، يجب على Alice إرسال هذه الرسالة بدلاً من Session Request، لتجنب العبء الإضافي للتشفير غير المتماثل في توليد Session Request.

حمولة Noise: انظر أدناه.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: Randomly generated by Alice

    Packet Number :: Random number generated by Alice

    type :: 10

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: Randomly generated by Alice,

    :   must not be equal to Destination Connection ID

    Token :: zero
```
#### الحمولة

- كتلة DateTime
- كتلة الحشو

الحد الأدنى لحجم البيانات المفيدة هو 8 بايت.

#### ملاحظات

- لتوفير مقاومة للاستطلاع، يجب على router ألا يرسل رسالة Retry استجابةً لرسالة Token Request إلا إذا كانت حقول نوع الرسالة وإصدار البروتوكول ومعرف الشبكة في رسالة Token Request صالحة.
- هذه ليست رسالة Noise قياسية وليست جزءاً من المصافحة. وهي غير مرتبطة برسالة Session Request إلا من خلال معرفات الاتصال.
- في معظم الأخطاء، بما في ذلك AEAD، أو الإعادة الواضحة، يجب على Bob إيقاف معالجة الرسائل الإضافية وإسقاط الرسالة دون الاستجابة.
- يجب على Bob رفض الاتصالات حيث تكون قيمة الطابع الزمني بعيدة جداً عن الوقت الحالي. أطلق على أقصى وقت دلتا "D". يجب على Bob الاحتفاظ بذاكرة تخزين مؤقت محلية لقيم المصافحة المستخدمة سابقاً ورفض المكررات، لمنع هجمات الإعادة. القيم في ذاكرة التخزين المؤقت يجب أن يكون لها عمر افتراضي لا يقل عن 2*D. قيم ذاكرة التخزين المؤقت تعتمد على التنفيذ، ومع ذلك يمكن استخدام قيمة X البالغة 32 بايت (أو ما يعادلها المشفر).
- يجوز لـ Bob إرسال رسالة Retry تحتوي على رمز مميز صفري وكتلة Termination مع رمز سبب انحراف الساعة إذا كان الطابع الزمني في كتلة DateTime منحرفاً جداً.
- الحد الأدنى للحجم: TBD، نفس القواعد كما هو الحال مع Session Created؟

### KDF لـ Hole Punch

يجب أن تكون هذه الرسالة سريعة في التوليد، باستخدام التشفير المتماثل فقط.

```
// AEAD parameters

// aik = Alice's intro key k = aik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = aik k_header_2 = aik
```
### Hole Punch (النوع 11)

يرسل تشارلي إلى أليس، استجابةً لـ Relay Intro مُستلم من بوب. تستجيب أليس بـ Session Request جديد. الحجم: 48 + حجم البيانات.

حمولة Noise: انظر أدناه.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Alice intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Alice intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
البيانات غير المشفرة (علامة مصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: See below

    Packet Number :: Random number generated by Charlie

    type :: 11

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: See below

    Token :: 8 byte unsigned integer, randomly generated by Charlie, nonzero.
```
#### الحمولة

- كتلة DateTime
- كتلة Address
- كتلة Relay Response
- كتلة Padding (اختيارية)

الحد الأدنى لحجم البيانات المفيدة هو 8 بايت. نظراً لأن كتل DateTime و Address يبلغ مجموعها أكثر من ذلك، فإن المتطلب يتم الوفاء به بهاتين الكتلتين فقط.

معرفات الاتصال: يتم اشتقاق معرفي الاتصال من relay nonce. معرف اتصال الوجهة هو نسختان من relay nonce بحجم 4 بايت big-endian، أي ((nonce << 32) | nonce). معرف اتصال المصدر هو عكس معرف اتصال الوجهة، أي ~((nonce << 32) | nonce).

يجب على Alice تجاهل الرمز المميز في الرأس. الرمز المميز المطلوب استخدامه في طلب الجلسة موجود في كتلة استجابة الترحيل.

## حمولة Noise

تحتوي كل حمولة Noise على صفر أو أكثر من "الكتل".

يستخدم هذا نفس تنسيق الكتلة كما هو محدد في مواصفات [NTCP2](/docs/specs/ntcp2) و [ECIES](/docs/specs/ecies). يتم تعريف أنواع الكتل الفردية بشكل مختلف. المصطلح المكافئ في QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) هو "frames".

هناك مخاوف من أن تشجيع المطورين على مشاركة الكود قد يؤدي إلى مشاكل في التحليل. يجب على المطورين النظر بعناية في فوائد ومخاطر مشاركة الكود، والتأكد من أن قواعد الترتيب والكتل الصحيحة مختلفة للسياقين.

### تنسيق الحمولة

يوجد كتلة واحدة أو أكثر في الحمولة المشفرة. الكتلة هي تنسيق بسيط Tag-Length-Value (TLV). تحتوي كل كتلة على معرف من بايت واحد، وطول من بايتين، وصفر أو أكثر من بايتات البيانات. هذا التنسيق مطابق لذلك الموجود في [NTCP2](/docs/specs/ntcp2) و [ECIES](/docs/specs/ecies)، ومع ذلك فإن تعريفات الكتل مختلفة.

للقابلية للتوسع، يجب على المستقبلين تجاهل الكتل ذات المعرفات غير المعروفة، والتعامل معها كحشو.

(علامة مصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

[|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ [|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ ~ . . . ~

    blk :: 1 byte, see below size :: 2 bytes, big endian, size of data to follow, 0 - TBD data :: the data
```
يستخدم تشفير الرأس آخر 24 بايت من الحزمة كـ IV لعمليتي ChaCha20. وبما أن جميع الحزم تنتهي بـ MAC من 16 بايت، فهذا يتطلب أن تكون جميع حمولات الحزم 8 بايت كحد أدنى. إذا كانت الحمولة لا تلبي هذا المطلب، فيجب تضمين كتلة Padding.

يختلف الحد الأقصى لحمولة ChaChaPoly بناءً على نوع الرسالة وقيمة MTU ونوع عنوان IPv4 أو IPv6. الحد الأقصى للحمولة هو MTU - 60 لـ IPv4 و MTU - 80 لـ IPv6. الحد الأقصى لبيانات الحمولة هو MTU - 63 لـ IPv4 و MTU - 83 لـ IPv6. الحد الأعلى حوالي 1440 بايت لـ IPv4، مع MTU 1500، لرسالة البيانات. الحد الأقصى للحجم الإجمالي للكتلة هو الحد الأقصى لحجم الحمولة. الحد الأقصى لحجم الكتلة الواحدة هو الحد الأقصى للحجم الإجمالي للكتلة. نوع الكتلة هو 1 بايت. طول الكتلة هو 2 بايت. الحد الأقصى لحجم بيانات الكتلة الواحدة هو الحد الأقصى لحجم الكتلة الواحدة ناقص 3.

ملاحظات:

- يجب على المطورين التأكد من أنه عند قراءة كتلة، فإن البيانات المشوهة أو الضارة لن تتسبب في تجاوز القراءة للكتلة التالية أو خارج حدود الحمولة.
- يجب أن تتجاهل التطبيقات أنواع الكتل غير المعروفة من أجل التوافق المستقبلي.

أنواع الكتل:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### قواعد ترتيب الكتل

في Session Confirmed، يجب أن يكون Router Info هو البلوك الأول.

في جميع الرسائل الأخرى، الترتيب غير محدد، باستثناء المتطلبات التالية: الحشو (Padding)، إذا كان موجوداً، يجب أن يكون الكتلة الأخيرة. الإنهاء (Termination)، إذا كان موجوداً، يجب أن يكون الكتلة الأخيرة باستثناء الحشو. كتل الحشو المتعددة غير مسموحة في حمولة واحدة.

### مواصفات الكتل

#### التاريخ والوقت

لمزامنة الوقت:

```
+----+----+----+----+----+----+----+

| 0 | 4 | timestamp |

    +----+----+----+----+----+----+----+

    blk :: 0 size :: 2 bytes, big endian, value = 4 timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106
```
ملاحظات:

- على عكس SSU 1، لا يوجد طابع زمني في رأس الحزمة لمرحلة البيانات في SSU 2.
- يجب على التطبيقات إرسال كتل DateTime بشكل دوري في مرحلة البيانات.
- يجب على التطبيقات التقريب إلى أقرب ثانية لمنع انحياز الساعة في الشبكة.

#### الخيارات

تمرير الخيارات المحدثة. تشمل الخيارات: الحد الأدنى والأقصى للحشو.

كتلة الخيارات ستكون ذات طول متغير.

```
+----+----+----+----+----+----+----+----+

| 1 | size [|tmin|](##SUBST##|tmin|)tmax[|rmin|](##SUBST##|rmin|)rmax[|tdmy|](##SUBST##|tdmy|)

    +----+----+----+----+----+----+----+----+ [|tdmy|](##SUBST##|tdmy|) rdmy | tdelay | rdelay | | ~----+----+----+----+----+----+----+ ~ | more_options | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 1 size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

    tmin, tmax, rmin, rmax :: requested padding limits

    :   tmin and rmin are for desired resistance to traffic analysis. tmax and rmax are for bandwidth limits. tmin and tmax are the transmit limits for the router sending this options block. rmin and rmax are the receive limits for the router sending this options block. Each is a 4.4 fixed-point float representing 0 to 15.9375 (or think of it as an unsigned 8-bit integer divided by 16.0). This is the ratio of padding to data. Examples: Value of 0x00 means no padding Value of 0x01 means add 6 percent padding Value of 0x10 means add 100 percent padding Value of 0x80 means add 800 percent (8x) padding Alice and Bob will negotiate the minimum and maximum in each direction. These are guidelines, there is no enforcement. Sender should honor receiver's maximum. Sender may or may not honor receiver's minimum, within bandwidth constraints.

    tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average rdelay: Requested intra-message delay, 2 bytes big endian, msec average

    Padding distribution specified as additional parameters? Random delay specified as additional parameters?

    more_options :: Format TBD
```
مشاكل الخيارات:

- تفاوض الخيارات لم يتم تحديده بعد.

#### RouterInfo

تمرير RouterInfo الخاص بـ Alice إلى Bob. يُستخدم فقط في الحمولة الخاصة بـ Session Confirmed الجزء 2. لا يُستخدم في مرحلة البيانات؛ استخدم رسالة I2NP DatabaseStore بدلاً من ذلك.

الحد الأدنى للحجم: حوالي 420 بايت، ما لم تكن هوية الـ router والتوقيع في معلومات الـ router قابلة للضغط، وهو أمر غير محتمل.

ملاحظة: كتلة معلومات الـ Router لا يتم تجزئتها أبداً. حقل frag يكون دائماً 0/1. راجع قسم تجزئة الجلسة المؤكدة أعلاه للحصول على مزيد من المعلومات.

```
+----+----+----+----+----+----+----+----+

| 2 | size [|flag|](##SUBST##|flag|)frag| |

    +----+----+----+----+----+ + | | + Router Info fragment + | (Alice RI in Session Confirmed) | + (Alice, Bob, or third-party + | RI in data phase) | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 2 size :: 2 bytes, big endian, 2 + fragment size flag :: 1 byte flags bit order: 76543210 (bit 7 is MSB) bit 0: 0 for local store, 1 for flood request bit 1: 0 for uncompressed, 1 for gzip compressed bits 7-2: Unused, set to 0 for future compatibility frag :: 1 byte fragment info: bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number, always 0 bits 3-0: total fragments, always 1, big endian

    routerinfo :: Alice's or Bob's RouterInfo
```
ملاحظات:

- يتم ضغط Router Info اختيارياً باستخدام gzip، كما هو محدد بواسطة bit العلامة 1. هذا يختلف عن NTCP2، حيث لا يتم ضغطه أبداً، وعن DatabaseStore Message، حيث يتم ضغطه دائماً. الضغط اختياري لأنه عادة ما يكون ذا فائدة قليلة للـ Router Infos الصغيرة، حيث يوجد محتوى قابل للضغط قليل، ولكنه مفيد جداً للـ Router Infos الكبيرة مع عدة Router Addresses قابلة للضغط. يُنصح بالضغط إذا كان يسمح لـ Router Info بالتناسب في حزمة Session Confirmed واحدة دون تجزئة.
- الحد الأقصى لحجم الجزء الأول أو الوحيد في رسالة Session Confirmed: MTU - 113 لـ IPv4 أو MTU - 133 لـ IPv6. بافتراض MTU افتراضي 1500 بايت، وعدم وجود كتل أخرى في الرسالة، 1387 لـ IPv4 أو 1367 لـ IPv6. 97% من router infos الحالية أصغر من 1367 بدون gzipping. 99.9% من router infos الحالية أصغر من 1367 عند استخدام gzipped. بافتراض MTU أدنى 1280 بايت، وعدم وجود كتل أخرى في الرسالة، 1167 لـ IPv4 أو 1147 لـ IPv6. 94% من router infos الحالية أصغر من 1147 بدون gzipping. 97% من router infos الحالية أصغر من 1147 عند استخدام gzipped.
- بايت frag الآن غير مستخدم، كتلة Router Info لا يتم تجزئتها أبداً. يجب تعيين بايت frag إلى جزء 0، مجموع الأجزاء 1. راجع قسم Session Confirmed Fragmentation أعلاه للمزيد من المعلومات.
- يجب عدم طلب الإغراق إلا إذا كان هناك RouterAddresses منشورة في RouterInfo. يجب على router المستقبل عدم إغراق RouterInfo إلا إذا كان يحتوي على RouterAddresses منشورة.
- هذا البروتوكول لا يوفر تأكيداً بأن RouterInfo تم تخزينه أو إغراقه. إذا كان التأكيد مطلوباً، وكان المستقبل floodfill، فيجب على المرسل بدلاً من ذلك إرسال I2NP DatabaseStoreMessage قياسي مع رمز رد.

#### رسالة I2NP

رسالة I2NP كاملة مع رأس معدّل.

يستخدم هذا نفس الـ 9 بايت لرأس I2NP كما في [NTCP2](/docs/specs/ntcp2) (النوع، معرف الرسالة، انتهاء الصلاحية المختصر).

```
+----+----+----+----+----+----+----+----+

| 3 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 3 size :: 2 bytes, big endian, size of type + msg id + exp + message to follow I2NP message body size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: I2NP message body
```
ملاحظات:

- هذا هو نفس تنسيق رأس I2NP المكون من 9 بايت المستخدم في NTCP2.
- هذا هو نفس التنسيق تماماً مثل كتلة الجزء الأول، لكن نوع الكتلة يشير إلى أن هذه رسالة كاملة.
- الحد الأقصى للحجم بما في ذلك رأس I2NP المكون من 9 بايت هو MTU - 63 لـ IPv4 و MTU - 83 لـ IPv6.

#### الجزء الأول

الجزء الأول (الجزء رقم 0) من رسالة I2NP مع رأس معدّل.

هذا يستخدم نفس الـ 9 بايتات لرأس I2NP كما في [NTCP2](/docs/specs/ntcp2) (النوع، معرف الرسالة، انتهاء الصلاحية القصير).

العدد الإجمالي للأجزاء غير محدد.

```
+----+----+----+----+----+----+----+----+

| 4 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 4 size :: 2 bytes, big endian, size of data to follow Fragment size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: Partial I2NP message body, bytes 0 - (size - 10)
```
ملاحظات:

- هذا هو نفس تنسيق رأس I2NP المكون من 9 بايت المستخدم في NTCP2.
- هذا هو نفس التنسيق تماماً مثل كتلة رسالة I2NP، ولكن نوع الكتلة يشير إلى أن هذه هي الجزء الأول من الرسالة.
- طول الرسالة الجزئية يجب أن يكون أكبر من صفر.
- كما هو الحال في SSU 1، يُنصح بإرسال الجزء الأخير أولاً، بحيث يعرف المستقبل العدد الإجمالي للأجزاء ويمكنه تخصيص مخازن الاستقبال بكفاءة.
- الحد الأقصى للحجم بما في ذلك رأس I2NP المكون من 9 بايت هو MTU - 63 لـ IPv4 و MTU - 83 لـ IPv6.

#### جزء تابع

جزء إضافي (رقم الجزء أكبر من الصفر) من رسالة I2NP.

```
+----+----+----+----+----+----+----+----+

| 5 | size [|frag|](##SUBST##|frag|) msg id |

    +----+----+----+----+----+----+----+----+ | | + + | partial message | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 5 size :: 2 bytes, big endian, size of data to follow Fragment size is (size - 5). frag :: Fragment info: Bit order: 76543210 (bit 7 is MSB) bits 7-1: fragment number 1 - 127 (0 not allowed) bit 0: isLast (1 = true) msg id :: 4 bytes, big endian, I2NP message ID message :: Partial I2NP message body
```
ملاحظات:

- يجب أن يكون طول الرسالة الجزئية أكبر من الصفر.
- كما هو الحال في SSU 1، يُنصح بإرسال الجزء الأخير أولاً، بحيث يعرف المستقبل العدد الإجمالي للأجزاء ويمكنه تخصيص مخازن الاستقبال بكفاءة.
- كما هو الحال في SSU 1، الحد الأقصى لرقم الجزء هو 127، لكن الحد العملي هو 63 أو أقل. قد تحدد التطبيقات الحد الأقصى لما هو عملي لحجم رسالة I2NP أقصى يبلغ حوالي 64 كيلوبايت، وهو حوالي 55 جزءًا مع حد أدنى MTU يبلغ 1280. راجع قسم الحد الأقصى لحجم رسالة I2NP أدناه.
- الحد الأقصى لحجم الرسالة الجزئية (غير شامل frag ومعرف الرسالة) هو MTU - 68 لـ IPv4 و MTU - 88 لـ IPv6.

#### الإنهاء

إسقاط الاتصال. يجب أن يكون هذا آخر كتلة غير مبطنة في الحمولة.

```
+----+----+----+----+----+----+----+----+

| 6 | size | valid data packets |

    +----+----+----+----+----+----+----+----+

    :   received | rsn| addl data |

    +----+----+----+----+ + ~ . . . ~ +----+----+----+----+----+----+----+----+

    blk :: 6 size :: 2 bytes, big endian, value = 9 or more valid data packets received :: The number of valid packets received (current receive nonce value) 0 if error occurs in handshake phase 8 bytes, big endian rsn :: reason, 1 byte: 0: normal close or unspecified 1: termination received 2: idle timeout 3: router shutdown 4: data phase AEAD failure 5: incompatible options 6: incompatible signature type 7: clock skew 8: padding violation 9: AEAD framing error 10: payload format error 11: Session Request error 12: Session Created error 13: Session Confirmed error 14: Timeout 15: RI signature verification fail 16: s parameter missing, invalid, or mismatched in RouterInfo 17: banned 18: bad token 19: connection limits 20: incompatible version 21: wrong net ID 22: replaced by new session addl data :: optional, 0 or more bytes, for future expansion, debugging, or reason text. Format unspecified and may vary based on reason code.
```
ملاحظات:

- قد لا تُستخدم جميع الأسباب فعلياً، وهذا يعتمد على التطبيق. معظم الأخفاقات ستؤدي عموماً إلى إسقاط الرسالة، وليس إلى الإنهاء. راجع الملاحظات في أقسام رسائل المصافحة أعلاه. الأسباب الإضافية المدرجة هي للاتساق، والتسجيل، وإزالة الأخطاء، أو في حالة تغيير السياسات.
- يُوصى بتضمين كتلة ACK مع كتلة الإنهاء.
- في مرحلة البيانات، لأي سبب غير "تم استلام الإنهاء"، يجب على النظير الاستجابة بكتلة إنهاء مع السبب "تم استلام الإنهاء".

#### RelayRequest

يتم إرسالها في رسالة Data داخل الجلسة، من Alice إلى Bob. انظر قسم عملية التتابع أدناه.

```
+----+----+----+----+----+----+----+----+

|  7 | size [|flag|](##SUBST##|flag|) nonce |

    +-------+-------+---------------+-----------------------------------+
    | > relay tag                   | > timestamp                       |
    +-------+-------+---------------+-----------------------------------+
    | ver   | asz   | AlicePort     | > Alice IP address                |
    +-------+-------+---------------+-----------------------------------+

    ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 7 size :: 2 bytes, big endian, size of data to follow flag :: 1 byte flags, Unused, set to 0 for future compatibility

    The data below here is covered by the signature, and Bob forwards it unmodified.

    nonce :: 4 bytes, randomly generated by Alice relay tag :: 4 bytes, the itag from Charlie's RI timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 ver :: 1 byte SSU version to be used for the introduction: 1: SSU 1 2: SSU 2 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice.
```
ملاحظات:

- عنوان IP مُضمن دائماً (على عكس SSU 1) وقد يكون مختلفاً عن عنوان IP المستخدم للجلسة.

التوقيع:

تقوم Alice بتوقيع الطلب وتضمينه في هذا البلوك؛ يقوم Bob بإعادة توجيهه في بلوك Relay Intro إلى Charlie. خوارزمية التوقيع: قم بتوقيع البيانات التالية باستخدام مفتاح توقيع router الخاص بـ Alice:

- المقدمة: 16 بايت "RelayRequestData"، غير منتهية بـ null (غير مضمنة في الرسالة)
- bhash: router hash الخاص بـ Bob بحجم 32 بايت (غير مضمن في الرسالة)
- chash: router hash الخاص بـ Charlie بحجم 32 بايت (غير مضمن في الرسالة)
- nonce: 4 بايت nonce
- relay tag: 4 بايت relay tag
- الطابع الزمني: 4 بايت الطابع الزمني (ثوانٍ)
- ver: 1 بايت إصدار SSU
- asz: 1 بايت حجم endpoint (المنفذ + IP) (6 أو 18)
- AlicePort: 2 بايت رقم منفذ Alice
- Alice IP: (asz - 2) بايت عنوان IP الخاص بـ Alice

#### RelayResponse

يُرسل في رسالة Data أثناء الجلسة، من Charlie إلى Bob أو من Bob إلى Alice، وأيضاً في رسالة Hole Punch من Charlie إلى Alice. راجع قسم عملية التتابع أدناه.

```
+----+----+----+----+----+----+----+----+

|  8 | size [|flag|](##SUBST##|flag|)code| nonce

    +----+----+----+----+----+----+----+----+

    :   |     timestamp | ver| csz|Char

    +----+----+----+----+----+----+----+----+

    :   Port| Charlie IP addr | |

    +----+----+----+----+----+ + | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+ | Token | +----+----+----+----+----+----+----+----+

    blk :: 8 size :: 2 bytes, 6 flag :: 1 byte flags, Unused, set to 0 for future compatibility code :: 1 byte status code: 0: accept 1: rejected by Bob, reason unspecified 2: rejected by Bob, Charlie is banned 3: rejected by Bob, limit exceeded 4: rejected by Bob, signature failure 5: rejected by Bob, relay tag not found 6: rejected by Bob, Alice RI not found 7-63: other rejected by Bob codes TBD 64: rejected by Charlie, reason unspecified 65: rejected by Charlie, unsupported address 66: rejected by Charlie, limit exceeded 67: rejected by Charlie, signature failure 68: rejected by Charlie, Alice is already connected 69: rejected by Charlie, Alice is banned 70: rejected by Charlie, Alice is unknown 71-127: other rejected by Charlie codes TBD 128: reject, source and reason unspecified 129-255: other reject codes TBD

    The data below is covered by the signature if the code is 0 (accept). Bob forwards it unmodified.

    nonce :: 4 bytes, as received from Bob or Alice

    The data below is present only if the code is 0 (accept).

    timestamp :: Unix timestamp, unsigned seconds.

    :   Wraps around in 2106

    ver :: 1 byte SSU version to be used for the introduction:

    :   1: SSU 1 2: SSU 2

    csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)

    :   may be 0 for some rejection codes

    CharliePort :: 2 byte Charlie's port number, big endian

    :   not present if csz is 0

    Charlie IP :: (csz - 2) byte representation of Charlie's IP address,

    :   network byte order not present if csz is 0

    signature :: length varies, 64 bytes for Ed25519.

    :   Signature of prologue, Bob's hash, and signed data above, as signed by Charlie. Not present if rejected by Bob.

    token :: Token generated by Charlie for Alice to use

    :   in the Session Request. Only present if code is 0 (accept)
```
ملاحظات:

يجب على أليس استخدام الرمز المميز فوراً في طلب الجلسة.

التوقيع:

إذا وافق Charlie (كود الاستجابة 0) أو رفض (كود الاستجابة 64 أو أعلى)، يقوم Charlie بتوقيع الاستجابة وتضمينها في هذا البلوك؛ يقوم Bob بإعادة توجيهها في بلوك Relay Response إلى Alice. خوارزمية التوقيع: وقّع البيانات التالية باستخدام مفتاح التوقيع الخاص بـ router تشارلي:

- المقدمة: 16 بايت "RelayAgreementOK"، غير منتهية بقيمة فارغة (غير مُضمنة في الرسالة)
- bhash: hash الـ router الخاص بـ Bob بحجم 32 بايت (غير مُضمن في الرسالة)
- nonce: nonce بحجم 4 بايت
- الطابع الزمني: طابع زمني بحجم 4 بايت (بالثواني)
- ver: إصدار SSU بحجم 1 بايت
- csz: حجم نقطة النهاية (المنفذ + IP) بحجم 1 بايت (0 أو 6 أو 18)
- CharliePort: رقم منفذ Charlie بحجم 2 بايت (غير موجود إذا كان csz يساوي 0)
- Charlie IP: عنوان IP الخاص بـ Charlie بحجم (csz - 2) بايت (غير موجود إذا كان csz يساوي 0)

إذا رفض Bob (كود الاستجابة 1-63)، يوقع Bob الاستجابة ويضمنها في هذا البلوك. خوارزمية التوقيع: وقع البيانات التالية بمفتاح توقيع router الخاص بـ Bob:

- prologue: 16 بايت "RelayAgreementOK"، غير منتهية بـ null (غير مضمنة في الرسالة)
- bhash: router hash الخاص بـ Bob بحجم 32 بايت (غير مضمن في الرسالة)
- nonce: 4 بايت nonce
- timestamp: 4 بايت timestamp (بالثواني)
- ver: 1 بايت إصدار SSU
- csz: 1 بايت = 0

#### RelayIntro

يُرسل في رسالة Data داخل الجلسة، من Bob إلى Charlie. انظر قسم عملية الترحيل أدناه.

يجب أن يسبقه كتلة RouterInfo، أو كتلة رسالة I2NP DatabaseStore (أو جزء منها)، تحتوي على معلومات router الخاصة بـ Alice، إما في نفس الحمولة (إذا كان هناك مساحة)، أو في رسالة سابقة.

```
+----+----+----+----+----+----+----+----+

|  9 | size [|flag|](##SUBST##|flag|) |

    +----+----+----+----+ + | | + + | Alice Router Hash | + 32 bytes + | | + +----+----+----+----+ | | nonce | +----+----+----+----+----+----+----+----+ | relay tag | timestamp | +----+----+----+----+----+----+----+----+ | ver| asz[|AlicePort|](##SUBST##|AlicePort|) Alice IP address | +----+----+----+----+----+----+----+----+ | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 9 size :: 2 bytes, big endian, size of data to follow flag :: 1 byte flags, Unused, set to 0 for future compatibility hash :: Alice's 32-byte router hash,

    The data below here is covered by the signature, as received from Alice in the Relay Request, and Bob forwards it unmodified.

    nonce :: 4 bytes, as received from Alice relay tag :: 4 bytes, the itag from Charlie's RI timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 ver :: 1 byte SSU version to be used for the introduction: 1: SSU 1 2: SSU 2 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice.
```
ملاحظات:

- بالنسبة لـ IPv4، عنوان IP الخاص بـ Alice يكون دائماً 4 بايت، لأن Alice تحاول الاتصال بـ Charlie عبر IPv4. IPv6 مدعوم، وقد يكون عنوان IP الخاص بـ Alice 16 بايت.
- بالنسبة لـ IPv4، يجب إرسال هذه الرسالة عبر اتصال IPv4 مُنشأ، لأن هذه هي الطريقة الوحيدة التي يعرف بها Bob عنوان IPv4 الخاص بـ Charlie لإرجاعه إلى Alice في [RelayResponse](#relayresponse). IPv6 مدعوم، وقد يتم إرسال هذه الرسالة عبر اتصال IPv6 مُنشأ.
- أي عنوان SSU منشور مع introducers يجب أن يحتوي على "4" أو "6" في خيار "caps".

التوقيع:

تقوم Alice بتوقيع الطلب ويقوم Bob بإعادة توجيهه في هذا البلوك إلى Charlie. خوارزمية التحقق: تحقق من البيانات التالية باستخدام مفتاح التوقيع الخاص بـ router الخاص بـ Alice:

- prologue: 16 بايت "RelayRequestData"، غير منتهية بـ null (غير مُضمنة في الرسالة)
- bhash: router hash الخاص بـ Bob بحجم 32 بايت (غير مُضمن في الرسالة)
- chash: router hash الخاص بـ Charlie بحجم 32 بايت (غير مُضمن في الرسالة)
- nonce: nonce بحجم 4 بايت
- relay tag: relay tag بحجم 4 بايت
- timestamp: طابع زمني بحجم 4 بايت (بالثواني)
- ver: إصدار SSU بحجم 1 بايت
- asz: حجم نقطة النهاية (المنفذ + IP) بحجم 1 بايت (6 أو 18)
- AlicePort: رقم منفذ Alice بحجم 2 بايت
- Alice IP: عنوان IP الخاص بـ Alice بحجم (asz - 2) بايت

#### PeerTest

يُرسل إما في رسالة Data أثناء الجلسة، أو في رسالة Peer Test خارج الجلسة. راجع قسم عملية Peer Test أدناه.

بالنسبة للرسالة 2، يجب أن تسبقها كتلة RouterInfo، أو كتلة رسالة I2NP DatabaseStore (أو جزء منها)، تحتوي على Router Info الخاص بأليس، إما في نفس الحمولة (إذا كان هناك مساحة)، أو في رسالة سابقة.

بالنسبة للرسالة 4، إذا تم قبول الـ relay (رمز السبب 0)، يجب أن تسبق بكتلة RouterInfo، أو كتلة رسالة I2NP DatabaseStore (أو جزء منها)، تحتوي على معلومات Router الخاصة بتشارلي، إما في نفس الحمولة (إذا كان هناك مساحة)، أو في رسالة سابقة.

```
+----+----+----+----+----+----+----+----+

| 10 | size | msg[|code|](##SUBST##|code|)flag| |

    +----+----+----+----+----+----+ + | Alice router hash (message 2 only) | + or + | Charlie router hash (message 4 only) | + or all zeros if rejected by Bob + | Not present in messages 1,3,5,6,7 | + +----+----+ | | ver| +----+----+----+----+----+----+----+----+ nonce | timestamp | asz| +----+----+----+----+----+----+----+----+ [|AlicePort|](##SUBST##|AlicePort|) Alice IP address | | +----+----+----+----+----+----+ + | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 10 size :: 2 bytes, big endian, size of data to follow msg :: 1 byte message number 1-7 code :: 1 byte status code: 0: accept 1: rejected by Bob, reason unspecified 2: rejected by Bob, no Charlie available 3: rejected by Bob, limit exceeded 4: rejected by Bob, signature failure 5: rejected by Bob, address unsupported 6-63: other rejected by Bob codes TBD 64: rejected by Charlie, reason unspecified 65: rejected by Charlie, unsupported address 66: rejected by Charlie, limit exceeded 67: rejected by Charlie, signature failure 68: rejected by Charlie, Alice is already connected 69: rejected by Charlie, Alice is banned 70: rejected by Charlie, Alice is unknown 70-127: other rejected by Charlie codes TBD 128: reject, source and reason unspecified 129-255: other reject codes TBD reject codes only allowed in messages 3 and 4 flag :: 1 byte flags, Unused, set to 0 for future compatibility hash :: Alice's or Charlie's 32-byte router hash, only present in messages 2 and 4. All zeros (fake hash) in message 4 if rejected by Bob.

    For messages 1-4, the data below here is covered by the signature, if present, and Bob forwards it unmodified.

    ver :: 1 byte SSU version:

    :   1: SSU 1 (not supported) 2: SSU 2 (required)

    nonce :: 4 byte test nonce, big endian timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice or Charlie. Only present for messages 1-4. Optional in message 5-7.
```
ملاحظات:

- على عكس SSU 1، يجب أن تتضمن الرسالة 1 عنوان IP الخاص بأليس والمنفذ.

- اختبار عناوين IPv6 مدعوم، وقد يكون التواصل بين Alice-Bob و Alice-Charlie عبر IPv6، إذا أشار Bob و Charlie إلى الدعم بقدرة 'B' في عنوان IPv6 المنشور الخاص بهم. راجع الاقتراح 126 للتفاصيل.

ترسل Alice الطلب إلى Bob باستخدام جلسة موجودة عبر وسيلة النقل (IPv4 أو IPv6) التي تريد اختبارها. عندما يستقبل Bob طلباً من Alice عبر IPv4، يجب على Bob أن يختار Charlie الذي يعلن عن عنوان IPv4. عندما يستقبل Bob طلباً من Alice عبر IPv6، يجب على Bob أن يختار Charlie الذي يعلن عن عنوان IPv6. التواصل الفعلي بين Bob-Charlie قد يكون عبر IPv4 أو IPv6 (أي مستقل عن نوع عنوان Alice).

- يجب أن تكون الرسائل 1-4 موجودة في رسالة Data في جلسة موجودة.

- يجب على بوب إرسال RI الخاص بأليس إلى تشارلي قبل إرسال الرسالة 2.

- يجب على Bob إرسال RI الخاص بـ Charlie إلى Alice قبل إرسال الرسالة 4، في حالة القبول (رمز السبب 0).

- يجب أن تكون الرسائل 5-7 موجودة في رسالة Peer Test خارج الجلسة.

- الرسائل 5 و 7 قد تحتوي على نفس البيانات الموقعة كما تم إرسالها في الرسائل 3 و 4، أو قد يتم إعادة توليدها بطابع زمني جديد. التوقيع اختياري.

- قد تحتوي الرسالة 6 على نفس البيانات الموقعة المرسلة في الرسالتين 1 و 2، أو قد يتم إعادة إنتاجها بطابع زمني جديد. التوقيع اختياري.

التوقيعات:

تقوم أليس بتوقيع الطلب وتضمينه في الرسالة 1؛ بوب يقوم بإعادة توجيهها في الرسالة 2 إلى تشارلي. تشارلي يوقع الاستجابة ويضمنها في الرسالة 3؛ بوب يعيد توجيهها في الرسالة 4 إلى أليس. خوارزمية التوقيع: وقع أو تحقق من البيانات التالية باستخدام مفتاح التوقيع الخاص بأليس أو تشارلي:

- prologue: 16 بايت "PeerTestValidate"، غير منتهية بـ null (غير مضمنة في الرسالة)
- bhash: router hash الخاص بـ Bob بحجم 32 بايت (غير مضمن في الرسالة)
- ahash: router hash الخاص بـ Alice بحجم 32 بايت (يُستخدم فقط في التوقيع للرسائل 3 و 4؛ غير مضمن في الرسالة 3 أو 4)
- ver: 1 بايت إصدار SSU
- nonce: 4 بايت test nonce
- timestamp: 4 بايت الطابع الزمني (بالثواني)
- asz: 1 بايت حجم endpoint (المنفذ + IP) (6 أو 18)
- AlicePort: 2 بايت رقم منفذ Alice
- Alice IP: (asz - 2) بايت عنوان IP الخاص بـ Alice

#### NextNonce

TODO فقط إذا قمنا بتدوير المفاتيح

```
+----+----+----+----+----+----+----+----+

| 11 | size | TBD |

    +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 11 size :: 2 bytes, big endian, size of data to follow
```
#### إقرار

4 بايت ack خلال، متبوعة بعدد ack وصفر أو أكثر من نطاقات nack/ack.

هذا التصميم مُقتبس ومُبسط من QUIC. أهداف التصميم هي كما يلي:

- نريد ترميز "حقل البتات" بكفاءة، وهو تسلسل من البتات يمثل الحزم المؤكدة.
- حقل البتات يحتوي في الغالب على 1. كل من الـ 1 والـ 0 تأتي عادة في "كتل" متتالية.
- مقدار المساحة المتاحة في الحزمة للتأكيدات متغير.
- البت الأهم هو الذي يحمل الرقم الأعلى. البتات ذات الأرقام الأدنى أقل أهمية. تحت مسافة معينة من البت الأعلى، ستكون البتات الأقدم "منسية" ولن يتم إرسالها مرة أخرى.

يحقق الترميز المحدد أدناه هذه الأهداف التصميمية، من خلال إرسال رقم أعلى بت مضبوط على 1، مع بتات إضافية متتالية أقل من ذلك والتي هي أيضاً مضبوطة على 1. بعد ذلك، إذا كان هناك مساحة، واحد أو أكثر من "النطاقات" التي تحدد عدد البتات المتتالية 0 والبتات المتتالية 1 الأقل من ذلك. راجع QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) القسم 13.2.3 لمزيد من المعلومات الأساسية.

```
+----+----+----+----+----+----+----+----+

| 12 | size | Ack Through [|acnt|](##SUBST##|acnt|)

    +-------------+-------------+
    | > range     | > range     |
    +-------------+-------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 12 size :: 2 bytes, big endian, size of data to follow, 5 minimum ack through :: highest packet number acked acnt :: number of acks lower than ack through also acked, 0-255 range :: If present, 1 byte nack count followed by 1 byte ack count, 0-255 each
```
أمثلة:

نريد إرسال ACK للحزمة رقم 10 فقط:

- Ack Through: 10
- acnt: 0
- لا توجد نطاقات مضمنة

نريد إرسال إقرار استلام للحزم 8-10 فقط:

- Ack Through: 10
- acnt: 2
- لا توجد نطاقات مشمولة

نريد إرسال ACK للرسائل 10 9 8 6 5 2 1 0، وإرسال NACK للرسائل 7 4 3. تشفير ACK Block هو:

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

ملاحظات:

- قد لا تكون النطاقات موجودة. العدد الأقصى للنطاقات غير محدد، قد يكون بقدر ما يمكن أن يتسع له الحزمة.
- قد يكون range nack صفراً إذا كان يتم إقرار أكثر من 255 حزمة متتالية.
- قد يكون range ack صفراً إذا كان يتم رفض أكثر من 255 حزمة متتالية.
- قد لا يكون كل من range nack و ack صفراً في نفس الوقت.
- بعد النطاق الأخير، لا يتم إقرار أو رفض الحزم. طول كتلة ack وكيفية التعامل مع acks/nacks القديمة متروك لمرسل كتلة ack. انظر أقسام ack أدناه للمناقشة.
- يجب أن يكون ack through هو أعلى رقم حزمة تم استلامها، وأي حزم أعلى لم يتم استلامها. ومع ذلك، في حالات محدودة، قد يكون أقل، مثل إقرار حزمة واحدة "تملأ ثغرة"، أو تنفيذ مبسط لا يحتفظ بحالة جميع الحزم المستلمة. فوق الأعلى المستلم، لا يتم إقرار أو رفض الحزم، ولكن بعد عدة كتل ack، قد يكون من المناسب الدخول في وضع fast retransmit.
- هذا التنسيق هو نسخة مبسطة من ذلك الموجود في QUIC. تم تصميمه لترميز عدد كبير من ACKs بكفاءة، مع دفعات من NACKs.
- تُستخدم كتل ACK لإقرار حزم مرحلة البيانات. يجب تضمينها فقط لحزم مرحلة البيانات داخل الجلسة.

#### العنوان

منفذ بحجم 2 بايت وعنوان IP بحجم 4 أو 16 بايت. عنوان Alice، يُرسل إلى Alice من قبل Bob، أو عنوان Bob، يُرسل إلى Bob من قبل Alice.

```
+----+----+----+----+----+----+----+----+

| 13 | 6 or 18 | Port | IP Address

    +----+----+----+----+----+----+----+----+

    :   | 

    +----+

    blk :: 13 size :: 2 bytes, big endian, 6 or 18 port :: 2 bytes, big endian ip :: 4 byte IPv4 or 16 byte IPv6 address, big endian (network byte order)
```
#### طلب علامة الترحيل

قد يتم إرسال هذا من قبل Alice في رسالة Session Request أو Session Confirmed أو Data. غير مدعوم في رسالة Session Created، حيث أن Bob لا يملك RI الخاص بـ Alice بعد، ولا يعرف إذا كانت Alice تدعم relay. أيضاً، إذا كان Bob يحصل على اتصال وارد، فمن المحتمل أنه لا يحتاج إلى introducers (باستثناء ربما للنوع الآخر ipv4/ipv6).

عند الإرسال في طلب الجلسة، قد يستجيب Bob برقم Relay Tag في رسالة إنشاء الجلسة، أو قد يختار الانتظار حتى استقبال RouterInfo الخاص بـ Alice في تأكيد الجلسة للتحقق من هوية Alice قبل الاستجابة في رسالة البيانات. إذا كان Bob لا يريد أن يكون وسيط لـ Alice، فإنه لا يرسل كتلة Relay Tag.

```
+----+----+----+

| 15 | 0 |

    +----+----+----+

    blk :: 15 size :: 2 bytes, big endian, value = 0
```
#### علامة الترحيل

قد يتم إرسال هذا بواسطة Bob في رسالة Session Confirmed أو Data، كاستجابة لطلب Relay Tag Request من Alice.

عندما يتم إرسال طلب Relay Tag في رسالة Session Request، قد يستجيب Bob بـ Relay Tag في رسالة Session Created، أو قد يختار الانتظار حتى استلام RouterInfo الخاص بـ Alice في Session Confirmed للتحقق من هوية Alice قبل الاستجابة في رسالة Data. إذا كان Bob لا يرغب في القيام بالترحيل لـ Alice، فإنه لا يرسل كتلة Relay Tag.

```
+----+----+----+----+----+----+----+

| 16 | 4 | relay tag |

    +----+----+----+----+----+----+----+

    blk :: 16 size :: 2 bytes, big endian, value = 4 relay tag :: 4 bytes, big endian, nonzero
```
#### رمز جديد

للاتصال اللاحق. يتم تضمينه عادة في رسائل Session Created و Session Confirmed. قد يتم إرساله مرة أخرى في رسالة Data للجلسة طويلة المدى إذا انتهت صلاحية الرمز المميز السابق.

```
+----+----+----+----+----+----+----+----+

| 17 | 12 | expires |

    +----+----+----+----+----+----+----+----+

    :   token |

    +----+----+----+----+----+----+----+

    blk :: 17 size :: 2 bytes, big endian, value = 12 expires :: Unix timestamp, unsigned seconds. Wraps around in 2106 token :: 8 bytes, big endian
```
#### تحدي المسار

إرسال Ping مع بيانات اختيارية يتم إرجاعها في Path Response، يُستخدم كإشارة حفاظ على الاتصال أو للتحقق من تغيير عنوان IP/منفذ.

```
+----+----+----+----+----+----+----+----+

| 18 | size | Arbitrary Data |

    +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 18 size :: 2 bytes, big endian, size of data to follow data :: Arbitrary data to be returned in a Path Response length as selected by sender
```
ملاحظات:

- يُوصى بحد أدنى لحجم البيانات يبلغ 8 بايت، يحتوي على بيانات عشوائية، ولكن هذا غير مطلوب.
- الحد الأقصى للحجم غير محدد، ولكن يجب أن يكون أقل بكثير من 1280، لأن PMTU خلال مرحلة التحقق من المسار هو 1280.
- أحجام التحدي الكبيرة غير موصى بها لأنها يمكن أن تكون ناقلاً لهجمات تضخيم الحزم.

#### استجابة المسار

رسالة Pong تحتوي على البيانات المستلمة في Path Challenge، كرد على Path Challenge، تُستخدم كإشارة حفاظ على الاتصال أو للتحقق من تغيير عنوان IP/المنفذ.

```
+----+----+----+----+----+----+----+----+

| 19 | size | |

    +----+----+----+ + | Data received in Path Challenge | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 19 size :: 2 bytes, big endian, size of data to follow data :: As received in a Path Challenge
```
#### رقم الحزمة الأولى

يُضمّن اختيارياً في المصافحة في كل اتجاه، لتحديد رقم الحزمة الأولى التي سيتم إرسالها. وهذا يوفر مزيداً من الأمان لتشفير الرؤوس، مشابهاً لـ TCP.

غير محدد بالكامل، غير مدعوم حالياً.

```
+----+----+----+----+----+----+----+

| 20 | size | First pkt number |

    +----+----+----+----+----+----+----+

    blk :: 20 size :: 4 pkt num :: The first packet number to be sent in the data phase
```
#### الازدحام

هذا الكتلة مصممة لتكون طريقة قابلة للتوسيع لتبادل معلومات التحكم في الازدحام. يمكن أن يكون التحكم في الازدحام معقداً وقد يتطور مع اكتساب المزيد من الخبرة مع البروتوكول في الاختبارات المباشرة، أو بعد النشر الكامل.

هذا يبقي أي معلومات ازدحام خارج الكتل عالية الاستخدام I2NP، والجزء الأول First Fragment، والأجزاء التالية Followon Fragment، وكتل ACK، حيث لا توجد مساحة مخصصة للعلامات. بينما توجد ثلاثة بايتات من العلامات غير المستخدمة في رأس حزمة البيانات، فإن ذلك يوفر أيضاً مساحة محدودة للقابلية للتوسع، وحماية تشفير أضعف.

بينما يعتبر استخدام كتلة من 4 بايت لمعلومات من بتين فقط نوعاً من الهدر، إلا أنه من خلال وضع هذا في كتلة منفصلة، يمكننا بسهولة توسيعها ببيانات إضافية مثل أحجام النوافذ الحالية، أو RTT المقاس، أو علامات أخرى. لقد أظهرت التجربة أن بتات العلامات وحدها غالباً ما تكون غير كافية ومعقدة لتنفيذ مخططات التحكم في الازدحام المتقدمة. محاولة إضافة دعم لأي ميزة ممكنة للتحكم في الازدحام في، على سبيل المثال، كتلة ACK، من شأنه أن يهدر المساحة ويضيف تعقيداً إلى تحليل تلك الكتلة.

يجب على التطبيقات عدم افتراض أن الـ router الآخر يدعم أي bit علم معين أو ميزة مدرجة هنا، ما لم يكن التطبيق مطلوباً بواسطة إصدار مستقبلي من هذه المواصفة.

يجب أن يكون هذا البلوك على الأرجح آخر بلوك غير مبطن في الحمولة.

```
+----+----+----+----+

| 21 | size [|flag|](##SUBST##|flag|)

    +----+----+----+----+

    blk :: 21 size :: 1 (or more if extended) flag :: 1 byte flags bit order: 76543210 (bit 7 is MSB) bit 0: 1 to request immediate ack bit 1: 1 for explicit congestion notification (ECN) bits 7-2: Unused, set to 0 for future compatibility
```
#### الحشو

هذا للحشو داخل حمولات AEAD. الحشو لجميع الرسائل موجود داخل حمولات AEAD.

يجب أن تلتزم الحشوة (Padding) تقريباً بالمعاملات المتفاوض عليها. أرسل Bob معاملات tx/rx الدنيا/العليا المطلوبة في Session Created. أرسلت Alice معاملات tx/rx الدنيا/العليا المطلوبة في Session Confirmed. يمكن إرسال خيارات محدثة أثناء مرحلة البيانات. راجع معلومات كتلة الخيارات أعلاه.

إذا كان موجوداً، يجب أن يكون هذا الكتلة الأخيرة في الحمولة.

```
+----+----+----+----+----+----+----+----+

[|254 |](##SUBST##|254 |) size | padding | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 254 size :: 2 bytes, big endian, size of padding to follow padding :: random data
```
ملاحظات:

- الحجم = 0 مسموح.
- استراتيجيات الحشو TBD.
- الحد الأدنى للحشو TBD.
- الحمولات التي تحتوي على حشو فقط مسموحة.
- إعدادات الحشو الافتراضية TBD.
- انظر كتلة الخيارات لتفاوض معاملات الحشو
- انظر كتلة الخيارات لمعاملات الحد الأدنى/الأقصى للحشو
- لا تتجاوز MTU. إذا كان هناك حاجة للمزيد من الحشو، أرسل رسائل متعددة.
- استجابة router عند انتهاك الحشو المتفاوض عليه تعتمد على التنفيذ.
- طول الحشو إما أن يتم تحديده على أساس كل رسالة وتقديرات توزيع الطول، أو يجب إضافة تأخيرات عشوائية. هذه التدابير المضادة يجب تضمينها لمقاومة DPI، حيث أن أحجام الرسائل ستكشف بخلاف ذلك أن حركة I2P يتم نقلها بواسطة بروتوكول النقل. مخطط الحشو الدقيق هو مجال للعمل المستقبلي، الملحق A من [NTCP2](/docs/specs/ntcp2) يوفر مزيدًا من المعلومات حول هذا الموضوع.

## منع إعادة التشغيل

تم تصميم SSU2 لتقليل تأثير الرسائل التي يعيد تشغيلها المهاجم.

رسائل Token Request وRetry وSession Request وSession Created وHole Punch ورسائل Peer Test خارج الجلسة يجب أن تحتوي على كتل DateTime.

يتحقق كل من أليس وبوب من أن وقت هذه الرسائل ضمن انحراف زمني صالح (يُوصى بـ +/- دقيقتان). لـ"مقاومة التحسس"، يجب على بوب عدم الرد على رسائل Token Request أو Session Request إذا كان الانحراف غير صالح، حيث قد تكون هذه الرسائل إعادة تشغيل أو هجوم تحسس.

قد يختار Bob رفض رسائل Token Request و Retry المكررة، حتى لو كان الانحراف صالحاً، عبر مرشح Bloom أو آلية أخرى. ومع ذلك، فإن حجم وتكلفة المعالج للرد على هذه الرسائل منخفضة. في أسوأ الأحوال، قد تؤدي رسالة Token Request معاد تشغيلها إلى إبطال رمز مميز تم إرساله مسبقاً.

نظام الرموز المميزة يقلل بشكل كبير من تأثير رسائل Session Request المعاد تشغيلها. نظرًا لأن الرموز المميزة يمكن استخدامها مرة واحدة فقط، فإن رسالة Session Request المعاد تشغيلها لن تحتوي أبدًا على رمز مميز صالح. يمكن لـ Bob اختيار رفض رسائل Session Request المكررة، حتى لو كان الانحراف صالحًا، عبر مرشح Bloom أو آلية أخرى. ومع ذلك، فإن الحجم وتكلفة المعالج للرد برسالة Retry منخفضة. في أسوأ الحالات، قد يؤدي إرسال رسالة Retry إلى إبطال رمز مميز تم إرساله مسبقًا.

رسائل Session Created و Session Confirmed المكررة لن يتم التحقق من صحتها لأن حالة مصافحة Noise لن تكون في الحالة الصحيحة لفك تشفيرها. في أسوأ الحالات، قد يقوم النظير بإعادة إرسال Session Confirmed استجابة لرسالة Session Created مكررة ظاهريًا.

رسائل Hole Punch و Peer Test المعاد تشغيلها يجب أن يكون لها تأثير قليل أو معدوم.

يجب على أجهزة router استخدام رقم حزمة رسالة البيانات لاكتشاف وإسقاط رسائل مرحلة البيانات المكررة. كل رقم حزمة يجب أن يُستخدم مرة واحدة فقط. الرسائل المعاد تشغيلها يجب تجاهلها.

## إعادة إرسال المصافحة

### طلب الجلسة

إذا لم تتلق Alice أي Session Created أو Retry:

حافظ على نفس معرفات المصدر والاتصال، والمفتاح المؤقت، ورقم الحزمة 0. أو، احتفظ فقط بنفس الحزمة المشفرة وأعد إرسالها. يجب عدم زيادة رقم الحزمة، لأن ذلك سيغير قيمة التجميع المتسلسل المستخدمة لتشفير رسالة Session Created.

فترات إعادة الإرسال الموصى بها: 1.25، 2.5، و 5 ثوانٍ (1.25، 3.75، و 8.75 ثانية بعد الإرسال الأول). المهلة الزمنية الموصى بها: 15 ثانية إجمالاً

### تم إنشاء الجلسة

إذا لم يتلق بوب أي Session Confirmed:

الحفاظ على نفس معرفات المصدر والاتصال، والمفتاح المؤقت، ورقم الحزمة 0. أو، ببساطة الاحتفاظ بالحزمة المشفرة. يجب عدم زيادة رقم الحزمة، لأن ذلك سيغير قيمة التجمع المتسلسل المستخدمة لتشفير رسالة Session Confirmed.

فترات إعادة الإرسال الموصى بها: 1 و 2 و 4 ثوانِ (1 و 3 و 7 ثوانِ بعد الإرسال الأول). المهلة الزمنية الموصى بها: 12 ثانية إجمالية

### تم تأكيد الجلسة

في SSU 1، لا تنتقل Alice إلى مرحلة البيانات حتى يتم استلام أول حزمة بيانات من Bob. هذا يجعل SSU 1 إعداداً يتطلب رحلتين ذهاباً وإياباً.

بالنسبة لـ SSU 2، فترات إعادة الإرسال الموصى بها لـ Session Confirmed: 1.25، 2.5، و 5 ثوانٍ (1.25، 3.75، و 8.75 ثانية بعد الإرسال الأول).

هناك عدة بدائل. جميعها 1 RTT:

1) تفترض أليس أن Session Confirmed قد تم استلامه، ترسل رسائل البيانات فوراً، ولا تعيد إرسال Session Confirmed أبداً. حزم البيانات المستلمة خارج التسلسل (قبل Session Confirmed) ستكون غير قابلة لفك التشفير، لكن سيتم إعادة إرسالها. إذا فُقد Session Confirmed، سيتم إسقاط جميع رسائل البيانات المرسلة. 2) كما في 1)، إرسال رسائل البيانات فوراً، ولكن أيضاً إعادة إرسال Session Confirmed حتى يتم استلام رسالة بيانات. 3) يمكننا استخدام IK بدلاً من XK، حيث أن لديه رسالتين فقط في المصافحة، لكنه يستخدم DH إضافي (4 بدلاً من 3).

التنفيذ المُوصى به هو الخيار 2). يجب على Alice الاحتفاظ بالمعلومات المطلوبة لإعادة إرسال رسالة Session Confirmed. كما يجب على Alice إعادة إرسال جميع رسائل Data بعد إعادة إرسال رسالة Session Confirmed.

عند إعادة إرسال Session Confirmed، حافظ على نفس معرفات المصدر والاتصال، والمفتاح المؤقت، ورقم الحزمة 1. أو، احتفظ فقط بالحزمة المشفرة. يجب عدم زيادة رقم الحزمة، لأن ذلك سيغير قيمة hash المتسلسل والتي تعتبر مدخلاً لدالة split().

قد يحتفظ Bob (في قائمة انتظار) برسائل البيانات المستلمة قبل رسالة Session Confirmed. لا تتوفر مفاتيح حماية الرأس ولا مفاتيح فك التشفير قبل استلام رسالة Session Confirmed، لذلك لا يعلم Bob أنها رسائل بيانات، ولكن يمكن افتراض ذلك. بعد استلام رسالة Session Confirmed، يصبح Bob قادراً على فك تشفير ومعالجة رسائل البيانات المحفوظة في قائمة الانتظار. إذا كان هذا معقداً جداً، قد يقوم Bob بإسقاط رسائل البيانات غير القابلة لفك التشفير، حيث ستقوم Alice بإعادة إرسالها.

ملاحظة: إذا فُقدت حزم تأكيد الجلسة، فإن Bob سيعيد إرسال session created. لن يكون رأس session created قابلاً لفك التشفير باستخدام مفتاح intro الخاص بـ Alice، حيث أنه مُعيَّن بمفتاح intro الخاص بـ Bob (ما لم يتم تنفيذ فك تشفير احتياطي باستخدام مفتاح intro الخاص بـ Bob). قد يقوم Bob بإعادة إرسال حزم session confirmed فوراً إذا لم يتم تأكيد استلامها مسبقاً، وتم استلام حزمة غير قابلة لفك التشفير.

### طلب الرمز المميز

إذا لم تتلق أليس أي Retry:

الحفاظ على نفس معرفات المصدر والاتصال. يمكن للتنفيذ إنشاء رقم حزمة عشوائي جديد وتشفير حزمة جديدة؛ أو قد يعيد استخدام نفس رقم الحزمة أو فقط الاحتفاظ وإعادة إرسال نفس الحزمة المشفرة. يجب عدم زيادة رقم الحزمة، لأن ذلك سيغير قيمة التجميع المتسلسل المستخدمة لتشفير رسالة Session Created.

فترات إعادة الإرسال الموصى بها: 3 و 6 ثوانٍ (3 و 9 ثوانٍ بعد الإرسال الأول). المهلة الزمنية الموصى بها: 15 ثانية إجمالاً

### إعادة المحاولة

إذا لم يتلق Bob أي Session Confirmed:

لا يتم إعادة إرسال رسالة إعادة المحاولة عند انتهاء المهلة الزمنية، وذلك لتقليل تأثيرات عناوين المصدر المزيفة.

ومع ذلك، قد يتم إعادة إرسال رسالة Retry استجابةً لاستلام رسالة Session Request متكررة تحتوي على الرمز المميز الأصلي (غير الصالح)، أو استجابةً لرسالة Token Request متكررة. في كلتا الحالتين، هذا يشير إلى أن رسالة Retry قد فُقدت.

إذا تم استلام رسالة Session Request ثانية مع رمز مختلف ولكن لا يزال غير صالح، قم بإسقاط الجلسة المعلقة ولا تستجب.

إذا تم إعادة إرسال رسالة Retry: احتفظ بنفس معرفات المصدر والاتصال والرمز المميز. يمكن للتنفيذ إنشاء رقم حزمة عشوائي جديد وتشفير حزمة جديدة؛ أو يمكن إعادة استخدام نفس رقم الحزمة أو مجرد الاحتفاظ بنفس الحزمة المشفرة وإعادة إرسالها.

### المهلة الزمنية الإجمالية

المهلة الزمنية الإجمالية الموصى بها للمصافحة هي 20 ثانية.

### المكررات ومعالجة الأخطاء

يجب اكتشاف نسخ مكررة من رسائل مصافحة Noise الثلاث Session Request و Session Created و Session Confirmed قبل MixHash() للعنوان. بينما ستفشل معالجة Noise AEAD على الأرجح بعد ذلك، إلا أن hash المصافحة سيكون قد تلف بالفعل.

إذا تعرضت أي من الرسائل الثلاث للتلف وفشلت في AEAD، فإن المصافحة لا يمكن استردادها لاحقاً حتى مع إعادة الإرسال، لأن MixHash() تم استدعاؤها بالفعل على الرسالة التالفة.

## الرموز المميزة

يُستخدم الرمز المميز (Token) في رأس طلب الجلسة للتخفيف من هجمات حجب الخدمة (DoS)، ولمنع انتحال عنوان المصدر، وكمقاومة لهجمات إعادة التشغيل.

إذا لم يقبل Bob الرمز المميز في رسالة Session Request، فإن Bob لا يقوم بفك تشفير الرسالة، حيث أن ذلك يتطلب عملية DH مكلفة. يرسل Bob ببساطة رسالة Retry مع رمز مميز جديد.

إذا تم استلام رسالة Session Request لاحقة بذلك الرمز المميز، يقوم Bob بفك تشفير تلك الرسالة والمتابعة مع عملية المصافحة.

يجب أن يكون الرمز المميز قيمة مُولَّدة عشوائياً من 8 بايت، إذا كان مولد الرمز المميز يحفظ القيم وعنوان IP والمنفذ المرتبطين (في الذاكرة أو بشكل دائم). لا يجوز للمولد إنشاء قيمة غير شفافة، على سبيل المثال، باستخدام SipHash (مع بذرة سرية K0، K1) لعنوان IP والمنفذ والساعة أو اليوم الحالي، لإنشاء رموز مميزة لا تحتاج إلى الحفظ في الذاكرة، لأن هذه الطريقة تجعل من الصعب رفض الرموز المميزة المُعاد استخدامها وهجمات الإعادة. ومع ذلك، فإن الأمر يحتاج إلى دراسة إضافية فيما إذا كان بإمكاننا الانتقال إلى مثل هذا المخطط، كما يفعل [WireGuard](https://www.wireguard.com/papers/wireguard.pdf)، باستخدام HMAC من 16 بايت لسر الخادم وعنوان IP.

لا يمكن استخدام الرموز المميزة (tokens) إلا مرة واحدة. يجب استخدام الرمز المميز المرسل من Bob إلى Alice في رسالة Retry فوراً، وينتهي صلاحيته خلال ثوانٍ قليلة. يمكن استخدام الرمز المميز المرسل في كتلة New Token في جلسة مُنشأة في اتصال لاحق، وينتهي صلاحيته في الوقت المحدد في تلك الكتلة. يتم تحديد انتهاء الصلاحية من قِبل المرسل؛ القيم الموصى بها هي عدة دقائق كحد أدنى، وساعة أو أكثر كحد أقصى، اعتماداً على الحد الأقصى المرغوب للعبء الإضافي للرموز المميزة المخزنة.

إذا تغير عنوان IP أو المنفذ الخاص بـ router، فيجب عليه حذف جميع الرموز المحفوظة (الواردة والصادرة) للعنوان IP أو المنفذ القديم، حيث أنها لم تعد صالحة. يمكن اختيارياً الاحتفاظ بالرموز عبر إعادة تشغيل router، حسب التنفيذ. قبول رمز غير منتهي الصلاحية غير مضمون؛ إذا نسي بوب أو حذف رموزه المحفوظة، سيرسل Retry إلى أليس. يمكن لـ router اختيار تحديد تخزين الرموز، وإزالة أقدم الرموز المخزنة حتى لو لم تنته صلاحيتها.

يمكن إرسال كتل Token الجديدة من Alice إلى Bob أو من Bob إلى Alice. عادةً ما يتم إرسالها مرة واحدة على الأقل، أثناء أو بعد فترة وجيزة من إنشاء الجلسة. نظراً لعمليات التحقق من صحة RouterInfo في رسالة Session Confirmed، يجب على Bob عدم إرسال كتلة New Token في رسالة Session Created، ويمكن إرسالها مع ACK 0 و Router Info بعد استلام وتصديق Session Confirmed.

نظراً لأن فترات حياة الجلسات غالباً ما تكون أطول من انتهاء صلاحية الرمز المميز، يجب إعادة إرسال الرمز المميز قبل أو بعد انتهاء الصلاحية مع وقت انتهاء صلاحية جديد، أو يجب إرسال رمز مميز جديد. يجب على أجهزة router افتراض أن الرمز المميز الأخير المستلم فقط هو الصالح؛ لا يوجد متطلب لتخزين رموز مميزة متعددة واردة أو صادرة لنفس IP/port.

الرمز المميز مرتبط بتركيبة عنوان IP المصدر/المنفذ وعنوان IP الوجهة/المنفذ. الرمز المميز المُستلم عبر IPv4 لا يمكن استخدامه مع IPv6 والعكس صحيح.

إذا انتقل أي من الطرفين إلى IP أو منفذ جديد أثناء الجلسة (انظر قسم هجرة الاتصال)، فإن أي رموز تم تبادلها مسبقاً تصبح غير صالحة، ويجب تبادل رموز جديدة.

قد تحفظ التطبيقات الرموز المميزة على القرص وتعيد تحميلها عند إعادة التشغيل، لكن هذا ليس مطلوباً. في حالة الحفظ، يجب على التطبيق التأكد من أن عنوان IP والمنفذ لم يتغيرا منذ الإغلاق قبل إعادة تحميلها.

## تجزئة رسائل I2NP

الاختلافات عن SSU 1

ملاحظة: كما في SSU 1، لا تحتوي القطعة الأولى على معلومات حول العدد الإجمالي للقطع أو الطول الإجمالي. القطع اللاحقة لا تحتوي على معلومات حول إزاحتها. هذا يوفر للمرسل مرونة التقطيع "أثناء التنقل" بناءً على المساحة المتاحة في الحزمة. (Java I2P لا يفعل هذا؛ بل يقوم بـ "التقطيع المسبق" قبل إرسال القطعة الأولى) ومع ذلك، فإنه يحمل المستقبل عبء تخزين القطع المستلمة خارج الترتيب وتأخير إعادة التجميع حتى يتم استلام جميع القطع.

كما في SSU 1، أي إعادة إرسال للأجزاء يجب أن تحافظ على الطول (والإزاحة الضمنية) للإرسال السابق للجزء.

يفصل SSU 2 الحالات الثلاث (الرسالة الكاملة، الجزء الأولي، والجزء التالي) إلى ثلاثة أنواع كتل مختلفة، لتحسين كفاءة المعالجة.

## تكرار رسائل I2NP

هذا البروتوكول لا يمنع بشكل كامل التسليم المكرر لرسائل I2NP. المكررات على مستوى IP أو هجمات الإعادة سيتم اكتشافها على مستوى SSU2، لأن كل رقم حزمة يمكن استخدامه مرة واحدة فقط.

عندما يتم إعادة إرسال رسائل I2NP أو أجزاؤها في حزم جديدة، إلا أن هذا غير قابل للاكتشاف على طبقة SSU2. يجب على الـ router فرض انتهاء صلاحية I2NP (سواء القديمة جداً أو البعيدة جداً في المستقبل) واستخدام مرشح Bloom أو آلية أخرى مبنية على معرف رسالة I2NP.

قد يستخدم الـ router، أو في تطبيق SSU2، آليات إضافية لكشف التكرارات. على سبيل المثال، يمكن لـ SSU2 الاحتفاظ بذاكرة تخزين مؤقت لمعرفات الرسائل المستلمة مؤخراً. هذا يعتمد على التطبيق.

## التحكم في الازدحام

تحدد هذه المواصفات البروتوكول الخاص بترقيم الحزم وكتل ACK. يوفر هذا معلومات كافية في الوقت الفعلي للمرسل لتنفيذ خوارزمية تحكم في الازدحام فعالة ومتجاوبة، مع السماح بالمرونة والابتكار في هذا التنفيذ. يناقش هذا القسم أهداف التنفيذ ويقدم اقتراحات. يمكن العثور على إرشادات عامة في [RFC-9002](https://tools.ietf.org/html/rfc9002). انظر أيضاً [RFC-6298](https://tools.ietf.org/html/rfc6298) للحصول على إرشادات حول مؤقتات إعادة الإرسال.

حزم البيانات التي تحتوي على ACK فقط يجب ألا تُحسب ضمن البايتات أو الحزم قيد الإرسال ولا تخضع لتحكم الازدحام. على عكس TCP، يمكن لـ SSU2 اكتشاف فقدان هذه الحزم وقد تُستخدم هذه المعلومات لتعديل حالة الازدحام. ومع ذلك، هذا المستند لا يحدد آلية للقيام بذلك.

يمكن أيضاً استبعاد الحزم التي تحتوي على كتل أخرى غير البيانات من التحكم في الازدحام إذا رغب في ذلك، وهذا يعتمد على التنفيذ. على سبيل المثال:

- اختبار النظير
- طلب التتابع/التقديم/الاستجابة
- تحدي/استجابة المسار

يُنصح بأن يعتمد التحكم في الازدحام على عدد البايتات وليس على عدد الحزم، وذلك باتباع التوجيهات الواردة في TCP RFCs و QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). قد يكون من المفيد أيضًا وضع حد إضافي لعدد الحزم لمنع فيض المخزن المؤقت في النواة أو في الأجهزة الوسطية، حسب التطبيق، رغم أن هذا قد يضيف تعقيدًا كبيرًا. إذا كان الإخراج الخاص بالجلسة و/أو إجمالي الحزم محدود النطاق الترددي و/أو منظم السرعة، فقد يخفف هذا من الحاجة لتحديد عدد الحزم.

### أرقام الحزم

في SSU 1، تحتوي ACKs و NACKs على أرقام رسائل I2NP وأقنعة البتات للأجزاء المقسمة. يتتبع المرسلون حالة ACK للرسائل الصادرة (وأجزائها المقسمة) ويعيدون إرسال الأجزاء حسب الحاجة.

في SSU 2، تحتوي ACKs و NACKs على أرقام الحزم. يجب على المرسلين الاحتفاظ ببنية بيانات تحتوي على ربط أرقام الحزم بمحتوياتها. عندما يتم إرسال ACK أو NACK لحزمة، يجب على المرسل تحديد رسائل I2NP والأجزاء التي كانت في تلك الحزمة، لاتخاذ قرار بشأن ما يجب إعادة إرساله.

### تأكيد إقرار الجلسة

يرسل Bob رسالة ACK للحزمة 0، والتي تؤكد استلام رسالة Session Confirmed وتسمح لـ Alice بالانتقال إلى مرحلة البيانات، والتخلص من رسالة Session Confirmed الكبيرة المحفوظة لإعادة الإرسال المحتملة. هذا يحل محل DeliveryStatusMessage المرسلة من Bob في SSU 1.

يجب على Bob إرسال ACK في أقرب وقت ممكن بعد استلام رسالة Session Confirmed. يُقبل تأخير صغير (لا يزيد عن 50 مللي ثانية)، حيث يجب أن تصل رسالة Data واحدة على الأقل فور وصول رسالة Session Confirmed تقريباً، بحيث يمكن لـ ACK أن يؤكد استلام كل من رسالة Session Confirmed ورسالة Data. هذا سيمنع Bob من الاضطرار لإعادة إرسال رسالة Session Confirmed.

### توليد رسائل الإقرار (ACKs)

التعريف: الحزم المثيرة للإقرار: الحزم التي تحتوي على كتل مثيرة للإقرار تستدعي إقراراً (ACK) من المستقبِل خلال الحد الأقصى لتأخير الإقرار وتُسمى الحزم المثيرة للإقرار.

تقر أجهزة router بجميع الحزم التي تتلقاها وتعالجها. ومع ذلك، فقط الحزم المثيرة للإقرار تتسبب في إرسال كتلة ACK ضمن الحد الأقصى لتأخير الإقرار. الحزم التي لا تثير الإقرار يتم الإقرار بها فقط عندما يتم إرسال كتلة ACK لأسباب أخرى.

عند إرسال حزمة لأي سبب، يجب على نقطة النهاية محاولة تضمين كتلة ACK إذا لم يتم إرسال واحدة مؤخراً. القيام بذلك يساعد في اكتشاف الفقدان في الوقت المناسب لدى النظير.

بشكل عام، التغذية الراجعة المتكررة من المستقبل تحسن الاستجابة لفقدان البيانات والازدحام، ولكن يجب موازنة هذا مع الحمولة المفرطة التي ينتجها مستقبل يرسل كتلة ACK استجابة لكل حزمة تتطلب إقرار استلام. التوجيهات المقدمة أدناه تسعى لتحقيق هذا التوازن.

حزم البيانات داخل الجلسة التي تحتوي على أي كتلة باستثناء ما يلي تتطلب إقرار استلام:

- كتلة ACK
- كتلة العنوان
- كتلة DateTime
- كتلة الحشو
- كتلة الإنهاء
- أخرى؟

الحزم خارج الجلسة، بما في ذلك رسائل المصافحة ورسائل اختبار النظير 5-7، لها آليات الإقرار الخاصة بها. انظر أدناه.

### إقرارات المصافحة

هذه حالات خاصة:

- طلب الرمز المميز (Token Request) يتم إقراره ضمنياً بواسطة إعادة المحاولة (Retry)
- طلب الجلسة (Session Request) يتم إقراره ضمنياً بواسطة إنشاء الجلسة (Session Created) أو إعادة المحاولة (Retry)
- إعادة المحاولة (Retry) يتم إقرارها ضمنياً بواسطة طلب الجلسة (Session Request)
- إنشاء الجلسة (Session Created) يتم إقراره ضمنياً بواسطة تأكيد الجلسة (Session Confirmed)
- تأكيد الجلسة (Session Confirmed) يجب إقراره فوراً

### إرسال كتل ACK

تُستخدم كتل ACK لتأكيد استلام حزم مرحلة البيانات. يجب تضمينها فقط لحزم مرحلة البيانات داخل الجلسة.

يجب الإقرار بكل حزمة مرة واحدة على الأقل، ويجب الإقرار بالحزم التي تتطلب إقراراً مرة واحدة على الأقل خلال حد أقصى للتأخير.

يجب على نقطة النهاية إقرار جميع حزم المصافحة المطلوبة للإقرار فوراً ضمن الحد الأقصى للتأخير، مع الاستثناء التالي. قبل تأكيد المصافحة، قد لا تمتلك نقطة النهاية مفاتيح تشفير رؤوس الحزم لفك تشفير الحزم عند استلامها. لذلك قد تقوم بتخزينها مؤقتاً وإقرارها عندما تصبح المفاتيح المطلوبة متاحة.

نظراً لأن الحزم التي تحتوي على كتل ACK فقط غير خاضعة لمراقبة الازدحام، يجب ألا ترسل نقطة النهاية أكثر من حزمة واحدة من هذا النوع استجابةً لاستقبال حزمة مثيرة لـ ack.

يجب ألا ترسل نقطة النهاية حزمة غير مستوجبة للإقرار استجابةً لحزمة غير مستوجبة للإقرار، حتى لو كانت هناك فجوات في الحزم تسبق الحزمة المستلمة. هذا يتجنب حلقة التغذية الراجعة اللانهائية للإقرارات، والتي يمكن أن تمنع الاتصال من أن يصبح خاملاً في أي وقت. الحزم غير المستوجبة للإقرار يتم الإقرار بها في النهاية عندما ترسل نقطة النهاية كتلة ACK استجابةً لأحداث أخرى.

نقطة النهاية التي ترسل كتل ACK فقط لن تتلقى إقرارات من النظير الخاص بها ما لم يتم تضمين هذه الإقرارات في حزم تحتوي على كتل مثيرة للإقرار. يجب على نقطة النهاية إرسال كتلة ACK مع كتل أخرى عندما تكون هناك حزم جديدة مثيرة للإقرار تحتاج للإقرار بها. عندما تحتاج فقط حزم غير مثيرة للإقرار للإقرار بها، قد تختار نقطة النهاية عدم إرسال كتلة ACK مع الكتل الصادرة حتى يتم استقبال حزمة مثيرة للإقرار.

قد تختار نقطة النهاية التي ترسل فقط حزم لا تستدعي الإقرار أن تضيف أحياناً كتلة تستدعي الإقرار إلى تلك الحزم لضمان استلام إقرار. في هذه الحالة، يجب على نقطة النهاية ألا ترسل كتلة تستدعي الإقرار في جميع الحزم التي قد تكون غير مستدعية للإقرار، لتجنب حلقة تغذية راجعة لا نهائية من الإقرارات.

لمساعدة اكتشاف الفقدان في المرسل، يجب على نقطة النهاية إنشاء وإرسال كتلة ACK دون تأخير عندما تستقبل حزمة تستدعي الإقرار في أي من هذه الحالات:

- عندما تحتوي الحزمة المستلمة على رقم حزمة أقل من حزمة أخرى مثيرة للإقرار تم استلامها
- عندما تحتوي الحزمة على رقم حزمة أكبر من أعلى رقم حزمة مثيرة للإقرار تم استلامها وهناك حزم مفقودة بين تلك الحزمة وهذه الحزمة.
- عندما يتم تعيين علامة الإقرار الفوري في رأس الحزمة

من المتوقع أن تكون الخوارزميات مقاومة للمستقبلات التي لا تتبع الإرشادات المقدمة أعلاه. ومع ذلك، يجب على التطبيق الانحراف عن هذه المتطلبات فقط بعد دراسة دقيقة لتأثيرات الأداء للتغيير، سواء للاتصالات التي تتم بواسطة نقطة النهاية أو للمستخدمين الآخرين في الشبكة.

### تردد ACK

يحدد المستقبل عدد مرات إرسال الإقرارات استجابة للحزم التي تتطلب إقراراً. ينطوي هذا التحديد على مقايضة.

تعتمد نقاط النهاية على الإقرار في الوقت المناسب لاكتشاف الفقدان. تعتمد وحدات التحكم في الازدحام القائمة على النافذة على الإقرارات لإدارة نافذة الازدحام الخاصة بها. في كلتا الحالتين، يمكن أن يؤثر تأخير الإقرارات سلباً على الأداء.

من ناحية أخرى، فإن تقليل تكرار الحزم التي تحمل الإقرارات فقط يقلل من تكلفة إرسال ومعالجة الحزم في كلا النقطتين النهائيتين. يمكن أن يحسن إنتاجية الاتصال على الروابط غير المتماثلة بشدة ويقلل من حجم حركة مرور الإقرارات باستخدام سعة مسار الإرجاع؛ انظر القسم 3 من [RFC-3449](https://tools.ietf.org/html/rfc3449).

يجب على المستقبِل إرسال كتلة ACK بعد استلام حزمتين على الأقل تستدعيان الإقرار. هذه التوصية ذات طبيعة عامة ومتسقة مع التوصيات لسلوك نقاط نهاية TCP [RFC-5681](https://tools.ietf.org/html/rfc5681). معرفة ظروف الشبكة، أو معرفة وحدة التحكم في الازدحام للنظير، أو المزيد من البحث والتجريب قد تقترح استراتيجيات إقرار بديلة بخصائص أداء أفضل.

يمكن للمستقبل معالجة عدة حزم متاحة قبل تحديد ما إذا كان سيرسل كتلة ACK كرد. بشكل عام، يجب على المستقبل عدم تأخير ACK لأكثر من RTT / 6، أو 150 ميلي ثانية كحد أقصى.

علم ack-immediate في رأس حزمة البيانات هو طلب بأن يرسل المستقبل إقرار استلام بعد الاستقبال بوقت قصير، على الأرجح خلال بضعة ميلي ثانية. بشكل عام، يجب على المستقبل ألا يؤخر الإقرار الفوري لأكثر من RTT / 16، أو 5 ميلي ثانية كحد أقصى.

### علامة الإقرار الفوري

المستقبل لا يعرف حجم نافذة الإرسال الخاصة بالمرسل، وبالتالي لا يعرف كم من الوقت يجب أن يؤخر قبل إرسال ACK. علم ACK الفوري في رأس حزمة البيانات هو طريقة مهمة للحفاظ على أقصى إنتاجية من خلال تقليل RTT الفعال. علم ACK الفوري هو البايت 13 من الرأس، البت 0، أي (header[13] & 0x01). عندما يكون مضبوطاً، يُطلب ACK فوري. راجع قسم الرأس القصير أعلاه للتفاصيل.

هناك عدة استراتيجيات محتملة قد يستخدمها المرسل لتحديد متى يتم تعيين علامة immediate-ack:

- يُضبط مرة واحدة كل N حزم، لقيمة N صغيرة
- يُضبط على الحزمة الأخيرة في دفقة من الحزم
- يُضبط عندما تكون نافذة الإرسال ممتلئة تقريباً، على سبيل المثال أكثر من 2/3 ممتلئة
- يُضبط على جميع الحزم التي تحتوي على أجزاء معاد إرسالها

يجب أن تكون علامات ACK الفورية ضرورية فقط على حزم البيانات التي تحتوي على رسائل I2NP أو أجزاء من الرسائل.

### حجم كتلة ACK

عندما يتم إرسال كتلة ACK، يتم تضمين نطاق واحد أو أكثر من الحزم المؤكدة. يقلل تضمين إقرارات الاستلام للحزم الأقدم من احتمالية إعادة الإرسال الزائفة الناتجة عن فقدان كتل ACK المرسلة مسبقاً، على حساب كتل ACK أكبر حجماً.

يجب أن تقر كتل ACK دائماً بالحزم المستلمة مؤخراً، وكلما كانت الحزم أكثر عدم ترتيب، كلما كان من المهم أكثر إرسال كتلة ACK محدثة بسرعة، لمنع النظير من إعلان حزمة كمفقودة وإعادة إرسال الكتل التي تحتويها بشكل زائف. يجب أن تتسع كتلة ACK ضمن حزمة واحدة. إذا لم تتسع، فإن النطاقات الأقدم (تلك التي لها أصغر أرقام الحزم) يتم حذفها.

يقوم المستقبل بتحديد عدد نطاقات ACK التي يتذكرها ويرسلها في كتل ACK، وذلك لتقييد حجم كتل ACK وتجنب استنزاف الموارد. بعد استلام إقرارات الاستلام لكتلة ACK، يجب على المستقبل التوقف عن تتبع نطاقات ACK المؤكدة تلك. يمكن للمرسلين توقع إقرارات الاستلام لمعظم الحزم، ولكن هذا البروتوكول لا يضمن استلام إقرار استلام لكل حزمة يعالجها المستقبل.

من المحتمل أن يؤدي الاحتفاظ بالعديد من نطاقات ACK إلى جعل كتلة ACK كبيرة جداً. يمكن للمستقبل التخلص من نطاقات ACK غير المؤكدة لتحديد حجم كتلة ACK، على حساب زيادة عمليات الإرسال المتكررة من المرسل. هذا ضروري إذا كانت كتلة ACK ستصبح كبيرة جداً بحيث لا تتسع في حزمة واحدة. قد يقوم المستقبلون أيضاً بتحديد حجم كتلة ACK أكثر للحفاظ على مساحة للكتل الأخرى أو لتحديد عرض النطاق الترددي الذي تستهلكه عمليات الإقرار.

يجب على المستقبل الاحتفاظ بنطاق ACK ما لم يتمكن من ضمان أنه لن يقبل لاحقاً حزم بأرقام في ذلك النطاق. الحفاظ على حد أدنى لرقم الحزمة يزيد كلما تم التخلص من النطاقات هو إحدى الطرق لتحقيق ذلك بأقل حالة ممكنة.

يمكن للمستقبلات تجاهل جميع نطاقات الإقرار (ACK ranges)، ولكن يجب عليها الاحتفاظ بأكبر رقم حزمة تم معالجتها بنجاح، حيث يتم استخدام ذلك لاستعادة أرقام الحزم من الحزم اللاحقة.

يصف القسم التالي نهجاً مثالياً لتحديد الحزم التي يجب الإقرار بها في كل كتلة ACK. رغم أن الهدف من هذه الخوارزمية هو توليد إقرار لكل حزمة تتم معالجتها، إلا أنه لا يزال من الممكن فقدان الإقرارات.

### تحديد النطاقات عبر تتبع كتل ACK

عندما يتم إرسال حزمة تحتوي على كتلة ACK، يمكن حفظ حقل Ack Through في تلك الكتلة. عندما يتم تأكيد استلام حزمة تحتوي على كتلة ACK، يمكن للمستقبل التوقف عن تأكيد استلام الحزم التي تكون أقل من أو تساوي حقل Ack Through في كتلة ACK المرسلة.

قد لا يتلقى المستقبل الذي يرسل فقط حزم لا تتطلب إقرارًا، مثل كتل ACK، إقرارًا لفترة زمنية طويلة. قد يؤدي هذا إلى احتفاظ المستقبل بحالة لعدد كبير من كتل ACK لفترة زمنية طويلة، وقد تصبح كتل ACK التي يرسلها كبيرة بشكل غير ضروري. في مثل هذه الحالة، يمكن للمستقبل أن يرسل PING أو كتلة صغيرة أخرى تتطلب إقرارًا من حين لآخر، مثل مرة واحدة لكل رحلة ذهاب وإياب، لاستثارة ACK من النظير.

في الحالات التي لا تتضمن فقدان كتلة ACK، تسمح هذه الخوارزمية بحد أدنى من إعادة ترتيب واحد RTT. في الحالات التي تتضمن فقدان كتلة ACK وإعادة الترتيب، لا يضمن هذا النهج أن كل إقرار استلام يتم رؤيته من قبل المرسل قبل أن يتوقف عن كونه مُضمناً في كتلة ACK. يمكن أن تُستقبل الحزم خارج الترتيب، وقد تُفقد جميع كتل ACK اللاحقة التي تحتويها. في هذه الحالة، يمكن أن تتسبب خوارزمية استعادة الفقدان في إعادة إرسال زائفة، لكن المرسل سيستمر في تحقيق التقدم للأمام.

### الازدحام

وسائل النقل في I2P لا تضمن التسليم المرتب لرسائل I2NP. لذلك، فقدان رسالة Data تحتوي على رسالة I2NP واحدة أو أكثر أو أجزاء منها لا يمنع تسليم رسائل I2NP الأخرى؛ لا يوجد حجب في مقدمة الطابور. يجب على التطبيقات الاستمرار في إرسال رسائل جديدة أثناء مرحلة استرداد الفقدان إذا كانت نافذة الإرسال تسمح بذلك.

### إعادة الإرسال

يجب على المرسل عدم الاحتفاظ بالمحتويات الكاملة للرسالة، ليعيد إرسالها بشكل مطابق (باستثناء رسائل المصافحة، انظر أعلاه). يجب على المرسل تجميع الرسائل التي تحتوي على معلومات محدثة (ACKs، NACKs، والبيانات غير المؤكدة) في كل مرة يرسل فيها رسالة. يجب على المرسل تجنب إعادة إرسال المعلومات من الرسائل بمجرد تأكيد استلامها. يشمل هذا الرسائل التي يتم تأكيد استلامها بعد إعلان فقدانها، والذي يمكن أن يحدث في حالة وجود إعادة ترتيب في الشبكة.

### نافذة

سيتم تحديده لاحقاً. يمكن العثور على التوجيهات العامة في [RFC-9002](https://tools.ietf.org/html/rfc9002).

## ترحيل الاتصال

قد يتغير عنوان IP أو المنفذ الخاص بالنظير أثناء دورة حياة الجلسة. قد يكون سبب تغيير IP هو تناوب العناوين المؤقتة لـ IPv6، أو التغيير الدوري لعنوان IP من قبل مزود خدمة الإنترنت، أو انتقال عميل محمول بين شبكات WiFi وشبكات الخلوية، أو تغييرات أخرى في الشبكة المحلية. قد يكون سبب تغيير المنفذ هو إعادة ربط NAT بعد انتهاء مهلة الربط السابق.

قد يبدو أن عنوان IP أو المنفذ الخاص بالنظير يتغير بسبب هجمات مختلفة على المسار وخارج المسار، بما في ذلك تعديل أو حقن الحزم.

هجرة الاتصال هي العملية التي يتم من خلالها التحقق من صحة نقطة نهاية مصدر جديدة (IP+منفذ)، مع منع التغييرات التي لم يتم التحقق من صحتها. هذه العملية هي نسخة مبسطة من تلك المعرفة في QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000). هذه العملية معرفة فقط لمرحلة البيانات في الجلسة. الهجرة غير مسموحة أثناء المصافحة. يجب التحقق من أن جميع حزم المصافحة قادمة من نفس عنوان IP والمنفذ كما في الحزم المرسلة والمستلمة سابقاً. بمعنى آخر، يجب أن يكون عنوان IP والمنفذ الخاص بالنظير ثابتاً أثناء المصافحة.

### نموذج التهديد

(مقتبس من QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

#### انتحال عنوان النظير

قد ينتحل النظير عنوان المصدر الخاص به لجعل نقطة النهاية ترسل كميات مفرطة من البيانات إلى مضيف غير راغب. إذا أرسلت نقطة النهاية بيانات أكثر بكثير من النظير المنتحل، فقد يتم استخدام ترحيل الاتصال لتضخيم حجم البيانات التي يمكن للمهاجم توليدها تجاه الضحية.

#### انتحال العنوان على المسار

يمكن لمهاجم على المسار أن يتسبب في هجرة اتصال زائفة عن طريق نسخ وإعادة توجيه حزمة بعنوان مزيف بحيث تصل قبل الحزمة الأصلية. ستظهر الحزمة ذات العنوان المزيف وكأنها تأتي من اتصال قيد الهجرة، بينما ستظهر الحزمة الأصلية كمكررة وسيتم إسقاطها. بعد الهجرة الزائفة، سيفشل التحقق من صحة عنوان المصدر لأن الكيان الموجود على عنوان المصدر لا يملك المفاتيح التشفيرية اللازمة لقراءة أو الرد على Path Challenge المرسل إليه حتى لو أراد ذلك.

#### توجيه الحزم خارج المسار

يمكن لمهاجم خارج المسار الذي يستطيع مراقبة الحزم أن يقوم بإعادة توجيه نسخ من الحزم الأصلية إلى نقاط النهاية. إذا وصلت الحزمة المنسوخة قبل الحزمة الأصلية، فسيظهر هذا كإعادة ربط NAT. أي حزمة أصلية ستُرفض كحزمة مكررة. إذا تمكن المهاجم من الاستمرار في إعادة توجيه الحزم، فقد يتمكن من التسبب في الهجرة إلى مسار عبر المهاجم. هذا يضع المهاجم على المسار، مما يمنحه القدرة على مراقبة أو إسقاط جميع الحزم اللاحقة.

#### الآثار المترتبة على الخصوصية

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) حدد تغيير معرفات الاتصال عند تغيير مسارات الشبكة. استخدام معرف اتصال ثابت على مسارات شبكة متعددة سيسمح لمراقب سلبي بربط النشاط بين تلك المسارات. نقطة النهاية التي تتنقل بين الشبكات قد لا ترغب في أن يتم ربط نشاطها من قبل أي كيان آخر غير نظيرها. ومع ذلك، QUIC لا يشفر معرفات الاتصال في الرأس. SSU2 يقوم بذلك، لذا فإن تسريب الخصوصية سيتطلب من المراقب السلبي أيضاً الوصول إلى قاعدة بيانات الشبكة للحصول على مفتاح التعريف المطلوب لفك تشفير معرف الاتصال. حتى مع مفتاح التعريف، هذا ليس هجوماً قوياً، ونحن لا نغير معرفات الاتصال بعد الترحيل في SSU2، حيث أن هذا سيكون تعقيداً كبيراً.

### بدء التحقق من صحة المسار

خلال مرحلة البيانات، يجب على النظراء التحقق من عنوان IP المصدر والمنفذ لكل حزمة بيانات مستلمة. إذا كان عنوان IP أو المنفذ مختلفاً عما تم استلامه سابقاً، والحزمة ليست حزمة مكررة الرقم، والحزمة تم فك تشفيرها بنجاح، تدخل الجلسة في مرحلة التحقق من المسار.

بالإضافة إلى ذلك، يجب على الـ peer التحقق من أن عنوان IP والمنفذ الجديدين صالحان وفقاً لقواعد التحقق المحلية (غير محظورين، ليسا منافذ غير قانونية، إلخ). الـ peers غير مطالبين بدعم الانتقال بين IPv4 و IPv6، وقد يعاملون عنوان IP جديد في عائلة العناوين الأخرى كغير صالح، حيث أن هذا ليس سلوكاً متوقعاً وقد يضيف تعقيداً كبيراً في التنفيذ. عند تلقي حزمة من عنوان IP/منفذ غير صالح، قد يقوم التنفيذ بإسقاطها ببساطة، أو قد يبدأ التحقق من المسار مع عنوان IP/المنفذ القديم.

عند دخول مرحلة التحقق من صحة المسار، اتبع الخطوات التالية:

- ابدأ مؤقت انتهاء صلاحية التحقق من المسار لعدة ثوانٍ، أو عدة أضعاف RTO الحالي (لم يُحدد بعد)
- قلل نافذة الازدحام إلى الحد الأدنى
- قلل PMTU إلى الحد الأدنى (1280)
- أرسل حزمة بيانات تحتوي على كتلة Path Challenge، وكتلة Address (تحتوي على IP/منفذ جديد)، وعادةً كتلة ACK، إلى IP والمنفذ الجديد. تستخدم هذه الحزمة نفس معرف الاتصال ومفاتيح التشفير للجلسة الحالية. يجب أن تحتوي بيانات كتلة Path Challenge على إنتروبيا كافية (8 بايت على الأقل) بحيث لا يمكن انتحالها.
- اختياريًا، أرسل أيضًا Path Challenge إلى IP/المنفذ القديم، مع بيانات كتلة مختلفة. انظر أدناه.
- ابدأ مؤقت انتهاء صلاحية Path Response بناءً على RTO الحالي (عادةً RTT + مضاعف RTTdev)

أثناء مرحلة التحقق من المسار، قد تستمر الجلسة في معالجة الحزم الواردة. سواء من عنوان IP/المنفذ القديم أو الجديد. كما قد تستمر الجلسة في إرسال وتأكيد حزم البيانات. ومع ذلك، يجب أن تبقى نافذة الازدحام وPMTU عند القيم الدنيا أثناء مرحلة التحقق من المسار، لمنع استخدامها في هجمات حجب الخدمة عن طريق إرسال كميات كبيرة من حركة المرور إلى عنوان مزيف.

قد يحاول التنفيذ، ولكن ليس مطلوباً منه، التحقق من صحة مسارات متعددة في نفس الوقت. من المحتمل أن هذا لا يستحق التعقيد. قد يتذكر، ولكن ليس مطلوباً منه، عنوان IP/منفذ سابق كونه تم التحقق من صحته بالفعل، وتخطي التحقق من صحة المسار إذا عاد النظير إلى عنوان IP/منفذ السابق.

إذا تم استلام Path Response يحتوي على البيانات المطابقة التي تم إرسالها في Path Challenge، فإن Path Validation قد نجح. عنوان IP المصدر/المنفذ لرسالة Path Response غير مطلوب أن يكون نفس العنوان الذي تم إرسال Path Challenge إليه.

إذا لم يتم استلام Path Response قبل انتهاء صلاحية مؤقت Path Response، أرسل Path Challenge آخر وضاعف مؤقت Path Response.

إذا لم يتم استلام Path Response قبل انتهاء صلاحية مؤقت Path Validation، فإن Path Validation قد فشل.

### محتويات الرسالة

يجب أن تحتوي رسائل البيانات على الكتل التالية. الترتيب غير محدد باستثناء أن الحشو يجب أن يكون الأخير:

- كتلة Path Challenge أو Path Response. تحتوي Path Challenge على بيانات معتمة، يُوصى بحد أدنى 8 بايت. تحتوي Path Response على البيانات من Path Challenge.
- كتلة العنوان التي تحتوي على عنوان IP الظاهري للمستقبل
- كتلة DateTime
- كتلة ACK
- كتلة Padding

لا يُنصح بتضمين أي كتل أخرى (على سبيل المثال، I2NP) في الرسالة.

يُسمح بتضمين كتلة Path Challenge في الرسالة التي تحتوي على Path Response، لبدء عملية التحقق في الاتجاه الآخر.

كتل Path Challenge و Path Response تستدعي إقرار الاستلام (ACK-eliciting). سيتم إقرار استلام Path Challenge بواسطة رسالة بيانات تحتوي على كتل Path Response و ACK. يجب إقرار استلام Path Response بواسطة رسالة بيانات تحتوي على كتلة ACK.

### التوجيه أثناء التحقق من صحة المسار

مواصفات QUIC غير واضحة بشأن مكان إرسال حزم البيانات أثناء التحقق من المسار - إلى عنوان IP/المنفذ القديم أم الجديد؟ هناك توازن يجب تحقيقه بين الاستجابة السريعة لتغييرات IP/المنفذ، وعدم إرسال حركة المرور إلى عناوين مزيفة. كما يجب عدم السماح للحزم المزيفة بالتأثير بشكل كبير على جلسة موجودة. من المحتمل أن تحدث تغييرات المنفذ فقط بسبب إعادة ربط NAT بعد فترة خمول؛ بينما قد تحدث تغييرات IP أثناء مراحل حركة المرور المكثفة في اتجاه واحد أو كلا الاتجاهين.

الاستراتيجيات خاضعة للبحث والتطوير. الاحتمالات تشمل:

- عدم إرسال حزم البيانات إلى IP/port الجديد حتى يتم التحقق منه
- الاستمرار في إرسال حزم البيانات إلى IP/port القديم حتى يتم التحقق من IP/port الجديد
- إعادة التحقق من IP/port القديم في الوقت نفسه
- عدم إرسال أي بيانات حتى يتم التحقق من IP/port القديم أو الجديد
- استراتيجيات مختلفة لتغيير port فقط مقابل تغيير IP
- استراتيجيات مختلفة لتغيير IPv6 في نفس /32، والذي يُحتمل أن يكون ناتجاً عن دوران العنوان المؤقت

### الاستجابة لتحدي المسار

عند استلام Path Challenge، يجب على النظير الرد بحزمة بيانات تحتوي على Path Response، مع البيانات من Path Challenge.

يجب إرسال Path Response إلى عنوان IP/المنفذ الذي تم استقبال Path Challenge منه. هذا ليس بالضرورة عنوان IP/المنفذ الذي تم تأسيسه مسبقاً للـ peer. هذا يضمن أن التحقق من صحة المسار بواسطة peer ينجح فقط إذا كان المسار يعمل في كلا الاتجاهين. راجع قسم التحقق بعد التغيير المحلي أدناه.

ما لم يكن IP/المنفذ مختلفاً عن IP/المنفذ المعروف سابقاً للنظير، تعامل مع Path Challenge كـ ping بسيط، وأجب ببساطة دون قيد بـ Path Response. لا يحتفظ المستقبل بأي حالة أو يغيرها بناءً على Path Challenge مُستلم. إذا كان IP/المنفذ مختلفاً، يجب على النظير التحقق من أن IP والمنفذ الجديدين صالحان وفقاً لقواعد التحقق المحلية (غير محجوبين، ليسا منافذ غير قانونية، إلخ). النظراء غير مطالبين بدعم الاستجابات عبر عائلات العناوين المختلفة بين IPv4 و IPv6، وقد يتعاملون مع IP جديد في عائلة العناوين الأخرى كغير صالح، حيث أن هذا ليس سلوكاً متوقعاً.

ما لم يكن مقيداً بواسطة التحكم في الازدحام، يجب إرسال Path Response فوراً. يجب على التطبيقات اتخاذ تدابير لتحديد معدل Path Responses أو النطاق الترددي المستخدم إذا لزم الأمر.

كتلة Path Challenge عموماً تكون مصحوبة بكتلة Address في نفس الرسالة. إذا كانت كتلة العنوان تحتوي على IP/port جديد، يمكن للنود التحقق من صحة ذلك IP/port وبدء اختبار النود لذلك IP/port الجديد، مع نود الجلسة أو أي نود آخر. إذا كان النود يعتقد أنه محمي بجدار ناري، وفقط المنفذ تغير، فهذا التغيير على الأرجح بسبب إعادة ربط NAT، واختبار النود الإضافي على الأرجح غير مطلوب.

### التحقق الناجح من المسار

عند نجاح التحقق من صحة المسار، يتم ترحيل الاتصال بالكامل إلى عنوان IP/منفذ الجديد. عند النجاح:

- الخروج من مرحلة التحقق من المسار
- يتم إرسال جميع الحزم إلى العنوان IP والمنفذ الجديدين.
- يتم إزالة القيود على نافذة الازدحام و PMTU، ويُسمح لها بالزيادة. لا تقم ببساطة بإعادتها إلى القيم القديمة، حيث أن المسار الجديد قد يكون له خصائص مختلفة.
- إذا تغير العنوان IP، قم بتعيين RTT المحسوب و RTO إلى القيم الأولية. نظراً لأن تغييرات المنفذ فقط هي عادة نتيجة إعادة ربط NAT أو نشاط middlebox آخر، قد يحتفظ النظير بدلاً من ذلك بحالة التحكم في الازدحام وتقدير وقت الرحلة ذهاباً وإياباً في تلك الحالات بدلاً من العودة إلى القيم الأولية.
- حذف (إبطال) أي tokens مُرسلة أو مُستقبلة للعنوان IP/المنفذ القديم (اختياري)
- إرسال كتلة token جديدة للعنوان IP/المنفذ الجديد (اختياري)

### إلغاء التحقق من المسار

أثناء مرحلة التحقق من المسار، أي حزم صحيحة وغير مكررة يتم استقبالها من عنوان IP/المنفذ القديم ويتم فك تشفيرها بنجاح ستؤدي إلى إلغاء التحقق من المسار. من المهم ألا يؤدي إلغاء التحقق من المسار، الناتج عن حزمة مزيفة، إلى إنهاء جلسة صحيحة أو تعطيلها بشكل كبير.

عند إلغاء التحقق من المسار:

- الخروج من مرحلة التحقق من المسار
- يتم إرسال جميع الحزم إلى العنوان IP والمنفذ القديمين.
- يتم إزالة القيود على نافذة الازدحام و PMTU، ويُسمح لها بالزيادة، أو، اختيارياً، استعادة القيم السابقة
- إعادة إرسال أي حزم بيانات تم إرسالها مسبقاً إلى العنوان IP/المنفذ الجديد إلى العنوان IP/المنفذ القديم.

### فشل في التحقق من صحة المسار

من المهم ألا يؤدي فشل التحقق من المسار، الناجم عن حزمة مزيفة، إلى إنهاء جلسة صالحة أو تعطيلها بشكل كبير.

عند فشل التحقق من صحة المسار:

- الخروج من مرحلة التحقق من المسار
- يتم إرسال جميع الحزم إلى العنوان IP والمنفذ القديمين.
- يتم إزالة القيود على نافذة الازدحام و PMTU، ويُسمح لها بالزيادة.
- اختيارياً، بدء التحقق من المسار على العنوان IP والمنفذ القديمين. إذا فشل، إنهاء الجلسة.
- وإلا، اتباع قواعد انتهاء مهلة الجلسة والإنهاء المعيارية.
- إعادة إرسال أي حزم بيانات تم إرسالها سابقاً إلى العنوان IP/المنفذ الجديدين إلى العنوان IP/المنفذ القديمين.

### التحقق بعد التغيير المحلي

العملية المذكورة أعلاه محددة للأقران الذين يتلقون حزمة من عنوان IP/منفذ متغير. ومع ذلك، يمكن أيضاً بدء هذه العملية في الاتجاه الآخر، من قبل قرين يكتشف أن عنوان IP أو المنفذ الخاص به قد تغير. قد يتمكن القرين من اكتشاف أن عنوان IP المحلي الخاص به قد تغير؛ ومع ذلك، من الأقل احتمالاً بكثير أن يكتشف أن منفذه قد تغير بسبب إعادة ربط NAT. لذلك، هذا الأمر اختياري.

عند استلام تحدي المسار من نظير تغير عنوان IP أو المنفذ الخاص به، يجب على النظير الآخر أن يبدأ تحدي مسار في الاتجاه الآخر.

### استخدام كـ Ping/Pong

يمكن استخدام كتل Path Challenge و Path Response في أي وقت كحزم Ping/Pong. استقبال كتلة Path Challenge لا يغير أي حالة في المستقبل، إلا إذا تم استقباله من عنوان IP/منفذ مختلف.

## جلسات متعددة

يجب ألا ينشئ الأقران جلسات متعددة مع نفس القرين، سواء كان SSU 1 أو 2، أو مع نفس عناوين IP أو عناوين مختلفة. ومع ذلك، قد يحدث هذا إما بسبب أخطاء في البرمجة، أو فقدان رسالة إنهاء الجلسة السابقة، أو في حالة تنافس حيث لم تصل رسالة الإنهاء بعد.

إذا كان لدى Bob جلسة موجودة مع Alice، عندما يتلقى Bob تأكيد الجلسة من Alice، مما يكمل المصافحة وينشئ جلسة جديدة، يجب على Bob:

- ترحيل أي رسائل I2NP صادرة غير مرسلة أو غير مؤكدة من الجلسة القديمة إلى الجديدة
- إرسال إنهاء برمز السبب 22 على الجلسة القديمة
- إزالة الجلسة القديمة واستبدالها بالجديدة

## إنهاء الجلسة

### مرحلة المصافحة

الجلسات في مرحلة المصافحة يتم إنهاؤها عادة ببساطة عن طريق انتهاء المهلة الزمنية، أو عدم الاستجابة أكثر. اختيارياً، قد يتم إنهاؤها عن طريق تضمين كتلة إنهاء في الاستجابة، ولكن معظم الأخطاء غير قابلة للاستجابة لها بسبب نقص المفاتيح التشفيرية. حتى لو كانت المفاتيح متوفرة للاستجابة التي تتضمن كتلة إنهاء، فإنه عادة لا يستحق استهلاك وحدة المعالجة المركزية لتنفيذ DH للاستجابة. استثناء قد يكون كتلة إنهاء في رسالة إعادة المحاولة، والتي تكون غير مكلفة في التوليد.

### مرحلة البيانات

يتم إنهاء الجلسات في مرحلة البيانات عن طريق إرسال رسالة بيانات تتضمن كتلة إنهاء. يجب أن تتضمن هذه الرسالة أيضًا كتلة ACK. قد تتضمن، إذا كانت الجلسة نشطة لفترة كافية بحيث انتهت صلاحية رمز مُرسل سابقًا أو على وشك انتهاء صلاحيته، كتلة رمز جديد. هذه الرسالة لا تتطلب إقرارًا. عند استقبال كتلة إنهاء بأي سبب باستثناء "تم استقبال الإنهاء"، يستجيب النظير برسالة بيانات تحتوي على كتلة إنهاء بالسبب "تم استقبال الإنهاء".

بعد إرسال أو استقبال كتلة إنهاء، يجب أن تدخل الجلسة في مرحلة الإغلاق لفترة زمنية قصوى محددة لاحقاً. حالة الإغلاق ضرورية للحماية من فقدان الحزمة التي تحتوي على كتلة الإنهاء، والحزم المتنقلة في الاتجاه الآخر. أثناء وجودها في مرحلة الإغلاق، لا يوجد متطلب لمعالجة أي حزم إضافية مستقبلة. جلسة في حالة الإغلاق ترسل حزمة تحتوي على كتلة إنهاء كرد على أي حزمة واردة تُعزى إلى الجلسة. يجب على الجلسة تحديد معدل توليد الحزم في حالة الإغلاق. على سبيل المثال، يمكن للجلسة انتظار عدد متزايد تدريجياً من الحزم المستقبلة أو مقدار من الوقت قبل الاستجابة للحزم المستقبلة.

لتقليل الحالة التي يحتفظ بها router للجلسة المغلقة، يمكن للجلسات، ولكن ليس مطلوباً منها، إرسال نفس الحزمة بالضبط مع نفس رقم الحزمة كما هي في الاستجابة لأي حزمة مستلمة. ملاحظة: السماح بإعادة إرسال حزمة الإنهاء هو استثناء من متطلب استخدام رقم حزمة جديد لكل حزمة. إرسال أرقام حزم جديدة مفيد بشكل أساسي لاستعادة الفقدان والتحكم في الازدحام، والتي لا يُتوقع أن تكون ذات صلة بالاتصال المغلق. إعادة إرسال الحزمة الأخيرة تتطلب حالة أقل.

بعد تلقي كتلة إنهاء مع السبب "تم تلقي الإنهاء"، قد تخرج الجلسة من مرحلة الإغلاق.

### تنظيف

عند أي إنهاء عادي أو غير عادي، يجب على أجهزة router أن تصفر أي بيانات مؤقتة في الذاكرة، بما في ذلك مفاتيح التصافح المؤقتة، ومفاتيح التشفير المتماثل، والمعلومات ذات الصلة.

## MTU

المتطلبات تختلف، بناءً على ما إذا كان العنوان المنشور يتم مشاركته مع SSU 1. الحد الأدنى الحالي لـ SSU 1 IPv4 هو 620، وهو صغير جداً بلا شك.

الحد الأدنى لـ MTU الخاص بـ SSU2 هو 1280 لكل من IPv4 و IPv6، وهو نفس ما هو محدد في [RFC-9000](https://tools.ietf.org/html/rfc9000). انظر أدناه. من خلال زيادة الحد الأدنى لـ MTU، ستتسع رسائل tunnel بحجم 1 كيلوبايت ورسائل بناء tunnel القصيرة في datagram واحد، مما يقلل بشكل كبير من مقدار التجزئة المعتاد. هذا يسمح أيضاً بزيادة الحد الأقصى لحجم رسائل I2NP. رسائل التدفق بحجم 1820 بايت يجب أن تتسع في اثنين من datagrams.

يجب على router عدم تمكين SSU2 أو نشر عنوان SSU2 إلا إذا كان MTU لذلك العنوان 1280 على الأقل.

يجب على الـ routers نشر MTU غير افتراضي في كل عنوان router خاص بـ SSU أو SSU2.

### عنوان SSU

عنوان مشترك مع SSU 1، يجب اتباع قواعد SSU 1. IPv4: الافتراضي والحد الأقصى هو 1484. الحد الأدنى هو 1292. (IPv4 MTU + 4) يجب أن يكون مضاعفاً للعدد 16. IPv6: يجب أن يكون منشوراً، الحد الأدنى هو 1280 والحد الأقصى هو 1488. IPv6 MTU يجب أن يكون مضاعفاً للعدد 16.

### عنوان SSU2

IPv4: الافتراضي والحد الأقصى هو 1500. الحد الأدنى هو 1280. IPv6: الافتراضي والحد الأقصى هو 1500. الحد الأدنى هو 1280. لا توجد قواعد للمضاعفات من 16، لكن يُفضل أن يكون مضاعفاً للرقم 2 على الأقل.

### اكتشاف PMTU

بالنسبة لـ SSU 1، يقوم Java I2P الحالي بإجراء اكتشاف PMTU عبر البدء بحزم صغيرة وزيادة الحجم تدريجياً، أو زيادة الحجم بناءً على حجم الحزمة المستلمة. هذا الأسلوب بدائي ويقلل بشكل كبير من الكفاءة. استمرار هذه الميزة في SSU 2 لا يزال قيد التحديد.

تشير الدراسات الحديثة [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) إلى أن حداً أدنى لـ IPv4 يبلغ 1200 أو أكثر سيعمل مع أكثر من 99% من الاتصالات. يتطلب QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) حداً أدنى لحجم حزمة IP يبلغ 1280 بايت.

اقتبس من [RFC-9000](https://tools.ietf.org/html/rfc9000):

يُعرَّف الحد الأقصى لحجم الـ datagram كأكبر حجم لحمولة UDP يمكن إرسالها عبر مسار شبكة باستخدام datagram UDP واحد. يجب عدم استخدام QUIC إذا كان مسار الشبكة لا يستطيع دعم حد أقصى لحجم datagram يبلغ 1200 بايت على الأقل.

يفترض QUIC حد أدنى لحجم حزمة IP يبلغ 1280 بايت على الأقل. هذا هو الحد الأدنى لحجم IPv6 [IPv6] وهو مدعوم أيضاً من قبل معظم شبكات IPv4 الحديثة. بافتراض الحد الأدنى لحجم رأس IP وهو 40 بايت لـ IPv6 و 20 بايت لـ IPv4 وحجم رأس UDP يبلغ 8 بايت، ينتج عن ذلك حد أقصى لحجم البيانات يبلغ 1232 بايت لـ IPv6 و 1252 بايت لـ IPv4. وبالتالي، من المتوقع أن تكون شبكات IPv4 الحديثة وجميع مسارات شبكة IPv6 قادرة على دعم QUIC.

ملاحظة: هذا المتطلب لدعم حمولة UDP بحجم 1200 بايت يحد من المساحة المتاحة لرؤوس IPv6 الإضافية إلى 32 بايت أو خيارات IPv4 إلى 52 بايت إذا كان المسار يدعم فقط الحد الأدنى لـ MTU في IPv6 وهو 1280 بايت. هذا يؤثر على الحزم الأولية والتحقق من صحة المسار.

نهاية الاقتباس

### الحد الأدنى لحجم المصافحة

يتطلب QUIC أن تكون رسائل البيانات الأولية في كلا الاتجاهين بحجم 1200 بايت على الأقل، لمنع هجمات التضخيم والتأكد من أن PMTU يدعم ذلك في كلا الاتجاهين.

يمكننا أن نطلب هذا لـ Session Request و Session Created، بتكلفة كبيرة في عرض النطاق الترددي. ربما يمكننا فعل هذا فقط إذا لم يكن لدينا token، أو بعد استلام رسالة Retry. سيتم تحديدها لاحقاً

يتطلب QUIC ألا يرسل بوب أكثر من ثلاثة أضعاف كمية البيانات المستلمة حتى يتم التحقق من عنوان العميل. يلبي SSU2 هذا المتطلب بطبيعته، لأن رسالة Retry تقريباً بنفس حجم رسالة Token Request، وهي أصغر من رسالة Session Request. كما أن رسالة Retry ترسل مرة واحدة فقط.

### الحد الأدنى لحجم رسالة المسار

يتطلب QUIC أن تكون الرسائل التي تحتوي على كتل PATH_CHALLENGE أو PATH_RESPONSE بحجم 1200 بايت على الأقل، لمنع هجمات التضخيم وضمان أن PMTU يدعمها في كلا الاتجاهين.

يمكننا أن نطلب هذا أيضًا، ولكن بتكلفة كبيرة في عرض النطاق الترددي. ومع ذلك، هذه الحالات يجب أن تكون نادرة. TBD

### الحد الأقصى لحجم رسالة I2NP

IPv4: لا يُفترض تجزئة IP. رأس IP + datagram يبلغ 28 بايت. هذا يفترض عدم وجود خيارات IPv4. الحد الأقصى لحجم الرسالة هو MTU - 28. رأس مرحلة البيانات يبلغ 16 بايت و MAC يبلغ 16 بايت، بإجمالي 32 بايت. حجم الحمولة هو MTU - 60. الحد الأقصى لحمولة مرحلة البيانات هو 1440 لحد أقصى MTU يبلغ 1500. الحد الأقصى لحمولة مرحلة البيانات هو 1220 لحد أدنى MTU يبلغ 1280.

IPv6: لا يُسمح بتجزئة IP. رأس IP + datagram هو 48 بايت. هذا يفترض عدم وجود رؤوس امتداد IPv6. الحد الأقصى لحجم الرسالة هو MTU - 48. رأس مرحلة البيانات هو 16 بايت و MAC هو 16 بايت، بمجموع 32 بايت. حجم الحمولة هو MTU - 80. الحد الأقصى لحمولة مرحلة البيانات هو 1420 لأقصى MTU 1500. الحد الأقصى لحمولة مرحلة البيانات هو 1200 لأدنى MTU 1280.

في SSU 1، كانت الإرشادات تنص على حد أقصى صارم يبلغ حوالي 32 كيلوبايت لرسالة I2NP بناءً على 64 جزءًا كحد أقصى و620 MTU كحد أدنى. بسبب العبء الإضافي للـ LeaseSets المجمعة ومفاتيح الجلسة، كان الحد العملي على مستوى التطبيق أقل بحوالي 6 كيلوبايت، أي حوالي 26 كيلوبايت. يسمح بروتوكول SSU 1 بـ 128 جزءًا ولكن التطبيقات الحالية تحدده بـ 64 جزءًا.

برفع الحد الأدنى لـ MTU إلى 1280، مع حمولة مرحلة البيانات التي تبلغ حوالي 1200، يصبح من الممكن إرسال رسالة SSU 2 بحجم حوالي 76 كيلوبايت في 64 جزء و152 كيلوبايت في 128 جزء. هذا يتيح بسهولة حداً أقصى يبلغ 64 كيلوبايت.

نظراً للتجزئة في tunnels، والتجزئة في SSU 2، فإن احتمالية فقدان الرسائل يزداد بشكل أسي مع حجم الرسالة. نواصل التوصية بحد عملي يبلغ حوالي 10 كيلوبايت على طبقة التطبيق لبيانات I2NP datagrams.

## عملية اختبار النظير

انظر أمان اختبار النظير أعلاه للحصول على تحليل لـ SSU1 Peer Test والأهداف لـ SSU2 Peer Test.

```
Alice Bob Charlie

1.  

        PeerTest ------------------->

        :   Alice RI ------------------->

    2.  PeerTest ------------------->

    3\. <------------------ PeerTest

    :   <---------------- Charlie RI

    4.  <------------------ PeerTest
    5.  <----------------------------------------- PeerTest
    6.  PeerTest ----------------------------------------->
    7.  <----------------------------------------- PeerTest
```
عندما يتم الرفض من قبل Bob:

```
Alice Bob Charlie

1.  PeerTest ------------------->
    2.  <------------------ PeerTest (reject)
```
عندما يرفض تشارلي:

```
Alice Bob Charlie

1.  

        PeerTest ------------------->

        :   Alice RI ------------------->

    2.  PeerTest ------------------->

    3\. <------------------ PeerTest (reject)

    :   (optional: Bob could try another Charlie here)

    4.  <------------------ PeerTest (reject)
```
ملاحظة: قد يتم إرسال RI إما كرسائل I2NP Database Store في كتل I2NP، أو ككتل RI (إذا كانت صغيرة بما فيه الكفاية). قد تكون هذه موجودة في نفس الحزم مع كتل اختبار النظير، إذا كانت صغيرة بما فيه الكفاية.

الرسائل 1-4 هي داخل الجلسة باستخدام كتل Peer Test في رسالة Data. الرسائل 5-7 هي خارج الجلسة باستخدام كتل Peer Test في رسالة Peer Test.

ملاحظة: كما هو الحال في SSU 1، قد تصل الرسائل 4 و 5 بأي ترتيب. قد لا يتم استقبال الرسالة 5 و/أو 7 على الإطلاق إذا كانت Alice محمية بجدار حماية. عندما تصل الرسالة 5 قبل الرسالة 4، لا يمكن لـ Alice إرسال الرسالة 6 فوراً، لأنها لا تملك بعد مفتاح المقدمة الخاص بـ Charlie لتشفير الرأس. عندما تصل الرسالة 4 قبل الرسالة 5، يجب على Alice عدم إرسال الرسالة 6 فوراً، لأنها يجب أن تنتظر لترى إذا كانت الرسالة 5 ستصل دون فتح جدار الحماية بالرسالة 6.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### الإصدارات

اختبار الأقران عبر الإصدارات المختلفة غير مدعوم. التركيبة الوحيدة المسموحة للإصدارات هي عندما تكون جميع الأقران من الإصدار 2.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### إعادة الإرسال

الرسائل 1-4 تكون ضمن الجلسة ومغطاة بواسطة عمليات الإقرار وإعادة الإرسال في مرحلة البيانات. كتل Peer Test تتطلب إقراراً.

قد يتم إعادة إرسال الرسائل 5-7، دون تغيير.

### ملاحظات IPv6

كما هو الحال في SSU 1، يتم دعم اختبار عناوين IPv6، وقد تتم الاتصالات بين Alice-Bob و Alice-Charlie عبر IPv6، إذا أشار Bob و Charlie إلى الدعم بقدرة 'B' في عنوان IPv6 المنشور الخاص بهما. انظر الاقتراح 126 للتفاصيل.

كما هو الحال في SSU 1 قبل الإصدار 0.9.50، ترسل Alice الطلب إلى Bob باستخدام جلسة موجودة عبر وسيلة النقل (IPv4 أو IPv6) التي تريد اختبارها. عندما يتلقى Bob طلباً من Alice عبر IPv4، يجب على Bob أن يختار Charlie يعلن عن عنوان IPv4. عندما يتلقى Bob طلباً من Alice عبر IPv6، يجب على Bob أن يختار Charlie يعلن عن عنوان IPv6. التواصل الفعلي بين Bob-Charlie قد يكون عبر IPv4 أو IPv6 (أي، مستقل عن نوع عنوان Alice). هذا ليس سلوك SSU 1 اعتباراً من الإصدار 0.9.50، حيث يُسمح بالطلبات المختلطة IPv4/v6.

### المعالجة بواسطة Bob

على عكس SSU 1، تحدد أليس عنوان IP والمنفذ المطلوب اختبارهما في الرسالة 1. يجب على بوب التحقق من صحة عنوان IP والمنفذ هذين، ورفضهما برمز 5 إذا كانا غير صحيحين. التحقق الموصى به لعنوان IP هو أنه بالنسبة لـ IPv4، يجب أن يطابق عنوان IP الخاص بأليس، وبالنسبة لـ IPv6، يجب أن تتطابق على الأقل البايتات الثمانية الأولى من عنوان IP. يجب أن يرفض التحقق من المنفذ المنافذ المميزة والمنافذ المخصصة للبروتوكولات المعروفة.

### آلة حالة النتائج

هنا نوثق كيف يمكن لأليس تحديد نتائج اختبار النظير، بناءً على الرسائل المستقبلة. تحسينات SSU2 توفر لنا الفرصة لإصلاح وتحسين وتوثيق آلة حالة نتائج اختبار النظير بشكل أفضل مقارنة بتلك الموجودة في [SSU](/docs/transport/ssu).

لكل نوع عنوان يتم اختباره (IPv4 أو IPv6)، يمكن أن تكون النتيجة واحدة من UNKNOWN أو OK أو FIREWALLED أو SYMNAT. بالإضافة إلى ذلك، قد تتم معالجة أخرى لاكتشاف تغيير IP أو المنفذ، أو منفذ خارجي مختلف عن المنفذ الداخلي.

مشاكل مع آلة الحالة الموثقة لـ SSU:

- نحن لا نرسل أبداً الرسالة 6 ما لم نحصل على الرسالة 5، لذلك لا نعرف أبداً إذا كنا SYMNAT
- إذا حصلنا فعلاً على الرسائل 4 و 7، كيف يمكن أن نكون SYMNAT
- إذا لم يتطابق عنوان IP لكن المنفذ تطابق، فنحن لسنا SYMNAT، لقد قمنا فقط بتغيير عنوان IP الخاص بنا

لذلك، على النقيض من SSU، نوصي بالانتظار عدة ثوانٍ بعد الحصول على الرسالة 4، ثم إرسال الرسالة 6 حتى لو لم يتم استلام الرسالة 5.

ملخص آلة الحالة، بناءً على ما إذا كانت الرسائل 4 و 5 و 7 قد تم استلامها (نعم أو لا)، كما يلي:

```
4 5 7 Result Notes

----- ------ -----n n n UNKNOWN y n n FIREWALLED (unless currently SYMNAT) n y n OK (unless currently SYMNAT, which is unlikely) y y n OK (unless currently SYMNAT, which is unlikely) n n y n/a (can't send msg 6) y n y FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5) n y y n/a (can't send msg 6) y y y OK
```
آلة حالة أكثر تفصيلاً، مع فحوصات لعنوان IP/المنفذ المستلم في كتلة العنوان للرسالة 7، موضحة أدناه. أحد التحديات هو تحديد ما إذا كنت أنت (أليس) من لديه symmetric NAT، أم تشارلي.

يُنصح بإجراء معالجة لاحقة أو منطق إضافي لتأكيد انتقالات الحالة من خلال طلب نفس النتائج في اختبارين أو أكثر من اختبارات النظراء.

يُوصى أيضاً بالحصول على التحقق والتأكيد من عنوان IP/المنفذ من خلال اختبارين أو أكثر، أو مع كتلة العنوان في رسائل Session Created، ولكن هذا خارج نطاق هذه المواصفة.

```
If Alice does not get msg 5:

If Alice does not get msg 4: -> UNKNOWN If Alice does not get msg 7: -> UNKNOWN If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED If Alice gets msgs 4/7 and IP matches, port does not match: -> SYMNAT, but needs confirmation with 2nd test If Alice gets msgs 4/7 and IP does not match, port matches: -> FIREWALLED, address change? If Alice gets msgs 4/7 and both IP and port do not match: -> SYMNAT, address change?

    If Alice gets msg 5: If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN (in SSU2 have to stop here) If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN If Alice gets msgs 4/5/7 and IP/port match: -> OK If Alice gets msgs 4/5/7 and IP matches, port does not match: -> OK, charlie is probably sym. natted If Alice gets msgs 4/5/7 and IP does not match, port matches: -> OK, address change? If Alice gets msgs 4/5/7 and both IP and port do not match: -> OK, address change?
```
## عملية الترحيل

انظر أمان الترحيل أعلاه لتحليل SSU1 Relay وأهداف SSU2 Relay.

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  

        RelayRequest ---------------------->

        :   Alice RI ------------>

    2.  RelayIntro ----------->

    3.  <-------------- RelayResponse

    4.  <-------------- RelayResponse

    5.  <-------------------------------------------- HolePunch

    6.  SessionRequest -------------------------------------------->

    7.  <-------------------------------------------- SessionCreated

    8.  SessionConfirmed ------------------------------------------>
```
عند الرفض من قبل Bob:

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  RelayRequest ---------------------->
    2.  <-------------- RelayResponse
```
عندما يتم رفضه من قِبل تشارلي:

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  

        RelayRequest ---------------------->

        :   Alice RI ------------>

    2.  RelayIntro ----------->

    3.  <-------------- RelayResponse

    4.  <-------------- RelayResponse
```
ملاحظة: قد يتم إرسال RI إما كرسائل I2NP Database Store في كتل I2NP، أو ككتل RI (إذا كانت صغيرة بما فيه الكفاية). قد تكون هذه موجودة في نفس الحزم مثل كتل الترحيل، إذا كانت صغيرة بما فيه الكفاية.

في SSU 1، تحتوي معلومات router الخاصة بـ Charlie على عنوان IP والمنفذ ومفتاح التقديم وعلامة التتابع وتاريخ انتهاء الصلاحية لكل مُقدم.

في SSU 2، تحتوي معلومات router الخاصة بـ Charlie على router hash وrelay tag وتاريخ انتهاء الصلاحية لكل introducer.

يجب على أليس تقليل عدد الرحلات ذهاباً وإياباً المطلوبة من خلال اختيار مُقدم (بوب) لديها اتصال معه بالفعل أولاً. ثانياً، إذا لم يكن هناك أي مُقدم، تختار مُقدماً لديها معلومات router الخاصة به بالفعل.

يجب أيضاً دعم التتابع عبر الإصدارات إن أمكن. هذا سيسهل الانتقال التدريجي من SSU 1 إلى SSU 2. مجموعات الإصدارات المسموحة هي (مهمة مؤجلة):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### إعادة الإرسال

طلبات التتابع (Relay Request) وتقديم التتابع (Relay Intro) واستجابات التتابع (Relay Response) جميعها ضمن الجلسة ومغطاة بمرحلة البيانات لعمليات الإقرار وإعادة الإرسال. كتل طلبات التتابع وتقديم التتابع واستجابات التتابع تستدعي الإقرار.

لاحظ أنه عادةً ما سيستجيب تشارلي فوراً لـ Relay Intro بـ Relay Response، والذي يجب أن يتضمن كتلة ACK. في هذه الحالة، لا حاجة لرسالة منفصلة تحتوي على كتلة ACK.

قد يتم إعادة إرسال hole punch، كما في SSU 1.

على عكس رسائل I2NP، فإن رسائل Relay لا تحتوي على معرفات فريدة، لذا يجب اكتشاف المكررات بواسطة آلة حالة المرحل باستخدام الـ nonce. قد تحتاج التطبيقات أيضاً إلى الاحتفاظ بذاكرة تخزين مؤقت للـ nonces المستخدمة مؤخراً، بحيث يمكن اكتشاف المكررات المستلمة حتى بعد انتهاء آلة الحالة الخاصة بذلك الـ nonce.

### IPv4/v6

جميع ميزات ترحيل SSU 1 مدعومة، بما في ذلك تلك الموثقة في [Prop158](/proposals/158-ipv6-transport-enhancements) والمدعومة اعتباراً من الإصدار 0.9.50. مقدمات IPv4 و IPv6 مدعومة. يمكن إرسال طلب ترحيل عبر جلسة IPv4 لمقدمة IPv6، ويمكن إرسال طلب ترحيل عبر جلسة IPv6 لمقدمة IPv4.

### معالجة بواسطة أليس

فيما يلي الاختلافات عن SSU 1 والتوصيات لتنفيذ SSU 2.

#### اختيار المُقدِّم

في SSU 1، تكون المقدمة غير مكلفة نسبياً، وتقوم Alice عموماً بإرسال طلبات الترحيل إلى جميع المقدمين. في SSU 2، تكون المقدمة أكثر تكلفة، حيث يجب أولاً إنشاء اتصال مع مقدم. لتقليل زمن الاستجابة والأعباء الإضافية للمقدمة، فإن خطوات المعالجة الموصى بها هي كما يلي:

- تجاهل أي introducers منتهية الصلاحية بناءً على قيمة iexp في العنوان
- إذا كان اتصال SSU2 مُنشأً بالفعل مع introducer واحد أو أكثر، اختر واحداً وأرسل Relay Request إلى ذلك introducer فقط.
- وإلا، إذا كان Router Info معروفاً محلياً لـ introducer واحد أو أكثر، اختر واحداً واتصل بذلك introducer فقط.
- وإلا، ابحث عن Router Infos لجميع introducers، اتصل بالـ introducer الذي يتم استلام Router Info الخاص به أولاً.

#### معالجة الاستجابة

في كل من SSU 1 و SSU 2، قد يتم استقبال استجابة الترحيل و Hole Punch بأي ترتيب، أو قد لا يتم استقبالهما على الإطلاق.

في SSU 1، تستقبل Alice عادة الـ Relay Response (1 RTT) قبل الـ Hole Punch (1 1/2 RTT). قد لا يكون هذا موثقاً جيداً في تلك المواصفات، ولكن يجب على Alice استقبال الـ Relay Response من Bob قبل المتابعة، لاستقبال عنوان IP الخاص بـ Charlie. إذا تم استقبال الـ Hole Punch أولاً، فلن تتعرف عليه Alice، لأنه لا يحتوي على بيانات وعنوان IP المصدر غير معروف. بعد استقبال الـ Relay Response، يجب على Alice انتظار إما استقبال الـ Hole Punch من Charlie، أو تأخير قصير (يُنصح بـ 500 مللي ثانية) قبل بدء المصافحة مع Charlie.

في SSU 2، ستتلقى Alice عادةً Hole Punch (1 1/2 RTT) قبل Relay Response (2 RTT). إن SSU 2 Hole Punch أسهل في المعالجة من SSU 1، لأنها رسالة كاملة بمعرفات اتصال محددة (مشتقة من relay nonce) ومحتويات تشمل عنوان IP الخاص بـ Charlie. تحتوي Relay Response (رسالة Data) ورسالة Hole Punch على نفس كتلة Relay Response الموقعة. لذلك، يمكن لـ Alice بدء المصافحة مع Charlie بعد إما تلقي Hole Punch من Charlie، أو تلقي Relay Response من Bob.

يتضمن التحقق من التوقيع للثقب المباشر (Hole Punch) hash الخاص بـ router المُعرِّف (بوب). إذا تم إرسال طلبات الترحيل (Relay Requests) إلى أكثر من مُعرِّف واحد، فهناك عدة خيارات للتحقق من صحة التوقيع:

- جرب كل hash تم إرسال طلب إليه
- استخدم nonces مختلفة لكل introducer، واستخدم ذلك لتحديد أي introducer كان هذا Hole Punch ردًا عليه
- لا تعيد التحقق من التوقيع إذا كان المحتوى مطابقًا لذلك الموجود في Relay Response، إذا تم استلامه بالفعل
- لا تتحقق من التوقيع على الإطلاق

إذا كان Charlie خلف NAT متماثل، فإن المنفذ المُبلغ عنه في Relay Response و Hole Punch قد لا يكون دقيقاً. لذلك، يجب على Alice التحقق من منفذ مصدر UDP لرسالة Hole Punch، واستخدام ذلك إذا كان مختلفاً عن المنفذ المُبلغ عنه.

### طلبات العلامات من قِبل Bob

في SSU 1، يمكن لـ Alice فقط طلب tag، في Session Request. لا يمكن لـ Bob أبداً طلب tag، ولا يمكن لـ Alice أن تعمل كوسيط لـ Bob.

في SSU2، تطلب Alice عمومًا علامة في طلب الجلسة، لكن يمكن لـ Alice أو Bob أيضًا طلب علامة في مرحلة البيانات. Bob عمومًا لا يكون محجوبًا بجدار ناري بعد تلقي طلب وارد، لكن يمكن أن يحدث ذلك بعد ترحيل، أو قد تتغير حالة Bob، أو قد يطلب مقدم تعريف لنوع العنوان الآخر (IPv4/v6). لذلك، في SSU2، من الممكن لكل من Alice و Bob أن يكونا في نفس الوقت كمرحلات للطرف الآخر.

## معلومات Router المنشورة

### خصائص العنوان

خصائص العناوين التالية قد يتم نشرها، بدون تغيير من SSU 1، بما في ذلك التغييرات في [Prop158](/proposals/158-ipv6-transport-enhancements) المدعومة اعتباراً من API 0.9.50:

- caps: قدرات [B,C,4,6]
- host: عنوان IP (IPv4 أو IPv6). عنوان IPv6 المختصر (مع "::") مسموح. قد يكون موجوداً أو غير موجود إذا كان محمياً بجدار حماية. أسماء المضيفين غير مسموحة.
- iexp[0-2]: انتهاء صلاحية هذا المُقدِم. أرقام ASCII، بالثواني منذ بداية العصر. موجود فقط إذا كان محمياً بجدار حماية، والمُقدِمون مطلوبون. اختياري (حتى لو كانت خصائص أخرى لهذا المُقدِم موجودة).
- ihost[0-2]: عنوان IP الخاص بالمُقدِم (IPv4 أو IPv6). عنوان IPv6 المختصر (مع "::") مسموح. موجود فقط إذا كان محمياً بجدار حماية، والمُقدِمون مطلوبون. أسماء المضيفين غير مسموحة. عنوان SSU فقط.
- ikey[0-2]: مفتاح التقديم الخاص بالمُقدِم مُرمز Base 64. موجود فقط إذا كان محمياً بجدار حماية، والمُقدِمون مطلوبون. عنوان SSU فقط.
- iport[0-2]: منفذ المُقدِم 1024 - 65535. موجود فقط إذا كان محمياً بجدار حماية، والمُقدِمون مطلوبون. عنوان SSU فقط.
- itag[0-2]: علامة المُقدِم 1 - (2**32 - 1) أرقام ASCII. موجود فقط إذا كان محمياً بجدار حماية، والمُقدِمون مطلوبون.
- key: مفتاح التقديم مُرمز Base 64.
- mtu: اختياري. راجع قسم MTU أعلاه.
- port: 1024 - 65535 قد يكون موجوداً أو غير موجود إذا كان محمياً بجدار حماية.

### العناوين المنشورة

سيكون لدى RouterAddress المنشور (جزء من RouterInfo) معرف بروتوكول إما "SSU" أو "SSU2".

يجب أن يحتوي RouterAddress على ثلاث خيارات للإشارة إلى دعم SSU2:

- s=(مفتاح Base64) مفتاح Noise العام الثابت الحالي (s) لهذا RouterAddress. مُرمز بـ Base 64 باستخدام أبجدية I2P Base 64 المعيارية. 32 بايت في النظام الثنائي، 44 بايت كـ Base 64 مُرمز، مفتاح X25519 عام little-endian.
- i=(مفتاح Base64) مفتاح التقديم الحالي لتشفير الرؤوس لهذا RouterAddress. مُرمز بـ Base 64 باستخدام أبجدية I2P Base 64 المعيارية. 32 بايت في النظام الثنائي، 44 بايت كـ Base 64 مُرمز، مفتاح ChaCha20 big-endian.
- v=2 الإصدار الحالي (2). عند النشر كـ "SSU"، يُضمن الدعم الإضافي للإصدار 1. الدعم للإصدارات المستقبلية سيكون بقيم مفصولة بفواصل، مثل v=2,3 يجب على التطبيق التحقق من التوافق، بما في ذلك عدة إصدارات إذا كانت فاصلة موجودة. الإصدارات المفصولة بفواصل يجب أن تكون مرتبة عددياً.

يجب على Alice التحقق من وجود وصحة جميع الخيارات الثلاثة قبل الاتصال باستخدام بروتوكول SSU2.

عندما يتم النشر كـ "SSU" مع خيارات "s" و "i" و "v"، ومع خيارات "host" و "port"، يجب على الـ router قبول الاتصالات الواردة على ذلك المضيف والمنفذ لكل من بروتوكولي SSU و SSU2، والكشف التلقائي عن إصدار البروتوكول.

عندما يتم نشره كـ "SSU2" مع خيارات "s" و "i" و "v"، ومع خيارات "host" و "port"، يقبل الـ router الاتصالات الواردة على ذلك المضيف والمنفذ لبروتوكول SSU2 فقط.

إذا كان router يدعم اتصالات SSU1 و SSU2 ولكن لا يطبق الكشف التلقائي للإصدار للاتصالات الواردة، فيجب عليه الإعلان عن عناوين "SSU" و "SSU2" كليهما، وتضمين خيارات SSU2 في عنوان "SSU2" فقط. يجب على router تعيين قيمة تكلفة أقل (أولوية أعلى) في عنوان "SSU2" من عنوان "SSU"، حتى يُفضل SSU2.

إذا تم نشر عدة RouterAddresses من نوع SSU2 (سواء كـ "SSU" أو "SSU2") في نفس RouterInfo (لعناوين IP أو منافذ إضافية)، فيجب أن تحتوي جميع العناوين التي تحدد نفس المنفذ على خيارات وقيم SSU2 متطابقة. وعلى وجه الخصوص، يجب أن تحتوي جميعها على نفس المفتاح الثابت "s" ومفتاح التقديم "i".

#### المُقدِّمون

عندما يتم النشر كـ SSU أو SSU2 مع introducers، تكون الخيارات التالية متوفرة:

- ih[0-2]=(Base64 hash) hash الخاص بـ router للمُقدِم. مُرمز بـ Base 64 باستخدام أبجدية I2P القياسية لـ Base 64. 32 بايت في النظام الثنائي، 44 بايت مُرمز بـ Base 64
- iexp[0-2]: انتهاء صلاحية هذا المُقدِم. لم يتغير عن SSU 1.
- itag[0-2]: علامة المُقدِم 1 - (2**32 - 1) لم تتغير عن SSU 1.

الخيارات التالية مخصصة لـ SSU فقط ولا تُستخدم مع SSU2. في SSU2، تحصل Alice على هذه المعلومات من RI الخاص بـ Charlie بدلاً من ذلك.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

يجب على الـ router عدم نشر المضيف أو المنفذ في العنوان عند نشر المقدمين. يجب على الـ router نشر قدرات 4 و/أو 6 في العنوان عند نشر المقدمين للإشارة إلى دعم IPv4 و/أو IPv6. هذا مماثل للممارسة الحالية لعناوين SSU 1 الحديثة.

ملاحظة: إذا تم النشر كـ SSU، وكان هناك مزيج من مُقدمي SSU 1 و SSU2، يجب أن يكون مُقدمو SSU 1 في الفهارس الأقل ومُقدمو SSU2 في الفهارس الأعلى، للتوافق مع أجهزة router الأقدم.

### عنوان SSU2 غير منشور

إذا لم تقم Alice بنشر عنوان SSU2 الخاص بها (كـ "SSU" أو "SSU2") للاتصالات الواردة، فيجب عليها نشر عنوان router "SSU2" يحتوي فقط على مفتاحها الثابت وإصدار SSU2، بحيث يمكن لـ Bob التحقق من صحة المفتاح بعد استلام RouterInfo الخاص بـ Alice في الجزء الثاني من Session Confirmed.

- s=(Base64 key) كما هو معرف أعلاه للعناوين المنشورة.
- i=(Base64 key) كما هو معرف أعلاه للعناوين المنشورة.
- v=2 كما هو معرف أعلاه للعناوين المنشورة.

عنوان router هذا لن يحتوي على خيارات "host" أو "port"، حيث أن هذه غير مطلوبة لاتصالات SSU2 الصادرة. التكلفة المنشورة لهذا العنوان لا تهم بدقة، حيث أنه للاتصالات الواردة فقط؛ ومع ذلك، قد يكون من المفيد لـ routers الأخرى إذا تم تعيين التكلفة أعلى (أولوية أقل) من العناوين الأخرى. القيمة المقترحة هي 14.

يمكن لأليس أيضاً أن تضيف ببساطة خيارات "i" و "s" و "v" إلى عنوان "SSU" منشور موجود.

### تدوير المفتاح العام و IV

استخدام نفس المفاتيح الثابتة لـ NTCP2 و SSU2 مسموح، ولكنه غير مُوصى به.

بسبب التخزين المؤقت لمعلومات الـ RouterInfos، يجب على أجهزة الـ router عدم تدوير المفتاح العام الثابت أو الـ IV أثناء تشغيل الـ router، سواء كان في عنوان منشور أم لا. يجب على أجهزة الـ router تخزين هذا المفتاح والـ IV بشكل دائم لإعادة الاستخدام بعد إعادة التشغيل الفورية، حتى تستمر الاتصالات الواردة في العمل، ولا تنكشف أوقات إعادة التشغيل. يجب على أجهزة الـ router تخزين وقت الإغلاق الأخير بشكل دائم، أو تحديده بطريقة أخرى، بحيث يمكن حساب فترة التوقف السابقة عند بدء التشغيل.

مع مراعاة المخاوف حول كشف أوقات إعادة التشغيل، قد تقوم أجهزة router بتدوير هذا المفتاح أو IV عند بدء التشغيل إذا كان router متوقفاً سابقاً لفترة من الوقت (عدة أيام على الأقل).

إذا كان لدى الراوتر أي RouterAddresses منشورة من نوع SSU2 (كـ SSU أو SSU2)، فإن الحد الأدنى لوقت التوقف قبل التبديل يجب أن يكون أطول بكثير، على سبيل المثال شهر واحد، إلا إذا تغير عنوان IP المحلي أو قام الراوتر بـ "rekeys".

إذا كان الـ router يحتوي على أي عناوين SSU RouterAddresses منشورة، ولكن ليس SSU2 (كـ SSU أو SSU2)، فيجب أن يكون الحد الأدنى لوقت التوقف قبل التدوير أطول، على سبيل المثال يوم واحد، إلا إذا تغير عنوان IP المحلي أو قام الـ router بـ "rekeys". ينطبق هذا حتى لو كان عنوان SSU المنشور يحتوي على introducers.

إذا لم يكن لدى الـ router أي RouterAddresses منشورة (SSU أو SSU2 أو SSU)، فقد يكون الحد الأدنى لوقت التوقف قبل التبديل قصيراً يصل إلى ساعتين، حتى لو تغير عنوان IP، ما لم يقم الـ router بـ"rekeys".

إذا قام الـ router بـ "rekeys" إلى Router Hash مختلف، يجب عليه توليد noise key و intro key جديدين أيضاً.

يجب أن تكون التطبيقات على علم بأن تغيير المفتاح العام الثابت أو IV سيمنع الاتصالات الواردة من SSU2 من routers التي قامت بتخزين RouterInfo أقدم مؤقتاً. يجب أن تأخذ عملية نشر RouterInfo، واختيار نظراء tunnel (بما في ذلك كل من OBGW وأقرب hop للـ IB)، واختيار zero-hop tunnel، واختيار النقل، واستراتيجيات التطبيق الأخرى هذا الأمر في الاعتبار.

دوران مفتاح المقدمة يخضع لنفس القواعد المطبقة على دوران المفاتيح.

ملاحظة: قد يتم تعديل الحد الأدنى لوقت التوقف قبل إعادة إنتاج المفاتيح لضمان صحة الشبكة، ولمنع إعادة البذر بواسطة router متوقف لفترة زمنية معتدلة.

#### إخفاء الهوية

إنكار المسؤولية ليس هدفاً. راجع النظرة العامة أعلاه.

يتم تخصيص خصائص لكل نمط تصف السرية المقدمة للمفتاح العام الثابت للمُبادِر، وللمفتاح العام الثابت للمُجيب. الافتراضات الأساسية هي أن المفاتيح الخاصة المؤقتة آمنة، وأن الأطراف تلغي المصافحة إذا تلقوا مفتاحًا عامًا ثابتًا من الطرف الآخر لا يثقون به.

يتناول هذا القسم فقط تسريب الهوية من خلال حقول المفاتيح العامة الثابتة في عمليات المصافحة. بالطبع، قد تتعرض هويات المشاركين في Noise للكشف من خلال وسائل أخرى، بما في ذلك حقول الحمولة، أو تحليل حركة البيانات، أو البيانات الوصفية مثل عناوين IP.

أليس: (8) مشفرة بسرية أمامية إلى طرف مُصدق عليه.

بوب: (3) غير منقول، ولكن يمكن للمهاجم السلبي فحص المرشحين للمفتاح الخاص للمستجيب وتحديد ما إذا كان المرشح صحيحًا أم لا.

ينشر Bob مفتاحه العام الثابت في netDb. قد لا تفعل Alice ذلك، ولكن يجب أن تتضمنه في RI المرسل إلى Bob.

## إرشادات الحزم

### إنشاء الحزم الصادرة

الخطوات الأساسية لرسائل Handshake (Session Request/Created/Confirmed, Retry)، بالترتيب:

- إنشاء رأس بحجم 16 أو 32 بايت
- إنشاء الحمولة
- تطبيق mixHash() على الرأس (باستثناء Retry)
- تشفير الحمولة باستخدام Noise (باستثناء Retry، استخدم ChaChaPoly مع الرأس كبيانات إضافية)
- تشفير الرأس، وبالنسبة لـ Session Request/Created، المفتاح المؤقت

الخطوات الأساسية لرسائل مرحلة البيانات، بالترتيب:

- إنشاء رأس بحجم 16 بايت
- إنشاء الحمولة
- تشفير الحمولة باستخدام ChaChaPoly مع استخدام الرأس كـ AD
- تشفير الرأس

### معالجة الحزم الواردة

#### ملخص

المعالجة الأولية لجميع الرسائل الواردة:

- فك تشفير أول 8 بايت من الرأس (معرف اتصال الوجهة) باستخدام مفتاح المقدمة
- البحث عن الاتصال بواسطة معرف اتصال الوجهة
- إذا تم العثور على الاتصال وكان في مرحلة البيانات، انتقل إلى قسم مرحلة البيانات
- إذا لم يتم العثور على الاتصال، انتقل إلى قسم المصافحة
- ملاحظة: رسائل Peer Test و Hole Punch قد يتم البحث عنها أيضاً بواسطة معرف اتصال الوجهة المُنشأ من اختبار أو ترحيل nonce.

معالجة رسائل المصافحة (Session Request/Created/Confirmed, Retry, Token Request) والرسائل الأخرى خارج الجلسة (Peer Test, Hole Punch):

- فك تشفير البايتات 8-15 من الرأس (نوع الحزمة، الإصدار، ومعرف الشبكة) باستخدام intro key. إذا كان Session Request أو Token Request أو Peer Test أو Hole Punch صالحاً، تابع
- إذا لم تكن رسالة صالحة، ابحث عن اتصال صادر معلق حسب عنوان IP/منفذ مصدر الحزمة، تعامل مع الحزمة كـ Session Created أو Retry. أعد فك تشفير أول 8 بايتات من الرأس بالمفتاح الصحيح، والبايتات 8-15 من الرأس (نوع الحزمة، الإصدار، ومعرف الشبكة). إذا كان Session Created أو Retry صالحاً، تابع
- إذا لم تكن رسالة صالحة، فشل، أو ضع في الطابور كحزمة محتملة خارجة عن الترتيب في مرحلة البيانات
- بالنسبة لـ Session Request/Created و Retry و Token Request و Peer Test و Hole Punch، فك تشفير البايتات 16-31 من الرأس
- بالنسبة لـ Session Request/Created، فك تشفير المفتاح المؤقت
- تحقق من صحة جميع حقول الرأس، توقف إذا لم تكن صالحة
- mixHash() الرأس
- بالنسبة لـ Session Request/Created/Confirmed، فك تشفير الحمولة باستخدام Noise
- بالنسبة لـ Retry ومرحلة البيانات، فك تشفير الحمولة باستخدام ChaChaPoly
- معالج الرأس والحمولة

معالجة رسائل مرحلة البيانات:

- فك تشفير البايتات 8-15 من الرأس (نوع الحزمة، الإصدار، ومعرف الشبكة) بالمفتاح الصحيح
- فك تشفير الحمولة باستخدام ChaChaPoly مع استخدام الرأس كـ AD
- معالجة الرأس والحمولة

#### التفاصيل

في SSU 1، تصنيف الحزم الواردة صعب، لأنه لا يوجد رأس للإشارة إلى رقم الجلسة. يجب على أجهزة التوجيه أولاً مطابقة عنوان IP المصدر والمنفذ مع حالة نظير موجودة، وإذا لم توجد، محاولة فك تشفير متعددة بمفاتيح مختلفة للعثور على حالة النظير المناسبة أو بدء واحدة جديدة. في حالة تغير عنوان IP المصدر أو المنفذ لجلسة موجودة، ربما بسبب سلوك NAT، قد يستخدم الموجه خوارزميات تحليل مكلفة لمحاولة مطابقة الحزمة مع جلسة موجودة واستعادة المحتويات.

تم تصميم SSU 2 لتقليل جهد تصنيف الحزم الواردة مع الحفاظ على مقاومة DPI والتهديدات الأخرى على المسار. يتم تضمين رقم Connection ID في الرأس لجميع أنواع الرسائل، ومشفر (مشوش) باستخدام ChaCha20 بمفتاح ونونس معروفين. بالإضافة إلى ذلك، يتم أيضاً تضمين نوع الرسالة في الرأس (مشفر بحماية الرأس إلى مفتاح معروف ثم مشوش بـ ChaCha20) ويمكن استخدامه للتصنيف الإضافي. في أي حال من الأحوال، لا تكون عملية DH التجريبية أو عملية التشفير غير المتماثلة الأخرى ضرورية لتصنيف الحزمة.

بالنسبة لجميع الرسائل تقريباً من جميع الأقران، فإن مفتاح ChaCha20 لتشفير معرف الاتصال هو مفتاح التعريف الخاص بـ router الوجهة كما هو منشور في netDb.

الاستثناءات الوحيدة هي الرسائل الأولى المرسلة من Bob إلى Alice (Session Created أو Retry) حيث لا يعرف Bob بعد مفتاح التقديم الخاص بـ Alice. في هذه الحالات، يُستخدم مفتاح التقديم الخاص بـ Bob كمفتاح.

تم تصميم البروتوكول لتقليل معالجة تصنيف الحزم التي قد تتطلب عمليات تشفير إضافية في خطوات احتياطية متعددة أو استدلالات معقدة. بالإضافة إلى ذلك، فإن الغالبية العظمى من الحزم المستلمة لن تتطلب بحثاً احتياطياً (مكلف التكلفة محتملاً) حسب عنوان IP/المنفذ المصدر وفك تشفير ثاني للرأس. فقط Session Created و Retry (وربما أخرى سيتم تحديدها لاحقاً) ستتطلب المعالجة الاحتياطية. إذا غيّرت نقطة النهاية عنوان IP أو المنفذ بعد إنشاء الجلسة، فإن معرف الاتصال لا يزال يُستخدم للبحث عن الجلسة. ليس من الضروري أبداً استخدام الاستدلالات للعثور على الجلسة، على سبيل المثال من خلال البحث عن جلسة مختلفة بنفس عنوان IP ولكن بمنفذ مختلف.

لذلك، خطوات المعالجة الموصى بها في منطق حلقة المستقبل هي:

1) فك تشفير أول 8 بايتات باستخدام ChaCha20 مع مفتاح التقديم المحلي، لاسترداد معرف اتصال الوجهة. إذا كان معرف الاتصال يطابق جلسة واردة حالية أو معلقة:

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

2) إذا كان معرف الاتصال لا يطابق جلسة حالية: تحقق من أن رأس النص العادي في البايتات 8-15 صالح (دون القيام بأي عملية حماية رأس). تأكد من أن معرف الشبكة وإصدار البروتوكول صالحان، وأن نوع الرسالة هو Session Request، أو نوع رسالة آخر مسموح خارج الجلسة (TBD).

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

3) البحث عن جلسة صادرة معلقة بواسطة عنوان IP المصدر/المنفذ الخاص بالحزمة.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

4) إذا كان SSU 1 يعمل على نفس المنفذ، حاول معالجة الرسالة كحزمة SSU 1.

#### معالجة الأخطاء

بشكل عام، يجب ألا يتم تدمير الجلسة (في مرحلة المصافحة أو مرحلة البيانات) أبداً بعد استلام حزمة تحتوي على نوع رسالة غير متوقع. هذا يمنع هجمات حقن الحزم. كما ستُستلم هذه الحزم عادة بعد إعادة إرسال حزمة المصافحة، عندما تصبح مفاتيح فك تشفير الرأس غير صالحة.

في معظم الحالات، ببساطة تجاهل الحزمة. يمكن للتنفيذ، ولكن ليس مطلوباً منه، إعادة إرسال الحزمة المرسلة سابقاً (رسالة handshake أو ACK 0) كاستجابة.

بعد إرسال Session Created كـ Bob، الحزم غير المتوقعة عادة ما تكون حزم Data التي لا يمكن فك تشفيرها لأن حزم Session Confirmed فُقدت أو وصلت خارج الترتيب. ضع الحزم في الطابور وحاول فك تشفيرها بعد استقبال حزم Session Confirmed.

بعد استقبال Session Confirmed كـ Bob، الحزم غير المتوقعة عادة ما تكون حزم Session Confirmed معاد إرسالها، لأن ACK 0 الخاص بـ Session Confirmed قد ضاع. يمكن إسقاط الحزم غير المتوقعة. قد يقوم التنفيذ، ولكن ليس مطلوباً منه، بإرسال حزمة Data تحتوي على كتلة ACK كاستجابة.

### ملاحظات

بالنسبة لـ Session Created و Session Confirmed، يجب على التطبيقات التحقق بعناية من جميع حقول الرأس المفكوكة التشفير (Connection IDs، رقم الحزمة، نوع الحزمة، الإصدار، المعرف، الجزء، والأعلام) قبل استدعاء mixHash() على الرأس ومحاولة فك تشفير الحمولة باستخدام Noise AEAD. إذا فشل فك التشفير Noise AEAD، فلا يجوز إجراء أي معالجة إضافية، لأن mixHash() ستكون قد أفسدت حالة المصافحة، إلا إذا كان التطبيق يخزن حالة الـ hash ويقوم بـ"التراجع" عنها.

### كشف الإصدار

قد لا يكون من الممكن اكتشاف ما إذا كانت الحزم الواردة من الإصدار 1 أو 2 بكفاءة على نفس المنفذ الوارد. قد تكون الخطوات المذكورة أعلاه منطقية للتنفيذ قبل معالجة SSU 1، لتجنب محاولة عمليات DH التجريبية باستخدام كلا إصداري البروتوكول.

سيتم تحديدها عند الحاجة.

## الثوابت الموصى بها

- مهلة إعادة إرسال المصافحة الصادرة: 1.25 ثانية، مع التراجع الأسي (إعادة الإرسال عند 1.25، 3.75، و 8.75 ثانية)
- إجمالي مهلة المصافحة الصادرة: 15 ثانية
- مهلة إعادة إرسال المصافحة الواردة: ثانية واحدة، مع التراجع الأسي (إعادة الإرسال عند 1، 3، و 7 ثواني)
- إجمالي مهلة المصافحة الواردة: 12 ثانية
- المهلة بعد إرسال المحاولة: 9 ثواني
- تأخير ACK: max(10, min(rtt/6, 150)) مللي ثانية
- تأخير ACK الفوري: min(rtt/16, 5) مللي ثانية
- الحد الأقصى لنطاقات ACK: 256؟
- الحد الأقصى لعمق ACK: 512؟
- توزيع الحشو: 0-15 بايت، أو أكثر
- الحد الأدنى لمهلة إعادة الإرسال في مرحلة البيانات: ثانية واحدة، كما في [RFC-6298](https://tools.ietf.org/html/rfc6298)
- راجع أيضاً [RFC-6298](https://tools.ietf.org/html/rfc6298) للحصول على إرشادات إضافية حول مؤقتات إعادة الإرسال لمرحلة البيانات.

## تحليل العبء الإضافي للحزم

يفترض IPv4، لا يتضمن الحشو الإضافي، لا يتضمن أحجام رؤوس IP و UDP. الحشو هو حشو mod-16 لـ SSU 1 فقط.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## المشاكل والعمل المستقبلي

### الرموز المميزة

نحدد أعلاه أن الرمز المميز يجب أن يكون قيمة مولدة عشوائياً من 8 بايت، وليس توليد قيمة غامضة مثل hash أو HMAC لسر الخادم وعنوان IP والمنفذ، وذلك بسبب هجمات إعادة الاستخدام. ومع ذلك، فإن هذا يتطلب تخزيناً مؤقتاً و(اختيارياً) دائماً للرموز المميزة المُسلمة. يستخدم [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) HMAC من 16 بايت لسر خادم وعنوان IP، وسر الخادم يتناوب كل دقيقتين. يجب أن نبحث في شيء مماثل، مع عمر أطول لسر الخادم. إذا قمنا بتضمين طابع زمني في الرمز المميز، فقد يكون ذلك حلاً، لكن رمز مميز من 8 بايت قد لا يكون كبيراً بما فيه الكفاية لذلك.

## المراجع

- **[Common]** [مواصفات الهياكل المشتركة](/docs/specs/common-structures)
- **[ECIES]** [مواصفات ECIES-X25519-AEAD-Ratchet](/docs/specs/ecies)
- **[NetDB]** [قاعدة بيانات الشبكة](/docs/overview/network-database)
- **[NOISE]** [إطار عمل بروتوكول Noise](https://noiseprotocol.org/noise.html)
- **[Nonces]** [الخصوم المتجاهلون للـ Nonce](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [نقل NTCP](/docs/transport/ntcp)
- **[NTCP2]** [مواصفات NTCP2](/docs/specs/ntcp2)
- **[PMTU]** [اكتشاف وحدة الإرسال القصوى للمسار](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [الاقتراح 104: نقل TLS](/proposals/104-tls-transport)
- **[Prop109]** [الاقتراح 109: النقل القابل للتوصيل](/proposals/109-pt-transport)
- **[Prop158]** [الاقتراح 158: تحسينات نقل IPv6](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [الاقتراح 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: آثار أداء TCP](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: مجموعات MODP](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: التحكم في الازدحام TCP](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: اعتبارات أمان MD5](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: مؤقت إعادة الإرسال TCP](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: تسمية تدفق IPv6](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: المنحنيات الإهليلجية للأمان](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: مجموعات تشفير ChaCha20-Poly1305 لـ TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: بروتوكول نقل QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: استخدام TLS لتأمين QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: اكتشاف الفقدان والتحكم في الازدحام QUIC](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [هيكل RouterAddress](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [هيكل RouterIdentity](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [نوع SigningPublicKey](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [نقل SSU](/docs/transport/ssu)
- **[STS]** [بروتوكول المحطة إلى المحطة](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [تذكرة I2P 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [تذكرة I2P 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [بروتوكول WireGuard](https://www.wireguard.com/papers/wireguard.pdf)

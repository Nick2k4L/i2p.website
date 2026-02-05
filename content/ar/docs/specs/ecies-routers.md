---
title: "رسائل Router باستخدام ECIES-X25519"
description: "مواصفات تشفير رسائل garlic إلى routers ECIES باستخدام X25519"
slug: "ecies-routers"
category: "البروتوكولات"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## ملاحظة

مدعوم اعتبارًا من الإصدار 0.9.49. نشر الشبكة والاختبار قيد التقدم. قابل للمراجعة الطفيفة. انظر [الاقتراح 156](/proposals/156-ecies-routers).

## نظرة عامة

هذا المستند يحدد تشفير رسائل garlic إلى routers ECIES، باستخدام العمليات التشفيرية الأساسية المقدمة من [ECIES-X25519](/docs/specs/ecies). وهو جزء من [الاقتراح 156](/proposals/156-ecies-routers) الشامل لتحويل routers من مفاتيح ElGamal إلى مفاتيح ECIES-X25519. هذه المواصفة مطبقة اعتباراً من الإصدار 0.9.49.

للحصول على نظرة عامة على جميع التغييرات المطلوبة لـ ECIES routers، انظر [اقتراح 156](/proposals/156-ecies-routers). لرسائل Garlic إلى وجهات ECIES-X25519، انظر [ECIES-X25519](/docs/specs/ecies).

### العمليات التشفيرية الأساسية

العناصر الأساسية المطلوبة لتنفيذ هذه المواصفة هي:

- AES-256-CBC كما في [التشفير](/docs/specs/cryptography)
- دوال STREAM ChaCha20/Poly1305: ENCRYPT(k, n, plaintext, ad) و DECRYPT(k, n, ciphertext, ad) - كما في [NTCP2](/docs/specs/ntcp2)، [ECIES-X25519](/docs/specs/ecies)، و [RFC-7539](https://tools.ietf.org/html/rfc7539)
- دوال X25519 DH - كما في [NTCP2](/docs/specs/ntcp2) و [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - كما في [NTCP2](/docs/specs/ntcp2) و [ECIES-X25519](/docs/specs/ecies)

دوال Noise الأخرى المعرّفة في مكان آخر:

- MixHash(d) - كما في [NTCP2](/docs/specs/ntcp2) و [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - كما في [NTCP2](/docs/specs/ntcp2) و [ECIES-X25519](/docs/specs/ecies)

## التصميم

لا يحتاج ECIES Router SKM إلى Ratchet SKM كامل كما هو محدد في [ECIES](/docs/specs/ecies) للوجهات. لا يوجد متطلب للرسائل غير المجهولة التي تستخدم نمط IK. نموذج التهديد لا يتطلب مفاتيح مؤقتة مشفرة بـ Elligator2.

لذلك، سيستخدم router SKM نمط Noise "N"، كما هو محدد في [Prop152](/proposals/152-ecies-tunnels) لبناء الأنفاق. سيستخدم نفس تنسيق البيانات المحدد في [ECIES](/docs/specs/ecies) للوجهات. لن يتم استخدام وضع المفتاح الثابت الصفري (بدون ربط أو جلسة) لـ IK المحدد في [ECIES](/docs/specs/ecies).

ستُشفّر الردود على عمليات البحث بـ ratchet tag إذا طُلب ذلك في البحث. هذا كما هو موثق في [Prop154](/proposals/154-ecies-lookups)، والمحدد الآن في [I2NP](/docs/specs/i2np).

يُمكّن التصميم الـ router من امتلاك مدير مفاتيح جلسة ECIES واحد. لا توجد حاجة لتشغيل مديري مفاتيح جلسة "مزدوجة المفاتيح" كما هو موضح في [ECIES](/docs/specs/ecies) للوجهات. تمتلك الـ routers مفتاحاً عاماً واحداً فقط.

router ECIES لا يحتوي على مفتاح ElGamal ثابت. لا يزال router بحاجة إلى تنفيذ ElGamal لبناء tunnels من خلال routers ElGamal وإرسال رسائل مشفرة إلى routers ElGamal.

قد يتطلب router ECIES مدير جلسة ElGamal جزئي لاستقبال الرسائل المُعلَّمة بـ ElGamal التي يتم استلامها كردود على عمليات البحث في NetDB من routers floodfill السابقة للإصدار 0.9.46، حيث أن هذه الـ routers لا تحتوي على تنفيذ للردود المُعلَّمة بـ ECIES كما هو محدد في [Prop152](/proposals/152-ecies-tunnels). وإلا، فقد لا يطلب router ECIES رداً مُشفراً من router floodfill سابق للإصدار 0.9.46.

هذا اختياري. قد يختلف القرار في تطبيقات I2P المختلفة وقد يعتمد على مقدار الشبكة التي تمت ترقيتها إلى 0.9.46 أو أعلى. اعتباراً من هذا التاريخ، حوالي 85% من الشبكة تستخدم الإصدار 0.9.46 أو أعلى.

### إطار عمل بروتوكول Noise

تحدد هذه المواصفة المتطلبات المبنية على [إطار عمل بروتوكول Noise](https://noiseprotocol.org/noise.html) (المراجعة 34، 2018-07-11). في مصطلحات Noise، أليس هي المبادرة، وبوب هو المستجيب.

يعتمد على بروتوكول Noise وهو Noise_N_25519_ChaChaPoly_SHA256. يستخدم بروتوكول Noise هذا العناصر الأساسية التالية:

- **نمط المصافحة أحادي الاتجاه: N** - أليس لا ترسل مفتاحها الثابت إلى بوب (N)
- **دالة DH: X25519** - X25519 DH بطول مفتاح 32 بايت كما هو محدد في [RFC-7748](https://tools.ietf.org/html/rfc7748).
- **دالة التشفير: ChaChaPoly** - AEAD_CHACHA20_POLY1305 كما هو محدد في [RFC-7539](https://tools.ietf.org/html/rfc7539) القسم 2.8. نونس بطول 12 بايت، مع تعيين أول 4 بايت إلى الصفر. مطابق لذلك الموجود في [NTCP2](/docs/specs/ntcp2).
- **دالة التجزئة: SHA256** - تجزئة قياسية بحجم 32 بايت، مستخدمة بالفعل على نطاق واسع في I2P.

### أنماط المصافحة

تستخدم المصافحات أنماط مصافحة [Noise](https://noiseprotocol.org/noise.html).

يتم استخدام تطابق الأحرف التالي:

- e = مفتاح مؤقت لاستخدام واحد
- s = مفتاح ثابت
- p = حمولة الرسالة

طلب البناء مطابق لنمط Noise N. وهذا مطابق أيضاً لأول رسالة (طلب الجلسة) في نمط XK المستخدم في [NTCP2](/docs/specs/ntcp2).

```
<- s
  ...
  e es p ->
```
### تشفير الرسائل

يتم إنشاء الرسائل وتشفيرها بشكل غير متماثل إلى router الهدف. هذا التشفير غير المتماثل للرسائل هو حالياً ElGamal كما هو محدد في [التشفير](/docs/specs/cryptography) ويحتوي على مجموع تحقق SHA-256. هذا التصميم لا يوفر السرية الأمامية.

يستخدم تصميم ECIES نمط Noise أحادي الاتجاه "N" مع ECIES-X25519 ephemeral-static DH، مع HKDF، و ChaCha20/Poly1305 AEAD للسرية الأمامية والتكامل والمصادقة. أليس هي المرسل المجهول للرسالة، router أو destination. router ECIES المستهدف هو بوب.

### تشفير الرد

الردود ليست جزءًا من هذا البروتوكول، حيث أن أليس مجهولة الهوية. مفاتيح الرد، إن وجدت، تُجمع في رسالة الطلب. راجع [مواصفات I2NP](/docs/specs/i2np) لرسائل البحث في قاعدة البيانات.

الردود على رسائل البحث في قاعدة البيانات هي رسائل Database Store أو Database Search Reply. يتم تشفيرها كرسائل Existing Session باستخدام مفتاح الرد بطول 32 بايت وعلامة الرد بطول 8 بايت كما هو محدد في [I2NP](/docs/specs/i2np) و [Prop154](/proposals/154-ecies-lookups).

لا توجد ردود صريحة على رسائل Database Store. قد يقوم المرسل بتجميع رده الخاص كرسالة Garlic Message لنفسه، تحتوي على رسالة Delivery Status.

## المواصفات

X25519: انظر [ECIES](/docs/specs/ecies).

هوية الـ Router وشهادة المفتاح: راجع [الهياكل المشتركة](/docs/specs/common-structures).

### تشفير الطلبات

تشفير الطلب هو نفسه المحدد في [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) و [Prop152](/proposals/152-ecies-tunnels)، باستخدام نمط Noise "N".

سيتم تشفير الردود على عمليات البحث باستخدام ratchet tag إذا تم طلب ذلك في البحث. تحتوي رسائل طلب Database Lookup على مفتاح الرد المكون من 32 بايت وعلامة الرد المكونة من 8 بايت كما هو محدد في [I2NP](/docs/specs/i2np) و [Prop154](/proposals/154-ecies-lookups). يتم استخدام المفتاح والعلامة لتشفير الرد.

لا يتم إنشاء مجموعات العلامات. لن يتم استخدام مخطط المفتاح الثابت الصفري المحدد في ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) و [ECIES](/docs/specs/ecies). لن يتم ترميز المفاتيح المؤقتة بـ Elligator2.

بشكل عام، ستكون هذه رسائل جلسة جديدة وسيتم إرسالها بمفتاح ثابت صفري (بدون ربط أو جلسة)، حيث أن مرسل الرسالة مجهول الهوية.

#### KDF للـ ck و h الأولية

هذا هو [Noise](https://noiseprotocol.org/noise.html) القياسي للنمط "N" مع اسم بروتوكول قياسي. هذا هو نفسه المحدد في [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) و [Prop152](/proposals/152-ecies-tunnels) لرسائل بناء الأنفاق.

```
This is the "e" message pattern:

  // Define protocol_name.
  Set protocol_name = "Noise_N_25519_ChaChaPoly_SHA256"
  (31 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  // Pad to 32 bytes. Do NOT hash it, because it is not more than 32 bytes.
  h = protocol_name || 0

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by all routers.
```
#### KDF للرسالة

ينشئ منشئو الرسائل زوج مفاتيح X25519 مؤقت لكل رسالة. يجب أن تكون المفاتيح المؤقتة فريدة لكل رسالة. هذا مماثل لما هو محدد في [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) و [Prop152](/proposals/152-ecies-tunnels) لرسائل بناء tunnel.

```
  // Target router's X25519 static keypair (hesk, hepk) from the Router Identity
  hesk = GENERATE_PRIVATE()
  hepk = DERIVE_PUBLIC(hesk)

  // MixHash(hepk)
  // || below means append
  h = SHA256(h || hepk);

  // up until here, can all be precalculated by each router
  // for all incoming messages

  // Sender generates an X25519 ephemeral keypair
  sesk = GENERATE_PRIVATE()
  sepk = DERIVE_PUBLIC(sesk)

  // MixHash(sepk)
  h = SHA256(h || sepk);

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  // Sender performs an X25519 DH with receiver's static public key.
  // The target router
  // extracts the sender's ephemeral key preceding the encrypted record.
  sharedSecret = DH(sesk, hepk) = DH(hesk, sepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  // Chain key is not used
  //chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  plaintext = 464 byte build request record
  ad = h
  ciphertext = ENCRYPT(k, n, plaintext, ad)

  End of "es" message pattern.

  // MixHash(ciphertext) is not required
  //h = SHA256(h || ciphertext)
```
#### الحمولة

الحمولة هي نفس تنسيق الكتلة المعرّف في [ECIES](/docs/specs/ecies) و [Prop144](/proposals/144-ecies-x25519-aead-ratchet). يجب أن تحتوي جميع الرسائل على كتلة DateTime لمنع إعادة التشغيل.

## ملاحظات التنفيذ

- الـ routers الأقدم لا تتحقق من نوع التشفير الخاص بالـ router وستقوم بإرسال رسائل مشفرة بـ ElGamal. بعض الـ routers الحديثة تحتوي على أخطاء وستقوم بإرسال أنواع مختلفة من الرسائل المشوهة. يجب على المطورين اكتشاف ورفض هذه السجلات قبل عملية DH إن أمكن، لتقليل استخدام المعالج.

## المراجع

- [الهياكل الشائعة](/docs/specs/common-structures)
- [التشفير](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [إطار عمل بروتوكول Noise](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [إنشاء tunnel باستخدام ECIES](/docs/specs/tunnel-creation-ecies)

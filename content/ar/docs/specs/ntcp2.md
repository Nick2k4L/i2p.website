---
title: "نقل NTCP2"
description: "نقل TCP قائم على Noise لروابط router إلى router"
slug: "ntcp2"
category: "وسائل النقل"
lastUpdated: "2026-01"
accurateFor: "0.9.66"
---

## نظرة عامة

NTCP2 هو بروتوكول اتفاق مفاتيح مصادق عليه يحسن مقاومة [NTCP](/docs/transport/ntcp) لأشكال مختلفة من التحديد الآلي والهجمات.

تم تصميم NTCP2 للمرونة والتعايش مع NTCP. قد يكون مدعوماً على نفس المنفذ الخاص بـ NTCP، أو على منفذ مختلف، أو بدون دعم متزامن لـ NTCP على الإطلاق. راجع قسم معلومات router المنشورة أدناه للتفاصيل.

كما هو الحال مع وسائل النقل الأخرى في I2P، يتم تعريف NTCP2 حصرياً لنقل رسائل I2NP من نقطة إلى نقطة (من router إلى router). إنه ليس أنبوب بيانات للأغراض العامة.

NTCP2 مدعوم اعتباراً من الإصدار 0.9.36. راجع [Prop111](/proposals/111-ntcp-2) للاقتراح الأصلي، بما في ذلك النقاش الخلفي والمعلومات الإضافية.

## إطار عمل بروتوكول Noise

يستخدم NTCP2 إطار عمل بروتوكول Noise [NOISE](https://noiseprotocol.org/noise.html) (المراجعة 33، 2017-10-04). يحتوي Noise على خصائص مشابهة لبروتوكول Station-To-Station [STS](#references)، والذي يعتبر الأساس لبروتوكول [SSU](/docs/transport/ssu). في مصطلحات Noise، أليس هي البادئ، وبوب هو المستجيب.

يستند NTCP2 إلى بروتوكول Noise وهو Noise_XK_25519_ChaChaPoly_SHA256. (المعرف الفعلي لدالة اشتقاق المفتاح الأولية هو "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256" للإشارة إلى امتدادات I2P - انظر قسم KDF 1 أدناه) يستخدم بروتوكول Noise هذا العناصر الأساسية التالية:

- نمط المصافحة: XK أليس ترسل مفتاحها إلى بوب (X) أليس تعرف المفتاح الثابت لبوب مسبقاً (K)
- وظيفة DH: X25519 X25519 DH بطول مفتاح 32 بايت كما هو محدد في [RFC-7748](https://tools.ietf.org/html/rfc7748).
- وظيفة التشفير: ChaChaPoly AEAD_CHACHA20_POLY1305 كما هو محدد في [RFC-7539](https://tools.ietf.org/html/rfc7539) القسم 2.8. nonce بطول 12 بايت، مع تعيين أول 4 بايتات إلى الصفر.
- وظيفة التجزئة: SHA256 تجزئة قياسية بطول 32 بايت، مستخدمة بالفعل على نطاق واسع في I2P.

## إضافات إلى الإطار

يحدد NTCP2 التحسينات التالية لـ Noise_XK_25519_ChaChaPoly_SHA256. تتبع هذه التحسينات بشكل عام الإرشادات في [NOISE](https://noiseprotocol.org/noise.html) القسم 13.

1) يتم تشويش المفاتيح المؤقتة ذات النص الواضح باستخدام تشفير AES بمفتاح وقيمة تهيئة معروفين. 2) يتم إضافة حشو عشوائي بنص واضح إلى الرسائل 1 و 2. يتم تضمين الحشو ذو النص الواضح في حساب hash المصافحة (MixHash). انظر أقسام KDF أدناه للرسالة 2 والجزء الأول من الرسالة 3. يتم إضافة حشو AEAD عشوائي إلى الرسالة 3 ورسائل مرحلة البيانات. 3) يتم إضافة حقل بطول إطار من بايتين، كما هو مطلوب لـ Noise عبر TCP، وكما في obfs4. يُستخدم هذا في رسائل مرحلة البيانات فقط. إطارات AEAD للرسائل 1 و 2 لها طول ثابت. إطار AEAD للجزء الأول من الرسالة 3 له طول ثابت. يتم تحديد طول إطار AEAD للجزء الثاني من الرسالة 3 في الرسالة 1. 4) يتم تشويش حقل طول الإطار من بايتين باستخدام SipHash-2-4، كما في obfs4. 5) يتم تعريف تنسيق الحمولة للرسائل 1 و 2 و 3، ومرحلة البيانات. بطبيعة الحال، هذه غير معرّفة في الإطار العام.

## الرسائل

جميع رسائل NTCP2 أقل من أو تساوي 65537 بايت في الطول. تعتمد صيغة الرسائل على رسائل Noise، مع تعديلات للتأطير وعدم القابلية للتمييز. قد تحتاج التطبيقات التي تستخدم مكتبات Noise القياسية إلى معالجة مسبقة للرسائل المستقبلة من/إلى صيغة رسائل Noise. جميع الحقول المشفرة هي نصوص مشفرة AEAD.

تسلسل الإنشاء كما يلي:

```
Alice Bob

SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
باستخدام مصطلحات Noise، تسلسل التأسيس والبيانات كما يلي: (خصائص أمان الحمولة من [Noise](https://noiseprotocol.org/noise.html))

```
XK(s, rs): Authentication Confidentiality

<- s \... -> e, es 0 2 <- e, ee 2 1 -> s, se 2 5 <- 2 5
```
بمجرد إنشاء جلسة، يمكن لأليس وبوب تبادل رسائل البيانات.

جميع أنواع الرسائل (SessionRequest، SessionCreated، SessionConfirmed، Data و TimeSync) محددة في هذا القسم.

بعض الرموز:

    - RH_A = Router Hash for Alice (32 bytes)
    - RH_B = Router Hash for Bob (32 bytes)

### التشفير المصادق عليه

هناك ثلاث حالات منفصلة للتشفير المصادق عليه (CipherStates). واحدة أثناء مرحلة المصافحة، واثنتان (الإرسال والاستقبال) لمرحلة البيانات. كل منها لديها مفتاحها الخاص من KDF.

سيتم تمثيل البيانات المشفرة/المصادق عليها كما يلي

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Encrypted and authenticated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

تنسيق البيانات المشفرة والموثقة.

المدخلات لدوال التشفير/فك التشفير:

```
k :: 32 byte cipher key, as generated from KDF



nonce :: Counter-based nonce, 12 bytes.

Starts at 0 and incremented for each message. First four bytes are always zero. Last eight bytes are the counter, little-endian encoded. Maximum value is 2**64 - 2. Connection must be dropped and restarted after it reaches that value. The value 2**64 - 1 must never be sent.

ad :: In handshake phase:

Associated data, 32 bytes. The SHA256 hash of all preceding data. In data phase: Zero bytes

data :: Plaintext data, 0 or more bytes
```
مخرجات دالة التشفير، مدخلات دالة فك التشفير:

```
+----+----+----+----+----+----+----+----+

[|Obfs Len |](##SUBST##|Obfs Len |) | +----+----+ + | ChaCha20 encrypted data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | Poly1305 Message Authentication Code | + (MAC) + | 16 bytes | +----+----+----+----+----+----+----+----+

    Obfs Len :: Length of (encrypted data + MAC) to follow, 16 - 65535

    :   Obfuscation using SipHash (see below) Not used in message 1 or 2, or message 3 part 1, where the length is fixed Not used in message 3 part 1, as the length is specified in message 1

    encrypted data :: Same size as plaintext data, 0 - 65519 bytes

    MAC :: Poly1305 message authentication code, 16 bytes
```
بالنسبة لـ ChaCha20، ما هو موصوف هنا يتوافق مع [RFC-7539](https://tools.ietf.org/html/rfc7539)، والذي يُستخدم أيضاً بشكل مشابه في TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### ملاحظات

- نظرًا لأن ChaCha20 هو stream cipher، فإن النصوص العادية لا تحتاج إلى حشو. يتم تجاهل البايتات الإضافية من keystream.
- يتم الاتفاق على مفتاح التشفير (256 بت) بواسطة SHA256 KDF. تفاصيل KDF لكل رسالة موجودة في أقسام منفصلة أدناه.
- إطارات ChaChaPoly للرسائل 1 و 2 والجزء الأول من الرسالة 3، لها حجم معروف. بدءًا من الجزء الثاني من الرسالة 3، تكون الإطارات ذات حجم متغير. يتم تحديد حجم الجزء 1 من الرسالة 3 في الرسالة 1. بدءًا من مرحلة البيانات، يتم إضافة طول مكون من بايتين في بداية الإطارات مع تشويشه باستخدام SipHash كما في obfs4.
- الحشو خارج إطار البيانات المصادق عليها للرسائل 1 و 2. يتم استخدام الحشو في KDF للرسالة التالية لذلك سيتم اكتشاف التلاعب. بدءًا من الرسالة 3، يكون الحشو داخل إطار البيانات المصادق عليها.

#### معالجة أخطاء AEAD

- في الرسائل 1 و 2 وأجزاء الرسالة 3 الجزء 1 والجزء 2، حجم رسالة AEAD معروف مسبقاً. عند فشل مصادقة AEAD، يجب على المستقبل إيقاف معالجة الرسائل الإضافية وإغلاق الاتصال دون الرد. يجب أن يكون هذا إغلاقاً غير طبيعي (TCP RST).
- لمقاومة التحقيق، في الرسالة 1، بعد فشل AEAD، يجب على Bob تعيين مهلة زمنية عشوائية (النطاق لم يحدد بعد) ثم قراءة عدد عشوائي من البايتات (النطاق لم يحدد بعد) قبل إغلاق المقبس. يجب على Bob الاحتفاظ بقائمة سوداء لعناوين IP التي تعاني من إخفاقات متكررة.
- في مرحلة البيانات، حجم رسالة AEAD "مشفر" (مبهم) باستخدام SipHash. يجب توخي الحذر لتجنب إنشاء oracle فك التشفير. عند فشل مصادقة AEAD في مرحلة البيانات، يجب على المستقبل تعيين مهلة زمنية عشوائية (النطاق لم يحدد بعد) ثم قراءة عدد عشوائي من البايتات (النطاق لم يحدد بعد). بعد القراءة، أو عند انتهاء مهلة القراءة، يجب على المستقبل إرسال حمولة مع كتلة إنهاء تحتوي على رمز سبب "فشل AEAD"، وإغلاق الاتصال.
- اتخاذ نفس إجراء الخطأ لقيمة حقل طول غير صحيحة في مرحلة البيانات.

### دالة اشتقاق المفتاح (KDF) (لرسالة المصافحة 1)

تولد KDF مفتاح تشفير مرحلة المصافحة k من نتيجة DH، باستخدام HMAC-SHA256(key, data) كما هو محدد في [RFC-2104](https://tools.ietf.org/html/rfc2104). هذه هي دوال InitializeSymmetric()، وMixHash()، وMixKey()، تماماً كما هي محددة في مواصفات Noise.

```
This is the "e" message pattern:

// Define protocol_name. Set protocol_name = "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256" (48 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck. Set ck = h

Define rs = Bob's 32-byte static key as published in the RouterInfo

// MixHash(null prologue) h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Alice must validate that Bob's static key is a valid point on the curve here.

// Bob static key // MixHash(rs) // || below means append h = SHA256(h || rs);

// up until here, can all be precalculated by Bob for all incoming connections

This is the "e" message pattern:

Alice generates her ephemeral DH key pair e.

// Alice ephemeral key X // MixHash(e.pubkey) // || below means append h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 1 // Retain the Hash h for the message 2 KDF

End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re) Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's static key Set input_key_material = X25519 DH result

// MixKey(DH())

Define temp_key = 32 bytes Define HMAC-SHA256(key, data) as in [RFC-2104](https://tools.ietf.org/html/rfc2104) // Generate a temp key from the chaining key and DH result // ck is the chaining key, defined above temp_key = HMAC-SHA256(ck, input_key_material) // overwrite the DH result in memory, no longer needed input_key_material = (all zeros)

// Output 1 // Set a new chaining key from the temp key // byte() below means a single byte ck = HMAC-SHA256(temp_key, byte(0x01)).

// Output 2 // Generate the cipher key k Define k = 32 bytes // || below means append // byte() below means a single byte k = HMAC-SHA256(temp_key, ck || byte(0x02)). // overwrite the temp_key in memory, no longer needed temp_key = (all zeros)

// retain the chaining key ck for message 2 KDF

End of "es" message pattern.
```
### 1) SessionRequest

أليس ترسل إلى بوب.

محتوى Noise: مفتاح Alice المؤقت X حمولة Noise: كتلة خيار 16 بايت حمولة غير Noise: حشو عشوائي

(خصائص أمان الحمولة من [Noise](https://noiseprotocol.org/noise.html) )

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
يتم تشفير القيمة X لضمان عدم القابلية للتمييز والتفرد للحمولة، وهما إجراءان ضروريان لمواجهة فحص الحزم العميق (DPI). نستخدم تشفير AES لتحقيق هذا، بدلاً من البدائل الأكثر تعقيداً وبطئاً مثل elligator2. التشفير غير المتماثل لمفتاح router العام الخاص بـ Bob سيكون بطيئاً جداً. يستخدم تشفير AES هاش router الخاص بـ Bob كمفتاح وقيمة IV الخاصة بـ Bob كما هي منشورة في قاعدة بيانات الشبكة.

تشفير AES مخصص لمقاومة فحص الحزم العميق فقط. أي طرف يعرف router hash الخاص ببوب، وقيمة IV، والتي يتم نشرها في قاعدة بيانات الشبكة، يمكنه فك تشفير قيمة X في هذه الرسالة.

الحشو غير مُشفر من قبل Alice. قد يكون من الضروري أن يقوم Bob بفك تشفير الحشو، لمنع هجمات التوقيت.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + obfuscated with RH_B + | AES-CBC-256 encrypted X | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | | + + | ChaChaPoly frame | + (32 bytes) + | k defined in KDF for message 1 | + n = 0 + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | ~ padding (optional) ~ | length defined in options block | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian

    :   key: RH_B iv: As published in Bobs network database entry

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Total message length must be 287 bytes or less if Bob is publishing his address as NTCP (see Version Detection section below). Alice and Bob will use the padding data in the KDF for message 2. It is authenticated so that any tampering will cause the next message to fail.
```
البيانات غير المشفرة (علامة مصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | X | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | options | + (16 bytes) + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, X25519 ephemeral key, little endian

    options :: options block, 16 bytes, see below

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Total message length must be 287 bytes or less if Bob is publishing his address as "NTCP" (see Version Detection section below) Alice and Bob will use the padding data in the KDF for message 2. It is authenticated so that any tampering will cause the next message to fail.
```
كتلة الخيارات: ملاحظة: جميع الحقول بتنسيق big-endian.

```
+----+----+----+----+----+----+----+----+

| id | ver| padLen | m3p2len | Rsvd(0) |

    +-------------------------------+-------------------------------+
    | > tsA                         | > Reserved (0)                |
    +-------------------------------+-------------------------------+

    id :: 1 byte, the network ID (currently 2, except for test networks)

    :   As of 0.9.42. See proposal 147.

    ver :: 1 byte, protocol version (currently 2)

    padLen :: 2 bytes, length of the padding, 0 or more

    :   Min/max guidelines TBD. Random size from 0 to 31 bytes minimum? (Distribution is implementation-dependent)

    m3p2Len :: 2 bytes, length of the the second AEAD frame in SessionConfirmed

    :   (message 3 part 2) See notes below

    Rsvd :: 2 bytes, set to 0 for compatibility with future options

    tsA :: 4 bytes, Unix timestamp, unsigned seconds.

    :   Wraps around in 2106

    Reserved :: 4 bytes, set to 0 for compatibility with future options
```
#### ملاحظات

- عندما يكون العنوان المنشور "NTCP"، يدعم Bob كلاً من NTCP و NTCP2 على نفس المنفذ. من أجل التوافق، عند بدء اتصال بعنوان منشور باسم "NTCP"، يجب على Alice تحديد الحد الأقصى لحجم هذه الرسالة، بما في ذلك الحشو، إلى 287 بايت أو أقل. هذا يسهل التعرف التلقائي على البروتوكول من قبل Bob. عند النشر باسم "NTCP2"، لا يوجد قيد على الحجم. راجع أقسام العناوين المنشورة واكتشاف الإصدار أدناه.

- قيمة X الفريدة في كتلة AES الأولية تضمن أن النص المشفر مختلف لكل جلسة.

- يجب على Bob رفض الاتصالات التي تكون قيمة الطابع الزمني فيها بعيدة جداً عن الوقت الحالي. نسمي أقصى دلتا زمنية "D". يجب على Bob الاحتفاظ بذاكرة تخزين مؤقت محلية لقيم المصافحة المستخدمة مسبقاً ورفض المكررات، لمنع هجمات إعادة التشغيل. يجب أن تكون للقيم في الذاكرة المؤقتة مدة حياة تبلغ على الأقل 2*D. قيم الذاكرة المؤقتة تعتمد على التنفيذ، ومع ذلك يمكن استخدام قيمة X البالغة 32 بايت (أو ما يعادلها المشفر).

- مفاتيح Diffie-Hellman المؤقتة يجب ألا يُعاد استخدامها أبداً، لمنع الهجمات التشفيرية، وإعادة الاستخدام ستُرفض كهجوم إعادة تشغيل.

- يجب أن تكون خيارات "KE" و "auth" متوافقة، أي أن السر المشترك K يجب أن يكون بالحجم المناسب. إذا تم إضافة المزيد من خيارات "auth"، فقد يؤدي ذلك ضمنياً إلى تغيير معنى علامة "KE" لاستخدام KDF مختلف أو حجم اقتطاع مختلف.

- يجب على بوب التحقق من أن مفتاح أليس المؤقت هو نقطة صالحة على المنحنى هنا.

- يجب أن تكون البطانة محدودة بكمية معقولة. قد يرفض Bob الاتصالات التي تحتوي على بطانة مفرطة. سيحدد Bob خيارات البطانة الخاصة به في الرسالة 2. الحد الأدنى/الأقصى للإرشادات سيتم تحديده لاحقاً. حجم عشوائي من 0 إلى 31 بايت كحد أدنى؟ (التوزيع يعتمد على التطبيق) تطبيقات Java تحدد حالياً البطانة بحد أقصى 256 بايت.

- في حالة حدوث أي خطأ، بما في ذلك فشل AEAD أو DH أو الطابع الزمني أو إعادة التشغيل الظاهرة أو فشل التحقق من صحة المفتاح، يجب على Bob إيقاف معالجة الرسائل الإضافية وإغلاق الاتصال دون الرد. يجب أن يكون هذا إغلاقاً غير طبيعي (TCP RST). لمقاومة التحقق، بعد فشل AEAD، يجب على Bob تعيين مهلة زمنية عشوائية (النطاق سيُحدد لاحقاً) ثم قراءة عدد عشوائي من البايتات (النطاق سيُحدد لاحقاً)، قبل إغلاق المقبس.

- قد يقوم Bob بفحص MSB سريع للتحقق من صحة المفتاح (X[31] & 0x80 == 0) قبل محاولة فك التشفير. إذا كان البت العالي مُعيّن، قم بتطبيق مقاومة الاستكشاف كما في حالات فشل AEAD.

- تخفيف هجمات حجب الخدمة: DH هي عملية مكلفة نسبياً. كما هو الحال مع بروتوكول NTCP السابق، يجب على أجهزة router اتخاذ جميع الإجراءات اللازمة لمنع استنزاف المعالج أو الاتصالات. ضع حدود على الحد الأقصى للاتصالات النشطة والحد الأقصى لإعدادات الاتصال قيد التقدم. فرض مهلات القراءة (لكل قراءة والإجمالية لـ "slowloris"). قيد الاتصالات المتكررة أو المتزامنة من نفس المصدر. احتفظ بقوائم سوداء للمصادر التي تفشل بشكل متكرر. لا تستجب لفشل AEAD.

- لتسهيل الكشف السريع عن الإصدار وإجراء المصافحة، يجب على التطبيقات التأكد من أن Alice تقوم بتخزين محتويات الرسالة الأولى كاملة في المؤقت ثم إرسالها دفعة واحدة، بما في ذلك الحشو. هذا يزيد من احتمالية أن تكون البيانات موجودة في حزمة TCP واحدة (ما لم يتم تقسيمها بواسطة نظام التشغيل أو الأجهزة الوسيطة)، ويتم استقبالها دفعة واحدة من قبل Bob. بالإضافة إلى ذلك، يجب على التطبيقات التأكد من أن Bob يقوم بتخزين محتويات الرسالة الثانية كاملة في المؤقت ثم إرسالها دفعة واحدة، بما في ذلك الحشو. وأن Bob يقوم بتخزين محتويات الرسالة الثالثة كاملة في المؤقت ثم إرسالها دفعة واحدة. هذا أيضاً من أجل الكفاءة ولضمان فعالية الحشو العشوائي.

- حقل "ver": بروتوكول Noise الشامل والإضافات وبروتوكول NTCP2 بما في ذلك مواصفات الحمولة، مما يشير إلى NTCP2. يمكن استخدام هذا الحقل للإشارة إلى الدعم للتغييرات المستقبلية.

- طول الجزء الثاني من الرسالة 3: هذا هو حجم إطار AEAD الثاني (بما في ذلك MAC بحجم 16 بايت) الذي يحتوي على Router Info الخاص بأليس والحشو الاختياري الذي سيتم إرساله في رسالة SessionConfirmed. نظراً لأن أجهزة التوجيه تعيد توليد ونشر Router Info الخاص بها بشكل دوري، فقد يتغير حجم Router Info الحالي قبل إرسال الرسالة 3. يجب على التطبيقات اختيار إحدى الاستراتيجيتين التاليتين:

a\) حفظ معلومات الـ Router الحالية ليتم إرسالها في الرسالة 3، بحيث يكون الحجم معروفاً، وإضافة مساحة للحشو اختيارياً؛

ب) زيادة الحجم المحدد بما يكفي للسماح بالزيادة المحتملة في حجم Router Info، وإضافة padding دائماً عند إرسال الرسالة 3 فعلياً. في كلتا الحالتين، يجب أن يكون طول "m3p2len" المضمن في الرسالة 1 مساوياً تماماً لحجم ذلك الإطار عند إرساله في الرسالة 3.

- يجب أن يفشل Bob الاتصال إذا بقيت أي بيانات واردة بعد التحقق من صحة الرسالة 1 وقراءة الحشو. يجب ألا تكون هناك بيانات إضافية من Alice، حيث أن Bob لم يستجب بالرسالة 2 بعد.

- يتم استخدام حقل معرف الشبكة لتحديد الاتصالات عبر الشبكات بسرعة. إذا كان هذا الحقل غير صفري، ولا يطابق معرف شبكة Bob، يجب على Bob قطع الاتصال وحظر الاتصالات المستقبلية. أي اتصالات من شبكات الاختبار يجب أن يكون لها معرف مختلف وستفشل في الاختبار. اعتبارًا من الإصدار 0.9.42. انظر المقترح 147 لمزيد من المعلومات.

### دالة اشتقاق المفتاح (KDF) (لرسالة المصافحة 2 والجزء الأول من الرسالة 3)

```
// take h saved from message 1 KDF
// MixHash(ciphertext)
h = SHA256(h || 32 byte encrypted payload from message 1)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 1)

This is the "e" message pattern:

Bob generates his ephemeral DH key pair e.

// h is from KDF for handshake message 1
// Bob ephemeral key Y
// MixHash(e.pubkey)
// || below means append
h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 2
// Retain the Hash h for the message 3 KDF

End of "e" message pattern.

This is the "ee" message pattern:

// DH(e, re)
Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's ephemeral key
Set input_key_material = X25519 DH result
// overwrite Alice's ephemeral key in memory, no longer needed
// Alice:
e(public and private) = (all zeros)
// Bob:
re = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, from the KDF for handshake message 1
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).
// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)

// retain the chaining key ck for message 3 KDF

End of "ee" message pattern.
```
### 2) SessionCreated

بوب يرسل إلى أليس.

محتوى Noise: المفتاح المؤقت لبوب Y حمولة Noise: كتلة خيار 16 بايت حمولة غير Noise: حشو عشوائي

(خصائص أمان الحمولة من [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

<- e, ee 2 1

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 1. Encryption to an ephemeral recipient. This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee"). However, the sender has not authenticated the recipient, so this payload might be sent to any party, including an active attacker.

    "e": Bob generates a new ephemeral key pair and stores it in the e variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
قيمة Y مشفرة لضمان عدم التمييز والتفرد للحمولة، والتي تعتبر إجراءات مضادة ضرورية لفحص الحزم العميق (DPI). نحن نستخدم تشفير AES لتحقيق هذا، بدلاً من البدائل الأكثر تعقيداً وبطئاً مثل elligator2. التشفير غير المتماثل لمفتاح router العام الخاص بـ Alice سيكون بطيئاً جداً. تشفير AES يستخدم router hash الخاص بـ Bob كمفتاح وحالة AES من الرسالة 1 (التي تم تهيئتها بـ IV الخاص بـ Bob كما هو منشور في قاعدة بيانات الشبكة).

تشفير AES مخصص لمقاومة فحص الحزم العميق فقط. أي طرف يعرف router hash الخاص ببوب وقيمة IV، والتي تُنشر في قاعدة بيانات الشبكة، ويلتقط أول 32 بايت من الرسالة 1، قد يتمكن من فك تشفير قيمة Y في هذه الرسالة.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + obfuscated with RH_B + | AES-CBC-256 encrypted Y | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | ChaChaPoly frame | + Encrypted and authenticated data + | 32 bytes | + k defined in KDF for message 2 + | n = 0; see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian

    :   key: RH_B iv: Using AES state from message 1
```
البيانات غير المشفرة (علامة مصادقة Poly1305 غير مُظهرة):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Y | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | options | + (16 bytes) + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, X25519 ephemeral key, little endian

    options :: options block, 16 bytes, see below

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Alice and Bob will use the padding data in the KDF for message 3 part 1. It is authenticated so that any tampering will cause the next message to fail.
```
#### ملاحظات

- يجب على Alice التحقق من أن المفتاح المؤقت لـ Bob هو نقطة صحيحة على المنحنى هنا.
- يجب تحديد الحشو بكمية معقولة. قد ترفض Alice الاتصالات ذات الحشو المفرط. ستحدد Alice خيارات الحشو الخاصة بها في الرسالة 3. إرشادات الحد الأدنى/الأقصى لم تُحدد بعد. حجم عشوائي من 0 إلى 31 بايت كحد أدنى؟ (التوزيع يعتمد على التنفيذ)
- عند أي خطأ، بما في ذلك AEAD أو DH أو الطابع الزمني أو الإعادة الظاهرة أو فشل التحقق من المفتاح، يجب على Alice إيقاف معالجة الرسائل الإضافية وإغلاق الاتصال دون الرد. يجب أن يكون هذا إغلاقاً غير طبيعي (TCP RST).
- لتسهيل المصافحة السريعة، يجب على التطبيقات التأكد من أن Bob يخزن مؤقتاً ثم يطرد محتويات الرسالة الأولى بالكامل مرة واحدة، بما في ذلك الحشو. هذا يزيد من احتمالية احتواء البيانات في حزمة TCP واحدة (ما لم يتم تقسيمها بواسطة نظام التشغيل أو الأجهزة الوسيطة)، واستقبالها جميعاً مرة واحدة من قبل Alice. هذا أيضاً للكفاءة ولضمان فعالية الحشو العشوائي.
- يجب على Alice فشل الاتصال إذا بقيت أي بيانات واردة بعد التحقق من الرسالة 2 وقراءة الحشو. لا يجب أن تكون هناك بيانات إضافية من Bob، حيث لم ترد Alice بالرسالة 3 بعد.

كتلة الخيارات: ملاحظة: جميع الحقول بتنسيق big-endian.

```
+----+----+----+----+----+----+----+----+

| Rsvd(0) | padLen | Reserved (0) |

    +-------------------------------+-------------------------------+
    | > tsB                         | > Reserved (0)                |
    +-------------------------------+-------------------------------+

    Reserved :: 10 bytes total, set to 0 for compatibility with future options

    padLen :: 2 bytes, big endian, length of the padding, 0 or more

    :   Min/max guidelines TBD. Random size from 0 to 31 bytes minimum? (Distribution is implementation-dependent)

    tsB :: 4 bytes, big endian, Unix timestamp, unsigned seconds.

    :   Wraps around in 2106
```
#### ملاحظات

- يجب على Alice رفض الاتصالات حيث تكون قيمة الطابع الزمني بعيدة جداً عن الوقت الحالي. اطلق على أقصى وقت دلتا "D". يجب على Alice الاحتفاظ بذاكرة تخزين مؤقت محلية للقيم المستخدمة مسبقاً في المصافحة ورفض المكررات، لمنع هجمات إعادة التشغيل. يجب أن تكون للقيم في الذاكرة المؤقتة مدة حياة لا تقل عن 2*D. قيم الذاكرة المؤقتة تعتمد على التنفيذ، ومع ذلك يمكن استخدام قيمة Y البالغة 32 بايت (أو ما يعادلها المشفر).

#### المشاكل

- هل يجب تضمين خيارات الحشو الأدنى/الأقصى هنا؟

### التشفير لرسالة المصافحة 3 الجزء 1، باستخدام KDF الرسالة 2)

```
// take h saved from message 2 KDF
// MixHash(ciphertext)
h = SHA256(h || 24 byte encrypted payload from message 2)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 2)
// h is used as the associated data for the AEAD in message 3 part 1, below

This is the "s" message pattern:

Define s = Alice's static public key, 32 bytes

// EncryptAndHash(s.publickey)
// EncryptWithAd(h, s.publickey)
// AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data)
// k is from handshake message 1
// n is 1
ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, s.publickey)
// MixHash(ciphertext)
// || below means append
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in message 3 part 2

End of "s" message pattern.
```
### دالة اشتقاق المفاتيح (KDF) (لرسالة المصافحة 3 الجزء 2)

```
This is the "se" message pattern:

// DH(s, re) == DH(e, rs) Define input_key_material = 32 byte DH result of Alice's static key and Bob's ephemeral key Set input_key_material = X25519 DH result // overwrite Bob's ephemeral key in memory, no longer needed // Alice: re = (all zeros) // Bob: e(public and private) = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes Define HMAC-SHA256(key, data) as in [RFC-2104](https://tools.ietf.org/html/rfc2104) // Generate a temp key from the chaining key and DH result // ck is the chaining key, from the KDF for handshake message 1 temp_key = HMAC-SHA256(ck, input_key_material) // overwrite the DH result in memory, no longer needed input_key_material = (all zeros)

// Output 1 // Set a new chaining key from the temp key // byte() below means a single byte ck = HMAC-SHA256(temp_key, byte(0x01)).

// Output 2 // Generate the cipher key k Define k = 32 bytes // || below means append // byte() below means a single byte k = HMAC-SHA256(temp_key, ck || byte(0x02)).

// h from message 3 part 1 is used as the associated data for the AEAD in message 3 part 2

// EncryptAndHash(payload) // EncryptWithAd(h, payload) // AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data) // n is 0 ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, payload) // MixHash(ciphertext) // || below means append h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF // retain the hash h for the data phase Additional Symmetric Key (SipHash) KDF

End of "se" message pattern.

// overwrite the temp_key in memory, no longer needed temp_key = (all zeros)
```
### 3) SessionConfirmed

أليس ترسل إلى بوب.

محتوى Noise: المفتاح الثابت لأليس حمولة Noise: RouterInfo الخاص بأليس والحشو العشوائي الحمولة غير Noise: لا يوجد

(خصائص أمان الحمولة من [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

-> s, se 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.

    "s": Alice writes her static public key from the s variable into the message buffer, encrypting it, and hashes the output along with the old h to derive a new h.

    "se": A DH is performed between the Alice's static key pair and the Bob's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
يحتوي هذا على إطارين من ChaChaPoly. الأول هو المفتاح العام الثابت المشفر لـ Alice. الثاني هو حمولة Noise: RouterInfo المشفر لـ Alice، والخيارات الاختيارية، والحشو الاختياري. يستخدمان مفاتيح مختلفة، لأن دالة MixKey() يتم استدعاؤها بينهما.

المحتويات الخام:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + ChaChaPoly frame (48 bytes) + | Encrypted and authenticated | + Alice static key S + | (32 bytes) | + + | k defined in KDF for message 2 | + n = 1 + | see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | | + Length specified in message 1 + | | + ChaChaPoly frame + | Encrypted and authenticated | + + | Alice RouterInfo | + using block format 2 + | Alice Options (optional) | + using block format 1 + | Arbitrary padding | + using block format 254 + | | + + | k defined in KDF for message 3 part 2 | + n = 0 + | see KDF for associated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian

    :   inside 48 byte ChaChaPoly frame
```
البيانات غير المشفرة (علامات المصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | S | + Alice static key + | (32 bytes) | + + | | + + +----+----+----+----+----+----+----+----+ | | + + | | + + | Alice RouterInfo block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Optional Options block + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Optional Padding block + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, Alice's X25519 static key, little endian
```
#### ملاحظات

- يجب على Bob أن يؤدي التحقق المعتاد من Router Info. تأكد من أن نوع التوقيع مدعوم، وتحقق من التوقيع، وتحقق من أن الطابع الزمني ضمن الحدود المقبولة، وأي فحوصات أخرى ضرورية.

- يجب على Bob التحقق من أن المفتاح الثابت لـ Alice المستلم في الإطار الأول يطابق المفتاح الثابت في Router Info. يجب على Bob أولاً البحث في Router Info عن عنوان NTCP أو NTCP2 Router Address مع خيار إصدار (v) مطابق. راجع أقسام Published Router Info و Unpublished Router Info أدناه.

- إذا كان لدى Bob إصدار أقدم من RouterInfo الخاص بـ Alice في netDb الخاص به، تحقق من أن المفتاح الثابت في معلومات الموجه متطابق في كليهما، إن وُجد، وإذا كان الإصدار الأقدم أقل من XXX قديم (انظر وقت دوران المفتاح أدناه)

- يجب على Bob التحقق من أن المفتاح الثابت لـ Alice هو نقطة صحيحة على المنحنى هنا.

- يجب تضمين الخيارات، لتحديد معايير الحشو.

- في حالة حدوث أي خطأ، بما في ذلك فشل AEAD أو RI أو DH أو الطابع الزمني أو التحقق من المفتاح، يجب على Bob إيقاف معالجة الرسائل الإضافية وإغلاق الاتصال دون الاستجابة. يجب أن يكون هذا إغلاقاً غير طبيعي (TCP RST).

- لتسهيل المصافحة السريعة، يجب على التطبيقات التأكد من أن Alice تخزن مؤقتاً ثم تدفق المحتويات الكاملة للرسالة الثالثة دفعة واحدة، بما في ذلك كلا إطاري AEAD. هذا يزيد من احتمالية احتواء البيانات في حزمة TCP واحدة (ما لم يتم تقسيمها من قبل نظام التشغيل أو middleboxes)، واستقبالها كاملة من قبل Bob. هذا أيضاً من أجل الكفاءة ولضمان فعالية الحشو العشوائي.

- طول إطار الجزء الثاني من الرسالة 3: طول هذا الإطار (بما في ذلك MAC) يتم إرساله من قبل Alice في الرسالة 1. راجع تلك الرسالة للملاحظات المهمة حول ترك مساحة كافية للحشو.

- محتوى إطار الجزء الثاني من الرسالة الثالثة: تنسيق هذا الإطار هو نفس تنسيق إطارات مرحلة البيانات، باستثناء أن طول الإطار يتم إرساله بواسطة Alice في الرسالة الأولى. انظر أدناه لتنسيق إطار مرحلة البيانات. يجب أن يحتوي الإطار على 1 إلى 3 كتل بالترتيب التالي:

1)  كتلة معلومات router الخاصة بأليس (مطلوبة)   2)  كتلة الخيارات (اختيارية)

3\) كتلة الحشو (اختيارية) يجب ألا يحتوي هذا الإطار أبداً على أي نوع كتلة أخرى.

- حشو الجزء الثاني من الرسالة 3 غير مطلوب إذا قامت أليس بإلحاق إطار مرحلة البيانات (يحتوي اختيارياً على حشو) بنهاية الرسالة 3 وأرسلت كليهما معاً، حيث سيظهر كتدفق كبير واحد من البايتات للمراقب. نظراً لأن أليس ستحتاج عموماً، وليس دائماً، إلى إرسال رسالة I2NP إلى بوب (وهذا سبب اتصالها به)، فإن هذا هو التنفيذ الموصى به، من أجل الكفاءة ولضمان فعالية الحشو العشوائي.

- الطول الإجمالي لكلا إطاري Message 3 AEAD (الجزء 1 والجزء 2) هو 65535 بايت؛ الجزء 1 هو 48 بايت لذا الحد الأقصى لطول إطار الجزء 2 هو 65487؛ الحد الأقصى لطول النص الخام في الجزء 2 باستثناء MAC هو 65471.

### دالة اشتقاق المفتاح (KDF) (لمرحلة البيانات)

تستخدم مرحلة البيانات مدخل بيانات مرتبطة بطول صفر.

تولد KDF مفتاحين للتشفير k_ab و k_ba من مفتاح التسلسل ck، باستخدام HMAC-SHA256(key, data) كما هو محدد في [RFC-2104](https://tools.ietf.org/html/rfc2104). هذه هي دالة Split()، تماماً كما هي محددة في مواصفات Noise.

```
ck = from handshake phase

// k_ab, k_ba = HKDF(ck, zerolen) // ask_master = HKDF(ck, zerolen, info="ask")

// zerolen is a zero-length byte array temp_key = HMAC-SHA256(ck, zerolen) // overwrite the chaining key in memory, no longer needed ck = (all zeros)

// Output 1 // cipher key, for Alice transmits to Bob (Noise doesn't make clear which is which, but Java code does) k_ab = HMAC-SHA256(temp_key, byte(0x01)).

// Output 2 // cipher key, for Bob transmits to Alice (Noise doesn't make clear which is which, but Java code does) k_ba = HMAC-SHA256(temp_key, k_ab || byte(0x02)).

KDF for SipHash for length field: Generate an Additional Symmetric Key (ask) for SipHash SipHash uses two 8-byte keys (big endian) and 8 byte IV for first data.

// "ask" is 3 bytes, US-ASCII, no null termination ask_master = HMAC-SHA256(temp_key, "ask" || byte(0x01)) // sip_master = HKDF(ask_master, h || "siphash") // "siphash" is 7 bytes, US-ASCII, no null termination // overwrite previous temp_key in memory // h is from KDF for message 3 part 2 temp_key = HMAC-SHA256(ask_master, h || "siphash") // overwrite ask_master in memory, no longer needed ask_master = (all zeros) sip_master = HMAC-SHA256(temp_key, byte(0x01))

Alice to Bob SipHash k1, k2, IV: // sipkeys_ab, sipkeys_ba = HKDF(sip_master, zerolen) // overwrite previous temp_key in memory temp_key = HMAC-SHA256(sip_master, zerolen) // overwrite sip_master in memory, no longer needed sip_master = (all zeros)

sipkeys_ab = HMAC-SHA256(temp_key, byte(0x01)). sipk1_ab = sipkeys_ab[0:7], little endian sipk2_ab = sipkeys_ab[8:15], little endian sipiv_ab = sipkeys_ab[16:23]

Bob to Alice SipHash k1, k2, IV:

sipkeys_ba = HMAC-SHA256(temp_key, sipkeys_ab || byte(0x02)). sipk1_ba = sipkeys_ba[0:7], little endian sipk2_ba = sipkeys_ba[8:15], little endian sipiv_ba = sipkeys_ba[16:23]

// overwrite the temp_key in memory, no longer needed temp_key = (all zeros)
```
### 4) مرحلة البيانات

حمولة Noise: كما هو محدد أدناه، بما في ذلك الحشو العشوائي حمولة غير Noise: لا يوجد

بدءاً من الجزء الثاني من الرسالة 3، تكون جميع الرسائل داخل "إطار" ChaChaPoly مُصادق عليه ومُشفر مع طول مُبهم مُسبق من بايتين. جميع الحشو يكون داخل الإطار. داخل الإطار يوجد تنسيق قياسي مع صفر أو أكثر من "الكتل". كل كتلة لها نوع من بايت واحد وطول من بايتين. الأنواع تشمل التاريخ/الوقت، ورسالة I2NP، والخيارات، والإنهاء، والحشو.

ملاحظة: قد يرسل Bob معلومات RouterInfo الخاصة به إلى Alice كأول رسالة له إلى Alice في مرحلة البيانات، لكن هذا غير مطلوب.

(خصائص أمان الحمولة من [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

<- 2 5 -> 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### ملاحظات

- للكفاءة وتقليل تحديد حقل الطول، يجب على التطبيقات ضمان أن المرسل يخزن مؤقتاً ثم يدفق المحتويات الكاملة لرسائل البيانات دفعة واحدة، بما في ذلك حقل الطول وإطار AEAD. هذا يزيد من احتمالية أن تكون البيانات محتواة في حزمة TCP واحدة (ما لم يتم تقسيمها بواسطة نظام التشغيل أو middleboxes)، ويتم استلامها دفعة واحدة من الطرف الآخر. هذا أيضاً للكفاءة ولضمان فعالية الحشو العشوائي.
- قد يختار الـ router إنهاء الجلسة عند حدوث خطأ AEAD، أو قد يستمر في محاولة التواصل. في حالة الاستمرار، يجب على الـ router الإنهاء بعد أخطاء متكررة.

#### طول SipHash المبهم

المرجع: [SipHash](https://www.131002.net/siphash/)

بمجرد أن يكمل كلا الطرفين عملية المصافحة، يقومان بنقل الحمولات التي يتم تشفيرها والتحقق من صحتها في "إطارات" ChaChaPoly.

يتم تسبيق كل إطار بطول مكون من بايتين، big endian. يحدد هذا الطول عدد بايتات الإطار المشفرة التي تتبع، بما في ذلك الـ MAC. لتجنب نقل حقول الطول القابلة للتعريف في التدفق، يتم إخفاء طول الإطار عن طريق XOR مع قناع مشتق من SipHash، كما هو مهيأ من KDF مرحلة البيانات. لاحظ أن الاتجاهين لديهما مفاتيح وقيم IV فريدة من SipHash من الـ KDF.

```
sipk1, sipk2 = The SipHash keys from the KDF.  (two 8-byte long integers)
    IV[0] = sipiv = The SipHash IV from the KDF. (8 bytes)
    length is big endian.
    For each frame:
      IV[n] = SipHash-2-4(sipk1, sipk2, IV[n-1])
      Mask[n] = First 2 bytes of IV[n]
      obfuscatedLength = length ^ Mask[n]

    The first length output will be XORed with with IV[1].
```
المستقبل لديه مفاتيح SipHash و IV المطابقة. يتم فك تشفير الطول عن طريق اشتقاق القناع المستخدم لإخفاء الطول وتطبيق عملية XOR على الملخص المقتطع للحصول على طول الإطار. طول الإطار هو الطول الإجمالي للإطار المشفر بما في ذلك MAC.

#### ملاحظات

- إذا كنت تستخدم دالة مكتبة SipHash التي ترجع عدد صحيح طويل غير موقع، استخدم البايتين الأقل أهمية كـ Mask. حول العدد الصحيح الطويل إلى IV التالي كـ little endian.

#### المحتويات الخام

```
+----+----+----+----+----+----+----+----+

[|obf size |](##SUBST##|obf size |) | +----+----+ + | | + ChaChaPoly frame + | Encrypted and authenticated | + key is k_ab for Alice to Bob + | key is k_ba for Bob to Alice | + as defined in KDF for data phase + | n starts at 0 and increments | + for each frame in that direction + | no associated data | + 16 bytes minimum + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    obf size :: 2 bytes length obfuscated with SipHash

    :   when de-obfuscated: 16 - 65535

    Minimum size including length field is 18 bytes. Maximum size including length field is 65537 bytes. Obfuscated length is 2 bytes. Maximum ChaChaPoly frame is 65535 bytes.
```
#### ملاحظات

- نظرًا لأن المستقبل يجب أن يحصل على الإطار بالكامل للتحقق من MAC، فمن المستحسن أن يقوم المرسل بتقييد الإطارات إلى بضعة كيلوبايت بدلاً من زيادة حجم الإطار إلى الحد الأقصى. هذا سيقلل من زمن التأخير لدى المستقبل.

#### البيانات غير المشفرة

يوجد صفر أو أكثر من الكتل في الإطار المشفر. تحتوي كل كتلة على معرف من بايت واحد، وطول من بايتين، وصفر أو أكثر من بايتات البيانات.

لضمان قابلية التوسع، يجب على المستقبلات تجاهل الكتل ذات المعرفات غير المعروفة، والتعامل معها كحشو.

البيانات المشفرة بحد أقصى 65535 بايت، تشمل رأس مصادقة بحجم 16 بايت، لذا الحد الأقصى للبيانات غير المشفرة هو 65519 بايت.

(علامة المصادقة Poly1305 غير معروضة):

```
+----+----+----+----+----+----+----+----+

[|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ [|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ ~ . . . ~

    blk :: 1 byte

    :   0 for datetime 1 for options 2 for RouterInfo 3 for I2NP message 4 for termination 224-253 reserved for experimental features 254 for padding 255 reserved for future extension

    size :: 2 bytes, big endian, size of data to follow, 0 - 65516 data :: the data

    Maximum ChaChaPoly frame is 65535 bytes. Poly1305 tag is 16 bytes Maximum total block size is 65519 bytes Maximum single block size is 65519 bytes Block type is 1 byte Block length is 2 bytes Maximum single block data size is 65516 bytes.
```
#### قواعد ترتيب الكتل

في رسالة المصافحة 3 الجزء 2، يجب أن يكون الترتيب: RouterInfo، يليها Options إذا كانت موجودة، يليها Padding إذا كان موجودًا. لا يُسمح بأي كتل أخرى.

في مرحلة البيانات، الترتيب غير محدد، باستثناء المتطلبات التالية: الحشو، إذا كان موجوداً، يجب أن يكون الكتلة الأخيرة. الإنهاء، إذا كان موجوداً، يجب أن يكون الكتلة الأخيرة باستثناء الحشو.

قد تكون هناك عدة كتل I2NP في إطار واحد. لا يُسمح بوجود عدة كتل Padding في إطار واحد. أنواع الكتل الأخرى على الأرجح لن تحتوي على كتل متعددة في إطار واحد، ولكن هذا غير محظور.

#### التاريخ والوقت

حالة خاصة لمزامنة الوقت:

```
+----+----+----+----+----+----+----+

| 0 | 4 | timestamp |

    +----+----+----+----+----+----+----+

    blk :: 0 size :: 2 bytes, big endian, value = 4 timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106
```
ملاحظة: يجب على التنفيذات التقريب إلى أقرب ثانية لمنع انحراف الساعة في الشبكة.

#### الخيارات

تمرير الخيارات المحدثة. تتضمن الخيارات: الحد الأدنى والأقصى للحشو.

كتلة الخيارات ستكون بطول متغير.

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
#### مشاكل الخيارات

- تنسيق الخيارات قيد التحديد.
- التفاوض على الخيارات قيد التحديد.

#### RouterInfo

مرر RouterInfo الخاص بأليس إلى بوب. يُستخدم في الجزء الثاني من رسالة المصافحة 3. مرر RouterInfo الخاص بأليس إلى بوب، أو RouterInfo الخاص ببوب إلى أليس. يُستخدم اختيارياً في مرحلة البيانات.

```
+----+----+----+----+----+----+----+----+

| 2 | size [|flg |](##SUBST##|flg |) RouterInfo |

    +----+----+----+----+ + | (Alice RI in handshake msg 3 part 2) | ~ (Alice, Bob, or third-party ~ | RI in data phase) | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 2 size :: 2 bytes, big endian, size of flag + router info to follow flg :: 1 byte flags bit order: 76543210 bit 0: 0 for local store, 1 for flood request bits 7-1: Unused, set to 0 for future compatibility routerinfo :: Alice's or Bob's RouterInfo
```
#### ملاحظات

- عند الاستخدام في مرحلة البيانات، يجب على المستقبِل (Alice أو Bob) التحقق من أنه نفس Router Hash المُرسل أصلاً (لـ Alice) أو المُرسل إليه (لـ Bob). ثم، تعامل معه كرسالة I2NP DatabaseStore محلية. تحقق من التوقيع، تحقق من الطابع الزمني الأحدث، واحفظه في netDb المحلي. إذا كان bit العلامة 0 هو 1، والطرف المستقبِل هو floodfill، تعامل معه كرسالة DatabaseStore برمز رد غير صفري، وانشره إلى أقرب floodfills.
- Router Info غير مضغوط بـ gzip (على عكس رسالة DatabaseStore، حيث يكون مضغوطاً)
- يجب عدم طلب النشر إلا إذا كانت هناك RouterAddresses منشورة في RouterInfo. يجب على router المستقبِل عدم نشر RouterInfo إلا إذا كانت هناك RouterAddresses منشورة فيه.
- يجب على المطورين ضمان أنه عند قراءة كتلة، البيانات المشوهة أو الضارة لن تتسبب في تجاوز القراءات إلى الكتلة التالية.
- هذا البروتوكول لا يوفر إقراراً بأن RouterInfo تم استلامه أو تخزينه أو نشره (سواء في مرحلة المصافحة أو مرحلة البيانات). إذا كان الإقرار مرغوباً، والمستقبِل هو floodfill، يجب على المُرسِل بدلاً من ذلك إرسال رسالة I2NP DatabaseStoreMessage قياسية برمز رد.

#### المشاكل

- يمكن أيضاً استخدامها في مرحلة البيانات، بدلاً من I2NP DatabaseStoreMessage. على سبيل المثال، يمكن لبوب استخدامها لبدء مرحلة البيانات.
- هل يُسمح لها بأن تحتوي على RI لـ routers غير المنشئ، كبديل عام لـ DatabaseStoreMessages، مثلاً للإغراق بواسطة floodfills؟

#### رسالة I2NP

رسالة I2NP واحدة مع رأس معدل. رسائل I2NP لا يجوز تجزئتها عبر الكتل أو عبر إطارات ChaChaPoly.

هذا يستخدم أول 9 بايتات من رأس NTCP I2NP المعياري، ويزيل آخر 7 بايتات من الرأس، كما يلي: تقصير انتهاء الصلاحية من 8 إلى 4 بايتات (ثوانٍ بدلاً من ميللي ثانية، نفس الشيء بالنسبة لـ SSU)، إزالة الطول المكون من 2 بايت (استخدم حجم الكتلة - 9)، وإزالة checksum SHA256 المكون من بايت واحد.

```
+----+----+----+----+----+----+----+----+

| 3 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 3 size :: 2 bytes, big endian, size of type + msg id + exp + message to follow I2NP message body size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: I2NP message body
```
#### ملاحظات

- يجب على المطورين التأكد من أنه عند قراءة كتلة، البيانات المشوهة أو الضارة لن تتسبب في تجاوز القراءة إلى الكتلة التالية.

#### الإنهاء

ينصح Noise برسالة إنهاء صريحة. NTCP الأصلي لا يحتوي على واحدة. قطع الاتصال. يجب أن يكون هذا آخر كتلة غير حشو في الإطار.

```
+----+----+----+----+----+----+----+----+

| 4 | size | valid data frames |

    +----+----+----+----+----+----+----+----+

    :   received | rsn| addl data |

    +----+----+----+----+ + ~ . . . ~ +----+----+----+----+----+----+----+----+

    blk :: 4 size :: 2 bytes, big endian, value = 9 or more valid data frames received :: The number of valid AEAD data phase frames received (current receive nonce value) 0 if error occurs in handshake phase 8 bytes, big endian rsn :: reason, 1 byte: 0: normal close or unspecified 1: termination received 2: idle timeout 3: router shutdown 4: data phase AEAD failure 5: incompatible options 6: incompatible signature type 7: clock skew 8: padding violation 9: AEAD framing error 10: payload format error 11: message 1 error 12: message 2 error 13: message 3 error 14: intra-frame read timeout 15: RI signature verification fail 16: s parameter missing, invalid, or mismatched in RouterInfo 17: banned addl data :: optional, 0 or more bytes, for future expansion, debugging, or reason text. Format unspecified and may vary based on reason code.
```
#### ملاحظات

قد لا تُستخدم جميع الأسباب فعلياً، وهذا يعتمد على التنفيذ. فشل المصافحة سيؤدي عموماً إلى إغلاق مع TCP RST بدلاً من ذلك. انظر الملاحظات في أقسام رسالة المصافحة أعلاه. الأسباب الإضافية المذكورة هي لأغراض الاتساق والتسجيل وتصحيح الأخطاء، أو في حالة تغيير السياسات.

#### الحشو

هذا للحشو داخل إطارات AEAD. الحشو للرسائل 1 و 2 يكون خارج إطارات AEAD. جميع الحشو للرسالة 3 ومرحلة البيانات يكون داخل إطارات AEAD.

يجب أن تلتزم المساحة المضافة داخل AEAD تقريباً بالمعاملات المتفاوض عليها. أرسل Bob معاملات tx/rx الدنيا/العليا المطلوبة في الرسالة 2. أرسلت Alice معاملات tx/rx الدنيا/العليا المطلوبة في الرسالة 3. يمكن إرسال خيارات محدثة أثناء مرحلة البيانات. راجع معلومات كتلة الخيارات أعلاه.

إذا كان موجوداً، يجب أن يكون هذا آخر block في الإطار.

```
+----+----+----+----+----+----+----+----+

[|254 |](##SUBST##|254 |) size | padding | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 254 size :: 2 bytes, big endian, size of padding to follow padding :: random data
```
#### ملاحظات

- الحجم = 0 مسموح.
- استراتيجيات الحشو لم تحدد بعد.
- الحد الأدنى للحشو لم يحدد بعد.
- الإطارات التي تحتوي على حشو فقط مسموحة.
- قيم الحشو الافتراضية لم تحدد بعد.
- انظر كتلة الخيارات للتفاوض على معايير الحشو
- انظر كتلة الخيارات لمعايير الحد الأدنى والأقصى للحشو
- Noise يحد الرسائل إلى 64KB. إذا كان هناك حاجة لمزيد من الحشو، أرسل إطارات متعددة.
- استجابة router عند انتهاك الحشو المتفاوض عليه تعتمد على التنفيذ.

#### أنواع الكتل الأخرى

يجب على التطبيقات تجاهل أنواع الكتل غير المعروفة من أجل التوافق المستقبلي، باستثناء الرسالة 3 الجزء 2، حيث الكتل غير المعروفة غير مسموحة.

#### العمل المستقبلي

- يجب تحديد طول الحشو إما على أساس كل رسالة على حدة وتقديرات توزيع الطول، أو يجب إضافة تأخيرات عشوائية. هذه الإجراءات المضادة يجب تضمينها لمقاومة DPI، حيث أن أحجام الرسائل ستكشف خلاف ذلك أن حركة مرور I2P يتم نقلها عبر بروتوكول النقل. مخطط الحشو الدقيق هو مجال للعمل المستقبلي.

### 5) الإنهاء

يمكن إنهاء الاتصالات عبر إغلاق مقبس TCP العادي أو غير العادي، أو، كما ينصح Noise، عبر رسالة إنهاء صريحة. رسالة الإنهاء الصريحة محددة في مرحلة البيانات أعلاه.

عند أي إنهاء طبيعي أو غير طبيعي، يجب على أجهزة router أن تقوم بمحو أي بيانات مؤقتة في الذاكرة، بما في ذلك مفاتيح المصافحة المؤقتة ومفاتيح التشفير المتماثل والمعلومات ذات الصلة.

## معلومات Router المنشورة

### القدرات

اعتباراً من الإصدار 0.9.50، يتم دعم خيار "caps" في عناوين NTCP2، مشابهاً لـ SSU. يمكن نشر قدرة واحدة أو أكثر في خيار "caps". يمكن أن تكون القدرات بأي ترتيب، لكن "46" هو الترتيب الموصى به، للاتساق عبر التطبيقات المختلفة. هناك قدرتان محددتان:

4: يشير إلى قدرة IPv4 الصادرة. إذا تم نشر عنوان IP في حقل المضيف، فإن هذه القدرة ليست ضرورية. إذا كان الـ router مخفيًا، أو كان NTCP2 صادرًا فقط، فيمكن دمج '4' و '6' في عنوان واحد.

6: يشير إلى قدرة IPv6 الصادرة. إذا تم نشر عنوان IP في حقل المضيف، فإن هذه القدرة غير ضرورية. إذا كان router مخفياً، أو كان NTCP2 صادراً فقط، فيمكن دمج '4' و '6' في عنوان واحد.

### العناوين المنشورة

عنوان الموجه المنشور RouterAddress (جزء من معلومات الموجه RouterInfo) سيكون له معرف بروتوكول إما "NTCP" أو "NTCP2".

يجب أن يحتوي RouterAddress على خيارات "host" و "port"، كما هو الحال في بروتوكول NTCP الحالي.

يجب أن يحتوي RouterAddress على ثلاث خيارات للإشارة إلى دعم NTCP2:

- s=(Base64 key) المفتاح العام الثابت (s) الحالي لـ Noise لهذا RouterAddress. مُرمز بـ Base 64 باستخدام الأبجدية القياسية لـ I2P Base 64. 32 بايت في النظام الثنائي، 44 بايت كـ Base 64 مُرمز، مفتاح عام X25519 little-endian.
- i=(Base64 IV) الـ IV الحالي لتشفير قيمة X في الرسالة 1 لهذا RouterAddress. مُرمز بـ Base 64 باستخدام الأبجدية القياسية لـ I2P Base 64. 16 بايت في النظام الثنائي، 24 بايت كـ Base 64 مُرمز، big-endian.
- v=2 الإصدار الحالي (2). عند النشر كـ "NTCP"، يُفترض دعم إضافي للإصدار 1. دعم الإصدارات المستقبلية سيكون بقيم مفصولة بفواصل، مثل v=2,3 يجب على التنفيذ التحقق من التوافق، بما في ذلك إصدارات متعددة إذا كانت هناك فاصلة. الإصدارات المفصولة بفواصل يجب أن تكون مرتبة رقمياً.

يجب على Alice التحقق من وجود وصحة جميع الخيارات الثلاثة قبل الاتصال باستخدام بروتوكول NTCP2.

عند النشر باسم "NTCP" مع خيارات "s" و "i" و "v"، يجب على الـ router قبول الاتصالات الواردة على ذلك المضيف والمنفذ لكل من بروتوكولي NTCP و NTCP2، واكتشاف إصدار البروتوكول تلقائياً.

عندما يتم نشره كـ "NTCP2" مع خيارات "s" و "i" و "v"، يقبل الـ router الاتصالات الواردة على ذلك المضيف والمنفذ لبروتوكول NTCP2 فقط.

إذا كان router يدعم كلاً من اتصالات NTCP1 و NTCP2 ولكنه لا ينفذ الكشف التلقائي للإصدار للاتصالات الواردة، فيجب عليه الإعلان عن كل من عناوين "NTCP" و "NTCP2"، وتضمين خيارات NTCP2 في عنوان "NTCP2" فقط. يجب على الـ router تعيين قيمة تكلفة أقل (أولوية أعلى) في عنوان "NTCP2" مقارنة بعنوان "NTCP"، بحيث يفضل NTCP2.

إذا تم نشر عدة NTCP2 RouterAddresses (سواء كـ "NTCP" أو "NTCP2") في نفس RouterInfo (لعناوين IP إضافية أو منافذ)، فيجب أن تحتوي جميع العناوين التي تحدد نفس المنفذ على نفس خيارات وقيم NTCP2. وبشكل خاص، يجب أن تحتوي جميعها على نفس المفتاح الثابت و iv.

### عنوان NTCP2 غير منشور

إذا لم تقم Alice بنشر عنوان NTCP2 الخاص بها (كـ "NTCP" أو "NTCP2") للاتصالات الواردة، يجب عليها نشر عنوان router "NTCP2" يحتوي فقط على مفتاحها الثابت وإصدار NTCP2، بحيث يمكن لـ Bob التحقق من صحة المفتاح بعد تلقي RouterInfo الخاص بـ Alice في الرسالة 3 الجزء 2.

- s=(Base64 key) كما هو معرّف أعلاه للعناوين المنشورة.
- v=2 كما هو معرّف أعلاه للعناوين المنشورة.

عنوان router هذا لن يحتوي على خيارات "i" أو "host" أو "port"، حيث أن هذه غير مطلوبة لاتصالات NTCP2 الصادرة. التكلفة المنشورة لهذا العنوان لا تهم بدقة، حيث أنه للاتصالات الواردة فقط؛ ومع ذلك، قد يكون من المفيد لـ routers الأخرى إذا تم تعيين التكلفة أعلى (أولوية أقل) من العناوين الأخرى. القيمة المقترحة هي 14.

يمكن لأليس أيضًا ببساطة إضافة خيارات "s" و "v" إلى عنوان "NTCP" منشور موجود.

### تدوير المفتاح العام ومتجه التهيئة

نظراً لتخزين RouterInfos مؤقتاً، يجب على أجهزة router عدم تدوير المفتاح العام الثابت أو IV أثناء تشغيل الـ router، سواء في عنوان منشور أم لا. يجب على أجهزة router تخزين هذا المفتاح وIV بشكل دائم لإعادة الاستخدام بعد إعادة التشغيل الفورية، بحيث تستمر الاتصالات الواردة في العمل، ولا يتم كشف أوقات إعادة التشغيل. يجب على أجهزة router تخزين، أو تحديد بطريقة أخرى، وقت آخر إيقاف تشغيل، بحيث يمكن حساب فترة التوقف السابقة عند بدء التشغيل.

مع مراعاة المخاوف حول كشف أوقات إعادة التشغيل، قد تقوم أجهزة router بتدوير هذا المفتاح أو IV عند بدء التشغيل إذا كان router متوقفاً سابقاً لبعض الوقت (ساعتين على الأقل).

إذا كان لدى الـ router أي NTCP2 RouterAddresses منشورة (كـ NTCP أو NTCP2)، فإن الحد الأدنى لوقت التوقف قبل التدوير يجب أن يكون أطول بكثير، على سبيل المثال شهر واحد، ما لم يتغير عنوان IP المحلي أو يقوم الـ router بـ "rekeys".

إذا كان router يحتوي على أي عناوين SSU RouterAddresses منشورة، ولكن ليس NTCP2 (كـ NTCP أو NTCP2)، فيجب أن يكون الحد الأدنى لوقت التوقف قبل التدوير أطول، على سبيل المثال يوم واحد، ما لم يتغير عنوان IP المحلي أو يقوم router بـ "rekeys". هذا ينطبق حتى لو كان عنوان SSU المنشور يحتوي على مقدمين.

إذا لم يكن لدى router أي RouterAddresses منشورة (NTCP أو NTCP2 أو SSU)، فقد يكون الحد الأدنى لوقت التوقف قبل التدوير قصيرًا يصل إلى ساعتين، حتى لو تغير عنوان IP، ما لم يقم router بـ "إعادة تكوين المفاتيح".

إذا قام الـ router بإعادة تشفير المفاتيح "rekeys" إلى Router Hash مختلف، يجب أن ينشئ مفتاح noise وIV جديدين أيضاً.

يجب أن تكون التطبيقات على علم بأن تغيير المفتاح العام الثابت أو IV سيمنع اتصالات NTCP2 الواردة من routers التي قامت بحفظ RouterInfo أقدم في التخزين المؤقت. يجب أن تأخذ عملية نشر RouterInfo، واختيار أقران tunnel (بما في ذلك كل من OBGW وأقرب hop للـ IB)، واختيار tunnel بدون hops، واختيار النقل، واستراتيجيات التطبيق الأخرى هذا الأمر في الاعتبار.

تناوب IV يخضع لنفس القواعد المطبقة على تناوب المفاتيح، باستثناء أن IVs غير موجودة إلا في RouterAddresses المنشورة، لذا لا يوجد IV لأجهزة router المخفية أو المحمية بجدار حماية. إذا تغير أي شيء (الإصدار، المفتاح، الخيارات؟) فمن المستحسن أن يتغير IV أيضاً.

ملاحظة: قد يتم تعديل الحد الأدنى لوقت التوقف قبل إعادة إنتاج المفاتيح لضمان صحة الشبكة، ولمنع إعادة البذر بواسطة router متوقف لفترة زمنية متوسطة.

## اكتشاف الإصدار

عندما يُنشر كـ "NTCP"، يجب على الـ router أن يكتشف تلقائياً إصدار البروتوكول للاتصالات الواردة.

هذا الكشف يعتمد على التنفيذ، ولكن إليك بعض الإرشادات العامة.

لاكتشاف إصدار اتصال NTCP الواردة، يتابع Bob كما يلي:

- انتظر على الأقل 64 بايت (الحد الأدنى لحجم رسالة NTCP2 الأولى)

- إذا كانت البيانات المستلمة الأولية 288 بايت أو أكثر، فإن الاتصال الوارد هو الإصدار 1.

- إذا كان أقل من 288 بايت، إما

> - انتظر لفترة قصيرة للحصول على المزيد من البيانات (استراتيجية جيدة قبل الاعتماد الواسع النطاق لـ NTCP2) إذا تم استلام 288 إجمالي على الأقل، فهو NTCP 1.   >   > - جرب المراحل الأولى من فك التشفير كإصدار 2، إذا فشل، انتظر لفترة قصيرة للحصول على المزيد من البيانات (استراتيجية جيدة بعد الاعتماد الواسع النطاق لـ NTCP2)   >   >   > - فك تشفير أول 32 بايت (مفتاح X) من حزمة SessionRequest باستخدام AES-256 مع المفتاح RH_B.   >   > - التحقق من نقطة صالحة على المنحنى. إذا فشل، انتظر لفترة قصيرة للحصول على المزيد من البيانات لـ NTCP 1   >   > - التحقق من إطار AEAD. إذا فشل، انتظر لفترة قصيرة للحصول على المزيد من البيانات لـ NTCP 1

لاحظ أنه قد يُوصى بتغييرات أو استراتيجيات إضافية إذا اكتشفنا هجمات تقسيم TCP نشطة على NTCP 1.

لتسهيل اكتشاف الإصدار السريع والمصافحة، يجب على التطبيقات التأكد من أن Alice تقوم بتخزين محتويات الرسالة الأولى كاملة في المخزن المؤقت ثم إرسالها دفعة واحدة، بما في ذلك الحشو. هذا يزيد من احتمالية أن تكون البيانات محتواة في حزمة TCP واحدة (ما لم يتم تقسيمها بواسطة نظام التشغيل أو الصناديق الوسيطة)، وأن يستقبلها Bob دفعة واحدة. هذا أيضاً من أجل الكفاءة وضمان فعالية الحشو العشوائي. ينطبق هذا على مصافحات NTCP وNTCP2 على حد سواء.

## المتغيرات والبدائل والمسائل العامة

- إذا كانت أليس وبوب كلاهما يدعم NTCP2، فيجب على أليس الاتصال باستخدام NTCP2.
- إذا فشلت أليس في الاتصال ببوب باستخدام NTCP2 لأي سبب، فإن الاتصال يفشل. لا يجوز لأليس إعادة المحاولة باستخدام NTCP 1.

## إرشادات انحراف الساعة

يتم تضمين طوابع زمنية للأقران في أول رسالتين من المصافحة، طلب الجلسة وإنشاء الجلسة. الانحراف الزمني بين قرينين أكبر من +/- 60 ثانية يكون قاتلاً بشكل عام. إذا اعتقد Bob أن ساعته المحلية سيئة، فيمكنه ضبط ساعته باستخدام الانحراف المحسوب، أو مصدر خارجي. وإلا، يجب على Bob الرد برسالة إنشاء جلسة حتى لو تم تجاوز الحد الأقصى للانحراف، بدلاً من مجرد إغلاق الاتصال. هذا يسمح لـ Alice بالحصول على طابع Bob الزمني وحساب الانحراف، واتخاذ إجراء إذا لزم الأمر. Bob لا يملك هوية router الخاصة بـ Alice في هذه النقطة، ولكن للحفاظ على الموارد، قد يكون من المرغوب فيه أن يحظر Bob الاتصالات الواردة من عنوان IP الخاص بـ Alice لفترة من الزمن، أو بعد محاولات اتصال متكررة مع انحراف مفرط.

يجب على Alice تعديل انحراف الساعة المحسوب بطرح نصف RTT. إذا كانت Alice تعتقد أن ساعتها المحلية سيئة، فقد تقوم بتعديل ساعتها باستخدام الانحراف المحسوب، أو مصدر خارجي. إذا كانت Alice تعتقد أن ساعة Bob سيئة، فقد تحظر Bob لفترة من الزمن. في كلتا الحالتين، يجب على Alice إغلاق الاتصال.

إذا ردت Alice بـ Session Confirmed (ربما لأن الانحراف قريب جداً من حد الـ 60 ثانية، وحسابات Alice و Bob ليست متطابقة تماماً بسبب RTT)، يجب على Bob تعديل الانحراف المحسوب للساعة عن طريق طرح نصف RTT. إذا تجاوز الانحراف المعدل للساعة الحد الأقصى، يجب على Bob حينها الرد برسالة Disconnect تحتوي على رمز سبب انحراف الساعة، وإغلاق الاتصال. في هذه النقطة، يمتلك Bob هوية router الخاصة بـ Alice، وقد يحظر Alice لفترة زمنية معينة.

## المراجع

- [الهياكل الشائعة](/docs/specs/common-structures)
- [I2NP](/docs/specs/i2np)
- [قاعدة بيانات الشبكة](/docs/overview/network-database)
- [NOISE - إطار عمل بروتوكول Noise](https://noiseprotocol.org/noise.html)
- [NTCP](/docs/transport/ntcp)
- [Prop104](/proposals/104-tls-transport)
- [Prop109](/proposals/109-pt-transport)
- [Prop111](/proposals/111-ntcp-2)
- [RFC-2104 - HMAC](https://tools.ietf.org/html/rfc2104)
- [RFC-3526 - مجموعات DH](https://tools.ietf.org/html/rfc3526)
- [RFC-6151](https://tools.ietf.org/html/rfc6151)
- [RFC-7539 - ChaCha20-Poly1305](https://tools.ietf.org/html/rfc7539)
- [RFC-7748 - X25519](https://tools.ietf.org/html/rfc7748)
- [RFC-7905](https://tools.ietf.org/html/rfc7905)
- [SipHash](https://www.131002.net/siphash/)
- [SSU](/docs/transport/ssu)
- **[STS]** Diffie, W.; van Oorschot P. C.; Wiener M. J., المصادقة وتبادل المفاتيح المصادق عليها

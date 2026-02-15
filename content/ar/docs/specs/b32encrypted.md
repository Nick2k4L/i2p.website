---
title: "B32 لـ Encrypted Leasesets"
description: "تنسيق عنوان Base 32 لـ leasesets من نوع LS2 المشفرة"
slug: "b32encrypted"
aliases:
  - "/ar/docs/specs/b32-for-encrypted-leasesets"
  - "/ar/docs/specs/b32-for-encrypted-leasesets/"
category: "التصميم"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## نظرة عامة

تحتوي عناوين Base 32 القياسية ("b32") على hash الخاص بالوجهة. هذا لن يعمل مع ls2 المشفر (اقتراح 123).

لا يمكننا استخدام عنوان base 32 تقليدي لـ LS2 مشفر (اقتراح 123)، حيث أنه يحتوي فقط على hash الوجهة. لا يوفر المفتاح العام غير المخفي. يجب على العملاء معرفة المفتاح العام للوجهة، ونوع التوقيع، ونوع التوقيع المخفي، ومفتاح سري أو خاص اختياري لجلب وفك تشفير leaseSet. لذلك، عنوان base 32 وحده غير كافٍ. يحتاج العميل إما إلى الوجهة الكاملة (التي تحتوي على المفتاح العام)، أو المفتاح العام بحد ذاته. إذا كان لدى العميل الوجهة الكاملة في دفتر العناوين، ودفتر العناوين يدعم البحث العكسي بواسطة hash، فيمكن استرجاع المفتاح العام.

يضع هذا التنسيق المفتاح العام بدلاً من التشفير في عنوان base32. يجب أن يحتوي هذا التنسيق أيضاً على نوع التوقيع للمفتاح العام، ونوع التوقيع لنظام الإخفاء.

تحدد هذه الوثيقة تنسيق b32 لهذه العناوين. بينما أشرنا إلى هذا التنسيق الجديد أثناء المناقشات كعنوان "b33"، إلا أن التنسيق الجديد الفعلي يحتفظ باللاحقة المعتادة ".b32.i2p".

## التصميم

- التنسيق الجديد سيحتوي على المفتاح العام غير المعمى، ونوع التوقيع غير المعمى، ونوع التوقيع المعمى.
- اختيارياً يحتوي على مفتاح سري و/أو مفتاح خاص، للروابط الخاصة فقط
- استخدام لاحقة ".b32.i2p" الموجودة، ولكن بطول أكبر.
- إضافة مجموع تحقق.
- عناوين leaseSet المشفرة تُعرف بـ 56 حرفاً مُرمزاً أو أكثر (35 بايت مفكوك أو أكثر)، مقارنة بـ 52 حرفاً (32 بايت) للعناوين التقليدية base 32.

## المواصفات

### الإنشاء والترميز

قم ببناء اسم مضيف من {56+ حرف}.b32.i2p (35+ حرف في النظام الثنائي) كما يلي:

```
flag (1 byte)
    bit 0: 0 for one-byte sigtypes, 1 for two-byte sigtypes
    bit 1: 0 for no secret, 1 if secret is required
    bit 2: 0 for no per-client auth, 1 if client private key is required
    bits 7-3: Unused, set to 0

public key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

blinded key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

public key
    Number of bytes as implied by sigtype
```
المعالجة اللاحقة والمجموع الاختباري:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
يجب أن تكون أي بتات غير مستخدمة في نهاية b32 تساوي 0. لا توجد بتات غير مستخدمة لعنوان قياسي مكون من 56 حرفاً (35 بايت).

### فك التشفير والتحقق

```
strip the ".b32.i2p" from the hostname
data = Base32.decode(hostname)
Calculate checksum = CRC-32(data[3:end])
Treat checksum as little-endian.
flags = data[0] ^ (byte) checksum
if 1 byte sigtypes:
    pubkey sigtype = data[1] ^ (byte) (checksum >> 8)
    blinded sigtype = data[2] ^ (byte) (checksum >> 16)
else (2 byte sigtypes):
    pubkey sigtype = data[1] ^ ((byte) (checksum >> 8)) || data[2] ^ ((byte) (checksum >> 16))
    blinded sigtype = data[3] || data[4]
parse the remainder based on the flags to get the public key
```
### بتات المفتاح السري والخاص

تُستخدم بتات المفتاح السري والخاص للإشارة إلى العملاء أو الوكلاء أو أي كود آخر من جانب العميل أن المفتاح السري و/أو الخاص سيكون مطلوباً لفك تشفير الـ leaseset. قد تطلب تطبيقات معينة من المستخدم توفير البيانات المطلوبة، أو ترفض محاولات الاتصال في حالة عدم وجود البيانات المطلوبة.

## التخزين المؤقت

بينما يقع هذا خارج نطاق هذه المواصفة، يجب على أجهزة router و/أو العملاء تذكر وتخزين مؤقتاً (على الأرجح بشكل دائم) ربط المفتاح العام بالوجهة، والعكس صحيح.

## ملاحظات

- التمييز بين النكهات القديمة والجديدة بالطول. عناوين b32 القديمة هي
  دائماً {52 حرفاً}.b32.i2p. الجديدة هي {56+ حرفاً}.b32.i2p
- موضوع نقاش Tor:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- لا تتوقع حدوث sigtypes من بايتين أبداً، نحن فقط وصلنا إلى 13. لا
  حاجة للتنفيذ الآن.
- يمكن استخدام التنسيق الجديد في روابط القفز (وتقديمها بواسطة خوادم القفز) إذا
  كان مرغوباً فيه، تماماً مثل b32.

## المراجع

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - انظر أيضاً [RFC 3309](https://tools.ietf.org/html/rfc3309)

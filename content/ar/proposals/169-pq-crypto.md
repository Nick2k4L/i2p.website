---
title: "بروتوكولات التشفير ما بعد الكمي"
aliases: 
number: "169"
author: "zzz, orignal, drzed, eyedeekay"
created: "2025-01-21"
lastupdated: "2026-02-26"
status: "فتح"
thread: "http://zzz.i2p/topics/3294"
target: "0.9.80"
toc: true
---

### الحالة

| البروتوكول / الميزة | الحالة |
|--------------------|--------|
| Ratchet | مكتمل في Java I2P و i2pd |
| NTCP2 | نسخة تجريبية الربع الأول 2026 |
| SSU2 | التنفيذ يبدأ قريباً، نسخة تجريبية الربع الثالث 2026 |
| MLDSA SigTypes | أولوية منخفضة، على الأرجح 2027+ |
## نظرة عامة

بينما استمرت البحوث والمنافسة للحصول على تشفير مناسب لما بعد الكم (PQ) لعقد من الزمن، لم تصبح الخيارات واضحة حتى وقت قريب.

بدأنا في النظر في آثار التشفير المقاوم للحوسبة الكمية (PQ crypto) في عام 2022 [zzz.i2p](http://zzz.i2p/topics/3294).

أضافت معايير TLS دعم التشفير المختلط في العامين الماضيين وهو يُستخدم الآن لجزء كبير من حركة البيانات المشفرة على الإنترنت بسبب الدعم في Chrome وFirefox [Cloudflare](https://blog.cloudflare.com/pq-2024/).

قام NIST مؤخراً بوضع اللمسات الأخيرة ونشر الخوارزميات الموصى بها لعلم التشفير ما بعد الكمي [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). تدعم عدة مكتبات تشفير شائعة الآن معايير NIST أو ستصدر دعماً لها في المستقبل القريب.

كل من [Cloudflare](https://blog.cloudflare.com/pq-2024/) و [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) يوصيان ببدء الانتقال فوراً. راجع أيضاً الأسئلة الشائعة حول PQ من NSA لعام 2022 [NSA](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF). يجب أن يكون I2P رائداً في الأمان والتشفير. الآن هو الوقت المناسب لتطبيق الخوارزميات الموصى بها. باستخدام نظام نوع التشفير ونوع التوقيع المرن لدينا، سنضيف أنواعاً للتشفير المختلط، وللتوقيعات PQ والمختلطة.

## الأهداف

- اختيار خوارزميات مقاومة للحوسبة الكمية
- إضافة خوارزميات كمية فقط وهجينة إلى بروتوكولات I2P حسب الحاجة
- تعريف متغيرات متعددة
- اختيار أفضل المتغيرات بعد التنفيذ والاختبار والتحليل والبحث
- إضافة الدعم تدريجياً ومع التوافق العكسي

## الأهداف المستبعدة

- لا تغير بروتوكولات التشفير أحادية الاتجاه (Noise N)
- لا تتخلى عن SHA256، غير مهدد على المدى القريب بواسطة PQ
- لا تختر المتغيرات المفضلة النهائية في هذا الوقت

## نموذج التهديد

- أجهزة router في OBEP أو IBGW، والتي قد تتواطأ،
  لتخزين رسائل garlic encryption لفك تشفيرها لاحقاً (السرية المستقبلية)
- مراقبو الشبكة
  الذين يخزنون رسائل النقل لفك تشفيرها لاحقاً (السرية المستقبلية)
- مشاركو الشبكة الذين يزورون التوقيعات لـ RI أو LS أو streaming أو datagrams،
  أو هياكل أخرى

## البروتوكولات المتأثرة

سنقوم بتعديل البروتوكولات التالية، تقريباً بترتيب التطوير. سيكون الطرح الإجمالي على الأرجح من أواخر 2025 حتى منتصف 2027. راجع قسم الأولويات والطرح أدناه للحصول على التفاصيل.

| البروتوكول / الميزة | الحالة |
|--------------------|--------|
| Hybrid MLKEM Ratchet and LS | تمت الموافقة 2025-06؛ بيتا 2025-08؛ إصدار 2025-11 |
| Hybrid MLKEM NTCP2 | تم اختباره على الشبكة المباشرة، تمت الموافقة 2026-02؛ هدف البيتا 2026-05؛ هدف الإصدار 2026-08 |
| Hybrid MLKEM SSU2 | تمت الموافقة 2026-02؛ هدف البيتا 2026-08؛ هدف الإصدار 2026-11 |
| MLDSA SigTypes 12-14 | الاقتراح مستقر لكن قد لا يكتمل حتى 2027 |
| MLDSA Dests | تم اختباره على الشبكة المباشرة، يتطلب ترقية الشبكة لدعم floodfill |
| Hybrid SigTypes 15-17 | أولي |
| Hybrid Dests | |
## التصميم

سنقوم بدعم معايير NIST FIPS 203 و 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) والتي تستند إلى، ولكنها غير متوافقة مع، CRYSTALS-Kyber و CRYSTALS-Dilithium (الإصدارات 3.1، 3، والإصدارات الأقدم).

### تبادل المفاتيح

سندعم تبادل المفاتيح المختلط في البروتوكولات التالية:

| البروتوكول | نوع Noise | دعم PQ فقط؟ | دعم هجين؟ |
|---------|------------|------------------|-----------------|
| NTCP2   | XK         | لا               | نعم             |
| SSU2    | XK         | لا               | نعم             |
| Ratchet | IK         | لا               | نعم             |
| TBM     | N          | لا               | لا              |
| NetDB   | N          | لا               | لا              |
PQ KEM يوفر مفاتيح مؤقتة فقط، ولا يدعم بشكل مباشر عمليات المصافحة بالمفاتيح الثابتة مثل Noise XK و IK.

Noise N لا يستخدم تبادل مفاتيح ثنائي الاتجاه وبالتالي فهو غير مناسب للتشفير الهجين.

لذلك سندعم التشفير الهجين فقط، لـ NTCP2 و SSU2 و Ratchet. سنعرّف المتغيرات الثلاثة لـ ML-KEM كما هو موضح في [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)، للحصول على 3 أنواع تشفير جديدة إجمالاً. الأنواع الهجينة ستُعرّف فقط بالتركيب مع X25519.

أنواع التشفير الجديدة هي:

| النوع | الكود |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
ستكون النفقات العامة كبيرة. أحجام الرسائل النموذجية 1 و 2 (لـ XK و IK) تبلغ حالياً حوالي 100 بايت (قبل أي حمولة إضافية). سيزداد هذا بمقدار 8 إلى 15 مرة حسب الخوارزمية.

### التوقيعات

سندعم التوقيعات PQ والهجينة في الهياكل التالية:

| النوع | دعم PQ فقط؟ | دعم المختلط؟ |
|------|------------------|-----------------|
| RouterInfo | نعم | نعم |
| LeaseSet | نعم | نعم |
| Streaming SYN/SYNACK/Close | نعم | نعم |
| Repliable Datagrams | نعم | نعم |
| Datagram2 (prop. 163) | نعم | نعم |
| I2CP create session msg | نعم | نعم |
| ملفات SU3 | نعم | نعم |
| شهادات X.509 | نعم | نعم |
| مخازن مفاتيح Java | نعم | نعم |
لذلك سندعم التوقيعات الخاصة بـ PQ فقط والتوقيعات المختلطة. سنحدد المتغيرات الثلاثة لـ ML-DSA كما هو موضح في [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)، وثلاثة متغيرات مختلطة مع Ed25519، وثلاثة متغيرات خاصة بـ PQ فقط مع prehash لملفات SU3 فقط، بإجمالي 9 أنواع توقيع جديدة. ستُحدد الأنواع المختلطة فقط بالتركيب مع Ed25519. سنستخدم ML-DSA القياسي، وليس متغيرات pre-hash (HashML-DSA)، باستثناء ملفات SU3.

سوف نستخدم متغير التوقيع "المحوط" أو العشوائي، وليس المتغير "الحتمي"، كما هو معرّف في [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) القسم 3.4. هذا يضمن أن كل توقيع يكون مختلفاً، حتى عند التوقيع على نفس البيانات، ويوفر حماية إضافية ضد هجمات القنوات الجانبية. راجع قسم ملاحظات التنفيذ أدناه للتفاصيل الإضافية حول خيارات الخوارزمية بما في ذلك التشفير والسياق.

أنواع التوقيع الجديدة هي:

| النوع | الكود |
|------|------|
| MLDSA44 | 12 |
| MLDSA65 | 13 |
| MLDSA87 | 14 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 |
| MLDSA44ph | 18 |
| MLDSA65ph | 19 |
| MLDSA87ph | 20 |
شهادات X.509 والتشفيرات الأخرى بصيغة DER ستستخدم الهياكل المركبة ومعرفات الكائنات المحددة في [مسودة IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

ستكون الأعباء الإضافية كبيرة. أحجام وجهة Ed25519 النموذجية وهوية router هي 391 بايت. ستزداد هذه بمقدار 3.5 إلى 6.8 مرة حسب الخوارزمية. توقيعات Ed25519 هي 64 بايت. ستزداد هذه بمقدار 38 إلى 76 مرة حسب الخوارزمية. RouterInfo الموقع والـ LeaseSet ومخططات البيانات القابلة للرد ورسائل streaming الموقعة النموذجية تبلغ حوالي 1KB. ستزداد هذه بمقدار 3 إلى 8 مرات حسب الخوارزمية.

نظرًا لأن أنواع الهوية الجديدة للوجهة والـ router لن تحتوي على حشو، فإنها لن تكون قابلة للضغط. أحجام الوجهات وهويات الـ router المضغوطة بـ gzip أثناء النقل ستزيد بمقدار 12 إلى 38 مرة حسب الخوارزمية.

### التركيبات القانونية

بالنسبة للوجهات، أنواع التوقيع الجديدة مدعومة مع جميع أنواع التشفير في leaseSet. قم بتعيين نوع التشفير في شهادة المفتاح إلى NONE (255).

بالنسبة لـ RouterIdentities، نوع تشفير ElGamal مُهمل. أنواع التوقيع الجديدة مدعومة مع تشفير X25519 (النوع 4) فقط. أنواع التشفير الجديدة سيتم الإشارة إليها في RouterAddresses. نوع التشفير في شهادة المفتاح سيستمر كونه النوع 4.

### مطلوب تشفير جديد

- ML-KEM (المعروف سابقاً باسم CRYSTALS-Kyber) [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
- ML-DSA (المعروف سابقاً باسم CRYSTALS-Dilithium) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
- SHA3-128 (المعروف سابقاً باسم Keccak-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf) يُستخدم فقط لـ SHAKE128
- SHA3-256 (المعروف سابقاً باسم Keccak-512) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- SHAKE128 و SHAKE256 (امتدادات XOF لـ SHA3-128 و SHA3-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)

متجهات الاختبار لـ SHA3-256 و SHAKE128 و SHAKE256 متوفرة في [NIST](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values).

لاحظ أن مكتبة Java bouncycastle تدعم جميع ما سبق. دعم مكتبة C++ متوفر في OpenSSL 3.5 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### البدائل

لن ندعم [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) (Sphincs+)، فهو أبطأ بكثير وأكبر حجماً من ML-DSA. لن ندعم FIPS206 القادم (Falcon)، فهو لم يُعتمد كمعيار بعد. لن ندعم NTRU أو مرشحي التشفير ما بعد الكمي الآخرين التي لم تعتمدها NIST كمعايير.

### Rosenpass

يوجد بعض البحوث [الورقة البحثية](https://eprint.iacr.org/2020/379.pdf) حول تكييف Wireguard (IK) للتشفير PQ النقي، ولكن هناك عدة أسئلة مفتوحة في تلك الورقة. لاحقاً، تم تنفيذ هذا النهج كـ Rosenpass [Rosenpass](https://rosenpass.eu/) [الورقة البيضاء](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf) لـ PQ Wireguard.

يستخدم Rosenpass مصافحة شبيهة بـ Noise KK مع مفاتيح ثابتة مشتركة مسبقاً من Classic McEliece 460896 (500 كيلوبايت لكل منها) ومفاتيح مؤقتة Kyber-512 (في الأساس MLKEM-512). نظراً لأن نصوص Classic McEliece المشفرة تبلغ 188 بايت فقط، ومفاتيح Kyber-512 العامة والنصوص المشفرة معقولة الحجم، فإن كلا رسالتي المصافحة تتسعان ضمن MTU قياسي لـ UDP. المفتاح المشترك الناتج (osk) من مصافحة PQ KK يُستخدم كمفتاح مشترك مسبقاً مدخل (psk) لمصافحة Wireguard IK المعيارية. لذا هناك مصافحتان كاملتان في المجموع، واحدة PQ خالصة وأخرى X25519 خالصة.

لا يمكننا القيام بأي من هذا لاستبدال مصافحات XK و IK الخاصة بنا لأن:

- لا يمكننا القيام بـ KK، بوب لا يملك المفتاح الثابت الخاص بأليس
- المفاتيح الثابتة بحجم 500KB كبيرة جداً
- لا نريد رحلة إضافية ذهاباً وإياباً

هناك الكثير من المعلومات المفيدة في الورقة البيضاء، وسنقوم بمراجعتها للحصول على أفكار وإلهام. TODO.

## المواصفة

### البُنى الشائعة

قم بتحديث الأقسام والجداول في وثيقة البُنى المشتركة [/docs/specs/common-structures/](/docs/specs/common-structures/) كما يلي:

### PublicKey

أنواع المفاتيح العامة الجديدة هي:

| النوع | طول المفتاح العام | منذ | الاستخدام |
|------|-------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM512 | 800 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| MLKEM768 | 1184 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| MLKEM1024 | 1568 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| MLKEM512_CT | 768 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| MLKEM768_CT | 1088 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| MLKEM1024_CT | 1568 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| NONE | 0 | 0.9.xx | انظر الاقتراح 169، للوجهات مع أنواع توقيع PQ فقط، وليس لـ RIs أو Leasesets |
المفاتيح العامة الهجينة هي مفتاح X25519. مفاتيح KEM العامة هي مفتاح PQ المؤقت المرسل من Alice إلى Bob. الترميز وترتيب البايتات محددان في [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

مفاتيح MLKEM*_CT ليست مفاتيح عامة حقيقية، بل هي "النص المشفر" المرسل من Bob إلى Alice في مصافحة Noise. وهي مدرجة هنا من أجل الاكتمال.

### المفتاح الخاص

أنواع المفاتيح الخاصة الجديدة هي:

| النوع | طول المفتاح الخاص | منذ | الاستخدام |
|------|---------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM512 | 1632 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| MLKEM768 | 2400 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
| MLKEM1024 | 3168 | 0.9.xx | انظر الاقتراح 169، للمصافحات فقط، وليس لـ Leasesets أو RIs أو Destinations |
المفاتيح الخاصة الهجينة هي مفاتيح X25519. مفاتيح KEM الخاصة مخصصة لأليس فقط. ترميز KEM وترتيب البايتات محددان في [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

### مفتاح التوقيع العام

أنواع مفاتيح التوقيع العامة الجديدة هي:

| النوع | الطول (بايت) | منذ | الاستخدام |
|------|----------------|-------|-------|
| MLDSA44 | 1312 | 0.9.xx | انظر اقتراح 169 |
| MLDSA65 | 1952 | 0.9.xx | انظر اقتراح 169 |
| MLDSA87 | 2592 | 0.9.xx | انظر اقتراح 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 0.9.xx | انظر اقتراح 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 0.9.xx | انظر اقتراح 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 0.9.xx | انظر اقتراح 169 |
| MLDSA44ph | 1344 | 0.9.xx | فقط لملفات SU3، وليس لهياكل netDb |
| MLDSA65ph | 1984 | 0.9.xx | فقط لملفات SU3، وليس لهياكل netDb |
| MLDSA87ph | 2624 | 0.9.xx | فقط لملفات SU3، وليس لهياكل netDb |
المفاتيح العامة للتوقيع الهجين هي مفتاح Ed25519 متبوعاً بمفتاح PQ، كما هو موضح في [مسودة IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). التشفير وترتيب البايتات محددان في [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### مفتاح التوقيع الخاص

أنواع مفاتيح التوقيع الخاصة الجديدة هي:

| النوع | الطول (بايت) | منذ | الاستخدام |
|------|----------------|-------|-------|
| MLDSA44 | 2560 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA65 | 4032 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA87 | 4896 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2592 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 4064 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4928 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA44ph | 2592 | 0.9.xx | لملفات SU3 فقط، وليس لهياكل netDb. انظر الاقتراح 169 |
| MLDSA65ph | 4064 | 0.9.xx | لملفات SU3 فقط، وليس لهياكل netDb. انظر الاقتراح 169 |
| MLDSA87ph | 4928 | 0.9.xx | لملفات SU3 فقط، وليس لهياكل netDb. انظر الاقتراح 169 |
مفاتيح التوقيع الخاصة الهجينة هي مفتاح Ed25519 متبوعاً بمفتاح PQ، كما هو موضح في [مسودة IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). التشفير وترتيب البايتات محددان في [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### التوقيع

أنواع التوقيع الجديدة هي:

| النوع | الطول (بايت) | منذ | الاستخدام |
|------|----------------|-------|-------|
| MLDSA44 | 2420 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA65 | 3309 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA87 | 4627 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2484 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 3373 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4691 | 0.9.xx | انظر الاقتراح 169 |
| MLDSA44ph | 2484 | 0.9.xx | لملفات SU3 فقط، وليس لهياكل netDb. انظر الاقتراح 169 |
| MLDSA65ph | 3373 | 0.9.xx | لملفات SU3 فقط، وليس لهياكل netDb. انظر الاقتراح 169 |
| MLDSA87ph | 4691 | 0.9.xx | لملفات SU3 فقط، وليس لهياكل netDb. انظر الاقتراح 169 |
التوقيعات المختلطة هي توقيع Ed25519 متبوعاً بتوقيع PQ، كما هو موضح في [مسودة IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). يتم التحقق من التوقيعات المختلطة من خلال التحقق من كلا التوقيعين، والفشل في حال فشل أي منهما. يتم تعريف التشفير وترتيب البايتات في [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### شهادات المفاتيح

أنواع مفاتيح التوقيع العامة الجديدة هي:

| النوع | رمز النوع | إجمالي طول المفتاح العام | منذ | الاستخدام |
|------|-----------|-------------------------|-------|-------|
| MLDSA44 | 12 | 1312 | 0.9.xx | راجع الاقتراح 169 |
| MLDSA65 | 13 | 1952 | 0.9.xx | راجع الاقتراح 169 |
| MLDSA87 | 14 | 2592 | 0.9.xx | راجع الاقتراح 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 0.9.xx | راجع الاقتراح 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 0.9.xx | راجع الاقتراح 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 0.9.xx | راجع الاقتراح 169 |
| MLDSA44ph | 18 | غير متاح | 0.9.xx | فقط لملفات SU3 |
| MLDSA65ph | 19 | غير متاح | 0.9.xx | فقط لملفات SU3 |
| MLDSA87ph | 20 | غير متاح | 0.9.xx | فقط لملفات SU3 |
أنواع مفاتيح التشفير العامة الجديدة هي:

| النوع | كود النوع | إجمالي طول المفتاح العام | منذ | الاستخدام |
|------|-----------|-------------------------|-------|-------|
| MLKEM512_X25519 | 5 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM768_X25519 | 6 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| MLKEM1024_X25519 | 7 | 32 | 0.9.xx | انظر الاقتراح 169، لـ Leasesets فقط، وليس لـ RIs أو Destinations |
| NONE | 255 | 0 | 0.9.xx | انظر الاقتراح 169 |
أنواع المفاتيح الهجينة لا يتم تضمينها أبداً في شهادات المفاتيح؛ فقط في leasesets.

بالنسبة للوجهات التي تستخدم أنواع التوقيع Hybrid أو PQ، استخدم NONE (النوع 255) لنوع التشفير، ولكن لا يوجد مفتاح تشفير، والقسم الرئيسي البالغ 384 بايت بأكمله مخصص لمفتاح التوقيع.

### أحجام الوجهات

إليكم الأطوال للأنواع الجديدة من Destination. نوع التشفير لجميعها هو NONE (النوع 255) وطول مفتاح التشفير يُعامل كـ 0. يُستخدم القسم بأكمله المكون من 384 بايت للجزء الأول من مفتاح التوقيع العام. ملاحظة: هذا مختلف عن المواصفات لأنواع التوقيع ECDSA_SHA512_P521 وRSA، حيث احتفظنا بمفتاح ElGamal بحجم 256 بايت في الوجهة رغم أنه لم يكن مُستخدماً.

لا توجد حشوة. الطول الإجمالي هو 7 + إجمالي طول المفتاح. طول شهادة المفتاح هو 4 + طول المفتاح الزائد.

مثال على تدفق البايتات للوجهة بحجم 1319 بايت لـ MLDSA44:

skey[0:383] 5 (932 >> 8) (932 & 0xff) 00 12 00 255 skey[384:1311]

| النوع | رمز النوع | إجمالي طول المفتاح العام | الرئيسي | الفائض | إجمالي طول الوجهة |
|------|-----------|-------------------------|------|--------|-------------------|
| MLDSA44 | 12 | 1312 | 384 | 928 | 1319 |
| MLDSA65 | 13 | 1952 | 384 | 1568 | 1959 |
| MLDSA87 | 14 | 2592 | 384 | 2208 | 2599 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 384 | 960 | 1351 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 384 | 1600 | 1991 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 384 | 2240 | 2631 |
### أحجام RouterIdent

إليك الأطوال لأنواع الوجهة الجديدة. نوع التشفير لجميعها هو X25519 (النوع 4). يتم استخدام القسم الكامل البالغ 352 بايت بعد المفتاح العام X28819 للجزء الأول من مفتاح التوقيع العام. لا توجد حشوة. الطول الإجمالي هو 39 + إجمالي طول المفتاح. طول شهادة المفتاح هو 4 + طول المفتاح الإضافي.

مثال على تدفق بايتات هوية router بحجم 1351 بايت لـ MLDSA44:

enckey[0:31] skey[0:351] 5 (960 >> 8) (960 & 0xff) 00 12 00 4 skey[352:1311]

| النوع | رمز النوع | إجمالي طول المفتاح العام | الرئيسي | الفائض | إجمالي طول RouterIdent |
|------|-----------|-------------------------|------|--------|--------------------------|
| MLDSA44 | 12 | 1312 | 352 | 960 | 1351 |
| MLDSA65 | 13 | 1952 | 352 | 1600 | 1991 |
| MLDSA87 | 14 | 2592 | 352 | 2240 | 2631 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 352 | 992 | 1383 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 352 | 1632 | 2023 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 352 | 2272 | 2663 |
### أنماط المصافحة

تستخدم المصافحات أنماط مصافحة [Noise Protocol](https://noiseprotocol.org/noise.html).

يتم استخدام تطابق الأحرف التالي:

- e = مفتاح مؤقت لمرة واحدة
- s = مفتاح ثابت
- p = حمولة الرسالة
- e1 = مفتاح PQ مؤقت لمرة واحدة، يُرسل من Alice إلى Bob
- ekem1 = نص KEM المشفر، يُرسل من Bob إلى Alice

التعديلات التالية على XK و IK للسرية الأمامية المختلطة (hfs) محددة كما هو موضح في [مواصفات Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) القسم 5:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  IK:                       IKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, s, ss, p       -> e, es, e1, s, ss, p
  <- tag, e, ee, se, p     <- tag, e, ee, ekem1, se, p
  <- p                     <- p
  p ->                     p ->

  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
يتم تعريف نمط e1 كما يلي، كما هو محدد في [مواصفات Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) القسم 4:

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
يتم تعريف نمط ekem1 كما يلي، كما هو محدد في [مواصفات Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) القسم 4:

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### دالة اشتقاق المفاتيح لمصافحة Noise

#### المشاكل

- هل يجب أن نغير دالة الـ hash الخاصة بالـ handshake؟ راجع [المقارنة](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3).
  SHA256 غير معرض للخطر من PQ، لكن إذا كنا نريد ترقية
  دالة الـ hash الخاصة بنا، فهذا هو الوقت المناسب، بينما نقوم بتغيير أشياء أخرى.
  الاقتراح الحالي لـ IETF SSH [مسودة IETF](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/) هو استخدام MLKEM768
  مع SHA256، و MLKEM1024 مع SHA384. هذا الاقتراح يتضمن
  مناقشة حول الاعتبارات الأمنية.
- هل يجب أن نتوقف عن إرسال بيانات ratchet الـ 0-RTT (غير الـ LS)؟
- هل يجب أن نبدل الـ ratchet من IK إلى XK إذا لم نرسل بيانات 0-RTT؟

#### نظرة عامة

ينطبق هذا القسم على بروتوكولي IK و XK.

يتم تعريف المصافحة الهجينة في [مواصفات Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). الرسالة الأولى، من Alice إلى Bob، تحتوي على e1، مفتاح التغليف، قبل حمولة الرسالة. يتم التعامل مع هذا كمفتاح ثابت إضافي؛ استدعِ EncryptAndHash() عليه (كـ Alice) أو DecryptAndHash() (كـ Bob). ثم قم بمعالجة حمولة الرسالة كالمعتاد.

الرسالة الثانية، من Bob إلى Alice، تحتوي على ekem1، النص المشفر، قبل حمولة الرسالة. يتم التعامل معها كمفتاح ثابت إضافي؛ قم باستدعاء EncryptAndHash() عليها (كـ Bob) أو DecryptAndHash() (كـ Alice). ثم، احسب kem_shared_key واستدعي MixKey(kem_shared_key). ثم قم بمعالجة حمولة الرسالة كالمعتاد.

#### عمليات ML-KEM المحددة

نحدد الدوال التالية المقابلة للوحدات البنائية التشفيرية المستخدمة كما هو معرّف في [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

لاحظ أن كلاً من encap_key والنص المشفر مشفران داخل كتل ChaCha/Poly في رسائل مصافحة Noise 1 و 2. سيتم فك تشفيرهما كجزء من عملية المصافحة.

يتم خلط kem_shared_key في chaining key باستخدام MixHash(). انظر أدناه للتفاصيل.

#### Alice KDF للرسالة 1

بالنسبة لـ XK: بعد نمط الرسالة 'es' وقبل الحمولة، أضف:

أو

بالنسبة لـ IK: بعد نمط الرسالة 'es' وقبل نمط الرسالة 's'، أضف:

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF للرسالة 1

بالنسبة لـ XK: بعد نمط رسالة 'es' وقبل البيانات النافعة، أضف:

أو

بالنسبة لـ IK: بعد نمط رسالة 'es' وقبل نمط رسالة 's'، أضف:

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF للرسالة 2

بالنسبة لـ XK: بعد نمط الرسالة 'ee' وقبل الحمولة، أضف:

أو

بالنسبة لـ IK: بعد نمط الرسالة 'ee' وقبل نمط الرسالة 'se'، أضف:

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### Alice KDF للرسالة 2

بعد نمط الرسالة 'ee' (وقبل نمط الرسالة 'ss' لـ IK)، أضف:

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### KDF للرسالة 3 (XK فقط)

دون تغيير

#### KDF لـ split()

دون تغيير

### آلية التشفير المتدرج (Ratchet)

قم بتحديث مواصفات ECIES-Ratchet [/docs/specs/ecies/](/docs/specs/ecies/) كما يلي:

#### معرفات Noise

- "Noise_IKhfselg2_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1b) تنسيق الجلسة الجديد (مع الربط)

التغييرات: احتوى الـ ratchet الحالي على المفتاح الثابت في القسم الأول من ChaCha، والحمولة في القسم الثاني. مع ML-KEM، توجد الآن ثلاثة أقسام. يحتوي القسم الأول على المفتاح العام PQ المشفر. يحتوي القسم الثاني على المفتاح الثابت. يحتوي القسم الثالث على الحمولة.

التنسيق المشفر:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   New Session Ephemeral Public Key    |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           ML-KEM encap_key            +
  |       ChaCha20 encrypted data         |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for encap_key Section        +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           X25519 Static Key           +
  |       ChaCha20 encrypted data         |
  +             32 bytes                  +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for Static Key Section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
التنسيق المفكوك التشفير:

```
Payload Part 1:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM encap_key                +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       X25519 Static Key               +
  |                                       |
  +      (32 bytes)                       +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
الأحجام:

| النوع | كود النوع | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | pl len |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 96+pl | 64+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 912+pl | 880+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1296+pl | 1360+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1680+pl | 1648+pl | 1568+pl | 1568 | pl |
لاحظ أن الحمولة يجب أن تحتوي على كتلة DateTime، لذلك الحد الأدنى لحجم الحمولة هو 7. يمكن حساب الأحجام الدنيا للرسالة 1 وفقاً لذلك.

#### 1ز) تنسيق رد الجلسة الجديدة

التغييرات: ratchet الحالي له payload فارغ للقسم الأول من ChaCha، و payload في القسم الثاني. مع ML-KEM، يوجد الآن ثلاثة أقسام. القسم الأول يحتوي على النص المشفر PQ المشفر. القسم الثاني له payload فارغ. القسم الثالث يحتوي على payload.

التنسيق المشفر:

```
  +----+----+----+----+----+----+----+----+
  |       Session Tag   8 bytes           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Ephemeral Public Key           +
  |                                       |
  +            32 bytes                   +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  | ChaCha20 encrypted ML-KEM ciphertext  |
  +      (see table below for length)     +
  ~                                       ~
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for ciphertext Section         +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for key Section (no data)      +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
التنسيق المفكوك التشفير:

```
Payload Part 1:


  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM ciphertext               +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  empty

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
الأحجام:

| النوع | كود النوع | طول Y | طول الرسالة 2 | طول تشفير الرسالة 2 | طول فك تشفير الرسالة 2 | طول PQ CT | طول opt |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 72+pl | 32+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 856+pl | 816+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1176+pl | 1136+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1656+pl | 1616+pl | 1568+pl | 1568 | pl |
لاحظ أنه بينما ستحتوي الرسالة 2 عادة على حمولة غير صفرية، فإن مواصفات ratchet [/docs/specs/ecies/](/docs/specs/ecies/) لا تتطلب ذلك، لذا فإن الحد الأدنى لحجم الحمولة هو 0. يمكن حساب الأحجام الدنيا للرسالة 2 وفقاً لذلك.

### NTCP2

حدث مواصفات NTCP2 [/docs/specs/ntcp2/](/docs/specs/ntcp2/) كما يلي:

#### معرفات Noise

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

التغييرات: NTCP2 الحالي يحتوي فقط على الخيارات في قسم ChaCha. مع ML-KEM، سيحتوي قسم ChaCha أيضاً على المفتاح العام PQ المشفر.

حتى يمكن دعم NTCP2 مع PQ وبدون PQ على نفس عنوان وميناء router، نستخدم البت الأكثر أهمية في قيمة X (المفتاح العام المؤقت X25519) لتمييز أنه اتصال PQ. هذا البت يكون دائماً غير مُعيَّن للاتصالات غير PQ.

بالنسبة لأليس، بعد تشفير الرسالة بواسطة Noise، ولكن قبل تشويش AES للـ X، قم بتعيين X[31] |= 0x7f.

بالنسبة لـ Bob، بعد إلغاء تشويش AES لـ X، اختبر X[31] & 0x80. إذا كان البت مُعيّن، امحه باستخدام X[31] &= 0x7f، وفكّ التشفير عبر Noise كاتصال PQ. إذا كان البت غير مُعيّن، فكّ التشفير عبر Noise كاتصال غير PQ كالمعتاد.

بالنسبة لـ PQ NTCP2 المُعلن عنه على عنوان router مختلف ومنفذ مختلف، فهذا غير مطلوب.

للحصول على معلومات إضافية، راجع قسم العناوين المنشورة أدناه.

المحتويات الخام:

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
البيانات غير المشفرة (علامة مصادقة Poly1305 غير معروضة):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
ملاحظة: يجب تعيين حقل الإصدار في كتلة خيارات الرسالة 1 إلى 2، حتى لاتصالات PQ.

الأحجام:

| النوع | رمز النوع | طول X | طول الرسالة 1 | طول الرسالة 1 المشفرة | طول الرسالة 1 المفكوكة | طول مفتاح PQ | طول الخيارات |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
ملاحظة: رموز الأنواع للاستخدام الداخلي فقط. ستبقى الـ routers من النوع 4، وسيتم الإشارة إلى الدعم في عناوين الـ router.

#### 2) SessionCreated

المحتويات الخام:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير معروضة):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
الأحجام:

| النوع | كود النوع | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
ملاحظة: رموز الأنواع للاستخدام الداخلي فقط. ستبقى routers من النوع 4، وسيتم الإشارة إلى الدعم في عناوين router.

#### 3) SessionConfirmed

بدون تغيير

#### دالة اشتقاق المفتاح (KDF) (لمرحلة البيانات)

بدون تغيير

#### العناوين المنشورة

في جميع الحالات، استخدم اسم نقل NTCP2 كالمعتاد.

استخدم نفس العنوان/المنفذ كما هو الحال مع غير-PQ، غير محجوب بجدار حماية. يتم دعم متغير PQ واحد فقط. في عنوان الـ router، انشر v=2 (كالمعتاد) والمعامل الجديد pq=[3|4|5] للإشارة إلى MLKEM 512/768/1024. تقوم Alice بتعيين البت الأكثر أهمية للمفتاح المؤقت (key[31] & 0x80) في طلب الجلسة للإشارة إلى أن هذا اتصال هجين. انظر أعلاه. الـ routers الأقدم ستتجاهل معامل pq وتتصل بشكل غير-pq كالمعتاد.

عنوان/منفذ مختلف عن non-PQ، أو PQ-only، non-firewalled غير مدعوم. لن يتم تنفيذ هذا حتى يتم تعطيل non-PQ NTCP2، بعد عدة سنوات من الآن. عندما يتم تعطيل non-PQ، قد يتم دعم متغيرات PQ متعددة، ولكن واحد فقط لكل عنوان. في عنوان الـ router، انشر v=[3|4|5] للإشارة إلى MLKEM 512/768/1024. Alice لا تقوم بتعيين MSB للمفتاح المؤقت. الـ routers الأقدم ستتحقق من معامل v وتتخطى هذا العنوان كونه غير مدعوم.

العناوين المحمية بجدار الحماية (لا يتم نشر IP): في عنوان router، قم بنشر v=2 (كالمعتاد). لا حاجة لنشر معامل pq.

يمكن لأليس الاتصال بـ Bob المقاوم للكم (PQ) باستخدام متغير PQ الذي ينشره Bob، سواء كانت أليس تعلن عن دعم pq في معلومات router الخاص بها أم لا، أو ما إذا كانت تعلن عن نفس المتغير.

#### الحد الأقصى للحشو

في المواصفة الحالية، تم تعريف الرسائل 1 و 2 لتحتوي على كمية "معقولة" من الحشو، مع نطاق موصى به من 0-31 بايت، وبدون تحديد حد أقصى.

حتى API 0.9.68 (الإصدار 2.11.0)، طبقت Java I2P حداً أقصى قدره 256 بايت للحشو للاتصالات غير PQ، ولكن هذا لم يكن موثقاً مسبقاً. اعتباراً من API 0.9.69 (الإصدار 2.12.0)، تطبق Java I2P نفس الحد الأقصى للحشو للاتصالات غير PQ كما هو الحال مع MLKEM-512. انظر الجدول أدناه.

استخدم حجم الرسالة المحدد كحد أقصى للحشو، أي أن الحد الأقصى للحشو سيضاعف حجم الرسالة لاتصالات PQ، كما يلي:

| الحد الأقصى لحشو الرسالة | غير-PQ (حتى 0.9.68) | غير-PQ (اعتباراً من 0.9.69) | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------|----------------------|-----------------------|-----------|-----------|------------|
| Session Request  |   256   |   880   |    880   |     1264   |    1648  |
| Session Created  |   256   |   848   |    848   |     1136   |    1616  |
### SSU2

حدّث مواصفات SSU2 [/docs/specs/ssu2/](/docs/specs/ssu2/) كما يلي:

#### معرفات Noise

- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"

لاحظ أن MLKEM-1024 غير مدعوم لـ SSU2، حيث أن المفاتيح كبيرة جداً بحيث لا تتسع ضمن datagram قياسي بحجم 1500 بايت.

#### عنوان طويل

الرأس الطويل يبلغ 32 بايت. يُستخدم قبل إنشاء الجلسة، لطلب الرمز المميز، وطلب الجلسة، وإنشاء الجلسة، والمحاولة مرة أخرى. كما يُستخدم أيضاً لرسائل اختبار النظراء وثقب الجدار الناري خارج الجلسة.

في الرسائل التالية، قم بتعيين حقل ver (الإصدار) في الرأس الطويل إلى 3 أو 4، للإشارة إلى MLKEM-512 أو MLKEM-768.

- (0) طلب الجلسة
- (1) تم إنشاء الجلسة
- (9) إعادة المحاولة
- (10) طلب الرمز المميز
- (11) ثقب الاتصال

في الرسائل التالية، اضبط حقل ver (الإصدار) في الرأس الطويل على 2، كالمعتاد، حتى لو كان MLKEM-512 أو MLKEM-768 مدعوماً. قد تقوم التطبيقات أيضاً بتعيين القيمة إلى 3 أو 4، إذا كان الطرف الآخر يدعم ذلك، لكن هذا ليس ضرورياً. يجب على التطبيقات قبول أي قيمة من 2-4.

- (7) اختبار النظير (رسائل خارج الجلسة 5-7)

المناقشة: قد لا يكون تعيين حقل الإصدار إلى 3 أو 4 ضروريًا بشكل صارم لجميع أنواع الرسائل، لكن القيام بذلك يساعد في الكشف المبكر عن الفشل للاتصالات غير المدعومة لما بعد الكم. يجب أن تحتوي رسائل Token Request و Retry (الأنواع 9 و 10) على الإصدارات 3/4 للاتساق. قد لا تتطلب رسائل Hole Punch (النوع 11) هذه المعاملة لكننا سنتبع نفس النمط للتوحيد. رسائل Peer Test (النوع 7) خارج الجلسة ولا تشير إلى نية بدء جلسة.

قبل تشفير الرأس:

```

  +----+----+----+----+----+----+----+----+
  |      Destination Connection ID        |
  +----+----+----+----+----+----+----+----+
  |   Packet Number   |type| ver| id |flag|
  +----+----+----+----+----+----+----+----+
  |        Source Connection ID           |
  +----+----+----+----+----+----+----+----+
  |                 Token                 |
  +----+----+----+----+----+----+----+----+

  Destination Connection ID :: 8 bytes, unsigned big endian integer

  Packet Number :: 4 bytes, unsigned big endian integer

  type :: The message type = 0, 1, 7, 9, 10, or 11

  ver :: The protocol version = 2, 3, or 4 for non-PQ, MLKEM512, MLKEM768

  id :: 1 byte, the network ID (currently 2, except for test networks)

  flag :: 1 byte, unused, set to 0 for future compatibility

  Source Connection ID :: 8 bytes, unsigned big endian integer

  Token :: 8 bytes, unsigned big endian integer

```
#### رأس قصير

غير متغير

#### SessionRequest (النوع 0)

التغييرات: SSU2 الحالي يحتوي فقط على بيانات الكتلة في قسم ChaCha. مع ML-KEM، سيحتوي قسم ChaCha أيضاً على المفتاح العام PQ المشفر.

تغيير KDF لحماية التلاعب: لمعالجة القضايا المطروحة في الاقتراح 165 [Prop165]_، ولكن مع حل مختلف، نقوم بتعديل KDF لطلب الجلسة. هذا فقط لجلسات PQ. يبقى KDF للجلسات غير PQ دون تغيير.

```

// End of KDF for initial chain key (unchanged)
  // Bob static key
  // MixHash(bpk)
  h = SHA256(h || bpk);

  // Start of KDF for session request
  // NEW for PQ only
  // bhash = Bob router hash (32 bytes)
  // MixHash(bhash)
  h = SHA256(h || bhash);

  // Rest of KDF for session request, unchanged, as in SSU2 spec
  // MixHash(header)
  h = SHA256(h || header)

  ...

```
المحتويات الخام:

```
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 0-15, ChaCha20     |
  +  encrypted with Bob intro key         +
  |    See Header Encryption KDF          |
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 16-31, ChaCha20    |
  +  encrypted with Bob intro key n=0     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +       X, ChaCha20 encrypted           +
  |       with Bob intro key n=0          |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaCha20 encrypted data (MLKEM)     |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaCha20 encrypted data (payload)   |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Poly1305 MAC (16 bytes)        +
  |                                       |
  +----+----+----+----+----+----+----+----+


```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير معروضة):

```
  +----+----+----+----+----+----+----+----+
  |      Destination Connection ID        |
  +----+----+----+----+----+----+----+----+
  |   Packet Number   |type| ver| id |flag|
  +----+----+----+----+----+----+----+----+
  |        Source Connection ID           |
  +----+----+----+----+----+----+----+----+
  |                 Token                 |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |     see below for allowed blocks      |
  +----+----+----+----+----+----+----+----+
```
الأحجام، غير شاملة النفقات العامة لـ IP:

| النوع | رمز النوع | طول X | طول الرسالة 1 | طول الرسالة 1 المشفرة | طول الرسالة 1 المفكوكة | طول مفتاح PQ | طول pl |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 896+pl | 832+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1280+pl | 1216+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | n/a | كبير جداً | | | | |
ملاحظة: رموز الأنواع مخصصة للاستخدام الداخلي فقط. ستبقى الـ routers من النوع 4، وسيتم الإشارة إلى الدعم في عناوين الـ router.

الحد الأدنى لـ MTU لـ MLKEM768_X25519: حوالي 1316 لـ IPv4 و 1336 لـ IPv6.

#### SessionCreated (النوع 1)

التغييرات: يحتوي SSU2 الحالي على بيانات الكتلة فقط في قسم ChaCha. مع ML-KEM، سيحتوي قسم ChaCha أيضاً على المفتاح العام PQ المشفر.

المحتويات الخام:

```
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 0-15, ChaCha20     |
  +  encrypted with Bob intro key and     +
  | derived key, see Header Encryption KDF|
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 16-31, ChaCha20    |
  +  encrypted with derived key n=0       +
  |  See Header Encryption KDF            |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +       Y, ChaCha20 encrypted           +
  |       with derived key n=0            |
  +              (32 bytes)               +
  |       See Header Encryption KDF       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaCha20 data (MLKEM)               |
  +   Encrypted and authenticated data    +
  |  length varies                        |
  +  k defined in KDF for Session Created +
  |  n = 0; see KDF for associated data   |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaCha20 data (payload)             |
  +   Encrypted and authenticated data    +
  |  length varies                        |
  +  k defined in KDF for Session Created +
  |  n = 0; see KDF for associated data   |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Poly1305 MAC (16 bytes)        +
  |                                       |
  +----+----+----+----+----+----+----+----+


```
البيانات غير المشفرة (علامة المصادقة Poly1305 غير معروضة):

```
  +----+----+----+----+----+----+----+----+
  |      Destination Connection ID        |
  +----+----+----+----+----+----+----+----+
  |   Packet Number   |type| ver| id |flag|
  +----+----+----+----+----+----+----+----+
  |        Source Connection ID           |
  +----+----+----+----+----+----+----+----+
  |                 Token                 |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |      see below for allowed blocks     |
  +----+----+----+----+----+----+----+----+
```
الأحجام، غير شاملة لحمولة IP الإضافية:

| النوع | رمز النوع | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | pl len |
|------|-----------|-------|-----------|---------------|---------------|-----------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 864+pl | 800+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1184+pl | 1118+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | غير متوفر | كبير جداً | | | | |
ملاحظة: رموز الأنواع للاستخدام الداخلي فقط. ستبقى الموجهات من النوع 4، وسيتم الإشارة إلى الدعم في عناوين الموجه.

الحد الأدنى لـ MTU لـ MLKEM768_X25519: حوالي 1316 لـ IPv4 و 1336 لـ IPv6.

#### SessionConfirmed (النوع 2)

غير متغير

#### KDF لمرحلة البيانات

غير متغير

#### اختبار التتابع والأقران

الكتل التالية تحتوي على حقول الإصدار. ستبقى الإصدار 2 (للتوافق مع Bob غير PQ)، ولن تتغير إلى الإصدار 3/4 لـ PQ.

- طلب الترحيل
- استجابة الترحيل
- تقديم الترحيل
- اختبار النظير

توقيعات PQ: تحتوي كتل Relay وكتل Peer Test ورسائل Peer Test جميعها على توقيعات. لسوء الحظ، توقيعات PQ أكبر من MTU. لا توجد آلية حالية لتجزئة كتل Relay أو Peer Test أو الرسائل عبر حزم UDP متعددة. يجب توسيع البروتوكول لدعم التجزئة. سيتم ذلك في اقتراح منفصل سيتم تحديده لاحقاً. حتى اكتمال ذلك، لن يتم دعم Relay و Peer Test.

#### العناوين المنشورة

في جميع الحالات، استخدم اسم نقل SSU2 كالمعتاد. MLKEM-1024 غير مدعوم.

استخدم نفس العنوان/المنفذ كما في الحالة غير-PQ، غير المحجوبة بجدار الحماية. يتم دعم أحد أو كلا متغيري PQ. في عنوان الـ router، انشر v=2 (كالمعتاد) والمعامل الجديد pq=[3|4|3,4] للإشارة إلى MLKEM 512/768/كلاهما. الـ routers الأقدم ستتجاهل معامل pq وتتصل بشكل غير-pq كالمعتاد.

عنوان/منفذ مختلف كغير-PQ، أو PQ فقط، غير محجوب بجدار حماية غير مدعوم. لن يتم تنفيذ هذا حتى يتم تعطيل SSU2 غير-PQ، بعد عدة سنوات من الآن. عندما يتم تعطيل غير-PQ، يتم دعم واحد أو كلا من متغيرات PQ. في عنوان الـ router، انشر v=[3|4|3,4] للإشارة إلى MLKEM 512/768/كلاهما. الـ routers الأقدم ستتحقق من معامل v وتتخطى هذا العنوان باعتباره غير مدعوم.

العناوين المحجوبة بجدار الحماية (لم يتم نشر عنوان IP): في عنوان الموجه، قم بنشر v=2 (كالمعتاد). يجب نشر معامل pq في العناوين المحجوبة بجدار الحماية، لدعم التمرير.

قد تتصل Alice بـ PQ Bob باستخدام متغير PQ الذي ينشره Bob، سواء كانت Alice تعلن عن دعم pq في معلومات router الخاصة بها أم لا، أو ما إذا كانت تعلن عن نفس المتغير.

#### MTU

احرص على عدم تجاوز MTU مع MLKEM768. الحد الأدنى لـ MTU في SSU2 هو 1280، وهو حجم الرسالة 1 بدون حشو. لا تضع حشواً في الرسالة 1 إذا كان MTU الخاص بـ Alice أو Bob هو 1280.

#### المشاكل

يمكننا استخدام حقل الإصدار داخلياً واستخدام 3 لـ MLKEM512 و 4 لـ MLKEM768.

بالنسبة للرسائل 1 و 2، سيؤدي MLKEM768 إلى زيادة أحجام الحزم إلى ما يتجاوز الحد الأدنى للـ MTU البالغ 1280. من المحتمل أننا لن ندعمه لذلك الاتصال إذا كان الـ MTU منخفضًا جدًا.

بالنسبة للرسائل 1 و 2، سيؤدي MLKEM1024 إلى زيادة أحجام الحزم إلى ما يتجاوز الحد الأقصى لـ MTU البالغ 1500. هذا سيتطلب تجزئة الرسائل 1 و 2، وسيكون تعقيداً كبيراً. من المحتمل أننا لن نقوم بذلك.

Relay وPeer Test: انظر أعلاه

### البث المباشر

TODO: هل يوجد طريقة أكثر كفاءة لتعريف التوقيع/التحقق لتجنب نسخ التوقيع؟

### ملفات SU3

قائمة المهام

يمنع القسم 8.1 من [مسودة IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) استخدام HashML-DSA في شهادات X.509 ولا يخصص معرفات كائنات (OIDs) لـ HashML-DSA، وذلك بسبب تعقيدات التنفيذ وانخفاض الأمان.

بالنسبة لتوقيعات PQ فقط لملفات SU3، استخدم معرفات الكائن (OIDs) المحددة في [مسودة IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) للمتغيرات غير المُجمَّعة مسبقاً للشهادات. نحن لا نحدد التوقيعات المختلطة لملفات SU3، لأنه قد يتوجب علينا إجراء hash للملفات مرتين (على الرغم من أن HashML-DSA و X2559 يستخدمان نفس دالة الـ hash وهي SHA512). أيضاً، ربط مفتاحين وتوقيعين في شهادة X.509 سيكون غير معياري تماماً.

لاحظ أننا نمنع توقيع Ed25519 لملفات SU3، وبينما قمنا بتعريف توقيع Ed25519ph، لم نتفق أبداً على OID له، أو نستخدمه.

أنواع التوقيع العادية غير مسموحة لملفات SU3؛ استخدم متغيرات ph (prehash).

### مواصفات أخرى

سيكون الحد الأقصى الجديد لحجم الوجهة 2599 (3468 في base 64).

تحديث الوثائق الأخرى التي تقدم إرشادات حول أحجام الوجهات، بما في ذلك:

- SAMv3
- Bittorrent
- إرشادات المطورين
- التسمية / دفتر العناوين / خوادم القفز
- مستندات أخرى

## تحليل النفقات العامة

### تبادل المفاتيح

زيادة الحجم (بايت):

| النوع | Pubkey (Msg 1) | Cipertext (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
السرعة:

السرعات كما ذكرها [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| النوع | السرعة النسبية |
|------|----------------|
| X25519 DH/keygen | خط الأساس |
| MLKEM512 | أسرع بـ 2.25 مرة |
| MLKEM768 | أسرع بـ 1.5 مرة |
| MLKEM1024 | 1x (نفس السرعة) |
| XK | 4x DH (keygen + 3 DH) |
| MLKEM512_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 4.9x DH = أبطأ بـ 22% |
| MLKEM768_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 5.3x DH = أبطأ بـ 32% |
| MLKEM1024_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 6x DH = أبطأ بـ 50% |
نتائج الاختبارات الأولية في Java:

| النوع | DH/encaps النسبي | DH/decaps | keygen |
|------|-------------------|-----------|--------|
| X25519 | خط الأساس | خط الأساس | خط الأساس |
| MLKEM512 | أسرع بـ29 مرة | أسرع بـ22 مرة | أسرع بـ17 مرة |
| MLKEM768 | أسرع بـ17 مرة | أسرع بـ14 مرة | أسرع بـ9 مرات |
| MLKEM1024 | أسرع بـ12 مرة | أسرع بـ10 مرات | أسرع بـ6 مرات |
### التوقيعات

الحجم:

أحجام المفاتيح والتوقيعات والهوية وجهة الوجهة النموذجية أو الزيادات في الحجم (تم تضمين Ed25519 للمرجع) بافتراض نوع التشفير X25519 لـ RIs. الحجم المضاف لـ Router Info وLeaseSet والرسائل القابلة للرد وكل من حزمتي البث (SYN و SYN ACK) المدرجتين. تحتوي الوجهات وLeasesets الحالية على حشو متكرر وقابلة للضغط أثناء النقل. الأنواع الجديدة لا تحتوي على حشو ولن تكون قابلة للضغط، مما يؤدي إلى زيادة أكبر بكثير في الحجم أثناء النقل. انظر قسم التصميم أعلاه.

| النوع | Pubkey | Sig | Key+Sig | RIdent | Dest | RInfo | LS/Streaming/Datagram (كل رسالة) |
|------|--------|-----|---------|--------|------|-------|----------------------------------|
| EdDSA_SHA512_Ed25519 | 32 | 64 | 96 | 391 | 391 | أساسي | أساسي |
| MLDSA44 | 1312 | 2420 | 3732 | 1351 | 1319 | +3316 | +3284 |
| MLDSA65 | 1952 | 3309 | 5261 | 1991 | 1959 | +5668 | +5636 |
| MLDSA87 | 2592 | 4627 | 7219 | 2631 | 2599 | +7072 | +7040 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 2484 | 3828 | 1383 | 1351 | +3412 | +3380 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 3373 | 5357 | 2023 | 1991 | +5668 | +5636 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 4691 | 7315 | 2663 | 2631 | +7488 | +7456 |
السرعة:

السرعات كما ذكرتها [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| النوع | علامة السرعة النسبية | التحقق |
|------|---------------------|--------|
| EdDSA_SHA512_Ed25519 | خط الأساس | خط الأساس |
| MLDSA44 | أبطأ 5 مرات | أسرع مرتين |
| MLDSA65 | ??? | ??? |
| MLDSA87 | ??? | ??? |
نتائج الاختبارات الأولية في Java:

| النوع | علامة السرعة النسبية | التحقق | توليد المفتاح |
|------|---------------------|--------|--------|
| EdDSA_SHA512_Ed25519 | خط الأساس | خط الأساس | خط الأساس |
| MLDSA44 | أبطأ بـ 4.6 مرة | أسرع بـ 1.7 مرة | أسرع بـ 2.6 مرة |
| MLDSA65 | أبطأ بـ 8.1 مرة | نفس السرعة | أسرع بـ 1.5 مرة |
| MLDSA87 | أبطأ بـ 11.1 مرة | أبطأ بـ 1.5 مرة | نفس السرعة |
## تحليل الأمان

تم تلخيص فئات أمان NIST في [عرض NIST](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) الشريحة 10. المعايير الأولية: يجب أن تكون الحد الأدنى لفئة أمان NIST هو 2 للبروتوكولات المختلطة و 3 لـ PQ فقط.

| الفئة | آمنة مثل |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### المصافحات

هذه جميعها بروتوكولات مختلطة. يجب على التطبيقات تفضيل MLKEM768؛ MLKEM512 ليس آمناً بما فيه الكفاية.

فئات أمان NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| الخوارزمية | فئة الأمان |
|-----------|-------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
### التوقيعات

يحدد هذا الاقتراح أنواع التوقيع المختلطة والكمية البحتة. MLDSA44 المختلط مُفضل على MLDSA65 الكمي البحت. أحجام المفاتيح والتوقيعات لـ MLDSA65 و MLDSA87 كبيرة جداً بالنسبة لنا، على الأقل في البداية.

فئات الأمان NIST [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf):

| الخوارزمية | فئة الأمان |
|-----------|-------------------|
| MLDSA44 | 2 |
| MLKEM67 | 3 |
| MLKEM87 | 5 |
## تفضيلات النوع

بينما سنحدد وننفذ 3 أنواع تشفير و 9 أنواع توقيع، نخطط لقياس الأداء أثناء التطوير، وتحليل تأثيرات زيادة أحجام الهياكل بشكل أعمق. سنواصل أيضاً البحث ومراقبة التطورات في المشاريع والبروتوكولات الأخرى.

بعد سنة أو أكثر من التطوير سنحاول الاستقرار على نوع مفضل أو افتراضي لكل حالة استخدام. سيتطلب الاختيار المقايضة بين عرض النطاق الترددي ووحدة المعالجة المركزية ومستوى الأمان المقدر. قد لا تكون جميع الأنواع مناسبة أو مسموحة لجميع حالات الاستخدام.

التفضيلات الأولية كما يلي، وهي قابلة للتغيير:

التشفير: MLKEM768_X25519

التوقيعات: MLDSA44_EdDSA_SHA512_Ed25519

القيود الأولية هي كما يلي، وهي قابلة للتغيير:

التشفير: MLKEM1024_X25519 غير مسموح لـ SSU2

التوقيعات: MLDSA87 والمتغير الهجين كبير جداً على الأرجح؛ MLDSA65 والمتغير الهجين قد يكون كبيراً جداً

## ملاحظات التنفيذ

### دعم المكتبة

مكتبات Bouncycastle و BoringSSL و WolfSSL تدعم الآن MLKEM و MLDSA. دعم OpenSSL سيكون في إصدارهم 3.5 في 8 أبريل 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

مكتبة Noise الخاصة بموقع southernstorm.com والمُكيّفة بواسطة Java I2P كانت تحتوي على دعم أولي للمصافحات الهجينة، ولكننا قمنا بإزالته لعدم الاستخدام؛ سنحتاج إلى إضافته مرة أخرى وتحديثه ليتطابق مع [مواصفات Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf).

### متغيرات التوقيع

سنستخدم المتغير "المحوط" أو العشوائي للتوقيع، وليس المتغير "الحتمي"، كما هو محدد في [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) القسم 3.4. هذا يضمن أن كل توقيع مختلف، حتى عند التوقيع على نفس البيانات، ويوفر حماية إضافية ضد هجمات القنوات الجانبية. بينما يحدد [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) أن المتغير "المحوط" هو الافتراضي، قد يكون هذا صحيحاً أو غير صحيح في مكتبات مختلفة. يجب على المطورين التأكد من استخدام المتغير "المحوط" للتوقيع.

نحن نستخدم عملية التوقيع العادية (تُسمى Pure ML-DSA Signature Generation) والتي تشفر الرسالة داخلياً كـ 0x00 || len(ctx) || ctx || message، حيث ctx هو قيمة اختيارية بحجم 0x00..0xFF. نحن لا نستخدم أي سياق اختياري. len(ctx) == 0. هذه العملية محددة في [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) Algorithm 2 step 10 و Algorithm 3 step 5. لاحظ أن بعض متجهات الاختبار المنشورة قد تتطلب تعيين وضع لا يتم فيه ترميز الرسالة.

### الموثوقية

زيادة الحجم ستؤدي إلى تجزئة أكبر بكثير للـ tunnel في مخازن NetDB، ومصافحات التدفق، والرسائل الأخرى. تحقق من تغييرات الأداء والموثوقية.

### أحجام الهياكل

ابحث وتحقق من أي كود يحدد حجم البايت لمعلومات router ومجموعات leaseSet.

### NetDB

مراجعة وربما تقليل الحد الأقصى لـ LS/RI المخزنة في ذاكرة الوصول العشوائي أو على القرص، لتحديد زيادة التخزين. زيادة الحد الأدنى لمتطلبات النطاق الترددي لـ floodfills؟

### Ratchet

#### الأنفاق المشتركة

يجب أن يكون التصنيف/الكشف التلقائي لبروتوكولات متعددة على نفس tunnels ممكناً بناءً على فحص طول الرسالة 1 (رسالة الجلسة الجديدة). باستخدام MLKEM512_X25519 كمثال، طول الرسالة 1 أكبر بـ 816 بايت من بروتوكول ratchet الحالي، والحد الأدنى لحجم الرسالة 1 (مع تضمين حمولة DateTime فقط) هو 919 بايت. معظم أحجام الرسالة 1 مع ratchet الحالي تحتوي على حمولة أقل من 816 بايت، لذا يمكن تصنيفها كـ non-hybrid ratchet. الرسائل الكبيرة على الأرجح هي POSTs وهي نادرة.

إذن الاستراتيجية الموصى بها هي:

- إذا كانت الرسالة 1 أقل من 919 بايت، فهي بروتوكول ratchet الحالي.
- إذا كانت الرسالة 1 أكبر من أو تساوي 919 بايت، فهي على الأرجح MLKEM512_X25519.
  جرب MLKEM512_X25519 أولاً، وإذا فشل، جرب بروتوكول ratchet الحالي.

هذا يجب أن يسمح لنا بدعم standard ratchet و hybrid ratchet بكفاءة على نفس الوجهة، تماماً كما دعمنا سابقاً ElGamal و ratchet على نفس الوجهة. لذلك، يمكننا الانتقال إلى بروتوكول MLKEM المختلط بسرعة أكبر مما لو لم نتمكن من دعم البروتوكولات المزدوجة لنفس الوجهة، لأننا نستطيع إضافة دعم MLKEM للوجهات الموجودة.

التركيبات المدعومة المطلوبة هي:

- X25519 + MLKEM512
- X25519 + MLKEM768
- X25519 + MLKEM1024

التركيبات التالية قد تكون معقدة، وليس مطلوباً دعمها، ولكن قد تكون مدعومة، حسب التنفيذ:

- أكثر من MLKEM واحد
- ElG + واحد أو أكثر من MLKEM
- X25519 + واحد أو أكثر من MLKEM
- ElG + X25519 + واحد أو أكثر من MLKEM

قد لا نحاول دعم خوارزميات MLKEM متعددة (على سبيل المثال، MLKEM512_X25519 و MLKEM_768_X25519) على نفس الوجهة. اختر واحدة فقط؛ ومع ذلك، هذا يعتمد على اختيارنا لمتغير MLKEM المفضل، بحيث يمكن لأنفاق عميل HTTP استخدام واحد منها. يعتمد على التنفيذ.

قد نحاول دعم ثلاث خوارزميات (على سبيل المثال X25519، MLKEM512_X25519، و MLKEM769_X25519) على نفس الوجهة. قد تكون استراتيجية التصنيف وإعادة المحاولة معقدة جداً. قد تكون التكوين وواجهة المستخدم للتكوين معقدة جداً. يعتمد على التنفيذ.

من المحتمل ألا نحاول دعم خوارزميات ElGamal والهجينة على نفس الوجهة. ElGamal عفا عليه الزمن، وElGamal + هجين فقط (بدون X25519) لا يبدو منطقياً. أيضاً، رسائل الجلسة الجديدة لـ ElGamal والهجينة كبيرة الحجم، لذا ستحتاج استراتيجيات التصنيف غالباً لمحاولة كلا التشفيرين، مما سيكون غير فعال. يعتمد على التنفيذ.

يمكن للعملاء استخدام نفس مفاتيح X25519 الثابتة أو مفاتيح مختلفة لبروتوكولي X25519 والهجين على نفس الأنفاق، وهذا يعتمد على التنفيذ.

#### السرية الأمامية

مواصفة ECIES تسمح برسائل Garlic في حمولة New Session Message، مما يتيح تسليم 0-RTT للحزمة الأولى للتدفق، عادة HTTP GET، مع leaseset الخاص بالعميل. ومع ذلك، حمولة New Session Message لا تتمتع بالسرية الأمامية. نظراً لأن هذا الاقتراح يؤكد على تعزيز السرية الأمامية لـ ratchet، قد تؤجل التطبيقات أو يجب أن تؤجل تضمين حمولة التدفق، أو رسالة التدفق الكاملة، حتى أول Existing Session Message. هذا سيكون على حساب تسليم 0-RTT. قد تعتمد الاستراتيجيات أيضاً على نوع الحركة أو نوع tunnel، أو على GET مقابل POST، على سبيل المثال. يعتمد على التطبيق.

#### حجم الجلسة الجديدة

MLKEM أو MLDSA أو كليهما على نفس الوجهة، سيزيد بشكل كبير من حجم رسالة الجلسة الجديدة، كما هو موضح أعلاه. قد يقلل هذا بشكل كبير من موثوقية تسليم رسالة الجلسة الجديدة عبر الأنفاق (tunnels)، حيث يجب تقسيمها إلى عدة رسائل نفق بحجم 1024 بايت. نجاح التسليم يتناسب مع العدد الأسي للأجزاء. قد تستخدم التطبيقات استراتيجيات مختلفة لتحديد حجم الرسالة، على حساب تسليم 0-RTT. يعتمد على التطبيق.

### NTCP2

نحن نضع البت الأعلى (MSB) للمفتاح المؤقت (key[31] & 0x80) في طلب الجلسة للإشارة إلى أن هذا اتصال مختلط. هذا يسمح لنا بتشغيل كل من NTCP القياسي وNTCP المختلط على نفس المنفذ. يتم دعم متغير مختلط واحد فقط، ويتم الإعلان عنه في عنوان router. على سبيل المثال، v=2,3 أو v=2,4 أو v=2,5.

#### إخفاء الهوية

كأليس، لاتصال PQ، قبل التشويش، اضبط X[31] |= 0x80. هذا يجعل X مفتاحًا عامًا غير صالح لـ X25519. بعد التشويش، سيعمل AES-CBC على جعله عشوائيًا. ستكون البتة الأكثر أهمية (MSB) لـ X عشوائية بعد التشويش.

كـ Bob، اختبر إذا كان (X[31] & 0x80) != 0 بعد إلغاء التشويش. إذا كان كذلك، فهو اتصال PQ.

الحد الأدنى لإصدار router المطلوب لـ NTCP2-PQ لم يتم تحديده بعد.

ملاحظة: رموز الأنواع للاستخدام الداخلي فقط. ستبقى أجهزة router من النوع 4، وسيتم الإشارة إلى الدعم في عناوين router.

### SSU2

نستخدم حقل الإصدار في الرأس الطويل ونقوم بتعيينه إلى 3 لـ MLKEM512 و 4 لـ MLKEM768. v=2,3,4 في العنوان سيكون كافياً.

تحقق وتأكد من أن SSU2 يمكنه التعامل مع RI الموقع بـ MLDSA والمجزأ عبر حزم متعددة (6-8؟).

ملاحظة: رموز النوع مخصصة للاستخدام الداخلي فقط. ستبقى الـ routers من النوع 4، وسيتم الإشارة إلى الدعم في عناوين الـ router.

## توافق Router

### أسماء النقل

في جميع الحالات، استخدم أسماء النقل NTCP2 و SSU2 كما هو معتاد.

### أنواع تشفير Router

لدينا عدة بدائل للنظر فيها:

#### أجهزة router من النوع 5/6/7

غير مُوصى به. استخدم فقط وسائل النقل الجديدة المذكورة أعلاه التي تتطابق مع نوع الـ router. الـ routers الأقدم لا يمكنها الاتصال أو بناء tunnels من خلالها أو إرسال رسائل netDb إليها. قد يتطلب عدة دورات إصدار لتصحيح الأخطاء وضمان الدعم قبل التفعيل افتراضياً. قد يؤدي إلى تمديد فترة الطرح بسنة أو أكثر مقارنة بالبدائل أدناه.

#### روترات النوع 4

موصى به. حيث أن PQ لا يؤثر على المفتاح الثابت X25519 أو بروتوكولات المصافحة N، يمكننا ترك أجهزة router كنوع 4، والإعلان فقط عن وسائل النقل الجديدة. يمكن لأجهزة router الأقدم أن تتصل وتبني الأنفاق من خلالها أو ترسل رسائل netDb إليها.

#### التوصيات

MLKEM-768 مُوصى به لـ Ratchet و NTCP2 و SSU2، كونه يوفر أفضل توازن بين الأمان وطول المفتاح.

### أنواع توقيع Router

#### Routers من النوع 12-17

أجهزة router الأقدم تتحقق من RIs ولذلك لا يمكنها الاتصال أو بناء أنفاق من خلالها أو إرسال رسائل netDb إليها. سيتطلب عدة دورات إصدار لتصحيح الأخطاء وضمان الدعم قبل التمكين افتراضياً. ستكون نفس المشاكل مثل طرح enc. type 5/6/7؛ قد يمدد الطرح لسنة أو أكثر مقارنة ببديل طرح type 4 enc. type المذكور أعلاه.

لا توجد بدائل.

### أنواع تشفير LS

#### مفاتيح LS من النوع 5-7

قد تكون هذه موجودة في LS مع مفاتيح X25519 من النوع 4 الأقدم. ستتجاهل أجهزة router الأقدم المفاتيح غير المعروفة.

يمكن للوجهات أن تدعم أنواع مفاتيح متعددة، ولكن فقط من خلال القيام بفك تشفير تجريبي للرسالة 1 باستخدام كل مفتاح. يمكن تقليل العبء الإضافي من خلال الاحتفاظ بعداد لعمليات فك التشفير الناجحة لكل مفتاح، ومحاولة استخدام المفتاح الأكثر استخداماً أولاً. يستخدم Java I2P هذه الاستراتيجية لـ ElGamal+X25519 على نفس الوجهة.

### أنواع توقيع الوجهة

#### النوع 12-17 Dests

تتحقق أجهزة router من توقيعات leaseSet ولذلك لا يمكنها الاتصال أو استقبال leaseSets لوجهات من النوع 12-17. سيتطلب الأمر عدة دورات إصدار لإصلاح الأخطاء وضمان الدعم قبل التمكين افتراضياً.

لا توجد بدائل.

## الأولويات والطرح

البيانات الأكثر قيمة هي حركة البيانات من طرف إلى طرف، المشفرة باستخدام ratchet. بصفتك مراقب خارجي بين قفزات tunnel، فهي مشفرة مرتين إضافيتين، مع تشفير tunnel وتشفير النقل. بصفتك مراقب خارجي بين OBEP و IBGW، فهي مشفرة مرة إضافية واحدة فقط، مع تشفير النقل. بصفتك مشارك OBEP أو IBGW، فإن ratchet هو التشفير الوحيد. ومع ذلك، نظراً لأن tunnels أحادية الاتجاه، فإن التقاط كلا الرسالتين في مصافحة ratchet سيتطلب تواطؤ routers، إلا إذا تم بناء tunnels مع OBEP و IBGW على نفس router.

نموذج التهديد الأكثر إثارة للقلق في الحوسبة الكمية حالياً هو تخزين حركة البيانات اليوم، لفك تشفيرها بعد سنوات عديدة من الآن (السرية الأمامية). النهج المختلط سيوفر الحماية ضد ذلك.

نموذج التهديد PQ لكسر مفاتيح المصادقة في فترة زمنية معقولة (لنقل بضعة أشهر) ثم انتحال هوية المصادقة أو فك التشفير في الوقت شبه الفعلي، هو أبعد بكثير؟ وهذا هو الوقت الذي سنريد فيه الانتقال إلى المفاتيح الثابتة PQC.

إذن، أقدم نموذج تهديد PQ هو قيام OBEP/IBGW بتخزين حركة البيانات لفك تشفيرها لاحقاً. يجب أن ننفذ hybrid ratchet أولاً.

Ratchet هو الأولوية القصوى. وسائل النقل تأتي بعد ذلك. التوقيعات هي الأولوية الأدنى.

سيكون طرح التوقيع أيضاً متأخراً سنة أو أكثر عن طرح التشفير، لأن التوافق العكسي غير ممكن. كما أن اعتماد MLDSA في الصناعة سيتم توحيده من قبل منتدى CA/Browser ومؤسسات إصدار الشهادات. تحتاج مؤسسات إصدار الشهادات أولاً إلى دعم وحدة الأمان الأجهزة (HSM)، والذي غير متوفر حالياً [CA/Browser Forum](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/). نتوقع أن يقود منتدى CA/Browser القرارات حول اختيارات المعاملات المحددة، بما في ذلك ما إذا كان سيتم دعم أو طلب التوقيعات المركبة [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

| المعلم | الهدف |
|-----------|--------|
| Ratchet beta | أواخر 2025 |
| اختيار أفضل نوع تشفير | أوائل 2026 |
| NTCP2 beta | أوائل 2026 |
| SSU2 beta | منتصف 2026 |
| Ratchet production | منتصف 2026 |
| Ratchet default | أواخر 2026 |
| Signature beta | أواخر 2026 |
| NTCP2 production | أواخر 2026 |
| SSU2 production | أوائل 2027 |
| اختيار أفضل نوع توقيع | أوائل 2027 |
| NTCP2 default | أوائل 2027 |
| SSU2 default | منتصف 2027 |
| Signature production | منتصف 2027 |
## الترحيل

إذا لم نتمكن من دعم بروتوكولات ratchet القديمة والجديدة على نفس الأنفاق، فإن الترحيل سيكون أصعب بكثير.

يجب أن نكون قادرين على تجربة واحد تلو الآخر، كما فعلنا مع X25519، لإثبات ذلك.

## المشاكل

- اختيار Noise Hash - البقاء مع SHA256 أم الترقية؟
  SHA256 يجب أن يكون جيداً لـ 20-30 سنة أخرى، غير مهدد بـ PQ،
  انظر [عرض NIST](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf) و [عرض NCCOE](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf).
  إذا تم كسر SHA256 فلدينا مشاكل أسوأ (netdb).
- NTCP2 منفذ منفصل، عنوان router منفصل
- SSU2 ترحيل / اختبار النظير
- حقل إصدار SSU2
- إصدار عنوان router في SSU2

## المراجع

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)

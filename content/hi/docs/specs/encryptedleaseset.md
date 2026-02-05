---
title: "एन्क्रिप्टेड LeaseSet विनिर्देश"
description: "Encrypted leasesets का blinding, encryption, और decryption"
slug: "encryptedleaseset"
category: "प्रोटोकॉल"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## अवलोकन

यह दस्तावेज़ encrypted leasesets की blinding, encryption, और decryption को निर्दिष्ट करता है। encrypted leaseset की संरचना के लिए, [सामान्य संरचना विनिर्देश](/docs/specs/common-structures) देखें। encrypted leasesets पर पृष्ठभूमि के लिए, [प्रस्ताव 123](/proposals/123-new-netdb-entries) देखें। netDb में उपयोग के लिए, netdb दस्तावेज़ देखें।

### परिभाषाएं

हम encrypted LS2 के लिए उपयोग किए जाने वाले क्रिप्टोग्राफिक बिल्डिंग ब्लॉक्स के अनुरूप निम्नलिखित functions को परिभाषित करते हैं:

**CSRNG(n)** : क्रिप्टोग्राफिकली-सुरक्षित रैंडम नंबर जेनरेटर से n-byte आउटपुट।

CSRNG के cryptographically-secure होने की आवश्यकता के अतिरिक्त (और इस प्रकार key material उत्पन्न करने के लिए उपयुक्त), यह n-byte output के लिए सुरक्षित होना चाहिए जब इससे तुरंत पहले और बाद के byte sequences network पर exposed हों (जैसे कि salt में, या encrypted padding में)। जो implementations संभावित रूप से अविश्वसनीय source पर निर्भर करती हैं, उन्हें किसी भी output को hash करना चाहिए जो network पर exposed होना है [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html)।

**H(p, d)** : SHA-256 hash function जो एक personalization string p और data d लेता है, और 32 bytes की लंबाई का output उत्पन्न करता है।

SHA-256 का उपयोग निम्नलिखित तरीके से करें:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : ChaCha20 stream cipher जैसा कि [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4) में निर्दिष्ट है, प्रारंभिक काउंटर को 1 पर सेट करके। S_KEY_LEN = 32 और S_IV_LEN = 12।

- **ENCRYPT(k, iv, plaintext)** : cipher key k और nonce iv का उपयोग करके plaintext को encrypt करता है, जो key k के लिए अद्वितीय (unique) होना चाहिए। एक ciphertext return करता है जो plaintext के समान आकार का होता है। यदि key गुप्त है तो पूरा ciphertext random से अप्रभेद्य होना चाहिए।

- **DECRYPT(k, iv, ciphertext)** : cipher key k और nonce iv का उपयोग करके ciphertext को decrypt करता है। plaintext वापस करता है।

**SIG** : Red25519 signature scheme (SigType 11 के अनुरूप) key blinding के साथ। इसमें निम्नलिखित functions हैं:

- **DERIVE_PUBLIC(privkey)** : दिए गए private key के अनुरूप public key वापस करता है।

- **SIGN(privkey, m)** : दिए गए संदेश m पर निजी कुंजी privkey द्वारा एक हस्ताक्षर लौटाता है।

- **VERIFY(pubkey, m, sig)** : signature sig को public key pubkey और message m के विरुद्ध सत्यापित करता है। यदि signature वैध है तो true रिटर्न करता है, अन्यथा false।

इसे निम्नलिखित key blinding operations का भी समर्थन करना चाहिए:

- **GENERATE_ALPHA(data, secret)** : उन लोगों के लिए alpha generate करें जो data और एक वैकल्पिक secret को जानते हैं। परिणाम private keys के समान रूप से distributed होना चाहिए।

- **BLIND_PRIVKEY(privkey, alpha)** : एक गुप्त alpha का उपयोग करके एक private key को blind करता है।

- **BLIND_PUBKEY(pubkey, alpha)** : एक गुप्त alpha का उपयोग करके एक सार्वजनिक कुंजी को अंधा करता है। दिए गए keypair (privkey, pubkey) के लिए निम्नलिखित संबंध स्थापित होता है:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : X25519 public key agreement system. Private keys 32 बाइट्स के, public keys 32 बाइट्स के, 32 बाइट्स का आउटपुट उत्पन्न करता है। इसमें निम्नलिखित functions हैं:

- **GENERATE_PRIVATE()** : एक नई private key उत्पन्न करता है।

- **DERIVE_PUBLIC(privkey)** : दी गई private key के अनुरूप public key को वापस करता है।

- **DH(privkey, pubkey)** : दिए गए private और public keys से एक shared secret उत्पन्न करता है।

**HKDF(salt, ikm, info, n)** : एक क्रिप्टोग्राफिक key derivation function जो कुछ input key material ikm (जिसमें अच्छी entropy होनी चाहिए लेकिन uniformly random string होना आवश्यक नहीं), 32 bytes लंबाई का एक salt, और एक context-specific 'info' value लेती है, और n bytes का output उत्पन्न करती है जो key material के रूप में उपयोग के लिए उपयुक्त होता है।

[RFC-5869](https://tools.ietf.org/html/rfc5869) में निर्दिष्ट HKDF का उपयोग करें, [RFC-2104](https://tools.ietf.org/html/rfc2104) में निर्दिष्ट HMAC hash function SHA-256 का उपयोग करते हुए। इसका मतलब है कि SALT_LEN अधिकतम 32 bytes है।

### प्रारूप

एन्क्रिप्टेड LS2 प्रारूप तीन नेस्टेड परतों से मिलकर बना है:

- एक बाहरी परत जिसमें भंडारण और पुनर्प्राप्ति के लिए आवश्यक plaintext जानकारी होती है।
- एक मध्य परत जो client प्रमाणीकरण को संभालती है।
- एक आंतरिक परत जिसमें वास्तविक LS2 डेटा होता है।

समग्र प्रारूप इस तरह दिखता है:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
ध्यान दें कि encrypted LS2 blinded है। Destination header में नहीं है। DHT storage location SHA-256(sig type || blinded public key) है, और दैनिक रूप से rotate होता है।

ऊपर निर्दिष्ट मानक LS2 header का उपयोग नहीं करता है।

#### लेयर 0 (बाहरी)

**Type** : 1 byte

वास्तव में header में नहीं है, लेकिन signature द्वारा कवर किए गए data का हिस्सा है। Database Store Message में field से लें।

**Blinded Public Key Sig Type** : 2 बाइट्स, big endian

यह हमेशा type 11 होगा, जो एक Red25519 blinded key की पहचान करता है।

**Blinded Public Key** : लंबाई sig type द्वारा निहित

**प्रकाशित टाइमस्टैम्प** : 4 बाइट्स, big endian

युग (epoch) के बाद से सेकंड, 2106 में रोल ओवर हो जाता है

**Expires** : 2 bytes, big endian

प्रकाशित timestamp से सेकंड में offset, अधिकतम 18.2 घंटे

**Flags** : 2 bytes

बिट क्रम: 15 14 ... 3 2 1 0

- बिट 0: यदि 0 है, तो कोई offline keys नहीं; यदि 1 है, तो offline keys हैं
- अन्य bits: भविष्य के उपयोग के साथ संगतता के लिए 0 पर सेट करें

**Transient key data** : यदि flag offline keys को इंगित करता है तो मौजूद है

- **Expires timestamp** : 4 bytes, big endian। Epoch से सेकंड, 2106 में roll over हो जाता है
- **Transient sig type** : 2 bytes, big endian
- **Transient signing public key** : लंबाई sig type द्वारा निहित के अनुसार
- **Signature** : लंबाई blinded public key sig type द्वारा निहित के अनुसार। expires timestamp, transient sig type, और transient public key पर। blinded public key के साथ verified होता है।

**lenOuterCiphertext** : 2 बाइट्स, big endian

**outerCiphertext** : lenOuterCiphertext बाइट्स

एन्क्रिप्टेड लेयर 1 डेटा। key derivation और encryption algorithms के लिए नीचे देखें।

**Signature** : हस्ताक्षर कुंजी के sig type द्वारा निहित लंबाई के अनुसार

हस्ताक्षर ऊपर की सभी चीजों का है। यदि फ्लैग offline keys को दर्शाता है, तो हस्ताक्षर को transient public key के साथ सत्यापित किया जाता है। अन्यथा, हस्ताक्षर को blinded public key के साथ सत्यापित किया जाता है।

#### परत 1 (मध्य)

**फ्लैग्स** : 1 बाइट

बिट क्रम: 76543210

- Bit 0: सभी के लिए 0, per-client के लिए 1, auth section का पालन करना होगा
- Bits 3-1: Authentication scheme, केवल तभी जब bit 0 को per-client के लिए 1 पर सेट किया गया हो, अन्यथा 000
  - 000: DH client authentication (या कोई per-client authentication नहीं)
  - 001: PSK client authentication
- Bits 7-4: अप्रयुक्त, भविष्य की संगतता के लिए 0 पर सेट करें

**DH client auth data** : यदि flag bit 0 को 1 पर सेट किया गया है और flag bits 3-1 को 000 पर सेट किया गया है तो मौजूद होता है।

- **ephemeralPublicKey** : 32 bytes
- **clients** : 2 bytes, big endian। आगे आने वाली authClient entries की संख्या, प्रत्येक 40 bytes की
- **authClient** : एक single client के लिए Authorization डेटा। per-client authorization algorithm के लिए नीचे देखें।
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**PSK client auth data** : यदि flag bit 0 को 1 पर सेट किया गया है और flag bits 3-1 को 001 पर सेट किया गया है तो मौजूद होता है।

- **authSalt** : 32 bytes
- **clients** : 2 bytes, big endian. आने वाली authClient entries की संख्या, प्रत्येक 40 bytes का
- **authClient** : एक single client के लिए Authorization data। per-client authorization algorithm के लिए नीचे देखें।
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**innerCiphertext** : lenOuterCiphertext द्वारा निहित लंबाई (जो भी डेटा शेष है)

एन्क्रिप्टेड लेयर 2 डेटा। की डेरिवेशन और एन्क्रिप्शन एल्गोरिदम के लिए नीचे देखें।

#### लेयर 2 (आंतरिक)

**Type** : 1 byte

या तो 3 (LS2) या 7 (Meta LS2)

**Data** : दिए गए प्रकार के लिए LeaseSet2 डेटा।

हेडर और हस्ताक्षर शामिल है।

### ब्लाइंडिंग की डेरिवेशन

हम key blinding के लिए निम्नलिखित scheme का उपयोग करते हैं, जो Ed25519 और ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) पर आधारित है। Red25519 signatures Ed25519 curve पर हैं, जो hash के लिए SHA-512 का उपयोग करते हैं।

हम Tor के rend-spec-v3.txt appendix A.2 [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3) का उपयोग नहीं करते हैं, जिसके समान डिज़ाइन लक्ष्य हैं, क्योंकि इसकी blinded public keys prime-order subgroup से बाहर हो सकती हैं, जिसके अज्ञात सुरक्षा निहितार्थ हैं।

#### लक्ष्य

- अंधित न किए गए destination में signing public key Ed25519 (sig type 7) या Red25519 (sig type 11) होनी चाहिए; अन्य कोई sig types समर्थित नहीं हैं
- यदि signing public key ऑफलाइन है, तो transient signing public key भी Ed25519 होनी चाहिए
- Blinding कम्प्यूटेशनल रूप से सरल है
- मौजूदा cryptographic primitives का उपयोग करें
- Blinded public keys को unblind नहीं किया जा सकता
- Blinded public keys Ed25519 curve और prime-order subgroup पर होनी चाहिए
- Blinded public key प्राप्त करने के लिए destination की signing public key (पूरी destination आवश्यक नहीं) जानना आवश्यक है
- वैकल्पिक रूप से blinded public key प्राप्त करने के लिए अतिरिक्त secret की आवश्यकता हो सकती है

#### सुरक्षा

एक blinding scheme की सुरक्षा के लिए आवश्यक है कि alpha का वितरण unblinded private keys के समान हो। हालांकि, जब हम एक Ed25519 private key (sig type 7) को Red25519 private key (sig type 11) में blind करते हैं, तो वितरण अलग होता है। zcash section 4.1.6.1 [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) की आवश्यकताओं को पूरा करने के लिए, Red25519 (sig type 11) को unblinded keys के लिए भी उपयोग किया जाना चाहिए, ताकि "एक re-randomized public key और उस key के तहत signature(s) का संयोजन उस key को प्रकट न करे जिससे इसे re-randomize किया गया था।" हम मौजूदा destinations के लिए type 7 की अनुमति देते हैं, लेकिन नए destinations के लिए type 11 की सिफारिश करते हैं जो encrypted होंगे।

#### परिभाषाएं

**B** : Ed25519 आधार बिंदु (जनरेटर) 2^255 - 19 जैसा कि [ED25519-REFS](http://cr.yp.to/papers.html#ed25519) में है

**L** : Ed25519 order 2^252 + 27742317777372353535851937790883648493 जैसा कि [ED25519-REFS](http://cr.yp.to/papers.html#ed25519) में है

**DERIVE_PUBLIC(a)** : एक private key को public में convert करना, जैसे Ed25519 में (G से multiply करना)

**alpha** : एक 32-बाइट यादृच्छिक संख्या जो उन लोगों को ज्ञात है जो गंतव्य को जानते हैं।

**GENERATE_ALPHA(destination, date, secret)** : वर्तमान तारीख के लिए alpha उत्पन्न करें, उनके लिए जो destination और secret जानते हैं। परिणाम Ed25519 private keys के समान रूप से वितरित होना चाहिए।

**a** : destination को sign करने के लिए उपयोग की जाने वाली unblinded 32-byte EdDSA या RedDSA signing private key

**A** : destination में unblinded 32-byte EdDSA या RedDSA signing public key, = DERIVE_PUBLIC(a), जैसा कि Ed25519 में होता है

**a'** : एन्क्रिप्टेड leaseset पर हस्ताक्षर करने के लिए उपयोग की जाने वाली ब्लाइंडेड 32-बाइट EdDSA साइनिंग प्राइवेट की। यह एक वैध EdDSA प्राइवेट की है।

**A'** : Destination में blinded 32-byte EdDSA signing public key, जो DERIVE_PUBLIC(a') के साथ generate की जा सकती है, या A और alpha से। यह एक valid EdDSA public key है, curve पर और prime-order subgroup पर।

**LEOS2IP(x)** : इनपुट बाइट्स के क्रम को little-endian में बदलें

**H\*(x)** : 32 bytes = (LEOS2IP(SHA512(x))) mod B, Ed25519 hash-and-reduce के समान

#### ब्लाइंडिंग गणना

एक नई गुप्त alpha और blinded keys प्रत्येक दिन (UTC) उत्पन्न की जानी चाहिए।

गुप्त alpha और blinded keys की गणना निम्नलिखित प्रकार से की जाती है:

GENERATE_ALPHA(destination, date, secret), सभी पक्षों के लिए:

```
// secret is optional, else zero-length
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of blinded public key A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
datestring = 8 bytes ASCII YYYYMMDD from the current date UTC
secret = UTF-8 encoded string
seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
// treat seed as a 64 byte little-endian value
alpha = seed mod L
```
BLIND_PRIVKEY(), leaseSet प्रकाशित करने वाले स्वामी के लिए:

```
alpha = GENERATE_ALPHA(destination, date, secret)
// If for a Ed25519 private key (type 7)
seed = destination's signing private key
a = left half of SHA512(seed) and clamped as usual for Ed25519
// else for a Red25519 private key (type 11)
a = destination's signing private key
// Addition using scalar arithmetic
blinded signing private key = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
blinded signing public key = A' = DERIVE_PUBLIC(a')
```
BLIND_PUBKEY(), उन clients के लिए जो leaseset प्राप्त कर रहे हैं:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
A' की गणना की दोनों विधियां समान परिणाम देती हैं, जैसा कि आवश्यक है।

#### हस्ताक्षर

unblinded leaseset को unblinded Ed25519 या Red25519 signing private key द्वारा हस्ताक्षरित किया जाता है और सामान्य रूप से unblinded Ed25519 या Red25519 signing public key (sig types 7 या 11) के साथ सत्यापित किया जाता है।

यदि signing public key offline है, तो unblinded leaseset को unblinded transient Ed25519 या Red25519 signing private key द्वारा sign किया जाता है और unblinded Ed25519 या Red25519 transient signing public key (sig types 7 या 11) के साथ सामान्य रूप से verify किया जाता है। encrypted leasesets के लिए offline keys पर अतिरिक्त टिप्पणियों के लिए नीचे देखें।

एन्क्रिप्टेड leaseset के signing के लिए, हम Red25519 का उपयोग करते हैं जो RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) पर आधारित है, blinded keys के साथ sign और verify करने के लिए। Red25519 signatures Ed25519 curve पर होते हैं, hash के लिए SHA-512 का उपयोग करते हुए।

Red25519 मानक Ed25519 के समान है सिवाय नीचे निर्दिष्ट के अनुसार।

#### साइन/वेरिफाई गणनाएं

एन्क्रिप्टेड leaseset का बाहरी हिस्सा Red25519 keys और signatures का उपयोग करता है।

Red25519 Ed25519 के समान है। दो अंतर हैं:

Red25519 private keys यादृच्छिक संख्याओं से उत्पन्न की जाती हैं और फिर उन्हें mod L के साथ reduced करना होता है, जहाँ L ऊपर परिभाषित है। Ed25519 private keys यादृच्छिक संख्याओं से उत्पन्न की जाती हैं और फिर bytes 0 और 31 पर bitwise masking का उपयोग करके "clamped" की जाती हैं। यह Red25519 के लिए नहीं किया जाता। ऊपर परिभाषित GENERATE_ALPHA() और BLIND_PRIVKEY() फंक्शन mod L का उपयोग करके उचित Red25519 private keys उत्पन्न करते हैं।

Red25519 में, हस्ताक्षर के लिए r की गणना अतिरिक्त यादृच्छिक डेटा का उपयोग करती है, और निजी key के hash के बजाय सार्वजनिक key मान का उपयोग करती है। यादृच्छिक डेटा के कारण, हर Red25519 हस्ताक्षर अलग होता है, यहाँ तक कि जब समान key के साथ समान डेटा पर हस्ताक्षर कर रहे हों।

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### एन्क्रिप्शन और प्रोसेसिंग

#### उप-प्रमाणपत्रों की व्युत्पत्ति

blinding प्रक्रिया के हिस्से के रूप में, हमें यह सुनिश्चित करना होगा कि एक encrypted LS2 को केवल वही व्यक्ति decrypt कर सके जो संबंधित Destination की signing public key जानता हो। पूर्ण Destination की आवश्यकता नहीं है। इसे प्राप्त करने के लिए, हम signing public key से एक credential derive करते हैं:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
व्यक्तिगतकरण स्ट्रिंग यह सुनिश्चित करती है कि credential का किसी भी hash के साथ टकराव न हो जो DHT lookup key के रूप में उपयोग किया जाता है, जैसे कि plain Destination hash।

दिए गए blinded key के लिए, हम तब एक subcredential प्राप्त कर सकते हैं:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
Subcredential को नीचे दी गई key derivation प्रक्रियाओं में शामिल किया गया है, जो उन keys को Destination की signing public key के ज्ञान से बांधती है।

#### लेयर 1 एन्क्रिप्शन

सबसे पहले, key derivation प्रक्रिया के लिए इनपुट तैयार किया जाता है:

```
outerInput = subcredential || publishedTimestamp
```
अगला, एक यादृच्छिक salt उत्पन्न किया जाता है:

```
outerSalt = CSRNG(32)
```
फिर layer 1 को encrypt करने के लिए उपयोग की जाने वाली key को derive किया जाता है:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
अंत में, लेयर 1 प्लेनटेक्स्ट को एन्क्रिप्ट और सीरियलाइज़ किया जाता है:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### लेयर 1 डिक्रिप्शन

Salt को layer 1 ciphertext से parse किया जाता है:

```
outerSalt = outerCiphertext[0:31]
```
फिर layer 1 को encrypt करने के लिए उपयोग की जाने वाली key derive की जाती है:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
अंत में, layer 1 ciphertext को decrypt किया जाता है:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### लेयर 2 एन्क्रिप्शन

जब client authorization सक्षम होता है, तो `authCookie` की गणना नीचे वर्णित तरीके से की जाती है। जब client authorization अक्षम होता है, तो `authCookie` शून्य-लंबाई byte array होता है।

एन्क्रिप्शन लेयर 1 के समान तरीके से आगे बढ़ता है:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Layer 2 डिक्रिप्शन

जब client authorization सक्षम होता है, तो `authCookie` की गणना नीचे वर्णित तरीके से की जाती है। जब client authorization अक्षम होता है, तो `authCookie` शून्य-लंबाई का byte array होता है।

डिक्रिप्शन layer 1 के समान तरीके से आगे बढ़ता है:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### प्रति-क्लाइंट प्राधिकरण

जब किसी Destination के लिए client authorization सक्षम होता है, तो server उन clients की एक सूची बनाए रखता है जिन्हें वे encrypted LS2 data को decrypt करने के लिए authorize कर रहे हैं। प्रति-client संग्रहीत डेटा authorization mechanism पर निर्भर करता है, और इसमें कुछ रूप की key material शामिल होती है जो प्रत्येक client generate करता है और एक secure out-of-band mechanism के माध्यम से server को भेजता है।

प्रति-क्लाइंट प्राधिकरण को लागू करने के लिए दो विकल्प हैं:

#### DH क्लाइंट प्राधिकरण

प्रत्येक client एक DH keypair `[csk_i, cpk_i]` generate करता है, और public key `cpk_i` को server को भेजता है।

##### सर्वर प्रोसेसिंग

सर्वर एक नया `authCookie` और एक अस्थायी DH keypair जेनरेट करता है:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
फिर प्रत्येक अधिकृत क्लाइंट के लिए, सर्वर `authCookie` को उसकी public key से encrypt करता है:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
सर्वर प्रत्येक `[clientID_i, clientCookie_i]` tuple को encrypted LS2 की layer 1 में `epk` के साथ रखता है।

##### क्लाइंट प्रोसेसिंग

क्लाइंट अपनी private key का उपयोग करके अपना अपेक्षित client identifier `clientID_i`, encryption key `clientKey_i`, और encryption IV `clientIV_i` प्राप्त करता है:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
फिर client layer 1 authorization data में एक entry की खोज करता है जिसमें `clientID_i` होता है। यदि कोई मैचिंग entry मौजूद है, तो client इसे decrypt करके `authCookie` प्राप्त करता है:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### पूर्व-साझा कुंजी क्लाइंट प्राधिकरण

प्रत्येक client एक गुप्त 32-byte key `psk_i` generate करता है, और इसे server को भेजता है। वैकल्पिक रूप से, server गुप्त key generate कर सकता है, और इसे एक या अधिक clients को भेज सकता है।

##### सर्वर प्रोसेसिंग

सर्वर एक नया `authCookie` और salt उत्पन्न करता है:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
फिर प्रत्येक अधिकृत क्लाइंट के लिए, सर्वर `authCookie` को उसकी पूर्व-साझा की गई key से encrypt करता है:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
सर्वर प्रत्येक `[clientID_i, clientCookie_i]` tuple को encrypted LS2 की layer 1 में `authSalt` के साथ रखता है।

##### क्लाइंट प्रसंस्करण

क्लाइंट अपनी pre-shared key का उपयोग करके अपने अपेक्षित client identifier `clientID_i`, encryption key `clientKey_i`, और encryption IV `clientIV_i` को derive करता है:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
फिर client layer 1 authorization data में एक entry की खोज करता है जिसमें `clientID_i` हो। यदि कोई मैचिंग entry मौजूद है, तो client इसे decrypt करके `authCookie` प्राप्त करता है:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### सुरक्षा संबंधी विचार

उपरोक्त दोनों client authorization तंत्र client membership के लिए गोपनीयता प्रदान करते हैं। एक entity जो केवल Destination को जानती है, वह यह देख सकती है कि किसी भी समय कितने clients subscribed हैं, लेकिन यह track नहीं कर सकती कि कौन से clients को add या revoke किया जा रहा है।

जब भी servers एक encrypted LS2 generate करते हैं तो उन्हें clients के क्रम को randomize करना चाहिए, ताकि clients को अपनी list में स्थिति का पता न चले और वे यह अनुमान न लगा सकें कि कब अन्य clients को add या revoke किया गया है।

एक server चुन सकता है कि authorization data की सूची में random entries डालकर subscribe किए गए clients की संख्या को छुपाया जाए।

##### DH client authorization के फायदे

- स्कीम की सुरक्षा पूरी तरह से client key material के out-of-band exchange पर निर्भर नहीं है। client की private key को कभी भी उनके device को छोड़ने की आवश्यकता नहीं है, और इसलिए एक adversary जो out-of-band exchange को intercept करने में सक्षम है, लेकिन DH algorithm को तोड़ नहीं सकता, वह encrypted LS2 को decrypt नहीं कर सकता, या यह निर्धारित नहीं कर सकता कि client को कितने समय तक access दिया गया है।

##### DH client authorization के नुकसान

- N clients के लिए server side पर N + 1 DH operations की आवश्यकता होती है।
- Client side पर एक DH operation की आवश्यकता होती है।
- Client को secret key generate करने की आवश्यकता होती है।

##### PSK क्लाइंट प्राधिकरण के फायदे

- किसी DH operations की आवश्यकता नहीं है।
- सर्वर को secret key जेनरेट करने की अनुमति देता है।
- सर्वर को चाहने पर कई clients के साथ same key साझा करने की अनुमति देता है।

##### PSK क्लाइंट प्राधिकरण की कमियां

- स्कीम की सुरक्षा क्लाइंट key material के out-of-band एक्सचेंज पर गंभीर रूप से निर्भर है। एक प्रतिपक्षी जो किसी विशेष क्लाइंट के लिए एक्सचेंज को इंटरसेप्ट कर लेता है, वह उस क्लाइंट के लिए अधिकृत किसी भी बाद के encrypted LS2 को decrypt कर सकता है, साथ ही यह भी पता लगा सकता है कि क्लाइंट का एक्सेस कब रद्द किया गया है।

### Base 32 पतों के साथ एन्क्रिप्टेड LS

आप एक encrypted LS2 के लिए पारंपरिक base 32 address का उपयोग नहीं कर सकते, क्योंकि इसमें केवल destination का hash होता है। यह non-blinded public key प्रदान नहीं करता। इसलिए, अकेले base 32 address अपर्याप्त है। client को या तो पूरे destination (जिसमें public key होती है), या अकेली public key की आवश्यकता होती है। यदि client के पास address book में पूरा destination है, और address book hash द्वारा reverse lookup का समर्थन करता है, तो public key प्राप्त की जा सकती है।

इसलिए हमें एक नए format की जरूरत है जो hash के बजाय public key को base32 address में डालता है। इस format में public key के signature type और blinding scheme के signature type भी होने चाहिए। कुल आवश्यकताएं 32 + 3 = 35 bytes हैं, जिसके लिए base 32 में 56 characters की जरूरत है, या अधिक लंबे public key types के लिए और भी ज्यादा।

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
हम पारंपरिक base 32 addresses के समान ".b32.i2p" suffix का उपयोग करते हैं। Encrypted leasesets के लिए addresses को 56 encoded characters (35 decoded bytes) से पहचाना जाता है, जबकि पारंपरिक base 32 addresses के लिए 52 characters (32 bytes) होते हैं। b32 के अंत में पांच अनुपयोगित bits 0 होने चाहिए।

आप bittorrent के लिए encrypted LS2 का उपयोग नहीं कर सकते, क्योंकि compact announce replies 32 bytes के होते हैं। इन 32 bytes में केवल hash होता है। इसमें यह बताने के लिए कोई जगह नहीं है कि leaseset encrypted है, या signature types क्या हैं।

नए प्रारूप के बारे में अधिक जानकारी के लिए [naming specification](/docs/specs/naming) या [proposal 149](/proposals/149-b32-encrypted-ls2) देखें।

### ऑफलाइन कीज़ के साथ एन्क्रिप्टेड LS

ऑफलाइन keys के साथ एन्क्रिप्टेड leasesets के लिए, blinded private keys भी ऑफलाइन उत्पन्न करनी होंगी, प्रत्येक दिन के लिए एक।

चूंकि वैकल्पिक ऑफलाइन signature block encrypted leaseset के cleartext भाग में होता है, कोई भी floodfills को scrape करने वाला इसका उपयोग करके leaseset को (लेकिन इसे decrypt नहीं कर सकता) कई दिनों तक track कर सकता है। इसे रोकने के लिए, keys के मालिक को हर दिन के लिए नई transient keys भी generate करनी चाहिए। Transient और blinded दोनों keys को पहले से generate किया जा सकता है, और router को batch में deliver किया जा सकता है।

कई अस्थायी और blinded keys को पैकेजिंग करने और उन्हें client या router को प्रदान करने के लिए कोई file format परिभाषित नहीं है। offline keys के साथ encrypted leasesets का समर्थन करने के लिए कोई I2CP protocol enhancement परिभाषित नहीं है।

### नोट्स

- एन्क्रिप्टेड leasesets का उपयोग करने वाली सेवा floodfills में एन्क्रिप्टेड संस्करण प्रकाशित करेगी। हालांकि, दक्षता के लिए, यह प्रमाणीकरण के बाद (उदाहरण के लिए, whitelist के माध्यम से) wrapped garlic message में clients को unencrypted leasesets भेजेगी।
- Floodfills दुरुपयोग को रोकने के लिए अधिकतम आकार को एक उचित मान तक सीमित कर सकते हैं।
- डिक्रिप्शन के बाद, कई जांच की जानी चाहिए, जिसमें यह शामिल है कि आंतरिक timestamp और expiration शीर्ष स्तर पर मेल खाते हैं।
- ChaCha20 को AES के बजाय चुना गया था। जबकि AES हार्डवेयर समर्थन उपलब्ध होने पर गति समान होती है, ChaCha20 2.5-3x तेज है जब AES हार्डवेयर समर्थन उपलब्ध नहीं है, जैसे कि निम्न-स्तरीय ARM डिवाइसों पर।

## संदर्भ

- **[ED25519-REFS]** Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, और Bo-Yin Yang द्वारा "High-speed high-security signatures"। [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) और [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) और [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)

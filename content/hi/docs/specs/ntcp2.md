---
title: "NTCP2 Transport"
description: "router-से-router लिंक के लिए Noise-आधारित TCP परिवहन"
slug: "ntcp2"
category: "ट्रांसपोर्ट"
lastUpdated: "2026-01"
accurateFor: "0.9.66"
---

## अवलोकन

NTCP2 एक प्रमाणीकृत key agreement protocol है जो [NTCP](/docs/transport/ntcp) के विभिन्न प्रकार की स्वचालित पहचान और हमलों के प्रतिरोध में सुधार करता है।

NTCP2 को लचीलेपन और NTCP के साथ सहअस्तित्व के लिए डिज़ाइन किया गया है। इसे NTCP के समान पोर्ट पर, या अलग पोर्ट पर, या बिना किसी समकालिक NTCP समर्थन के समर्थित किया जा सकता है। विवरण के लिए नीचे Published Router Info अनुभाग देखें।

अन्य I2P transports की तरह, NTCP2 केवल I2NP संदेशों के point-to-point (router-to-router) transport के लिए परिभाषित है। यह एक सामान्य-उद्देश्य डेटा पाइप नहीं है।

NTCP2 संस्करण 0.9.36 से समर्थित है। मूल प्रस्ताव के लिए [Prop111](/proposals/111-ntcp-2) देखें, जिसमें पृष्ठभूमि चर्चा और अतिरिक्त जानकारी शामिल है।

## Noise Protocol Framework

NTCP2 Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (संशोधन 33, 2017-10-04) का उपयोग करता है। Noise के गुण Station-To-Station protocol [STS](#references) के समान हैं, जो [SSU](/docs/transport/ssu) protocol का आधार है। Noise की भाषा में, Alice पहल करने वाला (initiator) है, और Bob जवाब देने वाला (responder) है।

NTCP2 Noise प्रोटोकॉल Noise_XK_25519_ChaChaPoly_SHA256 पर आधारित है। (प्रारंभिक key derivation function के लिए वास्तविक identifier "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256" है जो I2P एक्सटेंशन को दर्शाता है - नीचे KDF 1 अनुभाग देखें) यह Noise प्रोटोकॉल निम्नलिखित primitives का उपयोग करता है:

- Handshake Pattern: XK Alice अपनी key Bob को transmit करती है (X) Alice को Bob की static key पहले से पता है (K)
- DH Function: X25519 X25519 DH 32 bytes की key length के साथ जैसा कि [RFC-7748](https://tools.ietf.org/html/rfc7748) में निर्दिष्ट है।
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305 जैसा कि [RFC-7539](https://tools.ietf.org/html/rfc7539) section 2.8 में निर्दिष्ट है। 12 byte nonce, जिसके पहले 4 bytes zero पर set हैं।
- Hash Function: SHA256 Standard 32-byte hash, जो पहले से ही I2P में व्यापक रूप से उपयोग किया जाता है।

## फ्रेमवर्क में जोड़े गए तत्व

NTCP2 निम्नलिखित सुधारों को Noise_XK_25519_ChaChaPoly_SHA256 के लिए परिभाषित करता है। ये आम तौर पर [NOISE](https://noiseprotocol.org/noise.html) सेक्शन 13 की दिशानिर्देशों का पालन करते हैं।

1) Cleartext ephemeral keys को एक ज्ञात key और IV का उपयोग करके AES encryption के साथ obfuscate किया जाता है। 2) संदेश 1 और 2 में random cleartext padding जोड़ा जाता है। Cleartext padding को handshake hash (MixHash) गणना में शामिल किया जाता है। संदेश 2 और संदेश 3 भाग 1 के लिए नीचे KDF अनुभाग देखें। संदेश 3 और data phase संदेशों में random AEAD padding जोड़ा जाता है। 3) एक दो-बाइट frame length field जोड़ा जाता है, जैसा कि TCP पर Noise के लिए आवश्यक है, और obfs4 की तरह। इसका उपयोग केवल data phase संदेशों में किया जाता है। संदेश 1 और 2 AEAD frames निश्चित लंबाई के हैं। संदेश 3 भाग 1 AEAD frame निश्चित लंबाई का है। संदेश 3 भाग 2 AEAD frame की लंबाई संदेश 1 में निर्दिष्ट होती है। 4) दो-बाइट frame length field को SipHash-2-4 के साथ obfuscate किया जाता है, जैसा कि obfs4 में होता है। 5) संदेश 1,2,3, और data phase के लिए payload format परिभाषित है। निश्चित रूप से, ये framework में परिभाषित नहीं हैं।

## संदेश

सभी NTCP2 संदेश 65537 बाइट्स या उससे कम लंबाई के होते हैं। संदेश प्रारूप Noise संदेशों पर आधारित है, जिसमें framing और indistinguishability के लिए संशोधन किए गए हैं। मानक Noise लाइब्रेरी का उपयोग करने वाले implementations को प्राप्त संदेशों को Noise संदेश प्रारूप में/से पूर्व-प्रसंस्करण की आवश्यकता हो सकती है। सभी एन्क्रिप्टेड फ़ील्ड AEAD ciphertexts हैं।

स्थापना अनुक्रम निम्नलिखित है:

```
Alice Bob

SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Noise terminology का उपयोग करते हुए, establishment और data sequence निम्नलिखित है: (Payload Security Properties [Noise](https://noiseprotocol.org/noise.html) से)

```
XK(s, rs): Authentication Confidentiality

<- s \... -> e, es 0 2 <- e, ee 2 1 -> s, se 2 5 <- 2 5
```
एक बार session स्थापित हो जाने के बाद, Alice और Bob Data messages का आदान-प्रदान कर सकते हैं।

सभी संदेश प्रकार (SessionRequest, SessionCreated, SessionConfirmed, Data और TimeSync) इस खंड में निर्दिष्ट हैं।

कुछ संकेतन:

    - RH_A = Router Hash for Alice (32 bytes)
    - RH_B = Router Hash for Bob (32 bytes)

### प्रमाणित एन्क्रिप्शन

तीन अलग-अलग प्रामाणिक एन्क्रिप्शन इंस्टेंस (CipherStates) हैं। एक handshake चरण के दौरान, और दो (transmit और receive) डेटा चरण के लिए। प्रत्येक का KDF से अपना key है।

एन्क्रिप्टेड/प्रमाणित डेटा को इस प्रकार दर्शाया जाएगा

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Encrypted and authenticated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

एन्क्रिप्टेड और प्रमाणित डेटा प्रारूप।

एन्क्रिप्शन/डिक्रिप्शन फंक्शन्स के इनपुट:

```
k :: 32 byte cipher key, as generated from KDF



nonce :: Counter-based nonce, 12 bytes.

Starts at 0 and incremented for each message. First four bytes are always zero. Last eight bytes are the counter, little-endian encoded. Maximum value is 2**64 - 2. Connection must be dropped and restarted after it reaches that value. The value 2**64 - 1 must never be sent.

ad :: In handshake phase:

Associated data, 32 bytes. The SHA256 hash of all preceding data. In data phase: Zero bytes

data :: Plaintext data, 0 or more bytes
```
एन्क्रिप्शन फ़ंक्शन का आउटपुट, डिक्रिप्शन फ़ंक्शन का इनपुट:

```
+----+----+----+----+----+----+----+----+

[|Obfs Len |](##SUBST##|Obfs Len |) | +----+----+ + | ChaCha20 encrypted data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | Poly1305 Message Authentication Code | + (MAC) + | 16 bytes | +----+----+----+----+----+----+----+----+

    Obfs Len :: Length of (encrypted data + MAC) to follow, 16 - 65535

    :   Obfuscation using SipHash (see below) Not used in message 1 or 2, or message 3 part 1, where the length is fixed Not used in message 3 part 1, as the length is specified in message 1

    encrypted data :: Same size as plaintext data, 0 - 65519 bytes

    MAC :: Poly1305 message authentication code, 16 bytes
```
ChaCha20 के लिए, यहाँ जो वर्णित है वह [RFC-7539](https://tools.ietf.org/html/rfc7539) के अनुरूप है, जो TLS [RFC-7905](https://tools.ietf.org/html/rfc7905) में भी समान रूप से उपयोग किया जाता है।

#### टिप्पणियाँ

- चूंकि ChaCha20 एक stream cipher है, plaintexts को padded करने की आवश्यकता नहीं है। अतिरिक्त keystream bytes को छोड़ दिया जाता है।
- cipher के लिए key (256 bits) SHA256 KDF के माध्यम से सहमत की जाती है। प्रत्येक संदेश के लिए KDF का विवरण नीचे अलग-अलग खंडों में है।
- संदेश 1, 2, और संदेश 3 के पहले भाग के लिए ChaChaPoly frames ज्ञात आकार के हैं। संदेश 3 के दूसरे भाग से शुरू करके, frames परिवर्तनीय आकार के हैं। संदेश 3 भाग 1 का आकार संदेश 1 में निर्दिष्ट है। data phase से शुरू करके, frames को दो-बाइट लंबाई के साथ प्रीपेंड किया जाता है जो obfs4 की तरह SipHash के साथ obfuscated होता है।
- Padding संदेश 1 और 2 के लिए authenticated data frame के बाहर है। अगले संदेश के लिए KDF में padding का उपयोग किया जाता है ताकि tampering का पता लगाया जा सके। संदेश 3 से शुरू करके, padding authenticated data frame के अंदर है।

#### AEAD Error Handling

- संदेशों 1, 2, और संदेश 3 के भाग 1 और 2 में, AEAD संदेश का आकार पहले से ज्ञात है। AEAD प्रमाणीकरण विफलता पर, प्राप्तकर्ता को आगे की संदेश प्रसंस्करण रोकनी चाहिए और बिना जवाब दिए कनेक्शन बंद कर देना चाहिए। यह एक असामान्य बंद होना चाहिए (TCP RST)।
- probing प्रतिरोध के लिए, संदेश 1 में, AEAD विफलता के बाद, Bob को एक यादृच्छिक timeout (रेंज TBD) सेट करना चाहिए और फिर socket बंद करने से पहले यादृच्छिक संख्या में bytes (रेंज TBD) पढ़ना चाहिए। Bob को बार-बार विफलता वाले IPs की blacklist बनाए रखनी चाहिए।
- data phase में, AEAD संदेश का आकार SipHash के साथ "encrypted" (obfuscated) है। decryption oracle बनाने से बचने के लिए सावधानी बरतनी चाहिए। data phase AEAD प्रमाणीकरण विफलता पर, प्राप्तकर्ता को एक यादृच्छिक timeout (रेंज TBD) सेट करना चाहिए और फिर यादृच्छिक संख्या में bytes (रेंज TBD) पढ़ना चाहिए। पढ़ने के बाद, या read timeout पर, प्राप्तकर्ता को "AEAD failure" reason code युक्त termination block के साथ payload भेजना चाहिए, और कनेक्शन बंद कर देना चाहिए।
- data phase में invalid length field value के लिए समान error action लें।

### Key Derivation Function (KDF) (handshake message 1 के लिए)

KDF, DH परिणाम से एक handshake phase cipher key k उत्पन्न करता है, HMAC-SHA256(key, data) का उपयोग करके जैसा कि [RFC-2104](https://tools.ietf.org/html/rfc2104) में परिभाषित है। ये InitializeSymmetric(), MixHash(), और MixKey() functions हैं, बिल्कुल वैसे ही जैसे Noise spec में परिभाषित हैं।

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

एलिस बॉब को भेजती है।

Noise सामग्री: Alice की ephemeral key X Noise payload: 16 बाइट विकल्प ब्लॉक गैर-noise payload: यादृच्छिक पैडिंग

(पेलोड सुरक्षा गुण [Noise](https://noiseprotocol.org/noise.html) से)

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
X मान को encrypted किया जाता है ताकि payload indistinguishably और uniqueness सुनिश्चित की जा सके, जो आवश्यक DPI countermeasures हैं। हम इसे प्राप्त करने के लिए AES encryption का उपयोग करते हैं, न कि अधिक जटिल और धीमे विकल्पों जैसे elligator2 का। Bob के router public key के लिए Asymmetric encryption बहुत धीमा होगा। AES encryption Bob के router hash को key के रूप में और Bob के IV का उपयोग करता है जैसा कि network database में प्रकाशित है।

AES एन्क्रिप्शन केवल DPI प्रतिरोध के लिए है। कोई भी पक्ष जो Bob के router hash और IV को जानता है, जो नेटवर्क डेटाबेस में प्रकाशित हैं, इस संदेश में X मान को decrypt कर सकता है।

पैडिंग Alice द्वारा एन्क्रिप्ट नहीं की जाती है। टाइमिंग अटैक को रोकने के लिए Bob के लिए पैडिंग को डिक्रिप्ट करना आवश्यक हो सकता है।

कच्ची सामग्री:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + obfuscated with RH_B + | AES-CBC-256 encrypted X | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | | + + | ChaChaPoly frame | + (32 bytes) + | k defined in KDF for message 1 | + n = 0 + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | ~ padding (optional) ~ | length defined in options block | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian

    :   key: RH_B iv: As published in Bobs network database entry

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Total message length must be 287 bytes or less if Bob is publishing his address as NTCP (see Version Detection section below). Alice and Bob will use the padding data in the KDF for message 2. It is authenticated so that any tampering will cause the next message to fail.
```
अनएन्क्रिप्टेड डेटा (Poly1305 प्रमाणीकरण टैग दिखाया नहीं गया):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | X | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | options | + (16 bytes) + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, X25519 ephemeral key, little endian

    options :: options block, 16 bytes, see below

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Total message length must be 287 bytes or less if Bob is publishing his address as "NTCP" (see Version Detection section below) Alice and Bob will use the padding data in the KDF for message 2. It is authenticated so that any tampering will cause the next message to fail.
```
Options block: नोट: सभी फ़ील्ड big-endian हैं।

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
#### नोट्स

- जब प्रकाशित पता "NTCP" है, तो Bob एक ही पोर्ट पर NTCP और NTCP2 दोनों का समर्थन करता है। संगतता के लिए, जब "NTCP" के रूप में प्रकाशित पते से कनेक्शन शुरू करते समय, Alice को इस संदेश के अधिकतम आकार को, padding सहित, 287 bytes या उससे कम तक सीमित करना चाहिए। यह Bob द्वारा स्वचालित protocol पहचान की सुविधा प्रदान करता है। जब "NTCP2" के रूप में प्रकाशित होता है, तो कोई आकार प्रतिबंध नहीं है। नीचे Published Addresses और Version Detection अनुभागों को देखें।

- प्रारंभिक AES ब्लॉक में अद्वितीय X मान यह सुनिश्चित करता है कि ciphertext हर session के लिए अलग हो।

- Bob को उन connections को reject करना चाहिए जहाँ timestamp value वर्तमान समय से बहुत अधिक अलग है। अधिकतम delta time को "D" कहते हैं। Bob को पहले से उपयोग किए गए handshake values का एक local cache बनाए रखना चाहिए और duplicates को reject करना चाहिए, replay attacks को रोकने के लिए। Cache में values का lifetime कम से कम 2*D होना चाहिए। Cache values implementation-dependent हैं, हालांकि 32-byte X value (या इसका encrypted equivalent) का उपयोग किया जा सकता है।

- Diffie-Hellman ephemeral keys का कभी भी पुन: उपयोग नहीं किया जा सकता है, क्रिप्टोग्राफिक हमलों को रोकने के लिए, और पुन: उपयोग को replay attack के रूप में अस्वीकार किया जाएगा।

- "KE" और "auth" विकल्प संगत होने चाहिए, यानी साझा गुप्त K उपयुक्त आकार का होना चाहिए। यदि अधिक "auth" विकल्प जोड़े जाते हैं, तो यह अलग KDF या अलग truncation आकार का उपयोग करने के लिए "KE" flag के अर्थ को अस्पष्ट रूप से बदल सकता है।

- Bob को यहाँ यह सत्यापित करना होगा कि Alice की ephemeral key curve पर एक वैध बिंदु है।

- Padding को एक उचित मात्रा तक सीमित होना चाहिए। Bob अत्यधिक padding वाले connections को reject कर सकता है। Bob अपने padding options को message 2 में specify करेगा। Min/max guidelines TBD। न्यूनतम 0 से 31 bytes तक का random size? (Distribution implementation-dependent है) Java implementations वर्तमान में padding को अधिकतम 256 bytes तक सीमित करते हैं।

- किसी भी त्रुटि पर, जिसमें AEAD, DH, timestamp, स्पष्ट replay, या key validation failure शामिल है, Bob को आगे की message processing रोकनी चाहिए और बिना जवाब दिए connection बंद कर देना चाहिए। यह एक असामान्य बंद होना चाहिए (TCP RST)। probing resistance के लिए, AEAD failure के बाद, Bob को एक यादृच्छिक timeout (सीमा TBD) सेट करना चाहिए और फिर socket बंद करने से पहले यादृच्छिक संख्या में bytes (सीमा TBD) पढ़ना चाहिए।

- Bob वैध key के लिए decryption की कोशिश करने से पहले एक तेज़ MSB जांच कर सकता है (X[31] & 0x80 == 0)। यदि high bit सेट है, तो AEAD failures की तरह probing resistance को implement करें।

- DoS शमन: DH एक अपेक्षाकृत महंगा ऑपरेशन है। पिछले NTCP प्रोटोकॉल की तरह, router को CPU या कनेक्शन समाप्ति को रोकने के लिए सभी आवश्यक उपाय करने चाहिए। अधिकतम सक्रिय कनेक्शन और प्रगति में अधिकतम कनेक्शन सेटअप पर सीमा लगाएं। पढ़ने के समय की सीमा लागू करें (प्रति-पढ़ने और "slowloris" के लिए कुल दोनों)। एक ही स्रोत से दोहराए या साथ-साथ कनेक्शन को सीमित करें। बार-बार असफल होने वाले स्रोतों के लिए ब्लैकलिस्ट बनाए रखें। AEAD विफलता का जवाब न दें।

- तेज़ version detection और handshaking की सुविधा के लिए, implementations को यह सुनिश्चित करना चाहिए कि Alice पहले message की पूरी contents को buffer करे और फिर एक साथ flush करे, padding सहित। इससे इस बात की संभावना बढ़ जाती है कि data एक single TCP packet में contained होगा (जब तक कि OS या middleboxes द्वारा segmented न हो), और Bob द्वारा एक साथ receive होगा। इसके अतिरिक्त, implementations को यह सुनिश्चित करना चाहिए कि Bob दूसरे message की पूरी contents को buffer करे और फिर एक साथ flush करे, padding सहित। और यह कि Bob तीसरे message की पूरी contents को buffer करे और फिर एक साथ flush करे। यह भी efficiency के लिए है और random padding की effectiveness सुनिश्चित करने के लिए है।

- "ver" फील्ड: समग्र Noise protocol, extensions, और NTCP protocol जिसमें payload specifications शामिल हैं, जो NTCP2 को दर्शाता है। इस फील्ड का उपयोग भविष्य के बदलावों के लिए समर्थन को दर्शाने के लिए किया जा सकता है।

- Message 3 part 2 length: यह दूसरे AEAD frame का आकार है (16-byte MAC सहित) जिसमें Alice की Router Info और वैकल्पिक padding होती है जो SessionConfirmed message में भेजी जाएगी। चूंकि router समय-समय पर अपनी Router Info को पुनर्जनित और पुनः प्रकाशित करते हैं, वर्तमान Router Info का आकार message 3 भेजे जाने से पहले बदल सकता है। Implementations को दो रणनीतियों में से एक चुननी होगी:

a\) संदेश 3 में भेजे जाने वाली वर्तमान Router Info को सेव करें, ताकि size पता हो, और वैकल्पिक रूप से padding के लिए जगह जोड़ें;

b\) निर्दिष्ट आकार को Router Info आकार में संभावित वृद्धि के लिए पर्याप्त बढ़ाएं, और जब message 3 वास्तव में भेजा जाता है तो हमेशा padding जोड़ें। दोनों में से किसी भी स्थिति में, message 1 में शामिल "m3p2len" लंबाई उस frame के आकार के बिल्कुल बराबर होनी चाहिए जब वह message 3 में भेजा जाता है।

- Bob को connection को fail करना चाहिए यदि message 1 को validate करने और padding को पढ़ने के बाद कोई भी incoming data बचा रहता है। Alice से कोई extra data नहीं होना चाहिए, क्योंकि Bob ने अभी तक message 2 के साथ respond नहीं किया है।

- नेटवर्क ID फील्ड का उपयोग क्रॉस-नेटवर्क कनेक्शन को जल्दी पहचानने के लिए किया जाता है। यदि यह फील्ड शून्य नहीं है, और Bob के नेटवर्क ID से मेल नहीं खाता, तो Bob को डिस्कनेक्ट हो जाना चाहिए और भविष्य के कनेक्शन को ब्लॉक कर देना चाहिए। टेस्ट नेटवर्क से आने वाले किसी भी कनेक्शन में अलग ID होना चाहिए और वे टेस्ट में फेल हो जाएंगे। 0.9.42 के अनुसार। अधिक जानकारी के लिए proposal 147 देखें।

### Key Derivation Function (KDF) (handshake message 2 और message 3 part 1 के लिए)

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

बॉब एलिस को भेजता है।

Noise सामग्री: Bob की ephemeral key Y Noise payload: 16 बाइट विकल्प ब्लॉक Non-noise payload: रैंडम पैडिंग

(पेलोड सुरक्षा गुण [Noise](https://noiseprotocol.org/noise.html) से)

```
XK(s, rs): Authentication Confidentiality

<- e, ee 2 1

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 1. Encryption to an ephemeral recipient. This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee"). However, the sender has not authenticated the recipient, so this payload might be sent to any party, including an active attacker.

    "e": Bob generates a new ephemeral key pair and stores it in the e variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Y वैल्यू को payload की अविभेद्यता और विशिष्टता सुनिश्चित करने के लिए एन्क्रिप्ट किया जाता है, जो आवश्यक DPI प्रतिरोधी उपाय हैं। हम इसे प्राप्त करने के लिए AES एन्क्रिप्शन का उपयोग करते हैं, न कि elligator2 जैसे अधिक जटिल और धीमे विकल्पों का। Alice के router public key के लिए असममित एन्क्रिप्शन बहुत धीमा होगा। AES एन्क्रिप्शन Bob के router hash को key के रूप में उपयोग करता है और message 1 से AES state का उपयोग करता है (जो Bob के IV के साथ initialize किया गया था जैसा कि network database में प्रकाशित है)।

AES encryption केवल DPI प्रतिरोध के लिए है। कोई भी पक्ष जो Bob के router hash और IV को जानता है, जो नेटवर्क डेटाबेस में प्रकाशित हैं, और संदेश 1 के पहले 32 bytes को कैप्चर करता है, वह इस संदेश में Y मान को decrypt कर सकता है।

कच्ची सामग्री:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + obfuscated with RH_B + | AES-CBC-256 encrypted Y | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | ChaChaPoly frame | + Encrypted and authenticated data + | 32 bytes | + k defined in KDF for message 2 + | n = 0; see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian

    :   key: RH_B iv: Using AES state from message 1
```
असंकेतित डेटा (Poly1305 auth tag दिखाया नहीं गया):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Y | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | options | + (16 bytes) + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, X25519 ephemeral key, little endian

    options :: options block, 16 bytes, see below

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Alice and Bob will use the padding data in the KDF for message 3 part 1. It is authenticated so that any tampering will cause the next message to fail.
```
#### नोट्स

- Alice को यहाँ यह validate करना होगा कि Bob की ephemeral key curve पर एक valid point है।
- Padding को एक reasonable amount तक सीमित होना चाहिए। Alice excessive padding वाले connections को reject कर सकती है। Alice message 3 में अपने padding options specify करेगी। Min/max guidelines TBD। कम से कम 0 से 31 bytes का random size? (Distribution implementation-dependent है)
- किसी भी error पर, AEAD, DH, timestamp, apparent replay, या key validation failure सहित, Alice को आगे की message processing रोकनी होगी और बिना respond किए connection बंद करना होगा। यह एक abnormal close (TCP RST) होना चाहिए।
- तेज़ handshaking की सुविधा के लिए, implementations को ensure करना होगा कि Bob पहले message की पूरी contents को padding सहित buffer करे और फिर एक साथ flush करे। इससे इस बात की संभावना बढ़ जाती है कि data एक single TCP packet में contained होगा (जब तक OS या middleboxes द्वारा segment न किया जाए), और Alice द्वारा एक साथ receive किया जाएगा। यह efficiency के लिए भी है और random padding की effectiveness ensure करने के लिए है।
- Alice को connection fail करना होगा अगर message 2 को validate करने और padding पढ़ने के बाद कोई incoming data बचा रहता है। Bob से कोई extra data नहीं होना चाहिए, क्योंकि Alice ने अभी तक message 3 के साथ respond नहीं किया है।

Options block: नोट: सभी फील्ड big-endian हैं।

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
#### नोट्स

- Alice को उन connections को reject करना चाहिए जहाँ timestamp value वर्तमान समय से बहुत अधिक अलग है। अधिकतम delta time को "D" कहते हैं। Alice को पहले से उपयोग किए गए handshake values का एक local cache बनाए रखना चाहिए और duplicates को reject करना चाहिए, ताकि replay attacks को रोका जा सके। Cache में values का lifetime कम से कम 2*D होना चाहिए। Cache values implementation-dependent हैं, हालांकि 32-byte Y value (या इसका encrypted equivalent) का उपयोग किया जा सकता है।

#### समस्याएं

- यहाँ min/max padding विकल्प शामिल करें?

### हैंडशेक संदेश 3 भाग 1 के लिए एन्क्रिप्शन, संदेश 2 KDF का उपयोग करके)

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
### Key Derivation Function (KDF) (handshake message 3 part 2 के लिए)

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

Alice, Bob को भेजती है।

Noise सामग्री: Alice की static key Noise payload: Alice का RouterInfo और random padding Non-noise payload: कोई नहीं

(पेलोड सुरक्षा गुण [Noise](https://noiseprotocol.org/noise.html) से)

```
XK(s, rs): Authentication Confidentiality

-> s, se 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.

    "s": Alice writes her static public key from the s variable into the message buffer, encrypting it, and hashes the output along with the old h to derive a new h.

    "se": A DH is performed between the Alice's static key pair and the Bob's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
इसमें दो ChaChaPoly फ्रेम हैं। पहला Alice की encrypted static public key है। दूसरा Noise payload है: Alice की encrypted RouterInfo, वैकल्पिक विकल्प, और वैकल्पिक padding। ये अलग keys का उपयोग करते हैं, क्योंकि बीच में MixKey() function को कॉल किया जाता है।

कच्ची सामग्री:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + ChaChaPoly frame (48 bytes) + | Encrypted and authenticated | + Alice static key S + | (32 bytes) | + + | k defined in KDF for message 2 | + n = 1 + | see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | | + Length specified in message 1 + | | + ChaChaPoly frame + | Encrypted and authenticated | + + | Alice RouterInfo | + using block format 2 + | Alice Options (optional) | + using block format 1 + | Arbitrary padding | + using block format 254 + | | + + | k defined in KDF for message 3 part 2 | + n = 0 + | see KDF for associated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian

    :   inside 48 byte ChaChaPoly frame
```
अनएन्क्रिप्टेड डेटा (Poly1305 auth tags दिखाए नहीं गए):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | S | + Alice static key + | (32 bytes) | + + | | + + +----+----+----+----+----+----+----+----+ | | + + | | + + | Alice RouterInfo block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Optional Options block + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Optional Padding block + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, Alice's X25519 static key, little endian
```
#### नोट्स

- Bob को सामान्य Router Info सत्यापन करना चाहिए। सुनिश्चित करें कि signature प्रकार समर्थित है, signature को सत्यापित करें, timestamp की सीमा के भीतर होने की पुष्टि करें, और कोई अन्य आवश्यक जांच करें।

- Bob को यह सत्यापित करना होगा कि पहले frame में प्राप्त Alice की static key, Router Info में स्थित static key से मेल खाती है। Bob को पहले Router Info में मिलते version (v) विकल्प के साथ NTCP या NTCP2 Router Address की खोज करनी होगी। नीचे Published Router Info और Unpublished Router Info अनुभागों को देखें।

- यदि Bob के netdb में Alice की RouterInfo का पुराना version है, तो सत्यापित करें कि router info में static key दोनों में समान है, यदि मौजूद है, और यदि पुराना version XXX से कम पुराना है (नीचे key rotate time देखें)

- Bob को यहाँ यह सत्यापित करना चाहिए कि Alice की static key curve पर एक वैध बिंदु है।

- विकल्प शामिल किए जाने चाहिए, padding पैरामीटर निर्दिष्ट करने के लिए।

- किसी भी त्रुटि पर, जिसमें AEAD, RI, DH, timestamp, या key validation failure शामिल है, Bob को आगे की message processing रोकनी चाहिए और बिना response दिए connection बंद कर देना चाहिए। यह एक असामान्य close (TCP RST) होना चाहिए।

- तेज़ handshaking को सुविधाजनक बनाने के लिए, implementations को यह सुनिश्चित करना चाहिए कि Alice तीसरे message की संपूर्ण contents को buffer करे और फिर एक साथ flush करे, दोनों AEAD frames सहित। इससे इस बात की संभावना बढ़ जाती है कि data एक ही TCP packet में समाहित होगा (जब तक कि OS या middleboxes द्वारा segmented न किया जाए), और Bob द्वारा एक साथ receive किया जाएगा। यह efficiency के लिए भी है और random padding की प्रभावशीलता सुनिश्चित करने के लिए भी।

- Message 3 part 2 frame length: इस frame की लंबाई (MAC सहित) Alice द्वारा message 1 में भेजी जाती है। padding के लिए पर्याप्त स्थान की अनुमति देने के महत्वपूर्ण नोट्स के लिए उस message को देखें।

- Message 3 part 2 frame content: इस frame का format data phase frames के format के समान है, सिवाय इसके कि frame की length Alice द्वारा message 1 में भेजी जाती है। Data phase frame format के लिए नीचे देखें। Frame में निम्नलिखित क्रम में 1 से 3 blocks होने चाहिए:

1)  Alice के Router Info ब्लॉक (आवश्यक)   2)  Options ब्लॉक (वैकल्पिक)

3\) पैडिंग ब्लॉक (वैकल्पिक) इस फ्रेम में कभी भी कोई अन्य ब्लॉक प्रकार नहीं होना चाहिए।

- Message 3 part 2 padding की आवश्यकता नहीं है यदि Alice message 3 के अंत में एक data phase frame (वैकल्पिक रूप से padding युक्त) जोड़ती है और दोनों को एक साथ भेजती है, क्योंकि यह एक observer को एक बड़ी byte stream के रूप में दिखाई देगा। चूंकि Alice के पास आम तौर पर, लेकिन हमेशा नहीं, Bob को भेजने के लिए एक I2NP message होता है (इसीलिए उसने उससे connection बनाया), यह अनुशंसित implementation है, efficiency के लिए और random padding की प्रभावशीलता सुनिश्चित करने के लिए।

- दोनों Message 3 AEAD frames (भाग 1 और 2) की कुल लंबाई 65535 bytes है; भाग 1 48 bytes है इसलिए भाग 2 की अधिकतम frame लंबाई 65487 है; MAC को छोड़कर भाग 2 की अधिकतम plaintext लंबाई 65471 है।

### Key Derivation Function (KDF) (डेटा चरण के लिए)

डेटा चरण शून्य-लंबाई संबद्ध डेटा इनपुट का उपयोग करता है।

KDF chaining key ck से दो cipher keys k_ab और k_ba generate करता है, HMAC-SHA256(key, data) का उपयोग करके जैसा कि [RFC-2104](https://tools.ietf.org/html/rfc2104) में परिभाषित है। यह Split() function है, बिल्कुल वैसा जैसा Noise spec में परिभाषित है।

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
### 4) डेटा चरण

Noise payload: जैसा कि नीचे परिभाषित है, रैंडम पैडिंग सहित Non-noise payload: कोई नहीं

संदेश 3 के दूसरे भाग से शुरू करके, सभी संदेश एक प्रमाणित और एन्क्रिप्टेड ChaChaPoly "frame" के अंदर होते हैं जिसमें दो-बाइट अस्पष्टीकृत लंबाई जोड़ी गई होती है। सभी padding frame के अंदर होती है। frame के अंदर एक मानक प्रारूप होता है जिसमें शून्य या अधिक "blocks" होते हैं। प्रत्येक block में एक-बाइट प्रकार और दो-बाइट लंबाई होती है। प्रकारों में date/time, I2NP message, options, termination, और padding शामिल हैं।

नोट: Bob अपना RouterInfo Alice को data phase में अपने पहले संदेश के रूप में भेज सकता है, लेकिन यह आवश्यक नहीं है।

(पेलोड सुरक्षा गुण [Noise](https://noiseprotocol.org/noise.html) से)

```
XK(s, rs): Authentication Confidentiality

<- 2 5 -> 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### नोट्स

- दक्षता के लिए और length field की पहचान को कम से कम करने के लिए, implementations को यह सुनिश्चित करना चाहिए कि sender data messages की संपूर्ण सामग्री को एक साथ buffer करे और फिर flush करे, जिसमें length field और AEAD frame शामिल है। इससे इस बात की संभावना बढ़ जाती है कि data एक single TCP packet में समाहित हो जाएगा (जब तक कि OS या middleboxes द्वारा segmented न किया जाए), और दूसरी पार्टी को एक साथ प्राप्त हो जाएगा। यह दक्षता के लिए भी है और random padding की प्रभावशीलता सुनिश्चित करने के लिए है।
- Router AEAD error पर session को समाप्त करने का चुनाव कर सकता है, या communications जारी रखने का प्रयास कर सकता है। यदि जारी रखता है, तो router को बार-बार errors के बाद समाप्त कर देना चाहिए।

#### SipHash अस्पष्टीकृत लंबाई

संदर्भ: [SipHash](https://www.131002.net/siphash/)

एक बार दोनों पक्षों द्वारा handshake पूरा हो जाने के बाद, वे payloads को स्थानांतरित करते हैं जो फिर ChaChaPoly "frames" में encrypted और authenticated होते हैं।

प्रत्येक frame से पहले दो-बाइट की length होती है, big endian में। यह length बताती है कि कितने encrypted frame bytes आगे आने हैं, MAC सहित। stream में पहचान योग्य length fields को transmit करने से बचने के लिए, frame length को SipHash से प्राप्त mask के साथ XOR करके obfuscated किया जाता है, जैसा कि data phase KDF से initialized होता है। ध्यान दें कि दोनों दिशाओं में KDF से unique SipHash keys और IVs होती हैं।

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
रिसीवर के पास समान SipHash keys और IV होती है। लंबाई को डिकोड करना mask को derive करके किया जाता है जो लंबाई को obfuscate करने के लिए उपयोग की जाती है और truncated digest को XOR करके frame की लंबाई प्राप्त की जाती है। Frame length encrypted frame की कुल लंबाई है जिसमें MAC भी शामिल है।

#### नोट्स

- यदि आप SipHash library function का उपयोग करते हैं जो एक unsigned long integer return करता है, तो Mask के रूप में सबसे कम महत्वपूर्ण दो bytes का उपयोग करें। long integer को अगले IV के रूप में little endian में convert करें।

#### कच्ची सामग्री

```
+----+----+----+----+----+----+----+----+

[|obf size |](##SUBST##|obf size |) | +----+----+ + | | + ChaChaPoly frame + | Encrypted and authenticated | + key is k_ab for Alice to Bob + | key is k_ba for Bob to Alice | + as defined in KDF for data phase + | n starts at 0 and increments | + for each frame in that direction + | no associated data | + 16 bytes minimum + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    obf size :: 2 bytes length obfuscated with SipHash

    :   when de-obfuscated: 16 - 65535

    Minimum size including length field is 18 bytes. Maximum size including length field is 65537 bytes. Obfuscated length is 2 bytes. Maximum ChaChaPoly frame is 65535 bytes.
```
#### नोट्स

- चूंकि receiver को MAC की जांच के लिए पूरा frame प्राप्त करना होता है, यह अनुशंसा की जाती है कि sender frame के आकार को अधिकतम करने के बजाय कुछ KB तक सीमित रखे। इससे receiver पर latency कम से कम होगी।

#### अनएन्क्रिप्टेड डेटा

एन्क्रिप्टेड फ्रेम में शून्य या अधिक ब्लॉक होते हैं। प्रत्येक ब्लॉक में एक वन-बाइट आइडेंटिफायर, एक टू-बाइट लेंथ, और शून्य या अधिक बाइट्स का डेटा होता है।

विस्तारशीलता के लिए, रिसीवर को अज्ञात पहचानकर्ताओं वाले ब्लॉक्स को नजरअंदाज करना चाहिए, और उन्हें पैडिंग के रूप में मानना चाहिए।

एन्क्रिप्टेड डेटा अधिकतम 65535 बाइट्स का होता है, जिसमें एक 16-बाइट प्रमाणीकरण हेडर भी शामिल है, इसलिए अधिकतम अनएन्क्रिप्टेड डेटा 65519 बाइट्स का होता है।

(Poly1305 auth tag दिखाया नहीं गया):

```
+----+----+----+----+----+----+----+----+

[|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ [|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ ~ . . . ~

    blk :: 1 byte

    :   0 for datetime 1 for options 2 for RouterInfo 3 for I2NP message 4 for termination 224-253 reserved for experimental features 254 for padding 255 reserved for future extension

    size :: 2 bytes, big endian, size of data to follow, 0 - 65516 data :: the data

    Maximum ChaChaPoly frame is 65535 bytes. Poly1305 tag is 16 bytes Maximum total block size is 65519 bytes Maximum single block size is 65519 bytes Block type is 1 byte Block length is 2 bytes Maximum single block data size is 65516 bytes.
```
#### ब्लॉक क्रमबद्धता नियम

handshake message 3 part 2 में, क्रम इस प्रकार होना चाहिए: RouterInfo, उसके बाद Options यदि मौजूद हो, उसके बाद Padding यदि मौजूद हो। कोई अन्य blocks की अनुमति नहीं है।

डेटा चरण में, क्रम निर्दिष्ट नहीं है, निम्नलिखित आवश्यकताओं को छोड़कर: Padding, यदि मौजूद है, तो अंतिम ब्लॉक होना चाहिए। Termination, यदि मौजूद है, तो Padding को छोड़कर अंतिम ब्लॉक होना चाहिए।

एक ही frame में कई I2NP blocks हो सकते हैं। एक ही frame में कई Padding blocks की अनुमति नहीं है। अन्य block types में शायद एक ही frame में कई blocks नहीं होंगे, लेकिन यह प्रतिबंधित नहीं है।

#### DateTime

समय सिंक्रोनाइज़ेशन के लिए विशेष मामला:

```
+----+----+----+----+----+----+----+

| 0 | 4 | timestamp |

    +----+----+----+----+----+----+----+

    blk :: 0 size :: 2 bytes, big endian, value = 4 timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106
```
नोट: नेटवर्क में clock bias को रोकने के लिए implementations को निकटतम सेकंड तक round करना चाहिए।

#### विकल्प

अपडेटेड विकल्प पास करें। विकल्पों में शामिल हैं: न्यूनतम और अधिकतम पैडिंग।

Options block परिवर्तनीय लंबाई का होगा।

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
#### विकल्प समस्याएं

- Options format TBD है।
- Options negotiation TBD है।

#### RouterInfo

Alice का RouterInfo Bob को पास करें। handshake message 3 part 2 में उपयोग किया जाता है। Alice का RouterInfo Bob को, या Bob का Alice को पास करें। data phase में वैकल्पिक रूप से उपयोग किया जाता है।

```
+----+----+----+----+----+----+----+----+

| 2 | size [|flg |](##SUBST##|flg |) RouterInfo |

    +----+----+----+----+ + | (Alice RI in handshake msg 3 part 2) | ~ (Alice, Bob, or third-party ~ | RI in data phase) | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 2 size :: 2 bytes, big endian, size of flag + router info to follow flg :: 1 byte flags bit order: 76543210 bit 0: 0 for local store, 1 for flood request bits 7-1: Unused, set to 0 for future compatibility routerinfo :: Alice's or Bob's RouterInfo
```
#### नोट्स

- जब data phase में उपयोग किया जाता है, तो receiver (Alice या Bob) को validate करना चाहिए कि यह वही Router Hash है जो मूल रूप से भेजा गया था (Alice के लिए) या भेजा गया था (Bob के लिए)। फिर, इसे एक local I2NP DatabaseStore Message के रूप में treat करें। signature को validate करें, अधिक recent timestamp को validate करें, और local netdb में store करें। यदि flag bit 0 है 1, और receiving party floodfill है, तो इसे एक nonzero reply token के साथ DatabaseStore Message के रूप में treat करें, और इसे nearest floodfills में flood करें।
- Router Info gzip के साथ compressed नहीं है (DatabaseStore Message के विपरीत, जहाँ यह है)
- Flooding तब तक request नहीं की जानी चाहिए जब तक RouterInfo में published RouterAddresses न हों। Receiving router को RouterInfo को तब तक flood नहीं करना चाहिए जब तक उसमें published RouterAddresses न हों।
- Implementers को यह ensure करना चाहिए कि block पढ़ते समय, malformed या malicious data के कारण reads अगले block में overrun न हों।
- यह protocol कोई acknowledgement प्रदान नहीं करता कि RouterInfo receive, store या flood हुआ था (handshake या data phase दोनों में)। यदि acknowledgement चाहिए, और receiver floodfill है, तो sender को इसके बजाय reply token के साथ standard I2NP DatabaseStoreMessage भेजना चाहिए।

#### समस्याएं

- डेटा चरण में भी उपयोग किया जा सकता है, I2NP DatabaseStoreMessage के बजाय। उदाहरण के लिए, Bob इसे डेटा चरण शुरू करने के लिए उपयोग कर सकता है।
- क्या इसमें प्रवर्तक के अलावा अन्य routers के लिए RI शामिल करने की अनुमति है, DatabaseStoreMessages के सामान्य प्रतिस्थापन के रूप में, जैसे floodfills द्वारा flooding के लिए?

#### I2NP Message

एक संशोधित हेडर के साथ एक एकल I2NP मैसेज। I2NP मैसेज को ब्लॉक्स के बीच या ChaChaPoly फ्रेम्स के बीच फ्रैगमेंट नहीं किया जा सकता है।

यह मानक NTCP I2NP header से पहले 9 bytes का उपयोग करता है, और header के अंतिम 7 bytes को हटा देता है, निम्नलिखित तरीके से: expiration को 8 से 4 bytes तक छोटा करता है (milliseconds के बजाय seconds, SSU के समान), 2 byte length को हटा देता है (block size - 9 का उपयोग करता है), और one-byte SHA256 checksum को हटा देता है।

```
+----+----+----+----+----+----+----+----+

| 3 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 3 size :: 2 bytes, big endian, size of type + msg id + exp + message to follow I2NP message body size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: I2NP message body
```
#### नोट्स

- कार्यान्वयनकर्ताओं को यह सुनिश्चित करना चाहिए कि जब एक ब्लॉक पढ़ा जाता है, तो विकृत या दुर्भावनापूर्ण डेटा के कारण रीड अगले ब्लॉक में ओवरफ्लो न हो।

#### समाप्ति

Noise एक स्पष्ट समाप्ति संदेश की सिफारिश करता है। मूल NTCP में यह नहीं है। कनेक्शन को बंद कर दें। यह फ्रेम में अंतिम गैर-पैडिंग ब्लॉक होना चाहिए।

```
+----+----+----+----+----+----+----+----+

| 4 | size | valid data frames |

    +----+----+----+----+----+----+----+----+

    :   received | rsn| addl data |

    +----+----+----+----+ + ~ . . . ~ +----+----+----+----+----+----+----+----+

    blk :: 4 size :: 2 bytes, big endian, value = 9 or more valid data frames received :: The number of valid AEAD data phase frames received (current receive nonce value) 0 if error occurs in handshake phase 8 bytes, big endian rsn :: reason, 1 byte: 0: normal close or unspecified 1: termination received 2: idle timeout 3: router shutdown 4: data phase AEAD failure 5: incompatible options 6: incompatible signature type 7: clock skew 8: padding violation 9: AEAD framing error 10: payload format error 11: message 1 error 12: message 2 error 13: message 3 error 14: intra-frame read timeout 15: RI signature verification fail 16: s parameter missing, invalid, or mismatched in RouterInfo 17: banned addl data :: optional, 0 or more bytes, for future expansion, debugging, or reason text. Format unspecified and may vary based on reason code.
```
#### नोट्स

सभी कारण वास्तव में उपयोग नहीं हो सकते हैं, implementation पर निर्भर। Handshake की विफलताओं का परिणाम आमतौर पर TCP RST के साथ close होना होगा। ऊपर handshake message sections में नोट्स देखें। अतिरिक्त सूचीबद्ध कारण consistency, logging, debugging, या यदि policy में बदलाव हो तो के लिए हैं।

#### पैडिंग

यह AEAD frames के अंदर padding के लिए है। संदेश 1 और 2 के लिए padding AEAD frames के बाहर हैं। संदेश 3 और data phase के लिए सभी padding AEAD frames के अंदर हैं।

AEAD के अंदर padding को negotiated parameters का मोटे तौर पर पालन करना चाहिए। Bob ने message 2 में अपने requested tx/rx min/max parameters भेजे थे। Alice ने message 3 में अपने requested tx/rx min/max parameters भेजे थे। Data phase के दौरान updated options भेजे जा सकते हैं। ऊपर दी गई options block जानकारी देखें।

यदि मौजूद है, तो यह frame में अंतिम block होना चाहिए।

```
+----+----+----+----+----+----+----+----+

[|254 |](##SUBST##|254 |) size | padding | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 254 size :: 2 bytes, big endian, size of padding to follow padding :: random data
```
#### नोट्स

- Size = 0 की अनुमति है।
- Padding रणनीतियां TBD।
- न्यूनतम padding TBD।
- केवल-padding frames की अनुमति है।
- Padding defaults TBD।
- Padding parameter बातचीत के लिए options block देखें
- न्यूनतम/अधिकतम padding parameters के लिए options block देखें
- Noise संदेशों को 64KB तक सीमित करता है। यदि अधिक padding आवश्यक है, तो कई frames भेजें।
- बातचीत में तय किए गए padding के उल्लंघन पर router प्रतिक्रिया implementation-dependent है।

#### अन्य ब्लॉक प्रकार

भविष्य की संगतता के लिए implementations को अज्ञात block प्रकारों को नजरअंदाज करना चाहिए, सिवाय message 3 part 2 के, जहां अज्ञात blocks की अनुमति नहीं है।

#### भविष्य का कार्य

- Padding की लंबाई या तो प्रति-संदेश के आधार पर तय की जानी चाहिए और लंबाई वितरण के अनुमान लगाने चाहिए, या random delays जोड़े जाने चाहिए। ये countermeasures DPI का विरोध करने के लिए शामिल किए जाने हैं, क्योंकि संदेश के आकार अन्यथा प्रकट कर देंगे कि I2P traffic को transport protocol द्वारा carried किया जा रहा है। सटीक padding scheme भविष्य के काम का एक क्षेत्र है।

### 5) समाप्ति

कनेक्शन को सामान्य या असामान्य TCP socket close के माध्यम से समाप्त किया जा सकता है, या जैसा कि Noise सुझाता है, एक स्पष्ट termination message के द्वारा। स्पष्ट termination message को ऊपर data phase में परिभाषित किया गया है।

किसी भी सामान्य या असामान्य समाप्ति पर, routers को किसी भी इन-मेमोरी अस्थायी डेटा को शून्य कर देना चाहिए, जिसमें handshake अस्थायी keys, symmetric crypto keys, और संबंधित जानकारी शामिल है।

## प्रकाशित Router जानकारी

### क्षमताएं

रिलीज़ 0.9.50 के अनुसार, NTCP2 addresses में "caps" विकल्प समर्थित है, SSU के समान। "caps" विकल्प में एक या अधिक क्षमताएं प्रकाशित की जा सकती हैं। क्षमताएं किसी भी क्रम में हो सकती हैं, लेकिन implementations में स्थिरता के लिए "46" अनुशंसित क्रम है। दो क्षमताएं परिभाषित हैं:

4: आउटबाउंड IPv4 क्षमता को दर्शाता है। यदि host फील्ड में कोई IP प्रकाशित है, तो यह capability आवश्यक नहीं है। यदि router छुपा हुआ है, या NTCP2 केवल आउटबाउंड है, तो '4' और '6' को एक ही address में संयोजित किया जा सकता है।

6: आउटबाउंड IPv6 क्षमता को दर्शाता है। यदि host फील्ड में कोई IP प्रकाशित है, तो यह capability आवश्यक नहीं है। यदि router छुपा हुआ है, या NTCP2 केवल आउटबाउंड है, तो '4' और '6' को एक ही address में संयोजित किया जा सकता है।

### प्रकाशित पते

प्रकाशित RouterAddress (RouterInfo का हिस्सा) में "NTCP" या "NTCP2" में से कोई एक protocol identifier होगा।

RouterAddress में "host" और "port" विकल्प होने चाहिए, जैसा कि वर्तमान NTCP protocol में है।

RouterAddress में NTCP2 समर्थन को इंगित करने के लिए तीन विकल्प होने चाहिए:

- s=(Base64 key) इस RouterAddress के लिए वर्तमान Noise static public key (s)। मानक I2P Base 64 alphabet का उपयोग करके Base 64 encoded। binary में 32 bytes, Base 64 encoded के रूप में 44 bytes, little-endian X25519 public key।
- i=(Base64 IV) इस RouterAddress के लिए message 1 में X value को encrypt करने के लिए वर्तमान IV। मानक I2P Base 64 alphabet का उपयोग करके Base 64 encoded। binary में 16 bytes, Base 64 encoded के रूप में 24 bytes, big-endian।
- v=2 वर्तमान version (2)। जब "NTCP" के रूप में प्रकाशित हो, तो version 1 के लिए अतिरिक्त समर्थन निहित है। भविष्य के versions के लिए समर्थन comma-separated values के साथ होगा, जैसे v=2,3 Implementation को compatibility की जांच करनी चाहिए, यदि comma मौजूद है तो multiple versions सहित। Comma-separated versions numerical order में होने चाहिए।

Alice को NTCP2 प्रोटोकॉल का उपयोग करके कनेक्ट करने से पहले यह सत्यापित करना होगा कि सभी तीनों विकल्प मौजूद और वैध हैं।

जब "s", "i", और "v" विकल्पों के साथ "NTCP" के रूप में प्रकाशित किया जाता है, तो router को उस host और port पर NTCP और NTCP2 दोनों protocols के लिए आने वाले connections को स्वीकार करना चाहिए, और protocol version को स्वचालित रूप से detect करना चाहिए।

जब "NTCP2" के रूप में "s", "i", और "v" विकल्पों के साथ प्रकाशित किया जाता है, तो router केवल NTCP2 प्रोटोकॉल के लिए उस host और port पर आने वाले कनेक्शन स्वीकार करता है।

यदि कोई router NTCP1 और NTCP2 दोनों connections को support करता है लेकिन incoming connections के लिए automatic version detection implement नहीं करता है, तो उसे "NTCP" और "NTCP2" दोनों addresses को advertise करना चाहिए, और NTCP2 options को केवल "NTCP2" address में include करना चाहिए। router को "NTCP2" address में "NTCP" address की तुलना में कम cost value (उच्च priority) set करनी चाहिए, ताकि NTCP2 को प्राथमिकता मिले।

यदि एक ही RouterInfo में कई NTCP2 RouterAddresses ("NTCP" या "NTCP2" के रूप में) प्रकाशित हैं (अतिरिक्त IP पते या पोर्ट के लिए), तो समान पोर्ट निर्दिष्ट करने वाले सभी पतों में समान NTCP2 विकल्प और मान होने चाहिए। विशेष रूप से, सभी में समान static key और iv होना चाहिए।

### अप्रकाशित NTCP2 पता

यदि Alice आने वाले कनेक्शन के लिए अपना NTCP2 पता ("NTCP" या "NTCP2" के रूप में) प्रकाशित नहीं करती है, तो उसे केवल अपनी static key और NTCP2 version वाला एक "NTCP2" router address प्रकाशित करना होगा, ताकि Bob message 3 part 2 में Alice की RouterInfo प्राप्त करने के बाद key को validate कर सके।

- s=(Base64 key) प्रकाशित पतों के लिए ऊपर परिभाषित के अनुसार।
- v=2 प्रकाशित पतों के लिए ऊपर परिभाषित के अनुसार।

इस router address में "i", "host" या "port" विकल्प शामिल नहीं होंगे, क्योंकि ये outbound NTCP2 connections के लिए आवश्यक नहीं हैं। इस address के लिए प्रकाशित cost का कोई खास मतलब नहीं है, क्योंकि यह केवल inbound है; हालांकि, अगर cost को अन्य addresses की तुलना में अधिक (कम priority) सेट किया जाए तो यह अन्य routers के लिए सहायक हो सकता है। सुझाया गया मान 14 है।

Alice मौजूदा प्रकाशित "NTCP" पते में केवल "s" और "v" विकल्प भी जोड़ सकती है।

### पब्लिक की और IV रोटेशन

RouterInfos की caching के कारण, router को static public key या IV को rotate नहीं करना चाहिए जब तक router चालू है, चाहे वह published address में हो या न हो। Router को इस key और IV को persistently store करना चाहिए ताकि तत्काल restart के बाद पुन: उपयोग के लिए उपलब्ध हो, जिससे incoming connections काम करते रहें और restart times exposed न हों। Router को last-shutdown time को persistently store करना चाहिए, या अन्यथा निर्धारित करना चाहिए, ताकि startup पर पिछले downtime की गणना की जा सके।

रीस्टार्ट समय को उजागर करने की चिंताओं के अधीन, router इस key या IV को स्टार्टअप पर rotate कर सकते हैं यदि router पहले कुछ समय के लिए बंद था (कम से कम कुछ घंटे)।

यदि router के पास कोई प्रकाशित NTCP2 RouterAddresses हैं (NTCP या NTCP2 के रूप में), तो rotation से पहले न्यूनतम downtime बहुत अधिक होना चाहिए, उदाहरण के लिए एक महीना, जब तक कि स्थानीय IP address नहीं बदला हो या router "rekeys" न करे।

यदि router के पास कोई प्रकाशित SSU RouterAddresses हैं, लेकिन NTCP2 (NTCP या NTCP2 के रूप में) नहीं है, तो rotation से पहले न्यूनतम downtime अधिक होना चाहिए, उदाहरण के लिए एक दिन, जब तक कि स्थानीय IP address नहीं बदला हो या router "rekeys" न करे। यह तब भी लागू होता है जब प्रकाशित SSU address में introducers हों।

यदि router के पास कोई प्रकाशित RouterAddresses (NTCP, NTCP2, या SSU) नहीं हैं, तो rotation से पहले न्यूनतम downtime केवल दो घंटे का हो सकता है, भले ही IP address बदल जाए, जब तक कि router "rekeys" न करे।

यदि router एक अलग Router Hash के लिए "rekeys" करता है, तो उसे एक नया noise key और IV भी generate करना चाहिए।

Implementations को यह ध्यान रखना चाहिए कि static public key या IV को बदलने से उन routers से आने वाले NTCP2 connections रुक जाएंगे जिन्होंने पुराना RouterInfo cached किया है। RouterInfo publishing, tunnel peer selection (OBGW और IB closest hop दोनों सहित), zero-hop tunnel selection, transport selection, और अन्य implementation रणनीतियों को इस बात का ध्यान रखना चाहिए।

IV rotation उन्हीं नियमों के अधीन है जो key rotation के हैं, सिवाय इसके कि IVs केवल प्रकाशित RouterAddresses में मौजूद होते हैं, इसलिए छुपे हुए या firewalled routers के लिए कोई IV नहीं होता। यदि कुछ भी बदलता है (version, key, options?) तो यह सिफारिश की जाती है कि IV भी बदला जाए।

नोट: rekeying से पहले न्यूनतम डाउनटाइम को नेटवर्क स्वास्थ्य सुनिश्चित करने के लिए संशोधित किया जा सकता है, और मध्यम समय के लिए बंद router द्वारा reseeding को रोकने के लिए।

## संस्करण का पता लगाना

जब "NTCP" के रूप में प्रकाशित किया जाता है, तो router को आने वाले कनेक्शन के लिए स्वचालित रूप से protocol version का पता लगाना चाहिए।

यह पहचान implementation-dependent है, लेकिन यहाँ कुछ सामान्य मार्गदर्शन है।

आने वाले NTCP कनेक्शन का version detect करने के लिए, Bob निम्नलिखित तरीके से आगे बढ़ता है:

- कम से कम 64 bytes की प्रतीक्षा करें (न्यूनतम NTCP2 message 1 size)

- यदि प्रारंभिक प्राप्त डेटा 288 या अधिक बाइट्स है, तो आने वाला कनेक्शन version 1 है।

- यदि 288 बाइट्स से कम है, तो या तो

> - अधिक डेटा के लिए थोड़ा समय प्रतीक्षा करें (व्यापक NTCP2 अपनाने से पहले अच्छी रणनीति) यदि कम से कम 288 कुल प्राप्त हुआ है, तो यह NTCP 1 है।   >   > - संस्करण 2 के रूप में डिकोडिंग के पहले चरणों का प्रयास करें, यदि यह विफल हो जाता है, तो अधिक डेटा के लिए थोड़ा समय प्रतीक्षा करें (व्यापक NTCP2 अपनाने के बाद अच्छी रणनीति)   >   >   > - SessionRequest पैकेट के पहले 32 बाइट्स (X key) को key RH_B के साथ AES-256 का उपयोग करके डिक्रिप्ट करें।   >   > - वक्र पर एक वैध बिंदु की पुष्टि करें। यदि यह विफल हो जाता है, तो NTCP 1 के लिए अधिक डेटा के लिए थोड़ा समय प्रतीक्षा करें   >   > - AEAD frame की पुष्टि करें। यदि यह विफल हो जाता है, तो NTCP 1 के लिए अधिक डेटा के लिए थोड़ा समय प्रतीक्षा करें

ध्यान दें कि यदि हम NTCP 1 पर सक्रिय TCP segmentation हमलों का पता लगाते हैं तो अतिरिक्त रणनीतियों या परिवर्तनों की सिफारिश की जा सकती है।

तेज़ version detection और handshaking को सुविधाजनक बनाने के लिए, implementations को यह सुनिश्चित करना होगा कि Alice पहले message की संपूर्ण contents को buffer करे और फिर एक साथ flush करे, padding सहित। इससे इस बात की संभावना बढ़ जाती है कि data एक single TCP packet में contained होगा (जब तक कि OS या middleboxes द्वारा segmented न हो), और Bob द्वारा एक साथ receive किया जाएगा। यह efficiency के लिए भी है और random padding की effectiveness को ensure करने के लिए भी। यह NTCP और NTCP2 दोनों handshakes पर लागू होता है।

## रूपांतर, फॉलबैक, और सामान्य समस्याएं

- यदि Alice और Bob दोनों NTCP2 को सपोर्ट करते हैं, तो Alice को NTCP2 के साथ कनेक्ट करना चाहिए।
- यदि Alice किसी भी कारण से NTCP2 का उपयोग करके Bob से कनेक्ट करने में असफल हो जाती है, तो कनेक्शन असफल हो जाता है। Alice NTCP 1 का उपयोग करके पुनः प्रयास नहीं कर सकती।

## क्लॉक स्क्यू दिशानिर्देश

Peer timestamps पहले दो handshake messages में शामिल किए जाते हैं, Session Request और Session Created। दो peers के बीच +/- 60 सेकंड से अधिक का clock skew आमतौर पर घातक होता है। यदि Bob को लगता है कि उसकी local clock खराब है, तो वह calculated skew या किसी external source का उपयोग करके अपनी clock को adjust कर सकता है। अन्यथा, Bob को connection को बंद करने के बजाय Session Created के साथ reply करना चाहिए, भले ही maximum skew exceed हो गया हो। यह Alice को Bob का timestamp प्राप्त करने और skew को calculate करने की अनुमति देता है, और यदि आवश्यक हो तो कार्रवाई करने की। इस समय Bob के पास Alice की router identity नहीं है, लेकिन resources को संरक्षित करने के लिए, Bob के लिए यह वांछनीय हो सकता है कि वह Alice के IP से आने वाले connections को कुछ समय के लिए ban कर दे, या excessive skew के साथ repeated connection attempts के बाद।

Alice को RTT का आधा घटाकर गणना किए गए clock skew को समायोजित करना चाहिए। यदि Alice को लगता है कि उसकी स्थानीय clock खराब है, तो वह गणना किए गए skew या किसी बाहरी स्रोत का उपयोग करके अपनी clock को समायोजित कर सकती है। यदि Alice को लगता है कि Bob की clock खराब है, तो वह Bob को कुछ समय के लिए ban कर सकती है। किसी भी स्थिति में, Alice को कनेक्शन बंद कर देना चाहिए।

यदि Alice Session Confirmed के साथ जवाब देती है (संभवतः इसलिए कि skew 60s सीमा के बहुत करीब है, और RTT के कारण Alice और Bob की गणनाएं बिल्कुल समान नहीं हैं), तो Bob को आधे RTT को घटाकर गणना किए गए clock skew को समायोजित करना चाहिए। यदि समायोजित clock skew अधिकतम सीमा से अधिक हो जाता है, तो Bob को clock skew reason code वाले Disconnect संदेश के साथ जवाब देना चाहिए और कनेक्शन बंद कर देना चाहिए। इस बिंदु पर, Bob के पास Alice की router identity है, और वह कुछ समय के लिए Alice को प्रतिबंधित कर सकता है।

## संदर्भ

- [सामान्य संरचनाएं](/docs/specs/common-structures)
- [I2NP](/docs/specs/i2np)
- [Network Database](/docs/overview/network-database)
- [NOISE - Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP](/docs/transport/ntcp)
- [Prop104](/proposals/104-tls-transport)
- [Prop109](/proposals/109-pt-transport)
- [Prop111](/proposals/111-ntcp-2)
- [RFC-2104 - HMAC](https://tools.ietf.org/html/rfc2104)
- [RFC-3526 - DH Groups](https://tools.ietf.org/html/rfc3526)
- [RFC-6151](https://tools.ietf.org/html/rfc6151)
- [RFC-7539 - ChaCha20-Poly1305](https://tools.ietf.org/html/rfc7539)
- [RFC-7748 - X25519](https://tools.ietf.org/html/rfc7748)
- [RFC-7905](https://tools.ietf.org/html/rfc7905)
- [SipHash](https://www.131002.net/siphash/)
- [SSU](/docs/transport/ssu)
- **[STS]** Diffie, W.; van Oorschot P. C.; Wiener M. J., प्रमाणीकरण और प्रमाणित कुंजी एक्सचेंज

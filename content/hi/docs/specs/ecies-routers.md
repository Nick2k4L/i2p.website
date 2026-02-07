---
title: "ECIES-X25519 Router संदेश"
description: "X25519 का उपयोग करते हुए ECIES routers के लिए Garlic message encryption की विशिष्टता"
slug: "ecies-routers"
category: "प्रोटोकॉल"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## नोट

रिलीज़ 0.9.49 से समर्थित। नेटवर्क डिप्लॉयमेंट और परीक्षण प्रगति में है। मामूली संशोधन के अधीन। देखें [proposal 156](/proposals/156-ecies-routers)।

## अवलोकन

यह दस्तावेज़ ECIES routers के लिए Garlic message encryption को निर्दिष्ट करता है, जो [ECIES-X25519](/docs/specs/ecies) द्वारा शुरू किए गए crypto primitives का उपयोग करता है। यह routers को ElGamal से ECIES-X25519 keys में बदलने के लिए समग्र [proposal 156](/proposals/156-ecies-routers) का एक हिस्सा है। यह specification release 0.9.49 के अनुसार implemented है।

ECIES routers के लिए आवश्यक सभी परिवर्तनों का अवलोकन देखने के लिए, [proposal 156](/proposals/156-ecies-routers) देखें। ECIES-X25519 गंतव्यों के लिए Garlic Messages के लिए, [ECIES-X25519](/docs/specs/ecies) देखें।

### क्रिप्टोग्राफिक प्रिमिटिव्स

इस विनिर्देश को लागू करने के लिए आवश्यक आदिम तत्व हैं:

- AES-256-CBC जैसा कि [Cryptography](/docs/specs/cryptography) में है
- STREAM ChaCha20/Poly1305 functions: ENCRYPT(k, n, plaintext, ad) और DECRYPT(k, n, ciphertext, ad) - जैसा कि [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), और [RFC-7539](https://tools.ietf.org/html/rfc7539) में है
- X25519 DH functions - जैसा कि [NTCP2](/docs/specs/ntcp2) और [ECIES-X25519](/docs/specs/ecies) में है
- HKDF(salt, ikm, info, n) - जैसा कि [NTCP2](/docs/specs/ntcp2) और [ECIES-X25519](/docs/specs/ecies) में है

अन्यत्र परिभाषित अन्य Noise फ़ंक्शन:

- MixHash(d) - जैसा कि [NTCP2](/docs/specs/ntcp2) और [ECIES-X25519](/docs/specs/ecies) में है
- MixKey(d) - जैसा कि [NTCP2](/docs/specs/ntcp2) और [ECIES-X25519](/docs/specs/ecies) में है

## डिज़ाइन

ECIES Router SKM को Destinations के लिए [ECIES](/docs/specs/ecies) में निर्दिष्ट पूर्ण Ratchet SKM की आवश्यकता नहीं है। IK pattern का उपयोग करने वाले गैर-अज्ञात संदेशों की कोई आवश्यकता नहीं है। threat model में Elligator2-encoded ephemeral keys की आवश्यकता नहीं है।

इसलिए, router SKM Noise "N" पैटर्न का उपयोग करेगा, जैसा कि tunnel building के लिए [Prop152](/proposals/152-ecies-tunnels) में निर्दिष्ट है। यह Destinations के लिए [ECIES](/docs/specs/ecies) में निर्दिष्ट समान payload format का उपयोग करेगा। [ECIES](/docs/specs/ecies) में निर्दिष्ट IK का zero static key (no binding या session) mode का उपयोग नहीं किया जाएगा।

यदि lookup में अनुरोध किया गया हो तो lookups के जवाब ratchet tag के साथ एन्क्रिप्टेड होंगे। यह [Prop154](/proposals/154-ecies-lookups) में प्रलेखित है, अब [I2NP](/docs/specs/i2np) में निर्दिष्ट है।

यह डिज़ाइन router को एक single ECIES Session Key Manager रखने की सुविधा देता है। Destinations के लिए [ECIES](/docs/specs/ecies) में वर्णित "dual key" Session Key Managers चलाने की कोई आवश्यकता नहीं है। Routers के पास केवल एक public key होती है।

एक ECIES router में ElGamal static key नहीं होती है। router को अभी भी ElGamal का implementation चाहिए होता है ताकि वह ElGamal routers के माध्यम से tunnel बना सके और ElGamal routers को encrypted messages भेज सके।

एक ECIES router को pre-0.9.46 floodfill routers से NetDB lookups के उत्तर के रूप में प्राप्त ElGamal-tagged messages को receive करने के लिए एक partial ElGamal Session Key Manager की आवश्यकता हो सकती है, क्योंकि उन routers में [Prop152](/proposals/152-ecies-tunnels) में निर्दिष्ट ECIES-tagged replies का implementation नहीं है। यदि ऐसा नहीं है, तो एक ECIES router pre-0.9.46 floodfill router से encrypted reply का अनुरोध नहीं कर सकता है।

यह वैकल्पिक है। निर्णय विभिन्न I2P implementations में भिन्न हो सकता है और इस बात पर निर्भर हो सकता है कि नेटवर्क का कितना हिस्सा 0.9.46 या उससे उच्चतर संस्करण में अपग्रेड हो चुका है। इस तारीख तक, नेटवर्क का लगभग 85% हिस्सा 0.9.46 या उससे उच्चतर संस्करण पर है।

### Noise Protocol Framework

यह विनिर्देश [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (संशोधन 34, 2018-07-11) पर आधारित आवश्यकताओं को प्रदान करता है। Noise की भाषा में, Alice प्रारंभकर्ता है, और Bob उत्तरदाता है।

यह Noise protocol Noise_N_25519_ChaChaPoly_SHA256 पर आधारित है। यह Noise protocol निम्नलिखित primitives का उपयोग करता है:

- **One-Way Handshake Pattern: N** - Alice अपनी static key को Bob (N) को transmit नहीं करती
- **DH Function: X25519** - X25519 DH जिसमें 32 bytes की key length है जैसा कि [RFC-7748](https://tools.ietf.org/html/rfc7748) में specified है।
- **Cipher Function: ChaChaPoly** - AEAD_CHACHA20_POLY1305 जैसा कि [RFC-7539](https://tools.ietf.org/html/rfc7539) section 2.8 में specified है। 12 byte nonce, जिसके पहले 4 bytes zero पर set हैं। यह [NTCP2](/docs/specs/ntcp2) में उपयोग किए गए के समान है।
- **Hash Function: SHA256** - Standard 32-byte hash, जो पहले से ही I2P में व्यापक रूप से उपयोग किया जाता है।

### हैंडशेक पैटर्न

Handshakes [Noise](https://noiseprotocol.org/noise.html) handshake patterns का उपयोग करते हैं।

निम्नलिखित अक्षर मैपिंग का उपयोग किया जाता है:

- e = एक-बार का अस्थायी key
- s = स्थैतिक key
- p = संदेश payload

build request Noise N pattern के समान ही है। यह [NTCP2](/docs/specs/ntcp2) में उपयोग किए जाने वाले XK pattern के पहले (Session Request) संदेश के भी समान है।

```
<- s
  ...
  e es p ->
```
### संदेश एन्क्रिप्शन

Messages को बनाया जाता है और target router के लिए asymmetrically encrypted किया जाता है। Messages का यह asymmetric encryption वर्तमान में ElGamal है जैसा कि [Cryptography](/docs/specs/cryptography) में परिभाषित है और इसमें SHA-256 checksum होता है। यह design forward-secret नहीं है।

ECIES डिज़ाइन एक-तरफ़ा Noise pattern "N" का उपयोग करता है जिसमें ECIES-X25519 ephemeral-static DH, एक HKDF, और ChaCha20/Poly1305 AEAD शामिल है जो forward secrecy, integrity, और authentication के लिए है। Alice गुमनाम संदेश भेजने वाला है, एक router या destination। लक्षित ECIES router Bob है।

### उत्तर एन्क्रिप्शन

उत्तर इस प्रोटोकॉल का हिस्सा नहीं हैं, क्योंकि Alice अज्ञात है। reply keys, यदि कोई हैं, तो request message में bundled होते हैं। Database Lookup Messages के लिए [I2NP specification](/docs/specs/i2np) देखें।

Database Lookup संदेशों के उत्तर Database Store या Database Search Reply संदेश हैं। ये Existing Session संदेशों के रूप में 32-byte reply key और 8-byte reply tag के साथ एन्क्रिप्ट किए जाते हैं जैसा कि [I2NP](/docs/specs/i2np) और [Prop154](/proposals/154-ecies-lookups) में निर्दिष्ट है।

Database Store संदेशों के लिए कोई स्पष्ट उत्तर नहीं होते हैं। भेजने वाला अपने लिए एक Garlic Message के रूप में अपना उत्तर बंडल कर सकता है, जिसमें एक Delivery Status संदेश होता है।

## विनिर्देश

X25519: [ECIES](/docs/specs/ecies) देखें।

Router Identity और Key Certificate: देखें [Common Structures](/docs/specs/common-structures)।

### अनुरोध एन्क्रिप्शन

request encryption वही है जो [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) और [Prop152](/proposals/152-ecies-tunnels) में निर्दिष्ट है, जो Noise "N" pattern का उपयोग करता है।

यदि lookup में अनुरोध किया गया हो तो lookup के उत्तर ratchet tag के साथ एन्क्रिप्ट किए जाएंगे। Database Lookup अनुरोध संदेशों में 32-byte reply key और 8-byte reply tag होते हैं जैसा कि [I2NP](/docs/specs/i2np) और [Prop154](/proposals/154-ecies-lookups) में निर्दिष्ट है। key और tag का उपयोग उत्तर को एन्क्रिप्ट करने के लिए किया जाता है।

Tag sets नहीं बनाए जाते हैं। ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) और [ECIES](/docs/specs/ecies) में निर्दिष्ट zero static key scheme का उपयोग नहीं किया जाएगा। Ephemeral keys को Elligator2-encoded नहीं किया जाएगा।

आम तौर पर, ये New Session संदेश होंगे और शून्य static key (कोई binding या session नहीं) के साथ भेजे जाएंगे, क्योंकि संदेश का भेजने वाला anonymous होता है।

#### प्रारंभिक ck और h के लिए KDF

यह pattern "N" के लिए मानक [Noise](https://noiseprotocol.org/noise.html) है जो एक मानक प्रोटोकॉल नाम के साथ है। यह tunnel build messages के लिए [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) और [Prop152](/proposals/152-ecies-tunnels) में निर्दिष्ट के समान है।

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
#### संदेश के लिए KDF

संदेश निर्माता प्रत्येक संदेश के लिए एक ephemeral X25519 keypair उत्पन्न करते हैं। Ephemeral keys प्रत्येक संदेश के लिए अद्वितीय होनी चाहिए। यह tunnel build संदेशों के लिए [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) और [Prop152](/proposals/152-ecies-tunnels) में निर्दिष्ट के समान है।

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
#### पेलोड

पेलोड वही ब्लॉक फॉर्मेट है जो [ECIES](/docs/specs/ecies) और [Prop144](/proposals/144-ecies-x25519-aead-ratchet) में परिभाषित है। रिप्ले रोकथाम के लिए सभी संदेशों में DateTime ब्लॉक होना आवश्यक है।

## कार्यान्वयन टिप्पणियाँ

- पुराने routers, router के encryption type की जांच नहीं करते और ElGamal-encrypted संदेश भेजते हैं। कुछ हालिया routers में बग होते हैं और वे विभिन्न प्रकार के गलत संदेश भेजते हैं। implementers को CPU उपयोग कम करने के लिए, यदि संभव हो तो DH operation से पहले इन records का पता लगाना और उन्हें reject करना चाहिए।

## संदर्भ

- [सामान्य संरचनाएं](/docs/specs/common-structures)
- [क्रिप्टोग्राफी](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies)

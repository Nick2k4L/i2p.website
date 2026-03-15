---
title: "SSU2 विनिर्देश"
description: "सुरक्षित अर्ध-विश्वसनीय UDP परिवहन प्रोटोकॉल संस्करण 2"
slug: "ssu2"
category: "ट्रांसपोर्ट"
lastUpdated: "2026-03"
accurateFor: "0.9.69"
---

## स्थिति

पूर्णतः पूर्ण। अतिरिक्त पृष्ठभूमि और लक्ष्यों के लिए [Prop159](/proposals/159-ssu2) देखें, जिसमें सुरक्षा विश्लेषण, खतरा मॉडल, SSU 1 सुरक्षा और समस्याओं की समीक्षा, और QUIC विनिर्देशों के अंश शामिल हैं।

रोलआउट योजना:

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
बेसिक सेशन में handshake और डेटा चरण शामिल है। विस्तारित प्रोटोकॉल में relay और peer test शामिल हैं।

## अवलोकन

यह विशिष्टता एक प्रमाणित कुंजी समझौता प्रोटोकॉल परिभाषित करती है जो [SSU](/docs/transport/ssu) की विभिन्न प्रकार की स्वचालित पहचान और हमलों के प्रति प्रतिरोध में सुधार करने के लिए है।

अन्य I2P transports की तरह, SSU2 को I2NP संदेशों के point-to-point (router-to-router) transport के लिए परिभाषित किया गया है। यह एक सामान्य-उद्देश्य डेटा पाइप नहीं है। [SSU](/docs/transport/ssu) की तरह, यह दो अतिरिक्त सेवाएं भी प्रदान करता है: NAT traversal के लिए Relaying, और inbound reachability का निर्धारण करने के लिए Peer Testing। यह एक तीसरी सेवा भी प्रदान करता है, जो SSU में नहीं है, connection migration के लिए जब कोई peer अपना IP या port बदलता है।

## डिज़ाइन अवलोकन

### सारांश

हम प्रेरणा, मार्गदर्शन और कोड पुन:उपयोग के लिए कई मौजूदा प्रोटोकॉल पर निर्भर करते हैं, जो I2P के भीतर और बाहरी मानकों दोनों में हैं:

- Threat models: NTCP2 [NTCP2](/docs/specs/ntcp2) से, UDP transport के लिए प्रासंगिक महत्वपूर्ण अतिरिक्त खतरों के साथ जैसा कि QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001) द्वारा विश्लेषित किया गया है।
- Cryptographic choices: [NTCP2](/docs/specs/ntcp2) से।
- Handshake: [NTCP2](/docs/specs/ntcp2) और [NOISE](https://noiseprotocol.org/noise.html) से Noise XK। UDP द्वारा प्रदान की गई encapsulation (अंतर्निहित संदेश सीमाओं) के कारण NTCP2 में महत्वपूर्ण सरलीकरण संभव हैं।
- Handshake ephemeral key obfuscation: [NTCP2](/docs/specs/ntcp2) से अनुकूलित लेकिन AES के बजाय [ECIES](/docs/specs/ecies) से ChaCha20 का उपयोग करके।
- Packet headers: WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) और QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001) से अनुकूलित।
- Packet header obfuscation: [NTCP2](/docs/specs/ntcp2) से अनुकूलित लेकिन AES के बजाय [ECIES](/docs/specs/ecies) से ChaCha20 का उपयोग करके।
- Packet header protection: QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) और [Nonces](https://eprint.iacr.org/2019/624.pdf) से अनुकूलित।
- Headers को AEAD associated data के रूप में उपयोग किया गया है जैसा कि [ECIES](/docs/specs/ecies) में है।
- Packet numbering: WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) और QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001) से अनुकूलित।
- Messages: [SSU](/docs/transport/ssu) से अनुकूलित।
- I2NP Fragmentation: [SSU](/docs/transport/ssu) से अनुकूलित।
- Relay और Peer Testing: [SSU](/docs/transport/ssu) से अनुकूलित।
- Relay और Peer Test data के Signatures: common structures spec [Common](/docs/specs/common-structures) से।
- Block format: [NTCP2](/docs/specs/ntcp2) और [ECIES](/docs/specs/ecies) से।
- Padding और options: [NTCP2](/docs/specs/ntcp2) और [ECIES](/docs/specs/ecies) से।
- Acks, nacks: QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) से अनुकूलित।
- Flow control: TBD

कोई नए cryptographic primitives नहीं हैं जो पहले I2P में उपयोग नहीं किए गए हों।

### डिलीवरी गारंटी

अन्य I2P transports NTCP, NTCP2, और SSU 1 की तरह, यह transport bytes के in-order stream की delivery के लिए एक सामान्य-उद्देश्य सुविधा नहीं है। यह I2NP messages के transport के लिए डिज़ाइन किया गया है। कोई "stream" abstraction प्रदान नहीं की गई है।

इसके अलावा, SSU के लिए, इसमें peer-facilitated NAT traversal और reachability की जांच (inbound connections) के लिए अतिरिक्त सुविधाएं शामिल हैं।

SSU 1 के लिए, यह I2NP संदेशों की क्रमबद्ध डिलीवरी प्रदान नहीं करता है। न ही यह I2NP संदेशों की गारंटीशुदा डिलीवरी प्रदान करता है। दक्षता के लिए, या UDP डेटाग्राम की अव्यवस्थित डिलीवरी या उन डेटाग्राम के नुकसान के कारण, I2NP संदेश दूर के छोर तक अव्यवस्थित रूप से पहुंचाए जा सकते हैं, या बिल्कुल भी नहीं पहुंचाए जा सकते हैं। यदि आवश्यक हो तो एक I2NP संदेश को कई बार पुनः प्रसारित किया जा सकता है, लेकिन पूरे कनेक्शन को डिस्कनेक्ट किए बिना अंततः डिलीवरी विफल हो सकती है। इसके अलावा, नए I2NP संदेश भेजे जाना जारी रह सकते हैं जबकि अन्य I2NP संदेशों के लिए पुनः प्रसारण (हानि रिकवरी) हो रही हो।

यह protocol I2NP संदेशों की डुप्लिकेट डिलीवरी को पूरी तरह से नहीं रोकता है। router को I2NP expiration को लागू करना चाहिए और I2NP message ID के आधार पर Bloom filter या अन्य mechanism का उपयोग करना चाहिए। नीचे I2NP Message Duplication सेक्शन देखें।

### Noise Protocol Framework

यह स्पेसिफिकेशन Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revision 33, 2017-10-04) पर आधारित आवश्यकताओं को प्रदान करती है। Noise में Station-To-Station protocol [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol) के समान गुण हैं, जो [SSU](/docs/transport/ssu) protocol का आधार है। Noise की भाषा में, Alice initiator है, और Bob responder है।

SSU2 Noise protocol Noise_XK_25519_ChaChaPoly_SHA256 पर आधारित है। (प्रारंभिक key derivation function के लिए वास्तविक identifier "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" है जो I2P extensions को दर्शाता है - नीचे KDF 1 section देखें)

नोट: यह पहचानकर्ता NTCP2 के लिए उपयोग किए जाने वाले से अलग है, क्योंकि तीनों handshake संदेश header को associated data के रूप में उपयोग करते हैं।

यह Noise प्रोटोकॉल निम्नलिखित आदिम तत्वों (primitives) का उपयोग करता है:

- Handshake Pattern: XK Alice अपनी key Bob को transmit करती है (X) Alice को Bob की static key पहले से पता है (K)
- DH Function: X25519 X25519 DH जिसकी key length 32 bytes है जैसा कि [RFC-7748](https://tools.ietf.org/html/rfc7748) में specified है।
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305 जैसा कि [RFC-7539](https://tools.ietf.org/html/rfc7539) section 2.8 में specified है। 12 byte nonce, जिसके पहले 4 bytes zero पर set हैं।
- Hash Function: SHA256 मानक 32-byte hash, जो I2P में पहले से व्यापक रूप से उपयोग किया जा रहा है।

### फ्रेमवर्क में जोड़े गए तत्व

यह विनिर्देश Noise_XK_25519_ChaChaPoly_SHA256 में निम्नलिखित संवर्धनों को परिभाषित करता है। ये आम तौर पर [NOISE](https://noiseprotocol.org/noise.html) अनुभाग 13 की दिशानिर्देशों का पालन करते हैं।

1) Handshake संदेश (Session Request, Created, Confirmed) में 16 या 32 बाइट का header शामिल होता है। 2) Handshake संदेश (Session Request, Created, Confirmed) के headers को encryption/decryption से पहले mixHash() के इनपुट के रूप में उपयोग किया जाता है ताकि headers को संदेश से जोड़ा जा सके। 3) Headers encrypted और सुरक्षित होते हैं। 4) Cleartext ephemeral keys को ज्ञात key और IV का उपयोग करते हुए ChaCha20 encryption के साथ obfuscate किया जाता है। यह elligator2 से तेज़ है। 5) Payload format संदेश 1, 2, और data phase के लिए परिभाषित है। बेशक, यह Noise में परिभाषित नहीं है।

डेटा फेज Noise डेटा फेज के समान, लेकिन उसके साथ संगत नहीं, एन्क्रिप्शन का उपयोग करता है।

### सेशन स्थापना

हम उपयोग किए गए cryptographic building blocks के अनुरूप निम्नलिखित functions को परिभाषित करते हैं।

#### लंबा हेडर

ZEROLEN

#### संक्षिप्त हेडर

:   शून्य-लंबाई बाइट array

#### कनेक्शन ID नंबरिंग

H(p, d)

#### पैकेट नंबरिंग

:   SHA-256 hash function जो एक personalization string p और data d लेता है, और 32 bytes की length का output देता है। जैसा कि [NOISE](https://noiseprotocol.org/noise.html) में परिभाषित है। || का मतलब नीचे append करना है।

## परिभाषाएं

MixHash(d)

:   SHA-256 hash function जो पिछले hash h और नए data d को लेता है, और 32 bytes की लंबाई का output उत्पन्न करता है। नीचे || का मतलब append करना है।

STREAM

:   [RFC-7539](https://tools.ietf.org/html/rfc7539) में निर्दिष्ट ChaCha20/Poly1305 AEAD। S_KEY_LEN = 32 और S_IV_LEN = 12।

DH

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

:   X25519 पब्लिक की एग्रीमेंट सिस्टम। 32 बाइट्स की प्राइवेट कीज़, 32 बाइट्स की पब्लिक कीज़, 32 बाइट्स का आउटपुट देता है। इसके निम्नलिखित फ़ंक्शन हैं:

HKDF(salt, ikm, info, n)

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

:   एक क्रिप्टोग्राफिक key derivation function जो कुछ input key material ikm (जिसमें अच्छी entropy होनी चाहिए लेकिन uniformly random string होना आवश्यक नहीं है), 32 bytes लंबाई का एक salt, और एक context-specific 'info' value लेता है, और n bytes का output उत्पन्न करता है जो key material के रूप में उपयोग के लिए उपयुक्त होता है।

MixKey(d)

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

:   पिछली chainKey और नए डेटा d के साथ HKDF() का उपयोग करें, और नई chainKey और k सेट करें। जैसा कि [NOISE](https://noiseprotocol.org/noise.html) में परिभाषित है।

प्रत्येक UDP datagram में बिल्कुल एक message होता है। datagram की लंबाई (IP और UDP headers के बाद) message की लंबाई होती है। Padding, यदि कोई है, तो वह message के अंदर एक padding block में समाहित होता है। इस document में, हम "datagram" और "packet" शब्दों का उपयोग मुख्यतः एक दूसरे के स्थान पर करते हैं। प्रत्येक datagram (या packet) में एक single message होता है (QUIC के विपरीत, जहाँ एक datagram में कई QUIC packets हो सकते हैं)। "packet header" IP/UDP header के बाद का हिस्सा है।

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

अपवाद: Session Confirmed संदेश इस मामले में अनोखा है कि यह कई packets में विभाजित हो सकता है। अधिक जानकारी के लिए नीचे Session Confirmed Fragmentation अनुभाग देखें।

सभी SSU2 संदेश कम से कम 40 बाइट्स लंबाई के होते हैं। 1-39 बाइट्स लंबाई का कोई भी संदेश अमान्य है। सभी SSU2 संदेश 1472 (IPv4) या 1452 (IPv6) बाइट्स लंबाई से कम या बराबर होते हैं। संदेश प्रारूप Noise संदेशों पर आधारित है, जिसमें फ्रेमिंग और अविभेद्यता के लिए संशोधन हैं। मानक Noise पुस्तकालयों का उपयोग करने वाले implementation को प्राप्त संदेशों को मानक Noise संदेश प्रारूप में पूर्व-प्रसंस्करण करना होगा। सभी एन्क्रिप्टेड फ़ील्ड AEAD ciphertext हैं।

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

निम्नलिखित संदेश परिभाषित हैं:

मानक स्थापना अनुक्रम, जब Alice के पास Bob से पहले प्राप्त एक वैध टोकन है, निम्नलिखित है:

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## संदेश

जब Alice के पास एक वैध टोकन नहीं है, तो स्थापना अनुक्रम निम्नलिखित है:

जब Alice को लगता है कि उसके पास एक वैध टोकन है, लेकिन Bob इसे अस्वीकार कर देता है (शायद इसलिए कि Bob पुनः आरंभ हुआ है), तो स्थापना अनुक्रम निम्नलिखित है:

Bob एक Session या Token Request को अस्वीकार कर सकता है एक Retry message के साथ जवाब देकर जिसमें एक कारण कोड के साथ Termination block होता है। कारण कोड के आधार पर, Alice को कुछ समय तक दूसरी request का प्रयास नहीं करना चाहिए:

Noise शब्दावली का उपयोग करते हुए, स्थापना और डेटा अनुक्रम निम्नलिखित है: (Payload Security Properties)

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
### पैकेट हेडर

एक बार session स्थापित हो जाने के बाद, Alice और Bob Data messages का आदान-प्रदान कर सकते हैं।

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
सभी packets एक obfuscated (encrypted) header के साथ शुरू होते हैं। दो header प्रकार हैं, लंबा और छोटा। ध्यान दें कि पहले 13 bytes (Destination Connection ID, packet number, और type) सभी headers के लिए समान हैं।

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
लंबा header 32 बाइट्स का है। इसका उपयोग session बनाने से पहले Token Request, SessionRequest, SessionCreated, और Retry के लिए किया जाता है। इसका उपयोग out-of-session Peer Test और Hole Punch संदेशों के लिए भी किया जाता है।

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
हेडर एन्क्रिप्शन से पहले:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
छोटा header 16 bytes का होता है। यह Session Created और Data messages के लिए उपयोग किया जाता है। अप्रमाणित संदेश जैसे Session Request, Retry, और Peer Test हमेशा लंबे header का उपयोग करेंगे।

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
16 bytes आवश्यक है, क्योंकि receiver को message type प्राप्त करने के लिए पहले 16 bytes को decrypt करना होता है, और फिर यदि यह वास्तव में एक long header है, जैसा कि message type द्वारा संकेत दिया गया है, तो उसे अतिरिक्त 16 bytes को decrypt करना होता है।

### पैकेट अखंडता

Session Confirmed के लिए, header encryption से पहले:

#### हेडर बाइंडिंग

frag फ़ील्ड के बारे में अधिक जानकारी के लिए नीचे Session Confirmed Fragmentation अनुभाग देखें।

Data संदेशों के लिए, header encryption से पहले:

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

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### हेडर एन्क्रिप्शन

Connection ID को यादृच्छिक रूप से उत्पन्न किया जाना चाहिए। Source और Destination ID समान नहीं होने चाहिए, ताकि कोई on-path attacker (पथ पर स्थित आक्रमणकारी) कोई packet को capture करके originator को वापस न भेज सके जो वैध दिखे। Connection ID उत्पन्न करने के लिए counter का उपयोग न करें, ताकि कोई on-path attacker ऐसा packet उत्पन्न न कर सके जो वैध दिखे।

QUIC के विपरीत, हम handshake के दौरान या बाद में connection IDs को नहीं बदलते, यहाँ तक कि Retry message के बाद भी नहीं। IDs पहले message (Token Request या Session Request) से अंतिम message (Data with Termination) तक स्थिर रहते हैं। इसके अतिरिक्त, connection IDs path challenge या connection migration के दौरान या बाद में नहीं बदलते।

QUIC से अलग यह भी है कि headers में connection IDs हमेशा header-encrypted होते हैं। नीचे देखें।

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
यदि handshake में कोई First Packet Number block नहीं भेजा जाता है, तो packets को एक single session के भीतर, प्रत्येक दिशा के लिए, 0 से शुरू करके अधिकतम (2**32 -1) तक नंबर दिया जाता है। अधिकतम संख्या के packets भेजे जाने से काफी पहले session को समाप्त किया जाना चाहिए, और एक नया session बनाया जाना चाहिए।

यदि handshake में First Packet Number block भेजा जाता है, तो packets को एक single session के भीतर, उस दिशा के लिए, उस packet number से शुरू करके क्रमांकित किया जाता है। packet number session के दौरान wrap around हो सकता है। जब अधिकतम 2**32 packets भेजे जा चुके हों, packet number को वापस first packet number पर wrap करने पर, वह session अब valid नहीं रहता। session को terminate करना होगा, और एक नया session बनाना होगा, packets की अधिकतम संख्या भेजे जाने से काफी पहले।

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Header Encryption KDF

TODO key rotation, अधिकतम packet संख्या कम करें?

Handshake पैकेट जो खोए हुए निर्धारित किए जाते हैं, उन्हें पैकेट नंबर सहित समान header के साथ पूर्ण रूप से पुनः प्रेषित किया जाता है। Handshake संदेश Session Request, Session Created, और Session Confirmed को समान पैकेट नंबर और समान encrypted सामग्री के साथ पुनः प्रेषित किया जाना चाहिए, ताकि प्रतिक्रिया को encrypt करने के लिए समान chained hash का उपयोग किया जाए। Retry संदेश कभी भी प्रेषित नहीं किया जाता।

डेटा फेज़ पैकेट्स जो खो गए हैं माने जाते हैं, उन्हें कभी भी पूर्ण रूप से पुनः प्रेषित नहीं किया जाता (टर्मिनेशन को छोड़कर, नीचे देखें)। यही नियम उन ब्लॉक्स पर भी लागू होता है जो खोए गए पैकेट्स में शामिल हैं। इसके बजाय, वह जानकारी जो ब्लॉक्स में हो सकती है, आवश्यकतानुसार नए पैकेट्स में फिर से भेजी जाती है। डेटा पैकेट्स को कभी भी समान पैकेट नंबर के साथ पुनः प्रेषित नहीं किया जाता। पैकेट सामग्री की कोई भी पुनः प्रेषण (चाहे सामग्री समान रहे या न रहे) में अगले अप्रयुक्त पैकेट नंबर का उपयोग होना चाहिए।

#### हेडर सत्यापन

एक अपरिवर्तित पूरे पैकेट को वैसे ही, समान पैकेट संख्या के साथ पुनः प्रेषित करना कई कारणों से अनुमतित नहीं है। पृष्ठभूमि के लिए QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) धारा 12.3 देखें।

नए पैकेट उस जानकारी को ले जाने के लिए उपयोग किए जाते हैं जिसे खो गया माना जाता है। सामान्यतः, जानकारी तब फिर से भेजी जाती है जब उस जानकारी वाले पैकेट को खो गया माना जाता है, और भेजना तब बंद हो जाता है जब उस जानकारी वाले पैकेट की पावती मिल जाती है।

अपवाद: एक डेटा फेज पैकेट जिसमें Termination ब्लॉक हो, वह पूरा, जैसा-का-तैसा retransmit हो सकता है, लेकिन यह आवश्यक नहीं है। नीचे Session Termination सेक्शन देखें।

निम्नलिखित packets में एक random packet number होता है जिसे नजरअंदाज किया जाता है:

Alice के लिए, outbound packet numbering Session Confirmed के साथ 0 से शुरू होती है। Bob के लिए, outbound packet numbering पहले Data packet के साथ 0 से शुरू होती है, जो Session Confirmed का ACK होना चाहिए। एक उदाहरण standard handshake में packet numbers होंगे:

handshake संदेशों (SessionRequest, SessionCreated, या SessionConfirmed) का कोई भी पुनः प्रसारण वही packet number के साथ अपरिवर्तित रूप से भेजा जाना चाहिए। इन संदेशों को पुनः प्रसारित करते समय अलग ephemeral keys का उपयोग न करें या payload को न बदलें।

- पुनः प्रसारण के लिए packets को संग्रहीत करना अक्षम है
- एक नया packet data किसी on-path observer को अलग दिखता है, यह नहीं बता सकते कि यह पुनः प्रसारित है
- एक नया packet के साथ एक अपडेटेड ack block भेजा जाता है, पुराना ack block नहीं
- आप केवल वही पुनः प्रसारित करते हैं जो आवश्यक है। कुछ fragments पहले से ही एक बार पुनः प्रसारित हो चुके हो सकते हैं और ack हो गए हों
- यदि और भी pending है तो आप प्रत्येक पुनः प्रसारित packet में जितनी आवश्यकता हो उतना फिट कर सकते हैं
- Endpoints जो duplicates का पता लगाने के उद्देश्य से सभी व्यक्तिगत packets को ट्रैक करते हैं, उनमें अत्यधिक state संचय का जोखिम रहता है। Duplicates का पता लगाने के लिए आवश्यक data को एक न्यूनतम packet number बनाए रखकर सीमित किया जा सकता है जिसके नीचे सभी packets को तुरंत drop कर दिया जाता है।
- यह योजना बहुत अधिक लचीली है

हेडर (obfuscation और protection से पहले) हमेशा AEAD function के लिए associated data में शामिल होता है, ताकि हेडर को data के साथ cryptographically bind किया जा सके।

Header encryption के कई लक्ष्य हैं। पृष्ठभूमि और अनुमानों के लिए ऊपर "Additional DPI Discussion" अनुभाग देखें।

Headers को network database में प्रकाशित ज्ञात keys या बाद में गणना की गई keys के साथ encrypt किया जाता है। handshake phase में, यह केवल DPI प्रतिरोध के लिए है, क्योंकि key सार्वजनिक है और key और nonces का पुन: उपयोग किया जाता है, इसलिए यह वास्तव में केवल obfuscation है। ध्यान दें कि header encryption का उपयोग ephemeral keys X (Session Request में) और Y (Session Created में) को obfuscate करने के लिए भी किया जाता है।

- Session Request
- Session Created
- Token Request
- Retry
- Peer Test
- Hole Punch

अतिरिक्त मार्गदर्शन के लिए नीचे दिए गए Inbound Packet Handling सेक्शन को देखें।

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
सभी headers के Bytes 0-15 को header protection scheme का उपयोग करके encrypt किया जाता है, जो ज्ञात keys से calculated data के साथ XOR करके, ChaCha20 का उपयोग करता है, जो QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) और [Nonces](https://eprint.iacr.org/2019/624.pdf) के समान है। यह सुनिश्चित करता है कि encrypted short header और long header का पहला हिस्सा random दिखाई देगा।

#### ChaCha20/Poly1305

Session Request और Session Created के लिए, long header के bytes 16-31 और 32-byte Noise ephemeral key को ChaCha20 का उपयोग करके एन्क्रिप्ट किया जाता है। unencrypted data random है, इसलिए encrypted data भी random दिखाई देगा।

#### नोट्स

Retry के लिए, long header के bytes 16-31 को ChaCha20 का उपयोग करके encrypt किया जाता है। unencrypted डेटा random है, इसलिए encrypted डेटा भी random दिखाई देगा।

- प्रोटोकॉल की पहचान करने से ऑनलाइन DPI को रोकना
- हैंडशेक पुनःप्रसारण को छोड़कर, एक ही कनेक्शन में संदेशों की श्रृंखला में पैटर्न को रोकना
- विभिन्न कनेक्शन में एक ही प्रकार के संदेशों में पैटर्न को रोकना
- netDb में मिली introduction key की जानकारी के बिना हैंडशेक हेडर की डिक्रिप्शन को रोकना
- netDb में मिली introduction key की जानकारी के बिना X25519 ephemeral keys की पहचान को रोकना
- किसी भी ऑनलाइन या ऑफलाइन हमलावर द्वारा डेटा फेज पैकेट नंबर और टाइप की डिक्रिप्शन को रोकना
- netDb में मिली introduction key की जानकारी के बिना on-path या off-path observer द्वारा वैध हैंडशेक पैकेट के injection को रोकना
- on-path या off-path observer द्वारा वैध डेटा पैकेट के injection को रोकना
- आने वाले पैकेट्स के तीव्र और कुशल वर्गीकरण की अनुमति देना
- "probing" प्रतिरोध प्रदान करना ताकि खराब Session Request का कोई response न हो, या यदि Retry response है तो netDb में मिली introduction key की जानकारी के बिना response को I2P के रूप में पहचाना न जा सके
- Destination Connection ID महत्वपूर्ण डेटा नहीं है, और यह ठीक है यदि netDb में मिली introduction key की जानकारी रखने वाले observer द्वारा इसे decrypt किया जा सके
- डेटा फेज पैकेट का पैकेट नंबर एक AEAD nonce है और यह महत्वपूर्ण डेटा है। netDb में मिली introduction key की जानकारी के साथ भी observer द्वारा इसे decrypt नहीं किया जा सकता। [Nonces](https://eprint.iacr.org/2019/624.pdf) देखें।

QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) header protection scheme के विपरीत, सभी headers के सभी भाग, destination और source connection IDs सहित, encrypted हैं। QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) और [Nonces](https://eprint.iacr.org/2019/624.pdf) मुख्य रूप से header के "critical" भाग को encrypt करने पर केंद्रित हैं, यानी packet number (ChaCha20 nonce)। जबकि session ID को encrypt करना incoming packet classification को थोड़ा अधिक जटिल बनाता है, यह कुछ attacks को अधिक कठिन बनाता है। QUIC अलग-अलग phases के लिए, और path challenge तथा connection migration के लिए अलग connection IDs define करता है। यहाँ हम पूरे समय एक ही connection IDs का उपयोग करते हैं, क्योंकि वे encrypted हैं।

हेडर सुरक्षा की सात प्रमुख चरण हैं:

Header encryption का डिज़ाइन तेज़ी से इनबाउंड packets का वर्गीकरण करने के लिए किया गया है, बिना जटिल heuristics या fallbacks के। यह लगभग सभी इनबाउंड messages के लिए समान k_header_1 key का उपयोग करके पूरा किया जाता है। यहाँ तक कि जब किसी connection का source IP या port वास्तविक IP परिवर्तन या NAT व्यवहार के कारण बदल जाता है, तो भी packet को connection ID की एक single lookup के साथ तेज़ी से session के साथ mapped किया जा सकता है।

ध्यान दें कि Session Created और Retry केवल वे संदेश हैं जिन्हें Connection ID को decrypt करने के लिए k_header_1 के लिए fallback processing की आवश्यकता होती है, क्योंकि वे भेजने वाले (Bob के) intro key का उपयोग करते हैं। अन्य सभी संदेश k_header_1 के लिए प्राप्तकर्ता के intro key का उपयोग करते हैं। fallback processing को केवल source IP/port द्वारा pending outbound connections को देखना होता है।

यदि source IP/port द्वारा fallback processing एक pending outbound connection खोजने में विफल हो जाती है, तो इसके कई कारण हो सकते हैं:

जबकि pending outbound connection को खोजने और उस connection के लिए k_header_1 का उपयोग करके connection ID को decrypt करने के लिए अतिरिक्त fallback processing संभव है, यह शायद आवश्यक नहीं है। यदि Bob को अपने NAT या packet routing के साथ समस्याएं हैं, तो शायद connection को fail होने देना बेहतर है। यह design इस बात पर निर्भर करता है कि endpoints handshake की अवधि के लिए एक स्थिर address बनाए रखें।

अतिरिक्त दिशानिर्देशों के लिए नीचे दिया गया Inbound Packet Handling सेक्शन देखें।

- Session Request और Token Request
- Session Created
- Retry
- Session Confirmed
- Data Phase
- Peer Test
- Hole Punch

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
उस चरण के लिए header encryption keys की व्युत्पत्ति के लिए नीचे दिए गए व्यक्तिगत KDF अनुभागों को देखें।

यह KDF पैकेट के अंतिम 24 bytes को दो ChaCha20 operations के लिए IV के रूप में उपयोग करता है। चूंकि सभी पैकेट 16 byte MAC के साथ समाप्त होते हैं, इसके लिए आवश्यक है कि सभी पैकेट payloads न्यूनतम 8 bytes के हों। यह आवश्यकता नीचे message sections में अतिरिक्त रूप से प्रलेखित है।

हेडर के पहले 8 बाइट्स को decrypt करने के बाद, receiver को Destination Connection ID पता चल जाएगा। वहाँ से, receiver को पता चल जाएगा कि हेडर के बाकी हिस्से के लिए कौन सी header encryption key का उपयोग करना है, जो session के key phase पर आधारित होती है।

- SSU2 संदेश नहीं है
- एक दूषित SSU2 संदेश
- उत्तर किसी हमलावर द्वारा स्पूफ किया गया या संशोधित किया गया है
- Bob के पास symmetric NAT है
- संदेश प्रसंस्करण के दौरान Bob ने IP या port बदल दिया
- Bob ने उत्तर एक अलग interface से भेजा

हेडर के अगले 8 बाइट्स को decrypt करने से message type का पता चल जाएगा और यह निर्धारित किया जा सकेगा कि यह short या long header है। यदि यह long header है, तो receiver को version और netid fields को validate करना होगा। यदि version != 2 है, या netid != expected value है (आमतौर पर 2, test networks को छोड़कर), तो receiver को message को drop कर देना चाहिए।

सभी संदेशों में तीन या चार भाग होते हैं:

सभी मामलों में, header (और यदि मौजूद है, तो ephemeral key) को authentication MAC के साथ बाइंड किया जाता है ताकि यह सुनिश्चित हो सके कि पूरा संदेश बरकरार है।

#### AEAD त्रुटि प्रबंधन

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Inbound packet handlers को हमेशा ChaCha20 payload को decrypt करना चाहिए और message को process करने से पहले MAC को validate करना चाहिए, एक अपवाद के साथ: अमान्य token के साथ स्पष्ट Session Request messages वाले address-spoofed packets से DoS attacks को कम करने के लिए, एक handler को पूरे message को decrypt और validate करने का प्रयास करने की आवश्यकता नहीं है (ChaCha20/Poly1305 decryption के अतिरिक्त एक महंगे DH operation की आवश्यकता होती है)। Handler Session Request message के header में मिले values का उपयोग करके Retry message के साथ जवाब दे सकता है।

#### प्रारंभिक ChainKey के लिए KDF

तीन अलग authenticated encryption instances (CipherStates) हैं। एक handshake phase के दौरान, और दो (transmit और receive) data phase के लिए। प्रत्येक का अपना key KDF से है।

एन्क्रिप्टेड/प्रमाणित डेटा को इस रूप में प्रस्तुत किया जाएगा

### प्रमाणित एन्क्रिप्शन

एन्क्रिप्टेड और प्रमाणित डेटा प्रारूप।

- संदेश हेडर
- केवल Session Request और Session Created के लिए, एक ephemeral key
- एक ChaCha20-encrypted payload
- एक Poly1305 MAC

एन्क्रिप्शन/डिक्रिप्शन फ़ंक्शन के लिए इनपुट:

- handshake संदेशों Session Request, Session Created, और Session Confirmed के लिए, संदेश हेडर को Noise प्रोसेसिंग फेज से पहले mixHash() किया जाता है
- ephemeral key, यदि मौजूद है, तो एक मानक Noise misHash() द्वारा कवर की जाती है
- Noise handshake के बाहर के संदेशों के लिए, हेडर का उपयोग ChaCha20/Poly1305 एन्क्रिप्शन के लिए Associated Data के रूप में किया जाता है।

एन्क्रिप्शन फ़ंक्शन का आउटपुट, डिक्रिप्शन फ़ंक्शन का इनपुट:

### Session Request के लिए KDF

ChaCha20 के लिए, यहाँ जो वर्णित है वह [RFC-7539](https://tools.ietf.org/html/rfc7539) के अनुरूप है, जो TLS [RFC-7905](https://tools.ietf.org/html/rfc7905) में भी समान रूप से उपयोग किया जाता है।

Key Derivation Function (KDF) DH परिणाम से एक handshake phase cipher key k उत्पन्न करता है, HMAC-SHA256(key, data) का उपयोग करते हुए जैसा कि [RFC-2104](https://tools.ietf.org/html/rfc2104) में परिभाषित है। ये InitializeSymmetric(), MixHash(), और MixKey() functions हैं, बिल्कुल वैसे ही जैसे Noise spec में परिभाषित किए गए हैं।

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### Session Request के लिए KDF

Alice, Bob को भेजता है, या तो handshake में पहले संदेश के रूप में, या Retry संदेश के जवाब में। Bob एक Session Created संदेश के साथ जवाब देता है। Size: 80 + payload size। Minimum Size: 88

यदि Alice के पास एक वैध token नहीं है, तो Alice को Session Request के बजाय Token Request message भेजना चाहिए, ताकि Session Request बनाने में asymmetric encryption के overhead से बचा जा सके।

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
लंबा हेडर। Noise सामग्री: Alice की ephemeral key X Noise payload: DateTime और अन्य blocks अधिकतम payload आकार: MTU - 108 (IPv4) या MTU - 128 (IPv6)। 1280 MTU के लिए: अधिकतम payload 1172 (IPv4) या 1152 (IPv6) है। 1500 MTU के लिए: अधिकतम payload 1392 (IPv4) या 1372 (IPv6) है।

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
पेलोड सुरक्षा गुण:

#### पेलोड

- चूंकि ChaCha20 एक stream cipher है, plaintexts को padded करने की आवश्यकता नहीं है। अतिरिक्त keystream bytes को त्याग दिया जाता है।
- cipher के लिए key (256 bits) SHA256 KDF के माध्यम से सहमत की जाती है। प्रत्येक message के लिए KDF का विवरण नीचे अलग sections में है।

#### नोट्स

- सभी संदेशों में, AEAD संदेश का आकार पहले से ही ज्ञात होता है। AEAD प्रमाणीकरण विफलता पर, प्राप्तकर्ता को आगे का संदेश प्रसंस्करण रोकना चाहिए और संदेश को छोड़ देना चाहिए।
- Bob को बार-बार विफलताओं वाले IPs की एक काली सूची बनाए रखनी चाहिए।

### SessionRequest (प्रकार 0)

X वैल्यू को payload की अप्रभेद्यता और विशिष्टता सुनिश्चित करने के लिए एन्क्रिप्ट किया जाता है, जो आवश्यक DPI प्रतिकारी उपाय हैं। हम इसे प्राप्त करने के लिए ChaCha20 एन्क्रिप्शन का उपयोग करते हैं, बजाय अधिक जटिल और धीमे विकल्पों जैसे elligator2 के। Bob के router public key के लिए असममित एन्क्रिप्शन बहुत धीमा होगा। ChaCha20 एन्क्रिप्शन Bob की intro key का उपयोग करता है जैसा कि network database में प्रकाशित है।

#### पेलोड

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### नोट्स

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### Session Created और Session Confirmed part 1 के लिए KDF

ChaCha20 एन्क्रिप्शन केवल DPI प्रतिरोध के लिए है। Bob की introduction key जानने वाला कोई भी पक्ष, जो network database में प्रकाशित है, इस संदेश में header और X value को decrypt कर सकता है।

कच्ची सामग्री:

असंक्रमित डेटा (Poly1305 प्रामाणीकरण टैग दिखाया नहीं गया):

न्यूनतम payload का आकार 8 बाइट्स है। चूंकि DateTime ब्लॉक केवल 7 बाइट्स का है, इसलिए कम से कम एक और ब्लॉक उपस्थित होना चाहिए।

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
Bob, Alice को Session Request संदेश के जवाब में भेजता है। Alice, Session Confirmed संदेश के साथ जवाब देती है। आकार: 80 + payload आकार। न्यूनतम आकार: 88

Noise content: Bob की ephemeral key Y Noise payload: DateTime, Address, और अन्य blocks Max payload size: MTU - 108 (IPv4) या MTU - 128 (IPv6)। 1280 MTU के लिए: Max payload 1172 (IPv4) या 1152 (IPv6) है। 1500 MTU के लिए: Max payload 1392 (IPv4) या 1372 (IPv6) है।

पेलोड सुरक्षा गुण:

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
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Y मान को payload अविभेद्यता और विशिष्टता सुनिश्चित करने के लिए एन्क्रिप्ट किया जाता है, जो आवश्यक DPI प्रतिकारी उपाय हैं। हम इसे प्राप्त करने के लिए ChaCha20 एन्क्रिप्शन का उपयोग करते हैं, elligator2 जैसे अधिक जटिल और धीमे विकल्पों के बजाय। Alice के router public key के लिए असममित एन्क्रिप्शन बहुत धीमा होगा। ChaCha20 एन्क्रिप्शन Bob की intro key का उपयोग करता है, जैसा कि network database में प्रकाशित है।

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
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### समस्याएं

- DateTime ब्लॉक
- Options ब्लॉक (वैकल्पिक)
- Relay Tag Request ब्लॉक (वैकल्पिक)
- Padding ब्लॉक (वैकल्पिक)

ChaCha20 encryption केवल DPI प्रतिरोध के लिए है। कोई भी पक्ष जो Bob की intro key जानता है, जो network database में प्रकाशित है, और Session Request के पहले 32 bytes को capture करता है, इस संदेश में Y value को decrypt कर सकता है।

#### पेलोड

- प्रारंभिक ChaCha20 block में अनोखा X मान यह सुनिश्चित करता है कि ciphertext हर session के लिए अलग हो।
- probing प्रतिरोध प्रदान करने के लिए, Bob को Session Request message के जवाब में Retry message नहीं भेजना चाहिए जब तक कि Session Request message में message type, protocol version, और network ID fields वैध न हों।
- Bob को उन connections को अस्वीकार करना चाहिए जहाँ timestamp मान वर्तमान समय से बहुत दूर है। अधिकतम delta time को "D" कहते हैं। Bob को पहले से उपयोग किए गए handshake values का local cache बनाए रखना चाहिए और duplicates को अस्वीकार करना चाहिए, replay attacks को रोकने के लिए। Cache में values का जीवनकाल कम से कम 2*D होना चाहिए। Cache values implementation-dependent हैं, हालांकि 32-byte X value (या इसका encrypted equivalent) का उपयोग किया जा सकता है। zero token और termination block वाला Retry message भेजकर अस्वीकार करें।
- Diffie-Hellman ephemeral keys का कभी भी पुन: उपयोग नहीं किया जा सकता, cryptographic attacks को रोकने के लिए, और पुन: उपयोग को replay attack के रूप में अस्वीकार किया जाएगा।
- "KE" और "auth" options compatible होने चाहिए, यानी shared secret K उपयुक्त आकार का होना चाहिए। यदि अधिक "auth" options जोड़े जाते हैं, तो यह "KE" flag के अर्थ को implicitly बदल सकता है ताकि अलग KDF या अलग truncation size का उपयोग हो।
- Bob को validate करना चाहिए कि Alice की ephemeral key curve पर एक valid point है।
- Padding को reasonable मात्रा तक सीमित होना चाहिए। Bob excessive padding वाली connections को अस्वीकार कर सकता है। Bob अपने padding options को Session Created में specify करेगा। Min/max guidelines TBD। 0 से 31 bytes minimum तक का random size? (Distribution निर्धारित किया जाना है, Appendix A देखें।)
- अधिकांश errors पर, जिनमें AEAD, DH, स्पष्ट replay, या key validation failure शामिल हैं, Bob को आगे की message processing रोकनी चाहिए और बिना जवाब दिए message को drop कर देना चाहिए।
- Bob zero token और Termination block के साथ एक Retry message भेज सकता है जिसमें clock skew reason code हो यदि DateTime block में timestamp बहुत skewed है।
- DoS Mitigation: DH एक relatively expensive operation है। पिछले NTCP protocol की तरह, routers को CPU या connection exhaustion को रोकने के लिए सभी आवश्यक उपाय करने चाहिए। अधिकतम active connections और progress में अधिकतम connection setups पर सीमा लगाएं। Read timeouts enforce करें (प्रति-read और "slowloris" के लिए कुल दोनों)। एक ही source से repeated या simultaneous connections को सीमित करें। बार-बार fail होने वाले sources के लिए blacklists बनाए रखें। AEAD failure का जवाब न दें। वैकल्पिक रूप से, DH operation और AEAD validation से पहले Retry message के साथ जवाब दें।
- "ver" field: समग्र Noise protocol, extensions, और SSU2 protocol जिसमें payload specifications शामिल हैं, SSU2 को indicate करते हुए। यह field भविष्य के बदलावों के support को indicate करने के लिए उपयोग किया जा सकता है।
- network ID field का उपयोग cross-network connections को जल्दी identify करने के लिए किया जाता है। यदि यह field Bob की network ID से match नहीं करता, तो Bob को disconnect करना चाहिए और भविष्य की connections को block करना चाहिए।
- Bob को message drop करना चाहिए यदि Source Connection ID, Destination Connection ID के बराबर है।

### SessionCreated (Type 1)

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### Session Confirmed भाग 1 के लिए KDF, Session Created KDF का उपयोग करते हुए

कच्ची सामग्री:

असंकेतित डेटा (Poly1305 प्रमाणीकरण टैग दिखाया नहीं गया):

न्यूनतम payload का आकार 8 bytes है। चूंकि DateTime और Address blocks मिलकर उससे अधिक होते हैं, इसलिए केवल इन दो blocks के साथ ही आवश्यकता पूरी हो जाती है।

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Alice, Session Created संदेश के जवाब में Bob को भेजती है। Bob तुरंत एक ACK block युक्त Data संदेश के साथ जवाब देता है। आकार: 80 + payload size। न्यूनतम आकार: लगभग 500 (न्यूनतम router info block का आकार लगभग 420 bytes है)

Noise सामग्री: Alice की static key Noise payload भाग 1: कोई नहीं Noise payload भाग 2: Alice का RouterInfo, और अन्य blocks Max payload आकार: MTU - 108 (IPv4) या MTU - 128 (IPv6)। 1280 MTU के लिए: Max payload 1172 (IPv4) या 1152 (IPv6) है। 1500 MTU के लिए: Max payload 1392 (IPv4) या 1372 (IPv6) है।

Payload सुरक्षा गुण:

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
|   ChaCha20 data                       |
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

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
इसमें दो ChaChaPoly frames हैं। पहला Alice की encrypted static public key है। दूसरा Noise payload है: Alice का encrypted RouterInfo, वैकल्पिक options, और वैकल्पिक padding। ये अलग-अलग keys का उपयोग करते हैं, क्योंकि बीच में MixKey() function को call किया जाता है।

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
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 1

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### नोट्स

- DateTime block
- Address block
- Relay Tag block (वैकल्पिक)
- New Token block (अनुशंसित नहीं, नोट देखें)
- First Packet Number block (वैकल्पिक)
- Options block (वैकल्पिक)
- Termination block (अनुशंसित नहीं, इसके बजाय retry message में भेजें)
- Padding block (वैकल्पिक)

कच्ची सामग्री:

#### Session पुष्टि खंडन

- Alice को यहाँ यह validate करना होगा कि Bob की ephemeral key curve पर एक valid point है।
- Padding को reasonable मात्रा तक सीमित होना चाहिए। Alice अत्यधिक padding वाले connections को reject कर सकती है। Alice अपने padding options को Session Confirmed में specify करेगी। Min/max guidelines TBD। 0 से 31 bytes तक minimum random size? (Distribution निर्धारित होना है, Appendix A देखें।)
- किसी भी error पर, जिसमें AEAD, DH, timestamp, apparent replay, या key validation failure शामिल है, Alice को आगे की message processing रोकनी होगी और बिना response दिए connection बंद करना होगा।
- Alice को उन connections को reject करना होगा जहाँ timestamp value current time से बहुत अधिक अलग है। Maximum delta time को "D" कहते हैं। Alice को पहले उपयोग हुए handshake values का local cache maintain करना होगा और duplicates को reject करना होगा, replay attacks को रोकने के लिए। Cache में values का lifetime कम से कम 2*D होना चाहिए। Cache values implementation-dependent हैं, हालांकि 32-byte Y value (या इसका encrypted equivalent) उपयोग किया जा सकता है।
- Alice को message drop करना होगा यदि source IP और port, Session Request के destination IP और port से match नहीं करते।
- Alice को message drop करना होगा यदि Destination और Source Connection IDs, Session Request के Source और Destination Connection IDs से match नहीं करते।
- Bob एक relay tag block भेजता है यदि Alice द्वारा Session Request में requested हो।
- Session Created में New Token block recommended नहीं है, क्योंकि Bob को पहले Session Confirmed का validation करना चाहिए। नीचे Tokens section देखें।

#### नोट्स

- यहाँ min/max padding विकल्प शामिल करें?

### Session Confirmed भाग 2 के लिए KDF

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### SessionConfirmed (टाइप 2)

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### डेटा चरण के लिए KDF

असंगुप्तित डेटा (Poly1305 auth tags दिखाए नहीं गए हैं):

न्यूनतम payload का आकार 8 bytes है। चूंकि RouterInfo block इससे काफी अधिक होगा, इसलिए केवल इस block के साथ ही आवश्यकता पूरी हो जाती है।

1)  Alice का Router Info block (आवश्यक)   2)  Options block (वैकल्पिक)   3)  I2NP blocks (वैकल्पिक)

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
4\) Padding block (वैकल्पिक) इस frame में कभी भी कोई अन्य block type नहीं होना चाहिए। TODO: relay और peer test के बारे में क्या?

Session Confirmed संदेश में Alice की पूर्ण हस्ताक्षरित Router Info होनी चाहिए ताकि Bob कई आवश्यक जांच कर सके:

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 encrypted data (32 bytes)  |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaCha20 encrypted data             +
|   see below for allowed blocks        |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaCha20 encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
दुर्भाग्य से, Router Info, RI block में gzip compressed होने पर भी, MTU से अधिक हो सकता है। इसलिए, Session Confirmed दो या अधिक packets में fragmented हो सकता है। यह SSU2 protocol में एकमात्र मामला है जहाँ एक AEAD-protected payload दो या अधिक packets में fragmented होता है।

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### नोट्स

- RouterInfo ब्लॉक (पहला ब्लॉक होना चाहिए)
- Options ब्लॉक (वैकल्पिक)
- New Token ब्लॉक (वैकल्पिक)
- Relay Request ब्लॉक (वैकल्पिक)
- Peer Test ब्लॉक (वैकल्पिक)
- First Packet Number ब्लॉक (वैकल्पिक)
- I2NP, First Fragment, या Follow-on Fragment ब्लॉक (वैकल्पिक, लेकिन शायद जगह नहीं है)
- Padding ब्लॉक (वैकल्पिक)

प्रत्येक पैकेट के लिए हेडर निम्नलिखित रूप में बनाए जाते हैं:

#### पेलोड

- Bob को सामान्य Router Info सत्यापन करना होगा। सुनिश्चित करें कि signature type समर्थित है, signature को सत्यापित करें, timestamp सीमा के भीतर है यह जांचें, और कोई भी अन्य आवश्यक जांच करें। खंडित Router Infos को संभालने के बारे में नोट्स के लिए नीचे देखें।

- Bob को यह सत्यापित करना होगा कि पहले frame में प्राप्त Alice की static key, Router Info में स्थित static key से मेल खाती है। Bob को पहले Router Info में एक matching version (v) option के साथ NTCP या SSU2 Router Address की खोज करनी होगी। नीचे Published Router Info और Unpublished Router Info sections देखें। fragmented Router Infos को handle करने के नोट्स के लिए नीचे देखें।

- यदि Bob के netdb में Alice के RouterInfo का पुराना version है, तो यह verify करें कि router info में static key दोनों में समान है, यदि मौजूद है, और यदि पुराना version XXX से कम पुराना है (नीचे key rotate time देखें)

- Bob को यहाँ यह सत्यापित करना चाहिए कि Alice की static key curve पर एक वैध बिंदु है।

- विकल्प शामिल किए जाने चाहिए, padding parameters निर्दिष्ट करने के लिए।

- किसी भी त्रुटि पर, AEAD, RI, DH, timestamp, या key validation विफलता सहित, Bob को आगे की message processing रोकनी चाहिए और बिना जवाब दिए connection बंद कर देना चाहिए।

- Message 3 part 2 frame सामग्री: इस frame का format data phase frames के format के समान है, सिवाय इसके कि frame की length Alice द्वारा Session Request में भेजी जाती है। Data phase frame format के लिए नीचे देखें। Frame में निम्नलिखित क्रम में 1 से 4 blocks होने चाहिए:

पैकेट्स की श्रृंखला को निम्नलिखित प्रकार से बनाएं:

पुनर्संयोजन प्रक्रिया:

- Message 3 part 2 padding block की सिफारिश की जाती है।

- MTU और Router Info के आकार के आधार पर, I2NP blocks के लिए कोई स्थान नहीं हो सकता है, या केवल थोड़ा सा स्थान उपलब्ध हो सकता है। यदि Router Info fragmented है तो I2NP blocks को शामिल न करें। सबसे सरल implementation यह हो सकती है कि Session Confirmed message में कभी भी I2NP blocks शामिल न करें, और सभी I2NP blocks को बाद के Data messages में भेजें। अधिकतम block size के लिए नीचे Router Info block section देखें।

#### पेलोड

जब Bob को कोई Session Confirmed message प्राप्त होता है, तो वह header को decrypt करता है, frag field का निरीक्षण करता है, और निर्धारित करता है कि Session Confirmed fragmented है। वह तब तक message को decrypt नहीं करता (और नहीं कर सकता) जब तक कि सभी fragments प्राप्त नहीं हो जाते और reassemble नहीं हो जाते।

- RI में स्टेटिक key "s" handshake में स्टेटिक key से मेल खाती है
- RI में introduction key "i" को निकाला जाना चाहिए और वैध होना चाहिए, जिसका उपयोग data phase में किया जाएगा
- RI signature वैध है

Bob के पास व्यक्तिगत fragments को ack करने का कोई तंत्र नहीं है। जब Bob सभी fragments प्राप्त करता है, पुनः असेंबल करता है, decrypt करता है, और contents को validate करता है, तो Bob सामान्य रूप से split() करता है, data phase में प्रवेश करता है, और packet number 0 का ACK भेजता है।

यदि Alice को packet number 0 का ACK प्राप्त नहीं होता है, तो उसे सभी session confirmed packets को जैसे हैं वैसे ही retransmit करना होगा।

- सभी हेडर छोटे हेडर होते हैं जिनका पैकेट नंबर 0 होता है
- सभी हेडर का प्रकार = 2 (सत्र पुष्टि किया गया) होता है
- सभी हेडर में "frag" फ़ील्ड होता है, जिसमें खंड की संख्या और खंडों की कुल संख्या होती है
- खंड 0 का एनक्रिप्टेड हेडर "जंबो" संदेश के लिए सहयोगी डेटा (AD) होता है
- प्रत्येक हेडर को उस पैकेट में अंतिम 24 बाइट्स डेटा का उपयोग करके एनक्रिप्ट किया जाता है

उदाहरण:

- एक single RI block बनाएं (RI block frag field में fragment 0 of 1)। हम RI block fragmentation का उपयोग नहीं करते, यह समान समस्या को हल करने की एक वैकल्पिक पद्धति के लिए था।
- RI block और शामिल किए जाने वाले किसी भी अन्य blocks के साथ एक "jumbo" payload बनाएं
- कुल data size की गणना करें (header शामिल नहीं करके), जो payload size + static key और दो MACs के लिए 64 bytes है
- प्रत्येक packet में उपलब्ध space की गणना करें, जो MTU माइनस IP header (20 या 40), माइनस UDP header (8), माइनस SSU2 short header (16) है। कुल per-packet overhead 44 (IPv4) या 64 (IPv6) है।
- packets की संख्या की गणना करें।
- अंतिम packet में data के size की गणना करें। यह 24 bytes से अधिक या बराबर होना चाहिए, ताकि header encryption काम करे। यदि यह बहुत छोटा है, तो या तो एक padding block जोड़ें, या यदि पहले से मौजूद है तो padding block का size बढ़ाएं, या अन्य packets में से किसी एक का size कम करें ताकि अंतिम packet पर्याप्त बड़ा हो।
- पहले packet के लिए unencrypted header बनाएं, frag field में total fragments की संख्या के साथ, और "jumbo" payload को Noise के साथ encrypt करें, header को AD के रूप में उपयोग करके, हमेशा की तरह।
- encrypted jumbo packet को fragments में विभाजित करें
- प्रत्येक fragment 1-n के लिए एक unencrypted header जोड़ें
- प्रत्येक fragment 0-n के लिए header को encrypt करें। प्रत्येक header उसी k_header_1 और k_header_2 का उपयोग करता है जैसा कि ऊपर Session Confirmed KDF में परिभाषित है।
- सभी fragments को transmit करें

1500 MTU over IPv6 के लिए, अधिकतम payload 1372 है, RI block overhead 5 है, अधिकतम (gzip compressed) RI data size 1367 है (यह मानते हुए कि कोई अन्य blocks नहीं हैं)। दो packets के साथ, दूसरे packet का overhead 64 है, इसलिए यह अतिरिक्त 1436 bytes का payload रख सकता है। अतः दो packets एक compressed RI के लिए 2803 bytes तक पर्याप्त हैं।

वर्तमान नेटवर्क में देखा गया सबसे बड़ा compressed RI लगभग 1400 bytes का है; इसलिए, व्यावहारिक रूप से, दो fragments पर्याप्त होने चाहिए, यहाँ तक कि न्यूनतम 1280 MTU के साथ भी। प्रोटोकॉल अधिकतम 15 fragments की अनुमति देता है।

- Fragment 0 के लिए header को संरक्षित रखें, क्योंकि इसका उपयोग Noise AD के रूप में किया जाता है
- Reassembly से पहले अन्य fragments के headers को त्याग दें
- "Jumbo" payload को reassemble करें, fragment 0 के header के साथ AD के रूप में, और Noise के साथ decrypt करें
- RI block को सामान्य रूप से validate करें
- Data phase में आगे बढ़ें और सामान्य रूप से ACK 0 भेजें

सुरक्षा विश्लेषण:

एक fragmented Session Confirmed की अखंडता और सुरक्षा unfragmented Session Confirmed के समान होती है। किसी भी fragment का कोई भी परिवर्तन reassembly के बाद Noise AEAD को असफल बना देगा। fragment 0 के बाद के fragments के headers केवल fragment की पहचान के लिए उपयोग किए जाते हैं। भले ही किसी on-path attacker के पास header को encrypt करने के लिए उपयोग की जाने वाली k_header_2 key हो (असंभावित, handshake से derived), यह भी attacker को valid fragment substitute करने की अनुमति नहीं देगा।

डेटा चरण संबंधित डेटा के लिए हेडर का उपयोग करता है।

KDF chaining key ck से दो cipher keys k_ab और k_ba उत्पन्न करता है, HMAC-SHA256(key, data) का उपयोग करके जैसा कि [RFC-2104](https://tools.ietf.org/html/rfc2104) में परिभाषित है। यह split() function है, बिल्कुल वैसे ही जैसे Noise spec में परिभाषित है।

Noise payload: सभी block types की अनुमति है Max payload size: MTU - 60 (IPv4) या MTU - 80 (IPv6)। 1500 MTU के लिए: Max payload 1440 (IPv4) या 1420 (IPv6) है।

Session Confirmed के दूसरे भाग से शुरू करके, सभी संदेश एक प्रमाणित और एन्क्रिप्टेड ChaChaPoly payload के अंदर होते हैं। सभी पैडिंग संदेश के अंदर होती है। payload के अंदर एक मानक प्रारूप होता है जिसमें शून्य या अधिक "blocks" होते हैं। प्रत्येक block में एक-बाइट का प्रकार और दो-बाइट की लंबाई होती है। प्रकारों में date/time, I2NP message, options, termination, और padding शामिल हैं।

नोट: Bob अपने RouterInfo को Alice को data phase में अपने पहले संदेश के रूप में भेज सकता है, लेकिन यह आवश्यक नहीं है।

### डेटा संदेश (प्रकार 6)

पेलोड सुरक्षा गुण:

अनएन्क्रिप्टेड डेटा (Poly1305 auth tag दिखाया नहीं गया):

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### Peer Test के लिए KDF

Charlie, Alice को भेजता है, और Alice, Charlie को भेजती है, केवल Peer Test phases 5-7 के लिए। Peer Test phases 1-4 को in-session भेजा जाना चाहिए एक Data message में Peer Test block का उपयोग करके। अधिक जानकारी के लिए नीचे Peer Test Block और Peer Test Process अनुभाग देखें।

आकार: 48 + payload का आकार।

Noise payload: नीचे देखें।

कच्ची सामग्री:

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### नोट्स

- router को AEAD error के साथ आने वाले message को drop करना चाहिए।

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
असंगुप्त डेटा (Poly1305 प्रमाणीकरण टैग नहीं दिखाया गया):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### पेलोड

- न्यूनतम payload का आकार 8 बाइट्स है। यह आवश्यकता किसी भी ACK, I2NP, First Fragment, या Follow-on Fragment block द्वारा पूरी की जाएगी। यदि आवश्यकता पूरी नहीं होती है, तो एक Padding block शामिल करना होगा।
- प्रत्येक packet number का उपयोग केवल एक बार किया जा सकता है। I2NP messages या fragments को retransmit करते समय, एक नया packet number का उपयोग करना होगा।

### Peer Test (Type 7)

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### पुनः प्रयास के लिए KDF

न्यूनतम payload का आकार 8 bytes है। चूंकि Peer Test block का कुल आकार इससे अधिक है, इसलिए केवल इस block के साथ ही आवश्यकता पूरी हो जाती है।

संदेश 5 और 7 में, Peer Test ब्लॉक in-session संदेश 3 और 4 के ब्लॉक के समान हो सकता है, जिसमें Charlie द्वारा हस्ताक्षरित समझौता होता है, या इसे पुनः जेनरेट किया जा सकता है। हस्ताक्षर वैकल्पिक है।

संदेश 6 में, Peer Test block in-session संदेशों 1 और 2 के block के समान हो सकता है, जिसमें Alice द्वारा हस्ताक्षरित अनुरोध होता है, या यह पुनर्जनित हो सकता है। Signature वैकल्पिक है।

Connection IDs: दोनों connection ID test nonce से प्राप्त किए जाते हैं। Charlie से Alice को भेजे गए messages 5 और 7 के लिए, Destination Connection ID 4-byte big-endian test nonce की दो प्रतियां हैं, यानी ((nonce << 32) | nonce)। Source Connection ID, Destination Connection ID का inverse है, यानी ~((nonce << 32) | nonce)। Alice से Charlie को भेजे गए message 6 के लिए, दोनों connection ID को अदला-बदली करें।

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
पता ब्लॉक सामग्री:

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
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### नोट्स

- DateTime block
- Address block (संदेश 6 और 7 के लिए आवश्यक, नीचे दिया गया नोट देखें)
- Peer Test block
- Padding block (वैकल्पिक)

Retry message की आवश्यकता यह है कि Bob को जवाब में Retry message उत्पन्न करने के लिए Session Request message को decrypt करने की आवश्यकता नहीं है। साथ ही, यह message तेज़ी से उत्पन्न होना चाहिए, केवल symmetric encryption का उपयोग करके।

Bob, Alice को Session Request या Token Request संदेश के जवाब में भेजता है। Alice एक नए Session Request के साथ प्रतिक्रिया देती है। आकार: 48 + payload का आकार।

यदि एक Termination block शामिल है तो यह एक Termination संदेश के रूप में भी कार्य करता है (यानी, "पुनः प्रयास न करें")।

Noise payload: नीचे देखें।

कच्ची सामग्री:

- संदेश 5 में: आवश्यक नहीं।
- संदेश 6 में: Charlie का IP और port जैसा कि Charlie के RI से चुना गया।
- संदेश 7 में: Alice का वास्तविक IP और port जिससे संदेश 6 प्राप्त हुआ था।

### पुनः प्रयास (Type 9)

अनएन्क्रिप्टेड डेटा (Poly1305 authentication tag दिखाया नहीं गया):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### टोकन अनुरोध के लिए KDF

न्यूनतम payload आकार 8 बाइट्स है। चूंकि DateTime और Address ब्लॉक्स मिलकर इससे अधिक हैं, इसलिए केवल इन दो ब्लॉक्स के साथ ही आवश्यकता पूरी हो जाती है।

यह संदेश तुरंत जेनरेट होना चाहिए, केवल symmetric encryption का उपयोग करके।

Alice, Bob को भेजता है। Bob एक Retry संदेश के साथ जवाब देता है। आकार: 48 + payload आकार।

यदि Alice के पास एक वैध टोकन नहीं है, तो Alice को Session Request के बजाय यह संदेश भेजना चाहिए, ताकि Session Request बनाने में asymmetric encryption के ओवरहेड से बचा जा सके।

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Noise payload: नीचे देखें।

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
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### पेलोड

- DateTime ब्लॉक
- Address ब्लॉक
- Options ब्लॉक (वैकल्पिक)
- Termination ब्लॉक (वैकल्पिक, यदि सत्र अस्वीकृत है)
- Padding ब्लॉक (वैकल्पिक)

कच्ची सामग्री:

#### दिनांक समय

- probing प्रतिरोध प्रदान करने के लिए, एक router को Session Request या Token Request संदेश के जवाब में Retry संदेश नहीं भेजना चाहिए जब तक कि Request संदेश में संदेश प्रकार, प्रोटोकॉल संस्करण, और नेटवर्क ID फ़ील्ड वैध न हों।
- नकली स्रोत पतों का उपयोग करके किए जा सकने वाले किसी भी amplification हमले की परिमाण को सीमित करने के लिए, Retry संदेश में बड़ी मात्रा में padding नहीं होनी चाहिए। यह अनुशंसा की जाती है कि Retry संदेश उस संदेश के आकार से तीन गुना से बड़ा न हो जिसका वह जवाब दे रहा है। वैकल्पिक रूप से, एक सरल विधि का उपयोग करें जैसे कि 1-64 बाइट्स की रेंज में यादृच्छिक मात्रा में padding जोड़ना।

### Token Request (प्रकार 10)

अशिफ्रीकृत डेटा (Poly1305 प्रमाणीकरण टैग दिखाया नहीं गया):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Hole Punch के लिए KDF

न्यूनतम payload का आकार 8 bytes है।

यह संदेश तेज़ी से उत्पन्न होना चाहिए, केवल symmetric encryption का उपयोग करके।

Charlie, Bob से प्राप्त Relay Intro के जवाब में Alice को भेजता है। Alice एक नए Session Request के साथ प्रतिक्रिया देती है। आकार: 48 + payload size।

Noise payload: नीचे देखें।

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
कच्ची सामग्री:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### विकल्प

- DateTime ब्लॉक
- Padding ब्लॉक

अनएन्क्रिप्टेड डेटा (Poly1305 प्रमाणीकरण टैग दिखाया नहीं गया):

#### RouterInfo

- probing प्रतिरोध प्रदान करने के लिए, एक router को Token Request message के जवाब में Retry message नहीं भेजना चाहिए जब तक कि Token Request message में message type, protocol version, और network ID fields वैध न हों।
- यह एक मानक Noise message नहीं है और handshake का हिस्सा नहीं है। यह connection IDs के अलावा Session Request message से बाध्य नहीं है।
- अधिकांश errors पर, AEAD सहित, या स्पष्ट replay पर Bob को आगे की message processing रोकनी चाहिए और बिना जवाब दिए message को drop कर देना चाहिए।
- Bob को उन connections को reject करना चाहिए जहाँ timestamp value वर्तमान समय से बहुत दूर है। अधिकतम delta time को "D" कहते हैं। Bob को पहले इस्तेमाल किए गए handshake values का एक local cache रखना चाहिए और replay attacks को रोकने के लिए duplicates को reject करना चाहिए। Cache में values का lifetime कम से कम 2*D होना चाहिए। Cache values implementation-dependent हैं, हालांकि 32-byte X value (या इसका encrypted equivalent) का उपयोग किया जा सकता है।
- Bob एक Retry message भेज सकता है जिसमें zero token और एक Termination block हो जिसमें clock skew reason code हो यदि DateTime block में timestamp बहुत अधिक skewed है।
- न्यूनतम size: TBD, Session Created के लिए समान नियम?

### होल पंच (टाइप 11)

न्यूनतम payload का आकार 8 bytes है। चूंकि DateTime और Address blocks का कुल योग इससे अधिक है, इसलिए केवल इन दो blocks से ही आवश्यकता पूरी हो जाती है।

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### पेलोड फॉर्मेट

Connection ID: दो connection ID relay nonce से प्राप्त किए जाते हैं। Destination Connection ID relay nonce के 4-byte big-endian की दो प्रतियां होती है, यानी ((nonce << 32) | nonce)। Source Connection ID, Destination Connection ID का उल्टा होता है, यानी ~((nonce << 32) | nonce)।

Alice को header में token को ignore करना चाहिए। Session Request में उपयोग होने वाला token Relay Response block में है।

प्रत्येक Noise payload में शून्य या अधिक "blocks" होते हैं।

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
यह [NTCP2](/docs/specs/ntcp2) और [ECIES](/docs/specs/ecies) विनिर्देशों में परिभाषित समान ब्लॉक प्रारूप का उपयोग करता है। व्यक्तिगत ब्लॉक प्रकार अलग तरीके से परिभाषित किए गए हैं। QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) में समकक्ष शब्द "frames" है।

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
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### I2NP Message

- DateTime ब्लॉक
- Address ब्लॉक
- Relay Response ब्लॉक
- Padding ब्लॉक (वैकल्पिक)

ऐसी चिंताएं हैं कि implementers को code साझा करने के लिए प्रोत्साहित करने से parsing की समस्याएं हो सकती हैं। Implementers को code साझा करने के फायदे और जोखिमों पर सावधानीपूर्वक विचार करना चाहिए, और यह सुनिश्चित करना चाहिए कि दोनों contexts के लिए ordering और valid block rules अलग हों।

encrypted payload में एक या अधिक blocks होते हैं। एक block एक सरल Tag-Length-Value (TLV) format है। प्रत्येक block में एक one-byte identifier, एक two-byte length, और शून्य या अधिक bytes का data होता है। यह format [NTCP2](/docs/specs/ntcp2) और [ECIES](/docs/specs/ecies) के समान है, हालांकि block definitions अलग हैं।

विस्तारशीलता के लिए, receivers को अज्ञात identifiers वाले blocks को नज़रअंदाज़ करना चाहिए, और उन्हें padding की तरह मानना चाहिए।

## Noise Payload

(Poly1305 auth tag नहीं दिखाया गया):

Header encryption पैकेट के अंतिम 24 bytes को दो ChaCha20 operations के लिए IV के रूप में उपयोग करता है। चूंकि सभी पैकेट 16 byte MAC के साथ समाप्त होते हैं, इसके लिए आवश्यक है कि सभी packet payloads न्यूनतम 8 bytes के हों। यदि कोई payload अन्यथा इस आवश्यकता को पूरा नहीं करता है, तो एक Padding block को शामिल करना होगा।

अधिकतम ChaChaPoly payload संदेश प्रकार, MTU, और IPv4 या IPv6 पता प्रकार के आधार पर भिन्न होता है। अधिकतम payload IPv4 के लिए MTU - 60 और IPv6 के लिए MTU - 80 है। अधिकतम payload डेटा IPv4 के लिए MTU - 63 और IPv6 के लिए MTU - 83 है। ऊपरी सीमा IPv4, 1500 MTU, Data संदेश के लिए लगभग 1440 bytes है। अधिकतम कुल block आकार अधिकतम payload आकार है। अधिकतम single block आकार अधिकतम कुल block आकार है। Block प्रकार 1 byte है। Block लंबाई 2 bytes है। अधिकतम single block डेटा आकार अधिकतम single block आकार माइनस 3 है।

### ब्लॉक क्रमबद्धता नियम

टिप्पणियाँ:

ब्लॉक प्रकार:

Session Confirmed में, Router Info पहला block होना चाहिए।

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
अन्य सभी संदेशों में, क्रम अनिर्दिष्ट है, निम्नलिखित आवश्यकताओं को छोड़कर: Padding, यदि मौजूद है, तो अंतिम block होना चाहिए। Termination, यदि मौजूद है, तो Padding को छोड़कर अंतिम block होना चाहिए। एकल payload में कई Padding blocks की अनुमति नहीं है।

समय सिंक्रोनाइज़ेशन के लिए:

नोट्स:

- Implementers को यह सुनिश्चित करना चाहिए कि जब एक block पढ़ते हैं, तो malformed या malicious data के कारण reads अगले block या payload boundary से आगे न बढ़ें।
- Implementations को forward compatibility के लिए unknown block types को ignore करना चाहिए।

अपडेटेड विकल्प पास करें। विकल्पों में शामिल हैं: न्यूनतम और अधिकतम padding।

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
### ब्लॉक विनिर्देश

Options block की लंबाई परिवर्तनीय होगी।

विकल्प संबंधी समस्याएं:

### सेशन अनुरोध

#### पहला खंड

Alice के RouterInfo को Bob को पास करें। केवल Session Confirmed part 2 payload में उपयोग किया जाता है। डेटा फेज में उपयोग न करें; इसके बजाय I2NP DatabaseStore Message का उपयोग करें।

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
न्यूनतम आकार: लगभग 420 बाइट्स, जब तक कि router info में router identity और signature संपीड़ित न हों, जो कि संभावना नहीं है।

- SSU 1 के विपरीत, SSU 2 में data phase के लिए packet header में कोई timestamp नहीं है।
- Implementations को data phase में समय-समय पर DateTime blocks भेजना चाहिए।
- Implementations को network में clock bias को रोकने के लिए निकटतम सेकंड तक round करना चाहिए।

#### अनुवर्ती खंड

नोट: Router Info ब्लॉक कभी भी fragmented नहीं होता है। frag फील्ड हमेशा 0/1 होता है। अधिक जानकारी के लिए ऊपर Session Confirmed Fragmentation सेक्शन देखें।

नोट्स:

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
एक संशोधित header के साथ पूर्ण I2NP message।

- Options negotiation TBD है।

#### समाप्ति

यह [NTCP2](/docs/specs/ntcp2) की तरह I2NP header के लिए समान 9 bytes का उपयोग करता है (type, message id, short expiration)।

नोट्स:

I2NP संदेश का पहला खंड (fragment #0) जिसमें संशोधित हेडर है।

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
यह [NTCP2](/docs/specs/ntcp2) की तरह I2NP header के लिए वही 9 bytes का उपयोग करता है (type, message id, short expiration)।

- Router Info को वैकल्पिक रूप से gzip के साथ संपीड़ित किया जाता है, जैसा कि flag bit 1 द्वारा इंगित किया गया है। यह NTCP2 से अलग है, जहाँ यह कभी संपीड़ित नहीं होता, और DatabaseStore Message से अलग है, जहाँ यह हमेशा संपीड़ित होता है। संपीड़न वैकल्पिक है क्योंकि यह आमतौर पर छोटे Router Infos के लिए कम फायदेमंद होता है, जहाँ कम संपीड़ित करने योग्य सामग्री होती है, लेकिन कई संपीड़ित करने योग्य Router Addresses वाले बड़े Router Infos के लिए बहुत फायदेमंद होता है। संपीड़न की सिफारिश की जाती है यदि यह Router Info को बिना fragmentation के एकल Session Confirmed packet में फिट करने की अनुमति देता है।
- Session Confirmed message में पहले या केवल fragment का अधिकतम आकार: IPv4 के लिए MTU - 113 या IPv6 के लिए MTU - 133। 1500 बाइट डिफ़ॉल्ट MTU मानते हुए, और message में कोई अन्य blocks नहीं, IPv4 के लिए 1387 या IPv6 के लिए 1367। वर्तमान router infos का 97% gzipping के बिना 1367 से छोटा है। वर्तमान router infos का 99.9% gzipped होने पर 1367 से छोटा है। 1280 बाइट न्यूनतम MTU मानते हुए, और message में कोई अन्य blocks नहीं, IPv4 के लिए 1167 या IPv6 के लिए 1147। वर्तमान router infos का 94% gzipping के बिना 1147 से छोटा है। वर्तमान router infos का 97% gzipped होने पर 1147 से छोटा है।
- frag byte अब अनुपयोगी है, Router Info block कभी fragmented नहीं होता। frag byte को fragment 0, total fragments 1 पर सेट किया जाना चाहिए। अधिक जानकारी के लिए ऊपर Session Confirmed Fragmentation अनुभाग देखें।
- Flooding का अनुरोध तब तक नहीं किया जाना चाहिए जब तक RouterInfo में प्रकाशित RouterAddresses न हों। प्राप्तकर्ता router को RouterInfo को तब तक flood नहीं करना चाहिए जब तक उसमें प्रकाशित RouterAddresses न हों।
- यह प्रोटोकॉल यह पुष्टि प्रदान नहीं करता कि RouterInfo संग्रहीत या flooded किया गया था। यदि पुष्टि वांछित है, और प्राप्तकर्ता floodfill है, तो भेजने वाले को इसके बजाय reply token के साथ एक मानक I2NP DatabaseStoreMessage भेजना चाहिए।

#### RelayRequest

टुकड़ों की कुल संख्या निर्दिष्ट नहीं है।

नोट्स:

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
एक I2NP संदेश का अतिरिक्त खंड (खंड संख्या शून्य से अधिक)।

- यह वही 9-बाइट I2NP हेडर फॉर्मेट है जो NTCP2 में उपयोग किया जाता है।
- यह बिल्कुल वही फॉर्मेट है जो First Fragment ब्लॉक का है, लेकिन ब्लॉक टाइप इंडिकेट करता है कि यह एक पूर्ण संदेश है।
- 9-बाइट I2NP हेडर सहित अधिकतम साइज़ IPv4 के लिए MTU - 63 और IPv6 के लिए MTU - 83 है।

#### RelayResponse

नोट्स:

कनेक्शन को छोड़ें। यह payload में अंतिम non-padding block होना चाहिए।

नोट्स:

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
सत्र के दौरान एक Data message में भेजा गया, Alice से Bob को। नीचे Relay Process अनुभाग देखें।

- यह वही 9-byte I2NP header format है जो NTCP2 में उपयोग किया जाता है।
- यह बिल्कुल वही format है जो I2NP Message block का है, लेकिन block type यह दर्शाता है कि यह संदेश का पहला fragment है।
- Partial message length शून्य से अधिक होना चाहिए।
- SSU 1 की तरह, यह सिफारिश की जाती है कि अंतिम fragment को पहले भेजा जाए, ताकि receiver को fragments की कुल संख्या पता चल जाए और वह receive buffers को कुशलता से allocate कर सके।
- 9-byte I2NP header सहित अधिकतम size IPv4 के लिए MTU - 63 और IPv6 के लिए MTU - 83 है।

#### RelayIntro

टिप्पणियाँ:

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
हस्ताक्षर:

- आंशिक संदेश की लंबाई शून्य से अधिक होनी चाहिए।
- SSU 1 की तरह, यह सुझाव दिया जाता है कि अंतिम fragment पहले भेजें, ताकि receiver को fragments की कुल संख्या पता चल जाए और वह receive buffers को कुशलतापूर्वक allocate कर सके।
- SSU 1 की तरह, अधिकतम fragment संख्या 127 है, लेकिन व्यावहारिक सीमा 63 या उससे कम है। Implementations लगभग 64 KB के अधिकतम I2NP संदेश आकार के लिए व्यावहारिक सीमा तक सीमित कर सकते हैं, जो 1280 न्यूनतम MTU के साथ लगभग 55 fragments है। नीचे Max I2NP Message Size अनुभाग देखें।
- अधिकतम आंशिक संदेश आकार (frag और message id को छोड़कर) IPv4 के लिए MTU - 68 और IPv6 के लिए MTU - 88 है।

#### PeerTest

Alice अनुरोध पर हस्ताक्षर करती है और इसे इस block में शामिल करती है; Bob इसे Relay Intro block में Charlie को forward करता है। Signature algorithm: निम्नलिखित डेटा पर Alice की router signing key के साथ हस्ताक्षर करें:

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
सेशन के दौरान Data message में भेजा जाता है, Charlie से Bob को या Bob से Alice को, और Charlie से Alice को Hole Punch message में भी। नीचे Relay Process सेक्शन देखें।

- सभी कारण वास्तव में उपयोग नहीं हो सकते हैं, implementation पर निर्भर है। अधिकांश विफलताएं आमतौर पर message को drop करने का परिणाम होंगी, termination का नहीं। ऊपर handshake message sections में notes देखें। सूचीबद्ध अतिरिक्त कारण consistency, logging, debugging, या यदि policy बदलती है तो के लिए हैं।
- यह अनुशंसा की जाती है कि Termination block के साथ एक ACK block शामिल किया जाए।
- Data phase में, "termination received" के अलावा किसी भी कारण से, peer को "termination received" कारण के साथ termination block के साथ respond करना चाहिए।

#### NextNonce

नोट्स:

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
टोकन का उपयोग Alice द्वारा Session Request में तुरंत किया जाना चाहिए।

- IP address हमेशा शामिल होता है (SSU 1 के विपरीत) और यह session के लिए उपयोग किए गए IP से अलग हो सकता है।

हस्ताक्षर:

यदि Charlie सहमत होता है (response code 0) या अस्वीकार करता है (response code 64 या उससे अधिक), तो Charlie response पर हस्ताक्षर करता है और इसे इस block में शामिल करता है; Bob इसे Relay Response block में Alice को भेज देता है। Signature algorithm: निम्नलिखित डेटा को Charlie के router signing key के साथ हस्ताक्षरित करें:

- prologue: 16 bytes "RelayRequestData", null-terminated नहीं (संदेश में शामिल नहीं)
- bhash: Bob का 32-byte router hash (संदेश में शामिल नहीं)
- chash: Charlie का 32-byte router hash (संदेश में शामिल नहीं)
- nonce: 4 byte nonce
- relay tag: 4 byte relay tag
- timestamp: 4 byte timestamp (सेकंड में)
- ver: 1 byte SSU version
- asz: 1 byte endpoint (port + IP) size (6 या 18)
- AlicePort: 2 byte Alice का port number
- Alice IP: (asz - 2) byte Alice IP address

#### पुष्टि

यदि Bob अस्वीकार करता है (response code 1-63), Bob response पर हस्ताक्षर करता है और इसे इस block में शामिल करता है। Signature algorithm: Bob की router signing key के साथ निम्नलिखित data पर हस्ताक्षर करें:

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
सत्र में Data संदेश में भेजा गया, Bob से Charlie को। नीचे Relay Process अनुभाग देखें।

इसके पहले एक RouterInfo ब्लॉक, या I2NP DatabaseStore message ब्लॉक (या fragment) होना चाहिए, जिसमें Alice की Router Info हो, या तो उसी payload में (यदि जगह हो), या पिछले message में।

नोट्स:

हस्ताक्षर:

- prologue: 16 bytes "RelayAgreementOK", null-terminated नहीं (संदेश में शामिल नहीं)
- bhash: Bob का 32-byte router hash (संदेश में शामिल नहीं)
- nonce: 4 byte nonce
- timestamp: 4 byte timestamp (सेकंड में)
- ver: 1 byte SSU version
- csz: 1 byte endpoint (port + IP) size (0 या 6 या 18)
- CharliePort: 2 byte Charlie का port number (यदि csz 0 है तो मौजूद नहीं)
- Charlie IP: (csz - 2) byte Charlie IP address (यदि csz 0 है तो मौजूद नहीं)

Alice अनुरोध पर हस्ताक्षर करती है और Bob इसे इस block में Charlie को भेज देता है। सत्यापन एल्गोरिदम: Alice के router signing key के साथ निम्नलिखित डेटा को सत्यापित करें:

- prologue: 16 बाइट्स "RelayAgreementOK", null-terminated नहीं (संदेश में शामिल नहीं)
- bhash: Bob का 32-बाइट router hash (संदेश में शामिल नहीं)
- nonce: 4 बाइट nonce
- timestamp: 4 बाइट timestamp (सेकंड)
- ver: 1 बाइट SSU version
- csz: 1 बाइट = 0

#### पता

या तो सत्र के दौरान Data संदेश में भेजा जाता है, या सत्र के बाहर Peer Test संदेश में। नीचे Peer Test Process अनुभाग देखें।

संदेश 2 के लिए, इससे पहले एक RouterInfo ब्लॉक या I2NP DatabaseStore संदेश ब्लॉक (या फ्रैगमेंट) होना चाहिए, जिसमें Alice का Router Info हो, या तो उसी payload में (यदि जगह है), या किसी पिछले संदेश में।

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
संदेश 4 के लिए, यदि relay स्वीकार किया जाता है (कारण कोड 0), तो इससे पहले एक RouterInfo ब्लॉक, या I2NP DatabaseStore संदेश ब्लॉक (या खंड) होना चाहिए, जिसमें Charlie की Router Info हो, या तो उसी payload में (यदि जगह है), या किसी पिछले संदेश में।

- IPv4 के लिए, Alice का IP address हमेशा 4 bytes का होता है, क्योंकि Alice IPv4 के माध्यम से Charlie से connect करने की कोशिश कर रहा है। IPv6 समर्थित है, और Alice का IP address 16 bytes का हो सकता है।
- IPv4 के लिए, यह message एक established IPv4 connection के माध्यम से भेजा जाना चाहिए, क्योंकि यही एकमात्र तरीका है जिससे Bob को Charlie का IPv4 address पता चलता है जिसे [RelayResponse](#relayresponse) में Alice को वापस करना है। IPv6 समर्थित है, और यह message एक established IPv6 connection के माध्यम से भेजा जा सकता है।
- introducers के साथ प्रकाशित किया गया कोई भी SSU address "caps" option में "4" या "6" शामिल करना चाहिए।

नोट्स:

Alice मौजूदा session का उपयोग करके transport (IPv4 या IPv6) के माध्यम से Bob को request भेजती है जिसे वह test करना चाहती है। जब Bob को Alice से IPv4 के माध्यम से request मिलती है, तो Bob को एक Charlie का चयन करना चाहिए जो IPv4 address advertise करता है। जब Bob को Alice से IPv6 के माध्यम से request मिलती है, तो Bob को एक Charlie का चयन करना चाहिए जो IPv6 address advertise करता है। वास्तविक Bob-Charlie communication IPv4 या IPv6 के माध्यम से हो सकती है (यानी, Alice के address type से स्वतंत्र)।

- prologue: 16 बाइट्स "RelayRequestData", null-terminated नहीं (संदेश में शामिल नहीं)
- bhash: Bob का 32-बाइट router hash (संदेश में शामिल नहीं)
- chash: Charlie का 32-बाइट router hash (संदेश में शामिल नहीं)
- nonce: 4 बाइट nonce
- relay tag: 4 बाइट relay tag
- timestamp: 4 बाइट timestamp (सेकंड में)
- ver: 1 बाइट SSU version
- asz: 1 बाइट endpoint (port + IP) साइज़ (6 या 18)
- AlicePort: 2 बाइट Alice का port नंबर
- Alice IP: (asz - 2) बाइट Alice IP address

#### रिले टैग अनुरोध

हस्ताक्षर:

Alice अनुरोध पर हस्ताक्षर करती है और इसे संदेश 1 में शामिल करती है; Bob इसे संदेश 2 में Charlie को अग्रेषित करता है। Charlie प्रतिक्रिया पर हस्ताक्षर करता है और इसे संदेश 3 में शामिल करता है; Bob इसे संदेश 4 में Alice को अग्रेषित करता है। हस्ताक्षर एल्गोरिदम: Alice की या Charlie की signing key के साथ निम्नलिखित डेटा पर हस्ताक्षर करें या सत्यापित करें:

TODO केवल यदि हम keys को rotate करते हैं

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
4 बाइट ack through, जिसके बाद एक ack count और शून्य या अधिक nack/ack ranges आते हैं।

- SSU 1 के विपरीत, message 1 में Alice का IP address और port शामिल होना चाहिए।

- IPv6 addresses का testing समर्थित है, और Alice-Bob तथा Alice-Charlie communication IPv6 के माध्यम से हो सकती है, यदि Bob और Charlie अपने published IPv6 address में 'B' capability के साथ समर्थन का संकेत देते हैं। विवरण के लिए Proposal 126 देखें।

यह डिज़ाइन QUIC से अनुकूलित और सरलीकृत है। डिज़ाइन के लक्ष्य निम्नलिखित हैं:

- Messages 1-4 को एक मौजूदा session में एक Data message में समाहित होना चाहिए।

- Bob को संदेश 2 भेजने से पहले Charlie को Alice का RI भेजना चाहिए।

- Bob को Alice को message 4 भेजने से पहले Charlie का RI भेजना होगा, यदि स्वीकार किया गया हो (reason code 0)।

- Messages 5-7 को एक Peer Test message में out-of-session होना चाहिए।

- संदेश 5 और 7 में वही हस्ताक्षरित डेटा हो सकता है जो संदेश 3 और 4 में भेजा गया था, या इसे नए timestamp के साथ पुनर्जनित किया जा सकता है। Signature वैकल्पिक है।

- Message 6 में वही signed डेटा हो सकता है जो messages 1 और 2 में भेजा गया था, या इसे नए timestamp के साथ पुनर्जनित किया जा सकता है। Signature वैकल्पिक है।

नीचे निर्दिष्ट encoding इन डिज़ाइन लक्ष्यों को पूरा करती है, उच्चतम bit की संख्या भेजकर जो 1 पर सेट है, उसके साथ अतिरिक्त लगातार bits भेजकर जो उससे कम हैं और जो भी 1 पर सेट हैं। उसके बाद, यदि जगह है, तो एक या अधिक "ranges" निर्दिष्ट करते हुए लगातार 0 bits की संख्या और लगातार 1 bits की संख्या जो उससे कम हैं। अधिक पृष्ठभूमि के लिए QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) section 13.2.3 देखें।

उदाहरण:

- prologue: 16 bytes "PeerTestValidate", null-terminated नहीं (संदेश में शामिल नहीं)
- bhash: Bob का 32-byte router hash (संदेश में शामिल नहीं)
- ahash: Alice का 32-byte router hash (केवल संदेश 3 और 4 के लिए signature में उपयोग; संदेश 3 या 4 में शामिल नहीं)
- ver: 1 byte SSU version
- nonce: 4 byte test nonce
- timestamp: 4 byte timestamp (सेकंड में)
- asz: 1 byte endpoint (port + IP) size (6 या 18)
- AlicePort: 2 byte Alice का port number
- Alice IP: (asz - 2) byte Alice IP address

#### रिले टैग

हम केवल packet 10 को ACK करना चाहते हैं:

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### नया टोकन

हम केवल पैकेट 8-10 को ACK करना चाहते हैं:

हम 10 9 8 6 5 2 1 0 को ACK करना चाहते हैं, और 7 4 3 को NACK करना चाहते हैं। ACK Block की encoding है:

- हम एक "bitfield" को कुशलता से एन्कोड करना चाहते हैं, जो acked packets का प्रतिनिधित्व करने वाले bits का एक क्रम है।
- bitfield में ज्यादातर 1's होते हैं। 1's और 0's दोनों आम तौर पर क्रमिक "clumps" में आते हैं।
- packet में acks के लिए उपलब्ध स्थान की मात्रा अलग-अलग होती है।
- सबसे महत्वपूर्ण bit सबसे बड़े नंबर वाला होता है। छोटे नंबर वाले कम महत्वपूर्ण होते हैं। सबसे बड़े bit से एक निश्चित दूरी के नीचे, पुराने bits "भुला दिए" जाएंगे और फिर कभी नहीं भेजे जाएंगे।

नोट्स:

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
2 बाइट पोर्ट और 4 या 16 बाइट IP पता। Alice का पता, Bob द्वारा Alice को भेजा गया, या Bob का पता, Alice द्वारा Bob को भेजा गया।

यह Alice द्वारा Session Request, Session Confirmed, या Data message में भेजा जा सकता है। Session Created message में समर्थित नहीं है, क्योंकि Bob के पास अभी तक Alice का RI नहीं है, और वह नहीं जानता कि Alice relay का समर्थन करता है या नहीं। साथ ही, यदि Bob को incoming connection मिल रहा है, तो उसे शायद introducers की आवश्यकता नहीं है (शायद अन्य प्रकार ipv4/ipv6 को छोड़कर)।

- Ack Through: 10
- acnt: 0
- कोई रेंज शामिल नहीं हैं

जब Session Request में भेजा जाता है, तो Bob Session Created संदेश में एक Relay Tag के साथ जवाब दे सकता है, या Alice की पहचान को validate करने के लिए Session Confirmed में Alice का RouterInfo प्राप्त होने तक प्रतीक्षा करने का चुनाव कर सकता है और फिर Data संदेश में जवाब दे सकता है। यदि Bob Alice के लिए relay नहीं करना चाहता है, तो वह Relay Tag block नहीं भेजता है।

- Ack Through: 10
- acnt: 2
- कोई ranges शामिल नहीं हैं

यह Bob द्वारा Session Confirmed या Data message में भेजा जा सकता है, Alice से Relay Tag Request के जवाब में।

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

जब Session Request में Relay Tag Request भेजा जाता है, तो Bob Session Created संदेश में Relay Tag के साथ प्रतिक्रिया दे सकता है, या Alice की पहचान को सत्यापित करने के लिए Session Confirmed में Alice का RouterInfo प्राप्त करने तक प्रतीक्षा करने का विकल्प चुन सकता है और फिर Data संदेश में प्रतिक्रिया दे सकता है। यदि Bob Alice के लिए relay नहीं करना चाहता, तो वह Relay Tag block नहीं भेजता।

- Ranges उपस्थित नहीं हो सकती हैं। Ranges की अधिकतम संख्या निर्दिष्ट नहीं है, packet में जितनी फिट हो सकें उतनी हो सकती हैं।
- Range nack शून्य हो सकता है यदि 255 से अधिक consecutive packets को ack कर रहे हैं।
- Range ack शून्य हो सकता है यदि 255 से अधिक consecutive packets को nack कर रहे हैं।
- Range nack और ack दोनों शून्य नहीं हो सकते।
- अंतिम range के बाद, packets न तो acked होते हैं और न ही nacked होते हैं। Ack block की लंबाई और पुराने acks/nacks को कैसे handle किया जाता है, यह ack block के भेजने वाले पर निर्भर है। चर्चा के लिए नीचे ack sections देखें।
- Ack through सबसे अधिक प्राप्त packet number होना चाहिए, और इससे ऊंचे कोई भी packets प्राप्त नहीं हुए हैं। हालांकि, सीमित स्थितियों में, यह कम हो सकता है, जैसे कि एक single packet को ack करना जो "एक hole को भरता है", या एक सरलीकृत implementation जो सभी प्राप्त packets की state को maintain नहीं करती। सबसे अधिक प्राप्त के ऊपर, packets न तो acked होते हैं और न ही nacked होते हैं, लेकिन कई ack blocks के बाद, fast retransmit mode में जाना उचित हो सकता है।
- यह format QUIC में उपयोग किए गए format का एक सरलीकृत version है। यह बड़ी संख्या में ACKs को efficiently encode करने के लिए designed है, NACKs के bursts के साथ।
- ACK blocks का उपयोग data phase packets को acknowledge करने के लिए किया जाता है। ये केवल in-session data phase packets के लिए include किए जाने हैं।

#### पाथ चैलेंज

बाद के कनेक्शन के लिए। आमतौर पर Session Created और Session Confirmed संदेशों में शामिल होता है। लंबे समय तक चलने वाले session में यदि पिछला token समाप्त हो जाता है तो इसे Data संदेश में फिर से भेजा जा सकता है।

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### पथ प्रतिक्रिया

एक Ping जिसमें मनमाना डेटा होता है जो Path Response में वापस किया जाता है, इसका उपयोग keep-alive के रूप में या IP/Port परिवर्तन को सत्यापित करने के लिए किया जाता है।

नोट्स:

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### पहला पैकेट नंबर

Path Challenge में प्राप्त डेटा के साथ एक Pong, Path Challenge के उत्तर के रूप में, keep-alive के रूप में या IP/Port परिवर्तन को मान्य करने के लिए उपयोग किया जाता है।

वैकल्पिक रूप से प्रत्येक दिशा में handshake में शामिल किया जाता है, पहले packet number को निर्दिष्ट करने के लिए जो भेजा जाएगा। यह header encryption के लिए अधिक सुरक्षा प्रदान करता है, TCP के समान।

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### भीड़भाड़

पूर्णतः निर्दिष्ट नहीं, वर्तमान में समर्थित नहीं।

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### पैडिंग

यह ब्लॉक congestion control की जानकारी का आदान-प्रदान करने के लिए एक विस्तारणीय विधि के रूप में डिज़ाइन किया गया है। Congestion control जटिल हो सकता है और जैसे-जैसे हमें लाइव टेस्टिंग में प्रोटोकॉल के साथ अधिक अनुभव मिलता है, या पूर्ण rollout के बाद, यह विकसित हो सकता है।

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
यह किसी भी congestion जानकारी को high-usage I2NP, First Fragment, Followon Fragment, और ACK blocks से बाहर रखता है, जहाँ flags के लिए कोई स्थान आवंटित नहीं है। जबकि Data packet header में तीन bytes के unused flags हैं, वह भी extensibility के लिए सीमित स्थान प्रदान करता है, और कमजोर encryption protection देता है।

- न्यूनतम 8 बाइट का डेटा आकार, जिसमें यादृच्छिक डेटा हो, की सिफारिश की जाती है लेकिन यह आवश्यक नहीं है।
- अधिकतम आकार निर्दिष्ट नहीं है, लेकिन यह 1280 से काफी कम होना चाहिए, क्योंकि path validation चरण के दौरान PMTU 1280 होता है।
- बड़े challenge आकार की सिफारिश नहीं की जाती क्योंकि वे packet amplification attacks के लिए एक वेक्टर हो सकते हैं।

#### पीयर एड्रेस स्पूफिंग

जबकि दो बिट्स की जानकारी के लिए 4-बाइट ब्लॉक का उपयोग करना कुछ हद तक बर्बादी है, इसे एक अलग ब्लॉक में रखने से हम इसे आसानी से अतिरिक्त डेटा जैसे वर्तमान विंडो साइज़, मापे गए RTT, या अन्य फ्लैग्स के साथ विस्तारित कर सकते हैं। अनुभव ने दिखाया है कि केवल फ्लैग बिट्स अक्सर अपर्याप्त और उन्नत कंजेशन कंट्रोल स्कीमों के कार्यान्वयन के लिए असुविधाजनक होते हैं। उदाहरण के लिए, ACK ब्लॉक में किसी भी संभावित कंजेशन कंट्रोल फीचर के लिए समर्थन जोड़ने की कोशिश करना स्थान की बर्बादी होगी और उस ब्लॉक की पार्सिंग में जटिलता जोड़ेगी।

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### ऑन-पाथ एड्रेस स्पूफिंग

implementations को यह नहीं मानना चाहिए कि दूसरा router यहाँ शामिल किसी विशेष flag bit या feature को support करता है, जब तक कि इस specification के भविष्य के version द्वारा implementation आवश्यक न हो।

यह ब्लॉक संभवतः payload में अंतिम गैर-padding ब्लॉक होना चाहिए।

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### ऑफ-पाथ पैकेट फॉरवर्डिंग

यह AEAD payloads के अंदर padding के लिए है। सभी संदेशों के लिए padding AEAD payloads के अंदर होती है।

Padding को negotiated parameters का मोटे तौर पर पालन करना चाहिए। Bob ने Session Created में अपने requested tx/rx min/max parameters भेजे थे। Alice ने Session Confirmed में अपने requested tx/rx min/max parameters भेजे थे। Data phase के दौरान updated options भेजे जा सकते हैं। ऊपर दिए गए options block information को देखें।

यदि मौजूद है, तो यह payload में अंतिम block होना चाहिए।

नोट्स:

SSU2 को एक आक्रमणकारी द्वारा दोहराए गए संदेशों के प्रभाव को कम करने के लिए डिज़ाइन किया गया है।

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### गोपनीयता के निहितार्थ

Token Request, Retry, Session Request, Session Created, Hole Punch, और out-of-session Peer Test संदेशों में DateTime blocks होना आवश्यक है।

Alice और Bob दोनों यह सत्यापित करते हैं कि इन messages का समय एक वैध skew (अनुशंसित +/- 2 मिनट) के भीतर है। "probing resistance" के लिए, Bob को Token Request या Session Request messages का उत्तर नहीं देना चाहिए यदि skew अवैध है, क्योंकि ये messages एक replay या probing attack हो सकते हैं।

Bob duplicate Token Request और Retry messages को reject करने का चुनाव कर सकता है, भले ही skew valid हो, Bloom filter या अन्य mechanism के माध्यम से। हालांकि, इन messages का जवाब देने की size और CPU cost कम है। सबसे खराब स्थिति में, एक replayed Token Request message पहले से भेजे गए token को invalidate कर सकता है।

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
टोकन सिस्टम replayed Session Request संदेशों के प्रभाव को काफी कम कर देता है। चूंकि टोकन केवल एक बार उपयोग किए जा सकते हैं, एक replayed Session Request संदेश में कभी भी वैध टोकन नहीं होगा। Bob Bloom filter या अन्य तंत्र के माध्यम से duplicate Session Request संदेशों को अस्वीकार करना चुन सकता है, भले ही skew वैध हो। हालांकि, Retry संदेश के साथ उत्तर देने का आकार और CPU लागत कम है। सबसे खराब स्थिति में, Retry संदेश भेजना पहले से भेजे गए टोकन को अमान्य कर सकता है।

- Size = 0 की अनुमति है।
- Padding रणनीतियाँ TBD।
- न्यूनतम padding TBD।
- केवल-Padding payloads की अनुमति है।
- Padding defaults TBD।
- Padding parameter बातचीत के लिए options block देखें
- न्यूनतम/अधिकतम padding parameters के लिए options block देखें
- MTU से अधिक न करें। यदि अधिक padding आवश्यक है, तो कई संदेश भेजें।
- बातचीत की गई padding के उल्लंघन पर router response implementation-dependent है।
- Padding की लंबाई या तो प्रति-संदेश आधार पर तय की जाती है और लंबाई वितरण के अनुमान, या random delays जोड़े जाने चाहिए। ये प्रतिउपाय DPI का विरोध करने के लिए शामिल किए जाते हैं, क्योंकि संदेश के आकार अन्यथा प्रकट कर देंगे कि I2P traffic transport protocol द्वारा ले जाया जा रहा है। सटीक padding scheme भविष्य के कार्य का क्षेत्र है, [NTCP2](/docs/specs/ntcp2) के Appendix A में इस विषय पर अधिक जानकारी प्रदान की गई है।

## पुनरावृत्ति रोकथाम

डुप्लिकेट Session Created और Session Confirmed मैसेज validate नहीं होंगे क्योंकि Noise handshake state उन्हें decrypt करने के लिए सही state में नहीं होगा। सबसे खराब स्थिति में, एक peer एक स्पष्ट डुप्लिकेट Session Created के जवाब में Session Confirmed को retransmit कर सकता है।

रीप्ले किए गए Hole Punch और Peer Test संदेशों का बहुत कम या कोई प्रभाव नहीं होना चाहिए।

Router को data message packet number का उपयोग करके duplicate data phase messages का पता लगाना और उन्हें drop करना चाहिए। प्रत्येक packet number का उपयोग केवल एक बार होना चाहिए। Replayed messages को ignore करना चाहिए।

यदि Alice को कोई Session Created या Retry प्राप्त नहीं होता है:

समान source और connection IDs, ephemeral key, और packet number 0 बनाए रखें। या फिर, केवल समान encrypted packet को बनाए रखें और पुनः प्रेषित करें। Packet number को बढ़ाया नहीं जाना चाहिए, क्योंकि इससे Session Created message को encrypt करने के लिए उपयोग किया जाने वाला chained hash value बदल जाएगा।

अनुशंसित पुनः प्रसारण अंतराल: 1.25, 2.5, और 5 सेकंड (पहली बार भेजने के 1.25, 3.75, और 8.75 सेकंड बाद)। अनुशंसित टाइमआउट: कुल 15 सेकंड

यदि Bob को कोई Session Confirmed प्राप्त नहीं होता है:

समान स्रोत और कनेक्शन IDs, ephemeral key, और packet number 0 बनाए रखें। या, केवल एन्क्रिप्टेड packet को बनाए रखें। Packet number को बढ़ाया नहीं जाना चाहिए, क्योंकि इससे Session Confirmed message को एन्क्रिप्ट करने के लिए उपयोग किया जाने वाला chained hash value बदल जाएगा।

## हैंडशेक पुन:प्रसारण

### सत्र बनाया गया

अनुशंसित पुनः प्रसारण अंतराल: 1, 2, और 4 सेकंड (पहली बार भेजे जाने के 1, 3, और 7 सेकंड बाद)। अनुशंसित timeout: कुल 12 सेकंड

SSU 1 में, Alice तब तक data phase में नहीं जाती जब तक Bob से पहला data packet प्राप्त नहीं हो जाता। इससे SSU 1 एक two-round-trip setup बन जाता है।

SSU 2 के लिए, अनुशंसित Session Confirmed पुनः प्रसारण अंतराल: 1.25, 2.5, और 5 सेकंड (पहली बार भेजे जाने के 1.25, 3.75, और 8.75 सेकंड बाद)।

### सत्र पुष्ट

कई विकल्प हैं। सभी 1 RTT हैं:

1) Alice मान लेती है कि Session Confirmed प्राप्त हो गया था, तुरंत data messages भेजती है, कभी भी Session Confirmed को पुनः प्रसारित नहीं करती। गलत क्रम में प्राप्त data packets (Session Confirmed से पहले) डिक्रिप्ट नहीं हो सकेंगे, लेकिन वे पुनः प्रसारित हो जाएंगे। यदि Session Confirmed खो जाता है, तो सभी भेजे गए data messages को drop कर दिया जाएगा। 2) जैसा कि 1) में है, data messages तुरंत भेजें, लेकिन तब तक Session Confirmed को भी पुनः प्रसारित करते रहें जब तक कोई data message प्राप्त नहीं होता। 3) हम XK के बजाय IK का उपयोग कर सकते हैं, क्योंकि इसमें handshake में केवल दो messages होते हैं, लेकिन यह एक अतिरिक्त DH का उपयोग करता है (3 के बजाय 4)।

अनुशंसित implementation विकल्प 2) है। Alice को Session Confirmed message को पुनः प्रसारित करने के लिए आवश्यक जानकारी बनाए रखनी चाहिए। Alice को Session Confirmed message के पुनः प्रसारित होने के बाद सभी Data messages को भी पुनः प्रसारित करना चाहिए।

### टोकन अनुरोध

Session Confirmed को पुनः भेजते समय, समान source और connection IDs, ephemeral key, और packet number 1 को बनाए रखें। या, केवल encrypted packet को बनाए रखें। Packet number को बढ़ाया नहीं जाना चाहिए, क्योंकि इससे chained hash value बदल जाएगी जो split() function के लिए एक input है।

Bob, Session Confirmed message प्राप्त होने से पहले मिले data messages को retain (queue) कर सकता है। Session Confirmed message प्राप्त होने से पहले न तो header protection keys और न ही decryption keys उपलब्ध होती हैं, इसलिए Bob को पता नहीं होता कि ये data messages हैं, लेकिन यह मान लिया जा सकता है। Session Confirmed message प्राप्त होने के बाद, Bob queued Data messages को decrypt और process करने में सक्षम हो जाता है। यदि यह बहुत जटिल है, तो Bob बस undecryptable Data messages को drop कर सकता है, क्योंकि Alice उन्हें retransmit करेगी।

नोट: यदि session confirmed पैकेट खो जाते हैं, तो Bob session created को फिर से भेजेगा। Session created हैडर Alice की intro key से decrypt नहीं हो सकेगा, क्योंकि यह Bob की intro key के साथ सेट किया गया है (जब तक कि Bob की intro key के साथ fallback decryption नहीं किया जाता)। Bob तुरंत session confirmed पैकेट को फिर से भेज सकता है यदि पहले से ack नहीं हुआ है, और एक undecryptable पैकेट प्राप्त होता है।

यदि Alice को कोई Retry प्राप्त नहीं होता:

समान source और connection ID बनाए रखें। एक implementation एक नया random packet number generate कर सकता है और एक नया packet encrypt कर सकता है; या यह समान packet number का पुन: उपयोग कर सकता है या बस समान encrypted packet को retain और retransmit कर सकता है। Packet number को increment नहीं करना चाहिए, क्योंकि इससे Session Created message को encrypt करने के लिए उपयोग की जाने वाली chained hash value बदल जाएगी।

अनुशंसित पुनः प्रसारण अंतराल: 3 और 6 सेकंड (पहली बार भेजने के बाद 3 और 9 सेकंड)। अनुशंसित टाइमआउट: कुल 15 सेकंड

यदि Bob को कोई Session Confirmed प्राप्त नहीं होता है:

Retry संदेश को timeout पर पुनः प्रेषित नहीं किया जाता है, ताकि नकली स्रोत पतों के प्रभावों को कम किया जा सके।

### पुनः प्रयास करें

हालांकि, एक Retry message को दोबारा भेजा जा सकता है यदि मूल (अमान्य) token के साथ एक दोहराया गया Session Request message प्राप्त होता है, या एक दोहराए गए Token Request message के जवाब में। दोनों मामलों में, यह इंगित करता है कि Retry message खो गया था।

यदि दूसरा Session Request message एक अलग लेकिन फिर भी अवैध token के साथ प्राप्त होता है, तो pending session को छोड़ दें और कोई प्रतिक्रिया न दें।

यदि Retry संदेश को पुनः भेजा जा रहा है: समान source और connection IDs तथा token बनाए रखें। एक implementation एक नया random packet number generate कर सकती है और एक नया packet encrypt कर सकती है; या यह समान packet number का पुनः उपयोग कर सकती है या केवल समान encrypted packet को retain करके retransmit कर सकती है।

### कुल समय सीमा

handshake के लिए अनुशंसित कुल timeout 20 सेकंड है।

तीन Noise handshake संदेशों Session Request, Session Created, और Session Confirmed के डुप्लिकेट्स को header के MixHash() से पहले detect किया जाना चाहिए। जबकि Noise AEAD प्रसंस्करण संभवतः उसके बाद fail हो जाएगा, handshake hash पहले से ही corrupt हो चुका होगा।

यदि तीन संदेशों में से कोई भी दूषित हो जाता है और AEAD में विफल हो जाता है, तो handshake को बाद में retransmission के साथ भी पुनर्प्राप्त नहीं किया जा सकता, क्योंकि MixHash() पहले से ही दूषित संदेश पर कॉल किया जा चुका है।

Session Request header में Token का उपयोग DoS शमन के लिए, source address spoofing को रोकने के लिए, और replay attacks के प्रतिरोध के रूप में किया जाता है।

यदि Bob Session Request संदेश में token को स्वीकार नहीं करता है, तो Bob संदेश को decrypt नहीं करता है, क्योंकि इसके लिए एक महंगी DH operation की आवश्यकता होती है। Bob केवल एक नए token के साथ Retry संदेश भेजता है।

### डुप्लिकेट और त्रुटि हैंडलिंग

यदि उस token के साथ कोई बाद का Session Request message प्राप्त होता है, तो Bob उस message को decrypt करने के लिए आगे बढ़ता है और handshake के साथ आगे बढ़ता है।

### पैकेट नंबर

टोकन एक यादृच्छिक रूप से उत्पन्न 8 बाइट मान होना चाहिए, यदि टोकन का जनरेटर मानों और संबंधित IP और port को संग्रहीत करता है (मेमोरी में या स्थायी रूप से)। जनरेटर एक अपारदर्शी मान उत्पन्न नहीं कर सकता, उदाहरण के लिए, IP, port, और वर्तमान घंटे या दिन के SipHash (एक गुप्त seed K0, K1 के साथ) का उपयोग करके, ऐसे टोकन बनाने के लिए जिन्हें मेमोरी में सहेजने की आवश्यकता नहीं है, क्योंकि यह विधि पुन: उपयोग किए गए टोकन और replay attacks को अस्वीकार करना कठिन बना देती है। हालांकि, यह आगे के अध्ययन का विषय है कि क्या हम ऐसी योजना में स्थानांतरित हो सकते हैं, जैसा कि [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) करता है, server secret और IP address के 16-बाइट HMAC का उपयोग करके।

टोकन केवल एक बार उपयोग किए जा सकते हैं। Bob से Alice को Retry संदेश में भेजा गया टोकन तुरंत उपयोग किया जाना चाहिए, और यह कुछ सेकंड में समाप्त हो जाता है। स्थापित सत्र में New Token ब्लॉक में भेजा गया टोकन बाद के कनेक्शन में उपयोग किया जा सकता है, और यह उस ब्लॉक में निर्दिष्ट समय पर समाप्त हो जाता है। समाप्ति भेजने वाले द्वारा निर्दिष्ट की जाती है; संग्रहीत टोकन के वांछित अधिकतम ओवरहेड के आधार पर, अनुशंसित मान न्यूनतम कई मिनट, अधिकतम एक या अधिक घंटे हैं।

## टोकन

यदि किसी router का IP या port बदल जाता है, तो उसे पुराने IP या port के लिए सभी सहेजे गए tokens (inbound और outbound दोनों) को हटाना होगा, क्योंकि वे अब मान्य नहीं हैं। Tokens को router restarts के दौरान वैकल्पिक रूप से बनाए रखा जा सकता है, यह implementation पर निर्भर करता है। एक unexpired token की स्वीकृति की गारंटी नहीं है; यदि Bob अपने सहेजे गए tokens को भूल गया है या हटा दिया है, तो वह Alice को एक Retry भेजेगा। एक router token storage को सीमित करना चुन सकता है, और सबसे पुराने stored tokens को हटा सकता है भले ही उनकी समय सीमा समाप्त न हुई हो।

नए Token blocks Alice से Bob को या Bob से Alice को भेजे जा सकते हैं। ये आमतौर पर कम से कम एक बार भेजे जाते हैं, session establishment के दौरान या उसके तुरंत बाद। Session Confirmed message में RouterInfo की validation checks के कारण, Bob को Session Created message में New Token block नहीं भेजना चाहिए, यह ACK 0 और Router Info के साथ भेजा जा सकता है जब Session Confirmed receive और validate हो जाए।

चूंकि सत्र की अवधि अक्सर token की समाप्ति से लंबी होती है, token को समाप्ति से पहले या बाद में नई समाप्ति समय के साथ पुनः भेजा जाना चाहिए, या एक नया token भेजा जाना चाहिए। Router को यह मान लेना चाहिए कि केवल अंतिम प्राप्त token ही मान्य है; समान IP/port के लिए कई inbound या outbound token संग्रहीत करने की कोई आवश्यकता नहीं है।

एक टोकन स्रोत IP/पोर्ट और गंतव्य IP/पोर्ट के संयोजन से बंधा होता है। IPv4 पर प्राप्त एक टोकन का उपयोग IPv6 के लिए नहीं किया जा सकता या इसके विपरीत।

यदि सत्र के दौरान कोई भी peer नए IP या port पर migrate हो जाता है (Connection Migration सेक्शन देखें), तो पहले से exchange किए गए सभी tokens अमान्य हो जाते हैं, और नए tokens का exchange करना होगा।

इम्प्लीमेंटेशन टोकन को डिस्क पर सेव कर सकते हैं और रीस्टार्ट पर उन्हें रीलोड कर सकते हैं, लेकिन यह आवश्यक नहीं है। यदि संग्रहीत किया जाता है, तो इम्प्लीमेंटेशन को यह सुनिश्चित करना होगा कि टोकन को रीलोड करने से पहले शटडाउन के बाद से IP और पोर्ट में कोई बदलाव नहीं हुआ है।

SSU 1 से अंतर

नोट: SSU 1 की तरह, प्रारंभिक fragment में fragments की कुल संख्या या कुल लंबाई की जानकारी नहीं होती। अगले fragments में उनके offset की जानकारी नहीं होती। यह sender को packet में उपलब्ध स्थान के आधार पर "on the fly" fragmenting की सुविधा प्रदान करता है। (Java I2P ऐसा नहीं करता; यह पहला fragment भेजने से पहले "pre-fragments" करता है) हालांकि, यह receiver पर बोझ डालता है कि वह गलत क्रम में प्राप्त fragments को स्टोर करे और सभी fragments प्राप्त होने तक reassembly में देरी करे।

SSU 1 की तरह, fragments के किसी भी retransmission में fragment के पिछले transmission की लंबाई (और implicit offset) को संरक्षित रखना आवश्यक है।

SSU 2 तीन मामलों (पूर्ण संदेश, प्रारंभिक खंड, और अनुवर्ती खंड) को तीन अलग block प्रकारों में अलग करता है, प्रसंस्करण दक्षता में सुधार के लिए।

यह प्रोटोकॉल I2NP संदेशों की डुप्लिकेट डिलीवरी को पूरी तरह से रोकता नहीं है। IP-layer डुप्लिकेट्स या replay attacks का पता SSU2 layer पर लगाया जाएगा, क्योंकि प्रत्येक packet number का उपयोग केवल एक बार ही किया जा सकता है।

## I2NP मैसेज फ्रैगमेंटेशन

जब I2NP messages या fragments को नए packets में retransmit किया जाता है, तो यह SSU2 layer पर detectable नहीं होता है। router को I2NP expiration को enforce करना चाहिए (बहुत पुराना और भविष्य में बहुत दूर दोनों) और I2NP message ID के आधार पर Bloom filter या अन्य mechanism का उपयोग करना चाहिए।

router द्वारा, या SSU2 implementation में, duplicates का पता लगाने के लिए अतिरिक्त mechanisms का उपयोग किया जा सकता है। उदाहरण के लिए, SSU2 हाल ही में प्राप्त message IDs का एक cache maintain कर सकता है। यह implementation-dependent है।

यह विनिर्देश packet numbering और ACK blocks के लिए protocol को निर्दिष्ट करता है। यह transmitter के लिए एक कुशल और responsive congestion control algorithm को implement करने के लिए पर्याप्त real-time जानकारी प्रदान करता है, जबकि उस implementation में लचीलेपन और नवाचार की अनुमति देता है। यह अनुभाग implementation के लक्ष्यों पर चर्चा करता है और सुझाव प्रदान करता है। सामान्य मार्गदर्शन [RFC-9002](https://tools.ietf.org/html/rfc9002) में पाया जा सकता है। retransmission timers पर मार्गदर्शन के लिए [RFC-6298](https://tools.ietf.org/html/rfc6298) भी देखें।

ACK-only डेटा packets को bytes या in-flight packets की गिनती में शामिल नहीं करना चाहिए और ये congestion-controlled नहीं हैं। TCP के विपरीत, SSU2 इन packets के loss का पता लगा सकता है और उस जानकारी का उपयोग congestion state को adjust करने के लिए किया जा सकता है। हालांकि, यह document ऐसा करने के लिए कोई mechanism निर्दिष्ट नहीं करता।

## I2NP संदेश डुप्लिकेशन

कुछ अन्य गैर-डेटा ब्लॉक्स वाले पैकेट्स को भी चाहने पर congestion control से बाहर रखा जा सकता है, यह implementation-dependent है। उदाहरण के लिए:

यह सुझाव दिया जाता है कि congestion control बाइट गिनती पर आधारित हो, पैकेट गिनती पर नहीं, TCP RFCs और QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002) में दिए गए मार्गदर्शन का पालन करते हुए। एक अतिरिक्त पैकेट गिनती सीमा भी उपयोगी हो सकती है kernel या middleboxes में buffer overflow को रोकने के लिए, implementation पर निर्भर करते हुए, हालांकि इससे काफी जटिलता बढ़ सकती है। यदि per-session और/या कुल पैकेट output bandwidth-limited और/या paced है, तो यह पैकेट गिनती सीमा की आवश्यकता को कम कर सकता है।

SSU 1 में, ACKs और NACKs में I2NP message numbers और fragment bitmasks होते थे। Transmitters ने outbound messages (और उनके fragments) की ACK status को track किया और आवश्यकतानुसार fragments को retransmit किया।

## कंजेशन कंट्रोल

SSU 2 में, ACK और NACK में packet numbers होते हैं। Transmitters को packet numbers और उनकी contents का mapping के साथ एक data structure बनाए रखना चाहिए। जब कोई packet ACK या NACK होता है, तो transmitter को यह निर्धारित करना चाहिए कि उस packet में कौन से I2NP messages और fragments थे, ताकि यह तय कर सके कि क्या retransmit करना है।

Bob पैकेट 0 का ACK भेजता है, जो Session Confirmed संदेश को स्वीकार करता है और Alice को डेटा चरण में आगे बढ़ने की अनुमति देता है, और संभावित पुनः प्रसारण के लिए सेव किए गए बड़े Session Confirmed संदेश को छोड़ने की अनुमति देता है। यह SSU 1 में Bob द्वारा भेजे गए DeliveryStatusMessage को बदल देता है।

Bob को Session Confirmed संदेश प्राप्त करने के तुरंत बाद जल्द से जल्द ACK भेजना चाहिए। एक छोटी देरी (50 ms से अधिक नहीं) स्वीकार्य है, क्योंकि Session Confirmed संदेश के तुरंत बाद कम से कम एक Data संदेश आना चाहिए, ताकि ACK Session Confirmed और Data संदेश दोनों की पुष्टि कर सके। इससे Bob को Session Confirmed संदेश को पुनः प्रेषित करने से बचा जा सकेगा।

- Peer Test
- Relay request/intro/response
- Path challenge/response

परिभाषा: Ack-eliciting packets: वे पैकेट जिनमें ack-eliciting blocks होते हैं, रिसीवर से अधिकतम acknowledgment delay के भीतर एक ACK प्राप्त करते हैं और इन्हें ack-eliciting packets कहा जाता है।

### सेशन पुष्टि ACK

Router सभी packets को acknowledge करते हैं जो वे receive और process करते हैं। हालांकि, केवल ack-eliciting packets के कारण maximum ack delay के भीतर एक ACK block भेजा जाता है। जो packets ack-eliciting नहीं हैं, वे केवल तभी acknowledge किए जाते हैं जब अन्य कारणों से ACK block भेजा जाता है।

किसी भी कारण से पैकेट भेजते समय, एक endpoint को ACK block शामिल करने का प्रयास करना चाहिए यदि हाल ही में कोई नहीं भेजा गया है। ऐसा करने से peer पर समयबद्ध loss detection में मदद मिलती है।

### ACKs जेनरेट करना

सामान्य तौर पर, receiver से बार-बार मिलने वाला feedback हानि और congestion response में सुधार करता है, लेकिन इसे उस अत्यधिक लोड के साथ संतुलित करना होता है जो एक receiver द्वारा उत्पन्न होता है जो हर ack-eliciting packet के जवाब में एक ACK block भेजता है। नीचे दी गई मार्गदर्शन इस संतुलन को बनाने का प्रयास करती है।

निम्नलिखित को छोड़कर किसी भी ब्लॉक वाले in-session डेटा पैकेट ack-eliciting होते हैं:

### Handshake ACKs

आउट-ऑफ सेशन पैकेट, जिनमें हैंडशेक संदेश और पीयर टेस्ट संदेश 5-7 शामिल हैं, के पास अपने स्वयं के पावती तंत्र हैं। नीचे देखें।

ये विशेष मामले हैं:

ACK blocks का उपयोग data phase packets को acknowledge करने के लिए किया जाता है। ये केवल in-session data phase packets के लिए ही शामिल किए जाने चाहिए।

हर packet को कम से कम एक बार acknowledge किया जाना चाहिए, और ack-eliciting packets को अधिकतम देरी के भीतर कम से कम एक बार acknowledge किया जाना चाहिए।

एक endpoint को अपनी अधिकतम देरी के भीतर तुरंत सभी ack-eliciting handshake packets को acknowledge करना चाहिए, निम्नलिखित अपवाद के साथ। handshake confirmation से पहले, एक endpoint के पास packet header encryption keys नहीं हो सकती हैं जो packets प्राप्त होने पर उन्हें decrypt करने के लिए आवश्यक हैं। इसलिए यह उन्हें buffer कर सकता है और जब आवश्यक keys उपलब्ध हो जाती हैं तो उन्हें acknowledge कर सकता है।

- ACK block
- Address block
- DateTime block
- Padding block
- Termination block
- अन्य?

चूंकि केवल ACK blocks वाले packets congestion controlled नहीं होते हैं, एक endpoint को ack-eliciting packet प्राप्त करने के जवाब में एक से अधिक ऐसे packet नहीं भेजने चाहिए।

### ACK Blocks भेजना

एक endpoint को non-ack-eliciting packet के जवाब में non-ack-eliciting packet नहीं भेजना चाहिए, भले ही प्राप्त packet से पहले packet gaps मौजूद हों। यह acknowledgments के अनंत feedback loop से बचाता है, जो connection को कभी idle होने से रोक सकता है। Non-ack-eliciting packets का अंततः acknowledgment तब होता है जब endpoint अन्य events के जवाब में ACK block भेजता है।

- Token Request को Retry द्वारा अंतर्निहित रूप से ack किया जाता है
- Session Request को Session Created या Retry द्वारा अंतर्निहित रूप से ack किया जाता है
- Retry को Session Request द्वारा अंतर्निहित रूप से ack किया जाता है
- Session Created को Session Confirmed द्वारा अंतर्निहित रूप से ack किया जाता है
- Session Confirmed को तुरंत ack किया जाना चाहिए

### ACK आवृत्ति

एक endpoint जो केवल ACK blocks भेज रहा है, उसे अपने peer से acknowledgments तब तक प्राप्त नहीं होंगे जब तक कि वे acknowledgments ack-eliciting blocks वाले packets में शामिल न हों। जब acknowledge करने के लिए नए ack-eliciting packets हों तो एक endpoint को अन्य blocks के साथ ACK block भेजना चाहिए। जब केवल non-ack-eliciting packets को acknowledge करना हो, तो एक endpoint तब तक outgoing blocks के साथ ACK block न भेजने का विकल्प चुन सकता है जब तक कि कोई ack-eliciting packet प्राप्त न हो जाए।

एक endpoint जो केवल non-ack-eliciting packets भेज रहा है, वह कभी-कभी उन packets में ack-eliciting block जोड़ने का विकल्प चुन सकता है ताकि यह सुनिश्चित हो सके कि उसे acknowledgment प्राप्त हो। उस स्थिति में, एक endpoint को उन सभी packets में ack-eliciting block नहीं भेजना चाहिए जो अन्यथा non-ack-eliciting होंगे, ताकि acknowledgments का अनंत feedback loop से बचा जा सके।

भेजने वाले (sender) पर loss detection में सहायता करने के लिए, एक endpoint को बिना देरी के ACK block generate करना और भेजना चाहिए जब वह इनमें से किसी भी स्थिति में ack-eliciting packet प्राप्त करता है:

एल्गोरिदम से अपेक्षा की जाती है कि वे उन receivers के प्रति resilient हों जो ऊपर दी गई guidance का पालन नहीं करते। हालांकि, एक implementation को इन requirements से केवल तभी विचलित होना चाहिए जब endpoint द्वारा बनाए गए connections और network के अन्य उपयोगकर्ताओं के लिए किसी बदलाव के performance implications पर सावधानीपूर्वक विचार किया गया हो।

एक रिसीवर यह निर्धारित करता है कि ack-eliciting packets के जवाब में कितनी बार acknowledgments भेजना है। इस निर्धारण में एक trade-off शामिल है।

Endpoints हानि का पता लगाने के लिए समय पर acknowledgment पर निर्भर करते हैं। Window-based congestion controllers अपनी congestion window को प्रबंधित करने के लिए acknowledgments पर निर्भर करते हैं। दोनों मामलों में, acknowledgments में देरी करना प्रदर्शन पर प्रतिकूल प्रभाव डाल सकता है।

दूसरी ओर, उन packets की आवृत्ति को कम करना जो केवल acknowledgments ले जाते हैं, दोनों endpoints पर packet transmission और processing cost को कम करता है। यह गंभीर रूप से असममित links पर connection throughput में सुधार कर सकता है और return path capacity का उपयोग करते हुए acknowledgment traffic की मात्रा को कम कर सकता है; [RFC-3449](https://tools.ietf.org/html/rfc3449) का Section 3 देखें।

एक receiver को कम से कम दो ack-eliciting packets प्राप्त करने के बाद एक ACK block भेजना चाहिए। यह सिफारिश सामान्य प्रकृति की है और TCP endpoint व्यवहार के लिए सिफारिशों के साथ संगत है [RFC-5681](https://tools.ietf.org/html/rfc5681)। नेटवर्क की स्थितियों का ज्ञान, peer के congestion controller का ज्ञान, या आगे के अनुसंधान और प्रयोग बेहतर प्रदर्शन विशेषताओं के साथ वैकल्पिक acknowledgment रणनीतियों का सुझाव दे सकते हैं।

- जब प्राप्त packet का packet number किसी अन्य ack-eliciting packet से कम हो जो पहले से प्राप्त हो चुका है
- जब packet का packet number सबसे अधिक संख्या वाले ack-eliciting packet से बड़ा हो जो प्राप्त हुआ है और उस packet और इस packet के बीच कुछ packets गुम हैं।
- जब packet header में ack-immediate flag सेट हो

एक receiver प्रतिक्रिया में ACK block भेजने का निर्धारण करने से पहले कई उपलब्ध packets को प्रोसेस कर सकता है। सामान्यतः, receiver को ACK को RTT / 6, या अधिकतम 150 ms से अधिक विलंबित नहीं करना चाहिए।

### तत्काल ACK फ्लैग

डेटा पैकेट हेडर में ack-immediate फ्लैग एक अनुरोध है कि रिसीवर रिसेप्शन के तुरंत बाद, शायद कुछ ms के भीतर ack भेजे। सामान्यतः, रिसीवर को immediate ACK को RTT / 16, या अधिकतम 5 ms से ज्यादा देरी नहीं करनी चाहिए।

प्राप्तकर्ता को भेजने वाले की send window size का पता नहीं होता, और इसलिए वह नहीं जानता कि ACK भेजने से पहले कितनी देर प्रतीक्षा करनी है। डेटा पैकेट header में immediate ACK flag प्रभावी RTT को कम करके अधिकतम throughput बनाए रखने का एक महत्वपूर्ण तरीका है। Immediate ACK flag header byte 13, bit 0 में होता है, यानी (header[13] & 0x01)। जब यह सेट होता है, तो तत्काल ACK का अनुरोध किया जाता है। विवरण के लिए ऊपर दिया गया short header अनुभाग देखें।

भेजने वाले के पास immediate-ack फ्लैग कब सेट करना है, यह निर्धारित करने के लिए कई संभावित रणनीतियां हैं:

तत्काल ACK flags केवल उन data packets पर आवश्यक होने चाहिए जिनमें I2NP messages या message fragments हों।

जब एक ACK block भेजा जाता है, तो एक या अधिक acknowledged packets की ranges शामिल होती हैं। पुराने packets के लिए acknowledgments शामिल करना पहले भेजे गए ACK blocks के खोने के कारण होने वाले spurious retransmissions की संभावना को कम करता है, बड़े ACK blocks की कीमत पर।

ACK blocks को हमेशा सबसे हाल ही में प्राप्त packets को acknowledge करना चाहिए, और packets जितने अधिक गलत क्रम में हों, उतना ही महत्वपूर्ण है कि updated ACK block को तुरंत भेजा जाए, ताकि peer को किसी packet को lost घोषित करने और उसमें निहित blocks को गलत तरीके से retransmit करने से रोका जा सके। एक ACK block को एक single packet के भीतर fit होना चाहिए। यदि ऐसा नहीं है, तो पुराने ranges (जिनमें सबसे छोटे packet numbers हैं) को छोड़ दिया जाता है।

### ACK ब्लॉक साइज़

एक receiver उन ACK ranges की संख्या को सीमित करता है जिन्हें वह याद रखता है और ACK blocks में भेजता है, दोनों ACK blocks के आकार को सीमित करने और संसाधन समाप्ति से बचने के लिए। एक ACK block के लिए acknowledgments प्राप्त करने के बाद, receiver को उन acknowledged ACK ranges को track करना बंद कर देना चाहिए। Senders अधिकांश packets के लिए acknowledgments की उम्मीद कर सकते हैं, लेकिन यह protocol हर उस packet के लिए acknowledgment प्राप्त होने की गारंटी नहीं देता जिसे receiver process करता है।

यह संभव है कि कई ACK ranges को बनाए रखने से ACK block बहुत बड़ा हो सकता है। एक receiver अस्वीकृत ACK Ranges को छोड़ सकता है ताकि ACK block का आकार सीमित हो सके, भले ही इससे sender से अधिक retransmissions हों। यह आवश्यक है यदि ACK block किसी packet में फिट होने के लिए बहुत बड़ा हो। Receivers ACK block के आकार को और भी सीमित कर सकते हैं ताकि अन्य blocks के लिए जगह बचाई जा सके या acknowledgments द्वारा उपयोग की जाने वाली bandwidth को सीमित किया जा सके।

- हर N packets में एक बार सेट करें, कुछ छोटे N के लिए
- packet के burst में अंतिम पर सेट करें
- जब भी send window लगभग भरा हो तो सेट करें, उदाहरण के लिए 2/3 से अधिक भरा हो
- retransmitted fragments के साथ सभी packets पर सेट करें

एक receiver को ACK range को तब तक बनाए रखना चाहिए जब तक वह यह सुनिश्चित न कर सके कि वह बाद में उस range में numbers वाले packets को स्वीकार नहीं करेगा। ranges को discard करने के साथ-साथ बढ़ने वाला minimum packet number बनाए रखना न्यूनतम state के साथ इसे प्राप्त करने का एक तरीका है।

### ACK ब्लॉक्स को ट्रैक करके रेंज को सीमित करना

रिसीवर सभी ACK रेंज को हटा सकते हैं, लेकिन उन्हें सबसे बड़ा पैकेट नंबर बनाए रखना चाहिए जो सफलतापूर्वक प्रोसेस किया गया है, क्योंकि इसका उपयोग बाद के पैकेट्स से पैकेट नंबर रिकवर करने के लिए किया जाता है।

निम्नलिखित खंड प्रत्येक ACK ब्लॉक में किन पैकेटों को acknowledge करना है, इसे निर्धारित करने के लिए एक उदाहरणीय दृष्टिकोण का वर्णन करता है। यद्यपि इस एल्गोरिदम का लक्ष्य प्रत्येक पैकेट के लिए एक acknowledgment उत्पन्न करना है जो प्रोसेस किया जाता है, फिर भी acknowledgments के खो जाने की संभावना रहती है।

जब एक ACK block वाला packet भेजा जाता है, तो उस block में Ack Through field को save किया जा सकता है। जब एक ACK block वाले packet को acknowledge किया जाता है, तो receiver उन packets को acknowledge करना बंद कर सकता है जो भेजे गए ACK block के Ack Through field से कम या बराबर हैं।

एक receiver जो केवल non-ack-eliciting packets भेजता है, जैसे कि ACK blocks, वह लंबे समय तक acknowledgment प्राप्त नहीं कर सकता है। इससे receiver को लंबे समय तक बड़ी संख्या में ACK blocks के लिए state बनाए रखना पड़ सकता है, और जो ACK blocks वह भेजता है वे अनावश्यक रूप से बड़े हो सकते हैं। ऐसी स्थिति में, एक receiver कभी-कभार एक PING या अन्य छोटा ack-eliciting block भेज सकता है, जैसे कि प्रति round trip एक बार, ताकि peer से ACK प्राप्त हो सके।

ACK block loss के बिना मामलों में, यह algorithm कम से कम 1 RTT के reordering की अनुमति देता है। ACK block loss और reordering वाले मामलों में, यह approach इस बात की गारंटी नहीं देता कि प्रत्येक acknowledgment को sender द्वारा देखा जाए इससे पहले कि वह ACK block में शामिल न रहे। Packets गलत क्रम में प्राप्त हो सकते हैं, और उन्हें शामिल करने वाले सभी बाद के ACK blocks खो सकते हैं। इस स्थिति में, loss recovery algorithm गलत retransmissions का कारण बन सकता है, लेकिन sender आगे की प्रगति करना जारी रखेगा।

I2P transports I2NP messages की in-order delivery की गारंटी नहीं देते। इसलिए, एक या अधिक I2NP messages या fragments वाले Data message का loss अन्य I2NP messages की delivery को रोकता नहीं है; यहाँ कोई head-of-line blocking नहीं है। Implementations को loss recovery phase के दौरान नए messages भेजना जारी रखना चाहिए यदि send window इसकी अनुमति देती है।

एक sender को संदेश की पूर्ण सामग्री को बनाए नहीं रखना चाहिए, ताकि उसे समान रूप से पुनः प्रसारित किया जा सके (handshake messages को छोड़कर, ऊपर देखें)। एक sender को हर बार संदेश भेजते समय अद्यतन जानकारी (ACKs, NACKs, और unacknowledged data) युक्त संदेश तैयार करना चाहिए। एक sender को संदेशों से जानकारी को पुनः प्रसारित करने से बचना चाहिए जब वे acknowledge हो जाते हैं। इसमें वे संदेश शामिल हैं जो lost घोषित होने के बाद acknowledge होते हैं, जो network reordering की उपस्थिति में हो सकता है।

### भीड़भाड़

TBD। सामान्य मार्गदर्शन [RFC-9002](https://tools.ietf.org/html/rfc9002) में मिल सकता है।

एक peer का IP या port एक session के जीवनकाल के दौरान बदल सकता है। IP परिवर्तन IPv6 temporary address rotation, ISP-संचालित आवधिक IP परिवर्तन, WiFi और cellular IP के बीच संक्रमण करने वाले mobile client, या अन्य local network परिवर्तनों के कारण हो सकता है। Port परिवर्तन पिछली binding के timeout होने के बाद NAT rebinding के कारण हो सकता है।

एक peer का IP या port विभिन्न on-path और off-path हमलों के कारण बदला हुआ दिख सकता है, जिसमें packets को modify करना या inject करना शामिल है।

### पुनः प्रेषण

Connection migration वह प्रक्रिया है जिसके द्वारा एक नया source endpoint (IP+port) को वैलिडेट किया जाता है, जबकि उन परिवर्तनों को रोका जाता है जो वैलिडेट नहीं हैं। यह प्रक्रिया QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) में परिभाषित प्रक्रिया का एक सरलीकृत संस्करण है। यह प्रक्रिया केवल session के data phase के लिए परिभाषित है। Handshake के दौरान migration की अनुमति नहीं है। सभी handshake packets को यह सत्यापित करना होगा कि वे उसी IP और port से आए हैं जैसे पहले भेजे और प्राप्त किए गए packets। दूसरे शब्दों में, handshake के दौरान एक peer का IP और port स्थिर होना चाहिए।

### विंडो

(QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) से अनुकूलित)

### खतरा मॉडल

एक peer अपने source address को spoof कर सकता है ताकि एक endpoint को किसी अनिच्छुक host की ओर अत्यधिक मात्रा में डेटा भेजने के लिए प्रेरित किया जा सके। यदि endpoint spoofing peer की तुलना में काफी अधिक डेटा भेजता है, तो connection migration का उपयोग उस डेटा की मात्रा को बढ़ाने के लिए किया जा सकता है जो एक आक्रमणकारी किसी पीड़ित के विरुद्ध उत्पन्न कर सकता है।

## कनेक्शन माइग्रेशन

एक on-path attacker पैकेट को कॉपी करके और spoofed address के साथ forward करके एक झूठा connection migration का कारण बन सकता है, जिससे यह मूल पैकेट से पहले पहुंच जाए। spoofed address वाला पैकेट एक migrating connection से आने वाला दिखाई देगा, और मूल पैकेट को duplicate माना जाकर drop कर दिया जाएगा। एक झूठे migration के बाद, source address का validation fail हो जाएगा क्योंकि source address पर मौजूद entity के पास Path Challenge को पढ़ने या उसका जवाब देने के लिए आवश्यक cryptographic keys नहीं हैं, भले ही वह चाहे भी।

एक off-path हमलावर जो packets को observe कर सकता है, वह genuine packets की copies को endpoints तक forward कर सकता है। यदि copied packet, genuine packet से पहले पहुंचता है, तो यह NAT rebinding की तरह दिखाई देगा। कोई भी genuine packet को duplicate के रूप में discard कर दिया जाएगा। यदि हमलावर packets को forward करना जारी रखने में सक्षम है, तो वह हमलावर के माध्यम से एक path पर migration का कारण बन सकता है। यह हमलावर को on-path रखता है, जिससे उसे बाद के सभी packets को observe करने या drop करने की क्षमता मिल जाती है।

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) ने नेटवर्क पथ बदलते समय connection ID बदलने की निर्देशना दी है। कई नेटवर्क पथों पर एक स्थिर connection ID का उपयोग करने से एक निष्क्रिय निरीक्षक (passive observer) उन पथों के बीच गतिविधि को सहसंबंधित कर सकता है। एक endpoint जो नेटवर्क के बीच जाता है, वह नहीं चाहेगा कि उनकी गतिविधि को उनके peer के अलावा किसी अन्य entity द्वारा सहसंबंधित किया जाए। हालांकि, QUIC header में connection ID को एन्क्रिप्ट नहीं करता है। SSU2 यह करता है, इसलिए privacy leak के लिए निष्क्रिय निरीक्षक को connection ID को decrypt करने के लिए आवश्यक introduction key प्राप्त करने हेतु network database तक पहुंच की भी आवश्यकता होगी। introduction key के साथ भी, यह कोई मजबूत attack नहीं है, और हम SSU2 में migration के बाद connection ID नहीं बदलते हैं, क्योंकि यह एक महत्वपूर्ण जटिलता होगी।

### पथ सत्यापन प्रारंभ करना

डेटा चरण के दौरान, peers को प्रत्येक प्राप्त डेटा पैकेट के source IP और port की जांच करनी चाहिए। यदि IP या port पहले प्राप्त किए गए से अलग है, और पैकेट एक duplicate packet number नहीं है, और पैकेट सफलतापूर्वक decrypt हो जाता है, तो session path validation चरण में प्रवेश करता है।

#### Introducer चयन

इसके अतिरिक्त, एक peer को यह सत्यापित करना होगा कि नया IP और port स्थानीय सत्यापन नियमों के अनुसार वैध हैं (अवरुद्ध नहीं, अवैध ports नहीं, आदि)। Peers को IPv4 और IPv6 के बीच migration का समर्थन करना आवश्यक नहीं है, और वे दूसरे address family में एक नए IP को अवैध मान सकते हैं, क्योंकि यह अपेक्षित व्यवहार नहीं है और महत्वपूर्ण implementation जटिलता जोड़ सकता है। एक अवैध IP/port से packet प्राप्त करने पर, एक implementation इसे सरल रूप से drop कर सकती है, या पुराने IP/port के साथ path validation शुरू कर सकती है।

#### प्रतिक्रिया प्रबंधन

path validation चरण में प्रवेश करने पर, निम्नलिखित चरण उठाएं:

#### परिचयकर्ता

path validation चरण के दौरान, session आने वाले packets को process करना जारी रख सकता है। चाहे वे पुराने या नए IP/port से आ रहे हों। session data packets को भेजना और acknowledge करना भी जारी रख सकता है। हालांकि, path validation चरण के दौरान congestion window और PMTU को न्यूनतम मानों पर बना रहना चाहिए, ताकि spoofed address पर बड़ी मात्रा में traffic भेजकर denial of service attacks के लिए उपयोग होने से रोका जा सके।

#### पहचान छिपाना

एक implementation एक साथ कई paths को validate करने का प्रयास कर सकती है, लेकिन यह आवश्यक नहीं है। यह संभवतः complexity के लायक नहीं है। यह पिछले IP/port को पहले से validated के रूप में याद रख सकती है, और यदि कोई peer अपने पिछले IP/port पर वापस आ जाता है तो path validation को skip कर सकती है, लेकिन यह आवश्यक नहीं है।

### संदेश सामग्री

यदि एक Path Response प्राप्त होता है, जिसमें Path Challenge में भेजा गया समान डेटा होता है, तो Path Validation सफल हो गया है। Path Response संदेश का स्रोत IP/port वही होना आवश्यक नहीं है जिस पर Path Challenge भेजा गया था।

यदि Path Response timer की समय सीमा समाप्त होने से पहले Path Response प्राप्त नहीं होता है, तो दूसरा Path Challenge भेजें और Path Response timer को दोगुना करें।

यदि Path Validation टाइमर समाप्त होने से पहले Path Response प्राप्त नहीं होता है, तो Path Validation असफल हो गया है।

- कई सेकंड का, या वर्तमान RTO के कई गुना का path validation timeout timer शुरू करें (TBD)
- congestion window को न्यूनतम तक कम करें
- PMTU को न्यूनतम (1280) तक कम करें
- नए IP और port पर एक data packet भेजें जिसमें Path Challenge block, Address block (नया IP/port युक्त), और आमतौर पर एक ACK block हो। यह packet वर्तमान session के समान connection ID और encryption keys का उपयोग करता है। Path Challenge block data में पर्याप्त entropy (कम से कम 8 bytes) होना चाहिए ताकि इसे spoof नहीं किया जा सके।
- वैकल्पिक रूप से, पुराने IP/port पर भी अलग block data के साथ Path Challenge भेजें। नीचे देखें।
- वर्तमान RTO के आधार पर Path Response timeout timer शुरू करें (आमतौर पर RTT + RTTdev का गुणांक)

Data messages में निम्नलिखित blocks होने चाहिए। Order निर्दिष्ट नहीं है सिवाय इसके कि Padding अंत में होना चाहिए:

संदेश में किसी अन्य blocks (उदाहरण के लिए, I2NP) को शामिल करने की अनुशंसा नहीं है।

Path Response वाले संदेश में Path Challenge block को शामिल करने की अनुमति है, ताकि दूसरी दिशा में validation शुरू की जा सके।

Path Challenge और Path Response ब्लॉक्स ACK-eliciting हैं। Path Challenge को एक Data संदेश द्वारा ACK किया जाएगा जिसमें Path Response और ACK ब्लॉक्स होंगे। Path Response को एक Data संदेश द्वारा ACK किया जाना चाहिए जिसमें एक ACK ब्लॉक हो।

QUIC विशिष्टता इस बारे में स्पष्ट नहीं है कि path validation के दौरान डेटा पैकेट कहाँ भेजे जाएं - पुराने या नए IP/port पर? IP/port परिवर्तनों का तेजी से जवाब देने और spoofed addresses पर ट्रैफिक न भेजने के बीच संतुलन बनाना होता है। इसके अलावा, spoofed पैकेट को मौजूदा session पर काफी प्रभाव डालने की अनुमति नहीं देनी चाहिए। Port-only परिवर्तन संभावित रूप से idle अवधि के बाद NAT rebinding के कारण हो सकते हैं; IP परिवर्तन एक या दोनों दिशाओं में high-traffic phases के दौरान हो सकते हैं।

### Path Validation के दौरान Routing

रणनीतियाँ अनुसंधान और सुधार के अधीन हैं। संभावनाओं में शामिल हैं:

- Path Challenge या Path Response ब्लॉक। Path Challenge में अपारदर्शी डेटा होता है, न्यूनतम 8 बाइट्स अनुशंसित। Path Response में Path Challenge का डेटा होता है।
- Address ब्लॉक जिसमें प्राप्तकर्ता का स्पष्ट IP होता है
- DateTime ब्लॉक
- ACK ब्लॉक
- Padding ब्लॉक

Path Challenge प्राप्त करने पर, peer को एक data packet के साथ जवाब देना चाहिए जिसमें Path Response हो, जिसमें Path Challenge का डेटा शामिल हो।

Path Response को उसी IP/port पर भेजा जाना चाहिए जहाँ से Path Challenge प्राप्त हुआ था। यह जरूरी नहीं है कि यह वही IP/port हो जो पहले से peer के लिए स्थापित था। यह सुनिश्चित करता है कि peer द्वारा path validation तभी सफल हो जब path दोनों दिशाओं में कार्यशील हो। नीचे Validation after Local Change सेक्शन देखें।

जब तक IP/port peer के लिए पहले से ज्ञात IP/port से अलग नहीं है, Path Challenge को एक साधारण ping की तरह मानें, और बिना शर्त Path Response के साथ उत्तर दें। receiver किसी प्राप्त Path Challenge के आधार पर कोई state नहीं रखता या बदलता है। यदि IP/port अलग है, तो एक peer को यह सत्यापित करना होगा कि नया IP और port स्थानीय validation नियमों के अनुसार वैध हैं (blocked नहीं, अवैध ports नहीं, आदि)। Peers को IPv4 और IPv6 के बीच cross-address-family responses का समर्थन करना आवश्यक नहीं है, और वे दूसरे address family में नए IP को अवैध मान सकते हैं, क्योंकि यह अपेक्षित व्यवहार नहीं है।

### Path Challenge का जवाब देना

जब तक congestion control द्वारा बाधित न हो, Path Response तुरंत भेजा जाना चाहिए। यदि आवश्यक हो तो implementations को Path Responses या उपयोग की जाने वाली bandwidth को rate limit करने के उपाय करने चाहिए।

एक Path Challenge block आमतौर पर उसी संदेश में एक Address block के साथ आता है। यदि address block में एक नया IP/port है, तो एक peer उस IP/port को validate कर सकता है और उस नए IP/port का peer testing शुरू कर सकता है, session peer या किसी अन्य peer के साथ। यदि peer को लगता है कि वह firewalled है, और केवल port बदला है, तो यह परिवर्तन संभवतः NAT rebinding के कारण है, और आगे peer testing की शायद आवश्यकता नहीं है।

- नए IP/port को validate होने तक डेटा packets नहीं भेजना
- नया IP/port validate होने तक पुराने IP/port पर डेटा packets भेजना जारी रखना
- साथ ही साथ पुराने IP/port को revalidate करना
- पुराना या नया IP/port में से कोई भी validate होने तक कोई डेटा नहीं भेजना
- केवल port बदलाव के लिए IP बदलाव से अलग रणनीति
- समान /32 में IPv6 बदलाव के लिए अलग रणनीति, जो संभावित रूप से temporary address rotation के कारण हो

### सफल पथ सत्यापन

सफल पथ सत्यापन पर, कनेक्शन को पूर्णतः नए IP/port पर स्थानांतरित कर दिया जाता है। सफलता पर:

पाथ वैलिडेशन फेज के दौरान, पुराने IP/port से प्राप्त कोई भी वैध, गैर-डुप्लिकेट पैकेट्स जो सफलतापूर्वक डिक्रिप्ट हो जाते हैं, Path Validation को रद्द कर देंगे। यह महत्वपूर्ण है कि स्पूफ्ड पैकेट के कारण रद्द किया गया पाथ वैलिडेशन, किसी वैध सेशन को समाप्त या महत्वपूर्ण रूप से बाधित न करे।

रद्द किए गए path validation पर:

यह महत्वपूर्ण है कि एक असफल path validation, जो spoofed packet के कारण होता है, किसी वैध session को समाप्त या महत्वपूर्ण रूप से बाधित न करे।

असफल पाथ सत्यापन पर:

### पथ सत्यापन रद्द करना

उपरोक्त प्रक्रिया उन peers के लिए परिभाषित है जो बदले हुए IP/port से packet प्राप्त करते हैं। हालांकि, यह दूसरी दिशा में भी शुरू की जा सकती है, ऐसे peer द्वारा जो पता लगाता है कि उसका IP या port बदल गया है। एक peer यह पता लगाने में सक्षम हो सकता है कि उसका local IP बदल गया है; हालांकि, NAT rebinding के कारण उसके लिए यह पता लगाना कि उसका port बदल गया है, बहुत कम संभावना है। इसलिए, यह वैकल्पिक है।

- path validation चरण से बाहर निकलें
- सभी packets नए IP और port पर भेजे जाते हैं।
- congestion window और PMTU पर प्रतिबंध हटा दिए जाते हैं, और उन्हें बढ़ने की अनुमति दी जाती है। उन्हें केवल पुराने values पर restore न करें, क्योंकि नए path की विशेषताएं अलग हो सकती हैं।
- यदि IP बदल गया है, तो calculated RTT और RTO को initial values पर set करें। क्योंकि port-only changes आमतौर पर NAT rebinding या अन्य middlebox गतिविधि का परिणाम होते हैं, peer इसके बजाय initial values पर revert करने के बजाय अपनी congestion control state और round-trip estimate को retain कर सकता है।
- पुराने IP/port के लिए भेजे गए या प्राप्त किए गए किसी भी tokens को delete (invalidate) करें (वैकल्पिक)
- नए IP/port के लिए एक नया token block भेजें (वैकल्पिक)

### पाथ वैलिडेशन विफल

जब किसी peer से path challenge प्राप्त हो जिसका IP या port बदल गया हो, तो दूसरे peer को विपरीत दिशा में path challenge शुरू करना चाहिए।

Path Challenge और Path Response blocks का उपयोग किसी भी समय Ping/Pong packets के रूप में किया जा सकता है। Path Challenge block की प्राप्ति receiver पर किसी भी state को नहीं बदलती, जब तक कि यह किसी अलग IP/port से प्राप्त न हो।

- पथ सत्यापन चरण से बाहर निकलें
- सभी पैकेट पुराने IP और port पर भेजे जाते हैं।
- congestion window और PMTU पर प्रतिबंध हटा दिए जाते हैं, और उन्हें बढ़ने की अनुमति दी जाती है, या वैकल्पिक रूप से, पिछले मान पुनर्स्थापित करें
- किसी भी डेटा पैकेट को retransmit करें जो पहले नए IP/port पर भेजे गए थे, उन्हें पुराने IP/port पर भेजें।

### स्थानीय परिवर्तन के बाद सत्यापन

Peers को एक ही peer के साथ कई sessions स्थापित नहीं करने चाहिए, चाहे वह SSU 1 या 2 हो, या समान या अलग IP addresses के साथ हो। हालांकि, यह हो सकता है, या तो bugs के कारण, या पिछले session termination message के खो जाने के कारण, या एक race की स्थिति में जहां termination message अभी तक नहीं आया है।

यदि Bob का Alice के साथ एक मौजूदा session है, जब Bob को Alice से Session Confirmed प्राप्त होता है, handshake पूरा करके और एक नया session स्थापित करके, Bob को चाहिए:

- path validation चरण से बाहर निकलें
- सभी packets पुराने IP और port पर भेजे जाते हैं।
- congestion window और PMTU पर लगी पाबंदियाँ हटा दी जाती हैं, और उन्हें बढ़ने की अनुमति दी जाती है।
- वैकल्पिक रूप से, पुराने IP और port पर path validation शुरू करें। यदि यह विफल हो जाता है, तो session को समाप्त कर दें।
- अन्यथा, मानक session timeout और समाप्ति नियमों का पालन करें।
- किसी भी data packets को जो पहले नए IP/port पर भेजे गए थे, पुराने IP/port पर फिर से भेजें।

### Ping/Pong के रूप में उपयोग करें

हैंडशेक चरण में sessions आमतौर पर केवल timeout करके या आगे respond नहीं करके समाप्त हो जाते हैं। वैकल्पिक रूप से, response में Termination block शामिल करके भी इन्हें समाप्त किया जा सकता है, लेकिन cryptographic keys की कमी के कारण अधिकांश errors का जवाब देना संभव नहीं होता। यदि termination block सहित response के लिए keys उपलब्ध हैं, तो भी आमतौर पर response के लिए DH perform करना CPU के लिए उपयुक्त नहीं होता। एक अपवाद retry message में Termination block हो सकता है, जो generate करने में कम खर्चीला होता है।

डेटा चरण में sessions को एक डेटा संदेश भेजकर समाप्त किया जाता है जिसमें एक Termination block शामिल होता है। इस संदेश में एक ACK block भी शामिल होना चाहिए। यदि session काफी लंबे समय से चालू है कि पहले भेजा गया token समाप्त हो गया है या समाप्त होने वाला है, तो इसमें एक New Token block भी शामिल हो सकता है। यह संदेश ack-eliciting नहीं है। "Termination Received" को छोड़कर किसी भी कारण से Termination block प्राप्त करने पर, peer "Termination Received" कारण के साथ Termination block वाले डेटा संदेश से जवाब देता है।

### हैंडशेक चरण

Termination block भेजने या प्राप्त करने के बाद, session को कुछ अधिकतम समय अवधि TBD के लिए closing phase में प्रवेश करना चाहिए। closing state आवश्यक है ताकि Termination block वाले packet के खो जाने और दूसरी दिशा में in-flight packets से सुरक्षा हो सके। closing phase के दौरान, कोई भी अतिरिक्त प्राप्त packets को process करने की आवश्यकता नहीं है। closing state में एक session किसी भी incoming packet के जवाब में Termination block वाला packet भेजता है जिसे वह session के लिए attribute करता है। एक session को closing state में packets generate करने की दर को सीमित करना चाहिए। उदाहरण के लिए, एक session प्राप्त packets की progressively बढ़ती संख्या या समय की मात्रा का इंतजार कर सकता है, प्राप्त packets का जवाब देने से पहले।

## एकाधिक सत्र

एक बंद हो रहे session के लिए router द्वारा बनाए रखी जाने वाली state को कम करने के लिए, sessions वैसा ही packet भेज सकते हैं (लेकिन जरूरी नहीं है) जिसमें वही packet number हो जैसा कि किसी भी प्राप्त packet के जवाब में है। नोट: termination packet के retransmission की अनुमति देना इस आवश्यकता का अपवाद है कि हर packet के लिए एक नया packet number इस्तेमाल किया जाए। नए packet numbers भेजना मुख्य रूप से loss recovery और congestion control के लिए फायदेमंद है, जिनकी एक बंद connection के लिए प्रासंगिकता की उम्मीद नहीं है। अंतिम packet को retransmit करने के लिए कम state की आवश्यकता होती है।

"Termination Received" कारण के साथ Termination block प्राप्त करने के बाद, session closing phase से बाहर निकल सकता है।

- पुराने session से नए session में किसी भी अनभेजे या अस्वीकृत outbound I2NP संदेशों को स्थानांतरित करें
- पुराने session पर reason code 22 के साथ एक termination भेजें
- पुराने session को हटा दें और इसे नए session से बदल दें

## सत्र समाप्ति

### डेटा चरण

किसी भी सामान्य या असामान्य समाप्ति पर, routers को किसी भी in-memory ephemeral डेटा को शून्य कर देना चाहिए, जिसमें handshake ephemeral keys, symmetric crypto keys, और संबंधित जानकारी शामिल है।

### सफाई

आवश्यकताएं अलग होती हैं, इस आधार पर कि प्रकाशित पता SSU 1 के साथ साझा किया गया है या नहीं। वर्तमान SSU 1 IPv4 न्यूनतम 620 है, जो निश्चित रूप से बहुत छोटा है।

न्यूनतम SSU2 MTU IPv4 और IPv6 दोनों के लिए 1280 है, जो [RFC-9000](https://tools.ietf.org/html/rfc9000) में निर्दिष्ट के समान है। नीचे देखें। न्यूनतम MTU बढ़ाने से, 1 KB tunnel संदेश और छोटे tunnel build संदेश एक datagram में फिट हो जाएंगे, जिससे सामान्य fragmentation की मात्रा काफी कम हो जाएगी। यह अधिकतम I2NP संदेश आकार में वृद्धि की भी अनुमति देता है। 1820-बाइट streaming संदेश दो datagrams में फिट होने चाहिए।

एक router को SSU2 सक्षम नहीं करना चाहिए या SSU2 पता प्रकाशित नहीं करना चाहिए जब तक कि उस पते के लिए MTU कम से कम 1280 न हो।

राउटर्स को प्रत्येक SSU या SSU2 राउटर पते में एक गैर-डिफ़ॉल्ट MTU प्रकाशित करना चाहिए।

### SSU Address

SSU 1 के साथ साझा पता, SSU 1 नियमों का पालन करना आवश्यक। IPv4: डिफ़ॉल्ट और अधिकतम 1484 है। न्यूनतम 1292 है। (IPv4 MTU + 4) 16 का गुणज होना चाहिए। IPv6: प्रकाशित होना आवश्यक, न्यूनतम 1280 और अधिकतम 1488 है। IPv6 MTU 16 का गुणज होना चाहिए।

## MTU

IPv4: डिफ़ॉल्ट और अधिकतम 1500 है। न्यूनतम 1280 है। IPv6: डिफ़ॉल्ट और अधिकतम 1500 है। न्यूनतम 1280 है। 16 के गुणज के नियम नहीं हैं, लेकिन कम से कम 2 का गुणज होना चाहिए।

SSU 1 के लिए, वर्तमान Java I2P छोटे पैकेट्स से शुरू करके और धीरे-धीरे आकार बढ़ाकर, या प्राप्त पैकेट आकार के आधार पर बढ़ाकर PMTU discovery करता है। यह कच्चा तरीका है और दक्षता को काफी कम कर देता है। SSU 2 में इस सुविधा को जारी रखना TBD है।

हाल के अध्ययन [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) सुझाते हैं कि IPv4 के लिए 1200 या अधिक का न्यूनतम आकार 99% से अधिक कनेक्शन के लिए काम करेगा। QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) के लिए न्यूनतम IP पैकेट आकार 1280 बाइट्स की आवश्यकता होती है।

[RFC-9000](https://tools.ietf.org/html/rfc9000) का उद्धरण:

### SSU2 Address

अधिकतम datagram आकार को सबसे बड़े UDP payload के आकार के रूप में परिभाषित किया गया है जो एक single UDP datagram का उपयोग करके network path पर भेजा जा सकता है। यदि network path कम से कम 1200 bytes के अधिकतम datagram आकार का समर्थन नहीं कर सकता है तो QUIC का उपयोग नहीं किया जाना चाहिए।

### PMTU खोज

QUIC कम से कम 1280 बाइट्स के न्यूनतम IP पैकेट आकार की अपेक्षा करता है। यह IPv6 न्यूनतम आकार [IPv6] है और अधिकांश आधुनिक IPv4 नेटवर्क द्वारा भी समर्थित है। IPv6 के लिए 40 बाइट्स और IPv4 के लिए 20 बाइट्स के न्यूनतम IP हेडर आकार और 8 बाइट्स के UDP हेडर आकार को मानते हुए, इसके परिणामस्वरूप IPv6 के लिए अधिकतम डेटाग्राम आकार 1232 बाइट्स और IPv4 के लिए 1252 बाइट्स होता है। इस प्रकार, आधुनिक IPv4 और सभी IPv6 नेटवर्क पथों से QUIC को समर्थन करने में सक्षम होने की अपेक्षा की जाती है।

### हैंडशेक न्यूनतम आकार

नोट: UDP payload के 1200 bytes को support करने की यह आवश्यकता IPv6 extension headers के लिए उपलब्ध स्थान को 32 bytes तक या IPv4 options को 52 bytes तक सीमित करती है यदि path केवल IPv6 के minimum MTU 1280 bytes को support करता है। यह Initial packets और path validation को प्रभावित करता है।

उद्धरण समाप्त

QUIC की आवश्यकता है कि दोनों दिशाओं में Initial datagrams कम से कम 1200 bytes के हों, amplification attacks को रोकने के लिए और यह सुनिश्चित करने के लिए कि PMTU दोनों दिशाओं में इसका समर्थन करता है।

हम Session Request और Session Created के लिए इसकी आवश्यकता कर सकते हैं, bandwidth में काफी लागत के साथ। शायद हम यह तभी कर सकें जब हमारे पास कोई token न हो, या Retry message प्राप्त होने के बाद। TBD

QUIC की आवश्यकता है कि Bob क्लाइंट पता सत्यापित होने तक प्राप्त डेटा की मात्रा से तीन गुना से अधिक डेटा न भेजे। SSU2 इस आवश्यकता को स्वाभाविक रूप से पूरा करता है, क्योंकि Retry मैसेज Token Request मैसेज के लगभग समान आकार का है, और Session Request मैसेज से छोटा है। इसके अलावा, Retry मैसेज केवल एक बार भेजा जाता है।

QUIC की आवश्यकता है कि PATH_CHALLENGE या PATH_RESPONSE blocks वाले संदेश कम से कम 1200 बाइट्स के हों, amplification attacks को रोकने के लिए और यह सुनिश्चित करने के लिए कि PMTU दोनों दिशाओं में इसका समर्थन करता है।

हम इसे भी आवश्यक बना सकते हैं, bandwidth में काफी लागत के साथ। हालांकि, ये मामले दुर्लभ होने चाहिए। TBD

### पथ संदेश न्यूनतम आकार

IPv4: कोई IP fragmentation की अपेक्षा नहीं है। IP + datagram header 28 bytes का है। यह मानता है कि कोई IPv4 options नहीं हैं। अधिकतम message size MTU - 28 है। Data phase header 16 bytes और MAC 16 bytes का है, कुल मिलाकर 32 bytes। Payload size MTU - 60 है। अधिकतम 1500 MTU के लिए अधिकतम data phase payload 1440 है। न्यूनतम 1280 MTU के लिए अधिकतम data phase payload 1220 है।

IPv6: कोई IP fragmentation की अनुमति नहीं है। IP + datagram header 48 bytes का है। यह मानता है कि कोई IPv6 extension headers नहीं हैं। अधिकतम message size MTU - 48 है। Data phase header 16 bytes का है और MAC 16 bytes का है, कुल मिलाकर 32 bytes। Payload size MTU - 80 है। अधिकतम 1500 MTU के लिए अधिकतम data phase payload 1420 है। न्यूनतम 1280 MTU के लिए अधिकतम data phase payload 1200 है।

SSU 1 में, दिशानिर्देश 64 अधिकतम fragments और 620 न्यूनतम MTU के आधार पर I2NP message के लिए लगभग 32 KB की एक कड़ी अधिकतम सीमा थे। bundled LeaseSets और session keys के overhead के कारण, application स्तर पर व्यावहारिक सीमा लगभग 6KB कम थी, या लगभग 26KB। SSU 1 protocol 128 fragments की अनुमति देता है लेकिन वर्तमान implementations इसे 64 fragments तक सीमित करते हैं।

### अधिकतम I2NP संदेश आकार

न्यूनतम MTU को 1280 तक बढ़ाकर, लगभग 1200 के डेटा फेज पेलोड के साथ, लगभग 76 KB का एक SSU 2 मैसेज 64 fragments में संभव है और 152 KB 128 fragments में। यह आसानी से अधिकतम 64 KB की अनुमति देता है।

tunnel में fragmentation और SSU 2 में fragmentation के कारण, message का size बढ़ने के साथ message loss की संभावना तेज़ी से बढ़ती है। हम I2NP datagram के लिए application layer पर लगभग 10 KB की व्यावहारिक सीमा की सिफारिश करना जारी रखते हैं।

### संस्करण

SSU1 Peer Test के विश्लेषण और SSU2 Peer Test के लक्ष्यों के लिए ऊपर Peer Test Security देखें।

जब Bob द्वारा अस्वीकार किया जाता है:

जब Charlie द्वारा अस्वीकार किया जाता है:

नोट: RI को या तो I2NP blocks में I2NP Database Store messages के रूप में भेजा जा सकता है, या RI blocks के रूप में (यदि काफी छोटा हो)। ये peer test blocks के समान packets में शामिल हो सकते हैं, यदि काफी छोटे हों।

संदेश 1-4 एक Data संदेश में Peer Test blocks का उपयोग करके in-session हैं। संदेश 5-7 एक Peer Test संदेश में Peer Test blocks का उपयोग करके out-of-session हैं।

## पीयर टेस्ट प्रक्रिया

नोट: SSU 1 की तरह ही, संदेश 4 और 5 किसी भी क्रम में आ सकते हैं। यदि Alice firewalled है तो संदेश 5 और/या 7 बिल्कुल प्राप्त नहीं हो सकते हैं। जब संदेश 5, संदेश 4 से पहले आता है, तो Alice तुरंत संदेश 6 नहीं भेज सकती, क्योंकि उसके पास अभी तक header को encrypt करने के लिए Charlie की intro key नहीं है। जब संदेश 4, संदेश 5 से पहले आता है, तो Alice को तुरंत संदेश 6 नहीं भेजना चाहिए, क्योंकि उसे यह देखने के लिए प्रतीक्षा करनी चाहिए कि क्या संदेश 6 के साथ firewall खोले बिना संदेश 5 आता है।

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
क्रॉस-वर्जन peer परीक्षण समर्थित नहीं है। केवल अनुमतित वर्जन संयोजन वह है जहाँ सभी peer वर्जन 2 के हों।

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
संदेश 1-4 in-session में हैं और data phase ACK और retransmission प्रक्रियाओं द्वारा कवर किए जाते हैं। Peer Test blocks ack-eliciting होते हैं।

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
संदेश 5-7 को बिना परिवर्तन के पुनः प्रसारित किया जा सकता है।

SSU 1 की तरह, IPv6 पतों का परीक्षण समर्थित है, और Alice-Bob और Alice-Charlie संचार IPv6 के माध्यम से हो सकता है, यदि Bob और Charlie अपने प्रकाशित IPv6 पते में 'B' capability के साथ समर्थन का संकेत देते हैं। विवरण के लिए Proposal 126 देखें।

SSU 1 में 0.9.50 से पहले की तरह, Alice उस transport (IPv4 या IPv6) पर एक मौजूदा session का उपयोग करके Bob को request भेजती है जिसका वह परीक्षण करना चाहती है। जब Bob को Alice से IPv4 के माध्यम से request प्राप्त होती है, तो Bob को एक ऐसा Charlie चुनना होगा जो IPv4 address का विज्ञापन करता है। जब Bob को Alice से IPv6 के माध्यम से request प्राप्त होती है, तो Bob को एक ऐसा Charlie चुनना होगा जो IPv6 address का विज्ञापन करता है। वास्तविक Bob-Charlie संचार IPv4 या IPv6 के माध्यम से हो सकता है (यानी, Alice के address type से स्वतंत्र)। यह SSU 1 का व्यवहार नहीं है जैसा कि 0.9.50 में है, जहाँ मिश्रित IPv4/v6 requests की अनुमति है।

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
### पुनर्प्रसारण

SSU 1 के विपरीत, Alice संदेश 1 में अनुरोधित परीक्षण IP और port निर्दिष्ट करती है। Bob को इस IP और port को सत्यापित करना चाहिए, और यदि अमान्य है तो कोड 5 के साथ अस्वीकार करना चाहिए। अनुशंसित IP सत्यापन यह है कि IPv4 के लिए, यह Alice के IP से मेल खाता है, और IPv6 के लिए, IP के कम से कम पहले 8 बाइट्स मेल खाते हैं। Port सत्यापन में विशेषाधिकार प्राप्त ports और प्रसिद्ध प्रोटोकॉल के लिए उपयोग किए जाने वाले ports को अस्वीकार करना चाहिए।

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
### IPv6 नोट्स

यहाँ हम दस्तावेज़ीकृत करते हैं कि Alice कैसे peer test के परिणामों को निर्धारित कर सकती है, इस आधार पर कि कौन से संदेश प्राप्त हुए हैं। SSU2 के सुधार हमें [SSU](/docs/transport/ssu) की तुलना में peer test परिणाम state machine को ठीक करने, सुधारने और बेहतर दस्तावेज़ीकरण का अवसर प्रदान करते हैं।

प्रत्येक परीक्षित पता प्रकार (IPv4 या IPv6) के लिए, परिणाम UNKNOWN, OK, FIREWALLED, या SYMNAT में से कोई एक हो सकता है। इसके अतिरिक्त, IP या port परिवर्तन का पता लगाने के लिए, या आंतरिक port से भिन्न बाहरी port का पता लगाने के लिए अन्य प्रसंस्करण भी किया जा सकता है।

### Bob द्वारा प्रसंस्करण

प्रलेखित SSU state machine के साथ समस्याएं:

तो, SSU के विपरीत, हम message 4 प्राप्त करने के बाद कई सेकंड प्रतीक्षा करने की सिफारिश करते हैं, फिर message 6 भेजते हैं भले ही message 5 प्राप्त न हुआ हो।

### परिणाम स्टेट मशीन

स्थिति मशीन का सारांश, इस आधार पर कि संदेश 4, 5, और 7 प्राप्त हुए हैं या नहीं (हाँ या नहीं), निम्नलिखित है:

### पुनः प्रसारण

एक अधिक विस्तृत स्टेट मशीन, message 7 के address block में प्राप्त IP/port की जांच के साथ, नीचे दी गई है। एक चुनौती यह निर्धारित करना है कि क्या आप (Alice) symmetric natted हैं, या Charlie है।

दो या अधिक peer परीक्षणों पर समान परिणामों की आवश्यकता के द्वारा स्थिति संक्रमण की पुष्टि करने के लिए पोस्ट-प्रोसेसिंग या अतिरिक्त तर्क की सिफारिश की जाती है।

दो या अधिक परीक्षणों द्वारा प्राप्त IP/port सत्यापन और पुष्टि, या Session Created संदेशों में address block के साथ, भी अनुशंसित है, लेकिन यह इस विनिर्देश के दायरे से बाहर है।

- हम कभी भी message 6 नहीं भेजते जब तक हमें message 5 नहीं मिला है, इसलिए हम कभी नहीं जानते कि हम SYMNAT हैं या नहीं
- यदि हमें messages 4 और 7 मिले थे, तो हम कैसे संभवतः SYMNAT हो सकते हैं
- यदि IP match नहीं किया लेकिन port ने किया, तो हम SYMNAT नहीं हैं, हमने बस अपना IP बदला है

SSU1 Relay का विश्लेषण और SSU2 Relay के लक्ष्यों के लिए ऊपर दी गई Relay Security देखें।

जब Bob द्वारा अस्वीकार किया जाता है:

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
जब Charlie द्वारा अस्वीकार किया जाता है:

नोट: RI को या तो I2NP blocks में I2NP Database Store messages के रूप में भेजा जा सकता है, या RI blocks के रूप में (यदि पर्याप्त छोटा हो)। यदि पर्याप्त छोटे हों तो ये relay blocks के समान packets में शामिल हो सकते हैं।

SSU 1 में, Charlie की router जानकारी में प्रत्येक introducer का IP, port, intro key, relay tag, और expiration शामिल होता है।

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## रिले प्रक्रिया

SSU 2 में, Charlie की router info में प्रत्येक introducer का router hash, relay tag, और expiration शामिल होता है।

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Alice को पहले एक introducer (Bob) का चयन करके आवश्यक round trips की संख्या कम करनी चाहिए जिससे उसका पहले से ही कनेक्शन हो। दूसरे, यदि कोई नहीं है, तो एक introducer का चयन करें जिसके लिए उसके पास पहले से ही router info हो।

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
यदि संभव हो तो Cross-version relaying का भी समर्थन किया जाना चाहिए। यह SSU 1 से SSU 2 में क्रमिक संक्रमण की सुविधा प्रदान करेगा। अनुमतित version combinations हैं (TODO):

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
नोट: RI को I2NP ब्लॉक में I2NP डेटाबेस स्टोर संदेशों के रूप में भेजा जा सकता है, या RI ब्लॉक के रूप में (यदि आकार छोटा है)। यदि आकार छोटा है तो इन्हें रिले ब्लॉक के साथ एक ही पैकेट में शामिल किया जा सकता है।

ध्यान दें कि आमतौर पर, Charlie एक Relay Intro के लिए तुरंत Relay Response के साथ जवाब देगा, जिसमें एक ACK block शामिल होना चाहिए। उस स्थिति में, ACK block के साथ अलग संदेश की आवश्यकता नहीं है।

Hole punch को पुनः प्रसारित किया जा सकता है, जैसा कि SSU 1 में होता है।

I2NP संदेशों के विपरीत, Relay संदेशों में अद्वितीय पहचानकर्ता नहीं होते हैं, इसलिए डुप्लिकेट का पता nonce का उपयोग करके relay state machine द्वारा लगाया जाना चाहिए। implementations को हाल ही में उपयोग किए गए nonces का cache भी बनाए रखना पड़ सकता है, ताकि उस nonce के लिए state machine पूरी होने के बाद भी प्राप्त डुप्लिकेट का पता लगाया जा सके।

SSU 1 relay की सभी विशेषताएं समर्थित हैं, जिसमें [Prop158](/proposals/158-ipv6-transport-enhancements) में प्रलेखित और 0.9.50 से समर्थित विशेषताएं भी शामिल हैं। IPv4 और IPv6 introductions समर्थित हैं। एक Relay Request को IPv4 session के माध्यम से IPv6 introduction के लिए भेजा जा सकता है, और एक Relay Request को IPv6 session के माध्यम से IPv4 introduction के लिए भेजा जा सकता है।

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
### IPv4/v6

निम्नलिखित SSU 1 से अंतर और SSU 2 कार्यान्वयन के लिए सिफारिशें हैं।

SSU 1 में, introduction अपेक्षाकृत सस्ता है, और Alice आम तौर पर सभी introducers को Relay Requests भेजती है। SSU 2 में, introduction अधिक महंगा है, क्योंकि पहले एक introducer के साथ connection स्थापित करना होता है। Introduction latency और overhead को कम करने के लिए, अनुशंसित प्रसंस्करण चरण निम्नलिखित हैं:

SSU 1 और SSU 2 दोनों में, Relay Response और Hole Punch किसी भी क्रम में प्राप्त हो सकते हैं, या बिल्कुल भी प्राप्त नहीं हो सकते हैं।

SSU 1 में, Alice आमतौर पर Hole Punch (1 1/2 RTT) से पहले Relay Response (1 RTT) प्राप्त करती है। हो सकता है कि यह उन विनिर्देशों में अच्छी तरह से प्रलेखित न हो, लेकिन Alice को आगे बढ़ने से पहले Bob से Relay Response प्राप्त करना आवश्यक है, ताकि Charlie का IP प्राप्त हो सके। यदि Hole Punch पहले प्राप्त होता है, तो Alice इसे पहचान नहीं पाएगी, क्योंकि इसमें कोई डेटा नहीं होता और source IP पहचाना नहीं जाता। Relay Response प्राप्त करने के बाद, Alice को Charlie के साथ handshake शुरू करने से पहले या तो Charlie से Hole Punch प्राप्त होने का इंतज़ार करना चाहिए, या एक छोटी देरी (अनुशंसित 500 ms) का इंतज़ार करना चाहिए।

### Alice द्वारा प्रसंस्करण

SSU 2 में, Alice आमतौर पर Hole Punch (1 1/2 RTT) को Relay Response (2 RTT) से पहले प्राप्त करेगी। SSU 2 Hole Punch को SSU 1 की तुलना में प्रोसेस करना आसान है, क्योंकि यह परिभाषित connection IDs (relay nonce से व्युत्पन्न) और Charlie के IP सहित सामग्री के साथ एक पूर्ण संदेश है। Relay Response (Data message) और Hole Punch message में समान signed Relay Response block होता है। इसलिए, Alice या तो Charlie से Hole Punch प्राप्त करने के बाद, या Bob से Relay Response प्राप्त करने के बाद Charlie के साथ handshake शुरू कर सकती है।

### Bob द्वारा टैग अनुरोध

Hole Punch के signature verification में introducer के (Bob के) router hash शामिल होता है। यदि Relay Requests एक से अधिक introducer को भेजे गए हैं, तो signature को validate करने के लिए कई विकल्प हैं:

#### सारांश

यदि Charlie एक symmetric NAT के पीछे है, तो Relay Response और Hole Punch में उसका रिपोर्ट किया गया port सटीक नहीं हो सकता है। इसलिए, Alice को Hole Punch संदेश के UDP source port की जांच करनी चाहिए, और यदि यह रिपोर्ट किए गए port से अलग है तो उसका उपयोग करना चाहिए।

- पते में iexp मान के आधार पर expired किसी भी introducers को ignore करें
- यदि एक या अधिक introducers के साथ SSU2 connection पहले से established है, तो एक को चुनें और केवल उस introducer को Relay Request भेजें।
- अन्यथा, यदि एक या अधिक introducers के लिए Router Info स्थानीय रूप से ज्ञात है, तो एक को चुनें और केवल उस introducer से connect करें।
- अन्यथा, सभी introducers के लिए Router Infos lookup करें, उस introducer से connect करें जिसका Router Info पहले प्राप्त होता है।

#### विवरण

SSU 1 में, केवल Alice ही Session Request में एक tag का अनुरोध कर सकती थी। Bob कभी भी tag का अनुरोध नहीं कर सकता था, और Alice भी Bob के लिए relay नहीं कर सकती थी।

SSU2 में, Alice आम तौर पर Session Request में एक tag का अनुरोध करती है, लेकिन Alice या Bob दोनों में से कोई भी data phase में tag का अनुरोध कर सकता है। Bob आम तौर पर inbound request प्राप्त करने के बाद firewalled नहीं होता, लेकिन यह relay के बाद हो सकता है, या Bob की state बदल सकती है, या वह दूसरे address type (IPv4/v6) के लिए introducer का अनुरोध कर सकता है। इसलिए, SSU2 में, Alice और Bob दोनों के लिए एक साथ दूसरे पक्ष के लिए relay बनना संभव है।

निम्नलिखित पता गुण प्रकाशित किए जा सकते हैं, SSU 1 से अपरिवर्तित, जिसमें [Prop158](/proposals/158-ipv6-transport-enhancements) में परिवर्तन शामिल हैं जो API 0.9.50 से समर्थित हैं:

प्रकाशित RouterAddress (RouterInfo का हिस्सा) में "SSU" या "SSU2" में से कोई एक protocol identifier होगा।

- प्रत्येक hash को आज़माएं जिसके लिए request भेजी गई थी
- प्रत्येक introducer के लिए अलग nonces का उपयोग करें, और इसका उपयोग यह निर्धारित करने के लिए करें कि यह Hole Punch किस introducer के जवाब में था
- यदि contents Relay Response में समान हैं और पहले से प्राप्त हैं, तो signature को फिर से validate न करें
- Signature को बिल्कुल भी validate न करें

RouterAddress में SSU2 समर्थन को दर्शाने के लिए तीन विकल्प होने चाहिए:

### पता गुणधर्म

Alice को SSU2 प्रोटोकॉल का उपयोग करके कनेक्ट करने से पहले यह सत्यापित करना होगा कि तीनों विकल्प उपस्थित और वैध हैं।

जब "s", "i", और "v" विकल्पों के साथ "SSU" के रूप में प्रकाशित किया जाता है, और "host" और "port" विकल्पों के साथ, router को उस host और port पर SSU और SSU2 दोनों protocols के लिए आने वाले connections को स्वीकार करना चाहिए, और protocol version का स्वचालित रूप से पता लगाना चाहिए।

## प्रकाशित Router जानकारी

### प्रकाशित पते

जब "SSU2" के रूप में "s", "i", और "v" विकल्पों के साथ, और "host" तथा "port" विकल्पों के साथ प्रकाशित किया जाता है, तो router केवल SSU2 protocol के लिए उस host और port पर आने वाले कनेक्शन स्वीकार करता है।

- caps: [B,C,4,6] क्षमताएं
- host: IP (IPv4 या IPv6)। संक्षिप्त IPv6 पता ("::" के साथ) की अनुमति है। फायरवॉल्ड होने पर उपस्थित हो भी सकता है और नहीं भी। होस्ट नाम की अनुमति नहीं है।
- iexp[0-2]: इस introducer की समाप्ति। ASCII अंक, epoch के बाद से सेकंड में। केवल फायरवॉल्ड होने पर उपस्थित, और introducers आवश्यक हैं। वैकल्पिक (भले ही इस introducer के लिए अन्य गुण उपस्थित हों)।
- ihost[0-2]: Introducer का IP (IPv4 या IPv6)। संक्षिप्त IPv6 पता ("::" के साथ) की अनुमति है। केवल फायरवॉल्ड होने पर उपस्थित, और introducers आवश्यक हैं। होस्ट नाम की अनुमति नहीं है। केवल SSU पता।
- ikey[0-2]: Introducer की Base 64 introduction key। केवल फायरवॉल्ड होने पर उपस्थित, और introducers आवश्यक हैं। केवल SSU पता।
- iport[0-2]: Introducer का पोर्ट 1024 - 65535। केवल फायरवॉल्ड होने पर उपस्थित, और introducers आवश्यक हैं। केवल SSU पता।
- itag[0-2]: Introducer का tag 1 - (2**32 - 1) ASCII अंक। केवल फायरवॉल्ड होने पर उपस्थित, और introducers आवश्यक हैं।
- key: Base 64 introduction key।
- mtu: वैकल्पिक। ऊपर MTU अनुभाग देखें।
- port: 1024 - 65535 फायरवॉल्ड होने पर उपस्थित हो भी सकता है और नहीं भी।

### अप्रकाशित SSU2 पता

यदि कोई router SSU1 और SSU2 दोनों connections को support करता है लेकिन incoming connections के लिए automatic version detection implement नहीं करता है, तो उसे "SSU" और "SSU2" दोनों addresses को advertise करना चाहिए, और SSU2 options को केवल "SSU2" address में include करना चाहिए। router को "SSU2" address में "SSU" address की तुलना में कम cost value (उच्च priority) set करनी चाहिए, ताकि SSU2 को प्राथमिकता मिले।

यदि एक ही RouterInfo में कई SSU2 RouterAddresses (या तो "SSU" या "SSU2" के रूप में) प्रकाशित किए जाते हैं (अतिरिक्त IP addresses या ports के लिए), तो समान port को निर्दिष्ट करने वाले सभी addresses में समान SSU2 विकल्प और मान होने चाहिए। विशेष रूप से, सभी में समान static key "s" और introduction key "i" होनी चाहिए।

- s=(Base64 key) इस RouterAddress के लिए वर्तमान Noise static public key (s)। मानक I2P Base 64 alphabet का उपयोग करके Base 64 encoded। binary में 32 bytes, Base 64 encoded के रूप में 44 bytes, little-endian X25519 public key।
- i=(Base64 key) इस RouterAddress के लिए headers को encrypt करने के लिए वर्तमान introduction key। मानक I2P Base 64 alphabet का उपयोग करके Base 64 encoded। binary में 32 bytes, Base 64 encoded के रूप में 44 bytes, big-endian ChaCha20 key।
- v=2 वर्तमान version (2)। जब "SSU" के रूप में प्रकाशित किया जाता है, तो version 1 के लिए अतिरिक्त समर्थन निहित है। भविष्य के versions के लिए समर्थन comma-separated values के साथ होगा, जैसे v=2,3 Implementation को compatibility सत्यापित करनी चाहिए, यदि comma मौजूद है तो multiple versions सहित। Comma-separated versions numerical order में होने चाहिए।

जब introducers के साथ SSU या SSU2 के रूप में प्रकाशित किया जाता है, तो निम्नलिखित विकल्प उपस्थित होते हैं:

निम्नलिखित विकल्प केवल SSU के लिए हैं और SSU2 के लिए उपयोग नहीं किए जाते हैं। SSU2 में, Alice को यह जानकारी Charlie के RI से मिलती है।

एक router को introducers प्रकाशित करते समय address में host या port प्रकाशित नहीं करना चाहिए। एक router को introducers प्रकाशित करते समय address में 4 और/या 6 caps प्रकाशित करना चाहिए ताकि IPv4 और/या IPv6 के लिए समर्थन का संकेत दिया जा सके। यह हाल के SSU 1 addresses के लिए वर्तमान अभ्यास के समान है।

नोट: यदि SSU के रूप में प्रकाशित किया गया है, और SSU 1 और SSU2 introducers का मिश्रण है, तो पुराने routers के साथ संगतता के लिए SSU 1 introducers निचले indexes पर होने चाहिए और SSU2 introducers ऊंचे indexes पर होने चाहिए।

यदि Alice अपना SSU2 पता (जो "SSU" या "SSU2" के रूप में हो) incoming connections के लिए publish नहीं करती है, तो उसे एक "SSU2" router address publish करना चाहिए जिसमें केवल उसकी static key और SSU2 version हो, ताकि Bob Session Confirmed part 2 में Alice का RouterInfo प्राप्त करने के बाद key को validate कर सके।

#### त्रुटि प्रबंधन

इस router address में "host" या "port" विकल्प शामिल नहीं होंगे, क्योंकि ये outbound SSU2 कनेक्शन के लिए आवश्यक नहीं हैं। इस address के लिए प्रकाशित cost का कड़ाई से कोई महत्व नहीं है, क्योंकि यह केवल inbound है; हालांकि, यदि cost को अन्य addresses की तुलना में अधिक (कम प्राथमिकता) सेट किया जाए तो यह अन्य routers के लिए सहायक हो सकता है। सुझाया गया मान 14 है।

- ih[0-2]=(Base64 hash) एक introducer के लिए router hash। मानक I2P Base 64 alphabet का उपयोग करके Base 64 encoded। binary में 32 bytes, Base 64 encoded के रूप में 44 bytes
- iexp[0-2]: इस introducer की समाप्ति। SSU 1 से अपरिवर्तित।
- itag[0-2]: Introducer का tag 1 - (2**32 - 1) SSU 1 से अपरिवर्तित।

Alice बस एक मौजूदा प्रकाशित "SSU" address में "i" "s" और "v" विकल्प भी जोड़ सकती है।

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

NTCP2 और SSU2 के लिए समान static keys का उपयोग करना अनुमतित है, लेकिन अनुशंसित नहीं है।

RouterInfos के caching के कारण, router चालू होने के दौरान static public key या IV को rotate नहीं करना चाहिए, चाहे वह published address में हो या न हो। Router को इस key और IV को persistently store करना चाहिए ताकि तुरंत restart के बाद पुन: उपयोग किया जा सके, जिससे incoming connections काम करते रहें, और restart times expose न हों। Router को last-shutdown time को persistently store करना चाहिए, या अन्यथा निर्धारित करना चाहिए, ताकि startup पर पिछले downtime की गणना की जा सके।

### Public Key और IV रोटेशन

restart समय को उजागर करने की चिंताओं के अधीन, router इस key या IV को startup पर rotate कर सकते हैं यदि router पहले कुछ समय के लिए (कम से कम कई दिन) down था।

- s=(Base64 key) जैसा कि ऊपर प्रकाशित पतों के लिए परिभाषित किया गया है।
- i=(Base64 key) जैसा कि ऊपर प्रकाशित पतों के लिए परिभाषित किया गया है।
- v=2 जैसा कि ऊपर प्रकाशित पतों के लिए परिभाषित किया गया है।

यदि router के पास कोई प्रकाशित SSU2 RouterAddresses हैं (SSU या SSU2 के रूप में), तो rotation से पहले न्यूनतम downtime बहुत अधिक होना चाहिए, उदाहरण के लिए एक महीना, जब तक कि स्थानीय IP address नहीं बदला हो या router "rekeys" न करे।

यदि router के पास कोई प्रकाशित SSU RouterAddresses हैं, लेकिन SSU2 नहीं है (SSU या SSU2 के रूप में), तो rotation से पहले न्यूनतम downtime अधिक होना चाहिए, उदाहरण के लिए एक दिन, जब तक कि स्थानीय IP address नहीं बदला हो या router "rekeys" न हो। यह तब भी लागू होता है जब प्रकाशित SSU address में introducers हों।

### आउटबाउंड पैकेट निर्माण

यदि router के पास कोई प्रकाशित RouterAddresses (SSU, SSU2, या SSU) नहीं हैं, तो rotation से पहले न्यूनतम downtime दो घंटे जितना कम हो सकता है, भले ही IP address बदल जाए, जब तक कि router "rekeys" न करे।

यदि router एक अलग Router Hash के लिए "rekeys" करता है, तो उसे एक नई noise key और intro key भी generate करनी चाहिए।

इम्प्लीमेंटेशन को यह ध्यान रखना चाहिए कि static public key या IV को बदलने से उन router से आने वाले SSU2 कनेक्शन प्रतिबंधित हो जाएंगे जिन्होंने पुराना RouterInfo cache किया है। RouterInfo publishing, tunnel peer selection (OBGW और IB closest hop दोनों सहित), zero-hop tunnel selection, transport selection, और अन्य implementation रणनीतियों को इस बात का ध्यान रखना चाहिए।

Intro key rotation, key rotation के समान नियमों के अधीन है।

नोट: rekeying से पहले न्यूनतम डाउनटाइम को नेटवर्क स्वास्थ्य सुनिश्चित करने के लिए संशोधित किया जा सकता है, और मध्यम समय के लिए बंद रहे router द्वारा reseeding को रोकने के लिए।

इनकार करने की क्षमता एक लक्ष्य नहीं है। ऊपर दिया गया अवलोकन देखें।

प्रत्येक pattern को गुणों के साथ असाइन किया जाता है जो initiator की static public key को प्रदान की गई गोपनीयता का वर्णन करते हैं, और responder की static public key को प्रदान की गई गोपनीयता का वर्णन करते हैं। अंतर्निहित धारणाएं यह हैं कि ephemeral private keys सुरक्षित हैं, और यदि parties को दूसरे पक्ष से कोई static public key प्राप्त होती है जिस पर वे भरोसा नहीं करते तो वे handshake को रद्द कर देते हैं।

यह खंड केवल handshakes में स्थिर सार्वजनिक कुंजी फ़ील्ड के माध्यम से पहचान के रिसाव पर विचार करता है। बेशक, Noise प्रतिभागियों की पहचान अन्य साधनों के माध्यम से भी उजागर हो सकती है, जिसमें payload फ़ील्ड, ट्रैफिक विश्लेषण, या IP पते जैसे metadata शामिल हैं।

Alice: (8) एक प्रमाणित पार्टी के लिए forward secrecy के साथ एन्क्रिप्टेड।

Bob: (3) प्रसारित नहीं किया गया, लेकिन एक निष्क्रिय आक्रमणकारी responder की private key के उम्मीदवारों की जांच कर सकता है और यह निर्धारित कर सकता है कि उम्मीदवार सही है या नहीं।

#### पहचान छिपाना

Bob अपनी static public key को netDb में प्रकाशित करता है। Alice ऐसा नहीं कर सकती, लेकिन उसे इसे Bob को भेजे गए RI में शामिल करना होगा।

हैंडशेक संदेश (Session Request/Created/Confirmed, Retry) बुनियादी चरण, क्रम में:

डेटा चरण संदेशों के मूलभूत चरण, क्रम में:

सभी आने वाले संदेशों की प्रारंभिक प्रसंस्करण:

Handshake संदेश (Session Request/Created/Confirmed, Retry, Token Request) और अन्य out-of-session संदेश (Peer Test, Hole Punch) प्रसंस्करण:

डेटा चरण संदेशों की प्रसंस्करण:

## पैकेट दिशानिर्देश

### इनबाउंड पैकेट हैंडलिंग

SSU 1 में, inbound packet classification कठिन है, क्योंकि session number को indicate करने के लिए कोई header नहीं होता। Routers को पहले source IP और port को existing peer state से match करना होता है, और यदि नहीं मिलता, तो appropriate peer state खोजने या नया शुरू करने के लिए विभिन्न keys के साथ multiple decryptions का प्रयास करना पड़ता है। यदि existing session के लिए source IP या port बदल जाता है, संभवतः NAT behavior के कारण, तो router packet को existing session से match करने और contents को recover करने के लिए महंगे heuristics का उपयोग कर सकता है।

- 16 या 32 byte header बनाएं
- Payload बनाएं
- Header को mixHash() करें (Retry को छोड़कर)
- Noise का उपयोग करके payload को encrypt करें (Retry को छोड़कर, header को AD के रूप में उपयोग करके ChaChaPoly का उपयोग करें)
- Header को encrypt करें, और Session Request/Created के लिए, ephemeral key को भी

SSU 2 को inbound packet classification effort को कम करने के लिए डिज़ाइन किया गया है जबकि DPI प्रतिरोध और अन्य on-path threats को बनाए रखा गया है। Connection ID नंबर सभी message types के लिए header में शामिल किया गया है, और ज्ञात key और nonce के साथ ChaCha20 का उपयोग करके encrypted (obfuscated) किया गया है। इसके अतिरिक्त, message type भी header में शामिल किया गया है (header protection के साथ ज्ञात key में encrypted और फिर ChaCha20 के साथ obfuscated) और अतिरिक्त classification के लिए इसका उपयोग किया जा सकता है। किसी भी स्थिति में packet को classify करने के लिए trial DH या अन्य asymmetric crypto operation आवश्यक नहीं है।

- 16-byte header बनाएं
- Payload बनाएं
- Header को AD के रूप में उपयोग करके ChaChaPoly का उपयोग करके payload को encrypt करें
- Header को encrypt करें

### नोट्स

#### सारांश

लगभग सभी peers से आने वाले सभी संदेशों के लिए, Connection ID encryption के लिए ChaCha20 key गंतव्य router की introduction key होती है जो netdb में प्रकाशित की गई है।

- intro key के साथ header के पहले 8 bytes (Destination Connection ID) को decrypt करें
- Destination Connection ID द्वारा connection को lookup करें
- यदि connection मिल जाता है और data phase में है, तो data phase section पर जाएं
- यदि connection नहीं मिलता है, तो handshake section पर जाएं
- नोट: Peer Test और Hole Punch messages को भी test या relay nonce से बनाए गए Destination Connection ID द्वारा lookup किया जा सकता है।

केवल अपवाद वे पहले संदेश हैं जो Bob से Alice को भेजे जाते हैं (Session Created या Retry) जहाँ Alice की introduction key अभी तक Bob को पता नहीं है। इन मामलों में, Bob की introduction key को key के रूप में उपयोग किया जाता है।

- header के bytes 8-15 को (packet type, version, और net ID) intro key के साथ decrypt करें। यदि यह एक valid Session Request, Token Request, Peer Test, या Hole Punch है, तो आगे बढ़ें
- यदि valid message नहीं है, तो packet source IP/port द्वारा pending outbound connection को lookup करें, packet को Session Created या Retry के रूप में treat करें। header के पहले 8 bytes को correct key के साथ re-decrypt करें, और header के bytes 8-15 (packet type, version, और net ID) को। यदि यह एक valid Session Created या Retry है, तो आगे बढ़ें
- यदि valid message नहीं है, तो fail करें, या संभावित out-of-order data phase packet के रूप में queue करें
- Session Request/Created, Retry, Token Request, Peer Test, और Hole Punch के लिए, header के bytes 16-31 को decrypt करें
- Session Request/Created के लिए, ephemeral key को decrypt करें
- सभी header fields को validate करें, यदि valid नहीं है तो रोकें
- header को mixHash() करें
- Session Request/Created/Confirmed के लिए, Noise का उपयोग करके payload को decrypt करें
- Retry और data phase के लिए, ChaChaPoly का उपयोग करके payload को decrypt करें
- Header और payload को process करें

यह प्रोटोकॉल packet classification प्रसंस्करण को कम से कम करने के लिए डिज़ाइन किया गया है जिसमें कई fallback चरणों में अतिरिक्त crypto operations या जटिल heuristics की आवश्यकता हो सकती है। इसके अतिरिक्त, प्राप्त होने वाले अधिकांश packets को source IP/port द्वारा (संभावित रूप से महंगे) fallback lookup और दूसरे header decryption की आवश्यकता नहीं होगी। केवल Session Created और Retry (और संभवतः अन्य TBD) को fallback processing की आवश्यकता होगी। यदि session creation के बाद कोई endpoint अपना IP या port बदलता है, तो भी connection ID का उपयोग session को lookup करने के लिए किया जाता है। session खोजने के लिए heuristics का उपयोग करना कभी आवश्यक नहीं है, उदाहरण के लिए समान IP लेकिन अलग port वाले किसी अन्य session की खोज करना।

- सही key के साथ header के bytes 8-15 को decrypt करें (packet type, version, और net ID)
- Header को AD के रूप में उपयोग करके ChaChaPoly का उपयोग करके payload को decrypt करें
- Header और payload को process करें

#### विवरण

इसलिए, receiver loop logic में अनुशंसित प्रसंस्करण चरण हैं:

1) स्थानीय introduction key का उपयोग करके ChaCha20 के साथ पहले 8 bytes को decrypt करें, Destination Connection ID को recover करने के लिए। यदि Connection ID किसी वर्तमान या pending inbound session से मेल खाता है:

2) यदि connection ID वर्तमान session से मेल नहीं खाता: bytes 8-15 पर plaintext header की जांच करें कि वे वैध हैं (बिना कोई header protection operation किए)। Net ID और protocol version की पुष्टि करें कि वे वैध हैं, और message type Session Request है, या कोई अन्य message type जो out-of-session की अनुमति है (TBD)।

3) पैकेट के स्रोत IP/port द्वारा एक pending outbound session को खोजें।

4)  यदि समान पोर्ट पर SSU 1 चल रहा है, तो संदेश को SSU 1 पैकेट के रूप में प्रोसेस करने का प्रयास करें।

सामान्यतः, एक अप्रत्याशित message type वाला packet प्राप्त होने के बाद session (handshake या data phase में) को कभी भी नष्ट नहीं करना चाहिए। यह packet injection attacks को रोकता है। ये packets आमतौर पर handshake packet के retransmission के बाद भी प्राप्त होंगे, जब header decryption keys अब वैध नहीं रहीं।

अधिकतर मामलों में, बस packet को drop कर दें। एक implementation चाहे तो, लेकिन यह आवश्यक नहीं है, response में पहले से भेजे गए packet (handshake message या ACK 0) को retransmit कर सकती है।

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

Bob के रूप में Session Created भेजने के बाद, अप्रत्याशित packets आमतौर पर Data packets होते हैं जिन्हें decrypt नहीं किया जा सकता क्योंकि Session Confirmed packets खो गए या क्रम से बाहर हो गए। packets को queue करें और Session Confirmed packets प्राप्त करने के बाद उन्हें decrypt करने का प्रयास करें।

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

Bob के रूप में Session Confirmed प्राप्त करने के बाद, अप्रत्याशित packets आमतौर पर पुनः प्रेषित Session Confirmed packets होते हैं, क्योंकि Session Confirmed का ACK 0 खो गया था। अप्रत्याशित packets को drop किया जा सकता है। एक implementation प्रतिक्रिया में ACK block युक्त Data packet भेज सकता है, लेकिन यह आवश्यक नहीं है।

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

Session Created और Session Confirmed के लिए, implementations को सभी decrypted header fields (Connection IDs, packet number, packet type, version, id, frag, और flags) को सावधानीपूर्वक validate करना चाहिए header पर mixHash() को call करने और Noise AEAD के साथ payload को decrypt करने का प्रयास करने से पहले। यदि Noise AEAD decryption fail हो जाता है, तो कोई और processing नहीं की जा सकती, क्योंकि mixHash() handshake state को corrupt कर देगा, जब तक कि कोई implementation hash state को store नहीं करती और "back out" नहीं करती।

#### त्रुटि नियंत्रण

एक ही inbound port पर आने वाले packets का version 1 या 2 होना कुशलतापूर्वक detect करना संभव नहीं हो सकता है। ऊपर दिए गए steps को SSU 1 processing से पहले करना समझदारी हो सकती है, ताकि दोनों protocol versions का उपयोग करके trial DH operations का प्रयास करने से बचा जा सके।

यदि आवश्यक हो तो निर्धारित किया जाना है।

IPv4 मानता है, अतिरिक्त padding शामिल नहीं, IP और UDP header के आकार शामिल नहीं। Padding केवल SSU 1 के लिए mod-16 padding है।

**SSU 1**

### संस्करण का पता लगाना

**SSU 2**

### टोकन

हम ऊपर निर्दिष्ट करते हैं कि token एक यादृच्छिक रूप से उत्पन्न 8 byte value होना चाहिए, न कि कोई अपारदर्शी value जैसे कि server secret और IP, port का hash या HMAC उत्पन्न करना चाहिए, reuse attacks के कारण। हालांकि, इसके लिए delivered tokens के temporary और (वैकल्पिक रूप से) persistent storage की आवश्यकता होती है। [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) एक server secret और IP address के 16-byte HMAC का उपयोग करता है, और server secret हर दो मिनट में rotate होता है। हमें कुछ समान की जांच करनी चाहिए, एक लंबे server secret lifetime के साथ। यदि हम token में एक timestamp embed करते हैं, तो वह एक समाधान हो सकता है, लेकिन एक 8-byte token उसके लिए पर्याप्त बड़ा नहीं हो सकता।

यदि आवश्यकता हो तो बाद में निर्धारित किया जाएगा।

## अनुशंसित स्थिरांक

- Outbound handshake पुनः प्रेषण timeout: 1.25 सेकंड, exponential backoff के साथ (1.25, 3.75, और 8.75 सेकंड पर पुनः प्रेषण)
- कुल outbound handshake timeout: 15 सेकंड
- Inbound handshake पुनः प्रेषण timeout: 1 सेकंड, exponential backoff के साथ (1, 3, और 7 सेकंड पर पुनः प्रेषण)
- कुल inbound handshake timeout: 12 सेकंड
- retry भेजने के बाद timeout: 9 सेकंड
- ACK देरी: max(10, min(rtt/6, 150)) ms
- तत्काल ACK देरी: min(rtt/16, 5) ms
- अधिकतम ACK ranges: 256?
- अधिकतम ACK depth: 512?
- Padding वितरण: 0-15 bytes, या अधिक
- Data phase न्यूनतम पुनः प्रेषण timeout: 1 सेकंड, जैसा कि [RFC-6298](https://tools.ietf.org/html/rfc6298) में है
- Data phase के लिए पुनः प्रेषण timers पर अतिरिक्त मार्गदर्शन के लिए [RFC-6298](https://tools.ietf.org/html/rfc6298) भी देखें।

## पैकेट ओवरहेड विश्लेषण

IPv4 मानता है, अतिरिक्त पैडिंग सहित नहीं, IP और UDP हेडर आकार सहित नहीं। पैडिंग केवल SSU 1 के लिए mod-16 पैडिंग है।

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
## समस्याएं और भविष्य का कार्य

### टोकन

हम ऊपर निर्दिष्ट करते हैं कि टोकन एक यादृच्छिक रूप से उत्पन्न 8 बाइट मान होना चाहिए, और सर्वर सीक्रेट तथा IP, पोर्ट के हैश या HMAC जैसा कोई अपारदर्शी मान उत्पन्न नहीं करना चाहिए, क्योंकि पुनः उपयोग हमलों के कारण ऐसा करने से सुरक्षा जोखिम होता है। हालाँकि, इसके लिए वितरित टोकन के अस्थायी और (वैकल्पिक रूप से) स्थायी भंडारण की आवश्यकता होती है। [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) सर्वर सीक्रेट और IP पते के 16-बाइट HMAC का उपयोग करता है, और सर्वर सीक्रेट हर दो मिनट में बदल जाता है। हमें इसी तरह कुछ जांच करना चाहिए, लेकिन लंबे समय तक चलने वाले सर्वर सीक्रेट के साथ। यदि हम टोकन में टाइमस्टैम्प सम्मिलित करें, तो यह एक समाधान हो सकता है, लेकिन 8-बाइट टोकन इसके लिए पर्याप्त बड़ा नहीं हो सकता।

## संदर्भ

- **[Common]** [Common Structures Specification](/docs/specs/common-structures)
- **[ECIES]** [ECIES-X25519-AEAD-Ratchet Specification](/docs/specs/ecies)
- **[NetDB]** [Network Database](/docs/overview/network-database)
- **[NOISE]** [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Nonce-Disrespecting Adversaries](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [NTCP Transport](/docs/transport/ntcp)
- **[NTCP2]** [NTCP2 Specification](/docs/specs/ntcp2)
- **[PMTU]** [Path MTU Discovery](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Proposal 104: TLS Transport](/proposals/104-tls-transport)
- **[Prop109]** [Proposal 109: Pluggable Transport](/proposals/109-pt-transport)
- **[Prop158]** [Proposal 158: IPv6 Transport Enhancements](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Proposal 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: TCP Performance Implications](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: MODP Groups](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: TCP Congestion Control](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: MD5 Security Considerations](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: TCP Retransmission Timer](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: IPv6 Flow Label](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Elliptic Curves for Security](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: ChaCha20-Poly1305 Cipher Suites for TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: QUIC Transport Protocol](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: Using TLS to Secure QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: QUIC Loss Detection and Congestion Control](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [RouterAddress Structure](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [RouterIdentity Structure](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [SigningPublicKey Type](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [SSU Transport](/docs/transport/ssu)
- **[STS]** [Station-to-Station Protocol](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [I2P Ticket 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [I2P Ticket 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [WireGuard Protocol](https://www.wireguard.com/papers/wireguard.pdf)

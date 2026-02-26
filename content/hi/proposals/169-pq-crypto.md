---
title: "पोस्ट-क्वांटम क्रिप्टो प्रोटोकॉल"
aliases: 
number: "169"
author: "zzz, orignal, drzed, eyedeekay"
created: "2025-01-21"
lastupdated: "2026-02-26"
status: "खोलें"
thread: "http://zzz.i2p/topics/3294"
target: "0.9.80"
toc: true
---

### स्थिति

| प्रोटोकॉल / फीचर | स्थिति |
|--------------------|--------|
| Ratchet | Java I2P और i2pd में पूर्ण |
| NTCP2 | बीटा Q1 2026 |
| SSU2 | कार्यान्वयन जल्द शुरू हो रहा है, बीटा Q23 2026 |
| MLDSA SigTypes | कम प्राथमिकता, शायद 2027+ |
## अवलोकन

जबकि उपयुक्त पोस्ट-क्वांटम (PQ) क्रिप्टोग्राफी के लिए अनुसंधान और प्रतिस्पर्धा एक दशक से जारी है, विकल्प हाल तक स्पष्ट नहीं हुए थे।

हमने 2022 में PQ crypto के प्रभावों को देखना शुरू किया [zzz.i2p](http://zzz.i2p/topics/3294)।

TLS मानकों ने पिछले दो वर्षों में हाइब्रिड एन्क्रिप्शन समर्थन जोड़ा है और अब Chrome और Firefox में समर्थन के कारण यह इंटरनेट पर एन्क्रिप्टेड ट्रैफिक के एक महत्वपूर्ण हिस्से के लिए उपयोग किया जाता है [Cloudflare](https://blog.cloudflare.com/pq-2024/)।

NIST ने हाल ही में post-quantum cryptography के लिए अनुशंसित एल्गोरिदम को अंतिम रूप दिया और प्रकाशित किया है [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)। कई सामान्य cryptography libraries अब NIST मानकों का समर्थन करती हैं या निकट भविष्य में समर्थन जारी करेंगी।

[Cloudflare](https://blog.cloudflare.com/pq-2024/) और [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) दोनों की सिफारिश है कि माइग्रेशन तुरंत शुरू होना चाहिए। 2022 NSA PQ FAQ [NSA](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF) भी देखें। I2P को सुरक्षा और क्रिप्टोग्राफी में अग्रणी होना चाहिए। अब अनुशंसित एल्गोरिदम को लागू करने का समय है। अपने लचीले crypto type और signature type सिस्टम का उपयोग करके, हम hybrid crypto के लिए, और PQ तथा hybrid signatures के लिए types जोड़ेंगे।

## लक्ष्य

- PQ-प्रतिरोधी एल्गोरिदम का चयन करें
- उपयुक्त स्थानों पर I2P प्रोटोकॉल में PQ-केवल और हाइब्रिड एल्गोरिदम जोड़ें
- कई वेरिएंट परिभाषित करें
- कार्यान्वयन, परीक्षण, विश्लेषण और अनुसंधान के बाद सर्वोत्तम वेरिएंट का चयन करें
- वृद्धिशील रूप से और पिछड़ी संगतता के साथ समर्थन जोड़ें

## गैर-लक्ष्य

- एक-तरफा (Noise N) एन्क्रिप्शन प्रोटोकॉल को न बदलें
- SHA256 से दूर न जाएं, PQ द्वारा निकट-अवधि में खतरा नहीं
- इस समय अंतिम पसंदीदा वेरिएंट का चयन न करें

## खतरा मॉडल

- OBEP या IBGW पर routers, संभावित रूप से मिलकर काम करते हुए,
  बाद में डिक्रिप्शन के लिए garlic messages को स्टोर करना (forward secrecy)
- नेटवर्क observers
  बाद में डिक्रिप्शन के लिए transport messages को स्टोर करना (forward secrecy)
- नेटवर्क प्रतिभागी RI, LS, streaming, datagrams,
  या अन्य संरचनाओं के लिए signatures को जाली बनाना

## प्रभावित प्रोटोकॉल

हम निम्नलिखित protocols को modify करेंगे, मोटे तौर पर development के क्रम में। समग्र rollout संभवतः 2025 के अंत से 2027 के मध्य तक होगा। विवरण के लिए नीचे Priorities और Rollout section देखें।

| प्रोटोकॉल / सुविधा | स्थिति |
|--------------------|--------|
| Hybrid MLKEM Ratchet और LS | अनुमोदित 2025-06; बीटा 2025-08; रिलीज़ 2025-11 |
| Hybrid MLKEM NTCP2 | लाइव नेट पर परीक्षित, अनुमोदित 2026-02; बीटा लक्ष्य 2026-05; रिलीज़ लक्ष्य 2026-08 |
| Hybrid MLKEM SSU2 | अनुमोदित 2026-02; बीटा लक्ष्य 2026-08; रिलीज़ लक्ष्य 2026-11 |
| MLDSA SigTypes 12-14 | प्रस्ताव स्थिर है लेकिन 2027 तक अंतिम रूप नहीं दिया जा सकता |
| MLDSA Dests | लाइव नेट पर परीक्षित, floodfill समर्थन के लिए नेट अपग्रेड की आवश्यकता |
| Hybrid SigTypes 15-17 | प्रारंभिक |
| Hybrid Dests | |
## डिज़ाइन

हम NIST FIPS 203 और 204 मानकों [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) का समर्थन करेंगे जो CRYSTALS-Kyber और CRYSTALS-Dilithium (संस्करण 3.1, 3, और पुराने) पर आधारित हैं, लेकिन उनके साथ संगत नहीं हैं।

### कुंजी विनिमय

हम निम्नलिखित प्रोटोकॉल में hybrid key exchange का समर्थन करेंगे:

| Proto   | Noise Type | Support PQ only? | Support Hybrid? |
|---------|------------|------------------|-----------------|
| NTCP2   | XK         | नहीं               | हाँ             |
| SSU2    | XK         | नहीं               | हाँ             |
| Ratchet | IK         | नहीं               | हाँ             |
| TBM     | N          | नहीं               | नहीं              |
| NetDB   | N          | नहीं               | नहीं              |
PQ KEM केवल ephemeral keys प्रदान करता है, और static-key handshakes जैसे कि Noise XK और IK का प्रत्यक्ष समर्थन नहीं करता है।

Noise N दो-तरफा key exchange का उपयोग नहीं करता है और इसलिए यह hybrid encryption के लिए उपयुक्त नहीं है।

इसलिए हम केवल hybrid encryption का समर्थन करेंगे, NTCP2, SSU2, और Ratchet के लिए। हम तीन ML-KEM variants को [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) के अनुसार परिभाषित करेंगे, कुल 3 नए encryption types के लिए। Hybrid types केवल X25519 के संयोजन में ही परिभाषित किए जाएंगे।

नए encryption प्रकार हैं:

| Type | Code |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
ओवरहेड काफी अधिक होगा। वर्तमान में विशिष्ट संदेश 1 और 2 के आकार (XK और IK के लिए) लगभग 100 बाइट्स हैं (किसी भी अतिरिक्त पेलोड से पहले)। यह एल्गोरिदम के आधार पर 8x से 15x तक बढ़ेगा।

### हस्ताक्षर

हम निम्नलिखित संरचनाओं में PQ और hybrid signatures का समर्थन करेंगे:

| प्रकार | केवल PQ समर्थन? | Hybrid समर्थन? |
|------|------------------|-----------------|
| RouterInfo | हाँ | हाँ |
| LeaseSet | हाँ | हाँ |
| Streaming SYN/SYNACK/Close | हाँ | हाँ |
| Repliable Datagrams | हाँ | हाँ |
| Datagram2 (prop. 163) | हाँ | हाँ |
| I2CP create session msg | हाँ | हाँ |
| SU3 files | हाँ | हाँ |
| X.509 certificates | हाँ | हाँ |
| Java keystores | हाँ | हाँ |
इसलिए हम PQ-only और hybrid दोनों signatures का समर्थन करेंगे। हम तीन ML-DSA variants को [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) के अनुसार परिभाषित करेंगे, Ed25519 के साथ तीन hybrid variants, और केवल SU3 files के लिए prehash के साथ तीन PQ-only variants, कुल मिलाकर 9 नए signature types। Hybrid types केवल Ed25519 के संयोजन में परिभाषित किए जाएंगे। हम मानक ML-DSA का उपयोग करेंगे, pre-hash variants (HashML-DSA) का नहीं, SU3 files को छोड़कर।

हम [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) सेक्शन 3.4 में परिभाषित "hedged" या randomized signing variant का उपयोग करेंगे, "determinstic" variant का नहीं। यह सुनिश्चित करता है कि प्रत्येक signature अलग हो, यहां तक कि समान data पर भी, और side-channel attacks के खिलाफ अतिरिक्त सुरक्षा प्रदान करता है। encoding और context सहित algorithm choices के बारे में अतिरिक्त विवरण के लिए नीचे implementation notes सेक्शन देखें।

नए signature प्रकार हैं:

| प्रकार | कोड |
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
X.509 प्रमाणपत्र और अन्य DER encodings [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/) में परिभाषित composite structures और OIDs का उपयोग करेंगे।

ओवरहेड काफी अधिक होगा। सामान्य Ed25519 destination और router identity का आकार 391 बाइट्स है। एल्गोरिदम के आधार पर ये 3.5x से 6.8x तक बढ़ेगा। Ed25519 signatures 64 बाइट्स के हैं। एल्गोरिदम के आधार पर ये 38x से 76x तक बढ़ेंगे। सामान्य signed RouterInfo, LeaseSet, repliable datagrams, और signed streaming messages लगभग 1KB के होते हैं। एल्गोरिदम के आधार पर ये 3x से 8x तक बढ़ेंगे।

चूंकि नए destination और router identity प्रकारों में padding नहीं होगी, वे compressible नहीं होंगे। Destinations और router identities के आकार जो in-transit में gzipped हैं, algorithm के आधार पर 12x - 38x तक बढ़ जाएंगे।

### कानूनी संयोजन

Destinations के लिए, नए signature types को leaseset में सभी encryption types के साथ समर्थन प्राप्त है। key certificate में encryption type को NONE (255) पर सेट करें।

RouterIdentities के लिए, ElGamal encryption type deprecated है। नए signature types केवल X25519 (type 4) encryption के साथ supported हैं। नए encryption types RouterAddresses में indicate किए जाएंगे। key certificate में encryption type type 4 ही रहेगा।

### नई क्रिप्टो आवश्यक

- ML-KEM (पूर्व में CRYSTALS-Kyber) [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
- ML-DSA (पूर्व में CRYSTALS-Dilithium) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
- SHA3-128 (पूर्व में Keccak-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf) केवल SHAKE128 के लिए उपयोग किया जाता है
- SHA3-256 (पूर्व में Keccak-512) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- SHAKE128 और SHAKE256 (SHA3-128 और SHA3-256 के XOF एक्सटेंशन) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)

SHA3-256, SHAKE128, और SHAKE256 के लिए टेस्ट वेक्टर [NIST](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values) पर उपलब्ध हैं।

ध्यान दें कि Java bouncycastle library उपरोक्त सभी का समर्थन करती है। C++ library समर्थन OpenSSL 3.5 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/) में उपलब्ध है।

### विकल्प

हम [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) (Sphincs+) का समर्थन नहीं करेंगे, यह ML-DSA से बहुत अधिक धीमा और बड़ा है। हम आगामी FIPS206 (Falcon) का समर्थन नहीं करेंगे, यह अभी भी मानकीकृत नहीं है। हम NTRU या अन्य PQ उम्मीदवारों का समर्थन नहीं करेंगे जो NIST द्वारा मानकीकृत नहीं किए गए हैं।

### Rosenpass

Wireguard (IK) को शुद्ध PQ crypto के लिए अनुकूलित करने पर कुछ अनुसंधान [paper](https://eprint.iacr.org/2020/379.pdf) उपलब्ध है, लेकिन उस paper में कई खुले प्रश्न हैं। बाद में, इस दृष्टिकोण को PQ Wireguard के लिए Rosenpass [Rosenpass](https://rosenpass.eu/) [whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf) के रूप में लागू किया गया।

Rosenpass एक Noise KK-जैसे handshake का उपयोग करता है जिसमें preshared Classic McEliece 460896 static keys (प्रत्येक 500 KB) और Kyber-512 (मूल रूप से MLKEM-512) ephemeral keys होती हैं। चूंकि Classic McEliece ciphertexts केवल 188 bytes के होते हैं, और Kyber-512 public keys और ciphertexts उचित आकार के होते हैं, दोनों handshake messages एक मानक UDP MTU में फिट हो जाते हैं। PQ KK handshake से प्राप्त output shared key (osk) का उपयोग मानक Wireguard IK handshake के लिए input preshared key (psk) के रूप में किया जाता है। इसलिए कुल मिलाकर दो पूर्ण handshakes होते हैं, एक शुद्ध PQ और एक शुद्ध X25519।

हम अपने XK और IK handshakes को बदलने के लिए इनमें से कुछ भी नहीं कर सकते क्योंकि:

- हम KK नहीं कर सकते, Bob के पास Alice की static key नहीं है
- 500KB static keys बहुत ज्यादा बड़ी हैं
- हमें अतिरिक्त round-trip नहीं चाहिए

whitepaper में बहुत सारी अच्छी जानकारी है, और हम इसे विचारों और प्रेरणा के लिए समीक्षा करेंगे। TODO।

## विशिष्टता

### सामान्य संरचनाएं

सामान्य संरचना दस्तावेज़ [/docs/specs/common-structures/](/docs/specs/common-structures/) में निम्नलिखित अनुसार अनुभागों और तालिकाओं को अपडेट करें:

### PublicKey

नए Public Key प्रकार हैं:

| प्रकार | Public Key लंबाई | से | उपयोग |
|------|-------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | प्रस्ताव 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM768_X25519 | 32 | 0.9.xx | प्रस्ताव 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM1024_X25519 | 32 | 0.9.xx | प्रस्ताव 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM512 | 800 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| MLKEM768 | 1184 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| MLKEM1024 | 1568 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| MLKEM512_CT | 768 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| MLKEM768_CT | 1088 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| MLKEM1024_CT | 1568 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| NONE | 0 | 0.9.xx | प्रस्ताव 169 देखें, केवल PQ sig types वाले destinations के लिए, RIs या Leasesets के लिए नहीं |
हाइब्रिड पब्लिक keys X25519 key हैं। KEM पब्लिक keys वे ephemeral PQ key हैं जो Alice से Bob को भेजी जाती हैं। Encoding और byte order [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) में परिभाषित हैं।

MLKEM*_CT keys वास्तव में public keys नहीं हैं, ये "ciphertext" हैं जो Noise handshake में Bob से Alice को भेजे जाते हैं। इन्हें यहाँ पूर्णता के लिए सूचीबद्ध किया गया है।

### PrivateKey

नए Private Key प्रकार हैं:

| प्रकार | निजी कुंजी लंबाई | बाद से | उपयोग |
|------|---------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | प्रस्ताव 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM768_X25519 | 32 | 0.9.xx | प्रस्ताव 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM1024_X25519 | 32 | 0.9.xx | प्रस्ताव 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM512 | 1632 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| MLKEM768 | 2400 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
| MLKEM1024 | 3168 | 0.9.xx | प्रस्ताव 169 देखें, केवल handshakes के लिए, Leasesets, RIs या Destinations के लिए नहीं |
Hybrid private keys X25519 keys हैं। KEM private keys केवल Alice के लिए हैं। KEM encoding और byte order [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) में परिभाषित हैं।

### SigningPublicKey

नए Signing Public Key प्रकार हैं:

| प्रकार | लंबाई (बाइट्स) | से | उपयोग |
|------|----------------|-------|-------|
| MLDSA44 | 1312 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA65 | 1952 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA87 | 2592 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA44ph | 1344 | 0.9.xx | केवल SU3 फाइलों के लिए, netDb संरचनाओं के लिए नहीं |
| MLDSA65ph | 1984 | 0.9.xx | केवल SU3 फाइलों के लिए, netDb संरचनाओं के लिए नहीं |
| MLDSA87ph | 2624 | 0.9.xx | केवल SU3 फाइलों के लिए, netDb संरचनाओं के लिए नहीं |
Hybrid signing public keys Ed25519 key के बाद PQ key होती हैं, जैसा कि [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/) में है। Encoding और byte order [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) में परिभाषित हैं।

### SigningPrivateKey

नए Signing Private Key प्रकार हैं:

| Type | Length (bytes) | Since | Usage |
|------|----------------|-------|-------|
| MLDSA44 | 2560 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA65 | 4032 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA87 | 4896 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2592 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA65_EdDSA_SHA512_Ed25519 | 4064 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4928 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA44ph | 2592 | 0.9.xx | केवल SU3 फाइलों के लिए, netDb संरचनाओं के लिए नहीं। प्रस्ताव 169 देखें |
| MLDSA65ph | 4064 | 0.9.xx | केवल SU3 फाइलों के लिए, netDb संरचनाओं के लिए नहीं। प्रस्ताव 169 देखें |
| MLDSA87ph | 4928 | 0.9.xx | केवल SU3 फाइलों के लिए, netDb संरचनाओं के लिए नहीं। प्रस्ताव 169 देखें |
Hybrid signing private keys Ed25519 key के बाद PQ key होती हैं, जैसा कि [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/) में है। Encoding और byte order [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) में परिभाषित हैं।

### हस्ताक्षर

नए Signature प्रकार हैं:

| Type | Length (bytes) | Since | Usage |
|------|----------------|-------|-------|
| MLDSA44 | 2420 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA65 | 3309 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA87 | 4627 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2484 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA65_EdDSA_SHA512_Ed25519 | 3373 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4691 | 0.9.xx | प्रस्ताव 169 देखें |
| MLDSA44ph | 2484 | 0.9.xx | केवल SU3 फ़ाइलों के लिए, netDb संरचनाओं के लिए नहीं। प्रस्ताव 169 देखें |
| MLDSA65ph | 3373 | 0.9.xx | केवल SU3 फ़ाइलों के लिए, netDb संरचनाओं के लिए नहीं। प्रस्ताव 169 देखें |
| MLDSA87ph | 4691 | 0.9.xx | केवल SU3 फ़ाइलों के लिए, netDb संरचनाओं के लिए नहीं। प्रस्ताव 169 देखें |
हाइब्रिड signatures Ed25519 signature के बाद PQ signature होते हैं, जैसा कि [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/) में है। हाइब्रिड signatures को दोनों signatures को verify करके सत्यापित किया जाता है, और यदि दोनों में से कोई भी fail हो जाए तो यह fail हो जाता है। Encoding और byte order [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) में परिभाषित हैं।

### मुख्य प्रमाणपत्र

नई Signing Public Key प्रकार हैं:

| प्रकार | प्रकार कोड | कुल Public Key लंबाई | के बाद से | उपयोग |
|------|-----------|-------------------------|-------|-------|
| MLDSA44 | 12 | 1312 | 0.9.xx | See proposal 169 |
| MLDSA65 | 13 | 1952 | 0.9.xx | See proposal 169 |
| MLDSA87 | 14 | 2592 | 0.9.xx | See proposal 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 0.9.xx | See proposal 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 0.9.xx | See proposal 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 0.9.xx | See proposal 169 |
| MLDSA44ph | 18 | n/a | 0.9.xx | केवल SU3 फाइलों के लिए |
| MLDSA65ph | 19 | n/a | 0.9.xx | केवल SU3 फाइलों के लिए |
| MLDSA87ph | 20 | n/a | 0.9.xx | केवल SU3 फाइलों के लिए |
नए Crypto Public Key प्रकार हैं:

| प्रकार | प्रकार कोड | कुल Public Key Length | के बाद से | उपयोग |
|------|-----------|-------------------------|-------|-------|
| MLKEM512_X25519 | 5 | 32 | 0.9.xx | proposal 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM768_X25519 | 6 | 32 | 0.9.xx | proposal 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| MLKEM1024_X25519 | 7 | 32 | 0.9.xx | proposal 169 देखें, केवल Leasesets के लिए, RIs या Destinations के लिए नहीं |
| NONE | 255 | 0 | 0.9.xx | proposal 169 देखें |
हाइब्रिड key types को key certificates में कभी भी शामिल नहीं किया जाता है; केवल leasesets में शामिल किया जाता है।

Hybrid या PQ signature types वाले destinations के लिए, encryption type के लिए NONE (type 255) का उपयोग करें, लेकिन कोई crypto key नहीं होती है, और पूरा 384-byte main section signing key के लिए होता है।

### गंतव्य आकार

यहाँ नए Destination प्रकारों के लिए लंबाइयाँ हैं। सभी के लिए Enc type NONE (प्रकार 255) है और encryption key length को 0 माना जाता है। पूरा 384-byte सेक्शन signing public key के पहले भाग के लिए उपयोग किया जाता है। नोट: यह ECDSA_SHA512_P521 और RSA signature प्रकारों के स्पेसिफिकेशन से अलग है, जहाँ हमने destination में 256-byte ElGamal key को बनाए रखा था भले ही वह अप्रयुक्त था।

कोई पैडिंग नहीं। कुल लंबाई 7 + कुल की लंबाई है। की सर्टिफिकेट लंबाई 4 + अतिरिक्त की लंबाई है।

MLDSA44 के लिए उदाहरण 1319-बाइट destination बाइट स्ट्रीम:

skey[0:383] 5 (932 >> 8) (932 & 0xff) 00 12 00 255 skey[384:1311]

| Type | Type Code | Total Public Key Length | Main | Excess | Total Dest Length |
|------|-----------|-------------------------|------|--------|-------------------|
| MLDSA44 | 12 | 1312 | 384 | 928 | 1319 |
| MLDSA65 | 13 | 1952 | 384 | 1568 | 1959 |
| MLDSA87 | 14 | 2592 | 384 | 2208 | 2599 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 384 | 960 | 1351 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 384 | 1600 | 1991 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 384 | 2240 | 2631 |
### RouterIdent आकार

यहाँ नए Destination प्रकारों के लिए लंबाई दी गई है। सभी के लिए Enc प्रकार X25519 (प्रकार 4) है। X28819 public key के बाद का पूरा 352-byte सेक्शन signing public key के पहले भाग के लिए उपयोग किया जाता है। कोई padding नहीं। कुल लंबाई 39 + कुल key लंबाई है। Key certificate की लंबाई 4 + अतिरिक्त key लंबाई है।

MLDSA44 के लिए उदाहरण 1351-बाइट router identity बाइट स्ट्रीम:

enckey[0:31] skey[0:351] 5 (960 >> 8) (960 & 0xff) 00 12 00 4 skey[352:1311]

| Type | Type Code | Total Public Key Length | Main | Excess | Total RouterIdent Length |
|------|-----------|-------------------------|------|--------|--------------------------|
| MLDSA44 | 12 | 1312 | 352 | 960 | 1351 |
| MLDSA65 | 13 | 1952 | 352 | 1600 | 1991 |
| MLDSA87 | 14 | 2592 | 352 | 2240 | 2631 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 352 | 992 | 1383 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 352 | 1632 | 2023 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 352 | 2272 | 2663 |
### हैंडशेक पैटर्न

Handshake [Noise Protocol](https://noiseprotocol.org/noise.html) handshake patterns का उपयोग करते हैं।

निम्नलिखित अक्षर मैपिंग का उपयोग किया जाता है:

- e = एक-बार का ephemeral key
- s = static key
- p = message payload
- e1 = एक-बार का ephemeral PQ key, Alice से Bob को भेजी गई
- ekem1 = KEM ciphertext, Bob से Alice को भेजा गया

हाइब्रिड फॉरवर्ड सिक्योरिटी (hfs) के लिए XK और IK में निम्नलिखित संशोधन [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) सेक्शन 5 में निर्दिष्ट हैं:

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
e1 pattern इस प्रकार परिभाषित है, जैसा कि [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) अनुभाग 4 में निर्दिष्ट है:

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
ekem1 पैटर्न निम्नलिखित रूप में परिभाषित है, जैसा कि [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) सेक्शन 4 में निर्दिष्ट है:

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
### Noise Handshake KDF

#### समस्याएं

- क्या हमें handshake hash function बदलना चाहिए? [तुलना](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3) देखें।
  SHA256 PQ के लिए संवेदनशील नहीं है, लेकिन यदि हम
  अपने hash function को अपग्रेड करना चाहते हैं, तो अभी समय है, जबकि हम अन्य चीजें बदल रहे हैं।
  वर्तमान IETF SSH प्रस्ताव [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/) MLKEM768
  को SHA256 के साथ, और MLKEM1024 को SHA384 के साथ उपयोग करने का है। उस प्रस्ताव में
  सुरक्षा विचारों की चर्चा शामिल है।
- क्या हमें 0-RTT ratchet data (LS के अलावा) भेजना बंद करना चाहिए?
- यदि हम 0-RTT data नहीं भेजते हैं तो क्या हमें ratchet को IK से XK में बदलना चाहिए?

#### अवलोकन

यह खंड IK और XK दोनों protocols पर लागू होता है।

हाइब्रिड handshake को [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) में परिभाषित किया गया है। पहला संदेश, Alice से Bob तक, message payload से पहले e1, encapsulation key, को शामिल करता है। इसे एक अतिरिक्त static key के रूप में माना जाता है; इस पर EncryptAndHash() को कॉल करें (Alice के रूप में) या DecryptAndHash() (Bob के रूप में)। फिर message payload को सामान्य तरीके से प्रोसेस करें।

दूसरा संदेश, Bob से Alice तक, में ekem1, ciphertext शामिल है, जो message payload से पहले आता है। इसे एक अतिरिक्त static key के रूप में माना जाता है; इस पर EncryptAndHash() कॉल करें (Bob के रूप में) या DecryptAndHash() (Alice के रूप में)। फिर, kem_shared_key की गणना करें और MixKey(kem_shared_key) कॉल करें। उसके बाद message payload को सामान्य तरीके से प्रोसेस करें।

#### परिभाषित ML-KEM ऑपरेशन्स

हम निम्नलिखित functions को परिभाषित करते हैं जो cryptographic building blocks के अनुरूप हैं जैसा कि [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) में परिभाषित किया गया है।

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

ध्यान दें कि encap_key और ciphertext दोनों Noise handshake messages 1 और 2 में ChaCha/Poly blocks के अंदर encrypted हैं। वे handshake प्रक्रिया के हिस्से के रूप में decrypt हो जाएंगे।

kem_shared_key को MixHash() के साथ chaining key में मिलाया जाता है। विवरण के लिए नीचे देखें।

#### संदेश 1 के लिए Alice KDF

XK के लिए: 'es' message pattern के बाद और payload से पहले, जोड़ें:

या

IK के लिए: 'es' message pattern के बाद और 's' message pattern से पहले, जोड़ें:

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
#### संदेश 1 के लिए Bob KDF

XK के लिए: 'es' संदेश पैटर्न के बाद और payload से पहले, जोड़ें:

या

IK के लिए: 'es' message pattern के बाद और 's' message pattern से पहले, जोड़ें:

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
#### Message 2 के लिए Bob KDF

XK के लिए: 'ee' संदेश पैटर्न के बाद और payload से पहले, जोड़ें:

या

IK के लिए: 'ee' संदेश पैटर्न के बाद और 'se' संदेश पैटर्न से पहले, जोड़ें:

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
#### संदेश 2 के लिए Alice KDF

'ee' संदेश पैटर्न के बाद (और IK के लिए 'ss' संदेश पैटर्न से पहले), जोड़ें:

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
#### संदेश 3 के लिए KDF (केवल XK)

अपरिवर्तित

#### split() के लिए KDF

अपरिवर्तित

### Ratchet

ECIES-Ratchet विनिर्देश [/docs/specs/ecies/](/docs/specs/ecies/) को निम्नलिखित के अनुसार अपडेट करें:

#### Noise पहचानकर्ता

- "Noise_IKhfselg2_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1b) नया session format (binding के साथ)

परिवर्तन: वर्तमान ratchet में पहले ChaCha सेक्शन में static key और दूसरे सेक्शन में payload शामिल था। ML-KEM के साथ, अब तीन सेक्शन हैं। पहले सेक्शन में encrypted PQ public key है। दूसरे सेक्शन में static key है। तीसरे सेक्शन में payload है।

एन्क्रिप्टेड प्रारूप:

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
डिक्रिप्टेड फॉर्मेट:

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
आकार:

| Type | Type Code | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | pl len |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 96+pl | 64+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 912+pl | 880+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1296+pl | 1360+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1680+pl | 1648+pl | 1568+pl | 1568 | pl |
ध्यान दें कि payload में एक DateTime block होना चाहिए, इसलिए न्यूनतम payload size 7 है। न्यूनतम message 1 sizes की गणना तदनुसार की जा सकती है।

#### 1g) नया सेशन उत्तर प्रारूप

परिवर्तन: वर्तमान ratchet में पहले ChaCha section के लिए एक खाली payload है, और दूसरे section में payload है। ML-KEM के साथ, अब तीन sections हैं। पहले section में encrypted PQ ciphertext है। दूसरे section में एक खाली payload है। तीसरे section में payload है।

एन्क्रिप्टेड प्रारूप:

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
डिक्रिप्टेड प्रारूप:

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
आकार:

| प्रकार | प्रकार कोड | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 72+pl | 32+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 856+pl | 816+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1176+pl | 1136+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1656+pl | 1616+pl | 1568+pl | 1568 | pl |
ध्यान दें कि जबकि संदेश 2 में सामान्यतः एक गैर-शून्य payload होगा, ratchet specification [/docs/specs/ecies/](/docs/specs/ecies/) इसकी आवश्यकता नहीं करता, इसलिए न्यूनतम payload आकार 0 है। न्यूनतम संदेश 2 आकार की गणना तदनुसार की जा सकती है।

### NTCP2

NTCP2 विनिर्देश [/docs/specs/ntcp2/](/docs/specs/ntcp2/) को निम्नलिखित प्रकार से अपडेट करें:

#### Noise पहचानकर्ता

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

परिवर्तन: वर्तमान NTCP2 में केवल ChaCha सेक्शन में विकल्प हैं। ML-KEM के साथ, ChaCha सेक्शन में एन्क्रिप्टेड PQ public key भी होगी।

ताकि PQ और non-PQ NTCP2 दोनों को एक ही router पते और पोर्ट पर समर्थित किया जा सके, हम X मान (X25519 ephemeral public key) के सबसे महत्वपूर्ण बिट का उपयोग करते हैं यह दर्शाने के लिए कि यह एक PQ कनेक्शन है। यह बिट non-PQ कनेक्शन के लिए हमेशा unset रहता है।

Alice के लिए, संदेश को Noise द्वारा एन्क्रिप्ट किए जाने के बाद, लेकिन X के AES obfuscation से पहले, X[31] |= 0x7f सेट करें।

Bob के लिए, X के AES de-obfuscation के बाद, X[31] & 0x80 का परीक्षण करें। यदि बिट सेट है, तो इसे X[31] &= 0x7f के साथ साफ करें, और PQ कनेक्शन के रूप में Noise के माध्यम से decrypt करें। यदि बिट साफ है, तो सामान्य रूप से non-PQ कनेक्शन के रूप में Noise के माध्यम से decrypt करें।

PQ NTCP2 के लिए जो एक अलग router पते और port पर विज्ञापित है, यह आवश्यक नहीं है।

अतिरिक्त जानकारी के लिए, नीचे दिए गए Published Addresses सेक्शन को देखें।

कच्ची सामग्री:

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
अनएन्क्रिप्टेड डेटा (Poly1305 प्रमाणीकरण टैग दिखाया नहीं गया):

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
नोट: message 1 options block में version field को 2 पर सेट करना होगा, यहाँ तक कि PQ connections के लिए भी।

आकार:

| प्रकार | प्रकार कोड | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | opt len |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
नोट: टाइप कोड केवल आंतरिक उपयोग के लिए हैं। Router टाइप 4 ही रहेंगे, और समर्थन router addresses में इंगित किया जाएगा।

#### 2) SessionCreated

कच्ची सामग्री:

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
अनएन्क्रिप्टेड डेटा (Poly1305 auth tag दिखाया नहीं गया):

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
आकार:

| Type | Type Code | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
नोट: Type codes केवल आंतरिक उपयोग के लिए हैं। Router type 4 ही रहेंगे, और समर्थन router addresses में दिखाया जाएगा।

#### 3) SessionConfirmed

अपरिवर्तित

#### Key Derivation Function (KDF) (डेटा चरण के लिए)

अपरिवर्तित

#### प्रकाशित पते

सभी मामलों में, हमेशा की तरह NTCP2 transport name का उपयोग करें।

गैर-PQ, गैर-firewalled के समान address/port का उपयोग करें। केवल एक PQ variant समर्थित है। router address में, v=2 (सामान्य रूप से) और नया parameter pq=[3|4|5] प्रकाशित करें जो MLKEM 512/768/1024 को दर्शाता है। Alice session request में ephemeral key के MSB (key[31] & 0x80) को सेट करती है यह दर्शाने के लिए कि यह एक hybrid connection है। ऊपर देखें। पुराने routers pq parameter को अनदेखा कर देंगे और सामान्य रूप से गैर-pq कनेक्ट करेंगे।

गैर-PQ के रूप में अलग पता/पोर्ट, या केवल PQ, गैर-फ़ायरवॉल समर्थित नहीं है। इसे तब तक लागू नहीं किया जाएगा जब तक गैर-PQ NTCP2 को अक्षम नहीं कर दिया जाता, जो अब से कई साल बाद होगा। जब गैर-PQ अक्षम हो जाएगा, तो कई PQ वेरिएंट समर्थित हो सकते हैं, लेकिन प्रत्येक पते के लिए केवल एक। router पते में, MLKEM 512/768/1024 को इंगित करने के लिए v=[3|4|5] प्रकाशित करें। Alice ephemeral key का MSB सेट नहीं करता। पुराने router v पैरामीटर की जांच करेंगे और इस पते को असमर्थित के रूप में छोड़ देंगे।

Firewalled addresses (कोई IP प्रकाशित नहीं): router address में, v=2 प्रकाशित करें (हमेशा की तरह)। pq parameter प्रकाशित करने की कोई आवश्यकता नहीं है।

Alice एक PQ Bob से उस PQ variant का उपयोग करके कनेक्ट हो सकती है जो Bob प्रकाशित करता है, चाहे Alice अपनी router info में pq support का विज्ञापन करे या न करे, या चाहे वह समान variant का विज्ञापन करे।

#### अधिकतम पैडिंग

वर्तमान specification में, message 1 और 2 को "उचित" मात्रा में padding के साथ परिभाषित किया गया है, जिसमें 0-31 bytes की range की सिफारिश की गई है, और कोई अधिकतम सीमा निर्दिष्ट नहीं है।

API 0.9.68 (रिलीज़ 2.11.0) के माध्यम से, Java I2P ने non-PQ connections के लिए अधिकतम 256 bytes padding को implemented किया था, हालांकि इसे पहले documented नहीं किया गया था। API 0.9.69 (रिलीज़ 2.12.0) से, Java I2P non-PQ connections के लिए वही max padding implement करता है जो MLKEM-512 के लिए है। नीचे दी गई table देखें।

परिभाषित संदेश आकार का उपयोग अधिकतम पैडिंग के रूप में करें, अर्थात्, अधिकतम पैडिंग PQ कनेक्शन के लिए संदेश आकार को दोगुना कर देगी, निम्नलिखित प्रकार से:

| Message Max Padding | non-PQ (thru 0.9.68) | non-PQ (as of 0.9.69) | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------|----------------------|-----------------------|-----------|-----------|------------|
| Session Request  |   256   |   880   |    880   |     1264   |    1648  |
| Session Created  |   256   |   848   |    848   |     1136   |    1616  |
### SSU2

SSU2 विशिष्टता [/docs/specs/ssu2/](/docs/specs/ssu2/) को निम्नलिखित रूप में अपडेट करें:

#### Noise पहचानकर्ता

- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"

ध्यान दें कि MLKEM-1024 SSU2 के लिए समर्थित नहीं है, क्योंकि keys एक मानक 1500 byte datagram के भीतर fit होने के लिए बहुत बड़ी हैं।

#### लंबा हेडर

लंबा हेडर 32 बाइट्स का होता है। यह सत्र बनने से पहले, Token Request, SessionRequest, SessionCreated, और Retry के लिए उपयोग किया जाता है। यह सत्र के बाहर के Peer Test और Hole Punch संदेशों के लिए भी उपयोग किया जाता है।

निम्नलिखित संदेशों में, MLKEM-512 या MLKEM-768 को इंगित करने के लिए लंबे हेडर में ver (version) फ़ील्ड को 3 या 4 पर सेट करें।

- (0) Session Request (सत्र अनुरोध)
- (1) Session Created (सत्र निर्मित)
- (9) Retry (पुनः प्रयास)
- (10) Token Request (टोकन अनुरोध)
- (11) Hole Punch (होल पंच)

निम्नलिखित संदेशों में, long header में ver (version) फ़ील्ड को 2 पर सेट करें, जैसा कि सामान्यतः किया जाता है, भले ही MLKEM-512 या MLKEM-768 समर्थित हो। यदि दूसरा छोर इसका समर्थन करता है तो implementations मान को 3 या 4 पर भी सेट कर सकते हैं, लेकिन यह आवश्यक नहीं है। Implementations को कोई भी मान 2-4 स्वीकार करना चाहिए।

- (7) पीयर टेस्ट (सत्र के बाहर संदेश 5-7)

चर्चा: सभी message प्रकारों के लिए version फील्ड को 3 या 4 पर सेट करना सख्त रूप से आवश्यक नहीं हो सकता है, लेकिन ऐसा करने से unsupported post-quantum connections के लिए पहले failure detection में मदद मिलती है। Token Request और Retry (प्रकार 9 और 10) में consistency के लिए versions 3/4 होने चाहिए। Hole Punch messages (प्रकार 11) को इस treatment की आवश्यकता नहीं हो सकती है लेकिन हम uniformity के लिए समान pattern का पालन करेंगे। Peer Test messages (प्रकार 7) out-of-session है और session शुरू करने के intent को इंगित नहीं करता है।

header encryption से पहले:

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
#### छोटा हेडर

अपरिवर्तित

#### SessionRequest (प्रकार 0)

परिवर्तन: वर्तमान SSU2 में ChaCha सेक्शन में केवल ब्लॉक डेटा होता है। ML-KEM के साथ, ChaCha सेक्शन में एन्क्रिप्टेड PQ पब्लिक की भी होगी।

स्पूफ सुरक्षा के लिए KDF परिवर्तन: Proposal 165 [Prop165]_ में उठाए गए मुद्दों को संबोधित करने के लिए, लेकिन एक अलग समाधान के साथ, हम Session Request के लिए KDF को संशोधित करते हैं। यह केवल PQ sessions के लिए है। गैर-PQ sessions के लिए KDF अपरिवर्तित रहता है।

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
कच्ची सामग्री:

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
अनएन्क्रिप्टेड डेटा (Poly1305 प्रमाणीकरण टैग नहीं दिखाया गया):

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
आकार, IP ओवरहेड शामिل नहीं:

| प्रकार | प्रकार कोड | X लंबाई | Msg 1 लंबाई | Msg 1 Enc लंबाई | Msg 1 Dec लंबाई | PQ key लंबाई | pl लंबाई |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 896+pl | 832+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1280+pl | 1216+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | n/a | बहुत बड़ा | | | | |
नोट: टाइप कोड केवल आंतरिक उपयोग के लिए हैं। Router टाइप 4 ही रहेंगे, और समर्थन router addresses में दर्शाया जाएगा।

MLKEM768_X25519 के लिए न्यूनतम MTU: IPv4 के लिए लगभग 1316 और IPv6 के लिए 1336।

#### SessionCreated (Type 1)

परिवर्तन: वर्तमान SSU2 में ChaCha सेक्शन में केवल ब्लॉक डेटा होता है। ML-KEM के साथ, ChaCha सेक्शन में एन्क्रिप्टेड PQ पब्लिक की भी होगी।

कच्ची सामग्री:

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
असंवृत्त डेटा (Poly1305 auth tag दिखाया नहीं गया):

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
आकार, IP overhead को शामिल नहीं करते हुए:

| प्रकार | प्रकार कोड | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | pl len |
|------|-----------|-------|-----------|---------------|---------------|-----------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 864+pl | 800+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1184+pl | 1118+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | n/a | बहुत बड़ा | | | | |
नोट: टाइप कोड केवल आंतरिक उपयोग के लिए हैं। Router टाइप 4 ही रहेंगे, और समर्थन का संकेत router addresses में दिया जाएगा।

MLKEM768_X25519 के लिए न्यूनतम MTU: IPv4 के लिए लगभग 1316 और IPv6 के लिए 1336।

#### SessionConfirmed (Type 2)

अपरिवर्तित

#### डेटा चरण के लिए KDF

अपरिवर्तित

#### रिले और पीयर टेस्ट

निम्नलिखित blocks में version fields हैं। ये version 2 ही रहेंगे (गैर-PQ Bob के साथ compatibility के लिए), और PQ के लिए version 3/4 में नहीं बदलेंगे।

- Relay Request
- Relay Response
- Relay Intro
- Peer Test

PQ Signatures: Relay blocks, Peer Test blocks, और Peer Test messages सभी में signatures होती हैं। दुर्भाग्य से, PQ signatures MTU से बड़ी होती हैं। वर्तमान में कोई तंत्र नहीं है जो Relay या Peer Test blocks या messages को कई UDP packets में fragment कर सके। protocol को fragmentation का समर्थन करने के लिए बढ़ाया जाना चाहिए। यह एक अलग प्रस्ताव में किया जाएगा जो TBD है। जब तक यह पूरा नहीं होता, Relay और Peer Test का समर्थन नहीं किया जाएगा।

#### प्रकाशित पते

सभी मामलों में, SSU2 transport नाम का सामान्य रूप से उपयोग करें। MLKEM-1024 समर्थित नहीं है।

non-PQ, non-firewalled के समान address/port का उपयोग करें। एक या दोनों PQ variants समर्थित हैं। router address में, v=2 (सामान्य रूप से) और नया parameter pq=[3|4|3,4] publish करें ताकि MLKEM 512/768/both को indicate किया जा सके। पुराने routers pq parameter को ignore करेंगे और सामान्य रूप से non-pq connect करेंगे।

non-PQ से अलग address/port, या PQ-only, non-firewalled समर्थित नहीं है। यह तब तक लागू नहीं किया जाएगा जब तक non-PQ SSU2 अक्षम नहीं हो जाता, जो अब से कई साल बाद होगा। जब non-PQ अक्षम हो जाएगा, तो एक या दोनों PQ variants समर्थित होंगे। router address में, MLKEM 512/768/दोनों को इंगित करने के लिए v=[3|4|3,4] प्रकाशित करें। पुराने routers v parameter की जांच करेंगे और इस address को असमर्थित मानकर छोड़ देंगे।

Firewalled addresses (कोई IP प्रकाशित नहीं): router address में, v=2 प्रकाशित करें (सामान्य रूप से)। pq parameter को firewalled addresses में अवश्य प्रकाशित किया जाना चाहिए, relay को समर्थन देने के लिए।

Alice, Bob द्वारा प्रकाशित PQ variant का उपयोग करके PQ Bob से कनेक्ट हो सकती है, चाहे Alice अपने router info में pq support का विज्ञापन करे या न करे, या चाहे वह समान variant का विज्ञापन करे।

#### MTU

MLKEM768 के साथ MTU से अधिक न जाने की सावधानी बरतें। SSU2 के लिए न्यूनतम MTU 1280 है, जो बिना padding के message 1 का आकार है। यदि Alice या Bob का MTU 1280 है तो message 1 में padding शामिल न करें।

#### मुद्दे

हम आंतरिक रूप से version फ़ील्ड का उपयोग कर सकते हैं और MLKEM512 के लिए 3 तथा MLKEM768 के लिए 4 का उपयोग कर सकते हैं।

संदेश 1 और 2 के लिए, MLKEM768 पैकेट साइज़ को 1280 न्यूनतम MTU से अधिक बढ़ा देगा। संभवतः यदि MTU बहुत कम होगा तो उस कनेक्शन के लिए इसका समर्थन नहीं किया जाएगा।

संदेश 1 और 2 के लिए, MLKEM1024 पैकेट आकार को 1500 अधिकतम MTU से अधिक बढ़ा देगा। इसके लिए संदेश 1 और 2 को खंडित करना आवश्यक होगा, और यह एक बड़ी जटिलता होगी। शायद ऐसा नहीं करेंगे।

Relay और Peer Test: ऊपर देखें

### स्ट्रीमिंग

TODO: क्या signature की कॉपी से बचने के लिए signing/verification को परिभाषित करने का कोई अधिक कुशल तरीका है?

### SU3 फ़ाइलें

करने योग्य कार्य

[IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) धारा 8.1 X.509 प्रमाणपत्रों में HashML-DSA की अनुमति नहीं देती है और HashML-DSA के लिए OIDs असाइन नहीं करती है, क्योंकि इसमें implementation की जटिलताएं और कम सुरक्षा है।

SU3 files के PQ-only signatures के लिए, certificates के लिए non-prehash variants के [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) में परिभाषित OIDs का उपयोग करें। हम SU3 files के hybrid signatures को परिभाषित नहीं करते हैं, क्योंकि हमें files को दो बार hash करना पड़ सकता है (हालांकि HashML-DSA और X2559 समान hash function SHA512 का उपयोग करते हैं)। इसके अतिरिक्त, X.509 certificate में दो keys और signatures को concatenate करना पूर्णतः nonstandard होगा।

ध्यान दें कि हम SU3 files के Ed25519 signing की अनुमति नहीं देते हैं, और जबकि हमने Ed25519ph signing को परिभाषित किया है, हमने इसके लिए कभी भी किसी OID पर सहमति नहीं बनाई है, या इसका उपयोग नहीं किया है।

SU3 फाइलों के लिए सामान्य sig types की अनुमति नहीं है; ph (prehash) variants का उपयोग करें।

### अन्य विशिष्टताएं

नया अधिकतम Destination आकार 2599 होगा (base 64 में 3468)।

अन्य दस्तावेजों को अपडेट करें जो Destination sizes पर मार्गदर्शन प्रदान करते हैं, जिनमें शामिल है:

- SAMv3
- Bittorrent
- डेवलपर दिशानिर्देश
- नामकरण / पता पुस्तिका / जंप सर्वर
- अन्य दस्तावेज़

## ओवरहेड विश्लेषण

### कुंजी विनिमय

आकार वृद्धि (बाइट्स):

| Type | Pubkey (Msg 1) | Cipertext (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
गति:

[Cloudflare](https://blog.cloudflare.com/pq-2024/) द्वारा रिपोर्ट की गई गति:

| प्रकार | सापेक्षिक गति |
|------|----------------|
| X25519 DH/keygen | आधार |
| MLKEM512 | 2.25x तेज़ |
| MLKEM768 | 1.5x तेज़ |
| MLKEM1024 | 1x (समान) |
| XK | 4x DH (keygen + 3 DH) |
| MLKEM512_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 4.9x DH = 22% धीमा |
| MLKEM768_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 5.3x DH = 32% धीमा |
| MLKEM1024_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 6x DH = 50% धीमा |
Java में प्रारंभिक परीक्षण परिणाम:

| प्रकार | Relative DH/encaps | DH/decaps | keygen |
|------|-------------------|-----------|--------|
| X25519 | baseline | baseline | baseline |
| MLKEM512 | 29x तेज़ | 22x तेज़ | 17x तेज़ |
| MLKEM768 | 17x तेज़ | 14x तेज़ | 9x तेज़ |
| MLKEM1024 | 12x तेज़ | 10x तेज़ | 6x तेज़ |
### हस्ताक्षर

आकार:

विशिष्ट key, sig, RIdent, Dest साइज़ या साइज़ वृद्धि (Ed25519 संदर्भ के लिए शामिल) RIs के लिए X25519 encryption type मानते हुए। Router Info, LeaseSet, repliable datagrams, और दोनों streaming (SYN और SYN ACK) packets में से प्रत्येक के लिए जोड़ा गया साइज़ सूचीबद्ध है। वर्तमान Destinations और Leasesets में दोहराया गया padding होता है और ये in-transit संपीड़ित हो सकते हैं। नए प्रकारों में padding नहीं होता है और ये संपीड़ित नहीं होंगे, जिसके परिणामस्वरूप in-transit में बहुत अधिक साइज़ वृद्धि होगी। ऊपर design section देखें।

| प्रकार | Pubkey | Sig | Key+Sig | RIdent | Dest | RInfo | LS/Streaming/Datagram (प्रत्येक संदेश) |
|------|--------|-----|---------|--------|------|-------|----------------------------------|
| EdDSA_SHA512_Ed25519 | 32 | 64 | 96 | 391 | 391 | baseline | baseline |
| MLDSA44 | 1312 | 2420 | 3732 | 1351 | 1319 | +3316 | +3284 |
| MLDSA65 | 1952 | 3309 | 5261 | 1991 | 1959 | +5668 | +5636 |
| MLDSA87 | 2592 | 4627 | 7219 | 2631 | 2599 | +7072 | +7040 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 2484 | 3828 | 1383 | 1351 | +3412 | +3380 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 3373 | 5357 | 2023 | 1991 | +5668 | +5636 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 4691 | 7315 | 2663 | 2631 | +7488 | +7456 |
गति:

[Cloudflare](https://blog.cloudflare.com/pq-2024/) द्वारा रिपोर्ट की गई गति:

| प्रकार | सापेक्ष गति संकेत | सत्यापन |
|------|---------------------|--------|
| EdDSA_SHA512_Ed25519 | आधारभूत | आधारभूत |
| MLDSA44 | 5x धीमा | 2x तेज़ |
| MLDSA65 | ??? | ??? |
| MLDSA87 | ??? | ??? |
Java में प्रारंभिक परीक्षण परिणाम:

| प्रकार | सापेक्षिक गति चिह्न | सत्यापन | कीजेन |
|------|---------------------|--------|--------|
| EdDSA_SHA512_Ed25519 | आधारभूत | आधारभूत | आधारभूत |
| MLDSA44 | 4.6x धीमा | 1.7x तेज़ | 2.6x तेज़ |
| MLDSA65 | 8.1x धीमा | समान | 1.5x तेज़ |
| MLDSA87 | 11.1x धीमा | 1.5x धीमा | समान |
## सुरक्षा विश्लेषण

NIST सुरक्षा श्रेणियों का सारांश [NIST presentation](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) स्लाइड 10 में दिया गया है। प्रारंभिक मानदंड: हमारी न्यूनतम NIST सुरक्षा श्रेणी hybrid protocols के लिए 2 और PQ-only के लिए 3 होनी चाहिए।

| Category | As Secure As |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### हैंडशेक

ये सभी हाइब्रिड प्रोटोकॉल हैं। implementations को MLKEM768 को प्राथमिकता देनी चाहिए; MLKEM512 पर्याप्त सुरक्षित नहीं है।

NIST सुरक्षा श्रेणियां [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| एल्गोरिदम | सुरक्षा श्रेणी |
|-----------|-------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
### हस्ताक्षर

यह प्रस्ताव hybrid और PQ-only दोनों signature प्रकारों को परिभाषित करता है। MLDSA44 hybrid, MLDSA65 PQ-only से बेहतर है। MLDSA65 और MLDSA87 के लिए keys और sig sizes शायद हमारे लिए बहुत बड़े हैं, कम से कम शुरुआत में।

NIST सुरक्षा श्रेणियां [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf):

| एल्गोरिदम | सुरक्षा श्रेणी |
|-----------|-------------------|
| MLDSA44 | 2 |
| MLKEM67 | 3 |
| MLKEM87 | 5 |
## प्रकार प्राथमिकताएं

जबकि हम 3 crypto और 9 signature प्रकारों को परिभाषित और कार्यान्वित करेंगे, हम विकास के दौरान प्रदर्शन को मापने और बढ़े हुए structure आकारों के प्रभावों का और विश्लेषण करने की योजना बनाते हैं। हम अन्य परियोजनाओं और प्रोटोकॉल में विकास पर अनुसंधान और निगरानी भी जारी रखेंगे।

एक वर्ष या उससे अधिक के विकास के बाद हम प्रत्येक उपयोग मामले के लिए एक पसंदीदा प्रकार या डिफ़ॉल्ट पर निर्णय लेने का प्रयास करेंगे। चयन के लिए बैंडविड्थ, CPU, और अनुमानित सुरक्षा स्तर के बीच समझौता करना होगा। सभी प्रकार सभी उपयोग मामलों के लिए उपयुक्त या अनुमतित नहीं हो सकते हैं।

प्रारंभिक प्राथमिकताएं निम्नलिखित हैं, जो परिवर्तन के अधीन हैं:

Encryption: MLKEM768_X25519

हस्ताक्षर: MLDSA44_EdDSA_SHA512_Ed25519

प्रारंभिक प्रतिबंध निम्नलिखित हैं, जो परिवर्तन के अधीन हैं:

एन्क्रिप्शन: MLKEM1024_X25519 SSU2 के लिए अनुमतित नहीं है

सिग्नेचर: MLDSA87 और hybrid variant संभवतः बहुत बड़े हैं; MLDSA65 और hybrid variant बहुत बड़े हो सकते हैं

## कार्यान्वयन टिप्पणियाँ

### लाइब्रेरी सहायता

Bouncycastle, BoringSSL, और WolfSSL libraries अब MLKEM और MLDSA का समर्थन करती हैं। OpenSSL का समर्थन उनकी 3.5 रिलीज़ में 8 अप्रैल, 2025 को होगा [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)।

Java I2P द्वारा अनुकूलित southernstorm.com Noise लाइब्रेरी में hybrid handshakes के लिए प्रारंभिक समर्थन था, लेकिन हमने इसे अप्रयुक्त होने के कारण हटा दिया था; हमें इसे वापस जोड़ना होगा और [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) के अनुरूप अपडेट करना होगा।

### हस्ताक्षर रूप

हम [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) सेक्शन 3.4 में परिभाषित "hedged" या randomized signing variant का उपयोग करेंगे, न कि "determinstic" variant का। यह सुनिश्चित करता है कि प्रत्येक signature अलग हो, यहाँ तक कि समान डेटा पर भी, और side-channel attacks के विरुद्ध अतिरिक्त सुरक्षा प्रदान करता है। जबकि [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) निर्दिष्ट करता है कि "hedged" variant डिफ़ॉल्ट है, यह विभिन्न libraries में सत्य हो भी सकता है और नहीं भी। Implementors को यह सुनिश्चित करना चाहिए कि signing के लिए "hedged" variant का उपयोग हो।

हम सामान्य signing प्रक्रिया (जिसे Pure ML-DSA Signature Generation कहा जाता है) का उपयोग करते हैं जो message को आंतरिक रूप से 0x00 || len(ctx) || ctx || message के रूप में encode करती है, जहाँ ctx कुछ वैकल्पिक मान है जिसका आकार 0x00..0xFF है। हम किसी वैकल्पिक context का उपयोग नहीं कर रहे हैं। len(ctx) == 0। यह प्रक्रिया [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) Algorithm 2 step 10 और Algorithm 3 step 5 में परिभाषित है। ध्यान दें कि कुछ प्रकाशित test vectors में एक mode सेट करने की आवश्यकता हो सकती है जहाँ message को encode नहीं किया जाता।

### विश्वसनीयता

आकार बढ़ाने से NetDB स्टोर्स, स्ट्रीमिंग हैंडशेक्स, और अन्य संदेशों के लिए tunnel fragmentation काफी अधिक हो जाएगा। प्रदर्शन और विश्वसनीयता में बदलावों की जाँच करें।

### संरचना आकार

router infos और leasesets के byte size को सीमित करने वाले किसी भी कोड को खोजें और जांचें।

### NetDB

RAM या डिस्क में संग्रहीत अधिकतम LS/RI की समीक्षा करें और संभवतः कम करें, ताकि स्टोरेज वृद्धि को सीमित किया जा सके। floodfills के लिए न्यूनतम बैंडविड्थ आवश्यकताओं को बढ़ाएं?

### रैचेट

#### साझा Tunnels

संदेश 1 (New Session Message) की लंबाई जांच के आधार पर समान tunnels पर कई protocols का auto-classify/detect करना संभव होना चाहिए। MLKEM512_X25519 को उदाहरण के रूप में उपयोग करते हुए, संदेश 1 की लंबाई वर्तमान ratchet protocol से 816 bytes अधिक है, और न्यूनतम संदेश 1 का आकार (केवल DateTime payload के साथ) 919 bytes है। वर्तमान ratchet के साथ अधिकांश संदेश 1 के आकार में 816 bytes से कम payload होता है, इसलिए उन्हें non-hybrid ratchet के रूप में वर्गीकृत किया जा सकता है। बड़े संदेश संभवतः POSTs हैं जो दुर्लभ हैं।

तो अनुशंसित रणनीति है:

- यदि message 1 919 bytes से कम है, तो यह वर्तमान ratchet protocol है।
- यदि message 1 919 bytes के बराबर या अधिक है, तो यह संभवतः MLKEM512_X25519 है।
  पहले MLKEM512_X25519 आज़माएं, और यदि यह विफल हो जाता है, तो वर्तमान ratchet protocol आज़माएं।

यह हमें एक ही destination पर standard ratchet और hybrid ratchet को कुशलतापूर्वक support करने की अनुमति देगा, जैसे हमने पहले एक ही destination पर ElGamal और ratchet को support किया था। इसलिए, हम MLKEM hybrid protocol में बहुत तेज़ी से migrate कर सकते हैं, क्योंकि अगर हम एक ही destination के लिए dual-protocols को support नहीं कर सकते तो उससे कहीं ज्यादा तेज़, क्योंकि हम मौजूदा destinations में MLKEM support जोड़ सकते हैं।

आवश्यक समर्थित संयोजन हैं:

- X25519 + MLKEM512
- X25519 + MLKEM768
- X25519 + MLKEM1024

निम्नलिखित संयोजन जटिल हो सकते हैं, और इन्हें समर्थित करना आवश्यक नहीं है, लेकिन ये implementation-dependent हो सकते हैं:

- एक से अधिक MLKEM
- ElG + एक या अधिक MLKEM
- X25519 + एक या अधिक MLKEM
- ElG + X25519 + एक या अधिक MLKEM

हम एक ही destination पर कई MLKEM algorithms (उदाहरण के लिए, MLKEM512_X25519 और MLKEM_768_X25519) को support करने का प्रयास नहीं कर सकते। केवल एक चुनें; हालांकि, यह हमारे द्वारा एक पसंदीदा MLKEM variant का चयन करने पर निर्भर करता है, ताकि HTTP client tunnels एक का उपयोग कर सकें। Implementation-dependent।

हम एक ही destination पर तीन algorithms (उदाहरण के लिए X25519, MLKEM512_X25519, और MLKEM769_X25519) को support करने का प्रयास कर सकते हैं। classification और retry strategy बहुत जटिल हो सकती है। configuration और configuration UI बहुत जटिल हो सकता है। Implementation-dependent।

हम संभवतः एक ही destination पर ElGamal और hybrid algorithms दोनों को support करने का प्रयास नहीं करेंगे। ElGamal पुराना हो चुका है, और ElGamal + hybrid केवल (बिना X25519 के) का अधिक अर्थ नहीं है। इसके अलावा, ElGamal और Hybrid New Session Messages दोनों बड़े होते हैं, इसलिए classification strategies को अक्सर दोनों decryptions आज़माने पड़ते हैं, जो अकुशल होगा। Implementation-dependent है।

क्लाइंट समान टनल पर X25519 और hybrid protocols के लिए समान या अलग X25519 static keys का उपयोग कर सकते हैं, यह implementation पर निर्भर करता है।

#### फॉरवर्ड सिक्योरिटी

ECIES specification New Session Message payload में Garlic Messages की अनुमति देती है, जो प्रारंभिक streaming packet (आमतौर पर एक HTTP GET) की 0-RTT delivery को client के leaseset के साथ मिलकर संभव बनाता है। हालांकि, New Session Message payload में forward secrecy नहीं होती है। चूंकि यह proposal ratchet के लिए enhanced forward secrecy पर जोर दे रहा है, implementations को streaming payload, या पूरे streaming message को पहले Existing Session Message तक के लिए स्थगित करना चाहिए या कर सकते हैं। यह 0-RTT delivery की कीमत पर होगा। रणनीतियां traffic type या tunnel type, या उदाहरण के लिए GET vs. POST पर भी निर्भर हो सकती हैं। Implementation-dependent।

#### नया सेशन आकार

MLKEM, MLDSA, या दोनों को एक ही destination पर उपयोग करना, New Session Message का आकार नाटकीय रूप से बढ़ाएगा, जैसा कि ऊपर वर्णित है। यह tunnels के माध्यम से New Session Message delivery की विश्वसनीयता को काफी कम कर सकता है, जहाँ उन्हें कई 1024 byte tunnel messages में खंडित करना पड़ता है। Delivery की सफलता fragments की exponential संख्या के अनुपातिक होती है। Implementations विभिन्न रणनीतियों का उपयोग करके message के आकार को सीमित कर सकते हैं, 0-RTT delivery की कीमत पर। Implementation-dependent।

### NTCP2

हम session request में ephemeral key का MSB (key[31] & 0x80) सेट करते हैं यह दर्शाने के लिए कि यह एक hybrid connection है। यह हमें एक ही port पर standard NTCP और hybrid NTCP दोनों चलाने की अनुमति देता है। केवल एक hybrid variant को support किया जाएगा, और router address में advertise किया जाएगा। उदाहरण के लिए, v=2,3 या v=2,4 या v=2,5।

#### अस्पष्टीकरण

Alice के रूप में, PQ connection के लिए, obfuscation से पहले, X[31] |= 0x80 सेट करें। यह X को एक invalid X25519 public key बनाता है। Obfuscation के बाद, AES-CBC इसे randomize कर देगा। Obfuscation के बाद X का MSB random होगा।

Bob के रूप में, de-obfuscation के बाद जांचें कि क्या (X[31] & 0x80) != 0 है। यदि हां, तो यह एक PQ connection है।

NTCP2-PQ के लिए आवश्यक न्यूनतम router संस्करण TBD है।

नोट: टाइप कोड केवल आंतरिक उपयोग के लिए हैं। Router टाइप 4 ही रहेंगे, और समर्थन router addresses में दर्शाया जाएगा।

### SSU2

हम long header में version field का उपयोग करते हैं और इसे MLKEM512 के लिए 3 और MLKEM768 के लिए 4 पर सेट करते हैं। address में v=2,3,4 पर्याप्त होगा।

जांचें और सत्यापित करें कि SSU2 कई packets (6-8?) में विभाजित MLDSA-signed RI को संभाल सकता है।

नोट: Type codes केवल आंतरिक उपयोग के लिए हैं। Routers type 4 ही रहेंगे, और समर्थन router addresses में दिखाया जाएगा।

## Router संगतता

### ट्रांसपोर्ट नाम

सभी मामलों में, NTCP2 और SSU2 transport नामों का उपयोग हमेशा की तरह करें।

### Router एन्क्रिप्शन प्रकार

हमारे पास विचार करने के लिए कई विकल्प हैं:

#### Type 5/6/7 Routers

अनुशंसित नहीं। केवल ऊपर सूचीबद्ध नए transports का उपयोग करें जो router प्रकार से मेल खाते हैं। पुराने routers कनेक्ट नहीं कर सकते, इनके माध्यम से tunnels नहीं बना सकते, या netDb संदेश नहीं भेज सकते। डिफ़ॉल्ट रूप से सक्षम करने से पहले समर्थन को debug करने और सुनिश्चित करने में कई release cycles लगेंगे। नीचे दिए गए विकल्पों की तुलना में rollout को एक साल या अधिक तक बढ़ा सकता है।

#### Type 4 Routers

अनुशंसित। चूंकि PQ X25519 static key या N handshake protocols को प्रभावित नहीं करता, हम routers को type 4 के रूप में छोड़ सकते हैं, और केवल नए transports का विज्ञापन कर सकते हैं। पुराने routers अभी भी connect कर सकते हैं, उनके माध्यम से tunnels बना सकते हैं, या netdb messages भेज सकते हैं।

#### सिफारिशें

MLKEM-768 को Ratchet, NTCP2, और SSU2 के लिए सुझाया जाता है, क्योंकि यह सुरक्षा और key length का सबसे अच्छा संतुलन प्रदान करता है।

### Router हस्ताक्षर प्रकार

#### Type 12-17 Routers

पुराने router RIs को सत्यापित करते हैं और इसलिए कनेक्ट नहीं कर सकते, इनके माध्यम से tunnel नहीं बना सकते, या netdb संदेश नहीं भेज सकते। डिफ़ॉल्ट रूप से सक्षम करने से पहले समर्थन को डिबग करने और सुनिश्चित करने के लिए कई रिलीज़ चक्र लगेंगे। यह enc. type 5/6/7 रोलआउट के समान समस्याएं होंगी; ऊपर सूचीबद्ध type 4 enc. type रोलआउट विकल्प की तुलना में रोलआउट को एक साल या अधिक तक बढ़ा सकता है।

कोई विकल्प नहीं।

### LS Enc. Types

#### Type 5-7 LS Keys

ये पुराने type 4 X25519 keys के साथ LS में मौजूद हो सकते हैं। पुराने router अज्ञात keys को नजरअंदाज कर देंगे।

Destinations कई key types को support कर सकते हैं, लेकिन केवल प्रत्येक key के साथ message 1 के trial decrypts करके। इस overhead को प्रत्येक key के लिए successful decrypts की गिनती बनाए रखकर और सबसे अधिक उपयोग की गई key को पहले try करके कम किया जा सकता है। Java I2P एक ही destination पर ElGamal+X25519 के लिए इस रणनीति का उपयोग करता है।

### गंतव्य हस्ताक्षर प्रकार

#### टाइप 12-17 Dests

Router leaseset signatures को verify करते हैं और इसलिए type 12-17 destinations के लिए connect नहीं कर सकते या leaseset प्राप्त नहीं कर सकते। Default रूप से enable करने से पहले debug करने और support सुनिश्चित करने के लिए कई release cycles की आवश्यकता होगी।

कोई विकल्प नहीं।

## प्राथमिकताएं और रोलआउट

सबसे मूल्यवान डेटा end-to-end ट्रैफिक है, जो ratchet से एन्क्रिप्टेड होता है। tunnel hops के बीच एक बाहरी पर्यवेक्षक के रूप में, वह दो बार और एन्क्रिप्टेड होता है, tunnel encryption और transport encryption के साथ। OBEP और IBGW के बीच एक बाहरी पर्यवेक्षक के रूप में, यह केवल एक बार और एन्क्रिप्टेड होता है, transport encryption के साथ। OBEP या IBGW प्रतिभागी के रूप में, ratchet ही एकमात्र encryption है। हालांकि, चूंकि tunnels एकदिशीय होते हैं, ratchet handshake में दोनों संदेशों को कैप्चर करने के लिए मिलीभगत करने वाले routers की आवश्यकता होगी, जब तक कि tunnels को समान router पर OBEP और IBGW के साथ नहीं बनाया गया हो।

अभी सबसे चिंताजनक PQ threat model यह है कि आज ट्रैफिक को स्टोर करना और कई-कई वर्षों बाद उसे decrypt करना (forward secrecy)। एक hybrid approach इससे सुरक्षा प्रदान कर सकता है।

PQ threat model में authentication keys को किसी उचित समय अवधि (मान लेते हैं कुछ महीने) में तोड़ना और फिर authentication की नकल करना या लगभग real-time में decrypt करना, यह बहुत दूर की बात है? और तभी हमें PQC static keys पर migrate करना होगा।

तो, सबसे पुराना PQ threat model OBEP/IBGW द्वारा बाद में decryption के लिए traffic को store करना है। हमें पहले hybrid ratchet को implement करना चाहिए।

Ratchet सबसे उच्च प्राथमिकता है। Transport अगली प्राथमिकता में हैं। Signature सबसे कम प्राथमिकता हैं।

Signature rollout भी encryption rollout से एक साल या अधिक बाद होगा, क्योंकि कोई backward compatibility संभव नहीं है। इसके अलावा, उद्योग में MLDSA adoption को CA/Browser Forum और Certificate Authorities द्वारा मानकीकृत किया जाएगा। CAs को पहले hardware security module (HSM) समर्थन की आवश्यकता है, जो वर्तमान में उपलब्ध नहीं है [CA/Browser Forum](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)। हम उम्मीद करते हैं कि CA/Browser Forum विशिष्ट parameter choices पर निर्णय लेगा, जिसमें composite signatures का समर्थन करना या आवश्यक बनाना शामिल है [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)।

| मील का पत्थर | लक्ष्य |
|-----------|--------|
| Ratchet beta | देर 2025 |
| सर्वोत्तम enc प्रकार चुनें | प्रारंभिक 2026 |
| NTCP2 beta | प्रारंभिक 2026 |
| SSU2 beta | मध्य 2026 |
| Ratchet production | मध्य 2026 |
| Ratchet default | देर 2026 |
| Signature beta | देर 2026 |
| NTCP2 production | देर 2026 |
| SSU2 production | प्रारंभिक 2027 |
| सर्वोत्तम sig प्रकार चुनें | प्रारंभिक 2027 |
| NTCP2 default | प्रारंभिक 2027 |
| SSU2 default | मध्य 2027 |
| Signature production | मध्य 2027 |
## माइग्रेशन

यदि हम एक ही tunnel पर पुराने और नए ratchet प्रोटोकॉल दोनों का समर्थन नहीं कर सकते, तो migration बहुत अधिक कठिन होगा।

हमें केवल एक-के-बाद-दूसरे को आज़माने में सक्षम होना चाहिए, जैसा कि हमने X25519 के साथ किया था, सिद्ध करने के लिए।

## समस्याएं

- Noise Hash चयन - SHA256 के साथ बने रहें या अपग्रेड करें?
  SHA256 अगले 20-30 वर्षों के लिए अच्छा होना चाहिए, PQ द्वारा खतरा नहीं,
  देखें [NIST presentation](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf) और [NCCOE presentation](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf).
  यदि SHA256 टूट जाता है तो हमारे पास बदतर समस्याएं हैं (netdb)।
- NTCP2 अलग पोर्ट, अलग router पता
- SSU2 relay / peer test
- SSU2 संस्करण फील्ड
- SSU2 router पता संस्करण

## संदर्भ

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

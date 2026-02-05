---
title: "सामान्य संरचना विनिर्देश"
description: "सभी I2P protocols में सामान्य डेटा प्रकार"
slug: "common-structures"
category: "डिज़ाइन"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

यह दस्तावेज़ सभी I2P प्रोटोकॉल में सामान्य कुछ डेटा प्रकारों का वर्णन करता है, जैसे [I2NP](/docs/specs/i2np/), [I2CP](/docs/specs/i2cp/), [SSU](/docs/legacy/ssu/), आदि।

## सामान्य प्रकार विनिर्देश

### पूर्णांक

#### विवरण

एक गैर-नकारात्मक पूर्णांक का प्रतिनिधित्व करता है।

#### सामग्री

नेटवर्क बाइट ऑर्डर (बिग एंडियन) में 1 से 8 बाइट्स जो एक अहस्ताक्षरित पूर्णांक का प्रतिनिधित्व करते हैं।

### दिनांक

#### विवरण

GMT टाइमज़ोन में 1 जनवरी, 1970 की मध्यरात्रि से मिलीसेकंड की संख्या। यदि यह संख्या 0 है, तो दिनांक अपरिभाषित या null है।

#### सामग्री

8 byte [Integer](#integer)

### स्ट्रिंग

#### विवरण

एक UTF-8 एन्कोडेड स्ट्रिंग को दर्शाता है।

#### विषय-सूची

1 या अधिक बाइट्स जहाँ पहला बाइट string में बाइट्स की संख्या है (characters की नहीं!) और शेष 0-255 बाइट्स non-null terminated UTF-8 encoded character array हैं। लंबाई की सीमा 255 बाइट्स है (characters की नहीं)। लंबाई 0 हो सकती है।

### PublicKey

#### विवरण

यह संरचना ElGamal या अन्य asymmetric encryption में उपयोग की जाती है, जो केवल exponent का प्रतिनिधित्व करती है, primes का नहीं, जो स्थिर हैं और cryptography specification [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) में परिभाषित हैं। अन्य encryption schemes परिभाषित किए जाने की प्रक्रिया में हैं, नीचे दी गई तालिका देखें।

#### विषय-सूची

Key का प्रकार और लंबाई संदर्भ से समझे जाते हैं या Destination या RouterInfo के Key Certificate में निर्दिष्ट होते हैं, या [LeaseSet2](#leaseset2) या अन्य डेटा संरचना के फील्ड में होते हैं। डिफ़ॉल्ट प्रकार ElGamal है। रिलीज़ 0.9.38 के अनुसार, संदर्भ के आधार पर अन्य प्रकार भी समर्थित हो सकते हैं। अन्यथा उल्लेख न हो तो Keys big-endian होती हैं।

X25519 keys को Destinations और LeaseSet2 में release 0.9.44 से समर्थन प्राप्त है। X25519 keys को RouterIdentities में release 0.9.48 से समर्थन प्राप्त है।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">800</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1184</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1088</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PublicKey.html

### PrivateKey

#### विवरण

यह संरचना ElGamal या अन्य असममित डिक्रिप्शन में उपयोग की जाती है, जो केवल घातांक (exponent) का प्रतिनिधित्व करती है, न कि प्राइम्स का जो स्थिर होते हैं और क्रिप्टोग्राफी विनिर्देश [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) में परिभाषित हैं। अन्य एन्क्रिप्शन स्कीम परिभाषित किए जाने की प्रक्रिया में हैं, नीचे दी गई तालिका देखें।

#### विषय-सूची

Key प्रकार और लंबाई को context से समझा जाता है या डेटा संरचना या private key फ़ाइल में अलग से संग्रहीत किया जाता है। डिफ़ॉल्ट प्रकार ElGamal है। रिलीज़ 0.9.38 के बाद से, context के आधार पर अन्य प्रकार भी समर्थित हो सकते हैं। Keys big-endian हैं जब तक कि अन्यथा उल्लेख न किया गया हो।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1632</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2400</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3168</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PrivateKey.html

### SessionKey

#### विवरण

यह संरचना समरूप AES256 एन्क्रिप्शन और डिक्रिप्शन के लिए उपयोग की जाती है।

#### सामग्री

32 बाइट्स

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### SigningPublicKey

#### विवरण

यह संरचना signatures को सत्यापित करने के लिए उपयोग की जाती है।

#### विषय-सूची

Key का प्रकार और लंबाई संदर्भ से निकाली जाती है या Destination के Key Certificate में निर्दिष्ट होती है। डिफ़ॉल्ट प्रकार DSA_SHA1 है। रिलीज़ 0.9.12 के बाद से, संदर्भ के आधार पर अन्य प्रकार भी समर्थित हो सकते हैं।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### टिप्पणियाँ

* जब एक key दो elements से बनी होती है (उदाहरण के लिए points X,Y), तो इसे serialize करने के लिए प्रत्येक element को length/2 तक पैड किया जाता है, यदि आवश्यक हो तो leading zeros के साथ।

* सभी प्रकार Big Endian हैं, EdDSA और RedDSA को छोड़कर, जो Little Endian प्रारूप में संग्रहीत और प्रेषित किए जाते हैं।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### विवरण

यह संरचना signatures बनाने के लिए उपयोग की जाती है।

#### सामग्री

Key type और length बनाते समय निर्दिष्ट की जाती है। डिफ़ॉल्ट type DSA_SHA1 है। रिलीज़ 0.9.12 से, अन्य types भी समर्थित हो सकते हैं, context के आधार पर।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### नोट्स

* जब कोई key दो elements से मिलकर बनी हो (उदाहरण के लिए points X,Y), तो इसे serialize करने के लिए प्रत्येक element को length/2 तक leading zeros के साथ pad किया जाता है यदि आवश्यक हो।

* सभी प्रकार Big Endian हैं, EdDSA और RedDSA को छोड़कर, जो Little Endian प्रारूप में संग्रहीत और प्रसारित किए जाते हैं।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### हस्ताक्षर

#### विवरण

यह संरचना किसी डेटा के हस्ताक्षर को दर्शाती है।

#### सामग्री

Signature प्रकार और लंबाई का अनुमान उपयोग की गई key के प्रकार से लगाया जाता है। डिफ़ॉल्ट प्रकार DSA_SHA1 है। रिलीज़ 0.9.12 के अनुसार, संदर्भ के आधार पर अन्य प्रकार समर्थित हो सकते हैं।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### टिप्पणियां

* जब एक signature दो elements से बना होता है (उदाहरण के लिए values R,S), तो इसे serialize करने के लिए प्रत्येक element को length/2 तक pad किया जाता है और यदि आवश्यक हो तो leading zeros के साथ।

* सभी प्रकार Big Endian हैं, EdDSA और RedDSA को छोड़कर, जो Little Endian format में संग्रहीत और प्रसारित किए जाते हैं।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### हैश

#### विवरण

कुछ डेटा का SHA256 प्रतिनिधित्व करता है।

#### सामग्री

32 बाइट्स

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### सेशन टैग

नोट: ECIES-X25519 destinations (ratchet) और ECIES-X25519 routers के लिए Session Tags 8 bytes के होते हैं। देखें [ECIES](/docs/specs/ecies/) और [ECIES-ROUTERS](/docs/specs/ecies-routers/)।

#### विवरण

एक यादृच्छिक संख्या

#### विषय सूची

32 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### विवरण

एक identifier परिभाषित करता है जो tunnel में प्रत्येक router के लिए अद्वितीय होता है। एक Tunnel ID आम तौर पर शून्य से अधिक होता है; विशेष मामलों को छोड़कर शून्य का मान उपयोग न करें।

#### विषय-सूची

4 byte [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### प्रमाणपत्र

#### विवरण

एक certificate विभिन्न रसीदों या proof of works का एक container है जो I2P network में उपयोग किया जाता है।

#### सामग्री

1 byte [Integer](#integer) certificate type को निर्दिष्ट करता है, इसके बाद 2 byte [Integer](#integer) certificate payload का आकार निर्दिष्ट करता है, फिर उतने bytes।

```
+----+----+----+----+----+-/
|type| length  | payload
+----+----+----+----+----+-/

type :: `Integer`
        length -> 1 byte

        case 0 -> NULL
        case 1 -> HASHCASH
        case 2 -> HIDDEN
        case 3 -> SIGNED
        case 4 -> MULTIPLE
        case 5 -> KEY

length :: `Integer`
          length -> 2 bytes

payload :: data
           length -> $length bytes
```
#### नोट्स

* [Router Identities](#routeridentity) के लिए, Certificate हमेशा NULL होता है संस्करण 0.9.15 तक। 0.9.16 से, एक Key Certificate का उपयोग key types को specify करने के लिए किया जाता है। 0.9.48 से, X25519 encryption public key types की अनुमति है। नीचे देखें।

* [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove) के लिए, Certificate हमेशा NULL होता है, वर्तमान में कोई अन्य implemented नहीं हैं।

* [Garlic Messages](/docs/specs/i2np/#msg-garlic) के लिए, Certificate हमेशा NULL होता है, वर्तमान में कोई अन्य implemented नहीं हैं।

* [Destinations](#destination) के लिए, Certificate non-NULL हो सकता है। 0.9.12 के अनुसार, एक Key Certificate का उपयोग signing public key type को निर्दिष्ट करने के लिए किया जा सकता है। नीचे देखें।

* कार्यान्वयनकर्ताओं को सलाह दी जाती है कि वे Certificates में अतिरिक्त डेटा को प्रतिबंधित करें।
  प्रत्येक certificate प्रकार के लिए उपयुक्त लंबाई को लागू किया जाना चाहिए।

#### प्रमाणपत्र के प्रकार

निम्नलिखित certificate प्रकार परिभाषित हैं:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HashCash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains an ASCII colon-separated hashcash string.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Hidden</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Hidden routers generally do not announce that they are hidden.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signed</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40 or 72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">43 or 75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains a 40-byte DSA signature, optionally followed by the 32-byte Hash of the signing Destination.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Multiple</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains multiple certificates.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Since 0.9.12. See below for details.</td>
    </tr>
  </tbody>
</table>
#### की प्रमाणपत्र

Key certificates रिलीज़ 0.9.12 में शुरू किए गए थे। उस रिलीज़ से पहले, सभी PublicKeys 256-byte ElGamal keys थीं, और सभी SigningPublicKeys 128-byte DSA-SHA1 keys थीं। एक key certificate Destination या RouterIdentity में PublicKey और SigningPublicKey के प्रकार को दर्शाने के लिए एक तंत्र प्रदान करता है, और मानक लंबाई से अधिक किसी भी key data को पैकेज करने के लिए।

Certificate से पहले बिल्कुल 384 bytes बनाए रखकर, और किसी भी अतिरिक्त key data को certificate के अंदर रखकर, हम उस सभी software के लिए compatibility बनाए रखते हैं जो Destinations और Router Identities को parse करता है।

key certificate payload में निम्नलिखित होता है:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signing Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Crypto Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Signing Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Crypto Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
  </tbody>
</table>
चेतावनी: कुंजी प्रकार का क्रम आपकी अपेक्षा के विपरीत है; Signing Public Key Type पहले आता है।

परिभाषित Signing Public Key प्रकार हैं:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only; never used for Router Identities</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">13</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">14</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
परिभाषित Crypto Public Key प्रकार हैं:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies/">ECIES</a> and proposal 156</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (NONE)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">255</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
जब Key Certificate मौजूद नहीं होता है, तो Destination या RouterIdentity में पूर्ववर्ती 384 bytes को 256-byte ElGamal PublicKey के बाद 128-byte DSA-SHA1 SigningPublicKey के रूप में परिभाषित किया जाता है। जब Key Certificate मौजूद होता है, तो पूर्ववर्ती 384 bytes को निम्नानुसार पुनः परिभाषित किया जाता है:

* Crypto Public Key का पूर्ण या प्रथम भाग

* यादृच्छिक पैडिंग यदि दो keys की कुल लंबाई 384 bytes से कम है

* Signing Public Key का पूरा या पहला हिस्सा

Crypto Public Key की शुरुआत में संरेखण होता है और Signing Public Key का संरेखण अंत में होता है। padding (यदि कोई है) बीच में होती है। certificates में प्रारंभिक key data, padding, और अतिरिक्त key data भागों की लंबाई और सीमाएं स्पष्ट रूप से निर्दिष्ट नहीं हैं, बल्कि निर्दिष्ट key types की लंबाई से प्राप्त होती हैं। यदि Crypto और Signing Public Keys की कुल लंबाई 384 bytes से अधिक है, तो शेष भाग Key Certificate में समाहित होगा। यदि Crypto Public Key की लंबाई 256 bytes नहीं है, तो दोनों keys के बीच सीमा निर्धारित करने की विधि इस दस्तावेज़ के भविष्य के संशोधन में निर्दिष्ट की जाएगी।

ElGamal Crypto Public Key और संकेतित Signing Public Key प्रकार का उपयोग करते हुए उदाहरण लेआउट:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Signing Key Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Excess Signing Key Data in Cert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Certificate.html

#### नोट्स

* कार्यान्वयनकर्ताओं को Key Certificates में अतिरिक्त डेटा को प्रतिबंधित करने की सलाह दी जाती है।
  प्रत्येक certificate प्रकार के लिए उपयुक्त लंबाई को लागू किया जाना चाहिए।

* एक KEY certificate जिसमें types 0,0 (ElGamal,DSA_SHA1) है, वह अनुमतित है लेकिन हतोत्साहित है।
  यह अच्छी तरह से परीक्षित नहीं है और कुछ implementations में समस्याएं पैदा कर सकता है।
  (ElGamal,DSA_SHA1) Destination या RouterIdentity के canonical representation में
  एक NULL certificate का उपयोग करें, जो KEY certificate का उपयोग करने से
  4 bytes छोटा होगा।

### मैपिंग

#### विवरण

key/value मैपिंग या गुणों का एक सेट

#### सामग्री

एक 2-बाइट साइज़ Integer के बाद String=String; जोड़ों की एक श्रृंखला।

चेतावनी: Mapping के अधिकांश उपयोग signed structures में होते हैं, जहाँ Mapping entries को key के अनुसार क्रमबद्ध करना आवश्यक है, ताकि signature अपरिवर्तनीय रहे। key के अनुसार क्रमबद्ध करने में विफलता से signature failures हो सकती हैं!

```
+----+----+----+----+----+----+----+----+
|  size   | key_string (len + data)| =  |
+----+----+----+----+----+----+----+----+
| val_string (len + data)     | ;  | ...
+----+----+----+----+----+----+----+
size :: `Integer`
        length -> 2 bytes
        Total number of bytes that follow

key_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

= :: A single byte containing '='

val_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

; :: A single byte containing ';'
```
#### नोट्स

* एन्कोडिंग अनुकूलित नहीं है - हमें या तो '=' और ';' वर्ण चाहिए, या
  स्ट्रिंग की लंबाई चाहिए, लेकिन दोनों नहीं

* कुछ दस्तावेज़ कहते हैं कि strings में '=' या ';' शामिल नहीं हो सकते हैं लेकिन यह encoding उन्हें support करती है

* स्ट्रिंग्स को UTF-8 के रूप में परिभाषित किया गया है लेकिन वर्तमान implementation में, I2CP UTF-8 का उपयोग करता है परंतु I2NP नहीं करता। उदाहरण के लिए, I2NP Database Store Message में RouterInfo options mapping की UTF-8 स्ट्रिंग्स दूषित हो जाएंगी।

* एन्कोडिंग डुप्लिकेट कीज़ की अनुमति देती है, हालांकि किसी भी उपयोग में जहां मैपिंग साइन की गई है, डुप्लिकेट्स एक सिग्नेचर फेलियर का कारण बन सकते हैं।

* I2NP संदेशों में निहित मैपिंग (जैसे RouterAddress या RouterInfo में)
  को key के अनुसार क्रमबद्ध होना चाहिए ताकि signature अपरिवर्तनीय हो। डुप्लिकेट keys
  की अनुमति नहीं है।

* [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig) में निहित mappings को key के अनुसार क्रमबद्ध होना चाहिए ताकि signature अपरिवर्तनीय रहे। डुप्लिकेट keys की अनुमति नहीं है।

* sort method Java String.compareTo() के समान परिभाषित है, जो characters के Unicode मान का उपयोग करती है।

* यद्यपि यह एप्लिकेशन पर निर्भर है, keys और values आम तौर पर case-sensitive होती हैं।

* Key और value string की लंबाई की सीमा प्रत्येक 255 bytes (characters नहीं) है, साथ में
  length byte। Length byte 0 हो सकता है।

* कुल लंबाई सीमा 65535 bytes है, साथ ही 2 byte size field, या कुल 65537।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## सामान्य संरचना विनिर्देश

### KeysAndCert

#### विवरण

एक एन्क्रिप्शन पब्लिक की, एक साइनिंग पब्लिक की, और एक सर्टिफिकेट, जो RouterIdentity या Destination के रूप में उपयोग किया जाता है।

#### सामग्री

एक [PublicKey](#publickey) के बाद एक [SigningPublicKey](#signingpublickey) और फिर एक [Certificate](#certificate)।

```
+----+----+----+----+----+----+----+----+
| public_key                            |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| padding (optional)                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| certificate                           |
+----+----+----+-/

public_key :: `PublicKey` (partial or full)
              length -> 256 bytes or as specified in key certificate

padding :: random data
           length -> 0 bytes or as specified in key certificate
           public_key length + padding length + signing_key length == 384 bytes

signing__key :: `SigningPublicKey` (partial or full)
                length -> 128 bytes or as specified in key certificate

certificate :: `Certificate`
               length -> >= 3 bytes

total length: 387+ bytes
```
#### पैडिंग जेनरेशन दिशा-निर्देश

ये दिशानिर्देश Proposal 161 में प्रस्तावित किए गए थे और API version 0.9.57 में लागू किए गए थे। ये दिशानिर्देश 0.6 (2005) के बाद से सभी versions के साथ backward-compatible हैं। पृष्ठभूमि और अधिक जानकारी के लिए Proposal 161 देखें।

ElGamal + DSA-SHA1 के अलावा वर्तमान में उपयोग किए जाने वाले key types के किसी भी संयोजन के लिए, padding मौजूद होगा। इसके अतिरिक्त, destinations के लिए, 256-byte public key field संस्करण 0.6 (2005) के बाद से अप्रयुक्त रहा है।

डेवलपर्स को Destination public keys, और Destination और Router Identity padding के लिए रैंडम डेटा इस तरह जेनरेट करना चाहिए कि यह विभिन्न I2P प्रोटोकॉल में कंप्रेसिबल हो जबकि अभी भी सुरक्षित रहे, और बिना Base 64 प्रतिनिधित्व को दूषित या असुरक्षित दिखाए। यह किसी भी विघटनकारी प्रोटोकॉल परिवर्तन के बिना padding फील्ड हटाने के अधिकांश लाभ प्रदान करता है।

सख्ती से कहें तो, केवल 32-बाइट signing public key (Destinations और Router Identities दोनों में) और 32-बाइट encryption public key (केवल Router Identities में) एक random number है जो इन structures के SHA-256 hashes के लिए आवश्यक सभी entropy प्रदान करता है ताकि वे cryptographically strong हों और network database DHT में randomly distributed हों।

हालांकि, अत्यधिक सावधानी के कारण, हम ElG public key फील्ड और padding में न्यूनतम 32 bytes के random data का उपयोग करने की सिफारिश करते हैं। इसके अतिरिक्त, यदि सभी फील्ड शून्य होते हैं, तो Base 64 destinations में AAAA characters की लंबी श्रृंखला होगी, जो उपयोगकर्ताओं में चिंता या भ्रम का कारण बन सकती है।

32 बाइट्स के random data को आवश्यकतानुसार दोहराएं ताकि पूरा KeysAndCert structure I2P protocols जैसे I2NP Database Store Message, Streaming SYN, SSU2 handshake, और repliable Datagrams में अत्यधिक compressible हो।

उदाहरण:

* X25519 encryption type और Ed25519 signature type के साथ एक Router Identity में random data की 10 प्रतियां (320 bytes) होंगी, जिससे compress करने पर लगभग 288 bytes की बचत होगी।

* Ed25519 signature प्रकार वाले Destination में
  random data की 11 प्रतियां (352 bytes) होंगी, जो compress करने पर लगभग 320 bytes की बचत देगी।

कार्यान्वयन (Implementations) को निश्चित रूप से पूरी 387+ बाइट संरचना को स्टोर करना चाहिए क्योंकि संरचना का SHA-256 हैश पूरी सामग्री को कवर करता है।

#### नोट्स

* यह मत मानिए कि ये हमेशा 387 bytes होते हैं! ये 387 bytes हैं प्लस certificate length जो bytes 385-386 पर निर्दिष्ट है, जो non-zero हो सकती है।

* रिलीज़ 0.9.12 के अनुसार, यदि सर्टिफिकेट एक Key Certificate है, तो key फ़ील्ड्स की सीमाएं भिन्न हो सकती हैं। विवरण के लिए ऊपर Key Certificate अनुभाग देखें।

* Crypto Public Key शुरुआत में aligned होती है और Signing Public Key अंत में aligned होती है। Padding (यदि कोई है) बीच में होती है।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### विवरण

एक विशिष्ट router को विशिष्ट रूप से पहचानने का तरीका परिभाषित करता है

#### विषय-सूची

KeysAndCert के समान।

padding field के लिए random data generate करने के guidelines के लिए [KeysAndCert](#keysandcert) देखें।

#### नोट्स

* RouterIdentity के लिए certificate हमेशा NULL था रिलीज़ 0.9.12 तक।

* यह मान न लें कि ये हमेशा 387 bytes होते हैं! ये 387 bytes प्लस certificate की लंबाई होते हैं जो bytes 385-386 पर निर्दिष्ट होती है, जो शून्य से अधिक हो सकती है।

* रिलीज 0.9.12 के अनुसार, यदि certificate एक Key Certificate है, तो key fields की सीमाएं भिन्न हो सकती हैं। विवरण के लिए ऊपर Key Certificate अनुभाग देखें।

* Crypto Public Key शुरुआत में aligned है और Signing Public Key अंत में aligned है। padding (यदि कोई है) बीच में है।

* key certificate और ECIES_X25519 public key के साथ RouterIdentities का समर्थन रिलीज़ 0.9.48 से किया जा रहा है।
  इससे पहले, सभी RouterIdentities ElGamal थीं।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### गंतव्य

#### विवरण

एक Destination एक विशिष्ट endpoint को परिभाषित करता है जिस पर सुरक्षित डिलीवरी के लिए संदेशों को भेजा जा सकता है।

#### विषय-सूची

[KeysAndCert](#keysandcert) के समान, सिवाय इसके कि public key का कभी उपयोग नहीं होता, और इसमें वैध ElGamal Public Key के बजाय random data हो सकता है।

Public key और padding fields के लिए random data generate करने के दिशानिर्देशों के लिए [KeysAndCert](#keysandcert) देखें।

#### नोट्स

* गंतव्य की public key का उपयोग पुराने i2cp-to-i2cp
  एन्क्रिप्शन के लिए किया जाता था जो संस्करण 0.6 (2005) में अक्षम कर दिया गया था, यह वर्तमान में अप्रयुक्त है सिवाय
  LeaseSet एन्क्रिप्शन के लिए IV के, जो deprecated है। इसके बजाय
  LeaseSet में public key का उपयोग किया जाता है।

* यह मत मानिए कि ये हमेशा 387 bytes होते हैं! ये 387 bytes होते हैं प्लस certificate length जो bytes 385-386 पर निर्दिष्ट होती है, जो non-zero हो सकती है।

* रिलीज़ 0.9.12 के अनुसार, यदि certificate एक Key Certificate है, तो key fields की boundaries अलग हो सकती हैं। विवरण के लिए ऊपर Key Certificate सेक्शन देखें।

* Crypto Public Key की शुरुआत में संरेखित किया गया है और Signing Public Key अंत में संरेखित की गई है। Padding (यदि कोई हो) बीच में है।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### विवरण

एक विशिष्ट tunnel के लिए [Destination](#destination) को लक्षित संदेशों को प्राप्त करने की प्राधिकरण को परिभाषित करता है।

#### सामग्री

Gateway router की [RouterIdentity](#routeridentity) का SHA256 [Hash](#hash), फिर [TunnelId](#tunnelid), और अंत में समाप्ति [Date](#date)।

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date
+----+----+----+----+----+----+----+----+
                    |
+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: `Date`
            length -> 8 bytes
```
#### नोट्स

* कुल आकार: 44 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### विवरण

किसी विशेष [Destination](#destination) के लिए वर्तमान में अधिकृत सभी [Leases](#lease) को शामिल करता है, [PublicKey](#publickey) जिससे garlic messages को एन्क्रिप्ट किया जा सकता है, और फिर [SigningPublicKey](#signingpublickey) जिसका उपयोग इस संरचना के विशेष संस्करण को रद्द करने के लिए किया जा सकता है। LeaseSet network database में संग्रहीत दो संरचनाओं में से एक है (दूसरी [RouterInfo](#routerinfo) है), और इसकी key शामिल [Destination](#destination) के SHA256 के तहत है।

#### विषय-सूची

[Destination](#destination), जिसके बाद एन्क्रिप्शन के लिए एक [PublicKey](#publickey), फिर एक [SigningPublicKey](#signingpublickey) जो इस LeaseSet के संस्करण को रद्द करने के लिए उपयोग किया जा सकता है, फिर एक 1 बाइट [Integer](#integer) जो निर्दिष्ट करता है कि सेट में कितनी [Lease](#lease) संरचनाएं हैं, इसके बाद वास्तविक [Lease](#lease) संरचनाएं और अंत में [Destination](#destination) की [SigningPrivateKey](#signingprivatekey) द्वारा हस्ताक्षरित पिछले बाइट्स का एक [Signature](#signature)।

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| encryption_key                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease 0                          |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease 1                               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease ($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

encryption_key :: `PublicKey`
                  length -> 256 bytes

signing_key :: `SigningPublicKey`
               length -> 128 bytes or as specified in destination's key
                         certificate

num :: `Integer`
       length -> 1 byte
       Number of leases to follow
       value: 0 <= num <= 16

leases :: [`Lease`]
          length -> $num*44 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate
```
#### नोट्स

* destination की public key पुराने I2CP-to-I2CP encryption के लिए उपयोग की जाती थी जो version 0.6 में disable कर दिया गया था, वर्तमान में यह unused है।

* एन्क्रिप्शन key का उपयोग end-to-end ElGamal/AES+SessionTag एन्क्रिप्शन के लिए किया जाता है
  [ELGAMAL-AES](/docs/specs/elgamal-aes/)। यह वर्तमान में हर router स्टार्टअप पर नई बनाई जाती है, यह
  स्थायी नहीं है।

* हस्ताक्षर को destination की signing public key का उपयोग करके सत्यापित किया जा सकता है।

* शून्य Leases के साथ एक LeaseSet की अनुमति है लेकिन यह अप्रयुक्त है।
  यह LeaseSet निरसन के लिए अभिप्रेत था, जो अकार्यान्वित है।
  सभी LeaseSet2 variants में कम से कम एक Lease की आवश्यकता होती है।

* signing_key वर्तमान में अप्रयुक्त है। यह leaseSet निरसन के लिए अभिप्रेत था,
  जो अभी तक लागू नहीं किया गया है। यह वर्तमान में हर router
  स्टार्टअप पर नए सिरे से जेनरेट होती है, यह स्थायी नहीं है। signing key प्रकार हमेशा
  destination की signing key के प्रकार के समान होता है।

* सभी Leases की सबसे जल्दी expiration को LeaseSet का timestamp या version माना जाता है। Routers आमतौर पर किसी LeaseSet का store तब तक स्वीकार नहीं करते जब तक कि यह मौजूदा से "नया" न हो। नया LeaseSet प्रकाशित करते समय सावधान रहें जहां सबसे पुराना Lease पिछले LeaseSet के सबसे पुराने Lease के समान हो। ऐसी स्थिति में प्रकाशन करने वाले router को आमतौर पर सबसे पुराने Lease की expiration को कम से कम 1 ms बढ़ाना चाहिए।

* रिलीज़ 0.9.7 से पहले, जब originating router द्वारा भेजे गए DatabaseStore Message में शामिल किया जाता था, तो router सभी published leases की समाप्ति को समान मान पर सेट करता था, जो सबसे पहले समाप्त होने वाली lease का था। रिलीज़ 0.9.7 के बाद से, router प्रत्येक lease के लिए वास्तविक lease expiration को publish करता है। यह एक implementation detail है और structures specification का हिस्सा नहीं है।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### विवरण

किसी विशेष tunnel के लिए [Destination](#destination) को लक्षित संदेशों को प्राप्त करने की प्राधिकरण को परिभाषित करता है। [Lease](#lease) के समान लेकिन 4-byte end_date के साथ। [LeaseSet2](#leaseset2) द्वारा उपयोग किया जाता है। 0.9.38 से समर्थित है; अधिक जानकारी के लिए proposal 123 देखें।

#### सामग्री

gateway router के [RouterIdentity](#routeridentity) का SHA256 [Hash](#hash), फिर [TunnelId](#tunnelid), और अंत में 4 byte का end date।

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### टिप्पणियाँ

* कुल आकार: 40 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### विवरण

यह [LeaseSet2Header](#leaseset2header) का एक वैकल्पिक भाग है। streaming और I2CP में भी उपयोग किया जाता है। 0.9.38 से समर्थित है; अधिक जानकारी के लिए proposal 123 देखें।

#### विषयसूची

इसमें एक समाप्ति तिथि, एक sigtype और अस्थायी [SigningPublicKey](#signingpublickey), और एक [Signature](#signature) शामिल है।

```
+----+----+----+----+----+----+----+----+
|     expires       | sigtype |         |
+----+----+----+----+----+----+         +
|       transient_public_key            |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|           signature                   |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

expires :: 4 byte date
           length -> 4 bytes
           Seconds since the epoch, rolls over in 2106.

sigtype :: 2 byte type of the transient_public_key
           length -> 2 bytes

transient_public_key :: `SigningPublicKey`
                        length -> As inferred from the sigtype

signature :: `Signature`
             length -> As inferred from the sigtype of the signing public key
                       in the `Destination` that preceded this offline signature.
             Signature of expires timestamp, transient sig type, and public key,
             by the destination public key.

```
#### नोट्स

* यह सेक्शन ऑफलाइन जेनरेट किया जा सकता है, और किया जाना चाहिए।

### LeaseSet2Header

#### विवरण

यह [LeaseSet2](#leaseset2) और [MetaLeaseSet](#metaleaseset) का सामान्य भाग है। 0.9.38 से समर्थित; अधिक जानकारी के लिए प्रस्ताव 123 देखें।

#### विषय-सूची

[Destination](#destination), दो timestamps, और एक वैकल्पिक [OfflineSignature](#offlinesignature) शामिल करता है।

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one, unless bit 2 is set.
  Bit 2: If 0, a standard published leaseset.
         If 1, this unencrypted leaseset will be blinded and encrypted when published.
         If this leaseset expires, query the blinded location in the netdb for a new one.
         If this bit is set to 1, set bit 1 to 1 also.
         As of release 0.9.42.
  Bits 15-3: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

```
#### टिप्पणियां

* कुल आकार: न्यूनतम 395 बाइट्स

* वास्तविक समाप्ति समय अधिकतम [LeaseSet2](#leaseset2) के लिए लगभग 660 (11 मिनट) और [MetaLeaseSet](#metaleaseset) के लिए 65535 (पूर्ण 18.2 घंटे) है।

* [LeaseSet](#leaseset) (1) में 'published' फील्ड नहीं था, इसलिए versioning के लिए 
  सबसे पुराने lease की खोज करनी पड़ती थी। LeaseSet2 एक सेकंड के resolution के साथ 
  'published' फील्ड जोड़ता है। Routers को floodfills को नए leasesets भेजने की दर को 
  प्रति सेकंड एक बार से बहुत धीमी गति (प्रति destination) तक सीमित करना चाहिए।
  यदि यह implemented नहीं है, तो code को यह सुनिश्चित करना होगा कि हर नए leaseset 
  का 'published' समय पहले वाले से कम से कम एक सेकंड बाद का हो, वरना 
  floodfills नए leaseset को store या flood नहीं करेंगे।

### LeaseSet2

#### विवरण

I2NP DatabaseStore संदेश के प्रकार 3 में शामिل। 0.9.38 से समर्थित; अधिक जानकारी के लिए प्रस्ताव 123 देखें।

किसी विशेष [Destination](#destination) के लिए वर्तमान में अधिकृत सभी [Lease2](#lease2) और [PublicKey](#publickey) को शामिल करता है जिसमें garlic messages को encrypt किया जा सकता है। LeaseSet network database में संग्रहीत दो structures में से एक है (दूसरा [RouterInfo](#routerinfo) है), और यह निहित [Destination](#destination) के SHA256 के तहत keyed है।

#### सामग्री

[LeaseSet2Header](#leaseset2header), के बाद विकल्प, फिर एक या अधिक [PublicKey](#publickey) एन्क्रिप्शन के लिए, [Integer](#integer) जो निर्दिष्ट करता है कि सेट में कितने [Lease2](#lease2) संरचनाएं हैं, के बाद वास्तविक [Lease2](#lease2) संरचनाएं और अंत में पिछले बाइट्स का [Signature](#signature) जो [Destination](#destination) की [SigningPrivateKey](#signingprivatekey) या transient key द्वारा हस्ताक्षरित है।

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numk| keytype0| keylen0 |              |
+----+----+----+----+----+              +
|          encryption_key_0             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| keytypen| keylenn |                   |
+----+----+----+----+                   +
|          encryption_key_n             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease2 0                         |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease2($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

numk :: `Integer`
        length -> 1 byte
        Number of key types, key lengths, and `PublicKey`s to follow
        value: 1 <= numk <= max TBD

keytype :: The encryption type of the `PublicKey` to follow.
           length -> 2 bytes

keylen :: The length of the `PublicKey` to follow.
          Must match the specified length of the encryption type.
          length -> 2 bytes

encryption_key :: `PublicKey`
                  length -> keylen bytes

num :: `Integer`
       length -> 1 byte
       Number of `Lease2`s to follow
       value: 0 <= num <= 16

leases :: [`Lease2`]
          length -> $num*40 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### एन्क्रिप्शन की प्राथमिकता

प्रकाशित (server) leaseSets के लिए, encryption keys server की प्राथमिकता के क्रम में होती हैं, सबसे प्राथमिक पहले। यदि clients एक से अधिक encryption प्रकार का समर्थन करते हैं, तो यह अनुशंसा की जाती है कि वे server की प्राथमिकता का सम्मान करें और server से कनेक्ट करने के लिए encryption विधि के रूप में पहले समर्थित प्रकार का चयन करें। आम तौर पर, नए (उच्च-संख्या वाले) key प्रकार अधिक सुरक्षित या कुशल होते हैं और प्राथमिक होते हैं, इसलिए keys को key प्रकार के विपरीत क्रम में सूचीबद्ध किया जाना चाहिए।

हालांकि, clients अपनी पसंद के आधार पर implementation-dependent तरीके से चुन सकते हैं, या "संयुक्त" पसंद निर्धारित करने के लिए कोई विधि उपयोग कर सकते हैं। यह एक configuration विकल्प के रूप में या debugging के लिए उपयोगी हो सकता है।

अप्रकाशित (client) leaseSets में key का क्रम प्रभावी रूप से महत्वपूर्ण नहीं है, क्योंकि आमतौर पर अप्रकाशित clients से कनेक्शन का प्रयास नहीं किया जाता है। जब तक कि इस क्रम का उपयोग संयुक्त प्राथमिकता निर्धारित करने के लिए न किया जाए, जैसा कि ऊपर वर्णित है।

#### विकल्प

API 0.9.66 के अनुसार, service record options के लिए एक मानक प्रारूप परिभाषित किया गया है। विवरण के लिए proposal 167 देखें। service records के अलावा अन्य options, जो भिन्न प्रारूप का उपयोग करते हैं, भविष्य में परिभाषित किए जा सकते हैं।

LS2 विकल्पों को key के अनुसार क्रमबद्ध होना चाहिए, ताकि signature अपरिवर्तनीय रहे।

सेवा रिकॉर्ड विकल्प निम्नलिखित रूप में परिभाषित हैं:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := वांछित सेवा का प्रतीकात्मक नाम। छोटे अक्षरों में होना चाहिए। उदाहरण: "smtp"।
  अनुमतित वर्ण [a-z0-9-] हैं और '-' से शुरू या समाप्त नहीं होना चाहिए।
  [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) या Linux /etc/services के मानक पहचानकर्ता का उपयोग करना चाहिए यदि वहाँ परिभाषित हैं।
- proto := वांछित सेवा का परिवहन प्रोटोकॉल। छोटे अक्षरों में होना चाहिए, या तो "tcp" या "udp"।
  "tcp" का अर्थ streaming है और "udp" का अर्थ repliable datagrams है।
  Raw datagrams और datagram2 के लिए प्रोटोकॉल संकेतक बाद में परिभाषित हो सकते हैं।
  अनुमतित वर्ण [a-z0-9-] हैं और '-' से शुरू या समाप्त नहीं होना चाहिए।
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := time to live, पूर्णांक सेकंड। धनात्मक पूर्णांक। उदाहरण: "86400"।
  न्यूनतम 86400 (एक दिन) की सिफारिश की जाती है, विवरण के लिए नीचे सिफारिशें अनुभाग देखें।
- priority := लक्षित होस्ट की प्राथमिकता, कम मान का अर्थ अधिक पसंदीदा है। गैर-नकारात्मक पूर्णांक। उदाहरण: "0"
  केवल तभी उपयोगी है जब एक से अधिक रिकॉर्ड हों, लेकिन केवल एक रिकॉर्ड होने पर भी आवश्यक है।
- weight := समान प्राथमिकता वाले रिकॉर्ड के लिए सापेक्षिक भार। उच्च मान का अर्थ चुने जाने की अधिक संभावना है। गैर-नकारात्मक पूर्णांक। उदाहरण: "0"
  केवल तभी उपयोगी है जब एक से अधिक रिकॉर्ड हों, लेकिन केवल एक रिकॉर्ड होने पर भी आवश्यक है।
- port := I2CP पोर्ट जिस पर सेवा मिलनी है। गैर-नकारात्मक पूर्णांक। उदाहरण: "25"
  पोर्ट 0 समर्थित है लेकिन अनुशंसित नहीं है।
- target := सेवा प्रदान करने वाले गंतव्य का hostname या b32। [NAMING](/docs/overview/naming/) में दिए गए अनुसार एक वैध hostname। छोटे अक्षरों में होना चाहिए।
  उदाहरण: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" या "example.i2p"।
  b32 की सिफारिश की जाती है जब तक कि hostname "प्रसिद्ध" न हो, यानी आधिकारिक या डिफ़ॉल्ट पता पुस्तकों में।
- appoptions := एप्लिकेशन के लिए विशिष्ट मनमाना पाठ, इसमें " " या "," नहीं होना चाहिए। एन्कोडिंग UTF-8 है।

उदाहरण:

LS2 में aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p के लिए, एक SMTP सर्वर की ओर इंगित करते हुए:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

LS2 में aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p के लिए, दो SMTP सर्वर की ओर इशारा करते हुए:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

LS2 में bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p के लिए, खुद को एक SMTP सर्वर के रूप में इंगित करते हुए:

"_smtp._tcp" "0 999999 25"

#### नोट्स

* destination की public key का उपयोग पुराने I2CP-to-I2CP encryption के लिए किया जाता था जो version 0.6 में disable कर दिया गया था, यह वर्तमान में अप्रयुक्त है।

* एन्क्रिप्शन keys का उपयोग end-to-end ElGamal/AES+SessionTag encryption
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (type 0) या अन्य end-to-end encryption schemes के लिए किया जाता है।
  देखें [ECIES](/docs/specs/ecies/) और proposals 145 और 156।
  ये हर router startup पर नई generate की जा सकती हैं
  या ये persistent हो सकती हैं।
  X25519 (type 4, देखें [ECIES](/docs/specs/ecies/)) release 0.9.44 से supported है।

* हस्ताक्षर उपरोक्त डेटा पर है, जो DatabaseStore प्रकार (3) वाले एकल बाइट के साथ PREPENDED है।

* हस्ताक्षर को गंतव्य की signing public key का उपयोग करके सत्यापित किया जा सकता है, या transient signing public key का उपयोग करके, यदि leaseset2 header में एक offline signature शामिल है।

* प्रत्येक key के लिए key length प्रदान की जाती है, ताकि floodfills और clients संरचना को parse कर सकें भले ही सभी encryption प्रकार ज्ञात या समर्थित न हों।

* [LeaseSet2Header](#leaseset2header) में 'published' फील्ड पर नोट देखें

* options mapping, यदि size एक से अधिक है, तो key द्वारा क्रमबद्ध होना चाहिए, ताकि signature अपरिवर्तनीय रहे।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### विवरण

एक विशिष्ट tunnel के लिए [Destination](#destination) को लक्षित संदेशों को प्राप्त करने की प्राधिकरण को परिभाषित करता है। [Lease2](#lease2) के समान लेकिन tunnel id के बजाय flags और cost के साथ। [MetaLeaseSet](#metaleaseset) द्वारा उपयोग किया जाता है। प्रकार 7 के I2NP DatabaseStore संदेश में निहित। 0.9.38 से समर्थित; अधिक जानकारी के लिए proposal 123 देखें।

#### सामग्री

गेटवे router के [RouterIdentity](#routeridentity) का SHA256 [Hash](#hash), फिर flags और cost, और अंत में 4 byte का end date।

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|    flags     |cost|      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway,
             or the hash of another `MetaLeaseSet`.
             length -> 32 bytes

flags :: 3 bytes of flags
         Bit order: 23 22 ... 3 2 1 0
         Bits 3-0: Type of the entry.
         If 0, unknown.
         If 1, a `LeaseSet`.
         If 3, a `LeaseSet2`.
         If 5, a `MetaLeaseSet`.
         Bits 23-4: set to 0 for compatibility with future uses
         length -> 3 bytes

cost :: 1 byte, 0-255. Lower value is higher priority.
        length -> 1 byte

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### नोट्स

* कुल आकार: 40 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### विवरण

टाइप 7 के I2NP DatabaseStore संदेश में निहित। 0.9.38 के रूप में परिभाषित; 0.9.40 के रूप में कार्य करने के लिए निर्धारित; अधिक जानकारी के लिए प्रस्ताव 123 देखें।

एक विशेष [Destination](#destination) के लिए वर्तमान में अधिकृत सभी [MetaLease](#metalease) और [PublicKey](#publickey) को शामिल करता है जिससे garlic messages को एन्क्रिप्ट किया जा सकता है। LeaseSet network database में संग्रहीत दो संरचनाओं में से एक है (दूसरी [RouterInfo](#routerinfo) है), और यह शामिल [Destination](#destination) के SHA256 के तहत keyed है।

#### विषय-सूची

[LeaseSet2Header](#leaseset2header), उसके बाद एक options, [Integer](#integer) जो यह निर्दिष्ट करता है कि set में कितने [Lease2](#lease2) structures हैं, उसके बाद वास्तविक [Lease2](#lease2) structures और अंत में पिछले bytes का एक [Signature](#signature) जो [Destination](#destination) की [SigningPrivateKey](#signingprivatekey) या transient key द्वारा sign किया गया है।

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| MetaLease 0                      |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| MetaLease($num-1)                     |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numr|                                  |
+----+                                  +
|          revocation_0                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          revocation_n                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

num :: `Integer`
        length -> 1 byte
        Number of `MetaLease`s to follow
        value: 1 <= num <= max TBD

leases :: `MetaLease`s
          length -> $numr*40 bytes

numr :: `Integer`
        length -> 1 byte
        Number of `Hash`es to follow
        value: 0 <= numr <= max TBD

revocations :: [`Hash`]
               length -> $numr*32 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### नोट्स

* गंतव्य की सार्वजनिक कुंजी पुराने I2CP-to-I2CP एन्क्रिप्शन के लिए उपयोग की जाती थी जो संस्करण 0.6 में अक्षम कर दी गई थी, यह वर्तमान में अप्रयुक्त है।

* हस्ताक्षर उपरोक्त डेटा पर है, जो DatabaseStore प्रकार (7) वाले एकल बाइट के साथ PREPENDED है।

* हस्ताक्षर को destination की signing public key का उपयोग करके सत्यापित किया जा सकता है, या transient signing public key का उपयोग करके, यदि leaseset2 header में offline signature शामिल है।

* [LeaseSet2Header](#leaseset2header) में 'published' फ़ील्ड पर टिप्पणी देखें

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### विवरण

टाइप 5 के I2NP DatabaseStore संदेश में निहित है। 0.9.38 के रूप में परिभाषित; 0.9.39 के रूप में कार्य कर रहा है; अधिक जानकारी के लिए प्रस्ताव 123 देखें।

केवल blinded key और expiration cleartext में दिखाई देते हैं। वास्तविक leaseSet एन्क्रिप्टेड है।

#### सामग्री

दो बाइट signature प्रकार, blinded [SigningPrivateKey](#signingprivatekey), प्रकाशित समय, समाप्ति, और flags। फिर, दो बाइट लंबाई के बाद encrypted डेटा। अंत में, blinded [SigningPrivateKey](#signingprivatekey) या transient key द्वारा हस्ताक्षरित पिछले बाइट्स का एक [Signature](#signature)।

```
+----+----+----+----+----+----+----+----+
| sigtype |                             |
+----+----+                             +
|        blinded_public_key             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  len    |                             |
+----+----+                             +
|         encrypted_data                |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

sigtype :: A two byte signature type of the public key to follow
           length -> 2 bytes

blinded_public_key :: `SigningPublicKey`
                      length -> As inferred from the sigtype

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one.
  Bits 15-2: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

len :: `Integer`
        length -> 2 bytes
        length of encrypted_data to follow
        value: 1 <= num <= max TBD

encrypted_data :: Data encrypted
                  length -> len bytes

signature :: `Signature`
             length -> As specified by the sigtype of the blinded pubic key,
                       or by the sigtype of the transient public key,
                       if present in the header

```
#### नोट्स

* गंतव्य की सार्वजनिक कुंजी पुराने I2CP-to-I2CP एन्क्रिप्शन के लिए उपयोग की जाती थी जो संस्करण 0.6 में निष्क्रिय कर दी गई थी, यह वर्तमान में अप्रयुक्त है।

* signature उपरोक्त डेटा पर है, जो DatabaseStore प्रकार (5) वाले एकल बाइट के साथ PREPENDED है।

* हस्ताक्षर को destination की signing public key का उपयोग करके सत्यापित किया जा सकता है, या transient signing public key का उपयोग करके, यदि leaseset2 header में एक offline signature शामिल है।

* Blinding और encryption [EncryptedLeaseSet](/docs/specs/encryptedleaseset/) में निर्दिष्ट हैं

* यह संरचना [LeaseSet2Header](#leaseset2header) का उपयोग नहीं करती है।

* वास्तविक अधिकतम समाप्ति समय लगभग 660 (11 मिनट) है, जब तक कि यह एक एन्क्रिप्टेड [MetaLeaseSet](#metaleaseset) न हो।

* encrypted leasesets के साथ offline signatures के उपयोग पर टिप्पणियों के लिए proposal 123 देखें।

* [LeaseSet2Header](#leaseset2header) में 'published' फील्ड पर नोट देखें
  (यही समस्या, भले ही हम यहां LeaseSet2Header फॉर्मेट का उपयोग नहीं करते हैं)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### विवरण

यह संरचना transport protocol के माध्यम से router से संपर्क करने के साधनों को परिभाषित करती है।

#### सामग्री

1 byte [Integer](#integer) जो पते का उपयोग करने की सापेक्षिक लागत को परिभाषित करता है, जहाँ 0 मुफ्त है और 255 महंगा है, इसके बाद समाप्ति [Date](#date) आता है जिसके बाद पते का उपयोग नहीं करना चाहिए, या यदि null है, तो पता कभी समाप्त नहीं होता। इसके बाद एक [String](#string) आता है जो transport protocol को परिभाषित करता है जिसका यह router address उपयोग करता है। अंत में एक [Mapping](#mapping) है जिसमें कनेक्शन स्थापित करने के लिए आवश्यक सभी transport विशिष्ट विकल्प होते हैं, जैसे IP address, port number, email address, URL, आदि।

```
+----+----+----+----+----+----+----+----+
|cost|           expiration
+----+----+----+----+----+----+----+----+
     |        transport_style           |
+----+----+----+----+-/-+----+----+----+
|                                       |
+                                       +
|               options                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

cost :: `Integer`
        length -> 1 byte

        case 0 -> free
        case 255 -> expensive

expiration :: `Date` (must be all zeros, see notes below)
              length -> 8 bytes

              case null -> never expires

transport_style :: `String`
                   length -> 1-256 bytes

options :: `Mapping`
```
#### नोट्स

* Cost आमतौर पर SSU के लिए 5 या 6 होता है, और NTCP के लिए 10 या 11 होता है।

* Expiration वर्तमान में अप्रयुक्त है, हमेशा null (सभी शून्य)। रिलीज़ 0.9.3 के अनुसार, expiration को शून्य माना जाता है और संग्रहीत नहीं किया जाता, इसलिए कोई भी गैर-शून्य expiration RouterInfo signature verification में विफल हो जाएगी। Expiration को लागू करना (या इन bytes के लिए कोई अन्य उपयोग) एक backwards-incompatible परिवर्तन होगा। Router इस फील्ड को सभी शून्य पर सेट करना चाहिए। रिलीज़ 0.9.12 के अनुसार, एक गैर-शून्य expiration फील्ड को फिर से पहचाना जाता है, हालांकि हमें इस फील्ड का उपयोग करने के लिए कई रिलीज़ का इंतजार करना होगा, जब तक कि नेटवर्क का विशाल बहुमत इसे नहीं पहचानता।

* निम्नलिखित विकल्प, हालांकि आवश्यक नहीं हैं, मानक हैं और अधिकांश router पतों में मौजूद होने की अपेक्षा की जाती है: "host" (एक IPv4 या IPv6 पता या host नाम) और "port"।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### विवरण

उस सभी डेटा को परिभाषित करता है जिसे एक router नेटवर्क के देखने के लिए प्रकाशित करना चाहता है। [RouterInfo](#routerinfo) network database में संग्रहीत दो संरचनाओं में से एक है (दूसरी [LeaseSet](#leaseset) है), और यह समाहित [RouterIdentity](#routeridentity) के SHA256 के तहत keyed है।

#### सामग्री

[RouterIdentity](#routeridentity) के बाद [Date](#date), जब एंट्री प्रकाशित की गई थी

```
+----+----+----+----+----+----+----+----+
| router_ident                          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| published                             |
+----+----+----+----+----+----+----+----+
|size| RouterAddress 0                  |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress 1                       |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress ($size-1)               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+-/-+----+----+----+
|psiz| options                          |
+----+----+----+----+-/-+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

router_ident :: `RouterIdentity`
                length -> >= 387+ bytes

published :: `Date`
             length -> 8 bytes

size :: `Integer`
        length -> 1 byte
        The number of `RouterAddress`es to follow, 0-255

addresses :: [`RouterAddress`]
             length -> varies

peer_size :: `Integer`
             length -> 1 byte
             The number of peer `Hash`es to follow, 0-255, unused, always zero
             value -> 0

options :: `Mapping`

signature :: `Signature`
             length -> 40 bytes or as specified in router_ident's key
                       certificate
```
#### नोट्स

* peer_size [Integer](#integer) के बाद उतने router hashes की एक सूची हो सकती है।
  यह वर्तमान में अप्रयुक्त है। यह प्रतिबंधित routes के एक रूप के लिए था,
  जो अनुप्रयुक्त है।
  कुछ implementations में सूची को क्रमबद्ध करने की आवश्यकता हो सकती है ताकि signature अपरिवर्तनीय रहे।
  इस सुविधा को सक्षम करने से पहले अनुसंधान किया जाना है।

* हस्ताक्षर को router_ident की signing public key का उपयोग करके सत्यापित किया जा सकता है।

* सभी router info में मौजूद होने वाले मानक विकल्पों के लिए network database पृष्ठ [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) देखें।

* बहुत पुराने router में addresses को उनके data के SHA256 के अनुसार sort करना आवश्यक था
  ताकि signature अपरिवर्तनीय रहे।
  अब यह आवश्यक नहीं है, और backward compatibility के लिए इसे implement करना उचित नहीं है।

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### डिलीवरी निर्देश

Tunnel Message Delivery Instructions को Tunnel Message Specification [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions) में परिभाषित किया गया है।

Garlic Message Delivery Instructions I2NP Message Specification [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions) में परिभाषित हैं।

## संदर्भ

- [ECIES](/docs/specs/ecies/)
- [ECIES-HYBRID](/docs/specs/ecies-hybrid/)
- [ECIES-ROUTERS](/docs/specs/ecies-routers/)
- [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy)
- [ELGAMAL-AES](/docs/specs/elgamal-aes/)
- [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions)
- [I2CP](/docs/specs/i2cp/)
- [I2NP](/docs/specs/i2np/)
- [NAMING](/docs/overview/naming/)
- [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo)
- [Prop134](/proposals/134-gost/)
- [Prop169](/proposals/169-pq-crypto/)
- [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
- [SSU](/docs/legacy/ssu/)
- [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions)

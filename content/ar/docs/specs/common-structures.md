---
title: "مواصفات الهياكل الشائعة"
description: "أنواع البيانات الشائعة في جميع بروتوكولات I2P"
slug: "common-structures"
category: "التصميم"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

تصف هذه الوثيقة بعض أنواع البيانات المشتركة بين جميع بروتوكولات I2P، مثل [I2NP](/docs/specs/i2np/)، [I2CP](/docs/specs/i2cp/)، [SSU](/docs/legacy/ssu/)، إلخ.

## مواصفات النوع الشائع

### عدد صحيح

#### الوصف

يمثل عددًا صحيحًا غير سالب.

#### المحتويات

من 1 إلى 8 بايت بترتيب البايت الشبكي (big endian) تمثل عددًا صحيحًا موجبًا.

### التاريخ

#### الوصف

عدد المللي ثانية منذ منتصف الليل في 1 يناير 1970 في المنطقة الزمنية GMT. إذا كان الرقم 0، فإن التاريخ غير محدد أو فارغ.

#### المحتويات

8 بايت [عدد صحيح](#integer)

### سلسلة نصية

#### الوصف

يمثل سلسلة نصية مُرمزة بـ UTF-8.

#### المحتويات

1 أو أكثر من البايتات حيث البايت الأول هو عدد البايتات (وليس الأحرف!) في النص والبايتات المتبقية من 0-255 هي مصفوفة الأحرف المُرمزة بـ UTF-8 غير المنتهية بـ null. الحد الأقصى للطول هو 255 بايت (وليس أحرف). قد يكون الطول 0.

### PublicKey

#### الوصف

يُستخدم هذا الهيكل في ElGamal أو أنواع التشفير غير المتماثل الأخرى، حيث يمثل الأس فقط وليس الأعداد الأولية، والتي تكون ثابتة ومُعرّفة في مواصفات التشفير [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). مخططات التشفير الأخرى في طور التعريف، انظر الجدول أدناه.

#### المحتويات

يتم استنتاج نوع المفتاح وطوله من السياق أو يتم تحديدهما في شهادة المفتاح الخاصة بوجهة أو RouterInfo، أو الحقول في [LeaseSet2](#leaseset2) أو هيكل بيانات آخر. النوع الافتراضي هو ElGamal. اعتباراً من الإصدار 0.9.38، قد يتم دعم أنواع أخرى، حسب السياق. المفاتيح big-endian ما لم يُذكر خلاف ذلك.

مفاتيح X25519 مدعومة في Destinations وLeaseSet2 اعتباراً من الإصدار 0.9.44. مفاتيح X25519 مدعومة في RouterIdentities اعتباراً من الإصدار 0.9.48.

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

### المفتاح الخاص

#### الوصف

يتم استخدام هذا الهيكل في ElGamal أو فك التشفير غير المتماثل الآخر، ويمثل الأس فقط، وليس الأعداد الأولية التي تكون ثابتة ومحددة في مواصفات التشفير [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). مخططات التشفير الأخرى في طور التعريف، راجع الجدول أدناه.

#### المحتويات

يتم استنتاج نوع ومدى المفتاح من السياق أو يتم تخزينهما منفصلين في بنية بيانات أو ملف مفتاح خاص. النوع الافتراضي هو ElGamal. اعتباراً من الإصدار 0.9.38، قد يتم دعم أنواع أخرى، حسب السياق. المفاتيح هي big-endian ما لم يُذكر خلاف ذلك.

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

#### الوصف

يتم استخدام هذه البنية للتشفير وفك التشفير المتماثل باستخدام AES256.

#### المحتويات

32 بايت

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### SigningPublicKey

#### الوصف

تُستخدم هذه البنية للتحقق من التوقيعات.

#### المحتويات

يتم استنتاج نوع المفتاح وطوله من السياق أو يتم تحديدهما في Key Certificate الخاص بـ Destination. النوع الافتراضي هو DSA_SHA1. اعتباراً من الإصدار 0.9.12، قد يتم دعم أنواع أخرى، حسب السياق.

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
#### ملاحظات

* عندما يتكون مفتاح من عنصرين (على سبيل المثال النقاط X,Y)، يتم تسلسله عن طريق ملء كل عنصر إلى length/2 بأصفار بادئة إذا لزم الأمر.

* جميع الأنواع تستخدم ترتيب البايت الكبير (Big Endian)، باستثناء EdDSA و RedDSA، والتي يتم تخزينها ونقلها بتنسيق ترتيب البايت الصغير (Little Endian).

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### الوصف

يُستخدم هذا الهيكل لإنشاء التوقيعات.

#### المحتويات

يتم تحديد نوع المفتاح وطوله عند الإنشاء. النوع الافتراضي هو DSA_SHA1. اعتباراً من الإصدار 0.9.12، قد يتم دعم أنواع أخرى، حسب السياق.

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
#### ملاحظات

* عندما يتكون المفتاح من عنصرين (على سبيل المثال النقاط X,Y)، يتم تسلسله عن طريق حشو كل عنصر إلى length/2 بأصفار بادئة إذا لزم الأمر.

* جميع الأنواع تستخدم ترتيب البايت الكبير (Big Endian)، باستثناء EdDSA و RedDSA، والتي يتم تخزينها ونقلها بتنسيق ترتيب البايت الصغير (Little Endian).

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### التوقيع

#### الوصف

تمثل هذه البنية توقيع بعض البيانات.

#### المحتويات

يتم استنتاج نوع التوقيع وطوله من نوع المفتاح المستخدم. النوع الافتراضي هو DSA_SHA1. اعتباراً من الإصدار 0.9.12، قد يتم دعم أنواع أخرى، حسب السياق.

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
#### ملاحظات

* عندما يتكون التوقيع من عنصرين (على سبيل المثال القيم R,S)، يتم تسلسله من خلال حشو كل عنصر إلى length/2 بأصفار بادئة إذا لزم الأمر.

* جميع الأنواع تستخدم ترتيب البايت الكبير (Big Endian)، باستثناء EdDSA و RedDSA، والتي يتم تخزينها ونقلها بتنسيق ترتيب البايت الصغير (Little Endian).

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### التجمع

#### الوصف

يمثل SHA256 لبعض البيانات.

#### المحتويات

32 بايت

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### علامة الجلسة

ملاحظة: علامات الجلسة (Session Tags) لوجهات ECIES-X25519 (ratchet) و routers الخاصة بـ ECIES-X25519 هي 8 بايت. راجع [ECIES](/docs/specs/ecies/) و [ECIES-ROUTERS](/docs/specs/ecies-routers/).

#### الوصف

رقم عشوائي

#### المحتويات

32 بايت

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### الوصف

يُعرِّف معرفاً فريداً لكل router في tunnel. عادة ما يكون Tunnel ID أكبر من الصفر؛ لا تستخدم قيمة الصفر إلا في الحالات الخاصة.

#### المحتويات

4 بايت [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### الشهادة

#### الوصف

الشهادة هي حاوية لمختلف الإيصالات أو إثباتات العمل المستخدمة عبر شبكة I2P.

#### المحتويات

1 بايت [Integer](#integer) يحدد نوع الشهادة، متبوعًا بـ 2 بايت [Integer](#integer) يحدد حجم حمولة الشهادة، ثم عدد البايتات المقابل.

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
#### ملاحظات

* بالنسبة لـ [Router Identities](#routeridentity)، فإن الشهادة تكون دائماً NULL حتى الإصدار 0.9.15. اعتباراً من الإصدار 0.9.16، يتم استخدام شهادة المفتاح لتحديد أنواع المفاتيح. اعتباراً من الإصدار 0.9.48، أنواع مفاتيح التشفير العامة X25519 مسموحة. انظر أدناه.

* بالنسبة لـ [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove)، الشهادة دائماً NULL، ولا يوجد أي تطبيقات أخرى حالياً.

* بالنسبة لـ [Garlic Messages](/docs/specs/i2np/#msg-garlic)، تكون الشهادة (Certificate) دائماً NULL، ولا يوجد أي شهادات أخرى مُطبقة حالياً.

* بالنسبة لـ [Destinations](#destination)، قد تكون الشهادة غير فارغة (non-NULL). اعتباراً من الإصدار 0.9.12، يمكن استخدام شهادة المفتاح لتحديد نوع مفتاح التوقيع العام. انظر أدناه.

* يُحذر المطورون من السماح ببيانات زائدة في الشهادات.
  يجب فرض الطول المناسب لكل نوع من أنواع الشهادات.

#### أنواع الشهادات

أنواع الشهادات التالية محددة:

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
#### شهادات المفاتيح

تم تقديم شهادات المفاتيح في الإصدار 0.9.12. قبل ذلك الإصدار، كانت جميع PublicKeys عبارة عن مفاتيح ElGamal بحجم 256 بايت، وكانت جميع SigningPublicKeys عبارة عن مفاتيح DSA-SHA1 بحجم 128 بايت. توفر شهادة المفتاح آلية للإشارة إلى نوع PublicKey و SigningPublicKey في الوجهة أو هوية router، وتغليف أي بيانات مفتاح تتجاوز الأطوال القياسية.

من خلال الحفاظ على 384 بايت بالضبط قبل الشهادة، ووضع أي بيانات مفاتيح إضافية داخل الشهادة، نحافظ على التوافق مع أي برنامج يقوم بتحليل الوجهات وهويات الموجهات.

تحتوي حمولة شهادة المفتاح على:

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
تحذير: ترتيب أنواع المفاتيح عكس ما قد تتوقعه؛ نوع مفتاح التوقيع العام يأتي أولاً.

أنواع مفاتيح التوقيع العامة المحددة هي:

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
أنواع مفاتيح التشفير العامة المُعرَّفة هي:

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
عندما لا تكون Key Certificate موجودة، يتم تعريف الـ 384 بايت السابقة في Destination أو RouterIdentity على أنها 256 بايت للـ ElGamal PublicKey متبوعة بـ 128 بايت للـ DSA-SHA1 SigningPublicKey. عندما تكون Key Certificate موجودة، يتم إعادة تعريف الـ 384 بايت السابقة كما يلي:

* كامل أو الجزء الأول من مفتاح التشفير العام

* حشو عشوائي إذا كان إجمالي أطوال المفتاحين أقل من 384 بايت

* الجزء الكامل أو الجزء الأول من مفتاح التوقيع العام

يتم محاذاة Crypto Public Key في البداية ويتم محاذاة Signing Public Key في النهاية. الحشو (إن وجد) في المنتصف. أطوال وحدود بيانات المفتاح الأولية، والحشو، وأجزاء بيانات المفتاح الزائدة في الشهادات غير محددة بشكل صريح، ولكن يتم اشتقاقها من أطوال أنواع المفاتيح المحددة. إذا تجاوزت الأطوال الإجمالية لمفاتيح Crypto و Signing Public Keys 384 بايت، فسيتم احتواء الباقي في Key Certificate. إذا لم يكن طول Crypto Public Key هو 256 بايت، فستتم تحديد طريقة تحديد الحد الفاصل بين المفتاحين في مراجعة مستقبلية لهذا المستند.

أمثلة على التخطيطات باستخدام مفتاح التشفير العام ElGamal ونوع مفتاح التوقيع العام المشار إليه:

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

#### ملاحظات

* يُنصح المطورون بمنع البيانات الزائدة في Key Certificates.
  يجب تطبيق الطول المناسب لكل نوع من أنواع الشهادات.

* شهادة KEY مع الأنواع 0,0 (ElGamal,DSA_SHA1) مسموحة لكن غير مستحسنة.
  لم يتم اختبارها جيداً وقد تسبب مشاكل في بعض التطبيقات.
  استخدم شهادة NULL في التمثيل القانوني لـ
  (ElGamal,DSA_SHA1) Destination أو RouterIdentity، والتي ستكون أقصر بـ 4 بايتات
  من استخدام شهادة KEY.

### التخطيط

#### الوصف

مجموعة من تطابقات المفاتيح/القيم أو الخصائص

#### المحتويات

عدد صحيح بحجم 2 بايت متبوعًا بسلسلة من أزواج String=String;

تحذير: معظم استخدامات Mapping توجد في الهياكل الموقعة، حيث يجب ترتيب إدخالات Mapping حسب المفتاح، بحيث يكون التوقيع غير قابل للتغيير. عدم الترتيب حسب المفتاح سيؤدي إلى فشل التوقيع!

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
#### ملاحظات

* التشفير ليس مُحسَّناً - نحتاج إما إلى الرموز '=' و ';'، أو أطوال النصوص، ولكن ليس كليهما

* تذكر بعض الوثائق أن السلاسل النصية قد لا تتضمن '=' أو ';' لكن هذا التشفير يدعمها

* النصوص محددة لتكون UTF-8 لكن في التنفيذ الحالي، I2CP يستخدم UTF-8 بينما I2NP لا يفعل ذلك. على سبيل المثال، نصوص UTF-8 في خريطة خيارات RouterInfo في رسالة I2NP Database Store Message ستكون تالفة.

* يسمح الترميز بالمفاتيح المكررة، ولكن في أي استخدام يكون فيه التطابق موقعاً، قد تسبب المفاتيح المكررة فشلاً في التوقيع.

* التطابقات الموجودة في رسائل I2NP (مثل في RouterAddress أو RouterInfo)
  يجب أن تكون مرتبة حسب المفتاح بحيث يكون التوقيع ثابتاً. المفاتيح المكررة
  غير مسموحة.

* يجب أن تكون التخصيصات الموجودة في [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig) مرتبة حسب المفتاح بحيث يكون التوقيع ثابتاً. المفاتيح المكررة غير مسموحة.

* طريقة الترتيب محددة كما في Java String.compareTo()، باستخدام قيمة Unicode للأحرف.

* بينما يعتمد الأمر على التطبيق، فإن المفاتيح والقيم حساسة لحالة الأحرف بشكل عام.

* حدود طول سلسلة المفتاح والقيمة هي 255 بايت (وليس أحرف) لكل منهما، بالإضافة إلى بايت الطول. يمكن أن يكون بايت الطول 0.

* حد الطول الإجمالي هو 65535 بايت، بالإضافة إلى حقل الحجم المكون من 2 بايت، أو 65537 إجمالي.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## مواصفة الهيكل المشترك

### KeysAndCert

#### الوصف

مفتاح تشفير عام ومفتاح توقيع عام وشهادة، تُستخدم إما كـ RouterIdentity أو Destination.

#### المحتويات

[PublicKey](#publickey) متبوع بـ [SigningPublicKey](#signingpublickey) ثم [Certificate](#certificate).

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
#### إرشادات إنتاج الحشو

تم اقتراح هذه الإرشادات في الاقتراح 161 وتم تنفيذها في إصدار API 0.9.57. هذه الإرشادات متوافقة مع الإصدارات السابقة لجميع الإصدارات منذ 0.6 (2005). راجع الاقتراح 161 للحصول على معلومات أساسية وإضافية.

بالنسبة لأي مزيج مستخدم حالياً من أنواع المفاتيح بخلاف ElGamal + DSA-SHA1، سيكون هناك حشو موجود. بالإضافة إلى ذلك، بالنسبة للوجهات، لم يعد حقل المفتاح العام الذي يبلغ 256 بايت مستخدماً منذ الإصدار 0.6 (2005).

يجب على المطورين توليد البيانات العشوائية لمفاتيح Destination العامة، وحشو Destination وهوية router بحيث تكون قابلة للضغط في بروتوكولات I2P المختلفة مع الحفاظ على الأمان، ودون أن تبدو تمثيلات Base 64 وكأنها تالفة أو غير آمنة. هذا يوفر معظم فوائد إزالة حقول الحشو دون أي تغييرات مدمرة في البروتوكول.

من الناحية التقنية الصارمة، فإن مفتاح التوقيع العام المكون من 32 بايت وحده (في كل من Destinations وهويات Router) ومفتاح التشفير العام المكون من 32 بايت (في هويات Router فقط) هو رقم عشوائي يوفر كل العشوائية اللازمة لجعل خلاصات SHA-256 لهذه الهياكل قوية تشفيرياً وموزعة عشوائياً في DHT لقاعدة بيانات الشبكة.

ومع ذلك، من باب الحذر الشديد، نوصي باستخدام حد أدنى من 32 بايت من البيانات العشوائية في حقل ElG public key والحشو. بالإضافة إلى ذلك، إذا كانت جميع الحقول أصفار، فإن وجهات Base 64 ستحتوي على سلاسل طويلة من أحرف AAAA، مما قد يسبب القلق أو الارتباك للمستخدمين.

كرر 32 بايت من البيانات العشوائية حسب الضرورة بحيث يكون هيكل KeysAndCert الكامل قابلاً للضغط بشكل كبير في بروتوكولات I2P مثل I2NP Database Store Message و Streaming SYN و SSU2 handshake و repliable Datagrams.

أمثلة:

* هوية router مع نوع تشفير X25519 ونوع توقيع Ed25519
  ستحتوي على 10 نسخ (320 بايت) من البيانات العشوائية، مما يوفر حوالي 288 بايت عند الضغط.

* Destination مع نوع توقيع Ed25519
  ستحتوي على 11 نسخة (352 بايت) من البيانات العشوائية، مما يوفر حوالي 320 بايت عند الضغط.

يجب على التطبيقات، بالطبع، تخزين البنية الكاملة المكونة من 387+ بايت لأن hash SHA-256 الخاص بالبنية يغطي المحتويات الكاملة.

#### ملاحظات

* لا تفترض أن هذه دائماً 387 بايت! هي 387 بايت بالإضافة إلى طول الشهادة المحدد في البايتات 385-386، والذي قد يكون غير صفر.

* اعتباراً من الإصدار 0.9.12، إذا كانت الشهادة هي Key Certificate، فقد تختلف حدود حقول المفاتيح. راجع قسم Key Certificate أعلاه للتفاصيل.

* يتم محاذاة المفتاح العام للتشفير في البداية ويتم محاذاة المفتاح العام للتوقيع في النهاية. الحشو (إن وجد) يكون في المنتصف.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### الوصف

يحدد الطريقة لتعريف router معين بشكل فريد

#### المحتويات

مطابق لـ KeysAndCert.

انظر [KeysAndCert](#keysandcert) للحصول على إرشادات حول إنتاج البيانات العشوائية لحقل الحشو.

#### ملاحظات

* كانت الشهادة الخاصة بـ RouterIdentity دائماً NULL حتى الإصدار 0.9.12.

* لا تفترض أن هذه دائماً 387 بايت! إنها 387 بايت بالإضافة إلى طول الشهادة المحدد في البايتات 385-386، والذي قد يكون غير صفري.

* اعتباراً من الإصدار 0.9.12، إذا كانت الشهادة هي Key Certificate، فقد تختلف حدود حقول المفاتيح. راجع قسم Key Certificate أعلاه للتفاصيل.

* يتم محاذاة المفتاح العام للتشفير في البداية ويتم محاذاة المفتاح العام للتوقيع في النهاية. الحشو (إن وجد) يكون في المنتصف.

* RouterIdentities مع شهادة مفتاح ومفتاح عام ECIES_X25519
  مدعومة اعتباراً من الإصدار 0.9.48.
  قبل ذلك، كانت جميع RouterIdentities من نوع ElGamal.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### الوجهة

#### الوصف

يُعرّف الـ Destination نقطة نهاية معينة يمكن توجيه الرسائل إليها للتسليم الآمن.

#### المحتويات

مطابق لـ [KeysAndCert](#keysandcert)، باستثناء أن المفتاح العام لا يُستخدم أبداً، وقد يحتوي على بيانات عشوائية بدلاً من مفتاح ElGamal عام صحيح.

انظر [KeysAndCert](#keysandcert) للحصول على إرشادات حول توليد البيانات العشوائية لحقول المفتاح العام والحشو.

#### ملاحظات

* تم استخدام المفتاح العام للوجهة للتشفير القديم من i2cp إلى i2cp
  والذي تم إلغاؤه في الإصدار 0.6 (2005)، وهو حالياً غير مستخدم باستثناء
  IV لتشفير LeaseSet، والذي أصبح مهجوراً. يتم استخدام المفتاح العام في
  LeaseSet بدلاً من ذلك.

* لا تفترض أن هذه دائماً 387 بايت! إنها 387 بايت بالإضافة إلى طول الشهادة المحدد في البايتات 385-386، والذي قد يكون غير صفر.

* اعتباراً من الإصدار 0.9.12، إذا كانت الشهادة هي Key Certificate، فقد تختلف حدود حقول المفاتيح. راجع قسم Key Certificate أعلاه للحصول على التفاصيل.

* يتم محاذاة المفتاح العام للتشفير في البداية ويتم محاذاة المفتاح العام للتوقيع في النهاية. الحشو (إن وجد) يكون في الوسط.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### الوصف

يحدد التفويض لـ tunnel معين لتلقي الرسائل المستهدفة لـ [Destination](#destination).

#### المحتويات

SHA256 [Hash](#hash) لـ [RouterIdentity](#routeridentity) الخاص بـ router البوابة، ثم [TunnelId](#tunnelid)، وأخيراً [Date](#date) النهاية.

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
#### ملاحظات

* الحجم الإجمالي: 44 بايت

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### الوصف

يحتوي على جميع [Leases](#lease) المصرح بها حاليًا لوجهة [Destination](#destination) معينة، و[PublicKey](#publickey) الذي يمكن تشفير رسائل garlic إليه، ثم [SigningPublicKey](#signingpublickey) الذي يمكن استخدامه لإلغاء هذا الإصدار المحدد من البنية. LeaseSet هو أحد البنيتين المخزنتين في قاعدة بيانات الشبكة (والأخرى هي [RouterInfo](#routerinfo))، ويُفهرس تحت SHA256 للوجهة [Destination](#destination) المحتواة.

#### المحتويات

[Destination](#destination)، يليه [PublicKey](#publickey) للتشفير، ثم [SigningPublicKey](#signingpublickey) والذي يمكن استخدامه لإلغاء هذا الإصدار من LeaseSet، ثم بايت واحد [Integer](#integer) يحدد عدد هياكل [Lease](#lease) الموجودة في المجموعة، يليه هياكل [Lease](#lease) الفعلية وأخيراً [Signature](#signature) للبايتات السابقة موقعة بواسطة [SigningPrivateKey](#signingprivatekey) الخاص بـ [Destination](#destination).

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
#### ملاحظات

* تم استخدام المفتاح العام للوجهة للتشفير القديم من I2CP إلى I2CP والذي تم تعطيله في الإصدار 0.6، وهو حالياً غير مستخدم.

* يتم استخدام مفتاح التشفير للتشفير من طرف إلى طرف ElGamal/AES+SessionTag
  [ELGAMAL-AES](/docs/specs/elgamal-aes/). يتم إنشاؤه حاليًا من جديد عند كل بدء تشغيل router، وهو
  غير مستمر.

* يمكن التحقق من التوقيع باستخدام المفتاح العام للتوقيع الخاص بالوجهة.

* LeaseSet مع صفر Leases مسموح لكن غير مستخدم.
  كان مخصصاً لإلغاء LeaseSet، والذي لم يتم تنفيذه.
  جميع متغيرات LeaseSet2 تتطلب Lease واحد على الأقل.

* يكون signing_key غير مُستخدم حالياً. كان مُخصصاً لإلغاء leaseSet،
  والذي لم يتم تنفيذه. يتم إنشاؤه حالياً من جديد عند كل بدء تشغيل للموجه router،
  وهو ليس دائماً. نوع signing key يكون دائماً نفس نوع
  signing key الخاص بالوجهة destination.

* يُعامل أقرب انتهاء صلاحية لجميع عقود الإيجار (Leases) كطابع زمني أو إصدار لـ LeaseSet. بشكل عام، لن تقبل الموجهات (routers) تخزين LeaseSet إلا إذا كان "أحدث" من الحالي. كن حذراً عند نشر LeaseSet جديد حيث يكون عقد الإيجار الأقدم هو نفسه عقد الإيجار الأقدم في LeaseSet السابق. يجب على الموجه الناشر بشكل عام زيادة انتهاء صلاحية عقد الإيجار الأقدم بما لا يقل عن 1 مللي ثانية في هذه الحالة.

* قبل الإصدار 0.9.7، عندما يتم تضمينها في رسالة DatabaseStore Message المُرسلة من قبل router المنشئ، كان router يضع جميع انتهاءات leases المنشورة لنفس القيمة، وهي قيمة lease الأقرب انتهاءً. اعتباراً من الإصدار 0.9.7، يقوم router بنشر انتهاء lease الفعلي لكل lease. هذا تفصيل تنفيذي وليس جزءاً من مواصفات الهياكل.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### الوصف

يحدد التفويض لنفق معين لاستقبال الرسائل المُوجهة إلى [Destination](#destination). نفس [Lease](#lease) ولكن مع end_date من 4 بايت. يُستخدم بواسطة [LeaseSet2](#leaseset2). مدعوم اعتباراً من الإصدار 0.9.38؛ راجع المقترح 123 لمزيد من المعلومات.

#### المحتويات

SHA256 [Hash](#hash) لـ [RouterIdentity](#routeridentity) الخاص بـ router البوابة، ثم [TunnelId](#tunnelid)، وأخيراً تاريخ انتهاء من 4 بايت.

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
#### ملاحظات

* الحجم الإجمالي: 40 بايت

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### الوصف

هذا جزء اختياري من [LeaseSet2Header](#leaseset2header). يُستخدم أيضًا في streaming و I2CP. مدعوم اعتبارًا من الإصدار 0.9.38؛ راجع الاقتراح 123 لمزيد من المعلومات.

#### المحتويات

يحتوي على انتهاء صلاحية، ونوع توقيع و[SigningPublicKey](#signingpublickey) مؤقت، و[Signature](#signature).

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
#### ملاحظات

* يمكن إنشاء هذا القسم، ويجب إنشاؤه، دون اتصال بالإنترنت.

### LeaseSet2Header

#### الوصف

هذا هو الجزء المشترك من [LeaseSet2](#leaseset2) و [MetaLeaseSet](#metaleaseset). مدعوم اعتباراً من الإصدار 0.9.38؛ انظر الاقتراح 123 للمزيد من المعلومات.

#### المحتويات

يحتوي على [Destination](#destination)، وطابعين زمنيين، و [OfflineSignature](#offlinesignature) اختياري.

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
#### ملاحظات

* الحجم الإجمالي: 395 بايت كحد أدنى

* الحد الأقصى الفعلي لوقت انتهاء الصلاحية هو حوالي 660 (11 دقيقة) لـ
  [LeaseSet2](#leaseset2) و 65535 (18.2 ساعة كاملة) لـ [MetaLeaseSet](#metaleaseset).

* [LeaseSet](#leaseset) (1) لم يحتوي على حقل 'published'، لذلك تطلب التحكم في الإصدارات البحث عن أقدم lease. يضيف LeaseSet2 حقل 'published' بدقة ثانية واحدة. يجب على أجهزة router تقييد معدل إرسال leasesets جديدة إلى floodfills بمعدل أبطأ بكثير من مرة واحدة في الثانية (لكل وجهة). إذا لم يتم تنفيذ ذلك، فيجب على الكود التأكد من أن كل leaseset جديد لديه وقت 'published' متأخر بثانية واحدة على الأقل عن السابق، وإلا فلن تقوم floodfills بتخزين أو إغراق leaseset الجديد.

### LeaseSet2

#### الوصف

موجود في رسالة I2NP DatabaseStore من النوع 3. مدعوم اعتبارًا من الإصدار 0.9.38؛ راجع الاقتراح 123 لمزيد من المعلومات.

يحتوي على جميع [Lease2](#lease2) المُصرح بها حالياً لـ [Destination](#destination) معين، و [PublicKey](#publickey) التي يمكن تشفير رسائل garlic إليها. LeaseSet هو أحد الهيكلين المخزنين في قاعدة بيانات الشبكة (والآخر هو [RouterInfo](#routerinfo))، ويتم فهرسته تحت SHA256 للـ [Destination](#destination) المحتوى.

#### المحتويات

[LeaseSet2Header](#leaseset2header)، متبوعًا بخيارات، ثم واحد أو أكثر من [PublicKey](#publickey) للتشفير، [Integer](#integer) يحدد عدد هياكل [Lease2](#lease2) الموجودة في المجموعة، متبوعًا بهياكل [Lease2](#lease2) الفعلية وأخيرًا [Signature](#signature) للبايتات السابقة موقعة بواسطة [SigningPrivateKey](#signingprivatekey) الخاص بـ [Destination](#destination) أو المفتاح المؤقت.

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
#### تفضيل مفتاح التشفير

بالنسبة لـ leasesets المنشورة (الخادم)، فإن مفاتيح التشفير مرتبة حسب تفضيل الخادم، الأكثر تفضيلاً أولاً. إذا كان العملاء يدعمون أكثر من نوع تشفير واحد، فمن المستحسن أن يحترموا تفضيل الخادم ويختاروا أول نوع مدعوم كطريقة التشفير المستخدمة للاتصال بالخادم. بشكل عام، أنواع المفاتيح الأحدث (ذات الأرقام الأعلى) أكثر أماناً أو كفاءة وهي مفضلة، لذلك يجب إدراج المفاتيح بترتيب عكسي لنوع المفتاح.

ومع ذلك، يمكن للعملاء، حسب التنفيذ، الاختيار بناءً على تفضيلهم بدلاً من ذلك، أو استخدام طريقة ما لتحديد التفضيل "المدمج". قد يكون هذا مفيداً كخيار إعداد، أو لأغراض التشخيص.

ترتيب المفاتيح في leasesets غير المنشورة (العميل) لا يهم فعلياً، لأن الاتصالات عادة لن يتم محاولتها مع العملاء غير المنشورين. ما لم يتم استخدام هذا الترتيب لتحديد تفضيل مدمج، كما هو موضح أعلاه.

#### الخيارات

اعتبارًا من API 0.9.66، تم تحديد صيغة معيارية لخيارات service record. راجع الاقتراح 167 للتفاصيل. قد يتم تحديد خيارات أخرى غير service records باستخدام صيغة مختلفة في المستقبل.

خيارات LS2 يجب أن تكون مرتبة حسب المفتاح، بحيث يكون التوقيع ثابتاً.

خيارات سجل الخدمة محددة كما يلي:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := الاسم الرمزي للخدمة المرغوبة. يجب أن يكون بأحرف صغيرة. مثال: "smtp".
  الأحرف المسموحة هي [a-z0-9-] ويجب ألا تبدأ أو تنتهي بـ '-'.
  يجب استخدام المعرفات القياسية من [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) أو Linux /etc/services إذا كانت محددة هناك.
- proto := بروتوكول النقل للخدمة المرغوبة. يجب أن يكون بأحرف صغيرة، إما "tcp" أو "udp".
  "tcp" يعني التدفق و "udp" يعني الرسائل القابلة للرد.
  قد يتم تحديد مؤشرات البروتوكول للرسائل الخام و datagram2 لاحقاً.
  الأحرف المسموحة هي [a-z0-9-] ويجب ألا تبدأ أو تنتهي بـ '-'.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := وقت البقاء، ثوانٍ صحيحة. عدد صحيح موجب. مثال: "86400".
  يُنصح بحد أدنى 86400 (يوم واحد)، انظر قسم التوصيات أدناه للتفاصيل.
- priority := أولوية المضيف المستهدف، القيمة الأقل تعني تفضيل أكبر. عدد صحيح غير سالب. مثال: "0"
  مفيد فقط إذا كان هناك أكثر من سجل واحد، ولكن مطلوب حتى لو كان سجل واحد فقط.
- weight := وزن نسبي للسجلات التي لها نفس الأولوية. القيمة الأعلى تعني فرصة أكبر للاختيار. عدد صحيح غير سالب. مثال: "0"
  مفيد فقط إذا كان هناك أكثر من سجل واحد، ولكن مطلوب حتى لو كان سجل واحد فقط.
- port := منفذ I2CP الذي توجد عليه الخدمة. عدد صحيح غير سالب. مثال: "25"
  المنفذ 0 مدعوم لكن غير مُستحسن.
- target := اسم المضيف أو b32 للوجهة التي تقدم الخدمة. اسم مضيف صالح كما في [NAMING](/docs/overview/naming/). يجب أن يكون بأحرف صغيرة.
  مثال: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" أو "example.i2p".
  يُنصح بـ b32 إلا إذا كان اسم المضيف "معروف جيداً"، أي في دفاتر العناوين الرسمية أو الافتراضية.
- appoptions := نص عشوائي خاص بالتطبيق، يجب ألا يحتوي على " " أو ",". الترميز هو UTF-8.

أمثلة:

في LS2 لـ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p، يشير إلى خادم SMTP واحد:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

في LS2 لـ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p، يشير إلى خادمي SMTP:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

في LS2 لـ bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p، يشير إلى نفسه كخادم SMTP:

"_smtp._tcp" "0 999999 25"

#### ملاحظات

* تم استخدام المفتاح العام للوجهة لتشفير I2CP-to-I2CP القديم الذي تم تعطيله في الإصدار 0.6، وهو حالياً غير مستخدم.

* مفاتيح التشفير تُستخدم للتشفير من نهاية إلى نهاية ElGamal/AES+SessionTag
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (النوع 0) أو مخططات التشفير الأخرى من نهاية إلى نهاية.
  انظر [ECIES](/docs/specs/ecies/) والمقترحات 145 و 156.
  يمكن إنشاؤها من جديد عند كل بدء تشغيل للـ router
  أو يمكن أن تكون دائمة.
  X25519 (النوع 4، انظر [ECIES](/docs/specs/ecies/)) مدعوم اعتباراً من الإصدار 0.9.44.

* التوقيع يكون على البيانات أعلاه، مُسبوقة بالبايت الواحد الذي يحتوي على نوع DatabaseStore (3).

* يمكن التحقق من التوقيع باستخدام المفتاح العام للتوقيع الخاص بالوجهة، أو المفتاح العام المؤقت للتوقيع، إذا كان التوقيع غير المتصل مضمناً في رأس leaseset2.

* يتم توفير طول المفتاح لكل مفتاح، بحيث يمكن لـ floodfills والعملاء تحليل الهيكل حتى لو لم تكن جميع أنواع التشفير معروفة أو مدعومة.

* انظر ملاحظة حول حقل 'published' في [LeaseSet2Header](#leaseset2header)

* تخطيط الخيارات، إذا كان الحجم أكبر من واحد، يجب أن يكون مرتباً حسب المفتاح، بحيث يكون التوقيع ثابتاً.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### الوصف

يحدد التفويض لـ tunnel معين لاستقبال الرسائل المستهدفة لـ [Destination](#destination). مماثل لـ [Lease2](#lease2) ولكن مع flags وتكلفة بدلاً من معرف tunnel. يُستخدم بواسطة [MetaLeaseSet](#metaleaseset). محتوى في رسالة I2NP DatabaseStore من النوع 7. مدعوم اعتباراً من الإصدار 0.9.38؛ راجع الاقتراح 123 لمزيد من المعلومات.

#### المحتويات

SHA256 [Hash](#hash) الخاص بـ [RouterIdentity](#routeridentity) لـ gateway router، ثم flags والتكلفة، وأخيراً تاريخ انتهاء مكون من 4 بايت.

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
#### ملاحظات

* الحجم الإجمالي: 40 بايت

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### الوصف

موجود في رسالة I2NP DatabaseStore من النوع 7. تم تعريفه اعتبارًا من الإصدار 0.9.38؛ مجدول للعمل اعتبارًا من الإصدار 0.9.40؛ راجع الاقتراح 123 للحصول على مزيد من المعلومات.

يحتوي على جميع [MetaLease](#metalease) المُصرح بها حاليًا لـ [Destination](#destination) معين، و [PublicKey](#publickey) التي يمكن تشفير رسائل garlic إليها. LeaseSet هو أحد الهيكلين المُخزنين في قاعدة بيانات الشبكة (الآخر هو [RouterInfo](#routerinfo))، ويتم فهرسته تحت SHA256 للـ [Destination](#destination) المُضمن.

#### المحتويات

[LeaseSet2Header](#leaseset2header)، متبوعًا بخيارات، [Integer](#integer) يحدد عدد هياكل [Lease2](#lease2) الموجودة في المجموعة، متبوعًا بهياكل [Lease2](#lease2) الفعلية وأخيرًا [Signature](#signature) للبايتات السابقة موقعة بواسطة [SigningPrivateKey](#signingprivatekey) الخاص بـ [Destination](#destination) أو المفتاح المؤقت.

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
#### ملاحظات

* تم استخدام المفتاح العام للوجهة في تشفير I2CP-to-I2CP القديم والذي تم تعطيله في الإصدار 0.6، وهو غير مستخدم حالياً.

* التوقيع يشمل البيانات أعلاه، مُسبقة بالبايت المفرد الذي يحتوي على نوع DatabaseStore (7).

* يمكن التحقق من التوقيع باستخدام المفتاح العام للتوقيع الخاص بالوجهة، أو المفتاح العام المؤقت للتوقيع، إذا كان التوقيع غير المتصل مُضمَّناً في رأس leaseset2.

* انظر الملاحظة حول حقل 'published' في [LeaseSet2Header](#leaseset2header)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### الوصف

موجود في رسالة I2NP DatabaseStore من النوع 5. مُعرَّف اعتباراً من الإصدار 0.9.38؛ يعمل اعتباراً من الإصدار 0.9.39؛ راجع الاقتراح 123 لمزيد من المعلومات.

فقط المفتاح المخفي وتاريخ الانتهاء مرئيان في النص الواضح. أما leaseSet الفعلي فهو مشفر.

#### المحتويات

نوع توقيع من بايتين، [SigningPrivateKey](#signingprivatekey) المُعمى، وقت النشر، انتهاء الصلاحية، والعلامات. ثم، طول من بايتين متبوعًا ببيانات مشفرة. وأخيرًا، [Signature](#signature) للبايتات السابقة موقعة بواسطة [SigningPrivateKey](#signingprivatekey) المُعمى أو المفتاح المؤقت.

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
#### ملاحظات

* تم استخدام المفتاح العام للوجهة لتشفير I2CP-to-I2CP القديم والذي تم تعطيله في الإصدار 0.6، وهو غير مستخدم حالياً.

* التوقيع يكون على البيانات أعلاه، مُسبقة بالبايت الواحد
  الذي يحتوي على نوع DatabaseStore (5).

* يمكن التحقق من التوقيع باستخدام المفتاح العام للتوقيع الخاص بالوجهة، أو المفتاح العام المؤقت للتوقيع، إذا كان التوقيع غير المتصل مُضمناً في رأس leaseset2.

* التعمية والتشفير محددان في [EncryptedLeaseSet](/docs/specs/encryptedleaseset/)

* هذه البنية لا تستخدم [LeaseSet2Header](#leaseset2header).

* الحد الأقصى لوقت انتهاء الصلاحية الفعلي هو حوالي 660 (11 دقيقة)، إلا إذا كان [MetaLeaseSet](#metaleaseset) مشفراً.

* راجع الاقتراح 123 للملاحظات حول استخدام التوقيعات غير المتصلة مع leasesets المشفرة.

* راجع الملاحظة حول حقل 'published' في [LeaseSet2Header](#leaseset2header)
  (نفس المشكلة، حتى لو لم نستخدم تنسيق LeaseSet2Header هنا)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### الوصف

تحدد هذه البنية وسائل الاتصال بـ router من خلال بروتوكول نقل.

#### المحتويات

1 بايت [Integer](#integer) يحدد التكلفة النسبية لاستخدام العنوان، حيث 0 يعني مجاني و 255 يعني مكلف، متبوعاً بتاريخ انتهاء الصلاحية [Date](#date) الذي بعده لا يجب استخدام العنوان، أو إذا كان null، فإن العنوان لا ينتهي أبداً. بعد ذلك يأتي [String](#string) يحدد بروتوكول النقل الذي يستخدمه عنوان router هذا. أخيراً هناك [Mapping](#mapping) يحتوي على جميع الخيارات المحددة للنقل اللازمة لإنشاء الاتصال، مثل عنوان IP ورقم المنفذ وعنوان البريد الإلكتروني وURL، إلخ.

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
#### ملاحظات

* التكلفة عادة ما تكون 5 أو 6 لـ SSU، و 10 أو 11 لـ NTCP.

* انتهاء الصلاحية غير مستخدم حالياً، دائماً null (كلها أصفار). اعتباراً من الإصدار
  0.9.3، يُفترض أن تكون انتهاء الصلاحية صفراً ولا يتم تخزينها، لذا أي انتهاء صلاحية 
  غير صفري سيفشل في التحقق من توقيع RouterInfo. تنفيذ انتهاء الصلاحية (أو استخدام
  آخر لهذه البايتات) سيكون تغييراً غير متوافق مع الإصدارات السابقة. يجب على الـ routers
  تعيين هذا الحقل إلى كلها أصفار. اعتباراً من الإصدار 0.9.12، يتم التعرف على حقل
  انتهاء الصلاحية غير الصفري مرة أخرى، ومع ذلك يجب أن ننتظر عدة إصدارات لاستخدام هذا
  الحقل، حتى تتعرف عليه الغالبية العظمى من الشبكة.

* الخيارات التالية، بينما غير مطلوبة، هي معيارية ومتوقع وجودها في معظم عناوين router: "host" (عنوان IPv4 أو IPv6 أو اسم المضيف) و "port".

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### الوصف

يحدد جميع البيانات التي يريد الـ router نشرها ليراها الشبكة. الـ [RouterInfo](#routerinfo) هو أحد هيكلين مخزنين في قاعدة بيانات الشبكة (والآخر هو [LeaseSet](#leaseset))، ويتم فهرسته تحت الـ SHA256 الخاص بـ [RouterIdentity](#routeridentity) المضمن.

#### المحتويات

[RouterIdentity](#routeridentity) متبوعًا بـ [Date](#date)، عند نشر الإدخال

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
#### ملاحظات

* قد يتبع peer_size [Integer](#integer) قائمة تحتوي على عدد مماثل من router hashes.
  هذا غير مستخدم حالياً. كان مخصصاً لشكل من أشكال المسارات المحدودة،
  والذي لم يتم تنفيذه.
  قد تتطلب تطبيقات معينة أن تكون القائمة مرتبة حتى يكون التوقيع ثابتاً.
  يجب البحث في هذا قبل تفعيل هذه الميزة.

* يمكن التحقق من التوقيع باستخدام المفتاح العام للتوقيع الخاص بـ
  router_ident.

* راجع صفحة قاعدة بيانات الشبكة [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) للخيارات القياسية التي
  من المتوقع أن تكون موجودة في جميع معلومات router.

* أجهزة router القديمة جداً تطلبت ترتيب العناوين حسب SHA256 لبياناتها
  بحيث يكون التوقيع ثابتاً.
  هذا لم يعد مطلوباً، ولا يستحق التنفيذ من أجل التوافق مع الإصدارات السابقة.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### تعليمات التسليم

تعليمات تسليم رسائل tunnel محددة في مواصفات رسائل tunnel [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions).

تعليمات تسليم رسائل Garlic Message محددة في مواصفات رسائل I2NP [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions).

## المراجع

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

---
title: "स्ट्रीमिंग प्रोटोकॉल स्पेसिफिकेशन"
description: "I2P streaming protocol के लिए विनिर्देश जो TCP-जैसा विश्वसनीय परिवहन प्रदान करता है"
slug: "streaming"
category: "प्रोटोकॉल"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## अवलोकन

Streaming protocol की एक समग्र जानकारी के लिए [Streaming Library](/docs/api/streaming) देखें।

## प्रोटोकॉल संस्करण

streaming protocol में version field शामिल नहीं है। नीचे दिए गए versions Java I2P के लिए हैं। implementations और वास्तविक crypto support भिन्न हो सकते हैं। यह निर्धारित करने का कोई तरीका नहीं है कि far-end कोई विशेष version या feature को support करता है या नहीं। नीचे दी गई table विभिन्न features की release dates के लिए सामान्य मार्गदर्शन के रूप में है।

नीचे सूचीबद्ध सुविधाएं प्रोटोकॉल के लिए हैं। कॉन्फ़िगरेशन के विभिन्न विकल्प [Streaming Library](/docs/api/streaming) में प्रलेखित हैं और साथ ही Java I2P संस्करण भी दिया गया है जिसमें वे लागू किए गए थे।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## प्रोटोकॉल विशिष्टता

### पैकेट प्रारूप

स्ट्रीमिंग प्रोटोकॉल में एक पैकेट का प्रारूप नीचे दिखाया गया है। NACKs या option data के बिना न्यूनतम हेडर का आकार 22 बाइट्स है।

streaming protocol में कोई length field नहीं है। Framing निचली परतों द्वारा प्रदान की जाती है - I2CP और I2NP।

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : पहला SYN reply पैकेट भेजने से पहले पैकेट प्राप्तकर्ता द्वारा चुना गया यादृच्छिक संख्या और कनेक्शन के जीवनकाल के लिए स्थिर, शून्य से अधिक। कनेक्शन प्रारंभकर्ता द्वारा भेजे गए SYN संदेश में 0, और बाद के संदेशों में, जब तक SYN reply प्राप्त नहीं होती, जिसमें peer का stream ID होता है।

**receiveStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : पैकेट भेजने वाले द्वारा पहला SYN पैकेट भेजने से पहले चुना गया यादृच्छिक संख्या और कनेक्शन के जीवनकाल के लिए स्थिर, शून्य से अधिक। यदि अज्ञात हो तो 0 हो सकता है, उदाहरण के लिए RESET पैकेट में।

**sequenceNum** :: 4 byte [Integer](/docs/specs/common-structures#integer) : इस संदेश के लिए अनुक्रम, जो SYN संदेश में 0 से शुरू होता है, और सादे ACKs और पुनः प्रेषण को छोड़कर हर संदेश में 1 से बढ़ता है। यदि sequenceNum 0 है और SYN फ्लैग सेट नहीं है, तो यह एक सादा ACK पैकेट है जिसे ACK नहीं किया जाना चाहिए।

**ackThrough** :: 4 byte [Integer](/docs/specs/common-structures#integer) : सबसे ऊंचा packet sequence number जो receiveStreamId पर प्राप्त हुआ था। यह field प्रारंभिक connection packet पर अनदेखा किया जाता है (जहां receiveStreamId अज्ञात id है) या यदि NO_ACK flag सेट है। इस sequence number तक और इसे शामिल करते हुए सभी packets ACK हैं, उन packets को छोड़कर जो नीचे NACKs में सूचीबद्ध हैं।

**NACK count** :: 1 byte [Integer](/docs/specs/common-structures#integer) : अगले फील्ड में 4-byte NACKs की संख्या, या 8 जब 0.9.58 के बाद से replay prevention के लिए SYNCHRONIZE के साथ उपयोग किया जाता है; नीचे देखें।

**NACKs** :: nc * 4 byte [Integer](/docs/specs/common-structures#integer)s : Sequence numbers जो ackThrough से कम हैं और अभी तक प्राप्त नहीं हुए हैं। एक packet के दो NACKs उस packet के 'fast retransmit' के लिए अनुरोध हैं। 0.9.58 के बाद से replay prevention के लिए SYNCHRONIZE के साथ भी उपयोग किया जाता है; नीचे देखें।

**resendDelay** :: 1 byte [Integer](/docs/specs/common-structures#integer) : इस packet के निर्माता को इस packet को दोबारा भेजने से पहले कितनी देर तक इंतजार करना होगा (यदि इसे अभी तक ACK नहीं मिला है)। यह value packet बनने के बाद से seconds में है। वर्तमान में receive पर ignore किया जाता है।

**flags** :: 2 बाइट मान : नीचे देखें।

**option size** :: 2 byte [Integer](/docs/specs/common-structures#integer) : अगले फ़ील्ड में bytes की संख्या

**option data** :: 0 या अधिक bytes : जैसा कि flags द्वारा निर्दिष्ट है। नीचे देखें।

**payload** :: शेष पैकेट आकार

### फ़्लैग्स और ऑप्शन डेटा फ़ील्ड्स

ऊपर दिया गया flags फील्ड पैकेट के बारे में कुछ metadata निर्दिष्ट करता है, और बदले में कुछ अतिरिक्त डेटा शामिल करने की आवश्यकता हो सकती है। flags निम्नलिखित हैं। जो भी डेटा संरचनाएं निर्दिष्ट हैं उन्हें दिए गए क्रम में options क्षेत्र में जोड़ा जाना चाहिए।

बिट क्रम: 15....0 (15 MSB है)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### चर लंबाई हस्ताक्षर टिप्पणियां

रिलीज 0.9.11 से पहले, विकल्प फील्ड में signature हमेशा 40 bytes का होता था।

रिलीज़ 0.9.11 के अनुसार, signature परिवर्तनीय लंबाई का है। Signature का प्रकार और लंबाई FROM_INCLUDED विकल्प में उपयोग की गई key के प्रकार और [Signature](/docs/specs/common-structures#signature) दस्तावेज़ीकरण से निर्धारित होती है।

रिलीज़ 0.9.39 के रूप में, OFFLINE_SIGNATURE विकल्प समर्थित है। यदि यह विकल्प मौजूद है, तो transient [SigningPublicKey](/docs/specs/common-structures#signingpublickey) का उपयोग किसी भी हस्ताक्षरित पैकेट को सत्यापित करने के लिए किया जाता है, और signature की लंबाई और प्रकार विकल्प में transient SigningPublicKey से निकाले जाते हैं।

- जब एक packet में FROM_INCLUDED और SIGNATURE_INCLUDED दोनों शामिल होते हैं (जैसे कि SYNCHRONIZE में), तो अनुमान सीधे लगाया जा सकता है।

- जब किसी packet में FROM_INCLUDED शामिल नहीं होता है, तो अनुमान पिछले SYNCHRONIZE packet से लगाना होगा।

- जब एक packet में FROM_INCLUDED नहीं होता है, और कोई पिछला SYNCHRONIZE packet नहीं था (उदाहरण के लिए एक आवारा CLOSE या RESET packet), तो अनुमान शेष options की लंबाई से लगाया जा सकता है (क्योंकि SIGNATURE_INCLUDED अंतिम option है), लेकिन packet शायद फिर भी discard कर दिया जाएगा, क्योंकि signature को validate करने के लिए कोई FROM उपलब्ध नहीं है। यदि भविष्य में अधिक option fields परिभाषित किए जाते हैं, तो उन्हें हिसाब में लेना होगा।

### पुनरावृत्ति रोकथाम

Bob को Alice से प्राप्त एक वैध हस्ताक्षरित SYNCHRONIZE packet को स्टोर करके और बाद में इसे पीड़ित Charlie को भेजकर replay attack का उपयोग करने से रोकने के लिए, Alice को निम्नानुसार SYNCHRONIZE packet में Bob का destination hash शामिल करना चाहिए:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
SYNCHRONIZE प्राप्त होने पर, यदि NACK count फील्ड 8 है, तो Bob को NACKs फील्ड को 32-byte destination hash के रूप में व्याख्या करना चाहिए, और यह सत्यापित करना चाहिए कि यह उसके destination hash से मेल खाता है। उसे पैकेट के signature को भी सामान्य रूप से सत्यापित करना चाहिए, क्योंकि यह NACK count और NACKs फील्ड सहित संपूर्ण पैकेट को कवर करता है। यदि NACK count 8 है और NACKs फील्ड मेल नहीं खाता, तो Bob को पैकेट को drop करना चाहिए।

यह संस्करण 0.9.58 और इससे ऊपर के लिए आवश्यक है। यह पुराने संस्करणों के साथ backward-compatible है, क्योंकि SYNCHRONIZE packet में NACKs की अपेक्षा नहीं की जाती। Destinations को पता नहीं होता और वे जान भी नहीं सकते कि दूसरे छोर पर कौन सा संस्करण चल रहा है।

Bob से Alice को भेजे जाने वाले SYNCHRONIZE ACK packet में कोई बदलाव आवश्यक नहीं है; उस packet में NACKs शामिल न करें।

## संदर्भ

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Streaming Library](/docs/api/streaming)

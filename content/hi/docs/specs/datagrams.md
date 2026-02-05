---
title: "डेटाग्राम विनिर्देश"
description: "I2P डेटाग्राम संदेश प्रारूपों का विनिर्देश जिसमें कच्चे, उत्तर देने योग्य, और प्रमाणित प्रकार शामिल हैं"
slug: "datagrams"
category: "प्रोटोकॉल"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## अवलोकन

Datagrams API का अवलोकन के लिए [Datagrams API documentation](/docs/api/datagrams/) देखें।

निम्नलिखित प्रकार परिभाषित हैं। मानक प्रोटोकॉल संख्याएं सूचीबद्ध हैं, हालांकि स्ट्रीमिंग प्रोटोकॉल संख्या (6) के अलावा कोई भी अन्य प्रोटोकॉल संख्याएं उपयोग की जा सकती हैं, एप्लिकेशन-विशिष्ट।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
विभिन्न router और library implementations में Datagram2 और Datagram3 के लिए समर्थन TBD है। उन implementations के लिए documentation देखें।

### डेटाग्राम प्रकार पहचान

चार datagram प्रकार एक ही स्थान पर protocol version के साथ एक सामान्य header साझा नहीं करते हैं। Packets को उनकी सामग्री के आधार पर प्रकार द्वारा पहचाना नहीं जा सकता। एक ही session पर कई प्रकारों का उपयोग करते समय, या streaming के साथ एक एकल प्रकार का उपयोग करते समय, applications को आने वाले packets को सही स्थान पर route करने के लिए protocol numbers और/या I2CP/SAM ports का उपयोग करना चाहिए। मानक protocol numbers का उपयोग करना इसे आसान बनाएगा। Protocol number को अनसेट (0 या PROTO_ANY) छोड़ना, यहां तक कि एक datagram-only application के लिए भी, अनुशंसित नहीं है क्योंकि यह routing errors की संभावना बढ़ाता है और multi-protocol application में upgrades को कठिन बनाता है। Datagram 2 और 3 में version fields केवल routing errors और भविष्य के बदलावों के लिए एक अतिरिक्त जांच के रूप में प्रदान किए गए हैं।

### एप्लिकेशन डिज़ाइन

डेटाग्राम के सभी उपयोग एप्लिकेशन-विशिष्ट हैं।

चूंकि authenticated datagrams में काफी overhead होता है, एक सामान्य एप्लिकेशन authenticated और non-authenticated दोनों प्रकार के datagrams का उपयोग करती है। एक सामान्य डिज़ाइन यह है कि client से server को एक token युक्त single authenticated datagram भेजा जाता है। Server उसी token वाले एक unauthenticated datagram के साथ जवाब देता है। token timeout से पहले कोई भी बाद की संचार में raw datagrams का उपयोग होता है।

एप्लिकेशन [I2CP](/docs/specs/i2cp/) API या [SAMv3](/docs/api/samv3/) के माध्यम से प्रोटोकॉल और पोर्ट नंबर का उपयोग करके डेटाग्राम भेजते और प्राप्त करते हैं।

Datagrams निश्चित रूप से अविश्वसनीय होते हैं। Applications को अविश्वसनीय delivery के लिए design करना चाहिए। I2P के भीतर, यदि अगला hop पहुंचने योग्य है तो delivery hop-to-hop विश्वसनीय होती है, क्योंकि NTCP2 और SSU2 transports विश्वसनीयता प्रदान करते हैं। हालांकि, end-to-end delivery विश्वसनीय नहीं होती, क्योंकि I2NP messages किसी भी hop के भीतर queue limits, expirations, timeouts, bandwidth limits, या unreachable next-hops के कारण drop हो सकते हैं।

### डेटाग्राम साइज़

I2NP संदेशों के लिए नाममात्र आकार सीमा, datagrams सहित, 64 KB है। Garlic और tunnel संदेश overhead इसे कुछ हद तक कम कर देते हैं।

हालांकि, सभी I2NP संदेशों को 1 KB tunnel संदेशों में विभाजित किया जाना चाहिए। n KB I2NP संदेश की ड्रॉप संभावना एक एकल tunnel संदेश की ड्रॉप संभावना का घातांकीय फ़ंक्शन है, p ** n। चूंकि विखंडन के परिणामस्वरूप tunnel संदेशों का एक फटा आता है, वास्तविक ड्रॉप संभावना घातांकीय फ़ंक्शन की तुलना में बहुत अधिक है, क्यूंकि router कार्यान्वयन में क्यू सीमा और सक्रिय क्यू प्रबंधन (AQM, CoDel या समान) के कारण।

विश्वसनीय डिलीवरी सुनिश्चित करने के लिए अनुशंसित सामान्य अधिकतम आकार कुछ KB है, या अधिक से अधिक 10 KB है। सभी प्रोटोकॉल स्तरों (परिवहन को छोड़कर) पर ओवरहेड आकारों का सावधानीपूर्वक विश्लेषण करके, डेवलपर्स को एक अधिकतम पेलोड आकार सेट करना चाहिए जो एक, दो, या तीन tunnel मैसेज में सटीक रूप से फिट हो सके। यह दक्षता और विश्वसनीयता को अधिकतम करेगा। विभिन्न स्तरों पर ओवरहेड में gzip हेडर, I2NP हेडर, garlic मैसेज हेडर, garlic encryption, tunnel मैसेज हेडर, tunnel मैसेज fragmentation हेडर, और अन्य शामिल हैं। उदाहरणों के लिए [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/) में streaming MTU गणना और Java I2P स्रोत में ConnectionOptions.java देखें।

### SAM विचारणीय बातें

एप्लिकेशन I2CP API या SAM के माध्यम से प्रोटोकॉल और पोर्ट नंबर का उपयोग करके datagrams भेजते और प्राप्त करते हैं। SAM के माध्यम से प्रोटोकॉल और पोर्ट नंबर निर्दिष्ट करने के लिए SAM v3.2 या उससे ऊंचे संस्करण की आवश्यकता होती है। एक ही SAM session (tunnels) पर datagrams और streaming दोनों (UDP और TCP) का उपयोग करने के लिए SAM v3.3 या उससे ऊंचे संस्करण की आवश्यकता होती है। एक ही SAM session (tunnels) पर कई datagram प्रकारों का उपयोग करने के लिए SAM v3.3 या उससे ऊंचे संस्करण की आवश्यकता होती है। SAM v3.3 इस समय केवल Java I2P router द्वारा समर्थित है।

विभिन्न router और library implementations में Datagram2 और Datagram3 के लिए SAM समर्थन अभी भी निर्धारित किया जाना है। उन implementations के दस्तावेज़ीकरण की जांच करें।

ध्यान दें कि सामान्य 1500 बाइट नेटवर्क MTU से अधिक आकार SAM applications को SAM सर्वर से/तक unfragmented packets को transport करने से रोक देगा, यदि application और सर्वर अलग computers पर हैं। आमतौर पर, ऐसा नहीं होता है, वे दोनों localhost पर होते हैं, जहाँ MTU 65536 या अधिक होता है। यदि किसी SAM application को सर्वर से अलग computer पर अलग करने की अपेक्षा है, तो repliable datagram के लिए अधिकतम payload 1 KB से थोड़ा कम होता है।

### PQ विचारणाएं

यदि Post-Quantum [Proposal 169](/proposals/169-pq-crypto/) का MLDSA हिस्सा लागू किया जाता है, तो overhead काफी बढ़ जाएगा। एक destination + signature का साइज़ 391 + 64 = 455 bytes से बढ़कर MLDSA44 के लिए न्यूनतम 3739 और MLDSA87 के लिए अधिकतम 7226 हो जाएगा। इसके व्यावहारिक प्रभाव निर्धारित किए जाने हैं। Datagram3, जिसमें router द्वारा प्रमाणीकरण प्रदान किया जाता है, एक समाधान हो सकता है।

## रॉ (गैर-उत्तरदेय) डेटाग्राम {#raw}

Non-repliable datagrams का कोई 'from' पता नहीं होता और ये प्रमाणित नहीं होते। इन्हें "raw" datagrams भी कहा जाता है। सख्त अर्थ में, ये बिल्कुल भी "datagrams" नहीं हैं, ये केवल raw डेटा हैं। इन्हें datagram API द्वारा handle नहीं किया जाता। हालांकि, SAM और I2PTunnel classes "raw datagrams" को support करती हैं।

कच्चे datagrams के लिए मानक I2CP प्रोटोकॉल संख्या PROTO_DATAGRAM_RAW (18) है।

प्रारूप यहाँ निर्दिष्ट नहीं है, यह एप्लिकेशन द्वारा परिभाषित है। पूर्णता के लिए, हमने नीचे प्रारूप की एक तस्वीर शामिल की है।

### प्रारूप

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### नोट्स

व्यावहारिक लंबाई विभिन्न स्तरों पर ओवरहेड और विश्वसनीयता दोनों द्वारा सीमित है।

## Datagram1 (उत्तर देने योग्य) {#repliable}

Repliable datagrams में एक 'from' address और signature होता है। ये कम से कम 427 bytes का overhead जोड़ते हैं।

repliable datagrams के लिए मानक I2CP प्रोटोकॉल नंबर PROTO_DATAGRAM (17) है।

### प्रारूप

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
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
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### नोट्स

- व्यावहारिक लंबाई विभिन्न layers पर overhead और विश्वसनीयता दोनों द्वारा सीमित है।
- बड़े datagrams की विश्वसनीयता के बारे में महत्वपूर्ण नोट्स के लिए [Datagrams API documentation](/docs/api/datagrams/) देखें। सर्वोत्तम परिणामों के लिए, payload को लगभग 10 KB या उससे कम तक सीमित करें।
- DSA_SHA1 के अलावा अन्य types के लिए signatures को release 0.9.14 में पुनः परिभाषित किया गया था।
- यह format LS2 (proposal 123) के लिए offline signature block के समावेश का समर्थन नहीं करता है। इसके लिए flags के साथ एक नया protocol परिभाषित किया जाना चाहिए।

## Datagram2 {#datagram2}

Datagram2 फॉर्मेट वही है जो [Proposal 163](/proposals/163-datagram2/) में निर्दिष्ट है। Datagram2 के लिए I2CP protocol संख्या 19 है।

Datagram2 का उद्देश्य Datagram1 के प्रतिस्थापन के रूप में है। यह Datagram1 में निम्नलिखित सुविधाएं जोड़ता है:

- रीप्ले रोकथाम
- ऑफलाइन हस्ताक्षर समर्थन
- विस्तारशीलता के लिए फ्लैग्स और विकल्प फील्ड

ध्यान दें कि Datagram2 के लिए signature calculation algorithm Datagram1 की तुलना में काफी अलग है।

### प्रारूप

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
कुल लंबाई: न्यूनतम 433 + payload लंबाई; X25519 senders के लिए विशिष्ट लंबाई और offline signatures के बिना: 457 + payload लंबाई। ध्यान दें कि संदेश आमतौर पर I2CP layer पर gzip के साथ compressed होगा, जिससे महत्वपूर्ण बचत होगी यदि from destination compressible है।

नोट: ऑफलाइन signature format वही है जो [Common Structures Specification](/docs/specs/common-structures/) और [Streaming Specification](/docs/specs/streaming/) में है।

### हस्ताक्षर

हस्ताक्षर निम्नलिखित फ़ील्ड पर है:

- Prelude: लक्षित गंतव्य का 32-byte hash (datagram में शामिल नहीं)
- flags
- options (यदि उपस्थित है)
- offline_signature (यदि उपस्थित है)
- payload

रिप्लायएबल डेटाग्राम में, DSA_SHA1 key type के लिए, signature पेलोड के SHA-256 hash पर था, पेलोड पर नहीं; यहाँ, signature हमेशा ऊपर दिए गए फील्ड पर होता है (hash पर नहीं), key type की परवाह किए बिना।

### ToHash सत्यापन

प्राप्तकर्ताओं को signature को सत्यापित करना चाहिए (अपने destination hash का उपयोग करके) और असफलता पर datagram को त्याग देना चाहिए, replay रोकथाम के लिए।

## Datagram3 {#datagram3}

Datagram3 फॉर्मेट [Proposal 163](/proposals/163-datagram2/) में निर्दिष्ट के अनुसार है। Datagram3 के लिए I2CP protocol नंबर 20 है।

Datagram3 को raw datagrams के एक उन्नत संस्करण के रूप में डिज़ाइन किया गया है। यह raw datagrams में निम्नलिखित सुविधाएं जोड़ता है:

- पुनरावृत्ति क्षमता
- विस्तारशीलता के लिए फ्लैग और विकल्प फ़ील्ड

Datagram3 प्रमाणित नहीं है। भविष्य के प्रस्ताव में, प्रमाणीकरण router की ratchet layer द्वारा प्रदान किया जा सकता है, और प्रमाणीकरण स्थिति client को पास की जाएगी।

### प्रारूप

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
कुल लंबाई: न्यूनतम 34 + payload लंबाई।

## संदर्भ

- [Common](/docs/specs/common-structures/) - सामान्य संरचना विनिर्देश
- [DATAGRAMS](/docs/api/datagrams/) - Datagrams API अवलोकन
- [I2CP](/docs/specs/i2cp/) - I2CP विनिर्देश
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - ECIES-X25519-AEAD-Ratchet प्रस्ताव
- [Prop163](/proposals/163-datagram2/) - Datagram2 और Datagram3 प्रस्ताव
- [Prop169](/proposals/169-pq-crypto/) - Post-Quantum Cryptography प्रस्ताव
- [SAMv3](/docs/api/samv3/) - SAM v3 विनिर्देश
- [Streaming](/docs/specs/streaming/) - Streaming विनिर्देश
- [TRANSPORT](/docs/overview/transport/) - Transport अवलोकन
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Tunnel Message विनिर्देश

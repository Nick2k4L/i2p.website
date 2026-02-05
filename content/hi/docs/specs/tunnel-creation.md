---
title: "Tunnel निर्माण विनिर्देश"
description: "गैर-इंटरैक्टिव टेलीस्कोपिंग का उपयोग करके tunnel बनाने के लिए ElGamal tunnel निर्माण विनिर्देश।"
slug: "tunnel-creation"
aliases: 
category: "डिज़ाइन"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## अवलोकन

नोट: अप्रचलित - यह ElGamal tunnel build specification है। X25519 tunnel build specification के लिए [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) देखें।

यह दस्तावेज़ "non-interactive telescoping" विधि का उपयोग करके tunnel बनाने के लिए उपयोग किए जाने वाले encrypted tunnel build संदेशों की विवरण निर्दिष्ट करता है। प्रक्रिया का अवलोकन, peer selection और ordering विधियों सहित, tunnel build दस्तावेज़ [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) देखें।

tunnel निर्माण एक single message के द्वारा पूरा किया जाता है जो tunnel में peers के path के साथ भेजा जाता है, जगह पर rewrite किया जाता है, और tunnel creator को वापस transmit किया जाता है। यह single tunnel message variable संख्या के records (8 तक) से बना होता है - tunnel में प्रत्येक संभावित peer के लिए एक। Individual records को asymmetrically (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) encrypt किया जाता है ताकि वे केवल path के साथ एक specific peer द्वारा पढ़े जा सकें, जबकि encryption की एक अतिरिक्त symmetric layer (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) प्रत्येक hop पर जोड़ी जाती है ताकि asymmetrically encrypted record को केवल उपयुक्त समय पर expose किया जा सके।

### रिकॉर्ड्स की संख्या

सभी records में वैध डेटा होना आवश्यक नहीं है। उदाहरण के लिए, 3-hop tunnel के लिए build message में tunnel की वास्तविक लंबाई को प्रतिभागियों से छुपाने के लिए अधिक records हो सकते हैं। दो build message प्रकार हैं। मूल Tunnel Build Message ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) में 8 records होते हैं, जो किसी भी व्यावहारिक tunnel लंबाई के लिए पर्याप्त से अधिक है। नया Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) में 1 से 8 records होते हैं। प्रवर्तक message के आकार और tunnel लंबाई के वांछित obfuscation की मात्रा के बीच समझौता कर सकता है।

वर्तमान नेटवर्क में, अधिकांश tunnel 2 या 3 hop लंबे होते हैं। वर्तमान कार्यान्वयन 4 hop या उससे कम के tunnel बनाने के लिए 5-record VTBM का उपयोग करता है, और लंबे tunnel के लिए 8-record TBM का उपयोग करता है। 5-record VTBM (जो खंडित होने पर तीन 1KB tunnel संदेशों में फिट हो जाता है) नेटवर्क ट्रैफिक को कम करता है और निर्माण सफलता दर बढ़ाता है, क्योंकि छोटे संदेशों के गिरने की संभावना कम होती है।

उत्तर संदेश का प्रकार और लंबाई build संदेश के समान होनी चाहिए।

### अनुरोध रिकॉर्ड विनिर्देश

यह I2NP Specification [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) में भी निर्दिष्ट है।

रिकॉर्ड का cleartext, केवल पूछे जाने वाले hop को दिखाई देता है:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
अगला tunnel ID और अगला router identity hash फील्ड tunnel में अगले hop को निर्दिष्ट करने के लिए उपयोग किए जाते हैं, हालांकि outbound tunnel endpoint के लिए, ये निर्दिष्ट करते हैं कि rewritten tunnel creation reply message कहाँ भेजा जाना चाहिए। इसके अतिरिक्त, अगला message ID उस message ID को निर्दिष्ट करता है जिसका उपयोग message (या reply) को करना चाहिए।

tunnel layer key, tunnel IV key, reply key, और reply IV प्रत्येक 32-byte के यादृच्छिक मान हैं जो निर्माता द्वारा उत्पन्न किए जाते हैं, केवल इस build request record में उपयोग के लिए।

flags फील्ड में निम्नलिखित शामिल है (बिट क्रम: 76543210, बिट 7 MSB है):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
बिट 7 दर्शाता है कि hop एक inbound gateway (IBGW) होगा। बिट 6 दर्शाता है कि hop एक outbound endpoint (OBEP) होगा। यदि कोई भी बिट सेट नहीं है, तो hop एक intermediate participant होगा। दोनों एक साथ सेट नहीं हो सकते।

#### अनुरोध रिकॉर्ड निर्माण

हर hop को एक यादृच्छिक Tunnel ID मिलती है, गैर-शून्य। वर्तमान और अगले-hop के Tunnel ID भरे जाते हैं। हर record को एक यादृच्छिक tunnel IV key, reply IV, layer key, और reply key मिलती है।

#### अनुरोध रिकॉर्ड एन्क्रिप्शन

वह cleartext record ElGamal 2048 encrypted [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) है hop की public encryption key के साथ और 528 byte record में formatted है:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
512-byte एन्क्रिप्टेड रिकॉर्ड में, ElGamal डेटा में 514-byte ElGamal एन्क्रिप्टेड ब्लॉक [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) के bytes 1-256 और 258-513 शामिल हैं। ब्लॉक से दो padding bytes (स्थान 0 और 257 पर स्थित zero bytes) हटा दिए गए हैं।

चूंकि cleartext पूरे field का उपयोग करता है, इसलिए `SHA256(cleartext) + cleartext` के अलावा अतिरिक्त padding की कोई आवश्यकता नहीं है।

प्रत्येक 528-byte रिकॉर्ड को फिर iteratively encrypt किया जाता है (AES decryption का उपयोग करके, प्रत्येक hop के लिए reply key और reply IV के साथ) ताकि router identity केवल संबंधित hop के लिए ही cleartext में हो।

### Hop प्रोसेसिंग और एन्क्रिप्शन

जब कोई hop एक TunnelBuildMessage प्राप्त करता है, तो वह इसमें निहित records को देखता है और उनमें से अपने identity hash (16 bytes में trimmed) से शुरू होने वाले record को ढूंढता है। फिर वह उस record से ElGamal block को decrypt करता है और protected cleartext को retrieve करता है। उस बिंदु पर, वे AES-256 reply key को Bloom filter में डालकर यह सुनिश्चित करते हैं कि tunnel request duplicate नहीं है। Duplicates या invalid requests को drop कर दिया जाता है। जो records current hour या previous hour (यदि घंटे के शीर्ष के तुरंत बाद हो) के stamp के साथ नहीं हैं, उन्हें drop करना चाहिए। उदाहरण के लिए, timestamp में hour लें, इसे full time में convert करें, फिर यदि यह current time से 65 मिनट से अधिक पीछे या 5 मिनट आगे है, तो यह invalid है। Bloom filter की duration कम से कम एक घंटा (plus कुछ मिनट, clock skew के लिए allowance देने हेतु) होनी चाहिए, ताकि current hour में duplicate records जो record में hour timestamp check करके reject नहीं होते, वे filter द्वारा reject हो जाएं।

यह तय करने के बाद कि वे tunnel में भाग लेने के लिए सहमत होंगे या नहीं, वे उस record को बदल देते हैं जिसमें request था और उसकी जगह एक encrypted reply block रख देते हैं। अन्य सभी records को शामिल reply key और IV के साथ AES-256 encrypted [CRYPTO-AES](/docs/specs/cryptography/#aes) किया जाता है। प्रत्येक को समान reply key और reply IV के साथ अलग से AES/CBC encrypted किया जाता है। CBC mode को records के बीच जारी (chained) नहीं रखा जाता।

प्रत्येक hop केवल अपनी प्रतिक्रिया जानता है। यदि यह सहमत है, तो यह tunnel को समाप्ति तक बनाए रखेगा, भले ही इसका उपयोग न किया जाए, क्योंकि यह नहीं जान सकता कि अन्य सभी hops सहमत हुए या नहीं।

#### Reply Record विनिर्देश

वर्तमान hop अपना record पढ़ने के बाद, वे इसे एक reply record से बदल देते हैं जो यह बताता है कि वे tunnel में भाग लेने के लिए सहमत हैं या नहीं, और यदि वे नहीं हैं, तो वे अपनी अस्वीकृति का कारण वर्गीकृत करते हैं। यह केवल एक 1 byte value है, जहाँ 0x0 का मतलब है कि वे tunnel में भाग लेने के लिए सहमत हैं, और उच्च values का मतलब अस्वीकृति के उच्च स्तर हैं।

निम्नलिखित अस्वीकरण कोड परिभाषित हैं:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

अन्य कारणों को छुपाने के लिए, जैसे कि router बंद होना, peers से, वर्तमान implementation लगभग सभी rejections के लिए TUNNEL_REJECT_BANDWIDTH का उपयोग करती है।

उत्तर को AES session key के साथ एन्क्रिप्ट किया जाता है जो इसे एन्क्रिप्टेड ब्लॉक में दिया जाता है, और पूरे record size तक पहुंचने के लिए 495 बाइट्स के random data के साथ पैड किया जाता है। padding को status byte से पहले रखा जाता है:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
यह I2NP spec [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) में भी वर्णित है।

### Tunnel Build Message की तैयारी

एक नया Tunnel Build Message बनाते समय, सभी Build Request Records को पहले बनाया जाना चाहिए और ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) का उपयोग करके असममित रूप से एन्क्रिप्ट किया जाना चाहिए। फिर प्रत्येक रिकॉर्ड को AES [CRYPTO-AES](/docs/specs/cryptography/#aes) का उपयोग करके पथ में पहले के hops की reply keys और IVs के साथ पूर्व-निवारक रूप से डिक्रिप्ट किया जाता है। यह डिक्रिप्शन उल्टे क्रम में चलाया जाना चाहिए ताकि असममित रूप से एन्क्रिप्ट किया गया डेटा सही hop पर स्पष्ट रूप से दिखाई दे जब उनका पूर्ववर्ती इसे एन्क्रिप्ट करता है।

व्यक्तिगत अनुरोधों के लिए आवश्यक नहीं होने वाले अतिरिक्त रिकॉर्ड को निर्माता द्वारा केवल यादृच्छिक डेटा से भर दिया जाता है।

### Tunnel Build Message Delivery

outbound tunnels के लिए, delivery tunnel creator से सीधे first hop तक की जाती है, TunnelBuildMessage को इस तरह package करके जैसे कि creator tunnel में सिर्फ एक और hop हो। inbound tunnels के लिए, delivery एक existing outbound tunnel के माध्यम से की जाती है। outbound tunnel आमतौर पर उसी pool से होता है जिससे नई tunnel बनाई जा रही है। यदि उस pool में कोई outbound tunnel उपलब्ध नहीं है, तो एक outbound exploratory tunnel का उपयोग किया जाता है। startup के समय, जब अभी तक कोई outbound exploratory tunnel मौजूद नहीं है, तो एक fake 0-hop outbound tunnel का उपयोग किया जाता है।

### Tunnel Build Message Endpoint Handling

एक outbound tunnel के निर्माण के लिए, जब अनुरोध एक outbound endpoint तक पहुंचता है ('allow messages to anyone' flag द्वारा निर्धारित), hop को सामान्य रूप से संसाधित किया जाता है, record के स्थान पर एक reply को encrypt करते हुए और अन्य सभी records को encrypt करते हुए, लेकिन चूंकि TunnelBuildMessage को आगे भेजने के लिए कोई 'next hop' नहीं है, इसके बजाय यह encrypted reply records को एक TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) या VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) में रखता है (message का प्रकार और records की संख्या अनुरोध से मेल खानी चाहिए) और इसे request record में निर्दिष्ट reply tunnel को भेजता है। वह reply tunnel किसी भी अन्य संदेश की तरह Tunnel Build Reply Message को वापस tunnel creator को forward करता है [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)। Tunnel creator फिर इसे संसाधित करता है, जैसा कि नीचे वर्णित है।

Reply tunnel का चयन निर्माता द्वारा निम्न प्रकार से किया गया था: आमतौर पर यह उसी pool से एक inbound tunnel होता है जिससे नई outbound tunnel बनाई जा रही है। यदि उस pool में कोई inbound tunnel उपलब्ध नहीं है, तो एक inbound exploratory tunnel का उपयोग किया जाता है। स्टार्टअप के समय, जब अभी तक कोई inbound exploratory tunnel मौजूद नहीं है, तो एक नकली 0-hop inbound tunnel का उपयोग किया जाता है।

एक inbound tunnel के निर्माण के लिए, जब अनुरोध inbound endpoint (जिसे tunnel creator भी कहा जाता है) तक पहुंचता है, तो एक स्पष्ट Tunnel Build Reply Message उत्पन्न करने की आवश्यकता नहीं होती, और router प्रत्येक उत्तर को नीचे दिए गए अनुसार प्रक्रिया करता है।

### Tunnel Build Reply Message Processing

reply records को प्रोसेस करने के लिए, creator को बस प्रत्येक record को व्यक्तिगत रूप से AES decrypt करना होता है, peer के बाद tunnel में प्रत्येक hop की reply key और IV का उपयोग करके (विपरीत क्रम में)। यह तब reply को उजागर करता है जो निर्दिष्ट करता है कि वे tunnel में भाग लेने के लिए सहमत हैं या वे क्यों मना करते हैं। यदि वे सभी सहमत हैं, तो tunnel को created माना जाता है और इसका तुरंत उपयोग किया जा सकता है, लेकिन यदि कोई भी मना करता है, तो tunnel को discard कर दिया जाता है।

समझौते और अस्वीकरण प्रत्येक peer के profile [PEER-SELECTION](/docs/overview/tunnel-routing/) में दर्ज किए जाते हैं, जिनका उपयोग peer tunnel क्षमता के भविष्य के आकलन में किया जाता है।

## इतिहास और टिप्पणियाँ

यह रणनीति I2P मेलिंग सूची पर Michael Rogers, Matthew Toseland (toad), और jrandom के बीच predecessor attack के संबंध में हुई चर्चा के दौरान विकसित हुई। देखें [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html), [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)। यह रिलीज़ 0.6.1.10 में 2006-02-16 को पेश की गई थी, जो I2P में अंतिम बार कोई non-backward-compatible बदलाव किया गया था।

नोट्स:

- यह डिज़ाइन tunnel के भीतर दो शत्रुतापूर्ण peers को एक या अधिक request या reply records को tag करने से नहीं रोकता है ताकि यह पता लगाया जा सके कि वे समान tunnel के भीतर हैं, लेकिन ऐसा करना tunnel creator द्वारा reply पढ़ते समय detect किया जा सकता है, जिससे tunnel को अमान्य के रूप में चिह्नित किया जा सकता है।
- इस डिज़ाइन में asymmetrically encrypted section पर proof of work शामिल नहीं है, हालांकि 16 byte identity hash को आधे में काटा जा सकता है जिसमें बाद वाले को 2^64 cost तक के hashcash function से बदला जा सकता है।
- यह डिज़ाइन अकेले tunnel के भीतर दो शत्रुतापूर्ण peers को timing information का उपयोग करके यह निर्धारित करने से नहीं रोकता है कि वे समान tunnel में हैं या नहीं। batched और synchronized request delivery का उपयोग मदद कर सकता है (requests को batch करना और उन्हें (ntp-synchronized) मिनट पर भेजना)। हालांकि, ऐसा करने से peers requests को delay करके और बाद में tunnel में delay को detect करके 'tag' कर सकते हैं, हालांकि शायद छोटी window में deliver नहीं होने वाले requests को drop करना काम कर सकता है (हालांकि ऐसा करने के लिए clock synchronization की उच्च डिग्री की आवश्यकता होगी)। वैकल्पिक रूप से, शायद individual hops request को forward करने से पहले random delay inject कर सकते हैं?
- क्या request को tag करने के कोई nonfatal तरीके हैं?
- एक घंटे के resolution के साथ timestamp का उपयोग replay prevention के लिए किया जाता है। यह constraint release 0.9.16 तक enforce नहीं किया गया था।

## भविष्य का कार्य

- वर्तमान implementation में, originator अपने लिए एक record खाली छोड़ता है। इस प्रकार n records का एक message केवल n-1 hops का tunnel बना सकता है। यह inbound tunnels के लिए आवश्यक प्रतीत होता है (जहाँ अंतिम से पहले का hop अगले hop के लिए hash prefix देख सकता है), लेकिन outbound tunnels के लिए नहीं। इस पर शोध और सत्यापन किया जाना है। यदि anonymity से समझौता किए बिना शेष record का उपयोग संभव है, तो हमें ऐसा करना चाहिए।
- ऊपर दिए गए नोट्स में वर्णित संभावित tagging और timing attacks का और विश्लेषण।
- केवल VTBM का उपयोग करें; ऐसे पुराने peers का चयन न करें जो इसे समर्थित नहीं करते।
- Build Request Record में tunnel lifetime या expiration निर्दिष्ट नहीं है; प्रत्येक hop 10 मिनट बाद tunnel को expire कर देता है, जो एक network-wide hardcoded constant है। हम flag field में एक bit का उपयोग कर सकते हैं और lifetime या expiration निर्दिष्ट करने के लिए padding से 4 (या 8) bytes ले सकते हैं। Requestor केवल तभी इस विकल्प को निर्दिष्ट करेगा यदि सभी participants इसे समर्थित करते हों।

## संदर्भ

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - BuildRequestRecord specification
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - AES एन्क्रिप्शन
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - ElGamal एन्क्रिप्शन
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage

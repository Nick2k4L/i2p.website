---
title: "OBEP को 1-ऑफ-एन या एन-ऑफ-एन टनल्स के लिए डिलीवरी"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Open"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## अवलोकन

यह प्रस्ताव नेटवर्क प्रदर्शन में सुधार के लिए दो सुधारों को शामिल करता है:

- एकल विकल्प के बजाय वैकल्पिकों की सूची प्रदान करके OBEP को IBGW चयन का अधिकार सौंपना।

- OBEP पर मल्टीकास्ट पैकेट रूटिंग को सक्षम करना।


## प्रेरणा

सीधे कनेक्शन के मामले में, विचार OBEP को IBGWs से कनेक्ट होने के तरीके में लचीलापन देकर कनेक्शन की भीड़ को कम करना है। कई टनल निर्दिष्ट करने की क्षमता हमें OBEP पर मल्टीकास्ट लागू करने में सक्षम बनाती है (सभी निर्दिष्ट टनल को संदेश वितरित करके)।

इस प्रस्ताव के अधिकार सौंपने के हिस्से के एक वैकल्पिक तरीके के रूप में, एक LeaseSet हैश के माध्यम से भेजना हो सकता है, जैसा कि लक्ष्य [RouterIdentity](/docs/specs/common-structures/#common-structure-specification) हैश निर्दिष्ट करने की मौजूदा क्षमता है। इससे संदेश छोटा होगा और संभावित रूप से एक नया LeaseSet मिलेगा। हालाँकि:

1. इससे OBEP को लुकअप करने के लिए मजबूर किया जाएगा

2. LeaseSet फ्लडफिल पर प्रकाशित नहीं हो सकता है, इसलिए लुकअप विफल हो सकता है।

3. LeaseSet एन्क्रिप्टेड हो सकता है, इसलिए OBEP को लीज़ प्राप्त नहीं हो सकतीं।

4. LeaseSet निर्दिष्ट करने से OBEP को संदेश का [Destination](/docs/specs/common-structures/#destination) पता चल जाएगा, जिसे वे अन्यथा केवल नेटवर्क में सभी LeaseSets को स्क्रैप करके और लीज़ मिलान के लिए खोजकर ही पता लगा सकते थे।


## डिज़ाइन

मूल स्रोत (OBGW) एक का चयन करने के बजाय डिलीवरी निर्देशों [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) में लक्ष्य [Leases](/docs/specs/common-structures/#lease) के कुछ (सभी?) को रखेगा।

OBEP उनमें से एक का चयन करेगा जिसे वितरित करना है। OBEP उसे चुनेगा, यदि उपलब्ध हो, जिससे वह पहले से ही कनेक्टेड है या जिसके बारे में वह पहले से जानता है। इससे OBEP-IBGW पथ तेज़ और अधिक विश्वसनीय होगा, और समग्र नेटवर्क कनेक्शन कम होंगे।

हमारे पास TUNNEL-DELIVERY के लिए एक अप्रयुक्त डिलीवरी प्रकार (0x03) और फ्लैग्स में दो शेष बिट्स (0 और 1) हैं, जिनका उपयोग हम इन सुविधाओं को लागू करने के लिए कर सकते हैं।


## सुरक्षा प्रभाव

यह प्रस्ताव OBGW के लक्ष्य Destination या उनके NetDB के दृश्य के बारे में लीक होने वाली जानकारी की मात्रा में कोई परिवर्तन नहीं करता है:

- एक ऐसा प्रतिकूलता जो OBEP को नियंत्रित करता है और NetDB से LeaseSets को स्क्रैप कर रहा है, पहले से ही यह निर्धारित कर सकता है कि क्या एक विशेष Destination को संदेश भेजा जा रहा है, TunnelId / RouterIdentity जोड़ी के लिए खोज करके। अधिकतम, TMDI में कई Leases की उपस्थिति प्रतिकूलता के डेटाबेस में मिलान तेज़ी से खोजने में मदद कर सकती है।

- एक ऐसा प्रतिकूलता जो एक दुर्भावनापूर्ण Destination संचालित कर रहा है, पहले से ही एक जुड़ने वाले पीड़ित के NetDB के दृश्य के बारे में जानकारी प्राप्त कर सकता है, अलग-अलग फ्लडफिल पर अलग-अलग इनबाउंड टनल युक्त LeaseSets प्रकाशित करके, और यह देखकर कि OBGW किन टनल के माध्यम से कनेक्ट होता है। उनके दृष्टिकोण से, OBEP द्वारा टनल का चयन करना OBGW द्वारा चयन करने के कार्यात्मक रूप से समान है।

मल्टीकास्ट फ्लैग OBEPs को यह जानकारी लीक करता है कि OBGW मल्टीकास्टिंग कर रहा है। इससे उच्च-स्तरीय प्रोटोकॉल लागू करते समय विचार किए जाने वाले प्रदर्शन बनाम गोपनीयता के बीच एक व्यापार-ऑफ़ उत्पन्न होता है। एक वैकल्पिक फ्लैग होने के कारण, उपयोगकर्ता अपने अनुप्रयोग के लिए उचित निर्णय ले सकते हैं। हालाँकि, संगत अनुप्रयोगों के लिए यह डिफ़ॉल्ट व्यवहार होने के कुछ लाभ हो सकते हैं, क्योंकि विभिन्न अनुप्रयोगों द्वारा व्यापक उपयोग संदेश किस विशेष अनुप्रयोग से है, इस बारे में जानकारी लीक होने को कम करेगा।


## विनिर्देश

प्रथम फ्रैगमेंट डिलीवरी निर्देशों में निम्नलिखित परिवर्तन किए जाएंगे:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       Bit order: 76543210
       bits 6-5: delivery type
                 0x03 = TUNNELS
       bit 0: multicast? If 0, deliver to one of the tunnels
                         If 1, deliver to all of the tunnels
                         Set to 0 for compatibility with future uses if
                         delivery type is not TUNNELS

Count ::
       1 byte
       Optional, present if delivery type is TUNNELS
       2-255 - Number of id/hash pairs to follow

Tunnel ID :: TunnelId
To Hash ::
       36 bytes each
       Optional, present if delivery type is TUNNELS
       id/hash pairs

Total length: Typical length is:
       75 bytes for count 2 TUNNELS delivery (unfragmented tunnel message);
       79 bytes for count 2 TUNNELS delivery (first fragment)

Rest of delivery instructions unchanged
```


## संगतता

नए विनिर्देश को समझने की आवश्यकता वाले एकमात्र पीयर OBGWs और OBEPs हैं। इसलिए हम इस परिवर्तन को मौजूदा नेटवर्क के साथ संगत बना सकते हैं यदि इसका उपयोग लक्ष्य I2P संस्करण पर आधारित हो:

* OBGWs को आउटबाउंड टनल बनाते समय संगत OBEPs का चयन करना चाहिए, उनके [RouterInfo](/docs/specs/common-structures/#routerinfo) में घोषित I2P संस्करण के आधार पर।

* लक्ष्य संस्करण को घोषित करने वाले पीयर्स को नए फ्लैग्स को पार्स करने का समर्थन करना चाहिए, और निर्देशों को अमान्य के रूप में अस्वीकार नहीं करना चाहिए।


## संदर्भ

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)

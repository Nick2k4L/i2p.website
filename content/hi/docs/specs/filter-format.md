---
title: "एक्सेस फिल्टर फॉर्मेट"
description: "tunnel एक्सेस-कंट्रोल फ़िल्टर फ़ाइलों के लिए सिंटैक्स"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## अवलोकन

फ़िल्टर की परिभाषा स्ट्रिंग्स की एक सूची है। खाली लाइनें और `#` से शुरू होने वाली लाइनें अनदेखी कर दी जाती हैं। फ़िल्टर परिभाषा में परिवर्तन tunnel के पुनः आरंभ पर प्रभावी होते हैं।

प्रत्येक पंक्ति इनमें से किसी एक आइटम का प्रतिनिधित्व कर सकती है:

- इस फ़ाइल या किसी भी संदर्भित फ़ाइल में सूचीबद्ध नहीं किए गए किसी भी remote destinations पर लागू करने के लिए default threshold की परिभाषा
- किसी विशिष्ट remote destination पर लागू करने के लिए threshold की परिभाषा
- किसी फ़ाइल में सूचीबद्ध remote destinations पर लागू करने के लिए threshold की परिभाषा
- एक threshold की परिभाषा जो यदि उल्लंघन किया जाए तो अपराधी remote destination को निर्दिष्ट फ़ाइल में रिकॉर्ड किया जाएगा

परिभाषाओं का क्रम महत्वपूर्ण है। किसी दिए गए destination के लिए पहली threshold (चाहे वह स्पष्ट हो या फ़ाइल में सूचीबद्ध हो) उसी destination के लिए भविष्य की किसी भी threshold को override कर देती है, चाहे वह स्पष्ट हो या फ़ाइल में सूचीबद्ध हो।

## थ्रेसहोल्ड

एक threshold को remote destination द्वारा निर्दिष्ट सेकंड की संख्या में "breach" होने से पहले करने की अनुमति प्राप्त connection attempts की संख्या से परिभाषित किया जाता है। उदाहरण के लिए निम्नलिखित threshold definition `15/5` का अर्थ है कि समान remote destination को 5 सेकंड की अवधि में 14 connection attempts करने की अनुमति है। यदि यह समान अवधि के भीतर एक और attempt करता है, तो threshold का उल्लंघन हो जाएगा।

threshold format निम्नलिखित में से कोई एक हो सकता है:

- **संख्यात्मक परिभाषा** - सेकंड की संख्या के ऊपर कनेक्शन की संख्या - `15/5`, `30/60`, और इसी तरह। ध्यान दें कि यदि कनेक्शन की संख्या 1 है (जैसे `1/1` में) तो पहला कनेक्शन प्रयास उल्लंघन का परिणाम होगा।
- शब्द **`allow`**। यह threshold कभी भी उल्लंघित नहीं होती, यानी असीमित संख्या में कनेक्शन प्रयासों की अनुमति है।
- शब्द **`deny`**। यह threshold हमेशा उल्लंघित होती है, यानी कोई भी कनेक्शन प्रयास की अनुमति नहीं दी जाएगी।

### डिफ़ॉल्ट थ्रेशोल्ड

डिफ़ॉल्ट threshold किसी भी remote destinations पर लागू होती है जो definition में या referenced files में स्पष्ट रूप से सूचीबद्ध नहीं हैं। डिफ़ॉल्ट threshold सेट करने के लिए keyword `default` का उपयोग करें। निम्नलिखित डिफ़ॉल्ट thresholds के उदाहरण हैं:

```text
15/5 default
allow default
deny default
```
प्रति फिल्टर केवल एक default threshold की परिभाषा हो सकती है। यदि इसे छोड़ दिया जाता है, तो फिल्टर default रूप से अज्ञात connections को अनुमति देगा।

### स्पष्ट सीमाएं

स्पष्ट सीमाएं (Explicit thresholds) उस रिमोट destination पर लागू होती हैं जो परिभाषा में ही सूचीबद्ध है। उदाहरण:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### बल्क थ्रेशोल्ड

सुविधा के लिए एक फ़ाइल में destinations की सूची बनाए रखना और उन सभी के लिए एक साथ threshold परिभाषित करना संभव है। उदाहरण:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
ये फाइलें tunnel चलने के दौरान हाथ से संपादित की जा सकती हैं। इन फाइलों में किए गए परिवर्तनों को प्रभावी होने में 10 सेकंड तक का समय लग सकता है।

## रिकॉर्डर

Recorders रिमोट destination द्वारा किए गए कनेक्शन प्रयासों का ट्रैक रखते हैं, और यदि वह एक निश्चित threshold को पार करता है, तो उस destination को दी गई फ़ाइल में record किया जाता है। उदाहरण:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
एक recorder का उपयोग करके aggressive destinations को किसी दी गई file में record करना संभव है, और फिर उसी file का उपयोग करके उन्हें throttle करना। उदाहरण के लिए, निम्नलिखित snippet एक filter define करेगा जो शुरुआत में सभी connection attempts को allow करता है, लेकिन यदि कोई भी single destination 5 seconds में 30 attempts से अधिक करता है तो यह 5 seconds में 15 attempts तक throttle हो जाता है:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
एक tunnel में recorder का उपयोग करना संभव है जो एक file में लिखता है जो दूसरी tunnel को throttle करती है। कई tunnels में destinations के साथ same file को reuse करना संभव है। और बेशक, इन files को हाथ से edit करना भी संभव है।

यहाँ एक उदाहरण फ़िल्टर परिभाषा है जो डिफ़ॉल्ट रूप से कुछ throttling लागू करती है, `friends.txt` फ़ाइल में destinations के लिए कोई throttling नहीं, `enemies.txt` फ़ाइल में destinations से किसी भी कनेक्शन को मना करती है और किसी भी आक्रामक व्यवहार को `suspicious.txt` नामक फ़ाइल में रिकॉर्ड करती है:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```
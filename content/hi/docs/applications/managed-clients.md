---
title: "प्रबंधित क्लाइंट्स"
description: "router-managed applications कैसे ClientAppManager और port mapper के साथ integrate होते हैं"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## अवलोकन

Clients को router द्वारा सीधे शुरू किया जा सकता है जब वे [clients.config](/docs/specs/configuration/) फाइल में सूचीबद्ध होते हैं। ये clients "managed" या "unmanaged" हो सकते हैं। इसे ClientAppManager द्वारा संभाला जाता है। इसके अतिरिक्त, managed या unmanaged clients ClientAppManager के साथ पंजीकृत हो सकते हैं ताकि अन्य clients उनका reference प्राप्त कर सकें। Clients के लिए एक सरल Port Mapper सुविधा भी है जो आंतरिक port को पंजीकृत करने के लिए है जिसे अन्य clients देख सकते हैं।

---

## प्रबंधित क्लाइंट

रिलीज़ 0.9.4 के अनुसार, router managed clients का समर्थन करता है। Managed clients को ClientAppManager द्वारा instantiate और start किया जाता है। ClientAppManager client का reference बनाए रखता है और client की स्थिति पर अपडेट प्राप्त करता है। Managed clients को प्राथमिकता दी जाती है, क्योंकि state tracking को implement करना और client को start और stop करना बहुत आसान होता है। Client code में static references से बचना भी बहुत आसान होता है जो client के stop होने के बाद अत्यधिक memory usage का कारण बन सकते हैं। Managed clients को user द्वारा router console में start और stop किया जा सकता है, और router shutdown पर ये stop हो जाते हैं।

प्रबंधित clients या तो net.i2p.app.ClientApp या net.i2p.router.app.RouterApp interface को implement करते हैं। ClientApp interface को implement करने वाले clients को निम्नलिखित constructor प्रदान करना होगा:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
RouterApp इंटरफेस को implement करने वाले clients को निम्नलिखित constructor प्रदान करना होगा:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
प्रदान किए गए arguments clients.config फ़ाइल में निर्दिष्ट हैं।

---

## अप्रबंधित क्लाइंट्स

यदि clients.config फ़ाइल में निर्दिष्ट main class एक managed interface को implement नहीं करती है, तो इसे निर्दिष्ट arguments के साथ main() से शुरू किया जाएगा, और निर्दिष्ट arguments के साथ main() से बंद किया जाएगा। router कोई reference नहीं रखता, क्योंकि सभी interactions static main() method के माध्यम से होते हैं। console उपयोगकर्ता को सटीक state information प्रदान नहीं कर सकता।

---

## पंजीकृत क्लाइंट्स

Clients, चाहे वे managed हों या unmanaged, ClientAppManager के साथ register हो सकते हैं ताकि अन्य clients उनका reference प्राप्त कर सकें। Registration नाम के द्वारा होती है। ज्ञात registered clients हैं:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## पोर्ट मैपर

Router भी clients के लिए internal socket service खोजने के लिए एक सरल तंत्र प्रदान करता है, जैसे कि HTTP proxy। यह Port Mapper द्वारा प्रदान किया जाता है। पंजीकरण नाम के द्वारा होता है। जो clients पंजीकृत होते हैं वे आमतौर पर उस port पर एक internal emulated socket प्रदान करते हैं।

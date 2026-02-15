---
title: "UDP Trackers"
description: "I2P में UDP BitTorrent announces के लिए प्रोटोकॉल विनिर्देश"
slug: "udp-announces"
aliases:
  - "/hi/docs/specs/udp-bittorrent-announces"
  - "/hi/docs/specs/udp-bittorrent-announces/"
category: "प्रोटोकॉल"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## अवलोकन

यह specification I2P में UDP bittorrent announces के लिए protocol का दस्तावेजीकरण करती है। I2P में bittorrent की समग्र specification के लिए, देखें [BitTorrent over I2P](/docs/applications/bittorrent)। इस specification के विकास पर पृष्ठभूमि और अतिरिक्त जानकारी के लिए, देखें [Proposal 160](/proposals/160-udp-trackers)।

## डिज़ाइन

यह प्रस्ताव repliable datagram2, repliable datagram3, और raw datagrams का उपयोग करता है, जैसा कि [Datagrams](/docs/specs/datagrams) में परिभाषित है। Datagram2 और Datagram3 repliable datagrams के नए रूप हैं, जो [Proposal 163](/proposals/163-datagram2-datagram3) में परिभाषित हैं। Datagram2 replay resistance और offline signature support जोड़ता है। Datagram3 पुराने datagram format से छोटा है, लेकिन authentication के बिना।

### BEP 15

संदर्भ के लिए, [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) में परिभाषित संदेश प्रवाह निम्नलिखित है:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
कनेक्ट चरण IP पता स्पूफिंग को रोकने के लिए आवश्यक है। ट्रैकर एक कनेक्शन ID वापस करता है जिसका उपयोग क्लाइंट बाद की announces में करता है। यह कनेक्शन ID क्लाइंट में डिफ़ॉल्ट रूप से एक मिनट में और ट्रैकर में दो मिनट में समाप्त हो जाता है।

I2P मौजूदा UDP-सक्षम client code bases में आसान अपनाने के लिए BEP 15 के समान message flow का उपयोग करेगा: दक्षता के लिए, और नीचे चर्चा किए गए सुरक्षा कारणों से:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
यह streaming (TCP) announces की तुलना में संभावित रूप से बड़ी bandwidth की बचत प्रदान करता है। जबकि Datagram2 का आकार streaming SYN के लगभग समान है, raw response streaming SYN ACK से बहुत छोटा है। बाद के requests में Datagram3 का उपयोग होता है, और बाद के responses raw होते हैं।

announce requests Datagram3 हैं ताकि tracker को connection IDs से announce destination या hash के लिए एक बड़ी mapping table बनाए रखने की आवश्यकता न हो। इसके बजाय, tracker connection IDs को sender hash, वर्तमान timestamp (किसी interval के आधार पर), और एक secret value से cryptographically generate कर सकता है। जब एक announce request प्राप्त होता है, तो tracker connection ID को validate करता है, और फिर Datagram3 sender hash का उपयोग send target के रूप में करता है।

### कनेक्शन जीवनकाल

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) निर्दिष्ट करता है कि connection ID क्लाइंट पर एक मिनट में समाप्त हो जाता है, और tracker पर दो मिनट में। यह कॉन्फ़िगर नहीं किया जा सकता। यह संभावित दक्षता लाभों को सीमित करता है, जब तक कि क्लाइंट announces को batch में नहीं करते ताकि वे सभी एक मिनट की विंडो के भीतर हो सकें। i2psnark वर्तमान में announces को batch में नहीं करता; यह उन्हें फैलाता है, ट्रैफिक के bursts से बचने के लिए। बताया जाता है कि power users एक साथ हजारों torrents चला रहे हैं, और इतनी सारी announces को एक मिनट में burst करना वास्तविक नहीं है।

यहाँ, हम connect response को extend करने का प्रस्ताव करते हैं ताकि एक optional connection lifetime field जोड़ा जा सके। यदि यह present नहीं है तो default एक मिनट है। अन्यथा, seconds में specified lifetime का उपयोग client द्वारा किया जाएगा, और tracker connection ID को एक मिनट अधिक तक maintain करेगा।

### BEP 15 के साथ संगतता

यह डिज़ाइन [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) के साथ यथासंभव संगतता बनाए रखता है ताकि मौजूदा clients और trackers में आवश्यक परिवर्तनों को सीमित किया जा सके।

एकमात्र आवश्यक परिवर्तन announce response में peer info का format है। connect response में lifetime field का जोड़ना आवश्यक नहीं है लेकिन efficiency के लिए इसकी दृढ़ता से सिफारिश की जाती है, जैसा कि ऊपर बताया गया है।

### सुरक्षा विश्लेषण

UDP announce प्रोटोकॉल का एक महत्वपूर्ण लक्ष्य address spoofing को रोकना है। क्लाइंट का वास्तव में अस्तित्व होना चाहिए और एक वास्तविक leaseset को bundle करना चाहिए। Connect Response प्राप्त करने के लिए इसके पास inbound tunnels होने चाहिए। ये tunnels zero-hop हो सकते हैं और तुरंत बनाए जा सकते हैं, लेकिन इससे creator का पर्दाफाश हो जाएगा। यह प्रोटोकॉल उस लक्ष्य को पूरा करता है।

### समस्याएं

- यह protocol blinded destinations का समर्थन नहीं करता, लेकिन इसे इसके लिए विस्तारित किया जा सकता है। नीचे देखें।

## विनिर्देश

### प्रोटोकॉल और पोर्ट्स

Repliable Datagram2 I2CP protocol 19 का उपयोग करता है; repliable Datagram3 I2CP protocol 20 का उपयोग करता है; raw datagrams I2CP protocol 18 का उपयोग करते हैं। Requests Datagram2 या Datagram3 हो सकते हैं। Responses हमेशा raw होते हैं। पुराने repliable datagram ("Datagram1") format जो I2CP protocol 17 का उपयोग करता है, उसे requests या replies के लिए उपयोग नहीं किया जाना चाहिए; यदि ये request/reply ports पर प्राप्त हों तो इन्हें drop करना होगा। ध्यान दें कि Datagram1 protocol 17 अभी भी DHT protocol के लिए उपयोग किया जाता है।

अनुरोध announce URL से I2CP "to port" का उपयोग करते हैं; नीचे देखें। अनुरोध "from port" क्लाइंट द्वारा चुना जाता है, लेकिन यह गैर-शून्य होना चाहिए, और DHT द्वारा उपयोग किए जाने वाले पोर्ट से अलग होना चाहिए, ताकि प्रतिक्रियाओं को आसानी से वर्गीकृत किया जा सके। Trackers को गलत पोर्ट पर प्राप्त अनुरोधों को अस्वीकार करना चाहिए।

प्रतिक्रियाएं अनुरोध से I2CP "to port" का उपयोग करती हैं। अनुरोध का "from port" अनुरोध से "to port" होता है।

### Announce URL

announce URL format [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) में निर्दिष्ट नहीं है, लेकिन clearnet की तरह, UDP announce URLs इस रूप में होते हैं `udp://host:port/path`। path को नजरअंदाज किया जाता है और यह खाली हो सकता है, लेकिन आमतौर पर clearnet पर यह `/announce` होता है। `:port` भाग हमेशा मौजूद होना चाहिए, हालांकि, यदि `:port` भाग को छोड़ दिया गया है, तो 6969 का default I2CP port उपयोग करें, क्योंकि यह clearnet पर आम port है। cgi parameters `&a=b&c=d` भी जोड़े जा सकते हैं, जिन्हें प्रोसेस किया जा सकता है और announce request में प्रदान किया जा सकता है, देखें [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)। यदि कोई parameters या path नहीं हैं, तो trailing `/` को भी छोड़ा जा सकता है, जैसा कि [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) में निहित है।

### डेटाग्राम प्रारूप

सभी values network byte order (big endian) में भेजे जाते हैं। packets का बिल्कुल निश्चित आकार होने की अपेक्षा न करें। भविष्य के extensions packets का आकार बढ़ा सकते हैं।

#### कनेक्ट अनुरोध

Client से tracker तक। 16 bytes। Repliable Datagram2 होना चाहिए। [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) के समान। कोई बदलाव नहीं।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### कनेक्ट प्रतिक्रिया

Tracker से client तक। 16 या 18 bytes। Raw होना चाहिए। [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) के समान, सिवाय नीचे दिए गए नोट्स के।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
प्रतिक्रिया अनिवार्य रूप से I2CP "to port" पर भेजी जानी चाहिए जो अनुरोध "from port" के रूप में प्राप्त हुआ था।

lifetime फील्ड वैकल्पिक है और connection_id क्लाइंट की जीवनावधि को सेकंड में दर्शाता है। डिफ़ॉल्ट 60 है, और यदि निर्दिष्ट किया गया है तो न्यूनतम 60 है। अधिकतम 65535 है या लगभग 18 घंटे। tracker को connection_id को क्लाइंट की जीवनावधि से 60 सेकंड अधिक बनाए रखना चाहिए।

#### Announce Request

Client से tracker तक। न्यूनतम 98 bytes। Repliable Datagram3 होना आवश्यक है। [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) के समान है सिवाय नीचे दी गई बातों के।

connection_id वही है जो connect response में प्राप्त हुई है।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) से परिवर्तन:

- key को नज़रअंदाज़ किया जाता है
- IP address का उपयोग नहीं किया जाता
- port को शायद नज़रअंदाज़ किया जाता है लेकिन I2CP from port के समान होना चाहिए
- options सेक्शन, यदि मौजूद है, तो [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) में परिभाषित के अनुसार है

प्रतिक्रिया को I2CP "to port" पर भेजा जाना चाहिए जो अनुरोध "from port" के रूप में प्राप्त हुआ था। announce अनुरोध के port का उपयोग न करें।

#### घोषणा प्रतिक्रिया

Tracker से client तक। न्यूनतम 20 bytes। Raw होना चाहिए। [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) के समान, नीचे दिए गए नोट्स को छोड़कर।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) से परिवर्तन:

- 6-byte IPv4+port या 18-byte IPv6+port के बजाय, हम SHA-256 binary peer hashes के साथ 32-byte "compact responses" का गुणज वापस करते हैं। TCP compact responses की तरह, हम port शामिल नहीं करते।

प्रतिक्रिया को उस I2CP "to port" पर भेजा जाना चाहिए जो अनुरोध के "from port" के रूप में प्राप्त हुआ था। announce अनुरोध के port का उपयोग न करें।

I2P datagrams का अधिकतम आकार लगभग 64 KB का बहुत बड़ा होता है; हालांकि, विश्वसनीय वितरण के लिए, 4 KB से बड़े datagrams से बचना चाहिए। bandwidth दक्षता के लिए, trackers को शायद अधिकतम peers को लगभग 50 तक सीमित करना चाहिए, जो विभिन्न layers पर overhead से पहले लगभग 1600 byte packet के अनुरूप है, और fragmentation के बाद दो-tunnel-message payload सीमा के भीतर होना चाहिए।

BEP 15 की तरह, यहाँ भी पीयर addresses (BEP 15 के लिए IP/port, यहाँ hashes) की संख्या का कोई count शामिल नहीं है जो आगे आने वाला है। जबकि BEP 15 में इस पर विचार नहीं किया गया था, सभी zeros का एक end-of-peers marker परिभाषित किया जा सकता है यह इंगित करने के लिए कि पीयर info पूरी हो गई है और कुछ extension data आगे आता है।

ताकि भविष्य में extension संभव हो सके, clients को 32-byte के सभी शून्य hash को नज़रअंदाज़ करना चाहिए, और उसके बाद आने वाले किसी भी data को भी। Trackers को सभी शून्य hash से आने वाले announces को reject करना चाहिए, हालांकि वह hash पहले से ही Java routers द्वारा प्रतिबंधित है।

#### स्क्रैप

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) से scrape request/response इस specification द्वारा आवश्यक नहीं है, लेकिन यदि चाहें तो इसे implement किया जा सकता है, कोई changes की आवश्यकता नहीं। client को पहले एक connection ID प्राप्त करना होगा। scrape request हमेशा repliable Datagram3 होता है। scrape response हमेशा raw होता है।

#### त्रुटि प्रतिक्रिया

Tracker से client तक। न्यूनतम 8 bytes (यदि संदेश खाली है)। Raw होना चाहिए। [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) के समान। कोई बदलाव नहीं।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## एक्सटेंशन

Extension bits या version field शामिल नहीं हैं। Clients और trackers को packets का एक निश्चित आकार मानना नहीं चाहिए। इस तरह, compatibility को बिगाड़े बिना अतिरिक्त fields जोड़े जा सकते हैं। यदि आवश्यक हो तो [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) में परिभाषित extensions format की सिफारिश की जाती है।

connect response को एक वैकल्पिक connection ID lifetime जोड़ने के लिए संशोधित किया गया है।

यदि blinded destination समर्थन की आवश्यकता है, तो हम या तो announce request के अंत में blinded 35-byte address जोड़ सकते हैं, या [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) format का उपयोग करके responses में blinded hashes का अनुरोध कर सकते हैं (parameters TBD)। Blinded 35-byte peer addresses का set announce reply के अंत में, सभी-शून्य 32-byte hash के बाद जोड़ा जा सकता है।

## कार्यान्वयन दिशानिर्देश

गैर-एकीकृत, गैर-I2CP clients और trackers की चुनौतियों पर चर्चा के लिए ऊपर design section देखें।

### क्लाइंट्स

किसी दिए गए tracker hostname के लिए, एक client को HTTP URLs की बजाय UDP को प्राथमिकता देनी चाहिए, और दोनों को announce नहीं करना चाहिए।

मौजूदा BEP 15 समर्थन वाले क्लाइंट्स में केवल छोटे संशोधनों की आवश्यकता होनी चाहिए।

यदि कोई client DHT या अन्य datagram protocols का समर्थन करता है, तो उसे शायद request "from port" के रूप में एक अलग port चुनना चाहिए ताकि replies उस port पर वापस आएं और DHT messages के साथ मिश्रित न हों। Client को केवल replies के रूप में raw datagrams प्राप्त होते हैं। Trackers कभी भी client को repliable datagram2 नहीं भेजेंगे।

जिन क्लाइंट्स के पास opentrackers की डिफ़ॉल्ट लिस्ट है, उन्हें UDP URLs जोड़ने के लिए लिस्ट को अपडेट करना चाहिए, इसके बाद जब ज्ञात opentrackers के UDP समर्थन की पुष्टि हो जाए।

Clients अनुरोधों के पुनः प्रसारण को implement कर सकते हैं या नहीं भी कर सकते हैं। यदि पुनः प्रसारण implement किया गया है, तो कम से कम 15 सेकंड का प्रारंभिक timeout उपयोग करना चाहिए, और प्रत्येक पुनः प्रसारण के लिए timeout को दोगुना करना चाहिए (exponential backoff)।

क्लाइंट्स को एरर रिस्पांस प्राप्त करने के बाद वापस हटना चाहिए।

### ट्रैकर्स

मौजूदा BEP 15 समर्थन वाले trackers को केवल छोटे संशोधनों की आवश्यकता होनी चाहिए। यह specification 2014 के प्रस्ताव से इस बात में अलग है कि tracker को एक ही port पर repliable datagram2 और datagram3 के reception को समर्थन करना चाहिए।

tracker संसाधन आवश्यकताओं को कम करने के लिए, इस protocol को इस तरह डिज़ाइन किया गया है कि tracker को बाद की validation के लिए client hashes से connection IDs की mappings store करने की कोई आवश्यकता न हो। यह इसलिए संभव है क्योंकि announce request packet एक repliable Datagram3 packet है, इसलिए इसमें sender का hash शामिल होता है।

एक अनुशंसित कार्यान्वयन है:

- वर्तमान epoch को connection lifetime के resolution के साथ वर्तमान समय के रूप में परिभाषित करें, `epoch = now / lifetime`।
- एक cryptographic hash function `H(secret, clienthash, epoch)` परिभाषित करें जो 8 byte का output उत्पन्न करता है।
- सभी connections के लिए उपयोग किए जाने वाले random constant secret को generate करें।
- Connect responses के लिए, `connection_id = H(secret, clienthash, epoch)` generate करें
- Announce requests के लिए, वर्तमान epoch में प्राप्त connection ID को `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)` को verify करके validate करें

## संदर्भ

- **[BEP15]** [BEP 15 - UDP Tracker Protocol](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - UDP Tracker Protocol Extensions](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Datagrams Specification](/docs/specs/datagrams)
- **[Prop160]** [Proposal 160 - UDP Trackers](/proposals/160-udp-trackers)
- **[Prop163]** [Proposal 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [SAM v3 API](/docs/api/samv3)
- **[SPEC]** [BitTorrent over I2P](/docs/applications/bittorrent)

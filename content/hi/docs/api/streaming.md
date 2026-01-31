---
title: "स्ट्रीमिंग प्रोटोकॉल"
description: "अधिकांश I2P अनुप्रयोगों द्वारा उपयोग किया जाने वाला TCP-जैसा transport"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## अवलोकन {#overview}

streaming library तकनीकी रूप से "application" layer का हिस्सा है, क्योंकि यह एक मुख्य router फंक्शन नहीं है। हालांकि, व्यावहारिक रूप में, यह लगभग सभी मौजूदा I2P applications के लिए एक महत्वपूर्ण कार्य प्रदान करती है, I2P पर TCP-like streams प्रदान करके, और मौजूदा apps को आसानी से I2P में port करने की अनुमति देकर। client संचार के लिए दूसरी end-to-end transport library [datagram library](/docs/specs/datagrams) है।

streaming library एक परत है जो मुख्य [I2CP API](/docs/specs/i2cp) के ऊपर होती है जो विश्वसनीय, क्रमबद्ध, और प्रमाणित संदेशों की धाराओं को एक अविश्वसनीय, अव्यवस्थित, और अप्रमाणित संदेश परत पर संचालित करने की अनुमति देती है। ठीक TCP से IP के रिश्ते की तरह, इस streaming कार्यक्षमता में समझौतों और अनुकूलन की एक पूरी श्रृंखला उपलब्ध है, लेकिन उस कार्यक्षमता को मूल I2P कोड में एम्बेड करने के बजाय, इसे अपनी अलग library में विभाजित किया गया है ताकि TCP-जैसी जटिलताओं को अलग रखा जा सके और वैकल्पिक अनुकूलित implementations की अनुमति दी जा सके।

संदेशों की अपेक्षाकृत उच्च लागत को ध्यान में रखते हुए, streaming library का प्रोटोकॉल उन संदेशों को शेड्यूल करने और वितरित करने के लिए अनुकूलित किया गया है ताकि व्यक्तिगत संदेश में जितनी भी जानकारी उपलब्ध हो, उसे शामिल किया जा सके। उदाहरण के लिए, streaming library के माध्यम से प्रॉक्सी किए गए एक छोटे HTTP transaction को एक ही round trip में पूरा किया जा सकता है - पहला संदेश SYN, FIN, और छोटे HTTP request payload को bundle करता है, और reply में SYN, FIN, ACK, और HTTP response payload को bundle करता है। जबकि HTTP server को बताने के लिए एक अतिरिक्त ACK ट्रांसमिट करना होता है कि SYN/FIN/ACK प्राप्त हो गया है, स्थानीय HTTP proxy अक्सर browser को पूरा response तुरंत deliver कर सकता है।

streaming library TCP के एक abstraction के समान है, जिसमें इसकी sliding windows, congestion control algorithms (slow start और congestion avoidance दोनों), और सामान्य packet व्यवहार (ACK, SYN, FIN, RST, rto calculation, आदि) शामिल हैं।

streaming library एक मजबूत library है जो I2P पर संचालन के लिए अनुकूलित है। इसमें एक-चरणीय सेटअप है, और इसमें एक पूर्ण windowing implementation शामिल है।

## API {#api}

streaming library API Java applications को एक मानक socket paradigm प्रदान करता है। निचले स्तर का [I2CP](/docs/specs/i2cp) API पूरी तरह से छुपा हुआ है, सिवाय इसके कि applications streaming library के माध्यम से [I2CP parameters](/docs/specs/i2cp#options) पास कर सकते हैं, जिन्हें I2CP द्वारा व्याख्या किया जाता है।

streaming lib का मानक interface यह है कि application I2PSocketManagerFactory का उपयोग करके एक I2PSocketManager बनाए। फिर application socket manager से एक I2PSession मांगती है, जो [I2CP](/docs/specs/i2cp) के माध्यम से router के साथ connection का कारण बनेगा। उसके बाद application I2PSocket के साथ connections स्थापित कर सकती है या I2PServerSocket के साथ connections प्राप्त कर सकती है।

उपयोग का एक अच्छा उदाहरण देखने के लिए, i2psnark कोड देखें।

### विकल्प और डिफ़ॉल्ट {#options}

विकल्प और वर्तमान डिफ़ॉल्ट मान नीचे सूचीबद्ध हैं। विकल्प case-sensitive हैं और पूरे router के लिए, किसी विशेष client के लिए, या प्रति-कनेक्शन आधार पर किसी व्यक्तिगत socket के लिए सेट किए जा सकते हैं। कई मान सामान्य I2P स्थितियों में HTTP प्रदर्शन के लिए ट्यून किए गए हैं। अन्य एप्लिकेशन जैसे कि peer-to-peer सेवाओं को आवश्यकतानुसार संशोधन करने के लिए दृढ़ता से प्रोत्साहित किया जाता है, विकल्पों को सेट करके और उन्हें I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts) के कॉल के माध्यम से पास करके। समय के मान ms में हैं।

ध्यान दें कि उच्च-स्तरीय APIs, जैसे [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob), और [I2PTunnel](/docs/api/i2ptunnel), अपने स्वयं के defaults के साथ इन defaults को override कर सकते हैं। यह भी ध्यान दें कि कई विकल्प केवल incoming connections के लिए listening करने वाले servers पर लागू होते हैं।

रिलीज़ 0.9.1 के अनुसार, अधिकांश विकल्प, लेकिन सभी नहीं, एक सक्रिय socket manager या session पर बदले जा सकते हैं। विवरण के लिए javadocs देखें।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## प्रोटोकॉल विनिर्देश {#spec}

[Streaming Library Specification पृष्ठ देखें।](/docs/specs/streaming)

## कार्यान्वयन विवरण {#implementation}

### सेटअप {#setup}

प्रारंभकर्ता SYNCHRONIZE flag सेट के साथ एक packet भेजता है। इस packet में प्रारंभिक data भी हो सकता है। peer SYNCHRONIZE flag सेट के साथ एक packet के साथ जवाब देता है। इस packet में प्रारंभिक response data भी हो सकता है।

प्रारंभकर्ता SYNCHRONIZE प्रतिक्रिया प्राप्त करने से पहले, प्रारंभिक विंडो साइज़ तक, अतिरिक्त डेटा पैकेट भेज सकता है। इन पैकेट्स में भी send Stream ID फील्ड 0 पर सेट होगा। प्राप्तकर्ताओं को अज्ञात streams पर प्राप्त पैकेट्स को कम समय के लिए बफर करना चाहिए, क्योंकि वे SYNCHRONIZE पैकेट से पहले, क्रम से बाहर आ सकते हैं।

### MTU चयन और बातचीत {#mtu}

अधिकतम संदेश आकार (जिसे MTU / MRU भी कहते हैं) दो peers द्वारा समर्थित निम्न मान पर negotiate किया जाता है। चूंकि tunnel संदेशों को 1KB तक padded किया जाता है, एक खराब MTU चयन से बड़ी मात्रा में overhead हो सकता है। MTU को option i2p.streaming.maxMessageSize द्वारा निर्दिष्ट किया जाता है। वर्तमान default MTU 1730 को सामान्य स्थिति के लिए overhead सहित दो 1K I2NP tunnel संदेशों में सटीक रूप से फिट होने के लिए चुना गया था।

नोट: यह केवल payload का अधिकतम आकार है, header को शामिल नहीं करता।

नोट: ECIES कनेक्शन के लिए, जिनका ओवरहेड कम होता है, अनुशंसित MTU 1812 है। डिफ़ॉल्ट MTU सभी कनेक्शन के लिए 1730 ही रहता है, चाहे कोई भी key type का उपयोग हो। क्लाइंट्स को हमेशा की तरह भेजे गए और प्राप्त किए गए MTU में से न्यूनतम का उपयोग करना चाहिए। प्रस्ताव 155 देखें।

एक connection में पहला message में streaming layer द्वारा जोड़ा गया 387 byte (सामान्य) Destination शामिल होता है, और आमतौर पर 898 byte (सामान्य) LeaseSet, और Session keys, जो router द्वारा Garlic message में bundled होती हैं। (LeaseSet और Session Keys bundled नहीं होंगी यदि ElGamal Session पहले से established है)। इसलिए, एक complete HTTP request को single 1KB I2NP message में fit करने का लक्ष्य हमेशा प्राप्त नहीं होता। हालांकि, MTU का चयन, tunnel gateway processor में fragmentation और batching strategies के सावधानीपूर्वक implementation के साथ, network bandwidth, latency, reliability, और efficiency में महत्वपूर्ण कारक हैं, विशेषकर long-lived connections के लिए।

### डेटा अखंडता {#integrity}

डेटा अखंडता [I2CP layer](/docs/specs/i2cp#format) में लागू gzip CRC-32 checksum द्वारा सुनिश्चित की जाती है। streaming protocol में कोई checksum field नहीं है।

### पैकेट एनकैप्सुलेशन {#encapsulation}

प्रत्येक पैकेट को I2P के माध्यम से एक एकल संदेश के रूप में भेजा जाता है (या [Garlic Message](/docs/overview/garlic-routing) में एक व्यक्तिगत clove के रूप में)। Message encapsulation अंतर्निहित [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np), और [tunnel message](/docs/specs/tunnel-message) layers में लागू किया गया है। स्ट्रीमिंग प्रोटोकॉल में कोई पैकेट delimiter mechanism या payload length field नहीं है।

### वैकल्पिक विलंब {#delay}

डेटा पैकेट में एक वैकल्पिक delay field शामिल हो सकता है जो मिलीसेकंड में अनुरोधित देरी निर्दिष्ट करता है, इससे पहले कि receiver को पैकेट को ack करना चाहिए। वैध मान 0 से 60000 तक (शामिल) हैं। 0 का मान तत्काल ack का अनुरोध करता है। यह केवल सलाह के रूप में है, और receiver को थोड़ी देर करनी चाहिए ताकि अतिरिक्त पैकेट को एक ही ack के साथ acknowledge किया जा सके। कुछ implementations इस field में (measured RTT / 2) का सलाहकार मान शामिल कर सकते हैं। गैर-शून्य वैकल्पिक delay मानों के लिए, receiver को ack भेजने से पहले अधिकतम देरी को अधिकतम कुछ सेकंड तक सीमित करना चाहिए। 60000 से अधिक वैकल्पिक delay मान choking को दर्शाते हैं, नीचे देखें।

### ट्रांसमिट/रिसीव विंडोज़ और चोकिंग {#windows}

TCP headers में receive window को bytes में शामिल किया जाता है; हालांकि, streaming protocol अधिकतम receive window size को bytes या packets में exchange करने का कोई तरीका प्रदान नहीं करता। केवल एक सरल choke/unchoke indication होता है जो दर्शाता है कि receive buffer भरा हुआ है। प्रत्येक endpoint को far-end receive window का अपना अनुमान बनाए रखना चाहिए, चाहे वह bytes में हो या packets में। ध्यान दें कि यदि client application buffer को खाली करने में धीमा है तो receive buffer किसी भी window size पर overflow हो सकता है।

Java implementation में डिफ़ॉल्ट अधिकतम transmit और receive window साइज़ 128 packets है। जो implementations अधिकतम transmit window साइज़ को 128 से अधिक सेट करती हैं, उन्हें निम्नलिखित मुद्दों पर विचार करना चाहिए:

- Receive buffer overflow के कारण Java routers से CHOKE responses आने की संभावना बहुत अधिक है।
- बार-बार होने वाले overflows को कम करने के लिए Far-end receiver buffer size estimation को implement करना होगा (ऊपर देखें)
- CHOKE को सही तरीके से handle करना होगा (नीचे देखें)
- 256 से अधिक Max window sizes और भी error-prone हैं, क्योंकि nack count option field length एक byte है, जो maximum NACKs को 255 तक सीमित करता है। यह specification यह address नहीं करती कि 255 से अधिक NACKs होने पर क्या करना चाहिए। 256 से अधिक Max window sizes की सिफारिश नहीं की जाती।

receiver implementations के लिए अनुशंसित न्यूनतम buffer size 128 packets या 232 KB है (लगभग 128 * 1812)। I2P network latency, packet drops, और परिणामी congestion control के कारण, इस आकार का buffer शायद ही कभी भरता है। हालांकि, overflow का होना high-bandwidth "local loopback" (same-router) connections या local testing में बहुत अधिक संभावित है।

overflow conditions से जल्दी संकेत देने और आसानी से ठीक होने के लिए, streaming protocol में pushback के लिए एक सरल तंत्र है। यदि कोई packet 60001 या उससे अधिक मान के वैकल्पिक delay field के साथ प्राप्त होता है, तो यह "choking" या शून्य receive window का संकेत देता है। 60000 या उससे कम मान के वैकल्पिक delay field वाला packet "unchoking" का संकेत देता है। वैकल्पिक delay field के बिना packets choke/unchoke state को प्रभावित नहीं करते हैं।

choke होने के बाद, transmitter के unchoke होने तक डेटा के साथ कोई और packets नहीं भेजे जाने चाहिए, सिवाय कभी-कभार "probe" डेटा packets के जो संभावित खोए हुए unchoke packets की भरपाई के लिए होते हैं। choked endpoint को TCP की तरह probing को नियंत्रित करने के लिए "persist timer" शुरू करना चाहिए। unchoking endpoint को इस field के सेट के साथ कई packets भेजने चाहिए, या जब तक डेटा packets फिर से प्राप्त नहीं होते तब तक उन्हें नियमित रूप से भेजना जारी रखना चाहिए। unchoking का इंतज़ार करने का अधिकतम समय implementation पर निर्भर है। unchoke होने के बाद transmitter window size और congestion control strategy implementation पर निर्भर है।

### कन्जेशन कंट्रोल {#congestion}

स्ट्रीमिंग lib मानक स्लो-स्टार्ट (एक्सपोनेंशियल विंडो ग्रोथ) और कंजेशन अवॉइडेंस (लिनियर विंडो ग्रोथ) चरणों का उपयोग करती है, एक्सपोनेंशियल बैकऑफ के साथ। विंडोइंग और एक्नॉलेजमेंट पैकेट काउंट का उपयोग करते हैं, बाइट काउंट का नहीं।

### बंद करें {#close}

कोई भी packet, जिसमें SYNCHRONIZE flag set वाले भी शामिल हैं, में CLOSE flag भी भेजा जा सकता है। Connection तब तक बंद नहीं होता जब तक peer CLOSE flag के साथ जवाब नहीं देता। CLOSE packets में data भी हो सकता है।

### Ping / Pong {#ping}

I2CP layer (ICMP echo के समकक्ष) या datagrams में कोई ping function नहीं है। यह function streaming में प्रदान किया गया है। Pings और pongs को standard streaming packet के साथ जोड़ा नहीं जा सकता; यदि ECHO option सेट है, तो अधिकांश अन्य flags, options, ackThrough, sequenceNum, NACKs, आदि को नजरअंदाज कर दिया जाता है।

एक ping packet में ECHO, SIGNATURE_INCLUDED, और FROM_INCLUDED flags सेट होने चाहिए। sendStreamId शून्य से अधिक होना चाहिए, और receiveStreamId को नज़रअंदाज़ किया जाता है। sendStreamId किसी मौजूदा connection से मेल खा भी सकता है और नहीं भी।

एक pong packet में ECHO flag सेट होना चाहिए। sendStreamId शून्य होना चाहिए, और receiveStreamId ping से sendStreamId है। रिलीज़ 0.9.18 से पहले, pong packet में ping में शामिल कोई भी payload शामिल नहीं होता है।

रिलीज़ 0.9.18 के अनुसार, pings और pongs में एक payload हो सकता है। ping में payload, अधिकतम 32 bytes तक, pong में वापस किया जाता है।

Streaming को कॉन्फ़िगरेशन i2p.streaming.answerPings=false के साथ pongs भेजना अक्षम करने के लिए कॉन्फ़िगर किया जा सकता है।

### i2p.streaming.profile नोट्स {#profile}

यह विकल्प दो मान समर्थित करता है; 1=bulk और 2=interactive। यह विकल्प streaming library और/या router को अपेक्षित ट्रैफिक पैटर्न के बारे में संकेत प्रदान करता है।

"Bulk" का मतलब है उच्च bandwidth के लिए अनुकूलन करना, संभावित रूप से latency की कीमत पर। यह default है। "Interactive" का मतलब है कम latency के लिए अनुकूलन करना, संभावित रूप से bandwidth या दक्षता की कीमत पर। अनुकूलन रणनीतियां, यदि कोई हैं, implementation-dependent हैं, और इसमें streaming protocol के बाहर के परिवर्तन शामिल हो सकते हैं।

API संस्करण 0.9.63 तक, Java I2P किसी भी मान के लिए एक त्रुटि वापस करता था जो 1 (bulk) के अलावा हो और tunnel शुरू होने में विफल हो जाता था। API 0.9.64 से, Java I2P इस मान को नजरअंदाज करता है। API संस्करण 0.9.63 तक, i2pd इस विकल्प को नजरअंदाज करता था; यह API 0.9.64 से i2pd में लागू किया गया है।

जबकि streaming protocol में दूसरे छोर तक profile setting पास करने के लिए एक flag field शामिल है, यह किसी भी ज्ञात router में implemented नहीं है।

### Control Block साझाकरण {#sharing}

streaming lib "TCP" Control Block sharing का समर्थन करती है। यह तीन महत्वपूर्ण streaming lib parameters (window size, round trip time, round trip time variance) को एक ही remote peer के connections में साझा करती है। यह connection open/close time पर "temporal" sharing के लिए उपयोग होती है, connection के दौरान "ensemble" sharing के लिए नहीं ([RFC 2140](http://www.ietf.org/rfc/rfc2140.txt) देखें)। प्रत्येक ConnectionManager (यानी प्रत्येक local Destination) के लिए एक अलग share होता है ताकि एक ही router पर अन्य Destinations में कोई information leakage न हो। किसी दिए गए peer के लिए share data कुछ मिनट बाद expire हो जाता है। निम्नलिखित Control Block Sharing parameters प्रत्येक router के लिए सेट किए जा सकते हैं:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### अन्य पैरामीटर {#other}

निम्नलिखित पैरामीटर अनुशंसित डिफ़ॉल्ट हैं। डिफ़ॉल्ट भिन्न हो सकते हैं, कार्यान्वयन पर निर्भर:

- MIN_RESEND_DELAY = 100 ms (न्यूनतम RTO)
- MAX_RESEND_DELAY = 45 sec (अधिकतम RTO)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (न्यूनतम MTU)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (केवल RTT नमूना लेने से पहले मान्य) = 9 sec
- "alpha" ( RFC 6298 के अनुसार RTT dampening factor ) = 0.125
- "beta" ( RFC 6298 के अनुसार RTTDEV dampening factor ) = 0.25
- "K" ( RFC 6298 के अनुसार RTDEV multiplier ) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- अधिकतम RTT अनुमान: 60 sec

### इतिहास {#history}

I2P के लिए streaming library (स्ट्रीमिंग लाइब्रेरी) का विकास प्राकृतिक रूप से हुआ है - पहले mihi ने I2PTunnel के हिस्से के रूप में "mini streaming library" को implement किया, जो 1 message के window size तक सीमित था (अगला भेजने से पहले ACK की आवश्यकता), और फिर इसे एक generic streaming interface में refactor किया गया (TCP sockets को mirror करते हुए) और full streaming implementation को sliding window protocol के साथ deploy किया गया था तथा high bandwidth x delay product को ध्यान में रखते हुए optimizations के साथ। व्यक्तिगत streams maximum packet size और अन्य options को adjust कर सकती हैं। default message size को दो 1K I2NP tunnel messages में precisely fit करने के लिए चुना गया है, और यह lost messages को retransmit करने की bandwidth costs, तथा multiple messages की latency और overhead के बीच एक उचित tradeoff है।

## भविष्य का कार्य {#future}

streaming library का व्यवहार application-level performance पर गहरा प्रभाव डालता है, और इस प्रकार यह आगे के विश्लेषण के लिए एक महत्वपूर्ण क्षेत्र है।

- streaming lib पैरामीटर की अतिरिक्त tuning आवश्यक हो सकती है।
- अनुसंधान का एक और क्षेत्र streaming lib का NTCP और SSU transport layers के साथ interaction है। विवरण के लिए [NTCP discussion page](/docs/historical/ntcp-discussion) देखें।
- routing algorithms का streaming lib के साथ interaction प्रदर्शन को मजबूती से प्रभावित करता है। विशेष रूप से, pool में कई tunnels में messages का random distribution out-of-order delivery की उच्च डिग्री का कारण बनता है जिसके परिणामस्वरूप window sizes अन्यथा होने वाले आकार से छोटे होते हैं। router वर्तमान में एक single from/to destination pair के लिए messages को tunnels के एक consistent set के माध्यम से route करता है, जब तक tunnel expiration या delivery failure न हो। router के failure और tunnel selection algorithms की संभावित सुधारों के लिए समीक्षा की जानी चाहिए।
- पहले SYN packet में data receiver के MTU से अधिक हो सकता है।
- DELAY_REQUESTED field का अधिक उपयोग किया जा सकता है।
- short-lived streams पर duplicate initial SYNCHRONIZE packets को पहचाना और हटाया नहीं जा सकता है।
- retransmission में MTU न भेजें।
- Data तब तक भेजा जाता है जब तक outbound window full नहीं होता। (यानी no-Nagle या TCP_NODELAY) शायद इसके लिए एक configuration option होना चाहिए।
- zzz ने streaming library में wireshark-compatible (pcap) format में packets को log करने के लिए debug code जोड़ा है; प्रदर्शन का और विश्लेषण करने के लिए इसका उपयोग करें। streaming lib parameters को TCP fields में map करने के लिए format को enhancement की आवश्यकता हो सकती है।
- streaming lib को standard TCP (या शायद raw sockets के साथ null layer) से बदलने के प्रस्ताव हैं। यह दुर्भाग्य से streaming lib के साथ incompatible होगा लेकिन दोनों के प्रदर्शन की तुलना करना अच्छा होगा।

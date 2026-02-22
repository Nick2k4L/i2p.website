---
title: "SAM V3"
description: "गैर-Java I2P एप्लिकेशन के लिए सरल गुमनाम संदेश प्रोटोकॉल"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM, I2P के साथ बातचीत करने के लिए एक सरल client protocol है। SAM गैर-Java applications के लिए I2P network से जुड़ने की अनुशंसित protocol है, और यह कई router implementations द्वारा समर्थित है। Java applications को streaming या I2CP APIs का सीधे उपयोग करना चाहिए।

SAM version 3 को I2P release 0.7.3 (मई 2009) में पेश किया गया था और यह एक स्थिर और समर्थित इंटरफेस है। 3.1 भी स्थिर है और signature type विकल्प का समर्थन करता है, जिसकी दृढ़ता से सिफारिश की जाती है। अधिक हाल के 3.x versions उन्नत सुविधाओं का समर्थन करते हैं। ध्यान दें कि i2pd वर्तमान में अधिकांश 3.2 और 3.3 सुविधाओं का समर्थन नहीं करता है।

विकल्प: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (deprecated)](/docs/api/bob)। पुराने संस्करण: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2)।

## ज्ञात SAM लाइब्रेरीज

चेतावनी: इनमें से कुछ बहुत पुराने या असमर्थित हो सकते हैं। जब तक नीचे उल्लेख न किया गया हो, इनमें से कोई भी I2P प्रोजेक्ट द्वारा परीक्षित, समीक्षित, या अनुरक्षित नहीं है। अपना स्वयं का शोध करें।

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Library Name</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">Version</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">STREAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">DGRAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">RAW</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2psam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++, C wrapper</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2psam">github.com/i2p/i2psam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">gosam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/goSam">github.com/eyedeekay/goSam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">sam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/sam3">github.com/eyedeekay/sam3</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">onramp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/onramp">github.com/eyedeekay/onramp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">txi2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/str4d/txi2p">github.com/str4d/txi2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.socket</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/majestrate/i2p.socket">github.com/majestrate/i2p.socket</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/l-n-s/i2plib">github.com/l-n-s/i2plib</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib-fork</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/weko/i2plib-fork">codeberg.org/weko/i2plib-fork</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Py2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://i2pgit.org/robin/Py2p">i2pgit.org/robin/Py2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-rs</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2p-rs">github.com/i2p/i2p-rs</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">libsam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/libsam3">github.com/i2p/libsam3</a><br>(Maintained by the I2P project)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">mooni2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Lua</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/villain/mooni2p">notabug.org/villain/mooni2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">haskell-network-anonymous-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Haskell</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/solatis/haskell-network-anonymous-i2p">github.com/solatis/haskell-network-anonymous-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-sam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/diva.exchange/i2p-sam">codeberg.org/diva.exchange/i2p-sam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">node-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/redhog/node-i2p">github.com/redhog/node-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Jsam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/Jsam">github.com/eyedeekay/Jsam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">I2PSharp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/MohA39/I2PSharp">github.com/MohA39/I2PSharp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2pdotnet</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/SamuelFisher/i2pdotnet">github.com/SamuelFisher/i2pdotnet</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.rb</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Ruby</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/dryruby/i2p.rb">github.com/dryruby/i2p.rb</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">solitude</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/syvita/solitude">github.com/syvita/solitude</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Samty</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/acetone/samty">notabug.org/acetone/samty</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">bitcoin</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/bitcoin/bitcoin/blob/master/src/i2p.cpp">source (not a library, but good reference code)</a></td>
    </tr>
  </tbody>
</table>
## त्वरित प्रारंभ

एक बुनियादी TCP-only, peer-to-peer एप्लिकेशन को implement करने के लिए, client को निम्नलिखित commands का समर्थन करना होगा:

- `HELLO VERSION MIN=3.1 MAX=3.1` - बाकी सभी के लिए आवश्यक
- `DEST GENERATE SIGNATURE_TYPE=7` - हमारी private key और destination उत्पन्न करने के लिए
- `NAMING LOOKUP NAME=...` - .i2p addresses को destinations में बदलने के लिए
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - STREAM CONNECT और STREAM ACCEPT के लिए आवश्यक
- `STREAM CONNECT ID=... DESTINATION=...` - outgoing connections बनाने के लिए
- `STREAM ACCEPT ID=...` - incoming connections स्वीकार करने के लिए

## डेवलपर्स के लिए सामान्य मार्गदर्शन

### एप्लिकेशन डिज़ाइन

SAM sessions (या I2P के अंदर, tunnel pools या tunnels के समूह) को लंबे समय तक चलने के लिए डिज़ाइन किया गया है। अधिकांश एप्लिकेशन को केवल एक session की आवश्यकता होगी, जो स्टार्टअप पर बनाया जाता है और बंद करने पर बंद हो जाता है। I2P, Tor से अलग है, जहाँ circuits को तेज़ी से बनाया और त्यागा जा सकता है। अगर आप अपने एप्लिकेशन को एक या दो से अधिक समानांतर sessions उपयोग करने के लिए, या उन्हें तेज़ी से बनाने और त्यागने के लिए डिज़ाइन कर रहे हैं, तो सावधानी से सोचें और I2P developers से सलाह लें। अधिकांश threat models में हर connection के लिए एक अनूठे session की आवश्यकता नहीं होगी।

इसके अलावा, कृपया सुनिश्चित करें कि आपकी एप्लिकेशन सेटिंग्स (और router सेटिंग्स के बारे में उपयोगकर्ताओं को दिए गए निर्देश, या router डिफ़ॉल्ट यदि आप router बंडल करते हैं) के परिणामस्वरूप आपके उपयोगकर्ता नेटवर्क में उनके उपभोग से अधिक संसाधन योगदान करें। I2P एक peer-to-peer नेटवर्क है, और यदि कोई लोकप्रिय एप्लिकेशन नेटवर्क को स्थायी भीड़भाड़ में धकेल देती है तो नेटवर्क जीवित नहीं रह सकता।

### संगतता और परीक्षण

Java I2P और i2pd router implementations स्वतंत्र हैं और इनमें व्यवहार, फीचर समर्थन, और defaults में मामूली अंतर हैं। कृपया अपने एप्लिकेशन को दोनों routers के नवीनतम संस्करण के साथ परीक्षण करें।

i2pd SAM डिफ़ॉल्ट रूप से सक्षम है; Java I2P SAM नहीं है। अपने उपयोगकर्ताओं को Java I2P में SAM को सक्षम करने के तरीके के बारे में निर्देश प्रदान करें (router console में /configclients के माध्यम से), और/या उपयोगकर्ता को एक अच्छा error message प्रदान करें यदि प्रारंभिक कनेक्ट असफल हो जाता है, जैसे "सुनिश्चित करें कि I2P चल रहा है और SAM interface सक्षम है"।

Java I2P और i2pd router में tunnel की मात्रा के लिए अलग-अलग डिफ़ॉल्ट सेटिंग्स हैं। Java का डिफ़ॉल्ट 2 है और i2pd का डिफ़ॉल्ट 5 है। अधिकांश कम से मध्यम bandwidth और कम से मध्यम connection counts के लिए, 2 या 3 पर्याप्त है। Java I2P और i2pd router के साथ consistent performance पाने के लिए कृपया SESSION CREATE message में tunnel quantity specify करें। नीचे देखें।

डेवलपर्स को यह सुनिश्चित करने के लिए अधिक मार्गदर्शन के लिए कि आपका एप्लिकेशन केवल उन संसाधनों का उपयोग करे जिनकी इसे आवश्यकता है, कृपया [आपके एप्लिकेशन के साथ I2P को बंडल करने के लिए हमारी गाइड](/docs/applications/embedding) देखें।

### हस्ताक्षर और एन्क्रिप्शन प्रकार

I2P कई signature और encryption प्रकारों का समर्थन करता है। पिछड़ी संगतता के लिए, SAM पुराने और अकुशल प्रकारों को डिफ़ॉल्ट करता है, इसलिए सभी clients को नए प्रकारों को निर्दिष्ट करना चाहिए।

signature type को DEST GENERATE और SESSION CREATE (transient के लिए) commands में निर्दिष्ट किया जाता है। सभी clients को `SIGNATURE_TYPE=7` (Ed25519) सेट करना चाहिए।

एन्क्रिप्शन प्रकार SESSION CREATE कमांड में निर्दिष्ट किया जाता है। कई एन्क्रिप्शन प्रकारों की अनुमति है। क्लाइंट्स को या तो `i2cp.leaseSetEncType=4` (केवल ECIES-X25519 के लिए) या `i2cp.leaseSetEncType=4,0` (ECIES-X25519 और ElGamal के लिए, यदि संगतता आवश्यक है) सेट करना चाहिए।

## संस्करण 3 में परिवर्तन

### संस्करण 3.0 परिवर्तन

Version 3.0 को I2P release 0.7.3 में पेश किया गया था। SAM v2 ने एक ही I2P destination पर कई sockets को *समानांतर में* प्रबंधित करने का तरीका प्रदान किया था, यानी client को दूसरे socket पर data भेजने से पहले एक socket पर data सफलतापूर्वक भेजे जाने का इंतजार नहीं करना पड़ता था। लेकिन सभी data एक ही client-to-SAM socket के माध्यम से ट्रांजिट होता था, जिसे client के लिए प्रबंधित करना काफी जटिल था।

SAM v3 सॉकेट्स को एक अलग तरीके से प्रबंधित करता है: प्रत्येक *I2P socket* एक अनूठे client-to-SAM socket से मेल खाता है, जो संभालने में बहुत अधिक सरल है। यह [BOB](/docs/api/bob) के समान है।

SAM v3 I2P के माध्यम से datagrams भेजने के लिए एक UDP port भी प्रदान करता है, और I2P datagrams को client के datagram server पर वापस forward कर सकता है।

### संस्करण 3.1 परिवर्तन

Version 3.1 को Java I2P release 0.9.14 (जुलाई 2014) में पेश किया गया था। SAMv3.1 अनुशंसित न्यूनतम SAM implementation है क्योंकि इसमें SAMv3.0 की तुलना में बेहतर signature types का समर्थन है। i2pd भी अधिकांश 3.1 सुविधाओं का समर्थन करता है।

- DEST GENERATE और SESSION CREATE अब एक SIGNATURE_TYPE पैरामीटर का समर्थन करते हैं।
- HELLO VERSION में MIN और MAX पैरामीटर अब वैकल्पिक हैं।
- HELLO VERSION में MIN और MAX पैरामीटर अब एकल-अंक संस्करणों जैसे "3" का समर्थन करते हैं।
- RAW SEND अब bridge socket पर समर्थित है।

### संस्करण 3.2 परिवर्तन

Version 3.2 को Java I2P release 0.9.24 (जनवरी 2016) में पेश किया गया था। ध्यान दें कि i2pd वर्तमान में अधिकांश 3.2 सुविधाओं का समर्थन नहीं करता है।

#### I2CP पोर्ट और प्रोटोकॉल समर्थन

- SESSION CREATE विकल्प FROM_PORT और TO_PORT
- SESSION CREATE STYLE=RAW विकल्प PROTOCOL
- STREAM CONNECT, DATAGRAM SEND, और RAW SEND विकल्प FROM_PORT और TO_PORT
- RAW SEND विकल्प PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED, और फॉरवर्ड किए गए या प्राप्त streams और उत्तर देने योग्य datagrams में FROM_PORT और TO_PORT शामिल होते हैं
- RAW session विकल्प HEADER=true के कारण फॉरवर्ड किए गए raw datagrams के आगे PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn युक्त एक लाइन जोड़ी जाएगी
- पोर्ट 7655 के माध्यम से भेजे गए datagrams की पहली लाइन अब किसी भी 3.x संस्करण से शुरू हो सकती है
- पोर्ट 7655 के माध्यम से भेजे गए datagrams की पहली लाइन में FROM_PORT, TO_PORT, PROTOCOL में से कोई भी विकल्प हो सकता है
- RAW RECEIVED में PROTOCOL=nnn शामिल होता है

#### SSL और प्रमाणीकरण

- प्राधिकरण के लिए HELLO पैरामीटर में USER/PASSWORD। [नीचे](#authorization) देखें।
- AUTH कमांड के साथ वैकल्पिक प्राधिकरण कॉन्फ़िगरेशन। [नीचे](#authorization-configuration-sam-32-or-higher-optional-feature) देखें।
- कंट्रोल सॉकेट पर वैकल्पिक SSL/TLS समर्थन। [नीचे](#ssl) देखें।
- STREAM FORWARD विकल्प SSL=true

#### मल्टीथ्रेडिंग

- समान session ID पर समवर्ती pending STREAM ACCEPTs की अनुमति है।

#### कमांड लाइन पार्सिंग और Keepalive

- सत्र और socket को बंद करने के लिए वैकल्पिक commands QUIT, STOP और EXIT। [नीचे](#quitstopexitinvisible-sam-32-or-higher-optional-features) देखें।
- Command parsing UTF-8 को सही तरीके से handle करेगा
- Command parsing quotes के अंदर whitespace को विश्वसनीय तरीके से handle करता है
- एक backslash '\\' command line पर quotes को escape कर सकता है
- सिफारिश की जाती है कि server commands को upper case में map करे, telnet के माध्यम से testing में आसानी के लिए।
- Empty option values जैसे PROTOCOL या PROTOCOL= की अनुमति हो सकती है, implementation पर निर्भर।
- Keepalive के लिए PING/PONG। नीचे देखें।
- Server HELLO या बाद की commands के लिए timeouts implement कर सकते हैं, implementation पर निर्भर।

### संस्करण 3.3 परिवर्तन

Version 3.3 को Java I2P release 0.9.25 (मार्च 2016) में पेश किया गया था। ध्यान दें कि i2pd वर्तमान में अधिकांश 3.3 सुविधाओं का समर्थन नहीं करता है।

- एक ही session का उपयोग streams, datagrams, और raw के लिए एक साथ किया जा सकता है। आने वाले packets और streams को I2P protocol और to-port के आधार पर route किया जाएगा। [नीचे PRIMARY section देखें](#sam-primary-sessions-v33-and-higher)।
- DATAGRAM SEND और RAW SEND अब options SEND_TAGS, TAG_THRESHOLD, EXPIRES, और SEND_LEASESET को support करते हैं। [नीचे datagram sending section देखें](#sending-repliable-or-raw-datagrams)।

## संस्करण 3 प्रोटोकॉल

### Simple Anonymous Messaging (SAM) संस्करण 3.3 विशिष्टता अवलोकन

क्लाइंट एप्लिकेशन SAM bridge से बात करता है, जो सभी I2P कार्यक्षमता को संभालता है (virtual streams के लिए [streaming library](/docs/api/streaming) का उपयोग करके, या datagrams के लिए सीधे [I2CP](/docs/protocol/i2cp) का उपयोग करके)।

डिफ़ॉल्ट रूप से, client-to-SAM bridge संचार अनएन्क्रिप्टेड और अप्रमाणित होता है। SAM bridge SSL/TLS कनेक्शन का समर्थन कर सकता है; कॉन्फ़िगरेशन और implementation विवरण इस specification के दायरे से बाहर हैं। SAM 3.2 के अनुसार, प्रारंभिक handshake में वैकल्पिक authentication user/password पैरामीटर समर्थित हैं और bridge द्वारा आवश्यक हो सकते हैं।

I2P संचार कई अलग रूप ले सकता है:

- [Virtual streams](/docs/api/streaming)
- [Repliable और authenticated datagrams](/docs/specs/datagrams#repliable) (FROM फील्ड के साथ संदेश)
- [Anonymous datagrams](/docs/specs/datagrams#raw) (raw anonymous संदेश)
- [Datagram2](/docs/specs/datagrams#datagram2) (एक नया repliable और authenticated प्रारूप)
- [Datagram3](/docs/specs/datagrams#datagram3) (एक नया repliable लेकिन unauthenticated प्रारूप)

I2P संचार I2P sessions द्वारा समर्थित होते हैं, और प्रत्येक I2P session एक पते (जिसे destination कहा जाता है) से जुड़ा होता है। एक I2P session ऊपर दिए गए तीन प्रकारों में से किसी एक के साथ जुड़ा होता है, और दूसरे प्रकार के संचार को संभाल नहीं सकता, जब तक कि [PRIMARY sessions](#sam-primary-sessions-v33-and-higher) का उपयोग न किया जाए।

### एन्कोडिंग और एस्केपिंग

ये सभी SAM संदेश एक ही पंक्ति में भेजे जाते हैं, जो newline character (\\n) से समाप्त होते हैं। SAM 3.2 से पहले, केवल 7-bit ASCII समर्थित था। SAM 3.2 के बाद से, encoding UTF-8 होनी चाहिए। कोई भी UTF8-encoded keys या values काम करनी चाहिए।

नीचे दी गई इस specification में दिखाया गया formatting केवल readability के लिए है, और जबकि प्रत्येक message में पहले दो words अपने specific order में रहने चाहिए, key=value pairs की ordering बदल सकती है (जैसे "ONE TWO A=B C=D" या "ONE TWO C=D A=B" दोनों पूर्णतः valid constructions हैं)। इसके अतिरिक्त, protocol case-sensitive है। निम्नलिखित में, message examples से पहले "->" client द्वारा SAM bridge को भेजे गए messages के लिए, और "<-" SAM bridge द्वारा client को भेजे गए messages के लिए लगाया गया है।

मूल command या response line निम्नलिखित रूपों में से एक लेती है:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND बिना SUBCOMMAND के केवल SAM 3.2 में कुछ नए कमांड्स के लिए समर्थित है।

Key=value जोड़ों को एक ही स्पेस से अलग किया जाना चाहिए। (SAM 3.2 से, कई स्पेस की अनुमति है) यदि values में स्पेस हैं तो उन्हें double quotes में enclosed करना चाहिए, उदाहरण के लिए key="long value text"। (SAM 3.2 से पहले, यह कुछ implementations में विश्वसनीय रूप से काम नहीं करता था)

SAM 3.2 से पहले, कोई escaping mechanism नहीं था। SAM 3.2 के बाद से, double quotes को backslash '\\' के साथ escape किया जा सकता है और एक backslash को दो backslashes '\\\\' के रूप में दर्शाया जा सकता है।

### खाली मान

SAM 3.2 के अनुसार, खाली विकल्प मान जैसे KEY, KEY=, या KEY="" की अनुमति हो सकती है, यह implementation पर निर्भर करता है।

### केस संवेदनशीलता

प्रोटोकॉल, जैसा कि निर्दिष्ट है, case-sensitive है। यह अनुशंसित है लेकिन आवश्यक नहीं है कि सर्वर commands को upper case में map करे, telnet के माध्यम से testing में आसानी के लिए। इससे उदाहरण के लिए, "hello version" काम कर सकेगा। यह implementation-dependent है। keys या values को upper case में map न करें, क्योंकि इससे [I2CP](/docs/protocol/i2cp) options भ्रष्ट हो जाएंगे।

### SAM कनेक्शन हैंडशेक

SAM संचार तब तक नहीं हो सकता जब तक कि client और bridge एक protocol version पर सहमत न हो जाएं, जो client द्वारा HELLO भेजने और bridge द्वारा HELLO REPLY भेजने से होता है:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
और

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
संस्करण 3.1 (I2P 0.9.14) से, MIN और MAX पैरामीटर वैकल्पिक हैं। SAM हमेशा MIN और MAX बाधाओं के अनुसार उच्चतम संभावित संस्करण वापस करेगा, या यदि कोई बाधाएं नहीं दी गई हैं तो वर्तमान server संस्करण वापस करेगा।

यदि SAM bridge को कोई उपयुक्त version नहीं मिलता, तो यह इस प्रकार उत्तर देता है:

```
<- HELLO REPLY RESULT=NOVERSION
```
यदि कोई त्रुटि हुई, जैसे कि खराब अनुरोध प्रारूप, तो यह इसके साथ उत्तर देता है:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

सर्वर का control socket वैकल्पिक रूप से SSL/TLS समर्थन प्रदान कर सकता है, जैसा कि सर्वर और client पर कॉन्फ़िगर किया गया है। implementations अन्य transport layers भी प्रदान कर सकते हैं; यह protocol definition के दायरे से बाहर है।

#### प्राधिकरण

प्राधिकरण के लिए, क्लाइंट HELLO पैरामीटर में USER="xxx" PASSWORD="yyy" जोड़ता है। उपयोगकर्ता और पासवर्ड के लिए डबल कोट्स की सिफारिश की जाती है लेकिन आवश्यक नहीं है। उपयोगकर्ता या पासवर्ड के अंदर एक डबल कोट को बैकस्लैश के साथ एस्केप किया जाना चाहिए। असफलता पर सर्वर I2P_ERROR और एक संदेश के साथ उत्तर देगा। यह सिफारिश की जाती है कि किसी भी SAM सर्वर पर SSL सक्षम हो जहां प्राधिकरण आवश्यक है।

#### टाइमआउट

सर्वर HELLO या बाद की commands के लिए timeouts लागू कर सकते हैं, यह implementation पर निर्भर करता है। Clients को connect करने के बाद तुरंत HELLO और अगली command भेजनी चाहिए।

यदि HELLO प्राप्त होने से पहले timeout हो जाता है, तो bridge इसके साथ उत्तर देता है:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
और फिर डिस्कनेक्ट हो जाता है।

यदि HELLO प्राप्त होने के बाद लेकिन अगले command से पहले timeout हो जाता है, तो bridge इसके साथ जवाब देता है:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
और फिर डिस्कनेक्ट हो जाता है।

### I2CP पोर्ट्स और प्रोटोकॉल

SAM 3.2 के अनुसार, [I2CP](/docs/protocol/i2cp) पोर्ट और प्रोटोकॉल को SAM क्लाइंट भेजने वाले द्वारा निर्दिष्ट किया जा सकता है ताकि वे [I2CP](/docs/protocol/i2cp) तक पहुंचाए जा सकें, और SAM bridge प्राप्त [I2CP](/docs/protocol/i2cp) पोर्ट और प्रोटोकॉल जानकारी को SAM क्लाइंट तक पहुंचाएगा।

FROM_PORT और TO_PORT के लिए, वैध सीमा 0-65535 है, और डिफ़ॉल्ट 0 है।

PROTOCOL के लिए, जो केवल RAW के लिए निर्दिष्ट किया जा सकता है, वैध सीमा 0-255 है, और डिफ़ॉल्ट 18 है।

SESSION commands के लिए, निर्दिष्ट पोर्ट्स और प्रोटोकॉल उस session के लिए डिफॉल्ट हैं। व्यक्तिगत streams या datagrams के लिए, निर्दिष्ट पोर्ट्स और प्रोटोकॉल session defaults को override करते हैं। प्राप्त streams या datagrams के लिए, संकेतित पोर्ट्स और प्रोटोकॉल [I2CP](/docs/protocol/i2cp) से प्राप्त हुए अनुसार हैं।

#### मानक IP से महत्वपूर्ण अंतर

I2CP पोर्ट I2P sockets और datagrams के लिए हैं। इनका SAM से कनेक्ट होने वाले आपके स्थानीय sockets से कोई संबंध नहीं है।

- Port 0 मान्य है और इसका विशेष अर्थ है।
- Ports 1-1023 विशेष या privileged नहीं हैं।
- Servers डिफ़ॉल्ट रूप से port 0 पर सुनते हैं, जिसका मतलब है "सभी ports"।
- Clients डिफ़ॉल्ट रूप से port 0 पर भेजते हैं, जिसका मतलब है "कोई भी port"।
- Clients डिफ़ॉल्ट रूप से port 0 से भेजते हैं, जिसका मतलब है "अनिर्दिष्ट"।
- Servers में port 0 पर एक service सुन रही हो सकती है और अन्य services उच्चतर ports पर सुन रही हो सकती हैं। यदि ऐसा है, तो port 0 service डिफ़ॉल्ट है, और इससे कनेक्ट किया जाएगा यदि आने वाला socket या datagram port किसी अन्य service से मैच नहीं करता।
- अधिकांश I2P destinations पर केवल एक service चल रही होती है, इसलिए आप डिफ़ॉल्ट्स का उपयोग कर सकते हैं, और I2CP port कॉन्फ़िगरेशन को नज़रअंदाज़ कर सकते हैं।
- I2CP ports निर्दिष्ट करने के लिए SAM 3.2 या 3.3 आवश्यक है।
- यदि आपको I2CP ports की आवश्यकता नहीं है, तो आपको SAM 3.2 या 3.3 की आवश्यकता नहीं है; 3.1 पर्याप्त है।
- Protocol 0 मान्य है और इसका मतलब है "कोई भी protocol"। यह अनुशंसित नहीं है, और शायद काम नहीं करेगा।
- I2P sockets एक आंतरिक connection ID द्वारा ट्रैक किए जाते हैं। इसलिए, यह आवश्यक नहीं है कि dest:port:dest:port:protocol का 5-tuple अद्वितीय हो। उदाहरण के लिए, दो destinations के बीच समान ports के साथ कई sockets हो सकते हैं। Clients को आउटबाउंड कनेक्शन के लिए "मुफ्त port" चुनने की आवश्यकता नहीं है।

यदि आप कई subsessions के साथ SAMv3.3 एप्लिकेशन डिज़ाइन कर रहे हैं, तो ports और protocols का प्रभावी उपयोग कैसे करें इस पर सावधानीपूर्वक विचार करें। अधिक जानकारी के लिए [I2CP](/docs/protocol/i2cp) specification देखें।

### SAM सेशन

एक SAM सेशन तब बनाया जाता है जब कोई client SAM bridge के लिए एक socket खोलता है, handshake संचालित करता है, और SESSION CREATE संदेश भेजता है, और सेशन तब समाप्त हो जाता है जब socket डिस्कनेक्ट हो जाता है।

प्रत्येक पंजीकृत I2P Destination विशिष्ट रूप से एक session ID (या nickname) के साथ जुड़ा होता है। Session ID, PRIMARY sessions के लिए subsession ID सहित, SAM server पर globally unique होना चाहिए। अन्य clients के साथ संभावित ID टकराव को रोकने के लिए, सबसे अच्छा अभ्यास यह है कि client ID को randomly generate करे।

प्रत्येक सेशन विशिष्ट रूप से इससे जुड़ा होता है:

- वह socket जिससे client session बनाता है
- इसकी ID (या nickname)

#### सत्र निर्माण अनुरोध

सत्र निर्माण संदेश केवल इन रूपों में से एक का उपयोग कर सकता है (अन्य रूपों के माध्यम से प्राप्त संदेशों का उत्तर एक त्रुटि संदेश के साथ दिया जाता है):

```
->  SESSION CREATE
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, for DESTINATION=TRANSIENT only, default DSA_SHA1
          [PORT=$port]                         # Required for DATAGRAM* RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [HEADER={true,false}]                # SAM 3.2 or higher only, for STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
DESTINATION निर्दिष्ट करता है कि संदेश/स्ट्रीम भेजने और प्राप्त करने के लिए कौन सा destination का उपयोग किया जाना चाहिए। $privkey [Destination](/docs/specs/common-structures#type_Destination) के concatenation का base 64 है जिसके बाद [Private Key](/docs/specs/common-structures#type_PrivateKey) है फिर [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey) है, वैकल्पिक रूप से [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) के बाद, जो signature type के आधार पर binary में 663 या अधिक bytes और base 64 में 884 या अधिक bytes है। binary format Private Key File में निर्दिष्ट है। नीचे Destination Key Generation अनुभाग में [Private Key](/docs/specs/common-structures#type_PrivateKey) के बारे में अतिरिक्त नोट्स देखें।

यदि signing private key सभी शून्य हैं, तो [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) अनुभाग इसके बाद आता है। Offline signatures केवल STREAM और RAW sessions के लिए समर्थित हैं। Offline signatures को DESTINATION=TRANSIENT के साथ नहीं बनाया जा सकता। Offline signature अनुभाग का प्रारूप है:

1. समाप्ति timestamp (4 bytes, big endian, epoch से सेकंड, 2106 में roll over होता है)
2. transient Signing Public Key का Sig type (2 bytes, big endian)
3. Transient Signing Public key (लंबाई transient sig type के अनुसार निर्दिष्ट)
4. offline key द्वारा उपरोक्त तीन fields का Signature (लंबाई destination sig type के अनुसार निर्दिष्ट)
5. Transient Signing Private key (लंबाई transient sig type के अनुसार निर्दिष्ट)

यदि destination को TRANSIENT के रूप में निर्दिष्ट किया गया है, तो SAM bridge एक नया destination बनाता है। version 3.1 (I2P 0.9.14) के अनुसार, यदि destination TRANSIENT है, तो एक वैकल्पिक parameter SIGNATURE_TYPE समर्थित है। SIGNATURE_TYPE value कोई भी नाम (जैसे ECDSA_SHA256_P256, case insensitive) या संख्या (जैसे 1) हो सकती है जो [Key Certificates](/docs/specs/common-structures#type_Certificate) द्वारा समर्थित है। default DSA_SHA1 है, जो आप नहीं चाहते। अधिकांश applications के लिए, कृपया SIGNATURE_TYPE=7 निर्दिष्ट करें।

$nickname क्लाइंट की पसंद है। कोई whitespace की अनुमति नहीं है।

दिए गए अतिरिक्त विकल्प I2P सत्र कॉन्फ़िगरेशन में पास किए जाते हैं यदि वे SAM bridge द्वारा व्याख्यायित नहीं होते हैं (जैसे outbound.length=0)।

Java I2P और i2pd router में tunnel की मात्रा के लिए अलग-अलग डिफ़ॉल्ट सेटिंग्स हैं। Java का डिफ़ॉल्ट 2 है और i2pd का डिफ़ॉल्ट 5 है। अधिकांश कम से मध्यम bandwidth और कम से मध्यम connection counts के लिए, 2 या 3 पर्याप्त है। कृपया Java I2P और i2pd router के साथ consistent performance प्राप्त करने के लिए SESSION CREATE message में tunnel quantities निर्दिष्ट करें, options जैसे inbound.quantity=3 outbound.quantity=3 का उपयोग करके। ये और अन्य options [नीचे दिए गए लिंक में documented हैं](#tunnel-i2cp-and-streaming-options)।

SAM bridge स्वयं पहले से ही यह कॉन्फ़िगर होना चाहिए कि उसे किस router के माध्यम से I2P पर संचार करना चाहिए (हालांकि यदि आवश्यकता हो तो override प्रदान करने का कोई तरीका हो सकता है, जैसे i2cp.tcp.host=localhost और i2cp.tcp.port=7654)।

#### सेशन निर्माण प्रतिक्रिया

session create message प्राप्त करने के बाद, SAM bridge एक session status message के साथ उत्तर देगा, जैसा कि निम्नलिखित है:

यदि निर्माण सफल था:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
$privkey [Destination](/docs/specs/common-structures#type_Destination) के बाद [Private Key](/docs/specs/common-structures#type_PrivateKey) के बाद [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey) के संयोजन (concatenation) का base 64 है, जिसके बाद वैकल्पिक रूप से [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) हो सकता है। यह signature type के आधार पर binary में 663 या अधिक bytes और base 64 में 884 या अधिक bytes का होता है। binary format Private Key File में निर्दिष्ट है।

यदि SESSION CREATE में सभी शून्य की signing private key और एक [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) सेक्शन शामिल था, तो SESSION STATUS reply में समान फॉर्मेट में समान डेटा शामिल होगा। विवरण के लिए ऊपर SESSION CREATE सेक्शन देखें।

यदि nickname पहले से ही किसी session के साथ जुड़ा हुआ है:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
यदि गंतव्य पहले से उपयोग में है:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
यदि गंतव्य एक वैध निजी destination key नहीं है:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
यदि कोई अन्य त्रुटि हुई है:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
यदि यह ठीक नहीं है, तो MESSAGE में मानव-पठनीय जानकारी होनी चाहिए कि सत्र क्यों नहीं बनाया जा सका।

ध्यान दें कि router SESSION STATUS के साथ जवाब देने से पहले tunnels का निर्माण करता है। इसमें कई सेकंड लग सकते हैं, या router के startup के समय या गंभीर network congestion के दौरान एक मिनट या अधिक समय लग सकता है। यदि असफल होता है, तो router कई मिनट तक failure message के साथ जवाब नहीं देगा। response की प्रतीक्षा करते समय कम timeout न रखें। tunnel build की प्रक्रिया चल रही हो तो session को छोड़कर दोबारा कोशिश न करें।

SAM सत्र उस socket के साथ जीते और मरते हैं जिससे वे जुड़े होते हैं। जब socket बंद हो जाता है, तो सत्र समाप्त हो जाता है, और उस सत्र का उपयोग करने वाली सभी संचार एक ही समय में समाप्त हो जाती है। और इसके विपरीत, जब सत्र किसी भी कारण से समाप्त हो जाता है, तो SAM bridge socket को बंद कर देता है।

### SAM Virtual Streams

वर्चुअल स्ट्रीम्स को विश्वसनीय रूप से और क्रम में भेजे जाने की गारंटी है, जैसे ही उपलब्ध होता है तुरंत असफलता और सफलता की सूचना के साथ।

Streams दो I2P destinations के बीच द्विदिशीय संचार sockets हैं, लेकिन इनका खोलना उनमें से किसी एक द्वारा अनुरोध करना होता है। इसके बाद, CONNECT commands का उपयोग SAM client द्वारा ऐसे अनुरोध के लिए किया जाता है। FORWARD / ACCEPT commands का उपयोग SAM client द्वारा तब किया जाता है जब वह अन्य I2P destinations से आने वाले अनुरोधों को सुनना चाहता है।

### SAM Virtual Streams: CONNECT

एक client निम्नलिखित तरीके से connection की मांग करता है:

- SAM bridge के साथ एक नया socket खोलना
- ऊपर के समान HELLO handshake पास करना
- STREAM CONNECT command भेजना

#### कनेक्ट अनुरोध

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
यह स्थानीय सत्र से एक नया आभासी कनेक्शन स्थापित करता है जिसका ID $nickname है, निर्दिष्ट peer के लिए।

लक्ष्य $destination है, जो [Destination](/docs/specs/common-structures#type_Destination) का base 64 है, जो signature type के आधार पर 516 या अधिक base 64 वर्ण (बाइनरी में 387 या अधिक bytes) है।

**नोट:** लगभग 2014 (SAM v3.1) से, Java I2P ने $destination के लिए hostnames और b32 addresses का भी समर्थन किया है, लेकिन यह पहले अप्रलेखित था। Hostnames और b32 addresses अब आधिकारिक रूप से Java I2P द्वारा रिलीज़ 0.9.48 से समर्थित हैं। i2pd router रिलीज़ 2.38.0 (0.9.50) से hostnames और b32 addresses का समर्थन करता है। दोनों routers के लिए, "b32" समर्थन में blinded destinations के लिए विस्तारित "b33" addresses का समर्थन शामिल है।

#### कनेक्ट रिस्पॉन्स

यदि SILENT=true पास किया जाता है, तो SAM bridge socket पर कोई अन्य संदेश जारी नहीं करेगा। यदि कनेक्शन विफल हो जाता है, तो socket बंद हो जाएगा। यदि कनेक्शन सफल हो जाता है, तो वर्तमान socket के माध्यम से गुजरने वाला सभी शेष डेटा जुड़े हुए I2P destination peer से आगे-पीछे भेजा जाता है।

यदि SILENT=false है, जो कि डिफ़ॉल्ट वैल्यू है, तो SAM bridge अपने client को socket को forward करने या बंद करने से पहले एक अंतिम संदेश भेजता है:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT मान निम्नलिखित में से कोई एक हो सकता है:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
यदि RESULT OK है, तो मौजूदा socket के माध्यम से गुजरने वाला सभी शेष डेटा जुड़े हुए I2P destination peer से और उसकी ओर forward किया जाता है। यदि कनेक्शन संभव नहीं था (timeout, आदि), तो RESULT में उपयुक्त त्रुटि मान होगा (एक वैकल्पिक human-readable MESSAGE के साथ), और SAM bridge socket को बंद कर देता है।

router stream connect timeout आंतरिक रूप से लगभग एक मिनट का होता है, जो implementation पर निर्भर करता है। response का इंतजार करते समय इससे कम timeout सेट न करें।

### SAM Virtual Streams: ACCEPT

एक client आने वाले connection request का इंतजार करता है:

- SAM bridge के साथ एक नया socket खोलना
- ऊपर दिए गए समान HELLO handshake को पास करना
- STREAM ACCEPT command भेजना

#### अनुरोध स्वीकार करें

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
यह session ${nickname} को I2P network से एक incoming connection request के लिए listen करवाता है। session पर active FORWARD होने पर ACCEPT की अनुमति नहीं है।

SAM 3.2 के अनुसार, एक ही session ID पर कई समानांतर pending STREAM ACCEPTs की अनुमति है (यहाँ तक कि समान port के साथ भी)। 3.2 से पहले, समानांतर accepts ALREADY_ACCEPTING के साथ विफल हो जाते थे। नोट: Java I2P भी SAM 3.1 पर समानांतर ACCEPTs का समर्थन करता है, release 0.9.24 (2016-01) से। i2pd भी SAM 3.1 पर समानांतर ACCEPTs का समर्थन करता है, release 2.50.0 (2023-12) से।

#### स्वीकार प्रतिक्रिया

यदि SILENT=true पास किया जाता है, तो SAM bridge सॉकेट पर कोई अन्य संदेश जारी नहीं करेगा। यदि accept विफल हो जाता है, तो सॉकेट बंद हो जाएगा। यदि accept सफल हो जाता है, तो वर्तमान सॉकेट से गुजरने वाला सभी शेष डेटा जुड़े हुए I2P destination peer से और उसकी ओर अग्रेषित किया जाता है। विश्वसनीयता के लिए, और आने वाले कनेक्शन के लिए destination प्राप्त करने के लिए, SILENT=false की सिफारिश की जाती है।

यदि SILENT=false है, जो कि डिफ़ॉल्ट वैल्यू है, तो SAM bridge इसके साथ उत्तर देता है:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT का मान निम्नलिखित में से एक हो सकता है:

```
OK
I2P_ERROR
INVALID_ID
```
यदि परिणाम OK नहीं है, तो SAM bridge द्वारा socket तुरंत बंद कर दिया जाता है। यदि परिणाम OK है, तो SAM bridge दूसरे I2P peer से आने वाले connection request का इंतजार करना शुरू करता है। जब कोई request आती है, तो SAM bridge उसे स्वीकार करता है और:

यदि SILENT=true पास किया गया था, तो SAM bridge क्लाइंट socket पर कोई अन्य संदेश जारी नहीं करेगा। वर्तमान socket से गुजरने वाला सभी शेष डेटा जुड़े हुए I2P destination peer से और उसकी ओर फॉरवर्ड किया जाता है।

यदि SILENT=false पास किया गया था, जो कि डिफ़ॉल्ट वैल्यू है, तो SAM bridge क्लाइंट को एक ASCII line भेजता है जिसमें अनुरोधकर्ता peer की base64 public destination key होती है, और केवल SAM 3.2 के लिए अतिरिक्त जानकारी:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
इस '\\n' समाप्त लाइन के बाद, वर्तमान socket से गुजरने वाला सभी शेष डेटा जुड़े हुए I2P destination peer से और उसको फॉरवर्ड किया जाता है, जब तक कि कोई एक peer socket को बंद नहीं कर देता।

#### OK के बाद त्रुटियां

दुर्लभ मामलों में, SAM bridge को RESULT=OK भेजने के बाद लेकिन connection आने और client को $destination line भेजने से पहले error आ सकती है। इन errors में router shutdown, router restart, और session close शामिल हो सकते हैं। इन मामलों में, जब SILENT=false हो, तो SAM bridge भेज सकता है, लेकिन यह आवश्यक नहीं है (implementation-dependent), यह line:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
socket को तुरंत बंद करने से पहले। यह लाइन निश्चित रूप से एक वैध Base 64 destination के रूप में decode नहीं की जा सकती।

### SAM Virtual Streams: FORWARD

एक client नियमित socket server का उपयोग कर सकता है और I2P से आने वाले connection requests की प्रतीक्षा कर सकता है। इसके लिए, client को निम्नलिखित करना होगा:

- SAM bridge के साथ एक नया socket खोलें
- ऊपर दिए गए समान HELLO handshake को पास करें
- forward command भेजें

#### फॉरवर्ड अनुरोध

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
यह session ${nickname} को I2P network से आने वाले connection requests को सुनने के लिए बनाता है। session पर pending ACCEPT होने के दौरान FORWARD की अनुमति नहीं है।

#### फॉरवर्ड रिस्पांस

SILENT की डिफ़ॉल्ट वैल्यू false है। चाहे SILENT true हो या false, SAM bridge हमेशा STREAM STATUS संदेश के साथ जवाब देता है। ध्यान दें कि यह STREAM ACCEPT और STREAM CONNECT से अलग व्यवहार है जब SILENT=true होता है। STREAM STATUS संदेश है:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT मान निम्नलिखित में से कोई एक हो सकता है:

```
OK
I2P_ERROR
INVALID_ID
```
$host socket server का hostname या IP address है जिस पर SAM कनेक्शन requests को forward करेगा। यदि नहीं दिया गया है, तो SAM उस socket का IP लेगा जिसने forward command जारी की है।

$port सॉकेट सर्वर का पोर्ट नंबर है जिसपर SAM कनेक्शन रिक्वेस्ट्स को फॉरवर्ड करेगा। यह अनिवार्य है।

जब I2P से एक connection request आती है, तो SAM bridge $host:$port पर एक socket connection खोलता है। यदि यह 3 सेकंड से कम समय में accept हो जाता है, तो SAM I2P से connection को accept कर देगा, और फिर:

यदि SILENT=true पास किया गया था, तो प्राप्त वर्तमान socket से गुजरने वाला सभी डेटा जुड़े हुए I2P destination peer से और उसकी ओर forward किया जाता है।

यदि SILENT=false पास किया गया था, जो कि डिफ़ॉल्ट वैल्यू है, तो SAM bridge प्राप्त socket पर एक ASCII लाइन भेजता है जिसमें अनुरोधकर्ता peer की base64 public destination key होती है, और केवल SAM 3.2 के लिए अतिरिक्त जानकारी:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
इस '\\n' समाप्त लाइन के बाद, socket के माध्यम से गुजरने वाला सभी शेष डेटा जुड़े हुए I2P destination peer से और उसके लिए forward किया जाता है, जब तक कि कोई एक पक्ष socket को बंद नहीं कर देता।

SAM 3.2 के अनुसार, यदि SSL=true निर्दिष्ट किया गया है, तो forwarding socket SSL/TLS के माध्यम से होता है।

I2P router "forwarding" socket बंद होते ही आने वाले connection requests को सुनना बंद कर देगा।

### SAM Datagrams

SAMv3 स्थानीय datagram sockets के माध्यम से datagrams भेजने और प्राप्त करने के लिए तंत्र प्रदान करता है। कुछ SAMv3 implementations पुराने v1/v2 तरीके से SAM bridge socket के माध्यम से datagrams भेजने/प्राप्त करने का भी समर्थन करते हैं। दोनों का विवरण नीचे दिया गया है।

I2P चार प्रकार के डेटाग्राम का समर्थन करता है:

- Repliable और authenticated datagrams भेजने वाले के destination के साथ prefixed होते हैं, और भेजने वाले का signature शामिल करते हैं, ताकि प्राप्तकर्ता यह सत्यापित कर सके कि भेजने वाले का destination spoofed नहीं था, और datagram का जवाब दे सके। नया Datagram2 format भी repliable और authenticated है।
- नया Datagram3 format repliable है लेकिन authenticated नहीं है। भेजने वाले की जानकारी अस्वीकृत है।
- Raw datagrams में भेजने वाले का destination या signature शामिल नहीं होता।

Default I2CP ports repliable और raw datagrams दोनों के लिए परिभाषित हैं। Raw datagrams के लिए I2CP port को बदला जा सकता है।

एक सामान्य प्रोटोकॉल डिज़ाइन पैटर्न यह है कि repliable datagrams को servers को भेजा जाता है, जिसमें कुछ identifier शामिल होता है, और server एक raw datagram के साथ respond करता है जिसमें वह identifier शामिल होता है, ताकि response को request के साथ correlate किया जा सके। यह डिज़ाइन पैटर्न replies में repliable datagrams के substantial overhead को समाप्त कर देता है। I2CP protocols और ports की सभी choices application-specific हैं, और designers को इन मुद्दों पर विचार करना चाहिए।

नीचे दिए गए खंड में datagram MTU पर महत्वपूर्ण टिप्पणियां भी देखें।

#### उत्तर योग्य या कच्चे डेटाग्राम भेजना

जबकि I2P में स्वाभाविक रूप से FROM address नहीं होता है, उपयोग में आसानी के लिए एक अतिरिक्त परत repliable datagrams के रूप में प्रदान की गई है - ये अव्यवस्थित और अविश्वसनीय संदेश हैं जो 31744 bytes तक के होते हैं और इनमें FROM address शामिल होता है (header material के लिए 1KB तक जगह छोड़कर)। यह FROM address SAM द्वारा आंतरिक रूप से प्रमाणित होता है (source को सत्यापित करने के लिए destination की signing key का उपयोग करते हुए) और इसमें replay prevention शामिल है।

न्यूनतम आकार 1 है। सर्वोत्तम डिलीवरी विश्वसनीयता के लिए, अनुशंसित अधिकतम आकार लगभग 11 KB है। विश्वसनीयता संदेश के आकार के व्युत्क्रमानुपाती है, शायद घातीय रूप से भी।

STYLE=DATAGRAM या STYLE=RAW के साथ SAM सत्र स्थापित करने के बाद, क्लाइंट SAM के UDP पोर्ट (डिफ़ॉल्ट रूप से 7655) के माध्यम से repliable या raw डेटाग्राम भेज सकता है।

इस port के माध्यम से भेजे गए datagram की पहली लाइन निम्नलिखित format में होनी चाहिए। यह सब एक ही लाइन पर है (स्थान से अलग किया गया), स्पष्टता के लिए कई लाइनों पर दिखाया गया है:

```
3.0                                  # As of SAM 3.2, any "3.x" is allowed. Prior to that, "3.0" is required.
$nickname
$destination
[FROM_PORT=nnn]                      # SAM 3.2 or higher only, default from session options
[TO_PORT=nnn]                        # SAM 3.2 or higher only, default from session options
[PROTOCOL=nnn]                       # SAM 3.2 or higher only, only for RAW sessions, default from session options
[SEND_TAGS=nnn]                      # SAM 3.3 or higher only, number of session tags to send
                                     # Overrides crypto.tagsToSend I2CP session option
                                     # Default is router-dependent (40 for Java router)
[TAG_THRESHOLD=nnn]                  # SAM 3.3 or higher only, low session tag threshold
                                     # Overrides crypto.lowTagThreshold I2CP session option
                                     # Default is router-dependent (30 for Java router)
[EXPIRES=nnn]                        # SAM 3.3 or higher only, expiration from now in seconds
                                     # Overrides clientMessageTimeout I2CP session option (which is in ms)
                                     # Default is router-dependent (60 for Java router)
[SEND_LEASESET={true,false}]         # SAM 3.3 or higher only, whether to send our leaseset
                                     # Overrides shouldBundleReplyInfo I2CP session option
                                     # Default is true
\n
```
- 3.0 SAM का version है। SAM 3.2 के बाद से, कोई भी 3.x allowed है।
- $nickname उस DATAGRAM session का id है जो उपयोग किया जाएगा
- Target $destination है, जो [Destination](/docs/specs/common-structures#type_Destination) का base 64 है, जो signature type के आधार पर 516 या अधिक base 64 characters (binary में 387 या अधिक bytes) होता है। **नोट:** लगभग 2014 (SAM v3.1) से, Java I2P ने $destination के लिए hostnames और b32 addresses का भी समर्थन किया है, लेकिन यह पहले undocumented था। Hostnames और b32 addresses अब Java I2P द्वारा release 0.9.48 से आधिकारिक रूप से समर्थित हैं। i2pd router वर्तमान में hostnames और b32 addresses का समर्थन नहीं करता; भविष्य की release में समर्थन जोड़ा जा सकता है।
- सभी options per-datagram settings हैं जो SESSION CREATE में निर्दिष्ट defaults को override करती हैं।
- Version 3.3 options SEND_TAGS, TAG_THRESHOLD, EXPIRES, और SEND_LEASESET को [I2CP](/docs/protocol/i2cp) को pass किया जाएगा यदि समर्थित हो। विवरण के लिए [I2CP specification](/docs/protocol/i2cp#msg_SendMessageExpire) देखें। SAM server द्वारा समर्थन optional है, यह इन options को ignore करेगा यदि unsupported हो।
- यह line '\\n' terminated है।

पहली पंक्ति को SAM द्वारा संदेश के शेष डेटा को निर्दिष्ट गंतव्य पर भेजने से पहले छोड़ दिया जाएगा।

repliable और raw datagrams भेजने की वैकल्पिक विधि के लिए, देखें [DATAGRAM SEND और RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling)।

#### SAM Repliable Datagrams: एक डेटाग्राम प्राप्त करना

प्राप्त datagrams को SAM द्वारा उस socket पर लिखा जाता है जिससे datagram session खोला गया था, यदि SESSION CREATE command में forwarding PORT निर्दिष्ट नहीं किया गया है। यह datagrams प्राप्त करने का v1/v2-compatible तरीका है।

जब एक datagram आता है, तो bridge इसे client को message के माध्यम से पहुंचाता है:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
स्रोत $destination है, जो [Destination](/docs/specs/common-structures#type_Destination) का base 64 है, जो signature type के आधार पर 516 या अधिक base 64 characters (binary में 387 या अधिक bytes) होता है।

SAM bridge कभी भी client को authentication headers या अन्य fields को expose नहीं करता, केवल वह data जो sender ने प्रदान किया था। यह तब तक जारी रहता है जब तक session बंद नहीं हो जाता (client द्वारा connection छोड़ने पर)।

#### Raw या Repliable Datagrams को Forward करना

datagram session बनाते समय, client SAM से अनुरोध कर सकता है कि वह आने वाले messages को एक निर्दिष्ट ip:port पर forward करे। यह PORT और HOST options के साथ CREATE command जारी करके ऐसा करता है:

```
-> SESSION CREATE
          STYLE={DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          PORT=$port
          [HOST=$host]
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP options
```
$privkey [Destination](/docs/specs/common-structures#type_Destination) के बाद [Private Key](/docs/specs/common-structures#type_PrivateKey) के बाद [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey) के concatenation का base 64 है, जिसके बाद वैकल्पिक रूप से [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) होता है, जो signature type के आधार पर 884 या अधिक base 64 characters (binary में 663 या अधिक bytes) होता है। binary format Private Key File में निर्दिष्ट है।

ऑफ़लाइन हस्ताक्षर RAW, DATAGRAM2, और DATAGRAM3 datagrams के लिए समर्थित हैं, लेकिन DATAGRAM के लिए नहीं। विवरण के लिए ऊपर SESSION CREATE सेक्शन और नीचे DATAGRAM2/3 सेक्शन देखें।

$host डेटाग्राम सर्वर का hostname या IP address है जिसे SAM डेटाग्राम forward करेगा। यदि नहीं दिया गया है, तो SAM उस socket के IP को लेता है जिसने forward command जारी किया था।

$port वह पोर्ट नंबर है जिस datagram server पर SAM datagrams को forward करेगा। यदि $port सेट नहीं है, तो datagrams forward नहीं किए जाएंगे, वे control socket पर v1/v2-compatible तरीके से प्राप्त होंगे।

दिए गए अतिरिक्त विकल्पों को I2P session कॉन्फ़िगरेशन में पास किया जाता है यदि वे SAM bridge द्वारा व्याख्यायित नहीं हैं (जैसे outbound.length=0)। ये विकल्प [नीचे प्रलेखित हैं](#tunnel-i2cp-and-streaming-options)।

Forwarded repliable datagrams हमेशा base64 destination के साथ prefixed होते हैं, Datagram3 को छोड़कर, नीचे देखें। जब एक repliable datagram आता है, तो bridge निर्दिष्ट host:port पर एक UDP packet भेजता है जिसमें निम्नलिखित data होता है:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Forwarded raw datagrams को बिना किसी prefix के निर्दिष्ट host:port पर जैसा है वैसा ही forward किया जाता है। UDP packet में निम्नलिखित डेटा होता है:

```
$datagram_payload
```
SAM 3.2 के अनुसार, जब SESSION CREATE में HEADER=true निर्दिष्ट किया जाता है, तो forwarded raw datagram के आगे निम्नलिखित प्रकार से एक header line जोड़ी जाएगी:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
$destination [Destination](/docs/specs/common-structures#type_Destination) का base 64 है, जो signature type के आधार पर 516 या अधिक base 64 characters (binary में 387 या अधिक bytes) होता है।

#### SAM Anonymous (Raw) Datagrams

I2P की bandwidth का अधिकतम उपयोग करते हुए, SAM clients को anonymous datagrams भेजने और प्राप्त करने की अनुमति देता है, authentication और reply information को client पर ही छोड़ देता है। ये datagrams अविश्वसनीय और अव्यवस्थित होते हैं, और 32768 bytes तक हो सकते हैं।

न्यूनतम आकार 1 है। सर्वोत्तम डिलीवरी विश्वसनीयता के लिए, अनुशंसित अधिकतम आकार लगभग 11 KB है।

STYLE=RAW के साथ SAM session स्थापित करने के बाद, client SAM bridge के माध्यम से anonymous datagrams बिल्कुल उसी तरह से भेज सकता है जैसे [repliable datagrams भेजना](#sending-repliable-or-raw-datagrams)।

डेटाग्राम प्राप्त करने के दोनों तरीके गुमनाम डेटाग्राम के लिए भी उपलब्ध हैं।

प्राप्त datagrams को SAM द्वारा उस socket पर लिखा जाता है जिससे datagram session खोला गया था, यदि SESSION CREATE command में forwarding PORT निर्दिष्ट नहीं है। यह datagrams प्राप्त करने का v1/v2-compatible तरीका है।

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
जब anonymous datagrams को किसी host:port पर forward करना होता है, तो bridge निर्दिष्ट host:port पर निम्नलिखित data वाला एक message भेजता है:

```
$datagram_payload
```
SAM 3.2 के अनुसार, जब SESSION CREATE में HEADER=true निर्दिष्ट किया जाता है, तो forwarded raw datagram के आगे निम्नलिखित के अनुसार एक header line जोड़ी जाएगी:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
अज्ञात डेटाग्राम भेजने की वैकल्पिक विधि के लिए, [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling) देखें।

#### डेटाग्राम 2/3

Datagram 2/3 नए प्रारूप हैं जो 2025 की शुरुआत में निर्दिष्ट किए गए हैं। वर्तमान में कोई ज्ञात implementation मौजूद नहीं है। वर्तमान स्थिति के लिए implementation दस्तावेज़ देखें। अधिक जानकारी के लिए [specification](/docs/specs/datagrams) देखें।

Datagram 2/3 समर्थन को दर्शाने के लिए SAM version बढ़ाने की कोई वर्तमान योजना नहीं है। यह समस्याग्रस्त हो सकता है क्योंकि implementations Datagram 2/3 का समर्थन करना चाह सकती हैं लेकिन SAM v3.3 सुविधाओं का नहीं। कोई भी version परिवर्तन TBD है।

Datagram2 और Datagram3 दोनों repliable हैं। केवल Datagram2 authenticated है।

Datagram2, SAM के दृष्टिकोण से repliable datagrams के समान है। दोनों authenticated हैं। केवल I2CP format और signature अलग हैं, लेकिन यह SAM clients को दिखाई नहीं देता। Datagram2 offline signatures का भी समर्थन करता है, इसलिए इसका उपयोग offline-signed destinations द्वारा किया जा सकता है।

इसका उद्देश्य यह है कि Datagram2 उन नई applications के लिए Repliable datagrams को replace करे जिन्हें backward-compatibility की आवश्यकता नहीं है। Datagram2 replay protection प्रदान करता है जो Repliable datagrams में उपस्थित नहीं है। यदि backward-compatibility की आवश्यकता है, तो एक application SAM 3.3 PRIMARY sessions के साथ same session पर Datagram2 और Repliable दोनों को support कर सकती है।

Datagram3 उत्तर देने योग्य है लेकिन प्रमाणित नहीं है। I2CP प्रारूप में 'from' फ़ील्ड एक hash है, destination नहीं। SAM server से client को भेजा गया $destination एक 44-byte base64 hash होगा। उत्तर के लिए इसे पूर्ण destination में परिवर्तित करने के लिए, इसे base64-decode करके 32 bytes binary में करें, फिर इसे base32-encode करके 52 characters बनाएं और NAMING LOOKUP के लिए ".b32.i2p" जोड़ें। हमेशा की तरह, clients को बार-बार NAMING LOOKUPs से बचने के लिए अपना cache बनाए रखना चाहिए।

एप्लिकेशन डिज़ाइनरों को अत्यधिक सावधानी बरतनी चाहिए और अप्रमाणित डेटाग्राम्स के सुरक्षा निहितार्थों पर विचार करना चाहिए।

#### V3 Datagram MTU विचार

I2P Datagrams सामान्य इंटरनेट MTU 1500 से बड़े हो सकते हैं। स्थानीय रूप से भेजे गए datagrams और 516+ बाइट base64 destination के साथ prefixed forwarded repliable datagrams उस MTU से अधिक होने की संभावना है। हालांकि, Linux सिस्टम पर localhost MTUs आमतौर पर बहुत बड़े होते हैं, उदाहरण के लिए 65536। Localhost MTUs OS के अनुसार अलग-अलग होंगे। I2P Datagrams कभी भी 65536 से बड़े नहीं होंगे। Datagram का आकार एप्लिकेशन प्रोटोकॉल पर निर्भर करता है।

यदि SAM client SAM server के स्थानीय है और सिस्टम एक बड़े MTU का समर्थन करता है, तो datagrams स्थानीय रूप से खंडित नहीं होंगे। हालांकि, यदि SAM client दूरस्थ है, तो IPv4 datagrams खंडित हो जाएंगे और IPv6 datagrams विफल हो जाएंगे (IPv6 UDP fragmentation का समर्थन नहीं करता)।

Client library और एप्लिकेशन डेवलपर्स को इन समस्याओं के बारे में जानकारी होनी चाहिए और fragmentation से बचने तथा packet loss को रोकने के लिए सिफारिशों का दस्तावेजीकरण करना चाहिए, विशेष रूप से remote SAM client-server connections पर।

#### DATAGRAM SEND, RAW SEND (V1/V2 संगत Datagram हैंडलिंग)

SAMv3 में, datagram भेजने का पसंदीदा तरीका पोर्ट 7655 पर datagram socket के माध्यम से है जैसा कि ऊपर दस्तावेजित है। हालांकि, उत्तर देने योग्य datagram को सीधे SAM bridge socket के माध्यम से DATAGRAM SEND कमांड का उपयोग करके भेजा जा सकता है, जैसा कि [SAM V1](/docs/api/sam) और [SAM V2](/docs/api/samv2) में दस्तावेजित है।

रिलीज 0.9.14 (संस्करण 3.1) के अनुसार, anonymous datagrams को SAM bridge socket के माध्यम से RAW SEND कमांड का उपयोग करके सीधे भेजा जा सकता है, जैसा कि [SAM V1](/docs/api/sam) और [SAM V2](/docs/api/samv2) में दस्तावेजीकरण किया गया है।

रिलीज़ 0.9.24 (संस्करण 3.2) से, DATAGRAM SEND और RAW SEND में डिफ़ॉल्ट पोर्ट्स को ओवरराइड करने के लिए FROM_PORT=nnnn और/या TO_PORT=nnnn पैरामीटर शामिल हो सकते हैं। रिलीज़ 0.9.24 (संस्करण 3.2) से, RAW SEND में डिफ़ॉल्ट प्रोटोकॉल को ओवरराइड करने के लिए PROTOCOL=nnn पैरामीटर शामिल हो सकता है।

ये commands ID parameter का समर्थन *नहीं* करते हैं। datagrams को सबसे हाल ही में बनाए गए DATAGRAM- या RAW-style session में भेजा जाता है, जैसा उपयुक्त हो। ID parameter के लिए समर्थन भविष्य की रिलीज़ में जोड़ा जा सकता है।

DATAGRAM2 और DATAGRAM3 formats V1/V2 compatible तरीके से समर्थित *नहीं* हैं।

### SAM PRIMARY Sessions (V3.3 और उच्चतर)

*संस्करण 3.3 को I2P रिलीज 0.9.25 में शुरू किया गया था।*

*इस विनिर्देश के पहले के संस्करण में, PRIMARY sessions को MASTER sessions के नाम से जाना जाता था। `i2pd` और `I2P+` दोनों में, वे अभी भी केवल MASTER sessions के नाम से ही जाने जाते हैं।*

SAM v3.3 एक ही प्राथमिक सत्र पर streaming, datagrams, और raw subsessions चलाने के लिए समर्थन जोड़ता है, और एक ही शैली के कई subsessions चलाने के लिए भी। सभी subsession ट्रैफिक एक ही destination, या tunnels के सेट का उपयोग करता है। I2P से ट्रैफिक की routing subsessions के लिए port और protocol विकल्पों पर आधारित होती है।

मल्टिप्लेक्स्ड सबसेशन बनाने के लिए, आपको पहले एक प्राइमरी सेशन बनाना होगा और फिर प्राइमरी सेशन में सबसेशन जोड़ने होंगे। प्रत्येक सबसेशन का एक अनूठा id और एक अनूठा listen प्रोटोकॉल और पोर्ट होना चाहिए। सबसेशन को प्राइमरी सेशन से हटाया भी जा सकता है।

एक PRIMARY session और subsessions के संयोजन के साथ, एक SAM client कई applications का समर्थन कर सकता है, या tunnels के एक single set पर विभिन्न protocols का उपयोग करने वाली एक sophisticated application का समर्थन कर सकता है। उदाहरण के लिए, एक bittorrent client peer-to-peer connections के लिए एक streaming subsession स्थापित कर सकता है, DHT communication के लिए datagram और raw subsessions के साथ।

#### PRIMARY Session बनाना

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
SAM bridge सफलता या असफलता के साथ प्रतिक्रिया देगा जैसा कि [मानक SESSION CREATE की प्रतिक्रिया में](#session-creation-response) होता है।

प्राथमिक सेशन पर PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL, या HEADER विकल्प सेट न करें। आप PRIMARY सेशन ID पर या control socket पर कोई डेटा नहीं भेज सकते। STREAM CONNECT, DATAGRAM SEND, आदि जैसे सभी कमांड को अलग socket पर subsession ID का उपयोग करना चाहिए।

PRIMARY session router से कनेक्ट होता है और tunnels बनाता है। जब SAM bridge रिस्पॉन्स करता है, तो tunnels बन गए होते हैं और session subsessions जोड़ने के लिए तैयार होता है। सभी [I2CP](/docs/protocol/i2cp) विकल्प जो tunnel पैरामीटर से संबंधित हैं जैसे कि length, quantity, और nickname, primary के SESSION CREATE में प्रदान किए जाने चाहिए।

सभी utility commands प्राथमिक session पर समर्थित हैं।

जब प्राथमिक सत्र बंद हो जाता है, तो सभी उप-सत्र भी बंद हो जाते हैं।

नोट: रिलीज 0.9.47 से पहले, STYLE=MASTER का उपयोग करें। STYLE=PRIMARY रिलीज 0.9.47 से समर्थित है। पिछड़ी संगतता के लिए MASTER अभी भी समर्थित है।

#### सबसेशन बनाना

उसी control socket का उपयोग करते हुए जिस पर PRIMARY session बनाया गया था:

```
->  SESSION ADD
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See above for DATAGRAM2/3
          ID=$nickname                         # must be unique
          [PORT=$port]                         # Required for DATAGRAM* and RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # For outbound traffic, default 0
          [TO_PORT=nnn]                        # For outbound traffic, default 0
          [PROTOCOL=nnn]                       # For outbound traffic for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [LISTEN_PORT=nnn]                    # For inbound traffic, default is the FROM_PORT value.
                                               # For STYLE=STREAM, only the FROM_PORT value or 0 is allowed.
          [LISTEN_PROTOCOL=nnn]                # For inbound traffic for STYLE=RAW only.
                                               # Default is the PROTOCOL value; 6 (streaming) is disallowed
          [HEADER={true,false}]                # For STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
SAM bridge [मानक SESSION CREATE के response](#session-creation-response) की तरह सफलता या असफलता के साथ जवाब देगा। चूंकि tunnels पहले से ही प्राथमिक SESSION CREATE में बनाए गए थे, SAM bridge को तुरंत जवाب देना चाहिए।

SESSION ADD पर DESTINATION विकल्प सेट न करें। subsession प्राथमिक session में निर्दिष्ट destination का उपयोग करेगा। सभी subsessions को control socket पर जोड़ा जाना चाहिए, यानी उसी connection पर जिस पर आपने प्राथमिक session बनाया था।

कई subsessions के पास पर्याप्त रूप से अनूठे विकल्प होने चाहिए ताकि आने वाला डेटा सही तरीके से route किया जा सके। विशेष रूप से, समान शैली के कई sessions के पास अलग LISTEN_PORT विकल्प होने चाहिए (और/या LISTEN_PROTOCOL, केवल RAW के लिए)। एक SESSION ADD जिसमें listen port और protocol हो जो किसी मौजूदा subsession को duplicate करता है, उसका परिणाम error होगा।

LISTEN_PORT स्थानीय I2P port है, यानी आने वाले डेटा के लिए receive (TO) port। यदि LISTEN_PORT निर्दिष्ट नहीं है, तो FROM_PORT का मान उपयोग किया जाएगा। यदि LISTEN_PORT और FROM_PORT दोनों निर्दिष्ट नहीं हैं, तो आने वाली routing केवल STYLE और PROTOCOL के आधार पर होगी। LISTEN_PORT और LISTEN_PROTOCOL के लिए, 0 का अर्थ कोई भी मान है, यानी एक wildcard। यदि LISTEN_PORT और LISTEN_PROTOCOL दोनों 0 हैं, तो यह subsession आने वाले traffic के लिए default होगा जो किसी अन्य subsession में route नहीं हो पाता। आने वाले streaming traffic (protocol 6) को कभी भी RAW subsession में route नहीं किया जाएगा, भले ही इसका LISTEN_PROTOCOL 0 हो। RAW subsession 6 का LISTEN_PROTOCOL set नहीं कर सकता। यदि कोई default या subsession नहीं है जो आने वाले traffic के protocol और port से मेल खाता हो, तो वह डेटा drop कर दिया जाएगा।

डेटा भेजने और प्राप्त करने के लिए subsession ID का उपयोग करें, प्राथमिक session ID का नहीं। सभी commands जैसे STREAM CONNECT, DATAGRAM SEND, आदि में subsession ID का उपयोग करना आवश्यक है।

सभी utility commands प्राथमिक session या subsession पर समर्थित हैं। v1/v2 datagram/raw भेजना/प्राप्त करना प्राथमिक session या subsessions पर समर्थित नहीं है।

#### सबसेशन बंद करना

उसी control socket का उपयोग करते हुए जिस पर PRIMARY session बनाया गया था:

```
->  SESSION REMOVE
          ID=$nickname
```
यह primary session से एक subsession को हटाता है। SESSION REMOVE पर कोई अन्य विकल्प सेट न करें। Subsessions को control socket पर हटाया जाना चाहिए, यानी उसी connection पर जिस पर आपने primary session बनाया था। Subsession हटाने के बाद, यह बंद हो जाता है और डेटा भेजने या प्राप्त करने के लिए उपयोग नहीं किया जा सकता।

SAM bridge सफलता या असफलता के साथ जवाब देगा जैसा कि [एक मानक SESSION CREATE के जवाब](#session-creation-response) में होता है।

### SAM उपयोगिता कमांड

कुछ utility commands के लिए पहले से मौजूद session की आवश्यकता होती है और कुछ के लिए नहीं। विवरण नीचे देखें।

#### होस्ट नाम लुकअप

निम्नलिखित संदेश का उपयोग client द्वारा name resolution के लिए SAM bridge को query करने के लिए किया जा सकता है:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
जिसका उत्तर दिया जाता है

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
RESULT का मान निम्नलिखित में से एक हो सकता है:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
यदि NAME=ME है, तो reply में current session द्वारा उपयोग किए गए destination शामिल होंगे (यह उपयोगी है यदि आप TRANSIENT का उपयोग कर रहे हैं)। यदि $result OK नहीं है, तो MESSAGE में एक वर्णनात्मक संदेश हो सकता है, जैसे "bad format" आदि। INVALID_KEY का अर्थ है कि request में $name के साथ कुछ समस्या है, संभवतः invalid characters हैं।

$destination, [Destination](/docs/specs/common-structures#type_Destination) का base 64 है, जो signature type के आधार पर 516 या अधिक base 64 characters (binary में 387 या अधिक bytes) होता है।

NAMING LOOKUP के लिए पहले से session बनाना आवश्यक नहीं है। हालांकि, कुछ implementations में, एक .b32.i2p lookup जो uncached है और network query की आवश्यकता है, वह fail हो सकती है, क्योंकि lookup के लिए कोई client tunnels उपलब्ध नहीं हैं।

#### नाम खोज विकल्प

NAMING LOOKUP को router API 0.9.66 के रूप में service lookups का समर्थन करने के लिए विस्तारित किया गया है। समर्थन implementation के अनुसार भिन्न हो सकता है। अतिरिक्त जानकारी के लिए proposal 167 देखें।

NAMING LOOKUP NAME=example.i2p OPTIONS=true रिप्लाई में options mapping का अनुरोध करता है। जब OPTIONS=true हो तो NAME एक पूर्ण base64 destination हो सकता है।

यदि destination lookup सफल था और leaseset में options मौजूद थे, तो reply में, destination के बाद, OPTION:key=value के रूप में एक या अधिक options होंगे। प्रत्येक option का अलग OPTION: prefix होगा। leaseset से सभी options शामिल किए जाएंगे, न केवल service record options। उदाहरण के लिए, भविष्य में परिभाषित parameters के लिए options मौजूद हो सकते हैं। उदाहरण:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

'=' वाली keys, और newline वाली keys या values को अमान्य माना जाता है और key/value pair को reply से हटा दिया जाएगा। यदि leaseset में कोई options नहीं मिलते हैं, या यदि leaseset version 1 था, तो response में कोई options शामिल नहीं होंगे। यदि lookup में OPTIONS=true था, और leaseset नहीं मिला, तो एक नया result value LEASESET_NOT_FOUND return किया जाएगा।

#### गंतव्य कुंजी निर्माण

निम्नलिखित संदेश का उपयोग करके सार्वजनिक और निजी base64 keys उत्पन्न की जा सकती हैं:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
जिसका उत्तर द्वारा दिया जाता है

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
संस्करण 3.1 (I2P 0.9.14) के अनुसार, एक वैकल्पिक पैरामीटर SIGNATURE_TYPE समर्थित है। SIGNATURE_TYPE मान कोई भी नाम (जैसे ECDSA_SHA256_P256, case insensitive) या संख्या (जैसे 1) हो सकता है जो [Key Certificates](/docs/specs/common-structures#type_Certificate) द्वारा समर्थित है। डिफ़ॉल्ट DSA_SHA1 है, जो आप नहीं चाहते। अधिकांश एप्लिकेशन के लिए, कृपया SIGNATURE_TYPE=7 निर्दिष्ट करें।

$destination [Destination](/docs/specs/common-structures#type_Destination) का base 64 है, जो signature प्रकार के आधार पर 516 या अधिक base 64 characters (binary में 387 या अधिक bytes) होता है।

$privkey, [Destination](/docs/specs/common-structures#type_Destination) के बाद [Private Key](/docs/specs/common-structures#type_PrivateKey) और फिर [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey) के संयोजन का base 64 है, जो signature प्रकार के आधार पर 884 या अधिक base 64 characters (binary में 663 या अधिक bytes) होता है। binary format को Private Key File में निर्दिष्ट किया गया है।

256-byte binary [Private Key](/docs/specs/common-structures#type_PrivateKey) के बारे में नोट्स: यह फील्ड version 0.6 (2005) के बाद से अप्रयुक्त है। SAM implementations इस फील्ड में random data या सभी zeros भेज सकते हैं; base 64 में AAAA की स्ट्रिंग से चिंतित न हों। अधिकांश applications केवल base 64 string को store करेंगे और SESSION CREATE में इसे वैसे ही वापस करेंगे, या storage के लिए binary में decode करेंगे, फिर SESSION CREATE के लिए दोबारा encode करेंगे। हालांकि, applications base 64 को decode कर सकते हैं, PrivateKeyFile specification के अनुसार binary को parse कर सकते हैं, 256-byte private key portion को discard कर सकते हैं, और फिर SESSION CREATE के लिए re-encoding करते समय इसे 256 bytes के random data या सभी zeros से replace कर सकते हैं। PrivateKeyFile specification में अन्य सभी फील्ड्स को preserve करना आवश्यक है। इससे 256 bytes की file system storage की बचत होगी लेकिन अधिकांश applications के लिए यह परेशानी शायद इसके लायक नहीं है। अतिरिक्त जानकारी और पृष्ठभूमि के लिए proposal 161 देखें।

DEST GENERATE के लिए पहले से session बनाया जाना आवश्यक नहीं है।

DEST GENERATE का उपयोग offline signatures के साथ destination बनाने के लिए नहीं किया जा सकता।

#### PING/PONG (SAM 3.2 या उससे ऊपर)

क्लाइंट या सर्वर दोनों में से कोई भी भेज सकता है:

```
PING[ arbitrary text]
```
control port पर, प्रतिक्रिया के साथ:

```
PONG[ arbitrary text from the ping]
```
control socket keepalive के लिए उपयोग किया जाना है। यदि उचित समय में कोई response प्राप्त नहीं होती है तो कोई भी पक्ष session और socket को बंद कर सकता है, यह implementation पर निर्भर है।

यदि क्लाइंट से PONG की प्रतीक्षा करते समय timeout हो जाता है, तो bridge भेज सकता है:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
और फिर डिस्कनेक्ट करें।

यदि bridge से PONG का इंतजार करते समय timeout हो जाता है, तो client केवल disconnect हो सकता है।

PING/PONG के लिए यह आवश्यक नहीं है कि पहले एक session बनाया गया हो।

#### QUIT/STOP/EXIT (SAM 3.2 या उससे ऊपर, वैकल्पिक सुविधाएं)

Commands QUIT, STOP और EXIT session और socket को बंद कर देंगे। Implementation वैकल्पिक है, telnet के माध्यम से testing में आसानी के लिए। Socket बंद होने से पहले कोई response होगी या नहीं (उदाहरण के लिए, एक SESSION STATUS message) यह implementation-specific है और इस specification के दायरे से बाहर है।

QUIT/STOP/EXIT के लिए यह आवश्यक नहीं है कि पहले से कोई सत्र बनाया गया हो।

#### HELP (वैकल्पिक सुविधा)

सर्वर एक HELP कमांड को implement कर सकते हैं। Implementation वैकल्पिक है, telnet के माध्यम से testing में आसानी के लिए। Output format और output के अंत की detection implementation-specific है और इस specification के दायरे के बाहर है।

HELP के लिए यह आवश्यक नहीं है कि पहले एक session बनाया गया हो।

#### प्राधिकरण कॉन्फ़िगरेशन (SAM 3.2 या उच्चतर, वैकल्पिक सुविधा)

AUTH कमांड का उपयोग करके प्राधिकरण कॉन्फ़िगरेशन। एक SAM सर्वर इन कमांड्स को लागू कर सकता है ताकि क्रेडेंशियल्स के स्थायी भंडारण की सुविधा मिल सके। इन कमांड्स के अलावा अन्य प्रमाणीकरण का कॉन्फ़िगरेशन implementation-specific है और इस specification के दायरे से बाहर है।

- AUTH ENABLE बाद की connections पर authorization को सक्षम करता है
- AUTH DISABLE बाद की connections पर authorization को निष्क्रिय करता है
- AUTH ADD USER="foo" PASSWORD="bar" एक user/password जोड़ता है
- AUTH REMOVE USER="foo" इस user को हटाता है

उपयोगकर्ता और पासवर्ड के लिए डबल कोट्स की सिफारिश की जाती है लेकिन ये आवश्यक नहीं हैं। उपयोगकर्ता या पासवर्ड के अंदर एक डबल कोट को बैकस्लैश के साथ escape करना होगा। असफलता पर सर्वर I2P_ERROR और एक संदेश के साथ उत्तर देगा।

AUTH के लिए यह आवश्यक नहीं है कि पहले एक session बनाया गया हो।

### RESULT मान

ये वे मान हैं जो RESULT फ़ील्ड द्वारा ले जाए जा सकते हैं, उनके अर्थ के साथ:

```
OK              Operation completed successfully
CANT_REACH_PEER The peer exists, but cannot be reached
DUPLICATED_DEST The specified Destination is already in use
I2P_ERROR       A generic I2P error (e.g. I2CP disconnection, etc.)
INVALID_KEY     The specified key is not valid (bad format, etc.)
KEY_NOT_FOUND   The naming system can't resolve the given name
PEER_NOT_FOUND  The peer cannot be found on the network
TIMEOUT         Timeout while waiting for an event (e.g. peer answer)
LEASESET_NOT_FOUND  See Name Lookup Options above. As of router API 0.9.66.
```
विभिन्न implementations विभिन्न scenarios में कौन सा RESULT return किया जाता है इसमें consistent नहीं हो सकते हैं।

OK के अलावा RESULT वाले अधिकांश responses में अतिरिक्त जानकारी के साथ एक MESSAGE भी शामिल होगा। MESSAGE आमतौर पर समस्याओं को debug करने में सहायक होगा। हालांकि, MESSAGE strings implementation-dependent हैं, SAM server द्वारा current locale में translate हो भी सकती हैं या नहीं भी, इनमें exceptions जैसी internal implementation-specific जानकारी हो सकती है, और ये बिना सूचना के बदली जा सकती हैं। जबकि SAM clients MESSAGE strings को users के सामने प्रस्तुत करना चुन सकते हैं, उन्हें इन strings के आधार पर programmatic decisions नहीं लेने चाहिए, क्योंकि यह नाज़ुक होगा।

### Tunnel, I2CP, और Streaming विकल्प

ये विकल्प SAM SESSION CREATE लाइन में name=value जोड़ों के रूप में पास किए जा सकते हैं।

सभी sessions में [I2CP विकल्प जैसे कि tunnel की लंबाई और मात्रा](/docs/protocol/i2cp#options) शामिल हो सकते हैं। STREAM sessions में [Streaming library विकल्प](/docs/api/streaming#options) शामिल हो सकते हैं।

विकल्प नामों और डिफ़ॉल्ट्स के लिए उन संदर्भों को देखें। संदर्भित दस्तावेज़ीकरण Java router कार्यान्वयन के लिए है। डिफ़ॉल्ट्स परिवर्तन के अधीन हैं। विकल्प नाम और मान case-sensitive हैं। अन्य router कार्यान्वयन सभी विकल्पों का समर्थन नहीं कर सकते हैं और उनके अलग डिफ़ॉल्ट्स हो सकते हैं; विवरण के लिए router दस्तावेज़ीकरण से परामर्श करें।

### BASE 64 नोट्स

Base 64 encoding में I2P मानक Base 64 alphabet "A-Z, a-z, 0-9, -, ~" का उपयोग करना आवश्यक है।

### डिफ़ॉल्ट SAM सेटअप

डिफ़ॉल्ट SAM पोर्ट 7656 है। SAM Java I2P Router में डिफ़ॉल्ट रूप से सक्षम नहीं होता है; इसे मैन्युअल रूप से शुरू करना होगा, या router console के configure clients पेज पर, या clients.config फाइल में स्वचालित रूप से शुरू होने के लिए कॉन्फ़िगर करना होगा। डिफ़ॉल्ट SAM UDP पोर्ट 7655 है, जो 127.0.0.1 पर सुन रहा है। इन्हें Java router में sam.udp.port=nnnnn और/या sam.udp.host=w.x.y.z आर्गुमेंट्स को invocation में या SESSION लाइन पर जोड़कर बदला जा सकता है।

अन्य router में कॉन्फ़िगरेशन implementation-specific है। [यहाँ i2pd कॉन्फ़िगरेशन गाइड देखें](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/)।

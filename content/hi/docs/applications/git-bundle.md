---
title: "I2P स्रोत कोड प्राप्त करने के लिए git bundle का उपयोग करना"
description: "git bundles और BitTorrent का उपयोग करके I2P पर बड़े repositories को clone करना"
slug: "git-bundle"
aliases:
  - "/hi/docs/applications/git"
  - "/hi/docs/applications/git/"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

I2P पर बड़े software repositories को clone करना कठिन हो सकता है, और git का उपयोग करना कभी-कभी इसे और भी कठिन बना देता है। सौभाग्य से, यह कभी-कभी इसे आसान भी बना सकता है। Git में एक `git bundle` command है जिसका उपयोग git repository को एक file में बदलने के लिए किया जा सकता है जिसे git आपकी local disk पर किसी स्थान से clone, fetch, या import कर सकता है। इस क्षमता को bittorrent downloads के साथ मिलाकर, हम `git clone` के साथ अपनी शेष समस्याओं को हल कर सकते हैं।

---

## शुरू करने से पहले

यदि आप एक git bundle बनाने का इरादा रखते हैं, तो आपके पास **git** repository की पूर्ण प्रति पहले से होनी **चाहिए**, mtn repository की नहीं। आप इसे github या git.idk.i2p से प्राप्त कर सकते हैं, लेकिन एक shallow clone (--depth=1 के साथ किया गया clone) *काम नहीं करेगा*। यह चुपचाप विफल हो जाएगा, एक bundle जैसा दिखने वाला कुछ बना देगा, लेकिन जब आप इसे clone करने की कोशिश करेंगे तो यह विफल हो जाएगा। यदि आप केवल एक पूर्व-निर्मित git bundle प्राप्त कर रहे हैं, तो यह अनुभाग आप पर लागू नहीं होता।

---

## Bittorrent के माध्यम से I2P Source प्राप्त करना

किसी को आपको एक torrent file या magnet link प्रदान करना होगा जो एक मौजूदा `git bundle` के अनुरूप हो जो उन्होंने पहले से आपके लिए तैयार किया हो। मुख्यधारा i2p.i2p source code का एक हालिया, सही तरीके से तैयार किया गया bundle (बुधवार, 18 मार्च, 2020 के अनुसार) I2P के अंदर मेरे pastebin paste.idk.i2p/f/4hq37i पर मिल सकता है।

एक बार जब आपके पास bundle हो जाए, तो आपको git का उपयोग करके इससे एक working repository बनानी होगी। यदि आप GNU/Linux और i2psnark का उपयोग कर रहे हैं, तो git bundle $HOME/.i2p/i2psnark में स्थित होना चाहिए या, Debian पर service के रूप में, /var/lib/i2p/i2p-config/i2psnark में। यदि आप GNU/Linux पर BiglyBT का उपयोग कर रहे हैं, तो यह शायद "$HOME/BiglyBT Downloads/" में होगा। यहाँ के उदाहरण GNU/Linux पर I2PSnark को मानकर दिए गए हैं, यदि आप कुछ और उपयोग करते हैं, तो bundle के path को अपने client और platform द्वारा पसंद की जाने वाली download directory से बदल दें।

### `git clone` का उपयोग करना

git bundle से cloning करना आसान है, बस:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
यदि आपको निम्नलिखित त्रुटि मिलती है, तो इसके बजाय मैन्युअल रूप से git init और git fetch का उपयोग करने का प्रयास करें।

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### `git init` और `git fetch` का उपयोग

पहले, एक i2p.i2p डायरेक्टरी बनाएं जिसे git repository में बदला जा सके।

```
mkdir i2p.i2p && cd i2p.i2p
```
अगला, परिवर्तनों को वापस लाने के लिए एक खाली git repository को initialize करें।

```
git init
```
अंत में, bundle से repository को fetch करें।

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### bundle remote को upstream remote के साथ बदलें

अब जब आपके पास एक bundle है, तो आप upstream repository source के लिए remote सेट करके changes के साथ अप-टू-डेट रह सकते हैं।

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## एक बंडल जनरेट करना

सबसे पहले, [उपयोगकर्ताओं के लिए Git गाइड](/docs/applications/git/) का पालन करें जब तक आपके पास i2p.i2p repository का सफलतापूर्वक `--unshallow`ed clone न हो जाए। यदि आपके पास पहले से ही एक clone है, तो सुनिश्चित करें कि आप torrent bundle बनाने से पहले `git fetch --unshallow` चलाएं।

एक बार आपके पास यह हो जाए, तो बस संबंधित ant target चलाएं:

```
ant git-bundle
```
और परिणामी bundle को अपनी I2PSnark downloads directory में copy करें। उदाहरण के लिए:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
एक या दो मिनट में, I2PSnark torrent को पकड़ लेगा। torrent को seed करना शुरू करने के लिए "Start" बटन पर क्लिक करें।

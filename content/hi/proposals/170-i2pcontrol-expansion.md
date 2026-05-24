---
title: "I2PControl विस्तार"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "खोलें"
toc: true
---

## अवलोकन

यह प्रस्ताव i2pcontrol API के लिए नई जानकारी प्रदर्शित करता है, जिससे अधिक लचीलापन प्राप्त होता है। इस जानकारी में: एड्रेसबुक और हिडन सर्विसेज़ को जोड़ना, हटाना, पुनःप्राप्त करना और संशोधित करना शामिल है। यह प्रस्ताव आपके राउटर के बारे में अधिक जानकारी भी प्रदर्शित करता है, जैसे कि पीयर्स, समाचार, netdb, और अन्य।

## अभिप्रेरणा

इस प्रस्ताव का उपयोग मामला हर राउटर लागूकरण के लिए मानक i2p टनल सूट के साथ साझा की जा सकने वाली एक एकीकृत और सरलीकृत राउटर कंसोल बनाना है। अंततः, यह प्रस्ताव I2P नेटवर्क पर उपयोगकर्ताओं के लिए अधिक बुद्धिमान और उपयोगकर्ता-अनुकूल अनुभव की अनुमति देता है।

यह प्रस्ताव अनुप्रयोगों के लिए I2P प्रशासनिक अंतराफलक को लागू करने और प्रबंधित करने के लिए I2P API में अधिक लचीलापन भी प्रदान करेगा। i2pcontrol को ऐसी जानकारी उपलब्ध कराने से उपयोगकर्ताओं को अधिक उन्नत अनुप्रयोग बनाने और दूरस्थ प्रबंधन के लिए बेहतर समर्थन प्रदान करने में सक्षम बनाया जा सकता है।

## डिजाइन

जब उपयोगकर्ता i2pcontrol API के साथ बातचीत करते हैं, तो वे नए एंडपॉइंट्स तक पहुंच पाएंगे जो ऊपर उल्लिखित जानकारी प्रदान करते हैं। उदाहरण के लिए, i2pcontrol API नए तरीकों `TunnelManager` और `AddressBook` को उजागर करेगा जो उपयोगकर्ताओं को सुरंगों और एड्रेसबुक को बनाने, हटाने, पुनर्प्राप्त करने और संशोधित करने के लिए पैरामीटर दर्ज करने की अनुमति देगा। इसके अतिरिक्त, पहले से मौजूद `RouterInfo` विधि में राउटर के बारे में जानकारी उजागर करने के लिए नए पैरामीटर होंगे।

## सुरक्षा के निहितार्थ

इस प्रस्ताव से कोई अतिरिक्त सुरक्षा प्रभाव अपेक्षित नहीं हैं, क्योंकि जानकारी जो प्रकट की जा रही है वह पहले से ही अन्य तरीकों से सुलभ है। हालांकि, यह सुनिश्चित करना महत्वपूर्ण है कि i2pcontrol API तक पहुंच के लिए उचित प्रमाणीकरण और अधिकृतकरण तंत्र लागू हों, ताकि संवेदनशील जानकारी या राउटर पर नियंत्रण तक अनधिकृत पहुंच को रोका जा सके।

## एपीआई विशिष्टता और विधियाँ

सभी अनुरोध JSON-RPC 2.0 संरचना का पालन करते हैं:

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
### विधि - राउटरइन्फो (GETTERS)

नीचे `RouterInfo` विधि के लिए नए पैरामीटर और उनके द्वारा लौटाए गए मान दिए गए हैं:

- `i2p.router.news` - सभी राउटर समाचार प्रविष्टियाँ लौटाता है। वापसी प्रकार - `String`
- `i2p.router.id` - राउटर हैश को एक Base64 स्ट्रिंग के रूप में लौटाता है, या `null`। वापसी प्रकार - `String`
- `i2p.router.clockskew` - औसत पीयर घड़ी विसंगति लौटाता है, या `null`। वापसी प्रकार - `long`
- `i2p.router.info` - सीरियलाइज़ किया गया RouterInfo को एक Base64 स्ट्रिंग के रूप में लौटाता है, या `null`। वापसी प्रकार - `String`
- `i2p.router.logs` - हाल के राउटर लॉग संदेश लौटाता है। वापसी प्रकार - `List<String>`
- `i2p.router.logs.clear` - राउटर लॉग बफर को साफ़ करता है और `"success"` लौटाता है। वापसी प्रकार - `String`

- `i2p.router.net.total.received.bytes` - आरंभ के बाद से प्राप्त कुल बाइट्स लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `long`
- `i2p.router.net.total.sent.bytes` - आरंभ के बाद से भेजे गए कुल बाइट्स लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `long`
- `i2p.router.net.total.transit.bytes` - आरंभ के बाद से अग्रेषित कुल ट्रांज़िट बाइट्स लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `long`
- `i2p.router.net.bw.transit.15s` - 15-सेकंड की औसत ट्रांज़िट बैंडविड्थ (बाइट्स/सेकंड) लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `long`

- `i2p.router.net.tunnels.shareratio` - टनल शेयर अनुपात लौटाता है। रिटर्न प्रकार - `double`
- `i2p.router.net.tunnels.participating.info` - भाग लेने वाली टनल की जानकारी लौटाता है। रिटर्न प्रकार - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.i2ptunnel` - कॉन्फ़िगर की गई I2PTunnel नियंत्रक जानकारी लौटाता है (सभी की त्वरित आँकड़े)। रिटर्न प्रकार - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.exploratory.inbound` - अन्वेषणात्मक आगमन टनल की संख्या लौटाता है। रिटर्न प्रकार - `int`
- `i2p.router.net.tunnels.exploratory.outbound` - अन्वेषणात्मक आउटबाउंड टनल की संख्या लौटाता है। रिटर्न प्रकार - `int`
- `i2p.router.net.tunnels.exploratory.info.list` - अन्वेषणात्मक टनल जानकारी सूची लौटाता है। रिटर्न प्रकार - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.client.inbound` - क्लाइंट आगमन टनल की संख्या लौटाता है। रिटर्न प्रकार - `int`
- `i2p.router.net.tunnels.client.outbound` - क्लाइंट आउटबाउंड टनल की संख्या लौटाता है। रिटर्न प्रकार - `int`
- `i2p.router.net.tunnels.client.info.list` - क्लाइंट टनल जानकारी सूची लौटाता है। रिटर्न प्रकार - `List<Map<String, Object>>`

- `i2p.router.net.status.v6` - IPv6 नेटवर्क स्थिति कोड लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `int`
- `i2p.router.net.error` - IPv4 नेटवर्क त्रुटि कोड लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `int`
- `i2p.router.net.error.v6` - IPv6 नेटवर्क त्रुटि कोड लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `int`
- `i2p.router.net.testing` - यह बताता है कि क्या IPv4 नेटवर्क परीक्षण अवस्था में है (0 या 1)। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `int`
- `i2p.router.net.testing.v6` - यह बताता है कि क्या IPv6 नेटवर्क परीक्षण अवस्था में है (0 या 1)। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `int`

- `i2p.router.net.tunnels.successrate` - हाल के टनल निर्माण की सफलता दर (%) लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `double`
- `i2p.router.net.tunnels.totalsuccessrate` - शुरुआत के बाद से कुल टनल निर्माण सफलता दर (%) लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `double`
- `i2p.router.net.tunnels.queue` - टनल निर्माण अनुरोध कतार का आकार लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `int`
- `i2p.router.net.tunnels.tbmqueue` - टनल निर्माण संदेश कतार का आकार लौटाता है। *(i2pd से अपनाया गया)* रिटर्न प्रकार - `int`

- `i2p.router.netdb.peers` - ज्ञात पीयर हैश की सूची लौटाता है। रिटर्न प्रकार - `List<String>`
- `i2p.router.netdb.activepeers.info` - सक्रिय पीयर्स के लिए सीरियलाइज़्ड RouterInfo डेटा लौटाता है। रिटर्न प्रकार - `List<String>`
- `i2p.router.netdb.ntcp.limit` - NTCP कनेक्शन सीमा लौटाता है। रिटर्न प्रकार - `int`
- `i2p.router.netdb.ssu.limit` - SSU कनेक्शन सीमा लौटाता है। रिटर्न प्रकार - `int`
- `i2p.router.netdb.bannedpeers` - बैन विवरण के साथ बैन किए गए पीयर्स लौटाता है। रिटर्न प्रकार - `Map<String, Map<String, Object>>`
- `i2p.router.netdb.activepeers.list` - सक्रिय पीयर हैश लौटाता है। रिटर्न प्रकार - `List<String>`
- `i2p.router.netdb.peers.list` - ज्ञात पीयर हैश लौटाता है। रिटर्न प्रकार - `List<String>`
- `i2p.router.netdb.peers.info` - ज्ञात पीयर्स के लिए सीरियलाइज़्ड RouterInfo डेटा लौटाता है। रिटर्न प्रकार - `List<String>`
- `i2p.router.netdb.activepeers.stats` - सक्रिय पीयर सांख्यिकी लौटाता है। रिटर्न प्रकार - `List<Map<String, Object>>`

- `i2p.router.addressbook.private.list` - निजी एड्रेस बुक प्रविष्टियाँ लौटाता है। रिटर्न प्रकार - `List<Map<String, String>>`
- `i2p.router.addressbook.local.list` - स्थानीय एड्रेस बुक प्रविष्टियाँ लौटाता है। रिटर्न प्रकार - `List<Map<String, String>>`
- `i2p.router.addressbook.router.list` - राउटर एड्रेस बुक प्रविष्टियाँ लौटाता है। रिटर्न प्रकार - `List<Map<String, String>>`
- `i2p.router.addressbook.published.list` - प्रकाशित एड्रेस बुक प्रविष्टियाँ लौटाता है। रिटर्न प्रकार - `List<Map<String, String>>`
- `i2p.router.addressbook.subscriptions` - सदस्यता फ़ाइल पथ और प्रविष्टियाँ लौटाता है। रिटर्न प्रकार - `Map<String, Object>`
- `i2p.router.addressbook.config` - एड्रेस बुक कॉन्फ़िग पथ और प्रविष्टियाँ लौटाता है। रिटर्न प्रकार - `Map<String, Object>`

उदाहरण:

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
वापसी:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
### विधि - एड्रेसबुक (सेटर्स)

`AddressBook` विधि के लिए, एड्रेस बुक में प्रविष्टियों को हटाने और जोड़ने के लिए तीन पैरामीटर/तर्क आवश्यक हैं:

- `Type` - पता पुस्तिका के प्रकार के अनुरूप है:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - पता पुस्तिका प्रविष्टि से जुड़े होस्टनाम या डोमेन नाम के अनुरूप है।
- `Destination` - पता पुस्तिका प्रविष्टि से जुड़े गंतव्य के अनुरूप है।
- `Delete` - यह पैरामीटर वैकल्पिक है और पता पुस्तिका प्रविष्टि को हटाने के लिए उपयोग किया जाता है। यदि यह पैरामीटर प्रदान नहीं किया जाता है, तो विधि पता पुस्तिका में एक नई प्रविष्टि जोड़ देगी।

उदाहरण:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
AddressBookSubscriptions संपादित करने के लिए:

- `SetSubscriptions` - इस पैरामीटर का उपयोग किसी एड्रेस बुक एंट्री के लिए सदस्यताएँ सेट करने के लिए किया जाता है। इसे तर्क के रूप में स्ट्रिंग्स की एक सूची लेता है।

उदाहरण:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
AddressBookConfig संपादित करने के लिए:

- `SetConfig` - इस पैरामीटर का उपयोग किसी एड्रेस बुक एंट्री के लिए कॉन्फ़िगरेशन सेट करने के लिए किया जाता है।

यह एक JSON ऑब्जेक्ट को तर्क के रूप में लेता है, जिसमें कॉन्फ़िगरेशन सेटिंग्स शामिल होती हैं।

उपलब्ध/सामान्य कॉन्फ़िग पैरामीटर:

- `subscriptions` - सदस्यता URL की सूची युक्त फ़ाइल।
- `update_delay` - घंटों में अद्यतन अंतराल।
- `published_addressbook` - प्रकाशित एड्रेस बुक का मार्ग।
- `router_addressbook` - राउटर एड्रेस बुक का मार्ग।
- `local_addressbook` - स्थानीय एड्रेस बुक का मार्ग।
- `private_addressbook` - निजी एड्रेस बुक का मार्ग।
- `proxy_port` - eepProxy पोर्ट।
- `proxy_host` - eepProxy होस्टनाम।
- `should_publish` - प्रकाशित एड्रेस बुक को अद्यतन करना चाहिए या नहीं।
- `etags` - सदस्यता URL etags युक्त फ़ाइल।
- `last_modified` - सदस्यता URL के अंतिम-संशोधित समय-स्टैम्प युक्त फ़ाइल।
- `log` - लॉग फ़ाइल का मार्ग।
- `theme` - थीम।

उदाहरण:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
### विधि - टनल प्रबंधक (1 चिह्नित गेटर, शेष सेटर)

`TunnelManager` विधि का उपयोग I2PTunnel नियंत्रकों को बनाने, संपादित करने, प्राप्त करने, शुरू करने, रोकने, पुनः आरंभ करने और हटाने के लिए किया जाता है।

आवश्यक पैरामीटर:

- `Name` - टनल का नाम। यह टनल का पहचानकर्ता है।
- `Action` - करने के लिए क्रिया:
  - `create`
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

वैकल्पिक पैरामीटर:

- `All` - बूलियन, यह बताता है कि क्या क्रिया सभी टनलों पर लागू की जाए। यह केवल `start`, `stop`, और `restart` क्रियाओं के लिए मान्य है।

`create` के लिए समर्थित टनल प्रकार:

- `client`
- `httpclient`
- `ircclient`
- `socks`
- `socksirc`
- `connectclient`
- `streamrclient`

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

टनल बनाने/संपादित करने के लिए सामान्य पैरामीटर:

- `Type` - टनल का प्रकार। `create` के लिए आवश्यक।
- `NewName` - संपादन करते समय वैकल्पिक नया नाम।
- `Port` - स्थानीय लिसन पोर्ट।
- `TargetHost` या `Host` - सर्वर टनल के लिए लक्ष्य होस्ट।
- `TargetPort` - सर्वर टनल के लिए लक्ष्य पोर्ट।
- `TargetDestination` या `Destination` - क्लाइंट टनल के लिए गंतव्य, जिन्हें एक की आवश्यकता हो।
- `StartOnLoad` - बूलियन, यह दर्शाता है कि टनल लोड होने पर शुरू होना चाहिए या नहीं।
- `Description` - टनल का विवरण।
- `ReachableBy` - इंटरफ़ेस/एड्रेस जिस पर टनल सुनता है।
- `Shared` - बूलियन, यह दर्शाता है कि क्लाइंट टनल साझा किया जाना चाहिए या नहीं।
- `UseSSL` - बूलियन, जहां समर्थित हो वहां SSL सक्षम करें।
- `TunnelLength` - टनल की लंबाई, `0` से `3` तक।
- `TunnelVariance` - टनल विचरण, `-2` से `2` तक।
- `TunnelQuantity` - टनल मात्रा, `1` से `6` तक।
- `TunnelBackupQuantity` - बैकअप टनल मात्रा, `0` से `3` तक।
- `SigType` - हस्ताक्षर कुंजी प्रकार।
- `EncType` - एन्क्रिप्शन प्रकार।
- `CustomOptions` - कस्टम टनल विकल्प।

क्लाइंट प्रॉक्सी विकल्प:

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

क्लाइंट प्रबंधन विकल्प:

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

HTTP क्लाइंट फ़िल्टरिंग विकल्प:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

सर्वर विकल्प:

- `WebsiteHostname` या `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

लीज़सेट विकल्प:

- `EncryptLeaseSet` - निम्न में से एक:
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

उदाहरण बनाएं:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
उदाहरण संपादित करें:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
उदाहरण प्राप्त करें (केवल गेटर) लौटाता है - `Map<String, Object>` (जानकारी) और `String` (स्थिति):

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
शुरू करें, रोकें, पुनः आरंभ करें, उदाहरण हटाएं। इनकी संरचना समान होती है, बस अलग-अलग `Action` पैरामीटर के साथ:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
### विधि - क्लाइंटसर्विसेजइन्फो *(i2pd से अपनाया गया)*

`ClientServicesInfo` विधि राउटर पर चल रही क्लाइंट सेवाओं के बारे में स्थिति जानकारी लौटाती है। प्रत्येक सेवा की स्थिति के लिए अनुरोध करने के लिए `params` में वांछित सेवा कुंजियाँ (किसी भी मान के साथ) शामिल करें।

समर्थित पैरामीटर:

- `I2PTunnel` - कॉन्फ़िगर किए गए टनल नामों का उनके पतों पर मानचित्र लौटाता है, जिसे `client` और `server` उप-वस्तुओं में विभाजित किया गया है।
- `HTTPProxy` - HTTP प्रॉक्सी सक्षम स्थिति और पता लौटाता है।
- `SOCKS` - SOCKS प्रॉक्सी सक्षम स्थिति और पता लौटाता है।
- `SAM` - SAM ब्रिज सक्षम स्थिति और सक्रिय सत्र की जानकारी लौटाता है।
- `BOB` - BOB ब्रिज सक्षम स्थिति लौटाता है। (जावा I2P में अप्रचलित; हमेशा `false` लौटाता है।)
- `I2CP` - I2CP सर्वर सक्षम स्थिति लौटाता है।

उदाहरण:

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
वापसी:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
## संगतता

मौजूदा i2pcontrol API के साथ संगतता बनाए रखी जानी चाहिए, क्योंकि नए तरीकों और मापदंडों को इस तरह जोड़ा गया है जो मौजूदा कार्यक्षमता में हस्तक्षेप नहीं करता है। i2pcontrol API का उपयोग करने वाले मौजूदा अनुप्रयोगों को बिना किसी परिवर्तन के काम करते रहना चाहिए, जबकि नए अनुप्रयोग इस प्रस्ताव द्वारा प्रदान की गई अतिरिक्त जानकारी और क्षमताओं का लाभ उठा सकते हैं।

## कार्यान्वयन

### Java I2P

यह प्रस्ताव अभी तक जावा आई2पी में लागू नहीं किया गया है, लेकिन कोड [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) रिपॉजिटरी में पुल रिक्वेस्ट [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6) के तहत उपलब्ध है। मौजूदा कोड को प्रभावित किए बिना नए तरीकों के परीक्षण और विकास की अनुमति देने के लिए ऐसा किया गया था। एक बार कोड उत्पादन उपयोग के लिए तैयार हो जाने पर इसे i2pcontrol निर्देशिका के तहत मुख्य आई2पी रिपॉजिटरी में अपडेट कर दिया जाएगा।

### i2pd

"(i2pd से अपनाया गया)" के रूप में चिह्नित विधियाँ और मापदंड i2pd में लागू की गई हैं और इस प्रस्ताव में अपरिवर्तित हैं। इस प्रस्ताव के तहत i2pd के एक्सटेंशन में कोई संशोधन आवश्यक नहीं होगा। इस प्रस्ताव के बिना चिह्नित भाग i2pd में लागू नहीं हैं।

### go-i2p

go-i2p इस प्रस्ताव को अपनाने और अपने राउटर कंसोल एप्लिकेशन को सक्षम तथा बेहतर बनाने के उद्देश्य से इस प्रस्ताव का अनुसरण करने के लिए प्रेरित है। यह भविष्य में इस प्रस्ताव को अपनाएगा और लागू करेगा।

### emissary

इस समय एमिसरी में अपनाए जाने की संभावना अज्ञात है, हालांकि गो-आई2पी के समान ही एमिसरी को इस प्रस्ताव से लाभ होने की संभावना है।

## प्रदर्शन

कोई प्रदर्शन प्रभाव की अपेक्षा नहीं है।

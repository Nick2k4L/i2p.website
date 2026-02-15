---
title: "Encrypted Leasesets के लिए B32"
description: "एन्क्रिप्टेड LS2 leasesets के लिए Base 32 address प्रारूप"
slug: "b32encrypted"
aliases:
  - "/hi/docs/specs/b32-for-encrypted-leasesets"
  - "/hi/docs/specs/b32-for-encrypted-leasesets/"
category: "डिज़ाइन"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## अवलोकन

Standard Base 32 ("b32") पते destination का hash शामिल करते हैं। यह encrypted ls2 (proposal 123) के लिए काम नहीं करेगा।

हम एक encrypted LS2 (प्रस्ताव 123) के लिए पारंपरिक base 32 address का उपयोग नहीं कर सकते, क्योंकि इसमें केवल destination का hash होता है। यह non-blinded public key प्रदान नहीं करता। Clients को destination की public key, sig type, blinded sig type, और leaseset को fetch और decrypt करने के लिए एक वैकल्पिक secret या private key जानना आवश्यक है। इसलिए, केवल base 32 address अपर्याप्त है। Client को या तो पूरा destination (जिसमें public key शामिल है), या अकेली public key की आवश्यकता होती है। यदि client के पास address book में पूरा destination है, और address book hash द्वारा reverse lookup का समर्थन करता है, तो public key को प्राप्त किया जा सकता है।

यह format hash के बजाय public key को base32 address में डालता है। इस format में public key का signature type और blinding scheme का signature type भी होना चाहिए।

यह दस्तावेज़ इन पतों के लिए एक b32 प्रारूप निर्दिष्ट करता है। जबकि हमने चर्चाओं के दौरान इस नए प्रारूप को "b33" पता कहा है, वास्तविक नया प्रारूप सामान्य ".b32.i2p" प्रत्यय को बनाए रखता है।

## डिज़ाइन

- नया प्रारूप में unblinded public key, unblinded sig type, और blinded sig type शामिल होगा।
- वैकल्पिक रूप से एक secret और/या private key शामिल हो सकती है, केवल private links के लिए
- मौजूदा ".b32.i2p" suffix का उपयोग करें, लेकिन अधिक लंबाई के साथ।
- एक checksum जोड़ें।
- Encrypted leasesets के लिए addresses की पहचान 56 या अधिक encoded characters (35 या अधिक decoded bytes) से होती है, पारंपरिक base 32 addresses के 52 characters (32 bytes) की तुलना में।

## विनिर्देश

### निर्माण और एन्कोडिंग

{56+ वर्ण}.b32.i2p (बाइनरी में 35+ वर्ण) का hostname निम्नलिखित तरीके से बनाएं:

```
flag (1 byte)
    bit 0: 0 for one-byte sigtypes, 1 for two-byte sigtypes
    bit 1: 0 for no secret, 1 if secret is required
    bit 2: 0 for no per-client auth, 1 if client private key is required
    bits 7-3: Unused, set to 0

public key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

blinded key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

public key
    Number of bytes as implied by sigtype
```
पोस्ट-प्रोसेसिंग और चेकसम:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
b32 के अंत में कोई भी अप्रयुक्त bits 0 होना चाहिए। एक मानक 56 character (35 byte) address के लिए कोई अप्रयुक्त bits नहीं हैं।

### डिकोडिंग और सत्यापन

```
strip the ".b32.i2p" from the hostname
data = Base32.decode(hostname)
Calculate checksum = CRC-32(data[3:end])
Treat checksum as little-endian.
flags = data[0] ^ (byte) checksum
if 1 byte sigtypes:
    pubkey sigtype = data[1] ^ (byte) (checksum >> 8)
    blinded sigtype = data[2] ^ (byte) (checksum >> 16)
else (2 byte sigtypes):
    pubkey sigtype = data[1] ^ ((byte) (checksum >> 8)) || data[2] ^ ((byte) (checksum >> 16))
    blinded sigtype = data[3] || data[4]
parse the remainder based on the flags to get the public key
```
### गुप्त और निजी कुंजी बिट्स

Secret और private key bits का उपयोग clients, proxies, या अन्य client-side code को यह संकेत देने के लिए किया जाता है कि leaseset को decrypt करने के लिए secret और/या private key की आवश्यकता होगी। विशिष्ट implementations उपयोगकर्ता से आवश्यक डेटा प्रदान करने के लिए प्रॉम्प्ट कर सकती हैं, या यदि आवश्यक डेटा अनुपस्थित है तो connection attempts को अस्वीकार कर सकती हैं।

## कैशिंग

जबकि यह इस विनिर्देश के दायरे से बाहर है, router और/या client को public key से destination की मैपिंग, और इसके विपरीत, को याद रखना और cache करना चाहिए (संभवतः स्थायी रूप से)।

## नोट्स

- लंबाई के आधार पर पुराने और नए flavors को अलग करें। पुराने b32 addresses हमेशा {52 chars}.b32.i2p होते हैं। नए वाले {56+ chars}.b32.i2p होते हैं
- Tor चर्चा thread:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- 2-byte sigtypes की उम्मीद न करें, हम अभी केवल 13 तक हैं। अभी implement करने की जरूरत नहीं।
- नया format jump links में इस्तेमाल हो सकता है (और jump servers द्वारा serve किया जा सकता है) यदि चाहें तो, बिल्कुल b32 की तरह।

## संदर्भ

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - यह भी देखें [RFC 3309](https://tools.ietf.org/html/rfc3309)

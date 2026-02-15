---
title: "Encrypted LeaseSet을 위한 B32"
description: "암호화된 LS2 leaseSet을 위한 Base 32 주소 형식"
slug: "b32encrypted"
aliases:
  - "/ko/docs/specs/b32-for-encrypted-leasesets"
  - "/ko/docs/specs/b32-for-encrypted-leasesets/"
category: "설계"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## 개요

표준 Base 32 ("b32") 주소는 목적지의 해시를 포함합니다. 이는 암호화된 ls2 (제안 123)에서는 작동하지 않습니다.

암호화된 LS2 (제안 123)에 대해서는 전통적인 base 32 주소를 사용할 수 없습니다. 이는 목적지의 해시만을 포함하기 때문입니다. 이것은 블라인드되지 않은 공개 키를 제공하지 않습니다. 클라이언트는 leaseset을 가져오고 복호화하기 위해 목적지의 공개 키, 서명 타입, 블라인드된 서명 타입, 그리고 선택적 비밀 키나 개인 키를 알아야 합니다. 따라서 base 32 주소만으로는 충분하지 않습니다. 클라이언트는 전체 목적지(공개 키를 포함하는) 또는 공개 키 자체가 필요합니다. 클라이언트가 주소록에 전체 목적지를 가지고 있고, 주소록이 해시로 역방향 조회를 지원한다면, 공개 키를 검색할 수 있습니다.

이 형식은 해시 대신 공개 키를 base32 주소에 넣습니다. 이 형식은 또한 공개 키의 서명 유형과 블라인딩 스킴의 서명 유형을 포함해야 합니다.

이 문서는 이러한 주소들을 위한 b32 형식을 명시합니다. 논의 중에 이 새로운 형식을 "b33" 주소라고 언급했지만, 실제 새로운 형식은 일반적인 ".b32.i2p" 접미사를 유지합니다.

## 설계

- 새로운 형식은 unblinded public key, unblinded sig type, 그리고 blinded sig type을 포함합니다.
- 선택적으로 private 링크에만 해당하는 secret 및/또는 private key를 포함합니다.
- 기존의 ".b32.i2p" 접미사를 사용하지만 더 긴 길이를 가집니다.
- 체크섬을 추가합니다.
- 암호화된 leaseSet의 주소는 56개 이상의 인코딩된 문자(35개 이상의 디코딩된 바이트)로 식별되며, 이는 기존 base 32 주소의 52개 문자(32바이트)와 비교됩니다.

## 사양

### 생성 및 인코딩

다음과 같이 {56+ chars}.b32.i2p (바이너리로 35+ chars)의 hostname을 구성합니다:

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
후처리 및 체크섬:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
b32의 끝에 있는 사용되지 않은 비트는 반드시 0이어야 합니다. 표준 56자(35바이트) 주소에는 사용되지 않은 비트가 없습니다.

### 디코딩 및 검증

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
### 비밀키와 개인키 비트

secret과 private key 비트는 클라이언트, 프록시, 또는 기타 클라이언트 측 코드에 leaseset을 복호화하는 데 secret 및/또는 private key가 필요함을 나타내는 데 사용됩니다. 특정 구현에서는 사용자에게 필요한 데이터를 제공하도록 요청하거나, 필요한 데이터가 누락된 경우 연결 시도를 거부할 수 있습니다.

## 캐싱

이 명세의 범위를 벗어나지만, router 및/또는 클라이언트는 공개 키와 destination 간의 매핑을 기억하고 캐시해야 하며(아마도 영구적으로), 그 반대의 경우도 마찬가지입니다.

## 참고사항

- 길이로 기존 방식과 새 방식을 구분합니다. 기존 b32 주소는
  항상 {52글자}.b32.i2p입니다. 새 주소는 {56글자 이상}.b32.i2p입니다
- Tor 토론 스레드:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- 2바이트 sigtypes는 절대 일어나지 않을 것으로 예상됩니다. 아직 13까지밖에 없습니다. 지금 
  구현할 필요가 없습니다.
- 원한다면 새로운 형식을 점프 링크에서 사용할 수 있고 (점프 서버에서 제공 가능), 
  b32와 마찬가지입니다.

## 참고 자료

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - [RFC 3309](https://tools.ietf.org/html/rfc3309)도 참조

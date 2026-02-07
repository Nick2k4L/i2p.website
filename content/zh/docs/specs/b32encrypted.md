---
title: "B32 用于加密 LeaseSet"
description: "加密 LS2 leaseSet 的 Base 32 地址格式"
slug: "b32encrypted"
category: "设计"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## 概述

标准Base 32（"b32"）地址包含目标的哈希值。这对于加密的ls2（提案123）不会生效。

我们无法为加密的 LS2（提案 123）使用传统的 base 32 地址，因为它只包含目标的哈希值。它不提供非盲化的公钥。客户端必须知道目标的公钥、签名类型、盲化签名类型，以及一个可选的密钥或私钥来获取和解密 leaseset。因此，仅有 base 32 地址是不够的。客户端需要完整的目标（包含公钥），或者单独的公钥。如果客户端在地址簿中有完整的目标，并且地址簿支持通过哈希进行反向查找，那么可以检索到公钥。

这种格式将公钥而不是哈希值放入base32地址中。这种格式还必须包含公钥的签名类型和致盲方案的签名类型。

本文档规定了这些地址的 b32 格式。虽然在讨论过程中我们将这种新格式称为"b33"地址，但实际的新格式仍保留通常的".b32.i2p"后缀。

## 设计

- 新格式将包含未盲化的公钥、未盲化签名类型和盲化签名类型。
- 可选择性地包含密钥和/或私钥，仅用于私有链接
- 使用现有的".b32.i2p"后缀，但长度更长。
- 添加校验和。
- 加密 leaseSet 的地址由 56 个或更多编码字符（35 个或更多解码字节）标识，相比之下传统的 base 32 地址为 52 个字符（32 字节）。

## 规范

### 创建和编码

按以下方式构造一个 {56+ 字符}.b32.i2p 的主机名（二进制形式为 35+ 字符）：

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
后处理和校验和：

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
b32末尾的任何未使用位必须为0。对于标准的56字符（35字节）地址，没有未使用的位。

### 解码和验证

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
### 私钥和密钥位数

secret 和 private key 位用于向客户端、代理或其他客户端代码指示，解密 leaseset 时需要 secret 和/或 private key。特定实现可能会提示用户提供所需数据，或在缺少所需数据时拒绝连接尝试。

## 缓存

虽然这超出了本规范的范围，router 和/或客户端必须记住并缓存（可能是持久性的）公钥到目标地址的映射，反之亦然。

## 注意事项

- 通过长度区分新旧格式。旧的 b32 地址始终是 {52 字符}.b32.i2p。新的是 {56+ 字符}.b32.i2p
- Tor 讨论串：
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- 不要期望会出现 2 字节的签名类型，我们目前只到 13。现在无需实现。
- 新格式可以在跳转链接中使用（并由跳转服务器提供），如有需要，就像 b32 一样。

## 参考资料

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - 另请参见 [RFC 3309](https://tools.ietf.org/html/rfc3309)

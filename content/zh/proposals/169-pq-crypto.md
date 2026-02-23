---
title: "后量子密码协议"
aliases: 
number: "169"
author: "zzz, orignal, drzed, eyedeekay"
created: "2025-01-21"
lastupdated: "2026-02-23"
status: "打开"
thread: "http://zzz.i2p/topics/3294"
target: "0.9.80"
toc: true
---

### 状态

| 协议 / 功能 | 状态 |
|--------------------|--------|
| Ratchet | 在 Java I2P 和 i2pd 中完成 |
| NTCP2 | 2026 年第一季度测试版 |
| SSU2 | 即将开始实施，2026 年第二三季度测试版 |
| MLDSA SigTypes | 低优先级，可能 2027 年以后 |
## 概述

虽然对合适的后量子（PQ）密码学的研究和竞争已经进行了十年，但直到最近选择才变得明确。

我们在2022年开始研究PQ密码学的影响 [zzz.i2p](http://zzz.i2p/topics/3294)。

TLS 标准在过去两年中增加了混合加密支持，由于 Chrome 和 Firefox 的支持，现在它已被用于互联网上相当大一部分的加密流量 [Cloudflare](https://blog.cloudflare.com/pq-2024/)。

NIST 最近确定并发布了后量子密码学的推荐算法 [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)。一些常见的密码学库现在已经支持 NIST 标准，或将在不久的将来发布支持。

[Cloudflare](https://blog.cloudflare.com/pq-2024/) 和 [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) 都建议立即开始迁移。另请参阅2022年NSA后量子FAQ [NSA](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)。I2P应该在安全性和密码学方面保持领先地位。现在是实现推荐算法的时候了。使用我们灵活的加密类型和签名类型系统，我们将为混合加密以及后量子和混合签名添加类型。

## 目标

- 选择抗量子算法
- 在适当的I2P协议中添加纯量子和混合算法
- 定义多个变体
- 在实现、测试、分析和研究后选择最佳变体
- 增量添加支持并保持向后兼容性

## 非目标

- 不要更改单向（Noise N）加密协议
- 不要放弃 SHA256，在近期内不受后量子威胁
- 此时不要选择最终的首选变体

## 威胁模型

- OBEP 或 IBGW 处的 router，可能串通，
  存储 garlic 消息以供后续解密（前向保密性）
- 网络观察者
  存储传输消息以供后续解密（前向保密性）
- 网络参与者为 RI、LS、流传输、数据报
  或其他结构伪造签名

## 受影响的协议

我们将按照大致的开发顺序修改以下协议。整体推出时间可能从2025年末到2027年中。详情请参见下面的优先级和推出部分。

| 协议 / 功能 | 状态 |
|--------------------|--------|
| 混合 MLKEM Ratchet 和 LS | 2025年6月批准；2025年8月测试版；2025年11月发布 |
| 混合 MLKEM NTCP2 | 已在实际网络测试，2026年2月批准；2026年5月测试版目标；2026年8月发布目标 |
| 混合 MLKEM SSU2 | 2026年2月批准；2026年8月测试版目标；2026年11月发布目标 |
| MLDSA SigTypes 12-14 | 提案稳定但可能要到2027年才最终确定 |
| MLDSA Dests | 已在实际网络测试，需要网络升级以支持 floodfill |
| 混合 SigTypes 15-17 | 初步阶段 |
| 混合 Dests | |
## 设计

我们将支持 NIST FIPS 203 和 204 标准 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)，这些标准基于但不兼容 CRYSTALS-Kyber 和 CRYSTALS-Dilithium（版本 3.1、3 及更早版本）。

### 密钥交换

我们将在以下协议中支持混合密钥交换：

| 协议    | Noise 类型 | 仅支持 PQ？      | 支持混合？       |
|---------|------------|------------------|-----------------|
| NTCP2   | XK         | no               | yes             |
| SSU2    | XK         | no               | yes             |
| Ratchet | IK         | no               | yes             |
| TBM     | N          | no               | no              |
| NetDB   | N          | no               | no              |
PQ KEM 仅提供临时密钥，不直接支持静态密钥握手，如 Noise XK 和 IK。

Noise N 不使用双向密钥交换，因此不适合用于混合加密。

因此，我们将仅支持混合加密，用于 NTCP2、SSU2 和 Ratchet。我们将按照 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) 定义三种 ML-KEM 变体，总共 3 种新的加密类型。混合类型将仅与 X25519 结合定义。

新的加密类型包括：

| 类型 | 代码 |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
开销将会很大。典型的消息 1 和 2 的大小（对于 XK 和 IK）目前约为 100 字节（在任何额外载荷之前）。根据算法的不同，这将增加 8 倍到 15 倍。

### 签名

我们将在以下结构中支持 PQ 和混合签名：

| 类型 | 仅支持 PQ？ | 支持混合？ |
|------|-------------|-----------|
| RouterInfo | 是 | 是 |
| LeaseSet | 是 | 是 |
| Streaming SYN/SYNACK/Close | 是 | 是 |
| Repliable Datagrams | 是 | 是 |
| Datagram2 (prop. 163) | 是 | 是 |
| I2CP create session msg | 是 | 是 |
| SU3 files | 是 | 是 |
| X.509 certificates | 是 | 是 |
| Java keystores | 是 | 是 |
因此我们将同时支持纯 PQ 和混合签名。我们将按照 [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) 定义三种 ML-DSA 变体，三种与 Ed25519 的混合变体，以及三种仅用于 SU3 文件的带预哈希的纯 PQ 变体，总共 9 种新的签名类型。混合类型将仅与 Ed25519 组合定义。我们将使用标准 ML-DSA，而不是预哈希变体 (HashML-DSA)，除了 SU3 文件。

我们将使用"对冲"或随机化签名变体，而不是"确定性"变体，如 [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) 第 3.4 节所定义。这确保每个签名都是不同的，即使对相同数据进行签名，并提供针对侧信道攻击的额外保护。有关算法选择（包括编码和上下文）的更多详细信息，请参见下面的实现说明部分。

新的签名类型包括：

| 类型 | 代码 |
|------|------|
| MLDSA44 | 12 |
| MLDSA65 | 13 |
| MLDSA87 | 14 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 |
| MLDSA44ph | 18 |
| MLDSA65ph | 19 |
| MLDSA87ph | 20 |
X.509证书和其他DER编码将使用[IETF草案](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)中定义的复合结构和OID。

开销将是巨大的。典型的Ed25519目标地址和router身份大小为391字节。根据算法不同，这些将增加3.5倍到6.8倍。Ed25519签名为64字节。根据算法不同，这些将增加38倍到76倍。典型的已签名RouterInfo、leaseSet、可回复数据报和已签名流消息大约为1KB。根据算法不同，这些将增加3倍到8倍。

由于新的目标地址和router身份类型将不包含填充，它们将不可压缩。在传输过程中被gzip压缩的目标地址和router身份的大小将根据算法增加12倍至38倍。

### 合法组合

对于 Destinations，新的签名类型在 leaseSet 中支持所有加密类型。在密钥证书中将加密类型设置为 NONE (255)。

对于 RouterIdentities，ElGamal 加密类型已被弃用。新的签名类型仅支持 X25519（类型 4）加密。新的加密类型将在 RouterAddresses 中指示。密钥证书中的加密类型将继续为类型 4。

### 需要新的加密算法

- ML-KEM (原 CRYSTALS-Kyber) [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
- ML-DSA (原 CRYSTALS-Dilithium) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
- SHA3-128 (原 Keccak-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf) 仅用于 SHAKE128
- SHA3-256 (原 Keccak-512) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- SHAKE128 和 SHAKE256 (SHA3-128 和 SHA3-256 的 XOF 扩展) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)

SHA3-256、SHAKE128 和 SHAKE256 的测试向量可在 [NIST](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values) 获取。

注意 Java bouncycastle 库支持上述所有功能。C++ 库支持在 OpenSSL 3.5 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/) 中提供。

### 替代方案

我们不会支持 [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) (Sphincs+)，它比 ML-DSA 慢得多且体积更大。我们不会支持即将发布的 FIPS206 (Falcon)，因为它尚未标准化。我们不会支持 NTRU 或其他未被 NIST 标准化的后量子候选算法。

### Rosenpass

有一些研究[论文](https://eprint.iacr.org/2020/379.pdf)探讨了将Wireguard (IK)适配为纯后量子密码学的方法，但该论文中仍存在几个未解决的问题。后来，这种方法被实现为Rosenpass [Rosenpass](https://rosenpass.eu/) [白皮书](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)，用于后量子Wireguard。

Rosenpass 使用类似 Noise KK 的握手，采用预共享的 Classic McEliece 460896 静态密钥（每个 500 KB）和 Kyber-512（本质上是 MLKEM-512）临时密钥。由于 Classic McEliece 密文只有 188 字节，而 Kyber-512 公钥和密文大小合理，两个握手消息都能装入标准 UDP MTU 中。来自 PQ KK 握手的输出共享密钥（osk）被用作标准 Wireguard IK 握手的输入预共享密钥（psk）。因此总共有两个完整的握手，一个是纯 PQ 的，一个是纯 X25519 的。

我们无法用任何这些方法来替换我们的 XK 和 IK 握手，因为：

- 我们无法使用KK，Bob没有Alice的静态密钥
- 500KB的静态密钥太大了
- 我们不希望增加额外的往返

白皮书中有很多有价值的信息，我们会审查其中的想法和启发。待办事项。

## 规范

### 通用结构

按以下方式更新通用结构文档 [/docs/specs/common-structures/](/docs/specs/common-structures/) 中的章节和表格：

### PublicKey

新的公钥类型包括：

| 类型 | 公钥长度 | 起始版本 | 用途 |
|------|----------|---------|------|
| MLKEM512_X25519 | 32 | 0.9.xx | 见提案 169，仅用于 leaseSet，不用于 RI 或 Destination |
| MLKEM768_X25519 | 32 | 0.9.xx | 见提案 169，仅用于 leaseSet，不用于 RI 或 Destination |
| MLKEM1024_X25519 | 32 | 0.9.xx | 见提案 169，仅用于 leaseSet，不用于 RI 或 Destination |
| MLKEM512 | 800 | 0.9.xx | 见提案 169，仅用于握手，不用于 leaseSet、RI 或 Destination |
| MLKEM768 | 1184 | 0.9.xx | 见提案 169，仅用于握手，不用于 leaseSet、RI 或 Destination |
| MLKEM1024 | 1568 | 0.9.xx | 见提案 169，仅用于握手，不用于 leaseSet、RI 或 Destination |
| MLKEM512_CT | 768 | 0.9.xx | 见提案 169，仅用于握手，不用于 leaseSet、RI 或 Destination |
| MLKEM768_CT | 1088 | 0.9.xx | 见提案 169，仅用于握手，不用于 leaseSet、RI 或 Destination |
| MLKEM1024_CT | 1568 | 0.9.xx | 见提案 169，仅用于握手，不用于 leaseSet、RI 或 Destination |
| NONE | 0 | 0.9.xx | 见提案 169，仅用于具有 PQ 签名类型的 destination，不用于 RI 或 leaseSet |
混合公钥是 X25519 密钥。KEM 公钥是从 Alice 发送到 Bob 的临时 PQ 密钥。编码和字节顺序在 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) 中定义。

MLKEM*_CT 密钥并不是真正的公钥，它们是在 Noise 握手过程中从 Bob 发送给 Alice 的"密文"。在此列出是为了完整性。

### PrivateKey

新的私钥类型包括：

| 类型 | 私钥长度 | 版本 | 用途 |
|------|---------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | 参见提案 169，仅用于 Leasesets，不用于 RI 或 Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | 参见提案 169，仅用于 Leasesets，不用于 RI 或 Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | 参见提案 169，仅用于 Leasesets，不用于 RI 或 Destinations |
| MLKEM512 | 1632 | 0.9.xx | 参见提案 169，仅用于握手，不用于 Leasesets、RI 或 Destinations |
| MLKEM768 | 2400 | 0.9.xx | 参见提案 169，仅用于握手，不用于 Leasesets、RI 或 Destinations |
| MLKEM1024 | 3168 | 0.9.xx | 参见提案 169，仅用于握手，不用于 Leasesets、RI 或 Destinations |
混合私钥是 X25519 密钥。KEM 私钥仅适用于 Alice。KEM 编码和字节顺序在 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) 中定义。

### SigningPublicKey

新的签名公钥类型有：

| 类型 | 长度（字节） | 起始版本 | 用途 |
|------|----------------|-------|-------|
| MLDSA44 | 1312 | 0.9.xx | 参见提案 169 |
| MLDSA65 | 1952 | 0.9.xx | 参见提案 169 |
| MLDSA87 | 2592 | 0.9.xx | 参见提案 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 0.9.xx | 参见提案 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 0.9.xx | 参见提案 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 0.9.xx | 参见提案 169 |
| MLDSA44ph | 1344 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构 |
| MLDSA65ph | 1984 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构 |
| MLDSA87ph | 2624 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构 |
混合签名公钥是Ed25519密钥后跟PQ密钥，如[IETF草案](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)中所述。编码和字节顺序在[FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)中定义。

### SigningPrivateKey

新的签名私钥类型有：

| 类型 | 长度（字节） | 起始版本 | 用途 |
|------|----------------|-------|-------|
| MLDSA44 | 2560 | 0.9.xx | 见提案 169 |
| MLDSA65 | 4032 | 0.9.xx | 见提案 169 |
| MLDSA87 | 4896 | 0.9.xx | 见提案 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2592 | 0.9.xx | 见提案 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 4064 | 0.9.xx | 见提案 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4928 | 0.9.xx | 见提案 169 |
| MLDSA44ph | 2592 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构。见提案 169 |
| MLDSA65ph | 4064 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构。见提案 169 |
| MLDSA87ph | 4928 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构。见提案 169 |
混合签名私钥是 Ed25519 密钥后跟 PQ 密钥，如 [IETF 草案](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/) 中所述。编码和字节顺序在 [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) 中定义。

### 签名

新的签名类型包括：

| 类型 | 长度（字节） | 起始版本 | 用途 |
|------|----------------|-------|-------|
| MLDSA44 | 2420 | 0.9.xx | 参见提案 169 |
| MLDSA65 | 3309 | 0.9.xx | 参见提案 169 |
| MLDSA87 | 4627 | 0.9.xx | 参见提案 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2484 | 0.9.xx | 参见提案 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 3373 | 0.9.xx | 参见提案 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4691 | 0.9.xx | 参见提案 169 |
| MLDSA44ph | 2484 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构。参见提案 169 |
| MLDSA65ph | 3373 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构。参见提案 169 |
| MLDSA87ph | 4691 | 0.9.xx | 仅用于 SU3 文件，不用于 netDb 结构。参见提案 169 |
混合签名是 Ed25519 签名后跟 PQ 签名，如 [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/) 中所述。混合签名通过验证两个签名来进行验证，如果任一签名验证失败则整个验证失败。编码和字节序在 [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) 中定义。

### 密钥证书

新的签名公钥类型包括：

| 类型 | 类型代码 | 总公钥长度 | 起始版本 | 用途 |
|------|-----------|-------------------------|-------|-------|
| MLDSA44 | 12 | 1312 | 0.9.xx | 见提案 169 |
| MLDSA65 | 13 | 1952 | 0.9.xx | 见提案 169 |
| MLDSA87 | 14 | 2592 | 0.9.xx | 见提案 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 0.9.xx | 见提案 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 0.9.xx | 见提案 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 0.9.xx | 见提案 169 |
| MLDSA44ph | 18 | n/a | 0.9.xx | 仅用于 SU3 文件 |
| MLDSA65ph | 19 | n/a | 0.9.xx | 仅用于 SU3 文件 |
| MLDSA87ph | 20 | n/a | 0.9.xx | 仅用于 SU3 文件 |
新的加密公钥类型包括：

| 类型 | 类型代码 | 总公钥长度 | 起始版本 | 用途 |
|------|-----------|-------------------------|-------|-------|
| MLKEM512_X25519 | 5 | 32 | 0.9.xx | 参见提案 169，仅用于 LeaseSet，不用于 RI 或 Destination |
| MLKEM768_X25519 | 6 | 32 | 0.9.xx | 参见提案 169，仅用于 LeaseSet，不用于 RI 或 Destination |
| MLKEM1024_X25519 | 7 | 32 | 0.9.xx | 参见提案 169，仅用于 LeaseSet，不用于 RI 或 Destination |
| NONE | 255 | 0 | 0.9.xx | 参见提案 169 |
混合密钥类型绝不会包含在密钥证书中；只会包含在 leaseSet 中。

对于使用 Hybrid 或 PQ 签名类型的目标，加密类型使用 NONE（类型 255），但没有加密密钥，整个 384 字节的主要部分都用于签名密钥。

### 目标地址大小

以下是新 Destination 类型的长度。所有类型的加密类型都是 NONE（类型 255），加密密钥长度被视为 0。整个 384 字节部分用于签名公钥的第一部分。注意：这与 ECDSA_SHA512_P521 和 RSA 签名类型的规范不同，在那些类型中，即使 256 字节的 ElGamal 密钥未被使用，我们仍在目标中保留了它。

无填充。总长度为 7 + 总密钥长度。密钥证书长度为 4 + 超出密钥长度。

MLDSA44 的示例 1319 字节目标字节流：

skey[0:383] 5 (932 >> 8) (932 & 0xff) 00 12 00 255 skey[384:1311]

| 类型 | 类型代码 | 总公钥长度 | 主要 | 多余 | 总目标长度 |
|------|-----------|-------------------------|------|--------|-------------------|
| MLDSA44 | 12 | 1312 | 384 | 928 | 1319 |
| MLDSA65 | 13 | 1952 | 384 | 1568 | 1959 |
| MLDSA87 | 14 | 2592 | 384 | 2208 | 2599 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 384 | 960 | 1351 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 384 | 1600 | 1991 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 384 | 2240 | 2631 |
### RouterIdent 大小

以下是新 Destination 类型的长度。所有类型的加密类型都是 X25519（类型 4）。X25519 公钥之后的整个 352 字节部分用于签名公钥的第一部分。无填充。总长度为 39 + 总密钥长度。密钥证书长度为 4 + 超出密钥长度。

MLDSA44 的 1351 字节 router identity 字节流示例：

enckey[0:31] skey[0:351] 5 (960 >> 8) (960 & 0xff) 00 12 00 4 skey[352:1311]

| 类型 | 类型代码 | 总公钥长度 | 主要 | 多余 | 总RouterIdent长度 |
|------|-----------|-------------------------|------|--------|--------------------------|
| MLDSA44 | 12 | 1312 | 352 | 960 | 1351 |
| MLDSA65 | 13 | 1952 | 352 | 1600 | 1991 |
| MLDSA87 | 14 | 2592 | 352 | 2240 | 2631 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 352 | 992 | 1383 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 352 | 1632 | 2023 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 352 | 2272 | 2663 |
### 握手模式

握手使用 [Noise Protocol](https://noiseprotocol.org/noise.html) 握手模式。

使用以下字母映射：

- e = 一次性临时密钥
- s = 静态密钥
- p = 消息负载
- e1 = 一次性临时PQ密钥，从Alice发送到Bob
- ekem1 = KEM密文，从Bob发送到Alice

以下对 XK 和 IK 的混合前向保密 (hfs) 修改是根据 [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 第 5 节的规定：

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  IK:                       IKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, s, ss, p       -> e, es, e1, s, ss, p
  <- tag, e, ee, se, p     <- tag, e, ee, ekem1, se, p
  <- p                     <- p
  p ->                     p ->

  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
e1 模式定义如下，正如 [Noise HFS 规范](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 第4节中所规定的：

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
ekem1 模式定义如下，如 [Noise HFS 规范](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 第 4 节所指定：

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### Noise 握手 KDF

#### 问题

- 我们是否应该更改握手哈希函数？请参见[比较](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)。
  SHA256 不易受到量子攻击，但如果我们确实想要升级
  哈希函数，现在正是时机，趁着我们正在更改其他方面。
  当前的 IETF SSH 提案 [IETF 草案](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/) 是使用 MLKEM768
  配合 SHA256，以及 MLKEM1024 配合 SHA384。该提案包含
  对安全考虑因素的讨论。
- 我们是否应该停止发送 0-RTT ratchet 数据（除了 LS 之外）？
- 如果我们不发送 0-RTT 数据，是否应该将 ratchet 从 IK 切换到 XK？

#### 概述

本节适用于 IK 和 XK 协议。

混合握手在 [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 中定义。第一条消息从 Alice 发送到 Bob，在消息载荷之前包含 e1（封装密钥）。这被视为额外的静态密钥；对其调用 EncryptAndHash()（作为 Alice）或 DecryptAndHash()（作为 Bob）。然后像往常一样处理消息载荷。

第二条消息，从 Bob 到 Alice，在消息载荷之前包含 ekem1，即密文。这被视为一个额外的静态密钥；对其调用 EncryptAndHash()（作为 Bob）或 DecryptAndHash()（作为 Alice）。然后，计算 kem_shared_key 并调用 MixKey(kem_shared_key)。接着按常规处理消息载荷。

#### 定义的ML-KEM操作

我们定义以下函数，对应于 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) 中定义的加密构建块。

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

请注意，encap_key 和密文都在 Noise 握手消息 1 和 2 的 ChaCha/Poly 块内进行加密。它们将作为握手过程的一部分被解密。

kem_shared_key 通过 MixHash() 混合到链式密钥中。详细信息请参见下文。

#### Alice 消息 1 的 KDF

对于 XK：在 'es' 消息模式之后和载荷之前，添加：

或者

对于 IK：在 'es' 消息模式之后和 's' 消息模式之前，添加：

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF 用于消息 1

对于 XK：在 'es' 消息模式之后和载荷之前，添加：

或者

对于 IK：在 'es' 消息模式之后和 's' 消息模式之前，添加：

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### 消息 2 的 Bob KDF

对于 XK：在 'ee' 消息模式之后和载荷之前，添加：

或者

对于 IK：在 'ee' 消息模式之后和 'se' 消息模式之前，添加：

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### Alice 消息2的密钥派生函数

在 'ee' 消息模式之后（以及在 IK 的 'ss' 消息模式之前），添加：

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### 消息3的KDF（仅XK）

unchanged

#### split() 的密钥派生函数

未更改

### 棘轮

按如下方式更新 ECIES-Ratchet 规范 [/docs/specs/ecies/](/docs/specs/ecies/)：

#### Noise 标识符

- "Noise_IKhfselg2_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1b) 新会话格式（带绑定）

变更：当前的 ratchet 在第一个 ChaCha 部分包含静态密钥，在第二部分包含载荷。使用 ML-KEM 后，现在有三个部分。第一部分包含加密的 PQ 公钥。第二部分包含静态密钥。第三部分包含载荷。

加密格式：

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   New Session Ephemeral Public Key    |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           ML-KEM encap_key            +
  |       ChaCha20 encrypted data         |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for encap_key Section        +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           X25519 Static Key           +
  |       ChaCha20 encrypted data         |
  +             32 bytes                  +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for Static Key Section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
解密格式：

```
Payload Part 1:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM encap_key                +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       X25519 Static Key               +
  |                                       |
  +      (32 bytes)                       +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
大小：

| 类型 | 类型代码 | X 长度 | 消息 1 长度 | 消息 1 加密长度 | 消息 1 解密长度 | PQ 密钥长度 | pl 长度 |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 96+pl | 64+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 912+pl | 880+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1296+pl | 1360+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1680+pl | 1648+pl | 1568+pl | 1568 | pl |
注意有效载荷必须包含一个DateTime块，因此最小有效载荷大小为7。可以据此计算最小消息1的大小。

#### 1g) 新会话回复格式

变更：当前的 ratchet 在第一个 ChaCha 部分有一个空载荷，载荷在第二部分。使用 ML-KEM 后，现在有三个部分。第一部分包含加密的 PQ 密文。第二部分有一个空载荷。第三部分包含载荷。

加密格式：

```
  +----+----+----+----+----+----+----+----+
  |       Session Tag   8 bytes           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Ephemeral Public Key           +
  |                                       |
  +            32 bytes                   +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  | ChaCha20 encrypted ML-KEM ciphertext  |
  +      (see table below for length)     +
  ~                                       ~
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for ciphertext Section         +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for key Section (no data)      +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
解密格式：

```
Payload Part 1:


  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM ciphertext               +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  empty

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
大小：

| 类型 | 类型代码 | Y 长度 | 消息 2 长度 | 消息 2 加密长度 | 消息 2 解密长度 | PQ CT 长度 | 选项长度 |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 72+pl | 32+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 856+pl | 816+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1176+pl | 1136+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1656+pl | 1616+pl | 1568+pl | 1568 | pl |
请注意，虽然消息2通常会有非零载荷，但ratchet规范[/docs/specs/ecies/](/docs/specs/ecies/)并不要求这样做，所以最小载荷大小为0。消息2的最小大小可以相应地计算出来。

### NTCP2

按如下方式更新 NTCP2 规范 [/docs/specs/ntcp2/](/docs/specs/ntcp2/)：

#### Noise 标识符

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

变更：当前的 NTCP2 仅包含 ChaCha 部分中的选项。使用 ML-KEM 后，ChaCha 部分还将包含加密的 PQ 公钥。

变更：当前的 NTCP2 仅包含 ChaCha 部分中的选项。使用 ML-KEM 后，ChaCha 部分还将包含加密的 PQ 公钥。

为了让PQ和非PQ的NTCP2能够在同一个router地址和端口上得到支持，我们使用X值（X25519临时公钥）的最高有效位来标记这是一个PQ连接。对于非PQ连接，这个位始终为未设置状态。

对于 Alice，在消息被 Noise 加密之后，但在对 X 进行 AES 混淆之前，设置 X[31] |= 0x7f。

对于 Bob，在对 X 进行 AES 去混淆后，测试 X[31] & 0x80。如果该位被设置，则用 X[31] &= 0x7f 清除它，并通过 Noise 作为 PQ 连接进行解密。如果该位未设置，则按常规通过 Noise 作为非 PQ 连接进行解密。

对于在不同 router 地址和端口上通告的 PQ NTCP2，这不是必需的。

更多信息请参见下方的已发布地址部分。

原始内容：

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
未加密数据（未显示 Poly1305 认证标签）：

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
注意：消息1选项块中的版本字段必须设置为2，即使对于PQ连接也是如此。

大小：

| 类型 | 类型代码 | X 长度 | 消息 1 长度 | 消息 1 加密长度 | 消息 1 解密长度 | PQ 密钥长度 | 可选长度 |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
注意：类型代码仅供内部使用。Router 将保持类型 4，支持情况将在 router 地址中指示。

#### 2) SessionCreated

原始内容：

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
未加密数据（未显示 Poly1305 验证标签）：

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
大小：

| 类型 | 类型代码 | Y 长度 | 消息 2 长度 | 消息 2 加密长度 | 消息 2 解密长度 | PQ CT 长度 | 可选长度 |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
注意：类型代码仅供内部使用。Router将保持类型4，支持情况将在router地址中指示。

#### 3) SessionConfirmed

未更改

#### 密钥派生函数 (KDF)（用于数据阶段）

未更改

#### 已发布地址

在所有情况下，像往常一样使用 NTCP2 传输名称。

使用与非PQ、非防火墙相同的地址/端口。仅支持一种PQ变体。在router地址中，发布v=2（如常）和新参数pq=[3|4|5]以指示MLKEM 512/768/1024。Alice在会话请求中设置临时密钥的最高有效位（key[31] & 0x80）以表明这是混合连接。见上文。较旧的router将忽略pq参数并照常进行非pq连接。

不支持与非PQ不同的地址/端口，或仅PQ、非防火墙模式。这将不会实施，直到非PQ NTCP2被禁用，即从现在起的几年后。当非PQ被禁用时，可能支持多个PQ变体，但每个地址只支持一个。在router地址中，发布v=[3|4|5]来表示MLKEM 512/768/1024。Alice不设置临时密钥的MSB。较旧的router将检查v参数并跳过此地址，因为不受支持。

防火墙地址（未发布IP）：在 router 地址中，发布 v=2（如常）。无需发布 pq 参数。

Alice可以使用Bob发布的PQ变体连接到PQ Bob，无论Alice是否在其router信息中宣传pq支持，或者她是否宣传相同的变体。

#### 最大填充

在当前规范中，消息 1 和消息 2 被定义为具有"合理"数量的填充，建议范围为 0-31 字节，且未指定最大值。

Java I2P为非PQ连接实现了最大256字节的填充，但这之前没有被记录在文档中。

使用定义的消息大小作为最大填充量，也就是说，最大填充量将使消息大小翻倍，如下所示：

| 消息最大填充 | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------|-----------|-----------|------------|
| Session Request  |       880   |     1264   |    1648  |
| Session Created  |       848   |     1136   |    1616	 |
### SSU2

按如下方式更新 SSU2 规范 [/docs/specs/ssu2/](/docs/specs/ssu2/)：

#### 噪声标识符

- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"

请注意，MLKEM-1024 不支持用于 SSU2，因为密钥过大，无法放入标准的 1500 字节数据报中。

#### 长标头

长头部长度为32字节。它在会话创建之前使用，用于Token Request、SessionRequest、SessionCreated和Retry。它也用于会话外的Peer Test和Hole Punch消息。

在以下消息中，将长头部中的 ver（版本）字段设置为 3 或 4，以指示 MLKEM-512 或 MLKEM-768。

- (0) 会话请求
- (1) 会话已创建
- (9) 重试
- (10) 令牌请求
- (11) 打洞

在以下消息中，将长头部中的 ver（版本）字段设置为 2，如常规操作，即使支持 MLKEM-512 或 MLKEM-768。如果对端支持，实现也可以将值设置为 3 或 4，但这不是必需的。实现应接受任何 2-4 范围内的值。

- (7) 对等测试（会话外消息 5-7）

讨论：将版本字段设置为 3 或 4 对于所有消息类型可能并非严格必要，但这样做有助于更早地检测不支持的后量子连接故障。Token Request 和 Retry（类型 9 和 10）应该使用版本 3/4 以保持一致性。Hole Punch 消息（类型 11）可能不需要此处理，但我们将遵循相同的模式以保持统一性。Peer Test 消息（类型 7）是会话外的，并不表示启动会话的意图。

在头部加密之前：

```

  +----+----+----+----+----+----+----+----+
  |      Destination Connection ID        |
  +----+----+----+----+----+----+----+----+
  |   Packet Number   |type| ver| id |flag|
  +----+----+----+----+----+----+----+----+
  |        Source Connection ID           |
  +----+----+----+----+----+----+----+----+
  |                 Token                 |
  +----+----+----+----+----+----+----+----+

  Destination Connection ID :: 8 bytes, unsigned big endian integer

  Packet Number :: 4 bytes, unsigned big endian integer

  type :: The message type = 0, 1, 7, 9, 10, or 11

  ver :: The protocol version = 2, 3, or 4 for non-PQ, MLKEM512, MLKEM768

  id :: 1 byte, the network ID (currently 2, except for test networks)

  flag :: 1 byte, unused, set to 0 for future compatibility

  Source Connection ID :: 8 bytes, unsigned big endian integer

  Token :: 8 bytes, unsigned big endian integer

```
#### 短标头

unchanged

#### SessionRequest (类型 0)

变更：当前的 SSU2 在 ChaCha 部分只包含块数据。使用 ML-KEM 后，ChaCha 部分还将包含加密的 PQ 公钥。

用于伪装保护的 KDF 更改：为了解决提案 165 [Prop165]_ 中提出的问题，但采用不同的解决方案，我们修改了会话请求的 KDF。这仅适用于 PQ 会话。非 PQ 会话的 KDF 保持不变。

```

// End of KDF for initial chain key (unchanged)
  // Bob static key
  // MixHash(bpk)
  h = SHA256(h || bpk);

  // Start of KDF for session request
  // NEW for PQ only
  // bhash = Bob router hash (32 bytes)
  // MixHash(bhash)
  h = SHA256(h || bhash);

  // Rest of KDF for session request, unchanged, as in SSU2 spec
  // MixHash(header)
  h = SHA256(h || header)

  ...

```
原始内容：

```
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 0-15, ChaCha20     |
  +  encrypted with Bob intro key         +
  |    See Header Encryption KDF          |
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 16-31, ChaCha20    |
  +  encrypted with Bob intro key n=0     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +       X, ChaCha20 encrypted           +
  |       with Bob intro key n=0          |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaCha20 encrypted data (MLKEM)     |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaCha20 encrypted data (payload)   |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Poly1305 MAC (16 bytes)        +
  |                                       |
  +----+----+----+----+----+----+----+----+


```
未加密数据（未显示 Poly1305 认证标签）：

```
  +----+----+----+----+----+----+----+----+
  |      Destination Connection ID        |
  +----+----+----+----+----+----+----+----+
  |   Packet Number   |type| ver| id |flag|
  +----+----+----+----+----+----+----+----+
  |        Source Connection ID           |
  +----+----+----+----+----+----+----+----+
  |                 Token                 |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |     see below for allowed blocks      |
  +----+----+----+----+----+----+----+----+
```
大小，不包括IP开销：

| 类型 | 类型代码 | X 长度 | 消息 1 长度 | 消息 1 加密长度 | 消息 1 解密长度 | PQ 密钥长度 | pl 长度 |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 896+pl | 832+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1280+pl | 1216+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | n/a | 太大 | | | | |
注意：类型代码仅供内部使用。Router 将保持类型 4，支持情况将在 router 地址中指示。

MLKEM768_X25519 的最小 MTU：IPv4 约为 1316，IPv6 约为 1336。

#### SessionCreated (类型 1)

更改：当前的 SSU2 在 ChaCha 部分只包含块数据。使用 ML-KEM 后，ChaCha 部分还将包含加密的 PQ 公钥。

原始内容：

```
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 0-15, ChaCha20     |
  +  encrypted with Bob intro key and     +
  | derived key, see Header Encryption KDF|
  +----+----+----+----+----+----+----+----+
  |  Long Header bytes 16-31, ChaCha20    |
  +  encrypted with derived key n=0       +
  |  See Header Encryption KDF            |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +       Y, ChaCha20 encrypted           +
  |       with derived key n=0            |
  +              (32 bytes)               +
  |       See Header Encryption KDF       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaCha20 data (MLKEM)               |
  +   Encrypted and authenticated data    +
  |  length varies                        |
  +  k defined in KDF for Session Created +
  |  n = 0; see KDF for associated data   |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaCha20 data (payload)             |
  +   Encrypted and authenticated data    +
  |  length varies                        |
  +  k defined in KDF for Session Created +
  |  n = 0; see KDF for associated data   |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Poly1305 MAC (16 bytes)        +
  |                                       |
  +----+----+----+----+----+----+----+----+


```
未加密数据（未显示 Poly1305 认证标签）：

```
  +----+----+----+----+----+----+----+----+
  |      Destination Connection ID        |
  +----+----+----+----+----+----+----+----+
  |   Packet Number   |type| ver| id |flag|
  +----+----+----+----+----+----+----+----+
  |        Source Connection ID           |
  +----+----+----+----+----+----+----+----+
  |                 Token                 |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |      see below for allowed blocks     |
  +----+----+----+----+----+----+----+----+
```
大小，不包括 IP 开销：

| 类型 | 类型代码 | Y 长度 | 消息 2 长度 | 消息 2 加密长度 | 消息 2 解密长度 | PQ CT 长度 | pl 长度 |
|------|-----------|-------|-----------|---------------|---------------|-----------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 864+pl | 800+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1184+pl | 1118+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | n/a | 太大 | | | | |
注意：类型代码仅供内部使用。Router 将保持类型 4，并且支持将在 router 地址中指示。

MLKEM768_X25519的最小MTU：IPv4约为1316，IPv6约为1336。

#### SessionConfirmed (类型 2)

unchanged

#### 数据阶段的 KDF

unchanged

#### 中继和对等测试

以下数据块包含版本字段。它们将保持版本 2（为了与非 PQ Bob 兼容），并且不会为 PQ 更改为版本 3/4。

- 中继请求
- 中继响应
- 中继介绍
- 对等测试

PQ 签名：Relay 块、Peer Test 块和 Peer Test 消息都包含签名。不幸的是，PQ 签名大于 MTU。目前没有机制可以将 Relay 或 Peer Test 块或消息分片到多个 UDP 数据包中。必须扩展协议以支持分片。这将在待定的单独提案中完成。在完成之前，将不支持 Relay 和 Peer Test。

#### 已发布地址

在所有情况下，像往常一样使用 SSU2 传输名称。不支持 MLKEM-1024。

使用与非PQ、非防火墙相同的地址/端口。支持一种或两种PQ变体。在router地址中，发布v=2（如常）和新参数pq=[3|4|3,4]来表示MLKEM 512/768/两者。较旧的router将忽略pq参数并照常进行非pq连接。

不支持与非PQ使用不同的地址/端口，或仅PQ、非防火墙模式。这将不会实现，直到非PQ SSU2被禁用，这将是几年后的事情。当非PQ被禁用时，支持一个或两个PQ变体。在router地址中，发布v=[3|4|3,4]以表示MLKEM 512/768/两者。较旧的router将检查v参数并跳过此地址，视为不支持。

防火墙地址（未发布IP）：在router地址中，发布v=2（如常）。在防火墙地址中必须发布pq参数，以支持中继。

Alice可以使用Bob发布的PQ变体连接到PQ Bob，无论Alice是否在她的router信息中宣传pq支持，或者她是否宣传相同的变体。

#### MTU

使用 MLKEM768 时要注意不要超过 MTU。SSU2 的最小 MTU 是 1280，这是消息 1 不含填充的大小。如果 Alice 或 Bob 的 MTU 是 1280，则不要在消息 1 中包含填充。

#### 问题

我们可以在内部使用版本字段，对 MLKEM512 使用版本 3，对 MLKEM768 使用版本 4。

对于消息1和消息2，MLKEM768会使数据包大小超出1280字节的最小MTU。如果MTU过低，可能就不支持该连接。

对于消息1和2，MLKEM1024会使数据包大小超过1500的最大MTU。这将需要对消息1和2进行分片处理，这会是一个很大的复杂问题。可能不会这样做。

中继和节点测试：见上文

### 流媒体

TODO: 是否有更高效的方法来定义签名/验证以避免复制签名？

### SU3 文件

待办事项

[IETF 草案](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) 第 8.1 节禁止在 X.509 证书中使用 HashML-DSA，并且不为 HashML-DSA 分配 OID，这是因为实现复杂性和安全性降低的考虑。

对于 SU3 文件的仅 PQ 签名，请使用证书中非预哈希变体的 [IETF 草案](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) 中定义的 OID。我们不定义 SU3 文件的混合签名，因为我们可能需要对文件进行两次哈希（尽管 HashML-DSA 和 X2559 使用相同的哈希函数 SHA512）。此外，在 X.509 证书中连接两个密钥和签名将完全不符合标准。

请注意，我们不允许对 SU3 文件使用 Ed25519 签名，虽然我们已经定义了 Ed25519ph 签名，但我们从未就其 OID 达成一致，也从未使用过它。

SU3 文件不允许使用普通的签名类型；请使用 ph（预哈希）变体。

### 其他规范

新的最大 Destination 大小将为 2599（base 64 编码为 3468）。

更新其他提供 Destination 大小指导的文档，包括：

- SAMv3
- Bittorrent
- 开发者指南
- 命名 / 地址簿 / 跳转服务器
- 其他文档

## 开销分析

### 密钥交换

大小增加（字节）：

| 类型 | 公钥 (消息 1) | 密文 (消息 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
速度：

据 [Cloudflare](https://blog.cloudflare.com/pq-2024/) 报告的速度：

| 类型 | 相对速度 |
|------|----------------|
| X25519 DH/keygen | 基准线 |
| MLKEM512 | 快 2.25 倍 |
| MLKEM768 | 快 1.5 倍 |
| MLKEM1024 | 1 倍（相同） |
| XK | 4x DH (keygen + 3 DH) |
| MLKEM512_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 4.9x DH = 慢 22% |
| MLKEM768_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 5.3x DH = 慢 32% |
| MLKEM1024_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 6x DH = 慢 50% |
Java 中的初步测试结果：

| 类型 | 相对 DH/encaps | DH/decaps | keygen |
|------|----------------|-----------|--------|
| X25519 | 基准 | 基准 | 基准 |
| MLKEM512 | 快29倍 | 快22倍 | 快17倍 |
| MLKEM768 | 快17倍 | 快14倍 | 快9倍 |
| MLKEM1024 | 快12倍 | 快10倍 | 快6倍 |
### 签名

大小：

假设 RIs 使用 X25519 加密类型，典型的密钥、签名、RIdent、Dest 大小或大小增长（包含 Ed25519 作为参考）。列出的 Router Info、LeaseSet、可回复数据报以及两个流传输（SYN 和 SYN ACK）数据包的增加大小。当前的 Destinations 和 Leasesets 包含重复填充，在传输中是可压缩的。新类型不包含填充且不可压缩，导致传输中的大小增长要高得多。请参见上述设计部分。

| 类型 | 公钥 | 签名 | 密钥+签名 | RIdent | Dest | RInfo | LS/Streaming/Datagram (每条消息) |
|------|--------|-----|---------|--------|------|-------|----------------------------------|
| EdDSA_SHA512_Ed25519 | 32 | 64 | 96 | 391 | 391 | 基准 | 基准 |
| MLDSA44 | 1312 | 2420 | 3732 | 1351 | 1319 | +3316 | +3284 |
| MLDSA65 | 1952 | 3309 | 5261 | 1991 | 1959 | +5668 | +5636 |
| MLDSA87 | 2592 | 4627 | 7219 | 2631 | 2599 | +7072 | +7040 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 2484 | 3828 | 1383 | 1351 | +3412 | +3380 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 3373 | 5357 | 2023 | 1991 | +5668 | +5636 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 4691 | 7315 | 2663 | 2631 | +7488 | +7456 |
速度：

根据 [Cloudflare](https://blog.cloudflare.com/pq-2024/) 报告的速度：

| 类型 | 相对速度标志 | 验证 |
|------|---------------------|--------|
| EdDSA_SHA512_Ed25519 | 基准 | 基准 |
| MLDSA44 | 慢5倍 | 快2倍 |
| MLDSA65 | ??? | ??? |
| MLDSA87 | ??? | ??? |
Java 初步测试结果：

| 类型 | 相对签名速度 | 验证 | 密钥生成 |
|------|-------------|------|----------|
| EdDSA_SHA512_Ed25519 | 基准 | 基准 | 基准 |
| MLDSA44 | 慢 4.6 倍 | 快 1.7 倍 | 快 2.6 倍 |
| MLDSA65 | 慢 8.1 倍 | 相同 | 快 1.5 倍 |
| MLDSA87 | 慢 11.1 倍 | 慢 1.5 倍 | 相同 |
## 安全分析

NIST 安全类别在 [NIST presentation](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) 第 10 页幻灯片中有总结。初步标准：对于混合协议，我们的最低 NIST 安全类别应该是 2，对于纯 PQ 协议应该是 3。

| 类别 | 安全级别相当于 |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### 握手

这些都是混合协议。实现应优先选择 MLKEM768；MLKEM512 不够安全。

NIST 安全类别 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| 算法 | 安全类别 |
|-----------|-------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
### 签名

此提案定义了混合和仅PQ的签名类型。MLDSA44混合类型比MLDSA65仅PQ类型更可取。MLDSA65和MLDSA87的密钥和签名大小对我们来说可能太大了，至少在初期是这样。

NIST 安全类别 [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)：

| 算法 | 安全类别 |
|-----------|-------------------|
| MLDSA44 | 2 |
| MLKEM67 | 3 |
| MLKEM87 | 5 |
## 类型首选项

虽然我们将定义并实现3种加密类型和9种签名类型，但我们计划在开发过程中测量性能，并进一步分析结构大小增加的影响。我们还将继续研究并监控其他项目和协议的发展。

经过一年或更长时间的开发后，我们将尝试为每个用例确定首选类型或默认类型。选择需要在带宽、CPU和估计安全级别之间进行权衡。并非所有类型都适合或允许用于所有用例。

初步偏好设置如下，可能会有所变更：

加密：MLKEM768_X25519

签名：MLDSA44_EdDSA_SHA512_Ed25519

初步限制如下，可能会有变更：

加密：SSU2不允许使用MLKEM1024_X25519

签名：MLDSA87 和混合变体可能过于庞大；MLDSA65 和混合变体可能也过于庞大

## 实现说明

### 库支持

Bouncycastle、BoringSSL 和 WolfSSL 库现在支持 MLKEM 和 MLDSA。OpenSSL 的支持将在 2025 年 4 月 8 日的 3.5 版本中提供 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)。

由 Java I2P 适配的 southernstorm.com Noise 库包含对混合握手的初步支持，但我们将其作为未使用的功能移除了；我们需要重新添加它并更新以匹配 [Noise HFS 规范](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)。

### 签名变体

我们将使用"对冲"或随机化签名变体，而不是"确定性"变体，如 [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) 第 3.4 节所定义。这确保了每个签名都是不同的，即使是对相同数据进行签名，并提供了针对侧信道攻击的额外保护。虽然 [FIPS 204](https://nvlpubs.nist.gov.nistpubs/FIPS/NIST.FIPS.204.pdf) 规定"对冲"变体是默认选项，但在各种库中这可能成立也可能不成立。实现者必须确保使用"对冲"变体进行签名。

我们使用标准的签名过程（称为纯 ML-DSA 签名生成），该过程在内部将消息编码为 0x00 || len(ctx) || ctx || message，其中 ctx 是大小为 0x00..0xFF 的可选值。我们不使用任何可选上下文。len(ctx) == 0。此过程在 [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) 算法 2 步骤 10 和算法 3 步骤 5 中定义。请注意，一些已发布的测试向量可能需要设置消息不进行编码的模式。

### 可靠性

大小增加将导致 NetDB 存储、流式握手和其他消息的 tunnel 碎片化大幅增加。请检查性能和可靠性变化。

### 结构体大小

查找并检查任何限制 router info 和 leaseSet 字节大小的代码。

### NetDB

审查并可能减少在内存或磁盘上存储的最大 LS/RI 数量，以限制存储增长。提高 floodfill 的最低带宽要求？

### Ratchet

#### 共享 tunnel

基于消息 1（新会话消息）的长度检查，应该可以在同一个 tunnel 上自动分类/检测多个协议。以 MLKEM512_X25519 为例，消息 1 的长度比当前的 ratchet 协议大 816 字节，最小消息 1 大小（仅包含 DateTime 负载）为 919 字节。当前 ratchet 的大多数消息 1 大小的负载都小于 816 字节，因此可以将它们归类为非混合 ratchet。大消息可能是很少见的 POST 请求。

因此推荐的策略是：

- 如果消息 1 小于 919 字节，则使用当前的 ratchet 协议。
- 如果消息 1 大于或等于 919 字节，则可能是 MLKEM512_X25519。
  先尝试 MLKEM512_X25519，如果失败，则尝试当前的 ratchet 协议。

这应该允许我们在同一个目标上高效地支持标准 ratchet 和混合 ratchet，就像我们之前在同一个目标上支持 ElGamal 和 ratchet 一样。因此，我们可以比无法在同一目标上支持双协议的情况下更快地迁移到 MLKEM 混合协议，因为我们可以向现有目标添加 MLKEM 支持。

必须支持的组合包括：

- X25519 + MLKEM512
- X25519 + MLKEM768
- X25519 + MLKEM1024

以下组合可能比较复杂，不要求必须支持，但可能会根据具体实现而定：

- 多个 MLKEM
- ElG + 一个或多个 MLKEM
- X25519 + 一个或多个 MLKEM
- ElG + X25519 + 一个或多个 MLKEM

我们可能不会尝试在同一个目标上支持多个 MLKEM 算法（例如，MLKEM512_X25519 和 MLKEM_768_X25519）。只选择一个即可；但是，这取决于我们选择一个首选的 MLKEM 变体，这样 HTTP 客户端 tunnel 就可以使用一个。这依赖于具体实现。

我们可能尝试在同一个 destination 上支持三种算法（例如 X25519、MLKEM512_X25519 和 MLKEM769_X25519）。分类和重试策略可能过于复杂。配置和配置UI可能过于复杂。依赖于具体实现。

我们可能不会尝试在同一个目标上同时支持ElGamal和混合算法。ElGamal已经过时，而且只有ElGamal + 混合（没有X25519）意义不大。此外，ElGamal和混合新会话消息都很大，因此分类策略通常必须尝试两种解密，这会导致效率低下。具体实现取决于实现方式。

客户端可以在相同的隧道上为X25519协议和混合协议使用相同或不同的X25519静态密钥，这取决于具体实现。

#### 前向保密

ECIES 规范允许在 New Session Message 有效载荷中包含 Garlic Messages，这样可以实现 0-RTT 传输初始流数据包（通常是 HTTP GET）以及客户端的 leaseSet。然而，New Session Message 有效载荷不具备前向保密性。由于本提案强调增强 ratchet 的前向保密性，实现可能会或应该推迟包含流载荷或完整流消息，直到第一个 Existing Session Message。这样做的代价是失去 0-RTT 传输能力。策略也可能取决于流量类型、tunnel 类型，或者例如 GET 与 POST 的区别。具体实现自行决定。

#### 新会话大小

在同一个destination上使用MLKEM、MLDSA或两者结合，会如上所述大幅增加New Session Message的大小。这可能会显著降低New Session Message通过tunnel传输的可靠性，因为它们必须被分片为多个1024字节的tunnel消息。传输成功率与分片数量成指数关系。实现可以使用各种策略来限制消息大小，但代价是放弃0-RTT传输。具体取决于实现。

### NTCP2

我们在会话请求中设置临时密钥的MSB（key[31] & 0x80）来表示这是一个混合连接。这允许我们在同一端口上同时运行标准NTCP和混合NTCP。只支持一种混合变体，并在router地址中公告。例如，v=2,3或v=2,4或v=2,5。

#### 混淆

作为 Alice，对于 PQ 连接，在混淆之前，设置 X[31] |= 0x80。这使得 X 成为一个无效的 X25519 公钥。混淆后，AES-CBC 会将其随机化。混淆后 X 的最高有效位将是随机的。

作为 Bob，在去混淆后测试 (X[31] & 0x80) != 0。如果是，则这是一个 PQ 连接。

NTCP2-PQ 所需的最低 router 版本待定。

注意：类型代码仅供内部使用。Router 将保持类型 4，支持情况将在 router 地址中指示。

### SSU2

我们在长报头中使用版本字段，对于 MLKEM512 设置为 3，对于 MLKEM768 设置为 4。地址中的 v=2,3,4 就足够了。

检查并验证 SSU2 能够处理跨多个数据包（6-8个？）分片的 MLDSA 签名 RI。

注意：类型代码仅供内部使用。router 将保持类型 4，支持情况将在 router 地址中指示。

## Router 兼容性

### 传输名称

在所有情况下，都要使用通常的 NTCP2 和 SSU2 传输名称。

### Router 加密类型

我们有几个替代方案需要考虑：

#### Type 5/6/7 Router

不推荐。仅使用上面列出的与router类型匹配的新传输协议。旧版router无法连接、构建tunnel或发送netDb消息。需要经过几个发布周期来调试并确保支持后才能默认启用。相比下面的替代方案，可能会将推广时间延长一年或更久。

#### Type 4 Router

推荐。由于PQ不影响X25519静态密钥或N握手协议，我们可以保持router为类型4，只需要宣传新的传输方式。较旧的router仍然可以连接、构建tunnel通过，或发送netDb消息到。

#### 建议

建议在 Ratchet、NTCP2 和 SSU2 中使用 MLKEM-768，因为它在安全性和密钥长度之间达到了最佳平衡。

### Router 签名类型

#### Type 12-17 Router

较旧的 router 会验证 RI，因此无法连接、通过其构建 tunnel 或向其发送 netDb 消息。需要几个发布周期来调试并确保支持，然后才能默认启用。这将面临与加密类型 5/6/7 部署相同的问题；相比上述列出的类型 4 加密类型部署替代方案，可能会延长部署时间一年或更久。

没有替代方案。

### LS 加密类型

#### 类型 5-7 LS 密钥

这些可能会出现在具有较旧类型4 X25519密钥的leaseSet中。较旧的router会忽略未知的密钥。

Destinations 可以支持多种密钥类型，但只能通过对消息1使用每个密钥进行试探性解密来实现。这种开销可以通过维护每个密钥成功解密次数的统计，并优先尝试使用最多的密钥来缓解。Java I2P 在同一个 destination 上对 ElGamal+X25519 使用这种策略。

### 目标签名类型

#### 类型 12-17 目标地址

Router 会验证 leaseSet 签名，因此无法连接或接收类型 12-17 目标的 leaseSet。需要几个发布周期来调试并确保支持，然后才能默认启用。

无替代方案。

## 优先级和推出计划

最有价值的数据是端到端流量，使用ratchet加密。作为tunnel跳跃之间的外部观察者，这些数据被额外加密了两次，包括tunnel加密和传输加密。作为OBEP和IBGW之间的外部观察者，只被额外加密了一次，即传输加密。作为OBEP或IBGW参与者，ratchet是唯一的加密。然而，由于tunnel是单向的，要在ratchet握手中捕获两个消息需要串通的router，除非tunnel的OBEP和IBGW构建在同一个router上。

目前最令人担忧的后量子威胁模型是存储今天的流量，以便在许多年后进行解密（前向保密）。混合方法将能够保护这一点。

PQ威胁模型中在合理时间内（比如几个月）破解认证密钥，然后冒充认证或近实时解密的威胁还很遥远？那时我们才需要迁移到PQC静态密钥。

因此，最早的 PQ 威胁模型是 OBEP/IBGW 存储流量以供稍后解密。我们应该首先实现混合棘轮。

Ratchet是最高优先级。传输协议次之。签名是最低优先级。

签名的推出也将比加密推出晚一年或更长时间，因为不可能实现向后兼容。此外，MLDSA在行业中的采用将由CA/Browser Forum和证书颁发机构进行标准化。CA首先需要硬件安全模块(HSM)支持，而这目前还不可用[CA/Browser Forum](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)。我们预期CA/Browser Forum将推动对特定参数选择的决策，包括是否支持或要求复合签名[IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)。

| 里程碑 | 目标 |
|-----------|--------|
| Ratchet beta | 2025年末 |
| 选择最佳加密类型 | 2026年初 |
| NTCP2 beta | 2026年初 |
| SSU2 beta | 2026年中 |
| Ratchet 生产版 | 2026年中 |
| Ratchet 默认 | 2026年末 |
| 签名 beta | 2026年末 |
| NTCP2 生产版 | 2026年末 |
| SSU2 生产版 | 2027年初 |
| 选择最佳签名类型 | 2027年初 |
| NTCP2 默认 | 2027年初 |
| SSU2 默认 | 2027年中 |
| 签名生产版 | 2027年中 |
## 迁移

如果我们无法在同一个tunnel上同时支持新旧ratchet协议，迁移将会变得更加困难。

我们应该能够像处理X25519那样，逐一尝试不同方法来验证。

## 问题

- Noise Hash 选择 - 继续使用 SHA256 还是升级？
  SHA256 在未来 20-30 年内应该都是安全的，不受量子计算威胁，
  参见 [NIST 演示文稿](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf) 和 [NCCOE 演示文稿](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)。
  如果 SHA256 被破解，我们还有更严重的问题（netDb）。
- NTCP2 独立端口、独立 router 地址
- SSU2 中继 / 对等测试
- SSU2 版本字段
- SSU2 router 地址版本

## 参考文献

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)

---
title: "通用结构规范"
description: "所有 I2P 协议通用的数据类型"
slug: "common-structures"
category: "设计"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

本文档描述了所有 I2P 协议中常见的一些数据类型，如 [I2NP](/docs/specs/i2np/)、[I2CP](/docs/specs/i2cp/)、[SSU](/docs/legacy/ssu/) 等。

## 通用类型规范

### 整数

#### 描述

表示一个非负整数。

#### 目录

1到8个字节，采用网络字节序（大端序）表示无符号整数。

### 日期

#### 描述

自1970年1月1日GMT时区午夜以来的毫秒数。如果数字为0，则日期未定义或为空。

#### 目录

8 字节 [Integer](#integer)

### 字符串

#### 描述

表示一个 UTF-8 编码的字符串。

#### 目录

1个或更多字节，其中第一个字节是字符串中的字节数（不是字符数！），其余0-255个字节是非空终止的UTF-8编码字符数组。长度限制为255字节（不是字符数）。长度可以为0。

### PublicKey

#### 描述

这种结构用于 ElGamal 或其他非对称加密中，仅表示指数，而不是素数，素数是常量并在密码学规范 [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) 中定义。其他加密方案正在定义中，请参见下表。

#### 目录

密钥类型和长度从上下文推断，或在目标地址或 RouterInfo 的密钥证书中指定，或在 [LeaseSet2](#leaseset2) 或其他数据结构的字段中指定。默认类型是 ElGamal。从 0.9.38 版本开始，可能支持其他类型，具体取决于上下文。除非另有说明，密钥采用大端序格式。

从 0.9.44 版本开始，Destinations 和 LeaseSet2 支持 X25519 密钥。从 0.9.48 版本开始，RouterIdentities 支持 X25519 密钥。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">800</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1184</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1088</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PublicKey.html

### 私钥

#### 描述

这种结构用于 ElGamal 或其他非对称解密，仅表示指数，而不是在密码学规范 [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) 中定义的常数素数。其他加密方案正在定义过程中，请参见下表。

#### 目录

密钥类型和长度从上下文推断或单独存储在数据结构或私钥文件中。默认类型是 ElGamal。从 0.9.38 版本开始，根据上下文可能支持其他类型。除非另有说明，密钥采用大端序。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1632</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2400</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3168</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PrivateKey.html

### SessionKey

#### 描述

这个结构用于对称AES256加密和解密。

#### 目录

32 字节

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### 签名公钥

#### 描述

此结构用于验证签名。

#### 目录

密钥类型和长度从上下文推断或在目标的密钥证书中指定。默认类型是 DSA_SHA1。从 0.9.12 版本开始，根据上下文可能支持其他类型。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### 注释

* 当密钥由两个元素组成时（例如点 X,Y），通过在必要时用前导零将每个元素填充到 length/2 来进行序列化。

* 所有类型都是大端序（Big Endian），除了 EdDSA 和 RedDSA，它们以小端序（Little Endian）格式存储和传输。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### 描述

此结构用于创建签名。

#### 目录

密钥类型和长度在创建时指定。默认类型是 DSA_SHA1。从 0.9.12 版本开始，根据上下文可能支持其他类型。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### 注释

* 当密钥由两个元素组成时（例如点 X,Y），通过在必要时用前导零将每个元素填充到 length/2 来进行序列化。

* 除了 EdDSA 和 RedDSA 以小端格式存储和传输外，所有类型都使用大端格式。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### 签名

#### 描述

这个结构表示某些数据的签名。

#### 目录

签名类型和长度是从所使用的密钥类型推断出来的。默认类型是DSA_SHA1。从0.9.12版本开始，根据上下文可能支持其他类型。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### 注释

* 当签名由两个元素组成时（例如值 R,S），通过在必要时用前导零将每个元素填充到 length/2 来进行序列化。

* 所有类型均为大端序，除了 EdDSA 和 RedDSA，它们以小端序格式存储和传输。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### 哈希

#### 描述

表示某些数据的 SHA256 值。

#### 目录

32 字节

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### 会话标签

注意：ECIES-X25519 目标节点（ratchet）和 ECIES-X25519 router 的 Session Tags 为 8 字节。请参阅 [ECIES](/docs/specs/ecies/) 和 [ECIES-ROUTERS](/docs/specs/ecies-routers/)。

#### 描述

一个随机数

#### 目录

32 字节

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### 描述

定义每个 router 在 tunnel 中的唯一标识符。Tunnel ID 通常大于零；除非特殊情况，否则不要使用零值。

#### 目录

4 字节 [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### 证书

#### 描述

证书是一个容器，用于存储在I2P网络中使用的各种收据或工作证明。

#### 目录

1 字节 [Integer](#integer) 指定证书类型，后跟 2 字节 [Integer](#integer) 指定证书载荷的大小，然后是相应数量的字节。

```
+----+----+----+----+----+-/
|type| length  | payload
+----+----+----+----+----+-/

type :: `Integer`
        length -> 1 byte

        case 0 -> NULL
        case 1 -> HASHCASH
        case 2 -> HIDDEN
        case 3 -> SIGNED
        case 4 -> MULTIPLE
        case 5 -> KEY

length :: `Integer`
          length -> 2 bytes

payload :: data
           length -> $length bytes
```
#### 注释

* 对于 [Router Identities](#routeridentity)，在 0.9.15 版本及之前，Certificate 始终为 NULL。从 0.9.16 版本开始，使用 Key Certificate 来指定密钥类型。从 0.9.48 版本开始，允许使用 X25519 加密公钥类型。详见下文。

* 对于 [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove)，证书始终为 NULL，目前没有实现其他类型。

* 对于 [Garlic Messages](/docs/specs/i2np/#msg-garlic)，Certificate 总是 NULL，目前没有实现其他类型。

* 对于 [Destinations](#destination)，证书可以为非空。从 0.9.12 版本开始，可以使用密钥证书来指定签名公钥类型。详见下文。

* 提醒实现者要禁止证书中的多余数据。
  应该强制执行每种证书类型的适当长度。

#### 证书类型

定义了以下证书类型：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HashCash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains an ASCII colon-separated hashcash string.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Hidden</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Hidden routers generally do not announce that they are hidden.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signed</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40 or 72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">43 or 75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains a 40-byte DSA signature, optionally followed by the 32-byte Hash of the signing Destination.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Multiple</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains multiple certificates.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Since 0.9.12. See below for details.</td>
    </tr>
  </tbody>
</table>
#### 密钥证书

密钥证书在0.9.12版本中引入。在该版本之前，所有PublicKeys都是256字节的ElGamal密钥，所有SigningPublicKeys都是128字节的DSA-SHA1密钥。密钥证书提供了一种机制，用于指示Destination或RouterIdentity中PublicKey和SigningPublicKey的类型，并打包任何超出标准长度的密钥数据。

通过在证书之前准确保持384字节，并将任何多余的密钥数据放入证书内部，我们为任何解析Destinations和Router Identities的软件维持了兼容性。

密钥证书载荷包含：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signing Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Crypto Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Signing Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Crypto Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
  </tbody>
</table>
警告：密钥类型顺序与您可能期望的相反；签名公钥类型在前。

已定义的签名公钥类型包括：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only; never used for Router Identities</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">13</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">14</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
已定义的加密公钥类型包括：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies/">ECIES</a> and proposal 156</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (NONE)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">255</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
当不存在密钥证书时，Destination 或 RouterIdentity 中前面的 384 字节定义为 256 字节的 ElGamal PublicKey，后跟 128 字节的 DSA-SHA1 SigningPublicKey。当存在密钥证书时，前面的 384 字节重新定义如下：

* 加密公钥的完整或首部分

* 如果两个密钥的总长度小于 384 字节，则添加随机填充

* 完整或首部分的签名公钥

Crypto Public Key 在开头对齐，Signing Public Key 在末尾对齐。填充数据（如果有的话）位于中间。证书中初始密钥数据、填充数据和多余密钥数据部分的长度和边界没有明确指定，而是从指定密钥类型的长度推导出来的。如果 Crypto 和 Signing Public Keys 的总长度超过 384 字节，剩余部分将包含在 Key Certificate 中。如果 Crypto Public Key 长度不是 256 字节，确定两个密钥之间边界的方法将在本文档的未来修订版中指定。

使用 ElGamal 加密公钥和指定签名公钥类型的示例布局：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Signing Key Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Excess Signing Key Data in Cert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Certificate.html

#### 注释

* 提醒实现者禁止在密钥证书中包含多余数据。
  应当强制执行每种证书类型的适当长度。

* 允许但不建议使用类型为 0,0 (ElGamal,DSA_SHA1) 的 KEY 证书。
  它没有经过充分测试，可能在某些实现中造成问题。
  在 (ElGamal,DSA_SHA1) Destination 或 RouterIdentity 的规范表示中使用 NULL 证书，
  这比使用 KEY 证书要短 4 个字节。

### 映射

#### 描述

一组键/值映射或属性

#### 目录

一个2字节大小的整数，后跟一系列String=String;对。

警告：Mapping的大多数用途都在签名结构中，其中Mapping条目必须按键排序，以确保签名不可变。如果未按键排序，将导致签名失败！

```
+----+----+----+----+----+----+----+----+
|  size   | key_string (len + data)| =  |
+----+----+----+----+----+----+----+----+
| val_string (len + data)     | ;  | ...
+----+----+----+----+----+----+----+
size :: `Integer`
        length -> 2 bytes
        Total number of bytes that follow

key_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

= :: A single byte containing '='

val_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

; :: A single byte containing ';'
```
#### 注意事项

* 编码不是最优的 - 我们要么需要 '=' 和 ';' 字符，要么需要字符串长度，但不需要两者都有

* 一些文档说字符串可能不包含 '=' 或 ';'，但这种编码支持它们

* 字符串被定义为UTF-8编码，但在当前实现中，I2CP使用UTF-8而I2NP不使用。例如，I2NP Database Store Message中RouterInfo选项映射中的UTF-8字符串会被损坏。

* 该编码允许重复键，但是在映射被签名的任何使用场景中，重复键可能会导致签名失败。

* 包含在I2NP消息中的映射（例如在RouterAddress或RouterInfo中）必须按键排序，以确保签名的不变性。不允许重复键。

* 包含在 [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig) 中的映射必须按键排序，以使签名保持不变。不允许重复键。

* 排序方法定义与 Java String.compareTo() 相同，使用字符的 Unicode 值。

* 虽然这取决于具体的应用程序，但键和值通常是大小写敏感的。

* 键和值字符串长度限制分别为255字节（不是字符），加上长度字节。长度字节可以为0。

* 总长度限制为 65535 字节，加上 2 字节的大小字段，总计 65537 字节。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## 通用结构规范

### KeysAndCert

#### 描述

一个加密公钥、一个签名公钥和一个证书，用作 RouterIdentity 或 Destination。

#### 目录

一个 [PublicKey](#publickey) 后跟一个 [SigningPublicKey](#signingpublickey)，然后是一个 [Certificate](#certificate)。

```
+----+----+----+----+----+----+----+----+
| public_key                            |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| padding (optional)                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| certificate                           |
+----+----+----+-/

public_key :: `PublicKey` (partial or full)
              length -> 256 bytes or as specified in key certificate

padding :: random data
           length -> 0 bytes or as specified in key certificate
           public_key length + padding length + signing_key length == 384 bytes

signing__key :: `SigningPublicKey` (partial or full)
                length -> 128 bytes or as specified in key certificate

certificate :: `Certificate`
               length -> >= 3 bytes

total length: 387+ bytes
```
#### 填充生成指南

这些指导原则在提案161中提出，并在API版本0.9.57中实现。这些指导原则与0.6版本（2005年）以来的所有版本向后兼容。有关背景和更多信息，请参见提案161。

对于当前使用的除 ElGamal + DSA-SHA1 之外的任何密钥类型组合，都会存在填充。此外，对于目标地址，256 字节的公钥字段自 0.6 版本（2005年）以来就未被使用。

实现者应该为目标公钥以及目标和 router Identity 填充生成随机数据，使其在各种 I2P 协议中可压缩，同时仍然保持安全性，并且不会让 Base 64 表示看起来损坏或不安全。这提供了移除填充字段的大部分好处，而无需进行任何破坏性的协议更改。

严格来说，仅32字节的签名公钥（在目标地址和router身份中）和32字节的加密公钥（仅在router身份中）就是一个随机数，它提供了所有必要的熵值，使这些结构的SHA-256哈希在netDb DHT中具有密码学强度和随机分布。

不过，出于谨慎考虑，我们建议在 ElG 公钥字段和填充中至少使用 32 字节的随机数据。此外，如果字段全为零，Base 64 目标地址将包含长串的 AAAA 字符，这可能会引起用户的警觉或困惑。

根据需要重复这32字节的随机数据，使完整的KeysAndCert结构在I2P协议中具有高度可压缩性，例如在I2NP Database Store Message、Streaming SYN、SSU2握手和可回复数据报中。

示例：

* 使用 X25519 加密类型和 Ed25519 签名类型的 Router Identity 将包含 10 份随机数据副本（320 字节），压缩后可节省大约 288 字节。

* 使用 Ed25519 签名类型的 Destination 将包含 11 份随机数据副本（352 字节），压缩后可节省大约 320 字节。

当然，实现必须存储完整的 387+ 字节结构，因为结构的 SHA-256 哈希值涵盖了完整的内容。

#### 注意事项

* 不要假设这些总是387字节！它们是387字节加上在第385-386字节指定的证书长度，这个长度可能不为零。

* 从 0.9.12 版本开始，如果证书是 Key Certificate，密钥字段的边界可能会有所不同。详情请参见上面的 Key Certificate 部分。

* 加密公钥在开头对齐，签名公钥在末尾对齐。填充（如果有的话）在中间。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### 描述

定义了唯一识别特定 router 的方法

#### 目录

与 KeysAndCert 相同。

有关为填充字段生成随机数据的指导原则，请参阅 [KeysAndCert](#keysandcert)。

#### 注意事项

* RouterIdentity的证书在0.9.12版本之前始终为NULL。

* 不要假设这些总是 387 字节！它们是 387 字节加上在字节 385-386 处指定的证书长度，该长度可能不为零。

* 从版本 0.9.12 开始，如果证书是 Key Certificate，密钥字段的边界可能会变化。详细信息请参见上面的 Key Certificate 部分。

* 加密公钥在开头对齐，签名公钥在末尾对齐。填充（如果有的话）在中间。

* 带有密钥证书和 ECIES_X25519 公钥的 RouterIdentity 从 0.9.48 版本开始支持。
  在此之前，所有的 RouterIdentity 都是 ElGamal。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### 目标地址

#### 描述

Destination定义了一个特定的端点，消息可以被定向到该端点以进行安全传输。

#### 目录

与 [KeysAndCert](#keysandcert) 相同，除了公钥从未被使用，并且可能包含随机数据而不是有效的 ElGamal 公钥。

有关为公钥和填充字段生成随机数据的指导原则，请参阅 [KeysAndCert](#keysandcert)。

#### 注释

* 目的地的公钥曾用于旧的 i2cp-to-i2cp 加密，该功能在 0.6 版本（2005年）中被禁用，目前除了用作 LeaseSet 加密的 IV（已弃用）外未被使用。现在使用 LeaseSet 中的公钥。

* 不要假设这些总是387字节！它们是387字节加上在第385-386字节处指定的证书长度，该长度可能不为零。

* 从版本 0.9.12 开始，如果证书是密钥证书，密钥字段的边界可能会有所变化。详情请参见上面的密钥证书部分。

* Crypto Public Key 对齐在开始位置，Signing Public Key 对齐在结束位置。填充（如果有的话）在中间。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### 描述

定义特定 tunnel 接收目标为某个 [Destination](#destination) 的消息的授权。

#### 目录

网关 router 的 [RouterIdentity](#routeridentity) 的 SHA256 [Hash](#hash)，然后是 [TunnelId](#tunnelid)，最后是结束 [Date](#date)。

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date
+----+----+----+----+----+----+----+----+
                    |
+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: `Date`
            length -> 8 bytes
```
#### 注意事项

* 总大小：44 字节

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### 描述

包含特定[目标](#destination)的所有当前授权[租约](#lease)、可用于加密garlic消息的[公钥](#publickey)，以及可用于撤销此结构特定版本的[签名公钥](#signingpublickey)。LeaseSet是存储在网络数据库中的两种结构之一（另一种是[路由器信息](#routerinfo)），并以所包含[目标](#destination)的SHA256值作为键值。

#### 目录

[Destination](#destination)，然后是用于加密的 [PublicKey](#publickey)，接着是可用于撤销此版本 LeaseSet 的 [SigningPublicKey](#signingpublickey)，然后是1字节的 [Integer](#integer) 指定集合中 [Lease](#lease) 结构的数量，接着是实际的 [Lease](#lease) 结构，最后是由 [Destination](#destination) 的 [SigningPrivateKey](#signingprivatekey) 对前述字节进行签名的 [Signature](#signature)。

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| encryption_key                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease 0                          |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease 1                               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease ($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

encryption_key :: `PublicKey`
                  length -> 256 bytes

signing_key :: `SigningPublicKey`
               length -> 128 bytes or as specified in destination's key
                         certificate

num :: `Integer`
       length -> 1 byte
       Number of leases to follow
       value: 0 <= num <= 16

leases :: [`Lease`]
          length -> $num*44 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate
```
#### 注意事项

* 目标的公钥曾用于旧的 I2CP-to-I2CP 加密，该功能在 0.6 版本中被禁用，目前未使用。

* 加密密钥用于端到端的 ElGamal/AES+SessionTag 加密
  [ELGAMAL-AES](/docs/specs/elgamal-aes/)。它目前在每次 router 启动时重新生成，不是持久化的。

* 可以使用目标地址的签名公钥来验证签名。

* 允许使用零 Lease 的 LeaseSet，但不会被使用。
  这原本是为 LeaseSet 撤销功能设计的，但该功能尚未实现。
  所有 LeaseSet2 变体都需要至少一个 Lease。

* signing_key 目前未使用。它原本用于 LeaseSet 撤销功能，但该功能尚未实现。它目前在每次 router 启动时重新生成，不会持久保存。signing key 类型始终与目标的 signing key 类型相同。

* 所有 Lease 中最早的过期时间被视为 LeaseSet 的时间戳或版本。除非新的 LeaseSet 比当前的"更新"，否则 router 通常不会接受 LeaseSet 的存储。当发布新的 LeaseSet 时，如果其中最旧的 Lease 与之前 LeaseSet 中最旧的 Lease 相同，需要特别注意。在这种情况下，发布的 router 通常应该将最旧 Lease 的过期时间至少增加 1 毫秒。

* 在 0.9.7 版本之前，当包含在由发起 router 发送的 DatabaseStore 消息中时，router 会将所有已发布 lease 的过期时间设置为相同值，即最早 lease 的过期时间。从 0.9.7 版本开始，router 会发布每个 lease 的实际过期时间。这是一个实现细节，不属于结构规范的一部分。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### 描述

定义特定 tunnel 接收针对[目标](#destination)消息的授权。与 [Lease](#lease) 相同，但使用 4 字节的 end_date。由 [LeaseSet2](#leaseset2) 使用。从 0.9.38 版本开始支持；更多信息请参见提案 123。

#### 目录

网关 router 的 [RouterIdentity](#routeridentity) 的 SHA256 [Hash](#hash)，然后是 [TunnelId](#tunnelid)，最后是 4 字节的结束日期。

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### 注释

* 总大小：40 字节

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### 描述

这是 [LeaseSet2Header](#leaseset2header) 的可选部分。也用于流传输和 I2CP。从 0.9.38 版本开始支持；更多信息请参见提案 123。

#### 目录

包含一个过期时间、签名类型和临时的 [SigningPublicKey](#signingpublickey)，以及一个 [Signature](#signature)。

```
+----+----+----+----+----+----+----+----+
|     expires       | sigtype |         |
+----+----+----+----+----+----+         +
|       transient_public_key            |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|           signature                   |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

expires :: 4 byte date
           length -> 4 bytes
           Seconds since the epoch, rolls over in 2106.

sigtype :: 2 byte type of the transient_public_key
           length -> 2 bytes

transient_public_key :: `SigningPublicKey`
                        length -> As inferred from the sigtype

signature :: `Signature`
             length -> As inferred from the sigtype of the signing public key
                       in the `Destination` that preceded this offline signature.
             Signature of expires timestamp, transient sig type, and public key,
             by the destination public key.

```
#### 注释

* 本节可以且应该离线生成。

### LeaseSet2Header

#### 描述

这是[LeaseSet2](#leaseset2)和[MetaLeaseSet](#metaleaseset)的公共部分。从0.9.38版本开始支持；更多信息请参阅提案123。

#### 目录

包含 [Destination](#destination)、两个时间戳和一个可选的 [OfflineSignature](#offlinesignature)。

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one, unless bit 2 is set.
  Bit 2: If 0, a standard published leaseset.
         If 1, this unencrypted leaseset will be blinded and encrypted when published.
         If this leaseset expires, query the blinded location in the netdb for a new one.
         If this bit is set to 1, set bit 1 to 1 also.
         As of release 0.9.42.
  Bits 15-3: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

```
#### 注释

* 总大小：最小 395 字节

* 实际最大过期时间约为 660（11 分钟）对于 [LeaseSet2](#leaseset2)，65535（完整的 18.2 小时）对于 [MetaLeaseSet](#metaleaseset)。

* [LeaseSet](#leaseset) (1) 没有 'published' 字段，所以版本控制需要
  搜索最早的 lease。LeaseSet2 添加了一个 'published' 字段，
  分辨率为一秒。Router 应该限制向 floodfill 发送
  新 leaseSet 的速率，使其远低于每秒一次（每个目标）。
  如果没有实现这一点，那么代码必须确保每个新 leaseSet
  的 'published' 时间比前一个至少晚一秒，否则
  floodfill 将不会存储或传播新的 leaseSet。

### LeaseSet2

#### 描述

包含在类型为 3 的 I2NP DatabaseStore 消息中。从 0.9.38 版本开始支持；更多信息请参见提案 123。

包含特定 [Destination](#destination) 当前所有授权的 [Lease2](#lease2)，以及可用于 garlic 消息加密的 [PublicKey](#publickey)。LeaseSet 是存储在网络数据库中的两种结构之一（另一种是 [RouterInfo](#routerinfo)），以所包含 [Destination](#destination) 的 SHA256 值作为键。

#### 目录

[LeaseSet2Header](#leaseset2header)，后跟选项，然后是一个或多个用于加密的 [PublicKey](#publickey)，[Integer](#integer) 指定集合中有多少个 [Lease2](#lease2) 结构，接着是实际的 [Lease2](#lease2) 结构，最后是由 [Destination](#destination) 的 [SigningPrivateKey](#signingprivatekey) 或临时密钥签名的前述字节的 [Signature](#signature)。

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numk| keytype0| keylen0 |              |
+----+----+----+----+----+              +
|          encryption_key_0             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| keytypen| keylenn |                   |
+----+----+----+----+                   +
|          encryption_key_n             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease2 0                         |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease2($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

numk :: `Integer`
        length -> 1 byte
        Number of key types, key lengths, and `PublicKey`s to follow
        value: 1 <= numk <= max TBD

keytype :: The encryption type of the `PublicKey` to follow.
           length -> 2 bytes

keylen :: The length of the `PublicKey` to follow.
          Must match the specified length of the encryption type.
          length -> 2 bytes

encryption_key :: `PublicKey`
                  length -> keylen bytes

num :: `Integer`
       length -> 1 byte
       Number of `Lease2`s to follow
       value: 0 <= num <= 16

leases :: [`Lease2`]
          length -> $num*40 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### 加密密钥偏好设置

对于已发布的（服务器）leaseSet，加密密钥按服务器偏好顺序排列，最偏好的排在前面。如果客户端支持多种加密类型，建议它们遵循服务器偏好，选择第一个支持的类型作为连接服务器的加密方法。通常，较新的（编号更高的）密钥类型更安全或更高效，因此更受偏好，所以密钥应该按密钥类型的逆序排列。

然而，客户端可能会根据实现情况，基于自己的偏好进行选择，或使用某种方法来确定"组合"偏好。这可能作为配置选项或用于调试很有用。

未发布的（客户端）leaseSet 中的密钥顺序实际上并不重要，因为通常不会尝试连接到未发布的客户端。除非这个顺序用于确定组合偏好，如上所述。

#### 选项

自 API 0.9.66 起，定义了服务记录选项的标准格式。详细信息请参见提案 167。将来可能会定义使用不同格式的非服务记录选项。

LS2 选项必须按键排序，这样签名就是不变的。

服务记录选项定义如下：

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := 所需服务的符号名称。必须为小写。示例："smtp"。
  允许的字符为 [a-z0-9-]，且不能以 '-' 开头或结尾。
  如果在 [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) 或 Linux /etc/services 中有定义，必须使用其中的标准标识符。
- proto := 所需服务的传输协议。必须为小写，要么是 "tcp" 要么是 "udp"。
  "tcp" 表示流式传输，"udp" 表示可回复数据报。
  原始数据报和 datagram2 的协议指示符可能会在稍后定义。
  允许的字符为 [a-z0-9-]，且不能以 '-' 开头或结尾。
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := 生存时间，以秒为单位的整数。正整数。示例："86400"。
  建议最小值为 86400（一天），详情请参见下面的建议部分。
- priority := 目标主机的优先级，数值越低表示越优先。非负整数。示例："0"
  仅在有多个记录时有用，但即使只有一个记录也是必需的。
- weight := 同优先级记录的相对权重。数值越高表示被选中的机会越大。非负整数。示例："0"
  仅在有多个记录时有用，但即使只有一个记录也是必需的。
- port := 提供服务的 I2CP 端口。非负整数。示例："25"
  支持端口 0，但不推荐使用。
- target := 提供服务的目标主机名或 b32。如 [NAMING](/docs/overview/naming/) 中所述的有效主机名。必须为小写。
  示例："aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" 或 "example.i2p"。
  建议使用 b32，除非主机名是"众所周知的"，即在官方或默认地址簿中。
- appoptions := 应用程序特定的任意文本，不能包含 " " 或 ","。编码为 UTF-8。

示例：

在 LS2 中，对于 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p，指向一个 SMTP 服务器：

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

在 LS2 中，对于 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p，指向两个 SMTP 服务器：

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

在 LS2 中，对于 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p，指向自身作为 SMTP 服务器：

"_smtp._tcp" "0 999999 25"

#### 注释

* 目标的公钥曾用于旧的 I2CP-to-I2CP 加密，该功能在 0.6 版本中被禁用，目前未使用。

* 加密密钥用于端到端的 ElGamal/AES+SessionTag 加密
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (类型 0) 或其他端到端加密方案。
  参见 [ECIES](/docs/specs/ecies/) 和提案 145 和 156。
  这些密钥可能在每次 router 启动时重新生成，
  也可能是持久的。
  X25519 (类型 4，参见 [ECIES](/docs/specs/ecies/)) 从 0.9.44 版本开始支持。

* 签名覆盖上述数据，并在前面加上包含 DatabaseStore 类型 (3) 的单个字节。

* 签名可以使用目的地的签名公钥进行验证，如果 leaseset2 头部包含离线签名，也可以使用临时签名公钥进行验证。

* 每个密钥都提供了密钥长度，这样 floodfill 和客户端即使不知道或不支持所有加密类型，也可以解析该结构。

* 请参阅 [LeaseSet2Header](#leaseset2header) 中关于 'published' 字段的说明

* 如果选项映射的大小大于一，则必须按键排序，以便签名保持不变。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### 描述

定义特定 tunnel 接收目标为某个 [Destination](#destination) 的消息的授权。与 [Lease2](#lease2) 相同，但使用标志和成本而不是 tunnel id。由 [MetaLeaseSet](#metaleaseset) 使用。包含在类型为 7 的 I2NP DatabaseStore 消息中。从 0.9.38 版本开始支持；更多信息请参见提案 123。

#### 目录

网关 router 的 [RouterIdentity](#routeridentity) 的 SHA256 [Hash](#hash)，然后是标志和成本，最后是 4 字节的结束日期。

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|    flags     |cost|      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway,
             or the hash of another `MetaLeaseSet`.
             length -> 32 bytes

flags :: 3 bytes of flags
         Bit order: 23 22 ... 3 2 1 0
         Bits 3-0: Type of the entry.
         If 0, unknown.
         If 1, a `LeaseSet`.
         If 3, a `LeaseSet2`.
         If 5, a `MetaLeaseSet`.
         Bits 23-4: set to 0 for compatibility with future uses
         length -> 3 bytes

cost :: 1 byte, 0-255. Lower value is higher priority.
        length -> 1 byte

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### 注意事项

* 总大小：40 字节

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### 描述

包含在类型为 7 的 I2NP DatabaseStore 消息中。自 0.9.38 版本定义；计划在 0.9.40 版本开始工作；更多信息请参见提案 123。

包含特定 [Destination](#destination) 当前所有已授权的 [MetaLease](#metalease)，以及可用于加密 garlic 消息的 [PublicKey](#publickey)。LeaseSet 是存储在网络数据库中的两种结构之一（另一种是 [RouterInfo](#routerinfo)），并以所含 [Destination](#destination) 的 SHA256 值作为键。

#### 目录

[LeaseSet2Header](#leaseset2header)，后面跟着选项，[Integer](#integer) 指定集合中有多少个 [Lease2](#lease2) 结构，然后是实际的 [Lease2](#lease2) 结构，最后是由 [Destination](#destination) 的 [SigningPrivateKey](#signingprivatekey) 或临时密钥对前面字节进行签名的 [Signature](#signature)。

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| MetaLease 0                      |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| MetaLease($num-1)                     |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numr|                                  |
+----+                                  +
|          revocation_0                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          revocation_n                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

num :: `Integer`
        length -> 1 byte
        Number of `MetaLease`s to follow
        value: 1 <= num <= max TBD

leases :: `MetaLease`s
          length -> $numr*40 bytes

numr :: `Integer`
        length -> 1 byte
        Number of `Hash`es to follow
        value: 0 <= numr <= max TBD

revocations :: [`Hash`]
               length -> $numr*32 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### 注释

* 目标的公钥用于旧的I2CP到I2CP加密，该功能在0.6版本中被禁用，目前未使用。

* 签名覆盖上述数据，并在前面加上包含 DatabaseStore 类型 (7) 的单个字节。

* 签名可以使用目标地址的签名公钥进行验证，或者如果 leaseset2 头部包含离线签名，则使用临时签名公钥进行验证。

* 请参阅 [LeaseSet2Header](#leaseset2header) 中关于 'published' 字段的说明

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### 描述

包含在类型为 5 的 I2NP DatabaseStore 消息中。自 0.9.38 版本定义；自 0.9.39 版本开始工作；更多信息请参见提案 123。

只有盲化密钥和过期时间以明文形式可见。实际的 leaseSet 是加密的。

#### 目录

一个两字节的签名类型、盲化的[SigningPrivateKey](#signingprivatekey)、发布时间、过期时间和标志位。然后是两字节长度后跟加密数据。最后是由盲化的[SigningPrivateKey](#signingprivatekey)或临时密钥对前述字节进行签名的[Signature](#signature)。

```
+----+----+----+----+----+----+----+----+
| sigtype |                             |
+----+----+                             +
|        blinded_public_key             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  len    |                             |
+----+----+                             +
|         encrypted_data                |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

sigtype :: A two byte signature type of the public key to follow
           length -> 2 bytes

blinded_public_key :: `SigningPublicKey`
                      length -> As inferred from the sigtype

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one.
  Bits 15-2: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

len :: `Integer`
        length -> 2 bytes
        length of encrypted_data to follow
        value: 1 <= num <= max TBD

encrypted_data :: Data encrypted
                  length -> len bytes

signature :: `Signature`
             length -> As specified by the sigtype of the blinded pubic key,
                       or by the sigtype of the transient public key,
                       if present in the header

```
#### 注释

* 目标地址的公钥曾用于旧的 I2CP-to-I2CP 加密，该功能在 0.6 版本中被禁用，目前未使用。

* 签名是针对上述数据，并在前面添加包含 DatabaseStore 类型 (5) 的单字节。

* 签名可以使用目标的签名公钥进行验证，或者如果 leaseset2 头部包含离线签名，则使用临时签名公钥进行验证。

* 混淆和加密在 [EncryptedLeaseSet](/docs/specs/encryptedleaseset/) 中有详细说明

* 此结构不使用 [LeaseSet2Header](#leaseset2header)。

* 最大实际过期时间约为 660（11 分钟），除非它是加密的 [MetaLeaseSet](#metaleaseset)。

* 参见提案123，了解在加密leaseSet中使用离线签名的说明。

* 查看 [LeaseSet2Header](#leaseset2header) 中 'published' 字段的说明
  （同样的问题，即使我们在这里没有使用 LeaseSet2Header 格式）

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### 描述

此结构定义了通过传输协议联系 router 的方式。

#### 目录

1字节的[整数](#integer)定义了使用该地址的相对成本，其中0表示免费，255表示昂贵，后跟过期[日期](#date)，超过该日期后地址不应被使用，如果为空，则地址永不过期。之后是定义该router地址使用的传输协议的[字符串](#string)。最后是包含建立连接所需的所有传输特定选项的[映射](#mapping)，如IP地址、端口号、电子邮件地址、URL等。

```
+----+----+----+----+----+----+----+----+
|cost|           expiration
+----+----+----+----+----+----+----+----+
     |        transport_style           |
+----+----+----+----+-/-+----+----+----+
|                                       |
+                                       +
|               options                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

cost :: `Integer`
        length -> 1 byte

        case 0 -> free
        case 255 -> expensive

expiration :: `Date` (must be all zeros, see notes below)
              length -> 8 bytes

              case null -> never expires

transport_style :: `String`
                   length -> 1-256 bytes

options :: `Mapping`
```
#### 注释

* 成本通常为 SSU 的 5 或 6，NTCP 的 10 或 11。

* 过期时间目前未使用，始终为 null（全零）。从 0.9.3 版本开始，过期时间被假定为零且不会存储，因此任何非零过期时间都会导致 RouterInfo 签名验证失败。实现过期时间（或这些字节的其他用途）将是一个向后不兼容的更改。Router 必须将此字段设置为全零。从 0.9.12 版本开始，非零过期时间字段再次被识别，但是我们必须等待几个版本才能使用此字段，直到网络中的绝大多数节点都能识别它。

* 以下选项虽然不是必需的，但是标准选项，预期在大多数 router 地址中都会出现："host"（IPv4 或 IPv6 地址或主机名）和 "port"。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### 描述

定义了router想要发布给网络查看的所有数据。[RouterInfo](#routerinfo)是存储在netDb中的两种结构之一（另一种是[LeaseSet](#leaseset)），并以所包含的[RouterIdentity](#routeridentity)的SHA256值作为键。

#### 目录

[RouterIdentity](#routeridentity) 后跟 [Date](#date)，表示条目发布的时间

```
+----+----+----+----+----+----+----+----+
| router_ident                          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| published                             |
+----+----+----+----+----+----+----+----+
|size| RouterAddress 0                  |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress 1                       |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress ($size-1)               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+-/-+----+----+----+
|psiz| options                          |
+----+----+----+----+-/-+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

router_ident :: `RouterIdentity`
                length -> >= 387+ bytes

published :: `Date`
             length -> 8 bytes

size :: `Integer`
        length -> 1 byte
        The number of `RouterAddress`es to follow, 0-255

addresses :: [`RouterAddress`]
             length -> varies

peer_size :: `Integer`
             length -> 1 byte
             The number of peer `Hash`es to follow, 0-255, unused, always zero
             value -> 0

options :: `Mapping`

signature :: `Signature`
             length -> 40 bytes or as specified in router_ident's key
                       certificate
```
#### 注意事项

* peer_size [Integer](#integer) 后面可能跟着一个包含相应数量 router 哈希的列表。
  这个功能目前未使用。它原本是为一种受限路由形式设计的，
  但该功能尚未实现。
  某些实现可能要求该列表经过排序，以确保签名的不变性。
  在启用此功能之前需要进一步研究。

* 可以使用 router_ident 的签名公钥来验证签名。

* 查看网络数据库页面 [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) 了解所有 router 信息中应包含的标准选项。

* 非常老的 router 要求地址按其数据的 SHA256 排序，以使签名保持不变。这不再是必需的，为了向后兼容而实现它也不值得。

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### 交付说明

Tunnel 消息传递指令在 Tunnel 消息规范 [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions) 中定义。

Garlic Message Delivery Instructions 在 I2NP Message Specification [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions) 中定义。

## 参考文献

- [ECIES](/docs/specs/ecies/)
- [ECIES-HYBRID](/docs/specs/ecies-hybrid/)
- [ECIES-ROUTERS](/docs/specs/ecies-routers/)
- [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy)
- [ELGAMAL-AES](/docs/specs/elgamal-aes/)
- [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions)
- [I2CP](/docs/specs/i2cp/)
- [I2NP](/docs/specs/i2np/)
- [NAMING](/docs/overview/naming/)
- [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo)
- [Prop134](/proposals/134-gost/)
- [Prop169](/proposals/169-pq-crypto/)
- [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
- [SSU](/docs/legacy/ssu/)
- [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions)

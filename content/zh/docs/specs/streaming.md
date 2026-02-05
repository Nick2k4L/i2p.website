---
title: "流协议规范"
description: "I2P streaming 协议规范，提供类似 TCP 的可靠传输"
slug: "streaming"
category: "协议"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## 概述

有关 Streaming 协议的概述，请参阅 [Streaming Library](/docs/api/streaming)。

## 协议版本

streaming 协议不包含版本字段。下面列出的版本适用于 Java I2P。实现和实际的加密支持可能有所不同。无法确定远端是否支持任何特定版本或功能。下表仅供参考，用于了解各种功能的发布日期。

下面列出的功能是针对协议本身的。各种配置选项在[Streaming Library](/docs/api/streaming)中有文档说明，同时也标明了它们在哪个Java I2P版本中实现。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## 协议规范

### 数据包格式

流协议中单个数据包的格式如下所示。最小头部大小为22字节，不包括NACK或选项数据。

流协议中没有长度字段。帧结构由底层协议提供 - I2CP 和 I2NP。

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 字节 [Integer](/docs/specs/common-structures#integer) : 由数据包接收方在发送第一个 SYN 回复数据包之前选择的随机数，在连接的生命周期内保持不变，大于零。在连接发起方发送的 SYN 消息中为 0，在后续消息中也为 0，直到收到包含对方 stream ID 的 SYN 回复。

**receiveStreamId** :: 4 字节 [Integer](/docs/specs/common-structures#integer) : 在发送第一个 SYN 数据包之前由数据包发起者选择的随机数，在连接的整个生命周期内保持不变，必须大于零。如果未知则可能为 0，例如在 RESET 数据包中。

**sequenceNum** :: 4 字节 [Integer](/docs/specs/common-structures#integer) : 此消息的序列号，在 SYN 消息中从 0 开始，在每个消息中递增 1，但纯 ACK 和重传消息除外。如果 sequenceNum 为 0 且未设置 SYN 标志，则这是一个不应被 ACK 的纯 ACK 数据包。

**ackThrough** :: 4 字节 [Integer](/docs/specs/common-structures#integer) : 在 receiveStreamId 上接收到的最高数据包序列号。此字段在初始连接数据包（其中 receiveStreamId 为未知 id）或设置了 NO_ACK 标志时被忽略。所有序列号小于等于此值的数据包都被确认（ACK），除了下面 NACKs 中列出的数据包。

**NACK count** :: 1字节 [Integer](/docs/specs/common-structures#integer) : 下一个字段中4字节NACK的数量，或者从0.9.58版本开始与SYNCHRONIZE一起用于重放防护时为8；见下文。

**NACKs** :: nc * 4字节 [Integer](/docs/specs/common-structures#integer)s : 小于ackThrough但尚未接收到的序列号。对一个数据包的两次NACK是对该数据包进行"快速重传"的请求。从0.9.58版本开始，也与SYNCHRONIZE一起用于防止重放攻击；见下文。

**resendDelay** :: 1 字节 [Integer](/docs/specs/common-structures#integer) : 此数据包的创建者在重新发送此数据包之前将等待多长时间（如果尚未收到 ACK）。该值是自数据包创建以来的秒数。目前在接收时被忽略。

**flags** :: 2 字节值：见下文。

**option size** :: 2 字节 [Integer](/docs/specs/common-structures#integer) : 下一个字段中的字节数

**选项数据** :: 0 或更多字节 : 按标志指定。见下文。

**payload** :: 剩余数据包大小

### 标志和选项数据字段

上面的标志字段指定了数据包的一些元数据，并且可能需要包含某些附加数据。标志如下所示。任何指定的数据结构都必须按给定顺序添加到选项区域中。

位序：15....0（15是最高有效位）

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### 可变长度签名说明

在 0.9.11 版本发布之前，选项字段中的签名始终是 40 字节。

从 0.9.11 版本开始，签名长度是可变的。签名类型和长度是从 FROM_INCLUDED 选项中使用的密钥类型和[签名](/docs/specs/common-structures#signature)文档中推断出来的。

从 0.9.39 版本开始，支持 OFFLINE_SIGNATURE 选项。如果存在此选项，则使用临时的 [SigningPublicKey](/docs/specs/common-structures#signingpublickey) 来验证任何已签名的数据包，签名长度和类型从选项中的临时 SigningPublicKey 推断得出。

- 当数据包同时包含 FROM_INCLUDED 和 SIGNATURE_INCLUDED（如在 SYNCHRONIZE 中）时，可以直接进行推断。

- 当数据包不包含 FROM_INCLUDED 时，必须从之前的 SYNCHRONIZE 数据包中进行推断。

- 当数据包不包含 FROM_INCLUDED，且之前没有 SYNCHRONIZE 数据包时（例如游离的 CLOSE 或 RESET 数据包），可以从剩余选项的长度推断出这一点（因为 SIGNATURE_INCLUDED 是最后一个选项），但数据包可能会被丢弃，因为没有可用的 FROM 来验证签名。如果将来定义了更多选项字段，必须将它们考虑在内。

### 重放防护

为了防止 Bob 通过存储从 Alice 收到的有效签名 SYNCHRONIZE 数据包并稍后将其发送给受害者 Charlie 来进行重放攻击，Alice 必须在 SYNCHRONIZE 数据包中包含 Bob 的目标哈希值，如下所示：

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
收到SYNCHRONIZE后，如果NACK count字段为8，Bob必须将NACKs字段解释为32字节的目标哈希，并且必须验证它与他的目标哈希匹配。他还必须像往常一样验证数据包的签名，因为签名覆盖整个数据包，包括NACK count和NACKs字段。如果NACK count为8且NACKs字段不匹配，Bob必须丢弃该数据包。

这是版本 0.9.58 及更高版本所必需的。这与旧版本向后兼容，因为在 SYNCHRONIZE 数据包中不期望出现 NACK。目标节点不知道也无法知道对端正在运行什么版本。

从Bob发送给Alice的SYNCHRONIZE ACK数据包无需更改；不要在该数据包中包含NACK。

## 参考资料

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [流媒体库](/docs/api/streaming)

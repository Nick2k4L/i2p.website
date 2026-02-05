---
title: "Tunnel 创建规范"
description: "使用非交互式伸缩创建tunnel的ElGamal tunnel构建规范。"
slug: "tunnel-creation"
aliases: 
category: "设计"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## 概览

注意：已过时 - 这是 ElGamal tunnel 构建规范。请参阅 [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) 了解 X25519 tunnel 构建规范。

本文档规定了使用"非交互式望远镜"方法创建tunnel时所使用的加密tunnel构建消息的详细信息。请参阅tunnel构建文档[TUNNEL-IMPL](/docs/specs/tunnel-implementation/)了解该过程的概述，包括节点选择和排序方法。

tunnel创建通过沿着tunnel中的节点路径传递的单个消息来完成，该消息在传输过程中被就地重写，并传输回tunnel创建者。这个单一的tunnel消息由可变数量的记录（最多8个）组成——tunnel中的每个潜在节点都有一个记录。单个记录使用非对称加密（ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)）进行加密，只能由路径上的特定节点读取，同时在每一跳都添加额外的对称加密层（AES [CRYPTO-AES](/docs/specs/cryptography/#aes)），以便仅在适当的时间暴露非对称加密的记录。

### 记录数量

并非所有记录都必须包含有效数据。例如，3跳tunnel的构建消息可能包含更多记录来向参与者隐藏tunnel的实际长度。有两种构建消息类型。原始的Tunnel构建消息（[TBM](/docs/specs/i2np/#struct-TunnelBuild)）包含8条记录，这对于任何实际的tunnel长度都足够了。较新的可变Tunnel构建消息（[VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)）包含1到8条记录。发起者可以在消息大小与所需的tunnel长度混淆程度之间进行权衡。

在当前网络中，大多数 tunnel 的长度为 2 或 3 跳。当前实现使用 5 记录的 VTBM 来构建 4 跳或更少的 tunnel，对于更长的 tunnel 则使用 8 记录的 TBM。5 记录的 VTBM（在分片时可以放入三个 1KB 的 tunnel 消息中）减少了网络流量并提高了构建成功率，因为较小的消息不太容易被丢弃。

回复消息必须与构建消息具有相同的类型和长度。

### 请求记录规范

也在 I2NP 规范 [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) 中指定。

记录的明文，仅对被询问的 hop 可见：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
下一个 tunnel ID 和下一个 router 身份哈希字段用于指定 tunnel 中的下一跳，不过对于出站 tunnel 端点，它们指定重写的 tunnel 创建回复消息应该发送到哪里。此外，下一个消息 ID 指定消息（或回复）应该使用的消息 ID。

tunnel 层密钥、tunnel IV 密钥、回复密钥和回复 IV 都是由创建者生成的随机 32 字节值，仅用于此构建请求记录。

flags 字段包含以下内容（位顺序：76543210，第 7 位是 MSB）：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
第7位表示该跳点将作为入站网关（IBGW）。第6位表示该跳点将作为出站端点（OBEP）。如果两个位都没有设置，该跳点将作为中间参与者。两个位不能同时设置。

#### 请求记录创建

每个跳点都会获得一个随机的非零 Tunnel ID。当前和下一跳的 Tunnel ID 都会被填入。每条记录都会获得一个随机的 tunnel IV 密钥、回复 IV、层密钥和回复密钥。

#### 请求记录加密

该明文记录使用跳点的公共加密密钥进行ElGamal 2048加密[CRYPTO-ELG](/docs/specs/cryptography/#elgamal)，并格式化为528字节记录：

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
在512字节加密记录中，ElGamal数据包含514字节ElGamal加密块[CRYPTO-ELG](/docs/specs/cryptography/#elgamal)的第1-256字节和第258-513字节。块中的两个填充字节（位于位置0和257的零字节）被移除。

由于明文使用了完整字段，因此除了 `SHA256(cleartext) + cleartext` 之外不需要额外的填充。

然后，每个528字节的记录都会被迭代加密（使用AES解密，为每个跳点使用reply key和reply IV），这样router身份只会在相关跳点中以明文形式存在。

### 跳点处理与加密

当一个跳点接收到 TunnelBuildMessage 时，它会查看其中包含的记录，寻找以自己的身份哈希（截断为16字节）开头的记录。然后它解密该记录中的 ElGamal 块并获取受保护的明文。此时，它们通过将 AES-256 回复密钥输入到布隆过滤器中来确保tunnel请求不是重复的。重复或无效的请求会被丢弃。没有标记当前小时或前一小时（如果刚过整点不久）时间戳的记录必须被丢弃。例如，取时间戳中的小时，转换为完整时间，然后如果它比当前时间落后超过65分钟或提前超过5分钟，则无效。布隆过滤器必须至少持续一小时（加上几分钟以允许时钟偏差），这样当前小时内未被记录中的小时时间戳检查拒绝的重复记录，将被过滤器拒绝。

在决定是否同意参与tunnel后，它们将包含请求的记录替换为加密的回复块。所有其他记录都使用包含的回复密钥和IV进行AES-256加密[CRYPTO-AES](/docs/specs/cryptography/#aes)。每个记录都使用相同的回复密钥和回复IV单独进行AES/CBC加密。CBC模式不会跨记录继续（链接）。

每个跳点只知道自己的响应。如果它同意，即使不会被使用，它也会维护 tunnel 直到过期，因为它无法知道其他所有跳点是否都同意了。

#### 回复记录规范

当前跳节点读取其记录后，会将其替换为一个回复记录，说明他们是否同意参与tunnel，如果不同意，则会分类说明拒绝的原因。这只是一个1字节的值，0x0表示他们同意参与tunnel，更高的值表示更高级别的拒绝。

定义了以下拒绝代码：

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

为了向对等节点隐藏其他原因（如router关闭），当前实现对几乎所有拒绝都使用TUNNEL_REJECT_BANDWIDTH。

回复使用在加密块中传递给它的AES会话密钥进行加密，并用495字节的随机数据进行填充以达到完整的记录大小。填充放置在状态字节之前：

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
这在 I2NP 规范 [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) 中也有描述。

### Tunnel 构建消息准备

在构建新的 Tunnel Build Message 时，必须首先构建所有的 Build Request Records，并使用 ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) 进行非对称加密。然后使用路径中较早跳点的回复密钥和 IV，通过 AES [CRYPTO-AES](/docs/specs/cryptography/#aes) 对每个记录进行预先解密。该解密应该以相反顺序运行，这样当前驱节点对其进行加密后，非对称加密的数据将在正确的跳点以明文形式显示。

创建者会将个别请求不需要的多余记录简单地用随机数据填充。

### tunnel 构建消息传递

对于出站 tunnel，传递是直接从 tunnel 创建者到第一跳完成的，将 TunnelBuildMessage 打包，就好像创建者只是 tunnel 中的另一跳一样。对于入站 tunnel，传递是通过现有的出站 tunnel 完成的。出站 tunnel 通常来自与正在构建的新 tunnel 相同的池。如果该池中没有可用的出站 tunnel，则使用出站探索性 tunnel。在启动时，当还不存在出站探索性 tunnel 时，使用伪造的 0 跳出站 tunnel。

### Tunnel 构建消息端点处理

对于outbound tunnel的创建，当请求到达outbound端点时（由"允许向任何人发送消息"标志确定），该跳点按常规处理，加密回复以替代记录并加密所有其他记录，但由于没有"下一跳"可以将TunnelBuildMessage转发到，它会将加密的回复记录放入TunnelBuildReplyMessage（[TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)）或VariableTunnelBuildReplyMessage（[VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)）中（消息类型和记录数量必须与请求匹配），并将其传递到请求记录中指定的回复tunnel。该回复tunnel将Tunnel Build Reply Message转发回tunnel创建者，就像处理任何其他消息一样[TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)。然后tunnel创建者处理它，如下所述。

回复tunnel的选择由创建者按以下方式进行：通常它是来自与正在构建的新出站tunnel相同池的入站tunnel。如果该池中没有可用的入站tunnel，则使用入站探索tunnel。在启动时，当尚不存在入站探索tunnel时，会使用一个虚假的0跳入站tunnel。

对于创建入站tunnel，当请求到达入站端点（也称为tunnel创建者）时，无需生成显式的Tunnel Build Reply Message，router会处理每个回复，如下所示。

### tunnel 构建回复消息处理

为了处理回复记录，创建者只需使用 tunnel 中每个节点（在对等节点之后，按相反顺序）的回复密钥和 IV，对每条记录进行单独的 AES 解密。这样就会暴露回复内容，说明它们是否同意参与 tunnel 或拒绝的原因。如果它们都同意，tunnel 就被认为已创建并可以立即使用，但如果有任何节点拒绝，tunnel 就会被丢弃。

协议和拒绝情况会记录在每个对等节点的配置文件 [PEER-SELECTION](/docs/overview/tunnel-routing/) 中，用于未来评估对等节点 tunnel 容量。

## 历史和说明

这种策略源于I2P邮件列表上Michael Rogers、Matthew Toseland (toad)和jrandom之间关于前驱攻击的讨论。参见[TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)，[TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)。它在2006年2月16日的0.6.1.10版本中引入，这是I2P最后一次进行非向后兼容的更改。

注意事项：

- 此设计无法防止tunnel内的两个恶意对等节点标记一个或多个请求或回复记录来检测它们是否在同一个tunnel内，但这样做可以被tunnel创建者在读取回复时检测到，导致tunnel被标记为无效。
- 此设计在非对称加密部分不包含工作量证明，尽管16字节身份哈希可以减半，后半部分替换为最高2^64成本的hashcash函数。
- 仅此设计无法防止tunnel内的两个恶意对等节点使用时间信息来确定它们是否在同一个tunnel中。使用批量和同步的请求传递可能有所帮助（将请求批处理并在（ntp同步的）分钟数发送）。然而，这样做让对等节点可以通过延迟请求并在tunnel后续检测到延迟来"标记"请求，尽管也许丢弃在小窗口内未传递的请求会有效（但这样做需要高度的时钟同步）。或者，也许各个跳点可以在转发请求前注入随机延迟？
- 是否存在标记请求的非致命方法？
- 具有一小时分辨率的时间戳用于重放防护。此约束直到0.9.16版本才被强制执行。

## 未来工作

- 在当前实现中，发起者为自己保留一个空记录。因此，n 条记录的消息只能构建 n-1 跳的 tunnel。这对于入站 tunnel 似乎是必要的（倒数第二跳可以看到下一跳的哈希前缀），但对于出站 tunnel 则不是。这需要进一步研究和验证。如果可以在不损害匿名性的情况下使用剩余记录，我们应该这样做。
- 进一步分析上述说明中描述的可能的标记和时序攻击。
- 仅使用 VTBM；不要选择不支持它的旧节点。
- 构建请求记录没有指定 tunnel 生命周期或过期时间；每个跳点在 10 分钟后使 tunnel 过期，这是一个网络范围的硬编码常量。我们可以使用标志字段中的一位，并从填充中取出 4（或 8）字节来指定生命周期或过期时间。请求者只有在所有参与者都支持此选项时才会指定此选项。

## 参考资料

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - BuildRequestRecord 规范
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - AES 加密
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - ElGamal 加密
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage

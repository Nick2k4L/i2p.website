---
title: "SAM V3"
description: "用于非Java I2P应用程序的简单匿名消息协议"
slug: "samv3"
aliases: 
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM 是一个用于与 I2P 交互的简单客户端协议。SAM 是推荐非 Java 应用程序连接到 I2P 网络的协议，并且被多个 router 实现所支持。Java 应用程序应该直接使用 streaming 或 I2CP API。

SAMv3 是在 I2P 0.7.3 版本（2009年5月）中引入的，是一个稳定且受支持的接口。3.1 版本也很稳定，并支持签名类型选项，强烈推荐使用。较新的 3.x 版本支持高级功能。请注意，i2pd 目前不支持大部分 3.2 和 3.3 版本的功能。

替代方案：[SOCKS](/docs/api/socks)、[Streaming](/docs/api/streaming)、[I2CP](/docs/protocol/i2cp)、[BOB（已弃用）](/docs/api/bob)。已弃用版本：[SAM V1](/docs/api/sam)、[SAM V2](/docs/api/samv2)。

## 已知的 SAM 库

警告：其中一些可能非常陈旧或不再受支持。除非在下文中注明，否则这些工具都没有经过I2P项目的测试、审查或维护。请自行进行研究。

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
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Typescript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/diva-exchange/i2p-sam">github.com/diva-exchange/i2p-sam</a></td>
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
## 快速开始

要实现一个基本的仅TCP、点对点应用程序，客户端必须支持以下命令：

- `HELLO VERSION MIN=3.1 MAX=3.1` - 所有其余命令都需要此命令
- `DEST GENERATE SIGNATURE_TYPE=7` - 用于生成我们的私钥和destination
- `NAMING LOOKUP NAME=...` - 用于将.i2p地址转换为destinations
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - STREAM CONNECT和STREAM ACCEPT需要此命令
- `STREAM CONNECT ID=... DESTINATION=...` - 用于建立出站连接
- `STREAM ACCEPT ID=...` - 用于接受入站连接

## 开发者通用指南

### 应用程序设计

SAM sessions（或在I2P内部称为tunnel pools或tunnel集合）被设计为长期存在的。大多数应用程序只需要一个session，在启动时创建并在退出时关闭。I2P不同于Tor，在Tor中circuits可能会被快速创建和丢弃。在设计你的应用程序使用多个或两个以上的同时session，或快速创建和丢弃它们之前，请仔细考虑并咨询I2P开发人员。大多数威胁模型不需要为每个连接使用唯一的session。

此外，请确保您的应用程序设置（以及向用户提供的关于router设置的指导，或者如果您捆绑了router的默认设置）能够让您的用户为网络贡献的资源超过他们消耗的资源。I2P是一个对等网络，如果一个流行的应用程序使网络陷入永久拥塞状态，网络将无法生存。

### 兼容性和测试

Java I2P 和 i2pd router 实现是独立的，在行为、功能支持和默认设置方面存在细微差异。请使用两种 router 的最新版本测试您的应用程序。

i2pd SAM 默认启用；Java I2P SAM 则不是。请向用户提供如何在 Java I2P 中启用 SAM 的说明（通过 router 控制台中的 /configclients），和/或在初始连接失败时向用户提供良好的错误消息，例如"确保 I2P 正在运行且 SAM 接口已启用"。

Java I2P 和 i2pd router 对 tunnel 数量有不同的默认设置。Java 的默认值是 2，而 i2pd 的默认值是 5。对于大多数低到中等带宽和低到中等连接数的情况，2 或 3 个就足够了。请在 SESSION CREATE 消息中指定 tunnel 数量，以在 Java I2P 和 i2pd router 之间获得一致的性能。请参见下文。

如需更多开发者指导以确保您的应用程序仅使用所需的资源，请参阅[我们的应用程序打包I2P指南](/docs/applications/embedding)。

### 签名和加密类型

I2P支持多种签名和加密类型。为了向后兼容，SAM默认使用旧的和低效的类型，因此所有客户端都应该指定较新的类型。

签名类型在 DEST GENERATE 和 SESSION CREATE（用于临时）命令中指定。所有客户端都应设置 `SIGNATURE_TYPE=7` (Ed25519)。

加密类型在 SESSION CREATE 命令中指定。允许使用多种加密类型。客户端应设置 `i2cp.leaseSetEncType=4`（仅用于 ECIES-X25519）或 `i2cp.leaseSetEncType=4,0`（用于 ECIES-X25519 和 ElGamal，如果需要兼容性）。

## 版本3变更

### 3.0 版本更改

版本 3.0 在 I2P 发布版本 0.7.3 中引入。SAMv2 提供了一种在同一个 I2P destination 上*并行*管理多个套接字的方法，即客户端无需等待一个套接字上的数据成功发送后才能在另一个套接字上发送数据。但所有数据都通过同一个客户端到 SAM 的套接字传输，这对客户端来说管理起来相当复杂。

SAMv3 以不同的方式管理套接字：每个 *I2P socket* 对应一个唯一的客户端到 SAM 套接字，这样处理起来要简单得多。这类似于 [BOB](/docs/api/bob)。

SAMv3 还提供了一个 UDP 端口用于通过 I2P 发送数据报，并且可以将 I2P 数据报转发回客户端的数据报服务器。

### 版本 3.1 更改

版本 3.1 在 Java I2P 0.9.14 版本（2014年7月）中引入。SAMv3.1 是推荐的最低 SAM 实现版本，因为它相比 SAMv3.0 支持更好的签名类型。i2pd 也支持大部分 3.1 版本的功能。

- DEST GENERATE 和 SESSION CREATE 现在支持 SIGNATURE_TYPE 参数。
- HELLO VERSION 中的 MIN 和 MAX 参数现在是可选的。
- HELLO VERSION 中的 MIN 和 MAX 参数现在支持单位数版本，如"3"。
- bridge socket 现在支持 RAW SEND。

### 版本 3.2 变更

版本 3.2 在 Java I2P 发布版 0.9.24（2016年1月）中引入。请注意，i2pd 目前不支持大部分 3.2 功能。

#### I2CP 端口和协议支持

- SESSION CREATE 选项 FROM_PORT 和 TO_PORT
- SESSION CREATE STYLE=RAW 选项 PROTOCOL
- STREAM CONNECT、DATAGRAM SEND 和 RAW SEND 选项 FROM_PORT 和 TO_PORT
- RAW SEND 选项 PROTOCOL
- DATAGRAM RECEIVED、RAW RECEIVED 以及转发或接收的流和可回复的数据报，包括 FROM_PORT 和 TO_PORT
- RAW session 选项 HEADER=true 将使转发的原始数据报前面添加一行，包含 PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- 通过端口 7655 发送的数据报的第一行现在可以以任何 3.x 版本开始
- 通过端口 7655 发送的数据报的第一行可以包含任何 FROM_PORT、TO_PORT、PROTOCOL 选项
- RAW RECEIVED 包括 PROTOCOL=nnn

#### SSL 和身份验证

- 在 HELLO 参数中使用 USER/PASSWORD 进行授权。见[下文](#authorization)。
- 使用 AUTH 命令的可选授权配置。见[下文](#authorization-configuration-sam-32-or-higher-optional-feature)。
- 控制套接字上的可选 SSL/TLS 支持。见[下文](#ssl)。
- STREAM FORWARD 选项 SSL=true

#### 多线程

- 允许在同一会话 ID 上并发挂起 STREAM ACCEPT。

#### 命令行解析和保活机制

- 可选命令 QUIT、STOP 和 EXIT 用于关闭会话和套接字。参见[下方](#quitstopexitinvisible-sam-32-or-higher-optional-features)。
- 命令解析将正确处理 UTF-8
- 命令解析可靠地处理引号内的空白字符
- 反斜杠 '\\' 可以在命令行中转义引号
- 建议服务器将命令映射为大写，以便通过 telnet 进行测试。
- 空选项值如 PROTOCOL 或 PROTOCOL= 可能被允许，取决于实现。
- PING/PONG 用于保活。参见下方。
- 服务器可能对 HELLO 或后续命令实现超时，取决于实现。

### 版本 3.3 更改

版本 3.3 在 Java I2P 0.9.25 版本中引入（2016年3月）。请注意，i2pd 目前不支持大部分 3.3 功能。

- 同一个会话可以同时用于流、数据报和原始数据。传入的数据包和流将根据 I2P 协议和目标端口进行路由。参见[下面的 PRIMARY 部分](#sam-primary-sessions-v33-and-higher)。
- DATAGRAM SEND 和 RAW SEND 现在支持选项 SEND_TAGS、TAG_THRESHOLD、EXPIRES 和 SEND_LEASESET。参见[下面的数据报发送部分](#sending-repliable-or-raw-datagrams)。

## 版本 3 协议

### 简单匿名消息传递 (SAM) 版本 3.3 规范概述

客户端应用程序与 SAM 桥接器通信，SAM 桥接器处理所有的 I2P 功能（使用 [streaming library](/docs/api/streaming) 进行虚拟流传输，或直接使用 [I2CP](/docs/protocol/i2cp) 进行数据报传输）。

默认情况下，客户端到SAM bridge的通信是未加密和未认证的。SAM bridge可能支持SSL/TLS连接；配置和实现细节超出了本规范的范围。从SAM 3.2开始，在初始握手中支持可选的认证用户名/密码参数，bridge可能要求提供这些参数。

I2P 通信可以采用几种不同的形式：

- [虚拟流](/docs/api/streaming)
- [可回复和已认证的数据报](/docs/specs/datagrams#repliable)（带有FROM字段的消息）
- [匿名数据报](/docs/specs/datagrams#raw)（原始匿名消息）
- [Datagram2](/docs/specs/datagrams#datagram2)（新的可回复和已认证格式）
- [Datagram3](/docs/specs/datagrams#datagram3)（新的可回复但未认证格式）

I2P 通信由 I2P session（会话）支持，每个 I2P session 都绑定到一个地址（称为 destination）。一个 I2P session 与上述三种类型之一相关联，不能承载其他类型的通信，除非使用 [PRIMARY sessions](#sam-primary-sessions-v33-and-higher)。

### 编码和转义

所有这些 SAM 消息都在单行中发送，以换行符（\\n）结尾。在 SAM 3.2 之前，只支持 7 位 ASCII 编码。从 SAM 3.2 开始，必须使用 UTF-8 编码。任何 UTF-8 编码的键或值都应该可以正常工作。

本规范中显示的格式仅为了可读性，虽然每个消息中的前两个词必须保持其特定顺序，但 key=value 对的顺序可以改变（例如 "ONE TWO A=B C=D" 或 "ONE TWO C=D A=B" 都是完全有效的构造）。此外，协议是区分大小写的。在下文中，消息示例以 "->" 开头表示客户端发送给 SAM bridge 的消息，以 "<-" 开头表示 SAM bridge 发送给客户端的消息。

基本命令或响应行采用以下格式之一：

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
仅在 SAM 3.2 中，某些新命令支持没有子命令的命令格式。

键值对必须用单个空格分隔。（从 SAM 3.2 开始，允许使用多个空格）如果值包含空格，则必须用双引号括起来，例如 key="long value text"。（在 SAM 3.2 之前，这在某些实现中无法可靠工作）

在 SAM 3.2 之前，没有转义机制。从 SAM 3.2 开始，双引号可以用反斜杠 '\\' 转义，反斜杠可以表示为两个反斜杠 '\\\\'。

### 空值

从 SAM 3.2 开始，空选项值如 KEY、KEY= 或 KEY="" 可能被允许，这取决于具体实现。

### 大小写敏感

协议规范是区分大小写的。建议但不要求服务器将命令映射为大写，以便通过 telnet 进行测试。例如，这样可以让 "hello version" 正常工作。这取决于具体实现。不要将键或值映射为大写，因为这会破坏 [I2CP](/docs/protocol/i2cp) 选项。

### SAM 连接握手

在客户端和网桥就协议版本达成一致之前，不能进行任何 SAM 通信，这是通过客户端发送 HELLO 和网桥发送 HELLO REPLY 来完成的：

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
和

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
从版本3.1（I2P 0.9.14）开始，MIN和MAX参数是可选的。SAM将始终返回在MIN和MAX约束条件下可能的最高版本，或者如果没有给出约束条件则返回当前服务器版本。

如果 SAM bridge 找不到合适的版本，它会回复：

```
<- HELLO REPLY RESULT=NOVERSION
```
如果发生某些错误，例如请求格式错误，它会回复：

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

服务器的控制套接字可以选择性地提供SSL/TLS支持，这取决于服务器和客户端的配置。实现可能还提供其他传输层；这超出了协议定义的范围。

#### 授权

对于授权，客户端在 HELLO 参数中添加 USER="xxx" PASSWORD="yyy"。建议但不强制要求用户名和密码使用双引号。用户名或密码中的双引号必须用反斜杠转义。失败时服务器将回复 I2P_ERROR 和消息。建议在任何需要授权的 SAM 服务器上启用 SSL。

#### 超时设置

服务器可以为 HELLO 或后续命令实现超时机制，这取决于具体实现。客户端应该在连接后立即发送 HELLO 和下一个命令。

如果在收到 HELLO 之前发生超时，网桥会回复：

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
然后断开连接。

如果在接收到 HELLO 之后但在下一个命令之前发生超时，bridge 会回复：

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
然后断开连接。

### I2CP 端口和协议

从 SAM 3.2 开始，SAM 客户端发送方可以指定 [I2CP](/docs/protocol/i2cp) 端口和协议传递给 [I2CP](/docs/protocol/i2cp)，SAM 网桥将把接收到的 [I2CP](/docs/protocol/i2cp) 端口和协议信息传递给 SAM 客户端。

对于 FROM_PORT 和 TO_PORT，有效范围是 0-65535，默认值是 0。

对于PROTOCOL，只能为RAW指定，有效范围是0-255，默认值是18。

对于 SESSION 命令，指定的端口和协议是该会话的默认值。对于单个流或数据报，指定的端口和协议会覆盖会话默认值。对于接收到的流或数据报，指示的端口和协议是从 [I2CP](/docs/protocol/i2cp) 接收到的。

#### 与标准 IP 的重要区别

I2CP 端口用于 I2P 套接字和数据报。它们与连接到 SAM 的本地套接字无关。

- 端口 0 是有效的，具有特殊含义。
- 端口 1-1023 不是特殊端口或特权端口。
- 服务器默认监听端口 0，这意味着"所有端口"。
- 客户端默认发送到端口 0，这意味着"任意端口"。
- 客户端默认从端口 0 发送，这意味着"未指定"。
- 服务器可能有一个服务监听端口 0，同时其他服务监听更高的端口。如果是这样，端口 0 服务是默认服务，当传入的套接字或数据报端口与其他服务不匹配时，将连接到该服务。
- 大多数 I2P 目标只运行一个服务，因此您可以使用默认设置，并忽略 I2CP 端口配置。
- 需要 SAM 3.2 或 3.3 来指定 I2CP 端口。
- 如果您不需要 I2CP 端口，则不需要 SAM 3.2 或 3.3；3.1 就足够了。
- 协议 0 是有效的，意味着"任意协议"。不推荐这样做，并且可能无法工作。
- I2P 套接字通过内部连接 ID 进行跟踪。因此，不要求 dest:port:dest:port:protocol 的五元组是唯一的。例如，两个目标之间可能有多个具有相同端口的套接字。客户端不需要为出站连接选择"空闲端口"。

如果您正在设计一个具有多个子会话的SAM 3.3应用程序，请仔细考虑如何有效地使用端口和协议。有关更多信息，请参阅[I2CP](/docs/protocol/i2cp)规范。

### SAM 会话

SAMv3 会话由客户端打开到 SAM 桥的套接字、执行握手并发送 SESSION CREATE 消息来创建，当套接字断开连接时会话终止。

每个注册的 I2P Destination 都与一个会话 ID（或昵称）唯一关联。会话 ID，包括 PRIMARY 会话的子会话 ID，在 SAM 服务器上必须全局唯一。为了防止与其他客户端可能发生的 ID 冲突，最佳做法是让客户端随机生成 ID。

每个会话都唯一关联着：

- 客户端创建会话的套接字
- 其ID（或昵称）

#### 会话创建请求

会话创建消息只能使用其中一种形式（通过其他形式接收的消息将收到错误消息作为回应）：

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
DESTINATION 指定应该用于发送和接收消息/流的目标地址。$privkey 是 [Destination](/docs/specs/common-structures#type_Destination) 后跟 [Private Key](/docs/specs/common-structures#type_PrivateKey) 再跟 [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)，可选地后跟 [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) 的连接的 base 64 编码，根据签名类型，二进制格式为 663 字节或更多，base 64 格式为 884 字节或更多。二进制格式在私钥文件中指定。有关 [Private Key](/docs/specs/common-structures#type_PrivateKey) 的更多说明，请参见下面的目标密钥生成部分。

如果签名私钥全为零，则接下来是 [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) 部分。离线签名仅支持 STREAM 和 RAW 会话。离线签名不能使用 DESTINATION=TRANSIENT 创建。离线签名部分的格式为：

1. 过期时间戳（4字节，大端序，自纪元以来的秒数，2106年回滚）
2. 临时签名公钥的签名类型（2字节，大端序）
3. 临时签名公钥（长度由临时签名类型指定）
4. 离线密钥对上述三个字段的签名（长度由目标签名类型指定）
5. 临时签名私钥（长度由临时签名类型指定）

如果目标被指定为 TRANSIENT，SAM 桥接器会创建一个新的目标。从版本 3.1（I2P 0.9.14）开始，如果目标是 TRANSIENT，支持一个可选参数 SIGNATURE_TYPE。SIGNATURE_TYPE 值可以是任何受[密钥证书](/docs/specs/common-structures#type_Certificate)支持的名称（例如 ECDSA_SHA256_P256，不区分大小写）或数字（例如 1）。默认值是 DSA_SHA1，这不是您想要的。对于大多数应用程序，请指定 SIGNATURE_TYPE=7。

$nickname 是客户端的选择。不允许有空白字符。

给出的附加选项如果不被SAM桥接解释，则会传递给I2P会话配置（例如outbound.length=0）。

Java I2P 和 i2pd router 对 tunnel 数量有不同的默认值。Java 默认值是 2，i2pd 默认值是 5。对于大多数低到中等带宽和低到中等连接数的情况，2 或 3 就足够了。请在 SESSION CREATE 消息中指定 tunnel 数量，以在 Java I2P 和 i2pd router 之间获得一致的性能，使用选项如 inbound.quantity=3 outbound.quantity=3。这些和其他选项[在下面的链接中有文档说明](#tunnel-i2cp-and-streaming-options)。

SAM bridge 本身应该已经配置好了它应该通过哪个 router 进行 I2P 通信（不过如果需要的话，可能有办法提供覆盖配置，例如 i2cp.tcp.host=localhost 和 i2cp.tcp.port=7654）。

#### 会话创建响应

在接收到会话创建消息后，SAM bridge 将回复一个会话状态消息，如下所示：

如果创建成功：

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
$privkey 是以下内容串联的 base 64 编码：[Destination](/docs/specs/common-structures#type_Destination)，然后是 [Private Key](/docs/specs/common-structures#type_PrivateKey)，然后是 [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)，可选地后面跟着 [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature)，根据签名类型，二进制格式为 663 字节或更多，base 64 格式为 884 字节或更多。二进制格式在私钥文件中指定。

如果 SESSION CREATE 包含全零的签名私钥和一个 [离线签名](/docs/specs/common-structures#struct_OfflineSignature) 部分，SESSION STATUS 回复将包含相同格式的相同数据。详细信息请参阅上面的 SESSION CREATE 部分。

如果昵称已经与某个会话关联：

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
如果目标地址已在使用中：

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
如果目标不是有效的私有目标密钥：

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
如果发生了其他错误：

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
如果不成功，MESSAGE 应该包含人类可读的信息，说明为什么无法创建会话。

请注意，router 在响应 SESSION STATUS 之前会构建 tunnel。这可能需要几秒钟，或者在 router 启动时或严重网络拥塞期间，可能需要一分钟或更长时间。如果不成功，router 将在几分钟内不会响应失败消息。等待响应时不要设置过短的超时时间。在 tunnel 构建过程中不要放弃会话并重试。

SAM 会话与其关联的套接字共存亡。当套接字关闭时，会话终止，同时使用该会话的所有通信也会终止。反之亦然，当会话因任何原因终止时，SAM 桥接器会关闭套接字。

### SAM 虚拟流

虚拟流保证可靠且有序地发送，并在故障或成功通知可用时立即提供反馈。

流（Streams）是两个I2P目标地址之间的双向通信套接字，但它们的打开必须由其中一个目标地址请求。此后，SAM客户端使用CONNECT命令来发出此类请求。当SAM客户端想要监听来自其他I2P目标地址的请求时，会使用FORWARD / ACCEPT命令。

### SAM 虚拟流：CONNECT

客户端通过以下方式请求连接：

- 与 SAM bridge 建立新的套接字连接
- 传递与上述相同的 HELLO 握手
- 发送 STREAM CONNECT 命令

#### 连接请求

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
这将建立一个从 ID 为 $nickname 的本地会话到指定对等节点的新虚拟连接。

目标是 $destination，它是 [Destination](/docs/specs/common-structures#type_Destination) 的 base 64 编码，根据签名类型不同，包含 516 个或更多 base 64 字符（二进制形式为 387 个或更多字节）。

**注意：** 自2014年左右（SAM v3.1）开始，Java I2P也支持在$destination中使用主机名和b32地址，但这在之前并未记录在文档中。从0.9.48版本开始，主机名和b32地址现已得到Java I2P的官方支持。i2pd router从2.38.0版本（0.9.50）开始支持主机名和b32地址。对于两种router，"b32"支持包括对盲化目标地址的扩展"b33"地址的支持。

#### 连接响应

如果传递了 SILENT=true，SAM bridge 不会在套接字上发出任何其他消息。如果连接失败，套接字将被关闭。如果连接成功，通过当前套接字传递的所有剩余数据将从连接的 I2P 目标对等节点转发到该节点或从该节点转发。

如果 SILENT=false（这是默认值），SAM bridge 会在转发或关闭套接字之前向其客户端发送最后一条消息：

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT 值可能是以下之一：

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
如果 RESULT 是 OK，则通过当前套接字传输的所有剩余数据都会与连接的 I2P 目标节点进行转发。如果连接不可能（超时等），RESULT 将包含相应的错误值（附带可选的人类可读 MESSAGE），SAM 桥接器会关闭套接字。

router 流连接的内部超时时间大约为一分钟，具体取决于实现。在等待响应时不要设置更短的超时时间。

### SAM 虚拟流：ACCEPT

客户端通过以下方式等待传入的连接请求：

- 与SAM bridge建立新的套接字连接
- 传递与上述相同的HELLO握手
- 发送STREAM ACCEPT命令

#### 接受请求

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
这使得会话 ${nickname} 监听来自 I2P 网络的一个传入连接请求。当会话上有活跃的 FORWARD 时，不允许使用 ACCEPT。

从 SAM 3.2 开始，允许在同一个会话 ID 上进行多个并发的待处理 STREAM ACCEPT（即使是相同端口）。在 3.2 之前，并发 accept 会失败并返回 ALREADY_ACCEPTING。注意：Java I2P 从 0.9.24 版本（2016年1月）开始也在 SAM 3.1 上支持并发 ACCEPT。i2pd 从 2.50.0 版本（2023年12月）开始也在 SAM 3.1 上支持并发 ACCEPT。

#### 接受响应

如果传递了 SILENT=true，SAM bridge 不会在套接字上发出任何其他消息。如果接受失败，套接字将被关闭。如果接受成功，通过当前套接字传递的所有剩余数据将从连接的 I2P destination 对等方转发到该对等方。为了可靠性，以及接收传入连接的 destination，建议使用 SILENT=false。

如果 SILENT=false（这是默认值），SAM bridge 会回应：

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT 值可能是以下之一：

```
OK
I2P_ERROR
INVALID_ID
```
如果结果不是 OK，socket 会被 SAM bridge 立即关闭。如果结果是 OK，SAM bridge 开始等待来自其他 I2P peer 的传入连接请求。当请求到达时，SAM bridge 接受它并：

如果传递了 SILENT=true，SAM bridge 将不会在客户端套接字上发送任何其他消息。通过当前套接字传递的所有剩余数据都会转发到连接的 I2P 目标对等节点或从其转发。

如果传递了 SILENT=false（这是默认值），SAM bridge 会向客户端发送一行 ASCII 文本，包含请求对等节点的 base64 公钥目标地址，以及仅适用于 SAM 3.2 的附加信息：

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
在这个以 '\\n' 结尾的行之后，通过当前套接字传输的所有剩余数据都会与连接的 I2P destination 对等节点进行转发，直到其中一个对等节点关闭套接字为止。

#### OK后的错误

在极少数情况下，SAM bridge可能在发送RESULT=OK之后但在连接建立并向客户端发送$destination行之前遇到错误。这些错误可能包括router关闭、router重启和会话关闭。在这些情况下，当SILENT=false时，SAM bridge可能（但不是必须的，取决于实现）发送以下行：

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
然后立即关闭套接字。当然，这一行无法解码为有效的 Base 64 目标地址。

### SAM Virtual Streams: FORWARD

客户端可以使用常规套接字服务器并等待来自I2P的连接请求。为此，客户端必须：

- 与 SAM bridge 建立新的套接字连接
- 执行与上述相同的 HELLO 握手
- 发送转发命令

#### 转发请求

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
这使得会话 ${nickname} 监听来自 I2P 网络的传入连接请求。当会话上有待处理的 ACCEPT 时，不允许使用 FORWARD。

#### 转发响应

SILENT 默认为 false。无论 SILENT 是 true 还是 false，SAM bridge 总是会回复 STREAM STATUS 消息。请注意，这与 SILENT=true 时 STREAM ACCEPT 和 STREAM CONNECT 的行为不同。STREAM STATUS 消息是：

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT 值可能是以下之一：

```
OK
I2P_ERROR
INVALID_ID
```
$host 是 SAM 将转发连接请求的套接字服务器的主机名或 IP 地址。如果未提供，SAM 将使用发出转发命令的套接字的 IP 地址。

$port 是套接字服务器的端口号，SAM 将向该服务器转发连接请求。此参数是必需的。

当来自I2P的连接请求到达时，SAM bridge会打开一个到$host:$port的socket连接。如果在3秒内被接受，SAM将接受来自I2P的连接，然后：

如果传递了 SILENT=true，则通过获得的当前套接字传递的所有数据都会转发到连接的 I2P 目标节点以及从该节点转发回来。

如果传递了 SILENT=false（这是默认值），SAM 网桥会在获得的套接字上发送一个 ASCII 行，包含请求对等节点的 base64 公钥目标密钥，以及仅适用于 SAM 3.2 的附加信息：

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
在这个以'\\n'结尾的行之后，所有通过套接字传递的剩余数据都会在连接的I2P目标对等节点之间转发，直到其中一方关闭套接字。

从SAMv3.2开始，如果指定SSL=true，转发socket将使用SSL/TLS。

一旦"转发"套接字关闭，I2P router将停止监听传入的连接请求。

### SAM 数据报

SAMv3 提供了通过本地数据报套接字发送和接收数据报的机制。一些 SAMv3 实现还支持通过 SAM 桥接套接字发送/接收数据报的旧版 v1/v2 方式。以下将对两种方式进行说明。

I2P支持四种类型的数据报：

- 可回复和已认证的数据报以发送方的目标地址为前缀，并包含发送方的签名，因此接收方可以验证发送方的目标地址未被欺骗，并可以回复该数据报。新的 Datagram2 格式也是可回复和已认证的。
- 新的 Datagram3 格式是可回复但未认证的。发送方信息未经验证。
- 原始数据报不包含发送方的目标地址或签名。

默认的 I2CP 端口已为可回复和原始数据报定义。原始数据报的 I2CP 端口可以更改。

一种常见的协议设计模式是向服务器发送可回复数据报，其中包含某个标识符，服务器以包含该标识符的原始数据报进行响应，这样响应就可以与请求相关联。这种设计模式消除了回复中可回复数据报的大量开销。所有I2CP协议和端口的选择都是特定于应用程序的，设计者应该考虑这些问题。

另请参阅下面章节中关于数据报 MTU 的重要说明。

#### 发送可回复或原始数据报

虽然I2P本身不包含FROM地址，但为了使用方便，提供了一个额外的层作为可回复数据报 - 最大31744字节的无序且不可靠消息，其中包含FROM地址（为头部材料保留最多1KB空间）。这个FROM地址由SAM在内部进行身份验证（利用destination的签名密钥来验证源），并包含重放防护。

最小大小为 1。为了获得最佳传输可靠性，建议最大大小约为 11 KB。可靠性与消息大小成反比，甚至可能呈指数关系。

在使用 STYLE=DATAGRAM 或 STYLE=RAW 建立 SAMv3 会话后，客户端可以通过 SAM 的 UDP 端口（默认为 7655）发送可回复的或原始数据报。

通过此端口发送的数据报的第一行必须采用以下格式。这些内容全部在一行中（以空格分隔），为了清晰起见显示为多行：

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
- 3.0 是 SAM 的版本。从 SAM 3.2 开始，允许使用任何 3.x 版本。
- $nickname 是将要使用的 DATAGRAM 会话的 id
- 目标是 $destination，它是 [Destination](/docs/specs/common-structures#type_Destination) 的 base 64 编码，包含 516 个或更多 base 64 字符（二进制为 387 字节或更多），取决于签名类型。**注意：** 从大约 2014 年（SAM v3.1）开始，Java I2P 也支持在 $destination 中使用主机名和 b32 地址，但这之前没有文档记录。从 0.9.48 版本开始，Java I2P 正式支持主机名和 b32 地址。i2pd router 目前不支持主机名和 b32 地址；可能会在未来版本中添加支持。
- 所有选项都是每个数据报的设置，会覆盖在 SESSION CREATE 中指定的默认值。
- 版本 3.3 的选项 SEND_TAGS、TAG_THRESHOLD、EXPIRES 和 SEND_LEASESET 将在支持的情况下传递给 [I2CP](/docs/protocol/i2cp)。详情请参见 [I2CP 规范](/docs/protocol/i2cp#msg_SendMessageExpire)。SAM 服务器的支持是可选的，如果不支持这些选项将被忽略。
- 此行以 '\\n' 终止。

第一行将被 SAM 丢弃，然后将消息的剩余数据发送到指定的目标。

有关发送可回复和原始数据报的其他方法，请参阅 [DATAGRAM SEND 和 RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling)。

#### SAM 可回复数据报：接收数据报

如果在 SESSION CREATE 命令中未指定转发 PORT，则接收到的数据报将由 SAMv3 写入打开数据报会话的套接字。这是接收数据报的 v1/v2 兼容方式。

当数据报到达时，网桥通过消息将其传递给客户端：

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
源是 $destination，这是 [Destination](/docs/specs/common-structures#type_Destination) 的 base 64 编码，根据签名类型不同，包含 516 个或更多 base 64 字符（二进制格式为 387 个或更多字节）。

SAM bridge 从不向客户端暴露认证头或其他字段，仅提供发送方提供的数据。这种情况会持续到会话关闭（由客户端断开连接）。

#### 转发原始或可回复数据报

在创建数据报会话时，客户端可以要求SAM将传入的消息转发到指定的ip:port。通过在CREATE命令中使用PORT和HOST选项来实现：

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
$privkey 是以下内容连接后的 base 64 编码：[Destination](/docs/specs/common-structures#type_Destination) 后跟 [Private Key](/docs/specs/common-structures#type_PrivateKey) 后跟 [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)，可选地后跟 [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature)，总长度为 884 个或更多 base 64 字符（二进制格式为 663 个或更多字节），具体取决于签名类型。二进制格式在私钥文件中指定。

离线签名支持 RAW、DATAGRAM2 和 DATAGRAM3 数据报，但不支持 DATAGRAM。详情请参见上面的 SESSION CREATE 部分和下面的 DATAGRAM2/3 部分。

$host 是 SAM 将转发数据报的数据报服务器的主机名或 IP 地址。如果未提供，SAM 将使用发出转发命令的套接字的 IP 地址。

$port 是数据报服务器的端口号，SAM 会将数据报转发到该端口。如果未设置 $port，数据报将不会被转发，它们将在控制套接字上接收，采用 v1/v2 兼容的方式。

提供的其他选项如果不被SAM桥接器解释，则会传递给I2P会话配置（例如outbound.length=0）。这些选项[在下面有详细说明](#tunnel-i2cp-and-streaming-options)。

转发的可回复数据报总是以base64目标地址为前缀，除了Datagram3，见下文。当可回复数据报到达时，网桥向指定的host:port发送包含以下数据的UDP数据包：

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
转发的原始数据报按原样转发到指定的主机:端口，不添加前缀。UDP 数据包包含以下数据：

```
$datagram_payload
```
从 SAM 3.2 开始，当在 SESSION CREATE 中指定 HEADER=true 时，转发的原始数据报将在前面加上如下的头部行：

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
$destination 是 [Destination](/docs/specs/common-structures#type_Destination) 的 base 64 编码，根据签名类型不同，长度为 516 个或更多 base 64 字符（二进制形式为 387 个或更多字节）。

#### SAM 匿名（原始）数据报

为了最大化利用I2P的带宽，SAM允许客户端发送和接收匿名数据报，将身份验证和回复信息的处理留给客户端自己处理。这些数据报是不可靠和无序的，最大可达32768字节。

最小大小为1。为了获得最佳传输可靠性，建议最大大小约为11KB。

在建立了 STYLE=RAW 的 SAM 会话后，客户端可以通过 SAM 桥发送匿名数据报，方式与[发送可回复数据报](#sending-repliable-or-raw-datagrams)完全相同。

这两种接收数据报的方式也适用于匿名数据报。

如果在 SESSION CREATE 命令中未指定转发端口，接收到的数据报将由 SAMv3 写入到打开数据报会话的套接字上。这是兼容 v1/v2 版本的数据报接收方式。

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
当匿名数据报需要转发到某个主机:端口时，网桥会向指定的主机:端口发送包含以下数据的消息：

```
$datagram_payload
```
从 SAM 3.2 开始，当在 SESSION CREATE 中指定 HEADER=true 时，转发的原始数据报将在前面加上如下的头部行：

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
有关发送匿名数据报的替代方法，请参见 [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling)。

#### 数据报 2/3

Datagram 2/3 是在 2025 年初指定的新格式。目前尚无已知的实现。请查看实现文档了解当前状态。更多信息请参见[规范](/docs/specs/datagrams)。

目前没有计划增加SAM版本来表示Datagram 2/3支持。这可能会有问题，因为实现可能希望支持Datagram 2/3但不支持SAM v3.3功能。任何版本更改都待定。

Datagram2 和 Datagram3 都是可回复的。只有 Datagram2 是经过身份验证的。

从 SAM 角度来看，Datagram2 与可回复数据报相同。两者都经过身份验证。只有 I2CP 格式和签名不同，但这对 SAM 客户端是不可见的。Datagram2 还支持离线签名，因此可以被离线签名目标使用。

Datagram2的目的是为不需要向后兼容性的新应用程序替换Repliable数据报。Datagram2提供了Repliable数据报所没有的重放保护功能。如果需要向后兼容性，应用程序可以在SAM 3.3 PRIMARY会话中同时支持Datagram2和Repliable。

Datagram3 是可回复的但未经身份验证。I2CP 格式中的 'from' 字段是一个哈希值，而不是目的地。从 SAM 服务器发送到客户端的 $destination 将是一个 44 字节的 base64 哈希值。要将其转换为用于回复的完整目的地，需要将其 base64 解码为 32 字节二进制数据，然后 base32 编码为 52 个字符并附加".b32.i2p"进行 NAMING LOOKUP。和往常一样，客户端应该维护自己的缓存以避免重复的 NAMING LOOKUP。

应用程序设计者应当极其谨慎，并考虑未经身份验证的数据报的安全影响。

#### V3 数据报 MTU 注意事项

I2P 数据报可能比典型互联网 MTU 1500 字节更大。本地发送的数据报和带有 516+ 字节 base64 目标地址前缀的可转发可回复数据报可能会超过该 MTU。然而，Linux 系统上的本地主机 MTU 通常要大得多，例如 65536。本地主机 MTU 会因操作系统而异。I2P 数据报永远不会大于 65536 字节。数据报大小取决于应用协议。

如果SAM客户端与SAM服务器在同一本地系统上，并且系统支持更大的MTU，那么数据报不会在本地被分片。但是，如果SAM客户端是远程的，那么IPv4数据报会被分片，而IPv6数据报会失败（IPv6不支持UDP分片）。

客户端库和应用程序开发者应该了解这些问题并记录建议，以避免分片并防止数据包丢失，特别是在远程SAM客户端-服务器连接上。

#### DATAGRAM SEND, RAW SEND（V1/V2兼容数据报处理）

在SAMv3中，发送数据报的首选方式是通过上面记录的端口7655的数据报套接字。但是，可回复的数据报也可以使用DATAGRAM SEND命令直接通过SAM桥接套接字发送，如[SAM V1](/docs/api/sam)和[SAM V2](/docs/api/samv2)中所记录的。

从 0.9.14 版本（版本 3.1）开始，可以通过 SAM 桥接套接字使用 RAW SEND 命令直接发送匿名数据报，详见 [SAM V1](/docs/api/sam) 和 [SAM V2](/docs/api/samv2) 文档。

从版本 0.9.24（版本 3.2）开始，DATAGRAM SEND 和 RAW SEND 可以包含参数 FROM_PORT=nnnn 和/或 TO_PORT=nnnn 来覆盖默认端口。从版本 0.9.24（版本 3.2）开始，RAW SEND 可以包含参数 PROTOCOL=nnn 来覆盖默认协议。

这些命令*不*支持ID参数。数据报会根据情况发送到最近创建的DATAGRAM或RAW风格的会话。未来版本可能会添加对ID参数的支持。

DATAGRAM2 和 DATAGRAM3 格式*不*支持 V1/V2 兼容方式。

### SAM PRIMARY 会话（V3.3 及更高版本）

*版本 3.3 在 I2P 发布版 0.9.25 中引入。*

*在本规范的早期版本中，PRIMARY 会话被称为 MASTER 会话。在 `i2pd` 和 `I2P+` 中，它们仍然只被称为 MASTER 会话。*

SAMv3.3 增加了对在同一个主会话上运行流式传输、数据报和原始子会话的支持，以及运行多个相同类型子会话的支持。所有子会话流量使用单一目标地址或隧道集。来自 I2P 的流量路由基于子会话的端口和协议选项。

要创建多路复用子会话，您必须先创建一个主会话，然后向主会话添加子会话。每个子会话必须有唯一的id以及唯一的监听协议和端口。子会话也可以从主会话中移除。

通过PRIMARY会话和子会话的组合，SAM客户端可以在一组隧道上支持多个应用程序，或者支持使用多种协议的单个复杂应用程序。例如，一个BitTorrent客户端可以为点对点连接设置一个流式子会话，同时为DHT通信设置数据报和原始子会话。

#### 创建主要会话

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
SAM bridge 将响应成功或失败，如[标准 SESSION CREATE 的响应](#session-creation-response)中所述。

不要在主会话上设置 PORT、HOST、FROM_PORT、TO_PORT、PROTOCOL、LISTEN_PORT、LISTEN_PROTOCOL 或 HEADER 选项。您不能在主会话 ID 或控制套接字上发送任何数据。所有命令如 STREAM CONNECT、DATAGRAM SEND 等都必须在单独的套接字上使用子会话 ID。

PRIMARY 会话连接到 router 并构建 tunnel。当 SAM 桥响应时，tunnel 已经构建完成，会话已准备好添加子会话。所有与 tunnel 参数相关的 [I2CP](/docs/protocol/i2cp) 选项，如长度、数量和昵称，都必须在主会话的 SESSION CREATE 中提供。

所有实用程序命令都在主会话上受支持。

当主会话关闭时，所有子会话也会被关闭。

注意：在 0.9.47 版本之前，使用 STYLE=MASTER。从 0.9.47 版本开始支持 STYLE=PRIMARY。MASTER 仍然支持以保持向后兼容性。

#### 创建子会话

使用创建 PRIMARY 会话的同一个控制套接字：

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
SAM桥接器将响应成功或失败，如[标准SESSION CREATE的响应](#session-creation-response)中所述。由于tunnel已经在主要的SESSION CREATE中构建，SAM桥接器应该立即响应。

不要在 SESSION ADD 上设置 DESTINATION 选项。子会话将使用在主会话中指定的目标地址。所有子会话都必须在控制套接字上添加，即在创建主会话的同一连接上。

多个子会话必须具有足够独特的选项，以便传入数据能够正确路由。特别是，相同类型的多个会话必须具有不同的 LISTEN_PORT 选项（和/或 LISTEN_PROTOCOL，仅适用于 RAW）。使用与现有子会话重复的监听端口和协议执行 SESSION ADD 将导致错误。

LISTEN_PORT 是本地 I2P 端口，即用于接收传入数据的接收（TO）端口。如果没有指定 LISTEN_PORT，将使用 FROM_PORT 的值。如果既没有指定 LISTEN_PORT 也没有指定 FROM_PORT，传入路由将仅基于 STYLE 和 PROTOCOL。对于 LISTEN_PORT 和 LISTEN_PROTOCOL，0 表示任意值，即通配符。如果 LISTEN_PORT 和 LISTEN_PROTOCOL 都是 0，此子会话将成为不会路由到其他子会话的传入流量的默认会话。传入的流式传输流量（协议 6）永远不会路由到 RAW 子会话，即使其 LISTEN_PROTOCOL 是 0。RAW 子会话不能设置 LISTEN_PROTOCOL 为 6。如果没有默认或匹配传入流量协议和端口的子会话，该数据将被丢弃。

使用子会话ID，而不是主会话ID来发送和接收数据。所有命令如STREAM CONNECT、DATAGRAM SEND等都必须使用子会话ID。

所有实用命令在主会话或子会话上都受支持。主会话或子会话不支持 v1/v2 数据报/原始数据的发送/接收。

#### 停止子会话

使用创建 PRIMARY 会话的同一个控制套接字：

```
->  SESSION REMOVE
          ID=$nickname
```
这会从主会话中移除一个子会话。在 SESSION REMOVE 上不要设置任何其他选项。子会话必须在控制套接字上移除，即创建主会话的同一连接上。子会话被移除后，它会被关闭且不能再用于发送或接收数据。

SAM bridge 将响应成功或失败，如[标准 SESSION CREATE 的响应](#session-creation-response)中所示。

### SAM 实用命令

一些实用程序命令需要预先存在的会话，而另一些则不需要。详情请参见下文。

#### 主机名查找

客户端可以使用以下消息向 SAM 网桥查询名称解析：

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
其答案是

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
RESULT 值可能是以下之一：

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
如果 NAME=ME，则回复将包含当前会话使用的目标地址（如果您使用的是 TRANSIENT 类型，这会很有用）。如果 $result 不是 OK，MESSAGE 可能会传达描述性消息，如"格式错误"等。INVALID_KEY 表示请求中的 $name 存在问题，可能包含无效字符。

$destination 是 [Destination](/docs/specs/common-structures#type_Destination) 的 base 64 编码，根据签名类型不同，包含 516 个或更多 base 64 字符（二进制格式为 387 个或更多字节）。

NAMING LOOKUP 不要求必须先创建会话。但是，在某些实现中，未缓存且需要网络查询的 .b32.i2p 查找可能会失败，因为没有可用于查找的客户端 tunnel。

#### 名称查找选项

NAMING LOOKUP 在 router API 0.9.66 中得到扩展，支持服务查找。支持情况可能因实现而异。更多信息请参见提案 167。

NAMING LOOKUP NAME=example.i2p OPTIONS=true 请求在回复中包含选项映射。当 OPTIONS=true 时，NAME 可以是完整的 base64 目标地址。

如果目标查找成功且 leaseset 中存在选项，那么在回复中，跟随目标之后，将会有一个或多个格式为 OPTION:key=value 的选项。每个选项都会有单独的 OPTION: 前缀。leaseset 中的所有选项都会被包含，不仅仅是服务记录选项。例如，未来定义的参数选项也可能存在。示例：

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

包含'='的键，以及包含换行符的键或值，被视为无效，该键/值对将从回复中移除。如果在leaseSet中未找到选项，或者leaseSet是版本1，则响应将不包含任何选项。如果查找中包含OPTIONS=true，而leaseSet未找到，将返回新的结果值LEASESET_NOT_FOUND。

#### 目标密钥生成

可以使用以下消息生成公钥和私钥的base64格式：

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
其回答是

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
从版本 3.1 开始（I2P 0.9.14），支持一个可选参数 SIGNATURE_TYPE。SIGNATURE_TYPE 值可以是任何受 [Key Certificates](/docs/specs/common-structures#type_Certificate) 支持的名称（例如 ECDSA_SHA256_P256，不区分大小写）或数字（例如 1）。默认值是 DSA_SHA1，这不是您想要的。对于大多数应用程序，请指定 SIGNATURE_TYPE=7。

$destination 是 [Destination](/docs/specs/common-structures#type_Destination) 的 base 64 编码，根据签名类型不同，长度为 516 个或更多 base 64 字符（二进制格式为 387 个或更多字节）。

$privkey 是以下内容连接后的 base 64 编码：[Destination](/docs/specs/common-structures#type_Destination) 后跟 [Private Key](/docs/specs/common-structures#type_PrivateKey) 再跟 [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)，根据签名类型不同，这是 884 个或更多 base 64 字符（二进制格式为 663 个或更多字节）。二进制格式在 Private Key File 中有详细说明。

关于256字节二进制[Private Key](/docs/specs/common-structures#type_PrivateKey)的说明：此字段自0.6版本（2005年）以来就未使用。SAM实现可能在此字段中发送随机数据或全零；对于base 64中的一串AAAA不必惊慌。大多数应用程序将简单地存储base 64字符串并在SESSION CREATE中按原样返回，或解码为二进制进行存储，然后为SESSION CREATE重新编码。但是，应用程序也可以解码base 64，按照PrivateKeyFile规范解析二进制数据，丢弃256字节的private key部分，然后在为SESSION CREATE重新编码时用256字节的随机数据或全零替换它。PrivateKeyFile规范中的所有其他字段都必须保留。这将节省256字节的文件系统存储空间，但对大多数应用程序来说可能不值得这么麻烦。有关其他信息和背景，请参见提案161。

DEST GENERATE 不需要先创建会话。

DEST GENERATE 不能用于创建具有离线签名的目标地址。

#### PING/PONG (SAM 3.2 或更高版本)

客户端或服务器都可以发送：

```
PING[ arbitrary text]
```
在控制端口上，响应为：

```
PONG[ arbitrary text from the ping]
```
用于控制套接字保活。如果在合理时间内没有收到响应，任何一方都可以关闭会话和套接字，具体实现取决于实现方式。

如果等待客户端 PONG 响应时发生超时，桥接器可能会发送：

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
然后断开连接。

如果在等待来自网桥的 PONG 时发生超时，客户端可以直接断开连接。

PING/PONG 不要求必须先创建会话。

#### QUIT/STOP/EXIT（SAM 3.2 或更高版本，可选功能）

命令 QUIT、STOP 和 EXIT 将关闭会话和套接字。这些命令的实现是可选的，主要是为了便于通过 telnet 进行测试。在套接字关闭之前是否有任何响应（例如 SESSION STATUS 消息）是特定于实现的，超出了本规范的范围。

QUIT/STOP/EXIT 命令不需要先创建会话。

#### HELP（可选功能）

服务器可以实现 HELP 命令。此实现是可选的，主要是为了便于通过 telnet 进行测试。输出格式和输出结束的检测是特定于实现的，超出了本规范的范围。

HELP 不要求必须先创建会话。

#### 授权配置（SAM 3.2 或更高版本，可选功能）

使用 AUTH 命令进行授权配置。SAM 服务器可以实现这些命令以便于凭据的持久化存储。除了使用这些命令之外的身份验证配置是特定于实现的，超出了本规范的范围。

- AUTH ENABLE 在后续连接上启用授权
- AUTH DISABLE 在后续连接上禁用授权
- AUTH ADD USER="foo" PASSWORD="bar" 添加用户名/密码
- AUTH REMOVE USER="foo" 移除此用户

推荐但不强制要求在用户名和密码周围使用双引号。用户名或密码内部的双引号必须用反斜杠进行转义。失败时服务器将回复 I2P_ERROR 和一条消息。

AUTH 不需要先创建会话。

### RESULT 值

这些是 RESULT 字段可以携带的值及其含义：

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
不同的实现在各种场景下返回的 RESULT 可能不一致。

大多数带有RESULT的响应（除了OK之外）还会包含一个MESSAGE，提供额外信息。MESSAGE通常有助于调试问题。但是，MESSAGE字符串依赖于具体实现，SAM服务器可能会也可能不会将其翻译为当前语言环境，可能包含内部实现特定的信息（如异常），并且可能在不另行通知的情况下发生变更。虽然SAM客户端可以选择向用户显示MESSAGE字符串，但不应基于这些字符串做出程序化决策，因为这样做会很脆弱。

### Tunnel、I2CP 和流传输选项

这些选项可以作为 name=value 键值对在 SAM SESSION CREATE 行中传递。

所有会话都可以包含 [I2CP 选项，如 tunnel 长度和数量](/docs/protocol/i2cp#options)。STREAM 会话可以包含 [Streaming 库选项](/docs/api/streaming#options)。

请参阅这些参考文档了解选项名称和默认值。引用的文档适用于Java router实现。默认值可能会发生变化。选项名称和值区分大小写。其他router实现可能不支持所有选项，并且可能有不同的默认值；请查阅router文档了解详情。

### BASE 64 说明

Base 64 编码必须使用 I2P 标准 Base 64 字母表 "A-Z, a-z, 0-9, -, ~"。

### 默认 SAM 设置

默认的SAM端口是7656。SAM在Java I2P Router中默认未启用；必须在router控制台的配置客户端页面手动启动，或配置为自动启动，也可以在clients.config文件中配置。默认的SAM UDP端口是7655，监听127.0.0.1。这些可以在Java router中通过在调用时添加参数sam.udp.port=nnnnn和/或sam.udp.host=w.x.y.z来更改，或者在SESSION行中更改。

其他 router 中的配置是特定于实现的。请参阅[此处的 i2pd 配置指南](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/)。

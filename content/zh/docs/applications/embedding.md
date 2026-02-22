---
title: "在您的应用程序中嵌入 I2P"
description: "在您的应用程序中捆绑 I2P router 的指南"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## 概述

本页面介绍如何将整个I2P router二进制文件与你的应用程序打包在一起。这不是关于编写与I2P配合工作的应用程序（无论是打包还是外部的）。不过，即使不打包router，许多准则也可能很有用。

许多项目正在捆绑或讨论捆绑I2P。如果操作得当，这很好。如果操作不当，可能会对我们的网络造成真正的伤害。I2P router很复杂，向用户隐藏所有复杂性可能是一个挑战。本页面讨论一些一般准则。

这些指导原则大多同样适用于Java I2P或i2pd。但是，一些指导原则是Java I2P特有的，下文会有说明。

### 联系我们

开始对话。我们在这里提供帮助。嵌入I2P的应用程序是我们扩展网络和为每个人改善匿名性的最有前景和最令人兴奋的机会。

### 明智地选择你的 router

如果您的应用程序是用 Java 或 Scala 开发的，这很容易选择 - 使用 Java router。如果是 C/C++，我们推荐 i2pd。i2pcpp 的开发已经停止。对于其他语言的应用程序，最好使用 SAM 或 BOB 或 SOCKS，并将 Java router 作为单独的进程打包。以下部分内容仅适用于 Java router。

### 许可协议

确保您符合所打包软件的许可证要求。

---

## 配置

### 验证默认配置

正确的默认配置至关重要。大多数用户不会更改默认设置。您的应用程序的默认配置可能需要与您捆绑的 router 的默认配置不同。如有必要，请覆盖 router 的默认设置。

需要检查的一些重要默认设置：最大带宽、tunnel 数量和长度、最大参与 tunnel 数量。这些设置在很大程度上取决于你的应用程序的预期带宽和使用模式。

配置足够的带宽和tunnel以允许您的用户为网络做出贡献。考虑禁用外部I2CP，因为您可能不需要它，并且它会与任何其他正在运行的I2P实例发生冲突。另外，请查看配置以禁用退出时终止JVM的设置等。

### 参与流量考虑因素

您可能会想要禁用参与流量。有几种方法可以做到这一点（隐藏模式、将最大 tunnel 数量设置为 0、将共享带宽设置为低于 12 KB/秒）。如果没有参与流量，您就不必担心优雅关闭，您的用户也不会看到不是由他们产生的带宽使用等。但是，您应该允许参与 tunnel 有很多原因。

首先，如果 router 没有机会与网络"整合"，它就无法很好地工作，而其他人通过你建立 tunnel 对此帮助极大。

其次，当前网络中超过90%的router允许参与中转流量。这是Java router的默认设置。如果你的应用程序不为其他人提供路由服务但却变得非常受欢迎，那么它就成了网络的寄生虫，破坏了我们目前的平衡。如果它变得真的很大，那么我们就会变成Tor，把时间花在恳求人们启用中继功能上。

第三，参与流量是覆盖流量，有助于保护您用户的匿名性。

我们强烈建议您不要默认禁用参与流量。如果您这样做并且您的应用程序变得非常受欢迎，这可能会破坏网络。

### 持久化

您必须在 router 运行之间保存 router 的数据（netDb、配置等）。如果每次启动都必须重新获取种子数据，I2P 无法正常工作，这会给我们的种子服务器带来巨大负载，对匿名性也不利。即使您打包了 router 信息，I2P 也需要保存的配置文件数据才能获得最佳性能。没有持久化，您的用户将会有糟糕的启动体验。

如果您无法提供持久化存储，有两种可能的解决方案。任何一种都可以消除您项目对我们 reseed 服务器的负载，并显著改善启动时间。

1) 建立你自己的项目 reseed 服务器，提供比通常数量多得多的 router 信息，比如几百个。配置 router 只使用你的服务器。

2) 在您的安装程序中捆绑一到两千个 router info。

此外，延迟或错开您的 tunnel 启动时间，给 router 一个机会在构建大量 tunnel 之前先进行整合。

### 可配置性

为您的用户提供更改重要设置配置的方法。我们理解您可能希望隐藏I2P的大部分复杂性，但显示一些基本设置是很重要的。除了上述默认设置外，一些网络设置如UPnP、IP/端口等可能会有所帮助。

### Floodfill 注意事项

超过某个带宽设置，并且满足其他健康标准时，你的 router 将成为 floodfill，这可能会导致连接数和内存使用量大幅增加（至少在 Java router 中是这样）。请考虑这是否可以接受。你可以禁用 floodfill，但这样你最快的用户就无法贡献他们应有的资源。这也取决于你应用程序的典型运行时间。

### 重新播种

决定是否要捆绑 router info 或使用我们的重新种子主机。Java 重新种子主机列表位于源代码中，所以如果您保持源代码更新，主机列表也会随之更新。请注意可能会被敌对政府封锁。

### 使用共享客户端

Java I2P i2ptunnel 支持共享客户端，客户端可以配置为使用单一池。如果您需要多个客户端，并且符合您的安全目标，请将客户端配置为共享模式。

### 限制 Tunnel 数量

使用 `inbound.quantity` 和 `outbound.quantity` 选项显式指定 tunnel 数量。Java I2P 中的默认值是 2；i2pd 中的默认值更高。在使用 SAM 的 SESSION CREATE 行中指定，以在两个 router 上获得一致的设置。对于大多数低到中等带宽和低到中等扇出的应用程序，入站和出站各两个就足够了。服务器和高扇出 P2P 应用程序可能需要更多。有关计算高流量服务器和应用程序需求的指导，请参见[此论坛帖子](http://zzz.i2p/topics/1584)。

### 指定 SAM SIGNATURE_TYPE

SAM 默认为目标使用 DSA_SHA1，这不是你想要的。Ed25519（类型 7）是正确的选择。在 DEST GENERATE 命令中添加 SIGNATURE_TYPE=7，或者在使用 DESTINATION=TRANSIENT 的 SESSION CREATE 命令中添加。

### 限制 SAM 会话

大多数应用程序只需要一个 SAM 会话。如果创建大量会话，SAM 可能会快速压垮本地 router，甚至更广泛的网络。如果多个子服务可以使用单个会话，请使用 PRIMARY 会话和 SUBSESSIONS 来设置它们（i2pd 目前不支持）。会话的合理限制是总共 3 或 4 个，或者在极少数情况下最多 10 个。如果您确实有多个会话，请确保为每个会话指定较低的 tunnel 数量，请参见上文。

几乎在任何情况下，你都不应该要求每个连接使用唯一的会话。如果没有仔细的设计，这可能会迅速对网络造成DDoS攻击。请仔细考虑你的安全目标是否需要唯一会话。在实现每连接会话之前，请咨询Java I2P或i2pd开发人员。

### 减少网络资源使用

请注意，这些选项目前在 i2pd 中不受支持。这些选项通过 I2CP 和 SAM 支持（除了 delay-open，它仅通过 i2ptunnel 支持）。详细信息请参阅 I2CP 文档（对于 delay-open，请参阅 i2ptunnel 配置文档）。

考虑将你的应用程序 tunnel 设置为延迟打开、空闲时减少和/或空闲时关闭。如果使用 i2ptunnel 这很简单，但如果直接使用 I2CP，你需要自己实现其中一些功能。请参考 i2psnark 的代码，了解如何减少 tunnel 数量然后关闭 tunnel，即使在存在一些后台 DHT 活动的情况下。

---

## 生命周期

### 可更新性

如果可能的话，请提供自动更新功能，或者至少提供新版本的自动通知。我们最担心的是大量无法更新的 router 存在于网络中。我们每年会发布大约 6-8 个 Java router 版本，用户保持更新对网络健康至关重要。通常在发布后的 6 周内，我们会有超过 80% 的网络运行在最新版本上，我们希望保持这种状态。您不需要担心禁用 router 内置的自动更新功能，因为该代码位于 router console 中，而您大概不会打包这部分。

### 部署

制定渐进式推广计划。不要一下子让网络负载过重。我们目前每天约有2.5万独立用户，每月有4万独立用户。我们可能能够处理每年2-3倍的增长而不会出现太大问题。如果您预期增长速度会更快，或者您的用户群的带宽分布（或在线时间分布，或任何其他重要特征）与我们当前用户群有显著差异，我们真的需要进行讨论。您的增长计划越大，这个检查清单中的其他所有内容就越重要。

### 设计并鼓励长时间运行

告诉你的用户，I2P在持续运行时效果最佳。启动后可能需要几分钟才能正常工作，首次安装后甚至需要更长时间。如果你的平均运行时间少于一小时，I2P可能不是合适的解决方案。

---

## 用户界面

### 显示状态

向用户提供一些指示，说明应用程序 tunnel 已准备就绪。鼓励用户保持耐心。

### 优雅关闭

如果可能，请延迟关闭直到您的参与 tunnel 过期。不要让用户轻易中断 tunnel，或者至少要求他们确认。

### 教育和捐赠

如果你能为用户提供更多了解I2P的链接和捐赠链接就太好了。

### 外部 Router 选项

根据您的用户群体和应用程序，提供使用外部 router 的选项或单独的软件包可能会很有帮助。

---

## 其他主题

### 使用其他通用服务

如果你计划使用或链接到其他常见的I2P服务（新闻源、hosts.txt订阅、tracker、outproxy等），请确保不会使它们过载，并与运行这些服务的人员沟通以确保获得许可。

### 时间 / NTP 问题

注意：本节内容适用于 Java I2P。i2pd 不包含 SNTP 客户端。

I2P 包含一个 SNTP 客户端。I2P 需要正确的时间才能运行。它可以补偿偏斜的系统时钟，但这可能会延迟启动。您可以禁用 I2P 的 SNTP 查询，但除非您的应用程序确保系统时钟正确，否则不建议这样做。

### 选择打包的内容和方式

注意：本节仅适用于 Java I2P。

至少你需要 i2p.jar、router.jar、streaming.jar 和 mstreaming.jar。对于仅使用数据报的应用，你可以省略这两个 streaming jar 文件。某些应用可能需要更多文件，例如 i2ptunnel.jar 或 addressbook.jar。不要忘记 jbigi.jar，或者为你支持的平台准备其子集，以使加密速度大幅提升。构建需要 Java 7 或更高版本。如果你正在构建 Debian / Ubuntu 包，你应该要求使用我们 PPA 中的 I2P 包，而不是将其打包在内。例如，你几乎肯定不需要 susimail、susidns、router console 和 i2psnark。

以下文件应包含在I2P安装目录中，通过"i2p.dir.base"属性指定。不要忘记certificates/目录，这是重新播种所必需的，以及用于IP验证的blocklist.txt。geoip目录是可选的，但建议包含，这样router可以基于位置做出决策。如果包含geoip，请确保将GeoLite2-Country.mmdb文件放在该目录中（从installer/resources/GeoLite2-Country.mmdb.gz解压缩）。可能需要hosts.txt文件，您可以修改它以包含您的应用程序使用的任何主机。您可以在基础目录中添加router.config文件来覆盖初始默认值。请检查并编辑或删除clients.config和i2ptunnel.config文件。

许可证要求可能需要您包含 LICENSES.txt 文件和 licenses 目录。

- 你可能还希望打包一个 hosts.txt 文件。
- 如果你为发行版编译 Java I2P 而不是使用我们的二进制文件，请确保指定 bootclasspath。

### Android 注意事项

注意：本节仅适用于 Java I2P。

我们的 Android router 应用可以被多个客户端共享。如果未安装该应用，用户在启动客户端应用时会收到提示。

一些开发者表示担心这种体验对用户不够友好，他们希望将 router 嵌入到自己的应用中。我们的路线图中确实包含一个 Android router 服务库，这可能会让嵌入变得更容易。需要更多信息。

如果您需要帮助，请联系我们。

### Maven jar包

注意：本节仅适用于 Java I2P。

我们在 [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22) 上有数量有限的 jar 包。我们有许多 trac 工单需要处理，这将改进和扩展在 Maven Central 上发布的 jar 包。

如果您需要帮助，请联系我们。

### 数据报（DHT）注意事项

如果您的应用程序使用 I2P 数据报，例如用于 DHT，有许多高级选项可用来减少开销并提高可靠性。这可能需要一些时间和实验才能正常工作。请注意大小/可靠性之间的权衡。如需帮助请联系我们。在同一个 Destination 上使用数据报和流是可能的，也是推荐的做法。不要为此创建单独的 Destination。不要尝试将与现有网络 DHT（iMule、bote、bittorrent 和 router）无关的数据存储在其中。构建您自己的 DHT。如果您要硬编码种子节点，我们建议您拥有多个种子节点。

### 出口代理

I2P 到明网的 outproxy（出口代理）是有限的资源。只能将 outproxy 用于正常的用户主动发起的网页浏览或其他有限的流量。对于任何其他用途，请咨询 outproxy 运营商并获得批准。

### 联合营销

让我们一起合作。不要等到完成后再行动。给我们你的 Twitter 账号并开始发推文，我们也会回报这份支持。

### 恶意软件

请不要将I2P用于恶意目的。这可能会对我们的网络和声誉造成巨大伤害。

### 加入我们

这可能很显而易见，但请加入社区。24/7运行I2P。为你的项目创建一个I2P网站。在IRC #i2p-dev频道聊天。在论坛发帖。传播消息。我们可以帮助你获得用户、测试人员、翻译人员，甚至编码人员。

---

## 示例

### 应用示例

您可能希望安装并试用 I2P Android 应用，并查看其代码，作为一个捆绑 router 的应用示例。了解我们向用户公开了什么，隐藏了什么。查看我们用于启动和停止 router 的状态机。其他示例包括：Vuze、Nightweb Android 应用、iMule、TAILS、iCloak 和 Monero。

### 代码示例

注意：本节仅适用于 Java I2P。

以上内容实际上都没有告诉您如何编写代码来打包 Java router，因此以下是一个简单的示例。

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
这段代码适用于您的应用程序启动router的情况，就像我们的Android应用程序中那样。您也可以让router通过clients.config和i2ptunnel.config文件以及Jetty webapps来启动应用程序，就像我们Java软件包中所做的那样。一如既往，状态管理是困难的部分。

另见：[router javadocs](http://idk.i2p/javadoc-i2p/net/i2p/router/Router.html)。

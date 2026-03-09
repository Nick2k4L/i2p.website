---
title: "开始使用 I2P：完整的新手指南"
description: "开始使用 I2P：完整的新手指南"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P 是一个完全加密的、在互联网“内部”运行的点对点匿名网络**，而来自 geti2p.net 的 Java 实现仍是使用它的主流方式。与主要为常规网络访问提供匿名化的 Tor 不同，I2P 构建了一个完全独立的网络，其中包含隐藏服务、网站、电子邮件、聊天和文件共享。

---

## 启动 I2P 的瞬间会发生什么

安装后，I2P 会在 `http://127.0.0.1:7657` 启动一个名为 **router console** 的本地Web应用程序。这是您的控制中心，完全在您的设备上运行，并出于安全考虑绑定到 localhost。首次启动时，**setup wizard** 会引导您完成语言选择、主题选择（深色或浅色），以及大约一分钟的自动带宽测试（使用外部 M-Lab 测量服务）。然后，您可以设置与网络共享的带宽百分比。

![I2P 安装向导 - 语言选择](/images/guides/quickstart/wizard-language-selection.webp)

向导完成后，路由器将开始一个称为“重新种子（reseeding）”的**引导（bootstrapping）**过程。路由器会通过 HTTPS 从硬编码的 reseed 服务器下载大约 **100 个 RouterInfo 记录**，从而获得初始的对等节点列表。随后，它会开始建立**探索性隧道**，以发现更多对等节点，并填充其本地的网络数据库副本（即“netDb”）。在最初几分钟内，你会看到“正在拒绝隧道：正在启动”的消息，这是正常现象。

![I2P 重新种子 - 引导](/images/guides/quickstart/reseed-bootstrapping.webp)

**预计需要等待 3–10 分钟**，你的路由器才能正常使用，而要达到最佳性能则需要更长时间——连续运行数天。路由器控制台侧边栏会以“活跃 x/y”显示你的对等节点数量，其中 x 是最近与你交换过消息的节点，y 是你所看到的所有节点。当你看到**活跃节点达到 10 个或以上**时，说明你的路由器已健康连接。新用户能做的最重要的一件事就是**让路由器持续运行**。每次关闭后，其他节点会将你的路由器标记为不可靠，至少持续 24 小时，因此频繁重启会严重损害性能。

![I2P 路由器控制台仪表盘](/images/guides/quickstart/router-console-dashboard.png)

---

## 为 I2P 配置您的浏览器

与Tor网络不同，I2P没有配备专用浏览器。要访问I2P网站（`.i2p`伪顶级域名），您需要配置浏览器的代理设置，将流量通过I2P的HTTP代理（端口 **4444**）进行路由。

**Windows 用户最简单的选择**是**一键安装包**，它集成了 Java、路由器以及预配置的 Firefox 浏览器配置文件，并内置了“I2P in Private Browsing”扩展。该安装包无需任何手动代理设置，从下载到浏览 I2P 网站大约只需四分钟。macOS（Apple Silicon）的一键安装包也已推出测试版。如果你使用一键安装包，可跳过下方的手动设置步骤。

### Firefox（推荐）

强烈推荐使用 Firefox，因为它拥有独立于操作系统的代理设置——而 Chrome 和 Edge 使用的是影响所有应用程序的系统范围代理设置。

**步骤1。** 打开Firefox菜单（汉堡图标），然后点击**设置**。

![Firefox - 打开设置](/images/guides/browser-config/accessi2p_3.png)

**步骤2。** 在设置搜索栏中搜索 **proxy**，然后点击网络设置旁边的 **Settings...**。

![Firefox - 搜索代理](/images/guides/browser-config/accessi2p_4.png)

**步骤3。** 选择**手动代理配置**，在HTTP代理中输入`127.0.0.1`，端口输入`4444`，然后点击**确定**。

![Firefox - 手动代理配置](/images/guides/browser-config/accessi2p_5.png)

设置代理后，建议进行几项 `about:config` 调整：

- 将 `media.peerConnection.ice.proxy_only` 设置为 **true**（防止 WebRTC 泄露）
- 将 `keyword.enabled` 设置为 **false**（阻止在 .i2p 地址上的搜索引擎重定向）
- 创建一个布尔值 `browser.fixup.domainsuffixwhitelist.i2p` 并设为 **true**（告诉 Firefox `.i2p` 是一个有效的域名后缀）

初学者常遇到的一个问题：在输入 `.i2p` 地址时，一定要在前面加上 `http://`。大多数 I2P 网站不使用 HTTPS（因为 I2P 本身已经对所有流量进行了端到端加密），如果没有这个前缀，Firefox 会将你重定向到搜索引擎。

### Chrome / Edge（Windows）

注意：Chrome 和 Edge 使用您操作系统的代理设置，这会影响系统上的**所有**应用程序。

**步骤1。** 打开Chrome菜单，然后点击**设置**。

![Chrome - 打开设置](/images/guides/browser-config/accessi2p_6.png)

**步骤 2。** 搜索 **proxy**，然后点击 **打开计算机的代理设置**。

![Chrome - 搜索代理](/images/guides/browser-config/accessi2p_7.png)

**步骤3。** 在**手动代理设置**下，点击“使用代理服务器”旁边的**设置**。

![Windows - 代理设置](/images/guides/browser-config/accessi2p_8.png)

**步骤4。** 将 **使用代理服务器** 切换为开启状态，代理IP地址输入 `127.0.0.1`，端口输入 `4444`，然后点击 **保存**。

![Windows - 编辑代理服务器](/images/guides/browser-config/accessi2p_9.png)

### Safari（macOS）

**步骤1。** 导航至 **Safari → 设置 → 高级**，然后点击代理旁边的 **更改设置...**。

![Safari - 高级设置](/images/guides/browser-config/accessi2p_1.png)

**步骤 2。** 启用 **Web 代理 (HTTP)**，服务器输入 `127.0.0.1`，端口输入 `4444`，然后点击 **确定**。

![macOS - Web 代理设置](/images/guides/browser-config/accessi2p_2.png)

---

## 理解路由器控制台仪表板

位于 `127.0.0.1:7657` 的路由器控制台会显示多个关键指标，用于反映你的节点运行状况。**侧边栏**会显示你的 I2P 版本、运行时间、带宽使用情况（上传/下载）、活跃对等节点数量以及隧道状态。当“共享客户端”变为绿色时，表示你的路由器已成功接入网络并准备就绪。

![路由器控制台 - 共享客户端 绿色](/images/guides/quickstart/shared-clients-green.png)

**带宽图表** 显示实时吞吐量。默认值较为保守——**下行 96 KBps，上行 40 KBps**，且仅有 48 KBps 用于共享；官方文档强烈建议提高这些限制。请前往 `http://127.0.0.1:7657/config`（或在控制台中点击“配置带宽”）以提升你的带宽上限。更高的共享带宽不仅能改善你自身的网络性能，也有助于提升整个网络的健康状况。若将共享带宽设置为低于 **12 KBps**，你的路由器将进入“隐藏模式”，无法参与网络流量转发。当共享带宽达到 **128 KBps 或更高** 时，你的路由器可能被提升为 floodfill 节点，这意味着它将协助维护分布式哈希表（DHT）。

![带宽配置](/images/guides/quickstart/bandwidth-config.png)

**隧道状态**部分显示了您正在为他人中继的参与隧道。默认情况下，超过90%的I2P路由器会中继参与流量。这既为您自身的匿名性提供了掩护流量，也是您对网络的贡献。隧道每10分钟过期一次，并会自动重建。

![I2PTunnel Manager](/images/guides/quickstart/tunnel-manager.png)

在 `http://127.0.0.1:7657/i2ptunnel/` 的 **I2PTunnel 管理器** 中，可以看到所有已配置的隧道——HTTP 代理、IRC、电子邮件以及您的 eepsite 服务器隧道在开箱时均已预先配置好。

![I2PTunnel 列表](/images/guides/quickstart/i2ptunnel-list.png)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Console page</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">URL</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Home / Status</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/home</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Dashboard with peers, bandwidth, tunnels</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Bandwidth config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/config</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Adjust speed limits and share percentage</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Network config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/confignet</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Firewall, port, and reachability settings</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Tunnel manager</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2ptunnel/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage all I2P tunnels and hidden services</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">I2PSnark</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2psnark/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in BitTorrent client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">SusiMail</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/susimail/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in email client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Address book</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/dns</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage .i2p hostname mappings</td>
</tr>
</tbody>
</table>
---

## 连接后你可以做的五件事

### 浏览 .i2p 网站

I2P 最直接的用途是浏览隐藏网站。将你的浏览器通过 4444 端口代理后，即可访问任何 `.i2p` 地址。有几个知名的站点可作为良好的起点：**`i2p-projekt.i2p`** 是官方 I2P 项目在网内的镜像站点，**`i2pforum.i2p`** 是社区支持论坛，**`stats.i2p`** 提供网络统计信息和地址注册服务，而 **`notbob.i2p`** 则跟踪已知 eepsite 的在线时间，让你了解哪些站点真正处于运行状态。当你遇到未知的 `.i2p` 地址时，代理会提供“跳转服务”链接来解析该主机名——点击这些链接可将新站点添加到你的本地地址簿中。

I2P 还包含一个默认的 **出站代理**（`exit.stormycloud.i2p`），可让你通过 I2P 访问常规互联网，但这并非该网络的主要用途，且性能会较慢。I2P 的设计初衷是一个内部暗网（darknet），而非像 Tor 那样的出口节点网络。

### 使用 I2PSnark 匿名下载种子文件

**I2PSnark** 是一个功能完整的 BitTorrent 客户端，内置于每个 I2P 安装中，可通过 `http://127.0.0.1:7657/i2psnark/` 访问。它完全在 I2P 网络内部运行——无法连接到 clearnet torrents，且 clearnet 用户无法看到 I2P torrents。其网页界面支持 magnet links、DHT、拖放操作、torrent 搜索、顺序下载以及 UDP trackers（自版本 2.10.0 起支持）。默认 tunnel 长度为三个 hops。只需通过界面添加 `.torrent` 文件或 magnet links 即可。

![I2PSnark 界面](/images/guides/quickstart/i2psnark-interface.png)

要查找种子文件，请访问 **Postman Tracker**：`http://tracker2.postman.i2p/` —— 这是一个集中式中心，用户可在其中搜索并下载由 I2P 网络内其他用户上传的种子文件。你也可以上传自己的种子文件，与社区共享。

![Postman Tracker](/images/guides/quickstart/postman-tracker.png)

其他兼容 I2P 的种子客户端包括 BiglyBT 和带有 I2P 插件的 qBittorrent。

### 使用 SusiMail 发送加密邮件

**SusiMail** 位于 `http://127.0.0.1:7657/susimail/`，是一个基于网页的电子邮件客户端，旨在避免泄露身份信息。它连接到由“postman”运营的 **`mail.i2p`** 邮件服务器。要开始使用，请先在 **`hq.postman.i2p`**（可通过您的 I2P 代理访问）注册一个账户，然后使用该账户凭据在 SusiMail 中登录。预配置的 I2PTunnel 条目将 SMTP 流量路由至 `localhost:7659`，POP3 流量路由至 `localhost:7660`。您既可以向其他 `@mail.i2p` 用户发送邮件，也可以发送至常规互联网邮箱地址（通过邮件服务器的出站代理转发）。SusiMail 支持 Markdown 格式、拖放附件以及 HTML 邮件。

![SusiMail 收件箱](/images/guides/quickstart/susimail-login.png)

![SusiMail 写邮件](/images/guides/quickstart/susimail-inbox.png)

### 通过 Irc2P 网络在 IRC 上聊天

I2P 预配置了一个位于 `localhost:6668` 的 **IRC 隧道**。将任意 IRC 客户端指向此地址（**禁用** SSL/TLS —— 加密由 I2P 自行处理），即可连接到 Irc2P 网络，该网络由多个服务器组成，包括 `irc.postman.i2p`、`irc.echelon.i2p` 和 `irc.dg.i2p`。主要频道包括用于一般讨论的 **`#i2p`**、用于开发的 **`#i2p-dev`** 以及用于技术支持的 **`#i2p-help`**。IRC 隧道会自动剥离连接中的识别信息。推荐使用的客户端包括 WeeChat、Pidgin 和 Thunderbird Chat。

### 托管您自己的匿名网站

每个 I2P 安装实例都包含一个已在 `localhost:7658` 上运行的 **Jetty 网页服务器**，并配有相应的 I2P 服务器隧道。要发布网站，只需将 HTML 文件放入文档根目录：Linux 系统为 `~/.i2p/eepsite/docroot`，Windows 系统为 `%LOCALAPPDATA%\I2P\I2P Site\docroot`。你的网站将自动获得一个加密的 Base64 目标地址以及一个较短的 `xxxxx.b32.i2p` 地址。若要获得类似 `mysite.i2p` 这样便于记忆的域名，可在 `stats.i2p` 或 `no.i2p` 等地址簿服务中进行注册。对于更高级的配置，你也可以用 Apache 或 Nginx 替代 Jetty，并通过 I2PTunnel 服务器隧道提供服务——只需记得移除可能泄露身份的服务器头部信息。详细操作指南，请参阅我们的 [创建 I2P Eepsite](/docs/guides/creating-an-eepsite/) 教程。

---

## 新用户必备的安全实践

**切勿在同一浏览器配置文件中同时浏览 I2P 和明网。** 这是最重要的安全准则。请通过 `about:profiles` 创建一个专用的 Firefox 配置文件，或使用 Easy Install Bundle 中预配置的配置文件。在匿名浏览和实名浏览之间发生 cookie、历史记录和缓存数据的交叉污染，是最常见的操作安全失误。

官方的 **"I2P in Private Browsing"** Firefox 扩展（可从 Mozilla 附加组件商店获取）通过创建启用反指纹识别、第一方隔离和信封式布局（letterboxing）的隔离容器标签页，自动完成大部分配置。对于 Chromium 用户，请使用以下独立参数启动：`--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`。

---

---
title: "在 macOS 上安装 I2P"
description: "在 macOS 上手动安装 I2P 及其依赖项的分步指南"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## 您需要准备的东西

- 运行 macOS 10.14 (Mojave) 或更高版本的 Mac
- 安装应用程序的管理员权限
- 大约 15-20 分钟的时间
- 用于下载安装程序的互联网连接

## 概述

此安装过程有四个主要步骤：

1. **安装 Java** - 下载并安装 Oracle Java 运行时环境
2. **安装 I2P** - 下载并运行 I2P 安装程序
3. **配置 I2P 应用** - 设置启动器并添加到您的程序坞
4. **配置 I2P 带宽** - 运行设置向导来优化您的连接

## 第一部分：安装 Java

I2P 需要 Java 才能运行。如果您已经安装了 Java 8 或更高版本，您可以[跳到第二部分](#part-two-download-and-install-i2p)。

### 步骤 1：下载 Java

访问 [Oracle Java 下载页面](https://www.oracle.com/java/technologies/downloads/) 并下载适用于 macOS 的 Java 8 或更高版本的安装程序。

![为 macOS 下载 Oracle Java](/images/guides/macos-install/0-jre.png)

### 步骤 2：运行安装程序

在下载文件夹中找到下载的 `.dmg` 文件，双击打开它。

![打开Java安装程序](/images/guides/macos-install/1-jre.png)

### 步骤3：允许安装

macOS 可能会显示安全提示，因为安装程序来自已识别的开发者。点击**打开**继续。

![授予安装程序继续进行的权限](/images/guides/macos-install/2-jre.png)

### 第四步：安装 Java

点击 **Install** 开始 Java 安装过程。

![开始安装 Java](/images/guides/macos-install/3-jre.png)

### 步骤5：等待安装

安装程序将复制文件并在您的系统上配置 Java。这通常需要 1-2 分钟。

![等待安装程序完成](/images/guides/macos-install/4-jre.png)

### 步骤6：安装完成

当您看到成功消息时，Java 已安装完成！点击 **关闭** 以完成安装。

![Java installation complete](/images/guides/macos-install/5-jre.png)

## 第二部分：下载和安装 I2P

现在Java已经安装好了，您可以安装I2P router了。

### 步骤 1：下载 I2P

访问[下载页面](/downloads/)并下载**I2P for Unix/Linux/BSD/Solaris**安装程序（`.jar`文件）。

![下载 I2P 安装程序](/images/guides/macos-install/0-i2p.png)

### 步骤 2：运行安装程序

双击下载的 `i2pinstall_X.X.X.jar` 文件。安装程序将启动并要求您选择首选语言。

![选择您的语言](/images/guides/macos-install/1-i2p.png)

### 步骤 3：欢迎界面

阅读欢迎信息并点击**下一步**继续。

![安装程序介绍](/images/guides/macos-install/2-i2p.png)

### 第4步：重要提示

安装程序将显示关于更新的重要提示。I2P 更新是**端到端签名**并经过验证的，尽管安装程序本身是未签名的。点击**下一步**。

![关于更新的重要通知](/images/guides/macos-install/3-i2p.png)

### 步骤 5：许可协议

阅读 I2P 许可协议（BSD 风格许可证）。点击 **Next** 接受。

![许可协议](/images/guides/macos-install/4-i2p.png)

### 步骤 6：选择安装目录

选择I2P的安装位置。推荐使用默认位置（`/Applications/i2p`）。点击**下一步**。

![选择安装目录](/images/guides/macos-install/5-i2p.png)

### 步骤 7：选择组件

保持所有组件处于选中状态以进行完整安装。点击**下一步**。

![选择要安装的组件](/images/guides/macos-install/6-i2p.png)

### 第8步：开始安装

检查您的选择并点击 **Next** 开始安装 I2P。

![开始安装](/images/guides/macos-install/7-i2p.png)

### 步骤 9：安装文件

安装程序将把 I2P 文件复制到您的系统中。这大约需要 1-2 分钟。

![安装进行中](/images/guides/macos-install/8-i2p.png)

### 步骤 10：生成启动脚本

安装程序会创建用于启动 I2P 的启动脚本。

![生成启动脚本](/images/guides/macos-install/9-i2p.png)

### 步骤 11：安装快捷方式

安装程序会提供创建桌面快捷方式和菜单项的选项。请做出选择并点击**下一步**。

![Create shortcuts](/images/guides/macos-install/10-i2p.png)

### 步骤 12：安装完成

成功！I2P 现已安装完成。点击 **完成** 来结束安装。

![安装完成](/images/guides/macos-install/11-i2p.png)

## 第三部分：配置 I2P 应用程序

现在让我们将 I2P 添加到应用程序文件夹和程序坞中，以便轻松启动。

### 步骤 1：打开应用程序文件夹

打开 Finder 并导航到您的 **Applications** 文件夹。

![打开应用程序文件夹](/images/guides/macos-install/0-conf.png)

### 步骤 2：找到 I2P Launcher

在 `/Applications/i2p/` 中寻找 **I2P** 文件夹或 **Start I2P Router** 应用程序。

![找到 I2P 启动器](/images/guides/macos-install/1-conf.png)

### 步骤 3：添加到程序坞

将 **Start I2P Router** 应用程序拖拽到您的 Dock 栏以便快速访问。您也可以在桌面上创建别名。

![将 I2P 添加到程序坞](/images/guides/macos-install/2-conf.png)

**提示**：右键点击 Dock 中的 I2P 图标，选择**选项 → 在 Dock 中保留**以使其永久保留。

## 第四部分：配置 I2P 带宽

当您首次启动I2P时，您将运行一个设置向导来配置您的带宽设置。这有助于为您的连接优化I2P的性能。

### 步骤1：启动I2P

点击 Dock 中的 I2P 图标（或双击启动器）。您的默认网络浏览器将打开 I2P Router Console。

![I2P Router Console welcome screen](/images/guides/macos-install/0-wiz.png)

### 步骤 2：欢迎向导

设置向导将迎接您。点击 **下一步** 开始配置 I2P。

![设置向导介绍](/images/guides/macos-install/1-wiz.png)

### 步骤 3：语言和主题

选择您偏好的**界面语言**并在**浅色**或**深色**主题之间进行选择。点击**下一步**。

![选择语言和主题](/images/guides/macos-install/2-wiz.png)

### 步骤4：带宽测试信息

向导将说明带宽测试。此测试连接到 **M-Lab** 服务来测量您的网络速度。点击 **下一步** 继续。

![带宽测试说明](/images/guides/macos-install/3-wiz.png)

### 步骤 5：运行带宽测试

点击**运行测试**来测量您的上传和下载速度。测试大约需要30-60秒。

![运行带宽测试](/images/guides/macos-install/4-wiz.png)

### 步骤 6：测试结果

查看您的测试结果。I2P 将根据您的连接速度推荐带宽设置。

![带宽测试结果](/images/guides/macos-install/5-wiz.png)

### 步骤7：配置带宽共享

选择您希望与 I2P 网络共享多少带宽：

- **自动**（推荐）：I2P 根据您的使用情况管理带宽
- **限制**：设置特定的上传/下载限制
- **无限制**：尽可能多地共享（适用于快速连接）

点击 **下一步** 保存你的设置。

![配置带宽共享](/images/guides/macos-install/6-wiz.png)

### 步骤 8：配置完成

您的 I2P router 现已配置完成并正在运行！router 控制台将显示您的连接状态，并允许您浏览 I2P 站点。

## I2P 入门指南

现在 I2P 已安装并配置完成，您可以：

1. **浏览 I2P 站点**：访问 `http://127.0.0.1:7657/home` 查看热门 I2P 服务的链接
2. **配置您的浏览器**：设置一个[浏览器配置文件](/docs/guides/browser-config)来访问 `.i2p` 站点
3. **探索服务**：体验 I2P 邮件、论坛、文件分享等更多服务
4. **监控您的 router**：`http://127.0.0.1:7657/console`显示您的网络状态和统计信息

### 有用链接

- **Router Console**: `http://127.0.0.1:7657/`
- **配置**: `http://127.0.0.1:7657/config`
- **地址簿**: `http://127.0.0.1:7657/susidns/addressbook`
- **带宽设置**: `http://127.0.0.1:7657/config`

## 重新运行设置向导

如果您想要更改带宽设置或稍后重新配置 I2P，您可以从 Router Console 重新运行欢迎向导：

1. 前往 `http://127.0.0.1:7657/welcome`
2. 再次按照向导步骤操作

## 故障排除

### I2P 无法启动

- **检查 Java**：在终端中运行 `java -version` 确保已安装 Java
- **检查权限**：确保 I2P 文件夹具有正确的权限
- **检查日志**：查看 `~/.i2p/wrapper.log` 中的错误消息

### 浏览器无法访问I2P网站

- 确保 I2P 正在运行（检查 Router Console）
- 配置浏览器的代理设置使用 HTTP 代理 `127.0.0.1:4444`
- 启动后等待 5-10 分钟让 I2P 融入网络

### 性能缓慢

- 重新运行带宽测试并调整您的设置
- 确保您与网络共享一些带宽
- 在 Router Console 中检查您的连接状态

## 卸载 I2P

要从您的 Mac 上卸载 I2P：

1. 如果 I2P router 正在运行，请退出它
2. 删除 `/Applications/i2p` 文件夹
3. 删除 `~/.i2p` 文件夹（你的 I2P 配置和数据）
4. 从你的 Dock 中移除 I2P 图标

## 下一步

- **加入社区**：访问 [i2pforum.net](http://i2pforum.net) 或在 Reddit 上查看 I2P 相关内容
- **了解更多**：阅读 [I2P 文档](/en/docs) 来理解网络的工作原理
- **参与其中**：考虑[为 I2P 贡献力量](/en/get-involved)，参与开发或运行基础设施

恭喜！您现在已经成为 I2P 网络的一部分。欢迎来到隐形互联网！

---

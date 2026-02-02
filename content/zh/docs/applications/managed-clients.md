---
title: "托管客户端"
description: "router 管理的应用程序如何与 ClientAppManager 和端口映射器集成"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## 概述

当客户端在 [clients.config](/docs/specs/configuration/) 文件中列出时，可以由 router 直接启动。这些客户端可能是"托管的"或"非托管的"。这由 ClientAppManager 处理。此外，托管或非托管客户端可以向 ClientAppManager 注册，以便其他客户端可以获取对它们的引用。还有一个简单的端口映射器工具，供客户端注册内部端口，其他客户端可以查找这些端口。

---

## 托管客户端

从 0.9.4 版本开始，router 支持托管客户端。托管客户端由 ClientAppManager 实例化并启动。ClientAppManager 维护对客户端的引用并接收客户端状态更新。托管客户端是首选方式，因为它更容易实现状态跟踪以及启动和停止客户端。它也更容易避免在客户端代码中使用静态引用，这可能导致客户端停止后出现过度内存使用。托管客户端可以由用户在 router 控制台中启动和停止，并在 router 关闭时停止。

托管客户端实现 net.i2p.app.ClientApp 或 net.i2p.router.app.RouterApp 接口。实现 ClientApp 接口的客户端必须提供以下构造函数：

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
实现RouterApp接口的客户端必须提供以下构造函数：

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
提供的参数在 clients.config 文件中指定。

---

## 非托管客户端

如果在 clients.config 文件中指定的主类没有实现托管接口，它将通过 main() 方法使用指定的参数启动，并通过 main() 方法使用指定的参数停止。router 不会维护引用，因为所有交互都通过静态 main() 方法进行。控制台无法向用户提供准确的状态信息。

---

## 已注册客户端

客户端，无论是托管还是非托管的，都可以向 ClientAppManager 注册，以便其他客户端能够获取对它们的引用。注册是通过名称进行的。已知的注册客户端包括：

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## 端口映射器

router还提供了一个简单的机制，让客户端能够找到内部套接字服务，比如HTTP代理。这是通过端口映射器(Port Mapper)提供的。注册是按名称进行的。注册的客户端通常在该端口上提供一个内部模拟套接字。

---
title: "加密的 LeaseSet"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Rejected"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## 概述

该提案是关于重新设计 LeaseSet 加密机制的。


## 动机

当前的加密 LS 是非常糟糕和不安全的。我可以这么说，因为我设计并实现了它。

原因：

- 使用 AES CBC 加密
- 所有人共用一个 AES 密钥
- 租约过期仍然暴露
- 加密公钥仍然暴露


## 设计

### 目标

- 使整个过程变得透明
- 为每个接收者使用不同的密钥


### 策略

像 GPG/OpenPGP 一样。为每个接收者使用非对称加密对称密钥。数据使用该非对称密钥解密。参见例如 [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1) 如果我们可以找到一个小巧且快速的算法。

问题在于找到一个小巧且快速的非对称加密算法。ElGamal 算法需要 514 字节，这有点痛苦。我们可以做得更好。

参见例如 http://security.stackexchange.com/questions/824...

这种方法适用于少数接收者（或者说，密钥；你仍然可以将密钥分发给多个人）.


## 规范

- 目的地
- 发布时间戳
- 过期时间
- 标志
- 数据长度
- 加密数据
- 签名

加密数据可以在前面加上某种 enctype 指定符，或者不加.


## 参考文献

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)

---
title: "引导者过期"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "已关闭"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## 概述

本提案旨在提高引入（introduction）的成功率。


## 动机

引入者（introducer）会在一定时间后过期，但该信息并未在路由器信息（Router Info）中公布。目前路由器必须使用启发式方法来估计某个引入者是否已失效。


## 设计

在包含引入者的 SSU 路由器地址（Router Address）中，发布者可选择性地为每个引入者包含过期时间。


## 规范

```
iexp{X}={nnnnnnnnnn}

X :: 引入者编号 (0-2)

nnnnnnnnnn :: 自纪元以来的秒数（非毫秒）。
```

### 说明

* 每个过期时间必须大于路由器信息（Router Info）的发布日期，且不超过发布日期之后的6小时。

* 发布路由器和引入者应尽量保证引入者在过期前有效，但无法保证这一点。

* 路由器不应在引入者过期后继续使用该引入者。

* 引入者过期时间位于路由器地址（Router Address）的映射中，而非路由器地址中当前未使用的8字节过期字段。

**示例：** `iexp0=1486309470`


## 迁移

无问题。实现为可选。
向后兼容性有保障，因为旧版路由器会忽略未知参数。


## 参考资料

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)

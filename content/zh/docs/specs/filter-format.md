---
title: "访问过滤器格式"
description: "tunnel 访问控制过滤器文件的语法"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## 概述

过滤器的定义是一个字符串列表。空行和以`#`开头的行会被忽略。过滤器定义的更改在tunnel重启后生效。

每一行可以表示以下项目之一：

- 定义一个默认阈值，应用于未在此文件或任何引用文件中列出的远程目的地
- 定义应用于特定远程目的地的阈值
- 定义应用于文件中列出的远程目的地的阈值
- 定义一个阈值，如果被违反，将导致违规的远程目的地被记录到指定文件中

定义的顺序很重要。给定目标的第一个阈值（无论是显式的还是在文件中列出的）会覆盖该目标的任何后续阈值，无论是显式的还是在文件中列出的。

## 阈值

阈值由远程目标在指定秒数内允许执行的连接尝试次数定义，超过此次数将发生"违反"。例如，以下阈值定义 `15/5` 意味着同一个远程目标允许在 5 秒时间段内进行 14 次连接尝试。如果它在同一时间段内再尝试一次，阈值将被违反。

阈值格式可以是以下之一：

- **数字定义** 在指定秒数内的连接数量 - `15/5`、`30/60` 等等。请注意，如果连接数为 1（例如 `1/1`），第一次连接尝试就会导致阈值突破。
- 单词 **`allow`**。此阈值永远不会被突破，即允许无限次连接尝试。
- 单词 **`deny`**。此阈值总是被突破，即不允许任何连接尝试。

### 默认阈值

默认阈值适用于任何未在定义中或任何引用文件中明确列出的远程目标。要设置默认阈值，请使用关键字 `default`。以下是默认阈值的示例：

```text
15/5 default
allow default
deny default
```
每个过滤器只能有一个默认阈值定义。如果省略了该定义，过滤器将默认允许未知连接。

### 显式阈值

显式阈值应用于定义本身中列出的远程目标。示例：

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### 批量阈值

为了方便起见，可以在文件中维护一个目标列表，并批量为所有目标定义阈值。示例：

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
这些文件可以在 tunnel 运行时手动编辑。对这些文件的更改可能需要最多 10 秒才能生效。

## 记录器

Recorder 会跟踪远程目标发起的连接尝试，如果超过某个阈值，该目标就会被记录到指定文件中。示例：

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
可以使用记录器将激进的目标记录到指定文件中，然后使用同一文件来限制它们。例如，以下代码片段将定义一个过滤器，该过滤器最初允许所有连接尝试，但如果任何单个目标在5秒内超过30次尝试，就会被限制为每5秒15次尝试：

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
可以在一个 tunnel 中使用记录器写入文件，该文件可以限制另一个 tunnel 的流量。可以在多个 tunnel 中重复使用同一个文件的目标地址。当然，也可以手动编辑这些文件。

以下是一个过滤器定义示例，它默认应用一些限流，对 `friends.txt` 文件中的目标地址不进行限流，禁止 `enemies.txt` 文件中目标地址的任何连接，并将任何攻击性行为记录在名为 `suspicious.txt` 的文件中：

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```
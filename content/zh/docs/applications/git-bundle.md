---
title: "使用 git bundle 获取 I2P 源代码"
description: "使用 git bundles 和 BitTorrent 通过 I2P 克隆大型仓库"
slug: "git-bundle"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

通过 I2P 克隆大型软件仓库可能会很困难，使用 git 有时会让这变得更加困难。幸运的是，它有时也能让事情变得更容易。Git 有一个 `git bundle` 命令，可以用来将 git 仓库转换为一个文件，然后 git 可以从本地磁盘上的位置克隆、获取或导入该文件。通过将这种功能与 bittorrent 下载相结合，我们可以解决 `git clone` 的剩余问题。

---

## 开始之前

如果您打算生成一个 git bundle，您**必须**已经拥有完整的 **git** 仓库副本，而不是 mtn 仓库。您可以从 github 或 git.idk.i2p 获取，但浅克隆（使用 --depth=1 完成的克隆）*无法工作*。它会静默失败，创建看起来像 bundle 的文件，但当您尝试克隆它时会失败。如果您只是检索预生成的 git bundle，那么本节不适用于您。

---

## 通过 Bittorrent 获取 I2P 源代码

需要有人向您提供一个torrent文件或磁力链接，对应于他们已经为您生成的现有`git bundle`。截至2020年3月18日星期三的主线i2p.i2p源代码的最新正确生成bundle可以在I2P内我的pastebin [paste.idk.i2p/f/4hq37i](http://paste.idk.i2p/f/4h137i) 中找到。

一旦您有了bundle文件，您需要使用git从中创建一个工作仓库。如果您使用的是GNU/Linux和i2psnark，git bundle应该位于$HOME/.i2p/i2psnark，或者如果在Debian上作为服务运行，则位于/var/lib/i2p/i2p-config/i2psnark。如果您在GNU/Linux上使用BiglyBT，它可能位于"$HOME/BiglyBT Downloads/"。这里的示例假设在GNU/Linux上使用I2PSnark，如果您使用其他软件，请将bundle的路径替换为您的客户端和平台首选的下载目录。

### 使用 `git clone`

从 git bundle 克隆很简单，只需：

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
如果你遇到以下错误，请尝试手动使用 git init 和 git fetch。

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### 使用 `git init` 和 `git fetch`

首先，创建一个 i2p.i2p 目录以转换为 git 仓库。

```
mkdir i2p.i2p && cd i2p.i2p
```
接下来，初始化一个空的 git 仓库来获取更改。

```
git init
```
最后，从捆绑包中获取仓库。

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### 将捆绑包远程仓库替换为上游远程仓库

现在您有了一个 bundle，您可以通过将远程设置为上游仓库源来跟上更新。

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## 生成Bundle

首先，按照[用户Git指南](/docs/applications/git/)操作，直到成功对i2p.i2p仓库进行了`--unshallow`克隆。如果你已经有一个克隆，请确保在生成torrent包之前运行`git fetch --unshallow`。

一旦你有了这些，只需运行相应的 ant 目标：

```
ant git-bundle
```
并将生成的包复制到您的 I2PSnark 下载目录中。例如：

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
一两分钟后，I2PSnark 会检测到该种子文件。点击"开始"按钮开始做种。

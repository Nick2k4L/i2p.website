---
title: "git bundle을 사용하여 I2P 소스 코드 가져오기"
description: "git bundle과 BitTorrent를 사용하여 I2P를 통해 대용량 저장소 복제하기"
slug: "git-bundle"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

I2P를 통해 대용량 소프트웨어 저장소를 복제하는 것은 어려울 수 있으며, git을 사용하면 때때로 이를 더 어렵게 만들 수 있습니다. 다행히도, git이 때로는 이를 더 쉽게 만들어주기도 합니다. Git에는 `git bundle` 명령이 있는데, 이는 git 저장소를 파일로 변환하여 git이 로컬 디스크의 위치에서 해당 파일을 복제, 가져오기, 또는 임포트할 수 있게 해줍니다. 이 기능을 bittorrent 다운로드와 결합하면, `git clone`의 남은 문제들을 해결할 수 있습니다.

---

## 시작하기 전에

git bundle을 생성하려는 경우, mtn repository가 아닌 **git** repository의 전체 사본을 **반드시** 미리 보유하고 있어야 합니다. github나 git.idk.i2p에서 가져올 수 있지만, shallow clone(--depth=1로 수행된 clone)은 *작동하지 않습니다*. 조용히 실패하여 bundle처럼 보이는 것을 생성하지만, clone을 시도하면 실패할 것입니다. 미리 생성된 git bundle을 단순히 가져오는 경우라면, 이 섹션은 해당되지 않습니다.

---

## Bittorrent를 통한 I2P 소스 코드 가져오기

누군가가 이미 당신을 위해 생성한 기존 `git bundle`에 해당하는 torrent 파일이나 magnet 링크를 제공해야 합니다. 2020년 3월 18일 수요일 기준으로 mainline i2p.i2p 소스 코드의 최근에 올바르게 생성된 bundle은 제 pastebin paste.idk.i2p/f/4hq37i에서 I2P 내에서 찾을 수 있습니다.

bundle을 받으면 git을 사용하여 작업 저장소를 생성해야 합니다. GNU/Linux에서 i2psnark를 사용하는 경우, git bundle은 $HOME/.i2p/i2psnark에 있거나 Debian에서 서비스로 실행 중인 경우 /var/lib/i2p/i2p-config/i2psnark에 있을 것입니다. GNU/Linux에서 BiglyBT를 사용하는 경우에는 "$HOME/BiglyBT Downloads/" 경로에 있을 것입니다. 여기의 예시들은 GNU/Linux에서 I2PSnark를 사용한다고 가정합니다. 다른 것을 사용한다면 bundle 경로를 사용하는 클라이언트와 플랫폼에서 선호하는 다운로드 디렉터리로 바꾸세요.

### `git clone` 사용하기

git bundle에서 복제하는 것은 간단합니다:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
다음과 같은 오류가 발생하면 대신 git init과 git fetch를 수동으로 사용해 보세요.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### `git init`과 `git fetch` 사용하기

먼저 git 저장소로 만들 i2p.i2p 디렉터리를 생성합니다.

```
mkdir i2p.i2p && cd i2p.i2p
```
다음으로, 변경사항을 다시 가져올 빈 git 저장소를 초기화합니다.

```
git init
```
마지막으로 번들에서 저장소를 가져옵니다.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### bundle 원격을 upstream 원격으로 교체

이제 번들이 있으므로 원격 저장소를 업스트림 리포지토리 소스로 설정하여 변경 사항을 계속 추적할 수 있습니다.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## 번들 생성하기

먼저, i2p.i2p 저장소를 성공적으로 `--unshallow`된 클론을 가질 때까지 [사용자를 위한 Git 가이드](/docs/applications/git/)를 따르세요. 이미 클론이 있다면, torrent 번들을 생성하기 전에 `git fetch --unshallow`를 실행해야 합니다.

이를 준비했다면, 해당하는 ant 타겟을 실행하기만 하면 됩니다:

```
ant git-bundle
```
그리고 생성된 번들을 I2PSnark 다운로드 디렉토리에 복사합니다. 예를 들어:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
1-2분 후 I2PSnark가 토렌트를 인식할 것입니다. "Start" 버튼을 클릭하여 토렌트 시딩을 시작하세요.

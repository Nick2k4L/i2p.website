---
title: "I2P 사용 시작하기: 완전 초보자를 위한 종합 안내서"
description: "I2P 사용 시작하기: 완전 초보자를 위한 종합 안내서"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P는 인터넷 "내부"에서 실행되는 완전히 암호화된 피어 투 피어 익명 네트워크이며**, i2p.net에서 제공하는 자바 구현체가 이를 사용하는 대표적인 방법으로 남아 있습니다. 일반 웹에 대한 접근을 익명화하는 데 주로 사용되는 Tor와 달리, I2P는 익명 웹사이트(eepsite), 이메일, 채팅, 파일 공유 등이 가능한 완전히 독립된 은닉 서비스 네트워크를 구축합니다.

---

## I2P를 시작하는 순간에 발생하는 일

설치 후, I2P는 `http://127.0.0.1:7657`에서 **router console**이라는 로컬 웹 애플리케이션을 실행합니다. 이곳은 사용자의 명령 센터로서, 전적으로 사용자의 기기에서 실행되며 보안을 위해 localhost에 연결되어 있습니다. 처음 실행 시 **setup wizard**가 언어 선택, 테마 선택(다크 또는 라이트), 외부 M-Lab 측정 서비스를 사용하는 약 1분 정도 소요되는 자동 대역폭 테스트를 안내합니다. 이후 네트워크와 공유할 대역폭의 비율을 설정하게 됩니다.

![I2P 설치 마법사 - 언어 선택](/images/guides/quickstart/wizard-language-selection.webp)

마법사가 완료되면 라우터는 "재시딩(reseeding)"이라고 불리는 **부트스트래핑(bootstrapping)** 과정을 시작합니다. 라우터는 HTTPS를 통해 하드코딩된 리시드(reseed) 서버로부터 약 **100개의 RouterInfo 레코드**를 다운로드하여 초기 피어 목록을 확보합니다. 이후, 더 많은 피어를 발견하고 로컬 네트워크 데이터베이스(이른바 "netDb")를 채우기 위해 **탐사용 터널(exploratory tunnels)** 을 구성하기 시작합니다. 처음 몇 분 동안 "터널 거부 중: 시작 중(rejecting tunnels: starting up)"이라는 메시지가 표시되는데, 이는 정상적인 현상입니다.

![I2P 리시딩 - 부트스트래핑](/images/guides/quickstart/reseed-bootstrapping.webp)

**라우터를 사용할 수 있게 되기 전까지 3~10분 정도 기다려야 하며**, 최상의 성능에 도달하려면 그보다 훨씬 더 오랜 시간—연속 가동 상태로 며칠 정도—가 필요합니다. 라우터 콘솔 사이드바에는 "활성 x/y" 형태로 피어 수가 표시되며, 여기서 x는 최근에 메시지를 주고받은 피어 수이고 y는 전체에서 확인된 피어 수입니다. **활성 피어가 10명 이상** 보일 때, 라우터는 건강하게 연결된 상태입니다. 신규 사용자가 할 수 있는 가장 중요한 일은 **라우터를 계속 실행 상태로 두는 것**입니다. 종료 후에는 다른 노드들이 최소 24시간 동안 귀하의 라우터를 신뢰할 수 없는 것으로 간주하므로, 자주 재시작하면 성능이 크게 저하됩니다.

![I2P 라우터 콘솔 대시보드](/images/guides/quickstart/router-console-dashboard.png)

---

## I2P용 브라우저 설정하기

Tor 네트워크와 달리 I2P는 전용 브라우저를 제공하지 않습니다. I2P 사이트( `.i2p` 의사 최상위 도메인)에 접속하려면 브라우저의 프록시 설정을 구성하여 트래픽을 포트 **4444**의 I2P HTTP 프록시를 통해 라우팅해야 합니다.

**Windows 사용자에게 가장 쉬운 방법**은 **쉬운 설치 번들(Easy Install Bundle)** 로, 자바(Java), 라우터, "비공개 탐색에서 I2P 사용(I2P in Private Browsing)" 확장 프로그램이 미리 설정된 Firefox 프로필을 함께 제공합니다. 이 방법은 프록시 수동 설정을 모두 생략할 수 있게 해줍니다. 다운로드 후 I2P 사이트 탐색까지 약 4분 정도 소요됩니다. macOS용 쉬운 설치 번들(애플 실리콘)도 베타 버전으로 제공 중입니다. 쉬운 설치 번들을 사용하는 경우 아래의 수동 설정을 건너뛸 수 있습니다.

### Firefox (권장)

Firefox를 강력히 권장합니다. Firefox는 운영 체제와 별개인 자체 프록시 설정을 제공하기 때문입니다. 반면 Chrome과 Edge는 모든 애플리케이션에 영향을 미치는 시스템 전체 프록시 설정을 사용합니다.

**1단계.** Firefox 메뉴(햄버거 아이콘)를 열고 **설정**을 클릭합니다.

![Firefox - 설정 열기](/images/guides/browser-config/accessi2p_3.png)

**2단계.** 설정 검색창에서 **proxy**를 검색한 후, 네트워크 설정 옆의 **설정...**을 클릭합니다.

![Firefox - 프록시 검색](/images/guides/browser-config/accessi2p_4.png)

**3단계.** **수동 프록시 구성**을 선택하고, HTTP 프록시에 `127.0.0.1`을, 포트에 `4444`를 입력한 후 **확인**을 클릭합니다.

![Firefox - 수동 프록시 구성](/images/guides/browser-config/accessi2p_5.png)

프록시 설정 후, 몇 가지 `about:config` 조정을 권장합니다:

- `media.peerConnection.ice.proxy_only`를 **true**로 설정 (WebRTC 유출 방지)
- `keyword.enabled`를 **false**로 설정 (.i2p 주소에서 검색 엔진 리디렉션 중지)
- `browser.fixup.domainsuffixwhitelist.i2p`라는 불리언 값을 생성하고 **true**로 설정 (Firefox에게 `.i2p`가 유효한 도메인 접미사임을 알림)

초보자들이 자주 실수하는 점: 항상 `.i2p` 주소 앞에 `http://`를 입력하세요. 대부분의 I2P 사이트는 HTTPS를 사용하지 않으며(이미 I2P가 모든 트래픽을 종단 간 암호화하기 때문), 접두사 없이 입력하면 Firefox가 검색 엔진으로 리디렉션합니다.

### Chrome / Edge (Windows)

참고: Chrome과 Edge는 운영체제의 프록시 설정을 사용하므로 시스템의 **모든** 애플리케이션에 영향을 미칩니다.

**1단계.** Chrome 메뉴를 열고 **설정**을 클릭합니다.

![Chrome - 설정 열기](/images/guides/browser-config/accessi2p_6.png)

**2단계.** **프록시**를 검색한 후, **컴퓨터의 프록시 설정 열기**를 클릭합니다.

![Chrome - 프록시 검색](/images/guides/browser-config/accessi2p_7.png)

**3단계.** **수동 프록시 설정** 아래에서 "프록시 서버 사용" 옆의 **설정**을 클릭합니다.

![Windows - 프록시 설정](/images/guides/browser-config/accessi2p_8.png)

**4단계.** **프록시 서버 사용**을 켜고, 프록시 IP 주소에 `127.0.0.1`, 포트에 `4444`를 입력한 후 **저장**을 클릭하세요.

![Windows - 프록시 서버 편집](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**1단계.** **Safari → 설정 → 고급**으로 이동한 후 프록시 옆의 **설정 변경...**을 클릭합니다.

![Safari - 고급 설정](/images/guides/browser-config/accessi2p_1.png)

**2단계.** **웹 프록시(HTTP)**를 활성화하고, 서버에 `127.0.0.1`, 포트에 `4444`를 입력한 후 **확인**을 클릭합니다.

![macOS - 웹 프록시 설정](/images/guides/browser-config/accessi2p_2.png)

---

## 라우터 콘솔 대시보드 이해하기

`127.0.0.1:7657`에서 실행되는 라우터 콘솔은 노드의 성능 상태를 알려주는 여러 주요 지표를 표시합니다. **사이드바**에는 I2P 버전, 가동 시간, 대역폭 사용량(입력/출력), 활성 피어 수, 터널 상태가 표시됩니다. "공유 클라이언트(Shared Clients)" 항목이 녹색으로 바뀌면 라우터가 통합되어 사용 준비가 된 것입니다.

![라우터 콘솔 - 공유 클라이언트 초록색](/images/guides/quickstart/shared-clients-green.png)

**대역폭 그래프**는 실시간 처리량을 보여줍니다. 기본값은 보수적인 설정으로, 다운로드 **96 KBps**, 업로드 **40 KBps**, 공유 대역폭은 단지 **48 KBps**입니다. 공식 문서에서는 이 값을 높일 것을 강력히 권장합니다. `http://127.0.0.1:7657/config`로 이동하거나(또는 콘솔에서 "Configure Bandwidth" 클릭) 제한 값을 높일 수 있습니다. 더 높은 공유 대역폭은 본인의 성능 향상은 물론 네트워크 전체의 건강에도 기여합니다. 공유 대역폭을 **12 KBps 미만**으로 설정하면 라우터가 "hidden mode"가 되어, 참여형 트래픽에서 사실상 차단됩니다. 반면 **128 KBps 이상**으로 설정하면 라우터가 floodfill 상태로 승격될 수 있으며, 이는 분산 해시 테이블(DHT)의 유지 관리에 기여한다는 의미입니다.

![대역폭 구성](/images/guides/quickstart/bandwidth-config.png)

**터널 상태** 섹션은 타인을 위해 중계하는 트래픽인 참여형 터널을 보여줍니다. I2P 라우터의 90% 이상은 기본적으로 참여형 트래픽을 중계합니다. 이는 당신 자신의 익명성을 위한 커버 트래픽이자 네트워크에 기여하는 방식이기도 합니다. 터널은 매 10분마다 만료되며 자동으로 재구축됩니다.

![I2PTunnel 관리자](/images/guides/quickstart/tunnel-manager.png)

`http://127.0.0.1:7657/i2ptunnel/` 에 있는 **I2PTunnel 관리자**는 구성된 모든 터널을 표시합니다. HTTP 프록시, IRC, 이메일 및 eepsite 서버 터널은 모두 처음 사용 시 미리 구성되어 있습니다.

![I2PTunnel 목록](/images/guides/quickstart/i2ptunnel-list.png)

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

## 연결 후 할 수 있는 다섯 가지 일

### .i2p 웹사이트 탐색

I2P의 가장 직접적인 용도는 숨겨진 웹사이트를 탐색하는 것입니다. 브라우저를 포트 4444를 통해 프록시 설정한 후, 어떤 `.i2p` 주소로든 접속할 수 있습니다. 몇 가지 잘 알려진 사이트는 좋은 출발점이 됩니다: **`i2p-projekt.i2p`**는 네트워크 내부에 미러된 공식 I2P 프로젝트 사이트이며, **`i2pforum.i2p`**는 커뮤니티 지원 포럼을 운영하고 있으며, **`stats.i2p`**는 네트워크 통계와 주소 등록 서비스를 제공하고, **`notbob.i2p`**는 알려진 eepsite들의 가동 시간을 추적하여 실제로 온라인 상태인 사이트를 확인할 수 있게 해줍니다. 알려지지 않은 `.i2p` 주소를 만날 경우, 프록시는 호스트 이름을 해석하는 "점프 서비스(jump service)" 링크를 제공합니다. 이러한 링크를 클릭하면 새 사이트를 로컬 주소록에 추가할 수 있습니다.

I2P는 또한 일반 인터넷에 I2P를 통해 접근할 수 있도록 해주는 기본 **아웃프록시**(`exit.stormycloud.i2p`)를 포함하고 있지만, 이는 네트워크의 주요 목적은 아니며 성능이 느릴 수 있습니다. I2P는 Tor와 같은 익스노드 네트워크가 아니라 내부 다크넷으로 설계되었습니다.

### I2PSnark로 익명으로 토렌트 파일 공유

**I2PSnark**는 모든 I2P 설치에 기본 포함된 완전한 기능의 BitTorrent 클라이언트로, `http://127.0.0.1:7657/i2psnark/` 에서 접근할 수 있습니다. 이 클라이언트는 I2P 네트워크 내에서만 작동하며, 일반 인터넷(클리어넷) 토렌트에는 연결할 수 없고, 클리어넷 사용자도 I2P 토렌트를 볼 수 없습니다. 웹 인터페이스는 마그넷 링크, DHT, 드래그 앤 드롭, 토렌트 검색, 순차적 다운로드, UDP 트래커(버전 2.10.0에서 추가됨)를 지원합니다. 기본 터널 길이는 3홉입니다. 인터페이스를 통해 `.torrent` 파일이나 마그넷 링크를 추가하기만 하면 됩니다.

![I2PSnark 인터페이스](/images/guides/quickstart/i2psnark-interface.png)

토렌트를 찾으려면 I2P 네트워크 내에서 다른 사용자들이 업로드한 토렌트를 검색하고 다운로드할 수 있는 중앙 허브인 **Postman Tracker**(`http://tracker2.postman.i2p/`)를 방문하세요. 또한 자신의 토렌트를 업로드하여 커뮤니티와 공유할 수도 있습니다.

![Postman 트래커](/images/guides/quickstart/postman-tracker.png)

I2P와 호환되는 기타 토렌트 클라이언트로는 I2P 플러그인이 탑재된 BiglyBT와 qBittorrent가 있다.

### SusiMail로 암호화된 이메일 보내기

**SusiMail**은 `http://127.0.0.1:7657/susimail/` 에서 사용할 수 있는 웹 기반 이메일 클라이언트로, 식별 정보 유출을 방지하도록 설계되었습니다. 이 클라이언트는 "postman"이 운영하는 **`mail.i2p`** 메일 서버에 연결됩니다. 사용을 시작하려면 I2P 프록시를 통해 접근 가능한 **`hq.postman.i2p`** 에서 계정을 등록한 후, 해당 자격 증명을 사용해 SusiMail에 로그인하면 됩니다. 사전 설정된 I2PTunnel 항목을 통해 SMTP는 `localhost:7659`, POP3는 `localhost:7660`을 통해 라우팅됩니다. SusiMail을 사용하면 다른 `@mail.i2p` 사용자뿐 아니라 일반 인터넷 이메일 주소로도 이메일을 보낼 수 있습니다(메일 서버의 아웃프록시를 통해 연결됨). SusiMail은 마크다운 형식, 드래그 앤 드롭 첨부 파일, HTML 이메일을 지원합니다.

![SusiMail 받은편지함](/images/guides/quickstart/susimail-login.png)

![SusiMail 작성](/images/guides/quickstart/susimail-inbox.png)

### Irc2P 네트워크를 통해 IRC에서 채팅하기

I2P는 `localhost:6668`에서 **미리 구성된 IRC 터널**을 제공합니다. SSL/TLS을 **비활성화한 상태에서** 이 주소로 어떤 IRC 클라이언트를 연결하면 Irc2P 네트워크에 접속하게 되며, 여기에는 `irc.postman.i2p`, `irc.echelon.i2p`, `irc.dg.i2p` 등의 서버가 포함되어 있습니다. 주요 채널로는 일반 토론을 위한 **`#i2p`**, 개발 관련 논의를 위한 **`#i2p-dev`**, 지원 문의를 위한 **`#i2p-help`** 가 있습니다. IRC 터널은 연결 시 자동으로 신원을 식별할 수 있는 정보를 제거합니다. 추천 클라이언트로는 WeeChat, Pidgin, Thunderbird Chat이 있습니다.

### 자신의 익명 웹사이트를 호스팅하세요

모든 I2P 설치에는 `localhost:7658`에서 이미 실행 중인 **Jetty 웹 서버**와 해당 I2P 서버 튜널이 포함되어 있습니다. 사이트를 게시하려면 Linux의 경우 `~/.i2p/eepsite/docroot`, Windows의 경우 `%LOCALAPPDATA%\I2P\I2P Site\docroot`에 HTML 파일을 넣기만 하면 됩니다. 사이트는 자동으로 암호학적 Base64 목적지와 더 짧은 `xxxxx.b32.i2p` 주소를 부여받습니다. `mysite.i2p`와 같은 사람이 읽기 쉬운 이름을 얻으려면 `stats.i2p` 또는 `no.i2p` 같은 주소록 서비스에 등록하세요. 보다 고급 설정의 경우, I2PTunnel 서버 튜널 뒤에 Jetty 대신 Apache 또는 Nginx를 사용할 수 있습니다. 단, 식별 가능한 서버 헤더를 제거하는 것을 잊지 마세요. 자세한 설명은 [Creating an I2P Eepsite](/docs/guides/creating-an-eepsite/) 가이드를 참조하세요.

---

## 새 사용자를 위한 필수 보안 실천 방법

**절대로 동일한 브라우저 프로필에서 I2P와 일반 인터넷(clearnet)을 동시에 사용하지 마십시오.** 이것이 가장 중요한 보안 규칙입니다. `about:profiles`를 통해 전용 Firefox 프로필을 생성하거나, Easy Install Bundle에 포함된 미리 구성된 프로필을 사용하세요. 익명 상태의 탐색과 신원이 노출된 탐색 사이에서 쿠키, 기록, 캐시 데이터가 혼용되는 것은 가장 흔한 운영 보안 실패 사례입니다.

공식 **"I2P in Private Browsing"** Firefox 확장 프로그램(Mozilla 애드온 저장소에서 제공)은 지문 추적 방지, 1차 당사자 격리, 레터박싱 기능을 활성화한 상태에서 격리된 컨테이너 탭을 자동으로 생성함으로써 대부분의 작업을 자동화합니다. Chromium 사용자의 경우, 다음과 같은 별도의 플래그로 실행하십시오: `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"` .

---

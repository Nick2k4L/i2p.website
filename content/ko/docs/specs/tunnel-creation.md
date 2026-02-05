---
title: "Tunnel 생성 사양"
description: "비대화형 텔레스코핑을 사용하여 tunnel을 생성하기 위한 ElGamal tunnel 구축 사양."
slug: "tunnel-creation"
aliases: 
category: "설계"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## 개요

참고: 구식 - 이것은 ElGamal tunnel 구축 사양입니다. X25519 tunnel 구축 사양은 [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/)를 참조하세요.

이 문서는 "비대화형 망원경" 방법을 사용하여 tunnel을 생성하는 데 사용되는 암호화된 tunnel 구축 메시지의 세부 사항을 명시합니다. 피어 선택 및 정렬 방법을 포함한 프로세스 개요는 tunnel 구축 문서 [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)을 참조하세요.

tunnel 생성은 tunnel 경로상의 피어들을 따라 전달되는 단일 메시지를 통해 수행되며, 이 메시지는 제자리에서 다시 작성되어 tunnel 생성자에게 다시 전송됩니다. 이 단일 tunnel 메시지는 가변적인 수의 레코드(최대 8개)로 구성되며, tunnel 내 각 잠재적 피어마다 하나씩 할당됩니다. 개별 레코드는 경로상의 특정 피어만이 읽을 수 있도록 비대칭적으로 (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) 암호화되며, 각 홉마다 추가적인 대칭 암호화 계층 (AES [CRYPTO-AES](/docs/specs/cryptography/#aes))이 추가되어 적절한 시점에만 비대칭적으로 암호화된 레코드가 노출되도록 합니다.

### 레코드 수

모든 레코드가 유효한 데이터를 포함해야 하는 것은 아닙니다. 예를 들어, 3-hop tunnel의 빌드 메시지는 참가자들로부터 tunnel의 실제 길이를 숨기기 위해 더 많은 레코드를 포함할 수 있습니다. 빌드 메시지에는 두 가지 타입이 있습니다. 원래의 Tunnel Build Message ([TBM](/docs/specs/i2np/#struct-TunnelBuild))는 8개의 레코드를 포함하며, 이는 실용적인 어떤 tunnel 길이에도 충분합니다. 더 새로운 Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild))는 1개부터 8개까지의 레코드를 포함합니다. 발신자는 메시지의 크기와 원하는 tunnel 길이 난독화 정도 사이에서 절충점을 선택할 수 있습니다.

현재 네트워크에서 대부분의 tunnel은 2개 또는 3개 hop 길이입니다. 현재 구현에서는 4개 hop 이하의 tunnel을 구축하기 위해 5-record VTBM을 사용하고, 더 긴 tunnel에는 8-record TBM을 사용합니다. 5-record VTBM은 (분할될 때 세 개의 1KB tunnel 메시지에 맞춰집니다) 네트워크 트래픽을 줄이고 구축 성공률을 높입니다. 작은 메시지가 드롭될 가능성이 낮기 때문입니다.

응답 메시지는 빌드 메시지와 동일한 유형과 길이여야 합니다.

### 요청 레코드 명세서

또한 I2NP 명세서 [BRR](/docs/specs/i2np/#struct-BuildRequestRecord)에 명시되어 있습니다.

요청받는 hop에게만 보이는 레코드의 평문:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
다음 tunnel ID와 다음 router 신원 해시 필드는 tunnel의 다음 홉을 지정하는 데 사용되지만, 아웃바운드 tunnel 엔드포인트의 경우에는 재작성된 tunnel 생성 응답 메시지가 전송되어야 할 위치를 지정합니다. 또한 다음 메시지 ID는 메시지(또는 응답)가 사용해야 하는 메시지 ID를 지정합니다.

tunnel layer key, tunnel IV key, reply key, reply IV는 각각 생성자가 생성한 무작위 32바이트 값으로, 이 빌드 요청 레코드에서만 사용됩니다.

flags 필드는 다음을 포함합니다 (비트 순서: 76543210, 비트 7이 MSB):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
비트 7은 해당 홉이 인바운드 게이트웨이(IBGW)가 될 것임을 나타냅니다. 비트 6은 해당 홉이 아웃바운드 엔드포인트(OBEP)가 될 것임을 나타냅니다. 두 비트 모두 설정되지 않은 경우, 홉은 중간 참여자가 됩니다. 두 비트가 동시에 설정될 수는 없습니다.

#### 요청 레코드 생성

모든 hop은 0이 아닌 무작위 Tunnel ID를 받습니다. 현재와 다음 hop의 Tunnel ID가 채워집니다. 모든 레코드는 무작위 tunnel IV 키, 응답 IV, 레이어 키, 응답 키를 받습니다.

#### 요청 레코드 암호화

해당 평문 레코드는 hop의 공개 암호화 키로 ElGamal 2048 암호화 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)되어 528바이트 레코드로 포맷됩니다:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
512바이트 암호화된 레코드에서, ElGamal 데이터는 514바이트 ElGamal 암호화된 블록 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)의 1-256바이트와 258-513바이트를 포함합니다. 블록의 두 패딩 바이트(위치 0과 257의 제로 바이트)는 제거됩니다.

cleartext가 전체 필드를 사용하므로 `SHA256(cleartext) + cleartext` 외에 추가 패딩이 필요하지 않습니다.

각 528바이트 레코드는 반복적으로 암호화되며(각 홉에 대해 reply key와 reply IV를 사용한 AES 복호화 사용), router identity는 해당 홉에서만 평문으로 나타납니다.

### 홉 처리 및 암호화

hop이 TunnelBuildMessage를 받으면, 그 안에 포함된 레코드들을 살펴보며 자신의 identity hash(16바이트로 잘린)로 시작하는 레코드를 찾습니다. 그런 다음 해당 레코드에서 ElGamal 블록을 복호화하고 보호된 평문을 가져옵니다. 이 시점에서 AES-256 응답 키를 Bloom filter에 넣어서 tunnel 요청이 중복이 아닌지 확인합니다. 중복되거나 유효하지 않은 요청은 삭제됩니다. 현재 시간이나 시간 초반 직후라면 이전 시간으로 스탬프가 찍히지 않은 레코드는 반드시 삭제되어야 합니다. 예를 들어, 타임스탬프의 시간을 가져와서 전체 시간으로 변환한 다음, 현재 시간보다 65분 이상 뒤처지거나 5분 이상 앞서 있으면 유효하지 않습니다. Bloom filter는 최소 1시간(시계 편차를 허용하기 위해 몇 분 추가)의 지속 시간을 가져야 하므로, 레코드의 시간 타임스탬프 확인으로 거부되지 않은 현재 시간의 중복 레코드들이 filter에 의해 거부됩니다.

tunnel에 참여할지 여부를 결정한 후, 요청이 포함되어 있던 레코드를 암호화된 응답 블록으로 교체합니다. 다른 모든 레코드는 포함된 응답 키와 IV로 AES-256 암호화 [CRYPTO-AES](/docs/specs/cryptography/#aes)됩니다. 각각은 동일한 응답 키와 응답 IV로 개별적으로 AES/CBC 암호화됩니다. CBC 모드는 레코드 간에 지속되지(연결되지) 않습니다.

각 hop은 자신의 응답만을 알고 있습니다. 동의한다면, 다른 모든 hop들이 동의했는지 알 수 없기 때문에 사용되지 않더라도 만료될 때까지 tunnel을 유지할 것입니다.

#### 응답 레코드 사양

현재 hop이 자신의 레코드를 읽은 후, tunnel 참여에 동의하는지 여부를 명시하는 응답 레코드로 교체하며, 동의하지 않는 경우 거부 사유를 분류합니다. 이는 단순히 1바이트 값으로, 0x0은 tunnel 참여에 동의함을 의미하고, 더 높은 값은 더 높은 수준의 거부를 의미합니다.

다음과 같은 거부 코드가 정의되어 있습니다:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

router 종료와 같은 다른 원인을 피어들로부터 숨기기 위해, 현재 구현에서는 거의 모든 거부에 대해 TUNNEL_REJECT_BANDWIDTH를 사용합니다.

응답은 암호화된 블록에서 전달된 AES 세션 키로 암호화되며, 전체 레코드 크기에 도달하기 위해 495바이트의 무작위 데이터로 패딩됩니다. 패딩은 상태 바이트 앞에 배치됩니다:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
이는 I2NP 스펙 [BRR](/docs/specs/i2np/#struct-BuildRequestRecord)에서도 설명되어 있습니다.

### Tunnel 구축 메시지 준비

새로운 Tunnel Build Message를 구축할 때, 모든 Build Request Record들은 먼저 구축되고 ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)을 사용하여 비대칭 암호화되어야 합니다. 그런 다음 각 레코드는 경로상의 이전 홉들의 응답 키와 IV를 사용하여 AES [CRYPTO-AES](/docs/specs/cryptography/#aes)로 선제적으로 복호화됩니다. 해당 복호화는 역순으로 실행되어야 하므로, 비대칭 암호화된 데이터가 이전 홉이 암호화한 후 올바른 홉에서 평문으로 나타나게 됩니다.

개별 요청에 필요하지 않은 초과 레코드는 생성자가 단순히 무작위 데이터로 채웁니다.

### Tunnel 구축 메시지 전달

아웃바운드 tunnel의 경우, 전달은 tunnel 생성자로부터 첫 번째 홉으로 직접 수행되며, 생성자가 tunnel의 또 다른 홉인 것처럼 TunnelBuildMessage를 패키징합니다. 인바운드 tunnel의 경우, 전달은 기존 아웃바운드 tunnel을 통해 수행됩니다. 아웃바운드 tunnel은 일반적으로 구축되는 새 tunnel과 동일한 풀에서 선택됩니다. 해당 풀에서 사용 가능한 아웃바운드 tunnel이 없으면 아웃바운드 탐색 tunnel이 사용됩니다. 시작 시 아웃바운드 탐색 tunnel이 아직 존재하지 않을 때는 가짜 0-홉 아웃바운드 tunnel이 사용됩니다.

### Tunnel 빌드 메시지 엔드포인트 처리

outbound tunnel 생성의 경우, 요청이 outbound endpoint에 도달하면 ('allow messages to anyone' 플래그에 의해 결정됨), 해당 hop은 평소와 같이 처리되어 레코드 대신 응답을 암호화하고 다른 모든 레코드들을 암호화합니다. 하지만 TunnelBuildMessage를 전달할 '다음 hop'이 없으므로, 대신 암호화된 응답 레코드들을 TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) 또는 VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply))에 배치하고 (메시지 타입과 레코드 수는 요청과 일치해야 함) 요청 레코드 내에 지정된 reply tunnel로 전달합니다. 해당 reply tunnel은 다른 메시지와 마찬가지로 Tunnel Build Reply Message를 tunnel 생성자에게 다시 전달합니다 [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). 그러면 tunnel 생성자는 아래에 설명된 대로 이를 처리합니다.

응답 tunnel은 생성자에 의해 다음과 같이 선택됩니다: 일반적으로 구축 중인 새로운 아웃바운드 tunnel과 동일한 풀의 인바운드 tunnel입니다. 해당 풀에서 사용 가능한 인바운드 tunnel이 없는 경우, 인바운드 탐색 tunnel이 사용됩니다. 시작 시, 인바운드 탐색 tunnel이 아직 존재하지 않을 때는 가짜 0-hop 인바운드 tunnel이 사용됩니다.

인바운드 tunnel 생성 시, 요청이 인바운드 엔드포인트(tunnel 생성자라고도 함)에 도달하면 명시적인 Tunnel Build Reply Message를 생성할 필요가 없으며, router는 아래와 같이 각 응답을 처리합니다.

### Tunnel 구축 응답 메시지 처리

응답 레코드를 처리하기 위해, 생성자는 단순히 각 레코드를 개별적으로 AES 복호화하면 되며, 피어 이후 tunnel의 각 hop의 응답 키와 IV를 (역순으로) 사용합니다. 이를 통해 tunnel 참여에 동의하는지 또는 거부하는 이유를 명시하는 응답이 노출됩니다. 모든 노드가 동의하면 tunnel이 생성된 것으로 간주되어 즉시 사용할 수 있지만, 누군가 거부하면 tunnel은 폐기됩니다.

승인과 거부는 각 피어의 프로필 [PEER-SELECTION](/docs/overview/tunnel-routing/)에 기록되어, 향후 피어 tunnel 용량 평가에 사용됩니다.

## 역사 및 참고사항

이 전략은 predecessor attack에 관해 I2P 메일링 리스트에서 Michael Rogers, Matthew Toseland (toad), 그리고 jrandom 사이의 논의 중에 나왔습니다. [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html), [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)을 참조하세요. 이는 2006-02-16에 출시된 0.6.1.10 버전에서 도입되었으며, 이는 I2P에서 비역호환적 변경이 이루어진 마지막 시점이었습니다.

참고사항:

- 이 설계는 tunnel 내의 두 적대적 peer가 하나 이상의 요청이나 응답 레코드에 태그를 달아 같은 tunnel 내에 있다는 것을 탐지하는 것을 방지하지 않지만, 이렇게 하면 tunnel 생성자가 응답을 읽을 때 탐지할 수 있어 해당 tunnel이 무효로 표시됩니다.
- 이 설계는 비대칭 암호화된 섹션에 작업 증명을 포함하지 않지만, 16바이트 신원 해시를 반으로 줄이고 후자를 최대 2^64 비용의 hashcash 함수로 대체할 수 있습니다.
- 이 설계만으로는 tunnel 내의 두 적대적 peer가 타이밍 정보를 사용하여 같은 tunnel에 있는지 확인하는 것을 방지하지 않습니다. 일괄 처리되고 동기화된 요청 전달을 사용하면 도움이 될 수 있습니다(요청을 일괄 처리하여 (ntp 동기화된) 분 단위로 전송). 하지만 이렇게 하면 peer들이 요청을 지연시키고 나중에 tunnel에서 지연을 탐지하여 요청에 '태그'를 달 수 있습니다. 다만 작은 시간 창에서 전달되지 않은 요청을 삭제하는 것이 작동할 수 있습니다(하지만 이렇게 하려면 높은 수준의 시계 동기화가 필요합니다). 대안으로, 개별 홉이 요청을 전달하기 전에 무작위 지연을 주입할 수 있을까요?
- 요청에 태그를 다는 치명적이지 않은 방법이 있나요?
- 1시간 해상도를 가진 타임스탬프는 재생 공격 방지에 사용됩니다. 이 제약은 0.9.16 릴리스까지 강제되지 않았습니다.

## 향후 작업

- 현재 구현에서 originator는 자신을 위해 하나의 레코드를 비워둡니다. 따라서 n개의 레코드로 구성된 메시지는 n-1 hop의 tunnel만 구축할 수 있습니다. 이는 인바운드 tunnel(마지막에서 두 번째 hop이 다음 hop에 대한 해시 접두사를 볼 수 있는 경우)에는 필요한 것으로 보이지만, 아웃바운드 tunnel에는 그렇지 않습니다. 이는 연구하고 검증해야 할 사항입니다. 익명성을 손상시키지 않고 남은 레코드를 사용할 수 있다면, 그렇게 해야 합니다.
- 위 주석에서 설명한 가능한 태깅 및 타이밍 공격에 대한 추가 분석.
- VTBM만 사용하고, 이를 지원하지 않는 오래된 피어는 선택하지 않습니다.
- Build Request Record는 tunnel 수명이나 만료 시간을 지정하지 않습니다. 각 hop은 10분 후에 tunnel을 만료시키는데, 이는 네트워크 전체에 하드코딩된 상수입니다. 플래그 필드의 비트를 사용하고 패딩에서 4바이트(또는 8바이트)를 가져와서 수명이나 만료 시간을 지정할 수 있습니다. 요청자는 모든 참여자가 이를 지원하는 경우에만 이 옵션을 지정할 것입니다.

## 참고 문헌

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - BuildRequestRecord 명세
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - AES 암호화
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - ElGamal 암호화
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage

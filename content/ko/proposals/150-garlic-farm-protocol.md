---
title: "Garlic Farm 프로토콜"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "Open"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## 개요

이 문서는 JRaft를 기반으로 하며, TCP를 통한 구현을 위한 "exts" 코드와 그 "dmprinter" 샘플 애플리케이션 [JRAFT](https://github.com/datatechnology/jraft)에 기반한 Garlic Farm 와이어 프로토콜 사양입니다.

문서화된 와이어 프로토콜을 가진 구현체를 찾을 수 없었습니다. 그러나 JRaft 구현은 충분히 단순하여 코드를 검사한 후 그 프로토콜을 문서화할 수 있었습니다. 이 제안서는 그러한 노력의 결과입니다.

이 사양은 라우터가 메타 LeaseSet에 항목을 게시할 때의 조정을 위한 백엔드가 될 것입니다. 제안서 123을 참조하세요.

## 목표

- 작은 코드 크기
- 기존 구현에 기반
- 직렬화된 Java 객체나 Java 전용 기능 또는 인코딩 사용 금지
- 부트스트래핑은 범위 밖입니다. 최소한 하나 이상의 서버는 하드코딩되거나 이 프로토콜 외부에서 구성된 것으로 간주합니다.
- 아웃오브밴드 및 I2P 내부 사용 사례 모두 지원

## 설계

Raft 프로토콜은 구체적인 프로토콜이 아니라 상태 머신만 정의합니다. 따라서 우리는 JRaft의 구체적인 프로토콜을 문서화하고 이를 기반으로 합니다. JRaft 프로토콜에 대한 변경 사항은 인증 핸드셰이크 추가 외에는 없습니다.

Raft는 로그를 게시하는 리더를 선출합니다. 로그는 Raft 구성 데이터와 애플리케이션 데이터를 포함합니다. 애플리케이션 데이터는 각 서버의 라우터 상태와 Meta LS2 클러스터의 대상(Destination)을 포함합니다. 서버들은 공통 알고리즘을 사용하여 Meta LS2의 게시자와 내용을 결정합니다. Meta LS2의 게시자는 반드시 Raft 리더일 필요는 없습니다.

## 사양

와이어 프로토콜은 SSL 소켓 또는 비-SSL I2P 소켓을 통해 이루어집니다. I2P 소켓은 HTTP 프록시를 통해 프록시됩니다. 클리어넷 비-SSL 소켓은 지원하지 않습니다.

### 핸드셰이크 및 인증

JRaft에서 정의하지 않음.

목표:

- 사용자/비밀번호 인증 방식
- 버전 식별자
- 클러스터 식별자
- 확장 가능
- I2P 소켓 사용 시 프록시를 쉽게 할 수 있음
- 불필요하게 서버를 Garlic Farm 서버로 노출하지 않음
- 전체 웹 서버 구현이 필요하지 않은 간단한 프로토콜
- 일반적인 표준과 호환되어 구현체가 원할 경우 표준 라이브러리를 사용할 수 있음

웹소켓과 유사한 핸드셰이크와 HTTP 다이제스트 인증 [RFC 2617](https://tools.ietf.org/html/rfc2617)을 사용합니다. RFC 2617의 기본 인증(Basic authentication)은 지원하지 않습니다. HTTP 프록시를 통해 프록시할 때는 [RFC 2616](https://tools.ietf.org/html/rfc2616)에 명시된 대로 프록시와 통신합니다.

#### 자격 증명

사용자 이름과 비밀번호가 클러스터별인지 서버별인지 여부는 구현에 따라 다릅니다.

#### HTTP 요청 1

발신자는 다음을 전송합니다.

모든 줄은 HTTP에서 요구하는 대로 CRLF로 종료됩니다.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (any other headers ignored)
  (blank line)

  CLUSTER is the name of the cluster (default "farm")
  VERSION is the Garlic Farm version (currently "1")

```

#### HTTP 응답 1

경로가 올바르지 않으면, 수신자는 [RFC 2616](https://tools.ietf.org/html/rfc2616)에 따라 표준 "HTTP/1.1 404 Not Found" 응답을 보냅니다.

경로가 올바르면, 수신자는 [RFC 2617](https://tools.ietf.org/html/rfc2617)에 따라 WWW-Authenticate HTTP 다이제스트 인증 헤더를 포함한 표준 "HTTP/1.1 401 Unauthorized" 응답을 보냅니다.

양측은 이후 소켓을 닫습니다.

#### HTTP 요청 2

발신자는 [RFC 2617](https://tools.ietf.org/html/rfc2617)에 따라 다음을 전송합니다.

모든 줄은 HTTP에서 요구하는 대로 CRLF로 종료됩니다.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (Sec-Websocket-* headers if proxied)
  Authorization: (HTTP digest authorization header as in RFC 2617)
  (any other headers ignored)
  (blank line)

  CLUSTER is the name of the cluster (default "farm")
  VERSION is the Garlic Farm version (currently "1")

```

#### HTTP 응답 2

인증이 올바르지 않으면, 수신자는 [RFC 2617](https://tools.ietf.org/html/rfc2617)에 따라 또 다른 표준 "HTTP/1.1 401 Unauthorized" 응답을 보냅니다.

인증이 올바르면, 수신자는 웹소켓 프로토콜에 따라 다음 응답을 보냅니다.

모든 줄은 HTTP에서 요구하는 대로 CRLF로 종료됩니다.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (Sec-Websocket-* headers)
  (any other headers ignored)
  (blank line)

```

이 응답을 수신한 후 소켓은 계속 열린 상태로 유지됩니다. 아래에 정의된 Raft 프로토콜이 동일한 소켓에서 시작됩니다.

#### 캐싱

자격 증명은 최소한 1시간 동안 캐싱되어야 하므로, 이후 연결은 위의 "HTTP 요청 2"로 바로 점프할 수 있습니다.

### 메시지 유형

두 가지 유형의 메시지가 있습니다: 요청과 응답. 요청은 로그 항목을 포함할 수 있으며 가변 크기입니다. 응답은 로그 항목을 포함하지 않으며 고정 크기입니다.

메시지 유형 1-4는 Raft에서 정의한 표준 RPC 메시지입니다. 이것이 핵심 Raft 프로토콜입니다.

메시지 유형 5-15는 JRaft에서 정의한 확장된 RPC 메시지로, 클라이언트 지원, 동적 서버 변경, 효율적인 로그 동기화를 위해 사용됩니다.

메시지 유형 16-17은 Raft 7절에서 정의한 로그 압축 RPC 메시지입니다.

| 메시지 | 번호 | 발신자 | 수신자 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | 후보자(Candidate) | 팔로워(Follower) | 표준 Raft RPC; 로그 항목 포함 금지 |
| RequestVoteResponse | 2 | 팔로워 | 후보자 | 표준 Raft RPC |
| AppendEntriesRequest | 3 | 리더 | 팔로워 | 표준 Raft RPC |
| AppendEntriesResponse | 4 | 팔로워 | 리더 / 클라이언트 | 표준 Raft RPC |
| ClientRequest | 5 | 클라이언트 | 리더 / 팔로워 | 응답은 AppendEntriesResponse; 애플리케이션 로그 항목만 포함해야 함 |
| AddServerRequest | 6 | 클라이언트 | 리더 | 단일 ClusterServer 로그 항목만 포함해야 함 |
| AddServerResponse | 7 | 리더 | 클라이언트 | 리더는 또한 JoinClusterRequest를 보냄 |
| RemoveServerRequest | 8 | 팔로워 | 리더 | 단일 ClusterServer 로그 항목만 포함해야 함 |
| RemoveServerResponse | 9 | 리더 | 팔로워 | |
| SyncLogRequest | 10 | 리더 | 팔로워 | 단일 LogPack 로그 항목만 포함해야 함 |
| SyncLogResponse | 11 | 팔로워 | 리더 | |
| JoinClusterRequest | 12 | 리더 | 새 서버 | 가입 초대; 단일 구성 로그 항목만 포함해야 함 |
| JoinClusterResponse | 13 | 새 서버 | 리더 | |
| LeaveClusterRequest | 14 | 리더 | 팔로워 | 탈퇴 명령 |
| LeaveClusterResponse | 15 | 팔로워 | 리더 | |
| InstallSnapshotRequest | 16 | 리더 | 팔로워 | Raft 7절; 단일 SnapshotSyncRequest 로그 항목만 포함해야 함 |
| InstallSnapshotResponse | 17 | 팔로워 | 리더 | Raft 7절 |

### 연결 설정

HTTP 핸드셰이크 후 연결 설정 순서는 다음과 같습니다:

```text

새 서버 앨리스              임의의 팔로워 밥

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  밥이 자신이 리더라고 말하면 아래로 계속 진행.
  그렇지 않으면, 앨리스는 밥과 연결을 끊고 리더에 연결해야 함.


  새 서버 앨리스              리더 찰리

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       OR InstallSnapshotRequest
  SyncLogResponse  ------->
  OR InstallSnapshotResponse

```

연결 종료 순서:

```text

팔로워 앨리스              리더 찰리

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

선거 순서:

```text

후보자 앨리스               팔로워 밥

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  앨리스가 선거에서 승리하면:

  리더 앨리스                팔로워 밥

  AppendEntriesRequest   ------->
  (heartbeat)
          <---------   AppendEntriesResponse

```

### 정의

- 소스(Source): 메시지 발신자를 식별
- 대상(Destination): 메시지 수신자를 식별
- 텀(Terms): Raft 참조. 0으로 초기화되며 단조롭게 증가
- 인덱스(Indexes): Raft 참조. 0으로 초기화되며 단조롭게 증가

### 요청

요청은 헤더와 0개 이상의 로그 항목을 포함합니다. 요청은 고정 크기 헤더와 가변 크기의 선택적 로그 항목을 포함합니다.

#### 요청 헤더

요청 헤더는 45바이트이며 다음과 같습니다. 모든 값은 부호 없는 빅엔디언입니다.

```text

메시지 유형:      1바이트
  소스:            ID, 4바이트 정수
  대상:            ID, 4바이트 정수
  텀:              현재 텀 (참고 참조), 8바이트 정수
  마지막 로그 텀:     8바이트 정수
  마지막 로그 인덱스:    8바이트 정수
  커밋 인덱스:      8바이트 정수
  로그 항목 크기:  바이트 단위 총 크기, 4바이트 정수
  로그 항목:       아래 참조, 지정된 총 길이

```

#### 참고

RequestVoteRequest에서 텀은 후보자의 텀입니다. 그 외의 경우 리더의 현재 텀입니다.

AppendEntriesRequest에서 로그 항목 크기가 0이면 이 메시지는 하트비트(keepalive) 메시지입니다.

#### 로그 항목

로그는 0개 이상의 로그 항목을 포함합니다. 각 로그 항목은 다음과 같습니다. 모든 값은 부호 없는 빅엔디언입니다.

```text

텀:           8바이트 정수
  값 유형:     1바이트
  항목 크기:     바이트 단위, 4바이트 정수
  항목:          지정된 길이

```

#### 로그 내용

모든 값은 부호 없는 빅엔디언입니다.

| 로그 값 유형 | 번호 |
| :--- | :--- |
| 애플리케이션 | 1 |
| 구성 | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |

#### 애플리케이션

애플리케이션 내용은 UTF-8 인코딩된 [JSON](https://www.json.org/)입니다. 아래 애플리케이션 계층 섹션 참조.

#### 구성

리더가 새 클러스터 구성을 직렬화하고 피어에 복제할 때 사용됩니다. 0개 이상의 ClusterServer 구성이 포함됩니다.

```text

로그 인덱스:  8바이트 정수
  마지막 로그 인덱스:  8바이트 정수
  각 서버의 ClusterServer 데이터:
    ID:                4바이트 정수
    엔드포인트 데이터 길이: 바이트 단위, 4바이트 정수
    엔드포인트 데이터:     "tcp://localhost:9001" 형태의 ASCII 문자열, 지정된 길이

```

#### ClusterServer

클러스터 내 서버의 구성 정보. AddServerRequest 또는 RemoveServerRequest 메시지에만 포함됩니다.

AddServerRequest 메시지에서 사용할 때:

```text

ID:                4바이트 정수
  엔드포인트 데이터 길이: 바이트 단위, 4바이트 정수
  엔드포인트 데이터:     "tcp://localhost:9001" 형태의 ASCII 문자열, 지정된 길이

```

RemoveServerRequest 메시지에서 사용할 때:

```text

ID:                4바이트 정수

```

#### LogPack

SyncLogRequest 메시지에만 포함됩니다.

전송 전에 다음은 gzip으로 압축됩니다:

```text

인덱스 데이터 길이: 바이트 단위, 4바이트 정수
  로그 데이터 길이:   바이트 단위, 4바이트 정수
  인덱스 데이터:     각 인덱스당 8바이트, 지정된 길이
  로그 데이터:       지정된 길이

```

#### SnapshotSyncRequest

InstallSnapshotRequest 메시지에만 포함됩니다.

```text

마지막 로그 인덱스:  8바이트 정수
  마지막 로그 텀:   8바이트 정수
  구성 데이터 길이: 바이트 단위, 4바이트 정수
  구성 데이터:     지정된 길이
  오프셋:          데이터베이스 내 데이터의 오프셋(바이트 단위), 8바이트 정수
  데이터 길이:        바이트 단위, 4바이트 정수
  데이터:            지정된 길이
  완료 여부:         완료 시 1, 미완료 시 0 (1바이트)

```

### 응답

모든 응답은 26바이트이며 다음과 같습니다. 모든 값은 부호 없는 빅엔디언입니다.

```text

메시지 유형:   1바이트
  소스:         ID, 4바이트 정수
  대상:    일반적으로 실제 대상 ID (참고 참조), 4바이트 정수
  텀:           현재 텀, 8바이트 정수
  다음 인덱스:     리더의 마지막 로그 인덱스 + 1로 초기화, 8바이트 정수
  수락 여부:    수락 시 1, 미수락 시 0 (참고 참조), 1바이트

```

#### 참고

대상 ID는 일반적으로 이 메시지의 실제 대상입니다. 그러나 AppendEntriesResponse, AddServerResponse, RemoveServerResponse의 경우 현재 리더의 ID입니다.

RequestVoteResponse에서 수락 여부는 후보자(요청자)에게 투표할 경우 1, 투표하지 않을 경우 0입니다.

## 애플리케이션 계층

각 서버는 주기적으로 ClientRequest에서 로그에 애플리케이션 데이터를 게시합니다. 애플리케이션 데이터는 각 서버의 라우터 상태와 Meta LS2 클러스터의 대상(Destination)을 포함합니다. 서버들은 공통 알고리즘을 사용하여 Meta LS2의 게시자와 내용을 결정합니다. 로그에서 "가장 좋은" 최근 상태를 가진 서버가 Meta LS2 게시자입니다. Meta LS2의 게시자는 반드시 Raft 리더일 필요는 없습니다.

### 애플리케이션 데이터 내용

단순성과 확장성을 위해 애플리케이션 내용은 UTF-8 인코딩된 [JSON](https://json.org/)입니다. 전체 사양은 미정(TBD)입니다. 목표는 Meta LS2를 게시할 "가장 좋은" 라우터를 결정할 알고리즘을 작성할 수 있는 충분한 데이터를 제공하고, 게시자가 Meta LS2 내 대상들을 가중치를 두어 선택할 수 있는 충분한 정보를 갖도록 하는 것입니다. 데이터는 라우터 및 대상 통계를 모두 포함합니다.

데이터는 선택적으로 다른 서버의 상태 및 Meta LS 가져오기 능력에 대한 원격 감지 데이터를 포함할 수 있습니다. 이러한 데이터는 첫 번째 릴리스에서 지원되지 않을 수 있습니다.

데이터는 선택적으로 관리자 클라이언트가 게시한 구성 정보를 포함할 수 있습니다. 이러한 데이터는 첫 번째 릴리스에서 지원되지 않을 수 있습니다.

"name: value"가 나열된 경우, JSON 맵 키와 값을 지정합니다. 그 외는 사양 미정(TBD)입니다.

클러스터 데이터(최상위):

- cluster: 클러스터 이름
- date: 이 데이터의 날짜 (long, 에포크 이후 밀리초)
- id: Raft ID (정수)

구성 데이터(config):

- 모든 구성 매개변수

MetaLS 게시 상태(meta):

- destination: 메탈스 대상, base64
- lastPublishedLS: 존재할 경우, 마지막으로 게시된 메탈스의 base64 인코딩
- lastPublishedTime: 밀리초 단위, 또는 처음 게시하지 않았을 경우 0
- publishConfig: 게시자 구성 상태 off/on/auto
- publishing: 메탈스 게시자 상태 불리언 true/false

라우터 데이터(router):

- lastPublishedRI: 존재할 경우, 마지막으로 게시된 라우터 정보의 base64 인코딩
- uptime: 가동 시간(밀리초)
- Job lag
- 탐사 터널
- 참여 터널
- 구성된 대역폭
- 현재 대역폭

대상들(destinations):
목록

대상 데이터:

- destination: 대상, base64
- uptime: 가동 시간(밀리초)
- 구성된 터널
- 현재 터널
- 구성된 대역폭
- 현재 대역폭
- 구성된 연결
- 현재 연결
- 블랙리스트 데이터

원격 라우터 감지 데이터:

- 본 라우터가 본 마지막 RI 버전
- LS 가져오기 시간
- 연결 테스트 데이터
- 가장 가까운 플러드필의 프로파일 데이터
  어제, 오늘, 내일 기간에 대해

원격 대상 감지 데이터:

- 본 라우터가 본 마지막 LS 버전
- LS 가져오기 시간
- 연결 테스트 데이터
- 가장 가까운 플러드필의 프로파일 데이터
  어제, 오늘, 내일 기간에 대해

Meta LS 감지 데이터:

- 본 라우터가 본 마지막 버전
- 가져오기 시간
- 가장 가까운 플러드필의 프로파일 데이터
  어제, 오늘, 내일 기간에 대해

## 관리 인터페이스

미정(TBD), 별도의 제안일 수 있음. 첫 번째 릴리스에는 필요하지 않음.

관리 인터페이스 요구사항:

- 다중 마스터 대상 지원, 즉 다중 가상 클러스터(팜)
- 구성원이 게시한 모든 통계, 현재 리더 등 공유 클러스터 상태의 포괄적인 보기 제공
- 클러스터에서 참가자 또는 리더를 강제로 제거할 수 있는 기능
- 현재 노드가 게시자일 경우 메타LS 강제 게시 기능
- 현재 노드가 게시자일 경우 메타LS에서 해시를 제외할 수 있는 기능
- 대량 배포를 위한 구성 가져오기/내보내기 기능

## 라우터 인터페이스

미정(TBD), 별도의 제안일 수 있음. 첫 번째 릴리스에는 i2pcontrol이 필요하지 않으며 자세한 변경 사항은 별도 제안서에 포함될 예정입니다.

Garlic Farm에서 라우터로의 API 요구사항 (in-JVM 자바 또는 i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // 아마 MVP에는 없음
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // 또는 서명된 MetaLeaseSet? 누가 서명?
- stopPublishingMetaLS(Hash masterHash)
- 인증 TBD?

## 정당성

Atomix는 너무 크며 I2P를 통해 프로토콜을 라우팅할 수 있도록 사용자 정의를 허용하지 않습니다. 또한 그 와이어 형식은 문서화되어 있지 않으며 Java 직렬화에 의존합니다.

## 참고

## 이슈

- 클라이언트가 알 수 없는 리더를 찾아 연결할 방법이 없습니다. 팔로워가 AppendEntriesResponse에서 구성 정보를 로그 항목으로 전송하도록 하는 것은 사소한 변경 사항입니다.

## 마이그레이션

하위 호환성 문제 없음.

## 참고 자료

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)

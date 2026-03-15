---
title: "OBEP의 1-of-N 또는 N-of-N 터널로의 전달"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Open"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## 개요

이 제안서는 네트워크 성능 향상을 위한 두 가지 개선 사항을 다룹니다:

- 단일 옵션 대신 대안 목록을 제공함으로써 OBEP가 IBGW 선택을 위임받도록 함.

- OBEP에서 멀티캐스트 패킷 라우팅을 가능하게 함.


## 동기

직접 연결 상황에서, OBEP가 IBGW에 연결하는 방식에 유연성을 부여함으로써 연결 혼잡을 줄이는 것이 목적입니다. 다중 터널을 지정할 수 있는 기능은 OBEP에서 멀티캐스트를 구현하는 데에도 활용될 수 있습니다(지정된 모든 터널에 메시지를 전달함으로써).

이 제안의 위임 부분에 대한 대안으로는 기존의 대상 [RouterIdentity](/docs/specs/common-structures/#common-structure-specification) 해시를 지정하는 것과 유사하게 LeaseSet 해시를 전송하는 방법이 있습니다. 이 방법은 더 작은 메시지 크기를 가지며 잠재적으로 더 최신의 LeaseSet을 사용할 수 있습니다. 그러나 다음의 문제가 있습니다:

1. OBEP가 조회를 수행하도록 강제함.

2. LeaseSet이 플러드필(floodfill)에 게시되지 않았을 경우 조회가 실패할 수 있음.

3. LeaseSet이 암호화되어 있을 경우 OBEP가 lease를 얻을 수 없음.

4. LeaseSet을 지정하는 것은 OBEP에게 메시지의 [Destination](/docs/specs/common-structures/#destination)을 노출시키며, 그렇지 않으면 OBEP는 네트워크의 모든 LeaseSet을 스크래핑하여 Lease 일치 여부를 확인해야만 알 수 있음.


## 설계

발신자(OBGW)는 단 하나의 Lease만 선택하는 대신, 대상 [Leases](/docs/specs/common-structures/#lease) 중 일부(또는 전부)를 전달 지시문 [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions)에 포함시킵니다.

OBEP는 그 중 하나를 선택하여 전달합니다. 가능하다면 OBEP는 이미 연결되어 있거나 이미 알고 있는 Lease를 선택합니다. 이를 통해 OBEP-IBGW 경로가 더 빠르고 안정적이며, 전체 네트워크 연결 수를 줄일 수 있습니다.

TUNNEL-DELIVERY의 플래그에서 사용되지 않은 전달 유형 하나(0x03)와 두 개의 남은 비트(0과 1)를 활용하여 이러한 기능을 구현할 수 있습니다.


## 보안 영향

이 제안은 OBGW의 대상 Destination이나 NetDB에 대한 시각 정보 유출량을 변경하지 않습니다:

- OBEP를 제어하고 NetDB에서 LeaseSet을 스크래핑하는 공격자는 이미 메시지가 특정 Destination으로 전송되는지 여부를 TunnelId / RouterIdentity 쌍을 검색하여 판단할 수 있습니다. 최악의 경우, TMDI에 여러 Lease가 존재하면 공격자의 데이터베이스에서 일치 항목을 더 빠르게 찾을 수 있습니다.

- 악성 Destination을 운영하는 공격자는 서로 다른 플러드필에 다른 인바운드 터널을 포함한 LeaseSet을 게시하고, OBGW가 어떤 터널을 통해 연결되는지 관찰함으로써 피해자의 NetDB 시각에 대한 정보를 이미 얻을 수 있습니다. 공격자의 관점에서 OBEP가 터널 사용 여부를 결정하는 것은 OBGW가 선택하는 것과 기능적으로 동일합니다.

멀티캐스트 플래그는 OBGW가 OBEP에 멀티캐스트를 수행하고 있다는 사실을 OBEP에게 노출시킵니다. 이는 고수준 프로토콜 구현 시 고려해야 할 성능과 프라이버시 간의 트레이드오프를 만듭니다. 선택적 플래그이기 때문에 사용자는 애플리케이션에 맞는 적절한 결정을 내릴 수 있습니다. 그러나 다양한 애플리케이션에서 광범위하게 사용된다면 특정 메시지가 어떤 애플리케이션에서 왔는지에 대한 정보 유출을 줄일 수 있기 때문에, 호환 가능한 애플리케이션에서 기본 동작으로 설정하는 것이 유리할 수 있습니다.


## 명세

첫 번째 조각 전달 지시문(First Fragment Delivery Instructions)은 다음과 같이 수정됩니다:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       비트 순서: 76543210
       비트 6-5: 전달 유형
                 0x03 = TUNNELS
       비트 0: 멀티캐스트 여부. 0이면 터널 중 하나에 전달
                              1이면 모든 터널에 전달
                              전달 유형이 TUNNELS가 아닌 경우 향후 사용 호환성을 위해 0으로 설정

Count ::
       1 byte
       선택적, 전달 유형이 TUNNELS일 경우에만 존재
       2-255 - 뒤이어 오는 id/hash 쌍의 수

Tunnel ID :: TunnelId
To Hash ::
       각각 36 bytes
       선택적, 전달 유형이 TUNNELS일 경우에만 존재
       id/hash 쌍

총 길이: 일반적인 길이는 다음과 같음:
       75 bytes (count 2 TUNNELS 전달, 비조각화 터널 메시지);
       79 bytes (count 2 TUNNELS 전달, 첫 번째 조각)

나머지 전달 지시문은 변경 없음
```


## 호환성

새 명세를 이해해야 하는 유일한 피어는 OBGW와 OBEP입니다. 따라서 이 변경을 기존 네트워크와 호환되도록 만들 수 있으며, 사용 여부를 대상 I2P 버전에 따라 조건부로 결정할 수 있습니다:

* OBGW는 인바운드 터널을 구성할 때 [RouterInfo](/docs/specs/common-structures/#routerinfo)에 공표된 I2P 버전을 기반으로 호환 가능한 OBEP를 선택해야 합니다.

* 대상 버전을 공표하는 피어는 새로운 플래그를 파싱할 수 있어야 하며, 지시문을 무효로 거부해서는 안 됩니다.


## 참고 자료

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)

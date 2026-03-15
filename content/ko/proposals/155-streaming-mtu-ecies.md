---
title: "ECIES 목적지를 위한 스트리밍 MTU"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Closed"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## 참고 사항
네트워크 배포 및 테스트 진행 중입니다.  
사소한 수정이 있을 수 있습니다.


## 개요


### 요약

ECIES는 기존 세션(ES) 메시지 오버헤드를 약 90바이트 줄입니다.  
따라서 ECIES 연결의 MTU를 약 90바이트 증가시킬 수 있습니다.  
[ECIES 사양](/docs/specs/ecies/#overhead), [스트리밍 사양](/docs/specs/streaming/#flags-and-option-data-fields), 및 [스트리밍 API 문서](/docs/api/streaming/)를 참조하세요.

MTU를 증가시키지 않으면, 많은 경우 오버헤드 절감 효과가 실제로 '절감'되지 않습니다.  
왜냐하면 메시지가 어차피 두 개의 전체 터널 메시지를 사용하도록 패딩되기 때문입니다.

이 제안은 사양에 대한 변경을 요구하지 않습니다.  
단지 권장 값과 구현 세부 사항에 대한 논의 및 합의를 촉진하기 위해 제안서 형태로 게시되었습니다.


### 목표

- 협상된 MTU 증가
- 1KB 터널 메시지의 사용 극대화
- 스트리밍 프로토콜 변경 없음


## 설계

기존 MAX_PACKET_SIZE_INCLUDED 옵션과 MTU 협상을 사용합니다.  
스트리밍은 계속해서 전송된 MTU와 수신된 MTU 중 작은 값을 사용합니다.  
기본값은 사용된 키와 관계없이 모든 연결에 대해 1730으로 유지됩니다.

구현체는 모든 방향의 모든 SYN 패킷에 MAX_PACKET_SIZE_INCLUDED 옵션을 포함하도록 권장되지만,  
이것은 필수 사항이 아닙니다.

대상이 ECIES 전용인 경우, (앨리스나 밥 모두) 더 높은 값을 사용합니다.  
대상이 이중 키(Dual-key)인 경우, 동작이 달라질 수 있습니다:

이중 키 클라이언트가 라우터 외부에 있는 경우(외부 애플리케이션 내),  
원격 끝에서 사용되는 키를 "알지 못할" 수 있으며, 앨리스는 SYN에서 더 높은 값을 요청할 수 있지만,  
SYN의 최대 데이터는 여전히 1730으로 유지됩니다.

이중 키 클라이언트가 라우터 내부에 있는 경우,  
사용 중인 키 정보가 클라이언트에 알려져 있을 수도 있고 아닐 수도 있습니다.  
leaseset이 아직 가져와지지 않았거나, 내부 API 인터페이스가 해당 정보를 클라이언트에 쉽게 제공하지 않을 수 있기 때문입니다.  
정보가 사용 가능한 경우, 앨리스는 더 높은 값을 사용할 수 있습니다.  
그렇지 않으면, 앨리스는 협상될 때까지 표준 값 1730을 사용해야 합니다.

이중 키 클라이언트가 밥 역할을 하는 경우, 앨리스로부터 값이 없거나 1730의 값이 수신되었더라도  
응답에 더 높은 값을 보낼 수 있습니다.  
그러나 스트리밍에서는 상향 협상에 대한 규정이 없으므로, MTU는 1730으로 유지되어야 합니다.

[스트리밍 API 문서](/docs/api/streaming/)에 설명된 바와 같이,  
앨리스에서 밥으로 전송된 SYN 패킷의 데이터는 밥의 MTU를 초과할 수 있습니다.  
이것은 스트리밍 프로토콜의 약점입니다.  
따라서 이중 키 클라이언트는 더 높은 MTU 옵션을 전송하면서도,  
전송된 SYN 패킷의 데이터를 1730바이트로 제한해야 합니다.  
밥으로부터 더 높은 MTU가 수신되면, 앨리스는 전송되는 실제 최대 페이로드를 증가시킬 수 있습니다.


### 분석

[ECIES 사양](/docs/specs/ecies/#overhead)에 설명된 바와 같이, 기존 세션 메시지의 ElGamal 오버헤드는  
151바이트이며, Ratchet 오버헤드는 69바이트입니다.  
따라서 래칫 연결의 MTU를 (151 - 69) = 82바이트만큼 증가시켜,  
1730에서 1812로 늘릴 수 있습니다.



## 사양

[스트리밍 API 문서](/docs/api/streaming/)의 MTU 선택 및 협상 섹션에 다음 변경 사항과 명확화 사항을 추가합니다.  
[스트리밍 사양](/docs/specs/streaming/)에는 변경 사항이 없습니다.

모든 연결에 대해, 사용된 키와 관계없이 옵션 i2p.streaming.maxMessageSize의 기본값은 1730으로 유지됩니다.  
클라이언트는 기존과 같이 전송된 MTU와 수신된 MTU 중 작은 값을 사용해야 합니다.

관련된 네 가지 MTU 상수 및 변수가 있습니다:

- DEFAULT_MTU: 1730, 모든 연결에 대해 변경 없음
- i2cp.streaming.maxMessageSize: 기본값 1730 또는 1812, 구성에 따라 변경 가능
- ALICE_SYN_MAX_DATA: 앨리스가 SYN 패킷에 포함할 수 있는 최대 데이터
- negotiated_mtu: 앨리스와 밥의 MTU 중 작은 값. 밥에서 앨리스로 보내는 SYN ACK 및 이후 양방향으로 전송되는 모든 패킷에서 최대 데이터 크기로 사용됨


다섯 가지 경우를 고려해야 합니다:


### 1) 앨리스가 ElGamal 전용인 경우
변경 없음, 모든 패킷에서 1730 MTU.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize 기본값: 1730
- 앨리스는 SYN에 MAX_PACKET_SIZE_INCLUDED를 전송할 수 있음. 1730과 다를 경우에만 필수


### 2) 앨리스가 ECIES 전용인 경우
모든 패킷에서 1812 MTU.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize 기본값: 1812
- 앨리스는 반드시 SYN에 MAX_PACKET_SIZE_INCLUDED를 전송해야 함


### 3) 앨리스가 이중 키이며 밥이 ElGamal임을 아는 경우
모든 패킷에서 1730 MTU.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize 기본값: 1812
- 앨리스는 SYN에 MAX_PACKET_SIZE_INCLUDED를 전송할 수 있음. 1730과 다를 경우에만 필수


### 4) 앨리스가 이중 키이며 밥이 ECIES임을 아는 경우
모든 패킷에서 1812 MTU.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize 기본값: 1812
- 앨리스는 반드시 SYN에 MAX_PACKET_SIZE_INCLUDED를 전송해야 함


### 5) 앨리스가 이중 키이며 밥의 키를 알 수 없는 경우
SYN 패킷에서 MAX_PACKET_SIZE_INCLUDED로 1812를 전송하지만, SYN 패킷 데이터는 1730으로 제한.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize 기본값: 1812
- 앨리스는 반드시 SYN에 MAX_PACKET_SIZE_INCLUDED를 전송해야 함


### 모든 경우에 대해

앨리스와 밥은 negotiated_mtu를 계산합니다. 이는 앨리스와 밥의 MTU 중 작은 값이며,  
밥에서 앨리스로 보내는 SYN ACK 및 이후 양방향으로 전송되는 모든 패킷에서 최대 데이터 크기로 사용됩니다.




## 정당성

현재 값이 1730인 이유는 [Java I2P 소스 코드](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)를 참조하세요.  
ECIES 오버헤드가 ElGamal보다 82바이트 적은 이유는 [ECIES 사양](/docs/specs/ecies/#overhead)을 참조하세요.



## 구현 노트

스트리밍이 최적 크기의 메시지를 생성하는 경우,  
ECIES-Ratchet 계층이 그 크기를 초과하여 패딩하지 않는 것이 매우 중요합니다.

두 개의 터널 메시지에 맞는 최적의 Garlic 메시지 크기는,  
16바이트 Garlic 메시지 I2NP 헤더, 4바이트 Garlic 메시지 길이, 8바이트 ES 태그, 16바이트 MAC를 포함하여 1956바이트입니다.

ECIES에서 권장되는 패딩 알고리즘은 다음과 같습니다:

- Garlic 메시지의 총 길이가 1954-1956바이트가 될 경우, 패딩 블록을 추가하지 마십시오(공간 없음)
- Garlic 메시지의 총 길이가 1938-1953바이트가 될 경우, 정확히 1956바이트로 패딩하기 위해 패딩 블록을 추가하십시오.
- 그 외의 경우, 예를 들어 0-15바이트의 임의량으로 일반적인 방식으로 패딩하십시오.

유사한 전략은 최적의 단일 터널 메시지 크기(964)와 세 터널 메시지 크기(2952)에도 사용할 수 있지만,  
이러한 크기는 실제로 드물게 발생할 것입니다.



## 이슈

1812 값은 임시입니다. 확인 후 조정될 수 있습니다.




## 마이그레이션

하위 호환성 문제 없음.  
이것은 기존 옵션이며 MTU 협상은 이미 사양의 일부입니다.

이전 ECIES 대상은 1730을 지원합니다.  
더 높은 값을 수신하는 클라이언트는 1730으로 응답하며, 원격 끝은 기존과 같이 하향 협상합니다.


## 참고 자료

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)

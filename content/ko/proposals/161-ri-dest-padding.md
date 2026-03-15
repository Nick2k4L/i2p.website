---
title: "RI 및 목적지 패딩"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Open"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## 상태

0.9.57 버전에서 구현됨.  
"향후 계획(Future Planning)" 섹션의 아이디어를 향상시키고 논의하기 위해 이 제안서를 열어 둡니다.


## 개요


### 요약

Destination의 ElGamal 공개 키는 릴리스 0.6(2005년) 이후로 사용되지 않았습니다.  
사양 문서에서는 이 키가 사용되지 않는다고 명시하고 있지만, **구현체가 ElGamal 키 쌍을 생성하지 않고 해당 필드를 임의의 데이터로 채워도 된다고 명시하지는 않습니다**.

우리는 사양을 다음과 같이 변경할 것을 제안합니다:  
해당 필드는 무시되며, 구현체는 해당 필드를 임의의 데이터로 채울 수 있다(MAY).  
이 변경은 하위 호환성이 보장됩니다. ElGamal 공개 키를 검증하는 것으로 알려진 구현체는 없습니다.

또한, 이 제안서는 Destination과 Router Identity의 패딩을 생성할 때 압축이 잘 되면서도 보안을 유지하고, Base64 표현에서 손상되거나 불안정해 보이지 않도록 하는 방법에 대한 지침을 제공합니다.  
이를 통해 프로토콜에 중대한 변경 없이도 패딩 필드를 제거하는 것과 유사한 이점을 대부분 얻을 수 있습니다.  
압축 가능한 Destination은 스트리밍 SYN 및 응답 가능한 데이터그램의 크기를 줄이며,  
압축 가능한 Router Identity는 Database Store 메시지, SSU2 Session Confirmed 메시지, reseed su3 파일의 크기를 줄입니다.

마지막으로, 패딩을 완전히 제거하는 새로운 Destination 및 Router Identity 형식에 대한 가능성을 논의합니다.  
또한 포스트-양자 암호(Post-quantum crypto)와 향후 계획에 미칠 영향에 대한 간략한 논의도 포함됩니다.



### 목표

- Destination 생성 시 ElGamal 키 쌍 생성 요구 제거
- Destination과 Router Identity가 압축이 잘 되고, Base64 표현에서 명백한 패턴이 드러나지 않도록 하는 모범 사례 권장
- 모든 구현체가 모범 사례를 채택하여 해당 필드가 구별되지 않도록 유도
- 스트리밍 SYN 크기 감소
- 응답 가능한 데이터그램 크기 감소
- SSU2 RI 블록 크기 감소
- SSU2 Session Confirmed 크기 및 단편화 빈도 감소
- Database Store 메시지(리더 포함) 크기 감소
- reseed 파일 크기 감소
- 모든 프로토콜 및 API에서 호환성 유지
- 사양 업데이트
- 새로운 Destination 및 Router Identity 형식에 대한 대안 논의

ElGamal 키 생성 요구를 제거함으로써, 다른 프로토콜의 하위 호환성 고려 사항에 따라 구현체가 ElGamal 코드를 완전히 제거할 수 있게 될 수 있습니다.



## 설계

엄밀히 말하면, Destination과 Router Identity 모두에 포함된 32바이트 서명 공개 키와, Router Identity에만 포함된 32바이트 암호화 공개 키는 랜덤 숫자이며, 이러한 구조의 SHA-256 해시가 네트워크 데이터베이스 DHT에서 암호학적으로 강력하고 무작위 분포되도록 하는 데 필요한 모든 엔트로피를 제공합니다.

그러나 과도한 주의를 기울여, ElGamal 공개 키 필드와 패딩에는 최소한 32바이트의 난수 데이터를 사용할 것을 권장합니다. 또한, 해당 필드가 모두 0인 경우 Base64로 인코딩된 Destination에 장시간 AAAA 문자가 반복되어 사용자에게 경각심이나 혼란을 줄 수 있습니다.

Ed25519 서명 유형과 X25519 암호화 유형의 경우:  
Destination은 난수 데이터를 11번 반복(352바이트) 포함합니다.  
Router Identity는 난수 데이터를 10번 반복(320바이트) 포함합니다.



### 예상 절감 효과

Destination은 모든 스트리밍 SYN 및 응답 가능한 데이터그램에 포함됩니다.  
Router Info(RI, Router Identity 포함)는 Database Store 메시지와 NTCP2 및 SSU2의 Session Confirmed 메시지에 포함됩니다.

NTCP2는 Router Info를 압축하지 않습니다.  
Database Store 메시지와 SSU2 Session Confirmed 메시지의 RI는 gzip으로 압축됩니다.  
Router Info는 reseed SU3 파일에서 zip으로 압축됩니다.

Database Store 메시지에 포함된 Destination은 압축되지 않습니다.  
스트리밍 SYN 메시지는 I2CP 계층에서 gzip으로 압축됩니다.

Ed25519 서명 유형과 X25519 암호화 유형의 경우 예상 절감 효과:

| 데이터 유형 | 총 크기 | 키 및 인증서 | 비압축 패딩 | 압축된 패딩 | 크기 | 절감 효과 |
|-----------|------------|---------------|----------------------|--------------------|------|---------|
| Destination | 391 | 39 | 352 | 32 | 71 | 320바이트 (82%) |
| Router Identity | 391 | 71 | 320 | 32 | 103 | 288바이트 (74%) |
| Router Info | 1000 일반적 | 71 | 320 | 32 | 722 일반적 | 288바이트 (29%) |

비고: 7바이트 인증서는 압축되지 않는다고 가정하며, 추가 gzip 오버헤드는 없다고 가정.  
둘 다 정확하지 않지만 영향은 미미함.  
Router Info의 다른 압축 가능한 부분은 무시함.



## 사양

현재 사양에 대한 제안된 변경 사항은 아래에 문서화되어 있습니다.


### 공통 구조
공통 구조 사양을 변경하여, 256바이트 Destination 공개 키 필드는 무시되며 임의의 데이터를 포함할 수 있다고 명시합니다.

다음과 같이 Destination 공개 키 필드와 Destination 및 Router Identity의 패딩 필드에 대한 모범 사례를 권장하는 섹션을 공통 구조 사양에 추가합니다:

강력한 암호학적 의사난수 생성기(PRNG)를 사용해 32바이트의 난수 데이터를 생성하고, 이를 Destination의 공개 키 필드와 Destination 및 Router Identity의 패딩 필드를 채우기 위해 필요한 만큼 반복합니다.


### 개인 키 파일
개인 키 파일(eepPriv.dat) 형식은 공식 사양의 일부는 아니지만, [Java I2P javadocs](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html) 및 기타 구현체에서 문서화되어 있으며 지원하고 있습니다.  
이는 개인 키를 다른 구현체로 이식 가능하게 합니다.  
해당 javadoc에 다음과 같은 주석을 추가합니다: 암호화 공개 키는 임의의 패딩일 수 있으며, 암호화 개인 키는 모두 0이거나 임의의 데이터일 수 있다.


### SAM
SAM 사양에 암호화 개인 키는 사용되지 않으며 무시될 수 있다고 주석을 추가합니다.  
클라이언트는 임의의 데이터를 반환할 수 있습니다.  
SAM 브리지는 생성 시(DEST GENERATE 또는 SESSION CREATE DESTINATION=TRANSIENT) 모두 0 대신 임의의 데이터를 전송하여, Base64 표현에서 AAAA 문자열이 반복되어 손상된 것처럼 보이는 것을 방지할 수 있습니다.


### I2CP
I2CP에 대한 변경은 필요 없습니다. Destination의 암호화 공개 키에 대한 개인 키는 라우터로 전송되지 않습니다.


## 향후 계획


### 프로토콜 변경

프로토콜 변경과 하위 호환성 상실을 감수한다면, Destination, Router Identity 또는 둘 다의 패딩 필드를 제거하기 위해 프로토콜과 사양을 변경할 수 있습니다.

이 제안은 키와 타입 필드만 포함하는 "b33" 암호화 leaseset 형식과 다소 유사합니다.

일부 호환성을 유지하기 위해, 특정 프로토콜 계층이 다른 계층에 제공할 때 패딩 필드를 0으로 "확장(expand)"할 수 있습니다.

Destination의 경우, 키 인증서에서 암호화 유형 필드를 제거하여 2바이트를 절약할 수 있습니다.  
또는, 공개 키(및 패딩)가 0임을 나타내는 새로운 암호화 유형을 Destination에 도입할 수 있습니다.

이전 형식과 새로운 형식 간의 호환성 변환이 어떤 프로토콜 계층에서도 포함되지 않는다면, 다음 사양, API, 프로토콜 및 애플리케이션이 영향을 받습니다:

- 공통 구조 사양
- I2NP
- I2CP
- NTCP2
- SSU2
- Ratchet
- 스트리밍
- SAM
- BitTorrent
- 리시딩(reseeding)
- 개인 키 파일
- Java 코어 및 라우터 API
- i2pd API
- 타사 SAM 라이브러리
- 번들 및 타사 도구
- 여러 Java 플러그인
- 사용자 인터페이스
- P2P 애플리케이션 예: MuWire, 비트코인, 모네로
- hosts.txt, 주소록, 구독

어떤 계층에서 변환이 정의된다면, 영향을 받는 항목 목록은 줄어들 수 있습니다.

이러한 변경의 비용과 이점은 명확하지 않습니다.

구체적인 제안은 미정(TBD):





### PQ 키

예상되는 어떤 알고리즘의 포스트-양자(PQ) 암호화 공개 키도 256바이트보다 큽니다. 이는 Router Identity의 모든 패딩과 위에서 제안된 변경으로 인한 절감 효과를 무효화합니다.

SSL이 하고 있는 것처럼 "하이브리드(hybrid)" PQ 접근 방식에서는 PQ 키는 일시적(ephemeral)이며, Router Identity에는 나타나지 않습니다.

PQ 서명 키는 실현 가능하지 않으며, Destination은 암호화 공개 키를 포함하지 않습니다.  
래칫(ratchet)의 정적 키는 Lease Set에 있으며 Destination에는 없습니다.  
따라서 다음 논의에서 Destination은 제외할 수 있습니다.

따라서 PQ는 Router Info에만 영향을 미치며, PQ 정적 키(일시적이 아닌)에만 해당하며, 하이브리드 PQ에는 해당하지 않습니다.  
이는 새로운 암호화 유형이 필요하며 NTCP2, SSU2, 암호화된 Database Lookup 메시지 및 응답에 영향을 줍니다.  
이 설계, 개발 및 배포의 예상 시기는 ????????  
하지만 하이브리드 또는 래칫 이후 ????????????

추가 논의는 [이 주제](http://zzz.i2p/topics/3294)를 참조하십시오.




## 이슈

새로운 라우터를 위한 커버를 제공하기 위해 천천히 네트워크를 재키(rekey)하는 것이 바람직할 수 있습니다.  
"재키"는 실제로 키를 변경하는 것이 아니라 단순히 패딩을 변경하는 것을 의미할 수 있습니다.

기존 Destination은 재키할 수 없습니다.

공개 키 필드에 패딩이 있는 Router Identity는 키 인증서에서 다른 암호화 유형으로 식별되어야 할까요? 이는 호환성 문제를 일으킬 수 있습니다.




## 마이그레이션

ElGamal 키를 패딩으로 대체하는 데는 하위 호환성 문제가 없습니다.

재키가 구현된다면, 이전 세 번의 라우터 ID 전환과 유사할 것입니다:  
DSA-SHA1에서 ECDSA 서명으로, 그 다음 EdDSA 서명으로, 그 다음 X25519 암호화로 전환한 것과 같습니다.

하위 호환성 문제에 따라, SSU를 비활성화한 후 구현체는 ElGamal 코드를 완전히 제거할 수 있습니다.  
네트워크의 약 14%의 라우터가 ElGamal 암호화 유형이며, 많은 플러드필(floodfill)이 포함되어 있습니다.

Java I2P용 초안 병합 요청은 [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)에 있습니다.


## 참고 자료

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)

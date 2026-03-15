---
title: "암호화된 LeaseSet"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Rejected"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## 개요

이 제안은 LeaseSet을 암호화하는 메커니즘을 재설계하는 것에 관한 것이다.


## 동기

현재 암호화된 LS는 끔찍하고 안전하지 않다. 나는 그것을 설계하고 구현했기 때문에 그렇게 말할 수 있다.

이유들:

- AES CBC 암호화
- 모든 사람에게 단일 AES 키
- 임대 만기仍然 노출
- 암호화 공개 키仍然 노출


## 설계

### 목표

- 전체를 불투명하게 만들기
- 각 수신자에 대한 키


### 전략

GPG/OpenPGP가 하는 것처럼 하자. 각 수신자에 대한 대칭 키를 비대칭으로 암호화한다. 데이터는 그 비대칭 키로 복호화된다. 예를 들어, [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)을 참조하라. 만약 작은 크기와 빠른 알고리즘을 찾을 수 있다면.

비밀은 작은 크기와 빠른 비대칭 암호화를 찾는 것이다. 514바이트의 ElGamal은 여기서 조금 고통스럽다. 우리는 더 잘할 수 있다.

예를 들어, http://security.stackexchange.com/questions/824...를 참조하라.

이 방법은 수신자(또는 실제로 키)의 작은 숫자에 대해 작동한다. 당신이喜欢的话, 여전히 여러 사람에게 키를 배포할 수 있다.


## 명세

- 목적지
- 게시된 타임스탬프
- 만기
- 플래그
- 데이터 길이
- 암호화된 데이터
- 서명

암호화된 데이터는 enctype 지정자로 접두사가 될 수 있다.


## 참고문헌

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)

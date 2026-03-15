---
title: "소개자 만료"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Closed"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## 개요

이 제안은 소개(introduction) 성공률을 향상시키는 것을 목표로 한다.


## 동기

소개자(introducer)는 일정 시간 후 만료되지만, 이 정보는 라우터 정보(Router Info)에 공개되지 않는다. 현재 라우터들은 소개자가 더 이상 유효하지 않을 시점을 추정하기 위해 휴리스틱을 사용해야 한다.


## 설계

SSU 라우터 주소에 소개자가 포함된 경우, 게시자는 각 소개자에 대해 선택적으로 만료 시간을 포함할 수 있다.


## 명세

```
iexp{X}={nnnnnnnnnn}

X :: 소개자 번호 (0-2)

nnnnnnnnnn :: 에포크 이후 경과한 시간(초 단위, 밀리초 아님).
```

### 참고 사항

* 각 만료 시간은 라우터 정보(Router Info)의 게시일보다 커야 하며, 게시일로부터 6시간 이내여야 한다.

* 게시 라우터와 소개자는 만료 시간까지 소개자가 유효하도록 유지하려 시도해야 하지만, 이를 보장할 방법은 없다.

* 라우터는 소개자의 만료 이후에는 게시된 소개자를 사용해서는 안 된다.

* 소개자 만료 시간은 라우터 주소 매핑(Router Address mapping)에 포함된다. 이는 현재 사용되지 않는 라우터 주소 내 8바이트 만료 필드와는 별개이다.

**예시:** `iexp0=1486309470`


## 마이그레이션

문제 없음. 구현은 선택 사항이다.  
이전 버전과의 호환성은 보장되며, 이전 라우터들은 알 수 없는 매개변수를 무시할 것이다.


## 참고 자료

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)

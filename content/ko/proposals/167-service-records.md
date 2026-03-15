---
title: "LS2의 서비스 기록"
number: "167"
author: "zzz, orignal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Closed"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## 상태
2025-04-01에 2차 검토 시 승인됨; 사양은 업데이트됨; 아직 구현되지 않음.


## 개요

I2P는 중앙 집중식 DNS 시스템을 갖추고 있지 않습니다.  
그러나 주소록과 b32 호스트명 시스템을 함께 사용하면  
라우터가 전체 목적지를 조회하고 리스 세트(leaseSet)를 가져올 수 있으며,  
이 리스 세트에는 게이트웨이 및 키 목록이 포함되어 있어 클라이언트가 해당 목적지에 연결할 수 있습니다.

따라서 리스 세트는 어느 정도 DNS 레코드와 유사합니다.  
그러나 현재로서는 DNS [SRV 레코드](https://en.wikipedia.org/wiki/SRV_record)처럼,  
특정 호스트가 해당 목적지 또는 다른 목적지에서 어떤 서비스를 지원하는지 확인할 수 있는 기능은 존재하지 않습니다.  
이는 [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782)에서 정의된 바와 같습니다.

이 기능의 첫 번째 응용 사례는 피어 투 피어 이메일일 수 있습니다.  
기타 가능한 응용 분야: DNS, GNS, 키 서버, 인증 기관, 시간 서버,  
비트토렌트, 암호화폐, 기타 피어 투 피어 응용 프로그램.


## 관련 제안 및 대안

### 서비스 목록

LS2 [제안 123](/proposals/123-new-netdb-entries/)에서는 목적지가 글로벌 서비스에 참여하고 있음을 나타내는 '서비스 레코드'를 정의했습니다.  
플러드필(floodfill)은 이러한 레코드를 수집하여 글로벌 '서비스 목록'으로 집계했습니다.  
그러나 복잡성, 인증 부재, 보안 및 스팸 문제로 인해 이 기능은 구현되지 않았습니다.

이 제안은 글로벌 서비스를 위한 글로벌 목적지 풀을 제공하는 것이 아니라,  
특정 목적지에 대한 서비스 조회를 제공한다는 점에서 다릅니다.

### GNS

GNS는 모든 사용자가 자체 DNS 서버를 운영할 것을 제안합니다.  
이 제안은 보완적인데, 표준 서비스 이름 "domain"과 포트 53을 사용하여  
GNS(또는 DNS)가 지원됨을 나타내는 서비스 레코드를 사용할 수 있기 때문입니다.

### Dot well-known

[제안된 바](http://i2pforum.i2p/viewtopic.php?p=3102)에 따르면, 서비스는  
`/.well-known/i2pmail.key`로의 HTTP 요청을 통해 조회될 수 있습니다.  
이 방법은 모든 서비스가 키를 호스팅하는 관련 웹사이트를 운영해야 하므로,  
대부분의 사용자가 웹사이트를 운영하지 않는 한 현실성이 떨어집니다.

한 가지 우회 방법은 b32 주소에 대한 서비스가 실제로 그 b32 주소에서 실행되고 있다고 가정하는 것입니다.  
예를 들어, example.i2p에 대한 서비스를 찾을 때는  
`http://example.i2p/.well-known/i2pmail.key`에서 HTTP를 가져와야 하지만,  
aaa...aaa.b32.i2p에 대한 서비스는 조회 없이 바로 연결할 수 있습니다.

하지만 example.i2p도 b32로 주소 지정이 가능하므로 모호성이 존재합니다.

### MX 레코드

SRV 레코드는 모든 서비스에 대한 일반적인 버전의 MX 레코드일 뿐입니다.  
"_smtp._tcp"는 "MX" 레코드입니다.  
SRV 레코드가 있다면 MX 레코드는 필요 없으며, MX 레코드만으로는 모든 서비스에 대한 일반 레코드를 제공하지 못합니다.


## 설계

서비스 레코드는 [LS2](/docs/specs/common-structures/)의 옵션 섹션에 배치됩니다.  
LS2 옵션 섹션은 현재 사용되지 않고 있습니다.  
LS1에서는 지원되지 않습니다.  
이는 터널 빌드 레코드에 대한 옵션을 정의하는 [터널 대역폭 제안](/proposals/168-tunnel-bandwidth/)과 유사합니다.

특정 호스트명 또는 b32에 대한 서비스 주소를 조회하려면, 라우터는 리스 세트를 가져와 속성에서 서비스 레코드를 찾습니다.

해당 서비스는 리스 세트 자체와 동일한 목적지에서 호스팅되거나, 다른 호스트명/b32를 참조할 수 있습니다.

서비스의 대상 목적지가 다른 경우, 대상 리스 세트도 해당 서비스를 지원함을 나타내는 자기 자신을 가리키는 서비스 레코드를 포함해야 합니다.

이 설계는 플러드필에서 특별한 지원, 캐싱 또는 변경이 필요하지 않습니다.  
리스 세트 게시자와 서비스 레코드를 조회하는 클라이언트만 이러한 변경을 지원하면 됩니다.

클라이언트가 서비스 레코드를 검색할 수 있도록 하기 위해 소규모의 I2CP 및 SAM 확장이 제안됩니다.



## 사양

### LS2 옵션 사양

LS2 옵션은 키 순으로 정렬되어야 하므로 서명이 불변합니다.

다음과 같이 정의됩니다:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := 원하는 서비스의 기호 이름. 소문자여야 함. 예: "smtp".  
  허용되는 문자는 [a-z0-9-]이며, '-'로 시작하거나 끝나서는 안 됩니다.  
  [DNS-SD Service Types registry](http://www.dns-sd.org/ServiceTypes.html) 또는 Linux /etc/services에 정의된 경우 표준 식별자를 사용해야 합니다.
- proto := 원하는 서비스의 전송 프로토콜. 소문자이며, "tcp" 또는 "udp" 중 하나여야 함.  
  "tcp"는 스트리밍을 의미하고, "udp"는 응답 가능한 데이터그램을 의미합니다.  
  raw 데이터그램 및 datagram2에 대한 프로토콜 지시자는 나중에 정의될 수 있습니다.  
  허용되는 문자는 [a-z0-9-]이며, '-'로 시작하거나 끝나서는 안 됩니다.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := 생존 시간(time to live), 정수 초. 양의 정수. 예: "86400".  
  최소 86400(하루) 이상을 권장하며, 자세한 내용은 아래의 권장 사항 섹션을 참조하세요.
- priority := 대상 호스트의 우선순위. 값이 작을수록 더 선호됨. 음이 아닌 정수. 예: "0"  
  레코드가 여러 개인 경우에만 유용하지만, 단일 레코드일 경우에도 필수입니다.
- weight := 동일한 우선순위를 가진 레코드 간의 상대적 가중치. 값이 클수록 선택될 확률이 높음. 음이 아닌 정수. 예: "0"  
  레코드가 여러 개인 경우에만 유용하지만, 단일 레코드일 경우에도 필수입니다.
- port := 서비스가 위치한 I2CP 포트. 음이 아닌 정수. 예: "25"  
  포트 0도 지원되지만 권장되지 않습니다.
- target := 서비스를 제공하는 목적지의 호스트명 또는 b32. 유효한 [호스트명](/docs/overview/naming/). 소문자여야 함.  
  예: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" 또는 "example.i2p".  
  공식 또는 기본 주소록에 있는 "잘 알려진" 호스트명이 아닌 한 b32 사용을 권장합니다.
- appoptions := 애플리케이션별 임의 텍스트. " " 또는 ","를 포함해서는 안 됨. 인코딩은 UTF-8.

### 예시

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p에 대한 LS2에서 하나의 SMTP 서버를 가리키는 경우:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p에 대한 LS2에서 두 개의 SMTP 서버를 가리키는 경우:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p에 대한 LS2에서 자기 자신을 SMTP 서버로 가리키는 경우:

    "_smtp._tcp" "0 999999 25"

이메일 리디렉션을 위한 가능한 형식 (아래 참조):

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### 제한 사항

LS2 옵션에 사용되는 매핑 데이터 구조 형식은 키와 값의 최대 길이를 255바이트(문자가 아님)로 제한합니다.  
b32 대상을 사용할 경우 optionvalue는 약 67바이트이므로, 3개의 레코드만 들어갈 수 있습니다.  
긴 appoptions 필드가 있는 경우 하나 또는 두 개만 가능하며, 짧은 호스트명의 경우 최대 4~5개까지 가능합니다.  
이 정도면 충분할 것으로 보이며, 다중 레코드는 드물 것입니다.


### RFC 2782과의 차이점

- 후행 점 없음
- proto 뒤에 이름 없음
- 소문자 필수
- 이진 DNS 형식이 아닌, 쉼표로 구분된 텍스트 형식
- 다른 레코드 유형 지시자
- 추가적인 appoptions 필드


### 참고 사항

(별표), (별표)._tcp, 또는 _tcp와 같은 와일드카드는 허용되지 않습니다.  
지원되는 각 서비스는 자체 레코드를 가져야 합니다.



### 서비스 이름 레지스트리

[DNS-SD Service Types registry](http://www.dns-sd.org/ServiceTypes.html) 또는 Linux /etc/services에 나열되지 않은 비표준 식별자는  
[공통 구조 사양](/docs/specs/common-structures/)에 요청 및 추가될 수 있습니다.

서비스별 appoptions 형식도 그곳에 추가될 수 있습니다.


### I2CP 사양

[I2CP 프로토콜](/docs/specs/i2cp/)은 서비스 조회를 지원하도록 확장되어야 합니다.  
서비스 조회와 관련된 추가적인 MessageStatusMessage 및/또는 HostReplyMessage 오류 코드가 필요합니다.  
조회 기능을 서비스 레코드 전용이 아닌 일반적으로 사용 가능하게 하기 위해,  
모든 LS2 옵션의 검색을 지원하는 설계입니다.

구현: HostLookupMessage를 확장하여 해시, 호스트명, 목적지에 대한 LS2 옵션 요청을 추가합니다(요청 유형 2-4).  
HostReplyMessage를 확장하여 요청 시 옵션 매핑을 포함합니다.  
추가 오류 코드를 위해 HostReplyMessage를 확장합니다.

옵션 매핑은 클라이언트 또는 라우터 측에서 일시적으로 캐시 또는 네거티브 캐시될 수 있으며, 구현에 따라 다릅니다.  
권장 최대 시간은 한 시간이며, 서비스 레코드 TTL이 더 짧은 경우를 제외합니다.  
서비스 레코드는 애플리케이션, 클라이언트 또는 라우터에서 지정한 TTL까지 캐시될 수 있습니다.

다음과 같이 사양을 확장합니다:

#### 구성 옵션

[I2CP 구성 옵션](/docs/specs/i2cp/)에 다음을 추가합니다.

i2cp.leaseSetOption.nnn

리스 세트에 포함될 옵션. LS2에서만 사용 가능.  
nnn은 0부터 시작. 옵션 값은 "key=value"를 포함합니다.  
(따옴표 포함하지 마세요)

예:
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### HostLookup 메시지

- 조회 유형 2: 해시 조회, 옵션 매핑 요청
- 조회 유형 3: 호스트명 조회, 옵션 매핑 요청
- 조회 유형 4: 목적지 조회, 옵션 매핑 요청

조회 유형 4의 경우, 항목 5는 Destination입니다.



#### HostReply 메시지

조회 유형 2-4의 경우, 라우터는 조회 키가 주소록에 있더라도 리스 세트를 가져와야 합니다.

성공 시, HostReply는 리스 세트의 옵션 매핑을 포함하며, 목적지 뒤에 항목 5로 포함됩니다.  
매핑에 옵션이 없거나 리스 세트가 버전 1인 경우에도 빈 매핑(두 바이트: 0 0)으로 포함됩니다.  
리스 세트의 모든 옵션이 포함되며, 서비스 레코드 옵션만 포함되는 것은 아닙니다.  
예를 들어, 미래에 정의될 매개변수에 대한 옵션도 포함될 수 있습니다.

리스 세트 조회 실패 시, 응답은 새로운 오류 코드 6(Leaseset lookup failure)을 포함하며 매핑을 포함하지 않습니다.  
오류 코드 6이 반환되면 Destination 필드는 존재할 수도 있고 아닐 수도 있습니다.  
주소록에서의 호스트명 조회가 성공했거나, 이전 조회가 성공하여 결과가 캐시되었거나,  
조회 메시지에 Destination이 포함된 경우(조회 유형 4) 존재합니다.

조회 유형이 지원되지 않는 경우, 응답은 새로운 오류 코드 7(lookup type unsupported)을 포함합니다.



### SAM 사양

[SAMv3 프로토콜](/docs/api/samv3/)은 서비스 조회를 지원하도록 확장되어야 합니다.

다음과 같이 NAMING LOOKUP을 확장합니다:

NAMING LOOKUP NAME=example.i2p OPTIONS=true는 응답에 옵션 매핑을 요청합니다.

OPTIONS=true일 때 NAME은 전체 base64 목적지일 수 있습니다.

목적지 조회가 성공하고 리스 세트에 옵션이 있는 경우, 응답에서 목적지 다음에  
OPTION:key=value 형식의 하나 이상의 옵션이 포함됩니다.  
각 옵션은 별도의 OPTION: 접두사를 가집니다.  
리스 세트의 모든 옵션이 포함되며, 서비스 레코드 옵션만 포함되는 것은 아닙니다.  
예를 들어, 미래에 정의될 매개변수에 대한 옵션도 포함될 수 있습니다.  
예:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

'='을 포함하는 키, 또는 개행 문자를 포함하는 키 또는 값은 유효하지 않으며, 키/값 쌍은 응답에서 제거됩니다.

리스 세트에서 옵션이 발견되지 않았거나 리스 세트가 버전 1인 경우, 응답은 옵션을 포함하지 않습니다.

조회에 OPTIONS=true가 포함되었고 리스 세트를 찾을 수 없는 경우, 새로운 결과 값 LEASESET_NOT_FOUND가 반환됩니다.


## 이름 조회 대안

서비스를 전체 호스트명으로 조회하는 것을 지원하기 위한 대안 설계가 고려되었습니다.  
예를 들어 _smtp._tcp.example.i2p와 같은 형식이며,  
[이름 지정 사양](/docs/overview/naming/)을 업데이트하여 '_'로 시작하는 호스트명을 처리하도록 지정하는 방식입니다.  
이 방식은 두 가지 이유로 거부되었습니다:

- I2CP 및 SAM 변경이 여전히 필요하여 TTL 및 포트 정보를 클라이언트에 전달해야 합니다.
- 미래에 정의될 수 있는 다른 LS2 옵션을 검색할 수 있는 일반적인 기능이 되지 못합니다.


## 권장 사항

서버는 애플리케이션의 표준 포트와 함께 최소 86400의 TTL을 지정해야 합니다.



## 고급 기능

### 재귀 조회

DNS 방식처럼 각 후속 리스 세트를 검사하여 다른 리스 세트를 가리키는 서비스 레코드를 찾는 재귀 조회를 지원하는 것이 바람직할 수 있습니다.  
초기 구현에서는 아마도 필요하지 않을 것입니다.

TODO



### 애플리케이션별 필드

서비스 레코드에 애플리케이션별 데이터가 있는 것이 바람직할 수 있습니다.  
예를 들어, example.i2p 운영자는 이메일을 example@mail.i2p로 전달해야 한다고 표시하고자 할 수 있습니다.  
"example@" 부분은 서비스 레코드의 별도 필드에 있어야 하거나, 대상에서 제거되어야 합니다.

운영자가 자체 이메일 서비스를 운영하더라도, 이메일을 example@example.i2p로 보내야 한다고 표시하고자 할 수 있습니다.  
대부분의 I2P 서비스는 한 사람에 의해 운영됩니다.  
따라서 별도의 필드가 여기에서도 유용할 수 있습니다.

TODO 이를 일반적인 방식으로 수행하는 방법


### 이메일을 위한 변경 사항

이 제안의 범위를 벗어납니다. 자세한 내용은 [i2pforum 토론](http://i2pforum.i2p/viewtopic.php?p=3102)을 참조하세요.


## 구현 노트

서비스 레코드는 TTL까지 라우터 또는 애플리케이션에 의해 캐시될 수 있으며, 구현에 따라 다릅니다.  
지속적 캐시 여부도 구현에 따라 다릅니다.

조회는 대상 리스 세트를 조회하고, 클라이언트에게 대상 목적지를 반환하기 전에  
그 안에 "self" 레코드가 포함되어 있는지 확인해야 합니다.


## 보안 분석

리스 세트는 서명되어 있으므로, 그 안의 서비스 레코드는 목적지의 서명 키에 의해 인증됩니다.

서비스 레코드는 리스 세트가 암호화되지 않는 한 공개되며 플러드필에서 볼 수 있습니다.  
리스 세트를 요청하는 모든 라우터는 서비스 레코드를 볼 수 있습니다.

"self"가 아닌 SRV 레코드(즉, 다른 호스트명/b32 대상을 가리키는 레코드)는  
대상 호스트명/b32의 동의를 요구하지 않습니다.  
임의의 목적지로 서비스를 리디렉션하는 것이 어떤 공격을 가능하게 할 수 있는지, 또는 그러한 공격의 목적은 무엇인지 명확하지 않습니다.  
그러나 이 제안은 대상 리스 세트에 "self" SRV 레코드를 게시하도록 요구함으로써 이러한 공격을 완화합니다.  
구현자는 대상 리스 세트의 "self" 레코드를 확인해야 합니다.


## 호환성

LS2: 문제 없음. 알려진 모든 구현은 현재 LS2의 옵션 필드를 무시하며, 비어 있지 않은 옵션 필드를 올바르게 건너뜁니다.  
이것은 LS2 개발 중 Java I2P와 i2pd 모두에 의해 테스트로 확인되었습니다.  
LS2는 2016년 0.9.38에서 구현되었으며 모든 라우터 구현에서 잘 지원됩니다.  
이 설계는 플러드필에서 특별한 지원, 캐싱 또는 변경을 요구하지 않습니다.

이름 지정: '_'는 i2p 호스트명에서 유효한 문자가 아닙니다.

I2CP: 최소 API 버전(미정) 이하의 라우터에는 조회 유형 2-4를 전송해서는 안 됩니다.

SAM: Java SAM 서버는 OPTIONS=true와 같은 추가 키/값을 무시합니다.  
i2pd도 마찬가지로 무시해야 하며, 검증 예정입니다.  
SAM 클라이언트는 OPTIONS=true로 요청하지 않으면 응답에서 추가 값을 받지 못합니다.  
버전 업그레이드는 필요하지 않습니다.


## 마이그레이션

I2CP 변경에 대한 효과적인 API 버전에 대한 합의를 제외하고는 언제든지 구현이 지원을 추가할 수 있으며, 조정이 필요하지 않습니다.  
각 구현의 SAM 호환성 버전은 SAM 사양에 문서화될 것입니다.


## 참고 자료

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)

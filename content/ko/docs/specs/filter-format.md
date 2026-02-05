---
title: "접근 필터 형식"
description: "tunnel 접근 제어 필터 파일 구문"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## 개요

필터의 정의는 문자열 목록입니다. 빈 줄과 `#`으로 시작하는 줄은 무시됩니다. 필터 정의의 변경 사항은 tunnel 재시작 시 적용됩니다.

각 줄은 다음 항목 중 하나를 나타낼 수 있습니다:

- 이 파일이나 참조된 파일에 나열되지 않은 모든 원격 목적지에 적용할 기본 임계값 정의
- 특정 원격 목적지에 적용할 임계값 정의
- 파일에 나열된 원격 목적지에 적용할 임계값 정의
- 위반 시 문제가 되는 원격 목적지를 지정된 파일에 기록하게 할 임계값 정의

정의의 순서가 중요합니다. 특정 대상에 대한 첫 번째 임계값(명시적이든 파일에 나열되든)은 같은 대상에 대한 이후의 모든 임계값을 재정의하며, 이는 명시적이든 파일에 나열되든 상관없습니다.

## 임계값

임계값은 "위반"이 발생하기 전까지 원격 목적지가 지정된 초 동안 수행할 수 있는 연결 시도 횟수로 정의됩니다. 예를 들어 다음 임계값 정의 `15/5`는 동일한 원격 목적지가 5초 기간 동안 14회의 연결 시도를 할 수 있음을 의미합니다. 같은 기간 내에 한 번 더 시도하면 임계값을 위반하게 됩니다.

임계값 형식은 다음 중 하나가 될 수 있습니다:

- 초 단위 시간당 연결 수의 **숫자 정의** - `15/5`, `30/60` 등. 연결 수가 1인 경우(예: `1/1`) 첫 번째 연결 시도가 임계값 위반을 초래한다는 점에 주의하세요.
- **`allow`** 단어. 이 임계값은 절대 위반되지 않습니다. 즉, 무제한 연결 시도가 허용됩니다.
- **`deny`** 단어. 이 임계값은 항상 위반됩니다. 즉, 연결 시도가 전혀 허용되지 않습니다.

### 기본 임계값

기본 임계값은 정의에 명시적으로 나열되지 않았거나 참조된 파일 중 어디에도 없는 모든 원격 대상에 적용됩니다. 기본 임계값을 설정하려면 `default` 키워드를 사용하세요. 다음은 기본 임계값의 예시입니다:

```text
15/5 default
allow default
deny default
```
필터당 기본 임계값은 하나만 정의할 수 있습니다. 생략된 경우, 필터는 기본적으로 알 수 없는 연결을 허용합니다.

### 명시적 임계값

명시적 임계값은 정의 자체에 나열된 원격 목적지에 적용됩니다. 예시:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### 벌크 임계값

편의를 위해 파일에 목적지 목록을 유지하고 모든 목적지에 대해 임계값을 일괄적으로 정의할 수 있습니다. 예시:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
이 파일들은 tunnel이 실행 중일 때 수동으로 편집할 수 있습니다. 이 파일들의 변경사항이 적용되는 데 최대 10초가 걸릴 수 있습니다.

## 레코더

Recorder는 원격 destination에서 시도하는 연결 시도를 추적하며, 특정 임계값을 초과하면 해당 destination이 지정된 파일에 기록됩니다. 예시:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
recorder를 사용하여 공격적인 destination들을 특정 파일에 기록한 다음, 동일한 파일을 사용하여 이들을 제한하는 것이 가능합니다. 예를 들어, 다음 코드 조각은 처음에는 모든 연결 시도를 허용하지만, 단일 destination이 5초 동안 30회 시도를 초과하면 5초 동안 15회 시도로 제한되는 필터를 정의합니다:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
한 tunnel에서 레코더를 사용하여 파일에 쓰고, 그 파일이 다른 tunnel을 조절하는 것이 가능합니다. 여러 tunnel의 목적지에서 같은 파일을 재사용하는 것도 가능합니다. 그리고 물론 이러한 파일들을 손으로 직접 편집하는 것도 가능합니다.

다음은 기본적으로 일부 조절(throttling)을 적용하고, `friends.txt` 파일에 있는 destination들에 대해서는 조절을 하지 않으며, `enemies.txt` 파일에 있는 destination들로부터의 모든 연결을 금지하고, 공격적인 행동을 `suspicious.txt`라는 파일에 기록하는 필터 정의 예시입니다:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```
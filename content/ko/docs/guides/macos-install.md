---
title: "macOS에 I2P 설치하기"
description: "macOS에서 I2P와 종속성을 수동으로 설치하는 단계별 가이드"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## 필요한 것들

- macOS 10.14 (Mojave) 이상을 실행하는 Mac
- 애플리케이션 설치를 위한 관리자 권한
- 약 15-20분 정도의 시간
- 설치 프로그램 다운로드를 위한 인터넷 연결

## 개요

이 설치 과정은 네 가지 주요 단계로 구성되어 있습니다:

1. **Java 설치** - Oracle Java Runtime Environment를 다운로드하고 설치합니다
2. **I2P 설치** - I2P 설치 프로그램을 다운로드하고 실행합니다
3. **I2P 앱 구성** - 런처를 설정하고 dock에 추가합니다
4. **I2P 대역폭 구성** - 설정 마법사를 실행하여 연결을 최적화합니다

## 1부: Java 설치

I2P를 실행하려면 Java가 필요합니다. 이미 Java 8 이상이 설치되어 있다면 [2부로 건너뛸 수 있습니다](#part-two-download-and-install-i2p).

### 1단계: Java 다운로드

[Oracle Java 다운로드 페이지](https://www.oracle.com/java/technologies/downloads/)를 방문하여 Java 8 이상의 macOS 설치 프로그램을 다운로드하세요.

![macOS용 Oracle Java 다운로드](/images/guides/macos-install/0-jre.png)

### 2단계: 설치 프로그램 실행

다운로드 폴더에서 다운로드한 `.dmg` 파일을 찾아 더블클릭하여 엽니다.

![Java 설치 프로그램 열기](/images/guides/macos-install/1-jre.png)

### 3단계: 설치 허용

macOS는 설치 프로그램이 식별된 개발자로부터 제공되었기 때문에 보안 프롬프트를 표시할 수 있습니다. 계속 진행하려면 **열기**를 클릭하세요.

![설치 프로그램이 진행할 수 있도록 권한 부여](/images/guides/macos-install/2-jre.png)

### 4단계: Java 설치

**설치**를 클릭하여 Java 설치 과정을 시작합니다.

![Java 설치 시작](/images/guides/macos-install/3-jre.png)

### 5단계: 설치 대기

설치 프로그램이 파일을 복사하고 시스템에 Java를 구성합니다. 일반적으로 1-2분 정도 소요됩니다.

![설치 프로그램이 완료될 때까지 기다리세요](/images/guides/macos-install/4-jre.png)

### 6단계: 설치 완료

성공 메시지가 표시되면 Java가 설치된 것입니다! **닫기**를 클릭하여 완료하세요.

![Java 설치 완료](/images/guides/macos-install/5-jre.png)

## 2부: I2P 다운로드 및 설치

이제 Java가 설치되었으므로 I2P router를 설치할 수 있습니다.

### 1단계: I2P 다운로드

[다운로드 페이지](/downloads/)를 방문하여 **I2P for Unix/Linux/BSD/Solaris** 설치 파일(`.jar` 파일)을 다운로드하세요.

![I2P 설치 프로그램 다운로드](/images/guides/macos-install/0-i2p.png)

### 2단계: 설치 프로그램 실행

다운로드한 `i2pinstall_X.X.X.jar` 파일을 더블클릭하세요. 설치 프로그램이 실행되고 선호하는 언어를 선택하라는 메시지가 표시됩니다.

![언어를 선택하세요](/images/guides/macos-install/1-i2p.png)

### 3단계: 환영 화면

환영 메시지를 읽고 **다음**을 클릭하여 계속 진행하세요.

![설치 프로그램 소개](/images/guides/macos-install/2-i2p.png)

### 4단계: 중요 공지사항

설치 프로그램에서 업데이트에 대한 중요한 공지사항을 표시합니다. I2P 업데이트는 이 설치 프로그램 자체는 서명되지 않았지만 **end-to-end 서명**되고 검증됩니다. **Next**를 클릭하세요.

![업데이트에 대한 중요 공지](/images/guides/macos-install/3-i2p.png)

### 5단계: 라이선스 동의

I2P 라이선스 동의서(BSD 스타일 라이선스)를 읽어보세요. 동의하려면 **다음**을 클릭하세요.

![라이선스 계약](/images/guides/macos-install/4-i2p.png)

### 6단계: 설치 디렉터리 선택

I2P를 설치할 위치를 선택하세요. 기본 위치(`/Applications/i2p`)를 권장합니다. **다음**을 클릭하세요.

![설치 디렉토리 선택](/images/guides/macos-install/5-i2p.png)

### 7단계: 구성 요소 선택

완전한 설치를 위해 모든 구성 요소를 선택한 상태로 두세요. **다음**을 클릭하세요.

![설치할 구성 요소 선택](/images/guides/macos-install/6-i2p.png)

### 8단계: 설치 시작

선택 사항을 검토하고 **다음**을 클릭하여 I2P 설치를 시작하세요.

![설치 시작](/images/guides/macos-install/7-i2p.png)

### 9단계: 파일 설치

설치 프로그램이 I2P 파일을 시스템에 복사합니다. 약 1-2분이 소요됩니다.

![설치 진행 중](/images/guides/macos-install/8-i2p.png)

### 10단계: 실행 스크립트 생성

설치 프로그램은 I2P를 시작하기 위한 실행 스크립트를 생성합니다.

![실행 스크립트 생성](/images/guides/macos-install/9-i2p.png)

### 11단계: 설치 바로가기

설치 프로그램에서 바탕화면 바로가기와 메뉴 항목을 만들 것인지 묻습니다. 원하는 항목을 선택하고 **다음**을 클릭하세요.

![바로가기 만들기](/images/guides/macos-install/10-i2p.png)

### 12단계: 설치 완료

성공! I2P가 설치되었습니다. **완료**를 클릭하여 마무리하세요.

![설치 완료](/images/guides/macos-install/11-i2p.png)

## 3부: I2P 앱 구성

이제 I2P를 Applications 폴더와 Dock에 추가하여 쉽게 실행할 수 있도록 만들어 봅시다.

### 1단계: 애플리케이션 폴더 열기

Finder를 열고 **응용 프로그램** 폴더로 이동하세요.

![애플리케이션 폴더 열기](/images/guides/macos-install/0-conf.png)

### 2단계: I2P Launcher 찾기

`/Applications/i2p/` 안에서 **I2P** 폴더나 **Start I2P Router** 애플리케이션을 찾아보세요.

![I2P 런처 찾기](/images/guides/macos-install/1-conf.png)

### 3단계: Dock에 추가

쉬운 접근을 위해 **Start I2P Router** 애플리케이션을 Dock으로 드래그하세요. 데스크톱에 별칭을 만들 수도 있습니다.

![Dock에 I2P 추가하기](/images/guides/macos-install/2-conf.png)

**팁**: Dock에서 I2P 아이콘을 우클릭하고 **옵션 → Dock에 유지**를 선택하여 영구적으로 유지할 수 있습니다.

## 4부: I2P 대역폭 구성

I2P를 처음 실행하면 대역폭 설정을 구성하는 설정 마법사가 실행됩니다. 이를 통해 연결 상태에 맞게 I2P 성능을 최적화할 수 있습니다.

### 1단계: I2P 실행

Dock에서 I2P 아이콘을 클릭하거나 런처를 더블클릭하세요. 기본 웹 브라우저가 열리면서 I2P Router Console이 표시됩니다.

![I2P Router Console 환영 화면](/images/guides/macos-install/0-wiz.png)

### 단계 2: 환영 마법사

설정 마법사가 나타납니다. **다음**을 클릭하여 I2P 구성을 시작하세요.

![설정 마법사 소개](/images/guides/macos-install/1-wiz.png)

### 3단계: 언어 및 테마

선호하는 **인터페이스 언어**를 선택하고 **밝은** 테마 또는 **어두운** 테마 중에서 선택하세요. **다음**을 클릭하세요.

![언어 및 테마 선택](/images/guides/macos-install/2-wiz.png)

### 4단계: 대역폭 테스트 정보

마법사가 대역폭 테스트에 대해 설명합니다. 이 테스트는 **M-Lab** 서비스에 연결하여 인터넷 속도를 측정합니다. 계속하려면 **다음**을 클릭하세요.

![대역폭 테스트 설명](/images/guides/macos-install/3-wiz.png)

### 5단계: 대역폭 테스트 실행

**테스트 실행**을 클릭하여 업로드 및 다운로드 속도를 측정하세요. 테스트는 약 30-60초가 소요됩니다.

![대역폭 테스트 실행](/images/guides/macos-install/4-wiz.png)

### 6단계: 테스트 결과

테스트 결과를 검토하세요. I2P는 연결 속도를 기반으로 대역폭 설정을 권장합니다.

![대역폭 테스트 결과](/images/guides/macos-install/5-wiz.png)

### 7단계: 대역폭 공유 설정

I2P 네트워크와 공유할 대역폭을 선택하세요:

- **자동** (권장): I2P가 사용량에 따라 대역폭을 관리합니다
- **제한**: 특정 업로드/다운로드 제한을 설정합니다
- **무제한**: 가능한 많이 공유합니다 (빠른 연결용)

**다음**을 클릭하여 설정을 저장합니다.

![대역폭 공유 구성](/images/guides/macos-install/6-wiz.png)

### 8단계: 설정 완료

I2P router가 이제 구성되어 실행 중입니다! router 콘솔에서 연결 상태를 확인하고 I2P 사이트를 탐색할 수 있습니다.

## I2P 시작하기

I2P가 설치되고 구성되었으므로, 이제 다음을 할 수 있습니다:

1. **I2P 사이트 탐색**: [I2P 홈페이지](http://127.0.0.1:7657/home)를 방문하여 인기 있는 I2P 서비스 링크를 확인하세요
2. **브라우저 구성**: `.i2p` 사이트에 접근하기 위해 [브라우저 프로필](/docs/guides/browser-config)을 설정하세요
3. **서비스 탐색**: I2P 이메일, 포럼, 파일 공유 등을 확인해보세요
4. **router 모니터링**: [콘솔](http://127.0.0.1:7657/console)에서 네트워크 상태와 통계를 확인할 수 있습니다

### 유용한 링크

- **Router Console**: [http://127.0.0.1:7657/](http://127.0.0.1:7657/)
- **설정**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)
- **주소록**: [http://127.0.0.1:7657/susidns/addressbook](http://127.0.0.1:7657/susidns/addressbook)
- **대역폭 설정**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)

## 설정 마법사 다시 실행하기

대역폭 설정을 변경하거나 나중에 I2P를 다시 구성하고 싶다면, Router Console에서 환영 마법사를 다시 실행할 수 있습니다:

1. [I2P 설정 마법사](http://127.0.0.1:7657/welcome)로 이동하세요
2. 마법사 단계를 다시 따라하세요

## 문제 해결

### I2P가 시작되지 않음

- **Java 확인**: Terminal에서 `java -version`을 실행하여 Java가 설치되어 있는지 확인하세요
- **권한 확인**: I2P 폴더가 올바른 권한을 가지고 있는지 확인하세요
- **로그 확인**: 오류 메시지를 위해 `~/.i2p/wrapper.log`를 살펴보세요

### 브라우저에서 I2P 사이트에 접근할 수 없음

- I2P가 실행 중인지 확인하세요 (Router Console 확인)
- 브라우저의 프록시 설정을 HTTP 프록시 `127.0.0.1:4444`를 사용하도록 구성하세요
- I2P가 네트워크에 통합되도록 시작 후 5-10분 정도 기다리세요

### 느린 성능

- 대역폭 테스트를 다시 실행하고 설정을 조정하세요
- 네트워크와 일부 대역폭을 공유하고 있는지 확인하세요
- Router Console에서 연결 상태를 확인하세요

## I2P 제거

Mac에서 I2P를 제거하려면:

1. I2P router가 실행 중이면 종료합니다
2. `/Applications/i2p` 폴더를 삭제합니다
3. `~/.i2p` 폴더를 삭제합니다 (I2P 설정 및 데이터)
4. Dock에서 I2P 아이콘을 제거합니다

## 다음 단계

- **커뮤니티 참여**: [i2pforum.net](http://i2pforum.net)을 방문하거나 Reddit에서 I2P를 확인하세요
- **더 알아보기**: 네트워크 작동 방식을 이해하기 위해 [I2P 문서](/en/docs)를 읽어보세요
- **참여하기**: I2P 개발에 [기여](/en/get-involved)하거나 인프라 운영을 고려해보세요

축하합니다! 이제 I2P 네트워크의 일원이 되셨습니다. 보이지 않는 인터넷에 오신 것을 환영합니다!

---

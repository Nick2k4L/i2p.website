---
title: "관리형 클라이언트"
description: "router 관리 애플리케이션이 ClientAppManager와 포트 매퍼와 통합되는 방법"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## 개요

클라이언트는 [clients.config](/docs/specs/configuration/) 파일에 나열되어 있을 때 router에 의해 직접 시작될 수 있습니다. 이러한 클라이언트는 "관리형" 또는 "비관리형"일 수 있습니다. 이는 ClientAppManager에 의해 처리됩니다. 또한 관리형 또는 비관리형 클라이언트는 ClientAppManager에 등록하여 다른 클라이언트가 해당 클라이언트에 대한 참조를 검색할 수 있도록 할 수 있습니다. 또한 클라이언트가 내부 포트를 등록하고 다른 클라이언트가 조회할 수 있도록 하는 간단한 Port Mapper 기능도 있습니다.

---

## 관리형 클라이언트

릴리스 0.9.4부터 router는 관리형 클라이언트를 지원합니다. 관리형 클라이언트는 ClientAppManager에 의해 인스턴스화되고 시작됩니다. ClientAppManager는 클라이언트에 대한 참조를 유지하고 클라이언트 상태에 대한 업데이트를 받습니다. 관리형 클라이언트는 상태 추적을 구현하고 클라이언트를 시작하고 중지하기가 훨씬 쉽기 때문에 선호됩니다. 또한 클라이언트가 중지된 후 과도한 메모리 사용으로 이어질 수 있는 클라이언트 코드의 정적 참조를 피하는 것이 훨씬 쉽습니다. 관리형 클라이언트는 router 콘솔에서 사용자가 시작하고 중지할 수 있으며, router 종료 시 중지됩니다.

관리형 클라이언트는 net.i2p.app.ClientApp 또는 net.i2p.router.app.RouterApp 인터페이스를 구현합니다. ClientApp 인터페이스를 구현하는 클라이언트는 다음 생성자를 제공해야 합니다:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
RouterApp 인터페이스를 구현하는 클라이언트는 다음 생성자를 제공해야 합니다:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
제공된 인수는 clients.config 파일에 지정됩니다.

---

## 관리되지 않는 클라이언트

clients.config 파일에 지정된 메인 클래스가 관리 인터페이스를 구현하지 않는 경우, 지정된 인수와 함께 main()으로 시작되고, 지정된 인수와 함께 main()으로 중지됩니다. router는 모든 상호작용이 정적 main() 메서드를 통해 이루어지므로 참조를 유지하지 않습니다. 콘솔은 사용자에게 정확한 상태 정보를 제공할 수 없습니다.

---

## 등록된 클라이언트

관리형 또는 비관리형 클라이언트는 다른 클라이언트가 해당 클라이언트에 대한 참조를 검색할 수 있도록 ClientAppManager에 등록할 수 있습니다. 등록은 이름으로 이루어집니다. 알려진 등록된 클라이언트는 다음과 같습니다:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## 포트 매퍼

router는 또한 클라이언트가 HTTP 프록시와 같은 내부 소켓 서비스를 찾을 수 있는 간단한 메커니즘을 제공합니다. 이는 Port Mapper에 의해 제공됩니다. 등록은 이름으로 이루어집니다. 등록하는 클라이언트는 일반적으로 해당 포트에서 내부 에뮬레이션된 소켓을 제공합니다.

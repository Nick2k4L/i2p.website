---
title: "Clientes Gestionados"
description: "Cómo las aplicaciones gestionadas por router se integran con ClientAppManager y el mapeador de puertos"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## Visión general

Los clientes pueden ser iniciados directamente por el router cuando están listados en el archivo [clients.config](/docs/specs/configuration/). Estos clientes pueden ser "gestionados" o "no gestionados". Esto es manejado por el ClientAppManager. Además, los clientes gestionados o no gestionados pueden registrarse con el ClientAppManager para que otros clientes puedan obtener una referencia a ellos. También existe una facilidad simple de Port Mapper para que los clientes registren un puerto interno que otros clientes puedan consultar.

---

## Clientes Gestionados

A partir de la versión 0.9.4, el router soporta clientes administrados. Los clientes administrados son instanciados e iniciados por el ClientAppManager. El ClientAppManager mantiene una referencia al cliente y recibe actualizaciones sobre el estado del cliente. Los clientes administrados son preferibles, ya que es mucho más fácil implementar el seguimiento del estado y iniciar y detener un cliente. También es mucho más fácil evitar referencias estáticas en el código del cliente que podrían llevar a un uso excesivo de memoria después de que un cliente se detenga. Los clientes administrados pueden ser iniciados y detenidos por el usuario en la consola del router, y se detienen al apagar el router.

Los clientes gestionados implementan la interfaz net.i2p.app.ClientApp o net.i2p.router.app.RouterApp. Los clientes que implementan la interfaz ClientApp deben proporcionar el siguiente constructor:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
Los clientes que implementan la interfaz RouterApp deben proporcionar el siguiente constructor:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
Los argumentos proporcionados se especifican en el archivo clients.config.

---

## Clientes no administrados

Si la clase principal especificada en el archivo clients.config no implementa una interfaz administrada, se iniciará con main() con los argumentos especificados, y se detendrá con main() con los argumentos especificados. El router no mantiene una referencia, ya que todas las interacciones son a través del método estático main(). La consola no puede proporcionar información de estado precisa al usuario.

---

## Clientes Registrados

Los clientes, ya sean administrados o no administrados, pueden registrarse con el ClientAppManager para que otros clientes puedan obtener una referencia a ellos. El registro se realiza por nombre. Los clientes registrados conocidos son:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## Mapeador de Puertos

El router también proporciona un mecanismo simple para que los clientes encuentren un servicio de socket interno, como el proxy HTTP. Esto lo proporciona el Port Mapper. El registro es por nombre. Los clientes que se registran generalmente proporcionan un socket emulado interno en ese puerto.

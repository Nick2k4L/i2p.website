---
title: "Clientes I2P Alternativos"
description: "Implementaciones de cliente I2P mantenidas por la comunidad (actualizado para 2025)"
slug: "alternative-clients"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

La implementación principal del cliente I2P utiliza **Java**. Si no puedes o prefieres no usar Java en un sistema particular, existen implementaciones alternativas del cliente I2P desarrolladas y mantenidas por miembros de la comunidad. Estos programas proporcionan la misma funcionalidad central usando diferentes lenguajes de programación o enfoques.

---

## Tabla de Comparación

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Client</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Maturity</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Actively Maintained</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Suitable For</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Java I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes (official)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">General users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Standard full router; includes console, plugins, and tools</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>i2pd</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Low-resource systems, servers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Lightweight, fully compatible with Java I2P, includes web console</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Go-I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, testing</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Early-stage Go implementation; not yet production ready</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Emissary</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, embedded use</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust I2P implementation; embeddable router with eepsite, torrent, IRC and email support</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>I2P+</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable (fork)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Advanced users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Enhanced Java I2P fork with UI and performance improvements</td>
    </tr>
  </tbody>
</table>
---

## i2pd (C++)

**Sitio web:** [https://i2pd.website](https://i2pd.website)

**Descripción:** i2pd (el *I2P Daemon*) es un cliente I2P completo implementado en C++. Ha sido estable para uso en producción durante muchos años (desde alrededor de 2016) y es mantenido activamente por la comunidad. i2pd implementa completamente los protocolos de red y APIs de I2P, haciéndolo totalmente compatible con la red Java I2P. Este router de C++ se utiliza a menudo como una alternativa ligera en sistemas donde el runtime de Java no está disponible o no se desea. i2pd incluye una consola web integrada para configuración y monitoreo. Es multiplataforma y está disponible en muchos formatos de empaquetado — incluso existe una versión de Android de i2pd disponible (por ejemplo, a través de F-Droid).

---

## Go-I2P (Go)

**Repositorio:** [https://github.com/go-i2p/go-i2p](https://github.com/go-i2p/go-i2p)

**Descripción:** Go-I2P es un cliente I2P escrito en el lenguaje de programación Go. Es una implementación independiente del router I2P, con el objetivo de aprovechar la eficiencia y portabilidad de Go. El proyecto está bajo desarrollo activo, pero aún se encuentra en una etapa temprana y no está completo en características. A partir de 2025, Go-I2P se considera experimental — está siendo trabajado activamente por desarrolladores de la comunidad, pero no se recomienda para uso en producción hasta que madure más. El objetivo de Go-I2P es proporcionar un router I2P moderno y liviano con compatibilidad completa con la red I2P una vez que se complete el desarrollo.

---

## Emissary (Rust)

**Sitio web:** [https://eepnet.github.io/emissary/](https://eepnet.github.io/emissary/)

**Descripción:** Emissary es una implementación en Rust de la pila de protocolos I2P, diseñada para funcionar como un router I2P embebible. Puede integrarse en otras aplicaciones o ejecutarse de forma independiente. Emissary admite hosting de eepsites, torrents, servicios de IRC y correo electrónico. El proyecto incluye documentación extensa que cubre configuración de inicio rápido, embedding para desarrolladores y configuración detallada. Como proyecto experimental, está en desarrollo activo y aún no se recomienda para uso en producción.

---

## I2P+ (fork de Java)

**Sitio web:** [https://i2pplus.github.io](https://i2pplus.github.io)

**Descripción:** I2P+ es un fork mantenido por la comunidad del cliente Java I2P estándar. No es una reimplementación en un nuevo lenguaje, sino más bien una versión mejorada del router Java con características adicionales y optimizaciones. I2P+ se enfoca en ofrecer una experiencia de usuario mejorada y mejor rendimiento mientras se mantiene completamente compatible con la red oficial I2P. Introduce una interfaz de consola web renovada, opciones de configuración más amigables para el usuario, y varias optimizaciones (por ejemplo, rendimiento mejorado de torrent y mejor manejo de peers de red, especialmente para routers detrás de firewalls). I2P+ requiere un entorno Java al igual que el software oficial I2P, por lo que no es una solución para entornos sin Java. Sin embargo, para usuarios que sí tienen Java y quieren una versión alternativa con capacidades extra, I2P+ proporciona una opción atractiva. Este fork se mantiene actualizado con las versiones upstream de I2P (con su numeración de versión agregando un "+") y se puede obtener desde el sitio web del proyecto.

---
title: "Nuevo Propuesta de Plantilla de Cifrado"
aliases:
  - "/es/proposals/142-ecies-template"
  - "/es/proposals/142-ecies-template/"
number: "142"
author: "zzz"
created: "2018-01-11"
lastupdated: "2018-01-20"
status: "Meta"
thread: "http://zzz.i2p/topics/2499"
toc: true
---
## Descripción general

Este documento describe aspectos importantes a considerar al proponer
un reemplazo o adición a nuestro cifrado asimétrico ElGamal.

Este es un documento informativo.


## Motivación

ElGamal es antiguo y lento, y existen mejores alternativas.
Sin embargo, hay varios problemas que deben abordarse antes de poder añadir o cambiar a cualquier nuevo algoritmo.
Este documento destaca estos problemas sin resolver.



## Investigación previa

Cualquier persona que proponga nueva criptografía debe conocer primero los siguientes documentos:

- [Propuesta 111 NTCP2](/proposals/111-ntcp-2/)
- [Propuesta 123 LS2](/proposals/123-new-netdb-entries/)
- [Propuesta 136 tipos de firma experimentales](/proposals/136-experimental-sigtypes/)
- [Propuesta 137 tipos de firma opcionales](/proposals/137-optional-sigtypes/)
- Hilos de discusión aquí para cada una de las propuestas anteriores, enlazados dentro
- [Prioridades de propuestas 2018](http://zzz.i2p/topics/2494)
- [Propuesta ECIES](http://zzz.i2p/topics/2418)
- [Resumen de nueva criptografía asimétrica](http://zzz.i2p/topics/1768)
- [Resumen de criptografía de bajo nivel](/docs/specs/common-structures/)


## Usos de la criptografía asimétrica

Como repaso, usamos ElGamal para:

1) Mensajes de construcción de túnel (la clave está en RouterIdentity)

2) Cifrado entre routers de netdb y otros mensajes I2NP (la clave está en RouterIdentity)

3) Cliente de extremo a extremo con ElGamal+AES/SessionTag (la clave está en LeaseSet, la clave de Destination no se usa)

4) DH efímero para NTCP y SSU


## Diseño

Cualquier propuesta para reemplazar ElGamal con otro algoritmo debe proporcionar los siguientes detalles.



## Especificación

Cualquier propuesta para nueva criptografía asimétrica debe especificar completamente las siguientes cosas.



### 1. General

Conteste las siguientes preguntas en su propuesta. Tenga en cuenta que esto podría necesitar ser una propuesta separada de los detalles en el punto 2) más abajo, ya que podría entrar en conflicto con propuestas existentes como 111, 123, 136, 137 u otras.

- ¿Para cuáles de los casos anteriores del 1 al 4 propone usar la nueva criptografía?
- Si es para 1) o 2) (router), ¿dónde irá la clave pública, en RouterIdentity o en las propiedades de RouterInfo? ¿Tiene intención de usar el tipo de criptografía en el certificado de clave? Especifique completamente. Justifique su decisión en cualquier caso.
- Si es para 3) (cliente), ¿tiene intención de almacenar la clave pública en el destino y usar el tipo de criptografía en el certificado de clave (como en la propuesta ECIES), o almacenarla en LS2 (como en la propuesta 123), o algo diferente? Especifique completamente, y justifique su decisión.
- Para todos los usos, ¿cómo se anunciará el soporte? Si es para 3), ¿irá en LS2 o en otro lugar? Si es para 1) y 2), ¿es similar a las propuestas 136 y/o 137? Especifique completamente, y justifique sus decisiones. Probablemente necesitará una propuesta separada para esto.
- Especifique completamente cómo y por qué esto es compatible con versiones anteriores, y detalle completamente un plan de migración.
- ¿Qué propuestas no implementadas son prerrequisitos para su propuesta?


### 2. Tipo específico de criptografía

Conteste las siguientes preguntas en su propuesta:

- Información general de criptografía, curvas/parámetros específicos, justifique completamente su elección. Proporcione enlaces a especificaciones y otra información.
- Resultados de pruebas de velocidad comparados con ElG y otras alternativas si aplica. Incluya cifrado, descifrado y generación de claves.
- Disponibilidad de bibliotecas en C++ y Java (tanto OpenJDK, BouncyCastle, como de terceros)
  Para bibliotecas de terceros o no-Java, proporcione enlaces y licencias
- Número(s) propuesto(s) para el tipo de criptografía (en rango experimental o no)




## Notas

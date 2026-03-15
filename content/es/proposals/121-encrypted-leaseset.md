---
title: "LeaseSet Encriptado"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Rechazado"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## Resumen

Esta propuesta trata sobre el rediseño del mecanismo para cifrar los LeaseSets.


## Motivación

El LS cifrado actual es horrible e inseguro. Puedo decirlo, yo lo diseñé e implementé.

Razones:

- Cifrado AES CBC
- Una sola clave AES para todos
- Las expiraciones de los leases siguen expuestas
- La clave pública de cifrado sigue expuesta


## Diseño

### Objetivos

- Hacer que todo sea opaco
- Claves para cada destinatario


### Estrategia

Hacer como GPG/OpenPGP. Cifrar asimétricamente una clave simétrica para cada destinatario. Los datos se descifran con esa clave asimétrica. Ver, por ejemplo, [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
Si podemos encontrar un algoritmo que sea pequeño y rápido.

El truco es encontrar un cifrado asimétrico que sea pequeño y rápido. ElGamal con 514 bytes es un poco doloroso aquí. Podemos hacer mejor.

Ver, por ejemplo, http://security.stackexchange.com/questions/824...

Esto funciona para pequeños números de destinatarios (o en realidad, claves; todavía puedes distribuir claves a varias personas si lo deseas).


## Especificación

- Destino
- Timestamp publicado
- Expiración
- Indicadores
- Longitud de los datos
- Datos cifrados
- Firma

Los datos cifrados podrían tener un prefijo con un especificador de tipo de cifrado, o no.


## Referencias

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)

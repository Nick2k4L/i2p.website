---
title: "RI y Padding de Destino"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Open"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## Estado

Implementado en la versión 0.9.57.
Se deja esta propuesta abierta para poder mejorar y discutir las ideas en la sección "Planificación Futura".


## Visión general


### Resumen

La clave pública ElGamal en Destinos ha estado sin usar desde la versión 0.6 (2005).
Aunque nuestras especificaciones indican que no se utiliza, NO indican que las implementaciones puedan evitar
generar un par de claves ElGamal y simplemente llenar el campo con datos aleatorios.

Proponemos modificar las especificaciones para indicar que
el campo es ignorado y que las implementaciones PUEDEN llenarlo con datos aleatorios.
Este cambio es compatible con versiones anteriores. No se conoce ninguna implementación que valide
la clave pública ElGamal.

Además, esta propuesta ofrece orientación a los desarrolladores sobre cómo generar los
datos aleatorios para el relleno (padding) de Destinos e Identidades de Routers, de modo que sean comprimibles,
a la vez que sean seguros y sus representaciones en Base 64 no parezcan corruptas o inseguras.
Esto proporciona la mayor parte de los beneficios de eliminar los campos de relleno sin necesidad de
cambios disruptivos en el protocolo.
Los Destinos comprimibles reducen el tamaño del SYN de streaming y de los datagramas con respuesta;
las Identidades de Routers comprimibles reducen los mensajes Database Store, los mensajes SSU2 Session Confirmed
y los archivos su3 de reseed.

Finalmente, la propuesta discute posibilidades para nuevos formatos de Destino e Identidad de Router
que eliminarían por completo el relleno. También hay una breve discusión sobre criptografía post-cuántica
y cómo podría afectar la planificación futura.



### Objetivos

- Eliminar el requisito de generar un par de claves ElGamal para Destinos
- Recomendar buenas prácticas para que Destinos e Identidades de Routers sean altamente comprimibles,
  sin mostrar patrones evidentes en sus representaciones Base 64.
- Fomentar la adopción de buenas prácticas por todas las implementaciones para que
  los campos no sean distinguibles
- Reducir el tamaño del SYN de streaming
- Reducir el tamaño del datagrama con respuesta
- Reducir el tamaño del bloque de Identidad de Router en SSU2
- Reducir el tamaño y la frecuencia de fragmentación del mensaje SSU2 Session Confirmed
- Reducir el tamaño del mensaje Database Store (con RI)
- Reducir el tamaño del archivo de reseed
- Mantener compatibilidad en todos los protocolos y APIs
- Actualizar especificaciones
- Discutir alternativas para nuevos formatos de Destino e Identidad de Router

Al eliminar el requisito de generar claves ElGamal, las implementaciones podrían
ser capaces de eliminar completamente el código ElGamal, sujeto a consideraciones de compatibilidad
con otros protocolos.



## Diseño

Estrictamente hablando, la clave pública de firma de 32 bytes (tanto en Destinos como en Identidades de Routers)
y la clave pública de cifrado de 32 bytes (solo en Identidades de Routers) constituyen un número aleatorio
que proporciona toda la entropía necesaria para que los hashes SHA-256 de estas estructuras
sean criptográficamente fuertes y estén distribuidos aleatoriamente en la DHT de la base de datos de la red.

Sin embargo, por exceso de precaución, recomendamos usar al menos 32 bytes de datos aleatorios
en el campo de clave pública ElGamal y en el relleno. Además, si los campos fueran todos ceros,
los Destinos en Base 64 contendrían largas secuencias de caracteres AAAA, lo que podría causar alarma
o confusión a los usuarios.

Para el tipo de firma Ed25519 y tipo de cifrado X25519:
los Destinos contendrán 11 copias (352 bytes) de los datos aleatorios.
Las Identidades de Routers contendrán 10 copias (320 bytes) de los datos aleatorios.



### Ahorro estimado

Los Destinos se incluyen en cada SYN de streaming
y en cada datagrama con respuesta.
Las Informaciones de Routers (que contienen Identidades de Routers) se incluyen en los mensajes Database Store
y en los mensajes Session Confirmed de NTCP2 y SSU2.

NTCP2 no comprime la Información de Router.
Las RIs en los mensajes Database Store y en los mensajes SSU2 Session Confirmed están comprimidas con gzip.
Las Informaciones de Routers están comprimidas en los archivos SU3 de reseed.

Los Destinos en los mensajes Database Store no están comprimidos.
Los mensajes SYN de streaming están comprimidos con gzip a nivel de I2CP.

Para el tipo de firma Ed25519 y tipo de cifrado X25519,
ahorro estimado:

| Tipo de dato | Tamaño total | Claves y certificado | Relleno sin comprimir | Relleno comprimido | Tamaño | Ahorro |
|--------------|--------------|------------------------|------------------------|---------------------|--------|--------|
| Destino | 391 | 39 | 352 | 32 | 71 | 320 bytes (82%) |
| Identidad de Router | 391 | 71 | 320 | 32 | 103 | 288 bytes (74%) |
| Información de Router | 1000 típ. | 71 | 320 | 32 | 722 típ. | 288 bytes (29%) |

Notas: Supone que el certificado de 7 bytes no es comprimible y cero sobrecarga adicional de gzip.
Ninguna de las dos suposiciones es estrictamente cierta, pero los efectos serán pequeños.
Ignora otras partes comprimibles de la Información de Router.



## Especificación

Los cambios propuestos a nuestras especificaciones actuales se documentan a continuación.


### Estructuras comunes
Modificar la especificación de estructuras comunes
para indicar que el campo de 256 bytes de clave pública del Destino es ignorado y puede
contener datos aleatorios.

Añadir una sección a la especificación de estructuras comunes
recomendando buenas prácticas para el campo de clave pública del Destino y los
campos de relleno en el Destino y la Identidad de Router, como sigue:

Generar 32 bytes de datos aleatorios usando un generador criptográfico fuerte de números pseudoaleatorios (PRNG)
y repetir esos 32 bytes según sea necesario para llenar el campo de clave pública (para Destinos)
y el campo de relleno (para Destinos e Identidades de Routers).


### Archivo de clave privada
El formato del archivo de clave privada (eepPriv.dat) no es una parte oficial de nuestras especificaciones,
pero está documentado en los [javadocs de Java I2P](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
y otras implementaciones lo soportan.
Esto permite la portabilidad de claves privadas entre diferentes implementaciones.
Añadir una nota en esos javadocs indicando que la clave pública de cifrado puede ser relleno aleatorio
y que la clave privada de cifrado puede ser todo ceros o datos aleatorios.

### SAM
Indicar en la especificación de SAM que la clave privada de cifrado no se usa y puede ignorarse.
Cualquier dato aleatorio puede devolverse por el cliente.
El puente SAM puede enviar datos aleatorios al crear (con DEST GENERATE o SESSION CREATE DESTINATION=TRANSIENT)
en lugar de todo ceros, para que la representación Base 64 no contenga una cadena de caracteres AAAA
y no parezca defectuosa.


### I2CP
No se requieren cambios en I2CP. La clave privada para la clave pública de cifrado en el Destino
no se envía al router.


## Planificación futura


### Cambios de protocolo

A costa de cambios en el protocolo y pérdida de compatibilidad, podríamos
modificar nuestros protocolos y especificaciones para eliminar el campo de relleno en
el Destino, la Identidad de Router, o ambos.

Esta propuesta tiene cierta similitud con el formato de leaseset cifrado "b33",
que contiene solo un campo de clave y un campo de tipo.

Para mantener cierta compatibilidad, ciertas capas del protocolo podrían "expandir" el campo de relleno
con ceros para presentarlo a otras capas del protocolo.

Para Destinos, también podríamos eliminar el campo de tipo de cifrado en el certificado de clave,
con un ahorro de dos bytes.
Alternativamente, los Destinos podrían obtener un nuevo tipo de cifrado en el certificado,
indicando una clave pública cero (y relleno).

Si no se incluye conversión de compatibilidad entre formatos antiguos y nuevos en alguna capa del protocolo,
las siguientes especificaciones, APIs, protocolos y aplicaciones se verían afectadas:

- Especificación de estructuras comunes
- I2NP
- I2CP
- NTCP2
- SSU2
- Ratchet
- Streaming
- SAM
- Bittorrent
- Reseeding
- Archivo de clave privada
- API del núcleo y router de Java
- API de i2pd
- Bibliotecas SAM de terceros
- Herramientas integradas y de terceros
- Varios plugins de Java
- Interfaces de usuario
- Aplicaciones P2P, por ejemplo MuWire, bitcoin, monero
- hosts.txt, libreta de direcciones y suscripciones

Si se especifica conversión en alguna capa, la lista se reduciría.

Los costos y beneficios de estos cambios no están claros.

Propuestas específicas por determinar:





### Claves PQ

Las claves públicas de cifrado Post-Cuántico (PQ), para cualquier algoritmo anticipado,
son mayores de 256 bytes. Esto eliminaría cualquier relleno y cualquier ahorro de los cambios propuestos anteriormente,
para Identidades de Routers.

En un enfoque "híbrido" PQ, como el que está adoptando SSL, las claves PQ serían solo efímeras,
y no aparecerían en la Identidad de Router.

Las claves de firma PQ no son viables,
y los Destinos no contienen claves públicas de cifrado.
Las claves estáticas para ratchet están en el Lease Set, no en el Destino.
por lo tanto podemos excluir los Destinos del resto de esta discusión.

Así que PQ solo afecta a las Informaciones de Router, y solo para claves estáticas PQ (no efímeras), no para PQ híbrido.
Esto sería para un nuevo tipo de cifrado y afectaría a NTCP2, SSU2, y
a los mensajes cifrados de búsqueda en la base de datos y sus respuestas.
El marco temporal estimado para el diseño, desarrollo y despliegue de esto sería ????????
Pero sería después del híbrido o ratchet ????????????

Para más discusión ver [este tema](http://zzz.i2p/topics/3294).




## Problemas

Podría ser deseable reconfigurar la red a un ritmo lento, para proporcionar cobertura a nuevos routers.
"Reconfigurar" podría significar simplemente cambiar el relleno, sin cambiar realmente las claves.

No es posible reconfigurar Destinos existentes.

¿Deberían las Identidades de Router con relleno en el campo de clave pública identificarse con un tipo
de cifrado diferente en el certificado de clave? Esto causaría problemas de compatibilidad.




## Migración

No hay problemas de compatibilidad con versiones anteriores al reemplazar la clave ElGamal por relleno.

La reconfiguración, si se implementa, sería similar a la realizada
en tres transiciones anteriores de identidad de router:
De firmas DSA-SHA1 a ECDSA, luego a
firmas EdDSA, luego a cifrado X25519.

Sujeto a problemas de compatibilidad, y tras deshabilitar SSU,
las implementaciones podrían eliminar completamente el código ElGamal.
Aproximadamente el 14% de los routers en la red usan cifrado ElGamal, incluyendo muchos floodfills.

Una solicitud de fusión preliminar para Java I2P está disponible en [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66).


## Referencias

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)

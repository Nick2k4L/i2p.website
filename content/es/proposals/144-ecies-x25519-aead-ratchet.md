---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/es/proposals/144-ecies-x25519"
  - "/es/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "Cerrado"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## Nota
Despliegue y pruebas en la red en curso.
Sujeto a revisiones menores.
Ver [SPEC](/docs/specs/ecies/) para la especificación oficial.

Las siguientes características no están implementadas a partir de la versión 0.9.46:

- Bloques MessageNumbers, Options y Termination
- Respuestas a nivel de protocolo
- Clave estática cero
- Multicast


## Visión general

Esta es una propuesta para el primer nuevo tipo de cifrado de extremo a extremo
desde el inicio de I2P, para reemplazar ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/).

Se basa en trabajos previos de la siguiente manera:

- Especificación de estructuras comunes [Common Structures](/docs/specs/common-structures/)
- Especificación [I2NP](/docs/specs/i2np/) incluyendo LS2
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) visión general de nueva criptografía asimétrica
- Visión general de criptografía de bajo nivel [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Proposal 111](/proposals/111-ntcp-2/)
- 123 Nuevas entradas en netDB
- 142 Nueva plantilla de criptografía
- Protocolo [Noise](https://noiseprotocol.org/noise.html)
- Algoritmo de doble trinquete [Signal](https://signal.org/docs/)

El objetivo es soportar nuevo cifrado para comunicación
de extremo a extremo, de destino a destino.

El diseño usará un handshake Noise y una fase de datos que incorpora el doble trinquete de Signal.

Todas las referencias a Signal y Noise en esta propuesta son solo para información de contexto.
No se requiere conocimiento de los protocolos Signal y Noise para entender
o implementar esta propuesta.


### Usos actuales de ElGamal

Como repaso,
las claves públicas ElGamal de 256 bytes pueden encontrarse en las siguientes estructuras de datos.
Consulte la especificación de estructuras comunes.

- En una Identidad de Router
  Esta es la clave de cifrado del router.

- En un Destino
  La clave pública del destino se usó para el antiguo cifrado i2cp-to-i2cp
  que fue desactivado en la versión 0.6, actualmente no se usa excepto por
  el IV para el cifrado del LeaseSet, que está obsoleto.
  En su lugar, se usa la clave pública en el LeaseSet.

- En un LeaseSet
  Esta es la clave de cifrado del destino.

- En un LS2
  Esta es la clave de cifrado del destino.



### Tipos de cifrado en certificados de clave

Como repaso,
agregamos soporte para tipos de cifrado cuando agregamos soporte para tipos de firma.
El campo de tipo de cifrado siempre es cero, tanto en Destinos como en RouterIdentities.
Si alguna vez se cambiará eso está por determinar.
Consulte la especificación de estructuras comunes [Common Structures](/docs/specs/common-structures/).




### Usos de criptografía asimétrica

Como repaso, usamos ElGamal para:

1) Mensajes de construcción de túnel (la clave está en RouterIdentity)
   El reemplazo no está cubierto en esta propuesta.
   Ver propuesta 152 [Proposal 152](/proposals/152-ecies-tunnels).

2) Cifrado router-a-router de netdb y otros mensajes I2NP (la clave está en RouterIdentity)
   Depende de esta propuesta.
   Requiere una propuesta para 1) también, o poner la clave en las opciones del RI.

3) Cifrado ElGamal+AES/SessionTag de cliente a extremo (la clave está en LeaseSet, la clave del Destino no se usa)
   El reemplazo SÍ está cubierto en esta propuesta.

4) DH efímero para NTCP1 y SSU
   El reemplazo no está cubierto en esta propuesta.
   Ver propuesta 111 para NTCP2.
   No hay propuesta actual para SSU2.


### Objetivos

- Compatible con versiones anteriores
- Requiere y se basa en LS2 (propuesta 123)
- Aprovechar nueva criptografía o primitivas agregadas para NTCP2 (propuesta 111)
- No se requiere nueva criptografía o primitivas para soporte
- Mantener la desacoplación entre criptografía y firmas; soportar todas las versiones actuales y futuras
- Habilitar nueva criptografía para destinos
- Habilitar nueva criptografía para routers, pero solo para mensajes de ajo - la construcción de túneles sería
  una propuesta separada
- No romper nada que dependa de hashes binarios de destino de 32 bytes, por ejemplo bittorrent
- Mantener entrega de mensajes 0-RTT usando DH efímero-estático
- No requerir almacenamiento en búfer / cola de mensajes en esta capa de protocolo;
  continuar soportando entrega ilimitada de mensajes en ambas direcciones sin esperar respuesta
- Actualizar a DH efímero-efímero después de 1 RTT
- Mantener el manejo de mensajes fuera de orden
- Mantener seguridad de 256 bits
- Agregar secreto hacia adelante
- Agregar autenticación (AEAD)
- Mucho más eficiente en CPU que ElGamal
- No depender de Java jbigi para hacer DH eficiente
- Minimizar operaciones DH
- Mucho más eficiente en ancho de banda que ElGamal (bloque ElGamal de 514 bytes)
- Soportar criptografía nueva y antigua en el mismo túnel si se desea
- El receptor puede distinguir eficientemente entre criptografía nueva y antigua que llega por
  el mismo túnel
- Otros no pueden distinguir entre criptografía nueva, antigua o futura
- Eliminar la clasificación de longitud de sesión nueva vs. existente (soportar relleno)
- No se requieren nuevos mensajes I2NP
- Reemplazar la suma de verificación SHA-256 en la carga útil AES con AEAD
- Soportar vinculación de sesiones de transmisión y recepción para que
  los acuses de recibo puedan ocurrir dentro del protocolo, en lugar de únicamente fuera de banda.
  Esto también permitirá que las respuestas tengan secreto hacia adelante inmediatamente.
- Habilitar cifrado de extremo a extremo de ciertos mensajes (almacenamiento de RouterInfo)
  que actualmente no hacemos debido al costo de CPU.
- No cambiar el Mensaje de Ajo I2NP
  ni el formato de Instrucciones de Entrega de Mensaje de Ajo.
- Eliminar campos no utilizados o redundantes en los formatos de Conjunto de Clavos de Ajo y Clavo.

Eliminar varios problemas con las etiquetas de sesión, incluyendo:

- Incapacidad de usar AES hasta la primera respuesta
- Falta de confiabilidad y bloqueos si se asume la entrega de etiquetas
- Ineficiente en ancho de banda, especialmente en la primera entrega
- Gran ineficiencia de espacio para almacenar etiquetas
- Gran sobrecarga de ancho de banda para entregar etiquetas
- Altamente complejo, difícil de implementar
- Difícil de ajustar para varios casos de uso
  (transmisión continua vs. datagramas, servidor vs. cliente, ancho de banda alto vs. bajo)
- Vulnerabilidades de agotamiento de memoria debido a la entrega de etiquetas


### No objetivos / Fuera de alcance

- Cambios en el formato LS2 (la propuesta 123 está terminada)
- Nuevo algoritmo de rotación DHT o generación de número aleatorio compartido
- Nuevo cifrado para la construcción de túneles.
  Ver propuesta 152 [Proposal 152](/proposals/152-ecies-tunnels).
- Nuevo cifrado para el cifrado de capa de túnel.
  Ver propuesta 153 [Proposal 153](/proposals/153-chacha20-layer-encryption).
- Métodos de cifrado, transmisión y recepción de mensajes I2NP DLM / DSM / DSRM.
  No cambia.
- No se soporta comunicación de LS1-a-LS2 o de ElGamal/AES-a-esta-propuesta.
  Esta propuesta es un protocolo bidireccional.
  Los destinos pueden manejar compatibilidad hacia atrás publicando dos leasesets
  usando los mismos túneles, o poniendo ambos tipos de cifrado en el LS2.
- Cambios en el modelo de amenazas
- Los detalles de implementación no se discuten aquí y se dejan a cada proyecto.
- (Optimista) Agregar extensiones o ganchos para soportar multicast



### Justificación

ElGamal/AES+SessionTag ha sido nuestro único protocolo de extremo a extremo durante aproximadamente 15 años,
esencialmente sin modificaciones al protocolo.
Ahora existen primitivas criptográficas que son más rápidas.
Necesitamos mejorar la seguridad del protocolo.
También hemos desarrollado estrategias heurísticas y soluciones para minimizar el
uso de memoria y ancho de banda del protocolo, pero esas estrategias
son frágiles, difíciles de ajustar y hacen que el protocolo sea aún más propenso
a fallar, causando la desconexión de la sesión.

Durante aproximadamente el mismo período, la especificación ElGamal/AES+SessionTag y la documentación relacionada
han descrito lo costoso en ancho de banda que es entregar etiquetas de sesión,
y han propuesto reemplazar la entrega de etiquetas de sesión con un "PRNG sincronizado".
Un PRNG sincronizado genera determinísticamente las mismas etiquetas en ambos extremos,
derivadas de una semilla común.
Un PRNG sincronizado también puede denominarse "trinquete".
Esta propuesta (finalmente) especifica ese mecanismo de trinquete, y elimina la entrega de etiquetas.

Al usar un trinquete (un PRNG sincronizado) para generar las
etiquetas de sesión, eliminamos la sobrecarga de enviar etiquetas de sesión
en el mensaje Nueva Sesión y mensajes posteriores cuando se necesiten.
Para un conjunto típico de etiquetas de 32 etiquetas, esto es 1KB.
Esto también elimina el almacenamiento de etiquetas de sesión en el lado emisor,
reduciendo así los requisitos de almacenamiento a la mitad.

Un handshake bidireccional completo, similar al patrón Noise IK, es necesario para evitar ataques de suplantación por compromiso de clave (KCI).
Ver la tabla "Propiedades de seguridad de carga útil" de Noise en [NOISE](https://noiseprotocol.org/noise.html).
Para más información sobre KCI, ver el artículo https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### Modelo de amenazas

El modelo de amenazas es algo diferente al de NTCP2 (propuesta 111).
Los nodos MitM son el OBEP y el IBGW y se asume que tienen vista completa de
la NetDB global actual o histórica, mediante colusión con floodfills.

El objetivo es evitar que estos MitMs clasifiquen el tráfico como
mensajes de sesión nueva y existente, o como criptografía nueva vs. antigua.



## Propuesta detallada

Esta propuesta define un nuevo protocolo de extremo a extremo para reemplazar ElGamal/AES+SessionTags.
El diseño usará un handshake Noise y una fase de datos que incorpora el doble trinquete de Signal.


### Resumen del diseño criptográfico

Hay cinco partes del protocolo que deben rediseñarse:


- 1) Los formatos contenedores de sesión nueva y existente
  se reemplazan con nuevos formatos.
- 2) ElGamal (claves públicas de 256 bytes, claves privadas de 128 bytes) se reemplaza
  con ECIES-X25519 (claves públicas y privadas de 32 bytes)
- 3) AES se reemplaza con
  AEAD_ChaCha20_Poly1305 (abreviado como ChaChaPoly a continuación)
- 4) SessionTags se reemplazará con trinquetes,
  que es esencialmente un PRNG criptográfico, sincronizado.
- 5) La carga útil AES, según se define en la especificación ElGamal/AES+SessionTags,
  se reemplaza con un formato de bloque similar al de NTCP2.

Cada uno de los cinco cambios tiene su propia sección a continuación.


### Nuevas primitivas criptográficas para I2P

Las implementaciones actuales del router I2P requerirán implementaciones para
las siguientes primitivas criptográficas estándar,
que no son requeridas por los protocolos I2P actuales:

- ECIES (pero esto es esencialmente X25519)
- Elligator2

Implementaciones del router I2P existentes que aún no hayan implementado [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/))
también requerirán implementaciones para:

- Generación de claves X25519 y DH
- AEAD_ChaCha20_Poly1305 (abreviado como ChaChaPoly a continuación)
- HKDF


### Tipo de criptografía

El tipo de criptografía (usado en el LS2) es 4.
Esto indica una clave pública X25519 de 32 bytes little-endian,
y el protocolo de extremo a extremo especificado aquí.

El tipo de criptografía 0 es ElGamal.
Los tipos de criptografía 1-3 están reservados para ECIES-ECDH-AES-SessionTag, ver propuesta 145 [Proposal 145](/proposals/145-ecies).


### Marco del protocolo Noise

Esta propuesta proporciona los requisitos basados en el Marco del Protocolo Noise
[NOISE](https://noiseprotocol.org/noise.html) (Revisión 34, 2018-07-11).
Noise tiene propiedades similares al protocolo Station-To-Station
[STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), que es la base del protocolo [SSU](/docs/legacy/ssu/). En términos de Noise, Alice
es el iniciador, y Bob es el respondedor.

Esta propuesta se basa en el protocolo Noise Noise_IK_25519_ChaChaPoly_SHA256.
(El identificador real para la función de derivación de clave inicial
es "Noise_IKelg2_25519_ChaChaPoly_SHA256"
para indicar extensiones I2P - ver sección KDF 1 a continuación)
Este protocolo Noise usa las siguientes primitivas:

- Patrón de handshake interactivo: IK
  Alice transmite inmediatamente su clave estática a Bob (I)
  Alice ya conoce la clave estática de Bob (K)

- Patrón de handshake unidireccional: N
  Alice no transmite su clave estática a Bob (N)

- Función DH: X25519
  DH X25519 con una longitud de clave de 32 bytes según se especifica en [RFC-7748](https://tools.ietf.org/html/rfc7748).

- Función de cifrado: ChaChaPoly
  AEAD_CHACHA20_POLY1305 según se especifica en [RFC-7539](https://tools.ietf.org/html/rfc7539) sección 2.8.
  Nonce de 12 bytes, con los primeros 4 bytes establecidos en cero.
  Idéntico al de [NTCP2](/docs/specs/ntcp2/).

- Función hash: SHA256
  Hash estándar de 32 bytes, ya usado ampliamente en I2P.


### Adiciones al marco

Esta propuesta define las siguientes mejoras a
Noise_IK_25519_ChaChaPoly_SHA256. Estos generalmente siguen las pautas en
[NOISE](https://noiseprotocol.org/noise.html) sección 13.

1) Las claves efímeras en texto claro se codifican con [Elligator2](https://elligator.cr.yp.to/).

2) La respuesta se antepone con una etiqueta en texto claro.

3) Se define el formato de carga útil para los mensajes 1, 2 y la fase de datos.
   Por supuesto, esto no está definido en Noise.

Todos los mensajes incluyen un encabezado de Mensaje de Ajo [I2NP](/docs/specs/i2np/).
La fase de datos usa cifrado similar a, pero no compatible con, la fase de datos de Noise.


### Patrones de handshake

Los handshakes usan patrones de handshake [Noise](https://noiseprotocol.org/noise.html).

Se usa la siguiente asignación de letras:

- e = clave efímera de un solo uso
- s = clave estática
- p = carga útil del mensaje

Las sesiones de un solo uso y sin enlazar son similares al patrón Noise N.

```

<- s
  ...
  e es p ->

```

Las sesiones enlazadas son similares al patrón Noise IK.

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### Sesiones

El protocolo actual ElGamal/AES+SessionTag es unidireccional.
En esta capa, el receptor no sabe de dónde viene un mensaje.
Las sesiones salientes y entrantes no están asociadas.
Los acuses de recibo son fuera de banda usando un DeliveryStatusMessage
(envuelto en un GarlicMessage) en el clavo.

Hay una ineficiencia sustancial en un protocolo unidireccional.
Cualquier respuesta también debe usar un costoso mensaje 'Nueva Sesión'.
Esto causa un mayor uso de ancho de banda, CPU y memoria.

También hay debilidades de seguridad en un protocolo unidireccional.
Todas las sesiones se basan en DH efímero-estático.
Sin una ruta de retorno, no hay forma de que Bob "trinque" su clave estática
a una clave efímera.
Sin saber de dónde viene un mensaje, no hay forma de usar
la clave efímera recibida para mensajes salientes,
por lo que la respuesta inicial también usa DH efímero-estático.

Para esta propuesta, definimos dos mecanismos para crear un protocolo bidireccional -
"emparejamiento" y "enlazado".
Estos mecanismos proporcionan mayor eficiencia y seguridad.


### Contexto de sesión

Al igual que con ElGamal/AES+SessionTags, todas las sesiones entrantes y salientes
deben estar en un contexto dado, ya sea el contexto del router o
el contexto para un destino local particular.
En Java I2P, este contexto se llama el Administrador de Claves de Sesión.

Las sesiones no deben compartirse entre contextos, ya que eso permitiría
la correlación entre los diversos destinos locales,
o entre un destino local y un router.

Cuando un destino dado soporta tanto ElGamal/AES+SessionTags
como esta propuesta, ambos tipos de sesiones pueden compartir un contexto.
Ver sección 1c) a continuación.



### Emparejamiento de sesiones entrantes y salientes

Cuando se crea una sesión saliente en el originador (Alice),
se crea una nueva sesión entrante y se empareja con la sesión saliente,
a menos que no se espere respuesta (por ejemplo, datagramas sin procesar).

Una nueva sesión entrante siempre se empareja con una nueva sesión saliente,
a menos que no se solicite respuesta (por ejemplo, datagramas sin procesar).

Si se solicita respuesta y se enlaza a un destino o router remoto,
esa nueva sesión saliente se enlaza a ese destino o router,
y reemplaza cualquier sesión saliente anterior a ese destino o router.

El emparejamiento de sesiones entrantes y salientes proporciona un protocolo bidireccional
con la capacidad de trinquear las claves DH.



### Enlazado de sesiones y destinos

Solo hay una sesión saliente hacia un destino o router determinado.
Puede haber varias sesiones entrantes actuales desde un destino o router determinado.
Generalmente, cuando se crea una nueva sesión entrante y se recibe tráfico
en esa sesión (lo que sirve como ACK), las demás se marcarán
para expirar relativamente rápido, dentro de un minuto o así.
Se verifica el valor de mensajes enviados previamente (PN), y si no hay
mensajes no recibidos (dentro del tamaño de la ventana) en la sesión entrante anterior,
la sesión anterior puede eliminarse inmediatamente.


Cuando se crea una sesión saliente en el originador (Alice),
se enlaza al destino remoto (Bob),
y cualquier sesión entrante emparejada también se enlazará al destino remoto.
A medida que las sesiones trinquean, continúan enlazadas al destino remoto.

Cuando se crea una sesión entrante en el receptor (Bob),
puede enlazarse al destino remoto (Alice), a opción de Alice.
Si Alice incluye información de enlazado (su clave estática) en el mensaje Nueva Sesión,
la sesión se enlazará a ese destino,
y se creará una sesión saliente y se enlazará al mismo destino.
A medida que las sesiones trinquean, continúan enlazadas al destino remoto.


### Beneficios del enlazado y emparejamiento

Para el caso común, de transmisión continua, esperamos que Alice y Bob usen el protocolo de la siguiente manera:

- Alice empareja su nueva sesión saliente con una nueva sesión entrante, ambas enlazadas al destino remoto (Bob).
- Alice incluye la información de enlazado y firma, y una solicitud de respuesta, en el
  mensaje Nueva Sesión enviado a Bob.
- Bob empareja su nueva sesión entrante con una nueva sesión saliente, ambas enlazadas al destino remoto (Alice).
- Bob envía una respuesta (ack) a Alice en la sesión emparejada, con un trinquete a una nueva clave DH.
- Alice trinca a una nueva sesión saliente con la nueva clave de Bob, emparejada a la sesión entrante existente.

Al enlazar una sesión entrante a un destino remoto, y emparejar la sesión entrante
a una sesión saliente enlazada al mismo destino, logramos dos beneficios principales:

1) La respuesta inicial de Bob a Alice usa DH efímero-efímero

2) Después de que Alice recibe la respuesta de Bob y trinca, todos los mensajes posteriores de Alice a Bob
usan DH efímero-efímero.


### ACKs de mensajes

En ElGamal/AES+SessionTags, cuando un LeaseSet se agrupa como un clavo de ajo,
o se entregan etiquetas, el router emisor solicita un ACK.
Este es un clavo de ajo separado que contiene un Mensaje de Estado de Entrega.
Por seguridad adicional, el Mensaje de Estado de Entrega está envuelto en un Mensaje de Ajo.
Este mecanismo es fuera de banda desde la perspectiva del protocolo.

En el nuevo protocolo, dado que las sesiones entrantes y salientes están emparejadas,
podemos tener ACKs dentro de la banda. No se requiere un clavo separado.

Un ACK explícito es simplemente un mensaje de Sesión Existente sin bloque I2NP.
Sin embargo, en la mayoría de los casos, se puede evitar un ACK explícito, ya que hay tráfico inverso.
Puede ser deseable que las implementaciones esperen un corto tiempo (quizás cien ms)
antes de enviar un ACK explícito, para dar tiempo a la capa de transmisión continua o de aplicación para responder.

Las implementaciones también necesitarán posponer cualquier envío de ACK hasta después de que
el bloque I2NP sea procesado, ya que el Mensaje de Ajo puede contener un Mensaje de Almacenamiento de Base de Datos
con un lease set. Un lease set reciente será necesario para enrutar el ACK,
y el destino remoto (contenido en el lease set) será necesario para
verificar la clave estática de enlazado.


### Tiempos de expiración de sesión

Las sesiones salientes siempre deben expirar antes que las entrantes.
Una vez que una sesión saliente expira y se crea una nueva, también se creará
una nueva sesión entrante emparejada. Si había una sesión entrante antigua,
se permitirá que expire.


### Multicast

Por determinar


### Definiciones
Definimos las siguientes funciones correspondientes a los bloques criptográficos utilizados.

ZEROLEN
    matriz de bytes de longitud cero

CSRNG(n)
    salida de n bytes de un generador de números aleatorios criptográficamente seguro.

H(p, d)
    función hash SHA-256 que toma una cadena de personalización p y datos d, y
    produce una salida de longitud 32 bytes.
    Como se define en [NOISE](https://noiseprotocol.org/noise.html).
    || a continuación significa concatenar.

    Usar SHA-256 de la siguiente manera::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    función hash SHA-256 que toma un hash anterior h y nuevos datos d,
    y produce una salida de longitud 32 bytes.
    || a continuación significa concatenar.

    Usar SHA-256 de la siguiente manera::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    El AEAD ChaCha20/Poly1305 según se especifica en [RFC-7539](https://tools.ietf.org/html/rfc7539).
    S_KEY_LEN = 32 y S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)
        Cifra plaintext usando la clave de cifrado k, y nonce n que DEBE ser único para
        la clave k.
        Los datos asociados ad son opcionales.
        Devuelve un texto cifrado del tamaño del texto plano + 16 bytes para el HMAC.

        Todo el texto cifrado debe ser indistinguible de aleatorio si la clave es secreta.

    DECRYPT(k, n, ciphertext, ad)
        Descifra ciphertext usando la clave de cifrado k, y nonce n.
        Los datos asociados ad son opcionales.
        Devuelve el texto plano.

DH
    Sistema de acuerdo de clave pública X25519. Claves privadas de 32 bytes, claves públicas de 32
    bytes, produce salidas de 32 bytes. Tiene las siguientes
    funciones:

    GENERATE_PRIVATE()
        Genera una nueva clave privada.

    DERIVE_PUBLIC(privkey)
        Devuelve la clave pública correspondiente a la clave privada dada.

    GENERATE_PRIVATE_ELG2()
        Genera una nueva clave privada que se mapea a una clave pública adecuada para codificación Elligator2.
        Nótese que la mitad de las claves privadas generadas aleatoriamente no serán adecuadas y deben descartarse.

    ENCODE_ELG2(pubkey)
        Devuelve la clave pública codificada con Elligator2 correspondiente a la clave pública dada (mapeo inverso).
        Las claves codificadas son little endian.
        La clave codificada debe ser de 256 bits indistinguible de datos aleatorios.
        Ver sección Elligator2 a continuación para especificación.

    DECODE_ELG2(pubkey)
        Devuelve la clave pública correspondiente a la clave pública codificada con Elligator2 dada.
        Ver sección Elligator2 a continuación para especificación.

    DH(privkey, pubkey)
        Genera un secreto compartido a partir de las claves privada y pública dadas.

HKDF(salt, ikm, info, n)
    Una función de derivación de clave criptográfica que toma material de clave de entrada ikm (que
    debe tener buena entropía pero no se requiere que sea una cadena uniformemente aleatoria), una sal
    de longitud 32 bytes, y un valor 'info' específico del contexto, y produce una salida
    de n bytes adecuada para uso como material de clave.

    Usar HKDF según se especifica en [RFC-5869](https://tools.ietf.org/html/rfc5869), usando la función hash HMAC SHA-256
    según se especifica en [RFC-2104](https://tools.ietf.org/html/rfc2104). Esto significa que SALT_LEN es como máximo 32 bytes.

MixKey(d)
    Usa HKDF() con una chainKey anterior y nuevos datos d, y
    establece la nueva chainKey y k.
    Como se define en [NOISE](https://noiseprotocol.org/noise.html).

    Usar HKDF de la siguiente manera::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) Formato de mensaje


### Revisión del formato de mensaje actual

El Mensaje de Ajo según se especifica en [I2NP](/docs/specs/i2np/) es el siguiente.
Como objetivo de diseño es que los nodos intermedios no puedan distinguir criptografía nueva de antigua,
este formato no puede cambiar, aunque el campo de longitud sea redundante.
El formato se muestra con el encabezado completo de 16 bytes, aunque el
encabezado real puede estar en un formato diferente, dependiendo del transporte usado.

Cuando se descifra, los datos contienen una serie de Clavos de Ajo y datos adicionales,
también conocidos como Conjunto de Clavos.

Ver [I2NP](/docs/specs/i2np/) para detalles y una especificación completa.


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### Revisión del formato de datos cifrados

El formato de mensaje actual, usado durante más de 15 años,
es ElGamal/AES+SessionTags.
En ElGamal/AES+SessionTags, hay dos formatos de mensaje:

1) Nueva sesión:
- Bloque ElGamal de 514 bytes
- Bloque AES (mínimo 128 bytes, múltiplo de 16)

2) Sesión existente:
- Etiqueta de sesión de 32 bytes
- Bloque AES (mínimo 128 bytes, múltiplo de 16)

El relleno mínimo a 128 es como se implementa en Java I2P pero no se aplica en la recepción.

Estos mensajes están encapsulados en un mensaje de ajo I2NP, que contiene
un campo de longitud, por lo que se conoce la longitud.

Nótese que no se define relleno a una longitud no múltiplo de 16,
por lo que la Nueva Sesión siempre es (mod 16 == 2),
y una Sesión Existente siempre es (mod 16 == 0).
Necesitamos arreglar esto.

El receptor primero intenta buscar los primeros 32 bytes como una Etiqueta de Sesión.
Si se encuentra, descifra el bloque AES.
Si no se encuentra, y los datos tienen al menos (514+16) de longitud, intenta descifrar el bloque ElGamal,
y si tiene éxito, descifra el bloque AES.


### Nuevas etiquetas de sesión y comparación con Signal

En Signal Double Ratchet, el encabezado contiene:

- DH: Clave pública actual del trinquete
- PN: Longitud del mensaje de cadena anterior
- N: Número de mensaje

Las "cadenas de envío" de Signal son aproximadamente equivalentes a nuestros conjuntos de etiquetas.
Al usar una etiqueta de sesión, podemos eliminar la mayor parte de eso.

En Nueva Sesión, ponemos solo la clave pública en el encabezado sin cifrar.

En Sesión Existente, usamos una etiqueta de sesión para el encabezado.
La etiqueta de sesión está asociada con la clave pública actual del trinquete,
y el número de mensaje.

Tanto en sesión nueva como existente, PN y N están en el cuerpo cifrado.

En Signal, las cosas están constantemente trinqueando. Una nueva clave pública DH requiere que el
receptor trinque y envíe una nueva clave pública de vuelta, lo que también sirve
como ack para la clave pública recibida.
Esto sería demasiadas operaciones DH para nosotros.
Así que separamos el ack de la clave recibida y la transmisión de una nueva clave pública.
Cualquier mensaje que use una etiqueta de sesión generada a partir de la nueva clave pública DH constituye un ACK.
Solo transmitimos una nueva clave pública cuando deseamos reconfigurar.

El número máximo de mensajes antes de que el DH deba trinquear es 65535.

Al entregar una clave de sesión, derivamos el "Conjunto de Etiquetas" a partir de ella,
en lugar de tener que entregar también etiquetas de sesión.
Un Conjunto de Etiquetas puede tener hasta 65536 etiquetas.
Sin embargo, los receptores deben implementar una estrategia de "búsqueda hacia adelante",
en lugar de generar todas las etiquetas posibles a la vez.
Solo genere como máximo N etiquetas después de la última etiqueta buena recibida.
N podría ser como máximo 128, pero 32 o incluso menos puede ser una mejor elección.



### 1a) Formato de nueva sesión

Clave pública efímera de nueva sesión (32 bytes)
Datos cifrados y MAC (bytes restantes)

El mensaje Nueva Sesión puede o no contener la clave pública estática del emisor.
Si se incluye, la sesión inversa se enlaza a esa clave.
La clave estática debe incluirse si se esperan respuestas,
es decir, para transmisión continua y datagramas con respuesta.
No debe incluirse para datagramas sin procesar.

El mensaje Nueva Sesión es similar al patrón unidireccional Noise [NOISE](https://noiseprotocol.org/noise.html)
"N" (si no se envía la clave estática),
o al patrón bidireccional "IK" (si se envía la clave estática).



### 1b) Formato de nueva sesión (con enlazado)

Longitud es 96 + longitud de carga útil.
Formato cifrado:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Clave Pública Efímera Nueva Sesión  |
  +             32 bytes                  +
  |     Codificada con Elligator2         |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         Clave Estática                +
  |       Datos cifrados ChaCha20         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +    (MAC) para sección Clave Estática  +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sección de Carga Útil      +
  |       Datos cifrados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +         (MAC) para sección Carga Útil +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Clave Pública :: 32 bytes, little endian, Elligator2, texto claro

  Datos cifrados Clave Estática :: 32 bytes

  Datos cifrados Sección Carga Útil :: datos restantes menos 16 bytes

  MAC :: Código de autenticación de mensaje Poly1305, 16 bytes

```


### Clave efímera de nueva sesión

La clave efímera es de 32 bytes, codificada con Elligator2.
Esta clave nunca se reutiliza; se genera una nueva clave con
cada mensaje, incluyendo retransmisiones.

### Clave estática

Cuando se descifra, la clave estática X25519 de Alice, 32 bytes.


### Carga útil

La longitud cifrada es el resto de los datos.
La longitud descifrada es 16 menos que la longitud cifrada.
La carga útil debe contener un bloque DateTime y generalmente contendrá uno o más bloques de Clavo de Ajo.
Ver la sección de carga útil a continuación para formato y requisitos adicionales.



### 1c) Formato de nueva sesión (sin enlazado)

Si no se requiere respuesta, no se envía clave estática.


Longitud es 96 + longitud de carga útil.
Formato cifrado:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Clave Pública Efímera Nueva Sesión  |
  +             32 bytes                  +
  |     Codificada con Elligator2         |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Sección de Banderas         +
  |       Datos cifrados ChaCha20         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +         (MAC) para sección anterior   +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sección de Carga Útil      +
  |       Datos cifrados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +         (MAC) para sección Carga Útil +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Clave Pública :: 32 bytes, little endian, Elligator2, texto claro

  Datos cifrados Sección de Banderas :: 32 bytes

  Datos cifrados Sección Carga Útil :: datos restantes menos 16 bytes

  MAC :: Código de autenticación de mensaje Poly1305, 16 bytes

```

### Clave efímera de nueva sesión

Clave efímera de Alice.
La clave efímera es de 32 bytes, codificada con Elligator2, little endian.
Esta clave nunca se reutiliza; se genera una nueva clave con
cada mensaje, incluyendo retransmisiones.


### Datos descifrados de sección de banderas

La sección de banderas no contiene nada.
Siempre es de 32 bytes, porque debe tener la misma longitud
que la clave estática para mensajes de Nueva Sesión con enlazado.
Bob determina si es una clave estática o una sección de banderas
probando si los 32 bytes son todos ceros.

¿FALTAN banderas necesarias aquí?

### Carga útil

La longitud cifrada es el resto de los datos.
La longitud descifrada es 16 menos que la longitud cifrada.
La carga útil debe contener un bloque DateTime y generalmente contendrá uno o más bloques de Clavo de Ajo.
Ver la sección de carga útil a continuación para formato y requisitos adicionales.




### 1d) Formato de un solo uso (sin enlazado ni sesión)

Si solo se espera enviar un solo mensaje,
no se requiere configuración de sesión ni clave estática.


Longitud es 96 + longitud de carga útil.
Formato cifrado:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Clave Pública Efímera           |
  +             32 bytes                  +
  |     Codificada con Elligator2         |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Sección de Banderas         +
  |       Datos cifrados ChaCha20         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +         (MAC) para sección anterior   +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sección de Carga Útil      +
  |       Datos cifrados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +         (MAC) para sección Carga Útil +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Clave Pública :: 32 bytes, little endian, Elligator2, texto claro

  Datos cifrados Sección de Banderas :: 32 bytes

  Datos cifrados Sección Carga Útil :: datos restantes menos 16 bytes

  MAC :: Código de autenticación de mensaje Poly1305, 16 bytes

```


### Clave efímera de una sola vez

La clave de una sola vez es de 32 bytes, codificada con Elligator2, little endian.
Esta clave nunca se reutiliza; se genera una nueva clave con
cada mensaje, incluyendo retransmisiones.


### Datos descifrados de sección de banderas

La sección de banderas no contiene nada.
Siempre es de 32 bytes, porque debe tener la misma longitud
que la clave estática para mensajes de Nueva Sesión con enlazado.
Bob determina si es una clave estática o una sección de banderas
probando si los 32 bytes son todos ceros.

¿FALTAN banderas necesarias aquí?

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             Todos ceros               +
  |              32 bytes                 |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  ceros:: Todos ceros, 32 bytes.

```


### Carga útil

La longitud cifrada es el resto de los datos.
La longitud descifrada es 16 menos que la longitud cifrada.
La carga útil debe contener un bloque DateTime y generalmente contendrá uno o más bloques de Clavo de Ajo.
Ver la sección de carga útil a continuación para formato y requisitos adicionales.



### 1f) KDFs para mensaje Nueva Sesión

### KDF para ChainKey inicial

Este es el estándar [NOISE](https://noiseprotocol.org/noise.html) para IK con un nombre de protocolo modificado.
Nótese que usamos el mismo inicializador tanto para el patrón IK (sesiones enlazadas)
como para el patrón N (sesiones sin enlazar).

El nombre del protocolo se modifica por dos razones.
Primero, para indicar que las claves efímeras están codificadas con Elligator2,
y segundo, para indicar que MixHash() se llama antes del segundo mensaje
para mezclar el valor de la etiqueta.

```

Este es el patrón de mensaje "e":

  // Definir protocol_name.
  Establecer protocol_name = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 bytes, codificado en US-ASCII, sin terminación NULL).

  // Definir Hash h = 32 bytes
  h = SHA256(protocol_name);

  Definir ck = 32 bytes de clave de encadenamiento. Copiar los datos de h a ck.
  Establecer chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // hasta aquí, puede precalcularse todo por Alice para todas las conexiones salientes

```


### KDF para contenido cifrado de sección de Claves/Banderas

```

Este es el patrón de mensaje "e":

  // Claves X25519 estáticas de Bob
  // bpk se publica en leaseset
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Clave pública estática de Bob
  // MixHash(bpk)
  // || a continuación significa concatenar
  h = SHA256(h || bpk);

  // hasta aquí, puede precalcularse todo por Bob para todas las conexiones entrantes

  // Claves X25519 efímeras de Alice
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Clave pública efímera de Alice
  // MixHash(aepk)
  // || a continuación significa concatenar
  h = SHA256(h || aepk);

  // h se usa como datos asociados para el AEAD en el mensaje Nueva Sesión
  // Retener el Hash h para el KDF de Respuesta Nueva Sesión
  // eapk se envía en texto claro al
  // comienzo del mensaje Nueva Sesión
  elg2_aepk = ENCODE_ELG2(aepk)
  // Como descodificado por Bob
  aepk = DECODE_ELG2(elg2_aepk)

  Fin del patrón de mensaje "e".

  Este es el patrón de mensaje "es":

  // Noise es
  sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parámetros ChaChaPoly para cifrar/descifrar
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parámetros AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, sección claves/banderas, ad)

  Fin del patrón de mensaje "es".

  Este es el patrón de mensaje "s":

  // MixHash(ciphertext)
  // Guardar para KDF sección Carga Útil
  h = SHA256(h || ciphertext)

  // Claves X25519 estáticas de Alice
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  Fin del patrón de mensaje "s".


```



### KDF para sección de carga útil (con clave estática de Alice)

```

Este es el patrón de mensaje "ss":

  // Noise ss
  sharedSecret = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parámetros ChaChaPoly para cifrar/descifrar
  // chainKey de sección Clave Estática
  Establecer sharedSecret = resultado DH X25519
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parámetros AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, carga útil, ad)

  Fin del patrón de mensaje "ss".

  // MixHash(ciphertext)
  // Guardar para KDF Respuesta Nueva Sesión
  h = SHA256(h || ciphertext)

```


### KDF para sección de carga útil (sin clave estática de Alice)

Nótese que esto es un patrón Noise "N", pero usamos el mismo inicializador "IK"
que para sesiones enlazadas.

Los mensajes Nueva Sesión no pueden identificarse como conteniendo la clave estática de Alice o no
hasta que la clave estática se descifre e inspeccione para determinar si contiene todos ceros.
Por lo tanto, el receptor debe usar la máquina de estados "IK" para todos
los mensajes Nueva Sesión.
Si la clave estática es todo ceros, el patrón de mensaje "ss" debe omitirse.



```

chainKey = de sección Claves/Banderas
  k = de sección Claves/Banderas
  n = 1
  ad = h de sección Claves/Banderas
  ciphertext = ENCRYPT(k, n, carga útil, ad)

```



### 1g) Formato de Respuesta Nueva Sesión

Una o más Respuestas Nueva Sesión pueden enviarse en respuesta a un solo mensaje Nueva Sesión.
Cada respuesta va precedida por una etiqueta, que se genera a partir de un Conjunto de Etiquetas para la sesión.

La Respuesta Nueva Sesión tiene dos partes.
La primera parte es la finalización del handshake Noise IK con una etiqueta antepuesta.
La longitud de la primera parte es de 56 bytes.
La segunda parte es la carga útil de la fase de datos.
La longitud de la segunda parte es de 16 + longitud de carga útil.

Longitud total es 72 + longitud de carga útil.
Formato cifrado:

```

+----+----+----+----+----+----+----+----+
  |       Etiqueta de Sesión   8 bytes    |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Clave Pública Efímera          +
  |                                       |
  +            32 bytes                   +
  |     Codificada con Elligator2         |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +  (MAC) para sección Clave (sin datos) +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sección de Carga Útil      +
  |       Datos cifrados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +         (MAC) para sección Carga Útil +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Etiqueta :: 8 bytes, texto claro

  Clave Pública :: 32 bytes, little endian, Elligator2, texto claro

  MAC :: Código de autenticación de mensaje Poly1305, 16 bytes
         Nota: Los datos de texto plano ChaCha20 están vacíos (ZEROLEN)

  Datos cifrados Sección Carga Útil :: datos restantes menos 16 bytes

  MAC :: Código de autenticación de mensaje Poly1305, 16 bytes

```

### Etiqueta de sesión
La etiqueta se genera en el KDF de Etiquetas de Sesión, como se inicializa
en el KDF de Inicialización DH a continuación.
Esto correlaciona la respuesta con la sesión.
La Clave de Sesión del Inicialización DH no se usa.


### Clave efímera de Respuesta Nueva Sesión

Clave efímera de Bob.
La clave efímera es de 32 bytes, codificada con Elligator2, little endian.
Esta clave nunca se reutiliza; se genera una nueva clave con
cada mensaje, incluyendo retransmisiones.


### Carga útil
La longitud cifrada es el resto de los datos.
La longitud descifrada es 16 menos que la longitud cifrada.
La carga útil generalmente contendrá uno o más bloques de Clavo de Ajo.
Ver la sección de carga útil a continuación para formato y requisitos adicionales.


### KDF para Conjunto de Etiquetas de Respuesta

Una o más etiquetas se crean a partir del Conjunto de Etiquetas, que se inicializa usando
el KDF a continuación, usando el chainKey del mensaje Nueva Sesión.

```

// Generar conjunto de etiquetas
  tagsetKey = HKDF(chainKey, ZEROLEN, "SessionReplyTags", 32)
  tagset_nsr = DH_INITIALIZE(chainKey, tagsetKey)

```


### KDF para contenido cifrado de sección de clave de respuesta

```

// Claves del mensaje Nueva Sesión
  // Claves X25519 de Alice
  // apk y aepk se envían en el mensaje Nueva Sesión original
  // ask = clave privada estática de Alice
  // apk = clave pública estática de Alice
  // aesk = clave privada efímera de Alice
  // aepk = clave pública efímera de Alice
  // Claves X25519 estáticas de Bob
  // bsk = clave privada estática de Bob
  // bpk = clave pública estática de Bob

  // Generar la etiqueta
  tagsetEntry = tagset_nsr.GET_NEXT_ENTRY()
  tag = tagsetEntry.SESSION_TAG

  // MixHash(tag)
  h = SHA256(h || tag)

  Este es el patrón de mensaje "e":

  // Claves X25519 efímeras de Bob
  besk = GENERATE_PRIVATE_ELG2()
  bepk = DERIVE_PUBLIC(besk)

  // Clave pública efímera de Bob
  // MixHash(bepk)
  // || a continuación significa concatenar
  h = SHA256(h || bepk);

  // elg2_bepk se envía en texto claro al
  // comienzo del mensaje Nueva Sesión
  elg2_bepk = ENCODE_ELG2(bepk)
  // Como descodificado por Bob
  bepk = DECODE_ELG2(elg2_bepk)

  Fin del patrón de mensaje "e".

  Este es el patrón de mensaje "ee":

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parámetros ChaChaPoly para cifrar/descifrar
  // chainKey de sección Carga Útil Nueva Sesión original
  sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
  keydata = HKDF(chainKey, sharedSecret, "", 32)
  chainKey = keydata[0:31]

  Fin del patrón de mensaje "ee".

  Este es el patrón de mensaje "se":

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  sharedSecret = DH(ask, bepk) = DH(besk, apk)
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parámetros AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, ZEROLEN, ad)

  Fin del patrón de mensaje "se".

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  chainKey se usa en el trinquete a continuación.

```


### KDF para contenido cifrado de sección de carga útil

Esto es como el primer mensaje de Sesión Existente,
post-división, pero sin una etiqueta separada.
Además, usamos el hash de arriba para vincular la
carga útil al mensaje NSR.


```

// split()
  keydata = HKDF(chainKey, ZEROLEN, "", 64)
  k_ab = keydata[0:31]
  k_ba = keydata[32:63]
  tagset_ab = DH_INITIALIZE(chainKey, k_ab)
  tagset_ba = DH_INITIALIZE(chainKey, k_ba)

  // Parámetros AEAD para carga útil Respuesta Nueva Sesión
  k = HKDF(k_ba, ZEROLEN, "AttachPayloadKDF", 32)
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, carga útil, ad)
```


### Notas

Pueden enviarse múltiples mensajes NSR como respuesta, cada uno con claves efímeras únicas, dependiendo del tamaño de la respuesta.

Alice y Bob deben usar nuevas claves efímeras para cada mensaje NS y NSR.

Alice debe recibir uno de los mensajes NSR de Bob antes de enviar mensajes de Sesión Existente (ES),
y Bob debe recibir un mensaje ES de Alice antes de enviar mensajes ES.

El ``chainKey`` y ``k`` de la sección de carga útil del NSR de Bob se usan
como entradas para los trinquetes DH iniciales ES (ambas direcciones, ver KDF de trinquete DH).

Bob solo debe mantener Sesiones Existente para los mensajes ES recibidos de Alice.
Cualquier otra sesión entrante y saliente creada (para múltiples NSR) debe ser
destruida inmediatamente después de recibir el primer mensaje ES de Alice para una sesión dada.



### 1h) Formato de sesión existente

Etiqueta de sesión (8 bytes)
Datos cifrados y MAC (ver sección 3 a continuación)


### Formato
Cifrado:

```

+----+----+----+----+----+----+----+----+
  |       Etiqueta de Sesión              |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sección de Carga Útil      +
  |       Datos cifrados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +              (MAC)                    +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Etiqueta de Sesión :: 8 bytes, texto claro

  Datos cifrados Sección Carga Útil :: datos restantes menos 16 bytes

  MAC :: Código de autenticación de mensaje Poly1305, 16 bytes

```


### Carga útil
La longitud cifrada es el resto de los datos.
La longitud descifrada es 16 menos que la longitud cifrada.
Ver la sección de carga útil a continuación para formato y requisitos.


KDF

```
Ver sección AEAD a continuación.

  // Parámetros AEAD para carga útil Sesión Existente
  k = La clave de sesión de 32 bytes asociada con esta etiqueta de sesión
  n = El número de mensaje N en la cadena actual, como se recupera de la etiqueta de sesión asociada.
  ad = La etiqueta de sesión, 8 bytes
  ciphertext = ENCRYPT(k, n, carga útil, ad)
```



### 2) ECIES-X25519


Formato: claves públicas y privadas de 32 bytes, little-endian.

Justificación: Usado en [NTCP2](/docs/specs/ntcp2/).



### 2a) Elligator2

En handshakes Noise estándar, los mensajes iniciales de handshake en cada dirección comienzan con
claves efímeras que se transmiten en texto claro.
Como las claves X25519 válidas son distinguibles de aleatorias, un hombre en el medio puede distinguir
estos mensajes de mensajes de Sesión Existente que comienzan con etiquetas de sesión aleatorias.
En [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/)), usamos una función XOR de bajo sobrecoste usando la clave estática fuera de banda para ofuscar
la clave. Sin embargo, el modelo de amenazas aquí es diferente; no queremos permitir que ningún MitM
use ningún medio para confirmar el destino del tráfico, o para distinguir
los mensajes iniciales de handshake de mensajes de Sesión Existente.

Por lo tanto, [Elligator2](https://elligator.cr.yp.to/) se usa para transformar las claves efímeras en los mensajes Nueva Sesión y Respuesta Nueva Sesión
para que sean indistinguibles de cadenas aleatorias uniformes.



### Formato

Claves públicas y privadas de 32 bytes.
Las claves codificadas son little endian.

Como se define en [Elligator2](https://elligator.cr.yp.to/), las claves codificadas son indistinguibles de 254 bits aleatorios.
Requerimos 256 bits aleatorios (32 bytes). Por lo tanto, la codificación y decodificación se
definen de la siguiente manera:

Codificación:

```

Definición ENCODE_ELG2()

  // Codificar según se define en especificación Elligator2
  encodedKey = encode(pubkey)
  // O en 2 bits aleatorios al MSB
  randomByte = CSRNG(1)
  encodedKey[31] |= (randomByte & 0xc0)
```


Decodificación:

```

Definición DECODE_ELG2()

  // Enmascarar 2 bits aleatorios del MSB
  encodedKey[31] &= 0x3f
  // Decodificar según se define en especificación Elligator2
  pubkey = decode(encodedKey)
```




### Justificación

Requerido para evitar que el OBEP y el IBGW clasifiquen el tráfico.


### Notas

Elligator2 duplica en promedio el tiempo de generación de claves, ya que la mitad de las claves privadas
dan como resultado claves públicas que no son adecuadas para codificación con Elligator2.
Además, el tiempo de generación de claves es ilimitado con una distribución exponencial,
ya que el generador debe seguir intentando hasta encontrar un par de claves adecuado.

Esta sobrecarga puede gestionarse generando claves por adelantado,
en un hilo separado, para mantener un grupo de claves adecuadas.

El generador hace la función ENCODE_ELG2() para determinar la adecuación.
Por lo tanto, el generador debería almacenar el resultado de ENCODE_ELG2()
para que no tenga que calcularse de nuevo.

Además, las claves no adecuadas pueden agregarse al grupo de claves
usadas para [NTCP2](/docs/specs/ntcp2/), donde no se usa Elligator2.
Los problemas de seguridad de hacerlo están por determinar.




### 3) AEAD (ChaChaPoly)

AEAD usando ChaCha20 y Poly1305, igual que en [NTCP2](/docs/specs/ntcp2/).
Esto corresponde a [RFC-7539](https://tools.ietf.org/html/rfc7539), que también se usa
de manera similar en TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).



### Entradas de Nueva Sesión y Respuesta Nueva Sesión

Entradas a las funciones de cifrado/descifrado
para un bloque AEAD en un mensaje Nueva Sesión:

```

k :: clave de cifrado de 32 bytes
       Ver KDFs de Nueva Sesión y Respuesta Nueva Sesión arriba.

  n :: nonce basado en contador, 12 bytes.
       n = 0

  ad :: Datos asociados, 32 bytes.
        El hash SHA256 de los datos anteriores, como salida de mixHash()

  data :: Datos de texto plano, 0 o más bytes

```


### Entradas de Sesión Existente

Entradas a las funciones de cifrado/descifrado
para un bloque AEAD en un mensaje de Sesión Existente:

```

k :: clave de sesión de 32 bytes
       Como se busca desde la etiqueta de sesión acompañante.

  n :: nonce basado en contador, 12 bytes.
       Comienza en 0 y se incrementa para cada mensaje al transmitir.
       Para el receptor, el valor
       como se busca desde la etiqueta de sesión acompañante.
       Los primeros cuatro bytes siempre son cero.
       Los últimos ocho bytes son el número de mensaje (n), codificados little-endian.
       Valor máximo es 65535.
       La sesión debe trinquear cuando N alcance ese valor.
       Nunca deben usarse valores superiores.

  ad :: Datos asociados
        La etiqueta de sesión

  data :: Datos de texto plano, 0 o más bytes

```


### Formato cifrado

Salida de la función de cifrado, entrada a la función de descifrado:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Datos cifrados ChaCha20         |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticación de Mensaje   |
  +              (MAC)                    +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  datos cifrados :: Mismo tamaño que los datos de texto plano, 0 - 65519 bytes

  MAC :: Código de autenticación de mensaje Poly1305, 16 bytes

```

### Notas
- Dado que ChaCha20 es un cifrado de flujo, no es necesario rellenar los textos planos.
  Se descartan bytes adicionales de flujo de clave.

- La clave para el cifrado (256 bits) se acuerda mediante el KDF SHA256.
  Los detalles del KDF para cada mensaje están en secciones separadas a continuación.

- Los marcos ChaChaPoly son de tamaño conocido ya que están encapsulados en el mensaje de datos I2NP.

- Para todos los mensajes,
  el relleno está dentro del
  marco de datos autenticados.


### Manejo de errores AEAD

Todos los datos recibidos que fallen la verificación AEAD deben descartarse.
No se devuelve ninguna respuesta.


### Justificación

Usado en [NTCP2](/docs/specs/ntcp2/).



### 4) Trinquetes

Todavía usamos etiquetas de sesión, como antes, pero usamos trinquetes para generarlas.
Las etiquetas de sesión también tenían una opción de reconfiguración que nunca implementamos.
Así que es como un doble trinquete pero nunca hicimos el segundo.

Aquí definimos algo similar al Doble Trinquete de Signal.
Las etiquetas de sesión se generan de forma determinista e idéntica en
los lados del emisor y receptor.

Al usar un trinquete simétrico/etiqueta, eliminamos el uso de memoria para almacenar etiquetas de sesión en el lado del emisor.
También eliminamos el consumo de ancho de banda de enviar conjuntos de etiquetas.
El uso del lado del receptor

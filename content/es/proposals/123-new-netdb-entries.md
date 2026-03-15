---
title: "Nuevas Entradas en netDB"
number: "123"
author: "zzz, str4d, orignal"
created: "2016-01-16"
lastupdated: "2020-07-18"
status: "Abrir"
thread: "http://zzz.i2p/topics/2051"
supercedes: "110, 120, 121, 122"
toc: true
---
## Estado

Partes de esta propuesta están completas e implementadas en las versiones 0.9.38 y 0.9.39.  
Las estructuras comunes, I2CP, I2NP y otras especificaciones  
ahora están actualizadas para reflejar los cambios que actualmente se admiten.

Las partes completadas aún están sujetas a revisiones menores.  
Otras partes de esta propuesta aún están en desarrollo  
y están sujetas a revisiones sustanciales.

La búsqueda de servicios (tipos 9 y 11) tiene baja prioridad,  
no está programada y podría separarse en una propuesta distinta.


## Visión general

Esta es una actualización y agregación de las siguientes 4 propuestas:

- 110 LS2
- 120 Meta LS2 para multihoming masivo
- 121 LS2 Cifrado
- 122 Búsqueda de servicio sin autenticación (anycasting)

Estas propuestas son mayormente independientes, pero por coherencia definimos y usamos un  
formato común para varias de ellas.

Las siguientes propuestas están relacionadas:

- 140 Multihoming Invisible (incompatible con esta propuesta)
- 142 Nueva Plantilla de Criptografía (para nueva criptografía simétrica)
- 144 ECIES-X25519-AEAD-Ratchet
- 145 ECIES-P256
- 146 Red25519
- 148 EdDSA-BLAKE2b-Ed25519
- 149 B32 para LS2 Cifrado
- 150 Protocolo Garlic Farm
- 151 ECDSA Blinding


## Propuesta

Esta propuesta define 5 nuevos tipos de DatabaseEntry y el proceso para  
almacenarlos y recuperarlos desde la base de datos de red,  
así como el método para firmarlos y verificar esas firmas.

### Objetivos

- Compatibilidad hacia atrás
- LS2 usable con multihoming de estilo antiguo
- No se requiere nueva criptografía ni primitivas para el soporte
- Mantener la desacoplación entre criptografía y firma; soportar todas las versiones actuales y futuras
- Habilitar claves de firma opcionales fuera de línea
- Reducir la precisión de las marcas de tiempo para reducir el rastreo por huellas
- Habilitar nueva criptografía para destinos
- Habilitar multihoming masivo
- Corregir múltiples problemas con el LS cifrado existente
- Ofuscar opcionalmente para reducir la visibilidad por floodfills
- Cifrado soporta tanto claves únicas como múltiples claves revocables
- Búsqueda de servicios para facilitar la búsqueda de outproxies, arranque de DHT de aplicaciones,  
  y otros usos
- No romper nada que dependa de hashes binarios de destino de 32 bytes, por ejemplo bittorrent
- Añadir flexibilidad a leasesets mediante propiedades, como tenemos en routerinfos.
- Poner la marca de tiempo de publicación y expiración variable en el encabezado, para que funcione incluso  
  si el contenido está cifrado (no derivar la marca de tiempo de la primera lease)
- Todos los nuevos tipos viven en el mismo espacio DHT y ubicaciones que los leasesets existentes,  
  para que los usuarios puedan migrar del antiguo LS a LS2,  
  o cambiar entre LS2, Meta y Cifrado,  
  sin cambiar el Destino o el hash.
- Un Destino existente puede convertirse para usar claves fuera de línea,  
  o volver a claves en línea, sin cambiar el Destino o el hash.


### No objetivos / Fuera de alcance

- Nuevo algoritmo de rotación DHT o generación compartida de números aleatorios
- El tipo específico de nueva encriptación y esquema de cifrado extremo a extremo  
  para usar ese nuevo tipo estaría en una propuesta separada.  
  No se especifica ni discute nueva criptografía aquí.
- Nueva encriptación para RIs o construcción de túneles.  
  Eso estaría en una propuesta separada.
- Métodos de encriptación, transmisión y recepción de mensajes I2NP DLM / DSM / DSRM.  
  No cambia.
- Cómo generar y soportar Meta, incluyendo comunicación inter-routers, gestión, conmutación por error y coordinación.  
  El soporte podría añadirse a I2CP, o i2pcontrol, o un nuevo protocolo.  
  Esto podría o no estandarizarse.
- Cómo implementar y gestionar realmente túneles de expiración más larga, o cancelar túneles existentes.  
  Es extremadamente difícil, y sin ello, no puedes tener un apagado ordenado razonable.
- Cambios en el modelo de amenazas
- Formato de almacenamiento fuera de línea, o métodos para almacenar/recuperar/compartir los datos.
- Los detalles de implementación no se discuten aquí y se dejan a cada proyecto.



### Justificación

LS2 añade campos para cambiar el tipo de encriptación y para futuros cambios de protocolo.

LS2 Cifrado corrige varios problemas de seguridad del LS cifrado existente mediante  
el uso de encriptación asimétrica de todo el conjunto de leases.

Meta LS2 proporciona multihoming flexible, eficiente, efectivo y a gran escala.

El Registro de Servicio y la Lista de Servicios proporcionan servicios anycast como búsqueda de nombres  
y arranque de DHT.


### Tipos de Datos NetDB

Los números de tipo se usan en los mensajes I2NP de Búsqueda/Almacenamiento en la Base de Datos.

La columna de extremo a extremo indica si las consultas/respuestas se envían a un Destino en un mensaje Garlic.


Tipos existentes:

| NetDB Data | Lookup Type | Store Type |
|------------|-------------|------------|
| any        | 0           | any        |
| LS         | 1           | 1          |
| RI         | 2           | 0          |
| exploratory| 3           | DSRM       |

Nuevos tipos:

| NetDB Data     | Lookup Type | Store Type | Std. LS2 Header? | Sent end-to-end? |
|----------------|-------------|------------|------------------|------------------|
| LS2            | 1           | 3          | yes              | yes              |
| Encrypted LS2  | 1           | 5          | no               | no               |
| Meta LS2       | 1           | 7          | yes              | no               |
| Service Record | n/a         | 9          | yes              | no               |
| Service List   | 4           | 11         | no               | no               |



### Notas

- Los tipos de búsqueda actualmente usan los bits 3-2 en el mensaje de Búsqueda en la Base de Datos.  
  Cualquier tipo adicional requeriría el uso del bit 4.

- Todos los tipos de almacenamiento son impares, ya que los bits superiores en el campo de tipo del mensaje de Almacenamiento en la Base de Datos  
  son ignorados por routers antiguos.  
  Preferimos que el análisis falle como un LS que como un RI comprimido.

- ¿Debe el tipo ser explícito, implícito o ninguno en los datos cubiertos por la firma?



### Proceso de Búsqueda/Almacenamiento

Los tipos 3, 5 y 7 pueden devolverse como respuesta a una búsqueda estándar de leaseset (tipo 1).  
El tipo 9 nunca se devuelve como respuesta a una búsqueda.  
El tipo 11 se devuelve como respuesta a un nuevo tipo de búsqueda de servicio (tipo 11).

Solo el tipo 3 puede enviarse en un mensaje Garlic de cliente a cliente.



### Formato

Los tipos 3, 7 y 9 tienen un formato común::

  Encabezado Estándar LS2
  - como se define a continuación

  Parte Específica del Tipo
  - como se define a continuación en cada parte

  Firma Estándar LS2:
  - Longitud según el tipo de firma de la clave de firma

El tipo 5 (Cifrado) no comienza con un Destino y tiene un  
formato diferente. Ver más abajo.

El tipo 11 (Lista de Servicios) es una agregación de varios Registros de Servicio y tiene un  
formato diferente. Ver más abajo.


### Consideraciones de Privacidad/Seguridad

TBD



## Encabezado Estándar LS2

Los tipos 3, 7 y 9 usan el encabezado estándar LS2, especificado a continuación:


### Formato

```
Encabezado Estándar LS2:
  - Tipo (1 byte)
    No está realmente en el encabezado, pero forma parte de los datos cubiertos por la firma.
    Tómese del campo en el mensaje de Almacenamiento en la Base de Datos.
  - Destino (387+ bytes)
  - Marca de tiempo de publicación (4 bytes, big endian, segundos desde la época, se reinicia en 2106)
  - Expira (2 bytes, big endian) (desplazamiento desde la marca de tiempo de publicación en segundos, máximo 18.2 horas)
  - Flags (2 bytes)
    Orden de bits: 15 14 ... 3 2 1 0
    Bit 0: Si 0, sin claves fuera de línea; si 1, claves fuera de línea
    Bit 1: Si 0, un leaseset publicado estándar.
           Si 1, un leaseset no publicado. No debería ser inundado, publicado ni
           enviado como respuesta a una consulta. Si este leaseset expira, no consulte la
           base de datos de red para uno nuevo, a menos que el bit 2 esté activado.
    Bit 2: Si 0, un leaseset publicado estándar.
           Si 1, este leaseset sin cifrar será ofuscado y cifrado al publicarse.
           Si este leaseset expira, consulte la ubicación ofuscada en la base de datos de red para uno nuevo.
           Si este bit se establece en 1, también establezca el bit 1 en 1.
           A partir de la versión 0.9.42.
    Bits 3-15: establecidos en 0 para compatibilidad con usos futuros
  - Si la bandera indica claves fuera de línea, la sección de firma fuera de línea:
    Marca de tiempo de expiración (4 bytes, big endian, segundos desde la época, se reinicia en 2106)
    Tipo de firma transitoria (2 bytes, big endian)
    Clave pública de firma transitoria (longitud según el tipo de firma)
    Firma de la marca de tiempo de expiración, tipo de firma transitoria y clave pública,
    por la clave pública del destino,
    longitud según el tipo de firma de la clave pública del destino.
    Esta sección puede, y debería, generarse fuera de línea.
```

### Justificación

- No publicado/publicado: Para uso al enviar un almacenamiento de base de datos extremo a extremo,  
  el router emisor puede desear indicar que este leaseset no debería enviarse a otros. Actualmente usamos heurísticas para mantener este estado.

- Publicado: Reemplaza la lógica compleja necesaria para determinar la 'versión' del  
  leaseset. Actualmente, la versión es la expiración de la última lease,  
  y un router publicador debe incrementar esa expiración al menos 1ms al  
  publicar un leaseset que solo elimina una lease más antigua.

- Expira: Permite que la expiración de una entrada de base de datos sea anterior a la de  
  su última lease. Puede no ser útil para LS2, donde se espera que los leasesets  
  permanezcan con una expiración máxima de 11 minutos, pero  
  para otros nuevos tipos, es necesario (ver Meta LS y Registro de Servicio más abajo).

- Las claves fuera de línea son opcionales, para reducir la complejidad inicial/obligatoria de implementación.


### Problemas

- Podría reducirse aún más la precisión de la marca de tiempo (¿10 minutos?) pero habría que añadir  
  un número de versión. Esto podría romper el multihoming, a menos que tengamos encriptación que preserve el orden?  
  Probablemente no se pueda hacer sin marcas de tiempo.

- Alternativa: marca de tiempo de 3 bytes (época / 10 minutos), versión de 1 byte, expiración de 2 bytes

- ¿Es el tipo explícito o implícito en los datos / firma? ¿Constantes de "dominio" para la firma?


### Notas

- Los routers no deberían publicar un LS más de una vez por segundo.  
  Si lo hacen, deben incrementar artificialmente la marca de tiempo publicada en 1  
  sobre el LS publicado anteriormente.

- Las implementaciones de routers podrían almacenar en caché las claves y firma transitorias para  
  evitar la verificación cada vez. En particular, los floodfills y los routers en  
  ambos extremos de conexiones de larga duración podrían beneficiarse de esto.

- Las claves y firma fuera de línea solo son apropiadas para destinos de larga duración,  
  es decir, servidores, no clientes.



## Nuevos tipos DatabaseEntry


### LeaseSet 2

Cambios respecto al LeaseSet existente:

- Añadir marca de tiempo de publicación, marca de tiempo de expiración, flags y propiedades
- Añadir tipo de encriptación
- Eliminar clave de revocación

Buscar con  
    Bandera LS estándar (1)  
Almacenar con  
    Tipo LS2 estándar (3)  
Almacenar en  
    Hash del destino  
    Este hash se usa luego para generar la "clave de enrutamiento" diaria, como en LS1  
Expiración típica  
    10 minutos, como en un LS regular.  
Publicado por  
    Destino

### Formato

```
Encabezado LS2 Estándar como se especificó anteriormente

  Parte Específica del Tipo LS2 Estándar
  - Propiedades (Mapeo según se especifica en la especificación de estructuras comunes, 2 bytes cero si no hay)
  - Número de secciones de clave que siguen (1 byte, máximo TBD)
  - Secciones de clave:
    - Tipo de encriptación (2 bytes, big endian)
    - Longitud de clave de encriptación (2 bytes, big endian)
      Esto es explícito, para que los floodfills puedan analizar LS2 con tipos de encriptación desconocidos.
    - Clave de encriptación (número de bytes especificado)
  - Número de lease2s (1 byte)
  - Lease2s (40 bytes cada uno)
    Estas son leases, pero con una expiración de 4 bytes en lugar de 8 bytes,
    segundos desde la época (se reinicia en 2106)

  Firma LS2 Estándar:
  - Firma
    Si la bandera indica claves fuera de línea, esto está firmado por la clave pública transitoria,
    de lo contrario, por la clave pública del destino
    Longitud según el tipo de firma de la clave de firma
    La firma es de todo lo anterior.
```


### Justificación

- Propiedades: Expansión futura y flexibilidad.  
  Colocadas primero por si son necesarias para el análisis de los datos restantes.

- Múltiples pares tipo de encriptación/clave pública son  
  para facilitar la transición a nuevos tipos de encriptación. La otra forma de hacerlo  
  es publicar múltiples leasesets, posiblemente usando los mismos túneles,  
  como hacemos ahora para destinos DSA y EdDSA.  
  La identificación del tipo de encriptación entrante en un túnel  
  puede hacerse con el mecanismo existente de etiqueta de sesión,  
  y/o descifrado de prueba usando cada clave. Las longitudes de los mensajes  
  entrantes también pueden proporcionar una pista.

### Discusión

Esta propuesta continúa usando la clave pública en el leaseset para la  
clave de encriptación extremo a extremo, y deja el campo de clave pública en el  
Destino sin usar, como está ahora. El tipo de encriptación no se especifica  
en el certificado de clave del Destino, seguirá siendo 0.

Una alternativa rechazada es especificar el tipo de encriptación en el certificado de clave del Destino,  
usar la clave pública en el Destino, y no usar la clave pública  
en el leaseset. No tenemos previsto hacer esto.

Beneficios de LS2:

- La ubicación de la clave pública real no cambia.
- El tipo de encriptación o la clave pública pueden cambiar sin cambiar el Destino.
- Elimina el campo de revocación no utilizado
- Compatibilidad básica con otros tipos DatabaseEntry en esta propuesta
- Permite múltiples tipos de encriptación

Desventajas de LS2:

- La ubicación de la clave pública y el tipo de encriptación difiere de RouterInfo
- Mantiene la clave pública no utilizada en el leaseset
- Requiere implementación en toda la red; en la alternativa, tipos de encriptación experimentales pueden usarse, si los permiten los floodfills  
  (pero ver propuestas relacionadas 136 y 137 sobre soporte para tipos de firma experimentales).  
  La propuesta alternativa podría ser más fácil de implementar y probar para tipos de encriptación experimentales.


### Nuevos Problemas de Encriptación

Algunas partes están fuera del alcance de esta propuesta,  
pero ponemos notas aquí por ahora ya que no tenemos  
una propuesta de encriptación separada todavía.  
Ver también las propuestas ECIES 144 y 145.

- El tipo de encriptación representa la combinación  
  de curva, longitud de clave y esquema extremo a extremo,  
  incluyendo KDF y MAC, si los hay.

- Hemos incluido un campo de longitud de clave, para que el LS2 sea  
  analizable y verificable por el floodfill incluso para tipos de encriptación desconocidos.

- El primer nuevo tipo de encriptación que se propondrá será  
  probablemente ECIES/X25519. Cómo se usa extremo a extremo  
  (ya sea una versión ligeramente modificada de ElGamal/AES+SessionTag  
  o algo completamente nuevo, por ejemplo ChaCha/Poly) se especificará  
  en una o más propuestas separadas.  
  Ver también las propuestas ECIES 144 y 145.


### Notas

- La expiración de 8 bytes en leases cambia a 4 bytes.

- Si alguna vez implementamos revocación, podemos hacerlo con un campo de expiración de cero,  
  o leases de cero, o ambos. No necesitamos una clave de revocación separada.

- Las claves de encriptación están en orden de preferencia del servidor, la más preferida primero.  
  El comportamiento predeterminado del cliente es seleccionar la primera clave con  
  un tipo de encriptación soportado. Los clientes pueden usar otros algoritmos de selección  
  basados en soporte de encriptación, rendimiento relativo y otros factores.


### LS2 Cifrado

Objetivos:

- Añadir ofuscación
- Permitir múltiples tipos de firma
- No requerir nuevas primitivas criptográficas
- Opcionalmente cifrar a cada destinatario, revocable
- Soportar cifrado solo de LS2 Estándar y Meta LS2

LS2 Cifrado nunca se envía en un mensaje garlic extremo a extremo.  
Usa el LS2 Estándar como arriba.


Cambios respecto al LeaseSet cifrado existente:

- Cifrar todo por seguridad
- Cifrar de forma segura, no solo con AES.
- Cifrar a cada destinatario

Buscar con  
    Bandera LS estándar (1)  
Almacenar con  
    Tipo LS2 Cifrado (5)  
Almacenar en  
    Hash del tipo de firma ofuscada y clave pública ofuscada  
    Tipo de firma de 2 bytes (big endian, por ejemplo 0x000b) || clave pública ofuscada  
    Este hash se usa luego para generar la "clave de enrutamiento" diaria, como en LS1  
Expiración típica  
    10 minutos, como en un LS regular, o horas, como en un meta LS.  
Publicado por  
    Destino


### Definiciones

Definimos las siguientes funciones correspondientes a los bloques criptográficos usados  
para LS2 Cifrado:

CSRNG(n)  
    salida de n bytes de un generador de números aleatorios criptográficamente seguro.

    Además del requisito de que CSRNG sea criptográficamente seguro (y por tanto  
    adecuado para generar material de clave), DEBE ser seguro  
    que alguna salida de n bytes se use como material de clave cuando las secuencias de bytes inmediatamente  
    anteriores y posteriores estén expuestas en la red (como en una sal, o relleno cifrado). Las implementaciones que dependan de una fuente potencialmente no confiable deben hashear  
    cualquier salida que se expondrá en la red. Ver [referencias PRNG](http://projectbullrun.org/dual-ec/ext-rand.html) y [discusión en tor-dev](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html).

H(p, d)  
    función hash SHA-256 que toma una cadena de personalización p y datos d, y  
    produce una salida de longitud 32 bytes.

    Usa SHA-256 de la siguiente manera::

        H(p, d) := SHA-256(p || d)

STREAM  
    el cifrado de flujo ChaCha20 según se especifica en [RFC 7539 Sección 2.4](https://tools.ietf.org/html/rfc7539#section-2.4), con el contador inicial  
    establecido en 1. S_KEY_LEN = 32 y S_IV_LEN = 12.

    ENCRYPT(k, iv, plaintext)  
        Cifra el texto plano usando la clave de cifrado k, y el nonce iv que DEBE ser único para  
        la clave k. Devuelve un texto cifrado del mismo tamaño que el texto plano.

        Todo el texto cifrado debe ser indistinguible de aleatorio si la clave es secreta.

    DECRYPT(k, iv, ciphertext)  
        Descifra el texto cifrado usando la clave de cifrado k, y el nonce iv. Devuelve el texto plano.


SIG  
    el esquema de firma RedDSA (correspondiente al SigType 11) con ofuscación de clave.  
    Tiene las siguientes funciones:

    DERIVE_PUBLIC(privkey)  
        Devuelve la clave pública correspondiente a la clave privada dada.

    SIGN(privkey, m)  
        Devuelve una firma por la clave privada privkey sobre el mensaje dado m.

    VERIFY(pubkey, m, sig)  
        Verifica la firma sig contra la clave pública pubkey y el mensaje m. Devuelve  
        verdadero si la firma es válida, falso en caso contrario.

    También debe soportar las siguientes operaciones de ofuscación de clave:

    GENERATE_ALPHA(data, secret)  
        Genera alpha para quienes conocen los datos y un secreto opcional.  
        El resultado debe tener distribución idéntica a las claves privadas.

    BLIND_PRIVKEY(privkey, alpha)  
        Ofusca una clave privada, usando un alpha secreto.

    BLIND_PUBKEY(pubkey, alpha)  
        Ofusca una clave pública, usando un alpha secreto.  
        Para un par de claves (privkey, pubkey) se cumple la siguiente relación::

            BLIND_PUBKEY(pubkey, alpha) ==
            DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))

DH  
    sistema de acuerdo de clave pública X25519. Claves privadas de 32 bytes, claves públicas de 32  
    bytes, produce salidas de 32 bytes. Tiene las siguientes  
    funciones:

    GENERATE_PRIVATE()  
        Genera una nueva clave privada.

    DERIVE_PUBLIC(privkey)  
        Devuelve la clave pública correspondiente a la clave privada dada.

    DH(privkey, pubkey)  
        Genera un secreto compartido a partir de las claves privada y pública dadas.

HKDF(salt, ikm, info, n)  
    una función criptográfica de derivación de clave que toma material de clave de entrada ikm (que  
    debería tener buena entropía pero no se requiere que sea una cadena uniformemente aleatoria), una sal  
    de longitud 32 bytes, y un valor 'info' específico del contexto, y produce una salida  
    de n bytes adecuada para usar como material de clave.

    Usa HKDF según se especifica en [RFC 5869](https://tools.ietf.org/html/rfc5869), usando la función hash HMAC SHA-256  
    según se especifica en [RFC 2104](https://tools.ietf.org/html/rfc2104). Esto significa que SALT_LEN es 32 bytes como máximo.


### Formato

El formato de LS2 cifrado consta de tres capas anidadas:

- Una capa externa que contiene la información en texto claro necesaria para almacenamiento y recuperación.
- Una capa intermedia que maneja la autenticación del cliente.
- Una capa interna que contiene los datos reales de LS2.

El formato general es::

    Datos capa 0 + Enc(datos capa 1 + Enc(datos capa 2)) + Firma

Nota que LS2 cifrado está ofuscado. El Destino no está en el encabezado.  
La ubicación de almacenamiento DHT es SHA-256(tipo de firma || clave pública ofuscada), y se rota diariamente.

NO usa el encabezado LS2 estándar especificado anteriormente.

#### Capa 0 (externa)
Tipo  
    1 byte

    No está realmente en el encabezado, pero forma parte de los datos cubiertos por la firma.  
    Tómese del campo en el mensaje de Almacenamiento en la Base de Datos.

Tipo de Firma de Clave Pública Ofuscada  
    2 bytes, big endian  
    Esto siempre será tipo 11, identificando una clave Red25519 ofuscada.

Clave Pública Ofuscada  
    Longitud según el tipo de firma

Marca de tiempo de publicación  
    4 bytes, big endian

    Segundos desde la época, se reinicia en 2106

Expira  
    2 bytes, big endian

    Desplazamiento desde la marca de tiempo de publicación en segundos, máximo 18.2 horas

Flags  
    2 bytes

    Orden de bits: 15 14 ... 3 2 1 0

    Bit 0: Si 0, sin claves fuera de línea; si 1, claves fuera de línea

    Otros bits: establecidos en 0 para compatibilidad con usos futuros

Datos de clave transitoria  
    Presente si la bandera indica claves fuera de línea

    Marca de tiempo de expiración  
        4 bytes, big endian

        Segundos desde la época, se reinicia en 2106

    Tipo de firma transitoria  
        2 bytes, big endian

    Clave pública de firma transitoria  
        Longitud según el tipo de firma

    Firma  
        Longitud según el tipo de firma de la clave pública ofuscada

        Sobre la marca de tiempo de expiración, tipo de firma transitoria y clave pública transitoria.

        Verificada con la clave pública ofuscada.

lenOuterCiphertext  
    2 bytes, big endian

outerCiphertext  
    lenOuterCiphertext bytes

    Datos de capa 1 cifrados. Ver más abajo para algoritmos de derivación de clave y cifrado.

Firma  
    Longitud según el tipo de firma de la clave de firma usada

    La firma es de todo lo anterior.

    Si la bandera indica claves fuera de línea, la firma se verifica con la clave pública transitoria.  
    De lo contrario, la firma se verifica con la clave pública ofuscada.


#### Capa 1 (intermedia)
Flags  
    1 byte
    
    Orden de bits: 76543210

    Bit 0: 0 para todos, 1 para por cliente, sección de autenticación a continuación

    Bits 3-1: Esquema de autenticación, solo si el bit 0 está establecido en 1 para por cliente, de lo contrario 000  
              000: Autenticación de cliente DH (o sin autenticación por cliente)  
              001: Autenticación de cliente PSK

    Bits 7-4: No usados, establecidos en 0 para compatibilidad futura

Datos de autenticación de cliente DH  
    Presente si el bit 0 de la bandera está establecido en 1 y los bits 3-1 están establecidos en 000.

    clavePúblicaEfímera  
        32 bytes

    clientes  
        2 bytes, big endian

        Número de entradas authClient que siguen, 40 bytes cada una

    authClient  
        Datos de autorización para un solo cliente.  
        Ver más abajo para el algoritmo de autorización por cliente.

        clientID_i  
            8 bytes

        clientCookie_i  
            32 bytes

Datos de autenticación de cliente PSK  
    Presente si el bit 0 de la bandera está establecido en 1 y los bits 3-1 están establecidos en 001.

    authSalt  
        32 bytes

    clientes  
        2 bytes, big endian

        Número de entradas authClient que siguen, 40 bytes cada una

    authClient  
        Datos de autorización para un solo cliente.  
        Ver más abajo para el algoritmo de autorización por cliente.

        clientID_i  
            8 bytes

        clientCookie_i  
            32 bytes


innerCiphertext  
    Longitud implícita por lenOuterCiphertext (lo que quede de datos)

    Datos de capa 2 cifrados. Ver más abajo para algoritmos de derivación de clave y cifrado.


#### Capa 2 (interna)
Tipo  
    1 byte

    Ya sea 3 (LS2) o 7 (Meta LS2)

Datos  
    Datos LeaseSet2 para el tipo dado.

    Incluye el encabezado y la firma.


### Derivación de Clave Ofuscada

Usamos el siguiente esquema para ofuscar claves,  
basado en Ed25519 y [ZCash RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf).  
Las firmas Re25519 son sobre la curva Ed25519, usando SHA-512 para el hash.

No usamos [Tor's rend-spec-v3.txt appendix A.2](https://spec.torproject.org/rend-spec-v3),  
que tiene objetivos de diseño similares, porque sus claves públicas ofuscadas  
pueden estar fuera del subgrupo de orden primo, con implicaciones de seguridad desconocidas.


#### Objetivos

- La clave pública de firma en el destino sin ofuscar debe ser  
  Ed25519 (tipo de firma 7) o Red25519 (tipo de firma 11);  
  no se admiten otros tipos de firma
- Si la clave pública de firma está fuera de línea, la clave pública de firma transitoria también debe ser Ed25519
- La ofuscación es computacionalmente simple
- Usar primitivas criptográficas existentes
- Las claves públicas ofuscadas no pueden desofuscarse
- Las claves públicas ofuscadas deben estar en la curva Ed25519 y en el subgrupo de orden primo
- Debe conocerse la clave pública de firma del destino  
  (no se requiere el destino completo) para derivar la clave pública ofuscada
- Opcionalmente proporcionar un secreto adicional requerido para derivar la clave pública ofuscada


#### Seguridad

La seguridad de un esquema de ofuscación requiere que la  
distribución de alpha sea la misma que las claves privadas sin ofuscar.  
Sin embargo, cuando ofuscamos una clave privada Ed25519 (tipo de firma 7)  
a una clave privada Red25519 (tipo de firma 11), la distribución es diferente.  
Para cumplir con los requisitos de [zcash sección 4.1.6.1](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf),  
se debería usar Red25519 (tipo de firma 11) también para las claves sin ofuscar, para que  
"la combinación de una clave pública realeatorizada y firma(s)  
bajo esa clave no revele la clave de la cual fue realeatorizada".  
Permitimos el tipo 7 para destinos existentes, pero recomendamos  
el tipo 11 para nuevos destinos que serán cifrados.



#### Definiciones

B  
    El punto base Ed25519 (generador) 2^255 - 19 como en [Ed25519](http://cr.yp.to/papers.html#ed25519)

L  
    El orden Ed25519 2^252 + 27742317777372353535851937790883648493  
    como en [Ed25519](http://cr.yp.to/papers.html#ed25519)

DERIVE_PUBLIC(a)  
    Convierte una clave privada a pública, como en Ed25519 (multiplicar por G)

alpha  
    Un número aleatorio de 32 bytes conocido por quienes conocen el destino.

GENERATE_ALPHA(destination, date, secret)  
    Genera alpha para la fecha actual, para quienes conocen el destino y el secreto.  
    El resultado debe tener distribución idéntica a claves privadas Ed25519.

a  
    La clave privada de firma EdDSA o RedDSA de 32 bytes sin ofuscar usada para firmar el destino

A  
    La clave pública de firma EdDSA o RedDSA de 32 bytes sin ofuscar en el destino,  
    = DERIVE_PUBLIC(a), como en Ed25519

a'  
    La clave privada de firma EdDSA ofuscada de 32 bytes usada para firmar el leaseset cifrado  
    Esta es una clave privada EdDSA válida.

A'  
    La clave pública de firma EdDSA ofuscada de 32 bytes en el Destino,  
    puede generarse con DERIVE_PUBLIC(a'), o desde A y alpha.  
    Esta es una clave pública EdDSA válida, en la curva y en el subgrupo de orden primo.

LEOS2IP(x)  
    Invierte el orden de los bytes de entrada a little-endian

H*(x)  
    32 bytes = (LEOS2IP(SHA512(x))) mod B, igual que en Ed25519 hash-and-reduce


#### Cálculos de Ofuscación

Una nueva clave secreta alpha y claves ofuscadas deben generarse cada día (UTC).  
La clave secreta alpha y las claves ofuscadas se calculan como sigue.

GENERATE_ALPHA(destination, date, secret), para todas las partes:

```text
// GENERATE_ALPHA(destination, date, secret)

  // secreto es opcional, si no, longitud cero
  A = clave pública de firma del destino
  stA = tipo de firma de A, 2 bytes big endian (0x0007 o 0x000b)
  stA' = tipo de firma de la clave pública ofuscada A', 2 bytes big endian (0x000b)
  keydata = A || stA || stA'
  datestring = 8 bytes ASCII YYYYMMDD de la fecha actual UTC
  secreto = cadena codificada UTF-8
  seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secreto, "i2pblinding1", 64)
  // tratar seed como un valor little-endian de 64 bytes
  alpha = seed mod L
```

BLIND_PRIVKEY(), para el propietario que publica el leaseset:

```text
// BLIND_PRIVKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  // Si para una clave privada Ed25519 (tipo 7)
  seed = clave privada de firma del destino
  a = mitad izquierda de SHA512(seed) y ajustada como es habitual para Ed25519
  // de lo contrario, para una clave privada Red25519 (tipo 11)
  a = clave privada de firma del destino
  // Adición usando aritmética escalar
  clave privada de firma ofuscada = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
  clave pública de firma ofuscada = A' = DERIVE_PUBLIC(a')
```

BLIND_PUBKEY(), para los clientes que recuperan el leaseset:

```text
// BLIND_PUBKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  A = clave pública de firma del destino
  // Adición usando elementos de grupo (puntos en la curva)
  clave pública ofuscada = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```

Ambos métodos de cálculo de A' producen el mismo resultado, como se requiere.



#### Firmado

El leaseset sin ofuscar está firmado por la clave privada de firma Ed25519 o Red25519 sin ofuscar  
y verificado con la clave pública de firma Ed25519 o Red25519 sin ofuscar (tipos de firma 7 u 11) como de costumbre.

Si la clave pública de firma está fuera de línea,  
el leaseset sin ofuscar está firmado por la clave privada de firma transitoria Ed25519 o Red25519 sin ofuscar  
y verificado con la clave pública de firma transitoria Ed25519 o Red25519 sin ofuscar (tipos de firma 7 u 11) como de costumbre.  
Ver más abajo para notas adicionales sobre claves fuera de línea para leasesets cifrados.

Para la firma del leaseset cifrado, usamos Red25519, basado en [RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)  
para firmar y verificar con claves ofuscadas.  
Las firmas Red25519 son sobre la curva Ed25519, usando SHA-512 para el hash.

Red25519 es idéntico a Ed25519 estándar excepto como se especifica a continuación.


#### Cálculos de Firma/Verificación

La parte externa del leaseset cifrado usa claves y firmas Red25519.

Red25519 es casi idéntico a Ed25519. Hay dos diferencias:

Las claves privadas Red25519 se generan a partir de números aleatorios y luego deben reducirse mod L, donde L se define arriba.  
Las claves privadas Ed25519 se generan a partir de números aleatorios y luego "ajustan" usando  
enmascaramiento bit a bit a los bytes 0 y 31. Esto no se hace para Red25519.  
Las funciones GENERATE_ALPHA() y BLIND_PRIVKEY() definidas arriba generan claves privadas Red25519 adecuadas usando mod L.

En Red25519, el cálculo de r para la firma usa datos aleatorios adicionales,  
y usa el valor de la clave pública en lugar del hash de la clave privada.  
Debido a los datos aleatorios, cada firma Red25519 es diferente, incluso  
al firmar los mismos datos con la misma clave.

Firmado:

```text
T = 80 bytes aleatorios
  r = H*(T || clave pública || mensaje)
  // el resto es igual que en Ed25519
```

Verificación:

```text
// igual que en Ed25519
```



### Encriptación y procesamiento

#### Derivación de subcredenciales
Como parte del proceso de ofuscación, necesitamos asegurar que un LS2 cifrado solo pueda ser  
descifrado por alguien que conozca la clave pública de firma del Destino correspondiente.  
No se requiere el Destino completo.  
Para lograr esto, derivamos una credencial de la clave pública de firma:

```text
A = clave pública de firma del destino
  stA = tipo de firma de A, 2 bytes big endian (0x0007 o 0x000b)
  stA' = tipo de firma de A', 2 bytes big endian (0x000b)
  keydata = A || stA || stA'
  credencial = H("credential", keydata)
```

La cadena de personalización asegura que la credencial no colisione con ningún hash usado  
como clave de búsqueda DHT, como el hash simple del Destino.

Para una clave ofuscada dada, podemos derivar una subcredencial:

```text
subcredencial = H("subcredential", credencial || clavePúblicaOfuscada)
```

La subcredencial se incluye en los procesos de derivación de clave más abajo, lo que enlaza esas  
claves al conocimiento de la clave pública de firma del Destino.

#### Encriptación de capa 1
Primero, se prepara la entrada para el proceso de derivación de clave:

```text
entradaExterna = subcredencial || marcaTiempoPublicación
```

Luego, se genera una sal aleatoria:

```text
salExterna = CSRNG(32)
```

Luego, se deriva la clave usada para cifrar la capa 1:

```text
claves = HKDF(salExterna, entradaExterna, "ELS2_L1K", 44)
  claveExterna = claves[0:31]
  ivExterno = claves[32:43]
```

Finalmente, se cifra y serializa el texto plano de la capa 1:

```text
textoCifradoExterno = salExterna || ENCRYPT(claveExterna, ivExterno, textoPlanoExterno)
```

#### Descifrado de capa 1
La sal se analiza desde el texto cifrado de la capa 1:

```text
salExterna = textoCifradoExterno[0:31]
```

Luego, se deriva la clave usada para cifrar la capa 1:

```text
entradaExterna = subcredencial || marcaTiempoPublicación
  claves = HKDF(salExterna, entradaExterna, "ELS2_L1K", 44)
  claveExterna = claves[0:31]
  ivExterno = claves[32:43]
```

Finalmente, se descifra el texto cifrado de la capa 1:

```text
textoPlanoExterno = DECRYPT(claveExterna, ivExterno, textoCifradoExterno[32:fin])
```

#### Encriptación de capa 2
Cuando la autorización de cliente está habilitada, se calcula ``authCookie`` como se describe más abajo.  
Cuando la autorización de cliente está deshabilitada, ``authCookie`` es el array de bytes de longitud cero.

El cifrado procede de forma similar a la capa 1:

```text
entradaInterna = authCookie || subcredencial || marcaTiempoPublicación
  salInterna = CSRNG(32)
  claves = HKDF(salInterna, entradaInterna, "ELS2_L2K", 44)
  claveInterna = claves[0:31]
  ivInterno = claves[32:43]
  textoCifradoInterno = salInterna || ENCRYPT(claveInterna, ivInterno, textoPlanoInterno)
```

#### Descifrado de capa 2
Cuando la autorización de cliente está habilitada, se calcula ``authCookie`` como se describe más abajo.  
Cuando la autorización de cliente está deshabilitada, ``authCookie`` es el array de bytes de longitud cero.

El descifrado procede de forma similar a la capa 1:

```text
entradaInterna = authCookie || subcredencial || marcaTiempoPublicación
  salInterna = textoCifradoInterno[0:31]
  claves = HKDF(salInterna, entradaInterna, "ELS2_L2K", 44)
  claveInterna = claves[0:31]
  ivInterno = claves[32:43]
  textoPlanoInterno = DECRYPT(claveInterna, ivInterno, textoCifradoInterno[32:fin])
```


### Autorización por cliente

Cuando la autorización de cliente está habilitada para un Destino, el servidor mantiene una lista de  
clientes a los que autoriza para descifrar los datos del LS2 cifrado. Los datos almacenados por cliente  
dependen del mecanismo de autorización, e incluyen alguna forma de material de clave que cada  
cliente genera y envía al servidor mediante un mecanismo seguro fuera de banda.

Hay dos alternativas para implementar la autorización por cliente:

#### Autorización de cliente DH
Cada cliente genera un par de claves DH ``[csk_i, cpk_i]``, y envía la clave pública ``cpk_i``  
al servidor.

Procesamiento del servidor  
^^^^^^^^^^^^^^^^^
El servidor genera un nuevo ``authCookie`` y un par de claves DH efímero:

```text
authCookie = CSRNG(32)
  esk = GENERATE_PRIVATE()
  epk = DERIVE_PUBLIC(esk)
```

Luego, para cada cliente autorizado, el servidor cifra ``authCookie`` con su clave pública:

```text
secretoCompartido = DH(esk, cpk_i)
  entradaAuth = secretoCompartido || cpk_i || subcredencial || marcaTiempoPublicación
  okm = HKDF(epk, entradaAuth, "ELS2_XCA", 52)
  claveCliente_i = okm[0:31]
  ivCliente_i = okm[32:43]
  idCliente_i = okm[44:51]
  cookieCliente_i = ENCRYPT(claveCliente_i, ivCliente_i, authCookie)
```

El servidor coloca cada tupla ``[idCliente_i, cookieCliente_i]`` en la capa 1 del  
LS2 cifrado, junto con ``epk``.

Procesamiento del cliente  
^^^^^^^^^^^^^^^^^
El cliente usa su clave privada para derivar su identificador de cliente esperado ``idCliente_i``,  
clave de cifrado ``claveCliente_i``, y IV de cifrado ``ivCliente_i``:

```text
secretoCompartido = DH(csk_i, epk)
  entradaAuth = secretoCompartido || cpk_i || subcredencial || marcaTiempoPublicación
  okm = HKDF(epk, entradaAuth, "ELS2_XCA", 52)
  claveCliente_i = okm[0:31]
  ivCliente_i = okm[32:43]
  idCliente_i = okm[44:51]
```

Luego, el cliente busca en los datos de autorización de la capa 1 una entrada que contenga  
``idCliente_i``. Si existe una entrada coincidente, el cliente la descifra para obtener  
``authCookie``:

```text
authCookie = DECRYPT(claveCliente_i, ivCliente_i, cookieCliente_i)
```

#### Autorización de cliente con clave precompartida
Cada cliente genera una clave secreta de 32 bytes ``psk_i``, y la envía al servidor.  
Alternativamente, el servidor puede generar la clave secreta, y enviársela a uno o más clientes.


Procesamiento del servidor  
^^^^^^^^^^^^^^^^^
El servidor genera un nuevo ``authCookie`` y una sal:

```text
authCookie = CSRNG(32)
  authSalt = CSRNG(32)
```

Luego, para cada cliente autorizado, el servidor cifra ``authCookie`` con su clave precompartida:

```text
entradaAuth = psk_i || subcredencial || marcaTiempoPublicación
  okm = HKDF(authSalt, entradaAuth, "ELS2PSKA", 52)
  claveCliente_i = okm[0:31]
  ivCliente_i = okm[32:43]
  idCliente_i = okm[44:51]
  cookieCliente_i = ENCRYPT(claveCliente_i, ivCliente_i, authCookie)
```

El servidor coloca cada tupla ``[idCliente_i, cookieCliente_i]`` en la capa 1 del  
LS2 cifrado, junto con ``authSalt``.

Procesamiento del cliente  
^^^^^^^^^^^^^^^^^
El cliente usa su clave precompartida para derivar su identificador de cliente esperado ``idCliente_i``,  
clave de cifrado ``claveCliente_i``, y IV de cifrado ``ivCliente_i``:

```text
entradaAuth = psk_i || subcredencial || marcaTiempoPublicación
  okm = HKDF(authSalt, entradaAuth, "ELS2PSKA", 52)
  claveCliente_i = okm[0:31]
  ivCliente_i = okm[32:43]
  idCliente_i = okm[44:51]
```

Luego, el cliente busca en los datos de autorización de la capa 1 una entrada que contenga  
``idCliente_i``. Si existe una entrada coincidente, el cliente la descifra para obtener  
``authCookie``:

```text
authCookie = DECRYPT(claveCliente_i, ivCliente_i, cookieCliente_i)
```

#### Consideraciones de seguridad
Ambos mecanismos de autorización de cliente anteriores proporcionan privacidad para la membresía de clientes.  
Una entidad que solo conozca el Destino puede ver cuántos clientes están suscritos en cualquier  
momento, pero no puede rastrear qué clientes se están añadiendo o revocando.

Los servidores DEBERÍAN aleatorizar el orden de los clientes cada vez que generen un LS2 cifrado, para  
evitar que los clientes aprendan su posición en la lista e infieran cuándo se han añadido o revocado otros clientes.

Un servidor PUEDE optar por ocultar el número de clientes suscritos insertando entradas aleatorias  
en la lista de datos de autorización.

Ventajas de la autorización de cliente DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- La seguridad del esquema no depende únicamente del intercambio fuera de banda del material de clave del cliente.  
  La clave privada del cliente nunca necesita salir de su dispositivo, y por tanto un  
  adversario que pueda interceptar el intercambio fuera de banda, pero no pueda romper el algoritmo DH,  
  no puede descifrar el LS2 cifrado, ni determinar cuánto tiempo se le da acceso al cliente.

Desventajas de la autorización de cliente DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Requiere N + 1 operaciones DH en el lado del servidor para N clientes.
- Requiere una operación DH en el lado del cliente.
- Requiere que el cliente genere la clave secreta.

Ventajas de la autorización de cliente PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- No requiere operaciones DH.
- Permite que el servidor genere la clave secreta.
- Permite que el servidor comparta la misma clave con múltiples clientes, si se desea.

Desventajas de la autorización de cliente PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- La seguridad del esquema depende críticamente del intercambio fuera de banda del material de clave del cliente.  
  Un adversario que intercepte el intercambio para un cliente particular puede descifrar  
  cualquier LS2 cifrado posterior para el cual ese cliente esté autorizado, así como determinar  
  cuándo se revoca el acceso del cliente.


### LS Cifrado con Direcciones Base 32

Ver propuesta 149.

No puedes usar un LS2 cifrado para bittorrent, debido a las respuestas compactas de anuncio que son de 32 bytes.  
Los 32 bytes contienen solo el hash. No hay espacio para indicar que el  
leaseset está cifrado, o los tipos de firma.



### LS Cifrado con Claves Fuera de Línea

Para leasesets cifrados con claves fuera de línea, las claves privadas ofuscadas también deben generarse fuera de línea,  
una por cada día.

Como el bloque opcional de firma fuera de línea está en la parte en texto claro del leaseset cifrado,  
cualquiera que rastree los floodfills podría usar esto para rastrear el leaseset (pero no descifrarlo)  
durante varios días.  
Para evitar esto, el propietario de las claves debería generar nuevas claves transitorias  
para cada día también.  
Tanto las claves transitorias como las ofuscadas pueden generarse por adelantado, y entregarse al router  
por lotes.

No se define en esta propuesta un formato de archivo para empaquetar múltiples claves transitorias y  
ofuscadas y proporcionarlas al cliente o router.  
No se define en esta propuesta una mejora del protocolo I2CP para soportar  
leasesets cifrados con claves fuera de línea.



### Notas

- Un servicio que use leasesets cifrados publicaría la versión cifrada a los  
  floodfills. Sin embargo, por eficiencia, enviaría leasesets sin cifrar a  
  clientes en el mensaje garlic envuelto, una vez autenticado (por ejemplo, mediante lista blanca).

- Los floodfills pueden limitar el tamaño máximo a un valor razonable para prevenir abusos.

- Después del descifrado, se deben hacer varias comprobaciones, incluyendo que  
  la marca de tiempo interna y la expiración coincidan con las del nivel superior.

- ChaCha20 fue seleccionado sobre AES. Aunque las velocidades son similares si  
  el soporte de hardware AES está disponible, ChaCha20 es 2.5-3 veces más rápido cuando  
  el soporte de hardware AES no está disponible, como en dispositivos ARM de gama baja.

- No nos importa lo suficiente la velocidad como para usar BLAKE2b con clave. Tiene un tamaño de salida  
  lo suficientemente grande para acomodar el mayor n que requerimos (o podemos llamarlo una vez por  
  clave deseada con un argumento contador). BLAKE2b es mucho más rápido que SHA-256, y  
  BLAKE2b con clave reduciría el número total de llamadas a funciones hash.  
  Sin embargo, ver propuesta 148, donde se propone que cambiemos a BLAKE2b por otras razones.  
  Ver [rendimiento de derivación segura de claves](https://www.lvh.io/posts/secure-key-derivation-performance.html).


### Meta LS2

Se usa para reemplazar el multihoming. Como cualquier leaseset, está firmado por el  
creador. Es una lista autenticada de hashes de destino.

Meta LS2 es la parte superior, y posiblemente nodos intermedios,  
de una estructura de árbol.  
Contiene un número de entradas, cada una apuntando a un LS, LS2 o otro Meta LS2  
para soportar multihoming masivo.  
Un Meta LS2 puede contener una mezcla de entradas LS, LS2 y Meta LS2.  
Las hojas del árbol siempre son un LS o LS2.  
El árbol es un DAG; se prohíben bucles; los clientes que hacen búsquedas deben detectar y  
rechazar seguir bucles.

Un Meta LS2 puede tener una expiración mucho más larga que un LS o LS2 estándar.  
El nivel superior puede tener una expiración varias horas después de la fecha de publicación.  
El tiempo máximo de expiración será aplicado por floodfills y clientes, y está por determinar.

El caso de uso para Meta LS2 es multihoming masivo, pero sin más  
protección para la correlación de routers con leasesets (en el reinicio del router) que  
la proporcionada actualmente con LS o LS2.  
Esto es equivalente al caso de uso de "facebook", que probablemente no necesita  
protección contra correlación. Este caso de uso probablemente necesita claves fuera de línea,  
que se proporcionan en el encabezado estándar en cada nodo del árbol.

El protocolo de back-end para coordinación entre los routers hoja, firmantes intermedios y maestros de Meta LS  
no se especifica aquí. Los requisitos son extremadamente simples: solo verificar que el par está activo,  
y publicar un nuevo LS cada pocas horas. La única complejidad es para elegir nuevos  
publicadores para los Meta LS de nivel superior o intermedio en caso de fallo.

Leasesets mixtos donde leases de múltiples routers se combinan, firman y publican  
en un solo leaseset se documentan en la propuesta 140, "multihoming invisible".  
Esta propuesta es inviable tal como está escrita, porque las conexiones de streaming no serían  
"pegajosas" a un solo router, ver http://zzz.i2p/topics/2335 .

El protocolo de back-end, y la interacción con los componentes internos del router y cliente, sería  
bastante complejo para el multihoming invisible.

Para evitar sobrecargar el floodfill para el Meta LS de nivel superior, la expiración debería  
ser de varias horas como mínimo. Los clientes deben almacenar en caché el Meta LS de nivel superior, y  
persistirlo entre reinicios si no ha expirado.

Necesitamos definir algún algoritmo para que los clientes recorran el árbol, incluyendo alternativas,  
para que el uso se disperse. Alguna función de distancia de hash, costo y aleatoriedad.  
Si un nodo tiene tanto LS o LS2 como Meta LS, necesitamos saber cuándo está permitido  
usar esos leasesets, y cuándo seguir recorriendo el árbol.




Buscar con  
    Bandera LS estándar (1)  
Almacenar con  
    Tipo Meta LS2 (7)  
Almacenar en  
    Hash del destino  
    Este hash se usa luego para generar la "clave de enrutamiento" diaria, como en LS1  
Expiración típica  
    Horas. Máximo 18.2 horas (65535 segundos)  
Publicado por  
    Destino "maestro" o coordinador, o coordinadores intermedios

### Formato

```
Encabezado LS2 Estándar como se especificó anteriormente

  Parte Específica del Tipo Meta LS2
  - Propiedades (Mapeo según se especifica en la especificación de estructuras comunes, 2 bytes cero si no hay)
  - Número de entradas (1 byte) Máximo TBD
  - Entradas. Cada entrada contiene: (40 bytes)
    - Hash (32 bytes)
    - Flags (2 bytes)
      TBD. Establecer todos a cero para compatibilidad con usos futuros.
    - Tipo (1 byte) El tipo de LS al que hace referencia;  
      1 para LS, 3 para LS2, 5 para cifrado, 7 para meta, 0 para desconocido.
    - Costo (prioridad) (1 byte)
    - Expira (4 bytes) (4 bytes, big endian, segundos desde la época, se reinicia en 2106)
  - Número de revocaciones (1 byte) Máximo TBD
  - Revocaciones: Cada revocación contiene: (32 bytes)
    - Hash (32 bytes)

  Firma LS2 Estándar:
  - Firma (40+ bytes)
    La firma es de todo lo anterior.
```

Flags y propiedades: para uso futuro


### Notas

- Un servicio distribuido que use esto tendría uno o más "maestros" con la  
  clave privada del destino del servicio. Determinarían (fuera de banda) la  
  lista actual de destinos activos y publicarían el Meta LS2. Para  
  redundancia, múltiples maestros podrían hacer multihoming (es decir, publicar simultáneamente) el  
  Meta LS2.

- Un servicio distribuido podría comenzar con un solo destino o usar multihoming de estilo antiguo,  
  luego pasar a un Meta LS2. Una búsqueda LS estándar podría devolver  
  cualquiera de un LS, LS2 o Meta LS2.

- Cuando un servicio usa un Meta LS2, no tiene túneles (leases).


### Registro de Servicio

Este es un registro individual que indica que un destino está participando en un  
servicio. Se envía desde el participante al floodfill. Nunca se envía  
individualmente por un floodfill, sino solo como parte de una Lista de Servicios. El Registro de Servicio también se usa para revocar la participación en un servicio, estableciendo la  
expiración en cero.

Esto no es un LS2 pero usa el formato estándar de encabezado y firma LS2.

Buscar con  
    n/a, ver Lista de Servicios  
Almacenar con  
    Tipo Registro de Servicio (9)  
Almacenar en  
    Hash del nombre del servicio  
    Este hash se usa luego para generar la "clave de enrutamiento" diaria, como en LS1  
Expiración típica  
    Horas. Máximo 18.2 horas (65535 segundos)  
Publicado por  
    Destino

### Formato

```
Encabezado LS2 Estándar como se especificó anteriormente

  Parte Específica del Tipo Registro de Servicio
  - Puerto (2 bytes, big endian) (0 si no especificado)
  - Hash del nombre del servicio (32 bytes)

  Firma LS2 Estándar:
  - Firma (40+ bytes)
    La firma es de todo lo anterior.
```

### Notas

- Si expira es todo cero, el floodfill debería revocar el registro y ya no  
  incluirlo en la lista de servicios.

- Almacenamiento: El floodfill puede limitar estrictamente el almacenamiento de estos registros y  
  limitar el número de registros almacenados por hash y su expiración. También puede usarse  
  una lista blanca de hashes.

- Cualquier otro tipo netdb en el mismo hash tiene prioridad, por lo que un registro de servicio nunca puede  
  sobrescribir un LS/RI, pero un LS/RI sobrescribirá todos los registros de servicio en ese hash.



### Lista de Servicios

Esto no es nada parecido a un LS2 y usa un formato diferente.

La lista de servicios es creada y firmada por el floodfill. Es no autenticada  
en el sentido de que cualquiera puede unirse a un servicio publicando un Registro de Servicio a un  
floodfill.

Una Lista de Servicios contiene Registros de Servicio Cortos, no Registros de Servicio completos. Estos  
contienen firmas pero solo hashes, no destinos completos, por lo que no pueden verificarse sin el destino completo.

La seguridad, si la hay, y la conveniencia de las listas de servicios está por determinar.  
Los floodfills podrían limitar la publicación y búsquedas a una lista blanca de servicios,  
pero esa lista blanca puede variar según la implementación o preferencia del operador.  
Puede no ser posible lograr consenso sobre una lista blanca común y básica  
entre implementaciones.

Si el nombre del servicio se incluye en el registro de servicio anterior,  
entonces los operadores de floodfill pueden objetar; si solo se incluye el hash,  
no hay verificación, y un registro de servicio podría "entrar" antes que  
cualquier otro tipo netdb y almacenarse en el floodfill.

Buscar con  
    Tipo de búsqueda Lista de Servicios (11)  
Almacenar con  
    Tipo Lista de Servicios (11)  
Almacenar en  
    Hash del nombre del servicio  
    Este hash se usa luego para generar la "clave de enrutamiento" diaria, como en LS1  
Expiración típica  
    Horas, no especificada en la lista misma, según política local  
Publicado por  
    Nadie, nunca se envía al floodfill, nunca se inunda.

### Formato

NO usa el encabezado LS2 estándar especificado anteriormente.

```
- Tipo (1 byte)
    No está realmente en el encabezado, pero forma parte de los datos cubiertos por la firma.
    Tómese del campo en el mensaje de Almacenamiento en la Base de Datos.
  - Hash del nombre del servicio (implícito, en el mensaje de Almacenamiento en la Base de Datos)
  - Hash del Creador (floodfill) (32 bytes)
  - Marca de tiempo de publicación (8 bytes, big endian)

  - Número de Registros de Servicio Cortos (1 byte)
  - Lista de Registros de Servicio Cortos:
    Cada Registro de Servicio Corto contiene (90+ bytes)
    - Hash de destino (32 bytes)
    - Marca de tiempo de publicación (8 bytes, big endian)
    - Expira (4 bytes, big endian) (desplazamiento desde la publicación en ms)
    - Flags (2 bytes)
    - Puerto (2 bytes, big endian)
    - Longitud de firma (2 bytes, big endian)
    - Firma del destino (40+ bytes)

  - Número de Registros de Revocación (1 byte)
  - Lista de Registros de Revocación:
    Cada Registro de Revocación contiene (86+ bytes)
    - Hash de destino (32 bytes)
    - Marca de tiempo de publicación (8 bytes, big endian)
    - Flags (2 bytes)
    - Puerto (2 bytes, big endian)
    - Longitud de firma (2 bytes, big endian)
    - Firma del destino (40+ bytes)

  - Firma del floodfill (40+ bytes)
    La firma es de todo lo anterior.
```

Para verificar la firma de la Lista de Servicios:

- anteponer el hash del nombre del servicio
- eliminar el hash del creador
- Verificar la firma del contenido modificado

Para verificar la firma de cada Registro de Servicio Corto:

- Obtener el destino
- Verificar la firma de (marca de tiempo de publicación + expira + flags + puerto + Hash del  
  nombre del servicio)

Para verificar la firma de cada Registro de Revocación:

- Obtener el destino
- Verificar la firma de (marca de tiempo de publicación + 4 bytes cero + flags + puerto + Hash  
  del nombre del servicio)

### Notas

- Usamos longitud de firma en lugar de tipo de firma para soportar tipos de firma desconocidos.

- No hay expiración de una lista de servicios, los receptores pueden tomar su propia  
  decisión según política o la expiración de los registros individuales.

- Las Listas de Servicios no se inundan, solo los Registros de Servicio individuales lo son. Cada  
  floodfill crea, firma y almacena en caché una Lista de Servicios. El floodfill usa su  
  propia política para el tiempo de caché y el número máximo de registros de servicio y revocación.



## Cambios Requeridos en la Especificación de Estructuras Comunes


### Certificados de Clave

Fuera del alcance de esta propuesta.  
Añadir a las propuestas ECIES 144 y 145.


### Nuevas Estructuras Intermedias

Añadir nuevas estructuras para Lease2, MetaLease, LeaseSet2Header y OfflineSignature.  
Efectivo a partir de la versión 0.9.38.


### Nuevos Tipos NetDB

Añadir estructuras para cada nuevo tipo de leaseset, incorporadas de arriba.  
Para LeaseSet2, EncryptedLeaseSet y MetaLeaseSet,  
efectivo a partir de la versión 0.9.38.  
Para Registro de Servicio y Lista de Servicios,  
preliminar y no programado.


### Nuevo Tipo de Firma

Añadir RedDSA_SHA512_Ed25519 Tipo 11.  
Clave pública de 32 bytes; clave privada de 32 bytes; hash de 64 bytes; firma de

---
title: "Registros de Servicio en LS2"
number: "167"
author: "zzz, orignal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Cerrado"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## Estado
Aprobado en la segunda revisión el 2025-04-01; las especificaciones están actualizadas; aún no implementado.


## Visión general

I2P carece de un sistema DNS centralizado.  
Sin embargo, la libreta de direcciones, junto con el sistema de nombres de host b32, permite  
al router buscar destinos completos y obtener conjuntos de arrendamientos (lease sets), que contienen  
una lista de puertas de enlace y claves para que los clientes puedan conectarse a ese destino.

Por tanto, los conjuntos de arrendamientos (leasesets) son algo así como un registro DNS. Pero actualmente no existe una forma de  
saber si ese host soporta algún servicio, ya sea en ese destino o en uno diferente,  
de manera similar a los [registros SRV de DNS](https://en.wikipedia.org/wiki/SRV_record) definidos en [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782).

La primera aplicación de esto podría ser el correo electrónico punto a punto.  
Otras aplicaciones posibles: DNS, GNS, servidores de claves, autoridades de certificados, servidores de tiempo,  
bittorrent, criptomonedas, otras aplicaciones punto a punto.


## Propuestas y alternativas relacionadas

### Listas de servicios

La [Propuesta 123](/proposals/123-new-netdb-entries/) de LS2 definió 'registros de servicio' que indicaban que un destino  
participaba en un servicio global. Los floodfills agruparían estos registros  
en 'listas de servicios' globales.  
Esto nunca se implementó debido a la complejidad, falta de autenticación,  
preocupaciones de seguridad y spam.

Esta propuesta es diferente en que proporciona una búsqueda de servicio para un destino específico,  
no un grupo global de destinos para algún servicio global.

### GNS

GNS propone que cada uno ejecute su propio servidor DNS.  
Esta propuesta es complementaria, en el sentido de que podríamos usar registros de servicio para indicar  
que GNS (o DNS) está soportado, con un nombre de servicio estándar "domain" en el puerto 53.

### Dot well-known

Se ha [propuesto](http://i2pforum.i2p/viewtopic.php?p=3102) que los servicios se busquen mediante una solicitud HTTP a  
/.well-known/i2pmail.key. Esto requiere que cada servicio tenga un sitio web asociado que aloje la clave. La mayoría de los usuarios no ejecutan sitios web.

Una solución alternativa es suponer que un servicio para una dirección b32 realmente  
se ejecuta en esa dirección b32. Así, buscar el servicio para example.i2p requiere  
la obtención HTTP desde http://example.i2p/.well-known/i2pmail.key, pero  
un servicio para aaa...aaa.b32.i2p no requiere esa búsqueda, puede conectarse directamente.

Pero hay una ambigüedad aquí, porque example.i2p también puede ser referenciado por su b32.

### Registros MX

Los registros SRV son simplemente una versión genérica de los registros MX para cualquier servicio.  
"_smtp._tcp" es el registro "MX".  
No hay necesidad de registros MX si tenemos registros SRV, y los registros MX  
por sí solos no proporcionan un registro genérico para cualquier servicio.


## Diseño

Los registros de servicio se colocan en la sección de opciones en [LS2](/docs/specs/common-structures/).  
La sección de opciones de LS2 actualmente no se utiliza.  
No soportado para LS1.  
Esto es similar a la [propuesta de ancho de banda de túnel](/proposals/168-tunnel-bandwidth/),  
que define opciones para registros de construcción de túneles.

Para buscar una dirección de servicio para un nombre de host o b32 específico, el router obtiene el  
conjunto de arrendamientos (leaseset) y busca el registro de servicio en las propiedades.

El servicio puede estar alojado en el mismo destino que el LS mismo, o puede referenciar  
un nombre de host/b32 diferente.

Si el destino objetivo para el servicio es diferente, el LS objetivo también  
debe incluir un registro de servicio, apuntando a sí mismo, indicando que soporta el servicio.

El diseño no requiere soporte especial, caché ni cambios en los floodfills.  
Solo el publicador del conjunto de arrendamientos y el cliente que busca un registro de servicio  
deben soportar estos cambios.

Se proponen extensiones menores a I2CP y SAM para facilitar la recuperación de  
registros de servicio por parte de los clientes.



## Especificación

### Especificación de opción LS2

Las opciones LS2 DEBEN estar ordenadas por clave, para que la firma sea invariante.

Definidas de la siguiente manera:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Nombre simbólico del servicio deseado. Debe estar en minúsculas. Ejemplo: "smtp".  
  Los caracteres permitidos son [a-z0-9-] y no debe comenzar ni terminar con un '-'.  
  Se deben usar identificadores estándar del [registro de tipos de servicio DNS-SD](http://www.dns-sd.org/ServiceTypes.html) o de /etc/services de Linux si están definidos allí.
- proto := Protocolo de transporte del servicio deseado. Debe estar en minúsculas, ya sea "tcp" o "udp".  
  "tcp" significa transmisión continua (streaming) y "udp" significa datagramas con respuesta.  
  Los indicadores de protocolo para datagramas sin formato y datagram2 podrían definirse más adelante.  
  Los caracteres permitidos son [a-z0-9-] y no debe comenzar ni terminar con un '-'.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := tiempo de vida, segundos enteros. Entero positivo. Ejemplo: "86400".  
  Se recomienda un mínimo de 86400 (un día), ver la sección Recomendaciones para más detalles.
- priority := Prioridad del host objetivo, valor más bajo significa más preferido. Entero no negativo. Ejemplo: "0"  
  Solo útil si hay más de un registro, pero requerido incluso si solo hay un registro.
- weight := Peso relativo para registros con la misma prioridad. Valor más alto significa mayor probabilidad de ser elegido. Entero no negativo. Ejemplo: "0"  
  Solo útil si hay más de un registro, pero requerido incluso si solo hay un registro.
- port := Puerto I2CP en el que se encuentra el servicio. Entero no negativo. Ejemplo: "25"  
  El puerto 0 está soportado pero no recomendado.
- target := Nombre de host o b32 del destino que proporciona el servicio. Un [nombre de host](/docs/overview/naming/) válido. Debe estar en minúsculas.  
  Ejemplo: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" o "example.i2p".  
  Se recomienda usar b32 a menos que el nombre de host sea "bien conocido", es decir, esté en libretas de direcciones oficiales o predeterminadas.
- appoptions := texto arbitrario específico de la aplicación, no debe contener " " ni ",". La codificación es UTF-8.

### Ejemplos

En LS2 para aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, apuntando a un servidor SMTP:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

En LS2 para aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, apuntando a dos servidores SMTP:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

En LS2 para bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, apuntando a sí mismo como servidor SMTP:

    "_smtp._tcp" "0 999999 25"

Formato posible para redirigir correo (ver más abajo):

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### Límites

La estructura de datos de mapeo usada para las opciones LS2 limita claves y valores a un máximo de 255 bytes (no caracteres).  
Con un destino b32, el optionvalue tiene aproximadamente 67 bytes, por lo que solo cabrían 3 registros.  
Quizás solo uno o dos con un campo appoptions largo, o hasta cuatro o cinco con un nombre de host corto.  
Esto debería ser suficiente; múltiples registros deberían ser raros.


### Diferencias con RFC 2782

- Sin puntos finales
- Sin nombre después del proto
- Requiere minúsculas
- En formato de texto con registros separados por comas, no en formato binario DNS
- Indicadores de tipo de registro diferentes
- Campo appoptions adicional


### Notas

No se permite el uso de comodines como (asterisco), (asterisco)._tcp, o _tcp.  
Cada servicio soportado debe tener su propio registro.



### Registro de nombres de servicio

Los identificadores no estándar que no estén listados en el [registro de tipos de servicio DNS-SD](http://www.dns-sd.org/ServiceTypes.html) o en /etc/services de Linux  
pueden solicitarse y añadirse a la [especificación de estructuras comunes](/docs/specs/common-structures/).

Los formatos appoptions específicos del servicio también pueden añadirse allí.


### Especificación I2CP

El [protocolo I2CP](/docs/specs/i2cp/) debe ampliarse para soportar búsquedas de servicios.  
Se requieren códigos de error adicionales en MessageStatusMessage y/o HostReplyMessage relacionados con la búsqueda de servicios.  
Para hacer la funcionalidad de búsqueda general, no solo específica para registros de servicio,  
el diseño es soportar la recuperación de todas las opciones LS2.

Implementación: Ampliar HostLookupMessage para añadir solicitud de  
opciones LS2 para hash, nombre de host y destino (tipos de solicitud 2-4).  
Ampliar HostReplyMessage para añadir el mapeo de opciones si se solicita.  
Ampliar HostReplyMessage con códigos de error adicionales.

Los mapeos de opciones pueden almacenarse en caché o en caché negativa por un corto tiempo en el lado del cliente o del router,  
dependiendo de la implementación. El tiempo máximo recomendado es una hora, a menos que el TTL del registro de servicio sea menor.  
Los registros de servicio pueden almacenarse en caché hasta el TTL especificado por la aplicación, el cliente o el router.

Ampliar la especificación como sigue:

#### Opciones de configuración

Añadir lo siguiente a las [opciones de configuración I2CP](/docs/specs/i2cp/)

i2cp.leaseSetOption.nnn

Opciones a incluir en el conjunto de arrendamientos. Solo disponible para LS2.  
nnn comienza en 0. El valor de la opción contiene "key=value".  
(no incluir comillas)

Ejemplo:  
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### Mensaje HostLookup

- Tipo de búsqueda 2: Búsqueda por hash, solicita mapeo de opciones
- Tipo de búsqueda 3: Búsqueda por nombre de host, solicita mapeo de opciones
- Tipo de búsqueda 4: Búsqueda por destino, solicita mapeo de opciones

Para el tipo de búsqueda 4, el elemento 5 es un Destino.



#### Mensaje HostReply

Para los tipos de búsqueda 2-4, el router debe obtener el conjunto de arrendamientos,  
incluso si la clave de búsqueda está en la libreta de direcciones.

Si tiene éxito, HostReply contendrá el mapeo de opciones  
del conjunto de arrendamientos, e incluirá como elemento 5 después del destino.  
Si no hay opciones en el mapeo, o si el conjunto de arrendamientos era de la versión 1,  
aún se incluirá como un mapeo vacío (dos bytes: 0 0).  
Se incluirán todas las opciones del conjunto de arrendamientos, no solo las opciones de registro de servicio.  
Por ejemplo, podrían estar presentes opciones para parámetros definidos en el futuro.

En caso de fallo en la búsqueda del conjunto de arrendamientos, la respuesta contendrá un nuevo código de error 6 (fallo en la búsqueda del conjunto de arrendamientos)  
y no incluirá un mapeo.  
Cuando se devuelva el código de error 6, el campo Destino puede o no estar presente.  
Estará presente si la búsqueda por nombre de host en la libreta de direcciones fue exitosa,  
o si una búsqueda anterior fue exitosa y el resultado fue almacenado en caché,  
o si el Destino estaba presente en el mensaje de búsqueda (tipo de búsqueda 4).

Si un tipo de búsqueda no es soportado,  
la respuesta contendrá un nuevo código de error 7 (tipo de búsqueda no soportado).



### Especificación SAM

El [protocolo SAMv3](/docs/api/samv3/) debe ampliarse para soportar búsquedas de servicios.

Ampliar NAMING LOOKUP como sigue:

NAMING LOOKUP NAME=example.i2p OPTIONS=true solicita el mapeo de opciones en la respuesta.

NAME puede ser un destino base64 completo cuando OPTIONS=true.

Si la búsqueda del destino fue exitosa y había opciones presentes en el conjunto de arrendamientos,  
entonces en la respuesta, tras el destino,  
habrá una o más opciones en la forma OPTION:key=value.  
Cada opción tendrá un prefijo OPTION: separado.  
Se incluirán todas las opciones del conjunto de arrendamientos, no solo las opciones de registro de servicio.  
Por ejemplo, podrían estar presentes opciones para parámetros definidos en el futuro.  
Ejemplo:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Las claves que contengan '=', y claves o valores que contengan un salto de línea,  
se consideran inválidas y el par clave/valor será eliminado de la respuesta.

Si no se encuentran opciones en el conjunto de arrendamientos, o si el conjunto de arrendamientos era de la versión 1,  
la respuesta no incluirá ninguna opción.

Si OPTIONS=true estaba en la búsqueda y no se encuentra el conjunto de arrendamientos, se devolverá un nuevo valor de resultado LEASESET_NOT_FOUND.


## Alternativa de búsqueda de nombres

Se consideró un diseño alternativo, para soportar búsquedas de servicios  
como un nombre de host completo, por ejemplo _smtp._tcp.example.i2p,  
actualizando la [especificación de nombres](/docs/overview/naming/) para especificar el manejo de nombres de host que comienzan con '_'.  
Esto fue rechazado por dos razones:

- Aún serían necesarios cambios en I2CP y SAM para pasar la información de TTL y puerto al cliente.
- No sería una funcionalidad general que podría usarse para recuperar otras opciones LS2  
  que podrían definirse en el futuro.


## Recomendaciones

Los servidores deben especificar un TTL de al menos 86400, y el puerto estándar para la aplicación.



## Características avanzadas

### Búsquedas recursivas

Podría ser deseable soportar búsquedas recursivas, donde cada conjunto de arrendamientos sucesivo  
se verifique en busca de un registro de servicio que apunte a otro conjunto de arrendamientos, estilo DNS.  
Esto probablemente no sea necesario, al menos en una implementación inicial.

TODO



### Campos específicos de la aplicación

Podría ser deseable tener datos específicos de la aplicación en el registro de servicio.  
Por ejemplo, el operador de example.i2p podría querer indicar que el correo debe  
reenviarse a example@mail.i2p. La parte "example@" necesitaría estar en un campo separado  
del registro de servicio, o eliminarse del destino.

Incluso si el operador ejecuta su propio servicio de correo, podría querer indicar que  
el correo debe enviarse a example@example.i2p. La mayoría de los servicios I2P los ejecuta una sola persona.  
Así que un campo separado también podría ser útil aquí.

TODO cómo hacer esto de forma genérica


### Cambios necesarios para correo electrónico

Fuera del alcance de esta propuesta. Ver la [discusión en i2pforum](http://i2pforum.i2p/viewtopic.php?p=3102) para más detalles.


## Notas de implementación

El almacenamiento en caché de registros de servicio hasta el TTL puede hacerse por el router o la aplicación,  
dependiendo de la implementación. Si se almacena en caché de forma persistente también depende de la implementación.

Las búsquedas también deben buscar el conjunto de arrendamientos objetivo y verificar que contiene un registro "self"  
antes de devolver el destino objetivo al cliente.


## Análisis de seguridad

Como el conjunto de arrendamientos está firmado, cualquier registro de servicio dentro de él está autenticado por la clave de firma del destino.

Los registros de servicio son públicos y visibles para los floodfills, a menos que el conjunto de arrendamientos esté cifrado.  
Cualquier router que solicite el conjunto de arrendamientos podrá ver los registros de servicio.

Un registro SRV distinto de "self" (es decir, uno que apunte a un destino diferente de nombre de host/b32)  
no requiere el consentimiento del nombre de host/b32 objetivo.  
No está claro si una redirección de un servicio a un destino arbitrario podría facilitar algún  
tipo de ataque, o cuál sería el propósito de tal ataque.  
Sin embargo, esta propuesta mitiga tal ataque al exigir que el destino  
también publique un registro SRV "self". Los implementadores deben verificar la existencia de un registro "self"  
en el conjunto de arrendamientos del destino.


## Compatibilidad

LS2: Sin problemas. Todas las implementaciones conocidas actualmente ignoran el campo de opciones en LS2,  
y pasan correctamente por alto un campo de opciones no vacío.  
Esto fue verificado en pruebas tanto por Java I2P como por i2pd durante el desarrollo de LS2.  
LS2 fue implementado en la versión 0.9.38 en 2016 y es bien soportado por todas las implementaciones de routers.  
El diseño no requiere soporte especial, caché ni cambios en los floodfills.

Nombres: '_' no es un carácter válido en los nombres de host de i2p.

I2CP: Los tipos de búsqueda 2-4 no deben enviarse a routers con una versión de API inferior  
a la versión mínima en la que se soporta (por determinar).

SAM: El servidor SAM de Java ignora claves/valores adicionales como OPTIONS=true.  
i2pd debería hacer lo mismo, por verificar.  
Los clientes SAM no obtendrán los valores adicionales en la respuesta a menos que se soliciten con OPTIONS=true.  
No debería ser necesario un aumento de versión.


## Migración

Las implementaciones pueden añadir soporte en cualquier momento, no se necesita coordinación,  
excepto un acuerdo sobre la versión de API efectiva para los cambios en I2CP.  
Las versiones de compatibilidad SAM para cada implementación se documentarán en la especificación SAM.


## Referencias

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)

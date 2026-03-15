---
title: "Propuesta I2P #166: Tipos de Túneles Conscientes de Identidad/Host"
number: "166"
author: "eyedeekay"
created: "2024-05-27"
lastupdated: "2024-08-27"
status: "Open"
thread: "http://i2pforum.i2p/viewforum.php?f=13"
target: "0.9.65"
toc: true
---
### Propuesta para un tipo de túnel HTTP Proxy consciente del host

Esta es una propuesta para resolver el "Problema de Identidad Compartida" en el uso convencional de HTTP sobre I2P mediante la introducción de un nuevo tipo de túnel HTTP Proxy. Este tipo de túnel tiene un comportamiento adicional destinado a prevenir o limitar la utilidad del rastreo realizado por posibles operadores hostiles de servicios ocultos, contra agentes de usuario específicos (navegadores) y la propia Aplicación Cliente de I2P.

#### ¿Qué es el problema de "Identidad Compartida"?

El problema de "Identidad Compartida" ocurre cuando un agente de usuario en una red superpuesta con direcciones criptográficas comparte una identidad criptográfica con otro agente de usuario. Esto sucede, por ejemplo, cuando Firefox y GNU Wget están ambos configurados para usar el mismo Proxy HTTP.

En este escenario, es posible que el servidor recoja y almacene la dirección criptográfica (Destination) utilizada para responder a la actividad. Puede tratar esto como una "huella digital" que siempre es 100% única, porque tiene origen criptográfico. Esto significa que la vinculación observada por el problema de Identidad Compartida es perfecta.

¿Pero es un problema?
^^^^^^^^^^^^^^^^^^^^

El problema de identidad compartida es un problema cuando los agentes de usuario que utilizan el mismo protocolo desean unlinkabilidad. [Fue mencionado por primera vez en el contexto de HTTP en este hilo de Reddit](https://old.reddit.com/r/i2p/comments/579idi/warning_i2p_is_linkablefingerprintable/), con los comentarios eliminados accesibles gracias a [pullpush.io](https://api.pullpush.io/reddit/search/comment/?link_id=579idi). *En aquel momento* yo era uno de los respondientes más activos, y *en aquel momento* creía que el problema era pequeño. En los últimos 8 años, la situación y mi opinión sobre él han cambiado; ahora creo que la amenaza planteada por la correlación maliciosa de destinos crece considerablemente a medida que más sitios están en condiciones de "perfilizar" usuarios específicos.

Esta ataque tiene una barrera de entrada muy baja. Solo requiere que un operador de servicio oculto gestione múltiples servicios. Para ataques sobre visitas contemporáneas (visitar múltiples sitios al mismo tiempo), este es el único requisito. Para vinculaciones no contemporáneas, uno de esos servicios debe ser un servicio que aloje "cuentas" que pertenezcan a un solo usuario al que se desea rastrear.

Actualmente, cualquier operador de servicios que aloje cuentas de usuario podrá correlacionarlas con la actividad en cualquier sitio que controle explotando el problema de Identidad Compartida. Mastodon, Gitlab o incluso foros simples podrían ser atacantes disfrazados siempre que operen más de un servicio y tengan interés en crear un perfil para un usuario. Esta vigilancia podría realizarse por acoso, ganancia económica o motivos relacionados con inteligencia. En este momento hay docenas de operadores importantes que podrían llevar a cabo este ataque y obtener datos significativos de él. Por ahora confiamos mayormente en que no lo hagan, pero podrían surgir fácilmente actores que no les importen nuestras opiniones.

Esto está directamente relacionado con una forma bastante básica de creación de perfiles en la web clara, donde las organizaciones pueden correlacionar interacciones en su sitio con interacciones en redes que controlan. En I2P, debido a que el destino criptográfico es único, esta técnica a veces puede ser incluso más confiable, aunque sin el poder adicional de la geolocalización.

La Identidad Compartida no es útil contra un usuario que utiliza I2P únicamente para ofuscar su geolocalización. Tampoco puede usarse para romper el enrutamiento de I2P. Es solo un problema de gestión de identidad contextual.

-  Es imposible usar el problema de Identidad Compartida para geolocalizar a un usuario de I2P.
-  Es imposible usar el problema de Identidad Compartida para vincular sesiones de I2P si no son contemporáneas.

Sin embargo, es posible usarlo para degradar el anonimato de un usuario de I2P en circunstancias que probablemente son muy comunes. Una razón por la que son comunes es porque fomentamos el uso de Firefox, un navegador web que soporta operación con "pestañas".

-  Es *siempre* posible producir una huella digital a partir del problema de Identidad Compartida en *cualquier* navegador web que soporte solicitar recursos de terceros.
-  Desactivar Javascript no logra **nada** contra el problema de Identidad Compartida.
-  Si se puede establecer un vínculo entre sesiones no contemporáneas, por ejemplo mediante la huella digital de navegador "tradicional", entonces la Identidad Compartida puede aplicarse de forma transitiva, posiblemente permitiendo una estrategia de vinculación no contemporánea.
-  Si se puede establecer un vínculo entre una actividad en la red clara y una identidad I2P, por ejemplo, si el objetivo ha iniciado sesión en un sitio con presencia tanto en I2P como en la red clara en ambos lados, la Identidad Compartida puede aplicarse de forma transitiva, posiblemente permitiendo una desanonimización completa.

La forma en que usted vea la gravedad del problema de Identidad Compartida en relación con el proxy HTTP de I2P depende de dónde usted (o más precisamente, un "usuario" con expectativas potencialmente no informadas) considere que reside la "identidad contextual" para la aplicación. Hay varias posibilidades:

1. HTTP es tanto la Aplicación como la Identidad Contextual — Así es como funciona ahora. Todas las Aplicaciones HTTP comparten una identidad.
2. El Proceso es la Aplicación y la Identidad Contextual — Así es como funciona cuando una aplicación usa una API como SAMv3 o I2CP, donde una aplicación crea su identidad y controla su duración.
3. HTTP es la Aplicación, pero el Host es la Identidad Contextual — Este es el objetivo de esta propuesta, que trata a cada Host como una posible "Aplicación Web" y considera la superficie de ataque como tal.

¿Es soluble?
^^^^^^^^^^^^^^^

Probablemente no sea posible crear un proxy que responda inteligentemente a todos los casos posibles en los que su operación podría debilitar el anonimato de una aplicación. Sin embargo, es posible construir un proxy que responda inteligentemente a una aplicación específica que se comporte de manera predecible. Por ejemplo, en navegadores web modernos, se espera que los usuarios tengan múltiples pestañas abiertas, interactuando con múltiples sitios web, que se distinguen por nombre de host.

Esto nos permite mejorar el comportamiento del Proxy HTTP para este tipo de agente de usuario HTTP haciendo que el comportamiento del proxy coincida con el del agente de usuario, asignando a cada host su propio Destination cuando se usa con el Proxy HTTP. Este cambio hace imposible usar el problema de Identidad Compartida para derivar una huella digital que pueda usarse para correlacionar la actividad del cliente con 2 hosts, porque los 2 hosts ya no compartirán una identidad de retorno.

Descripción:
^^^^^^^^^^^^

Se creará un nuevo Proxy HTTP y se añadirá al Gestor de Servicios Ocultos (I2PTunnel). El nuevo Proxy HTTP operará como un "multiplexor" de I2PSocketManagers. El multiplexor en sí no tiene destino. Cada I2PSocketManager individual que forme parte del multiplex tiene su propio destino local y su propio grupo de túneles. Los I2PSocketManagers se crean bajo demanda por el multiplexor, donde la "demanda" es la primera visita a un nuevo host. Es posible optimizar la creación de los I2PSocketManagers antes de insertarlos en el multiplexor creando uno o más por adelantado y almacenándolos fuera del multiplexor. Esto podría mejorar el rendimiento.

Un I2PSocketManager adicional, con su propio destino, se configura como portador de un "Outproxy" para cualquier sitio que *no* tenga un Destino I2P, por ejemplo cualquier sitio de la red clara. Esto convierte efectivamente todo el uso de Outproxy en una única Identidad Contextual, con la salvedad de que configurar múltiples Outproxys para el túnel provocará la rotación "Sticky" normal del outproxy, donde cada outproxy solo recibe solicitudes para un solo sitio. Este es *casi* el comportamiento equivalente al aislamiento de proxies HTTP sobre I2P por destino, en la internet clara.

Consideraciones de recursos:
''''''''''''''''''''''''''''

El nuevo proxy HTTP requiere recursos adicionales en comparación con el proxy HTTP existente. Esto implicará:

-  Potencialmente construir más túneles e I2PSocketManagers
-  Construir túneles con más frecuencia

Cada uno de estos requiere:

-  Recursos informáticos locales
-  Recursos de red de los pares

Configuración:
''''''''''''''

Para minimizar el impacto del aumento del uso de recursos, el proxy debe configurarse para usar lo mínimo posible. Los proxies que formen parte del multiplexor (no el proxy principal) deben configurarse para:

-  Los I2PSocketManagers multiplexados construyan 1 túnel de entrada, 1 túnel de salida en sus grupos de túneles
-  Los I2PSocketManagers multiplexados usen 3 saltos por defecto.
-  Cerrar sockets tras 10 minutos de inactividad
-  Los I2PSocketManagers iniciados por el Multiplexor comparten la duración del Multiplexor. Los túneles multiplexados no se "destruyen" hasta que lo hace el Multiplexor principal.

Diagramas:
^^^^^^^^^

El diagrama siguiente representa el funcionamiento actual del proxy HTTP, que corresponde a la "Posibilidad 1." en la sección "¿Es un problema?". Como puede verse, el proxy HTTP interactúa con sitios I2P directamente usando solo un destino. En este escenario, HTTP es tanto la aplicación como la identidad contextual.

```text
**Situación actual: HTTP es la Aplicación, HTTP es la Identidad Contextual**
                                                      __-> Outproxy <-> i2pgit.org
                                                     /
Browser <-> HTTP Proxy(un Destino)<->I2PSocketManager <---> idk.i2p
                                                     \__-> translate.idk.i2p
                                                      \__-> git.idk.i2p
```

El diagrama siguiente representa el funcionamiento de un proxy HTTP consciente del host, que corresponde a la "Posibilidad 3." en la sección "¿Es un problema?". En este escenario, HTTP es la aplicación, pero el Host define la identidad contextual, donde cada sitio I2P interactúa con un proxy HTTP diferente con un destino único por host. Esto impide que los operadores de múltiples sitios puedan distinguir cuándo la misma persona visita múltiples sitios que ellos operan.

```text
**Después del cambio: HTTP es la Aplicación, el Host es la Identidad Contextual**
                                                    __-> I2PSocketManager(Destino A - Solo Outproxies) <--> i2pgit.org
                                                   /
Browser <-> HTTP Proxy Multiplexor(Sin Destino) <---> I2PSocketManager(Destino B) <--> idk.i2p
                                                   \__-> I2PSocketManager(Destino C) <--> translate.idk.i2p
                                                    \__-> I2PSocketManager(Destino C) <--> git.idk.i2p
```

Estado:
^^^^^^^

Una implementación funcional en Java del proxy consciente del host que cumple con una versión anterior de esta propuesta está disponible en el fork de idk bajo la rama: i2p.i2p.2.6.0-browser-proxy-post-keepalive Enlace en citas. Está en revisión intensiva, con el fin de dividir los cambios en secciones más pequeñas.

Se han escrito implementaciones con capacidades variables en Go usando la biblioteca SAMv3, que podrían ser útiles para integrar en otras aplicaciones Go o para go-i2p, pero no son adecuadas para Java I2P. Además, carecen de buen soporte para trabajar interactivamente con leaseSets cifrados.

Apéndice: ``i2psocks``
                      

Es posible un enfoque orientado a aplicaciones simples para aislar otros tipos de clientes sin implementar un nuevo tipo de túnel ni cambiar el código I2P existente, combinando herramientas existentes de I2PTunnel que ya están ampliamente disponibles y probadas en la comunidad de privacidad. Sin embargo, este enfoque hace una suposición difícil que no es cierta para HTTP ni para muchos otros tipos potenciales de clientes I2P.

Aproximadamente, el siguiente script producirá un proxy SOCKS5 consciente de la aplicación y socksificará el comando subyacente:

```sh
#! /bin/sh
command_to_proxy="$@"
java -jar ~/i2p/lib/i2ptunnel.jar -wait -e 'sockstunnel 7695'
torsocks --port 7695 $command_to_proxy
```

Apéndice: ``ejemplo de implementación del ataque``
                                                  

[Un ejemplo de implementación del ataque de Identidad Compartida sobre Agentes de Usuario HTTP](https://github.com/eyedeekay/colluding_sites_attack/) ha existido durante varios años. Un ejemplo adicional está disponible en el subdirectorio ``simple-colluder`` del [repositorio prop166 de idk](https://git.idk.i2p/idk/i2p.host-aware-proxy). Estos ejemplos están diseñados deliberadamente para demostrar que el ataque funciona y requerirían modificaciones (aunque menores) para convertirse en un ataque real.

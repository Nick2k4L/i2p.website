---
title: "Introducción a I2P: una guía completa para principiantes"
description: "Introducción a I2P: una guía completa para principiantes"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P es una red anónima cifrada completamente y de igual a igual que funciona "dentro" de internet**, y la implementación en Java de geti2p.net sigue siendo la forma principal de usarla. A diferencia de Tor, que principalmente anonimiza el acceso a la web convencional, I2P crea una red totalmente autónoma compuesta por servicios ocultos, sitios web, correo electrónico, chat y compartición de archivos.

---

## Lo que sucede en el momento en que inicias I2P

Después de la instalación, I2P inicia una aplicación web local llamada **consola del router** en `http://127.0.0.1:7657`. Este es tu centro de control, funciona completamente en tu máquina y está vinculado a localhost por seguridad. En el primer inicio, un **asistente de configuración** te guía a través de la selección de idioma, elección de tema (oscuro o claro) y una prueba automatizada de ancho de banda que dura aproximadamente un minuto utilizando el servicio externo de medición M-Lab. Luego, estableces qué porcentaje de tu ancho de banda compartir con la red.

![Asistente de configuración de I2P - Selección de idioma](/images/guides/quickstart/wizard-language-selection.webp)

Una vez que el asistente finaliza, el router comienza un proceso denominado "reseeding" o **arranque inicial**. Su router descarga aproximadamente **100 registros RouterInfo** desde servidores de reseeding preconfigurados mediante HTTPS, obteniendo así una lista inicial de pares. A partir de ahí, comienza a crear **túneles exploratorios** para descubrir más pares y completar su copia local de la base de datos de la red (la "netDb"). Durante estos primeros minutos, verá un mensaje que dice "Rechazando túneles: iniciando". Esto es normal.

![Reinicio de I2P - Arranque inicial](/images/guides/quickstart/reseed-bootstrapping.webp)

**Espere esperar entre 3 y 10 minutos** antes de que su router sea utilizable, y mucho más tiempo —días de funcionamiento continuo— antes de alcanzar el rendimiento máximo. La barra lateral de la consola del router muestra su cantidad de pares como "Activos x/y", donde x son los pares con los que ha intercambiado mensajes recientemente e y es el total de pares vistos. Una vez que vea **10 o más pares activos**, su router estará conectado de forma saludable. Lo más importante que puede hacer un nuevo usuario es **dejar el router funcionando continuamente**. Tras un apagado, otros nodos marcan su router como poco confiable durante al menos 24 horas, por lo que los reinicios frecuentes reducen drásticamente el rendimiento.

![Panel de la consola del router I2P](/images/guides/quickstart/router-console-dashboard.png)

---

## Configurar tu navegador para I2P

A diferencia de la red Tor, I2P no incluye un navegador dedicado. Para acceder a sitios I2P (el dominio pseudo-nivel superior `.i2p`), debes configurar la configuración de proxy de tu navegador para enrutar el tráfico a través del proxy HTTP de I2P en el puerto **4444**.

**La opción más sencilla para usuarios de Windows** es el **paquete de instalación fácil**, que incluye Java, el router y un perfil preconfigurado de Firefox con la extensión "I2P in Private Browsing". Esto elimina toda configuración manual del proxy. Desde la descarga hasta navegar por sitios I2P tarda aproximadamente cuatro minutos. También hay disponible en versión beta un paquete de instalación fácil para macOS (Apple Silicon). Si estás utilizando el paquete de instalación fácil, puedes omitir la configuración manual que se describe a continuación.

### Firefox (Recomendado)

Se recomienda encarecidamente Firefox porque tiene su propia configuración de proxy independiente del sistema operativo; Chrome y Edge utilizan la configuración de proxy del sistema que afecta a todas las aplicaciones.

**Paso 1.** Abre el menú de Firefox (ícono de hamburguesa) y haz clic en **Configuración**.

![Firefox - Abrir configuración](/images/guides/browser-config/accessi2p_3.png)

**Paso 2.** Busca **proxy** en la barra de búsqueda de configuración, luego haz clic en **Configuración...** junto a Configuración de red.

![Firefox - Buscar proxy](/images/guides/browser-config/accessi2p_4.png)

**Paso 3.** Seleccione **Configuración manual del proxy**, ingrese `127.0.0.1` para el proxy HTTP y `4444` para el puerto, luego haga clic en **Aceptar**.

![Firefox - Configuración manual del proxy](/images/guides/browser-config/accessi2p_5.png)

Después de configurar el proxy, se recomiendan varios ajustes en `about:config`:

- Establecer `media.peerConnection.ice.proxy_only` en **true** (evita fugas de WebRTC)
- Establecer `keyword.enabled` en **false** (detiene las redirecciones del motor de búsqueda en direcciones .i2p)
- Crear un valor booleano `browser.fixup.domainsuffixwhitelist.i2p` establecido en **true** (indica a Firefox que `.i2p` es un sufijo de dominio válido)

Una trampa persistente para principiantes: siempre escribe `http://` antes de las direcciones `.i2p`. La mayoría de los sitios I2P no usan HTTPS (I2P ya cifra todo el tráfico de extremo a extremo), y sin este prefijo Firefox te redirigirá a un motor de búsqueda.

### Chrome / Edge (Windows)

Nota: Chrome y Edge utilizan la configuración de proxy de tu sistema operativo, lo que afecta a **todas** las aplicaciones de tu sistema.

**Paso 1.** Abre el menú de Chrome y haz clic en **Configuración**.

![Chrome - Abrir Configuración](/images/guides/browser-config/accessi2p_6.png)

**Paso 2.** Busca **proxy**, luego haz clic en **Abrir la configuración de proxy de tu computadora**.

![Chrome - Buscar proxy](/images/guides/browser-config/accessi2p_7.png)

**Paso 3.** En **Configuración manual del proxy**, haz clic en **Configurar** junto a "Usar un servidor proxy".

![Windows - Configuración de proxy](/images/guides/browser-config/accessi2p_8.png)

**Paso 4.** Activa **Usar un servidor proxy**, ingresa `127.0.0.1` como dirección IP del proxy y `4444` como puerto, luego haz clic en **Guardar**.

![Windows - Editar servidor proxy](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**Paso 1.** Ve a **Safari → Configuración → Avanzado** y haz clic en **Cambiar configuración...** junto a Proxies.

![Safari - Configuración avanzada](/images/guides/browser-config/accessi2p_1.png)

**Paso 2.** Activa el **proxy web (HTTP)**, introduce `127.0.0.1` como servidor y `4444` como puerto, luego haz clic en **Aceptar**.

![macOS - Configuración de proxy web](/images/guides/browser-config/accessi2p_2.png)

---

## Entendiendo el panel de control de la consola del router

La consola del router en `127.0.0.1:7657` muestra varios indicadores clave que le indican qué tan bien está funcionando su nodo. La **barra lateral** muestra su versión de I2P, tiempo de actividad, uso de ancho de banda (entrada/salida), cantidad de pares activos y estado de los túneles. Cuando "Clientes Compartidos" se vuelve verde, su router está integrado y listo.

![Consola del router - Clientes compartidos en verde](/images/guides/quickstart/shared-clients-green.png)

Los **gráficos de ancho de banda** muestran el rendimiento en tiempo real. Los valores predeterminados son conservadores: **96 KBps de descarga y 40 KBps de subida**, compartiendo solo 48 KBps; la documentación oficial recomienda encarecidamente aumentar estos valores. Navega a `http://127.0.0.1:7657/config` (o haz clic en "Configurar ancho de banda" en la consola) para elevar tus límites. Un mayor ancho de banda compartido mejora tanto tu propio rendimiento como la salud de la red. Establecer el ancho de banda compartido por debajo de **12 KBps** coloca efectivamente a tu router en "modo oculto", desconectándote del tráfico participativo. A partir de **128 KBps o más**, tu router podría ser promovido a estado *floodfill*, lo que significa que ayuda a mantener la tabla hash distribuida.

![Configuración de ancho de banda](/images/guides/quickstart/bandwidth-config.png)

La sección **estado del túnel** muestra los túneles participantes: tráfico que estás retransmitiendo para otros. Más del 90 % de los routers I2P retransmiten tráfico participante por defecto. Esto actúa simultáneamente como tráfico de cobertura para tu propio anonimato y como tu contribución a la red. Los túneles expiran cada 10 minutos y se reconstruyen automáticamente.

![Administrador de I2PTunnel](/images/guides/quickstart/tunnel-manager.png)

El **gestor de I2PTunnel** en `http://127.0.0.1:7657/i2ptunnel/` muestra todos tus túneles configurados: el proxy HTTP, IRC, correo electrónico y el túnel de tu servidor eepsite vienen preconfigurados directamente desde la instalación.

![Lista de I2PTunnel](/images/guides/quickstart/i2ptunnel-list.png)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Console page</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">URL</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Home / Status</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/home</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Dashboard with peers, bandwidth, tunnels</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Bandwidth config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/config</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Adjust speed limits and share percentage</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Network config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/confignet</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Firewall, port, and reachability settings</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Tunnel manager</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2ptunnel/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage all I2P tunnels and hidden services</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">I2PSnark</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2psnark/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in BitTorrent client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">SusiMail</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/susimail/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in email client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Address book</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/dns</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage .i2p hostname mappings</td>
</tr>
</tbody>
</table>
---

## Cinco cosas que puedes hacer una vez conectado

### Navegar sitios web .i2p

El uso más inmediato de I2P es navegar por sitios web ocultos. Con tu navegador configurado para usar el proxy del puerto 4444, accede a cualquier dirección `.i2p`. Varios sitios conocidos sirven como buenos puntos de partida: **`i2p-projekt.i2p`** es el sitio oficial del proyecto I2P reflejado dentro de la red, **`i2pforum.i2p`** aloja el foro comunitario de soporte, **`stats.i2p`** ofrece estadísticas de la red y un servicio de registro de direcciones, y **`notbob.i2p`** registra el tiempo de actividad de los eepsites conocidos para que puedas ver qué está realmente en línea. Cuando encuentres una dirección `.i2p` desconocida, el proxy ofrecerá enlaces de "servicio de salto" que resuelven el nombre de host; haz clic en ellos para agregar nuevos sitios a tu libreta de direcciones local.

I2P también incluye un **outproxy** predeterminado (`exit.stormycloud.i2p`) que te permite acceder a internet regular a través de I2P, pero esta no es la función principal de la red y el rendimiento será lento. I2P está diseñado como una darknet interna, no como una red de nodos de salida como Tor.

### Comparte archivos torrent anónimamente con I2PSnark

**I2PSnark** es un cliente BitTorrent completamente funcional integrado en cada instalación de I2P, accesible en `http://127.0.0.1:7657/i2psnark/`. Funciona completamente dentro de la red I2P: no puede conectarse a torrents de la internet clara, y los usuarios de la internet clara no pueden ver los torrents de I2P. La interfaz web admite enlaces magnéticos (magnet links), DHT, arrastrar y soltar, búsqueda de torrents, descargas secuenciales y rastreadores UDP (agregados en la versión 2.10.0). La longitud predeterminada del túnel es de tres saltos. Simplemente agregue archivos `.torrent` o enlaces magnéticos a través de la interfaz.

![Interfaz de I2PSnark](/images/guides/quickstart/i2psnark-interface.png)

Para encontrar torrents, visita el **Postman Tracker** en `http://tracker2.postman.i2p/` - un centro centralizado donde los usuarios buscan y descargan torrents que han sido subidos por otros dentro de la red I2P. También puedes subir tus propios torrents para compartirlos con la comunidad.

![Postman Tracker](/images/guides/quickstart/postman-tracker.png)

Otros clientes torrent compatibles con I2P incluyen BiglyBT y qBittorrent con un complemento I2P.

### Enviar correo electrónico cifrado con SusiMail

**SusiMail** en `http://127.0.0.1:7657/susimail/` es un cliente de correo electrónico basado en web diseñado para evitar fugas de información identificativa. Se conecta al servidor de correo **`mail.i2p`** operado por "postman". Para comenzar, regístrese en una cuenta en **`hq.postman.i2p`** (accesible a través de su proxy de I2P), luego inicie sesión con esas credenciales en SusiMail. Las entradas preconfiguradas de I2PTunnel enrutan SMTP a través de `localhost:7659` y POP3 a través de `localhost:7660`. Puede enviar correos tanto a otros usuarios `@mail.i2p` como a direcciones de correo electrónico regulares de Internet (mediante puente a través del outproxy del servidor de correo). SusiMail soporta formato markdown, adjuntos por arrastrar y soltar, y correo HTML.

![Bandeja de entrada de SusiMail](/images/guides/quickstart/susimail-login.png)

![Redactar SusiMail](/images/guides/quickstart/susimail-inbox.png)

### Chatea en IRC a través de la red Irc2P

I2P incluye un **túnel IRC preconfigurado** en `localhost:6668`. Apunte cualquier cliente IRC a esta dirección (con SSL/TLS **deshabilitado** - I2P maneja el cifrado) y se conectará a la red Irc2P, una federación de servidores que incluye `irc.postman.i2p`, `irc.echelon.i2p` y `irc.dg.i2p`. Los canales principales son **`#i2p`** para discusiones generales, **`#i2p-dev`** para desarrollo y **`#i2p-help`** para soporte. El túnel IRC elimina automáticamente la información identificativa de su conexión. Los clientes recomendados incluyen WeeChat, Pidgin y Thunderbird Chat.

### Aloja tu propio sitio web anónimo

Cada instalación de I2P incluye un **servidor web Jetty** ya en ejecución en `localhost:7658` con un túnel de servidor I2P correspondiente. Para publicar un sitio, simplemente coloque los archivos HTML en el directorio raíz: `~/.i2p/eepsite/docroot` en Linux o `%LOCALAPPDATA%\I2P\I2P Site\docroot` en Windows. Su sitio obtendrá automáticamente un destino criptográfico en Base64 y una dirección más corta `xxxxx.b32.i2p`. Para obtener un nombre legible como `mysite.i2p`, regístrelo en servicios de libreta de direcciones como `stats.i2p` o `no.i2p`. Para configuraciones más avanzadas, puede reemplazar Jetty con Apache o Nginx detrás del túnel de servidor I2PTunnel, solo recuerde eliminar los encabezados del servidor que revelen información. Para una guía detallada, consulte nuestra guía [Crear un Eepsite en I2P](/docs/guides/creating-an-eepsite/).

---

## Prácticas esenciales de seguridad para nuevos usuarios

**Nunca navegues por I2P y por la clearnet en el mismo perfil del navegador.** Esta es la regla de seguridad más importante. Crea un perfil dedicado de Firefox a través de `about:profiles` o utiliza el perfil preconfigurado del Paquete de Instalación Fácil. La contaminación cruzada de cookies, historial y datos almacenados en caché entre tu navegación anónima e identificada es el error más común de seguridad operativa.

La extensión oficial de Firefox **"I2P in Private Browsing"** (disponible en la tienda de complementos de Mozilla) automatiza gran parte de este proceso creando pestañas con contenedores aislados, con anti-huellas digitales, aislamiento de primera parte y recuadro de cartas (letterboxing) habilitados. Para usuarios de Chromium, inícielo con banderas separadas: `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`.

---

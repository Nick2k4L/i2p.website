---
title: "Duplicando tus Servicios en I2P"
description: "Una guía amigable para principiantes sobre cómo hacer que tus sitios web, repositorios de Git, APIs y más estén disponibles en la red I2P — con instrucciones paso a paso y diagramas"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

Tienes un sitio web en internet normal. Ahora quieres hacerlo disponible también en I2P — para que las personas puedan visitarlo de forma privada, sin revelar quiénes son o de dónde vienen. De eso trata esta guía.

El mirroring no reemplaza tu sitio existente. Agrega una segunda entrada — una privada — a través de la red I2P. Tu sitio clearnet sigue funcionando exactamente como antes.

![Cómo funciona el mirroring de I2P — tu servidor obtiene una segunda entrada privada a través de la red I2P](/images/guides/mirroring/how-mirroring-works.svg)

## ¿Por qué hacer un espejo en I2P?

Hay varias razones prácticas para crear mirrors de tus servicios:

**Privacidad para tus visitantes.** Las personas pueden acceder a tu contenido sin exponer su dirección IP. El tráfico entre ellos y tu servicio se cifra a través de múltiples saltos: ni tú ni nadie que esté monitoreando la red puede identificar quién está visitando.

**Resistencia a la censura.** Si tu sitio está bloqueado en ciertas regiones por filtrado DNS, bloqueo de IP u otros medios, el mirror de I2P permanece accesible. No depende de DNS o enrutamiento IP convencional.

**Resistencia.** Un mirror de I2P añade redundancia. Si tu dominio es incautado o tu CDN te abandona, la versión de I2P permanece activa mientras tu servidor esté funcionando.

**Apoyando la red.** Cada servicio en I2P hace que la red sea más útil y ayuda a hacer crecer el ecosistema.

## Lo que necesitarás

Antes de comenzar, asegúrate de tener:

- **Un router I2P en funcionamiento** en tu servidor (la implementación Java). Si aún no tienes uno, sigue primero la [Guía de Instalación de I2P](/downloads/).
- **Tu sitio web o servicio ya funcionando** — debe estar sirviendo contenido en tu servidor.
- **Comodidad básica con la línea de comandos** — estarás editando un archivo de configuración y ejecutando algunos comandos.
- **Aproximadamente 15–20 minutos** — eso es todo lo que se necesita.

Tu router I2P necesita al menos 512 MB de RAM y funciona mejor en un servidor con tiempo de actividad 24/7. Si tu router acaba de iniciarse por primera vez, dale 10-15 minutos para integrarse con la red antes de crear tunnels.

## Entendiendo los Tunnels

El concepto central detrás del mirroring de I2P es el **server tunnel**. La idea es la siguiente:

Cuando alguien en I2P quiere visitar tu sitio, su solicitud viaja a través de varios saltos cifrados a través de la red I2P hasta que llega a tu router I2P. Tu router luego entrega la solicitud a un **túnel de servidor**, que la reenvía a tu servidor web ejecutándose en localhost. Tu servidor web responde, y la respuesta toma el camino inverso de regreso a través de la red cifrada.

Tu servidor web nunca toca la internet pública para estas solicitudes — solo se comunica con localhost. El router I2P maneja todo lo que da hacia la red.

### ¿Qué Tipo de Tunnel Necesitas?

I2P ofrece varios tipos de túnel para diferentes situaciones:

![Comparación de tipos de tunnel — HTTP Server es la opción correcta para la mayoría de sitios web](/images/guides/mirroring/tunnel-types.svg)

Para crear un mirror de un sitio web, casi con certeza quieres un túnel **HTTP Server**. Está diseñado específicamente para tráfico web y maneja el filtrado de encabezados, compresión y spoofing de hostname automáticamente. Los otros tipos existen para casos de uso especializados como acceso SSH, aplicaciones bidireccionales o servidores IRC.

## Parte 1: Crear un Espejo de un Sitio Web

Este es el escenario más común: tienes un sitio web clearnet existente y quieres hacerlo disponible a través de I2P. Aquí está el proceso de un vistazo:

![Los cinco pasos para crear un mirror de tu sitio en I2P](/images/guides/mirroring/steps-overview.svg)

Veamos cada paso.

### Paso 1: Agregar un Listener de Localhost a tu Servidor Web

Tu sitio clearnet probablemente ya esté funcionando en los puertos 80 y 443, abierto al mundo. Para I2P, crearás un listener *separado* en localhost al que solo el tunnel I2P puede acceder. Esto te da control completo sobre cómo se ve la versión de I2P — puedes eliminar headers, bloquear paneles de administración y ajustar el caché para la mayor latencia de I2P.

> **Alternativa rápida:** Si no necesitas ninguna personalización, puedes omitir este paso y dirigir el túnel I2P directamente a `127.0.0.1:80`. Pero se recomienda el enfoque de listener dedicado.

Elige tu servidor web:

#### Nginx

Crea una nueva configuración de sitio:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Pega esta configuración, reemplazando `yoursite.i2p` y la ruta raíz con tus propios valores:

```nginx
server {
    # Only listen on localhost — the I2P tunnel connects here
    listen 127.0.0.1:8080;

    server_name yoursite.i2p yoursite.b32.i2p;

    # Point this to the same content as your clearnet site
    root /var/www/your-site;
    index index.html;

    # Don't reveal server software
    server_tokens off;

    # Security headers — note: NO HSTS (it breaks I2P access)
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "same-origin" always;

    # Restrict resources to your own site only
    add_header Content-Security-Policy
        "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'"
        always;

    location / {
        try_files $uri $uri/ =404;

        # Aggressive caching reduces the impact of I2P latency
        expires 1d;
        add_header Cache-Control "public, immutable";
    }

    # Cache static assets even more aggressively
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Optional: block admin areas from I2P visitors
    location ~ ^/(admin|wp-admin|login) {
        return 403;
    }
}
```
Habilitarlo y recargar:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Crea una nueva configuración de sitio:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Pega esta configuración:

```apache
<VirtualHost 127.0.0.1:8080>
    ServerName yoursite.i2p
    ServerAlias yoursite.b32.i2p

    DocumentRoot /var/www/your-site

    # Hide server identification
    ServerSignature Off
    ServerTokens Prod
    TraceEnable Off

    <IfModule mod_headers.c>
        Header unset X-Powered-By
        Header unset Server
        # Never include HSTS — it breaks I2P
        Header unset Strict-Transport-Security

        Header always set X-Content-Type-Options "nosniff"
        Header always set X-Frame-Options "SAMEORIGIN"
        Header always set Referrer-Policy "same-origin"
        Header always set Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'"

        # Aggressive caching for I2P latency
        Header set Cache-Control "public, max-age=86400, immutable"
    </IfModule>

    <Directory /var/www/your-site>
        Options -Indexes -FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>

    # Optional: block admin areas from I2P visitors
    <LocationMatch "^/(admin|wp-admin|login)">
        Require all denied
    </LocationMatch>
</VirtualHost>
```
Luego añade el puerto, habilita el sitio y recarga:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### ¿Por qué no HSTS?

Notarás que ambas configuraciones evitan explícitamente los headers `Strict-Transport-Security`. Esto es crítico. HSTS le dice a los navegadores que solo usen HTTPS, pero I2P no usa TLS tradicional — el cifrado se maneja en la capa de red en su lugar. Incluir HSTS bloquearía completamente a los visitantes de tu sitio I2P.

### Paso 2: Crear el Túnel del Servidor

Abre la Consola del Router I2P en tu navegador:

```
http://127.0.0.1:7657/i2ptunnel/
```
Haz clic en **"Tunnel Wizard"** para comenzar a crear un nuevo túnel.

![I2P Tunnel Wizard startup](/images/guides/mirroring/mirror_02.svg)

Selecciona **"HTTP Server"** como el tipo de túnel y haz clic en **Siguiente**.

### Paso 3: Configurar el Tunnel

Complete la configuración del tunnel:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Setting</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Name</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">My Website Mirror</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Any descriptive name</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Description</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(optional)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Helps you remember what this tunnel is for</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Target Host</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>127.0.0.1</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Always localhost</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Target Port</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>8080</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Must match the port from Step 1</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Website Hostname</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>mysite.i2p</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The .i2p name you want (registered later)</td>
    </tr>
  </tbody>
</table>
![Configuración del tunnel](/images/guides/mirroring/mirror_03.png)

Haz clic en **"Create"** para generar tu tunnel. I2P creará una clave de destino criptográfica única — esto se convierte en tu dirección permanente en la red.

### Paso 4: Iniciar el Tunnel y Esperar

Encuentra tu nuevo tunnel en la lista y haz clic en **"Iniciar"**. Verás:

- **Destino Local** — una dirección base32 larga como `abc123...xyz.b32.i2p`
- **Estado** — debería cambiar a "En Ejecución"

![Estado de ejecución del tunnel](/images/guides/mirroring/mirror_04.png)

> **¡Ten paciencia!** El primer arranque toma de 2 a 5 minutos mientras tu tunnel se construye y publica sus leaseSets en la red. Esto es normal.

### Paso 5: Prueba tu Mirror

Una vez que el tunnel muestre que está ejecutándose, abre tu navegador configurado para I2P y visita tu dirección base32. La primera carga de página puede tomar de 5 a 30 segundos — eso es típico en I2P.

Si la página se carga, ¡felicitaciones! — ¡tu sitio ahora está activo en I2P!

### Paso 6: Registrar una Dirección .i2p Legible (Opcional)

Tu sitio ya es accesible a través de la dirección base32, pero `abc123...xyz.b32.i2p` no es precisamente fácil de recordar. Para obtener un dominio `.i2p` limpio:

**Para tu propia libreta de direcciones** — ve a `http://127.0.0.1:7657/dns` y añade el nombre de host elegido asociado a tu clave de destino.

**Para descubrimiento público** — regístrate en el registro de direcciones I2P:

1. Visita `http://stats.i2p/i2p/addkey.html` (dentro de I2P)
2. Ingresa el nombre de host deseado y tu clave de destino completa (la cadena de más de 500 caracteres de los detalles de tu tunnel, que termina en "AAAA")
3. Envía para registro

Una vez registrado, cualquier persona con las suscripciones de libreta de direcciones apropiadas podrá encontrar tu sitio por nombre.

## Parte 2: Duplicación de Aplicaciones Dinámicas

Si tu sitio web funciona con un framework backend (Node.js, Python, Ruby, PHP, etc.) en lugar de archivos estáticos, necesitas Nginx o Apache como proxy inverso entre el túnel I2P y tu aplicación.

### Configuración de Proxy Inverso (Nginx)

```nginx
server {
    listen 127.0.0.1:8080;
    server_name yourapp.i2p;

    server_tokens off;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-I2P-Request "true";

        # CRITICAL: never forward real IP headers
        proxy_set_header X-Forwarded-For "";
        proxy_set_header X-Real-IP "";

        # Strip headers that leak information
        proxy_hide_header Strict-Transport-Security;
        proxy_hide_header X-Powered-By;
        proxy_hide_header Server;

        # Extended timeouts — I2P is slower than clearnet
        proxy_connect_timeout 60s;
        proxy_read_timeout 120s;
        proxy_send_timeout 60s;
    }
}
```
La cabecera `X-I2P-Request` permite que tu aplicación detecte el tráfico de I2P si necesita comportarse de manera diferente (por ejemplo, deshabilitando funciones que requieren acceso a clearnet).

### Reescritura de URL para Mirrors de Clearnet

Si tu aplicación genera URLs que apuntan a tu dominio clearnet, querrás reescribirlas para los visitantes de I2P:

```nginx
location / {
    proxy_pass http://127.0.0.1:3000;

    sub_filter_once off;
    sub_filter_types text/html text/css application/javascript;

    # Rewrite your clearnet domain to the I2P domain
    sub_filter 'https://www.example.com' 'http://yoursite.i2p';
    sub_filter '//www.example.com' '//yoursite.i2p';
}
```
Luego crea un túnel de Servidor HTTP que apunte a `127.0.0.1:8080`, tal como en la Parte 1.

## Parte 3: Creación de Mirrors de Repositorios Git

### Gitea (Con Todas las Características)

Gitea es una excelente opción para alojar Git sobre I2P. Tiene una interfaz web, seguimiento de problemas y pull requests, todo lo cual funciona bien a través de la red.

Configurar `/etc/gitea/app.ini`:

```ini
[server]
HTTP_ADDR     = 127.0.0.1
HTTP_PORT     = 3000
DOMAIN        = yourgit.i2p
ROOT_URL      = http://yourgit.i2p/
SSH_DOMAIN    = yourgit.i2p
PROTOCOL      = http
OFFLINE_MODE  = true

[service]
DISABLE_REGISTRATION    = false
REGISTER_MANUAL_CONFIRM = true
REGISTER_EMAIL_CONFIRM  = false

[mailer]
ENABLED = false

[session]
COOKIE_SECURE = false
```
Puntos clave: `OFFLINE_MODE = true` evita que Gitea cargue recursos externos (avatares, assets de CDN). `COOKIE_SECURE = false` es necesario porque I2P no usa HTTPS en el sentido tradicional. Desactiva el correo electrónico ya que tu servidor I2P puede no tener configurado correo saliente.

Crea dos tunnels: 1. **tunnel de Servidor HTTP** → `127.0.0.1:3000` (interfaz web) 2. **tunnel de Servidor Estándar** → `127.0.0.1:22` (acceso SSH para git push/pull — opcional)

### cgit (Alternativa Ligera)

Si solo necesitas navegación de solo lectura y clonado HTTP, cgit es mucho más ligero:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=http://yourgit.i2p/$CGIT_REPO_URL
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
El almacenamiento en caché agresivo de cgit lo hace particularmente adecuado para la mayor latencia de I2P.

### Configuración del Cliente para Git sobre I2P

Cualquier persona que clone desde tu mirror Git de I2P necesita enrutar el tráfico de Git a través del proxy HTTP de I2P:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy http://127.0.0.1:4444
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone http://yourgit.i2p/repo
```
Para repositorios grandes, los clones superficiales ahorran mucho tiempo a través de I2P:

```bash
git clone --depth 1 http://yourgit.i2p/project
git fetch --unshallow   # grab full history later if needed
```
## Parte 4: Duplicación de Alojamiento de Archivos

### Nextcloud

Nextcloud funciona sobre I2P con algo de configuración. Edita `config/config.php`:

```php
$CONFIG = array(
    'trusted_domains' => array(
        0 => 'localhost',
        1 => 'yourbase32address.b32.i2p',
        2 => 'yoursite.i2p',
    ),
    'trusted_proxies'   => array('127.0.0.1'),
    'overwritehost'     => 'yoursite.i2p',
    'overwriteprotocol' => 'http',
    'overwrite.cli.url' => 'http://yoursite.i2p/',
);
```
Lo que funciona bien: carga y descarga de archivos, navegación de directorios, autenticación, compartir enlaces públicos y WebDAV. Lo que no: los clientes de sincronización de escritorio necesitan configuración de proxy SOCKS, los backends de almacenamiento externo pueden filtrar direcciones IP, y la federación con instancias de Nextcloud de clearnet puede comprometer la privacidad.

### Servidor de Archivos Simple

Para el alojamiento directo de archivos sin la sobrecarga de Nextcloud, un servidor Python mínimo hace el trabajo:

```python
#!/usr/bin/env python3
import http.server
import socketserver

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    server_version = ""  # don't reveal server software
    sys_version = ""

with socketserver.TCPServer(("127.0.0.1", 8080), QuietHandler) as httpd:
    print("Serving on 127.0.0.1:8080")
    httpd.serve_forever()
```
Crear un túnel de servidor HTTP que apunte a `127.0.0.1:8080`.

## Parte 5: APIs de Duplicación

### Proxy de API Básico

```nginx
server {
    listen 127.0.0.1:8080;
    server_name api.yoursite.i2p;

    server_tokens off;

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_set_header Host $host;
        proxy_set_header Content-Type $content_type;

        # Strip identifying headers
        proxy_set_header X-Forwarded-For "";
        proxy_set_header X-Real-IP "";
        proxy_hide_header X-Powered-By;

        # I2P-appropriate timeouts
        proxy_connect_timeout 60s;
        proxy_read_timeout 120s;
    }
}
```
### Soporte para WebSocket

Si tu aplicación usa WebSockets (aplicaciones de chat, paneles en vivo, etc.):

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}

server {
    listen 127.0.0.1:8080;

    location /ws {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;

        # Long timeout for persistent connections
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
        proxy_buffering off;
    }
}
```
Ten en cuenta que WebSockets sobre I2P tendrán una latencia notablemente mayor que clearnet. Para funciones en tiempo real, considera intervalos de sondeo más largos o actualizaciones de interfaz optimistas en el lado del cliente.

## Mejores Prácticas de Seguridad

Hacer que tu mirror funcione es la parte fácil. Mantenerlo seguro requiere prestar atención a algunos detalles que son únicos del alojamiento en I2P.

![Lista de verificación de seguridad para mirrors de I2P](/images/guides/mirroring/security-checklist.svg)

### Las Reglas Principales

**Vincular solo a localhost.** Su servicio debe escuchar en `127.0.0.1`, nunca en `0.0.0.0`. El router I2P es lo único que debería poder acceder a su servicio.

**Eliminar cabeceras identificativas.** Los servidores web adoran anunciar qué software están ejecutando. A través de I2P, esta es información que no quieres compartir.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">What It Leaks</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">How to Fix</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Server</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Web server software and version</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>server_tokens off;</code> (Nginx)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>X-Powered-By</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Application framework</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_hide_header X-Powered-By;</code></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>X-Forwarded-For</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP addresses in proxy chain</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_set_header X-Forwarded-For "";</code></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>X-Real-IP</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Client IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_set_header X-Real-IP "";</code></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Strict-Transport-Security</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Breaks I2P access entirely</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_hide_header Strict-Transport-Security;</code></td>
    </tr>
  </tbody>
</table>
**Aloja todo por ti mismo.** No cargues fuentes de Google, scripts de CDNs, o analíticas de terceros. Cada recurso externo es una solicitud que sale de la red I2P, añadiendo una enorme latencia y potencialmente filtrando información. Descarga las librerías y fuentes, ponlas en tu servidor, y sírvelas localmente.

**Nunca expongas bases de datos.** Debería ser obvio, pero no crees tunnels I2P hacia los puertos de tu base de datos. Los tunnels de servidor solo deberían apuntar a servidores web o servidores de aplicaciones.

## Optimización de Rendimiento

I2P añade entre 2 y 10 segundos de latencia por solicitud. Ese es el precio del cifrado multi-salto. Pero con el ajuste adecuado, tu mirror de I2P puede sentirse sorprendentemente ágil.

### Cachear Agresivamente

Los recursos estáticos deben tener tiempos de vida de caché largos. Si un visitante ya ha cargado tu CSS e imágenes, no debería tener que esperar a que se carguen nuevamente:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Habilitar Compresión

Cargas útiles más pequeñas significan transferencias más rápidas sobre el ancho de banda limitado de I2P:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Ajustar la Cantidad de Túneles para el Tráfico

Más tunnels significa más conexiones concurrentes. El valor predeterminado de 3 está bien para sitios de poco tráfico, pero si estás viendo congestión:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Longitud del Tunnel (Saltos)

Cada salto añade latencia pero también añade anonimato. Elige según tu modelo de amenazas:

![Intercambio de saltos de tunnel — más saltos significa más privacidad pero mayor latencia](/images/guides/mirroring/tunnel-hops.svg)

Para un mirror público donde la identidad del servidor ya es conocida (el sitio web de tu organización, por ejemplo), reducir a 2 saltos es un compromiso razonable:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Consejos Generales del Router

- Ejecuta tu router I2P **24/7**. Cuanto más tiempo esté activo, mejor integrado estará con la red, y más rápido funcionarán tus tunnels.
- Configura el ancho de banda compartido a al menos **256 KB/sec**, pero mantenlo ligeramente por debajo de la velocidad real de tu línea.
- Espera que las primeras conexiones después de un reinicio sean lentas (30–90 segundos). Esto mejora rápidamente a medida que se construyen los tunnels.

## Avanzado: Configuración Manual de Tunnels

El asistente de la Consola del Router funciona muy bien, pero si prefieres editar archivos de configuración directamente — o necesitas automatizar despliegues — puedes configurar tunnels en `~/.i2p/i2ptunnel.config` (o `/var/lib/i2p/i2p-config/i2ptunnel.config` para instalaciones del sistema):

```properties
# HTTP Server Tunnel
tunnel.0.name=My Website
tunnel.0.description=I2P mirror of my clearnet site
tunnel.0.type=httpserver
tunnel.0.targetHost=127.0.0.1
tunnel.0.targetPort=8080
tunnel.0.privKeyFile=mysite-privKeys.dat
tunnel.0.spoofedHost=mysite.i2p
tunnel.0.startOnLoad=true
tunnel.0.sharedClient=false

# I2CP connection settings
tunnel.0.i2cpHost=127.0.0.1
tunnel.0.i2cpPort=7654

# Tunnel pool configuration
tunnel.0.option.inbound.length=3
tunnel.0.option.inbound.quantity=3
tunnel.0.option.inbound.backupQuantity=1
tunnel.0.option.outbound.length=3
tunnel.0.option.outbound.quantity=3
tunnel.0.option.outbound.backupQuantity=1
```
Reinicia I2P después de los cambios:

```bash
sudo systemctl restart i2p
```
A partir de I2P 0.9.42, también puedes usar archivos de configuración individuales en `i2ptunnel.config.d/` para una gestión más limpia de múltiples tunnels:

```bash
mkdir -p ~/.i2p/i2ptunnel.config.d/

cat > ~/.i2p/i2ptunnel.config.d/mysite.config <<EOF
tunnel.0.name=My Website
tunnel.0.type=httpserver
tunnel.0.targetHost=127.0.0.1
tunnel.0.targetPort=8080
tunnel.0.privKeyFile=mysite-privKeys.dat
tunnel.0.startOnLoad=true
EOF
```
## Solución de problemas

### "No puedo acceder a mi sitio"

Trabaja con esta lista de verificación en orden:

**1. ¿Está realmente escuchando el servidor web?**

```bash
nc -zv 127.0.0.1 8080
```
Si esto falla, la configuración de tu servidor web tiene un problema — regresa al Paso 1.

**2. ¿Está funcionando el tunnel?** Visita `http://127.0.0.1:7657/i2ptunnel/` y verifica el estado. Si dice "Starting" por más de 5 minutos, revisa la integración de red de tu router.

**3. ¿Está publicado el LeaseSet?** Asegúrate de que `i2cp.dontPublishLeaseSet` NO esté configurado en las opciones de tu túnel. Sin un LeaseSet publicado, nadie puede encontrar tu túnel.

**4. ¿Está tu reloj en hora?** I2P requiere precisión horaria dentro de 60 segundos. Verifica con:

```bash
timedatectl status
```
Si tu reloj está desincronizado, I2P tendrá problemas para construir tunnels.

### Rendimiento lento después del reinicio

Esto es normal. Después de reiniciar tu router I2P, dale entre 10 y 15 minutos para reconstruir sus pools de tunnel y reintegrarse con la red. El rendimiento mejora a medida que más peers aprenden sobre tu router.

También verifica que el reenvío de puertos esté configurado para tu puerto I2NP (consulta la Consola del Router para el número de puerto específico). Sin esto, tu router opera en modo "con firewall", lo que limita el rendimiento.

### Errores de "Dirección no encontrada" cuando otros visitan

Los visitantes necesitan tu dirección en su libreta de direcciones. Asegúrate de haberte registrado en una libreta de direcciones pública, o comparte tu dirección base32 completa directamente. También pueden agregar más suscripciones en `http://127.0.0.1:7657/susidns/subscriptions`:

```
http://stats.i2p/cgi-bin/newhosts.txt
http://i2host.i2p/cgi-bin/i2hostetag
```
### Tiempos de espera al realizar pruebas

I2P tiene inherentemente tiempos de ida y vuelta más altos. Al realizar pruebas desde la línea de comandos, usa timeouts extendidos:

```bash
# curl
curl --connect-timeout 60 --max-time 300 http://yoursite.i2p/

# wget
wget --timeout=300 http://yoursite.i2p/
```
### Leyendo los registros

Si nada más ayuda, revisa los logs del router I2P para buscar errores:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Respalda Tus Claves

Esto es lo único que absolutamente no debes omitir. Los archivos de clave privada de tu tunnel (archivos `.dat` en tu directorio de configuración I2P) son los que le dan a tu servicio su dirección permanente en la red. Si los pierdes, pierdes tu dirección I2P — permanentemente. No hay recuperación, no hay reinicio, no hay ticket de soporte. Tendrías que empezar de nuevo con una nueva dirección.

Haz una copia de seguridad ahora:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Almacena la copia de seguridad en un lugar seguro y fuera del servidor.

## Has Terminado

Eso es todo. Tu servicio ahora está disponible tanto en internet regular como en la red I2P. Estás ofreciendo a las personas una forma privada de acceder a tu contenido, una donde su identidad permanece siendo suya.

Si tienes problemas o quieres involucrarte más, aquí es donde puedes encontrar a la comunidad:

- **Foro:** [i2pforum.net](https://i2pforum.net)
- **IRC:** #i2p en varias redes
- **Desarrollo:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*Guía creada por [StormyCloud Inc](https://www.stormycloud.org) para la comunidad I2P.*

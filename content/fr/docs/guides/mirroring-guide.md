---
title: "Mettre en miroir vos services sur I2P"
description: "Un guide convivial pour les débutants pour rendre vos sites web, dépôts Git, API et plus encore disponibles sur le réseau I2P — avec des instructions étape par étape et des diagrammes"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

Vous avez un site web sur l'internet classique. Maintenant vous voulez le rendre disponible sur I2P aussi — pour que les gens puissent le visiter de manière privée, sans révéler qui ils sont ou d'où ils viennent. C'est l'objet de ce guide.

La mise en miroir ne remplace pas votre site existant. Elle ajoute une seconde entrée — privée — via le réseau I2P. Votre site clearnet continue de fonctionner exactement comme avant.

![Comment fonctionne la mise en miroir I2P — votre serveur obtient une seconde entrée privée via le réseau I2P](/images/guides/mirroring/how-mirroring-works.svg)

## Pourquoi créer un miroir sur I2P ?

Il existe plusieurs raisons pratiques de mettre en miroir vos services :

**Confidentialité pour vos visiteurs.** Les gens peuvent accéder à votre contenu sans exposer leur adresse IP. Le trafic entre eux et votre service est chiffré à travers plusieurs relais — ni vous ni quiconque surveille le réseau ne peut identifier qui visite.

**Résistance à la censure.** Si votre site est bloqué dans certaines régions par filtrage DNS, blocage IP, ou autres moyens, le miroir I2P reste accessible. Il ne dépend pas du DNS ou du routage IP conventionnel.

**Résilience.** Un miroir I2P ajoute de la redondance. Si votre domaine est saisi ou que votre CDN vous abandonne, la version I2P reste en ligne tant que votre serveur fonctionne.

**Soutenir le réseau.** Chaque service sur I2P rend le réseau plus utile et aide à faire croître l'écosystème.

## Ce dont vous aurez besoin

Avant de commencer, assurez-vous d'avoir :

- **Un router I2P en fonctionnement** sur votre serveur (l'implémentation Java). Si vous n'en avez pas encore, suivez d'abord le [Guide d'installation I2P](/downloads/).
- **Votre site web ou service déjà fonctionnel** — il doit servir du contenu sur votre serveur.
- **Aisance de base avec la ligne de commande** — vous devrez modifier un fichier de configuration et exécuter quelques commandes.
- **Environ 15–20 minutes** — c'est tout ce qu'il faut.

Votre router I2P nécessite au moins 512 Mo de RAM et fonctionne de manière optimale sur un serveur avec une disponibilité 24h/24 et 7j/7. Si votre router vient de démarrer pour la première fois, laissez-lui 10 à 15 minutes pour s'intégrer au réseau avant de créer des tunnels.

## Comprendre les tunnels

Le concept fondamental derrière la mise en miroir I2P est le **tunnel serveur**. Voici l'idée :

Lorsque quelqu'un sur I2P souhaite visiter votre site, sa requête voyage à travers plusieurs sauts chiffrés sur le réseau I2P jusqu'à ce qu'elle atteigne votre router I2P. Votre router transmet ensuite la requête à un **server tunnel**, qui la transmet à votre serveur web fonctionnant sur localhost. Votre serveur web répond, et la réponse emprunte le chemin inverse à travers le réseau chiffré.

Votre serveur web ne touche jamais l'internet public pour ces requêtes — il ne communique qu'avec localhost. Le router I2P gère tout ce qui concerne le réseau.

### De quel type de tunnel avez-vous besoin ?

I2P offre plusieurs types de tunnels pour différentes situations :

![Comparaison des types de tunnels — Le serveur HTTP est le bon choix pour la plupart des sites web](/images/guides/mirroring/tunnel-types.svg)

Pour la mise en miroir d'un site web, vous voulez presque certainement un tunnel **Serveur HTTP**. Il est conçu spécifiquement pour le trafic web et gère le filtrage des en-têtes, la compression et l'usurpation de nom d'hôte prêts à l'emploi. Les autres types existent pour des cas d'usage spécialisés comme l'accès SSH, les applications bidirectionnelles ou les serveurs IRC.

## Partie 1 : Mise en miroir d'un site web

Il s'agit du scénario le plus courant — vous avez un site web clearnet existant et souhaitez le rendre disponible sur I2P. Voici le processus en un coup d'œil :

![Les cinq étapes pour mettre en miroir votre site sur I2P](/images/guides/mirroring/steps-overview.svg)

Parcourons chaque étape.

### Étape 1 : Ajouter un écouteur Localhost à votre serveur web

Votre site clearnet fonctionne probablement déjà sur les ports 80 et 443, ouvert au monde. Pour I2P, vous allez créer un listener *séparé* sur localhost que seul le tunnel I2P peut atteindre. Cela vous donne un contrôle total sur l'apparence de la version I2P — vous pouvez supprimer des en-têtes, bloquer les panneaux d'administration et ajuster la mise en cache pour la latence plus élevée d'I2P.

> **Alternative rapide :** Si vous n'avez besoin d'aucune personnalisation, vous pouvez ignorer cette étape et faire pointer le tunnel I2P directement vers `127.0.0.1:80`. Mais l'approche avec un écouteur dédié est recommandée.

Choisissez votre serveur web :

#### Nginx

Créer une nouvelle configuration de site :

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Collez cette configuration en remplaçant `yoursite.i2p` et le chemin racine par vos propres valeurs :

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
Activez-le et rechargez :

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Créer une nouvelle configuration de site :

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Collez cette configuration :

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
Puis ajoutez le port, activez le site, et rechargez :

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### Pourquoi pas de HSTS ?

Vous remarquerez que les deux configurations évitent explicitement les en-têtes `Strict-Transport-Security`. C'est essentiel. HSTS indique aux navigateurs d'utiliser uniquement HTTPS, mais I2P n'utilise pas le TLS traditionnel — le chiffrement est géré au niveau de la couche réseau à la place. Inclure HSTS bloquerait complètement l'accès des visiteurs à votre site I2P.

### Étape 2 : Créer le tunnel serveur

Ouvrez la console I2P Router dans votre navigateur :

```
http://127.0.0.1:7657/i2ptunnel/
```
Cliquez sur **"Tunnel Wizard"** pour commencer à créer un nouveau tunnel.

![Démarrage de l'assistant de tunnel I2P](/images/guides/mirroring/mirror_02.svg)

Sélectionnez **"HTTP Server"** comme type de tunnel et cliquez sur **Suivant**.

### Étape 3 : Configurer le Tunnel

Remplissez les paramètres du tunnel :

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
![Paramètres de configuration du tunnel](/images/guides/mirroring/mirror_03.png)

Cliquez sur **"Create"** pour générer votre tunnel. I2P créera une clé de destination cryptographique unique — celle-ci devient votre adresse permanente sur le réseau.

### Étape 4 : Démarrer le tunnel et attendre

Trouvez votre nouveau tunnel dans la liste et cliquez sur **"Start"**. Vous verrez :

- **Destination Locale** — une longue adresse base32 comme `abc123...xyz.b32.i2p`
- **Statut** — devrait passer à "En cours d'exécution"

![Statut de fonctionnement du tunnel](/images/guides/mirroring/mirror_04.png)

> **Soyez patient !** Le premier démarrage prend 2 à 5 minutes pendant que votre tunnel se construit et publie ses leaseSets sur le réseau. C'est normal.

### Étape 5 : Tester votre miroir

Une fois que le tunnel apparaît comme étant en cours d'exécution, ouvrez votre navigateur configuré pour I2P et visitez votre adresse base32. Le premier chargement de page peut prendre 5 à 30 secondes — c'est typique pour I2P.

Si la page se charge, félicitations — votre site est maintenant en ligne sur I2P !

### Étape 6 : Enregistrer une adresse .i2p lisible par l'homme (Optionnel)

Votre site est déjà accessible via l'adresse base32, mais `abc123...xyz.b32.i2p` n'est pas vraiment mémorisable. Pour obtenir un domaine `.i2p` propre :

**Pour votre propre carnet d'adresses** — allez sur `http://127.0.0.1:7657/dns` et ajoutez le nom d'hôte de votre choix associé à votre clé de destination.

**Pour la découverte publique** — enregistrez-vous auprès du registre d'adresses I2P :

1. Visitez `http://stats.i2p/i2p/addkey.html` (dans I2P)
2. Saisissez le nom d'hôte souhaité et votre clé de destination complète (la chaîne de plus de 500 caractères de vos détails de tunnel, se terminant par "AAAA")
3. Soumettez pour l'enregistrement

Une fois enregistré, toute personne ayant les abonnements au carnet d'adresses appropriés pourra trouver votre site par son nom.

## Partie 2 : Mise en miroir d'applications dynamiques

Si votre site fonctionne sur un framework backend (Node.js, Python, Ruby, PHP, etc.) au lieu de fichiers statiques, vous avez besoin de Nginx ou Apache comme proxy inverse entre le tunnel I2P et votre application.

### Configuration de Proxy Inverse (Nginx)

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
L'en-tête `X-I2P-Request` permet à votre application de détecter le trafic I2P si elle doit se comporter différemment (par exemple, désactiver les fonctionnalités qui nécessitent un accès au clearnet).

### Réécriture d'URL pour les miroirs Clearnet

Si votre application génère des URLs pointant vers votre domaine clearnet, vous voudrez les réécrire pour les visiteurs I2P :

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
Ensuite, créez un tunnel de serveur HTTP pointant vers `127.0.0.1:8080`, exactement comme dans la Partie 1.

## Partie 3 : Mise en miroir des dépôts Git

### Gitea (Fonctionnalités complètes)

Gitea est un excellent choix pour héberger Git sur I2P. Il dispose d'une interface web, d'un suivi des problèmes et de demandes de fusion — tout cela fonctionne bien sur le réseau.

Configurez `/etc/gitea/app.ini` :

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
Points clés : `OFFLINE_MODE = true` empêche Gitea de charger des ressources externes (avatars, assets CDN). `COOKIE_SECURE = false` est nécessaire car I2P n'utilise pas HTTPS au sens traditionnel. Désactivez l'email car votre serveur I2P pourrait ne pas avoir d'email sortant configuré.

Créer deux tunnels : 1. **tunnel Serveur HTTP** → `127.0.0.1:3000` (interface web) 2. **tunnel Serveur Standard** → `127.0.0.1:22` (accès SSH pour git push/pull — optionnel)

### cgit (Alternative légère)

Si vous avez seulement besoin d'une navigation en lecture seule et du clonage HTTP, cgit est beaucoup plus léger :

```ini
# /etc/cgitrc
virtual-root=/
clone-url=http://yourgit.i2p/$CGIT_REPO_URL
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
La mise en cache agressive de cgit le rend particulièrement bien adapté à la latence plus élevée d'I2P.

### Configuration côté client pour Git sur I2P

Toute personne clonant depuis votre miroir Git I2P doit router le trafic Git à travers le proxy HTTP I2P :

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy http://127.0.0.1:4444
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone http://yourgit.i2p/repo
```
Pour les gros dépôts, les clones superficiels permettent d'économiser beaucoup de temps sur I2P :

```bash
git clone --depth 1 http://yourgit.i2p/project
git fetch --unshallow   # grab full history later if needed
```
## Partie 4 : Hébergement de fichiers en miroir

### Nextcloud

Nextcloud fonctionne sur I2P avec quelques configurations. Modifiez `config/config.php` :

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
Ce qui fonctionne bien : téléchargement et téléversement de fichiers, navigation dans les répertoires, authentification, partage de liens publics, et WebDAV. Ce qui ne fonctionne pas : les clients de synchronisation desktop nécessitent une configuration de proxy SOCKS, les backends de stockage externe peuvent divulguer les adresses IP, et la fédération avec les instances Nextcloud du clearnet peut compromettre la confidentialité.

### Serveur de fichiers simple

Pour un hébergement de fichiers simple sans la complexité de Nextcloud, un serveur Python minimal fait l'affaire :

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
Créez un tunnel serveur HTTP pointant vers `127.0.0.1:8080`.

## Partie 5 : APIs de miroir

### Proxy API de base

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
### Support WebSocket

Si votre application utilise WebSockets (applications de chat, tableaux de bord en temps réel, etc.) :

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
Notez que les WebSockets sur I2P auront une latence sensiblement plus élevée que sur le clearnet. Pour les fonctionnalités en temps réel, envisagez des intervalles de polling plus longs ou des mises à jour optimistes de l'interface utilisateur côté client.

## Meilleures pratiques de sécurité

Faire fonctionner votre miroir est la partie facile. Le maintenir sécurisé nécessite de prêter attention à quelques détails qui sont spécifiques à l'hébergement I2P.

![Liste de vérification de sécurité pour les miroirs I2P](/images/guides/mirroring/security-checklist.svg)

### Les Règles Principales

**Lier uniquement à localhost.** Votre service doit écouter sur `127.0.0.1`, jamais sur `0.0.0.0`. Le router I2P est la seule chose qui devrait pouvoir atteindre votre service.

**Supprimer les en-têtes d'identification.** Les serveurs web adorent annoncer quel logiciel ils utilisent. Sur I2P, c'est une information que vous ne voulez pas partager.

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
**Auto-hébergez tout.** Ne chargez pas de polices depuis Google, de scripts depuis des CDN, ou d'analytiques depuis des tiers. Chaque ressource externe est une requête qui sort du réseau I2P, ajoutant une latence énorme et potentiellement divulguant des informations. Téléchargez les bibliothèques et polices, placez-les sur votre serveur, et servez-les localement.

**N'exposez jamais les bases de données.** Cela devrait aller de soi, mais ne créez pas de tunnels I2P vers vos ports de base de données. Les tunnels serveur ne doivent pointer que vers des serveurs web ou des serveurs d'applications.

## Optimisation des Performances

I2P ajoute 2 à 10 secondes de latence par requête. C'est le prix du chiffrement multi-saut. Mais avec un réglage approprié, votre miroir I2P peut sembler étonnamment réactif.

### Mise en cache agressive

Les ressources statiques devraient avoir une durée de vie de cache longue. Si un visiteur a déjà chargé votre CSS et vos images, il ne devrait pas avoir à attendre qu'ils se rechargent :

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Activer la compression

Des charges utiles plus petites signifient des transferts plus rapides sur la bande passante limitée d'I2P :

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Ajuster la Quantité de Tunnels pour le Trafic

Plus de tunnels signifie plus de connexions simultanées. La valeur par défaut de 3 convient pour les sites à faible trafic, mais si vous constatez de la congestion :

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Longueur du tunnel (sauts)

Chaque saut ajoute de la latence mais aussi de l'anonymat. Choisissez en fonction de votre modèle de menace :

![Compromis des sauts de tunnel — plus de sauts signifie plus de confidentialité mais une latence plus élevée](/images/guides/mirroring/tunnel-hops.svg)

Pour un miroir public où l'identité du serveur est déjà connue (le site web de votre organisation, par exemple), réduire à 2 sauts est un compromis raisonnable :

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Conseils généraux pour le routeur

- Faites fonctionner votre router I2P **24h/24 et 7j/7**. Plus il reste en ligne longtemps, mieux il s'intègre au réseau, et plus vos tunnels sont performants.
- Configurez le partage de bande passante à au moins **256 KB/sec**, mais gardez-le légèrement en dessous de votre vitesse réelle de ligne.
- Attendez-vous à ce que les premières connexions après un redémarrage soient lentes (30–90 secondes). Cela s'améliore rapidement au fur et à mesure que les tunnels se construisent.

## Avancé : Configuration manuelle des tunnels

L'assistant de la Console du Router fonctionne très bien, mais si vous préférez éditer directement les fichiers de configuration — ou si vous devez automatiser les déploiements — vous pouvez configurer les tunnels dans `~/.i2p/i2ptunnel.config` (ou `/var/lib/i2p/i2p-config/i2ptunnel.config` pour les installations système) :

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
Redémarrez I2P après les modifications :

```bash
sudo systemctl restart i2p
```
À partir d'I2P 0.9.42, vous pouvez également utiliser des fichiers de configuration individuels dans `i2ptunnel.config.d/` pour une gestion plus claire de plusieurs tunnels :

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
## Dépannage

### "Je n'arrive pas à accéder à mon site"

Suivez cette liste de contrôle dans l'ordre :

**1. Le serveur web écoute-t-il vraiment ?**

```bash
nc -zv 127.0.0.1 8080
```
Si cela échoue, la configuration de votre serveur web a un problème — retournez à l'Étape 1.

**2. Le tunnel fonctionne-t-il ?** Visitez `http://127.0.0.1:7657/i2ptunnel/` et vérifiez l'état. S'il indique "Démarrage" pendant plus de 5 minutes, vérifiez l'intégration réseau de votre router.

**3. Le LeaseSet est-il publié ?** Assurez-vous que `i2cp.dontPublishLeaseSet` n'est PAS défini dans les options de votre tunnel. Sans un LeaseSet publié, personne ne peut trouver votre tunnel.

**4. Votre horloge est-elle précise ?** I2P nécessite une précision temporelle à 60 secondes près. Vérifiez avec :

```bash
timedatectl status
```
Si votre horloge n'est pas à l'heure, I2P aura des difficultés à construire des tunnels.

### Performance lente après redémarrage

C'est normal. Après avoir redémarré votre router I2P, laissez-lui 10 à 15 minutes pour reconstruire ses pools de tunnel et se réintégrer au réseau. Les performances s'améliorent à mesure que davantage de pairs découvrent votre router.

Vérifiez également que la redirection de port est configurée pour votre port I2NP (consultez la Console du Routeur pour le numéro de port spécifique). Sans cela, votre router fonctionne en mode "pare-feu", ce qui limite les performances.

### Erreurs "Adresse introuvable" lors des visites d'autres utilisateurs

Les visiteurs ont besoin de votre adresse dans leur carnet d'adresses. Assurez-vous de vous être enregistré auprès d'un carnet d'adresses public, ou partagez directement votre adresse base32 complète. Ils peuvent également ajouter plus d'abonnements à l'adresse `http://127.0.0.1:7657/susidns/subscriptions` :

```
http://stats.i2p/cgi-bin/newhosts.txt
http://i2host.i2p/cgi-bin/i2hostetag
```
### Délais d'expiration lors des tests

I2P a intrinsèquement des temps de réponse plus élevés. Lors de tests en ligne de commande, utilisez des délais d'attente étendus :

```bash
# curl
curl --connect-timeout 60 --max-time 300 http://yoursite.i2p/

# wget
wget --timeout=300 http://yoursite.i2p/
```
### Lecture des journaux

Si rien d'autre n'aide, vérifiez les journaux du router I2P pour les erreurs :

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Sauvegardez vos clés

C'est la seule chose que vous ne devez absolument pas négliger. Les fichiers de clés privées de votre tunnel (fichiers `.dat` dans votre répertoire de configuration I2P) sont ce qui donne à votre service son adresse permanente sur le réseau. Si vous les perdez, vous perdez votre adresse I2P — définitivement. Il n'y a pas de récupération, pas de réinitialisation, pas de ticket de support. Vous devriez recommencer avec une nouvelle adresse.

Sauvegardez-les maintenant :

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Stockez la sauvegarde dans un endroit sûr et hors serveur.

## C'est terminé

C'est tout. Votre service est maintenant disponible à la fois sur l'internet classique et sur le réseau I2P. Vous offrez aux utilisateurs un moyen privé d'accéder à votre contenu — un moyen où leur identité leur appartient.

Si vous rencontrez des problèmes ou souhaitez vous impliquer davantage, voici où trouver la communauté :

- **Forum :** [i2pforum.net](https://i2pforum.net)
- **IRC :** #i2p sur divers réseaux
- **Développement :** [i2pgit.org](https://i2pgit.org)
- **StormyCloud :** [stormycloud.org](https://www.stormycloud.org)

---

*Guide créé par [StormyCloud Inc](https://www.stormycloud.org) pour la communauté I2P.*

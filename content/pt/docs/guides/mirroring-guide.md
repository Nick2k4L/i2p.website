---
title: "Espelhando Seus Serviços no I2P"
description: "Um guia amigável para iniciantes sobre como tornar seus websites, repositórios Git, APIs e muito mais disponíveis na rede I2P — com instruções passo a passo e diagramas"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

Você tem um site na internet normal. Agora quer torná-lo disponível no I2P também — para que as pessoas possam visitá-lo de forma privada, sem revelar quem são ou de onde estão vindo. É sobre isso que este guia trata.

O espelhamento não substitui seu site existente. Ele adiciona uma segunda entrada — uma entrada privada — através da rede I2P. Seu site clearnet continua funcionando exatamente como antes.

![Como funciona o espelhamento I2P — seu servidor obtém uma segunda entrada privada através da rede I2P](/images/guides/mirroring/how-mirroring-works.svg)

## Por que Espelhar no I2P?

Existem várias razões práticas para espelhar seus serviços:

**Privacidade para seus visitantes.** As pessoas podem acessar seu conteúdo sem expor seu endereço IP. O tráfego entre elas e seu serviço é criptografado através de múltiplos saltos — nem você nem qualquer pessoa monitorando a rede pode identificar quem está visitando.

**Resistência à censura.** Se o seu site estiver bloqueado em certas regiões por filtragem de DNS, bloqueio de IP ou outros meios, o espelho I2P permanece acessível. Ele não depende de DNS ou roteamento IP convencional.

**Resiliência.** Um espelho I2P adiciona redundância. Se o seu domínio for apreendido ou sua CDN te abandonar, a versão I2P permanece ativa enquanto seu servidor estiver funcionando.

**Apoiando a rede.** Cada serviço no I2P torna a rede mais útil e ajuda a crescer o ecossistema.

## O Que Você Precisará

Antes de começar, certifique-se de que você tem:

- **Um router I2P em execução** no seu servidor (a implementação Java). Se você ainda não tem um, siga primeiro o [Guia de Instalação do I2P](/downloads/).
- **Seu website ou serviço já funcionando** — ele deve estar servindo conteúdo no seu servidor.
- **Conhecimento básico de linha de comando** — você editará um arquivo de configuração e executará alguns comandos.
- **Cerca de 15–20 minutos** — é só isso que você precisa.

Seu router I2P precisa de pelo menos 512 MB de RAM e funciona melhor em um servidor com disponibilidade 24/7. Se seu router acabou de ser iniciado pela primeira vez, aguarde 10–15 minutos para que ele se integre à rede antes de criar tunnels.

## Entendendo Tunnels

O conceito central por trás do espelhamento I2P é o **server tunnel**. Aqui está a ideia:

Quando alguém no I2P quer visitar o seu site, a solicitação viaja através de vários saltos criptografados pela rede I2P até chegar ao seu router I2P. O seu router então entrega a solicitação para um **server tunnel**, que a encaminha para o seu servidor web rodando no localhost. Seu servidor web responde, e a resposta toma o caminho reverso de volta através da rede criptografada.

Seu servidor web nunca toca a internet pública para essas solicitações — ele apenas se comunica com localhost. O I2P router cuida de tudo que é voltado para a rede.

### Que Tipo de Tunnel Você Precisa?

O I2P oferece vários tipos de tunnel para diferentes situações:

![Comparação de tipos de tunnel — HTTP Server é a escolha certa para a maioria dos sites](/images/guides/mirroring/tunnel-types.svg)

Para espelhar um website, você quase certamente quer um túnel **HTTP Server**. Ele foi projetado especificamente para tráfego web e lida com filtragem de cabeçalhos, compressão e spoofing de hostname de forma nativa. Os outros tipos existem para casos de uso especializados como acesso SSH, aplicações bidirecionais ou servidores IRC.

## Parte 1: Espelhando um Site

Este é o cenário mais comum — você tem um website clearnet existente e quer disponibilizá-lo no I2P. Aqui está o processo resumidamente:

![Os cinco passos para espelhar seu site no I2P](/images/guides/mirroring/steps-overview.svg)

Vamos percorrer cada etapa.

### Passo 1: Adicionar um Listener Localhost ao Seu Servidor Web

Seu site clearnet provavelmente já está rodando nas portas 80 e 443, aberto ao mundo. Para I2P, você criará um listener *separado* no localhost que apenas o tunnel I2P pode alcançar. Isso lhe dá controle total sobre como a versão I2P se parece — você pode remover headers, bloquear painéis de admin e ajustar o cache para a maior latência do I2P.

> **Alternativa rápida:** Se você não precisar de nenhuma personalização, pode pular esta etapa e apontar o tunnel I2P diretamente para `127.0.0.1:80`. Mas a abordagem de listener dedicado é recomendada.

Escolha o seu servidor web:

#### Nginx

Criar uma nova configuração de site:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Cole esta configuração, substituindo `yoursite.i2p` e o caminho raiz pelos seus próprios valores:

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
Ative-o e recarregue:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Crie uma nova configuração de site:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Cole esta configuração:

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
Em seguida, adicione a porta, habilite o site e recarregue:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### Por Que Não HSTS?

Você notará que ambas as configurações explicitamente evitam cabeçalhos `Strict-Transport-Security`. Isso é crítico. O HSTS instrui navegadores a usar apenas HTTPS, mas o I2P não usa TLS tradicional — a criptografia é tratada na camada de rede. Incluir HSTS bloquearia completamente os visitantes do seu eepsite I2P.

### Passo 2: Criar o Túnel do Servidor

Abra o Console do Router I2P no seu navegador:

```
`http://127.0.0.1:7657/i2ptunnel/`
```
Clique em **"Tunnel Wizard"** para começar a criar um novo tunnel.

![Inicialização do Assistente de Tunnel I2P](/images/guides/mirroring/mirror_02.svg)

Selecione **"HTTP Server"** como tipo de túnel e clique em **Avançar**.

### Passo 3: Configurar o Tunnel

Preencha as configurações do tunnel:

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
![Configurações do tunnel](/images/guides/mirroring/mirror_03.png)

Clique em **"Create"** para gerar seu tunnel. O I2P criará uma chave de destino criptográfica única — esta se torna seu endereço permanente na rede.

### Passo 4: Iniciar o Tunnel e Aguardar

Encontre seu novo tunnel na lista e clique em **"Start"**. Você verá:

- **Destino Local** — um endereço base32 longo como `abc123...xyz.b32.i2p`
- **Status** — deve mudar para "Em execução"

![Tunnel running status](/images/guides/mirroring/mirror_04.png)

> **Seja paciente!** A primeira inicialização leva de 2 a 5 minutos enquanto seu túnel é construído e publica seus leaseSets na rede. Isso é normal.

### Passo 5: Teste Seu Espelho

Assim que o tunnel aparecer como em execução, abra seu navegador configurado para I2P e visite seu endereço base32. O primeiro carregamento da página pode demorar de 5 a 30 segundos — isso é típico do I2P.

Se a página carregar, parabéns — seu site agora está funcionando no I2P!

### Passo 6: Registrar um Endereço .i2p Legível para Humanos (Opcional)

Seu site já está acessível através do endereço base32, mas `abc123...xyz.b32.i2p` não é exatamente memorável. Para obter um domínio `.i2p` limpo:

**Para seu próprio catálogo de endereços** — vá para `http://127.0.0.1:7657/dns` e adicione o nome de host escolhido mapeado para sua chave de destino.

**Para descoberta pública** — registre-se no registro de endereços I2P:

1. Visite `http://stats.i2p/i2p/addkey.html` (dentro do I2P)
2. Insira o nome de host desejado e sua chave de destino completa (a string de 500+ caracteres dos detalhes do seu tunnel, terminando em "AAAA")
3. Envie para registro

Uma vez registrado, qualquer pessoa com as subscrições de livro de endereços apropriadas será capaz de encontrar seu site pelo nome.

## Parte 2: Espelhamento de Aplicações Dinâmicas

Se o seu site funciona com um framework de backend (Node.js, Python, Ruby, PHP, etc.) em vez de arquivos estáticos, você precisa do Nginx ou Apache como um proxy reverso entre o tunnel I2P e sua aplicação.

### Configuração de Proxy Reverso (Nginx)

```nginx
server {
    listen 127.0.0.1:8080;
    server_name yourapp.i2p;

    server_tokens off;

    location / {
        proxy_pass `http://127.0.0.1:3000;`
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
O cabeçalho `X-I2P-Request` permite que sua aplicação detecte tráfego I2P caso precise se comportar de forma diferente (por exemplo, desabilitando recursos que requerem acesso à clearnet).

### Reescrita de URL para Mirrors da Clearnet

Se sua aplicação gerar URLs apontando para seu domínio clearnet, você precisará reescrevê-las para visitantes I2P:

```nginx
location / {
    proxy_pass `http://127.0.0.1:3000;`

    sub_filter_once off;
    sub_filter_types text/html text/css application/javascript;

    # Rewrite your clearnet domain to the I2P domain
    sub_filter 'https://www.example.com' 'http://yoursite.i2p';
    sub_filter '//www.example.com' '//yoursite.i2p';
}
```
Em seguida, crie um túnel de Servidor HTTP apontando para `127.0.0.1:8080`, assim como na Parte 1.

## Parte 3: Espelhamento de Repositórios Git

### Gitea (Com Todos os Recursos)

Gitea é uma excelente escolha para hospedar Git sobre I2P. Tem uma interface web, rastreamento de problemas e pull requests — tudo funciona bem na rede.

Configure `/etc/gitea/app.ini`:

```ini
[server]
HTTP_ADDR     = 127.0.0.1
HTTP_PORT     = 3000
DOMAIN        = yourgit.i2p
ROOT_URL      = `http://yourgit.i2p/`
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
Pontos-chave: `OFFLINE_MODE = true` impede que o Gitea carregue recursos externos (avatares, assets de CDN). `COOKIE_SECURE = false` é necessário porque o I2P não usa HTTPS no sentido tradicional. Desabilite o email já que seu servidor I2P pode não ter email de saída configurado.

Crie dois tunnels: 1. **tunnel de Servidor HTTP** → `127.0.0.1:3000` (interface web) 2. **tunnel de Servidor Padrão** → `127.0.0.1:22` (acesso SSH para git push/pull — opcional)

### cgit (Alternativa Leve)

Se você precisa apenas de navegação somente leitura e clonagem HTTP, o cgit é muito mais leve:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=`http://yourgit.i2p/$CGIT_REPO_URL`
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
O cache agressivo do cgit o torna particularmente adequado para a alta latência do I2P.

### Configuração do Lado do Cliente para Git sobre I2P

Qualquer pessoa clonando do seu espelho Git I2P precisa rotear o tráfego Git através do proxy HTTP I2P:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy `http://127.0.0.1:4444`
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone `http://yourgit.i2p/repo`
```
Para repositórios grandes, clones superficiais economizam muito tempo através do I2P:

```bash
git clone --depth 1 `http://yourgit.i2p/project`
git fetch --unshallow   # grab full history later if needed
```
## Parte 4: Espelhamento de Hospedagem de Arquivos

### Nextcloud

O Nextcloud funciona através do I2P com algumas configurações. Edite `config/config.php`:

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
    'overwrite.cli.url' => '`http://yoursite.i2p/',`
);
```
O que funciona bem: upload e download de arquivos, navegação de diretórios, autenticação, compartilhamento de links públicos e WebDAV. O que não funciona: clientes de sincronização desktop precisam de configuração de proxy SOCKS, backends de armazenamento externo podem vazar endereços IP, e federação com instâncias Nextcloud da clearnet pode comprometer a privacidade.

### Servidor de Arquivos Simples

Para hospedagem simples de arquivos sem a sobrecarga do Nextcloud, um servidor Python mínimo resolve a questão:

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
Crie um túnel de servidor HTTP apontando para `127.0.0.1:8080`.

## Parte 5: APIs de Espelhamento

### Proxy de API Básico

```nginx
server {
    listen 127.0.0.1:8080;
    server_name api.yoursite.i2p;

    server_tokens off;

    location / {
        proxy_pass `http://127.0.0.1:3000;`

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
### Suporte WebSocket

Se sua aplicação usa WebSockets (aplicativos de chat, painéis em tempo real, etc.):

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}

server {
    listen 127.0.0.1:8080;

    location /ws {
        proxy_pass `http://127.0.0.1:3000;`
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
Note que WebSockets sobre I2P terão latência notavelmente mais alta que a clearnet. Para recursos em tempo real, considere intervalos de polling mais longos ou atualizações otimistas da UI no lado do cliente.

## Melhores Práticas de Segurança

Fazer seu mirror funcionar é a parte fácil. Mantê-lo seguro requer atenção a alguns detalhes únicos da hospedagem I2P.

![Lista de verificação de segurança para mirrors I2P](/images/guides/mirroring/security-checklist.svg)

### As Grandes Regras

**Vincule apenas ao localhost.** Seu serviço deve escutar em `127.0.0.1`, nunca em `0.0.0.0`. O router I2P é a única coisa que deve conseguir alcançar seu serviço.

**Remover cabeçalhos identificadores.** Servidores web adoram anunciar qual software estão executando. Sobre I2P, esta é uma informação que você não quer compartilhar.

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
**Hospede tudo você mesmo.** Não carregue fontes do Google, scripts de CDNs ou análises de terceiros. Todo recurso externo é uma solicitação que sai da rede I2P, adicionando latência enorme e potencialmente vazando informações. Baixe bibliotecas e fontes, coloque-as no seu servidor e sirva-as localmente.

**Nunca exponha bases de dados.** Deveria ser óbvio, mas não crie tunnels I2P para as portas da sua base de dados. Os tunnels de servidor devem apenas apontar para servidores web ou servidores de aplicação.

## Ajuste de Performance

O I2P adiciona 2–10 segundos de latência por solicitação. Esse é o preço da criptografia multi-hop. Mas com o ajuste adequado, seu mirror I2P pode parecer surpreendentemente ágil.

### Cache de Forma Agressiva

Recursos estáticos devem ter tempos de vida de cache longos. Se um visitante já carregou seu CSS e imagens, ele não deveria ter que esperar por eles novamente:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Ativar Compressão

Payloads menores significam transferências mais rápidas sobre a largura de banda limitada do I2P:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Ajustar Quantidade de Tunnel para Tráfego

Mais tunnels significam mais conexões simultâneas. O padrão de 3 é adequado para sites de baixo tráfego, mas se você estiver vendo congestionamento:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Comprimento do Tunnel (Saltos)

Cada hop adiciona latência, mas também adiciona anonimato. Escolha com base no seu modelo de ameaças:

![Compensação de saltos de tunnel — mais saltos significa mais privacidade, mas maior latência](/images/guides/mirroring/tunnel-hops.svg)

Para um espelho público onde a identidade do servidor já é conhecida (o website da sua organização, por exemplo), reduzir para 2 saltos é uma troca razoável:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Dicas Gerais do Router

- Execute o seu router I2P **24/7**. Quanto mais tempo estiver ativo, melhor integrado estará com a rede, e mais rápidos serão os seus tunnels.
- Defina o compartilhamento de largura de banda para pelo menos **256 KB/seg**, mas mantenha ligeiramente abaixo da sua velocidade real de linha.
- Espere que as primeiras conexões após um reinício sejam lentas (30–90 segundos). Isso melhora rapidamente conforme os tunnels são construídos.

## Avançado: Configuração Manual de Tunnel

O assistente do Console do Router funciona muito bem, mas se você preferir editar arquivos de configuração diretamente — ou precisar automatizar implementações — você pode configurar tunnels em `~/.i2p/i2ptunnel.config` (ou `/var/lib/i2p/i2p-config/i2ptunnel.config` para instalações do sistema):

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
Reinicie o I2P após as alterações:

```bash
sudo systemctl restart i2p
```
A partir do I2P 0.9.42, você também pode usar arquivos de configuração individuais em `i2ptunnel.config.d/` para um gerenciamento mais limpo de múltiplos tunnels:

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
## Resolução de Problemas

### "Não consigo acessar meu site"

Trabalhe nesta lista de verificação em ordem:

**1. O servidor web está realmente ouvindo?**

```bash
nc -zv 127.0.0.1 8080
```
Se isso falhar, a configuração do seu servidor web tem um problema — volte para o Passo 1.

**2. O tunnel está funcionando?** Visite `http://127.0.0.1:7657/i2ptunnel/` e verifique o status. Se mostrar "Starting" por mais de 5 minutos, verifique a integração de rede do seu router.

**3. O LeaseSet está publicado?** Certifique-se de que `i2cp.dontPublishLeaseSet` NÃO esteja definido nas opções do seu túnel. Sem um LeaseSet publicado, ninguém pode encontrar o seu túnel.

**4. O seu relógio está preciso?** O I2P requer precisão de tempo dentro de 60 segundos. Verifique com:

```bash
timedatectl status
```
Se o seu relógio estiver desajustado, o I2P terá problemas para construir tunnels.

### Desempenho lento após reinicialização

Isso é normal. Após reiniciar seu I2P router, aguarde 10–15 minutos para que ele reconstrua seus tunnel pools e se reintegre à rede. O desempenho melhora conforme mais peers ficam cientes do seu router.

Verifique também se o encaminhamento de porta está configurado para sua porta I2NP (consulte o Router Console para o número específico da porta). Sem isso, seu router opera em modo "firewalled", o que limita o desempenho.

### Erros "Address not found" quando outros visitam

Os visitantes precisam do seu endereço no livro de endereços deles. Certifique-se de que você se registrou em um livro de endereços público, ou compartilhe seu endereço base32 completo diretamente. Eles também podem adicionar mais subscrições em `http://127.0.0.1:7657/susidns/subscriptions`:

```
`http://stats.i2p/cgi-bin/newhosts.txt`
`http://i2host.i2p/cgi-bin/i2hostetag`
```
### Timeouts ao testar

O I2P tem inerentemente tempos de ida e volta mais altos. Ao testar a partir da linha de comando, use timeouts estendidos:

```bash
# curl
curl --connect-timeout 60 --max-time 300 `http://yoursite.i2p/`

# wget
wget --timeout=300 `http://yoursite.i2p/`
```
### Lendo os logs

Se nada mais ajudar, verifique os logs do router I2P em busca de erros:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Faça Backup das Suas Chaves

Esta é a única coisa que você absolutamente não deve pular. Os arquivos de chave privada do seu tunnel (arquivos `.dat` no seu diretório de configuração do I2P) são o que dão ao seu serviço seu endereço permanente na rede. Se você perdê-los, você perde seu endereço I2P — permanentemente. Não há recuperação, não há reset, não há ticket de suporte. Você teria que começar do zero com um novo endereço.

Faça backup deles agora:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Armazene o backup em um local seguro e fora do servidor.

## Pronto

É isso. Seu serviço agora está disponível tanto na internet regular quanto na rede I2P. Você está oferecendo às pessoas uma forma privada de acessar seu conteúdo — uma onde a identidade delas permanece própria.

Se você encontrar problemas ou quiser se envolver mais, aqui é onde encontrar a comunidade:

- **Fórum:** [i2pforum.net](https://i2pforum.net)
- **IRC:** #i2p em várias redes
- **Desenvolvimento:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*Guia criado pela [StormyCloud Inc](https://www.stormycloud.org) para a comunidade I2P.*

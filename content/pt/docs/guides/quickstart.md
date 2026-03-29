---
title: "Introdução ao I2P: um guia completo para iniciantes"
description: "Introdução ao I2P: um guia completo para iniciantes"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**O I2P é uma rede anônima par-a-par totalmente criptografada que opera "dentro" da internet**, e a implementação em Java do i2p.net continua sendo a forma principal de utilizá-la. Diferentemente do Tor, que basicamente anonimiza o acesso à web convencional, o I2P cria uma rede completamente autônoma composta por serviços ocultos, sites, e-mail, bate-papo e compartilhamento de arquivos.

---

## O que acontece no momento em que você inicia o I2P

Após a instalação, o I2P inicia uma aplicação web local chamada **console do roteador** em `http://127.0.0.1:7657`. Este é o seu centro de controle, que funciona inteiramente na sua máquina e está vinculado ao localhost por segurança. Na primeira execução, um **assistente de configuração** orienta você pela seleção de idioma, escolha de tema (escuro ou claro) e um teste automatizado de largura de banda que leva aproximadamente um minuto, utilizando o serviço externo de medição M-Lab. Em seguida, você define qual porcentagem da sua largura de banda compartilhará com a rede.

![Assistente de Configuração do I2P - Seleção de Idioma](/images/guides/quickstart/wizard-language-selection.webp)

Uma vez que o assistente é concluído, o roteador inicia o processo de **inicialização** chamado "atualização inicial" ("reseeding"). Seu roteador baixa cerca de **100 registros RouterInfo** de servidores de atualização inicial pré-configurados via HTTPS, obtendo assim uma lista inicial de pares. A partir daí, começa a criar **túneis exploratórios** para descobrir mais pares e preencher sua cópia local do banco de dados da rede (o "netDb"). Você verá uma mensagem "Rejeitando túneis: inicializando" durante esses primeiros minutos. Isso é normal.

![Reseeding do I2P - Inicialização](/images/guides/quickstart/reseed-bootstrapping.webp)

**Espere esperar de 3 a 10 minutos** antes que seu roteador fique utilizável, e um tempo significativamente maior — dias de tempo de atividade contínuo — antes de atingir o desempenho máximo. A barra lateral do console do roteador mostra sua contagem de pares como "Ativos x/y", onde x são os pares com os quais você trocou mensagens recentemente e y é o total de pares vistos. Quando você vir **10 ou mais pares ativos**, seu roteador estará conectado de forma saudável. A coisa mais importante que um novo usuário pode fazer é **deixar o roteador em execução continuamente**. Após uma desativação, outros nós marcam seu roteador como não confiável por pelo menos 24 horas, portanto reinícios frequentes prejudicam severamente o desempenho.

![Painel da Console do Roteador I2P](/images/guides/quickstart/router-console-dashboard.png)

---

## Configurando seu navegador para o I2P

Diferentemente da rede Tor, o I2P não vem com um navegador dedicado. Para acessar sites do I2P (o domínio pseudo-nível superior `.i2p`), você precisa configurar as configurações de proxy do seu navegador para rotear o tráfego através do proxy HTTP do I2P na porta **4444**.

**O caminho mais fácil para usuários do Windows** é o **Pacote de Instalação Fácil**, que inclui o Java, o roteador e um perfil pré-configurado do Firefox com a extensão "I2P in Private Browsing". Ele elimina toda configuração manual de proxy. Do download à navegação em eepsites, o processo leva aproximadamente quatro minutos. Um pacote de instalação fácil para macOS (Apple Silicon) também está disponível em versão beta. Se você estiver usando o Pacote de Instalação Fácil, pode pular a configuração manual abaixo.

### Firefox (Recomendado)

Recomenda-se fortemente o Firefox, pois ele possui suas próprias configurações de proxy independentes do sistema operacional - o Chrome e o Edge usam configurações de proxy globais que afetam todos os aplicativos.

**Passo 1.** Abra o menu do Firefox (ícone de hambúrguer) e clique em **Configurações**.

![Firefox - Abrir Configurações](/images/guides/browser-config/accessi2p_3.png)

**Passo 2.** Procure por **proxy** na barra de pesquisa das configurações, depois clique em **Configurações...** ao lado de Configurações de Rede.

![Firefox - Pesquisar por proxy](/images/guides/browser-config/accessi2p_4.png)

**Passo 3.** Selecione **Configuração manual de proxy**, digite `127.0.0.1` para o Proxy HTTP e `4444` para a porta, então clique em **OK**.

![Firefox - Configuração manual de proxy](/images/guides/browser-config/accessi2p_5.png)

Após configurar o proxy, várias alterações em `about:config` são recomendadas:

- Defina `media.peerConnection.ice.proxy_only` como **true** (impede vazamentos WebRTC)
- Defina `keyword.enabled` como **false** (impede redirecionamentos para mecanismos de busca em endereços .i2p)
- Crie um valor booleano `browser.fixup.domainsuffixwhitelist.i2p` definido como **true** (informa ao Firefox que `.i2p` é um sufixo de domínio válido)

Uma armadilha comum para iniciantes: sempre digite `http://` antes dos endereços `.i2p`. A maioria dos sites I2P não usa HTTPS (o I2P já criptografa todo o tráfego de ponta a ponta), e sem o prefixo o Firefox irá redirecioná-lo para um mecanismo de busca.

### Chrome / Edge (Windows)

Observação: o Chrome e o Edge usam as configurações de proxy do seu sistema operacional, o que afeta **todas** as aplicações do seu sistema.

**Etapa 1.** Abra o menu do Chrome e clique em **Configurações**.

![Chrome - Abrir Configurações](/images/guides/browser-config/accessi2p_6.png)

**Passo 2.** Procure por **proxy**, então clique em **Abrir as configurações de proxy do seu computador**.

![Chrome - Pesquisar por proxy](/images/guides/browser-config/accessi2p_7.png)

**Etapa 3.** Em **Configuração de proxy manual**, clique em **Configurar** ao lado de "Usar um servidor proxy."

![Windows - Configurações de proxy](/images/guides/browser-config/accessi2p_8.png)

**Passo 4.** Alterne **Usar um servidor proxy** para Ligado, insira `127.0.0.1` para o endereço IP do proxy e `4444` para a porta, então clique em **Salvar**.

![Windows - Editar servidor proxy](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**Passo 1.** Acesse **Safari → Configurações → Avançado** e clique em **Alterar Configurações...** ao lado de Proxies.

![Safari - Configurações avançadas](/images/guides/browser-config/accessi2p_1.png)

**Etapa 2.** Habilite o **Proxy da Web (HTTP)**, insira `127.0.0.1` para o servidor e `4444` para a porta, então clique em **OK**.

![macOS - Configurações de proxy da web](/images/guides/browser-config/accessi2p_2.png)

---

## Entendendo o painel do console do roteador

O console do roteador em `127.0.0.1:7657` exibe vários indicadores principais que mostram o desempenho do seu nó. A **barra lateral** mostra a versão do I2P, tempo de atividade, uso de largura de banda (entrada/saída), contagem de pares ativos e status dos túneis. Quando "Clientes Compartilhados" ficar verde, seu roteador estará integrado e pronto.

![Console do Roteador - Clientes Compartilhados Verdes](/images/guides/quickstart/shared-clients-green.png)

Os **gráficos de largura de banda** mostram a taxa de transferência em tempo real. Os valores padrão são conservadores – **96 KBps de download e 40 KBps de upload**, com apenas 48 KBps compartilhados – e a documentação oficial recomenda fortemente aumentá-los. Acesse `http://127.0.0.1:7657/config` (ou clique em "Configurar Largura de Banda" no console) para aumentar seus limites. Uma largura de banda compartilhada mais alta melhora tanto o seu próprio desempenho quanto a saúde da rede. Definir a largura de banda compartilhada abaixo de **12 KBps** coloca efetivamente seu roteador no "modo oculto", impedindo-o de participar do tráfego da rede. A partir de **128 KBps ou mais**, seu roteador pode ser promovido ao status de floodfill, o que significa que ele ajuda a manter a tabela de hash distribuída.

![Configuração de Largura de Banda](/images/guides/quickstart/bandwidth-config.png)

A seção **status do túnel** mostra os túneis participantes – tráfego que você está repassando para outros. Mais de 90% dos roteadores I2P retransmitem tráfego participante por padrão. Isso serve simultaneamente como tráfego de cobertura para sua própria anonimidade e como sua contribuição para a rede. Os túneis expiram a cada 10 minutos e são reconstruídos automaticamente.

![Gerenciador do I2PTunnel](/images/guides/quickstart/tunnel-manager.png)

O gerenciador do **I2PTunnel** em `http://127.0.0.1:7657/i2ptunnel/` mostra todos os seus túneis configurados — o proxy HTTP, IRC, e-mail e o túnel do servidor eepsite são todos pré-configurados diretamente da caixa.

![Lista do I2PTunnel](/images/guides/quickstart/i2ptunnel-list.png)

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

## Cinco coisas que você pode fazer assim que estiver conectado

### Navegar por sites .i2p

O uso mais imediato do I2P é navegar em sites ocultos. Com seu navegador configurado para usar o proxy na porta 4444, acesse qualquer endereço `.i2p`. Vários sites conhecidos servem como bons pontos de partida: **`i2p-projekt.i2p`** é o site oficial do projeto I2P espelhado dentro da rede, **`i2pforum.i2p`** hospeda o fórum de suporte comunitário, **`stats.i2p`** fornece estatísticas da rede e um serviço de registro de endereços, e **`notbob.i2p`** monitora o tempo de atividade dos eepsites conhecidos para que você possa ver o que está realmente online. Quando encontrar um endereço `.i2p` desconhecido, o proxy oferecerá links de "serviço de salto" que resolvem o nome do host — clique neles para adicionar novos sites ao seu catálogo de endereços local.

O I2P também inclui um **outproxy** padrão (`exit.stormycloud.i2p`) que permite acessar a internet regular através do I2P, mas essa não é a finalidade principal da rede e o desempenho será lento. O I2P foi projetado como uma darknet interna, não como uma rede de nós de saída como o Tor.

### Compartilhe arquivos torrent anonimamente com o I2PSnark

**I2PSnark** é um cliente BitTorrent totalmente funcional integrado a toda instalação I2P, acessível em `http://127.0.0.1:7657/i2psnark/`. Ele opera inteiramente dentro da rede I2P — não pode se conectar a torrents da internet clara, e usuários da internet clara não podem ver torrents do I2P. A interface web suporta links magnéticos (magnet links), DHT, arrastar e soltar (drag-and-drop), busca de torrents, downloads sequenciais e rastreadores UDP (adicionados na versão 2.10.0). O comprimento padrão do túnel é de três saltos. Basta adicionar arquivos `.torrent` ou links magnéticos pela interface.

![Interface do I2PSnark](/images/guides/quickstart/i2psnark-interface.png)

Para encontrar torrents, visite o **Postman Tracker** em `http://tracker2.postman.i2p/` - um hub centralizado onde os usuários pesquisam e baixam torrents que foram enviados por outras pessoas dentro da rede I2P. Você também pode enviar seus próprios torrents para compartilhar com a comunidade.

![Postman Tracker](/images/guides/quickstart/postman-tracker.png)

Outros clientes torrent compatíveis com I2P incluem BiglyBT e qBittorrent com um plugin I2P.

### Envie e-mails criptografados com o SusiMail

**SusiMail** em `http://127.0.0.1:7657/susimail/` é um cliente de e-mail baseado na web projetado para evitar vazamento de informações identificáveis. Ele se conecta ao servidor de e-mail **`mail.i2p`** operado por "postman". Para começar, registre uma conta em **`hq.postman.i2p`** (acessível através do seu proxy I2P), depois faça login com essas credenciais no SusiMail. As entradas pré-configuradas do I2PTunnel roteiam SMTP por `localhost:7659` e POP3 por `localhost:7660`. Você pode enviar e-mails tanto para outros usuários `@mail.i2p` quanto para endereços de e-mail da internet convencional (conectados através do outproxy do servidor de e-mail). O SusiMail suporta formatação markdown, anexos por arrastar e soltar, e e-mails em HTML.

![Caixa de Entrada do SusiMail](/images/guides/quickstart/susimail-login.png)

![Escrever no SusiMail](/images/guides/quickstart/susimail-inbox.png)

### Converse no IRC através da rede Irc2P

O I2P é fornecido com um **túnel IRC pré-configurado** em `localhost:6668`. Aponte qualquer cliente IRC para este endereço (com SSL/TLS **desativado** - o I2P cuida da criptografia) e você se conectará à rede Irc2P, uma federação de servidores que inclui `irc.postman.i2p`, `irc.echelon.i2p` e `irc.dg.i2p`. Os principais canais são **`#i2p`** para discussões gerais, **`#i2p-dev`** para desenvolvimento e **`#i2p-help`** para suporte. O túnel IRC remove automaticamente informações identificáveis da sua conexão. Clientes recomendados incluem WeeChat, Pidgin e Thunderbird Chat.

### Hospede seu próprio site anônimo

Toda instalação do I2P inclui um **servidor web Jetty** já em execução em `localhost:7658` com um túnel de servidor I2P correspondente. Para publicar um site, basta colocar os arquivos HTML na raiz do documento: `~/.i2p/eepsite/docroot` no Linux ou `%LOCALAPPDATA%\I2P\I2P Site\docroot` no Windows. Seu site recebe automaticamente um destino criptográfico Base64 e um endereço mais curto `xxxxx.b32.i2p`. Para obter um nome legível como `mysite.i2p`, registre-o em serviços de catálogo de endereços como `stats.i2p` ou `no.i2p`. Para configurações mais avançadas, você pode substituir o Jetty pelo Apache ou Nginx atrás do túnel de servidor I2PTunnel — apenas lembre-se de remover os cabeçalhos do servidor que possam identificá-lo. Para um guia detalhado, consulte nosso tutorial [Criando um Eepsite no I2P](/docs/guides/creating-an-eepsite/).

---

## Práticas essenciais de segurança para novos usuários

**Nunca navegue no I2P e na clearnet no mesmo perfil do navegador.** Esta é a regra de segurança mais importante. Crie um perfil dedicado do Firefox através de `about:profiles` ou use o perfil pré-configurado do Easy Install Bundle. A contaminação cruzada de cookies, histórico e dados armazenados em cache entre sua navegação anônima e identificada é a falha mais comum em segurança operacional.

A extensão oficial do Firefox **"I2P in Private Browsing"** (disponível na loja de complementos da Mozilla) automatiza grande parte desse processo criando abas em contêineres isolados com anti-fingerprinting, isolamento de primeira parte e letterboxing ativados. Para usuários do Chromium, inicie com flags separadas: `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`.

---

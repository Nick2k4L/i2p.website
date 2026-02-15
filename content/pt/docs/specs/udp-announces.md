---
title: "Trackers UDP"
description: "Especificação de protocolo para anúncios UDP BitTorrent em I2P"
slug: "udp-announces"
aliases:
  - "/pt/docs/specs/udp-bittorrent-announces"
  - "/pt/docs/specs/udp-bittorrent-announces/"
category: "Protocolos"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Visão Geral

Esta especificação documenta o protocolo para anúncios UDP do bittorrent no I2P. Para a especificação geral do bittorrent no I2P, consulte [BitTorrent sobre I2P](/docs/applications/bittorrent). Para informações de contexto e adicionais sobre o desenvolvimento desta especificação, consulte a [Proposta 160](/proposals/160-udp-trackers).

## Design

Esta proposta usa repliable datagram2, repliable datagram3, e raw datagrams, conforme definido em [Datagrams](/docs/specs/datagrams). Datagram2 e Datagram3 são novas variantes de repliable datagrams, definidas na [Proposta 163](/proposals/163-datagram2-datagram3). Datagram2 adiciona resistência a replay e suporte para assinatura offline. Datagram3 é menor que o formato de datagram antigo, mas sem autenticação.

### BEP 15

Para referência, o fluxo de mensagens definido em [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) é o seguinte:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
A fase de conexão é necessária para prevenir a falsificação de endereços IP. O rastreador retorna um ID de conexão que o cliente usa em anúncios subsequentes. Este ID de conexão expira por padrão em um minuto no cliente e em dois minutos no rastreador.

O I2P usará o mesmo fluxo de mensagens do BEP 15, para facilitar a adoção em bases de código de clientes existentes capazes de UDP: por eficiência e pelas razões de segurança discutidas abaixo:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
Isso potencialmente proporciona uma grande economia de largura de banda em relação aos anúncios de streaming (TCP). Embora o Datagram2 tenha aproximadamente o mesmo tamanho que um SYN de streaming, a resposta raw é muito menor que o SYN ACK de streaming. Solicitações subsequentes usam Datagram3, e as respostas subsequentes são raw.

As solicitações de anúncio são Datagram3 para que o tracker não precise manter uma grande tabela de mapeamento de IDs de conexão para o destino do anúncio ou hash. Em vez disso, o tracker pode gerar IDs de conexão criptograficamente a partir do hash do remetente, do timestamp atual (baseado em algum intervalo) e de um valor secreto. Quando uma solicitação de anúncio é recebida, o tracker valida o ID de conexão e então usa o hash do remetente Datagram3 como o alvo de envio.

### Tempo de Vida da Conexão

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) especifica que o ID de conexão expira em um minuto no cliente, e em dois minutos no tracker. Não é configurável. Isso limita os ganhos potenciais de eficiência, a menos que os clientes agrupem anúncios para fazer todos eles dentro de uma janela de um minuto. O i2psnark atualmente não agrupa anúncios; ele os distribui, para evitar rajadas de tráfego. Relatam que usuários avançados executam milhares de torrents simultaneamente, e concentrar tantos anúncios em um minuto não é realista.

Aqui, propomos estender a resposta de conexão para adicionar um campo opcional de tempo de vida da conexão. O padrão, se não estiver presente, é de um minuto. Caso contrário, o tempo de vida especificado em segundos deve ser usado pelo cliente, e o tracker manterá o ID de conexão por mais um minuto.

### Compatibilidade com BEP 15

Este design mantém compatibilidade com [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) o máximo possível para limitar as mudanças necessárias em clientes e trackers existentes.

A única mudança obrigatória é o formato das informações do peer na resposta de anúncio. A adição do campo lifetime na resposta de conexão não é obrigatória, mas é altamente recomendada para eficiência, conforme explicado acima.

### Análise de Segurança

Um objetivo importante de um protocolo de anúncio UDP é prevenir a falsificação de endereços. O cliente deve realmente existir e agrupar um leaseset real. Ele deve ter tunnels de entrada para receber a Resposta de Conexão. Esses tunnels poderiam ser de zero saltos e construídos instantaneamente, mas isso exporia o criador. Este protocolo atinge esse objetivo.

### Problemas

- Este protocolo não suporta destinos ocultos, mas pode ser estendido para fazê-lo. Veja abaixo.

## Especificação

### Protocolos e Portas

Repliable Datagram2 usa protocolo I2CP 19; repliable Datagram3 usa protocolo I2CP 20; datagramas brutos usam protocolo I2CP 18. Solicitações podem ser Datagram2 ou Datagram3. Respostas são sempre brutas. O formato mais antigo de datagrama repliable ("Datagram1") usando protocolo I2CP 17 NÃO deve ser usado para solicitações ou respostas; estes devem ser descartados se recebidos nas portas de solicitação/resposta. Note que o protocolo Datagram1 17 ainda é usado para o protocolo DHT.

As requisições usam a "porta de destino" I2CP da URL de anúncio; veja abaixo. A "porta de origem" da requisição é escolhida pelo cliente, mas deve ser diferente de zero e uma porta diferente daquelas usadas pelo DHT, para que as respostas possam ser facilmente classificadas. Os trackers devem rejeitar requisições recebidas na porta errada.

As respostas usam a "porta de destino" I2CP da solicitação. A "porta de origem" da solicitação é a "porta de destino" da solicitação.

### URL de Anúncio

O formato da URL de anúncio não está especificado no [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), mas como na clearnet, URLs de anúncio UDP são da forma `udp://host:port/path`. O caminho é ignorado e pode estar vazio, mas é tipicamente `/announce` na clearnet. A parte `:port` deve sempre estar presente, entretanto, se a parte `:port` for omitida, use uma porta I2CP padrão de 6969, pois essa é a porta comum na clearnet. Também podem haver parâmetros cgi `&a=b&c=d` anexados, esses podem ser processados e fornecidos na solicitação de anúncio, veja [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). Se não houver parâmetros ou caminho, a `/` final também pode ser omitida, como implícito no [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

### Formatos de Datagrama

Todos os valores são enviados em ordem de bytes de rede (big endian). Não espere que os pacotes tenham exatamente um determinado tamanho. Extensões futuras podem aumentar o tamanho dos pacotes.

#### Solicitação de Conexão

Cliente para tracker. 16 bytes. Deve ser Datagram2 que permita resposta. Igual ao [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Sem alterações.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### Resposta de Conexão

Tracker para cliente. 16 ou 18 bytes. Deve ser raw. Igual ao [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) exceto conforme observado abaixo.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
A resposta DEVE ser enviada para a "porta de destino" I2CP que foi recebida como "porta de origem" da solicitação.

O campo lifetime é opcional e indica o tempo de vida do cliente connection_id em segundos. O padrão é 60, e o mínimo se especificado é 60. O máximo é 65535 ou cerca de 18 horas. O rastreador deve manter o connection_id por 60 segundos a mais que o tempo de vida do cliente.

#### Pedido de Anúncio

Cliente para rastreador. 98 bytes mínimo. Deve ser Datagram3 com capacidade de resposta. Igual ao [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) exceto quando observado abaixo.

O connection_id é como recebido na resposta de conexão.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
Mudanças do [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- key é ignorada
- endereço IP não é usado
- port provavelmente é ignorada mas deve ser a mesma que a porta I2CP from
- A seção options, se presente, é como definida em [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

A resposta DEVE ser enviada para a "porta de destino" I2CP que foi recebida como "porta de origem" da solicitação. Não use a porta da solicitação de anúncio.

#### Resposta de Anúncio

Tracker para cliente. Mínimo de 20 bytes. Deve ser raw. Igual ao [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) exceto conforme observado abaixo.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Alterações do [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- Em vez de IPv4+porta de 6 bytes ou IPv6+porta de 18 bytes, retornamos múltiplos de "respostas compactas" de 32 bytes com os hashes SHA-256 binários dos peers. Como nas respostas compactas TCP, não incluímos uma porta.

A resposta DEVE ser enviada para a "porta de destino" I2CP que foi recebida como "porta de origem" da solicitação. Não use a porta da solicitação de anúncio.

Os datagramas I2P têm um tamanho máximo muito grande de cerca de 64 KB; no entanto, para entrega confiável, datagramas maiores que 4 KB devem ser evitados. Para eficiência de largura de banda, os trackers provavelmente devem limitar o máximo de peers para cerca de 50, o que corresponde a cerca de um pacote de 1600 bytes antes do overhead em várias camadas, e deve estar dentro do limite de payload de duas mensagens de tunnel após fragmentação.

Como no BEP 15, não há contagem incluída do número de endereços de peer (IP/porta para BEP 15, hashes aqui) a seguir. Embora não contemplado no BEP 15, um marcador de fim-de-peers com todos zeros poderia ser definido para indicar que a informação de peer está completa e alguns dados de extensão seguem.

Para que a extensão seja possível no futuro, os clientes devem ignorar um hash de 32 bytes composto apenas por zeros, e quaisquer dados que o seguem. Os trackers devem rejeitar anúncios de um hash composto apenas por zeros, embora esse hash já seja banido pelos routers Java.

#### Extrair

A solicitação/resposta de scrape do [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) não é exigida por esta especificação, mas pode ser implementada se desejado, sem necessidade de alterações. O cliente deve primeiro adquirir um ID de conexão. A solicitação de scrape é sempre um Datagram3 com resposta obrigatória. A resposta de scrape é sempre raw.

#### Resposta de Erro

Tracker para cliente. 8 bytes no mínimo (se a mensagem estiver vazia). Deve ser raw. Igual ao [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Sem alterações.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## Extensões

Bits de extensão ou um campo de versão não são incluídos. Clientes e trackers não devem assumir que os pacotes tenham um determinado tamanho. Desta forma, campos adicionais podem ser adicionados sem quebrar a compatibilidade. O formato de extensões definido em [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) é recomendado se necessário.

A resposta de conexão é modificada para adicionar um tempo de vida opcional do ID de conexão.

Se for necessário suporte para destino oculto, podemos adicionar o endereço oculto de 35 bytes ao final da solicitação de anúncio, ou solicitar hashes ocultos nas respostas, usando o formato [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) (parâmetros a serem determinados). O conjunto de endereços de pares ocultos de 35 bytes pode ser adicionado ao final da resposta de anúncio, após um hash de 32 bytes com todos zeros.

## Diretrizes de Implementação

Consulte a seção de design acima para uma discussão dos desafios para clientes e trackers não integrados e não-I2CP.

### Clientes

Para um determinado hostname do tracker, um cliente deve preferir URLs UDP sobre HTTP, e não deve anunciar para ambos.

Clientes com suporte BEP 15 existente devem exigir apenas pequenas modificações.

Se um cliente suporta DHT ou outros protocolos de datagram, provavelmente deveria selecionar uma porta diferente como "porta de origem" da solicitação, para que as respostas retornem a essa porta e não sejam misturadas com mensagens DHT. O cliente apenas recebe datagramas brutos como respostas. Os trackers nunca enviarão um datagram2 respondível para o cliente.

Clientes com uma lista padrão de opentrackers devem atualizar a lista para adicionar URLs UDP depois que os opentrackers conhecidos passarem a suportar UDP.

Os clientes podem ou não implementar retransmissão de solicitações. Retransmissões, se implementadas, devem usar um timeout inicial de pelo menos 15 segundos, e dobrar o timeout para cada retransmissão (backoff exponencial).

Os clientes devem recuar após receberem uma resposta de erro.

### Rastreadores

Trackers com suporte BEP 15 existente devem necessitar apenas pequenas modificações. Esta especificação difere da proposta de 2014, pois o tracker deve suportar a recepção de repliable datagram2 e datagram3 na mesma porta.

Para minimizar os requisitos de recursos do tracker, este protocolo foi projetado para eliminar qualquer necessidade de que o tracker armazene mapeamentos de hashes de clientes para IDs de conexão para validação posterior. Isso é possível porque o pacote de solicitação de anúncio é um pacote Datagram3 que pode ser respondido, então ele contém o hash do remetente.

Uma implementação recomendada é:

- Definir a época atual como o tempo atual com uma resolução do tempo de vida da conexão, `epoch = now / lifetime`.
- Definir uma função de hash criptográfico `H(secret, clienthash, epoch)` que gera uma saída de 8 bytes.
- Gerar a constante aleatória secreta usada para todas as conexões.
- Para respostas de conexão, gerar `connection_id = H(secret, clienthash, epoch)`
- Para solicitações de anúncio, validar o ID de conexão recebido na época atual verificando `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## Referências

- **[BEP15]** [BEP 15 - Protocolo de Tracker UDP](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - Extensões do Protocolo de Tracker UDP](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Especificação de Datagramas](/docs/specs/datagrams)
- **[Prop160]** [Proposta 160 - Trackers UDP](/proposals/160-udp-trackers)
- **[Prop163]** [Proposta 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [API SAM v3](/docs/api/samv3)
- **[SPEC]** [BitTorrent sobre I2P](/docs/applications/bittorrent)

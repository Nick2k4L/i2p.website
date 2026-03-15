---
title: "Entrega OBEP para Túneis de 1-em-N ou N-em-N"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Open"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## Visão Geral

Esta proposta abrange duas melhorias para aumentar o desempenho da rede:

- Delegar a seleção do IBGW ao OBEP fornecendo uma lista de
  alternativas em vez de uma única opção.

- Habilitar o roteamento de pacotes multicast no OBEP.


## Motivação

No caso de conexão direta, a ideia é reduzir a congestão da conexão, dando ao
OBEP flexibilidade na forma como se conecta aos IBGWs. A capacidade de especificar
múltiplos túneis também nos permite implementar multicast no OBEP (entregando a
mensagem a todos os túneis especificados).

Uma alternativa à parte de delegação desta proposta seria enviar através de um
hash de LeaseSet, semelhante à capacidade existente de especificar um hash de
[RouterIdentity](/docs/specs/common-structures/#common-structure-specification). Isso resultaria em uma mensagem menor e um LeaseSet potencialmente
mais recente. No entanto:

1. Isso forçaria o OBEP a fazer uma consulta.

2. O LeaseSet pode não estar publicado em um floodfill, então a consulta falharia.

3. O LeaseSet pode estar criptografado, então o OBEP não poderia obter os leases.

4. Especificar um LeaseSet revelaria ao OBEP o [Destination](/docs/specs/common-structures/#destination) da mensagem,
   que de outra forma só poderia descobrir varrendo todos os LeaseSets da
   rede e procurando por um lease correspondente.


## Projeto

O originador (OBGW) colocaria alguns (todos?) dos [Leases](/docs/specs/common-structures/#lease) de destino nas
instruções de entrega [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) em vez de escolher apenas um.

O OBEP selecionaria um desses para entregar. O OBEP selecionaria, se
disponível, um ao qual já está conectado ou que já conhece. Isso tornaria o caminho OBEP-IBGW mais rápido e confiável, e reduziria o número total de
conexões na rede.

Temos um tipo de entrega não utilizado (0x03) e dois bits restantes (0 e 1) nas
flags do TUNNEL-DELIVERY, que podemos aproveitar para implementar essas funcionalidades.


## Implicações de Segurança

Esta proposta não altera a quantidade de informações vazadas sobre o
Destination de destino do OBGW ou sua visão do NetDB:

- Um adversário que controle o OBEP e esteja varrendo LeaseSets do NetDB
  já pode determinar se uma mensagem está sendo enviada para um determinado
  Destination, buscando o par TunnelId / RouterIdentity. Na pior das hipóteses, a presença de múltiplos Leases no TMDI pode tornar mais rápido encontrar uma correspondência no banco de dados do adversário.

- Um adversário que opere um Destination malicioso já pode obter
  informações sobre a visão da vítima do NetDB, publicando
  LeaseSets contendo diferentes túneis de entrada em diferentes floodfills e
  observando por quais túneis o OBGW se conecta. Do ponto de vista do adversário,
  o OBEP selecionando qual túnel usar é funcionalmente idêntico ao OBGW
  fazendo a seleção.

A flag multicast revela ao OBEP o fato de que o OBGW está fazendo multicast. Isso cria uma troca entre desempenho e privacidade que deve ser considerada ao
implementar protocolos de nível superior. Sendo uma flag opcional, os usuários podem tomar
a decisão apropriada para sua aplicação. Pode haver benefícios em tornar esse
comportamento padrão para aplicações compatíveis, entretanto, pois o uso generalizado
por uma variedade de aplicações reduziria a vazão de informações sobre qual aplicação
específica uma mensagem provém.


## Especificação

As Instruções de Entrega do Primeiro Fragmento seriam modificadas da seguinte forma:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       Ordem dos bits: 76543210
       bits 6-5: tipo de entrega
                 0x03 = TUNNELS
       bit 0: multicast? Se 0, entregar a um dos túneis
                         Se 1, entregar a todos os túneis
                         Definido como 0 para compatibilidade com usos futuros se
                         o tipo de entrega não for TUNNELS

Count ::
       1 byte
       Opcional, presente se o tipo de entrega for TUNNELS
       2-255 - Número de pares id/hash a seguir

Tunnel ID :: TunnelId
To Hash ::
       36 bytes cada
       Opcional, presente se o tipo de entrega for TUNNELS
       pares id/hash

Tamanho total: Comprimento típico é:
       75 bytes para entrega TUNNELS com contagem 2 (mensagem de túnel não fragmentada);
       79 bytes para entrega TUNNELS com contagem 2 (primeiro fragmento)

Resto das instruções de entrega inalterado
```


## Compatibilidade

Os únicos pares que precisam entender a nova especificação são os OBGWs
e os OBEPs. Portanto, podemos tornar essa mudança compatível com a rede existente
tornando seu uso condicional à versão do I2P de destino:

* Os OBGWs devem selecionar OBEPs compatíveis ao construir túneis de saída, com base
  na versão do I2P anunciada em seu [RouterInfo](/docs/specs/common-structures/#routerinfo).

* Pares que anunciam a versão de destino devem suportar a análise das novas flags,
  e não devem rejeitar as instruções como inválidas.


## Referências

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)

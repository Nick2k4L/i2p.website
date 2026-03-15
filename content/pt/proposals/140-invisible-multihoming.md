---
title: "Multihoming Invisível"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "Abrir"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## Visão geral

Esta proposta descreve um projeto para um protocolo que permite a um cliente I2P, serviço ou processo balanceador externo gerenciar múltiplos roteadores hospedando transparentemente uma única [Destination](/docs/specs/common-structures/#destination).

A proposta atualmente não especifica uma implementação concreta. Pode ser implementada como uma extensão do [I2CP](/docs/specs/i2cp/), ou como um novo protocolo.


## Motivação

Multihoming é o uso de múltiplos roteadores para hospedar a mesma Destination. A maneira atual de fazer multihoming com I2P é executar a mesma Destination em cada roteador de forma independente; o roteador usado pelos clientes em um determinado momento é o último a publicar um LeaseSet.

Isso é uma solução improvisada e presumivelmente não funcionará para grandes sites em escala. Digamos que tivéssemos 100 roteadores com multihoming, cada um com 16 túneis. Isso resultaria em 1600 publicações de LeaseSet a cada 10 minutos, ou quase 3 por segundo. Os floodfills seriam sobrecarregados e os limitadores entrariam em ação. E isso sem sequer mencionar o tráfego de consulta.

A Proposta 123 resolve esse problema com um meta-LeaseSet, que lista os 100 hashes reais de LeaseSet. Uma consulta torna-se um processo de duas etapas: primeiro procurando o meta-LeaseSet, e depois um dos LeaseSets nomeados. Essa é uma boa solução para o problema do tráfego de consulta, mas por si só cria um vazamento significativo de privacidade: é possível determinar quais roteadores com multihoming estão online monitorando o meta-LeaseSet publicado, porque cada LeaseSet real corresponde a um único roteador.

Precisamos de uma maneira para que um cliente ou serviço I2P espalhe uma única Destination por múltiplos roteadores, de forma indistinguível do uso de um único roteador (do ponto de vista do próprio LeaseSet).


## Projeto

### Definições

    User
        A pessoa ou organização que deseja usar multihoming em suas Destination(s). Uma
        única Destination é considerada aqui sem perda de generalidade (WLOG).

    Client
        O aplicativo ou serviço executado atrás da Destination. Pode ser um
        aplicativo cliente, servidor ou ponto a ponto; referimo-nos a ele como
        cliente no sentido de que se conecta aos roteadores I2P.

        O cliente consiste em três partes, que podem estar no mesmo processo
        ou podem ser divididas entre processos ou máquinas (em uma configuração multi-cliente):

        Balancer
            A parte do cliente que gerencia a seleção de pares e a construção de túneis.
            Há um único balanceador em um dado momento, e ele se comunica com todos os roteadores I2P.
            Pode haver balanceadores de failover.

        Frontend
            A parte do cliente que pode ser operada em paralelo. Cada frontend se comunica com um único roteador I2P.

        Backend
            A parte do cliente compartilhada entre todos os frontends. Não possui comunicação direta com nenhum roteador I2P.

    Router
        Um roteador I2P executado pelo usuário que fica na fronteira entre a rede I2P e a rede do usuário (semelhante a um dispositivo de borda em redes corporativas). Ele constrói túneis sob comando de um balanceador e roteia pacotes para um cliente ou frontend.

### Visão geral de alto nível

Imagine a seguinte configuração desejada:

- Um aplicativo cliente com uma Destination.
- Quatro roteadores, cada um gerenciando três túneis de entrada.
- Os doze túneis devem ser publicados em um único LeaseSet.

### Cliente único

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]-----
                 |-{ [Tunnel 3]===/               \
                 |                                 \
                 |-{ [Tunnel 4]===\                 \
  [Destination]  |-{ [Tunnel 5]====[Router 2]-----   \
    \            |-{ [Tunnel 6]===/               \   \
     [LeaseSet]--|                               [Client]
                 |-{ [Tunnel 7]===\               /   /
                 |-{ [Tunnel 8]====[Router 3]-----   /
                 |-{ [Tunnel 9]===/                 /
                 |                                 /
                 |-{ [Tunnel 10]==\               /
                 |-{ [Tunnel 11]===[Router 4]-----
                  -{ [Tunnel 12]==/
```

### Cliente múltiplo

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]---------[Frontend 1]
                 |-{ [Tunnel 3]===/          \                    \
                 |                            \                    \
                 |-{ [Tunnel 4]===\            \                    \
  [Destination]  |-{ [Tunnel 5]====[Router 2]---\-----[Frontend 2]   \
    \            |-{ [Tunnel 6]===/          \   \                \   \
     [LeaseSet]--|                         [Balancer]            [Backend]
                 |-{ [Tunnel 7]===\          /   /                /   /
                 |-{ [Tunnel 8]====[Router 3]---/-----[Frontend 3]   /
                 |-{ [Tunnel 9]===/            /                    /
                 |                            /                    /
                 |-{ [Tunnel 10]==\          /                    /
                 |-{ [Tunnel 11]===[Router 4]---------[Frontend 4]
                  -{ [Tunnel 12]==/
```

### Processo geral do cliente

- Carregar ou gerar uma Destination.

- Abrir uma sessão com cada roteador, vinculada à Destination.

- Periodicamente (a cada dez minutos, aproximadamente, mas mais ou menos com base na atividade dos túneis):

  - Obter a camada rápida (fast tier) de cada roteador.

  - Usar o conjunto completo de pares para construir túneis para/de cada roteador.

    - Por padrão, túneis para/de um roteador específico usarão pares da camada rápida desse roteador, mas isso não é imposto pelo protocolo.

  - Coletar o conjunto de túneis de entrada ativos de todos os roteadores ativos e criar um LeaseSet.

  - Publicar o LeaseSet por meio de um ou mais roteadores.

### Diferenças em relação ao I2CP

Para criar e gerenciar essa configuração, o cliente precisa das seguintes funcionalidades novas além do que é atualmente fornecido pelo [I2CP](/docs/specs/i2cp/):

- Instruir um roteador a construir túneis, sem criar um LeaseSet para eles.
- Obter uma lista dos túneis atuais no pool de entrada.

Além disso, as seguintes funcionalidades permitiriam flexibilidade significativa na forma como o cliente gerencia seus túneis:

- Obter o conteúdo da camada rápida (fast tier) de um roteador.
- Instruir um roteador a construir um túnel de entrada ou saída usando uma lista específica de pares.

### Esboço do protocolo

```
         Client                           Router

                    --------------------->  Create Session
   Session Status  <---------------------
                    --------------------->  Get Fast Tier
        Peer List  <---------------------
                    --------------------->  Create Tunnel
    Tunnel Status  <---------------------
                    --------------------->  Get Tunnel Pool
      Tunnel List  <---------------------
                    --------------------->  Publish LeaseSet
                    --------------------->  Send Packet
      Send Status  <---------------------
  Packet Received  <---------------------
```

### Mensagens

**Create Session**
- Cria uma sessão para a Destination fornecida.

**Session Status**
- Confirmação de que a sessão foi configurada e que o cliente pode agora começar a construir túneis.

**Get Fast Tier**
- Solicita uma lista dos pares que o roteador atualmente consideraria para construção de túneis.

**Peer List**
- Uma lista de pares conhecidos pelo roteador.

**Create Tunnel**
- Solicita que o roteador construa um novo túnel pelos pares especificados.

**Tunnel Status**
- O resultado da construção de um túnel específico, assim que estiver disponível.

**Get Tunnel Pool**
- Solicita uma lista dos túneis atuais no pool de entrada ou saída para a Destination.

**Tunnel List**
- Uma lista de túneis para o pool solicitado.

**Publish LeaseSet**
- Solicita que o roteador publique o LeaseSet fornecido por meio de um dos túneis de saída para a Destination. Nenhum status de resposta é necessário; o roteador deve continuar tentando até que esteja satisfeito de que o LeaseSet foi publicado.

**Send Packet**
- Um pacote de saída do cliente. Opcionalmente especifica um túnel de saída pelo qual o pacote deve (deveria?) ser enviado.

**Send Status**
- Informa ao cliente o sucesso ou falha no envio de um pacote.

**Packet Received**
- Um pacote de entrada para o cliente. Opcionalmente especifica o túnel de entrada pelo qual o pacote foi recebido(?)


## Implicações de segurança

Do ponto de vista dos roteadores, este projeto é funcionalmente equivalente à situação atual. O roteador ainda constrói todos os túneis, mantém seus próprios perfis de pares e impõe separação entre operações do roteador e do cliente. Na configuração padrão, é completamente idêntico, porque os túneis para esse roteador são construídos a partir de sua própria camada rápida.

Do ponto de vista do netDB, um único LeaseSet criado por meio deste protocolo é idêntico à situação atual, porque aproveita funcionalidades já existentes. No entanto, para LeaseSets maiores, próximos de 16 Leases, pode ser possível para um observador determinar que o LeaseSet está usando multihoming:

- O tamanho máximo atual da camada rápida é de 75 pares. O Gateway de Entrada (IBGW, o nó publicado em um Lease) é selecionado de uma fração dessa camada (particionada aleatoriamente por pool de túneis por hash, não por contagem):

      1 salto
          Toda a camada rápida

      2 saltos
          Metade da camada rápida
          (o padrão até meados de 2014)

      3+ saltos
          Um quarto da camada rápida
          (3 sendo o padrão atual)

  Isso significa que, em média, os IBGWs virão de um conjunto de 20-30 pares.

- Em uma configuração com um único roteador, um LeaseSet completo de 16 túneis teria 16 IBGWs selecionados aleatoriamente de um conjunto de até (digamos) 20 pares.

- Em uma configuração com 4 roteadores usando multihoming com a configuração padrão, um LeaseSet completo de 16 túneis teria 16 IBGWs selecionados aleatoriamente de um conjunto de no máximo 80 pares, embora provavelmente haja uma fração de pares comuns entre os roteadores.

Portanto, com a configuração padrão, pode ser possível, por meio de análise estatística, descobrir que um LeaseSet está sendo gerado por este protocolo. Também pode ser possível descobrir quantos roteadores existem, embora o efeito da rotatividade (churn) nas camadas rápidas reduza a eficácia dessa análise.

Como o cliente tem controle total sobre quais pares seleciona, esse vazamento de informação poderia ser reduzido ou eliminado selecionando IBGWs de um conjunto reduzido de pares.


## Compatibilidade

Este projeto é completamente compatível com a rede, pois não há alterações no formato do LeaseSet. Todos os roteadores precisariam conhecer o novo protocolo, mas isso não é uma preocupação, já que todos seriam controlados pela mesma entidade.


## Notas sobre desempenho e escalabilidade

O limite superior de 16 Leases por LeaseSet não é alterado por esta proposta. Para Destinations que exigem mais túneis do que isso, existem duas possíveis modificações na rede:

- Aumentar o limite superior do tamanho dos LeaseSets. Isso seria o mais simples de implementar (embora ainda exigisse suporte generalizado na rede antes de poder ser amplamente usado), mas poderia resultar em consultas mais lentas devido ao aumento do tamanho dos pacotes. O tamanho máximo viável de um LeaseSet é definido pelo MTU dos transportes subjacentes, sendo portanto cerca de 16kB.

- Implementar a Proposta 123 para LeaseSets em camadas. Em combinação com esta proposta, as Destinations para os sub-LeaseSets poderiam ser distribuídas por múltiplos roteadores, funcionando efetivamente como múltiplos endereços IP para um serviço em clearnet.


## Agradecimentos

Agradecimentos a psi pela discussão que levou a esta proposta.


## Referências

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)

---
title: "Protocolo da Fazenda de Alho"
number: "150"
author: "zzz"
created: "02-05-2019"
lastupdated: "20-05-2019"
status: "Aberto"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## Visão Geral

Esta é a especificação para o protocolo de rede Garlic Farm,
baseado no JRaft, seu código "exts" para implementação sobre TCP,
e seu aplicativo de exemplo "dmprinter" [JRAFT](https://github.com/datatechnology/jraft).


Não conseguimos encontrar nenhuma implementação com um protocolo de rede documentado.
No entanto, a implementação do JRaft é simples o suficiente para que pudéssemos
inspecionar o código e então documentar seu protocolo.
Esta proposta é o resultado desse esforço.

Esta será a base para a coordenação de roteadores publicando
entradas em um Meta LeaseSet. Veja a proposta 123.


## Objetivos

- Pequeno tamanho de código
- Baseado em implementação existente
- Sem objetos Java serializados ou quaisquer recursos ou codificações específicas do Java
- Qualquer inicialização está fora do escopo. Assume-se que pelo menos um outro servidor
  esteja codificado diretamente ou configurado fora da banda deste protocolo.
- Suportar casos de uso tanto fora da banda quanto dentro do I2P.


## Projeto

O protocolo Raft não é um protocolo concreto; ele define apenas uma máquina de estados.
Portanto, documentamos o protocolo concreto do JRaft e baseamos nosso protocolo nele.
Não há alterações no protocolo JRaft além da adição de
um handshake de autenticação.

O Raft elege um Líder cujo trabalho é publicar um log.
O log contém dados de Configuração Raft e dados de Aplicação.
Os dados de aplicação contêm o status de cada Roteador do Servidor e o Destino
para o cluster Meta LS2.
Os servidores usam um algoritmo comum para determinar o publicador e o conteúdo
do Meta LS2.
O publicador do Meta LS2 NÃO é necessariamente o Líder Raft.



## Especificação

O protocolo de rede opera sobre sockets SSL ou sockets I2P sem SSL.
Sockets I2P são proxyados através do Proxy HTTP.
Não há suporte para sockets não SSL na clearnet.

### Handshake e autenticação

Não definido pelo JRaft.

Objetivos:

- Método de autenticação usuário/senha
- Identificador de versão
- Identificador de cluster
- Extensível
- Facilidade de proxy quando usado para sockets I2P
- Não expor desnecessariamente o servidor como um servidor Garlic Farm
- Protocolo simples para que uma implementação completa de servidor web não seja necessária
- Compatível com padrões comuns, para que implementações possam usar
  bibliotecas padrão se desejado

Usaremos um handshake semelhante ao websocket e
autenticação HTTP Digest [RFC 2617](https://tools.ietf.org/html/rfc2617).
A autenticação Basic da RFC 2617 NÃO é suportada.
Ao fazer proxy através do proxy HTTP, comunique-se com
o proxy conforme especificado na [RFC 2616](https://tools.ietf.org/html/rfc2616).

#### Credenciais

Se nomes de usuário e senhas são por cluster ou
por servidor, é dependente da implementação.


#### HTTP Request 1

O originador enviará o seguinte.

Todas as linhas são terminadas com CRLF conforme exigido pelo HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (quaisquer outros cabeçalhos ignorados)
  (linha em branco)

  CLUSTER é o nome do cluster (padrão "farm")
  VERSION é a versão Garlic Farm (atualmente "1")

```


#### HTTP Response 1

Se o caminho não estiver correto, o destinatário enviará uma resposta padrão "HTTP/1.1 404 Not Found",
conforme na [RFC 2616](https://tools.ietf.org/html/rfc2616).

Se o caminho estiver correto, o destinatário enviará uma resposta padrão "HTTP/1.1 401 Unauthorized",
incluindo o cabeçalho WWW-Authenticate de autenticação digest HTTP,
conforme na [RFC 2617](https://tools.ietf.org/html/rfc2617).

Ambas as partes então fecharão o socket.


#### HTTP Request 2

O originador enviará o seguinte,
conforme na [RFC 2617](https://tools.ietf.org/html/rfc2617).

Todas as linhas são terminadas com CRLF conforme exigido pelo HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (cabeçalhos Sec-Websocket-* se for proxyado)
  Authorization: (cabeçalho de autorização digest HTTP conforme RFC 2617)
  (quaisquer outros cabeçalhos ignorados)
  (linha em branco)

  CLUSTER é o nome do cluster (padrão "farm")
  VERSION é a versão Garlic Farm (atualmente "1")

```


#### HTTP Response 2

Se a autenticação não estiver correta, o destinatário enviará outra resposta padrão "HTTP/1.1 401 Unauthorized",
conforme na [RFC 2617](https://tools.ietf.org/html/rfc2617).

Se a autenticação estiver correta, o destinatário enviará a seguinte resposta,
conforme no protocolo WebSocket.

Todas as linhas são terminadas com CRLF conforme exigido pelo HTTP.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (cabeçalhos Sec-Websocket-*)
  (quaisquer outros cabeçalhos ignorados)
  (linha em branco)

```

Após isso ser recebido, o socket permanece aberto.
O protocolo Raft conforme definido abaixo começa, no mesmo socket.


#### Cache

As credenciais devem ser armazenadas em cache por pelo menos uma hora, para que
conexões subsequentes possam pular diretamente para
"HTTP Request 2" acima.



### Tipos de Mensagem

Há dois tipos de mensagens: requisições e respostas.
Requisições podem conter Entradas de Log e são de tamanho variável;
respostas não contêm Entradas de Log e são de tamanho fixo.

Os tipos de mensagem 1-4 são as mensagens RPC padrão definidas pelo Raft.
Este é o protocolo Raft principal.

Os tipos de mensagem 5-15 são as mensagens RPC estendidas definidas pelo
JRaft, para suportar clientes, mudanças dinâmicas de servidor e
sincronização eficiente de log.

Os tipos de mensagem 16-17 são as mensagens RPC de compactação de log definidas
na seção 7 do Raft.


| Mensagem | Número | Enviado Por | Enviado Para | Notas |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Candidato | Seguidor | RPC padrão Raft; não deve conter entradas de log |
| RequestVoteResponse | 2 | Seguidor | Candidato | RPC padrão Raft |
| AppendEntriesRequest | 3 | Líder | Seguidor | RPC padrão Raft |
| AppendEntriesResponse | 4 | Seguidor | Líder / Cliente | RPC padrão Raft |
| ClientRequest | 5 | Cliente | Líder / Seguidor | Resposta é AppendEntriesResponse; deve conter apenas entradas de log de Aplicação |
| AddServerRequest | 6 | Cliente | Líder | Deve conter apenas uma única entrada de log ClusterServer |
| AddServerResponse | 7 | Líder | Cliente | O Líder também enviará um JoinClusterRequest |
| RemoveServerRequest | 8 | Seguidor | Líder | Deve conter apenas uma única entrada de log ClusterServer |
| RemoveServerResponse | 9 | Líder | Seguidor | |
| SyncLogRequest | 10 | Líder | Seguidor | Deve conter apenas uma única entrada de log LogPack |
| SyncLogResponse | 11 | Seguidor | Líder | |
| JoinClusterRequest | 12 | Líder | Novo Servidor | Convite para ingressar; deve conter apenas uma única entrada de log de Configuração |
| JoinClusterResponse | 13 | Novo Servidor | Líder | |
| LeaveClusterRequest | 14 | Líder | Seguidor | Comando para sair |
| LeaveClusterResponse | 15 | Seguidor | Líder | |
| InstallSnapshotRequest | 16 | Líder | Seguidor | Seção 7 do Raft; Deve conter apenas uma única entrada de log SnapshotSyncRequest |
| InstallSnapshotResponse | 17 | Seguidor | Líder | Seção 7 do Raft |


### Estabelecimento

Após o handshake HTTP, a sequência de estabelecimento é a seguinte:

```text

Novo Servidor Alice              Seguidor Aleatório Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  Se Bob disser que é o líder, continue conforme abaixo.
  Caso contrário, Alice deve se desconectar de Bob e conectar-se ao líder.


  Novo Servidor Alice              Líder Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       OU InstallSnapshotRequest
  SyncLogResponse  ------->
  OU InstallSnapshotResponse

```

Sequência de Desconexão:

```text

Seguidor Alice              Líder Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

Sequência de Eleição:

```text

Candidato Alice               Seguidor Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  se Alice vencer a eleição:

  Líder Alice                Seguidor Bob

  AppendEntriesRequest   ------->
  (heartbeat)
          <---------   AppendEntriesResponse

```


### Definições

- Origem: Identifica o originador da mensagem
- Destino: Identifica o destinatário da mensagem
- Termos: Veja Raft. Inicializado em 0, aumenta monotonicamente
- Índices: Veja Raft. Inicializado em 0, aumenta monotonicamente



### Requisições

Requisições contêm um cabeçalho e zero ou mais entradas de log.
Requisições contêm um cabeçalho de tamanho fixo e Entradas de Log opcionais de tamanho variável.


#### Cabeçalho de Requisição

O cabeçalho da requisição tem 45 bytes, conforme a seguir.
Todos os valores são inteiros sem sinal em big-endian.

```text

Tipo de mensagem:      1 byte
  Origem:                ID, inteiro de 4 bytes
  Destino:               ID, inteiro de 4 bytes
  Termo:                 Termo atual (ver notas), inteiro de 8 bytes
  Último Termo do Log:   inteiro de 8 bytes
  Último Índice do Log:  inteiro de 8 bytes
  Índice de Confirmação: inteiro de 8 bytes
  Tamanho das entradas de log: Tamanho total em bytes, inteiro de 4 bytes
  Entradas de log:       ver abaixo, comprimento total conforme especificado

```


#### Notas

Na RequestVoteRequest, Termo é o termo do candidato.
Caso contrário, é o termo atual do líder.

Na AppendEntriesRequest, quando o tamanho das entradas de log é zero,
esta mensagem é uma mensagem de heartbeat (keepalive).



#### Entradas de Log

O log contém zero ou mais entradas de log.
Cada entrada de log é conforme a seguir.
Todos os valores são inteiros sem sinal em big-endian.

```text

Termo:           inteiro de 8 bytes
  Tipo de valor:   1 byte
  Tamanho da entrada: Em bytes, inteiro de 4 bytes
  Entrada:         comprimento conforme especificado

```


#### Conteúdo do Log

Todos os valores são inteiros sem sinal em big-endian.

| Tipo de Valor do Log | Número |
| :--- | :--- |
| Aplicação | 1 |
| Configuração | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Aplicação

O conteúdo da aplicação é codificado em UTF-8 [JSON](https://www.json.org/).
Veja a seção Camada de Aplicação abaixo.


#### Configuração

Isso é usado para o líder serializar uma nova configuração de cluster e replicar para os pares.
Contém zero ou mais configurações de ClusterServer.


```text

Índice do Log:  inteiro de 8 bytes
  Último Índice do Log:  inteiro de 8 bytes
  Dados ClusterServer para cada servidor:
    ID:                inteiro de 4 bytes
    Tamanho dos dados do endpoint: Em bytes, inteiro de 4 bytes
    Dados do endpoint:     string ASCII no formato "tcp://localhost:9001", comprimento conforme especificado

```


#### ClusterServer

As informações de configuração de um servidor em um cluster.
Isso é incluído apenas em uma mensagem AddServerRequest ou RemoveServerRequest.

Quando usado em uma mensagem AddServerRequest:

```text

ID:                inteiro de 4 bytes
  Tamanho dos dados do endpoint: Em bytes, inteiro de 4 bytes
  Dados do endpoint:     string ASCII no formato "tcp://localhost:9001", comprimento conforme especificado

```


Quando usado em uma mensagem RemoveServerRequest:

```text

ID:                inteiro de 4 bytes

```


#### LogPack

Isso é incluído apenas em uma mensagem SyncLogRequest.

O seguinte é compactado com gzip antes da transmissão:


```text

Tamanho dos dados do índice: Em bytes, inteiro de 4 bytes
  Tamanho dos dados do log:   Em bytes, inteiro de 4 bytes
  Dados do índice:     8 bytes para cada índice, comprimento conforme especificado
  Dados do log:       comprimento conforme especificado

```



#### SnapshotSyncRequest

Isso é incluído apenas em uma mensagem InstallSnapshotRequest.

```text

Último Índice do Log:  inteiro de 8 bytes
  Último Termo do Log:   inteiro de 8 bytes
  Tamanho dos dados da configuração: Em bytes, inteiro de 4 bytes
  Dados da configuração:     comprimento conforme especificado
  Offset:          O offset dos dados no banco de dados, em bytes, inteiro de 8 bytes
  Tamanho dos dados:        Em bytes, inteiro de 4 bytes
  Dados:            comprimento conforme especificado
  Está Concluído:         1 se concluído, 0 se não concluído (1 byte)

```




### Respostas

Todas as respostas têm 26 bytes, conforme a seguir.
Todos os valores são inteiros sem sinal em big-endian.

```text

Tipo de mensagem:   1 byte
  Origem:         ID, inteiro de 4 bytes
  Destino:    Geralmente o ID do destinatário real (ver notas), inteiro de 4 bytes
  Termo:           Termo atual, inteiro de 8 bytes
  Próximo Índice:     Inicializado como último índice do log do líder + 1, inteiro de 8 bytes
  É Aceito:    1 se aceito, 0 se não aceito (ver notas), 1 byte

```


#### Notas

O ID do Destino geralmente é o destinatário real desta mensagem.
No entanto, para AppendEntriesResponse, AddServerResponse e RemoveServerResponse,
é o ID do líder atual.

Na RequestVoteResponse, É Aceito é 1 para um voto ao candidato (solicitante),
e 0 para nenhum voto.


## Camada de Aplicação

Cada Servidor publica periodicamente dados de Aplicação no log em uma ClientRequest.
Os dados de aplicação contêm o status de cada Roteador do Servidor e o Destino
para o cluster Meta LS2.
Os servidores usam um algoritmo comum para determinar o publicador e o conteúdo
do Meta LS2.
O servidor com o status mais "bom" recente no log é o publicador do Meta LS2.
O publicador do Meta LS2 NÃO é necessariamente o Líder Raft.


### Conteúdo dos Dados de Aplicação

Os conteúdos da aplicação são codificados em UTF-8 [JSON](https://json.org/),
por simplicidade e extensibilidade.
A especificação completa está por definir.
O objetivo é fornecer dados suficientes para escrever um algoritmo que determine o
roteador "melhor" para publicar o Meta LS2, e para que o publicador tenha informações suficientes
para ponderar os Destinos no Meta LS2.
Os dados conterão estatísticas tanto do roteador quanto dos Destinos.

Os dados podem opcionalmente conter dados de sensoriamento remoto sobre a saúde dos
outros servidores e a capacidade de buscar o Meta LS.
Esses dados não seriam suportados na primeira versão.

Os dados podem opcionalmente conter informações de configuração publicadas
por um cliente administrador.
Esses dados não seriam suportados na primeira versão.

Se "nome: valor" for listado, isso especifica a chave e o valor do mapa JSON.
Caso contrário, a especificação está por definir.


Dados do cluster (nível superior):

- cluster: Nome do cluster
- date: Data desses dados (longo, ms desde a época)
- id: ID Raft (inteiro)

Dados de configuração (config):

- Quaisquer parâmetros de configuração

Status de publicação do MetaLS (meta):

- destination: o destino do metals, base64
- lastPublishedLS: se presente, codificação base64 do último metals publicado
- lastPublishedTime: em ms, ou 0 se nunca
- publishConfig: status da configuração do publicador: desligado/ligado/auto
- publishing: status booleano do publicador do metals verdadeiro/falso

Dados do roteador (router):

- lastPublishedRI: se presente, codificação base64 da última informação do roteador publicada
- uptime: Tempo de atividade em ms
- Atraso de tarefas
- Túneis exploratórios
- Túneis participantes
- Largura de banda configurada
- Largura de banda atual

Destinos (destinations):
Lista

Dados do destino:

- destination: o destino, base64
- uptime: Tempo de atividade em ms
- Túneis configurados
- Túneis atuais
- Largura de banda configurada
- Largura de banda atual
- Conexões configuradas
- Conexões atuais
- Dados da lista negra

Dados de sensoriamento de roteador remoto:

- Última versão do RI vista
- Tempo de busca do LS
- Dados do teste de conexão
- Dados do perfil dos floodfills mais próximos
  para os períodos ontem, hoje e amanhã

Dados de sensoriamento de destino remoto:

- Última versão do LS vista
- Tempo de busca do LS
- Dados do teste de conexão
- Dados do perfil dos floodfills mais próximos
  para os períodos ontem, hoje e amanhã

Dados de sensoriamento do Meta LS:

- Última versão vista
- Tempo de busca
- Dados do perfil dos floodfills mais próximos
  para os períodos ontem, hoje e amanhã


## Interface de Administração

Por definir, possivelmente uma proposta separada.
Não é necessário para a primeira versão.

Requisitos de uma interface de administração:

- Suporte para múltiplos destinos mestres, ou seja, múltiplos clusters virtuais (farms)
- Fornecer visão abrangente do estado compartilhado do cluster - todas as estatísticas publicadas pelos membros, quem é o líder atual, etc.
- Capacidade de forçar a remoção de um participante ou líder do cluster
- Capacidade de forçar a publicação do metaLS (se o nó atual for o publicador)
- Capacidade de excluir hashes do metaLS (se o nó atual for o publicador)
- Funcionalidade de importação/exportação de configuração para implantações em massa



## Interface do Roteador

Por definir, possivelmente uma proposta separada.
O i2pcontrol não é necessário para a primeira versão e mudanças detalhadas serão incluídas em uma proposta separada.

Requisitos para a API Garlic Farm para roteador (java in-JVM ou i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // provavelmente não no MVP
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // ou MetaLeaseSet assinado? Quem assina?
- stopPublishingMetaLS(Hash masterHash)
- autenticação por definir?


## Justificativa

O Atomix é muito grande e não permitirá personalização para rotear
o protocolo sobre o I2P. Além disso, seu formato de rede é indocumentado e depende
de serialização Java.


## Notas



## Problemas

- Não há maneira de um cliente descobrir e se conectar a um líder desconhecido.
  Seria uma mudança mínima para um Seguidor enviar a Configuração como uma Entrada de Log na AppendEntriesResponse.



## Migração

Sem problemas de compatibilidade com versões anteriores.


## Referências

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)

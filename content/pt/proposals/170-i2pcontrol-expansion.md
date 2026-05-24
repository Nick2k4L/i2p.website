---
title: "Expansão do I2PControl"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Abrir"
toc: true
---

## Visão Geral

Esta proposta expõe novas informações para a API i2pcontrol, permitindo maior flexibilidade. Essas informações incluem: adicionar, excluir, recuperar e modificar livros de endereços e serviços ocultos. Esta proposta também expõe mais informações sobre seu roteador, como pares, notícias, netDb e mais.

## Motivação

O caso de uso para esta proposta é a criação de um console de roteador unificado e simplificado que possa ser compartilhado entre todas as implementações de roteador com o conjunto padrão de túneis i2p. Essencialmente, esta proposta permite uma experiência mais intuitiva e amigável para os usuários em toda a rede I2P.

Esta proposta também permitirá maior flexibilidade na API do I2P para que aplicações possam implementar e gerenciar uma interface administrativa do I2P. Expor tais informações ao i2pcontrol permite que os usuários criem aplicações mais avançadas e ofereçam melhor suporte para gerenciamento remoto.

## Design

Quando os usuários interagirem com a API i2pcontrol, poderão acessar novos endpoints que fornecem as informações mencionadas acima. Por exemplo, a API i2pcontrol exporá novos métodos `TunnelManager` e `AddressBook` que permitirão aos usuários inserir parâmetros para criar, excluir, recuperar e modificar túneis e livros de endereços. Além disso, o método preexistente `RouterInfo` terá novos parâmetros para expor informações sobre o roteador.

## Implicações de segurança

Não há implicações de segurança adicionais esperadas a partir desta proposta, pois as informações expostas já são acessíveis por outros meios. No entanto, é importante garantir que mecanismos adequados de autenticação e autorização estejam em vigor para acessar a API i2pcontrol, a fim de evitar acesso não autorizado a informações sensíveis ou controle sobre o roteador.

## Especificação da API e Métodos

Todas as solicitações seguem a estrutura JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
### Método - RouterInfo (GETTERS)

Abaixo estão os novos parâmetros do método `RouterInfo` e o que eles retornam:

- `i2p.router.news` - retorna todas as entradas de notícias do roteador. Tipo de retorno - `String`
- `i2p.router.id` - retorna o hash do roteador como uma string Base64, ou `null`. Tipo de retorno - `String`
- `i2p.router.clockskew` - retorna a diferença média de relógio dos pares, ou `null`. Tipo de retorno - `long`
- `i2p.router.info` - retorna o RouterInfo serializado como uma string Base64, ou `null`. Tipo de retorno - `String`
- `i2p.router.logs` - retorna mensagens recentes do log do roteador. Tipo de retorno - `List<String>`
- `i2p.router.logs.clear` - limpa o buffer de log do roteador e retorna `"success"`. Tipo de retorno - `String`

- `i2p.router.net.total.received.bytes` - retorna o total de bytes recebidos desde a inicialização. *(adotado do i2pd)* Tipo de Retorno - `long`
- `i2p.router.net.total.sent.bytes` - retorna o total de bytes enviados desde a inicialização. *(adotado do i2pd)* Tipo de Retorno - `long`
- `i2p.router.net.total.transit.bytes` - retorna o total de bytes em trânsito encaminhados desde a inicialização. *(adotado do i2pd)* Tipo de Retorno - `long`
- `i2p.router.net.bw.transit.15s` - retorna a largura de banda média de trânsito nos últimos 15 segundos (bytes/seg). *(adotado do i2pd)* Tipo de Retorno - `long`

- `i2p.router.net.tunnels.shareratio` - retorna a taxa de compartilhamento de túneis. Tipo de retorno - `double`
- `i2p.router.net.tunnels.participating.info` - retorna informações sobre túneis participantes. Tipo de retorno - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.i2ptunnel` - retorna informações do controlador I2PTunnel configurado (estatísticas rápidas de todos). Tipo de retorno - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.exploratory.inbound` - retorna a quantidade de túneis exploratórios de entrada. Tipo de retorno - `int`
- `i2p.router.net.tunnels.exploratory.outbound` - retorna a quantidade de túneis exploratórios de saída. Tipo de retorno - `int`
- `i2p.router.net.tunnels.exploratory.info.list` - retorna a lista de informações de túneis exploratórios. Tipo de retorno - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.client.inbound` - retorna a quantidade de túneis cliente de entrada. Tipo de retorno - `int`
- `i2p.router.net.tunnels.client.outbound` - retorna a quantidade de túneis cliente de saída. Tipo de retorno - `int`
- `i2p.router.net.tunnels.client.info.list` - retorna a lista de informações de túneis cliente. Tipo de retorno - `List<Map<String, Object>>`

- `i2p.router.net.status.v6` - retorna o código de status da rede IPv6. *(adotado do i2pd)* Tipo de Retorno - `int`
- `i2p.router.net.error` - retorna o código de erro da rede IPv4. *(adotado do i2pd)* Tipo de Retorno - `int`
- `i2p.router.net.error.v6` - retorna o código de erro da rede IPv6. *(adotado do i2pd)* Tipo de Retorno - `int`
- `i2p.router.net.testing` - retorna se a rede IPv4 está em estado de teste (0 ou 1). *(adotado do i2pd)* Tipo de Retorno - `int`
- `i2p.router.net.testing.v6` - retorna se a rede IPv6 está em estado de teste (0 ou 1). *(adotado do i2pd)* Tipo de Retorno - `int`

- `i2p.router.net.tunnels.successrate` - retorna a taxa de sucesso recente na criação de túneis (%). *(adotado do i2pd)* Tipo de Retorno - `double`
- `i2p.router.net.tunnels.totalsuccessrate` - retorna a taxa total de sucesso na criação de túneis desde a inicialização (%). *(adotado do i2pd)* Tipo de Retorno - `double`
- `i2p.router.net.tunnels.queue` - retorna o tamanho da fila de solicitações de criação de túneis. *(adotado do i2pd)* Tipo de Retorno - `int`
- `i2p.router.net.tunnels.tbmqueue` - retorna o tamanho da fila de mensagens de construção de túneis (Tunnel Build Message). *(adotado do i2pd)* Tipo de Retorno - `int`

- `i2p.router.netdb.peers` - retorna uma lista de hashes de pares conhecidos. Tipo de Retorno - `List<String>`
- `i2p.router.netdb.activepeers.info` - retorna dados serializados do RouterInfo para pares ativos. Tipo de Retorno - `List<String>`
- `i2p.router.netdb.ntcp.limit` - retorna o limite de conexões NTCP. Tipo de Retorno - `int`
- `i2p.router.netdb.ssu.limit` - retorna o limite de conexões SSU. Tipo de Retorno - `int`
- `i2p.router.netdb.bannedpeers` - retorna os pares banidos com detalhes do banimento. Tipo de Retorno - `Map<String, Map<String, Object>>`
- `i2p.router.netdb.activepeers.list` - retorna os hashes dos pares ativos. Tipo de Retorno - `List<String>`
- `i2p.router.netdb.peers.list` - retorna os hashes dos pares conhecidos. Tipo de Retorno - `List<String>`
- `i2p.router.netdb.peers.info` - retorna dados serializados do RouterInfo para pares conhecidos. Tipo de Retorno - `List<String>`
- `i2p.router.netdb.activepeers.stats` - retorna estatísticas dos pares ativos. Tipo de Retorno - `List<Map<String, Object>>`

- `i2p.router.addressbook.private.list` - retorna entradas da agenda privada. Tipo de Retorno - `List<Map<String, String>>`
- `i2p.router.addressbook.local.list` - retorna entradas da agenda local. Tipo de Retorno - `List<Map<String, String>>`
- `i2p.router.addressbook.router.list` - retorna entradas da agenda do roteador. Tipo de Retorno - `List<Map<String, String>>`
- `i2p.router.addressbook.published.list` - retorna entradas da agenda publicada. Tipo de Retorno - `List<Map<String, String>>`
- `i2p.router.addressbook.subscriptions` - retorna o caminho do arquivo de inscrição e suas entradas. Tipo de Retorno - `Map<String, Object>`
- `i2p.router.addressbook.config` - retorna o caminho do arquivo de configuração da agenda e suas entradas. Tipo de Retorno - `Map<String, Object>`

Exemplo:

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
Retorno:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
### Método - Catálogo de Endereços (DEFINIDORES)

Para o método `AddressBook`, são necessários três parâmetros/argumentos para excluir e adicionar entradas na agenda de endereços:

- `Type` - corresponde ao tipo da agenda de endereços:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - corresponde ao nome do host ou nome de domínio associado à entrada na agenda de endereços.
- `Destination` - corresponde à destino associado à entrada na agenda de endereços.
- `Delete` - este parâmetro é opcional e é usado para excluir uma entrada da agenda de endereços. Se este parâmetro não for fornecido, o método adicionará uma nova entrada à agenda de endereços.

Exemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Para editar AddressBookSubscriptions:

- `SetSubscriptions` - este parâmetro é usado para definir as assinaturas de uma entrada na agenda. Ele aceita uma lista de strings como argumento.

Exemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Para editar o AddressBookConfig:

- `SetConfig` - este parâmetro é usado para definir a configuração de uma entrada na agenda de endereços.

Recebe um objeto JSON como argumento, que contém as configurações de configuração.

Parâmetros de configuração disponíveis/comuns:

- `subscriptions` - arquivo contendo a lista de URLs de assinatura.
- `update_delay` - intervalo de atualização em horas.
- `published_addressbook` - caminho para a agenda publicada.
- `router_addressbook` - caminho para a agenda do roteador.
- `local_addressbook` - caminho para a agenda local.
- `private_addressbook` - caminho para a agenda privada.
- `proxy_port` - porta do eepProxy.
- `proxy_host` - nome do host do eepProxy.
- `should_publish` - indica se a agenda publicada deve ser atualizada.
- `etags` - arquivo contendo as etags das URLs de assinatura.
- `last_modified` - arquivo contendo os carimbos de data/hora do último modificado das URLs de assinatura.
- `log` - caminho do arquivo de log.
- `theme` - tema.

Exemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
### Método - TunnelManager (1 GETTER MARCADO, RESTANTE SETTERS)

O método `TunnelManager` é usado para criar, editar, obter, iniciar, parar, reiniciar e excluir controladores de I2PTunnel.

Parâmetros obrigatórios:

- `Name` - nome do túnel. Este é o identificador do túnel.
- `Action` - ação a ser realizada:
  - `create`
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

Parâmetros opcionais:

- `All` - booleano, se deve aplicar a ação a todos os túneis. Isso é válido apenas para as ações `start`, `stop` e `restart`.

Tipos de túnel suportados para `create`:

- `client`
- `httpclient`
- `ircclient`
- `socks`
- `socksirc`
- `connectclient`
- `streamrclient`

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

Parâmetros comuns para criar/editar túneis:

- `Type` - tipo do túnel. Obrigatório para `create`.
- `NewName` - nome novo opcional ao editar.
- `Port` - porta local de escuta.
- `TargetHost` ou `Host` - host de destino para túneis servidor.
- `TargetPort` - porta de destino para túneis servidor.
- `TargetDestination` ou `Destination` - destino para túneis cliente que exigem um.
- `StartOnLoad` - booleano, indica se o túnel deve iniciar ao ser carregado.
- `Description` - descrição do túnel.
- `ReachableBy` - interface/endereço no qual o túnel escuta.
- `Shared` - booleano, indica se o túnel cliente deve ser compartilhado.
- `UseSSL` - booleano, ativa SSL onde for suportado.
- `TunnelLength` - comprimento do túnel, de `0` a `3`.
- `TunnelVariance` - variação do túnel, de `-2` a `2`.
- `TunnelQuantity` - quantidade de túneis, de `1` a `6`.
- `TunnelBackupQuantity` - quantidade de túneis de backup, de `0` a `3`.
- `SigType` - tipo de chave de assinatura.
- `EncType` - tipo de criptografia.
- `CustomOptions` - opções personalizadas do túnel.

Opções de proxy do cliente:

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

Opções de gerenciamento de cliente:

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

Opções de filtragem de cliente HTTP:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Opções do servidor:

- `WebsiteHostname` ou `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

Opções de LeaseSet:

- `EncryptLeaseSet` - um dos seguintes:
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

Criar exemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
Exemplo de edição:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Obter exemplo (APENAS GETTER) Retorna - `Map<String, Object>` (informação) e `String` (status):

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
Exemplos de Iniciar, Parar, Reiniciar, Excluir. Eles seguem a mesma estrutura, apenas com parâmetros `Action` diferentes:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
### Método - ClientServicesInfo *(adotado do i2pd)*

O método `ClientServicesInfo` retorna informações de status sobre os serviços clientes em execução no roteador. Inclua as chaves de serviço desejadas (com qualquer valor) em `params` para solicitar o status de cada serviço.

Parâmetros suportados:

- `I2PTunnel` - retorna um mapa dos nomes dos túneis configurados para seus endereços, dividido em subobjetos `client` e `server`.
- `HTTPProxy` - retorna o estado de ativação do proxy HTTP e seu endereço.
- `SOCKS` - retorna o estado de ativação do proxy SOCKS e seu endereço.
- `SAM` - retorna o estado de ativação da ponte SAM e informações sobre sessões ativas.
- `BOB` - retorna o estado de ativação da ponte BOB. (Obsoleto no Java I2P; sempre retorna `false`.)
- `I2CP` - retorna o estado de ativação do servidor I2CP.

Exemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
Retorno:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
## Compatibilidade

A compatibilidade com a API i2pcontrol existente deve ser mantida, já que os novos métodos e parâmetros são adicionados de forma que não interfira com a funcionalidade existente. Aplicativos existentes que utilizam a API i2pcontrol devem continuar funcionando sem modificações, enquanto novos aplicativos podem aproveitar as informações e capacidades adicionais fornecidas por esta proposta.

## Implementação

### Java I2P

Esta proposta ainda não foi implementada no Java I2P, mas o código está disponível no repositório [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) sob a solicitação de pull [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6). Isso foi feito para permitir testes e desenvolvimento dos novos métodos sem afetar o código existente. Isso será atualizado no repositório principal do I2P, no diretório i2pcontrol, assim que o código estiver pronto para uso em produção.

### i2pd

Métodos e parâmetros marcados como "(adotados do i2pd)" são implementados no i2pd e permanecem inalterados nesta proposta. As extensões do i2pd não exigirão modificações como parte desta proposta. Partes não marcadas desta proposta não estão implementadas no i2pd.

### go-i2p

O go-i2p tem interesse em seguir esta proposta para habilitar e aprimorar seu aplicativo de console do roteador. Ele adotará e implementará a proposta no futuro.

### emissary

A probabilidade de adoção no Emissary é desconhecida no momento, porém o Emissary provavelmente se beneficiará desta proposta da mesma forma que o go-i2p.

## Desempenho

Não se espera impacto no desempenho.

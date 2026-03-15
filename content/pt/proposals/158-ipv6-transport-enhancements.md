---
title: "Melhorias no Transporte IPv6"
aliases:
  - "/pt/spec/proposals/158"
  - "/pt/spec/proposals/158/"
number: "158"
author: "zzz, original"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Fechado"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## Nota
Implantação e testes na rede em andamento.
Sujeito a revisões menores.


## Visão Geral

Esta proposta tem como objetivo implementar aprimoramentos nos transportes SSU e NTCP2 para IPv6.


## Motivação

À medida que o IPv6 cresce ao redor do mundo e configurações exclusivas de IPv6 (especialmente em dispositivos móveis) se tornam mais comuns,
precisamos melhorar nosso suporte ao IPv6 e remover as suposições de que
todos os roteadores são compatíveis com IPv4.



### Verificação de Conectividade

Ao selecionar pares para túneis, ou ao escolher caminhos OBEP/IBGW para rotear mensagens,
é útil calcular se o roteador A pode se conectar ao roteador B.
Em geral, isso significa determinar se A possui capacidade de saída para um transporte e tipo de endereço (IPv4/v6)
que corresponda a um dos endereços de entrada anunciados por B.

No entanto, em muitos casos não conhecemos as capacidades de A e precisamos fazer suposições.
Se A estiver oculto ou atrás de um firewall, os endereços não são publicados e não temos conhecimento direto –
portanto, assumimos que é compatível com IPv4, mas não com IPv6.
A solução é adicionar duas novas "caps" ou capacidades ao Router Info para indicar a capacidade de saída para IPv4 e IPv6.


### Introducers IPv6

Nossas especificações para SSU contêm erros e inconsistências sobre se
introducers IPv6 são suportados para introduções IPv4.
De qualquer forma, isso nunca foi implementado nem no Java I2P nem no i2pd.
Isso precisa ser corrigido.


### Introduções IPv6

Nossas especificações para SSU deixam claro que
introduções IPv6 não são suportadas.
Isso foi baseado na suposição de que o IPv6 nunca é bloqueado por firewall.
Isso claramente não é verdade, e precisamos melhorar o suporte a roteadores IPv6 atrás de firewall.


### Diagramas de Introdução

Legenda: ----- é IPv4, ====== é IPv6

**Atual, somente IPv4:**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Introdução IPv4, introducer IPv6:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Introdução IPv6, introducer IPv6:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**Introdução IPv6, introducer IPv4:**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```


## Projeto

Três alterações devem ser implementadas.

- Adicionar capacidades "4" e "6" às capacidades do endereço do roteador para indicar suporte de saída IPv4 e IPv6
- Adicionar suporte para introduções IPv4 via introducers IPv6
- Adicionar suporte para introduções IPv6 via introducers IPv4 e IPv6



## Especificação

### Caps 4/6

Isso foi originalmente implementado sem uma proposta formal, mas é necessário para
introduções IPv6, portanto o incluímos aqui.


Duas novas capacidades "4" e "6" são definidas.
Essas novas capacidades serão adicionadas à propriedade "caps" no Endereço do Roteador, não nas caps do Router Info.
Atualmente não temos uma propriedade "caps" definida para NTCP2.
Um endereço SSU com introducers é, por definição, ipv4 no momento. Não suportamos introdução ipv6 de forma alguma.
No entanto, esta proposta é compatível com introduções IPv6. Veja abaixo.

Além disso, um roteador pode suportar conectividade via uma rede sobreposta como I2P-over-Yggdrasil,
mas não deseja publicar um endereço, ou esse endereço não possui um formato IPv4 ou IPv6 padrão.
Esse novo sistema de capacidades deve ser flexível o suficiente para suportar essas redes também.

Definimos as seguintes alterações:

NTCP2: Adicionar propriedade "caps"

SSU: Adicionar suporte para um Endereço de Roteador sem host ou introducers, para indicar suporte de saída
para IPv4, IPv6 ou ambos.

Ambos os transportes: Definir os seguintes valores de caps:

- "4": suporte IPv4
- "6": suporte IPv6

Vários valores podem ser suportados em um único endereço. Veja abaixo.
Pelo menos um desses caps é obrigatório se nenhum valor "host" estiver incluído no Endereço do Roteador.
No máximo um desses caps é opcional se um valor "host" estiver incluído no Endereço do Roteador.
Caps de transporte adicionais podem ser definidos no futuro para indicar suporte a redes sobrepostas ou outra conectividade.


#### Casos de uso e exemplos

SSU:

SSU com host: 4/6 opcional, nunca mais de um.
Exemplo: SSU caps="4" host="1.2.3.4" key=... port="1234"

SSU somente saída para um, outro publicado: Apenas caps, 4/6.
Exemplo: SSU caps="6"

SSU com introducers: nunca combinado. 4 ou 6 é obrigatório.
Exemplo: SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

SSU oculto: Apenas caps, 4, 6 ou 46. Múltiplos são permitidos.
Não há necessidade de dois endereços, um com 4 e outro com 6.
Exemplo: SSU caps="46"

NTCP2:

NTCP2 com host: 4/6 opcional, nunca mais de um.
Exemplo: NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

NTCP2 somente saída para um, outro publicado: Apenas caps, s, v, 4/6/y, múltiplos permitidos.
Exemplo: NTCP2 caps="6" i=... s=... v="2"

NTCP2 oculto: Apenas caps, s, v, 4/6, múltiplos permitidos. Não há necessidade de dois endereços, um com 4 e outro com 6.
Exemplo: NTCP2 caps="46" i=... s=... v="2"



### Introducers IPv6 para IPv4

As seguintes alterações são necessárias para corrigir erros e inconsistências nas especificações.
Também descrevemos isso como "parte 1" da proposta.

#### Alterações na Especificação

A especificação SSU atual diz (notas IPv6):

IPv6 é suportado a partir da versão 0.9.8. Endereços de retransmissão publicados podem ser IPv4 ou IPv6, e a comunicação Alice-Bob pode ser via IPv4 ou IPv6.

Adicionar o seguinte:

Embora a especificação tenha sido alterada a partir da versão 0.9.8, a comunicação Alice-Bob via IPv6 não foi realmente suportada até a versão 0.9.50.
Versões anteriores de roteadores Java publicaram erroneamente a capacidade 'C' para endereços IPv6,
mesmo que não atuassem como introducer via IPv6.
Portanto, roteadores devem confiar na capacidade 'C' em um endereço IPv6 apenas se a versão do roteador for 0.9.50 ou superior.



A especificação SSU atual diz (Solicitação de Retransmissão):

O endereço IP é incluído apenas se for diferente do endereço de origem e porta do pacote.
Na implementação atual, o comprimento do IP é sempre 0 e a porta é sempre 0,
e o destinatário deve usar o endereço de origem e porta do pacote.
Esta mensagem pode ser enviada via IPv4 ou IPv6. Se IPv6, Alice deve incluir seu endereço e porta IPv4.

Adicionar o seguinte:

O IP e a porta devem ser incluídos para introduzir um endereço IPv4 ao enviar esta mensagem via IPv6.
Isso é suportado a partir da versão 0.9.50.



### Introduções IPv6

Todas as três mensagens de retransmissão SSU (RelayRequest, RelayResponse e RelayIntro) contêm campos de comprimento IP
para indicar o comprimento do endereço IP (de Alice, Bob ou Charlie) a seguir.

Portanto, nenhuma alteração no formato das mensagens é necessária.
Apenas alterações textuais nas especificações, indicando que endereços IP de 16 bytes são permitidos.

As seguintes alterações são necessárias nas especificações.
Também descrevemos isso como "parte 2" da proposta.


#### Alterações na Especificação

A especificação SSU atual diz (notas IPv6):

A comunicação Bob-Charlie e Alice-Charlie é somente via IPv4.

A especificação SSU atual diz (Solicitação de Retransmissão):

Não há planos para implementar retransmissão para IPv6.

Alterar para dizer:

A retransmissão para IPv6 é suportada a partir da versão 0.9.xx

A especificação SSU atual diz (Resposta de Retransmissão):

O endereço IP de Charlie deve ser IPv4, pois é o endereço para o qual Alice enviará o SessionRequest após o Hole Punch.
Não há planos para implementar retransmissão para IPv6.

Alterar para dizer:

O endereço IP de Charlie pode ser IPv4 ou, a partir da versão 0.9.xx, IPv6.
Esse é o endereço para o qual Alice enviará o SessionRequest após o Hole Punch.
A retransmissão para IPv6 é suportada a partir da versão 0.9.xx

A especificação SSU atual diz (Introdução de Retransmissão):

O endereço IP de Alice tem sempre 4 bytes na implementação atual, porque Alice está tentando se conectar a Charlie via IPv4.
Esta mensagem deve ser enviada via uma conexão IPv4 estabelecida,
pois é a única maneira de Bob conhecer o endereço IPv4 de Charlie para retornar a Alice na RelayResponse.

Alterar para dizer:

Para IPv4, o endereço IP de Alice tem sempre 4 bytes, porque Alice está tentando se conectar a Charlie via IPv4.
A partir da versão 0.9.xx, o IPv6 é suportado, e o endereço IP de Alice pode ter 16 bytes.

Para IPv4, esta mensagem deve ser enviada via uma conexão IPv4 estabelecida,
pois é a única maneira de Bob conhecer o endereço IPv4 de Charlie para retornar a Alice na RelayResponse.
A partir da versão 0.9.xx, o IPv6 é suportado, e esta mensagem pode ser enviada via uma conexão IPv6 estabelecida.

Adicionar também:

A partir da versão 0.9.xx, qualquer endereço SSU publicado com introducers deve conter "4" ou "6" na opção "caps".


## Migração

Todos os roteadores antigos devem ignorar a propriedade caps no NTCP2 e caracteres de capacidade desconhecidos na propriedade caps do SSU.

Qualquer endereço SSU com introducers que não contenha uma cap "4" ou "6" será assumido como sendo para introdução IPv4.


## Referências

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)

---
title: "Proposta I2P nº 166: Tipos de Túneis Conscientes de Identidade/Host"
number: "166"
author: "eyedeekay"
created: "2024-05-27"
lastupdated: "2024-08-27"
status: "Open"
thread: "http://i2pforum.i2p/viewforum.php?f=13"
target: "0.9.65"
toc: true
---
### Proposta para um Tipo de Túnel HTTP Proxy Ciente de Host

Esta é uma proposta para resolver o "Problema de Identidade Compartilhada" no uso convencional de HTTP-sobre-I2P, introduzindo um novo tipo de túnel HTTP Proxy. Esse tipo de túnel possui comportamento suplementar destinado a prevenir ou limitar a utilidade de rastreamento conduzido por operadores potencialmente hostis de serviços ocultos, contra agentes de usuário direcionados (navegadores) e a própria Aplicação Cliente I2P.

#### O que é o problema de "Identidade Compartilhada"?

O problema de "Identidade Compartilhada" ocorre quando um agente de usuário em uma rede sobreposta com endereçamento criptográfico compartilha uma identidade criptográfica com outro agente de usuário. Isso ocorre, por exemplo, quando um Firefox e o GNU Wget estão ambos configurados para usar o mesmo Proxy HTTP.

Nesse cenário, é possível que o servidor colete e armazene o endereço criptográfico (Destination) usado para responder à atividade. Ele pode tratar isso como uma "impressão digital" que é sempre 100% única, porque tem origem criptográfica. Isso significa que a vinculação observada pelo problema de Identidade Compartilhada é perfeita.

Mas é um problema?
^^^^^^^^^^^^^^^^^^^^

O problema de identidade compartilhada é um problema quando agentes de usuário que usam o mesmo protocolo desejam unlinkabilidade. [Foi mencionado pela primeira vez no contexto de HTTP nesta thread do Reddit](https://old.reddit.com/r/i2p/comments/579idi/warning_i2p_is_linkablefingerprintable/), com os comentários excluídos acessíveis graças ao [pullpush.io](https://api.pullpush.io/reddit/search/comment/?link_id=579idi). *Na época*, eu era um dos respondentes mais ativos, e *na época* eu acreditava que o problema era pequeno. Nos últimos 8 anos, a situação e minha opinião sobre ela mudaram; agora acredito que a ameaça representada pela correlação maliciosa de destinos aumenta consideravelmente à medida que mais sites ficam em posição de "perfilizar" usuários específicos.

Este ataque tem uma barreira de entrada muito baixa. Requer apenas que um operador de serviço oculto opere múltiplos serviços. Para ataques em visitas contemporâneas (visitar múltiplos sites ao mesmo tempo), este é o único requisito. Para vinculação não contemporânea, um desses serviços deve ser um serviço que hospede "contas" pertencentes a um único usuário que é alvo de rastreamento.

Atualmente, qualquer operador de serviço que hospede contas de usuário poderá correlacioná-las com atividades em todos os sites que controla explorando o problema de Identidade Compartilhada. Mastodon, Gitlab ou até fóruns simples poderiam ser atacantes disfarçados, desde que operem mais de um serviço e tenham interesse em criar um perfil para um usuário. Essa vigilância poderia ser conduzida por motivos de perseguição, ganho financeiro ou relacionados a inteligência. Atualmente existem dezenas de grandes operadores que poderiam realizar esse ataque e obter dados significativos com ele. Até agora confiamos principalmente neles para não fazê-lo, mas atores que não se importam com nossas opiniões poderiam facilmente surgir.

Isso está diretamente relacionado a uma forma bastante básica de construção de perfil na web clara, onde organizações podem correlacionar interações em seus sites com interações em redes que controlam. No I2P, como o destino criptográfico é único, essa técnica pode às vezes ser ainda mais confiável, embora sem o poder adicional da geolocalização.

A Identidade Compartilhada não é útil contra um usuário que usa o I2P apenas para ofuscar a geolocalização. Também não pode ser usada para quebrar o roteamento do I2P. É apenas um problema de gerenciamento de identidade contextual.

-  É impossível usar o problema de Identidade Compartilhada para geolocalizar um usuário I2P.
-  É impossível usar o problema de Identidade Compartilhada para vincular sessões I2P se elas não forem contemporâneas.

No entanto, é possível usá-lo para degradar o anonimato de um usuário I2P em circunstâncias que provavelmente são muito comuns. Uma razão pela qual são comuns é porque incentivamos o uso do Firefox, um navegador que suporta operação com "abas".

-  É *sempre* possível produzir uma impressão digital a partir do problema de Identidade Compartilhada em *qualquer* navegador que suporte solicitação de recursos de terceiros.
-  Desativar o Javascript não faz **nada** contra o problema de Identidade Compartilhada.
-  Se um vínculo puder ser estabelecido entre sessões não contemporâneas, como por meio de "impressão digital" tradicional do navegador, então a Identidade Compartilhada pode ser aplicada transitivamente, potencialmente habilitando uma estratégia de vinculação não contemporânea.
-  Se um vínculo puder ser estabelecido entre uma atividade na clearnet e uma identidade I2P, por exemplo, se o alvo estiver logado em um site com presença tanto no I2P quanto na clearnet em ambos os lados, a Identidade Compartilhada pode ser aplicada transitivamente, potencialmente habilitando a desanonimização completa.

A forma como você avalia a gravidade do problema de Identidade Compartilhada no que se refere ao proxy HTTP do I2P depende de onde você (ou mais precisamente, um "usuário" com expectativas potencialmente mal informadas) acredita que reside a "identidade contextual" para a aplicação. Existem várias possibilidades:

1. HTTP é tanto a Aplicação quanto a Identidade Contextual — É assim que funciona atualmente. Todas as Aplicações HTTP compartilham uma identidade.
2. O Processo é a Aplicação e a Identidade Contextual — É assim que funciona quando uma aplicação usa uma API como SAMv3 ou I2CP, onde uma aplicação cria sua identidade e controla seu tempo de vida.
3. HTTP é a Aplicação, mas o Host é a Identidade Contextual — Este é o objetivo desta proposta, que trata cada Host como uma possível "Aplicação Web" e trata a superfície de ataque como tal.

É Solucionável?
^^^^^^^^^^^^^^^

Provavelmente não é possível criar um proxy que responda inteligentemente a todos os casos possíveis em que sua operação possa enfraquecer o anonimato de uma aplicação. No entanto, é possível construir um proxy que responda inteligentemente a uma aplicação específica que se comporta de maneira previsível. Por exemplo, em navegadores web modernos, espera-se que os usuários tenham várias abas abertas, interagindo com múltiplos sites, que serão distinguidos pelo nome do host.

Isso nos permite melhorar o comportamento do Proxy HTTP para esse tipo de agente de usuário HTTP, fazendo com que o comportamento do proxy corresponda ao comportamento do agente de usuário, fornecendo a cada host seu próprio Destination ao usar o Proxy HTTP. Essa mudança torna impossível usar o problema de Identidade Compartilhada para derivar uma impressão digital que possa ser usada para correlacionar a atividade do cliente com 2 hosts, porque os 2 hosts simplesmente não compartilharão mais uma identidade de retorno.

Descrição:
^^^^^^^^^^^^

Um novo Proxy HTTP será criado e adicionado ao Gerenciador de Serviços Ocultos (I2PTunnel). O novo Proxy HTTP operará como um "multiplexador" de I2PSocketManagers. O próprio multiplexador não possui destino. Cada I2PSocketManager individual que se torna parte do multiplex possui seu próprio destino local e seu próprio pool de túneis. Os I2PSocketManagers são criados sob demanda pelo multiplexador, onde a "demanda" é a primeira visita a um novo host. É possível otimizar a criação dos I2PSocketManagers antes de inseri-los no multiplexador criando um ou mais com antecedência e armazenando-os fora do multiplexador. Isso pode melhorar o desempenho.

Um I2PSocketManager adicional, com seu próprio destino, é configurado como transportador de um "Outproxy" para qualquer site que *não* tenha um Destino I2P, por exemplo, qualquer site da Clearnet. Isso efetivamente torna todo o uso de Outproxy uma única Identidade Contextual, com a ressalva de que configurar múltiplos Outproxys para o túnel causará a rotação "Sticky" normal do outproxy, onde cada outproxy recebe apenas solicitações de um único site. Este é *quase* o comportamento equivalente ao isolamento de proxies HTTP-sobre-I2P por destino, na internet clara.

Considerações de Recursos:
''''''''''''''''''''''''

O novo proxy HTTP exige recursos adicionais em comparação com o proxy HTTP existente. Ele irá:

-  Potencialmente construir mais túneis e I2PSocketManagers
-  Construir túneis com mais frequência

Cada um desses requer:

-  Recursos computacionais locais
-  Recursos de rede dos pares

Configurações:
'''''''''''''''

A fim de minimizar o impacto do aumento no uso de recursos, o proxy deve ser configurado para usar o mínimo possível. Proxies que fazem parte do multiplex (não o proxy pai) devem ser configurados para:

-  I2PSocketManagers multiplexados construírem 1 túnel de entrada e 1 túnel de saída em seus pools de túneis
-  I2PSocketManagers multiplexados usarem 3 saltos por padrão
-  Fecharem sockets após 10 minutos de inatividade
-  I2PSocketManagers iniciados pelo Multiplexador compartilharem o tempo de vida do Multiplexador. Túneis multiplexados não são "Destruídos" até que o Multiplexador pai o seja.

Diagramas:
^^^^^^^^^

O diagrama abaixo representa a operação atual do proxy HTTP, que corresponde à "Possibilidade 1." na seção "É um problema?". Como você pode ver, o proxy HTTP interage com sites I2P diretamente usando apenas um destino. Nesse cenário, HTTP é tanto a aplicação quanto a identidade contextual.

```text
**Situação Atual: HTTP é a Aplicação, HTTP é a Identidade Contextual**
                                                      __-> Outproxy <-> i2pgit.org
                                                     /
Browser <-> HTTP Proxy(um Destination)<->I2PSocketManager <---> idk.i2p
                                                     \__-> translate.idk.i2p
                                                      \__-> git.idk.i2p
```

O diagrama abaixo representa a operação de um proxy HTTP ciente de host, que corresponde à "Possibilidade 3." na seção "É um problema?". Nesse cenário, HTTP é a aplicação, mas o Host define a identidade contextual, onde cada site I2P interage com um proxy HTTP diferente com um destino único por host. Isso impede que operadores de múltiplos sites possam distinguir quando a mesma pessoa está visitando múltiplos sites que eles operam.

```text
**Após a Mudança: HTTP é a Aplicação, Host é a Identidade Contextual**
                                                    __-> I2PSocketManager(Destination A - Apenas Outproxies) <--> i2pgit.org
                                                   /
Browser <-> HTTP Proxy Multiplexer(Sem Destination) <---> I2PSocketManager(Destination B) <--> idk.i2p
                                                   \__-> I2PSocketManager(Destination C) <--> translate.idk.i2p
                                                    \__-> I2PSocketManager(Destination C) <--> git.idk.i2p
```

Status:
^^^^^^^

Uma implementação Java funcional do proxy ciente de host que está de acordo com uma versão anterior desta proposta está disponível no fork do idk na branch: i2p.i2p.2.6.0-browser-proxy-post-keepalive. Link nas citações. Está sob revisão intensa, a fim de dividir as mudanças em seções menores.

Implementações com capacidades variadas foram escritas em Go usando a biblioteca SAMv3; elas podem ser úteis para incorporação em outras aplicações Go ou para o go-i2p, mas são inadequadas para o I2P Java. Além disso, elas carecem de bom suporte para trabalhar interativamente com leaseSets criptografados.

Apêndice: ``i2psocks``
                      

Uma abordagem simples orientada a aplicações para isolar outros tipos de clientes é possível sem implementar um novo tipo de túnel ou alterar o código I2P existente, combinando ferramentas existentes do I2PTunnel que já estão amplamente disponíveis e testadas na comunidade de privacidade. No entanto, essa abordagem faz uma suposição difícil que não é verdadeira para HTTP e também não é verdadeira para muitos outros tipos potenciais de clientes I2P.

Grosseiramente, o seguinte script produzirá um proxy SOCKS5 ciente de aplicação e socksificará o comando subjacente:

```sh
#! /bin/sh
command_to_proxy="$@"
java -jar ~/i2p/lib/i2ptunnel.jar -wait -e 'sockstunnel 7695'
torsocks --port 7695 $command_to_proxy
```

Apêndice: ``exemplo de implementação do ataque``
                                                  

[Um exemplo de implementação do ataque de Identidade Compartilhada em Agentes de Usuário HTTP](https://github.com/eyedeekay/colluding_sites_attack/) existe há vários anos. Um exemplo adicional está disponível no subdiretório ``simple-colluder`` do [repositório prop166 do idk](https://git.idk.i2p/idk/i2p.host-aware-proxy). Esses exemplos são deliberadamente projetados para demonstrar que o ataque funciona e exigiriam modificação (embora mínima) para serem transformados em um ataque real.

---
title: "Protocolo de Streaming"
description: "Transporte similar ao TCP usado pela maioria das aplicações I2P"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Visão Geral {#overview}

A biblioteca de streaming é tecnicamente parte da camada de "aplicação", pois não é uma função central do router. Na prática, no entanto, ela fornece uma função vital para quase todas as aplicações I2P existentes, ao fornecer streams semelhantes ao TCP sobre I2P, e permitindo que aplicações existentes sejam facilmente portadas para I2P. A outra biblioteca de transporte ponta-a-ponta para comunicação cliente é a [biblioteca de datagram](/docs/specs/datagrams).

A biblioteca de streaming é uma camada sobre a [API I2CP](/docs/specs/i2cp) principal que permite streams de mensagens confiáveis, ordenadas e autenticadas operarem através de uma camada de mensagens não confiável, desordenada e não autenticada. Assim como a relação TCP para IP, esta funcionalidade de streaming tem toda uma série de compensações e otimizações disponíveis, mas ao invés de incorporar essa funcionalidade no código base do I2P, ela foi separada em sua própria biblioteca tanto para manter as complexidades similares ao TCP separadas quanto para permitir implementações alternativas otimizadas.

Considerando o custo relativamente alto das mensagens, o protocolo da biblioteca de streaming para agendamento e entrega dessas mensagens foi otimizado para permitir que mensagens individuais transmitidas contenham o máximo de informações disponíveis. Por exemplo, uma pequena transação HTTP proxificada através da biblioteca de streaming pode ser completada em uma única ida e volta - as primeiras mensagens agrupam um SYN, FIN e a pequena carga útil da solicitação HTTP, e a resposta agrupa o SYN, FIN, ACK e a carga útil da resposta HTTP. Embora um ACK adicional deva ser transmitido para informar ao servidor HTTP que o SYN/FIN/ACK foi recebido, o proxy HTTP local frequentemente pode entregar a resposta completa ao navegador imediatamente.

A biblioteca de streaming tem muita semelhança com uma abstração do TCP, com suas janelas deslizantes, algoritmos de controle de congestionamento (tanto slow start quanto prevenção de congestionamento), e comportamento geral de pacotes (ACK, SYN, FIN, RST, cálculo de rto, etc).

A biblioteca de streaming é uma biblioteca robusta otimizada para operação sobre I2P. Ela tem uma configuração de uma fase e contém uma implementação completa de janelamento.

## API {#api}

A API da biblioteca de streaming fornece um paradigma de socket padrão para aplicações Java. A API [I2CP](/docs/specs/i2cp) de nível mais baixo fica completamente oculta, exceto que as aplicações podem passar [parâmetros I2CP](/docs/specs/i2cp#options) através da biblioteca de streaming, para serem interpretados pelo I2CP.

A interface padrão para a biblioteca de streaming é a aplicação usar o I2PSocketManagerFactory para criar um I2PSocketManager. A aplicação então solicita ao gerenciador de socket uma I2PSession, que irá causar uma conexão ao router via [I2CP](/docs/specs/i2cp). A aplicação pode então configurar conexões com um I2PSocket ou receber conexões com um I2PServerSocket.

Para um bom exemplo de uso, consulte o código do i2psnark.

### Opções e Padrões {#options}

As opções e valores padrão atuais estão listados abaixo. As opções são sensíveis a maiúsculas e minúsculas e podem ser definidas para todo o router, para um cliente específico, ou para um socket individual em uma base por conexão. Muitos valores são ajustados para desempenho HTTP sob condições típicas do I2P. Outras aplicações, como serviços peer-to-peer, são fortemente encorajadas a modificar conforme necessário, definindo as opções e passando-as através da chamada para I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts). Valores de tempo estão em ms.

Note que APIs de camada superior, como [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob), e [I2PTunnel](/docs/api/i2ptunnel), podem sobrescrever esses padrões com seus próprios padrões. Note também que muitas opções se aplicam apenas a servidores que estão escutando por conexões de entrada.

A partir da versão 0.9.1, a maioria das opções, mas não todas, podem ser alteradas em um gerenciador de socket ou sessão ativa. Consulte os javadocs para detalhes.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## Especificação do Protocolo {#spec}

[Veja a página de Especificação da Biblioteca de Streaming.](/docs/specs/streaming)

## Detalhes da Implementação {#implementation}

### Configuração {#setup}

O iniciador envia um pacote com a flag SYNCHRONIZE definida. Este pacote também pode conter os dados iniciais. O peer responde com um pacote com a flag SYNCHRONIZE definida. Este pacote também pode conter os dados de resposta iniciais.

O iniciador pode enviar pacotes de dados adicionais, até o tamanho da janela inicial, antes de receber a resposta SYNCHRONIZE. Esses pacotes também terão o campo send Stream ID definido como 0. Os destinatários devem armazenar em buffer os pacotes recebidos em streams desconhecidos por um curto período de tempo, pois eles podem chegar fora de ordem, antes do pacote SYNCHRONIZE.

### Seleção e Negociação de MTU {#mtu}

O tamanho máximo da mensagem (também chamado de MTU / MRU) é negociado para o valor mais baixo suportado pelos dois peers. Como as mensagens de tunnel são preenchidas até 1KB, uma seleção inadequada de MTU levará a uma grande quantidade de overhead. O MTU é especificado pela opção i2p.streaming.maxMessageSize. O MTU padrão atual de 1730 foi escolhido para se encaixar precisamente em duas mensagens I2NP tunnel de 1K, incluindo overhead para o caso típico.

Nota: Este é o tamanho máximo apenas da carga útil, não incluindo o cabeçalho.

Nota: Para conexões ECIES, que têm overhead reduzido, o MTU recomendado é 1812. O MTU padrão permanece 1730 para todas as conexões, independentemente do tipo de chave usado. Os clientes devem usar o mínimo dos MTU enviado e recebido, como de costume. Veja a proposta 155.

A primeira mensagem em uma conexão inclui um Destination de 387 bytes (típico) adicionado pela camada de streaming, e geralmente um LeaseSet de 898 bytes (típico), e chaves de sessão, empacotados na mensagem Garlic pelo router. (O LeaseSet e as chaves de sessão não serão empacotados se uma sessão ElGamal foi previamente estabelecida). Portanto, o objetivo de encaixar uma requisição HTTP completa em uma única mensagem I2NP de 1KB nem sempre é atingível. No entanto, a seleção do MTU, junto com a implementação cuidadosa de estratégias de fragmentação e agrupamento no processador gateway do tunnel, são fatores importantes na largura de banda da rede, latência, confiabilidade e eficiência, especialmente para conexões de longa duração.

### Integridade de Dados {#integrity}

A integridade dos dados é assegurada pelo checksum gzip CRC-32 implementado na [camada I2CP](/docs/specs/i2cp#format). Não há campo de checksum no protocolo de streaming.

### Encapsulamento de Pacotes {#encapsulation}

Cada pacote é enviado através do I2P como uma única mensagem (ou como um cravo individual em uma [Garlic Message](/docs/overview/garlic-routing)). O encapsulamento de mensagens é implementado nas camadas subjacentes [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np) e [tunnel message](/docs/specs/tunnel-message). Não há mecanismo delimitador de pacotes ou campo de comprimento de payload no protocolo de streaming.

### Atraso Opcional {#delay}

Os pacotes de dados podem incluir um campo de atraso opcional especificando o atraso solicitado, em ms, antes que o receptor deva confirmar o pacote. Os valores válidos são de 0 a 60000 inclusive. Um valor de 0 solicita uma confirmação imediata. Isso é apenas consultivo, e os receptores devem atrasar ligeiramente para que pacotes adicionais possam ser confirmados com uma única confirmação. Algumas implementações podem incluir um valor consultivo de (RTT medido / 2) neste campo. Para valores de atraso opcional diferentes de zero, os receptores devem limitar o atraso máximo antes de enviar uma confirmação para no máximo alguns segundos. Valores de atraso opcional maiores que 60000 indicam bloqueio, veja abaixo.

### Janelas de Transmissão/Recepção e Estrangulamento {#windows}

Os cabeçalhos TCP incluem a janela de recepção em bytes; no entanto, o protocolo de streaming não fornece uma forma de trocar o tamanho máximo da janela de recepção nem em bytes nem em pacotes. Existe apenas uma indicação simples de bloqueio/desbloqueio indicando que o buffer de recepção está cheio. Cada endpoint deve manter sua própria estimativa da janela de recepção da extremidade remota, seja em bytes ou pacotes. Note que um buffer de recepção pode transbordar em qualquer tamanho de janela se a aplicação cliente for lenta para esvaziar o buffer.

O tamanho máximo padrão da janela de transmissão e recepção na implementação Java é de 128 pacotes. Implementações que definem um tamanho máximo de janela de transmissão superior a 128 devem considerar as seguintes questões:

- Respostas CHOKE de routers Java devido a estouro de buffer de recepção são muito mais prováveis.
- A estimativa do tamanho do buffer do receptor remoto deve ser implementada para mitigar estouros repetidos (veja acima)
- CHOKE deve ser tratado corretamente (veja abaixo)
- Tamanhos máximos de janela acima de 256 são ainda mais propensos a erros, porque o comprimento do campo de opção de contagem nack é de um byte, limitando o máximo de NACKs a 255. Esta especificação não aborda o que fazer se houver mais de 255 NACKs. Tamanhos máximos de janela acima de 256 não são recomendados.

O tamanho mínimo recomendado do buffer para implementações de receptor é de 128 pacotes ou 232 KB (aproximadamente 128 * 1812). Devido à latência da rede I2P, perda de pacotes e o controle de congestionamento resultante, um buffer deste tamanho raramente é preenchido. Overflow é, no entanto, muito mais provável de ocorrer em conexões de alta largura de banda de "local loopback" (mesmo router) ou em testes locais.

Para indicar rapidamente e recuperar suavemente de condições de overflow, existe um mecanismo simples de pushback no protocolo de streaming. Se um pacote for recebido com um campo de delay opcional com valor de 60001 ou superior, isso indica "choking" ou uma janela de recepção de zero. Um pacote com um campo de delay opcional com valor de 60000 ou inferior indica "unchoking". Pacotes sem um campo de delay opcional não afetam o estado choke/unchoke.

Após ser sufocado, nenhum pacote adicional com dados deve ser enviado até que o transmissor seja desobstruído, exceto por pacotes de dados de "sonda" ocasionais para compensar possíveis pacotes de desobstrução perdidos. O endpoint sufocado deve iniciar um "temporizador de persistência" para controlar a sondagem, como no TCP. O endpoint que desobstrui deve enviar vários pacotes com este campo definido, ou continuar enviando-os periodicamente até que pacotes de dados sejam recebidos novamente. O tempo máximo para aguardar a desobstrução depende da implementação. O tamanho da janela do transmissor e a estratégia de controle de congestionamento após ser desobstruído dependem da implementação.

### Controle de Congestionamento {#congestion}

A biblioteca de streaming usa as fases padrão de slow-start (crescimento exponencial da janela) e congestion avoidance (crescimento linear da janela), com backoff exponencial. O janelamento e acknowledgments usam contagem de pacotes, não contagem de bytes.

### Fechar {#close}

Qualquer pacote, incluindo um com a flag SYNCHRONIZE definida, pode ter a flag CLOSE enviada também. A conexão não é fechada até que o peer responda com a flag CLOSE. Pacotes CLOSE também podem conter dados.

### Ping / Pong {#ping}

Não há função de ping na camada I2CP (equivalente ao echo ICMP) ou em datagramas. Esta função é fornecida no streaming. Pings e pongs não podem ser combinados com um pacote de streaming padrão; se a opção ECHO estiver definida, então a maioria das outras flags, opções, ackThrough, sequenceNum, NACKs, etc. são ignoradas.

Um pacote ping deve ter as flags ECHO, SIGNATURE_INCLUDED e FROM_INCLUDED definidas. O sendStreamId deve ser maior que zero, e o receiveStreamId é ignorado. O sendStreamId pode ou não corresponder a uma conexão existente.

Um pacote pong deve ter a flag ECHO definida. O sendStreamId deve ser zero, e o receiveStreamId é o sendStreamId do ping. Antes da versão 0.9.18, o pacote pong não incluía nenhuma carga útil que estava contida no ping.

A partir da versão 0.9.18, pings e pongs podem conter uma carga útil. A carga útil no ping, até um máximo de 32 bytes, é retornada no pong.

O streaming pode ser configurado para desabilitar o envio de pongs com a configuração i2p.streaming.answerPings=false.

### Notas de i2p.streaming.profile {#profile}

Esta opção suporta dois valores; 1=bulk e 2=interactive. A opção fornece uma dica para a biblioteca de streaming e/ou router sobre o padrão de tráfego esperado.

"Bulk" significa otimizar para alta largura de banda, possivelmente às custas da latência. Este é o padrão. "Interactive" significa otimizar para baixa latência, possivelmente às custas da largura de banda ou eficiência. As estratégias de otimização, se houver, dependem da implementação e podem incluir mudanças fora do protocolo de streaming.

Até a versão da API 0.9.63, o Java I2P retornaria um erro para qualquer valor diferente de 1 (bulk) e o tunnel falharia ao iniciar. A partir da API 0.9.64, o Java I2P ignora o valor. Até a versão da API 0.9.63, o i2pd ignorava esta opção; foi implementada no i2pd a partir da API 0.9.64.

Embora o protocolo de streaming inclua um campo de flag para passar a configuração de perfil para a outra extremidade, isso não está implementado em nenhum router conhecido.

### Compartilhamento de Bloco de Controle {#sharing}

A biblioteca de streaming suporta compartilhamento de "TCP" Control Block. Isso compartilha três parâmetros importantes da biblioteca de streaming (tamanho da janela, tempo de ida e volta, variância do tempo de ida e volta) entre conexões com o mesmo peer remoto. Isso é usado para compartilhamento "temporal" no momento de abertura/fechamento da conexão, não compartilhamento "conjunto" durante uma conexão (Veja [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). Há um compartilhamento separado por ConnectionManager (ou seja, por Destination local) para que não haja vazamento de informações para outros Destinations no mesmo router. Os dados de compartilhamento para um determinado peer expiram após alguns minutos. Os seguintes parâmetros de Compartilhamento de Control Block podem ser definidos por router:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Outros Parâmetros {#other}

Os seguintes parâmetros são padrões recomendados. Os padrões podem variar, dependendo da implementação:

- MIN_RESEND_DELAY = 100 ms (RTO mínimo)
- MAX_RESEND_DELAY = 45 seg (RTO máximo)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (MTU mínimo)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (válido apenas antes do RTT ser amostrado) = 9 seg
- "alpha" (fator de amortecimento RTT conforme RFC 6298) = 0.125
- "beta" (fator de amortecimento RTTDEV conforme RFC 6298) = 0.25
- "K" (multiplicador RTDEV conforme RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- Estimativa máxima de RTT: 60 seg

### Histórico {#history}

A biblioteca de streaming cresceu organicamente para o I2P - primeiro o mihi implementou a "mini biblioteca de streaming" como parte do I2PTunnel, que estava limitada a um tamanho de janela de 1 mensagem (exigindo um ACK antes de enviar a próxima), e então foi refatorada para uma interface de streaming genérica (espelhando sockets TCP) e a implementação completa de streaming foi implantada com um protocolo de janela deslizante e otimizações para levar em conta o alto produto largura de banda x atraso. Streams individuais podem ajustar o tamanho máximo do pacote e outras opções. O tamanho padrão da mensagem é selecionado para caber precisamente em duas mensagens I2NP tunnel de 1K, e é um compromisso razoável entre os custos de largura de banda de retransmitir mensagens perdidas, e a latência e sobrecarga de múltiplas mensagens.

## Trabalho Futuro {#future}

O comportamento da biblioteca de streaming tem um impacto profundo no desempenho a nível da aplicação e, como tal, é uma área importante para análise adicional.

- Ajustes adicionais dos parâmetros da biblioteca de streaming podem ser necessários.
- Outra área para pesquisa é a interação da biblioteca de streaming com as camadas de transporte NTCP e SSU. Consulte [a página de discussão NTCP](/docs/historical/ntcp-discussion) para detalhes.
- A interação dos algoritmos de roteamento com a biblioteca de streaming afeta fortemente o desempenho. Em particular, a distribuição aleatória de mensagens para múltiplos tunnels em um pool leva a um alto grau de entrega fora de ordem, o que resulta em tamanhos de janela menores do que seria o caso normalmente. O router atualmente roteia mensagens para um único par de destino from/to através de um conjunto consistente de tunnels, até a expiração do tunnel ou falha na entrega. Os algoritmos de falha e seleção de tunnel do router devem ser revisados para possíveis melhorias.
- Os dados no primeiro pacote SYN podem exceder o MTU do receptor.
- O campo DELAY_REQUESTED poderia ser usado mais.
- Pacotes SYNCHRONIZE iniciais duplicados em streams de curta duração podem não ser reconhecidos e removidos.
- Não envie o MTU em uma retransmissão.
- Os dados são enviados a menos que a janela de saída esteja cheia. (ou seja, no-Nagle ou TCP_NODELAY) Provavelmente deveria ter uma opção de configuração para isso.
- zzz adicionou código de debug à biblioteca de streaming para registrar pacotes em um formato compatível com wireshark (pcap); Use isso para analisar melhor o desempenho. O formato pode requerer melhorias para mapear mais parâmetros da biblioteca de streaming para campos TCP.
- Há propostas para substituir a biblioteca de streaming por TCP padrão (ou talvez uma camada nula junto com raw sockets). Isso seria infelizmente incompatível com a biblioteca de streaming, mas seria bom comparar o desempenho dos dois.

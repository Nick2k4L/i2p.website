---
title: "Потоковый протокол"
description: "TCP-подобный транспорт, используемый большинством I2P-приложений"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Обзор {#overview}

Библиотека потоковой передачи технически является частью "прикладного" уровня, поскольку она не является основной функцией router. Однако на практике она обеспечивает жизненно важную функцию для почти всех существующих I2P-приложений, предоставляя TCP-подобные потоки через I2P и позволяя легко портировать существующие приложения на I2P. Другой библиотекой транспорта end-to-end для клиентской связи является [библиотека датаграмм](/docs/specs/datagrams).

Библиотека streaming представляет собой слой поверх основного [I2CP API](/docs/specs/i2cp), который обеспечивает надёжные, упорядоченные и аутентифицированные потоки сообщений поверх ненадёжного, неупорядоченного и неаутентифицированного слоя сообщений. Подобно отношению TCP к IP, эта функциональность streaming имеет целый ряд компромиссов и доступных оптимизаций, но вместо встраивания этой функциональности в базовый код I2P, она была выделена в отдельную библиотеку как для того, чтобы отделить TCP-подобные сложности, так и для обеспечения возможности альтернативных оптимизированных реализаций.

Учитывая относительно высокую стоимость сообщений, протокол библиотеки streaming для планирования и доставки этих сообщений был оптимизирован, чтобы позволить отдельным передаваемым сообщениям содержать как можно больше доступной информации. Например, небольшая HTTP-транзакция, проксируемая через библиотеку streaming, может быть завершена за один круговой обмен - первые сообщения объединяют SYN, FIN и небольшую полезную нагрузку HTTP-запроса, а ответ объединяет SYN, FIN, ACK и полезную нагрузку HTTP-ответа. Хотя дополнительный ACK должен быть передан, чтобы сообщить HTTP-серверу о получении SYN/FIN/ACK, локальный HTTP-прокси часто может доставить полный ответ в браузер немедленно.

Библиотека потоковой передачи данных очень похожа на абстракцию TCP со своими скользящими окнами, алгоритмами контроля перегрузки (как медленный старт, так и избежание перегрузки) и общим поведением пакетов (ACK, SYN, FIN, RST, расчет rto и т.д.).

Библиотека streaming — это надёжная библиотека, оптимизированная для работы в сети I2P. Она имеет однофазную настройку и содержит полную реализацию оконного протокола.

## API {#api}

API библиотеки потоковой передачи предоставляет стандартную парадигму сокетов для Java-приложений. Низкоуровневый API [I2CP](/docs/specs/i2cp) полностью скрыт, за исключением того, что приложения могут передавать [параметры I2CP](/docs/specs/i2cp#options) через библиотеку потоковой передачи для интерпретации I2CP.

Стандартный интерфейс к библиотеке потокового вещания заключается в том, что приложение использует I2PSocketManagerFactory для создания I2PSocketManager. Затем приложение запрашивает у менеджера сокетов I2PSession, что вызовет подключение к роутеру через [I2CP](/docs/specs/i2cp). После этого приложение может устанавливать соединения с помощью I2PSocket или принимать соединения с помощью I2PServerSocket.

Хороший пример использования можно найти в коде i2psnark.

### Опции и значения по умолчанию {#options}

Опции и их текущие значения по умолчанию перечислены ниже. Опции чувствительны к регистру и могут быть установлены для всего router, для конкретного клиента или для отдельного сокета на основе каждого соединения. Многие значения настроены для производительности HTTP в типичных условиях I2P. Другим приложениям, таким как peer-to-peer сервисы, настоятельно рекомендуется изменять их по мере необходимости, устанавливая опции и передавая их через вызов I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts). Значения времени указаны в мс.

Обратите внимание, что API более высокого уровня, такие как [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob) и [I2PTunnel](/docs/api/i2ptunnel), могут переопределять эти значения по умолчанию своими собственными. Также учтите, что многие параметры применяются только к серверам, ожидающим входящие соединения.

Начиная с версии 0.9.1, большинство опций, но не все, могут быть изменены в активном менеджере сокетов или сессии. Подробности смотрите в javadocs.

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
## Спецификация протокола {#spec}

[См. страницу спецификации библиотеки Streaming.](/docs/specs/streaming)

## Детали реализации {#implementation}

### Настройка {#setup}

Инициатор отправляет пакет с установленным флагом SYNCHRONIZE. Этот пакет также может содержать начальные данные. Узел отвечает пакетом с установленным флагом SYNCHRONIZE. Этот пакет также может содержать начальные данные ответа.

Инициатор может отправить дополнительные пакеты данных, до размера начального окна, перед получением ответа SYNCHRONIZE. Эти пакеты также будут иметь поле Stream ID отправителя установленное в 0. Получатели должны буферизировать пакеты, полученные для неизвестных потоков, в течение короткого периода времени, поскольку они могут прибыть не по порядку, до получения пакета SYNCHRONIZE.

### Выбор и согласование MTU {#mtu}

Максимальный размер сообщения (также называемый MTU / MRU) согласовывается до меньшего значения, поддерживаемого двумя узлами. Поскольку сообщения tunnel дополняются до 1КБ, плохой выбор MTU приведет к большому объему накладных расходов. MTU задается параметром i2p.streaming.maxMessageSize. Текущий MTU по умолчанию в 1730 байт был выбран для точного размещения в двух 1К I2NP tunnel сообщениях, включая накладные расходы для типичного случая.

Примечание: Это максимальный размер только полезной нагрузки, не включая заголовок.

Примечание: Для ECIES соединений, которые имеют уменьшенные накладные расходы, рекомендуемый MTU составляет 1812. MTU по умолчанию остается 1730 для всех соединений, независимо от используемого типа ключа. Клиенты должны использовать минимальное значение из отправленного и полученного MTU, как обычно. См. предложение 155.

Первое сообщение в соединении включает 387 байт (типично) Destination, добавленный уровнем потоковой передачи, и обычно 898 байт (типично) LeaseSet, и ключи сессии, упакованные в garlic-сообщение роутером. (LeaseSet и ключи сессии не будут упакованы, если сессия ElGamal была установлена ранее). Поэтому цель размещения полного HTTP-запроса в одном 1KB I2NP-сообщении не всегда достижима. Однако выбор MTU вместе с тщательной реализацией стратегий фрагментации и пакетирования в процессоре шлюза tunnel являются важными факторами пропускной способности сети, задержки, надежности и эффективности, особенно для долгоживущих соединений.

### Целостность данных {#integrity}

Целостность данных обеспечивается контрольной суммой gzip CRC-32, реализованной в [слое I2CP](/docs/specs/i2cp#format). В протоколе потоковой передачи нет поля контрольной суммы.

### Инкапсуляция пакетов {#encapsulation}

Каждый пакет отправляется через I2P как отдельное сообщение (или как индивидуальный clove в [Garlic Message](/docs/overview/garlic-routing)). Инкапсуляция сообщений реализована в базовых слоях [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np) и [tunnel message](/docs/specs/tunnel-message). В протоколе потоковой передачи нет механизма разделителей пакетов или поля длины полезной нагрузки.

### Необязательная задержка {#delay}

Пакеты данных могут включать необязательное поле задержки, указывающее запрашиваемую задержку в миллисекундах перед тем, как получатель должен подтвердить получение пакета. Допустимые значения от 0 до 60000 включительно. Значение 0 запрашивает немедленное подтверждение. Это только рекомендация, и получатели должны немного задерживать подтверждения, чтобы дополнительные пакеты могли быть подтверждены одним ack. Некоторые реализации могут включать рекомендуемое значение (измеренный RTT / 2) в это поле. Для ненулевых значений необязательной задержки получатели должны ограничивать максимальную задержку перед отправкой подтверждения несколькими секундами максимум. Значения необязательной задержки больше 60000 указывают на дросселирование, см. ниже.

### Окна передачи/приема и троттлинг {#windows}

TCP заголовки включают окно приёма в байтах; однако протокол потоковой передачи не предоставляет способа обмениваться максимальным размером окна приёма ни в байтах, ни в пакетах. Существует только простая индикация блокировки/разблокировки, указывающая на то, что буфер приёма заполнен. Каждая конечная точка должна поддерживать собственную оценку окна приёма удалённой стороны в байтах или пакетах. Обратите внимание, что буфер приёма может переполниться при любом размере окна, если клиентское приложение медленно опустошает буфер.

Размер окна передачи и приема по умолчанию в Java-реализации составляет максимум 128 пакетов. Реализации, устанавливающие максимальный размер окна передачи больше 128, должны учитывать следующие вопросы:

- CHOKE ответы от Java router'ов из-за переполнения буфера приема гораздо более вероятны.
- Должна быть реализована оценка размера буфера приемника на дальнем конце для предотвращения повторяющихся переполнений (см. выше)
- CHOKE должен обрабатываться корректно (см. ниже)
- Максимальные размеры окна свыше 256 еще более подвержены ошибкам, поскольку длина поля опции счетчика nack составляет один байт, ограничивая максимальное количество NACK до 255. Данная спецификация не рассматривает, что делать при наличии более 255 NACK. Максимальные размеры окна свыше 256 не рекомендуются.

Рекомендуемый минимальный размер буфера для реализаций получателя составляет 128 пакетов или 232 КБ (приблизительно 128 * 1812). Из-за задержек в сети I2P, потери пакетов и результирующего контроля перегрузки буфер такого размера редко заполняется полностью. Переполнение, однако, гораздо более вероятно при высокоскоростных соединениях "локальной петли" (внутри одного router) или при локальном тестировании.

Для быстрого обнаружения и плавного восстановления от условий переполнения в потоковом протоколе существует простой механизм обратного давления. Если получен пакет с опциональным полем задержки со значением 60001 или выше, это указывает на "блокировку" или нулевое окно приема. Пакет с опциональным полем задержки со значением 60000 или меньше указывает на "разблокировку". Пакеты без опционального поля задержки не влияют на состояние блокировки/разблокировки.

После блокировки не должно отправляться больше пакетов с данными до тех пор, пока передатчик не будет разблокирован, за исключением редких "зондирующих" пакетов данных для компенсации возможных потерянных пакетов разблокировки. Заблокированная конечная точка должна запустить "таймер постоянства" для управления зондированием, как в TCP. Разблокирующая конечная точка должна отправить несколько пакетов с установленным этим полем или продолжать отправлять их периодически до тех пор, пока пакеты данных не будут получены снова. Максимальное время ожидания разблокировки зависит от реализации. Размер окна передатчика и стратегия управления перегрузкой после разблокировки зависят от реализации.

### Управление перегрузкой {#congestion}

Библиотека streaming использует стандартные фазы медленного старта (экспоненциальный рост окна) и предотвращения перегрузки (линейный рост окна) с экспоненциальной задержкой. Управление окном и подтверждения используют количество пакетов, а не количество байтов.

### Закрыть {#close}

Любой пакет, включая пакет с установленным флагом SYNCHRONIZE, может также иметь установленный флаг CLOSE. Соединение не закрывается до тех пор, пока узел не ответит флагом CLOSE. Пакеты CLOSE также могут содержать данные.

### Ping / Pong {#ping}

На уровне I2CP нет функции ping (эквивалент ICMP echo) или в датаграммах. Эта функция предоставляется в streaming. Ping и pong нельзя объединять со стандартным streaming пакетом; если установлена опция ECHO, то большинство других флагов, опций, ackThrough, sequenceNum, NACK и т.д. игнорируются.

Пакет ping должен иметь установленные флаги ECHO, SIGNATURE_INCLUDED и FROM_INCLUDED. Значение sendStreamId должно быть больше нуля, а receiveStreamId игнорируется. Значение sendStreamId может соответствовать или не соответствовать существующему соединению.

Пакет pong должен иметь установленный флаг ECHO. Поле sendStreamId должно быть равно нулю, а receiveStreamId должно соответствовать sendStreamId из пакета ping. До версии 0.9.18 пакет pong не включал полезную нагрузку, которая содержалась в пакете ping.

Начиная с версии 0.9.18, ping и pong могут содержать полезную нагрузку. Полезная нагрузка в ping, до максимум 32 байт, возвращается в pong.

Потоковая передача может быть настроена для отключения отправки pong-ответов с помощью конфигурации i2p.streaming.answerPings=false.

### Примечания к i2p.streaming.profile {#profile}

Эта опция поддерживает два значения; 1=bulk и 2=interactive. Опция предоставляет подсказку библиотеке потоковой передачи и/или router относительно ожидаемого шаблона трафика.

"Bulk" означает оптимизацию для высокой пропускной способности, возможно, за счёт задержки. Это значение по умолчанию. "Interactive" означает оптимизацию для низкой задержки, возможно, за счёт пропускной способности или эффективности. Стратегии оптимизации, если таковые имеются, зависят от реализации и могут включать изменения вне протокола потоковой передачи.

До версии API 0.9.63 Java I2P возвращал ошибку для любого значения, отличного от 1 (bulk), и tunnel не удавалось запустить. Начиная с API 0.9.64, Java I2P игнорирует это значение. До версии API 0.9.63 i2pd игнорировал эту опцию; она была реализована в i2pd начиная с API 0.9.64.

Хотя протокол потоковой передачи включает поле флага для передачи настройки профиля на другой конец, это не реализовано ни в одном известном router.

### Совместное использование блока управления {#sharing}

Библиотека потокового вещания поддерживает совместное использование "TCP" блоков управления. Это позволяет совместно использовать три важных параметра библиотеки потокового вещания (размер окна, время прохождения пакета в оба конца, дисперсия времени прохождения пакета в оба конца) между соединениями к одному и тому же удаленному узлу. Это используется для "временного" совместного использования во время открытия/закрытия соединения, а не "ансамблевого" совместного использования во время соединения (См. [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). Существует отдельное совместное использование для каждого ConnectionManager (т.е. для каждого локального Destination), чтобы не было утечки информации к другим Destination на том же router. Данные совместного использования для данного узла истекают через несколько минут. Следующие параметры совместного использования блоков управления могут быть установлены для каждого router:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Другие параметры {#other}

Следующие параметры являются рекомендуемыми значениями по умолчанию. Значения по умолчанию могут отличаться в зависимости от реализации:

- MIN_RESEND_DELAY = 100 мс (минимальный RTO)
- MAX_RESEND_DELAY = 45 сек (максимальный RTO)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (минимальный MTU)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (действует только до измерения RTT) = 9 сек
- "alpha" (коэффициент сглаживания RTT согласно RFC 6298) = 0.125
- "beta" (коэффициент сглаживания RTTDEV согласно RFC 6298) = 0.25
- "K" (множитель RTDEV согласно RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 мс
- Максимальная оценка RTT: 60 сек

### История {#history}

Библиотека потоковой передачи развивалась органично для I2P - сначала mihi реализовал "мини-библиотеку потоковой передачи" как часть I2PTunnel, которая была ограничена размером окна в 1 сообщение (требовалось подтверждение перед отправкой следующего), а затем она была выделена в универсальный интерфейс потоковой передачи (отражающий TCP сокеты), и была развернута полная реализация потоковой передачи с протоколом скользящего окна и оптимизациями для учета высокого произведения пропускной способности на задержку. Отдельные потоки могут настраивать максимальный размер пакета и другие параметры. Размер сообщения по умолчанию выбран так, чтобы точно помещаться в два I2NP tunnel сообщения размером 1К, и представляет собой разумный компромисс между затратами пропускной способности на повторную передачу потерянных сообщений и задержкой и накладными расходами множественных сообщений.

## Планы на будущее {#future}

Поведение библиотеки потокового вещания оказывает глубокое влияние на производительность на уровне приложений и поэтому является важной областью для дальнейшего анализа.

- Может потребоваться дополнительная настройка параметров streaming lib.
- Другой областью для исследования является взаимодействие streaming lib с транспортными слоями NTCP и SSU. См. [страницу обсуждения NTCP](/docs/historical/ntcp-discussion) для деталей.
- Взаимодействие алгоритмов маршрутизации со streaming lib сильно влияет на производительность. В частности, случайное распределение сообщений по нескольким tunnel в пуле приводит к высокой степени доставки не по порядку, что приводит к меньшим размерам окна, чем могло бы быть в противном случае. В настоящее время router направляет сообщения для одной пары назначения от/к через согласованный набор tunnel, до истечения срока действия tunnel или сбоя доставки. Алгоритмы обработки сбоев и выбора tunnel в router следует пересмотреть на предмет возможных улучшений.
- Данные в первом SYN пакете могут превышать MTU получателя.
- Поле DELAY_REQUESTED могло бы использоваться больше.
- Дублированные начальные SYNCHRONIZE пакеты в коротко живущих потоках могут не распознаваться и не удаляться.
- Не отправлять MTU в повторной передаче.
- Данные отправляются, если только исходящее окно не заполнено. (т.е. no-Nagle или TCP_NODELAY) Вероятно, следует иметь опцию конфигурации для этого.
- zzz добавил отладочный код в streaming library для логирования пакетов в wireshark-совместимом (pcap) формате; Используйте это для дальнейшего анализа производительности. Формат может потребовать улучшения для сопоставления большего количества параметров streaming lib с полями TCP.
- Есть предложения заменить streaming lib на стандартный TCP (или, возможно, нулевой слой вместе с raw sockets). К сожалению, это было бы несовместимо со streaming lib, но было бы хорошо сравнить производительность этих двух решений.

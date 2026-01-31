---
title: "Streaming Protocol"
description: "TCP-ähnlicher Transport, der von den meisten I2P-Anwendungen verwendet wird"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Überblick {#overview}

Die Streaming-Bibliothek gehört technisch zur "Anwendungs"-Schicht, da sie keine Kernfunktion des routers ist. In der Praxis stellt sie jedoch eine wichtige Funktion für fast alle existierenden I2P-Anwendungen bereit, indem sie TCP-ähnliche Streams über I2P ermöglicht und bestehende Apps einfach zu I2P portieren lässt. Die andere End-to-End-Transport-Bibliothek für Client-Kommunikation ist die [Datagramm-Bibliothek](/docs/specs/datagrams).

Die Streaming-Bibliothek ist eine Schicht auf der Kern-[I2CP API](/docs/specs/i2cp), die zuverlässige, geordnete und authentifizierte Nachrichtenströme über eine unzuverlässige, ungeordnete und nicht authentifizierte Nachrichtenschicht ermöglicht. Genau wie bei der TCP-zu-IP-Beziehung bietet diese Streaming-Funktionalität eine ganze Reihe von Kompromissen und Optimierungen, aber anstatt diese Funktionalität in den I2P-Basis-Code einzubetten, wurde sie in eine eigene Bibliothek ausgelagert, um sowohl die TCP-ähnlichen Komplexitäten getrennt zu halten als auch alternative optimierte Implementierungen zu ermöglichen.

In Anbetracht der relativ hohen Kosten von Nachrichten wurde das Protokoll der Streaming-Bibliothek für die Planung und Zustellung dieser Nachrichten optimiert, um zu ermöglichen, dass einzelne übertragene Nachrichten so viele Informationen wie verfügbar enthalten können. Zum Beispiel kann eine kleine HTTP-Transaktion, die über die Streaming-Bibliothek geleitet wird, in einem einzigen Roundtrip abgeschlossen werden - die ersten Nachrichten bündeln ein SYN, FIN und die kleine HTTP-Request-Nutzlast, und die Antwort bündelt das SYN, FIN, ACK und die HTTP-Response-Nutzlast. Während ein zusätzliches ACK übertragen werden muss, um dem HTTP-Server mitzuteilen, dass das SYN/FIN/ACK empfangen wurde, kann der lokale HTTP-Proxy oft die vollständige Antwort sofort an den Browser liefern.

Die Streaming-Bibliothek weist große Ähnlichkeit mit einer Abstraktion von TCP auf, mit ihren Sliding Windows, Congestion-Control-Algorithmen (sowohl Slow Start als auch Congestion Avoidance) und dem allgemeinen Paketverhalten (ACK, SYN, FIN, RST, RTO-Berechnung, etc.).

Die Streaming-Bibliothek ist eine robuste Bibliothek, die für den Betrieb über I2P optimiert ist. Sie verfügt über eine einstufige Einrichtung und enthält eine vollständige Windowing-Implementierung.

## API {#api}

Die Streaming-Bibliotheks-API bietet Java-Anwendungen ein Standard-Socket-Paradigma. Die darunterliegende [I2CP](/docs/specs/i2cp)-API ist vollständig verborgen, außer dass Anwendungen [I2CP-Parameter](/docs/specs/i2cp#options) durch die Streaming-Bibliothek weiterleiten können, um von I2CP interpretiert zu werden.

Die Standardschnittstelle zur Streaming-Bibliothek besteht darin, dass die Anwendung die I2PSocketManagerFactory verwendet, um einen I2PSocketManager zu erstellen. Die Anwendung fragt dann den Socket-Manager nach einer I2PSession, was eine Verbindung zum router über [I2CP](/docs/specs/i2cp) verursacht. Die Anwendung kann dann Verbindungen mit einem I2PSocket einrichten oder Verbindungen mit einem I2PServerSocket empfangen.

Ein gutes Beispiel für die Verwendung finden Sie im i2psnark-Code.

### Optionen und Standardwerte {#options}

Die Optionen und aktuellen Standardwerte sind unten aufgeführt. Optionen sind groß-/kleinschreibungssensitiv und können für den gesamten router, für einen bestimmten Client oder für einen einzelnen Socket auf Verbindungsbasis gesetzt werden. Viele Werte sind für HTTP-Performance unter typischen I2P-Bedingungen optimiert. Andere Anwendungen wie Peer-to-Peer-Dienste werden ausdrücklich ermutigt, diese nach Bedarf zu ändern, indem sie die Optionen setzen und über den Aufruf an I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts) übergeben. Zeitwerte sind in ms angegeben.

Beachten Sie, dass höhere APIs wie [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob) und [I2PTunnel](/docs/api/i2ptunnel) diese Standardwerte mit ihren eigenen Standardwerten überschreiben können. Beachten Sie auch, dass viele Optionen nur für Server gelten, die auf eingehende Verbindungen lauschen.

Ab Version 0.9.1 können die meisten, aber nicht alle Optionen in einem aktiven Socket-Manager oder einer aktiven Session geändert werden. Details finden Sie in der Javadoc.

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
## Protokollspezifikation {#spec}

[Siehe die Streaming Library Spezifikationsseite.](/docs/specs/streaming)

## Implementierungsdetails {#implementation}

### Einrichtung {#setup}

Der Initiator sendet ein Paket mit gesetztem SYNCHRONIZE-Flag. Dieses Paket kann auch die initialen Daten enthalten. Der Peer antwortet mit einem Paket mit gesetztem SYNCHRONIZE-Flag. Dieses Paket kann auch die initiale Antwortdaten enthalten.

Der Initiator kann zusätzliche Datenpakete senden, bis zur anfänglichen Fenstergröße, bevor er die SYNCHRONIZE-Antwort erhält. Diese Pakete haben ebenfalls das Feld "send Stream ID" auf 0 gesetzt. Empfänger müssen Pakete, die auf unbekannten Streams empfangen werden, für eine kurze Zeit puffern, da sie außer der Reihe ankommen können, noch vor dem SYNCHRONIZE-Paket.

### MTU-Auswahl und -Verhandlung {#mtu}

Die maximale Nachrichtengröße (auch MTU / MRU genannt) wird auf den niedrigeren Wert verhandelt, der von beiden Peers unterstützt wird. Da tunnel-Nachrichten auf 1KB aufgefüllt werden, führt eine schlechte MTU-Auswahl zu einem großen Overhead. Die MTU wird durch die Option i2p.streaming.maxMessageSize festgelegt. Die aktuelle Standard-MTU von 1730 wurde gewählt, um genau in zwei 1K I2NP tunnel-Nachrichten zu passen, einschließlich des Overheads für den typischen Fall.

Hinweis: Dies ist die maximale Größe der Nutzdaten nur, ohne den Header.

Hinweis: Für ECIES-Verbindungen, die einen reduzierten Overhead haben, wird eine MTU von 1812 empfohlen. Die Standard-MTU bleibt für alle Verbindungen bei 1730, unabhängig davon, welcher Schlüsseltyp verwendet wird. Clients müssen wie gewöhnlich das Minimum der gesendeten und empfangenen MTU verwenden. Siehe Vorschlag 155.

Die erste Nachricht in einer Verbindung enthält eine 387 Byte (typisch) große Destination, die von der Streaming-Schicht hinzugefügt wird, und normalerweise ein 898 Byte (typisch) großes LeaseSet sowie Session-Schlüssel, die vom Router in der Garlic-Nachricht gebündelt werden. (Das LeaseSet und die Session-Schlüssel werden nicht gebündelt, wenn zuvor eine ElGamal-Session etabliert wurde). Daher ist das Ziel, eine vollständige HTTP-Anfrage in eine einzige 1KB I2NP-Nachricht zu packen, nicht immer erreichbar. Jedoch sind die Auswahl der MTU zusammen mit einer sorgfältigen Implementierung von Fragmentierungs- und Stapelungsstrategien im Tunnel-Gateway-Prozessor wichtige Faktoren für Netzwerkbandbreite, Latenz, Zuverlässigkeit und Effizienz, insbesondere bei langlebigen Verbindungen.

### Datenintegrität {#integrity}

Die Datenintegrität wird durch die gzip CRC-32 Prüfsumme gewährleistet, die in [der I2CP-Schicht](/docs/specs/i2cp#format) implementiert ist. Es gibt kein Prüfsummenfeld im Streaming-Protokoll.

### Paket-Kapselung {#encapsulation}

Jedes Paket wird durch I2P als einzelne Nachricht (oder als individuelle Gewürznelke in einer [Garlic Message](/docs/overview/garlic-routing)) gesendet. Die Nachrichtenkapselung wird in den zugrundeliegenden [I2CP](/docs/specs/i2cp)-, [I2NP](/docs/specs/i2np)- und [tunnel message](/docs/specs/tunnel-message)-Schichten implementiert. Es gibt keinen Paketbegrenzungsmechanismus oder ein Payload-Längenfeld im Streaming-Protokoll.

### Optionale Verzögerung {#delay}

Datenpakete können ein optionales Verzögerungsfeld enthalten, das die angeforderte Verzögerung in ms angibt, bevor der Empfänger das Paket bestätigen soll. Gültige Werte sind 0 bis 60000 einschließlich. Ein Wert von 0 fordert eine sofortige Bestätigung an. Dies ist nur beratend, und Empfänger sollten leicht verzögern, damit zusätzliche Pakete mit einer einzigen Bestätigung quittiert werden können. Einige Implementierungen können einen beratenden Wert von (gemessene RTT / 2) in diesem Feld enthalten. Bei Verzögerungswerten ungleich null sollten Empfänger die maximale Verzögerung vor dem Senden einer Bestätigung auf höchstens wenige Sekunden begrenzen. Optionale Verzögerungswerte größer als 60000 zeigen Drosselung an, siehe unten.

### Sende-/Empfangsfenster und Choking {#windows}

TCP-Header enthalten das Empfangsfenster in Bytes; das Streaming-Protokoll bietet jedoch keine Möglichkeit, die maximale Empfangsfenstergröße weder in Bytes noch in Paketen auszutauschen. Es gibt nur eine einfache Choke/Unchoke-Anzeige, die signalisiert, dass der Empfangspuffer voll ist. Jeder Endpunkt muss seine eigene Schätzung des Empfangsfensters am anderen Ende aufrechterhalten, entweder in Bytes oder Paketen. Beachten Sie, dass ein Empfangspuffer bei jeder Fenstergröße überlaufen kann, wenn die Client-Anwendung zu langsam ist, den Puffer zu leeren.

Die standardmäßige maximale Übertragung- und Empfangsfenstergröße in der Java-Implementierung beträgt 128 Pakete. Implementierungen, die eine maximale Übertragungsfenstergröße höher als 128 setzen, müssen die folgenden Punkte berücksichtigen:

- CHOKE-Antworten von Java-Routern aufgrund von Empfangspuffer-Überläufen sind viel wahrscheinlicher.
- Eine Schätzung der Empfangspuffergröße am anderen Ende muss implementiert werden, um wiederholte Überläufe zu vermeiden (siehe oben)
- CHOKE muss korrekt behandelt werden (siehe unten)
- Maximale Fenstergrößen über 256 sind noch fehleranfälliger, da das Nack-Count-Optionsfeld eine Länge von einem Byte hat, was die maximalen NACKs auf 255 begrenzt. Diese Spezifikation behandelt nicht, was zu tun ist, wenn es mehr als 255 NACKs gibt. Maximale Fenstergrößen über 256 werden nicht empfohlen.

Die empfohlene Mindestpuffergröße für Empfänger-Implementierungen beträgt 128 Pakete oder 232 KB (ungefähr 128 * 1812). Aufgrund der I2P-Netzwerklatenz, Paketverlusten und der daraus resultierenden Überlastungskontrolle wird ein Puffer dieser Größe selten vollständig gefüllt. Ein Überlauf ist jedoch viel wahrscheinlicher bei Verbindungen mit hoher Bandbreite über "local loopback" (gleicher router) oder bei lokalen Tests.

Um Überlaufbedingungen schnell anzuzeigen und reibungslos zu beheben, gibt es einen einfachen Mechanismus für Pushback im Streaming-Protokoll. Wenn ein Paket mit einem optionalen Verzögerungsfeld mit einem Wert von 60001 oder höher empfangen wird, zeigt dies "Choking" oder ein Empfangsfenster von Null an. Ein Paket mit einem optionalen Verzögerungsfeld mit einem Wert von 60000 oder weniger zeigt "Unchoking" an. Pakete ohne optionales Verzögerungsfeld beeinflussen den Choke/Unchoke-Zustand nicht.

Nachdem gedrosselt wurde, sollten keine weiteren Datenpakete gesendet werden, bis der Sender wieder entdrosselt wird, außer gelegentlichen "Sondierungs"-Datenpaketen, um mögliche verlorene Entdrosselungspakete zu kompensieren. Der gedrosselte Endpunkt sollte einen "Persistenz-Timer" starten, um die Sondierung zu steuern, wie bei TCP. Der entdrosselnde Endpunkt sollte mehrere Pakete mit diesem Feld gesetzt senden oder sie periodisch weiter senden, bis wieder Datenpakete empfangen werden. Die maximale Wartezeit für die Entdrosselung ist implementierungsabhängig. Die Senderfenstergröße und Staukontrollstrategie nach der Entdrosselung ist implementierungsabhängig.

### Congestion Control {#congestion}

Die Streaming-Bibliothek verwendet Standard-Slow-Start (exponentielles Fensterwachstum) und Congestion-Avoidance-Phasen (lineares Fensterwachstum) mit exponentiellem Backoff. Windowing und Bestätigungen verwenden Paketzählung, nicht Bytezählung.

### Schließen {#close}

Jedes Paket, einschließlich eines mit gesetztem SYNCHRONIZE-Flag, kann auch das CLOSE-Flag gesetzt haben. Die Verbindung wird erst geschlossen, wenn der Peer mit dem CLOSE-Flag antwortet. CLOSE-Pakete können ebenfalls Daten enthalten.

### Ping / Pong {#ping}

Es gibt keine Ping-Funktion auf der I2CP-Ebene (äquivalent zu ICMP-Echo) oder in Datagrammen. Diese Funktion wird im Streaming bereitgestellt. Pings und Pongs dürfen nicht mit einem Standard-Streaming-Paket kombiniert werden; wenn die ECHO-Option gesetzt ist, werden die meisten anderen Flags, Optionen, ackThrough, sequenceNum, NACKs usw. ignoriert.

Ein Ping-Paket muss die Flags ECHO, SIGNATURE_INCLUDED und FROM_INCLUDED gesetzt haben. Die sendStreamId muss größer als null sein, und die receiveStreamId wird ignoriert. Die sendStreamId kann einer bestehenden Verbindung entsprechen oder auch nicht.

Ein Pong-Paket muss das ECHO-Flag gesetzt haben. Die sendStreamId muss null sein, und die receiveStreamId ist die sendStreamId aus dem Ping. Vor Release 0.9.18 enthält das Pong-Paket keine Nutzdaten, die im Ping enthalten waren.

Ab Release 0.9.18 können Pings und Pongs eine Nutzlast enthalten. Die Nutzlast im Ping, bis zu maximal 32 Bytes, wird im Pong zurückgegeben.

Streaming kann so konfiguriert werden, dass das Senden von Pongs mit der Konfiguration i2p.streaming.answerPings=false deaktiviert wird.

### i2p.streaming.profile Notizen {#profile}

Diese Option unterstützt zwei Werte; 1=bulk und 2=interactive. Die Option gibt der Streaming-Bibliothek und/oder dem router einen Hinweis auf das erwartete Verkehrsmuster.

"Bulk" bedeutet die Optimierung für hohe Bandbreite, möglicherweise auf Kosten der Latenz. Dies ist die Standardeinstellung. "Interactive" bedeutet die Optimierung für niedrige Latenz, möglicherweise auf Kosten der Bandbreite oder Effizienz. Optimierungsstrategien, falls vorhanden, sind implementierungsabhängig und können Änderungen außerhalb des Streaming-Protokolls beinhalten.

Bis API-Version 0.9.63 gab Java I2P einen Fehler für jeden anderen Wert als 1 (bulk) zurück und der tunnel konnte nicht gestartet werden. Ab API 0.9.64 ignoriert Java I2P den Wert. Bis API-Version 0.9.63 ignorierte i2pd diese Option; sie ist in i2pd ab API 0.9.64 implementiert.

Obwohl das Streaming-Protokoll ein Flag-Feld enthält, um die Profil-Einstellung an das andere Ende zu übertragen, ist dies in keinem bekannten router implementiert.

### Control Block Sharing {#sharing}

Die Streaming-Bibliothek unterstützt "TCP" Control Block Sharing. Dies teilt drei wichtige Parameter der Streaming-Bibliothek (Fenstergröße, Round-Trip-Zeit, Round-Trip-Zeit-Varianz) zwischen Verbindungen zum selben entfernten Peer. Dies wird für "zeitliches" Teilen beim Öffnen/Schließen von Verbindungen verwendet, nicht für "Ensemble"-Teilen während einer Verbindung (Siehe [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). Es gibt einen separaten Share pro ConnectionManager (d.h. pro lokaler Destination), sodass keine Informationsleckage zu anderen Destinations auf demselben router auftritt. Die Share-Daten für einen bestimmten Peer laufen nach einigen Minuten ab. Die folgenden Control Block Sharing Parameter können pro router gesetzt werden:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Andere Parameter {#other}

Die folgenden Parameter sind empfohlene Standardwerte. Standardwerte können je nach Implementierung variieren:

- MIN_RESEND_DELAY = 100 ms (minimale RTO)
- MAX_RESEND_DELAY = 45 Sek (maximale RTO)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (minimale MTU)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (gültig nur bevor RTT gemessen wird) = 9 Sek
- "alpha" (RTT-Dämpfungsfaktor gemäß RFC 6298) = 0,125
- "beta" (RTTDEV-Dämpfungsfaktor gemäß RFC 6298) = 0,25
- "K" (RTDEV-Multiplikator gemäß RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- Maximale RTT-Schätzung: 60 Sek

### Geschichte {#history}

Die Streaming-Bibliothek ist organisch für I2P gewachsen - zuerst implementierte mihi die "Mini-Streaming-Bibliothek" als Teil von I2PTunnel, die auf eine Fenstergröße von 1 Nachricht begrenzt war (ein ACK war erforderlich, bevor die nächste gesendet werden konnte), und dann wurde sie in eine generische Streaming-Schnittstelle (die TCP-Sockets nachahmt) refaktoriert und die vollständige Streaming-Implementierung wurde mit einem Sliding-Window-Protokoll und Optimierungen bereitgestellt, um das hohe Bandbreite x Verzögerung-Produkt zu berücksichtigen. Einzelne Streams können die maximale Paketgröße und andere Optionen anpassen. Die Standard-Nachrichtengröße ist so gewählt, dass sie exakt in zwei 1K I2NP tunnel-Nachrichten passt und stellt einen vernünftigen Kompromiss zwischen den Bandbreitenkosten für die Neuübertragung verlorener Nachrichten und der Latenz und dem Overhead mehrerer Nachrichten dar.

## Zukünftige Arbeiten {#future}

Das Verhalten der Streaming-Bibliothek hat einen tiefgreifenden Einfluss auf die Anwendungsleistung und ist daher ein wichtiger Bereich für weitere Analysen.

- Zusätzliche Feinabstimmung der streaming lib Parameter könnte erforderlich sein.
- Ein weiterer Bereich für die Forschung ist die Interaktion der streaming lib mit den NTCP- und SSU-Transportschichten. Siehe [die NTCP-Diskussionsseite](/docs/historical/ntcp-discussion) für Details.
- Die Interaktion der Routing-Algorithmen mit der streaming lib beeinflusst die Leistung stark. Insbesondere führt die zufällige Verteilung von Nachrichten auf mehrere tunnel in einem Pool zu einem hohen Grad an Auslieferung in falscher Reihenfolge, was zu kleineren Fenstergrößen führt, als dies sonst der Fall wäre. Der router leitet derzeit Nachrichten für ein einzelnes Von/Zu-Zielpaar durch eine konsistente Menge von tunneln weiter, bis zum tunnel-Ablauf oder Zustellungsfehler. Die Fehler- und tunnel-Auswahlalgorithmen des routers sollten auf mögliche Verbesserungen überprüft werden.
- Die Daten im ersten SYN-Paket könnten die MTU des Empfängers überschreiten.
- Das DELAY_REQUESTED-Feld könnte mehr genutzt werden.
- Doppelte initiale SYNCHRONIZE-Pakete bei kurzlebigen Streams werden möglicherweise nicht erkannt und entfernt.
- Die MTU nicht bei einer Neuübertragung senden.
- Daten werden gesendet, es sei denn, das ausgehende Fenster ist voll. (d.h. kein-Nagle oder TCP_NODELAY) Sollte wahrscheinlich eine Konfigurationsoption dafür haben.
- zzz hat Debug-Code zur streaming library hinzugefügt, um Pakete in einem wireshark-kompatiblen (pcap) Format zu protokollieren; Verwende dies zur weiteren Leistungsanalyse. Das Format könnte eine Erweiterung benötigen, um mehr streaming lib Parameter zu TCP-Feldern zu mappen.
- Es gibt Vorschläge, die streaming lib durch Standard-TCP (oder vielleicht eine Null-Schicht zusammen mit Raw-Sockets) zu ersetzen. Dies wäre leider inkompatibel mit der streaming lib, aber es wäre gut, die Leistung der beiden zu vergleichen.

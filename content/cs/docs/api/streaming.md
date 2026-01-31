---
title: "Streaming protokol"
description: "TCP-podobný transport používaný většinou I2P aplikací"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Přehled {#overview}

Streaming knihovna je technicky částí "aplikační" vrstvy, protože není základní funkcí routeru. V praxi však poskytuje zásadní funkci pro téměř všechny existující I2P aplikace tím, že poskytuje TCP-like proudy přes I2P a umožňuje snadné portování existujících aplikací na I2P. Druhou end-to-end transportní knihovnou pro klientskou komunikaci je [datagram knihovna](/docs/specs/datagrams).

Streaming knihovna je vrstva nad základním [I2CP API](/docs/specs/i2cp), která umožňuje spolehlivé, uspořádané a autentizované proudy zpráv fungovat přes nespolehlivou, neuspořádanou a neautentizovanou vrstvu zpráv. Stejně jako vztah TCP k IP má tato streaming funkcionalita celou řadu kompromisů a optimalizací k dispozici, ale namísto vložení této funkcionality do základního I2P kódu byla vyčleněna do vlastní knihovny, aby se TCP-podobné složitosti udržely oddělené a umožnily se alternativní optimalizované implementace.

Vzhledem k relativně vysokým nákladům na zprávy byl protokol streaming knihovny pro plánování a doručování těchto zpráv optimalizován tak, aby umožnil jednotlivým zprávám obsahovat co nejvíce dostupných informací. Například malá HTTP transakce proxovaná přes streaming knihovnu může být dokončena v jediném round tripu - první zpráva spojuje SYN, FIN a malý HTTP request payload, a odpověď spojuje SYN, FIN, ACK a HTTP response payload. I když musí být odeslán dodatečný ACK, aby se HTTP serveru oznámilo, že SYN/FIN/ACK bylo přijato, místní HTTP proxy často může doručit úplnou odpověď do prohlížeče okamžitě.

Streaming knihovna má velkou podobnost s abstrakcí TCP, se svými posuvnými okny, algoritmy řízení zahlcení (jak pomalý start, tak prevence zahlcení) a obecným chováním paketů (ACK, SYN, FIN, RST, výpočet rto atd.).

Streaming knihovna je robustní knihovna optimalizovaná pro provoz v rámci I2P. Má jednofázové nastavení a obsahuje kompletní implementaci oken.

## API {#api}

API knihovny pro streaming poskytuje standardní paradigma socketů pro Java aplikace. Nižší úroveň [I2CP](/docs/specs/i2cp) API je zcela skryta, kromě toho, že aplikace mohou předávat [I2CP parametry](/docs/specs/i2cp#options) skrze streaming knihovnu, které jsou interpretovány I2CP.

Standardní rozhraní ke streaming knihovně je takové, že aplikace použije I2PSocketManagerFactory pro vytvoření I2PSocketManager. Aplikace pak požádá socket manager o I2PSession, což způsobí připojení k routeru prostřednictvím [I2CP](/docs/specs/i2cp). Aplikace pak může nastavit připojení pomocí I2PSocket nebo přijímat připojení pomocí I2PServerSocket.

Pro dobrý příklad použití se podívejte na kód i2psnark.

### Možnosti a výchozí hodnoty {#options}

Možnosti a současné výchozí hodnoty jsou uvedeny níže. Možnosti rozlišují velká a malá písmena a mohou být nastaveny pro celý router, pro konkrétního klienta nebo pro jednotlivý socket na bázi připojení. Mnoho hodnot je laděno pro HTTP výkon za typických I2P podmínek. Ostatní aplikace jako peer-to-peer služby jsou důrazně vybízeny k úpravám podle potřeby nastavením možností a jejich předáním prostřednictvím volání I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts). Časové hodnoty jsou v ms.

Vezměte na vědomí, že vyšší úrovně API, jako jsou [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob) a [I2PTunnel](/docs/api/i2ptunnel), mohou tyto výchozí hodnoty přepsat svými vlastními výchozími hodnotami. Také vezměte na vědomí, že mnohé možnosti se vztahují pouze na servery, které naslouchají příchozím spojením.

Od verze 0.9.1 lze většinu, ale ne všechny možnosti změnit na aktivním správci socketů nebo relaci. Podrobnosti najdete v javadocs.

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
## Specifikace protokolu {#spec}

[Viz stránku Specifikace knihovny Streaming.](/docs/specs/streaming)

## Detaily implementace {#implementation}

### Nastavení {#setup}

Iniciátor odešle paket s nastaveným příznakem SYNCHRONIZE. Tento paket může obsahovat také počáteční data. Partner odpoví paketem s nastaveným příznakem SYNCHRONIZE. Tento paket může obsahovat také počáteční odpověď.

Iniciátor může odeslat další datové pakety, až do velikosti počátečního okna, před přijetím odpovědi SYNCHRONIZE. Tyní pakety budou mít také pole send Stream ID nastavené na 0. Příjemci musí po krátkou dobu ukládat do vyrovnávací paměti pakety přijaté na neznámých streamech, protože mohou dorazit mimo pořadí, před paketem SYNCHRONIZE.

### Výběr a vyjednávání MTU {#mtu}

Maximální velikost zprávy (také nazývaná MTU / MRU) je vyjednána na nižší hodnotu podporovanou oběma protějšky. Jelikož tunnel zprávy jsou doplněny na 1KB, špatný výběr MTU povede k velkému množství režie. MTU je specifikováno možností i2p.streaming.maxMessageSize. Současná výchozí MTU 1730 byla zvolena tak, aby se přesně vešla do dvou 1K I2NP tunnel zpráv, včetně režie pro typický případ.

Poznámka: Toto je maximální velikost pouze užitečného zatížení (payload), nezahrnuje hlavičku.

Poznámka: Pro ECIES spojení, která mají sníženou režii, je doporučené MTU 1812. Výchozí MTU zůstává 1730 pro všechna spojení, bez ohledu na použitý typ klíče. Klienti musí použít minimum z odeslaného a přijatého MTU, jak je obvyklé. Viz návrh 155.

První zpráva v připojení obsahuje 387 bajtů (typicky) Destination přidanou streaming vrstvou a obvykle 898 bajtů (typicky) leaseSet a klíče relace, zabalené v garlic zprávě routerem. (leaseSet a klíče relace nebudou zabaleny, pokud byla dříve navázána ElGamal relace). Proto cíl vejít kompletní HTTP požadavek do jediné 1KB I2NP zprávy není vždy dosažitelný. Výběr MTU však společně s pečlivou implementací strategií fragmentace a dávkování v tunnel gateway procesoru jsou důležité faktory pro šířku pásma sítě, latenci, spolehlivost a efektivitu, zejména pro dlouhodobá připojení.

### Integrita dat {#integrity}

Integrita dat je zajištěna pomocí gzip CRC-32 kontrolního součtu implementovaného v [I2CP vrstvě](/docs/specs/i2cp#format). Ve streaming protokolu není žádné pole pro kontrolní součet.

### Zapouzdření paketů {#encapsulation}

Každý paket je odeslán přes I2P jako jedna zpráva (nebo jako jednotlivý hřebíček v [Garlic Message](/docs/overview/garlic-routing)). Zapouzdření zprávy je implementováno v základních vrstvách [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np) a [tunnel message](/docs/specs/tunnel-message). Ve streaming protokolu neexistuje mechanismus oddělovače paketů ani pole délky užitečného zatížení.

### Volitelné zpoždění {#delay}

Datové pakety mohou obsahovat volitelné pole zpoždění specifikující požadované zpoždění v ms, před tím než příjemce potvrdí paket. Platné hodnoty jsou 0 až 60000 včetně. Hodnota 0 požaduje okamžité potvrzení. Toto je pouze doporučující a příjemci by měli mírně zpozdit, aby mohly být další pakety potvrzeny jediným potvrzením. Některé implementace mohou do tohoto pole zahrnout doporučující hodnotu (naměřené RTT / 2). Pro nenulové volitelné hodnoty zpoždění by příjemci měli omezit maximální zpoždění před odesláním potvrzení na nejvýše několik sekund. Volitelné hodnoty zpoždění větší než 60000 indikují škrcení, viz níže.

### Okna pro odesílání/příjem a omezování {#windows}

TCP hlavičky zahrnují okno příjmu v bajtech; streaming protokol však neposkytuje způsob, jak vyměňovat maximální velikost okna příjmu buď v bajtech nebo paketech. Existuje pouze jednoduché označení choke/unchoke indikující, že buffer příjmu je plný. Každý koncový bod musí udržovat svůj vlastní odhad okna příjmu vzdáleného konce, buď v bajtech nebo paketech. Všimněte si, že buffer příjmu se může přeplnit při jakékoli velikosti okna, pokud je klientská aplikace pomalá při vyprazdňování bufferu.

Výchozí maximální velikost okna pro odesílání a příjem v Java implementaci je 128 paketů. Implementace nastavující maximální velikost okna pro odesílání vyšší než 128 musí zvážit následující problémy:

- CHOKE odpovědi od Java routerů kvůli přetečení přijímacího bufferu jsou mnohem pravděpodobnější.
- Musí být implementován odhad velikosti bufferu vzdáleného příjemce pro zmírnění opakovaných přetečení (viz výše)
- CHOKE musí být zpracováno správně (viz níže)
- Maximální velikosti oken nad 256 jsou ještě náchylnější k chybám, protože délka pole volby počtu nack je jeden byte, což omezuje maximální počet NACKů na 255. Tato specifikace neřeší, co dělat, pokud je NACKů více než 255. Maximální velikosti oken nad 256 se nedoporučují.

Doporučená minimální velikost bufferu pro implementace přijímače je 128 paketů nebo 232 KB (přibližně 128 * 1812). Kvůli latenci I2P sítě, ztrátám paketů a výsledné kontrole zahlcení se buffer této velikosti zřídka zcela naplní. Přetečení je však mnohem pravděpodobnější při vysokorychlostních "local loopback" (stejný router) spojeních nebo při lokálním testování.

Pro rychlé indikování a plynulé obnovení z přetečení existuje jednoduchý mechanismus pro zpětný tlak ve streamovacím protokolu. Pokud je přijat paket s volitelným polem zpoždění s hodnotou 60001 nebo vyšší, indikuje to "choking" nebo okno příjmu s nulovou velikostí. Paket s volitelným polem zpoždění s hodnotou 60000 nebo nižší indikuje "unchoking". Pakety bez volitelného pole zpoždění neovlivňují stav choke/unchoke.

Po udušení by neměly být odesílány žádné další pakety s daty, dokud není odesílatel odušen, kromě občasných "sondovacích" datových paketů pro kompenzaci možných ztracených paketů pro odušení. Udušený koncový bod by měl spustit "persist timer" pro řízení sondování, stejně jako v TCP. Odušující koncový bod by měl odeslat několik paketů s nastaveným tímto polem, nebo je nadále odesílat periodicky, dokud nejsou znovu přijímány datové pakety. Maximální doba čekání na odušení závisí na implementaci. Velikost okna odesílatele a strategie řízení zahlcení po odušení závisí na implementaci.

### Řízení zahlcení {#congestion}

Streaming knihovna používá standardní pomalý start (exponenciální růst okna) a fáze vyhýbání se zahlcení (lineární růst okna), s exponenciálním zpětným krokem. Okenní mechanismus a potvrzování používají počet paketů, nikoli počet bajtů.

### Zavřít {#close}

Jakýkoliv paket, včetně paketu s nastaveným příznakem SYNCHRONIZE, může mít také nastaven příznak CLOSE. Spojení není ukončeno, dokud protistrana neodpoví s příznakem CLOSE. Pakety CLOSE mohou také obsahovat data.

### Ping / Pong {#ping}

Na vrstvě I2CP neexistuje funkce ping (ekvivalent ICMP echo) ani v datagramech. Tato funkce je poskytována ve streamování. Pingy a pongy nemohou být kombinovány se standardním streamovacím paketem; pokud je nastavena možnost ECHO, pak jsou většina ostatních příznaků, možností, ackThrough, sequenceNum, NACKs atd. ignorovány.

Ping paket musí mít nastavené příznaky ECHO, SIGNATURE_INCLUDED a FROM_INCLUDED. SendStreamId musí být větší než nula a receiveStreamId se ignoruje. SendStreamId může, ale nemusí odpovídat existujícímu spojení.

Pong paket musí mít nastaven příznak ECHO. SendStreamId musí být nula a receiveStreamId je sendStreamId z ping paketu. Před verzí 0.9.18 pong paket neobsahuje žádný payload, který byl obsažen v ping paketu.

Od verze 0.9.18 mohou ping a pong obsahovat datovou část. Datová část v ping, až do maximálně 32 bajtů, je vrácena v pong.

Streaming může být nakonfigurován tak, aby zakázal odesílání pongů pomocí konfigurace i2p.streaming.answerPings=false.

### i2p.streaming.profile Poznámky {#profile}

Tato možnost podporuje dvě hodnoty; 1=bulk a 2=interactive. Možnost poskytuje nápovědu pro streaming knihovnu a/nebo router ohledně očekávaného vzoru provozu.

"Bulk" znamená optimalizaci pro vysokou šířku pásma, případně na úkor latence. Toto je výchozí nastavení. "Interactive" znamená optimalizaci pro nízkou latenci, případně na úkor šířky pásma nebo efektivity. Strategie optimalizace, pokud nějaké existují, závisí na implementaci a mohou zahrnovat změny mimo streamovací protokol.

Do verze API 0.9.63 Java I2P vracelo chybu pro jakoukoli hodnotu jinou než 1 (bulk) a tunnel se nepodařilo spustit. Od verze API 0.9.64 Java I2P tuto hodnotu ignoruje. Do verze API 0.9.63 i2pd tuto možnost ignorovalo; v i2pd je implementována od verze API 0.9.64.

Zatímco streaming protokol obsahuje pole pro příznak pro předání nastavení profilu na druhý konec, toto není implementováno v žádném známém routeru.

### Sdílení Control Blocku {#sharing}

Streaming knihovna podporuje sdílení "TCP" Control Block. Toto sdílí tři důležité parametry streaming knihovny (velikost okna, doba odezvy, rozptyl doby odezvy) napříč připojeními ke stejnému vzdálenému peer. Používá se pro "časové" sdílení při otevření/uzavření připojení, ne pro "souborové" sdílení během připojení (Viz [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). Existuje samostatné sdílení pro každý ConnectionManager (tj. pro každou místní Destination), takže nedochází k úniku informací do jiných Destinations na stejném router. Data sdílení pro daný peer vyprší po několika minutách. Následující parametry Control Block Sharing lze nastavit pro každý router:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Další parametry {#other}

Následující parametry jsou doporučené výchozí hodnoty. Výchozí hodnoty se mohou lišit v závislosti na implementaci:

- MIN_RESEND_DELAY = 100 ms (minimální RTO)
- MAX_RESEND_DELAY = 45 sec (maximální RTO)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (minimální MTU)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (platný pouze před vzorkováním RTT) = 9 sec
- "alpha" (faktor tlumení RTT podle RFC 6298) = 0.125
- "beta" (faktor tlumení RTTDEV podle RFC 6298) = 0.25
- "K" (násobitel RTDEV podle RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- Maximální odhad RTT: 60 sec

### Historie {#history}

Streaming knihovna se vyvinula organicky pro I2P - nejprve mihi implementoval "mini streaming knihovnu" jako součást I2PTunnel, která byla omezena na velikost okna 1 zprávy (vyžadovala ACK před odesláním další zprávy), a poté byla refaktorována do generického streaming rozhraní (zrcadlící TCP sockety) a byla nasazena úplná streaming implementace s protokolem posuvného okna a optimalizacemi, které berou v úvahu vysoký součin šířky pásma x zpoždění. Jednotlivé streamy mohou upravit maximální velikost paketu a další možnosti. Výchozí velikost zprávy je vybrána tak, aby se přesně vešla do dvou 1K I2NP tunnel zpráv, a představuje rozumný kompromis mezi náklady na šířku pásma při opakovaném přenosu ztracených zpráv a latencí a režií více zpráv.

## Budoucí práce {#future}

Chování streaming knihovny má zásadní vliv na výkon na úrovni aplikace, a proto je důležitou oblastí pro další analýzu.

- Může být nutné další ladění parametrů streaming lib.
- Další oblast pro výzkum je interakce streaming lib s transportními vrstvami NTCP a SSU. Podrobnosti najdete v [diskusní stránce o NTCP](/docs/historical/ntcp-discussion).
- Interakce směrovacích algoritmů se streaming lib silně ovlivňuje výkon. Konkrétně náhodná distribuce zpráv do více tunnelů v poolu vede k vysokému stupni doručování mimo pořadí, což má za následek menší velikosti oken, než by jinak bylo. Router aktuálně směruje zprávy pro jeden pár cíl/zdroj přes konzistentní sadu tunnelů, dokud nevyprší tunnel nebo nedojde k selhání doručení. Algoritmy selhání a výběru tunnelů routeru by měly být přezkoumány kvůli možným vylepšením.
- Data v prvním SYN paketu mohou překročit MTU příjemce.
- Pole DELAY_REQUESTED by mohlo být více využíváno.
- Duplicitní počáteční SYNCHRONIZE pakety na krátkodobých streamech nemusí být rozpoznány a odstraněny.
- Neposílat MTU v retransmisi.
- Data jsou odesílána, pokud není výstupní okno plné. (tj. no-Nagle nebo TCP_NODELAY) Pravděpodobně by měla existovat konfigurační možnost pro toto.
- zzz přidal do streaming library debug kód pro logování paketů ve formátu kompatibilním s wireshark (pcap); Použijte to k další analýze výkonu. Formát může vyžadovat vylepšení pro mapování více parametrů streaming lib na TCP pole.
- Existují návrhy nahradit streaming lib standardním TCP (nebo možná null vrstvou spolu s raw sockety). To by bohužel bylo nekompatibilní se streaming lib, ale bylo by dobré porovnat výkon těchto dvou.

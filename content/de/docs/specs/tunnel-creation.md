---
title: "Tunnel-Erstellungs-Spezifikation"
description: "ElGamal tunnel Build-Spezifikation für die Erstellung von tunneln mit nicht-interaktivem Telescoping."
slug: "tunnel-creation"
aliases: 
category: "Design"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Überblick

HINWEIS: VERALTET - Dies ist die ElGamal tunnel build Spezifikation. Siehe [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) für die X25519 tunnel build Spezifikation.

Dieses Dokument spezifiziert die Details der verschlüsselten tunnel Build-Nachrichten, die verwendet werden, um tunnel mit einer "nicht-interaktiven Teleskopierung"-Methode zu erstellen. Siehe das tunnel Build-Dokument [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) für einen Überblick über den Prozess, einschließlich Peer-Auswahl und Sortierungsmethoden.

Die Tunnel-Erstellung wird durch eine einzelne Nachricht bewerkstelligt, die entlang des Pfades der Peers im Tunnel weitergegeben, an Ort und Stelle umgeschrieben und zurück an den Tunnel-Ersteller übertragen wird. Diese einzelne Tunnel-Nachricht besteht aus einer variablen Anzahl von Datensätzen (bis zu 8) - einen für jeden potentiellen Peer im Tunnel. Einzelne Datensätze werden asymmetrisch (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) verschlüsselt, um nur von einem bestimmten Peer entlang des Pfades gelesen werden zu können, während eine zusätzliche symmetrische Verschlüsselungsschicht (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) bei jedem Hop hinzugefügt wird, um den asymmetrisch verschlüsselten Datensatz nur zum angemessenen Zeitpunkt freizulegen.

### Anzahl der Datensätze

Nicht alle Datensätze müssen gültige Daten enthalten. Die Build-Nachricht für einen 3-Hop-Tunnel kann beispielsweise mehr Datensätze enthalten, um die tatsächliche Länge des Tunnels vor den Teilnehmern zu verbergen. Es gibt zwei Build-Nachrichtentypen. Die ursprüngliche Tunnel Build Message ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) enthält 8 Datensätze, was für jede praktische Tunnellänge mehr als ausreichend ist. Die neuere Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) enthält 1 bis 8 Datensätze. Der Urheber kann zwischen der Größe der Nachricht und dem gewünschten Grad der Tunnellängen-Verschleierung abwägen.

Im aktuellen Netzwerk sind die meisten tunnel 2 oder 3 Hops lang. Die aktuelle Implementierung verwendet eine 5-Datensatz-VTBM zum Aufbau von tunneln mit 4 Hops oder weniger und die 8-Datensatz-TBM für längere tunnel. Die 5-Datensatz-VTBM (die bei Fragmentierung in drei 1KB tunnel-Nachrichten passt) reduziert den Netzwerkverkehr und erhöht die Erfolgsrate beim Aufbau, da kleinere Nachrichten weniger wahrscheinlich verworfen werden.

Die Antwortnachricht muss den gleichen Typ und die gleiche Länge wie die Build-Nachricht haben.

### Spezifikation der Anfrage-Datensätze

Auch spezifiziert in der I2NP-Spezifikation [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

Klartext des Datensatzes, nur für den angefragten Hop sichtbar:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
Die Felder für die nächste tunnel ID und den nächsten router-Identitäts-Hash werden verwendet, um den nächsten Hop im tunnel anzugeben, obwohl sie für einen ausgehenden tunnel-Endpunkt angeben, wohin die umgeschriebene tunnel-Erstellungsantwortnachricht gesendet werden soll. Zusätzlich gibt die nächste Nachrichten-ID die Nachrichten-ID an, die die Nachricht (oder Antwort) verwenden soll.

Der tunnel layer key, tunnel IV key, reply key und reply IV sind jeweils zufällige 32-Byte-Werte, die vom Ersteller generiert werden und nur für diesen Build-Request-Datensatz verwendet werden.

Das Flags-Feld enthält folgendes (Bit-Reihenfolge: 76543210, Bit 7 ist MSB):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
Bit 7 zeigt an, dass der Hop ein Inbound-Gateway (IBGW) sein wird. Bit 6 zeigt an, dass der Hop ein Outbound-Endpunkt (OBEP) sein wird. Wenn keines der beiden Bits gesetzt ist, wird der Hop ein zwischengeschalteter Teilnehmer sein. Beide können nicht gleichzeitig gesetzt werden.

#### Erstellung von Anfragedatensätzen

Jeder Hop erhält eine zufällige Tunnel-ID, die nicht null ist. Die aktuellen und nächsten Hop-Tunnel-IDs werden ausgefüllt. Jeder Datensatz erhält einen zufälligen Tunnel-IV-Schlüssel, Antwort-IV, Ebenen-Schlüssel und Antwort-Schlüssel.

#### Request Record Verschlüsselung

Dieser Klartextdatensatz wird mit ElGamal 2048 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) verschlüsselt unter Verwendung des öffentlichen Verschlüsselungsschlüssels des Hops und in einen 528 Byte Datensatz formatiert:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
Im 512-Byte verschlüsselten Datensatz enthalten die ElGamal-Daten die Bytes 1-256 und 258-513 des 514-Byte ElGamal verschlüsselten Blocks [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Die beiden Padding-Bytes aus dem Block (die Null-Bytes an den Positionen 0 und 257) werden entfernt.

Da der Klartext das gesamte Feld verwendet, ist keine zusätzliche Auffüllung über `SHA256(cleartext) + cleartext` hinaus erforderlich.

Jeder 528-Byte-Datensatz wird dann iterativ verschlüsselt (unter Verwendung von AES-Entschlüsselung mit dem Antwortschlüssel und der Antwort-IV für jeden Hop), sodass die router-Identität nur für den jeweiligen Hop im Klartext vorliegt.

### Hop-Verarbeitung und Verschlüsselung

Wenn ein Hop eine TunnelBuildMessage empfängt, durchsucht er die darin enthaltenen Datensätze nach einem, der mit seinem eigenen identity hash (auf 16 Bytes gekürzt) beginnt. Anschließend entschlüsselt er den ElGamal-Block aus diesem Datensatz und ruft den geschützten Klartext ab. An diesem Punkt stellt er sicher, dass die tunnel-Anfrage kein Duplikat ist, indem er den AES-256-Antwortschlüssel in einen Bloom-Filter einspeist. Duplikate oder ungültige Anfragen werden verworfen. Datensätze, die nicht mit der aktuellen Stunde oder der vorherigen Stunde (falls kurz nach dem Stundenbeginn) gestempelt sind, müssen verworfen werden. Zum Beispiel: Nimm die Stunde aus dem Zeitstempel, wandle sie in eine vollständige Zeit um, und wenn sie mehr als 65 Minuten zurück oder 5 Minuten voraus liegt, ist sie ungültig. Der Bloom-Filter muss eine Dauer von mindestens einer Stunde (plus einige Minuten, um Uhrenabweichungen zu berücksichtigen) haben, damit doppelte Datensätze in der aktuellen Stunde, die nicht durch Überprüfung des Stunden-Zeitstempels im Datensatz abgelehnt werden, vom Filter abgelehnt werden.

Nachdem sie entschieden haben, ob sie der Teilnahme am tunnel zustimmen oder nicht, ersetzen sie den Datensatz, der die Anfrage enthalten hatte, durch einen verschlüsselten Antwortblock. Alle anderen Datensätze werden mit AES-256 [CRYPTO-AES](/docs/specs/cryptography/#aes) unter Verwendung des mitgelieferten Antwortschlüssels und IV verschlüsselt. Jeder wird separat mit AES/CBC unter Verwendung desselben Antwortschlüssels und Antwort-IV verschlüsselt. Der CBC-Modus wird nicht über Datensätze hinweg fortgesetzt (verkettet).

Jeder Hop kennt nur seine eigene Antwort. Wenn er zustimmt, wird er den tunnel bis zum Ablauf aufrechterhalten, auch wenn er nicht genutzt wird, da er nicht wissen kann, ob alle anderen Hops zugestimmt haben.

#### Reply Record Spezifikation

Nachdem der aktuelle Hop seinen Datensatz gelesen hat, ersetzt er ihn durch einen Antwortdatensatz, der angibt, ob er der Teilnahme am tunnel zustimmt oder nicht, und falls nicht, klassifiziert er seinen Ablehnungsgrund. Dies ist einfach ein 1-Byte-Wert, wobei 0x0 bedeutet, dass er der Teilnahme am tunnel zustimmt, und höhere Werte höhere Ablehnungsgrade bedeuten.

Die folgenden Ablehnungscodes sind definiert:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

Um andere Ursachen, wie das Herunterfahren des routers, vor Peers zu verbergen, verwendet die aktuelle Implementierung TUNNEL_REJECT_BANDWIDTH für fast alle Ablehnungen.

Die Antwort wird mit dem AES-Sitzungsschlüssel verschlüsselt, der im verschlüsselten Block übertragen wurde, und mit 495 Bytes an Zufallsdaten aufgefüllt, um die vollständige Datensatzgröße zu erreichen. Die Auffüllung wird vor dem Statusbyte platziert:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
Dies wird auch in der I2NP-Spezifikation [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) beschrieben.

### Tunnel Build Message Vorbereitung

Beim Erstellen einer neuen Tunnel Build Message müssen zunächst alle Build Request Records erstellt und asymmetrisch mit ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) verschlüsselt werden. Jeder Record wird dann präventiv mit den Antwortschlüsseln und IVs der früheren Hops im Pfad entschlüsselt, wobei AES [CRYPTO-AES](/docs/specs/cryptography/#aes) verwendet wird. Diese Entschlüsselung sollte in umgekehrter Reihenfolge durchgeführt werden, damit die asymmetrisch verschlüsselten Daten beim richtigen Hop im Klartext erscheinen, nachdem ihr Vorgänger sie verschlüsselt hat.

Die überschüssigen Datensätze, die für einzelne Anfragen nicht benötigt werden, werden vom Ersteller einfach mit zufälligen Daten gefüllt.

### Tunnel Build Message Delivery

Für ausgehende Tunnel erfolgt die Zustellung direkt vom tunnel-Ersteller zum ersten Hop, wobei die TunnelBuildMessage so verpackt wird, als wäre der Ersteller nur ein weiterer Hop im tunnel. Für eingehende Tunnel erfolgt die Zustellung über einen bestehenden ausgehenden tunnel. Der ausgehende tunnel stammt im Allgemeinen aus demselben Pool wie der neue tunnel, der aufgebaut wird. Wenn kein ausgehender tunnel in diesem Pool verfügbar ist, wird ein ausgehender Erkundungs-tunnel verwendet. Beim Start, wenn noch kein ausgehender Erkundungs-tunnel existiert, wird ein gefälschter 0-Hop ausgehender tunnel verwendet.

### Tunnel Build Message Endpoint-Behandlung

Bei der Erstellung eines outbound tunnel wird, wenn die Anfrage einen outbound endpoint erreicht (wie durch das 'allow messages to anyone' Flag bestimmt), der Hop wie üblich verarbeitet, wobei eine Antwort anstelle des Datensatzes verschlüsselt und alle anderen Datensätze verschlüsselt werden. Da es jedoch keinen 'next hop' gibt, an den die TunnelBuildMessage weitergeleitet werden könnte, werden stattdessen die verschlüsselten Antwortdatensätze in eine TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) oder VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) eingesetzt (der Nachrichtentyp und die Anzahl der Datensätze müssen mit denen der Anfrage übereinstimmen) und an den in der Anfrage angegebenen reply tunnel übermittelt. Dieser reply tunnel leitet die Tunnel Build Reply Message zurück an den tunnel-Ersteller weiter, genau wie bei jeder anderen Nachricht [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). Der tunnel-Ersteller verarbeitet sie dann wie unten beschrieben.

Der Reply-Tunnel wurde vom Ersteller wie folgt ausgewählt: Im Allgemeinen ist es ein eingehender Tunnel aus demselben Pool wie der neue ausgehende Tunnel, der erstellt wird. Wenn kein eingehender Tunnel in diesem Pool verfügbar ist, wird ein eingehender Exploratory-Tunnel verwendet. Beim Start, wenn noch kein eingehender Exploratory-Tunnel existiert, wird ein gefälschter 0-Hop eingehender Tunnel verwendet.

Für die Erstellung eines inbound tunnel erreicht die Anfrage den inbound endpoint (auch bekannt als tunnel creator), es ist nicht erforderlich, eine explizite Tunnel Build Reply Message zu generieren, und der router verarbeitet jede der Antworten wie folgt.

### Tunnel Build Reply Nachrichtenverarbeitung

Um die Antwortdatensätze zu verarbeiten, muss der Ersteller einfach jeden Datensatz einzeln mit AES entschlüsseln, wobei er den Antwortschlüssel und IV jedes Hops im tunnel nach dem Peer verwendet (in umgekehrter Reihenfolge). Dies legt dann die Antwort frei, die angibt, ob sie der Teilnahme am tunnel zustimmen oder warum sie ablehnen. Wenn alle zustimmen, gilt der tunnel als erstellt und kann sofort verwendet werden, aber wenn jemand ablehnt, wird der tunnel verworfen.

Die Zustimmungen und Ablehnungen werden im Profil jedes Peers [PEER-SELECTION](/docs/overview/tunnel-routing/) vermerkt, um bei zukünftigen Bewertungen der Peer-Tunnel-Kapazität verwendet zu werden.

## Geschichte und Hinweise

Diese Strategie entstand während einer Diskussion in der I2P-Mailingliste zwischen Michael Rogers, Matthew Toseland (toad) und jrandom bezüglich des Predecessor-Angriffs. Siehe [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html), [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html). Sie wurde in Release 0.6.1.10 am 2006-02-16 eingeführt, was das letzte Mal war, dass eine nicht-rückwärtskompatible Änderung in I2P vorgenommen wurde.

Hinweise:

- Dieses Design verhindert nicht, dass zwei feindliche Peers innerhalb eines tunnels ein oder mehrere Anfrage- oder Antwort-Datensätze markieren, um zu erkennen, dass sie sich im selben tunnel befinden, aber dies kann vom tunnel-Ersteller beim Lesen der Antwort erkannt werden, wodurch der tunnel als ungültig markiert wird.
- Dieses Design beinhaltet keinen Arbeitsnachweis für den asymmetrisch verschlüsselten Abschnitt, obwohl der 16-Byte-Identitäts-Hash halbiert werden könnte, wobei die Hälfte durch eine Hashcash-Funktion mit Kosten von bis zu 2^64 ersetzt wird.
- Dieses Design allein verhindert nicht, dass zwei feindliche Peers innerhalb eines tunnels Timing-Informationen verwenden, um zu bestimmen, ob sie sich im selben tunnel befinden. Die Verwendung von stapelweiser und synchronisierter Anfrage-Zustellung könnte helfen (Anfragen sammeln und sie zur (ntp-synchronisierten) Minute versenden). Dies ermöglicht es Peers jedoch, die Anfragen zu 'markieren', indem sie diese verzögern und die Verzögerung später im tunnel erkennen, obwohl möglicherweise das Verwerfen von Anfragen, die nicht in einem kleinen Zeitfenster zugestellt werden, funktionieren würde (obwohl dies einen hohen Grad an Uhren-Synchronisation erfordern würde). Alternativ könnten einzelne Hops eine zufällige Verzögerung einfügen, bevor sie die Anfrage weiterleiten?
- Gibt es nicht-fatale Methoden zum Markieren der Anfrage?
- Der Zeitstempel mit einer einstündigen Auflösung wird zur Replay-Verhinderung verwendet. Die Einschränkung wurde erst ab Version 0.9.16 durchgesetzt.

## Zukünftige Arbeiten

- In der aktuellen Implementierung lässt der Originator einen Datensatz für sich selbst leer. Daher kann eine Nachricht mit n Datensätzen nur einen tunnel mit n-1 Hops aufbauen. Dies scheint für Inbound-tunnels notwendig zu sein (wo der vorletzte Hop das Hash-Präfix für den nächsten Hop sehen kann), aber nicht für Outbound-tunnels. Dies ist zu untersuchen und zu verifizieren. Falls es möglich ist, den verbleibenden Datensatz zu verwenden, ohne die Anonymität zu gefährden, sollten wir dies tun.
- Weitere Analyse möglicher Tagging- und Timing-Angriffe, die in den obigen Hinweisen beschrieben sind.
- Nur VTBM verwenden; keine alten Peers auswählen, die es nicht unterstützen.
- Der Build Request Record spezifiziert keine tunnel-Lebensdauer oder Ablaufzeit; jeder Hop lässt den tunnel nach 10 Minuten ablaufen, was eine netzwerkweite fest codierte Konstante ist. Wir könnten ein Bit im Flag-Feld verwenden und 4 (oder 8) Bytes aus dem Padding nehmen, um eine Lebensdauer oder Ablaufzeit zu spezifizieren. Der Anforderer würde diese Option nur spezifizieren, wenn alle Teilnehmer sie unterstützen würden.

## Referenzen

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - BuildRequestRecord Spezifikation
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - AES-Verschlüsselung
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - ElGamal-Verschlüsselung
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage

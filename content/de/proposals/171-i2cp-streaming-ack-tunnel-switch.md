---
title: "I2CP-Flag für den Wechsel ausgehender Tunnel"
number: "171"
author: "onon, eyedeekay"
created: "2026-05-19"
lastupdated: "2026-05-23"
status: "Entwurf"
toc: true
---

## Übersicht

Streaming-Client-Verbindungen können ins Stocken geraten, wenn Zustellbestätigungen stillschweigend verloren gehen. Der Sender sendet erneut, bis eine Bestätigung empfangen wird oder die Verbindung abgebaut wird, wobei keine zuverlässige Möglichkeit besteht, zu überprüfen, ob die Bestätigungen die andere Seite erreichen. Dieser Vorschlag fügt ein neues Flag-Bit zum Flags-Feld von [SendMessageExpiresMessage](/docs/specs/i2cp/) hinzu, sodass ein Client den Router anweisen kann, für nachfolgende Nachrichten an dasselbe Ziel einen anderen Outbound-Tunnel auszuwählen. Das Streaming-Protokoll nutzt dieses Bit, um beim Erkennen einer blockierten Verbindung einen Tunnelwechsel einzuleiten.

## Auslöser

Zwei Bedingungen SOLLTEN den Client veranlassen, die Kennung in der nächsten ausgehenden Nachricht zu setzen. Diese Bedingungen werden auf der Streaming-Schicht gemessen.

**Absenderseite**

Innerhalb des aktuellen Wiederholungs-Timeout-Intervalls des Clients wurde keine Bestätigung empfangen.

**Empfängerseite**

Der Empfänger hat beobachtet, dass das entfernte Ende dieselben Daten mehrfach erneut überträgt, was darauf hinweist, dass seine Bestätigungen (Acknowledgments) das entfernte Ende nicht erreichen. Der Empfänger SOLLTE dieses Flag bei seiner nächsten ausgehenden I2CP-Nachricht setzen, damit die Bestätigungen das entfernte Ende über einen anderen Pfad erreichen. Der Empfänger MUSS warten, bis: (1) er ein Duplikat empfangen hat, (2) er mindestens eine Bestätigung gesendet hat und (3) das entfernte Ende erneut eine Wiederholungsübertragung durchgeführt hat, bevor er das Flag setzt.

Um Zeitkorrelationsangriffe zu begrenzen, DARF ein Client das Flag pro Verbindung nicht öfter als einmal innerhalb eines 10-Sekunden-Fensters setzen. Der Client SOLLTE das Setzen des Flags außerdem um eine zufällige Verzögerung (Jitter) verzögern, die gleichmäßig aus `[0, min(T/4, 2000ms)]` gezogen wird, wobei T das aktuelle Wiedersendungs-Timeout (retransmit timeout) des Clients in Millisekunden ist, nachdem die Blockierung erkannt wurde, um die Genauigkeit von Zeitkorrelationen zu verringern.

## Spezifikation

Das Flags-Feld von [SendMessageExpiresMessage](/docs/specs/i2cp/) belegt die oberen 2 Bytes nach dem Date-Feld (umdefiniert ab Version 0.8.4) und wird big-endian übertragen. Bit 15 ist derzeit unbenutzt; dieser Vorschlag definiert es.

Bit-Reihenfolge: 15...0

| Bit | Name | Beschreibung |
|-----|------|-------------|
| 15 | SWITCH_OUTBOUND_TUNNEL | Wenn 1, SOLLTE der Router einen anderen ausgehenden Tunnel aus seinem Pool für nachfolgende Nachrichten an dieses Ziel auswählen. Falls kein alternativer Tunnel verfügbar ist, wird dieses Flag stillschweigend ignoriert. Der Router DARF den zuvor verwendeten Tunnel nicht schließen oder außer Betrieb nehmen, nur weil dieses Flag gesetzt wurde. |
Diese Kennung hat standardmäßig den Wert 0. Router, die sie nicht implementieren, MÜSSEN sie fehlerfrei ignorieren.

## Implementierungshinweise

Wenn `SWITCH_OUTBOUND_TUNNEL` gesetzt ist, SOLLTE der Router ein Tunnel gleichmäßig zufällig aus dem Outbound-Pool auswählen, ausgenommen:

- den derzeit für diese Sitzung verwendeten Tunnel sowie
- den jeweils zuletzt fehlgeschlagenen Tunnel im Pool, falls vorhanden.

Alle anderen Metriken zur Tunnel-Integrität, Erstellungszeiten oder Auswahlverläufe DÜRFEN die Auswahl nicht beeinflussen, da eine gewichtete Auswahl Sybil-Angreifer begünstigen könnte. Wenn nach diesen Ausschlüssen kein geeigneter Tunnel im Pool vorhanden ist, wird das Flag stillschweigend ignoriert.

Diese Option verursacht keine zusätzlichen Tunnel-Nachrichten; das Wechseln von Tunneln kann die scheinbare Latenz verändern. Die ratenbegrenzung von 10 Sekunden pro Verbindung (siehe Auslöser) verhindert übermäßiges Wechseln.

## Überlegungen zur Anonymität

Die Flags in [SendMessageExpiresMessage](/docs/specs/i2cp/) werden über I2CP übertragen, was eine lokale Schnittstelle zwischen dem Client und seinem eigenen Router darstellt. Sie sind für Netzwerkbeobachter nicht sichtbar.

Das Anonymitätsrisiko basiert auf Datenverkehrsmustern: Ein Angreifer mit Sicht auf mehrere Tunnelendpunkte kann beobachten, *wann* sich die Tunnelnutzung ändert.

Das Wechseln von ausgehenden Tunneln als direkte Reaktion auf eine Blockierung auf Client-Seite erzeugt ein erkennbares Verhaltensmuster. Es gibt zwei konkrete Beobachtungsvektoren:

**Sybil-Angriff auf die ersten Stationen ausgehender Tunnel**

Der erste Hop jedes ausgehenden Tunnels sieht den gesamten Datenverkehr, der von dem Router des Absenders in diesen Tunnel eingeht. Ein Angreifer, der den ersten Hop von mehr als einem Tunnel im Pool des Absenders kontrolliert, kann beobachten, wie der Datenverkehr auf einem ersten Hop kurzzeitig stoppt und kurz darauf auf einem anderen beginnt, wodurch beide Tunnel mit demselben Absender verknüpft werden. Bei einem Pool von N Tunneln hat ein Angreifer, der K erste Hops kontrolliert, eine Wahrscheinlichkeit von K/N, ein bestimmtes Wechselereignis zu beobachten.

**Timing von Datenverkehrsunterbrechungen**

Während des Stillstands sendet der Client keine neuen Daten, weshalb der alte ausgehende Tunnel verstummt. Wenn der Wechsel erfolgt, setzt der Datenverkehr auf einem anderen Pfad wieder ein. Ein Angreifer mit Beobachtungspunkt am Router des Senders – beispielsweise der Internetdienstanbieter des Senders oder der erste Hop selbst – kann das Muster aus Stille und anschließender Wiederaufnahme beobachten. Die Länge der Pause verrät zudem eine Annäherung an den aktuellen Retransmit-Timeout-Wert des Clients.

Clients MÜSSEN die Rate-Limiting- und Jitter-Anforderungen in Triggers einhalten.

## Referenzen

- [I2CP-Spezifikation](/docs/specs/i2cp/)

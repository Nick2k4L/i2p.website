---
title: "Service Records in LS2"
number: "167"
author: "zzz, orignal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Closed"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## Status
Am 2. Überprüfung am 2025-04-01 genehmigt; Spezifikationen wurden aktualisiert; noch nicht implementiert.


## Übersicht

I2P verfügt über kein zentrales DNS-System.  
Allerdings ermöglicht das Adressbuch zusammen mit dem b32-Hostnamensystem dem Router, vollständige Ziele aufzulösen und Lease-Sets abzurufen, die eine Liste von Gateways und Schlüsseln enthalten, sodass Clients eine Verbindung zu diesem Ziel herstellen können.

Lease-Sets sind also in gewisser Weise vergleichbar mit einem DNS-Eintrag. Derzeit gibt es jedoch keine Möglichkeit herauszufinden, ob der Host bestimmte Dienste unterstützt, entweder auf diesem Ziel oder einem anderen, ähnlich wie DNS-[SRV-Einträge](https://en.wikipedia.org/wiki/SRV_record) gemäß [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782).

Die erste Anwendung dafür könnte Peer-to-Peer-E-Mail sein.  
Weitere mögliche Anwendungen: DNS, GNS, Schlüsselserver, Zertifizierungsstellen, Zeitserver, BitTorrent, Kryptowährungen, andere Peer-to-Peer-Anwendungen.


## Verwandte Vorschläge und Alternativen

### Dienstelisten

Die LS2-[Vorschlag 123](/proposals/123-new-netdb-entries/) definierte „Diensteinträge“, die angaben, dass ein Ziel an einem globalen Dienst teilnimmt. Die Floodfills würden diese Einträge zu globalen „Dienstelisten“ aggregieren.  
Dies wurde nie implementiert aufgrund von Komplexität, fehlender Authentifizierung, Sicherheits- und Spam-Bedenken.

Dieser Vorschlag unterscheidet sich darin, dass er eine Nachschlagefunktion für einen Dienst eines bestimmten Ziels bereitstellt, nicht für einen globalen Pool von Zielen für einen globalen Dienst.

### GNS

GNS schlägt vor, dass jeder seinen eigenen DNS-Server betreibt.  
Dieser Vorschlag ist ergänzend, da wir Diensteinträge verwenden könnten, um anzugeben, dass GNS (oder DNS) unterstützt wird, mit einem standardisierten Dienstnamen „domain“ auf Port 53.

### Dot well-known

Es wurde [vorgeschlagen](http://i2pforum.i2p/viewtopic.php?p=3102), dass Dienste über eine HTTP-Anfrage an  
/.well-known/i2pmail.key aufzulösen seien. Dies erfordert, dass jeder Dienst eine zugehörige Webseite zum Hosten des Schlüssels hat. Die meisten Benutzer betreiben keine Webseiten.

Ein Workaround wäre, anzunehmen, dass ein Dienst für eine b32-Adresse tatsächlich auf dieser b32-Adresse läuft. So erfordert die Suche nach dem Dienst für example.i2p das Abrufen per HTTP von http://example.i2p/.well-known/i2pmail.key, aber ein Dienst für aaa...aaa.b32.i2p erfordert diese Nachschlagefunktion nicht, sondern kann direkt verbunden werden.

Es gibt jedoch eine Mehrdeutigkeit, da example.i2p auch über seine b32-Adresse adressiert werden kann.

### MX-Einträge

SRV-Einträge sind einfach eine generische Version von MX-Einträgen für jeden Dienst.  
„_smtp._tcp“ ist der „MX“-Eintrag.  
MX-Einträge sind nicht erforderlich, wenn wir SRV-Einträge haben, und MX-Einträge allein bieten keinen generischen Eintrag für jeden Dienst.


## Entwurf

Diensteinträge werden im Optionsabschnitt in [LS2](/docs/specs/common-structures/) platziert. Der LS2-Optionsabschnitt ist derzeit ungenutzt.  
Nicht unterstützt für LS1.  
Dies ist vergleichbar mit dem [Tunnel-Bandbreiten-Vorschlag](/proposals/168-tunnel-bandwidth/), der Optionen für Tunnel-Bau-Einträge definiert.

Um eine Dienstadresse für einen bestimmten Hostnamen oder b32 aufzulösen, holt der Router das Lease-Set und sucht den Diensteintrag in den Eigenschaften.

Der Dienst kann auf demselben Ziel wie das LS selbst gehostet werden oder auf einen anderen Hostnamen/b32 verweisen.

Wenn das Ziel des Dienstes unterschiedlich ist, muss das Ziel-LS ebenfalls einen Diensteintrag enthalten, der auf sich selbst verweist und angibt, dass es den Dienst unterstützt.

Der Entwurf erfordert keine besondere Unterstützung oder Zwischenspeicherung oder Änderungen an den Floodfills.  
Nur der Publisher des Lease-Sets und der Client, der einen Diensteintrag nachschlägt, müssen diese Änderungen unterstützen.

Kleine Erweiterungen von I2CP und SAM werden vorgeschlagen, um Clients die Abrufung von Diensteinträgen zu erleichtern.



## Spezifikation

### LS2-Optionsspezifikation

LS2-Optionen MÜSSEN nach Schlüssel sortiert sein, damit die Signatur invariant ist.

Folgendermaßen definiert:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Der symbolische Name des gewünschten Dienstes. Muss Kleinbuchstaben sein. Beispiel: „smtp“.  
  Erlaubte Zeichen sind [a-z0-9-] und dürfen nicht mit einem „-“ beginnen oder enden.  
  Standard-Bezeichner aus der [DNS-SD Service Types registry](http://www.dns-sd.org/ServiceTypes.html) oder Linux /etc/services müssen verwendet werden, wenn dort definiert.
- proto := Das Transportprotokoll des gewünschten Dienstes. Muss Kleinbuchstaben sein, entweder „tcp“ oder „udp“.  
  „tcp“ bedeutet Streaming und „udp“ bedeutet repliable Datagramme.  
  Protokollindikatoren für Raw-Datagramme und Datagram2 können später definiert werden.  
  Erlaubte Zeichen sind [a-z0-9-] und dürfen nicht mit einem „-“ beginnen oder enden.
- optionvalue := self | srvrecord[,srvrecord]*
- self := „0“ ttl port [appoptions]
- srvrecord := „1“ ttl priority weight port target [appoptions]
- ttl := Gültigkeitsdauer (time to live), ganze Sekunden. Positive ganze Zahl. Beispiel: „86400“.  
  Ein Minimum von 86400 (ein Tag) wird empfohlen, siehe Abschnitt Empfehlungen unten für Details.
- priority := Die Priorität des Zielhosts, niedrigere Werte bedeuten bevorzugt. Nicht-negative ganze Zahl. Beispiel: „0“  
  Nur nützlich, wenn mehr als ein Eintrag vorhanden ist, aber erforderlich, auch wenn nur ein Eintrag existiert.
- weight := Ein relatives Gewicht für Einträge mit derselben Priorität. Höhere Werte bedeuten größere Auswahlwahrscheinlichkeit. Nicht-negative ganze Zahl. Beispiel: „0“  
  Nur nützlich, wenn mehr als ein Eintrag vorhanden ist, aber erforderlich, auch wenn nur ein Eintrag existiert.
- port := Der I2CP-Port, auf dem der Dienst zu finden ist. Nicht-negative ganze Zahl. Beispiel: „25“  
  Port 0 ist erlaubt, aber nicht empfohlen.
- target := Der Hostname oder b32 des Ziels, das den Dienst bereitstellt. Ein gültiger [Hostname](/docs/overview/naming/). Muss Kleinbuchstaben sein.  
  Beispiel: „aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p“ oder „example.i2p“.  
  b32 wird empfohlen, es sei denn, der Hostname ist „allgemein bekannt“, d.h. in offiziellen oder Standard-Adressbüchern.
- appoptions := Beliebiger Text, spezifisch für die Anwendung, darf kein „ “ oder „,“ enthalten. Kodierung ist UTF-8.

### Beispiele

In LS2 für aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, verweist auf einen SMTP-Server:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

In LS2 für aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, verweist auf zwei SMTP-Server:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

In LS2 für bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, verweist auf sich selbst als SMTP-Server:

    "_smtp._tcp" "0 999999 25"

Mögliche Formatierung zur Umleitung von E-Mails (siehe unten):

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### Grenzwerte

Die für LS2-Optionen verwendete Mapping-Datenstruktur begrenzt Schlüssel und Werte auf maximal 255 Bytes (nicht Zeichen).  
Bei einem b32-Ziel ist der optionvalue etwa 67 Bytes lang, sodass nur 3 Einträge passen.  
Möglicherweise nur einer oder zwei bei langem appoptions-Feld, oder bis zu vier oder fünf bei kurzem Hostnamen.  
Dies sollte ausreichen; mehrere Einträge sollten selten sein.


### Unterschiede zu RFC 2782

- Keine abschließenden Punkte
- Kein Name nach dem proto
- Kleinbuchstaben erforderlich
- Im Textformat mit durch Komma getrennten Einträgen, nicht im binären DNS-Format
- Unterschiedliche Eintrags-Typ-Indikatoren
- Zusätzliches appoptions-Feld


### Hinweise

Platzhalter wie (Stern), (Stern)._tcp oder _tcp sind nicht erlaubt.  
Jeder unterstützte Dienst muss seinen eigenen Eintrag haben.



### Dienstnamens-Registry

Nicht-standardisierte Bezeichner, die nicht in der [DNS-SD Service Types registry](http://www.dns-sd.org/ServiceTypes.html) oder Linux /etc/services aufgeführt sind, können beantragt und der [common structures specification](/docs/specs/common-structures/) hinzugefügt werden.

Dienstspezifische appoptions-Formate können dort ebenfalls hinzugefügt werden.


### I2CP-Spezifikation

Das [I2CP-Protokoll](/docs/specs/i2cp/) muss erweitert werden, um Dienstnachschlagen zu unterstützen.  
Zusätzliche MessageStatusMessage- und/oder HostReplyMessage-Fehlercodes im Zusammenhang mit Dienstnachschlagen sind erforderlich.  
Um die Nachschlagefunktion allgemein zu halten, nicht nur spezifisch für Diensteinträge, ist der Entwurf darauf ausgelegt, den Abruf aller LS2-Optionen zu unterstützen.

Implementierung: Erweitere HostLookupMessage, um Anfragen für LS2-Optionen für Hash, Hostnamen und Ziel hinzuzufügen (Anfragetypen 2-4).  
Erweitere HostReplyMessage, um die Optionszuordnung bei Anfrage hinzuzufügen.  
Erweitere HostReplyMessage um zusätzliche Fehlercodes.

Optionszuordnungen können kurzzeitig auf Client- oder Router-Seite zwischengespeichert oder negativ zwischengespeichert werden, abhängig von der Implementierung.  
Empfohlene maximale Zeit ist eine Stunde, es sei denn, die TTL des Diensteintrags ist kürzer.  
Diensteinträge können bis zur von der Anwendung, dem Client oder dem Router angegebenen TTL zwischengespeichert werden.

Erweitere die Spezifikation wie folgt:

#### Konfigurationsoptionen

Füge Folgendes zu den [I2CP-Konfigurationsoptionen](/docs/specs/i2cp/) hinzu:

i2cp.leaseSetOption.nnn

Optionen, die in das Lease-Set eingefügt werden sollen. Nur verfügbar für LS2.  
nnn beginnt bei 0. Der Optionswert enthält „key=value“.  
(zitate nicht einschließen)

Beispiel:
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### HostLookup-Nachricht

- Nachschlagetyp 2: Hash-Nachschlagefunktion, fordert Optionszuordnung an
- Nachschlagetyp 3: Hostnamen-Nachschlagefunktion, fordert Optionszuordnung an
- Nachschlagetyp 4: Ziel-Nachschlagefunktion, fordert Optionszuordnung an

Für Nachschlagetyp 4 ist Element 5 ein Ziel (Destination).


#### HostReply-Nachricht

Für Nachschlagetypen 2-4 muss der Router das Lease-Set abrufen, auch wenn der Suchschlüssel im Adressbuch steht.

Bei Erfolg enthält die HostReply die Optionszuordnung aus dem Lease-Set und fügt sie als Element 5 nach dem Ziel ein.  
Wenn keine Optionen in der Zuordnung vorhanden sind oder das Lease-Set Version 1 war, wird sie dennoch als leere Zuordnung eingefügt (zwei Bytes: 0 0).  
Alle Optionen aus dem Lease-Set werden eingefügt, nicht nur Diensteinträge.  
Zum Beispiel können Optionen für zukünftig definierte Parameter vorhanden sein.

Bei einem Fehler beim Abruf des Lease-Sets enthält die Antwort einen neuen Fehlercode 6 (Lease-Set-Abruffehler) und enthält keine Zuordnung.  
Wenn Fehlercode 6 zurückgegeben wird, kann das Feld Destination vorhanden sein oder auch nicht.  
Es ist vorhanden, wenn eine Hostnamen-Nachschlagefunktion im Adressbuch erfolgreich war, oder wenn eine vorherige Nachschlagefunktion erfolgreich war und das Ergebnis zwischengespeichert wurde, oder wenn die Destination in der Nachschlage-Nachricht vorhanden war (Nachschlagetyp 4).

Wenn ein Nachschlagetyp nicht unterstützt wird, enthält die Antwort einen neuen Fehlercode 7 (Nachschlagetyp nicht unterstützt).



### SAM-Spezifikation

Das [SAMv3-Protokoll](/docs/api/samv3/) muss erweitert werden, um Dienstnachschlagen zu unterstützen.

Erweitere NAMING LOOKUP wie folgt:

NAMING LOOKUP NAME=example.i2p OPTIONS=true fordert die Optionszuordnung in der Antwort an.

NAME kann eine vollständige base64-Destination sein, wenn OPTIONS=true.

Wenn die Zielauflösung erfolgreich war und Optionen im Lease-Set vorhanden waren, folgen in der Antwort nach der Destination ein oder mehrere Optionen im Format OPTION:key=value.  
Jede Option hat ein separates OPTION:-Präfix.  
Alle Optionen aus dem Lease-Set werden eingefügt, nicht nur Diensteinträge.  
Zum Beispiel können Optionen für zukünftig definierte Parameter vorhanden sein.  
Beispiel:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Schlüssel, die „=“ enthalten, sowie Schlüssel oder Werte, die einen Zeilenumbruch enthalten, gelten als ungültig, und das Schlüssel-Wert-Paar wird aus der Antwort entfernt.

Wenn keine Optionen im Lease-Set gefunden wurden oder das Lease-Set Version 1 war, enthält die Antwort keine Optionen.

Wenn OPTIONS=true in der Anfrage war und das Lease-Set nicht gefunden wurde, wird ein neuer Ergebniswert LEASESET_NOT_FOUND zurückgegeben.


## Alternative zur Namensauflösung

Ein alternativer Entwurf wurde in Betracht gezogen, um die Nachschlagefunktion von Diensten als vollständigen Hostnamen zu unterstützen, z.B. _smtp._tcp.example.i2p,  
indem die [Namensspezifikation](/docs/overview/naming/) aktualisiert wird, um die Behandlung von Hostnamen, die mit „_“ beginnen, festzulegen.  
Dies wurde aus zwei Gründen abgelehnt:

- I2CP- und SAM-Änderungen wären weiterhin erforderlich, um TTL- und Portinformationen an den Client weiterzuleiten.
- Es wäre keine allgemeine Funktion, die verwendet werden könnte, um andere LS2-Optionen abzurufen, die in Zukunft definiert werden könnten.


## Empfehlungen

Server sollten eine TTL von mindestens 86400 angeben und den Standardport für die Anwendung verwenden.



## Erweiterte Funktionen

### Rekursive Nachschlagen

Es könnte wünschenswert sein, rekursive Nachschlagen zu unterstützen, bei denen jedes nachfolgende Lease-Set auf einen Diensteintrag geprüft wird, der auf ein anderes Lease-Set verweist, DNS-artig.  
Dies ist wahrscheinlich nicht notwendig, zumindest nicht in einer ersten Implementierung.

TODO



### Anwendungsspezifische Felder

Es könnte wünschenswert sein, anwendungsspezifische Daten im Diensteintrag zu haben.  
Zum Beispiel könnte der Betreiber von example.i2p angeben wollen, dass E-Mails an example@mail.i2p weitergeleitet werden sollen. Der Teil „example@“ müsste in einem separaten Feld des Diensteintrags stehen oder vom Ziel entfernt werden.

Auch wenn der Betreiber seinen eigenen E-Mail-Dienst betreibt, könnte er angeben wollen, dass E-Mails an example@example.i2p gesendet werden sollen. Die meisten I2P-Dienste werden von einer einzelnen Person betrieben.  
Ein separates Feld könnte hier ebenfalls hilfreich sein.

TODO wie dies auf generische Weise umzusetzen ist


### Für E-Mail erforderliche Änderungen

Außerhalb des Geltungsbereichs dieses Vorschlags. Weitere Details finden sich in der [Diskussion auf i2pforum](http://i2pforum.i2p/viewtopic.php?p=3102).


## Implementierungshinweise

Das Zwischenspeichern von Diensteinträgen bis zur TTL kann vom Router oder der Anwendung durchgeführt werden, abhängig von der Implementierung. Ob persistent zwischengespeichert wird, ist ebenfalls implementierungsabhängig.

Bei Nachschlagen muss auch das Ziel-Lease-Set abgerufen und überprüft werden, ob es einen „self“-Eintrag enthält, bevor das Ziel an den Client zurückgegeben wird.


## Sicherheitsanalyse

Da das Lease-Set signiert ist, werden alle darin enthaltenen Diensteinträge durch den Signaturschlüssel des Ziels authentifiziert.

Die Diensteinträge sind öffentlich und für Floodfills sichtbar, es sei denn, das Lease-Set ist verschlüsselt.  
Jeder Router, der das Lease-Set anfordert, kann die Diensteinträge sehen.

Ein SRV-Eintrag, der nicht „self“ ist (d.h. auf ein anderes Hostnamen-/b32-Ziel verweist), erfordert nicht die Zustimmung des adressierten Hostnamens/b32.  
Es ist unklar, ob eine Umleitung eines Dienstes zu einem beliebigen Ziel einen Angriff ermöglichen könnte oder welchen Zweck ein solcher Angriff hätte.  
Dieser Vorschlag mindert jedoch einen solchen Angriff, indem er verlangt, dass das Ziel ebenfalls einen „self“-SRV-Eintrag veröffentlicht. Implementierer müssen im Lease-Set des Ziels auf einen „self“-Eintrag prüfen.


## Kompatibilität

LS2: Keine Probleme. Alle bekannten Implementierungen ignorieren derzeit das Optionsfeld in LS2 und überspringen korrekt ein nicht-leeres Optionsfeld.  
Dies wurde während der Entwicklung von LS2 durch Tests sowohl in Java I2P als auch in i2pd bestätigt.  
LS2 wurde in Version 0.9.38 im Jahr 2016 implementiert und wird von allen Router-Implementierungen gut unterstützt.  
Der Entwurf erfordert keine besondere Unterstützung, Zwischenspeicherung oder Änderungen an den Floodfills.

Namensgebung: „_“ ist kein gültiges Zeichen in I2P-Hostnamen.

I2CP: Nachschlagetypen 2-4 sollten nicht an Router gesendet werden, die unterhalb der minimalen API-Version liegen, ab der sie unterstützt werden (TBD).

SAM: Der Java-SAM-Server ignoriert zusätzliche Schlüssel/Werte wie OPTIONS=true.  
i2pd sollte dies ebenfalls tun, muss aber noch verifiziert werden.  
SAM-Clients erhalten die zusätzlichen Werte in der Antwort nur, wenn sie mit OPTIONS=true angefordert wurden.  
Ein Versionsinkrement sollte nicht erforderlich sein.


## Migration

Implementierungen können jederzeit Unterstützung hinzufügen, keine Koordination ist erforderlich,  
außer einer Einigung über die effektive API-Version für die I2CP-Änderungen.  
SAM-Kompatibilitätsversionen für jede Implementierung werden in der SAM-Spezifikation dokumentiert.


## Referenzen

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)

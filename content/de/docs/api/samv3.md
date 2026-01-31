---
title: "SAM V3"
description: "Einfaches Anonymes Messaging-Protokoll für Nicht-Java I2P-Anwendungen"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM ist ein einfaches Client-Protokoll für die Interaktion mit I2P. SAM ist das empfohlene Protokoll für Nicht-Java-Anwendungen, um sich mit dem I2P-Netzwerk zu verbinden, und wird von mehreren router-Implementierungen unterstützt. Java-Anwendungen sollten die Streaming- oder I2CP-APIs direkt verwenden.

SAMv3 wurde in I2P Release 0.7.3 (Mai 2009) eingeführt und ist eine stabile und unterstützte Schnittstelle. 3.1 ist ebenfalls stabil und unterstützt die Signaturtyp-Option, die dringend empfohlen wird. Neuere 3.x-Versionen unterstützen erweiterte Funktionen. Beachten Sie, dass i2pd derzeit die meisten 3.2- und 3.3-Funktionen nicht unterstützt.

Alternativen: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (veraltet)](/docs/api/bob). Veraltete Versionen: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Bekannte SAM-Bibliotheken

Warnung: Einige davon könnten sehr alt oder nicht mehr unterstützt sein. Keine wird vom I2P-Projekt getestet, überprüft oder gewartet, sofern unten nicht anders vermerkt. Führen Sie Ihre eigene Recherche durch.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Library Name</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">Version</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">STREAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">DGRAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">RAW</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2psam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++, C wrapper</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2psam">github.com/i2p/i2psam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">gosam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/goSam">github.com/eyedeekay/goSam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">sam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/sam3">github.com/eyedeekay/sam3</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">onramp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/onramp">github.com/eyedeekay/onramp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">txi2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/str4d/txi2p">github.com/str4d/txi2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.socket</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/majestrate/i2p.socket">github.com/majestrate/i2p.socket</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/l-n-s/i2plib">github.com/l-n-s/i2plib</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib-fork</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/weko/i2plib-fork">codeberg.org/weko/i2plib-fork</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Py2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://i2pgit.org/robin/Py2p">i2pgit.org/robin/Py2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-rs</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2p-rs">github.com/i2p/i2p-rs</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">libsam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/libsam3">github.com/i2p/libsam3</a><br>(Maintained by the I2P project)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">mooni2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Lua</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/villain/mooni2p">notabug.org/villain/mooni2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">haskell-network-anonymous-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Haskell</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/solatis/haskell-network-anonymous-i2p">github.com/solatis/haskell-network-anonymous-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-sam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/diva.exchange/i2p-sam">codeberg.org/diva.exchange/i2p-sam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">node-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/redhog/node-i2p">github.com/redhog/node-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Jsam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/Jsam">github.com/eyedeekay/Jsam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">I2PSharp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/MohA39/I2PSharp">github.com/MohA39/I2PSharp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2pdotnet</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/SamuelFisher/i2pdotnet">github.com/SamuelFisher/i2pdotnet</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.rb</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Ruby</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/dryruby/i2p.rb">github.com/dryruby/i2p.rb</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">solitude</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/syvita/solitude">github.com/syvita/solitude</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Samty</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/acetone/samty">notabug.org/acetone/samty</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">bitcoin</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/bitcoin/bitcoin/blob/master/src/i2p.cpp">source (not a library, but good reference code)</a></td>
    </tr>
  </tbody>
</table>
## Schnellstart

Um eine grundlegende, ausschließlich auf TCP basierende Peer-to-Peer-Anwendung zu implementieren, muss der Client die folgenden Befehle unterstützen:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Erforderlich für alle folgenden Befehle
- `DEST GENERATE SIGNATURE_TYPE=7` - Um unseren privaten Schlüssel und destination zu generieren
- `NAMING LOOKUP NAME=...` - Um .i2p-Adressen in destinations umzuwandeln
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Erforderlich für STREAM CONNECT und STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Um ausgehende Verbindungen herzustellen
- `STREAM ACCEPT ID=...` - Um eingehende Verbindungen zu akzeptieren

## Allgemeine Anleitung für Entwickler

### Anwendungsdesign

SAM-Sessions (oder innerhalb von I2P, tunnel pools oder Sets von tunneln) sind darauf ausgelegt, langlebig zu sein. Die meisten Anwendungen benötigen nur eine Session, die beim Start erstellt und beim Beenden geschlossen wird. I2P unterscheidet sich von Tor, wo Circuits schnell erstellt und verworfen werden können. Denken Sie sorgfältig nach und konsultieren Sie I2P-Entwickler, bevor Sie Ihre Anwendung so entwerfen, dass sie mehr als ein oder zwei gleichzeitige Sessions verwendet oder diese schnell erstellt und verwirft. Die meisten Bedrohungsmodelle erfordern keine eindeutige Session für jede Verbindung.

Stellen Sie außerdem sicher, dass Ihre Anwendungseinstellungen (und die Anleitung für Benutzer bezüglich router-Einstellungen oder router-Standardwerte, falls Sie einen router mitliefern) dazu führen, dass Ihre Benutzer mehr Ressourcen zum Netzwerk beitragen, als sie verbrauchen. I2P ist ein Peer-to-Peer-Netzwerk, und das Netzwerk kann nicht überleben, wenn eine beliebte Anwendung das Netzwerk in eine dauerhafte Überlastung treibt.

### Kompatibilität und Tests

Die Java I2P und i2pd router Implementierungen sind unabhängig und haben kleinere Unterschiede im Verhalten, bei der Funktionsunterstützung und den Standardeinstellungen. Bitte testen Sie Ihre Anwendung mit der neuesten Version beider router.

i2pd SAM ist standardmäßig aktiviert; Java I2P SAM ist es nicht. Geben Sie Ihren Benutzern Anweisungen, wie SAM in Java I2P aktiviert wird (über /configclients in der router-Konsole), und/oder stellen Sie eine aussagekräftige Fehlermeldung für den Benutzer bereit, falls die anfängliche Verbindung fehlschlägt, z.B. "Stellen Sie sicher, dass I2P läuft und die SAM-Schnittstelle aktiviert ist".

Die Java I2P und i2pd router haben unterschiedliche Standardwerte für die Anzahl der tunnel. Der Java-Standard ist 2 und der i2pd-Standard ist 5. Für die meisten Anwendungen mit geringer bis mittlerer Bandbreite und geringen bis mittleren Verbindungszahlen sind 2 oder 3 ausreichend. Bitte geben Sie die tunnel-Anzahl in der SESSION CREATE-Nachricht an, um eine konsistente Leistung mit den Java I2P und i2pd routern zu erhalten. Siehe unten.

Für weitere Anleitungen an Entwickler, wie Sie sicherstellen können, dass Ihre Anwendung nur die benötigten Ressourcen verwendet, siehe bitte [unseren Leitfaden zum Bündeln von I2P mit Ihrer Anwendung](/docs/applications/embedding).

### Signatur- und Verschlüsselungstypen

I2P unterstützt mehrere Signatur- und Verschlüsselungstypen. Aus Gründen der Rückwärtskompatibilität verwendet SAM standardmäßig alte und ineffiziente Typen, daher sollten alle Clients neuere Typen angeben.

Der Signaturtyp wird in den Befehlen DEST GENERATE und SESSION CREATE (für transient) angegeben. Alle Clients sollten `SIGNATURE_TYPE=7` (Ed25519) setzen.

Der Verschlüsselungstyp wird im SESSION CREATE-Befehl angegeben. Mehrere Verschlüsselungstypen sind erlaubt. Clients sollten entweder `i2cp.leaseSetEncType=4` (nur für ECIES-X25519) oder `i2cp.leaseSetEncType=4,0` (für ECIES-X25519 und ElGamal, falls Kompatibilität erforderlich ist) setzen.

## Änderungen in Version 3

### Version 3.0 Änderungen

Version 3.0 wurde in I2P Release 0.7.3 eingeführt. SAM v2 bot eine Möglichkeit, mehrere Sockets auf demselben I2P destination *parallel* zu verwalten, d.h. der Client musste nicht warten, bis Daten erfolgreich auf einem Socket gesendet wurden, bevor er Daten auf einem anderen Socket senden konnte. Aber alle Daten liefen über denselben Client-zu-SAM Socket, was für den Client ziemlich kompliziert zu verwalten war.

SAMv3 verwaltet Sockets auf eine andere Art: Jeder *I2P Socket* entspricht einem eindeutigen Client-zu-SAM Socket, was viel einfacher zu handhaben ist. Dies ist ähnlich zu [BOB](/docs/api/bob).

SAMv3 bietet auch einen UDP-Port zum Senden von Datagrammen über I2P und kann I2P-Datagramme an den Datagramm-Server des Clients weiterleiten.

### Version 3.1 Änderungen

Version 3.1 wurde in Java I2P Release 0.9.14 (Juli 2014) eingeführt. SAMv3.1 ist die empfohlene Mindest-SAM-Implementierung aufgrund ihrer Unterstützung für bessere Signaturtypen als SAMv3.0. i2pd unterstützt ebenfalls die meisten 3.1-Funktionen.

- DEST GENERATE und SESSION CREATE unterstützen jetzt einen SIGNATURE_TYPE Parameter.
- Die MIN und MAX Parameter in HELLO VERSION sind jetzt optional.
- Die MIN und MAX Parameter in HELLO VERSION unterstützen jetzt einstellige Versionen wie "3".
- RAW SEND wird jetzt auf dem Bridge-Socket unterstützt.

### Version 3.2 Änderungen

Version 3.2 wurde in Java I2P Release 0.9.24 (Januar 2016) eingeführt. Beachten Sie, dass i2pd derzeit die meisten 3.2-Features nicht unterstützt.

#### I2CP Port- und Protokollunterstützung

- SESSION CREATE Optionen FROM_PORT und TO_PORT
- SESSION CREATE STYLE=RAW Option PROTOCOL
- STREAM CONNECT, DATAGRAM SEND und RAW SEND Optionen FROM_PORT und TO_PORT
- RAW SEND Option PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED und weitergeleitete oder empfangene Streams und beantwortbare Datagramme, enthalten FROM_PORT und TO_PORT
- RAW Session Option HEADER=true bewirkt, dass die weitergeleiteten Raw-Datagramme mit einer Zeile vorangestellt werden, die PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn enthält
- Die erste Zeile von Datagrammen, die über Port 7655 gesendet werden, kann jetzt mit einer beliebigen 3.x Version beginnen
- Die erste Zeile von Datagrammen, die über Port 7655 gesendet werden, kann beliebige der Optionen FROM_PORT, TO_PORT, PROTOCOL enthalten
- RAW RECEIVED enthält PROTOCOL=nnn

#### SSL und Authentifizierung

- USER/PASSWORD in den HELLO-Parametern für die Autorisierung. Siehe [unten](#authorization).
- Optionale Autorisierungskonfiguration mit dem AUTH-Befehl. Siehe [unten](#authorization-configuration-sam-32-or-higher-optional-feature).
- Optionale SSL/TLS-Unterstützung auf dem Kontroll-Socket. Siehe [unten](#ssl).
- STREAM FORWARD-Option SSL=true

#### Multithreading

- Gleichzeitige ausstehende STREAM ACCEPTs sind auf derselben Session-ID erlaubt.

#### Kommandozeilen-Analyse und Keepalive

- Optionale Befehle QUIT, STOP und EXIT zum Schließen der Sitzung und des Sockets. Siehe [unten](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- Befehlsanalyse behandelt UTF-8 ordnungsgemäß
- Befehlsanalyse behandelt Leerzeichen in Anführungszeichen zuverlässig
- Ein Backslash '\\' kann Anführungszeichen in der Befehlszeile maskieren
- Empfohlen wird, dass der Server Befehle in Großbuchstaben umwandelt, um Tests über telnet zu erleichtern.
- Leere Optionswerte wie PROTOCOL oder PROTOCOL= können erlaubt sein, implementierungsabhängig.
- PING/PONG für Keepalive. Siehe unten.
- Server können Timeouts für HELLO oder nachfolgende Befehle implementieren, implementierungsabhängig.

### Änderungen in Version 3.3

Version 3.3 wurde in Java I2P Release 0.9.25 (März 2016) eingeführt. Beachten Sie, dass i2pd derzeit die meisten 3.3-Funktionen nicht unterstützt.

- Dieselbe Sitzung kann gleichzeitig für Streams, Datagramme und Raw-Daten verwendet werden. Eingehende Pakete und Streams werden basierend auf dem I2P-Protokoll und dem Ziel-Port weitergeleitet. Siehe [den PRIMARY-Abschnitt unten](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND und RAW SEND unterstützen jetzt die Optionen SEND_TAGS, TAG_THRESHOLD, EXPIRES und SEND_LEASESET. Siehe [den Abschnitt zum Versenden von Datagrammen unten](#sending-repliable-or-raw-datagrams).

## Version 3 Protokoll

### Simple Anonymous Messaging (SAM) Version 3.3 Spezifikation Übersicht

Die Client-Anwendung kommuniziert mit der SAM-Brücke, die sich um alle I2P-Funktionalitäten kümmert (unter Verwendung der [streaming library](/docs/api/streaming) für virtuelle Streams oder [I2CP](/docs/protocol/i2cp) direkt für Datagramme).

Standardmäßig ist die Kommunikation zwischen Client und SAM bridge unverschlüsselt und nicht authentifiziert. Die SAM bridge kann SSL/TLS-Verbindungen unterstützen; Konfigurations- und Implementierungsdetails liegen außerhalb des Umfangs dieser Spezifikation. Ab SAM 3.2 werden optionale Authentifizierungs-Benutzer/Passwort-Parameter im initialen Handshake unterstützt und können von der bridge erforderlich sein.

I2P-Kommunikation kann verschiedene Formen annehmen:

- [Virtuelle Streams](/docs/api/streaming)
- [Beantwortbare und authentifizierte Datagramme](/docs/specs/datagrams#repliable) (Nachrichten mit einem FROM-Feld)
- [Anonyme Datagramme](/docs/specs/datagrams#raw) (rohe anonyme Nachrichten)
- [Datagram2](/docs/specs/datagrams#datagram2) (ein neues beantwortbares und authentifiziertes Format)
- [Datagram3](/docs/specs/datagrams#datagram3) (ein neues beantwortbares aber nicht authentifiziertes Format)

I2P-Kommunikation wird durch I2P-Sitzungen unterstützt, und jede I2P-Sitzung ist an eine Adresse gebunden (genannt destination). Eine I2P-Sitzung ist mit einem der drei oben genannten Typen verknüpft und kann keine Kommunikation eines anderen Typs übertragen, es sei denn, sie verwendet [PRIMARY-Sitzungen](#sam-primary-sessions-v33-and-higher).

### Kodierung und Escaping

Alle diese SAM-Nachrichten werden in einer einzigen Zeile gesendet und mit dem Zeilenendezeichen (\\n) abgeschlossen. Vor SAM 3.2 wurde nur 7-Bit ASCII unterstützt. Ab SAM 3.2 muss die Kodierung UTF-8 sein. Alle UTF8-kodierten Schlüssel oder Werte sollten funktionieren.

Die in dieser Spezifikation unten gezeigte Formatierung dient lediglich der Lesbarkeit, und während die ersten beiden Wörter in jeder Nachricht in ihrer spezifischen Reihenfolge bleiben müssen, kann sich die Reihenfolge der Schlüssel=Wert-Paare ändern (z.B. sind "ONE TWO A=B C=D" oder "ONE TWO C=D A=B" beide vollkommen gültige Konstruktionen). Zusätzlich ist das Protokoll groß-/kleinschreibungsabhängig. Im Folgenden werden Nachrichtenbeispiele mit "->" für vom Client an die SAM bridge gesendete Nachrichten und mit "<-" für von der SAM bridge an den Client gesendete Nachrichten vorangestellt.

Die grundlegende Befehls- oder Antwortzeile hat eine der folgenden Formen:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND ohne einen SUBCOMMAND wird nur für einige neue Befehle in SAM 3.2 unterstützt.

Schlüssel=Wert-Paare müssen durch ein einzelnes Leerzeichen getrennt werden. (Ab SAMv3.2 sind mehrere Leerzeichen erlaubt) Werte müssen in Anführungszeichen gesetzt werden, wenn sie Leerzeichen enthalten, z.B. key="long value text". (Vor SAMv3.2 funktionierte dies in einigen Implementierungen nicht zuverlässig)

Vor SAM 3.2 gab es keinen Escape-Mechanismus. Ab SAM 3.2 können doppelte Anführungszeichen mit einem Backslash '\\' maskiert werden und ein Backslash kann als zwei Backslashes '\\\\' dargestellt werden.

### Leere Werte

Ab SAM 3.2 können leere Optionswerte wie KEY, KEY= oder KEY="" erlaubt sein, abhängig von der Implementierung.

### Groß-/Kleinschreibung

Das Protokoll ist, wie spezifiziert, groß- und kleinschreibungsempfindlich. Es wird empfohlen, aber nicht vorausgesetzt, dass der Server Befehle auf Großbuchstaben abbildet, um das Testen über telnet zu erleichtern. Dies würde zum Beispiel ermöglichen, dass "hello version" funktioniert. Dies ist implementierungsabhängig. Bilden Sie Schlüssel oder Werte nicht auf Großbuchstaben ab, da dies [I2CP](/docs/protocol/i2cp)-Optionen beschädigen würde.

### SAM-Verbindungshandshake

Keine SAM-Kommunikation kann stattfinden, bis sich Client und Bridge auf eine Protokollversion geeinigt haben, was durch das Senden eines HELLO vom Client und eines HELLO REPLY von der Bridge erfolgt:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
und

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
Ab Version 3.1 (I2P 0.9.14) sind die Parameter MIN und MAX optional. SAM wird immer die höchstmögliche Version zurückgeben, die den MIN- und MAX-Beschränkungen entspricht, oder die aktuelle Serverversion, wenn keine Beschränkungen angegeben sind.

Wenn die SAM bridge keine geeignete Version finden kann, antwortet sie mit:

```
<- HELLO REPLY RESULT=NOVERSION
```
Wenn ein Fehler auftritt, wie z.B. ein fehlerhaftes Anfrage-Format, antwortet es mit:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

Der Control-Socket des Servers kann optional SSL/TLS-Unterstützung anbieten, wie auf dem Server und Client konfiguriert. Implementierungen können auch andere Transportschichten anbieten; dies liegt außerhalb des Umfangs der Protokolldefinition.

#### Autorisierung

Für die Autorisierung fügt der Client USER="xxx" PASSWORD="yyy" zu den HELLO-Parametern hinzu. Anführungszeichen für Benutzername und Passwort werden empfohlen, sind aber nicht erforderlich. Ein Anführungszeichen innerhalb eines Benutzernamens oder Passworts muss mit einem Backslash escaped werden. Bei einem Fehler antwortet der Server mit einem I2P_ERROR und einer Nachricht. Es wird empfohlen, SSL auf allen SAM-Servern zu aktivieren, bei denen eine Autorisierung erforderlich ist.

#### Zeitüberschreitungen

Server können Timeouts für den HELLO oder nachfolgende Befehle implementieren, je nach Implementierung. Clients sollten den HELLO und den nächsten Befehl umgehend nach dem Verbinden senden.

Wenn ein Timeout auftritt, bevor das HELLO empfangen wird, antwortet die Bridge mit:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
und trennt dann die Verbindung.

Wenn ein Timeout auftritt, nachdem das HELLO empfangen wurde, aber bevor der nächste Befehl eintrifft, antwortet die Bridge mit:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
und trennt dann die Verbindung.

### I2CP Ports und Protokoll

Ab SAM 3.2 können die [I2CP](/docs/protocol/i2cp)-Ports und das Protokoll vom SAM-Client-Sender spezifiziert werden, um an [I2CP](/docs/protocol/i2cp) weitergeleitet zu werden, und die SAM-Bridge wird die empfangenen [I2CP](/docs/protocol/i2cp)-Port- und Protokollinformationen an den SAM-Client weiterleiten.

Für FROM_PORT und TO_PORT ist der gültige Bereich 0-65535, und der Standardwert ist 0.

Für PROTOCOL, das nur für RAW angegeben werden kann, ist der gültige Bereich 0-255, und der Standardwert ist 18.

Für SESSION-Befehle sind die angegebenen Ports und das Protokoll die Standardwerte für diese Sitzung. Für einzelne Streams oder Datagramme überschreiben die angegebenen Ports und das Protokoll die Sitzungsstandards. Für empfangene Streams oder Datagramme sind die angegebenen Ports und das Protokoll wie von [I2CP](/docs/protocol/i2cp) empfangen.

#### Wichtige Unterschiede zum Standard-IP

I2CP-Ports sind für I2P-Sockets und Datagramme. Sie haben nichts mit Ihren lokalen Sockets zu tun, die sich mit SAM verbinden.

- Port 0 ist gültig und hat eine besondere Bedeutung.
- Ports 1-1023 sind nicht speziell oder privilegiert.
- Server lauschen standardmäßig auf Port 0, was "alle Ports" bedeutet.
- Clients senden standardmäßig an Port 0, was "beliebiger Port" bedeutet.
- Clients senden standardmäßig von Port 0, was "nicht spezifiziert" bedeutet.
- Server können einen Dienst haben, der auf Port 0 lauscht, und andere Dienste, die auf höheren Ports lauschen. In diesem Fall ist der Port-0-Dienst der Standard und wird verbunden, wenn der eingehende Socket- oder Datagramm-Port nicht mit einem anderen Dienst übereinstimmt.
- Die meisten I2P-Ziele haben nur einen Dienst, der auf ihnen läuft, daher können Sie die Standardeinstellungen verwenden und die I2CP-Port-Konfiguration ignorieren.
- SAM 3.2 oder 3.3 ist erforderlich, um I2CP-Ports zu spezifizieren.
- Wenn Sie keine I2CP-Ports benötigen, brauchen Sie nicht SAM 3.2 oder 3.3; 3.1 ist ausreichend.
- Protokoll 0 ist gültig und bedeutet "beliebiges Protokoll". Dies wird nicht empfohlen und wird wahrscheinlich nicht funktionieren.
- I2P-Sockets werden durch eine interne Verbindungs-ID verfolgt. Daher gibt es keine Anforderung, dass das 5-Tupel aus Ziel:Port:Ziel:Port:Protokoll eindeutig sein muss. Zum Beispiel kann es mehrere Sockets mit denselben Ports zwischen zwei Zielen geben. Clients müssen keinen "freien Port" für eine ausgehende Verbindung wählen.

Wenn Sie eine SAM 3.3-Anwendung mit mehreren Subsessions entwerfen, überlegen Sie sorgfältig, wie Sie Ports und Protokolle effektiv nutzen können. Weitere Informationen finden Sie in der [I2CP](/docs/protocol/i2cp)-Spezifikation.

### SAM Sessions

Eine SAM-Sitzung wird erstellt, indem ein Client einen Socket zur SAM-Bridge öffnet, einen Handshake durchführt und eine SESSION CREATE-Nachricht sendet. Die Sitzung wird beendet, wenn der Socket getrennt wird.

Jede registrierte I2P Destination ist eindeutig mit einer Sitzungs-ID (oder einem Spitznamen) verknüpft. Sitzungs-IDs, einschließlich Untersitzungs-IDs für PRIMARY-Sitzungen, müssen auf dem SAM-Server global eindeutig sein. Um mögliche ID-Kollisionen mit anderen Clients zu verhindern, ist es bewährte Praxis, dass der Client IDs zufällig generiert.

Jede Sitzung ist eindeutig verknüpft mit:

- der Socket, von dem aus der Client die Sitzung erstellt
- seine ID (oder Spitzname)

#### Session-Erstellungsanfrage

Die Session-Erstellungsnachricht kann nur eine dieser Formen verwenden (Nachrichten, die über andere Formen empfangen werden, werden mit einer Fehlermeldung beantwortet):

```
->  SESSION CREATE
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, for DESTINATION=TRANSIENT only, default DSA_SHA1
          [PORT=$port]                         # Required for DATAGRAM* RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [HEADER={true,false}]                # SAM 3.2 or higher only, for STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
DESTINATION gibt an, welche Destination zum Senden und Empfangen von Nachrichten/Streams verwendet werden soll. Der $privkey ist die Base-64-Kodierung der Verkettung der [Destination](/docs/specs/common-structures#type_Destination) gefolgt vom [Private Key](/docs/specs/common-structures#type_PrivateKey) gefolgt vom [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), optional gefolgt von der [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), was 663 oder mehr Bytes im Binärformat und 884 oder mehr Bytes in Base 64 entspricht, abhängig vom Signaturtyp. Das Binärformat ist in Private Key File spezifiziert. Siehe zusätzliche Hinweise zum [Private Key](/docs/specs/common-structures#type_PrivateKey) im Abschnitt Destination Key Generation unten.

Wenn der private Signaturschlüssel nur aus Nullen besteht, folgt der Abschnitt [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature). Offline-Signaturen werden nur für STREAM- und RAW-Sessions unterstützt. Offline-Signaturen dürfen nicht mit DESTINATION=TRANSIENT erstellt werden. Das Format des Offline-Signatur-Abschnitts ist:

1. Ablaufzeitstempel (4 Bytes, Big Endian, Sekunden seit Epoch, läuft 2106 über)
2. Sig-Typ des temporären Signing Public Key (2 Bytes, Big Endian)
3. Temporärer Signing Public Key (Länge wie durch temporären Sig-Typ spezifiziert)
4. Signatur der obigen drei Felder durch Offline-Schlüssel (Länge wie durch Ziel-Sig-Typ spezifiziert)
5. Temporärer Signing Private Key (Länge wie durch temporären Sig-Typ spezifiziert)

Wenn das Ziel als TRANSIENT angegeben wird, erstellt die SAM bridge ein neues Ziel. Ab Version 3.1 (I2P 0.9.14) wird, falls das Ziel TRANSIENT ist, ein optionaler Parameter SIGNATURE_TYPE unterstützt. Der SIGNATURE_TYPE-Wert kann jeder Name (z.B. ECDSA_SHA256_P256, Groß-/Kleinschreibung wird ignoriert) oder jede Nummer (z.B. 1) sein, die von [Key Certificates](/docs/specs/common-structures#type_Certificate) unterstützt wird. Der Standard ist DSA_SHA1, was NICHT das ist, was Sie wollen. Für die meisten Anwendungen geben Sie bitte SIGNATURE_TYPE=7 an.

$nickname ist die Wahl des Clients. Leerzeichen sind nicht erlaubt.

Zusätzliche Optionen werden an die I2P-Session-Konfiguration weitergegeben, falls sie nicht von der SAM bridge interpretiert werden (z.B. outbound.length=0).

Die Java I2P und i2pd router haben unterschiedliche Standardwerte für die Anzahl der Tunnel. Der Java-Standard ist 2 und der i2pd-Standard ist 5. Für die meisten Anwendungen mit geringer bis mittlerer Bandbreite und geringen bis mittleren Verbindungszahlen sind 2 oder 3 ausreichend. Bitte geben Sie die Tunnel-Anzahl in der SESSION CREATE-Nachricht an, um eine konsistente Leistung mit den Java I2P und i2pd routern zu erhalten, z.B. mit den Optionen inbound.quantity=3 outbound.quantity=3. Diese und andere Optionen [sind in den unten stehenden Links dokumentiert](#tunnel-i2cp-and-streaming-options).

Die SAM bridge selbst sollte bereits konfiguriert sein, mit welchem router sie über I2P kommunizieren soll (obwohl es bei Bedarf möglicherweise eine Möglichkeit gibt, dies zu überschreiben, z.B. i2cp.tcp.host=localhost und i2cp.tcp.port=7654).

#### Session-Erstellungsantwort

Nach dem Empfang der Session-Erstellungsnachricht wird die SAM-Bridge mit einer Session-Statusnachricht antworten, wie folgt:

Wenn die Erstellung erfolgreich war:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
Der $privkey ist die Base64-Kodierung der Verkettung der [Destination](/docs/specs/common-structures#type_Destination), gefolgt vom [Private Key](/docs/specs/common-structures#type_PrivateKey), gefolgt vom [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), optional gefolgt von der [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), was 663 oder mehr Bytes in binärer Form und 884 oder mehr Bytes in Base64 entspricht, abhängig vom Signaturtyp. Das Binärformat ist in der Private Key File spezifiziert.

Wenn das SESSION CREATE einen signing private key aus lauter Nullen und einen [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) Abschnitt enthielt, wird die SESSION STATUS Antwort dieselben Daten im selben Format enthalten. Siehe den SESSION CREATE Abschnitt oben für Details.

Wenn der Nickname bereits mit einer Session verknüpft ist:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Wenn das Ziel bereits verwendet wird:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Wenn das Ziel kein gültiger privater destination key ist:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Falls ein anderer Fehler aufgetreten ist:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Wenn es nicht OK ist, sollte die MESSAGE menschenlesbare Informationen darüber enthalten, warum die Sitzung nicht erstellt werden konnte.

Beachten Sie, dass der router Tunnel erstellt, bevor er mit SESSION STATUS antwortet. Dies kann mehrere Sekunden dauern, oder beim router-Start oder bei starker Netzwerküberlastung eine Minute oder länger. Bei Erfolglosigkeit wird der router nicht für mehrere Minuten mit einer Fehlermeldung antworten. Setzen Sie kein kurzes Timeout beim Warten auf die Antwort. Verlassen Sie die Sitzung nicht während des Tunnel-Aufbaus und versuchen Sie es erneut.

SAM-Sitzungen leben und sterben mit dem Socket, mit dem sie verbunden sind. Wenn der Socket geschlossen wird, stirbt die Sitzung und alle Kommunikationen, die diese Sitzung verwenden, sterben zur gleichen Zeit. Und umgekehrt: Wenn die Sitzung aus irgendeinem Grund stirbt, schließt die SAM-Brücke den Socket.

### SAM Virtual Streams

Virtuelle Streams werden garantiert zuverlässig und in der richtigen Reihenfolge gesendet, mit Fehler- und Erfolgsbenachrichtigung sobald diese verfügbar sind.

Streams sind bidirektionale Kommunikations-Sockets zwischen zwei I2P destinations, aber ihre Öffnung muss von einer von ihnen angefordert werden. Im Folgenden werden CONNECT-Befehle vom SAM-Client für solche Anfragen verwendet. FORWARD / ACCEPT-Befehle werden vom SAM-Client verwendet, wenn er auf Anfragen von anderen I2P destinations lauschen möchte.

### SAM Virtual Streams: CONNECT

Ein Client fordert eine Verbindung an durch:

- Öffnen eines neuen Sockets mit der SAM bridge
- Übertragen desselben HELLO-Handshakes wie oben
- Senden des STREAM CONNECT-Befehls

#### Verbindungsanfrage

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Dies stellt eine neue virtuelle Verbindung von der lokalen Sitzung mit der ID $nickname zu dem angegebenen Peer her.

Das Ziel ist $destination, was die base 64-Kodierung der [Destination](/docs/specs/common-structures#type_Destination) ist, die 516 oder mehr base 64-Zeichen (387 oder mehr Bytes im Binärformat) umfasst, abhängig vom Signaturtyp.

**HINWEIS:** Seit etwa 2014 (SAM v3.1) hat Java I2P auch Hostnamen und b32-Adressen für das $destination unterstützt, aber dies war zuvor undokumentiert. Hostnamen und b32-Adressen werden nun offiziell von Java I2P ab Release 0.9.48 unterstützt. Der i2pd router unterstützt Hostnamen und b32-Adressen ab Release 2.38.0 (0.9.50). Für beide router umfasst die "b32"-Unterstützung auch erweiterte "b33"-Adressen für blinded destinations.

#### Verbindungsantwort

Wenn SILENT=true übergeben wird, sendet die SAM bridge keine weiteren Nachrichten über den Socket. Falls die Verbindung fehlschlägt, wird der Socket geschlossen. Falls die Verbindung erfolgreich ist, werden alle verbleibenden Daten, die durch den aktuellen Socket fließen, von und zu dem verbundenen I2P destination peer weitergeleitet.

Wenn SILENT=false, was der Standardwert ist, sendet die SAM bridge eine letzte Nachricht an ihren Client, bevor sie den Socket weiterleitet oder schließt:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Der RESULT-Wert kann einer der folgenden sein:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
Wenn das RESULT OK ist, werden alle verbleibenden Daten, die durch den aktuellen Socket übertragen werden, von und zu dem verbundenen I2P-Ziel-Peer weitergeleitet. Wenn die Verbindung nicht möglich war (Timeout, etc.), enthält RESULT den entsprechenden Fehlerwert (begleitet von einer optionalen menschenlesbaren MESSAGE), und die SAM bridge schließt den Socket.

Das interne Timeout für router Stream-Verbindungen beträgt etwa eine Minute und ist implementierungsabhängig. Setzen Sie kein kürzeres Timeout beim Warten auf die Antwort.

### SAM Virtual Streams: ACCEPT

Ein Client wartet auf eine eingehende Verbindungsanfrage durch:

- Öffnen eines neuen Sockets mit der SAM-Brücke
- Übergeben des gleichen HELLO-Handshakes wie oben
- Senden des STREAM ACCEPT-Befehls

#### Anfrage annehmen

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Dies lässt die Sitzung ${nickname} auf eine eingehende Verbindungsanfrage aus dem I2P-Netzwerk lauschen. ACCEPT ist nicht erlaubt, solange ein aktiver FORWARD auf der Sitzung vorhanden ist.

Ab SAM 3.2 sind mehrere gleichzeitige ausstehende STREAM ACCEPTs auf derselben Session-ID erlaubt (sogar mit demselben Port). Vor 3.2 schlugen gleichzeitige Accepts mit ALREADY_ACCEPTING fehl. Hinweis: Java I2P unterstützt auch gleichzeitige ACCEPTs auf SAM 3.1, ab Release 0.9.24 (2016-01). i2pd unterstützt auch gleichzeitige ACCEPTs auf SAM 3.1, ab Release 2.50.0 (2023-12).

#### Antwort akzeptieren

Wenn SILENT=true übergeben wird, gibt die SAM bridge keine weiteren Nachrichten über den Socket aus. Wenn das Accept fehlschlägt, wird der Socket geschlossen. Wenn das Accept erfolgreich ist, werden alle verbleibenden Daten, die durch den aktuellen Socket fließen, von und zu dem verbundenen I2P destination Peer weitergeleitet. Für Zuverlässigkeit und um die destination für eingehende Verbindungen zu erhalten, wird SILENT=false empfohlen.

Falls SILENT=false, was der Standardwert ist, antwortet die SAM bridge mit:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Der RESULT-Wert kann einer der folgenden sein:

```
OK
I2P_ERROR
INVALID_ID
```
Wenn das Ergebnis nicht OK ist, wird der Socket sofort von der SAM bridge geschlossen. Wenn das Ergebnis OK ist, beginnt die SAM bridge auf eine eingehende Verbindungsanfrage von einem anderen I2P-Peer zu warten. Wenn eine Anfrage eintrifft, akzeptiert die SAM bridge diese und:

Wenn SILENT=true übergeben wurde, sendet die SAM bridge keine weiteren Nachrichten über den Client-Socket. Alle verbleibenden Daten, die durch den aktuellen Socket übertragen werden, werden vom und zum verbundenen I2P destination peer weitergeleitet.

Wenn SILENT=false übergeben wurde, was der Standardwert ist, sendet die SAM bridge dem Client eine ASCII-Zeile, die den base64 public destination key des anfragenden Peers enthält, sowie zusätzliche Informationen nur für SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Nach dieser mit '\\n' terminierten Zeile werden alle verbleibenden Daten, die durch den aktuellen Socket übertragen werden, von und zu dem verbundenen I2P destination Peer weitergeleitet, bis einer der Peers den Socket schließt.

#### Fehler nach OK

In seltenen Fällen kann die SAM bridge einen Fehler antreffen, nachdem RESULT=OK gesendet wurde, aber bevor eine Verbindung eingeht und die $destination-Zeile an den Client gesendet wird. Diese Fehler können router shutdown, router restart und session close umfassen. In diesen Fällen kann die SAM bridge, wenn SILENT=false ist, aber muss nicht (implementierungsabhängig), die folgende Zeile senden:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
bevor der Socket sofort geschlossen wird. Diese Zeile ist natürlich nicht als gültiges Base 64 Ziel dekodierbar.

### SAM Virtual Streams: FORWARD

Ein Client kann einen regulären Socket-Server verwenden und auf Verbindungsanfragen aus I2P warten. Dafür muss der Client:

- öffnen Sie einen neuen Socket mit der SAM bridge
- übergeben Sie denselben HELLO-Handshake wie oben
- senden Sie den forward-Befehl

#### Weiterleitungsanfrage

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Dies lässt die Sitzung ${nickname} auf eingehende Verbindungsanfragen aus dem I2P-Netzwerk lauschen. FORWARD ist nicht erlaubt, solange ein ausstehender ACCEPT auf der Sitzung vorhanden ist.

#### Weitergeleitete Antwort

SILENT ist standardmäßig false. Ob SILENT true oder false ist, die SAM bridge antwortet immer mit einer STREAM STATUS Nachricht. Beachten Sie, dass dies ein anderes Verhalten als bei STREAM ACCEPT und STREAM CONNECT ist, wenn SILENT=true. Die STREAM STATUS Nachricht ist:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Der RESULT-Wert kann einer der folgenden sein:

```
OK
I2P_ERROR
INVALID_ID
```
$host ist der Hostname oder die IP-Adresse des Socket-Servers, an den SAM Verbindungsanfragen weiterleitet. Wenn nicht angegeben, verwendet SAM die IP des Sockets, der den Forward-Befehl ausgegeben hat.

$port ist die Portnummer des Socket-Servers, an den SAM Verbindungsanfragen weiterleitet. Sie ist obligatorisch.

Wenn eine Verbindungsanfrage von I2P ankommt, öffnet die SAM bridge eine Socket-Verbindung zu $host:$port. Wenn diese in weniger als 3 Sekunden akzeptiert wird, akzeptiert SAM die Verbindung von I2P und dann:

Wenn SILENT=true übergeben wurde, werden alle Daten, die durch den erhaltenen aktuellen Socket laufen, von und zu dem verbundenen I2P-Ziel-Peer weitergeleitet.

Wenn SILENT=false übergeben wurde, was der Standardwert ist, sendet die SAM-Brücke über den erhaltenen Socket eine ASCII-Zeile, die den base64 öffentlichen Zielschlüssel des anfragenden Peers enthält, sowie zusätzliche Informationen nur für SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Nach dieser mit '\\n' beendeten Zeile werden alle verbleibenden Daten, die durch den Socket übertragen werden, von und zu dem verbundenen I2P destination Peer weitergeleitet, bis eine der Seiten den Socket schließt.

Ab SAMv3.2 wird, wenn SSL=true angegeben ist, der Weiterleitungs-Socket über SSL/TLS übertragen.

Der I2P router wird aufhören, auf eingehende Verbindungsanfragen zu hören, sobald der "forwarding"-Socket geschlossen wird.

### SAM Datagrams

SAMv3 bietet Mechanismen zum Senden und Empfangen von Datagrammen über lokale Datagram-Sockets. Einige SAMv3-Implementierungen unterstützen auch die ältere v1/v2-Methode zum Senden/Empfangen von Datagrammen über den SAM-Bridge-Socket. Beide werden unten dokumentiert.

I2P unterstützt vier Arten von Datagrammen:

- Beantwortbare und authentifizierte Datagramme haben das Ziel des Absenders als Präfix und enthalten die Signatur des Absenders, sodass der Empfänger überprüfen kann, dass das Ziel des Absenders nicht gefälscht wurde, und auf das Datagramm antworten kann. Das neue Datagram2-Format ist ebenfalls beantwortbar und authentifiziert.
- Das neue Datagram3-Format ist beantwortbar, aber nicht authentifiziert. Die Absenderinformationen sind ungeprüft.
- Rohe Datagramme enthalten weder das Ziel des Absenders noch eine Signatur.

Standard-I2CP-Ports sind sowohl für beantwortbare als auch für rohe Datagramme definiert. Der I2CP-Port kann für rohe Datagramme geändert werden.

Ein häufiges Protokoll-Designmuster besteht darin, dass beantwortbare Datagramme an Server gesendet werden, die eine Kennung enthalten, und der Server mit einem rohen Datagramm antwortet, das diese Kennung enthält, sodass die Antwort mit der Anfrage korreliert werden kann. Dieses Designmuster eliminiert den erheblichen Overhead von beantwortbaren Datagrammen in Antworten. Alle Entscheidungen bezüglich I2CP-Protokollen und Ports sind anwendungsspezifisch, und Designer sollten diese Aspekte berücksichtigen.

Siehe auch die wichtigen Hinweise zur Datagram-MTU im Abschnitt unten.

#### Senden von beantwortbaren oder rohen Datagrammen

Obwohl I2P von Natur aus keine FROM-Adresse enthält, wird zur Benutzerfreundlichkeit eine zusätzliche Ebene als repliable datagrams bereitgestellt - ungeordnete und unzuverlässige Nachrichten von bis zu 31744 Bytes, die eine FROM-Adresse enthalten (wodurch bis zu 1KB für Header-Material übrig bleiben). Diese FROM-Adresse wird intern von SAM authentifiziert (unter Verwendung des Signaturschlüssels des Ziels zur Überprüfung der Quelle) und beinhaltet Replay-Schutz.

Die Mindestgröße beträgt 1. Für beste Zustellzuverlässigkeit wird eine maximale Größe von etwa 11 KB empfohlen. Die Zuverlässigkeit ist umgekehrt proportional zur Nachrichtengröße, möglicherweise sogar exponentiell.

Nach dem Aufbau einer SAM-Sitzung mit STYLE=DATAGRAM oder STYLE=RAW kann der Client beantwortbare oder rohe Datagramme über SAMs UDP-Port (standardmäßig 7655) senden.

Die erste Zeile eines Datagramms, das über diesen Port gesendet wird, muss das folgende Format haben. Dies steht alles in einer Zeile (durch Leerzeichen getrennt), wird hier zur besseren Übersicht auf mehrere Zeilen aufgeteilt:

```
3.0                                  # As of SAM 3.2, any "3.x" is allowed. Prior to that, "3.0" is required.
$nickname
$destination
[FROM_PORT=nnn]                      # SAM 3.2 or higher only, default from session options
[TO_PORT=nnn]                        # SAM 3.2 or higher only, default from session options
[PROTOCOL=nnn]                       # SAM 3.2 or higher only, only for RAW sessions, default from session options
[SEND_TAGS=nnn]                      # SAM 3.3 or higher only, number of session tags to send
                                     # Overrides crypto.tagsToSend I2CP session option
                                     # Default is router-dependent (40 for Java router)
[TAG_THRESHOLD=nnn]                  # SAM 3.3 or higher only, low session tag threshold
                                     # Overrides crypto.lowTagThreshold I2CP session option
                                     # Default is router-dependent (30 for Java router)
[EXPIRES=nnn]                        # SAM 3.3 or higher only, expiration from now in seconds
                                     # Overrides clientMessageTimeout I2CP session option (which is in ms)
                                     # Default is router-dependent (60 for Java router)
[SEND_LEASESET={true,false}]         # SAM 3.3 or higher only, whether to send our leaseset
                                     # Overrides shouldBundleReplyInfo I2CP session option
                                     # Default is true
\n
```
- 3.0 ist die Version von SAM. Ab SAM 3.2 ist jede 3.x Version erlaubt.
- $nickname ist die ID der DATAGRAM-Session, die verwendet wird
- Das Ziel ist $destination, was die Base64-Darstellung der [Destination](/docs/specs/common-structures#type_Destination) ist, die 516 oder mehr Base64-Zeichen (387 oder mehr Bytes in binärer Form) umfasst, abhängig vom Signaturtyp. **HINWEIS:** Seit etwa 2014 (SAM v3.1) unterstützt Java I2P auch Hostnamen und b32-Adressen für die $destination, aber dies war zuvor undokumentiert. Hostnamen und b32-Adressen werden jetzt offiziell von Java I2P ab Version 0.9.48 unterstützt. Der i2pd router unterstützt derzeit keine Hostnamen und b32-Adressen; die Unterstützung könnte in einer zukünftigen Version hinzugefügt werden.
- Alle Optionen sind datagramm-spezifische Einstellungen, die die in SESSION CREATE angegebenen Standardwerte überschreiben.
- Version 3.3 Optionen SEND_TAGS, TAG_THRESHOLD, EXPIRES und SEND_LEASESET werden an [I2CP](/docs/protocol/i2cp) weitergegeben, falls unterstützt. Siehe [die I2CP-Spezifikation](/docs/protocol/i2cp#msg_SendMessageExpire) für Details. Die Unterstützung durch den SAM-Server ist optional, er wird diese Optionen ignorieren, falls sie nicht unterstützt werden.
- diese Zeile ist mit '\\n' terminiert.

Die erste Zeile wird von SAM verworfen, bevor die verbleibenden Daten der Nachricht an das angegebene Ziel gesendet werden.

Für eine alternative Methode zum Senden von beantwortbaren und rohen Datagrammen, siehe [DATAGRAM SEND and RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: Empfangen eines Datagramms

Empfangene Datagramme werden von SAM auf den Socket geschrieben, von dem die Datagramm-Sitzung geöffnet wurde, wenn kein Weiterleitungs-PORT im SESSION CREATE-Befehl angegeben ist. Dies ist die v1/v2-kompatible Art, Datagramme zu empfangen.

Wenn ein Datagramm ankommt, liefert die Brücke es über die Nachricht an den Client:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
Die Quelle ist $destination, welches die Base64-Kodierung der [Destination](/docs/specs/common-structures#type_Destination) ist, die 516 oder mehr Base64-Zeichen (387 oder mehr Bytes in binärer Form) umfasst, abhängig vom Signaturtyp.

Die SAM bridge gibt niemals die Authentifizierungs-Header oder andere Felder an den Client weiter, sondern nur die Daten, die der Absender bereitgestellt hat. Dies setzt sich fort, bis die Session geschlossen wird (durch Trennen der Verbindung seitens des Clients).

#### Weiterleitung von Raw- oder Beantwortbaren Datagrammen

Beim Erstellen einer Datagram-Sitzung kann der Client SAM bitten, eingehende Nachrichten an eine bestimmte IP:Port weiterzuleiten. Dies geschieht durch Ausgabe des CREATE-Befehls mit den Optionen PORT und HOST:

```
-> SESSION CREATE
          STYLE={DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          PORT=$port
          [HOST=$host]
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP options
```
Das $privkey ist die Base64-Kodierung der Verkettung von [Destination](/docs/specs/common-structures#type_Destination), gefolgt vom [Private Key](/docs/specs/common-structures#type_PrivateKey), gefolgt vom [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), optional gefolgt von der [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), was 884 oder mehr Base64-Zeichen (663 oder mehr Bytes im Binärformat) entspricht, je nach Signaturtyp. Das Binärformat ist in Private Key File spezifiziert.

Offline-Signaturen werden für RAW-, DATAGRAM2- und DATAGRAM3-Datagramme unterstützt, aber nicht für DATAGRAM. Siehe den Abschnitt SESSION CREATE oben und den Abschnitt DATAGRAM2/3 unten für Details.

$host ist der Hostname oder die IP-Adresse des Datagram-Servers, an den SAM Datagramme weiterleitet. Wenn nicht angegeben, verwendet SAM die IP des Sockets, der den Forward-Befehl ausgegeben hat.

$port ist die Portnummer des Datagramm-Servers, an den SAM Datagramme weiterleiten wird. Wenn $port nicht gesetzt ist, werden Datagramme NICHT weitergeleitet, sondern auf dem Kontroll-Socket empfangen, auf die v1/v2-kompatible Art.

Zusätzliche Optionen werden an die I2P-Sitzungskonfiguration weitergegeben, wenn sie nicht von der SAM-Bridge interpretiert werden (z.B. outbound.length=0). Diese Optionen [sind unten dokumentiert](#tunnel-i2cp-and-streaming-options).

Weitergeleitete beantwortbare Datagramme werden immer mit der base64-Destination vorangestellt, außer bei Datagram3, siehe unten. Wenn ein beantwortbares Datagramm ankommt, sendet die Bridge an den angegebenen Host:Port ein UDP-Paket mit den folgenden Daten:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Weitergeleitete rohe Datagramme werden unverändert an den angegebenen Host:Port ohne Präfix weitergeleitet. Das UDP-Paket enthält die folgenden Daten:

```
$datagram_payload
```
Ab SAM 3.2 wird, wenn HEADER=true bei SESSION CREATE angegeben wird, das weitergeleitete rohe Datagramm mit einer Header-Zeile wie folgt vorangestellt:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Die $destination ist die Base64-Kodierung der [Destination](/docs/specs/common-structures#type_Destination), die 516 oder mehr Base64-Zeichen (387 oder mehr Bytes in binärer Form) umfasst, abhängig vom Signaturtyp.

#### SAM Anonyme (Raw) Datagramme

Um das Maximum aus I2Ps Bandbreite herauszuholen, ermöglicht SAM Clients das Senden und Empfangen anonymer Datagramme, wobei Authentifizierung und Antwortinformationen den Clients selbst überlassen bleiben. Diese Datagramme sind unzuverlässig und ungeordnet und können bis zu 32768 Bytes groß sein.

Die Mindestgröße beträgt 1. Für beste Zustellungszuverlässigkeit wird eine maximale Größe von etwa 11 KB empfohlen.

Nach dem Aufbau einer SAM-Sitzung mit STYLE=RAW kann der Client anonyme Datagramme über die SAM-Brücke genau auf die gleiche Weise senden wie [das Senden beantwortbarer Datagramme](#sending-repliable-or-raw-datagrams).

Beide Wege zum Empfangen von Datagrammen sind auch für anonyme Datagramme verfügbar.

Empfangene Datagramme werden von SAM auf den Socket geschrieben, über den die Datagramm-Session geöffnet wurde, falls kein Weiterleitungs-PORT im SESSION CREATE-Befehl angegeben ist. Dies ist die v1/v2-kompatible Art, Datagramme zu empfangen.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Wenn anonyme Datagramme an einen bestimmten host:port weitergeleitet werden sollen, sendet die Bridge an den angegebenen host:port eine Nachricht, die folgende Daten enthält:

```
$datagram_payload
```
Seit SAM 3.2 wird, wenn HEADER=true in SESSION CREATE angegeben ist, dem weitergeleiteten rohen Datagramm eine Header-Zeile wie folgt vorangestellt:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Für eine alternative Methode zum Senden anonymer Datagramme, siehe [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagram 2/3

Datagram 2/3 sind neue Formate, die Anfang 2025 spezifiziert wurden. Es existieren derzeit keine bekannten Implementierungen. Prüfen Sie die Implementierungsdokumentation für den aktuellen Status. Siehe [die Spezifikation](/docs/specs/datagrams) für weitere Informationen.

Es gibt derzeit keine Pläne, die SAM-Version zu erhöhen, um die Unterstützung für Datagram 2/3 anzuzeigen. Dies könnte problematisch sein, da Implementierungen möglicherweise Datagram 2/3 unterstützen möchten, aber nicht die SAM v3.3-Features. Jede Versionsänderung ist noch offen.

Sowohl Datagram2 als auch Datagram3 sind beantwortbar. Nur Datagram2 ist authentifiziert.

Datagram2 ist aus SAM-Sicht identisch mit beantwortbaren Datagrammen. Beide sind authentifiziert. Nur das I2CP-Format und die Signatur sind unterschiedlich, aber dies ist für SAM-Clients nicht sichtbar. Datagram2 unterstützt auch Offline-Signaturen, sodass es von offline-signierten Zielen verwendet werden kann.

Die Absicht ist, dass Datagram2 die Repliable datagrams für neue Anwendungen ersetzt, die keine Rückwärtskompatibilität benötigen. Datagram2 bietet Replay-Schutz, der bei Repliable datagrams nicht vorhanden ist. Wenn Rückwärtskompatibilität erforderlich ist, kann eine Anwendung sowohl Datagram2 als auch Repliable in derselben Sitzung mit SAMv3 PRIMARY-Sitzungen unterstützen.

Datagram3 ist beantwortbar, aber nicht authentifiziert. Das 'from'-Feld im I2CP-Format ist ein Hash, kein Ziel. Das $destination, wie es vom SAM-Server an den Client gesendet wird, ist ein 44-Byte base64-Hash. Um es in ein vollständiges Ziel für eine Antwort umzuwandeln, dekodieren Sie es base64 zu 32 Bytes binär, kodieren Sie es dann base32 zu 52 Zeichen und hängen Sie ".b32.i2p" für einen NAMING LOOKUP an. Wie üblich sollten Clients ihren eigenen Cache pflegen, um wiederholte NAMING LOOKUPs zu vermeiden.

Anwendungsdesigner sollten äußerste Vorsicht walten lassen und die Sicherheitsimplikationen von nicht authentifizierten Datagrammen berücksichtigen.

#### V3 Datagram MTU Überlegungen

I2P Datagrams können größer sein als die typische Internet-MTU von 1500. Lokal gesendete Datagrams und weitergeleitete antwortfähige Datagrams, die mit dem 516+ Byte base64-Ziel vorangestellt sind, werden wahrscheinlich diese MTU überschreiten. Allerdings sind localhost-MTUs auf Linux-Systemen typischerweise viel größer, beispielsweise 65536. Localhost-MTUs variieren je nach Betriebssystem. I2P Datagrams werden niemals größer als 65536 sein. Die Datagram-Größe hängt vom Anwendungsprotokoll ab.

Wenn der SAM-Client lokal zum SAM-Server ist und das System eine größere MTU unterstützt, werden die Datagramme nicht lokal fragmentiert. Wenn jedoch der SAM-Client remote ist, würden IPv4-Datagramme fragmentiert werden und IPv6-Datagramme würden fehlschlagen (IPv6 unterstützt keine UDP-Fragmentierung).

Client-Bibliothek- und Anwendungsentwickler sollten sich dieser Probleme bewusst sein und Empfehlungen dokumentieren, um Fragmentierung zu vermeiden und Paketverluste zu verhindern, insbesondere bei entfernten SAM Client-Server-Verbindungen.

#### DATAGRAM SEND, RAW SEND (V1/V2 Kompatible Datagram-Behandlung)

In SAMv3 ist der bevorzugte Weg, Datagramme zu senden, über den Datagramm-Socket an Port 7655, wie oben dokumentiert. Allerdings können beantwortbare Datagramme direkt über den SAM Bridge-Socket mit dem DATAGRAM SEND-Befehl gesendet werden, wie in [SAM V1](/docs/api/sam) und [SAM V2](/docs/api/samv2) dokumentiert.

Ab Release 0.9.14 (Version 3.1) können anonyme Datagramme direkt über den SAM-Bridge-Socket mit dem RAW SEND-Befehl gesendet werden, wie in [SAM V1](/docs/api/sam) und [SAM V2](/docs/api/samv2) dokumentiert.

Ab Version 0.9.24 (Version 3.2) können DATAGRAM SEND und RAW SEND die Parameter FROM_PORT=nnnn und/oder TO_PORT=nnnn enthalten, um die Standard-Ports zu überschreiben. Ab Version 0.9.24 (Version 3.2) kann RAW SEND den Parameter PROTOCOL=nnn enthalten, um das Standard-Protokoll zu überschreiben.

Diese Befehle unterstützen den ID-Parameter *nicht*. Die Datagramme werden an die zuletzt erstellte DATAGRAM- oder RAW-Style-Sitzung gesendet, je nach Bedarf. Die Unterstützung für den ID-Parameter könnte in einer zukünftigen Version hinzugefügt werden.

DATAGRAM2- und DATAGRAM3-Formate werden *nicht* in der V1/V2-kompatiblen Art unterstützt.

### SAM PRIMARY Sessions (V3.3 und höher)

*Version 3.3 wurde in I2P-Release 0.9.25 eingeführt.*

*In einer früheren Version dieser Spezifikation wurden PRIMARY-Sessions als MASTER-Sessions bezeichnet. Sowohl in `i2pd` als auch in `I2P+` werden sie immer noch nur als MASTER-Sessions bezeichnet.*

SAM v3.3 fügt Unterstützung für das Ausführen von Streaming-, Datagram- und Raw-Subsessions in derselben primären Session hinzu, sowie für das Ausführen mehrerer Subsessions desselben Typs. Der gesamte Subsession-Verkehr verwendet ein einziges Ziel oder einen Satz von tunnels. Das Routing des Verkehrs von I2P basiert auf den Port- und Protokolloptionen für die Subsessions.

Um multiplexte Untersitzungen zu erstellen, müssen Sie eine primäre Sitzung erstellen und dann Untersitzungen zur primären Sitzung hinzufügen. Jede Untersitzung muss eine eindeutige ID und ein eindeutiges Listen-Protokoll und -Port haben. Untersitzungen können auch von der primären Sitzung entfernt werden.

Mit einer PRIMARY-Session und einer Kombination von Subsessions kann ein SAM-Client mehrere Anwendungen oder eine einzige komplexe Anwendung mit verschiedenen Protokollen auf einem einzigen Satz von tunnels unterstützen. Zum Beispiel könnte ein BitTorrent-Client eine Streaming-Subsession für Peer-to-Peer-Verbindungen einrichten, zusammen mit Datagram- und Raw-Subsessions für die DHT-Kommunikation.

#### Erstellen einer PRIMARY Session

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
Die SAM bridge wird mit Erfolg oder Fehlschlag antworten wie in [der Antwort auf ein Standard SESSION CREATE](#session-creation-response).

Setzen Sie die Optionen PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL oder HEADER nicht für eine primäre Sitzung. Sie dürfen keine Daten über eine PRIMARY Sitzungs-ID oder über den Kontroll-Socket senden. Alle Befehle wie STREAM CONNECT, DATAGRAM SEND usw. müssen die Untersitzungs-ID auf einem separaten Socket verwenden.

Die PRIMARY-Session verbindet sich mit dem router und baut tunnels auf. Wenn die SAM-Bridge antwortet, wurden tunnels erstellt und die Session ist bereit für das Hinzufügen von Subsessions. Alle [I2CP](/docs/protocol/i2cp)-Optionen bezüglich tunnel-Parameter wie Länge, Anzahl und Nickname müssen im SESSION CREATE der Primary-Session angegeben werden.

Alle Utility-Befehle werden in einer primären Sitzung unterstützt.

Wenn die primäre Sitzung geschlossen wird, werden auch alle Untersitzungen geschlossen.

HINWEIS: Vor Version 0.9.47 verwenden Sie STYLE=MASTER. STYLE=PRIMARY wird ab Version 0.9.47 unterstützt. MASTER wird weiterhin für Rückwärtskompatibilität unterstützt.

#### Erstellen einer Subsession

Verwendung des gleichen Control-Sockets, über den die PRIMARY-Sitzung erstellt wurde:

```
->  SESSION ADD
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See above for DATAGRAM2/3
          ID=$nickname                         # must be unique
          [PORT=$port]                         # Required for DATAGRAM* and RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # For outbound traffic, default 0
          [TO_PORT=nnn]                        # For outbound traffic, default 0
          [PROTOCOL=nnn]                       # For outbound traffic for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [LISTEN_PORT=nnn]                    # For inbound traffic, default is the FROM_PORT value.
                                               # For STYLE=STREAM, only the FROM_PORT value or 0 is allowed.
          [LISTEN_PROTOCOL=nnn]                # For inbound traffic for STYLE=RAW only.
                                               # Default is the PROTOCOL value; 6 (streaming) is disallowed
          [HEADER={true,false}]                # For STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
Die SAM bridge wird mit Erfolg oder Fehler antworten, wie in [der Antwort auf ein Standard-SESSION CREATE](#session-creation-response). Da die tunnel bereits beim primären SESSION CREATE erstellt wurden, sollte die SAM bridge sofort antworten.

Setzen Sie die DESTINATION-Option nicht bei einem SESSION ADD. Die Untersitzung wird das in der primären Sitzung angegebene Ziel verwenden. Alle Untersitzungen müssen über den Control-Socket hinzugefügt werden, d.h. über dieselbe Verbindung, über die Sie die primäre Sitzung erstellt haben.

Mehrere Subsessions müssen ausreichend unterschiedliche Optionen haben, damit eingehende Daten korrekt geroutet werden können. Insbesondere müssen mehrere Sessions desselben Typs unterschiedliche LISTEN_PORT-Optionen haben (und/oder LISTEN_PROTOCOL, nur für RAW). Ein SESSION ADD mit Listen-Port und Protokoll, die eine bestehende Subsession duplizieren, führt zu einem Fehler.

Der LISTEN_PORT ist der lokale I2P-Port, d.h. der Empfangs-(TO-)Port für eingehende Daten. Wenn der LISTEN_PORT nicht angegeben ist, wird der FROM_PORT-Wert verwendet. Wenn weder LISTEN_PORT noch FROM_PORT angegeben sind, basiert das eingehende Routing ausschließlich auf STYLE und PROTOCOL. Für LISTEN_PORT und LISTEN_PROTOCOL bedeutet 0 jeden beliebigen Wert, also einen Platzhalter. Wenn sowohl LISTEN_PORT als auch LISTEN_PROTOCOL 0 sind, wird diese Subsession zur Standardeinstellung für eingehenden Traffic, der nicht zu einer anderen Subsession weitergeleitet wird. Eingehender Streaming-Traffic (Protokoll 6) wird niemals zu einer RAW-Subsession weitergeleitet, auch wenn ihr LISTEN_PROTOCOL 0 ist. Eine RAW-Subsession darf kein LISTEN_PROTOCOL von 6 setzen. Wenn es keine Standard- oder Subsession gibt, die dem Protokoll und Port des eingehenden Traffics entspricht, werden diese Daten verworfen.

Verwenden Sie die Subsession-ID, nicht die primäre Session-ID, zum Senden und Empfangen von Daten. Alle Befehle wie STREAM CONNECT, DATAGRAM SEND usw. müssen die Subsession-ID verwenden.

Alle Utility-Befehle werden in einer primären Session oder Subsession unterstützt. v1/v2 Datagram/Raw Senden/Empfangen wird in einer primären Session oder in Subsessions nicht unterstützt.

#### Eine Subsession stoppen

Verwendung des gleichen Kontroll-Sockets, auf dem die PRIMARY-Sitzung erstellt wurde:

```
->  SESSION REMOVE
          ID=$nickname
```
Dies entfernt eine Untersession von der primären Session. Setzen Sie keine anderen Optionen bei einem SESSION REMOVE. Untersessions müssen über den Kontroll-Socket entfernt werden, d.h. über dieselbe Verbindung, auf der Sie die primäre Session erstellt haben. Nachdem eine Untersession entfernt wurde, wird sie geschlossen und kann nicht mehr zum Senden oder Empfangen von Daten verwendet werden.

Die SAM bridge wird mit Erfolg oder Fehlschlag antworten, wie in [der Antwort auf eine Standard SESSION CREATE](#session-creation-response).

### SAM Utility-Befehle

Einige Hilfsbefehle erfordern eine bereits bestehende Sitzung und andere nicht. Siehe Details unten.

#### Hostname-Auflösung

Die folgende Nachricht kann vom Client verwendet werden, um die SAM bridge nach Namensauflösung zu fragen:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
welches beantwortet wird von

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
Der RESULT-Wert kann einer der folgenden sein:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Wenn NAME=ME, dann wird die Antwort das Ziel enthalten, das von der aktuellen Sitzung verwendet wird (nützlich, wenn Sie eine TRANSIENT-Sitzung verwenden). Wenn $result nicht OK ist, kann MESSAGE eine beschreibende Nachricht enthalten, wie "bad format", etc. INVALID_KEY bedeutet, dass etwas mit $name in der Anfrage nicht stimmt, möglicherweise ungültige Zeichen.

Das $destination ist die Base64-Kodierung der [Destination](/docs/specs/common-structures#type_Destination), welche 516 oder mehr Base64-Zeichen (387 oder mehr Bytes in binärer Form) umfasst, abhängig vom Signaturtyp.

NAMING LOOKUP erfordert nicht, dass zuerst eine Sitzung erstellt wurde. In manchen Implementierungen kann jedoch eine .b32.i2p-Abfrage, die nicht zwischengespeichert ist und eine Netzwerkabfrage erfordert, fehlschlagen, da keine Client-tunnel für die Abfrage verfügbar sind.

#### Namensauflösungsoptionen

NAMING LOOKUP wurde ab router API 0.9.66 erweitert, um Service-Lookups zu unterstützen. Die Unterstützung kann je nach Implementierung variieren. Siehe Proposal 167 für zusätzliche Informationen.

NAMING LOOKUP NAME=example.i2p OPTIONS=true fordert die Options-Zuordnung in der Antwort an. NAME kann eine vollständige base64-Destination sein, wenn OPTIONS=true.

Wenn die Ziel-Suche erfolgreich war und Optionen im leaseSet vorhanden waren, dann werden in der Antwort nach dem Ziel eine oder mehrere Optionen in der Form OPTION:schlüssel=wert folgen. Jede Option wird ein separates OPTION: Präfix haben. Alle Optionen aus dem leaseSet werden eingeschlossen, nicht nur Service-Record-Optionen. Zum Beispiel können Optionen für Parameter vorhanden sein, die in der Zukunft definiert werden. Beispiel:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Schlüssel, die '=' enthalten, und Schlüssel oder Werte, die einen Zeilenumbruch enthalten, werden als ungültig betrachtet und das Schlüssel/Wert-Paar wird aus der Antwort entfernt. Wenn keine Optionen im leaseSet gefunden werden, oder wenn das leaseSet Version 1 war, dann wird die Antwort keine Optionen enthalten. Wenn OPTIONS=true in der Abfrage enthalten war und das leaseSet nicht gefunden wird, wird ein neuer Ergebniswert LEASESET_NOT_FOUND zurückgegeben.

#### Destination Key-Generierung

Öffentliche und private Base64-Schlüssel können mit der folgenden Nachricht generiert werden:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
was beantwortet wird durch

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
Ab Version 3.1 (I2P 0.9.14) wird ein optionaler Parameter SIGNATURE_TYPE unterstützt. Der SIGNATURE_TYPE-Wert kann ein beliebiger Name (z.B. ECDSA_SHA256_P256, Groß-/Kleinschreibung irrelevant) oder eine Nummer (z.B. 1) sein, die von [Key Certificates](/docs/specs/common-structures#type_Certificate) unterstützt wird. Der Standard ist DSA_SHA1, was NICHT das ist, was Sie wollen. Für die meisten Anwendungen geben Sie bitte SIGNATURE_TYPE=7 an.

Das $destination ist die Base64-Kodierung der [Destination](/docs/specs/common-structures#type_Destination), die 516 oder mehr Base64-Zeichen (387 oder mehr Bytes in Binärform) umfasst, abhängig vom Signaturtyp.

Der $privkey ist die Base64-Kodierung der Verkettung der [Destination](/docs/specs/common-structures#type_Destination) gefolgt vom [Private Key](/docs/specs/common-structures#type_PrivateKey) gefolgt vom [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), was 884 oder mehr Base64-Zeichen (663 oder mehr Bytes im Binärformat) entspricht, abhängig vom Signaturtyp. Das Binärformat ist in der Private Key File spezifiziert.

Hinweise zum 256-Byte-Binary [Private Key](/docs/specs/common-structures#type_PrivateKey): Dieses Feld wird seit Version 0.6 (2005) nicht mehr verwendet. SAM-Implementierungen können zufällige Daten oder nur Nullen in diesem Feld senden; lassen Sie sich nicht von einer Reihe von AAAA im Base 64 beunruhigen. Die meisten Anwendungen werden einfach die Base 64-Zeichenkette speichern und sie unverändert im SESSION CREATE zurückgeben, oder sie für die Speicherung in Binärdaten dekodieren und dann für SESSION CREATE wieder kodieren. Anwendungen können jedoch auch das Base 64 dekodieren, die Binärdaten gemäß der PrivateKeyFile-Spezifikation parsen, den 256-Byte-Private-Key-Anteil verwerfen und ihn dann durch 256 Bytes zufälliger Daten oder Nullen ersetzen, wenn sie für SESSION CREATE neu kodieren. ALLE anderen Felder in der PrivateKeyFile-Spezifikation müssen erhalten bleiben. Dies würde 256 Bytes Dateisystem-Speicherplatz sparen, ist aber wahrscheinlich für die meisten Anwendungen den Aufwand nicht wert. Siehe Vorschlag 161 für zusätzliche Informationen und Hintergründe.

DEST GENERATE erfordert nicht, dass zuerst eine Session erstellt wurde.

DEST GENERATE kann nicht verwendet werden, um ein Ziel mit Offline-Signaturen zu erstellen.

#### PING/PONG (SAM 3.2 oder höher)

Entweder der Client oder der Server kann senden:

```
PING[ arbitrary text]
```
am Control-Port, mit der Antwort:

```
PONG[ arbitrary text from the ping]
```
zur Verwendung für Control Socket Keepalive. Jede Seite kann die Sitzung und den Socket schließen, wenn keine Antwort in angemessener Zeit empfangen wird, implementierungsabhängig.

Wenn eine Zeitüberschreitung beim Warten auf ein PONG vom Client auftritt, kann die Bridge senden:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
und dann die Verbindung trennen.

Wenn beim Warten auf ein PONG von der Bridge ein Timeout auftritt, kann der Client einfach die Verbindung trennen.

PING/PONG erfordern nicht, dass zuerst eine Sitzung erstellt wurde.

#### QUIT/STOP/EXIT (SAM 3.2 oder höher, optionale Funktionen)

Die Befehle QUIT, STOP und EXIT schließen die Sitzung und den Socket. Die Implementierung ist optional, um das Testen über telnet zu erleichtern. Ob es eine Antwort gibt, bevor der Socket geschlossen wird (zum Beispiel eine SESSION STATUS-Nachricht), ist implementierungsspezifisch und liegt außerhalb des Umfangs dieser Spezifikation.

QUIT/STOP/EXIT erfordern nicht, dass zuvor eine Session erstellt wurde.

#### HELP (optionale Funktion)

Server können einen HELP-Befehl implementieren. Die Implementierung ist optional, um das Testen über telnet zu erleichtern. Das Ausgabeformat und die Erkennung des Endes der Ausgabe sind implementierungsspezifisch und liegen außerhalb des Umfangs dieser Spezifikation.

HELP erfordert nicht, dass zuerst eine Session erstellt wurde.

#### Autorisierungskonfiguration (SAM 3.2 oder höher, optionales Feature)

Autorisierungskonfiguration mit dem AUTH-Befehl. Ein SAM-Server kann diese Befehle implementieren, um die dauerhafte Speicherung von Anmeldedaten zu ermöglichen. Die Konfiguration von Authentifizierung über diese Befehle hinaus ist implementierungsspezifisch und liegt außerhalb des Geltungsbereichs dieser Spezifikation.

- AUTH ENABLE aktiviert die Autorisierung für nachfolgende Verbindungen
- AUTH DISABLE deaktiviert die Autorisierung für nachfolgende Verbindungen
- AUTH ADD USER="foo" PASSWORD="bar" fügt einen Benutzer/Passwort hinzu
- AUTH REMOVE USER="foo" entfernt diesen Benutzer

Anführungszeichen für Benutzer und Passwort werden empfohlen, sind aber nicht erforderlich. Ein Anführungszeichen innerhalb eines Benutzers oder Passworts muss mit einem Backslash maskiert werden. Bei einem Fehler antwortet der Server mit einem I2P_ERROR und einer Nachricht.

AUTH erfordert nicht, dass zuerst eine Sitzung erstellt wurde.

### RESULT-Werte

Das sind die Werte, die das RESULT-Feld enthalten kann, mit ihrer Bedeutung:

```
OK              Operation completed successfully
CANT_REACH_PEER The peer exists, but cannot be reached
DUPLICATED_DEST The specified Destination is already in use
I2P_ERROR       A generic I2P error (e.g. I2CP disconnection, etc.)
INVALID_KEY     The specified key is not valid (bad format, etc.)
KEY_NOT_FOUND   The naming system can't resolve the given name
PEER_NOT_FOUND  The peer cannot be found on the network
TIMEOUT         Timeout while waiting for an event (e.g. peer answer)
LEASESET_NOT_FOUND  See Name Lookup Options above. As of router API 0.9.66.
```
Verschiedene Implementierungen sind möglicherweise nicht konsistent darin, welches RESULT in verschiedenen Szenarien zurückgegeben wird.

Die meisten Antworten mit einem RESULT, außer OK, enthalten auch eine MESSAGE mit zusätzlichen Informationen. Die MESSAGE ist im Allgemeinen hilfreich beim Debuggen von Problemen. MESSAGE-Strings sind jedoch implementierungsabhängig, können vom SAM-Server in die aktuelle Locale übersetzt werden oder auch nicht, können interne implementierungsspezifische Informationen wie Exceptions enthalten und können ohne Vorankündigung geändert werden. Während SAM-Clients MESSAGE-Strings den Benutzern anzeigen können, sollten sie keine programmatischen Entscheidungen basierend auf diesen Strings treffen, da dies fehleranfällig wäre.

### Tunnel-, I2CP- und Streaming-Optionen

Diese Optionen können als Name=Wert-Paare in der SAM SESSION CREATE Zeile übergeben werden.

Alle Sitzungen können [I2CP-Optionen wie tunnel-Längen und -Mengen](/docs/protocol/i2cp#options) enthalten. STREAM-Sitzungen können [Streaming-Bibliothek-Optionen](/docs/api/streaming#options) enthalten.

Siehe diese Referenzen für Optionsnamen und Standardwerte. Die referenzierte Dokumentation ist für die Java-Router-Implementierung. Standardwerte können sich ändern. Optionsnamen und -werte sind groß-/kleinschreibungsabhängig. Andere Router-Implementierungen unterstützen möglicherweise nicht alle Optionen und haben möglicherweise andere Standardwerte; konsultieren Sie die Router-Dokumentation für Details.

### BASE 64 Hinweise

Base 64-Kodierung muss das I2P-Standard Base 64-Alphabet "A-Z, a-z, 0-9, -, ~" verwenden.

### Standard SAM-Einrichtung

Der Standard-SAM-Port ist 7656. SAM ist standardmäßig im Java I2P Router nicht aktiviert; es muss manuell gestartet oder für den automatischen Start konfiguriert werden, entweder auf der Clients-Konfigurationsseite in der Router-Konsole oder in der clients.config-Datei. Der Standard-SAM-UDP-Port ist 7655 und lauscht auf 127.0.0.1. Diese können im Java router geändert werden, indem die Argumente sam.udp.port=nnnnn und/oder sam.udp.host=w.x.y.z zum Aufruf oder zur SESSION-Zeile hinzugefügt werden.

Die Konfiguration in anderen Routern ist implementierungsspezifisch. Siehe [die i2pd-Konfigurationsanleitung hier](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).

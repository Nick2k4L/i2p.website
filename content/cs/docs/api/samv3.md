---
title: "SAM V3"
description: "Protokol Simple Anonymous Messaging pro non-Java I2P aplikace"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM je jednoduchý klientský protokol pro interakci s I2P. SAM je doporučený protokol pro aplikace napsané v jiných jazycích než Java pro připojení k síti I2P a je podporován více implementacemi routerů. Aplikace v Javě by měly používat streaming nebo I2CP API přímo.

SAMv3 verze 3 byla představena ve vydání I2P 0.7.3 (květen 2009) a je stabilní a podporované rozhraní. Verze 3.1 je také stabilní a podporuje možnost typu podpisu, což je důrazně doporučeno. Novější verze 3.x podporují pokročilé funkce. Poznámka: i2pd v současnosti nepodporuje většinu funkcí verzí 3.2 a 3.3.

Alternativy: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (zastaralé)](/docs/api/bob). Zastaralé verze: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Známé SAM knihovny

Varování: Některé z těchto mohou být velmi staré nebo nepodporované. Žádné nejsou testovány, kontrolovány nebo udržovány projektem I2P, pokud není uvedeno jinak níže. Proveďte si vlastní průzkum.

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
## Rychlý start

Pro implementaci základní TCP-only, peer-to-peer aplikace musí klient podporovat následující příkazy:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Potřebné pro všechny zbývající příkazy
- `DEST GENERATE SIGNATURE_TYPE=7` - Pro vygenerování našeho soukromého klíče a destination
- `NAMING LOOKUP NAME=...` - Pro konverzi .i2p adres na destinations
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Potřebné pro STREAM CONNECT a STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Pro vytváření odchozích spojení
- `STREAM ACCEPT ID=...` - Pro přijímání příchozích spojení

## Obecné pokyny pro vývojáře

### Návrh aplikace

SAM sessions (nebo uvnitř I2P, tunnel pooly nebo sady tunnelů) jsou navrženy tak, aby byly dlouhodobé. Většina aplikací bude potřebovat pouze jednu session, vytvořenou při spuštění a uzavřenou při ukončení. I2P se liší od Toru, kde mohou být okruhy rychle vytvářeny a zahazovány. Důkladně zvažte a poraďte se s vývojáři I2P před navržením vaší aplikace tak, aby používala více než jednu nebo dvě současné sessions, nebo je rychle vytvářela a zahazovala. Většina modelů hrozeb nevyžaduje jedinečnou session pro každé připojení.

Také se prosím ujistěte, že nastavení vaší aplikace (a pokyny pro uživatele ohledně nastavení routeru, nebo výchozí nastavení routeru pokud router přibalujete) povedou k tomu, že vaši uživatelé budou přispívat síti více zdrojů, než kolik spotřebují. I2P je peer-to-peer síť a síť nemůže přežít, pokud populární aplikace přivede síť do trvalého přetížení.

### Kompatibilita a testování

Implementace Java I2P a i2pd router jsou nezávislé a mají drobné rozdíly v chování, podpoře funkcí a výchozích nastaveních. Otestujte prosím svou aplikaci s nejnovější verzí obou routerů.

i2pd SAM je ve výchozím nastavení povoleno; Java I2P SAM nikoli. Poskytněte uživatelům pokyny, jak povolit SAM v Java I2P (přes /configclients v konzoli routeru), a/nebo poskytněte uživateli dobrou chybovou zprávu, pokud počáteční připojení selže, např. "ujistěte se, že I2P běží a SAM rozhraní je povoleno".

Java I2P a i2pd routery mají různé výchozí hodnoty pro množství tunelů. Výchozí hodnota pro Java je 2 a výchozí hodnota pro i2pd je 5. Pro většinu aplikací s nízkou až střední šířkou pásma a nízkým až středním počtem připojení je dostačující 2 nebo 3. Pro konzistentní výkon s Java I2P a i2pd routery prosím specifikujte množství tunelů ve zprávě SESSION CREATE. Viz níže.

Pro další pokyny pro vývojáře, jak zajistit, aby vaše aplikace používala pouze potřebné zdroje, si prosím přečtěte [náš průvodce pro zabalení I2P s vaší aplikací](/docs/applications/embedding).

### Typy podpisů a šifrování

I2P podporuje více typů podpisů a šifrování. Kvůli zpětné kompatibilitě SAM standardně používá staré a neefektivní typy, takže všichni klienti by měli specifikovat novější typy.

Typ podpisu je specifikován v příkazech DEST GENERATE a SESSION CREATE (pro přechodné). Všichni klienti by měli nastavit `SIGNATURE_TYPE=7` (Ed25519).

Typ šifrování je specifikován v příkazu SESSION CREATE. Je povoleno více typů šifrování. Klienti by měli nastavit buď `i2cp.leaseSetEncType=4` (pouze pro ECIES-X25519) nebo `i2cp.leaseSetEncType=4,0` (pro ECIES-X25519 a ElGamal, pokud je vyžadována kompatibilita).

## Změny ve verzi 3

### Změny ve verzi 3.0

Verze 3.0 byla představena v I2P vydání 0.7.3. SAM v2 poskytoval způsob správy několika socketů na stejné I2P destinaci *paralelně*, tj. klient nemusel čekat na úspěšné odeslání dat na jednom socketu před odesláním dat na jiném socketu. Ale všechna data procházela přes stejný socket klient-SAM, což bylo pro klienta poměrně složité na správu.

SAM v3 spravuje sockety jiným způsobem: každý *I2P socket* odpovídá jedinečnému client-to-SAM socketu, což je mnohem jednodušší na zpracování. Toto je podobné [BOB](/docs/api/bob).

SAMv3 také nabízí UDP port pro odesílání datagramů přes I2P a může přeposílat I2P datagramy zpět na datagramový server klienta.

### Změny verze 3.1

Verze 3.1 byla představena v Java I2P vydání 0.9.14 (červenec 2014). SAM 3.1 je doporučená minimální implementace SAM kvůli podpoře lepších typů podpisů než SAM 3.0. i2pd také podporuje většinu funkcí verze 3.1.

- DEST GENERATE a SESSION CREATE nyní podporují parametr SIGNATURE_TYPE.
- Parametry MIN a MAX v HELLO VERSION jsou nyní volitelné.
- Parametry MIN a MAX v HELLO VERSION nyní podporují jednociferné verze jako "3".
- RAW SEND je nyní podporováno na bridge socketu.

### Změny ve verzi 3.2

Verze 3.2 byla představena v Java I2P vydání 0.9.24 (leden 2016). Upozorňujeme, že i2pd v současnosti nepodporuje většinu funkcí verze 3.2.

#### Podpora portu a protokolu I2CP

- SESSION CREATE možnosti FROM_PORT a TO_PORT
- SESSION CREATE STYLE=RAW možnost PROTOCOL
- STREAM CONNECT, DATAGRAM SEND a RAW SEND možnosti FROM_PORT a TO_PORT
- RAW SEND možnost PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED a přeposílané nebo přijaté streamy a odpověditelné datagramy, zahrnují FROM_PORT a TO_PORT
- RAW session možnost HEADER=true způsobí, že přeposílané raw datagramy budou předřazeny řádkem obsahujícím PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- První řádek datagramů odeslaných přes port 7655 může nyní začínat libovolnou verzí 3.x
- První řádek datagramů odeslaných přes port 7655 může obsahovat libovolné z možností FROM_PORT, TO_PORT, PROTOCOL
- RAW RECEIVED zahrnuje PROTOCOL=nnn

#### SSL a autentifikace

- USER/PASSWORD v parametrech HELLO pro autorizaci. Viz [níže](#authorization).
- Volitelná konfigurace autorizace pomocí příkazu AUTH. Viz [níže](#authorization-configuration-sam-32-or-higher-optional-feature).
- Volitelná podpora SSL/TLS na řídicím socketu. Viz [níže](#ssl).
- Možnost STREAM FORWARD SSL=true

#### Vícevláknové zpracování

- Souběžné čekající STREAM ACCEPT jsou povoleny na stejném session ID.

#### Parsování příkazové řádky a Keepalive

- Volitelné příkazy QUIT, STOP a EXIT pro uzavření relace a socketu. Viz [níže](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- Parsování příkazů bude správně zpracovávat UTF-8
- Parsování příkazů spolehlivě zpracovává bílé znaky uvnitř uvozovek
- Zpětné lomítko '\\' může escapovat uvozovky na příkazové řádce
- Doporučuje se, aby server mapoval příkazy na velká písmena, pro snadnější testování přes telnet.
- Prázdné hodnoty voleb jako PROTOCOL nebo PROTOCOL= mohou být povoleny, závisí na implementaci.
- PING/PONG pro udržení spojení. Viz níže.
- Servery mohou implementovat časové limity pro HELLO nebo následné příkazy, závisí na implementaci.

### Změny ve verzi 3.3

Verze 3.3 byla představena v Java I2P vydání 0.9.25 (březen 2016). Upozorňujeme, že i2pd v současnosti nepodporuje většinu funkcí verze 3.3.

- Stejná relace může být použita současně pro streamy, datagramy a raw. Příchozí pakety a streamy budou směrovány na základě I2P protokolu a cílového portu. Viz [sekce PRIMARY níže](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND a RAW SEND nyní podporují možnosti SEND_TAGS, TAG_THRESHOLD, EXPIRES a SEND_LEASESET. Viz [sekce odesílání datagramů níže](#sending-repliable-or-raw-datagrams).

## Protokol verze 3

### Přehled specifikace Simple Anonymous Messaging (SAM) verze 3.3

Klientská aplikace komunikuje se SAM bridge, který se stará o veškerou I2P funkcionalité (používá [streaming library](/docs/api/streaming) pro virtuální streamy, nebo [I2CP](/docs/protocol/i2cp) přímo pro datagramy).

Ve výchozím nastavení je komunikace mezi klientem a SAM bridge nešifrovaná a neautentifikovaná. SAM bridge může podporovat SSL/TLS připojení; podrobnosti konfigurace a implementace jsou mimo rozsah této specifikace. Od SAM 3.2 jsou v počátečním handshake podporovány volitelné autentifikační parametry uživatelské jméno/heslo a bridge je může vyžadovat.

I2P komunikace může mít několik odlišných forem:

- [Virtuální proudy](/docs/api/streaming)
- [Odpovědné a autentizované datagramy](/docs/specs/datagrams#repliable) (zprávy s polem FROM)
- [Anonymní datagramy](/docs/specs/datagrams#raw) (surové anonymní zprávy)
- [Datagram2](/docs/specs/datagrams#datagram2) (nový odpovědný a autentizovaný formát)
- [Datagram3](/docs/specs/datagrams#datagram3) (nový odpovědný, ale neautentizovaný formát)

I2P komunikace jsou podporovány I2P relacemi a každá I2P relace je vázána na adresu (nazvanou destination). I2P relace je přidružena k jednomu ze tří výše uvedených typů a nemůže nést komunikaci jiného typu, pokud nepoužívá [PRIMARY relace](#sam-primary-sessions-v33-and-higher).

### Kódování a escapování

Všechny tyto SAM zprávy jsou odesílány na jednom řádku, ukončeném znakem nového řádku (\\n). Před verzí SAM 3.2 byla podporována pouze 7-bitová ASCII. Od verze SAM 3.2 musí být použito kódování UTF-8. Jakékoli klíče nebo hodnoty zakódované v UTF8 by měly fungovat.

Formátování uvedené v této specifikaci níže slouží pouze pro čitelnost, a zatímco první dvě slova v každé zprávě musí zůstat ve svém specifickém pořadí, pořadí dvojic klíč=hodnota se může měnit (např. "ONE TWO A=B C=D" nebo "ONE TWO C=D A=B" jsou obě perfektně platné konstrukce). Navíc je protokol citlivý na velikost písmen. V následujícím textu jsou příklady zpráv předcházeny "->" pro zprávy odeslané klientem na SAM bridge a "<-" pro zprávy odeslané SAM bridge klientovi.

Základní příkaz nebo odpověď má jednu z následujících forem:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND bez SUBCOMMAND je podporován pouze pro některé nové příkazy v SAMv3.2.

Páry Key=value musí být odděleny jednou mezerou. (Od SAM 3.2 jsou povoleny i vícenásobné mezery) Hodnoty musí být uzavřeny v uvozovkách, pokud obsahují mezery, např. key="dlouhý text hodnoty". (Před SAM 3.2 to v některých implementacích nefungovalo spolehlivě)

Před SAMv3.2 neexistoval žádný mechanismus pro escapování. Od SAMv3.2 mohou být dvojité uvozovky escapovány pomocí zpětného lomítka '\\' a zpětné lomítko může být reprezentováno jako dvě zpětná lomítka '\\\\'.

### Prázdné hodnoty

Od SAMv3.2 mohou být povoleny prázdné hodnoty možností jako KEY, KEY= nebo KEY="", závisí na implementaci.

### Rozlišování velikosti písmen

Protokol, jak je specifikován, je citlivý na velikost písmen. Je doporučeno, ale není vyžadováno, aby server mapoval příkazy na velká písmena, pro snadnější testování přes telnet. To by umožnilo, například, aby "hello version" fungovalo. Toto je závislé na implementaci. Nemapujte klíče nebo hodnoty na velká písmena, protože by to poškodilo možnosti [I2CP](/docs/protocol/i2cp).

### SAM Connection Handshake

Žádná SAM komunikace nemůže probíhat, dokud se klient a bridge neshodnou na verzi protokolu, což se provádí tak, že klient odešle HELLO a bridge odešle HELLO REPLY:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
a

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
Od verze 3.1 (I2P 0.9.14) jsou parametry MIN a MAX volitelné. SAM vždy vrátí nejvyšší možnou verzi s ohledem na omezení MIN a MAX, nebo aktuální verzi serveru, pokud nejsou zadána žádná omezení.

Pokud SAM bridge nemůže najít vhodnou verzi, odpoví:

```
<- HELLO REPLY RESULT=NOVERSION
```
Pokud nastane nějaká chyba, například nesprávný formát požadavku, odpoví:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

Řídicí socket serveru může volitelně nabízet podporu SSL/TLS, jak je nakonfigurováno na serveru a klientovi. Implementace mohou nabízet i další transportní vrstvy; to je mimo rozsah definice protokolu.

#### Autorizace

Pro autorizaci klient přidá USER="xxx" PASSWORD="yyy" do parametrů HELLO. Dvojité uvozovky pro uživatelské jméno a heslo jsou doporučené, ale nejsou povinné. Dvojité uvozovky uvnitř uživatelského jména nebo hesla musí být escapovány zpětným lomítkem. Při selhání server odpoví s I2P_ERROR a zprávou. Doporučuje se povolit SSL na všech SAM serverech, kde je vyžadována autorizace.

#### Časové limity

Servery mohou implementovat časové limity pro příkaz HELLO nebo následující příkazy, což závisí na implementaci. Klienti by měli po připojení rychle odeslat HELLO a následující příkaz.

Pokud dojde k timeoutu před přijetím HELLO, bridge odpoví:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
a poté se odpojí.

Pokud dojde k vypršení časového limitu poté, co je přijato HELLO, ale před dalším příkazem, bridge odpoví:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
a poté se odpojí.

### I2CP Porty a Protokol

Od verze SAM 3.2 mohou být I2CP porty a protokol specifikovány klientem odesílatele SAM k předání do [I2CP](/docs/protocol/i2cp), a SAM bridge předá přijaté informace o I2CP portu a protokolu SAM klientovi.

Pro FROM_PORT a TO_PORT je platný rozsah 0-65535 a výchozí hodnota je 0.

Pro PROTOCOL, který lze specifikovat pouze pro RAW, je platný rozsah 0-255 a výchozí hodnota je 18.

Pro příkazy SESSION jsou zadané porty a protokol výchozí hodnoty pro tuto relaci. Pro jednotlivé streamy nebo datagramy zadané porty a protokol přepíší výchozí hodnoty relace. Pro přijaté streamy nebo datagramy jsou uvedené porty a protokol takové, jak byly přijaty z [I2CP](/docs/protocol/i2cp).

#### Důležité rozdíly od standardního IP

I2CP porty jsou určeny pro I2P sockety a datagramy. Nesouvisí s vašimi lokálními sockety připojujícími se k SAM.

- Port 0 je platný a má speciální význam.
- Porty 1-1023 nejsou speciální ani privilegované.
- Servery ve výchozím nastavení naslouchají na portu 0, což znamená "všechny porty".
- Klienti ve výchozím nastavení odesílají na port 0, což znamená "libovolný port".
- Klienti ve výchozím nastavení odesílají z portu 0, což znamená "nespecifikovaný".
- Servery mohou mít službu naslouchající na portu 0 a další služby naslouchající na vyšších portech. Pokud ano, služba na portu 0 je výchozí a bude připojena, pokud port příchozího socketu nebo datagramu neodpovídá jiné službě.
- Většina I2P destinací má spuštěnou pouze jednu službu, takže můžete použít výchozí nastavení a ignorovat konfiguraci I2CP portů.
- Pro specifikaci I2CP portů je vyžadován SAM 3.2 nebo 3.3.
- Pokud nepotřebujete I2CP porty, nepotřebujete SAM 3.2 nebo 3.3; verze 3.1 je dostačující.
- Protokol 0 je platný a znamená "libovolný protokol". To se nedoporučuje a pravděpodobně nebude fungovat.
- I2P sockety jsou sledovány pomocí interního ID připojení. Proto neexistuje požadavek, aby 5-tice dest:port:dest:port:protocol byla jedinečná. Například mezi dvěma destinacemi může existovat více socketů se stejnými porty. Klienti nepotřebují vybírat "volný port" pro odchozí připojení.

Pokud navrhujete aplikaci SAMv3.3 s více podsezení, pečlivě zvažte, jak efektivně používat porty a protokoly. Další informace najdete ve specifikaci [I2CP](/docs/protocol/i2cp).

### SAM Sessions

SAM session je vytvořena klientem otevřením socketu k SAM bridge, provedením handshaku a odesláním zprávy SESSION CREATE, a session končí při odpojení socketu.

Každá registrovaná I2P Destination je jednoznačně asociována s ID relace (nebo přezdívkou). ID relací, včetně ID podrelací pro PRIMARY relace, musí být globálně jedinečná na SAM serveru. Aby se předešlo možným kolizím ID s ostatními klienty, je doporučenou praxí, aby klient generoval ID náhodně.

Každá relace je jedinečně spojena s:

- socket, ze kterého klient vytváří relaci
- jeho ID (nebo přezdívka)

#### Požadavek na vytvoření relace

Zpráva pro vytvoření relace může používat pouze jednu z těchto forem (zprávy přijaté prostřednictvím jiných forem jsou zodpovězeny chybovou zprávou):

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
DESTINATION specifikuje, jaký cíl by měl být použit pro odesílání a přijímání zpráv/streamů. $privkey je base 64 zřetězení [Destination](/docs/specs/common-structures#type_Destination) následovaného [Private Key](/docs/specs/common-structures#type_PrivateKey) následovaným [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), volitelně následovaným [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), což je 663 nebo více bytů v binárním formátu a 884 nebo více bytů v base 64, v závislosti na typu podpisu. Binární formát je specifikován v Private Key File. Viz další poznámky o [Private Key](/docs/specs/common-structures#type_PrivateKey) v sekci Generování klíčů cíle níže.

Pokud je soukromý klíč pro podepisování samé nuly, následuje sekce [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature). Offline podpisy jsou podporovány pouze pro relace STREAM a RAW. Offline podpisy nemohou být vytvořeny s DESTINATION=TRANSIENT. Formát sekce offline podpisu je:

1. Časové razítko vypršení (4 bajty, big endian, sekundy od epochy, přetečení v roce 2106)
2. Typ podpisu přechodného veřejného klíče pro podepisování (2 bajty, big endian)
3. Přechodný veřejný klíč pro podepisování (délka podle specifikace typu přechodného podpisu)
4. Podpis výše uvedených tří polí offline klíčem (délka podle specifikace typu podpisu cíle)
5. Přechodný soukromý klíč pro podepisování (délka podle specifikace typu přechodného podpisu)

Pokud je cíl specifikován jako TRANSIENT, SAM bridge vytvoří nový cíl. Od verze 3.1 (I2P 0.9.14), pokud je cíl TRANSIENT, je podporován volitelný parametr SIGNATURE_TYPE. Hodnota SIGNATURE_TYPE může být jakýkoli název (např. ECDSA_SHA256_P256, bez rozlišování velkých a malých písmen) nebo číslo (např. 1) podporované [Key Certificates](/docs/specs/common-structures#type_Certificate). Výchozí hodnota je DSA_SHA1, což NENÍ to, co chcete. Pro většinu aplikací prosím specifikujte SIGNATURE_TYPE=7.

$nickname je volba klienta. Mezery nejsou povoleny.

Dodatečné zadané možnosti jsou předány do konfigurace I2P relace, pokud nejsou interpretovány SAM mostem (např. outbound.length=0).

Java I2P a i2pd routery mají různé výchozí hodnoty pro množství tunelů. Výchozí hodnota pro Java je 2 a výchozí hodnota pro i2pd je 5. Pro většinu aplikací s nízkou až střední šířkou pásma a nízkým až středním počtem připojení postačí 2 nebo 3. Prosím specifikujte množství tunelů ve zprávě SESSION CREATE pro dosažení konzistentního výkonu s Java I2P a i2pd routery, pomocí možností např. inbound.quantity=3 outbound.quantity=3. Tyto a další možnosti [jsou zdokumentovány v odkazech níže](#tunnel-i2cp-and-streaming-options).

SAM bridge samotný by již měl být nakonfigurován s tím, který router má používat pro komunikaci přes I2P (ačkoliv v případě potřeby může existovat způsob, jak toto nastavení přepsat, např. i2cp.tcp.host=localhost a i2cp.tcp.port=7654).

#### Odpověď na vytvoření relace

Po obdržení zprávy o vytvoření session SAM bridge odpoví zprávou o stavu session následovně:

Pokud bylo vytvoření úspěšné:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
$privkey je base 64 reprezentace zřetězení [Destination](/docs/specs/common-structures#type_Destination) následovaného [Private Key](/docs/specs/common-structures#type_PrivateKey) následovaným [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), volitelně následovaným [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), což je 663 nebo více bytů v binární podobě a 884 nebo více bytů v base 64, v závislosti na typu podpisu. Binární formát je specifikován v Private Key File.

Pokud SESSION CREATE obsahovalo privátní klíč pro podepisování složený ze samých nul a sekci [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), odpověď SESSION STATUS bude obsahovat stejná data ve stejném formátu. Podrobnosti viz sekce SESSION CREATE výše.

Pokud je přezdívka již přidružena k relaci:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Pokud je cíl již používán:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Pokud cíl není platný privátní klíč destination:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Pokud došlo k jiné chybě:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Pokud to není v pořádku, MESSAGE by měla obsahovat informace čitelné pro člověka o tom, proč nemohla být relace vytvořena.

Poznámka: router buduje tunnely před odpovědí se SESSION STATUS. To může trvat několik sekund, nebo při startu routeru nebo během vážného přetížení sítě i minutu či více. Pokud neuspěje, router neodpoví chybovou zprávou několik minut. Nenastavujte krátký timeout při čekání na odpověď. Neopouštějte session během budování tunnelů a nepokoušejte se znovu.

SAM relace žijí a umírají se socketem, se kterým jsou spojené. Když se socket zavře, relace umře a všechny komunikace používající tuto relaci umírají ve stejný okamžik. A naopak, když relace z jakéhokoli důvodu umře, SAM bridge zavře socket.

### SAM virtuální streamy

Virtuální proudy jsou garantovány k spolehlivému odesílání v pořadí, s oznámením o selhání a úspěchu, jakmile je k dispozici.

Streamy jsou obousměrné komunikační sockety mezi dvěma I2P destinacemi, ale jejich otevření musí být vyžádáno jednou z nich. Dále se příkazy CONNECT používají SAM klientem pro takové požadavky. Příkazy FORWARD / ACCEPT používá SAM klient, když chce naslouchat požadavkům přicházejícím z jiných I2P destinací.

### SAM Virtual Streams: CONNECT

Klient požádá o připojení pomocí:

- otevření nového socketu s SAM bridge
- předání stejného HELLO handshake jako výše
- odeslání příkazu STREAM CONNECT

#### Žádost o připojení

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Toto vytvoří nové virtuální spojení z lokální relace, jejíž ID je $nickname, k určenému protějšku.

Cílem je $destination, což je base 64 [Destination](/docs/specs/common-structures#type_Destination), které má 516 nebo více base 64 znaků (387 nebo více bajtů v binárním formátu), v závislosti na typu podpisu.

**POZNÁMKA:** Přibližně od roku 2014 (SAM v3.1) Java I2P také podporuje názvy hostitelů a b32 adresy pro $destination, ale to dříve nebylo zdokumentováno. Názvy hostitelů a b32 adresy jsou nyní oficiálně podporovány Java I2P od vydání 0.9.48. Router i2pd podporuje názvy hostitelů a b32 adresy od vydání 2.38.0 (0.9.50). U obou routerů podpora "b32" zahrnuje podporu rozšířených "b33" adres pro slepé destinace.

#### Odpověď na připojení

Pokud je předán SILENT=true, SAM bridge nevydá na socketu žádnou další zprávu. Pokud připojení selže, socket bude uzavřen. Pokud připojení uspěje, všechna zbývající data procházející aktuálním socketem jsou přeposílána z a do připojeného I2P destination peer.

Pokud je SILENT=false, což je výchozí hodnota, SAM bridge pošle svému klientovi poslední zprávu před přesměrováním nebo ukončením socketu:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Hodnota RESULT může být jedna z následujících:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
Pokud je RESULT OK, všechna zbývající data procházející aktuálním socketem jsou přeposílána z a do připojeného I2P cílového uzlu. Pokud připojení nebylo možné (timeout apod.), RESULT bude obsahovat příslušnou chybovou hodnotu (doprovázenou volitelnou lidsky čitelnou MESSAGE) a SAM bridge zavře socket.

Timeout pro připojení router streamu je interně přibližně jedna minuta, závislý na implementaci. Nenastavujte kratší timeout při čekání na odpověď.

### SAM Virtual Streams: ACCEPT

Klient čeká na příchozí požadavek o připojení následujícím způsobem:

- otevření nového socketu s SAM bridge
- předání stejného HELLO handshake jako výše
- odeslání příkazu STREAM ACCEPT

#### Přijmout žádost

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Toto způsobí, že relace ${nickname} bude naslouchat jednomu příchozímu požadavku na připojení z I2P sítě. ACCEPT není povoleno, když je na relaci aktivní FORWARD.

Od SAMv3.2 je na stejném session ID povoleno více současných čekajících STREAM ACCEPTů (i se stejným portem). Před verzí 3.2 by současné accepty selhaly s ALREADY_ACCEPTING. Poznámka: Java I2P také podporuje současné ACCEPTy na SAMv3.1 od verze 0.9.24 (2016-01). i2pd také podporuje současné ACCEPTy na SAMv3.1 od verze 2.50.0 (2023-12).

#### Přijmout odpověď

Pokud je předán SILENT=true, SAM bridge nevydá na socketu žádnou další zprávu. Pokud příjem selže, socket bude uzavřen. Pokud příjem uspěje, všechna zbývající data procházející aktuálním socketem jsou přeposílána z a do připojeného I2P destination peer. Pro spolehlivost a aby bylo možné přijmout destination pro příchozí spojení, je doporučeno SILENT=false.

Pokud je SILENT=false, což je výchozí hodnota, SAM bridge odpoví:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Hodnota RESULT může být jedna z následujících:

```
OK
I2P_ERROR
INVALID_ID
```
Pokud výsledek není OK, socket je okamžitě uzavřen SAM bridge. Pokud je výsledek OK, SAM bridge začne čekat na příchozí požadavek o připojení od jiného I2P peer. Když požadavek dorazí, SAM bridge ho přijme a:

Pokud bylo předáno SILENT=true, SAM bridge nevydá na klientském socketu žádnou další zprávu. Všechna zbývající data procházející aktuálním socketem jsou předávána z a do připojené I2P destination peer.

Pokud byl předán SILENT=false, což je výchozí hodnota, SAM bridge odešle klientovi ASCII řádek obsahující base64 veřejný destination klíč žádajícího peer a dodatečné informace pouze pro SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Po tomto řádku ukončeném '\\n' jsou veškerá zbývající data procházející aktuálním socketem přeposílána z a do připojeného I2P destination partnera, dokud jeden z partnerů socket nezavře.

#### Chyby po OK

Ve vzácných případech může SAM bridge narazit na chybu po odeslání RESULT=OK, ale před navázáním spojení a odesláním řádku $destination klientovi. Tyto chyby mohou zahrnovat vypnutí routeru, restart routeru a zavření relace. V těchto případech, když SILENT=false, může SAM bridge, ale není to vyžadováno (závisí na implementaci), odeslat řádek:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
před okamžitým uzavřením socketu. Tento řádek samozřejmě není dekódovatelný jako platná Base 64 destination.

### SAM Virtual Streams: FORWARD

Klient může použít běžný socket server a čekat na požadavky na připojení přicházející z I2P. K tomu musí klient:

- otevřít nový socket s SAM bridge
- předat stejný HELLO handshake jako výše
- odeslat forward příkaz

#### Přeposílání požadavku

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Toto způsobí, že relace ${nickname} bude naslouchat příchozím požadavkům na připojení ze sítě I2P. FORWARD není povoleno, pokud v relaci probíhá čekající ACCEPT.

#### Předat odpověď

SILENT má výchozí hodnotu false. Bez ohledu na to, zda je SILENT true nebo false, SAM bridge vždy odpovídá zprávou STREAM STATUS. Všimněte si, že se jedná o jiné chování než u STREAM ACCEPT a STREAM CONNECT, když je SILENT=true. Zpráva STREAM STATUS je:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Hodnota RESULT může být jedna z následujících:

```
OK
I2P_ERROR
INVALID_ID
```
$host je hostname nebo IP adresa socket serveru, na který bude SAM předávat požadavky na připojení. Pokud není zadáno, SAM použije IP adresu socketu, který vydal forward příkaz.

$port je číslo portu socket serveru, na který SAM přesměruje požadavky na připojení. Je povinný.

Když přijde požadavek na spojení z I2P, SAM bridge otevře socket spojení na $host:$port. Pokud je přijato během méně než 3 sekund, SAM přijme spojení z I2P a poté:

Pokud bylo předáno SILENT=true, všechna data procházející získaným aktuálním socketem jsou přeposílána z a do připojeného I2P destination peer.

Pokud bylo předáno SILENT=false, což je výchozí hodnota, SAM bridge odešle na získaný socket ASCII řádek obsahující base64 veřejný klíč cíle požadujícího peer, a další informace pouze pro SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Po tomto řádku ukončeném '\\n' jsou všechna zbývající data procházející socketem přesměrována z a do připojené I2P destination peer, dokud jedna ze stran socket nezavře.

Od SAMv3.2, pokud je specifikováno SSL=true, je přesměrovávací socket přes SSL/TLS.

I2P router přestane naslouchat příchozím požadavkům na připojení, jakmile se "forwarding" socket uzavře.

### SAM Datagramy

SAMv3 poskytuje mechanismy pro odesílání a přijímání datagramů přes místní datagram sockety. Některé implementace SAMv3 také podporují starší způsob v1/v2 pro odesílání/přijímání datagramů přes SAM bridge socket. Obě jsou dokumentovány níže.

I2P podporuje čtyři typy datagramů:

- Odpověditelné a autentizované datagramy jsou předpony s cílem odesilatele a obsahují podpis odesilatele, takže příjemce může ověřit, že cíl odesilatele nebyl falšován, a může na datagram odpovědět. Nový formát Datagram2 je také odpověditelný a autentizovaný.
- Nový formát Datagram3 je odpověditelný, ale ne autentizovaný. Informace o odesilateli jsou neověřené.
- Surové datagramy neobsahují cíl odesilatele ani podpis.

Výchozí I2CP porty jsou definovány jak pro odpověditelné, tak pro nezpracované datagramy. I2CP port může být změněn pro nezpracované datagramy.

Běžný návrhový vzor protokolu je posílání repliable datagramů na servery s nějakým identifikátorem a server odpovídá surovým datagramem, který obsahuje tento identifikátor, takže odpověď může být korelována s požadavkem. Tento návrhový vzor eliminuje značnou režii repliable datagramů v odpovědích. Všechny volby I2CP protokolů a portů jsou specifické pro aplikaci a návrháři by měli tyto otázky vzít v úvahu.

Viz také důležité poznámky o MTU datagramu v sekci níže.

#### Odesílání odpověditelných nebo surových datagramů

Ačkoli I2P z podstaty neobsahuje adresu FROM, pro snadnější použití je poskytována dodatečná vrstva ve formě odpověditelných datagramů - neuspořádané a nespolehlivé zprávy o velikosti až 31744 bajtů, které obsahují adresu FROM (a ponechávají až 1KB pro hlavičkový materiál). Tato adresa FROM je interně ověřována pomocí SAM (využívá se podpisový klíč cíle k ověření zdroje) a zahrnuje prevenci před opakovaným přehráním.

Minimální velikost je 1. Pro nejlepší spolehlivost doručení se doporučuje maximální velikost přibližně 11 KB. Spolehlivost je nepřímo úměrná velikosti zprávy, možná dokonce exponenciálně.

Po navázání SAM relace s STYLE=DATAGRAM nebo STYLE=RAW může klient posílat odpověditelné nebo surové datagramy přes UDP port SAMu (ve výchozím nastavení 7655).

První řádek datagramu odeslaného přes tento port musí být v následujícím formátu. Vše je na jednom řádku (odděleno mezerami), zobrazeno na více řádcích pro přehlednost:

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
- 3.0 je verze SAM. Od SAM 3.2 je povolena jakákoli verze 3.x.
- $nickname je id DATAGRAM relace, která bude použita
- Cíl je $destination, což je base 64 [Destination](/docs/specs/common-structures#type_Destination), což je 516 nebo více base 64 znaků (387 nebo více bajtů v binárním formátu), v závislosti na typu podpisu. **POZNÁMKA:** Přibližně od roku 2014 (SAM v3.1) Java I2P také podporuje hostnames a b32 adresy pro $destination, ale to bylo dříve nedokumentováno. Hostnames a b32 adresy jsou nyní oficiálně podporovány Java I2P od verze 0.9.48. Router i2pd v současnosti nepodporuje hostnames a b32 adresy; podpora může být přidána v budoucí verzi.
- Všechny možnosti jsou nastavení per-datagram, která přepisují výchozí hodnoty specifikované v SESSION CREATE.
- Možnosti verze 3.3 SEND_TAGS, TAG_THRESHOLD, EXPIRES a SEND_LEASESET budou předány do [I2CP](/docs/protocol/i2cp), pokud jsou podporovány. Podrobnosti viz [specifikace I2CP](/docs/protocol/i2cp#msg_SendMessageExpire). Podpora SAM serverem je volitelná, bude tyto možnosti ignorovat, pokud nejsou podporovány.
- tento řádek je ukončen '\\n'.

První řádek bude SAM zahozen před odesláním zbývajících dat zprávy do zadaného cíle.

Pro alternativní metodu odesílání odpověditelných a surových datagramů viz [DATAGRAM SEND a RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: Příjem datagramu

Přijaté datagramy jsou zapisovány SAM na socket, ze kterého byla datagramová relace otevřena, pokud není ve příkazu SESSION CREATE specifikován přesměrovací PORT. Toto je způsob přijímání datagramů kompatibilní s v1/v2.

Když přijde datagram, bridge jej doručí klientovi prostřednictvím zprávy:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
Zdrojem je $destination, což je base 64 reprezentace [Destination](/docs/specs/common-structures#type_Destination), která má 516 nebo více base 64 znaků (387 nebo více bajtů v binární podobě), v závislosti na typu podpisu.

SAM bridge nikdy nevystavuje klientovi autentizační hlavičky nebo jiná pole, pouze data, která poskytl odesílatel. Toto pokračuje, dokud není relace ukončena (klientem, který ukončí spojení).

#### Přeposílání Raw nebo Odpovídatelných Datagramů

Při vytváření datagram session může klient požádat SAM, aby přeposílal příchozí zprávy na zadanou ip:port. Činí tak vydáním příkazu CREATE s možnostmi PORT a HOST:

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
$privkey je base 64 zřetězení [Destination](/docs/specs/common-structures#type_Destination) následovaného [Private Key](/docs/specs/common-structures#type_PrivateKey) následovaného [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), volitelně následovaného [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), což je 884 nebo více base 64 znaků (663 nebo více bajtů v binárním formátu), v závislosti na typu podpisu. Binární formát je specifikován v Private Key File.

Offline podpisy jsou podporovány pro RAW, DATAGRAM2 a DATAGRAM3 datagramy, ale ne pro DATAGRAM. Podrobnosti najdete v sekci SESSION CREATE výše a v sekci DATAGRAM2/3 níže.

$host je hostname nebo IP adresa datagram serveru, na který SAM přeposílá datagramy. Pokud není uvedeno, SAM použije IP adresu socketu, který vydal forward příkaz.

$port je číslo portu datagramového serveru, na který bude SAM přeposílat datagramy. Pokud $port není nastaven, datagramy NEBUDOU přeposílány, budou přijímány na řídícím socketu způsobem kompatibilním s v1/v2.

Další zadané možnosti jsou předány do konfigurace I2P relace, pokud nejsou interpretovány SAM mostem (např. outbound.length=0). Tyto možnosti [jsou dokumentovány níže](#tunnel-i2cp-and-streaming-options).

Přeposílané datagramy s možností odpovědi jsou vždy předznačeny base64 destinací, kromě Datagram3, viz níže. Když dorazí datagram s možností odpovědi, bridge odešle na zadaný host:port UDP paket obsahující následující data:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Přeposílané surové datagramy jsou přeposílány beze změny na zadaný host:port bez předpony. UDP paket obsahuje následující data:

```
$datagram_payload
```
Od verze SAM 3.2, když je v SESSION CREATE specifikováno HEADER=true, bude předávaný surový datagram doplněn o hlavičkový řádek následovně:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
$destination je base 64 reprezentace [Destination](/docs/specs/common-structures#type_Destination), což je 516 nebo více base 64 znaků (387 nebo více bajtů v binární podobě), v závislosti na typu podpisu.

#### SAM Anonymní (Raw) Datagramy

Pro maximální využití šířky pásma I2P umožňuje SAM klientům odesílat a přijímat anonymní datagramy, přičemž autentizaci a informace o odpovědích nechává na samotných klientech. Tyto datagramy jsou nespolehlivé a neuspořádané a mohou mít až 32768 bytů.

Minimální velikost je 1. Pro nejlepší spolehlivost doručení je doporučená maximální velikost přibližně 11 KB.

Po navázání SAM session s STYLE=RAW může klient odesílat anonymní datagramy přes SAM bridge přesně stejným způsobem jako [odesílání datagramů s možností odpovědi](#sending-repliable-or-raw-datagrams).

Oba způsoby příjmu datagramů jsou také dostupné pro anonymní datagramy.

Přijaté datagramy jsou zapisovány pomocí SAM na socket, ze kterého byla datagramová relace otevřena, pokud není v příkazu SESSION CREATE specifikován přesměrovací PORT. Toto je způsob přijímání datagramů kompatibilní s v1/v2.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Když mají být anonymní datagramy předány na nějaký host:port, most odešle na specifikovaný host:port zprávu obsahující následující data:

```
$datagram_payload
```
Od SAMv3.2, když je v SESSION CREATE specifikováno HEADER=true, bude přeposílaný surový datagram doplněn o hlavičkový řádek následovně:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Pro alternativní způsob odesílání anonymních datagramů viz [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagram 2/3

Datagram 2/3 jsou nové formáty specifikované na začátku roku 2025. V současnosti neexistují žádné známé implementace. Zkontrolujte dokumentaci implementace pro aktuální stav. Pro více informací viz [specifikace](/docs/specs/datagrams).

V současnosti neexistují plány na zvýšení verze SAM pro indikaci podpory Datagram 2/3. To může být problematické, protože implementace mohou chtít podporovat Datagram 2/3, ale ne funkce SAM v3.3. Jakákoliv změna verze je zatím nerozhodnuta.

Datagram2 i Datagram3 umožňují odpověď. Pouze Datagram2 je autentifikován.

Datagram2 je z pohledu SAMv3 identický s repliable datagramy. Oba jsou autentizované. Liší se pouze I2CP formát a podpis, ale to není viditelné pro SAM klienty. Datagram2 také podporuje offline podpisy, takže může být použit destinacemi s offline podpisem.

Záměrem je, aby Datagram2 nahradil Repliable datagramy pro nové aplikace, které nevyžadují zpětnou kompatibilitu. Datagram2 poskytuje ochranu proti opakovaným útokům (replay protection), která není přítomna u Repliable datagramů. Pokud je vyžadována zpětná kompatibilita, aplikace může podporovat jak Datagram2, tak Repliable ve stejné relaci s SAMv3 PRIMARY sessions.

Datagram3 je odpověditelný, ale není autentizovaný. Pole 'from' ve formátu I2CP je hash, ne destination. $destination jak je odesláno ze SAM serveru klientovi bude 44-bytový base64 hash. Pro převod na úplnou destination pro odpověď jej dekódujte z base64 na 32 bytů binárně, pak jej zakódujte pomocí base32 na 52 znaků a připojte ".b32.i2p" pro NAMING LOOKUP. Jako obvykle by si klienti měli udržovat vlastní cache, aby se vyhnuli opakovaným NAMING LOOKUPům.

Návrháři aplikací by měli postupovat s nejvyšší opatrností a zvážit bezpečnostní důsledky neautentizovaných datagramů.

#### Úvahy o MTU datagramů V3

I2P datagramy mohou být větší než typické internetové MTU 1500. Lokálně odeslané datagramy a přeposílané odpověditelné datagramy s předponou 516+ bajtové base64 destinace pravděpodobně toto MTU překročí. Nicméně localhost MTU na Linux systémech jsou typicky mnohem větší, například 65536. Localhost MTU se liší podle operačního systému. I2P datagramy nikdy nebudou větší než 65536. Velikost datagramu závisí na aplikačním protokolu.

Pokud je SAM klient lokální vůči SAM serveru a systém podporuje větší MTU, pak nebudou datagramy fragmentovány lokálně. Pokud je však SAM klient vzdálený, pak by IPv4 datagramy byly fragmentovány a IPv6 datagramy by selhaly (IPv6 nepodporuje UDP fragmentaci).

Vývojáři klientských knihoven a aplikací by si měli být vědomi těchto problémů a dokumentovat doporučení, jak se vyhnout fragmentaci a zabránit ztrátě paketů, zejména při vzdálených SAM klient-server spojeních.

#### DATAGRAM SEND, RAW SEND (Kompatibilní zpracování datagramů V1/V2)

V SAMv3 je preferovaným způsobem odesílání datagramů použití datagram socketu na portu 7655, jak je zdokumentováno výše. Nicméně odpověditelné datagramy mohou být odesílány přímo přes SAMv3 bridge socket pomocí příkazu DATAGRAM SEND, jak je zdokumentováno v [SAM V1](/docs/api/sam) a [SAM V2](/docs/api/samv2).

Od verze 0.9.14 (verze 3.1) mohou být anonymní datagramy odesílány přímo přes SAM bridge socket pomocí příkazu RAW SEND, jak je zdokumentováno v [SAM V1](/docs/api/sam) a [SAM V2](/docs/api/samv2).

Od verze 0.9.24 (verze 3.2) mohou DATAGRAM SEND a RAW SEND obsahovat parametry FROM_PORT=nnnn a/nebo TO_PORT=nnnn pro přepsání výchozích portů. Od verze 0.9.24 (verze 3.2) může RAW SEND obsahovat parametr PROTOCOL=nnn pro přepsání výchozího protokolu.

Tyto příkazy *nepodporují* parametr ID. Datagramy jsou odesílány do naposledy vytvořené relace typu DATAGRAM nebo RAW, podle potřeby. Podpora parametru ID může být přidána v budoucí verzi.

Formáty DATAGRAM2 a DATAGRAM3 *nejsou* podporovány způsobem kompatibilním s V1/V2.

### SAM PRIMARY Sessions (V3.3 a vyšší)

*Verze 3.3 byla představena v I2P vydání 0.9.25.*

*V dřívější verzi této specifikace byly PRIMARY relace známy jako MASTER relace. V `i2pd` i `I2P+` jsou stále známy pouze jako MASTER relace.*

SAM v3.3 přidává podporu pro provozování streaming, datagramů a raw podsezení na stejném primárním sezení a pro provozování více podsezení stejného stylu. Veškerý provoz podsezení používá jednu destinaci nebo sadu tunelů. Směrování provozu z I2P je založeno na možnostech portu a protokolu pro podsezení.

Pro vytvoření multiplexovaných podsezení musíte vytvořit primární sezení a poté přidat podsezení k primárnímu sezení. Každé podsezení musí mít jedinečné id a jedinečný protokol a port pro naslouchání. Podsezení mohou být také odstraněna z primárního sezení.

S PRIMARY session a kombinací subsessions může SAM klient podporovat více aplikací, nebo jednu sofistikovanou aplikaci používající různé protokoly, na jediné sadě tunnelů. Například bittorrent klient by mohl nastavit streaming subsession pro peer-to-peer spojení, společně s datagram a raw subsessions pro DHT komunikaci.

#### Vytvoření PRIMARY Session

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
SAM bridge odpoví úspěchem nebo selháním jako v [odpovědi na standardní SESSION CREATE](#session-creation-response).

Nenastavujte PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL ani HEADER možnosti na primární relaci. Nesmíte odesílat žádná data na PRIMARY session ID nebo na řídící socket. Všechny příkazy jako STREAM CONNECT, DATAGRAM SEND atd. musí používat subsession ID na samostatném socketu.

PRIMÁRNÍ relace se připojuje k routeru a buduje tunely. Když SAM bridge odpoví, tunely byly vybudovány a relace je připravena pro přidání podrelací. Všechny [I2CP](/docs/protocol/i2cp) možnosti týkající se parametrů tunelů, jako je délka, množství a přezdívka, musí být poskytnuty v SESSION CREATE primární relace.

Všechny utility příkazy jsou podporovány v primární relaci.

Když je primární relace uzavřena, všechny podrelace se také uzavřou.

POZNÁMKA: Před verzí 0.9.47 použijte STYLE=MASTER. STYLE=PRIMARY je podporováno od verze 0.9.47. MASTER je stále podporováno kvůli zpětné kompatibilitě.

#### Vytvoření subsession

Použitím stejného kontrolního socketu, na kterém byla vytvořena PRIMARY session:

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
SAM bridge odpoví úspěchem nebo neúspěchem jako v [odpovědi na standardní SESSION CREATE](#session-creation-response). Protože tunnely byly již vybudovány v primárním SESSION CREATE, SAM bridge by měl odpovědět okamžitě.

Nenastavujte možnost DESTINATION u SESSION ADD. Podsezení bude používat cíl specifikovaný v primárním sezení. Všechna podsezení musí být přidána na řídicím socketu, tj. na stejném připojení, na kterém jste vytvořili primární sezení.

Více subsezení musí mít dostatečně jedinečné možnosti, aby mohla být příchozí data správně směrována. Zejména více sezení stejného stylu musí mít různé možnosti LISTEN_PORT (a/nebo LISTEN_PROTOCOL pouze pro RAW). SESSION ADD s naslouchacím portem a protokolem, který duplikuje existující subsezení, bude mít za následek chybu.

LISTEN_PORT je místní I2P port, tj. přijímací (TO) port pro příchozí data. Pokud není LISTEN_PORT specifikován, bude použita hodnota FROM_PORT. Pokud nejsou specifikovány LISTEN_PORT ani FROM_PORT, příchozí směrování bude založeno pouze na STYLE a PROTOCOL. Pro LISTEN_PORT a LISTEN_PROTOCOL znamená 0 jakoukoli hodnotu, tj. zástupný znak. Pokud jsou LISTEN_PORT i LISTEN_PROTOCOL 0, tato subsession bude výchozí pro příchozí provoz, který není směrován do jiné subsession. Příchozí streaming provoz (protokol 6) nebude nikdy směrován do RAW subsession, ani když je její LISTEN_PROTOCOL 0. RAW subsession nesmí nastavit LISTEN_PROTOCOL na 6. Pokud neexistuje výchozí nebo subsession odpovídající protokolu a portu příchozího provozu, tato data budou zahozena.

Použijte ID subsession, nikoli primární ID session, pro odesílání a přijímání dat. Všechny příkazy jako STREAM CONNECT, DATAGRAM SEND atd. musí používat ID subsession.

Všechny utility příkazy jsou podporovány na primární relaci nebo podrelaci. Odesílání/přijímání datagram/raw v1/v2 není podporováno na primární relaci ani na podrelacích.

#### Zastavení podsezení

Použitím stejného kontrolního socketu, na kterém byla vytvořena PRIMARY relace:

```
->  SESSION REMOVE
          ID=$nickname
```
Toto odebere subsession z primární session. Nenastavujte žádné další možnosti při SESSION REMOVE. Subsessions musí být odstraněny na řídicím socketu, tj. na stejném připojení, na kterém jste vytvořili primární session. Po odstranění subsession je uzavřena a nesmí být použita k odesílání nebo přijímání dat.

SAM bridge odpoví úspěchem nebo neúspěchem stejně jako v [odpovědi na standardní SESSION CREATE](#session-creation-response).

### Příkazy SAM Utility

Některé pomocné příkazy vyžadují již existující relaci a některé ne. Podrobnosti viz níže.

#### Vyhledání názvu hostitele

Následující zprávu může klient použít k dotázání se SAM bridge na rozlišení názvu:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
na kterou je odpovězeno pomocí

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
Hodnota RESULT může být jedna z:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Pokud NAME=ME, pak odpověď bude obsahovat destinaci používanou aktuální relací (užitečné, pokud používáte TRANSIENT destinaci). Pokud $result není OK, MESSAGE může obsahovat popisnou zprávu, jako například "bad format" apod. INVALID_KEY znamená, že něco není v pořádku s $name v požadavku, možná neplatné znaky.

$destination je base 64 reprezentace [Destination](/docs/specs/common-structures#type_Destination), která má 516 nebo více base 64 znaků (387 nebo více bajtů v binární podobě), v závislosti na typu podpisu.

NAMING LOOKUP nevyžaduje, aby byla nejprve vytvořena relace. Nicméně v některých implementacích může vyhledávání .b32.i2p, které není v cache a vyžaduje síťový dotaz, selhat, protože pro vyhledávání nejsou k dispozici žádné klientské tunnely.

#### Možnosti vyhledávání názvů

NAMING LOOKUP je od router API 0.9.66 rozšířeno o podporu service lookups. Podpora se může lišit podle implementace. Další informace naleznete v návrhu 167.

NAMING LOOKUP NAME=example.i2p OPTIONS=true požaduje mapování možností v odpovědi. NAME může být úplná base64 destinace když OPTIONS=true.

Pokud bylo vyhledání cíle úspěšné a v leaseSet byly přítomny volby, pak v odpovědi, následující po cíli, bude jedna nebo více voleb ve formátu OPTION:key=value. Každá volba bude mít samostatnou předponu OPTION:. Budou zahrnuty všechny volby z leaseSet, nejen volby service record. Například mohou být přítomny volby pro parametry definované v budoucnu. Příklad:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Klíče obsahující '=' a klíče nebo hodnoty obsahující nový řádek jsou považovány za neplatné a pár klíč/hodnota bude odstraněn z odpovědi. Pokud v leaseSetu nejsou nalezeny žádné možnosti, nebo pokud leaseSet byl verze 1, pak odpověď nebude obsahovat žádné možnosti. Pokud bylo v dotazu uvedeno OPTIONS=true a leaseSet není nalezen, bude vrácena nová výsledná hodnota LEASESET_NOT_FOUND.

#### Generování klíčů destinace

Veřejné a soukromé base64 klíče lze vygenerovat pomocí následující zprávy:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
na což se odpovídá

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
Od verze 3.1 (I2P 0.9.14) je podporován volitelný parametr SIGNATURE_TYPE. Hodnota SIGNATURE_TYPE může být jakýkoliv název (např. ECDSA_SHA256_P256, nerozlišuje velká/malá písmena) nebo číslo (např. 1), které je podporováno [Key Certificates](/docs/specs/common-structures#type_Certificate). Výchozí hodnota je DSA_SHA1, což NENÍ to, co chcete. Pro většinu aplikací prosím specifikujte SIGNATURE_TYPE=7.

$destination je base 64 reprezentace [Destination](/docs/specs/common-structures#type_Destination), což je 516 nebo více base 64 znaků (387 nebo více bytů v binární podobě), v závislosti na typu podpisu.

$privkey je base 64 zřetězení [Destination](/docs/specs/common-structures#type_Destination) následovaného [Private Key](/docs/specs/common-structures#type_PrivateKey) následovaným [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), což je 884 nebo více base 64 znaků (663 nebo více bajtů v binárním formátu), v závislosti na typu podpisu. Binární formát je specifikován v Private Key File.

Poznámky k 256-bytovému binárnímu [Private Key](/docs/specs/common-structures#type_PrivateKey): Toto pole se nepoužívá od verze 0.6 (2005). Implementace SAM mohou v tomto poli odesílat náhodná data nebo samé nuly; nebojte se řetězce AAAA v base 64. Většina aplikací jednoduše uloží řetězec base 64 a vrátí jej v SESSION CREATE v nezměněné podobě, nebo jej dekóduje do binární formy pro uložení a poté znovu zakóduje pro SESSION CREATE. Aplikace však mohou dekódovat base 64, zpracovat binární data podle specifikace PrivateKeyFile, zahodit 256-bytovou část private key a poté ji nahradit 256 byty náhodných dat nebo samými nulami při opětovném kódování pro SESSION CREATE. VŠECHNA ostatní pole ve specifikaci PrivateKeyFile musí být zachována. To by ušetřilo 256 bytů úložného místa v souborovém systému, ale pro většinu aplikací to pravděpodobně nestojí za tu práci. Další informace a pozadí najdete v návrhu 161.

DEST GENERATE nevyžaduje, aby byla nejprve vytvořena relace.

DEST GENERATE nelze použít k vytvoření destinace s offline podpisy.

#### PING/PONG (SAM 3.2 nebo vyšší)

Buď klient nebo server může odeslat:

```
PING[ arbitrary text]
```
na kontrolním portu, s odpovědí:

```
PONG[ arbitrary text from the ping]
```
k použití pro udržování spojení řídicího socketu. Kterákoli strana může ukončit relaci a socket, pokud nedojde odpověď v rozumném čase, závisí na implementaci.

Pokud dojde k timeout při čekání na PONG od klienta, bridge může poslat:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
a poté se odpojit.

Pokud dojde k timeoutu při čekání na PONG z bridge, klient se může jednoduše odpojit.

PING/PONG nevyžadují, aby byla nejprve vytvořena relace.

#### QUIT/STOP/EXIT (SAM 3.2 nebo vyšší, volitelné funkce)

Příkazy QUIT, STOP a EXIT ukončí relaci a socket. Implementace je volitelná, pro snadné testování přes telnet. Zda před uzavřením socketu dojde k nějaké odpovědi (například zpráva SESSION STATUS) je specifické pro implementaci a je mimo rozsah této specifikace.

QUIT/STOP/EXIT nevyžadují, aby byla nejprve vytvořena relace.

#### HELP (volitelná funkce)

Servery mohou implementovat příkaz HELP. Implementace je volitelná, pro snadné testování přes telnet. Formát výstupu a detekce konce výstupu je specifická pro implementaci a je mimo rozsah této specifikace.

HELP nevyžaduje, aby byla nejprve vytvořena relace.

#### Konfigurace autorizace (SAM 3.2 nebo vyšší, volitelná funkce)

Konfigurace autorizace pomocí příkazu AUTH. SAM server může implementovat tyto příkazy pro usnadnění trvalého ukládání přihlašovacích údajů. Konfigurace autentizace jinými způsoby než těmito příkazy je specifická pro danou implementaci a mimo rámec této specifikace.

- AUTH ENABLE povolí autorizaci na následujících připojeních
- AUTH DISABLE zakáže autorizaci na následujících připojeních
- AUTH ADD USER="foo" PASSWORD="bar" přidá uživatele/heslo
- AUTH REMOVE USER="foo" odebere tohoto uživatele

Dvojité uvozovky pro uživatele a heslo jsou doporučené, ale nejsou vyžadované. Dvojité uvozovky uvnitř uživatelského jména nebo hesla musí být escapovány zpětným lomítkem. V případě neúspěchu server odpoví s I2P_ERROR a zprávou.

AUTH nevyžaduje, aby byla nejprve vytvořena relace.

### Hodnoty RESULT

Toto jsou hodnoty, které může obsahovat pole RESULT, s jejich významem:

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
Různé implementace nemusí být konzistentní v tom, který RESULT je vrácen v různých scénářích.

Většina odpovědí s RESULT, jiných než OK, bude také obsahovat MESSAGE s dodatečnými informacemi. MESSAGE bude obecně užitečná při ladění problémů. Nicméně řetězce MESSAGE jsou závislé na implementaci, mohou nebo nemusí být přeloženy SAM serverem do aktuálního locale, mohou obsahovat interní informace specifické pro implementaci, jako jsou výjimky, a mohou se změnit bez předchozího upozornění. Ačkoli SAM klienti se mohou rozhodnout vystavit řetězce MESSAGE uživatelům, neměli by na základě těchto řetězců činit programové rozhodnutí, protože to bude křehké.

### Možnosti tunnel, I2CP a streamingu

Tyto volby mohou být předány jako páry název=hodnota v řádku SAM SESSION CREATE.

Všechny relace mohou obsahovat [I2CP možnosti jako jsou délky a množství tunelů](/docs/protocol/i2cp#options). STREAM relace mohou obsahovat [možnosti knihovny Streaming](/docs/api/streaming#options).

Pro názvy voleb a výchozí hodnoty se podívejte na tyto odkazy. Odkazovaná dokumentace je pro implementaci Java router. Výchozí hodnoty se mohou změnit. Názvy voleb a hodnoty jsou citlivé na velikost písmen. Jiné implementace router nemusí podporovat všechny volby a mohou mít odlišné výchozí hodnoty; podrobnosti najdete v dokumentaci router.

### Poznámky k BASE 64

Kódování Base 64 musí používat standardní I2P Base 64 abecedu "A-Z, a-z, 0-9, -, ~".

### Výchozí nastavení SAM

Výchozí SAMv3 port je 7656. SAM není ve výchozím nastavení povolen v Java I2P routeru; musí být spuštěn ručně nebo nakonfigurován pro automatické spouštění na stránce konfigurace klientů v konzoli routeru nebo v souboru clients.config. Výchozí SAM UDP port je 7655, naslouchající na 127.0.0.1. Tyto hodnoty lze změnit v Java routeru přidáním argumentů sam.udp.port=nnnnn a/nebo sam.udp.host=w.x.y.z do volání nebo na řádek SESSION.

Konfigurace v jiných routerech je specifická pro danou implementaci. Viz [průvodce konfigurací i2pd zde](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).

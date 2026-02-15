---
title: "Specifikace vytváření tunelů"
description: "Specifikace ElGamal tunnel build pro vytváření tunelů pomocí neinteraktivního teleskopování."
slug: "tunnel-creation"
aliases: 
category: "Design"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Přehled

POZNÁMKA: ZASTARALÉ - Toto je specifikace vytváření tunelů ElGamal. Viz [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) pro specifikaci vytváření tunelů X25519.

Tento dokument specifikuje detaily šifrovaných zpráv pro budování tunelů, které se používají k vytváření tunelů pomocí metody "neinteraktivního teleskopování". Viz dokument o budování tunelů [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) pro přehled procesu, včetně metod výběru a uspořádání uzlů.

Vytvoření tunnelu je dosaženo jedinou zprávou předávanou podél cesty peerů v tunnelu, přepsanou na místě a přenášenou zpět k tvůrci tunnelu. Tato jediná zpráva tunnelu se skládá z proměnného počtu záznamů (až 8) - jeden pro každý potenciální peer v tunnelu. Jednotlivé záznamy jsou asymetricky (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) šifrovány tak, aby je mohl přečíst pouze konkrétní peer na cestě, zatímco dodatečná symetrická vrstva šifrování (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) je přidána na každém hopu tak, aby byl asymetricky šifrovaný záznam odhalen pouze v příslušném čase.

### Počet záznamů

Ne všechny záznamy musí obsahovat platná data. Zpráva build pro 3-hop tunnel například může obsahovat více záznamů, aby skryla skutečnou délku tunnelu před účastníky. Existují dva typy build zpráv. Původní Tunnel Build Message ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) obsahuje 8 záznamů, což je více než dostatečné pro jakoukoli praktickou délku tunnelu. Novější Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) obsahuje 1 až 8 záznamů. Původce může vybalancovat velikost zprávy s požadovanou mírou obfuskace délky tunnelu.

V současné síti jsou většina tunnelů dlouhé 2 nebo 3 hopů. Současná implementace používá 5-záznamový VTBM pro budování tunnelů o délce 4 hopy nebo méně a 8-záznamový TBM pro delší tunnely. 5-záznamový VTBM (který se po fragmentaci vejde do tří 1KB tunnel zpráv) snižuje síťový provoz a zvyšuje úspěšnost budování, protože menší zprávy mají menší pravděpodobnost zahození.

Odpověď musí být stejného typu a délky jako zpráva pro sestavení.

### Specifikace záznamu požadavku

Také specifikováno ve specifikaci I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

Nešifrovaný text záznamu, viditelný pouze pro dotazovaný hop:

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
Pole next tunnel ID a next router identity hash se používají k určení dalšího skoku v tunnel, ačkoli pro koncový bod odchozího tunnel určují, kam má být odeslána přepsaná zpráva odpovědi na vytvoření tunnel. Kromě toho next message ID určuje ID zprávy, které má zpráva (nebo odpověď) použít.

Klíč tunnel vrstvy, klíč tunnel IV, odpovědní klíč a odpovědní IV jsou každý náhodné 32-bajtové hodnoty vygenerované tvůrcem pro použití pouze v tomto záznamu požadavku na sestavení.

Pole flags obsahuje následující (pořadí bitů: 76543210, bit 7 je MSB):

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
Bit 7 označuje, že hop bude inbound gateway (IBGW). Bit 6 označuje, že hop bude outbound endpoint (OBEP). Pokud není nastaven ani jeden bit, hop bude intermediate participant. Oba nemohou být nastaveny současně.

#### Vytvoření záznamu požadavku

Každý hop dostane náhodné Tunnel ID, nenulové. Aktuální a další-hop Tunnel ID jsou vyplněny. Každý záznam dostane náhodný tunnel IV klíč, reply IV, layer klíč a reply klíč.

#### Šifrování záznamu požadavku

Tento čistý textový záznam je ElGamal 2048 šifrován [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) s veřejným šifrovacím klíčem skoku a formátován do 528 bajtového záznamu:

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
V 512-bytovém šifrovaném záznamu obsahují ElGamal data byty 1-256 a 258-513 ze 514-bytového ElGamal šifrovaného bloku [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Dva padding byty z bloku (nulové byty na pozicích 0 a 257) jsou odstraněny.

Protože cleartext využívá celé pole, není potřeba dalšího doplňování kromě `SHA256(cleartext) + cleartext`.

Každý 528-bajtový záznam je pak iterativně šifrován (pomocí AES dešifrování, s reply key a reply IV pro každý hop), takže identita routeru bude v nešifrované podobě pouze pro příslušný hop.

### Zpracování a šifrování skoků

Když hop obdrží TunnelBuildMessage, prohledá záznamy v něm obsažené a hledá ten, který začíná jeho vlastním hash identity (zkrácený na 16 bajtů). Poté dešifruje ElGamal blok z daného záznamu a získá chráněný cleartext. V tomto okamžiku se ujistí, že požadavek na tunnel není duplikát tím, že vloží AES-256 reply klíč do Bloom filtru. Duplikáty nebo neplatné požadavky jsou zahozeny. Záznamy, které nejsou označeny aktuální hodinou nebo předchozí hodinou (pokud je krátce po začátku hodiny), musí být zahozeny. Například vezměte hodinu z časové značky, převeďte na úplný čas, a pokud je více než 65 minut pozadu nebo 5 minut napřed oproti aktuálnímu času, je neplatný. Bloom filtr musí mít trvání nejméně jednu hodinu (plus několik minut pro umožnění časového posunu), aby duplicitní záznamy v aktuální hodině, které nejsou odmítnuty kontrolou časové značky hodiny v záznamu, byly odmítnuty filtrem.

Po rozhodnutí, zda souhlasí s účastí v tunnel nebo ne, nahradí záznam, který obsahoval požadavek, šifrovaným blokem odpovědi. Všechny ostatní záznamy jsou šifrovány AES-256 [CRYPTO-AES](/docs/specs/cryptography/#aes) s přiloženým klíčem odpovědi a IV. Každý je šifrován AES/CBC samostatně se stejným klíčem odpovědi a IV odpovědi. Režim CBC nepokračuje (není zřetězen) napříč záznamy.

Každý hop zná pouze svou vlastní odpověď. Pokud souhlasí, bude tunnel udržovat až do vypršení platnosti, i když nebude používán, protože nemůže vědět, zda všechny ostatní hopy souhlasily.

#### Specifikace Reply Record

Poté, co současný hop přečte svůj záznam, nahradí jej odpovědním záznamem uvádějícím, zda souhlasí nebo nesouhlasí s účastí v tunnelu, a pokud nesouhlasí, klasifikují svůj důvod odmítnutí. Jedná se jednoduše o hodnotu 1 byte, kde 0x0 znamená, že souhlasí s účastí v tunnelu, a vyšší hodnoty znamenají vyšší úrovně odmítnutí.

Následující kódy odmítnutí jsou definovány:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

Aby se před partnery skryly jiné příčiny, jako je vypnutí routeru, současná implementace používá TUNNEL_REJECT_BANDWIDTH pro téměř všechna odmítnutí.

Odpověď je zašifrována pomocí AES session key doručeného v zašifrovaném bloku, doplněna 495 bajty náhodných dat pro dosažení plné velikosti záznamu. Výplň je umístěna před stavový bajt:

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
Toto je také popsáno v I2NP specifikaci [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

### Příprava zprávy pro stavbu tunnel

Při vytváření nové Tunnel Build Message musí být nejprve sestaveny všechny Build Request Records a asymetricky zašifrovány pomocí ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Každý záznam je poté preventivně dešifrován pomocí reply klíčů a IV hodnot hopů dříve v cestě, pomocí AES [CRYPTO-AES](/docs/specs/cryptography/#aes). Tato dešifrace by měla být spuštěna v opačném pořadí, aby se asymetricky zašifrovaná data objevila v plaintextu ve správném hopu poté, co je jejich předchůdce zašifruje.

Přebytečné záznamy, které nejsou potřebné pro jednotlivé požadavky, jsou jednoduše vyplněny náhodnými daty tvůrcem.

### Doručování zpráv pro vybudování tunelu

U odchozích tunelů se doručení provádí přímo z tunnel creatoru na první hop, kdy se TunnelBuildMessage zabalí, jako kdyby creator byl jen dalším hopem v tunelu. U příchozích tunelů se doručení provádí prostřednictvím existujícího odchozího tunelu. Odchozí tunel je obecně ze stejného poolu jako nový tunel, který se buduje. Pokud v tomto poolu není dostupný žádný odchozí tunel, použije se odchozí exploratory tunel. Při spuštění, když ještě neexistuje žádný odchozí exploratory tunel, se použije falešný 0-hop odchozí tunel.

### Zpracování koncových bodů zpráv pro stavbu tunelů

Pro vytvoření odchozího tunelu, když požadavek dosáhne odchozího koncového bodu (jak je určeno příznakem 'povolit zprávy komukoliv'), je hop zpracován jako obvykle, šifruje odpověď na místo záznamu a šifruje všechny ostatní záznamy, ale protože neexistuje žádný 'další hop', na který by se TunnelBuildMessage předala dál, místo toho umístí zašifrované záznamy odpovědi do TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) nebo VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) (typ zprávy a počet záznamů musí odpovídat požadavku) a doručí ji do odpovědního tunelu specifikovaného v záznamu požadavku. Tento odpovědní tunel předá Tunnel Build Reply Message zpět tvůrci tunelu, stejně jako u jakékoliv jiné zprávy [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). Tvůrce tunelu ji poté zpracuje, jak je popsáno níže.

Reply tunnel byl vybrán tvůrcem následovně: Obecně se jedná o příchozí tunnel ze stejného poolu jako nový odchozí tunnel, který se buduje. Pokud v daném poolu není dostupný žádný příchozí tunnel, použije se příchozí exploratory tunnel. Při spuštění, když ještě neexistuje žádný příchozí exploratory tunnel, použije se falešný 0-hop příchozí tunnel.

Pro vytvoření inbound tunnelu, když požadavek dosáhne inbound koncového bodu (také známého jako tvůrce tunnelu), není potřeba generovat explicitní Tunnel Build Reply Message a router zpracovává každou z odpovědí, jak je uvedeno níže.

### Zpracování zprávy odpovědi na sestavení tunelu

Pro zpracování odpovědních záznamů musí tvůrce jednoduše AES dešifrovat každý záznam jednotlivě, pomocí odpovědního klíče a IV každého uzlu v tunelu za daným uzlem (v opačném pořadí). Tím se odhalí odpověď specifikující, zda souhlasí s účastí v tunelu nebo proč odmítají. Pokud všichni souhlasí, tunnel je považován za vytvořený a může být okamžitě použit, ale pokud někdo odmítne, tunnel je zahozen.

Dohody a odmítnutí jsou zaznamenány v profilu každého peer [PEER-SELECTION](/docs/overview/tunnel-routing/), aby mohly být použity v budoucích hodnoceních kapacity tunnel peer.

## Historie a poznámky

Tato strategie vznikla během diskuse na I2P mailing listu mezi Michaelem Rogersem, Matthewem Toselandem (toad) a jrandomem ohledně predecessor útoku. Viz TUNBUILD-SUMMARY, TUNBUILD-REASONING. Byla představena ve vydání 0.6.1.10 dne 16. února 2006, což bylo naposledy, kdy byla v I2P provedena změna nekompatibilní se zpětnou kompatibilitou.

Poznámky:

- Tento návrh nebrání dvěma nepřátelským peerům uvnitř tunelu označit jeden nebo více záznamů požadavků nebo odpovědí za účelem detekce, že se nacházejí ve stejném tunelu, ale takové jednání může být detekováno tvůrcem tunelu při čtení odpovědi, což způsobí označení tunelu jako neplatného.
- Tento návrh neobsahuje proof of work na asymetricky šifrované sekci, ačkoliv 16 bajtový hash identity by mohl být zkrácen na polovinu s tou druhou částí nahrazenou hashcash funkcí s náklady až 2^64.
- Tento návrh sám o sobě nebrání dvěma nepřátelským peerům uvnitř tunelu použít informace o časování k určení, zda se nacházejí ve stejném tunelu. Použití dávkového a synchronizovaného doručování požadavků by mohlo pomoci (seskupení požadavků a jejich odeslání na (ntp-synchronizovanou) minutu). Nicméně takový postup umožňuje peerům 'označit' požadavky jejich zpožděním a detekováním zpoždění později v tunelu, ačkoliv možná by fungovalo zahazování požadavků nedoručených v malém časovém okně (i když by to vyžadovalo vysoký stupeň synchronizace hodin). Alternativně by možná jednotlivé skoky mohly vložit náhodné zpoždění před přeposláním požadavku?
- Existují nějaké nefatální metody označování požadavku?
- Časové razítko s hodinovým rozlišením se používá pro prevenci replay útoků. Toto omezení nebylo vynucováno až do vydání 0.9.16.

## Budoucí práce

- V současné implementaci zanechává původce jeden záznam prázdný pro sebe. Zpráva s n záznamy tak může postavit pouze tunnel o n-1 hopech. Toto se zdá být nezbytné pro příchozí tunnely (kde předposlední hop může vidět hash prefix pro následující hop), ale ne pro odchozí tunnely. Toto je třeba prozkoumat a ověřit. Pokud je možné použít zbývající záznam bez kompromitování anonymity, měli bychom tak učinit.
- Další analýza možných útoků označováním a časováním popsaných ve výše uvedených poznámkách.
- Používat pouze VTBM; nevybírat staré uzly, které ji nepodporují.
- Build Request Record nespecifikuje životnost tunnelu nebo vypršení; každý hop ukončuje tunnel po 10 minutách, což je síťově hardkódovaná konstanta. Mohli bychom použít bit v poli flag a vzít 4 (nebo 8) bajtů z paddingu pro specifikaci životnosti nebo vypršení. Žadatel by tuto možnost specifikoval pouze tehdy, pokud by ji všichni účastníci podporovali.

## Reference

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - Specifikace BuildRequestRecord
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - AES šifrování
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - ElGamal šifrování
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- TUNBUILD-REASONING
- TUNBUILD-SUMMARY
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage

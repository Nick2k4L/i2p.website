---
title: "UDP Trackery"
description: "Specifikace protokolu pro UDP BitTorrent oznámení v I2P"
slug: "udp-announces"
category: "Protokoly"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Přehled

Tato specifikace dokumentuje protokol pro UDP bittorrent oznámení v I2P. Pro celkovou specifikaci bittorrentu v I2P viz [BitTorrent over I2P](/docs/applications/bittorrent). Pro pozadí a další informace o vývoji této specifikace viz [Proposal 160](/proposals/160-udp-trackers).

## Návrh

Tento návrh používá repliable datagram2, repliable datagram3 a raw datagramy, jak jsou definovány v [Datagrams](/docs/specs/datagrams). Datagram2 a Datagram3 jsou nové varianty repliable datagramů, definované v [Proposal 163](/proposals/163-datagram2-datagram3). Datagram2 přidává odolnost proti replay útokům a podporu offline podpisů. Datagram3 je menší než starý formát datagramu, ale bez autentizace.

### BEP 15

Pro referenci, tok zpráv definovaný v [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) je následující:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
Fáze připojení je vyžadována pro zabránění podvrhování IP adres. Tracker vrací ID připojení, které klient používá v následných oznámeních. Toto ID připojení vyprší ve výchozím nastavení za jednu minutu u klienta a za dvě minuty u trackeru.

I2P bude používat stejný tok zpráv jako BEP 15, pro snadné přijetí v existujících klientských kódových základnách podporujících UDP: pro efektivitu a z bezpečnostních důvodů popsaných níže:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
To potenciálně poskytuje významné úspory šířky pásma oproti streamovacím (TCP) oznámením. Zatímco Datagram2 má přibližně stejnou velikost jako streamovací SYN, raw odpověď je mnohem menší než streamovací SYN ACK. Následné požadavky používají Datagram3 a následné odpovědi jsou raw.

Požadavky na oznámení jsou Datagram3, takže tracker nemusí udržovat velkou mapovací tabulku ID připojení k cíli oznámení nebo hash. Místo toho může tracker generovat ID připojení kryptograficky z hash odesílatele, aktuálního časového razítka (založeného na nějakém intervalu) a tajné hodnoty. Když je přijat požadavek na oznámení, tracker ověří ID připojení a poté použije hash odesílatele Datagram3 jako cíl odesílání.

### Životnost připojení

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) specifikuje, že ID připojení vyprší za jednu minutu u klienta a za dvě minuty u trackeru. Nelze to konfigurovat. To omezuje potenciální zisky efektivity, pokud klienti nesdruží oznámení tak, aby je všechna provedli v rámci jednominutového okna. i2psnark aktuálně oznámení nesdružuje; rozkládá je v čase, aby se vyhnul nárazům provozu. Uživatelé pokročilých funkcí údajně provozují tisíce torrentů najednou a soustředit tolik oznámení do jedné minuty není realistické.

Zde navrhujeme rozšířit odpověď připojení o volitelné pole životnosti spojení. Výchozí hodnota, pokud není uvedena, je jedna minuta. Jinak se použije životnost specifikovaná v sekundách klientem a tracker bude udržovat ID spojení o jednu minutu déle.

### Kompatibilita s BEP 15

Tento návrh zachovává kompatibilitu s [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) co nejvíce, aby omezil změny potřebné v existujících klientech a trackerech.

Jedinou požadovanou změnou je formát informací o peerech v announce odpovědi. Přidání pole lifetime v connect odpovědi není vyžadováno, ale je silně doporučeno z důvodu efektivity, jak bylo vysvětleno výše.

### Analýza bezpečnosti

Důležitým cílem UDP announce protokolu je zabránit falšování adres. Klient musí skutečně existovat a obsahovat skutečný leaseSet. Musí mít příchozí tunely pro příjem Connect Response. Tyto tunely by mohly mít nulový počet hopů a být vybudovány okamžitě, ale to by odhalilo tvůrce. Tento protokol tohoto cíle dosahuje.

### Problémy

- Tento protokol nepodporuje skryté destinace, ale může být rozšířen, aby tak činil. Viz níže.

## Specifikace

### Protokoly a porty

Repliable Datagram2 používá I2CP protokol 19; repliable Datagram3 používá I2CP protokol 20; surové datagramy používají I2CP protokol 18. Požadavky mohou být Datagram2 nebo Datagram3. Odpovědi jsou vždy surové. Starší formát repliable datagram ("Datagram1") používající I2CP protokol 17 NESMÍ být použit pro požadavky nebo odpovědi; tyto musí být zahozeny, pokud jsou přijaty na portech pro požadavky/odpovědi. Všimněte si, že Datagram1 protokol 17 se stále používá pro DHT protokol.

Požadavky používají I2CP "to port" z announce URL; viz níže. "From port" požadavku je volený klientem, ale měl by být nenulový a odlišný od portů používaných DHT, aby mohly být odpovědi snadno klasifikovány. Trackery by měly odmítnout požadavky přijaté na nesprávném portu.

Odpovědi používají I2CP "to port" z požadavku. "From port" požadavku je "to port" z požadavku.

### Adresa oznámení

Formát announce URL není specifikován v [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), ale stejně jako v clearnet, UDP announce URL mají formu `udp://host:port/path`. Cesta je ignorována a může být prázdná, ale na clearnet je typicky `/announce`. Část `:port` by měla být vždy přítomna, nicméně pokud je část `:port` vynechána, použije se výchozí I2CP port 6969, protože to je běžný port na clearnet. Mohou být také připojeny cgi parametry `&a=b&c=d`, ty mohou být zpracovány a poskytnuty v announce požadavku, viz [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). Pokud nejsou žádné parametry nebo cesta, může být také vynecháno koncové `/`, jak je naznačeno v [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

### Formáty datagramů

Všechny hodnoty jsou odesílány v síťovém pořadí bajtů (big endian). Neočekávejte, že pakety budou mít přesně určitou velikost. Budoucí rozšíření by mohla zvětšit velikost paketů.

#### Požadavek na připojení

Klient na tracker. 16 bajtů. Musí být odpověditelný Datagram2. Stejné jako v [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Žádné změny.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### Odpověď na připojení

Tracker ke klientovi. 16 nebo 18 bajtů. Musí být raw. Stejné jako v [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) kromě níže uvedených poznámek.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Odpověď MUSÍ být odeslána na I2CP "to port", který byl přijat jako "from port" požadavku.

Pole lifetime je volitelné a udává dobu života connection_id klienta v sekundách. Výchozí hodnota je 60 a minimální hodnota, pokud je specifikována, je 60. Maximum je 65535 neboli přibližně 18 hodin. Tracker by měl udržovat connection_id po dobu 60 sekund déle než je doba života klienta.

#### Žádost o oznámení

Klient k trackeru. Minimálně 98 bajtů. Musí být odpověditelný Datagram3. Stejné jako v [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) kromě níže uvedených poznámek.

connection_id je takové, jaké bylo přijato v odpovědi na připojení.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
Změny oproti [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- klíč je ignorován
- IP adresa se nepoužívá
- port je pravděpodobně ignorován, ale musí být stejný jako I2CP from port
- Sekce options, pokud je přítomna, je definována v [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

Odpověď MUSÍ být odeslána na I2CP "to port", který byl přijat jako "from port" požadavku. Nepoužívejte port z announce požadavku.

#### Odpověď na oznámení

Tracker ke klientovi. Minimálně 20 bajtů. Musí být nezpracované. Stejné jako v [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) kromě níže uvedených poznámek.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Změny oproti [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- Místo 6-bajtových IPv4+port nebo 18-bajtových IPv6+port vracíme násobky 32-bajtových "kompaktních odpovědí" s binárními SHA-256 hashy peerů. Stejně jako u TCP kompaktních odpovědí nezahrnujeme port.

Odpověď MUSÍ být odeslána na I2CP "to port", který byl přijat jako "from port" požadavku. Nepoužívejte port z announce požadavku.

I2P datagramy mají velmi velkou maximální velikost přibližně 64 KB; nicméně pro spolehlivé doručení by se mělo vyhnout datagramům větším než 4 KB. Z důvodu efektivity šířky pásma by trackery pravděpobně měly omezit maximální počet peerů na přibližně 50, což odpovídá přibližně 1600 bajtovému paketu před režií na různých vrstvách a mělo by to být v rámci limitu užitečného zatížení dvou tunnel zpráv po fragmentaci.

Stejně jako v BEP 15, není zahrnut počet adres peerů (IP/port pro BEP 15, zde hashe), které následují. Ačkoliv to není v BEP 15 uvažováno, mohl by být definován značkovač konce peerů ze samých nul, který by indikoval, že informace o peerech jsou kompletní a následují nějaká rozšiřující data.

Aby bylo možné rozšíření v budoucnosti, klienti by měli ignorovat 32-bajtový hash sestávající ze samých nul a veškerá data, která následují. Trackery by měly odmítat oznámení od hashe ze samých nul, ačkoli tento hash je již zakázán Java routery.

#### Scrape

Scrape požadavek/odpověď z [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) není vyžadován touto specifikací, ale může být implementován podle potřeby, bez nutnosti změn. Klient musí nejprve získat connection ID. Scrape požadavek je vždy repliable Datagram3. Scrape odpověď je vždy raw.

#### Chybová odpověď

Tracker ke klientovi. Minimálně 8 bajtů (pokud je zpráva prázdná). Musí být raw. Stejné jako v [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Bez změn.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## Rozšíření

Rozšiřující bity nebo pole verze nejsou zahrnuty. Klienti a trackery by neměli předpokládat, že pakety mají určitou velikost. Tímto způsobem lze přidat další pole bez narušení kompatibility. Pokud je to potřeba, doporučuje se formát rozšíření definovaný v [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

Odpověď na připojení je upravena o přidání volitelné životnosti ID připojení.

Pokud je vyžadována podpora blinded destination, můžeme buď přidat blinded 35-bajtovou adresu na konec announce požadavku, nebo požadovat blinded hashe v odpovědích, pomocí formátu [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) (parametry TBD). Sada blinded 35-bajtových peer adres by mohla být přidána na konec announce odpovědi, za hash o délce 32 bajtů složený ze samých nul.

## Pokyny pro implementaci

Viz sekci o návrhu výše pro diskusi o výzvách pro neintegrované, non-I2CP klienty a trackery.

### Klienti

Pro daný hostname trackeru by měl klient upřednostňovat UDP před HTTP URL a neměl by oznámit oběma.

Klienti s existující podporou BEP 15 by měli vyžadovat pouze malé úpravy.

Pokud klient podporuje DHT nebo jiné datagram protokoly, měl by pravděpodobně zvolit jiný port jako "zdrojový port" požadavku, aby se odpovědi vrátily na tento port a nezmíchaly se s DHT zprávami. Klient přijímá jako odpovědi pouze surové datagramy. Trackery nikdy neodešlou klientovi odpověditelný datagram2.

Klienti s výchozím seznamem opentrackerů by měli aktualizovat seznam a přidat UDP URL poté, co se zjistí, že známé opentrackery podporují UDP.

Klienti mohou, ale nemusí implementovat opětovné odesílání požadavků. Opětovná odesílání, pokud jsou implementována, by měla používat počáteční timeout alespoň 15 sekund a zdvojnásobovat timeout pro každé opětovné odesílání (exponenciální backoff).

Klienti se musí stáhnout po obdržení chybové odpovědi.

### Trackery

Trackery s existující podporou BEP 15 by měly vyžadovat pouze malé úpravy. Tato specifikace se liší od návrhu z roku 2014 v tom, že tracker musí podporovat příjem repliable datagram2 a datagram3 na stejném portu.

Pro minimalizaci požadavků na zdroje trackeru je tento protokol navržen tak, aby eliminoval jakékoli požadavky na to, aby tracker ukládal mapování hash hodnot klientů na ID připojení pro pozdější ověření. To je možné, protože paket announce request je odpověditelný Datagram3 paket, takže obsahuje hash odesílatele.

Doporučená implementace je:

- Definujte aktuální epochu jako aktuální čas s rozlišením životnosti spojení, `epoch = now / lifetime`.
- Definujte kryptografickou hash funkci `H(secret, clienthash, epoch)`, která generuje 8bajtový výstup.
- Vygenerujte náhodnou konstantu secret používanou pro všechna spojení.
- Pro odpovědi na připojení vygenerujte `connection_id = H(secret, clienthash, epoch)`
- Pro announce požadavky validujte přijaté connection ID v aktuální epoše ověřením `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## Reference

- **[BEP15]** [BEP 15 - UDP Tracker Protocol](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - UDP Tracker Protocol Extensions](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Specifikace datagramů](/docs/specs/datagrams)
- **[Prop160]** [Návrh 160 - UDP Trackery](/proposals/160-udp-trackers)
- **[Prop163]** [Návrh 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [SAMv3 API](/docs/api/samv3)
- **[SPEC]** [BitTorrent přes I2P](/docs/applications/bittorrent)

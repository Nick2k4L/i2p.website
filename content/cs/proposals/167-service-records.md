---
title: "Záznamy služeb v LS2"
number: "167"
author: "zzz, orignal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Zavřeno"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## Stav
Schváleno při druhém přezkoumání dne 2025-04-01; specifikace byly aktualizovány; zatím neimplementováno.


## Přehled

I2P nemá centralizovaný systém DNS.  
Nicméně, adresář spolu se systémem doménových jmen b32 umožňuje směrovači vyhledat úplné cíle a stáhnout lease sety, které obsahují seznam bran a klíčů, aby se klienti mohli k tomuto cíli připojit.

Lease sety jsou tedy něčím podobné záznamům DNS. V současnosti však neexistuje žádný způsob, jak zjistit, zda daný hostitel podporuje nějaké služby, a to buď na tomto cíli, nebo na jiném, podobně jako záznamy DNS [SRV](https://en.wikipedia.org/wiki/SRV_record) definované v [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782).

První aplikací tohoto může být e-mail peer-to-peer.  
Další možné aplikace: DNS, GNS, servery klíčů, certifikační autority, časové servery, bittorrent, kryptoměny, další aplikace peer-to-peer.


## Související návrhy a alternativy

### Seznamy služeb

LS2 [Návrh 123](/proposals/123-new-netdb-entries/) definoval „záznamy služeb“, které označovaly, že cíl se účastní globální služby. Floodfill uzly by tyto záznamy agregovaly do globálních „seznamů služeb“.  
Toto nebylo nikdy implementováno kvůli složitosti, absenci autentizace, bezpečnostním rizikům a obavám z spamování.

Tento návrh se liší tím, že poskytuje vyhledávání služby pro konkrétní cíl, nikoli globální fond cílů pro nějakou globální službu.

### GNS

GNS navrhuje, aby každý uživatel provozoval vlastní DNS server.  
Tento návrh je doplňkový, protože bychom mohli použít záznamy služeb k určení, že GNS (nebo DNS) je podporováno, se standardním názvem služby „domain“ na portu 53.

### Dot well-known

Bylo [navrženo](http://i2pforum.i2p/viewtopic.php?p=3102), že služby by měly být vyhledávány prostřednictvím HTTP požadavku na /.well-known/i2pmail.key. To vyžaduje, aby každá služba měla přidruženou webovou stránku, která bude hostovat klíč. Většina uživatelů weby neprovozuje.

Jednou z možných cest je předpokládat, že služba pro adresu b32 běží ve skutečnosti na této adrese b32. Takže vyhledání služby pro example.i2p vyžaduje HTTP stahování z http://example.i2p/.well-known/i2pmail.key, ale služba pro aaa...aaa.b32.i2p tento dotaz nepotřebuje, může se připojit přímo.

Existuje však nejednoznačnost, protože example.i2p lze adresovat také pomocí své adresy b32.

### MX záznamy

Záznamy SRV jsou jednoduše obecnou verzí MX záznamů pro jakoukoli službu.  
„_smtp._tcp“ je „MX“ záznam.  
Pokud máme záznamy SRV, nejsou MX záznamy potřeba, a samotné MX záznamy neposkytují obecný záznam pro jakoukoli službu.


## Návrh

Záznamy služeb jsou umístěny v sekci možností v [LS2](/docs/specs/common-structures/).  
Sekce možností LS2 je aktuálně nepoužívaná.  
Není podporováno pro LS1.  
Toto je podobné [návrhu šířky pásma tunelu](/proposals/168-tunnel-bandwidth/), který definuje možnosti pro záznamy sestavení tunelu.

Pro vyhledání adresy služby pro konkrétní doménu nebo b32 směrovač stáhne leaseset a vyhledá záznam služby vlastností.

Služba může být hostována na stejném cíli jako samotný LS, nebo může odkazovat na jinou doménu/b32.

Pokud je cílový cíl služby jiný, musí cílový LS také obsahovat záznam služby, který odkazuje sám na sebe a indikuje, že tuto službu podporuje.

Návrh nevyžaduje speciální podporu, ukládání do mezipaměti ani změny ve floodfillech.  
Tyto změny musí podporovat pouze vydavatel leasesetu a klient vyhledávající záznam služby.

Navrženy jsou drobné rozšíření I2CP a SAM pro usnadnění načítání záznamů služeb klienty.



## Specifikace

### Specifikace možnosti LS2

Možnosti LS2 MUSÍ být seřazeny podle klíče, aby byl podpis invariantní.

Definováno následovně:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Symbolický název požadované služby. Musí být malými písmeny. Příklad: „smtp“.  
  Povolené znaky jsou [a-z0-9-] a nesmí začínat ani končit pomlčkou.
  Pokud jsou definovány, musí být použity standardní identifikátory z [registru typů služeb DNS-SD](http://www.dns-sd.org/ServiceTypes.html) nebo Linux /etc/services.
- proto := Transportní protokol požadované služby. Musí být malými písmeny, buď „tcp“ nebo „udp“.  
  „tcp“ znamená proudový přenos a „udp“ znamená odpovědní datagramy.  
  Indikátory protokolu pro surové datagramy a datagram2 mohou být definovány později.  
  Povolené znaky jsou [a-z0-9-] a nesmí začínat ani končit pomlčkou.
- optionvalue := self | srvrecord[,srvrecord]*
- self := „0“ ttl port [appoptions]
- srvrecord := „1“ ttl priority weight port target [appoptions]
- ttl := čas života, celé číslo v sekundách. Kladné celé číslo. Příklad: „86400“.  
  Doporučuje se minimálně 86400 (jeden den), podrobnosti viz sekce Doporučení níže.
- priority := Priorita cílového hostitele, nižší hodnota znamená preferovanější. Nezáporné celé číslo. Příklad: „0“  
  Užitečné pouze pokud existuje více než jeden záznam, ale vyžadováno i při jednom záznamu.
- weight := Relativní váha pro záznamy se stejnou prioritou. Vyšší hodnota znamená větší šanci na výběr. Nezáporné celé číslo. Příklad: „0“  
  Užitečné pouze pokud existuje více než jeden záznam, ale vyžadováno i při jednom záznamu.
- port := Port I2CP, na kterém je služba dostupná. Nezáporné celé číslo. Příklad: „25“  
  Port 0 je podporován, ale nedoporučuje se.
- target := Doména nebo b32 cíle poskytujícího službu. Platná [doména](/docs/overview/naming/). Musí být malými písmeny.  
  Příklad: „aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p“ nebo „example.i2p“.  
  Doporučuje se b32, pokud doména není „známá“, tj. v oficiální nebo výchozí adresáři.
- appoptions := libovolný text specifický pro aplikaci, nesmí obsahovat „ “ ani „,“. Kódování je UTF-8.

### Příklady

V LS2 pro aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, odkazující na jeden SMTP server:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

V LS2 pro aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, odkazující na dva SMTP servery:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

V LS2 pro bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, odkazující na sebe sama jako SMTP server:

    "_smtp._tcp" "0 999999 25"

Možný formát pro přesměrování e-mailu (viz níže):

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### Limity

Formát datové struktury Mapping použitý pro možnosti LS2 omezuje klíče a hodnoty na maximálně 255 bajtů (ne znaků).  
S cílem b32 má optionvalue přibližně 67 bajtů, takže se vejdou jen 3 záznamy.  
Možná jen jeden nebo dva s dlouhým polem appoptions, nebo až čtyři až pět s krátkou doménou.  
To by mělo stačit; více záznamů by mělo být vzácné.


### Rozdíly od RFC 2782

- Žádné koncové tečky
- Žádný název za proto
- Vyžadováno malé písmeno
- Textový formát s čárkami oddělenými záznamy, nikoli binární formát DNS
- Jiné indikátory typu záznamu
- Další pole appoptions


### Poznámky

Není povoleno zástupné vyhledávání jako (hvězdička), (hvězdička)._tcp nebo _tcp.  
Každá podporovaná služba musí mít svůj vlastní záznam.



### Registr názvů služeb

Nestandardní identifikátory, které nejsou uvedeny v [registru typů služeb DNS-SD](http://www.dns-sd.org/ServiceTypes.html) nebo Linux /etc/services,  
mohou být požadovány a přidány do [specifikace běžných struktur](/docs/specs/common-structures/).

Formáty appoptions specifické pro službu mohou být přidány také tam.


### Specifikace I2CP

[I2CP protokol](/docs/specs/i2cp/) musí být rozšířen, aby podporoval vyhledávání služeb.  
Jsou vyžadovány další kódy chyb MessageStatusMessage a/nebo HostReplyMessage související s vyhledáváním služeb.  
Aby bylo vyhledávací zařízení obecné, ne jen specifické pro záznamy služeb,  
je návrh takový, že podporuje načítání všech možností LS2.

Implementace: Rozšiřte HostLookupMessage o požadavek na možnosti LS2 pro hash, doménu a cíl (typy požadavků 2-4).  
Rozšiřte HostReplyMessage o mapování možností, pokud je požadováno.  
Rozšiřte HostReplyMessage o další kódy chyb.

Mapování možností může být na straně klienta nebo směrovače dočasně uloženo do mezipaměti nebo negativně uloženo do mezipaměti, závisí na implementaci.  
Doporučená maximální doba je jedna hodina, pokud TTL záznamu služby není kratší.  
Záznamy služeb mohou být uloženy do mezipaměti až do TTL určeného aplikací, klientem nebo směrovačem.

Rozšiřte specifikaci následovně:

#### Konfigurační možnosti

Přidejte následující do [konfiguračních možností I2CP](/docs/specs/i2cp/)

i2cp.leaseSetOption.nnn

Možnosti, které mají být vloženy do leasesetu. Pouze pro LS2.  
nnn začíná od 0. Hodnota možnosti obsahuje „key=value“.  
(nezahrnujte uvozovky)

Příklad:
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### Zpráva HostLookup

- Typ vyhledávání 2: Vyhledávání podle hash, požadavek mapování možností
- Typ vyhledávání 3: Vyhledávání podle domény, požadavek mapování možností
- Typ vyhledávání 4: Vyhledávání podle cíle, požadavek mapování možností

Pro typ vyhledávání 4 je položka 5 cíl (Destination).



#### Zpráva HostReply

Pro typy vyhledávání 2-4 musí směrovač stáhnout leaseset,  
i když je klíč vyhledávání v adresáři.

V případě úspěchu bude HostReply obsahovat mapování možností z leasesetu a zahrne jej jako položku 5 za cílem.  
Pokud nejsou v mapování žádné možnosti, nebo byl leaseset verze 1,  
bude stále zahrnuto jako prázdné mapování (dva bajty: 0 0).  
Zahrnuty budou všechny možnosti z leasesetu, ne jen možnosti záznamů služeb.  
Například možnosti pro parametry definované v budoucnu mohou být přítomny.

Při selhání vyhledávání leasesetu bude odpověď obsahovat nový kód chyby 6 (selhání vyhledávání leasesetu)  
a nebude obsahovat žádné mapování.  
Když je vrácen kód chyby 6, pole Destination může být přítomno nebo nemusí.  
Bude přítomno, pokud bylo vyhledávání domény v adresáři úspěšné,  
nebo pokud bylo předchozí vyhledávání úspěšné a výsledek byl uložen do mezipaměti,  
nebo pokud byl cíl přítomen ve zprávě vyhledávání (typ vyhledávání 4).

Pokud typ vyhledávání není podporován,  
bude odpověď obsahovat nový kód chyby 7 (typ vyhledávání nepodporován).



### Specifikace SAM

[SAMv3 protokol](/docs/api/samv3/) musí být rozšířen, aby podporoval vyhledávání služeb.

Rozšiřte NAMING LOOKUP následovně:

NAMING LOOKUP NAME=example.i2p OPTIONS=true požaduje mapování možností v odpovědi.

NAME může být úplný base64 cíl, pokud OPTIONS=true.

Pokud bylo vyhledávání cíle úspěšné a možnosti byly přítomny v leasesetu,  
pak v odpovědi, za cílem,  
bude jeden nebo více možností ve formě OPTION:key=value.  
Každá možnost bude mít samostatnou předponu OPTION:.  
Zahrnuty budou všechny možnosti z leasesetu, ne jen možnosti záznamů služeb.  
Například možnosti pro parametry definované v budoucnu mohou být přítomny.  
Příklad:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Klíče obsahující '=', a klíče nebo hodnoty obsahující nový řádek,  
jsou považovány za neplatné a dvojice klíč/hodnota budou z odpovědi odstraněny.

Pokud nejsou v leasesetu nalezeny žádné možnosti, nebo pokud byl leaseset verze 1,  
pak odpověď nebude obsahovat žádné možnosti.

Pokud bylo v dotazu OPTIONS=true a leaseset není nalezen, bude vrácena nová hodnota výsledku LEASESET_NOT_FOUND.


## Alternativa vyhledávání jmen

Byl zvažován alternativní návrh, který by podporoval vyhledávání služeb jako úplnou doménu, například _smtp._tcp.example.i2p,  
aktualizací [specifikace pojmenování](/docs/overview/naming/) pro zpracování domén začínajících znakem '_'.  
Toto bylo zamítnuto z důvodu dvou důvodů:

- Změny I2CP a SAM by stále byly nutné k předání informací TTL a portu klientovi.
- Nejednalo by se o obecné zařízení, které by mohlo být použito k načtení jiných možností LS2,  
  které by mohly být definovány v budoucnu.


## Doporučení

Servery by měly uvádět TTL alespoň 86400 a standardní port pro aplikaci.



## Pokročilé funkce

### Rekurzivní vyhledávání

Může být žádoucí podporovat rekurzivní vyhledávání, kde je každý následující leaseset  
zkontrolován na záznam služby odkazující na další leaseset, ve stylu DNS.  
To pravděpodobně není nutné, alespoň v počáteční implementaci.

TODO



### Aplikací specifická pole

Může být žádoucí mít v záznamu služby data specifická pro aplikaci.  
Například provozovatel example.i2p může chtít uvést, že e-mail by měl  
být přesměrován na example@mail.i2p. Část „example@“ by musela být v samostatném poli  
záznamu služby, nebo odstraněna z cíle.

I když provozovatel provozuje vlastní e-mailovou službu, může chtít uvést,  
že e-mail by měl být odeslán na example@example.i2p. Většina služeb I2P je provozována jednou osobou.  
Takže samostatné pole může být užitečné i zde.

TODO jak to udělat obecným způsobem


### Změny vyžadované pro e-mail

Mimo rozsah tohoto návrhu. Více podrobností viz [diskuze na i2pforum](http://i2pforum.i2p/viewtopic.php?p=3102).


## Poznámky k implementaci

Ukládání záznamů služeb do mezipaměti až do TTL může být provedeno směrovačem nebo aplikací, závisí na implementaci.  
Zda ukládat do mezipaměti trvale, je také závislé na implementaci.

Vyhledávání musí také vyhledat cílový leaseset a ověřit, že obsahuje záznam „self“,  
než bude cílový cíl vrácen klientovi.


## Bezpečnostní analýza

Jelikož je leaseset podepsaný, jsou všechny záznamy služeb v něm autentizovány podpisovým klíčem cíle.

Záznamy služeb jsou veřejné a viditelné pro floodfill uzly, pokud leaseset není šifrovaný.  
Každý směrovač požadující leaseset bude moci vidět záznamy služeb.

Záznam SRV jiný než „self“ (tj. ten, který odkazuje na jiný cíl domény/b32)  
nepožaduje souhlas cílové domény/b32.  
Není jasné, zda by přesměrování služby na libovolný cíl mohlo usnadnit nějaký  
útok, nebo jaký by byl účel takového útoku.  
Tento návrh však takový útok zmírňuje tím, že vyžaduje, aby cíl  
také publikoval „self“ záznam SRV. Implementátoři musí zkontrolovat přítomnost záznamu „self“  
v leasesetu cíle.


## Kompatibilita

LS2: Žádné problémy. Všechny známé implementace aktuálně ignorují pole možností v LS2  
a správně přeskočí neprázdné pole možností.  
To bylo ověřeno testováním jak Java I2P, tak i2pd během vývoje LS2.  
LS2 byl implementován ve verzi 0.9.38 v roce 2016 a je dobře podporován všemi implementacemi směrovačů.  
Návrh nevyžaduje speciální podporu, ukládání do mezipaměti ani změny ve floodfillech.

Počmenování: '_' není platný znak v doménách I2P.

I2CP: Typy vyhledávání 2-4 by neměly být odesílány směrovačům s verzí API nižší než minimální verze,  
ve které jsou podporovány (bude určeno později).

SAM: Java SAM server ignoruje další klíče/hodnoty jako OPTIONS=true.  
i2pd by měl také, bude ověřeno.  
SAM klienti nezískají další hodnoty v odpovědi, pokud nejsou požadovány s OPTIONS=true.  
Zvýšení verze by nemělo být nutné.


## Migrace

Implementace mohou přidat podporu kdykoli, není potřeba žádná koordinace,  
kromě dohody o efektivní verzi API pro změny I2CP.  
Verze kompatibility SAM pro každou implementaci budou zdokumentovány ve specifikaci SAM.


## Reference

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

---
title: "Streamované MTU pro cíle ECIES"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Uzavřeno"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## Poznámka
Nasazení a testování sítě probíhá.
Předmět malých revizí.


## Přehled


### Shrnutí

ECIES snižuje režii existujících relačních (ES) zpráv o přibližně 90 bajtů.
Proto můžeme zvýšit MTU o přibližně 90 bajtů pro ECIES spojení.
Viz [specifikace ECIES](/docs/specs/ecies/#overhead), [specifikace Streaming](/docs/specs/streaming/#flags-and-option-data-fields) a [dokumentace Streaming API](/docs/api/streaming/).

Bez zvýšení MTU nejsou úspory režie v mnoha případech skutečně „uloženy“,
protože zprávy budou stejně doplněny na dvě plné tunelové zprávy.

Tento návrh nevyžaduje žádné změny specifikací.
Je publikován pouze jako návrh, aby usnadnil diskuzi a dosažení konsensu
ohledně doporučené hodnoty a detailů implementace.


### Cíle

- Zvýšit vyjednávané MTU
- Maximalizovat využití 1 KB tunelových zpráv
- Nezměnit streamovací protokol


## Návrh

Použijte stávající možnost MAX_PACKET_SIZE_INCLUDED a vyjednávání MTU.
Streaming nadále používá minimum mezi odeslaným a přijatým MTU.
Výchozí hodnota zůstává 1730 pro všechna spojení, bez ohledu na použité klíče.

Implementacím je doporučeno zahrnout možnost MAX_PACKET_SIZE_INCLUDED do všech SYN paketů, v obou směrech,
i když to není požadováno.

Pokud je cíl pouze ECIES, použijte vyšší hodnotu (ať už jako Alice nebo Bob).
Pokud je cíl dual-key, může se chování lišit:

Pokud je dual-key klient mimo směrovač (ve vnější aplikaci),
nemusí „vědět“ klíč používaný na vzdáleném konci a Alice může požadovat
vyšší hodnotu v SYN, zatímco max data v SYN zůstává 1730.

Pokud je dual-key klient uvnitř směrovače, informace o používaném klíči
může nebo nemusí být klientovi známa.
Leaseset ještě nemusel být načten, nebo interní API rozhraní
nemusí tuto informaci klientovi snadno poskytnout.
Pokud je informace dostupná, Alice může použít vyšší hodnotu;
jinak musí Alice použít standardní hodnotu 1730, dokud nebude vyjednáno.

Dual-key klient jako Bob může odeslat vyšší hodnotu v odpovědi,
i když od Alice nebyla přijata žádná hodnota nebo byla přijata hodnota 1730;
nicméně v rámci streamingu neexistuje mechanismus pro vyjednávání nahoru,
takže MTU by mělo zůstat na 1730.

Jak je uvedeno v [dokumentaci Streaming API](/docs/api/streaming/),
data v SYN paketech odeslaných od Alice k Bobovi mohou překročit Bobovo MTU.
Toto je slabina streamovacího protokolu.
Proto musí dual-key klienti omezit data v odeslaných SYN paketech
na 1730 bajtů, přičemž odesílají vyšší hodnotu MTU.
Jakmile Alice obdrží vyšší MTU od Boba, může zvýšit skutečnou maximální
odesílanou datovou část.


### Analýza

Jak je popsáno v [specifikaci ECIES](/docs/specs/ecies/#overhead), režie ElGamal pro existující relační zprávy je
151 bajtů a režie Ratchet je 69 bajtů.
Proto můžeme zvýšit MTU pro ratchetová spojení o (151 - 69) = 82 bajtů,
z 1730 na 1812.



## Specifikace

Přidejte následující změny a objasnění do sekce Výběr a vyjednávání MTU v [dokumentaci Streaming API](/docs/api/streaming/).
Žádné změny ve [specifikaci Streaming](/docs/specs/streaming/).


Výchozí hodnota možnosti i2p.streaming.maxMessageSize zůstává 1730 pro všechna spojení, bez ohledu na použité klíče.
Klienti musí použít minimum mezi odeslaným a přijatým MTU, jak je zvykem.

Existují čtyři související konstanty a proměnné MTU:

- DEFAULT_MTU: 1730, beze změny, pro všechna spojení
- i2cp.streaming.maxMessageSize: výchozí 1730 nebo 1812, může být změněno konfigurací
- ALICE_SYN_MAX_DATA: Maximální data, která Alice může zahrnout do SYN paketu
- negotiated_mtu: Minimum mezi Aliceho a Bobovým MTU, použité jako maximální velikost dat
  v SYN ACK od Boba k Alici a ve všech následných paketech odesílaných v obou směrech


Je třeba zvážit pět případů:


### 1) Alice pouze ElGamal
Žádná změna, 1730 MTU ve všech paketech.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize výchozí: 1730
- Alice může odeslat MAX_PACKET_SIZE_INCLUDED v SYN, není vyžadováno, pokud != 1730


### 2) Alice pouze ECIES
1812 MTU ve všech paketech.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize výchozí: 1812
- Alice musí odeslat MAX_PACKET_SIZE_INCLUDED v SYN



### 3) Alice Dual-Key a ví, že Bob je ElGamal
1730 MTU ve všech paketech.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize výchozí: 1812
- Alice může odeslat MAX_PACKET_SIZE_INCLUDED v SYN, není vyžadováno, pokud != 1730



### 4) Alice Dual-Key a ví, že Bob je ECIES
1812 MTU ve všech paketech.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize výchozí: 1812
- Alice musí odeslat MAX_PACKET_SIZE_INCLUDED v SYN



### 5) Alice Dual-Key a Bobův klíč je neznámý
Odeslat 1812 jako MAX_PACKET_SIZE_INCLUDED v SYN paketu, ale omezit data SYN paketu na 1730.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize výchozí: 1812
- Alice musí odeslat MAX_PACKET_SIZE_INCLUDED v SYN


### Pro všechny případy

Alice a Bob vypočítají
negotiated_mtu, minimum mezi Aliceho a Bobovým MTU, které bude použito jako maximální velikost dat
v SYN ACK od Boba k Alici a ve všech následných paketech odesílaných v obou směrech.




## Odůvodnění

Viz [zdrojový kód Java I2P](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) pro vysvětlení, proč je aktuální hodnota 1730.
Viz [specifikace ECIES](/docs/specs/ecies/#overhead) pro vysvětlení, proč je režie ECIES o 82 bajtů nižší než u ElGamal.



## Poznámky k implementaci

Pokud streaming vytváří zprávy optimální velikosti, je velmi důležité,
aby vrstva ECIES-Ratchet nepřidávala větší padding než je třeba.

Optimální velikost Garlic Message, aby se vešla do dvou tunelových zpráv,
včetně 16 bajtového Garlic Message I2NP hlavičky, 4 bajtové délky Garlic Message,
8 bajtového ES tagu a 16 bajtového MAC, je 1956 bajtů.

Doporučený algoritmus pro doplňování v ECIES je následující:

- Pokud by celková délka Garlic Message byla 1954–1956 bajtů,
  nepřidávejte blok doplňování (není místo)
- Pokud by celková délka Garlic Message byla 1938–1953 bajtů,
  přidejte blok doplňování, aby bylo doplněno přesně na 1956 bajtů.
- Jinak doplňujte obvyklým způsobem, např. náhodně o 0–15 bajtů.

Podobné strategie by mohly být použity pro optimální velikost jedné tunelové zprávy (964)
a tří tunelových zpráv (2952), i když tyto velikosti by v praxi měly být vzácné.



## Problémy

Hodnota 1812 je předběžná. Bude potvrzena a případně upravena.




## Migrace

Žádné problémy s zpětnou kompatibilitou.
Toto je stávající možnost a vyjednávání MTU je již součástí specifikace.

Starší ECIES cíle budou podporovat 1730.
Jakýkoli klient, který obdrží vyšší hodnotu, odpoví 1730 a vzdálený konec
vyjedná MTU dolů, jak je zvykem.


## Reference

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)

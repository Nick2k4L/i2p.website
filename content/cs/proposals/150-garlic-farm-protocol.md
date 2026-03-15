---
title: "Protokol Garlic Farm"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "Otevřený"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## Přehled

Toto je specifikace protokolu Garlic Farm pro přenos po drátě,
založená na JRaft, jeho kódu „exts“ pro implementaci přes TCP
a ukázkové aplikaci „dmprinter“ [JRAFT](https://github.com/datatechnology/jraft).


Nepodařilo se nám nalézt žádnou implementaci s dokumentovaným protokolem pro přenos po drátě.
Implementace JRaft je však dostatečně jednoduchá, abychom mohli
prozkoumat kód a následně dokumentovat jeho protokol.
Tento návrh je výsledkem tohoto úsilí.

Tato specifikace bude sloužit jako backend pro koordinaci směrovačů publikujících
záznamy v Meta LeaseSet. Viz návrh 123.


## Cíle

- Malá velikost kódu
- Založeno na stávající implementaci
- Žádné serializované Java objekty ani žádné Java-specifické funkce nebo kódování
- Jakékoli zavádění (bootstrapping) je mimo rozsah. Předpokládá se, že alespoň jeden jiný server je
  pevně zakódován nebo nakonfigurován mimo tento protokol.
- Podpora jak scénářů mimo pásmo, tak použití v rámci I2P.


## Návrh

Protokol Raft není konkrétním protokolem; definuje pouze stavový stroj.
Proto dokumentujeme konkrétní protokol JRaft a na něm založíme náš protokol.
Jedinou změnou oproti protokolu JRaft je přidání
ověřovacího handshake.

Raft zvolí Vůdce (Leader), jehož úkolem je publikovat záznamy do logu.
Log obsahuje data konfigurace Raft a aplikační data.
Aplikační data obsahují stav směrovače každého serveru a cíl (Destination)
pro cluster Meta LS2.
Servery používají společný algoritmus k určení vydavatele a obsahu
Meta LS2.
Vydavatel Meta LS2 NENÍ nutně Vůdcem Raft.


## Specifikace

Protokol pro přenos po drátě běží přes SSL sokety nebo ne-SSL I2P sokety.
I2P sokety jsou přesměrovány přes HTTP Proxy.
Není podporováno použití nešifrovaných soketů pro clearnet.

### Handshake a ověření

Není definováno JRaft.

Cíle:

- Metoda ověření uživatel/heslo
- Identifikátor verze
- Identifikátor clusteru
- Rozšiřitelnost
- Snadné přesměrování při použití I2P soketů
- Nepřehánět zbytečně expozici serveru jako serveru Garlic Farm
- Jednoduchý protokol, aby nebyla vyžadována plná implementace webového serveru
- Kompatibilita s běžnými standardy, aby implementace mohly použít
  standardní knihovny, pokud je to žádoucí

Použijeme handshake podobné websocketu a
ověření pomocí HTTP Digest [RFC 2617](https://tools.ietf.org/html/rfc2617).
RFC 2617 Basic authentication NENÍ podporováno.
Při přesměrování přes HTTP proxy komunikujte s
proxy podle specifikace v [RFC 2616](https://tools.ietf.org/html/rfc2616).

#### Přihlašovací údaje

Zda jsou uživatelská jména a hesla specifická pro cluster nebo
pro server, je závislé na implementaci.


#### HTTP Požadavek 1

Iniciátor pošle následující.

Všechny řádky jsou ukončeny CRLF, jak vyžaduje HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (jakékoli další hlavičky jsou ignorovány)
  (prázdný řádek)

  CLUSTER je název clusteru (výchozí „farm“)
  VERSION je verze Garlic Farm (aktuálně „1“)

```


#### HTTP Odpověď 1

Pokud není cesta správná, příjemce pošle standardní odpověď „HTTP/1.1 404 Not Found“,
jak je uvedeno v [RFC 2616](https://tools.ietf.org/html/rfc2616).

Pokud je cesta správná, příjemce pošle standardní odpověď „HTTP/1.1 401 Unauthorized“,
včetně hlavičky WWW-Authenticate s ověřením HTTP digest,
jak je uvedeno v [RFC 2617](https://tools.ietf.org/html/rfc2617).

Obě strany poté zavřou soket.


#### HTTP Požadavek 2

Iniciátor pošle následující,
jak je uvedeno v [RFC 2617](https://tools.ietf.org/html/rfc2617).

Všechny řádky jsou ukončeny CRLF, jak vyžaduje HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (Sec-Websocket-* hlavičky pokud je přesměrováno)
  Authorization: (hlavička autorizace HTTP digest podle RFC 2617)
  (jakékoli další hlavičky jsou ignorovány)
  (prázdný řádek)

  CLUSTER je název clusteru (výchozí „farm“)
  VERSION je verze Garlic Farm (aktuálně „1“)

```


#### HTTP Odpověď 2

Pokud není ověření správné, příjemce pošle další standardní odpověď „HTTP/1.1 401 Unauthorized“,
jak je uvedeno v [RFC 2617](https://tools.ietf.org/html/rfc2617).

Pokud je ověření správné, příjemce pošle následující odpověď,
jak je uvedeno v protokolu WebSocket.

Všechny řádky jsou ukončeny CRLF, jak vyžaduje HTTP.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (Sec-Websocket-* hlavičky)
  (jakékoli další hlavičky jsou ignorovány)
  (prázdný řádek)

```

Po přijetí této odpovědi zůstane soket otevřen.
Níže definovaný protokol Raft pak začne běžet na stejném soketu.


#### Ukládání do mezipaměti

Přihlašovací údaje musí být uloženy v mezipaměti alespoň na jednu hodinu, aby
následné připojení mohlo přejít přímo k
„HTTP Request 2“ výše.



### Typy zpráv

Existují dva typy zpráv: požadavky a odpovědi.
Požadavky mohou obsahovat záznamy logu a jsou proměnné velikosti;
odpovědi neobsahují záznamy logu a jsou pevné velikosti.

Typy zpráv 1–4 jsou standardní RPC zprávy definované protokolem Raft.
Toto je základní protokol Raft.

Typy zpráv 5–15 jsou rozšířené RPC zprávy definované
JRaft, které podporují klienty, dynamické změny serverů a
efektivní synchronizaci logu.

Typy zpráv 16–17 jsou RPC zprávy pro kompresi logu definované
v části 7 protokolu Raft.


| Zpráva | Číslo | Odesílatel | Příjemce | Poznámky |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Kandidát | Následovník | Standardní Raft RPC; nesmí obsahovat záznamy logu |
| RequestVoteResponse | 2 | Následovník | Kandidát | Standardní Raft RPC |
| AppendEntriesRequest | 3 | Vůdce | Následovník | Standardní Raft RPC |
| AppendEntriesResponse | 4 | Následovník | Vůdce / Klient | Standardní Raft RPC |
| ClientRequest | 5 | Klient | Vůdce / Následovník | Odpověď je AppendEntriesResponse; musí obsahovat pouze aplikační záznamy logu |
| AddServerRequest | 6 | Klient | Vůdce | Musí obsahovat pouze jeden záznam logu ClusterServer |
| AddServerResponse | 7 | Vůdce | Klient | Vůdce také pošle JoinClusterRequest |
| RemoveServerRequest | 8 | Následovník | Vůdce | Musí obsahovat pouze jeden záznam logu ClusterServer |
| RemoveServerResponse | 9 | Vůdce | Následovník | |
| SyncLogRequest | 10 | Vůdce | Následovník | Musí obsahovat pouze jeden záznam logu LogPack |
| SyncLogResponse | 11 | Následovník | Vůdce | |
| JoinClusterRequest | 12 | Vůdce | Nový server | Pozvánka k připojení; musí obsahovat pouze jeden záznam logu Configuration |
| JoinClusterResponse | 13 | Nový server | Vůdce | |
| LeaveClusterRequest | 14 | Vůdce | Následovník | Příkaz k opuštění |
| LeaveClusterResponse | 15 | Následovník | Vůdce | |
| InstallSnapshotRequest | 16 | Vůdce | Následovník | Raft část 7; musí obsahovat pouze jeden záznam logu SnapshotSyncRequest |
| InstallSnapshotResponse | 17 | Následovník | Vůdce | Raft část 7 |


### Navázání spojení

Po dokončení HTTP handshake probíhá sekvence navázání následovně:

```text

Nový server Alice              Náhodný následovník Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  Pokud Bob řekne, že je vůdcem, pokračujte níže.
  Jinak Alice musí odpojit Boba a připojit se k vůdci.


  Nový server Alice              Vůdce Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       NEBO InstallSnapshotRequest
  SyncLogResponse  ------->
  NEBO InstallSnapshotResponse

```

Sekvence odpojení:

```text

Následovník Alice              Vůdce Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

Sekvence volby:

```text

Kandidát Alice               Následovník Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  Pokud Alice vyhraje volby:

  Vůdce Alice                Následovník Bob

  AppendEntriesRequest   ------->
  (heartbeat)
          <---------   AppendEntriesResponse

```


### Definice

- Zdroj (Source): Identifikuje odesílatele zprávy
- Cíl (Destination): Identifikuje příjemce zprávy
- Termíny (Terms): Viz Raft. Inicializováno na 0, monotónně rostoucí
- Indexy (Indexes): Viz Raft. Inicializováno na 0, monotónně rostoucí



### Požadavky

Požadavky obsahují hlavičku a nula nebo více záznamů logu.
Požadavky obsahují hlavičku pevné velikosti a volitelné záznamy logu proměnné velikosti.


#### Hlavička požadavku

Hlavička požadavku má 45 bajtů, následovně.
Všechny hodnoty jsou neznaménkové, big-endian.

```text

Typ zprávy:      1 bajt
  Zdroj:            ID, 4 bajtové celé číslo
  Cíl:               ID, 4 bajtové celé číslo
  Termín:            Aktuální termín (viz poznámky), 8 bajtové celé číslo
  Poslední termín logu:     8 bajtové celé číslo
  Poslední index logu:    8 bajtové celé číslo
  Index potvrzení:      8 bajtové celé číslo
  Velikost záznamů logu:  Celková velikost v bajtech, 4 bajtové celé číslo
  Záznamy logu:       viz níže, celková délka podle specifikace

```


#### Poznámky

V RequestVoteRequest je Termín termínem kandidáta.
Jinak je to aktuální termín vůdce.

V AppendEntriesRequest, pokud je velikost záznamů logu nula,
jde o zprávu heartbeat (keepalive).


#### Záznamy logu

Log obsahuje nula nebo více záznamů logu.
Každý záznam logu je následující.
Všechny hodnoty jsou neznaménkové, big-endian.

```text

Termín:           8 bajtové celé číslo
  Typ hodnoty:     1 bajt
  Velikost záznamu:     V bajtech, 4 bajtové celé číslo
  Záznam:          délka podle specifikace

```


#### Obsah logu

Všechny hodnoty jsou neznaménkové, big-endian.

| Typ hodnoty logu | Číslo |
| :--- | :--- |
| Aplikační | 1 |
| Konfigurace | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Aplikační

Obsah aplikace je kódován v UTF-8 [JSON](https://www.json.org/).
Viz sekce Aplikační vrstva níže.


#### Konfigurace

Používá se pro serializaci nové konfigurace clusteru vůdcem a její replikaci na partnery.
Obsahuje nula nebo více konfigurací ClusterServer.


```text

Index logu:  8 bajtové celé číslo
  Poslední index logu:  8 bajtové celé číslo
  Data ClusterServer pro každý server:
    ID:                4 bajtové celé číslo
    Délka dat koncového bodu: V bajtech, 4 bajtové celé číslo
    Data koncového bodu:     ASCII řetězec ve tvaru „tcp://localhost:9001“, délka podle specifikace

```


#### ClusterServer

Konfigurační informace pro server v clusteru.
Zahrnuto pouze v zprávě AddServerRequest nebo RemoveServerRequest.

Použito v AddServerRequest:

```text

ID:                4 bajtové celé číslo
  Délka dat koncového bodu: V bajtech, 4 bajtové celé číslo
  Data koncového bodu:     ASCII řetězec ve tvaru „tcp://localhost:9001“, délka podle specifikace

```


Použito v RemoveServerRequest:

```text

ID:                4 bajtové celé číslo

```


#### LogPack

Zahrnuto pouze v zprávě SyncLogRequest.

Následující je před přenosem komprimováno pomocí gzip:


```text

Délka dat indexu: V bajtech, 4 bajtové celé číslo
  Délka dat logu:   V bajtech, 4 bajtové celé číslo
  Data indexu:     8 bajtů pro každý index, délka podle specifikace
  Data logu:       délka podle specifikace

```



#### SnapshotSyncRequest

Zahrnuto pouze v zprávě InstallSnapshotRequest.

```text

Poslední index logu:  8 bajtové celé číslo
  Poslední termín logu:   8 bajtové celé číslo
  Délka dat konfigurace: V bajtech, 4 bajtové celé číslo
  Data konfigurace:     délka podle specifikace
  Offset:          Offset dat v databázi, v bajtech, 8 bajtové celé číslo
  Délka dat:        V bajtech, 4 bajtové celé číslo
  Data:            délka podle specifikace
  Je dokončeno:         1 pokud ano, 0 pokud ne (1 bajt)

```




### Odpovědi

Všechny odpovědi mají 26 bajtů, následovně.
Všechny hodnoty jsou neznaménkové, big-endian.

```text

Typ zprávy:   1 bajt
  Zdroj:         ID, 4 bajtové celé číslo
  Cíl:            Obvykle skutečné ID cíle (viz poznámky), 4 bajtové celé číslo
  Termín:           Aktuální termín, 8 bajtové celé číslo
  Další index:     Inicializováno na poslední index logu vůdce + 1, 8 bajtové celé číslo
  Je přijato:    1 pokud přijato, 0 pokud nepřijato (viz poznámky), 1 bajt

```


#### Poznámky

ID cíle je obvykle skutečný cíl této zprávy.
U AppendEntriesResponse, AddServerResponse a RemoveServerResponse
je to však ID aktuálního vůdce.

V RequestVoteResponse je „Je přijato“ 1 pro hlas pro kandidáta (žadatele),
a 0 pro nepřijetí hlasu.


## Aplikační vrstva

Každý server pravidelně vkládá aplikační data do logu pomocí ClientRequest.
Aplikační data obsahují stav směrovače každého serveru a cíl
pro cluster Meta LS2.
Servery používají společný algoritmus k určení vydavatele a obsahu
Meta LS2.
Server s „nejlepším“ nedávným stavem v logu je vydavatelem Meta LS2.
Vydavatel Meta LS2 NENÍ nutně Vůdcem Raft.


### Obsah aplikačních dat

Aplikační data jsou kódována v UTF-8 [JSON](https://json.org/),
pro jednoduchost a rozšiřitelnost.
Plná specifikace je ještě neznámá (TBD).
Cílem je poskytnout dostatek dat pro napsání algoritmu, který určí „nejlepší“
směrovač pro publikování Meta LS2, a aby měl vydavatel dostatek informací
pro vážení cílů (Destinations) v Meta LS2.
Data budou obsahovat statistiky směrovače i cílů.

Data mohou volitelně obsahovat vzdálená měření stavu
ostatních serverů a schopnost stáhnout Meta LS.
Tato data nebudou podporována ve verzi 1.0.

Data mohou volitelně obsahovat konfigurační informace zadané
administrátorským klientem.
Tato data nebudou podporována ve verzi 1.0.

Pokud je uvedeno „název: hodnota“, určuje to klíč a hodnotu v mapě JSON.
Jinak je specifikace ještě neznámá (TBD).


Data clusteru (nejvyšší úroveň):

- cluster: Název clusteru
- date: Datum těchto dat (long, ms od epochy)
- id: Raft ID (celé číslo)

Konfigurační data (config):

- Jakékoli konfigurační parametry

Stav publikování MetaLS (meta):

- destination: cíl MetaLS, base64
- lastPublishedLS: pokud přítomno, base64 kódování naposledy publikovaného MetaLS
- lastPublishedTime: v ms, nebo 0 pokud nikdy
- publishConfig: stav konfigurace vydavatele vypnuto/zapnuto/auto
- publishing: stav vydavatele MetaLS, boolean true/false

Data směrovače (router):

- lastPublishedRI: pokud přítomno, base64 kódování naposledy publikovaných informací o směrovači
- uptime: Doba běhu v ms
- Zpoždění úloh (Job lag)
- Průzkumné tunely
- Účastnické tunely
- Nakonfigurovaná šířka pásma
- Aktuální šířka pásma

Cíle (destinations):
Seznam

Data cíle:

- destination: cíl, base64
- uptime: Doba běhu v ms
- Nakonfigurované tunely
- Aktuální tunely
- Nakonfigurovaná šířka pásma
- Aktuální šířka pásma
- Nakonfigurovaná připojení
- Aktuální připojení
- Data blacklistu

Data vzdáleného měření směrovače:

- Poslední viděná verze RI
- Čas stažení LS
- Data testu připojení
- Profil nejbližších floodfillů
  pro časové období včera, dnes a zítra

Data vzdáleného měření cíle:

- Poslední viděná verze LS
- Čas stažení LS
- Data testu připojení
- Profil nejbližších floodfillů
  pro časové období včera, dnes a zítra

Data vzdáleného měření Meta LS:

- Poslední viděná verze
- Čas stažení
- Profil nejbližších floodfillů
  pro časové období včera, dnes a zítra


## Rozhraní pro správu

Ještě neznámé (TBD), možná samostatný návrh.
Není vyžadováno pro první verzi.

Požadavky na administrační rozhraní:

- Podpora více hlavních cílů, tj. více virtuálních clusterů (farms)
- Komplexní přehled sdíleného stavu clusteru – všechny statistiky publikované členy, kdo je aktuální vůdce atd.
- Možnost vynutit odstranění účastníka nebo vůdce z clusteru
- Možnost vynutit publikování metaLS (pokud aktuální uzel je vydavatelem)
- Možnost vyloučit hash z metaLS (pokud aktuální uzel je vydavatelem)
- Funkce pro import/export konfigurace pro hromadná nasazení



## Rozhraní směrovače

Ještě neznámé (TBD), možná samostatný návrh.
i2pcontrol není vyžadováno pro první verzi a podrobné změny budou uvedeny v samostatném návrhu.

Požadavky na rozhraní Garlic Farm – směrovač (v-JVM java nebo i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // pravděpodobně ne v MVP
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // nebo podepsaný MetaLeaseSet? Kdo podepisuje?
- stopPublishingMetaLS(Hash masterHash)
- ověření ještě neznámé (TBD)?


## Odůvodnění

Atomix je příliš velký a nepovolí nám přizpůsobení pro směrování
protokolu přes I2P. Navíc jeho formát přenosu po drátě není dokumentován a závisí
na serializaci Java.


## Poznámky



## Problémy

- Klient nemá žádný způsob, jak zjistit a připojit se k neznámému vůdci.
  Byla by to malá změna, aby následovník poslal konfiguraci jako záznam logu v odpovědi AppendEntriesResponse.



## Migrace

Žádné problémy s zpětnou kompatibilitou.


## Reference

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)

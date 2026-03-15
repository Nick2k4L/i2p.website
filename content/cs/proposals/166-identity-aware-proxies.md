---
title: "I2P návrh č. 166: Identity/Host Aware Tunnel Types"
number: "166"
author: "eyedeekay"
created: "2024-05-27"
lastupdated: "2024-08-27"
status: "Otevřený"
thread: "http://i2pforum.i2p/viewforum.php?f=13"
target: "0.9.65"
toc: true
---
### Návrh hostitelem-vědomého typu HTTP proxy tunelu

Toto je návrh řešení „Problému sdílené identity“ při běžném použití HTTP přes I2P, který zavádí nový typ HTTP proxy tunelu. Tento typ tunelu má doplňkové chování, jehož cílem je zabránit nebo omezit užitečnost sledování prováděného potenciálně nepřátelskými operátory skrytých služeb vůči cíleným uživatelským agentům (prohlížečům) a samotné I2P klientské aplikaci.

#### Co je „Problém sdílené identity“?

„Problém sdílené identity“ nastává, když uživatelský agent na kryptograficky adresované překryvné síti sdílí kryptografickou identitu s jiným uživatelským agentem. K tomu dochází například, když jsou Firefox a GNU Wget nakonfigurovány tak, aby používaly stejnou HTTP proxy.

V tomto scénáři může server shromažďovat a ukládat kryptografickou adresu (Destination), která se používá k odpovědi na aktivitu. Může ji považovat za „otisk prstu“, který je vždy 100 % unikátní, protože má kryptografický původ. To znamená, že propojitelnost pozorovaná problémem sdílené identity je dokonalá.

Ale je to vůbec problém?
^^^^^^^^^^^^^^^^^^^^^^^^^

Problém sdílené identity je problémem tehdy, když uživatelské agenty, které používají stejný protokol, vyžadují nepropojitelnost. [Poprvé byl zmíněn v kontextu HTTP v tomto vláknu na Redditu](https://old.reddit.com/r/i2p/comments/579idi/warning_i2p_is_linkablefingerprintable/), s přístupem k odstraněným komentářům díky [pullpush.io](https://api.pullpush.io/reddit/search/comment/?link_id=579idi). *V té době* jsem byl jedním z nejaktivnějších odpovídačů a *v té době* jsem si myslel, že problém je malý. Během posledních 8 let se situace i mé stanovisko změnily, nyní se domnívám, že hrozba spojená s úmyslnou korelací destinací výrazně roste, jakmile více stránek získává možnost „profilovat“ konkrétní uživatele.

Tento útok má velmi nízkou bariéru vstupu. Stačí, aby operátor skryté služby provozoval více služeb. U útoků na současné návštěvy (navštěvování více stránek současně) je to jediná požadovaná podmínka. U nesoučasného propojování musí jedna z těchto služeb být služba, která hostuje „účty“ patřící jednomu uživateli, který je cílem sledování.

V současnosti každý operátor služby, který hostuje uživatelské účty, může korelovat tyto účty s aktivitou napříč libovolnými stránkami, které ovládá, a to využitím problému sdílené identity. Mastodon, Gitlab nebo dokonce jednoduché fóra by mohly být útočníky v maskování, pokud provozují více než jednu službu a mají zájem o vytvoření profilu uživatele. Toto sledování by mohlo být prováděno kvůli špehování, finančnímu zisku nebo z důvodů týkajících se zpravodajství. V současnosti existuje desítky hlavních operátorů, kteří by tento útok mohli provést a získat z něj smysluplná data. Většinou jim zatím důvěřujeme, že to neudělají, ale hráči, kterým na našem názoru nezáleží, by se mohli snadno objevit.

Toto je přímo spojeno s poměrně základní formou budování profilů na běžném webu, kde organizace mohou korelovat interakce na jejich stránce s interakcemi na sítích, které ovládají. V I2P, protože kryptografická destinace je unikátní, může být tato technika někdy dokonce spolehlivější, i když bez dodatečné síly geolokace.

Problém sdílené identity není užitečný proti uživateli, který používá I2P výhradně k zamaskování geolokace. Nelze jej také použít k porušení směrování I2P. Je to pouze problém správy kontextové identity.

-  Nelze použít problém sdílené identity k geolokaci uživatele I2P.
-  Nelze použít problém sdílené identity k propojení relací I2P, pokud nejsou současné.

Je však možné jej použít k oslabení anonymity uživatele I2P za okolností, které jsou pravděpodobně velmi běžné. Jedním z důvodů, proč jsou běžné, je to, že podporujeme použití Firefoxu, webového prohlížeče, který umožňuje „kartové“ provozování.

-  Je *vždy* možné vytvořit otisk prstu z problému sdílené identity v *libovolném* webovém prohlížeči, který podporuje požadavky na externí zdroje.
-  Zakázání Javascriptu nepřináší **žádný** efekt proti problému sdílené identity.
-  Pokud lze vytvořit spojení mezi nesoučasnými relacemi, například pomocí „tradičního“ otisku prohlížeče, pak lze sdílenou identitu použít tranzitivně, což potenciálně umožňuje strategii nesoučasného propojování.
-  Pokud lze vytvořit spojení mezi aktivitou na běžném webu a identitou I2P, například pokud je cíl přihlášen na stránce s přítomností jak v I2P, tak na běžném webu na obou stranách, lze sdílenou identitu použít tranzitivně, což potenciálně umožňuje úplné de-anonymizování.

Jak vnímáte závažnost problému sdílené identity ve vztahu k HTTP proxy I2P, závisí na tom, kde vy (nebo spíše „uživatel“ s potenciálně neinformovanými očekáváními) považujete „kontextovou identitu“ aplikace za ležící. Existuje několik možností:

1. HTTP je jak aplikace, tak kontextová identita – takto to funguje nyní. Všechny HTTP aplikace sdílejí identitu.
2. Proces je aplikace a kontextová identita – takto to funguje, když aplikace používá API jako SAMv3 nebo I2CP, kde aplikace vytváří svou identitu a ovládá její životnost.
3. HTTP je aplikace, ale hostitel je kontextová identita – toto je předmětem tohoto návrhu, který považuje každý hostitel za potenciální „webovou aplikaci“ a považuje povrch hrozby za takový.

Je to řešitelné?
^^^^^^^^^^^^^^^^

Pravděpodobně není možné vytvořit proxy, která by inteligentně reagovala na každý možný případ, kdy by její provoz mohl oslabit anonymitu aplikace. Je však možné vytvořit proxy, která inteligentně reaguje na konkrétní aplikaci, která se chová předvídatelným způsobem. Například u moderních webových prohlížečů se očekává, že uživatelé budou mít otevřené více karet, kde budou interagovat s více weby, které budou rozlišeny podle názvu hostitele.

To nám umožňuje zlepšit chování HTTP proxy pro tento typ uživatelského agenta HTTP tím, že chování proxy bude odpovídat chování uživatelského agenta, a to tím, že každému hostiteli přidělí vlastní destinaci při použití HTTP proxy. Tato změna znemožňuje použití problému sdílené identity k odvození otisku prstu, který by mohl být použit k korelaci činnosti klienta s 2 hostiteli, protože tyto 2 hostitelé již nebudou sdílet návratovou identitu.

Popis:
^^^^^^

Nová HTTP proxy bude vytvořena a přidána do Správce skrytých služeb (I2PTunnel). Nová HTTP proxy bude fungovat jako „multiplexer“ I2PSocketManagerů. Samotný multiplexer nemá žádnou destinaci. Každý jednotlivý I2PSocketManager, který se stane součástí multiplexu, má svou vlastní lokální destinaci a svůj vlastní fond tunelů. I2PSocketManagery jsou vytvářeny multiplexerem na vyžádání, kde „vyžádání“ je první návštěva nového hostitele. Je možné optimalizovat vytváření I2PSocketManagerů před jejich vložením do multiplexu tím, že se vytvoří jeden nebo více předem a uloží mimo multiplexer. To může zlepšit výkon.

Další I2PSocketManager, se svou vlastní destinací, je nastaven jako nositel „Outproxy“ pro jakoukoli stránku, která nemá I2P destinaci, například jakoukoli stránku na běžném webu. To efektivně činí veškeré použití Outproxy jedinou kontextovou identitou, s tím, že konfigurace více Outproxy pro tunel způsobí běžnou „přilepivou“ rotaci outproxy, kde každý outproxy dostává požadavky pouze pro jednu stránku. Toto je *téměř* ekvivalentní chování jako izolace HTTP přes I2P proxy podle destinace na běžném internetu.

Zvážení zdrojů:
'''''''''''''''

Nová HTTP proxy vyžaduje další zdroje ve srovnání s existující HTTP proxy. Bude:

-  Potenciálně stavět více tunelů a I2PSocketManagerů
-  Budovat tunely častěji

Každá z těchto činností vyžaduje:

-  Místní výpočetní zdroje
-  Síťové zdroje od partnerů

Nastavení:
''''''''''

Aby se minimalizoval dopad zvýšeného využití zdrojů, měla by být proxy nakonfigurována tak, aby používala co nejméně. Proxy, které jsou součástí multiplexu (ne rodičovská proxy), by měly být nakonfigurovány tak, aby:

-  Multiplexované I2PSocketManagery stavěly 1 tunel dovnitř, 1 tunel ven ve svých fondech tunelů
-  Multiplexované I2PSocketManagery používaly ve výchozím nastavení 3 skoky
-  Uzavíraly sokety po 10 minutách nečinnosti
-  I2PSocketManagery spuštěné multiplexerem sdílely životnost multiplexeru. Multiplexované tunely nejsou „zničeny“, dokud není zničen nadřazený multiplexer.

Diagramy:
^^^^^^^^

Níže uvedený diagram znázorňuje současný provoz HTTP proxy, který odpovídá „Možnosti 1.“ v sekci „Je to problém?“. Jak vidíte, HTTP proxy komunikuje s I2P stránkami přímo pomocí pouze jedné destinace. V tomto scénáři je HTTP jak aplikací, tak kontextovou identitou.

```text
**Současná situace: HTTP je aplikace, HTTP je kontextová identita**
                                                      __-> Outproxy <-> i2pgit.org
                                                     /
Prohlížeč <-> HTTP Proxy (jedna destinace) <-> I2PSocketManager <---> idk.i2p
                                                     \__-> translate.idk.i2p
                                                      \__-> git.idk.i2p
```

Níže uvedený diagram znázorňuje provoz hostitelem-vědomé HTTP proxy, který odpovídá „Možnosti 3.“ v sekci „Je to problém?“. V tomto scénáři je HTTP aplikací, ale hostitel definuje kontextovou identitu, přičemž každá I2P stránka komunikuje s jinou HTTP proxy s unikátní destinací pro každého hostitele. To brání operátorům více stránek v rozlišení, když stejná osoba navštěvuje více stránek, které provozují.

```text
**Po změně: HTTP je aplikace, hostitel je kontextová identita**
                                                    __-> I2PSocketManager (Destinace A – pouze Outproxy) <--> i2pgit.org
                                                   /
Prohlížeč <-> HTTP Proxy Multiplexer (žádná destinace) <---> I2PSocketManager (Destinace B) <--> idk.i2p
                                                   \__-> I2PSocketManager (Destinace C) <--> translate.idk.i2p
                                                    \__-> I2PSocketManager (Destinace C) <--> git.idk.i2p
```

Stav:
^^^^^

Pracující implementace v Javě hostitelem-vědomé proxy, která odpovídá starší verzi tohoto návrhu, je k dispozici ve větvi idk's fork: i2p.i2p.2.6.0-browser-proxy-post-keepalive Odkaz v citacích. Probíhá intenzivní revize, aby byly změny rozděleny do menších částí.

Implementace s různými schopnostmi byly napsány v Go pomocí knihovny SAMv3, mohou být užitečné pro vkládání do jiných aplikací Go nebo pro go-i2p, ale nejsou vhodné pro Java I2P. Navíc postrádají dobrou podporu pro interaktivní práci s šifrovanými leaseSety.

Příloha: ``i2psocks``
                     

Jednoduchý přístup orientovaný na aplikaci pro izolaci jiných typů klientů je možný bez implementace nového typu tunelu nebo změny stávajícího kódu I2P kombinací nástrojů I2PTunnel, které jsou již široce dostupné a otestované v komunitě soukromí. Tento přístup však činí obtížný předpoklad, který není pravdivý pro HTTP a také ne pro mnoho jiných potenciálních druhů klientů I2P.

Přibližně následující skript vytvoří aplikací-vědomou SOCKS5 proxy a socksifikuje základní příkaz:

```sh
#! /bin/sh
command_to_proxy="$@"
java -jar ~/i2p/lib/i2ptunnel.jar -wait -e 'sockstunnel 7695'
torsocks --port 7695 $command_to_proxy
```

Příloha: ``příklad implementace útoku``
                                        

[Příklad implementace útoku sdílené identity na HTTP uživatelské agenty](https://github.com/eyedeekay/colluding_sites_attack/) existuje několik let. Další příklad je k dispozici v podsložce ``simple-colluder`` [úložiště idk’s prop166](https://git.idk.i2p/idk/i2p.host-aware-proxy) Tyto příklady jsou záměrně navrženy tak, aby demonstrovaly, že útok funguje, a vyžadovaly by úpravu (i když malou), aby se z nich stal skutečný útok.

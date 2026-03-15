---
title: "Dodání OBEP do 1-z-N nebo N-z-N tunelů"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Otevřeno"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## Přehled

Tento návrh zahrnuje dvě vylepšení pro zlepšení výkonu sítě:

- Předání výběru IBGW do rukou OBEPu tím, že mu poskytne seznam
  alternativ namísto jediné možnosti.

- Povolení směrování multicastových paketů na straně OBEPu.


## Motivace

V případě přímého spojení jde o snížení zahlcení spojení tím, že OBEPu dáme větší volnost, jak se připojuje k IBGW. Schopnost zadat více tunelů nám také umožňuje implementovat multicast na straně OBEPu (tím, že zpráva bude doručena do všech zadaných tunelů).

Alternativou k části tohoto návrhu týkající se delegování by bylo poslat místo toho hash LeaseSetu, podobně jako u stávající možnosti zadat cílový hash [RouterIdentity](/docs/specs/common-structures/#common-structure-specification). To by vedlo k menší zprávě a potenciálně novějšímu LeaseSetu. Nicméně:

1. Vynutilo by to, aby OBEP provedl vyhledání.

2. LeaseSet nemusí být publikován na floodfillu, takže by vyhledání selhalo.

3. LeaseSet může být šifrovaný, takže OBEP nemůže získat příslušné lease.

4. Zadání LeaseSetu odhalí OBEPu [Destination](/docs/specs/common-structures/#destination) zprávy,
   což by jinak mohl zjistit pouze prohledáváním všech LeaseSetů v síti a hledáním shody lease.


## Návrh

Odesílatel (OBGW) by umístil některé (všechny?) cílové [Leases](/docs/specs/common-structures/#lease) do instrukcí doručení [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) místo výběru pouze jednoho.

OBEP by si jeden z nich vybral pro doručení. OBEP by vybral, pokud je k dispozici, ten, ke kterému už má spojení nebo který už zná. To by urychlilo a zvýšilo spolehlivost cesty OBEP-IBGW a snížilo celkový počet síťových spojení.

Máme jeden nepoužitý typ doručení (0x03) a dva zbývající bity (0 a 1) ve flagech pro TUNNEL-DELIVERY, které můžeme využít k implementaci těchto funkcí.


## Bezpečnostní důsledky

Tento návrh nemění množství informací, které unikají o cílové [Destination](/docs/specs/common-structures/#destination) OBGW nebo o jeho pohledu na NetDB:

- Útočník, který ovládá OBEP a prohledává LeaseSety z NetDB, už teď může určit, zda je zpráva posílána konkrétní Destination, a to hledáním dvojice TunnelId / RouterIdentity. V nejhorším případě přítomnost více Lease v TMDI může urychlit nalezení shody v databázi útočníka.

- Útočník, který provozuje zlotřilou Destination, už teď může získat informace o pohledu napojené oběti na NetDB tím, že publikuje LeaseSety obsahující různé příchozí tunely na různých floodfillech a sleduje, přes které tunely se OBGW připojuje. Z jejich pohledu je výběr tunelu OBEPem funkčně totožný s výběrem provedeným OBGW.

Flag pro multicast odhaluje OBEPům, že OBGW provádí multicast. To vytváří kompromis mezi výkonem a soukromím, který by měl být zvážen při implementaci vyšších protokolů. Jelikož se jedná o volitelný flag, uživatelé mohou rozhodnout podle potřeb své aplikace. Může být výhodné, aby se toto chovalo jako výchozí nastavení pro kompatibilní aplikace, protože široké použití různými aplikacemi by snížilo únik informací o tom, z jaké konkrétní aplikace zpráva pochází.


## Specifikace

Instrukce doručení prvního fragmentu by byly upraveny následovně:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       Bit order: 76543210
       bity 6-5: typ doručení
                 0x03 = TUNNELS
       bit 0: multicast? Pokud 0, doručit do jednoho z tunelů
                         Pokud 1, doručit do všech tunelů
                         Nastavit na 0 pro kompatibilitu s budoucím použitím,
                         pokud typ doručení není TUNNELS

Count ::
       1 byte
       Volitelné, přítomno, pokud je typ doručení TUNNELS
       2-255 - Počet následujících id/hash párů

Tunnel ID :: TunnelId
To Hash ::
       36 bytes každý
       Volitelné, přítomno, pokud je typ doručení TUNNELS
       id/hash páry

Celková délka: Typická délka je:
       75 bajtů pro doručení TUNNELS s počtem 2 (nefragmentovaná zpráva tunelu);
       79 bajtů pro doručení TUNNELS s počtem 2 (první fragment)

Zbytek instrukcí doručení beze změny
```


## Kompatibilita

Jediní protějšci, kteří musí novou specifikaci rozumět, jsou OBGW a OBEP. Tuto změnu můžeme proto udělat kompatibilní se stávající sítí tím, že použití bude podmíněno cílovou verzí I2P:

* OBGW musí při stavbě odchozích tunelů vybírat kompatibilní OBEPy na základě verze I2P uvedené v jejich [RouterInfo](/docs/specs/common-structures/#routerinfo).

* Protějšci, kteří inzerují cílovou verzi, musí podporovat parsování nových flagů a nesmí odmítat instrukce jako neplatné.


## Reference

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)

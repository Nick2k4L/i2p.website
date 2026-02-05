---
title: "Formát přístupového filtru"
description: "Syntaxe pro soubory filtru řízení přístupu tunnel"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## Přehled

Definice filtru je seznam řetězců. Prázdné řádky a řádky začínající `#` jsou ignorovány. Změny v definici filtru se projeví po restartu tunelu.

Každý řádek může reprezentovat jednu z těchto položek:

- Definice výchozího prahu, který se použije na všechny vzdálené destinace neuvedené v tomto souboru nebo v jakémkoliv z odkazovaných souborů
- Definice prahu, který se použije na konkrétní vzdálenou destinaci
- Definice prahu, který se použije na vzdálené destinace uvedené v souboru
- Definice prahu, který při překročení způsobí, že problémová vzdálená destinace bude zaznamenána do určeného souboru

Pořadí definic má význam. První práh pro danou destinaci (ať už explicitní nebo uvedený v souboru) přepíše jakékoli budoucí prahy pro tutéž destinaci, ať už explicitní nebo uvedené v souboru.

## Prahové hodnoty

Práh je definován počtem pokusů o připojení, které je vzdálené cílové místo oprávněno provést během určeného počtu sekund, než dojde k "porušení". Například následující definice prahu `15/5` znamená, že stejné vzdálené cílové místo může provést 14 pokusů o připojení během 5sekundového období. Pokud provede ještě jeden pokus ve stejném období, práh bude porušen.

Formát prahu může být jeden z následujících:

- **Číselná definice** počtu připojení za počet sekund - `15/5`, `30/60`, atd. Poznamenejme, že pokud je počet připojení 1 (například v `1/1`), první pokus o připojení povede k porušení limitu.
- Slovo **`allow`**. Tento práh není nikdy porušen, tj. je povoleno nekonečné množství pokusů o připojení.
- Slovo **`deny`**. Tento práh je vždy porušen, tj. žádné pokusy o připojení nebudou povoleny.

### Výchozí práh

Výchozí práh se vztahuje na jakékoli vzdálené cíle, které nejsou explicitně uvedeny v definici nebo v žádném z odkazovaných souborů. Pro nastavení výchozího prahu použijte klíčové slovo `default`. Následují příklady výchozích prahů:

```text
15/5 default
allow default
deny default
```
Může existovat pouze jedna definice výchozího prahu na filtr. Pokud je vynechána, filtr bude ve výchozím nastavení povolovat neznámá připojení.

### Explicitní prahové hodnoty

Explicitní prahové hodnoty jsou aplikovány na vzdálený cíl uvedený v samotné definici. Příklady:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### Hromadné prahové hodnoty

Pro pohodlí je možné udržovat seznam destinací v souboru a definovat prahovou hodnotu pro všechny najednou. Příklady:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
Tyto soubory lze upravovat ručně, zatímco tunnel běží. Změny v těchto souborech se mohou projevit až za 10 sekund.

## Záznamníky

Rekordéry sledují pokusy o připojení prováděné vzdálenou destinací, a pokud je překročen určitý práh, tato destinace se zaznamená do daného souboru. Příklady:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
Je možné použít rekordér k zaznamenávání agresivních destinací do daného souboru a poté použít tentýž soubor k jejich omezení. Například následující úryvek definuje filtr, který zpočátku povoluje všechny pokusy o připojení, ale pokud jakákoli jednotlivá destinace překročí 30 pokusů za 5 sekund, bude omezena na 15 pokusů za 5 sekund:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
Je možné použít záznamník v jednom tunnelu, který zapisuje do souboru, jenž reguluje jiný tunnel. Je možné znovu použít stejný soubor s cíli ve více tunnelech. A samozřejmě je možné tyto soubory upravovat ručně.

Zde je příklad definice filtru, který ve výchozím nastavení aplikuje určité omezení rychlosti, žádné omezování pro destinace v souboru `friends.txt`, zakazuje jakékoli připojení z destinací v souboru `enemies.txt` a zaznamenává jakékoli agresivní chování do souboru nazvaného `suspicious.txt`:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```
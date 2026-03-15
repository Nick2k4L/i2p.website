---
title: "Proces návrhov I2P"
number: "001"
author: "str4d"
created: "2016-04-10"
lastupdated: "2017-04-07"
status: "Meta"
thread: "http://zzz.i2p/topics/1980"
toc: true
---
## Přehled

Tento dokument popisuje, jak změnit specifikace I2P, jak fungují návrhy I2P a vztah mezi návrhy I2P a specifikacemi.

Tento dokument je adaptován z procesu návrhů Tor a většina obsahu níže byla původně napsána Nickem Mathewsonem.

Tento je informativní dokument.

## Motivace

Předtím byl náš proces aktualizace specifikací I2P relativně neformální: navrhovali jsme návrh na vývojovém fóru a diskutovali o změnách, poté jsme dosáhli konsensu a opravili specifikaci s návrhy změn (ne nutně v tomto pořadí), a nakonec jsme provedli změny.

To mělo několik problémů.

První, i při nejefektivnějším procesu, specifikace často zůstávaly nesynchronizované s kódem. Nejhorší případy byly ty, kde byla implementace odložena: specifikace a kód mohly zůstat nesynchronizované po několik verzí.

Druhé, bylo obtížné se účastnit diskuse, protože nebylo vždy jasné, které části diskusního vlákna byly součástí návrhu, nebo které změny specifikací byly provedeny. Vývojová fóra jsou navíc přístupná pouze uvnitř I2P, což znamená, že návrhy mohly být zobrazeny pouze lidmi, kteří používají I2P.

Třetí, bylo velmi snadné zapomenout na některé návrhy, protože se pohřbily několik stránek zpět ve fórovém vláknu.

## Jak změnit specifikace nyní

Nejdříve někdo napíše dokument návrhu. Měl by popisovat změnu, která by měla být provedena podrobně, a poskytnout somej ideu, jak ji implementovat. Jakmile je dostatečně rozvinut, stává se návrhem.

Podobně jako RFC, každý návrh dostává číslo. Na rozdíl od RFC, návrhy mohou změnit svůj obsah över čas a zachovat stejné číslo, dokud nejsou konečně přijaty nebo odmítnuty. Historie každého návrhu bude uložena v repozitáři webových stránek I2P.

Jakmile je návrh v repozitáři, měli bychom o něm diskutovat na odpovídajícím vláknu a vylepšovat ho, dokud nedosáhneme konsensu, že je to dobrý nápad, a že je dostatečně podrobný pro implementaci. Když k tomu dojde, implementujeme návrh a začleníme ho do specifikací. Takže specifikace zůstávají kanonickou dokumentací pro protokol I2P: žádný návrh není nikdy kanonickou dokumentací pro implementovanou funkci.

(Tento proces je khá podobný Python Enhancement Process, s hlavní výjimkou, že návrhy I2P se po implementaci znovu začleňují do specifikací, zatímco PEPy se *stávají* novou specifikací.)

### Malé změny

Je stále v pořádku provést malé změny přímo do specifikace, pokud lze kód napsat více nebo méně okamžitě, nebo kosmetické změny, pokud není vyžadována žádná změna kódu. Tento dokument odráží současnou *intent* vývojářů, ne trvalý slib, že budeme vždy používat tento proces v budoucnu: rezervujeme si právo být opravdu nadšení a běžet implementovat něco v noci plné kofeinu nebo M&M.

## Jak se přidávají nové návrhy

Chcete-li předložit návrh, zveřejněte ho na vývojovém fóru nebo vytvořte ticket s připojeným návrhem.

Jakmile je myšlenka navržena, existuje správně formátovaný (viz níže) návrh, a hrubý konsensus uvnitř aktivní vývojářské komunity existuje, že tato myšlenka si zaslouží úvahu, editoři návrhů oficiálně přidají návrh.

Aktuální editoři návrhů jsou zzz a str4d.

## Co by mělo být v návrhu

Každý návrh by měl mít hlavičku obsahující tyto pole:

```
:author:
:created:
:thread:
:lastupdated:
:status:
```

- Pole `author` by mělo obsahovat jména autorů tohoto návrhu.
- Pole `thread` by mělo být odkazem na vývojové fórum vlákno, kde byl tento návrh původně zveřejněn, nebo na nové vlákno vytvořené pro diskusi o tomto návrhu.
- Pole `lastupdated` by mělo být inicializováno jako `created` a mělo by být aktualizováno pokaždé, když je návrh změněn.

Tyto pole by měly být nastaveny, pokud je to nutné:

```
:supercedes:
:supercededby:
:editor:
```

- Pole `supercedes` je čárkou oddělený seznam všech návrhů, které tento návrh nahrazuje. Tyto návrhy by měly být odmítnuty a měly by mít nastavené pole `supercededby` na číslo tohoto návrhu.
- Pole `editor` by mělo být nastaveno, pokud jsou provedeny významné změny tohoto návrhu, které nezmění podstatně jeho obsah. Pokud je obsah podstatně měněn, měl by být přidán další `author` nebo vytvořen nový návrh, který nahrazuje tento.

Tyto pole jsou volitelné, ale doporučené:

```
:target:
:implementedin:
```

- Pole `target` by mělo popisovat, ve které verzi se navrhuje implementovat tento návrh (pokud je Otevřený nebo Přijatý).
- Pole `implementedin` by mělo popisovat, ve které verzi byl tento návrh implementován (pokud je Dokončený nebo Uzavřený).

Tělo návrhu by mělo začínat sekcí Přehled, která vysvětluje, o čem je návrh, co dělá a o jakém stavu se jedná.

Po Přehledu se návrh stává volnějším. V závislosti na jeho délce a složitosti může návrh rozdělit na sekce podle potřeby nebo následovat krátký diskusní formát. Každý návrh by měl obsahovat alespoň následující informace, než je Přijat, i když informace nemusí být v sekcích s těmito názvy.

**Motivace**
: Jaký problém se návrh snaží vyřešit? Proč je tento problém důležitý? Pokud jsou možné several přístupy, proč zvolit tento?

**Design**
: Vysokouhlíkový pohled na nové nebo upravené funkce, jak nové nebo upravené funkce fungují, jak spolu fungují a jak interagují s ostatními částmi I2P. Toto je hlavní tělo návrhu. Některé návrhy budou začínat pouze s Motivací a Designem a budou čekat na specifikaci, dokud Design nebude přibližně správný.

**Bezpečnostní důsledky**
: Jaké účinky mohou mít navrhované změny na anonymitu, jak jsou tyto účinky dobře pochopeny a tak dále.

**Specifikace**
: Podrobný popis toho, co je třeba přidat do specifikací I2P, aby se návrh implementoval. Toto by mělo být v přibližně stejné podrobnosti, jako budou specifikace obsahovat: mělo by být možné pro nezávislé programátory napsat vzájemně kompatibilní implementace návrhu na základě jeho specifikací.

**Kompatibilita**
: Budou verze I2P, které budou následovat tento návrh, kompatibilní s verzemi, které nebudou? Pokud ano, jak bude kompatibilita dosažena? Obecně se snažíme nedropovat kompatibilitu, pokud je to možné; jsme neudělali "flag day" změnu od března 2008 a nechceme udělat další.

**Implementace**
: Pokud bude návrh obtížně implementovatelný v současné architektuře I2P, dokument může obsahovat somej diskusi o tom, jak to provést. Skutečné patche by měly být na veřejných monotone větvích nebo nahrány do Trac.

**Poznámky k výkonu a škálovatelnosti**
: Pokud bude funkce mít účinek na výkon (v RAM, CPU, šířce pásma) nebo škálovatelnost, mělo by být somej analýzy toho, jak významný bude tento účinek, aby se zabránilo skutečným regresím výkonu a aby se neztrácel čas na zanedbatelné zisky.

**Reference**
: Pokud návrh odkazuje na vnější dokumenty, měly by být tyto dokumenty uvedeny.

## Stav návrhu

**Otevřený**
: Návrh pod diskusí.

**Přijatý**
: Návrh je kompletní a chceme ho implementovat. Po tomto bodě by se měly podstatné změny návrhu vyhnout a považovat za znamení, že proces selhal někde.

**Dokončený**
: Návrh byl přijat a implementován. Po tomto bodě by se neměl návrh měnit.

**Uzavřený**
: Návrh byl přijat, implementován a sloučen do hlavních specifikačních dokumentů. Návrh by se neměl měnit po tomto bodě.

**Odmítnutý**
: Nechceme implementovat funkci tak, jak je popsána zde, i když můžeme udělat somej jinou verzi. Viz poznámky v dokumentu pro podrobnosti. Návrh by se neměl měnit po tomto bodě; aby se přinesla somej jiná verze myšlenky, napište nový návrh.

**Návrh**
: Tento návrh ještě není kompletní; existují určité chybějící části. Prosím, nepřidávejte žádné nové návrhy se stavem; umístěte je do podsložky "ideas" místo toho.

**Potřebuje revizi**
: Nápad pro návrh je dobrý, ale návrh, jak je popsán, má vážné problémy, které brání jeho přijetí. Viz poznámky v dokumentu pro podrobnosti.

**Mrtvý**
: Návrh nebyl dotčen po dlouhou dobu a nezdá se, že by někdo chtěl dokončit ho brzy. Může se stát "Otevřeným" znovu, pokud získá nového protagonistu.

**Potřebuje výzkum**
: Existují výzkumné problémy, které je třeba vyřešit, bevor je jasné, zda je návrh dobrý.

**Meta**
: Toto není návrh, ale dokument o návrzích.

**Rezervní**
: Tento návrh není něco, co plánujeme implementovat, ale mohli bychom ho obnovit někdy v budoucnu, pokud se rozhodneme udělat něco podobného.

**Informativní**
: Tento návrh je poslední slovo o tom, co dělá. Není možné ho změnit na specifikaci, pokud někdo nezkopíruje a nevloží ho do nové specifikace pro nový subsystém.

Editoři udržují správný stav návrhů na základě hrubého konsensu a své vlastní diskrece.

## Číslování návrhů

Čísla 000-099 jsou rezervována pro speciální a meta-návrhy. 100 a výše jsou používána pro skutečné návrhy. Čísla nejsou recyklována.

## Reference

* [DEV-FORUM-PROPOSAL](http://zzz.i2p/topics/new?forum_id=7-big-topics-ideas-proposals-and-discussion)
* [TORSPEC-PROCESS](https://gitweb.torproject.org/torspec.git/tree/proposals/001-process.txt)
* [TRAC-PROPOSAL](http://trac.i2p2.i2p/newticket?summary=New%20proposal:%20&type=enhancement&milestone=n/a&component=www/i2p&keywords=review-needed)

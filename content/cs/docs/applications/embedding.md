---
title: "Zabudování I2P do vaší aplikace"
description: "Pokyny pro přibalení I2P routeru s vaší aplikací"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## Přehled

Tato stránka je o zabalení celého binárního souboru I2P router do vaší aplikace. Nejedná se o psaní aplikace pro práci s I2P (ať už zabalené nebo externí). Nicméně mnoho z těchto pokynů může být užitečných i v případě, že router nezabalujete.

Mnoho projektů začleňuje nebo uvažuje o začlenění I2P. To je skvělé, pokud se to dělá správně. Pokud se to dělá špatně, může to způsobit skutečnou škodu naší síti. I2P router je komplexní a může být výzvou skrýt všechnu tuto složitost před vašimi uživateli. Tato stránka popisuje některé obecné pokyny.

Většina těchto pokynů platí stejně pro Java I2P nebo i2pd. Některé pokyny jsou však specifické pro Java I2P a jsou uvedeny níže.

### Kontaktujte nás

Začněte dialog. Jsme tu, abychom pomohli. Aplikace, které integrují I2P, jsou pro nás nejslibnější - a nejzajímavější - příležitostí, jak rozšířit síť a zlepšit anonymitu pro všechny.

### Vyberte svůj router moudře

Pokud je vaše aplikace v Javě nebo Scale, je to snadná volba - použijte Java router. Pokud v C/C++, doporučujeme i2pd. Vývoj i2pcpp byl zastaven. Pro aplikace v jiných jazycích je nejlepší použít SAM nebo BOB nebo SOCKS a přibalit Java router jako samostatný proces. Některé z následujících informací platí pouze pro Java router.

### Licencování

Ujistěte se, že splňujete licenční požadavky softwaru, který balíčkujete.

---

## Konfigurace

### Ověřit výchozí konfiguraci

Správná výchozí konfigurace je klíčová. Většina uživatelů nezmění výchozí nastavení. Výchozí hodnoty pro vaši aplikaci se mohou lišit od výchozích hodnot pro router, který balíte. V případě potřeby přepište výchozí nastavení routeru.

Některé důležité výchozí hodnoty ke kontrole: maximální šířka pásma, množství a délka tunnelů, maximální počet účastnických tunnelů. Mnoho z toho závisí na očekávané šířce pásma a vzorcích použití vaší aplikace.

Nakonfigurujte dostatečnou šířku pásma a tunely, aby vaši uživatelé mohli přispívat do sítě. Zvažte zakázání externího I2CP, protože ho pravděpodobně nepotřebujete a mohlo by to kolidovat s jakoukoli jinou běžící instancí I2P. Podívejte se také například na konfigurace pro zakázání ukončování JVM při ukončení programu.

### Úvahy o účastnickém provozu

Může být lákavé zakázat participující provoz. Existuje několik způsobů, jak to udělat (skrytý režim, nastavení maximálního počtu tunnelů na 0, nastavení sdílené šířky pásma pod 12 KBytes/sec). Bez participujícího provozu se nemusíte starat o elegantní vypnutí, vaši uživatelé nevidí využití šířky pásma, které negenerují oni sami, atd. Nicméně existuje mnoho důvodů, proč byste měli povolit participující tunnely.

Především router nefunguje tak dobře, pokud nemá možnost se "integrovat" se sítí, což je výrazně podpořeno tím, když ostatní budují tunnely skrze vás.

Zadruhé, přes 90 % routerů v současné síti umožňuje přenos cizích dat. To je výchozí nastavení v Java routeru. Pokud vaše aplikace neroute pro ostatní a stane se opravdu populární, pak je parazitem sítě a narušuje rovnováhu, kterou teď máme. Pokud se stane opravdu velkou, pak se staneme Torem a budeme trávit čas žebráním o to, aby lidé povolili přenos dat.

Za třetí, procházející provoz slouží jako krycí provoz, který pomáhá anonymitě vašich uživatelů.

Důrazně nedoporučujeme, abyste ve výchozím nastavení zakázali participující provoz. Pokud to uděláte a vaše aplikace se stane velmi populární, mohlo by to poškodit síť.

### Perzistence

Musíte uložit data routeru (netDb, konfiguraci, atd.) mezi jednotlivými spuštěními routeru. I2P nefunguje dobře, pokud musíte při každém spuštění provádět reseed, což představuje obrovskou zátěž pro naše reseed servery a také to není příliš dobré pro anonymitu. I když dodáte router infos, I2P potřebuje uložená profilová data pro nejlepší výkon. Bez persistence budou mít vaši uživatelé špatný zážitek při spouštění.

Existují dvě možnosti, pokud nemůžete zajistit trvalost dat. Obě tyto možnosti eliminují zátěž vašeho projektu na naše reseed servery a výrazně zlepší čas spuštění.

1) Nastavte si vlastní projektové reseed servery, které poskytují mnohem více než obvyklý počet router info v resedu, řekněme několik stovek. Nakonfigurujte router tak, aby používal pouze vaše servery.

2) Zabalte jednu až dva tisíce router infos do vašeho instalátoru.

Také odložte nebo rozložte spuštění vašich tunelů v čase, abyste dali routeru šanci se integrovat před vybudováním velkého množství tunelů.

### Konfigurovatelnost

Poskytněte svým uživatelům způsob, jak měnit konfiguraci důležitých nastavení. Chápeme, že pravděpodobně budete chtít skrýt většinu složitosti I2P, ale je důležité zobrazit některá základní nastavení. Kromě výše uvedených výchozích hodnot mohou být užitečná některá síťová nastavení jako UPnP, IP/port.

### Úvahy o floodfill

Nad určitým nastavením šířky pásma a při splnění dalších kritérií stavu se váš router stane floodfill, což může způsobit značné zvýšení počtu připojení a využití paměti (alespoň u Java routeru). Zamyslete se, zda je to v pořádku. Můžete floodfill zakázat, ale pak vaši nejrychlejší uživatelé nepřispívají tím, čím by mohli. Záleží také na typické době provozu vaší aplikace.

### Reseeding

Rozhodněte se, zda budete sdružovat router infos nebo používat naše reseed hosty. Seznam Java reseed hostů je ve zdrojovém kódu, takže pokud budete udržovat zdrojový kód aktuální, seznam hostů bude také aktuální. Uvědomte si možné blokování nepřátelskými vládami.

### Použít sdílené klienty

Java I2P i2ptunnel podporuje sdílené klienty, kde klienti mohou být nakonfigurováni k použití jednoho fondu. Pokud potřebujete více klientů a je-li to v souladu s vašimi bezpečnostními cíli, nakonfigurujte klienty jako sdílené.

### Omezit počet tunelů

Specifikujte množství tunnelů explicitně pomocí možností `inbound.quantity` a `outbound.quantity`. Výchozí hodnota v Java I2P je 2; výchozí hodnota v i2pd je vyšší. Specifikujte v řádku SESSION CREATE pomocí SAM pro získání konzistentních nastavení u obou routerů. Dva tunnely pro každý směr (dovnitř/ven) jsou dostačující pro většinu aplikací s nízkou až střední šířkou pásma a nízkým až středním rozvětvením. Servery a P2P aplikace s vysokým rozvětvením mohou potřebovat více. Pro návod na výpočet požadavků pro servery a aplikace s vysokým provozem se podívejte na [tento příspěvek na fóru](http://zzz.i2p/topics/1584).

### Specifikujte SAM SIGNATURE_TYPE

SAM standardně používá pro destinace DSA_SHA1, což není to, co chcete. Ed25519 (typ 7) je správná volba. Přidejte SIGNATURE_TYPE=7 k příkazu DEST GENERATE, nebo k příkazu SESSION CREATE pro DESTINATION=TRANSIENT.

### Omezit SAM relace

Většina aplikací bude potřebovat pouze jednu SAM session. SAM poskytuje možnost rychle zahlcovat lokální router, nebo dokonce širší síť, pokud je vytvořen velký počet session. Pokud může více podslužeb používat jednu session, nastavte je s PRIMARY session a SUBSESSIONS (v současnosti není podporováno v i2pd). Rozumný limit pro session je 3 nebo 4 celkem, nebo možná až 10 ve vzácných situacích. Pokud máte více session, nezapomeňte pro každou specifikovat nízký počet tunnelů, viz výše.

Téměř v žádné situaci byste neměli potřebovat jedinečnou session pro každé připojení. Bez pečlivého návrhu by to mohlo rychle způsobit DDoS útok na síť. Pečlivě zvažte, zda vaše bezpečnostní cíle vyžadují jedinečné sessions. Před implementací sessions per-connection se prosím poraďte s vývojáři Java I2P nebo i2pd.

### Snížení využití síťových prostředků

Upozorňujeme, že tyto možnosti nejsou v současnosti podporovány v i2pd. Tyto možnosti jsou podporovány prostřednictvím I2CP a SAM (kromě delay-open, které je pouze přes i2ptunnel). Podrobnosti najdete v dokumentaci I2CP (a pro delay-open v konfigurační dokumentaci i2ptunnel).

Zvažte nastavení vašich aplikačních tunnelů na delay-open, reduce-on-idle a/nebo close-on-idle. Toto je jednoduché při použití i2ptunnel, ale pokud používáte I2CP přímo, budete si muset část implementovat sami. Podívejte se na i2psnark pro kód, který snižuje počet tunnelů a poté tunnel uzavře, a to i při přítomnosti určité aktivity DHT na pozadí.

---

## Životní cyklus

### Aktualizovatelnost

Pokud je to vůbec možné, zahrňte funkci automatické aktualizace, nebo alespoň automatické oznámení o nové verzi. Naší největší obavou je obrovské množství routerů, které nelze aktualizovat. Máme asi 6-8 vydání ročně Java routeru a je kritické pro zdraví sítě, aby uživatelé drželi krok. Obvykle máme přes 80 % sítě na nejnovějším vydání během 6 týdnů po vydání a rádi bychom si to udrželi. Nemusíte si dělat starosti s deaktivací vestavěné funkce automatické aktualizace routeru, protože tento kód je v router console, kterou pravděpodobně nebalíte.

### Nasazení

Mějte postupný plán nasazení. Nezahlťte síť najednou. V současnosti máme přibližně 25 tisíc unikátních uživatelů denně a 40 tisíc unikátních za měsíc. Pravděpodobně jsme schopni zvládnout růst 2-3× ročně bez větších problémů. Pokud očekáváte rychlejší nárůst než tento, NEBO je distribuce šířky pásma (nebo distribuce provozního času, nebo jakákoli jiná významná charakteristika) vaší uživatelské základny výrazně odlišná od naší současné uživatelské základny, opravdu si musíme promluvit. Čím větší jsou vaše růstové plány, tím důležitější je vše ostatní v tomto kontrolním seznamu.

### Navrhujte pro dlouhé provozní časy a podporujte je

Řekněte svým uživatelům, že I2P funguje nejlépe, pokud stále běží. Po spuštění může trvat několik minut, než bude fungovat dobře, a ještě déle po první instalaci. Pokud je vaše průměrná doba provozu kratší než hodina, I2P pravděpodobně není správné řešení.

---

## Uživatelské rozhraní

### Zobrazit stav

Poskytněte uživateli nějakou indikaci, že aplikační tunnely jsou připraveny. Vyžadujte trpělivost.

### Elegantní vypnutí

Pokud je to možné, odložte vypnutí, dokud nevyprší vaše participující tunnely. Neumožněte uživatelům snadno přerušit tunnely, nebo je alespoň požádejte o potvrzení.

### Vzdělávání a dary

Bylo by hezké, kdybyste svým uživatelům poskytli odkazy, kde se mohou dozvědět více o I2P a kde mohou přispět.

### Možnost externího routeru

V závislosti na vaší uživatelské základně a aplikaci může být užitečné poskytnout možnost nebo samostatný balíček pro použití externího router.

---

## Ostatní témata

### Použití dalších běžných služeb

Pokud plánujete používat nebo odkazovat na další běžné I2P služby (news feedy, hosts.txt odběry, trackery, outproxy, atd.), ujistěte se, že je nepřetěžujete, a promluvte si s lidmi, kteří je provozují, abyste se ujistili, že je to v pořádku.

### Problémy s časem / NTP

Poznámka: Tato sekce se vztahuje na Java I2P. i2pd neobsahuje SNTP klienta.

I2P obsahuje SNTP klienta. I2P vyžaduje správný čas pro fungování. Dokáže kompenzovat posunuté systémové hodiny, ale to může zpozdit spuštění. Můžete zakázat SNTP dotazy I2P, ale to se nedoporučuje, pokud si vaše aplikace nezajistí, že systémové hodiny jsou správné.

### Vyberte si, co a jak zabalit

Poznámka: Tato sekce se vztahuje pouze na Java I2P.

Minimálně budete potřebovat i2p.jar, router.jar, streaming.jar a mstreaming.jar. U aplikací pouze pro datagramy můžete vynechat dva streaming jary. Některé aplikace mohou potřebovat více, např. i2ptunnel.jar nebo addressbook.jar. Nezapomeňte na jbigi.jar, nebo jeho podmnožinu pro platformy, které podporujete, aby byla kryptografie mnohem rychlejší. Pro sestavení je vyžadována Java 7 nebo vyšší. Pokud vytváříte balíčky pro Debian / Ubuntu, měli byste vyžadovat balíček I2P z našeho PPA místo jeho přibalování. Téměř jistě nebudete potřebovat například susimail, susidns, router console a i2psnark.

Následující soubory by měly být zahrnuty v instalačním adresáři I2P, který je specifikován vlastností "i2p.dir.base". Nezapomeňte na adresář certificates/, který je požadován pro reseeding, a blocklist.txt pro validaci IP adres. Adresář geoip je volitelný, ale doporučený, aby router mohl činit rozhodnutí na základě lokace. Pokud zahrnujete geoip, nezapomeňte umístit soubor GeoLite2-Country.mmdb do tohoto adresáře (rozbalte jej z installer/resources/GeoLite2-Country.mmdb.gz). Soubor hosts.txt může být nezbytný, můžete jej upravit tak, aby zahrnoval všechny hosty, které vaše aplikace používá. Můžete přidat soubor router.config do základního adresáře pro přepsání počátečních výchozích hodnot. Zkontrolujte a upravte nebo odstraňte soubory clients.config a i2ptunnel.config.

Licenční požadavky mohou vyžadovat, abyste zahrnuli soubor LICENSES.txt a adresář licenses.

- Možná budete také chtít přibalit soubor hosts.txt.
- Nezapomeňte specifikovat bootclasspath, pokud kompilujete Java I2P pro vaše vydání, místo použití našich binárních souborů.

### Úvahy o Androidu

Poznámka: Tato sekce se vztahuje pouze na Java I2P.

Naše Android router aplikace může být sdílena více klienty. Pokud není nainstalována, uživatel bude vyzván k instalaci při spuštění klientské aplikace.

Někteří vývojáři vyjádřili obavy, že se jedná o špatnou uživatelskou zkušenost, a chtějí router integrovat do své aplikace. Máme v našem plánu knihovnu služby Android routeru, která by mohla usnadnit integraci. Jsou potřeba další informace.

Pokud potřebujete pomoc, prosím kontaktujte nás.

### Maven JAR soubory

Poznámka: Tato sekce se vztahuje pouze na Java I2P.

Máme omezený počet našich jar souborů na [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22). Existuje mnoho trac tiketů, které musíme vyřešit, aby se zlepšily a rozšířily vydané jar soubory na Maven Central.

Pokud potřebujete pomoc, kontaktujte nás prosím.

### Úvahy o datagramech (DHT)

Pokud vaše aplikace používá I2P datagramy, např. pro DHT, je k dispozici mnoho pokročilých možností pro snížení režie a zvýšení spolehlivosti. Může to chvíli trvat a vyžadovat experimentování, než to bude správně fungovat. Uvědomte si kompromisy mezi velikostí a spolehlivostью. Obraťte se na nás o pomoc. Je možné - a doporučuje se - používat datagramy a streamování na stejné destinaci. Nevytvářejte pro to samostatné destinace. Nepokoušejte se ukládat vaše nesouvisející data do stávajících síťových DHT (iMule, bote, bittorrent a router). Vytvořte si vlastní. Pokud natvrdo kódujete seed uzly, doporučujeme, abyste jich měli několik.

### Outproxy

I2P outproxy do clearnet jsou omezený zdroj. Používejte outproxy pouze pro běžné webové prohlížení iniciované uživatelem nebo jiný omezený provoz. Pro jakékoli jiné použití se poraďte s operátorem outproxy a získejte jeho souhlas.

### Komarketing

Pracujme společně. Nečekejte, až bude hotovo. Dejte nám svůj Twitter účet a začněte o tom tweetovat, oplatíme vám to.

### Malware

Prosím, nepoužívejte I2P ke zlým účelům. Mohlo by to způsobit velkou škodu jak naší síti, tak naší pověsti.

### Přidejte se k nám

To může být zřejmé, ale připojte se ke komunitě. Provozujte I2P 24/7. Založte I2P Site o vašem projektu. Trávte čas na IRC #i2p-dev. Přispívejte na fóra. Šiřte povědomí. Můžeme vám pomoci získat uživatele, testery, překladatele nebo dokonce programátory.

---

## Příklady

### Příklady aplikací

Možná si budete chtít nainstalovat a vyzkoušet I2P Android aplikaci a podívat se na její kód jako na příklad aplikace, která obsahuje router. Podívejte se, co uživateli zpřístupňujeme a co skrýváme. Prohlédněte si stavový automat, který používáme ke spuštění a zastavení routeru. Další příklady jsou: Vuze, Nightweb Android aplikace, iMule, TAILS, iCloak a Monero.

### Příklad kódu

Poznámka: Tato sekce se týká pouze Java I2P.

Nic z výše uvedeného vám vlastně neříká, jak napsat kód pro zabalení Java routeru, takže následuje stručný příklad.

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
Tento kód je pro případ, kdy vaše aplikace spustí router, jako v naší Android aplikaci. Můžete také nechat router spustit aplikaci prostřednictvím souborů clients.config a i2ptunnel.config spolu s Jetty webapps, jak se to dělá v našich Java balíčcích. Jako vždy je správa stavu složitá část.

Viz také: [javadocs routeru](http://idk.i2p/javadoc-i2p/net/i2p/router/Router.html).

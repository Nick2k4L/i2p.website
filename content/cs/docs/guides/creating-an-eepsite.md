---
title: "Vytvoření I2P Eepsite"
description: "Naučte se, jak vytvořit a hostovat svůj vlastní web v síti I2P pomocí vestavěného webového serveru Jetty"
lastUpdated: "2025-11"
toc: true
---

## Co je to Eepsite?

**eepsite** je web, který funguje výhradně v síti I2P. Na rozdíl od tradičních webů dostupných přes clearnet (veřejný internet) jsou eepsites dosažitelné pouze přes I2P, což poskytuje anonymitu a soukromí jak provozovateli, tak návštěvníkům. Eepsites používají pseudo-doménu nejvyšší úrovně `.i2p` a přistupuje se k nim prostřednictvím speciálních adres `.b32.i2p` nebo lidsky čitelných jmen registrovaných v adresáři I2P.

Všechna nasazení Java I2P mají [Jetty](https://jetty.org/index.html), lehký webový server založený na Javě, předinstalovaný a předkonfigurovaný. Díky tomu je snadné během několika minut začít hostovat vlastní eepsite - není nutná žádná další instalace softwaru.

Tento průvodce vás provede procesem vytvoření a konfigurace vašeho prvního eepsite pomocí vestavěných nástrojů I2P.

---

## Krok 1: Otevřete Správce skrytých služeb

Správce skrytých služeb (také nazývaný I2P Tunnel Manager) je místo, kde konfigurujete všechny I2P tunnels pro servery i klienty, včetně HTTP serverů (eepsites).

1. Otevřete svou `http://127.0.0.1:7657`
2. Přejděte na `http://127.0.0.1:7657/i2ptunnelmgr`

Měli byste vidět rozhraní Správce skrytých služeb, které zobrazuje: - **Stavové zprávy** - Aktuální stav tunnel a klienta - **Globální ovládání tunnel** - Tlačítka pro správu všech tunnels najednou - **I2P Skryté služby** - Seznam nakonfigurovaných serverových tunnels

![Správce skrytých služeb](/images/guides/eepsite/hidden-services-manager.png)

Ve výchozím nastavení uvidíte existující položku **I2P webový server** nakonfigurovanou, ale nespuštěnou. Jedná se o předem nakonfigurovaný webový server Jetty, připravený k použití.

---

## Krok 2: Nakonfigurujte nastavení vašeho serveru Eepsite

Klikněte na položku **I2P webserver** v seznamu Skrytých služeb a otevřete stránku s konfigurací serveru. Zde si upravíte nastavení svého eepsite.

![Nastavení serveru Eepsite](/images/guides/eepsite/webserver-settings.png)

### Vysvětlení možností konfigurace

**Název** - Toto je interní identifikátor pro váš tunnel - Hodí se, pokud provozujete více eepsites, abyste měli přehled, která je která - Výchozí: "I2P webserver"

**Popis** - Stručný popis vašeho eepsite pro vaši vlastní potřebu - Viditelné pouze vám ve Správci skrytých služeb - Příklad: "Můj eepsite" nebo "Osobní blog"

**Automatické spuštění tunnel** - **Důležité**: Zaškrtněte toto políčko, aby se váš eepsite automaticky spustil, když se spustí váš I2P router - Zajistí, že váš eepsite zůstane dostupný bez ručního zásahu, i když se router znovu spustí - Doporučeno: **Povoleno**

**Cíl (hostitel a port)** - **Hostitel**: Místní adresa, na které běží váš webový server (výchozí: `127.0.0.1`) - **Port**: Port, na kterém váš webový server naslouchá (výchozí: `7658` pro Jetty) - Pokud používáte předinstalovaný webový server Jetty, **ponechte je na výchozích hodnotách** - Měňte je pouze v případě, že provozujete vlastní webový server na jiném portu

**Název hostitele webu** - Toto je čitelný název domény `.i2p` vašeho eepsite - Výchozí: `mysite.i2p` (zástupný název) - Můžete si zaregistrovat vlastní doménu jako `stormycloud.i2p` nebo `myblog.i2p` - Nechte prázdné, pokud chcete používat pouze automaticky generovanou adresu `.b32.i2p` (pro outproxies (výstupní proxy)) - Viz níže [Registrace vaší I2P domény](#registering-your-i2p-domain), kde se dozvíte, jak získat vlastní název hostitele

**Místní destinace** - Toto je jedinečný kryptografický identifikátor (adresa destinace) vašeho eepsite - Automaticky generován při prvním vytvoření tunnel - Představte si to jako trvalou "IP adresu" vašeho webu na I2P - Dlouhý alfanumerický řetězec je kódovaná podoba `.b32.i2p` adresy vašeho webu

**Soubor soukromého klíče** - Umístění, kde jsou uloženy soukromé klíče vašeho eepsite - Výchozí: `eepsite/eepPriv.dat` - **Tento soubor udržujte v bezpečí** - kdokoli s přístupem k tomuto souboru se může vydávat za váš eepsite - Nikdy tento soubor nesdílejte ani nemažte

### Důležitá poznámka

Žlutý varovný rámeček vám připomíná, že pro povolení generování QR kódů nebo funkcí ověřování při registraci musíte nakonfigurovat Název hostitele webu s příponou `.i2p` (např. `mynewsite.i2p`).

---

## Krok 3: Pokročilé síťové možnosti (volitelné)

Pokud na stránce s nastavením posunete dolů, najdete pokročilá síťová nastavení. **Tato nastavení jsou volitelná** - výchozí nastavení fungují dobře pro většinu uživatelů. Nicméně je můžete upravit podle svých požadavků na zabezpečení a výkon.

### Možnosti délky pro Tunnel

![Možnosti délky a počtu pro Tunnel](/images/guides/eepsite/tunnel-options.png)

**Délka tunnelu** - **Výchozí**: tunnel o 3 skocích (vysoká anonymita) - Určuje, kolika skoky mezi routery požadavek prochází, než dorazí k vašemu eepsite - **Více skoků = vyšší anonymita, ale pomalejší výkon** - **Méně skoků = rychlejší výkon, ale nižší anonymita** - Možnosti sahají od 0-3 skoků s nastavením odchylky - **Doporučení**: ponechte 3 skoky, pokud nemáte specifické požadavky na výkon

**Variabilita tunnelu** - **Výchozí**: variabilita 0 hopů (bez náhodnosti, konzistentní výkon) - Přidává náhodnost do délky tunnelu pro vyšší bezpečnost - Příklad: "0-1 hop variance" znamená, že délka tunnelu bude náhodně 3 nebo 4 hopy - Zvyšuje nepředvídatelnost, ale může způsobit nekonzistentní časy načítání

### Možnosti počtu Tunnel

**Počet (Inbound/Outbound Tunnels)** - **Výchozí**: 2 inbound, 2 outbound tunnels (standardní šířka pásma a spolehlivost) - Určuje, kolik paralelních tunnels je vyhrazeno pro vaši eepsite - **Více tunnels = Lepší dostupnost a zvládání zátěže, ale vyšší využití prostředků** - **Méně tunnels = Nižší využití prostředků, ale snížená redundance** - Doporučeno pro většinu uživatelů: 2/2 (výchozí) - Weby s vysokým provozem mohou těžit z 3/3 nebo vyšší hodnoty

**Počet záložních tunnels** - **Výchozí**: 0 záložních tunnels (žádná redundance, žádné další využití prostředků) - Pohotovostní tunnels, které se aktivují, pokud primární tunnels selžou - Zvyšuje spolehlivost, ale spotřebovává více šířky pásma a CPU - Většina osobních eepsites nepotřebuje záložní tunnels

### Limity POST

![Konfigurace limitů POST](/images/guides/eepsite/post-limits.png)

Pokud váš eepsite obsahuje formuláře (kontaktní formuláře, sekce komentářů, nahrávání souborů apod.), můžete nakonfigurovat limity požadavků POST, abyste zabránili zneužívání:

**Limity na klienta** - **Za období**: Maximální počet požadavků od jednoho klienta (výchozí: 6 za 5 minut) - **Doba blokování**: Jak dlouho blokovat zneužívající klienty (výchozí: 20 minut)

**Celkové limity** - **Celkem**: Maximální počet požadavků POST ze všech klientů dohromady (výchozí: 20 během 5 minut) - **Doba blokace**: Jak dlouho odmítat všechny požadavky POST, pokud je limit překročen (výchozí: 10 minut)

**Interval omezení POST** - Časové okno pro měření míry požadavků (výchozí: 5 minut)

Tato omezení pomáhají chránit před spamem, útoky typu odepření služby (denial-of-service) a zneužíváním automatizovaného odesílání formulářů.

### Kdy upravit pokročilá nastavení

- **Komunitní web s vysokým provozem**: Zvyšte počet tunnelů (3-4 příchozí/odchozí)
- **Výkonově kritická aplikace**: Snižte délku tunnelu na 2 skoky (kompromis v oblasti soukromí)
- **Vyžadována maximální anonymita**: Zachovejte 3 skoky, přidejte 0-1 odchylku
- **Formuláře s legitimně vysokým využitím**: Podle toho zvyšte limity pro POST
- **Osobní blog/portfolio**: Použijte všechny výchozí hodnoty

---

## Krok 4: Přidání obsahu do vaší eepsite

Nyní, když je vaše eepsite nakonfigurována, musíte přidat soubory svého webu (HTML, CSS, obrázky apod.) do kořenového adresáře dokumentů webového serveru. Umístění se liší podle vašeho operačního systému, typu instalace a implementace I2P.

### Zjištění vašeho kořenového adresáře webu

**Kořenový adresář** (často nazývaný `docroot`) je složka, do níž umisťujete všechny soubory svého webu. Váš soubor `index.html` by měl být umístěn přímo v této složce.

#### Java I2P (Standardní distribuce)

**Linux** - **Standardní instalace**: `~/.i2p/eepsite/docroot/` - **Instalace z balíčku (běžící jako služba)**: `/var/lib/i2p/i2p-config/eepsite/docroot/`

**Windows** - **Standardní instalace**: `%LOCALAPPDATA%\I2P\eepsite\docroot\`   - Typická cesta: `C:\Users\YourUsername\AppData\Local\I2P\eepsite\docroot\` - **Instalace jako služba Windows**: `%PROGRAMDATA%\I2P\eepsite\docroot\`   - Typická cesta: `C:\ProgramData\I2P\eepsite\docroot\`

**macOS** - **Standardní instalace**: `/Users/YourUsername/Library/Application Support/i2p/eepsite/docroot/`

#### I2P+ (vylepšená distribuce I2P)

I2P+ používá stejnou adresářovou strukturu jako Java I2P. Řiďte se výše uvedenými cestami podle svého operačního systému.

#### i2pd (Implementace v C++)

**Linux/Unix** - **Výchozí**: `/var/lib/i2pd/eepsite/` nebo `~/.i2pd/eepsite/` - Zkontrolujte svůj konfigurační soubor `i2pd.conf` a ověřte aktuální nastavení `root` v oddílu pro váš HTTP server tunnel

**Windows** - Zkontrolujte `i2pd.conf` ve vašem instalačním adresáři i2pd

**macOS** - Obvykle: `~/Library/Application Support/i2pd/eepsite/`

### Přidání souborů vašeho webu

1. **Přejděte do svého kořenového adresáře dokumentů** pomocí správce souborů nebo terminálu
2. **Vytvořte nebo zkopírujte soubory svého webu** do složky `docroot`
   - Alespoň vytvořte soubor `index.html` (to je vaše domovská stránka)
   - Podle potřeby přidejte CSS, JavaScript, obrázky a další statické soubory
3. **Uspořádejte podadresáře** tak, jak byste to udělali u libovolného webu:
   ```
   docroot/
   ├── index.html
   ├── about.html
   ├── css/
   │   └── style.css
   ├── images/
   │   └── logo.png
   └── js/
       └── script.js
   ```

### Rychlý start: Jednoduchý příklad HTML

Pokud právě začínáte, vytvořte základní soubor `index.html` ve své složce `docroot`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My I2P Eepsite</title>
</head>
<body>
    <h1>Welcome to My Eepsite!</h1>
    <p>This is my first website on the I2P network.</p>
    <p>Privacy-focused and decentralized!</p>
</body>
</html>
```
### Oprávnění (Linux/Unix/macOS)

Pokud spouštíte I2P jako službu nebo pod jiným uživatelem, ujistěte se, že proces I2P má k vašim souborům oprávnění ke čtení:

```bash
# Set appropriate ownership (if running as i2p user)
sudo chown -R i2p:i2p /var/lib/i2p/i2p-config/eepsite/docroot/

# Or set readable permissions for all users
chmod -R 755 ~/.i2p/eepsite/docroot/
```
### Tipy

- **Výchozí obsah**: Když si poprvé nainstalujete I2P, ve složce `docroot` už je ukázkový obsah - klidně ho nahraďte
- **Statické weby fungují nejlépe**: Ačkoli Jetty podporuje servlety a JSP, jednoduché weby v HTML/CSS/JavaScriptu se nejlépe udržují
- **Externí webové servery**: Pokročilí uživatelé mohou provozovat vlastní webové servery (Apache, Nginx, Node.js, atd.) na různých portech a nasměrovat na ně I2P tunnel

---

## Krok 5: Spuštění vašeho Eepsite

Nyní, když je váš eepsite nakonfigurován a má obsah, je čas jej spustit a zpřístupnit v síti I2P.

### Spustit Tunnel

1. **Vraťte se do `http://127.0.0.1:7657/i2ptunnelmgr`**
2. Najděte v seznamu položku svého **I2P webového serveru**
3. Klikněte na tlačítko **Start** ve sloupci Ovládání

![Spuštěný Eepsite](/images/guides/eepsite/eepsite-running.png)

### Počkejte, až se tunnel naváže

Po kliknutí na Start se váš eepsite tunnel začne sestavovat. Tento proces obvykle trvá **30–60 sekund**. Sledujte indikátor stavu:

- **Červené světlo** = Tunnel se spouští/buduje
- **Žluté světlo** = Tunnel je částečně navázán
- **Zelené světlo** = Tunnel je plně funkční a připraven

Jakmile uvidíte **zelené světlo**, váš eepsite je dostupný v síti I2P!

### Přístup k vašemu eepsite

Klikněte na tlačítko **Preview** vedle vašeho spuštěného eepsite (I2P webová stránka). Tím se otevře nová karta prohlížeče s adresou vašeho eepsite.

Vaše eepsite má dva typy adres:

1. **Base32 adresa (.b32.i2p)**: Dlouhá kryptografická adresa, která vypadá takto:
   ```
   `http://fcyianvr325tdgiiueyg4rsq4r5iuibzovl26msox5ryoselykpq.b32.i2p`
   ```
   - Toto je trvalá, kryptograficky odvozená adresa vaší eepsite (web na I2P)
   - Nelze ji změnit a je svázána s vaším soukromým klíčem
   - Funguje vždy, i bez registrace domény

2. **Lidsky čitelná doména (.i2p)**: Pokud nastavíte název hostitele webu (např. `testwebsite.i2p`)
   - Funguje až po registraci domény (viz následující část)
   - Snadněji se pamatuje a sdílí
   - Mapuje se na vaši adresu .b32.i2p

Tlačítko **Copy Hostname** vám umožní rychle zkopírovat celou vaši adresu `.b32.i2p` ke sdílení.

---

## ⚠️ Kritické: Zálohujte svůj privátní klíč

Než budete pokračovat dál, **musíte zálohovat** soubor s privátním klíčem vašeho eepsite. Je to z několika důvodů kriticky důležité:

### Proč zálohovat svůj klíč?

**Váš soukromý klíč (`eepPriv.dat`) je identitou vašeho eepsite (webu na síti I2P).** Určuje vaši adresu `.b32.i2p` a prokazuje vlastnictví vašeho eepsite.

- **Klíč = .b32 adresa**: Váš soukromý klíč matematicky generuje vaši jedinečnou adresu .b32.i2p
- **Nelze obnovit**: Pokud ztratíte svůj klíč, trvale přijdete o adresu svého eepsite
- **Nelze změnit**: Pokud jste zaregistrovali doménu směřující na .b32 adresu, **neexistuje způsob, jak ji aktualizovat** - registrace je trvalá
- **Nutné pro migraci**: Přesun na nový počítač nebo přeinstalace I2P vyžaduje tento klíč k zachování stejné adresy
- **Multihoming support** (podpora hostování z více umístění): Provozování vašeho eepsite z více umístění vyžaduje stejný klíč na každém serveru

### Kde je soukromý klíč?

Ve výchozím nastavení je váš soukromý klíč uložen zde: - **Linux**: `~/.i2p/eepsite/eepPriv.dat` (nebo `/var/lib/i2p/i2p-config/eepsite/eepPriv.dat` v případě instalace jako služby) - **Windows**: `%LOCALAPPDATA%\I2P\eepsite\eepPriv.dat` nebo `%PROGRAMDATA%\I2P\eepsite\eepPriv.dat` - **macOS**: `/Users/YourUsername/Library/Application Support/i2p/eepsite/eepPriv.dat`

Tuto cestu můžete také zkontrolovat/změnit ve své konfiguraci tunnelu v položce "Private Key File".

### Jak zálohovat

1. **Zastavte svůj tunnel** (volitelné, ale bezpečnější)
2. **Zkopírujte `eepPriv.dat`** na bezpečné místo:
   - Externí USB disk
   - Šifrovaný záložní disk
   - Archiv chráněný heslem
   - Bezpečné cloudové úložiště (šifrované)
3. Mějte více záloh na různých fyzických místech
4. Tento soubor nikdy nesdílejte - kdokoli, kdo ho má, se může vydávat za váš eepsite

### Obnovit ze zálohy

Chcete-li obnovit svůj eepsite na novém systému nebo po reinstalaci:

1. Nainstalujte I2P a vytvořte/nakonfigurujte nastavení svého tunnelu
2. **Zastavte tunnel** před zkopírováním klíče
3. Zkopírujte svůj zálohovaný `eepPriv.dat` do správného umístění
4. Spusťte tunnel - použije vaši původní adresu .b32

---

## Pokud neregistrujete doménu

**Gratulujeme!** Pokud neplánujete registrovat vlastní doménové jméno `.i2p`, váš eepsite (webová stránka v síti I2P) je nyní hotový a v provozu.

Můžete: - Sdílet svou adresu `.b32.i2p` s ostatními - Přistupovat ke svému webu přes síť I2P pomocí libovolného prohlížeče s podporou I2P - Kdykoli aktualizovat soubory svého webu ve složce `docroot` - Sledovat tunnel status v Hidden Services Manager (Správce skrytých služeb)

**Pokud chcete lidsky čitelnou doménu** (například `mysite.i2p` místo dlouhé .b32 adresy), přejděte do další sekce.

---

## Registrace vaší I2P domény

Lidsky čitelná doména `.i2p` (například `testwebsite.i2p`) se mnohem snáze pamatuje a sdílí než dlouhá adresa `.b32.i2p`. Registrace domény je zdarma a propojí vámi zvolené jméno s kryptografickou adresou vašeho eepsite.

### Předpoklady

- Váš eepsite musí běžet se zelenou kontrolkou
- Musíte mít nastavený **Název hostitele webu** v konfiguraci pro tunnel (Krok 2)
- Příklad: `testwebsite.i2p` nebo `myblog.i2p`

### Krok 1: Vygenerujte autentizační řetězec

1. **Vraťte se ke své konfiguraci pro tunnel** ve Správci skrytých služeb
2. Klikněte na položku **I2P webserver** pro otevření nastavení
3. Posuňte se dolů a najděte tlačítko **Ověření registrace**

![Autentizace při registraci](/images/guides/eepsite/registration-authentication.png)

4. Klikněte na **Ověření registrace**
5. **Zkopírujte celý ověřovací řetězec** zobrazený pro "Ověření pro přidání hostitele [yourdomainhere]"

Ověřovací řetězec bude vypadat takto:

```
testwebsite.i2p=I8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1iPForksdU3GALrQq4S73meoIIXarCCdb~Z6Ehj2-yLWI8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1iPForksdU3GALrQq4S73meoIIXarCCdb~Z6Ehj2-yLWI8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1iPForksdU3GALrQq4S73meoIIXarCCdb~Z6Ehj2-yLWI8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1uNxFZ0HN7tQbbVj1pmbahepQZNxEW0ufwnMYAoFo8opBQAEAAcAAA==#!date=1762104890#sig=9DjEfrcNRxsoSxiE0Mp0-7rH~ktYWtgwU8c4J0eSo0VHbGxDxdiO9D1Cvwcx8hkherMO07UWOC9BWf-1wRyUAw==
```
Tento řetězec obsahuje: - Vaše doménové jméno (`testwebsite.i2p`) - Vaše cílová adresa (dlouhý kryptografický identifikátor) - Časové razítko - Kryptografický podpis prokazující, že vlastníte soukromý klíč

**Uschovejte si tento ověřovací řetězec** - budete ho potřebovat pro obě registrační služby.

### Krok 2: Zaregistrujte se na stats.i2p

1. **Přejděte na** stats.i2p Přidat klíč (v rámci I2P)

![stats.i2p registrace domény](/images/guides/eepsite/stats-i2p-add.png)

2. **Vložte ověřovací řetězec** do pole "Authentication String"
3. **Přidejte své jméno** (volitelné) – výchozí je "Anonymous"
4. **Přidejte popis** (doporučeno) – stručně popište, o čem je váš eepsite
   - Příklad: "Nový I2P Eepsite", "Osobní blog", "Služba pro sdílení souborů"
5. **Zaškrtněte "HTTP Service?"**, pokud jde o web (u většiny eepsites ponechte zaškrtnuto)
   - Zrušte zaškrtnutí pro IRC, NNTP, proxy, XMPP, git atd.
6. Klikněte na **Submit**

V případě úspěchu uvidíte potvrzení, že vaše doména byla přidána do adresáře na stats.i2p.

### Krok 3: Zaregistrujte se na reg.i2p

Abyste zajistili maximální dostupnost, měli byste se také zaregistrovat u služby reg.i2p:

1. **Přejděte na** reg.i2p Add Domain (v rámci I2P)

![Registrace domény na reg.i2p](/images/guides/eepsite/reg-i2p-add.png)

2. **Vložte stejný autentizační řetězec** do pole "Auth string"
3. **Přidejte popis** (volitelné, ale doporučeno)
   - To pomáhá ostatním uživatelům I2P pochopit, co váš web nabízí
4. Klikněte na **Submit**

Měli byste obdržet potvrzení, že vaše doména byla zaregistrována.

### Krok 4: Počkejte na propagaci

Po odeslání do obou služeb se registrace vaší domény rozšíří napříč adresářovým systémem sítě I2P.

**Časová osa propagace**: - **Počáteční registrace**: Okamžitě na registračních službách - **Propagace napříč sítí**: Několik hodin až 24+ hodin - **Plná dostupnost**: Může trvat až 48 hodin, než se všechny routers aktualizují

**To je normální!** Systém adresáře I2P se aktualizuje pravidelně, ne okamžitě. Váš eepsite funguje - ostatní uživatelé jen potřebují získat aktualizovaný adresář.

### Ověřte svou doménu

Po několika hodinách můžete otestovat svou doménu:

1. **Otevřete novou kartu prohlížeče** ve svém I2P prohlížeči
2. Zkuste přejít přímo na svou doménu: `http://yourdomainname.i2p`
3. Pokud se stránka načte, vaše doména je registrována a propaguje se!

Pokud to zatím nefunguje: - Počkejte déle (adresáře se aktualizují podle vlastního harmonogramu) - Adresář vašeho routeru může potřebovat čas na synchronizaci - Zkuste restartovat svůj I2P router, abyste vynutili aktualizaci adresáře

### Důležité poznámky

- **Registrace je trvalá**: Jakmile je jednou zaregistrována a rozšířena, vaše doména trvale směřuje na vaši adresu `.b32.i2p`
- **Cíl nelze změnit**: Nelze aktualizovat, na kterou adresu `.b32.i2p` vaše doména směřuje - proto je zásadní zálohovat `eepPriv.dat`
- **Vlastnictví domény**: Doménu může zaregistrovat nebo aktualizovat pouze držitel soukromého klíče
- **Služba zdarma**: Registrace domén na I2P je zdarma, spravovaná komunitou a decentralizovaná
- **Více registrátorů**: Registrace u stats.i2p i reg.i2p zvyšuje spolehlivost a rychlost propagace

---

## Gratulujeme!

Vaše I2P eepsite je nyní plně funkční s registrovanou doménou!

**Další kroky**: - Přidejte další obsah do své složky `docroot` - Sdílejte svou doménu s komunitou I2P - Uchovejte svou zálohu `eepPriv.dat` v bezpečí - Pravidelně sledujte stav svého tunnelu - Zvažte zapojení do fór I2P nebo IRC, abyste propagovali svůj web

Vítejte v síti I2P! 🎉

---
title: "Instalace I2P na macOS"
description: "Krok za krokem průvodce ruční instalací I2P a jeho závislostí na macOS"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## Co budete potřebovat

- Mac se systémem macOS 10.14 (Mojave) nebo novějším
- Přístup správce pro instalaci aplikací
- Přibližně 15-20 minut času
- Internetové připojení pro stažení instalačních souborů

## Přehled

Tento proces instalace má čtyři hlavní kroky:

1. **Instalovat Java** - Stáhněte a nainstalujte Oracle Java Runtime Environment
2. **Instalovat I2P** - Stáhněte a spusťte instalátor I2P
3. **Konfigurovat I2P aplikaci** - Nastavte spouštěč a přidejte do docku
4. **Konfigurovat I2P šířku pásma** - Spusťte průvodce nastavením pro optimalizaci vašeho připojení

## Část první: Instalace Javy

I2P vyžaduje ke spuštění Javu. Pokud už máte nainstalovanou Javu 8 nebo novější, můžete [přejít k druhé části](#part-two-download-and-install-i2p).

### Krok 1: Stáhnout Java

Navštivte [stránku pro stažení Oracle Java](https://www.oracle.com/java/technologies/downloads/) a stáhněte si macOS instalátor pro Java 8 nebo novější.

![Download Oracle Java for macOS](/images/guides/macos-install/0-jre.png)

### Krok 2: Spusťte instalátor

Najděte stažený soubor `.dmg` ve složce Stažené soubory a dvojkliknutím jej otevřete.

![Otevřete instalátor Java](/images/guides/macos-install/1-jre.png)

### Krok 3: Povolit instalaci

macOS může zobrazit bezpečnostní výzvu, protože instalátor je od identifikovaného vývojáře. Pro pokračování klikněte na **Otevřít**.

![Udělte instalátoru oprávnění k pokračování](/images/guides/macos-install/2-jre.png)

### Krok 4: Nainstalujte Java

Klikněte na **Instalovat** pro zahájení procesu instalace Javy.

![Zahájení instalace Javy](/images/guides/macos-install/3-jre.png)

### Krok 5: Čekání na instalaci

Instalátor zkopíruje soubory a nakonfiguruje Javu ve vašem systému. To obvykle trvá 1-2 minuty.

![Počkejte na dokončení instalátoru](/images/guides/macos-install/4-jre.png)

### Krok 6: Instalace dokončena

Když uvidíte zprávu o úspěchu, Java je nainstalovaná! Klikněte na **Zavřít** pro dokončení.

![Java installation complete](/images/guides/macos-install/5-jre.png)

## Část druhá: Stažení a instalace I2P

Nyní, když je Java nainstalována, můžete nainstalovat I2P router.

### Krok 1: Stáhnout I2P

Navštivte [stránku Stahování](/downloads/) a stáhněte si instalátor **I2P pro Unix/Linux/BSD/Solaris** (soubor `.jar`).

![Stáhnout I2P instalátor](/images/guides/macos-install/0-i2p.png)

### Krok 2: Spusťte instalátor

Dvakrát klikněte na stažený soubor `i2pinstall_X.X.X.jar`. Instalátor se spustí a požádá vás o výběr preferovaného jazyka.

![Select your language](/images/guides/macos-install/1-i2p.png)

### Krok 3: Uvítací obrazovka

Přečtěte si uvítací zprávu a klikněte na **Další** pro pokračování.

![Installer introduction](/images/guides/macos-install/2-i2p.png)

### Krok 4: Důležité upozornění

Instalátor zobrazí důležité upozornění o aktualizacích. Aktualizace I2P jsou **end-to-end signed** (kompletně podepsané) a ověřené, i když je samotný instalátor nepodepsaný. Klikněte na **Další**.

![Important notice about updates](/images/guides/macos-install/3-i2p.png)

### Krok 5: Licenční smlouva

Přečtěte si licenční smlouvu I2P (licence ve stylu BSD). Klikněte na **Další** pro přijetí.

![License agreement](/images/guides/macos-install/4-i2p.png)

### Krok 6: Vyberte instalační adresář

Vyberte, kam chcete nainstalovat I2P. Doporučuje se výchozí umístění (`/Applications/i2p`). Klikněte na **Další**.

![Select installation directory](/images/guides/macos-install/5-i2p.png)

### Krok 7: Výběr komponent

Ponechte všechny komponenty vybrané pro úplnou instalaci. Klikněte na **Další**.

![Vyberte komponenty k instalaci](/images/guides/macos-install/6-i2p.png)

### Krok 8: Spustit instalaci

Zkontrolujte své volby a klikněte na **Další** pro zahájení instalace I2P.

![Zahájit instalaci](/images/guides/macos-install/7-i2p.png)

### Krok 9: Instalace souborů

Instalátor zkopíruje soubory I2P do vašeho systému. Trvá to přibližně 1-2 minuty.

![Instalace probíhá](/images/guides/macos-install/8-i2p.png)

### Krok 10: Generování spouštěcích skriptů

Instalátor vytváří spouštěcí skripty pro spuštění I2P.

![Generování spouštěcích skriptů](/images/guides/macos-install/9-i2p.png)

### Krok 11: Zástupci pro instalaci

Instalátor nabízí vytvoření zástupců na ploše a položek v nabídce. Proveďte výběr a klikněte na **Další**.

![Vytvořit zkratky](/images/guides/macos-install/10-i2p.png)

### Krok 12: Instalace dokončena

Úspěch! I2P je nyní nainstalováno. Klikněte na **Hotovo** pro dokončení.

![Instalace dokončena](/images/guides/macos-install/11-i2p.png)

## Část třetí: Konfigurace I2P aplikace

Nyní si usnadníme spouštění I2P tím, že ho přidáme do složky Aplikace a do Docku.

### Krok 1: Otevřete složku Aplikace

Otevřete Finder a přejděte do složky **Aplikace**.

![Otevřete složku Aplikace](/images/guides/macos-install/0-conf.png)

### Krok 2: Najděte I2P Launcher

Hledejte složku **I2P** nebo aplikaci **Start I2P Router** uvnitř `/Applications/i2p/`.

![Najděte spouštěč I2P](/images/guides/macos-install/1-conf.png)

### Krok 3: Přidat do Docku

Přetáhněte aplikaci **Start I2P Router** do vašeho Docku pro snadný přístup. Můžete také vytvořit alias na ploše.

![Přidat I2P do Docku](/images/guides/macos-install/2-conf.png)

**Tip**: Klikněte pravým tlačítkem na ikonu I2P v Docku a vyberte **Možnosti → Ponechat v Docku**, aby zůstala trvale.

## Část čtvrtá: Konfigurace šířky pásma I2P

Při prvním spuštění I2P projdete průvodcem nastavení pro konfiguraci nastavení šířky pásma. To pomáhá optimalizovat výkon I2P pro vaše připojení.

### Krok 1: Spusťte I2P

Klikněte na ikonu I2P v Docku (nebo dvakrát klikněte na spouštěč). Váš výchozí webový prohlížeč se otevře na I2P Router Console.

![I2P Router Console welcome screen](/images/guides/macos-install/0-wiz.png)

### Krok 2: Průvodce vítání

Průvodce nastavením vás přivítá. Klikněte na **Další** pro zahájení konfigurace I2P.

![Setup wizard introduction](/images/guides/macos-install/1-wiz.png)

### Krok 3: Jazyk a motiv

Vyberte váš preferovaný **jazyk rozhraní** a zvolte mezi **světlým** nebo **tmavým** motivem. Klikněte na **Další**.

![Vyberte jazyk a téma](/images/guides/macos-install/2-wiz.png)

### Krok 4: Informace o testu šířky pásma

Průvodce vysvětlí test šířky pásma. Tento test se připojí ke službě **M-Lab** a změří rychlost vašeho internetového připojení. Pokračujte kliknutím na **Další**.

![Bandwidth test explanation](/images/guides/macos-install/3-wiz.png)

### Krok 5: Spusťte test šířky pásma

Klikněte na **Spustit test** pro změření rychlosti uploadu a downloadu. Test trvá přibližně 30-60 sekund.

![Running the bandwidth test](/images/guides/macos-install/4-wiz.png)

### Krok 6: Výsledky testů

Zkontrolujte výsledky testů. I2P doporučí nastavení šířky pásma na základě rychlosti vašeho připojení.

![Výsledky testu šířky pásma](/images/guides/macos-install/5-wiz.png)

### Krok 7: Konfigurace sdílení šířky pásma

Vyberte, kolik šířky pásma chcete sdílet se sítí I2P:

- **Automatické** (Doporučeno): I2P spravuje šířku pásma na základě vašeho využití
- **Omezené**: Nastavit konkrétní limity pro upload/download
- **Neomezené**: Sdílet co nejvíce je možné (pro rychlá připojení)

Klikněte na **Další** pro uložení vašich nastavení.

![Konfigurace sdílení šířky pásma](/images/guides/macos-install/6-wiz.png)

### Krok 8: Konfigurace dokončena

Váš I2P router je nyní nakonfigurován a spuštěn! Konzole routeru zobrazí stav vašeho připojení a umožní vám procházet I2P stránky.

## Začínáme s I2P

Nyní, když je I2P nainstalováno a nakonfigurováno, můžete:

1. **Procházejte I2P stránky**: Navštivte [I2P domovskou stránku](http://127.0.0.1:7657/home) a podívejte se na odkazy na populární I2P služby
2. **Nakonfigurujte svůj prohlížeč**: Nastavte [profil prohlížeče](/docs/guides/browser-config) pro přístup k `.i2p` stránkám
3. **Prozkoumejte služby**: Vyzkoušejte I2P email, fóra, sdílení souborů a další
4. **Sledujte svůj router**: [Konzole](http://127.0.0.1:7657/console) zobrazuje stav vaší sítě a statistiky

### Užitečné odkazy

- **Router Console**: [http://127.0.0.1:7657/](http://127.0.0.1:7657/)
- **Konfigurace**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)
- **Adresář**: [http://127.0.0.1:7657/susidns/addressbook](http://127.0.0.1:7657/susidns/addressbook)
- **Nastavení šířky pásma**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)

## Opětovné spuštění průvodce nastavením

Pokud chcete později změnit nastavení šířky pásma nebo překonfigurovat I2P, můžete znovu spustit průvodce z Router Console:

1. Přejděte na [I2P Setup Wizard](http://127.0.0.1:7657/welcome)
2. Znovu postupujte podle kroků průvodce

## Řešení problémů

### I2P se nespustí

- **Zkontrolujte Javu**: Ujistěte se, že je Java nainstalována spuštěním `java -version` v Terminálu
- **Zkontrolujte oprávnění**: Ujistěte se, že složka I2P má správná oprávnění
- **Zkontrolujte logy**: Podívejte se na `~/.i2p/wrapper.log` kvůli chybovým zprávám

### Prohlížeč nemůže přistupovat k I2P stránkám

- Ujistěte se, že I2P běží (zkontrolujte Router Console)
- Nakonfigurujte nastavení proxy vašeho prohlížeče na HTTP proxy `127.0.0.1:4444`
- Po spuštění počkejte 5-10 minut, než se I2P integruje do sítě

### Pomalý výkon

- Spusťte test šířky pásma znovu a upravte svá nastavení
- Ujistěte se, že sdílíte nějakou šířku pásma se sítí
- Zkontrolujte stav vašeho připojení v Router Console

## Odinstalace I2P

Pro odstranění I2P z vašeho Mac:

1. Ukončete I2P router, pokud běží
2. Smažte složku `/Applications/i2p`
3. Smažte složku `~/.i2p` (vaše I2P konfigurace a data)
4. Odstraňte ikonu I2P z vašeho Docku

## Další kroky

- **Připojte se ke komunitě**: Navštivte [i2pforum.net](http://i2pforum.net) nebo se podívejte na I2P na Redditu
- **Dozvědět se více**: Přečtěte si [dokumentaci I2P](/en/docs), abyste pochopili, jak síť funguje
- **Zapojte se**: Zvažte [přispívání do vývoje I2P](/en/get-involved) nebo provozování infrastruktury

Gratulujeme! Nyní jste součástí sítě I2P. Vítejte na neviditelném internetu!

---

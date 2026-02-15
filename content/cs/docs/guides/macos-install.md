---
title: "Instalace I2P na macOS"
description: "Podrobný návod pro ruční instalaci I2P a jeho závislostí na macOS"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## Co budete potřebovat

- Mac se systémem macOS 10.14 (Mojave) nebo novější
- Administrátorský přístup pro instalaci aplikací
- Přibližně 15-20 minut času
- Připojení k internetu pro stažení instalačních souborů

## Přehled

Tento proces instalace má čtyři hlavní kroky:

1. **Instalace Java** - Stáhněte a nainstalujte Oracle Java Runtime Environment
2. **Instalace I2P** - Stáhněte a spusťte instalátor I2P
3. **Konfigurace aplikace I2P** - Nastavte spouštěč a přidejte do doku
4. **Konfigurace šířky pásma I2P** - Spusťte průvodce nastavením pro optimalizaci připojení

## První část: Instalace Javy

I2P vyžaduje ke spuštění Javu. Pokud už máte nainstalovanou Javu 8 nebo novější, můžete [přeskočit na druhou část](#part-two-download-and-install-i2p).

### Krok 1: Stáhnout Javu

Navštivte [stránku pro stažení Oracle Java](https://www.oracle.com/java/technologies/downloads/) a stáhněte si macOS instalátor pro Java 8 nebo novější.

![Stáhnout Oracle Java pro macOS](/images/guides/macos-install/0-jre.png)

### Krok 2: Spusťte instalátor

Najděte stažený soubor `.dmg` ve složce Stažené soubory a dvojklikem jej otevřete.

![Otevřít instalátor Javy](/images/guides/macos-install/1-jre.png)

### Krok 3: Povolit instalaci

macOS může zobrazit bezpečnostní výzvu, protože instalátor pochází od identifikovaného vývojáře. Klikněte na **Otevřít** pro pokračování.

![Udělte instalátoru oprávnění k pokračování](/images/guides/macos-install/2-jre.png)

### Krok 4: Instalace Javy

Klikněte na **Instalovat** pro zahájení procesu instalace Java.

![Start installing Java](/images/guides/macos-install/3-jre.png)

### Krok 5: Počkejte na dokončení instalace

Instalátor zkopíruje soubory a nakonfiguruje Javu na vašem systému. Obvykle to trvá 1-2 minuty.

![Počkejte na dokončení instalátoru](/images/guides/macos-install/4-jre.png)

### Krok 6: Instalace dokončena

Když uvidíte zprávu o úspěchu, Java je nainstalována! Klikněte na **Zavřít** pro dokončení.

![Instalace Javy dokončena](/images/guides/macos-install/5-jre.png)

## Část druhá: Stažení a instalace I2P

Nyní, když je Java nainstalována, můžete nainstalovat I2P router.

### Krok 1: Stáhněte I2P

Navštivte [stránku ke stažení](/downloads/) a stáhněte si instalátor **I2P pro Unix/Linux/BSD/Solaris** (soubor `.jar`).

![Stáhnout I2P instalátor](/images/guides/macos-install/0-i2p.png)

### Krok 2: Spusťte instalátor

Dvakrát klikněte na stažený soubor `i2pinstall_X.X.X.jar`. Spustí se instalátor a požádá vás o výběr preferovaného jazyka.

![Vyberte svůj jazyk](/images/guides/macos-install/1-i2p.png)

### Krok 3: Uvítací obrazovka

Přečtěte si uvítací zprávu a klikněte na **Další** pro pokračování.

![Installer introduction](/images/guides/macos-install/2-i2p.png)

### Krok 4: Důležité upozornění

Instalátor zobrazí důležité upozornění o aktualizacích. Aktualizace I2P jsou **end-to-end podepsané** a ověřené, i když samotný instalátor není podepsaný. Klikněte na **Další**.

![Important notice about updates](/images/guides/macos-install/3-i2p.png)

### Krok 5: Licenční smlouva

Přečtěte si licenční smlouvu I2P (licence ve stylu BSD). Klikněte na **Další** pro přijetí.

![License agreement](/images/guides/macos-install/4-i2p.png)

### Krok 6: Vyberte instalační adresář

Vyberte, kam chcete I2P nainstalovat. Doporučuje se výchozí umístění (`/Applications/i2p`). Klikněte na **Další**.

![Vyberte instalační adresář](/images/guides/macos-install/5-i2p.png)

### Krok 7: Vyberte komponenty

Nechte všechny komponenty vybrané pro úplnou instalaci. Klikněte na **Další**.

![Vyberte komponenty k instalaci](/images/guides/macos-install/6-i2p.png)

### Krok 8: Spuštění instalace

Zkontrolujte své volby a klikněte na **Další** pro zahájení instalace I2P.

![Spustit instalaci](/images/guides/macos-install/7-i2p.png)

### Krok 9: Instalace souborů

Instalátor zkopíruje soubory I2P do vašeho systému. Trvá to přibližně 1-2 minuty.

![Instalace probíhá](/images/guides/macos-install/8-i2p.png)

### Krok 10: Vygenerování spouštěcích skriptů

Instalátor vytváří spouštěcí skripty pro spuštění I2P.

![Generování spouštěcích skriptů](/images/guides/macos-install/9-i2p.png)

### Krok 11: Zkratky pro instalaci

Instalátor nabízí vytvoření zástupců na ploše a položek v nabídce. Proveďte svůj výběr a klikněte na **Další**.

![Create shortcuts](/images/guides/macos-install/10-i2p.png)

### Krok 12: Instalace dokončena

Úspěch! I2P je nyní nainstalováno. Klikněte na **Hotovo** pro dokončení.

![Instalace dokončena](/images/guides/macos-install/11-i2p.png)

## Část třetí: Konfigurace I2P aplikace

Nyní si usnadníme spouštění I2P přidáním do složky Aplikace a Docku.

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

### Krok 2: Průvodce vítáním

Průvodce nastavením vás přivítá. Klikněte na **Další** pro zahájení konfigurace I2P.

![Setup wizard introduction](/images/guides/macos-install/1-wiz.png)

### Krok 3: Jazyk a téma

Vyberte váš preferovaný **jazyk rozhraní** a zvolte mezi **světlým** nebo **tmavým** motivem. Klikněte na **Další**.

![Vyberte jazyk a motiv](/images/guides/macos-install/2-wiz.png)

### Krok 4: Informace o testu šířky pásma

Průvodce vám vysvětlí test šířky pásma. Tento test se připojuje ke službě **M-Lab** pro měření rychlosti vašeho internetového připojení. Klikněte na **Další** pro pokračování.

![Bandwidth test explanation](/images/guides/macos-install/3-wiz.png)

### Krok 5: Spuštění testu šířky pásma

Klikněte na **Spustit test** pro změření rychlosti uploadu a downloadu. Test trvá přibližně 30-60 sekund.

![Spuštění testu šířky pásma](/images/guides/macos-install/4-wiz.png)

### Krok 6: Výsledky testování

Zkontrolujte výsledky testů. I2P doporučí nastavení šířky pásma na základě rychlosti vašeho připojení.

![Bandwidth test results](/images/guides/macos-install/5-wiz.png)

### Krok 7: Konfigurace sdílení šířky pásma

Vyberte, kolik šířky pásma chcete sdílet se sítí I2P:

- **Automaticky** (Doporučeno): I2P spravuje šířku pásma na základě vašeho využití
- **Omezeno**: Nastavte specifické limity pro upload/download
- **Neomezeno**: Sdílejte co nejvíce je možné (pro rychlá připojení)

Klikněte na **Další** pro uložení vašich nastavení.

![Configure bandwidth sharing](/images/guides/macos-install/6-wiz.png)

### Krok 8: Konfigurace dokončena

Váš I2P router je nyní nakonfigurován a spuštěn! Konzole routeru zobrazí stav vašeho připojení a umožní vám procházet I2P stránky.

## Začínáme s I2P

Nyní, když je I2P nainstalováno a nakonfigurováno, můžete:

1. **Procházejte I2P stránky**: Navštivte `http://127.0.0.1:7657/home` a podívejte se na odkazy na oblíbené I2P služby
2. **Nakonfigurujte svůj prohlížeč**: Nastavte [profil prohlížeče](/docs/guides/browser-config) pro přístup k `.i2p` stránkám
3. **Prozkoumejte služby**: Vyzkoušejte I2P email, fóra, sdílení souborů a další
4. **Monitorujte svůj router**: `http://127.0.0.1:7657/console` zobrazuje stav vaší sítě a statistiky

### Užitečné odkazy

- **Router Console**: `http://127.0.0.1:7657/`
- **Konfigurace**: `http://127.0.0.1:7657/config`
- **Adresář**: `http://127.0.0.1:7657/susidns/addressbook`
- **Nastavení šířky pásma**: `http://127.0.0.1:7657/config`

## Opětovné spuštění Průvodce nastavením

Pokud chcete později změnit nastavení šířky pásma nebo znovu nakonfigurovat I2P, můžete znovu spustit uvítací průvodce z Router Console:

1. Přejděte na `http://127.0.0.1:7657/welcome`
2. Znovu postupujte podle kroků průvodce

## Řešení problémů

### I2P se nespustí

- **Zkontrolujte Javu**: Ujistěte se, že je Java nainstalována spuštěním `java -version` v Terminálu
- **Zkontrolujte oprávnění**: Ujistěte se, že složka I2P má správná oprávnění
- **Zkontrolujte logy**: Podívejte se do `~/.i2p/wrapper.log` pro chybové zprávy

### Prohlížeč nemůže přistupovat k I2P stránkám

- Ujistěte se, že I2P běží (zkontrolujte Router Console)
- Nakonfigurujte nastavení proxy ve vašem prohlížeči na HTTP proxy `127.0.0.1:4444`
- Počkejte 5-10 minut po spuštění, než se I2P integruje do sítě

### Nízký výkon

- Spusťte test šířky pásma znovu a upravte svá nastavení
- Ujistěte se, že sdílíte nějakou šířku pásma se sítí
- Zkontrolujte stav svého připojení v Router Console

## Odinstalace I2P

Pro odstranění I2P z vašeho Macu:

1. Ukončete I2P router, pokud běží
2. Smažte složku `/Applications/i2p`
3. Smažte složku `~/.i2p` (vaše I2P konfigurace a data)
4. Odstraňte ikonu I2P z vašeho Docku

## Další kroky

- **Připojte se ke komunitě**: Navštivte [i2pforum.net](http://i2pforum.net) nebo se podívejte na I2P na Redditu
- **Zjistěte více**: Přečtěte si [dokumentaci I2P](/en/docs), abyste pochopili, jak síť funguje
- **Zapojte se**: Zvažte [přispívání do vývoje I2P](/en/get-involved) nebo provozování infrastruktury

Gratulujeme! Nyní jste součástí sítě I2P. Vítejte v neviditelném internetu!

---

---
title: "Začínáme s I2P: Kompletní průvodce pro začátečníky"
description: "Začínáme s I2P: Kompletní průvodce pro začátečníky"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P je plně šifrovaná, peer-to-peer anonymní síť, která běží „uvnitř“ internetu**, a její java implementace z i2p.net zůstává hlavním způsobem jejího použití. Na rozdíl od Toru, který především anonymizuje přístup k běžnému webu, I2P vytváří zcela uzavřenou síť skrytých služeb, webových stránek, e-mailů, chatů a sdílení souborů.

---

## Co se stane v okamžiku, kdy spustíte I2P

Po instalaci spustí I2P lokální webovou aplikaci nazývanou **konzole směrovače** na adrese `http://127.0.0.1:7657`. Toto je vaše ovládací centrum, které běží plně na vašem počítači a z bezpečnostních důvodů je vázáno na localhost. Při prvním spuštění vás **průvodce nastavením** provede výběrem jazyka, motivu (tmavý nebo světlý) a automatickým testem šířky pásma, který trvá přibližně jednu minutu a využívá externí měřicí službu M-Lab. Následně nastavíte, jaké procento vaší šířky pásma budete sdílet se sítí.

![Průvodce nastavením I2P – Výběr jazyka](/images/guides/quickstart/wizard-language-selection.webp)

Jakmile průvodce dokončí svou práci, router zahájí proces zvaný **bootstrapping** (tzv. "reseeding"). Váš router stáhne přibližně **100 záznamů RouterInfo** z pevně zakódovaných reseed serverů přes HTTPS, čímž získá počáteční seznam peerů. Následně začne stavět **průzkumné tunely**, aby objevil další peery a naplnil svou lokální kopii síťové databáze (tzv. "netDb"). Během těchto prvních minut uvidíte zprávu „Rejecting tunnels: starting up“ (Zamítání tunelů: spouštění). To je normální jev.

![I2P Reseeding – Zavádění](/images/guides/quickstart/reseed-bootstrapping.webp)

**Počítejte s tím, že budete muset počkat 3–10 minut**, než bude váš router použitelný, a výrazně déle – dny nepřetržitého provozu – než dosáhne maximálního výkonu. Na bočním panelu konzole routeru se počet vašich peerů zobrazuje jako „Aktivní x/y“, kde x jsou peery, se kterými jste nedávno vyměnili zprávy, a y jsou všichni zaznamenaní peery. Jakmile uvidíte **10 nebo více aktivních peerů**, je váš router úspěšně připojen. Nejdůležitější, co může nový uživatel udělat, je **nechat router nepřetržitě spuštěný**. Po vypnutí označí ostatní uzly váš router jako nespolehlivý minimálně na 24 hodin, takže časté restartování značně zhoršuje výkon.

![I2P Router Console Dashboard](/images/guides/quickstart/router-console-dashboard.png)

---

## Nastavení prohlížeče pro I2P

Na rozdíl od sítě Tor, I2P nedisponuje vyhrazeným prohlížečem. Pro přístup k I2P stránkám (pseudodomena `.i2p`) je nutné nakonfigurovat nastavení proxy ve vašem prohlížeči tak, aby provoz směřoval přes I2P HTTP proxy na portu **4444**.

**Nejjednodušší cesta pro uživatele Windows** je **instalační balíček Easy Install**, který obsahuje Javu, směrovač a přednastavený profil Firefoxu s rozšířením „I2P in Private Browsing“. Tímto způsobem odpadá veškerá ruční konfigurace proxy. Od stažení po prohlížení I2P stránek to trvá přibližně čtyři minuty. Beta verze instalačního balíčku Easy Install pro macOS (Apple Silicon) je také k dispozici. Pokud používáte instalační balíček Easy Install, můžete přeskočit ruční nastavení uvedené níže.

### Firefox (doporučeno)

Důrazně se doporučuje Firefox, protože má vlastní nastavení proxy nezávislé na operačním systému – Chrome a Edge používají systémová nastavení proxy, která ovlivňují všechny aplikace.

**Krok 1.** Otevřete nabídku Firefoxu (ikona se třemi čárkami) a klikněte na **Nastavení**.

![Firefox – Otevřít nastavení](/images/guides/browser-config/accessi2p_3.png)

**Krok 2.** Vyhledejte **proxy** v panelu hledání nastavení, poté klikněte na **Nastavení...** vedle Nastavení sítě.

![Firefox – Hledání proxy](/images/guides/browser-config/accessi2p_4.png)

**Krok 3.** Vyberte **Ruční nastavení proxy**, zadejte `127.0.0.1` pro HTTP proxy a `4444` pro port, poté klikněte na **OK**.

![Firefox – Ruční konfigurace proxy](/images/guides/browser-config/accessi2p_5.png)

Po nastavení proxy je doporučeno provést několik úprav v `about:config`:

- Nastavte `media.peerConnection.ice.proxy_only` na **true** (zabraňuje unikání WebRTC)
- Nastavte `keyword.enabled` na **false** (zastaví přesměrování vyhledávačů na adresách .i2p)
- Vytvořte boolean `browser.fixup.domainsuffixwhitelist.i2p` a nastavte ho na **true** (řekne Firefoxu, že `.i2p` je platná přípona domény)

Častá past pro začátečníky: vždy napište `http://` před adresami `.i2p`. Většina I2P stránek nepoužívá HTTPS (I2P už tak šifruje veškerý provoz end-to-end), a bez prefixu vás Firefox přesměruje na vyhledávač.

### Chrome / Edge (Windows)

Poznámka: Chrome a Edge používají nastavení proxy vašeho operačního systému, což ovlivňuje **všechny** aplikace ve vašem systému.

**Krok 1.** Otevřete nabídku Chrome a klikněte na **Nastavení**.

![Chrome – Otevřít nastavení](/images/guides/browser-config/accessi2p_6.png)

**Krok 2.** Vyhledejte **proxy**, poté klikněte na **Otevřít nastavení proxy vašeho počítače**.

![Chrome – Hledání proxy](/images/guides/browser-config/accessi2p_7.png)

**Krok 3.** V části **Nastavení proxy ručně** klikněte na **Nastavit** vedle položky „Použít proxy server.“

![Windows – nastavení proxy](/images/guides/browser-config/accessi2p_8.png)

**Krok 4.** Přepněte **Použít proxy server** na Zapnuto, zadejte `127.0.0.1` jako IP adresu proxy a `4444` jako port, poté klikněte na **Uložit**.

![Windows – Upravit proxy server](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**Krok 1.** Přejděte do **Safari → Nastavení → Pokročilé** a klikněte na **Změnit nastavení...** vedle položky Proxy.

![Safari – Pokročilá nastavení](/images/guides/browser-config/accessi2p_1.png)

**Krok 2.** Povolte **Webový proxy server (HTTP)**, zadejte `127.0.0.1` jako server a `4444` jako port, poté klikněte na **OK**.

![macOS – nastavení webového proxy](/images/guides/browser-config/accessi2p_2.png)

---

## Porozumění řídicímu panelu konzole směrovače

Konzole směrovače na `127.0.0.1:7657` zobrazuje několik klíčových ukazatelů, které informují o výkonu vašeho uzlu. **Boční panel** ukazuje verzi I2P, dobu běhu, využití šířky pásma (vstup/výstup), počet aktivních peerů a stav tunelů. Jakmile se „Sdílené klienty“ změní na zelenou, je váš směrovač integrován a připraven k použití.

![Konzole směrovače - Sdílené klienty Zelená](/images/guides/quickstart/shared-clients-green.png)

**Grafy šířky pásma** zobrazují aktuální propustnost. Výchozí hodnoty jsou konzervativní – **96 KBps dolů a 40 KBps nahoru** s pouhými 48 KBps sdílenými – a oficiální dokumentace důrazně doporučuje tyto hodnoty zvýšit. Přejděte na `http://127.0.0.1:7657/config` (nebo klikněte na „Configure Bandwidth“ v konzoli), abyste zvýšili své limity. Vyšší sdílené pásmo zlepšuje jak vaši vlastní výkonnost, tak celkovou kondici sítě. Nastavení sdíleného pásma pod **12 KBps** efektivně přepne váš router do „skrytého režimu“, čímž ztratíte přístup k účasti na provozu sítě. Při **128 KBps a více** může být váš router povýšen na stav floodfill, což znamená, že pomáhá udržovat distribuovanou hashovací tabulku (DHT).

![Nastavení šířky pásma](/images/guides/quickstart/bandwidth-config.png)

Část **stav tunelu** zobrazuje zapojené tunely – provoz, který přeposíláte pro ostatní. Více než 90 % I2P routerů ve výchozím nastavení přeposílá účastnický provoz. Tento provoz současně slouží jako krycí provoz pro vaši vlastní anonymitu a zároveň jako váš příspěvek do sítě. Tunely vyprší každých 10 minut a jsou automaticky znovu vytvářeny.

![Správce I2PTunnel](/images/guides/quickstart/tunnel-manager.png)

Správce **I2PTunnel** na `http://127.0.0.1:7657/i2ptunnel/` zobrazuje všechny nakonfigurované tunely – HTTP proxy, IRC, e-mail a serverový tunel pro eepsite jsou přednastaveny již při prvním spuštění.

![Seznam I2PTunnel](/images/guides/quickstart/i2ptunnel-list.png)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Console page</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">URL</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Home / Status</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/home</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Dashboard with peers, bandwidth, tunnels</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Bandwidth config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/config</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Adjust speed limits and share percentage</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Network config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/confignet</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Firewall, port, and reachability settings</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Tunnel manager</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2ptunnel/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage all I2P tunnels and hidden services</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">I2PSnark</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2psnark/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in BitTorrent client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">SusiMail</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/susimail/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in email client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Address book</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/dns</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage .i2p hostname mappings</td>
</tr>
</tbody>
</table>
---

## Pět věcí, které můžete dělat po připojení

### Procházejte weby .i2p

Nejběžnějším využitím I2P je prohlížení skrytých webových stránek. Po nastavení prohlížeče na proxy port 4444 přejděte na libovolnou adresu končící `.i2p`. Několik známých stránek slouží jako vhodný výchozí bod: **`i2p-projekt.i2p`** je oficiální webové místo projektu I2P zrcadlené uvnitř sítě, **`i2pforum.i2p`** hostuje komunitní fórum pro podporu uživatelů, **`stats.i2p`** poskytuje statistiky sítě a službu registrace adres, a **`notbob.i2p`** sleduje dostupnost známých eepsitů, takže můžete vidět, co je skutečně online. Když narazíte na neznámou adresu `.i2p`, proxy nabídne odkazy „jump service“ (skoková služba), které přeloží název hostitele – kliknutím na ně přidáte nové stránky do své lokální adresářové knihy.

I2P také obsahuje výchozí **outproxy** (`exit.stormycloud.i2p`), který umožňuje přístup k běžnému internetu přes I2P, ale to není hlavním účelem sítě a výkon bude pomalý. I2P je navrženo jako interní darknet, nikoli jako síť s výstupními uzly jako Tor.

### Sdílejte torrenty anonymně pomocí I2PSnark

**I2PSnark** je plně funkční BitTorrent klient zabudovaný do každé instalace I2P, přístupný na adrese `http://127.0.0.1:7657/i2psnark/`. Funguje výhradně uvnitř sítě I2P – nemůže se připojit k torrentům na clearnetu a uživatelé clearnetu nemohou vidět torrenty v I2P. Webové rozhraní podporuje magnet odkazy, DHT, přetahování myší, vyhledávání torrentů, sekvenční stahování a UDP trackery (přidáno ve verzi 2.10.0). Výchozí délka tunelu je tři skoky. Stačí přidat soubory `.torrent` nebo magnet odkazy přes rozhraní.

![Rozhraní I2PSnark](/images/guides/quickstart/i2psnark-interface.png)

Chcete-li najít torrenty, navštivte **Postman Tracker** na adrese `http://tracker2.postman.i2p/` – centralizované centrum, kde uživatelé hledají a stahují torrenty nahrávané ostatními uživateli v rámci sítě I2P. Můžete také nahrát vlastní torrenty a sdílet je s komunitou.

![Postman Tracker](/images/guides/quickstart/postman-tracker.png)

Mezi další I2P-kompatibilní klienty torrentů patří BiglyBT a qBittorrent s I2P pluginem.

### Odesílejte šifrovanou e-mailovou poštu pomocí SusiMail

**SusiMail** na `http://127.0.0.1:7657/susimail/` je webový e-mailový klient navržený tak, aby nedocházelo k úniku identifikovatelných informací. Připojuje se k e-mailovému serveru **`mail.i2p`**, který provozuje „postman“. Chcete-li začít, zaregistrujte si účet na **`hq.postman.i2p`** (přístupné přes váš I2P proxy), poté se přihlaste k SusiMailu s těmito přihlašovacími údaji. Přednastavené položky I2PTunnel směrují SMTP přes `localhost:7659` a POP3 přes `localhost:7660`. Můžete odesílat e-maily jak ostatním uživatelům `@mail.i2p`, tak běžným internetovým e-mailovým adresám (přes most přes outproxy e-mailového serveru). SusiMail podporuje formátování pomocí markdownu, přílohy přetažením a HTML e-maily.

![SusiMail Příchozí](/images/guides/quickstart/susimail-login.png)

![SusiMail – Nová zpráva](/images/guides/quickstart/susimail-inbox.png)

### Chat na IRC přes síť Irc2P

I2P je dodáváno s **přednastaveným IRC tunelem** na `localhost:6668`. Nasměrujte jakéhokoli IRC klienta na tuto adresu (se SSL/TLS **vypnutým** – šifrování řeší I2P) a připojíte se tak k síti Irc2P, což je federace serverů včetně `irc.postman.i2p`, `irc.echelon.i2p` a `irc.dg.i2p`. Hlavní kanály jsou **`#i2p`** pro obecnou diskuzi, **`#i2p-dev`** pro vývoj a **`#i2p-help`** pro podporu. IRC tunnel automaticky odebere identifikační informace z vašeho připojení. Doporučené klienty jsou WeeChat, Pidgin a Thunderbird Chat.

### Hostujte svou vlastní anonymní webovou stránku

Každá instalace I2P obsahuje již spuštěný webový server **Jetty** na `localhost:7658` spolu s odpovídajícím I2P serverovým tunelem. Chcete-li publikovat web, jednoduše vložte soubory HTML do kořenového adresáře dokumentů: `~/.i2p/eepsite/docroot` na Linuxu nebo `%LOCALAPPDATA%\I2P\I2P Site\docroot` ve Windows. Váš web automaticky získá kryptografickou Base64 destinaci a kratší adresu `xxxxx.b32.i2p`. Chcete-li získat čitelný název jako `mysite.i2p`, zaregistrujte jej u služeb adresáře, například na `stats.i2p` nebo `no.i2p`. Pro pokročilejší nastavení můžete Jetty nahradit Apache nebo Nginx za I2PTunnel serverovým tunelem – nezapomeňte pouze odstranit identifikovatelné hlavičky serveru. Podrobný návod najdete v našem průvodci [Vytvoření I2P eepsite](/docs/guides/creating-an-eepsite/).

---

## Základní bezpečnostní postupy pro nové uživatele

**Nikdy nepoužívejte procházení I2P a clearnetu ve stejném profilu prohlížeče.** Toto je nejdůležitější bezpečnostní pravidlo. Vytvořte si vyhrazený profil ve Firefoxu přes `about:profiles` nebo použijte přednastavený profil z balíčku Easy Install Bundle. Směšování cookie, historie a uložených dat mezi anonymním a identifikovaným procházením je nejčastější chybou operační bezpečnosti.

Oficiální rozšíření pro Firefox **"I2P in Private Browsing"** (dostupné v obchodě s doplňky Mozilly) automatizuje většinu tohoto nastavení tím, že vytváří izolované kontejnerové karty s povoleným ochranou proti otiskování, izolací první strany a letterboxingem. Uživatelé Chromium by měli spustit prohlížeč s následujícími parametry: `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`.

---

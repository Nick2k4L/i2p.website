---
title: "Alternativní I2P klienti"
description: "Komunitou udržované implementace I2P klientů (aktualizováno pro rok 2025)"
slug: "alternative-clients"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

Hlavní implementace I2P klienta používá **Java**. Pokud nemůžete nebo nechcete používat Java na konkrétním systému, existují alternativní implementace I2P klienta vyvíjené a udržované členy komunity. Tyto programy poskytují stejnou základní funkcionalnost pomocí různých programovacích jazyků nebo přístupů.

---

## Porovnávací tabulka

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Client</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Maturity</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Actively Maintained</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Suitable For</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Java I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes (official)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">General users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Standard full router; includes console, plugins, and tools</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>i2pd</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Low-resource systems, servers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Lightweight, fully compatible with Java I2P, includes web console</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Go-I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, testing</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Early-stage Go implementation; not yet production ready</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Emissary</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, embedded use</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust I2P implementation; embeddable router with eepsite, torrent, IRC and email support</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>I2P+</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable (fork)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Advanced users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Enhanced Java I2P fork with UI and performance improvements</td>
    </tr>
  </tbody>
</table>
---

## i2pd (C++)

**Webové stránky:** [https://i2pd.website](https://i2pd.website)

**Popis:** i2pd (*I2P Daemon*) je plnohodnotný I2P klient implementovaný v C++. Je stabilní pro produkční použití již mnoho let (přibližně od roku 2016) a je aktivně udržován komunitou. i2pd plně implementuje síťové protokoly a API I2P, což ho činí zcela kompatibilní se síťí Java I2P. Tento C++ router je často používán jako lehká alternativa na systémech, kde není Java runtime k dispozici nebo není žádoucí. i2pd obsahuje vestavěnou webovou konzoli pro konfiguraci a monitoring. Je multiplatformní a dostupný v mnoha formátech balíčků — je dokonce k dispozici i Android verze i2pd (například přes F-Droid).

---

## Go-I2P (Go)

**Repository:** [https://github.com/go-i2p/go-i2p](https://github.com/go-i2p/go-i2p)

**Popis:** Go-I2P je I2P klient napsaný v programovacím jazyce Go. Jedná se o nezávislou implementaci I2P routeru, která se snaží využít efektivity a přenositelnosti jazyka Go. Projekt je aktivně vyvíjen, ale stále se nachází v rané fázi a ještě není kompletně funkční. K roku 2025 je Go-I2P považováno za experimentální — na projektu aktivně pracují komunitní vývojáři, ale není doporučováno pro produkční použití, dokud nedospěje. Cílem Go-I2P je poskytovat moderní, lehký I2P router s plnou kompatibilitou se sítí I2P po dokončení vývoje.

---

## Emissary (Rust)

**Webová stránka:** [https://eepnet.github.io/emissary/](https://eepnet.github.io/emissary/)

**Popis:** Emissary je implementace protokolového zásobníku I2P v jazyce Rust, navržená tak, aby fungovala jako vestavitelný I2P router. Může být integrována do jiných aplikací nebo spuštěna samostatně. Emissary podporuje hosting eepsite, torrenty, IRC a emailové služby. Projekt zahrnuje rozsáhlou dokumentaci pokrývající rychlé nastavení, vestavění pro vývojáře a podrobnou konfiguraci. Jako experimentální projekt je aktivně vyvíjen a zatím se nedoporučuje pro produkční použití.

---

## I2P+ (Java fork)

**Webové stránky:** [https://i2pplus.github.io](https://i2pplus.github.io)

**Popis:** I2P+ je komunitou udržovaný fork standardního Java I2P klienta. Nejedná se o reimplementaci v novém jazyce, ale spíše o vylepšenou verzi Java routeru s dodatečnými funkcemi a optimalizacemi. I2P+ se zaměřuje na poskytování lepší uživatelské zkušenosti a vyššího výkonu při zachování plné kompatibility s oficiální I2P sítí. Přináší obnovené rozhraní webové konzole, uživatelsky přívětivější možnosti konfigurace a různé optimalizace (například vylepšený výkon torrentů a lepší správu síťových peerů, zejména pro routery za firewally). I2P+ vyžaduje Java prostředí stejně jako oficiální I2P software, takže není řešením pro prostředí bez Javy. Nicméně pro uživatele, kteří Java mají a chtějí alternativní build s dodatečnými schopnostmi, I2P+ poskytuje přesvědčivou možnost. Tento fork je udržován aktuální s upstream I2P vydáními (s jeho číslováním verzí připojujícím "+") a lze jej získat z webových stránek projektu.

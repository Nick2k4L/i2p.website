---
title: "Použití git bundle pro stažení zdrojového kódu I2P"
description: "Klonování velkých repozitářů přes I2P pomocí git bundlů a BitTorrentu"
slug: "git-bundle"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

Klonování velkých softwarových repozitářů přes I2P může být obtížné a použití gitu může toto někdy ztížit ještě více. Naštěstí to také někdy může usnadnit. Git má příkaz `git bundle`, který lze použít k převedení git repozitáře na soubor, ze kterého pak git může klonovat, stahovat nebo importovat z umístění na vašem lokálním disku. Kombinací této schopnosti se stahováním přes bittorrent můžeme vyřešit naše zbývající problémy s `git clone`.

---

## Než začnete

Pokud máte v úmyslu vygenerovat git bundle, **musíte** již vlastnit úplnou kopii **git** repozitáře, nikoli mtn repozitáře. Můžete jej získat z github nebo z git.idk.i2p, ale shallow clone (klon vytvořený s --depth=1) *nebude fungovat*. Selže tiše a vytvoří něco, co vypadá jako bundle, ale když se jej pokusíte naklonovat, selže. Pokud pouze načítáte předem vygenerovaný git bundle, pak se vás tato sekce netýká.

---

## Stahování zdrojového kódu I2P přes Bittorrent

Někdo vám bude muset poskytnout torrent soubor nebo magnet odkaz odpovídající existujícímu `git bundle`, který už pro vás vygeneroval. Nedávný, správně vygenerovaný bundle hlavní větve zdrojového kódu i2p.i2p ke středě 18. března 2020 můžete najít uvnitř I2P na mém pastebinu paste.idk.i2p/f/4hq37i.

Jakmile máte bundle, budete muset použít git k vytvoření pracovního repozitáře z něj. Pokud používáte GNU/Linux a i2psnark, git bundle by měl být umístěn v $HOME/.i2p/i2psnark nebo, jako služba na Debianu, v /var/lib/i2p/i2p-config/i2psnark. Pokud používáte BiglyBT na GNU/Linux, je pravděpodobně v "$HOME/BiglyBT Downloads/" místo toho. Příklady zde předpokládají I2PSnark na GNU/Linux, pokud používáte něco jiného, nahraďte cestu k bundle adresářem pro stahování, který preferuje váš klient a platforma.

### Použití `git clone`

Klonování z git bundle je jednoduché, stačí:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
Pokud se zobrazí následující chyba, zkuste místo toho použít `git init` a `git fetch` ručně.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### Používání `git init` a `git fetch`

Nejprve vytvořte adresář i2p.i2p, který převedete na git repositář.

```
mkdir i2p.i2p && cd i2p.i2p
```
Dále inicializujte prázdný git repozitář pro načtení změn zpět.

```
git init
```
Nakonec načtěte repozitář z bundle.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### Nahraďte bundle remote s upstream remote

Nyní, když máte bundle, můžete sledovat změny nastavením vzdáleného repozitáře na upstream zdroj repositáře.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## Generování balíčku

Nejprve postupujte podle [Git průvodce pro uživatele](/docs/applications/git/) dokud nebudete mít úspěšně `--unshallow`ed klon i2p.i2p repozitáře. Pokud již máte klon, ujistěte se, že spustíte `git fetch --unshallow` před generováním torrent balíčku.

Jakmile to máte, jednoduše spusťte odpovídající ant target:

```
ant git-bundle
```
a zkopírujte výsledný bundle do vašeho stahování adresáře I2PSnark. Například:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
Za minutu nebo dvě si I2PSnark všimne torrentu. Klikněte na tlačítko "Start" pro zahájení seedování torrentu.

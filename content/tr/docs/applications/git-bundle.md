---
title: "I2P kaynak kodunu almak için git bundle kullanımı"
description: "Git bundle'ları ve BitTorrent kullanarak I2P üzerinden büyük repository'leri klonlama"
slug: "git-bundle"
aliases:
  - "/tr/docs/applications/git"
  - "/tr/docs/applications/git/"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

I2P üzerinden büyük yazılım depolarını klonlamak zor olabilir ve git kullanmak bazen bunu daha da zorlaştırabilir. Neyse ki, bazen de kolaylaştırabilir. Git, bir git deposunu yerel diskinizde bulunan bir konumdan git'in klonlayabileceği, getirebileceği veya içe aktarabileceği bir dosyaya dönüştürmek için kullanılabilen `git bundle` komutuna sahiptir. Bu özelliği bittorrent indirmeleriyle birleştirerek, `git clone` ile ilgili kalan sorunlarımızı çözebiliriz.

---

## Başlamadan Önce

Eğer bir git bundle oluşturmayı planlıyorsanız, **mtn repository değil**, **git** repository'sinin tam bir kopyasına sahip olmanız **gereklidir**. Bunu github'dan veya git.idk.i2p'den alabilirsiniz, ancak shallow clone (--depth=1 ile yapılan clone) *çalışmayacaktır*. Sessizce başarısız olacak, bundle gibi görünen bir şey oluşturacaktır, ancak onu clone etmeye çalıştığınızda başarısız olacaktır. Sadece önceden oluşturulmuş bir git bundle'ı alıyorsanız, bu bölüm sizin için geçerli değildir.

---

## I2P Kaynak Kodunu Bittorrent ile İndirme

Birinin size zaten oluşturduğu mevcut bir `git bundle`'a karşılık gelen bir torrent dosyası veya magnet bağlantısı sağlaması gerekecek. 18 Mart 2020 Çarşamba tarihi itibariyle ana hat i2p.i2p kaynak kodunun güncel, doğru şekilde oluşturulmuş bir bundle'ı I2P içindeki pastebin'imde [paste.idk.i2p/f/4hq37i](http://paste.idk.i2p/f/4h137i) adresinde bulunabilir.

Bir bundle'ınız olduğunda, ondan çalışan bir repository oluşturmak için git kullanmanız gerekecek. GNU/Linux ve i2psnark kullanıyorsanız, git bundle $HOME/.i2p/i2psnark konumunda veya Debian'da servis olarak /var/lib/i2p/i2p-config/i2psnark konumunda bulunmalıdır. GNU/Linux'ta BiglyBT kullanıyorsanız, muhtemelen "$HOME/BiglyBT Downloads/" konumundadır. Buradaki örnekler GNU/Linux'ta I2PSnark'ı varsayar, başka bir şey kullanıyorsanız bundle'ın yolunu istemciniz ve platformunuz tarafından tercih edilen indirme dizini ile değiştirin.

### `git clone` kullanarak

Bir git bundle'dan klonlama kolaydır, sadece:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
Aşağıdaki hatayı alırsanız, bunun yerine git init ve git fetch komutlarını manuel olarak kullanmayı deneyin.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### `git init` ve `git fetch` kullanımı

Önce, git repository'sine dönüştürmek için bir i2p.i2p dizini oluşturun.

```
mkdir i2p.i2p && cd i2p.i2p
```
Ardından, değişiklikleri geri almak için boş bir git deposu başlatın.

```
git init
```
Son olarak, bundle'dan repository'yi getirin.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### Bundle remote'unu upstream remote ile değiştirin

Artık bir bundle'ınız olduğuna göre, remote'u upstream repository kaynağına ayarlayarak değişiklikleri takip edebilirsiniz.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## Paket Oluşturma

Öncelikle, i2p.i2p repository'sinin başarılı bir şekilde `--unshallow` edilmiş klonuna sahip olana kadar [Kullanıcılar için Git kılavuzu](/docs/applications/git/)'nu takip edin. Zaten bir klonunuz varsa, torrent paketi oluşturmadan önce `git fetch --unshallow` komutunu çalıştırdığınızdan emin olun.

Bunu elde ettikten sonra, sadece ilgili ant hedefini çalıştırın:

```
ant git-bundle
```
ve oluşan paketi I2PSnark indirmeler dizininize kopyalayın. Örneğin:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
Bir iki dakika içinde I2PSnark torrenti algılayacaktır. Torrenti seed etmeye başlamak için "Başlat" butonuna tıklayın.

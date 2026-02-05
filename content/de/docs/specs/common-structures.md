---
title: "Spezifikation gemeinsamer Strukturen"
description: "Datentypen, die allen I2P-Protokollen gemeinsam sind"
slug: "common-structures"
category: "Design"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

Dieses Dokument beschreibt einige Datentypen, die allen I2P-Protokollen gemeinsam sind, wie [I2NP](/docs/specs/i2np/), [I2CP](/docs/specs/i2cp/), [SSU](/docs/legacy/ssu/), etc.

## Allgemeine Typspezifikation

### Ganzzahl

#### Beschreibung

Repräsentiert eine nicht-negative ganze Zahl.

#### Inhaltsverzeichnis

1 bis 8 Bytes in Netzwerk-Byte-Reihenfolge (Big-Endian), die eine vorzeichenlose Ganzzahl darstellen.

### Datum

#### Beschreibung

Die Anzahl der Millisekunden seit Mitternacht am 1. Januar 1970 in der GMT-Zeitzone. Wenn die Zahl 0 ist, ist das Datum undefiniert oder null.

#### Inhaltsverzeichnis

8 Byte [Integer](#integer)

### Zeichenkette

#### Beschreibung

Stellt eine UTF-8-kodierte Zeichenkette dar.

#### Inhaltsverzeichnis

1 oder mehr Bytes, wobei das erste Byte die Anzahl der Bytes (nicht Zeichen!) in der Zeichenkette angibt und die verbleibenden 0-255 Bytes das nicht null-terminierte UTF-8-kodierte Zeichen-Array darstellen. Die Längenbegrenzung beträgt 255 Bytes (nicht Zeichen). Die Länge kann 0 sein.

### PublicKey

#### Beschreibung

Diese Struktur wird in ElGamal oder anderen asymmetrischen Verschlüsselungsverfahren verwendet und repräsentiert nur den Exponenten, nicht die Primzahlen, die konstant sind und in der Kryptographie-Spezifikation [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) definiert werden. Andere Verschlüsselungsverfahren befinden sich derzeit in der Definition, siehe die Tabelle unten.

#### Inhaltsverzeichnis

Schlüsseltyp und -länge werden aus dem Kontext abgeleitet oder sind im Key Certificate einer Destination oder RouterInfo spezifiziert, oder in den Feldern eines [LeaseSet2](#leaseset2) oder einer anderen Datenstruktur. Der Standardtyp ist ElGamal. Ab Release 0.9.38 können andere Typen unterstützt werden, je nach Kontext. Schlüssel sind Big-Endian, sofern nicht anders angegeben.

X25519-Schlüssel werden in Destinations und LeaseSet2 seit Release 0.9.44 unterstützt. X25519-Schlüssel werden in RouterIdentities seit Release 0.9.48 unterstützt.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">800</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1184</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1088</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PublicKey.html

### PrivateKey

#### Beschreibung

Diese Struktur wird in ElGamal oder anderen asymmetrischen Entschlüsselungsverfahren verwendet und repräsentiert nur den Exponenten, nicht die Primzahlen, die konstant sind und in der Kryptografie-Spezifikation [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) definiert werden. Andere Verschlüsselungsverfahren sind derzeit in der Definitionsphase, siehe Tabelle unten.

#### Inhalt

Schlüsseltyp und -länge werden aus dem Kontext abgeleitet oder separat in einer Datenstruktur oder einer privaten Schlüsseldatei gespeichert. Der Standardtyp ist ElGamal. Ab Release 0.9.38 können je nach Kontext andere Typen unterstützt werden. Schlüssel sind big-endian, sofern nicht anders angegeben.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1632</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2400</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3168</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PrivateKey.html

### SessionKey

#### Beschreibung

Diese Struktur wird für symmetrische AES256-Verschlüsselung und -Entschlüsselung verwendet.

#### Inhalt

32 Bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### SigningPublicKey

#### Beschreibung

Diese Struktur wird zur Überprüfung von Signaturen verwendet.

#### Inhalt

Schlüsseltyp und -länge werden aus dem Kontext abgeleitet oder sind im Key Certificate einer Destination angegeben. Der Standardtyp ist DSA_SHA1. Ab Release 0.9.12 können je nach Kontext auch andere Typen unterstützt werden.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Notizen

* Wenn ein Schlüssel aus zwei Elementen besteht (zum Beispiel Punkte X,Y), wird er serialisiert, indem jedes Element auf length/2 mit führenden Nullen aufgefüllt wird, falls erforderlich.

* Alle Typen sind Big Endian, außer EdDSA und RedDSA, die in einem Little Endian Format gespeichert und übertragen werden.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### Beschreibung

Diese Struktur wird zur Erstellung von Signaturen verwendet.

#### Inhalt

Schlüsseltyp und -länge werden bei der Erstellung festgelegt. Der Standardtyp ist DSA_SHA1. Ab Version 0.9.12 können je nach Kontext andere Typen unterstützt werden.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Hinweise

* Wenn ein Schlüssel aus zwei Elementen besteht (zum Beispiel Punkte X,Y), wird er serialisiert, indem jedes Element auf Länge/2 mit führenden Nullen aufgefüllt wird, falls erforderlich.

* Alle Typen sind Big Endian, außer EdDSA und RedDSA, die in einem Little Endian Format gespeichert und übertragen werden.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### Signatur

#### Beschreibung

Diese Struktur repräsentiert die Signatur einiger Daten.

#### Inhalte

Signaturtyp und -länge werden vom verwendeten Schlüsseltyp abgeleitet. Der Standardtyp ist DSA_SHA1. Ab Version 0.9.12 können je nach Kontext auch andere Typen unterstützt werden.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Notizen

* Wenn eine Signatur aus zwei Elementen besteht (zum Beispiel Werte R,S), wird sie serialisiert, indem jedes Element auf length/2 mit führenden Nullen aufgefüllt wird, falls erforderlich.

* Alle Typen sind Big Endian, außer EdDSA und RedDSA, die in einem Little Endian Format gespeichert und übertragen werden.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### Hash

#### Beschreibung

Stellt den SHA256 einiger Daten dar.

#### Inhaltsverzeichnis

32 Bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### Session Tag

Hinweis: Session Tags für ECIES-X25519 Ziele (ratchet) und ECIES-X25519 router sind 8 Bytes. Siehe [ECIES](/docs/specs/ecies/) und [ECIES-ROUTERS](/docs/specs/ecies-routers/).

#### Beschreibung

Eine Zufallszahl

#### Inhaltsverzeichnis

32 Bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### Beschreibung

Definiert einen Identifikator, der für jeden router in einem tunnel eindeutig ist. Eine Tunnel ID ist im Allgemeinen größer als null; verwenden Sie den Wert null nur in besonderen Fällen.

#### Inhaltsverzeichnis

4 Byte [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### Zertifikat

#### Beschreibung

Ein Zertifikat ist ein Container für verschiedene Belege oder Arbeitsnachweise, die im gesamten I2P-Netzwerk verwendet werden.

#### Inhalt

1 Byte [Integer](#integer), der den Zertifikatstyp angibt, gefolgt von einem 2 Byte [Integer](#integer), der die Größe der Zertifikatsdaten angibt, dann entsprechend viele Bytes.

```
+----+----+----+----+----+-/
|type| length  | payload
+----+----+----+----+----+-/

type :: `Integer`
        length -> 1 byte

        case 0 -> NULL
        case 1 -> HASHCASH
        case 2 -> HIDDEN
        case 3 -> SIGNED
        case 4 -> MULTIPLE
        case 5 -> KEY

length :: `Integer`
          length -> 2 bytes

payload :: data
           length -> $length bytes
```
#### Notizen

* Für [Router Identities](#routeridentity) ist das Zertifikat bis einschließlich Version
  0.9.15 immer NULL. Ab Version 0.9.16 wird ein Schlüsselzertifikat verwendet, um die
  Schlüsseltypen zu spezifizieren. Ab Version 0.9.48 sind X25519-Verschlüsselungs-
  Public-Key-Typen erlaubt. Siehe unten.

* Für [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove) ist das Certificate immer NULL, andere sind derzeit nicht
  implementiert.

* Für [Garlic Messages](/docs/specs/i2np/#msg-garlic) ist das Zertifikat immer NULL, andere sind derzeit nicht implementiert.

* Für [Destinations](#destination) kann das Certificate non-NULL sein. Ab Version 0.9.12 kann ein Key Certificate verwendet werden, um den Typ des öffentlichen Signaturschlüssels zu spezifizieren. Siehe unten.

* Implementierern wird geraten, überschüssige Daten in Zertifikaten zu verbieten.
  Die angemessene Länge für jeden Zertifikatstyp sollte durchgesetzt werden.

#### Zertifikatstypen

Die folgenden Zertifikatstypen sind definiert:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HashCash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains an ASCII colon-separated hashcash string.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Hidden</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Hidden routers generally do not announce that they are hidden.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signed</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40 or 72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">43 or 75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains a 40-byte DSA signature, optionally followed by the 32-byte Hash of the signing Destination.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Multiple</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains multiple certificates.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Since 0.9.12. See below for details.</td>
    </tr>
  </tbody>
</table>
#### Schlüsselzertifikate

Key-Zertifikate wurden in Release 0.9.12 eingeführt. Vor diesem Release waren alle PublicKeys 256-Byte ElGamal-Schlüssel und alle SigningPublicKeys 128-Byte DSA-SHA1-Schlüssel. Ein Key-Zertifikat bietet einen Mechanismus, um den Typ des PublicKey und SigningPublicKey in der Destination oder RouterIdentity anzugeben und alle Schlüsseldaten zu verpacken, die die Standardlängen überschreiten.

Durch die Beibehaltung von genau 384 Bytes vor dem Zertifikat und das Platzieren zusätzlicher Schlüsseldaten innerhalb des Zertifikats wahren wir die Kompatibilität für jede Software, die Destinations und Router Identities parst.

Die Schlüsselzertifikat-Nutzlast enthält:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signing Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Crypto Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Signing Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Crypto Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
  </tbody>
</table>
Warnung: Die Reihenfolge der Schlüsseltypen ist das Gegenteil von dem, was Sie erwarten könnten; der Signing Public Key Type steht an erster Stelle.

Die definierten Signing Public Key-Typen sind:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only; never used for Router Identities</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">13</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">14</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Die definierten Crypto Public Key-Typen sind:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies/">ECIES</a> and proposal 156</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (NONE)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">255</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Wenn ein Key Certificate nicht vorhanden ist, sind die vorhergehenden 384 Bytes in der Destination oder RouterIdentity definiert als der 256-Byte ElGamal PublicKey gefolgt vom 128-Byte DSA-SHA1 SigningPublicKey. Wenn ein Key Certificate vorhanden ist, werden die vorhergehenden 384 Bytes wie folgt neu definiert:

* Vollständiger oder erster Teil des Crypto Public Key

* Zufällige Auffüllung, wenn die Gesamtlänge der beiden Schlüssel weniger als 384 Bytes beträgt

* Vollständiger oder erster Teil des Signing Public Key

Der Crypto Public Key wird am Anfang ausgerichtet und der Signing Public Key wird am Ende ausgerichtet. Das Padding (falls vorhanden) befindet sich in der Mitte. Die Längen und Grenzen der anfänglichen Schlüsseldaten, des Paddings und der überschüssigen Schlüsseldatenteile in den Zertifikaten sind nicht explizit spezifiziert, sondern werden aus den Längen der angegebenen Schlüsseltypen abgeleitet. Wenn die Gesamtlängen der Crypto und Signing Public Keys 384 Bytes überschreiten, wird der Rest im Key Certificate enthalten sein. Wenn die Crypto Public Key-Länge nicht 256 Bytes beträgt, ist die Methode zur Bestimmung der Grenze zwischen den beiden Schlüsseln in einer zukünftigen Revision dieses Dokuments zu spezifizieren.

Beispiel-Layouts mit einem ElGamal Crypto Public Key und dem angegebenen Signing Public Key-Typ:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Signing Key Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Excess Signing Key Data in Cert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Certificate.html

#### Notizen

* Implementierer werden davor gewarnt, überschüssige Daten in Key Certificates zuzulassen.
  Die angemessene Länge für jeden Zertifikatstyp sollte durchgesetzt werden.

* Ein KEY-Zertifikat mit den Typen 0,0 (ElGamal,DSA_SHA1) ist erlaubt, aber nicht empfohlen.
  Es ist nicht gut getestet und kann in manchen Implementierungen Probleme verursachen.
  Verwenden Sie ein NULL-Zertifikat in der kanonischen Darstellung einer
  (ElGamal,DSA_SHA1) Destination oder RouterIdentity, welches 4 Bytes kürzer
  ist als die Verwendung eines KEY-Zertifikats.

### Zuordnung

#### Beschreibung

Ein Satz von Schlüssel/Wert-Zuordnungen oder Eigenschaften

#### Inhaltsverzeichnis

Ein 2-Byte-Größe Integer gefolgt von einer Reihe von String=String; Paaren.

WARNUNG: Die meisten Verwendungen von Mapping befinden sich in signierten Strukturen, wo die Mapping-Einträge nach Schlüssel sortiert sein müssen, damit die Signatur unveränderlich ist. Das Versäumnis, nach Schlüssel zu sortieren, führt zu Signaturfehlern!

```
+----+----+----+----+----+----+----+----+
|  size   | key_string (len + data)| =  |
+----+----+----+----+----+----+----+----+
| val_string (len + data)     | ;  | ...
+----+----+----+----+----+----+----+
size :: `Integer`
        length -> 2 bytes
        Total number of bytes that follow

key_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

= :: A single byte containing '='

val_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

; :: A single byte containing ';'
```
#### Notizen

* Die Kodierung ist nicht optimal - wir benötigen entweder die '=' und ';' Zeichen, oder
  die String-Längen, aber nicht beides

* Einige Dokumentationen besagen, dass die Zeichenketten kein '=' oder ';' enthalten dürfen, aber diese Kodierung unterstützt sie

* Strings sind als UTF-8 definiert, aber in der aktuellen Implementierung verwendet I2CP UTF-8, während I2NP dies nicht tut. Zum Beispiel werden UTF-8-Strings in einem RouterInfo-Options-Mapping in einer I2NP Database Store Message beschädigt.

* Die Kodierung erlaubt doppelte Schlüssel, jedoch kann bei jeder Verwendung, bei der das Mapping signiert ist, Duplikate zu einem Signatur-Fehler führen.

* Mappings, die in I2NP-Nachrichten enthalten sind (z.B. in einer RouterAddress oder RouterInfo), müssen nach Schlüssel sortiert sein, damit die Signatur unveränderlich ist. Doppelte Schlüssel sind nicht erlaubt.

* Zuordnungen, die in einer [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig) enthalten sind, müssen nach Schlüssel sortiert sein, damit
  die Signatur invariant ist. Doppelte Schlüssel sind nicht erlaubt.

* Die Sortierungsmethode ist wie in Java String.compareTo() definiert und verwendet den Unicode-Wert der Zeichen.

* Obwohl es anwendungsabhängig ist, sind Schlüssel und Werte im Allgemeinen
  groß-/kleinschreibungsabhängig.

* Die Längenbegrenzungen für Schlüssel- und Wert-Strings betragen jeweils 255 Bytes (nicht Zeichen), plus das Längen-Byte. Das Längen-Byte kann 0 sein.

* Die Gesamtlängenbegrenzung beträgt 65535 Bytes, plus das 2-Byte-Größenfeld, oder insgesamt 65537.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## Allgemeine Strukturspezifikation

### KeysAndCert

#### Beschreibung

Ein öffentlicher Verschlüsselungsschlüssel, ein öffentlicher Signaturschlüssel und ein Zertifikat, verwendet entweder als RouterIdentity oder als Destination.

#### Inhalt

Ein [PublicKey](#publickey) gefolgt von einem [SigningPublicKey](#signingpublickey) und dann einem [Certificate](#certificate).

```
+----+----+----+----+----+----+----+----+
| public_key                            |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| padding (optional)                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| certificate                           |
+----+----+----+-/

public_key :: `PublicKey` (partial or full)
              length -> 256 bytes or as specified in key certificate

padding :: random data
           length -> 0 bytes or as specified in key certificate
           public_key length + padding length + signing_key length == 384 bytes

signing__key :: `SigningPublicKey` (partial or full)
                length -> 128 bytes or as specified in key certificate

certificate :: `Certificate`
               length -> >= 3 bytes

total length: 387+ bytes
```
#### Richtlinien zur Padding-Generierung

Diese Richtlinien wurden in Proposal 161 vorgeschlagen und in API-Version 0.9.57 implementiert. Diese Richtlinien sind rückwärtskompatibel mit allen Versionen seit 0.6 (2005). Siehe Proposal 161 für Hintergrundinformationen und weitere Details.

Für jede aktuell verwendete Kombination von Schlüsseltypen außer ElGamal + DSA-SHA1 wird Padding vorhanden sein. Zusätzlich ist bei Destinations das 256-Byte Public-Key-Feld seit Version 0.6 (2005) ungenutzt.

Implementierer sollten die zufälligen Daten für öffentliche Destination-Schlüssel sowie das Padding von Destination- und Router-Identitäten so generieren, dass sie in verschiedenen I2P-Protokollen komprimierbar bleiben und dennoch sicher sind, ohne dass Base64-Darstellungen beschädigt oder unsicher erscheinen. Dies bietet die meisten Vorteile der Entfernung der Padding-Felder ohne störende Protokolländerungen.

Streng genommen ist der 32-Byte-Signatur-Public-Key allein (sowohl in Destinations als auch in Router Identities) und der 32-Byte-Verschlüsselungs-Public-Key (nur in Router Identities) eine Zufallszahl, die die gesamte Entropie liefert, die für die SHA-256-Hashes dieser Strukturen erforderlich ist, um kryptographisch stark und zufällig im netDb DHT verteilt zu sein.

Aus Vorsichtsgründen empfehlen wir jedoch, mindestens 32 Bytes an Zufallsdaten im ElG-Public-Key-Feld und der Auffüllung zu verwenden. Wenn die Felder alle Nullen wären, würden Base64-Zieladressen außerdem lange Folgen von AAAA-Zeichen enthalten, was bei Benutzern Alarm oder Verwirrung auslösen könnte.

Wiederholen Sie die 32 Bytes zufälliger Daten nach Bedarf, damit die vollständige KeysAndCert-Struktur in I2P-Protokollen wie I2NP Database Store Message, Streaming SYN, SSU2 handshake und repliable Datagrams hoch komprimierbar ist.

Beispiele:

* Eine Router Identity mit X25519-Verschlüsselungstyp und Ed25519-Signaturtyp
  wird 10 Kopien (320 Bytes) der Zufallsdaten enthalten, was eine Ersparnis von etwa 288 Bytes bei der Komprimierung bedeutet.

* Eine Destination mit Ed25519-Signaturtyp
  wird 11 Kopien (352 Bytes) der Zufallsdaten enthalten, was eine Einsparung von etwa 320 Bytes bei der Komprimierung bedeutet.

Implementierungen müssen natürlich die vollständige 387+ Byte-Struktur speichern, da der SHA-256-Hash der Struktur den gesamten Inhalt abdeckt.

#### Hinweise

* Gehen Sie nicht davon aus, dass diese immer 387 Bytes lang sind! Sie sind 387 Bytes plus die Zertifikatslänge, die bei den Bytes 385-386 angegeben ist und die ungleich null sein kann.

* Ab Version 0.9.12 können sich die Grenzen der Schlüsselfelder variieren, wenn das Zertifikat ein Key Certificate ist. Siehe den Abschnitt Key Certificate oben für Details.

* Der Crypto Public Key ist am Anfang ausgerichtet und der Signing Public Key ist
  am Ende ausgerichtet. Das Padding (falls vorhanden) befindet sich in der Mitte.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### Beschreibung

Definiert die Art, wie ein bestimmter router eindeutig identifiziert wird

#### Inhaltsverzeichnis

Identisch zu KeysAndCert.

Siehe [KeysAndCert](#keysandcert) für Richtlinien zur Generierung der Zufallsdaten für das Padding-Feld.

#### Notizen

* Das Zertifikat für eine RouterIdentity war bis zur Version 0.9.12 immer NULL.

* Gehen Sie nicht davon aus, dass diese immer 387 Bytes groß sind! Sie sind 387 Bytes plus der Zertifikatslänge, die in den Bytes 385-386 angegeben ist, welche ungleich null sein kann.

* Ab Release 0.9.12 können sich die Grenzen der Schlüsselfelder variieren, wenn das Zertifikat ein Key Certificate ist. Siehe den Abschnitt Key Certificate oben für Details.

* Der Crypto Public Key ist am Anfang ausgerichtet und der Signing Public Key ist
  am Ende ausgerichtet. Das Padding (falls vorhanden) befindet sich in der Mitte.

* RouterIdentities mit einem Schlüsselzertifikat und einem ECIES_X25519 öffentlichen Schlüssel
  werden seit Release 0.9.48 unterstützt.
  Davor waren alle RouterIdentities ElGamal.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### Ziel

#### Beschreibung

Eine Destination definiert einen bestimmten Endpunkt, an den Nachrichten zur sicheren Zustellung gerichtet werden können.

#### Inhaltsverzeichnis

Identisch zu [KeysAndCert](#keysandcert), außer dass der öffentliche Schlüssel niemals verwendet wird und anstelle eines gültigen ElGamal Public Key zufällige Daten enthalten kann.

Siehe [KeysAndCert](#keysandcert) für Richtlinien zur Generierung der Zufallsdaten für die Felder des öffentlichen Schlüssels und der Auffüllung.

#### Notizen

* Der öffentliche Schlüssel des Ziels wurde für die alte i2cp-to-i2cp-Verschlüsselung verwendet, die in Version 0.6 (2005) deaktiviert wurde. Er wird derzeit nicht verwendet, außer als IV für die LeaseSet-Verschlüsselung, welche veraltet ist. Stattdessen wird der öffentliche Schlüssel im LeaseSet verwendet.

* Gehen Sie nicht davon aus, dass diese immer 387 Bytes sind! Sie sind 387 Bytes plus der Zertifikatslänge, die in den Bytes 385-386 angegeben ist, welche ungleich null sein kann.

* Ab Release 0.9.12 können die Grenzen der Schlüsselfelder variieren, wenn das Zertifikat ein Key Certificate ist. Siehe den Abschnitt Key Certificate oben für Details.

* Der Crypto Public Key ist am Anfang ausgerichtet und der Signing Public Key ist
  am Ende ausgerichtet. Die Auffüllung (falls vorhanden) befindet sich in der Mitte.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### Beschreibung

Definiert die Autorisierung für einen bestimmten tunnel, Nachrichten zu empfangen, die auf eine [Destination](#destination) abzielen.

#### Inhaltsverzeichnis

SHA256 [Hash](#hash) der [RouterIdentity](#routeridentity) des Gateway-routers, dann die [TunnelId](#tunnelid), und schließlich ein End-[Date](#date).

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date
+----+----+----+----+----+----+----+----+
                    |
+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: `Date`
            length -> 8 bytes
```
#### Notizen

* Gesamtgröße: 44 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### Beschreibung

Enthält alle derzeit autorisierten [Leases](#lease) für ein bestimmtes [Destination](#destination), den [PublicKey](#publickey), mit dem garlic-Nachrichten verschlüsselt werden können, und dann den [SigningPublicKey](#signingpublickey), der verwendet werden kann, um diese bestimmte Version der Struktur zu widerrufen. Das LeaseSet ist eine der beiden Strukturen, die in der Netzwerkdatenbank gespeichert werden (die andere ist [RouterInfo](#routerinfo)), und wird unter dem SHA256 des enthaltenen [Destination](#destination) indiziert.

#### Inhalt

[Destination](#destination), gefolgt von einem [PublicKey](#publickey) für die Verschlüsselung, dann einem [SigningPublicKey](#signingpublickey), der verwendet werden kann, um diese Version des LeaseSet zu widerrufen, dann einem 1-Byte [Integer](#integer), der angibt, wie viele [Lease](#lease)-Strukturen im Set enthalten sind, gefolgt von den tatsächlichen [Lease](#lease)-Strukturen und schließlich einer [Signature](#signature) der vorherigen Bytes, die mit dem [SigningPrivateKey](#signingprivatekey) der [Destination](#destination) signiert wurde.

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| encryption_key                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease 0                          |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease 1                               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease ($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

encryption_key :: `PublicKey`
                  length -> 256 bytes

signing_key :: `SigningPublicKey`
               length -> 128 bytes or as specified in destination's key
                         certificate

num :: `Integer`
       length -> 1 byte
       Number of leases to follow
       value: 0 <= num <= 16

leases :: [`Lease`]
          length -> $num*44 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate
```
#### Notizen

* Der öffentliche Schlüssel des Ziels wurde für die alte I2CP-zu-I2CP-Verschlüsselung verwendet, die in Version 0.6 deaktiviert wurde und derzeit nicht genutzt wird.

* Der Verschlüsselungsschlüssel wird für die Ende-zu-Ende ElGamal/AES+SessionTag-Verschlüsselung
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) verwendet. Er wird derzeit bei jedem router-Start neu generiert und ist
  nicht persistent.

* Die Signatur kann mit dem öffentlichen Signaturschlüssel des
  Ziels verifiziert werden.

* Ein LeaseSet mit null Leases ist erlaubt, wird aber nicht verwendet.
  Es war für LeaseSet-Widerruf vorgesehen, der nicht implementiert ist.
  Alle LeaseSet2-Varianten erfordern mindestens einen Lease.

* Der signing_key wird derzeit nicht verwendet. Er war für LeaseSet-Widerruf vorgesehen, welcher nicht implementiert ist. Er wird derzeit bei jedem Router-Start neu generiert und ist nicht persistent. Der Signing-Key-Typ ist immer derselbe wie der Signing-Key-Typ des Ziels.

* Die früheste Ablaufzeit aller Leases wird als Zeitstempel oder Version des LeaseSet behandelt. Router akzeptieren im Allgemeinen keine Speicherung eines LeaseSet, es sei denn, es ist "neuer" als das aktuelle. Seien Sie vorsichtig beim Veröffentlichen eines neuen LeaseSet, bei dem der älteste Lease derselbe ist wie der älteste Lease im vorherigen LeaseSet. Der veröffentlichende Router sollte in diesem Fall im Allgemeinen die Ablaufzeit des ältesten Lease um mindestens 1 ms erhöhen.

* Vor Release 0.9.7 setzte der router, wenn er in einer DatabaseStore Message vom ursprünglichen router enthalten war, alle Ablaufzeiten der veröffentlichten leases auf denselben Wert, nämlich den des frühesten lease. Ab Release 0.9.7 veröffentlicht der router die tatsächliche lease-Ablaufzeit für jeden lease. Dies ist ein Implementierungsdetail und nicht Teil der Strukturspezifikation.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### Beschreibung

Definiert die Autorisierung für einen bestimmten tunnel, Nachrichten zu empfangen, die auf eine [Destination](#destination) abzielen. Identisch mit [Lease](#lease), aber mit einem 4-Byte end_date. Wird von [LeaseSet2](#leaseset2) verwendet. Unterstützt seit 0.9.38; siehe Vorschlag 123 für weitere Informationen.

#### Inhalt

SHA256 [Hash](#hash) der [RouterIdentity](#routeridentity) des Gateway-Routers, dann die [TunnelId](#tunnelid) und schließlich ein 4-Byte-Enddatum.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Hinweise

* Gesamtgröße: 40 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### Beschreibung

Dies ist ein optionaler Teil des [LeaseSet2Header](#leaseset2header). Wird auch beim Streaming und I2CP verwendet. Unterstützt seit 0.9.38; siehe Vorschlag 123 für weitere Informationen.

#### Inhalt

Enthält ein Ablaufdatum, einen sigtype und einen transient [SigningPublicKey](#signingpublickey), sowie eine [Signature](#signature).

```
+----+----+----+----+----+----+----+----+
|     expires       | sigtype |         |
+----+----+----+----+----+----+         +
|       transient_public_key            |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|           signature                   |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

expires :: 4 byte date
           length -> 4 bytes
           Seconds since the epoch, rolls over in 2106.

sigtype :: 2 byte type of the transient_public_key
           length -> 2 bytes

transient_public_key :: `SigningPublicKey`
                        length -> As inferred from the sigtype

signature :: `Signature`
             length -> As inferred from the sigtype of the signing public key
                       in the `Destination` that preceded this offline signature.
             Signature of expires timestamp, transient sig type, and public key,
             by the destination public key.

```
#### Hinweise

* Dieser Abschnitt kann und sollte offline generiert werden.

### LeaseSet2Header

#### Beschreibung

Dies ist der gemeinsame Teil des [LeaseSet2](#leaseset2) und [MetaLeaseSet](#metaleaseset). Unterstützt seit 0.9.38; siehe Vorschlag 123 für weitere Informationen.

#### Inhalt

Enthält die [Destination](#destination), zwei Zeitstempel und eine optionale [OfflineSignature](#offlinesignature).

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one, unless bit 2 is set.
  Bit 2: If 0, a standard published leaseset.
         If 1, this unencrypted leaseset will be blinded and encrypted when published.
         If this leaseset expires, query the blinded location in the netdb for a new one.
         If this bit is set to 1, set bit 1 to 1 also.
         As of release 0.9.42.
  Bits 15-3: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

```
#### Notizen

* Gesamtgröße: 395 Bytes mindestens

* Die maximale tatsächliche Ablaufzeit beträgt etwa 660 (11 Minuten) für
  [LeaseSet2](#leaseset2) und 65535 (die vollen 18,2 Stunden) für [MetaLeaseSet](#metaleaseset).

* [LeaseSet](#leaseset) (1) hatte kein 'published'-Feld, daher erforderte die Versionierung
  eine Suche nach dem frühesten Lease. LeaseSet2 fügt ein 'published'-Feld
  mit einer Auflösung von einer Sekunde hinzu. Router sollten das Senden
  neuer leasesets an floodfills auf eine Rate beschränken, die deutlich langsamer als einmal pro Sekunde ist (pro Ziel).
  Wenn dies nicht implementiert ist, muss der Code sicherstellen, dass jeder neue leaseset
  eine 'published'-Zeit hat, die mindestens eine Sekunde später liegt als die vorherige, sonst
  werden floodfills den neuen leaseset nicht speichern oder weiterleiten.

### LeaseSet2

#### Beschreibung

Enthalten in einer I2NP DatabaseStore-Nachricht vom Typ 3. Unterstützt seit 0.9.38; siehe Vorschlag 123 für weitere Informationen.

Enthält alle aktuell autorisierten [Lease2](#lease2) für eine bestimmte [Destination](#destination) und den [PublicKey](#publickey), mit dem garlic messages verschlüsselt werden können. Ein LeaseSet ist eine der beiden Strukturen, die in der Netzwerkdatenbank gespeichert werden (die andere ist [RouterInfo](#routerinfo)), und wird unter dem SHA256 der enthaltenen [Destination](#destination) indiziert.

#### Inhaltsverzeichnis

[LeaseSet2Header](#leaseset2header), gefolgt von Optionen, dann einem oder mehreren [PublicKey](#publickey) für die Verschlüsselung, [Integer](#integer) der angibt, wie viele [Lease2](#lease2) Strukturen im Set enthalten sind, gefolgt von den eigentlichen [Lease2](#lease2) Strukturen und schließlich einer [Signature](#signature) der vorherigen Bytes, signiert durch den [SigningPrivateKey](#signingprivatekey) des [Destination](#destination) oder den transienten Schlüssel.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numk| keytype0| keylen0 |              |
+----+----+----+----+----+              +
|          encryption_key_0             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| keytypen| keylenn |                   |
+----+----+----+----+                   +
|          encryption_key_n             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease2 0                         |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease2($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

numk :: `Integer`
        length -> 1 byte
        Number of key types, key lengths, and `PublicKey`s to follow
        value: 1 <= numk <= max TBD

keytype :: The encryption type of the `PublicKey` to follow.
           length -> 2 bytes

keylen :: The length of the `PublicKey` to follow.
          Must match the specified length of the encryption type.
          length -> 2 bytes

encryption_key :: `PublicKey`
                  length -> keylen bytes

num :: `Integer`
       length -> 1 byte
       Number of `Lease2`s to follow
       value: 0 <= num <= 16

leases :: [`Lease2`]
          length -> $num*40 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Verschlüsselungsschlüssel-Präferenz

Für veröffentlichte (Server) leaseSets sind die Verschlüsselungsschlüssel nach Serverpräferenz geordnet, mit dem am meisten bevorzugten zuerst. Wenn Clients mehr als einen Verschlüsselungstyp unterstützen, wird empfohlen, dass sie die Serverpräferenz respektieren und den ersten unterstützten Typ als Verschlüsselungsmethode für die Verbindung zum Server auswählen. Im Allgemeinen sind die neueren (höher nummerierten) Schlüsseltypen sicherer oder effizienter und werden bevorzugt, daher sollten die Schlüssel in umgekehrter Reihenfolge des Schlüsseltyps aufgelistet werden.

Clients können jedoch implementierungsabhängig stattdessen basierend auf ihrer Präferenz auswählen oder eine Methode verwenden, um die "kombinierte" Präferenz zu bestimmen. Dies kann als Konfigurationsoption oder zum Debugging nützlich sein.

Die Schlüsselreihenfolge in unveröffentlichten (Client-) leaseSets ist praktisch irrelevant, da normalerweise keine Verbindungsversuche zu unveröffentlichten Clients unternommen werden. Es sei denn, diese Reihenfolge wird verwendet, um eine kombinierte Präferenz zu bestimmen, wie oben beschrieben.

#### Optionen

Ab API 0.9.66 ist ein Standardformat für Service-Record-Optionen definiert. Siehe Proposal 167 für Details. Optionen außer Service Records, die ein anderes Format verwenden, können in Zukunft definiert werden.

LS2-Optionen MÜSSEN nach Schlüssel sortiert sein, damit die Signatur unveränderlich ist.

Service-Datensatz-Optionen sind wie folgt definiert:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Der symbolische Name des gewünschten Dienstes. Muss kleingeschrieben sein. Beispiel: "smtp".
  Erlaubte Zeichen sind [a-z0-9-] und dürfen nicht mit '-' beginnen oder enden.
  Standard-Bezeichner aus [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) oder Linux /etc/services müssen verwendet werden, falls dort definiert.
- proto := Das Transportprotokoll des gewünschten Dienstes. Muss kleingeschrieben sein, entweder "tcp" oder "udp".
  "tcp" bedeutet Streaming und "udp" bedeutet antwortfähige Datagramme.
  Protokollindikatoren für Raw-Datagramme und datagram2 können später definiert werden.
  Erlaubte Zeichen sind [a-z0-9-] und dürfen nicht mit '-' beginnen oder enden.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := Time to live (Lebensdauer), ganzzahlige Sekunden. Positive Ganzzahl. Beispiel: "86400".
  Ein Minimum von 86400 (ein Tag) wird empfohlen, siehe Abschnitt Empfehlungen unten für Details.
- priority := Die Priorität des Ziel-Hosts, niedrigerer Wert bedeutet bevorzugter. Nicht-negative Ganzzahl. Beispiel: "0"
  Nur nützlich bei mehr als einem Eintrag, aber auch bei nur einem Eintrag erforderlich.
- weight := Ein relatives Gewicht für Einträge mit derselben Priorität. Höherer Wert bedeutet größere Chance, ausgewählt zu werden. Nicht-negative Ganzzahl. Beispiel: "0"
  Nur nützlich bei mehr als einem Eintrag, aber auch bei nur einem Eintrag erforderlich.
- port := Der I2CP-Port, auf dem der Dienst zu finden ist. Nicht-negative Ganzzahl. Beispiel: "25"
  Port 0 wird unterstützt, aber nicht empfohlen.
- target := Der Hostname oder b32 des Ziels, das den Dienst bereitstellt. Ein gültiger Hostname wie in [NAMING](/docs/overview/naming/). Muss kleingeschrieben sein.
  Beispiel: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" oder "example.i2p".
  b32 wird empfohlen, es sei denn, der Hostname ist "allgemein bekannt", d.h. in offiziellen oder Standard-Adressbüchern.
- appoptions := beliebiger anwendungsspezifischer Text, darf keine " " oder "," enthalten. Kodierung ist UTF-8.

Beispiele:

In LS2 für aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, verweisend auf einen SMTP-Server:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

In LS2 für aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, zeigend auf zwei SMTP-Server:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

In LS2 für bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, zeigend auf sich selbst als SMTP-Server:

"_smtp._tcp" "0 999999 25"

#### Notizen

* Der öffentliche Schlüssel des Ziels wurde für die alte I2CP-zu-I2CP-Verschlüsselung verwendet, die in Version 0.6 deaktiviert wurde und derzeit nicht genutzt wird.

* Die Verschlüsselungsschlüssel werden für End-to-End ElGamal/AES+SessionTag-Verschlüsselung
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (Typ 0) oder andere End-to-End-Verschlüsselungsverfahren verwendet.
  Siehe [ECIES](/docs/specs/ecies/) und Vorschläge 145 und 156.
  Sie können bei jedem router-Start neu generiert werden
  oder persistent sein.
  X25519 (Typ 4, siehe [ECIES](/docs/specs/ecies/)) wird ab Version 0.9.44 unterstützt.

* Die Signatur bezieht sich auf die obigen Daten, VORANGESTELLT mit dem einzelnen Byte, das den DatabaseStore-Typ (3) enthält.

* Die Signatur kann mit dem öffentlichen Signaturschlüssel des
  Ziels oder dem temporären öffentlichen Signaturschlüssel verifiziert werden,
  falls eine Offline-Signatur im leaseset2-Header enthalten ist.

* Die Schlüssellänge wird für jeden Schlüssel bereitgestellt, damit floodfills und Clients
  die Struktur parsen können, auch wenn nicht alle Verschlüsselungstypen bekannt oder unterstützt sind.

* Siehe Hinweis zum 'published'-Feld in [LeaseSet2Header](#leaseset2header)

* Das Options-Mapping muss, wenn die Größe größer als eins ist, nach Schlüssel sortiert sein, damit die Signatur unveränderlich ist.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### Beschreibung

Definiert die Autorisierung für einen bestimmten tunnel, Nachrichten zu empfangen, die auf eine [Destination](#destination) abzielen. Wie [Lease2](#lease2), aber mit Flags und Kosten anstelle einer tunnel-ID. Wird von [MetaLeaseSet](#metaleaseset) verwendet. Enthalten in einer I2NP DatabaseStore-Nachricht vom Typ 7. Unterstützt ab Version 0.9.38; siehe Vorschlag 123 für weitere Informationen.

#### Inhalt

SHA256 [Hash](#hash) der [RouterIdentity](#routeridentity) des Gateway-Routers, dann Flags und Kosten, und schließlich ein 4-Byte-Enddatum.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|    flags     |cost|      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway,
             or the hash of another `MetaLeaseSet`.
             length -> 32 bytes

flags :: 3 bytes of flags
         Bit order: 23 22 ... 3 2 1 0
         Bits 3-0: Type of the entry.
         If 0, unknown.
         If 1, a `LeaseSet`.
         If 3, a `LeaseSet2`.
         If 5, a `MetaLeaseSet`.
         Bits 23-4: set to 0 for compatibility with future uses
         length -> 3 bytes

cost :: 1 byte, 0-255. Lower value is higher priority.
        length -> 1 byte

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Notizen

* Gesamtgröße: 40 Bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### Beschreibung

Enthalten in einer I2NP DatabaseStore-Nachricht vom Typ 7. Definiert ab Version 0.9.38; geplant funktionsfähig ab Version 0.9.40; siehe Vorschlag 123 für weitere Informationen.

Enthält alle derzeit autorisierten [MetaLease](#metalease) für eine bestimmte [Destination](#destination) und den [PublicKey](#publickey), mit dem Garlic-Nachrichten verschlüsselt werden können. Ein leaseSet ist eine der beiden Strukturen, die in der Netzwerkdatenbank gespeichert werden (die andere ist [RouterInfo](#routerinfo)), und wird unter dem SHA256-Hash der enthaltenen [Destination](#destination) indexiert.

#### Inhalt

[LeaseSet2Header](#leaseset2header), gefolgt von Optionen, [Integer](#integer) der angibt, wie viele [Lease2](#lease2) Strukturen im Set enthalten sind, gefolgt von den tatsächlichen [Lease2](#lease2) Strukturen und schließlich einer [Signature](#signature) der vorherigen Bytes, signiert mit dem [SigningPrivateKey](#signingprivatekey) der [Destination](#destination) oder dem transienten Schlüssel.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| MetaLease 0                      |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| MetaLease($num-1)                     |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numr|                                  |
+----+                                  +
|          revocation_0                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          revocation_n                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

num :: `Integer`
        length -> 1 byte
        Number of `MetaLease`s to follow
        value: 1 <= num <= max TBD

leases :: `MetaLease`s
          length -> $numr*40 bytes

numr :: `Integer`
        length -> 1 byte
        Number of `Hash`es to follow
        value: 0 <= numr <= max TBD

revocations :: [`Hash`]
               length -> $numr*32 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Hinweise

* Der öffentliche Schlüssel des Ziels wurde für die alte I2CP-zu-I2CP-Verschlüsselung verwendet, die in Version 0.6 deaktiviert wurde und derzeit nicht verwendet wird.

* Die Signatur erstreckt sich über die obigen Daten, VORANGESTELLT mit dem einzelnen Byte, das den DatabaseStore-Typ (7) enthält.

* Die Signatur kann mit dem öffentlichen Signaturschlüssel des
  Ziels oder dem temporären öffentlichen Signaturschlüssel verifiziert werden, wenn eine Offline-Signatur
  im leaseset2-Header enthalten ist.

* Siehe Hinweis zum 'published'-Feld in [LeaseSet2Header](#leaseset2header)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### Beschreibung

Enthalten in einer I2NP DatabaseStore-Nachricht vom Typ 5. Definiert seit 0.9.38; funktionsfähig seit 0.9.39; siehe Vorschlag 123 für weitere Informationen.

Nur der blinded Key und das Ablaufdatum sind im Klartext sichtbar. Das eigentliche leaseSet ist verschlüsselt.

#### Inhalt

Ein zwei Byte Signaturtyp, der blinded [SigningPrivateKey](#signingprivatekey), Veröffentlichungszeit, Ablaufzeit und Flags. Dann eine zwei Byte Länge gefolgt von verschlüsselten Daten. Schließlich eine [Signature](#signature) der vorherigen Bytes, signiert durch den blinded [SigningPrivateKey](#signingprivatekey) oder den transienten Schlüssel.

```
+----+----+----+----+----+----+----+----+
| sigtype |                             |
+----+----+                             +
|        blinded_public_key             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  len    |                             |
+----+----+                             +
|         encrypted_data                |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

sigtype :: A two byte signature type of the public key to follow
           length -> 2 bytes

blinded_public_key :: `SigningPublicKey`
                      length -> As inferred from the sigtype

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one.
  Bits 15-2: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

len :: `Integer`
        length -> 2 bytes
        length of encrypted_data to follow
        value: 1 <= num <= max TBD

encrypted_data :: Data encrypted
                  length -> len bytes

signature :: `Signature`
             length -> As specified by the sigtype of the blinded pubic key,
                       or by the sigtype of the transient public key,
                       if present in the header

```
#### Notizen

* Der öffentliche Schlüssel des Ziels wurde für die alte I2CP-zu-I2CP-Verschlüsselung verwendet, die in Version 0.6 deaktiviert wurde; er wird derzeit nicht verwendet.

* Die Signatur bezieht sich auf die oben genannten Daten, VORANGESTELLT mit dem einzelnen Byte, das den DatabaseStore-Typ (5) enthält.

* Die Signatur kann mit dem öffentlichen Signaturschlüssel des
  Ziels oder dem temporären öffentlichen Signaturschlüssel verifiziert werden,
  falls eine Offline-Signatur im leaseset2-Header enthalten ist.

* Blinding und Verschlüsselung sind in [EncryptedLeaseSet](/docs/specs/encryptedleaseset/) spezifiziert

* Diese Struktur verwendet nicht den [LeaseSet2Header](#leaseset2header).

* Die maximale tatsächliche Ablaufzeit beträgt etwa 660 (11 Minuten), es sei denn,
  es handelt sich um ein verschlüsseltes [MetaLeaseSet](#metaleaseset).

* Siehe Proposal 123 für Hinweise zur Verwendung von Offline-Signaturen
  mit verschlüsselten leaseSets.

* Siehe Hinweis zum 'published'-Feld in [LeaseSet2Header](#leaseset2header)
  (gleiches Problem, obwohl wir das LeaseSet2Header-Format hier nicht verwenden)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### Beschreibung

Diese Struktur definiert die Mittel, um einen Router über ein Transportprotokoll zu kontaktieren.

#### Inhaltsverzeichnis

1 Byte [Integer](#integer), der die relativen Kosten für die Verwendung der Adresse definiert, wobei 0 kostenlos und 255 teuer ist, gefolgt vom Ablauf-[Date](#date), nach dem die Adresse nicht mehr verwendet werden sollte, oder wenn null, läuft die Adresse niemals ab. Danach kommt ein [String](#string), der das Transportprotokoll definiert, das diese router-Adresse verwendet. Schließlich gibt es ein [Mapping](#mapping), das alle transportspezifischen Optionen enthält, die zum Aufbau der Verbindung erforderlich sind, wie IP-Adresse, Port-Nummer, E-Mail-Adresse, URL usw.

```
+----+----+----+----+----+----+----+----+
|cost|           expiration
+----+----+----+----+----+----+----+----+
     |        transport_style           |
+----+----+----+----+-/-+----+----+----+
|                                       |
+                                       +
|               options                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

cost :: `Integer`
        length -> 1 byte

        case 0 -> free
        case 255 -> expensive

expiration :: `Date` (must be all zeros, see notes below)
              length -> 8 bytes

              case null -> never expires

transport_style :: `String`
                   length -> 1-256 bytes

options :: `Mapping`
```
#### Hinweise

* Die Kosten betragen normalerweise 5 oder 6 für SSU und 10 oder 11 für NTCP.

* Expiration wird derzeit nicht verwendet, immer null (alle Nullen). Ab Release 0.9.3 wird die Expiration als Null angenommen und nicht gespeichert, daher wird jede Expiration ungleich Null bei der RouterInfo-Signaturverifikation fehlschlagen. Die Implementierung einer Expiration (oder eine andere Verwendung für diese Bytes) wird eine rückwärts-inkompatible Änderung sein. Router MÜSSEN dieses Feld auf alle Nullen setzen. Ab Release 0.9.12 wird ein Expiration-Feld ungleich Null wieder erkannt, jedoch müssen wir mehrere Releases abwarten, um dieses Feld zu verwenden, bis die große Mehrheit des Netzwerks es erkennt.

* Die folgenden Optionen sind zwar nicht erforderlich, aber standardmäßig vorhanden und werden in den meisten Router-Adressen erwartet: "host" (eine IPv4- oder IPv6-Adresse oder ein Hostname) und "port".

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### Beschreibung

Definiert alle Daten, die ein router im Netzwerk veröffentlichen möchte. Die [RouterInfo](#routerinfo) ist eine von zwei Strukturen, die in der Netzwerkdatenbank gespeichert werden (die andere ist [LeaseSet](#leaseset)), und wird unter dem SHA256-Hash der enthaltenen [RouterIdentity](#routeridentity) indiziert.

#### Inhalt

[RouterIdentity](#routeridentity) gefolgt vom [Date](#date), wann der Eintrag veröffentlicht wurde

```
+----+----+----+----+----+----+----+----+
| router_ident                          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| published                             |
+----+----+----+----+----+----+----+----+
|size| RouterAddress 0                  |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress 1                       |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress ($size-1)               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+-/-+----+----+----+
|psiz| options                          |
+----+----+----+----+-/-+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

router_ident :: `RouterIdentity`
                length -> >= 387+ bytes

published :: `Date`
             length -> 8 bytes

size :: `Integer`
        length -> 1 byte
        The number of `RouterAddress`es to follow, 0-255

addresses :: [`RouterAddress`]
             length -> varies

peer_size :: `Integer`
             length -> 1 byte
             The number of peer `Hash`es to follow, 0-255, unused, always zero
             value -> 0

options :: `Mapping`

signature :: `Signature`
             length -> 40 bytes or as specified in router_ident's key
                       certificate
```
#### Notizen

* Die peer_size [Integer](#integer) kann von einer Liste mit so vielen router hashes gefolgt werden.
  Dies wird derzeit nicht verwendet. Es war für eine Form von eingeschränkten Routen gedacht,
  die nicht implementiert ist.
  Bestimmte Implementierungen könnten erfordern, dass die Liste sortiert ist, damit die Signatur unveränderlich ist.
  Dies muss erforscht werden, bevor diese Funktion aktiviert wird.

* Die Signatur kann mit dem öffentlichen Signaturschlüssel der
  router_ident verifiziert werden.

* Siehe die Netzwerkdatenbank-Seite [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) für Standardoptionen, die
  in allen router infos vorhanden sein sollten.

* Sehr alte router verlangten, dass die Adressen nach dem SHA256 ihrer Daten sortiert werden,
  damit die Signatur unveränderlich ist.
  Dies ist nicht mehr erforderlich und nicht der Mühe wert, für Rückwärtskompatibilität implementiert zu werden.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### Zustellungsanweisungen

Tunnel Message Delivery Instructions sind in der Tunnel Message Specification [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions) definiert.

Garlic Message Delivery Instructions sind in der I2NP Message Specification [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions) definiert.

## Referenzen

- [ECIES](/docs/specs/ecies/)
- [ECIES-HYBRID](/docs/specs/ecies-hybrid/)
- [ECIES-ROUTERS](/docs/specs/ecies-routers/)
- [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy)
- [ELGAMAL-AES](/docs/specs/elgamal-aes/)
- [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions)
- [I2CP](/docs/specs/i2cp/)
- [I2NP](/docs/specs/i2np/)
- [NAMING](/docs/overview/naming/)
- [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo)
- [Prop134](/proposals/134-gost/)
- [Prop169](/proposals/169-pq-crypto/)
- [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
- [SSU](/docs/legacy/ssu/)
- [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions)

---
title: "B32 pour les Leasesets Chiffrés"
description: "Format d'adresse Base 32 pour les leaseSets LS2 chiffrés"
slug: "b32encrypted"
aliases:
  - "/fr/docs/specs/b32-for-encrypted-leasesets"
  - "/fr/docs/specs/b32-for-encrypted-leasesets/"
category: "Conception"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## Aperçu

Les adresses Base 32 standard ("b32") contiennent le hachage de la destination. Cela ne fonctionnera pas pour les ls2 chiffrés (proposition 123).

Nous ne pouvons pas utiliser une adresse base 32 traditionnelle pour un leaseSet chiffré LS2 (proposition 123), car elle ne contient que le hash de la destination. Elle ne fournit pas la clé publique non aveuglée. Les clients doivent connaître la clé publique de la destination, le type de signature, le type de signature aveuglée, et une clé secrète ou privée optionnelle pour récupérer et déchiffrer le leaseSet. Par conséquent, une adresse base 32 seule est insuffisante. Le client a besoin soit de la destination complète (qui contient la clé publique), soit de la clé publique seule. Si le client a la destination complète dans un carnet d'adresses, et que le carnet d'adresses prend en charge la recherche inversée par hash, alors la clé publique peut être récupérée.

Ce format place la clé publique au lieu du hash dans une adresse base32. Ce format doit également contenir le type de signature de la clé publique et le type de signature du schéma de masquage.

Ce document spécifie un format b32 pour ces adresses. Bien que nous ayons fait référence à ce nouveau format lors des discussions comme une adresse "b33", le nouveau format actuel conserve le suffixe habituel ".b32.i2p".

## Conception

- Le nouveau format contiendra la clé publique non aveuglée, le type de signature non aveuglée,
  et le type de signature aveuglée.
- Contenir optionnellement un secret et/ou une clé privée, uniquement pour les liens privés
- Utiliser le suffixe ".b32.i2p" existant, mais avec une longueur plus importante.
- Ajouter une somme de contrôle.
- Les adresses pour les leasesets chiffrés sont identifiées par 56 caractères encodés
  ou plus (35 octets décodés ou plus), comparé à 52 caractères (32
  octets) pour les adresses base 32 traditionnelles.

## Spécification

### Création et encodage

Construisez un nom d'hôte de {56+ caractères}.b32.i2p (35+ caractères en binaire) comme suit :

```
flag (1 byte)
    bit 0: 0 for one-byte sigtypes, 1 for two-byte sigtypes
    bit 1: 0 for no secret, 1 if secret is required
    bit 2: 0 for no per-client auth, 1 if client private key is required
    bits 7-3: Unused, set to 0

public key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

blinded key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

public key
    Number of bytes as implied by sigtype
```
Post-traitement et somme de contrôle :

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
Tous les bits inutilisés à la fin du b32 doivent être à 0. Il n'y a pas de bits inutilisés pour une adresse standard de 56 caractères (35 octets).

### Décodage et Vérification

```
strip the ".b32.i2p" from the hostname
data = Base32.decode(hostname)
Calculate checksum = CRC-32(data[3:end])
Treat checksum as little-endian.
flags = data[0] ^ (byte) checksum
if 1 byte sigtypes:
    pubkey sigtype = data[1] ^ (byte) (checksum >> 8)
    blinded sigtype = data[2] ^ (byte) (checksum >> 16)
else (2 byte sigtypes):
    pubkey sigtype = data[1] ^ ((byte) (checksum >> 8)) || data[2] ^ ((byte) (checksum >> 16))
    blinded sigtype = data[3] || data[4]
parse the remainder based on the flags to get the public key
```
### Bits de Clé Secrète et Privée

Les bits de clé secrète et privée sont utilisés pour indiquer aux clients, proxies, ou autre code côté client que la clé secrète et/ou privée sera nécessaire pour déchiffrer le leaseSet. Des implémentations particulières peuvent demander à l'utilisateur de fournir les données requises, ou rejeter les tentatives de connexion si les données requises sont manquantes.

## Mise en cache

Bien que cela soit en dehors du cadre de cette spécification, les routers et/ou clients doivent mémoriser et mettre en cache (probablement de manière persistante) la correspondance entre clé publique et destination, et vice versa.

## Notes

- Distinguer les anciennes des nouvelles variantes par la longueur. Les anciennes adresses b32 font
  toujours {52 chars}.b32.i2p. Les nouvelles font {56+ chars}.b32.i2p
- Discussion Tor :
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- Ne vous attendez pas à ce que les sigtypes sur 2 octets arrivent un jour, nous n'en sommes qu'à 13. Pas
  besoin d'implémenter maintenant.
- Le nouveau format peut être utilisé dans les liens de saut (et servi par les serveurs de saut) si
  souhaité, tout comme b32.

## Références

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - voir aussi [RFC 3309](https://tools.ietf.org/html/rfc3309)

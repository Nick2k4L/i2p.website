---
title: "PQ Hybrid NTCP2"
description: "Post-quantum hybrid variant of the NTCP2 transport protocol using ML-KEM"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "Transports"
accurateFor: "0.9.69"
---



### Status

Beta Q1 2026, release Q2 2026


## Overview

This is the hybrid post-quantum variant of the NTCP2 transport protocol,
as designed in Proposal 169.
See that proposal for additional background.

PQ Hybrid NTCP2 is only defined on the same address and port as standard NTCP2.
Operation on a different port, or without standard NTCP2 support, is not permitted,
and will not be for several years, when standard NTCP2 is deprecated.

This specification documents only the changes required to standard NTCP2 to
support PQ Hybrid. See the NTCP2 specification for the baseline implementation details.



## Design

We support the NIST FIPS 203 and 204 standards [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
which are based on, but NOT compatible with,
CRYSTALS-Kyber and CRYSTALS-Dilithium (versions 3.1, 3, and older).



### Key Exchange

PQ KEM provides ephemeral keys only, and does not directly support
static-key handshakes such as Noise XK and IK.
The encryption types are the same as used in PQ Hybrid Ratchet and are defined
in the common structures document [/docs/specs/common-structures/](/docs/specs/common-structures/),
as in [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf),
Hybrid types are only defined in combination with X25519.

The encryption types are:

| Type | Code |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |


### Legal Combinations

The new encryption types are indicated in the RouterAddresses.
The encryption type in the key certificate will continue to be type 4.



## Specification


### Handshake Patterns

Handshakes use [Noise Protocol](https://noiseprotocol.org/noise.html) handshake patterns.

The following letter mapping is used:

- e = one-time ephemeral key
- s = static key
- p = message payload
- e1 = one-time ephemeral PQ key, sent from Alice to Bob
- ekem1 = the KEM ciphertext, sent from Bob to Alice

The following modifications to XK and IK for hybrid forward secrecy (hfs) are
as specified in [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) section 5:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```

The e1 pattern is defined as follows, as specified in [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) section 4:

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```


The ekem1 pattern is defined as follows, as specified in [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) section 4:

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```




### Noise Handshake KDF


#### Overview

The hybrid handshake is defined in [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf).
The first message, from Alice to Bob, contains e1, the encapsulation key, before the message payload.
This is treated as an additional static key; call EncryptAndHash() on it (as Alice)
or DecryptAndHash() (as Bob).
Then process the message payload as usual.

The second message, from Bob to Alice, contains ekem1, the ciphertext, before the message payload.
This is treated as an additional static key; call EncryptAndHash() on it (as Bob)
or DecryptAndHash() (as Alice).
Then, calculate the kem_shared_key and call MixKey(kem_shared_key).
Then process the message payload as usual.


#### Defined ML-KEM Operations

We define the following functions corresponding to the cryptographic building blocks used
as defined in [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

(encap_key, decap_key) = PQ_KEYGEN()
    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)
    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)
    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

Note that both the encap_key and the ciphertext are encrypted inside ChaCha/Poly
blocks in the Noise handshake messages 1 and 2.
They will be decrypted as part of the handshake process.

The kem_shared_key is mixed into the chaining key with MixHash().
See below for details.


#### Alice KDF for Message 1

After the 'es' message pattern and before the payload, add:


```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```


#### Bob KDF for Message 1

After the 'es' message pattern and before the payload, add:

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```


#### Bob KDF for Message 2

For XK: After the 'ee' message pattern and before the payload, add:

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```


#### Alice KDF for Message 2

After the 'ee' message pattern, add:

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```


#### KDF for Message 3 (XK only)

unchanged


#### KDF for split()

unchanged



### Handshake Details


#### Noise identifiers

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"


#### 1) SessionRequest

Changes: Current NTCP2 contains only the options in the ChaCha section.
With ML-KEM, the ChaCha section will also contain the encrypted PQ public key.

So that PQ and non-PQ NTCP2 may be supported on the same router address and port,
we use the most significant bit of the X value (X25519 ephemeral public key) to mark that it
is a PQ connection. This bit is always unset for non-PQ connections.

For Alice, after the message is encrypted by Noise, but before the AES
obfuscation of X, set X[31] |= 0x7f.

For Bob, after the AES de-obfuscation of X, test X[31] & 0x80.
If the bit is set, clear it with X[31] &= 0x7f, and decrypt via Noise
as a PQ connection.
If the bit is clear, decrypt via Noise as a non-PQ connection as usual.

For PQ NTCP2 advertised on a different router address and port,
this is not required.

For additional information, see the Published Addresses section below.



Raw contents:

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```

Unencrypted data (Poly1305 authentication tag not shown):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```

Note: the version field in the message 1 options block must be set to 2,
even for PQ connections.


Sizes:

| Type | Type Code | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | opt len |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |

Note: Type codes are for internal use only. Routers will remain type 4,
and support will be indicated in the router addresses.


#### 2) SessionCreated

Raw contents:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```

Unencrypted data (Poly1305 auth tag not shown):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```

Sizes:

| Type | Type Code | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |

Note: Type codes are for internal use only. Routers will remain type 4,
and support will be indicated in the router addresses.



#### 3) SessionConfirmed

Unchanged


#### Key Derivation Function (KDF) (for data phase)

Unchanged


#### Published Addresses

In all cases, use the NTCP2 transport name as usual.

Use the same address/port as non-PQ, non-firewalled.
Only one PQ variant is supported.
In the router address, publish v=2 (as usual) and the new parameter pq=[3|4|5]
to indicate MLKEM 512/768/1024.
Alice sets the MSB of the ephemeral key
(key[31] & 0x80) in the session request to indicate that this
is a hybrid connection. See above.
Older routers will ignore the pq parameter and connect non-pq as usual.

Different address/port as non-PQ, or PQ-only, non-firewalled is NOT supported.
This will not be implemented until non-PQ NTCP2 is disabled, several years from now.
When non-PQ is disabled,
multiple PQ variants may be supported, but only one per-address.
When it is supported,
in the router address, publish v=[3|4|5]
to indicate MLKEM 512/768/1024.
Alice does not set the MSB of the ephemeral key.
Older routers will check the v parameter and skip this address as unsupported.

Firewalled addresses (no IP published):
In the router address, publish v=2 (as usual).
There is no need to publish a pq parameter.

Alice may connect to a PQ Bob using the PQ variant that Bob publishes,
whether or not Alice advertises pq support in her router info, or
whether she advertises the same variant.



#### Maximum Padding

In the current specification, messages 1 and 2 are defined to have a "reasonable"
amount of padding, with a range of 0-31 bytes recommended, and no maximum specified.

Java I2P implements a maximum of 256 bytes padding for non-PQ connections, however this
was not previously documented.

Use the defined message size as the maximum padding,
that is, the maximum padding will double the message size, as follows:

| Message Max Padding | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------|-----------|-----------|------------|
| Session Request  |       880   |     1264   |    1648  |
| Session Created  |       848   |     1136   |    1616	 |




## Overhead Analysis

### Key Exchange

Size increase (bytes):

| Type | Pubkey (Msg 1) | Cipertext (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |


## Security Analysis

NIST security categories are summarized in [NIST presentation](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) slide 10.
Preliminary criteria:
Our minimum NIST security category should be 2 for hybrid protocols
and 3 for PQ-only.

| Category | As Secure As |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |


### Handshakes
These are all hybrid protocols.
Implementations should prefer MLKEM768; MLKEM512 is not secure enough.

NIST security categories [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| Algorithm | Security Category |
|-----------|-------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |



## Implementation Notes

### Library Support

Bouncycastle, BoringSSL, and WolfSSL libraries support MLKEM and MLDSA now.
OpenSSL support is be in their 3.5 release April 8, 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).


### Inbound Traffic Identification

We set the MSB of the ephemeral key
(key[31] & 0x80) in the session request to indicate that this
is a hybrid connection.
This allows us to run both standard NTCP and hybrid NTCP
on the same port.
Only one hybrid variant is supported for inbound, and advertised in the router address.
For example, pq=3 or pq=4.


#### Obfuscation

As Alice, for a PQ connection, before obfuscation, set X[31] |= 0x80.
This makes X an invalid X25519 public key.
After obfuscation, AES-CBC will randomize it.
The MSB of X will be random after obfuscation.

As Bob, test if (X[31] & 0x80) != 0 after de-obfuscation.
If so, it's a PQ connection.

The minimum router version required for NTCP2-PQ is TBD.

Note: Type codes are for internal use only. Routers will remain type 4,
and support will be indicated in the router addresses.


## Router Compatibility

### Transport Names

In all cases, use the NTCP2 transport name as usual.
Older routers will ignore the pq parameter and connect with standard NTCP2 as usual.



## References

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)

---
title: "Specifikace streamovacího protokolu"
description: "Specifikace pro I2P streaming protokol poskytující spolehlivý transport podobný TCP"
slug: "streaming"
category: "Protokoly"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Přehled

Viz [Streaming Library](/docs/api/streaming) pro přehled Streaming protokolu.

## Verze protokolu

Streaming protokol neobsahuje pole verze. Verze uvedené níže jsou pro Java I2P. Implementace a skutečná podpora kryptografie se mohou lišit. Neexistuje způsob, jak zjistit, zda vzdálená strana podporuje konkrétní verzi nebo funkci. Tabulka níže slouží jako obecné vodítko pro data vydání různých funkcí.

Funkce uvedené níže se týkají samotného protokolu. Různé možnosti konfigurace jsou dokumentovány v [Streaming Library](/docs/api/streaming) spolu s verzí Java I2P, ve které byly implementovány.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## Specifikace protokolu

### Formát paketu

Formát jednotlivého paketu v streaming protokolu je zobrazen níže. Minimální velikost hlavičky, bez NACK nebo dat opcí, je 22 bajtů.

Ve streaming protokolu není žádné pole pro délku. Rámcování je poskytováno nižšími vrstvami - I2CP a I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Náhodné číslo vybrané příjemcem paketu před odesláním prvního SYN odpovědi paketu a konstantní po celou dobu života připojení, větší než nula. 0 ve SYN zprávě odeslané původcem připojení a v následujících zprávách, dokud není přijata SYN odpověď obsahující stream ID protějšku.

**receiveStreamId** :: 4 bytový [Integer](/docs/specs/common-structures#integer) : Náhodné číslo vybrané původcem paketu před odesláním prvního SYN paketu a konstantní po celou dobu života spojení, větší než nula. Může být 0, pokud není známo, například v RESET paketu.

**sequenceNum** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Sekvenční číslo pro tuto zprávu, začínající na 0 ve zprávě SYN a zvyšované o 1 v každé zprávě kromě prostých ACK a retransmisí. Pokud je sequenceNum 0 a příznak SYN není nastaven, jedná se o prostý ACK paket, který by neměl být potvrzován.

**ackThrough** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Nejvyšší pořadové číslo paketu, které bylo přijato na receiveStreamId. Toto pole je ignorováno v počátečním připojovacím paketu (kde receiveStreamId je neznámé id) nebo pokud je nastaven příznak NO_ACK. Všechny pakety až do tohoto pořadového čísla (včetně) jsou potvrzeny (ACKed), KROMĚ těch uvedených v NACK níže.

**Počet NACK** :: 1 byte [Integer](/docs/specs/common-structures#integer) : Počet 4-bajtových NACK v následujícím poli, nebo 8 když se používá společně s SYNCHRONIZE pro prevenci opakování od verze 0.9.58; viz níže.

**NACKs** :: nc * 4 byte [Integer](/docs/specs/common-structures#integer)s : Pořadová čísla menší než ackThrough, která ještě nebyla přijata. Dva NACKs paketu představují žádost o 'rychlé opětovné odeslání' tohoto paketu. Od verze 0.9.58 se také používá společně se SYNCHRONIZE pro zabránění replay útokům; viz níže.

**resendDelay** :: 1 bajt [Integer](/docs/specs/common-structures#integer) : Jak dlouho bude tvůrce tohoto paketu čekat před jeho opětovným odesláním (pokud ještě nebyl potvrzen ACK). Hodnota je v sekundách od vytvoření paketu. V současnosti se při příjmu ignoruje.

**flags** :: 2 bytová hodnota : Viz níže.

**velikost option** :: 2 byte [Integer](/docs/specs/common-structures#integer) : Počet bytů v následujícím poli

**option data** :: 0 nebo více bytů : Podle specifikace flags. Viz níže.

**payload** :: zbývající velikost paketu

### Pole příznaků a dat voleb

Pole flags výše specifikuje některá metadata o paketu a může vyžadovat, aby byla zahrnuta určitá dodatečná data. Flags jsou následující. Všechny specifikované datové struktury musí být přidány do oblasti options v daném pořadí.

Pořadí bitů: 15....0 (15 je MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### Poznámky k podpisům proměnné délky

Před vydáním 0.9.11 byl podpis v poli možností vždy 40 bajtů.

Od verze 0.9.11 má podpis proměnnou délku. Typ a délka podpisu se odvozují z typu klíče použitého v možnosti FROM_INCLUDED a z dokumentace [Signature](/docs/specs/common-structures#signature).

Od verze 0.9.39 je podporována možnost OFFLINE_SIGNATURE. Pokud je tato možnost přítomna, přechodný [SigningPublicKey](/docs/specs/common-structures#signingpublickey) se používá k ověření všech podepsaných paketů a délka a typ podpisu jsou odvozeny z přechodného SigningPublicKey v této možnosti.

- Když paket obsahuje jak FROM_INCLUDED, tak SIGNATURE_INCLUDED (jako v SYNCHRONIZE), lze odvození provést přímo.

- Když paket neobsahuje FROM_INCLUDED, závěr musí být učiněn z předchozího SYNCHRONIZE paketu.

- Když paket neobsahuje FROM_INCLUDED a nebyl žádný předchozí SYNCHRONIZE paket (například zbloudilý CLOSE nebo RESET paket), lze odvození provést z délky zbývajících opcí (protože SIGNATURE_INCLUDED je poslední opcí), ale paket bude pravděpodobně zahozen, protože není k dispozici FROM pro validaci podpisu. Pokud budou v budoucnu definována další pole opcí, musí být zohledněna.

### Prevence opětovného přehrání

Aby se zabránilo Bobovi v použití útoku opětovného přehrání uložením platného podepsaného SYNCHRONIZE paketu přijatého od Alice a jeho pozdějším odesláním oběti Charlie, musí Alice zahrnout Bobův destination hash do SYNCHRONIZE paketu následovně:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
Po přijetí SYNCHRONIZE, pokud je pole NACK count 8, musí Bob interpretovat pole NACKs jako 32-bajtový hash destinace a musí ověřit, že odpovídá jeho hash destinace. Musí také obvyklým způsobem ověřit podpis paketu, protože pokrývá celý paket včetně polí NACK count a NACKs. Pokud je NACK count 8 a pole NACKs neodpovídá, musí Bob paket zahodit.

Toto je vyžadováno pro verze 0.9.58 a vyšší. Toto je zpětně kompatibilní se staršími verzemi, protože NACK nejsou očekávány v SYNCHRONIZE paketu. Destinations neznají a nemohou vědět, jakou verzi druhá strana používá.

Pro SYNCHRONIZE ACK paket odeslaný z Boba do Alice není nutná žádná změna; nezahrnujte NACK do tohoto paketu.

## Reference

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Streaming Library](/docs/api/streaming)

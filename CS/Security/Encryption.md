---
chinese: 加密 (jiāmì) — 对称加密、非对称加密与数字签名
prerequisites:
  - "[[Data Security]]"
  - "[[Information Theory]]"
  - "[[Hash Tables]]"
  - "[[Compression]]"
leads_to:
  - "[[Digital Currency and Blockchain]]"
  - "[[Networks]]"
  - "[[Data Protection and Privacy]]"
  - "[[The Internet and the Web]]"
  - "[[Privacy-Preserving Computation]]"
tags:
  - subject/computer-science
  - domain/security
  - domain/cryptography
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-2-3
  - syllabus/9618-17-1
  - type/deep
  - misconception/the-private-key-encrypts-private-messages
  - misconception/asymmetric-replaces-symmetric
  - misconception/a-certificate-encrypts
  - misconception/quantum-cryptography-is-a-quantum-computer
---

# Encryption 加密

> *For four thousand years every cipher had one weakness: to send a secret you first had to share a secret. In 1976 that ended. You can now publish the lock and keep only the key, and the whole of online life — every padlock in every address bar — runs on the arithmetic that made it possible.*

## Definition

### Formal

**Encryption** transforms **plaintext** into **ciphertext** by an algorithm controlled by a **key**, so that the ciphertext is meaningless to anyone who intercepts it; **decryption** reverses it with the matching key.

- **Symmetric-key cryptography**: one secret key does both jobs. Sender and receiver must both hold it, and it must reach them without being seen.
- **Asymmetric-key (public-key) cryptography**: each party owns a **matched pair** — a **public key** that may be given to anyone and a **private key** that is never transmitted. What one key of the pair does, only the other can undo. Encrypt with the public key and only the private key decrypts (a private message *to* the owner); seal with the private key and anyone with the public key can verify (a **digital signature**, a verified message *from* the owner).

### Intuitive

A symmetric cipher is a strongbox with one key: you and I must both have a copy, so at some point one of us carried it to the other. An asymmetric cipher is a **padlock**. I make padlocks that only my key opens, and I hand out the *open padlocks* to everyone. To send me a secret you put it in a box and snap one of my padlocks shut. You cannot reopen it; neither can the postman; only my key can. And the same pair works in reverse as a **wax seal**: a mark only I can make, which anyone can compare against my published seal to check that a letter really came from me and was not altered on the way.

### 中文锚点

手机上刷脸付款、刷脸登录，你的脸去哪了？哪儿都没去。人脸和指纹从不离开手机，支付宝、微信、任何网站都拿不到它们；它们只是在手机上开一把锁，锁后面放的是一把私钥，存在手机的安全芯片里，永远不会导出。网站那边存的是和它配对的公钥。登录的时候，网站发来一串新的随机数；手机让你刷脸，刷脸只是为了解锁私钥，然后用私钥给这串随机数盖一个章；网站再用公钥验这个章。这个章只对这一串随机数有效，偷走了也没用；就算小偷把网站的整个数据库都拷走，拿到的也只是一堆公钥，什么门都打不开。这就是非对称加密的核心：一对钥匙，一把可以发给全世界，一把永不离手，而且其中一把做过的事，只有另一把能验证或者解开。反过来用，就是一封密信：谁都可以用你的公钥把信锁上，只有你的私钥打得开，浏览器地址栏里那把小锁，每次建立安全连接，都是从这一步开始的。银行以前发的 U 盾也是同一个道理，只不过现在这把钥匙搬进了手机。

### 术语对照 (Terms)

| English | 中文 | 一句话 |
|---|---|---|
| Plaintext / ciphertext | 明文 / 密文 | 加密前 / 加密后 |
| Key | 密钥 | 控制加密算法的那串秘密 |
| Symmetric encryption | 对称加密 | 一把钥匙加密解密都用（AES） |
| Asymmetric / public-key encryption | 非对称加密 / 公钥加密 | 一对钥匙：公钥公开，私钥永不离手（RSA、椭圆曲线） |
| Public key / private key | 公钥 / 私钥 | 开着的挂锁 / 唯一能开它的钥匙 |
| Digital signature | 数字签名 | 用私钥盖章，用公钥验章：证明来源且未被改 |
| Hash / message digest | 哈希 / 摘要 | 消息的定长"指纹"（SHA-256），签名签的是它 |
| Digital certificate | 数字证书 | CA 用自己的私钥签发的"这个公钥属于谁"的证明 |
| Certificate Authority (CA) | 证书颁发机构 | 浏览器预装其公钥、默认信任的机构 |
| SSL / TLS | 安全套接层 / 传输层安全 | HTTPS 背后的协议：先非对称握手，再对称传输 |
| Quantum key distribution | 量子密钥分发 | 用光子分发密钥，窃听必被察觉（墨子号） |

---

## Part I — One key: the symmetric world

### From Caesar to AES

Julius Caesar shifted every letter three places. The **Caesar cipher** has a 25-key keyspace and falls to trying them all; the **substitution cipher** (any permutation of the alphabet, $26! \approx 4 \times 10^{26}$ keys) falls anyway, to **frequency analysis** — the Arab scholar al-Kindī described the attack in the ninth century: in English *e* is the commonest letter, and the commonest ciphertext symbol is therefore *e*. Vigenère's sixteenth-century polyalphabetic cipher resisted for three hundred years until Babbage and Kasiski found the key length from repeated fragments. Every one of these fails the same way: the ciphertext still carries the *statistics* of the plaintext.

Two ideas fixed that.

**The one-time pad** (Vernam 1917; Shannon proved it in 1949). XOR each bit of the message with a truly random key bit, use each key bit once, and the ciphertext is *statistically independent* of the plaintext — [[Information Theory]]'s "perfect secrecy": the intercept carries zero information about the message. It is unbreakable and almost useless, because the key must be as long as everything you will ever send and must itself be delivered in secret.

**Modern block ciphers** — DES (1977, a 56-bit key, dead by 1999) and **AES** (2001, keys of 128, 192 or 256 bits) — take a fixed block of bits and put it through many rounds of substitution and permutation keyed by the secret, so that every output bit depends on every input bit and every key bit. The result is not perfectly secret, only *computationally* secret: no attack better than trying every key is known, and $2^{128}$ keys is beyond any machine that will ever be built. AES runs at gigabytes per second in a phone, because the CPU has instructions for it.

![[encryption-aes-round.mp4]]

*One round of AES-128 on the sixteen bytes of "Attack at dawn!!", every hex value the real intermediate state (computed by the from-scratch `encryption-aes.py` beside this card, which matches the `cryptography` library byte for byte and passes the FIPS-197 known-answer test). SubBytes scrambles each byte through a fixed table (**confusion**); ShiftRows and MixColumns spread each byte's influence across the block (**diffusion**); AddRoundKey is where the secret enters. Ten rounds later comes the avalanche: flip one bit of the plaintext and 65 of the 128 ciphertext bits change.*

### Kerckhoffs's principle, and the problem that would not go away

Auguste Kerckhoffs (1883): *the system must be secure even if everything about it except the key is public.* Modern ciphers are published, standardised, attacked by every cryptographer alive, and trusted precisely because they survive. Security lives in the key alone.

Which leaves the ancient weakness. To use a symmetric cipher, both ends need the key, so the key has to travel — by courier, by a diplomatic bag, by a meeting in person. For $n$ people to talk in pairs you need $n(n-1)/2$ keys, each delivered secretly. For a bank with ten million customers, or a web with a billion users who have never met, that is not a difficulty; it is an impossibility. Until 1976 there was no other kind of cipher.

---

## Part II — Two keys: the asymmetric idea

### Agreeing a secret in public — Diffie and Hellman, 1976

The first step was not encryption at all but **key agreement**. Whitfield Diffie and Martin Hellman asked: can two people who have never met, talking on a line everyone can hear, end up with a shared secret nobody listening can compute? Yes, with the arithmetic of a clock.

Everyone agrees, in public, on a prime $p$ and a base $g$. Alice picks a secret number $a$ and announces $A = g^a \bmod p$; Bob picks a secret $b$ and announces $B = g^b \bmod p$. Alice computes $B^a$, Bob computes $A^b$, and both get $g^{ab} \bmod p$ — the same number, which the eavesdropper cannot reach because turning $g^a \bmod p$ back into $a$ (the **discrete logarithm**) has no known shortcut for a large $p$. The script beside this card runs it with toy numbers:

```
public g=5, p=23; Alice sends A = 5^6 mod 23 = 8; Bob sends B = 5^15 mod 23 = 19
Alice computes B^a = 2; Bob computes A^b = 2  -> same shared secret, never transmitted
```

The shared secret becomes an AES key. This — in its elliptic-curve form — is what your browser does in the first milliseconds of every https connection.

### Encrypting with a lock you publish — RSA, 1977

Diffie and Hellman also predicted a cipher with separate public and private keys but did not find one. Rivest, Shamir and Adleman did the next year, and its arithmetic is small enough to run by hand. (Clifford Cocks at GCHQ had found the same scheme in 1973; it stayed classified until 1997.)

**Making the keys.** Choose two primes and keep them secret: $p = 61$, $q = 53$. Publish their product $n = 3233$. Compute — and keep secret — $\varphi = (p-1)(q-1) = 3120$. Choose a public exponent $e$ with no factor in common with $\varphi$: $e = 17$. Find the private exponent $d$ that undoes it, $e \cdot d \equiv 1 \pmod{\varphi}$: $d = 2753$, because $17 \times 2753 = 46801 = 1 + 15 \times 3120$.

- **Public key:** $(e, n) = (17, 3233)$. Give it to everyone.
- **Private key:** $(d, n) = (2753, 3233)$. Give it to no one.

> [!info] Reading $e \cdot d \equiv 1 \pmod{\varphi}$ — why 1, and why mod $\varphi$
> The symbol $\equiv \pmod{\varphi}$ means *leaves the same remainder when divided by $\varphi$*: on a clock with 12 hours, $14 \equiv 2 \pmod{12}$. So the line says *$e \times d$ is 1 on a clock with $\varphi$ hours* — $ed = 1 + k\varphi$ for some whole number $k$; here $46801 = 1 + 15 \times 3120$.
> **Why $\varphi$?** Euler's theorem says $m^{\varphi} \equiv 1 \pmod n$: raising to the power $\varphi$ brings any (coprime) $m$ back to itself, so *exponents only matter modulo $\varphi$*. The exponents live on their own clock, and its size is $\varphi$, not $n$. (That is why $\varphi$ is the secret worth keeping: the attacker knows the clock the *numbers* live on, $n$, but not the clock the *exponents* live on.)
> **Why 1?** We want encrypting then decrypting to be a round trip: $(m^{e})^{d} = m^{ed}$ must equal $m$, which is $m^{1}$. On the exponent clock, $ed$ must therefore land on 1. Any $d$ that does is a valid private key; there is exactly one in the range $1 \ldots \varphi - 1$.

### Finding $d$ — the extended Euclidean algorithm

*Tool: Euclid's algorithm, run forwards and then back.* We need $17d \equiv 1 \pmod{3120}$, i.e. whole numbers $d, k$ with $17d - 3120k = 1$. Forwards, Euclid divides until the remainder is 1 — which is guaranteed, because $\gcd(17, 3120) = 1$ was the condition for choosing $e$:

$$3120 = 183 \times 17 + 9, \qquad 17 = 1 \times 9 + 8, \qquad 9 = 1 \times 8 + 1.$$

Backwards, write that 1 in terms of the two numbers you started with, substituting each remainder in turn:

$$1 = 9 - 8 = 9 - (17 - 9) = 2 \times 9 - 17 = 2 \times (3120 - 183 \times 17) - 17 = 2 \times 3120 - 367 \times 17.$$

So $17 \times (-367) \equiv 1 \pmod{3120}$, and adding one full turn of the clock makes it positive: $d = 3120 - 367 = 2753$. Check: $17 \times 2753 = 46801 = 15 \times 3120 + 1$. Python's `pow(e, -1, phi)` in the script does exactly this walk; for a 2048-bit $\varphi$ it takes a few thousand divisions and a few microseconds. Nobody without $\varphi$ can run it, because the first line needs $\varphi$ itself.

**Encrypting and decrypting.** A message is a number $m < n$; take the letter *A*, ASCII 65.

$$c = m^{e} \bmod n = 65^{17} \bmod 3233 = 2790, \qquad m = c^{d} \bmod n = 2790^{2753} \bmod 3233 = 65.$$

Here is the script doing exactly that, and then the same trick backwards as a signature:

```
message m=65 ('A')  ->  ciphertext c = 65^17 mod 3233 = 2790  ->  2790^2753 mod 3233 = 65
signature s = 65^2753 mod 3233 = 588;  verify: 588^17 mod 3233 = 65
'HI' -> [3000, 1486] -> 'HI'
```

![[encryption-padlock.mp4]]

*The clip: the padlock and the wax seal, then the arithmetic. Encrypt with the public exponent, decrypt with the private one; seal with the private, check with the public. Same pair of numbers, two directions.*

**Why it works.** *Tool: Euler's theorem* — for any $m$ coprime to $n$, $m^{\varphi} \equiv 1 \pmod n$. Since $ed = 1 + k\varphi$,

$$c^{d} = m^{ed} = m^{1 + k\varphi} = m \cdot (m^{\varphi})^{k} \equiv m \pmod n.$$

Raising to $e$ and then to $d$ is a round trip on the clock. (A short extra argument covers the $m$ that share a factor with $n$.)

**Why it is safe.** Everything public — $e$, $n$, $c$ — is known to the attacker. To decrypt they need $d$; to get $d$ they need $\varphi$; to get $\varphi = (p-1)(q-1)$ they need the two primes; and to get the primes they must **factor $n$**. Multiplying $61 \times 53$ is instant; recovering 61 and 53 from 3233 is a search. Make $n$ six hundred digits long and the search, by every method known, takes longer than the age of the universe. That asymmetry — easy forwards, hopeless backwards without the secret — is called a **trapdoor one-way function**, and it is the whole invention. The trapdoor is knowing $p$ and $q$.

> [!tip] Run it at real size
> The script also generates two 1024-bit primes on the spot by the Miller–Rabin test (about a second), multiplies them into a 617-digit $n$, and encrypts, decrypts, signs and verifies a sentence:
> ```
> two 1024-bit primes found in 1.1 s; N has 2048 bits, 617 decimal digits
> encrypt with public (E, N): ciphertext starts 605043407277541190589068...; decrypt with private D: b'Meet at the Sublight Lounge at nine.'
> sign SHA-256(msg) with D; verify with E: True
> tamper one byte and verify again: False
> ```
> Nothing in it is a library call except `pow(m, e, n)` — Python's built-in modular exponentiation, which is also how every real implementation does the arithmetic.

> [!warning] Textbook RSA is a demonstration, not a product
> Two honest edges. Encrypting letter by letter, as the `'HI'` line does, is just a substitution cipher wearing RSA — the same letter always gives the same number, and frequency analysis returns. And raw $m^e \bmod n$ is *deterministic* and *malleable*: the same message always gives the same ciphertext, and an attacker can multiply ciphertexts to forge related ones. Real RSA first **pads** the message with random bytes under a scheme called OAEP (for encryption) or PSS (for signatures), so that the number being exponentiated is never the bare message. The library section of the script does it properly; the by-hand section shows the arithmetic those wrappers protect.

### Speed, and why the two kinds are always used together

RSA on a 2048-bit modulus is thousands of times slower than AES, and it can only encrypt a number smaller than $n$ — a couple of hundred bytes. Nobody encrypts a file or a web page with it. Every real protocol is a **hybrid**: the asymmetric cipher moves a fresh symmetric key, and the symmetric cipher moves everything else. The script measures it:

```
hybrid: 0.12 MB under AES-GCM in 0.4 ms; the 32-byte AES key travels inside a 256-byte RSA envelope
```

That is the answer to the exam's favourite "compare symmetric and asymmetric" question, in one line: symmetric is fast and needs a shared secret; asymmetric is slow and needs no shared secret; so asymmetric is used to *create* the shared secret and symmetric to *use* it.

---

## Part III — Who holds which key

Here is the part students get wrong most, and the part the syllabus phrases most carefully: the keys do two different jobs, and which key each party holds depends on the job.

![[encryption-direction-private-message.svg|860]]

![[encryption-direction-signature.svg|860]]

The rule that covers every case: **the private key does whatever must be exclusive to one party.** If only Alice should be able to *read*, the message is locked with Alice's public key and only her private key opens it. If only Alice should be able to *vouch*, she seals with her private key and everyone checks with her public key. The public key is never a secret and is never the bottleneck; the private key is the single thing that never moves.

| Situation | Who holds the **private** key | Who holds the **public** key | What the private key does | If the private key leaks |
|---|---|---|---|---|
| **HTTPS / TLS** — you and your bank | the bank's server, in its data centre or a hardware security module | your browser receives it inside the certificate | signs the handshake, proving the server is the real owner of the certificate | anyone can impersonate the bank until the certificate is revoked |
| **A certificate authority** (Let's Encrypt, DigiCert) | the CA, in an offline vault | every browser and OS on Earth, pre-installed in the root store | signs certificates: "this public key belongs to bank.example" | every site's identity can be forged — the 2011 DigiNotar breach ended the company |
| **Encrypted e-mail** (PGP / S-MIME) | each person, for their own mailbox | published on a key server or in the address book | decrypts mail sent *to* you; signs mail sent *by* you | your whole archive of received mail is readable |
| **Signal / WhatsApp / iMessage** | your phone, generated on the device | uploaded to the server as a "prekey" so people can message you first | derives the session keys; nobody, including the company, has it | that device's conversations are exposed |
| **SSH login** to a server | your laptop (`~/.ssh/id_ed25519`) | the server, in `~/.ssh/authorized_keys` | signs the server's challenge — proof you hold the key, with no password on the wire | anyone with the file logs in as you |
| **Passkeys / FIDO2** (Face ID sign-in) | the phone's secure enclave; never exported | the website, stored at registration | signs a one-time challenge; nothing reusable ever leaves the device | it cannot — the design's point |
| **Software updates, Secure Boot, app stores** | the vendor (Apple, Microsoft, a Linux distribution) | every device that will install the update | signs each release; the device refuses unsigned or altered code | malware can be shipped as an "update" — the 2020 SolarWinds attack |
| **Bank U 盾 / hardware token** | the customer, inside the USB token | the bank | signs each transaction; malware on the PC cannot | the token is a physical object: leaking it means losing it |
| **Bitcoin / a crypto wallet** | the owner — the private key *is* ownership | derived into the address anyone can pay | signs the transaction spending the coins | the coins are gone; "not your keys, not your coins" |
| **Git commit signing / package signing** | the developer | GitHub, and anyone reading the history | signs the commit or package | forged commits under your name |
| **Session tokens (JWT)** | the login server | every service that must accept the token | signs the token so the services can trust it without asking | anyone can mint a valid session as any user |
| **An LLM API key** (bearer token — not asymmetric at all) | you *and* the provider (it keeps a hash): a shared secret | nobody — there is no public half | sent whole with every request; whoever holds it is you | your account pays for someone else's traffic until you rotate it |

Two patterns fall out of the table. **Confidentiality cases** (mail, messaging) put the private key with the *reader*. **Authenticity cases** (TLS, updates, passkeys, U 盾, wallets, commits) put it with the *actor* — and there are far more of them. In modern practice the asymmetric key's commonest job is not secrecy at all; it is *proving who you are* to something that has your public key.

### Passkeys: the padlock in your pocket

When you sign in with Face ID or a fingerprint, the biometric is not sent anywhere and is not the key. A **passkey** (the FIDO2 / WebAuthn standard, shipped by Apple, Google and Microsoft from 2022) works like this. At registration your phone's secure chip **generates a fresh keypair for that one website** and sends the site the *public* half; the private half is stored in the chip and can never be exported. At login the site sends a random **challenge**; the phone asks for your face or finger purely to *unlock* the private key locally, signs the challenge, and returns the signature; the site verifies it with the public key it stored. Three consequences follow, each an improvement on passwords:

- **Nothing reusable is ever transmitted.** The signature is over a one-time challenge; capturing it is worthless a second later. A password, by contrast, is a shared secret sent in full every time.
- **The server holds nothing worth stealing.** A breached password database yields hashes to crack; a breached passkey database yields public keys, which were public anyway.
- **It cannot be phished.** The keypair is bound to the site's exact domain. A look-alike site at *paypa1.com* is a different origin, so the phone has no key for it and will not sign — the user *cannot* be tricked into authenticating to the wrong place, however convincing the page.

The biometric's job is local: it is the lock on the drawer where the private key lives. Passkeys sync between your devices through iCloud Keychain or Google Password Manager under end-to-end encryption, so the private keys are readable on your devices and nowhere else. It is the U 盾 of the anchor, made of software and carried by two billion phones.

### The odd one out: API keys

Against all that, the way a program talks to a large language model looks primitive: an **API key**, a long random string, sent in a header with every request. It is a **bearer token** — whoever *bears* it is you — and structurally it is a shared secret, a symmetric password for machines. TLS protects it in transit, and the provider stores only a hash (which is why a key is shown once and never again), so it is not interceptable and a database breach does not leak it. What it lacks is everything a passkey has: no proof of possession, no binding to one caller, no per-request freshness, and no local gate. It is attackable exactly as a password is, and the attacks are the boring ones: the key is pasted into code and pushed to a public GitHub repository (scanners find it in minutes, and a bill follows), left in a log, embedded in a mobile app anyone can unpack, or read by a colleague's malware. The defences are the shared-secret defences: keep it out of source code (environment variables, a secrets manager), give each key the **narrowest scope** and a **spending limit**, **rotate** it, and let the provider's secret-scanning revoke it automatically when it appears in public. Why do API keys persist at all? Because a server has no face to scan and no user present to tap *approve*; machine-to-machine trust is moving toward signed requests, short-lived tokens and workload identity, but the humble bearer key remains the simplest thing that works — and the line in the table below is the one to remember: if it leaks, your account funds someone else's chatbot until you notice.

> [!info] Why "encrypt with the private key" is not a private message
> A message "encrypted" with Alice's private key can be opened by *anyone*, because Alice's public key is public. That operation is a **signature**: it proves the message came from Alice and was not altered; it hides nothing. Cambridge mark schemes accept it as an alternative process for "sending a message" (the June 2026 question below lists both), so learn the exam's framing — but know that in the real world a private message is always locked with the *recipient's public* key, and the sender's private key is used only to sign.

---

## Part IV — Signatures, hashes, certificates, and the padlock in the address bar

### Hash, then sign

Signing a whole document with RSA would be slow and size-limited, so a signature is made in two steps. First the document is put through a **cryptographic hash** — SHA-256 — giving a 256-bit **message digest**, a fingerprint with the property that changing one bit of the document changes the digest unpredictably and that no one can find a second document with the same digest ([[Hash Tables]]' cousin, built to resist an opponent). Then the *digest* is sealed with the sender's private key. The receiver hashes the document they received, unseals the digest with the sender's public key, and compares: equal digests mean *this document, from this sender, unaltered*. The script runs it, alters one byte, and watches the verification fail — the library raises `InvalidSignature` on a document where "100 credits" has become "900".

### The certificate: who says this public key is Alice's?

A public key is a number. Nothing in it says whose it is. If an attacker can hand you *their* public key labelled "your bank", the whole scheme collapses — you would lock your password with the attacker's padlock. So public keys travel inside **digital certificates**: a document containing the owner's name and public key, **signed by a Certificate Authority** whose own public key your browser already trusts. To get one, the site proves to the CA that it controls the domain (Let's Encrypt automates this in seconds); the CA signs; the site presents the certificate to every visitor. Your browser checks the CA's signature with the CA public key in its root store, checks the name, and only then uses the key inside. A certificate does not encrypt anything. It is a signed statement of ownership — a signature *about* a public key.

Trust therefore rests on the root store, and when it is bent the effect is visible. In 2014 China's railway booking site 12306 used a certificate signed by its own root rather than a public CA, so every browser warned every user; millions of people were instructed to install the 12306 root certificate by hand — which is exactly the act a certificate system is designed never to require, because a root you install can sign *any* name.

### TLS in five lines

![[encryption-tls-handshake.svg|900]]

Everything in this card meets in the handshake: a certificate (signature by a CA), a signature by the server (proof it holds the private key), a Diffie–Hellman exchange (a shared secret no one transmitted), and then AES for the traffic. The asymmetric work happens twice and stops. That is why an https page is not slower than an http one in any way you can feel, and why the syllabus says SSL/TLS is used *"in client–server communication"* wherever data is private — banking, shopping, logins, mail — and where the *server's identity* must be certain, which today is everywhere.

---

## Part V — How strong, and for how long

### Key sizes

A symmetric key is attacked by trying every value, so its strength is its length: 128 bits is already unreachable. An RSA key is attacked by *factoring*, which has algorithms far better than brute force, so an RSA modulus must be much longer for the same strength:

| Symmetric strength | RSA / DH modulus | Elliptic-curve key |
|---|---|---|
| 112 bits | 2048 bits | 224 bits |
| 128 bits | 3072 bits | 256 bits |
| 256 bits | 15 360 bits | 512 bits |

This is why elliptic-curve cryptography has taken over key exchange and signatures: the same strength in a tenth of the bits, and far faster.

![[encryption-factoring-records.svg|820]]

The public record shows the arms race. The RSA-129 challenge, set in 1977 with an estimate of "forty quadrillion years", fell in 1994 to six hundred volunteers' computers; 512-bit keys fell in 1999; 768 bits in 2009; 829 bits in 2020. Progress is about 500 bits in thirty years, and the keys in use moved faster: 1024-bit keys were retired in 2013 with no public factorisation ever achieved, and 2048 is the floor today.

### Quantum: two different things

The syllabus says *quantum cryptography*, and two unrelated ideas hide under the phrase.

**Quantum key distribution (QKD)** — BB84, Bennett and Brassard 1984 — sends the bits of a *symmetric key* as single photons polarised in one of two bases. An eavesdropper who measures a photon in the wrong basis disturbs it, so listening leaves a statistical fingerprint the two ends can detect before they use the key; and an arbitrary unknown quantum state cannot be copied perfectly. This supports a security proof under stated assumptions; it does not make every physical implementation secure. Its **benefits**: eavesdropping is detectable, and repeated exchanges can generate fresh secret key material, limited by the equipment's key-generation rate. Its **drawbacks**: it needs a dedicated optical fibre or line of sight, range is limited by photon loss (China's Micius satellite, 墨子号, extended it to 1 200 km in 2017 by going through space), it is expensive, and it distributes keys only — the data is still encrypted classically. The classical channel also needs authentication, and imperfect sources or detectors can introduce vulnerabilities. See [NSA’s QKD limitations](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/).

**Quantum computing versus RSA** — the other thing — is Peter Shor's 1994 algorithm, which factors and takes discrete logarithms in polynomial time on a large enough quantum computer. No such machine exists yet; the one built would break RSA, Diffie–Hellman and elliptic curves at once, and would not touch AES-256 beyond halving its strength. The response is **post-quantum cryptography**: new public-key schemes built on lattice problems that Shor does not solve. NIST standardised the first of them (ML-KEM, ML-DSA) in 2024, and Chrome and Cloudflare already run a hybrid post-quantum key exchange on a large share of https connections — because an adversary who *records* today's traffic can decrypt it the day the machine arrives ("harvest now, decrypt later"), and some secrets need to last longer than that.

---

## Worked examples — real Paper 3 and Paper 1 questions, every mark point named

### Cambridge 9618 November 2022 Paper 31 Q6 — private key, the process, the signature [2 + 2 + 4]

*(a) State what is meant by a private key.* Two of: the **unpublished / secret key, never transmitted**; it has a **matching public key**; it **decrypts data encrypted with its matching public key**. *(b) Describe the process of asymmetric encryption.* The message is **encrypted with the recipient's public key** and **decrypted with the recipient's private key** (the scheme also accepts the sender's-private / sender's-public pair — the callout in Part III is about that). *(c) Explain how a digital signature is used to verify a message on receipt.* Four of: the message and signature are decrypted with the receiver's private key; the **signature is decrypted with the sender's public key** to recover the digest sent; the received message is **hashed with the agreed algorithm** to produce its digest; the **two digests are compared**; equal means unaltered, different means altered. The chain of five is the whole of Part IV's first section.

### Cambridge 9618 June 2022 Paper 32 Q7 — certificate, then signature [3 + 3 + 4]

*(a) State how a digital certificate is obtained.* Three of: an **enquiry to a Certificate Authority**; the CA **checks the enquirer's details**; if verified, a **public key is agreed**; the CA **issues a certificate containing that public key**; data to and from the CA is encrypted with the CA's keys. *(b)(i) How a signature is produced.* The message is **hashed** with the agreed algorithm (MP1) to produce a **message digest** (MP2), which is **encrypted with the sender's private key** to form the signature (MP3). *(b)(ii) How it is checked.* The same five-point chain as above. The trap is the order: *hash, then sign with the private key* — a candidate who writes "encrypt the message with the private key" has described neither a hash nor a signature and scores one mark at most.

### Cambridge 9618 June 2023 Paper 32 Q5 — quantum, and the two kinds compared [2 + 3]

*(a) Describe the purpose of quantum cryptography.* Two of: a **virtually unbreakable** system, **using the properties of photons / laws of quantum mechanics**; **eavesdropping is detected** because the photons' properties change; protects data on fibre-optic links; allows longer keys. *(b) Explain the differences between symmetric and asymmetric cryptography when encrypting and decrypting.* Three of: symmetric uses **one key**, asymmetric **two**; the symmetric key **must be shared**, whereas only the **public** key is shared and the private never; so symmetric carries a **higher risk of compromise**; symmetric is **simple and fast**, asymmetric **complex and slower**; symmetric keys are **shorter** (128/256 bits against 2048). The last two are Part II's hybrid argument in exam form.

### Cambridge 9618 June 2026 Paper 31 Q8 — define, then the four-step process [1 + 1 + 4]

*(a) Define cipher text* — the result of putting plain text through an encryption algorithm — *and public key* — a key that can be obtained and used by anyone, one of a matched pair. *(b) Outline the process for an individual to send a private message to an organisation using asymmetric encryption.* The scheme wants **the sequence**: the organisation **generates a matched pair** (MP1); makes its **public key available** to the individual (MP2); the individual **encrypts with that public key** (MP3) and **sends** the message (MP4); the organisation **decrypts with its private key** (MP5). Note the scheme's alternative, MP6–MP10, in which the individual encrypts with *their own private key* and the organisation decrypts with the individual's *public* key — that sequence is a signature and is not private, but it earns the marks; write the first version and you are right on both counts.

### Cambridge 0478 March 2024 Paper 12 Q7(a) — purpose, and the difference [1 + 4]

*(i) State the purpose of encrypting data.* **If intercepted it cannot be understood.** *(ii) Describe the differences between symmetric and asymmetric encryption.* Four of: symmetric has a **shared key** used **to encrypt and decrypt**, which **both sender and receiver know**; asymmetric has **different keys — a public and a private**; the **public encrypts and the private decrypts**; **anyone can know the public key, only the intended party knows the private**. IGCSE's whole treatment is this list plus the vocabulary.

### Cambridge 0478 June 2025 Paper 11 Q6(a) — the fill-in paragraph [8]

*Data is encrypted using an encryption key. This is a type of* **algorithm** *that scrambles the* **plain text** *and turns it into* **cipher text**. *This makes the data* **meaningless**. *A* **public** *key is used to encrypt the data. This key cannot be used to decrypt the data. A* **private** *key is used to decrypt the data. Any device is able to request the* **public** *key, but only your device knows the* **private** *key.* The scheme allows the encrypt/decrypt pair either way round as long as they are opposite — and the last two blanks, *public* requested by anyone and *private* known only to you, are fixed.

---

## Misconceptions

1. **"Encrypt with your private key to send a private message."** Anyone holding your public key — that is, anyone — can open it. That operation is a signature. A private message is locked with the *recipient's* public key.
2. **"Asymmetric encryption has replaced symmetric."** It bootstraps it. Every https byte after the handshake is AES; RSA and elliptic curves only ever move keys and make signatures.
3. **"A certificate encrypts the connection."** It is a signed statement that a public key belongs to a name. The encryption is done with keys agreed afterwards; the certificate's job is to stop you agreeing keys with an impostor.
4. **"The public key is a secret too."** It is printed in the certificate of every website you visit and published on key servers by design. Only the private key is secret; a scheme that needed the public key hidden would be symmetric in disguise.
5. **"Quantum cryptography means a quantum computer."** QKD is a way of *delivering* a key on photons so that eavesdropping is detectable; it uses no quantum computer. Shor's algorithm on a quantum computer is the *threat* to RSA; post-quantum cryptography is the classical answer to it.
6. **"A longer key is always better."** Key sizes are matched to attacks: 128-bit AES and 3072-bit RSA are equally strong, and doubling either buys nothing until the attack changes. Longer keys cost time and, past the equivalence, defend against nothing.

---

## Hands-on

Everything here runs on your own machine.

1. **Run the card.** `python3 encryption-aes.py` prints every intermediate state of one AES round and checks itself against the library and the FIPS test vector; `python3 encryption-rsa-demo.py` (beside this card) does RSA by hand with $p = 61$, $q = 53$; generates 2048-bit primes and encrypts, decrypts, signs and verifies a sentence with nothing but `pow`; then does it properly with the `cryptography` library, including the hybrid AES step and a forged-document failure; then Diffie–Hellman. Change the message. Change one byte of the ciphertext and watch decryption produce garbage.
2. **Make a keypair you will actually use.** `ssh-keygen -t ed25519` writes a private key to `~/.ssh/id_ed25519` and a public key beside it. Open the public one: that text is what you paste into GitHub or a server. The private one never leaves the laptop — Part III's SSH row, done.
3. **Read a real certificate.** Click the padlock in your browser on any https site and open the certificate: the subject (whose key), the issuer (which CA signed it), the validity dates, the public key itself, and the signature. Follow the chain up to a root that is already in your computer. Or from a terminal: `openssl s_client -connect example.com:443 -servername example.com` shows the handshake and the certificate chain as text.
4. **Break Caesar.** Write a ten-line Python loop that tries all 25 shifts of a ciphertext and prints each; then count letter frequencies of a longer English ciphertext and watch *e* stand out. You will have rediscovered al-Kindī, and understood why every symmetric cipher before 1917 died.

---

## Exam Notes

### Cambridge 9618 — §17.1 Encryption, Encryption Protocols and Digital Certificates (A2 Paper 3)

- **The LO list:** public key, private key, plain text, cipher text, symmetric and asymmetric cryptography; how the keys send a *private message from the public to an individual/organisation* and a *verified message to the public*; how data is encrypted and decrypted under each; **purpose, benefits and drawbacks of quantum cryptography**; the **purpose of SSL/TLS**, its use in client–server communication, and situations where it is appropriate; how a **digital certificate is acquired** and used to produce **digital signatures**.
- **Question shapes:** define a term (1 each); describe the asymmetric process (2–4, *in sequence*); produce / verify a digital signature (3 + 4, the hash-then-sign chain); obtain a certificate (3, the CA dialogue); symmetric vs asymmetric differences (3–4); quantum benefits and drawbacks (2 + 2); where SSL/TLS is used (2–3, with a scenario).
- **AS Paper 1 (§6.1)** mentions encryption only as a security measure; the mechanism is not examined until Paper 3.

### Cambridge 0478 IGCSE — §2.3 Encryption (Paper 1)

- **§2.3.1–2:** the need for and purpose of encryption when transmitting data; how data is encrypted using **symmetric and asymmetric** encryption, with public and private keys. No signatures, no certificates, no quantum.
- **Question shapes:** the purpose in one line (1); the symmetric process (2–3); the asymmetric process or the symmetric/asymmetric differences (4); and the fill-in paragraph with a word list (6–8), which is now a staple.

### IB Computer Science — A2.4 Network security

- Encryption appears as one of the countermeasures alongside the authentication material of [[Data Security]]; the depth expected is the symmetric/asymmetric distinction and the role of keys, roughly 0478's level with better vocabulary. The mechanism of RSA is not required.

### Not examined on…

- **AP Computer Science A** — no cryptography in the course.
- **Cambridge 9709 / 9231** — modular arithmetic and Euler's theorem are not on either syllabus; the number theory here is university material, though [[Number Bases]] and [[Prime Numbers]] are the IGCSE roots of it.
- **Physics boards** — QKD's photon polarisation is not examined as physics on 9702, 0625, AP or IB.

---

## Quick reference

| Ask | Answer in one line |
|---|---|
| symmetric | one shared key encrypts and decrypts (AES); fast; the key must be delivered in secret |
| asymmetric | a matched pair: public key given to all, private key never transmitted (RSA, elliptic curves); slow |
| private message *to* X | encrypt with X's **public** key; only X's **private** key decrypts |
| verified message *from* X | X hashes it and seals the digest with X's **private** key; anyone checks with X's **public** key |
| digital signature | hash → encrypt the digest with the sender's private key; receiver hashes, decrypts the signature with the public key, compares |
| digital certificate | the owner's public key + name, signed by a CA; obtained by proving identity to the CA |
| SSL / TLS | verify the server's certificate, agree a secret by Diffie–Hellman, then AES for everything |
| hybrid | asymmetric moves the key, symmetric moves the data |
| passkey | a keypair per site, private half in the phone's secure chip; the biometric only unlocks it locally; signs a one-time challenge; phishing-proof by origin binding |
| API key | a bearer secret, not a keypair; protected by TLS and hashing at rest, attackable by leaking — scope, rotate, never commit |
| finding $d$ | extended Euclid on $e$ and $\varphi$: $ed - k\varphi = 1$; `pow(e, -1, phi)` |
| RSA | $n = pq$, $ed \equiv 1 \pmod{(p-1)(q-1)}$; $c = m^e \bmod n$, $m = c^d \bmod n$; safe because factoring $n$ is hard |
| quantum key distribution | keys on photons; eavesdropping detectable; needs fibre or line of sight; keys only |
| Shor / post-quantum | a large quantum computer would factor $n$; lattice schemes standardised in 2024 |

---

## Connections

- **Parents:** [[Data Security]] — encryption as the last-line defence, "it makes the theft worthless"; this card is the mechanism. [[Information Theory]] — perfect secrecy and the one-time pad; why ciphertext must carry no information about plaintext. [[Hash Tables]] — the hash function, here in its opponent-resisting form, as the first step of every signature.
- **Children:** [[Networks]] — TLS as the layer above TCP, the protocol stack that carries it; [[Data Protection and Privacy]] — encryption at rest and in transit as the technical half of a legal duty.
- **Computing on ciphertexts:** [[Privacy-Preserving Computation]] — RSA's accidental homomorphism turned into a design goal (Paillier, fully homomorphic encryption), and proofs that reveal nothing but their own truth.
- **Cross-domain:** [[Number Bases]] and [[Prime Numbers]] — the arithmetic that RSA is built from; [[Big-O Notation]] — why multiplying is $O(n^2)$ and factoring is sub-exponential but not polynomial, which is the entire gap RSA lives in; [[Compression]] — its sibling: compression removes redundancy, encryption removes meaning, and a good protocol compresses first; [[Credit Is the Currency]] — the certificate chain as a tower of kept promises, trust delegated from a root; [[Sensors and Control Systems]] — nothing, except that QKD's photon detectors are its instruments.
- **Misconception traps cleared:** the private key encrypts private messages; asymmetric replaces symmetric; a certificate encrypts; the public key is secret; quantum cryptography is a quantum computer; longer keys are always better.

## Sources

- W. Diffie and M. Hellman, *New Directions in Cryptography*, IEEE Trans. Inf. Theory 1976. R. Rivest, A. Shamir, L. Adleman, *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*, CACM 1978. C. Cocks, *A Note on Non-Secret Encryption*, GCHQ 1973 (declassified 1997).
- C. Shannon, *Communication Theory of Secrecy Systems*, 1949. A. Kerckhoffs, *La cryptographie militaire*, 1883. NIST FIPS 197 (AES, 2001); NIST SP 800-57 (key-size equivalences).
- C. Bennett and G. Brassard, *Quantum cryptography: public key distribution and coin tossing*, 1984. P. Shor, *Algorithms for quantum computation*, FOCS 1994. J. Yin et al., *Satellite-based entanglement distribution over 1200 kilometers*, Science 2017 (Micius). NIST FIPS 203/204 (ML-KEM, ML-DSA), August 2024.
- RSA Factoring Challenge records: Atkins et al. 1994 (RSA-129); Cavallar et al. 2000 (RSA-155); Kleinjung et al. 2010 (RSA-768); Boudot et al. 2020 (RSA-240, RSA-250).
- The 12306 root-certificate episode: widely reported in Chinese technical press, 2014–2015; the site moved to a publicly trusted CA later.

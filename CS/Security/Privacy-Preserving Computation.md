---
chinese: 隐私计算 (yǐnsī jìsuàn)
aliases:
  - Secure Multi-Party Computation
  - Homomorphic Encryption
  - Federated Learning
  - Zero-Knowledge Proof
  - Secret Sharing
prerequisites:
  - "[[Data Protection and Privacy]]"
  - "[[Encryption]]"
  - "[[Artificial Intelligence]]"
  - "[[Prime Numbers]]"
leads_to:
  - "[[Affective Computing]]"
tags:
  - subject/computer-science
  - domain/security
  - domain/cryptography
  - level/university
  - level/enrichment
  - type/deep
  - misconception/encrypted-means-unusable
  - misconception/federated-means-private
  - misconception/zero-knowledge-means-no-proof
  - misconception/hardware-enclave-is-trustless
---

# Privacy-Preserving Computation 隐私计算

> *In January 2008 some twelve hundred Danish sugar-beet farmers had to trade production contracts among themselves, at a single price that would balance supply and demand. Finding that price needs every farmer's bid: how much he would sell or buy at each price. No farmer would hand that to Danisco, the only company that bought their beet, since a bid reveals how hard a farm can be squeezed. Danisco would not trust the farmers' association with it, and neither side wanted to pay for an auditor both could believe in. So each bid was cut into three random pieces, one each for servers run by Danisco, the growers' association and a university research group. The three machines computed the market price together, and contracts for 25 000 tonnes changed hands. No machine, and no person, ever saw a bid. It was the first time secure multi-party computation had been used for something that mattered.*

## Definition

### Formal

**Privacy-preserving computation** is the family of techniques for computing a result from data **without any party seeing inputs that are not its own**. The main members are **secure multi-party computation** (the inputs are split into random shares), **homomorphic encryption** (arithmetic is done on ciphertexts), **federated learning** (a model travels to the data), **trusted execution environments** (hardware hides the computation from its own operator) and **zero-knowledge proofs** (a statement about secret data is proved without revealing the data). They protect the **inputs**. What the **output** reveals is a separate question, answered by the anonymisation and differential privacy of [[Data Protection and Privacy]].

### Intuitive

Ordinary encryption protects data while it is stored and while it travels, and then the data has to be decrypted before anything can be done with it, in front of whoever runs the computer. These techniques remove that last step. The data stays hidden *while it is being used*.

### 中文锚点

几个同事想知道大家的平均工资，可是谁也不愿意把自己的数字告诉别人。有个老办法：第一个人在心里想一个很大的随机数，加上自己的工资，把结果悄悄告诉第二个人；第二个人加上自己的工资，再悄悄传给第三个人；这样传完一圈回到第一个人手里，他减去当初那个随机数，剩下的就是所有人工资的总和。每个人听到的那个数，都被一个自己不知道的随机数盖住了，单独看它毫无意义，从里面猜不出任何人的工资；可是所有人的数字确实都加了进去，最后的总和一分不差。隐私计算的核心就是这一点：把数据盖上随机的面具，面具之下照样可以做运算，等到所有的面具在最后互相抵消，露出来的只有大家想要的那个答案。银行之间联合查骗贷，医院之间联合训练诊断模型，用的都是这个思路，国内把它叫作"数据可用不可见"。要记住的是，答案本身也会说话：如果只有两个人，知道了总和，也就等于知道了对方的工资。

### 术语对照 (Terms)

隐私计算 privacy-preserving computation · 安全多方计算 secure multi-party computation (MPC) · 秘密分享 secret sharing · 门限 threshold · 同态加密 homomorphic encryption · 全同态加密 fully homomorphic encryption (FHE) · 联邦学习 federated learning · 安全聚合 secure aggregation · 可信执行环境 trusted execution environment (TEE) · 远程证明 remote attestation · 零知识证明 zero-knowledge proof · 半诚实 / 恶意 semi-honest / malicious · 数据可用不可见 usable but not visible

---

## Part I — Where the data is exposed, and whom you must trust

Data has three states. **At rest** on a disk it can be encrypted. **In transit** on a network it can be encrypted ([[Encryption]] covers both). **In use**, it traditionally cannot: a processor adds plaintext numbers. So every pooled analysis has had the same shape: send everything to one place, decrypt it there, and trust whoever runs that place, along with everyone who can break into it, subpoena it or buy it.

![[privacy-computation-three-settings.svg|860]]

Every technique below is a different answer to one question: **whom do I still have to trust, and with what?**

| Technique | What never becomes visible | What you must still trust | Typical cost |
|---|---|---|---|
| Secure multi-party computation | each party's input | that fewer than a threshold of the parties collude | heavy network traffic |
| Homomorphic encryption | the data sent to a server | the mathematics, and whoever holds the decryption key | heavy computation |
| Federated learning | the raw records | the server not to dissect the updates (unless aggregation is also secured) | many rounds of communication |
| Trusted execution environment | the data inside the chip's enclave | the chip's manufacturer and the absence of side channels | almost none |
| Zero-knowledge proof | the secret behind a claim | the mathematics | proving is slow, checking is fast |

None of them removes trust. Each moves it somewhere you may find easier to accept.

---

## Part II — Secret sharing and multi-party computation

### Cut a number into pieces that mean nothing

To share a secret $x$ among $n$ parties, pick $n-1$ numbers uniformly at random and let the last piece be whatever makes the total right, all modulo a prime $p$ (arithmetic modulo a prime, with its inverses, is in [[Prime Numbers]]):

```python
import secrets
P = 2**61 - 1

def share(x, n, p=P):
    parts = [secrets.randbelow(p) for _ in range(n - 1)]
    return parts + [(x - sum(parts)) % p]
```

Any $n-1$ of the pieces are just random numbers, identically distributed whatever $x$ was; in the lab the average of 20 000 shares is 0.50 of $p$ whether the secret is 5 or 2 000 000. All $n$ together give $x$ exactly. And the pieces can be **added without being opened**: if each party adds the shares it holds of $x$ and of $y$, the results are shares of $x + y$.

![[privacy-computation-secure-sum.mp4]]
*Three hospitals each cut a private number into three random pieces, deal them out, add what they hold and publish only that. The published numbers add up to the true total, and no private number ever left its box. (Arithmetic is shown mod 10 000 so that the numbers fit on the screen.)*

That is a complete protocol for a **secure sum**: three hospitals with 1204, 877 and 2310 patients obtain 4391 and nothing else.

### A threshold: any three of five

Additive shares need every party present. Adi Shamir's scheme (1979) needs only a chosen number of them. To require any $k$ of $n$ shares, hide the secret as the constant term of a random polynomial of degree $k-1$ and hand out points on its graph:

```python
def shamir_split(secret, k, n, p=P):
    coeffs = [secret] + [secrets.randbelow(p) for _ in range(k - 1)]
    return [(x, sum(c * pow(x, e, p) for e, c in enumerate(coeffs)) % p) for x in range(1, n + 1)]
```

![[privacy-computation-shamir.svg|820]]

Three points fix a parabola, so any three shares recover $f(0)$ by interpolation. Two points fix nothing: through them there is a parabola ending at **every** possible secret, one for each, so two shares carry no information at all, a stronger statement than "too little to be useful". This is the [[Remainder and Factor Theorems]] fact that a polynomial of degree below $k$ is determined by $k$ values, put to work. Companies split the master keys of their certificate authorities and cryptocurrency reserves this way, so that no single employee can sign and any three directors can.

### From sums to everything

Sums come free. Products need one trick (Beaver, 1991): use up a pre-shared random triple $a$, $b$, $c = ab$. The parties open $d = x - a$ and $e = y - b$, which reveal nothing because $a$ and $b$ are random masks, and then compute shares of $xy = c + db + ea + de$ locally. The lab multiplies 1234 by 5678 this way and gets 7 006 652. With addition and multiplication, any function that can be written as an arithmetic circuit can be computed on data nobody sees: an auction's clearing price, a regression, a join of two customer lists.

**Honest edges.** (1) **The output leaks.** Two colluding hospitals subtract their own numbers from the total and learn the third's. No protocol can prevent what the agreed answer itself gives away; that is a job for the output-side tools. (2) **Security is conditional** on how many parties collude, and on whether they merely peek (*semi-honest*) or actively lie (*malicious*, which needs costlier protocols with checks). (3) **The cost is communication**: every multiplication is a round of messages, so a computation that takes a millisecond on one machine can take seconds across three.

---

## Part III — Homomorphic encryption: arithmetic on ciphertexts

### An accident in RSA

Textbook RSA encrypts as $c = m^e \bmod n$. Multiply two ciphertexts: $m_1^e\, m_2^e = (m_1 m_2)^e$, which is the encryption of the product. The lab checks it with the toy key of [[Encryption]]: $\text{Enc}(7)\cdot\text{Enc}(12)$ decrypts to 84. Whoever holds only ciphertexts has multiplied two numbers they cannot read. In RSA this is a **flaw** (it lets an attacker manufacture valid messages, which is one reason real RSA pads its input). A scheme that offers the property on purpose is called **homomorphic**.

### Paillier: built to add

Pascal Paillier's scheme (1999) is homomorphic for addition. With $n = pq$ as in RSA, encrypt $m$ using fresh randomness $r$:

$$c = (1+n)^m \cdot r^n \bmod n^2 .$$

Why addition appears: by the binomial theorem $(1+n)^m = 1 + mn + \binom m2 n^2 + \dots \equiv 1 + mn \pmod{n^2}$, so the message sits in the exponent of $(1+n)$ in a way that can be read back out. Multiply two ciphertexts and the exponents add:

$$c_1 c_2 = (1+n)^{m_1+m_2}\,(r_1r_2)^n \bmod n^2 = \text{Enc}(m_1 + m_2).$$

Raising a ciphertext to a known power $k$ gives $\text{Enc}(km)$. The factor $r^n$ is the randomness that makes two encryptions of the same number look unrelated, and only the holder of $p$ and $q$ can strip it off.

```python
class Paillier:                     # key generation and decryption are in the lab file
    def enc(self, m):
        r = secrets.randbelow(self.n - 2) + 1
        return (1 + m * self.n) * pow(r, self.n, self.n2) % self.n2
    def add(self, c1, c2):   return c1 * c2 % self.n2      # Enc(a) * Enc(b) = Enc(a + b)
    def times(self, c, k):   return pow(c, k, self.n2)     # Enc(a) ^ k     = Enc(k a)
```

In the lab $\text{Dec}(\text{Enc}(3500)\cdot\text{Enc}(4200)) = 7700$. An **encrypted ballot box** follows at once: each of 400 voters encrypts 0 or 1; the counting server multiplies the 400 ciphertexts and sees nothing but large numbers; only the election authority decrypts, and it decrypts only the product, which is the tally of 222. The counting can be done by anyone and checked by everyone.

### Fully homomorphic encryption, and the bill

A scheme that supports **both** addition and multiplication can evaluate any circuit on encrypted data. For thirty years nobody knew whether one could exist. Craig Gentry built the first in 2009. His idea: ciphertexts carry a little random *noise* that grows with every operation and eventually swamps the message, so before that happens, run the decryption circuit itself homomorphically, producing a fresh ciphertext of the same message with the noise reset (**bootstrapping**).

![[privacy-computation-costs.svg|820]]

Measured on one core in plain Python (the exact figures vary from run to run): adding two secret shares costs about 4 times a plain addition; adding under Paillier a few hundred times; encrypting one number well over 100 000 times. A single multiplication under fully homomorphic encryption costs on the order of ten milliseconds in published benchmarks, about a million plain additions, and a 1-bit vote occupies 1019 bits as a Paillier ciphertext. Homomorphic encryption is used where the computation is small and the secrecy is worth a great deal.

---

## Part IV — Federated learning: send the model, not the data

Training a model on data held by many owners does not require moving the data. In **federated averaging** (McMahan and colleagues, 2016) a server sends the current model to every client; each client improves it with a few steps of gradient descent on its own records ([[Artificial Intelligence]]); the server averages the returned models and repeats.

```python
w = np.zeros(d + 1)
for _ in range(rounds):                                     # the model travels, the data stays
    w = np.mean([train(X, y, w, epochs=10) for X, y in clinics], axis=0)
```

![[privacy-computation-federated.svg|820]]

Ten synthetic clinics, each with 30 patients of a slightly different kind, reach 74.8 % accuracy training alone. Federated, they reach 94.1 %, against 94.7 % if all 300 records were pooled on one server. Nearly all the benefit of pooling, with no record leaving a clinic. This is how phone keyboards learn new words from what millions of people type.

**The honest edge is large.** "The data never leaves the device" is true of the bytes and false of the information. A model update is a function of the training data, and sometimes an invertible one. For a linear model updated on one patient, the gradient is $(\hat y - y)\,\mathbf{x}$, and its last component (for the constant feature) is $(\hat y - y)$ itself, so dividing one by the other returns the record **exactly**: the lower panel, error $2\times10^{-16}$. For deep networks the reconstruction takes an optimisation and is approximate, and it has been demonstrated on images and text.

Two earlier tools repair this. **Secure aggregation** is the secure sum of Part II applied to updates: every pair of clients agrees on a random mask that one adds and the other subtracts, so each upload looks like noise (in the lab, 3000 times larger than the true update and uncorrelated with it) while the masks cancel in the total to within $10^{-13}$. The server learns the average and no individual update. **Differential privacy** then adds calibrated noise so that even the average does not betray one person. Federated learning on its own is a bandwidth and governance technique; with these two it becomes a privacy technique.

---

## Part V — Trusted execution environments: a locked room inside the chip

A **trusted execution environment** (Intel SGX and TDX, AMD SEV, ARM TrustZone, the secure enclave of a phone) is a region of the processor whose memory is encrypted by the hardware with keys that the operating system, the hypervisor and the machine's owner cannot read. Data is sent in encrypted, decrypted only inside, processed at nearly full speed, and the result sent out encrypted. **Remote attestation** lets you check before sending anything: the chip signs a hash of the exact code it has loaded with a key the manufacturer burned in, so you can verify that the enclave is running the program you audited and no other.

It is by far the cheapest technique, and its trust model is the weakest of the five: you trust the manufacturer's keys, the absence of flaws in the design, and the absence of **side channels**. That last assumption has failed repeatedly. Foreshadow (2018) and several successors read SGX enclave memory through the processor's speculative execution, the same family of flaws as Spectre. There is nothing to run in the lab for this section, because the protection is in silicon; the point to carry away is that a hardware promise is only as good as the last audit of the hardware.

---

## Part VI — Zero-knowledge proofs: convincing without showing

Can you convince someone that you know a secret without telling them anything about it? Goldwasser, Micali and Rackoff showed in 1985 that you can, and the standard picture is a cave.

![[privacy-computation-cave.mp4]]
*A ring-shaped cave with a locked door at the back. The prover walks in by a side of her choosing, unseen; the verifier then calls out which side she must return by. With the key she can always comply. Without it she is right only when she happened to go in by the side that is called, half the time, and is soon caught. The verifier never sees the key.*

A real protocol replaces the door with arithmetic. The secret is a number $x$; the public value is $y = g^x \bmod p$, from which $x$ cannot feasibly be recovered (the discrete logarithm problem, as in the key exchange of [[Encryption]]). One round:

```python
r = secrets.randbelow(q);  t = pow(g, r, p)      # prover commits to a random t = g^r
c = secrets.randbelow(2)                         # verifier's challenge: 0 or 1
s = (r + c * x) % q                              # prover's response
assert pow(g, s, p) == t * pow(y, c, p) % p      # verifier checks g^s = t * y^c
```

The check works because $g^{r+cx} = g^r (g^x)^c$. Three properties make it a zero-knowledge proof.

- **Completeness.** A prover who knows $x$ always passes.
- **Soundness.** A prover who does not know $x$ can prepare for $c = 0$ (choose $r$ honestly) or for $c = 1$ (choose $s$ first and set $t = g^s y^{-1}$), and cannot prepare for both, since answers to both would give $x = s_1 - s_0$. She must guess the challenge, and passes $n$ rounds with probability $2^{-n}$.

![[privacy-computation-zk-soundness.svg|820]]

Measured over 360 000 attempts by a cheat: 0.501 for one round, 0.0642 for four, 0.0004 for twelve. Twenty rounds leave one chance in a million; forty, one in a trillion.

- **Zero knowledge.** The verifier's record of a session is a list of triples $(t, c, s)$. Anyone can manufacture such triples **without knowing $x$**, by choosing $c$ and $s$ first and computing the $t$ that fits; the lab forges a thousand and all of them verify. Whatever can be produced without the secret cannot contain the secret. It also follows that a transcript convinces nobody else: only someone who chose the challenges live, after the commitments, has reason to believe. The proof is real and cannot be passed on.

Modern systems (zk-SNARKs) compress this to a single short message that proves an arbitrary computation was done correctly. They let a blockchain check a payment without seeing its amount or parties ([[Digital Currency and Blockchain]]), and let a person prove "I am over 18" or "my income exceeds the threshold" from a signed credential without showing the birth date or the income.

---

## Choosing a tool

| The situation | Reach for | Because |
|---|---|---|
| A few organisations, one agreed statistic, mutual distrust | secure multi-party computation | no trusted party exists, and the computation is small |
| One client, one powerful server, a simple query on private input | homomorphic encryption | only one party has a secret, and it cannot stay online for rounds of messages |
| Millions of devices, one model to train | federated learning **with** secure aggregation and differential privacy | the data cannot physically be moved, and an update alone leaks |
| A heavy computation that must run at full speed on rented hardware | a trusted execution environment, with attestation | nothing cryptographic is fast enough, and you accept trusting the chip |
| Proving a fact about private data to a sceptic | a zero-knowledge proof | the sceptic needs certainty, not the data |
| The *answer* would itself expose a person | differential privacy, from [[Data Protection and Privacy]] | hiding the inputs does nothing about what the output says |

Real systems stack them: federated learning inside secure aggregation, with differential privacy on the result, running in an attested enclave.

---

## Where it is the working tool

**Auctions and benchmarks between rivals.** Since the Danish beet auction, multi-party computation has priced energy and spectrum, and let competing firms learn where they stand against an industry average. In Boston, from 2016, scores of employers jointly computed the city's gender pay gap from their payrolls without any payroll leaving its company, because no employer would have handed salary data to the city.

**Your phone.** Keyboards learn new words by federated learning with secure aggregation. When an iPhone checks an incoming number against a spam database, it sends the number **homomorphically encrypted**; the server computes the lookup on a ciphertext and returns an encrypted answer it cannot read, so the provider never learns who is calling you. Browsers check saved passwords against lists of breached ones in a similar way. Signal finds which of your contacts use Signal inside an attested enclave, so that its servers never hold your address book.

**数据可用不可见.** China's 2022 framework for the data economy (the "Twenty Data Measures") requires public data to be offered under the rule 原始数据不出域、数据可用不可见: raw data stays inside its domain, usable but not visible. That sentence is a specification for this card's techniques, and it has produced an industry: banks that detect a customer borrowing from many lenders at once without showing one another their customer lists, hospitals training shared models, and open-source frameworks from the large platforms.

**Why it matters for the next thing.** A system that reads faces, voices or heart rates to infer emotion handles the most sensitive category of personal data in both GDPR and PIPL. Whether anyone will agree to be read depends on whether the raw signal can be shown never to leave their device. [[Affective Computing]] is only deployable on top of this.

---

## Hands-on

Run `python3 privacy-preserving-computation-lab.py` (standard library and numpy, a few seconds). Then:

1. **Do the salary trick for real.** Four friends, one calculator. Work modulo 1 000 000. Afterwards, work out what two colluding neighbours of one person could learn, and what changes if everyone shares their number into pieces as in `secure_sum()`.
2. **Break the threshold.** In `shamir()`, change $k$ to 2 and look at what two shares now give. Then set $k = n$: what have you rebuilt?
3. **Leak a record.** In `federated()`, change the upload to the average gradient over *two* patients. Can the server still separate them? What about thirty? This is why batching helps and does not suffice.
4. **Cheat the verifier.** In `zero_knowledge()`, let the verifier's challenge come from `rnd` with a seed the prover knows. How often does the cheat pass now? What does that say about where a protocol's randomness must come from?

---

## Worked examples — every tool named

### Example 1 — a secure sum by hand

*Three clinics hold 12, 30 and 7 cases. Work modulo 100. Clinic A splits 12 as (45, 80, ?), B splits 30 as (91, 3, ?), C splits 7 as (60, 22, ?). Complete the shares, find what each clinic publishes, and the total.*

*Tool: the last share is whatever makes the sum right, mod 100.* A: $12 - 45 - 80 = -113 \equiv 87$. B: $30 - 94 = -64 \equiv 36$. C: $7 - 82 = -75 \equiv 25$. Piece $j$ goes to clinic $j$, so A holds $45 + 91 + 60 = 196 \equiv 96$, B holds $80 + 3 + 22 = 105 \equiv 5$, C holds $87 + 36 + 25 = 148 \equiv 48$. Published: 96, 5, 48. Total $149 \equiv 49 = 12 + 30 + 7$. *Trigger for the modulus:* it must exceed the largest possible true total, or the answer wraps round.

### Example 2 — Shamir with small numbers

*Share the secret 6 with threshold 2 among three people, modulo 11, using $f(x) = 6 + 4x$. Give the shares, and recover the secret from shares 1 and 3.*

Shares: $f(1) = 10$, $f(2) = 14 \equiv 3$, $f(3) = 18 \equiv 7$. From $(1, 10)$ and $(3, 7)$: the gradient is $(7 - 10)/(3 - 1) = -3 \cdot 2^{-1}$. Modulo 11, $2^{-1} = 6$ (since $2 \times 6 = 12 \equiv 1$), so the gradient is $-18 \equiv 4$, and $f(0) = 10 - 4 \times 1 = 6$. *Trigger: division in modular arithmetic means multiplying by the inverse*, which exists because 11 is prime.

### Example 3 — Paillier with a toy key

*Take $p = 3$, $q = 5$, so $n = 15$ and $n^2 = 225$. Encrypt $m_1 = 4$ with $r = 2$ and $m_2 = 7$ with $r = 4$, multiply the ciphertexts, and decrypt.*

*Tool: $c = (1 + mn)\,r^n \bmod n^2$.* First the powers: $2^{15} = 32768 \equiv 143$ and $4^{15} = (2^{15})^2 \equiv 143^2 \equiv 199 \pmod{225}$. Then
$$c_1 = (1 + 60)\times143 = 8723 \equiv 173, \qquad c_2 = (1 + 105)\times199 = 21094 \equiv 169, \qquad c_1c_2 = 29237 \equiv 212 .$$
*Tool for decryption: $m = L\big(c^{\lambda} \bmod n^2\big)\cdot\mu \bmod n$, with $L(u) = (u-1)/n$, $\lambda = \operatorname{lcm}(p-1, q-1) = 4$ and $\mu = \lambda^{-1} \bmod n = 4$ (since $4 \times 4 = 16 \equiv 1$).* Working with $212 \equiv -13$: $(-13)^2 = 169$ and $169^2 = 28561 \equiv 211$, so $L = 210/15 = 14$ and $m = 14 \times 4 = 56 \equiv 11 = 4 + 7$. The server that multiplied 173 by 169 never saw a 4 or a 7. Why $L$ comes out as 14: raising to the power $\lambda$ kills the random factor ($r^{n\lambda} \equiv 1$) and leaves $(1+n)^{\lambda m} \equiv 1 + \lambda m\,n$, so $L = \lambda m \bmod n = 44 \bmod 15 = 14$, and multiplying by $\mu = \lambda^{-1}$ removes the $\lambda$.

### Example 4 — how many rounds?

*A verifier wants a cheating prover to succeed with probability below one in a billion. How many one-bit rounds are needed?*

*Tool: soundness error $2^{-n}$.* $2^{-n} < 10^{-9}$ needs $n > 9\log_2 10 = 29.9$, so **30 rounds**. If each challenge were a number from 0 to 1023 instead of one bit, each round would cut the cheat's chance by 1024 and three rounds would do; practical protocols use a single huge challenge.

### Example 5 — a design review

*For each, name the technique and the residual risk. (a) Five banks want the number of customers who hold loans at three or more of them. (b) A health app wants a heart-rhythm model trained on a million users' watches. (c) A start-up rents cloud GPUs to run a model on clients' confidential contracts. (d) A website must check that a visitor is over 18.*

(a) Multi-party computation (a private set intersection with counting); risk: the count itself can identify someone if it is small, so suppress small counts. (b) Federated learning with secure aggregation and differential privacy; risk: without the last two, updates leak. (c) A trusted execution environment with attestation; risk: the chip's maker and side channels. (d) A zero-knowledge proof over a government-signed credential; risk: the credential issuer learns nothing here, but must itself be trusted to have checked the birth date.

### Example 6 — what does the total give away?

*Four flatmates run a secure sum of their monthly spending and obtain 9200. Three of them then compare notes. What do they learn, and what would stop it?*

They subtract their own three numbers and learn the fourth's exactly. No input-privacy protocol can help, since they used only the legitimate output and their own inputs. The options are to release a noisier answer (differential privacy), to release only a coarser one ("between 9000 and 10 000"), or to accept that with $n$ parties, the protocol protects you only against coalitions that are missing at least two people.

---

## Common Misconceptions (Teaching Notes)

### 1. "Encrypted data is useless until it is decrypted"
Homomorphic ciphertexts can be added and multiplied, and shares can be computed on. The cost is speed, not possibility.

### 2. "Federated learning is private because the data never leaves the device"
An update is a function of the data. One linear-model gradient returns a record exactly. Federation becomes private only with secure aggregation and differential privacy on top.

### 3. "A zero-knowledge proof proves nothing, since it reveals nothing"
It reveals nothing *beyond the truth of the claim*, and that one bit is what the verifier needed. Soundness is quantified: $2^{-n}$.

### 4. "A hardware enclave needs no trust"
It needs trust in the manufacturer's keys and design, and in the absence of side channels, which have been found repeatedly.

### 5. "If nobody sees the inputs, nothing leaks"
The output can leak, as can the pattern of who took part, when, and how large their messages were.

### 6. "These techniques make data sharing legal"
They are safeguards. Whether a purpose is lawful, and whether people were told, are separate questions that [[Data Protection and Privacy]] treats; pseudonymised and encrypted personal data generally remains personal data for whoever can reverse it.

---

## Exam Notes

**No school syllabus examines this material.** A search of the Cambridge 9618 (2027–29) and 0478 (2026–28) syllabuses, the IB Computer Science guide (first assessment 2027) and the AP Computer Science A course description finds none of: multi-party computation, secret sharing, homomorphic encryption, federated learning, trusted execution or zero-knowledge proof. It is first- and second-year university content in cryptography and machine-learning courses.

**What it strengthens that is examined.** Cambridge 9618 §6.1 and §7.1 and 0478 §5.3 ask for the difference between security and privacy and for measures that protect data: [[Data Protection and Privacy]] and [[Data Security]] are the examinable homes, and this card supplies the modern answer to "how can data be used without being disclosed?" IB A4.4 lists privacy among the ethical considerations of machine learning, for which Part IV is a concrete case. 9618 §17 (encryption, asymmetric keys, digital signatures) is the prerequisite for Parts III and VI, taught in [[Encryption]].

---

## Connections

- **Builds on:** [[Data Protection and Privacy]] — output privacy: anonymisation, tokens, differential privacy, and the law; [[Encryption]] — RSA, key exchange and the discrete logarithm; [[Artificial Intelligence]] — gradient descent, which federated averaging distributes; [[Prime Numbers]] — arithmetic modulo a prime, and why every non-zero number then has an inverse.
- **Mathematics:** [[Remainder and Factor Theorems]] — a polynomial of degree below $k$ is fixed by $k$ values, the whole of Shamir's scheme; [[Binomial Theorem]] — why $(1+n)^m \equiv 1 + mn$; [[Probability Basics]] — soundness as repeated independent halving.
- **Extends into:** [[Affective Computing]] — sensing that people will accept only if the raw signal provably stays with them; [[Digital Currency and Blockchain]] — zero-knowledge proofs for private payments, and threshold signatures for custody.
- **Same idea elsewhere:** [[Hash Tables]] and [[Error Detection and Correction]] — other places where adding structured redundancy or randomness buys a guarantee; [[Information Theory]] — "a share carries no information" is a statement about entropy.

---

## Beyond Syllabus

### Yao's millionaires
Recall that Part II computed on *shared numbers*. The field began in 1982 with Andrew Yao's puzzle: two millionaires wish to know who is richer without revealing their fortunes. His **garbled circuits** solve it for any function of two inputs: one party encrypts the truth table of every gate under random keys standing for the wire values, and the other evaluates the circuit blindly, able to decrypt exactly one row per gate. Two-party computation on the internet today mostly uses descendants of this.

### Private information retrieval
The caller-identification example is an instance of **PIR**: fetching row $i$ of a server's database without the server learning $i$. With additively homomorphic encryption the client sends an encrypted vector that is 1 in position $i$ and 0 elsewhere; the server computes $\prod_j c_j^{\,d_j}$, which is an encryption of $\sum_j [j = i]\, d_j = d_i$, and returns it. The server has touched every row and cannot tell which one mattered.

### From interactive proofs to one message
The cave needs a live verifier. Replace the verifier's random challenge with a hash of the prover's own commitment (the Fiat–Shamir transform) and the proof becomes a single message anyone can check, since the prover cannot choose the challenge before fixing the commitment. zk-SNARKs go further, encoding a whole computation as polynomial identities and checking them at a few random points, so that a proof of a long computation is a few hundred bytes.

### Why fully homomorphic encryption was hard
Recall that Paillier gives addition only. Schemes built on noisy lattice problems (learning with errors) give both operations, and their security rests on problems believed hard even for quantum computers. The noise that protects the message is also what limits the depth of computation, and Gentry's bootstrapping, decrypting inside the encryption, was the step nobody had seen for three decades.

---

## Sources

- P. Bogetoft and others, *Secure Multiparty Computation Goes Live*, Financial Cryptography 2009 (the Danish sugar-beet auction).
- A. Shamir, *How to Share a Secret*, Communications of the ACM 1979. A. Yao, *Protocols for Secure Computations*, 1982. D. Beaver, *Efficient Multiparty Protocols Using Circuit Randomization*, 1991.
- P. Paillier, *Public-Key Cryptosystems Based on Composite Degree Residuosity Classes*, Eurocrypt 1999. C. Gentry, *Fully Homomorphic Encryption Using Ideal Lattices*, STOC 2009.
- B. McMahan and others, *Communication-Efficient Learning of Deep Networks from Decentralized Data*, 2016. K. Bonawitz and others, *Practical Secure Aggregation for Privacy-Preserving Machine Learning*, 2017. L. Zhu, Z. Liu, S. Han, *Deep Leakage from Gradients*, 2019.
- S. Goldwasser, S. Micali, C. Rackoff, *The Knowledge Complexity of Interactive Proof Systems*, 1985. J.-J. Quisquater and others, *How to Explain Zero-Knowledge Protocols to Your Children*, 1989.
- Apple, *Announcing Swift Homomorphic Encryption* (swift.org, 2024), on Live Caller ID Lookup. 中共中央、国务院,《关于构建数据基础制度更好发挥数据要素作用的意见》, December 2022.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $x = \sum_i x_i \bmod p$ | `x = \sum_i x_i \bmod p` | additive secret sharing |
| $f(0)$, $\deg f = k-1$ | `f(0)` | Shamir: the secret is the constant term |
| $xy = c + db + ea + de$ | `xy = c + db + ea + de` | multiplication with a Beaver triple |
| $c = (1+n)^m r^n \bmod n^2$ | `c = (1+n)^m r^n \bmod n^2` | Paillier encryption |
| $g^s = t\,y^c$ | `g^s = t\,y^c` | the verifier's check |
| $2^{-n}$ | `2^{-n}` | a cheat's chance of surviving $n$ rounds |

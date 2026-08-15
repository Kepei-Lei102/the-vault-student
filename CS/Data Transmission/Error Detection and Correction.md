---
chinese: 差错检测与纠正 (chācuò jiǎncè yǔ jiūzhèng)
prerequisites:
  - "[[Number Bases]]"
  - "[[Bitwise Operations]]"
  - "[[Secondary Storage]]"
leads_to:
  - "[[A Fight With the Inevitable Errors]]"
tags:
  - subject/computer-science
  - domain/data-transmission
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-2-2
  - syllabus/9618-6-2
  - type/deep
  - type/definition
  - notation/binary
  - misconception/validation-is-verification
  - misconception/parity-catches-everything
  - misconception/check-digit-proves-correct
  - misconception/detection-implies-correction
---

# Error Detection and Correction 差错检测与纠正

> *Every wire, every radio link, every scratched disc surface is a place where a bit can quietly become the other bit. Nothing announces it. The receiving computer has no way of knowing it was handed damaged goods — a corrupted byte looks exactly like an intended one, because it **is** a byte.*
>
> *And it is not a matter of building things better. Perfect wiring and flawless code do not help against a cosmic ray or an electron that tunnels where it was not invited. So the only defence is one designed in advance: **send more than you need to**, arranged so that damage contradicts itself. That is the whole of this topic, and the interesting part is how little extra it takes — one spare bit per row and one per column is enough not merely to notice a flipped bit but to point straight at it.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| validation | 验证（合理性检查） | is this data *plausible*? checked against rules |
| verification | 核对（一致性检查） | is this data *faithful*? checked against the original |
| error detection | 差错检测 | noticing that something is wrong |
| error correction | 差错纠正 | working out what it should have been |
| parity bit | 奇偶校验位 | one spare bit that makes the count of 1s odd or even |
| parity block | 奇偶校验块 | parity on rows *and* columns, so the bad bit is locatable |
| checksum | 校验和 | send the total as well as the numbers |
| check digit | 校验位 | an extra digit computed from the others, for typed data |
| ARQ | 自动重传请求 | if it arrived wrong, ask for it again |
| redundancy | 冗余 | the extra data that makes the checking possible |

## Three questions, three prices

Students routinely merge these three into "checking the data". They are different questions, and each buys something the others cannot.

| | The question it asks | What it catches | What it cannot do |
|---|---|---|---|
| **Validation** | Is this data *sensible*? | nonsense — a month of 13, an empty name, an age of 900 | it cannot catch a **plausible lie**. Typing a real customer's age as 34 instead of 43 passes every rule you can write |
| **Verification** | Is this data *faithful* to what was sent or typed? | corruption and mistyping — the data changed on the way | it cannot tell you what the data *should* have been |
| **Correction** | What was it *supposed* to be? | the damage itself, repaired in place | nothing is free — it always costs more redundancy than mere detection |

> **A number can be perfectly valid and completely wrong.** That one sentence is the whole distinction between validation and verification, and it is worth saying out loud in a lesson, because the words sound like synonyms in English and their Chinese equivalents (验证 / 核对) split more cleanly than the English does.

## Why errors happen at all

Data in transit is a physical signal — a voltage on copper, a pulse of light, a radio wave, a magnetised patch. Anything that disturbs the signal disturbs the data, and the standard causes are **interference** from nearby electrical activity, attenuation over distance, and physical damage to the medium.

Those are the ones an engineer can fight. Two more cannot be engineered away at all, and they are the reason this whole topic exists rather than being a temporary embarrassment:

- **Radiation.** A cosmic-ray secondary particle, or an alpha particle from trace impurities in the chip's own packaging, deposits enough charge in a memory cell to flip it. The industry calls these **soft errors** — the hardware is undamaged, the stored value is simply now wrong. They are frequent enough to be budgeted for: server memory is specified with an expected error rate, and aircraft at altitude see more of them than equipment at sea level, because there is less atmosphere in the way.
- **Quantum tunnelling.** An electron has no strict boundary; it has a probability of being found on the far side of a barrier it has not got the energy to cross. In a flash memory cell, charge held on a floating gate slowly tunnels away, which is why an unpowered SSD eventually forgets. As transistors shrink, the barriers get thinner and the effect grows.

**Neither of these is a mistake anyone made.** They are the physics the machine is built out of, and no amount of care removes them. That is worth saying to a class outright, because it reframes the whole subject: error handling is not an apology for sloppy engineering, it is a permanent design requirement.

The syllabus names three consequences, and they are genuinely different:

- **Data loss** — bits that never arrive. The insidious version is a *partial* loss: what survives can still read as a perfectly plausible message, just not the one that was sent. (*V-MAX.* If you know, you know.)
- **Data gain** — spurious extra bits, picked up as noise.
- **Data change** — a bit that arrives as its opposite. The nastiest of the three, because the message is still the right *length* and still looks entirely legitimate.

## The first gate — validation

Validation is done by the **receiving program**, against rules chosen by whoever designed the system. It never compares against an original, because at data entry there is no original — only a human and a keyboard.

| Check | Asks | Example |
|---|---|---|
| **Range check** | is it between two bounds? | a month between 1 and 12 |
| **Limit check** | is it on the right side of *one* bound? | age $\geqslant 0$ |
| **Format check** | does it match the required pattern? | a postcode as letters-digits-letters |
| **Length check** | is it the right number of characters? | a 13-digit ISBN |
| **Presence check** | is there anything here at all? | a required email field |
| **Existence check** | does the thing it names actually exist? | a product code that is really in the catalogue |
| **Type check** | is it the right kind of data? | a quantity that is an integer, not text |
| **Check digit** | is the number self-consistent? | ISBN, bar codes — below |

## The second gate — verification

Verification always involves **a comparison against something authoritative**: either the human's intent, or the sender's original.

Verification comes in two flavours, and the difference is what it costs.

- **By repetition** — send or type the thing *twice* and compare the copies. Simple, and expensive: it doubles the work.
- **By summary** — send the data once plus a small computed fingerprint of it. Cheap, and imperfect: different data can share a fingerprint. Parity and checksums are this kind, which is why they cost one bit or one byte rather than a second copy.

**During data entry**, the original is what the human meant:

- **Visual check** — read back what you typed and compare it with the source document. Weak, because people see what they expect to see rather than what is there.
- **Double entry** — type it twice, and the machine compares. Stronger, because making the *same* slip twice in a row is unlikely. This is why a new password is always asked for twice.

> [!warning] Verification is the weakest of the three gates, and it is worth knowing why
> It only ever proves that **two copies agree**. It cannot prove that either copy is what you meant.
>
> Double-enter a password confidently and wrongly — the same wrong thing both times — and the check passes with a green tick. Both boxes matched. Neither of them was the password in your head, and you find that out tomorrow.
>
> ![[verification-double-entry-comic.png|640]]
>
> This is the same hole as validation's "plausible lie", one level up, and it is a live problem rather than a classroom curiosity: it is a large part of why the industry is moving to **passkeys and biometrics**, where there is no remembered secret to mistype and therefore nothing for double entry to faithfully preserve the wrong version of.

**During data transfer**, the original is what the sender sent — and that is where the rest of this page lives.

## Parity — one bit of conscience

Before sending a byte, count its 1s. Then set one spare **parity bit** so that the total count of 1s comes out even (**even parity**) or odd (**odd parity**) — the two systems must agree in advance which.

Take the seven data bits `1 0 1 1 0 0 1`. That is four 1s.

- Under **even parity** the count is already even, so the parity bit is `0` → sent as `1 0 1 1 0 0 1 0`.
- Under **odd parity** the count must become odd, so the parity bit is `1` → sent as `1 0 1 1 0 0 1 1`.

The receiver counts the 1s in what arrived. Wrong parity means the byte is damaged.

> [!question] If everything is stored in bytes, where does the parity bit actually go?
> A fair objection: adding a ninth bit to an eight-bit byte would wreck the tidiest structure in computing. The resolution is that **parity never lives inside the byte. It rides alongside it**, and hardware has three standard ways of finding it room.
>
> - **The character was seven bits by design.** This is the real reason [[Text Encoding|ASCII]] is a *7-bit* code on 8-bit hardware — seven bits of character, one bit spare, and that spare bit was the parity bit for decades of teleprinters and serial terminals. The byte was never violated; the payload was sized to leave room.
> - **The frame is bigger than the byte.** On a serial link the unit being sent is not a byte but a **frame**: a start bit, then the data bits, then an optional parity bit, then a stop bit. Parity is part of the envelope, not the letter.
> - **The hardware is physically wider.** Error-correcting server memory carries **nine** memory chips where an ordinary module has eight, moving 72 bits for every 64 bits of data. The extra width exists solely to hold the check bits.
>
> The principle underneath all three is worth stating plainly: **redundancy is always paid for with extra room, never by taking bits from the payload.** If it were taken from the payload it would not be redundancy — it would just be a shorter message.

> [!warning] Parity's honest limit — it misses exactly half of everything
> A single parity bit detects **any odd number** of flipped bits and **no even number** at all. Flip two bits in the same byte and the count of 1s changes by $-2$, $0$ or $+2$ — always an even change, so the parity still matches and the byte sails through looking perfect.
>
> This is not a flaw to be embarrassed about; it is the price of spending exactly one extra bit. It is also why the syllabus goes straight on to the parity *block*, which spends a few more and gets enormously more in return.

## The parity block — where detection becomes correction

Send a whole set of bytes as a rectangle. Give **every row** its parity bit, as before — and then add one extra row at the bottom holding the parity of **every column**. That bottom row is often called the *parity byte*.

Every row now sums to an even number of 1s, and so does every column. Now flip a single bit anywhere in the data — say the one in **row 3, column 5**:

![[parity-block-locates-the-bit.svg|880]]

- **Row 3's parity fails.** So the bad bit is somewhere in row 3.
- **Column 5's parity fails.** So the bad bit is somewhere in column 5.
- A bit that is in row 3 *and* in column 5 is one specific bit.

**The receiver now knows precisely which bit is wrong — and a wrong bit has only one possible correction.** Flip it back.

The same trick runs at the scale of whole disks. A [[RAID]] array of the RAID-5 kind stripes data across several drives and gives one drive's worth of space to parity — the XOR of the others. Lose an entire drive and every byte it held is recomputed from the survivors, for the price of one drive in the set. It is this rectangle, with each column a physical disk.

That is genuine **error correction**, built from nothing but parity, and it is sitting on an IGCSE syllabus. It is worth pausing on, because the leap from *"something is wrong"* to *"that one is wrong"* is the entire difference between the two halves of this card's title. Detection needs one bit; **location** needs a second dimension; and once you can locate, correction is free.

> [!tip] Where it still fails, and why that is the interesting part
> Flip **two** bits in the same row: that row's parity survives (two changes cancel), but *both* their columns now fail. You know something is wrong and you know which two columns — but not which rows — so you can detect without correcting. Flip four bits in a rectangle, one at each corner, and every row and every column stays even: the block is silently wrong.
>
> The pattern is general and worth stating: **more redundancy buys you a bigger family of errors you can survive**, and there is always a slightly larger family beyond it. The engineering question is never "is this safe?" but "is this safe enough for how noisy this channel actually is?"

> [!note] You are already doing this — reading is an error-corrected channel
> Ths sntnc s stll rdbl wth hlf ts lttrs gn. Written English carries roughly **50% redundancy**: Shannon measured it, and it means about half of what you read is, strictly speaking, unnecessary.
>
> It is not waste. Reading is a *noisy channel at both ends* — smudged print, a line your eye skipped, a moment when your attention was elsewhere, a word you half-know. The redundancy is what lets meaning survive all of that, and it is why you can read a typo without stopping.
>
> Which has a consequence for how explanations should be written. Good teaching prose **repeats deliberately**: a term defined in full on first appearance and recalled in a clause later, an idea stated once as a principle and again as an example. To a reader who caught it the first time, the repeat costs three seconds. To a reader who did not — because they were tired, because the sentence was dense, because reading is genuinely harder for some people than others — the repeat *is* the recovery. Same trade as a parity bit: spend a little extra so that damage does not destroy the message.
>
> It is worth knowing this before judging a text as too long. Some of what looks like padding is doing the same job the check bits do — and it is invisible precisely to the readers who did not need it.

## Checksum

Treat the block of data as numbers, add them all up, and send the total alongside. The receiver adds up what arrived and compares.

Bytes `212, 45, 199, 88` total $544$. Since a byte only holds $0$–$255$, the checksum is usually kept to one byte by taking the remainder: $544 \bmod 256 = 32$. The receiver re-adds, gets $32$, and accepts.

A checksum catches far more than parity — any single corrupted byte changes the total — but it is still a summary, and summaries collide. Two errors that cancel ($+3$ on one byte, $-3$ on another) leave the total untouched. Real protocols therefore use cleverer functions (CRCs) chosen so that cancellation is vanishingly unlikely, but the principle is exactly the one above.

## Echo check

The receiver sends the *entire message back*, and the sender compares it with what it originally sent. If they differ, something went wrong.

Simple, and weak for a reason worth asking students to find: **if the returned copy differs, you cannot tell whether the error happened on the way there or on the way back.** It also doubles the traffic. Echo check earns its place only where the return trip is cheap and errors are rare.

## Check digit — the one for human fingers

Everything above protects data in *transit*. A check digit protects data at *entry*, where the enemy is not interference but a person reading a number off a book and typing it in.

Humans make two characteristic mistakes: **a wrong digit**, and **a transposition** — two adjacent digits swapped. A check digit is an extra digit, computed from all the others by a fixed rule, chosen so that both mistakes break the rule.

### ISBN-13, worked in full

Take the first twelve digits of a real book — *Gödel, Escher, Bach* — which are `978030640615`.

**Step 1: weight the digits alternately 1, 3, 1, 3, …**

$$9(1) + 7(3) + 8(1) + 0(3) + 3(1) + 0(3) + 6(1) + 4(3) + 0(1) + 6(3) + 1(1) + 5(3)$$

$$= 9 + 21 + 8 + 0 + 3 + 0 + 6 + 12 + 0 + 18 + 1 + 15 = 93$$

**Step 2: the check digit is whatever makes the total a multiple of 10.**

$$93 + d \equiv 0 \pmod{10} \quad\Longrightarrow\quad d = 7$$

So the full ISBN is **978-0-306-40615-7**, and the printed check digit on the back of that book is indeed 7. To *verify* an ISBN you do the same sum including the check digit and confirm the total is divisible by 10.

### Why the weights are 1 and 3, and not 1 and 1

This is the part usually left out, and it is the entire design.

If every digit were weighted equally, swapping two adjacent digits would not change the sum at all — every transposition would be invisible. With alternating weights $1$ and $3$, swapping neighbouring digits $a$ and $b$ changes the total by

$$(3a + b) - (a + 3b) = 2(a-b)$$

so the check fails unless $2(a-b) \equiv 0 \pmod{10}$ — that is, unless $a - b = \pm 5$.

**So ISBN-13 catches every single-digit error and every transposition except those where the swapped digits differ by exactly 5.** Swap a 2 and a 7 and the code is silently happy. That hole is *known and accepted*: it is 10 of the 90 possible ordered pairs, the alternative schemes that close it are harder to compute by hand, and a check digit was designed for an era of paper catalogues and human clerks.

Bar codes (EAN-13) use exactly the same rule — an ISBN-13 *is* an EAN-13, which is why a book scans at a supermarket till.

The Chinese names for the two generations of printed code carry the whole engineering leap in their characters: **条形码** is a *strip* code, one-dimensional, holding a dozen digits guarded by a single check digit; **二维码** is literally a *two-dimensional* code, holding thousands of characters and protecting them with an error-correcting code strong enough to survive a third of the symbol being destroyed. Adding the second dimension bought capacity and durability at once — [[Stories/A Fight With the Inevitable Errors]] is how that came about, in a Japanese factory in 1994.

## ARQ — the cheapest answer of all

**Automatic Repeat reQuest** is the honest admission that fixing an error yourself is expensive, and that if you can simply ask again, you should.

1. The receiver checks each arriving block, using any of the methods above.
2. If it passes, the receiver sends a **positive acknowledgement (ACK)**.
3. If it fails, the receiver sends a **negative acknowledgement (NAK)** and the sender retransmits.
4. If *nothing* comes back at all — the block vanished, or the acknowledgement did — the sender's **timeout** expires and it retransmits anyway.

The timeout is the part students skip, and it is the part that makes the system actually work: without it, a lost message would leave both machines waiting forever, each politely expecting the other.

**And real protocols do not retry indefinitely.** Every practical ARQ carries a **retry limit**: Wi-Fi abandons a frame after a set number of attempts, and TCP retransmits with progressively longer gaps — *exponential backoff* — before eventually giving up and reporting the connection dead. The reason is worth drawing out, because it is not obvious that giving up is a feature.

A link that is genuinely broken will fail every retransmission, so an unbounded retry never terminates and never reports anything: the program above it waits forever with no information. A bounded retry converts an impossible situation into an *answer* — *this cannot be delivered* — which the layer above can act on, by showing an error, choosing another route, or falling back. **Knowing when to stop asking is part of the protocol, not a shortcoming in it.**

> **ARQ needs only detection, never correction.** That is why it is everywhere: on a channel where you can ask again, detection is enough, and detection is cheap. Correction earns its keep precisely where asking again is impossible — a spacecraft eight hours away by light, or a scratched disc that will never be any less scratched.

## The price of each method

| Method | Extra data | Detects | Corrects | Where it fits |
|---|---|---|---|---|
| Parity bit | 1 bit per byte | odd numbers of flipped bits | ✗ | cheapest possible check |
| Parity block | 1 bit per row + 1 row | most patterns | **✓ single bit** | when you must repair, not re-ask |
| Checksum | 1 byte per block | any change to the total | ✗ | whole-block integrity |
| Echo check | the entire message again | any difference | ✗ | short messages, cheap return path |
| Check digit | 1 digit | single-digit and most transpositions | ✗ | typed data |
| ARQ | acknowledgements | (relies on the above) | by retransmission | any two-way link |

## Common misconceptions (teaching notes)

### 1. "Validation and verification are the same thing"

The two English words are near-synonyms in ordinary speech, so the distinction feels artificial until it is made concrete.

**Fix:** one example, asked as a question. *A form demands an age between 0 and 120. A user means to type 43 and types 34. Which check catches it?* Neither range nor format nor length — it is a perfectly valid age. Only **double entry** catches it, and double entry is verification. Then reverse it: a transmission error turns 43 into 993, which validation catches instantly. Two different diseases, two different medicines.

### 2. "Parity catches errors"

Stated without qualification, and students then believe a parity bit makes a byte safe.

**Fix:** make them break it. Give a byte with even parity, ask them to flip any two bits, and recount. The parity is still correct and the byte is still wrong. Then ask what fraction of two-bit errors slip through — all of them.

### 3. "A valid check digit means the number is right"

**Fix:** a check digit proves a number is **self-consistent**, not that it is the number you wanted. Type a completely different but genuine ISBN and every check passes — you have simply ordered the wrong book. The check digit guards the *typing*, not the *choosing*. (This is the same distinction as misconception 1, one level up.)

### 4. "If you can detect an error you can fix it"

The instinct that makes the parity block feel obvious in hindsight — and, historically, the exact frustration that started the whole field.

**Fix:** hold up a single parity bit. It says *one of these eight bits is wrong*. Which one? There are eight equally consistent repairs and no way to choose. **Detection needs one bit; correction needs enough redundancy to identify a culprit** — which is why the parity block needs a second dimension before it can point. Get them to feel that gap before showing the block, and the block lands as an answer rather than a recipe.

## Exam Notes

### Cambridge IGCSE 0478 — **§2.2 Methods of error detection**

Four learning objectives, all of them "describe" or "understand" — this is a written-answer section with no calculation beyond the check-digit arithmetic.

- **Understand the need to check for errors after transmission, and how errors occur** — the marks are for naming a *cause* (interference) and a *consequence* (data loss, data gain, data change), not for saying "errors happen".
- **Describe parity check (odd and even), checksum and echo check** — the syllabus specifically adds **parity byte and parity block check**, so the rectangle above is examinable, not enrichment.
- **Describe how a check digit is used to detect errors in data entry, and identify examples** — **ISBN and bar codes are named in the syllabus**, so know both by name.
- **Describe how ARQ establishes that data is received without error** — the syllabus names **positive/negative acknowledgements** and **timeout**. All three earn marks; the timeout is the one most often missed.

**Answer-writing notes.** "Describe" wants the *process*, in order, not a definition — a parity answer that never mentions counting the 1s *at the receiving end* has only described half the method. And say which parity system is in use before computing anything: a byte is only correct or corrupt *relative to an agreed convention*.

### Cambridge A-Level 9618 — **§6.2 Data Integrity**

9618 frames the same material more broadly and expects the vocabulary split to be precise:

- **Describe how data validation and data verification help protect the integrity of data** — the distinction is examined directly, and answers that treat them as synonyms lose the marks.
- **Describe and use methods of data validation** — range, format, length, presence, existence, limit, and check digit. Note **"and use"**: you may be asked to apply one, or to say which is appropriate for a stated field.
- **Describe and use methods of data verification** — split by stage: **during data entry** (visual check, double entry) and **during data transfer** (parity check byte *and* block, checksum).

The reliable trap is a question that gives a field and asks for *the most appropriate check*. Read whether the risk is nonsense (validation) or mistyping (verification) before choosing.

### Where this is *not* examined

Hamming codes, CRCs and Reed–Solomon appear on **no** Cambridge pre-university syllabus. They are the natural next step and they are genuinely beautiful, but nothing below is required for either paper.

> [!info] Beyond syllabus — what a checksum grows up into
> The checksum above is the toy version of a real family, and the family splits by **what it is defending against**.
>
> Against *noise*, the standard tool is a **CRC** (cyclic redundancy check). It is still a fingerprint computed from the data, but the arithmetic is chosen so that the burst errors real channels actually produce cannot cancel out. Every Ethernet frame carries one.
>
> Against an *adversary*, you need a **cryptographic hash** — MD5, and its successors SHA-1 and SHA-256. The download page that lists a long hex string beside a file is asking you to verify exactly as above: recompute, compare.
>
> And **MD5 is the instructive one, because it is simultaneously broken and fine.** It is broken for security: it is now practical to construct *two different files with the same MD5 digest on purpose*, so an MD5 match no longer proves nobody tampered with the file. It remains perfectly adequate for spotting *accidental* corruption, because a random flipped bit will not stumble onto a collision.
>
> That distinction is the one to carry away: **resisting noise and resisting an opponent are different requirements**, and a check built for one is not automatically fit for the other. Noise is indifferent; an attacker is aiming. (Hashing algorithms in their own right are examined on 9618 — see [[Hash Tables]] for the data-structure use, where the requirement is different again: there you want collisions to be *rare and cheap*, not impossible.)

> [!info] Beyond syllabus — Hamming distance, and how far apart codewords have to be
> Two binary strings' **Hamming distance** is the number of positions where they differ; `1011` and `1001` are distance 1 apart. Think of every possible message as a point, and the legal codewords as a scattering of special points among them. An error nudges you off a codeword.
>
> Everything follows from how far apart the legal codewords are. If the nearest two are distance $d$, you can **detect** up to $d-1$ errors (any smaller nudge cannot land you on another legal codeword) and **correct** up to $\left\lfloor\frac{d-1}{2}\right\rfloor$ (a nudge smaller than half the gap still leaves the original nearest). A single parity bit gives $d = 2$: detect one, correct none — exactly what we found by counting.
>
> **Richard Hamming's 1950 codes** made this systematic: place parity bits at positions $1, 2, 4, 8, \ldots$, each covering a different subset of the data bits, and the pattern of failures spells out the position of the bad bit *in binary*. It is the parity block's trick, compressed — and it is why [[Gray Code]]'s "Hamming distance" carries his name too.

> [!info] Beyond syllabus — when you cannot ask again
> ARQ collapses the moment retransmission is impossible or absurdly expensive: a probe past Neptune, a scratched CD, a QR code on a rain-damaged poster. Those channels need codes that repair damage from the received copy alone — **Reed–Solomon**, which treats the data as a polynomial and the errors as unknowns to be solved for, using power sums to reconstruct where the damage is. The mathematics is the same machinery as [[Symmetric Functions of Roots]], and the history of how anyone came to want it is [[Stories/A Fight With the Inevitable Errors]].

## Connections

- **Built on:** [[Number Bases]] — everything here is counting 1s in binary; [[Bitwise Operations]] — parity is XOR over the whole byte, and checksums are addition with wraparound.
- **Neighbour:** [[Gray Code]] — the other card that turns on Hamming distance, for the opposite reason: Gray code arranges values so consecutive ones differ in exactly one bit, minimising the damage a mistimed read can do.
- **Where the story is:** [[Stories/A Fight With the Inevitable Errors]] — Hamming's ruined weekends, and the fifty years between "why can't it fix itself?" and a QR code surviving a coffee stain.
- **The mathematics underneath:** [[Symmetric Functions of Roots]] — power sums in, error positions out, which is how a scratched disc is actually repaired.
- **Same instinct elsewhere:** [[Information Theory]] — redundancy as the thing that makes a message survivable, measured rather than guessed.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $a \equiv b \pmod{n}$ | `a \equiv b \pmod{n}` | the check-digit condition |
| $\left\lfloor x \right\rfloor$ | `\left\lfloor x \right\rfloor` | floor — used in the correction bound |
| $d$ | `d` | Hamming distance between codewords |
| $\oplus$ | `\oplus` | XOR — parity of a byte is the XOR of its bits |

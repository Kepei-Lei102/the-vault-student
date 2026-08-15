---
chinese: 与必然的错误搏斗 (yǔ bìrán de cuòwù bódòu) — 机器如何学会修好自己
prerequisites:
  - "[[Error Detection and Correction]]"
leads_to:
  - "[[Information Theory]]"
tags:
  - type/story
  - subject/computer-science
  - subject/mathematics
  - era/20c
  - cast/hamming
  - cast/shannon
  - cast/reed
  - cast/solomon
  - cast/berlekamp
  - cast/hara
  - region/usa
  - region/japan
---

# A Fight With the Inevitable Errors 与必然的错误搏斗

> *"Damn it, if the machine can detect an error, why can't it locate the position of the error and correct it?"*
>
> — Richard Hamming, on the Monday morning that started all of this

## Act I — The ruined weekend

Bell Telephone Laboratories, New Jersey, 1947. Richard Hamming is thirty-two, newly arrived from Los Alamos, where he had spent the war running calculations for the bomb and thinking hard about what machines could and could not be trusted to do.

At Bell Labs he has a problem, and it is a problem of rank. The Model V relay computer — a room of clattering electromechanical switches — belongs during the week to people more senior than he is. Hamming gets the weekend. He loads his job on Friday evening, goes home, and comes back on Monday to collect the results.

The Model V was, for its era, admirably careful. It checked its own work: each number carried extra digits arranged so that a mangled value could be spotted. And when the machine spotted one, it did the sensible thing. It stopped that job, dumped it, and moved on to the next one in the queue.

Which meant that on Monday morning, Hamming had nothing.

One bad relay, some time on Saturday night, and two days of machine time had been thrown in the bin — politely, correctly, by a machine doing exactly what it had been designed to do.

If 1947 makes that feel distant, translate it. It is the eighty-gigabyte game download that died at 3 a.m. at ninety-nine percent because the connection hiccuped once. The overnight render abandoned at the last frame. The job that ran all night and crashed writing its results. That particular morning feeling — everything was *fine except for one moment, and now there is nothing* — has not changed since the relays. The only difference is that Hamming's next attempt was a week away, because he only had the machine on weekends.

He resubmitted. The following Monday, it happened again.

![[inevitable-errors-monday-morning-comic.png|720]]

## Act II — The question nobody had thought to ask

Most people, on the second Monday, would have been angry at the machine, or the queue, or the relay. Hamming was angry at something more useful: at the *design*.

The machine had known that a number was wrong. That was the whole point of the extra digits. And knowing that, it had thrown everything away and stopped.

> *If it is smart enough to know something is broken, why is it not smart enough to work out what?*

Written down, it sounds obvious. It was not obvious. It was a genuinely new question, and it is worth being precise about why nobody had asked it — because the answer is the entire technical content of the field that followed.

**Detection and correction are not the same size of problem.** A single parity bit says *one of these eight bits is wrong*. Which one? There are eight possible repairs and nothing whatsoever to choose between them. The information simply is not there. You cannot squeeze a location out of one bit of evidence, however clever you are.

So Hamming's question is really: **how much extra would you have to send, and how would you have to arrange it, so that the damage points at itself?**

## Act III — Parity, arranged cleverly

His answer, worked out over the following months and published in 1950, is one of those ideas that seems inevitable the moment you see it and was invisible before.

Don't send *one* extra bit. Send several — and make each one guard a **different, overlapping** group of the data bits. Then a single flipped bit will break some of those guards and leave others intact, and *which ones broke* is itself a number. Arrange the groups properly, and that number is the position of the guilty bit, written in binary.

The machine no longer says "something is wrong". It says "**bit eleven**". And a wrong bit has only one possible correction.

You can see the same trick in miniature in the **parity block** on [[Error Detection and Correction]] — parity on the rows, parity on the columns, and the bad bit sits at the intersection of the row that failed and the column that failed. Hamming's codes are that idea done efficiently, with the guards overlapping instead of laid out in a neat rectangle.

**And there was somebody down the corridor who could say what it meant.** Claude Shannon was at Bell Labs in exactly those years, assembling the paper that became *A Mathematical Theory of Communication* — the founding document of [[Information Theory]] — and Hamming's code appears in it. Shannon proved something almost unbelievable: for any channel, however noisy, there exists a coding scheme that gets your message through with as little error as you care to specify. He proved that such codes *exist*. He did not say how to build one.

That gap — between knowing a thing is possible and knowing how to do it — is where the next fifty years of this story lives.

## Act IV — Two men, five pages, and a theory nobody could use

MIT Lincoln Laboratory, 1960. **Irving Reed** and **Gustave Solomon** publish a paper of about five pages with an unpromising title: *Polynomial Codes Over Certain Finite Fields*.

The idea in it is startlingly elegant. Stop thinking of your message as a string of symbols. Think of it as a **polynomial** — and send not the coefficients but the polynomial's *values* at a set of agreed points. A polynomial of low degree is enormously over-determined by many values: any small number of them can be corrupted, and the true polynomial still shows through the wreckage, because no *other* low-degree polynomial passes near enough to that many of the surviving points.

It is the same instinct as drawing a straight line through scattered dots. Two points define the line; twenty points let you throw away the three that are obviously wrong.

And the mathematics for finding the damage turns out to be the machinery of [[Symmetric Functions of Roots]] — the receiver measures power sums of positions it cannot see, converts them into the coefficients of a polynomial whose *roots* are exactly the damaged positions, and only then goes looking for roots.

There was one problem, and it lasted fifteen years.

**Nobody could compute it.** The original decoding method was correct and hopelessly slow — fine on paper, useless in a machine that had to keep up with an incoming signal. Reed–Solomon codes spent the 1960s as a beautiful thing that specialists admired and nobody shipped.

## Act V — Making it run

The unlock came from **Elwyn Berlekamp** in 1968, with a decoding algorithm fast enough to be real, simplified the following year by **James Massey** into the form still taught as Berlekamp–Massey.

Berlekamp is worth a sentence of his own, because he is not the man the story would invent. He was a serious game theorist who wrote the book on the mathematics of Go endgames, later co-authored *Winning Ways for Your Mathematical Plays*, and ran a hedge fund. The algorithm that made deep-space photography and the compact disc possible was, to him, one interesting problem among many.

With Berlekamp's algorithm, Reed–Solomon stopped being a theorem and became a component.

## Act VI — Eight hours away, at the speed of light

**Voyager 2** left Earth in 1977 and kept going: Jupiter, Saturn, then out to the planets nobody had ever photographed closely.

By Uranus in 1986 and Neptune in 1989, the spacecraft was so far away that its signal arrived at a power measured in fractions of a billionth of a watt, and a round trip for any message took hours. Consider what that does to the strategy of **asking again**. A corrupted image line means a request going out, four hours in flight, and a retransmission coming back four hours later — from a probe on a trajectory that will never return, with a power budget that is draining, past a planet it is leaving at fifteen kilometres per second.

You do not get to ask again. **You have to be able to repair what arrived.**

So Voyager's later encounters ran a concatenated scheme with Reed–Solomon on the outside, and the photographs of Neptune's blue crescent and the geysers of Triton came home through it — assembled on Earth from a signal that arrived damaged and was *repaired*, by an algorithm that had been an unusable curiosity when the probe was designed.

## Act VII — The scratch you can see, and the note you cannot hear

The other place where asking again is impossible is closer to hand: a disc lying on a table.

When Philips and Sony specified the **compact disc** around 1980, they faced a fact about human beings. People put things down on other things. Discs get fingerprints, dust, and scratches, and a scratch does not damage one bit — it wipes out a long continuous run of them, thousands in a row.

Reed–Solomon can repair a few errors in a block. It cannot repair a block that has been obliterated. So the CD's designers added the move that makes the whole thing work, and it is beautiful: **interleaving**.

Do not store the music in order. **Scatter it.** Take consecutive samples and place them far apart on the spiral, interleaved with samples from elsewhere, according to a fixed shuffle. Now a scratch that destroys a long continuous run of the *disc* destroys a few scattered symbols from each of very many codewords — and a few scattered symbols is precisely the damage Reed–Solomon was built to absorb.

The scheme is called **CIRC**, Cross-Interleaved Reed–Solomon Code, and it is why a disc with a visible scratch plays without a click. The damage was real. It was spread thin enough to be survivable, and then repaired.

*The trick generalises past discs: if your errors come in bursts, rearrange the data so that a burst in the world becomes a scatter in the message.*

## Act VIII — A lunch break, and a board of black and white stones

Denso Wave, a Toyota subsidiary in Japan, 1994. **Masahiro Hara** has been asked to solve a factory problem: bar codes hold too little, and workers scanning car parts are having to read several per item.

Hara's account of where the answer came from is a good one. He was playing **Go** on a lunch break — the black and white stones on their grid — and saw a way for a pattern to say *here I am, and this is which way up I am*. That became the QR code's three big square eyes, which is how a scanner can read the code from any angle at all, upside down, at speed, on a moving part.

And because the code was going to live in a **factory** — on parts that get oily, scuffed, and rained on — it was built with Reed–Solomon in it from the beginning, at four selectable strength levels. At the highest, roughly a third of the code can be destroyed and the data still comes back.

Which is why you can print a company logo in the middle of a QR code, punching a hole clean through the data, and it still scans. The hole is damage. The code was designed to expect it.

Denso Wave chose not to enforce their patent. That decision is the reason the QR code is on restaurant tables, medicine boxes and payment terminals across the world rather than in one company's factories.

## What the whole thing is about

Follow the thread from 1947 to now and the same shape keeps appearing.

A relay fails on a Saturday night. A radio signal crosses four billion kilometres and arrives as a whisper. A disc is set down on a table. In every case, the world was going to damage the message, and no amount of care was going to stop it.

**The response was not to prevent the damage. It was to accept it in advance and build a message that could survive it.** Send more than you need. Arrange the extra so that damage contradicts itself. Scatter the data so that a wound in the world is a scratch in the message.

There is something worth taking out of the technical setting. Hamming's insight was not that errors are bad — everyone knew that. It was that **a system that merely notices its own failures has stopped one step too early**, and that the step from noticing to repairing is a design problem, not a miracle. He was not smarter than his colleagues about relays. He was less willing to accept that Monday morning was simply how things were.

> The machine could tell him something had gone wrong. He wanted to know what.

## Connections

- **The card underneath:** [[Error Detection and Correction]] — parity, the parity block, checksums, check digits and ARQ, with the parity block standing as Hamming's insight in miniature.
- **The mathematics:** [[Symmetric Functions of Roots]] — power sums of positions nobody can see, converted into a polynomial whose roots are the damage. Worked in full there over the integers mod 11.
- **The theory next door:** [[Information Theory]] — Shannon proving that good codes must exist, in the same building and the same years, while Hamming was building one.
- **Same distance, other purpose:** [[Gray Code]] — Hamming distance again, arranged so that consecutive values differ in one bit and a mistimed read is off by the smallest possible amount.
- **Where the errors come from:** [[Secondary Storage]] — the physics of a scratch, a flux reversal and a floating gate, and why every storage medium is an analogue quantity with a decision boundary drawn across it.

---

## Sources and further reading

- R. W. Hamming, *Error detecting and error correcting codes*, Bell System Technical Journal 29 (1950) — the founding paper, and readable.
- I. S. Reed and G. Solomon, *Polynomial Codes Over Certain Finite Fields*, J. SIAM 8 (1960).
- C. E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal 27 (1948).
- R. W. Hamming, *You and Your Research* (1986 lecture) — not about codes, but the clearest surviving picture of how he chose problems.

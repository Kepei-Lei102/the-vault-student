---
chinese: 数据压缩 (shùjù yāsuō)
prerequisites:
  - "[[Text Encoding]]"
  - "[[Image Encoding]]"
  - "[[Sound Encoding]]"
  - "[[Information Theory]]"
leads_to:
  - "[[Encryption]]"
tags:
  - subject/computer-science
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - level/IB
  - syllabus/0478-1-3
  - syllabus/9618-1-3
  - syllabus/IB-CS-A2-3
  - type/deep
  - type/definition
  - type/technique
  - notation/compression-ratio
  - misconception/everything-can-be-compressed
  - misconception/compressing-twice-shrinks-twice
  - misconception/lossy-is-recoverable
  - misconception/rle-always-helps
---

# Compression 数据压缩

## Definition

### Formal

**Compression** is re-encoding data so that it occupies fewer bits. It comes in exactly two kinds, split by one question — *can you get the original back?*

- **Lossless compression** re-encodes the data so the process is perfectly reversible: decompression reconstructs the original **bit for bit**. Nothing is discarded; the file only *says the same thing more efficiently*.
- **Lossy compression** *permanently removes* information the recipient is judged not to need. The file gets far smaller, and the original is gone for good — decompression rebuilds an approximation, never the original.

Why bother? The three-way payoff every exam wants stated: a smaller file needs **less storage space**, **less bandwidth**, and a **shorter transmission time**. Every photo you send, every video you stream, every web page you load is compressed — uncompressed video alone would be roughly 1.5 gigabits *per second* of viewing.

### Intuitive

The two kinds of compression are two different arts:

- **Lossless is the art of never saying the same thing twice.** "AAAAAAAA" and "8 As" carry identical information; one takes 8 symbols, the other takes 3. If a file has *any* pattern — repeated runs, some symbols commoner than others, parts that echo earlier parts — that pattern is wasted space, and lossless compression reclaims it.
- **Lossy is the art of knowing what your audience won't miss.** Your eye cannot tell 16 million colours from 4 million in a busy photo; your ear cannot hear a quiet tone in the shadow of a loud one. Lossy compression deletes exactly those imperceptible details — it is an engineering deal struck with human senses, not with mathematics.

One art is a promise ("you'll get every bit back"); the other is a judgement call ("you'll never notice"). Everything on this page follows from which of the two you are allowed to make.

### 中文锚点

**数据压缩 (shùjù yāsuō)** = 用更少的比特重新编码同样的数据。

| English | 中文 | Idea |
|---|---|---|
| Lossless compression | 无损压缩 (wúsǔn yāsuō) | 完全可逆，逐位还原 |
| Lossy compression | 有损压缩 (yǒusǔn yāsuō) | 永久删除信息，只能还原近似 |
| Run-length encoding (RLE) | 行程长度编码 (xíngchéng chángdù biānmǎ) | 把"连续重复"记成 (个数, 值) |
| Huffman coding | 霍夫曼编码 (huòfūmàn biānmǎ) | 常见符号用短码，罕见符号用长码 |
| Redundancy | 冗余 (rǒngyú) | 可被压缩掉的"废话" |
| Compression ratio | 压缩率 (yāsuō lǜ) | 原大小 ÷ 压缩后大小 |
| Entropy | 熵 (shāng) | 无损压缩的理论下限（见 [[Information Theory]]） |

考试语言注意：Cambridge 两个板块都**点名 RLE**；0478 的有损压缩答案要用它自己的四个动词——降低分辨率 (resolution)、降低色深 (colour depth)、降低采样率 (sample rate)、降低采样精度 (sample resolution)。

---

## Why compression is possible at all — redundancy

A file can be compressed only if it is, in a precise sense, *wasteful* — if the encoding spends more bits than the information deserves. Real files are wasteful in three recurring ways:

1. **Runs.** Neighbouring values repeat exactly: the white background of a screenshot, the silence between tracks, the blue sky across the top of a photo.
2. **Skewed frequencies.** Some symbols occur far more often than others, yet naive encodings ([[Text Encoding]]'s 8 bits per character, [[Image Encoding]]'s fixed bits per pixel) charge every symbol the same price. In English text, `e` appears about 170 times as often as `z` — but ASCII bills them identically.
3. **Echoes.** Parts of the file repeat earlier parts wholesale — the word "the" thousands of times, the same header phrase, the same texture tile.

Each waste has a lossless technique that targets it: **run-length encoding** for runs, **Huffman coding** for skewed frequencies, **dictionary methods** for echoes. And beneath all three sits a hard floor: a source's **entropy** is the minimum average bits per symbol *any* lossless scheme can achieve — the theorem, the proof, and the exact formula live in [[Information Theory]] §"Source coding — entropy is the compression limit". Lossless compression never creates a miracle; it only collects the waste.

---

## Run-length encoding — the exam's favourite

RLE replaces each **run** of identical values with a pair: *(count, value)*. It is the simplest real compression scheme, which is exactly why both Cambridge boards name it.

![[compression-rle-bitmap.svg|697]]

**Worked example — the bitmap row.** A row of a two-colour cartoon reads:

$$\underbrace{WWWWWW}_{6}\;\underbrace{BB}_{2}\;\underbrace{WWWW}_{4}\;\underbrace{BB}_{2}\;\underbrace{WW}_{2}$$

Raw storage at 1 bit per pixel: $16$ bits. RLE stores five pairs — $(6,W)(2,B)(4,W)(2,B)(2,W)$. With 4 bits for each count and 1 bit for each colour, that is $5 \times 5 = 25$ bits… **bigger than the original!** On a tiny row the bookkeeping outweighs the savings — but scale up: a 1920-pixel row of a screenshot that is entirely white costs $1920$ bits raw and *one pair* in RLE. RLE's natural prey is long runs: cartoons, diagrams, screenshots, scanned documents, fax machines (its first mass deployment), and the flat-colour regions of [[Image Encoding]]'s bitmap world.

**The honest edge — RLE can inflate.** In a noisy photograph, neighbouring pixels almost *never* repeat exactly, so nearly every run has length 1 — and storing $(1, \text{value})$ for each pixel is strictly bigger than storing the value alone. A compression scheme tuned to one kind of waste does nothing (or worse) on data that lacks it. This is a first taste of a deep fact proved under §Beyond Syllabus: **no scheme compresses everything.**

---

## Huffman coding — charge less for the common

The second waste — skewed frequencies — falls to an older idea than computing itself: **give the frequent symbols short codes and the rare symbols long ones.** Morse code did it in the 1840s: `e`, the commonest English letter, is a single dot; `q` is dah-dah-dit-dah.

Huffman's 1952 algorithm does it *optimally* (built greedily from the two rarest symbols upward — the construction and its optimality proof live in [[Information Theory]] §"Huffman codes"). Watch it work on an exam-sized example:

![[compression-huffman-mississippi.svg|697]]

**Worked example — MISSISSIPPI.** Frequencies: I×4, S×4, P×2, M×1. The tree assigns $S \to 0$, $I \to 10$, $P \to 110$, $M \to 111$: the two workhorses get 1 and 2 bits, the rarities pay 3. Compressed size:

$$4(1) + 4(2) + 2(3) + 1(3) = 21 \text{ bits} \qquad \text{vs. ASCII's } 11 \times 8 = 88 \text{ bits}$$

— a saving of 76%. Two structural details carry the idea:

- **No code is a prefix of another** (you never meet $S$'s code while reading $M$'s), so the bitstream decodes unambiguously without separators — that is why codes must come from a *tree*.
- **The floor is close — and small enough to compute by hand.** Recall from [[Information Theory]] that a symbol of probability $p$ carries $-\log_2 p$ bits of surprise — its *fair price* — and entropy is the average price over the source:

$$H = -\sum_i p_i \log_2 p_i = -\left[\tfrac{4}{11}\log_2\tfrac{4}{11} + \tfrac{4}{11}\log_2\tfrac{4}{11} + \tfrac{2}{11}\log_2\tfrac{2}{11} + \tfrac{1}{11}\log_2\tfrac{1}{11}\right].$$

Price each letter: $I$ and $S$ have $p = \tfrac{4}{11}$, so each costs $\log_2\tfrac{11}{4} \approx 1.46$ bits, contributing $\tfrac{4}{11} \times 1.46 \approx 0.531$ apiece; $P$ costs $\log_2\tfrac{11}{2} \approx 2.46$, contributing $\approx 0.447$; $M$ costs $\log_2 11 \approx 3.46$, contributing $\approx 0.315$. Total:

$$H \approx 0.531 + 0.531 + 0.447 + 0.315 = 1.82 \text{ bits/symbol} \quad\Longrightarrow\quad 11 \times 1.82 \approx 20.1 \text{ bits for the word.}$$

  And now Huffman's 21 bits explains itself: **Huffman is the entropy price list rounded to whole bits.** The fair prices are $1.46 / 1.46 / 2.46 / 3.46$; Huffman can only charge $1 / 2 / 3 / 3$ — codes come in whole bits — and that rounding costs the missing $\approx 0.9$ bits. (When every probability is a power of $\tfrac12$ the fair prices are already integers and Huffman lands *exactly* on the floor — [[Information Theory]]'s worked distribution is built that way on purpose.) Nothing lossless can beat $H$: the waste collected, the floor reached — compression is *bounded honesty*, not magic.

**Dictionary methods**, the third family, handle echoes: instead of re-sending a phrase the file has already contained, send a short back-reference ("copy 5 symbols from 300 symbols ago"). The LZ77 family of algorithms built on this idea powers ZIP, gzip, and PNG — every "zipped" file you have ever made is dictionary compression with a Huffman layer on top.

---

## Lossy compression — the deal with your senses

When the recipient is a *human being* rather than a program, a second budget opens up: everything below the threshold of perception. Lossy compression spends it deliberately.

At IGCSE level, lossy compression is described by four concrete verbs, and they are worth memorising as a family because each one turns a dial from an encoding card you already know:

| Verb | What it discards | The dial it turns |
|---|---|---|
| Reduce the **resolution** | pixels | [[Image Encoding]] — fewer samples of the scene |
| Reduce the **colour depth** | shades | [[Image Encoding]] — fewer bits per sample |
| Reduce the **sample rate** | high frequencies | [[Sound Encoding]] — fewer samples per second |
| Reduce the **sample resolution** | quiet detail | [[Sound Encoding]] — fewer bits per sample |

Real-world formats are cleverer versions of the same trade. **JPEG** keeps the pixel count but discards fine detail *within* each small block — precisely the detail eyes are worst at seeing — with a quality dial from "indistinguishable" to "visible blocky wreckage":

![[compression-jpeg-quality-ladder.png|820]]

**Why over-compressed images turn green-and-purple — the 包浆 effect.** JPEG does not treat brightness and colour equally: the eye resolves brightness sharply but colour coarsely, so the format stores **colour at a fraction of the resolution** and quantises it hardest (*chroma subsampling* — one more perceptual deal, unpacked in full in [[Chroma and Luma]]). Each re-save compounds the colour damage first, so a meme that has been screenshotted and reposted through enough generations grows green-and-purple fringes and a muddy sheen. Chinese social media has the perfect word for it: the image **包浆了** — it has "developed a patina," like a prayer bead polished by thirty years of handling. The joke is precise engineering: the patina *is* chroma quantisation error, compounding one lossy generation at a time — misconception 3 in slow motion.

> [!info] What about RAW files?
> A camera's RAW file is *not an image yet* — it is the sensor's **measurement**, saved before development: one brightness reading per photosite behind the colour-filter mosaic, at 12–14 bits, before demosaicing, white balance or gamma have happened (the pixels of [[Image Encoding]] don't exist yet). But the compression choices recur unchanged: RAW files ship losslessly compressed (or in the "visually lossless" lossy variants some cameras offer), because RAW's entire purpose is **headroom for later processing** — the master-lossless rule applied one step earlier in the pipeline. Exporting a JPEG is the moment you sign the lossy deal; RAW exists so you sign it *last*, and only once.

**MP3 and AAC** exploit *masking* from [[Sound Encoding]]'s psychoacoustics: a loud sound makes nearby quieter frequencies literally inaudible for a moment, so the encoder simply doesn't pay for them. **Video codecs** add the biggest saving of all: consecutive frames are nearly identical, so they transmit mostly *differences* between frames — which is why a still shot costs almost nothing and a confetti explosion makes streams stutter.

The defining property, stated once and bluntly: **the discarded information is gone.** Decompressing a JPEG produces an approximation; re-saving it at higher quality produces a *bigger file of the same approximation*, never the original. Lossy is a one-way door.

---

## Choosing a method — the justify-it question

The A-Level's favourite question shape gives you a file and a situation and asks you to **choose and justify**. The discipline: ask *what does the recipient do with the bits?*

| File                | Right kind          | Why                                                                                                                                                                                                                                                                |
| ------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Text / program code | **Lossless only**   | Every character is load-bearing: one changed byte corrupts a word, one changed bit breaks a program ([[Text Encoding]]'s 乱码 gallery is what "lossy text" looks like). Huffman + dictionary methods; ZIP.                                                           |
| Bitmap image        | Either — by purpose | Lossless (PNG, or RLE for flat-colour art) for diagrams, screenshots, medical scans, master copies; lossy (JPEG) for photographs to share — perceptual waste is huge in photos.                                                                                    |
| Vector graphic      | **Lossless**        | A vector file is *already* a compact recipe ([[Image Encoding]] §vector) stored as text — so it compresses like text (dictionary methods; SVGZ is literally a gzipped SVG). "Lossy vector" would mean deleting shapes or rounding coordinates — rarely acceptable. |
| Sound               | Either — by purpose | Lossy (MP3/AAC) for distribution — masking makes ~90% of the bits imperceptible; lossless (FLAC) for archiving, editing, or anything that will be processed further.                                                                                               |

Two supporting rules the mark schemes reward:

1. **Master lossless, distribute lossy.** Editing a lossy file re-compresses the loss on every save — photocopying a photocopy. Studios record in lossless and export lossy at the end ([[Stories/One Take, Many Tracks]]'s modern sessions work exactly this way).
2. **Compress before encrypting, never after.** Compression hunts patterns; good encryption *erases* patterns by design, so an encrypted file will not compress ([[Encryption]] carries the other half of that story).

---

## Worked example — the exam arithmetic

> A 800 × 600 bitmap uses a colour depth of 8 bits per pixel. (a) Calculate its raw file size in MB. (b) Lossless compression reduces the file to 40% of its original size; state the compressed size. (c) Explain one situation where lossy compression of this image would be inappropriate.

**(a)** Following the [[Image Encoding]] recipe and the [[Storage Units (Vocab)]] discipline (Cambridge uses decimal units: 1 MB = 1 000 000 bytes):

$$800 \times 600 \times 8 \text{ bits} = 3\,840\,000 \text{ bits} = 480\,000 \text{ bytes} = 0.48 \text{ MB}.$$

**(b)** $0.48 \times 0.40 = 0.192$ MB — and note the phrasing trap: "reduces *to* 40%" and "reduces *by* 40%" differ; read the preposition.

**(c)** If the image is a medical scan / legal evidence / a master file for further editing — any context where detail that looks imperceptible today may matter tomorrow — the information lossy compression discards is unrecoverable, so lossless must be used.

---

## Common Misconceptions (Teaching Notes)

### 1. "A good enough algorithm could compress anything"

Impossible — not "not yet invented", but *provably* impossible, by counting (the pigeonhole proof is three lines; see §Beyond Syllabus). Compression only ever removes redundancy; data with none — random noise, encrypted data, *already-compressed files* — will not shrink, and typically grows slightly.

**Fix:** the pigeonhole proof, plus the experiment: zip a JPEG and compare sizes.

### 2. "Compressing twice shrinks it twice"

The first pass removes the redundancy; the output is (nearly) pattern-free, so a second pass has nothing to collect — misconception 1 wearing a loop.

**Fix:** same experiment, run twice.

### 3. "You can restore quality by re-saving a lossy file at a higher setting"

The one-way door. The discarded detail is not hiding in the file at lower fidelity — it is *absent*. Re-exporting an MP3 as FLAC produces a large file of the small sound.

**Fix:** the photocopy-of-a-photocopy chain; generation loss is cumulative and irreversible.

### 4. "RLE always compresses"

Only when runs exist. On run-poor data every run has length 1 and RLE *inflates* (the (1, value) pairs cost more than the values). The worked bitmap row above inflates 16 → 25 bits.

**Fix:** have students RLE a noisy row by hand and watch it grow; then a screenshot row, and watch it collapse.

### 5. "Lossy is just lossless with a stronger setting"

Different *kind*, not different strength: lossless rewrites the same information; lossy deletes information. The exam question "the file must be reproduced exactly — which type?" is testing precisely this line.

**Fix:** the two-arts framing — a promise vs a judgement call — and the four-file-type table.

---

## Exam Notes

### Cambridge 0478 IGCSE (§1.3)

- Two learning objectives: **(2)** *understand the purpose of and need for data compression* — the mark-scheme triple is **less storage space · less bandwidth required · shorter transmission time**; give the impact, not just "smaller". **(4)** *understand how files are compressed using lossy and lossless methods* — with the syllabus's own examples: lossless = **run-length encoding**; lossy = **reducing resolution or colour depth** (images), **reducing sample rate or sample resolution** (sound). Use those exact verb phrases — they are the guidance column's wording.
- RLE questions come as data: a pixel row or character string to encode (give count-value pairs), or pairs to decode, often followed by "calculate the file-size saving". Show the arithmetic in bits or bytes explicitly.
- Definition marks: lossless = "no data is permanently removed / the original can be perfectly reconstructed"; lossy = "data is **permanently** removed / the original **cannot** be reconstructed". The word *permanently* is frequently the mark.

### Cambridge 9618 A-Level (§1.3)

- Three learning objectives: the need for and examples of compression; **lossy vs lossless with a justified choice for a given situation**; and how **a text file, a bitmap image, a vector graphic and a sound file** can each be compressed — the four-file-type table above is this LO. RLE is again named in the guidance.
- The vector graphic is the distinctive 9618 item — the expected line is that a vector file is already a compact set of drawing instructions stored as text, so it is compressed *losslessly* (general-purpose/dictionary methods); contrast with the bitmap's RLE/JPEG options.
- "Justify" answers score for matching the method to the *use*: exact reproduction needed → lossless; human viewing/listening where some loss is acceptable → lossy, with the file-size benefit stated. Name a mechanism (RLE, reduced sample rate) rather than just the category.

### IB Computer Science (first assessment 2027)

- The rebuilt two-theme IB course (the old Topics 1–7 syllabus retired after its 2026 sittings) places compression under **Theme A, A2 Networks — A2.3 Data transmission**: compression as the answer to *why transmitted files are made smaller*, with the lossy-vs-lossless distinction justified in context. Expect the justify question wearing transmission clothes — streaming vs archiving, a bandwidth-limited link, an attachment size cap.
- Data representation itself (binary, hexadecimal, logic) sits in **A1.2**, so the machinery here transfers intact — and the four-file-type table answers the IB version of "choose and justify" just as it answers Cambridge's.
- The sub-topic placement follows the published course outline; check the current guide for exact command terms before drilling wording.

### Where it is *not* examined

- **AP CSA:** no compression content — the Java curriculum doesn't touch data representation at this level.
- The mathematics of the entropy floor and Huffman optimality is beyond both Cambridge boards — examined nowhere here, proven in [[Information Theory]] for the students who ask "how do we *know* we can't do better?"

---

## Connections

- **Parent:** [[Information Theory]] — entropy as the lossless floor, the source-coding theorem, Huffman's optimality: the *why-no-further* beneath everything on this page.
- **The material it compresses:** [[Text Encoding]] (skewed letter frequencies; why text must survive bit-perfect), [[Image Encoding]] (runs in flat-colour bitmaps; vectors as recipes-already-compressed; resolution and colour depth as the lossy dials), [[Sound Encoding]] (sample rate and resolution as the other lossy dials; masking as MP3's budget).
- **Arithmetic sibling:** [[Storage Units (Vocab)]] — every saving calculation runs through its MB discipline.
- **Child:** [[Encryption]] — the order-of-operations partner: compress first (patterns exist), encrypt second (patterns erased).
- **Story neighbours:** [[Stories/One Take, Many Tracks]] — master-lossless-distribute-lossy is how every modern session works.
- **Bay closer:** with this card the data-representation arc is complete — bases → binary arithmetic → text → numbers → images → sound → *and how all of them go on a diet*.

---

## Beyond Syllabus

### The pigeonhole proof — why no scheme compresses everything

Recall that a lossless compressor must be reversible, so two different files can never compress to the same output — each output string can be claimed by **at most one** input.

Watch the counting fail on a toy scale. Suppose a scheme promises to shrink **every 3-bit file**. There are $2^3 = 8$ such files: $000, 001, 010, \ldots, 111$. The only outputs allowed are the *shorter* strings:

| Output length | The strings | How many |
|---|---|---|
| 2 bits | $00,\ 01,\ 10,\ 11$ | $4$ |
| 1 bit | $0,\ 1$ | $2$ |
| 0 bits | the empty string | $1$ |

Total homes available: $4 + 2 + 1 = 7$. **Eight files, seven homes.** By the pigeonhole principle two of the files must compress to the same output — and that shared output cannot decompress back into both. The promise was impossible before any algorithm was even designed.

The same count works at every size, because the shorter strings always number one fewer than the files: for 1000-bit files there are $2^{1000}$ inputs but only $2^{999} + 2^{998} + \cdots + 2 + 1 = 2^{1000} - 1$ shorter strings (a geometric series — always exactly one home short). So no scheme shrinks every file: make some smaller, and others *must* grow. Compression works in practice because the files humans actually make — text, images, sound — are a vanishingly thin, hugely redundant slice of all possible files. Compressors are bets about *which* slice.

And if compression is prediction (below), the bound has a second reading: **no intelligence solves everything, either** — every predictor is a bet about which world it will meet. It is the same reason CPU instruction sets keep sprouting new operations decade after decade: each new opcode is a fresh bet on a pattern worth committing to silicon, and the betting never ends.

### Kolmogorov complexity — the ultimate compressed form

The shortest possible lossless description of a string is the shortest *program* that outputs it ([[Turing Machine]] machinery): "a million digits of π" is a tiny program; a million random digits admit no program shorter than themselves. This length — the string's **Kolmogorov complexity** — is the true, scheme-independent information content… and it is **uncomputable**: no algorithm can, in general, find the shortest program (the proof runs on the same self-reference engine as the halting problem). The perfect compressor not only doesn't exist — it *can't*.

### The encoder searches, the decoder obeys — why software beats silicon

A video standard like H.265 defines only the **decoder**: what a valid bitstream *means*. It says nothing about how hard an encoder must hunt for a good bitstream — so encoding is a **search problem**. The standard is a language; the encoder searches for the shortest sentence in it; and quality at a fixed bitrate is bought with *thinking time*. That is why a software encoder on a slow preset beats a GPU's hardware encoder at the same bitrate: the CPU spends seconds per frame exploring block partitions, motion vectors and rate-distortion trade-offs, while fixed-function silicon must finish every frame in real time at a few watts — the same toolbox, a drastically pruned search. The asymmetry is deliberate: **think hard once, decode cheaply everywhere** — one encoder's effort is amortised over a billion effortless playbacks. And the codec generations themselves are the same trade at a larger scale: H.264 → H.265 → AV1 each demand more search for fewer bits, a bargain that keeps improving because compute gets cheaper faster than bandwidth.

### Compression is prediction — the road to the language models

A compressor shrinks a file exactly as well as it can *predict* it: if you can guess the next symbol with confidence, you need almost no bits to confirm it ([[Information Theory]]'s low-surprise = low-cost). Run backwards, this is startling: **anything that predicts well, compresses well — and vice versa.** A large language model is, mathematically, a next-symbol predictor trained to make text as unsurprising as possible — which is why LLMs are literally state-of-the-art text compressors, and why some researchers argue that compression *is* understanding: to compress an encyclopedia superbly, you must model the world it describes. A century after fax machines counted white pixels, compression quietly became a definition of intelligence.

### The zip bomb — compression as a weapon

Decompression multiplies. `42.zip`, a famous 42-kilobyte file, unpacks through nested layers into ~4.5 **petabytes** — engineered so that a naive virus scanner that inflates everything it inspects drowns itself.

![[compression-zip-bomb-comic.png|697]]

The defence is to **never grant decompression an unlimited budget**, enforced in layers: cap the **output size** (stop at some quota regardless of what the archive claims to contain); cap the **compression ratio** (a file promising thousand-fold expansion is treated as hostile and never unpacked); cap the **nesting depth** (an archive inside an archive inside an archive trips an alarm long before 42.zip's sixteen layers); and inspect **lazily** — an archive's headers *declare* the claimed sizes, so a scanner can read the declaration and refuse without inflating a single byte. The arms race then continued: in 2019 David Fifield built a *non-recursive* bomb — 46 MB expanding to 4.5 PB in a **single layer**, by overlapping thousands of file entries onto the same compressed data — precisely to defeat scanners that only guarded against nesting. The lesson outlives zip files: **never spend resources an untrusted input asked you to spend.**

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $H(X)$ | `H(X)` | Entropy — the lossless floor (bits/symbol); full treatment in [[Information Theory]] |
| $\bar{L} \ge H(X)$ | `\bar{L} \ge H(X)` | Source-coding bound: average code length can't beat entropy |
| $(6, W)$ | `(6, W)` | RLE pair — count, value |
| $2^{1000} - 1$ | `2^{1000} - 1` | Pigeonhole count of shorter bit-strings |

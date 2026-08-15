---
chinese: 文本编码 (wénběn biānmǎ)
prerequisites:
  - "[[Number Bases]]"
  - "[[Bitwise Operations]]"
leads_to:
  - "[[Sound Encoding]]"
  - "[[Image Encoding]]"
  - "[[Compression]]"
  - "[[Credit Is the Currency]]"
tags:
  - subject/computer-science
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-1-2
  - syllabus/9618-1-1
  - type/deep
  - type/definition
  - notation/binary
  - notation/hexadecimal
  - misconception/unicode-is-an-encoding
  - misconception/character-count-equals-byte-count
---

# Text Encoding 文本编码

> *A computer stores only numbers. Text exists because we all agreed on which number means which symbol — text encoding is not physics, it is a treaty. And when two machines sign different treaties, you get 乱码.*

Send the message **`hi 你好 🚀`** and count what it costs: seven characters, **fourteen bytes**. Each `h` and `i` costs one byte. Each 汉字 costs three. The rocket costs four. Same message, three different prices — and the pricing scheme, once you see it, is one of the most elegant pieces of engineering in computing.

![[text-encoding-one-message.svg|700]]

## 中文锚点

**文本编码 (wénběn biānmǎ)** = text encoding：把字符变成数字、再把数字变成字节的**约定**。两个独立的概念，务必分开：

- **字符集 (character set)** —— 一张编号表：给每个字符分配一个数字。ASCII 给 128 个英文字符编号；**Unicode 统一码** 给全世界每个字符编号（你 = U+4F60），编号叫**码点 (code point)**。
- **编码 (encoding)** —— 把码点变成实际存储的**字节**的规则。UTF-8 是变长编码：ASCII 字符 $1$ 字节、汉字 $3$ 字节、emoji $4$ 字节。
- **乱码 (luànmǎ / mojibake)** —— 字节没错，**查错了表**：用 GBK 的表去读 UTF-8 的字节（或反过来），就得到"锟斤拷"。
- 常见误区：**"Unicode 是一种编码"** ——不是。Unicode 只负责*编号*；UTF-8 / UTF-16 / UTF-32 才是把编号变成字节的*编码*。

---

## The idea — text is a treaty, not a signal

Sound and images are *continuous* physical things — to store them, a computer must measure and approximate ([[Sound Encoding]], [[Image Encoding]]). Text is different: it is **already discrete**. There are finitely many symbols, so nothing needs measuring — all that's needed is an *agreement* about which number stands for which symbol.

That agreement has two independent layers, and keeping them separate is the whole game:

1. A **character set** assigns each character a number. It is a numbered list — nothing more.
2. An **encoding** turns those numbers into actual stored **bytes**.

For ASCII the two layers coincide (one small number, one byte), which is exactly why everyone conflates them. For Unicode they split apart — one character set, several competing encodings — and the split is where all the interesting engineering (and all the 乱码) lives.

---

## ASCII — the 128-character treaty (1963)

**ASCII** (American Standard Code for Information Interchange) uses **7 bits**: $2^7 = 128$ slots, numbered 0–127. It was designed for teletype machines, and the design is *full* of deliberate tricks — the layout is not alphabetical accident but engineered structure:

![[text-encoding-ascii-map.svg|700]]

- **0–31 are control characters** — not symbols but *instructions to the machine*, straight from the teletype era: `10` = line feed `\n` (move the paper up one line), `9` = tab, `13` = carriage return `\r` (slide the print head back), and `7` = **BEL**, which physically rang a bell on the receiving teletype. Text files still carry these ghosts of 1963 machinery.
- **Digits `'0'`–`'9'` sit at 48–57** ($30_{16}$–$39_{16}$). So for any digit character, `character − 48 = its value` — converting `'7'` to $7$ is one subtraction. The bottom four bits of a digit's code *are* the digit ($0111$ for `'7'`) — BCD hiding inside ASCII.
- **`'A'`–`'Z'` at 65–90, `'a'`–`'z'` at 97–122.** The gap between a letter's two cases is exactly $97 - 65 = 32 = 2^5$: **uppercase and lowercase differ in a single bit (bit 5)**. `A` = $0100\,0001$, `a` = $0110\,0001$. Case conversion is one bit-flip, case-insensitive comparison is one masked compare — the [[Bitwise Operations]] toolkit applied to text, by design.
- **Alphabetical order = numerical order.** Sorting text *is* sorting numbers; no lookup needed.

**Worked example — encode `Hi!`:** `H` = 72 = $48_{16}$, `i` = 105 = $69_{16}$, `!` = 33 = $21_{16}$. Three characters, three bytes: `48 69 21`. (Byte ↔ two hex digits, as always — [[Number Bases]].)

**Character algebra.** Because the blocks are contiguous and in order, characters support *arithmetic* — you can compute with letters as if they were numbers, because underneath they are:

- `'b' − 'a' = 1` — neighbouring letters differ by exactly one;
- `c − '0'` — a digit character's **value**;
- `c − 'a'` — a letter's **alphabet index** (0–25);
- `c ± 32` (or flip bit 5) — the **other case**.

The classic payoff is the **Caesar shift**: rotate any letter by $k$ places with $(c - \texttt{'A'} + k) \bmod 26 + \texttt{'A'}$ — convert to alphabet index, walk $k$ steps around the circle ([[Modular Arithmetic]]), convert back. Every string algorithm you will ever write — searching, sorting, hashing, parsing — leans on character algebra somewhere. Text does maths **because the treaty was engineered to make it so.**

> [!tip] Why 7 bits, when a byte has 8?
> In 1963 the 8th bit was spent on *parity* — a simple transmission-error check. When parity moved elsewhere, the spare bit meant every ASCII byte had a free slot on top: values 128–255, unassigned. That spare half-byte is where the trouble started.

---

## The Babel era — extended ASCII and the code pages

128 slots hold English. They do not hold é, ñ, ß, Ω, я — let alone 汉字. The spare values 128–255 (**extended ASCII**) gave every region 128 extra slots, and every region filled them *differently*: Western Europe's Latin-1 put é at 233; Greek, Cyrillic, Hebrew each had their own **code page**; and Chinese needed thousands of characters, so **GB2312** (1980, 6,763 汉字) and its successor **GBK** used *pairs* of high bytes — two bytes per 汉字.

The fatal flaw: **a file of bytes does not say which table wrote it.** The byte 233 *is* é in Latin-1, *is* half a 汉字 in GBK, *is* the start of a three-byte sequence in UTF-8. Decode with the wrong treaty and every byte still "means" something — just the wrong thing. That is **乱码 (mojibake)**: not damaged data, but a correct file read through the wrong glasses.

> [!info] Why is there a GBK at all? — the 国标 story
> Because China needed computing in Chinese **eleven years before Unicode existed.** GB2312 (1980 — GB = **国标**, *national standard*) numbered 6,763 simplified 汉字: enough for a newspaper, not for the country — rare name-characters, traditional forms, and classical texts were simply unwritable, so some people could not type their own names. **GBK** (1995, K = **扩展**, *extension*) grew the table to about 21,000 characters — traditional forms included — while staying byte-compatible with every existing GB2312 file. Every neighbour did the same in the pre-Unicode years: Japan built Shift-JIS, Taiwan built Big5, Korea built EUC-KR. So why hasn't Unicode simply retired them? **Backward compatibility is forever**: decades of documents, databases and software speak GBK, and Windows' Simplified-Chinese locale defaulted to it for years. The modern answer, **GB18030** (2000) — a *mandatory* national standard that software sold in China must support — squares the circle by being GBK-backward-compatible *and* able to represent every Unicode code point. The treaties have converged; the old bytes remain.

---

## Unicode — one number for every character

The fix had to be a single treaty covering everything: **Unicode** (1991) assigns every character humanity uses a unique number called a **code point**, written `U+` followed by hex:

$$\texttt{A} = \text{U+0041} \qquad 你 = \text{U+4F60} \qquad 🚀 = \text{U+1F680}$$

The space runs to U+10FFFF — 1,114,112 slots, of which about 155,000 are assigned so far: every living script, historical scripts (cuneiform, hieroglyphs), mathematical symbols — and emoji.

> [!info] Since when does Unicode contain emoji?
> **October 2010, Unicode 6.0** — and the reason is this page's story repeating itself. Emoji were invented in 1999 by **Shigetaka Kurita** for the Japanese carrier NTT DoCoMo: 176 tiny 12×12-pixel pictographs for pagers and phones. The rival carriers cloned the idea with **incompatible private encodings** — a heart sent from one Japanese phone arrived on another as a wrong symbol, or as garbage. Sound familiar? It was the code-page Babel in miniature. When Gmail and the iPhone had to interoperate with Japanese phones, Google and Apple petitioned the Unicode Consortium, and the 2010 release absorbed emoji into the universal treaty. That is why 🚀 has a code point (U+1F680) exactly like 你 does — and why a rocket sent from Chengdu arrives intact on any phone on Earth.

**But Unicode is only the numbered list — the character set.** It deliberately says nothing about bytes. Turning code points into bytes is the encoding's job, and there are three: UTF-32 (every character = 4 bytes — simple, wasteful), UTF-16 (2 or 4 bytes — the compromise Java and Windows got frozen into), and the one that won the world:

---

## UTF-8 — the encoding that won

**UTF-8** (over 98% of the web) is a **variable-length** encoding: 1 to 4 bytes per character, decided by the code point's size. The scheme is a prefix code:

![[text-encoding-utf8-patterns.svg|697]]

| Code point range | Bytes | Pattern |
|---|---|---|
| U+0000 – U+007F | 1 | `0xxxxxxx` |
| U+0080 – U+07FF | 2 | `110xxxxx 10xxxxxx` |
| U+0800 – U+FFFF | 3 | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10000 – U+10FFFF | 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

The leading bits of the first byte announce the length; every continuation byte starts `10`; the `x`s carry the code point's bits.

**Worked encode — 你 (U+4F60).** The code point in binary: $4F60_{16} = 0100\,1111\,0110\,0000$ — sixteen bits, so it needs the 3-byte pattern. Pour the bits into the `x` slots, left to right:

$$\underbrace{1110\,\mathbf{0100}}_{E4}\;\;\underbrace{10\,\mathbf{111101}}_{BD}\;\;\underbrace{10\,\mathbf{100000}}_{A0}$$

你 = `E4 BD A0`. Three bytes — the "three-byte price" of every 汉字 in the opening message. (And 🚀 at U+1F680 needs 17 bits, hence the 4-byte pattern: `F0 9F 9A 80`.)

**The real-life algorithm — no table, just bit surgery.** The "pour" is not a metaphor; it is three lines of [[Bitwise Operations]], and this is essentially what every encoder on Earth executes. For a 3-byte code point `cp` (here `0x4F60`):

```
byte1 = 0xE0 | (cp >> 12)            top 4 bits:     0xE0 | 0x04 = 0xE4
byte2 = 0x80 | ((cp >> 6) & 0x3F)    middle 6 bits:  0x80 | 0x3D = 0xBD
byte3 = 0x80 | (cp & 0x3F)           bottom 6 bits:  0x80 | 0x20 = 0xA0
```

**Shift** to slide the wanted field to the bottom, **AND** with `0x3F` to mask it clean, **OR** to staple the prefix on top — a handful of CPU instructions per character, and decoding is the same surgery in reverse (mask the prefixes off, shift the payloads back together). Production libraries go further still, using vector (SIMD) instructions to validate and convert dozens of bytes per clock cycle — but the core is exactly these three lines. The masking toolkit, earning its keep.

**Why this design conquered the world** — four properties, each deliberate:

1. **Every ASCII file is already valid UTF-8.** One-byte characters use the pattern `0xxxxxxx` — which *is* ASCII, bit for bit. Decades of existing English text needed no conversion. This single property is most of why UTF-8 won.
2. **Self-synchronising.** A first byte and a continuation byte can never be confused (`0…`/`110…`/`1110…`/`11110…` vs `10…`). Jump into the middle of a file and you can always find the next character boundary within 3 bytes — a corrupted byte damages one character, not the rest of the file.
3. **No fake ASCII.** A multi-byte character contains no bytes below 128, so a `/` or `"` can never appear by accident inside a 汉字's bytes — old ASCII-assuming software stays safe.
4. **Frequency-matched cost.** The most common characters of computing (ASCII) cost 1 byte; rarer ones cost more — the same "common = short" instinct that powers [[Compression]].

> [!info] Designed on a placemat
> UTF-8 was sketched in September 1992 by **Ken Thompson** and **Rob Pike** — reportedly on a diner placemat in New Jersey, in one evening, after a proposal they disliked crossed their desks. Thompson had already co-created Unix; fifteen years later the same two men would be two of the three creators of the **Go programming language** — which is why Go handles text as UTF-8 to the bone, no conversion layer, by birthright. Some treaties take decades of committee; this one took dinner.

---

## The 乱码 gallery — reading the corpses

Wrong-treaty decoding produces *recognisable species* of garbage. Each one is a forensic clue — you can read back what went wrong:

- **`café` → `cafÃ©`** — UTF-8 read as Latin-1. The é is `C3 A9` in UTF-8; Latin-1 reads those as two separate characters, `Ã` and `©`. Every accented letter doubles into `Ã`-something: the signature of *UTF-8 bytes, Latin-1 glasses*.
- **锟斤拷 (kūn jīn kǎo)** — the most famous Chinese mojibake, and a *two-stage* accident. Stage 1: some text fails to decode, and the system replaces each bad character with Unicode's official replacement character � (U+FFFD, UTF-8 `EF BF BD`). Stage 2: that repaired UTF-8 is then read as GBK, which groups bytes in *pairs*: `EF BF · BD EF · BF BD` → 锟 · 斤 · 拷. Two replacement characters, misread, spell three nonsense 汉字 — corruption *of* corruption.
- **烫烫烫 (tàng tàng tàng)** — not an encoding error at all! Microsoft's C++ compiler fills *uninitialised stack memory* with the debug byte `CC`. Print that memory as GBK text and `CC CC` = 烫. A console screaming 烫烫烫 ("scalding!") means: you printed a variable you never assigned. (Uninitialised *heap* is filled `CD` — `CD CD` = 屯, so 屯屯屯 tells you which mistake you made.)

![[text-encoding-tang-comic.png|697]]

*(The robot's reply is the byte `0x3F` — decode it yourself with the ASCII skills above.)*

The lesson under the fun: **bytes carry no label saying which treaty wrote them.** Every file format and web page therefore *declares* its encoding (`charset=utf-8`) — and when the declaration is missing or wrong, the gallery above is what fills your screen.

---

## Worked examples

**Example 1 — decode ASCII.** The bytes `43 6F 64 65` (hex): $43_{16}=67=$ `C`, $6F_{16}=111=$ `o`, $64_{16}=100=$ `d`, $65_{16}=101=$ `e` → **`Code`**.

**Example 2 — the exam classic: why does Unicode need more bits per character than ASCII?** ASCII's 7 bits give $2^7 = 128$ slots — enough for English letters, digits and punctuation only. Unicode must number *every* character in *every* writing system (about 155,000 assigned, space for 1,114,112), and $2^7 \ll 155{,}000$: more characters force more bits ($2^{21}$ covers the full range). The cost: more storage per character; the gain: any language, one treaty, no code pages.

**Example 3 — byte count.** How many bytes is `Go向前🚀` in UTF-8? `G`, `o` = 1 each; 向, 前 = 3 each (CJK, U+0800–U+FFFF band); 🚀 = 4 (above U+FFFF). Total $1+1+3+3+4 = \mathbf{12}$ bytes for 5 characters. *Character count ≠ byte count* — the classic trap.

**Example 4 — the bit-5 trick.** Convert `'q'` (113) to uppercase without a lookup table: clear bit 5. $113 = 0111\,0001_2$; clearing bit 5 gives $0101\,0001_2 = 81 =$ `'Q'`. One `AND` with mask $1101\,1111_2$ — this is why ASCII put the cases exactly 32 apart.

---

## Exam Notes

### Cambridge 0478 (IGCSE) — **Paper 1**

**§1.2.1 — text representation.** Expect to: explain what a **character set** is (the complete collection of characters a system can represent, each with a unique binary code); describe **ASCII** (7-bit, 128 characters, English-only) and **Unicode** (a superset covering all languages and emoji); and answer the standard comparison — *why does Unicode require more bits per character, and what does that cost/gain?* (More characters need more bits; costs storage, gains every language.) You will **not** be asked to memorise specific codes.

### Cambridge 9618 (A-Level) — **Paper 1** (AS)

**§1.1** includes character representation: internal binary form of character data "depending on the character set used," with **ASCII, extended ASCII and Unicode** named explicitly. Expect conversions in context (given a partial ASCII table, encode/decode a short string) and set-vs-set comparisons as in 0478, at more depth: extended ASCII's 8th bit and its incompatible variants are fair game. Again: no memorising code values.

**Common mark-losers:** saying "Unicode is 16-bit" (it is a character *set* with code points up to U+10FFFF; the *encodings* vary in width — and even UTF-16 is variable-length); claiming ASCII "uses 1 byte" without noting only 7 bits carry data; treating character count and byte count as equal in a UTF-8 size calculation; calling Unicode "an encoding" (Unicode assigns numbers; UTF-8/16/32 produce bytes).

### IB CS (2027)

Text encoding is **not a named statement**: A1.2's published representation wording stops at binary/hexadecimal conversion and logic gates processing encoded data — character sets, ASCII and Unicode are not listed. Treat this card as the depth behind "encoded data" rather than examinable IB content.

### Where this is *not* examined

**AP Computer Science A** has `char` and `String` in its subset but does not examine character *sets* — ASCII, Unicode, encodings and their widths are all outside it, and there is no file I/O in which an encoding could go wrong. Beyond every board: UTF-8's self-synchronising design, byte-order marks, normalisation forms, and the 乱码 diagnosis gallery are here because they explain the examined facts, not because they are examined.

---

## Connections

- **Prerequisite:** [[Number Bases]] — every encoding table is read in hex; byte ↔ two hex digits is the working skill throughout.
- **Prerequisite:** [[Bitwise Operations]] — ASCII's engineered layout (bit-5 case flip, digit low-nibble) exists *so that* masking tricks work on text.
- **Siblings:** [[Sound Encoding]] and [[Image Encoding]] — the continuous signals, where representation means *measurement* (sampling) rather than *convention*. Text is the odd one out: already discrete, so purely a treaty.
- **Sequel:** [[Compression]] — UTF-8's "common characters cost fewer bytes" is variable-length coding by hand; Huffman coding turns the same idea into an algorithm.
- **Cross-domain:** [[Information Theory]] — "how many bits does a symbol *really* need?" is entropy's founding question, and English text's answer (≈1 bit per letter, not 7) is why text compresses so well.

---

## Notation Reference

| Notation | Meaning |
|---|---|
| `U+4F60` | a Unicode **code point** — the character's number, in hex (你 = 20,320) |
| `E4 BD A0` | bytes in hex — 你's UTF-8 encoding (3 bytes) |
| `0xxxxxxx` | a byte pattern: fixed prefix bits + `x` payload slots |
| $2^7 = 128$ | ASCII's capacity — 7 bits of code space |
| � (U+FFFD) | the replacement character — Unicode's official "a character died here" |

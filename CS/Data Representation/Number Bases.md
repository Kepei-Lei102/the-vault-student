---
chinese: 进制 (jìnzhì)
prerequisites:
  - "[[Logic Gates]]"
leads_to:
  - "[[Two's Complement]]"
  - "[[Half-Adder and Full-Adder]]"
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Floating-Point Representation]]"
  - "[[Text Encoding]]"
  - "[[Storage Units (Vocab)]]"
  - "[[Image Encoding]]"
  - "[[Sound Encoding]]"
  - "[[Assembly Language]]"
  - "[[Bitwise Operations]]"
  - "[[Gray Code]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/IB-CS-A1-2
  - syllabus/0478-1-1
  - syllabus/9618-1-1
  - type/deep
  - type/definition
  - notation/binary
  - notation/hexadecimal
  - misconception/binary-is-a-different-number
  - misconception/leading-zeros-change-value
  - misconception/hex-is-its-own-number-system
  - misconception/base-subscript-dropped
---

# Number Bases — Binary and Hexadecimal 进制

## Definition

A **number base** (or *radix*) is the size of the "alphabet of digits" a counting system uses, and the number whose powers give each column its weight. We grow up in **denary** (base 10, digits 0–9). Computers run on **binary** (base 2, digits 0 and 1), and programmers read binary through **hexadecimal** (base 16, digits 0–9 then A–F).

The crucial thing to hold onto from the start: **changing base does not change the number.** Eleven sheep are eleven sheep whether you write them `11` (denary), `1011` (binary), or `B` (hex). A base is a *notation* — a way of spelling a quantity — not a different quantity. Every base works by the *same* rule, **place value**, just with a different column weight.

Computers use base 2 for one physical reason: a circuit element is reliably either **off or on** (low or high voltage) — two states, cleanly distinguishable, exactly the [[Logic Gates|gates]] that make up every chip. There is no cheap, reliable "ten-state" wire, so hardware counts in two. Hex exists because raw binary is exhausting for humans to read, and base 16 packs neatly into binary (one hex digit = four bits).

### 中文锚点

**进制**（jìnzhì, number base / radix）：一个计数系统用多少个数字符号，以及每一位的「权重」是哪个数的幂。

- **十进制**（shí jìnzhì, denary, base 10）：人类日常用，数字 0–9。
- **二进制**（èr jìnzhì, binary, base 2）：计算机用，只有 0 和 1。原因很物理 —— 电路只有**关/开**（低/高电压）两个稳定状态，正是 [[Logic Gates|逻辑门]]。没有便宜可靠的「十种状态」的元件，所以硬件用二进制。
- **十六进制**（shíliù jìnzhì, hexadecimal, base 16）：程序员用来**读**二进制，数字 0–9 再加 A–F。一个十六进制位 = 四个二进制位（一个 **nibble** 半字节），所以一字节（8 位）= 两个十六进制位。

最关键的一句：**换进制不改变数本身。** 11（十进制）、1011（二进制）、B（十六进制）是同一个数的三种写法。所有进制都用同一条规则——**位值**（place value）——只是每位的权重不同。

## Place value — the one idea behind every base

In any base $b$, a string of digits is shorthand for a sum of **digit × power of $b$**. The rightmost column is $b^0 = 1$, the next is $b^1$, then $b^2$, and so on. Denary `214` means

$$2\times10^2 + 1\times10^1 + 4\times10^0 = 200 + 10 + 4.$$

Binary is the identical idea with $b=2$, so the column weights are the powers of two — $1, 2, 4, 8, 16, 32, 64, 128, \dots$ — and the only digits are 0 and 1 (each column is simply *present* or *absent*):

$$1101\,0110_2 = 128 + 64 + 16 + 4 + 2 = 214.$$

That's the whole engine. Learn the powers of two up to 256 by heart (they're the binary "times table") and conversions become reading off a checklist.

![[number-bases-byte.svg|697]]
*One byte, three ways. Each of the 8 bits is worth a power of two (top row); add the columns where the bit is 1 to get the denary value (214). Split the byte into two 4-bit **nibbles** and each becomes a single hex digit — `1101` = D, `0110` = 6 — so the same byte is `0xD6`. Binary for the machine, hex for the human, denary for everyday life; one quantity throughout.*

## Binary (base 2)

A single binary digit is a **bit**. Eight bits make a **byte**; four bits (half a byte) is a **nibble**. An 8-bit byte holds $2^8 = 256$ different patterns, i.e. the values 0–255.

**Binary → denary.** Add the place values where the bit is 1. For `1001101`:
$$1001101_2 = 64 + 8 + 4 + 1 = 77.$$

**Denary → binary, method 1 (subtract powers).** Take the largest power of two that fits, subtract, repeat. For 77: $64$ fits (remainder 13), $8$ fits (rem 5), $4$ fits (rem 1), $1$ fits (rem 0) → columns 64, 8, 4, 1 are on → `1001101`.

**Denary → binary, method 2 (repeated division by 2).** Divide by 2, write the remainder, repeat with the quotient; read the remainders **bottom-up**:

| ÷2 | quotient | remainder |
|---|---|---|
| 77 | 38 | **1** |
| 38 | 19 | **0** |
| 19 | 9 | **1** |
| 9 | 4 | **1** |
| 4 | 2 | **0** |
| 2 | 1 | **0** |
| 1 | 0 | **1** |

Reading the remainders from bottom to top: `1001101` — the same answer. (Method 2 is the one that generalises to *any* base: repeatedly divide by the base, read the remainders backwards.)

Written as a full byte, 77 is `0100 1101` — the **leading zero** pads it to 8 bits but changes nothing, exactly as `077` is still 77 in denary.

## Hexadecimal (base 16)

Base 16 needs sixteen digits, so after 0–9 it borrows letters: A = 10, B = 11, C = 12, D = 13, E = 14, F = 15. Column weights are powers of 16: $1, 16, 256, \dots$

The reason hex earns its place is its exact fit with binary: **$16 = 2^4$, so one hex digit is precisely one nibble (4 bits), and one byte is precisely two hex digits.** That makes binary↔hex conversion a no-arithmetic operation — you just chunk the bits into fours.

**Binary → hex.** Group the bits into nibbles from the right and translate each:
$$\underbrace{1101}_{\text{D}}\ \underbrace{0110}_{6} \;=\; \text{0xD6}.$$

**Hex → binary.** Expand each hex digit to its 4-bit pattern: `0x2F` → `0010 1111`.

**Hex → denary.** Weight by powers of 16: `0xD6` $= 13\times16 + 6 = 208 + 6 = 214$.

**Denary → hex.** Repeated division by 16: $214 = 13\times16 + 6$ → digit 6, then 13 = D → `0xD6`.

A note on **notation**: the same digits mean different values in different bases, so the base must be made clear. Conventions you'll meet: a subscript (`1101_2`, `D6_{16}`), a `0x` prefix for hex (`0xD6`), `0b` for binary (`0b11010110`), or a trailing letter. Dropping the marker is how `10` ends up ambiguous — it's *two* in binary, *ten* in denary, *sixteen* in hex.

## Why these bases?

- **Why binary for the hardware?** Two states is the *fewest* a system can have and still carry information, and "fewest" buys reliability: a wire that only has to be clearly-low or clearly-high tolerates noise and voltage drift that would scramble a ten-level signal. The transistor is a switch; the [[Logic Gates|gate]] is built from switches; the whole machine is therefore native to base 2. (The bit as the unit of information is the subject of [[Information Theory]].)
- **Why hex for the humans?** `11010110` is error-prone to read, copy, or dictate; `D6` is two characters and maps back to the bits with zero calculation. Hex is *compression for eyeballs* — a faithful, reversible shorthand for binary that respects the nibble/byte boundary. You'll see it everywhere bytes are shown raw: colours (`#FF8800`), memory addresses, MAC addresses, hash digests, error codes.
- **Why not denary in the hardware?** Because ten isn't a power of two, denary digits don't align to bits, and no cheap component reliably holds ten distinct states. (Early machines *did* try denary — see Beyond Syllabus — and it lost.)

## Worked examples

**1 — Read a byte three ways.** `1101 0110₂`: place values present are 128, 64, 16, 4, 2 → $128+64+16+4+2 = 214$ in denary; nibbles `1101`=D, `0110`=6 → `0xD6`. One byte, three spellings of 214.

**2 — Pack a colour.** The CSS colour `#2563EB` is three bytes (red, green, blue). The first byte — **red** — is `0x25` = $2\times16+5 = 37$; as binary `0010 0101`. So "37/255 red" and `0x25` and `00100101` are the same channel value. (Pulling a chosen channel out of the packed number is a job for [[Bitwise Operations]].)

**3 — Convert 200 to binary and hex.** Subtract powers: $128$ (rem 72), $64$ (rem 8), $8$ (rem 0) → columns 128, 64, 8 → `1100 1000`. Nibbles `1100`=C, `1000`=8 → `0xC8`. Check: $12\times16+8 = 200$. ✓

## Common Misconceptions (Teaching Notes)

### 1. "Binary numbers are different from 'real' numbers"

`1011` and `11` are the *same quantity* in two notations, like "eleven" and "XI." Conversion doesn't transform the number; it re-spells it. Students who internalise "it's the same value, different columns" stop fearing binary.

**Fix.** Always convert back and check you land on the original value.

### 2. "Leading zeros change the value / you can drop trailing structure"

`0100 1101` and `1001101` are equal — leading zeros only set the *width* (how many bits the field is, e.g. 8 for a byte). Width matters for storage and for [[Two's Complement|two's complement]], but not for the value.

**Fix.** Pad to the stated width (8-bit, 16-bit) for the format, but know the value is unchanged.

### 3. "Hex is a whole separate number system you also have to learn"

Hex is *just grouped binary*. You never really do hex arithmetic in your head — you chunk bits into fours. Once you see `16 = 2⁴`, hex stops being a third thing to memorise and becomes a lens on binary.

**Fix.** Learn the 16 nibble↔hex patterns once; after that, hex is pattern-matching, not calculation.

### 4. "`10` means ten"

Only in denary. `10` is two in binary, sixteen in hex. Whenever a base isn't obvious from context, the notation must say which — subscript, `0x`/`0b`, or words.

**Fix.** Write the base marker; read it before you trust a digit string.

## Exam Notes

### Cambridge 0478 (IGCSE CS)

**§1.1.1–1.1.2** — binary as the universal representation; convert between **denary, binary, and hex** in any direction (up to 16-bit); and explain the **use of hex** in CS (readability, colour codes, addresses, error codes). Those rows close here. Binary **addition, overflow, logical shifts** (§1.1.4–5) and **two's complement** for signed integers (§1.1.6) live in [[Two's Complement]] and [[Overflow and Underflow]].

### Cambridge 9618 (A-Level CS)

**§1.1 Data Representation** bundles binary/denary/hex + conversions (closed here) with binary addition + overflow ([[Overflow and Underflow]]), signed binary ([[Two's Complement]]), and **BCD** ([[Floating-Point Representation]]). The advanced §13.3 (floating-point) builds on all of it.

### IB Computer Science — A1.2

**Binary/hexadecimal and conversion is a named A1.2 statement** — the same skill set as 0478: convert denary ↔ binary ↔ hex in every direction, and say *why* each base exists (two reliable physical states → binary; one hex digit = one nibble → hex as compression for eyeballs). IB pairs it in A1.2 with logic gates "processing encoded data," so expect conversions embedded in a small scenario rather than asked bare.

*(AP CSA is a programming course and doesn't test number-base conversion directly — but bitwise/`int` behaviour rests on exactly this, so it's worth knowing.)*

## Connections

- **Prerequisite:** [[Logic Gates]] — the two physical states (off/on) that make base 2 the natural language of hardware; number bases are "what those 0s and 1s spell."
- **Sibling unit:** [[Information Theory]] — the **bit** as the *unit of information* (Shannon), the quantitative companion to the bit as a *digit* here.
- **Next:** [[Two's Complement]] — how those bits represent **negative** integers, plus binary addition, overflow, and shifts; then text/sound/image encoding and compression fill out the Data Representation bay.
- **History:** [[Stories/The Boolean-to-Silicon Bridge]] — how two-state logic became the substrate of every computer.

---

## Beyond Syllabus

### Other bases worth meeting

**Octal** (base 8, three bits per digit) was big in the era of 12- and 36-bit machines and still survives in Unix file permissions (`chmod 755`). **Base 64** packs three bytes into four printable characters and is how binary rides through text-only channels (email attachments, data URLs). **Babylonian base 60** is why we still have 60 seconds, 60 minutes, and 360°; **base 12** (duodecimal) has fans because 12 has more divisors than 10. The choice of 10 itself is pure anatomy — ten fingers — not mathematics, which is the same "anthropocentric vs natural" point [[Stories/The Hidden Number]] makes about base-10 logarithms.

### Decimal computers really were tried

The earliest electronic computer, **ENIAC (1945)**, counted in *decimal*, using ten-position ring counters — and it was a tangle of tubes for it. **Binary-coded decimal (BCD)**, which stores each decimal digit in its own nibble, survives in places where exact decimal matters (financial systems, the displays in some calculators) precisely because it dodges the rounding of binary fractions. But for general computation, binary's hardware simplicity won decisively.

### The most efficient base

If you measure a base by "radix economy" — roughly, digits needed × distinct symbols per digit — the theoretical optimum is base $e \approx 2.718$, and among integers **base 3** beats base 2. A few experimental machines (the Soviet **Setun**, 1958) used *balanced ternary* ($-1, 0, +1$) and it's genuinely elegant — negation is free, rounding is trivial. Binary still won, because two-state components are so much cheaper and more reliable to build than three-state ones. Engineering beat numerology, the same way it did in [[Sorting|quicksort vs the "optimal" sorts]].

## Notation Reference

| Symbol | Meaning |
|--------|---------|
| $b$ | the **base** / radix — column weights are powers of $b$ |
| $1011_2$ | subscript marks the base (here, binary) |
| `0x` / `0b` | prefixes for hexadecimal / binary (e.g. `0xD6`, `0b1011`) |
| bit | a single binary digit (0 or 1) |
| nibble | 4 bits = one hex digit |
| byte | 8 bits = two hex digits = values 0–255 |
| A–F | the hex digits for 10–15 |

---
chinese: 位运算 (wèi yùnsuàn)
prerequisites:
  - "[[Logic Gates]]"
  - "[[Number Bases]]"
  - "[[Two's Complement]]"
leads_to:
  - "[[Gray Code]]"
  - "[[Text Encoding]]"
  - "[[Assembly Language]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-1-1
  - syllabus/9618-4-3
  - type/deep
  - type/definition
  - notation/binary
  - misconception/bitwise-vs-logical-operators
  - misconception/right-shift-is-always-divide
  - misconception/shifting-is-just-multiplication
  - misconception/xor-is-rare
---

# Bitwise Operations 位运算

## Definition

**Bitwise operations** act on a number **one bit at a time**, treating it not as a quantity but as a *row of switches*. They come in two families:

1. **The logic operators** — `AND`, `OR`, `XOR`, `NOT` — which are exactly the [[Logic Gates|gates]] you already know, applied to **every bit position in parallel**. Where a gate took one or two bits, the bitwise version runs eight (or 32, or 64) gates side by side, one per column.
2. **The shifts** — `<<` and `>>` — which **slide** all the bits left or right.

Why bother operating below the level of "the number"? Because a single integer is also **eight (or more) independent booleans**, and bitwise operations are how you read and write them individually: pack a fistful of yes/no flags into one byte, switch one on without disturbing the others, pull a colour channel out of a packed pixel, or multiply by 8 in a single clock cycle. It is the toolkit for treating data *as bits*.

### 中文锚点

**位运算**（wèi yùnsuàn, bitwise operations）：把一个数当成**一排开关**，**逐位**操作。两大类：

1. **逻辑运算** `AND / OR / XOR / NOT` —— 就是 [[Logic Gates|逻辑门]]，只不过**对每一位并行**地做（8 位就是 8 个门并排）。
2. **移位** `<<` `>>` —— 把所有位整体**左移 / 右移**。

为什么要操作「位」而不是「数」？因为一个整数也是**八个（或更多）独立的布尔值**：用位运算可以把一堆开关塞进一个字节、单独打开某一位而不动其他位、从打包的像素里取出某个颜色通道、或者一个时钟周期内乘以 8。

- **掩码** mask：set 用 `OR`，clear 用 `AND ~mask`，toggle 用 `XOR`，test 用 `AND`。
- **逻辑右移**补 0；**算术右移**补符号位（处理负数除以 2）。

## The four logic operators, bit by bit

Each operator applies its truth table to matching bit positions of the two operands:

```
  AND (&)      OR (|)       XOR (^)       NOT (~)
  1011         1011         1011          ~1011
& 0110       | 0110       ^ 0110         = 0100
------       ------       ------
  0010         1111         1101
```

- **AND** gives 1 only where *both* are 1 — it's a **filter** ("keep only these bits").
- **OR** gives 1 where *either* is 1 — it **forces bits on**.
- **XOR** gives 1 where the bits *differ* — it **flips / compares**.
- **NOT** inverts every bit (and, as [[Two's Complement]] showed, `~x` is one short of $-x$).

> [!warning] Bitwise `&` is not logical `&&`
> `&`, `|` work on *all the bits* of their operands; `&&`, `||` (and Python's `and`, `or`) collapse each operand to a single true/false and combine those. `5 & 2` is `0` (no shared bits); `5 && 2` is `true` (both are non-zero). Mixing them up is a classic bug.

## Masking — the killer application

A **mask** is a constant you design so its 1-bits mark exactly the positions you want to touch. Four moves cover almost everything, and each is one operator:

**Test** whether a bit is set — `AND` with a mask, check if the result is non-zero:
```
  1011 0010   value
& 0001 0000   mask = bit 4
-----------
  0001 0000   ≠ 0  → bit 4 is SET
```

**Set** a bit (force it to 1) — `OR` with the mask:
```
  1011 0010   value
| 0000 1000   mask = bit 3
-----------
  1011 1010   bit 3 now 1, the rest untouched
```

**Clear** a bit (force it to 0) — `AND` with the *inverted* mask (`~mask`):
```
  1011 0010   value
& 1111 1101   ~mask  (mask was bit 1 = 0000 0010)
-----------
  1011 0000   bit 1 now 0, the rest untouched
```

**Toggle** a bit (flip it) — `XOR` with the mask:
```
  1011 0010   value
^ 0000 0110   mask = bits 1 and 2
-----------
  1011 0100   bits 1 and 2 flipped
```

The magic is "the rest untouched": OR-ing with 0 leaves a bit alone, AND-ing with 1 leaves it alone, XOR-ing with 0 leaves it alone. So a well-chosen mask is a scalpel — it edits the bits you name and *only* those.

## Shifts — sliding the bits

A **left shift** `x << k` moves every bit $k$ places toward the high end, filling the vacated low bits with 0 — which **multiplies by $2^k$** (each bit lands in a column worth $2^k$ as much). A **right shift** `x >> k` slides the other way, dropping the low bits — **integer division by $2^k$**.

```
  0000 0101  (5)  << 1  =  0000 1010  (10)     ×2
  0001 0100  (20) >> 2  =  0000 0101  (5)      ÷4
```

This is why compilers quietly turn `x * 8` into `x << 3`: a shift is one of the cheapest things a CPU can do, far faster than a general multiply. (Bits pushed off the end are simply lost — a left shift is also a way to [[Overflow and Underflow|overflow]].)

## Logical vs arithmetic shifts — the sign-bit trap

Left shifts are unambiguous. **Right** shifts are not, and this is the distinction that bites people:

- A **logical** right shift always feeds a **0** into the top. Perfect for unsigned values.
- An **arithmetic** right shift feeds a **copy of the sign bit** into the top — the [[Two's Complement|sign-extension]] idea — so a negative number stays negative.

On an unsigned value they agree. On a *signed negative* value they wildly disagree:

![[bitwise-shift-arithmetic-vs-logical.svg|697]]
*Right-shifting −8 (`1111 1000`) by one. A **logical** shift pulls a 0 into the top bit, giving `0111 1100` = +124 — the sign was destroyed, the answer is garbage. An **arithmetic** shift copies the sign bit (1) back in, giving `1111 1100` = −4 — a correct halving. The only difference is the single bit shifted *into* the top; that one bit is the whole distinction.*

> [!info] Arithmetic shift is *not* the same as ÷ for negatives
> Arithmetic right shift rounds **toward −∞** (it floors), while integer division in most languages rounds **toward zero** (it truncates). So `−7 >> 1` is `−4` (`1111 1001 → 1111 1100`), but `−7 / 2` is `−3`. They match for non-negative numbers and differ by one for negatives — a subtle, real bug when people use `>> 1` as a drop-in for `÷ 2` on signed data.

(Languages name these differently: Java has `>>` for arithmetic and a separate `>>>` for logical; C's `>>` on a signed type is arithmetic on most compilers but technically implementation-defined; Python's integers are arbitrary-precision so `>>` always behaves arithmetically.)

## Rotate ≠ shift

A **rotate** (circular shift) takes the bit that would fall off one end and **wraps it around** to the other, so no bits are ever lost — the byte just spins. A plain shift *discards* the bit that drops off. Rotates are examinable at A Level, where they go by the name **cyclic shift**, and beyond any syllabus they're everywhere in cryptography and hashing (where you must mix bits *reversibly*, losing nothing); most CPUs have a dedicated `ROL`/`ROR` instruction.

## Where bitwise operations live in the wild

- **Flags / bitfields.** Eight on/off settings fit in one byte instead of eight booleans. A window's state (visible? resizable? focused? …) is often a single `int` you read and write with masks.
- **Unix file permissions.** `chmod 755` is bitwise to the bone: each octal digit is three bits `rwx`, so `755` = `111 101 101` = owner-read/write/execute, group and others read/execute. Adding "group write" is `mode | 0o020`.
- **Colour packing.** A pixel `0x2563EB` packs three channels into one number. Pull the green channel out with a shift then a mask: `(0x2563EB >> 8) & 0xFF` = `0x63` = 99. Red is `>> 16 & 0xFF`, blue is `& 0xFF`. (See the worked example below.)
- **Fast arithmetic.** `× 2ⁿ` and `÷ 2ⁿ` (unsigned) become single shifts; `x & (n−1)` computes `x mod n` when `n` is a power of two.
- **Hashing & checksums.** Mixing functions lean on XOR and shifts/rotates to scramble bits cheaply and reversibly.

## Worked examples

**1 — Unpack a colour.** From `0x2563EB`: red = `(0x2563EB >> 16) & 0xFF` = `0x25` = 37; green = `(>> 8) & 0xFF` = `0x63` = 99; blue = `& 0xFF` = `0xEB` = 235. Three channels, extracted with shifts and one mask each.

**2 — Toggle a single flag.** A settings byte is `1011 0010`. To flip the "bit 2" setting: XOR with `0000 0100` → `1011 0110`. Run it again and you're back — XOR is its own inverse.

**3 — Multiply by 10 with shifts.** `x * 10 = x * 8 + x * 2 = (x << 3) + (x << 1)`. Compilers do exactly this kind of shift-and-add to avoid a slow multiply.

## Common Misconceptions (Teaching Notes)

### 1. "`&` and `|` are just `and` / `or`"

Bitwise `&`/`|` combine *every bit*; logical `&&`/`||`/`and`/`or` combine *truth values*. `6 & 1` = `0` (bit-level), but `6 and 1` is truthy. Use bitwise for bit manipulation, logical for conditions.

**Fix.** Bit work → `& | ^ ~`; yes/no conditions → `&& || !` (or `and or not`).

### 2. "Right shift always divides by two"

Only a **logical** shift of an **unsigned** value cleanly halves. On signed negatives you need an **arithmetic** shift, and even that floors toward −∞ rather than truncating toward zero — so `>> 1` and `÷ 2` disagree for negatives.

**Fix.** Match the shift to the type; don't treat `>> 1` as identical to `÷ 2` on signed data.

### 3. "Shifting is just a fast multiply, with no downside"

A left shift drops the bits that fall off the top — that's silent [[Overflow and Underflow|overflow]]. `x << 1` is `x × 2` *only if* the top bit was 0.

**Fix.** Shifting is fast ×/÷ by powers of two **within range**; off the end, bits are lost.

### 4. "XOR is an exotic, rarely-used operator"

XOR is one of the most useful operators in computing: it toggles bits, compares for difference, swaps two variables without a temporary (`a^=b; b^=a; a^=b`), drives parity/checksums and RAID, and is the workhorse of stream ciphers and hashing. It's also, algebraically, **addition modulo 2**.

**Fix.** Treat XOR as a first-class tool — flip, compare, mix.

## Exam Notes

### Cambridge 0478 (IGCSE CS)

**§1.1.5** — **logical binary shifts** (left and right), their effect (×2 / ÷2 by powers of two), and that bits shifted off the end are lost. This card closes the shift row and adds the surrounding bit-manipulation context. (Overflow from a left shift is in [[Overflow and Underflow]].)

### Cambridge 9618 (A-Level CS)

**§4.3 Bit manipulation** is this card's row, and it names the whole of it. Shifts come in **three** families — **logical, arithmetic and cyclic**, left and right — so all three are fair game, not just the logical pair. The second objective is masking, and it is framed as *using bit manipulation to monitor or control a device*: **test and set a bit**. The four recipes above are that answer — `AND` to test, `OR` to set, `AND` with the inverted mask to clear, `XOR` to toggle — and a device-control question is asking for exactly these with a mask you design.

The same operations return in the **§4.2 instruction set**, acting on the accumulator: `AND`, `OR` and `XOR`, each taking either an immediate operand (`#n`, `Bn`, `&n`) or an `<address>`, plus `LSL #n` and `LSR #n` for the shifts — see [[Assembly Language]]. Note that the Cambridge set provides the **logical** shifts only; arithmetic and cyclic shifts are examined as understanding, not as instructions you are given.

Logical operators **AND / OR / NOT** also appear as gates in §3.2 ([[Logic Gates]]) and as operators in programming (§11).

### IB Computer Science

Not a named statement: A1.2's confirmed wording stops at **binary/hexadecimal conversion and logic gates** — bit-level operators, masking and shifts are beyond every published outline. They remain quiet allies in IB programming work (any flag-packing or parity trick), but carry no marks of their own.

*(AP CSA: Java has `& | ^ ~`, the arithmetic `>>`, and the logical `>>>`; the operators behave exactly as here on Java's two's-complement `int`.)*

## Connections

- **Prerequisite:** [[Logic Gates]] — bitwise AND/OR/XOR/NOT *are* those gates, run in parallel across a word; this card is "what the gates do to a whole byte at once." [[Number Bases]] — the binary the bits live in. [[Two's Complement]] — the sign bit that makes arithmetic shift necessary (sign extension).
- **Sibling:** [[Overflow and Underflow]] — a left shift is a third way to overflow (bits lost off the top).
- **Application:** masking underlies flags, [[Information Theory|parity/checksums]], colour packing, and permissions; XOR underlies swaps, ciphers, and error detection.

---

## Beyond Syllabus

### XOR's party tricks

XOR's self-inverse property ($a \oplus a = 0$, $a \oplus 0 = a$) powers a surprising amount: **swap without a temp** (`a^=b; b^=a; a^=b`), the **XOR linked list** (store one pointer per node as `prev XOR next`, halving pointer memory), single-pass "find the one unpaired element" puzzles (XOR everything; pairs cancel), and **one-time-pad / stream-cipher** encryption (`cipher = plain XOR key`, decrypt by XOR-ing the key again — the [[Stories/Turing at Bletchley|Lorenz cipher]] was XOR-based).

### AND and XOR are multiplication and addition mod 2

Over the field $\mathrm{GF}(2)$ (the integers mod 2), **XOR is addition** and **AND is multiplication**. This isn't a metaphor — it's why XOR-and-shift machinery builds CRCs, Reed–Solomon and Hamming error-correcting codes, and linear-feedback shift registers: they're doing *polynomial arithmetic over $\mathrm{GF}(2)$* with gates. The bridge from "toggle a bit" to "correct a corrupted transmission" runs straight through this identity, and lands in [[Information Theory]].

### Bit-twiddling hacks

A whole folklore of branchless one-liners lives here: `x & (x − 1)` clears the lowest set bit (loop it to **count set bits** — the *population count* / Hamming weight); `x & −x` isolates the lowest set bit; `x & (n − 1)` is `x mod n` for power-of-two `n`; checking `(x & (x − 1)) == 0` tests whether `x` is a power of two. CPUs now have dedicated `POPCNT` instructions because counting 1-bits turns out to matter that much (error-correction, chess engines, database indexes).

## Notation Reference

| Symbol | Meaning |
|--------|---------|
| `&` | bitwise AND (filter / test) |
| `OR` ( \| ) | bitwise OR (set bits on) |
| `^` | bitwise XOR (toggle / compare) |
| `~` | bitwise NOT (invert all bits) |
| `<<` | left shift (× $2^k$) |
| `>>` | right shift (÷ $2^k$); arithmetic on signed, logical on unsigned |
| `>>>` | logical (zero-fill) right shift — e.g. Java |
| mask | a constant whose 1-bits mark the positions to act on |

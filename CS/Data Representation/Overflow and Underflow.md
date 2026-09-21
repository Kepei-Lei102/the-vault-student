---
chinese: 溢出与下溢 (yìchū yǔ xiàyì)
prerequisites:
  - "[[Two's Complement]]"
leads_to:
  - "[[Floating-Point Representation]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/AP-CSA
  - curriculum/AP-CSP
  - syllabus/0478-1-1
  - syllabus/9618-1-1
  - type/deep
  - type/definition
  - notation/binary
  - misconception/overflow-throws-an-error
  - misconception/underflow-is-just-overflow-backwards
  - misconception/right-shift-is-always-divide
  - misconception/only-addition-overflows
---

# Overflow and Underflow 溢出与下溢

## Definition

**Overflow** is what happens when the true result of a calculation is **too big to fit** in the fixed number of bits you've given it. **Underflow** is the mirror: a result too small (too far below the minimum, or — for fractions — too close to zero) to fit. The box has a fixed size; sometimes the answer doesn't.

This card is the dark twin of [[Two's Complement]]. There, the fixed-width *wraparound* was the hero — it's exactly what made $a + (-a) = 0$, dropping the carry off the top to land on zero. Here is the same mechanism wearing a black hat: when the answer was supposed to be a real, large number and the carry falls off the top anyway, the result **silently wraps to something wrong**. Same physics, opposite intent.

> [!tip] The one idea
> A register is a [[Two's Complement|clock]], not a number line. Run off the top and you reappear at the bottom (`127 + 1 → −128`, `255 + 1 → 0`); run off the bottom and you reappear at the top (`0 − 1 → 255`). Whether that wrap is a **feature** (modular arithmetic you intended) or a **bug** (a count that overflowed) depends entirely on whether you *meant* to leave the range. Fixed-width arithmetic may wrap, but hardware can also expose carry/overflow flags, and software may check, trap or saturate; behaviour depends on the system.

### 中文锚点

想象一个只有四位的机械计数器：9999 再往前拨一下，显示的却是 0000。次数明明增加了，只是它没有第五个轮子来显示那个“1”。电脑里有些位数固定的整数也会这样回绕，于是显示出来的数字看着挺正常，背后却可能已经发生了一次超出范围的计算。不过，电脑也可以检查并报错，或停在能表示的最大值；回绕不是唯一选择。浮点数的下溢则是另一种限制：数值太接近零，原有的精度开始保不住。

## The same wraparound, now a bug

In an 8-bit byte the signed range is $-128 \dots +127$. Ask for one more than the top:

```
  0111 1111   (127)
+ 0000 0001   (1)
-----------
  1000 0000   = -128   ← the true answer +128 doesn't fit, so it wrapped
```

The arithmetic is *correct mod $2^8$* — it's the same clean wrap that gave you $a+(-a)=0$ — but here you didn't want to leave the range, so $+128$ silently became $-128$. Unsigned, the cliff is at the other end: `1111 1111 (255) + 0000 0001 = 1 0000 0000`, the leading 1 drops, and you get **0**. The carry that was harmless in subtraction is now the whole disaster.

## Spotting overflow

You can't fix what you can't detect, and the rule depends on whether the bits are unsigned or signed.

**Unsigned:** overflow happened iff there is a **carry out of the most significant bit** (a 1 falls off the left). `255 + 1` carries out → overflow.

**Signed (two's complement):** the test is one line —

> **Overflow ⟺ the carry *into* the sign bit differs from the carry *out* of the sign bit.**

Equivalently, and easier to eyeball: **two operands of the *same* sign that produce a result of the *opposite* sign.** Two positives can't truly sum to a negative; if they appear to, the sum overflowed. (Adding a positive and a negative can *never* overflow — the result is between them, always in range.)

![[overflow-detection-byte.svg|697]]
*Detecting signed overflow on `127 + 1`. Add column by column with carries. At the sign-bit column the carry coming **in** is 1 but the carry going **out** is 0 — they disagree, so the addition overflowed. The visible result `1000 0000` reads as −128, while the true answer (+128) needed a ninth bit the byte doesn't have. Compare `64 + 1`: carries into and out of the sign bit are both 0 — they agree, no overflow.*

**Worked.** *Trigger: two positive inputs produce a negative-looking byte. Tool: check the mathematical sum against the signed 8-bit range, −128 to +127.* $64 + 64$: `0100 0000 + 0100 0000 = 1000 0000`. Two positives, result negative (−128) → overflow (true answer +128 won't fit). $64 + 1 = $ `0100 0001` = 65, signs fine, carries agree → no overflow.

## Underflow

The same wheel, turned the other way. Drive *below* the minimum and you wrap to the maximum:

- **Unsigned:** `0000 0000 (0) − 0000 0001 (1) = 1111 1111 (255)`. Zero minus one underflows to 255. (This is why an unsigned loop counter that hits `i--` at `i = 0` suddenly becomes a huge number — a classic infinite-loop bug.)
- **Signed:** `1000 0000 (−128) − 1 = 0111 1111 (+127)`. One below the floor reappears at the ceiling.

> [!info] A word on the word "underflow"
> In **integer** work (this card / 0478 §1.1), "going below the minimum and wrapping" is often just called overflow too — it's the same event at the other edge. The term **underflow** is used most precisely for **floating-point**: a non-zero value so close to zero that it rounds away to 0 (covered in [[Floating-Point Representation]]). Both senses share the idea "the magnitude fell out the small end."

## Shifts can overflow too

Bit-shifting is its own family of operations — for unsigned integers, a **logical left shift** multiplies by 2 if the result fits; a **logical right shift** divides by 2 and discards any remainder — and it's a third way to overflow: a left shift pushes the top bit clean off the end (`1000 0000 << 1 = 0000 0000`, the 1 is lost), so the ×2 overflowed, exactly like an addition that ran off the top. The full treatment — logical vs **arithmetic** shifts, the sign-bit subtleties, and masking with AND/OR/XOR — is its own card: [[Bitwise Operations]].

## When overflow is the plan, not the bug

Wraparound is only a bug if you didn't want to leave the range. Plenty of code leaves it **on purpose**:

- **Modular arithmetic by design.** Hash functions, checksums, and pseudo-random generators *rely* on unsigned wraparound — they're doing arithmetic mod $2^n$ deliberately, and the dropped carry is the point (just like $a+(-a)=0$). A 24-hour clock rolling `23:59 → 00:00` is the everyday version.
- **Ring buffers / counters** that are *meant* to cycle.
- **Saturating arithmetic** — the opposite choice: instead of wrapping, the value *sticks* at the max or min. Audio and image code use this so that `250 + 10` in an 8-bit channel gives `255` (full white / max volume), not `4` (wraps to near-black) — clamping is what your senses expect.

So a CPU/language offers more than one behaviour: **wrap** (defined modular result), **saturate** (clamp), or **trap/flag** (raise an error). Knowing which one you're getting is the engineering.

## The famous bugs

Overflow's greatest hits — each is just a fixed-width counter meeting a number bigger than its designers imagined:

- **Pac-Man's level 256 "kill screen."** The level counter is a single **8-bit** byte (max 255). At level 256 it overflows; the fruit-drawing routine reads sprite data from the wrong memory and corrupts the entire right half of the maze. Only 9 dots survive there, so the 244 dots the level demands are unreachable — the game is mathematically unwinnable. Not an ending anyone designed; an overflow.
- **"Gangnam Style" vs YouTube (2014).** YouTube's view counter was a **signed 32-bit** integer, topping out at $2^{31}-1 = 2{,}147{,}483{,}647$. Psy's video became the first to approach ~2.15 billion views, so YouTube re-engineered the counter to **64-bit** (good for ~9.2 *quintillion*). Same quirk as Pac-Man, eight times wider.
- **The Year 2038 problem (Y2K38).** Unix systems count seconds since 1 Jan 1970 in a **signed 32-bit** `time_t`. It overflows at $2^{31}-1$ seconds — **03:14:07 UTC on 19 January 2038** — when adding one more second flips the sign bit and the clock jumps to **December 1901**. The fix (64-bit time) is the same move YouTube made; the cleanup is ongoing.
- **Ariane 5, Flight 501 (4 June 1996).** Guidance code reused from the slower Ariane 4 converted a **64-bit floating-point** horizontal-velocity value into a **16-bit signed integer**. Ariane 5 flew faster, the value exceeded $32{,}767$, the conversion overflowed, the guidance computer threw an error and shut down — and the rocket self-destructed ~37 seconds after launch. Roughly **\$370 million** lost to an unchecked cast.

The lesson under all four: a fixed-width number is a promise about the *largest value you'll ever need*, and overflow is what collects when that promise is broken.

## Common Misconceptions (Teaching Notes)

### 1. "Overflow throws an error / the program crashes"

Usually it's **silent** — the value just wraps and execution continues with a wrong number, which is far more dangerous than a crash. Behaviour varies by language: C leaves *signed* overflow **undefined** (the compiler may assume it never happens) but defines *unsigned* as wrapping mod $2^n$; Java and Go wrap silently; Rust **panics** in debug builds and wraps in release; Python's integers grow without limit, so they don't overflow at all.

**Fix.** Never assume you'll be told. If a sum could exceed the range, check it or use a wider/arbitrary-precision type.

### 2. "Underflow is just overflow's opposite and also crashes"

Integer "underflow" is the *same* wraparound at the bottom edge (0 − 1 → max), not a separate explosion. And the most precise meaning of *underflow* is the floating-point one — a tiny value rounding to zero — which loses precision quietly rather than crashing.

**Fix.** Keep two senses straight: integer wrap-below-minimum vs floating-point round-to-zero ([[Floating-Point Representation]]).

### 3. "Right shift always divides by two"

Only for **unsigned** values, or with an **arithmetic** right shift on signed ones. A *logical* right shift on a negative number pulls a 0 into the sign position and gives nonsense (−8 → +124). Choose the shift that matches the type.

**Fix.** Signed ÷2 by shifting ⇒ arithmetic right shift (sign-preserving).

### 4. "Only addition can overflow"

Multiplication overflows much faster (two 16-bit values can need 32 bits). A **left shift** overflows by pushing bits off the top. Even **negation** overflows at one point: negating the most-negative number (−128 in a byte) can't be represented — the [[Two's Complement|lonely −128]] from the last card.

**Fix.** Any operation whose true result can leave the range can overflow — add, multiply, shift, even negate.

## Exam Notes

### Cambridge 0478 (IGCSE CS)

**§1.1.4** — add two **positive 8-bit binary integers** and explain overflow: an unsigned result above **255** cannot fit in the register. Carry beyond the eighth bit signals overflow for this unsigned task. This is distinct from signed overflow, where a result can be out of range with no carry-out. **§1.1.5** — perform logical left/right shifts, identify bits lost, and explain their multiplicative meaning. For unsigned values, right shift divides by a power of two and discards any remainder; left shift multiplies only while the result fits. **§1.1.6** supplies two's-complement representation → [[Two's Complement]].

### Cambridge 9618 (A-Level CS)

**§1.1 (2027–2029)** requires binary addition **and subtraction** using positive and negative integers, with understanding of overflow. Use the signed representable range to check the true answer. The same-sign test and unequal carries into/out of the sign bit are useful detection methods; the syllabus does not explicitly name the carry-XOR circuit as a separate outcome. **§13.3** requires floating-point overflow, underflow and representation/precision consequences → [[Floating-Point Representation]]. Underflow near zero is different from an integer result falling below its minimum.

### IB Computer Science — first assessment 2027

The full guide's **A1.2.1–2** covers binary/hexadecimal integers, conversions and binary storage. It does **not explicitly prescribe binary addition, signed-overflow detection or floating-point underflow calculations**. Keep those as supporting enrichment, without inferring a required carry-rule question from the broad word “representation”. Language behaviour also differs: Java `int` has a fixed range; ordinary Python integers expand as memory permits.

### AP Computer Science A — effective Fall 2025

**§1.5.B.1–3** requires reasoning about the `int` range, `Integer.MIN_VALUE` / `Integer.MAX_VALUE`, and expressions whose results lie outside that range. A Java `int` uses 32 signed bits: adding 1 to **2,147,483,647** yields **−2,147,483,648**. The trigger is the *mathematical result leaving the allowed range*, not an exception message. Bit-level carry tests and two's-complement conversion are not prescribed. **§1.5.C.1** separately addresses `double` round-off; that is not the same as underflow. The broader casting work of §1.5 still needs its own Java practice.

### AP Computer Science Principles

**Topic 2.1, DAT-1.B.1–3**, covers fixed-bit limitations, possible integer overflow, and approximate representation/round-off for real numbers. **CRD-2.I.4** also identifies overflow as an error category. Explain *why* a finite number of patterns imposes a limit. The reference-sheet language instead abstracts integers as limited by available memory; do not assume its arithmetic wraps like an 8-bit register. [College Board CED, pp. 39 and 47](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-course-and-exam-description.pdf)

**Not prescribed by these outcomes:** signed carry-XOR detection and floating-point underflow calculation are not AP CSA/AP CSP or IB A1.2 requirements; 0478 does not require floating-point underflow. Cambridge 9618 §13.3 does require the floating-point concepts.

## Connections

- **Prerequisite:** [[Two's Complement]] — the wraparound this card depends on; overflow is that wrap when you *didn't* want it. The lonely −128 reappears here as negation overflow.
- **Foundation:** [[Number Bases]] — fixed-width binary and the byte; [[Half-Adder and Full-Adder]] — the full-adder's carry-out is literally the overflow signal.
- **Next:** [[Floating-Point Representation]] — how fractions and huge ranges are stored, where overflow → ±∞ and underflow → 0 take their precise meaning; then text/sound/image encoding and compression close the bay.
- **Maths underneath:** modular arithmetic ($\mathbb{Z}/2^n\mathbb{Z}$) — wrap is the ring's reduction; saturating arithmetic is the non-modular alternative.

---

## Beyond Syllabus

### Floating-point: overflow → ∞, underflow → 0

Integers wrap; floats don't. When a floating-point result is too large it becomes a special value **±∞** (infinity); when it's too small to represent it **underflows toward 0**, first through gradual-precision "denormal" numbers, then to zero outright. So the two failure modes have *defined* values in IEEE 754 rather than silent wrap — a deliberately safer design, detailed in [[Floating-Point Representation]].

### Wrapping vs trapping vs saturating — a real design axis

Hardware and languages genuinely choose among three overflow policies: **wrap** (mod $2^n$ — C unsigned, most CPUs by default), **trap/flag** (raise an exception or set an overflow flag — Rust debug, Swift, the CPU's overflow flag `V`), and **saturate** (clamp to max/min — DSP, SIMD media instructions like `paddusb`). Picking the wrong one is how overflow bugs ship; picking the right one is how DSP audio avoids clicks. "Undefined behaviour" for signed overflow in C is a fourth, sharper-edged option that lets compilers optimise aggressively — and occasionally delete your safety checks.

### Checked and arbitrary-precision arithmetic

Languages increasingly fight silent overflow: Rust's `checked_add` returns `None` on overflow, Swift traps by default, and Python/Ruby/Haskell promote to **arbitrary-precision** integers that never overflow (at the cost of speed and memory). The right-by-default trend is "make overflow loud," because four decades of the bugs above proved that silent is expensive.

## Notation Reference

| Symbol | Meaning |
|--------|---------|
| overflow | a true result larger than the fixed width can hold |
| underflow | a result below the minimum (integer wrap) or too near zero to represent (float) |
| carry-out | a 1 leaving the most significant bit — the unsigned-overflow signal |
| `<<` / `>>` | logical left / right shift (×2 / ÷2) |
| arithmetic `>>` | sign-preserving right shift (signed ÷2) |
| wrap / saturate / trap | the three things hardware can do on overflow: cycle, clamp, or flag |

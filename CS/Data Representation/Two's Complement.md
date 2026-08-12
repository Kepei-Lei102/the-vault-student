---
chinese: 补码 (bǔmǎ)
prerequisites:
  - "[[Number Bases]]"
leads_to:
  - "[[Overflow and Underflow]]"
  - "[[Floating-Point Representation]]"
  - "[[Bitwise Operations]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-1-1
  - syllabus/9618-1-1
  - type/deep
  - type/definition
  - notation/binary
  - misconception/sign-bit-is-just-a-flag
  - misconception/twos-complement-has-two-zeros
  - misconception/negate-is-just-flip-bits
  - misconception/overflow-always-a-bug
---

# Two's Complement 补码

## Definition

**Two's complement** is the scheme almost every computer uses to store **negative whole numbers** in a fixed number of bits. In an $n$-bit field it represents the values $-2^{n-1}$ up to $+2^{n-1}-1$ (for a byte: **−128 to +127**), and it does so in a way that makes subtraction *fall out of addition for free*.

Here is the idea worth carrying away, because it recurs everywhere in computing:

> [!tip] Limitation turned into a feature
> A variable has only a **fixed** number of bits, so its arithmetic is forced to **wrap around** when it runs off the end — a hard limitation. Two's complement doesn't fight that wraparound; it **weaponises** it. By choosing to represent $-x$ as the bit-pattern that *wraps back to zero when you add $x$*, negatives and subtraction become free: the **same adder circuit** that does $a+b$ now does $a-b$ with no new hardware, and the carry that falls off the top — the "overflow" — is exactly what makes it work.

That is the whole story. Everything below is detail in service of that one move.

### 中文锚点

**补码**（bǔmǎ, two's complement）：计算机用来在**固定位数**里存**负整数**的方法。$n$ 位能表示 $-2^{n-1}$ 到 $+2^{n-1}-1$（一字节：**−128 到 +127**）。

核心思想——**把限制变成特性**：变量位数固定，算术必然**溢出回绕**（wrap around）。补码不是对抗回绕，而是**利用**它：把 $-x$ 定义成「再加 $x$ 就回到 0」的那个位模式。于是减法 = 加法，**同一个加法器电路**既能算 $a+b$ 又能算 $a-b$，从顶端丢掉的进位（溢出）正是让它成立的关键。

**最核心的特性**：$a+(-a)=0$ —— 「负数」的本质就是「加上它等于零」的那个数（加法逆元）。补码正是**靠溢出**做到这一点：$a+(-a)$ 加到 $2^n$，最高位进位溢出丢掉，正好回绕成 $0$。所以 $-a$ 不是「$a$ 戴了个负号」，而是被**定义**成「能把 $a$ 抵消成零」的位模式。

- **取负的口诀**：所有位**取反**，再 **+1**（invert + 1）。
- 最高位权重是 **负的** $-2^{n-1}$（不是单纯的「符号旗」）。
- 只有**一个 0**（不像原码 sign-and-magnitude 有 +0 和 −0 两个）。

## The problem: negatives in a fixed box

[[Number Bases|Unsigned binary]] handles 0, 1, 2, … fine — but how do you store $-5$ when all you have is eight 0/1 cells and no minus sign to write? You must spend the bit patterns you have to *mean* negative numbers. The only question is **which patterns mean what**, and a good scheme is one where ordinary binary addition still gives right answers.

## First attempt: sign-and-magnitude (and why it's clumsy)

The obvious idea: steal the top bit as a **sign flag** (0 = positive, 1 = negative) and let the rest be the magnitude. So $+5 =$ `0000 0101` and $-5 =$ `1000 0101`. Readable — but it has two ugly problems:

1. **Two zeros.** `0000 0000` is $+0$ and `1000 0000` is $-0$. Two bit patterns for one number wastes a code and forces "is it zero?" to check two cases.
2. **Addition breaks.** Add $+3$ and $-1$ in sign-and-magnitude: `0000 0011 + 1000 0001 = 1000 0100` = $-4$. Wrong. The hardware would need *special rules* to compare signs and magnitudes and decide whether to add or subtract — a whole extra circuit.

A representation you have to special-case is a representation fighting the hardware. Two's complement is the one that stops fighting.

## Two's complement: the representation

Same eight cells, one change of meaning: **the top bit's place value is negative.** For 8 bits the column weights are

$$-128,\ 64,\ 32,\ 16,\ 8,\ 4,\ 2,\ 1.$$

Every other column is the usual positive power of two; only the leading one flips sign. A value is still just "add the columns that are on" — you've simply made the biggest column count *against* you. So `1111 1011`:

$$-128 + 64 + 32 + 16 + 8 + 2 + 1 = -5.$$

The top bit still tells you the sign at a glance (1 ⇒ negative), but it is **not a mere flag** — it carries the weight $-2^{n-1}$, and that weight is what makes the arithmetic work.

**To negate a number: invert every bit, then add 1.** Take $+5 =$ `0000 0101`; invert → `1111 1010`; add 1 → `1111 1011` $= -5$. ✓ The same recipe run on $-5$ gives back $+5$, so it's its own inverse.

**Range and the single zero.** Eight bits give $-128 \dots +127$ — note it's *lopsided* (one more negative than positive; more on that below). And there is exactly **one zero**: `0000 0000`, whose negation (invert → `1111 1111`, +1 → `1 0000 0000`, drop the carry → `0000 0000`) is itself. One zero, no waste — already better than sign-and-magnitude.

## Why it works: the number is on a clock

The reason invert-and-add-1 is the right recipe is that a fixed-width register is a **wheel**, not a line. An $n$-bit value can only ever be one of $2^n$ patterns, and adding 1 to the largest pattern rolls back to the smallest — exactly like a car odometer rolling `9999 → 0000`, or a 12-hour clock going `12 → 1`. Arithmetic in a fixed width is **arithmetic modulo $2^n$.**

On a clock, "subtract 3 hours" and "add 9 hours" land in the same place ($-3 \equiv 9 \pmod{12}$). Two's complement is the same trick on $2^n$: the pattern we *call* $-x$ is the unsigned value $2^n - x$, because

$$x + (2^n - x) = 2^n \equiv 0 \pmod{2^n}.$$

Adding $x$ to "$-x$" gives $2^n$, which is `1` followed by $n$ zeros — and the `1` falls off the top of the register and is **discarded**. What's left is `0`. *That dropped carry is not a bug; it is the entire mechanism.* And invert-and-add-1 is just a quick way to compute $2^n - x$: inverting all bits gives $(2^n - 1) - x$, and the $+1$ finishes it to $2^n - x$.

**This is the feature that makes $-a$ genuinely *negative*.** What does it even *mean* for a bit-pattern to be "minus five"? The only honest answer is the one from algebra: a negative number is the **additive inverse** — the thing you add to $a$ to get **nothing**. Two's complement is engineered to guarantee exactly that, and it guarantees it *by overflowing*:

$$a + (-a) = 2^n \;\xrightarrow{\text{carry off the top}}\; \boxed{0}.$$

So $-a$ is not "$a$ wearing a minus sign in the top bit" — it is *defined* as the pattern that **cancels $a$ to zero**, and the overflow off the end is precisely what produces that zero. Read it the way you flagged it: the fixed-width limit (numbers must wrap) is turned into the one property that earns these patterns the name "negative." Everything else — subtraction on a single adder, the lone zero, the whole clock — falls out of this single guarantee.

![[twos-complement-wheel.svg|697]]
*A 4-bit register as a wheel of its 16 patterns. Going clockwise counts up; each pattern has two readings — **unsigned** 0–15 (grey) and **two's-complement signed** −8…+7 (coloured). The top half (`0xxx`) is 0…7, the bottom half (`1xxx`) is −8…−1, and $-x$ always sits at position $16-x$ (so −5 is at 11 = `1011`). Two boundaries matter: between `1111` (−1) and `0000` (0) the wheel turns *smoothly* (add 1 to −1, drop the carry, get 0); between `0111` (+7) and `1000` (−8) is the **cliff** where +1 jumps from the largest positive to the smallest negative — that jump is overflow ([[Overflow and Underflow]]).*

## Subtraction is just addition

Because $-x$ is built to wrap to zero, **$a - b$ is computed as $a + (\text{two's complement of } b)$** — one addition, then throw away any carry off the top.

**Worked: $12 - 5$.** Negate 5 → `1111 1011`. Add to $12 =$ `0000 1100`:

```
  0000 1100   (12)
+ 1111 1011   (-5)
-----------
1 0000 0111   drop the leading carry
  0000 0111 = 7   ✓
```

**Worked: $5 + (-5)$.** `0000 0101 + 1111 1011 = 1 0000 0000` → drop carry → `0000 0000` $= 0$. ✓

One adder, both operations. This is why two's complement won: a CPU needs **no subtractor** — to compute $a-b$ it inverts $b$, feeds a 1 into the adder's carry-in (that's the "+1"), and adds. The [[Half-Adder and Full-Adder|full-adder]] you'd build from gates is the whole arithmetic unit for signed *and* unsigned numbers at once.

## The one wart: an asymmetric range

The single price two's complement pays is a **lopsided range**: 8 bits run $-128 \dots +127$, one more negative than positive. The lonely value is $-128 =$ `1000 0000`, which has no positive partner ($+128$ doesn't fit in a byte). Try to negate it — invert `1000 0000` → `0111 1111`, add 1 → `1000 0000` — and you get $-128$ back. Negating the most-negative number overflows; it's the one input where "invert and add 1" can't give the right answer, because the right answer doesn't exist in the box. (This corner is a genuine source of real bugs — held for [[Overflow and Underflow]].)

## Worked examples

**1 — Read a signed byte.** `1001 0110`: top bit is 1, so negative. Columns: $-128 + 16 + 4 + 2 = -106$. (Cross-check via the recipe: invert → `0110 1001`, +1 → `0110 1010` $= 106$, so the original is $-106$. ✓)

**2 — Write $-40$ in 8-bit.** $+40 =$ `0010 1000`; invert → `1101 0111`; +1 → `1101 1000`. Check: $-128 + 64 + 16 + 8 = -40$. ✓

**3 — Subtract by adding.** $-3 - 4 = -3 + (-4)$. $-3 =$ `1111 1101`, $-4 =$ `1111 1100`. Sum: `1 1111 1001` → drop carry → `1111 1001` $= -128+64+32+16+8+1 = -7$. ✓

## Common Misconceptions (Teaching Notes)

### 1. "The top bit is just a sign flag"

It *looks* like one (1 means negative), but in two's complement the leading bit carries a real **negative place value** $-2^{n-1}$. That's the difference from sign-and-magnitude, and it's exactly why addition works without special-casing. Read `1111 1011` as $-128+64+\dots$, not as "minus, then 1111011."

**Fix.** Compute the value by the negative-weight columns, or by invert-and-add-1 — never by "flip the sign bit and read the rest."

### 2. "Two's complement has a +0 and a −0"

That's *sign-and-magnitude* (and one's complement). Two's complement has exactly **one** zero — a deliberate advantage. The freed-up pattern is spent on that one extra negative value (−128), which is where the asymmetry comes from.

**Fix.** Remember: one's complement / sign-magnitude → two zeros; two's complement → one zero, one extra negative.

### 3. "To negate, just flip all the bits"

Flipping all the bits is **one's complement** — it's off by one. You must invert **and add 1**. (Flipping `0000 0101` gives `1111 1010` = −6, not −5.)

**Fix.** Invert *then* +1, every time.

### 4. "Overflow means something went wrong"

The carry that drops off the top during subtraction is *intended* — it's the wraparound doing its job. Genuine overflow (a result that doesn't fit the range) is a separate event with its own detection rule, and even that is sometimes a *feature* (unsigned wraparound is defined modular arithmetic, used deliberately in hashing and cryptography). Sorting out "harmless dropped carry" from "true overflow" is the job of [[Overflow and Underflow]].

**Fix.** A dropped carry in a subtraction is normal; true overflow is when two same-signed numbers add to the wrong sign — see [[Overflow and Underflow]].

## Exam Notes

### Cambridge 0478 (IGCSE CS)

**§1.1.6** — represent positive and negative integers in **two's complement** (8-bit), and convert both ways. **§1.1.4** — perform **binary addition** of two positive 8-bit integers (the addition mechanism is covered here; the overflow-detection and **logical shifts** of §1.1.4–5 are in [[Overflow and Underflow]]). Be ready to: write a given denary value in 8-bit two's complement, read a two's-complement byte back to denary, and negate via invert-and-add-1.

### Cambridge 9618 (A-Level CS)

**§1.1** asks for **signed binary** by *both* sign-and-magnitude and two's complement, and to contrast them — both are here, plus the reason two's complement wins. Binary addition + overflow complete §1.1 in [[Overflow and Underflow]]; **BCD** is in [[Floating-Point Representation]]. Expect to justify *why* two's complement is used (one zero; subtraction via one adder).

### IB Computer Science

Not yet a confirmed statement: the rebuilt course's A1.2 ("Data representation and computer logic") **confirms binary/hexadecimal conversion by name** but its published wording does not name signed representation — pending the official guide, treat two's complement as *probable-adjacent* rather than examined. The conversion discipline transfers whole either way, and IB's Java/Python programming strand meets this card the moment an `int` wraps negative.

*(AP CSA doesn't test the representation, but Java's `int` is 32-bit two's complement, and its wraparound — `Integer.MAX_VALUE + 1` going negative — is exactly this wheel.)*

## Connections

- **Prerequisite:** [[Number Bases]] — unsigned binary and place value; two's complement is "place value with a negative leading column."
- **The circuit:** [[Half-Adder and Full-Adder]] — the full-adder built from gates is the one unit that does signed and unsigned add/subtract, *because* of two's complement.
- **Next:** [[Overflow and Underflow]] — what happens at the cliff: detecting true overflow, underflow, logical/arithmetic shifts, and the famous overflow bugs (and deliberate wraparound).
- **Maths underneath:** modular arithmetic — a fixed-width register is the ring $\mathbb{Z}/2^n\mathbb{Z}$; the clock is the right mental model.

---

## Beyond Syllabus

### It's literally arithmetic in $\mathbb{Z}/2^n\mathbb{Z}$

Everything here is the algebra of integers **modulo $2^n$**. The unsigned bytes are the residues $0 \dots 2^n-1$; two's complement just relabels the top half $2^{n-1} \dots 2^n-1$ as the negatives $-2^{n-1} \dots -1$. Addition, subtraction, and multiplication all "work" because they're the ring operations mod $2^n$, and the dropped carry *is* the reduction mod $2^n$. The clarifying identity: **$-1$ is `1111…1` (all ones) = `0xFF…F`**, because $-1 \equiv 2^n - 1$. Once you see that, "why is −1 all ones?" answers itself.

### Why two's complement beat the alternatives

Early machines tried **sign-and-magnitude** and **one's complement** (negate = invert only). Both carry two zeros, and one's complement needs an "end-around carry" (the carry-out gets added back in) to make addition work. Two's complement needs *none* of that — one ordinary adder, one zero, no special cases — so by the 1960s it was universal. It's a rare case where the theoretically cleanest option is also the cheapest to build; engineering and elegance agreed for once (unlike the base-2-vs-base-3 story in [[Number Bases]]).

### Sign extension

To widen a signed number to more bits (8-bit → 16-bit) you **copy the sign bit** into all the new high bits: `1111 1011` (−5) becomes `1111 1111 1111 1011` (still −5). Copying the top bit preserves the value precisely because that bit holds the $-2^{n-1}$ weight; this "sign extension" is why CPUs have separate arithmetic vs logical right-shift instructions — the distinction at the heart of [[Bitwise Operations]].

## Notation Reference

| Symbol | Meaning |
|--------|---------|
| $n$ | the field width in bits (8 for a byte) |
| MSB | most significant bit; in two's complement its weight is $-2^{n-1}$ |
| invert + 1 | the negation recipe: flip every bit, then add 1 |
| $2^n - x$ | the unsigned value of the pattern that means $-x$ |
| $\equiv \pmod{2^n}$ | "same on the wheel" — equal after dropping carries beyond $n$ bits |
| `0xFF` | $-1$ in 8-bit two's complement (all ones) |

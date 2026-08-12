---
chinese: 浮点数表示 (fúdiǎnshù biǎoshì)
prerequisites:
  - "[[Number Bases]]"
  - "[[Two's Complement]]"
  - "[[Overflow and Underflow]]"
  - "[[Pipelining and Simultaneous Multithreading]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/data-representation
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-13-3
  - syllabus/9618-1-1
  - type/definition
  - type/technique
  - notation/binary
  - misconception/floats-are-exact
  - misconception/more-bits-always-better
---

# Floating-Point Representation 浮点数表示

![[float-captcha-comic.png|697]]

> **Website:** *Security check — prove you are a robot. What is 0.1 + 0.2?*
> **Robot:** `0.30000000000000004`
> **Website:** *✓ Identity confirmed. Welcome.*

The joke is real. Ask any computer on Earth — your laptop, your phone, a supercomputer — to add $0.1$ and $0.2$, and it returns exactly that answer, wrong in exactly that digit. A human says $0.3$ and would fail the check; a machine *cannot* say $0.3$. This is not a bug. It is the visible edge of a design decision — the same decision that lets $32$ little bits hold both $6.02\times10^{23}$ and $0.0000001$ — and by the end you will be able to compute the wrong answer by hand.

> *Fixed-point integers can count exactly, but only across a fixed span. Floating point trades a little of that exactness for an enormous reach — it is binary scientific notation, and every trade-off it makes is written into the split between two fields.*

[[Two's Complement]] gave us signed integers, but they live on a fixed grid: with $16$ bits you get the whole numbers from $-32768$ to $+32767$, spaced exactly $1$ apart — no fractions, and nothing beyond that wall. A computer also has to hold $6.02\times10^{23}$ and $0.0000001$. The fix is the same one you already use in decimal: **scientific notation.** Write $6.02 \times 10^{23}$ — a *significand* ($6.02$) times a *base* raised to an *exponent* ($23$) — and a handful of digits now covers a colossal range. **Floating point is exactly this, in binary** (see [[Standard Form (Vocab)]] for the decimal version).

## 中文锚点

**浮点数 (fúdiǎnshù)** = floating-point number：用"二进制科学计数法"存储实数——

$$\text{数值} = \text{尾数 (mantissa)} \times 2^{\text{阶码 (exponent)}}$$

一个浮点数被切成两个字段：**尾数**（有效数字，决定**精度 precision**）和**阶码**（决定**范围/数量级 range**）。剑桥 9618 的约定：尾数和阶码都用 [[Two's Complement|二进制补码]]，尾数的小数点在符号位之后。

- **规格化 (normalisation)**：把尾数左移、同时减小阶码，直到**符号位与其后第一位不同**（正数形如 `0.1…`，负数形如 `1.0…`）——挤掉前导的冗余位，让有限的尾数位承载最多的有效数字。
- **范围 vs 精度的权衡**：总位数固定。阶码位越多 → 范围越大但精度越低；尾数位越多 → 精度越高但范围越小。
- **上溢/下溢 (overflow/underflow)**、**舍入误差 (rounding error)**：尾数位有限，很多十进制小数（如 $0.1$）在二进制里无限循环，只能近似——所以 $0.1+0.2 \ne 0.3$。
- **IEEE 754**：现实硬件的统一标准——符号位单独存、阶码加偏移量 (bias)、隐含首位 $1$；单精度 $1+8+23$ 位，双精度 $1+11+52$ 位。注意：IEEE 的规格化窗口是 $[1,2)$（尾数形如 $1.xxx$），剑桥格式是 $[\tfrac12,1)$（形如 $0.1xxx$）——差的那个因子 $2$ 被阶码吸收，所以同一个数在两种格式里阶码相差 $1$。AI 时代把"范围 vs 精度"这笔账重新算了一遍：训练用 bfloat16（保范围、砍精度），推理甚至只用 $4$ 位整数。

---

## The idea — a number split into two jobs

A floating-point number stores a real value as

$$\text{value} \;=\; \text{mantissa} \times 2^{\text{exponent}}$$

and packs it into a fixed number of bits split into **two fields**, each with a different job:

- the **mantissa** (also called the *significand*) holds the **significant figures** — it decides **precision**, how finely you can pin the value down;
- the **exponent** holds the **scale** — it decides **range**, how large or small the magnitude can be.

That two-field split is the whole story. Everything below — normalisation, the range–precision trade-off, overflow, rounding error — is a consequence of dividing a fixed bit budget between "how precise" and "how big."

> [!info] Fixed-point vs floating-point
> A **fixed-point** number puts the binary point at a *fixed* column (e.g. always 8 integer bits then 8 fraction bits). Simple and exact, but the point can't move, so the range is cramped. **Floating-point** lets the point *float* — the exponent says where it goes — buying range at the cost of even spacing. Fixed-point still wins where exactness matters (money: many currencies are stored in integer cents, never floats).

---

## The Cambridge 9618 format

The 9618 convention is clean and worth learning exactly, because every exam question uses it:

- **Both fields are [[Two's Complement|two's-complement]]** numbers — so the sign is built in, no separate sign bit to bolt on.
- The **mantissa** is a two's-complement *fraction*: the binary point sits **immediately after the leading (sign) bit**. So an 8-bit mantissa $s\,.\,b_1 b_2 b_3 b_4 b_5 b_6 b_7$ has value $-s + b_1 2^{-1} + b_2 2^{-2} + \cdots + b_7 2^{-7}$, a number in $[-1, 1)$.
- The **exponent** is an ordinary two's-complement integer (an $8$-bit exponent reaches $-128$ to $+127$).

Take a running example: a **16-bit float = 8-bit mantissa + 8-bit exponent.**

**Decode (float → denary).** Mantissa `01101000`, exponent `00000011`:

$$\text{mantissa} = 0.1101000_2 = \tfrac12 + \tfrac14 + \tfrac1{16} = 0.8125, \qquad \text{exponent} = +3.$$
$$\text{value} = 0.8125 \times 2^3 = 0.8125 \times 8 = \boxed{6.5}.$$

**Encode (denary → float).** Store $+6.5$:

1. Write it in binary: $6.5 = 110.1_2$.
2. Slide the point to the front to get a mantissa in $[\tfrac12, 1)$: $110.1_2 = 0.1101_2 \times 2^{3}$.
3. Pad the mantissa to $8$ bits and write the exponent in two's complement: mantissa `01101000`, exponent `00000011`. ✓ (matches the decode above).

> [!tip] The ×2 trick — converting the fraction part
> Step 1 hides a skill: how do you turn $0.6875$ into binary *efficiently*? For the integer part you already divide by $2$ and collect remainders ([[Number Bases]]). For the fraction part, do the mirror image: **repeatedly multiply by 2, and each time write down the digit that crosses the point.**
>
> $$0.6875 \times 2 = \mathbf{1}.375 \quad\to\quad 0.375 \times 2 = \mathbf{0}.75 \quad\to\quad 0.75 \times 2 = \mathbf{1}.5 \quad\to\quad 0.5 \times 2 = \mathbf{1}.0 \;\;\text{(stop)}$$
>
> Read the bold digits top to bottom: $0.6875 = 0.1011_2$. (Check: $\tfrac12 + \tfrac18 + \tfrac1{16} = 0.6875$. ✓) Keep only the fraction after each step; stop when it hits $0$.
>
> **Why it works:** multiplying by $2$ shifts the binary point one place right, so the digit that pops out into the ones place *is* the next fraction bit — the same reason ÷$2$ remainders read out integer bits, run in reverse.
>
> Now run it on $0.1$: $\;0.1 \to \mathbf{0}.2 \to \mathbf{0}.4 \to \mathbf{0}.8 \to \mathbf{1}.6 \to \mathbf{1}.2 \to \mathbf{0}.4 \ldots$ — and $0.4$ has appeared before. The process is in a loop, so the bits recur forever: $0.1_{10} = 0.000110011001100\ldots_2$. The ×2 trick doesn't just convert — when a fraction *can't* be stored exactly, it **proves** it, by looping. Hold that thought.

**A negative value.** Store $-6.5$. The magnitude normalises the same way ($0.1101 \times 2^3$); now make the mantissa two's-complement negative — negate `01101000`: invert to `10010111`, add $1$ → `10011000`. Check: $1.0011000_2 = -1 + \tfrac18 + \tfrac1{16} = -0.8125$, and $-0.8125 \times 2^3 = -6.5$. ✓ Exponent stays `00000011`.

![[float-format-anatomy.svg|660]]

---

## Normalisation — squeezing out wasted bits

The same value can be written many ways: $6.5 = 0.1101 \times 2^3 = 0.01101 \times 2^4 = 0.001101 \times 2^5$. The later forms waste mantissa bits on leading zeros — bits that carry *no* significant figures. **Normalisation** picks the one form that wastes nothing, and it is the single most tested skill in this topic.

**The rule (9618):** shift the mantissa left and decrease the exponent to match, until the **sign bit and the first bit after the point are different.**

- **positive** numbers normalise to `0.1…` (value in $[\tfrac12, 1)$) — a $0$ then a $1$;
- **negative** numbers normalise to `1.0…` (value in $[-1, -\tfrac12)$) — a $1$ then a $0$.

**Why this exact rule?** A normalised mantissa has no leading redundant bits, so all $7$ fraction bits carry real significant figures — **maximum precision** for the bits you paid for. It also makes the representation **unique** (one bit-pattern per value), which the hardware needs.

**Worked normalisation.** Normalise `0.0011010` $\times\,2^5$:

$$0.0011010 \times 2^5 \;\xrightarrow{\text{shift left 2, } \exp - 2}\; 0.1101000 \times 2^3.$$

The top two bits are now $0,1$ — different — so it is normalised, and it is the $+6.5$ from before. (Every shift left multiplies the mantissa by $2$; dropping the exponent by $1$ divides by $2$; the value is unchanged, only the wasted bits are gone.)

> [!warning] Normalising a negative number trips everyone
> For a *negative* mantissa the target is `1.0…`, **not** `1.1…`. Example: normalise `1.1101000` (value $-0.1875$). Shift left until the leading pair is $1,0$: `1.0100000` $\times\,2^{-2}$. A quick check that you're done — read the first two bits: identical means keep shifting, different means stop.

---

## Range vs precision — one budget, two claims on it

The total bit count is fixed, and the mantissa and exponent are fighting over it. Move the boundary and watch the trade:

| 16-bit split | Exponent reach | Mantissa fraction bits | Consequence |
|---|---|---|---|
| **8 mantissa / 8 exponent** | $2^{-128}$ … $2^{127}$ (vast) | 7 | huge range, coarse precision (~2 sig. figs) |
| **12 mantissa / 4 exponent** | $2^{-8}$ … $2^{7}$ (small) | 11 | fine precision, tiny range |

**More exponent bits → bigger range but fewer significant figures. More mantissa bits → finer precision but a smaller reach.** You cannot have both from a fixed budget; a format is a decision about which you need more. (This is why real machines offer *several* sizes — 32-bit `float`, 64-bit `double` — so you can buy more of both by spending more bits total.)

A subtle, important consequence: **floating-point numbers are not evenly spaced.** Because the value is mantissa $\times\,2^{\text{exponent}}$, the representable numbers cluster tightly near zero and spread further apart as the magnitude grows — each time the exponent ticks up, the gap between neighbours *doubles*.

![[float-nonuniform-spacing.svg|680]]

---

## Overflow, underflow, and rounding error

Three ways a real value fails to fit — the topic's practical payoff, and a direct sequel to [[Overflow and Underflow]]:

- **Overflow** — the magnitude is too *large*: the exponent it needs exceeds the biggest the field can hold (past $+127$ here). The number cannot be stored at all; real hardware signals this (IEEE 754 returns $\pm\infty$).
- **Underflow** — the magnitude is too *small* (a tiny positive number closer to $0$ than the smallest normalised value): the exponent it needs is below the field's floor, and the value collapses to $0$. Silent, and dangerous when you then divide by it.
- **Rounding error** — the value is in range but has **more significant figures than the mantissa can hold**, so it is stored to the nearest representable float. This is the everyday one, and it never fully goes away.

**Why $0.1 + 0.2 \ne 0.3$ — the robot check, explained.** The ×2 trick already showed it: in binary, $0.1_{10} = 0.0001100110011\ldots_2$ *recurs forever*, exactly as $\tfrac13 = 0.333\ldots_{10}$ does in decimal. A finite mantissa must chop it off, so $0.1$ is stored a hair too large; add the (also-rounded) $0.2$ and the tiny errors survive: the result is $0.30000000000000004$ — the robot's answer from the opener, to the digit. Nothing is broken — the mantissa simply ran out of bits. And because every machine follows the same standard (IEEE 754, below), every machine makes *the same* error, which is why the robot's answer is universal. The lesson every programmer learns: **never test floating-point values for exact equality; compare within a small tolerance.**

> [!warning] When rounding error kills — the Patriot missile (1991)
> A Patriot air-defence battery tracked time in tenths of a second — repeatedly using $0.1$, stored in $24$ bits, so carrying exactly the truncation error above ($\approx 0.000000095$ per tick). Individually invisible; but the system had run for $100$ hours, and the drift accumulated to $0.34$ seconds. A Scud missile travels half a kilometre in that time. The interceptor looked in the wrong part of the sky, the Scud struck a barracks in Dhahran, and $28$ soldiers died. Finite mantissas have real consequences.

---

## Worked examples

**Example 1 — decode.** Mantissa `01010000`, exponent `00000010`.
$0.1010000_2 = \tfrac12 + \tfrac18 = 0.625$; exponent $+2$; value $= 0.625 \times 4 = \mathbf{2.5}$.

**Example 2 — encode $-2.75$.** $2.75 = 10.11_2 = 0.1011_2 \times 2^2$. Positive mantissa `01011000`; negate for the minus sign: invert `10100111`, $+1$ → `10101000`; check $1.0101000_2 = -1 + \tfrac14 + \tfrac1{16} = -0.6875$, and $-0.6875 \times 2^2 = -2.75$. ✓ Result: mantissa `10101000`, exponent `00000010`.

**Example 3 — normalise.** `0.0001101` $\times\,2^{7}$: shift left $3$, exponent $-3$ → `0.1101000` $\times\,2^{4}$. Top two bits $0,1$ — normalised. (Value $0.8125 \times 16 = 13.0$.)

**Example 4 — the precision wall.** With a $7$-bit fraction, the smallest gap between normalised mantissas is $2^{-7}\approx 0.0078$ of the mantissa's scale. At exponent $+3$ (values near $6.5$) neighbouring representable numbers are $2^{-7}\times 2^{3} = 2^{-4} = 0.0625$ apart — so $6.5$ and $6.5625$ are storable but nothing between them is. Precision is *relative*: the same $7$ fraction bits give tiny gaps near $0$ and coarse gaps out at large magnitudes.

---

## The real standard — IEEE 754

The 9618 format is a teaching format. Since 1985, essentially every real chip — every CPU, every GPU, every phone — has used one standard: **IEEE 754**. It was born when Intel, designing the 8087 maths coprocessor (1980), decided its arithmetic should be "so good nobody could complain" and hired the numerical analyst **William Kahan** to design it; his draft became the standard, every rival format died out, and Kahan got the 1989 Turing Award for it. It keeps the same core idea — a fixed budget split between mantissa and exponent — but spends three clever tricks on top.

**Single precision (32 bits) = 1 sign + 8 exponent + 23 fraction:**

$$\text{value} \;=\; (-1)^{s} \;\times\; 1.f_1f_2\ldots f_{23}\,{}_2 \;\times\; 2^{\,E - 127}$$

![[ieee754-single-anatomy.svg|760]]

The three tricks, each with a reason:

1. **A separate sign bit, and a *biased* exponent.** The stored exponent $E$ is the true exponent plus $127$ (the *bias*), so the true range $-126$ to $+127$ is stored as $1$ to $254$ — always positive. Why: with the sign out front and the exponent unsigned, floats **sort like plain unsigned integers** — hardware can compare two floats with the integer comparator it already has, no float circuitry needed.
2. **The hidden bit.** With the sign stored separately, a normalised binary magnitude *always* starts $1.\ldots$ — so why waste storage on a bit that is always $1$? IEEE simply doesn't store it: the $23$ stored bits are what comes *after* the leading $1$, giving $24$ bits of precision for the price of $23$. (Notice the shape: $1.\ldots$, not 9618's $0.1\ldots$ — the normalisation window itself has moved. Heads-up below.)
3. **Special patterns.** The exponent values all-$0$s and all-$1$s are reserved:

| Exponent field | Fraction | Meaning |
|---|---|---|
| all $0$s | $0$ | $\pm 0$ |
| all $0$s | $\ne 0$ | *subnormals* — no hidden $1$; numbers fade gradually to $0$ instead of underflowing off a cliff |
| all $1$s | $0$ | $\pm\infty$ — the overflow result |
| all $1$s | $\ne 0$ | **NaN** (Not-a-Number): $0/0$, $\sqrt{-1}$, $\infty - \infty$ |

(NaN is the only value in computing that is **not equal to itself** — `x != x` is the classic test for it.)

> [!warning] Heads-up — the normalisation window has moved
> Read the two formats side by side and a quiet change jumps out. 9618 normalises a positive mantissa to `0.1…` — a value in $[\tfrac12,\, 1)$. IEEE normalises the magnitude to `1.…` — a **significand in $[1,\, 2)$**: at least $1$, strictly below $2$. That is not a typo, and neither format is "wrong": both rules mean the same thing — *slide the point right up against the first significant $1$* — they just park the point on opposite **sides** of that $1$. The factor of $2$ between the windows is absorbed by the exponent, which is why the same number carries **different exponents** in the two formats:
> $$6.5 \;=\; \underbrace{0.1101_2 \times 2^{3}}_{\text{9618: mantissa in } [\frac12,\,1)} \;=\; \underbrace{1.101_2 \times 2^{2}}_{\text{IEEE: significand in } [1,\,2)}$$
> IEEE picks $[1, 2)$ *because* it makes the hidden bit clean: with the sign stored separately, the digit before the point is a constant $1$, and a constant need not be stored. (A sharp eye will notice 9618's format hides a redundant bit too — a normalised mantissa's first fraction bit is always the *opposite* of its sign bit. But "opposite of the sign" is not a constant, so the trick is messier there, and the teaching format keeps every bit visible on purpose.)

**Worked encode — store $-6.5$ in single precision.**

1. Magnitude in binary, normalised to $1.\ldots$: $\;6.5 = 110.1_2 = 1.101_2 \times 2^2$ — exponent $2$, where the 9618 encode of the same number used $3$: the moved window at work.
2. Sign: negative, so $s = 1$.
3. Exponent field: $E = 2 + 127 = 129 = 10000001_2$.
4. Fraction: everything after the leading "$1.$" — $101$, padded to $23$ bits.

$$-6.5 \;=\; \texttt{1 10000001 10100000000000000000000} \;=\; \texttt{0xC0D00000}$$

(That hex form is what you see in a debugger — [[Number Bases|hexadecimal]] as the human-readable skin over binary, as always.)

**Worked decode — what is `0 01111100 01000000000000000000000`?**
Sign $0$ (positive); $E = 01111100_2 = 124$, so true exponent $= 124 - 127 = -3$; mantissa $= 1.01_2 = 1.25$ (hidden bit restored!). Value $= 1.25 \times 2^{-3} = \mathbf{0.15625}$.

**Double precision (64 bits) = 1 + 11 + 52**, bias $1023$: about $16$ significant decimal figures, range $\sim 10^{\pm 308}$. One consequence worth knowing: a double holds every integer up to $2^{53} = 9{,}007{,}199{,}254{,}740{,}992$ *exactly* — and then starts skipping (the gap between neighbours becomes $2$). JavaScript famously has no integer type — every JS number is an IEEE double — which is why `Number.MAX_SAFE_INTEGER` is exactly $2^{53}-1$.

### Who decided 8-and-23? (and why)

The split looks arbitrary. It isn't — it falls out of three constraints, in order:

1. **The word size comes first.** Memory buses and alignment want power-of-two sizes: $32$ and $64$ bits. One bit goes to the sign; the remaining $31$ (or $63$) are a zero-sum split between exponent and fraction.
2. **The returns are asymmetric.** An extra *fraction* bit buys a steady $\sim 0.3$ decimal digits of precision. An extra *exponent* bit **doubles the number of powers of two covered** — range grows explosively while precision grows linearly. So range saturates its usefulness fast: $8$ exponent bits already give $\sim 10^{\pm 38}$, which contains essentially every quantity in physical science (an electron's mass is $10^{-30}$ kg, the Sun's is $10^{30}$). Once the range covers the world you actually compute about, **every further bit is worth more in the mantissa** — so the mantissa takes everything that's left. The same logic explains why doubling the word to $64$ bits grew the exponent only $8 \to 11$ while the fraction leapt $23 \to 52$.
3. **The proportions were field-tested, not invented.** DEC's PDP-11 and VAX — *the* scientific workhorses of the 1970s — already used a $1+8+23$ format with a hidden bit. IEEE kept proportions that a decade of real numerical work had validated, then added the bias convention, the special values, and strict rounding rules.

And **double's split is derived from single's**, by two of Kahan's design rules: (a) the product of two $24$-bit mantissas has at most $48$ significant bits, and $52 + 1 = 53 > 48$ — so a double holds any product of two singles *exactly*; (b) the square of the largest single ($\sim 10^{38}$) is $\sim 10^{76}$, safely inside double's $10^{308}$ — so intermediate results of single-precision work can never overflow it. Double precision is sized, quite literally, *to be a safe workbench for single-precision data*.

---

## Precision is silicon — GPUs, CPUs, and the AI race downward

The range-vs-precision trade-off is not just an exam talking point. It is a **market worth trillions**, and the causal chain runs through silicon area.

**A double costs four singles.** Adding two mantissas needs circuitry that grows *linearly* with their width — but multiplying them (and every floating-point multiply must multiply mantissas) needs a grid of partial products that grows with the **square** of the width. $53^2 / 24^2 \approx 4.9$: one double-precision multiplier occupies the silicon of nearly *five* single-precision multipliers. On a chip of fixed size, every FP64 unit you install evicts several FP32 units. That single fact drives everything below.

![[float-precision-ladder.svg|760]]

**GPUs — a market sorted by mantissa width.** Graphics needs only FP32: $7$ significant figures is far below a pixel, and colour channels are $8$–$10$ bits anyway. So consumer GPUs are FP32 farms with a token sprinkle of FP64 — AMD's gaming chips run doubles at $\tfrac1{16}$ the FP32 rate, NVIDIA's at $\tfrac1{64}$: just enough for software compatibility, useless for real FP64 work. Science is the opposite: a climate model or an orbital simulation runs *millions of timesteps* and rounding errors compound at every one, so it genuinely needs FP64 — and the datacenter cards built for it (H100, MI300) keep FP64 at a full $\tfrac12$ of the FP32 rate, at ten times the price. The chain of causality: **FP64 is physically expensive (the square law) → only some buyers truly need it → vendors build two die designs → the FP64 ratio *is* the product segmentation.** Games even show you the FP32 precision wall directly: a `float` carries $\sim 7$ digits, so a spacecraft $10^7$ metres from the origin has its position quantised in steps of half a metre — early *Kerbal Space Program* ships far from the origin jittered and tore themselves apart (players named the bug the **Deep Space Kraken**) until the developers moved the coordinate origin along with the ship.

**AI — the race to fewer bits.** Neural networks flipped the race's direction. Two causes: **(1)** networks are noise-tolerant — training by stochastic gradient descent *is* controlled noise, so the seventh significant figure of a weight carries no information; **(2)** the bottleneck is not arithmetic but **memory bandwidth** — the chip spends its time hauling billions of weights from memory to the multipliers. Halve the bits per weight and *everything* doubles: weights per second through the bus, weights per cache, multipliers per mm². Hence the ladder downward:

- **Training** needs *range*, not digits: gradients span $10^{-8}$ to $10^{3}$, and underflowing them to $0$ stops learning. So Google's **bfloat16** keeps FP32's full $8$-bit exponent and chops the fraction to $7$ bits — the exam question "more exponent or more mantissa?" answered in production silicon: *for AI, range wins*.
- **Inference** (running a trained model) tolerates even less: the weights are frozen, a forward pass is a single shot, and each layer's nonlinearity squashes small errors instead of compounding them. Deployed models routinely run in **INT8 and even INT4** — $16$ distinct values per weight — with FP8/FP4 formats now built into the newest accelerators. The chatbots of the world run on arithmetic with two significant figures.

**CPUs too.** The A-Level model of a processor has one ALU doing the maths ([[CPU Architecture and the Fetch-Execute Cycle]]). Real CPUs outgrew that decades ago: a dedicated floating-point unit has been standard since the early 1990s, and its share of the die keeps growing. The cause is the **power wall**: around 2005, clock speeds hit $\sim 4$–$5$ GHz and stopped (heat grows faster than speed), while Moore's law kept delivering transistors. If you can't run *faster*, run **wider** — so Intel and AMD spent the transistors on SIMD vector units that apply one instruction to many floats at once: SSE ($128$-bit — $4$ singles per instruction), then AVX/AVX2 ($256$-bit — $8$), then AVX-512 ($16$); Apple's M-series does the same with NEON vector units plus dedicated matrix hardware. Same two forces as the GPUs: FP-hungry markets (games, media, science, now AI) pulling, the clock wall pushing.

---

## Fixing it — the exact-arithmetic menu

The robot check exposed the disease: decimal fractions recur in binary, and a finite mantissa must cut them short. So what do engineers do when *wrong is not an option* — when the number is money, or a proof? There are four families of cures, and each pays for exactness in a different currency: **speed, silicon, memory, or generality**. There is no fifth cure that costs nothing; if there were, floats would not exist.

### Cure 1 — change the base: BCD and decimal floats

If binary can't say $0.1$, compute in decimal. **Binary-coded decimal (BCD)** stores each decimal digit in its own **nibble** ($4$ bits), using only the patterns `0000`–`1001` for the digits $0$–$9$:

$$429 \;=\; \underbrace{\texttt{0100}}_{4}\ \underbrace{\texttt{0010}}_{2}\ \underbrace{\texttt{1001}}_{9}\ \text{(BCD)} \qquad\text{vs.}\qquad 429 = 110101101_2\ \text{(pure binary)}$$

Now $0.1$ is just "digit $1$, one place after the point" — **exact by construction**, because the machine's digits *are* the accountant's digits. This is why a thirty-yuan pocket calculator gets $0.1 + 0.2$ right while your laptop's floating-point hardware gets it wrong: calculators compute in BCD. (So do digital clocks and most chips driving seven-segment displays — each nibble maps straight onto one digit of the readout.)

The costs are real, though:

- **Wasted patterns.** A nibble has $16$ patterns; BCD uses $10$ of them. A decimal digit carries $\log_2 10 \approx 3.32$ bits of information but occupies $4$ — roughly $17\%$ of the storage buys nothing.
- **Clumsy arithmetic.** A binary adder doesn't know about decimal: $8 + 5$ gives `1000 + 0101 = 1101` ($13$ — not a valid digit). The hardware must detect any nibble above $9$ and add a correction of $6$ (`0110`), carrying into the next nibble: `0001 0011` — digits $1,3$. ✓ Every addition drags this check-and-fix step along: slower, and more silicon per digit.

The modern descendant: in 2008, IEEE 754 gained **decimal floating-point** formats (decimal64, decimal128), and IBM's mainframes implement them *in hardware* — because the world's banks are legally required to round the way a human accountant does. In software the same idea appears wherever money touches code: SQL's `DECIMAL` columns, Python's `decimal` module, Java's `BigDecimal`.

> [!warning] Changing base doesn't abolish recurrence — it relocates it
> $\tfrac13$ recurs in decimal exactly as $\tfrac1{10}$ recurs in binary. What decimal arithmetic buys is not "no error" but **the same error a human bookkeeper would make** — the rounding lands where tax law, regulators, and customers expect it.

### Cure 2 — banish fractions: integers in the smallest unit

The cleanest fix of all: pick a unit small enough that every value you will ever store is a **whole number**. Shops don't store £$1.99$ — they store $199$ *pence*, and integer arithmetic is exact (up to $2^{53}$ even inside a double, further with $64$-bit integers). Bitcoin takes this to its logical end: the protocol contains no floats at all — every amount is an integer count of *satoshis* ($10^{-8}$ BTC). The fixed-point representation from the top is this same idea wired into a bit layout.

The price is **generality**: you must choose the unit in advance, and the moment the maths steps off the grid — a square root, a percentage, an average — you are back among fractions.

### Cure 3 — store the structure, not the digits

$\tfrac13$'s decimal expansion is infinite, but the *fraction* $\tfrac13$ is just two small integers. **Rational arithmetic** stores every number as $\tfrac{p}{q}$ and adds, subtracts, multiplies and divides *exactly* — in Python, `Fraction(1,10) + Fraction(2,10) == Fraction(3,10)` is simply `True`. Computer-algebra systems go further and keep even irrationals as **symbols**: $\sqrt2$ stays $\sqrt2$, and squares to exactly $2$. (A calculator's "exact mode", answering in fractions and surds, is this cure living in your pencil case.)

The price is **memory and speed**: adding fractions multiplies denominators, and after a few thousand operations $q$ can be thousands of digits long. Fine for a proof; hopeless for a physics engine at $60$ frames per second.

### Cure 4 — keep the floats, tame the error

Usually speed wins, so engineers keep IEEE floats and manage the error the way a physicist manages experimental uncertainty ([[Significant Figures]]):

- **Tolerance comparison** — the rule from earlier: never `==`, always "equal within a small epsilon".
- **Kahan summation** — when adding a long list of floats, each addition drops the low-order bits of the smaller number. Keep a second *compensation* variable that catches what the last addition lost and feeds it back into the next, and the drift almost vanishes. It is the same **William Kahan**: the man who designed the standard also taught the world how to add safely inside it.
- **Interval arithmetic** — compute with a guaranteed pair $[\text{low},\, \text{high}]$ instead of a single value, rounding the low end down and the high end up, so the true answer is *certain* to lie inside. If the final interval is thin, every digit it pins down is trustworthy — this is how computer-assisted proofs (like Hales' proof of the Kepler sphere-packing conjecture) turn floating-point hardware into mathematical rigour.

**It's a menu, not a ladder.** None of these is "the best": banks compute in decimal, games in floats, cryptography in pure integers, proofs in intervals and symbols. Choosing well is a whole discipline — numerical analysis — but the one-line summary is this: floats answer "$0.1+0.2$?" *fast*; if you need it *right*, you pay — in bits, in silicon, or in time.

---

## Exam Notes

### Cambridge 9618 (A-Level)

**Syllabus ref 13.3 — Floating-point representation.** Expect to:

- **Convert both ways** between a denary real number and its normalised floating-point form, given the mantissa/exponent sizes and told both fields are two's complement. (Practise until the "binary → slide the point → pad → two's-complement the exponent" routine is automatic.)
- **Normalise** a given (un-normalised or negative) mantissa, adjusting the exponent — the rule is "sign bit and next bit differ" (`0.1…` / `1.0…`).
- Explain the **range vs precision trade-off** when the split between mantissa and exponent bits is changed (more mantissa → precision; more exponent → range).
- Identify **overflow / underflow** from an exponent that won't fit, and explain **rounding errors** as the finite mantissa forcing approximation.

**Common mark-losers:** forgetting the mantissa's point is *after the sign bit* (so `0.1…` is $\tfrac12$, not $1$); normalising a negative number to `1.1…` instead of `1.0…`; giving the exponent in sign-and-magnitude instead of two's complement; claiming a stored float is *exact*; and **importing IEEE 754 into a 9618 answer** — no bias, no hidden bit, no separate sign bit on the exam, and above all no normalising to `1.…`: the 9618 window is $[\tfrac12, 1)$, so a positive mantissa is `0.1…`, and the exponent is one *bigger* than the IEEE exponent for the same value. Both fields are plain two's complement, full stop.

**Also on the AS paper — §1.1 names BCD.** Expect to: represent a denary integer in **binary-coded decimal** (each digit in its own nibble, `0000`–`1001`), convert back, and state *where and why* BCD is used (exact decimal values — currency, calculators, digit displays). The exact-arithmetic menu above carries the full story; for the exam, nibble-per-digit conversion is the skill.

> [!info] Beyond syllabus
> The IEEE 754 and precision-economics sections, and most of the exact-arithmetic menu, are enrichment: 9618 examines only the two's-complement teaching format (§13.3) plus BCD (§1.1). But the enrichment is where the topic becomes real — IEEE 754 is what every device you own actually runs, and the precision economics is a live industry story.

---

### IB Computer Science

Not a named statement: A1.2's confirmed wording covers binary/hexadecimal conversion and logic gates — floating-point representation sits beyond every published outline (as with the rest of the machine-arithmetic family). The why-0.1-plus-0.2-misbehaves intuition still pays in any IB programming scenario touching real numbers.

## Connections

- **Prerequisite:** [[Number Bases]] — binary place value, extended past the point into fractions ($0.1_2 = \tfrac12$).
- **Prerequisite:** [[Two's Complement]] — both the mantissa and the exponent are two's-complement numbers; negating a mantissa is the same invert-and-add-1.
- **Prerequisite / sequel:** [[Overflow and Underflow]] — the integer wrap generalises here to exponent overflow ($\to\pm\infty$) and underflow ($\to 0$).
- **Sibling (decimal analogue):** [[Standard Form (Vocab)]] — floating point *is* scientific notation, in base 2.
- **Hardware sequel:** [[CPU Architecture and the Fetch-Execute Cycle]] — the exam model gives the processor one ALU; real dies grew a floating-point unit and ever-wider vector engines, because precision economics decides what silicon gets built.
- **Application:** rounding error is why numerical algorithms need care — cf. [[Numerical Methods]] (fixed-point iteration, error accumulation) and [[Significant Figures]] (the same "how many digits are real" question in physics).

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $m \times 2^{e}$ | `m \times 2^{e}` | mantissa $\times$ 2 to the exponent — a floating-point value |
| $0.1101_2$ | `0.1101_2` | a binary fraction (point after the sign bit) |
| $2^{-1}, 2^{-2}$ | `2^{-1}` | negative powers of two — the fraction place values $\tfrac12, \tfrac14, \dots$ |
| $[-1, 1)$ | `[-1, 1)` | half-open interval — the range of an 8-bit two's-complement mantissa |
| $\pm\infty$ | `\pm\infty` | IEEE 754 overflow result |

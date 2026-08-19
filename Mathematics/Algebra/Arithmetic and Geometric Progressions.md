---
chinese: 等差与等比数列 (děngchā yǔ děngbǐ shùliè)
prerequisites:
  - "[[Laws of Indices]]"
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Simple and Compound Interest (Vocab)]]"
  - "[[Binomial Theorem]]"
  - "[[Sequences]]"
  - "[[Stories/Gauss the Prodigy]]"
  - "[[Gauss the Prodigy]]"
  - "[[Recurring Decimals (Vocab)]]"
leads_to:
  - "[[Limit]]"
  - "[[Integration]]"
  - "[[Exponential Growth and Decay]]"
  - "[[Discrete Random Variables]]"
  - "[[Maclaurin Series]]"
  - "[[Summation of Series]]"
  - "[[Probability Generating Functions]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-12-3
  - syllabus/0606-12-4
  - syllabus/0606-12-5
  - syllabus/9709-1-6
  - type/definition
  - type/formula
  - type/proof
  - notation/subscript
  - notation/sigma
  - misconception/AP-vs-GP
  - misconception/n-vs-n-minus-1
  - misconception/r-vs-abs-r
  - misconception/infinite-sum-always-exists
---

# Arithmetic and Geometric Progressions 等差与等比数列

## Definition

### Formal

A **sequence** (数列) is an ordered list of numbers $u_1, u_2, u_3, \ldots$

A **progression** is a sequence that follows a *rule* for moving from one term to the next.

- **Arithmetic progression (AP)** 等差数列 — each term exceeds the previous by a fixed amount $d$, called the **common difference** (公差):
$$u_n = u_{n-1} + d \qquad \text{equivalently} \qquad u_n - u_{n-1} = d$$

- **Geometric progression (GP)** 等比数列 — each term is a fixed multiple $r$ of the previous, called the **common ratio** (公比):
$$u_n = r \cdot u_{n-1} \qquad \text{equivalently} \qquad \frac{u_n}{u_{n-1}} = r$$

A **series** (级数) is the sum of a sequence: $S_n = u_1 + u_2 + \cdots + u_n$.

### Intuitive

Progressions are patterns with a **repeating rule**:

- AP: "add the same thing each step" — $3, 7, 11, 15, \ldots$ (add 4)
- GP: "multiply by the same thing each step" — $3, 6, 12, 24, \ldots$ (multiply by 2)

That's literally the whole structure. The mathematics is about answering two questions:

1. **"What's the 100th term?"** — find a closed formula for $u_n$.
2. **"What's the sum of the first 100 terms?"** — find a closed formula for $S_n$.

And for GPs there's a third, more profound question: **"What if I add up *all* of them?"** Sometimes that infinite sum is a finite number. That is where progressions touch [[Limit]] and infinity.

### 中文锚点 (Chinese Anchor)

等差数列：相邻两项的**差**恒定 → 公差 $d$。
等比数列：相邻两项的**比**恒定 → 公比 $r$。

中英术语对照：

| 中文 | English | 符号 |
|---|---|---|
| 首项 | first term | $a$ 或 $u_1$ |
| 公差 | common difference | $d$ |
| 公比 | common ratio | $r$ |
| 通项公式 | $n$th term formula | $u_n$ |
| 前 $n$ 项之和 | sum of first $n$ terms | $S_n$ |
| 无穷级数 | infinite series | $S_\infty$ |
| 收敛 | convergent | $\lvert r \rvert < 1$ |
| 发散 | divergent | $\lvert r \rvert \geq 1$ |

> [!tip] 两个关键字
> 等 (děng) = equal / same. 差 (chā) = difference. 比 (bǐ) = ratio.
> So 等差 = "same difference", 等比 = "same ratio". The names literally tell you what's constant.

---

## The Bridge: sequence vs series vs progression

Students often use these three words interchangeably. They aren't the same.

| Word | Chinese | What it is | Example |
|---|---|---|---|
| **Sequence** 数列 | shùliè | Ordered list of numbers | $2, 4, 8, 16, \ldots$ |
| **Progression** | — | A sequence with a *rule* (AP, GP, etc.) | $2, 4, 8, 16, \ldots$ (GP, $r=2$) |
| **Series** 级数 | jíshù | The **sum** of a sequence | $2 + 4 + 8 + 16 + \cdots$ |

A GP is the sequence; a geometric series is the sum. The 0606 syllabus uses both words — read carefully which one the question wants.

---

## Arithmetic Progressions

### The $n$th term formula

With first term $a$ and common difference $d$:

$$\boxed{u_n = a + (n-1)d}$$

**Why $(n-1)$ and not $n$?** Because to get from $u_1$ to $u_n$ you make $n-1$ jumps of size $d$, not $n$. Walk the small cases:

$$u_1 = a, \qquad u_2 = a + d, \qquad u_3 = a + 2d, \qquad u_4 = a + 3d$$

The coefficient of $d$ is always *one less* than the subscript.

### The sum formula — Gauss's trick

$$\boxed{S_n = \tfrac{n}{2}\bigl(2a + (n-1)d\bigr) = \tfrac{n}{2}(a + \ell)}$$

where $\ell = u_n = a + (n-1)d$ is the **last** term.

> [!tip] The legend — young Gauss, 1786
> Gauss's teacher reportedly told his class to add $1 + 2 + 3 + \cdots + 100$ to keep them busy. Nine-year-old Carl wrote one number on his slate almost immediately: $5050$. His trick was to pair the first and last terms, then the second and second-to-last, and so on: $(1+100) + (2+99) + \cdots + (50+51)$. Fifty pairs, each summing to $101$. $50 \times 101 = 5050$. Whether the story is literally true or not, the method is the cleanest derivation of $S_n$ ever devised. (How much of it *is* true — the slate, the "Ligget se", and which details a century of retelling invented — is audited in [[Stories/Gauss the Prodigy]], along with the rest of the life.)

**Proof.** Write $S_n$ forwards and backwards and add:

$$
\begin{aligned}
S_n &= a \,\,+ (a + d) \,\,+ (a + 2d) \,\,+ \cdots + (a + (n-1)d) \\
S_n &= (a + (n-1)d) + (a + (n-2)d) + \cdots + \, a
\end{aligned}
$$

Every vertical column now sums to $2a + (n-1)d$ — the $d$ terms cancel. There are $n$ columns, so:

$$2S_n = n\bigl(2a + (n-1)d\bigr) \implies S_n = \tfrac{n}{2}\bigl(2a + (n-1)d\bigr). \quad\blacksquare$$

Grouping differently: $2a + (n-1)d = a + \bigl(a + (n-1)d\bigr) = a + \ell$, giving the **average-of-ends** form:

$$S_n = \tfrac{n}{2}(a + \ell)$$

which reads beautifully: *sum = (number of terms) × (average term)*. Every AP's mean is just the mean of its endpoints.

---

## Geometric Progressions

### The $n$th term formula

With first term $a$ and common ratio $r$:

$$\boxed{u_n = a \cdot r^{n-1}}$$

Same "one less" logic as AP: $n-1$ multiplications of $r$ get you from $u_1$ to $u_n$.

### The sum formula — the telescoping trick

$$\boxed{S_n = \dfrac{a(1 - r^n)}{1 - r} = \dfrac{a(r^n - 1)}{r - 1}} \qquad (r \neq 1)$$

Both forms are correct — pick whichever denominator is positive. Use the left form when $\lvert r \rvert < 1$, the right form when $r > 1$.

**Proof.** Start with the sum and multiply by $r$:

$$
\begin{aligned}
S_n &= a + ar + ar^2 + \cdots + ar^{n-1} \\
rS_n &= \phantom{a\,\,+} ar + ar^2 + \cdots + ar^{n-1} + ar^n
\end{aligned}
$$

Subtract the first line from the second. Every term in the middle cancels — the sum *telescopes*:

$$rS_n - S_n = ar^n - a$$

$$S_n(r - 1) = a(r^n - 1) \implies S_n = \dfrac{a(r^n - 1)}{r - 1}. \quad\blacksquare$$

**Special case $r = 1$.** The formula breaks (division by zero) because every term equals $a$: $S_n = na$.

> [!info] Why the trick works
> Multiplying by $r$ *shifts* the sequence forward by one slot. Subtracting kills everything except the ends — the first term drops out the bottom, the new $(n+1)$th term appears at the top. This "shift and subtract" idea reappears constantly: it's the engine behind generating functions, solving linear recurrences, and even how computers compute $\dfrac{1}{1 - r}$ as a power series.

---

## Sum to infinity — the limit that matters

What happens when $n \to \infty$? Look at $r^n$:

- If $\lvert r \rvert < 1$, then $r^n \to 0$. (Halve a number forever → it vanishes.)
- If $\lvert r \rvert > 1$, then $r^n \to \infty$. (Double a number forever → it explodes.)
- If $r = 1$, the sum is $na \to \pm\infty$ (unless $a = 0$).
- If $r = -1$, the sum **oscillates**: $a, 0, a, 0, \ldots$ — no limit exists.

Taking the limit in the sum formula when $\lvert r \rvert < 1$:

$$S_\infty = \lim_{n \to \infty} \dfrac{a(1 - r^n)}{1 - r} = \dfrac{a(1 - 0)}{1 - r}$$

$$\boxed{S_\infty = \dfrac{a}{1 - r} \qquad \text{valid only when } \lvert r \rvert < 1}$$

The condition $\lvert r \rvert < 1$ is called the **convergence condition** (收敛条件). Without it, $S_\infty$ is meaningless.

### Why this result is profound

Add infinitely many numbers → get a finite answer. That should feel strange. We're doing something our arithmetic was never designed for: summing a never-ending list. The only way this makes sense is through [[Limit]] — $S_\infty$ is *not* the sum of every term one by one (that never finishes). It is the **value the partial sums approach**.

$$S_\infty = \lim_{n \to \infty} S_n$$

Read: "the number the sums $S_1, S_2, S_3, \ldots$ march toward as $n$ grows." The limit is the bridge from *process* to *value*.

> [!tip] The unit square picture — $\tfrac{1}{2} + \tfrac{1}{4} + \tfrac{1}{8} + \cdots = 1$
> Take a square of area 1. Shade half of it. Shade half of what remains ($\tfrac{1}{4}$). Then half again ($\tfrac{1}{8}$). Keep going. The shaded area is the GP with $a = \tfrac{1}{2}$, $r = \tfrac{1}{2}$. You can *see* that the shaded region fills the whole square — never overflowing, never stopping. That picture is the proof: $S_\infty = \dfrac{1/2}{1 - 1/2} = 1$.

### Zeno's paradox, resolved

Achilles must travel 1 metre. First he covers $\tfrac{1}{2}$, then $\tfrac{1}{4}$, then $\tfrac{1}{8}$, ad infinitum. Zeno (~450 BCE) claimed this meant Achilles never arrives — he must complete infinitely many sub-journeys.

The resolution is the geometric series: the infinite sum of the distances is *finite* (it equals 1). Infinitely many steps can fit in finite time, because they shrink fast enough. The paradox dissolves once you accept that infinite sums can converge. Mathematics needed 2300 years — from Zeno to Cauchy — to formalise this.

> [!info] Beyond syllabus — the harmonic series diverges
> Not every shrinking sum converges. Try $1 + \tfrac{1}{2} + \tfrac{1}{3} + \tfrac{1}{4} + \cdots$ (the **harmonic series**). The terms shrink to zero, but the sum is **infinite**. Group them: $\tfrac{1}{3} + \tfrac{1}{4} > \tfrac{1}{2}$; $\tfrac{1}{5} + \tfrac{1}{6} + \tfrac{1}{7} + \tfrac{1}{8} > \tfrac{1}{2}$; the next 8 terms > $\tfrac{1}{2}$; and so on. You can always find another block summing to more than $\tfrac{1}{2}$, so the total grows without bound. *Moral: "terms go to zero" is necessary but not sufficient for convergence.* Full convergence theory (ratio test, integral test) comes at university level.

> [!info] Beyond syllabus — geometric → exponential
> The compound interest formula $P(1 + r)^n$ is a GP in $n$. Let the compounding happen $k$ times per year and take $k \to \infty$: the GP limits to the continuous exponential $Pe^{rt}$. That limit is the bridge from the discrete world of progressions to the continuous world of [[Exponential Growth and Decay]] — written up in full there. It's the same story as Zeno's: shrinking pieces, continuous limit.

---

## Worked Examples

### Example 1 (0606 §12.4): AP — find $n$ given $S_n$

The first term of an AP is $5$ and the common difference is $3$. For which $n$ does $S_n = 440$?

**Setup.** $a = 5$, $d = 3$. Use $S_n = \tfrac{n}{2}\bigl(2a + (n-1)d\bigr)$:

$$440 = \tfrac{n}{2}\bigl(10 + 3(n-1)\bigr) = \tfrac{n}{2}(3n + 7)$$

$$880 = n(3n + 7) \implies 3n^2 + 7n - 880 = 0$$

Quadratic formula (or factorising): $n = \dfrac{-7 \pm \sqrt{49 + 10560}}{6} = \dfrac{-7 \pm 103}{6}$

So $n = 16$ or $n = -\tfrac{110}{6}$. Reject the negative; $\boxed{n = 16}$.

### Example 2 (0606 §12.4): GP — partial sum

A GP has first term $2$ and common ratio $3$. Find the sum of the first 8 terms.

$$S_8 = \dfrac{2(3^8 - 1)}{3 - 1} = \dfrac{2(6561 - 1)}{2} = 6560$$

$$\boxed{S_8 = 6560}$$

### Example 3 (0606 §12.5): Sum to infinity

The sum to infinity of a GP is $\tfrac{27}{2}$, and the first term is $9$. Find $r$, and check convergence.

$$\dfrac{27}{2} = \dfrac{9}{1 - r} \implies 27(1 - r) = 18 \implies 1 - r = \tfrac{2}{3} \implies r = \tfrac{1}{3}$$

Check: $\lvert r \rvert = \tfrac{1}{3} < 1$ ✓, so the infinite sum is valid. $\boxed{r = \tfrac{1}{3}}$.

### Example 4 (A-Level / IB AA): recurring decimal as a GP

Show that $0.\overline{27} = \tfrac{3}{11}$.

$$0.\overline{27} = 0.272727\ldots = \dfrac{27}{100} + \dfrac{27}{10000} + \dfrac{27}{1000000} + \cdots$$

This is a GP with $a = \dfrac{27}{100}$, $r = \dfrac{1}{100}$. Since $\lvert r \rvert < 1$:

$$S_\infty = \dfrac{27/100}{1 - 1/100} = \dfrac{27/100}{99/100} = \dfrac{27}{99} = \dfrac{3}{11} \quad\blacksquare$$

This is the algebraic machine behind every "fraction from a recurring decimal" problem — and the proof that $0.\overline{9} = 1$.

---

## Common Misconceptions (Teaching Notes)

### 1. Confusing AP and GP

Students see $2, 4, 6, 8$ and $2, 4, 8, 16$ and aren't sure which is which. Both "grow by jumping."

**Fix.** Compute *both* the difference and the ratio for the first two pairs:

- $2, 4, 6, 8$: differences $2, 2, 2$ → AP. Ratios $2, 1.5, 1.33$ → not a GP.
- $2, 4, 8, 16$: differences $2, 4, 8$ → not an AP. Ratios $2, 2, 2$ → GP.

If the **difference** stays constant, it's AP; if the **ratio** stays constant, it's GP.

### 2. The $n$ vs $n-1$ slip

Writing $u_n = a + nd$ instead of $u_n = a + (n-1)d$. This bug gets the first term wrong: $u_1 = a + d$ instead of $u_1 = a$.

**Fix.** Always check $u_1$: plug $n = 1$ into your formula. If it doesn't give back $a$, you wrote it wrong.

### 3. Using $r$ instead of $\lvert r \rvert$ for convergence

Students write "converges when $r < 1$", which wrongly includes $r = -2$ (since $-2 < 1$). The correct condition is $\lvert r \rvert < 1$, i.e. $-1 < r < 1$.

**Fix.** Ask: does the sum $1 - 2 + 4 - 8 + 16 - \cdots$ converge? Terms don't even shrink, so clearly no. The absolute value test catches both the too-big-positive and too-big-negative cases in one go.

### 4. Assuming infinite sums always exist

After meeting $\tfrac{1}{2} + \tfrac{1}{4} + \tfrac{1}{8} + \cdots = 1$, some students believe every sum "goes to some number." Then they write $1 + 2 + 3 + \cdots = $ some finite value, or — worse — manipulate $1 - 1 + 1 - 1 + \cdots$ to equal $\tfrac{1}{2}$ (Grandi's series).

**Fix.** Hammer the convergence condition. $S_\infty$ is only defined when $\lvert r \rvert < 1$. If the condition fails, **do not write** $S_\infty$. The fancy-looking manipulations in divergent series are a genuine research topic (called "summation methods") but completely off-syllabus — and dangerous to copy without the theory.

### 5. Forgetting the index

Writing $S_n = \tfrac{n}{2}(2a + nd)$ — off by one. Or using $u_n = ar^n$ instead of $ar^{n-1}$.

**Fix.** Every progression formula has a "$n$ minus one" somewhere because the first term is the *zeroth* jump. When in doubt, test with $n = 1$: $u_1$ must equal $a$, $S_1$ must equal $a$.

---

## Exam Notes

### Memorise? — per board

The four-board exam-strategy table for AP/GP. Same legend as [[Standard Integrals]]: ✅ given on booklet, 📝 must memorise, 🛠 derive, ⚪ off-syllabus. Sources: [[MF19 Reference (9709)]], [[Edexcel IAL Reference]], [[OxAQA 9660 Reference]], [[AP Calculus Reference]].

| Formula | 9709 | IAL | 9660 | AP |
|---|:---:|:---:|:---:|:---:|
| **AP $n$-th term** $u_n = a + (n-1)d$ | ✅ | ✅ | ✅ | 📝 |
| **AP sum** $S_n = \tfrac{1}{2}n(a + l) = \tfrac{1}{2}n[2a + (n-1)d]$ | ✅ | ✅ | ✅ | 📝 |
| **GP $n$-th term** $u_n = ar^{n-1}$ | ✅ | ✅ | ✅ | 📝 |
| **GP finite sum** $S_n = \dfrac{a(1 - r^n)}{1 - r}$ | ✅ | ✅ | ✅ | 📝 |
| **GP sum to infinity** $S_\infty = \dfrac{a}{1 - r}$ for $\lvert r \rvert < 1$ | ✅ | ✅ | ✅ | 📝 |
| **$\sum_{r=1}^n r$** $= \tfrac{1}{2}n(n+1)$ | 🛠 from AP sum | ⚪ FP1 only | ✅ | 📝 |
| **$\sum_{r=1}^n r^2$** $= \tfrac{1}{6}n(n+1)(2n+1)$ | ⚪ 9231 only | ⚪ FP1 only | ✅ | 📝 |
| **$\sum_{r=1}^n r^3$** $= \tfrac{1}{4}n^2(n+1)^2$ | ⚪ 9231 only | ⚪ FP1 only | ✅ | 📝 |
| **Convergence condition** $\lvert r \rvert < 1$ for $S_\infty$ | ✅ (with formula) | ✅ | ✅ | 📝 |

> [!info] AP/GP is the most universally generous topic on the formula sheets
> All four boards print the AP and GP $n$-th term + finite sum + infinite sum on their booklets — except AP, which prints nothing. **An AP Calculus BC student is the only one who must memorise the basic AP/GP suite cold.** AP students typically don't *need* the AP/GP formulas as one-liners — they're embedded in the larger Unit 10 series-convergence apparatus, where the geometric-series convergence is the archetype but the sum formulas are recalled inline.
>
> **OxAQA 9660 is uniquely generous on the $\sum r^k$ formulas** (linear, quadratic, cubic). Cambridge keeps these for 9231 Further Math; IAL keeps them for FP1 Further; AP must memorise. *9660 students get the cleanest start on induction-style summation problems.*

---

### Cambridge 0606

**Syllabus ref:** §12.3 (recognise AP and GP), §12.4 ($n$th term and sum of first $n$ terms), §12.5 (convergent GP: convergence condition and sum to infinity).

A single deep card covers all three. Typical question patterns:

- Given two terms, find $a$ and $d$ (or $a$ and $r$), then compute $u_n$ or $S_n$.
- Given $S_n$ or $S_\infty$ and one parameter, solve for the other — usually reducing to a quadratic or linear equation in $r$.
- Word problems: population, depreciation, recurring decimals.
- Mixed AP+GP: a number is the $k$th term of an AP and the $m$th term of a GP — form simultaneous equations.

**Mark-scheme patterns:**
- Stating the correct formula is worth a mark even if the arithmetic later errs.
- On convergence questions, state the condition $\lvert r \rvert < 1$ explicitly — examiners award a mark for it.

### Cambridge 9709 — **Pure Mathematics 1, §1.6 Series**

Paper 1 is compulsory for both AS and A Level, and §1.6 has four learning objectives — the binomial expansion (which [[Binomial Theorem]] carries) plus **three that are entirely AP/GP**:

- **Recognise arithmetic and geometric progressions.**
- **Use the formulae for the $n$th term and the sum of the first $n$ terms to solve problems**, with the syllabus adding a specific piece of knowledge candidates are expected to have: numbers $a, b, c$ are in **arithmetic** progression if $2b = a+c$, and in **geometric** progression if $b^2 = ac$ *(or equivalent)*. It also warns that **questions may involve more than one progression**.
- **Use the condition for convergence of a geometric progression, and the formula for the sum to infinity.**

> [!tip] Where $2b = a+c$ and $b^2 = ac$ come from — and why the means are named after them
> Both conditions just say *the middle term is the middle*. In an AP the steps either side are equal, so $b - a = c - b$, which rearranges to $2b = a+c$, i.e. $b = \frac{a+c}{2}$ — the **arithmetic mean**. In a GP the ratios either side are equal, so $\frac{b}{a} = \frac{c}{b}$, giving $b^2 = ac$, i.e. $b = \sqrt{ac}$ — the **geometric mean**. The two familiar averages are named after these two progressions, not the other way round; and the classical inequality $\frac{a+c}{2} \geqslant \sqrt{ac}$ says an AP's middle term always sits at least as high as the matching GP's.
>
> In the exam these are the fastest route into a *"the first, fourth and eighth terms of an AP form a GP"* question: write the three terms in $a$ and $d$, apply $b^2 = ac$, and one equation falls out instead of three.

**What the syllabus explicitly does not require** on this section: knowledge of the greatest term, and properties of the binomial coefficients. Both are common textbook extras that cost revision time for no marks.

### Other A-Level specifications

Edexcel, AQA and OCR place the same content in their Pure 2 papers, and add:
- $\sum$-notation proficiency: $\displaystyle\sum_{k=1}^{n} u_k$.
- Proof of the $S_n$ formulas by induction (in the Further Mathematics options — [[Proof by Induction]]).
- Mixed arithmetic-and-geometric problems as a standard question type.

### IB AA

IB Mathematics AA (SL and HL) treats AP/GP as Topic 1.2/1.3.
- SL: covers through sum to infinity, plus compound interest applications.
- HL: adds the rigorous convergence argument, the power-series definition of $e$ via the limit of a GP-like expression, and Taylor series (where GP convergence is the archetype for radius-of-convergence).

### AP

- **AP Precalculus:** arithmetic and geometric sequences, partial sums, convergence of GPs.
- **AP Calculus BC (Unit 10):** geometric series are the first convergent series studied; the $\lvert r \rvert < 1$ condition motivates the full convergence-test suite (ratio test, integral test, $p$-series, etc.).

### Cambridge 0580

Not covered at the progression level — 0580 handles sequences at the $n$th-term-formula level via [[Sequences]] (A24–A26), without the AP/GP vocabulary or infinite sums.

---

## Connections

- **Prerequisite:** [[Laws of Indices]] — $r^{n-1}$ manipulation in GP
- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — term-manipulation vocabulary
- **Prerequisite:** [[Simple and Compound Interest (Vocab)]] — compound interest IS a GP; forms the student's real-world anchor
- **Related:** [[Binomial Theorem]] — expansions are finite series; extends to infinite power series at A-Level
- **Leads to:** [[Limit]] — $S_\infty = \lim_{n\to\infty} S_n$ is the gateway limit for most students
- **Leads to:** [[Sequences]] — the broader theory of number sequences (non-progression cases)
- **Leads to:** [[Integration]] — definite integral = $\lim$ of a Riemann sum, conceptually the continuous version of the GP sum story
- **Application:** [[Exponential Growth and Decay]] — continuous limit of a GP; the $k \to \infty$ compounding bridge
- **Physics bridge — reserved:** [[Simple Harmonic Motion]] — damped oscillations have geometric-progression amplitudes; the amplitude ratio of successive peaks is the logarithmic decrement
- **CS bridge — reserved:** [[Recursion]] — AP and GP are linear recurrences of order 1; generalising to higher order gives Fibonacci and the whole recurrence-solving toolkit

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $u_n$ | `u_n` | $n$th term |
| $a, d$ | `a, d` | first term, common difference (AP) |
| $a, r$ | `a, r` | first term, common ratio (GP) |
| $S_n$ | `S_n` | sum of first $n$ terms |
| $S_\infty$ | `S_\infty` | sum to infinity |
| $\lvert r \rvert < 1$ | `\lvert r \rvert < 1` | convergence condition — use `\lvert \rvert` not `|` |
| $\lim_{n\to\infty}$ | `\lim_{n\to\infty}` | limit as $n$ grows unboundedly |
| $\displaystyle\sum_{k=1}^{n} u_k$ | `\sum_{k=1}^{n} u_k` | sigma notation for a finite sum |
| $r^{n-1}$ | `r^{n-1}` | brace the exponent — `r^n-1` renders as $r^n - 1$ |
| $\dfrac{a}{1-r}$ | `\dfrac{a}{1-r}` | sum to infinity (inline-sized fraction) |

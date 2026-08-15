---
chinese: 多项式除法 (duōxiàngshì chúfǎ)
prerequisites:
  - "[[Remainder and Factor Theorems]]"
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Algebraic Fractions (Vocab)]]"
leads_to:
  - "[[Symmetric Functions of Roots]]"
  - "[[Partial Fractions]]"
  - "[[Binomial Series]]"
  - "[[Cubic Equations]]"
  - "[[Rational Functions and Graphs]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-3-1
  - syllabus/0606-3-2
  - syllabus/9709-3-1
  - syllabus/9709-2-1
  - type/technique
  - type/algorithm
  - notation/polynomial
  - misconception/skipping-missing-terms
  - misconception/sign-flip-in-subtraction
  - misconception/dividing-each-term
---

# Polynomial Division 多项式除法

## Definition

### Formal

Given two polynomials $P(x)$ (the **dividend**) and $D(x)$ (the **divisor**) with $\deg D \geq 1$ and $D(x) \not\equiv 0$, there exist unique polynomials $Q(x)$ (the **quotient**) and $R(x)$ (the **remainder**) such that

$$\boxed{\;P(x) = D(x)\,Q(x) + R(x), \qquad \deg R < \deg D\;}$$

The constraint $\deg R < \deg D$ is what makes $Q$ and $R$ unique — without it, you could shovel any amount of $D(x)$ between them.

### Intuitive

This is the polynomial version of integer division. When you divide $17$ by $5$, you write $17 = 5 \times 3 + 2$ — quotient $3$, remainder $2$, and the remainder must be smaller than the divisor. Polynomials are the same: divide $P$ by $D$, get a quotient and remainder, and the remainder must have *smaller degree* than the divisor.

The [[Remainder and Factor Theorems]] handle one important special case — when the divisor is linear, $D(x) = x - a$. There the remainder is just a number, $R = P(a)$, and you can read it off without doing any long division. Polynomial Division is the general algorithm: it works for **any** divisor — quadratic, cubic, ones with missing terms, ones with awkward leading coefficients. When the Factor Theorem can't help, this is the tool.

The other reason to learn it: **partial fractions**. To split $\dfrac{P(x)}{D(x)}$ into a sum of simpler fractions, the numerator's degree must be less than the denominator's. If it isn't, you have to polynomial-divide first to peel off a polynomial part, leaving a *proper* rational expression behind. That's the gateway problem of [[Partial Fractions]] (9709 P3 §3.1).

### 中文锚点

**多项式除法**（duōxiàngshì chúfǎ）：把多项式 $P(x)$ 除以多项式 $D(x)$，得到商式 $Q(x)$ 和余式 $R(x)$，满足

$$P(x) = D(x)\,Q(x) + R(x), \qquad \deg R < \deg D$$

跟整数除法一模一样：$17 \div 5 = 3 \cdots 2$，写成 $17 = 5 \times 3 + 2$；余数小于除数。多项式版本的"小于"指的是次数。

**为什么学这个？** [[Remainder and Factor Theorems|余式定理]]只在除数是 $(x - a)$ 这种一次式时给捷径。如果除数是 $x^2 + 1$，或者你需要把假分式 $\dfrac{x^3 + 2x}{x^2 - 1}$ 拆成多项式加真分式（[[Partial Fractions|部分分式]]的第一步），就必须用长除法。

中文教材里常叫"多项式长除法"或"竖式除法"，写法与英语一致，只是符号偏好不同。

---

## §1 The Division Identity — General Form

For integers, dividing $a$ by $b$ produces $a = bq + r$ with $0 \leq r < b$. For polynomials, replace "less than" by "smaller degree":

$$P(x) = D(x)\,Q(x) + R(x), \qquad \deg R(x) < \deg D(x)$$

Two structural consequences:

1. **The remainder's shape is fixed by the divisor's degree.**
   If $\deg D = 1$ (linear divisor), then $\deg R < 1$, so $R$ is a *constant*. That's the setting of the Remainder Theorem.
   If $\deg D = 2$ (quadratic divisor), then $\deg R \leq 1$, so $R$ is *linear or constant* — $R(x) = \alpha x + \beta$.
   In general, dividing by a degree-$d$ divisor leaves a remainder of degree at most $d - 1$.

2. **The quotient's degree is determined too.** $\deg Q = \deg P - \deg D$ (assuming $P$ doesn't completely vanish). So dividing a degree-$5$ polynomial by a degree-$2$ polynomial produces a degree-$3$ quotient and an at-most-degree-$1$ remainder.

> [!tip] Proper vs improper rational expressions
> A rational expression $\dfrac{P(x)}{D(x)}$ is **proper** if $\deg P < \deg D$ and **improper** if $\deg P \geq \deg D$. Polynomial division converts an improper one into a polynomial plus a proper one:
>
> $$\dfrac{P(x)}{D(x)} = Q(x) + \dfrac{R(x)}{D(x)}.$$
>
> This is exactly what [[Partial Fractions|partial fractions]] needs as input. If your starting fraction is improper, *long-divide first*, then decompose the proper-fraction leftover.

---

## §2 The Long Division Algorithm

The procedure is mechanical and looks identical to the long-division layout you learned for integers in primary school. Set it up as a tableau:

$$\require{enclose}
\begin{array}{rl}
& Q(x) \\[-1pt]
D(x) \enclose{longdiv}{P(x)} \\[-1pt]
\end{array}$$

Then loop:

> **At each step:** divide the *leading term* of the current dividend by the *leading term* of the divisor → write that next piece of $Q$ → multiply it back through $D$ → subtract → repeat until the leading remainder has degree below $\deg D$.

Five micro-steps per iteration:

1. **Leading-term divide.** Look at the leading term of what's currently sitting under the bar. Divide it by the leading term of $D(x)$. The result is the next term of $Q(x)$.
2. **Write it on top.** Place the new $Q$-term in the same column as the matching power above the bar.
3. **Multiply back.** Multiply the new $Q$-term by *every* term of $D(x)$.
4. **Subtract.** Line up the product underneath the dividend and subtract — column by column, like integer long division. *Sign flip happens here.*
5. **Bring down.** Bring down the next term of the dividend if there is one, and loop.

Stop when the running dividend has degree strictly less than $\deg D$. What's left is $R(x)$.

> [!warning] Two things to watch
> - **Missing terms.** Always rewrite $P(x)$ with every power explicit, including zero coefficients. $x^4 - 1$ becomes $x^4 + 0x^3 + 0x^2 + 0x - 1$. Skipping the zeros is the most common source of arithmetic errors in this algorithm.
> - **Sign flip in the subtraction.** When you subtract $D(x) \cdot Q\text{-term}$, every sign flips. $-(2x^2 - 3x + 1) = -2x^2 + 3x - 1$. Half of all student errors live in this single subtraction step.

### Why does this terminate?

Each iteration produces a new $Q$-term of degree $(\deg \text{current dividend}) - \deg D$, and the subtraction *kills the leading term* of the current dividend by construction. So after one iteration the running dividend's degree has dropped by at least one. Since degrees are non-negative integers, the process must terminate, and it terminates exactly when the running dividend's degree falls below $\deg D$.

---

## §3 Worked Example — The Standard Procedure

Divide $P(x) = 2x^3 - 3x^2 + 4x - 5$ by $D(x) = x^2 + x - 1$.

**Setup.** $\deg P = 3$, $\deg D = 2$, so the quotient will have degree $1$ and the remainder will have degree at most $1$.

**Iteration 1.**

- Leading term of dividend: $2x^3$. Leading term of divisor: $x^2$. Divide: $\dfrac{2x^3}{x^2} = 2x$. So the first term of $Q$ is $\boxed{2x}$.
- Multiply back: $2x \cdot (x^2 + x - 1) = 2x^3 + 2x^2 - 2x$.
- Subtract from the dividend:

$$(2x^3 - 3x^2 + 4x - 5) - (2x^3 + 2x^2 - 2x) = -5x^2 + 6x - 5.$$

The new running dividend is $-5x^2 + 6x - 5$. Its degree is $2 \geq \deg D = 2$, so we keep going.

**Iteration 2.**

- Leading term: $-5x^2$. Divide by $x^2$: $\dfrac{-5x^2}{x^2} = -5$. So the next term of $Q$ is $\boxed{-5}$.
- Multiply back: $-5 \cdot (x^2 + x - 1) = -5x^2 - 5x + 5$.
- Subtract:

$$(-5x^2 + 6x - 5) - (-5x^2 - 5x + 5) = 11x - 10.$$

The new running dividend is $11x - 10$. Its degree is $1 < \deg D = 2$, so we stop.

**Answer.**

$$Q(x) = 2x - 5, \qquad R(x) = 11x - 10.$$

**Sanity check** (always do this — it's a one-line confirmation):

$$D(x)Q(x) + R(x) = (x^2 + x - 1)(2x - 5) + (11x - 10) = 2x^3 - 3x^2 + 4x - 5 \;\checkmark$$

So $\boxed{\;\dfrac{2x^3 - 3x^2 + 4x - 5}{x^2 + x - 1} = (2x - 5) + \dfrac{11x - 10}{x^2 + x - 1}\;}$.

That right-hand side is now a polynomial plus a proper fraction — exactly the shape [[Partial Fractions|partial fractions]] expects.

### Watch the tableau build up

The same example above, drawn out as the schoolbook layout would look on paper. Each iteration is colour-coded: $\color{#2563eb}\text{blue}$ for the first quotient term and what it produces, $\color{#7c3aed}\text{purple}$ for the second, $\color{#059669}\text{green}$ for the final remainder.

![[polynomial-long-division-walkthrough.svg|697]]

The pattern to internalise: **quotient term goes up top in its own column → multiply through the divisor → subtract that row → repeat on the leftover until the leading degree drops below the divisor's**. The two coloured underbars are the two subtractions. The grey row sandwiched between them is what's left after the first subtraction — the *running dividend* that iteration 2 attacks.

---

## §4 Worked Example — Missing Terms

Divide $x^4 - 16$ by $x - 2$.

This is the classic missing-terms trap. The dividend has $x^4$ and $-16$, but no $x^3$, $x^2$, or $x$ terms. Rewrite explicitly:

$$x^4 - 16 = x^4 + 0x^3 + 0x^2 + 0x - 16.$$

Now run the algorithm:

| Step | Leading divide | New $Q$-term | Multiply back | Subtract → new running dividend |
|---|---|---|---|---|
| 1 | $x^4 / x = x^3$ | $x^3$ | $x^3(x - 2) = x^4 - 2x^3$ | $2x^3 + 0x^2 + 0x - 16$ |
| 2 | $2x^3 / x = 2x^2$ | $2x^2$ | $2x^2(x - 2) = 2x^3 - 4x^2$ | $4x^2 + 0x - 16$ |
| 3 | $4x^2 / x = 4x$ | $4x$ | $4x(x - 2) = 4x^2 - 8x$ | $8x - 16$ |
| 4 | $8x / x = 8$ | $8$ | $8(x - 2) = 8x - 16$ | $0$ |

So $Q(x) = x^3 + 2x^2 + 4x + 8$ and $R = 0$.

That makes $(x - 2)$ a factor — and the factorisation $x^4 - 16 = (x - 2)(x^3 + 2x^2 + 4x + 8)$ is just the difference-of-squares / geometric-sum identity:

$$x^4 - 16 = (x - 2)(x^3 + 2x^2 + 4x + 8).$$

You can also see this from the [[Remainder and Factor Theorems|Factor Theorem]]: $f(2) = 16 - 16 = 0 \Rightarrow (x - 2)$ is a factor. The Factor Theorem tells you the divisibility holds; long division gives you the actual quotient.

> [!tip] Cross-check with the geometric sum
> $x^n - a^n = (x - a)(x^{n-1} + ax^{n-2} + a^2 x^{n-3} + \ldots + a^{n-1})$ for any positive integer $n$. Setting $n = 4, a = 2$ recovers $x^4 - 16 = (x - 2)(x^3 + 2x^2 + 4x + 8)$ instantly. The long-division output is just an arithmetic confirmation of an algebraic identity.

---

## §5 Worked Example — Quadratic Divisor (Beyond Factor Theorem)

Divide $P(x) = x^4 + x^2 + 1$ by $D(x) = x^2 + x + 1$.

The Factor Theorem doesn't apply here — neither divisor nor dividend has obvious linear factors over $\mathbb{R}$. Long division is the only practical path.

Rewrite explicitly: $x^4 + 0x^3 + x^2 + 0x + 1$.

**Iteration 1.** $x^4 / x^2 = x^2$. Multiply: $x^2(x^2 + x + 1) = x^4 + x^3 + x^2$. Subtract:

$$(x^4 + 0x^3 + x^2 + 0x + 1) - (x^4 + x^3 + x^2) = -x^3 + 0x^2 + 0x + 1.$$

**Iteration 2.** $-x^3 / x^2 = -x$. Multiply: $-x(x^2 + x + 1) = -x^3 - x^2 - x$. Subtract:

$$(-x^3 + 0x^2 + 0x + 1) - (-x^3 - x^2 - x) = x^2 + x + 1.$$

**Iteration 3.** $x^2 / x^2 = 1$. Multiply: $1 \cdot (x^2 + x + 1) = x^2 + x + 1$. Subtract:

$$(x^2 + x + 1) - (x^2 + x + 1) = 0.$$

**Answer.** $Q(x) = x^2 - x + 1$, $R(x) = 0$. So

$$x^4 + x^2 + 1 = (x^2 + x + 1)(x^2 - x + 1).$$

This is a famous identity — $x^4 + x^2 + 1$ factors as the product of two real quadratics — and you've just rediscovered it by running the algorithm. (It also drops out of the cyclotomic identity $\Phi_3(x)\Phi_6(x) = x^4 + x^2 + 1$, but that's the long story.)

> [!info] Beyond syllabus — quadratic divisors via the Remainder Theorem
> Recall that when you divide by a quadratic $D(x)$, the remainder is at most linear: $R(x) = \alpha x + \beta$. If $D(x)$ has two distinct roots $r_1, r_2$ (real or complex), the identity $P(x) = D(x)Q(x) + R(x)$ evaluated at each root gives:
>
> $$P(r_1) = \alpha r_1 + \beta, \qquad P(r_2) = \alpha r_2 + \beta.$$
>
> Two equations in two unknowns — solve for $\alpha, \beta$ and you have the remainder *without doing the division*. This is the proper generalisation of the Remainder Theorem to higher-degree divisors. Standard at A-Level and in IB AA HL; out of 0606 / 9709 P3 scope.

---

## §6 The Synthetic-Division Shortcut (Linear Divisors Only)

When $D(x) = x - a$, the long-division layout has so many predictable zero entries that the algorithm collapses into a single row of arithmetic. This is **synthetic division** (also called *Horner's scheme*).

### The procedure

1. Write the coefficients of $P(x)$ in a row, including zeros for missing terms.
2. Bring the first coefficient straight down.
3. Multiply by $a$, write under the next coefficient, add.
4. Repeat to the end.
5. The last number is the remainder ($= P(a)$, by the [[Remainder and Factor Theorems|Remainder Theorem]]); the others are the coefficients of $Q(x)$, in order.

### Example — divide $2x^3 - 5x^2 + 3x - 7$ by $(x - 2)$

Coefficients of $P$: $2, -5, 3, -7$. Use $a = 2$:

$$\begin{array}{c|cccc}
2 & 2 & -5 & 3 & -7 \\
 &   &  4 & -2 &  2 \\ \hline
 & 2 & -1 & 1 & -5
\end{array}$$

Reading off: $Q(x) = 2x^2 - x + 1$, $R = -5$. So $P(x) = (x - 2)(2x^2 - x + 1) - 5$. (Cross-check: $P(2) = 16 - 20 + 6 - 7 = -5$ ✓ — exactly as the Remainder Theorem predicts.)

### When to use which

> [!tip] Algorithm choice
> - **Synthetic division** — divisor is $(x - a)$ (or $(ax - b)$ after a small tweak — divide all coefficients of $Q$ by $a$ at the end). Faster, less to write, mistakes are easier to spot.
> - **Long division** — divisor has degree $\geq 2$, OR you want full visibility of every step (helpful when teaching, when debugging, and when the divisor has many terms). The only general-purpose method.
> - **The Remainder Theorem** — divisor is linear AND you only need the remainder, not the quotient. Pure substitution; no division at all.

For 9709 P3 §3.1 and partial fractions, the divisors are usually quadratic (e.g., $x^2 + 1$, $(x-1)(x+2) = x^2 + x - 2$), so long division is the default tool. Synthetic division is a 0606 / A-Level fluency-builder.

---

## §7 Setting Up Partial Fractions — The Bridge Forward

The single biggest reason this card exists in a 9709 P3 student's life: improper-fraction setup for [[Partial Fractions|partial fractions]].

The partial-fractions algorithm starts with a *proper* rational expression — numerator degree strictly less than denominator degree. Real exam fractions don't always come that way. Compare:

$$\dfrac{x + 1}{x^2 + 3x + 2} \qquad \text{vs} \qquad \dfrac{x^3 + 2x}{x^2 - 1}.$$

The first is proper ($\deg 1 < \deg 2$) — it goes straight into partial fractions. The second is **improper** ($\deg 3 > \deg 2$). To split it, polynomial-divide first:

**Long-divide $x^3 + 2x$ by $x^2 - 1$.** Rewrite the dividend with explicit zeros: $x^3 + 0x^2 + 2x + 0$.

- Iteration 1: $x^3 / x^2 = x$. Multiply: $x(x^2 - 1) = x^3 - x$. Subtract: $0x^2 + 3x + 0$.
- Iteration 2: leading $0x^2$, current dividend is $3x + 0$. Degree $1 < 2$ — stop.

So $Q(x) = x$ and $R(x) = 3x$. Then

$$\dfrac{x^3 + 2x}{x^2 - 1} = x + \dfrac{3x}{x^2 - 1},$$

and the proper part $\dfrac{3x}{x^2 - 1} = \dfrac{3x}{(x-1)(x+1)}$ is now ready for partial-fraction decomposition.

**The pattern, every time.** If you're ever handed a fraction whose numerator degree is at least the denominator degree, the *first* move is polynomial long division. Don't try to decompose an improper fraction directly — every textbook method silently assumes you've already peeled off the polynomial part.

---

## §8 Common Misconceptions

### 1. Skipping missing terms

Dividing $x^3 - 7$ by $(x - 2)$ — many students write the dividend as just $x^3$ and $-7$ and skip the empty $x^2$ and $x$ slots. Subtraction then misaligns and the answer drifts.

**Fix.** Rewrite *every* power explicitly: $x^3 + 0x^2 + 0x - 7$. The empty columns must hold zeros, the way addition columns must hold zero digits.

### 2. Sign flip in the subtraction

When you subtract $-5x^2 - 5x + 5$, the result is $+5x^2 + 5x - 5$. Forgetting to flip *every* sign — not just the leading one — produces an off-by-a-sign quotient and a wrong remainder. The error is invisible until the sanity check at the end.

**Fix.** Write the subtraction in two steps: (a) write the row to subtract with its own signs; (b) write the same row again with every sign flipped, prefixed by a minus sign. Then do the addition. It's two extra rows but eliminates the bug.

### 3. Dividing each term separately

A common conceptual error: students see $\dfrac{x^3 + 2x^2 - 5x + 1}{x^2 - 1}$ and split it as $\dfrac{x^3}{x^2 - 1} + \dfrac{2x^2}{x^2 - 1} + \ldots$, hoping to simplify each piece. That's not polynomial division — that's just rewriting the fraction without progress.

**Fix.** "Divide each term" only works when the divisor is a *single term* (a monomial), e.g., $\dfrac{x^3 + 2x^2}{x^2} = x + 2$. For any divisor with two or more terms, you have to run the long-division algorithm — there's no termwise shortcut.

### 4. Stopping too early

Students sometimes stop the algorithm when the leading term of the running dividend has the same degree as the divisor — for example, stopping with $-5x^2 + 6x - 5$ when the divisor is $x^2 + x - 1$. That's still divisible. The stopping rule is degree *strictly less than* $\deg D$.

**Fix.** Repeat after me: "Stop when the running dividend's degree is *less than* the divisor's degree." Strictly less.

### 5. Forgetting the sanity check

The algorithm has many places to go wrong. The sanity check $P(x) \stackrel{?}{=} D(x)Q(x) + R(x)$ catches almost every error in 30 seconds. Many students skip it and find out the answer is wrong from the mark scheme.

**Fix.** Always expand $D(x)Q(x) + R(x)$ at the end, even informally. It costs one minute and saves the question.

---

## §9 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** Paper 3 §3.1 — *algebra*: modulus, polynomial division, partial fractions, $(1+x)^n$ binomial series for any $n$.

**What's tested:** Polynomial division almost never appears as a stand-alone question. It's a *prerequisite skill* embedded in:

- **Partial fractions setup** — improper-fraction problems where you must polynomial-divide first. Standard 4–6 mark question opener: "Express $\dfrac{P(x)}{D(x)}$ in partial fractions" with $\deg P \geq \deg D$ — the first 1–2 marks are for the polynomial division.
- **Binomial series with rational denominators** — when you're asked to expand $\dfrac{1}{D(x)}$ or use partial fractions to feed into a $(1 + x)^n$ expansion, the long division step usually comes first.
- **Integration by partial fractions** — the same setup; you long-divide, decompose, then integrate term by term.

**Mark scheme patterns for partial-fractions setups:**
1. Recognise improper / set up long division.
2. Correct quotient.
3. Correct remainder.
4. Decompose the proper-fraction leftover.

**Tip.** On 9709 P3 you'll never be asked "do this long division" with no further use of the answer. The division is always *for something*. Anticipate: the proper fraction you produce will go into partial fractions; the partial fractions will get integrated or expanded. Set out the long division so the next step uses the result cleanly.

### Cambridge 0606

**Syllabus refs:** 3.1 (polynomials, division), 3.2 (factor theorem applied to cubic factorisation), 3.3 (solving cubic equations).

**What's tested at 0606 level:** Polynomial division is taught primarily as the bridge from the [[Remainder and Factor Theorems|Factor Theorem]] (find a root) to the quotient quadratic (which you then factorise). Most 0606 questions can be done by *inspection* once you know the linear factor — the long-division layout is taught for the cases when inspection isn't obvious. Synthetic division is sometimes shown as enrichment; not strictly required.

**Typical questions:**
- "Show that $(x - 3)$ is a factor of $f(x) = x^3 - 4x^2 + x + 6$, and hence factorise $f(x)$ completely." [5 marks]
- "Find the quotient and remainder when $f(x) = 2x^3 - 5x^2 + 4$ is divided by $(x^2 - 1)$." [3 marks — the rare standalone-division question]

### A-Level

The same algorithm appears in **AS / A-Level Pure Maths**, with the partial-fractions application coming in A2. Edexcel, AQA, OCR, MEI all teach the same algorithm with cosmetic notational differences. The OxAQA 9660 syllabus also lists polynomial division as a §3.1-equivalent topic.

### IB AA

**Topic refs:** AA SL Topic 2 (functions), AA HL Topic 1 (algebra) — polynomial division appears as a fluency tool in factorisation problems and as a prerequisite for partial fractions in HL integration. The IB doesn't usually examine long division directly; it shows up inside larger questions.

### AP Calculus

Polynomial division per se isn't a CED-listed topic — but it's a prerequisite for **partial fractions integration** (BC Topic 6.10). AP students who haven't seen it in pre-calc will need it the day partial fractions arrives. Synthetic division is more common in US pre-calc curricula than in international syllabi.

---

### Cambridge 9231 Further Mathematics — the licence behind Further Pure 1

Polynomial division is not itself a named 9231 row, but the **factor theorem it rests on is what licenses the central move of FP1 §1.1**: a polynomial with roots $\alpha, \beta, \gamma$ must factor as $a(x-\alpha)(x-\beta)(x-\gamma)$, and expanding *that* is where every relation between roots and coefficients comes from — see [[Symmetric Functions of Roots]]. A student shaky on why a root forces a linear factor will treat those relations as magic.

It also reappears as machinery on FP2: §2.2's characteristic equation is a polynomial whose roots are the eigenvalues, and reducing it once a root is known is exactly this division.

### Where this is *not* examined

Not on **0580** or **0606** — IGCSE stops at factorising quadratics and the factor theorem for cubics without formal long division. Not a named topic on **IB AA** (SL or HL) or **AP Calculus**, though both assume the skill wherever partial fractions or rational-function limits appear. Synthetic division is on no syllabus at all; it is here because it is faster and the exam does not care how you got the quotient.

## §10 Connections

- **Prerequisite:** [[Remainder and Factor Theorems]] — the linear-divisor special case, and the source of the synthetic-division shortcut. *Polynomial Division generalises that card.*
- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — the language of polynomials, degrees, leading coefficients.
- **Prerequisite:** [[Expanding Brackets (Vocab)]] — needed for the multiply-back step inside each iteration, and for the sanity check at the end.
- **Prerequisite:** [[Algebraic Fractions (Vocab)]] — the proper-vs-improper distinction and the rational-expression vocabulary the card lives in.
- **Leads to:** [[Partial Fractions]] — the headline application. Improper-fraction problems start with polynomial division.
- **Leads to:** [[Binomial Series]] — partial fractions plus binomial expansion together cover most 9709 P3 §3.1 algebra questions.
- **Leads to:** [[Cubic Equations]] — once you've factored out a linear factor via the Factor Theorem, polynomial division produces the quadratic quotient you then solve.
- **Parallel:** [[Algebraic Proof]] — polynomial-identity reasoning ($P(x) \equiv D(x)Q(x) + R(x)$ as an identity in $x$) shares its logic with general algebraic-identity proofs.
- **Corollary of:** the **Division Algorithm for polynomials** — the field-agnostic theorem that this section's $\boxed{P = DQ + R}$ identity is uniquely solvable. Itself an echo of the Division Algorithm for integers ($a = bq + r$, $0 \leq r < b$).
- **For 9709 students:** [[MF19 Reference (9709)]] — polynomial division has nothing on the formula sheet; it's a procedural skill, no formula to give. The reference card lists what *is* available for the §3.1 algebra topics.

---

## Beyond Syllabus

### The integer–polynomial parallel runs deep

The Division Algorithm for integers ($a = bq + r$, $0 \leq r < b$) and the Division Algorithm for polynomials ($P = DQ + R$, $\deg R < \deg D$) aren't an analogy — they're the same theorem in two different rings. Both $\mathbb{Z}$ and $F[x]$ (polynomials over a field) are **Euclidean domains**: rings where you can run the Euclidean algorithm to compute greatest common divisors.

Run Euclid's algorithm on two polynomials and you compute the polynomial GCD — the highest-degree polynomial that divides both. That's the algorithmic foundation behind:
- Symbolic factorisation in computer algebra systems (Mathematica, SymPy).
- Reed–Solomon error-correcting codes (the math that keeps QR codes and Voyager-1 transmissions readable).
- Public-key cryptography over polynomial rings (lattice-based, post-quantum schemes).

The classroom algorithm of polynomial long division is the entry point.

### Horner's scheme as efficient evaluation

Synthetic division, viewed sideways, is **Horner's scheme** for polynomial evaluation. Instead of computing $a_n x^n + a_{n-1}x^{n-1} + \ldots + a_0$ as a sum of $n+1$ separately-computed monomials (which costs $O(n^2)$ multiplications), Horner rewrites it as

$$P(x) = a_0 + x(a_1 + x(a_2 + x(\ldots + x \cdot a_n)\ldots))$$

— a nested form that needs only $n$ multiplications and $n$ additions. The synthetic-division tableau is *exactly* Horner's scheme being executed. So the same trick that lets you divide quickly also lets you evaluate quickly. Numerical analysis courses lead with it.

### Polynomial long division over $\mathbb{F}_p$ — the same algorithm, smaller numbers

Everything in this card works identically when the coefficients live in $\mathbb{F}_p = \{0, 1, \ldots, p-1\}$ with arithmetic mod $p$ (a finite field). The long-division algorithm is unchanged; only the arithmetic is mod $p$. This is how Reed–Solomon codes are computed in practice — long division of polynomials over $\mathbb{F}_{256}$, where each coefficient is a byte.

Same recipe, different ring. The algorithm doesn't care.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $P(x) = D(x)Q(x) + R(x)$ | `P(x) = D(x)Q(x) + R(x)` | The general division identity |
| $\deg P$ | `\deg P` | Degree of polynomial $P$; use `\deg` to upright-style it |
| $\enclose{longdiv}{P}$ | `\enclose{longdiv}{P}` | Long-division "house" — needs the `enclose` MathJax extension; usually auto-loaded in Obsidian |
| $\dfrac{P(x)}{D(x)} = Q(x) + \dfrac{R(x)}{D(x)}$ | `\dfrac{P(x)}{D(x)} = Q(x) + \dfrac{R(x)}{D(x)}` | Improper-to-proper rewrite |
| $\begin{array}{c\|cccc}\ldots\end{array}$ | `\begin{array}{c\|cccc}` | Array with a vertical bar — the synthetic-division tableau format |
| $\stackrel{?}{=}$ | `\stackrel{?}{=}` | "Equals?" — used in the sanity-check step |
| $\mathbb{F}_p$ | `\mathbb{F}_p` | The finite field with $p$ elements (beyond syllabus) |
| $\equiv$ | `\equiv` | Identical to (used for polynomial identities) |

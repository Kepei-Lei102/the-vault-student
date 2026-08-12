---
chinese: 余式定理与因式定理 (yúshì dìnglǐ yǔ yīnshì dìnglǐ)
prerequisites:
  - "[[Quadratic Equations]]"
  - "[[Factorising (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Algebraic Fractions (Vocab)]]"
leads_to:
  - "[[Polynomial Division]]"
  - "[[Factorising Polynomials]]"
  - "[[Cubic Equations]]"
  - "[[Cubic Graphs]]"
  - "[[Graphs of Functions]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - syllabus/0606-3-1
  - syllabus/0606-3-2
  - syllabus/0606-3-3
  - syllabus/9709-2-1
  - type/theorem
  - type/proof
  - type/technique
  - notation/polynomial
  - misconception/sign-in-divisor
  - misconception/skipping-missing-terms
---

# Remainder and Factor Theorems 余式定理与因式定理

## Definition

### Formal

A **polynomial** in $x$ is an expression built from non-negative integer powers of $x$ with constant coefficients:

$$f(x) = a_n x^n + a_{n-1}x^{n-1} + \ldots + a_1 x + a_0, \qquad a_n \neq 0$$

The number $n$ is the **degree** and $a_n$ is the **leading coefficient**.

For any polynomial $f(x)$ and any linear divisor $(x - a)$, polynomial long division produces a quotient $q(x)$ and a constant remainder $R$ satisfying the **division identity**:

$$f(x) = (x - a)\,q(x) + R$$

- **Remainder Theorem.** The remainder is $R = f(a)$.
- **Factor Theorem.** $(x - a)$ is a factor of $f(x)$ if and only if $f(a) = 0$.

### Intuitive

When you divide numbers — say $17 \div 5$ — you get a quotient ($3$) and a remainder ($2$), with the identity $17 = 5 \times 3 + 2$. Polynomial division works exactly the same way:

$$\underbrace{f(x)}_{\text{dividend}} = \underbrace{(x - a)}_{\text{divisor}} \cdot \underbrace{q(x)}_{\text{quotient}} + \underbrace{R}_{\text{remainder}}$$

The remainder when dividing by $(x - a)$ has to be a number (anything of degree $\geq 1$ could be divided further). The Remainder Theorem is the surprise: that number is *just* $f(a)$. No polynomial long division needed — you substitute and you're done.

The Factor Theorem then says: if that remainder is zero, $(x - a)$ divided evenly, so it was a factor all along. The whole apparatus of cubic factorisation rests on this one-line observation.

### 中文锚点

**余式定理**：多项式 $f(x)$ 除以 $(x - a)$ 的余数等于 $f(a)$。不需要做长除法，代入即可。

**因式定理**：$(x - a)$ 是 $f(x)$ 的因式 $\iff f(a) = 0$。这是余式定理在余数为零时的推论。

这组定理是处理三次及更高次多项式的核心工具。二次方程我们有三种方法（因式分解、配方法、求根公式，见 [[Quadratic Equations]]），但三次方程没有学生会真用的公式——取而代之的是因式定理，像侦探一样一次猜一个根。

---

## §1 The Division Identity — Setup

Before the theorems themselves, write down what polynomial division means.

**Division identity.** For any polynomial $f(x)$ of degree $\geq 1$ and any linear divisor $(x - a)$, there exist a polynomial $q(x)$ (the **quotient**) and a constant $R$ (the **remainder**) such that

$$\boxed{\;f(x) = (x - a)\,q(x) + R\;}$$

This is an *existence* statement — not a formula. [[Polynomial Division|Polynomial long division]] is the algorithm that actually computes $q(x)$ and $R$. As we're about to see, the Remainder Theorem gives you $R$ without running the algorithm at all — *for linear divisors only*. Quadratic and higher-degree divisors don't have this shortcut, so you fall back to the general algorithm in [[Polynomial Division]].

> [!tip] Why must the remainder be a constant?
> When you divide by a divisor of degree $d$, the remainder must have degree strictly less than $d$ — otherwise you could keep dividing. The divisor $(x - a)$ has degree $1$, so the remainder has degree $< 1$, i.e., a constant. If we divided by a quadratic like $(x^2 - 1)$ instead, the remainder would be at most linear: $R(x) = \alpha x + \beta$.

---

## §2 The Remainder Theorem 余式定理

**Theorem.** If a polynomial $f(x)$ is divided by $(x - a)$, the remainder is $f(a)$.

### Proof

Start with the division identity from §1:

$$f(x) = (x - a)\,q(x) + R$$

This holds for *every* value of $x$. In particular, set $x = a$:

$$f(a) = (a - a)\,q(a) + R = 0 \cdot q(a) + R = R$$

So $R = f(a)$. $\blacksquare$

> [!tip] The magic is the zero
> Substituting $x = a$ annihilates the whole quotient term because $(x - a)$ becomes $0$. Whatever complicated polynomial $q(x)$ is, it gets multiplied by zero and vanishes. The remainder is all that's left. That's the entire content of the theorem — and the proof is two lines because the idea is that clean.

### Example — just substitute

Find the remainder when $f(x) = x^3 - 4x^2 + 5x + 1$ is divided by $(x - 2)$.

Without the theorem, this is a polynomial long division exercise. *With* the theorem, just compute $f(2)$:

$$f(2) = 2^3 - 4(2)^2 + 5(2) + 1 = 8 - 16 + 10 + 1 = 3$$

Remainder $= \boxed{3}$.

### Dividing by $(ax - b)$

The divisor isn't always as clean as $(x - a)$. For a general linear divisor $(ax - b)$, set $ax - b = 0$ to find the root $x = b/a$, then:

$$\text{Remainder when } f(x) \text{ is divided by } (ax - b) = f\!\left(\dfrac{b}{a}\right)$$

**Example.** Find the remainder when $f(x) = 2x^3 + x^2 - 5$ is divided by $(2x - 1)$.

$2x - 1 = 0 \Rightarrow x = \dfrac{1}{2}$:

$$f\!\left(\dfrac{1}{2}\right) = 2 \cdot \dfrac{1}{8} + \dfrac{1}{4} - 5 = \dfrac{1}{4} + \dfrac{1}{4} - 5 = -\dfrac{9}{2}$$

---

## §3 The Factor Theorem 因式定理

**Theorem.** $(x - a)$ is a factor of $f(x)$ if and only if $f(a) = 0$.

### Proof

This is an immediate corollary of the Remainder Theorem.

$(x - a)$ is a **factor** of $f(x)$ means: when we divide $f(x)$ by $(x - a)$, the remainder is $0$. By the Remainder Theorem, that remainder equals $f(a)$. So

$$(x - a) \text{ is a factor of } f(x) \iff R = 0 \iff f(a) = 0. \qquad \blacksquare$$

### The geometric picture

The Factor Theorem has a beautiful graphical meaning. The equation $f(a) = 0$ says the graph $y = f(x)$ crosses the $x$-axis at $x = a$. So three very different-looking statements are really the same:

> **$x = a$ is an $x$-intercept of $y = f(x)$** ⟺ **$f(a) = 0$** ⟺ **$(x - a)$ is a factor of $f(x)$**

Geometry, algebra, and factorisation — three windows into the same object.

![[factor-theorem-cubic.svg|640]]

### Example — verifying a factor

Show that $(x + 2)$ is a factor of $f(x) = x^3 + 4x^2 + x - 6$.

$(x + 2) = (x - (-2))$, so $a = -2$. Check $f(-2) = 0$:

$$f(-2) = (-2)^3 + 4(-2)^2 + (-2) - 6 = -8 + 16 - 2 - 6 = 0 \;\checkmark$$

So $(x + 2)$ is a factor. $\square$

---

## §4 The Main Event — Full Cubic Factorisation

This is what the Factor Theorem was made for. Cubics don't have a nice formula students will ever use in practice. Instead, we use the Factor Theorem as a detective trick:

> **Guess a root. Verify. Divide out. Finish the quadratic.**

### The procedure

1. **Hunt for a root.** Try small integers: $\pm 1$, $\pm 2$, and divisors of the constant term. When $f(a) = 0$, you've found a linear factor $(x - a)$.
2. **Divide out.** Use polynomial long division or inspection to write $f(x) = (x - a)\,q(x)$ where $q(x)$ is a quadratic.
3. **Factor the quadratic.** Apply the usual quadratic tools (see [[Quadratic Equations]]).

### Worked example

Fully factorise $f(x) = x^3 - 3x^2 - 4x + 12$ over the reals.

**Step 1 — hunt.**
- $f(1) = 1 - 3 - 4 + 12 = 6 \neq 0$.
- $f(2) = 8 - 12 - 8 + 12 = 0$. ✓

So $(x - 2)$ is a factor.

**Step 2 — divide out by inspection.** Write

$$x^3 - 3x^2 - 4x + 12 = (x - 2)(x^2 + bx + c)$$

The leading $x^3$ forces the $x^2$ term in the quotient. Constant term: $-2c = 12 \Rightarrow c = -6$. Linear term: $-4 = -2b + c \cdot 1 = -2b - 6$, so $b = -1$. Hence

$$f(x) = (x - 2)(x^2 - x - 6)$$

**Step 3 — factor the quadratic.** $x^2 - x - 6 = (x - 3)(x + 2)$.

**Final:** $\boxed{f(x) = (x - 2)(x - 3)(x + 2)}$.

The roots are $x = -2, 2, 3$ — the three $x$-intercepts on the cubic graph.

### Why "try divisors of the constant term"?

> [!info] Beyond syllabus — the Rational Root Theorem
> If $f(x) = a_n x^n + \ldots + a_0$ has a rational root $p/q$ in lowest terms, then $p$ divides $a_0$ and $q$ divides $a_n$.
>
> For a **monic** polynomial (leading coefficient $1$), every rational root must be an integer divisor of the constant term. For $x^3 - 3x^2 - 4x + 12$, the constant is $12$, so candidates are $\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12$.
>
> This is why "try divisors of the constant term" works — it's a genuine theorem, not a rule of thumb. (Proof: substitute $p/q$ into $f$, clear denominators, analyse which side $q$ and $p$ must divide.)

---

## §5 Finding Unknown Coefficients

Exam favourite: use the theorems backwards to recover unknowns from given conditions.

### Example 1 — one condition

$f(x) = 2x^3 + kx^2 - 5x + 3$ leaves remainder $9$ when divided by $(x - 2)$. Find $k$.

$$f(2) = 9 \;\Rightarrow\; 16 + 4k - 10 + 3 = 9 \;\Rightarrow\; 4k = 0 \;\Rightarrow\; k = 0$$

### Example 2 (0606 level) — two conditions, two unknowns

$f(x) = 2x^3 + ax^2 + bx - 5$ has $(2x - 1)$ as a factor and leaves remainder $-25$ when divided by $(x + 2)$. Find $a$ and $b$.

Two conditions, two equations.

**Condition 1.** $(2x - 1)$ factor $\Rightarrow f\!\left(\tfrac{1}{2}\right) = 0$.

$$2 \cdot \dfrac{1}{8} + a \cdot \dfrac{1}{4} + b \cdot \dfrac{1}{2} - 5 = 0 \;\Rightarrow\; \dfrac{a}{4} + \dfrac{b}{2} = \dfrac{19}{4} \;\Rightarrow\; a + 2b = 19$$

**Condition 2.** remainder $-25$ on $(x + 2)$ $\Rightarrow f(-2) = -25$.

$$2(-8) + a(4) + b(-2) - 5 = -25 \;\Rightarrow\; 4a - 2b = -4 \;\Rightarrow\; 2a - b = -2$$

**Solve.** From the second equation $b = 2a + 2$. Substitute: $a + 2(2a + 2) = 19 \Rightarrow 5a = 15 \Rightarrow a = 3$, so $b = 8$.

*(Sanity check: $f(x) = 2x^3 + 3x^2 + 8x - 5$. $f(\tfrac{1}{2}) = \tfrac{1}{4} + \tfrac{3}{4} + 4 - 5 = 0$ ✓. $f(-2) = -16 + 12 - 16 - 5 = -25$ ✓.)*

---

## §6 Common Misconceptions

### 1. Sign error in the divisor

To use the Remainder Theorem on $(x - a)$, you substitute $x = a$. But the divisor $(x + 3)$ is $(x - (-3))$ — so the root is $-3$, not $+3$. Students substitute $+3$ and wonder why the answer is wrong.

**Fix:** Always write "$(x + 3) = 0 \Rightarrow x = -3$" as an explicit mini-step before substituting. Treat the linear divisor as an equation whose root is the value you plug in.

### 2. Forgetting missing terms in long division

When dividing $x^3 - 7$ by $(x - 2)$ via long division, the $x^2$ and $x$ coefficients are $0$. Students skip those slots and the subtraction goes sideways.

**Fix:** Rewrite with every power explicit: $x^3 - 7 = x^3 + 0x^2 + 0x - 7$. Better still: use the Remainder Theorem directly — $f(2) = 8 - 7 = 1$.

### 3. Confusing "factor" with "divisor"

Students say "$(x - 2)$ divides $f(x)$" and just mean they're computing the division. But the Factor Theorem's conclusion requires the remainder to be **zero**. Doing the division doesn't make the divisor a factor.

**Fix:** *Factor* is a yes/no property that demands $f(a) = 0$. *Divisor* is anything you're dividing by — that's just notation.

### 4. Applying the theorem to quadratic divisors

The Remainder Theorem in this form only works for linear divisors $(x - a)$ or $(ax - b)$. Students try to substitute a single value for a quadratic divisor like $(x^2 - 1)$ and get tangled.

**Fix:** For quadratic divisors, the remainder is generally linear: $R(x) = \alpha x + \beta$. You substitute *both* roots of the quadratic to get two equations in $\alpha, \beta$. Out of 0606 scope but standard at A-Level.

---

## §7 Exam Notes

### Cambridge 0606

**Syllabus refs:** 3.1 (know and use the remainder and factor theorems), 3.2 (find factors of polynomials; cubic → linear × quadratic), 3.3 (solve cubic equations).

**What's tested:**

- Find the remainder when $f(x)$ is divided by $(x - a)$ or $(ax - b)$.
- Show that $(x - a)$ is a factor; hence fully factorise a cubic.
- Recover unknown coefficients from factor/remainder conditions (typically two unknowns from two conditions).
- Solve cubic equations by first factorising with the Factor Theorem.

**Typical questions:**

- "Show that $(x - 3)$ is a factor of $f(x) = x^3 - 2x^2 - 5x + 6$, and hence factorise $f(x)$ completely." [5 marks]
- "$f(x) = 2x^3 + ax^2 + bx + c$ has $(x - 1)$ as a factor, leaves remainder $-3$ when divided by $(x + 1)$, and $f(0) = -2$. Find $a$, $b$, $c$." [6 marks]
- "Solve $x^3 + x^2 - 4x - 4 = 0$." [4 marks — test $x = -1$, divide out, solve the quadratic]

**Mark scheme patterns:** (1) correct substitution, (2) equation setup from the condition, (3) quotient quadratic (from division), (4) quadratic factorisation, (5) all roots listed.

### A-Level

The theorems appear in **AS-Level Pure Maths** (Year 12) inside the Polynomials chapter. Expectations are the same as 0606, plus:

- Proof of the Remainder Theorem (the one-line argument in §2).
- Division by any linear divisor, including awkward ones like $(3x + 4)$ (root $-\tfrac{4}{3}$).
- Using the theorems to prove polynomial identities ($f(x) \equiv g(x)$ if they agree at enough points).

### Beyond — university

In ring theory, the Remainder Theorem generalises to polynomial rings $F[x]$ over any field $F$. The key statement becomes "$f(x) \equiv f(a) \pmod{(x - a)}$" — the template for modular arithmetic in rings. The Factor Theorem is the first instance of a deeper fact: the ideal $(x - a)$ is **maximal** in $F[x]$, and the quotient ring $F[x]/(x - a) \cong F$.

---

## §8 Connections

- **Prerequisite:** [[Quadratic Equations]] — the 2nd-degree baseline; every cubic factorisation ends with a quadratic quotient to solve
- **Prerequisite:** [[Factorising (Vocab)]] — the general factoring vocabulary (HCF, DOTS, trinomial, cross method)
- **Prerequisite:** [[Expanding Brackets (Vocab)]] — needed to check factorisations and do division-by-inspection
- **Parallel:** [[Algebraic Proof]] — the Remainder and Factor Theorems are textbook examples of *identity + clever substitution* proofs
- **Leads to:** [[Factorising Polynomials]] — the syllabus's next step: use these theorems systematically on cubics and beyond
- **Leads to:** [[Cubic Equations]] — solving $ax^3 + bx^2 + cx + d = 0$ starts with finding one root by the Factor Theorem
- **Leads to:** [[Cubic Graphs]] — the roots you find are the $x$-intercepts of the sketch
- **Leads to:** [[Graphs of Functions]] — *roots ↔ $x$-intercepts ↔ factors* is the through-line for every polynomial
- **Generalises into:** [[Polynomial Division]] — the general long-division algorithm for any divisor, not just linear; this card's $f(x) = (x-a)q(x) + R$ is the linear special case where the shortcut $R = f(a)$ exists. For 9709 P3 §3.1 partial-fractions setup, the general card is the workhorse.
- **Corollary of:** the Division Algorithm for polynomials — itself an echo of the Division Algorithm for integers

---

## Beyond Syllabus

### Synthetic division — the streamlined algorithm

For dividing by $(x - a)$ there's a much faster algorithm than full long division: **synthetic division**. Write just the coefficients of $f(x)$ in a row. Bring down the first; multiply by $a$ and add to the next; repeat. The last number is the remainder ($= f(a)$); the others are the coefficients of the quotient.

For $f(x) = x^3 - 3x^2 - 4x + 12$ divided by $(x - 2)$:

$$\begin{array}{c|cccc}
2 & 1 & -3 & -4 & 12 \\
 &   &  2 & -2 & -12 \\ \hline
 & 1 & -1 & -6 & 0
\end{array}$$

Read off: quotient $= x^2 - x - 6$, remainder $= 0$. Same answer as before, a third of the writing. It's what calculators do internally.

### Lagrange interpolation — the Remainder Theorem, generalised

Polynomials and integers share deep structural parallels. Both have a Division Algorithm. Both have primes (prime numbers / irreducible polynomials). Both obey a Chinese Remainder Theorem.

For polynomials, CRT says: if you know $f(a_1), f(a_2), \ldots, f(a_n)$ at $n$ distinct points, you can reconstruct $f(x)$ uniquely — provided its degree is less than $n$. This is **Lagrange interpolation**, the engine behind polynomial curve-fitting, Shamir's secret sharing, and Reed–Solomon error-correcting codes (the reason your QR codes and CDs stay readable when smudged).

The "modest" Remainder Theorem of 0606 §3.1 is the atomic case: one point, one remainder. Everything larger is built by stacking this atom.

### The Factor Theorem meets the Fundamental Theorem of Algebra

By the Factor Theorem, every root $a$ of $f(x)$ gives you a factor $(x - a)$. Combine that with the Fundamental Theorem of Algebra (Gauss, 1799) — every degree-$n$ polynomial has exactly $n$ complex roots, counted with multiplicity — and you get:

> Every polynomial of degree $n$ over $\mathbb{C}$ factorises completely into $n$ linear factors.

Gauss's theorem is the *existence* half (the roots are there). The Factor Theorem is the *constructive* half (once you find a root, you get a factor for free). Together they promote "there are roots" into "here is the factorisation."

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $f(x) = (x-a)q(x) + R$ | `f(x) = (x-a)q(x) + R` | The division identity |
| $R = f(a)$ | `R = f(a)` | The Remainder Theorem |
| $(x - a) \mid f(x)$ | `(x - a) \mid f(x)` | "$(x-a)$ divides $f(x)$"; vertical bar is `\mid` |
| $\iff$ | `\iff` | "if and only if" |
| $f\!\left(\tfrac{b}{a}\right)$ | `f\!\left(\tfrac{b}{a}\right)` | For dividing by $(ax - b)$ |
| $\blacksquare$ | `\blacksquare` | End of proof |

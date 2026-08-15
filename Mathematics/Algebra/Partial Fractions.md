---
chinese: 部分分式 (bùfèn fēnshì)
prerequisites:
  - "[[Polynomial Division]]"
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Factorising (Vocab)]]"
  - "[[Standard Integrals]]"
  - "[[Integration by Substitution]]"
leads_to:
  - "[[Binomial Series]]"
  - "[[Differential Equations]]"
  - "[[Summation of Series]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-3-1
  - type/technique
  - type/algorithm
  - notation/polynomial
  - notation/rational-expression
  - misconception/forgetting-improper-check
  - misconception/repeated-factor-two-pieces
  - misconception/quadratic-factor-shape
  - misconception/skipping-cover-up-when-applicable
---

# Partial Fractions 部分分式

## Definition

### Formal

Let $\dfrac{P(x)}{D(x)}$ be a *proper* rational expression — that is, $\deg P < \deg D$ — and assume $D(x)$ has been fully factorised over $\mathbb{R}$ into a product of distinct or repeated linear factors and irreducible quadratic factors. Then $\dfrac{P(x)}{D(x)}$ can be written *uniquely* as a sum of simpler fractions, one for each factor of $D(x)$, where:

- each **distinct linear factor** $(ax + b)$ contributes a single term $\dfrac{A}{ax + b}$;
- each **repeated linear factor** $(ax + b)^k$ contributes $k$ terms, $\dfrac{A_1}{ax + b} + \dfrac{A_2}{(ax + b)^2} + \ldots + \dfrac{A_k}{(ax + b)^k}$;
- each **irreducible quadratic factor** $(ax^2 + bx + c)$ contributes a term $\dfrac{Bx + C}{ax^2 + bx + c}$ — note the **linear numerator**, not just a constant.

The unknowns $A, A_1, \ldots, B, C$ are real constants determined uniquely by the requirement that the sum equals the original fraction as an *identity in $x$* (true for all $x$ in the common domain).

### Intuitive

You already know how to add fractions with different denominators: find a common denominator, combine numerators, simplify. Partial fractions is exactly that operation **run in reverse**.

$$\dfrac{1}{x - 1} + \dfrac{2}{x + 3} \;\xrightarrow[\text{combine}]{}\; \dfrac{(x + 3) + 2(x - 1)}{(x - 1)(x + 3)} = \dfrac{3x + 1}{(x - 1)(x + 3)}$$

Read that arrow left-to-right and you've combined two fractions. Read it right-to-left and you've decomposed a complicated fraction into simple pieces. **Partial fractions is the right-to-left direction.**

The reason this is worth a whole card: the right-hand side is essentially impossible to integrate or expand as a power series directly. The two pieces on the left are easy ($\int \tfrac{1}{x-1}\,dx = \ln\lvert x-1\rvert$, $\int \tfrac{2}{x+3}\,dx = 2\ln\lvert x+3\rvert$). So splitting the complicated fraction into simple pieces *unlocks* every analytic technique that works on the simple pieces.

This is the central use-case at A-Level / 9709 P3 / IB HL: **partial-fraction decompose, then integrate** (or expand, or take a Laplace transform, or solve a differential equation). The decomposition itself is just algebra; what it *enables* is the entire integration and series-expansion toolkit.

### 中文锚点

**部分分式**（bùfèn fēnshì），又叫"分式分解"或"部分分式分解"：把一个复杂的代数分式 $\dfrac{P(x)}{D(x)}$ 拆成若干个简单分式之和。

中文教材里通常这样讲：**先把分母完全因式分解，然后按因式的形状写出待定系数的分式之和，最后比较系数（或代特殊值）求出待定系数。**

跟 IGCSE 学过的"通分相加"恰好是逆运算：
$$\dfrac{1}{x-1} + \dfrac{2}{x+3} = \dfrac{3x+1}{(x-1)(x+3)} \quad\Longleftrightarrow\quad \dfrac{3x+1}{(x-1)(x+3)} = \dfrac{1}{x-1} + \dfrac{2}{x+3}$$

通分是把简单分式拼成复杂分式；部分分式是把复杂分式拆成简单分式。学了之后才能用对数和反正切积分有理函数（整 9709 P3 §3.5 的核心），也是 [[Binomial Series|二项级数]]展开的入口。

**重要前提：**只能拆**真分式（proper fraction）**。如果分子次数 $\geq$ 分母次数，必须先做[[Polynomial Division|多项式长除法]]，把它拆成"多项式 + 真分式"，然后只对真分式部分做分式分解。

---

## §1 The Inverse-of-Combining Bridge

You learned the forward direction in [[Algebraic Fractions (Vocab)|Algebraic Fractions]]:

$$\dfrac{A}{x - 1} + \dfrac{B}{x + 3} \xrightarrow[\text{forward}]{\text{add}} \dfrac{A(x + 3) + B(x - 1)}{(x - 1)(x + 3)} = \dfrac{(A + B)x + (3A - B)}{(x - 1)(x + 3)}$$

The *forward* direction is mechanical: cross-multiply and tidy up. The *backward* direction is "given $\dfrac{3x + 1}{(x-1)(x+3)}$, find $A$ and $B$ such that $A + B = 3$ and $3A - B = 1$." Two unknowns, two equations — a linear system. Solving gives $A = 1, B = 2$. That's a partial-fraction decomposition.

| Operation | Direction | What you do |
|---|---|---|
| **Combining (you already know)** | Forward | Common denominator, add numerators |
| **Partial fractions (this card)** | Reverse | Assume the decomposition shape; solve for the numerator constants |

The whole subject is: *given the destination, find the route*. Once you accept that, the rest is bookkeeping.

---

## §2 The Three Cases — What Shape to Assume

The decomposition's shape is dictated entirely by the **factorisation of the denominator**. Three cases, applicable in any combination:

### Case A — Distinct linear factors

If $D(x)$ has $n$ distinct linear factors $(a_1 x + b_1)(a_2 x + b_2)\cdots(a_n x + b_n)$, then

$$\dfrac{P(x)}{D(x)} = \dfrac{A_1}{a_1 x + b_1} + \dfrac{A_2}{a_2 x + b_2} + \ldots + \dfrac{A_n}{a_n x + b_n}.$$

One constant per factor. **Worked in §4.**

### Case B — Repeated linear factor

If a factor $(ax + b)$ appears with multiplicity $k$ in $D(x)$, that single factor contributes **$k$ separate terms** — one for each power from $1$ up to $k$:

$$\text{contribution from }(ax + b)^k = \dfrac{A_1}{ax + b} + \dfrac{A_2}{(ax + b)^2} + \ldots + \dfrac{A_k}{(ax + b)^k}.$$

The constants $A_1, \ldots, A_k$ are independent — you can't compress them into one. **This is the most-missed shape rule.** Worked in §5.

### Case C — Irreducible quadratic factor

If $D(x)$ contains an irreducible quadratic $(ax^2 + bx + c)$ — that is, a quadratic with discriminant $< 0$, so it does *not* factorise over $\mathbb{R}$ — that factor contributes a single term with a **linear numerator**:

$$\text{contribution from }(ax^2 + bx + c) = \dfrac{Bx + C}{ax^2 + bx + c}.$$

Two constants $B$ and $C$ — because the numerator must have degree strictly less than $2$, hence "linear or constant." **Worked in §6.**

> [!warning] The shape of the numerator is locked by the factor's degree
> Each piece in a partial-fraction decomposition is a *proper* rational expression: numerator degree strictly less than denominator degree. So:
> - Linear denominator $(ax + b)$ → constant numerator $A$ (degree $0 < 1$ ✓)
> - Quadratic denominator $(ax^2 + bx + c)$ → linear numerator $Bx + C$ (degree $\leq 1 < 2$ ✓)
> - Cubic denominator $(ax^3 + \ldots)$ → quadratic numerator $Bx^2 + Cx + D$ (degree $\leq 2 < 3$ ✓)
>
> Students sometimes write $\dfrac{B}{x^2 + 1}$ for an irreducible quadratic factor, dropping the $Bx$ term. That's wrong — you've assumed too restrictive a shape and the system will be inconsistent. *Always include the linear-numerator term for irreducible quadratics.*

### Combinations are routine

Any product of these factor types can be combined in one decomposition. For instance, a denominator $(x - 1)(x + 2)^2(x^2 + 4)$ has three distinct factors: one Case A linear, one Case B repeated linear (multiplicity 2), and one Case C irreducible quadratic. Its decomposition has the shape

$$\dfrac{P(x)}{(x-1)(x+2)^2(x^2+4)} = \dfrac{A}{x - 1} + \dfrac{B}{x + 2} + \dfrac{C}{(x + 2)^2} + \dfrac{Dx + E}{x^2 + 4}.$$

Five unknowns. The number of unknowns always equals the degree of $D(x)$ — which is exactly the number of equations you'll get from comparing coefficients.

---

## §3 Why It Works — Two Methods to Find the Coefficients

Once you've written down the decomposition's shape, you have an *identity in $x$*: a statement that two rational functions are equal for *every* value of $x$ (except where denominators vanish). The unknowns are the numerator constants. Two standard methods extract them.

### Method 1 — Multiply through and equate coefficients

Multiply both sides by $D(x)$ to clear all denominators. You get a polynomial identity:

$$P(x) = (\text{combined numerator on the right with constants}\;A, B, C, \ldots).$$

Two polynomials are equal as functions if and only if they have the same coefficients on every power of $x$. So expand the right-hand side, collect like powers of $x$, and equate coefficients term by term. This produces a linear system in the unknowns.

**Pro:** Always works, no special cases.
**Con:** A bit of algebra; for $n$ unknowns you set up an $n \times n$ system.

### Method 2 — Substitute strategic values

Since the identity holds for all $x$, plug in specific values that *kill* most of the unknowns. Distinct linear factors are gold here: setting $x$ equal to a root of one factor zeroes out every other term that contains that factor.

**Pro:** Often gives one unknown per substitution, cleaner arithmetic.
**Con:** Repeated factors and irreducible quadratics need supplemental substitutions or the equate-coefficients method to finish.

In practice, **mix the two**: use strategic substitutions to peel off as many constants as cleanly as possible, then equate coefficients on whatever remains.

### Why uniqueness holds

The decomposition is *unique* once you fix the factorisation of $D(x)$. The proof is short: if two decompositions agreed everywhere, their difference would be the zero rational function — meaning every numerator coefficient in the difference must be $0$. So the constants are forced. (This is also why the method *works*: the system of equations you set up always has a unique solution.)

> [!info] Beyond syllabus — the algebra of why decomposition is possible
> The existence-and-uniqueness theorem for partial fractions is a corollary of two classical results: the **Chinese Remainder Theorem** for polynomial rings $\mathbb{R}[x]$, and the **fundamental theorem of algebra** (every real polynomial factors into linear and irreducible-quadratic factors over $\mathbb{R}$).
>
> Together they say: $\mathbb{R}[x]/(D(x))$ decomposes as a direct sum of simpler quotient rings, one per factor. Partial-fraction decomposition is the manifestation of that direct-sum structure on the field of rational functions $\mathbb{R}(x)$. *That's why it always works, and why the uniqueness comes for free.*

---

## §4 Worked Example — Distinct Linear Factors (Case A)

Decompose $\;\dfrac{3x + 1}{(x - 1)(x + 3)}$.

**Setup.** Both factors are linear and distinct, so the shape is

$$\dfrac{3x + 1}{(x - 1)(x + 3)} = \dfrac{A}{x - 1} + \dfrac{B}{x + 3}.$$

**Multiply through by $(x - 1)(x + 3)$:**

$$3x + 1 = A(x + 3) + B(x - 1). \qquad (\star)$$

This is the *identity in $x$*. Now use Method 2 (strategic substitutions).

**Set $x = 1$** (kills the $B$ term, since $x - 1 = 0$): $\;\;3(1) + 1 = A(1 + 3) + B(0) \;\Rightarrow\; 4 = 4A \;\Rightarrow\; \boxed{A = 1}$.

**Set $x = -3$** (kills the $A$ term, since $x + 3 = 0$): $\;\;3(-3) + 1 = A(0) + B(-3 - 1) \;\Rightarrow\; -8 = -4B \;\Rightarrow\; \boxed{B = 2}$.

**Answer.**

$$\dfrac{3x + 1}{(x - 1)(x + 3)} = \dfrac{1}{x - 1} + \dfrac{2}{x + 3}.$$

**Sanity check.** Recombine: $\dfrac{(x + 3) + 2(x - 1)}{(x - 1)(x + 3)} = \dfrac{3x + 1}{(x - 1)(x + 3)} \;\checkmark$.

> [!tip] The cover-up method (Heaviside) — the speed-run for Case A
> For distinct linear factors there's a beautiful one-line shortcut. To find the constant over $(x - r)$:
>
> 1. **Cover up** the factor $(x - r)$ in the original fraction with your finger (or imagine it crossed out).
> 2. **Substitute $x = r$** into what remains.
> 3. The result *is* the constant.
>
> For $\dfrac{3x + 1}{(x - 1)(x + 3)}$:
> - Constant over $(x - 1)$: cover up $(x - 1)$, substitute $x = 1$ into what's left: $\dfrac{3(1) + 1}{(1) + 3} = \dfrac{4}{4} = 1$. So $A = 1$. ✓
> - Constant over $(x + 3)$: cover up $(x + 3)$, substitute $x = -3$: $\dfrac{3(-3) + 1}{(-3) - 1} = \dfrac{-8}{-4} = 2$. So $B = 2$. ✓
>
> This is just Method 2 (strategic substitution) compressed into a finger-on-the-page shortcut. It works only on the *non-repeated* linear factors; for repeated factors and quadratic factors you need supplementary equations. **Worth memorising — it saves real seconds in a P3 exam.**

The cover-up method is also called **Heaviside's cover-up method** after Oliver Heaviside (1850–1925), the self-taught British engineer-physicist who used it heavily in his work on operational calculus and the telegrapher's equations. He never wrote a formal proof; he just used the shortcut and the answers came out right. Mathematicians later proved he was justified.

---

## §5 Worked Example — Repeated Linear Factor (Case B)

Decompose $\;\dfrac{4x - 1}{(x - 2)^2(x + 1)}$.

**Setup.** $(x - 2)$ has multiplicity $2$, contributing two terms; $(x + 1)$ is a simple linear factor:

$$\dfrac{4x - 1}{(x - 2)^2(x + 1)} = \dfrac{A}{x - 2} + \dfrac{B}{(x - 2)^2} + \dfrac{C}{x + 1}.$$

**Multiply through by $(x - 2)^2(x + 1)$:**

$$4x - 1 = A(x - 2)(x + 1) + B(x + 1) + C(x - 2)^2. \qquad (\star)$$

**Set $x = 2$** (kills both $A$ and $C$ terms): $\;\; 4(2) - 1 = B(2 + 1) \;\Rightarrow\; 7 = 3B \;\Rightarrow\; B = \dfrac{7}{3}$.

**Set $x = -1$** (kills both $A$ and $B$ terms): $\;\; 4(-1) - 1 = C(-1 - 2)^2 \;\Rightarrow\; -5 = 9C \;\Rightarrow\; C = -\dfrac{5}{9}$.

**Now $A$ remains.** Substitution alone won't peel it off cleanly — there's no value of $x$ that zeroes out every $A$-, $B$-, and $C$-term simultaneously without zeroing out the $A$ term too. So fall back to **Method 1** (equate coefficients) on whatever's left.

The cleanest way: pick *any* third value of $x$ (say $x = 0$, which is usually arithmetic-friendly) and use the now-known $B$ and $C$ to solve for $A$.

**Set $x = 0$** in $(\star)$:

$$4(0) - 1 = A(-2)(1) + B(1) + C(-2)^2$$
$$-1 = -2A + \tfrac{7}{3} + 4 \cdot \!\left(-\tfrac{5}{9}\right)$$
$$-1 = -2A + \tfrac{7}{3} - \tfrac{20}{9}.$$

Common denominator on the right: $\tfrac{7}{3} = \tfrac{21}{9}$, so $\tfrac{21}{9} - \tfrac{20}{9} = \tfrac{1}{9}$. Then

$$-1 = -2A + \tfrac{1}{9} \;\Rightarrow\; -2A = -1 - \tfrac{1}{9} = -\tfrac{10}{9} \;\Rightarrow\; A = \dfrac{5}{9}.$$

**Answer.**

$$\dfrac{4x - 1}{(x - 2)^2(x + 1)} = \dfrac{5/9}{x - 2} + \dfrac{7/3}{(x - 2)^2} + \dfrac{-5/9}{x + 1}.$$

**Sanity check.** Pick a friendly $x$ not used to derive any constant — say $x = 3$. LHS: $\dfrac{4(3) - 1}{(3 - 2)^2 (3 + 1)} = \dfrac{11}{4}$. RHS: $\dfrac{5/9}{1} + \dfrac{7/3}{1} + \dfrac{-5/9}{4} = \dfrac{5}{9} + \dfrac{7}{3} - \dfrac{5}{36}$. Common denominator $36$: $\dfrac{20}{36} + \dfrac{84}{36} - \dfrac{5}{36} = \dfrac{99}{36} = \dfrac{11}{4}\,\checkmark$.

> [!warning] You cannot compress the two pieces over $(x - 2)$
> The shape rule says a multiplicity-$2$ linear factor contributes *two* terms: $\dfrac{A}{x - 2}$ AND $\dfrac{B}{(x - 2)^2}$. Students sometimes write only $\dfrac{C}{(x - 2)^2}$, hoping a single term is enough. It isn't — the decomposition would be missing degrees of freedom and the system becomes inconsistent. *Always write all $k$ terms for a multiplicity-$k$ factor.*

---

## §6 Worked Example — Irreducible Quadratic Factor (Case C)

Decompose $\;\dfrac{5x^2 + 2}{(x - 1)(x^2 + 1)}$.

**Setup.** $(x^2 + 1)$ has discriminant $0^2 - 4(1)(1) = -4 < 0$ — irreducible over $\mathbb{R}$. So the shape is

$$\dfrac{5x^2 + 2}{(x - 1)(x^2 + 1)} = \dfrac{A}{x - 1} + \dfrac{Bx + C}{x^2 + 1}.$$

Note the **linear numerator** $Bx + C$ over the quadratic.

**Multiply through by $(x - 1)(x^2 + 1)$:**

$$5x^2 + 2 = A(x^2 + 1) + (Bx + C)(x - 1). \qquad (\star)$$

**Set $x = 1$** (kills the $Bx + C$ term): $\;\; 5(1)^2 + 2 = A(1 + 1) \;\Rightarrow\; 7 = 2A \;\Rightarrow\; A = \dfrac{7}{2}$.

**Now $B$ and $C$ remain.** Substitution doesn't help directly (no real $x$ kills $A(x^2 + 1)$ since it's never zero). Use **Method 1**: expand and equate coefficients.

Expand the right of $(\star)$:

$$A(x^2 + 1) + (Bx + C)(x - 1) = Ax^2 + A + Bx^2 - Bx + Cx - C = (A + B)x^2 + (-B + C)x + (A - C).$$

Equate with the LHS $5x^2 + 0x + 2$:

| Power | LHS | RHS | Equation |
|---|---|---|---|
| $x^2$ | $5$ | $A + B$ | $A + B = 5$ |
| $x^1$ | $0$ | $-B + C$ | $-B + C = 0$ |
| $x^0$ | $2$ | $A - C$ | $A - C = 2$ |

From the first equation with $A = \tfrac{7}{2}$: $B = 5 - \tfrac{7}{2} = \tfrac{3}{2}$.
From the second: $C = B = \tfrac{3}{2}$.
Verify with the third: $A - C = \tfrac{7}{2} - \tfrac{3}{2} = 2 \,\checkmark$.

**Answer.**

$$\dfrac{5x^2 + 2}{(x - 1)(x^2 + 1)} = \dfrac{7/2}{x - 1} + \dfrac{(3/2)x + 3/2}{x^2 + 1} = \dfrac{7/2}{x - 1} + \dfrac{3(x + 1)/2}{x^2 + 1}.$$

> [!tip] When a quadratic factor *does* split — go back to Case A
> Before assuming $(ax^2 + bx + c)$ is irreducible, *always check the discriminant*. If $\Delta = b^2 - 4ac \geq 0$, the quadratic factors over $\mathbb{R}$ — split it into two linear factors and use Case A (or Case B if it factors as a perfect square). Case C is only for genuinely irreducible quadratics ($\Delta < 0$). The 9709 P3 syllabus is explicit that the irreducible quadratic case is the "$ax^2 + c$ with $a, c > 0$" shape (always irreducible) — so on exam day, the quadratic factor is usually $x^2 + 1$, $x^2 + 4$, or similar.

---

## §7 Improper Fractions — Polynomial-Divide First

Partial fractions only decomposes **proper** rational expressions ($\deg P < \deg D$). If you're handed an improper one, the first move is **always** [[Polynomial Division|polynomial long division]] — peel off the polynomial part, leaving a proper-fraction remainder, and only *then* apply partial fractions.

**Example.** Decompose $\;\dfrac{x^3 + 2x}{x^2 - 1}$.

**Step 1 — Recognise improper.** $\deg(\text{num}) = 3$, $\deg(\text{denom}) = 2$. So $\deg P \geq \deg D$ → improper. Polynomial-divide first.

**Step 2 — Polynomial divide.** From [[Polynomial Division]] §7: rewriting the dividend with explicit zeros, $x^3 + 0x^2 + 2x + 0$, dividing by $x^2 - 1$:

- Iteration 1: $x^3 / x^2 = x$. Multiply back: $x(x^2 - 1) = x^3 - x$. Subtract: $0x^2 + 3x + 0$.
- Stop: $\deg(3x) = 1 < \deg(x^2 - 1) = 2$.

So $\dfrac{x^3 + 2x}{x^2 - 1} = x + \dfrac{3x}{x^2 - 1}$.

**Step 3 — Now factor and decompose the proper leftover.** $x^2 - 1 = (x - 1)(x + 1)$, so

$$\dfrac{3x}{(x - 1)(x + 1)} = \dfrac{A}{x - 1} + \dfrac{B}{x + 1}.$$

Cover-up: $A = \dfrac{3(1)}{1 + 1} = \tfrac{3}{2}$; $B = \dfrac{3(-1)}{-1 - 1} = \tfrac{3}{2}$.

**Combined answer.**

$$\dfrac{x^3 + 2x}{x^2 - 1} = x + \dfrac{3/2}{x - 1} + \dfrac{3/2}{x + 1}.$$

> [!warning] Don't try to decompose an improper fraction directly
> If you skip the polynomial-division step, the linear system you set up will be either inconsistent (no solution) or under-determined (you've assumed the wrong shape). Either way, you've wasted exam time. *Always check $\deg P$ vs $\deg D$ first.* If $\deg P \geq \deg D$, polynomial-divide before anything else.

---

## §8 Where Partial Fractions Pays Off

The decomposition itself is just algebra. The reason 9709 P3 spends an entire syllabus point on it is because of the analytic techniques it *unlocks*.

### Application 1 — Integration of rational functions

Each piece in a partial-fraction decomposition is one of the elementary integrals you already know from [[Standard Integrals]]:

| Decomposition piece | Integrates to |
|---|---|
| $\dfrac{A}{ax + b}$ | $\dfrac{A}{a}\ln\lvert ax + b\rvert + C$ |
| $\dfrac{A}{(ax + b)^k}$ ($k \geq 2$) | $\dfrac{-A}{a(k-1)(ax + b)^{k-1}} + C$ (power rule with negative exponent) |
| $\dfrac{Bx + C}{x^2 + a^2}$ | Split: $B \cdot \tfrac{1}{2}\ln(x^2 + a^2)$ from the $f'/f$ pattern, plus $\tfrac{C}{a}\arctan(x/a)$ from the standard arctan integral |

So a rational integral that looks impossible — say, $\displaystyle\int \dfrac{3x + 1}{(x - 1)(x + 3)}\,dx$ — becomes, after decomposition,

$$\int \!\left(\dfrac{1}{x - 1} + \dfrac{2}{x + 3}\right) dx = \ln\lvert x - 1\rvert + 2\ln\lvert x + 3\rvert + C.$$

Done in one line. **This is the standard 9709 P3 §3.5 setup**: a rational integral disguised as something complicated, but trivial after partial fractions.

### Application 2 — Binomial series expansions

To expand $\dfrac{1}{(1 - 2x)(1 + x)}$ as a power series in $x$ (for $\lvert x\rvert$ small enough), partial-fraction decompose first:

$$\dfrac{1}{(1 - 2x)(1 + x)} = \dfrac{2/3}{1 - 2x} + \dfrac{1/3}{1 + x}.$$

Now each piece is a $(1 - u)^{-1}$ or $(1 + u)^{-1}$ — a [[Binomial Series|binomial series]] with $n = -1$. Expand each, keep terms up to whichever degree the question asks, add them. The combined fraction's series is the sum of the simple-fraction series.

### Application 3 — Differential equations

Many separable [[Differential Equations|ODEs]] produce integrals like $\int \dfrac{1}{y(y - 1)}\,dy = \ln\lvert y\rvert - \ln\lvert y - 1\rvert + C$ via partial fractions. The logistic-growth ODE is the canonical example.

### Application 4 — summing a series by the method of differences

The Further Pure payoff, and the one that most looks like magic. A sum such as $\displaystyle\sum_{r=1}^{n}\frac{1}{r(r+1)}$ has no common difference and no common ratio, so neither progression formula touches it — but decomposing the general term turns it into a difference:

$$\frac{1}{r(r+1)} = \frac{1}{r} - \frac{1}{r+1}$$

Now consecutive terms destroy each other in pairs and the whole sum collapses to its two ends, $1 - \frac{1}{n+1}$. **[[Summation of Series]]** is where that machinery lives; what matters here is the direction of the arrow — decomposition is not a step *within* the method, it is what makes the method available at all, and the syllabus wording says outright that producing the decomposition is the candidate's job.

One decomposition-side check is worth carrying over: **for a decomposition to be able to telescope, its coefficients must sum to zero.** In $\frac1r - \frac1{r+1}$ they are $1$ and $-1$; in $\frac{1}{r(r+1)(r+2)} = \frac{1}{2r} - \frac{1}{r+1} + \frac{1}{2(r+2)}$ they are $\tfrac12, -1, \tfrac12$. Coefficients that fail to cancel are the fastest signal that the decomposition itself is wrong.

> [!info] Beyond syllabus — Laplace transforms and inverse transforms
> In an engineering / control-theory context (university level), partial fractions is the workhorse for **inverting Laplace transforms**. A transfer function $H(s) = \dfrac{N(s)}{D(s)}$ gets decomposed, and each piece corresponds to a known time-domain function (exponentials, sines, polynomials in $t$). The system's response is then read off as a sum of those pieces. Partial fractions is the algebraic backbone of every undergraduate signals-and-systems course.

---

## §9 Common Misconceptions

### 1. Forgetting to check proper vs improper

The most common 9709 P3 error: decomposing without checking $\deg P$ vs $\deg D$. The marker writes "must polynomial-divide first" in the margin, you lose 2–3 marks on a 5-mark question.

**Fix.** *First step, always*: count the degree of the numerator and denominator. If $\deg P \geq \deg D$, polynomial-divide. *Only then* set up the partial-fraction shape. This is a 5-second check that saves the question.

### 2. Compressing repeated factors into one term

Writing $\dfrac{P(x)}{(x - 2)^2(x + 1)} = \dfrac{A}{(x - 2)^2} + \dfrac{B}{x + 1}$ instead of the full $\dfrac{A}{x - 2} + \dfrac{B}{(x - 2)^2} + \dfrac{C}{x + 1}$. The shape is wrong — your linear system will have no consistent solution.

**Fix.** Memorise the shape rule: a multiplicity-$k$ linear factor contributes $k$ terms, one for each power $1, 2, \ldots, k$. Always all $k$, never fewer.

### 3. Constant numerator over an irreducible quadratic

Writing $\dfrac{Bx + C}{x^2 + 1}$ as just $\dfrac{C}{x^2 + 1}$, dropping the $Bx$ term. Same effect as misconception 2: insufficient degrees of freedom, inconsistent system.

**Fix.** Numerator degree must be one less than denominator degree. Quadratic denominator → linear numerator $Bx + C$, *both terms*. Cubic denominator (rare at A-Level) → quadratic numerator $Bx^2 + Cx + D$.

### 4. Skipping the cover-up shortcut when it applies

Setting up the equate-coefficients system for a Case-A distinct-linear-factors decomposition costs you a minute of expansion and substitution. The cover-up method is 10 seconds of arithmetic.

**Fix.** *For every distinct linear factor*, do the cover-up first to get its constant. Only fall back to substitution-and-equate-coefficients for repeated factors and irreducible quadratics, where cover-up doesn't apply.

### 5. Treating a factorable quadratic as irreducible

Writing $\dfrac{Bx + C}{x^2 - 4}$ when $x^2 - 4 = (x - 2)(x + 2)$ would have given you two simpler Case-A pieces. The decomposition is still mathematically correct, but the integration and series-expansion steps that follow are harder than they need to be.

**Fix.** *Always* try to factor the quadratic first. Compute the discriminant (or look for an obvious factorisation like difference of squares). Only treat as irreducible if $\Delta < 0$.

### 6. Forgetting the sanity check

The decomposition is a long algebraic process with many places to drop a sign or miscalculate a fraction. The mark scheme catches the error; you don't.

**Fix.** *Always recombine* one of two ways: (a) pick a friendly $x$ value that wasn't used to derive any constant, plug into both sides — they must agree; or (b) put the decomposed pieces over the common denominator and confirm the numerator matches the original $P(x)$. 30 seconds, saves the question.

---

## §10 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** Paper 3 §3.1 — *algebra*. Lists the three covered cases:
- $\dfrac{px + q}{(ax + b)(cx + d)}$ — **distinct linear factors** (Case A).
- $\dfrac{px + q}{(ax + b)(cx + d)^2}$ — **repeated linear factor** (Case B).
- $\dfrac{px^2 + qx + r}{(ax + b)(cx^2 + d)}$ — **irreducible quadratic factor** (Case C, with $c, d > 0$ so $cx^2 + d$ is genuinely irreducible).

**Typical question shape (4–6 marks):**
1. Express $\dfrac{P(x)}{D(x)}$ in partial fractions. *(2–4 marks)*
2. Hence find $\displaystyle\int \dfrac{P(x)}{D(x)}\,dx$. *(2–3 marks)*

— *or* —

2. Hence find the coefficient of $x^n$ in the expansion of $\dfrac{P(x)}{D(x)}$ as a power series. *(3–4 marks)*

The "hence" is the giveaway: partial fractions is the bridge between §3.1 algebra and §3.5 integration / §3.1 binomial expansion.

**Mark scheme patterns:**
- M1 for setting up the correct shape (one mark just for writing the right form with correct numerator types).
- M1 for clearing denominators correctly (the polynomial identity).
- A1 for each constant correctly determined.
- M1 / A1 follow-on for the integration or expansion step.

**Tip.** If the question gives you the partial fractions ("Given that $\dfrac{P(x)}{D(x)} = \dfrac{A}{x - 1} + \ldots$, find $A$, $B$, $C$"), you don't need to determine the shape — you've been told. Go straight to finding the constants. Read the question carefully.

### Cambridge 0606

Partial fractions is **not** in the 0606 syllabus. The 0606 student stops at [[Polynomial Division|polynomial division]] and the [[Remainder and Factor Theorems]]. Partial fractions is purely an A-Level / 9709 P3 topic at this stage. (The vocabulary card [[Algebraic Fractions (Vocab)]] mentions partial fractions as a forward bridge to A-Level, but the technique itself isn't tested at 0606.)

### A-Level (Edexcel / AQA / OCR / MEI / OxAQA 9660)

The same three cases, taught the same way. Edexcel and AQA Pure Mathematics A2 papers test partial fractions as a 4–7 mark question, often as the algebraic setup for a binomial-series or integration question. Mark schemes match the Cambridge patterns above.

OxAQA 9660 lists partial fractions in the algebra section of A2; it does not appear in OxAQA 9260 (IGCSE).

### IB AA

**Topic refs:** AA HL Topic 1 (algebra) — partial fractions appears as a fluency tool inside HL integration problems (Topic 5 calculus). AA SL does not test partial fractions.

The IB AA HL formula booklet does **not** give the partial-fraction shapes; you're expected to know them. Same three cases as A-Level. Often used inside larger questions on integration and rational-function manipulation rather than as a standalone "decompose this" question.

### AP Calculus

**AP Calculus BC** explicitly includes partial fractions for integration: CED Topic 6.10, "Integration Using Partial Fractions." Restricted to **distinct linear factors only** at AP — repeated linear factors and irreducible quadratics are out of scope. So Case A only.

**AP Calculus AB** does *not* include partial fractions.

The AP Calculus reference sheet does not list partial-fraction shapes; you memorise Case A and the cover-up shortcut.

### Beyond high school — University

University courses on **differential equations**, **complex analysis**, and **signals and systems** use partial fractions every week — decomposition over $\mathbb{C}$, the Hermite-Ostrogradski reduction that computer-algebra systems run, and residue calculus, where the cover-up method turns out to have been a residue at a simple pole all along. The Beyond Syllabus section takes each in turn.

---

## Connections

- **Direct prerequisite:** [[Polynomial Division]] — improper fractions must be polynomial-divided before decomposition. The two cards form the §3.1 algebra spine of 9709 P3.
- **Direct prerequisite:** [[Algebraic Fractions (Vocab)]] — the language of rational expressions and the proper-vs-improper distinction.
- **Direct prerequisite:** [[Factorising (Vocab)]] — every partial-fraction problem starts with factoring $D(x)$.
- **Direct prerequisite:** [[Standard Integrals]] — each decomposition piece is a standard integral; the application step relies on knowing them.
- **Tool used:** [[Quadratic Equations]] — for factoring quadratic denominators and testing irreducibility via the discriminant.
- **Tool used:** [[Simultaneous Equations (Vocab)]] — the equate-coefficients method produces a small linear system that has to be solved.
- **Headline application:** [[Integration]] — partial fractions is the standard way to integrate rational functions in 9709 P3 §3.5 / IB HL / AP BC.
- **Application:** [[Binomial Series]] — partial-fraction decomposition lets you expand a complicated rational function as a sum of $(1 + u)^n$ series.
- **Application:** [[Differential Equations]] — separable ODEs frequently produce $\int \tfrac{1}{P(y)}\,dy$ integrals that need partial fractions.
- **Sibling:** [[Integration by Parts]] — a sibling integration technique. Parts handles products; partial fractions handles rational-function quotients. They sometimes combine inside one question.
- **Sibling:** [[Integration by Substitution]] — the other reverse-of-a-rule technique. Substitution reverses the chain rule; partial fractions is purely algebraic preprocessing rather than a rule reversal.
- **Reverse of:** *Combining fractions over a common denominator*. The IGCSE / [[Algebraic Fractions (Vocab)|algebraic fractions]] forward direction; partial fractions is the backward direction.
- **Beyond syllabus parallel:** *Chinese Remainder Theorem in $\mathbb{R}[x]$* — the algebraic structure that makes the decomposition unique and always exist.
- **Historical note:** Oliver Heaviside's cover-up method (1880s) — the speed-shortcut for Case A.
- **For 9709 students:** [[MF19 Reference (9709)]] — partial-fraction shapes are *not* given on MF19. The three cases must be memorised. Standard integrals that the decomposed pieces produce ($\int \tfrac{1}{x}$, $\int \tfrac{1}{x^2 + a^2}$) are partly on MF19 — see the reference card for which.

---

## Beyond Syllabus

### Why partial fractions exists at all — the algebraic structure

Recall the two classical results from §3: the **fundamental theorem of algebra** over $\mathbb{R}$, which guarantees $D(x)$ factors into linear and irreducible-quadratic pieces, and the **Chinese Remainder Theorem** for $\mathbb{R}[x]$, which turns that factorisation into a direct-sum decomposition $\mathbb{R}[x]/(D) \cong \mathbb{R}[x]/(D_1) \oplus \ldots \oplus \mathbb{R}[x]/(D_k)$ for pairwise-coprime factors. Partial fractions is that direct sum written out on the field of rational functions $\mathbb{R}(x)$ — which is why it always works, and why uniqueness comes for free.

Everything below is what happens when you push that structure further.

### Over $\mathbb{C}$, the irreducible-quadratic case disappears

Every irreducible-over-$\mathbb{R}$ quadratic factors over $\mathbb{C}$ into a pair of complex-conjugate linear factors. So if you allow complex coefficients, **every** partial-fraction decomposition is a sum of Case-A-like terms $\dfrac{A_k}{x - r_k}$ (one per pole), with the $r_k$ possibly complex and the $A_k$ possibly complex.

This is the standard form in **complex analysis** and **engineering**. The real-quadratic-form decomposition is recovered by pairing the complex-conjugate terms back together — which is why the real-form numerator is *linear* ($Bx + C$), not just constant: it carries the real and imaginary parts of the complex residue jointly.

### The cover-up method generalises to "residues"

Heaviside's cover-up shortcut for distinct linear factors, viewed through the complex-analysis lens, is the calculation of the **residue** of the rational function at each simple pole. The residue at $x = r$ is:

$$\mathrm{Res}_{x = r} \dfrac{P(x)}{D(x)} = \lim_{x \to r} (x - r)\,\dfrac{P(x)}{D(x)} = \dfrac{P(r)}{D'(r)}.$$

The first equality is exactly Heaviside's "cover up $(x - r)$ and substitute $x = r$." The second equality (l'Hôpital-style) is a slick alternative, useful when $D(x)$ isn't already factored.

Residue calculus is the engine of contour integration in complex analysis — used in physics for Green's functions, in number theory for the Riemann zeta function, in engineering for inverse Laplace and Fourier transforms.

### The Hermite-Ostrogradski algorithm

Computer-algebra systems (Mathematica, SymPy, Maple) compute integrals of rational functions in two phases:

1. **Hermite reduction** — algorithmically separate the *rational part* of the antiderivative (the bit that comes from the higher-power terms in repeated factors) from the *logarithmic-and-arctan part* (the bit that comes from the multiplicity-1 terms). This is faster than full partial-fraction decomposition.
2. **Lazard-Rioboo-Trager algorithm** — handle the logarithmic-and-arctan part using a clever combination of resultants and gcd computations.

Hand-computed partial fractions is the schoolroom version of phase 1.

### Liouville's theorem says all rational antiderivatives are partial-fraction sums

**Liouville's theorem (1833)** says: every elementary antiderivative of a rational function is a sum of (a) a rational function and (b) finitely many constant multiples of logarithms of polynomials. *Partial fractions is the constructive proof of Liouville's theorem in the rational-function case.*

This is a deep result: it says the integration toolkit you need for rational functions is exactly the toolkit partial fractions hands you. There's no clever trick that produces a fundamentally different kind of antiderivative. All paths lead through log + arctan + power-rule.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{P(x)}{D(x)}$ | `\dfrac{P(x)}{D(x)}` | Display-size rational expression — preferred in tables and identities |
| $\deg P$ | `\deg P` | Degree of $P$; use `\deg` for upright text |
| $\equiv$ | `\equiv` | Identity in $x$ — used to flag "true for all $x$" rather than a conditional equation |
| $\stackrel{?}{=}$ | `\stackrel{?}{=}` | "Equals?" — the sanity-check step |
| $\Delta = b^2 - 4ac$ | `\Delta = b^2 - 4ac` | Discriminant — used to test irreducibility of a quadratic |
| $\mathrm{Res}_{x=r} f(x)$ | `\mathrm{Res}_{x=r} f(x)` | Residue at the pole $r$ (beyond syllabus) |
| $\boxed{\text{result}}$ | `\boxed{...}` | Boxed final answer — used in exam writing |
| $\dfrac{A}{(ax + b)^k}$ | `\dfrac{A}{(ax + b)^k}` | The general term in a repeated-linear-factor decomposition |
| $\dfrac{Bx + C}{ax^2 + bx + c}$ | `\dfrac{Bx + C}{ax^2 + bx + c}` | The general term in an irreducible-quadratic decomposition |

---
chinese: 换元方程 (huàn yuán fāngchéng) / 代换法
prerequisites:
  - "[[Quadratic Equations]]"
  - "[[Indices in Algebra (Vocab)]]"
  - "[[Logarithms]]"
  - "[[Trigonometric Equations]]"
leads_to:
  - "[[Integration by Substitution]]"
  - "[[Differential Equations]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-4-3
  - type/deep
  - type/technique
  - misconception/forgot-to-back-substitute
  - misconception/dropped-domain-restriction
  - misconception/missed-the-disguise
---

# Substitution Equations 换元方程

## Definition

A **substitution equation** is an equation that is *not* immediately a quadratic, but *becomes* one after a clever change of variable $u = g(x)$. The general form:

$$A \cdot \bigl[g(x)\bigr]^2 \;+\; B \cdot g(x) \;+\; C \;=\; 0.$$

If you can spot the **disguise** — that some expression $g(x)$ is being squared — substitute $u = g(x)$ and the equation becomes the familiar

$$A u^2 + B u + C = 0.$$

Solve in $u$ (factor or quadratic formula), then **translate back** to find $x$.

The skill being tested is **pattern recognition**. Once $u = g(x)$ is identified, the calculus is mechanical. The art is in seeing the squared structure inside an equation that looks like a quartic, an exponential, a trig equation, or a logarithm.

This card is the *final* card on the 0606 syllabus list. It also forms the conceptual prequel to [[Integration by Substitution]] — both rely on the same idea: a change of variables turns an unfamiliar problem into a familiar one.

### 中文锚点

**换元方程 (huàn yuán fāngchéng)** = 通过**代换** (dàihuàn) $u = g(x)$，把一个看起来不是二次的方程**伪装解开**，变成关于 $u$ 的二次方程。

五步法：
1. **找到代换** $u = g(x)$ — 看哪个表达式被"平方"了
2. **代入** — 把方程变成 $Au^2 + Bu + C = 0$
3. **解 $u$** — 因式分解或二次公式
4. **回代** — 把每个 $u$ 解换回 $x$，解 $g(x) = u_1$ 和 $g(x) = u_2$
5. **检查定义域** — 有些 $u$ 值不合法（如 $u = e^x$ 必须 $> 0$，$u = \sin x$ 必须 $\in [-1, 1]$）

最常见的"伪装"：

| 方程类型 | 代换 |
|---|---|
| $x^4$ 含偶次幂 | $u = x^2$ |
| $x^{2/3}$ 类分数次幂 | $u = x^{1/3}$ |
| 指数方程 $e^{2x}, 4^x = (2^x)^2$ | $u = e^x$ 或 $u = 2^x$ |
| 三角方程 $\sin^2 x$ | $u = \sin x$ |
| 对数方程 $(\ln x)^2$ | $u = \ln x$ |

---

## The Five-Step Recipe

1. **Spot the disguise.** Find the expression $g(x)$ such that the equation contains $[g(x)]^2$ as well as $g(x)$ (or constants). Common patterns:
   - "Two appearances of $x^n$ where one is $x^{2n}$" → substitute $u = x^n$
   - "Two appearances of $e^{kx}$ where one is $e^{2kx}$" → substitute $u = e^{kx}$
   - "$\sin^2 x$ and $\sin x$ both appear" → substitute $u = \sin x$
2. **Substitute.** Replace every $g(x)$ with $u$. The equation becomes a quadratic in $u$.
3. **Solve the quadratic.** Factor or use the quadratic formula. You usually get two values $u_1, u_2$.
4. **Translate back.** For *each* value of $u$, solve $g(x) = u_i$ for $x$. This step often introduces multiple $x$-values per $u$-value.
5. **Check domain restrictions.** Some $u$-values are *invalid* in the original equation (e.g., $e^x > 0$ rejects $u \le 0$; $\sin x \in [-1, 1]$ rejects $|u| > 1$; $x^{2/3}$ requires $x \ge 0$ if defined as $\sqrt[3]{x^2}$).

> [!warning] Translating back is non-negotiable
> Many 0606 students stop at step 3 and report the values of $u$ as the answer. **Wrong** — the question asked for $x$, not $u$. Always make the back-substitution explicit, and write the final answer in terms of $x$. The substitution is just an intermediate algebraic move; the question is still about $x$.

---

## Worked Examples

![[substitution-mapping-quadratic-to-quartic.svg]]

Above: the same quadratic equation $u^2 - 5u + 4 = 0$ becomes the biquadratic $x^4 - 5x^2 + 4 = 0$ when $u = x^2$. Each $u$-root maps to *two* $x$-roots (its $\pm\sqrt{u}$), so the parabola's two roots become the quartic's four. Always read off all branches when translating back.

### Example 1 — biquadratic (the simplest disguise)

> Solve $x^4 - 5x^2 + 4 = 0$.

**Spot.** $x^4 = (x^2)^2$, so substitute $u = x^2$.

**Substitute.** $u^2 - 5u + 4 = 0$.

**Solve in $u$.** Factor: $(u - 1)(u - 4) = 0$, so $u = 1$ or $u = 4$.

**Translate back.** Both values are positive (so they're valid since $x^2 \ge 0$).

- $u = 1$ → $x^2 = 1$ → $x = \pm 1$.
- $u = 4$ → $x^2 = 4$ → $x = \pm 2$.

**Final answer.** $\boxed{x = \pm 1 \;\text{ or }\; x = \pm 2}$ — *four* solutions in $x$ from *two* solutions in $u$.

### Example 2 — fractional powers (the canonical 0606 form)

> Solve $x^{4/3} + x^{2/3} - 12 = 0$.

**Spot.** $x^{4/3} = (x^{2/3})^2$, so substitute $u = x^{2/3}$.

**Substitute.** $u^2 + u - 12 = 0$.

**Solve in $u$.** Factor: $(u + 4)(u - 3) = 0$, so $u = -4$ or $u = 3$.

**Domain check.** $u = x^{2/3}$. Reading $x^{2/3}$ as $(\sqrt[3]{x})^2$, the result is always $\ge 0$ for any real $x$. So $u = -4$ is **rejected** (no real $x$ gives a negative $x^{2/3}$).

**Translate back.** $u = 3$:

$$x^{2/3} = 3 \;\;\Longrightarrow\;\; x^2 = 3^3 = 27 \;\;\Longrightarrow\;\; x = \pm \sqrt{27} = \pm 3\sqrt{3}.$$

**Final answer.** $\boxed{x = \pm 3\sqrt{3}}$.

> [!info] Why the rejected $u$-value would have given complex roots
> If we kept $u = -4$ and solved $x^{2/3} = -4$, we'd need $x^2 = (-4)^3 = -64$, giving $x = \pm 8i$ — purely imaginary. At 0606 level, we restrict to real solutions and reject. At A-Level / IB HL with complex numbers in scope, you'd report all four roots: $\pm 3\sqrt{3}$ and $\pm 8i$.

### Example 3 — exponential equation

> Solve $e^{2x} - 7e^x + 12 = 0$.

**Spot.** $e^{2x} = (e^x)^2$, so substitute $u = e^x$.

**Substitute.** $u^2 - 7u + 12 = 0$.

**Solve in $u$.** Factor: $(u - 3)(u - 4) = 0$, so $u = 3$ or $u = 4$.

**Domain check.** $u = e^x > 0$ always — both values are positive, so both are valid.

**Translate back.**

- $u = 3$ → $e^x = 3$ → $x = \ln 3$.
- $u = 4$ → $e^x = 4$ → $x = \ln 4$.

**Final answer.** $\boxed{x = \ln 3 \;\text{ or }\; x = \ln 4}$.

### Example 4 — disguised exponential (different bases)

> Solve $4^x - 5 \cdot 2^x + 4 = 0$.

**Spot.** $4^x = (2^2)^x = (2^x)^2$, so substitute $u = 2^x$.

**Substitute.** $u^2 - 5u + 4 = 0$.

**Solve in $u$.** Factor: $(u - 1)(u - 4) = 0$, so $u = 1$ or $u = 4$.

**Domain check.** $u = 2^x > 0$ always — both valid.

**Translate back.**

- $u = 1$ → $2^x = 1$ → $x = 0$ (since $2^0 = 1$).
- $u = 4$ → $2^x = 4$ → $x = 2$ (since $2^2 = 4$).

**Final answer.** $\boxed{x = 0 \;\text{ or }\; x = 2}$.

### Example 5 — trig equation (with domain rejection)

> Solve $2\sin^2 x + 3\sin x - 2 = 0$ for $0 \le x \le 2\pi$.

**Spot.** $\sin^2 x = (\sin x)^2$, so substitute $u = \sin x$.

**Substitute.** $2u^2 + 3u - 2 = 0$.

**Solve in $u$.** Factor: $(2u - 1)(u + 2) = 0$, so $u = \tfrac{1}{2}$ or $u = -2$.

**Domain check.** $u = \sin x \in [-1, 1]$. So $u = -2$ is **rejected** (sine never reaches $-2$).

**Translate back.** $u = \tfrac{1}{2}$ means $\sin x = \tfrac{1}{2}$ on $[0, 2\pi]$.

From [[Trigonometric Equations]]: $\sin x = \tfrac{1}{2}$ at $x = \tfrac{\pi}{6}$ (principal) and $x = \pi - \tfrac{\pi}{6} = \tfrac{5\pi}{6}$ (second solution per period).

**Final answer.** $\boxed{x = \tfrac{\pi}{6} \;\text{ or }\; x = \tfrac{5\pi}{6}}$.

### Example 6 — logarithm equation

> Solve $(\ln x)^2 - 3 \ln x + 2 = 0$.

**Spot.** $(\ln x)^2$ and $\ln x$ both appear, so substitute $u = \ln x$.

**Substitute.** $u^2 - 3u + 2 = 0$.

**Solve in $u$.** Factor: $(u - 1)(u - 2) = 0$, so $u = 1$ or $u = 2$.

**Domain check.** $u = \ln x$ is defined for $x > 0$. Both values of $u$ are real, so both translate back.

**Translate back.**

- $u = 1$ → $\ln x = 1$ → $x = e^1 = e$.
- $u = 2$ → $\ln x = 2$ → $x = e^2$.

**Final answer.** $\boxed{x = e \;\text{ or }\; x = e^2}$.

---

## Spotting the Disguise — patterns to recognise

The substitution leaps off the page once you've seen a few:

| Equation pattern | Substitution | Why |
|---|---|---|
| $ax^4 + bx^2 + c = 0$ | $u = x^2$ | $x^4 = (x^2)^2$ |
| $ax^{2n} + bx^n + c = 0$ | $u = x^n$ | $x^{2n} = (x^n)^2$ |
| $ax^{4/3} + bx^{2/3} + c = 0$ | $u = x^{2/3}$ | $x^{4/3} = (x^{2/3})^2$ |
| $ae^{2x} + be^x + c = 0$ | $u = e^x$ | $e^{2x} = (e^x)^2$ |
| $a \cdot 9^x + b \cdot 3^x + c = 0$ | $u = 3^x$ | $9^x = (3^x)^2$ |
| $a \sin^2 x + b \sin x + c = 0$ | $u = \sin x$ | $\sin^2 x = (\sin x)^2$ |
| $a \cos^2 x + b \cos x + c = 0$ | $u = \cos x$ | $\cos^2 x = (\cos x)^2$ |
| $a \tan^2 x + b \tan x + c = 0$ | $u = \tan x$ | analogous |
| $a (\ln x)^2 + b \ln x + c = 0$ | $u = \ln x$ | direct |
| $a x + b/x + c = 0$ (multiply by $x$) | sometimes $u = x + 1/x$ | for *palindromic* coefficients |

> [!tip] The "ratio test" for spotting a substitution
> If two terms in your equation have exponents (or arguments) in a *2-to-1 ratio*, substitution will work. $x^4$ and $x^2$ — ratio $4:2 = 2:1$ ✓. $e^{2x}$ and $e^x$ — ratio $2:1$ ✓. $\sin^2 x$ and $\sin x$ — ratio $2:1$ ✓. $9^x$ and $3^x$ — note $9 = 3^2$, so the *exponential bases* have ratio $2:1$ in their logs ✓. If the ratio isn't $2:1$, try a different substitution.

---

## Common Mistakes

1. **Reporting $u$-values as the answer.** The substitution is intermediate; the final answer is in $x$. Always back-substitute and solve $g(x) = u_i$ explicitly.
2. **Forgetting that $u = x^2$ produces two $x$-values per $u$-root.** $u = 4$ means $x = \pm 2$, not just $x = 2$. Each square-root branch matters unless the original problem restricts to $x \ge 0$.
3. **Missing the domain restriction.** $u = e^x$ must be positive, so a negative root in $u$ is rejected (no $x$). $u = \sin x$ must be in $[-1, 1]$. $u = x^{2/3}$ must be $\ge 0$. Always check.
4. **Choosing the wrong substitution.** If the equation has $x^3$ and $x^2$ (ratio $3:2$, not $2:1$), no quadratic substitution works directly — you'd need a cubic factorisation instead. The substitution trick only handles $2:1$ ratios.
5. **Forgetting to apply the substitution to all terms.** For $x^{4/3} + x^{2/3} - 12$, the constant $-12$ has *no* $x^{2/3}$ in it — leave it alone. Don't accidentally write $u^2 + u - 12u$ or similar.
6. **Sloppy back-translation in trig.** $\sin x = 1/2$ has *two* solutions per $2\pi$ period (one in QI, one in QII). Don't lose half the solutions by only writing the principal value. See [[Trigonometric Equations]] for the full treatment.

---

## Exam Notes

### Cambridge 0606

**Syllabus ref:** §4.3 — use substitution to form and solve a quadratic. The standard exam phrasings:

- **Pattern A — direct biquadratic.** "Solve $x^4 - 13x^2 + 36 = 0$." Substitute $u = x^2$, factor, four solutions.
- **Pattern B — fractional power.** "Solve $x^{4/3} + x^{2/3} - 12 = 0$." Substitute $u = x^{2/3}$, factor, reject negative $u$, two solutions in $\pm$.
- **Pattern C — exponential.** "Solve $e^{2x} - 5e^x + 6 = 0$." Substitute $u = e^x$, take logs to recover $x$.
- **Pattern D — disguised exponential with related bases.** "Solve $9^x - 4 \cdot 3^x + 3 = 0$." Recognise $9^x = (3^x)^2$, substitute.
- **Pattern E — trig with domain.** "Solve $2\cos^2 x + \cos x - 1 = 0$ for $0 \le x \le 2\pi$." Substitute $u = \cos x$, find solutions in domain.
- **Pattern F — log.** "Solve $(\log_3 x)^2 - 5 \log_3 x + 6 = 0$." Substitute $u = \log_3 x$.

> [!tip] Show every step — the markscheme rewards bookkeeping
> 0606 markschemes for §4.3 typically award marks for: (1) correct substitution, (2) correct quadratic in $u$, (3) correct $u$-roots, (4) translating back, (5) final $x$-values. Each step is a separate mark. Even if you make an arithmetic slip late, earlier marks are secured by clearly written work. Write "let $u = \ldots$" at the top and label every line.

### A-Level / 9709 / IB AA / AP

A-Level adds:
- **Cubic-in-disguise via substitution** — e.g., $x^6 - 9x^3 + 8 = 0$ via $u = x^3$ becomes $u^2 - 9u + 8 = 0$.
- **Tschirnhaus transformations** — substitutions that *eliminate* a term in a polynomial (e.g., reducing a general cubic to a depressed cubic). Critical machinery in Cardano's formula.
- **Reciprocal substitutions** $u = x + 1/x$ for *palindromic* polynomials (those with coefficients reading the same forwards and backwards).
- **Trigonometric substitutions** in integration ($x = \sin\theta$, $x = \tan\theta$) — same idea, different setting.

AP Calculus and IB AA HL bring this technique into integration ([[Integration by Substitution]]), where the substitution turns one integrand into another more tractable one. The algebra here is the prequel.

---

## Beyond Syllabus

### The General Idea — Change of Variables

What's really going on is a **change of variables**. The original equation lives in one coordinate system (the $x$-axis); a smart substitution transports the problem to a new system (the $u$-axis) where the equation has a familiar shape. After solving, you transport the answer back.

This pattern appears everywhere in mathematics:

- **Integration by substitution** — $\int f(g(x)) g'(x)\, dx = \int f(u)\, du$ via $u = g(x)$. Same idea: change variables to make the integrand familiar. See [[Integration by Substitution]].
- **Differential equations** — many ODEs become *linear* (or *separable*) after a substitution like $u = y/x$ (homogeneous equations) or $v = 1/y$ (Bernoulli equations).
- **Fourier transforms** — change from time-domain to frequency-domain to convert convolutions into multiplications. The whole field of signal processing is one massive substitution.
- **Laplace transforms** — change from $f(t)$ to $F(s)$ to convert differential equations into algebraic ones. Engineers solve circuit problems this way.
- **Eigenvalue problems** in linear algebra — diagonalising a matrix is a change of basis (variables) that makes the matrix's action trivial in the new coordinates.

The 0606 substitution is the first instance. Once you see the pattern, you'll see it for the rest of your mathematical life.

### Tschirnhaus and the Path to Cardano's Formula

In 1683, **Ehrenfried Walther von Tschirnhaus** discovered a remarkable trick: the substitution $x = y - \dfrac{b}{3a}$ applied to a general cubic $ax^3 + bx^2 + cx + d = 0$ *eliminates the $y^2$ term*, producing a so-called **depressed cubic** $y^3 + py + q = 0$. From there, Cardano's formula does the rest. Tschirnhaus's substitution is *the* reason cubic formulas exist in workable form.

The same trick applies to quartics: a translation eliminates the cubic term, leaving $y^4 + py^2 + qy + r = 0$ — and Ferrari's quartic formula proceeds from there. Both 16th-century formulas (Cardano cubic, Ferrari quartic) are made accessible by *Tschirnhaus's substitution game*.

This was supposed to keep working for quintics. It didn't (Galois 1830s). But the *technique* — find a substitution that makes a hard problem easier — is universal.

### Solvability by Radicals — when substitutions run out

Galois theory studies *which* polynomials can be solved by repeated extraction of roots and arithmetic — i.e. by *substitutions of radicals*. The cubic and quartic *can* be solved this way (Cardano, Ferrari). The general quintic **cannot** (Abel-Ruffini, Galois). The reason: the *symmetry group* of the roots ($S_5$ for a generic quintic) is "too rich" for any chain of substitutions to fully untangle.

So the 0606 §4.3 technique — substitute, solve, back-substitute — has a fundamental limit. It works for polynomials whose root-symmetry group has a "solvable" structure (in Galois's sense). Quintics and higher are where it breaks.

### Substitution as the Foundational Move

**Substitution is mathematics's most universal idea.** When something is too hard, replace part of it with a new symbol, manipulate the simpler thing, then put the original back. Every theorem you'll ever prove uses this move at some level. From 0606 §4.3 to topology to category theory, substitution is what *change of perspective* looks like in symbols. The 0606 form is humble — but it's the same move that powers Fourier analysis and Lie group theory.

---

## Connections

- **Prerequisite:** [[Quadratic Equations]] — once the substitution is done, you're solving a quadratic
- **Prerequisite:** [[Indices in Algebra (Vocab)]] — fractional and large-integer exponents need fluency
- **Prerequisite:** [[Logarithms]] — exponential substitution problems require taking logs in step 4
- **Prerequisite:** [[Trigonometric Equations]] — trig substitutions lean on the standard solving recipe
- **Sibling:** [[Quadratic Inequalities]] — same disguised-quadratic recognition skill, applied to inequalities
- **Forward:** [[Integration by Substitution]] — the calculus version of the same idea
- **Beyond syllabus:** *Tschirnhaus transformation* (cubic and quartic depressions), *Galois theory* (when substitutions run out at degree 5), *change of variable in differential equations* (homogeneous, Bernoulli), *eigenvalue problems* (diagonalisation as substitution)
- **Application:** *signal processing* — Fourier transform is a global substitution from time to frequency
- **Application:** *control theory* — Laplace transform substitution from $t$ to $s$

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $u = g(x)$ | `u = g(x)` | The substitution itself |
| $A u^2 + B u + C = 0$ | `Au^2 + Bu + C = 0` | The quadratic in $u$ |
| $x^{4/3} + x^{2/3} - 12 = 0$ | `x^{4/3} + x^{2/3} - 12 = 0` | The canonical fractional-power form |
| $e^{2x} - 7e^x + 12 = 0$ | `e^{2x} - 7e^x + 12 = 0` | The canonical exponential form |
| $u = x^2, u = e^x, u = \sin x, u = \ln x$ | individual entries | Standard substitutions |
| $g(x) = u_i$ | `g(x) = u_i` | The translate-back step |

---
chinese: 标准积分 (biāozhǔn jīfēn)
prerequisites:
  - "[[Hyperbolic Functions]]"
  - "[[Integration]]"
  - "[[Differentiation Rules]]"
  - "[[Logarithms]]"
  - "[[Trigonometric Identities]]"
  - "[[Chain Rule]]"
  - "[[Maclaurin Series]]"
leads_to:
  - "[[Integration by Substitution]]"
  - "[[Integration by Parts]]"
  - "[[Partial Fractions]]"
  - "[[Differential Equations]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/IB-HL
  - level/AP
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-3-5
  - syllabus/9231-2-4
  - type/reference
  - type/theorem
  - notation/integral
  - misconception/forgetting-absolute-value-in-ln
  - misconception/missing-linear-inside-factor
  - misconception/wrong-arctan-coefficient
---

# Standard Integrals 标准积分

> *Differentiation has rules. Integration has* recognition. *The card you're reading is the recognition table — every elementary function whose antiderivative you should know on sight, with the "why" attached so the table is memorable rather than memorised.*
>
> *Companion to [[Differentiation Rules]] — read each row right-to-left and you have a derivative; read it left-to-right and you have an integral. Most of this card's content is exactly that re-reading. The genuinely new pieces are the $\ln \lvert x \rvert$ subtlety, the* $f'/f$ *pattern, and the inverse-trig family.*

## What this card is for

[[Integration]] introduces antidifferentiation and the basic Power Rule. [[Differentiation Rules]] is the master table for differentiation. **Standard Integrals** is the master table for integration — what you need to recognise without having to derive it under exam pressure. Specifically the 9709 P3 §3.5 / IB AA HL / AP BC level: the linear-inside extension, the $\ln \lvert x \rvert$ result, the $f'/f$ pattern, the inverse-trig family ($\arctan$ on 9709; $\arcsin$ on IB/AP), the $\sec x$ trick (beyond syllabus but pedagogically essential), and completing the square for shifted denominators.

This card *closes 9709 P3 §3.5* — pair with [[Integration by Substitution]] and [[Integration by Parts]] (already in the vault) and the trio handles every P3 integration question.

## The Reference Table

Each row is a derivative read backwards. The full table — including the $C$ on every right-hand side, even when omitted below for compactness — covers everything 9709 P3 / IB AA HL / AP BC need.

**Memorise? legend** (the four right-hand columns on every table give per-board status — pick the column for *your* exam):

- ✅ **Given** on the board's formula booklet — recognise, don't memorise.
- 📝 **Memorise** — on syllabus, not given on the booklet. Know cold.
- 🛠 **Derive** — recognise the pattern, work it on the fly (linear-inside rule, $f'/f$ recognition, etc.). Counts as memorisation in practice but compresses to one rule + many applications.
- ⚪ **Off-syllabus** — not on this board; you can skip unless you're cross-prepping.

**Source-of-truth references for each column** (verified against the official formula booklets):

- **9709** — Cambridge International A-Level Mathematics 9709, MF19 booklet. See [[MF19 Reference (9709)]].
- **IAL** — Pearson Edexcel International A-Level Mathematics, formula booklet (Pure-only path; Further Maths students get more). See [[Edexcel IAL Reference]].
- **9660** — Oxford International AQA International A-Level Mathematics. See [[OxAQA 9660 Reference]].
- **AP** — College Board AP Calculus AB and BC. *No formula sheet provided on exam day* — every entry below that's on syllabus is 📝. See [[AP Calculus Reference]].

### Foundational (on every syllabus)

| $f(x)$ | $\displaystyle \int f(x) \, dx$ | 9709 | IAL | 9660 | AP |
|---|---|:---:|:---:|:---:|:---:|
| $x^n,\; n \neq -1$ | $\dfrac{x^{n+1}}{n+1}$ | ✅ | 📝 | 📝 | 📝 |
| $\dfrac{1}{x}$ | $\ln \lvert x \rvert$ | ✅ | 📝 | 📝 | 📝 |
| $e^x$ | $e^x$ | ✅ | 📝 | 📝 | 📝 |
| $\sin x$ | $-\cos x$ | ✅ | 📝 | 📝 | 📝 |
| $\cos x$ | $\sin x$ | ✅ | 📝 | 📝 | 📝 |
| $\sec^2 x$ | $\tan x$ | ✅ | ✅ | ✅ | 📝 |

> [!info] Why MF19 dominates this row
> Cambridge MF19 reprints the foundational integrals on its standard P1+P3 page. IAL, 9660, and AP omit them — IAL because P1 is empty in the booklet and the basics live in your head from school; 9660 because the booklet's diff/integration tables only show the *non-obvious* extensions (starting at $\sin^{-1}$ on diff and $\tan x$ on int); AP because there is no booklet at all. **For three of four boards the foundational table is yours to memorise.** $\sec^2 x \to \tan x$ is the exception — IAL and 9660 list $\sec^2 kx \to \frac{1}{k}\tan kx$, which subsumes the $k = 1$ base case.

### Linear-inside extension

If the inside is linear in $x$ — $ax + b$ — the antiderivative gets a compensating factor of $1/a$ (chain rule, in reverse). For all four boards: derive the full row from the linear-inside *rule*, not as six separate formulas.

| $f(x)$ | $\displaystyle \int f(x) \, dx$ | 9709 | IAL | 9660 | AP |
|---|---|:---:|:---:|:---:|:---:|
| $(ax + b)^n$ | $\dfrac{(ax + b)^{n+1}}{a(n+1)}$ | 🛠 | 🛠 | 🛠 | 🛠 |
| $\dfrac{1}{ax + b}$ | $\dfrac{1}{a} \ln \lvert ax + b \rvert$ | 🛠 | 🛠 | 🛠 | 🛠 |
| $e^{ax + b}$ | $\dfrac{1}{a} e^{ax + b}$ | 🛠 | 🛠 | 🛠 | 🛠 |
| $\sin(ax + b)$ | $-\dfrac{1}{a} \cos(ax + b)$ | 🛠 | 🛠 | 🛠 | 🛠 |
| $\cos(ax + b)$ | $\dfrac{1}{a} \sin(ax + b)$ | 🛠 | 🛠 | 🛠 | 🛠 |
| $\sec^2(ax + b)$ | $\dfrac{1}{a} \tan(ax + b)$ | 🛠 | ✅ | ✅ | 🛠 |

> [!info] Why the linear-inside row is 🛠 not ✅
> MF19, IAL, 9660 all list *base* forms (e.g. $\int e^x = e^x$). The general linear-inside extensions (e.g. $\int e^{ax+b} = \tfrac{1}{a}e^{ax+b}$) are *not* individually given — but they're a one-line chain-rule reversal from the base. **Don't try to memorise six linear-inside formulas; memorise the rule.** Exception: IAL and 9660 *do* explicitly list $\int \sec^2 kx = \tfrac{1}{k}\tan kx$ on their booklets, presumably because the symbolic-differentiation muscle to derive that one is shaky for many students.

### Inverse-trig family

The new entries this card introduces. **All require absolute-value-of-$a$ care if $a$ might be negative; the standard convention takes $a > 0$.**

| $f(x)$                         | $\displaystyle \int f(x) \, dx$                                                            |      9709      |  IAL  | 9660  |          AP          |
| ------------------------------ | ------------------------------------------------------------------------------------------ | :------------: | :---: | :---: | :------------------: |
| $\dfrac{1}{x^2 + a^2}$         | $\dfrac{1}{a}\arctan\!\left(\dfrac{x}{a}\right)$                                           |       ✅        | ⚪ FP3 |   ✅   |          📝          |
| $\dfrac{1}{x^2 - a^2}$         | $\dfrac{1}{2a}\ln\!\left\lvert\dfrac{x - a}{x + a}\right\rvert$ ($x > a$)                  |       ✅        | ⚪ FP3 |   ✅   | 🛠 partial fractions |
| $\dfrac{1}{a^2 - x^2}$         | $\dfrac{1}{2a}\ln\!\left\lvert\dfrac{a + x}{a - x}\right\rvert$ ($\lvert x\rvert < a$)     |       ✅        | ⚪ FP3 |   ✅   | 🛠 partial fractions |
| $\dfrac{1}{\sqrt{a^2 - x^2}}$  | $\arcsin\!\left(\dfrac{x}{a}\right)$                                                       | ⚪ off-syllabus | ⚪ FP3 |   ✅   |          📝          |
| $\dfrac{1}{\sqrt{a^2 + x^2}}$  | $\sinh^{-1}\!\left(\dfrac{x}{a}\right) = \ln\!\lvert x + \sqrt{a^2 + x^2}\rvert$           |  ⚪ 9231 only   | ⚪ FP3 |   ✅   |    ⚪ off-syllabus    |
| $\dfrac{1}{\sqrt{x^2 - a^2}}$  | $\cosh^{-1}\!\left(\dfrac{x}{a}\right) = \ln\!\lvert x + \sqrt{x^2 - a^2}\rvert$ ($x > a$) |  ⚪ 9231 only   | ⚪ FP3 |   ✅   |    ⚪ off-syllabus    |
| $\dfrac{1}{x\sqrt{x^2 - a^2}}$ | $\dfrac{1}{a}\,\mathrm{arcsec}\!\left(\dfrac{\lvert x\rvert}{a}\right)$                    |     ⚪ uni      | ⚪ uni | ⚪ uni |   📝 (rare AB/BC)    |

> [!warning] The biggest cross-board asymmetry on this card
> Look at the *first three rows*: 9709 gives all three on MF19, 9660 gives all three on its booklet, IAL gives *none* of them on Pure (FP3 only), AP gives *none* in any form (memorise + partial-fraction derivation). **Pure-only IAL students have the worst deal of any board on these specific integrals.** They're standard P3 fare but the booklet leaves them out, while syllabus expects familiarity. Memorise or be ready to re-derive.
>
> The fourth row ($\arcsin$): 9709 doesn't have it (Cambridge keeps inverse-sin for 9231 Further Math); IAL's Pure booklet doesn't either (FP3 again); 9660 *does* (most generous); AP *expects it* but provides no booklet. *9660 wins this row decisively.*
>
> Rows 5–6 (the inverse-hyperbolic integrals) are 9660-only at undergraduate-feeder level; 9231 Further Math has them on a separate page; FP3 has them; AP and 9709-Pure don't touch them.

### Special trig integrals (the ones that need a trick)

| $f(x)$ | $\displaystyle \int f(x) \, dx$ | 9709 | IAL | 9660 | AP |
|---|---|:---:|:---:|:---:|:---:|
| $\tan x$ | $-\ln \lvert\cos x\rvert = \ln\lvert\sec x\rvert$ | 📝 (or $f'/f$) | ✅ | ✅ | 📝 |
| $\cot x$ | $\ln \lvert\sin x\rvert$ | 📝 (or $f'/f$) | ✅ | ✅ | 📝 |
| $\sec x$ | $\ln \lvert\sec x + \tan x\rvert$ | ⚪ beyond 9709 | ✅ (two forms) | ✅ (two forms) | 📝 |
| $\csc x$ | $-\ln \lvert\csc x + \cot x\rvert$ | ⚪ beyond 9709 | ✅ (two forms) | ✅ (two forms) | 📝 |

> [!warning] Cambridge specifically forces the Weierstrass-lite derivation
> Note the asymmetry on the $\sec x$ row: IAL and 9660 give it for free (in two equivalent forms — the standard $\ln \lvert \sec x + \tan x \rvert$ and the half-angle $\ln \lvert\tan(\tfrac{x}{2} + \tfrac{\pi}{4})\rvert$). 9709 doesn't, and AP (no sheet) doesn't. So 9709 students must derive $\int \sec x$ via the Weierstrass-lite "multiply by $\frac{\sec x + \tan x}{\sec x + \tan x}$" trick (see *Special Trick — $\int \sec x\,dx$* section below) under exam pressure, while IAL/9660 students just look it up. *This is a real exam-day skill gap between Cambridge and the international competitors.*

### The $f'/f$ master pattern

| $f(x)$ | $\displaystyle \int f(x) \, dx$ | 9709 | IAL | 9660 | AP |
|---|---|:---:|:---:|:---:|:---:|
| $\dfrac{f'(x)}{f(x)}$ | $\ln \lvert f(x) \rvert$ | ✅ | 📝 | 🛠 | 📝 |
| $f'(x)\cdot\bigl[f(x)\bigr]^n,\; n \neq -1$ | $\dfrac{[f(x)]^{n+1}}{n+1}$ | 🛠 | 🛠 | 🛠 | 🛠 |
| $f'(x)\,e^{f(x)}$ | $e^{f(x)}$ | 🛠 | 🛠 | 🛠 | 🛠 |

These are the chain rule read backwards. We'll work each below.

> [!info] Recognition is yours regardless of who gives the formula
> Note that even the 9709 row marked ✅ for $\int \tfrac{f'}{f}$ — where the *formula* sits on MF19 — still requires the *recognition skill* (spotting that a particular numerator is the derivative of the denominator). The booklet hands you the formula; the work of seeing-the-pattern is yours on every board.

> [!tip] Per-board memorisation triage
>
> **9709 P3:** $\int \tan x$, $\int \cot x$ are the only formulas you genuinely need to memorise *as formulas* (recoverable in 10s via $f'/f$ if you blank). Everything else is given or derivable. Plus the chain-rule + Weierstrass-lite skill for $\int \sec x$, $\int \csc x$ when they appear off-syllabus on harder questions.
>
> **Edexcel IAL Pure-only:** Memorise the foundational table ($\sin, \cos, e^x, 1/x, x^n, \sec^2$ — the booklet doesn't list these), the $\arctan$ and $\arcsin$ family (FP3-only on the booklet), and the $f'/f$ pattern. The $\sec x / \csc x$ formulas are free.
>
> **OxAQA 9660:** Memorise the foundational table only. Almost everything else is on the booklet (including $\arctan$, $\arcsin$, hyperbolic, $\sec x$, $\csc x$, $\sec^2 kx$). *The lightest must-memorise list of the four boards.*
>
> **AP Calculus BC:** Memorise everything. No booklet. The full standard-integrals table + linear-inside rule + $f'/f$ pattern + Weierstrass-lite for $\sec x$. Combined with the differentiation table, that's ~70 distinct items at recall speed (see [[AP Calculus Reference]] for the full list).

---

## 中文锚点

**标准积分**：积分版的「微分法则表」。每一行都是 [[Differentiation Rules]] 中某一行倒着读。

**中心策略**：积分不像微分有规则可循；它更像是「认形状」。把这张表背熟（或更准确地说，建立直觉），考试中遇到的大部分被积函数都能被认出来。

**最关键的几条**（9709 P3 §3.5 强调）：

- $\dfrac{1}{x^2 + a^2}$ 积分得 $\dfrac{1}{a}\arctan\dfrac{x}{a}$ —— 注意系数 $\dfrac{1}{a}$，是链式法则的逆向操作。
- $\dfrac{f'(x)}{f(x)}$ 形式的被积函数，积分得 $\ln \lvert f(x) \rvert$。**最常用、最易认。**
- $\dfrac{1}{x}$ 积分是 $\ln \lvert x \rvert$ —— 绝对值！不能写 $\ln x$，因为 $x$ 可能为负。

**口诀**：

- **见 $\dfrac{f'}{f}$，积分是 $\ln\lvert f \rvert$**（最好用的认形状口诀）。
- **绝对值不能省**——整张表的所有 $\ln$ 都带 $\lvert \cdot \rvert$。
- **配方法**——遇到 $\dfrac{1}{x^2 + ax + b}$ 这样的被积函数，先配方再用 $\arctan$ 公式。

---

## Why $\ln \lvert x \rvert$, not $\ln x$

The single most-tested subtlety on this whole card. The differentiation card gives:

$$\dfrac{d}{dx}\ln x = \dfrac{1}{x}.$$

Read right-to-left, this seems to say $\int \tfrac{1}{x}\,dx = \ln x + C$. **But $\ln x$ is only defined for $x > 0$, while $\tfrac{1}{x}$ is defined for all $x \neq 0$.** A correct antiderivative must work wherever the integrand is defined.

Solution: define separately on each branch.

- For $x > 0$: $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$. ✓
- For $x < 0$: $\dfrac{d}{dx}\ln(-x) = \dfrac{1}{-x}\cdot(-1) = \dfrac{1}{x}$. ✓ (chain rule on $-x$)

Both pieces give $1/x$, so a single formula covers both:

$$\boxed{\;\int \dfrac{1}{x}\,dx = \ln \lvert x \rvert + C\;}$$

The absolute value is *load-bearing*. Examiners catch the sloppy "$\ln x + C$" version routinely. Always write $\ln \lvert x \rvert$ unless the problem context guarantees $x > 0$ throughout.

> [!info] Beyond syllabus — there are TWO antiderivative families
> Strictly, the antiderivative of $1/x$ is *piecewise*: any function of the form
> $$F(x) = \begin{cases} \ln x + C_1 & x > 0 \\ \ln(-x) + C_2 & x < 0 \end{cases}$$
> with **independent** constants $C_1$ and $C_2$ on the two branches. The $\ln \lvert x \rvert + C$ formula assumes $C_1 = C_2$ — fine for any single-interval problem, but a real-analysis-style obstacle if a problem spans $x = 0$.
>
> 9709, IB, and AP all assume the single-constant form. University real analysis is where the two-constant version becomes load-bearing.

---

## The $f'/f$ Pattern — the Most-Used Recognition

If you can spot $f'(x)/f(x)$ inside an integrand, the antiderivative is $\ln \lvert f(x) \rvert + C$. This is the **chain rule on $\ln$**, read backwards:

$$\dfrac{d}{dx}\ln \lvert f(x) \rvert = \dfrac{f'(x)}{f(x)} \quad\Longrightarrow\quad \int \dfrac{f'(x)}{f(x)}\,dx = \ln \lvert f(x) \rvert + C.$$

### Three canonical examples

**Example A — $\int \tan x\,dx$.**

Rewrite $\tan x = \dfrac{\sin x}{\cos x}$. Notice $-\sin x = (\cos x)'$, so the integrand is $\dfrac{-(\cos x)'}{\cos x} = -\dfrac{f'}{f}$ with $f = \cos x$.

$$\int \tan x\,dx = -\int \dfrac{(\cos x)'}{\cos x}\,dx = -\ln \lvert \cos x \rvert + C = \ln \lvert \sec x \rvert + C.$$

**Example B — $\int \dfrac{x}{x^2 + 1}\,dx$.**

The numerator $x$ is $\tfrac{1}{2}(x^2 + 1)'$. So the integrand is $\tfrac{1}{2}\cdot\dfrac{(x^2 + 1)'}{x^2 + 1}$.

$$\int \dfrac{x}{x^2 + 1}\,dx = \dfrac{1}{2}\ln \lvert x^2 + 1 \rvert + C = \dfrac{1}{2}\ln(x^2 + 1) + C.$$

(Absolute value optional here because $x^2 + 1 > 0$ always.)

**Example C — $\int \dfrac{6x^2 - 2}{x^3 - x}\,dx$.**

Notice $(x^3 - x)' = 3x^2 - 1$, and $6x^2 - 2 = 2(3x^2 - 1)$. So the integrand is $\dfrac{2 f'(x)}{f(x)}$.

$$\int \dfrac{6x^2 - 2}{x^3 - x}\,dx = 2\ln \lvert x^3 - x \rvert + C.$$

> [!tip] How to spot the pattern
> Look at the numerator and the denominator's derivative. If they're proportional (constant multiple), the integrand is $k\cdot f'/f$. The integral is $k\ln \lvert f \rvert + C$. **This is the highest-leverage recognition pattern in elementary integration** — it shortcuts huge classes of textbook integrals that would otherwise need full $u$-substitution.

---

## The Inverse-Trig Family

### $\int \dfrac{1}{x^2 + a^2}\,dx = \dfrac{1}{a}\arctan\!\left(\dfrac{x}{a}\right) + C$ — derivation

From [[Differentiation Rules]]: $\dfrac{d}{dx}\arctan x = \dfrac{1}{1 + x^2}$. Generalise via the substitution $u = x/a$:

$$\dfrac{d}{dx}\arctan\!\left(\dfrac{x}{a}\right) = \dfrac{1}{1 + (x/a)^2}\cdot\dfrac{1}{a} = \dfrac{1}{a^2 + x^2}\cdot\dfrac{a^2}{a^2}\cdot\dfrac{1}{a} = \dfrac{a}{a^2 + x^2}\cdot\dfrac{1}{a} = \dfrac{1}{a(1 + (x/a)^2)}.$$

A cleaner re-derivation: let $u = x/a$ so $du = dx/a$, and $x^2 + a^2 = a^2(1 + u^2)$:

$$\int \dfrac{1}{x^2 + a^2}\,dx = \int \dfrac{1}{a^2(1 + u^2)}\cdot a\,du = \dfrac{1}{a}\int \dfrac{1}{1 + u^2}\,du = \dfrac{1}{a}\arctan u + C = \dfrac{1}{a}\arctan\!\dfrac{x}{a} + C.\qquad\blacksquare$$

The factor $\tfrac{1}{a}$ is the chain-rule-reversal correction. **Don't forget it.** A common error is writing $\arctan(x/a) + C$ without the $\tfrac{1}{a}$ — wrong by a factor of $a$.

### $\int \dfrac{1}{\sqrt{a^2 - x^2}}\,dx = \arcsin\!\left(\dfrac{x}{a}\right) + C$ — derivation

Same substitution $u = x/a$:

$$\sqrt{a^2 - x^2} = a\sqrt{1 - u^2} \quad (\text{for } a > 0)$$

$$\int \dfrac{1}{\sqrt{a^2 - x^2}}\,dx = \int \dfrac{1}{a\sqrt{1 - u^2}}\cdot a\,du = \int \dfrac{1}{\sqrt{1 - u^2}}\,du = \arcsin u + C = \arcsin\!\dfrac{x}{a} + C.\qquad\blacksquare$$

Notice **no $\tfrac{1}{a}$ factor here** — the $a$'s cancelled. That asymmetry between the $\arctan$ and $\arcsin$ forms is one of the most-tripped traps; learn the formulas exactly, don't try to predict the coefficient.

### Completing the square — for shifted denominators

When the denominator isn't a clean $x^2 + a^2$ — for instance $x^2 + 4x + 13$ — **complete the square first**:

$$x^2 + 4x + 13 = (x + 2)^2 + 9.$$

Now the substitution $u = x + 2$ (with $du = dx$) reduces the integral to the standard form:

$$\int \dfrac{1}{x^2 + 4x + 13}\,dx = \int \dfrac{1}{(x+2)^2 + 9}\,dx = \dfrac{1}{3}\arctan\!\dfrac{x + 2}{3} + C.$$

This pattern — **complete the square, $u$-substitute, apply the arctan formula** — handles every quadratic denominator that doesn't factor over the reals. (Quadratics that *do* factor go through [[Partial Fractions]] instead.) The 9709 P3 §3.5 syllabus explicitly cites $\int \tfrac{1}{2 + 3x^2}\,dx$ — same pattern, factor out the constant first.

---

## Special Trick — $\int \sec x\,dx$ via Weierstrass-Lite

This integral has no obvious recognition pattern, and the standard trick — multiply by $\dfrac{\sec x + \tan x}{\sec x + \tan x}$ — looks like magic until you see what it does.

$$\int \sec x\,dx = \int \sec x \cdot \dfrac{\sec x + \tan x}{\sec x + \tan x}\,dx = \int \dfrac{\sec^2 x + \sec x \tan x}{\sec x + \tan x}\,dx.$$

Now the numerator $\sec^2 x + \sec x \tan x$ is exactly $(\sec x + \tan x)'$ — by direct differentiation. So the integrand is $f'/f$ with $f = \sec x + \tan x$:

$$\int \sec x\,dx = \ln \lvert \sec x + \tan x \rvert + C.\qquad\blacksquare$$

The trick is "Weierstrass-lite" because the full **Weierstrass substitution** $t = \tan(x/2)$ (the universal trig substitution that converts any rational function of $\sin, \cos$ into a rational function of $t$) handles this and a much wider family — but this $\sec x$ case is so ubiquitous that the pre-multiplication trick became its own technique, decades before Weierstrass formalised the general substitution.

> [!info] Beyond syllabus — the universal substitution
> The Weierstrass substitution $t = \tan(x/2)$ converts the trio of trig functions:
> $$\sin x = \dfrac{2t}{1 + t^2}, \quad \cos x = \dfrac{1 - t^2}{1 + t^2}, \quad dx = \dfrac{2\,dt}{1 + t^2}.$$
> Any rational function of $\sin x, \cos x$ becomes a rational function of $t$, integrable via [[Partial Fractions]]. Beyond 9709 P3 — university level — but the trick is one of the gems of elementary integration. (See also [[Stories/The Bernoulli Family]] for Karl Weierstrass's role in 19th-century rigorisation, even though the substitution predates him by a century.)

The $\int \csc x\,dx$ companion uses the same pattern with $\csc x \cdot \dfrac{\csc x + \cot x}{\csc x + \cot x}$. Sign comes out flipped: $-\ln \lvert \csc x + \cot x\rvert + C$.

---

## Worked Examples

### Example 1 — $\int \dfrac{1}{2 + 3x^2}\,dx$

Factor the constant from the denominator to get the standard form:

$$2 + 3x^2 = 2\left(1 + \tfrac{3}{2}x^2\right) = 2\left(1 + \left(\sqrt{3/2}\,x\right)^2\right).$$

Hmm — easier to write $2 + 3x^2 = 3(x^2 + 2/3) = 3(x^2 + (\sqrt{2/3})^2)$, then:

$$\int \dfrac{1}{2 + 3x^2}\,dx = \dfrac{1}{3}\int \dfrac{1}{x^2 + (\sqrt{2/3})^2}\,dx = \dfrac{1}{3}\cdot\dfrac{1}{\sqrt{2/3}}\arctan\!\dfrac{x}{\sqrt{2/3}} + C.$$

Simplify $\dfrac{1}{3\sqrt{2/3}} = \dfrac{1}{3}\cdot\sqrt{3/2} = \dfrac{1}{\sqrt{6}}$:

$$\int \dfrac{1}{2 + 3x^2}\,dx = \dfrac{1}{\sqrt{6}}\arctan\!\left(x\sqrt{3/2}\right) + C.$$

Same answer, less elegant route. **Cleaner approach:** substitute $u = x\sqrt{3/2}$ from the start, transforming the integral to $\int \dfrac{du/\sqrt{3/2}}{2(1 + u^2)} = \dfrac{1}{\sqrt{6}}\arctan u$. Either route yields. The 9709 syllabus's example is exactly this shape.

### Example 2 — $\int \dfrac{x + 2}{x^2 + 4x + 13}\,dx$

The denominator is a quadratic; the numerator looks like *almost* its derivative. Check: $(x^2 + 4x + 13)' = 2x + 4 = 2(x + 2)$. So $x + 2 = \tfrac{1}{2}(x^2 + 4x + 13)'$, and the integrand is $\tfrac{1}{2}\cdot\dfrac{f'(x)}{f(x)}$:

$$\int \dfrac{x + 2}{x^2 + 4x + 13}\,dx = \dfrac{1}{2}\ln \lvert x^2 + 4x + 13 \rvert + C = \dfrac{1}{2}\ln(x^2 + 4x + 13) + C.$$

(Absolute value drops because $x^2 + 4x + 13 = (x+2)^2 + 9 > 0$ always.) **Pure $f'/f$**, no completing the square needed because the numerator was already proportional to the derivative.

### Example 3 — $\int \dfrac{1}{x^2 + 4x + 13}\,dx$ (the no-numerator-help version)

Same denominator, but no $f'$ in the numerator. Complete the square:

$$\int \dfrac{1}{x^2 + 4x + 13}\,dx = \int \dfrac{1}{(x + 2)^2 + 9}\,dx = \dfrac{1}{3}\arctan\!\dfrac{x + 2}{3} + C.$$

**Comparing Examples 2 and 3:** same denominator, different numerator, completely different antiderivative shape. The pattern *the integrand picks the technique* runs through all of integration. Recognising which pattern applies is most of the work.

### Example 4 — $\int \tan(2x)\,dx$

Two ways. **Linear-inside:** $\int \tan u\,du = -\ln \lvert \cos u\rvert$, so by the linear-inside rule $\int \tan(2x)\,dx = -\dfrac{1}{2}\ln \lvert \cos(2x)\rvert + C$.

**Direct $f'/f$:** rewrite as $\int \dfrac{\sin(2x)}{\cos(2x)}\,dx$. The numerator $\sin(2x) = -\dfrac{1}{2}(\cos(2x))'$, so the integrand is $-\dfrac{1}{2}\cdot\dfrac{f'}{f}$ with $f = \cos(2x)$:

$$\int \tan(2x)\,dx = -\dfrac{1}{2}\ln \lvert \cos(2x)\rvert + C.$$

Same answer, both routes legitimate.

### Example 5 — $\int \dfrac{1}{x \ln x}\,dx$ (the $f'/f$ delight)

What's $f$? The denominator is $x\ln x$ which doesn't suggest itself. But $(\ln x)' = 1/x$, so $\dfrac{1}{x \ln x} = \dfrac{(\ln x)'}{\ln x}$ — pure $f'/f$ with $f = \ln x$.

$$\int \dfrac{1}{x \ln x}\,dx = \ln \lvert \ln x \rvert + C.$$

A satisfying *iterated-log* result. The double absolute value isn't a typo — it accommodates $\ln x$ being negative for $0 < x < 1$.

---

## Common Pitfalls

### 1. Forgetting the $\dfrac{1}{a}$ in $\arctan$

$$\int \dfrac{1}{x^2 + 4}\,dx = \dfrac{1}{2}\arctan\!\dfrac{x}{2} + C, \quad \text{not} \quad \arctan\!\dfrac{x}{2} + C.$$

The $\tfrac{1}{a}$ comes from the chain-rule reversal when you let $u = x/a$. Forget it and your answer is off by a factor of $a$. *Always written as $\dfrac{1}{a}$ explicitly even when $a = 1$ — that disciplines the habit.*

### 2. Forgetting the $\lvert \cdot \rvert$ in $\ln$

Every $\ln$ that comes from integration has absolute-value bars unless the argument is provably positive in the problem's domain. If a marker sees "$\ln(x - 1)$" without bars and the problem allows $x < 1$, that's a method-mark loss.

### 3. Confusing $\arctan$ vs $\arcsin$ formulas

$\dfrac{1}{x^2 + a^2}$ → arctan, with $\dfrac{1}{a}$ factor.
$\dfrac{1}{\sqrt{a^2 - x^2}}$ → arcsin, **no** factor.

The denominator structure is the giveaway: **squared-sum → arctan, square-root-of-difference → arcsin.** If your integrand has a square-root, look for arcsin; if not, look for arctan.

### 4. Trying to use $f'/f$ when the numerator isn't proportional to $f'$

Recognition demands *exact* proportionality (up to a constant). $\int \dfrac{x + 1}{x^2 + 4x + 13}\,dx$ is **not** $f'/f$ because $(x^2 + 4x + 13)' = 2x + 4 = 2(x + 2)$, not $2(x+1)$. You'd split the numerator: $x + 1 = (x + 2) - 1$, then handle the $(x+2)/(x^2+4x+13)$ piece via $f'/f$ and the $-1/(x^2+4x+13)$ piece via complete-the-square + arctan. **Splitting the numerator** is the standard recovery move.

### 5. Sign error on $\int \sin x$ vs $\int \cos x$

$\int \sin x\,dx = -\cos x + C$ (the minus is because $\cos$ differentiates *to* $-\sin$, so integrating $\sin$ undoes that).
$\int \cos x\,dx = \sin x + C$ (no sign).

A recurring exam-day error under pressure. Mnemonic: *sine → minus cosine, cosine → plus sine.*

---

## Beyond Syllabus

### Hyperbolic integrals

Most of the inverse-trig family has hyperbolic siblings:

| $\dfrac{1}{x^2 - a^2}$ | $\dfrac{1}{2a}\ln\!\left\lvert\dfrac{x - a}{x + a}\right\rvert$ | Partial-fractions classic; appears in capacitor discharge, population dynamics |
| $\dfrac{1}{\sqrt{x^2 + a^2}}$ | $\sinh^{-1}(x/a)$ | Hyperbolic version of arcsin |
| $\dfrac{1}{\sqrt{x^2 - a^2}}$ | $\cosh^{-1}(x/a)$ | Same family |

University analysis covers these systematically. The connection: $\sinh, \cosh, \tanh$ relate to $\sin, \cos, \tan$ via the imaginary-unit substitution $x \to ix$, and the inverse-hyperbolic integrals fall out of inverse-trig integrals by the same substitution.

### The integral of $e^{-x^2}$ — and why it's missing

A glaring gap in the table: **$\int e^{-x^2}\,dx$ has no elementary antiderivative**. This is *the* canonical example of an integrable function with no closed-form antiderivative — proven by Liouville's theorem (1835). The function $\operatorname{erf}(x) = \tfrac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$ is *defined* by this integral; it cannot be reduced to elementary functions.

This is why the [[Normal Distribution]] uses tables: there's no formula for the cumulative distribution function. *The table-vs-formula distinction in statistics is downstream of Liouville's theorem.*

### Risch algorithm

For modern computer algebra: Robert Risch (1968) proved a complete decision procedure for "is this elementary integral expressible in closed form?" — and a constructive algorithm to find the closed form when it exists. Mathematica and Maple implement variants. The Risch algorithm is the closest mathematics has come to an "integration recipe" — but it requires several pages of casework even for moderate inputs, and the elementary-vs-non-elementary boundary is genuinely subtle. Liouville opened the question in 1835; Risch closed it in 1968.

---

## Exam Notes

### Cambridge 9709 (A-Level Mathematics)

**Paper 3 §3.5** — examined directly. The syllabus explicitly lists:
- $\int \dfrac{1}{x^2 + a^2}\,dx \to \arctan$ (with the $\frac{1}{a}$ factor)
- $f'/f$ pattern, $\tan x$ as worked example
- Trig identities for $\sin^2 x$ etc. (double-angle formulas)
- Partial-fractions integration (restricted forms, see [[Partial Fractions]])
- Linear-inside extension on every elementary form

**NOT on 9709:** $\int \dfrac{1}{\sqrt{a^2 - x^2}}\,dx \to \arcsin$. The syllabus says *"Derivatives of $\sin^{-1}x$ and $\cos^{-1}x$ are not required"* (P3 §3.4), and the $\arcsin$ integral is correspondingly out of scope. Knowing it anyway is enrichment for IB/AP students.

**NOT on 9709:** the $\int \sec x\,dx$ Weierstrass-lite trick. Beyond syllabus but pedagogically essential — it's one of the cleanest demonstrations of the "multiply by a clever 1" technique that recurs throughout integration theory.

### Cambridge 9231 Further Mathematics — **Further Pure 2, Paper 2**

The card carries a `syllabus/9231-2-4` tag and the tables mark rows "9231 only", but the section itself was missing until 2026-08-12. **§2.4 Integration** asks for:

- the three integrals $\displaystyle\int\frac{dx}{\sqrt{a^2-x^2}}$, $\displaystyle\int\frac{dx}{\sqrt{x^2+a^2}}$, $\displaystyle\int\frac{dx}{\sqrt{x^2-a^2}}$ **by trigonometric or hyperbolic substitution** — the substitutions themselves ($x = a\sin\theta$, $x = a\sinh u$, $x = a\cosh u$) come from [[Hyperbolic Functions]], and all three results are **printed on MF19**, so marks ride on the working and the limits rather than the answer;
- **reduction formulae** — derive $I_n$ in terms of $I_{n-1}$ (usually by parts) and run the recursion down to a base case;
- **rectangle bounds for sums** — sandwiching $\sum f(r)$ between integrals;
- **arc length and surface of revolution**, in Cartesian, parametric *and* polar form.

Only the first bullet lives on this page; the rest belong to [[Integration by Parts]], [[Areas and Volumes by Integration]] and their neighbours. A 9231 candidate reading this card for §2.4 should treat it as one quarter of the row.

### IB AA HL

**Topic 5** — both $\arctan$ and $\arcsin$ integrals on syllabus. $\sec x$ via the trick is covered in many textbooks even when not formally required.

### IB AA SL

Limited coverage — basic $\dfrac{1}{x}$ and elementary trig integrals only. The inverse-trig family is HL-only.

### AP Calculus AB / BC

**AB** — $\dfrac{1}{x}$, basic trig, $e^x$. No inverse-trig integrals.
**BC** — full inverse-trig family ($\arctan$, $\arcsin$, $\arctan$ via partial fractions), $\sec x$ trick is fair game.

### Beyond high school — University

Liouville's theorem, the Risch algorithm, hyperbolic integrals, the gamma function $\int_0^\infty x^{s-1}e^{-x}\,dx$ extending factorial to non-integers, contour integration in complex analysis. The standard integrals table extends massively at university; the pattern *"recognise then transform"* stays the same.

---

## Connections

- **Direct prerequisite:** [[Differentiation Rules]] — every entry in this table is a row of that one read backwards. Pair the two cards.
- **Direct prerequisite:** [[Integration]] — basic antidifferentiation, the constant of integration, the linear-inside rule.
- **Sibling techniques:** [[Integration by Substitution]] (chain rule reversed for non-linear inside), [[Integration by Parts]] (product rule reversed), [[Partial Fractions]] (rational-function decomposition before integration).
- **Direct application:** [[Differential Equations]] — most ODE solutions reduce to evaluating standard integrals. The $\int \dfrac{1}{x}\,dx = \ln \lvert x \rvert$ result is the heart of every separable-ODE solution.
- **Cross-domain — physics:** SUVAT (uniform acceleration) → $v = \int a\,dt$, $s = \int v\,dt$; both are linear-inside polynomial integrals. Logistic population growth, capacitor discharge, radioactive decay → $\int \dfrac{1}{x}\,dx$ and friends.
- **Cross-domain — statistics:** [[Normal Distribution]] cumulative function uses $\int e^{-x^2}\,dx$ which has no elementary antiderivative (see Beyond Syllabus on Liouville). The table-vs-formula approach in statistics is downstream of this card's silent gap.
- **For 9709 students:** [[MF19 Reference (9709)]] — the integration table on MF19 is generous. Given on the sheet: all foundational integrals; $1/(x^2+a^2)$, $1/(x^2-a^2)$, $1/(a^2-x^2)$ inverse-trig/log family; integration by parts; **and the $f'/f \to \ln \lvert f \rvert$ formula itself**. *Not* on MF19 (must memorise or derive): the linear-inside extensions ($\int e^{ax+b}$ etc — derive via the $1/a$ chain-rule rule); $\int \tan x$ and $\int \cot x$ (formulas to memorise, but recoverable from $f'/f$); $\int \sec x$ via Weierstrass-lite (beyond 9709). The asymmetry in the inverse-trig coefficient ($\arctan$ has $1/a$, $\arcsin$ doesn't) is exam-day memorisable; both are on the formula table when relevant.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\int \dfrac{1}{x}\,dx = \ln \lvert x \rvert + C$ | `\int \dfrac{1}{x}\,dx = \ln \lvert x \rvert + C` | The absolute-value subtlety. |
| $\int \dfrac{f'(x)}{f(x)}\,dx = \ln \lvert f(x) \rvert + C$ | `\int \dfrac{f'(x)}{f(x)}\,dx = \ln \lvert f(x) \rvert + C` | The master $f'/f$ pattern. |
| $\int \dfrac{1}{x^2 + a^2}\,dx = \dfrac{1}{a}\arctan\!\dfrac{x}{a} + C$ | `\int \dfrac{1}{x^2 + a^2}\,dx = \dfrac{1}{a}\arctan\!\dfrac{x}{a} + C` | Arctan integral. **Don't forget the $1/a$.** |
| $\int \dfrac{1}{\sqrt{a^2 - x^2}}\,dx = \arcsin\!\dfrac{x}{a} + C$ | `\int \dfrac{1}{\sqrt{a^2 - x^2}}\,dx = \arcsin\!\dfrac{x}{a} + C` | Arcsin integral (NOT on 9709). No $1/a$ factor. |
| $\int \sec x\,dx = \ln \lvert \sec x + \tan x \rvert + C$ | `\int \sec x\,dx = \ln \lvert \sec x + \tan x \rvert + C` | Weierstrass-lite trick. |
| $\int \tan x\,dx = -\ln \lvert \cos x \rvert + C = \ln \lvert \sec x \rvert + C$ | `\int \tan x\,dx = -\ln \lvert \cos x \rvert + C` | $f'/f$ with $f = \cos x$. |

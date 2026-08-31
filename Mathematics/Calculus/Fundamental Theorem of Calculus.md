---
chinese: 微积分基本定理 (wēijīfēn jīběn dìnglǐ) / 牛顿-莱布尼茨公式 (Niúdùn–Láibùnící gōngshì)
prerequisites:
  - "[[Differentiation]]"
  - "[[Integration]]"
  - "[[Limit]]"
  - "[[Differentiation Rules]]"
  - "[[Area Under a Graph (Vocab)]]"
  - "[[Mean Value Theorem]]"
  - "[[Properties of Definite Integrals]]"
leads_to:
  - "[[Integration by Substitution]]"
  - "[[Integration by Parts]]"
  - "[[The Calculus Priority Dispute]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - type/deep
  - type/theorem
  - type/proof
  - type/historical
  - notation/definite-integral
  - misconception/which-FTC
  - misconception/FTC-as-definition
---

# Fundamental Theorem of Calculus 微积分基本定理

## Definition

The **Fundamental Theorem of Calculus** (FTC), also called the **Newton–Leibniz formula** (牛顿–莱布尼茨公式) after its two independent discoverers, is the theorem that ties **differentiation and integration together as inverse operations**. It is the result that justifies *every* "evaluate the antiderivative at the limits" step you have ever written.

There are **two statements**, often called FTC1 and FTC2. Both are true; both are the FTC; they say different things. The first is the surprising one — it claims that *every continuous function has an antiderivative*, given as an explicit area formula. The second is the practical one — it tells you how to *compute* a definite integral once you have any antiderivative.

> **FTC1** (existence). If $f$ is continuous on $[a, b]$, then the function
> $$F(x) = \int_a^x f(t)\, dt$$
> is differentiable on $(a, b)$, and $F'(x) = f(x)$.
>
> **FTC2** (computation — the Newton–Leibniz formula). If $f$ is continuous on $[a, b]$ and $F$ is *any* antiderivative of $f$, then
> $$\int_a^b f(x)\, dx = F(b) - F(a).$$

This card states both, proves them, walks through the famous Newton–Leibniz priority dispute, and locates FTC inside the broader pattern of "fundamental theorems" in mathematics.

### 中文锚点

微积分基本定理 = 微分和积分互为逆运算的定理。它有**两个版本**：
- **FTC1**：连续函数 $f$ 的"积累函数" $F(x) = \int_a^x f(t)\,dt$ 是 $f$ 的一个原函数（即 $F'(x) = f(x)$）。
- **FTC2**（牛顿-莱布尼茨公式）：定积分 $\int_a^b f(x)\,dx = F(b) - F(a)$，其中 $F$ 是 $f$ 的任意一个原函数。

FTC1 是"惊奇"的版本——它告诉你 *任何连续函数都有原函数*，并直接给出了一个原函数的具体形式（积累函数）。FTC2 是"实用"的版本——它告诉你怎么用任意一个原函数算出定积分的值。两个版本一起构成微积分的核心。

---

## Why FTC1 Is the Surprising Half

If you've been computing integrals by saying *"$\int 2x\, dx = x^2 + C$, so $\int_1^3 2x\, dx = [x^2]_1^3 = 9 - 1 = 8$,"* you have been using FTC2. You probably never paused to ask whether $2x$ *has* an antiderivative — it obviously does, because the power rule hands you one.

But what about $f(x) = e^{-x^2}$? Or $f(x) = (\sin x)/x$? These functions have no closed-form antiderivative — no combination of polynomials, exponentials, logs, and trig functions gives a function that differentiates to them. Does that mean they have no antiderivative *at all*?

**FTC1 says: no — every continuous function has an antiderivative.** Specifically, the area-so-far function $F(x) = \int_a^x f(t)\, dt$ *is* an antiderivative, even when no closed-form expression exists. The function $F$ might not have a name in elementary calculus — but it exists as a perfectly good function, computable to any precision by numerical integration, and it differentiates back to $f$.

This is the deep claim. Antiderivatives *always* exist (for continuous integrands). The fact that we sometimes *cannot write them down* in elementary form is a limitation of our notation, not of the underlying mathematics. The function $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\, dt$ has its own name (the *error function*) precisely because it's an antiderivative of $e^{-x^2}$ that doesn't reduce to elementary functions — but it exists and is just as concrete as $\sin x$ once you accept it.

---

## Proof of FTC1 — via the Mean Value Theorem for Integrals

Let $f$ be continuous on $[a, b]$ and define $F(x) = \int_a^x f(t)\, dt$. We want to show $F'(x) = f(x)$.

By the definition of the derivative:

$$
F'(x) = \lim_{h \to 0}\frac{F(x + h) - F(x)}{h} = \lim_{h \to 0}\frac{1}{h}\!\left[\int_a^{x+h} f(t)\, dt - \int_a^{x} f(t)\, dt\right] = \lim_{h \to 0}\frac{1}{h}\int_x^{x+h} f(t)\, dt.
$$

(The last step uses the **additivity of the integral**, $\int_a^{x+h} = \int_a^{x} + \int_x^{x+h}$ — see [[Properties of Definite Integrals]] §2 for the Riemann-sum proof.)

Now invoke the **Mean Value Theorem for Integrals** (see [[Mean Value Theorem]]): since $f$ is continuous on $[x, x+h]$, there exists $c \in [x, x+h]$ such that

$$
\int_x^{x+h} f(t)\, dt = f(c) \cdot h.
$$

Geometrically: the area under $f$ from $x$ to $x+h$ equals the area of a rectangle of width $h$ whose height is $f$ evaluated at *some* point $c$ in the interval. (When $h$ is tiny, $c$ is squeezed near $x$.)

Substituting:

$$
F'(x) = \lim_{h \to 0}\frac{f(c) \cdot h}{h} = \lim_{h \to 0} f(c).
$$

As $h \to 0$, the interval $[x, x+h]$ shrinks to the point $x$, so $c \to x$. By the **continuity** of $f$, $f(c) \to f(x)$. Therefore

$$
F'(x) = f(x). \qquad\boxed{}
$$

Continuity is the crucial hypothesis: it is exactly what makes "$f(c) \to f(x)$ as $c \to x$" valid. Drop continuity and FTC1 can fail (jump discontinuities give the area function a "kink" where it isn't differentiable).

---

## Proof of FTC2 from FTC1

Let $G(x) = \int_a^x f(t)\, dt$. By FTC1, $G$ is an antiderivative of $f$ on $[a, b]$.

Let $F$ be *any* other antiderivative of $f$. Then $G$ and $F$ have the same derivative on $(a, b)$, so they differ by a constant: $G(x) = F(x) + C$ for all $x \in [a, b]$.

Plug in $x = a$:

$$
G(a) = \int_a^a f(t)\, dt = 0 \;\;\Longrightarrow\;\; F(a) + C = 0 \;\;\Longrightarrow\;\; C = -F(a).
$$

Plug in $x = b$:

$$
G(b) = \int_a^b f(t)\, dt = F(b) + C = F(b) - F(a). \qquad\boxed{}
$$

So FTC2 follows from FTC1 in three lines. The deep work is in FTC1; FTC2 is its corollary.

> [!tip] Two facts that quietly do the work
> The proof above leans on two earlier results that students often skip past: (1) two functions with the same derivative differ by a constant — proved via the **Mean Value Theorem for derivatives** (if $H' \equiv 0$ then $H$ is constant); (2) integration over a zero-length interval gives zero, $\int_a^a f = 0$. Both are simple, and both are essential.

---

## The Newton–Leibniz Priority Dispute

The FTC was discovered, *independently*, by **Isaac Newton** in England (1665–66, unpublished for decades) and **Gottfried Wilhelm Leibniz** in Germany (1675–76, published 1684 with the notation $dy$, $dx$, $\int$ that we still use today). The dispute over who should get credit became one of the ugliest priority fights in the history of mathematics — Royal Society rigging, anonymous self-reviews, Leibniz dying in poverty in 1716 while Newton was buried with state honours in Westminster Abbey in 1727. Britain then spent the next century behind continental Europe because it stuck patriotically with Newton's inferior dot notation, until three Cambridge undergraduates fixed it in 1812.

The full drama lives in **[[Stories/The Calculus Priority Dispute]]**. The headline for present purposes: both invented calculus independently; both are credited as co-discoverers in modern textbooks; Leibniz's notation won universally and is the one used in this card.

> [!info] Beyond syllabus — why Leibniz's notation won
> $\dfrac{dy}{dx}$ for the derivative makes the chain rule look like "cancelling differentials": $\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$. Newton's notation $\dot y$ does not. $\int f(x)\, dx$ visually pairs the "summa" symbol $\int$ with the "infinitesimal width" $dx$, so the substitution rule "let $u = g(x)$, then $du = g'(x)\, dx$" feels almost algebraic. **Leibniz's notation is *suggestive*** — it makes correct manipulations look natural and incorrect ones look strange. That suggestiveness is how it won the war.

---

## Why "Fundamental"?

Calling something a "fundamental theorem" is a strong claim. The phrase shows up in a small number of places in mathematics, and each time it tags the result that ties together the **two main operations** of the field. The pattern:

| Field | Two operations | The "fundamental theorem" claims |
|---|---|---|
| Calculus | differentiation and integration | the operations are inverses (FTC) |
| Algebra | polynomials and roots | every nonconstant complex polynomial has a root (FTAlg) |
| Arithmetic | multiplication and primes | every integer has a unique prime factorisation (FTArith) |
| Linear Algebra | row space, null space | rank–nullity + orthogonal complements (FTLA) |

In each case, "fundamental" means: *without this theorem, the two operations look unrelated; with it, they're inseparable.* For calculus, derivatives and integrals look like utterly different things — one is a limit of ratios, the other is a limit of sums — and the FTC reveals they are two faces of the same operation.

> [!info] Beyond syllabus — the generalised Stokes theorem
> The FTC is the **1-dimensional case** of a much larger theorem. In higher dimensions, integrals over regions are related to integrals over their boundaries:
> - **Green's theorem** (2D): line integral around a closed curve = double integral of the curl over the enclosed region
> - **Stokes' theorem** (surfaces in 3D): surface integral of the curl = line integral around the boundary
> - **Divergence theorem** / Gauss's theorem (volumes in 3D): volume integral of the divergence = flux through the boundary surface
> - **Generalised Stokes theorem** (any dimension, on manifolds): $\int_M d\omega = \int_{\partial M} \omega$
>
> They all say the same thing: *integrating a derivative over a region equals integrating the original function over the boundary.* The FTC is this with a 1-dimensional region $[a, b]$ whose "boundary" is the two endpoints $\{a, b\}$, where the "boundary integral" is just $F(b) - F(a)$. One theorem, infinitely many shapes.

---

## Common Mistakes

1. **Confusing FTC1 with FTC2.** They're different statements. FTC1 is "$F(x) = \int_a^x f(t)\, dt \Rightarrow F'(x) = f(x)$" — about the differentiability of an integral. FTC2 is "$\int_a^b f = F(b) - F(a)$" — about evaluating an integral via an antiderivative. Cambridge / IB / AP exam questions occasionally test FTC1 directly: "find $\frac{d}{dx}\int_2^x \sqrt{1 + t^4}\, dt$" — the answer is $\sqrt{1 + x^4}$, *not* an attempt to compute the integral.
2. **Forgetting continuity.** Both forms assume $f$ is continuous on $[a, b]$. If $f$ has a jump discontinuity, FTC1's conclusion can fail at the jump point. Most exam-level $f$'s are continuous, so this rarely bites — but in the abstract version it matters.
3. **"FTC says integration is the reverse of differentiation, *by definition*."** No — that's a *theorem*, not a definition. Integration is defined as a *limit of sums* (the Riemann integral). Differentiation is defined as a *limit of difference quotients*. The FTC is the surprising claim that these two completely different limits are inverse to one another. Calling it a definition robs the result of its content.
4. **Treating "antiderivative" as singular.** Every continuous function has *infinitely many* antiderivatives, differing by a constant. FTC2's $F$ is "any" antiderivative — pick the one with $C = 0$ for convenience, but the formula gives the same answer regardless.
5. **Chain rule on FTC1.** If $F(x) = \int_a^{g(x)} f(t)\, dt$ (variable upper limit is a *function* of $x$, not just $x$), the derivative is $F'(x) = f(g(x)) \cdot g'(x)$ by chain rule. The bare FTC1 is the special case $g(x) = x$.

---

## Exam Notes

### Cambridge 0606

The FTC is **assumed but rarely named explicitly** at 0606 level. Every "evaluate $\int_a^b \ldots\, dx$" question silently uses FTC2. You won't be asked to prove either form, and FTC1 with a variable limit doesn't appear. The vault recommends knowing the *statement* of FTC2 by heart and treating "Newton–Leibniz formula" as a synonym.

### Cambridge 0580

**Not examined.** Extended's calculus (E2.12) is differentiation only — there is no integration at 0580, so neither form of the theorem can arise.

### Cambridge 9709 / 9231 · Edexcel IAL · OxAQA 9660

On all the Cambridge-style A-Level boards the theorem is **invisible by definition**: the syllabus *defines* integration as the reverse of differentiation, so FTC2 is built into the notation before any question is asked, and the theorem's real content — that the *area under the curve* is computed by that antiderivative — arrives as an unproved bridge in the area topic. What analysis calls a theorem, these boards call a definition; no paper names "Fundamental Theorem", asks for a statement, or sets variable-upper-limit differentiation. (The claim is checked against the topic maps: no board row exists for the FTC on 9709, 9231, IAL or 9660 — every "evaluate $\int_a^b$" question simply *uses* FTC2 silently, exactly as at 0606.) At 9231 the theorem's spirit does surface once, in disguise: the **method of differences** is the FTC's discrete twin — summing consecutive differences telescopes to endpoint values, exactly as integrating a derivative does — and [[Summation of Series]] runs that engine.

### IB AA

**SL**: statement and use of FTC2; FTC1 with a variable upper limit appears in some textbooks but is not a heavily-tested item. **HL**: both forms, with at least an informal argument for FTC1, and variable-upper-limit problems ("find $\frac{d}{dx}\int_1^x e^{t^2}\, dt$") as standard fare.

### AP Calculus AB / BC

The one school system that examines the theorem *as a theorem*, by name. Topics **6.4** (accumulation functions), **6.7** (the FTC itself) and **8.3** (using accumulation functions in context) are map-confirmed rows; the accumulation function $F(x) = \int_a^x f(t)\,dt$ — read its derivative, its increasing/decreasing intervals, its concavity straight off the graph of $f$ — is AP's signature FRQ shape, and the chain-rule extension $F(x) = \int_{u(x)}^{v(x)} f(t)\, dt \Rightarrow F'(x) = f(v)v' - f(u)u'$ is fair game on both routes.

---

## Connections

- **Prerequisite:** [[Differentiation]] — the derivative limit defining $F'$
- **Prerequisite:** [[Integration]] — the area limit defining $\int_a^b f$
- **Prerequisite:** [[Limit]] — squeezed-limit argument in the FTC1 proof (continuity → $f(c) \to f(x)$)
- **Prerequisite:** [[Differentiation Rules]] — the elementary-function derivatives that supply antiderivatives in practice
- **Used by:** [[Integration by Substitution]] — the substitution rule is FTC2 + chain rule, run backwards
- **Used by:** [[Integration by Parts]] — IBP is FTC2 + product rule, run backwards
- **Lemma:** [[Mean Value Theorem]] — the MVT for integrals supplies the $f(c)$ in the FTC1 proof; the "same-derivative-implies-constant" lemma in the FTC2 proof is also MVT-based
- **Lemma:** [[Properties of Definite Integrals]] — additivity of the integral ($\int_a^{x+h} = \int_a^x + \int_x^{x+h}$) is the splitting step in the FTC1 derivation
- **Generalisation:** *Stokes' theorem* (multivariable calculus) — same statement on higher-dimensional manifolds: $\int_M d\omega = \int_{\partial M} \omega$
- **Family:** Fundamental Theorem of Algebra, Fundamental Theorem of Arithmetic — the "fundamental theorem" naming convention identifies the inverse-relationship results in each field
- **History:** the Newton–Leibniz priority dispute — one of the great mathematical feuds; cost British mathematics ~50 years of progress
- **Application:** *every definite integral computation in physics* — work, kinetic energy, charge, flux, expected value of a continuous random variable, all FTC2
- **Bridge to physics:** the work-energy theorem $W = \int_a^b F\, dx = \Delta KE$ is FTC2 with $F = ma = m\,dv/dt$ producing the antiderivative $\tfrac{1}{2}mv^2$

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\int_a^b f(x)\, dx$ | `\int_a^b f(x)\, dx` | definite integral with limits |
| $\bigl[F(x)\bigr]_a^b$ | `\bigl[F(x)\bigr]_a^b` | evaluation notation $F(b) - F(a)$ |
| $\dfrac{d}{dx}\int_a^x f(t)\, dt$ | `\dfrac{d}{dx}\int_a^x f(t)\, dt` | the FTC1 setup |
| $\operatorname{erf}(x)$ | `\operatorname{erf}(x)` | error function — antiderivative of $\frac{2}{\sqrt\pi}e^{-x^2}$ |
| $\partial M$ | `\partial M` | boundary of a region $M$ (Stokes) |
| $\boxed{}$ | `\boxed{}` | end-of-proof marker |

---
chinese: 换元积分法 (huànyuán jīfēn fǎ)
prerequisites:
  - "[[Integration]]"
  - "[[Chain Rule]]"
  - "[[Differentiation]]"
  - "[[Fundamental Theorem of Calculus]]"
  - "[[Standard Integrals]]"
  - "[[Substitution Equations]]"
leads_to:
  - "[[Integration by Parts]]"
  - "[[Differential Equations]]"
  - "[[Partial Fractions]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-3-5
  - type/technique
  - type/theorem
  - notation/integral
  - notation/differential
  - misconception/forget-to-change-dx
  - misconception/forget-to-change-limits
  - misconception/wrong-u-choice
---

# Integration by Substitution 换元积分法

## Definition

**Integration by substitution** is the technique for evaluating integrals of the form

$$\int f(g(x)) \, g'(x) \, dx$$

by changing the variable of integration. If we let $u = g(x)$, then $du = g'(x) \, dx$ and the integral collapses into

$$\int f(u) \, du.$$

This is the **[[Chain Rule]] running in reverse**: the chain rule differentiates $F(g(x))$ to produce $F'(g(x)) \cdot g'(x)$, so integrating something of that shape must give back $F(g(x)) + C$. Substitution is the bookkeeping that makes the reverse direction mechanical.

> 换元 — literally "change the variable." Replace $x$ with a new variable $u$ that makes the integral simpler, do the integration, then change back.

---

## Why It Works — The Chain Rule in Reverse

This is not a new theorem invented for integration. It is a *restatement* of the chain rule.

**The chain rule says:** if $F'(u) = f(u)$ and $u = g(x)$, then

$$\frac{d}{dx}\bigl[F(g(x))\bigr] = F'(g(x)) \cdot g'(x) = f(g(x)) \cdot g'(x).$$

**Integrate both sides** with respect to $x$. The left side is a derivative being integrated, so it unwinds to $F(g(x)) + C$:

$$\int f(g(x)) \cdot g'(x) \, dx = F(g(x)) + C.$$

Now substitute $u = g(x)$:

$$F(g(x)) + C = F(u) + C = \int f(u) \, du.$$

So the two integrals are equal:

$$\boxed{\int f(g(x)) \, g'(x) \, dx = \int f(u) \, du \quad \text{where } u = g(x).}$$

That is the whole theorem. Every u-substitution you will ever do is an application of this single identity.

![[integration-by-substitution-area-preservation.svg|697]]

Geometrically: the substitution *warps the $x$-axis* into the $u$-axis. The integrand's shape changes — $2x(x^2+1)^3$ climbs steeply in $x$, whereas $u^3$ rises more gently in $u$ — but the **area under the curve is identical**. Integration measures an accumulated total, and total is exactly what a change of variable preserves.

> [!tip] "Secretly integration by substitution" — the linear-inside rule unmasked
> The linear-inside rule in [[Integration]] (the $/a$ trick for $\int (ax+b)^n \, dx$) is exactly this theorem with $u = ax+b$, so $du = a \, dx$. The mysterious $/a$ is $du/a$. You have been doing substitution all along — this card makes it explicit and general.

---

## The Procedure — Five Steps

For $\displaystyle \int f(g(x)) \, g'(x) \, dx$:

1. **Choose $u$.** Pick $u = g(x)$ — typically the "inside" of a composite function, or the expression whose derivative you can spot elsewhere in the integrand.
2. **Compute $du$.** Differentiate: $\dfrac{du}{dx} = g'(x)$, so $du = g'(x) \, dx$.
3. **Rewrite the integrand in $u$.** Every $g(x)$ becomes $u$; the $g'(x) \, dx$ piece becomes $du$. If a constant factor is off, absorb it explicitly (e.g., if $g'(x) \, dx = 2 \, du$, rearrange to $dx = du/(2x)$ or multiply/divide as needed).
4. **Integrate in $u$.** You should now have a standard integral $\int f(u) \, du$.
5. **Substitute back.** Replace $u$ with $g(x)$ to express the answer in the original variable. (For indefinite integrals only — see the definite-integral shortcut below.)

The hard step is **Step 1**. Choosing $u$ correctly is the skill. The rest is bookkeeping.

### How to Choose $u$

There is no universal rule, but three heuristics cover the vast majority of exam integrals:

- **Look for a composite.** If the integrand contains something like $\sin(x^3)$ or $e^{x^2}$ or $\sqrt{1 + x^4}$, the inside is a strong candidate: $u = x^3$, $u = x^2$, $u = 1 + x^4$.
- **Look for a derivative/antiderivative pair.** If the integrand has $h(x)$ and $h'(x)$ both present as factors, let $u = h(x)$.
- **Look for the most awkward thing.** If one piece of the integrand is blocking you (a $\ln x$, a $\sqrt{\cdots}$, a $\tan^{-1} x$), try letting $u$ *be* that awkward thing and see if $du$ cancels the other stuff.

---

## Definite Integrals — Change the Limits

For a **definite integral**, you have two equally valid routes.

**Route A — substitute back at the end.** Do the u-substitution, integrate in $u$, substitute $u = g(x)$ to return to $x$, then evaluate between the original $x$-limits.

**Route B — change the limits.** Do the u-substitution, integrate in $u$, and evaluate between the *transformed* limits $u = g(a)$ and $u = g(b)$. Never substitute back:

$$\int_a^b f(g(x)) \, g'(x) \, dx = \int_{g(a)}^{g(b)} f(u) \, du.$$

Route B is faster and less error-prone — no ugly final re-substitution. But it requires discipline: *never evaluate in $u$ at the original $x$-values.* If you change the variable, change the limits.

> [!warning] The single most common definite-integral mistake
> Changing to $u$, integrating, then plugging in the original $x$-limits $a, b$. That gives a wrong answer because the expression is now in $u$, not $x$. Either change the limits or substitute back — pick one route and commit.

---

## Worked Examples

### Example 1 — The Archetypal Reverse Chain

Evaluate $\displaystyle \int 2x \, (x^2 + 1)^5 \, dx.$

The composite is $(x^2 + 1)^5$. Let $u = x^2 + 1$. Then $du = 2x \, dx$ — and there is $2x \, dx$ already sitting in the integrand. Perfect match.

$$\int 2x \, (x^2 + 1)^5 \, dx = \int u^5 \, du = \frac{u^6}{6} + C = \frac{(x^2 + 1)^6}{6} + C.$$

**Check by differentiating.** $\dfrac{d}{dx}\left[\dfrac{(x^2+1)^6}{6}\right] = \dfrac{6(x^2+1)^5 \cdot 2x}{6} = 2x(x^2+1)^5$. ✓

### Example 2 — Absorbing a Constant

Evaluate $\displaystyle \int x \, (x^2 + 1)^5 \, dx.$

Same composite, but now only $x \, dx$, not $2x \, dx$. Let $u = x^2 + 1$, so $du = 2x \, dx$, which means $x \, dx = \dfrac{1}{2} \, du$.

$$\int x (x^2 + 1)^5 \, dx = \int u^5 \cdot \frac{1}{2} \, du = \frac{1}{2} \cdot \frac{u^6}{6} + C = \frac{(x^2 + 1)^6}{12} + C.$$

Constants are easy to pull through — they never change. Only constants. If the mismatched piece involves $x$, substitution will not work, and you need a different technique.

### Example 3 — A Trig Integral

Evaluate $\displaystyle \int \sec^2 x \, \tan x \, dx.$

Spot the derivative/antiderivative pair: $\tan x$ is in the integrand, and $\dfrac{d}{dx} \tan x = \sec^2 x$ is also there. Let $u = \tan x$, so $du = \sec^2 x \, dx$.

$$\int \sec^2 x \, \tan x \, dx = \int u \, du = \frac{u^2}{2} + C = \frac{\tan^2 x}{2} + C.$$

> [!tip] Alternative for Example 3
> You could equally let $u = \sec x$, since $\dfrac{d}{dx} \sec x = \sec x \tan x$, giving $\dfrac{\sec^2 x}{2} + C$. The two answers differ by a constant ($\sec^2 x = 1 + \tan^2 x$), so both are correct — they live in the same $+C$ family.

### Example 4 — Definite Integral with Limit Change

Evaluate $\displaystyle \int_0^1 x \, (x^2 + 1)^5 \, dx.$

Let $u = x^2 + 1$, so $du = 2x \, dx$ and $x \, dx = \tfrac{1}{2} du$. Change the limits: when $x = 0$, $u = 1$; when $x = 1$, $u = 2$.

$$\int_0^1 x(x^2 + 1)^5 \, dx = \int_1^2 \frac{1}{2} u^5 \, du = \frac{1}{2}\left[\frac{u^6}{6}\right]_1^2 = \frac{1}{12}(64 - 1) = \frac{63}{12} = \frac{21}{4}.$$

Notice: the $x$-limits $0, 1$ became $u$-limits $1, 2$, and we never converted back to $x$.

### Example 5 — A 9709 P3-Style Given Substitution

Using the substitution $u = 1 + \sqrt{x}$, evaluate $\displaystyle \int_1^4 \frac{1}{\sqrt{x}\,(1 + \sqrt{x})^2} \, dx.$

From $u = 1 + \sqrt{x}$, we have $\dfrac{du}{dx} = \dfrac{1}{2\sqrt{x}}$, so $\dfrac{1}{\sqrt{x}} \, dx = 2 \, du$. When $x = 1$, $u = 2$; when $x = 4$, $u = 3$.

$$\int_1^4 \frac{1}{\sqrt{x}(1 + \sqrt{x})^2} \, dx = \int_2^3 \frac{2 \, du}{u^2} = 2 \left[-\frac{1}{u}\right]_2^3 = 2\left(-\frac{1}{3} + \frac{1}{2}\right) = 2 \cdot \frac{1}{6} = \frac{1}{3}.$$

9709 P3 almost always *gives* the substitution — the exam skill is executing it cleanly, not inventing it.

---

## Standard Patterns Worth Memorising

Three substitution patterns come up so often that they are worth recognising by shape.

### Pattern 1 — The $f'/f$ Pattern

$$\int \frac{g'(x)}{g(x)} \, dx = \ln \lvert g(x) \rvert + C.$$

**Proof.** Let $u = g(x)$, so $du = g'(x) \, dx$. Then $\int \dfrac{du}{u} = \ln|u| + C = \ln|g(x)| + C.$

> Examples.
> - $\displaystyle \int \frac{2x}{x^2 + 1} \, dx = \ln(x^2 + 1) + C$ (the denominator is always positive, so no absolute value needed).
> - $\displaystyle \int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx = -\ln \lvert \cos x \rvert + C = \ln \lvert \sec x \rvert + C$. (The minus comes from $\frac{d}{dx}\cos x = -\sin x$, so we need $u = \cos x$ with $du = -\sin x \, dx$.)
> - $\displaystyle \int \cot x \, dx = \int \frac{\cos x}{\sin x} \, dx = \ln \lvert \sin x \rvert + C.$

This is the first pattern to check whenever you see a fraction.

### Pattern 2 — Linear-Inside (the Baby Case)

Covered in [[Integration#The Linear-Inside Rule $(ax + b)^n$|Integration]]. Here, $u = ax + b$, so $du = a \, dx$. This is substitution with its training wheels on: the chain-rule coefficient is always the constant $a$, so the answer always picks up a $/a$.

### Pattern 3 — Power-of-a-Function

$$\int [g(x)]^n \, g'(x) \, dx = \frac{[g(x)]^{n+1}}{n+1} + C \quad (n \ne -1).$$

This is Example 1 generalised. Let $u = g(x)$, so $\int u^n \, du = \dfrac{u^{n+1}}{n+1} + C$.

> Example. $\displaystyle \int x \sqrt{1 + x^2} \, dx$. Let $u = 1 + x^2$, $du = 2x \, dx$. Then $\int x(1+x^2)^{1/2} \, dx = \tfrac12 \int u^{1/2} \, du = \tfrac12 \cdot \tfrac23 u^{3/2} + C = \tfrac13 (1+x^2)^{3/2} + C.$

---

## Trig Integrals That Are Really Substitution

Trig integrals scare students because they don't look like the tidy composites of Examples 1–3. But a huge fraction of them are secretly u-substitution — you just have to know the tricks.

> [!warning] Exam tactic — for any trig integral, **try substitution first**
> The overwhelming majority of trig integrals in exam papers are substitution problems in disguise. Before reaching for [[Integration by Parts]], scan the integrand for a derivative/antiderivative pair. Substitution is the *default* move for trig; parts is the *exception*.

> [!tip] The decision rule (substitution vs. [[Integration by Parts]])
> **If one factor's derivative appears as the other factor (up to a constant) → substitution.**
> **If the integrand is a product of different families (polynomial × trig, log × anything, exponential × trig) and no factor is the derivative of another → parts.**
>
> This is the single most useful heuristic for trig integrals. Check it *before* you start computing.

### Trick A — Odd power of sine or cosine: peel one off

Evaluate $\displaystyle \int \sin^3 x \, dx.$

There is no $\cos x$ in sight, so at first this looks like substitution won't help. But **peel off one factor of $\sin x$** and use $\sin^2 x = 1 - \cos^2 x$:

$$\int \sin^3 x \, dx = \int \sin^2 x \cdot \sin x \, dx = \int (1 - \cos^2 x) \sin x \, dx.$$

Now $\sin x$ is begging to be the $du$ of $u = \cos x$, because $du = -\sin x \, dx$. Substitute:

$$\int (1 - \cos^2 x) \sin x \, dx = \int (1 - u^2)(-du) = -u + \frac{u^3}{3} + C = -\cos x + \frac{\cos^3 x}{3} + C.$$

**The general strategy for $\displaystyle \int \sin^m x \cos^n x \, dx$:**

| Case | Strategy |
|------|----------|
| $m$ odd | Peel off one $\sin x$; convert remaining $\sin^{m-1} x$ to cosines via $\sin^2 = 1 - \cos^2$; let $u = \cos x$ |
| $n$ odd | Peel off one $\cos x$; convert remaining $\cos^{n-1} x$ to sines via $\cos^2 = 1 - \sin^2$; let $u = \sin x$ |
| Both even | Substitution fails directly — power-reduce first (see Trick B) |

The rule has an elegant symmetry: **at least one odd exponent means substitution works**. The odd factor donates one of itself to be the $du$; the rest converts cleanly via the Pythagorean identity.

### Trick B — Both even? Power-reduce first

Evaluate $\displaystyle \int \sin^2 x \, dx.$

No odd factor to peel. Instead, **flatten the power using the half-angle identity** $\sin^2 x = \dfrac{1 - \cos 2x}{2}$:

$$\int \sin^2 x \, dx = \int \frac{1 - \cos 2x}{2} \, dx = \frac{x}{2} - \frac{\sin 2x}{4} + C.$$

(The $\cos 2x$ integral is a linear-inside from [[Integration]].) The half-angle identities are the standard weapons here:

$$\sin^2 x = \frac{1 - \cos 2x}{2}, \qquad \cos^2 x = \frac{1 + \cos 2x}{2}.$$

For $\int \sin^4 x \, dx$ or $\int \cos^4 x \, dx$, apply the half-angle twice — the second application handles the $\cos^2 2x$ that appears after the first.

### Trick C — $\tan^n x \sec^2 x$ and $\sec^n x \tan x$

$\displaystyle \int \tan^3 x \sec^2 x \, dx$: let $u = \tan x$, $du = \sec^2 x \, dx$, so $\int u^3 \, du = \tfrac{\tan^4 x}{4} + C.$

$\displaystyle \int \sec^3 x \tan x \, dx$: let $u = \sec x$, $du = \sec x \tan x \, dx$, so $\int u^2 \, du = \tfrac{\sec^3 x}{3} + C.$

Both are Example 3 in disguise — derivative/antiderivative pairs hiding behind trig names.

> [!warning] When substitution is the *wrong* tool — use Parts
> Integrals like $\int x \sin x \, dx$, $\int x^2 \cos x \, dx$, $\int e^x \sin x \, dx$, $\int \ln x \, dx$, $\int \tan^{-1} x \, dx$ are **not substitution problems**. None of them has a factor whose derivative is the other factor. They need [[Integration by Parts]] — a different reverse of a different product, which opens with the same decision rule.

---

## Common Misconceptions

### 1. Forgetting to change $dx$ to $du$

Writing $\int (x^2 + 1)^5 \cdot 2x \, dx = \int u^5 \cdot 2x \, dx$ and then being stuck. You must fully eliminate $x$ from the integrand before integrating — including the $dx$.

**Fix.** Mechanical discipline: every substitution step rewrites *three* things at once — the $f(g(x))$ piece, the $dx$ piece, and (for definite integrals) the limits. Treat them as a package, never as individual swaps.

### 2. Trying to substitute when $du$ doesn't match

Attempting $\int (x^2 + 1)^5 \, dx$ with $u = x^2 + 1$. Then $du = 2x \, dx$, but there is no $x$ in the integrand to absorb. Writing "$dx = du / (2x)$" and carrying $x$ in the $u$-integral breaks the technique — you cannot have $x$ and $u$ mixed in the same integral.

**Fix.** Before committing to $u = g(x)$, check that $g'(x)$ (or a constant multiple of it) is already present. If not, this is not a substitution problem — it needs a different method (likely [[Integration by Parts]] or no elementary antiderivative at all).

### 3. Forgetting to change the limits on a definite integral

Classic trap. Student changes to $u$, integrates in $u$, then plugs in the original $x$-limits without converting.

**Fix.** A ritual: when you write the line "let $u = \ldots$", also write "$x = a \Rightarrow u = \ldots$" and "$x = b \Rightarrow u = \ldots$" *in the same line*. Convert limits at the moment you define the substitution.

### 4. Not substituting back in an indefinite integral

Leaving the answer as $\dfrac{u^6}{6} + C$ instead of $\dfrac{(x^2 + 1)^6}{6} + C$.

**Fix.** Indefinite integrals must end in the original variable. If the question starts in $x$, the final answer is in $x$. Only definite integrals escape this requirement — because they evaluate to a number, which has no variable at all.

### 5. Choosing $u$ = the whole integrand

Out of desperation, writing "let $u = x \sqrt{1 + x^2}$" for the whole messy expression. That makes $du$ worse, not better.

**Fix.** $u$ should simplify the integrand. The good $u$ is usually small — a single inside-of-a-composite, not the whole integrand. When in doubt, pick the smallest expression whose derivative you can spot elsewhere.

---

## Exam Notes

### Cambridge A-Level 9709

**Paper 3 §3.5** explicitly requires substitution — and Cambridge almost always **gives the substitution** in the question stem ("Using the substitution $u = \ldots$, evaluate…"). The exam skill is execution, not invention. Typical instruction:

> "Use the substitution $u = 1 + \sqrt{x}$ to show that $\int_0^{\,9} \dfrac{dx}{\sqrt{x}(1 + \sqrt{x})} = 2 \ln 2.$"

Memorise the three-line procedure: (1) compute $du$; (2) change the limits; (3) rewrite the integrand in $u$. Two marks for each.

Substitution is **not** on 9709 Paper 1 or Paper 2 — those papers stop at the linear-inside rule. But the linear-inside rule *is* substitution in disguise, as flagged in [[Integration]].

### Cambridge 0580 / 0606

**Not examined at either.** 0580 has no integration; 0606 integrates only the recognisable forms — powers of $(ax+b)$, $e^{ax+b}$, $\sin(ax+b)$, $\cos(ax+b)$ — which are the linear-inside family again, never a change of variable the student performs.

### Cambridge 9231 (Further Maths)

Assumed from P3, then made *systematic*: FP2 §2.4 names the three standard forms $\dfrac{1}{\sqrt{a^2-x^2}}$, $\dfrac{1}{\sqrt{x^2+a^2}}$, $\dfrac{1}{\sqrt{x^2-a^2}}$, integrated by **trigonometric or hyperbolic substitution** — [[Standard Integrals]] tabulates the recognition forms and [[Hyperbolic Functions]] derives the log forms the hyperbolic route lands on. Longer Paper 2 integrals ([[Arc Length and Surfaces of Revolution]]'s surface cases, [[Reduction Formulae]]'s set-ups) usually *give* the substitution, 9709-style; the FP2-specific skill is choosing between the trig and hyperbolic routes for the three standard shapes.

### Edexcel IAL / OxAQA 9660

IAL names substitution at **P4.6.2** (alongside parts); OxAQA 9660 at **P2.7**, where the syllabus pairs it with *integration by inspection* — recognising $\int f'(x)[f(x)]^n\,dx$ and $\int \frac{f'(x)}{f(x)}\,dx$ without writing the $u$ down, which is exactly this card's method internalised. Both boards, like 9709, usually supply the substitution for anything non-obvious.

### IB AA HL

Substitution is a technique students must *invent* more often than at Cambridge (AA HL's integration extension expects "substitution as a required technique", with non-obvious choices fair game). AA HL is also where the named **trigonometric substitutions** genuinely live at school level:

- $x = a \sin \theta \Rightarrow dx = a \cos \theta \, d\theta$, useful for $\sqrt{a^2 - x^2}$
- $x = a \tan \theta \Rightarrow dx = a \sec^2 \theta \, d\theta$, useful for $a^2 + x^2$

These exploit Pythagorean identities (e.g. $1 - \sin^2 \theta = \cos^2 \theta$) to convert algebraic radicals into clean trig expressions — the same move 9231 makes with its hyperbolic siblings.

### AP Calculus AB / BC

Unit 6 introduces u-substitution (Topic 6.9 for AB, extended integrand families at BC) — and both routes expect the substitution to be *invented*, on integrands built to make the choice visible. **Trigonometric substitution is not in the current AP course description** for either route — BC's named extras are integration by parts and linear partial fractions — so the trig-sub machinery above is IB/9231 territory, not AP's. The FRQ style tends to include substitution as a *step* in a longer kinematics or area/volume problem, not a standalone exercise.

> [!info] Beyond syllabus — Weierstrass substitution
> For integrands rational in $\sin x$ and $\cos x$ (e.g. $\int \dfrac{dx}{1 + \sin x}$), the substitution $t = \tan(x/2)$ converts everything into a rational function of $t$:
> $$\sin x = \frac{2t}{1+t^2}, \quad \cos x = \frac{1-t^2}{1+t^2}, \quad dx = \frac{2}{1+t^2} \, dt.$$
> Every rational-trig integral becomes a rational-$t$ integral, solvable by [[Partial Fractions]]. This is the "big hammer" of trig integration, named after Karl Weierstrass. Overkill for exams, but beautiful — a single substitution that in principle integrates any rational trig expression.

### Beyond high school — University

Substitution generalises to **the change-of-variable theorem** in multivariable integration. For a 2D integral under a map $(u, v) \mapsto (x, y)$ with inverse $(x, y) \mapsto (u(x,y), v(x,y))$,

$$\iint_R f(x, y) \, dA = \iint_{R'} f(x(u,v), y(u,v)) \, \lvert J \rvert \, du \, dv,$$

where $\lvert J \rvert$ is the absolute value of the **Jacobian determinant**. In 1D, the Jacobian is just $|g'(x)|$, which is why 1D substitution has the $g'(x) \, dx = du$ that this card is built around. Polar coordinates ($dA = r \, dr \, d\theta$) are the most famous example — the $r$ is the 2D Jacobian.

---

## Connections

- **Parent:** [[Integration]] — substitution is the first of two general techniques (the other being [[Integration by Parts]]).
- **Reverse of:** [[Chain Rule]] — this card is the chain rule run backwards, and every substitution that works does so because some composite $F(g(x))$ chain-ruled to produce the original integrand.
- **Siblings:** [[Integration by Parts]] (reverses the product rule instead of the chain rule); [[Partial Fractions]] (algebraic pre-processing before integration).
- **Application:** [[Differential Equations]] — separable ODEs are solved by substitution in the $dy$ direction.
- **Application — reserved:** [[Kinematics Calculus]] — velocity-to-displacement integrals often need substitution when the velocity depends on a composite expression of time.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\displaystyle \int f(u) \, du$ | `\int f(u) \, du` | Use `\,` for the small space before $du$ |
| $u = g(x)$ | `u = g(x)` | Substitution declaration |
| $du = g'(x) \, dx$ | `du = g'(x) \, dx` | Differential form |
| $\displaystyle \int_{g(a)}^{g(b)}$ | `\int_{g(a)}^{g(b)}` | Transformed limits |
| $\dfrac{du}{dx}$ | `\dfrac{du}{dx}` | Display-size derivative |
| $\lvert g(x) \rvert$ | `\lvert g(x) \rvert` | Absolute value inside $\ln$ — safe inside tables |
| $\sqrt{a^2 - x^2}$ | `\sqrt{a^2 - x^2}` | Trig-sub signature form |

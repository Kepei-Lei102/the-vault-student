---
chinese: 分部积分法 (fēnbù jīfēn fǎ)
prerequisites:
  - "[[Integration]]"
  - "[[Differentiation]]"
  - "[[Product Rule]]"
  - "[[Fundamental Theorem of Calculus]]"
  - "[[Integration by Substitution]]"
  - "[[Standard Integrals]]"
leads_to:
  - "[[Differential Equations]]"
  - "[[Reduction Formulae]]"
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
  - syllabus/9231-2-4
  - type/technique
  - type/theorem
  - notation/integral
  - notation/differential
  - misconception/wrong-u-choice
  - misconception/sign-error
  - misconception/infinite-loop
---

# Integration by Parts 分部积分法

## Definition

**Integration by parts** is the technique for integrating a product of two functions by turning the integral into a *different* integral that is (hopefully) easier.

$$\boxed{\int u \, dv = uv - \int v \, du}$$

Equivalently, in function notation with $u = f(x)$ and $v = g(x)$:

$$\int f(x) \, g'(x) \, dx = f(x) \, g(x) - \int f'(x) \, g(x) \, dx.$$

It is the **[[Product Rule|product rule]] running in reverse**, just as [[Integration by Substitution]] is the chain rule in reverse. Between the two techniques, you can attack almost every elementary integral you will meet.

> 分部 — literally "split into parts." Split the integrand into $u$ and $dv$, differentiate one and integrate the other, and use the trade-off to simplify.

---

## Why It Works — The Product Rule in Reverse

**The product rule says:** if $u$ and $v$ are both functions of $x$, then

$$\frac{d}{dx}(uv) = u \frac{dv}{dx} + v \frac{du}{dx}.$$

**Integrate both sides** with respect to $x$. The left side is a derivative being integrated, so it unwinds to $uv$:

$$uv = \int u \frac{dv}{dx} \, dx + \int v \frac{du}{dx} \, dx = \int u \, dv + \int v \, du.$$

Rearrange:

$$\int u \, dv = uv - \int v \, du.$$

That is the formula. Like substitution, **integration by parts is not a new theorem — it is the product rule read backwards.**

> [!tip] Why the trade matters
> On its own, $\int u \, dv$ and $\int v \, du$ are both integrals — neither is obviously easier than the other. The technique is only useful when the **new** integral $\int v \, du$ is simpler than the **original** $\int u \, dv$. Choosing $u$ and $dv$ well is the entire skill.

![[integration-by-parts-geometric.svg|640]]

Geometrically: for a parametric curve from $(u_1, v_1)$ to $(u_2, v_2)$, the rectangle's area $uv$ splits into the area *below* the curve (which is $\int v \, du$) plus the area *left of* the curve (which is $\int u \, dv$). The IBP formula is the algebraic statement of that picture.

---

## The Procedure — Five Steps

For an integral of the form $\int (\text{product}) \, dx$:

1. **Choose $u$ and $dv$.** Split the integrand into two factors. One becomes $u$ (to be differentiated); the other, together with $dx$, becomes $dv$ (to be integrated).
2. **Compute $du$ and $v$.** Differentiate $u$ to get $du$; integrate $dv$ to get $v$. (You don't need a $+C$ at this step — any antiderivative works.)
3. **Apply the formula.** Write $uv - \int v \, du$.
4. **Integrate the remainder.** $\int v \, du$ should now be something you can evaluate — by a standard integral, by substitution, or by a second round of parts.
5. **Simplify and $+C$.** Add the constant of integration at the end (for indefinite integrals).

The hard step is **Step 1**. A bad choice of $u$ and $dv$ makes the new integral *worse*, not better.

---

## How to Choose $u$ — the Disappearance Principle

The IBP formula trades the original integral $\int u \, dv$ for a new one $\int v \, du$. The trade is only useful if $du$ is *simpler* than $u$. So the real question — the only question — is:

> [!tip] The disappearance principle
> **Which factor, when differentiated, disappears or collapses into something much simpler?**
>
> Pick that factor as $u$. The other factor (with $dx$) becomes $dv$.

After parts, $u$ has been differentiated into $du$. If differentiating $u$ kills it, the new integral is *clean*. If differentiating $u$ leaves it the same size (like $\sin x \to \cos x$) or grows it, you have made no progress — or made it worse.

This principle is the whole idea. Everything below is just tactics.

### The LIATE shortcut

The disappearance principle, sorted into a priority list:

$$\text{\textbf{L}ogarithm} \ >\ \text{\textbf{I}nverse trig} \ >\ \text{\textbf{A}lgebraic} \ >\ \text{\textbf{T}rig} \ >\ \text{\textbf{E}xponential}$$

**The factor earlier in the list becomes $u$.** The letters are ranked by *how well they disappear* under differentiation:

- $\ln x \xrightarrow{d/dx} \dfrac{1}{x}$ — the log **vanishes entirely**. L wins top spot.
- $\tan^{-1} x \xrightarrow{d/dx} \dfrac{1}{1 + x^2}$ — inverse trig **collapses into a rational function**. Nearly as good. I comes second.
- $x^n \xrightarrow{d/dx} n x^{n-1}$ — algebraic loses one power each round. Shrinks, but doesn't vanish. A is third.
- $\sin x \xrightarrow{d/dx} \cos x$ — trig just rotates. Same size. T is fourth.
- $e^x \xrightarrow{d/dx} e^x$ — exponential **doesn't budge at all**. Worst $u$-candidate; E sits last.

So LIATE is not an arbitrary mnemonic — it is the disappearance principle sorted. And the reason L and I are up front is *exactly* the reason we want them gone: differentiating them kills them.

| Integral | $u$ | $dv$ | Why |
|----------|-----|------|-----|
| $\int x \sin x \, dx$ | $x$ (A) | $\sin x \, dx$ (T) | $x \to 1$ disappears; $\sin x$ would just rotate |
| $\int x^2 e^x \, dx$ | $x^2$ (A) | $e^x \, dx$ (E) | $x^2$ shrinks; $e^x$ would never move |
| $\int \ln x \, dx$ | $\ln x$ (L) | $dx$ (A) | $\ln x \to 1/x$ vanishes as a log |
| $\int x \ln x \, dx$ | $\ln x$ (L) | $x \, dx$ (A) | Kill the log first, even against an algebraic factor |
| $\int x \tan^{-1} x \, dx$ | $\tan^{-1} x$ (I) | $x \, dx$ (A) | Inverse trig collapses to rational |

**When LIATE seems ambiguous, fall back on the principle.** Ask which factor dies fastest under differentiation — that is your $u$. The table is shorthand; the principle is the law.

---

## Worked Examples

### Example 1 — Polynomial × Trig

Evaluate $\displaystyle \int x \sin x \, dx.$

LIATE: $u = x$ (A), $dv = \sin x \, dx$ (T). Then $du = dx$ and $v = -\cos x$.

$$\int x \sin x \, dx = uv - \int v \, du = -x \cos x - \int (-\cos x) \, dx = -x \cos x + \sin x + C.$$

**Check by differentiating.** $\dfrac{d}{dx}[-x \cos x + \sin x] = -\cos x + x \sin x + \cos x = x \sin x.$ ✓

### Example 2 — Parts Twice

Evaluate $\displaystyle \int x^2 e^x \, dx.$

LIATE: $u = x^2$, $dv = e^x \, dx$. Then $du = 2x \, dx$, $v = e^x$.

$$\int x^2 e^x \, dx = x^2 e^x - \int 2x e^x \, dx.$$

The new integral $\int 2x e^x \, dx$ is simpler (one less power of $x$) but not yet elementary. **Apply parts again** to $\int x e^x \, dx$: $u = x$, $dv = e^x \, dx$, giving $xe^x - e^x$. So

$$\int 2x e^x \, dx = 2(xe^x - e^x).$$

Therefore

$$\int x^2 e^x \, dx = x^2 e^x - 2xe^x + 2e^x + C = e^x(x^2 - 2x + 2) + C.$$

**Pattern.** Each round of parts peels one power off $x$. For $\int x^n e^x \, dx$, you need $n$ rounds.

### Example 3 — $\int \ln x \, dx$: the "Factor of 1" Trick

Evaluate $\displaystyle \int \ln x \, dx.$

It looks like a single function, not a product. But write $\ln x = (\ln x) \cdot 1$ and treat $dx$ as integrating that factor of 1. LIATE: $u = \ln x$ (L), $dv = dx$ (A). Then $du = \dfrac{1}{x} dx$ and $v = x$.

$$\int \ln x \, dx = x \ln x - \int x \cdot \frac{1}{x} \, dx = x \ln x - \int 1 \, dx = x \ln x - x + C.$$

This trick also evaluates $\int \tan^{-1} x \, dx$, $\int \sin^{-1} x \, dx$, and any other "log or inverse-trig alone" integral.

### Example 4 — The Self-Referential Trick

Evaluate $\displaystyle I = \int e^x \sin x \, dx.$

LIATE says $u = e^x$ (E) or $\sin x$ (T) — E is last, so $u = \sin x$, $dv = e^x \, dx$. Then $du = \cos x \, dx$, $v = e^x$:

$$I = e^x \sin x - \int e^x \cos x \, dx.$$

Apply parts again to the new integral: $u = \cos x$, $dv = e^x \, dx$. Then $du = -\sin x \, dx$, $v = e^x$:

$$\int e^x \cos x \, dx = e^x \cos x - \int e^x (-\sin x) \, dx = e^x \cos x + \int e^x \sin x \, dx = e^x \cos x + I.$$

Substitute back:

$$I = e^x \sin x - (e^x \cos x + I) = e^x \sin x - e^x \cos x - I.$$

Solve for $I$:

$$2I = e^x(\sin x - \cos x) \quad\Rightarrow\quad I = \frac{e^x(\sin x - \cos x)}{2} + C.$$

**The trick:** after two rounds of parts, the original integral $I$ reappears. Treat the equation as algebra — solve for $I$.

> [!tip] Why the "choose the same kind" rule matters
> Crucial detail: both rounds used $dv = e^x \, dx$. If you flip the choice on the second round (picking $dv = \cos x \, dx$ instead), you un-do the first round and spiral back to the starting integral. **Stay consistent** — whichever family you chose for $dv$ the first time, keep it for $dv$ the second time.

### Example 5 — 9709 P3-Style Definite Integral

Evaluate $\displaystyle \int_0^1 x e^{2x} \, dx.$

LIATE: $u = x$, $dv = e^{2x} \, dx$. Then $du = dx$, $v = \tfrac{1}{2} e^{2x}$.

$$\int x e^{2x} \, dx = \frac{x e^{2x}}{2} - \int \frac{e^{2x}}{2} \, dx = \frac{x e^{2x}}{2} - \frac{e^{2x}}{4} + C.$$

Evaluate between 0 and 1:

$$\left[\frac{x e^{2x}}{2} - \frac{e^{2x}}{4}\right]_0^1 = \left(\frac{e^2}{2} - \frac{e^2}{4}\right) - \left(0 - \frac{1}{4}\right) = \frac{e^2}{4} + \frac{1}{4} = \frac{e^2 + 1}{4}.$$

---

## Trig Integrals That Need Parts

The sibling card [[Integration by Substitution]] covers the trig integrals where one factor's derivative appears as the other factor. **This card covers the integrals where that does *not* happen** — products of different families where the only move is parts.

> [!warning] Exam tactic — substitution *first*, parts *second*
> For any trig integral on the page, **reach for substitution first**. The overwhelming majority of trig integrals a student meets are substitution problems in disguise — odd-power peels, $f'/f$ patterns ($\tan x$, $\cot x$), $\tan^n x \sec^2 x$ and $\sec^n x \tan x$ families, and half-angle power-reduction. All of those live on the Substitution card.
>
> **Only reach for parts if substitution clearly fails:** no matching derivative/antiderivative pair, and the integrand is a product of different families (polynomial × trig, exponential × trig, log × anything). Parts is the exception rule for trig, not the default.

> [!tip] Decision rule (restated from the Substitution card)
> **If one factor's derivative appears as the other factor (up to a constant) → substitution.**
> **Otherwise, if the integrand is a product of different families (polynomial × trig, log × anything, exponential × trig) → parts.**

### Parts territory

| Integral                                                 | Technique                      | $u$ choice        |
| -------------------------------------------------------- | ------------------------------ | ----------------- |
| $\int x^n \sin x \, dx$, $\int x^n \cos x \, dx$         | parts, $n$ times               | $u = x^n$         |
| $\int x^n e^{ax} \, dx$                                  | parts, $n$ times               | $u = x^n$         |
| $\int e^{ax} \sin bx \, dx$, $\int e^{ax} \cos bx \, dx$ | parts twice (self-referential) | $u =$ trig factor |
| $\int \ln x \, dx$, $\int x^n \ln x \, dx$               | parts once                     | $u = \ln x$       |
| $\int \tan^{-1} x \, dx$, $\int x \tan^{-1} x \, dx$     | parts once                     | $u = \tan^{-1} x$ |
| $\int \sin^{-1} x \, dx$                                 | parts once (factor-of-1)       | $u = \sin^{-1} x$ |

**The test:** look at the two factors. Is one the derivative of the other (up to a constant)? If yes, substitute. If they come from different families and neither is the derivative of the other, parts is the only way.

### Example — Parts then substitution

Not every integral is pure substitution or pure parts. $\displaystyle \int x \ln(1 + x^2) \, dx$ is parts first: $u = \ln(1+x^2)$, $dv = x \, dx$, giving

$$\int x \ln(1 + x^2) \, dx = \frac{x^2}{2}\ln(1+x^2) - \int \frac{x^2}{2} \cdot \frac{2x}{1+x^2} \, dx = \frac{x^2}{2}\ln(1+x^2) - \int \frac{x^3}{1+x^2} \, dx.$$

The remaining integral is finished by substitution $u = 1 + x^2$ (or polynomial long division). Real problems often need both techniques in sequence — don't think of them as rivals.

---

## Common Misconceptions

### 1. Choosing $u$ and $dv$ against LIATE

Writing $\int x \sin x \, dx$ with $u = \sin x$, $dv = x \, dx$. Then $du = \cos x \, dx$, $v = x^2/2$, and the new integral is $\int (x^2/2) \cos x \, dx$ — *worse* than the original ($x^2$ instead of $x$).

**Fix.** Commit to LIATE for the first few dozen exam problems. The rule almost never misfires at this level.

### 2. Sign error on $\int v \, du$

The formula is $uv - \int v \, du$. The **minus** is easy to drop, especially after a second or third round where signs compound. Every missed minus breaks the answer.

**Fix.** Write the formula explicitly on every application — don't shortcut the $uv$ term. Circle the minus sign before proceeding.

### 3. Adding $+C$ to the intermediate $v$

When you compute $v = \int dv$, you do **not** need a constant of integration *inside* the parts formula. The final $+C$ at the end of the problem absorbs everything. Including a $+C_1$ in the middle leads to $+C_1 \cdot u$ extras that cancel out but clutter the working.

**Fix.** Treat $v$ as *any* antiderivative of $dv$. The simplest one (no $+C$) is always correct for the middle step.

### 4. Infinite loop on self-referential integrals

On $\int e^x \sin x \, dx$, flipping the $dv$ choice between the two rounds (first $dv = e^x dx$, then $dv = \cos x \, dx$) spirals back to the starting integral and gives $I = I$ — a useless tautology.

**Fix.** Once you choose a family for $dv$ (exponential or trig), **stick with it for both rounds**. The algebraic trick only closes the loop when $dv$ stays the same kind.

### 5. Applying parts when substitution was the right move

$\int 2x (x^2 + 1)^5 \, dx$ is a substitution problem ($u = x^2 + 1$), not a parts problem. Choosing $u = 2x$, $dv = (x^2+1)^5 dx$ forces you to integrate $(x^2+1)^5$ by expansion — a mess. **Check the decision rule first.**

**Fix.** Before starting either technique, ask: "Is one factor the derivative of the other?" If yes, it is substitution. Only commit to parts once substitution is ruled out.

---

## Exam Notes

### Cambridge A-Level 9709

**Paper 3 §3.5** lists integration by parts as a required technique. Typical question style:

> "Use integration by parts to find $\displaystyle \int x \cos 2x \, dx$."
> "By integrating by parts twice, show that $\displaystyle \int_0^\pi e^{-x} \sin x \, dx = \frac{1 + e^{-\pi}}{2}.$"

Unlike substitution, parts is often **not** spoon-fed — Cambridge expects you to recognise "product of different families" and pick LIATE yourself. Practice spotting the two signatures: polynomial × trig/exp (one round per power), and trig × exp (self-referential two rounds).

Parts is **not** on 9709 Paper 1 or Paper 2.

### Cambridge 0580 / 0606

**Not examined at either.** 0580 has no integration at all, and 0606's integration stops at recognisable antiderivatives — powers of $(ax+b)$, $e^{ax+b}$, $\sin(ax+b)$, $\cos(ax+b)$ — never products. Parts begins at 9709 Paper 3.

### Cambridge 9231 (Further Maths)

Assumed from 9709 P3, then promoted from technique to **engine**: FP2's §2.4 builds **reduction formulae** on it — apply parts to a whole family $I_n$ and land a recurrence dropping $n$ by one or two rungs — and [[Reduction Formulae]] runs that machine on real Paper 2 questions, including the hinted-derivative variant where the paper hands you $\frac{d}{dx}[\ldots]$ instead of saying "integrate by parts". No FP2 question asks for a plain parts integral; it asks what parts can *build*.

### Edexcel IAL / OxAQA 9660

IAL names parts at **P4.6.2**, alongside substitution, with $\int \ln x \, dx$ the flagged standalone case (the "invisible 1" trick — differentiate the log, integrate the 1). OxAQA 9660 puts it at **P2.7**, glossed in the syllabus's own spirit as *the product rule reversed* — the honest genealogy, since parts is exactly the product rule read backwards and rearranged. Both expect the standard cases: $x^n e^{ax}$, $x^n \sin(ax)$, $x^n\cos(ax)$, $\ln x$, and the self-referential exponential-trig double round.

### IB AA HL

Parts is HL-only in AA (SL integrates by recognition and substitution). Same standard cases, plus **reduction formulas** as the HL extension — apply parts to a family like $\int x^n e^x \, dx$ to derive a recursive formula linking the $n$th integral to the $(n-1)$th:

$$I_n = \int x^n e^x \, dx = x^n e^x - n I_{n-1}.$$

Reduction formulas let you integrate $\int x^5 e^x \, dx$ without doing parts five times from scratch — you iterate the recurrence. The full machinery — why the ladder always reaches the ground, and what examiners do with it — is [[Reduction Formulae]].

### AP Calculus BC

Parts is a BC-only technique (not on AB). Expected cases: polynomial × exponential, polynomial × trig, $\ln x$ alone, $\tan^{-1} x$ alone, and the self-referential $e^x \sin x$ problem. The AP exam tends to bury parts inside a larger problem (area, volume of revolution) rather than asking for it in isolation.

> [!info] Beyond syllabus — the tabular method
> For $\int x^n e^{ax} \, dx$, the repeated parts can be organised into a table with alternating signs, differentiating $u$ down the left column and integrating $dv$ down the right. For $\int x^3 e^{2x} \, dx$:
>
> | Sign | $u$-column (differentiate) | $dv$-column (integrate) |
> |------|----------------------------|-------------------------|
> | $+$ | $x^3$ | $e^{2x}$ |
> | $-$ | $3x^2$ | $\tfrac{1}{2}e^{2x}$ |
> | $+$ | $6x$ | $\tfrac{1}{4}e^{2x}$ |
> | $-$ | $6$ | $\tfrac{1}{8}e^{2x}$ |
> | $+$ | $0$ | $\tfrac{1}{16}e^{2x}$ |
>
> Multiply along the diagonals and sum:
> $\int x^3 e^{2x} \, dx = \tfrac{1}{2}x^3 e^{2x} - \tfrac{3}{4}x^2 e^{2x} + \tfrac{3}{4} x e^{2x} - \tfrac{3}{8}e^{2x} + C.$
> Fast, visual, fewer sign errors — but only works cleanly when one column terminates (here, $x^n$ eventually hits 0).

### Beyond high school — University

In multivariable calculus and functional analysis, IBP generalises to **Green's identities** and the **divergence theorem** — the 2D and 3D analogues of the $uv\big|_a^b - \int v \, du$ formula. The boundary term $uv$ becomes a boundary integral over $\partial \Omega$, and the $\int v \, du$ becomes a volume integral. This is how integration by parts powers PDE theory: every weak formulation of a PDE pivots on a multidimensional IBP.

---

## Connections

- **Parent:** [[Integration]] — parts is the second of the two general techniques, alongside [[Integration by Substitution]].
- **Reverse of:** [[Product Rule]] — this card is the product rule run backwards, just as substitution is the chain rule in reverse.
- **Siblings:** [[Integration by Substitution]] (chain rule reversed); [[Partial Fractions]] (algebraic pre-processing, not a rule reversal).
- **Application:** [[Differential Equations]] — parts appears wherever an integrating factor leaves a product to integrate.
- **Extension:** Reduction formulas at IB HL / university — iterated IBP as a recurrence.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\displaystyle \int u \, dv = uv - \int v \, du$ | `\int u \, dv = uv - \int v \, du` | The IBP formula |
| $u = f(x)$, $dv = g'(x) dx$ | `u = f(x)`, `dv = g'(x) dx` | Assignment form |
| $du = f'(x) \, dx$ | `du = f'(x) \, dx` | Differential of $u$ |
| $v = \int dv$ | `v = \int dv` | Antiderivative of $dv$ |
| $\tan^{-1} x$ | `\tan^{-1} x` | Inverse tangent (arctan) |
| $\sin^{-1} x$ | `\sin^{-1} x` | Inverse sine (arcsin) |
| $I_n$ | `I_n` | Reduction-formula indexed integral |

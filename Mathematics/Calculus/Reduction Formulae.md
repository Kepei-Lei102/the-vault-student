---
chinese: 积分递推公式 (jīfēn dìtuī gōngshì)
prerequisites:
  - "[[Integration by Parts]]"
  - "[[Integration]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - syllabus/9231-2-4
  - type/technique
  - type/proof
  - notation/integral
  - misconception/forgetting-the-boundary-term
  - misconception/ladder-base-wrong
---

# Reduction Formulae 积分递推公式

> *Nobody integrates $\sin^{50}x$ by expanding it. Instead, one integration by parts builds a small machine — a formula that turns the* $n$ *problem into the* $n-2$ *problem — and then you feed the machine: $50$ becomes $48$, becomes $46$, … down to $\sin^0 x = 1$, which a child can integrate. Build the staircase once; walk it as many times as you like.*

## Definition

### Formal

Write $I_n$ for a definite integral whose integrand carries a power $n$, e.g. $I_n = \displaystyle\int_0^{\pi/2} \sin^n x \, dx$. A **reduction formula** is a recurrence expressing $I_n$ in terms of $I_{n-1}$ or $I_{n-2}$ (occasionally lower), such as

$$I_n = \frac{n-1}{n}\, I_{n-2}.$$

Together with the **base cases** ($I_0$, and $I_1$ if the step is $2$), the recurrence determines every $I_n$ — the integral is never computed directly for large $n$; it is *walked down to* a base case and the values climb back up.

### Intuitive

The power $n$ is the difficulty. Integration by parts is the only standard tool that can *lower a power while producing the same shape of integral again* — peel one factor off, differentiate what remains, and the debris reassembles into a smaller copy of the original problem. A reduction formula is that observation caught and written down as a machine. The mindset is the recursive one: **don't solve the big problem — relate it to a smaller version of itself, and solve the smallest one.**

### 中文锚点 (Chinese Anchor)

$\sin^{50}x$ 的积分没人硬算。**递推公式**的思路是：不直接求 $I_n$，而是用**分部积分**把 $I_n$ 和更低次的 $I_{n-2}$（或 $I_{n-1}$）挂上钩，得到一个递推关系，比如 $I_n = \frac{n-1}{n} I_{n-2}$。然后从 $n$ 一路降到 $I_0$ 或 $I_1$（这两个一眼就能积出来），再把数值一层层代回去。和数列的递推公式是同一个思想——**大问题化成小一号的同款问题**——只不过这里的"数列"每一项都是一个定积分。考试的两种问法都要会：**"推导"**（derive）——分部积分做一遍，把递推关系变出来，这是方法分所在；**"使用"**（use）——沿着梯子往下走，注意 $I_n \to I_{n-2}$ 是两级一跳，$n$ 的奇偶决定落在 $I_1$ 还是 $I_0$ 上。较难的题目可能会给提示（"考虑 $\frac{d}{dx}\big[x(1+x^5)^n\big]$"）：拿到提示就照做——求导、把高次幂拆开、两边积分，递推关系自己出现。

## The engine — how one integration by parts builds the machine

*Tool: [[Integration by Parts]], aimed so that the power drops and the shape survives.* The classic, worked in full — the syllabus's own first example, $I_n = \displaystyle\int_0^{\pi/2} \sin^n x \, dx$:

**Step 1 — peel one factor.** Write $\sin^n x = \sin^{n-1}x \cdot \sin x$ and integrate by parts with $u = \sin^{n-1}x$ (the power, to be differentiated down) and $dv = \sin x\,dx$ (one peeled factor, to be integrated):

$$I_n = \Big[-\sin^{n-1}x\cos x\Big]_0^{\pi/2} + (n-1)\int_0^{\pi/2} \sin^{n-2}x \cos^2 x \, dx.$$

**Step 2 — check the boundary term.** At $x = \frac{\pi}{2}$, $\cos x = 0$; at $x = 0$, $\sin^{n-1}x = 0$ (for $n \geq 2$). The bracket dies — as it very often does on well-chosen limits, which is precisely *why* examiners choose them.

**Step 3 — reassemble the debris into copies of $I$.** Trade $\cos^2 x = 1 - \sin^2 x$:

$$I_n = (n-1)\int_0^{\pi/2} \sin^{n-2}x\,dx - (n-1)\int_0^{\pi/2} \sin^{n}x\,dx = (n-1)I_{n-2} - (n-1)I_n.$$

**Step 4 — solve for $I_n$.** The "new" integral on the right *is the original* — gather it:

$$n I_n = (n-1) I_{n-2} \quad\Longrightarrow\quad \boxed{\ I_n = \frac{n-1}{n}\, I_{n-2}\ } \qquad (n \geq 2).$$

**Step 5 — walk the ladder.** Base cases $I_0 = \int_0^{\pi/2} 1\,dx = \frac{\pi}{2}$ and $I_1 = \int_0^{\pi/2}\sin x\,dx = 1$. Then, two rungs at a time:

$$I_5 = \tfrac{4}{5}I_3 = \tfrac{4}{5}\cdot\tfrac{2}{3}I_1 = \tfrac{8}{15}, \qquad I_6 = \tfrac{5}{6}\cdot\tfrac{3}{4}\cdot\tfrac{1}{2}\cdot\tfrac{\pi}{2} = \tfrac{15\pi}{96} = \tfrac{5\pi}{32}.$$

**Parity matters:** a step of $2$ means odd $n$ lands on $I_1$ and even $n$ lands on $I_0$ — reaching for the wrong base is the classic ladder slip. (These are the **Wallis integrals**; more on where they lead below.)

The same engine with a step of $1$ — the syllabus's second example, $I_n = \int_0^1 e^{-x}(1-x)^n dx$: parts with $u = (1-x)^n$, $dv = e^{-x}dx$ gives the boundary term $1$ (this time it *survives* — check it, don't assume it) and $I_n = 1 - nI_{n-1}$.

## Real case 1 — the hint-style question, and how to obey a hint

*A real Paper 2 question: $I_n = \displaystyle\int_0^1 (1+x^5)^n dx$. By considering $\dfrac{d}{dx}\Big[x\left(1+x^5\right)^n\Big]$, or otherwise, show that $(5n+1)\,I_n = 2^n + 5n\,I_{n-1}$. Hence find $I_3$.*

The syllabus warns that "in harder cases hints may be given" — and a hint is an instruction: **differentiate the thing, massage what appears, integrate both sides.**

*Tool: the product rule on the hinted object.*

$$\frac{d}{dx}\Big[x(1+x^5)^n\Big] = (1+x^5)^n + 5nx^5(1+x^5)^{n-1}.$$

*Tool: the power-splitting trade — write the loose $x^5$ as $(1+x^5) - 1$,* so every term becomes a clean power of $(1+x^5)$:

$$= (1+x^5)^n + 5n\left[(1+x^5) - 1\right](1+x^5)^{n-1} = (5n+1)(1+x^5)^n - 5n(1+x^5)^{n-1}.$$

*Tool: integrate both sides over $[0,1]$ — the left side is exact, that is the whole point of the hint.*

$$\Big[x(1+x^5)^n\Big]_0^1 = 2^n - 0 \quad\Longrightarrow\quad 2^n = (5n+1)I_n - 5n I_{n-1} \quad\Longrightarrow\quad (5n+1)I_n = 2^n + 5nI_{n-1}. \qquad\blacksquare$$

*Tool: walk the ladder — base first, then up.* $I_1 = \int_0^1(1 + x^5)dx = \left[x + \tfrac{x^6}{6}\right]_0^1 = \tfrac{7}{6}$. Then

$$11 I_2 = 2^2 + 10\cdot\tfrac{7}{6} \ \Rightarrow\ I_2 = \tfrac{47}{33}, \qquad 16 I_3 = 2^3 + 15\cdot\tfrac{47}{33} \ \Rightarrow\ I_3 = \tfrac{323}{176}.$$

(The mark scheme also accepts deriving the recurrence by integration by parts directly — the hint is a courtesy, not a cage. Numerical sanity: the integrand grows with $n$ on $(0,1]$, so $I_1 < I_2 < I_3$ must increase: $1.17 < 1.42 < 1.84$ ✓.)

## Real case 2 — the two-rung drop

*A real Paper 2 question: $I_n = \displaystyle\int_0^1 (1-x)^n \sinh x \, dx$. Show that, for $n \geq 2$, $\ I_n = -1 + n(n-1)\,I_{n-2}$.*

*Tool: integrate by parts twice — each pass differentiates the power once, and $\sinh \to \cosh \to \sinh$ returns the shape after two steps ([[Hyperbolic Functions]]).*

First pass ($u = (1-x)^n$, $dv = \sinh x\,dx$):

$$I_n = \Big[(1-x)^n \cosh x\Big]_0^1 + n\int_0^1 (1-x)^{n-1}\cosh x \, dx = -1 + n\int_0^1 (1-x)^{n-1}\cosh x\,dx$$

(boundary: the $x=1$ end dies through $(1-x)^n$; the $x=0$ end gives $-\cosh 0 = -1$). Second pass on the survivor ($u = (1-x)^{n-1}$, $dv = \cosh x\,dx$):

$$\int_0^1 (1-x)^{n-1}\cosh x\,dx = \Big[(1-x)^{n-1}\sinh x\Big]_0^1 + (n-1)\int_0^1 (1-x)^{n-2}\sinh x \, dx = 0 + (n-1)I_{n-2}$$

(this boundary term dies at *both* ends: $(1-x)^{n-1}$ kills $x=1$, $\sinh 0 = 0$ kills $x=0$ — needing $n \geq 2$ for the first kill, which is exactly why the question says $n \geq 2$). Substitute back:

$$I_n = -1 + n(n-1)\,I_{n-2}. \qquad\blacksquare$$

Note the shape of the mark scheme's demands across both cases: the recurrence is always **AG** (printed in the question), so the marks live in the visible route — the parts clearly set out, *each boundary term evaluated on the page*, the reassembly shown.

## Where this is the working tool

- **The factorial is a reduction formula wearing a gown.** $\Gamma(n+1) = \int_0^\infty x^n e^{-x}dx$ obeys — by exactly the integration by parts above — the recurrence $\Gamma(n+1) = n\,\Gamma(n)$, and with base $\Gamma(1) = 1$ that *is* $n!$. The Gamma function, which prices $\left(\frac12\right)! = \frac{\sqrt\pi}{2}$ and appears throughout statistics and physics, is the ladder of this topic run on an infinite interval.
- **The moments of the bell curve walk the same ladder.** For a standard normal variable, $E[X^n] = (n-1)\,E[X^{n-2}]$ — derived by the same peel-and-reassemble parts — giving $E[X^2] = 1$, $E[X^4] = 3$, $E[X^6] = 15$ and, for odd $n$, $0$. Every kurtosis calculation and every "fourth-moment" condition in statistics is a reduction formula cashed.
- **Wallis's ladder computes $\pi$.** Comparing $I_{2n}$ and $I_{2n+1}$ from the $\sin^n$ ladder squeezes out $\ \frac{\pi}{2} = \frac{2\cdot2\cdot4\cdot4\cdot6\cdots}{1\cdot3\cdot3\cdot5\cdot5\cdots}$ — the Wallis product (1656), the first infinite product for $\pi$, and a direct ancestor of how $\pi$ reaches the Gaussian integral $\int e^{-x^2}dx = \sqrt\pi$ at the heart of the normal distribution.

## Common Misconceptions (Teaching Notes)

### 1. The boundary term assumed dead

$\left[uv\right]$ evaluated lazily as $0$ because "it usually is". In the Wallis case it dies; in $\int_0^1 e^{-x}(1-x)^n dx$ it is $1$; in Real case 2 the first pass leaves $-1$ and the second leaves $0$. The recurrences differ *precisely* in their boundary terms.

**Fix:** evaluate $\left[uv\right]$ at both limits, on the page, every pass — it is usually where one of the A marks lives, and always where the constant in the recurrence comes from.

### 2. Wrong rung at the bottom

Using $I_0$ as the base for an odd $n$ on a two-step ladder (or vice versa), silently shifting every value.

**Fix:** before walking, say the parity out loud: step size $2$ + odd $n$ → lands on $I_1$; even $n$ → $I_0$. Then check the final value's plausibility against the integrand (positive? increasing in $n$? less than the interval length?).

### 3. Deriving the recurrence for general $n$, applying it below its floor

$I_n = -1 + n(n-1)I_{n-2}$ was proved *for $n \geq 2$* — the derivation's second boundary kill needed it. Applying a recurrence at $n = 1$ when its proof assumed $n \geq 2$ is an algebra-legal, calculus-illegal move.

**Fix:** the recurrence's floor is set by the derivation (which power had to stay positive to kill a boundary term); note it when deriving, respect it when walking.

### 4. Treating the hint as decoration

Given "*by considering $\frac{d}{dx}[\ldots]$*", students derive by parts from scratch, burn ten minutes, and tangle signs. The hint is the marker's own route: differentiate the object, split the stray power ($x^5 = (1+x^5) - 1$ is the standard trade), integrate both sides.

**Fix:** practise the hint-protocol as its own three-step skill; the "or otherwise" is real but rarely faster.

## Exam Notes

### Cambridge 9231 (Further Pure 2, Paper 2 — §2.4)

- Both syllabus verbs are examined: **derive** (the parts route or the hinted-derivative route — AG, marks in the route) and **use** (walk the ladder to a numerical value; recent schemes award one mark per rung, with the base case earning its own B1).
- The syllabus's own named examples are the shapes to drill: $\int_0^{\pi/2}\sin^n x\,dx$, $\int_0^1 e^{-x}(1-x)^n dx$, and hinted cases in the $\frac{d}{dx}\left(\tan x \sec^n x\right)$ style.
- **MF19 gives no reduction formulae** — but it does give the parts formula itself, and the base-case integrals are elementary. The skill is the route, and the route is not on the sheet.

### Edexcel IAL (Further Pure 3 — WFM03, §4.5)

"The derivation and use of simple reduction formulae", with the spec's own example $nI_n = (n-1)I_{n-2}$ — the Wallis shape. Same skill, same marks-in-the-route culture.

### Where it is *not* examined

Not on Cambridge 9709 (integration by parts appears in P3, but never iterated into recurrences), not on OxAQA 9660, not in IB AA/AI at either level, not on AP Calculus (BC iterates parts numerically but names no reduction formulae). A Further-Mathematics marker once again.

## Connections

- **Parent:** [[Integration by Parts]] — the engine; a reduction formula is IBP caught in a loop and written as a machine.
- **Kinship:** [[Proof by Induction]] and [[Stacks and Queues]]' recursive spirit — relate the size-$n$ problem to size-$n-2$, solve the base: the recursive decomposition, here wearing integral clothing.
- **Application:** [[Probability Generating Functions]] and the normal distribution's moments — statistics walks these ladders; the Gamma-function recurrence prices the factorial.
- **Supplier:** [[Hyperbolic Functions]] — $\sinh \to \cosh \to \sinh$ is what makes two-pass parts return the original shape in Real case 2.
- **For 9231 students:** [[MF19 Reference (9231)]] — no reduction formulae on the sheet; the parts formula is.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $I_n$ | `I_n` | the indexed integral |
| $\displaystyle\int_0^{\pi/2}\sin^n x\,dx$ | `\int_0^{\pi/2}\sin^n x\,dx` | the Wallis integral |
| $\Big[uv\Big]_0^1$ | `\Big[uv\Big]_0^1` | the boundary term — evaluate it, always |
| $\dfrac{d}{dx}\Big[x(1+x^5)^n\Big]$ | `\frac{d}{dx}\Big[x(1+x^5)^n\Big]` | the hinted object |
| $\Gamma(n+1) = n\,\Gamma(n)$ | `\Gamma(n+1) = n\,\Gamma(n)` | the factorial's own reduction formula |

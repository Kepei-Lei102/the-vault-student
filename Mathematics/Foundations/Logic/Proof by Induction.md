---
chinese: 数学归纳法 (shùxué guīnàfǎ)
prerequisites:
  - "[[Logic]]"
  - "[[Sequences]]"
  - "[[Algebraic Proof]]"
leads_to:
  - "[[Summation of Series]]"
  - "[[Recursion]]"
  - "[[Natural Numbers]]"
tags:
  - subject/mathematics
  - domain/logic
  - level/A-Level
  - curriculum/Cambridge-9231
  - syllabus/9231-1-7
  - curriculum/A-Level
  - curriculum/IB-AA
  - type/proof
  - type/methodology
  - notation/sigma
  - misconception/pattern-is-not-proof
  - misconception/assuming-what-you-prove
  - misconception/missing-base-case
  - misconception/broken-middle-step
  - misconception/backwards-induction-step
---

# Proof by Induction 数学归纳法

> *A claim "for all $n$" is infinitely many claims wearing one sentence. You can verify a thousand of them and the thousand-and-first can still betray you — checking is sampling, and no sample covers infinity. The hunter's move is different: stop checking cases and start tracing the **causality between them**. Prove, once, that each case forces the next. Then push the first. Infinity falls like dominoes — not because you visited every one, but because you built the law that carries the fall from each to its neighbour.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| proof by (mathematical) induction | 数学归纳法 | the two-pillar proof: first case + each-forces-next |
| base case | （归纳）奠基 | verify the claim at the starting value |
| inductive hypothesis | 归纳假设 | assume the claim at one value $k$ |
| inductive step | 归纳递推 | prove the claim passes from $k$ to $k+1$ |
| conjecture | 猜想 | the formula you guess before you prove |
| recurrence relation | 递推关系 | a sequence defined by "next from current" |
| strong induction | 强归纳法 | assume *all* cases up to $k$, not just $k$ |

> [!info] The name is a historical accident
> In science and philosophy, *induction* means generalising from examples — the sun rose every day so far, so it will rise tomorrow — and it can be **wrong**. Mathematical induction, despite the name, is not that: it is airtight **deduction** (演绎), an infinite chain of modus ponens financed by one theorem. Chinese textbooks keep the distinction visible — 不完全归纳法 (incomplete induction: pattern-guessing, inadmissible as proof) versus 数学归纳法 (this card: a complete, rigorous method). English hides the difference in one overloaded word; don't let the word fool you about the rigour.

## The problem, before the tool

Watch a pattern seduce. Put $n$ points on a circle, join every pair with a chord, and count the regions:

$$1,\ 2,\ 4,\ 8,\ 16,\ \ldots$$

Doubling, obviously: $2^{n-1}$. Then $n = 6$ arrives and the count is $\boxed{31}$. Not 32 — the pattern held five times and then simply wasn't the law.

![[moser-circle-betrayal.mp4]]

There is even a trap inside the trap. The points must be in **general position** — no three chords crossing at one spot — and a *regular* hexagon fails that test: its three long diagonals all meet at the centre, fusing regions that should have stayed apart, and the count comes to 30. The most symmetric arrangement, the one a student would draw first, doesn't even give the right counterexample.

Fermat fell into the same seduction with grander stakes: $2^{2^n}+1$ gives primes for $n = 0, 1, 2, 3, 4$ (3, 5, 17, 257, 65537), and Fermat conjectured it always would. Euler factorised the very next one: $2^{32}+1 = 641 \times 6700417$.

The lesson is not "check more cases." *No* number of checks proves a claim about all $n$ — the unchecked cases always outnumber the checked ones, infinitely to finitely. A universal statement over the integers needs a fundamentally different kind of argument: one that covers infinitely many cases with **finitely many sentences**. There is exactly one standard machine for this, and it works by proving not the cases, but the *link between* them.

> [!tip] Watch: the seduction, sung
> Grant Sanderson (3Blue1Brown) wrote a parody of Leonard Cohen's *Hallelujah* about precisely this — patterns that dress up as laws — and performed it live at Matt Parker's *An Evening of Unnecessary Detail* in London. The circle-and-chords count above is one of the traps it sings; integrals and prime-counting patterns are others.
>
> - **Bilibili (in China)**: [bilibili.com/video/BV1hg4y1A7pf](https://www.bilibili.com/video/BV1hg4y1A7pf/) — 《哈~被骗啦》, 官方双语字幕
> - **YouTube**: [youtu.be/NOCsdhzo6Jg](https://youtu.be/NOCsdhzo6Jg) — *"How They Fool Ya (live) | Math parody of Hallelujah"* by 3Blue1Brown, 2023.

## The tool — two pillars

To prove a statement $P(n)$ for every integer $n \geq n_0$:

1. **Base case 奠基:** prove $P(n_0)$ — the claim holds at the start.
2. **Inductive step 递推:** prove that **for every** $k \geq n_0$, $\ P(k) \Rightarrow P(k+1)$ — *if* the claim holds at any one value, it must hold at the next.

Then $P(n)$ holds for all $n \geq n_0$. That's the whole machine. In the logical notation of [[Logic]]:

$$P(n_0) \ \land\ \bigl(\forall k \geq n_0,\ P(k) \Rightarrow P(k+1)\bigr) \ \implies\ \forall n \geq n_0,\ P(n)$$

The domino picture is exact, not decorative: pillar 1 pushes the first domino; pillar 2 guarantees every domino is close enough to knock over its neighbour. Neither pillar works alone:

![[induction-dominoes.svg|700]]

- **A flawless step with no base is worthless.** Try to "prove" $n = n+1$: assume $k = k+1$, add 1 to both sides, $k+1 = k+2$ — the step is perfect. The dominoes are impeccably spaced and nothing ever falls, because nothing was ever pushed. A relay with no baton.
- **A base with one cracked step is worse — it *looks* like it works.** The classic: "all horses are the same colour." Base: one horse, one colour ✓. Step: take $k+1$ horses; horses $1..k$ share a colour (hypothesis), horses $2..k{+}1$ share a colour (hypothesis again), and the overlap $2..k$ forces the two colours equal. Convincing — except at $k = 1 \to 2$: two horses, and the "overlap" $2..1$ is **empty**. Nothing links the two one-horse sets. One gap, at one $k$, and everything downstream of it is unproven. The step must survive at *every* $k$ in range, and the smallest $k$ is where cracks hide.

![[proof-by-induction-dominoes.mp4]]

## Why it works — one level closer

Why is this *valid*? Because of what the integers **are**. Every integer $n \geq n_0$ is reachable from $n_0$ by finitely many $+1$ steps — that is not a theorem about the integers so much as the *definition* of them ([[Natural Numbers]]: Peano made "induction works" one of the axioms that pin down what "natural number" means). The inductive step is a relay theorem proved once, then invoked along the exact route by which every integer is built: $P(5)$ holds because $P(4) \Rightarrow P(5)$, because $P(3) \Rightarrow P(4)$, … down a *finite* chain to the base. Induction is infinitely many modus ponens for the price of one implication.

There is a second lens, and it is a [[Proof by Contradiction]] worth doing slowly. Rephrase the claim as "if both pillars hold, then no counterexample exists," and name the negation explicitly: *a counterexample exists.*

1. Suppose some values $\geq n_0$ falsify $P$. Every non-empty set of integers bounded below has a **least** element — so there is a *smallest* failure, $m$. (The minimal criminal.)
2. $m \neq n_0$, because the base case checked $P(n_0)$ directly.
3. So $m - 1 \geq n_0$, and since $m$ is the *smallest* criminal, $P(m-1)$ is **true**.
4. The inductive step at $k = m-1$ now fires: $P(m-1) \Rightarrow P(m)$. So $P(m)$ is true — but $m$ was a failure. Contradiction; no counterexample exists. $\blacksquare$

The two lenses are equivalent (induction ⇔ the well-ordering of the integers), and the second explains the *feel* of the method: induction is a machine that makes the smallest counterexample impossible.

## The grammar of the write-up — four movements

Exam induction proofs are marked on structure, and the structure is always the same four movements.

1. **Base.** Verify $P(n_0)$ honestly — compute *both* sides and show they agree. (One line; one mark; still droppable.)
2. **Hypothesis.** "*Assume $P(k)$ holds for some integer $k \geq n_0$*" — and write out what $P(k)$ says. The word is **some**, never *all*: you are standing on one rung, not claiming the ladder.
3. **Step.** Prove $P(k+1)$, and every route runs through the same discipline: **make the $k$-shape appear.** Engineer the $(k{+}1)$-expression until the exact expression named in your hypothesis is visible, cash the hypothesis, then finish the algebra toward the target. Each family has its standard opening move — *peel the last term* (sums), *peel one factor* (powers, matrices), *rewrite $f(k+1)$ in terms of $f(k)$* (divisibility), *apply the recurrence, then the hypothesis* (sequences). The worked examples name them all.
4. **Conclusion — the ritual sentence, citing both pillars.** "*Since $P(n_0)$ is true, and $P(k) \Rightarrow P(k+1)$ for all $k \geq n_0$, by mathematical induction $P(n)$ is true for all integers $n \geq n_0$.*" This is not decoration: it is the statement of the theorem you just invoked, and a mark rides on naming both premises. "So it's true" earns nothing.

## Worked examples — every tool named

### Example 1 (sums): $\displaystyle\sum_{r=1}^{n} r^3 = \tfrac{1}{4}n^2(n+1)^2$

**Base** $n=1$: LHS $= 1^3 = 1$; RHS $= \tfrac{1}{4}(1)(4) = 1$ ✓.

**Hypothesis:** assume $\sum_{r=1}^{k} r^3 = \tfrac{1}{4}k^2(k+1)^2$ for some integer $k \geq 1$.

**Step** — *Tool: peel the last term — a sum to $k+1$ is the sum to $k$ plus one term.*

$$\sum_{r=1}^{k+1} r^3 = \underbrace{\tfrac{1}{4}k^2(k+1)^2}_{\text{hypothesis, cashed}} + (k+1)^3 = \tfrac{1}{4}(k+1)^2\bigl[k^2 + 4(k+1)\bigr] = \tfrac{1}{4}(k+1)^2(k+2)^2$$

which is the target with $n = k+1$ (note $k^2+4k+4 = (k+2)^2$). ✓

**Conclusion:** $P(1)$ holds and $P(k) \Rightarrow P(k+1)$ for all $k \geq 1$; by mathematical induction the result holds for all integers $n \geq 1$. $\blacksquare$

*The factoring habit:* pull out the common factor $\tfrac14(k+1)^2$ **before** expanding anything. Expanding everything into a quartic and re-factoring is the long way round and the main source of slips. And notice what was proved: $\tfrac14 n^2(n+1)^2 = \left(\tfrac{n(n+1)}{2}\right)^2$ — *the sum of the first $n$ cubes is the square of the sum of the first $n$ integers.* That coincidence has been startling people since Nicomachus, ~100 CE.

### Example 2 (conjecture, then prove): $u_1 = 1,\ u_{n+1} = 3u_n - 1$

Find and prove a formula for $u_n$. First, hunt: $u_1..u_5 = 1,\ 2,\ 5,\ 14,\ 41$.

*Tool: forward reading for the invariant — stare until something is constant.* The terms triple-ish; test the tripling honestly: $2u_n - 1$ gives $1,\ 3,\ 9,\ 27,\ 81$ — exact powers. So conjecture

$$2u_n - 1 = 3^{n-1} \quad\text{i.e.}\quad u_n = \tfrac{1}{2}\bigl(1 + 3^{n-1}\bigr).$$

A conjecture from five cases is worth nothing yet (Moser's circle held for five cases too) — now the proof.

**Base** $n=1$: $\tfrac12(1 + 3^0) = 1 = u_1$ ✓.

**Hypothesis:** $u_k = \tfrac12(1 + 3^{k-1})$ for some $k \geq 1$.

**Step** — *Tool: apply the recurrence, then cash the hypothesis.*

$$u_{k+1} = 3u_k - 1 = 3 \cdot \tfrac12\bigl(1 + 3^{k-1}\bigr) - 1 = \tfrac32 + \tfrac12 \cdot 3^{k} - 1 = \tfrac12\bigl(1 + 3^{k}\bigr)$$

which is the formula at $n = k+1$. ✓ Conclusion sentence as always. $\blacksquare$

This example is the syllabus's two skills welded: *conjecture from a limited trial* (the hunt), then *establish by induction* (the proof). Keep the two phases separate on paper — the examiner wants to see that you know which one is evidence and which one is proof.

### Example 3 (matrix powers): $M = \begin{pmatrix} 4 & -1 \\ 6 & -1 \end{pmatrix}$

Prove that for every positive integer $n$: $\ M^n = \begin{pmatrix} 3 \cdot 2^n - 2 & 1 - 2^n \\ 6 \cdot 2^n - 6 & 3 - 2^{n+1} \end{pmatrix}$.

**Base** $n=1$: $\begin{pmatrix} 6-2 & 1-2 \\ 12-6 & 3-4 \end{pmatrix} = \begin{pmatrix} 4 & -1 \\ 6 & -1 \end{pmatrix} = M$ ✓.

**Hypothesis:** the formula holds at some $k \geq 1$.

**Step** — *Tool: peel one factor — $M^{k+1} = M \cdot M^k$, then cash the hypothesis on $M^k$.*

$$M^{k+1} = \begin{pmatrix} 4 & -1 \\ 6 & -1 \end{pmatrix}\begin{pmatrix} 3 \cdot 2^k - 2 & 1 - 2^k \\ 6 \cdot 2^k - 6 & 3 - 2^{k+1} \end{pmatrix}$$

Entry by entry (watch the arithmetic — this is where the marks leak):

- top-left: $4(3 \cdot 2^k - 2) - (6 \cdot 2^k - 6) = 6 \cdot 2^k - 2 = 3 \cdot 2^{k+1} - 2$ ✓
- top-right: $4(1 - 2^k) - (3 - 2^{k+1}) = 1 - 2 \cdot 2^k = 1 - 2^{k+1}$ ✓
- bottom-left: $6(3 \cdot 2^k - 2) - (6 \cdot 2^k - 6) = 12 \cdot 2^k - 6 = 6 \cdot 2^{k+1} - 6$ ✓
- bottom-right: $6(1 - 2^k) - (3 - 2^{k+1}) = 3 - 4 \cdot 2^k = 3 - 2^{(k+1)+1}$ ✓

All four entries match the target at $n = k+1$. Conclusion sentence. $\blacksquare$

($M^{k+1} = M^k \cdot M$ works equally well — peel on whichever side you prefer, but peel *consistently*. And the shapes inside the answer are not random: the constants and the $2^n$-parts are the matrix's two eigenvalues, $1$ and $2$, showing through — machinery at [[Eigenvalues and Eigenvectors]].)

### Example 4 (divisibility): $f(n) = 3^{2n} + 2 \cdot 5^n - 3$ is divisible by 8

**Base** $n=1$: $f(1) = 9 + 10 - 3 = 16 = 8 \times 2$ ✓.

**Hypothesis:** $f(k) = 8m$ for some integer $m$, for some $k \geq 1$.

**Step** — *Tool: rewrite $f(k+1)$ as (multiple of $f(k)$) + (visibly-divisible remainder). Choose the multiplier to kill the fastest-growing term.*

$$f(k+1) = 3^{2k+2} + 2 \cdot 5^{k+1} - 3 = 9 \cdot 3^{2k} + 10 \cdot 5^k - 3$$

The $3^{2k}$ term grows by a factor 9 each step, so compare against $9f(k) = 9 \cdot 3^{2k} + 18 \cdot 5^k - 27$:

$$f(k+1) - 9f(k) = -8 \cdot 5^k + 24 \qquad\Longrightarrow\qquad f(k+1) = 9f(k) - 8\bigl(5^k - 3\bigr) = 8\bigl(9m - 5^k + 3\bigr)$$

a multiple of 8. ✓ Conclusion sentence. $\blacksquare$

*Why the multiplier trick is the tool and not a fluke:* subtracting $9f(k)$ cancels the $3^{2k}$ term **exactly**, and everything that survives must then be checked for divisibility by hand ($10 - 18 = -8$ ✓, $-3 + 27 = 24$ ✓). If the survivors *aren't* all divisible, you picked the wrong multiplier (try the other growth factor) — or the claim is false, which the base case would usually have caught.

### Example 5 (the dominoes can start anywhere): $2^n > n^2$ for all integers $n \geq 5$

Check small cases and watch the claim stumble: $2^1 > 1$ ✓ — but then $2^2 = 4 = 4$, $2^3 = 8 < 9$, $2^4 = 16 = 16$, none of them $>$. An isolated truth at $n=1$ with three failures right after it: a domino that falls into a gap relays nothing. Truth settles in for good at $n = 5$, so that is where the base goes. A base case is not always $n=1$; it sits wherever the claim *stays* true.

**Base** $n=5$: $32 > 25$ ✓.

**Hypothesis:** $2^k > k^2$ for some $k \geq 5$.

**Step** — *Tool: relay through an intermediate bound — chain $2^{k+1} > 2k^2 \geq (k+1)^2$.*

$$2^{k+1} = 2 \cdot 2^k > 2k^2, \qquad\text{and}\qquad 2k^2 - (k+1)^2 = k^2 - 2k - 1 = (k-1)^2 - 2 > 0 \ \text{ for } k \geq 3.$$

So $2^{k+1} > (k+1)^2$. ✓ Conclusion, for all $n \geq 5$. $\blacksquare$

A subtlety worth savouring: the step is valid from $k \geq 3$, yet the claim is false at $n = 3$ and $4$. No contradiction — $P(3) \Rightarrow P(4)$ is vacuously true because $P(3)$ is false ([[Logic]]'s umbrella promise on a sunny day). A working relay cannot rescue dominoes that were never standing. **The base case decides where truth *enters* the chain; the step only carries it forward from there.**

### Example 6 (the rule you have already used ten thousand times)

> Prove that $\dfrac{d}{dx}\left(x^n\right) = nx^{n-1}$ for every positive integer $n$.

Look at what is being claimed before proving it. This is the **power rule** — the first thing anyone learns to differentiate, and the workhorse of every calculus question you have ever answered. It is not one statement but an infinite family of them ($x^2 \to 2x$, $x^3 \to 3x^2$, $x^{47} \to 47x^{46}$, …), which means it needs exactly the machine on this card.

**Base** $n = 1$: $\dfrac{d}{dx}(x) = 1 = 1 \cdot x^{0}$ ✓.

**Hypothesis:** $\dfrac{d}{dx}\left(x^k\right) = kx^{k-1}$ for some integer $k \geq 1$.

**Step** — *Tool: peel one factor, then differentiate the product.* Write $x^{k+1} = x \cdot x^{k}$ and apply the [[Product Rule|product rule]]:

$$\frac{d}{dx}\left(x^{k+1}\right) = \frac{d}{dx}(x) \cdot x^{k} + x \cdot \frac{d}{dx}\left(x^{k}\right) = 1 \cdot x^{k} + x \cdot \underbrace{kx^{k-1}}_{\text{hypothesis, cashed}} = x^{k} + kx^{k} = (k+1)x^{k}$$

which is the rule at $n = k+1$. ✓ Conclusion sentence as always. $\blacksquare$

Three lines. **The most-used theorem in your mathematical life stands on one base case, one product rule, and this card** — and on nothing else, because the product rule is proved straight from the limit definition and never quietly borrows the power rule. ([[Power Rule]] takes the other standard road, first principles with the binomial expansion of $(x+h)^n$; that road is equally honest and needs the [[Binomial Theorem]] — whose own standard proof is an induction, on Pascal's rule. Both roads to the power rule cross this bridge.)

## Common Misconceptions (Teaching Notes)

### 1. "You're assuming the thing you're trying to prove"

The hypothesis assumes $P$ at **one** value $k$; the conclusion asserts $P$ at **all** values. Those are different statements — local versus global. **Fix:** point at [[Logic]]'s proof skeletons: to prove any implication "$A \Rightarrow B$" you *begin by assuming $A$* — that is not circularity, it is what proving an implication means. The step proves only the relay "$k$ forces $k+1$"; the base is what injects an actual truth for the relay to carry.

### 2. "It holds for $n = 1$ to $5$, so it's proved"

Moser's circle held to $n=5$ and failed at 6; Fermat's primes held to $n=4$ and failed at 5. Five cases — or five million — are conjecture fuel, never proof. **Fix:** keep the two phases ritually separate (Example 2): *hunt* (compute, spot, conjecture), then *prove* (the four movements). The base case is not evidence; it is ignition.

### 3. Skipping the base "because it's obvious"

The step of $n = n+1$ is flawless, and the claim is absurd — the base case is the *only* thing standing between you and it. **Fix:** the base is one honest line (both sides computed) and it is load-bearing, not ceremonial. Write it first, every time, at the value where the claim starts (which Example 5 shows need not be 1).

### 4. A step that quietly fails at one $k$

"All horses are the same colour" has a true base and a step that works for every $k \geq 2$ — and is garbage, because the step breaks at exactly $k = 1 \to 2$, where the two overlapping sets don't overlap. **Fix:** test the step's argument at the *smallest* $k$ it must serve. If the argument mentions an overlap, a middle element, or "the other $k-1$" — smallest-$k$ is where it cracks.

### 5. Writing the step backwards

Starting from the target equality at $k+1$ and manipulating both sides until something true appears proves nothing unless every move is reversible — you've shown *target ⇒ truth*, the converse of what's needed ([[Logic]]'s converse trap wearing algebra). **Fix:** scratch-paper backwards is fine for *finding* the route; the written proof travels forwards — start from the $(k{+}1)$-expression or the hypothesis, and *arrive* at the target. If you catch yourself writing the target on line one of the step, stop and invert.

## Exam Notes

### Cambridge 9231 — Further Pure 1, §1.7

- **The named contexts are exactly this card's Examples 1–4** — the syllabus's own illustrations are $\sum r^3 = \tfrac14 n^2(n+1)^2$, the recurrence $u_{n+1} = 3u_n - 1$ with $u_n = \tfrac12(1+3^{n-1})$, the matrix $\begin{pmatrix} 4 & -1 \\ 6 & -1 \end{pmatrix}^n$, and divisibility of $3^{2n} + 2 \cdot 5^n - 3$ by 8. Sums, sequences, matrix powers, divisibility: four costumes, one four-movement grammar.
- The second learning objective is **conjecture-then-prove**: "recognise situations where conjecture based on a limited trial followed by inductive proof is a useful strategy" — Example 2's two-phase discipline. Show the trial, state the conjecture cleanly, then prove it as if it had been given.
- Mark-scheme shape: the base earns its point only with both sides evaluated; the step carries most marks and **must visibly use the hypothesis** (an induction proof that never cashes $P(k)$ scores as no induction at all); the closing statement must cite *both* pillars — base true, step valid for all $k$ — to collect the final mark.
- You are almost always proving a **given** result — the destination is printed on the paper. The marks are in the journey; if your algebra doesn't land exactly on the target, hunt the slip rather than massaging the last line.
- Induction returns in **FP2 §2.5**: de Moivre's theorem for positive integer exponents is proved by induction — the proof already lives at [[Euler's Formula and De Moivre's Theorem]].

### Cambridge 9709

- **Not examined.** Proof by induction belongs to Further Mathematics; the 9709 papers never ask it. (Worth saying out loud: students who've seen it elsewhere sometimes spend ten 9709 minutes inducting where a direct argument was wanted.)

### IB AA HL

- Topic 1 (Number & Algebra), **HL only**: proof by induction is a named skill, examined alongside proof by contradiction and counterexample. Favourite costumes: sums, divisibility, and inequalities (Example 5's kind), occasionally derivatives ($\tfrac{d^n}{dx^n}$ of a product — conjecture from the first few, then induct). SL sees none of it.

### A-Level Further Mathematics (UK boards)

- Edexcel (Core Pure 1), AQA, OCR: induction opens the Further Pure sequence with the same quartet — series sums, divisibility, matrix powers — and the same conclusion-sentence discipline. The grammar of this card transfers verbatim.

### IGCSE / AP

- **0580 / 0606 / 9260:** not examined; the nearest shadow is "explain why" pattern questions — where *incomplete* induction is exactly the trap (Misconception 2).
- **AP Calculus:** not examined. First appears at university (discrete mathematics, analysis) — where it is assumed fluent from day one; this card is the whole preparation.

## Beyond the syllabus

> [!info] Patterns that break late — why "I checked a lot of cases" is never enough
> Moser's circle breaks at $n = 6$ and Fermat's primes at $n = 5$, which is almost polite of them. Mathematics keeps far worse. The **Borwein integrals** are a chain of innocent-looking integrals whose first seven come out to exactly $\pi/2$ — and the eighth misses by about $2.3 \times 10^{-11}$, a discrepancy any numerical check would file under rounding error. **Pólya's conjecture** (1919), on whether most numbers below $n$ have an odd number of prime factors, survived every check anyone could run for forty years; its smallest counterexample is $n = 906{,}150{,}257$. You could verify a claim a billion times, be wrong, and never once suspect it. Verification is a finite sample of an infinite claim — the two pillars are cheaper *and* stronger.

> [!info] Strong induction — the dominoes lean on everyone behind them
> Recall the hypothesis assumed $P$ at *one* value $k$. **Strong induction** assumes it at **every** value from $n_0$ up to $k$ — and with that heavier hypothesis, proves $P(k+1)$. The showpiece: *every integer $\geq 2$ is a product of primes.* Take $n$: if it's prime, done; if not, $n = ab$ with $2 \leq a, b < n$ — and the strong hypothesis covers **both** factors at once (ordinary induction, holding only $P(k)$, couldn't touch them). That is the existence half of the fundamental theorem of arithmetic — [[Prime Numbers]]. Despite the extra muscle, strong induction is exactly as strong as the ordinary kind: apply ordinary induction to $Q(k) =$ "$P(n_0)$ and … and $P(k)$" and the two become one theorem in different clothes.

> [!info] Structural induction — CS runs on this card
> Recall that induction climbs $\mathbb{N}$ along the $+1$ steps every integer is built from. But *any* recursively built world supports the same argument: prove the claim for the atoms, prove each construction rule preserves it, and the claim holds for everything constructible. That is **structural induction** — induction on shape rather than size — and it is how one proves facts about [[Recursion]] (a recursive function's correctness proof *is* an induction on its argument — the twin claim, made from the other side), about [[Binary Trees]] (every non-empty tree has one more node than edge), about every grammar written in BNF ([[Compilers and Interpreters]]). When a computer scientist says "by induction on the structure of the tree," this card is what they mean.

> [!info] The axiom at the bottom — and the edge of the method
> Why does the relay argument get to call itself an *axiom*-grade truth? Peano's answer: it doesn't rest on anything deeper — **induction is one of the axioms that define $\mathbb{N}$** ([[Natural Numbers]]). "The naturals are exactly what induction reaches" is the fence that keeps out rogue numbers sitting beyond every finite chain of $+1$s. And the fence has a famous gate: **Goodstein's theorem**, a concrete statement about ordinary integers, is *true* but *unprovable* from Peano's axioms — proving it requires induction along orderings longer than $\mathbb{N}$ itself (transfinite induction). It is the concrete face of [[Gödel's Incompleteness Theorems]]: the method of this card proves essentially everything you will meet for years, and the exceptions are landmarks of logic, not potholes.

## Connections

- **Builds on:** [[Logic]] — the step is an implication proved the way implications are proved, the whole method is chained modus ponens, and Example 5's vacuous-truth subtlety is Logic's umbrella promise; [[Sequences]] — recurrences supply the conjecture-then-prove habitat, and this card is the cure for the pattern-spotting trap that card warns about.
- **Leads to:** [[Summation of Series]] — the standard results $\sum r, \sum r^2, \sum r^3$ this method certifies; [[Recursion]] — induction made executable: same base, same step, computing instead of proving; [[Natural Numbers]] — induction promoted from method to axiom.
- **Proof in the wild:** [[Power Rule]] — the rule every calculus student uses daily, in three lines (Example 6); [[Euler's Formula and De Moivre's Theorem]] — de Moivre for integer $n$, proved by induction; [[Binomial Theorem]] — the classic inductive proof via Pascal's rule, and the other road to the power rule.
- **Proof ingredient:** [[Product Rule]] — proved from first principles, so the inductive step of Example 6 borrows nothing it is trying to prove.
- **Kindred:** [[Matrix]] — the multiplication engine under Example 3; [[Eigenvalues and Eigenvectors]] — why Example 3's answer is built from $1^n$ and $2^n$; [[Proof by Contradiction]] — the minimal-criminal lens; [[Chain of Thought]] — where induction sits among the proof structures; [[Gödel's Incompleteness Theorems]] — the method's outer edge.
- **For 9231 students:** the standard sums $\sum r$, $\sum r^2$, $\sum r^3$ are *printed* in MF19's Further Pure list — the exam hands you the destination because the marks are in the journey. (Booklet-wide audit: [[MF19 Reference (9709)]].)

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $P(k) \Rightarrow P(k+1)$ | `P(k) \Rightarrow P(k+1)` | the inductive step |
| $\displaystyle\sum_{r=1}^{n} r^3$ | `\sum_{r=1}^{n} r^3` | sums with explicit limits |
| $\forall k \geq n_0$ | `\forall k \geq n_0` | "for every $k$ from the base up" |
| $\blacksquare$ | `\blacksquare` | end of proof |
| $u_{k+1} = 3u_k - 1$ | `u_{k+1} = 3u_k - 1` | recurrence relations |

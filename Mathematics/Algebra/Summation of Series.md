---
chinese: 级数求和 (jíshù qiúhé)
prerequisites:
  - "[[Sequences]]"
  - "[[Partial Fractions]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Proof by Induction]]"
  - "[[Limit]]"
leads_to:
  - "[[Maclaurin Series]]"
  - "[[De Moivre at Work]]"
  - "[[Bounding Sums with Integrals]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - curriculum/A-Level
  - curriculum/Cambridge-9231
  - syllabus/9231-1-3
  - type/deep
  - type/theorem
  - type/proof
  - notation/sigma
  - misconception/two-different-difference-methods
  - misconception/shrinking-terms-mean-convergence
  - misconception/cancel-without-counting-the-gap
  - misconception/sigma-is-multiplicative
  - misconception/standard-results-are-axioms
---

# Summation of Series 级数求和

> *Adding the first hundred whole numbers is a party trick: pair them off, $1+100$, $2+99$, and a schoolboy Gauss is done before the chalk is down. Now add the first hundred terms of*
> $$\frac{1}{1\cdot2\cdot3} + \frac{1}{2\cdot3\cdot4} + \frac{1}{3\cdot4\cdot5} + \cdots$$
> *No pairing helps. There is no common difference and no common ratio. And yet the total takes one line — because the right rewrite makes ninety-nine of those hundred terms destroy each other before anybody evaluates a single one.*
>
> *That is the whole topic. **A sum you cannot face term by term becomes trivial the moment each term is written as a difference.** The three "standard results" printed on the formula sheet are outputs of that same machine, not axioms handed down beside it — and the exam has asked candidates to derive all three.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| series | 级数 | a sequence with $+$ signs put between the terms |
| partial sum | 部分和 | $S_n$ — the total of the first $n$ terms only |
| sum to infinity | 无穷和 | the limit of $S_n$, when there is one |
| convergent | 收敛 | $S_n$ settles on a finite value |
| divergent | 发散 | $S_n$ does not settle |
| method of differences | 差分法 | write each term as $f(r)-f(r+k)$ so the middle cancels |
| telescoping | 裂项相消 | the cancelling itself — literally "split terms, mutually erase" |
| standard results | 标准公式 | the printed closed forms for $\sum r$, $\sum r^2$, $\sum r^3$ |

> [!warning] Two different things are called "differences"
> Finding the $n$th term of $2, 5, 10, 17, \ldots$ by taking differences **down a column** is a *different technique with a nearly identical name* — that one turns a list of terms into a formula, and lives with [[Sequences]]. The **method of differences** here turns a sum into two endpoints. They share a word and nothing else, and a student who conflates them will start subtracting consecutive terms of a series and wonder why nothing cancels.

## First, what a series actually is

Almost every difficulty in this topic dissolves once one sentence is taken seriously.

> **An infinite series does not have a sum. A sequence of partial sums has a limit.**

Given terms $u_1, u_2, u_3, \ldots$, build a *new* sequence out of running totals:

$$S_1 = u_1, \qquad S_2 = u_1+u_2, \qquad S_3 = u_1+u_2+u_3, \qquad \ldots, \qquad S_n = \sum_{r=1}^{n} u_r$$

$S_n$ is the object of study — not the terms. Writing $u_1+u_2+u_3+\cdots$ is a *promise* to look at $S_n$ and see whether it settles, and "the sum to infinity" is shorthand for

$$S_\infty = \lim_{n\to\infty} S_n \quad\text{(when that limit exists — see [[Limit]])}$$

So the topic has exactly one goal: **get $S_n$ in closed form.** Convergence, sums to infinity, and every awkward-looking limit of summation are then just questions about a formula you already hold.

### The three rules of $\sum$, and the one that is not a rule

$\sum$ distributes over addition and pulls out constants, because addition is associative and commutative — you may reorder and regroup a *finite* sum freely:

$$\sum_{r=1}^{n}\bigl(a\,u_r + b\,v_r\bigr) = a\sum_{r=1}^{n} u_r + b\sum_{r=1}^{n} v_r, \qquad \sum_{r=1}^{n} c = cn$$

That last one catches people: a constant still gets added $n$ times. But there is no product rule:

$$\sum u_r v_r \ne \left(\sum u_r\right)\left(\sum v_r\right)$$

Two terms settle it. With $u = v = (1,2)$: the left side is $1+4=5$, the right side is $3\times3=9$. $\sum$ is **linear, never multiplicative** — the same fact, and the same trap, as with $\int$.

## The standard results are outputs, not axioms

MF19 prints these three, so they need no memorising:

$$\sum_{r=1}^{n} r = \tfrac12 n(n+1), \qquad \sum_{r=1}^{n} r^2 = \tfrac16 n(n+1)(2n+1), \qquad \sum_{r=1}^{n} r^3 = \tfrac14 n^2(n+1)^2$$

They *do* need understanding, because the exam repeatedly asks candidates to **derive them** — and always by the method below, from a difference the question hands you. Here is the first one, built from nothing.

**Start with a difference of squares.** For any $r$,

$$(r+1)^2 - r^2 = 2r + 1$$

**Sum both sides from $1$ to $n$.** The left side is a chain in which every square is written once with a $+$ and once with a $-$:

$$\underbrace{(2^2 - 1^2) + (3^2 - 2^2) + (4^2 - 3^2) + \cdots + \bigl((n+1)^2 - n^2\bigr)}_{\text{everything between } 2^2 \text{ and } n^2 \text{ appears twice, oppositely signed}} = (n+1)^2 - 1$$

**Now read the right side with the linearity rules:**

$$\sum_{r=1}^{n}(2r+1) = 2\sum_{r=1}^{n} r + n$$

**Set the two equal and solve:**

$$2\sum r + n = (n+1)^2 - 1 = n^2 + 2n \quad\Longrightarrow\quad \sum_{r=1}^{n} r = \tfrac12 n(n+1) \ \blacksquare$$

The other two come from exactly the same move with a better-chosen starting difference:

| Start from | which expands to | and yields |
|---|---|---|
| $(r+1)^2 - r^2$ | $2r+1$ | $\sum r = \tfrac12 n(n+1)$ |
| $(2r+1)^3 - (2r-1)^3$ | $24r^2 + 2$ | $\sum r^2 = \tfrac16 n(n+1)(2n+1)$ |
| $(2r+1)^4 - (2r-1)^4$ | $64r^3 + 16r$ | $\sum r^3 = \tfrac14 n^2(n+1)^2$ |

**Why those odd-looking starts?** Because you want the expansion to contain the power you are after *and nothing you cannot already sum*. Squaring kills the $r^2$ terms and leaves $2r+1$ — perfect for $\sum r$. For $\sum r^2$ you need a cube, and the $\pm1$ version is chosen so the even powers cancel out of the expansion: $(2r+1)^3-(2r-1)^3$ has no $r$ term at all, so the answer needs no earlier result. For $\sum r^3$ the fourth-power version leaves $64r^3+16r$, which needs $\sum r$ — already in hand.

> [!tip] The check that costs three seconds
> Every closed form here can be tested at $n=1$, where the sum is just its first term. $\tfrac12(1)(2) = 1$ ✓. $\tfrac16(1)(2)(3) = 1$ ✓. $\tfrac14(1)(4)=1$ ✓. And at $n=2$: $\tfrac16(2)(3)(5) = 5 = 1+4$ ✓. A closed form that fails at $n=1$ is wrong, and it takes longer to read this sentence than to check.

## The method of differences

Here is the machine, stated once.

> **If every term can be written as $u_r = f(r) - f(r+1)$, then**
> $$\sum_{r=1}^{n} u_r = f(1) - f(n+1)$$

**Why.** Write the rows out and watch what each one does:

$$
\begin{aligned}
r=1:\quad & f(1) - f(2)\\
r=2:\quad & f(2) - f(3)\\
r=3:\quad & f(3) - f(4)\\
&\ \ \vdots\\
r=n:\quad & f(n) - f(n+1)
\end{aligned}
$$

Every row *hands its second term to the row below*, which brings it back with the opposite sign. Only $f(1)$ was never handed to anyone, and only $f(n+1)$ was never received from anyone. Everything between them appears exactly twice, oppositely signed, and dies. $\blacksquare$

![[telescoping-cancellation.svg|860]]

The name is honest: a brass telescope collapses because each tube's far end is the next tube's near end, so a metre of instrument folds into a few centimetres of brass. Here a sum of $n$ terms folds into **two evaluations**, and the $n-1$ cancellations were free.

### Count the gap — the part that is actually marked

The gap need not be 1. If $u_r = f(r) - f(r+k)$, a term must travel $k$ rows to meet its partner, so $k$ terms at each end never find one:

$$\sum_{r=1}^{n}\bigl[f(r)-f(r+k)\bigr] = \underbrace{f(1)+\cdots+f(k)}_{k\ \text{stranded at the top}} \;-\; \underbrace{f(n+1)-\cdots-f(n+k)}_{k\ \text{stranded at the bottom}}$$

This is not a formula to memorise; it is what writing the rows out *shows you*. And it is why mark schemes say, in as many words, *shows enough terms for cancellation to be clear*: with a gap of 2, a candidate who writes three rows has not yet watched one cancellation complete, and will guess the ends.

### Getting into that form: partial fractions

The method needs $u_r$ as a difference, and the syllabus is explicit that producing one may be your job. For rational terms the tool is [[Partial Fractions]]:

$$\frac{1}{r(r+1)} = \frac{1}{r} - \frac{1}{r+1} \quad\Longrightarrow\quad \sum_{r=1}^{n}\frac{1}{r(r+1)} = 1 - \frac{1}{n+1}$$

> [!tip] The one-second test that the decomposition can possibly telescope
> **The partial-fraction coefficients must add to zero.** In $\frac{1}{r} - \frac{1}{r+1}$ they are $1$ and $-1$. In the three-term case below they are $\tfrac12, -1, \tfrac12$. If your coefficients do not sum to zero, the terms cannot pair off — every row would leave a residue and there would be nothing to cancel. It also catches an arithmetic slip in the decomposition before you have wasted four minutes stacking rows.

## Convergence, by direct consideration

The syllabus wording is precise and worth obeying literally: *recognise, **by direct consideration of a sum to $n$ terms**, when a series is convergent.* No convergence tests. You already hold $S_n$ in closed form — so look at it and let $n\to\infty$.

For $\sum \frac{1}{r(r+1)}$ we found $S_n = 1 - \frac{1}{n+1}$. As $n$ grows the subtracted piece vanishes, so $S_n \to 1$: the series converges and its sum to infinity is $1$. If instead $S_n$ had come out as, say, $\tfrac12 n(n+1)$ or $2^n - 1$, it grows without bound and there is nothing to converge to.

**The trap is the terms.** It is tempting to reason "the terms shrink to nothing, so the total must settle". It does not follow:

![[summation-partial-sums.svg|880]]

The harmonic series $1 + \tfrac12 + \tfrac13 + \cdots$ has terms heading firmly to zero and a total that climbs forever, passing any number you name if you wait long enough. Shrinking terms are *necessary* for convergence and nowhere near sufficient. Convergence is a statement about $S_n$ — which is exactly why getting $S_n$ in closed form was the whole job.

> [!note] Two different convergence questions, both in your course
> [[Arithmetic and Geometric Progressions]] settles convergence with a **criterion**: a geometric series converges precisely when $\lvert r\rvert < 1$, and then $S_\infty = \frac{a}{1-r}$. That is a shortcut earned by knowing the closed form of *every* geometric partial sum in advance. Here there is no such family, so you go back to the definition and read the limit off the $S_n$ you just built. Same question, and the geometric criterion is the special case where somebody has already done the reading for you.

## Worked examples

The three parts below are a single real question — **9231 Paper 11, November 2021, Q2** — and they run the three learning objectives in order. Their expressions look unrelated. They are not.

### Example 1 — using the standard results [3 marks]

> **(a)** *Find $\displaystyle\sum_{r=1}^{n} \bigl(r^3 + 3r^2 + 2r\bigr)$, giving your answer in a fully factorised form.*

**Tool: linearity — split the sum and pull the constants out.**

$$\sum_{r=1}^{n}(r^3+3r^2+2r) = \sum r^3 + 3\sum r^2 + 2\sum r$$

**Tool: the three standard results**, quoted straight off the formula sheet:

$$= \tfrac14 n^2(n+1)^2 \;+\; 3\cdot\tfrac16 n(n+1)(2n+1) \;+\; 2\cdot\tfrac12 n(n+1)$$

**Tool: factor before expanding — always.** Every piece carries $n(n+1)$; take out $\tfrac14 n(n+1)$ and only the bracket needs work:

$$= \tfrac14 n(n+1)\Bigl[\,n(n+1) + 2(2n+1) + 4\,\Bigr] = \tfrac14 n(n+1)\bigl[n^2+5n+6\bigr]$$

$$= \boxed{\ \tfrac14\,n(n+1)(n+2)(n+3)\ }$$

Expanding everything into a quartic and re-factorising at the end is the long road and the main source of lost marks. Check at $n=1$: the sum is $1+3+2=6$, and $\tfrac14(1)(2)(3)(4) = 6$ ✓.

### Example 2 — partial fractions and the method of differences [5 marks]

> **(b)** *Express $\dfrac{1}{r(r+1)(r+2)}$ in partial fractions and hence use the method of differences to find $\displaystyle\sum_{r=1}^{n}\frac{1}{r(r+1)(r+2)}$.*

**Tool: partial fractions**, three distinct linear factors:

$$\frac{1}{r(r+1)(r+2)} = \frac{1}{2r} - \frac{1}{r+1} + \frac{1}{2(r+2)}$$

Coefficients $\tfrac12, -1, \tfrac12$ sum to zero, so telescoping is possible.

**Tool: write the rows out until the pattern closes.** With $f(x) = \frac1x$, each row is $\tfrac12 f(r) - f(r+1) + \tfrac12 f(r+2)$:

$$
\begin{aligned}
&\tfrac12 f(1) \;-\; f(2) \;+\; \tfrac12 f(3)\\
&\tfrac12 f(2) \;-\; f(3) \;+\; \tfrac12 f(4)\\
&\tfrac12 f(3) \;-\; f(4) \;+\; \tfrac12 f(5)\\
&\qquad\vdots\\
&\tfrac12 f(n-1) - f(n) + \tfrac12 f(n+1)\\
&\tfrac12 f(n) \;-\; f(n+1) \;+\; \tfrac12 f(n+2)
\end{aligned}
$$

Read a single column of the interior: $f(3)$ appears as $+\tfrac12$ in row 1, as $-1$ in row 2, and as $+\tfrac12$ in row 3. **The two halves arrive from opposite sides and together cancel the whole.** That is the gap-2 structure, and it is why three rows would not have been enough to see it.

**Tool: collect what never got cancelled.** At the top, $\tfrac12 f(1)$ survives whole and $-f(2)$ is only half-repaid by row 2's $\tfrac12 f(2)$; at the bottom the mirror image:

$$S_n = \tfrac12 f(1) - \tfrac12 f(2) - \tfrac12 f(n+1) + \tfrac12 f(n+2) = \tfrac12 - \tfrac14 - \frac{1}{2(n+1)} + \frac{1}{2(n+2)}$$

$$\boxed{\ S_n = \frac14 - \frac{1}{2(n+1)} + \frac{1}{2(n+2)}\ }$$

Check at $n=1$: the sum is $\tfrac16$, and $\tfrac14 - \tfrac14 + \tfrac16 = \tfrac16$ ✓.

> [!tip] The same answer in one line, by pairing at a higher level
> Nothing forces you to split into three pieces. Notice instead that
> $$\frac{1}{r(r+1)(r+2)} = \frac12\left[\frac{1}{r(r+1)} - \frac{1}{(r+1)(r+2)}\right]$$
> — check it by combining the bracket over a common denominator, where the numerator is $(r+2)-r = 2$. Now the term *is already* $\tfrac12\bigl[g(r) - g(r+1)\bigr]$ with $g(r) = \frac{1}{r(r+1)}$: a gap of 1, one survivor at each end, no stacking needed.
> $$S_n = \tfrac12\bigl[g(1) - g(n+1)\bigr] = \tfrac12\left[\frac12 - \frac{1}{(n+1)(n+2)}\right] = \frac14 - \frac{1}{2(n+1)(n+2)}$$
> Identical to the boxed answer — combine the two fractions there and see. The exam marks the partial-fraction route because it always works; this route is worth knowing because when it applies it is four minutes shorter, and because spotting it is the same skill as spotting the difference in the first place.

### Example 3 — the sum to infinity [1 mark]

> **(c)** *Deduce the value of $\displaystyle\sum_{r=1}^{\infty}\frac{1}{r(r+1)(r+2)}$.*

"Deduce" means *use what you just found* — no new work is expected, and one mark is on offer.

**Tool: let $n\to\infty$ in the closed form.** Both fractions have a denominator growing without bound, so both vanish:

$$\sum_{r=1}^{\infty}\frac{1}{r(r+1)(r+2)} = \lim_{n\to\infty}\left[\frac14 - \frac{1}{2(n+1)} + \frac{1}{2(n+2)}\right] = \boxed{\frac14}$$

> [!note] The two halves of that question were the same expression
> Part (a) summed $r^3+3r^2+2r$. Factorise it: $r^3+3r^2+2r = r(r+1)(r+2)$ — **precisely the denominator of part (b)**. One question asked for the sum of a thing and the sum of its reciprocal.
>
> Better still, part (a) telescopes too. Take $F(r) = \tfrac14 r(r+1)(r+2)(r+3)$ — the same product with one more factor bolted on — and compute
> $$F(r) - F(r-1) = \tfrac14 r(r+1)(r+2)\bigl[(r+3)-(r-1)\bigr] = \tfrac14 r(r+1)(r+2)\cdot 4 = r(r+1)(r+2)$$
> so the sum collapses to $F(n) - F(0) = \tfrac14 n(n+1)(n+2)(n+3)$ — the boxed answer of Example 1, with no standard results used at all. **There was only ever one method on this page.** The formula sheet is its trophy cabinet.

### And when the limits move

Papers routinely follow up with $\displaystyle\sum_{r=n+1}^{2n}$ or $\displaystyle\sum_{r=n}^{n^2}$, worth two marks. Nothing new is needed: a sum from $a$ to $b$ is the sum to $b$ minus the sum to $a-1$.

$$\sum_{r=n+1}^{2n} u_r = S_{2n} - S_n$$

The only real risk is an off-by-one on the lower limit, so **name it out loud**: to start at $r=n+1$ you remove everything up to and including $r=n$, hence $S_n$ — not $S_{n+1}$, not $S_{n-1}$. Test it on a tiny case if unsure: $\sum_{r=2}^{3} = S_3 - S_1$, which is $u_2+u_3$ ✓.

## Common misconceptions (teaching notes)

### 1. "The method of differences is that difference thing from IGCSE"

The two techniques share almost a name and nothing else. Students start subtracting consecutive *terms of the series* and cannot see why nothing collapses.

**Fix:** put them side by side once, explicitly. Differences **down a column of terms** turn a list into a formula for $u_r$ ([[Sequences]]). The method of differences turns a *sum* into two endpoints, and it starts by rewriting a single term as $f(r)-f(r+k)$ — an operation performed on one term at a time, never between neighbours.

### 2. "The terms go to zero, so it converges"

The single most common false step, and it feels obvious.

**Fix:** the harmonic series, computed rather than asserted. $S_{10} \approx 2.93$, $S_{1000} \approx 7.49$, $S_{100000} \approx 12.09$ — still climbing, and it will pass $100$ eventually. Shrinking terms are necessary, not sufficient. Then ask what the syllabus's phrase *by direct consideration of a sum to $n$ terms* was warning against, and the wording stops looking pedantic.

### 3. "Cancel the middle and write the first and last"

True only for a gap of 1. With a gap of 2 the student writes two survivors instead of four and loses the question.

**Fix:** ban the phrase "the middle cancels" and replace it with a question — *how far does a term have to travel to find its partner?* That number is how many are stranded at each end. Then make them write six rows of a gap-2 example and physically join the cancelling pairs with a pen.

### 4. "$\sum u_r v_r = \sum u_r \cdot \sum v_r$"

Invented under pressure, usually when a term is a product that will not decompose.

**Fix:** two numbers. $u = v = (1,2)$ gives $5$ on the left and $9$ on the right. Then name the pattern: $\sum$ is linear like $\int$, and shares its trap — nobody writes $\int fg = \int f \int g$ either.

### 5. "The standard results are printed, so I don't need to know where they come from"

Reasonable-sounding, and directly contradicted by the papers.

**Fix:** show the real questions. *By considering $(r+1)^2 - r^2$, prove that $\sum r = \tfrac12 n(n+1)$* has appeared with 4 marks; the $r^2$ version with 5; the $r^3$ version with 6. Being handed the destination is exactly why the marks are in the journey.

## Exam Notes

### Cambridge 9231 Further Mathematics — **Further Pure 1, Paper 1**

**§1.3** is the most reliably examined section on the paper: a §1.3 question has appeared on **every Paper 1 variant from 2021 through 2026**, June and November. Paper 1 is compulsory for both AS and A Level. Three learning objectives:

- **Use the standard results for $\sum r$, $\sum r^2$, $\sum r^3$ to find related sums.** Examined as a polynomial in $r$ to be summed and **fully factorised** — the factorised form is where the accuracy mark sits.
- **Use the method of differences to obtain the sum of a finite series**, with the syllabus adding that *use of partial fractions to express a general term in a suitable form may be required.* Read: producing the decomposition is your job, not the question's.
- **Recognise, by direct consideration of a sum to $n$ terms, when a series is convergent, and find the sum to infinity in such cases.** Note *direct consideration* — this is the definition, applied to the closed form you have just built. No convergence tests are on the syllabus.

**The recurring question shapes**, in rough order of frequency:

| Shape | Looks like | Marks |
|---|---|---|
| decompose, then telescope | *"Express … in partial fractions and hence use the method of differences to find …"* | 4–5 |
| deduce the sum to infinity | *"Deduce the value of $\sum_{r=1}^{\infty}$ …"* | 1 |
| shift the limits | *"Find also $\sum_{r=n+1}^{2n}$ … in terms of $n$"* | 2 |
| derive a standard result | *"By considering $(2r+1)^3-(2r-1)^3$, use the method of differences to prove …"* | 4–6 |
| decide convergence | *"Deduce the set of values of $x$ for which the infinite series is convergent, and give the sum to infinity when this exists"* | 3 |

**What mark schemes actually reward:**

- **Written-out rows.** The guidance reads *shows enough terms for cancellation to be clear*. A jump straight to the answer forfeits the method mark even when the answer is right — and with a gap of 2 you genuinely cannot see the ends without them.
- **"Deduce" means reuse.** A one-mark "deduce" part is marked *follow-through* from your own previous answer: even a wrong $S_n$ earns the mark if the limit is taken correctly. Never leave it blank.
- **Fully factorised** answers for the standard-results part. Factor before expanding.
- **In terms of $n$ and $k$** means the constant stays symbolic to the end; several recent versions carry a parameter through the whole question precisely to punish early substitution.

**MF19 status.** The three standard results *are* printed, under Further Pure Mathematics → Algebra → Summations. The method of differences is not, and nor is anything about convergence — there is nothing to look up there. See [[MF19 Reference (9709)]].

### Other Further Mathematics specifications

Edexcel places series and the method of differences in **Further Pure 1**; AQA and OCR examine the same material in their first further-pure papers, and OxAQA 9660 lists the identical three standard results. Content and technique are the same everywhere; only the formula-sheet support varies.

### Where this is *not* examined

**Not on Cambridge 9709** — single-maths A-Level covers arithmetic and geometric series ([[Arithmetic and Geometric Progressions]]) and stops there. **Not on IB Analysis and Approaches**, HL included: the method of differences is absent, though HL meets series convergence again through Maclaurin expansions. **AP Calculus BC** takes a different road entirely — it examines convergence *tests* (ratio, integral, comparison, alternating) which Cambridge does not, and telescoping series appear there as one example among many rather than as a named technique.

> [!info] Beyond syllabus — this is the fundamental theorem of calculus, in discrete clothing
> Set the two statements side by side:
> $$\int_a^b F'(x)\,dx = F(b) - F(a) \qquad\qquad \sum_{r=a}^{b}\bigl[F(r+1)-F(r)\bigr] = F(b+1) - F(a)$$
> They are the same theorem. Integration undoes differentiation and leaves you evaluating an antiderivative at two endpoints; summation undoes *differencing* and leaves you evaluating an "antidifference" at two endpoints. The method of differences is not a trick that happens to work — it is the discrete world's version of the most important theorem in calculus, and "find $f$ such that $u_r = f(r)-f(r+1)$" is word-for-word "find an antiderivative".
>
> The analogy keeps paying. The discrete counterpart of $x^n$ is not $r^n$ but the **falling factorial** $r^{(n)} = r(r-1)\cdots(r-n+1)$, because differencing it behaves exactly like differentiating a power: $\Delta r^{(n)} = n\,r^{(n-1)}$. That is why $\sum r(r+1)(r+2)$ came out as $\tfrac14 n(n+1)(n+2)(n+3)$ — a product of *four* consecutive integers over $4$, the discrete image of $\int x^3\,dx = \tfrac14 x^4$ — while $\sum r^2$ needs an ugly $\tfrac16 n(n+1)(2n+1)$. Choose the right notion of "power" and the formula sheet collapses to one line.

> [!info] Beyond syllabus — the sums that refuse to telescope
> Telescoping is a gift, not a right, and most series do not give it. Two famous refusals are worth meeting.
>
> The **harmonic series** $\sum \frac1r$ diverges, which Nicole Oresme proved around 1350 with an argument needing no calculus: group the terms as $\tfrac12$, then $\tfrac13+\tfrac14 > \tfrac12$, then $\tfrac15+\cdots+\tfrac18 > \tfrac12$, then the next sixteen, and so on. Each block outweighs $\tfrac12$, there are infinitely many blocks, so the total exceeds any bound. It just takes its time: passing $100$ needs more terms than there are atoms in a person.
>
> The **Basel problem**, $\sum \frac{1}{r^2}$, converges — comparison with our telescoping series shows it is bounded — but to *what*? The question defeated the best mathematicians for ninety years until Euler, aged 28, produced $\frac{\pi^2}{6}$. Nothing in the problem mentions a circle. That a sum of reciprocal squares should summon $\pi$ is one of the genuinely astonishing facts in mathematics, and the reason the young Euler became famous overnight.

## Connections

- **Parent:** [[Sequences]] — a series is a sequence with plus signs between its terms, and the partial sums $S_n$ are themselves a sequence, which is the whole reason limits get involved.
- **Sibling:** [[Arithmetic and Geometric Progressions]] — the two families whose partial sums have closed forms already known, so convergence there is a criterion rather than an investigation.
- **Tool used:** [[Partial Fractions]] — the standard route from a rational term to a difference; the syllabus warns you will have to produce the decomposition yourself.
- **Alternative proof:** [[Proof by Induction]] — certifies a closed form you already suspect; the method of differences *produces* one from nothing. Induction verifies, differences discover.
- **Application:** [[Maclaurin Series]] — where infinite sums stop being a curiosity and become a way of writing functions, with convergence the price of admission.
- **Where the idea leads:** [[Complex Numbers]] — real and imaginary parts let a pair of stubborn trigonometric sums, $\cos\theta + \cos2\theta + \cdots$ and its sine twin, be handled as one geometric series in $e^{i\theta}$, so a partial sum of the kind built here answers both at once.
- **For 9231 students:** [[MF19 Reference (9231)]] — the three standard results are printed; the method itself is not.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\displaystyle\sum_{r=1}^{n} u_r$ | `\sum_{r=1}^{n} u_r` | limits above and below in display mode |
| $S_n$ | `S_n` | the $n$th partial sum — the object of study |
| $S_\infty$ | `S_\infty` | the sum to infinity, when the limit exists |
| $\displaystyle\lim_{n\to\infty}$ | `\lim_{n\to\infty}` | always space `\to`; the limit *defines* $S_\infty$ |
| $f(r) - f(r+k)$ | `f(r) - f(r+k)` | the telescoping form; $k$ is the gap |
| $\Delta$ | `\Delta` | the difference operator, $\Delta f(r) = f(r+1)-f(r)$ |
| $r^{(n)}$ | `r^{(n)}` | falling factorial — the discrete analogue of a power |

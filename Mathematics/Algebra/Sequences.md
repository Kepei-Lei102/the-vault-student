---
chinese: 数列 (shùliè)
prerequisites:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Simultaneous Equations (Vocab)]]"
leads_to:
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Iteration]]"
  - "[[Recursion]]"
  - "[[Big-O Notation]]"
  - "[[Proof by Induction]]"
  - "[[Binomial Series]]"
  - "[[Maclaurin Series]]"
  - "[[Numerical Methods]]"
  - "[[Searching]]"
  - "[[Sorting]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A24
  - syllabus/9260-A25
  - syllabus/9260-A26
  - syllabus/0580-E2-7
  - type/definition
  - type/formula
  - notation/subscript
  - misconception/first-vs-second-difference
  - misconception/pattern-spotting
  - misconception/exponential-indexing
---

# Sequences 数列

## Definition

### Formal

A **sequence** (数列) is an ordered list of numbers $u_1, u_2, u_3, \ldots$ The $n$th entry $u_n$ is the **$n$th term** (第 $n$ 项). Two ways to describe a sequence:

- **Term-to-term rule** (递推公式) — how to get the next term from the previous one(s). Example: $u_{n+1} = u_n + 3$ with $u_1 = 5$.
- **Position-to-term rule** (通项公式 / nth term formula) — a direct formula for $u_n$ in terms of $n$. Example: $u_n = 3n + 2$.

Both describe the same sequence $5, 8, 11, 14, \ldots$ — but the position-to-term rule lets you jump to $u_{100}$ without computing the 99 terms before it. That's the point of the exam skill: **turn a list of numbers into a formula**.

### Intuitive

You're given the first few terms of a pattern. The question is: *what's the rule?*

The 0580/9260 exam gives you a short list — say $3, 8, 15, 24, 35, \ldots$ — and asks for the $n$th term. You treat the sequence like a detective scene: compute differences, match shapes, extract coefficients. Three or four standard fingerprints (linear, quadratic, cubic, exponential) cover almost everything they test.

### 中文锚点 (Chinese Anchor)

数列 = 按顺序排列的一列数。
项 = term; 第 $n$ 项 = $n$th term; 通项公式 = $n$th-term formula.

**两种给数列的方式：**

| 方式 | 英文 | 例子 |
|---|---|---|
| 递推 | term-to-term | $u_{n+1} = u_n + 3$, $u_1 = 5$ |
| 通项 | position-to-term | $u_n = 3n + 2$ |

**Key Chinese idea:** 找规律 (zhǎo guīlǜ) = "find the pattern." The exam skill is converting 找规律 into a **formula**, not just continuing the pattern. "$u_6 = 20$" is guessing; "$u_n = 3n + 2$" is mathematics.

---

## CS bridge — iteration and recursion 迭代与递归

The two ways of writing a sequence are the two fundamental ways a computer executes a **recurrence relation** (递推关系):

| Mathematical form | How a computer runs it | Example in Python |
|---|---|---|
| **Term-to-term** $u_{n+1} = u_n + 3$ | **[[Iteration]]** — a `for` loop carries the running value | `u = 5`<br>`for _ in range(n-1): u += 3` |
| **Term-to-term** $u_{n+1} = u_n + 3$ | **[[Recursion]]** — the function calls itself | `def u(n):`<br>`    if n == 1: return 5`<br>`    return u(n-1) + 3` |
| **Position-to-term** $u_n = 3n + 2$ | **Closed form** — compute directly, no loop, no stack | `def u(n): return 3*n + 2` |

[[Iteration]] and [[Recursion]] compute exactly the same recurrence — one keeps the running total in a variable, the other keeps it on the call stack. A position-to-term formula, when one exists, is what CS calls a **closed form**: it eliminates the loop entirely and runs in $O(1)$ (see [[Big-O Notation]]) regardless of $n$.

**The Fibonacci punchline.** Naive recursion on Fibonacci ($F_{n+2} = F_{n+1} + F_n$) is a disaster — every call spawns two more, so computing $F_{40}$ takes over a billion function calls. Iterative Fibonacci runs in $O(n)$. Binet's closed form

$$F_n = \dfrac{\varphi^n - \psi^n}{\sqrt{5}}, \qquad \varphi = \dfrac{1 + \sqrt{5}}{2}, \quad \psi = \dfrac{1 - \sqrt{5}}{2}$$

computes any $F_n$ in $O(1)$. *Finding a closed form for a recurrence* — which is exactly what the difference method below does for polynomial sequences — is the most valuable optimisation in computing.

> [!tip] Why this matters even for IGCSE students
> You already use closed forms every time you write $u_n = an + b$ instead of "add $d$ repeatedly starting from $a$." The difference between $O(n)$ and $O(1)$ is the difference between a calculator taking 0.001 seconds and a supercomputer taking 30 years on the same problem. The maths you're learning is *exactly* the optimisation computer scientists spend careers chasing.

*Full treatment of the iteration/recursion duality is reserved for the CS folder's [[Recursion]] card.*

---

## The Difference Method — the exam's main tool

Given terms $u_1, u_2, u_3, \ldots$, compute the **first differences**:

$$d_1 = u_2 - u_1, \quad d_2 = u_3 - u_2, \quad d_3 = u_4 - u_3, \ldots$$

Then compute differences of differences (**second differences**), and so on.

**The fingerprint rule:**

| Sequence type | What goes constant | $n$th-term shape |
|---|---|---|
| Linear (AP) | **First** differences constant | $u_n = an + b$ |
| Quadratic | **Second** differences constant | $u_n = an^2 + bn + c$ |
| Cubic | **Third** differences constant | $u_n = an^3 + bn^2 + cn + d$ |
| Exponential / Geometric | **Ratios** constant | $u_n = ab^{n-1}$ |

Compute differences from the top; the first row that goes flat names your fingerprint.

> [!tip] Why the rule works
> A polynomial of degree $k$ has its $k$th difference constant and its $(k+1)$th difference zero. This is the discrete analogue of: "$k$ derivatives of a degree-$k$ polynomial give a constant, and $k+1$ give zero." Differences play the role of derivatives on integer inputs. That single idea — *differences behave like derivatives* — is the foundation of the **calculus of finite differences** (Newton, 1687), used today in numerical analysis and signal processing. Full story below in Beyond syllabus.

---

## Linear Sequences

**Fingerprint:** first differences constant.

$$3,\ 7,\ 11,\ 15,\ 19,\ldots \qquad \underbrace{4, 4, 4, 4}_{\text{first differences}}$$

**$n$th term:** $u_n = dn + (u_1 - d)$ where $d$ is the common difference.

Practical shortcut — read off two numbers:
- Coefficient of $n$ = common difference ($d = 4$).
- Constant = $u_1 - d$ (here $3 - 4 = -1$).

$$u_n = 4n - 1$$

Check: $u_1 = 3$ ✓, $u_5 = 19$ ✓.

This is the same formula as an arithmetic progression, just written in $an + b$ form instead of $a + (n-1)d$. See [[Arithmetic and Geometric Progressions]] for the derivation and the sum.

---

## Quadratic Sequences — the main event

**Fingerprint:** *second* differences constant, first differences changing linearly.

$$3,\ 8,\ 15,\ 24,\ 35,\ldots$$

Compute:

$$\underbrace{5,\ 7,\ 9,\ 11}_{\text{first differences}} \qquad \underbrace{2,\ 2,\ 2}_{\text{second differences, constant}}$$

Second differences constant $\implies$ quadratic $u_n = an^2 + bn + c$.

### The shortcut that saves your life

Three things to find: $a$, $b$, $c$.

$$\boxed{a = \tfrac{1}{2} \cdot (\text{second difference})}$$

Here $a = \tfrac{2}{2} = 1$. Now you know $u_n = n^2 + bn + c$, so subtract $n^2$ from the sequence and what's left is a linear sequence in $n$:

$$n^2: \quad 1, 4, 9, 16, 25$$
$$u_n - n^2: \quad 2, 4, 6, 8, 10$$

That's linear with common difference $2$, so $u_n - n^2 = 2n$, giving:

$$\boxed{u_n = n^2 + 2n}$$

Check: $n = 1 \to 1 + 2 = 3$ ✓, $n = 5 \to 25 + 10 = 35$ ✓.

### Why $a = \tfrac{1}{2} d_2$ — the proof

If $u_n = an^2 + bn + c$, compute:

$$u_{n+1} - u_n = a(n+1)^2 + b(n+1) - an^2 - bn = a(2n + 1) + b = 2an + (a + b)$$

That's the first difference, a linear expression in $n$. Take one more difference:

$$(u_{n+2} - u_{n+1}) - (u_{n+1} - u_n) = \bigl[2a(n+1) + (a+b)\bigr] - \bigl[2an + (a+b)\bigr] = 2a$$

So the second difference is **always $2a$** regardless of $n$. Solving: $a = \tfrac{d_2}{2}$. $\blacksquare$

That's the theorem behind the shortcut. You don't re-derive it every time — you just *know* the leading coefficient is half the second difference.

### The full-system method (backup)

If the shortcut feels wobbly, plug $n = 1, 2, 3$ into $u_n = an^2 + bn + c$ and solve a $3 \times 3$ system:

$$a + b + c = u_1, \quad 4a + 2b + c = u_2, \quad 9a + 3b + c = u_3$$

Same answer, more arithmetic. Use this when the shortcut doesn't feel clean (e.g. the sequence is given as $u_3, u_4, u_5, \ldots$ without the first two terms).

---

## Cubic Sequences

**Fingerprint:** third differences constant (0580 Extended only).

$$1,\ 8,\ 27,\ 64,\ 125,\ldots \qquad \underbrace{7, 19, 37, 61}_{d_1} \quad \underbrace{12, 18, 24}_{d_2} \quad \underbrace{6, 6}_{d_3}$$

Third differences constant $= 6$. By the same argument as before, the leading coefficient satisfies $a = \tfrac{d_3}{6} = 1$ (the general rule: for degree $k$, leading coefficient $= \tfrac{d_k}{k!}$).

Subtract $n^3$ from each term: $0, 0, 0, 0, 0$ — done. $u_n = n^3$.

> [!info] Beyond syllabus — factorials show up because of calculus
> $k!$ appears as the divisor because the $k$th difference of $n^k$ is $k!$ — the same $k!$ that shows up in Taylor expansions. Differences and derivatives share the Taylor-series DNA. See [[Binomial Theorem]] for the combinatorial flavour of the same idea.

---

## Exponential / Geometric Sequences

**Fingerprint:** *ratios* constant, not differences.

$$3,\ 6,\ 12,\ 24,\ 48,\ldots$$

Ratios: $\tfrac{6}{3} = \tfrac{12}{6} = \tfrac{24}{12} = 2$. Constant ratio $r = 2$ $\implies$ geometric sequence.

**$n$th term:** $u_n = u_1 \cdot r^{n-1} = 3 \cdot 2^{n-1}$. (Cambridge 0580 also writes this as $ab^n$ with $a = \tfrac{3}{2}$, $b = 2$ — equivalent but index-shifted.)

> [!warning] Exponential indexing trap
> Is it $ar^{n-1}$ or $ar^n$? Both forms are valid — they describe the same sequence with the index shifted. Always check your first term. If the formula gives $u_1 = a$, good. If it gives $u_1 = ar$, you're off by one.

The detailed theory (sum of first $n$ terms, sum to infinity, convergence) lives in [[Arithmetic and Geometric Progressions]].

---

## Special Number Sequences — recognise on sight

The 9260 A25 and 0580 E2.7 syllabi list these by name. Learn the $n$th terms as a table:

| Sequence | Terms | $n$th term | Notes |
|---|---|---|---|
| **Natural numbers** 自然数 | $1, 2, 3, 4, 5, \ldots$ | $n$ | The reference sequence |
| **Odd numbers** 奇数 | $1, 3, 5, 7, 9, \ldots$ | $2n - 1$ | First difference $= 2$ |
| **Even numbers** 偶数 | $2, 4, 6, 8, 10, \ldots$ | $2n$ | First difference $= 2$ |
| **Square numbers** 平方数 | $1, 4, 9, 16, 25, \ldots$ | $n^2$ | Quadratic, $d_2 = 2$ |
| **Cube numbers** 立方数 | $1, 8, 27, 64, 125, \ldots$ | $n^3$ | Cubic, $d_3 = 6$ |
| **Triangular numbers** 三角形数 | $1, 3, 6, 10, 15, \ldots$ | $\tfrac{n(n+1)}{2}$ | Quadratic; the Gauss sum $1 + 2 + \cdots + n$ |
| **Powers of 2** 2 的幂 | $1, 2, 4, 8, 16, \ldots$ | $2^{n-1}$ | Geometric, $r = 2$ |
| **Fibonacci** 斐波那契 | $1, 1, 2, 3, 5, 8, 13, \ldots$ | (no polynomial formula) | Term-to-term: $u_{n+2} = u_{n+1} + u_n$ |

The Fibonacci row is the warning: **not every sequence has a polynomial $n$th term.** Fibonacci's closed form (Binet's formula) involves $\sqrt{5}$ and $\varphi$, the golden ratio — off-syllabus but beautiful.

> [!tip] The triangular-number shortcut
> Triangular numbers $T_n = \tfrac{n(n+1)}{2}$ show up all over combinatorics: they count handshakes in a group of $n+1$, diagonals of a polygon, edges in a complete graph, terms in a quadratic expansion. Every exam student should be able to recite $T_{10} = 55$.

---

## Worked Examples

### Example 1 (0580 E2.7): Find the nth term of the quadratic sequence $2, 7, 14, 23, 34, \ldots$

First differences: $5, 7, 9, 11$ — linear, not constant. Second differences: $2, 2, 2$ — constant, so quadratic.

$a = \tfrac{d_2}{2} = 1$, so $u_n = n^2 + bn + c$.

Subtract $n^2$: $2 - 1 = 1$, $7 - 4 = 3$, $14 - 9 = 5$, $23 - 16 = 7$, $34 - 25 = 9$. That's $1, 3, 5, 7, 9$ — odd numbers, $n$th term $2n - 1$.

$$\boxed{u_n = n^2 + 2n - 1}$$

### Example 2 (0580 E2.7, harder): Mixed linear-and-quadratic wording

A sequence starts $4, 10, 18, 28, 40, \ldots$ Find the $n$th term.

First differences: $6, 8, 10, 12$. Second differences: $2, 2, 2$. Quadratic with $a = 1$.

Subtract $n^2 = 1, 4, 9, 16, 25$: remainder $3, 6, 9, 12, 15$ — linear, $n$th term $3n$.

$$\boxed{u_n = n^2 + 3n}$$

### Example 3 (9260 A26 Ext): Cubic sequence

Find the $n$th term of $2, 10, 30, 68, 130, \ldots$

First differences: $8, 20, 38, 62$. Second: $12, 18, 24$. Third: $6, 6$. Cubic with $a = \tfrac{6}{6} = 1$.

Subtract $n^3$: $2 - 1 = 1$, $10 - 8 = 2$, $30 - 27 = 3$, $68 - 64 = 4$, $130 - 125 = 5$. That's just $n$.

$$\boxed{u_n = n^3 + n}$$

### Example 4 (0580 E2.7): Exponential sequence

Find the $n$th term of $6, 12, 24, 48, 96, \ldots$

Ratios: $2, 2, 2, 2$ — constant. Geometric with $r = 2$, $u_1 = 6$.

$$\boxed{u_n = 6 \cdot 2^{n-1} = 3 \cdot 2^n}$$

Both forms are acceptable; the second follows by writing $6 = 3 \cdot 2$.

---

## Common Misconceptions (Teaching Notes)

### 1. Confusing first and second differences

Students see differences changing and immediately call it "a pattern." They write $u_n$ = first term + (changing difference) × $n$ — which makes no sense.

**Fix.** If the **first** difference isn't constant, keep taking differences until something *is*. Name the sequence by the row that goes flat. Linear = row 1 flat; quadratic = row 2 flat; cubic = row 3 flat.

### 2. Using the AP formula on a quadratic sequence

Sequence $2, 7, 14, 23, \ldots$ First difference $5$, then $7$, then $9$. Student writes $u_n = 5n - 3$ (treating it like an AP with $d = 5$). This gives $u_2 = 7$ ✓ but $u_3 = 12$ ✗ (should be $14$).

**Fix.** Always compute the **first three** differences before committing. If they don't all agree, it's not linear — stop writing AP formulas.

### 3. "Spotting the pattern" without proving it

Students continue the sequence $1, 3, 6, 10, \ldots$ by saying "add one more each time, so next is $15$." That's *guessing*, not *deriving*. The exam wants a formula.

**Fix.** Force the move from pattern-continuation to formula-writing. Triangular numbers: $u_n = \tfrac{n(n+1)}{2}$, tested by plugging $n = 5$ → $15$ ✓. The formula is the answer; the continuation is a check.

### 4. Exponential indexing — $ab^n$ vs $ab^{n-1}$

Sequence $3, 6, 12, 24$. Student writes $u_n = 3 \cdot 2^n$. Test: $u_1 = 3 \cdot 2 = 6$ ✗. Correct is $u_n = 3 \cdot 2^{n-1}$ or equivalently $\tfrac{3}{2} \cdot 2^n$.

**Fix.** Always plug $n = 1$. If $u_1$ isn't right, your exponent is off by one.

### 5. Forgetting to simplify

$u_n = n^2 + 3n - 4 + 2$. Students leave it as is. Exam marks deduct — simplify: $u_n = n^2 + 3n - 2$.

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E2.7 — "Sequences: term-to-term, nth term; Linear, quadratic, cubic, exponential."

Tested every paper. Two question types:

- **"Find the next two terms and the $n$th term"** — usually linear or quadratic. The $n$th term is worth 2–3 marks.
- **"Given the $n$th term is $\_\_\_$, find the $k$th term"** — trivial substitution, 1 mark.

**Mark-scheme patterns:**
- Writing the correct form (e.g. "$u_n = an^2 + bn + c$") earns a method mark even if the arithmetic errs.
- Stating "second difference $= 2$" before computing $a$ is worth a mark on its own.
- Cubic and exponential questions are less common but do appear — the syllabus explicitly lists them.

### OxAQA 9260

**Syllabus ref:** A24 (generating sequences), A25 (recognising special sequences), A26 (deducing the $n$th term).

Both **arithmetic progressions** and **quadratic sequences** are named directly in A25 Ext. A26 explicitly requires "deduce nth term" for linear (core) and quadratic (Ext).

> [!note] 9260 vs 0580 overlap
> 0580 E2.7 is slightly broader (cubic, exponential listed explicitly). 9260 A25/A26 emphasise triangular/square/cube numbers as *named* sequences to recognise on sight. Both syllabi test the same core skill: compute differences, match the fingerprint, write the formula.

### A-Level and Beyond

A-Level Pure 2 and IB Mathematics AA both revisit sequences with more machinery:

- Recurrence relations of higher order (solving $u_{n+2} = au_{n+1} + bu_n$ — Fibonacci-style).
- Proof by induction that a proposed $n$th term is correct.
- Convergence/divergence of infinite sequences — see [[Limit]].
- Generating functions (university-level): a bijection between sequences and power series.

> [!info] Beyond syllabus — Newton's forward differences
> The difference method you learned above is a special case of **Newton's forward difference formula**:
> $$u_n = \sum_{k=0}^{\infty} \binom{n-1}{k} \Delta^k u_1$$
> where $\Delta^k u_1$ is the $k$th difference of the first term. If the sequence is a polynomial of degree $m$, the sum terminates at $k = m$ and gives the $n$th term exactly. This is the algorithm that powered 19th-century numerical tables (logarithms, trigonometric values) long before calculators existed — and it's the reason the difference method always works.

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — term, coefficient, substitution
- **Prerequisite:** [[Simultaneous Equations (Vocab)]] — for the backup full-system method of solving $a, b, c$
- **Leads to:** [[Arithmetic and Geometric Progressions]] — the AP / GP instances of linear and exponential sequences, plus their sums and sum to infinity
- **Leads to:** [[Limit]] — what happens to $u_n$ as $n \to \infty$ (convergent / divergent sequences)
- **Application:** [[Binomial Theorem]] — the coefficients $\binom{n}{k}$ themselves form sequences with beautiful difference patterns
- **CS bridge — reserved:** [[Iteration]], [[Recursion]] — the two ways a computer executes a term-to-term rule
- **CS bridge — reserved:** [[Big-O Notation]] — why closed forms matter: $O(1)$ vs $O(n)$ vs $O(2^n)$

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $u_n$ | `u_n` | $n$th term |
| $u_{n+1} = f(u_n)$ | `u_{n+1} = f(u_n)` | term-to-term (recursive) definition |
| $d_1, d_2, d_3$ | `d_1, d_2, d_3` | first, second, third differences |
| $\Delta u_n$ | `\Delta u_n` | forward difference operator (Beyond syllabus) |
| $T_n$ | `T_n` | triangular number |
| $a = \tfrac{d_2}{2}$ | `a = \tfrac{d_2}{2}` | leading coefficient shortcut for quadratic sequences |
| $an^2 + bn + c$ | `an^2 + bn + c` | general quadratic $n$th term |
| $ab^{n-1}$ | `ab^{n-1}` | exponential $n$th term — brace the exponent |

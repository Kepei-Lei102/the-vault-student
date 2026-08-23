---
chinese: 二项式定理 (èr xiàng shì dìnglǐ)
prerequisites:
  - "[[Permutations and Combinations]]"
  - "[[Factorial Notation]]"
  - "[[Laws of Indices]]"
  - "[[Indices in Algebra (Vocab)]]"
  - "[[Counting Problems]]"
  - "[[Expanding Brackets (Vocab)]]"
leads_to:
  - "[[Symmetric Functions of Roots]]"
  - "[[Power Rule]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Taylor Series]]"
  - "[[Euler's Number]]"
  - "[[Binomial Series]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[De Moivre at Work]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9260-A4
  - syllabus/9260-A4-Ext
  - syllabus/0606-12-1
  - syllabus/0606-12-2
  - syllabus/9709-1-6
  - type/theorem
  - type/formula
  - type/vocabulary
  - misconception/sign-errors-in-negative-terms
  - misconception/forgetting-coefficients
---

# Binomial Theorem 二项式定理

## Definition

### Formal

The **binomial theorem** gives the expansion of $(a + b)^n$ for any positive integer $n$:

$$(a + b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{n-r} b^r$$

Written out term by term:

$$(a + b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{n}b^n$$

where $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ is the **binomial coefficient** — the number of ways to choose $r$ items from $n$ (see [[Permutations and Combinations]]).

The expansion has exactly $n + 1$ terms, and the powers of $a$ decrease from $n$ to $0$ while the powers of $b$ increase from $0$ to $n$. In every term, the powers of $a$ and $b$ add up to $n$.

### Intuitive — It's a Counting Problem

When you expand $(a + b)^n$, you're multiplying $n$ copies of $(a + b)$ together:

$$(a + b)^n = \underbrace{(a+b)(a+b)(a+b)\cdots(a+b)}_{n \text{ copies}}$$

From each bracket, you must pick either $a$ or $b$. Every possible combination of picks gives one term. Watch what happens with $(a + b)^4$:

**Picking all $a$'s** — only 1 way to do this:
$$\underset{\uparrow}{a} \cdot \underset{\uparrow}{a} \cdot \underset{\uparrow}{a} \cdot \underset{\uparrow}{a} = a^4 \qquad \text{→ coefficient } \binom{4}{0} = 1$$

**Picking exactly 1 $b$** — which bracket does $b$ come from? 4 choices:
$$\underset{\uparrow}{b} \cdot a \cdot a \cdot a, \quad a \cdot \underset{\uparrow}{b} \cdot a \cdot a, \quad a \cdot a \cdot \underset{\uparrow}{b} \cdot a, \quad a \cdot a \cdot a \cdot \underset{\uparrow}{b}$$
All four give the same product $a^3b$ → coefficient $\binom{4}{1} = 4$

**Picking exactly 2 $b$'s** — which 2 brackets? $\binom{4}{2} = 6$ ways:
$$bb\,aa, \quad ba\,ba, \quad ba\,ab, \quad ab\,ba, \quad ab\,ab, \quad aa\,bb$$
All six give $a^2b^2$ → coefficient $\binom{4}{2} = 6$

And so on for 3 $b$'s ($\binom{4}{3} = 4$) and 4 $b$'s ($\binom{4}{4} = 1$).

In general: choosing $b$ from exactly $r$ of the $n$ brackets gives the product $a^{n-r}b^r$, and there are $\binom{n}{r}$ ways to pick which $r$ brackets contribute the $b$.

> [!question] "But wait — doesn't order matter? Why Combination, not Permutation?"
> Look at the 6 ways to pick 2 $b$'s listed above. Here are two of them:
>
> $$\underset{1}{b} \cdot \underset{2}{a} \cdot \underset{3}{b} \cdot \underset{4}{a} \qquad \text{and} \qquad \underset{1}{a} \cdot \underset{2}{b} \cdot \underset{3}{a} \cdot \underset{4}{b}$$
>
> The $b$'s came from different brackets (brackets 1&3 vs brackets 2&4). But multiply them out — both give exactly $a^2 b^2$. The *product* doesn't care which bracket each letter came from, because multiplication is commutative: $b \cdot a \cdot b \cdot a = a \cdot b \cdot a \cdot b = a^2b^2$.
>
> So the question is simply: "how many ways can I **mark** $r$ of the $n$ brackets?" Not "in what order do I mark them" — just "which ones." That's choosing a subset, which is exactly what $\binom{n}{r}$ counts.
>
> This same idea reappears in **binomial probability**: flip a coin $n$ times, get heads $r$ times. The probability depends on $\binom{n}{r}$ — because HHTHT and THHTH both count as "3 heads in 5 flips." Which flips were heads matters; the order you list them doesn't.

![[pascals-triangle.svg|700]]

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| binomial theorem | 二项式定理 | èr xiàng shì dìnglǐ |
| binomial | 二项式 | èr xiàng shì |
| binomial coefficient | 二项式系数 | èr xiàng shì xìshù |
| expansion | 展开式 | zhǎnkāi shì |
| general term | 通项 | tōng xiàng |
| Pascal's triangle | 杨辉三角 | Yáng Huī sānjiǎo |
| coefficient | 系数 | xìshù |
| term independent of $x$ | 与 $x$ 无关的项 | yǔ $x$ wúguān de xiàng |

> [!tip] 杨辉三角 — China got there first
> In the West, this triangle of coefficients is called "Pascal's triangle" after Blaise Pascal (1654). But Chinese mathematician **杨辉 (Yáng Huī)** published it in 1261 — nearly **400 years earlier** — in his book 《详解九章算法》. Even Yang Hui attributed it to an earlier work by **贾宪 (Jiǎ Xiàn)** from around 1050.
>
> The Chinese name 杨辉三角 is historically more accurate. The triangle's key property — each number is the sum of the two above it — was known in China centuries before Europe rediscovered it.

---

## Notation

| Symbol | Meaning | Also written as |
|--------|---------|-----------------|
| $\binom{n}{r}$ | Binomial coefficient: "$n$ choose $r$" | ${}^nC_r$ or $C_r^n$ |
| $(a + b)^n$ | A binomial raised to the $n$th power | |
| $T_{r+1}$ | The $(r+1)$th term of the expansion | $\binom{n}{r}a^{n-r}b^r$ |

> [!warning] The general term is $T_{r+1}$, not $T_r$
> The term with $b^r$ is the $(r+1)$th term (because we start counting from $r = 0$). When a question asks for "the 4th term", that's $r = 3$:
>
> $$T_4 = \binom{n}{3}a^{n-3}b^3$$
>
> Off-by-one errors here are one of the most common exam mistakes.

---

## Key Facts

### Pascal's Triangle 杨辉三角

Each row gives the binomial coefficients for that power of $n$:

| $n$ | Coefficients | Expansion |
|-----|-------------|-----------|
| 0 | 1 | $1$ |
| 1 | 1, 1 | $a + b$ |
| 2 | 1, 2, 1 | $a^2 + 2ab + b^2$ |
| 3 | 1, 3, 3, 1 | $a^3 + 3a^2b + 3ab^2 + b^3$ |
| 4 | 1, 4, 6, 4, 1 | $a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$ |
| 5 | 1, 5, 10, 10, 5, 1 | $a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$ |

**The rule:** each entry is the sum of the two entries directly above it. Formally, this is **Pascal's rule**:

$$\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$$

Why? To choose $r$ items from $n$, either you include the $n$th item (then choose $r - 1$ from the remaining $n - 1$) or you exclude it (then choose $r$ from $n - 1$).

### The general term

The $(r+1)$th term of $(a + b)^n$ is:

$$T_{r+1} = \binom{n}{r} a^{n-r} b^r \qquad \text{where } 0 \leq r \leq n$$

This is the single most useful formula for exam questions. To find a specific term, you substitute $a$, $b$, $n$, and $r$.

### Symmetry of coefficients

$$\binom{n}{r} = \binom{n}{n-r}$$

The coefficients are symmetric: the first and last are equal, the second and second-to-last are equal, and so on. This is because choosing $r$ items to include is the same as choosing $n - r$ items to exclude.

### Special cases

| Expansion | Result |
|-----------|--------|
| $(1 + x)^n$ | $1 + nx + \binom{n}{2}x^2 + \binom{n}{3}x^3 + \cdots + x^n$ |
| $(1 - x)^n$ | $1 - nx + \binom{n}{2}x^2 - \binom{n}{3}x^3 + \cdots + (-1)^n x^n$ |
| $(a + b)^2$ | $a^2 + 2ab + b^2$ |
| $(a - b)^2$ | $a^2 - 2ab + b^2$ |
| $(a + b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |

> [!note] Signs alternate when $b$ is negative
> In $(a - b)^n$, treat it as $(a + (-b))^n$. The term $(-b)^r = (-1)^r b^r$, so terms with odd $r$ are negative and terms with even $r$ are positive. This is the most common source of sign errors.

### Sum of binomial coefficients

Setting $a = b = 1$ in the theorem:

$$(1 + 1)^n = \sum_{r=0}^{n} \binom{n}{r} = 2^n$$

The sum of all binomial coefficients in row $n$ is $2^n$. This makes sense: each of the $n$ brackets contributes either $a$ or $b$, giving $2^n$ total paths.

---

## Misconceptions

### 1. Sign errors with negative terms

When expanding $(2x - 3)^5$, students often forget that $b = -3$ (not $3$), so every odd power of $b$ is negative.

**Fix:** Always identify $a$ and $b$ *including the sign* before expanding. Write $b = -3$ explicitly, then $(-3)^r$ handles the sign automatically:

$$T_{r+1} = \binom{5}{r}(2x)^{5-r}(-3)^r$$

### 2. Forgetting the coefficient inside the bracket

In $(2x + 3)^4$, $a = 2x$ — not $x$. The coefficient 2 must be raised to the power as well:

$$T_{r+1} = \binom{4}{r}(2x)^{4-r}(3)^r = \binom{4}{r} \cdot 2^{4-r} \cdot x^{4-r} \cdot 3^r$$

**Fix:** Always write $a$ and $b$ as entire expressions, then apply the exponent to the whole expression, not just the variable.

### 3. Off-by-one on the general term

"Find the 4th term" means $r = 3$ (since the first term has $r = 0$). Students who set $r = 4$ get the 5th term instead.

**Fix:** The term with $b^r$ is term number $r + 1$. So if you want term $k$, set $r = k - 1$.

### 4. "Pascal's triangle is only for small $n$"

Pascal's triangle is useful for quick expansion when $n \leq 6$ or so, but the binomial theorem formula works for *any* positive integer $n$. For $n = 20$, use the formula — don't try to build 20 rows of the triangle.

---

## Worked Examples

### Example 1 — Expand using Pascal's triangle (9260 A4 Ext / 0606 12.1)

Expand $(x + 3)^4$.

From Pascal's triangle, row $n = 4$: coefficients are $1, 4, 6, 4, 1$.

$$(x + 3)^4 = 1 \cdot x^4 \cdot 3^0 + 4 \cdot x^3 \cdot 3^1 + 6 \cdot x^2 \cdot 3^2 + 4 \cdot x^1 \cdot 3^3 + 1 \cdot x^0 \cdot 3^4$$

$$= x^4 + 12x^3 + 54x^2 + 108x + 81$$

**Check:** substitute $x = 1$: $(1 + 3)^4 = 256$. Sum of coefficients: $1 + 12 + 54 + 108 + 81 = 256$. ✓

---

### Example 2 — Finding a specific coefficient (0606 12.2)

Find the coefficient of $x^3$ in the expansion of $(3x - 2)^5$.

**Identify:** $a = 3x$, $b = -2$, $n = 5$.

**General term:**

$$T_{r+1} = \binom{5}{r}(3x)^{5-r}(-2)^r = \binom{5}{r} \cdot 3^{5-r} \cdot x^{5-r} \cdot (-2)^r$$

**Find $r$:** We need $x^3$, so $5 - r = 3$, giving $r = 2$.

$$T_3 = \binom{5}{2} \cdot 3^3 \cdot x^3 \cdot (-2)^2 = 10 \cdot 27 \cdot x^3 \cdot 4 = 1080x^3$$

**The coefficient of $x^3$ is $\mathbf{1080}$.**

---

### Example 3 — Term independent of $x$ (0606 12.2)

Find the term independent of $x$ in the expansion of $\left(2x + \dfrac{1}{x}\right)^{10}$.

**Identify:** $a = 2x$, $b = \dfrac{1}{x} = x^{-1}$, $n = 10$.

**General term:**

$$T_{r+1} = \binom{10}{r}(2x)^{10-r}\left(\dfrac{1}{x}\right)^r = \binom{10}{r} \cdot 2^{10-r} \cdot x^{10-r} \cdot x^{-r}$$

$$= \binom{10}{r} \cdot 2^{10-r} \cdot x^{10-2r}$$

**"Independent of $x$"** means the power of $x$ is zero: $10 - 2r = 0$, so $r = 5$.

$$T_6 = \binom{10}{5} \cdot 2^5 = 252 \cdot 32 = 8064$$

**The term independent of $x$ is $\mathbf{8064}$.**

---

### Example 4 — Expanding three binomials (9260 A4 Ext)

Expand $(x + 1)(x + 2)(x + 3)$.

This is the 9260-level version: no binomial theorem formula needed, just systematic bracket expansion.

**Step 1:** Expand the first two brackets:

$$(x + 1)(x + 2) = x^2 + 2x + x + 2 = x^2 + 3x + 2$$

**Step 2:** Multiply by the third bracket:

$$(x^2 + 3x + 2)(x + 3)$$

$$= x^3 + 3x^2 + 3x^2 + 9x + 2x + 6$$

$$= x^3 + 6x^2 + 11x + 6$$

**Check:** substitute $x = 0$: $(1)(2)(3) = 6$, and the constant term is $6$. ✓

---

## Exam Notes

### Memorise? — per board

The four-board exam-strategy table for the binomial theorem. Same legend as [[Standard Integrals]]: ✅ given on booklet, 📝 must memorise, 🛠 derive, ⚪ off-syllabus. Sources: [[MF19 Reference (9709)]], [[Edexcel IAL Reference]], [[OxAQA 9660 Reference]], [[AP Calculus Reference]].

| Form | 9709 | IAL | 9660 | AP |
|---|:---:|:---:|:---:|:---:|
| **Binomial coefficient** $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ | ✅ | ✅ | ✅ | 📝 |
| **Binomial $(a+b)^n$ for $n \in \mathbb{N}$** | ✅ | ✅ | ✅ | 📝 |
| **Binomial $(1+x)^n$ for rational $n$** ($\lvert x \rvert < 1$) | ✅ | ✅ | ✅ | ⚪ off-syllabus AB; 🛠 BC |
| **Maclaurin series for $(1+x)^n$ general** | ⚪ 9231 only | ⚪ FP2 only | ✅ on Maclaurin section | 📝 BC |
| **Pascal's triangle** | 📝 (geometric) | 📝 | 📝 | 📝 |

> [!info] Every board with a sheet gives the binomial — except for the rational-$n$ generalisation
> The basic positive-integer binomial $(a+b)^n$ is on every booklet (9709, IAL, 9660). The *rational-$n$* form $(1+x)^n$ with convergence is also on all three booklets. AP doesn't have it on AB and treats it as a Maclaurin expansion at BC. The convergence condition $\lvert x \rvert < 1$ — load-bearing for using rational-$n$ binomial in any limit / series problem — is given alongside the formula on every booklet that includes the formula.
>
> **Pascal's triangle never makes it onto a booklet** because it's a *visual* fact, not a formula. Memorise the construction (each entry = sum of two above) for any board.

---

### 9260

- **A4 Extension:** "expanding two or three binomials" — this means multiplying out $(ax + b)(cx + d)$ or $(ax + b)(cx + d)(ex + f)$ by hand. The full binomial theorem with $\binom{n}{r}$ is **not** in the 9260 spec, but understanding it helps with bracket expansion and connects to the Power Rule proof.

### 0606 (12.1, 12.2)

- **12.1:** Expand $(a + b)^n$ for positive integer $n$. The formula $(a+b)^n = \sum \binom{n}{r}a^{n-r}b^r$ is given in the formula sheet. You must simplify coefficients fully.
- **12.2:** Use the general term $\binom{n}{r}a^{n-r}b^r$ to find specific terms — the syllabus's own example is *the term independent of $x$ in $\left(2x + \tfrac{1}{x}\right)^{10}$*. Classic phrasings: "find the coefficient of $x^k$", "find the term independent of $x$", "find the constant term".

### Cambridge 9709 — Pure 1, §1.6 Series

- **Use the expansion of $(a+b)^n$, where $n$ is a positive integer**, "including the notations $\binom{n}{r}$ and $n!$" — the same content as 0606 §12, one year on, and MF19 prints the expansion (see the table above). The syllabus states explicitly that **"knowledge of the greatest term and properties of the coefficients are not required."**
- The rational-$n$ expansion $(1+x)^n$ with $\lvert x \rvert < 1$ is Pure 3 material — [[Binomial Series]].

### IB AA

- **SL 1.9** — the binomial theorem for $n \in \mathbb{N}$, with $\binom{n}{r}$ from Pascal's triangle or technology; **AHL 1.10** extends to fractional and negative $n$, the territory of [[Binomial Series]].

### Common exam phrasing

| Exam says | They want |
|-----------|-----------|
| "Expand $(2x + 3)^4$" | Write out all terms, fully simplified |
| "Find the coefficient of $x^3$ in $(...)^n$" | Use general term; find $r$ that gives $x^3$; compute the coefficient |
| "Find the term independent of $x$" | Set the power of $x$ to zero; solve for $r$ |
| "Find the constant term" | Same as "independent of $x$" — the term with no $x$ |
| "Find the first three terms in ascending powers of $x$" | The terms with $x^0$, $x^1$, $x^2$ (i.e. $r = 0, 1, 2$ when $a$ is the constant) |

---

## Connections

### Prerequisites
- **[[Permutations and Combinations]]** — $\binom{n}{r}$ is defined here; Pascal's rule is proved here
- **[[Factorial Notation]]** — $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$

### Leads to
- **[[Power Rule]]** — the proof that $\dfrac{d}{dx}(x^n) = nx^{n-1}$ uses the binomial expansion of $(x+h)^n$
- **[[Arithmetic Progressions]]** and **[[Geometric Progressions]]** — the next topics in the 0606 Series chapter
- **[[Taylor Series]]** — the generalised binomial series is a special case of Taylor series; this connection is explored at university level

### Related cards
- **[[Counting Problems]]** — $\binom{n}{r}$ appears as the coefficient because expanding $(a+b)^n$ is a counting problem
- **[[Set]]** — the number of subsets of a set with $n$ elements is $\sum_{r=0}^n \binom{n}{r} = 2^n$

---

## Beyond Syllabus

### AP / IB / A-Level depth

**Why does Pascal's rule work? — a combinatorial proof**

We want to show: $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$.

Imagine $n$ people. You want to choose a team of $r$. Focus on one specific person — call them Person $A$.

- **If Person A is on the team:** choose the remaining $r - 1$ from the other $n - 1$ people → $\binom{n-1}{r-1}$ ways.
- **If Person A is not on the team:** choose all $r$ from the other $n - 1$ people → $\binom{n-1}{r}$ ways.

These two cases are mutually exclusive and cover all possibilities, so:

$$\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r} \qquad \square$$

This is more than a formula — it's the *reason* Pascal's triangle works. Every entry is built from the two above it because every selection either includes or excludes one particular element.

**The binomial theorem proves the Power Rule**

In the [[Power Rule]] card, the proof for positive integer $n$ expands $(x+h)^n$ using the binomial theorem:

$$(x + h)^n = x^n + nx^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \cdots + h^n$$

Subtracting $x^n$, dividing by $h$, and taking $h \to 0$ kills every term except $nx^{n-1}$. Without the binomial theorem, we couldn't prove the power rule algebraically — making this theorem a cornerstone of calculus.

**Binomial probability — the binomial distribution**

If an event has probability $p$ of success on each trial, and you run $n$ independent trials, the probability of exactly $r$ successes is:

$$P(X = r) = \binom{n}{r} p^r (1-p)^{n-r}$$

This is the **binomial distribution** (二项分布) — the most important discrete probability distribution in statistics. The $\binom{n}{r}$ counts the number of ways $r$ successes can be arranged among $n$ trials (exactly the "which brackets contribute $b$?" argument from the intuitive section — with "success" playing the role of $b$).

This appears in Cambridge A-Level Mathematics (Statistics component), AP Statistics, and IB Mathematics. The formula is typically provided on the formula sheet — the key skill is recognising when a situation follows the binomial model (fixed $n$, independent trials, constant $p$, two outcomes).

**Newton's generalised binomial theorem (9709 P3 §3.1 / A-Level / IB AA / AP — beyond 0606)**

The binomial theorem as stated above requires $n$ to be a positive integer. Isaac Newton extended it to **any real exponent** $\alpha$ (including negative and fractional values). This generalised series is *in scope* for **9709 Paper 3 §3.1**, A-Level Pure Mathematics, IB AA HL, and AP Calculus BC — even though it falls beyond 0606. Cambridge A-Level lists it on the formula sheet (see callout below):

$$(1 + x)^\alpha = \sum_{r=0}^{\infty} \binom{\alpha}{r} x^r = 1 + \alpha x + \dfrac{\alpha(\alpha - 1)}{2!}x^2 + \dfrac{\alpha(\alpha - 1)(\alpha - 2)}{3!}x^3 + \cdots$$

where $\binom{\alpha}{r} = \dfrac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-r+1)}{r!}$ (no factorial in the numerator — $\alpha$ isn't a non-negative integer).

This expansion is an **infinite series** (it never terminates unless $\alpha$ is a non-negative integer), and it converges only when $|x| < 1$. For example:

$$\dfrac{1}{1+x} = (1+x)^{-1} = 1 - x + x^2 - x^3 + \cdots \qquad |x| < 1$$

$$\sqrt{1+x} = (1+x)^{1/2} = 1 + \dfrac{1}{2}x - \dfrac{1}{8}x^2 + \dfrac{1}{16}x^3 - \cdots \qquad |x| < 1$$

> [!important] This is on the Cambridge A-Level formula sheet
> A-Level students need to be familiar with the generalised formula and apply it for specific cases (usually expanding $(1 + x)^\alpha$ up to 3–4 terms). The key skill: identify $\alpha$ and $x$, substitute into the formula, and state the validity condition $|x| < 1$.
>
> For expressions like $(2 + 3x)^{-1}$, first factor out: $2^{-1}(1 + \frac{3x}{2})^{-1}$, then apply the formula with $x \to \frac{3x}{2}$. The validity condition becomes $\left\lvert\frac{3x}{2}\right\rvert < 1$, i.e. $|x| < \frac{2}{3}$.

Newton's generalised theorem is used throughout analysis and physics (approximations like $\sqrt{1 + \epsilon} \approx 1 + \dfrac{\epsilon}{2}$ for small $\epsilon$).

**Taylor series — the ultimate generalisation**

The generalised binomial theorem writes $(1+x)^\alpha$ as an infinite power series. But why stop at powers? **[[Taylor Series]]** generalise this to *any* smooth function:

$$f(x) = \sum_{n=0}^{\infty} \dfrac{f^{(n)}(a)}{n!}(x - a)^n = f(a) + f'(a)(x-a) + \dfrac{f''(a)}{2!}(x-a)^2 + \cdots$$

The binomial series is the Taylor series of $f(x) = (1+x)^\alpha$ centred at $a = 0$. Every function you know — $e^x$, $\sin x$, $\ln(1+x)$ — has a Taylor series, and they all look like the binomial expansion with different coefficients. This is AP Calculus BC (Unit 10) and IB Mathematics AA HL.

### Beyond high school — University

**杨辉三角 in history — a timeline**

| Year | Mathematician | Contribution |
|------|--------------|-------------|
| ~450 | **Pingala** (India) | Binary combinations in Sanskrit prosody — effectively $\binom{n}{r}$ |
| ~1050 | **贾宪 Jiǎ Xiàn** (China) | Tabulated binomial coefficients for extracting roots |
| 1261 | **杨辉 Yáng Huī** (China) | Published the triangle in 《详解九章算法》 |
| 1303 | **朱世杰 Zhū Shìjié** (China) | Extended the triangle to higher powers in 《四元玉鉴》 |
| 1527 | **Petrus Apianus** (Germany) | First European printing of the triangle |
| 1654 | **Blaise Pascal** (France) | Systematic study of properties; connected to probability theory |
| 1665 | **Isaac Newton** (England) | Generalised to non-integer exponents |

The mathematical ideas travelled from India through China to the Islamic world to Europe over more than a millennium. The name "Pascal's triangle" reflects European historiography, not chronological priority.

---

## LaTeX Reference

| Notation | LaTeX | Rendered |
|----------|-------|----------|
| Binomial coefficient | `\binom{n}{r}` | $\binom{n}{r}$ |
| Expansion | `(a+b)^n` | $(a+b)^n$ |
| General term | `\binom{n}{r}a^{n-r}b^r` | $\binom{n}{r}a^{n-r}b^r$ |
| Sum notation | `\sum_{r=0}^{n}` | $\sum_{r=0}^{n}$ |
| Pascal's rule | `\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}` | $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ |
| Generalised coefficient | `\dfrac{\alpha(\alpha-1)\cdots(\alpha-r+1)}{r!}` | $\dfrac{\alpha(\alpha-1)\cdots(\alpha-r+1)}{r!}$ |

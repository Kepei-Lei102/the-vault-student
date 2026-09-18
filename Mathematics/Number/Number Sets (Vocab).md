---
chinese: 数集 (shùjí)
prerequisites:
  - "[[Set]]"
  - "[[Factors and Multiples (Vocab)]]"
  - "[[Recurring Decimals (Vocab)]]"
leads_to:
  - "[[Surds]]"
  - "[[Complex Numbers]]"
  - "[[Prime Numbers]]"
  - "[[Natural Numbers]]"
  - "[[Integers]]"
  - "[[Decimals (Vocab)]]"
  - "[[Ordering and Inequalities Notation (Vocab)]]"
  - "[[Set-Builder Notation]]"
  - "[[Cantor vs Kronecker]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/OxAQA-9260
  - syllabus/9260-N4
  - syllabus/0580-E1-1
  - type/vocabulary
  - type/reference
  - notation/N-Z-Q-R
  - misconception/sqrt2-rational
  - misconception/decimal-implies-rational
---

# Number Sets 数集

## Definition

Mathematics builds its number system in a tower. Each level adds something the level below couldn't do, and each level *contains* every level below it as a subset:

$$\mathbb{N} \;\subset\; \mathbb{Z} \;\subset\; \mathbb{Q} \;\subset\; \mathbb{R} \;\subset\; \mathbb{C}.$$

| Symbol | Name | What's in it |
|---|---|---|
| $\mathbb{N}$ | **Natural numbers** | $0, 1, 2, 3, \ldots$ — the counting numbers (some authors start at $1$; check the source's convention) |
| $\mathbb{Z}$ | **Integers** | $\ldots, -2, -1, 0, 1, 2, \ldots$ — naturals plus their negatives |
| $\mathbb{Q}$ | **Rational numbers** | every $\dfrac{p}{q}$ with $p, q \in \mathbb{Z}$ and $q \ne 0$ — the *fractions* |
| $\mathbb{R}$ | **Real numbers** | every point on the number line — rationals plus *irrationals* like $\sqrt{2}$, $\pi$, $e$ |
| $\mathbb{C}$ | **Complex numbers** | every $a + bi$ with $a, b \in \mathbb{R}$ — beyond 0580/0606 syllabus, see [[Complex Numbers]] |

A separate "set" of importance: **prime numbers** $\mathbb{P} = \{2, 3, 5, 7, 11, 13, \ldots\}$ — natural numbers greater than 1 with exactly two divisors ($1$ and themselves). $\mathbb{P} \subset \mathbb{N}$ but is not a "level" of the tower; it's an important subset.

### 中文锚点

数苹果时，一、二、三就够用了；可要记下“还欠朋友两元”，就得让负数出场。一个蛋糕分给三个人，每人拿三分之一，光靠一个一个地数又不够了。自然数、整数、有理数这些名字，背后是同一件事：遇到原来的数说不清的问题，就把能用的数扩充一些。新工具也不会把旧工具赶走——二仍然是二，也可以写成一分之二。所以这些数集不是互不相干的几个盒子，而是一层套着一层；关键是看眼前的问题，需要哪一套数才说得清。

---

## Building the Tower — formal definitions

Each level of the number system is *defined* in terms of the level below. This isn't a stylistic choice — many things that *feel* obvious about numbers actually require a definition before they can be reasoned about. Watch how each definition leans on the one above it.

### Natural numbers $\mathbb{N}$

$$\mathbb{N} = \{0, 1, 2, 3, \ldots\}.$$

The **counting numbers**: start at $0$, and you can always add $1$ to get the next one (the "successor"). Closed under addition and multiplication — sum or product of two naturals is always a natural. *Not* closed under subtraction: $3 - 5$ falls outside $\mathbb{N}$. (The fully axiomatic construction via *Peano's axioms* is one level deeper still — see [[Natural Numbers]].)

### Integers $\mathbb{Z}$

$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\} = \mathbb{N} \cup \{-1, -2, -3, \ldots\}.$$

The **integers** extend $\mathbb{N}$ to make subtraction always work. Once $-3, -5, \ldots$ exist, $3 - 5 = -2$ is a legal answer. Closed under $+$, $-$, $\times$. *Not* closed under division: $3 \div 5$ falls outside. (The construction "$\mathbb{Z}$ from $\mathbb{N}$" — and the famous derivation of $(-1)\times(-1) = 1$ — lives in [[Integers]].)

### Rational numbers $\mathbb{Q}$

$$\mathbb{Q} = \left\{\frac{a}{b} \;:\; a, b \in \mathbb{Z},\; b \ne 0\right\}.$$

A **rational number** is *any number expressible as $a/b$ where $a$ and $b$ are integers and $b \ne 0$.* This is the official definition — read it carefully, because the next section's proof depends on it word-for-word.

So defining $\mathbb{Q}$ requires already having $\mathbb{Z}$, which requires already having $\mathbb{N}$. The tower is built in order; each level is meaningless until the level below exists.

$\mathbb{Q}$ is closed under $+$, $-$, $\times$, $\div$ (except division by $0$). It's the smallest *field* containing $\mathbb{Z}$ — every arithmetic operation works.

### Real numbers $\mathbb{R}$

The reals extend the rationals by **filling in the gaps**: every point on the number line gets a number. This includes irrational numbers like $\sqrt{2}, \pi, e$ that *cannot* be written as $a/b$ for integers $a, b$.

Formalising "the gaps" rigorously is non-trivial — it's the construction of $\mathbb{R}$ via *Dedekind cuts* or *Cauchy sequences*, which is undergraduate-level. At 0580 we just use the intuition: the real line has no holes, every length on the line is a real number.

### Complex numbers $\mathbb{C}$

$$\mathbb{C} = \{a + bi \;:\; a, b \in \mathbb{R}\}, \quad i^2 = -1.$$

Beyond 0580/0606. See [[Complex Numbers]]. Adds square roots of negative numbers, completing one more layer.

> [!info] Many "obvious" facts about numbers actually need a proof
> The point of this card isn't to be pedantic — it's to set up a habit. **Throughout maths, intuitive ideas need definitions, and definitions need proofs.** "$\sqrt{2}$ is irrational" *feels* like an assertion that doesn't need defending. The next section shows why it does, and how the *exact wording* of the definition of $\mathbb{Q}$ is what makes the proof go through. The vault's spirit: rigour and intuition together. Definitions get stated; proofs get given.

---

## Key Vocabulary

| English | 中文 | Definition |
|---------|------|------------|
| natural number | 自然数 | counting number; non-negative integer |
| integer | 整数 | whole number, positive, negative, or zero |
| rational number | 有理数 | expressible as $p/q$ with integer $p, q$ and $q \ne 0$ |
| irrational number | 无理数 | real but not rational; non-terminating non-repeating decimal |
| real number | 实数 | any point on the number line |
| prime number | 质数 / 素数 | natural number $> 1$ with exactly two divisors |
| composite number | 合数 (héshù) | natural number $> 1$ that's not prime |
| transcendental number | 超越数 (chāoyuèshù) | irrational AND not the root of any polynomial with integer coefficients (e.g., $\pi$, $e$) |
| algebraic number | 代数数 (dàishùshù) | a root of some polynomial with integer coefficients (e.g., $\sqrt{2}$, $\sqrt[3]{5}$) |

---

## How To Tell If A Number Is Rational

A real number is **rational** if and only if its decimal expansion **terminates** (e.g. $0.25$) or **eventually repeats** (e.g. $0.\overline{142857} = 1/7$). Otherwise, it's **irrational**.

| Decimal | Rational? | Why |
|---|---|---|
| $0.25$ | ✓ | Terminates → $1/4$ |
| $0.\overline{3}$ | ✓ | Repeats → $1/3$ (see [[Recurring Decimals (Vocab)\|Recurring Decimals]] for the conversion trick) |
| $0.121212\ldots$ | ✓ | Repeats → $4/33$ |
| $0.10110011100011110000\ldots$ | ✗ | Never settles into a repeating pattern (this is one of Liouville's irrational constructions) |
| $\pi = 3.14159265\ldots$ | ✗ | No repeating pattern (Lambert proved this in 1761) |
| $e = 2.71828\ldots$ | ✗ | No repeating pattern (Euler proved this in 1737) |
| $\sqrt{2} = 1.41421356\ldots$ | ✗ | Classic irrationality proof below |

> [!warning] "Decimal representation" alone doesn't decide rationality
> A non-terminating decimal might *still* be rational if it eventually repeats — like $0.\overline{142857}$. The distinguishing test is **periodicity in the tail**, not just length. Calculator outputs that look "random" might be a repeating decimal too long for the screen to show.

---

## The √2 Irrationality Proof (Pythagoras's school, ~500 BC)

This is the **classical first proof of irrationality** in the history of mathematics. The technique is **proof by contradiction** (see [[Proof by Contradiction]]) — assume the *opposite* of what you want to prove (that $\sqrt{2}$ *is* rational), follow the consequences, and arrive at a logical impossibility. That impossibility forces the original assumption to be false, which proves the theorem.

**Theorem.** $\sqrt{2}$ is irrational.

**Proof.** Suppose, for contradiction, that $\sqrt{2}$ is rational. Then **by the definition of $\mathbb{Q}$ above**, we can write

$$\sqrt{2} = \frac{p}{q}$$

for some integers $p, q$ with $q \ne 0$, where the fraction is in **lowest terms** (i.e., $p$ and $q$ share no common factor — we can always reduce to lowest terms).

Squaring both sides:

$$2 = \frac{p^2}{q^2} \;\;\Longrightarrow\;\; p^2 = 2 q^2.$$

So $p^2$ is even (it's twice $q^2$). But the square of an *odd* number is odd, so $p$ itself must be even. Write $p = 2k$ for some integer $k$:

$$(2k)^2 = 2q^2 \;\;\Longrightarrow\;\; 4k^2 = 2q^2 \;\;\Longrightarrow\;\; q^2 = 2k^2.$$

So $q^2$ is also even, which means $q$ is even.

But now both $p$ and $q$ are even — they share the factor $2$. This **contradicts** our assumption that $p/q$ was in lowest terms.

The assumption that $\sqrt{2}$ is rational must be false. Therefore $\sqrt{2}$ is irrational. $\blacksquare$

> [!info] Legend says this proof got someone killed
> Pythagoras's school (~500 BC) believed all quantities in the universe were ratios of whole numbers — that this was *the* deep truth of mathematics. The discovery that $\sqrt{2}$ (the diagonal of a unit square — a *geometric* quantity) is *not* expressible as a ratio shattered this belief. The legend (probably apocryphal but persistently retold) is that **Hippasus**, the Pythagorean who first announced the proof, was thrown overboard by his fellow disciples to keep the secret. Whether or not that's true, the discovery did force a fundamental rethinking of what "number" means — and gave mathematics its first non-rational quantity.
>
> The proof technique — *assume rational, find shared factor, contradiction* — generalises to show $\sqrt{p}$ is irrational for *every* prime $p$. The same template proves $\sqrt[3]{2}$ is irrational, with cubes instead of squares. See [[Surds]] for the irrationality of surd-like expressions in general.

---

## Transcendental vs Algebraic — beyond syllabus, beautiful

Within the irrationals, there's a finer distinction:

- **Algebraic number**: a real number that is a *root of some polynomial* with integer coefficients. $\sqrt{2}$ is algebraic (root of $x^2 - 2 = 0$). $\sqrt[3]{5}$ is algebraic (root of $x^3 - 5 = 0$). The golden ratio $\varphi = \tfrac{1+\sqrt 5}{2}$ is algebraic (root of $x^2 - x - 1 = 0$).
- **Transcendental number**: a real number that is *not* algebraic — no polynomial with integer coefficients has it as a root. $\pi$ is transcendental (Lindemann 1882). $e$ is transcendental (Hermite 1873). Almost every real number is transcendental, but proving any *specific* number is transcendental is famously hard.

> [!info] How can "almost every real number" be transcendental, yet so few are known?
> Cantor showed in 1874 that the set of algebraic numbers is **countable** — they can be put into a one-to-one list with $\mathbb{N}$. The set of all real numbers is **uncountable** — there's no such list, no matter how clever. So the algebraic numbers are a vanishingly small minority of $\mathbb{R}$, and picking a real number "at random" lands you on a transcendental almost surely. The full machinery — countable vs uncountable, Cantor's diagonal argument, the cardinalities $\aleph_0$ and $\mathfrak{c}$ — lives in [[Countability]].
>
> But constructing or recognising *specific* transcendentals is hard. Liouville built the first explicit transcendental in 1844 ($\sum 10^{-k!}$). Hermite proved $e$ is transcendental in 1873; Lindemann did $\pi$ in 1882. **We still don't know** whether $\pi + e$ is transcendental, or whether Euler's constant $\gamma$ is even *irrational*. The transcendentals are everywhere and almost completely unmapped.

---

## Exam Notes

### Cambridge 0580 — C1.1 / E1.1

The 2025–2027 syllabus requires identifying and using natural numbers, integers, primes, square/cube numbers, common factors/multiples, rational/irrational numbers and reciprocals. Prime factorisation, HCF and LCM also belong here. Recognising an irrational number is required; the specification does not name a general proof-by-contradiction method or prescribe the square-root irrationality proof as a separate outcome. Do not infer paper frequency or guaranteed marks from these examples.

**Original example:** a rational number between $\sqrt2$ and $\sqrt3$ is $1.5$, since $2<1.5^2<3$. A terminating decimal must still lie inside the requested interval.

### OxfordAQA 9260

**N4** covers even/odd/prime vocabulary, factors, multiples, HCF/LCM and prime factorisation; **N7** covers exact fractions and, at Extension tier, surds. The deeper construction of number systems, transcendence and infinite cardinalities are enrichment. One is neither prime nor composite; unique prime factorisation concerns integers **greater than one**.

### Cambridge 0606 and A-Level

0606 requires set language, surds and algebra, but not the axiomatic number-system constructions or Cantorian cardinalities. At A-Level, separate the qualifications: **9709** uses real-number algebra and surds; **9231** explicitly includes complex numbers and proof by induction. **Edexcel IAL** introduces complex numbers in Further Pure; its notation list defines $\mathbb N=\{1,2,3,\ldots\}$. **OxfordAQA 9660** includes surds and, in its Pure2 proof content, contradiction and counterexamples. These are not a blanket requirement to prove transcendence of $e$, study the Chinese remainder theorem or derive all number-system constructions.

### IB AA and AI

Both guides list natural/integer/rational/irrational/real number systems as prior learning. **AA HL AHL1.15** explicitly includes contradiction with irrationality examples and **AHL1.12–1.14** covers complex numbers. These placements do not require Cantor's countability argument; retain it as enrichment. AI's complex-number and matrix content has its own HL placement; see [[Complex Numbers]] for that scope. [IB AA guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf) · [IB AI guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf)

### AP Calculus AB/BC — boundary

Real-number and algebra fluency supports the course, but the inspected CED does not prescribe Peano axioms, Cantor's countability proof or proofs of transcendence. No claim is made here about a universal “AP number-systems unit”: course-specific requirements differ.

---

## Common Mistakes

1. **Thinking $\sqrt{4}$ is irrational.** $\sqrt{4} = 2$, a natural number. The square root of a *perfect square* is rational.
2. **Calling $1$ prime.** Definition says *exactly two* divisors; $1$ has only one. Not prime.
3. **"Rational" means "decimal terminates."** Not quite — *terminating or eventually repeating*. $1/3 = 0.\overline{3}$ never terminates, but it's still rational.
4. **Confusing irrational with imaginary.** Irrational ($\sqrt{2}, \pi$) lives in $\mathbb{R}$; imaginary ($i, 2 + 3i$) lives in $\mathbb{C}\setminus\mathbb{R}$. They're different "types" of non-rational.
5. **Negative naturals.** $\mathbb{N}$ does *not* include negatives — $-3$ is an integer but not a natural number.

---

## Connections

- **Forward (deep):** [[Natural Numbers]] — Peano axioms construction of $\mathbb{N}$ (axiomatic foundations)
- **Forward (deep):** [[Integers]] — extending naturals; the slick proof that $(-1)\times(-1) = 1$
- **Forward (deep):** [[Prime Numbers]] — Euclid's infinitude proof, Fundamental Theorem of Arithmetic
- **Forward:** [[Surds]] — manipulating irrational $\sqrt{n}$ expressions
- **Forward:** [[Recurring Decimals (Vocab)|Recurring Decimals]] — converting repeating decimals to fractions
- **Forward:** [[Complex Numbers]] — the level above $\mathbb{R}$
- **Forward:** [[Proof by Contradiction]] — the technique used in the $\sqrt{2}$ proof; the same template proves $\sqrt{p}$ irrational for every prime $p$
- **Forward:** [[Countability]] — Cantor's diagonal argument that $\mathbb{R}$ is "bigger" than $\mathbb{N}$, the formal sense in which "almost every real is transcendental"
- **Beyond syllabus:** *Liouville's transcendental construction*, *the still-open question whether $\pi + e$ is irrational*

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbb{N}$ | `\mathbb{N}` | Natural numbers |
| $\mathbb{Z}$ | `\mathbb{Z}` | Integers (from German *Zahlen*) |
| $\mathbb{Q}$ | `\mathbb{Q}` | Rationals (from *Quotient*) |
| $\mathbb{R}$ | `\mathbb{R}` | Reals |
| $\mathbb{C}$ | `\mathbb{C}` | Complex |
| $\mathbb{P}$ | `\mathbb{P}` | Primes (notation varies; sometimes just $\mathbb{P}$ or written out) |
| $\in, \notin$ | `\in, \notin` | Membership |
| $\subset, \subseteq$ | `\subset, \subseteq` | Subset |

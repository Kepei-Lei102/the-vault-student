---
chinese: 自然常数 e (zìrán chángshù e)
prerequisites:
  - "[[Binomial Theorem]]"
  - "[[Exponential Growth and Decay]]"
  - "[[Laws of Indices]]"
  - "[[Surds]]"
  - "[[Radians]]"
leads_to:
  - "[[Logarithms]]"
  - "[[Exponential Function]]"
  - "[[Differentiation]]"
  - "[[Integration]]"
  - "[[Complex Numbers]]"
  - "[[Differential Equations]]"
  - "[[Normal Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Proof by Contradiction]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[The Hidden Number]]"
tags:
  - subject/mathematics
  - domain/number
  - domain/analysis
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - type/deep
  - type/constant
  - type/proof
  - notation/e
  - notation/ln
  - misconception/e-is-arbitrary
  - misconception/e-stands-for-Euler
  - misconception/e-equivalent-to-other-bases
---

# Euler's Number 自然常数 e

$e \approx 2.718281828459045\ldots$ is the most famous constant in mathematics after $\pi$. It turns up in compound interest, the bell curve, rare-event statistics, the density of primes, and — spectacularly — in the most beautiful equation ever written, $e^{i\pi} + 1 = 0$. This card is the full story of *e*: where it came from, what kind of number it is, and why it keeps showing up in places that seem to have nothing to do with each other.

The companion card [[Exponential Growth and Decay]] uses $e$ as a tool; this card is about $e$ as an object.

### 中文锚点

自然常数 **$e \approx 2.71828$** —— 数学中继 $\pi$ 之后最重要的常数。它是**自然对数的底数**，即 $\ln x = \log_e x$。三种等价定义：
1. 复利极限 $e = \lim_{n\to\infty}(1+1/n)^n$
2. 无穷级数 $e = \sum_{k=0}^\infty 1/k!$
3. 微积分特征 $\dfrac{d}{dx}e^x = e^x$，且 $e^0 = 1$

$e$ 是**无理数**（1737 年欧拉证明）且**超越数**（1873 年 Hermite 证明）。这张卡片讲的是 $e$ 这个数本身的故事 —— 从 250 年的"盲人摸象"史，到它在微积分、概率、数论中无处不在的身影。

---

## 1. A short history of a shy number

The constant $e$ took **250 years** to be named. From John Napier's 1614 logarithm tables through Charles Hermite's 1873 transcendence proof, it kept showing up unannounced — five mathematicians, four countries, five independent paths all converging on the same number — before anyone realised they'd all been pointing at the same constant. Briefly:

- **1614/1618:** Napier's log tables. $e$ is the implicit base; nobody notices.
- **1647:** Saint-Vincent finds the area under $y = 1/x$ behaves like a logarithm. The base is $e$; he doesn't name it.
- **1668:** Mercator coins **"logarithmus naturalis"** — *natural logarithm* — for the function that emerges from $\int dx/x$ without anyone choosing a base.
- **1683:** Jacob Bernoulli proves $\lim_n (1+1/n)^n$ exists in the compound-interest problem; doesn't connect it to anything else.
- **1727/1748:** Euler writes $e$ for the first time, proves $e$ irrational (1737), and in *Introductio in Analysin Infinitorum* (1748) ties every previous thread together: series, compound-interest limit, hyperbolic-area base, and $e^{i\pi} + 1 = 0$.
- **1873:** Hermite proves $e$ is transcendental. Lindemann (1882) adapts the method to $\pi$, killing the 2000-year-old "squaring the circle" problem.

**The full historical drama** — including the cast-of-characters detail, the unanswered question of why the letter $e$ specifically, the side-stories of the failed circle-squarers and Leibniz's placeholder "$b$" — lives in **[[Stories/The Hidden Number]]**. That card also addresses the question *"why exactly are we calling these objects 'natural'?"* — short answer: because mathematics keeps producing them without anyone choosing them; "natural" is the technical word for *unbidden*.

---

## 2. What kind of number is $e$?

In the mathematical zoo, numbers come in nested layers:

| Layer | Definition | Example |
|-------|-----------|---------|
| $\mathbb{N}$ — naturals | $0, 1, 2, 3, \ldots$ | $7$ |
| $\mathbb{Z}$ — integers | $\ldots, -2, -1, 0, 1, 2, \ldots$ | $-3$ |
| $\mathbb{Q}$ — rationals | all ratios $p/q$ with $p, q \in \mathbb{Z}$, $q \neq 0$ | $\tfrac{22}{7}$ |
| **Algebraic numbers** | roots of polynomials with integer coefficients | $\sqrt{2}$ (root of $x^2 - 2 = 0$), $i$ (root of $x^2 + 1 = 0$), the golden ratio $\varphi$ |
| **Transcendental numbers** | NOT the root of *any* polynomial with integer coefficients | $\pi$, $e$ |

$e$ lives in the outermost layer. It is **transcendental** — a stronger statement than just irrational.

### Proof that $e$ is irrational — Euler's argument

This is one of the cleanest proofs in all of mathematics. It uses only the series definition of $e$ and a factorial trick. If you've never seen a [[Proof by Contradiction]] end so neatly, strap in.

**Setup.** Suppose, for contradiction, that $e$ **is** rational. Then we can write
$$e = \frac{p}{q}$$
for some positive integers $p, q$ with $q \geq 2$. (If $q = 1$ then $e$ would be an integer, which it clearly isn't: $2 < e < 3$.)

**Step 1 — Multiply both sides by $q!$.**
$$q! \cdot e = q! \cdot \frac{p}{q} = p \cdot (q-1)!$$

The right side is a product of integers, so it's an integer. Therefore **$q! \cdot e$ must be an integer too.** Remember this conclusion — it's what we're about to contradict.

**Step 2 — Split the series at $k = q$.** Using the series $e = \sum_{k=0}^\infty \tfrac{1}{k!}$,
$$q! \cdot e \;=\; q! \sum_{k=0}^\infty \frac{1}{k!} \;=\; \underbrace{q! \sum_{k=0}^{q} \frac{1}{k!}}_{\text{call this } X} \;+\; \underbrace{q! \sum_{k=q+1}^\infty \frac{1}{k!}}_{\text{call this } R}$$

We'll show $X$ is an integer and $0 < R < 1$ — which forces $q! \cdot e = X + R$ to be a non-integer.

**Step 3 — $X$ is an integer.** For each $k$ with $0 \leq k \leq q$, the factor $\tfrac{q!}{k!}$ equals $q \cdot (q-1) \cdots (k+1)$, a product of integers. So each term in $X$ is an integer, and a sum of integers is an integer. ✓

**Step 4 — $R$ is a positive number less than 1.** Write $R$ out:
$$R = q! \sum_{k=q+1}^\infty \frac{1}{k!} = \frac{1}{q+1} + \frac{1}{(q+1)(q+2)} + \frac{1}{(q+1)(q+2)(q+3)} + \cdots$$

(The $q!$ cancels most of each denominator — the first leftover factor is $q+1$, the second is $(q+1)(q+2)$, and so on.)

Each term is positive, and each term is strictly less than the corresponding term of the geometric series with common ratio $\tfrac{1}{q+1}$ — so:
$$R \;<\; \frac{1}{q+1} + \frac{1}{(q+1)^2} + \frac{1}{(q+1)^3} + \cdots \;=\; \frac{1/(q+1)}{1 - 1/(q+1)} \;=\; \frac{1}{q}$$

Since $q \geq 2$, we have $R < \tfrac{1}{q} \leq \tfrac{1}{2} < 1$. And $R > 0$ (it's a sum of positive numbers). So $0 < R < 1$. ✓

**Step 5 — The contradiction.** We have $q! \cdot e = X + R$ where $X$ is an integer and $0 < R < 1$. So $q! \cdot e$ equals (an integer) + (a strictly-between-0-and-1 number), which is **not an integer**. But Step 1 proved $q! \cdot e$ *is* an integer. Contradiction.

$$\boxed{\;e \text{ is irrational.}\;}$$

**Why this proof is beautiful.** It doesn't require heavy machinery — just the series definition, factorials, and a geometric-series bound. Euler could have written it on a napkin. Contrast Hermite's **transcendence** proof, which runs 20+ pages and uses auxiliary polynomials, integrals of $e^{-x}$, and a delicate inequality. Irrationality is a few strokes; transcendence is a cathedral.

### Transcendence — stated, not proved

Hermite's 1873 theorem:

> There is no non-zero polynomial $a_n x^n + a_{n-1} x^{n-1} + \cdots + a_0$ with integer coefficients $a_i \in \mathbb{Z}$ such that $a_n e^n + a_{n-1} e^{n-1} + \cdots + a_0 = 0$.

**Intuition.** If $e$ *were* algebraic — say $P(e) = 0$ for some polynomial $P$ — Hermite constructed a specific integer (involving integrals against $e^{-x}$) that, under the assumption $P(e) = 0$, would have to be both exactly zero AND strictly positive. Impossible. So $P(e) = 0$ has no solution, i.e. no such $P$ exists. The construction is delicate; getting the integer-vs-nonzero bound to work is where the 20 pages go.

> [!info] Beyond syllabus — what else is transcendental?
> After Hermite, **Lindemann (1882)** proved $\pi$ is transcendental using the same general method. **Gelfond (1934)** proved $e^\pi$ is transcendental (a famous open problem at the time). But we still don't know whether $e + \pi$, $e \cdot \pi$, $\pi^\pi$, or $\pi^e$ are transcendental — or even irrational. In a measure-theoretic sense, *almost every* real number is transcendental (the algebraic numbers are countable, the reals aren't), but proving a *specific* number is transcendental remains hard. $e$ was the first to fall; $\pi$ was the second. The list has grown slowly since.

---

## 3. Where $e$ comes from — three equivalent definitions

Mathematicians have three independent ways to pin down $e$. Each was discovered separately, for different reasons, and each uniquely determines the same number. The fact that three unrelated roads meet at the same constant is the deepest reason $e$ deserves a name.

### Definition 1 — The compound-interest limit (Bernoulli, 1683)

$$\boxed{\;e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n\;}$$

This is the form [[Exponential Growth and Decay]] stumbles onto when compounding more and more frequently. Compute $(1 + 1/n)^n$ for a few $n$:

| $n$ | $(1 + 1/n)^n$ |
|-----|-------------|
| 1 | 2 |
| 10 | 2.5937 |
| 100 | 2.7048 |
| 1,000 | 2.7169 |
| 1,000,000 | 2.71828 |
| $\to \infty$ | $e = 2.71828\ldots$ |

The full proof that this limit exists and equals the number we call $e$ has four steps. It uses the **binomial theorem** to rewrite the sequence in a tractable form, the **Monotone Convergence Theorem** (every increasing real sequence that's bounded above converges), and the [[Squeeze Theorem]] applied to a two-sided bound. It is the cleanest convergence proof in introductory analysis.

#### Proof that $\lim_{n \to \infty}(1 + 1/n)^n$ exists and equals $\sum_{k=0}^\infty 1/k!$

Write $a_n = (1 + 1/n)^n$. By the binomial theorem:

$$a_n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k} = \sum_{k=0}^n \frac{1}{k!} \cdot \frac{n(n-1)(n-2)\cdots(n-k+1)}{n^k} = \sum_{k=0}^n \frac{1}{k!} \prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right).$$

That last form — each term is $\frac{1}{k!}$ multiplied by a finite product of factors $(1 - j/n)$ — is the key. Every move below comes from inspecting that product.

**Step 1 — The sequence is increasing.** Compare term $k$ at $n$ versus term $k$ at $n+1$:

$$\frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n+1}\right) \;>\; \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right) \quad \text{for } k \geq 1$$

because for any $j > 0$, the factor $1 - j/(n+1)$ is *larger* than $1 - j/n$ (the subtracted piece is smaller when the denominator is larger). Moreover, $a_{n+1}$ has **one more positive term** than $a_n$ — the $k = n+1$ term, which is positive. So $a_{n+1} > a_n$ termwise *and* in total length. The sequence strictly increases. ✓

**Step 2 — The sequence is bounded above by 3.** Each factor $(1 - j/n) \leq 1$, so:

$$a_n \;\leq\; \sum_{k=0}^n \frac{1}{k!}.$$

For $k \geq 1$, $k! = 1 \cdot 2 \cdot 3 \cdots k \geq 1 \cdot 2 \cdot 2 \cdots 2 = 2^{k-1}$ (replacing every factor from $3$ onward with $2$, which is smaller). So $1/k! \leq 1/2^{k-1}$, and:

$$a_n \;\leq\; 1 + \sum_{k=1}^n \frac{1}{2^{k-1}} \;<\; 1 + \sum_{k=1}^\infty \frac{1}{2^{k-1}} \;=\; 1 + 2 \;=\; 3.$$

The geometric series telescopes cleanly. ✓

**Step 3 — Apply the Monotone Convergence Theorem.** An increasing sequence in $\mathbb{R}$ that's bounded above converges to its supremum. Combining Steps 1 and 2: $a_n$ converges. Call the limit $L$. From $a_1 = 2$ (the start of the increase) and $a_n < 3$ (the bound), we already know $2 \leq L \leq 3$. ✓

**Step 4 — The limit equals $\sum_{k=0}^\infty 1/k!$.** This is the squeeze-style step. We bound $L$ above and below by the partial sums of the series, then take the bound to its limit.

*Upper bound:* From Step 2, $a_n \leq \sum_{k=0}^n 1/k! \leq \sum_{k=0}^\infty 1/k!$. Taking $n \to \infty$:

$$L \;\leq\; \sum_{k=0}^\infty \frac{1}{k!}.$$

*Lower bound:* Fix any integer $K \geq 0$. For all $n \geq K$:

$$a_n \;\geq\; \sum_{k=0}^K \frac{1}{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$$

(we're keeping only the first $K+1$ terms of the full sum, which is fine because every term is positive). Now take $n \to \infty$ on this finite sum: each factor $(1 - j/n) \to 1$, so each term $\to 1/k!$. Therefore:

$$L \;=\; \lim_{n \to \infty} a_n \;\geq\; \sum_{k=0}^K \frac{1}{k!}.$$

This holds for *every* $K$, so taking $K \to \infty$:

$$L \;\geq\; \sum_{k=0}^\infty \frac{1}{k!}.$$

Combining the upper and lower bounds: $L = \sum_{k=0}^\infty 1/k!$. The limit *exists* (from MCT) and *equals* the infinite series (from the two-sided squeeze). $\blacksquare$

This is the full justification of "Definition 1 ↔ Definition 2." Bernoulli proved Step 3 in 1683 (the limit exists, between 2 and 3); the four-step argument as a whole is the modern presentation that became standard once real analysis was formalised in the 19th century.

### Definition 2 — The infinite series (Euler, 1748)

$$\boxed{\;e = \sum_{k=0}^\infty \frac{1}{k!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} + \frac{1}{720} + \cdots\;}$$

This is the best form for **computing** decimal expansions. The factorials in the denominator grow so fast that just the first ten terms give $e$ correct to seven decimal places:
$$1 + 1 + \tfrac{1}{2} + \tfrac{1}{6} + \tfrac{1}{24} + \tfrac{1}{120} + \tfrac{1}{720} + \tfrac{1}{5040} + \tfrac{1}{40320} + \tfrac{1}{362880} \approx 2.7182815$$

The series converges because $k! \geq 2^{k-1}$ for $k \geq 1$, so $\tfrac{1}{k!} \leq \tfrac{1}{2^{k-1}}$, and the geometric series $\sum \tfrac{1}{2^{k-1}}$ converges. This is what bounds the sequence in Definition 1 above by $3$.

### Definition 3 — The calculus characterization

$$\boxed{\;e^x \text{ is the unique function satisfying } \frac{d}{dx} e^x = e^x \text{ and } e^0 = 1.\;}$$

No other exponential has this property. For any other base $b$:
$$\frac{d}{dx} b^x = b^x \ln b$$

Base 2? The derivative has a factor of $\ln 2 \approx 0.693$ out front. Base 10? A factor of $\ln 10 \approx 2.303$. The derivative is never as clean as the original function — except when $b = e$, where $\ln e = 1$ and the correction factor vanishes.

This is the defining property that makes $e$ the **natural** base of calculus. Every application in physics where something changes at a rate proportional to its current size — exponential growth, exponential decay, oscillations via $e^{i\omega t}$, heat flow, diffusion — lands on base $e$ because of this identity.

### Why all three definitions agree

Here's the compact argument. Define the function
$$f(x) = \sum_{k=0}^\infty \frac{x^k}{k!}$$
(the **exponential series** in variable $x$).

1. **Differentiate term by term.** $\tfrac{d}{dx}\tfrac{x^k}{k!} = \tfrac{k \cdot x^{k-1}}{k!} = \tfrac{x^{k-1}}{(k-1)!}$. So $f'(x) = \sum_{k=1}^\infty \tfrac{x^{k-1}}{(k-1)!} = \sum_{j=0}^\infty \tfrac{x^j}{j!} = f(x)$. And $f(0) = 1$ (only the $k=0$ term survives). So $f$ satisfies **Definition 3** — it is *the* function whose derivative is itself.

2. **Evaluate at $x = 1$.** $f(1) = \sum_{k=0}^\infty \tfrac{1}{k!}$, which is the right side of **Definition 2**.

3. **The binomial-theorem argument** (Definition 1's proof above) shows $\lim_{n\to\infty} (1 + 1/n)^n = \sum_{k=0}^\infty \tfrac{1}{k!} = f(1)$. So **Definition 1** gives the same number.

All three definitions produce $f(1)$ for the same $f$. The "three faces of $e$" are really just three ways of describing the same special function evaluated at a single point.

---

## 4. $e$ everywhere

$e$ shows up in contexts that have nothing obvious to do with compound interest. Each appearance below is a clue that the deeper story of $e$ is about **change-by-a-factor-of-itself** — a pattern that hides inside dozens of apparently unrelated problems.

### Derangements — probability that nobody gets their hat back

A **derangement** of $\{1, 2, \ldots, n\}$ is a permutation with no fixed points: nothing lands in its original spot. The probability that a random permutation is a derangement:

$$P(\text{derangement}) = \sum_{k=0}^n \frac{(-1)^k}{k!} \;\xrightarrow[n \to \infty]{}\; \frac{1}{e} \approx 0.368$$

**Hat-check puzzle.** At a party, $n$ guests drop their hats at the door. The distracted attendant hands them back randomly. What's the probability *nobody* gets their own hat? For $n = 1$ it's 0, for $n = 2$ it's 1/2, for $n = 3$ it's 1/3, but by $n = 5$ the answer has already stabilized at $1/e \approx 36.8\%$. One of those results that feels like it shouldn't involve $e$ — but does.

### Normal distribution — the bell curve

$$\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

$e$ sits inside the exponent alongside $\pi$. The two most important transcendentals in mathematics, both at the heart of the most important distribution in statistics. [[Normal Distribution]] covers the full story — why this specific curve falls out of the Central Limit Theorem, why the $\tfrac{1}{\sqrt{2\pi}}$ normalization is forced, and why the sum of enough independent random things always ends up looking like this.

### Poisson distribution — rare events

$$P(X = k) = \frac{\mu^k e^{-\mu}}{k!}$$

The probability of exactly $k$ events in a fixed window when the average rate is $\mu$. The $e^{-\mu}$ is the "no events in the full interval" baseline; $\mu^k / k!$ corrects for allowing exactly $k$ of them. Used for radioactive decay counts, email arrival times, football goals, rare typos — anything where events are independent, fast, and rare. [[Poisson Distribution]] has the full picture.

### Stirling's approximation — factorials for large $n$

$$n! \;\approx\; \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$

This looks miraculous — we have $\pi$, $e$, $n$, and $n!$ all in the same line. For $n = 10$: Stirling gives $3{,}598{,}696$ against the true value $3{,}628{,}800$ — less than 1% off. For $n = 50$, handling the actual factorial requires a calculator; Stirling gives a clean pencil estimate. Used constantly in physics, algorithm analysis, and statistical mechanics.

### Euler's identity — the most beautiful equation in mathematics

$$\boxed{\;e^{i\pi} + 1 = 0\;}$$

A special case of **Euler's formula** $e^{ix} = \cos x + i \sin x$ at $x = \pi$. Five of the most important constants in mathematics — $e$, $i$, $\pi$, $1$, $0$ — and three fundamental operations — addition, multiplication, exponentiation — all in one line with no wasted symbols. Physicists and mathematicians routinely rank this as the most beautiful equation ever written. [[Complex Numbers]] derives it; [[Exponential Growth and Decay]] uses its general form $e^{i\omega t}$ for AC-circuit analysis.

### Prime Number Theorem

Let $\pi(x)$ denote the number of primes $\leq x$ (unrelated to the circle constant; the notational clash is unavoidable). The **Prime Number Theorem** (Hadamard and de la Vallée-Poussin, 1896, independently) says:

$$\pi(x) \sim \frac{x}{\ln x}$$

Natural logarithms — i.e., $e$ — describe the asymptotic density of primes. $e$ didn't ask to be in number theory; it just keeps showing up.

---

## 5. Why base $e$ is "natural"

Three of the above applications — calculus, statistics, number theory — all land on base $e$ rather than base 10 or base 2. This isn't a coincidence; it's structural. The cleanest way to see why:

**Derivatives of exponentials.** Take any base $b$ and differentiate:
$$\frac{d}{dx} b^x = b^x \ln b$$

Every base except $e$ comes with a correction factor $\ln b$ out front. Base 2 picks up $\ln 2 \approx 0.693$. Base 10 picks up $\ln 10 \approx 2.303$. Only for $b = e$ does $\ln b = 1$ — the correction vanishes, and $(e^x)' = e^x$. From calculus's perspective, every other exponential is just "$e^x$ with a constant stapled on."

**Logarithms.** Same story in reverse. The integral
$$\int \frac{dx}{x} = \ln |x| + C$$
uses the *natural* log. Try $\log_2$ or $\log_{10}$ and you pick up a correction factor again. Many real-analysis textbooks **define** $\ln x$ as $\int_1^x \tfrac{dt}{t}$ — because this is the log that makes calculus work without stapled-on constants.

**Why this matters physically.** Physical laws are differential equations. Differential equations involve derivatives. Exponential solutions use $e$ because anything else introduces spurious constants that would need to be absorbed somewhere, cluttering the equations. Nature doesn't care which base humans use to count — but it cares a lot about derivatives, and derivatives are cleanest in base $e$. That's why $e$ is the "natural" base: it's the base that makes the laws of physics look as simple as they can.

> [!tip] Why ln, specifically?
> The name **natural logarithm** comes from this cleanness. $\log_{10}$ is "natural" for humans counting in base 10; $\log_2$ is "natural" for computers counting in bits. But $\ln$ is "natural" for *calculus*, which is the language physics is written in — hence the universal-sounding name.

---

## 6. Common Misconceptions (Teaching Notes)

### 1. "$e$ is just an arbitrary constant — why 2.71828 and not 2.7 or 3?"

Students sometimes treat $e$ like a decoration, an arbitrary number chosen to make formulas look fancy. They wonder why we couldn't just round it to 3 and move on.

**Fix.** Emphasize Definition 3: $e^x$ is the *unique* function whose derivative equals itself. That uniqueness is what pins $e$ down — once you demand $f'(x) = f(x)$ and $f(0) = 1$, the value $f(1) = e \approx 2.71828\ldots$ is forced on you by the math. It's no more "arbitrary" than $\pi$ is: both are non-negotiable consequences of very simple geometric/analytic requirements.

### 2. "$e$ stands for 'Euler.'"

It's a plausible guess, repeated in many textbooks. Almost certainly wrong.

**Fix.** Euler was famously modest about naming things after himself. His other constants (the Euler–Mascheroni $\gamma$, Euler characteristic $\chi$) were named by *other* people, usually after his death. The best guesses for the letter $e$: "**e**xponential," or simply "the next unused vowel after $a$, $b$, $c$ were taken." The truth is lost to history — even historians of mathematics admit it.

### 3. "$e^x$ and $10^x$ are basically the same — different base, same idea."

Operationally true at the level of IGCSE arithmetic, but students who think this way miss why calculus adopts $e$.

**Fix.** Work out $\tfrac{d}{dx} 10^x = 10^x \cdot \ln 10 \approx 2.303 \cdot 10^x$ and compare with $\tfrac{d}{dx} e^x = e^x$. The point isn't that $e$ and $10$ are fundamentally different — they're both valid bases — but that differentiating any base other than $e$ introduces a correction factor. Calculus *prefers* $e$ for the same reason geometry prefers radians over degrees: no stapled-on constants.

### 4. "$e$ and $\pi$ being in Euler's identity means they're tightly related."

Students see $e^{i\pi} + 1 = 0$ and assume $e$ and $\pi$ must be linked by some deep hidden formula.

**Fix.** The identity is a consequence of Euler's *formula* $e^{ix} = \cos x + i\sin x$, which connects exponentials to circular motion. At $x = \pi$, the cosine and sine values happen to be $-1$ and $0$, giving the clean result. It's a bridge between two sides of math, not an algebraic relationship between the constants themselves. We still don't know whether $e + \pi$ or $e \cdot \pi$ are irrational, let alone transcendental — more than 350 years after Euler. The identity is a connection between *functions*, not a dependency between the numbers.

---

## Exam Notes

### Cambridge 0606

$e$ appears explicitly on the 0606 syllabus under "Exponential and logarithmic functions." Expect:
- Sketching $y = e^x$, $y = e^{-x}$, and $y = \ln x$
- Solving equations of the form $e^x = k$, $\ln x = k$, and equations reducing to these
- Problems mixing $e^x$ with the laws of logarithms
- Continuous compound-interest problems using $y = Ae^{kt}$

The three-definitions story and the irrationality proof are *not* examinable on 0606 — but the letter $e$ is treated as a real, specific constant, not a mystery. Students should be comfortable typing "e" and "ln" on their calculator buttons.

### OxAQA 9260

The base-$e$ form is **not required** on 9260 — the extension topic N20 (exponential growth and decay) uses $y = A(1+r)^t$ and $y = Ab^t$ only. No need to memorize $e \approx 2.718$ for 9260 marks. But the student will meet $e$ immediately if they progress to A-Level, so this card is still worth reading.

### Cambridge 0580

Same position as 9260: $e$ is not required; the discrete/base-$b$ forms suffice.

### A-Level (Edexcel / AQA / OCR / CIE)

- **Year 1:** Derivatives of $e^x$ and $\ln x$ are new named results. Proof at "quote and use" level — the full $f(x) = \sum x^k/k!$ argument is beyond-syllabus but worth seeing.
- **Year 2:** Integration of $e^x$ and $\tfrac{1}{x}$; separation of variables for first-order ODEs $\tfrac{dy}{dt} = ky$.
- **Further Maths:** Taylor series $e^x = \sum x^k/k!$ is proved rigorously; Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ becomes the main tool for trig identities and De Moivre's theorem.

### IB AA / AI

- **AA SL** and **AI SL**: $e^x$ and $\ln x$ appear in the "exponents and logarithms" block. Definition-by-limit is not required.
- **AA HL**: extends into derivatives of exponentials and light-touch Taylor series. The $e = \lim(1+1/n)^n$ definition is expected.
- **AI HL**: more applied — compound interest, Newton's cooling, population models.

### AP Calculus (AB / BC)

- **AP Calc AB**: derivative of $e^x$, integral of $e^x$, separation of variables for growth-decay problems.
- **AP Calc BC**: adds the Taylor series $e^x = \sum x^k/k!$ with radius-of-convergence discussion. Irrationality and transcendence are not tested.

### Beyond high school — University

Rigorous real analysis (first-year undergraduate) introduces $e$ as $\lim(1+1/n)^n$ and derives the three definitions equivalently — the argument this card sketches in Part 3 is made fully precise. Hermite's transcendence theorem is typically taught in a third-year or graduate number-theory / transcendence-theory course.

---

## Connections

- **Motivation:** [[Exponential Growth and Decay]] — compound interest is where $e$ first makes itself known. That card handles $e$-as-a-growth-shape; this card handles $e$-as-a-number.
- **Prerequisite for the convergence proof:** [[Binomial Theorem]] — expanding $(1+1/n)^n$ term-by-term is how Definition 1 ↔ Definition 2 gets proved.
- **Prerequisite for the irrationality proof:** [[Surds]] — the habit of proof by contradiction, learned there for $\sqrt{2}$, reappears here for $e$.
- **Proof technique:** [[Proof by Contradiction]] — Euler's $q!$ argument is the template: assume $e = p/q$, derive "an integer equals a non-integer," conclude no such $p, q$ exist.
- **Leads to:** [[Logarithms]] — the inverse $\ln x$; formal treatment of change-of-base and log laws.
- **Leads to:** [[Differentiation]] — $\dfrac{d}{dx} e^x = e^x$ is the calculus characterization.
- **Leads to:** [[Integration]] — $\int e^x\, dx = e^x + C$ and $\int \tfrac{dx}{x} = \ln|x| + C$ are the matching antiderivatives.
- **Leads to:** [[Complex Numbers]] — Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ and Euler's identity $e^{i\pi} + 1 = 0$.
- **Leads to:** [[Differential Equations]] — $e^{kt}$ is the solution family for first-order linear ODEs.
- **Appears in probability:** [[Normal Distribution]], [[Poisson Distribution]] — the density and PMF both contain $e$ explicitly.
- **Historical cousin:** $\pi$ — the other famous transcendental. Both proved transcendental via the Hermite–Lindemann method; both beyond algebraic reach.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $e$ | `e` | The constant itself |
| $e^x$ | `e^x` | Natural exponential |
| $e^{i\pi}$ | `e^{i\pi}` | Complex exponent |
| $\ln x$ | `\ln x` | Natural log; autospaced |
| $\log_b x$ | `\log_b x` | General-base log |
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$ | `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{Q}` | Number-system symbols |
| $\displaystyle\lim_{n \to \infty}$ | `\lim_{n\to\infty}` | Limit with subscript |
| $\displaystyle\sum_{k=0}^{\infty}$ | `\sum_{k=0}^{\infty}` | Sum to infinity |
| $\binom{n}{k}$ | `\binom{n}{k}` | Binomial coefficient |
| $\dfrac{d}{dx}$ | `\dfrac{d}{dx}` | Display-size derivative |
| $i$ | `i` | Imaginary unit |
| $\varphi$ | `\varphi` | Golden ratio (used in Part 2 list) |

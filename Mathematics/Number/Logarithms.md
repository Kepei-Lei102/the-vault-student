---
chinese: 对数 (duìshù)
prerequisites:
  - "[[Laws of Indices]]"
  - "[[Euler's Number]]"
  - "[[Changing the Subject (Vocab)]]"
leads_to:
  - "[[Differentiation]]"
  - "[[Integration]]"
  - "[[Differential Equations]]"
  - "[[Error Propagation]]"
  - "[[Information Theory]]"
teach_together:
  - "[[Exponential Function]]"
tags:
  - subject/mathematics
  - domain/number
  - domain/algebra
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/0606-6-1
  - syllabus/0606-6-2
  - syllabus/0606-6-3
  - syllabus/9709-2-2
  - syllabus/9709-3-2
  - type/deep
  - type/definition
  - type/proof
  - notation/log
  - notation/ln
  - notation/lg
  - misconception/log-of-a-sum
  - misconception/log-cancels-addition
  - misconception/ln-is-a-different-log
---

# Logarithms 对数

## Definition

A **logarithm** answers one question: *what power do I raise the base to, in order to get this number?* If you can raise $2$ to some power and land on $8$, the logarithm tells you that power is $3$.

Formally:

$$\boxed{\;\log_b x = y \iff b^y = x\;}$$

(with $b > 0$, $b \neq 1$, and $x > 0$.)

Read this out loud: "$\log_b x$ is the power you raise $b$ to, to get $x$." Everything else in this card — the laws, the graph, the calculator buttons, the applications — follows from that one sentence.

### Intuition

If exponentiation $b^y$ is the function "multiply $b$ by itself $y$ times", then $\log_b$ is the function that **undoes** it. $\log$ and exponentiation are inverses — in the exact sense that $\log_b (b^y) = y$ and $b^{\log_b x} = x$. Think of $\log$ as "the opposite of `^`".

A second intuition that pays off later: logarithms turn **multiplication into addition**. $\log(ab) = \log a + \log b$. Historically this is *why* logarithms were invented — before calculators, astronomers needed to multiply huge numbers, and turning a multiplication into an addition (via a log table, then un-log via an antilog table) cut the work in half.

### 中文锚点

**对数 (duìshù)** 就是**指数**的逆运算。$\log_b x = y$ 即 "以 $b$ 为**底 (dǐ)**，$x$ 是**真数 (zhēnshù)**，$y$ 是**对数值**"。它回答的是 "**$b$ 的几次方等于 $x$**？"

三个关键中文术语：
- **底 (dǐ)** = base ($b$)
- **真数 (zhēnshù)** = argument / number ($x$) — "the real number"，即取对数的对象
- **对数值 / 指数** = logarithm value ($y$)

两个特殊底要记牢：**常用对数 $\lg x = \log_{10} x$**（十进制），**自然对数 $\ln x = \log_e x$**（以 $e$ 为底，微积分专用）。中国教材用 $\lg$，英国/国际教材更多用 $\log$（无下标默认十为底）。

## Notation — three log symbols you will meet

English-language textbooks, Chinese textbooks, physics papers, and calculator keys do not all agree. Here is the full table:

| Symbol | Base | Used by | Note |
|--------|------|---------|------|
| $\log_b x$ | Any $b$ you like | Universal | Most explicit — always shows the base |
| $\log x$ | $10$ (UK / international) OR $e$ (pure-math style) | 0606, A-Level, IB — usually base $10$ | **Ambiguous without context.** When in doubt, assume base $10$ for 0606 |
| $\lg x$ | $10$ | Chinese textbooks, some European | "common log" / 常用对数 |
| $\ln x$ | $e \approx 2.718$ | Everywhere — calculus, physics, chemistry | "natural log" / 自然对数 |

> [!warning] $\ln$ is not a "different kind" of log
> Students sometimes treat $\ln$ as a separate function with separate rules. It is not. $\ln x$ is literally $\log_e x$ — the same function, base $e$. Every log law below applies to $\ln$ unchanged. The only reason $\ln$ gets its own symbol is that it shows up so often in calculus that writing "$\log_e$" every time would be exhausting.

**0606 convention.** On 0606 papers, if you see $\log$ without a subscript, read it as $\log_{10}$. $\ln$ always means $\log_e$. If a problem says "using logarithms, solve $2^x = 50$", you're free to pick base $10$ or base $e$ — both give the same answer; $\ln$ is usually faster because calculators have a dedicated $\ln$ button.

## Key Facts — the log laws

Every log identity below comes from an index identity you already know, with the roles of input and output swapped. That is the whole story of logarithms: *they inherit their structure from indices*.

### Three laws

Let $b > 0$, $b \neq 1$, and $x, y > 0$.

| Name | Identity | 中文 |
|------|----------|------|
| **Product law** | $\log_b(xy) = \log_b x + \log_b y$ | 积的对数 = 对数的和 |
| **Quotient law** | $\log_b\!\left(\dfrac{x}{y}\right) = \log_b x - \log_b y$ | 商的对数 = 对数的差 |
| **Power law** | $\log_b(x^n) = n \log_b x$ | 幂的对数 = 指数乘以对数 |

### Three special values

| Identity | Why |
|----------|-----|
| $\log_b 1 = 0$ | Because $b^0 = 1$ for any $b$ |
| $\log_b b = 1$ | Because $b^1 = b$ |
| $\log_b b^n = n$ | Because $b^n = b^n$ — this is $\log$ and exponentiation undoing each other |

### Why the product law works — the proof

This is the proof to understand; the other two follow the same template.

**Claim.** $\log_b(xy) = \log_b x + \log_b y$.

**Proof.** Let $p = \log_b x$ and $q = \log_b y$. By the definition of $\log$, these mean:

$$b^p = x \qquad \text{and} \qquad b^q = y.$$

Multiply the two equations:

$$b^p \cdot b^q = xy.$$

By the index law $b^p \cdot b^q = b^{p+q}$ (see [[Laws of Indices]]), the left side becomes $b^{p+q}$:

$$b^{p+q} = xy.$$

Apply the definition of $\log$ to this equation — "$b$ raised to what power gives $xy$? Answer: $p+q$":

$$\log_b(xy) = p + q = \log_b x + \log_b y. \qquad \blacksquare$$

> [!info] Why the three laws are really one law
> $\log$ is just a name for "the exponent." The product law says "exponents add when you multiply" — that's $b^p \cdot b^q = b^{p+q}$ in a funny hat. The quotient law is "exponents subtract when you divide" — $b^p / b^q = b^{p-q}$. The power law is "raising a power to a power multiplies the exponents" — $(b^p)^n = b^{np}$. Each log law is one index law, read backwards. If you can remember the index laws cold, you can re-derive every log law from scratch in thirty seconds.

### Change of base formula

What if your calculator has $\log_{10}$ and $\ln$, but your problem asks for $\log_3 50$? The **change of base** formula converts any log to any other log:

$$\boxed{\;\log_b x = \dfrac{\log_c x}{\log_c b}\;}$$

Pick $c$ to be whatever your calculator can do — usually $10$ or $e$.

**Proof.** Let $y = \log_b x$, so $b^y = x$. Take $\log_c$ of both sides (with any base $c$):

$$\log_c(b^y) = \log_c x.$$

Apply the power law on the left:

$$y \log_c b = \log_c x.$$

Divide:

$$y = \frac{\log_c x}{\log_c b},$$

which is what we wanted. $\blacksquare$

Two useful special cases:

- $\log_b x = \dfrac{\ln x}{\ln b}$ (base-$e$ conversion — favoured in calculus)
- $\log_b x = \dfrac{\log x}{\log b}$ (base-$10$ conversion — favoured for pure arithmetic)

## The graph of $y = \log_b x$

Logs and exponentials are inverse functions, so their graphs are reflections of each other across the line $y = x$. Swap $x$ and $y$ in every point on $y = b^x$ and you get a point on $y = \log_b x$.

| Feature | $y = b^x$ (with $b > 1$) | $y = \log_b x$ (with $b > 1$) |
|---------|--------------------------|-------------------------------|
| Domain | all real $x$ | $x > 0$ only |
| Range | $y > 0$ only | all real $y$ |
| Passes through | $(0, 1)$ | $(1, 0)$ |
| Asymptote | horizontal $y = 0$ | **vertical** $x = 0$ |
| Shape (for $b > 1$) | rising, concave up | rising, concave down |

![[log-exp-reflection.svg|697]]

Above: $y = e^x$ and $y = \ln x$ reflect into each other across the dashed line $y = x$. The vertical asymptote of $\ln x$ at $x = 0$ is the reflection of the horizontal asymptote of $e^x$ at $y = 0$. Wherever $e^x$ passes through $(a, b)$, $\ln x$ passes through $(b, a)$ — that is what "inverse function" means geometrically.

> [!warning] You cannot take the log of zero or a negative number
> The domain of $\log_b x$ is $x > 0$. Why? Because $b^y$ is always positive for any real $y$ — there is no exponent you can raise a positive base to and get $0$ or a negative number. So the "what power gives $x$" question has no answer for $x \leq 0$.
>
> On your calculator, `ln(-3)` errors out. In an exam, if your working ends at $\ln(-5) = \ldots$, you have made a mistake earlier — go back and find it. (Complex numbers do give $\log$ of negatives a meaning, but that is [[Complex Numbers]] territory, not 0606.)

## Natural log $\ln$ and calculus

$\ln x = \log_e x$ is the log base $e$. It is the log that calculus cares about, for one clean reason:

$$\frac{d}{dx} \ln x = \frac{1}{x}.$$

No other log has so clean a derivative — $\log_{10} x$ has derivative $\dfrac{1}{x \ln 10}$, with an ugly factor hanging off the front. Similarly, $\ln x$ is the **antiderivative** of $\dfrac{1}{x}$, which makes it the function you end up with whenever you integrate a reciprocal.

> [!info] Where does $(\ln x)' = 1/x$ come from?
> Two routes to the same fact, running in opposite directions:
>
> 1. **If you start with $e^x$** (the usual order at 0606 / A-Level): you define $\ln$ as the inverse of $e^x$, prove $(e^x)' = e^x$ first, then apply the inverse function rule — one chain-rule line gives $(\ln x)' = 1/x$. The proof lives with the calculus material; look for it in the [[Exponential Function]] card.
> 2. **If you start with the integral** $\ln x = \int_1^x \tfrac{1}{t}\, dt$ (the "integral definition" at the end of this card): the Fundamental Theorem of Calculus makes $(\ln x)' = 1/x$ automatic — it is literally what FTC says.
>
> Both routes build the same $\ln$ and the same $e^x$; they just disagree about which one to call the definition. Not circular, just two orderings of the same theory.

> [!info] Beyond 0606 — why $\ln$ is the "right" log for calculus
> The full story is in [[Euler's Number]]. In one line: $e$ is defined to be the base whose exponential $b^x$ has slope exactly $1$ at $x = 0$. That property forces $\dfrac{d}{dx} e^x = e^x$ (exponential is its own derivative) and, by the inverse-function relationship, forces $\dfrac{d}{dx} \ln x = \dfrac{1}{x}$. Every other base gives a clunkier derivative. $\ln$ isn't arbitrary — it's the log designed around calculus.

On 0606 §6.1, you are expected to *know* the properties of $\ln x$ and $e^x$ — including the asymptote, the reflection relationship, and that they are inverses — without needing to differentiate them yet. The calculus comes in at [[Differentiation]] and A-Level.

## Worked examples

### Example 1 — Solving $a^x = b$ (0606 §6.3)

> **Solve $3^x = 50$, giving your answer correct to 3 significant figures.**

Take $\ln$ of both sides. ($\log_{10}$ would work equally well; $\ln$ is the calculator default.)

$$\ln(3^x) = \ln 50.$$

Apply the power law on the left:

$$x \ln 3 = \ln 50.$$

Divide:

$$x = \frac{\ln 50}{\ln 3} = \frac{3.9120\ldots}{1.0986\ldots} = 3.56 \text{ (3 s.f.)}$$

**Sanity check.** $3^3 = 27$, $3^4 = 81$. Our answer $3.56$ sits between $3$ and $4$, and closer to $4$ — consistent with $50$ being closer to $81$ than to $27$. ✓

### Example 2 — Using log laws to simplify (0606 §6.2)

> **Write $2 \log x - 3 \log y + \log z$ as a single logarithm.**

Apply the power law to pull the coefficients back inside:

$$= \log(x^2) - \log(y^3) + \log z.$$

Apply product and quotient laws to combine:

$$= \log\!\left(\frac{x^2 z}{y^3}\right).$$

### Example 3 — Change of base (0606 §6.2)

> **Evaluate $\log_5 200$, giving your answer correct to 3 significant figures.**

Change to base $10$ (or $e$ — either works):

$$\log_5 200 = \frac{\log 200}{\log 5} = \frac{2.3010\ldots}{0.6990\ldots} = 3.29 \text{ (3 s.f.)}$$

### Example 4 — A log equation with an extraneous-solution trap (0606 §6.2)

> **Solve $\log_2(x+2) + \log_2(x-1) = 2$.**

Combine the left side using the product law:

$$\log_2\bigl[(x+2)(x-1)\bigr] = 2.$$

Rewrite in exponential form ($\log_2 A = 2 \iff A = 2^2 = 4$):

$$(x+2)(x-1) = 4.$$

Expand and rearrange:

$$x^2 + x - 2 = 4 \implies x^2 + x - 6 = 0 \implies (x+3)(x-2) = 0.$$

So $x = -3$ or $x = 2$.

**Check both.** $x = 2$: we need $\log_2(4) + \log_2(1) = 2 + 0 = 2$ ✓. $x = -3$: we would need $\log_2(-1) + \log_2(-4)$ — **undefined**. Reject. $\boxed{x = 2}$.

> [!warning] Always check log equation solutions
> When you combine logs with the product law, you lose track of the domain restriction $x > 0$ on each original term. After solving, **plug every candidate back in** and throw out any that make an argument zero or negative. This is the most common lost mark on 0606 §6.2 log equations.

## Common Misconceptions

### Misconception 1 — $\log(a + b) = \log a + \log b$

**Wrong.** The product law says $\log(ab) = \log a + \log b$. It is *multiplication* inside that splits into *addition* outside — not addition inside.

There is *no* simplification for $\log(a+b)$. You cannot pull the sum apart. Numerical check: $\log_{10}(10 + 10) = \log_{10} 20 \approx 1.301$, but $\log_{10} 10 + \log_{10} 10 = 1 + 1 = 2$. Clearly unequal.

### Misconception 2 — $\dfrac{\log a}{\log b} = \log\!\left(\dfrac{a}{b}\right)$

**Wrong.** The quotient law says $\log(a/b) = \log a - \log b$, with a *subtraction* on the right — not a division. The expression $\dfrac{\log a}{\log b}$ is what shows up in the *change of base* formula $\log_b a$ — a completely different thing.

### Misconception 3 — "$\ln$ and $\log$ give different answers, so they're different functions"

**Partly right, partly wrong.** They give different *numerical* answers because they're different bases, but they obey exactly the same laws and have the same *shape* of graph. They are as related as $2^x$ and $10^x$ — different bases of the same family.

### Misconception 4 — $\log_b(x^n) = (\log_b x)^n$

**Wrong.** The power law moves the exponent out as a *coefficient*, not an outer power. $\log_b(x^n) = n \log_b x$, not $(\log_b x)^n$. Numerical check: $\log_2(2^3) = 3$, but $(\log_2 2)^3 = 1^3 = 1$. Very different.

### Misconception 5 — "Log of a negative number is negative"

**Wrong.** Log of a negative number is *undefined* (over the real numbers). Log of a number less than $1$ is negative — that's different. $\log_{10}(0.1) = -1$ because $10^{-1} = 0.1$. But $\log_{10}(-1)$ simply doesn't exist.

## Beyond the syllabus

### Logarithmic scales

The human ear, eye, and earthquake sensors all respond to stimuli on a *log* scale, not a linear one. That's why we measure sound in **decibels** ($10 \log_{10}$ of the intensity ratio), earthquakes on the **Richter scale** (base-$10$ log of amplitude), and stellar brightness on a log magnitude scale. Doubling a logarithm-scale value means the underlying physical quantity grew by a constant **factor**, not a constant amount.

Linear instincts badly mislead on log scales: a magnitude-8 earthquake is not "twice as strong" as magnitude 4. It's $10^4 = 10{,}000$ times stronger in amplitude, and releases roughly $32^4 \approx 10^6$ times more energy.

### Screens, HDR, and why OLED beat LCD

Your eye's sensitivity to brightness is logarithmic. Going from $0.1$ nits to $1$ nit (a $10\times$ jump) is *enormously* perceptible — you go from "invisible black" to "barely visible grey." Going from $1000$ nits to $10{,}000$ nits is the same $10\times$ jump physically, but perceptually it's a modest bump, usually only noticeable in bright sunlight.

This log curve is the technical reason **OLED screens dominate the consumer market**. OLED's killer feature is *true black* — individual pixels can turn fully off, giving a near-zero lower end. Because human vision is log-sensitive near zero, deepening the blacks by even a fraction of a nit produces a huge perceived contrast gain. Meanwhile, LCD's $3000$-nit peaks matter less than advertised, because the log curve has flattened out up there — humans can't tell $1500$ from $3000$ as easily as they can tell $0.01$ from $0.5$. For indoor HDR content (films, games), OLED wins; for outdoor phones in direct sunlight where the ambient baseline is high, peak brightness starts to matter again.

### Loudness, hearing damage, and why it sneaks up on you

Sound pressure is measured in decibels: $\text{dB} = 20 \log_{10}(p / p_0)$. A $10$ dB increase is **ten times** the sound intensity, but only feels "about twice as loud" because perception is log-compressed. That compression is also what makes hearing damage so sneaky: the jump from $85$ dB (safe) to $100$ dB (damaging within minutes) feels like "a bit louder," but the actual energy hitting your cochlea is $10^{1.5} \approx 32\times$ more. By the time your ears tell you "this is too loud," you have already been over the damage threshold for a while.

Practical takeaways: the safe limit is roughly **$85$ dB for 8 hours**, halving for every $+3$ dB (so $88$ dB = $4$ hours, $91$ dB = $2$ hours, etc.). Good **active noise cancelling headphones** are a direct countermeasure — by cutting ambient noise $15$–$25$ dB, they let you listen to music at the actual volume you want ($60$–$70$ dB) rather than cranking up to $85$+ dB to drown out the subway.

This is also the backstory of the **loudness war** in pop music ($\sim 1990$–$2010$): producers discovered that whichever track sounded loudest on the radio got more attention, so albums were mastered to push every sample toward the maximum. The log-sensitive ear reads this as "exciting!" at first — but with no quiet passages for contrast, the dynamic range collapses and the music becomes fatiguing. Streaming platforms (Spotify, Apple Music) now normalise loudness automatically, which ended the war and let dynamic mastering come back — because once every track is turned to the same measured loudness, a crushed master arrives no louder than anyone else's and with nothing left in reserve. [[Stories/The Loudness War]] follows that arc in full, including the album whose best-sounding release was a video game.

### Napier's 1614 motivation

John Napier invented logarithms to make multiplication easier. Before calculators, multiplying two seven-digit numbers by hand took several minutes and was error-prone. Napier's table let you look up $\log a$, look up $\log b$, add them with a pencil (easy!), and then look up the antilog of the sum to recover $ab$. Astronomers saved *years* of arithmetic. Slide rules — the handheld calculators of 1650 to 1970 — are physical log tables.

Kepler, who was computing planetary orbits at the same time, reportedly credited Napier with "doubling the life of the astronomer."

### Information theory — log as "information content"

Claude Shannon (1948) defined the **information** of an event of probability $p$ as

$$I(p) = -\log_2 p \text{ bits.}$$

If something was certain ($p = 1$), learning it gives zero bits of information. If something had probability $1/2$, learning it gives one bit. Probability $1/8$ → three bits. This is why $\log_2$ shows up so often in computer science — it measures "how many yes/no questions worth of information is this?"

The full story — Shannon's 1948 paper founding information theory, the formula for **entropy** $H = -\sum p_i \log_2 p_i$, the channel capacity theorem behind every WiFi / 5G speed limit, and how all of it connects to data compression and AI — deserves its own deep card. See [[Information Theory]].

### The Prime Number Theorem

Roughly: among integers near $N$, the fraction that are prime is about $\dfrac{1}{\ln N}$. So primes thin out at the speed of a logarithm. This is the single deepest fact in the study of prime numbers, and $\ln$ — not $\log_{10}$, not $\log_2$ — is what shows up, because the derivation uses calculus.

### The integral definition of $\ln$ — an alternative framework

Here is one of the more beautiful *alternative* definitions in all of mathematics:

$$\ln x = \int_1^x \frac{1}{t}\, dt.$$

Read this as "$\ln x$ is the area under the curve $y = 1/t$ from $t = 1$ to $t = x$." In the framework of rigorous analysis, some courses take this as the *starting definition* of $\ln$, then define $e^x$ as its inverse — the reverse of the order used in this card. From that starting point, $(\ln x)' = \tfrac{1}{x}$ is automatic (the Fundamental Theorem of Calculus says it), and then $(e^x)' = e^x$ becomes the theorem to prove.

Both orderings end up with the same $\ln$ and the same $e^x$ — they're like two different blueprints for the same building. This card uses the standard order ($e^x$ first, $\ln$ as its inverse); the integral ordering is noted here because it's elegant, not because we're adopting it.

## Exam Notes

### Cambridge 0606

**§6.1 Exponential and logarithmic functions.** Know the shape and properties of $y = e^x$ and $y = \ln x$: domains, ranges, asymptotes, the reflection across $y = x$, and the values $e^0 = 1$, $\ln 1 = 0$, $\ln e = 1$. Typical exam task: "Sketch $y = \ln x$ stating any asymptote and the $x$-intercept." Losing marks usually comes from stating the wrong asymptote ($x = 0$, a vertical line, not $y = 0$).

**§6.2 Laws of logarithms, change of base.** Product, quotient, power laws; change of base. Expect 3–4 marks on problems like "Write $2 \ln x + \ln(x+1) - 3 \ln 2$ as a single logarithm" or "Without using a calculator, find the exact value of $\log_2 32 - \log_2 8$." *Without a calculator* means: get to an integer or simple fraction using the laws.

**§6.3 Solving equations of the form $a^x = b$.** The only technique is "take logs of both sides, then use the power law." Exam language: "Solve, giving your answer correct to 3 significant figures." A common extension is a disguised quadratic: let $u = 2^x$ in $2^{2x} - 5 \cdot 2^x + 4 = 0$ → $u^2 - 5u + 4 = 0$ → $u = 1$ or $u = 4$ → $x = 0$ or $x = 2$.

### A-Level

Logs reappear in:
- **Differentiation** — $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$, logarithmic differentiation for $y = x^x$ and similar.
- **Integration** — $\int \dfrac{1}{x}\,dx = \ln|x| + C$, plus integration-by-substitution tricks using logs.
- **Differential equations** — separable equations routinely end with a $\ln$ on both sides; solving for $y$ requires exponentiating to cancel.
- **Linearisation** — plotting $\ln y$ vs $x$ straightens out $y = A e^{kx}$, and $\ln y$ vs $\ln x$ straightens out $y = Ax^n$. This is the most-tested A-Level application: given data, *find the model*.

### IB AA

Same laws. IB AA SL covers log equations and change of base; HL extends into logarithmic differentiation, log scales in applications, and complex logs in the complex-numbers option.

## Connections

- **Prerequisite:** [[Laws of Indices]] — every log law is an index law in disguise; the proofs above are straight translations.
- **Prerequisite:** [[Euler's Number]] — $e$ is the base of $\ln$, and its defining calculus property is what makes $\ln$ the "natural" log.
- **Prerequisite:** [[Changing the Subject (Vocab)]] — solving $a^x = b$ is rearrangement with one extra tool (taking logs).
- **Inverse of:** [[Exponential Function]] — $\log_b$ and $b^x$ are literally inverse functions; the graphs mirror across $y = x$.
- **Related:** [[Exponential Graphs (Vocab)]] — shape catalogue for $y = b^x$; $\log$ graphs are the reflections.
- **Related:** [[Exponential Growth and Decay]] — every time you solve for time $t$ in $y = A e^{kt}$, you're taking a log.
- **Leads to:** [[Differentiation]] — $\ln$ has the cleanest derivative of any log.
- **Leads to:** [[Integration]] — $\int \dfrac{1}{x}\,dx = \ln\lvert x\rvert + C$.
- **Leads to:** [[Differential Equations]] — logs are the default tool for separable first-order equations.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\log_b x$ | `\log_b x` | General log, base $b$ |
| $\log x$ | `\log x` | Default base $10$ in 0606 / A-Level |
| $\ln x$ | `\ln x` | Natural log, base $e$ |
| $\lg x$ | `\lg x` | Base $10$ (Chinese convention) |
| $\log_b(xy) = \log_b x + \log_b y$ | `\log_b(xy)` | Product law |
| $\log_b\!\left(\dfrac{x}{y}\right)$ | `\log_b\!\left(\dfrac{x}{y}\right)` | Quotient law — `\!` tightens spacing |
| $\log_b(x^n) = n \log_b x$ | `\log_b(x^n) = n \log_b x` | Power law |
| $\log_b x = \dfrac{\log_c x}{\log_c b}$ | `\dfrac{\log_c x}{\log_c b}` | Change of base |
| $\log_b 1 = 0$ | `\log_b 1 = 0` | Log of 1 is always 0 |
| $e$ | `e` | Base of natural log |
| $\ln e = 1$ | `\ln e = 1` | Consequence of $e^1 = e$ |

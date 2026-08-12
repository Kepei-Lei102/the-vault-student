---
chinese: 指数增长与衰减 (zhǐshù zēngzhǎng yǔ shuāijiǎn)
prerequisites:
  - "[[Simple and Compound Interest (Vocab)]]"
  - "[[Laws of Indices]]"
  - "[[Percentage Calculations (Vocab)]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Direct and Inverse Proportion (Vocab)]]"
leads_to:
  - "[[Euler's Number]]"
  - "[[Logarithms]]"
  - "[[Exponential Function]]"
  - "[[Integration]]"
  - "[[Differential Equations]]"
  - "[[Exponential Graphs (Vocab)]]"
  - "[[Capacitors]]"
  - "[[Damped Oscillations]]"
  - "[[Linearisation]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - level/A-Level
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - syllabus/9260-N20
  - syllabus/9260-N20-Ext
  - syllabus/0580-E1-17
  - syllabus/9709-3-8
  - type/deep
  - misconception/exponential-vs-linear
  - misconception/e-is-arbitrary
  - misconception/half-life-depends-on-age
---

# Exponential Growth and Decay 指数增长与衰减

## Definition

**Exponential growth** (指数增长) and **exponential decay** (指数衰减) describe quantities whose *rate of change is proportional to their current size*. A balance earning interest, a decaying radioactive sample, a cooling cup of coffee, a drug clearing from the bloodstream — all follow the same shape because they share one mechanism: *how fast the quantity changes depends on how much of it there is right now*.

Three equivalent faces of the same function. In every form, $y$ is the amount at time $t$, and $A$ is the starting amount ($A = y$ when $t = 0$):

1. **Discrete (period-by-period):** $y = A (1 + r)^t$ — compound interest, population year-on-year. Here $r$ is the growth rate per period (as a decimal: 5% → 0.05), and $t$ counts whole periods.
2. **Continuous, base-$b$:** $y = A b^t$ — any fixed multiplier per unit time. Here $b$ is the factor per unit time; $b = 2$ means "doubles each unit of time", $b = 0.5$ means "halves each unit of time".
3. **Continuous, base-$e$:** $y = A e^{kt}$ — the form calculus prefers. Here $k$ is called the **continuous rate**, and $e \approx 2.71828$ is a specific constant. The full story of what $e$ is and why it's the most natural base for calculus lives in [[Euler's Number]]; for this card, we'll just use it as a fixed multiplier.

All three describe the same curve in different clothing. The rest of this card is the story of why form 3 keeps winning — and why that tells you something about $e$ itself.

> [!note] Seeing form 3 for the first time? Don't panic.
> If $\dfrac{d}{dt}$ or the phrase "calculus prefers" makes you nervous, that's completely fine — you're probably reading this card *before* you've met calculus, not after. Take $e^{kt}$ on faith for now: it's just "a smooth continuous version of $(1+r)^t$". Every 9260 and 0580 exam mark is reachable using forms 1 and 2 alone. The $e$-as-a-constant story in [[Euler's Number]] and the calculus justification in §6 are there so that when you do meet calculus later, this card clicks into place instantly — not to scare you now.

### 中文锚点

指数增长/衰减：**变化率 ∝ 当前数量**。银行利息、放射性衰变、牛顿冷却、药物代谢 —— 都共享这一结构。离散复利 $(1+r)^n$ 在连续化极限下变为 $e^{rt}$，其中 $e = \lim_{n\to\infty}(1+1/n)^n \approx 2.71828$。这是自然界最常见的增长模式。关键工具：取对数 $\ln$ 可以从指数里解出 $t$ 或 $k$。

## 1. From Compound Interest to Continuous Growth

The companion card [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]] ended with the closed form for annual compounding:

$$A = P\left(1 + \frac{r}{100}\right)^n$$

But real banks compound more often: monthly, daily, sometimes continuously. Does the compounding frequency matter, and if so, how much?

### Compounding $m$ times per year

Let $r$ be the *annual* rate written as a decimal. Compounding $m$ times per year, each period's rate is $r/m$ and the number of periods in $t$ years is $mt$:

$$A = P\left(1 + \frac{r}{m}\right)^{mt}$$

Set $P = 1$, $r = 1$ (100% per year — deliberately extreme so the effect is visible), $t = 1$ year, and increase $m$:

| $m$ | $(1 + 1/m)^m$ |
|----:|--------------:|
| 1 (annual) | 2.00000 |
| 2 (semi) | 2.25000 |
| 4 (quarterly) | 2.44141 |
| 12 (monthly) | 2.61304 |
| 365 (daily) | 2.71457 |
| 8,760 (hourly) | 2.71813 |
| 525,600 (per minute) | 2.71828 |
| $\infty$ (continuous) | $\mathbf{e} = 2.71828\ldots$ |

The sequence **converges** — not to a round number, but to a fundamental constant:

$$\boxed{\;e = \lim_{m \to \infty} \left(1 + \frac{1}{m}\right)^m \approx 2.71828\ldots\;}$$

### What this limit actually is — the toolkit for this card

The table *looks* like it's approaching something. Proving it actually does — and proving that value equals the constant $e \approx 2.71828\ldots$ you've seen on calculators — takes a careful argument using the **binomial theorem**, the **Monotone Convergence Theorem** (every increasing sequence bounded above converges), and a final [[Squeeze Theorem]] step to identify the value. **The full four-step proof lives in [[Euler's Number]] §3 Definition 1** alongside two *other* equivalent definitions of $e$ — an infinite series $e = \sum_{k=0}^\infty 1/k!$ and a calculus characterization — plus Euler's proof that $e$ is irrational.

For everything on *this* card, all you need is:

- $e \approx 2.71828\ldots$ is a fixed constant (irrational, even transcendental — see [[Euler's Number]] for proofs).
- $e^x$ is the unique exponential whose derivative equals itself: $\dfrac{d}{dx} e^{kt} = k\, e^{kt}$. This is what makes base $e$ the calculus-friendly choice.
- The inverse of $e^x$ is the **natural logarithm** $\ln x$, satisfying $e^{\ln x} = x$ and $\ln(e^x) = x$. We'll use $\ln$ in §5 whenever $t$ is trapped inside an exponent. The full treatment of $\ln$ — change of base, log laws, its graph — lives in [[Logarithms]]; here we treat it operationally as "the thing that undoes $e^x$".

That's the full operational toolkit. Onward.

### The continuous formula

For a general rate $r$ (as a decimal), compounding continuously gives:

$$\boxed{\;A = P e^{rt}\;}$$

Every exponential-growth problem in physics, biology, finance, and chemistry turns out to be a version of this equation.

> [!info] Why this *had* to happen
> The limit $(1 + r/m)^{mt}$ as $m \to \infty$ is not a coincidence — it's forced by the algebra. Substitute $u = m/r$, so $m = ur$ and $r/m = 1/u$:
> $$\left(1 + \frac{r}{m}\right)^{mt} = \left(1 + \frac{1}{u}\right)^{urt} = \left[\left(1 + \frac{1}{u}\right)^{u}\right]^{rt} \;\xrightarrow[u \to \infty]{}\; e^{rt}$$
> Whatever $e$ is defined as, it *must* be the limit inside the brackets. The compound-interest story gave it a name; algebra forced its value.

## 2. The Three Forms — converting between them

Same curve, three parameterizations. In all three, $y$ is the amount at time $t$ and $A$ is the starting amount (the value of $y$ when $t = 0$).

| Form | Formula | What the growth parameter means |
|------|---------|---------------------------------|
| Discrete | $y = A (1 + r)^t$ | $r$ is the per-period growth rate as a decimal. $r = 0.05$ means "grows by 5% each period". $r < 0$ means decay. $t$ counts whole periods. |
| Continuous, base-$b$ | $y = A b^t$ | $b$ is the factor the quantity multiplies by per unit of time. $b = 2$ means "doubles each unit of time"; $b = 0.5$ means "halves each unit". $b > 1$ is growth, $0 < b < 1$ is decay. |
| Continuous, base-$e$ | $y = A e^{kt}$ | $k$ is the **continuous rate** (dimensions: per unit time). $k > 0$ is growth, $k < 0$ is decay. Same physical quantity as $r$ in form 1, but measured in a slightly different way — see the conversion table. |

All three pass through the same point $(0, A)$ (since $y = A \cdot 1$ at $t = 0$ in every form) and trace the same shape. Only the name of the parameter changes.

### Conversions

Letting $r$, $b$, $k$ refer to the three parameters above:

| Given | Convert to | Formula |
|-------|-----------|---------|
| Discrete rate $r$ (decimal per period) | Continuous rate $k$ | $k = \ln(1 + r)$ |
| Base $b$ (multiplier per unit time) | Continuous rate $k$ | $k = \ln b$ |
| Continuous rate $k$ | Discrete rate $r$ | $r = e^k - 1$ |

**Worked conversion.** A balance grows at 5% per year (so in the discrete form $r = 0.05$). Find the equivalent *continuously-compounded* rate $k$:

$$k = \ln(1 + r) = \ln(1.05) \approx 0.04879$$

So a 5% discrete rate corresponds to $k \approx 0.04879$ per year in the continuous form. The continuous rate is always *slightly less* than the discrete rate because continuous compounding earns interest on the fraction of interest already earned within the period — precisely the APR-vs-APY distinction covered in [[Financial Literacy (Life)]] §2.

## 3. Half-life and Doubling Time — the hallmarks of exponential behavior

We're still using $y = A e^{kt}$, where $y$ is the amount at time $t$, $A$ is the starting amount, and $k$ is the continuous rate (positive for growth, negative for decay). The defining feature of exponential change is that **the time to multiply by any fixed factor is a constant** — it does not depend on when you start counting. That constant has two famous names.

### Doubling time

For a growing quantity ($k > 0$), call $T_d$ the **doubling time** — the amount of time it takes for $y$ to double, regardless of when you start the clock. Set $y = 2A$ in the formula and solve for $t = T_d$:

$$A e^{k T_d} = 2A \quad\Rightarrow\quad e^{k T_d} = 2 \quad\Rightarrow\quad k T_d = \ln 2 \quad\Rightarrow\quad T_d = \frac{\ln 2}{k}$$

The $A$ cancels — that's the crucial step. The doubling time does not depend on how much you started with. It only depends on $k$.

### Half-life

For a decaying quantity ($k < 0$), call $T_{1/2}$ the **half-life** — the time for $y$ to drop to half its current value. Set $y = A/2$:

$$A e^{k T_{1/2}} = \frac{A}{2} \quad\Rightarrow\quad e^{k T_{1/2}} = \frac{1}{2} \quad\Rightarrow\quad T_{1/2} = \frac{\ln(1/2)}{k} = \frac{-\ln 2}{k} = \frac{\ln 2}{|k|}$$

Same formula shape — the direction is absorbed by the sign of $k$. Both constants rely on $\ln 2 \approx 0.693$.

**Variable roster for §3** (worth pausing to re-read):
- $y$ = amount at time $t$ (units depend on context: dollars, atoms, cells)
- $A$ = starting amount at $t = 0$
- $k$ = continuous rate (units: per unit time). Positive ⇒ growth. Negative ⇒ decay.
- $T_d$ = doubling time (units: time)
- $T_{1/2}$ = half-life (units: time)

### Why these are *constants*

A carbon-14 atom does not "know how old" it is. Its probability of decay in the next second is the same whether the atom is new or 10,000 years old. A population growing at 3% per year grows by the same factor in any 23-year window. Every exponential process has this **memorylessness** — and this is precisely what distinguishes exponential from a *power-law* function ($y = t^2$, $y = t^3$, etc.) where the doubling time shrinks as $t$ grows.

> [!note] Yes — the video game
> Valve's *Half-Life* (1998), the game that launched Gordon Freeman, a crowbar, and one of the most influential shooters in history, is named after exactly this concept. Its sequel has been in development so long that fans joke it's undergoing a second half-life. The science name came first, though: physicists coined "half-life" in the early 1900s to describe radioactive decay once they realized the halving time was a constant of the isotope, not of the sample.

> [!tip] Rule of 72 — continuous form
> From [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]] we had $T_d \approx 72/r_\%$ for quick mental estimates (where $r_\%$ is the rate as a percent, so 5% → $r_\% = 5$). The continuous form is exact:
> $$T_d = \frac{\ln 2}{k} = \frac{0.693}{k} \;\approx\; \frac{69.3}{k_\%}$$
> The "72" is a rounded version of 69.3 chosen for its many divisors (1, 2, 3, 4, 6, 8, 9, 12). Both forms give the same ballpark — pick whichever is easier to compute in your head. Example: at $k_\% = 6$ (i.e. $k = 0.06$), $T_d \approx 11.55$ years by the exact formula; the Rule of 72 gives 12. Close enough for a mental check.

## 4. Canonical Applications

The same equation under five different names. Each subsection gives its own letter roster so you never have to flip back.

### Radioactive decay (放射性衰变)

$$N(t) = N_0\, e^{-\lambda t}$$

- $N(t)$ = number of atoms still undecayed at time $t$
- $N_0$ = number of atoms at $t = 0$ (the starting sample)
- $\lambda$ (lambda, Greek letter) = **decay constant**, units per unit time. It plays the role of $|k|$; the minus sign in the exponent makes this explicitly decay.
- $t$ = elapsed time

Half-life of the sample:

$$T_{1/2} = \frac{\ln 2}{\lambda}$$

**Carbon-14 dating.** $^{14}C$ (carbon-14) has $T_{1/2} = 5730$ years. A fossil contains 25% of the $^{14}C$ it would have had when alive. How old is it?

$$\frac{N(t)}{N_0} = 0.25 = e^{-\lambda t} \quad\Rightarrow\quad t = \frac{\ln 4}{\lambda} = \frac{2 \ln 2}{\lambda} = 2\,T_{1/2} = 11{,}460 \text{ years}$$

25% = one-quarter = two halvings — you can spot this without touching a calculator.

### Newton's law of cooling (牛顿冷却定律)

$$T(t) - T_{\text{room}} = \bigl(T_0 - T_{\text{room}}\bigr)\, e^{-kt}$$

- $T(t)$ = object's temperature at time $t$
- $T_0$ = object's temperature at $t = 0$
- $T_{\text{room}}$ = temperature of the surroundings (assumed constant)
- $k$ = cooling constant (units: per unit time) — depends on the object's material, surface area, and how well it's insulated
- $t$ = elapsed time

What decays exponentially is the *excess temperature* above room, not the temperature itself. A cup of coffee at 90°C in a 20°C room starts with an excess of 70°C. After one "time constant" $\tau = 1/k$ (that's the natural time-scale of the cooling), the excess drops to $70/e \approx 25.8$°C, so the coffee sits at about 45.8°C. After two time constants, the excess is $70/e^2 \approx 9.5$°C, giving 29.5°C. It never quite reaches room temperature — it just gets exponentially close.

### Population growth — and its limits

$$P(t) = P_0\, e^{kt}$$

- $P(t)$ = population size at time $t$
- $P_0$ = population at $t = 0$
- $k$ = intrinsic per-capita growth rate (births per individual minus deaths per individual, continuously)
- $t$ = elapsed time

At 2% per year ($k = 0.02$), a population doubles every $\ln 2 / 0.02 \approx 34.7$ years. Human populations have done this for stretches — the world population roughly doubled between 1960 and 2000.

But **pure exponential growth is unsustainable** — environmental limits eventually kick in, and the model transitions to *logistic growth* (see the "Beyond syllabus" callout, where we also say what the carrying capacity $K$ looks like in concrete cases). The exponential formula is the first approximation for small populations with plenty of resources, not the final answer.

### Drug pharmacokinetics (药物代谢动力学)

$$C(t) = C_0\, e^{-kt}$$

- $C(t)$ = plasma concentration of the drug at time $t$
- $C_0$ = plasma concentration just after the dose is absorbed
- $k$ = elimination rate constant (how fast the body clears the drug)
- $T_{1/2} = \ln 2 / k$ = biological half-life — the time for concentration to drop by half

| Drug | $T_{1/2}$ | Dosing implication |
|------|-----------|---------------------|
| Ibuprofen | ~2 hours | Every 4–6 hours |
| Caffeine | ~5 hours | Last dose 8 hours before sleep |
| Fluoxetine (Prozac) | ~4 days | Daily dosing; concentration builds to a steady state over weeks |
| Methotrexate | ~3–10 hours | Weekly dosing is possible for some indications |

Dosing schedules are chosen so that $C(t)$ stays above the therapeutic threshold but below the toxicity threshold — pure exponential-decay design.

### Continuous compound interest (the payoff from §1)

$$A(t) = P\, e^{rt}$$

- $A(t)$ = account balance at time $t$
- $P$ = principal (starting deposit) at $t = 0$
- $r$ = nominal annual interest rate as a decimal (5% → $r = 0.05$)
- $t$ = time in years

A \$10,000 deposit ($P = 10{,}000$) at 5% continuously compounded ($r = 0.05$) for 10 years ($t = 10$):

$$A(10) = 10{,}000 \cdot e^{0.05 \times 10} = 10{,}000 \cdot e^{0.5} \approx 10{,}000 \cdot 1.6487 = \$16{,}487$$

Compare with annual compounding at the same rate: $10{,}000 \cdot (1.05)^{10} \approx \$16{,}289$. Continuous is slightly higher ($\$198$ more) — the same limit story from §1, just scaled by principal $P$ and term $t$.

## 5. Solving for the Unknown — where logarithms enter

Up to this point we've been plugging numbers into $y = A e^{kt}$ to find $y$. The harder question: what if $y$ is known and we need to find $t$ or $k$? That's when algebra hits a wall — $t$ is trapped inside an exponent, and the only way to get it down is to take a **logarithm**.

### Solving for $t$

Starting point: $y = A e^{kt}$. In this section, $y$ is a *known target value* (say, the balance we want to reach), $A$ is the starting amount, $k$ is the continuous rate, and $t$ is the unknown time we're solving for.

$$y = A e^{kt} \;\Rightarrow\; \frac{y}{A} = e^{kt} \;\xrightarrow{\text{take } \ln \text{ of both sides}}\; \ln\!\frac{y}{A} = kt \;\Rightarrow\; t = \frac{1}{k} \ln \frac{y}{A}$$

**Worked example (0606-style).** A bank balance compounds continuously at 4% per year (so $k = 0.04$). We start with \$10,000 ($A = 10{,}000$) and want to know how long until the balance reaches \$15,000 ($y = 15{,}000$):

$$t = \frac{1}{0.04} \ln \frac{15{,}000}{10{,}000} = \frac{\ln 1.5}{0.04} \approx \frac{0.4055}{0.04} \approx 10.14 \text{ years}$$

### Solving for $k$ from two data points

Now suppose we don't know the rate $k$ — all we have is two measurements of the quantity. Call them $(t_1, y_1)$ and $(t_2, y_2)$, where $y_1$ is the amount measured at time $t_1$ and $y_2$ is the amount at time $t_2$. Both points sit on the same exponential curve $y = A e^{kt}$.

$$\frac{y_2}{y_1} = \frac{A e^{k t_2}}{A e^{k t_1}} = e^{k(t_2 - t_1)} \;\xrightarrow{\ln}\; k = \frac{\ln(y_2/y_1)}{t_2 - t_1}$$

Notice the $A$ cancels — we don't even need to know the starting amount to find the rate.

**Worked example.** A bacterial culture has $y_1 = 400$ cells at $t_1 = 0$ h (so that's also our $A$, for later) and $y_2 = 1200$ cells at $t_2 = 3$ h:

$$k = \frac{\ln(1200/400)}{3 - 0} = \frac{\ln 3}{3} \approx 0.366 \text{ per hour} \qquad T_d = \frac{\ln 2}{k} \approx 1.89 \text{ hours}$$

So the bacteria double in population every ~1.9 hours.

> [!info] You're meeting $\ln$ operationally here
> We're using $\ln$ as a tool — "the thing that undoes $e$". The full story of logarithms is in [[Logarithms]]: change of base, product/quotient/power laws, the relationship between $\log_b x$ and $\ln x$, the graph of $\ln x$, and (later) its derivative $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$. For the exam marks on this card, treating $\ln x$ as "the inverse of $e^x$" is enough. Everything else is enrichment.

## 6. The Calculus Perspective — why $Ae^{kt}$ is *inevitable*

Up to this point, the formula $y = A e^{kt}$ has been a guess that happens to fit the data. Calculus turns that guess into a proof. If you haven't met calculus yet, you can take this section on faith — it's showing you *why* form 3 is the natural one, not adding a new skill you need for the exam.

### The defining differential equation

"The rate of change of $y$ is proportional to $y$ itself" — that sentence, translated word-for-word into calculus notation, is:

$$\frac{dy}{dt} = k y$$

The left side $\dfrac{dy}{dt}$ reads "the rate at which $y$ changes as $t$ changes". The right side says that rate equals $k$ times the current value of $y$. This is called a **differential equation** — an equation that relates a function to its own derivative.

Solving it uses a technique called **separation of variables** (the full treatment is in [[Integration]]): we move everything involving $y$ to one side and everything involving $t$ to the other, then integrate:

$$\int \frac{dy}{y} = \int k \, dt \quad\Rightarrow\quad \ln|y| = kt + C$$

Here $C$ is an arbitrary constant of integration. Exponentiating both sides to undo the $\ln$:

$$|y| = e^{kt + C} = e^C \cdot e^{kt}$$

Call $A = e^C$ (itself a constant, since $C$ is). The sign of $y$ is set by the initial condition, so we drop the absolute-value bars and write:

$$y = A e^{kt}$$

Setting $t = 0$: $y(0) = A e^0 = A$. So $A$ is precisely the starting amount — the same $A$ we've been using all along.

**The key takeaway.** Exponential growth and decay are not *assumptions* chosen to fit data — they are the *unique* answer to "rate of change is proportional to current amount". Once you see the differential equation, no other form is possible.

> [!info] The calculus bridge — three cards you'll meet later
> - [[Differentiation]] — the identity $\dfrac{d}{dx} e^{kx} = k e^{kx}$ is what makes the calculus version of this card work cleanly. $e^{kx}$ is *not* a special case of the polynomial rule $\dfrac{d}{dx} x^n = n x^{n-1}$ — it's its own family, proved separately. That proof belongs in [[Differentiation]], not here.
> - [[Integration]] — the inverse of differentiation. It's what lets us solve $\dfrac{dy}{dt} = ky$ by separation of variables (the step we used above). Everything you'd want to know about $\int e^{kx}\,dx = \tfrac{1}{k}e^{kx} + C$ and the logarithm integral $\int \tfrac{dx}{x} = \ln|x| + C$ lives in that card.
> - [[Differential Equations]] — the general framework. $\dfrac{dy}{dt} = ky$ is the simplest non-trivial differential equation, and once you have the tools to handle it, almost all of mathematical physics opens up: heat flow, diffusion, oscillators, epidemic models, and more. Worth knowing that this modest card sits at the root of an entire A-Level / university subject.

## Exam Notes

### OxAQA 9260

**Syllabus ref:** N20 Ext — exponential growth and decay. Expect a 4–6 mark Extension-paper question involving a formula of the form $y = A b^t$ or $y = A (1+r)^t$. Common commands: *find the value after $n$ years*, *find when $y$ reaches \[target\]*, *find the rate $r$*. The base-$e$ form $e^{kt}$ is **not required**; the base-$b$ form suffices. Logs are **not required** on 9260 — calculator trial-and-improvement is the accepted route when $t$ is the unknown.

### Cambridge 0580 Extended

**Syllabus ref:** E1.17 — exponential growth and decay. Paper 4 typically embeds this in a multi-part question: one part sets up the formula from context, a later part asks for a specific target value or year. 0580 does not require logs; calculator trial-and-improvement is standard.

### Cambridge 0606

Exponential equations are first-class citizens on 0606, which *does* require the base-$e$ form and logarithms. Syllabus demands:

- Solve $e^x = k$, $\ln x = k$, and equations reducing to these
- Apply the laws of logarithms (product, quotient, power)
- Sketch $y = e^x$, $y = e^{-x}$, $y = \ln x$
- Algebraic half-life and doubling-time problems — no trial-and-improvement

The 0606 treatment is the bridge between 0580's calculator-based approach and A-Level's full calculus treatment.

### A-Level / IB / AP Calculus

Differentiation of $e^{kx}$ and $\ln x$ is standard Year 1. Separation of variables in first-order differential equations is Year 2. Exam technique: recognize the $\frac{dy}{dt} = ky$ pattern, separate variables, integrate both sides, apply boundary condition to find $A$, state the solution.

## Beyond syllabus

> [!tip] Logistic growth — the realistic population model
> Pure exponential growth $\dfrac{dP}{dt} = kP$ assumes unlimited resources. **Logistic growth** adds a second parameter, the **carrying capacity** $K$ — the maximum sustainable population the environment can support:
>
> $$\frac{dP}{dt} = kP \left(1 - \frac{P}{K}\right)$$
>
> Early on, when $P \ll K$, the second factor is ≈ 1 and it looks exponential. As $P \to K$, the second factor approaches 0 and the growth rate falls to zero — the curve flattens into an S-shape (a sigmoid).
>
> **What does $K$ look like in real cases?** It's always set by whatever resource is about to run out:
> - **Yeast in a 10-mL culture tube** — $K \approx 10^8$ cells. Limit: glucose in the medium.
> - **Moose on Isle Royale** (a wolf-free island in Lake Superior) — $K \approx 700$–$1{,}500$. Limit: winter forage under the snow.
> - **Deer in a managed forest** — $K$ ≈ set by tree regrowth and hunting quotas.
> - **Smartphone users globally** — $K \approx 7$ billion. Limit: the total human population minus infants.
> - **Humans on Earth** — $K$ is heavily contested; estimates range 9–11 billion based on food, fresh water, and climate-stability assumptions.
>
> Logistic curves are the standard model for population ecology, epidemic spread (early Covid-19 infection counts in each country fit logistic curves until behaviour-change kicked in), and tech-product adoption (Everett Rogers's diffusion-of-innovations theory — early adopters, early majority, late majority, laggards, all described by the same S-curve).

> [!tip] Euler's identity and alternating current — a concrete use-case
> $e$ has one more famous appearance: **Euler's formula**, which extends $e^x$ to imaginary inputs:
>
> $$e^{i\theta} = \cos\theta + i\sin\theta$$
>
> (Here $i = \sqrt{-1}$ — the imaginary unit. See [[Complex Numbers]] for the full derivation, and [[Euler's Number]] for why $e$ specifically shows up here rather than some other base.) This might look like a strange stunt, but it's the foundation of how every electrical engineer analyses **alternating current (AC)** — the electricity in the wall outlet.
>
> A wall-outlet voltage oscillates as $V(t) = V_0 \cos(\omega t)$, where $V_0$ is the peak voltage and $\omega = 2\pi f$ is the angular frequency (with $f = 50$ Hz in China / UK / most of the world, or $60$ Hz in the US / Japan). Working with real sines and cosines makes circuit analysis painful: every capacitor adds a derivative, every inductor an integral, and you end up chasing trigonometric identities for hours.
>
> The trick: analyse the circuit using $V(t) = V_0\, e^{i\omega t}$ instead. At the very end, take the real part $\text{Re}\{V(t)\} = V_0 \cos(\omega t)$ to get the physical voltage back. Why is this so much easier? Because differentiation of $e^{i\omega t}$ is just multiplication by $i\omega$, and integration is division by $i\omega$. Every differential equation in the circuit becomes simple algebra. This is how power grids, audio amplifiers, phone chargers, and motor controllers are designed today. The same constant $e$ that dropped out of the compound-interest limit in §1 runs the entire electrical industry — a unification that took mathematicians 300 years to see.
>
> Not on any pre-university syllabus. AP Physics 2 touches AC qualitatively; formal complex-exponential analysis shows up in first-year electrical engineering. Worth knowing the road continues.

## Connections

- **Prerequisite:** [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]] — the discrete starting point; $(1 + r)^n \to e^{rt}$ in the continuous limit.
- **Prerequisite:** [[Laws of Indices]] — every manipulation of $e^{kt}$ uses index laws; crucial for solving for $t$ algebraically.
- **Prerequisite:** [[Percentage Calculations (Vocab)|Percentage Calculations]] — the multiplier method underlies the discrete form.
- **Companion — $e$ as a number:** [[Euler's Number]] — this card is $e$-as-a-growth-shape; the companion handles $e$-as-a-number (three equivalent definitions, irrationality proof via $q!$, transcendence, the 250-year history).
- **Uses (indirectly — see [[Euler's Number]] for the proof):** [[Binomial Theorem]] — expanding $(1 + 1/m)^m$ is how the limit defining $e$ is proved to converge.
- **Uses:** [[Differentiation]] — the derivative identity $\dfrac{d}{dx} e^{kx} = k e^{kx}$ is the calculus foundation of this card.
- **Leads to:** [[Logarithms]] — the inverse function $\ln$, needed every time the unknown is trapped in an exponent.
- **Leads to:** [[Integration]] — solves the defining differential equation $\dfrac{dy}{dt} = ky$ by separation of variables.
- **Leads to:** [[Differential Equations]] — the general framework; this card is the simplest non-trivial case.
- **Real-world companion:** [[Financial Literacy (Life)]] — continuous compounding, APR vs APY at high compounding frequency, and why insurance "reserve rates" hide the true IRR.
- **Cross-curricular:** Physics (radioactive decay, Newton's cooling, RC-circuit discharge); Biology (population dynamics, pharmacokinetics); Chemistry (first-order reaction kinetics).

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $e$ | `e` | The constant itself |
| $e^{kt}$ | `e^{kt}` | Multi-char exponent in braces |
| $e^{-\lambda t}$ | `e^{-\lambda t}` | Decay form |
| $\ln x$ | `\ln x` | Natural log; autospaced |
| $\log_b x$ | `\log_b x` | General-base log |
| $\displaystyle\lim_{n \to \infty}$ | `\lim_{n\to\infty}` | Subscript on `\lim` |
| $\dfrac{dy}{dt}$ | `\dfrac{dy}{dt}` | Display-size derivative |
| $T_{1/2}$ | `T_{1/2}` | Half-life subscript |
| $\displaystyle\sum_{n=0}^{\infty}$ | `\sum_{n=0}^{\infty}` | Sum to infinity; use `\displaystyle` inline if needed |

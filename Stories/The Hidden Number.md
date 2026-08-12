---
chinese: 隐藏的数 (yǐncáng de shù) — e 的250年发现史
prerequisites:
  - "[[Euler's Number]]"
  - "[[Logarithms]]"
  - "[[Exponential Function]]"
leads_to:
  - "[[Stories/The Argument for i]]"
  - "[[Stories/The Bernoulli Family]]"
tags:
  - type/story
  - subject/mathematics
  - era/17c
  - era/18c
  - era/19c
  - cast/napier
  - cast/saint-vincent
  - cast/huygens
  - cast/mercator
  - cast/bernoulli-jacob
  - cast/leibniz
  - cast/euler
  - cast/hermite
  - region/europe
---

# The Hidden Number 隐藏的数

> *"Some numbers we choose. Other numbers find us."*
>
> *Five mathematicians, four countries, two-and-a-half centuries — and one constant that kept showing up unannounced, in problem after problem, before anyone realized they were all the same number.*

![[the-hidden-number-banner.png|697]]

## What this card is for

[[Euler's Number]] — the pedagogical card on $e$ — gives the formal definitions, the irrationality proof, the transcendence statement, the calculus identity $(e^x)' = e^x$, the ubiquity. It does the math.

This card does the **story**. From John Napier's 1614 log tables to Charles Hermite's 1873 transcendence proof, $e$ was the longest stalking-horse in mathematical history — repeatedly noticed, repeatedly missed, finally named. The story matters because the *kind* of number $e$ turns out to be — found rather than chosen — is exactly what mathematicians mean by **"natural."** The last section of this card unpacks that word, which is a question worth taking seriously and is load-bearing for understanding why every modern calculus course works in base-$e$ instead of base-10 or base-2.

## Cast of Characters

- **John Napier** (1550–1617) — Scottish laird and amateur mathematician at Merchiston Castle. Spent twenty years building the first table of logarithms (1614) so astronomers could replace painful multiplications with easy additions. The constant $e$ is hiding in his tables, unnamed.
- **Henry Briggs** (1561–1630) — Oxford mathematics professor; took Napier's logarithms and converted them to base 10 for everyday calculation, creating the "common" log. Lifelong correspondent of Napier; the friendship is its own small story.
- **Grégoire de Saint-Vincent** (1584–1667) — Belgian Jesuit. Spent forty years trying to square the circle; failed (because it's impossible — see [[Stories/The Calculus Priority Dispute|The Calculus Priority Dispute]] for why squaring-the-circle was finally settled). Failed beautifully, though: discovered the area-under-hyperbola property that *defines* the natural logarithm, without realising it.
- **Christiaan Huygens** (1629–1695) — Dutch polymath; pendulum clocks, Saturn's rings, wave optics, and the formalisation of Saint-Vincent's hyperbolic logarithm. Did not give the constant a name.
- **Nicolaus Mercator** (~1620–1687) — Danish-born, German-raised, lived in London. Gave us **the word "natural logarithm"** in his 1668 *Logarithmotechnia*. Wrote the first power series for $\ln(1 + x)$. The reason we call it "natural" lives at his desk.
- **Jacob Bernoulli** (1655–1705) — Swiss; the eldest of the [[Stories/The Bernoulli Family|Bernoulli mathematical dynasty]]. In 1683, while working out continuously-compounded interest, he proved the limit $\lim_{n\to\infty}(1 + 1/n)^n$ exists and lies between 2 and 3. He didn't compute it precisely; he didn't connect it to Saint-Vincent's hyperbolic area; he died not knowing his number was the same number.
- **Gottfried Leibniz** (1646–1716) — co-inventor of calculus (see [[Stories/The Calculus Priority Dispute]]). In letters to Huygens around 1690, used the letter **$b$** for the constant we now call $e$. The letter didn't stick.
- **Leonhard Euler** (1707–1783) — Swiss. The protagonist. The most prolific mathematician in history (886 papers + books, despite blindness in his last seventeen years). In 1727 he wrote $e$ for the first time; in 1737 he proved it irrational; in 1748 he published *Introductio in Analysin Infinitorum* and tied every previous thread together.
- **Charles Hermite** (1822–1901) — French; in 1873 proved $e$ is transcendental, putting it beyond the reach of all integer-coefficient polynomials forever.

## 中文锚点

**核心论题**：为什么 $e$ 和 $\ln$ 都被叫做「自然」(natural)？

答：因为没有人「选」它们。数学一次又一次从不同的方向独立发现这个数 —— 复利里出现、双曲线下面积里出现、链式法则里出现、级数里出现 —— 而每一次都是同一个数。**「自然」就意味着「不被选择」**。这与「常用对数」(base 10) 形成对比：**10 是因为人有十根手指 —— 那是「人类自然」；$e$ 是「数学自然」**。整张卡片讲的就是这个发现过程：250 年里，五个数学家，四个国家，从五条互不相干的小径上，各自走到同一个数面前。

**故事梗概**：

- 1614：苏格兰的 Napier 发表第一张对数表。$e$ 已经躲在表格的基底里，但没人意识到。
- 1647：比利时的 Saint-Vincent 在「化圆为方」失败的过程中，发现 $y = 1/x$ 下的面积具有对数性质。$e$ 是这个面积等于 1 的那个 $a$ 值，没被命名。
- 1668：丹麦-德国的 Mercator 在《对数学》一书中第一次写下 "logarithmus naturalis" —— **「自然对数」这个词正式诞生**。理由是：这个对数从积分 $\int dx/x$ 中自然冒出来，不需要选择基底。
- 1683：瑞士的 Jacob Bernoulli 算复利时遇到 $\lim_n (1+1/n)^n$，发现它收敛于 2 和 3 之间。还是不知道这是什么数。
- 1690：Leibniz 在给 Huygens 的信里把它叫 "$b$"。
- 1727/1748：Euler 写下 "$e$"，证明它是无理数，写出 $e = \sum 1/k!$，给出 $e^{i\pi} + 1 = 0$。**所有线索在一个人的脑子里汇合。**
- 1873：Hermite 证明 $e$ 是超越数 —— 比无理还要更"野"。

---

## Act I — Napier's tables: a constant in disguise (1614–1618)

![[the-hidden-number-astronomy.png|640]]
*A late-16th-century scholar by candlelight with an armillary sphere, a celestial globe, a star map, and a telescope on the wall — the working environment of the pre-Newtonian astronomer. This is the room Napier built his logarithms for.*

In 1594 the Scottish laird **John Napier**, age 44, sat down at his castle library and decided to spend the next twenty years inventing logarithms. **The motivation was astronomy.**

The late 1500s were the golden age of *pre-telescope* observational astronomy. **Tycho Brahe** at Uraniborg in Denmark had spent twenty years compiling the most precise stellar and planetary catalogue in human history — measuring positions to arc-minute accuracy with instruments the size of cathedrals. **Johannes Kepler** had just inherited Tycho's data when Tycho died in 1601, and was about to spend two decades grinding through it to derive what we now call Kepler's three laws of planetary motion. The work was bottlenecked not by Tycho's measurements — those were astonishingly good — but by *arithmetic*. A single Mars-orbit fit required *thousands* of multi-step multiplications of ten-digit numbers, each multiplication taking the better part of an hour, each producing errors that propagated through every subsequent step. Kepler is reported to have done the orbit calculation *eight times* before getting an answer he trusted, an effort that cost him roughly four years.

Napier's vision: turn multiplication into addition by indexing every number to a *power of a small base*. If you can convert "multiply $7234 \times 8591$" into "add the index of $7234$ to the index of $8591$ and look up the result," a problem that took thirty minutes now takes thirty seconds. The astronomers' four-year orbit fit becomes a six-month orbit fit. *Napier's invention was an arithmetic accelerator built specifically to unblock astronomy.*

Twenty years of single-handed table computation later, the *Mirifici Logarithmorum Canonis Descriptio* appeared in 1614. The book made Napier famous overnight precisely because the astronomers — Kepler especially — recognised what they had been handed. Kepler dedicated his 1620 *Ephemerides* to Napier; he later wrote that he had "halved his own arithmetic burden." Briggs travelled north from Oxford to meet Napier; they spent a fortnight together and Briggs convinced Napier the system would be cleaner in base 10.

The thing Napier himself never knew: his original tables (before Briggs's base-10 reform) were *equivalent* to natural logarithms with one minor convention difference. The constant $e$ — the implicit base — was lurking inside the structure of the tables, defining how everything was scaled. **Nobody noticed for decades.** When the 1618 English translation came out (probably with William Oughtred's appendix), the appendix included a correction-table that made the natural-log structure visible — but still, nobody named the constant. It was a fundamental mathematical object hidden inside an engineer's lookup table.

> *Napier died in 1617, three years after publication. He never met the number that lived in his book.*

## Act II — Saint-Vincent's hyperbola (1647–1661)

The Belgian Jesuit **Grégoire de Saint-Vincent** spent his life trying to *square the circle* — the ancient Greek problem of constructing a square with the same area as a given circle, using only compass and straightedge. He failed. (As we now know, the problem is impossible — proved 235 years later by Lindemann's 1882 transcendence-of-$\pi$ result.)

But the techniques Saint-Vincent invented to attack the problem accidentally proved a different theorem of staggering depth: **the area under the hyperbola $y = 1/x$ from $x = 1$ to $x = a$ behaves exactly like a logarithm.**

Write $A(a)$ for that area. Saint-Vincent's two claims:

- $A(1) = 0$ — *trivially*, since the region collapses: the integral from 1 to 1 is zero.
- $A(ab) = A(a) + A(b)$ — *less trivially*. This is the load-bearing claim, and it deserves a moment.

### Why $A(ab) = A(a) + A(b)$ — the rescaling trick

![[saint-vincent-rescaling-animated.svg|640]]

*Watch the strip slide right.* The width of $[1, 3]$ stretches by a factor $c$ to become $[c, 3c]$. As it slides, the heights underneath it shrink by exactly $1/c$ — because that's what $y = 1/x$ does. Width up by $c$, height down by $1/c$, area unchanged. The shaded patch keeps the same area no matter where on the curve it sits.

That's the trick. Now the algebra:

The hyperbola $y = 1/x$ has a special property no other power curve has: **it is invariant under the rescaling $x \mapsto cx, \, y \mapsto y/c$ for any positive $c$.** Stretch horizontally by a factor of $c$ and squash vertically by the same factor, and the curve sits in exactly the same place. (Substituting $x' = cx$, $y' = y/c$ into $y = 1/x$ gives $cy' = 1/(x'/c) = c/x'$, which simplifies back to $y' = 1/x'$. Same equation.)

Apply that rescaling to a strip of area under the curve:

- Take the strip from $x = 1$ to $x = b$. Its area is $A(b)$.
- Rescale by $c = a$: the strip now sits from $x = a$ to $x = ab$. Heights have shrunk by $1/a$; widths have stretched by $a$. **Heights and widths multiplied by reciprocals, so the area is unchanged.**

So the area under the hyperbola from $x = a$ to $x = ab$ equals the area from $x = 1$ to $x = b$:

$$\underbrace{A(ab) - A(a)}_{\text{strip from } a \text{ to } ab} \;=\; \underbrace{A(b)}_{\text{strip from } 1 \text{ to } b}$$

Rearranging: $A(ab) = A(a) + A(b)$. **The hyperbola's scale-invariance is exactly what turns multiplication of inputs into addition of areas.** That property *is* the logarithm property. No other curve has it; only $1/x$.

A concrete instance, with $a = 2$ and $b = 3$:

![[saint-vincent-hyperbola.svg|600]]

The blue strip is $A(2)$. The green strip is $A(6) - A(2)$ — and by the rescaling argument, that green area is the same as the area of $[1, 3]$, which is $A(3)$. So $A(6) = A(2) + A(3)$. Multiplication of the inputs ($2 \times 3 = 6$) became addition of the areas. That is what a logarithm *does*.

### What Saint-Vincent had — and didn't have

He had *the discovery*: the area under $1/x$ behaves like a logarithm. He had the additivity property, the rescaling argument (in geometric form, before calculus notation made it crisp), and the realisation that this geometrically-defined function had all the algebraic properties of a logarithm.

What he didn't have: **a name for its base.** The base of the geometric logarithm is *the value of $a$ where $A(a) = 1$* — the place where the shaded region under $1/x$ from 1 to $a$ has unit area. That value, of course, is $e \approx 2.71828\ldots$. But Saint-Vincent never wrote it as a number; he just noticed the area-equals-1 point existed and moved on. The constant was *defined by his geometry* but invisible *as a number*.

**Christiaan Huygens** picked up the work in the 1660s, sharpened the proof, and wrote the relationship in modern form. Huygens explicitly noted that the "hyperbolic logarithm" was a kind of logarithm. But to him too, the *base* of this logarithm was an implicit geometric quantity rather than a number with a name on the number line.

For thirty years, mathematicians knew there existed a "natural" hyperbolic logarithm. They knew the base was *some specific positive number* defined by the geometry. They just didn't know what it was. The number $e$ was the elephant in the room — defined by an integral, written implicitly in a hundred manuscripts as a constant of integration, but never written down as a decimal on its own.

## Act III — Mercator coins "natural logarithm" (1668)

In 1668, **Nicolaus Mercator** — born Niklaus Kauffman in Eutin (now in northern Germany), educated in Copenhagen, working in London — published *Logarithmotechnia*. The book did three things mathematicians cared about:

1. Gave the **first power-series expansion** of the logarithm:
$$\ln(1 + x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dfrac{x^4}{4} + \cdots, \quad \lvert x \rvert < 1.$$
2. Showed how to compute logarithms to arbitrary precision using only addition and subtraction (no Napier-style table-construction effort needed).
3. **Named the kind of logarithm produced by his series.** He called it ***logarithmus naturalis*** — *natural logarithm* — because the series fell out of the integral $\int dx/(1+x)$ *naturally*, without anyone choosing a base. The base was forced by the structure of the integral.

This is the moment the word "natural" enters the story. Mercator's reasoning, paraphrased: *every other logarithm has a chosen base — base 10 because we have ten fingers, base 2 because of doubling, whatever. This logarithm has no chosen base. It came directly out of the calculus. So this one is the natural one.*

The number $e$ — still unnamed at the surface — was the implicit base of Mercator's natural log. Within Mercator's framework, *$e$ was defined as the number whose logarithm is 1*: the place where the unbidden ladder hit the unbidden top step.

> *The whole reason we say "natural log" today is Mercator's word. He picked it because the series came from calculus without him having to choose a base. Two hundred fifty years later, every calculus textbook still says "natural" for exactly that reason.*

## Act IV — Bernoulli's compound interest (1683)

**Jacob Bernoulli** in Basel, fifteen years after Mercator, was working a different problem: *what happens if a bank pays interest continuously?* If you have £1 at 100% annual interest compounded once a year, after a year you have £2. If they compound twice a year (50% each half), you get £$(1 + 1/2)^2 = £2.25$. Compound four times a year and it's £$(1 + 1/4)^4 \approx £2.44$. Twelve times: £$(1 + 1/12)^{12} \approx £2.61$. Three hundred sixty-five times: £$\approx 2.7146$. You see where this is going.

Bernoulli proved the limit $\lim_{n\to\infty}(1 + 1/n)^n$ *exists* — i.e., your bank account doesn't blow up to infinity even with infinitely-frequent compounding — and showed it lies strictly between $2$ and $3$. The exact value he could not pin down; eight or so decimal places of computation by hand was the technological ceiling.

**He didn't connect his number to Mercator's hyperbolic constant.** He didn't know it was the same as the implicit base of Napier's log tables. He just had a limit that came out of compound interest, and he proved it was bounded.

This is the most famous "shy" appearance of $e$ in the history of math. A solid proof that the constant exists and lies in $(2, 3)$ — but the constant itself remained one unconnected sighting in a forty-year stack of unconnected sightings.

In letters from around 1690, **Leibniz** — deep into his calculus work — used the letter **$b$** for what we now call $e$. He didn't propose it as a universal name. It was a placeholder: *"this constant keeps coming up; let me call it $b$ until somebody picks a real name."* Huygens, in correspondence, used different ad-hoc letters too. There was no consensus.

## Act V — Euler unifies, names, and proves (1727–1748)

**Leonhard Euler**, born in Basel in 1707, twenty years after Bernoulli's compound-interest result, became Bernoulli's student and then surpassed every mathematician of his generation. (Sometimes literally: there are several theorems Euler proved that the field hadn't even *attempted* before — he solved the Königsberg bridge problem and accidentally founded graph theory; he summed $\sum 1/n^2 = \pi^2/6$ and accidentally founded analytic number theory; etc.)

In a 1727 unpublished manuscript on **the explosive forces of cannons** (because of course Euler was doing applied ballistics in his spare time), Euler first wrote the letter ***$e$*** for our constant. Why $e$? Three competing theories:

1. **"$e$ for *exponential*"** — the simplest, probably correct. Euler used $e$ in contexts where it was the base of an exponential function.
2. **"$e$ as the next available vowel"** — Euler had already used $a$, $b$, $c$, $d$ for other constants. Vowel-letters are easy to read; $e$ was free.
3. **"$e$ for *Euler*"** — romantic but almost certainly wrong. Euler was famously not the self-promoting type. He named theorems after Fermat, Bernoulli, Diophantus — not himself.

History never settled between (1) and (2). The point is: in 1727, a Swiss 20-year-old gave the constant a one-letter name, and the name stuck.

Then, across two landmark works, Euler dragged every previous thread together:

- **1737** — Euler proved $e$ is **irrational** using a continued-fraction expansion. First proof that $e$ cannot be written as $p/q$. (See [[Euler's Number]] for the cleaner 1748-style proof reproduced in modern notation.)
- **1748** — *Introductio in Analysin Infinitorum*, Euler's masterwork. In this single book Euler:
  1. **Defined $e$ as the infinite series** $e = \sum_{k=0}^{\infty} 1/k!$
  2. **Proved Bernoulli's compound-interest limit equals this series.**
  3. **Linked the series to the hyperbolic-area constant** of Saint-Vincent and Huygens — proving that Bernoulli's number, Mercator's natural-log base, Saint-Vincent's hyperbolic base, Napier's implicit base, and Leibniz's "$b$" were *all the same number*.
  4. **Derived $e^{i x} = \cos x + i \sin x$** — what we call **Euler's formula**. Set $x = \pi$ and you get $e^{i\pi} + 1 = 0$, the most famous equation in mathematics.

After *Introductio*, the dispersed sightings converged. The same constant that had haunted log tables for 130 years had a name, a series, an integral definition, an irrationality proof, and a place in the structure of the complex numbers. Euler turned $e$ from a coincidence into a citizen.

## Act VI — Hermite's transcendence proof (1873)

For 125 years after *Introductio*, mathematicians knew $e$ was irrational but could not say whether it was *algebraic* (the root of some polynomial with integer coefficients) or *transcendental* (not the root of any such polynomial).

In 1873 the French mathematician **Charles Hermite** ended the question. He proved $e$ is transcendental — for any non-zero polynomial $P$ with integer coefficients, $P(e) \neq 0$. The proof runs about 20 pages and uses a delicate construction involving auxiliary polynomials, integrals against $e^{-x}$, and an inequality between an integer and a strictly-between-0-and-1 number that yields a contradiction. (See [[Euler's Number]] §"Transcendence — stated, not proved" for an outline.)

Hermite's method was so sharp that nine years later, in **1882**, **Ferdinand von Lindemann** adapted it to prove the transcendence of $\pi$. The Lindemann result finally killed the 2000-year-old Greek problem of *squaring the circle*: you cannot construct a square equal in area to a given circle using compass and straightedge, because such a construction would require $\pi$ to be algebraic, and Lindemann had just proved it isn't.

So: a *cannon-calculation constant from a Swiss 20-year-old's notebook* ended up, via Hermite and Lindemann, *killing an Ancient Greek geometry problem*. The thread that started with Napier's log tables in 1614 closed an investigation that had been open since Anaxagoras around 460 BC. **The longest unbroken thread in the history of mathematics.**

---

## Why we call it "natural"

The load-bearing question: *why exactly are $e$ and $\ln$ "natural"?*

The shortest correct answer: **because mathematics keeps producing them without anyone asking.** "Natural" in mathematics has a technical meaning: *not chosen — forced by the structure*.

### Five paths converge on the same number

Each is a different question; each gives the same answer. *That convergence is what makes $e$ natural.*

1. **Compounding.** Solve "how much does £1 grow at 100% interest compounded continuously?" — the answer is $\lim_n (1 + 1/n)^n = e$. Bernoulli's path (1683).

2. **Function = its own derivative.** Solve "find $f$ with $f'(x) = f(x)$ and $f(0) = 1$" — the answer is $f(x) = e^x$. (See [[Differentiation Rules]] for the proof.) Euler's path (1748).

3. **Hyperbolic area.** Solve "find $a$ such that the area under $1/x$ from $1$ to $a$ equals 1" — the answer is $a = e$. Saint-Vincent's path (1647).

4. **Series.** Solve "what does $1 + 1 + 1/2! + 1/3! + 1/4! + \cdots$ converge to?" — the answer is $e$. Euler's series definition (1748).

5. **Probability.** Solve the *secretary problem* — "interview $n$ candidates, hire the first one better than all you've seen so far; what's the optimal $n/k$ cutoff?" — the answer involves $1/e$. Solve the *derangement problem* — "what fraction of permutations of $n$ items have no fixed point?" — the answer approaches $1/e$. Solve "Poisson with mean 1, what's $P(X = 0)$?" — answer: $1/e$.

Five different questions. Five mathematicians (or generations of mathematicians) walking five different paths from five different motivations. Same answer every time.

**That is what "natural" means.** Not "common" (which means humans use it) — *unbidden*. Mathematics keeps producing the constant without anyone choosing it.

### "Natural" vs "common"

Compare to **base 10**. The *common logarithm* $\log_{10}$ exists because humans have ten fingers. We count in base 10 because of anatomy. There is nothing mathematically special about 10 — pick any culture with $b$ fingers and they'd use base $b$ logarithms. The Maya used base 20 (ten fingers + ten toes). The Babylonians used base 60 (counting joints with the thumb across the four fingers — 12 joints × 5 fingers = 60). Computer scientists use base 2 (binary). All of these are *anthropocentric* or *technological* — chosen to fit human or machine convenience.

The natural log $\ln$ is different. **No one had to choose its base.** It emerged from the integral $\int dx/x$ — *the simplest possible reciprocal integrand* — without anyone supplying a parameter. The base $e$ is whatever value of $a$ makes $\int_1^a dx/x = 1$. There's no choice involved; you compute the area, declare *that's the unit*, and the base is the resulting number. Inevitable.

The same logic gives $\frac{d}{dx}\ln x = 1/x$ — *clean, no constants*. Every other base $\log_a x$ has derivative $\frac{1}{x \ln a}$, which adds an unwelcome constant. *Only* $\ln$ has the clean derivative because *only* $\ln$ wasn't chosen.

**"Natural" = "unbidden."** The fact that the same number $e$ shows up in five independent contexts — calculus, probability, hyperbolic geometry, compound interest, infinite series — is *evidence that it was already there*, waiting to be found. We don't choose $e$. It chooses us.

### The companion: $\pi$

The other classical "natural" constant. $\pi$ is "natural" the same way $e$ is — it emerges without choice. *Every* circle, regardless of size, has the same ratio $C/d$. There's no parameter to set, no convention to pick. The Greeks knew $\pi$ was natural in this sense centuries before they knew it was irrational, centuries before they knew it was transcendental.

When **Euler** (in 1748) wrote $e^{i\pi} + 1 = 0$, he was tying together five constants — $e$, $\pi$, $i$, $1$, $0$ — three of which are "natural" in the unbidden sense ($e$, $\pi$, $1$) and two of which are *given* by the structure of the field of complex numbers ($i$, $0$). The identity is famous because it shows the natural constants are *related to each other* in the deepest possible way: a single transcendental equation links them all. **The natural is not arbitrary; the natural is connected.**

That is the answer to "why natural?" — it's the technical word mathematics uses for *unbidden*, *unforced*, *not chosen*, and the reason we trust it more than the chosen alternatives. **Choose carefully and you get a tool. Don't choose, and the math shows you what was already there.**

---

## Cultural ripples — where $e$ shows up

A short tour of the modern presence:

- **Calculus.** $e^x$ is the function whose derivative is itself, the unique solution of $f' = f$ with $f(0) = 1$. Every differential equation involving exponential growth or decay reduces to a multiple of $e^x$. (See [[Differentiation Rules]] and [[Standard Integrals]].)
- **Compound finance.** Continuous compounding at rate $r$ gives $e^{rt}$ — banks since 1683 (and especially since the 1970s when continuous-compounding became the standard convention) live on $e$.
- **Population biology.** Exponential population growth and radioactive decay are both $N(t) = N_0 e^{kt}$ — life sciences run on $e$ even when biologists don't see the integration.
- **Statistics.** The normal distribution PDF is $\dfrac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\tfrac{1}{2}\left(\tfrac{x-\mu}{\sigma}\right)^2\right)$ — *both* $e$ and $\pi$ inside the same expression. (See [[Normal Distribution]].) Poisson distributions involve $e^{-\lambda}$. The "37% rule" $1/e \approx 0.368$ rules secretary-problem-style optimal stopping.
- **Quantum mechanics.** Wavefunctions are $\psi(x, t) = e^{i(kx - \omega t)}$ — Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ is what makes quantum mechanics computable instead of an awkward dance of $\sin$ and $\cos$. Schrödinger's equation has $e$ baked into its structure.
- **Information theory.** Shannon entropy is naturally written in base 2 (bits) or base $e$ (nats). The latter — *natural units of information* — is what physicists and statisticians use because the calculus is cleaner.
- **Electrical engineering.** RC circuits decay as $V(t) = V_0 e^{-t/\tau}$. The time constant $\tau$ is *literally defined* as the time for the voltage to fall to $1/e$ of its starting value.

In every one of these fields, $e$ is not a *choice* — it's what you arrive at when you do the math without imposing artificial conventions. **The same property — unbidden-ness — that makes $e$ "natural" is what makes it ubiquitous.** The two are the same fact stated twice.

---

## Where this surfaces in the vault

- **[[Euler's Number]]** — the pedagogical home: three definitions of $e$, irrationality proof, transcendence statement, taxonomy of $e$ in the number system. *This Stories card is the historical companion; that one is the math.*
- **[[Logarithms]]** — what makes $\ln$ a logarithm in the first place; the base-change formula linking it to $\log_{10}$.
- **[[Exponential Function]]** — $e^x$ as the one function whose derivative equals itself.
- **[[Differentiation Rules]]** — every appearance of $e^x$ and $\ln x$ in the standard derivative table.
- **[[Standard Integrals]]** — the $1/x \to \ln \lvert x \rvert$ row, including the absolute-value subtlety.
- **[[Normal Distribution]]** — $e$ inside the bell-curve formula.
- **[[Stories/The Calculus Priority Dispute]]** — companion Stories card on Newton vs Leibniz; the calculus that produced Mercator's natural log was the same calculus Newton and Leibniz invented.
- **[[Stories/The Argument for i]]** *(sibling story)* — the parallel 400-year discovery of $i = \sqrt{-1}$. Both stories are about constants found rather than chosen. Their threads tie together at Euler's identity $e^{i\pi} + 1 = 0$ — the moment Hidden Number's protagonist ($e$) and Argument for $i$'s protagonist ($i$) turn out to be the same conversation.
- **[[Stories/The Bernoulli Family]]** *(forthcoming)* — Jacob Bernoulli's compound-interest discovery is a chapter of the larger Bernoulli-family arc.

---

## Receipts

- **Edwards, C. H.** — *The Historical Development of the Calculus* (Springer, 1979). The standard pedagogical history of calculus origins. Chapters 4–6 cover the natural-log discovery thread.
- **Stillwell, John** — *Mathematics and Its History* (3rd ed, Springer, 2010). Chapter 9 on the discovery of $e$ and $\ln$. Approachable and sourced.
- **Maor, Eli** — ***e: The Story of a Number*** (Princeton, 1994). A book-length popular treatment of exactly this card's topic. Highly readable. The single best lay reference on $e$.
- **Euler, Leonhard** — *Introductio in Analysin Infinitorum* (1748). The primary source. Chapter 7 introduces $e$ via series; Chapter 8 introduces logarithms. English translations (J. D. Blanton, 1988) are still in print.
- **Mercator, Nicolaus** — *Logarithmotechnia* (London, 1668). The book that coined "logarithmus naturalis." Available via Google Books / archive.org for those who read 17th-century Latin.
- **Hermite, Charles** — *Sur la fonction exponentielle* (1873). The transcendence proof. Reproduced in Burger & Tubbs, *Making Transcendence Transparent* (Springer, 2004), with modern annotations.

> Memory rule: future Stories cards on $\pi$ (when written) or on the transcendence story will likely cross-cite this card and be cross-cited by it.

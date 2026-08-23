---
chinese: 棣莫弗定理实战 (Dìmòfú dìnglǐ shízhàn)
prerequisites:
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[Complex Numbers]]"
  - "[[Binomial Theorem]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Summation of Series]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/complex-numbers
  - domain/trigonometry
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/IB-AA
  - syllabus/9231-2-5
  - type/technique
  - type/proof
  - notation/complex-exponential
  - misconception/taking-the-real-part-too-early
  - misconception/forgetting-convergence
  - misconception/half-angle-sign
---

# De Moivre at Work 棣莫弗定理实战

> *A sawmill is one blade, spinning. What makes it a mill is everything bolted around the blade: the jigs that feed it timber, the guides that turn one cut into planks, mouldings, joints. De Moivre's theorem is one line —* $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ *— and Paper 2 is the mill built around it: an identity for* $\cos 5\theta$ *manufactured in four lines, a power of* $\sin\theta$ *flattened for integration, a sum of fifty cosines collapsed to a single fraction. One blade, three jigs. Learning the jigs is this topic.*

## The one move behind everything

Write $z = \cos\theta + i\sin\theta = e^{i\theta}$, so that **powers of $z$ are multiple angles**: $z^r = \cos r\theta + i\sin r\theta$ ([[Euler's Formula and De Moivre's Theorem]]). Every technique below is the same three-step move in different clothing:

1. **Bundle** the trigonometry into powers of $z$ — a real question becomes a complex one.
2. **Use algebra that only works for powers** — the [[Binomial Theorem]], or a geometric-series sum — machinery trigonometry does not have.
3. **Unbundle** at the end: equate real and imaginary parts, or take $\operatorname{Re}$ / $\operatorname{Im}$.

The trade is always the same: trigonometric identities are hard currency, powers are easy currency, and $z = e^{i\theta}$ is the exchange booth open in both directions.

### 中文锚点 (Chinese Anchor)

棣莫弗定理本身只有一句话——$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$——但考卷考的是**用它干活**，活儿分两类。**第一类：造恒等式。** 正着用：把 $(c + is)^5$ 按二项式定理展开，实部与虚部各归各位，$\cos 5\theta$、$\sin 5\theta$ 的展开式当场"现造"出来，不用背；反着用：把 $\cos\theta$ 写成 $\frac{1}{2}(z + \frac{1}{z})$（其中 $z = e^{i\theta}$），$\sin^6\theta$ 六次方一展开、同类项一配对，就得到只含 $\cos 2\theta, \cos 4\theta, \cos 6\theta$ 的**降幂公式**——高次幂的积分立刻变得可做。**第二类：求和。** 一列余弦或正弦的和（比如 $\sum \binom{n}{r}\sin r\theta$）直接求，求不动；把它看成复数级数 $\sum \binom{n}{r} z^r$ 的**虚部**（余弦和就看实部），先用二项式定理或等比数列求和公式把复数的和一口气算完，最后再取实部或虚部——这就是 **C+iS 方法**，名字的意思就是"把 $C$（余弦和）与 $iS$（正弦和）捆在一起算"。两个反复出现的小技巧要单独记：**提半角**，$1 + e^{i\theta} = 2\cos\frac{\theta}{2}\,e^{i\theta/2}$，把难看的和式变成一个模长乘一个方向；**乘共轭**，无穷级数的复数分母靠它化成实数。还有一句考场保命的话：无穷等比求和必须先说明 $\lvert z \rvert < 1$，否则整个求和不成立。

## Jig 1 — multiple angles forward, and the exam's two twists

Recall from [[Euler's Formula and De Moivre's Theorem]] §5: expand $(\cos\theta + i\sin\theta)^n$ by the binomial theorem, sort by real/imaginary, and $\cos n\theta$, $\sin n\theta$ fall out — identities manufactured, never memorised. The exam then adds a twist. A real Paper 2 pair, both "show that" questions:

**Twist A — divide through for sec / cosec / tan.** *Show that $\ \operatorname{cosec} 5\theta = \dfrac{\operatorname{cosec}^5\theta}{5\operatorname{cosec}^4\theta - 20\operatorname{cosec}^2\theta + 16}$.*

*Tool: De Moivre, then the binomial theorem, then match imaginary parts.* Write $c = \cos\theta$, $s = \sin\theta$. De Moivre gives the same object two ways:

$$\cos 5\theta + i\sin 5\theta = (c + is)^5 = c^5 + 5c^4(is) + 10c^3(is)^2 + 10c^2(is)^3 + 5c(is)^4 + (is)^5.$$

Sort the right side by powers of $i$ (using $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, $i^5 = i$):

$$= \underbrace{\left(c^5 - 10c^3 s^2 + 5c s^4\right)}_{\text{real}} + i\,\underbrace{\left(5c^4 s - 10c^2 s^3 + s^5\right)}_{\text{imaginary}}.$$

Two complex numbers are equal exactly when their real parts match *and* their imaginary parts match — so the imaginary part of the right side **is** $\sin 5\theta$ (that is all $\operatorname{Im}$, "the imaginary part of", means):

$$\sin 5\theta = 5c^4 s - 10c^2 s^3 + s^5 = 5(1-s^2)^2 s - 10(1-s^2)s^3 + s^5 = 16s^5 - 20s^3 + 5s \quad\text{(every } c^2 \text{ traded for } 1 - s^2\text{)}.$$

*Tool: the twist — divide numerator and denominator by the top power, $s^5$.*

$$\operatorname{cosec} 5\theta = \frac{1}{16s^5 - 20s^3 + 5s} = \frac{1/s^5}{16 - 20/s^2 + 5/s^4} = \frac{\operatorname{cosec}^5\theta}{5\operatorname{cosec}^4\theta - 20\operatorname{cosec}^2\theta + 16}. \qquad\blacksquare$$

(The mirror question — $\cos 5\theta = 16c^5 - 20c^3 + 5c$ divided through by $c^5$ for $\sec 5\theta$ — is a real paper from a different session. Same jig, other part.) The **tan variant** the syllabus names starts from the quotient of the two bracketed expansions above, then **divides the whole thing — every term, top and bottom — by $c^5$**, so each term becomes a power of $t = \tan\theta$:

$$\tan 5\theta = \frac{\sin 5\theta}{\cos 5\theta} = \frac{5c^4s - 10c^2s^3 + s^5}{c^5 - 10c^3s^2 + 5cs^4} = \frac{\frac{5c^4s}{c^5} - \frac{10c^2s^3}{c^5} + \frac{s^5}{c^5}}{\frac{c^5}{c^5} - \frac{10c^3s^2}{c^5} + \frac{5cs^4}{c^5}} = \frac{5t - 10t^3 + t^5}{1 - 10t^2 + 5t^4}.$$

(Watch one term to see the mechanism: $\frac{5c^4 s}{c^5} = 5\,\frac{s}{c} = 5t$, and $\frac{10c^2s^3}{c^5} = 10\,\frac{s^3}{c^3} = 10t^3$ — the division manufactures exactly one $t$ per surviving $s$.) Why $c^5$? It is the power that makes the leading denominator term $1$ — the same divide-by-the-top-power move as Twist A, aimed at $\tan$ instead of $\sec$.

**Twist B — the identity prices a polynomial's roots.** Stare at $\sin 5\theta = 16s^5 - 20s^3 + 5s$ from the other side: the right-hand expression is a quintic *in* $s$. Choose $\theta$ so the left side vanishes — $\theta = \frac{k\pi}{5}$ — and each such $\theta$ hands you a root of the polynomial:

$$16x^5 - 20x^3 + 5x = 0 \quad\text{has roots}\quad x = \sin\tfrac{k\pi}{5}, \qquad k = -2, -1, 0, 1, 2.$$

Exact values of $\sin 36°$, $\sin 72°$ from a quintic you could not otherwise touch — real exam follow-ups ask precisely this, sometimes routed through [[Symmetric Functions of Roots]] (products and sums of the $\sin\frac{k\pi}{5}$ read off Vieta). The identity is the bridge: **trigonometry supplies the roots that algebra names.**

## Jig 2 — powers flattened into multiple angles

The reverse direction has its own bundling, and it is the one integration cares about. Start by asking what $\frac{1}{z}$ *is* when $z = e^{i\theta}$: by the exponent rule, $\frac{1}{z} = e^{-i\theta} = \cos\theta - i\sin\theta$ — which is the **conjugate** $\bar z$. That is a unit-circle special: in general reciprocal and conjugate are different things ($\frac1z = \frac{\bar z}{\lvert z\rvert^2}$), but $\lvert z \rvert = 1$ makes them coincide — dividing by a pure direction is the same as reversing it. Now add and subtract:

$$z + \frac{1}{z} = (\cos\theta + i\sin\theta) + (\cos\theta - i\sin\theta) = 2\cos\theta \quad\text{(imaginary parts cancel)},$$
$$z - \frac{1}{z} = (\cos\theta + i\sin\theta) - (\cos\theta - i\sin\theta) = 2i\sin\theta \quad\text{(real parts cancel)}.$$

And De Moivre with exponents $\pm r$ says $z^r = \cos r\theta + i\sin r\theta$ and $z^{-r} = \cos r\theta - i\sin r\theta$, so the same two lines run at any multiple:

$$z^r + \frac{1}{z^r} = 2\cos r\theta, \qquad z^r - \frac{1}{z^r} = 2i\sin r\theta.$$

**Worked — the syllabus's own example: express $\sin^6\theta$ in terms of $\cos 2\theta$, $\cos 4\theta$, $\cos 6\theta$.**

*Tool: bundle — $(2i\sin\theta)^6 = \left(z - \frac{1}{z}\right)^6$, expand binomially.*

$$\left(z - \tfrac{1}{z}\right)^6 = z^6 - 6z^4 + 15z^2 - 20 + \frac{15}{z^2} - \frac{6}{z^4} + \frac{1}{z^6}$$

*Tool: pair the terms symmetrically — each $z^r + z^{-r}$ is a $2\cos r\theta$ waiting to be read.*

$$= \left(z^6 + \tfrac{1}{z^6}\right) - 6\left(z^4 + \tfrac{1}{z^4}\right) + 15\left(z^2 + \tfrac{1}{z^2}\right) - 20 = 2\cos 6\theta - 12\cos 4\theta + 30\cos 2\theta - 20.$$

*Tool: unbundle — the left side is $(2i)^6 \sin^6\theta = -64\sin^6\theta$.*

$$\sin^6\theta = \frac{20 - 30\cos 2\theta + 12\cos 4\theta - 2\cos 6\theta}{64} = \boxed{\ \frac{10 - 15\cos 2\theta + 6\cos 4\theta - \cos 6\theta}{32}\ }$$

Why the exam loves it: $\displaystyle\int \sin^6\theta \, d\theta$ is now four one-line integrals instead of a reduction-formula grind — the flattened form is *the* integration-ready form, and questions chain this jig straight into [[Integration]] parts. Sanity checks worth thirty seconds: at $\theta = 0$ both sides give $0$; the constant term $\frac{10}{32} = \frac{5}{16}$ is the average value of $\sin^6$ over a period, which must be positive and less than $\frac12$. ✓ (Sign discipline: $\sin$ uses $z - \frac1z$ and every *odd* power keeps an $i$ — for odd powers of $\sin$ the pairing produces $\sin$ terms, not $\cos$. Losing the $i$'s is the classic slip; the $\theta = 0$ check catches it instantly.)

## Jig 3 — the C+iS method: sums of sines and cosines

The star of the section. Face a sum like $\displaystyle\sum_{r=1}^{n} \cos r\theta$ — no trigonometric identity sums it. The C+iS move: name the target and its sibling,

$$C = \sum \cos r\theta, \qquad S = \sum \sin r\theta, \qquad\text{then}\qquad C + iS = \sum \left(\cos r\theta + i\sin r\theta\right) = \sum z^r,$$

and the right-hand side is a **power series in $z$** — summable by geometric or binomial machinery that plain cosines never had. Sum it as complex algebra, then read $C$ from the real part and $S$ from the imaginary part *at the very end*.

Two pieces of standing equipment before the engines:

> [!tip] Pull out the half — the factorisation that makes every answer tidy
> Factor $e^{i\theta/2}$ — **half the exponent** — out of both terms, and watch what each becomes:
> $$1 + e^{i\theta} = e^{i\theta/2}\left(e^{-i\theta/2} + e^{i\theta/2}\right) = e^{i\theta/2}\cdot 2\cos\tfrac{\theta}{2},$$
> because the bracket is exactly Jig 2's bundling read at the half-angle: $e^{i\theta/2} + e^{-i\theta/2} = 2\cos\frac{\theta}{2}$. The minus version runs the same way through the *other* bundling:
> $$1 - e^{i\theta} = e^{i\theta/2}\left(e^{-i\theta/2} - e^{i\theta/2}\right) = e^{i\theta/2}\cdot\left(-2i\sin\tfrac{\theta}{2}\right),$$
> since $e^{-i\theta/2} - e^{i\theta/2}$ is the negative of $z - \frac1z$ at the half-angle. In both cases the result is a **real magnitude times a clean direction** — the form from which taking $\operatorname{Re}$ or $\operatorname{Im}$ is one line. This single factorisation is the difference between a page of algebra and four lines; re-derive it, don't memorise it.

### Engine A — finite geometric

*A real Paper 2 opener, verbatim: "State the sum of the series $z + z^2 + z^3 + \cdots + z^n$, for $z \neq 1$."* One mark — it is $\dfrac{z(1 - z^n)}{1 - z}$, straight from [[Arithmetic and Geometric Progressions]]. Then set $z = e^{i\theta}$:

$$\sum_{r=1}^{n} e^{ir\theta} = e^{i\theta}\,\frac{1 - e^{in\theta}}{1 - e^{i\theta}}.$$

*Tool: pull out the half — on the top with $\theta$ replaced by $n\theta$, on the bottom as stated:*

$$1 - e^{in\theta} = -2i\sin\tfrac{n\theta}{2}\; e^{in\theta/2}, \qquad 1 - e^{i\theta} = -2i\sin\tfrac{\theta}{2}\; e^{i\theta/2}.$$

Divide: the two $-2i$'s cancel, and the exponentials divide by subtracting exponents, $e^{in\theta/2}/e^{i\theta/2} = e^{i(n-1)\theta/2}$:

$$\sum_{r=1}^{n} e^{ir\theta} = e^{i\theta}\cdot\frac{\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}\, e^{i(n-1)\theta/2} = \frac{\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}\; e^{i(n+1)\theta/2} \qquad \left(e^{i\theta} \cdot e^{i(n-1)\theta/2} = e^{i(n+1)\theta/2}\right).$$

Magnitude times direction — so both sums arrive at once:

$$C = \frac{\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}\cos\frac{(n+1)\theta}{2}, \qquad S = \frac{\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}\sin\frac{(n+1)\theta}{2}.$$

![[cis-phasor-chain.svg|760]]

### Engine B — binomial

The syllabus's own target: $\displaystyle\sum_{r=0}^{n} \binom{n}{r} \sin r\theta$. Bundle:

$$C + iS = \sum_{r=0}^{n} \binom{n}{r} \left(e^{i\theta}\right)^r = \left(1 + e^{i\theta}\right)^n \qquad\text{(the binomial theorem, read backwards)}$$

*Tool: pull out the half inside the bracket first, then raise the product to the $n$.*

$$\left(1 + e^{i\theta}\right)^n = \left(2\cos\tfrac{\theta}{2}\; e^{i\theta/2}\right)^n = 2^n \cos^n\tfrac{\theta}{2}\;\; e^{in\theta/2}$$

— a product to the $n$-th power is each factor to the $n$-th: the real factor $2\cos\frac{\theta}{2}$ becomes the magnitude $2^n\cos^n\frac{\theta}{2}$, and the direction $e^{i\theta/2}$ compounds to $e^{in\theta/2}$ (De Moivre again — half-angle in, $n$ half-angles out). Magnitude times direction once more, so unbundle by reading off:

$$S = \operatorname{Im}\left(C + iS\right) = 2^n \cos^n\tfrac{\theta}{2}\,\sin\tfrac{n\theta}{2}, \qquad C = 2^n\cos^n\tfrac{\theta}{2}\,\cos\tfrac{n\theta}{2}.$$

Fifty binomial-weighted sines, priced in three lines. The recognition skill: **a $\binom{n}{r}$ in the summand means the sum *is* a binomial expansion in disguise** — exactly as a plain $r$-th power means geometric.

### Engine C — infinite geometric, and the conjugate finish

*A real Paper 2 question, complete: given $z = \frac{1}{3}(\cos\theta + i\sin\theta)$, show that $\ \displaystyle\operatorname{Re}\sum_{m=1}^{\infty} z^m = \frac{3\cos\theta - 1}{10 - 6\cos\theta}$.*

*Tool: sum to infinity — legal because $\lvert z \rvert = \frac13 < 1$, and saying so is part of the answer.*

$$\sum_{m=1}^{\infty} z^m = \frac{z}{1 - z} = \frac{\cos\theta + i\sin\theta}{3 - \cos\theta - i\sin\theta}.$$

*Tool: the conjugate finish — a complex denominator becomes real by multiplying through by its conjugate ([[Complex Numbers]]).*

$$= \frac{(\cos\theta + i\sin\theta)(3 - \cos\theta + i\sin\theta)}{(3 - \cos\theta)^2 + \sin^2\theta}.$$

Multiply the numerator out term by term and watch the cross-terms kill each other:

$$(\cos\theta + i\sin\theta)(3 - \cos\theta + i\sin\theta) = 3\cos\theta - \cos^2\theta + \underline{i\cos\theta\sin\theta} + 3i\sin\theta - \underline{i\sin\theta\cos\theta} + i^2\sin^2\theta = (3\cos\theta - 1) + 3i\sin\theta$$

(the underlined pair cancels, and $i^2\sin^2\theta = -\sin^2\theta$ joins $-\cos^2\theta$ to make $-1$). The denominator expands to $9 - 6\cos\theta + \cos^2\theta + \sin^2\theta = 10 - 6\cos\theta$ — real, as the conjugate finish guarantees. So the real part reads straight off the numerator:

$$\operatorname{Re}\sum_{m=1}^{\infty} z^m = \boxed{\ \frac{3\cos\theta - 1}{10 - 6\cos\theta}\ } \qquad\blacksquare$$

— and the imaginary part hands over a second theorem free of charge: $\displaystyle\sum_{m=1}^{\infty} \frac{\sin m\theta}{3^m} = \frac{3\sin\theta}{10 - 6\cos\theta}$.

A second real case runs the same engine on a *damped* wave, $z = e^{-1 + i\theta}$ — it is part (c) of the full worked example below. Note what changes between the engines and what never does: the summing machinery rotates (finite geometric, binomial, infinite geometric — imported wholesale from [[Arithmetic and Geometric Progressions]] and the [[Binomial Theorem]]), while bundle-then-unbundle stays fixed.

### The roots-of-unity coda

Point the geometric lens at the roots of unity themselves and a standing identity falls out: for any $n$-th root of unity $\omega \neq 1$, the sum $1 + \omega + \cdots + \omega^{n-1} = \frac{1 - \omega^n}{1 - \omega} = 0$ since $\omega^n = 1$. **The roots of unity sum to zero because they are a geometric series that closes its own loop** — geometrically, the phasor chain of the figure above with the step angle set to exactly $\frac{2\pi}{n}$, walking a full regular polygon back to its starting point. Exams ask this lens in reverse ("find all roots of $1 + z + \cdots + z^6 = 0$") — worked as part (b) below.

## Worked example — one full exam question, every tool named

*A real Paper 2 question, all three parts, worked as an exam script.*

**(a) State the sum of the series $z + z^2 + z^3 + \cdots + z^n$, for $z \neq 1$.** [1]

*Tool: the geometric sum ([[Arithmetic and Geometric Progressions]]) — first term $z$, ratio $z$, $n$ terms.*

$$z + z^2 + \cdots + z^n = \frac{z(1 - z^n)}{1 - z}.$$

("State" means write it down — the mark is for knowing which formula, not for deriving it.)

**(b) Find all roots of the equation $1 + z + z^2 + \cdots + z^6 = 0$ in the form $e^{iq\pi}$, where $q$ is rational.** [2]

*Tool: recognise part (a)'s sum wearing a hat.* Multiply both sides by $(1 - z)$ — legal, because $z = 1$ is visibly not a root (it would make the left side $7$). The left side telescopes to $1 - z^7$, so the equation says

$$z^7 = 1, \quad z \neq 1 \quad\Longrightarrow\quad z = e^{2k\pi i / 7} = e^{iq\pi}, \qquad q = \tfrac{2k}{7}, \quad k = 1, 2, \ldots, 6$$

— the seventh roots of unity minus the trivial one ([[Euler's Formula and De Moivre's Theorem]] §6), six points of a regular heptagon.

**(c) Given instead that $z = e^{-1 + i\theta}$, use de Moivre's theorem to show that $\displaystyle\sum_{m=1}^{\infty} e^{-m} \cos m\theta = \frac{e\cos\theta - 1}{e^2 - 2e\cos\theta + 1}$.** [7]

*Tool: recognise the C+iS bundle.* $z^m = e^{-m}e^{im\theta} = e^{-m}(\cos m\theta + i\sin m\theta)$, so the target sum is exactly $\operatorname{Re}\sum z^m$.

*Tool: sum to infinity, with the convergence sentence.* $\lvert z \rvert = e^{-1} < 1$, so the infinite geometric series converges and

$$\sum_{m=1}^{\infty} z^m = \frac{z}{1 - z} = \frac{e^{-1}e^{i\theta}}{1 - e^{-1}e^{i\theta}} = \frac{e^{i\theta}}{e - e^{i\theta}} \qquad\text{(top and bottom multiplied by } e\text{ to clear the } e^{-1}\text{)}.$$

*Tool: the conjugate finish — the denominator's conjugate is $e - e^{-i\theta}$.*

$$\frac{e^{i\theta}\left(e - e^{-i\theta}\right)}{\left(e - e^{i\theta}\right)\left(e - e^{-i\theta}\right)} = \frac{e\,e^{i\theta} - 1}{e^2 - e\left(e^{i\theta} + e^{-i\theta}\right) + 1} = \frac{(e\cos\theta - 1) + i\,e\sin\theta}{e^2 - 2e\cos\theta + 1},$$

where the numerator used $e^{i\theta}e^{-i\theta} = 1$ and then unbundled $e\,e^{i\theta} = e\cos\theta + i\,e\sin\theta$, and the denominator used Jig 2's bundling $e^{i\theta} + e^{-i\theta} = 2\cos\theta$. The denominator is real — so take the real part and finish:

$$\sum_{m=1}^{\infty} e^{-m}\cos m\theta = \boxed{\ \frac{e\cos\theta - 1}{e^2 - 2e\cos\theta + 1}\ } \qquad\blacksquare$$

(The imaginary part is a free second result, $\sum e^{-m}\sin m\theta = \frac{e\sin\theta}{e^2 - 2e\cos\theta + 1}$ — a damped sine wave summed exactly, no further work. Seven marks: the bundle recognition, the convergence sentence, the geometric sum, clearing $e^{-1}$, the conjugate multiplication, the bundled denominator, the read-off.)

## Where this is the working tool

- **Every diffraction grating is Engine A running on light.** $N$ slits each contribute a wavelet one fixed phase $\phi$ behind the last; the total amplitude is $\sum e^{ir\phi}$ — literally the finite geometric C+iS sum — and its magnitude $\frac{\sin(N\phi/2)}{\sin(\phi/2)}$ is the interference pattern every optics textbook plots: tall principal maxima where the phasor chain straightens ($\phi = 2\pi k$), near-cancellation between, sharper peaks as $N$ grows. The physics of spectrometers is this jig's half-angle formula wearing a lab coat.
- **Digital signal processing sums these series all day.** The same $\sum e^{ir\theta}$ is the **Dirichlet kernel**, the object at the centre of Fourier analysis: it is what a finite chunk of a Fourier series actually adds up to, and its ringing sidelobes (the Gibbs phenomenon at the edges of a square wave) are the $\frac{\sin(n\theta/2)}{\sin(\theta/2)}$ shape misbehaving exactly as the formula predicts. Audio filters and image compressors are engineered around sums this card computes by hand.
- **AC circuit analysis is the bundle step made permanent.** Electrical engineers write every voltage as $\operatorname{Re}\left(V e^{i\omega t}\right)$ and simply *never unbundle until the end* — adding out-of-phase voltages becomes adding complex numbers. The C+iS discipline (work complex, take the real part last) is their standard operating procedure with its own name: phasor analysis.

## Common Misconceptions (Teaching Notes)

### 1. Unbundling too early

Taking $\operatorname{Re}$ halfway through — e.g. writing $\operatorname{Re}\frac{z}{1-z} = \frac{\operatorname{Re} z}{\operatorname{Re}(1-z)}$. Real parts do not pass through division (or multiplication).

**Fix:** the mantra *complex until the last line*. All algebra happens in $\mathbb{C}$; $\operatorname{Re}$ / $\operatorname{Im}$ is the final act, after the conjugate finish has made the denominator real.

### 2. The unstated $\lvert z \rvert < 1$

Summing $\frac{z}{1-z}$ to infinity without saying why it converges. With $z = \frac13 e^{i\theta}$ the reason is $\lvert z \rvert = \frac13 < 1$ — one sentence, and mark schemes look for it.

**Fix:** the convergence sentence is part of the sum-to-infinity tool, not an optional garnish — write it the moment $\infty$ appears on the $\Sigma$.

### 3. Half-angle sign slips

$1 - e^{i\theta} = -2i\sin\frac{\theta}{2}e^{i\theta/2}$: students drop the minus or the $i$, and the final $C$ and $S$ swap or change sign.

**Fix:** don't memorise the two factorisations separately — *re-derive in one line* by pulling out $e^{i\theta/2}$ and reading what remains as $2\cos\frac\theta2$ or $2i\sin\frac\theta2$. Then check the answer at a friendly angle: a thirty-second $\theta = \frac{\pi}{2}$, $n = 2$ numerical check has caught more sign errors than any amount of staring.

### 4. Losing the $i$'s in Jig 2

$(2i\sin\theta)^6 = -64\sin^6\theta$, not $64\sin^6\theta$ — the $i^6 = -1$ is load-bearing, and for *odd* powers the surviving $i$ means the answer pairs into **sines**, not cosines.

**Fix:** evaluate both sides at $\theta = 0$ (even powers) or $\theta = \frac{\pi}{2}$ (odd powers) before moving on. Wrong sign fails instantly.

## Exam Notes

### Cambridge 9231 (Further Pure 2, Paper 2 — §2.5)

- The recurring shapes, all from real papers: **multiple angles + a division twist** ($\cos 5\theta \to \sec 5\theta$, $\sin 5\theta \to \operatorname{cosec} 5\theta$, usually AG) with a polynomial-roots follow-up priced by the identity; **C+iS built in parts** — "state the geometric sum" [1] → roots of $1 + z + \cdots + z^n = 0$ → an infinite sum with $\operatorname{Re}$ or $\operatorname{Im}$ of an AG target; **root extraction** with rational exponents (generalise the argument, *then* divide — the M1 is for dividing the generalised argument).
- AG discipline as everywhere on this paper: the printed answer is the destination, so the marks are in the visible route — the binomial expansion written out, the conjugate multiplication shown, the convergence sentence stated.
- **MF19 gives nothing for this topic** — no De Moivre, no roots of unity, no $e^{i\theta}$ identities ([[MF19 Reference (9231)]]). The half-angle factorisations and the $z \pm \frac1z$ bundlings live in your head; they are four short lines in total.

### Edexcel IAL (Further Pure 2 — WFM02, §3.1–3.2)

Euler's relation with $\cos\theta = \frac12(e^{i\theta} + e^{-i\theta})$ and $\sin\theta = \frac{1}{2i}(e^{i\theta} - e^{-i\theta})$ stated in the spec; De Moivre proved for any integer $n$; multiple angles in **both** directions (powers → multiple angles is named explicitly, so Jig 2 is core there too); roots of complex numbers. **The C+iS series summation does not appear in the IAL spec** — checked — so Jig 3 is Cambridge-specific among these boards.

### IB AA HL

De Moivre with integer powers, proof by induction, and roots of complex numbers sit in AA HL's complex-numbers topic; powers of trig functions via $e^{i\theta}$ appear as the power-reduction trick ([[Euler's Formula and De Moivre's Theorem]] carries the IB-facing treatment). No C+iS.

### Where it is *not* examined

Not on Cambridge 9709 (P3 reaches complex numbers — arithmetic, Argand diagrams, polar form, square roots — but stops before De Moivre), not on OxAQA 9660 (no De Moivre content), not on AP Calculus, not in IB AI. The C+iS method specifically is examined **only** on 9231 among the vault's boards.

## Connections

- **Parent:** [[Euler's Formula and De Moivre's Theorem]] — the blade this mill is built around: the theorem, its proofs, roots of unity, and the forward multiple-angle derivation live there; every jig here starts from its $z = e^{i\theta}$.
- **Machinery:** [[Binomial Theorem]] and [[Arithmetic and Geometric Progressions]] — the two summing engines; [[Summation of Series]] — the wider toolkit this card's sums belong to, and the FP1 partner the exam assumes.
- **Tool:** [[Complex Numbers]] — the conjugate finish that makes denominators real; [[Trigonometric Identities]] — the $c^2 = 1 - s^2$ swaps inside Jig 1.
- **Application:** [[Symmetric Functions of Roots]] — Twist B hands a polynomial its roots as sines and cosines; Vieta then prices their sums and products.
- **Application:** [[Integration]] — Jig 2's flattened powers are the integration-ready form of $\sin^n\theta$, $\cos^n\theta$.
- **For 9231 students:** [[MF19 Reference (9231)]] — nothing from this topic is on the formula sheet.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $e^{i\theta}$ | `e^{i\theta}` | the bundled angle |
| $\operatorname{Re} z$, $\operatorname{Im} z$ | `\operatorname{Re} z` | unbundling, last line only |
| $z + \dfrac{1}{z} = 2\cos\theta$ | `z + \dfrac{1}{z} = 2\cos\theta` | Jig 2's bundling |
| $2\cos\tfrac{\theta}{2}\,e^{i\theta/2}$ | `2\cos\tfrac{\theta}{2}\,e^{i\theta/2}` | pull out the half |
| $\displaystyle\sum_{r=1}^{n} z^r$ | `\sum_{r=1}^{n} z^r` | the C+iS bundle |
| $\binom{n}{r}$ | `\binom{n}{r}` | binomial engine's tell |
| $\operatorname{cosec}\theta$ | `\operatorname{cosec}\theta` | Cambridge's spelling of csc |

---
chinese: 欧拉公式与棣莫弗定理 (ōulā gōngshì yǔ dìmòfú dìnglǐ)
prerequisites:
  - "[[Complex Numbers]]"
  - "[[Trigonometric Identities]]"
  - "[[Euler's Number]]"
  - "[[Radians]]"
  - "[[Binomial Theorem]]"
  - "[[Maclaurin Series]]"
leads_to:
  - "[[Heptadecagon]]"
  - "[[Differential Equations]]"
  - "[[Second-Order Differential Equations]]"
  - "[[De Moivre at Work]]"
tags:
  - subject/mathematics
  - domain/algebra
  - domain/complex-analysis
  - level/A-Level
  - level/IB-AA-HL
  - level/pre-IB
  - curriculum/IB-AA
  - curriculum/A-Level
  - syllabus/9231-2-5
  - type/theorem
  - type/technique
  - notation/euler-form
  - notation/argument
  - misconception/euler-mysticism
  - misconception/de-moivre-fractional-power
  - misconception/missing-roots-of-unity
  - misconception/cis-vs-exp-confusion
---

# Euler's Formula and De Moivre's Theorem 欧拉公式与棣莫弗定理

## Definition

### Formal

**Euler's formula** (Leonhard Euler, 1748):

$$\boxed{\;e^{i\theta} = \cos\theta + i\sin\theta\;}$$

**De Moivre's theorem** (Abraham de Moivre, 1707; named by Euler):

$$\boxed{\;[\cos\theta + i\sin\theta]^n = \cos(n\theta) + i\sin(n\theta)\;}$$

The two are *the same fact* in different notation: Euler's form turns De Moivre into the exponent rule $(e^{i\theta})^n = e^{in\theta}$. Together they are the central machinery of complex-number computation — the toolkit that makes multiplication, powers, roots, and trigonometric identities trivial.

### Intuitive

Recall that every non-zero complex number can be written in [[Complex Numbers|polar form]] $z = r(\cos\theta + i\sin\theta)$. The trigonometric building block $\cos\theta + i\sin\theta$ — which sits inside *every* polar-form complex number — turns out to have a shockingly compact closed form: it equals $e^{i\theta}$.

That single identity does three things:

1. **Compresses notation.** $r(\cos\theta + i\sin\theta)$ becomes $re^{i\theta}$. Same number, half the symbols.
2. **Makes polar arithmetic trivial.** Multiplication is $r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2 e^{i(\theta_1 + \theta_2)}$ — the IGCSE exponent rule, applied. De Moivre's theorem is just $(e^{i\theta})^n = e^{in\theta}$.
3. **Reveals the deep unity.** The same exponent-rule arithmetic that governs $e^x$ for real $x$ governs *rotations of the plane* via $e^{i\theta}$. Exponents and rotations are the same operation in a richer setting.

This is the moment in a student's life when complex numbers stop feeling like a separate weird subject and start feeling like the natural language of every wave, oscillation, and rotation in physics. Once you have $e^{i\theta}$, you have the alphabet of AC circuits, signal processing, quantum mechanics, and Fourier analysis. *That's why this card matters more than its 9709 P3 syllabus footprint suggests.*

### 中文锚点

**欧拉公式**（ōulā gōngshì）—— Leonhard Euler 1748 年：

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

**棣莫弗定理**（dìmòfú dìnglǐ）—— Abraham de Moivre 1707 年：

$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta).$$

两个其实是**同一个事实**的两种写法。用欧拉公式重写棣莫弗定理：$(e^{i\theta})^n = e^{in\theta}$ —— 这就是 IGCSE 学过的指数法则。**复数的乘法、幂、开根号，都被压缩成指数规则。**

中文教材把 $\cos\theta + i\sin\theta$ 简写作 $\mathrm{cis}\,\theta$（"cosine plus i sine"），但欧拉形式 $e^{i\theta}$ 更紧凑、更通用，是国际高校的统一语言。**学好欧拉形式，复数计算速度翻倍，且和大学物理 / 工程 / 信号处理直接对接。**

为什么这张卡值得单独写：复数本身（[[Complex Numbers]]）讲的是定义、Argand 图、极坐标、共轭、轨迹这些"什么是复数"的内容。这张卡讲的是"怎样高效用复数计算"的工具集。两张卡分工：基础卡是入门，工具卡是飞跃。

---

## §1 Why Polar Form Has a Closed Form

Recall from [[Complex Numbers]] §5 that every non-zero $z \in \mathbb{C}$ can be written as

$$z = r(\cos\theta + i\sin\theta), \qquad r = \lvert z \rvert,\; \theta = \arg(z).$$

Recall also (§5 of that card) the polar multiplication rule: when you multiply two polar-form numbers, **the moduli multiply and the arguments add**:

$$r_1(\cos\theta_1 + i\sin\theta_1) \cdot r_2(\cos\theta_2 + i\sin\theta_2) = r_1 r_2 [\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)].$$

The arithmetic operation that *adds* angles when applied is exactly the operation that *exponentials* perform on their exponents: $e^{a} \cdot e^{b} = e^{a+b}$. So the function $\theta \mapsto \cos\theta + i\sin\theta$ should *be* an exponential — it converts addition (of inputs) into multiplication (of outputs), with the multiplicative identity at $\theta = 0$ ($\cos 0 + i\sin 0 = 1$).

That argument suggests $\cos\theta + i\sin\theta = e^{c\theta}$ for some constant $c$. The next section pins down $c = i$ via three independent proofs.

---

## §2 Euler's Formula — Three Proofs

The three proofs come from completely different parts of mathematics — power series, differential equations, and functional equations — and they all converge on the same answer. *That's how you know the identity is real.*

### Proof 1 — Power-series matching

Recall the [[Maclaurin Series|Maclaurin series]] for $e^x$, $\cos x$, $\sin x$:

$$e^x = \sum_{n=0}^\infty \dfrac{x^n}{n!} = 1 + x + \tfrac{x^2}{2!} + \tfrac{x^3}{3!} + \tfrac{x^4}{4!} + \ldots$$

$$\cos x = \sum_{n=0}^\infty \dfrac{(-1)^n x^{2n}}{(2n)!} = 1 - \tfrac{x^2}{2!} + \tfrac{x^4}{4!} - \tfrac{x^6}{6!} + \ldots$$

$$\sin x = \sum_{n=0}^\infty \dfrac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \tfrac{x^3}{3!} + \tfrac{x^5}{5!} - \tfrac{x^7}{7!} + \ldots$$

Substitute $x = i\theta$ into the exponential series. Use $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, $i^5 = i$, etc. — the **powers of $i$ cycle every four steps**:

$$e^{i\theta} = 1 + i\theta + \tfrac{(i\theta)^2}{2!} + \tfrac{(i\theta)^3}{3!} + \tfrac{(i\theta)^4}{4!} + \ldots = 1 + i\theta - \tfrac{\theta^2}{2!} - \tfrac{i\theta^3}{3!} + \tfrac{\theta^4}{4!} + \tfrac{i\theta^5}{5!} - \ldots$$

Group the real and imaginary terms:

$$e^{i\theta} = \underbrace{\left(1 - \tfrac{\theta^2}{2!} + \tfrac{\theta^4}{4!} - \tfrac{\theta^6}{6!} + \ldots\right)}_{=\;\cos\theta} + i\underbrace{\left(\theta - \tfrac{\theta^3}{3!} + \tfrac{\theta^5}{5!} - \tfrac{\theta^7}{7!} + \ldots\right)}_{=\;\sin\theta} = \cos\theta + i\sin\theta. \;\;\square$$

The cycling of $i^n$ — the same property that drives the geometric "multiplication by $i$ rotates by 90°" picture — is what causes the four-term Maclaurin expansion to split into the cosine series (even powers, alternating signs) and the sine series (odd powers, alternating signs). *That's the proof.*

### Proof 2 — The differential-equation proof

Define $f(\theta) = \cos\theta + i\sin\theta$ and treat $f : \mathbb{R} \to \mathbb{C}$ as a function of a real variable.

Differentiate (treating $i$ as a constant):

$$f'(\theta) = -\sin\theta + i\cos\theta = i(\cos\theta + i\sin\theta) = i f(\theta).$$

So $f$ satisfies the differential equation $f'(\theta) = i f(\theta)$ with the initial condition $f(0) = \cos 0 + i\sin 0 = 1$.

The **unique solution** to the ODE $g'(\theta) = c\, g(\theta)$ with $g(0) = 1$ is the exponential $g(\theta) = e^{c\theta}$ — this is the basic theorem of separable first-order linear ODEs (see [[Differential Equations]]). Apply with $c = i$: the unique solution is $g(\theta) = e^{i\theta}$.

Two functions, $f(\theta) = \cos\theta + i\sin\theta$ and $g(\theta) = e^{i\theta}$, satisfy the same ODE with the same initial condition. By uniqueness, $f = g$. ✓

### Proof 3 — The functional-equation proof

A function $\phi : \mathbb{R} \to \mathbb{C}$ is called **multiplicative-additive** if $\phi(\theta_1 + \theta_2) = \phi(\theta_1) \cdot \phi(\theta_2)$. The polar-multiplication identity says that

$$\phi(\theta) = \cos\theta + i\sin\theta$$

is multiplicative-additive: $(\cos\theta_1 + i\sin\theta_1)(\cos\theta_2 + i\sin\theta_2) = \cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)$.

A classical theorem says: every continuous multiplicative-additive function $\phi : \mathbb{R} \to \mathbb{C}$ with $\phi(0) = 1$ has the form $\phi(\theta) = e^{c\theta}$ for some constant $c$. (Take logs of both sides of the functional equation; you get an additive function, which by continuity must be linear.) So $\cos\theta + i\sin\theta = e^{c\theta}$ for some $c \in \mathbb{C}$.

To pin down $c$: differentiate at $\theta = 0$. The left side gives $-\sin 0 + i\cos 0 = i$; the right side gives $c$. So $c = i$. ✓

This proof is the most abstract, but it's also the most general — the same argument works in every Lie group, generalising Euler's formula to a much broader setting.

---

## §3 Euler's Identity — The Five Constants

Substitute $\theta = \pi$ into Euler's formula:

$$e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0i = -1.$$

Rearranged:

$$\boxed{\;e^{i\pi} + 1 = 0\;}$$

This is **Euler's identity**. In a single short equation:

- $e$ — the base of the natural logarithm, born from continuous compounding (see [[Stories/The Hidden Number]] for the 250-year discovery story).
- $i$ — the imaginary unit, defined by $i^2 = -1$ (see [[Stories/The Argument for i]] for the 400-year drama).
- $\pi$ — the ratio of circumference to diameter, the quintessential geometric constant.
- $1$ — the multiplicative identity.
- $0$ — the additive identity.

The five most fundamental constants in mathematics, related by the three most fundamental operations (exponentiation, addition, equality). Richard Feynman called it "the most remarkable formula in mathematics."

> [!tip] The identity is a *consequence*, not a miracle
> The "miracle" is upstream: Euler's formula itself, $e^{i\theta} = \cos\theta + i\sin\theta$. Once you have that, evaluating at $\theta = \pi$ is one line of arithmetic. The deep fact is the unification of exponents and rotations — *that's* the structural beauty. Don't let the five-constants framing turn into mysticism. (See misconception 1.)

---

## §4 De Moivre's Theorem

For any integer $n$ and any real $\theta$:

$$[\cos\theta + i\sin\theta]^n = \cos(n\theta) + i\sin(n\theta).$$

In Euler form: $(e^{i\theta})^n = e^{in\theta}$. *Which is just the exponent rule.* De Moivre's theorem is exponent rules in disguise — historically discovered in 1707, but conceptually a consequence of Euler's 1748 unification.

### Proof by induction on $n \geq 0$

**Base case** ($n = 0$): $[\cos\theta + i\sin\theta]^0 = 1 = \cos 0 + i\sin 0$. ✓

**Inductive step.** Assume $[\cos\theta + i\sin\theta]^k = \cos(k\theta) + i\sin(k\theta)$. Then
$$[\cos\theta + i\sin\theta]^{k+1} = [\cos\theta + i\sin\theta]^k \cdot [\cos\theta + i\sin\theta] = [\cos(k\theta) + i\sin(k\theta)][\cos\theta + i\sin\theta]$$
which by the polar-multiplication rule (see [[Complex Numbers]] §5, or expand using compound-angle [[Trigonometric Identities|identities]]) equals $\cos((k+1)\theta) + i\sin((k+1)\theta)$. ✓ $\square$

**Negative integer case.** $z^{-1} = \bar{z} / \lvert z \rvert^2$; for $\lvert z \rvert = 1$ (which is the case here), $z^{-1} = \bar{z}$, so $[\cos\theta + i\sin\theta]^{-1} = \cos\theta - i\sin\theta = \cos(-\theta) + i\sin(-\theta)$ ✓. Induction extends from there. (Why the two-pillar argument itself is valid — and its four-movement grammar — is [[Proof by Induction]].)

> [!warning] De Moivre with non-integer $n$ — careful
> For non-integer $n$ (e.g. $n = 1/3$), the equation $[\cos\theta + i\sin\theta]^n = \cos(n\theta) + i\sin(n\theta)$ gives **only one of several values**. A cube root of $\cos\theta + i\sin\theta$ has *three* values; the formula returns the *principal* one. The other two are obtained by replacing $\theta$ with $\theta + 2\pi$ and $\theta + 4\pi$ before dividing by 3. (See §6 for the full $n$-th-roots-of-unity treatment.)

### Rational exponents — all the values, on purpose

The warning becomes a technique the moment you *want* every value. For $z^{p/q}$ (fraction in lowest terms), write $z$ with its **general argument first**, then exponentiate:

$$z = r\,e^{i(\theta + 2\pi k)} \quad\Longrightarrow\quad z^{p/q} = r^{p/q}\, e^{i\,p(\theta + 2\pi k)/q}, \qquad k = 0, 1, \ldots, q - 1$$

— exactly $q$ distinct values (because $\gcd(p, q) = 1$), equally spaced around a circle. A real Further exam case: *solve $z^3 = -108\sqrt{3} + 108i$.* Modulus: $\sqrt{108^2 \cdot 3 + 108^2} = 216 = 6^3$. Argument: $\pi - \frac{\pi}{6} = \frac{5\pi}{6}$. Generalise, then take the cube root:

$$z = 216^{1/3} e^{i\left(\frac{5\pi}{6} + 2\pi k\right)/3} = 6e^{5i\pi/18},\quad 6e^{17i\pi/18},\quad 6e^{29i\pi/18}.$$

The mark scheme's own M1 is for *dividing the generalised argument by* $3$ — the habit that earns it: **generalise the argument first, exponentiate second.** Exponentiating first throws away every value but one.

---

## §5 Application — Multiple-Angle Identities

De Moivre's theorem produces every $\cos(n\theta)$ and $\sin(n\theta)$ identity *on demand*. Take $n = 3$:

$$\cos(3\theta) + i\sin(3\theta) = (\cos\theta + i\sin\theta)^3.$$

Expand the right side using the [[Binomial Theorem|binomial theorem]]:

$$(\cos\theta + i\sin\theta)^3 = \cos^3\theta + 3i\cos^2\theta\sin\theta + 3i^2\cos\theta\sin^2\theta + i^3\sin^3\theta.$$

Use $i^2 = -1$, $i^3 = -i$:

$$= (\cos^3\theta - 3\cos\theta\sin^2\theta) + i(3\cos^2\theta\sin\theta - \sin^3\theta).$$

Equate real and imaginary parts:

$$\cos(3\theta) = \cos^3\theta - 3\cos\theta\sin^2\theta = 4\cos^3\theta - 3\cos\theta$$

$$\sin(3\theta) = 3\cos^2\theta\sin\theta - \sin^3\theta = 3\sin\theta - 4\sin^3\theta$$

(The second forms use $\sin^2\theta = 1 - \cos^2\theta$ and $\cos^2\theta = 1 - \sin^2\theta$ respectively.)

Standard triple-angle identities — derived from scratch in twenty seconds. **You don't memorise multiple-angle identities; you re-derive them on demand.** Same recipe for $n = 4, 5, \ldots$. (For $n = 5$: write $(\cos\theta + i\sin\theta)^5$, binomial-expand, sort by parity, equate real and imaginary parts.)

> [!info] Power-reduction identities — the reverse direction
> Going *the other way*, you can use Euler's formula plus its conjugate $e^{-i\theta} = \cos\theta - i\sin\theta$ to derive **power-reduction identities** like $\cos^2\theta = \tfrac{1}{2}(1 + \cos 2\theta)$ and $\sin^3\theta = \tfrac{3\sin\theta - \sin 3\theta}{4}$. The general trick: write $\cos\theta = \tfrac{1}{2}(e^{i\theta} + e^{-i\theta})$ and $\sin\theta = \tfrac{1}{2i}(e^{i\theta} - e^{-i\theta})$, then expand $\cos^n\theta$ or $\sin^n\theta$ binomially and re-collect. Standard at IB AA HL.

---

## §6 Application — $n$-th Roots of Unity

Solve $z^n = 1$ for $z \in \mathbb{C}$. Write $z = re^{i\theta}$; then

$$z^n = r^n e^{in\theta} = 1 = 1 \cdot e^{i \cdot 0}.$$

Equate moduli: $r^n = 1 \Rightarrow r = 1$ (since $r \geq 0$).
Equate arguments **mod $2\pi$**: $n\theta = 2\pi k$ for some integer $k$, so $\theta = \dfrac{2\pi k}{n}$.

The integer $k$ produces *distinct* values of $z$ for $k = 0, 1, 2, \ldots, n-1$; for $k \geq n$, the $\theta$ values just repeat (mod $2\pi$). So:

$$\boxed{\;z_k = e^{2\pi i k/n}, \qquad k = 0, 1, 2, \ldots, n-1\;}$$

These are the **$n$-th roots of unity**. Geometrically, they sit at the vertices of a **regular $n$-gon** inscribed in the unit circle, evenly spaced by angle $\dfrac{2\pi}{n}$. The first one ($k = 0$) is always $z_0 = 1$.

### Worked example — fifth roots of unity

Solve $z^5 = 1$. The five solutions are

$$z_k = e^{2\pi i k/5}, \quad k = 0, 1, 2, 3, 4.$$

That's $z_0 = 1$ and four others at angles $72°, 144°, 216°, 288°$ on the unit circle. They form a regular pentagon. The non-trivial roots are roots of $\dfrac{z^5 - 1}{z - 1} = z^4 + z^3 + z^2 + z + 1 = 0$ — the **5th cyclotomic polynomial**.

### Why this matters — the cyclotomic family

A **primitive $n$-th root of unity** is a root of $z^n = 1$ that *isn't* also a root of $z^k = 1$ for any smaller $k$. So $1$ is a primitive 1st root (it satisfies $z^1 = 1$); $-1$ is a primitive 2nd root (it satisfies $z^2 = 1$ but not $z^1 = 1$); $\pm i$ are primitive 4th roots; the two complex 3rd roots $e^{\pm 2\pi i/3}$ are primitive 3rd roots; and so on. The non-primitive $n$-th roots are *primitive divisors* — for example, among the six 6th roots, two are primitive 6th, but the rest are 1st, 2nd, or 3rd primitives in disguise.

The **$n$-th cyclotomic polynomial** $\Phi_n(x)$ is the *minimal monic polynomial over $\mathbb{Q}$ whose roots are exactly the primitive $n$-th roots of unity*. The first few:

$$\Phi_1(x) = x - 1, \quad \Phi_2(x) = x + 1, \quad \Phi_3(x) = x^2 + x + 1, \quad \Phi_4(x) = x^2 + 1, \quad \Phi_5(x) = x^4 + x^3 + x^2 + x + 1.$$

Because every $n$-th root of unity is *primitive of order $d$* for some divisor $d$ of $n$, the polynomial $x^n - 1$ factors over $\mathbb{Z}[x]$ as a product of one cyclotomic polynomial per divisor:

$$x^n - 1 = \prod_{d \mid n} \Phi_d(x).$$

For example, $x^6 - 1 = \Phi_1(x) \Phi_2(x) \Phi_3(x) \Phi_6(x) = (x-1)(x+1)(x^2 + x + 1)(x^2 - x + 1)$ — one factor per divisor of 6 ($d = 1, 2, 3, 6$). The cyclotomic polynomials are *irreducible over $\mathbb{Q}$* (Gauss, 1801, in his *Disquisitiones Arithmeticae*), and their degrees are $\varphi(n)$, the **Euler totient function** — the number of integers in $\{1, \ldots, n\}$ coprime to $n$.

This is exactly the algebra behind [[Heptadecagon|Gauss's regular 17-gon]] construction (1796): the 17th roots of unity are roots of $\Phi_{17}(x)$, which has degree 16. Gauss showed those roots can be expressed using only square roots — *which is what makes the construction compass-and-straightedge possible*. It's also the algebra behind which regular polygons are constructible (those whose number of sides is a power of 2 times distinct Fermat primes). Roots of unity, hidden inside polygon constructions, hidden inside Gauss's first major result.

---

## §7 Application — Solving $z^n = w$

The roots-of-unity argument generalises to any complex $w$. Solve $z^n = w$ where $w = Re^{i\phi}$ ($R = \lvert w \rvert$, $\phi = \arg w$).

Write $z = re^{i\theta}$. Then $z^n = r^n e^{in\theta} = R e^{i\phi}$. Equate:

- Moduli: $r^n = R \Rightarrow r = R^{1/n}$ (the positive $n$-th root of the real number $R$).
- Arguments mod $2\pi$: $n\theta = \phi + 2\pi k \Rightarrow \theta = \dfrac{\phi + 2\pi k}{n}$ for $k = 0, 1, \ldots, n-1$.

So:

$$\boxed{\;z_k = R^{1/n} \exp\!\left(\dfrac{i(\phi + 2\pi k)}{n}\right), \qquad k = 0, 1, \ldots, n-1\;}$$

The $n$ solutions sit at the vertices of a regular $n$-gon inscribed in the circle of radius $R^{1/n}$, with the first vertex at angle $\phi/n$.

### Worked example

Solve $z^3 = -8$. Write $-8 = 8 e^{i\pi}$ (modulus $8$, argument $\pi$). Then

$$z_k = 8^{1/3} \exp\!\left(\dfrac{i(\pi + 2\pi k)}{3}\right) = 2 e^{i(\pi + 2\pi k)/3}, \quad k = 0, 1, 2.$$

Compute:

- $z_0 = 2 e^{i\pi/3} = 2(\cos 60° + i\sin 60°) = 1 + i\sqrt{3}$.
- $z_1 = 2 e^{i\pi} = -2$.
- $z_2 = 2 e^{i5\pi/3} = 2(\cos 300° + i\sin 300°) = 1 - i\sqrt{3}$.

Check: $(-2)^3 = -8$ ✓; the other two are conjugate pairs (which is expected — coefficients of $z^3 + 8 = 0$ are real, so complex roots come in conjugate pairs by [[Complex Numbers]] §8's conjugate root theorem).

---

## §8 Why STEM Uses Complex Exponentials

Once Euler's form is in your toolkit, an entire family of physical-world phenomena becomes algebraically trivial.

**Oscillation = imaginary exponent.** A purely oscillating signal $\cos(\omega t + \phi)$ is just the real part of $e^{i(\omega t + \phi)}$. Phase shifts are angle additions. Two oscillations at the same frequency add as complex numbers. Phase-locked oscillators are points on a circle.

**Damped oscillation = complex exponent.** $e^{(\sigma + i\omega)t}$ describes an oscillation at frequency $\omega$ that grows ($\sigma > 0$) or decays ($\sigma < 0$) exponentially in amplitude. *One unified expression for what would otherwise be a product of $e^{\sigma t}$ and $\cos(\omega t)$.* Differential-equation solutions in the underdamped case, RLC circuits, mass-spring-damper systems, all collapse into this single form.

**Differentiation becomes multiplication.** $\dfrac{d}{dt} e^{i\omega t} = i\omega \, e^{i\omega t}$. In the frequency domain (Fourier-transformed), differentiation is "multiply by $i\omega$"; integration is "divide by $i\omega$." Differential equations become **algebraic equations** in the frequency domain.

**Fourier transform** decomposes any signal into a sum (or integral) of complex exponentials $e^{i\omega t}$. Every audio file (MP3, AAC), every image (JPEG, PNG), every radio transmission (Wi-Fi, 5G), every MRI scan, every digital filter — all run on Fourier decomposition. The natural building blocks are complex exponentials, not separate sines and cosines.

**AC circuit analysis** treats voltage and current as complex exponentials; resistors, inductors, capacitors become **complex impedances** $R$, $i\omega L$, $\dfrac{1}{i\omega C}$; Kirchhoff's laws become linear algebra over $\mathbb{C}$. The whole subject of *electrical engineering* — until you go to power electronics or RF — is complex-number arithmetic with $\omega t$ as the running argument.

**Quantum mechanics** writes wavefunctions as $\psi(x, t) = e^{i(kx - \omega t)}$. The Schrödinger equation $i\hbar \dfrac{\partial \psi}{\partial t} = \hat{H}\psi$ has $i$ on the left side — *this $i$ is load-bearing, not cosmetic*. Without it, you get the heat equation (real-valued, monotone smoothing). With it, you get wave propagation with **interference** (probabilities can cancel). The 16th-century algebra accident turned out to be the algebraic encoding of wave-particle duality.

That's why Euler's formula gets called "the bridge between mathematics and physics." Algebra demanded $i$ in 1545; geometry rationalised it in 1799; quantum mechanics revealed in 1925 that the universe was using it all along.

---

## Common Misconceptions

### 1. Euler-identity mysticism

Treating $e^{i\pi} + 1 = 0$ as an inexplicable miracle.

**Fix.** It's a *consequence* of Euler's formula evaluated at $\theta = \pi$, plus $\cos\pi = -1$ and $\sin\pi = 0$. Euler's formula itself is the deep fact, and *that* has three independent proofs. The five-constants framing is showmanship; the deep fact is the unification of exponents and rotations.

### 2. De Moivre with fractional $n$ — only one root

Writing $(\cos\theta + i\sin\theta)^{1/3} = \cos(\theta/3) + i\sin(\theta/3)$ and stopping there.

**Fix.** A cube root has *three* values; De Moivre with $n = 1/3$ returns only the principal one. To get all $n$ roots of $z^n = w$, use the §7 formula with $k = 0, 1, \ldots, n-1$. Always check that the number of roots you find equals the degree of the equation.

### 3. Forgetting the $2\pi k$ in roots problems

Solving $z^n = 1$ as just $z = 1^{1/n} = 1$, missing the other $n - 1$ roots.

**Fix.** The argument equation $n\theta = 0 + 2\pi k$ has *infinitely many* solutions $\theta$, but only $n$ distinct ones mod $2\pi$. Always sweep $k = 0, 1, \ldots, n-1$ when solving $z^n = w$.

### 4. CIS notation vs Euler form

Some textbooks (especially Australian/Asian) write $\mathrm{cis}\,\theta$ for $\cos\theta + i\sin\theta$, treating it as a notational shortcut. Students who learn CIS without learning Euler form miss the structural insight.

**Fix.** $\mathrm{cis}\,\theta$ and $e^{i\theta}$ are exactly the same number — but $e^{i\theta}$ is the international standard, makes the multiplication rule obvious (exponents add), and is what every university and engineering text uses. Learn both, but think in $e^{i\theta}$. CIS is training wheels.

### 5. Conflating the principal argument with any argument

Computing $\arg(z)$ via $\arctan$ and getting a value outside $(-\pi, \pi]$, or treating $\theta = 5\pi/3$ and $\theta = -\pi/3$ as different points (they're the same point on the Argand diagram).

**Fix.** Arguments are equivalent mod $2\pi$. The **principal** argument convention pins down a unique representative in $(-\pi, \pi]$ — but for *roots* problems, you sweep over all distinct values mod $2\pi$ (which gives the $n$ separate roots). Don't conflate "uniqueness up to $2\pi$" (the underlying truth) with "principal value" (a convention).

---

## Exam Notes

### Cambridge 9709 (A-Level)

**Euler form is *not* in 9709 P3 §3.9 syllabus.** De Moivre's theorem is *not* explicitly required either. *However*, both are taught universally because:

1. They make polar-form arithmetic vastly faster (which directly helps on §3.9 questions where polar form is required).
2. They make multiple-angle and conjugate-root computations one-liners.
3. They're the natural language of the §3.5 integration toolkit (when an arctan or log emerges from a complex-roots argument, Euler form is the lens).

So an organised P3 student learns Euler form *as enrichment*. Don't rely on it *appearing on the mark scheme* — but use it freely to compute the polar-form answers the mark scheme does want.

### Cambridge 9231 (Further Pure 2, Paper 2 — §2.5)

De Moivre's theorem is examined in full: integer and negative exponents with the geometric meaning, the induction proof (the syllabus's own suggested route — §4 above *is* the exam answer), rational exponents (the subsection above, with the generalise-the-argument-first discipline), and $n$-th roots of unity. The applied machinery — multiple-angle identities both directions, the $C+iS$ series method — is worked exam-shape by exam-shape in [[De Moivre at Work]]. **MF19 gives none of it** ([[MF19 Reference (9231)]]).

### Edexcel IAL (Further Pure 2 — WFM02, §3.1–3.2)

Euler's relation is stated in the spec itself (with $\cos\theta = \frac12(e^{i\theta} + e^{-i\theta})$ and its sine twin), De Moivre must be provable "for any integer $n$", and the applications named are trigonometric identities in both directions and roots of a complex number. In the UK-domestic families the same content sits in the **Further** qualifications (never in single-subject A-Level Pure).

### IB AA HL

**Topic 1 (Number and Algebra) — Subtopic 1.13**: includes Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$, the polar-Cartesian-Euler form trinity, De Moivre's theorem with applications to multiple-angle identities and $n$-th roots of unity. The IB formula booklet *gives* Euler's formula and De Moivre's theorem; you don't need to memorise the statements, but you must apply them fluently.

**Typical question shapes (5–8 marks):**
1. Express $z = (a + bi)$ in Euler form. (2 marks)
2. Use De Moivre to derive $\cos(5\theta)$ in terms of $\cos\theta$. (3–4 marks)
3. Find all $n$-th roots of $w \in \mathbb{C}$, plot on Argand diagram. (4 marks)
4. Express $\cos^4\theta$ in terms of $\cos 2\theta$ and $\cos 4\theta$ via Euler form (power-reduction). (4 marks)

AA SL does not test Euler form or De Moivre.

### AP

Not on AP Calculus AB or BC. AP Pre-calculus introduces Euler form briefly (no formal De Moivre).

### Beyond high school — University

- **Complex analysis** — calculus done with $z = x + iy$. Euler's formula is the foundation; holomorphic functions are precisely those that respect the Cauchy-Riemann equations, which are the local form of "differentiable in the $e^{i\theta}$ sense."
- **Linear algebra** — eigenvalues of real symmetric matrices are real, but eigenvalues of general matrices are complex; complex eigenvalues come in conjugate pairs and correspond to oscillatory modes via $e^{(\sigma + i\omega)t}$.
- **Signal processing & control theory** — every transfer function lives in $\mathbb{C}$; stability is a question about where the poles sit (left vs right half-plane).
- **Quantum mechanics** — $e^{i\theta}$ is a global phase; $e^{i(kx - \omega t)}$ is a momentum eigenstate; Berry phases and gauge transformations are all rotations in $U(1)$.

---

## Connections

- **Direct prerequisite:** [[Complex Numbers]] — the foundation card. Cartesian, Argand, polar form, modulus, argument, conjugate. Read that first; this card is the power-tools layer.
- **Direct prerequisite:** [[Trigonometric Identities]] — compound-angle identities are *equivalent* to polar multiplication. The cross-card unity is itself a teaching point (see §1).
- **Direct prerequisite:** [[Euler's Number]] — $e$ as the natural exponential base. Euler's form extends $e^x$ to imaginary exponents; the construction depends on knowing what $e$ is.
- **Direct prerequisite:** [[Radians]] — angles in Euler's formula are *always* in radians (the Maclaurin series for $\sin$ and $\cos$ require radian-measured input).
- **Direct prerequisite:** [[Binomial Theorem]] — used to expand $(\cos\theta + i\sin\theta)^n$ when extracting multiple-angle identities.
- **Application:** [[Heptadecagon]] — Gauss's 17-gon is the geometric realisation of the 17th roots of unity. The §6 cyclotomic-polynomial framework is the algebra behind which polygons are compass-and-straightedge constructible.
- **Application:** [[Differential Equations]] — second-order linear ODEs in the underdamped case use $e^{(\sigma + i\omega)t}$ solutions. Euler's form is the natural language for oscillations.
- **Application — beyond syllabus:** Fourier series and transform — every signal decomposes into complex exponentials.
- **Application — beyond syllabus:** AC circuit analysis — impedance is complex; Kirchhoff's laws become linear algebra over $\mathbb{C}$.
- **Story counterpart:** [[Stories/The Argument for i]] — the 400-year drama from Cardano's cubic to Schrödinger's wavefunction. Read alongside this card for the historical and physical context.
- **Story counterpart:** [[Stories/The Hidden Number]] — the 250-year discovery of $e$, climaxing in Euler's identity. Pairs naturally with this card.

---

## Beyond Syllabus

### The unity at the heart of the formula

The single most important thing about Euler's formula is what it says about *what an exponential is*. The function $e^x$ for real $x$ is "the function that is its own derivative" — it's defined by the differential property. Euler's formula extends $e$ to imaginary arguments by saying: **the same defining property — being its own derivative, up to a constant — also determines $e^{i\theta}$, and the answer is rotation by $\theta$.**

So the exponential function isn't really about "growth" — that's the special case for real arguments. The general truth is: **the exponential is the function that turns addition into multiplication**, applied in whatever space the input lives in. For real inputs, addition-of-numbers becomes multiplication-of-positive-reals. For imaginary inputs, addition-of-angles becomes multiplication-of-unit-circle-points (which is rotation). For complex inputs, you get both — the real part scales, the imaginary part rotates. Euler's formula is the single identity that unifies all these special cases.

### The matrix view

Multiplication by $z = re^{i\theta}$ acts on the complex plane (≃ $\mathbb{R}^2$) as the linear map represented by

$$M_z = r \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \quad \text{where } z = a + bi.$$

The 2×2 matrices of this *rotation-and-scaling* shape form a subring of $M_2(\mathbb{R})$ isomorphic to $\mathbb{C}$ as a field. So complex numbers literally *are* the rotation-and-scaling matrices of 2D, viewed as numbers. Multiplication of complex numbers is matrix multiplication restricted to this subring; the modulus is the determinant's square root; the argument is the rotation angle.

### Euler's identity in higher Lie groups

Euler's formula generalises. The expression $e^{X}$ for a matrix $X$ is defined by the Maclaurin series, just as for scalars; if $X$ is skew-symmetric (or anti-Hermitian in the complex case), $e^{X}$ is a rotation matrix (or unitary matrix). In Lie-theoretic language: Euler's formula is the special case of the **exponential map** $\exp : \mathfrak{g} \to G$ for the Lie group $G = U(1)$ (or $SO(2)$) and its Lie algebra $\mathfrak{g} = i\mathbb{R}$.

Same machinery, applied in $SO(3)$, gives Rodrigues's rotation formula for 3D. In $SU(2)$, you get the spin-$\tfrac{1}{2}$ rotations of quantum mechanics. In $SU(N)$, you get gauge transformations of the Standard Model. All of physics's continuous symmetries live in this framework, and Euler's formula is the simplest-possible-non-trivial example.

### What the formula implies about $\pi$

Euler's identity $e^{i\pi} = -1$ has a strange corollary: $\pi$ is the unique smallest positive real number $t$ such that $e^{it} = -1$. *That's an alternative definition of $\pi$* — not via "ratio of circumference to diameter," not via a series expansion, but via the imaginary-exponential operation. Some abstract analysis textbooks take this as the *defining* property of $\pi$ and recover the geometric meaning later. It's $\pi$ as a *number*, divorced from any underlying picture of a circle — which is, philosophically, the most natural definition.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $e^{i\theta}$ | `e^{i\theta}` | Euler form |
| $\cos\theta + i\sin\theta$ | `\cos\theta + i\sin\theta` | Polar building block (= $e^{i\theta}$) |
| $\mathrm{cis}\,\theta$ | `\mathrm{cis}\,\theta` | Shorthand for the polar building block; less common at university than $e^{i\theta}$ |
| $e^{i\pi} + 1 = 0$ | `e^{i\pi} + 1 = 0` | Euler's identity |
| $z = re^{i\theta}$ | `z = re^{i\theta}` | Polar form, Euler-style |
| $z^n = r^n e^{in\theta}$ | `z^n = r^n e^{in\theta}` | De Moivre / exponent rule |
| $z_k = R^{1/n} e^{i(\phi + 2\pi k)/n}$ | `z_k = R^{1/n} e^{i(\phi + 2\pi k)/n}` | $n$-th roots of $w = Re^{i\phi}$ |
| $\Phi_n(x)$ | `\Phi_n(x)` | $n$-th cyclotomic polynomial — minimal polynomial of primitive $n$-th roots of unity |
| $\varphi(n)$ | `\varphi(n)` | Euler's totient function — number of primitive $n$-th roots of unity |
| $U(1)$ | `U(1)` | Unit circle as a Lie group; $e^{i\theta}$ parameterises it |
| $\exp$ | `\exp` | Exponential map (text-form, used in Lie-theory contexts) |

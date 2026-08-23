---
chinese: 复数 (fùshù)
prerequisites:
  - "[[Quadratic Equations]]"
  - "[[Discriminant]]"
  - "[[Trigonometric Ratios]]"
  - "[[Radians]]"
  - "[[Number Sets (Vocab)]]"
  - "[[Vectors]]"
  - "[[Cubic Graphs]]"
  - "[[Euler's Number]]"
  - "[[Exponential Function]]"
  - "[[Maclaurin Series]]"
  - "[[Magnitude of a Vector (Vocab)]]"
leads_to:
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[Differential Equations]]"
  - "[[Heptadecagon]]"
  - "[[Second-Order Differential Equations]]"
  - "[[Galois at Twenty]]"
  - "[[The Argument for i]]"
  - "[[Polar Coordinates]]"
  - "[[De Moivre at Work]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/9709-3-9
  - syllabus/9231-2-5
  - type/definition
  - type/theorem
  - notation/imaginary-unit
  - notation/argand-diagram
  - misconception/i-is-not-a-number
  - misconception/sqrt-of-negative-confusion
  - misconception/argument-quadrant-error
  - misconception/missing-conjugate-root
---

# Complex Numbers 复数

## Definition

### Formal

A **complex number** is a number of the form

$$z = a + bi, \qquad a, b \in \mathbb{R}, \qquad i^2 = -1.$$

The real number $a$ is the **real part**, written $\Re(z) = a$. The real number $b$ is the **imaginary part**, written $\Im(z) = b$. The set of all complex numbers is denoted $\mathbb{C}$, and it forms a **field** — closed under addition, subtraction, multiplication, and division (except by $0$), with all the usual rules of arithmetic. Two complex numbers are equal exactly when both their real and imaginary parts agree:

$$a + bi = c + di \;\iff\; a = c \;\text{ and }\; b = d.$$

The chain of number systems extends as $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$. Each step adds the answers to a previously-unsolvable family of equations: $\mathbb{Z}$ gives $x + 5 = 0$ a solution; $\mathbb{Q}$ gives $2x = 1$; $\mathbb{R}$ gives $x^2 = 2$; $\mathbb{C}$ gives $x^2 = -1$.

### Intuitive

Yes, $i = \sqrt{-1}$ is weird. A number whose square is negative? Numbers measure things — lengths, costs, counts — and *no thing has a negative square*. The first reaction "this can't be right" is correct.

Here's the reconciliation, in three parts.

**1. The cubic formula forced the issue.** In 1545, Cardano published a solution to $x^3 + px + q = 0$ that produced *real* answers — but only after the calculation passed through square-roots-of-negatives in its intermediate steps. Bombelli, in the 1560s, wrote out the rules for computing with these "impossible" objects and *the answers came out right every time*. Two centuries before anyone could explain *why*, the algebra demanded that $\sqrt{-1}$ be allowed at the table. (See [[Stories/The Argument for i]] for the full 400-year drama.)

**2. The Argand diagram dissolves the mystery.** In 1799 (Wessel), 1806 (Argand), and 1831 (Gauss) — three independent rediscoveries — mathematicians realised that complex numbers can be drawn as **points in a plane**, with the real axis horizontal and the imaginary axis vertical. The number $a + bi$ is just the point $(a, b)$. Multiplication by $i$ becomes a 90° rotation. The "imaginary" part is just the $y$-coordinate. *None of it is imaginary.* The word is a 16th-century misnomer that stuck.

**3. The STEM field cashed it in.** Once you accept complex numbers, you get for free: alternating-current circuit analysis, the wave-particle behaviour of quantum mechanics, the Fourier transform that runs every digital signal-processing pipeline (your phone, MRI, JPEG, Wi-Fi), and the conformal-map theory behind aerofoil design. Modern STEM doesn't *use* complex numbers — it's *built on* them.

So the card's posture is: **the weirdness is real; the resolution is geometric; the payoff is everything from circuits to quantum.** This card lays the foundation: definitions, geometry, polar form, conjugate root theorem, loci. The companion card [[Euler's Formula and De Moivre's Theorem]] is the power-tools layer — Euler's $e^{i\theta}$, De Moivre, roots of unity, the unification of exponents and rotations. Read this card first.

### 中文锚点

**复数**（fùshù）：形如 $z = a + bi$ 的数，其中 $a, b$ 是实数，$i$ 是**虚数单位**（imaginary unit），定义为 $i^2 = -1$。

**实部** (real part) $\Re(z) = a$；**虚部** (imaginary part) $\Im(z) = b$。复数的集合记作 $\mathbb{C}$，是数系的最大扩展：

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}.$$

**为什么不是"假"的？** "Imaginary"（虚）只是 16 世纪的旧称，说当时数学家认为 $\sqrt{-1}$ 不存在、是想象出来的。真相是：

1. **代数上**：1545 年 Cardano 解三次方程时被迫接受 $\sqrt{-1}$，因为不经过它就算不出实数解。
2. **几何上**：1806 年 Argand 把复数画成平面上的点 $(a, b)$，"虚部"就是 $y$ 坐标，没有什么虚的。乘 $i$ 就是逆时针旋转 90°。
3. **物理上**：交流电、量子力学的波函数、傅里叶变换 —— 现代 STEM 不是"用"复数，而是"建立在"复数之上。

中文教材里有时叫 "复数"，对应英文的 "complex number"；"复" (fù) 意为"有多个部分组成"，准确捕捉了 $a + bi$ 由两个实部分组成的本质。比"imaginary"准确得多。

> [!info] Companion cards
> - **[[Euler's Formula and De Moivre's Theorem]]** — the power-tools sibling card. $e^{i\theta} = \cos\theta + i\sin\theta$ with three proofs, De Moivre's theorem, $n$-th roots of unity, multiple-angle identities. *Read this card first; reach for that one for computational firepower and any IB AA HL preparation.*
> - **[[Stories/The Argument for i]]** — the 400-year human drama from Cardano's cubic to Schrödinger's wavefunction. Read for the historical and physical context.
> - **[[Stories/The Hidden Number]]** — the 250-year discovery of $e$, climaxing in Euler's identity. Pairs naturally.

---

## §1 The Imaginary Unit — Why $i^2 = -1$ Even Makes Sense

### The algebraic motivation

The equation $x^2 + 1 = 0$ has no real solution — for any real $x$, $x^2 \geq 0$, so $x^2 + 1 \geq 1 > 0$. The graph of $y = x^2 + 1$ never touches the $x$-axis. *In $\mathbb{R}$, there is no answer.*

We *define* a new symbol $i$ to be a solution: $i^2 = -1$. The other solution is $-i$, since $(-i)^2 = i^2 = -1$ also.

That's the whole definition. From this single rule, all of complex-number arithmetic follows: any expression involving $i$ collapses by repeated use of $i^2 = -1$. For instance:

$$i^3 = i^2 \cdot i = -i, \qquad i^4 = (i^2)^2 = 1, \qquad i^5 = i^4 \cdot i = i, \qquad \ldots$$

The powers of $i$ cycle every four steps: $1, i, -1, -i, 1, i, -1, -i, \ldots$. *(Geometric reason: each multiplication by $i$ rotates by 90°. Four 90° rotations bring you back to start. We'll see this in §3.)*

### The "imaginary" misnomer

The word *imaginary* was coined by Descartes in 1637, derisively. He thought roots that involved $\sqrt{-1}$ were "imaginary" in the everyday sense: not real, not actually there, products of the imagination. The label stuck. It is *not* an accurate description — complex numbers are no more imaginary than negative numbers are. They have unambiguous arithmetic, unambiguous geometry, and concrete real-world manifestations.

A better modern name would be "rotational numbers" or "two-dimensional numbers" — but four centuries of textbook tradition is a hard thing to move.

### The historical motivation — *the cubic forced it*

It's tempting to think complex numbers were invented to solve $x^2 + 1 = 0$. They weren't. *That equation is happily ignorable* — if your real-life problem produces it, the answer is "no real solution, end of story." The cubic, however, is what *forced* mathematicians to take complex numbers seriously.

In 1545, Cardano published a formula for $x^3 + px + q = 0$:

$$x = \sqrt[3]{-\tfrac{q}{2} + \sqrt{\tfrac{q^2}{4} + \tfrac{p^3}{27}}} \;+\; \sqrt[3]{-\tfrac{q}{2} - \sqrt{\tfrac{q^2}{4} + \tfrac{p^3}{27}}}.$$

For some cubics with three *real* roots — for example $x^3 - 15x - 4 = 0$, which has roots $4, -2 + \sqrt{3}, -2 - \sqrt{3}$ — the inner discriminant $\tfrac{q^2}{4} + \tfrac{p^3}{27}$ comes out **negative**. So you'd be taking the square root of a negative number on the way to a real answer.

Bombelli, in 1572, worked out the rules for computing with these "impossible" objects: $\sqrt{-1}$ has $-\sqrt{-1}$ as a partner, $\sqrt{-1} \cdot \sqrt{-1} = -1$, and you can carry it through arithmetic just like any other symbol. *He verified that the cubic formula's path through $\sqrt{-1}$ terminated correctly at the real answer every time.* The math worked even though no one understood why.

That's the historical "why we have to allow it" moment — not the quadratic, the cubic. (See [[Stories/The Argument for i]] for the full Renaissance-to-quantum-mechanics story.)

---

## §2 Cartesian Form — The Algebra

Every complex number can be written uniquely as $z = a + bi$ with $a, b \in \mathbb{R}$. This is the **Cartesian form** (also called *rectangular form*). Arithmetic in Cartesian form treats $i$ as an algebraic symbol with the single rule $i^2 = -1$.

### Addition and subtraction

Add and subtract real and imaginary parts separately:

$$(a + bi) + (c + di) = (a + c) + (b + d)i, \qquad (a + bi) - (c + di) = (a - c) + (b - d)i.$$

This is exactly **vector addition in the plane**: $(a, b) + (c, d) = (a + c, b + d)$. The Argand-diagram view in §3 makes this picture explicit.

### Multiplication

Distribute, then collapse $i^2$ to $-1$:

$$(a + bi)(c + di) = ac + adi + bci + bd \cdot i^2 = (ac - bd) + (ad + bc)i.$$

The $(ac - bd) + (ad + bc)i$ formula is worth memorising — it's the engine of every complex-number multiplication.

**Worked example.** $(2 + 3i)(4 - i) = (2 \cdot 4 - 3 \cdot (-1)) + (2 \cdot (-1) + 3 \cdot 4)i = (8 + 3) + (-2 + 12)i = 11 + 10i$.

### The conjugate $\bar{z}$

The **complex conjugate** of $z = a + bi$ is

$$\bar{z} = a - bi.$$

(Some textbooks write $z^*$.) Geometrically, $\bar{z}$ is the reflection of $z$ across the real axis. The conjugate has three load-bearing properties:

1. **$z \cdot \bar{z}$ is real and non-negative:** $(a + bi)(a - bi) = a^2 + b^2 \geq 0$. The product is $0$ if and only if $z = 0$.
2. **Conjugation distributes over arithmetic:** $\overline{z + w} = \bar{z} + \bar{w}$, $\overline{zw} = \bar{z}\bar{w}$, $\overline{z/w} = \bar{z}/\bar{w}$.
3. **A real number is its own conjugate:** $\bar{z} = z \iff z \in \mathbb{R}$. (Imaginary parts must be zero.)

### Division — rationalising with the conjugate

To divide complex numbers in Cartesian form, **multiply numerator and denominator by the conjugate of the denominator** — exactly the [[Surds|rationalising]] trick from IGCSE, but with $a^2 + b^2$ in place of $a^2 - b^2$:

$$\dfrac{a + bi}{c + di} = \dfrac{(a + bi)(c - di)}{(c + di)(c - di)} = \dfrac{(ac + bd) + (bc - ad)i}{c^2 + d^2}.$$

The denominator becomes a *real number* $c^2 + d^2$, and you read off real and imaginary parts of the quotient.

**Worked example.** $\dfrac{3 + 2i}{1 + i} = \dfrac{(3 + 2i)(1 - i)}{(1 + i)(1 - i)} = \dfrac{3 - 3i + 2i - 2i^2}{1 - i^2} = \dfrac{(3 + 2) + (-3 + 2)i}{1 + 1} = \dfrac{5 - i}{2} = \tfrac{5}{2} - \tfrac{1}{2}i$.

> [!warning] $\sqrt{-a} \cdot \sqrt{-b}$ ≠ $\sqrt{ab}$ for positive $a, b$
> The familiar surd rule $\sqrt{x}\sqrt{y} = \sqrt{xy}$ **fails** when $x$ and $y$ are negative. Naively: $\sqrt{-1} \cdot \sqrt{-1} = \sqrt{(-1)(-1)} = \sqrt{1} = 1$. But the correct value is $i \cdot i = i^2 = -1$. The $\sqrt{-x}$ notation is itself a danger zone — *use $i\sqrt{x}$ instead*. So write $\sqrt{-9} = 3i$, not $\sqrt{-9} = \sqrt{9}\sqrt{-1}$. The rule "$\sqrt{xy} = \sqrt{x}\sqrt{y}$" was always restricted to $x, y \geq 0$; complex numbers make this restriction visible.

---

## §3 The Argand Diagram — The Geometry

The single insight that dissolves the "weirdness" of complex numbers: **draw them as points in a plane.** Plot $z = a + bi$ at coordinates $(a, b)$ — real part horizontal, imaginary part vertical.

This is the **Argand diagram** (sometimes called the *complex plane* or *Gauss plane*). The real numbers sit on the horizontal axis (the **real axis**), the pure imaginary numbers sit on the vertical axis (the **imaginary axis**), and *every* complex number is somewhere in between.

![[argand-diagram-overview.svg|697]]

In this view:

- **Addition** is vector addition: $z + w$ lands at the parallelogram-rule sum of the points $z$ and $w$.
- **Multiplication by a real number $r > 0$** is scaling: $rz$ stretches $z$ by factor $r$ (toward or away from the origin).
- **Multiplication by $-1$** is rotation by 180° — flipping through the origin.
- **Multiplication by $i$** is rotation by 90° counter-clockwise. *This is the geometric content of $i^2 = -1$:* multiply by $i$ once (90°), again (180°), and you've turned the positive real direction into the negative real direction. So $1 \cdot i \cdot i = -1$. ✓
- **The conjugate $\bar{z}$** is reflection across the real axis.

The historical name "Argand diagram" honours Jean-Robert Argand, a self-taught Swiss bookkeeper who published the construction anonymously in 1806. Caspar Wessel, a Norwegian surveyor, had the same insight in 1799 but published in Danish, and his work was overlooked for almost a century. Gauss made the construction famous in 1831. Three independent rediscoveries in 30 years — the idea was *waiting* to be found. (See [[Stories/The Argument for i]] §"Three Independent Geometric Rediscoveries" for the full story.)

> [!tip] The Argand diagram is the bridge between algebra and geometry
> Every complex-number identity has two readings: an algebraic one (manipulating $a + bi$ symbols) and a geometric one (transforming points in the plane). Most exam questions are easier in one of the two readings. *Get fluent at switching between them.* Multiplication, in particular, is **enormously** simpler in the geometric / polar view (§4) than in the Cartesian distribution-and-collect view of §2.

---

## §4 Modulus and Argument

The Argand diagram lets us re-describe each non-zero complex number by its **distance from the origin** and its **angle from the positive real axis** — exactly polar coordinates.

### Modulus $\lvert z \rvert$

The **modulus** (or *absolute value*, or *length*) of $z = a + bi$ is

$$\lvert z \rvert = \sqrt{a^2 + b^2}.$$

This is just Pythagoras applied to the right triangle with legs $a$ and $b$. The modulus is always non-negative, real, and equals $0$ only when $z = 0$.

Two key identities:

- $z \bar{z} = \lvert z \rvert^2$. This packs Pythagoras into a single algebraic statement: $z \bar{z} = (a + bi)(a - bi) = a^2 + b^2 = \lvert z \rvert^2$. ✓
- $\lvert zw \rvert = \lvert z \rvert \lvert w \rvert$. **Multiplication multiplies moduli.** Try it: $\lvert (3 + 4i)(1 + i) \rvert$ should equal $\lvert 3 + 4i \rvert \cdot \lvert 1 + i \rvert = 5 \cdot \sqrt{2} = 5\sqrt{2}$. Compute the product: $(3 + 4i)(1 + i) = 3 + 3i + 4i + 4i^2 = -1 + 7i$, with modulus $\sqrt{1 + 49} = \sqrt{50} = 5\sqrt{2}$ ✓.

### Argument $\arg(z)$

The **argument** of $z$ is the angle that the line from $0$ to $z$ makes with the positive real axis, measured counter-clockwise. We use radians and write $\arg(z)$.

For $z = a + bi$ with $z \neq 0$:

$$\tan(\arg z) = \dfrac{b}{a} \qquad \text{(but check the quadrant)}.$$

The "check the quadrant" footnote is critical — see misconception 3 below. The argument is determined only up to multiples of $2\pi$, since rotating by a full turn returns to the same point. The convention used at A-Level / 9709 P3 is the **principal argument** $\arg(z) \in (-\pi, \pi]$.

| Quadrant | sign of $a$ | sign of $b$ | $\arg(z)$ |
|---|---|---|---|
| I | $+$ | $+$ | $\arctan(b/a)$ |
| II | $-$ | $+$ | $\pi + \arctan(b/a)$ |
| III | $-$ | $-$ | $-\pi + \arctan(b/a)$ |
| IV | $+$ | $-$ | $\arctan(b/a)$ |

Special cases: $\arg(\text{positive real}) = 0$; $\arg(\text{negative real}) = \pi$; $\arg(i) = \pi/2$; $\arg(-i) = -\pi/2$.

Two key identities:

- $\arg(zw) = \arg z + \arg w$ (mod $2\pi$). **Multiplication adds arguments.**
- $\arg(\bar{z}) = -\arg(z)$. Conjugation reflects across the real axis, so the angle flips sign.

The pair "modulus multiplies, argument adds" under multiplication is the *real* power of the polar view. It turns multiplication into addition-of-angles + multiplication-of-lengths — both vastly simpler than the $(ac - bd) + (ad + bc)i$ formula.

> [!tip] The geometric content of $i^2 = -1$
> $\arg(i) = \pi/2$. Multiplication by $i$ adds $\pi/2$ to the argument. So $i^2$ has argument $\pi/2 + \pi/2 = \pi$ — that's the negative real direction. And $\lvert i \rvert = 1$, so $\lvert i^2 \rvert = 1 \cdot 1 = 1$. *Length 1, angle $\pi$ → that's $-1$.* The algebraic rule "$i^2 = -1$" and the geometric fact "two 90° rotations equals 180°" are the same statement.

---

## §5 Polar (Modulus-Argument) Form

Combining the modulus and argument, we can rewrite a complex number as

$$\boxed{\;z = r(\cos\theta + i\sin\theta)\;}$$

where $r = \lvert z \rvert$ and $\theta = \arg(z)$. This is the **polar form** (or *modulus-argument form* or *trigonometric form*). It's just polar coordinates with an extra $i$ in front of the sine.

To convert from Cartesian to polar: compute $r = \sqrt{a^2 + b^2}$, then $\theta$ via the quadrant table above.
To convert from polar to Cartesian: multiply out $r\cos\theta + ir\sin\theta = (r\cos\theta) + (r\sin\theta)i$, so $a = r\cos\theta$ and $b = r\sin\theta$.

### Multiplication in polar form

This is where polar earns its keep. If $z_1 = r_1(\cos\theta_1 + i\sin\theta_1)$ and $z_2 = r_2(\cos\theta_2 + i\sin\theta_2)$, then

$$z_1 z_2 = r_1 r_2 [\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)].$$

**Multiply moduli, add arguments.** That's it. The proof is direct: distribute and use the [[Trigonometric Identities|compound-angle identities]] $\cos(\theta_1 + \theta_2) = \cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2$ and $\sin(\theta_1 + \theta_2) = \sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2$.

> [!info] A lovely cross-card connection
> The compound-angle identities and complex-number multiplication are *the same fact*. You can read complex multiplication as a proof-by-construction of the compound-angle identities, or you can read the compound-angle identities as the source of complex multiplication. They're inseparable.

### Division in polar form

Same logic in reverse: $\dfrac{z_1}{z_2} = \dfrac{r_1}{r_2}[\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)]$. **Divide moduli, subtract arguments.**

### Worked example — multiplication

Let $z_1 = 2(\cos\tfrac{\pi}{3} + i\sin\tfrac{\pi}{3})$ and $z_2 = 3(\cos\tfrac{\pi}{6} + i\sin\tfrac{\pi}{6})$. Then

$$z_1 z_2 = 2 \cdot 3 \left[\cos\!\left(\tfrac{\pi}{3} + \tfrac{\pi}{6}\right) + i\sin\!\left(\tfrac{\pi}{3} + \tfrac{\pi}{6}\right)\right] = 6\left(\cos\tfrac{\pi}{2} + i\sin\tfrac{\pi}{2}\right) = 6i.$$

Try doing this in Cartesian form: $z_1 = 1 + i\sqrt{3}$, $z_2 = \tfrac{3\sqrt{3}}{2} + \tfrac{3}{2}i$, and $z_1 z_2 = (1 + i\sqrt{3})(\tfrac{3\sqrt{3}}{2} + \tfrac{3}{2}i)$. The arithmetic works out to $6i$ — but it takes ten times longer.

> [!tip] Beyond polar form — Euler's $e^{i\theta}$
> The polar building block $\cos\theta + i\sin\theta$ has an even more compact form: $e^{i\theta}$ (Euler's formula, 1748). Polar multiplication then becomes the IGCSE exponent rule, and powers and roots become trivial. *That's a separate card* — see [[Euler's Formula and De Moivre's Theorem]] for three independent proofs of Euler's formula and the power-tools that follow. For 9709 P3, polar form is sufficient; for IB AA HL, the Euler form is part of the syllabus.

---

## §6 Roots of Polynomials — The Conjugate Root Theorem and FTA

### Conjugate root theorem

If $P(x)$ is a polynomial with **real coefficients** and $z = a + bi$ is a complex root ($b \neq 0$), then $\bar{z} = a - bi$ is *also* a root.

**Why.** Take complex conjugate of the equation $P(z) = 0$. Since the coefficients are real, $\overline{a_n z^n + \ldots + a_0} = a_n \bar{z}^n + \ldots + a_0 = P(\bar{z})$. So $0 = \overline{P(z)} = P(\bar{z})$. ✓

**Consequence.** Complex roots of a real-coefficient polynomial come in **conjugate pairs**. So:

- A *quadratic* with real coefficients has either two real roots or one conjugate pair of complex roots — never one real and one complex.
- A *cubic* with real coefficients has either three real roots or one real + one conjugate pair (so always at least one real root).
- A *quartic* with real coefficients has zero, one, or two conjugate pairs (plus accordingly four, two, or zero real roots).

This is a very common P3 question shape: *"Given that $1 + 2i$ is a root of $z^3 - 5z^2 + 11z - 15 = 0$, find all the roots."* Use the conjugate-root theorem to write down $1 - 2i$ as another root immediately, multiply $(z - (1+2i))(z - (1-2i)) = z^2 - 2z + 5$, and divide the cubic by this quadratic (using [[Polynomial Division]]) to get the third linear factor.

### Fundamental Theorem of Algebra

**Every polynomial of degree $n \geq 1$ with complex coefficients has exactly $n$ roots in $\mathbb{C}$ (counted with multiplicity).**

This is the **Fundamental Theorem of Algebra (FTA)**. It says that *over $\mathbb{C}$, every polynomial factors completely into linear factors* — there are no "irreducible" pieces left over. The irreducible-quadratic case in [[Partial Fractions]] only exists because we're working over $\mathbb{R}$; over $\mathbb{C}$, every quadratic splits into two linear factors.

The FTA's proofs are all non-elementary — they need either complex analysis (Liouville's theorem), topology (degree theory), or algebra-with-some-analysis. Gauss gave the first rigorous proof in 1799 (his doctoral thesis); the cleanest modern proof uses the maximum-modulus principle from complex analysis.

The takeaway: **$\mathbb{C}$ is the *algebraic closure* of $\mathbb{R}$.** Once you have complex numbers, you've solved the polynomial-roots problem forever — there's no further extension needed.

> [!info] Beyond syllabus — algebraic closure
> A field $F$ is *algebraically closed* if every non-constant polynomial with coefficients in $F$ has a root in $F$. The reals are *not* algebraically closed (witness $x^2 + 1 = 0$). The complex numbers *are*. The technical name for $\mathbb{C}$ is "the algebraic closure of $\mathbb{R}$" — the smallest field containing $\mathbb{R}$ in which every polynomial factors completely.

---

## §7 Loci in the Complex Plane

The 9709 P3 §3.9 syllabus tests **loci in the Argand diagram** — sets of complex numbers satisfying a given geometric condition. The standard ones:

### $\lvert z - a \rvert = r$ — circle

Set of points $z$ at distance $r$ from the fixed point $a$. **A circle of radius $r$ centred at $a$.** Reading the algebra: $\lvert z - a \rvert$ is the distance between $z$ and $a$ in the Argand diagram, so saying it equals $r$ is saying $z$ is at distance $r$ from $a$. That's a circle.

### $\lvert z - a \rvert = \lvert z - b \rvert$ — perpendicular bisector

Set of points $z$ equidistant from two fixed points $a$ and $b$. **The perpendicular bisector of the line segment from $a$ to $b$.** Same logic as locus geometry on the Cartesian plane (cf. [[Perpendicular Lines (Vocab)]]).

### $\arg(z - a) = \theta$ — half-line (ray)

Set of points $z$ such that the line from $a$ to $z$ makes angle $\theta$ with the positive real direction. **A half-line (ray) starting at $a$**, pointing in direction $\theta$. The starting point $a$ itself is *excluded* (since $\arg(0)$ is undefined).

### Combining loci — set intersection

Real exam questions often combine two: "find the values of $z$ such that $\lvert z - 2 \rvert = 3$ AND $\arg(z - 2) = \pi/4$." That's a circle intersected with a ray — a single point on the circle.

### Inequalities

$\lvert z - a \rvert \leq r$ is the closed disc of radius $r$ centred at $a$. $\lvert z - a \rvert \geq r$ is the exterior. $\arg(z - a) < \theta_0$ is a half-plane bounded by a ray (handle the principal-argument convention carefully). 9709 P3 questions sometimes ask for the area of a locus region — usually a disc or sector.

---

## §8 Common Misconceptions

### 1. "$i$ is not a real number, so it can't really exist"

The student rejects $i$ as "fake" because it doesn't correspond to a measurable quantity.

**Fix.** Two angles. **Algebraic:** $i$ is *defined* by the rule $i^2 = -1$. That's a *legitimate* mathematical definition; the resulting algebra is internally consistent and matches the rules of any field. Numbers that "don't measure things" include negative numbers (no quantity is $-3$), fractions (no quantity is $\tfrac{1}{2}$ until you slice something), and irrationals ($\pi$ is not a quantity — it's a ratio). $i$ is the same kind of mathematical object: defined by its operational rules, not by what it counts.

**Geometric:** $i$ is the *unit vector* in the imaginary direction of the Argand plane. It corresponds to a 90° rotation. There's nothing "fake" about a 90° rotation. It's a geometric operation that makes a 2D plane work the way it does.

### 2. The $\sqrt{-a} \cdot \sqrt{-b}$ = $\sqrt{ab}$ trap

Naive surd manipulation gives $\sqrt{-1} \cdot \sqrt{-1} = \sqrt{(-1)(-1)} = \sqrt{1} = 1$. But the correct value is $i \cdot i = -1$.

**Fix.** The rule "$\sqrt{x}\sqrt{y} = \sqrt{xy}$" only holds when $x, y \geq 0$. Once negatives are involved, **always rewrite as $i\sqrt{x}$ first**: $\sqrt{-9} = 3i$, *not* $\sqrt{9 \cdot (-1)} = \sqrt{9}\sqrt{-1}$. Memorise the policy: *if you see $\sqrt{-\text{something}}$, the very first move is to extract the $i$.*

### 3. Argument quadrant errors

Computing $\arg(-1 + i) = \arctan(1/(-1)) = \arctan(-1) = -\pi/4$. Wrong — the actual argument is $3\pi/4$ (the point is in quadrant II).

**Fix.** $\arctan$ alone always returns a value in $(-\pi/2, \pi/2)$, which is only correct for points in quadrants I and IV. **Always sketch the point on the Argand diagram first** to identify the quadrant, then use the quadrant table from §4 to adjust. Better still: compute $\arctan(\lvert b \rvert / \lvert a \rvert)$ (a positive reference angle), then add the right sign / multiple of $\pi$ based on the quadrant.

### 4. Forgetting the conjugate root partner

Solving $z^3 - 5z^2 + 11z - 15 = 0$ given that $1 + 2i$ is one root, but only finding it and the third real root — forgetting that $1 - 2i$ must also be a root.

**Fix.** Whenever a real-coefficient polynomial has a complex root, write down the conjugate partner *immediately*. The conjugate-root theorem (§6) is one of the highest-value habits in P3 complex-number questions — it instantly produces a quadratic factor $(z - z_0)(z - \bar{z_0})$ that you can use to polynomial-divide and find the remaining roots.

### 5. Misreading the modulus inequality as an equation

Writing $\lvert z - 2 \rvert \leq 3$ and treating it as $\lvert z - 2 \rvert = 3$ — describing only the boundary circle and missing the interior disc.

**Fix.** Read carefully: $=$ means boundary only (the circle), $\leq$ means closed disc (boundary + interior), $<$ means open disc (interior only, no boundary). The inequalities describe **regions**, not curves. Sketch with shading, not just a curve.

---

## §9 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** Paper 3 §3.9 — *complex numbers*. The 2026–27 syllabus lists:
- Cartesian form $a + bi$ and the meaning of $\Re(z)$, $\Im(z)$; equality via matching real and imaginary parts.
- Argand diagram representation; modulus and argument — and note the syllabus's own flexibility on the interval: *the argument will usually be $-\pi < \theta \leqslant \pi$, but $0 \leqslant \theta < 2\pi$ may be more convenient; answers may use either unless the question specifies*.
- Polar form — and the syllabus writes it as $r(\cos\theta + i\sin\theta) \equiv re^{i\theta}$, so **Euler's form is officially on 9709 P3**, not an extra. Use $re^{i\theta}$ freely; it is the syllabus's own notation.
- Multiplication and division in polar form, including $\lvert z_1 z_2\rvert = \lvert z_1\rvert\lvert z_2\rvert$ and $\arg(z_1z_2) = \arg z_1 + \arg z_2$ with the division counterparts.
- Conjugate $\bar{z}$ and its properties; using $\bar{z}$ to divide in Cartesian form — with the syllabus warning that *full details of the working should be shown* for multiplication and division.
- **Find the two square roots of a complex number** — the syllabus's own example is the square roots of $5 + 12i$ in exact Cartesian form. Method: set $(a+bi)^2 = 5+12i$, match parts ($a^2 - b^2 = 5$, $2ab = 12$), solve the pair — here $\pm(3 + 2i)$. A reliable 4–5 mark question, and again *full working shown*.
- Solving polynomial equations with complex roots, including the conjugate-root theorem for real-coefficient polynomials.
- The **geometrical effects**, in simple terms, of conjugating and of the four operations — reflection in the real axis, translation, rotation-and-scaling.
- Loci in the Argand diagram: $\lvert z - a \rvert = r$, $\lvert z - a \rvert = \lvert z - b \rvert$, $\arg(z - a) = \alpha$, and inequalities thereof.

**What is genuinely *not* on 9709 P3:** **De Moivre's theorem** — that, with roots of unity and the multiple-angle applications, is 9231 territory, taught in [[Euler's Formula and De Moivre's Theorem]].

**Typical question shapes (6–10 marks):**
1. *Express $z = (a + bi)/(c + di)$ in Cartesian form* — rationalise with conjugate. (3 marks)
2. *Find the modulus and argument of $z$* — quadrant-aware. (2 marks)
3. *Write $z$ in polar form* — combining the above. (1–2 marks)
4. *Sketch the locus of $z$ such that $\ldots$ on an Argand diagram* — and compute area / specific points. (3–6 marks)
5. *Find the square roots of $w$ in exact form* — match real and imaginary parts of $(a+bi)^2 = w$. (4–5 marks)
6. *Given that $z = a + bi$ is a root of $P(z) = 0$, find all roots* — use conjugate-root theorem + polynomial-divide. (5–7 marks)

**Tip.** Always sketch the Argand diagram for argument and locus questions. The diagram catches quadrant mistakes that the algebra alone misses.

### A-Level (Edexcel / AQA / OCR / MEI)

Edexcel and AQA include complex numbers in **A2 Pure** at the same level as 9709 P3. OCR's *Further Mathematics* AS course adds De Moivre's theorem, $n$-th roots of unity, and complex-number applications to trigonometric identities (covered in [[Euler's Formula and De Moivre's Theorem]]). All boards converge on the same algebraic content; presentation differs only cosmetically.

### IB AA (HL only)

**Topic refs:** AA HL Topic 1 (Number and Algebra). The IB goes deeper: alongside this card's content, AA HL also tests Euler form $e^{i\theta}$, De Moivre's theorem, $n$-th roots of unity, and applications to trigonometric identities — all in the companion card [[Euler's Formula and De Moivre's Theorem]]. The IB AA HL formula booklet gives Euler's formula and De Moivre's theorem; you don't need to memorise them, but you do need to apply them fluently. AA SL does not test complex numbers at all.

### AP

**AP Calculus AB / BC** does not test complex numbers. (US students typically encounter complex numbers in pre-calculus and revisit them in differential equations / linear algebra at university.)

**AP Pre-calculus** (newer course, 2023+) does include a brief treatment: Cartesian form, conjugate, basic operations. Polar form is out of scope.

### Beyond high school — University

Complex numbers are everywhere at university level: **complex analysis** (calculus done with $z = x + iy$ — holomorphic functions, contour integrals, residue theorem), **differential equations** (complex eigenvalues for oscillation), **quantum mechanics** (wavefunctions are $\mathbb{C}$-valued), **signal processing** (Fourier transforms decompose into complex exponentials), **electrical engineering** (AC impedance), **algebraic number theory** (Gaussian integers $\mathbb{Z}[i]$). For the historical and physical-applications drama, see [[Stories/The Argument for i]].

---

## Connections

- **Direct prerequisite:** [[Quadratic Equations]] — complex roots first appear when $\Delta < 0$ in the [[Discriminant|quadratic discriminant]].
- **Direct prerequisite:** [[Discriminant]] — the $\Delta < 0$ case is what *requires* complex numbers; this card finally cashes in that loose end.
- **Direct prerequisite:** [[Trigonometric Ratios]] — cosine and sine define the polar-form components.
- **Direct prerequisite:** [[Radians]] — arguments are measured in radians.
- **Direct prerequisite:** [[Number Sets (Vocab)]] — places $\mathbb{C}$ at the top of the chain $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$.
- **Direct prerequisite:** [[Vectors]] — the Argand diagram view treats complex numbers as 2D vectors with extra multiplicative structure.
- **Headline sibling card:** [[Euler's Formula and De Moivre's Theorem]] — the power-tools layer. $e^{i\theta} = \cos\theta + i\sin\theta$ with three proofs, De Moivre, $n$-th roots of unity, multiple-angle identities, the unification of exponents and rotations. Read this card first; reach for that one for IB AA HL preparation and computational firepower.
- **Companion identity-source:** [[Trigonometric Identities]] — every compound-angle identity is a one-liner via complex multiplication. The polar multiplication rule §5 *is* the compound-angle identity.
- **Cashes in:** [[Cubic Graphs]] §"Cardano's Formula and the Birth of Complex Numbers" — the historical motivation for complex numbers as forced by the cubic.
- **Cashes in:** [[Discriminant]] §"Complex Conjugate Pair Beyond Syllabus" — the $\Delta < 0$ outcome was promised; here it's delivered.
- **Cashes in:** [[Substitution Equations]] §Galois — complex numbers needed for talking about quintic insolubility; this card grounds the prerequisite.
- **Application:** [[Heptadecagon]] — Gauss's regular 17-gon construction is built on the 17-th roots of unity.
- **Application:** [[Differential Equations]] — second-order linear ODEs with $\Delta < 0$ on the characteristic equation produce oscillatory solutions $e^{(\sigma + i\omega)t}$.
- **Application:** [[Standard Integrals]] — partial-fraction integration over $\mathbb{C}$ extends the real toolkit.
- **Application:** [[Partial Fractions]] §"Decomposition Over $\mathbb{C}$" — the irreducible-quadratic case dissolves over $\mathbb{C}$.
- **Story counterpart:** [[Stories/The Argument for i]] — the 400-year drama from Cardano's cubic to Schrödinger's wavefunction. The historical and physical context that this card sets up but doesn't tell.
- **Story counterpart:** [[Stories/The Hidden Number]] — the 250-year discovery story of $e$. Pairs naturally; both stories are about constants found rather than chosen.

---

## Beyond Syllabus

### The geometry of complex multiplication is rotation + scaling

Recall that a 2×2 matrix $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ rotates the plane by angle $\theta$. Multiply this by a positive scalar $r$ and you have rotation-and-scaling.

The key observation: multiplication by $z = r e^{i\theta}$ acts on the plane *exactly the same way* as the matrix $\begin{pmatrix} r\cos\theta & -r\sin\theta \\ r\sin\theta & r\cos\theta \end{pmatrix}$ acts on $\mathbb{R}^2$. Complex multiplication is a special case of 2×2 matrix multiplication — the special case where the matrix has the rotation-and-scaling form. And conversely, the rotation-and-scaling matrices form a subring of $2 \times 2$ real matrices that's *isomorphic to $\mathbb{C}$ as a field*.

So complex numbers are "the rotations and scalings of 2D space, viewed as numbers." This is why they're the natural language of physics — every wave, every oscillation, every interferometer is *literally* a story about rotations and scalings of an abstract 2D plane.

For the higher-dimensional cousins (quaternions $\mathbb{H}$ for 3D rotations, octonions $\mathbb{O}$, the Hurwitz tower that ends at dimension 8) and for the **load-bearing $i$ in Schrödinger's equation** that distinguishes interference from diffusion in quantum mechanics — see [[Stories/The Argument for i]] §IV–V, where those stories live in their full historical and physical drama.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $i$ | `i` | Imaginary unit; some physics texts write $j$ to avoid clash with current |
| $\mathbb{C}$ | `\mathbb{C}` | The complex numbers as a set / field |
| $\Re(z), \Im(z)$ | `\Re(z), \Im(z)` | Real and imaginary parts |
| $\bar{z}$ | `\bar{z}` | Complex conjugate (some books write `z^*`) |
| $\lvert z \rvert$ | `\lvert z \rvert` | Modulus / absolute value |
| $\arg(z)$ | `\arg(z)` | Argument (use upright `\arg`) |
| $r(\cos\theta + i\sin\theta)$ | `r(\cos\theta + i\sin\theta)` | Polar form (modulus-argument form) |
| $a + bi = c + di \iff a=c, b=d$ | `a + bi = c + di \iff a=c,\, b=d` | Equality as twin real-equation system |

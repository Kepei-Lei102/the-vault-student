---
chinese: 三角恒等式 (sānjiǎo héngděngshì)
prerequisites:
  - "[[Trigonometric Functions]]"
  - "[[Trigonometric Ratios]]"
  - "[[Pythagoras Theorem]]"
  - "[[Radians]]"
  - "[[Coordinate Geometry of the Circle]]"
  - "[[Exact Trigonometric Values]]"
leads_to:
  - "[[Hyperbolic Functions]]"
  - "[[Trigonometric Equations]]"
  - "[[Differentiation Rules]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[Standard Integrals]]"
  - "[[Polar Coordinates]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - level/IGCSE-extension
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-10-4
  - syllabus/0606-10-6
  - syllabus/9709-1-5
  - syllabus/9709-3-3
  - syllabus/9709-2-3
  - type/deep
  - type/identity
  - type/proof
  - notation/sin
  - notation/cos
  - notation/tan
  - notation/sec
  - notation/csc
  - notation/cot
  - misconception/identity-vs-equation
  - misconception/sin-squared-notation
---

# Trigonometric Identities 三角恒等式

## Definition

A **trigonometric identity** is an equality between trigonometric expressions that holds **for every value of the variable** (in the domain where both sides are defined). Compare to a *trigonometric equation*, which is true only for specific values you have to solve for.

The most famous identity, the engine of nearly all the others:

$$
\boxed{\sin^2 x + \cos^2 x = 1}
$$

This is true for **every** real number $x$. Plug in $x = 0$, $x = \pi/4$, $x = \pi$, $x = 17$, $x = -3.7\pi$ — both sides come out equal every time. Identities like this one are the *grammatical rules* of the trigonometric language: they let you rewrite any expression in an equivalent form, and that ability to rewrite is what makes trig manipulation tractable.

### 中文锚点

三角恒等式 = 对所有 $x$（在定义域内）都成立的三角等式。区别于"三角方程"——方程只对**特定** $x$ 成立，需要去解；恒等式对**所有** $x$ 成立，是变形工具。最重要的恒等式 $\sin^2 x + \cos^2 x = 1$ 来自单位圆上的勾股定理：单位圆上一点 $(\cos\theta, \sin\theta)$ 到原点的距离恒为 $1$，所以 $\cos^2\theta + \sin^2\theta = 1$。其他恒等式几乎全是它的推论。

> [!tip] Identity vs equation — keep them separate
> $\sin^2 x + \cos^2 x = 1$ is an **identity** — universally true. $\sin x = \tfrac{1}{2}$ is an **equation** — true only at $x = \pi/6, 5\pi/6, \pi/6 + 2\pi, \dots$ When 0606 §10.6 says *"prove that …"*, they want an identity argument: start with one side, use known identities, transform it into the other side. Solving for $x$ would be the wrong response.

---

## The Pythagorean Identity — Three Derivations

The identity $\sin^2 x + \cos^2 x = 1$ has three equivalent proofs, each shedding different light on why it's true.

### 1. Unit-circle proof (the geometric one)

Place the angle $x$ at the origin, measured anti-clockwise from the positive $x$-axis. The terminal ray meets the unit circle at the point

$$
P = (\cos x, \sin x).
$$

(This is the **definition** of $\cos$ and $\sin$ for any real $x$ — see [[Trigonometric Functions]] for the unit-circle definition.) The distance from the origin to $P$ is the radius — exactly $1$. Apply the distance formula (which is just [[Pythagoras Theorem]] applied to the right triangle with legs $|\cos x|$ and $|\sin x|$ and hypotenuse $1$):

$$
1^2 = (\cos x)^2 + (\sin x)^2 \;\;\Longrightarrow\;\; \cos^2 x + \sin^2 x = 1.
$$

![[trig-identities-unit-circle.svg]]

The Pythagorean identity *is* Pythagoras' theorem written in trigonometric notation. There is no separate fact to memorise — once you see the right triangle inside the unit circle, the identity is forced.

### 2. Right-triangle proof (the SOH-CAH-TOA one)

For an acute angle $\theta$ in a right triangle with hypotenuse $h$, opposite side $o$, and adjacent side $a$:

$$
\sin\theta = \frac{o}{h}, \qquad \cos\theta = \frac{a}{h}.
$$

Squaring and adding:

$$
\sin^2\theta + \cos^2\theta = \frac{o^2 + a^2}{h^2} = \frac{h^2}{h^2} = 1
$$

where the second equality is Pythagoras applied to the right triangle ($o^2 + a^2 = h^2$). This proof works only for acute $\theta$, but the unit-circle definition extends it to all real $x$.

### 3. Calculus / power-series proof (beyond syllabus, A-Level / IB HL)

Define $\cos x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$ and $\sin x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ as power series. Differentiate $f(x) = \sin^2 x + \cos^2 x$:

$$
f'(x) = 2\sin x\cos x + 2\cos x \cdot (-\sin x) = 0.
$$

So $f$ is constant. Evaluate at $x = 0$: $f(0) = 0 + 1 = 1$. Therefore $\sin^2 x + \cos^2 x = 1$ everywhere.

This proof doesn't *use* Pythagoras — it bootstraps the identity from the analytic definitions of sin and cos. The fact that the geometric proof and the analytic proof agree is one of the small miracles that made nineteenth-century mathematicians comfortable extending trigonometry beyond the unit circle.

---

## The Two Corollary Pythagorean Identities

Divide the master identity by $\cos^2 x$ (assuming $\cos x \neq 0$):

$$
\frac{\sin^2 x}{\cos^2 x} + \frac{\cos^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}
\;\;\Longrightarrow\;\;
\boxed{\tan^2 x + 1 = \sec^2 x}
$$

Divide instead by $\sin^2 x$ (assuming $\sin x \neq 0$):

$$
\frac{\sin^2 x}{\sin^2 x} + \frac{\cos^2 x}{\sin^2 x} = \frac{1}{\sin^2 x}
\;\;\Longrightarrow\;\;
\boxed{1 + \cot^2 x = \csc^2 x}
$$

These two are syllabus-named on Cambridge 0606 §10.4. Each is **just the master identity divided through** — no separate memorisation if you remember the master and the divisions. (Some boards write them as $\sec^2 x = 1 + \tan^2 x$ and $\csc^2 x = 1 + \cot^2 x$ — same thing, terms reordered.)

> [!info] Beyond syllabus — geometric reading of $\sec^2 = 1 + \tan^2$
> Inside the unit circle, draw the radius to $P = (\cos x, \sin x)$. Now extend the radius outward until it hits the **vertical tangent line** $X = 1$ (the line $x = 1$). The extension hits at the point $(1, \tan x)$, and its distance from the origin is exactly $\sec x$. The right triangle with vertices $(0,0)$, $(1,0)$, $(1, \tan x)$ has legs $1$ and $\tan x$ with hypotenuse $\sec x$. Pythagoras: $1 + \tan^2 x = \sec^2 x$. The same picture explains why "secant" and "tangent" are named after the geometric *secant line* (cuts the circle, length to the tangent point) and *tangent line* (touches the circle once). 17th-century names; same picture.

---

## Reciprocal and Quotient Identities

These three pairs are definitional — each new function is just shorthand:

| Identity | LHS in plain English | Why |
|---|---|---|
| $\sec x = \dfrac{1}{\cos x}$ | secant is the reciprocal of cosine | definition |
| $\csc x = \dfrac{1}{\sin x}$ | cosecant is the reciprocal of sine | definition |
| $\cot x = \dfrac{1}{\tan x} = \dfrac{\cos x}{\sin x}$ | cotangent is the reciprocal of tangent | two equivalent forms |
| $\tan x = \dfrac{\sin x}{\cos x}$ | tangent is sine-over-cosine | from unit-circle right triangle |

> [!tip] The "convert to sine and cosine" tactic
> When stuck on an identity proof, **rewrite everything in terms of $\sin$ and $\cos$** using the table above. Most identities collapse once you do this, because $\sin$ and $\cos$ are the only two trig functions with a Pythagorean identity tying them together — the other four are derived. This is by far the most common move in §10.6 proof questions.

---

## Even–Odd and Co-function Identities

These come straight from the symmetry of the unit circle.

**Even/odd** (substitute $-x$ for $x$):

| Identity | Type |
|---|---|
| $\cos(-x) = \cos x$ | even |
| $\sin(-x) = -\sin x$ | odd |
| $\tan(-x) = -\tan x$ | odd |
| $\sec(-x) = \sec x$ | even |
| $\csc(-x) = -\csc x$ | odd |
| $\cot(-x) = -\cot x$ | odd |

The geometric reason: reflecting across the $x$-axis takes $(\cos x, \sin x)$ to $(\cos x, -\sin x)$ — the $x$-coordinate stays, the $y$-coordinate flips. So $\cos$ is even, $\sin$ is odd, and the rest follow.

**Co-function** (replace $x$ with $\tfrac{\pi}{2} - x$):

| Identity | Geometric meaning |
|---|---|
| $\cos(\tfrac{\pi}{2} - x) = \sin x$ | the *complement* of $x$ swaps $\cos$ ↔ $\sin$ |
| $\sin(\tfrac{\pi}{2} - x) = \cos x$ | (this is where the *co* in *co*sine comes from) |
| $\cot(\tfrac{\pi}{2} - x) = \tan x$ | likewise for *co*tangent and *co*secant |

The complement of an angle in a right triangle is the *other* acute angle, and the opposite/adjacent legs swap roles between them. So $\sin$ of one acute angle equals $\cos$ of its complement.

---

## Sum and Difference Formulas (9709 P3 / A-Level / IB / AP — beyond 0606)

Cambridge 0606 §10.4 stops at the Pythagorean trio. Students continuing to **9709 Paper 3 §3.3**, A-Level Pure Mathematics, IB AA, or AP need the **sum and difference formulas**:

$$
\begin{aligned}
\sin(A + B) &= \sin A\cos B + \cos A\sin B \\
\sin(A - B) &= \sin A\cos B - \cos A\sin B \\
\cos(A + B) &= \cos A\cos B - \sin A\sin B \\
\cos(A - B) &= \cos A\cos B + \sin A\sin B \\
\tan(A + B) &= \frac{\tan A + \tan B}{1 - \tan A\tan B}
\end{aligned}
$$

The signs follow the rule **"sin keeps the sign, cos flips it"** — $\sin(A \pm B)$ has $\pm$ on the right; $\cos(A \pm B)$ has $\mp$. This is the most-failed sign convention in trig.

The **double-angle formulas** are the special case $A = B$:

$$
\begin{aligned}
\sin 2x &= 2\sin x\cos x \\
\cos 2x &= \cos^2 x - \sin^2 x \\
        &= 1 - 2\sin^2 x \\
        &= 2\cos^2 x - 1 \\
\tan 2x &= \frac{2\tan x}{1 - \tan^2 x}
\end{aligned}
$$

The three forms of $\cos 2x$ are all equivalent (use $\sin^2 + \cos^2 = 1$ to convert between them). They're useful in different situations — when you need to leave the answer in $\sin$, use the second form; in $\cos$, use the third.

### The whole table from one master formula

Of the eight sum/difference/double-angle formulas above, **only one needs an honest proof** — the rest are mechanical consequences. The master is:

$$
\cos(A - B) = \cos A\cos B + \sin A\sin B \tag{$\star$}
$$

Once you have ($\star$), the chain of consequences is:

1. **$\cos(A + B)$** — replace $B$ with $-B$ in ($\star$). By the even/odd identities ($\cos(-B) = \cos B$, $\sin(-B) = -\sin B$):
$$\cos(A + B) = \cos A\cos B - \sin A\sin B.$$
2. **$\sin(A + B)$** — use the co-function identity $\sin\theta = \cos\!\left(\tfrac{\pi}{2} - \theta\right)$:
$$\sin(A + B) = \cos\!\left(\tfrac{\pi}{2} - A - B\right) = \cos\!\left(\left(\tfrac{\pi}{2} - A\right) - B\right).$$
Now apply ($\star$) with $A \to \tfrac{\pi}{2} - A$:
$$= \cos\!\left(\tfrac{\pi}{2} - A\right)\cos B + \sin\!\left(\tfrac{\pi}{2} - A\right)\sin B = \sin A\cos B + \cos A\sin B.$$
3. **$\sin(A - B)$** — replace $B$ with $-B$ in step 2: $\sin A\cos B - \cos A\sin B$.
4. **$\tan(A \pm B)$** — take the quotient $\sin / \cos$ and divide top and bottom by $\cos A\cos B$:
$$\tan(A + B) = \frac{\sin A\cos B + \cos A\sin B}{\cos A\cos B - \sin A\sin B} = \frac{\tan A + \tan B}{1 - \tan A\tan B}.$$
5. **Double-angle** — set $A = B$ in steps 1, 2, 4: $\sin 2A = 2\sin A\cos A$, $\cos 2A = \cos^2 A - \sin^2 A$, $\tan 2A = \tfrac{2\tan A}{1 - \tan^2 A}$. The other two forms of $\cos 2A$ ($1 - 2\sin^2 A$ and $2\cos^2 A - 1$) come from the Pythagorean identity.

So the whole eight-formula table reduces to **one proof, four substitution moves, and the Pythagorean identity**. Memorising the eight formulas separately is the wrong study strategy; memorise ($\star$) and the chain.

> [!info] Beyond syllabus — the dot-product proof of ($\star$)
> The cleanest proof of $\cos(A - B) = \cos A\cos B + \sin A\sin B$ uses the **dot product** of two unit vectors. Take $\vec u = (\cos A, \sin A)$ and $\vec v = (\cos B, \sin B)$ — both unit-length points on the unit circle. The angle between them is $A - B$, so by the geometric definition of the dot product: $\vec u \cdot \vec v = |\vec u||\vec v|\cos(A - B) = \cos(A - B)$. Computing the dot product algebraically gives $\cos A\cos B + \sin A\sin B$. Equating the two — done. (See [[Vectors]] for the algebraic-vs-geometric definitions of the dot product.) Two other classical proofs: (a) the *geometric chord-length* proof — compute the chord $|UV|$ two ways using the distance formula and the law of cosines; (b) the *complex exponential* proof — multiply $e^{iA} \cdot e^{-iB}$ and read off real and imaginary parts (uses Euler's formula, university bridge).

---

## Worked Identity Proofs (the §10.6 skill)

Cambridge 0606 §10.6 explicitly tests **proving identities**. The standard play: pick the more complicated side, transform it using identities until it equals the other side. (If both sides look ugly, work each toward a common middle.)

**Example 1.** Prove that $\dfrac{\cos x}{1 - \sin x} + \dfrac{\cos x}{1 + \sin x} = \dfrac{2}{\cos x}$.

Common denominator on the LHS:

$$
\text{LHS} = \frac{\cos x(1 + \sin x) + \cos x(1 - \sin x)}{(1 - \sin x)(1 + \sin x)}
= \frac{2\cos x}{1 - \sin^2 x}
= \frac{2\cos x}{\cos^2 x}
= \frac{2}{\cos x} = \text{RHS}. \;\square
$$

The key move was **$(1 - \sin x)(1 + \sin x) = 1 - \sin^2 x = \cos^2 x$** — a difference of squares followed by Pythagoras. Watch for this pattern; it's everywhere.

**Example 2.** Prove that $\sin^4 x - \cos^4 x = \sin^2 x - \cos^2 x$.

Difference of squares:

$$
\text{LHS} = (\sin^2 x - \cos^2 x)(\sin^2 x + \cos^2 x) = (\sin^2 x - \cos^2 x) \cdot 1 = \text{RHS}. \;\square
$$

**Example 3.** Prove that $\tan x + \cot x = \sec x \csc x$.

Convert to sine and cosine:

$$
\text{LHS} = \frac{\sin x}{\cos x} + \frac{\cos x}{\sin x}
= \frac{\sin^2 x + \cos^2 x}{\sin x\cos x}
= \frac{1}{\sin x\cos x}
= \csc x\sec x = \text{RHS}. \;\square
$$

**Example 4.** Prove that $\dfrac{1 + \cos x}{\sin x} = \dfrac{\sin x}{1 - \cos x}$.

Cross-multiply (this is just rewriting — both sides equal a third quantity):

$$
(1 + \cos x)(1 - \cos x) = \sin^2 x.
$$

LHS expands to $1 - \cos^2 x$, which equals $\sin^2 x$ by Pythagoras. So the cross-multiplication is valid, hence the original identity. (For full rigour, also note that $\sin x \neq 0$ and $1 - \cos x \neq 0$ for the fractions to be defined — i.e., $x \neq n\pi$.) $\;\square$

The four standard tactics covered above: (1) convert to $\sin$ and $\cos$; (2) common denominator + Pythagoras; (3) difference of squares + Pythagoras; (4) cross-multiply if both sides are fractions. Most §10.6 identities yield to one of these.

---

## Common Mistakes

1. **Squared-function notation pitfall.** $\sin^2 x$ means $(\sin x)^2$, *not* $\sin(\sin x)$ and *not* $\sin(x^2)$. The "$2$" lives between $\sin$ and the argument by historical convention. The exception: $\sin^{-1} x$ means $\arcsin x$, *not* $1/\sin x$ — for the reciprocal you must write $(\sin x)^{-1}$ or $\csc x$. Notation is unfortunate; conventions are fixed.
2. **Confusing $\sec$ with $\sin^{-1}$.** $\sec x = 1/\cos x$; $\sin^{-1} x = \arcsin x$. Not the same. The reciprocals of $\sin$, $\cos$, $\tan$ are $\csc$, $\sec$, $\cot$. The inverses are $\arcsin$, $\arccos$, $\arctan$ (also written $\sin^{-1}$, etc., out of historical accident).
3. **Treating an identity proof as solving an equation.** "Prove that LHS = RHS" does *not* mean "solve LHS = RHS for $x$". It means: starting from one side, transform it via known identities until you reach the other side. Never *assume* the identity at the start and manipulate both sides — that's a logical mistake (you've assumed what you wanted to prove).
4. **Sign drift in sum/difference formulas.** $\cos(A + B) = \cos A\cos B - \sin A\sin B$ (minus). $\cos(A - B) = \cos A\cos B + \sin A\sin B$ (plus). The cos formulas *flip* the sign; the sin formulas *keep* it. The mnemonic: "**c**os contradicts, **s**in stays."
5. **Domain blindness.** Identities like $\tan x = \sin x / \cos x$ hold *where both sides are defined* — at $x = \pi/2$, both sides are undefined and the identity is silent there. In a proof you don't normally need to flag this, but for a *rigorous* proof on a high-mark question, mention "for $\cos x \neq 0$" to be safe.

---

## Exam Notes

### Cambridge 0606

**Syllabus refs:** §10.4 (use of identities) and §10.6 (proofs of identities). The Pythagorean trio is examined explicitly:

- $\sin^2 x + \cos^2 x = 1$
- $\sec^2 x = 1 + \tan^2 x$
- $\csc^2 x = 1 + \cot^2 x$

Plus reciprocal and quotient identities. **Sum/difference and double-angle formulas are not on 0606** — but they're prerequisites for the harder [[Trigonometric Equations]] problems (multiple-angle reductions, $R\sin(x+\alpha)$ form).

### Memorise? — per board

The four-board exam-strategy table for trig identities. Same legend as [[Standard Integrals]] / [[Differentiation Rules]]: ✅ given on booklet, 📝 must memorise, 🛠 derive, ⚪ off-syllabus. Sources: [[MF19 Reference (9709)]], [[Edexcel IAL Reference]], [[OxAQA 9660 Reference]], [[AP Calculus Reference]].

| Identity family | 9709 | IAL | 9660 | AP |
|---|:---:|:---:|:---:|:---:|
| **Pythagorean** $\sin^2\theta + \cos^2\theta \equiv 1$ | ✅ | 📝 | 📝 | 📝 |
| **Pythagorean corollary** $1 + \tan^2 \equiv \sec^2$ | ✅ | 📝 | 📝 | 📝 |
| **Pythagorean corollary** $1 + \cot^2 \equiv \csc^2$ | ✅ | 📝 | 📝 | 📝 |
| **Reciprocal** $\sec, \csc, \cot$ definitions | 📝 | 📝 | 📝 | 📝 |
| **Quotient** $\tan = \sin/\cos$ | ✅ | 📝 | 📝 | 📝 |
| **Even / Odd** $\sin(-x) = -\sin x$, $\cos(-x) = \cos x$ | 📝 | 📝 | 📝 | 📝 |
| **Co-function** $\sin(\pi/2 - x) = \cos x$ | 📝 | 📝 | 📝 | 📝 |
| **Sum / difference** $\sin(A \pm B)$, $\cos(A \pm B)$, $\tan(A \pm B)$ | ✅ | ✅ | ✅ | 📝 |
| **Double-angle** $\sin 2A$, $\cos 2A$ (3 forms), $\tan 2A$ | ✅ | 🛠 from sum | 🛠 from sum | 📝 |
| **Half-angle** $\sin^2(x/2)$, $\cos^2(x/2)$ | 🛠 from $\cos 2A$ | 🛠 from sum | 🛠 from sum | 🛠 |
| **Sum-to-product (factor formulas)** $\sin A \pm \sin B$, $\cos A \pm \cos B$ | 📝 | ✅ | ✅ | 📝 |
| **R-formula** $a\sin x + b\cos x = R\sin(x + \alpha)$ | 📝 (derive from sum) | 📝 | 📝 | 📝 |
| **Sine rule** $\dfrac{a}{\sin A} = \dfrac{b}{\sin B}$ | 📝 | 📝 | 📝 | ⚪ pre-calc |
| **Cosine rule** $a^2 = b^2 + c^2 - 2bc\cos A$ | 📝 | 📝 | ✅ | ⚪ pre-calc |
| **Triangle area** $\tfrac{1}{2}ab \sin C$ | 📝 | 📝 | 📝 | ⚪ pre-calc |

> [!info] Three patterns this table makes visible
>
> **Pattern 1 — Cambridge MF19 wins on the Pythagoreans.** All three Pythagorean forms are on MF19; the other three boards leave them as memorise. Pythagoreans appear in *every* trig integration problem, so this is a real exam-day cost for IAL / 9660 / AP students.
>
> **Pattern 2 — IAL and 9660 win on sum-to-product.** Their booklets give all four factor formulas; MF19 doesn't (and AP has no sheet). Sum-to-product comes up in compound-equation problems and in some integration tricks; Cambridge students have to derive on the day.
>
> **Pattern 3 — Sine rule and cosine rule are nobody's free lunch (except 9660 on cosine rule).** Triangle solving formulas are basic enough that no booklet bothers — except 9660 prints the cosine rule, presumably because of its connection to vector dot product. *9660 students get a Pure-page reminder of the cosine rule; Cambridge / IAL / AP students have to remember it from secondary school.*
>
> **Net for trig identities:** the must-memorise list compresses to the master Pythagorean ($\sin^2 + \cos^2 = 1$), reciprocal/quotient/even-odd/co-function definitions (all of which are visually obvious from the unit circle), the R-formula transformation skill, and the triangle rules. Sum/difference, double-angle, sum-to-product are all formula-derivable from one master sum formula — see the section above on "the whole table from one master formula". *Memorise the master sum formula and the Pythagorean; everything else falls out by sub or division.*

### A-Level (Pure Mathematics)

Sum/difference, double-angle, half-angle, and the $R\sin(x + \alpha)$ form (writing $a\sin x + b\cos x$ as a single sinusoid) are A-Level Year 2 content. The dot-product proof of $\cos(A - B)$ is sometimes given as bookwork.

### IB AA / IB AI

IB AA HL covers compound-angle identities, double-angle identities, and the trig-equation applications in depth. IB AI keeps the trig identities lighter — Pythagorean trio plus reciprocal/quotient.

### AP

AP Precalculus covers the Pythagorean trio, reciprocal/quotient, sum/difference, and double-angle. AP Calculus AB and BC use them constantly in trig integrals and trig substitutions.

---

## Connections

- **Prerequisite:** [[Trigonometric Functions]] — the unit-circle definition that makes the Pythagorean identity geometric
- **Prerequisite:** [[Trigonometric Ratios]] — SOH-CAH-TOA for the right-triangle derivation
- **Prerequisite:** [[Pythagoras Theorem]] — the engine of every Pythagorean identity
- **Prerequisite:** [[Radians]] — domain over which the identities live; calculus and IB-level identities are stated in radians
- **Sibling:** [[Sine and Cosine Rules]] — geometric trig identities for general triangles (vs identities for a *single* angle here)
- **Leads to:** [[Trigonometric Equations]] — solving uses identities to reduce the equation to a single trig function
- **Leads to:** [[Differentiation Rules]] — $\frac{d}{dx}\sin x = \cos x$ and the rest of the trig derivative table; the proof uses $\sin(A+B)$ and the small-angle limit
- **Leads to:** [[Coordinate Geometry of the Circle]] — the parametric form $(a + r\cos\theta, b + r\sin\theta)$ uses $\cos^2 + \sin^2 = 1$ to verify the equation
- **Application:** [[Integration by Substitution]] — trig substitutions like $x = a\sin\theta$ rely on $1 - \sin^2\theta = \cos^2\theta$
- **Application:** physics — wave superposition uses sum-to-product identities; AC circuit analysis uses $R\sin(x + \alpha)$ form
- **Beyond high school:** Fourier series — every periodic function is a sum of $\sin$ and $\cos$, and the orthogonality of $\sin nx$, $\cos mx$ is itself an identity (integrals of products vanish unless $n = m$)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\sin^2 x$ | `\sin^2 x` | shorthand for $(\sin x)^2$ |
| $\sin^{-1} x$ | `\sin^{-1} x` | $\arcsin x$, **not** $\csc x$ |
| $\sec x$ | `\sec x` | $1/\cos x$ |
| $\csc x$ | `\csc x` | $1/\sin x$ |
| $\cot x$ | `\cot x` | $1/\tan x = \cos x / \sin x$ |
| $\arcsin x$ | `\arcsin x` | inverse sine; preferred over $\sin^{-1}$ in proofs |
| $\equiv$ | `\equiv` | "is identically equal to" — sometimes used in identity statements |
| $\square$ | `\square` | end-of-proof marker |

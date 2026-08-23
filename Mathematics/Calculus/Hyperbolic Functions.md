---
chinese: 双曲函数 (shuāngqū hánshù)
prerequisites:
  - "[[Exponential Function]]"
  - "[[Logarithms]]"
  - "[[Trigonometric Identities]]"
leads_to:
  - "[[Standard Integrals]]"
  - "[[Arc Length and Surfaces of Revolution]]"
tags:
  - subject/mathematics
  - domain/calculus
  - domain/functions
  - level/A-Level
  - curriculum/A-Level
  - curriculum/Cambridge-9231
  - curriculum/OxAQA-9660
  - syllabus/9231-2-1
  - syllabus/9231-2-3
  - syllabus/9231-2-4
  - type/deep
  - type/definition
  - type/proof
  - notation/sinh
  - notation/cosh
  - notation/arsinh
  - misconception/hyperbolic-parameter-is-an-angle
  - misconception/cosh-derivative-has-a-minus
  - misconception/osborn-is-arbitrary
  - misconception/arcosh-plus-or-minus-is-a-choice
  - misconception/hanging-chain-is-a-parabola
---

# Hyperbolic Functions 双曲函数

> *Someone hands you $\dfrac{e^x + e^{-x}}{2}$ and calls it a cosine. It has no obvious right to the name: nothing here repeats, nothing goes round, and the graph is a single valley that runs off to infinity in both directions. Yet it obeys almost every identity $\cos$ obeys, its derivative behaves almost like $\cos$'s, and it is genuinely the shape a chain makes when you let it hang. The word "almost" hides one minus sign, and that sign is the whole story — where it comes from, why it lands exactly where it does, and why the answer explains both the name and the fact that the inverses of these functions turn out to be **logarithms**.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| hyperbolic function | 双曲函数 | the $e^x$ combinations that parametrise a hyperbola |
| hyperbolic sine / cosine | 双曲正弦 / 双曲余弦 | $\sinh$, $\cosh$ — the odd and even parts of $e^x$ |
| unit hyperbola | 单位双曲线 | $x^2 - y^2 = 1$, the curve these functions trace |
| hyperbolic angle | 双曲角 | the parameter — genuinely an **area**, not an angle |
| even / odd function | 偶函数 / 奇函数 | $f(-x) = f(x)$ / $f(-x) = -f(x)$ |
| Osborn's rule | 奥斯本法则 | convert a trig identity by flipping every $\sin \times \sin$ |
| logarithmic form | 对数形式 | the inverse hyperbolic functions written with $\ln$ |
| catenary | 悬链线 | the curve of a hanging chain, $y = a\cosh(x/a)$ |

## The definitions, and why *these* combinations

$$\boxed{\ \cosh x = \frac{e^x + e^{-x}}{2}, \qquad \sinh x = \frac{e^x - e^{-x}}{2}\ }$$

**The `h` is literally "hyperbolic"** — $\sinh$ is *sine, hyperbolic*, $\cosh$ is *cosine, hyperbolic*, and so on down the six. Read them aloud as "cosh", "sinch" (or "shine"), and "tanch". If you have never pressed those keys on a calculator, that is not an oversight: they appear on no single-maths A-Level, no IB course and neither AP Calculus, so most students meet the button years before the mathematics. The four remaining functions are built from the first two exactly as their trigonometric namesakes are:

$$\tanh x = \frac{\sinh x}{\cosh x}, \qquad \operatorname{sech} x = \frac{1}{\cosh x}, \qquad \operatorname{cosech} x = \frac{1}{\sinh x}, \qquad \coth x = \frac{1}{\tanh x}$$

Why those two combinations rather than any others? Because they are not a choice at all.

> **Every function splits, in exactly one way, into an even part and an odd part.**

That deserves better than being asserted, so here it is in three steps: *find* the split, *check* it, and *prove there is no other one.*

**Finding it.** Suppose such a split exists — write $f(x) = E(x) + O(x)$ with $E$ even and $O$ odd. Now feed in $-x$ and use what even and odd *mean*: $E(-x) = E(x)$ and $O(-x) = -O(x)$. That gives a second equation, and two equations in two unknowns is something you have solved since school:

$$\begin{aligned} f(x) &= E(x) + O(x) \\ f(-x) &= E(x) - O(x) \end{aligned}$$

Add them: $f(x) + f(-x) = 2E(x)$. Subtract them: $f(x) - f(-x) = 2O(x)$. So if a split exists, it can only be

$$E(x) = \frac{f(x) + f(-x)}{2}, \qquad O(x) = \frac{f(x) - f(-x)}{2}$$

Nothing was guessed. The formulas were *forced* by simultaneous equations.

**Checking it.** Those two do the job: replacing $x$ by $-x$ leaves the first unchanged and flips the sign of the second, and adding them returns $f(x)$. So the split exists.

**Proving it is the only one.** Suppose $f = E + O = E' + O'$, both splits legitimate. Rearranging, $E - E' = O' - O$. The left side is a difference of even functions, so it is even; the right side is a difference of odd functions, so it is odd. Call that common function $g$: it is both even and odd, so $g(-x) = g(x)$ *and* $g(-x) = -g(x)$. Therefore $g(x) = -g(x)$, so $2g(x) = 0$, so $g$ is identically zero — which forces $E = E'$ and $O = O'$. The split is unique. $\blacksquare$

Now put $f(x) = e^x$ into the formulas that were forced on us, and read off what comes out:

$$e^x = \cosh x + \sinh x$$

So $\cosh$ and $\sinh$ are not inventions. They are **the even and odd halves of the exponential function**, which is why they turn up whenever $e^x$ and $e^{-x}$ appear together — in the general solution of $y'' = y$, in a hanging chain, in a falling body with drag. Once you have met them, you stop seeing $\tfrac{1}{2}(e^x + e^{-x})$ and start seeing $\cosh$.

Two immediate consequences, free of charge: $\cosh$ is **even** and $\sinh$ is **odd** ($\cosh(-x) = \cosh x$, $\sinh(-x) = -\sinh x$), and $\cosh x + \sinh x = e^x$ while $\cosh x - \sinh x = e^{-x}$.

## Why "hyperbolic" — and why the parameter is not an angle

The name is earned by a parallel that is exact, and by one difference that matters.

**The circular functions parametrise a circle.** The point $(\cos t, \sin t)$ satisfies $x^2 + y^2 = 1$ for every $t$, so as $t$ runs it traces the unit circle.

**The hyperbolic functions parametrise a hyperbola.** The point $(\cosh t, \sinh t)$ satisfies $x^2 - y^2 = 1$, so as $t$ runs it traces the right branch of the unit hyperbola. The proof is one line, straight from the definitions:

$$\cosh^2 t - \sinh^2 t = \frac{(e^t + e^{-t})^2 - (e^t - e^{-t})^2}{4} = \frac{4 e^t e^{-t}}{4} = 1$$

$$\boxed{\ \cosh^2 t - \sinh^2 t \equiv 1\ }$$

Now the difference, which is the part usually left out and the part that makes everything else make sense. **In neither case is the parameter an angle.**

![[hyperbolic-circle-vs-hyperbola.svg]]

For the circle, $t$ *happens* to be the angle in radians — but it is also, and more fundamentally, **twice the area of the sector** swept from the positive $x$-axis. (A sector of angle $t$ in a unit circle has area $t/2$; the whole circle is $t = 2\pi$, area $\pi$.) For the hyperbola there is no angle to speak of — but the area statement survives untouched: **$t$ is twice the area of the region between the two rays and the curve.** That is one half of why $t$ is called the *hyperbolic angle*: area is what the circular "angle" was really measuring all along. But if there is no arc to measure, the name still has to earn itself, and it does — for a better reason than analogy.

**An angle's defining job is that angles add.** Turn by $a$, then turn by $b$, and you have turned by $a+b$; that is what makes $\cos(a+b)$ expressible in terms of $\cos a, \cos b, \sin a, \sin b$ at all. The hyperbolic parameter does exactly the same thing:

$$\cosh(a+b) = \cosh a \cosh b + \sinh a \sinh b, \qquad \sinh(a+b) = \sinh a \cosh b + \cosh a \sinh b$$

And there *is* a rotation — just not a Euclidean one. A Euclidean rotation is the matrix that preserves $x^2+y^2$; the transformation that preserves $x^2-y^2$ is its hyperbolic counterpart:

$$H(t) = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}, \qquad \det H(t) = \cosh^2 t - \sinh^2 t = 1$$

Multiply two of them and the addition formulas above are exactly what falls out: $H(a)\,H(b) = H(a+b)$. **The parameters add under composition, which is precisely what a rotation angle does** — so $t$ is an angle in the only sense that was ever load-bearing. It slides points *along* the hyperbola the way an angle slides points around a circle, stretching one diagonal and squeezing the other.

That is not an ornament. In relativity this matrix is the **Lorentz boost** and $t$ is the **rapidity** — which is why velocities refuse to add while rapidities add perfectly, a point the closing section returns to. The hyperbolic angle earned its name by doing an angle's job.

This is worth holding on to, because it pays for itself twice. It explains the odd-looking names of the inverses — properly $\operatorname{arsinh}$, $\operatorname{arcosh}$, $\operatorname{artanh}$, from **ar**ea, not $\mathrm{arc}$; there is no arc to measure. And it predicts, before any algebra, that those inverses will be **logarithms**, for a reason worth its own paragraph.

> [!tip] Why the inverses are logarithms — the two hyperbolas are the same curve
> [[Euler's Number]] records that in 1647 Saint-Vincent found the area under $y = 1/x$ behaves like a logarithm — the discovery [[Stories/The Hidden Number]] builds its second act on. That curve, $xy = 1$, is a **rectangular hyperbola**; rotate it by $45°$ and it becomes $x^2 - y^2 = 2$. It is the same conic, seen from a different angle: our unit hyperbola $x^2 - y^2 = 1$ is $xy = \tfrac12$ wearing a different coordinate system.
>
> So "the natural logarithm is an area under a hyperbola" and "the hyperbolic angle is an area under a hyperbola" are two descriptions of one fact. The inverse hyperbolic functions come out as logarithms not by algebraic accident but because **both are the same area measurement on the same curve.** The quadratic derivation below is how you *produce* the formula in an exam; this is why the formula was always going to look like that.

## The graphs

![[hyperbolic-graphs.svg]]

Everything visible here is already implied by $e^x = \cosh x + \sinh x$:

- **$\cosh x$** is even, has minimum value $\boxed{\cosh 0 = 1}$ — it never dips below 1 — and for large $x$ hugs $\tfrac12 e^{x}$, since $\tfrac12 e^{-x}$ dies away. Both arms rise; the graph is a valley, not a wave.
- **$\sinh x$** is odd, passes through the origin, and is strictly increasing — so it is **one-to-one**, and its inverse needs no restriction.
- **$\tanh x$** is odd, increasing, and squeezed between the horizontal asymptotes $y = \pm 1$: as $x \to \infty$ the $e^{-x}$ terms vanish and $\tanh x \to e^x/e^x = 1$. It is the classic S-curve, which is why it turns up as a *squashing* function anywhere a real number must be mapped into a bounded range.

Sketching marks go to: the correct intercept ($\cosh$ through $(0,1)$, the other two through the origin), the asymptotes on $\tanh$, and the symmetry.

## Osborn's rule — see it, then believe it, then prove it

The claim in the opening was that these functions obey almost every identity their trigonometric namesakes obey. Said flatly it is hard to swallow, because the functions look nothing alike — one pair oscillates forever between $-1$ and $1$, the other pair runs off to infinity and never comes back. So look at the claim before arguing for it:

![[hyperbolic-identity-check.svg]]

Nothing about the left and right halves matches. Feed them into their respective combinations and **the output is the same flat line at 1.** That is the whole phenomenon in one picture: the *functions* are unrelated to look at, and the *structure* is identical. Now the reason.

### Why the structure survives — same machine, different fuel

Here is the fact that makes all of it obvious in hindsight. [[Euler's Formula and De Moivre's Theorem]] gives $e^{i\theta} = \cos\theta + i\sin\theta$, and replacing $\theta$ by $-\theta$ gives $e^{-i\theta} = \cos\theta - i\sin\theta$. Two equations, two unknowns — the same simultaneous-equation move as before. Add and subtract:

$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \qquad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

Look at what those are. **$\cos$ is the even half of $e^{i\theta}$ and $\sin$ is (up to that $i$) its odd half** — the identical decomposition that produced $\cosh$ and $\sinh$, run on $e^{i\theta}$ instead of $e^{x}$. The two pairs are not cousins or analogies. They are *the same construction fed different input*, which is why every structural fact survives the crossing and why only the $i$'s differ.

### The substitution, derived

Put $\theta = ix$ into those two formulas and use $i \cdot i = -1$ in the exponents:

$$\cos(ix) = \frac{e^{i(ix)} + e^{-i(ix)}}{2} = \frac{e^{-x} + e^{x}}{2} = \cosh x$$

$$\sin(ix) = \frac{e^{i(ix)} - e^{-i(ix)}}{2i} = \frac{e^{-x} - e^{x}}{2i} = \frac{-(e^{x} - e^{-x})}{2i} = \frac{-2\sinh x}{2i} = -\frac{\sinh x}{i} = i\sinh x$$

(the last step uses $\dfrac{1}{i} = -i$, so $-\dfrac{\sinh x}{i} = -(-i)\sinh x = i\sinh x$)

$$\boxed{\ \cos(ix) = \cosh x, \qquad \sin(ix) = i\sinh x\ }$$

So take any trigonometric identity, replace $\theta$ by $ix$ throughout, and it becomes an identity in $\cosh$ and $\sinh$ — except that **every $\sin$ has brought an $i$ with it**. Wherever two sines multiply, those $i$'s meet and give $i^2 = -1$.

Run it on the picture above to see it work: $\cos^2\theta + \sin^2\theta = 1$ becomes $\cosh^2 x + (i\sinh x)^2 = \cosh^2 x - \sinh^2 x = 1$. The flat line at 1 on the right is the flat line at 1 on the left, with one $i^2$ spent.

That is the entire principle, and it is all you actually need:

> **Substituting $\theta \to ix$ turns cosines into $\cosh$ and sines into $i\sinh$, so any term carrying a product of two sines changes sign.**

**Osborn's rule** is that principle sorted into a recipe: *write the identity with every trig function replaced by its hyperbolic counterpart, then reverse the sign of any term containing a product of two sines.* The letters tell you where to look; the principle tells you why:

| Trigonometric | Product of two sines? | Hyperbolic |
|---|---|---|
| $\cos^2\theta + \sin^2\theta \equiv 1$ | yes — $\sin^2$ | $\cosh^2 x - \sinh^2 x \equiv 1$ |
| $\sin 2\theta \equiv 2\sin\theta\cos\theta$ | no — one sine only | $\sinh 2x \equiv 2\sinh x \cosh x$ |
| $\cos 2\theta \equiv \cos^2\theta - \sin^2\theta$ | yes | $\cosh 2x \equiv \cosh^2 x + \sinh^2 x$ |
| $1 + \tan^2\theta \equiv \sec^2\theta$ | yes — $\tan^2$ hides $\sin^2$ | $1 - \tanh^2 x \equiv \operatorname{sech}^2 x$ |

The last row is the one students miss: $\tan^2$ and $\coth^2$ and $\operatorname{cosech}^2$ all contain a hidden product of two sines, because a $\tan$ is a sine over a cosine. **When the mnemonic feels ambiguous, fall back on the principle** — write the trig identity in terms of $\sin$ and $\cos$ only, count the sines in each term, and flip the ones that have two.

## Differentiation — and the missing minus sign

Differentiate the definitions and there is nothing to learn:

$$\frac{d}{dx}\sinh x = \frac{e^x + e^{-x}}{2} = \cosh x, \qquad \frac{d}{dx}\cosh x = \frac{e^x - e^{-x}}{2} = \sinh x$$

$$\frac{d}{dx}\tanh x = \operatorname{sech}^2 x \quad \text{(quotient rule, then } \cosh^2 - \sinh^2 = 1\text{)}$$

**Note what is absent: $\dfrac{d}{dx}\cosh x = +\sinh x$, with no minus sign** — unlike $\dfrac{d}{dx}\cos x = -\sin x$. This is the single most-dropped mark on the topic, and it is worth understanding rather than memorising.

The trig minus sign comes from the $i$. Look at where it can enter here: differentiating $e^{-x}$ produces a minus. In $\cosh$ the two terms are *added*, so that minus turns the sum into a difference — giving $\sinh$. In $\sinh$ the terms are *subtracted*, so the same minus turns the difference into a sum — giving $\cosh$. The operation is symmetric, so it can never produce an overall sign flip. In the circular case the exponentials carry $i$'s, and it is $i^2 = -1$ that breaks the symmetry. **No $i$, no minus.**

The full derivative and integral tables, with per-board formula-sheet status, live in [[Differentiation Rules]] and [[Standard Integrals]].

## The inverse functions and their logarithmic forms

The syllabus asks you to **derive** these, not to quote them, and the derivation is the same trick three times: *set $u = e^y$ and you have a quadratic.*

### $\operatorname{arsinh} x$

Let $y = \operatorname{arsinh} x$, so $x = \sinh y = \dfrac{e^y - e^{-y}}{2}$.

**Step 1** — clear the fraction: $2x = e^y - e^{-y}$.
**Step 2** — substitute $u = e^y$ and multiply through by $u$: $\;2xu = u^2 - 1$, so $u^2 - 2xu - 1 = 0$.
**Step 3** — quadratic formula: $u = \dfrac{2x \pm \sqrt{4x^2+4}}{2} = x \pm \sqrt{x^2+1}$.
**Step 4** — choose the sign, and *say why*: $u = e^y > 0$ always, while $\sqrt{x^2+1} > \lvert x \rvert$, so $x - \sqrt{x^2+1}$ is negative and impossible. Take the $+$.

$$\boxed{\ \operatorname{arsinh} x = \ln\!\left(x + \sqrt{x^2+1}\right), \quad x \in \mathbb{R}\ }$$

### $\operatorname{arcosh} x$

The same four steps from $x = \cosh y$ give $u^2 - 2xu + 1 = 0$ and $u = x \pm \sqrt{x^2 - 1}$ — but this time **both roots are positive** (their product is $1$), so the sign is not decided for you. That is not a defect in the algebra; it is the algebra reporting a real fact: $\cosh$ is even, so $\cosh y = \cosh(-y)$ and every value is hit twice. Restricting to the principal branch $y \geq 0$ forces $u = e^y \geq 1$ and selects the $+$:

$$\boxed{\ \operatorname{arcosh} x = \ln\!\left(x + \sqrt{x^2-1}\right), \quad x \geq 1\ }$$

### $\operatorname{artanh} x$

From $x = \tanh y = \dfrac{e^y - e^{-y}}{e^y + e^{-y}}$, multiply top and bottom by $e^y$ to get $x = \dfrac{u^2-1}{u^2+1}$. Then $x(u^2+1) = u^2 - 1$, so $u^2(1-x) = 1+x$ and $u^2 = \dfrac{1+x}{1-x}$:

$$\boxed{\ \operatorname{artanh} x = \tfrac{1}{2}\ln\!\left(\frac{1+x}{1-x}\right), \quad \lvert x \rvert < 1\ }$$

The domain restriction is not decoration — it is the range of $\tanh$ read backwards, and stating it earns marks.

> [!info] Formula-sheet status — the sheet gives you the destination, not the journey
> **MF19's Further Pure section prints more than students expect**, and knowing exactly what changes how you revise:
>
> **Given.** The three identities $\cosh^2 x - \sinh^2 x \equiv 1$, $\sinh 2x \equiv 2\sinh x\cosh x$, $\cosh 2x \equiv \cosh^2 x + \sinh^2 x$; **all three logarithmic forms with their domains**; the Maclaurin series for $\sinh$, $\cosh$ and $\tanh^{-1}$; and the complete derivative and integral tables — $\sinh \to \cosh$, $\cosh \to \sinh$, $\tanh \to \operatorname{sech}^2$, and all three inverse-hyperbolic derivatives.
>
> **Not given.** The **definitions in terms of $e^x$** — the one thing everything else is built from. Nor the reciprocal functions $\operatorname{sech}$, $\operatorname{cosech}$, $\coth$, nor Osborn's rule, nor anything that would help you *prove* an identity rather than quote one.
>
> That division is the revision plan, and it is sharper than "memorise the list". The syllabus verb for the logarithmic forms is **derive** — so the sheet printing the answer does not excuse you from producing it, and a question saying *show that* wants the $u = e^y$ quadratic worked with the branch justified. The booklet hands you the destination precisely because **the marks are in the journey** — the same bargain [[Proof by Induction]] meets, where the standard summation formulae are printed and the proof is still what earns.
>
> **OxAQA 9660** additionally prints the $e^x$ definitions themselves. **Edexcel IAL** places hyperbolics in **FP3**, with the inverse-hyperbolic integrals on its booklet. Full audits: [[MF19 Reference (9709)]] and [[OxAQA 9660 Reference]].

## Worked examples

### Example 1 — prove an identity from the definitions

*Prove that $\cosh 2x \equiv 2\cosh^2 x - 1$.*

**Tool: Osborn's rule to predict the target.** The trig original is $\cos 2\theta \equiv 2\cos^2\theta - 1$, which contains no product of two sines, so no sign flips — the hyperbolic twin keeps the same shape. Now prove it properly.

**Tool: the definitions, and nothing else.**

$$2\cosh^2 x - 1 = 2\left(\frac{e^x + e^{-x}}{2}\right)^2 - 1 = \frac{e^{2x} + 2 + e^{-2x}}{2} - 1 = \frac{e^{2x} + e^{-2x}}{2} = \cosh 2x \quad \blacksquare$$

The middle step used $e^x e^{-x} = 1$ — the fact doing the work in nearly every proof on this page.

### Example 2 — solve an equation, and lose no roots

*Solve $3\cosh x - \sinh x = 3$.*

**Tool: convert to exponentials** — a hyperbolic equation in one variable is an exponential equation wearing a disguise.

$$3 \cdot \frac{e^x + e^{-x}}{2} - \frac{e^x - e^{-x}}{2} = 3 \;\Longrightarrow\; 3e^x + 3e^{-x} - e^x + e^{-x} = 6 \;\Longrightarrow\; 2e^x + 4e^{-x} = 6$$

**Tool: $u = e^x$ turns it into a quadratic** — the same move as the logarithmic forms.

$$2u^2 - 6u + 4 = 0 \;\Longrightarrow\; u^2 - 3u + 2 = 0 \;\Longrightarrow\; u = 1 \text{ or } u = 2$$

**Tool: reject nothing without checking.** Both roots are positive, so both are legal values of $e^x$ — and *both* give solutions:

$$x = \ln 1 = 0 \qquad \text{or} \qquad x = \ln 2$$

Discarding a root here is the standard way to lose a mark. A negative root would have to go, because $e^x > 0$ — but that is a reason to check, not a habit of throwing one away.

### Example 3 — derive a logarithmic form under exam conditions

*Show that $\operatorname{arcosh} 2 = \ln(2 + \sqrt{3})$.*

**Tool: the definition, not the formula.** Let $y = \operatorname{arcosh} 2$, so $\cosh y = 2$ and $e^y + e^{-y} = 4$. With $u = e^y$: $u^2 - 4u + 1 = 0$, giving $u = 2 \pm \sqrt{3}$.

**Tool: the branch condition.** $\operatorname{arcosh}$ takes the principal value $y \geq 0$, so $u = e^y \geq 1$; since $2 - \sqrt{3} \approx 0.27 < 1$, take $u = 2 + \sqrt{3}$ and $y = \ln(2+\sqrt{3})$. $\blacksquare$

(Worth noticing: $(2+\sqrt3)(2-\sqrt3) = 1$, so the rejected root is the *reciprocal* of the accepted one — which is exactly $e^{-y}$. The second root was never wrong, only the wrong branch.)

## Common misconceptions (teaching notes)

### 1. "The parameter is an angle"

Students carry the circular picture over and try to find "the hyperbolic angle" on the diagram with a protractor.

**Fix:** teach the area interpretation for the **circle** first, where it can be checked against something familiar — a sector of angle $t$ has area $t/2$, so $t = 2 \times$ area even there. Then the hyperbola needs no new idea: the same area statement, on a different conic. The "angle" was always a stand-in for area.

### 2. "$\dfrac{d}{dx}\cosh x = -\sinh x$"

Imported wholesale from $\cos$, and it costs a mark almost every time.

**Fix:** never let them memorise the pair as a table until they have differentiated $\tfrac12(e^x + e^{-x})$ on paper and watched the minus sign turn the sum into a difference. Then the rule is a two-second re-derivation rather than a recall, and the question *where would a minus even come from?* has an answer.

### 3. "Osborn's rule is an arbitrary rule to memorise"

They apply it to a term with one sine, or miss the $\sin^2$ hiding inside a $\tan^2$.

**Fix:** derive it once by substituting $\theta = ix$ into $\cos^2 + \sin^2 = 1$ and watching $i^2$ appear. After that, "flip products of two sines" is obviously a *bookkeeping device for counting $i$'s*, and the $\tan^2$ case is handled by writing $\tan$ as $\sin/\cos$ rather than by remembering a special case.

### 4. "The $\pm$ in $\operatorname{arcosh}$ is a choice you make"

They pick a sign because the answer in the book has one, and cannot say why.

**Fix:** make them notice that the two roots multiply to $1$, so one is $e^y$ and the other is $e^{-y}$ — the $\pm$ is the graph's own two-branch symmetry showing up in the algebra. The restriction $y \geq 0$ is what makes $\operatorname{arcosh}$ a function at all, exactly as restricting $\cos$ to $[0,\pi]$ is what makes $\arccos$ one.

### 5. "A hanging chain is a parabola"

An old and respectable error — see below.

**Fix:** plot both through the same three points and look at the gap. It is not a subtle difference once drawn, and it is a memorable demonstration that a shape that *looks* quadratic need not be.

## Exam Notes

### Cambridge 9231 Further Mathematics — **Further Pure 2, Paper 2**

**§2.1** is a small section with four learning objectives and no hiding places:

- **Definitions of all six** functions in terms of $e^x$ — including $\operatorname{sech}$, $\operatorname{cosech}$ and $\coth$, which candidates routinely neglect because the interesting work happens in the first three.
- **Sketch the graphs.** Marks for intercepts, asymptotes on $\tanh$, and the symmetry.
- **Prove and use identities.** The syllabus names $\cosh^2 x - \sinh^2 x \equiv 1$ and $\sinh 2x \equiv 2\sinh x\cosh x$ explicitly and then says *"and similar results corresponding to the standard trigonometric identities"* — which is Osborn's rule invited by name without being named. "Prove" means from the exponential definitions; quoting Osborn is a check, not a proof.
- **Derive and use the logarithmic forms.** The verb is *derive*, and the forms are **printed on MF19** — which does not make the derivation optional, it makes it the thing being tested. Expect *show that*, with the $u = e^y$ quadratic worked and the sign choice justified.

The topic then feeds two further sections of the same paper: **§2.3** wants the derivatives of the inverse hyperbolic functions, and **§2.4** wants the integrals $\int \frac{dx}{\sqrt{x^2+a^2}}$ and $\int \frac{dx}{\sqrt{x^2-a^2}}$ by hyperbolic substitution — which is where this material actually earns its keep in the exam, and which [[Standard Integrals]] tabulates.

### OxAQA 9660

Examined, and supported one step further than Cambridge: 9660's booklet prints the **$e^x$ definitions** as well as the identities, logarithmic forms and derivative table. Since the definitions are the root of every proof on this page, that is the difference between the two boards worth knowing — a 9660 candidate can look up the starting point of a derivation, a 9231 candidate must supply it. [[OxAQA 9660 Reference]] holds the audit.

### Edexcel IAL and other A-Level Further specifications

Hyperbolic functions sit in **FP3** on Edexcel IAL, with the inverse-hyperbolic integrals on the booklet; AQA and OCR Further Mathematics carry equivalent content in their own further-pure papers. The mathematics is identical across all of them — only the formula-sheet support and the paper labels differ.

### Where this is *not* examined

**Not on Cambridge 9709** at any level — hyperbolic functions appear nowhere in the single-maths A-Level, which is why MF19 has no room for them. **Not on IB Analysis and Approaches**, HL included. **Not on AP Calculus AB or BC** — a notable absence, since BC covers integration techniques that would use them. In short: this is *Further* Mathematics content and nothing else, so a student meeting $\cosh$ in a physics or engineering context is meeting it ahead of their maths syllabus.

> [!info] Beyond syllabus — the hanging chain, and Galileo's mistake
> Hold a chain by its two ends and let it hang. The curve is a **catenary** (from Latin *catena*, chain), and its equation is $y = a\cosh(x/a)$. Galileo asserted it was a parabola, which is wrong but not foolish — over a short span with a shallow sag the two curves are very close, and $\cosh t = 1 + \tfrac{t^2}{2} + \tfrac{t^4}{24} + \cdots$ shows exactly why: **the catenary's series begins with a parabola**, and only the fourth-order term gives it away. The true curve was found in 1691, when Jacob Bernoulli posed the problem publicly and Johann Bernoulli, Huygens and Leibniz all solved it — a scene from the family in [[Stories/The Bernoulli Family]].
>
> The reason a chain does this is worth one sentence: every element hangs in equilibrium, so the horizontal tension is constant along the chain and the vertical tension at a point equals the weight of chain below it — the slope is therefore proportional to the *arc length* so far, and the function whose slope tracks its own arc length is $\cosh$. Invert a catenary and it stands in pure compression, which is why arches are built from it.

> [!info] Beyond syllabus — where $\tanh$ turns up
> **Falling with drag.** A body falling under gravity against a resistance proportional to $v^2$ obeys $m\frac{dv}{dt} = mg - kv^2$, and the solution is $v = v_T \tanh\!\left(\frac{g t}{v_T}\right)$ with $v_T = \sqrt{mg/k}$ the terminal velocity. The S-curve *is* the speed graph of a skydiver: near-linear at first, then flattening onto the asymptote it never quite reaches. The [[Differential Equations|separable-equation]] machinery handles it directly.
>
> **Adding velocities in relativity.** Velocities do not add by $u + v$ near light speed — but *rapidities* do. Define $\phi$ by $v = c\tanh\phi$ and the relativistic composition law becomes plain addition, $\phi_{\text{total}} = \phi_1 + \phi_2$. Since $\tanh$ never reaches $1$, no sum of rapidities ever reaches $c$: the speed limit is a property of the function's asymptote.
>
> **Squashing in neural networks.** $\tanh$ maps all of $\mathbb{R}$ into $(-1, 1)$ smoothly and symmetrically, which is exactly what is wanted from an activation function, and its derivative $\operatorname{sech}^2 x = 1 - \tanh^2 x$ is cheap to compute from the value you already have — the same trick that makes the logistic function convenient.

## Connections

- **Parent:** [[Exponential Function]] — these *are* its even and odd halves, and every proof on this page reduces to $e^x e^{-x} = 1$.
- **Mirror:** [[Trigonometric Identities]] — every identity here is one of those with the sines counted; [[Euler's Formula and De Moivre's Theorem]] supplies the $\theta \to ix$ substitution that explains the correspondence.
- **Inverses:** [[Logarithms]] — not a coincidence but a consequence, since both measure area under the same hyperbola; [[Inverse Function]] for the branch restriction that makes $\operatorname{arcosh}$ a function.
- **Where it is used:** [[Standard Integrals]] — the hyperbolic substitutions for $\frac{1}{\sqrt{x^2 \pm a^2}}$, which is what Further Pure 2 actually examines; [[Differentiation Rules]] — the derivative table with per-board formula-sheet status.
- **History:** [[Stories/The Hidden Number]] — Saint-Vincent's hyperbolic area, the same measurement seen at $45°$; [[Stories/The Bernoulli Family]] — the 1691 catenary problem.
- **For 9231 students:** [[MF19 Reference (9231)]] — the identities, the three logarithmic forms and the whole derivative/integral table are printed; the $e^x$ definitions are not, and *derive* is still the syllabus's verb.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\sinh x$ | `\sinh x` | built in; always space before the argument |
| $\cosh x$ | `\cosh x` | built in |
| $\tanh x$ | `\tanh x` | built in |
| $\operatorname{sech} x$ | `\operatorname{sech} x` | **not** built in — `\sech` is undefined |
| $\operatorname{cosech} x$ | `\operatorname{cosech} x` | UK spelling; US texts write $\operatorname{csch}$ |
| $\coth x$ | `\coth x` | built in |
| $\operatorname{arsinh} x$ | `\operatorname{arsinh} x` | **ar**, not **arc** — the parameter is an area |
| $\sinh^{-1} x$ | `\sinh^{-1} x` | the notation Cambridge papers use |
| $\lvert x \rvert < 1$ | `\lvert x \rvert < 1` | use `\lvert…\rvert` inside tables, never a bare `\|` |

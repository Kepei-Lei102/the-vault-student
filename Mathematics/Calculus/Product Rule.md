---
chinese: 乘法法则 (chéngfǎ fǎzé)
prerequisites:
  - "[[Differentiation]]"
  - "[[Power Rule]]"
  - "[[Limit]]"
leads_to:
  - "[[Quotient Rule]]"
  - "[[Integration by Parts]]"
  - "[[Error Propagation]]"
  - "[[Differentiation Rules]]"
  - "[[Forward Reading and Problem Discovery]]"
teach_together:
  - "[[Chain Rule]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/0606-14-4
  - syllabus/9709-2-4
  - syllabus/9709-3-4
  - type/theorem
  - type/proof
  - notation/derivative
  - misconception/derivative-of-product-is-product-of-derivatives
---

# Product Rule 乘法法则

## The Rule

If $u$ and $v$ are differentiable functions of $x$, then

$$\boxed{\dfrac{d}{dx}\bigl(uv\bigr) = u\dfrac{dv}{dx} + v\dfrac{du}{dx}}$$

Using prime notation: $(uv)' = u'v + uv'$.

Read it as: **"derivative of the first times the second, plus the first times the derivative of the second."** It is symmetric in $u$ and $v$ — you can start from either side.

A useful paraphrase: *when a product changes, each factor contributes its own change while the other factor is held fixed, and the two contributions are added.*

## The Quotient Rule (Corollary)

$$\dfrac{d}{dx}\left(\dfrac{u}{v}\right) = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$$

Prime-notation: $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$, with $v \neq 0$.

This is **not a separate axiom** — we derive it from the Product Rule below. But you should memorise it for exams; the derivation is the backup, not the routine method.

> [!warning] Quotient Rule sign order
> The numerator is $u'v - uv'$, **not** $uv' - u'v$. Many students lose marks by flipping the sign. Mnemonic: *"low d-high minus high d-low, square the low and away we go"* — the denominator squared, numerator with the "low" ($v$) first.

## 中文锚点 (Chinese Anchor)

乘法法则：**两个函数相乘的导数 = 第一个的导数 × 第二个 + 第一个 × 第二个的导数**。

$$\bigl(uv\bigr)' = u'v + uv'$$

关键直觉：当 $u$ 和 $v$ 同时变化一点点时，乘积 $uv$ 的变化由两部分组成 —— $u$ 变化带来的 $v \cdot du$，加上 $v$ 变化带来的 $u \cdot dv$。还有一块二阶小项 $du \cdot dv$，但它比一阶项小得多，取极限时就消失了。下面的矩形图让这件事一目了然。

商法则：$\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$ —— 注意分子的顺序和减号，别写反。

## Why It Works — First Principles Proof

This is a proof every strong student should see at least once. It uses the limit definition of the derivative from [[Differentiation]] plus a single clever step: the **add-subtract trick**.

### Step 1: Write the difference quotient

$$\dfrac{d}{dx}\bigl[u(x)v(x)\bigr] = \lim_{h \to 0} \dfrac{u(x+h)\,v(x+h) - u(x)\,v(x)}{h}$$

The numerator is a *difference of products*. We cannot split it directly, because $u$ and $v$ both change at once.

### Step 2: The add–subtract trick

Insert $u(x+h)\,v(x)$ then subtract it — net change zero:

$$u(x+h)v(x+h) - u(x)v(x) = \underbrace{u(x+h)v(x+h) - u(x+h)v(x)}_{\text{only } v \text{ changed}} + \underbrace{u(x+h)v(x) - u(x)v(x)}_{\text{only } u \text{ changed}}$$

Now each bracket factors cleanly. The first has a common factor of $u(x+h)$; the second has a common factor of $v(x)$:

$$= u(x+h)\bigl[v(x+h) - v(x)\bigr] + v(x)\bigl[u(x+h) - u(x)\bigr]$$

### Step 3: Divide by $h$

$$\dfrac{u(x+h)v(x+h) - u(x)v(x)}{h} = u(x+h)\cdot\dfrac{v(x+h) - v(x)}{h} + v(x)\cdot\dfrac{u(x+h) - u(x)}{h}$$

### Step 4: Take the limit $h \to 0$

Because $u$ is differentiable (hence continuous), $u(x+h) \to u(x)$. Each difference quotient becomes the corresponding derivative:

$$\lim_{h \to 0} u(x+h) \cdot \lim_{h \to 0}\dfrac{v(x+h) - v(x)}{h} = u(x) \cdot v'(x)$$

$$\lim_{h \to 0} v(x) \cdot \lim_{h \to 0}\dfrac{u(x+h) - u(x)}{h} = v(x) \cdot u'(x)$$

Putting it together:

$$\boxed{\dfrac{d}{dx}\bigl(uv\bigr) = u\,v' + v\,u'} \qquad \blacksquare$$

> [!tip] The **注意到** move, unrolled
> In a Chinese textbook, Step 2 above would be introduced with **"注意到 …"** *(notice that …)* — and every student has thought **"你的注意力真的惊人"** *(your attention is astonishing)* in response. The sarcasm is fair: the inserted term $u(x+h)v(x)$ really does look like it was pulled out of a hat.
>
> But the move isn't one act of genius. It's **five small attentions firing in parallel**:
>
> 1. **Shape of the obstacle** — two factors change at once; this is a multivariable problem pretending to be single-variable.
> 2. **Technique for that shape** — sequential perturbation: move one factor, then the other.
> 3. **A picture that helps** — the Leibniz rectangle below: the right strip and the top strip come from nudging each side in turn.
> 4. **Remembered failure mode** — direct expansion leaves a cross-term; that cross-term is the rectangle's vanishing corner piece.
> 5. **What the answer should look like** — two single-variable differences, each multiplied by the *other* factor.
>
> Run those five in parallel, combine their outputs, and what rolls out is exactly: **"insert the intermediate rectangle $u(x+h)v(x)$."** That single inserted term is what 注意到 compresses.
>
> The 注意力惊人 meme is substantively correct — it points at real missing information, the *chain* of attention that led to the move. Unrolled, the move is not astonishing at all. It's **ordinary attention routed through the right heads** — and once you know the heads, the same trick will come to you next time without prompting. That's the transferable method; the inserted term is just its output.

## Geometric Picture — the Leibniz Rectangle

The same idea, visually. Imagine a rectangle with width $f$ and height $g$, so its area is $fg$. Now nudge $f$ by $df$ and $g$ by $dg$. The new area is $(f+df)(g+dg)$. The **increase** $d(fg)$ decomposes into three pieces:

![[product-rule-rectangle.svg|640]]

- **Right strip** (width $df$, height $g$): area $g\,df$.
- **Top strip** (width $f$, height $dg$): area $f\,dg$.
- **Corner square** (width $df$, height $dg$): area $df\,dg$ — a **second-order** term.

$$d(fg) = f\,dg + g\,df + df\,dg$$

When $df$ and $dg$ both shrink to zero, $df \cdot dg$ shrinks *quadratically* — much faster than the strips, which only shrink linearly. In the limit, the corner vanishes and we are left with

$$d(fg) = f\,dg + g\,df \qquad\Longleftrightarrow\qquad \dfrac{d(fg)}{dx} = f\dfrac{dg}{dx} + g\dfrac{df}{dx}.$$

> [!tip] Memorise the rectangle
> This picture *is* the product rule. When a student forgets the formula, reconstructing the rectangle takes five seconds and never misremembers.

## Deriving the Quotient Rule from the Product Rule

Many textbooks prove the quotient rule as its own separate theorem with a nasty limit. It's much cleaner to get it from the product rule, once we know the derivative of $1/v$.

### Lemma: $\dfrac{d}{dx}\left(\dfrac{1}{v}\right) = -\dfrac{v'}{v^2}$ (for $v \neq 0$)

Start from $v \cdot \dfrac{1}{v} = 1$. Differentiate both sides using the product rule:

$$v'\cdot \dfrac{1}{v} + v \cdot \dfrac{d}{dx}\left(\dfrac{1}{v}\right) = 0$$

Solve for the unknown derivative:

$$\dfrac{d}{dx}\left(\dfrac{1}{v}\right) = -\dfrac{v'}{v \cdot v} = -\dfrac{v'}{v^2}$$

### Now apply the Product Rule to $u \cdot \dfrac{1}{v}$

$$\dfrac{d}{dx}\left(\dfrac{u}{v}\right) = \dfrac{d}{dx}\left(u \cdot \dfrac{1}{v}\right) = u' \cdot \dfrac{1}{v} + u \cdot \left(-\dfrac{v'}{v^2}\right) = \dfrac{u'}{v} - \dfrac{uv'}{v^2}$$

Put over the common denominator $v^2$:

$$\boxed{\dfrac{d}{dx}\left(\dfrac{u}{v}\right) = \dfrac{u'v - uv'}{v^2}} \qquad \blacksquare$$

The minus sign and the $v^2$ appear naturally from the lemma — you don't have to memorise *why*, you can re-derive it in four lines.

> [!tip] Another **注意到** — but a different head is firing
> The slick step above was "start from $v \cdot \dfrac{1}{v} = 1$." Where did *that* come from? It's another unrolled attention chain — but this time the key head is different from the one in the add-subtract trick.
>
> 1. **Shape of the obstacle** — I want $(1/v)'$ but I don't know how to differentiate $1/v$ directly.
> 2. **Key move** — don't attack the function; **attack the equation that *defines* the function.**
> 3. **Candidate equations** — $1/v$ is defined by $v \cdot (1/v) = 1$. That equation is tractable: the left side is just a product.
> 4. **What the equation gives me** — differentiating both sides produces a linear equation in the unknown derivative, which I can solve.
>
> The transferable principle, worth memorising: *when the derivative you want is hard, differentiate the equation that defines it.* This pattern shows up all over calculus — it's how we'll derive $(\ln x)'$, $(\sqrt x)'$, and $(\sin^{-1}x)'$ in the upcoming [[Differentiation Rules]] card. That whole family of "slick" derivatives is one head firing: *attend to the defining equation, not to the function itself.*
>
> (Footnote for later: that principle is really **implicit differentiation**, which is itself **chain rule applied to both sides of an equation** — see [[Chain Rule]].)

## Worked Examples

### Example 1 — The bread-and-butter case: $y = x^2 \sin x$

Let $u = x^2$, $v = \sin x$. Then $u' = 2x$, $v' = \cos x$.

$$\dfrac{dy}{dx} = u'v + uv' = 2x \sin x + x^2 \cos x$$

### Example 2 — Product of three factors: $y = x\, e^x \sin x$

For three factors, differentiate one at a time, holding the others constant:

$$\dfrac{d}{dx}(fgh) = f'gh + fg'h + fgh'$$

This is easy to remember — each factor gets its turn to be differentiated, the others tag along.

$$\dfrac{dy}{dx} = (1)e^x\sin x + x(e^x)\sin x + x\, e^x(\cos x) = e^x\bigl[(1+x)\sin x + x\cos x\bigr]$$

> [!tip] Derive this from the two-factor rule
> Group $x e^x$ as one factor and $\sin x$ as the other:
>
> $(x e^x \sin x)' = (x e^x)' \sin x + (x e^x)(\sin x)' = (e^x + x e^x)\sin x + x e^x \cos x$
>
> which simplifies to the same answer. The three-factor pattern is just product rule applied twice.

### Example 3 — Quotient Rule: $y = \dfrac{x^2 + 1}{x - 3}$

Let $u = x^2 + 1$, $v = x - 3$. Then $u' = 2x$, $v' = 1$.

$$\dfrac{dy}{dx} = \dfrac{u'v - uv'}{v^2} = \dfrac{2x(x-3) - (x^2+1)(1)}{(x-3)^2} = \dfrac{2x^2 - 6x - x^2 - 1}{(x-3)^2} = \dfrac{x^2 - 6x - 1}{(x-3)^2}$$

### Example 4 — Quotient where simplification is tempting: $y = \dfrac{\sin x}{x}$

$$\dfrac{dy}{dx} = \dfrac{(\cos x)(x) - (\sin x)(1)}{x^2} = \dfrac{x\cos x - \sin x}{x^2}$$

> [!warning] Don't split the quotient first
> Beginners try to "simplify" $\dfrac{\sin x}{x}$ before differentiating. There is nothing to simplify — you can't cancel $x$ into $\sin x$. Apply the quotient rule directly.

### Example 5 — Double tangent: $y = (x^2 + 1)\ln x$

Let $u = x^2 + 1$, $v = \ln x$. Then $u' = 2x$, $v' = \dfrac{1}{x}$.

$$\dfrac{dy}{dx} = 2x\ln x + (x^2 + 1)\cdot\dfrac{1}{x} = 2x\ln x + x + \dfrac{1}{x}$$

A typical 0606 / 9709 P2 answer — keep the $\ln$ term unexpanded, combine the algebraic pieces.

## Common Misconceptions

### 1. The "fatal simplification": $(uv)' \neq u'v'$

The single most common error: students write $\dfrac{d}{dx}(x^2 \sin x) = 2x\cos x$. This is wrong. **The derivative of a product is not the product of the derivatives.**

**Fix:** Demonstrate with a clean counterexample. Take $u = v = x$, so $uv = x^2$. The correct answer is $(x^2)' = 2x$. The "product-of-derivatives" shortcut would give $u'v' = 1 \cdot 1 = 1$. Different by a factor of $2x$.

### 2. Forgetting to apply the product rule at all

Students see $y = x^2 \sin x$ and differentiate as if $\sin x$ were a constant: $\dfrac{dy}{dx} = 2x \sin x$. This is **half** of the correct answer — they forgot the $x^2 \cos x$ piece.

**Fix:** Circle the factors in different colours. Ask: "which factor is the variable $x^2$? which is the variable $\sin x$? both are *functions of $x$*, so both get differentiated."

### 3. Quotient rule sign flip

$(u/v)' = \dfrac{uv' - u'v}{v^2}$. Wrong sign order.

**Fix:** The mnemonic *"low d-high minus high d-low"* puts the denominator's derivative ($v$ is "low") second — so the $v\,du$ term comes first, the $u\,dv$ term comes second with a minus sign.

### 4. Forgetting to square the denominator in the quotient rule

Students write $\dfrac{u'v - uv'}{v}$.

**Fix:** Return to the derivation — the $v^2$ comes from the $\dfrac{1}{v}$ lemma combined with the common denominator.

### 5. Over-applying the product rule to constants

$\dfrac{d}{dx}(5x^3) \neq 0 \cdot x^3 + 5 \cdot 3x^2$ — technically correct, but unnecessarily ugly. For a **constant times a function**, just use linearity: $(5x^3)' = 15x^2$. Save the product rule for two genuinely variable factors.

## Exam Notes

### Cambridge 0606

- **§14.4:** differentiate products and quotients of functions.
- Typical candidates: $x^n \cdot e^x$, $x^n \cdot \ln x$, $\sin x \cdot \cos x$, rational functions.
- You must write out the rule (show $u$, $v$, $u'$, $v'$ explicitly on the working line) — method marks are awarded for setup, not just the final answer.
- Often combined with [[Chain Rule]] in a single question: differentiate $x^2 \sin(3x)$ requires product *and* chain.

### Cambridge A-Level (9709)

- **Paper 2 §2.4** and **Paper 3 §3.4:** chain, product, quotient rules are all listed together — expect a mixed problem.
- Examiners frequently ask for the derivative at a specific point, or to solve $dy/dx = 0$ — so simplify before solving, often by factoring out the largest common term.

### IB AA HL / AP Calculus BC

- Same rule, standard notation.
- In IB AA HL, product rule is a base ingredient for higher-order derivative applications (optimisation, kinematics, related rates).
- AP Calculus BC: product and quotient rules are assumed *and* tested; knowing the first-principles proof is not required but the add-subtract trick generalises to vector-valued derivatives later.

### Beyond syllabus — the Leibniz rule for $n$th derivatives

If you ever need the $n$th derivative of a product:

$$(fg)^{(n)} = \sum_{k=0}^{n} \binom{n}{k}\, f^{(n-k)}\, g^{(k)}$$

This is the **[[Binomial Theorem]]** structure again, not a coincidence: the product rule iterated $n$ times produces the same combinatorial count as picking $k$ of $n$ brackets to "contribute a derivative of $g$." You will see this in IB AA HL toolkit questions and in university complex analysis.

### University — higher dimensions

In multivariable calculus the product rule generalises to the **Leibniz rule for the gradient**:

$$\nabla(uv) = u\nabla v + v\nabla u$$

and further to **vector identities** like $\nabla \cdot (\phi \mathbf{F}) = \phi\,\nabla\cdot\mathbf{F} + \nabla\phi \cdot \mathbf{F}$, which underpin the divergence theorem and Green's identities. The pattern is always the same: *each factor gets its turn to be differentiated, the other tags along.*

> [!tip] Physics bridge — why percentage errors *add* for multiplication
> The Physics rule "for products and quotients, percentage errors add" is one line of product-rule algebra. Start with $z = xy$. Differentiate (product rule):
> $$dz = y\,dx + x\,dy.$$
> Divide both sides by $z = xy$:
> $$\dfrac{dz}{z} = \dfrac{y\,dx}{xy} + \dfrac{x\,dy}{xy} = \dfrac{dx}{x} + \dfrac{dy}{y}.$$
> Read $\dfrac{dz}{z}$ as the *fractional* (percentage) change in $z$, and the same for $x$ and $y$. So
> $$\dfrac{\Delta z}{z} \approx \dfrac{\Delta x}{x} + \dfrac{\Delta y}{y}\quad\text{(worst-case bound: take absolute values).}$$
> The rectangle picture above is the geometric version: the right strip is the "$y$ contribution" and the top strip is the "$x$ contribution", and dividing area increment by total area gives a *fractional* increment that is the sum of the two fractional side-increments. The corner $df\,dg$ that vanishes in the limit is the second-order error term — the same one Physics ignores when it writes $\Delta(xy) \approx y\Delta x + x\Delta y$. See [[Error Propagation]] (and [[Chain Rule]] for the $\ln$-trick that handles powers, quotients, and general $f(x)$).

## Connections

- **Parent:** [[Differentiation]] — the product rule is a theorem *about* differentiation, proved from first principles.
- **Sibling:** [[Chain Rule]] — rules for combining functions; product rule handles multiplication, chain rule handles composition.
- **Corollary:** the quotient rule — derived inside this note from Product Rule + the $1/v$ lemma (see the "Deriving the Quotient Rule from the Product Rule" section above).
- **Reverse:** [[Integration by Parts]] — integration analogue; the product rule integrated both sides gives IBP.
- **Ingredient:** [[Power Rule]], [[Differentiation Rules]] — standard derivatives of the factors.
- **Application:** [[Stationary Points]] — solving $(uv)' = 0$ usually needs product rule first.
- **Application:** [[Tangents and Normals]] — tangent slope of a product-form curve.
- **Application — Physics bridge:** [[Error Propagation]] — the percentage-error rule for products and quotients is product rule divided through by $z$.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $(uv)' = u'v + uv'$ | `(uv)' = u'v + uv'` | Prime-notation product rule |
| $\dfrac{d}{dx}(uv) = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ | `\dfrac{d}{dx}(uv) = u\dfrac{dv}{dx} + v\dfrac{du}{dx}` | Leibniz-notation product rule |
| $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$ | `\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}` | Quotient rule |
| $(fgh)' = f'gh + fg'h + fgh'$ | `(fgh)' = f'gh + fg'h + fgh'` | Three-factor product rule |
| $\binom{n}{k}$ | `\binom{n}{k}` | Binomial coefficient (Leibniz $n$th-derivative rule) |
| $\nabla$ | `\nabla` | Gradient (multivariable extension) |
| $\blacksquare$ | `\blacksquare` | End-of-proof marker |

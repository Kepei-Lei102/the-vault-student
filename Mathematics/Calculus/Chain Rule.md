---
chinese: 链式法则 (liànshì fǎzé)
prerequisites:
  - "[[Differentiation]]"
  - "[[Power Rule]]"
  - "[[Composite Function]]"
  - "[[Limit]]"
leads_to:
  - "[[Integration by Substitution]]"
  - "[[Quotient Rule]]"
  - "[[Implicit Differentiation]]"
  - "[[Parametric Differentiation]]"
  - "[[Differentiation Rules]]"
  - "[[Error Propagation]]"
  - "[[Connected Rates of Change]]"
  - "[[Forward Reading and Problem Discovery]]"
  - "[[Integration]]"
  - "[[Optimisation]]"
  - "[[Standard Integrals]]"
teach_together:
  - "[[Product Rule]]"
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
  - syllabus/0606-14-3
  - syllabus/9709-1-7
  - syllabus/9709-2-4
  - syllabus/9709-3-4
  - type/theorem
  - type/proof
  - notation/derivative
  - notation/leibniz
  - misconception/chain-rule-forgotten-on-inside
  - misconception/dx-du-cancellation
---

# Chain Rule 链式法则

## The Rule

If $y = f(u)$ and $u = g(x)$ are both differentiable, then $y = f(g(x))$ is differentiable and

$$\boxed{\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}}$$

In prime notation: $\bigl(f(g(x))\bigr)' = f'(g(x))\cdot g'(x)$.

Read it as: **"derivative of the outside (with the inside left alone) times derivative of the inside."** The Leibniz form looks like a fraction cancellation — that's not what's happening, but the notation was designed to *suggest* it, and the suggestion is correct in spirit.

A useful paraphrase: *when one quantity drives another that drives a third, the overall rate is the product of the local rates.*

## 中文锚点 (Chinese Anchor)

**链式法则** (literally "chain-style rule") differentiates a composite function by **chaining** the derivatives of the inner and outer pieces.

The Chinese curriculum often introduces the rule via the substitution form: 设 $u = g(x)$，则 $y = f(u)$，所以 $\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$. The same Leibniz form lands in English textbooks but the prime-notation form $f'(g(x))\,g'(x)$ is the one that shows up in Cambridge mark schemes — students must be fluent in both.

The English mistake to watch for: students who learn 链式法则 in Chinese sometimes write the answer as $f'(g(x))$ and forget the trailing $\cdot g'(x)$. The *chain* part of the name is exactly the multiplication that gets dropped. Drilling this with bilingual examples fixes it fast.

## Composition Recap (Bridge)

Before the rule, recognise the **composite**. If $y = (2x+1)^5$, the *outside* is "raise to the 5th power" and the *inside* is $2x+1$. If $y = \sin(x^2)$, outside is sine, inside is $x^2$. If $y = e^{\sqrt{x}}$, outside is exponential, middle is square root, inside is $x$ — yes, chains can stack.

| Composite | Outside $f$ | Inside $g$ |
|---|---|---|
| $(2x+1)^5$ | $f(u) = u^5$ | $g(x) = 2x+1$ |
| $\sin(x^2)$ | $f(u) = \sin u$ | $g(x) = x^2$ |
| $\ln(\cos x)$ | $f(u) = \ln u$ | $g(x) = \cos x$ |
| $e^{\sqrt{x}}$ | $f(u) = e^u$ | $g(x) = \sqrt{x}$ |

The rule says: differentiate the outside *as if the inside were a single variable*, then multiply by the derivative of the inside.

## Intuition — Rates Compose

Think of $x \to u \to y$ as a two-stage gearbox. If $u$ changes 3 times as fast as $x$, and $y$ changes 4 times as fast as $u$, how fast does $y$ change per unit of $x$? Twelve times — $3 \times 4$. That's the chain rule.

![[chain-rule-rates-compose.svg|640]]

Nudge $x$ by $dx$. The first stage propagates the nudge to $u$, which moves by $du = \dfrac{du}{dx} \cdot dx$. The second stage propagates that to $y$, which moves by $dy = \dfrac{dy}{du} \cdot du = \dfrac{dy}{du}\cdot\dfrac{du}{dx}\cdot dx$. Read off the overall rate:

$$\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}.$$

This is why the Leibniz notation is designed the way it is. The "$du$ cancels with $du$" reading isn't rigorous fraction algebra — $\dfrac{dy}{du}$ is a single symbol, not a fraction — but the notation was built so that the *correct* answer is the answer fraction-cancellation would give. That is by design, and Leibniz is rightly admired for it.

## Why It Works — First Principles Proof

Let $y = f(g(x))$. By the definition of derivative,

$$\dfrac{dy}{dx} = \lim_{h \to 0}\dfrac{f(g(x+h)) - f(g(x))}{h}.$$

The numerator wants to become $f'(g(x))$ — but $f'$ wants its argument to step from $g(x)$ to something near $g(x)$ over a *step in $g$*, not a step in $x$. The denominator is $h$, which is the wrong currency.

**Step 1 — Multiply and divide by $g(x+h) - g(x)$.** This is the move.

$$\dfrac{f(g(x+h)) - f(g(x))}{h} = \underbrace{\dfrac{f(g(x+h)) - f(g(x))}{g(x+h) - g(x)}}_{\text{outer's quotient}} \cdot \underbrace{\dfrac{g(x+h) - g(x)}{h}}_{\text{inner's quotient}}$$

**Step 2 — Take the limit on each factor.**

- *Inner factor:* $\dfrac{g(x+h) - g(x)}{h} \to g'(x)$ as $h \to 0$, by the definition of $g'(x)$.
- *Outer factor:* let $k = g(x+h) - g(x)$. As $h \to 0$, $k \to 0$ (because $g$ is continuous, which differentiable functions automatically are). The outer quotient becomes
  $$\dfrac{f(g(x) + k) - f(g(x))}{k} \to f'(g(x)).$$

**Step 3 — Multiply.**

$$\dfrac{dy}{dx} = f'(g(x)) \cdot g'(x). \qquad \blacksquare$$

> [!info] Beyond syllabus — the case when $g(x+h) = g(x)$
> The multiply-and-divide step requires $g(x+h) - g(x) \neq 0$. For a function like $g(x) =$ constant near $x$, that fails and the proof above doesn't go through verbatim. The fix is **Carathéodory's formulation** — write $f(z) - f(g(x)) = \varphi(z)(z - g(x))$ with $\varphi$ continuous at $g(x)$ and $\varphi(g(x)) = f'(g(x))$ — which avoids the division entirely. The conclusion is the same; the technicality is hidden. Cambridge does not test this.

> [!tip] The **注意到** move, unrolled
> Step 1 above is another classic *"注意到"* moment — and the meme response *"你的注意力真的惊人"* fits again. The multiply-and-divide trick really does look pulled from a hat. But, like the Product Rule's add-subtract trick, this is **ordinary attention routed through the right heads** — the same family, with one head retuned.
>
> 1. **Shape of the obstacle** — the difference quotient has $h$ in the denominator, but the outer derivative $f'$ wants the denominator to be a *step in $g$*. Currency mismatch.
> 2. **Technique for that shape** — convert one currency into another by inserting a unit conversion factor. Here that factor is $\dfrac{g(x+h) - g(x)}{g(x+h) - g(x)} = 1$.
> 3. **What the conversion does** — splits the single ugly quotient into two clean ones, each in its native currency: outer-quotient (units of $f$ per unit of $g$) times inner-quotient (units of $g$ per unit of $x$).
> 4. **What the answer should look like** — units. We want $dy/dx$, which is "$y$ per $x$". The rate-composition picture says that = ($y$ per $u$) × ($u$ per $x$). The proof must produce a product, not a sum.
> 5. **Remembered shortcut** — Leibniz wrote it as $\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$ in 1684, *before* there was a rigorous proof. The notation suggested the answer; the proof had to chase the notation. (See the historical note below.)
>
> Run the five heads, and the move "multiply and divide by $g(x+h)-g(x)$" is forced — it's the only insertion that gives both factors a meaningful limit. Same family of attention as the Product Rule's add-subtract trick: **make the difference quotient have the right denominator**. Once you see it, it stops being magical. It's the chain-rule head firing.

> [!info] Historical note — Leibniz, Lagrange, Cauchy
> The chain rule has the strangest history of the differentiation rules. **Leibniz** built it into his 1684 notation from day one — the symbols $\tfrac{dy}{dx}, \tfrac{dy}{du}, \tfrac{du}{dx}$ were chosen *so that* the rule would look like fraction cancellation. The rule was therefore "obvious from the notation" for over a century. **Lagrange** (~1797) gave it its modern prime-notation statement $f'(g(x))\,g'(x)$, separating the rule from the suggestive symbols. **Cauchy** (early 1800s) gave the rigorous limit proof — essentially the multiply-and-divide trick above.
>
> So in a real sense, **chain rule predates product rule** as a *named* rule (Leibniz 1684), even though the rigorous proofs of both came in the 19th century. When a student asks "how did anyone notice the multiply-and-divide trick?" the honest answer is: they didn't have to *notice* it — they had Leibniz's notation telling them what the answer should be, and then they reverse-engineered a proof that produced it. That's a perfectly respectable way to do mathematics.

## Worked Examples

### Example 1 — Power of a linear: $y = (2x+1)^5$

Outside $f(u) = u^5$, inside $u = 2x+1$. Then $f'(u) = 5u^4$, $u' = 2$.

$$\dfrac{dy}{dx} = 5(2x+1)^4 \cdot 2 = 10(2x+1)^4$$

> [!tip] Why expansion is a trap
> You *could* expand $(2x+1)^5$ via the binomial theorem and differentiate term by term. That gives the same answer after 30 lines of algebra. The chain rule does it in one. Always look for a composite first.

### Example 2 — Trig of a polynomial: $y = \sin(x^2)$

Outside $\sin u$, inside $x^2$. Derivatives $\cos u$ and $2x$.

$$\dfrac{dy}{dx} = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

The $\cos$ keeps the inside $x^2$ — students who write $2x\cos x$ have **forgotten the inside is unchanged in the outer derivative**. The chain rule does not differentiate the inside *inside* $\cos$.

### Example 3 — Chain inside chain: $y = e^{\sqrt{x}}$

Two-stage chain. Set $u = \sqrt{x}$, so $y = e^u$. Then $u = x^{1/2}$, so $\dfrac{du}{dx} = \tfrac{1}{2}x^{-1/2} = \dfrac{1}{2\sqrt{x}}$.

$$\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx} = e^{\sqrt{x}} \cdot \dfrac{1}{2\sqrt{x}} = \dfrac{e^{\sqrt{x}}}{2\sqrt{x}}$$

For three-stage chains (e.g. $\sin(\ln(\cos x))$), apply the rule once per stage — outer first, then keep peeling.

### Example 4 — The slick derivative: $\dfrac{d}{dx}(\sqrt{x})$

We earned this one in the Product Rule card by attacking the defining equation. Here it is again via the chain rule. Let $y = \sqrt{x}$, so $y^2 = x$. Differentiate both sides with respect to $x$, using the chain rule on the left:

$$2y\cdot\dfrac{dy}{dx} = 1 \quad\Longrightarrow\quad \dfrac{dy}{dx} = \dfrac{1}{2y} = \dfrac{1}{2\sqrt{x}}$$

This is **implicit differentiation**: chain rule applied to both sides of the equation that *defines* $y$. The "attack the defining equation" head from the Product Rule card is just chain rule wearing a different hat — see [[Implicit Differentiation]].

### Example 5 — Where Power Rule and Chain Rule meet

$\dfrac{d}{dx}\bigl((3x^2 - 7)^{10}\bigr) = 10(3x^2 - 7)^9 \cdot 6x = 60x(3x^2 - 7)^9$.

The "general power rule" some textbooks state — $\bigl(g(x)^n\bigr)' = n\,g(x)^{n-1}\,g'(x)$ — is **not a separate rule**. It is the chain rule with $f(u) = u^n$. Memorise the chain rule, derive the general power rule on the fly.

## Common Misconceptions

### 1. "Forgot to multiply by the derivative of the inside"

Student writes $\dfrac{d}{dx}\sin(x^2) = \cos(x^2)$ — the most common chain-rule error. They differentiated the outside but forgot the inside.

**Fix:** Always finish the chain rule by writing **"× derivative of inside"** as a literal step. For $\sin(x^2)$: write $\cos(x^2) \times \dfrac{d}{dx}(x^2)$ first, *then* compute the second factor. The mechanical pause prevents the dropped factor.

### 2. "Differentiated the inside *inside* the outer function"

Student writes $\dfrac{d}{dx}\sin(x^2) = \cos(2x)$ — they replaced $x^2$ with its derivative inside the cosine.

**Fix:** Strict reading: outer derivative gets evaluated *at* the inside, not differentiating the inside inside it. The inside stays put in the outer; its derivative comes out as a *separate factor*.

### 3. "The dx's actually cancel"

Student treats $\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$ as algebraic fraction cancellation — and then tries to apply the same cancellation in places where it doesn't generalise (e.g. with second derivatives, $\dfrac{d^2y}{dx^2} \neq \dfrac{d^2 y}{du^2}\cdot \dfrac{d^2 u}{dx^2}$).

**Fix:** Be explicit: $\dfrac{dy}{dx}$ is a single symbol, not a fraction; the chain rule is a *theorem* that produces an answer that *looks like* fraction cancellation in the first-derivative case. The intuition is excellent; the algebra is illegal. Use the prime-notation form $f'(g(x))\,g'(x)$ when the Leibniz form tempts you to over-cancel.

### 4. "Treats the chain as a sum"

Student writes $\dfrac{d}{dx}\sin(x^2) = \cos(x^2) + 2x$ — adding the two pieces instead of multiplying.

**Fix:** Repeat the rates analogy: gears multiply, not add. Two stages with rates 3 and 4 give an overall rate of 12, not 7. Chain rule = product; sum rule = sum of two *separate* terms, not a composite.

## Exam Notes

### Cambridge 0606 (priority)

Syllabus §14.3: chain rule is **explicitly listed** among required differentiation techniques alongside derivatives of $x^n$, $\sin x$, $\cos x$, $\tan x$, $e^x$, $\ln x$. Expect:

- Differentiate $(ax+b)^n$, $\sin(ax+b)$, $\cos(ax+b)$, $e^{ax+b}$, $\ln(ax+b)$ — the **linear-inside** family. These are the easiest chain-rule applications and appear constantly.
- Differentiate composites with quadratic, root, or trig insides — e.g. $(x^2+3)^7$, $\sqrt{1+x^2}$, $\sin^2 x$ (read as $(\sin x)^2$).
- Combined with [[Product Rule]] (and the quotient rule that lives inside it) in the same problem — typical Paper 1 structure: differentiate $y = x^2 \sin(3x)$ requires *both* product and chain.

Mark schemes award method marks for setting up the chain (writing $\tfrac{dy}{du}\tfrac{du}{dx}$ or naming the outer/inner derivatives) even when the final value is wrong.

### Cambridge 0580

**Not examined.** Extended's calculus (E2.12) stops at derivatives of $ax^n$ and sums of at most three such terms — no composites, so no chain rule. It is the single biggest step up from 0580 to 0606 differentiation.

### Cambridge A-Level 9709

§1.7 (Paper 1, AS): chain rule for $x^n$ composites and the linear-inside family.

§2.4 (Paper 2, AS) and §3.4 (Paper 3, A2): chain rule plus product/quotient, plus implicit and parametric differentiation. The chain rule **is the engine** behind implicit differentiation — every $\dfrac{d}{dx}\bigl(y^2\bigr) = 2y\dfrac{dy}{dx}$ step in an implicit-differentiation problem is one chain-rule application.

§3.5 (Paper 3): integration via substitution is chain rule running backwards — see [[Integration by Substitution]].

### Cambridge 9231 (Further Maths)

**Assumed, never re-examined.** 9709 P1–P3 knowledge is prerequisite for the whole qualification, and the chain rule runs silently inside most FP1/FP2 calculus — every [[Reduction Formulae]] integration by parts, every [[Polar Coordinates]] $\tfrac{dy}{dx}$ from $r(\theta)$, every [[Arc Length and Surfaces of Revolution]] integrand. Fluency is presumed; no question tests the rule itself.

### Edexcel IAL / OxAQA 9660

IAL examines the chain rule (with product and quotient) in **P3.4.2**; OxAQA 9660 in **P2.6**, where it is paired with the reciprocal-derivative rule $\dfrac{dy}{dx} = 1\big/\dfrac{dx}{dy}$ — itself a chain-rule consequence. Both boards then lean on it for connected rates of change: "a balloon's radius increases at $0.5$ cm/s — find the rate of change of volume when $r = 10$", solved as $\dfrac{dV}{dt} = \dfrac{dV}{dr}\cdot\dfrac{dr}{dt}$, the Leibniz form doing exactly what it looks like.

### IB AA / AI

AA names the chain rule at **SL 5.6** (with product and quotient — every AA student meets it); related rates of change are the HL extension and a recurring Paper 2 type. AI is the asymmetry to know: AI **SL** differentiates polynomials only — no chain rule — while AI **HL** brings composites in. HL students on either route are expected to combine chain, product, and quotient fluently.

### AP Calculus AB / BC

Unit 3. Chain rule is tested directly *and* as the engine inside implicit differentiation (Unit 3.2) and inverse-function differentiation (Unit 3.3). BC adds chain rule on parametric and polar curves. Multiple choice questions love trick chain rules — e.g. $\dfrac{d}{dx}\sin(\cos(x^2))$ is a three-stage chain.

> [!tip] Physics bridge — error propagation
> The chain rule is the **master equation of error propagation** in experimental physics. If $z = f(x)$ and $x$ is measured with uncertainty $\Delta x$, then to first order
> $$\Delta z \approx \lvert f'(x)\rvert\,\Delta x.$$
> That's just $\dfrac{dz}{dx}$ pretending to be $\dfrac{\Delta z}{\Delta x}$ — chain rule running through the error chain $\Delta x \to \Delta z$. From this single line, every rule in a Physics error-analysis sheet falls out:
>
> - **Sum / difference $z = x \pm y$.** $dz = dx \pm dy$, so the worst-case bound on $\Delta z$ is $\Delta x + \Delta y$ (signs unknown — absolute errors add).
> - **Product / quotient $z = xy$ or $z = x/y$.** Take logs and use $\dfrac{d(\ln u)}{du} = \dfrac{1}{u}$ — that's the chain rule on $\ln$. Then $\ln z = \ln x \pm \ln y \;\Rightarrow\; \dfrac{dz}{z} = \dfrac{dx}{x} \pm \dfrac{dy}{y}$, and percentage errors add.
> - **Power $z = x^n$.** Same logarithmic move: $\ln z = n\ln x \;\Rightarrow\; \dfrac{dz}{z} = n\dfrac{dx}{x}$. The percentage uncertainty in $z$ is $n$ times the percentage uncertainty in $x$. The textbook example: percentage uncertainty in the volume of a sphere $V = \tfrac{4}{3}\pi r^3$ is **three times** the percentage uncertainty in $r$.
>
> "Why do percentage errors add for multiplication?" is "why do logs turn products into sums?" plus chain rule on $\ln$. The Physics rules feel like a separate subject; they are the chain rule with a lab coat on. See [[Error Propagation]] for the full Physics treatment.

## Connections

- **Parent:** [[Differentiation]] — chain rule is one of the four core differentiation rules.
- **Sibling:** [[Product Rule]] — same family of "make the difference quotient solvable" tricks; both proved by the same kind of attention move.
- **Component:** [[Composite Function]] — without recognising composites, the chain rule has nothing to apply to.
- **Application — implicit:** [[Implicit Differentiation]] — chain rule applied to both sides of an equation. The "attack the defining equation" trick from the Product Rule card *is* implicit differentiation.
- **Application — special derivatives:** [[Differentiation Rules]] — derivations of $(\ln x)'$, $(\sin^{-1}x)'$, $(\sqrt{x})'$, etc., all use chain rule on a defining equation.
- **Application — integration:** [[Integration by Substitution]] — substitution is the chain rule run in reverse. The card explicitly states the chain rule and uses it as the engine.
- **Application — connected rates:** related-rates problems in Mechanics and Physics use chain rule in the Leibniz form $\dfrac{dV}{dt} = \dfrac{dV}{dr}\cdot\dfrac{dr}{dt}$.
- **Application — Physics bridge:** [[Error Propagation]] — the percentage-error and logarithmic-error rules in lab analysis are direct consequences of chain rule on $\ln$.
- **Generalisation:** multivariable calculus's chain rule (university — partial derivatives, Jacobians) — the matrix product version of "rates compose."

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{dy}{dx}$ | `\dfrac{dy}{dx}` | Leibniz form — display-size fraction |
| $f'(g(x))$ | `f'(g(x))` | Prime form — outer derivative evaluated at the inside |
| $\dfrac{dy}{du}\cdot\dfrac{du}{dx}$ | `\dfrac{dy}{du}\cdot\dfrac{du}{dx}` | Composed rates |
| $f \circ g$ | `f \circ g` | Composition operator (rare in calc, common in functional analysis) |
| $\Delta$ | `\Delta` | Finite change, precursor to $d$ in difference quotient |

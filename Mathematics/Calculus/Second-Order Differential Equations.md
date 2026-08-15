---
chinese: 二阶微分方程 (èr jiē wēifēn fāngchéng)
prerequisites:
  - "[[Differential Equations]]"
  - "[[Quadratic Equations]]"
  - "[[Complex Numbers]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[Exponential Function]]"
  - "[[Trigonometric Functions]]"
leads_to:
  - "[[Simple Harmonic Motion]]"
  - "[[Damped Oscillations]]"
  - "[[Resonance]]"
  - "[[Quantum Tunnelling]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - curriculum/A-Level
  - syllabus/9231-2-6
  - type/technique
  - type/theorem
  - type/proof
  - notation/ode
  - notation/auxiliary-equation
  - misconception/wrong-number-of-constants
  - misconception/repeated-root-collapse
  - misconception/pi-clash-with-cf
  - misconception/ics-before-pi
  - misconception/half-trial-for-trig
---

# Second-Order Differential Equations 二阶微分方程

## Definition

### Formal

A **second-order linear differential equation with constant coefficients** has the form

$$a\,\frac{d^2y}{dx^2} + b\,\frac{dy}{dx} + cy = f(x), \qquad a \neq 0,$$

where $a, b, c$ are constants and $f$ is a given function. It is **homogeneous** if $f(x) = 0$ and **non-homogeneous** otherwise. "Linear" means $y$ and its derivatives appear only to the first power, never multiplied together — $y\,\frac{dy}{dx}$ or $\left(\frac{dy}{dx}\right)^2$ would break linearity, and with it every technique on this page.

### Intuitive

Read the equation as a sentence about a moving quantity: *its acceleration is dictated, at every instant, by where it is and how fast it's going.* That is Newton's second law in miniature — $m\,\frac{d^2x}{dt^2} = F$ says exactly this whenever the force depends on position and velocity. A mass on a spring, a car on its suspension, charge sloshing in a circuit, a bridge deck in the wind: each is this one sentence wearing a different costume. First-order equations describe *approach* (growth, decay, cooling); second-order equations are where **oscillation** becomes possible, because a quantity can now overshoot its target and be pulled back.

### 中文锚点

国内教材把这类方程叫 **二阶常系数线性微分方程**。术语对照是这张卡最大的翻译障碍：

| Cambridge 术语 | 国内术语 | 含义 |
|---|---|---|
| auxiliary equation | 特征方程 | 代入 $y = e^{\lambda x}$ 得到的二次方程 |
| complementary function (CF) | 齐次方程的通解 | 右边为 $0$ 时的全部解 |
| particular integral (PI) | (非齐次方程的) 一个特解 | 凑出来的任意一个解 |
| general solution | 通解 | CF + PI，含两个任意常数 |

注意"particular integral"和"particular solution"不同：**particular integral** 是叠加在 CF 上的那一个特解 (不含常数)；**particular solution** 是用初始条件定出 $A, B$ 之后的最终答案。中文都译作"特解"，考试中要靠上下文区分。

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Leibniz | $\dfrac{d^2y}{dx^2}$ | "d two y by d x squared" | Cambridge's preferred form |
| Prime | $y''$ | "y double-prime" | Compact; used freely below |
| Auxiliary root | $\lambda$ (or $m$) | "lambda" | Mark schemes accept either letter |
| Matching sign | $\stackrel{!}{=}$ | "must equal" | Marks the demand step when comparing coefficients; German physics tradition, optional — introduced at first use below |

> [!warning] Notation Trap
> Physics texts write time derivatives with Newton's dots. The equations are identical; only the costume changes (see the LaTeX Reference table). In a maths paper, stay with $\frac{d^2y}{dx^2}$ or $y''$.

## The key idea — exponentials turn calculus into algebra

Try to solve $y'' - 3y' + 2y = 0$. We need a function whose second derivative, first derivative, and self can *cancel each other out* — so all three must have the same shape. Only one function family is unchanged by differentiation: the exponential. Differentiating $e^{\lambda x}$ just multiplies it by $\lambda$:

$$y = e^{\lambda x} \quad\Longrightarrow\quad y' = \lambda e^{\lambda x}, \quad y'' = \lambda^2 e^{\lambda x}.$$

Substitute into the equation:

$$\lambda^2 e^{\lambda x} - 3\lambda e^{\lambda x} + 2 e^{\lambda x} = 0 \quad\Longrightarrow\quad e^{\lambda x}\left(\lambda^2 - 3\lambda + 2\right) = 0.$$

Since $e^{\lambda x} \neq 0$, the *calculus problem collapses into algebra* — what remains is called the **auxiliary equation**:

$$\lambda^2 - 3\lambda + 2 = 0.$$

It factorises as $(\lambda - 1)(\lambda - 2) = 0$, so $e^{x}$ and $e^{2x}$ are both solutions — check them. The recipe in one line: **the derivative acts on exponentials as multiplication by $\lambda$, so a differential equation in $y$ becomes a [[Quadratic Equations|quadratic]] in $\lambda$.** (In the language of linear algebra, $e^{\lambda x}$ is an *eigenfunction* of the derivative — the deepest version of this observation, and the same one that makes $e^{\lambda x}$ the star of [[Differential Equations|first-order linear equations]].)

## Superposition — why two solutions and two constants

Stay with $y'' - 3y' + 2y = 0$, with $e^x$ and $e^{2x}$ in hand. Are there more solutions? Try a mix — say $y = 5e^x - 2e^{2x}$ — and feed it through the left-hand side, keeping the two ingredients in separate brackets:

$$5\underbrace{\left(e^x - 3e^x + 2e^x\right)}_{=\ 0} \;-\; 2\underbrace{\left(4e^{2x} - 6e^{2x} + 2e^{2x}\right)}_{=\ 0} \;=\; 0.$$

Each ingredient passes the test *separately*, so the mix passes automatically — and nothing about the numbers $5$ and $-2$ mattered:

**Claim.** If $y_1$ and $y_2$ solve the homogeneous equation, so does $Ay_1 + By_2$ for any constants $A, B$.

**Proof.** Substitute $y = Ay_1 + By_2$. Differentiation is linear, so $y' = Ay_1' + By_2'$ and $y'' = Ay_1'' + By_2''$. Then

$$a y'' + b y' + c y = A\left(ay_1'' + by_1' + cy_1\right) + B\left(ay_2'' + by_2' + cy_2\right) = A\cdot 0 + B \cdot 0 = 0. \qquad\blacksquare$$

This is **superposition**, and it is a gift of linearity — nonlinear equations enjoy nothing like it. It means the solutions form a *space*: pick two genuinely different solutions and every combination $Ay_1 + By_2$ is free.

Why exactly **two** constants? Recall the counting rule from [[Differential Equations]]: every integration introduces one constant. Undoing a second derivative takes two integrations, so the general solution carries two arbitrary constants — and pinning them down will take two conditions, typically $y(0)$ and $y'(0)$. So the general solution of the homogeneous equation is $y = Ay_1 + By_2$ with $y_1, y_2$ independent: no more solutions exist, none are missed.

## The auxiliary equation — three cases

Everything now hangs on the quadratic $a\lambda^2 + b\lambda + c = 0$, and quadratics come in three flavours, sorted by the discriminant $b^2 - 4ac$. Each flavour is a different *behaviour*.

| Roots of $a\lambda^2 + b\lambda + c = 0$ | Complementary function | Behaviour |
|---|---|---|
| Distinct real $\lambda_1 \neq \lambda_2$ | $y = Ae^{\lambda_1 x} + Be^{\lambda_2 x}$ | Pure growth/decay |
| Repeated real $\lambda$ | $y = (A + Bx)\,e^{\lambda x}$ | Decay with one shove |
| Complex pair $p \pm qi$ | $y = e^{px}\left(A\cos qx + B\sin qx\right)$ | Oscillation in an envelope |

### Case 1 — distinct real roots

The running example already lives here: $y'' - 3y' + 2y = 0$, roots $\lambda = 1, 2$, general solution

$$y = Ae^{x} + Be^{2x}.$$

What do these solutions *do*? Each ingredient grows (or, for negative roots, dies) on its own clock — nothing bends it back. A mix can manage one twist: with $A = 4$, $B = -1$ the solution climbs to a peak at $x = \ln 2$, then dives through zero at $x = \ln 4$ as the faster $e^{2x}$ outruns the slower term. But that is the *most* drama Case 1 allows — $y' = 4e^x - 2e^{2x} = 0$ has exactly one solution, because the ratio of two exponentials is again an exponential, and exponentials only ever cross a value once. One turn, no oscillation, ever.

![[second-order-de-case1-distinct.svg|640]]

### Case 2 — repeated root: where does the $x$ come from?

Change one number: $y'' + 6y' + 9y = 0$. The auxiliary equation $\lambda^2 + 6\lambda + 9 = (\lambda + 3)^2 = 0$ has one root, $\lambda = -3$, *twice*. The recipe hands us $e^{-3x}$ only once — and writing $Ae^{-3x} + Be^{-3x} = (A+B)e^{-3x}$ is a trap: that's *one* constant in disguise, not two. A second, genuinely different solution is needed, and it is $xe^{-3x}$.

**Check it, term by term.** With $y = xe^{-3x}$, the product rule gives $y' = (1 - 3x)e^{-3x}$ and $y'' = (9x - 6)e^{-3x}$. Substitute, keep the $e^{-3x}$ factored out, and sort what's left by powers of $x$:

$$y'' + 6y' + 9y = \Big[\underbrace{(9 - 18 + 9)}_{\text{auxiliary eqn at } \lambda = -3}x \;+\; \underbrace{(-6 + 6)}_{\text{vertex condition}}\Big]e^{-3x} = 0.$$

*Two* separate cancellations had to happen: the $x$-terms die because $-3$ solves the auxiliary equation, and the constants die because $-3$ is the parabola's *vertex* (that's what a double root is). Watch what the new solution looks like — $e^{-3x}$ can only fall, but $xe^{-3x}$ rises once and then decays: a shove that fades.

![[second-order-de-case2-repeated.svg|640]]

**Verify in general.** A repeated root means $b^2 = 4ac$ and $\lambda = -\frac{b}{2a}$, i.e. $2a\lambda + b = 0$. Let $y = xe^{\lambda x}$. Then $y' = (1 + \lambda x)e^{\lambda x}$ and $y'' = (2\lambda + \lambda^2 x)e^{\lambda x}$, so

$$ay'' + by' + cy = e^{\lambda x}\Big[\underbrace{(a\lambda^2 + b\lambda + c)}_{=\ 0}\,x + \underbrace{(2a\lambda + b)}_{=\ 0}\Big] = 0. \qquad\blacksquare$$

The same two cancellations as the concrete check, wearing letters: the first bracket is the auxiliary equation, the second is the vertex condition. For a *distinct* root only the first bracket dies — which is why the $x$-trick works exactly when roots collide.

**Where it really comes from.** Recall the definition of the derivative: $g'(\lambda) = \lim_{\mu \to \lambda} \dfrac{g(\mu) - g(\lambda)}{\mu - \lambda}$ — the limit of a difference quotient as the two sample points merge. Now imagine two distinct roots $\lambda$ and $\mu$ sliding toward each other. The combination $\dfrac{e^{\mu x} - e^{\lambda x}}{\mu - \lambda}$ is a legal solution while they're apart (it's just superposition with $A = \frac{-1}{\mu - \lambda}$, $B = \frac{1}{\mu - \lambda}$). Freeze $x$ and squint: reading $e^{\lambda x}$ as a function of the *root* — $g(\lambda) = e^{\lambda x}$, with $x$ a frozen constant — that combination **is** $g$'s difference quotient. So as $\mu \to \lambda$ it becomes $g$'s derivative, taken with respect to $\lambda$, not $x$:

$$\lim_{\mu \to \lambda} \frac{e^{\mu x} - e^{\lambda x}}{\mu - \lambda} = \frac{\partial}{\partial \lambda} e^{\lambda x} = x\,e^{\lambda x}.$$

The second solution doesn't vanish when the roots merge — it survives as the derivative of the family. 

### Case 3 — complex roots: oscillation is born

Change one number again: $y'' + 2y' + 5y = 0$. The auxiliary equation $\lambda^2 + 2\lambda + 5 = 0$ has no real roots — the discriminant is $4 - 20 < 0$ — and the quadratic formula delivers the conjugate pair $\lambda = -1 \pm 2i$. The table claims the general solution is $y = e^{-x}(A\cos 2x + B\sin 2x)$. Before *deriving* that, **check a piece of it, term by term**: take $y = e^{-x}\cos 2x$. The product rule gives $y' = -e^{-x}(\cos 2x + 2\sin 2x)$ and $y'' = e^{-x}(4\sin 2x - 3\cos 2x)$. Substitute, factor out $e^{-x}$, and collect cosines and sines *separately*:

$$y'' + 2y' + 5y = \Big[\underbrace{(-3 - 2 + 5)}_{\text{coefficient of}\ \cos 2x}\cos 2x + \underbrace{(4 - 4)}_{\text{coefficient of}\ \sin 2x}\sin 2x\Big]e^{-x} = 0.$$

Both collections vanish — the $\sin 2x$ terms that differentiation kept generating cancel *among themselves*. (The $\sin$-partner $e^{-x}\sin 2x$ passes the same check.) So the strange-looking recipe genuinely works. Here is where it comes from.

**Where the recipe knew.** Complex roots come in a conjugate pair $\lambda = p \pm qi$ (the coefficients are real). Formally the solution is $Ce^{(p+qi)x} + De^{(p-qi)x}$; [[Euler's Formula and De Moivre's Theorem|Euler's formula]] $e^{i\theta} = \cos\theta + i\sin\theta$ unpacks it:

$$e^{(p \pm qi)x} = e^{px}\,e^{\pm qix} = e^{px}\left(\cos qx \pm i \sin qx\right).$$

Regrouping the constants (take $A = C + D$, $B = i(C-D)$; both real when the initial conditions are real) gives the real form

$$\boxed{\,y = e^{px}\left(A\cos qx + B\sin qx\right)\,}$$

The real part $p$ builds the **envelope** $e^{px}$ — growth or decay. The imaginary part $q$ sets the **frequency** of the oscillation inside it. In the concrete example: $p = -1$ gives the shrinking cage $e^{-x}$, $q = 2$ gives the ringing inside it. This is the single deepest reason [[Complex Numbers|complex numbers]] matter in applied mathematics: the moment a system can overshoot and swing back, its natural "growth rates" become complex, and $i$ steps out of algebra into motion.

![[second-order-de-case3-complex.svg|640]]

### One machine, one dial

Line the three concrete examples up and they stop being three separate recipes. Fix the restoring force and turn the *friction* dial down: distinct real roots (sluggish return, no overshoot) merge into a repeated root (fastest return without overshoot) and then split into complex roots (overshoot and ring). On the complex plane, the two roots slide toward each other along the real axis, collide, and split *vertically* into a conjugate pair — and the solution curve morphs with them:

![[second-order-de-damping-dial.mp4]]

![[second-order-de-three-cases.svg|900]]

And all three settings are *products*, not failure modes — engineers pay for each one on purpose:

![[second-order-de-damping-comic.png|700]]

A soft-close drawer is overdamped by design (it must *never* slam, however hard it's shoved); a car's suspension is tuned near critical (a pothole absorbed in one motion, no bounce — [[Damped Oscillations]] tells the physics side, and the boundary value is derived under Beyond Syllabus); and a bell is underdamped *on purpose* — the ring is the product being sold.

## Non-homogeneous equations — the structure theorem

Now let the right-hand side speak. Take the running example and switch the forcing on:

$$y'' - 3y' + 2y = 4.$$

One solution is hiding in plain sight: try the constant $y = 2$. Both derivatives vanish, and $2 \cdot 2 = 4$. ✓ But a single solution with *no* arbitrary constants can't be the whole story. Try adding a homogeneous solution on top — $y = 2 + e^x$: the $e^x$ part contributes $0$ (it solves the homogeneous equation, as Case 1 checked), the $2$ part contributes $4$, so the sum still works. So does $2 + 5e^x - 2e^{2x}$, and so does $2$ plus *any* member of Case 1's family. One private solution, plus the entire homogeneous family riding along for free — that observation *is* the strategy:

> **General solution = CF + PI.**
> The **complementary function** is the general solution of the homogeneous equation (right side $0$).
> A **particular integral** is *any one* solution of the full equation.

**Why this is everything.** Suppose $y_p$ is one solution and $y$ is any other. Subtract:

$$a(y - y_p)'' + b(y - y_p)' + c(y - y_p) = f(x) - f(x) = 0,$$

so the *difference of any two solutions solves the homogeneous equation* — the difference is some member of the CF. Every solution is therefore $y_p$ plus CF, and $y = y_{\text{CF}} + y_{\text{PI}}$ captures them all with no repeats and no gaps. $\blacksquare$

The physical reading is worth keeping: the CF is the system's *own voice* — how it moves when left alone, fading out in any damped system (the **transient**). The PI is the *forcing's signature* — the response that the right-hand side sustains indefinitely (the **steady state**). Strike a wine glass and the CF rings and dies; sing at it steadily and the PI is the hum it holds while you do.

## Finding a particular integral — educated guessing

How do you *find* the one private solution? Watch it happen once before any rules. Same left side, a moving target on the right:

$$y'' - 3y' + 2y = 4x.$$

The forcing is a polynomial, so guess *in the polynomial family* with unknown coefficients: $y = px + q$. Then $y' = p$, $y'' = 0$, and substituting:

$$0 - 3p + 2(px + q) = 2px + (2q - 3p) \stackrel{!}{=} 4x.$$

(The symbol $\stackrel{!}{=}$ reads "**must** equal" — it marks the moment we stop *deriving* and start *demanding*, so the coefficients on both sides can be matched. It comes from the German physics tradition; Cambridge mark schemes don't use it, but examiners read it fine — or just write "comparing coefficients.") Matching: $2p = 4$ gives $p = 2$, then $2q - 6 = 0$ gives $q = 3$. So $y_{\text{PI}} = 2x + 3$ — and notice the $q$: the forcing $4x$ has no constant term, but the trial still needed one, because the $-3y'$ term feeds the constant slot.

That's the whole method: **trial a function of the same family as $f$, substitute, match.** Linear equations are polite — they never turn a polynomial into a sine or an exponential into a logarithm, so the guess stays in the family:

| Right-hand side $f(x)$ | Trial form |
|---|---|
| Polynomial of degree $n$ (e.g. $6x+7$) | Full polynomial of degree $n$: $px + q$ |
| $ke^{bx}$ | $\kappa e^{bx}$ |
| $k\cos px$, $k \sin px$, or a mix | $\kappa\cos px + \mu\sin px$ — **always both terms** |
| Sums of the above | Sum of the trials |

Two rules carry all the marks — and both are best learned by watching the wrong trial *fail*:

1. **Trial the whole family, not the term you see.** Try $y'' - 3y' + 2y = \sin x$ with the lazy guess $y = \mu\sin x$: the left side gives $-\mu\sin x - 3\mu\cos x + 2\mu\sin x = \mu\sin x - 3\mu\cos x$. That $-3\mu\cos x$ has no partner on the right — $\mu$ would have to be $0$ and $1$ at once. Differentiation *rotates* sine into cosine, so the pair is one family and the trial must carry both: $y = \kappa\cos x + \mu\sin x$ gives $(\kappa - 3\mu)\cos x + (3\kappa + \mu)\sin x \stackrel{!}{=} \sin x$, so $\kappa = 3\mu$ and $10\mu = 1$: the PI is $\tfrac{1}{10}(3\cos x + \sin x)$. Same discipline for polynomials — forcing $4x$ still needed the $q$.
2. **If the trial already lives in the CF, multiply by $x$.** Try $y'' - 3y' + 2y = e^{2x}$ with the obvious guess $y = \kappa e^{2x}$: the left side gives $\kappa(4 - 6 + 2)e^{2x} = 0$, and the working collapses to $0 = e^{2x}$ — a contradiction, not an equation for $\kappa$. Of course it does: $e^{2x}$ is *in the CF*, and the left side annihilates its own homogeneous solutions by definition. The escape is the same $x$-trick as Case 2, for the same structural reason: try $y = \kappa x e^{2x}$ instead, and the left side returns $\kappa e^{2x}$ exactly, so $\kappa = 1$ and $y_{\text{PI}} = xe^{2x}$. (Multiply by $x$ *again* if the trial still sits in the CF — the repeated-root case.) Physically this is **resonance**: forcing a system at its own natural frequency doesn't produce a steady response, it produces a growing one. Example 3 below shows it in full.

## Worked examples

### Example 1 — distinct real roots, polynomial forcing, initial conditions

> Solve $\dfrac{d^2y}{dx^2} - 5\dfrac{dy}{dx} + 6y = 6x + 7$, given $y(0) = 4$ and $y'(0) = 6$.

**Step 1 — CF.** Auxiliary: $\lambda^2 - 5\lambda + 6 = 0 \Rightarrow (\lambda-2)(\lambda-3) = 0 \Rightarrow \lambda = 2, 3$.
$$y_{\text{CF}} = Ae^{2x} + Be^{3x}.$$

**Step 2 — PI.** Trial $y = px + q$, so $y' = p$, $y'' = 0$:
$$0 - 5p + 6(px + q) = 6px + (6q - 5p) \stackrel{!}{=} 6x + 7.$$
Matching: $6p = 6 \Rightarrow p = 1$, then $6q - 5 = 7 \Rightarrow q = 2$. So $y_{\text{PI}} = x + 2$.

**Step 3 — general solution.** $y = Ae^{2x} + Be^{3x} + x + 2$.

**Step 4 — conditions last.** $y(0) = A + B + 2 = 4 \Rightarrow A + B = 2$. Differentiate the *whole* solution: $y' = 2Ae^{2x} + 3Be^{3x} + 1$, so $y'(0) = 2A + 3B + 1 = 6 \Rightarrow 2A + 3B = 5$. Solving: $B = 1$, $A = 1$.

$$\boxed{\,y = e^{2x} + e^{3x} + x + 2\,}$$

### Example 2 — complex roots, exponential forcing

> Solve $y'' + 2y' + 5y = 8e^{-x}$.

**CF.** $\lambda^2 + 2\lambda + 5 = 0 \Rightarrow \lambda = \dfrac{-2 \pm \sqrt{4 - 20}}{2} = -1 \pm 2i$, so $y_{\text{CF}} = e^{-x}(A\cos 2x + B\sin 2x)$.

**PI.** $e^{-x}$ is not in the CF (the CF carries $e^{-x}\cos 2x$ and $e^{-x}\sin 2x$ — different functions), so trial $y = \kappa e^{-x}$: $y' = -\kappa e^{-x}$, $y'' = \kappa e^{-x}$, giving $\kappa(1 - 2 + 5)e^{-x} = 4\kappa e^{-x} \stackrel{!}{=} 8e^{-x}$, so $\kappa = 2$.

$$\boxed{\,y = e^{-x}\left(A\cos 2x + B\sin 2x\right) + 2e^{-x}\,}$$

A damped oscillation riding on a decaying push — everything here fades, but the ringing ($\cos 2x, \sin 2x$) and the fading (envelope $e^{-x}$) are visibly separate parts of the answer.

### Example 3 — resonance, and reading a given trial form

> Given that $kx\cos 2x$ is a particular integral of $\dfrac{d^2y}{dx^2} + 4y = \sin 2x$, find $k$.

First, *why this strange trial*: the CF is $A\cos 2x + B\sin 2x$ (auxiliary $\lambda^2 + 4 = 0$, $\lambda = \pm 2i$), so the natural trial $\kappa\cos 2x + \mu\sin 2x$ is swallowed whole by the left-hand side — the forcing frequency *equals* the natural frequency. Multiply by $x$.

Substitute $y = kx\cos 2x$. Product rule, twice:
$$y' = k\cos 2x - 2kx\sin 2x,$$
$$y'' = -2k\sin 2x - 2k\sin 2x - 4kx\cos 2x = -4k\sin 2x - 4kx\cos 2x.$$
Then
$$y'' + 4y = -4k\sin 2x - 4kx\cos 2x + 4kx\cos 2x = -4k\sin 2x \stackrel{!}{=} \sin 2x,$$
so $-4k = 1$ and
$$\boxed{\,k = -\tfrac{1}{4}, \qquad y_{\text{PI}} = -\tfrac{x}{4}\cos 2x\,}$$

The $x$ out front means the amplitude **grows without bound** — each push arrives exactly in rhythm with the swing, so energy only ever flows in. That is resonance, caught red-handed by algebra.

![[second-order-de-resonance.svg|900]]

Real systems always carry some damping, which caps the growth at a tall-but-finite peak (right panel) — this is why soldiers break step on bridges and why a singer *can* crack a wine glass but a slightly-off note does nothing. The Tacoma Narrows collapse of 1940 is the folklore example; the honest fine print (the true mechanism was aeroelastic flutter, resonance's feedback-loop cousin) is in [[Stories/The Pendulum Story]], and the physics treatment lives in [[Simple Harmonic Motion]] §"Driven oscillations and resonance".

### Example 4 — a given substitution: the equation with variable coefficients

> Use the substitution $x = e^t$ to solve $x^2\dfrac{d^2y}{dx^2} - x\dfrac{dy}{dx} + y = 0$ for $x > 0$.

The coefficients here are *not* constant — the whole toolkit above seems to fail. The substitution rescues it. The symbol count in this derivation genuinely exceeds what working memory holds on a first read, so watch the conversion assemble itself first — each term generated, transformed, and slotted into place — then follow the written steps:

![[second-order-de-euler-substitution.mp4]]

Go slowly; every mark in this question is in the chain rule.

**Step 1.** From $x = e^t$: $t = \ln x$, so $\dfrac{dt}{dx} = \dfrac{1}{x}$.

**Step 2.** First derivative, chain rule:
$$\frac{dy}{dx} = \frac{dy}{dt}\cdot\frac{dt}{dx} = \frac{1}{x}\,\frac{dy}{dt} \quad\Longrightarrow\quad x\frac{dy}{dx} = \frac{dy}{dt}.$$

**Step 3.** Second derivative — differentiate $\frac{dy}{dx} = \frac{1}{x}\frac{dy}{dt}$ with respect to $x$, product rule first, chain rule inside:
$$\frac{d^2y}{dx^2} = -\frac{1}{x^2}\,\frac{dy}{dt} + \frac{1}{x}\cdot\frac{d}{dx}\!\left(\frac{dy}{dt}\right) = -\frac{1}{x^2}\,\frac{dy}{dt} + \frac{1}{x}\cdot\frac{d^2y}{dt^2}\cdot\frac{1}{x},$$
$$\Longrightarrow\quad x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} - \frac{dy}{dt}.$$

**Step 4.** Substitute both boxed conversions into the equation:
$$\left(\frac{d^2y}{dt^2} - \frac{dy}{dt}\right) - \frac{dy}{dt} + y = 0 \quad\Longrightarrow\quad \frac{d^2y}{dt^2} - 2\frac{dy}{dt} + y = 0.$$
Constant coefficients — the machine applies. Auxiliary: $\lambda^2 - 2\lambda + 1 = (\lambda - 1)^2 = 0$, repeated root $\lambda = 1$.

**Step 5.** $y = (A + Bt)e^t$, and translating back with $e^t = x$, $t = \ln x$:
$$\boxed{\,y = (A + B\ln x)\,x\,}$$

(Check the strange piece: $y = x\ln x$ gives $y' = \ln x + 1$, $y'' = \frac1x$, and $x^2\cdot\frac1x - x(\ln x + 1) + x\ln x = x - x\ln x - x + x\ln x = 0$.) Exam questions always *give* the substitution; the skill being bought is the chain-rule conversion in Steps 2–3, which is identical every time.

**Substitutions to separable form.** The same move appears one order down: for $\dfrac{dy}{dx} = \dfrac{x - y}{x + y}$, the given substitution $y = ux$ (with $\frac{dy}{dx} = u + x\frac{du}{dx}$) turns the right side into $\frac{1-u}{1+u}$ and the equation into
$$x\frac{du}{dx} = \frac{1 - 2u - u^2}{1 + u},$$
which is separable: $\int\frac{1+u}{1 - 2u - u^2}\,du = \int\frac{dx}{x}$. The left integrand is $-\tfrac12\cdot\frac{\text{derivative}}{\text{function}}$, so integrating gives $-\tfrac12\ln\lvert 1 - 2u - u^2\rvert = \ln\lvert x\rvert + C$, and tidying (exponentiate, substitute $u = y/x$, absorb constants) lands the elegant implicit solution $x^2 - 2xy - y^2 = C$. The separable machinery itself is [[Differential Equations]] material — the only new step is executing the given substitution.

## Common Misconceptions (Teaching Notes)

### 1. Wrong number of arbitrary constants

Students produce one constant (stopping at $y = Ae^{\lambda_1 x}$) or bolt a "+C" onto a finished solution.

**Fix:** count integrations. Undoing $\frac{d^2y}{dx^2}$ takes two integrations → two constants, *inside* the structure $Ay_1 + By_2$, never appended. A solution with the wrong number of constants fails before any algebra is checked.

### 2. The repeated-root collapse

$\lambda = 3$ twice, and the student writes $y = Ae^{3x} + Be^{3x}$ — which is $(A+B)e^{3x}$, one constant wearing two names.

**Fix:** have them *add* their two terms. The shock of watching two constants merge into one sells the need for $x$: $y = (A + Bx)e^{3x}$. Then show the colliding-roots limit — the $x$ isn't a patch, it's what survives when two exponentials merge.

### 3. Applying initial conditions before adding the PI

The classic mark-loser: find the CF, fit $A$ and $B$ to the initial conditions, *then* add the PI — the final answer no longer satisfies the conditions.

**Fix:** conditions come **last**, applied to the complete $y = \text{CF} + \text{PI}$. The PI contributes to $y(0)$ and $y'(0)$ too. Drill the order: CF → PI → general solution → conditions.

### 4. Half a trial for trig forcing

Forcing $\sin 2x$, trial $\mu \sin 2x$ — and the substitution produces unmatched $\cos 2x$ terms, forcing $\mu$ to do two contradictory jobs.

**Fix:** differentiation *rotates* sine and cosine into each other, so the pair is one family — the trial must carry both: $\kappa\cos 2x + \mu\sin 2x$. (Underneath: $\cos$ and $\sin$ are the two shadows of one $e^{2ix}$, and the family is closed the same way $e^{bx}$ is.)

### 5. Not noticing the trial sits in the CF

The student tries $\kappa e^{2x}$ against a CF containing $e^{2x}$, gets $0 = 8e^{2x}$, and concludes "no solution" (or worse, pushes on with broken algebra).

**Fix:** teach $0 = f(x)$ as a *diagnosis*, not a dead end: the left side annihilates the trial precisely because it's a homogeneous solution. Escape as in Case 2 — multiply by $x$. Physical anchor: pushing a swing at its own frequency can't produce a steady amplitude.

## Exam Notes

### Cambridge 9231 Further Pure 2 (§2.6)

- The full menu: integrating factor for first-order linear (covered in [[Differential Equations]]); CF + PI for first *and* second order; the three auxiliary-equation cases; PI forms — polynomial, $ae^{bx}$, $a\cos px + b\sin px$, plus "other simple cases" where the trial form is **given** and only the coefficient is wanted (Example 3 is the syllabus's own specimen); **given** substitutions reducing to constant-coefficient or separable form (Examples 4 and the $y = ux$ specimen); initial conditions and interpretation of solutions in a modelled context.
- Substitutions are always supplied in the question — the credit is in the chain-rule conversion and the tidy return to the original variable.
- Interpretation marks are cheap if you know the vocabulary: which term is the transient (the CF, dying with its negative exponents), what the steady state is (the PI), what happens as $t \to \infty$.
- **Formula sheet:** MF19 gives *nothing* for differential equations — the three-case CF table and the PI trial table must live in your head.

### Edexcel Further Mathematics (Core Pure 2)

- The same three-case CF table, PI by trial, and boundary/initial conditions — with a heavier **modelling accent**: damped and forced harmonic motion appear explicitly ($\frac{d^2x}{dt^2} + k\frac{dx}{dt} + \omega^2 x = f(t)$ dressed as a spring, a pendulum, or a circuit), and questions routinely ask you to *classify* the damping (heavy/critical/light in Edexcel's vocabulary = Cases 1/2/3) and describe the long-term motion.
- Edexcel's signature extra: **coupled first-order systems** ($\frac{dx}{dt} = ax + by$, $\frac{dy}{dt} = cx + dy$) reduced by elimination to one second-order equation — the technique is differentiation of one equation and substitution of the other, then everything on this page applies.

### AQA / OCR A-Level Further Mathematics

- Both carry the same core menu (three CF cases, CF + PI, initial/boundary conditions, oscillation contexts) in the compulsory pure content; OCR (including MEI) likewise runs damping-classification and lightly-damped-oscillation interpretations.
- Each board publishes its own formula booklet — check it before assuming anything is given; as with MF19, the CF case table is generally *not* handed to you.

### Where it is *not* examined

- **9709**: P3 §3.8 stops at first-order separable equations. Nothing second-order.
- **IB AA HL**: first-order only (separable, homogeneous via $y = ux$, integrating factor, Euler's method) — second-order equations are not in the current guide.
- **AP Calculus BC**: first-order separable, slope fields, Euler's method, logistic — no second-order, no CF/PI.

## Connections

- **Parent:** [[Differential Equations]] — first-order machinery, the constant-counting rule, and the modelling grammar all extend from there; its beyond-syllabus preview of second-order equations is delivered in full here.
- **Proof ingredients:** [[Quadratic Equations]] — the auxiliary equation *is* one, discriminant and all; [[Complex Numbers]] + [[Euler's Formula and De Moivre's Theorem]] — Case 3 runs on $e^{i\theta} = \cos\theta + i\sin\theta$; [[Exponential Function]] — the eigenfunction of the derivative, the engine of the whole method.
- **Physics application:** [[Simple Harmonic Motion]] — $\frac{d^2x}{dt^2} = -\omega^2 x$ is Case 3 with $p = 0$: pure oscillation, no envelope. The SHM treatment (two solution routes, energy, phase) is the physical life of the equation's cleanest special case; its §"Damping — when energy leaks out" and §"Driven oscillations and resonance" carry the physics of the full equation.
- **Physics bridges — reserved:** [[Damped Oscillations]], [[Resonance]] — 9702 §17's oscillation cards; the three-case dial and the forced-response peak are their mathematical skeletons.
- **Quantum bridge — reserved:** [[Quantum Tunnelling]] — the beyond-syllabus cameo grown up: barrier penetration as Case 1 (real exponential decay) living where Case 3 (oscillation) can't.
- **Electrical costume:** [[Capacitors]] — the RC circuit is the first-order cousin; adding an inductor makes the series RLC circuit, which obeys exactly $L\frac{d^2Q}{dt^2} + R\frac{dQ}{dt} + \frac{Q}{C} = V(t)$ — inductance as mass, resistance as friction, $1/C$ as stiffness. One equation, mechanical and electrical costumes.
- **Story:** [[Stories/The Pendulum Story]] — Galileo's chandelier to the caesium clock, with Tacoma Narrows as the dark twin of isochronism (and the honest flutter-vs-resonance correction).
- **Approximation link:** [[Maclaurin Series]] — why *linear* equations rule physics: near equilibrium, any restoring force is its tangent line ($F(x) \approx F'(0)\,x$), so small motions of almost anything obey the linear constant-coefficient equation. The pendulum's $\sin\theta \approx \theta$ is the canonical instance.
- **For 9231 students:** [[MF19 Reference (9231)]] — MF19 carries no ODE formulas at all; memorise the three-case table and the PI trials.

## Beyond Syllabus

### The operator view — factorising the derivative

Write $D = \frac{d}{dx}$, so the equation $y'' - 5y' + 6y = 0$ becomes $(D^2 - 5D + 6)\,y = 0$. The polynomial in $D$ factorises exactly like the auxiliary quadratic:

$$(D - 2)(D - 3)\,y = 0.$$

Anything killed by $(D-3)$ — that is, any solution of $y' = 3y$, i.e. $Be^{3x}$ — is killed by the whole product, and likewise for $(D-2)$. The auxiliary equation isn't a trick: **factorising the polynomial literally factorises the differential operator into first-order pieces.** The repeated-root case reads as $(D - \lambda)^2 y = 0$: applying $(D-\lambda)$ to $xe^{\lambda x}$ leaves $e^{\lambda x}$ (one "layer" peeled), and applying it again gives $0$ — which is exactly why the $x$-trick works once per repetition.

### Critical damping — the engineer's target

For a mass–spring–damper $m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx = 0$, the discriminant of $m\lambda^2 + c\lambda + k$ separates the three cases, and the boundary

$$c^2 = 4mk \quad\Longleftrightarrow\quad c = 2\sqrt{mk}$$

is **critical damping**: the repeated-root case, the fastest possible return to equilibrium with no overshoot. Car suspensions, door closers, and analogue meter needles are all tuned near it — less damping and the system rings (Case 3), more and it wallows (Case 1). The mathematically thinnest case (a single point on the $c$-axis) is the engineering sweet spot.

### Higher order, same recipe

An $n$-th order linear constant-coefficient equation has an $n$-th degree auxiliary polynomial: $n$ roots, $n$ independent solutions, $n$ constants. Repeated roots contribute $e^{\lambda x}, xe^{\lambda x}, x^2e^{\lambda x}, \ldots$; complex pairs contribute envelope-times-oscillation pairs. Nothing new is needed — the second-order case already contains every idea.

### Where the machine stops

Variable coefficients kill the exponential guess (the equation of Example 4 is the lucky exception, and only because a substitution restores constancy). Nonlinearity kills superposition itself — the true pendulum equation $\frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta$ has no CF, no PI, and no closed form; [[Numerical Methods]] take over from there, and qualitative tools (phase portraits, sketched in [[Differential Equations]]'s beyond-syllabus tour) recover understanding without formulas.

### The quantum cameo

Recall that Case 1 gives real exponentials and Case 3 gives oscillations. The time-independent Schrödinger equation in a region of constant potential is exactly the constant-coefficient equation above: where a particle has enough energy, the roots are imaginary and the wavefunction *oscillates* (a travelling wave); where it doesn't — inside a barrier — the roots are real and the wavefunction becomes a *decaying exponential* rather than vanishing. That leaking tail is [[Quantum Tunnelling|quantum tunnelling]]: Case 1 and Case 3 of the same auxiliary equation, drawn one on each side of a wall.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{d^2y}{dx^2}$ | `\dfrac{d^2y}{dx^2}` | Second derivative, Leibniz form |
| $y''$ | `y''` | Prime shorthand |
| $\ddot x$ | `\ddot x` | Newton's dots (physics texts, time derivatives) |
| $\lambda$ | `\lambda` | Auxiliary-equation root |
| $e^{\lambda x}$ | `e^{\lambda x}` | The trial exponential |
| $p \pm qi$ | `p \pm qi` | Complex root pair |
| $\kappa, \mu$ | `\kappa, \mu` | PI trial coefficients |
| $\stackrel{!}{=}$ | `\stackrel{!}{=}` | "Must equal" — matching condition |
| $\blacksquare$ | `\blacksquare` | End of proof |

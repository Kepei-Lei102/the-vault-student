---
chinese: 概率生成函数 (gàilǜ shēngchéng hánshù) — 又称概率母函数
prerequisites:
  - "[[Discrete Random Variables]]"
  - "[[Poisson Distribution]]"
  - "[[Linear Combinations of Random Variables]]"
  - "[[Binomial Series]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Differentiation]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/probability
  - domain/statistics
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/A-Level
  - syllabus/9231-4-5
  - type/deep
  - type/technique
  - notation/pgf-G-of-t
  - misconception/substituting-t-equals-1-before-differentiating
  - misconception/variance-from-pgf-drops-the-mean-term
  - misconception/pgf-product-without-independence
  - misconception/pgf-of-linear-transform
---

# Probability Generating Functions 概率生成函数

> *A discrete distribution is a list — a probability for $0$, one for $1$, one for $2$, and so on. A probability generating function is that same list written as **one expression**, with each probability hung on a hook labelled $t^0, t^1, t^2, \dots$ so that it cannot fall off. The payoff is that operations you would do to the list one entry at a time — add up, take the mean, add two independent variables — become single moves on the expression: put $t = 1$, differentiate, multiply. Two dice, a family tree, an outbreak: the same polynomial trick prices all of them.*

## Definition

### Formal

For a discrete random variable $X$ taking values in $\{0, 1, 2, \dots\}$ with $P(X = x) = p_x$, the **probability generating function** is

$$G_X(t) = E\!\left(t^X\right) = \sum_{x} p_x\, t^{x} = p_0 + p_1 t + p_2 t^2 + \cdots$$

— a power series (a polynomial if $X$ takes finitely many values) whose coefficient of $t^x$ is $P(X = x)$. Three facts follow at once, and they are the three lines MF19 prints:

$$G_X(1) = 1, \qquad E(X) = G_X'(1), \qquad \operatorname{Var}(X) = G_X''(1) + G_X'(1) - \{G_X'(1)\}^2 .$$

And the result that makes the machine worth building: if $X$ and $Y$ are **independent**, $G_{X+Y}(t) = G_X(t)\,G_Y(t)$. Because the coefficients are the probabilities, a PGF determines its distribution — read the coefficients back and you have the pmf; recognise a familiar shape and you have named the distribution.

### Intuitive

$t$ is not a probability and not a variable you will ever solve for. It is a **coat hook**. Write the distribution of $X$ = the number of heads in three tosses of a fair coin as $\tfrac18 + \tfrac38 t + \tfrac38 t^2 + \tfrac18 t^3$: the power on each hook says *which value*, the weight hanging on it says *how likely*. Nothing has been lost — but now the whole distribution is one object you can do algebra to. Put $t = 1$ and every hook counts once: the weights add to $1$. Differentiate, and calculus does something useful for free — it multiplies each weight by its own hook's label and drops the hook by one — so that at $t = 1$ you are adding $x \cdot p_x$: the mean. And multiply two of these shelves together and the powers add, $t^x \cdot t^y = t^{x+y}$, so the product is automatically sorted by the *sum* — which is exactly what the distribution of $X + Y$ needs.

![[pgf-coat-hooks.svg|860]]

### 中文锚点 (Chinese Anchor)

一句话：概率生成函数把一张"取值—概率"的表**打包成一个式子**——每个概率挂在写着 $t^x$ 的钩子上，$t$ 本身不是概率、也不用解，只是钩子。打包以后，原本要一项一项做的事变成一步：**代 $t=1$** 得到概率之和 $1$（顺手求出未知常数）；**求导再代 $t=1$** 得到均值，**求两次导**得到方差；两个**独立**变量之和的生成函数就是两个生成函数**相乘**（多项式相乘正好把"凑出同一个和"的方式全部收集起来）。反过来，把式子展开，$t^k$ 的系数就是 $P(X=k)$，认出形状就认出了分布（$(q+pt)^n$ 是二项分布，$e^{\lambda(t-1)}$ 是泊松分布）。要求：变量取非负整数值；相乘那一步**必须独立**。考试常见的坑：先代 $t=1$ 再求导（顺序反了）、方差公式漏掉 $+G'(1)$、把不独立的变量的生成函数相乘。

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| The PGF | $G_X(t) = E(t^X) = \sum p_x t^x$ | "G X of t" | the subscript names the variable; some books write $\Pi_X$ or $\phi_X$ |
| Its value at $1$ | $G_X(1) = 1$ | | total probability — the check that finds unknown constants |
| First derivative at $1$ | $G_X'(1) = E(X)$ | | differentiate **first**, then substitute |
| Second derivative at $1$ | $G_X''(1) = E[X(X-1)]$ | "the second factorial moment" | not $E(X^2)$: hence the extra $+G_X'(1)$ in the variance |
| Sum rule | $G_{X+Y}(t) = G_X(t)\,G_Y(t)$ | | **independent** $X, Y$ only; $n$ i.i.d. copies: $\{G_X(t)\}^n$ |
| Linear change | $G_{aX+b}(t) = t^{b}\,G_X(t^{a})$ | | $E(t^{aX+b}) = t^b E\big((t^a)^X\big)$ — the hooks are relabelled |
| Reading a probability | $P(X = k) = [t^k]\,G_X(t) = \dfrac{G_X^{(k)}(0)}{k!}$ | "the coefficient of $t^k$" | $G_X(0) = P(X = 0)$ |

> [!warning] Two habits that cost marks — and one that earns them
> **Differentiate first, substitute second.** $G_X'(1)$ means *differentiate, then put $t = 1$*; a student who writes $G_X(1) = 1$ and then differentiates $1$ gets $0$. **Keep the middle term of the variance.** $G_X''(1)$ is $E[X(X-1)] = E(X^2) - E(X)$, so $\operatorname{Var}(X) = G_X''(1) + G_X'(1) - \{G_X'(1)\}^2$ — dropping the $+G_X'(1)$ is the single commonest error on the paper. **And always check $G_X(1) = 1$ first**: it is how every unknown constant $k$ in a printed PGF is found, and it is a free sanity check on a PGF you built yourself.

## Why it works — hooks, labels, and multiplying shelves

**Why $G(1) = 1$, $G'(1) = E(X)$ and the variance formula are one move done three times.** Take $G_X(t) = 0.1 + 0.3t + 0.4t^2 + 0.2t^3$ (a real Paper 4 question, Case 1A below). Differentiating a single hook $p_x t^x$ gives $x\,p_x\,t^{x-1}$: calculus has *read the label $x$ off the hook and multiplied the weight by it*, then dropped the hook one power. Put $t = 1$ and every hook counts once again, so the derivative adds up $\sum x\,p_x = E(X)$: here $0 + 0.3 + 0.8 + 0.6 = 1.7$. Do it again: the second derivative reads the label a second time — but the label is now $x - 1$, because the hook already dropped — so each weight becomes $x(x-1)p_x$, and at $t = 1$ you have $E[X(X-1)] = E(X^2) - E(X)$: here $0.8 + 1.2 = 2$. That is why the variance needs a repair term — three lines, each one you already own:

$$\begin{aligned}
G''(1) &= E[X(X-1)] = E(X^2) - E(X) &&\text{(the second read sees the label } x-1\text{)}\\
\operatorname{Var}(X) &= E(X^2) - \{E(X)\}^2 &&\text{(the definition of variance)}\\
\text{so } \operatorname{Var}(X) &= \big[G''(1) + E(X)\big] - \{E(X)\}^2 = G''(1) + G'(1) - \{G'(1)\}^2 &&\text{(substitute } E(X^2) = G''(1) + E(X),\ E(X) = G'(1)\text{)}
\end{aligned}$$

Here: $2 + 1.7 - 1.7^2 = 0.81$ (the middle line is the variance definition from [[Discrete Random Variables]]). The formula is not a rule to memorise; it is what "differentiate twice" *does* to a shelf of hooks — with the $+G'(1)$ putting back the $E(X)$ that the second read subtracted — and the figure above shows all three moves on the same shelf.

**Why the PGF of a sum is a product — polynomial multiplication *is* counting the ways.** Roll two dice. Each has PGF $\tfrac16(t + t^2 + \dots + t^6)$. Multiply the two polynomials: every term of the first meets every term of the second, $t^i \cdot t^j = t^{i+j}$, and like powers collect. The coefficient of $t^7$ collects $t^1 t^6, t^2 t^5, \dots, t^6 t^1$ — six products, each $\tfrac1{36}$ — which is precisely the count of ways to roll $7$. Multiplication sorted all $36$ outcomes by their total without your having to list them; that is the same *count the ways* that runs [[Non-Parametric Tests]] and [[Chi-Squared Tests]], done by algebra. The one-line proof is the algebra behind the picture: $G_{X+Y}(t) = E(t^{X+Y}) = E(t^X\,t^Y) = E(t^X)\,E(t^Y)$ — and that last step, *the expectation of a product is the product of the expectations*, holds **only for independent** variables ([[Linear Combinations of Random Variables]] has the same caveat for variances). It is why Case 4B below is a trap: a sum of two variables that depend on each other has a PGF you must build by hand.

![[pgf-dice-convolution.svg|760]]

**Why the named PGFs look the way they do — build them, do not memorise them.**
- *Discrete uniform on $1, \dots, n$*: every hook carries $\tfrac1n$, so $G(t) = \tfrac1n(t + t^2 + \dots + t^n) = \dfrac{t(1 - t^n)}{n(1 - t)}$ — a geometric series ([[Arithmetic and Geometric Progressions]]).
- *Bernoulli, then binomial*: one trial with success probability $p$ has two hooks, $G(t) = q + pt$. A $B(n, p)$ variable is the sum of $n$ **independent** trials, so by the product rule $G(t) = (q + pt)^n$ — no algebra with $\binom{n}{r}$ needed, and the binomial theorem then *reads off* $P(X = r) = \binom{n}{r} q^{n-r} p^r$ as the coefficient of $t^r$. Differentiate: $G'(t) = np(q + pt)^{n-1}$, so $E(X) = np$; $G''(1) = n(n-1)p^2$, so $\operatorname{Var}(X) = n(n-1)p^2 + np - n^2p^2 = np(1-p)$ — the [[Discrete Random Variables]] results in two lines.
- *Geometric* (trials to the first success, $X = 1, 2, \dots$): $p_x = q^{x-1}p$, so $G(t) = pt\,(1 + qt + q^2t^2 + \dots) = \dfrac{pt}{1 - qt}$ for $\lvert qt \rvert < 1$. Differentiate the quotient: $E(X) = \tfrac1p$ and $\operatorname{Var}(X) = \tfrac{q}{p^2}$.
- *Poisson*: $p_x = e^{-\lambda}\lambda^x/x!$, so $G(t) = e^{-\lambda}\sum \dfrac{(\lambda t)^x}{x!} = e^{-\lambda}e^{\lambda t} = e^{\lambda(t-1)}$ — the exponential series doing the work. Then $G'(t) = \lambda e^{\lambda(t-1)}$ gives $E(X) = \lambda$, $G''(1) = \lambda^2$ gives $\operatorname{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$; and the sum of independent $\mathrm{Po}(\lambda)$ and $\mathrm{Po}(\mu)$ has PGF $e^{(\lambda+\mu)(t-1)}$ — Poisson again, the pooling rule of [[Poisson Distribution]] proved in one line.

**Why you can read a distribution back out.** A PGF is a power series in $t$, and a power series has only one set of coefficients: $P(X = k)$ is the coefficient of $t^k$, which is also $G^{(k)}(0)/k!$ (the Maclaurin coefficient) — so $G(0) = P(X = 0)$, $G'(0) = P(X = 1)$, $\tfrac12 G''(0) = P(X = 2)$. When the PGF is printed as a fraction such as $\dfrac{k}{1 - at^2}$ or $\dfrac{t}{(3 - 2t)^2}$, expand it with the [[Binomial Series]] for negative powers as far as the question needs, and the probabilities appear. Uniqueness cuts the other way too: meet $(\tfrac13 + \tfrac23 t)^{10}$ and you are entitled to say *this is $B(10, \tfrac23)$*, meet $e^{3(t-1)}$ and it is $\mathrm{Po}(3)$.

## The four moves — each with the real cases it exists for

Every PGF question on the paper is one or more of four moves: **build** a PGF from a distribution, **extract** the mean and variance, **read** a probability out of a PGF, and **combine** independent variables by multiplying. Each is stated in a few lines and then run on real Paper 4 questions, worked with the mark-scheme values.

### Move 1 — build the PGF from a distribution

**The tool.** From a table: hang each probability on its hook and add. From a named distribution: use the built forms above. For $Y = aX + b$: $G_Y(t) = t^b G_X(t^a)$. Check $G(1) = 1$.

**Case 1A — a printed polynomial, and a linear change of variable: 9231/43 June 2026 Q3.**

> $X$ has PGF $G_X(t) = 0.1 + 0.3t + 0.4t^2 + 0.2t^3$. **(a)** Use $G_X(t)$ to find $E(X)$ and $\operatorname{Var}(X)$. **[5]** **(b)** $Y = 3X + 2$. Find the PGF of $Y$. **[2]**

*Why this move.* The PGF is given as a polynomial; the four hooks are $x = 0, 1, 2, 3$ with weights $0.1, 0.3, 0.4, 0.2$ (they add to $1$ — check).

**(a)** *Tool: differentiate, then substitute.* $G_X'(t) = 0.3 + 0.8t + 0.6t^2$, so $E(X) = G_X'(1) = 1.7$. $G_X''(t) = 0.8 + 1.2t$, so $G_X''(1) = 2$ and $\operatorname{Var}(X) = 2 + 1.7 - 1.7^2 = 0.81$.

**(b)** *Tool: relabel the hooks.* $Y = 3X + 2$ takes the values $2, 5, 8, 11$ with the *same* probabilities, so $G_Y(t) = 0.1t^2 + 0.3t^5 + 0.4t^8 + 0.2t^{11}$ — which is exactly $t^2 G_X(t^3)$. (Two B1s: correct coefficients, correct powers. Writing $3G_X(t) + 2$ earns neither.)

**Case 1B — build from a bag: 9231/43 June 2025 Q6(a).**

> A bag holds $7$ red and $3$ blue balls; Kieran draws $2$ without replacement. $X$ = number of red balls drawn; $Y$ = number of different colours in the draw. **(a)** Find $G_X(t)$ and $G_Y(t)$. **[4]**

*Why this move.* No named distribution fits (drawing without replacement is [[Permutations and Combinations]] territory), so build each pmf by counting, then hang it.

*Tool: count, then hang.* $\binom{10}{2} = 45$ equally likely pairs. $P(X = 0) = \binom{3}{2}/45 = \tfrac1{15}$; $P(X = 1) = 7 \times 3/45 = \tfrac7{15}$; $P(X = 2) = \binom72/45 = \tfrac7{15}$. So $G_X(t) = \tfrac1{15} + \tfrac7{15}t + \tfrac7{15}t^2$. One colour means both the same: $\tfrac1{15} + \tfrac7{15} = \tfrac8{15}$; two colours $\tfrac7{15}$; so $G_Y(t) = \tfrac8{15}t + \tfrac7{15}t^2$. (Both add to $1$.) — Kieran returns in Case 4B.

### Move 2 — mean and variance from a PGF

**The tool.** $E(X) = G'(1)$; $\operatorname{Var}(X) = G''(1) + G'(1) - \{G'(1)\}^2$. Quotient or chain rule as the shape demands; if the PGF has unknown constants, $G(1) = 1$ is the first equation and a given mean is the second.

**Case 2A — a rational PGF, quotient rule: 9231/42 November 2025 Q6(a).**

> $X$ has PGF $G_X(t) = \dfrac{t}{(3 - 2t)^2}$. **(a)** Find $E(X)$ and $\operatorname{Var}(X)$. **[5]**

*Why this move.* Mean and variance asked directly from a PGF with no unknowns; the shape is a quotient, so it is a differentiation exercise with the MF19 formula at the end. ($G(1) = 1/1 = 1$ — check.)

*Tool: differentiate — quotient rule — then substitute.* $G_X'(t) = \dfrac{(3-2t)^2 + 4t(3-2t)}{(3-2t)^4} = \dfrac{3 + 2t}{(3-2t)^3}$, so $E(X) = G_X'(1) = 5$. Again: $G_X''(t) = \dfrac{2(3-2t)^3 + 6(3+2t)(3-2t)^2}{(3-2t)^6} = \dfrac{24 + 8t}{(3-2t)^4}$, so $G_X''(1) = 32$ and $\operatorname{Var}(X) = 32 + 5 - 25 = 12$. (Both method marks are for *attempting* each derivative — write them out even if the algebra wobbles.)

**Case 2B — unknown constants: two equations from $G(1) = 1$ and the mean: 9231/41 June 2026 Q6(a),(b).**

> $X$ has PGF $G_X(t) = \dfrac{k(at+1)^2}{t}$ and $E(X) = \tfrac13$. **(a)** Show that $a = 2$ and find $k$. **[5]** **(b)** Find $\operatorname{Var}(X)$. **[2]**

*Why this move.* Two unknowns, two facts: total probability and the mean. (Expand it and the variable shows its hooks: $G_X(t) = k t^{-1} + 2ak + ka^2 t$, so $X$ takes the values $-1, 0, 1$ — a PGF can carry a negative power, and the formulas still work.)

**(a)** *Tool: $G(1) = 1$.* $k(a+1)^2 = 1$. *Tool: $G'(1) = E(X)$.* $G_X'(t) = -kt^{-2} + ka^2$, so $ka^2 - k = \tfrac13$. Divide: $\dfrac{a^2 - 1}{(a+1)^2} = \dfrac{a - 1}{a + 1} = \dfrac13$, hence $3a - 3 = a + 1$, $a = 2$; then $k = \tfrac19$.

**(b)** *Tool: the variance formula.* $G_X''(t) = 2kt^{-3}$, so $G_X''(1) = \tfrac29$ and $\operatorname{Var}(X) = \tfrac29 + \tfrac13 - \tfrac19 = \tfrac49$. (Or from the table $P(-1) = \tfrac19$, $P(0) = \tfrac49$, $P(1) = \tfrac49$: $E(X^2) = \tfrac59$, $\operatorname{Var} = \tfrac59 - \tfrac19$ — the scheme takes either.)

**Case 2C — the variance as an identity to *show*: 9231/41 November 2025 Q7(a),(b).**

> $X$ takes $0, 1, 2$ with probabilities $a, 2a, b$. **(a)** Write down $G_X(t)$ and use it to find $E(X)$ in terms of $a$ and $b$. **[2]** **(b)** Show that $\operatorname{Var}(X) = 2b + 2(a+b)(1 - 2a - 2b)$. **[3]**

**(a)** $G_X(t) = a + 2at + bt^2$; $G_X'(t) = 2a + 2bt$; $E(X) = 2a + 2b$.
**(b)** $G_X''(t) = 2b$, so $\operatorname{Var}(X) = 2b + (2a + 2b) - (2a + 2b)^2 = 2b + (2a+2b)\big(1 - (2a + 2b)\big) = 2b + 2(a+b)(1 - 2a - 2b)$. (The scheme's *"shown convincingly"* wants the factorising step visible, not just the two ends.) — this $X$ returns in Case 4A.

### Move 3 — read a probability out of a PGF

**The tool.** $P(X = k)$ is the coefficient of $t^k$: expand a fraction with the binomial series (negative powers), or use $G(0), G'(0), \tfrac12 G''(0), \dots$. Tail probabilities: $P(X > k) = 1 - $ the first few coefficients.

**Case 3A — a fraction with a parameter: 9231/41 June 2025 Q6.**

> $Y$ takes the values $0, 2, 4, \dots$ and $G_Y(t) = \dfrac{k}{1 - at^2}$. **(a)** Find $k$ in terms of $a$. **[1]** **(b)** Show that $P(Y > 2) = a^2$. **[3]** It is now given that $a = 0.2$. **(c)** Find $E(Y)$. **[2]**

*Why this move.* A PGF given as a fraction and a probability asked: expand. ($k$ first, from $G(1) = 1$.)

**(a)** $G_Y(1) = \dfrac{k}{1 - a} = 1$, so $k = 1 - a$.
**(b)** *Tool: the binomial series.* $(1 - at^2)^{-1} = 1 + at^2 + a^2t^4 + \dots$, so $G_Y(t) = k + kat^2 + ka^2 t^4 + \dots$: $P(Y = 0) = k$, $P(Y = 2) = ka$ (the hooks $t^1, t^3, \dots$ are empty — that is what "takes the values $0, 2, 4, \dots$" means). Then $P(Y > 2) = 1 - k(1 + a) = 1 - (1-a)(1+a) = a^2$. (Alternatively $G_Y(0) = k$ and $\tfrac12 G_Y''(0) = ka$ — the derivative route earns the same marks.)
**(c)** $G_Y'(t) = \dfrac{2akt}{(1 - at^2)^2} = \dfrac{0.32t}{(1 - 0.2t^2)^2}$, so $E(Y) = \dfrac{0.32}{0.64} = 0.5$.

**Case 3B — a coefficient hunt in a product: 9231/42 November 2025 Q6(b).**

> With $G_X(t) = \dfrac{t}{(3-2t)^2}$ (Case 2A) and $G_Y(t) = \dfrac{t^2}{(3-2t)^2}$, and $Z = X + Y$ with $X, Y$ independent, find $P(Z > 4)$. **[5]**

*Why this move — and Move 4 first.* Independent, so multiply: $G_Z(t) = \dfrac{t^3}{(3 - 2t)^4}$. Then read: $Z$ starts at $3$ (the $t^3$ in front), so $P(Z > 4) = 1 - P(Z = 3) - P(Z = 4)$ needs only two coefficients.

*Tool: the binomial series for a negative power.* $\dfrac{t^3}{(3-2t)^4} = \dfrac{t^3}{81}\Big(1 - \tfrac23 t\Big)^{-4} = \dfrac{t^3}{81}\Big(1 + 4 \cdot \tfrac23 t + \dots\Big)$. So $P(Z = 3) = \tfrac1{81}$, $P(Z = 4) = \tfrac{8}{243}$, and $P(Z > 4) = 1 - \tfrac1{81} - \tfrac8{243} = \tfrac{232}{243} = 0.955$. (Expand only as far as needed — the scheme's M1 is for *identifying* the coefficient of $t^4$; a full expansion wastes time and invites slips.)

**Case 3C — a probability from a power of a PGF: 9231/41 June 2026 Q6(c).**

> With $G_X(t) = \dfrac{(2t+1)^2}{9t}$ (Case 2B), $Y$ is the sum of three independent observations of $X$. Find $P(Y = 0)$. **[3]**

*Tool: multiply, then read the $t^0$ coefficient.* $G_Y(t) = \dfrac{(2t+1)^6}{729\,t^3}$, and $P(Y = 0)$ is the coefficient of $t^0$ — i.e. of $t^3$ in $(2t+1)^6$: $\binom63 2^3 = 160$. So $P(Y = 0) = \tfrac{160}{729} = 0.219$. (By cases: the seven ways to make three values from $\{-1, 0, 1\}$ add to $0$ — $(0,0,0)$ and the six orderings of $(-1, 0, 1)$ — give $\big(\tfrac49\big)^3 + 6 \cdot \tfrac19 \cdot \tfrac49 \cdot \tfrac49$, the same $\tfrac{160}{729}$. The PGF did the case-count for you.)

### Move 4 — sums of independent variables: multiply, then recognise

**The tool.** Independent $X, Y$: $G_{X+Y} = G_X G_Y$; $n$ independent copies: $G^n$. Then differentiate for the mean (chain rule + $G(1) = 1$), or *recognise* the product as a named PGF. **State the independence** — it is the licence for the multiplication, and it is a marked line.

**Case 4A — ten copies, and a binomial hiding in the product: 9231/41 November 2025 Q7(c),(d).**

> $Y = X_1 + \dots + X_{10}$, ten independent observations of the $X$ of Case 2C. **(c)** Using the PGF of $Y$ and your $E(X)$, show that $E(Y) = 10E(X)$. **[3]** **(d)** For $b = 0$, define fully the distribution of $Y$. **[2]**

**(c)** *Tool: product, then chain rule.* $G_Y(t) = (a + 2at + bt^2)^{10}$, so $G_Y'(t) = 10(a + 2at + bt^2)^9(2a + 2bt)$ and $G_Y'(1) = 10\,(3a + b)^9\,(2a + 2b)$. But $3a + b = 1$ (total probability), so $E(Y) = 10(2a + 2b) = 10E(X)$. (The A1 is for *saying* $3a + b = 1$ — the mark is for knowing why the $9$th power vanishes.)
**(d)** *Tool: recognise.* $b = 0$ forces $a = \tfrac13$, so $G_X(t) = \tfrac13 + \tfrac23 t$ — a Bernoulli hook pair — and $G_Y(t) = \big(\tfrac13 + \tfrac23 t\big)^{10}$ is the PGF of $B(10, \tfrac23)$. Both marks: *binomial*, and *the parameters*.

**Case 4B — the trap: a sum whose parts are not independent: 9231/43 June 2025 Q6(b)–(d).**

> (Continuing Case 1B.) $Z$ = the number of red balls plus the number of different colours. Kieran claims $G_Z(t) = G_X(t)\,G_Y(t)$. **(b)** Explain why he is wrong. **[1]** **(c)** Find $G_Z(t)$ as a polynomial. **[4]** **(d)** Use it to find $E(Z)$. **[2]**

**(b)** $X$ and $Y$ are **not independent** — $Y$ is decided by $X$ (two reds or two blues means one colour; one of each means two). The product rule's licence is missing.
**(c)** *Tool: build the joint outcomes by hand.* $(x, y) = (0, 1)$ with probability $\tfrac1{15}$, giving $z = 1$; $(1, 2)$ with $\tfrac7{15}$, $z = 3$; $(2, 1)$ with $\tfrac7{15}$, $z = 3$. So $G_Z(t) = \tfrac1{15}t + \tfrac{14}{15}t^3$. (Kieran's product would have put weight on $t^2$ and $t^4$ — values $Z$ cannot take.)
**(d)** $G_Z'(t) = \tfrac1{15} + \tfrac{42}{15}t^2$, so $E(Z) = \tfrac{43}{15} = 2.87$.

## Choosing the move

| The question gives… and asks… | Move | The line that carries the mark |
|---|---|---|
| a table or a story → the PGF | build | hooks and weights add to $1$; a named form where one fits |
| a PGF → $E$, $\operatorname{Var}$ | extract | differentiate *then* substitute; keep the $+G'(1)$ |
| a PGF with unknowns | extract | $G(1) = 1$ first, the given mean second |
| a PGF → $P(X = k)$ or a tail | read | binomial series to the needed power; $G(0)$, $G'(0)$ |
| a sum of independent copies → its PGF, mean, name | combine | say *independent*; chain rule with $G(1) = 1$; recognise $(q+pt)^n$, $e^{\lambda(t-1)}$ |
| a sum whose parts depend on each other | combine — by hand | list joint outcomes; never multiply |

## Where the PGF meets the world

- **The surname problem, epidemics and chain reactions — the branching process.** Galton asked in 1873 why aristocratic surnames die out; Watson answered with a PGF. If each person has children according to a distribution with PGF $G(s)$, then the probability the line is extinct after $n$ generations is $G(G(\cdots G(0)))$ — $n$ nestings — and the probability it *ever* dies out is the smallest solution of $q = G(q)$: where the curve meets the diagonal. Mean offspring $\le 1$ gives $q = 1$ (extinction certain, however slowly); mean $> 1$ gives $q < 1$, survival with probability $1 - q$. Replace "children" by *people infected by one case* and $G'(1)$ is $R_0$ — the same fixed point says whether an outbreak fizzles; replace it by *neutrons released per fission* and it is criticality; by *copies of a new mutation* and it is whether the mutation survives. This is a PGF used as a working tool, not an exam device: nothing else prices "does this line survive?" so directly.

![[pgf-branching-tree.mp4]]

![[pgf-branching-extinction.svg|760]]

- **Dice, and the birth of generating functions.** De Moivre in the 1730s wanted the number of ways to roll a total of $k$ with $n$ dice — the coefficient of $t^k$ in $(t + t^2 + \dots + t^6)^n$ — and Euler and Laplace turned the trick into a whole method: encode a sequence as the coefficients of a series, and let algebra do the combinatorics. Modern computer algebra multiplies such polynomials by the fast Fourier transform, so the distribution of a sum of thousands of independent discrete variables is computed by exactly this move.
- **Random sums — insurance and queues.** If $N$ claims arrive in a year (PGF $G_N$) and each claim's size has PGF $G_X$, the total has PGF $G_N\big(G_X(t)\big)$ — a PGF *of* a PGF, and the branching process is the same composition run generation after generation. Actuaries, telecom engineers and epidemiologists modelling superspreading all live in this expression.
- **Physics.** A partition function $Z = \sum e^{-E_i/kT}$ is a generating function over energy states, and the statistical-mechanics shortcut that pulls the internal energy out of it by differentiating — the *Beyond* callout of [[Internal Energy]] shows $U = -\partial \ln Z/\partial\beta$ — is $G'(1) = E(X)$ in a different costume.

## Common Misconceptions (Teaching Notes)

### 1. Substituting $t = 1$ before differentiating
$G_X(1) = 1$ always; its derivative is $0$. **Fix:** differentiate the *function of $t$*, and only then put $t = 1$ — write $G'(t) = \dots$ as a line of its own.

### 2. $\operatorname{Var}(X) = G''(1) - \{G'(1)\}^2$
Missing the middle term. **Fix:** $G''(1)$ is $E[X(X-1)]$, not $E(X^2)$; the $+G'(1)$ repairs the difference. In Case 1A it is the difference between $0.81$ and $-0.89$ — a negative variance is the alarm.

### 3. Multiplying PGFs of dependent variables
Kieran's error (Case 4B): $X$ and $Y$ from the *same* draw. **Fix:** ask *are these separate experiments?* before multiplying; if not, list the joint outcomes and hang $Z$'s probabilities by hand.

### 4. $G_{aX+b}(t) = aG_X(t) + b$
Treating the PGF as if it were $X$. **Fix:** a linear change relabels the hooks: $G_{aX+b}(t) = t^b G_X(t^a)$ — Case 1A's $t^2 G_X(t^3)$.

### 5. Reading $P(X = k)$ as $G(k)$
$G$ takes $t$, not values of $X$. **Fix:** $P(X = k)$ is the *coefficient* of $t^k$ — expand, or use $G^{(k)}(0)/k!$.

### 6. Forgetting that $G(1) = 1$ finds the constant
Leaving $k$ unknown, or "finding" it some harder way. **Fix:** every printed PGF with a $k$ in it — Cases 2B and 3A — is a $G(1) = 1$ line first.

### 7. Expanding the whole series when two terms are asked
Case 3B needs the coefficients of $t^3$ and $t^4$, nothing more. **Fix:** decide which powers you need *before* expanding, and stop there.

## Exam Notes

### Cambridge 9231 — Further Probability & Statistics, §4.5

Three learning objectives, and a PGF question on every recent Paper 4 (6–9 marks, usually the last question):

- **Understand the concept of a PGF and construct and use it for given distributions** — *"including the discrete uniform, binomial, geometric and Poisson distributions"*: build them as above; expect a printed PGF with a constant to find from $G(1) = 1$ (Cases 2B, 3A), or a table to hang (1A, 2C), or a story to count (1B).
- **Use the formulae for the mean and variance in terms of the PGF** — MF19 prints all three lines; the M1s are for *attempting* each derivative (quotient rule for rational PGFs, Case 2A), the A1 for the value; "show that" variance identities (2C) need the factorising step seen.
- **Use the result that the PGF of a sum of independent variables is the product** — ten copies (4A), three copies (3C), two different variables (3B); recognise the product as a named distribution (4A(d)); and be ready for the *"explain why he is wrong"* one-marker when the parts are not independent (4B).
- Recurring shapes: a linear change $Y = aX + b$ (1A(b)); a probability read from a fraction by the binomial series (3A, 3B); a PGF with a negative power of $t$ (2B — the formulas still hold); the mark scheme's *"FT their $k$"* generosity, which makes the $G(1) = 1$ line the most valuable single line on the question.

### Where it is *not* examined

Among the boards this vault covers, **9231 is the only one that examines PGFs** — verified against the syllabus PDFs: **Cambridge 9709** never asks them (its shared MF19 booklet prints the three PGF lines, which is not an invitation); **Edexcel IAL** lists $G(t)$ in its notation appendix but no unit examines it; **OxAQA 9660**'s formula booklet carries a generating-functions page that belongs to its *Further* Mathematics sibling, not to 9660; **AP Statistics**, **IB AA / AI**, **0580** and **0606** have none of it. Outside the vault's boards, UK Edexcel Further Statistics 2 and OCR MEI examine PGFs in the same shape.

### Beyond high school — University

The PGF is the discrete member of a family. Replace $t^X$ by $e^{tX}$ and you have the **moment generating function** $M_X(t) = E(e^{tX})$, whose derivatives at $0$ are the moments $E(X^k)$ directly (no factorial-moment repair) and which works for continuous variables too — the normal's is $e^{\mu t + \sigma^2 t^2/2}$, and multiplying two of them is the cleanest proof that independent normals add to a normal ([[Linear Combinations of Random Variables]] waves at it). Replace $e^{tX}$ by $e^{itX}$ and you have the **characteristic function**, which always exists and carries the standard proof of the central limit theorem ([[Normal Distribution]] names it). All three are the same idea: encode a distribution as a function, so that convolution becomes multiplication and moments become derivatives.

> [!info] Beyond syllabus — why the extinction probability is the *smallest* fixed point, and why mean $\le 1$ means certain extinction
> $G$ is increasing and convex on $[0, 1]$ (its coefficients are non-negative), $G(0) = p_0 \ge 0$, $G(1) = 1$, and $G'(1)$ is the mean number of children. A convex curve through $(1, 1)$ can cross the diagonal at most once more, in $[0, 1)$, and does so exactly when it arrives at $(1, 1)$ *steeper* than the diagonal — $G'(1) > 1$. Starting from $s = 0$ and iterating $s \mapsto G(s)$ climbs monotonically (each step is "extinct by one more generation", and probabilities of nested events cannot fall) and cannot jump the first crossing, so it converges to the smallest fixed point $q$. Mean $\le 1$: no crossing before $1$, so $q = 1$. Mean $> 1$: $q < 1$, and the line survives with probability $1 - q$. Galton and Watson stated it in 1874; Steffensen proved it in 1930.

## Connections

- **Parent:** [[Discrete Random Variables]] — the pmf, $E(X)$, $\operatorname{Var}(X)$, binomial and geometric; the PGF is that card's table written as one expression, and the binomial and geometric results are re-derived here in two lines each.
- **The distributions it packages:** [[Poisson Distribution]] ($e^{\lambda(t-1)}$ and the pooling rule proved by multiplication), [[Discrete Random Variables]] (binomial $(q+pt)^n$, geometric $\tfrac{pt}{1-qt}$).
- **The rules it re-proves:** [[Linear Combinations of Random Variables]] — $E(X+Y) = E(X) + E(Y)$ always, but the product of PGFs (like the sum of variances) needs independence.
- **The algebra it borrows:** [[Binomial Series]] (negative-power expansions for reading probabilities out of fractions), [[Arithmetic and Geometric Progressions]] (the uniform and geometric PGFs), [[Differentiation]] (quotient and chain rules at $t = 1$), [[Permutations and Combinations]] (Case 1B's counting; the coefficient of $t^k$ as a count of ways).
- **The counting it shares:** [[Chi-Squared Tests]] and [[Non-Parametric Tests]] — *count the ways* by hand there, by polynomial multiplication here.
- **For 9231 students:** [[MF19 Reference (9231)]] — $G_X(t) = E(t^X)$, $E(X) = G_X'(1)$ and the variance line are printed; the named PGFs, the product rule and $G_{aX+b}(t) = t^bG_X(t^a)$ are **not** — build them.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $G_X(t) = E(t^X)$ | `G_X(t) = E(t^X)` | the PGF |
| $G_X'(1)$, $G_X''(1)$ | `G_X'(1)`, `G_X''(1)` | mean; second factorial moment |
| $\operatorname{Var}(X) = G_X''(1) + G_X'(1) - \{G_X'(1)\}^2$ | `\operatorname{Var}(X) = G_X''(1) + G_X'(1) - \{G_X'(1)\}^2` | MF19 line |
| $G_{X+Y}(t) = G_X(t)\,G_Y(t)$ | `G_{X+Y}(t) = G_X(t)\,G_Y(t)` | independent only |
| $t^{b}\,G_X(t^{a})$ | `t^{b}\,G_X(t^{a})` | PGF of $aX + b$ |
| $[t^k]\,G_X(t)$ | `[t^k]\,G_X(t)` | coefficient of $t^k$ = $P(X=k)$ |
| $e^{\lambda(t-1)}$, $(q+pt)^n$, $\dfrac{pt}{1-qt}$ | `e^{\lambda(t-1)}`, `(q+pt)^n`, `\dfrac{pt}{1-qt}` | Poisson, binomial, geometric |

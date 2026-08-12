---
chinese: 反函数 (fǎn hánshù)
prerequisites:
  - "[[Function]]"
  - "[[Composite Function]]"
  - "[[Changing the Subject (Vocab)]]"
  - "[[Inverse Operations (Vocab)]]"
  - "[[Reciprocals (Vocab)]]"
leads_to:
  - "[[Differentiation]]"
tags:
  - subject/mathematics
  - domain/functions
  - level/GCSE
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A9
  - syllabus/9260-A9-Ext
  - syllabus/0580-E2-13
  - syllabus/0606-1-5
  - syllabus/0606-1-6
  - syllabus/0606-1-8
  - syllabus/9709-1-2
  - type/definition
  - type/vocabulary
  - type/notation
  - misconception/inverse-vs-reciprocal
  - misconception/every-function-has-inverse
---

# Inverse Function 反函数

## Definition

### Formal

The **inverse function** $f^{-1}$ of a function $f$ reverses the effect of $f$. If $f(a) = b$, then $f^{-1}(b) = a$.

Formally, $f^{-1}$ satisfies:

$$f^{-1}(f(x)) = x \qquad \text{and} \qquad f(f^{-1}(x)) = x$$

or equivalently, using composite notation:

$$f^{-1}f(x) = ff^{-1}(x) = x$$

An inverse function exists **if and only if** $f$ is **one-to-one** (injective): every output comes from exactly one input. Many-to-one functions do **not** have inverses (unless the domain is restricted).

### Intuitive

If a function is a machine that turns inputs into outputs, the inverse function is the machine that **undoes** the process — it turns outputs back into inputs.

![[inverse-function-reflection.svg|700]]

If $f$ turns 5 into 13 (say, by doubling and adding 3), then $f^{-1}$ turns 13 back into 5 (by subtracting 3 and halving). The inverse literally runs the machine backwards.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| inverse function | 反函数 | fǎn hánshù |
| inverse | 逆 / 反 | nì / fǎn |
| one-to-one (injective) | 一对一 / 单射 | yī duì yī / dānshè |
| self-inverse | 自反函数 | zì fǎn hánshù |
| reflection | 反射 | fǎnshè |
| line of symmetry | 对称轴 | duìchèn zhóu |
| horizontal line test | 水平线测试 | shuǐpíng xiàn cèshì |
| restrict the domain | 限制定义域 | xiànzhì dìngyì yù |

> [!tip] 反 — the Chinese captures "reversal"
> 反 means "reverse / opposite". A 反函数 is literally a "reverse function" — it reverses what the original function did. This is more transparent than the English "inverse", which students sometimes confuse with "reciprocal" ($\dfrac{1}{f}$). In Chinese, the reciprocal would be 倒数 (dàoshù, "inverted number") — a completely different word, so the confusion is less likely.

---

## Notation

| Symbol | Meaning | Read as |
|--------|---------|---------|
| $f^{-1}(x)$ | The inverse function of $f$ applied to $x$ | "f inverse of x" |
| $f^{-1}: x \mapsto \ldots$ | Arrow notation for the inverse | "f inverse maps x to ..." |

> [!warning] $f^{-1}(x) \neq \dfrac{1}{f(x)}$
> The superscript $-1$ in function notation means **inverse**, not **reciprocal**. This is a critical distinction:
> - $f^{-1}(x)$ = the function that *undoes* $f$
> - $\dfrac{1}{f(x)}$ = $[f(x)]^{-1}$ = the *reciprocal* of the output
>
> For example, if $f(x) = 2x$, then $f^{-1}(x) = \dfrac{x}{2}$, but $\dfrac{1}{f(x)} = \dfrac{1}{2x}$.

---

## Key Facts

### When does an inverse exist?

A function has an inverse if and only if it is **one-to-one** (each output comes from exactly one input).

**The horizontal line test:** A function is one-to-one if every horizontal line crosses its graph at most once. (This is the companion to the vertical line test for *being* a function.)

| Function | One-to-one? | Inverse exists? |
|----------|-------------|-----------------|
| $f(x) = 3x + 2$ (linear, non-zero gradient) | Yes | Yes |
| $f(x) = x^2$ (full domain $\mathbb{R}$) | No ($f(3) = f(-3) = 9$) | No |
| $f(x) = x^2, \; x \geq 0$ (restricted domain) | Yes | Yes: $f^{-1}(x) = \sqrt{x}$ |
| $f(x) = x^3$ | Yes | Yes: $f^{-1}(x) = \sqrt[3]{x}$ |

> [!note] Why many-to-one functions fail
> If $f(3) = 9$ and $f(-3) = 9$, what should $f^{-1}(9)$ be? It can't be both 3 and $-3$ — that would make $f^{-1}$ one-to-many, which isn't a function. The solution: **restrict the domain** of $f$ so it becomes one-to-one.

### How to find $f^{-1}(x)$: the algebraic method

**Step 1:** Write $y = f(x)$.

**Step 2:** Swap $x$ and $y$ (interchange the roles of input and output).

**Step 3:** Rearrange to make $y$ the subject.

**Step 4:** Write $f^{-1}(x) = \ldots$ (replace $y$ with $f^{-1}(x)$).

### Domain and range swap

The domain and range **swap** between a function and its inverse:

$$\text{Domain of } f^{-1} = \text{Range of } f$$
$$\text{Range of } f^{-1} = \text{Domain of } f$$

This is a direct consequence of "undoing": if $f$ takes inputs from $A$ and produces outputs in $B$, then $f^{-1}$ takes inputs from $B$ and produces outputs in $A$.

### Graphical relationship: reflection in $y = x$

The graph of $y = f^{-1}(x)$ is the **reflection** of the graph of $y = f(x)$ in the line $y = x$.

Why? If the point $(a, b)$ lies on $y = f(x)$ (meaning $f(a) = b$), then $f^{-1}(b) = a$, so the point $(b, a)$ lies on $y = f^{-1}(x)$. Swapping coordinates $(a,b) \to (b,a)$ is exactly reflection in the line $y = x$.

### Self-inverse functions

A function is **self-inverse** if $f^{-1}(x) = f(x)$, i.e. applying it twice returns to the starting value: $f(f(x)) = x$.

Common examples:

| Function | Why it's self-inverse |
|----------|----------------------|
| $f(x) = -x$ | Negating twice returns to original |
| $f(x) = \dfrac{1}{x}$ | Taking reciprocal twice returns to original |
| $f(x) = a - x$ | Subtracting from $a$ twice: $a - (a - x) = x$ |

Graphically, self-inverse functions are **symmetric about the line $y = x$** (reflecting the graph gives the same graph).

---

## Misconceptions

### 1. "$f^{-1}(x)$ means $\dfrac{1}{f(x)}$"

This is the most common error. The $-1$ in $f^{-1}$ is **not** an exponent — it denotes the inverse function. Contrast:

| Notation | Meaning |
|----------|---------|
| $f^{-1}(x)$ | Inverse *function*: undoes $f$ |
| $[f(x)]^{-1} = \dfrac{1}{f(x)}$ | Reciprocal of the *output* |

**Fix:** If $f(x) = 2x + 1$, then $f^{-1}(x) = \dfrac{x-1}{2}$. Check: $f^{-1}(f(3)) = f^{-1}(7) = \dfrac{7-1}{2} = 3$. ✓

### 2. "Every function has an inverse"

Only **one-to-one** functions have inverses. $f(x) = x^2$ on all of $\mathbb{R}$ does not.

**Fix:** Apply the horizontal line test. If any horizontal line crosses the graph more than once, no inverse exists (unless the domain is restricted).

### 3. "Just swap $x$ and $y$ — done!"

Swapping is only Step 2. You must then *rearrange* to isolate $y$. Students sometimes leave the answer as $x = 3y + 2$ instead of $y = \dfrac{x - 2}{3}$.

**Fix:** The final answer must be in the form $f^{-1}(x) = \ldots$ with $x$ on the right-hand side.

### 4. Forgetting to state the domain of $f^{-1}$

If $f$ has a restricted domain, the range of $f$ becomes the domain of $f^{-1}$. For example, if $f(x) = x^2$ for $x \geq 0$, then $f^{-1}(x) = \sqrt{x}$ for $x \geq 0$ — not for all $\mathbb{R}$.

---

## Worked Examples

### Example 1 — Finding an inverse of a linear function (9260 A9 Ext / 0580 E2.13)

$f(x) = 5x - 3$. Find $f^{-1}(x)$.

**Step 1:** Let $y = 5x - 3$.

**Step 2:** Swap $x$ and $y$: $x = 5y - 3$.

**Step 3:** Rearrange for $y$:

$$x + 3 = 5y$$
$$y = \dfrac{x + 3}{5}$$

**Step 4:** $f^{-1}(x) = \dfrac{x + 3}{5}$

**Check:** $f^{-1}(f(2)) = f^{-1}(7) = \dfrac{7 + 3}{5} = \dfrac{10}{5} = 2$ ✓

---

### Example 2 — Inverse of a fraction function (0606 1.6)

$f(x) = \dfrac{2x + 1}{x - 3}, \quad x \neq 3$

Find $f^{-1}(x)$ and state its domain.

**Step 1:** $y = \dfrac{2x + 1}{x - 3}$

**Step 2:** Swap: $x = \dfrac{2y + 1}{y - 3}$

**Step 3:** Rearrange — multiply both sides by $(y - 3)$:

$$x(y - 3) = 2y + 1$$
$$xy - 3x = 2y + 1$$
$$xy - 2y = 3x + 1$$
$$y(x - 2) = 3x + 1$$
$$y = \dfrac{3x + 1}{x - 2}$$

**Step 4:** $f^{-1}(x) = \dfrac{3x + 1}{x - 2}$

**Domain of $f^{-1}$:** The range of $f$ is $\mathbb{R} \setminus \{2\}$ (since $f(x) = 2$ has no solution — check by setting $\dfrac{2x+1}{x-3} = 2$, which gives $2x + 1 = 2x - 6$, i.e. $1 = -6$, a contradiction). So the domain of $f^{-1}$ is $x \neq 2$.

---

### Example 3 — Showing a function has no inverse without restriction (0606 1.5)

$g(x) = x^2 - 4x + 7$. Explain why $g$ does not have an inverse.

$g$ is a quadratic with a positive leading coefficient — its graph is a U-shaped parabola. A horizontal line (e.g. $y = 10$) crosses it twice, so $g$ is **many-to-one** and therefore does not have an inverse on its natural domain.

Alternatively: $g(1) = 1 - 4 + 7 = 4$ and $g(3) = 9 - 12 + 7 = 4$. Since $g(1) = g(3)$ but $1 \neq 3$, $g$ is not one-to-one.

*If the domain is restricted to $x \geq 2$ (from the vertex onwards), $g$ becomes one-to-one and the inverse exists.*

---

### Example 4 — Verifying a self-inverse function (0606)

$f(x) = \dfrac{3 - x}{x + 1}, \quad x \neq -1$

Show that $f$ is self-inverse.

We need to show $f(f(x)) = x$:

$$f(f(x)) = f\!\left(\dfrac{3 - x}{x + 1}\right) = \dfrac{3 - \dfrac{3-x}{x+1}}{\dfrac{3-x}{x+1} + 1}$$

Simplify the numerator:

$$3 - \dfrac{3-x}{x+1} = \dfrac{3(x+1) - (3-x)}{x+1} = \dfrac{3x + 3 - 3 + x}{x+1} = \dfrac{4x}{x+1}$$

Simplify the denominator:

$$\dfrac{3-x}{x+1} + 1 = \dfrac{3 - x + x + 1}{x+1} = \dfrac{4}{x+1}$$

Divide:

$$f(f(x)) = \dfrac{\dfrac{4x}{x+1}}{\dfrac{4}{x+1}} = \dfrac{4x}{4} = x$$

Therefore $f(f(x)) = x$, so $f$ is self-inverse: $f^{-1} = f$. ✓

---

## Exam Notes

### 9260

- Extension: "inverse function $f^{-1}$" — find inverses algebraically and use them.
- Typically linear or simple rational functions.
- May ask "find $f^{-1}(7)$" directly (substitute into the inverse, or solve $f(x) = 7$).

### 0580 (E2.13)

- "Understand and find inverse functions $f^{-1}(x)$."
- The algebraic swap-and-rearrange method is expected.
- Functions will be linear or simple rational (no quadratics requiring domain restriction).

### 0606 (1.5, 1.6, 1.8)

- **1.5:** "Explain in words why a given function does not have an inverse" — answer: it is many-to-one (give a specific pair of inputs with the same output).
- **1.6:** "Find the inverse of a one-to-one function" — correct notation required ($f^{-1}(x) = \ldots$).
- **1.8:** "Use sketch graphs to show the relationship between a function and its inverse" — the graph of $f^{-1}$ is the reflection of $f$ in $y = x$. You may be asked to sketch both on the same axes.
- Domain/range swaps are explicitly tested.

### Common exam phrasing

| Exam says | They want |
|-----------|-----------|
| "Find $f^{-1}(x)$" | Use the swap-and-rearrange method |
| "Find $f^{-1}(5)$" | Either substitute into $f^{-1}$, or solve $f(x) = 5$ |
| "State the domain of $f^{-1}$" | This is the range of $f$ |
| "Explain why $f$ does not have an inverse" | Show $f$ is many-to-one (give two inputs with same output) |
| "On the same axes, sketch $f$ and $f^{-1}$" | Reflect $f$ in $y = x$; include the line $y = x$ as dashed |
| "Show that $f$ is self-inverse" | Prove $f(f(x)) = x$ |

---

## Connections

### Prerequisites
- **[[Function]]** — domain, range, one-to-one vs many-to-one
- **[[Composite Function]]** — the inverse is defined by $ff^{-1} = f^{-1}f = \text{identity}$

### Leads to
- **[[Differentiation]]** — the derivative of an inverse function: $\left(f^{-1}\right)'(x) = \dfrac{1}{f'(f^{-1}(x))}$ (IB/AP)

### Related cards
- **[[Inverse Matrix]]** — the matrix analogue: $AA^{-1} = I$. The parallel is exact — a matrix inverse "undoes" a transformation, just as a function inverse undoes a function.
- **[[Matrix Transformations]]** — if $f$ is a linear transformation, $f^{-1}$ corresponds to the inverse matrix.

---

## Beyond Syllabus

### AP / IB / A-Level depth

**Restricting the domain to create an inverse**

The standard example: $f(x) = x^2$ has no inverse on $\mathbb{R}$. But restricting to $x \geq 0$ gives $f^{-1}(x) = \sqrt{x}$, and restricting to $x \leq 0$ gives $f^{-1}(x) = -\sqrt{x}$.

For $f(x) = \sin x$ on $\mathbb{R}$, the function is many-to-one (it repeats every $2\pi$). Restricting to $-\dfrac{\pi}{2} \leq x \leq \dfrac{\pi}{2}$ gives the inverse $\arcsin x$. This is why the range of $\arcsin$ is $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$ — it's the restricted domain of $\sin$.

**Derivative of an inverse function**

If $f$ is differentiable and one-to-one with $f'(f^{-1}(x)) \neq 0$, then:

$$\left(f^{-1}\right)'(x) = \dfrac{1}{f'(f^{-1}(x))}$$

Graphical interpretation: the gradient of $f^{-1}$ at a point is the reciprocal of the gradient of $f$ at the corresponding reflected point. Since reflection in $y = x$ swaps the rise and run, this makes geometric sense.

### Beyond high school — University

**Bijections and invertibility**

In university mathematics, a function $f: A \to B$ is **invertible** if and only if it is a **bijection** — both injective (one-to-one) and surjective (onto, meaning every element of $B$ is hit). The surjectivity condition is automatically satisfied if we define $B$ to be the range of $f$, which is why at IGCSE level we only check injectivity.

**Left inverses and right inverses**

If $f$ is injective but not surjective, it has a **left inverse** ($g \circ f = \text{id}$) but not a right inverse. If surjective but not injective, it has a **right inverse** but not a left inverse. A bijection has both, and they are equal — this is the unique inverse $f^{-1}$.

This generalises to linear algebra: a matrix has a left inverse if it has full column rank and a right inverse if it has full row rank. Only square matrices of full rank have both (the standard inverse $A^{-1}$).

---

## LaTeX Reference

| Notation | LaTeX | Rendered |
|----------|-------|----------|
| Inverse function | `f^{-1}(x)` | $f^{-1}(x)$ |
| Inverse composition | `f^{-1}(f(x)) = x` | $f^{-1}(f(x)) = x$ |
| Maps-to (inverse) | `f^{-1}: x \mapsto \dfrac{x+3}{5}` | $f^{-1}: x \mapsto \dfrac{x+3}{5}$ |
| Set minus | `\mathbb{R} \setminus \{2\}` | $\mathbb{R} \setminus \{2\}$ |
| Domain restriction | `x \geq 0` | $x \geq 0$ |

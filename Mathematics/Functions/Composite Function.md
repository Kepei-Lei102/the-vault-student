---
chinese: 复合函数 (fùhé hánshù)
prerequisites:
  - "[[Function]]"
leads_to:
  - "[[Inverse Function]]"
  - "[[Chain Rule]]"
  - "[[Graphs of Functions]]"
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
  - syllabus/0606-1-7
  - syllabus/9709-1-2
  - type/definition
  - type/vocabulary
  - type/notation
  - misconception/order-of-composition
  - misconception/fg-means-f-times-g
---

# Composite Function 复合函数

## Definition

### Formal

The **composite function** $fg$ is defined as:

$$fg(x) = f(g(x))$$

This means: **apply $g$ first**, then **apply $f$ to the result**.

If $g: A \to B$ and $f: B \to C$, then the composite $fg: A \to C$.

The domain of $fg$ is the set of all $x$ in the domain of $g$ such that $g(x)$ is in the domain of $f$. In set notation:

$$\text{Domain of } fg \subseteq \text{Domain of } g$$

### Intuitive

Composing functions is like **chaining two machines together**. The output of the first machine becomes the input of the second.

![[composite-function-chain.svg|700]]

If machine $g$ doubles a number and machine $f$ adds 3, then chaining $g$ then $f$ means: double first, add 3 second. The *order matters* — adding 3 first, then doubling, gives a different answer.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| composite function | 复合函数 | fùhé hánshù |
| compose | 复合 / 组合 | fùhé / zǔhé |
| "f of g of x" | f(g(x)) | |
| order of operations | 运算顺序 | yùnsuàn shùnxù |
| inner function | 内函数 | nèi hánshù |
| outer function | 外函数 | wài hánshù |

> [!tip] 复合 — the Chinese reveals the structure
> 复 means "repeat / compound" and 合 means "combine / join together". A composite function is literally a *compound joining* of two functions — one layered on top of the other. The terms 内函数 (inner function) and 外函数 (outer function) make the layering structure explicit: $g$ is the inner function (applied first, closer to $x$), and $f$ is the outer function (applied second, wrapped around the result).

---

## Notation

| Symbol | Meaning | Read as |
|--------|---------|---------|
| $fg(x)$ | $f(g(x))$ — apply $g$ first, then $f$ | "f of g of x" |
| $gf(x)$ | $g(f(x))$ — apply $f$ first, then $g$ | "g of f of x" |
| $f^2(x)$ | $f(f(x))$ — apply $f$ twice | "f of f of x" |
| $f \circ g$ | Same as $fg$ (university notation) | "f composed with g" |

> [!warning] Reading order vs application order
> $fg(x)$ is read **left to right** as "f, g, x" — but the functions are **applied right to left**: $g$ first, then $f$. Think of the brackets: in $f(g(x))$, the innermost operation ($g$) happens first.

**Critical rule for 0606:** The notation $f^2(x)$ means $f(f(x))$, **not** $[f(x)]^2$. Cambridge 0606 explicitly states that $f^2(x)$ will not be used with trigonometric functions (to avoid confusion with $\sin^2 x$).

---

## Key Facts

### Order matters: $fg \neq gf$ in general

This is the single most important fact about composition. Let $f(x) = x + 3$ and $g(x) = 2x$:

$$fg(x) = f(g(x)) = f(2x) = 2x + 3$$

$$gf(x) = g(f(x)) = g(x + 3) = 2(x + 3) = 2x + 6$$

Since $2x + 3 \neq 2x + 6$, we have $fg \neq gf$.

> [!note] When *does* $fg = gf$?
> Special cases exist. For example, $f(x) = x + 2$ and $g(x) = x + 5$ give $fg(x) = gf(x) = x + 7$. This happens because addition is commutative. But don't assume it — always check.

### How to compute $fg(x)$: the substitution method

**Step 1:** Write down $f(x)$.

**Step 2:** Everywhere you see $x$ in $f$, replace it with the *entire expression* $g(x)$.

**Step 3:** Simplify.

This is pure substitution — the same skill used when evaluating $f(a-1)$ in the [[Function]] card.

### Domain of a composite

For $fg(x) = f(g(x))$ to be defined:

1. $x$ must be in the domain of $g$ (so $g(x)$ exists)
2. $g(x)$ must be in the **range** of $g$ that lies within the domain of $f$ (so $f$ can process the output of $g$)

The domain of $fg$ is therefore: $\{x : x \in \text{Dom}(g) \text{ and } g(x) \in \text{Dom}(f)\}$.

At 9260 and 0580, domain restrictions for composites are rarely tested. At 0606, they are explicitly in the syllabus (1.2 note: "The domain of f may need to be restricted for $f^{-1}$ and/or $gf$ to exist").

---

## Misconceptions

> [!tip] The common thread
> Nearly every misconception below comes from being **lazy with parentheses**. One extra pair of brackets — writing $f(g(x))$ instead of $fg(x)$ — makes the order obvious, prevents the multiplication misread, and forces you to substitute the *whole* expression. When in doubt, add more parentheses than you think you need.
>
> This is a real lesson that carries into programming too: explicit parentheses make code readable even when they're technically redundant. If you want someone new to an area to understand your work, see things from their perspective — and parentheses are how you do that.

### 1. "$fg(x)$ means $f(x) \times g(x)$"

This is the most common and most dangerous mistake. The notation $fg(x)$ means $f(g(x))$ — composition, **not** multiplication.

**Fix:** If the exam means multiplication, it writes $f(x) \cdot g(x)$ or $f(x)g(x)$ with both arguments shown. When you see $fg(x)$ with only one argument, it always means composition.

### 2. "Apply $f$ first because it comes first in $fg$"

No — $g$ is applied first. In $fg(x) = f(g(x))$, work from the inside out: $g$ acts on $x$ first, then $f$ acts on the result.

**Fix:** Read the brackets: $f(\underbrace{g(x)}_{\text{do this first}})$. The innermost function always goes first.

### 3. "You can always swap the order"

Students sometimes assume $fg = gf$. This is false in general — composition is **not commutative**.

**Fix:** Test with numbers. $f(x) = x^2$, $g(x) = x + 1$:
- $fg(3) = f(4) = 16$
- $gf(3) = g(9) = 10$

Different results → order matters.

> [!tip] The same logic shows up in [[Graphs of Functions]]
> Stacking graph transformations is function composition in disguise. "Shift right 2 then stretch vertically by 3" and "stretch vertically by 3 then shift right 2" give the same graph only because those two particular transformations commute. In general — especially when the horizontal transformations mix — the order is load-bearing, and the composite-function-chain diagram above is exactly the picture.

### 4. Forgetting to substitute the entire expression

When computing $fg(x)$ where $f(x) = 3x^2$ and $g(x) = x + 2$, students sometimes write $3(x + 2)$ instead of $3(x+2)^2$.

**Fix:** Replace *every* $x$ in $f$ with the *whole* of $g(x)$. If $f(x) = 3x^2$, then $f(\text{anything}) = 3(\text{anything})^2$.

---

## Worked Examples

### Example 1 — Basic composition (9260 A9 Ext)

$f(x) = 3x + 1$ and $g(x) = x^2$

**(a)** Find $fg(x)$.

$$fg(x) = f(g(x)) = f(x^2) = 3(x^2) + 1 = 3x^2 + 1$$

**(b)** Find $gf(x)$.

$$gf(x) = g(f(x)) = g(3x + 1) = (3x + 1)^2 = 9x^2 + 6x + 1$$

**(c)** Find $fg(2)$.

Using part (a): $fg(2) = 3(2)^2 + 1 = 3(4) + 1 = 13$

Or step by step: $g(2) = 4$, then $f(4) = 3(4) + 1 = 13$. ✓

---

### Example 2 — Composition with fractions (0606 1.7 / 0580 E2.13)

$f(x) = \dfrac{3}{x + 2}$ and $g(x) = (3x + 5)^2$

Find $fg(x)$.

$$fg(x) = f(g(x)) = f\!\left((3x+5)^2\right) = \dfrac{3}{(3x+5)^2 + 2}$$

---

### Example 3 — Solving a composite equation (0606 / 9260 Ext)

$f(x) = 2x - 5$ and $g(x) = x^2 + 1$. Solve $fg(x) = 13$.

**Step 1:** Find $fg(x)$.

$$fg(x) = f(g(x)) = f(x^2 + 1) = 2(x^2 + 1) - 5 = 2x^2 + 2 - 5 = 2x^2 - 3$$

**Step 2:** Solve $2x^2 - 3 = 13$.

$$2x^2 = 16$$
$$x^2 = 8$$
$$x = \pm 2\sqrt{2}$$

---

### Example 4 — $f^2(x)$ (0606 1.3)

$f(x) = 2x + 1$. Find $f^2(x)$.

$$f^2(x) = f(f(x)) = f(2x + 1) = 2(2x + 1) + 1 = 4x + 2 + 1 = 4x + 3$$

Note: $f^2(x) = 4x + 3$, whereas $[f(x)]^2 = (2x+1)^2 = 4x^2 + 4x + 1$. These are completely different.

---

## Exam Notes

### 9260

- Extension only: "understand and find the composite function $fg$".
- Questions typically provide two linear functions and ask for $fg(x)$ and/or $gf(x)$.
- May ask "show that $fg \neq gf$" by evaluating at a specific value.

### 0580 (E2.13)

- "Form composite functions as defined by $gf(x) = g(f(x))$."
- Note: Candidates are **not** expected to find domains and ranges of composite functions.
- May include mapping diagrams.

### 0606 (1.7)

- "Form and use composite functions. Understand that order of functions is important, i.e. $fg$ may not be the same as $gf$."
- $f^2(x) = f(f(x))$ notation is used (but not with trig functions).
- Domain restrictions may be tested: the domain of $gf$ requires $f(x) \in \text{Dom}(g)$.

### Common exam phrasing

| Exam says | They want |
|-----------|-----------|
| "Find $fg(x)$" | Compute $f(g(x))$ — substitute $g(x)$ into $f$ |
| "Find $gf(3)$" | Evaluate: first find $f(3)$, then apply $g$ |
| "Solve $fg(x) = k$" | Find the composite expression, set it equal to $k$, solve |
| "Show that $fg(x) \neq gf(x)$" | Find both and show they are different expressions |
| "Find $f^2(x)$" | Compute $f(f(x))$ |

---

## Connections

### Prerequisites
- **[[Function]]** — you must understand $f(x)$ notation and evaluation before composing functions

### Leads to
- **[[Inverse Function]]** — the inverse $f^{-1}$ is defined by the property $ff^{-1}(x) = x$ (a special composite)
- **[[Chain Rule]]** — differentiating a composite function: $\dfrac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

### Related cards
- **[[Differentiation]]** — uses $f(x)$ notation throughout; composite differentiation requires the Chain Rule

---

## Beyond Syllabus

### AP / IB / A-Level depth

**Composition and domain restrictions**

At higher levels, domain restrictions become a genuine concern. Consider:

$$f(x) = \sqrt{x}, \qquad g(x) = -x^2$$

Individually, $f$ has domain $x \geq 0$ and $g$ has domain $\mathbb{R}$. But $fg(x) = f(-x^2) = \sqrt{-x^2}$, which is only defined when $-x^2 \geq 0$, i.e. $x = 0$. So the domain of $fg$ is just $\{0\}$, even though both individual functions have large domains.

The 0606 syllabus explicitly notes: "Domain $gf \subseteq$ Domain $f$" and "Range $gf \subseteq$ Range $g$" — important constraints to check.

**Associativity of composition**

Composition is **associative**: $f(gh) = (fg)h$. This means we can write $fgh$ without ambiguity — but it is **not commutative** ($fg \neq gf$ in general).

This algebraic structure (associative but not commutative) is the same structure as matrix multiplication — which is no coincidence, since linear transformations *are* functions, and composing them corresponds to multiplying their matrices. See [[Matrix Transformations]] and [[Combination of Transformations]].

### Beyond high school — University

**Composition in computer science**

Function composition is a fundamental operation in programming. In functional languages:

```
compose f g x = f (g x)
```

This is identical to the mathematical definition $fg(x) = f(g(x))$. The Unix pipe operator works the same way: `cat file | sort | uniq` composes three functions in sequence (though the reading order is left-to-right, opposite to mathematical convention). See the [[Function#Everything is IO — 媒介学 (méijiè xué)|媒介学 section in the Function card]] — composition is the mathematical formalisation of IO chaining, the idea that the output of one process becomes the input of the next.

**Function composition in category theory** provides the foundation for all of abstract mathematics: a "category" is any collection of objects with composable arrows (morphisms) between them, where composition is associative and every object has an identity arrow.

---

## LaTeX Reference

| Notation | LaTeX | Rendered |
|----------|-------|----------|
| Composite | `fg(x) = f(g(x))` | $fg(x) = f(g(x))$ |
| Composition operator | `f \circ g` | $f \circ g$ |
| Iterated | `f^2(x) = f(f(x))` | $f^2(x) = f(f(x))$ |
| Domain subset | `\text{Dom}(fg) \subseteq \text{Dom}(g)` | $\text{Dom}(fg) \subseteq \text{Dom}(g)$ |

---
chinese: 函数 (hánshù)
prerequisites:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Set]]"
  - "[[Set-Builder Notation]]"
leads_to:
  - "[[Composite Function]]"
  - "[[Inverse Function]]"
  - "[[Graphs of Functions]]"
  - "[[Differentiation]]"
  - "[[Limit]]"
  - "[[Numerical Methods]]"
  - "[[Trigonometric Functions]]"
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
  - syllabus/0580-E2-13
  - syllabus/0606-1-1
  - syllabus/0606-1-2
  - syllabus/0606-1-3
  - syllabus/0606-1-8
  - syllabus/9709-1-2
  - type/definition
  - type/vocabulary
  - type/notation
  - misconception/function-vs-equation
  - misconception/one-to-one-vs-many-to-one
---

# Function 函数

## Definition

### Formal

A **function** is a rule that assigns **exactly one output** to each input in its domain.

If $f$ is a function, $x$ is an input, and $y$ is the corresponding output, we write:

$$f: x \mapsto y \qquad \text{or equivalently} \qquad y = f(x)$$

Three components fully specify a function:

1. **Domain** — the set of all permitted inputs
2. **Rule** — the operation performed on each input
3. **Range** (image set) — the set of all actual outputs

A function must satisfy the **vertical line test**: every vertical line crosses the graph at **most once**. This guarantees each input maps to exactly one output.

### Intuitive

A function is a **machine**: you feed it an input, it does something to it, and it produces exactly one output. The key word is *exactly one* — for any input you put in, you always get the same single answer back.

![[function-machine.svg|700]]

Think of a vending machine: you press button B3 (input), and you always get the same snack (output). If pressing B3 sometimes gave you crisps and sometimes gave you chocolate, the machine would be broken — and it wouldn't be a function.

> [!tip] "But wait — Python functions can return multiple values!"
> If you've written Python, you've seen `return x, y` — one function, two outputs. Doesn't that break the rule?
>
> Not really. Python is quietly packing those values into a single **tuple** `(x, y)`, so the function still returns *one object*. But the deeper point is real: **in computer science and engineering, "function" is used more loosely than in pure mathematics.** A programming function can accept multiple inputs, produce multiple outputs, print to the screen, modify files, or even crash your computer — mathematicians would not call most of these "functions" at all.
>
> The strict mathematical definition — one input set, one output per input, no side effects — is what this card is about. The broader concept lives in [[#Beyond Syllabus]].

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| function | 函数 | hánshù |
| input | 输入 / 自变量 | shūrù / zìbiànliàng |
| output | 输出 / 因变量 | shūchū / yīnbiànliàng |
| domain | 定义域 | dìngyì yù |
| range / image set | 值域 | zhí yù |
| mapping | 映射 | yìngshè |
| one-to-one (injective) | 一对一 / 单射 | yī duì yī / dānshè |
| many-to-one | 多对一 | duō duì yī |
| one-to-many | 一对多 | yī duì duō |
| vertical line test | 垂直线测试 | chuízhí xiàn cèshì |
| medium / mediation | 媒介 | méijiè |
| mediology (study of media) | 媒介学 | méijiè xué |
| Cartesian product | 笛卡尔积 | Díkǎ'ěr jī |

> [!tip] 函数 — the Chinese name reveals the meaning
> 函 means "to contain" and 数 means "number". A function *contains a number* — it holds a value inside, waiting for you to specify *which* value by giving an input. The formal Chinese for input/output is even more transparent: 自变量 means "self-changing quantity" (the independent variable you choose), and 因变量 means "because-changing quantity" (the dependent variable that changes *because of* your choice).

---

## Notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| $f(x)$ | "f of x" — the output when input is $x$ | $f(x) = 2x + 3$ |
| $f: x \mapsto 2x + 3$ | "f maps x to $2x + 3$" — arrow notation | Equivalent to the above |
| $f(3)$ | Evaluate: substitute $x = 3$ | $f(3) = 2(3) + 3 = 9$ |
| $f: A \to B$ | $f$ maps from set $A$ to set $B$ | $f: \mathbb{R} \to \mathbb{R}$ |
| Domain of $f$ | Set of all valid inputs | Written as $\{x : x \in \mathbb{R}, x \neq 0\}$ |
| Range of $f$ | Set of all actual outputs | Written as $\{y : y > 0\}$ |

> [!warning] $f(x)$ is **not** $f$ times $x$
> In function notation, the parentheses mean "applied to", not "multiplied by". This is a critical distinction: $f(x) = x^2$ means "the function $f$ applied to $x$ gives $x^2$", not "$f$ times $x$ equals $x^2$".

**Two notations — same meaning:**

| Style | Example | Used by |
|-------|---------|---------|
| $f(x) = \ldots$ | $f(x) = 3x - 1$ | 9260, 0580, 0606, IB, AP |
| $f: x \mapsto \ldots$ | $f: x \mapsto 3x - 1$ | 0606 (primary), IB |

The arrow notation $\mapsto$ (read "maps to") emphasises that $f$ is a *mapping* — a process that sends each input to an output. Cambridge 0606 uses both notations and may mix them in the same question.

---

## Key Facts

### Types of mapping

Not every mapping is a function. There are four types:

| Type | Description | Function? | Example |
|------|-------------|-----------|---------|
| **One-to-one** (injective) | Each input → unique output; no two inputs share an output | Yes | $f(x) = 2x + 1$ |
| **Many-to-one** | Multiple inputs can share the same output | Yes | $f(x) = x^2$ (both $3$ and $-3$ give $9$) |
| **One-to-many** | One input → multiple outputs | **No** | $y^2 = x$ (input $4$ → outputs $2$ and $-2$) |
| **Many-to-many** | Multiple inputs → multiple outputs | **No** | $x^2 + y^2 = 25$ (a circle) |

**The rule:** A mapping is a function if and only if it is **one-to-one** or **many-to-one** — every input produces *exactly one* output.

### Domain and range

The **domain** is the set of inputs for which the function is defined. If no domain is stated, assume the **largest possible subset of $\mathbb{R}$** (the real numbers).

Common restrictions:

| Situation | Restriction | Example |
|-----------|-------------|---------|
| Denominator = 0 | Exclude values that make the denominator zero | $f(x) = \dfrac{1}{x-3}$ → domain: $x \neq 3$ |
| Square root of negative | Exclude values that make the expression under $\sqrt{\phantom{x}}$ negative | $f(x) = \sqrt{x - 2}$ → domain: $x \geq 2$ |
| $\ln$ of non-positive | Exclude $x \leq 0$ | $f(x) = \ln(x)$ → domain: $x > 0$ |

The **range** is the set of all actual outputs — every value that $f(x)$ actually takes. Finding the range often requires sketching the graph or reasoning about the function's behaviour.

> [!example] Domain and range of $f(x) = x^2$
> - **Domain:** all real numbers, $\mathbb{R}$ (you can square anything)
> - **Range:** $f(x) \geq 0$ (squaring always gives a non-negative result)
>
> Even though the domain is all of $\mathbb{R}$, the range is only the non-negative reals — $f$ never outputs a negative number.

### The vertical line test

A graph represents a function if and only if **every vertical line** crosses it **at most once**.

Why? A vertical line at $x = a$ hits every point with that $x$-value. If it hits the graph twice, the input $a$ would produce two outputs — violating the definition of a function.

| Passes VLT | Fails VLT |
|-----------|-----------|
| Straight lines (non-vertical) | Circles: $x^2 + y^2 = r^2$ |
| Parabolas: $y = x^2$ | Sideways parabolas: $x = y^2$ |
| Cubics: $y = x^3$ | Ellipses |

> [!note] Vertical lines themselves
> The line $x = 3$ is not a function (it fails its own vertical line test — infinitely many $y$-values for one $x$-value). Horizontal lines like $y = 5$ *are* functions — every input maps to the same output.

### Evaluating a function

To find $f(a)$, replace every $x$ in the rule with $a$:

**If $f(x) = 3x^2 - 2x + 1$, find $f(-2)$:**

$$f(-2) = 3(-2)^2 - 2(-2) + 1 = 3(4) + 4 + 1 = 12 + 4 + 1 = 17$$

You can also evaluate at expressions: $f(a + 1)$ means replace $x$ with $(a + 1)$:

$$f(a + 1) = 3(a+1)^2 - 2(a+1) + 1$$

---

## Misconceptions

### 1. "A function is the same as an equation"

Not quite. An equation like $2x + 3 = 11$ is a statement that is true for specific values of $x$. A function $f(x) = 2x + 3$ is a *rule* — it works for every $x$ in the domain, producing a different output each time.

**Fix:** An equation asks "which $x$ makes this true?" A function asks "what does this $x$ produce?"

### 2. "The domain is always all real numbers"

Only if nothing goes wrong. When the function involves division, square roots, or logarithms, you must check for values that would cause problems (division by zero, square root of negative, log of non-positive).

**Fix:** Always ask: "What inputs would *break* this machine?"

### 3. "$f(x)$ means $f$ multiplied by $x$"

This is the most dangerous misread for students encountering function notation for the first time. The parentheses in $f(x)$ are **not** multiplication brackets.

**Fix:** Read $f(x)$ as "f *of* x" — the output of function $f$ when the input is $x$. Compare: $f(3) = 9$ means "the function $f$, given input $3$, produces $9$" — not "$f$ times $3$ equals $9$".

### 4. "Many-to-one means it's not a function"

Students sometimes think every input must give a *unique* output. That's the definition of *one-to-one* (injective), which is a special *type* of function — not a requirement for being a function at all.

**Fix:** $f(x) = x^2$ is a perfectly valid function. Both $x = 3$ and $x = -3$ give $f(x) = 9$. That's fine — the rule is "each *input* gives exactly one output", not "each *output* comes from exactly one input".

### 5. Confusing "range" with "codomain"

At IGCSE level, "range" means the set of values $f(x)$ actually takes (also called the **image set**). In university mathematics, the *codomain* is the set the outputs are allowed to live in (which may be larger). For now, range = image set = actual outputs.

---

## Worked Examples

### Example 1 — Evaluating and finding inputs (9260 A9)

$f(x) = 4x - 7$

**(a)** Find $f(5)$.

$$f(5) = 4(5) - 7 = 20 - 7 = 13$$

**(b)** Find $f(-3)$.

$$f(-3) = 4(-3) - 7 = -12 - 7 = -19$$

**(c)** Find $x$ when $f(x) = 21$.

Set the output equal to 21 and solve:

$$4x - 7 = 21$$
$$4x = 28$$
$$x = 7$$

---

### Example 2 — Domain and range from a rule (0606 1.2 / 0580 E2.13)

$f(x) = \dfrac{3}{x - 2}$

**(a)** State the domain of $f$.

The denominator cannot be zero: $x - 2 \neq 0$, so $x \neq 2$.

$$\text{Domain: } \{x : x \in \mathbb{R}, x \neq 2\}$$

**(b)** State the range of $f$.

As $x$ varies over the domain, $\dfrac{3}{x-2}$ takes every real value *except* zero (the fraction can be as large or small as you like, but the numerator $3$ ensures the output is never zero).

$$\text{Range: } \{y : y \in \mathbb{R}, y \neq 0\}$$

---

### Example 3 — Identifying functions from mapping diagrams (9260 A9 Core)

Determine whether each mapping is a function:

**(a)** $\{(1, 4), (2, 5), (3, 6), (4, 7)\}$

Each input appears exactly once → **Yes, it is a function** (one-to-one).

**(b)** $\{(1, 3), (2, 3), (3, 5), (4, 5)\}$

Inputs 1 and 2 both map to 3; inputs 3 and 4 both map to 5. Each input still has exactly one output → **Yes, it is a function** (many-to-one).

**(c)** $\{(1, 2), (1, 5), (3, 4)\}$

Input 1 maps to both 2 and 5 → **No, not a function** (one-to-many).

---

### Example 4 — Evaluating at an expression (0606 1.3)

$f(x) = 2x^2 - x + 3$. Find $f(a - 1)$ in terms of $a$.

Replace every $x$ with $(a - 1)$:

$$f(a - 1) = 2(a-1)^2 - (a-1) + 3$$

Expand:

$$= 2(a^2 - 2a + 1) - a + 1 + 3$$

$$= 2a^2 - 4a + 2 - a + 4$$

$$= 2a^2 - 5a + 6$$

---

## Exam Notes

### 9260

- **Core:** Interpret simple expressions as functions with inputs and outputs — the exam may present a flow diagram or word description and ask you to write the function rule, or give you the rule and ask for specific outputs.
- **Extension:** Use $f(x)$ notation, state domain and range, and recognise whether a mapping is a function. This is the gateway to composite and inverse functions.

### 0580 (E2.13)

- Understand functions, domain, range, and use function notation.
- Mapping diagrams may appear — you must identify whether a mapping is a function.
- Questions typically give $f(x) = \ldots$ and ask you to evaluate or solve $f(x) = k$.

### 0606 (1.1–1.3)

- Both $f(x) = \ldots$ and $f: x \mapsto \ldots$ notations are used.
- Includes explaining in words **why** a given rule is or is not a function (1.1 note).
- Domain restrictions and range-finding are tested explicitly.
- The distinction between one-to-one and many-to-one matters here because it determines whether an inverse exists.

### Common exam phrasing

| Exam says | They want |
|-----------|-----------|
| "Find $f(3)$" | Substitute $x = 3$ into $f(x)$ |
| "Solve $f(x) = 10$" | Set $f(x) = 10$ and solve for $x$ |
| "State the domain of $f$" | List all valid inputs (watch for $\div 0$, $\sqrt{\text{neg}}$, $\ln(\leq 0)$) |
| "Find the range of $f$" | Find all possible outputs (sketch helps) |
| "Explain why $f$ is a function" | Show every input gives exactly one output |
| "Explain why this mapping is not a function" | Show an input that gives more than one output |

---

## Connections

### Prerequisites
This card is a starting point — no prerequisites needed. Students should be comfortable with substitution and basic algebra.

### Leads to
- **[[Composite Function]]** — combining two functions: $fg(x)$ means "apply $g$ first, then $f$"
- **[[Inverse Function]]** — undoing a function: $f^{-1}$ reverses $f$
- **[[Differentiation]]** — the derivative $f'(x)$ is defined using $f(x)$ notation
- **[[Limit]]** — $\lim_{x \to a} f(x)$ asks what value $f(x)$ approaches

### Related cards
- **[[Set]]** and **[[Set-Builder Notation]]** — domains and ranges are sets, written in set-builder notation
- **[[Stationary Points]]** — finding where $f'(x) = 0$ requires understanding $f$ as a function

---

## Beyond Syllabus

### AP / IB / A-Level depth

**Piecewise functions 分段函数 (fēnduàn hánshù)**

A function can have different rules for different parts of its domain:

$$f(x) = \begin{cases} x^2 & \text{if } x < 0 \\ 2x + 1 & \text{if } x \geq 0 \end{cases}$$

This is one function, not two — it simply has a different formula in different regions. The domain is all of $\mathbb{R}$, but the rule changes at $x = 0$.

Piecewise functions are common in IB and AP (tested directly) and appear in real-world modelling: tax brackets, shipping costs, and phone tariffs are all piecewise.

**Even and odd functions**

| Type | Definition | Symmetry | Example |
|------|-----------|----------|---------|
| Even | $f(-x) = f(x)$ for all $x$ | Symmetric about the $y$-axis | $f(x) = x^2$, $f(x) = \cos x$ |
| Odd | $f(-x) = -f(x)$ for all $x$ | Rotational symmetry (180°) about the origin | $f(x) = x^3$, $f(x) = \sin x$ |

Most functions are neither even nor odd. Recognising symmetry can simplify integration (IB/AP) and Fourier analysis (university).

**Transformations of functions**

The relationship between $y = f(x)$ and transformed versions:

| Transformation | Effect on graph |
|----------------|-----------------|
| $y = f(x) + a$ | Translate up by $a$ |
| $y = f(x + a)$ | Translate left by $a$ |
| $y = af(x)$ | Vertical stretch, scale factor $a$ |
| $y = f(ax)$ | Horizontal stretch, scale factor $\dfrac{1}{a}$ |
| $y = -f(x)$ | Reflect in the $x$-axis |
| $y = f(-x)$ | Reflect in the $y$-axis |

This is a major topic in 0606 (tested in 1.4 with modulus) and central in IB/AP. The key insight: changes *inside* $f(\ldots)$ affect $x$ (horizontal, opposite direction); changes *outside* $f(\ldots)$ affect $y$ (vertical, same direction).

**Everything is IO — 媒介学 (méijiè xué)**

Step back from the formula for a moment. A function takes an input, transforms it, and produces an output. But here's the deeper observation: **the output of one function becomes the input of the next.** That's exactly what [[Composite Function|composition]] is — $f(g(x))$ means $g$ transforms $x$ into something, and $f$ picks up where $g$ left off.

Now extend that idea beyond mathematics. *Everything* is a medium — a 媒介 — that takes in, transforms, and passes on. The process itself is the 媒介:

- A **car** is a 媒介. Input: you want to be somewhere. Output: you arrive. But the car doesn't just transport — it *transforms your behaviour*. Owning a car encourages you to carry more things. A car with good assistive driving frees up your mental energy, making you more likely to hit the gym after work. The medium reshapes the output in ways the "function rule" didn't explicitly state.
- A **teacher** is a 媒介. Input: a concept. Output: understanding in the student's mind. But the teacher's style, personality, and methods transform not just *what* the student learns but *how* they think.
- A **language** is a 媒介. Input: a thought. Output: communication. But the structure of the language shapes which thoughts are easy to express and which are nearly impossible.

This perspective — 媒介学, the study of media and mediation — says: **don't just look at the input and output; look at how the process in between shapes both.** In mathematical notation, we write $y = f(x)$ and focus on $x$ and $y$. 媒介学 says: pay attention to $f$ itself. The transformation *is* the interesting part.

> [!tip] IO chains — how everything connects
> The world is a giant composition of functions. The output of one process is the input of the next:
>
> $$\text{sunlight} \xrightarrow{\text{photosynthesis}} \text{glucose} \xrightarrow{\text{digestion}} \text{energy} \xrightarrow{\text{muscles}} \text{movement}$$
>
> Each arrow is a 媒介 — a function that transforms and passes on. Mathematics gives us the precise language for this: **composition** ($f \circ g$), **chaining**, **pipelines**. Computer science calls it the same thing — data flows through functions, each one's output becoming the next one's input. The entire structure of modern software, biological systems, and even economies is IO chains mediated by transformations.

Once you see the world through 媒介学, entirely new fields open up — because you start asking: "What if we *design* the medium? What if we *change* what sits between input and output?"

- **Affective computing 情感计算 (qínggǎn jìsuàn)** — What if a computer could read your emotions as input? Your face, your voice, your heart rate — all become inputs to a function whose output is an adapted response. A tutoring app that detects frustration and slows down. A car dashboard that notices drowsiness and alerts you. The entire field exists because someone asked: "What if we put an emotion-reading 媒介 between the human and the machine?"
- **Feedback loops 反馈回路 (fǎnkuì huílù)** — What happens when the *output* of a system loops back as its own *input*? A thermostat reads the room temperature (output of heating), then adjusts the heater (input to heating). Social media reads your engagement (output of content), then reshapes your feed (input to your attention). In maths, this is **recursion**: $x_{n+1} = f(x_n)$ — the output becomes the next input. The 媒介 feeds into itself, and the system evolves. Cybernetics, control theory, and dynamical systems all study these self-referencing IO chains.
- **Neural networks 神经网络 (shénjīng wǎngluò)** — A deep learning model is literally a composition of functions: $f_n \circ f_{n-1} \circ \cdots \circ f_1(x)$. Each layer is a 媒介 — it transforms the data and passes it on. The magic is that the layers *learn* their own transformation rules from data. Nobody programs the medium; the medium programs itself.

The pattern is always the same: *identify what sits between input and output, then study it, design it, or redesign it.* That's 媒介学. And it all starts with the idea on this card — that a function is a transformation with an input and an output.

### Beyond high school — University

**Functions as the foundation of modern mathematics**

In set theory, a function $f: A \to B$ is formally defined as a subset of the **Cartesian product** $A \times B$. The Cartesian product $A \times B$ is simply the set of *all* ordered pairs you can form by picking one element from $A$ and one from $B$:

$$A \times B = \{(a, b) : a \in A, \; b \in B\}$$

For example, if $A = \{1, 2\}$ and $B = \{x, y\}$, then $A \times B = \{(1, x), (1, y), (2, x), (2, y)\}$ — every possible pairing. (The name honours René Descartes, whose coordinate system is built on exactly this idea: the $xy$-plane is $\mathbb{R} \times \mathbb{R}$.)

A function is then a subset of $A \times B$ satisfying:

$$\forall \, a \in A, \; \exists! \; b \in B \text{ such that } (a, b) \in f$$

(For every element $a$ in $A$, there exists exactly one element $b$ in $B$ such that the pair $(a, b)$ belongs to $f$.)

This definition makes no mention of formulas or rules — a function is just a *set of ordered pairs* where no input is repeated. This abstraction enables:

- **Analysis:** continuity, differentiability, and integrability are all properties of functions
- **Linear algebra:** linear transformations are functions between vector spaces
- **Computer science:** every program is a function from inputs to outputs; functional programming languages (Haskell, Lisp) make this explicit
- **Category theory:** the most abstract branch of mathematics studies functions (morphisms) between structures

The idea that "a function is a machine with inputs and outputs" scales from IGCSE all the way to research-level mathematics — only the domain and range become more exotic (from $\mathbb{R}$ to vector spaces, manifolds, function spaces, etc.).

---

## LaTeX Reference

| Notation | LaTeX | Rendered |
|----------|-------|----------|
| Function value | `f(x)` | $f(x)$ |
| Maps-to arrow | `f: x \mapsto 2x + 3` | $f: x \mapsto 2x + 3$ |
| Set map | `f: A \to B` | $f: A \to B$ |
| Domain set-builder | `\{x : x \in \mathbb{R}, x \neq 0\}` | $\{x : x \in \mathbb{R}, x \neq 0\}$ |
| Range set-builder | `\{y : y \geq 0\}` | $\{y : y \geq 0\}$ |
| Piecewise | `\begin{cases} ... \end{cases}` | (see Beyond section) |
| Real numbers | `\mathbb{R}` | $\mathbb{R}$ |
| For all | `\forall` | $\forall$ |
| There exists unique | `\exists!` | $\exists!$ |
| Cartesian product | `A \times B` | $A \times B$ |
| Composition chain | `A \xrightarrow{f} B \xrightarrow{g} C` | $A \xrightarrow{f} B \xrightarrow{g} C$ |

---
chinese: 阶乘 (jiēchéng)
prerequisites: []
leads_to:
  - "[[Permutations and Combinations]]"
  - "[[Binomial Theorem]]"
  - "[[Binomial Series]]"
  - "[[Counting Problems]]"
  - "[[Maclaurin Series]]"
  - "[[Recursion]]"
tags:
  - subject/mathematics
  - domain/combinatorics
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - syllabus/0606-11-2
  - type/definition
  - type/vocabulary
  - notation/factorial
  - misconception/zero-factorial
---

# Factorial Notation 阶乘

## Definition

### Formal

The **factorial** of a non-negative integer $n$, written $n!$ (read "$n$ factorial"), is the product of all positive integers from $1$ to $n$:

$$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$$

Equivalently, $n!$ has a **recursive definition**:

$$n! = \begin{cases} 1 & \text{if } n = 0 \quad \text{(base case)} \\ n \times (n-1)! & \text{if } n \geq 1 \quad \text{(recursive case)} \end{cases}$$

These two definitions give the same result, but the recursive version is more powerful — it defines the function in terms of itself.

### Intuitive

$n!$ answers the question: **"How many ways can you arrange $n$ objects in a line?"**

Line up 4 books on a shelf:

- Slot 1: **4** choices (any book)
- Slot 2: **3** choices (one already placed)
- Slot 3: **2** choices
- Slot 4: **1** choice (last book remaining)

Total: $4 \times 3 \times 2 \times 1 = 4! = 24$ arrangements.

This works because of the **multiplication principle** — if step 1 has $a$ options and step 2 has $b$ options, there are $a \times b$ total paths. Factorial is this principle applied $n$ times, with one fewer option each time.

### 中文锚点 (Chinese Anchor)

**阶乘** (jiēchéng)："阶"是台阶、阶梯——像走楼梯一样，从$n$一步一步乘下去，一直乘到1。

$$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$$

递归定义（参见下方"阶乘与递归"）：
- 起点：$0! = 1$（零个东西只有一种排法——什么都不做）
- 规则：$n! = n \times (n-1)!$（要排$n$个东西，先选一个放第一位，剩下$(n-1)$个按$(n-1)!$排）

## Values

| $n$ | $n!$ | Calculation |
|---|---|---|
| $0$ | $1$ | By definition |
| $1$ | $1$ | $1$ |
| $2$ | $2$ | $2 \times 1$ |
| $3$ | $6$ | $3 \times 2 \times 1$ |
| $4$ | $24$ | $4 \times 3 \times 2 \times 1$ |
| $5$ | $120$ | $5 \times 4 \times 3 \times 2 \times 1$ |
| $6$ | $720$ | |
| $7$ | $5{,}040$ | |
| $8$ | $40{,}320$ | |
| $9$ | $362{,}880$ | |
| $10$ | $3{,}628{,}800$ | |
| $20$ | $\approx 2.4 \times 10^{18}$ | Larger than the number of grains of sand on Earth |

Factorials grow **extremely fast** — faster than exponentials. By $n = 13$, $n!$ exceeds 6 billion. By $n = 70$, $n!$ exceeds $10^{100}$ (a **googol** — and yes, that's where the company Google got its name, as a misspelling of "googol" to represent searching through unimaginably large amounts of information).

## Key Facts / Properties

### Why $0! = 1$

This is the most common sticking point. Three reasons, each independently convincing:

**Reason 1 — The pattern:**

$$4! = 24, \quad 3! = 6, \quad 2! = 2, \quad 1! = 1$$

Each step divides by the next number down: $\dfrac{4!}{4} = 3!$, $\dfrac{3!}{3} = 2!$, $\dfrac{2!}{2} = 1!$

Following the pattern: $\dfrac{1!}{1} = 0! = 1$.

**Reason 2 — Counting:**

$n!$ counts the number of ways to arrange $n$ objects. How many ways can you arrange **zero** objects? Exactly **one** way — do nothing. The "empty arrangement" is a valid arrangement. So $0! = 1$.

**Reason 3 — The formulas need it:**

We need ${}^nC_n = 1$ (choosing all $n$ items gives one outcome). The formula $\dfrac{n!}{n! \cdot 0!}$ equals 1 **only if** $0! = 1$. Similarly, ${}^nC_0 = 1$ requires $0! = 1$.

### Useful Identities

| Identity | Why it works |
|---|---|
| $n! = n \times (n-1)!$ | Recursive definition |
| $\dfrac{n!}{(n-r)!} = n \times (n-1) \times \cdots \times (n-r+1)$ | Cancel the common tail — this is ${}^nP_r$ |
| $\dfrac{n!}{k! \cdot (n-k)!} = \binom{n}{k}$ | Combination formula — see [[Permutations and Combinations]] |

### Cancellation Trick

Never compute full factorials when a ratio is involved. Cancel first:

$$\dfrac{10!}{7!} = \dfrac{10 \times 9 \times 8 \times \cancel{7!}}{\cancel{7!}} = 720$$

$$\dfrac{100!}{98!} = 100 \times 99 = 9900$$

This is essential for exam speed and avoids calculator overflow.

## Factorial and Recursion

### What is recursion?

**Recursion** is when something is defined in terms of a smaller version of itself.

The factorial function is a perfect example:

$$5! = 5 \times 4!$$

But what is $4!$? It's $4 \times 3!$. And $3! = 3 \times 2!$. And $2! = 2 \times 1!$. And $1! = 1 \times 0!$. And $0! = 1$ — we stop here.

Unrolling the full chain:

$$5! = 5 \times 4! = 5 \times (4 \times 3!) = 5 \times 4 \times (3 \times 2!) = 5 \times 4 \times 3 \times (2 \times 1!) = 5 \times 4 \times 3 \times 2 \times (1 \times 0!)$$

$$= 5 \times 4 \times 3 \times 2 \times 1 \times 1 = 120$$

Every recursive definition has two parts:

| Part | Factorial example | Purpose |
|---|---|---|
| **Base case** | $0! = 1$ | Where the recursion stops — without this, it goes forever |
| **Recursive case** | $n! = n \times (n-1)!$ | Reduces the problem to a smaller version of itself |

> [!warning] What happens without a base case?
> 中文里有个经典故事："从前有座山，山里有座庙，庙里有个老和尚在给小和尚讲故事，讲的什么故事呢？——从前有座山……"
>
> In English: *"It was a dark and stormy night, and the captain said to his mate, 'Tell us a story!' And the mate began: 'It was a dark and stormy night, and the captain said to his mate, "Tell us a story!" And the mate began...'"*
>
> Both are recursion **without a base case** — they loop forever. That's exactly what would happen if we didn't define $0! = 1$: the factorial would keep calling itself ($0! = 0 \times (-1)! = 0 \times (-1) \times (-2)! = \cdots$) and never stop. The base case is what makes recursion useful instead of infinite.

> [!info] Beyond syllabus — Recursion in computer science
> Recursion is one of the most powerful ideas in computer science. When a function calls itself, that's recursive programming. The factorial function is usually the first example taught:
>
> ```
> function factorial(n):
>     if n = 0 then return 1          ← base case
>     else return n × factorial(n-1)   ← recursive case
> ```
>
> This pattern appears everywhere: file systems (folders inside folders), fractals (patterns inside patterns), divide-and-conquer algorithms (merge sort, quicksort), and even the way web pages are structured (HTML elements nested inside other elements).
>
> The key insight: a complex problem can be solved by reducing it to a simpler version of the same problem, plus a small amount of work. Factorial reduces "arrange $n$ things" to "pick one for first place, then arrange the remaining $n-1$ things."

### Why recursion works for factorial

Think of arranging $n$ books:

1. **Pick which book goes first** — $n$ choices
2. **Arrange the remaining $n-1$ books** — that's the same problem, just smaller!

So the number of arrangements = $n \times (\text{arrangements of } n-1 \text{ books}) = n \times (n-1)!$

This "reduce and recurse" pattern is exactly why the recursive definition works. Each step reduces the problem by one, until you reach 0 books — one arrangement (do nothing), which is the base case.

## Common Misconceptions (Teaching Notes)

### 1. "$0! = 0$"

The most common factorial mistake. Students assume "zero things multiplied together = zero."

**Fix:** All three reasons from the Key Facts section. The pattern argument ($\dfrac{1!}{1} = 0! = 1$) is usually the most convincing.

### 2. Computing full factorials before dividing

Students calculate $20!$ and $17!$ separately, then divide. This causes calculator overflow or rounding errors.

**Fix:** Always cancel first. $\dfrac{20!}{17!} = 20 \times 19 \times 18 = 6840$. "If you see a fraction of factorials, cancel the common tail."

### 3. Thinking $n!$ means $n$ times something

Students read $5!$ as "5 times" and expect it to equal 5, or confuse it with $5 \times 1$.

**Fix:** "The exclamation mark means factorial, not emphasis. $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$."

### 4. Applying factorial to non-integers

$3.5!$ is undefined in the basic definition (though the Gamma function extends it at university level). Students sometimes try to compute $\dfrac{1}{2}!$ or similar.

**Fix:** "Factorial is only defined for non-negative integers: $0, 1, 2, 3, \ldots$"

## Exam Notes

### Cambridge 0606

- 11.2: know and use $n!$; know that $0! = 1$
- Factorials appear inside ${}^nP_r$ and ${}^nC_r$ formulas
- Expect simplification: "simplify $\dfrac{8!}{5! \times 3!}$"
- Calculator: students should know how to find the $!$ button (usually `MATH` → `PRB` or `OPTN` → `PROB`)
- Both Paper 1 and Paper 2

### Not in 0580 or 9260

Factorial notation is not in the Cambridge 0580 or OxAQA 9260 specification.

### AP / IB / A-Level

- **AP / IB:** factorials used in binomial expansion, probability distributions (binomial, Poisson)
- **A-Level Further:** multinomial coefficients, Taylor series ($e^x = \sum \dfrac{x^n}{n!}$)

### Beyond high school — University

- Gamma function $\Gamma(n+1) = n!$ extends factorial to all complex numbers
- Stirling's approximation $n! \approx \sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n$ estimates large factorials

## Connections

- **Application:** [[Permutations and Combinations]] — ${}^nP_r$ and ${}^nC_r$ are both defined using factorials
- **Application:** [[Binomial Theorem]] — $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ is the binomial coefficient
- **Foundation for:** [[Combined Probability]] — counting outcomes often requires factorials
- **Computer science:** [[Recursion]] — factorial is the classic first example of a recursive function
- **Growth:** Factorial growth ($n!$) outpaces exponential growth ($k^n$) — relevant in algorithm complexity
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas on this card are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $n!$ | `n!` | Factorial |
| $0! = 1$ | `0! = 1` | Special case — by definition |
| $\binom{n}{r}$ | `\binom{n}{r}` | Uses factorials: $\dfrac{n!}{r!(n-r)!}$ |
| $\dfrac{n!}{(n-r)!}$ | `\dfrac{n!}{(n-r)!}` | Permutation formula |

---
chinese: 递归 (dīguī)
prerequisites:
  - "[[Logic]]"
  - "[[Factorial Notation]]"
  - "[[Sequences]]"
  - "[[Proof by Induction]]"
  - "[[Logic Gates]]"
leads_to:
  - "[[Dynamic Programming]]"
  - "[[Searching]]"
  - "[[Sorting]]"
  - "[[Trees]]"
  - "[[Recursion as a Way of Thinking]]"
  - "[[Big-O Notation]]"
  - "[[Compilers and Interpreters]]"
  - "[[Turing Machine]]"
  - "[[Parallel and External Sorting]]"
  - "[[The Boolean-to-Silicon Bridge]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/algorithms
  - domain/recursion
  - level/A-Level
  - level/AP
  - curriculum/Cambridge-9618
  - curriculum/AP-CSA
  - curriculum/IB-CS
  - syllabus/IB-CS-B2-4
  - syllabus/9618-19-1c
  - syllabus/9618-19-2
  - syllabus/AP-CSA-4-16
  - syllabus/AP-CSA-4-17
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/recursive-call
  - notation/base-case
  - notation/recursive-case
  - notation/call-stack
  - misconception/recursion-is-just-iteration
  - misconception/missing-base-case
  - misconception/wrong-recursive-direction
  - misconception/all-recursion-is-exponential
---

# Recursion 递归

## Definition

A **recursive function** is a function that calls itself, with each call working on a *smaller* version of the same problem, until it reaches a **base case** that can be solved directly without further recursion.

Every recursive definition has two parts:

1. **The base case** — one or more *simple inputs* whose answer is known directly, with **no recursive call**.
2. **The recursive case** — a rule that solves the problem for a general input by *calling the function on smaller inputs* and combining their answers.

The canonical example, written in pseudocode:

```python
def factorial(n):
    if n == 0:                  # base case
        return 1
    else:                       # recursive case
        return n * factorial(n - 1)
```

Two facts hide in plain sight inside this six-line definition:

- **No loop appears anywhere.** The function never says "repeat" or "for each." Yet it computes products of arbitrarily many numbers. The repetition is *hidden inside the recursive call* — every time `factorial(n-1)` runs, it generates its own next call.
- **The function defines itself in terms of itself**, and this is *not* circular. The circularity is broken by the base case — `factorial(0) = 1` is just a fact, with no recursion. Every recursive call eventually descends to this base.

> [!info] Why this matters for the hunter
> This card is the hunter target *"trace why each recursive call goes deeper, where the base case stops descent, and how returns unwind the stack."* The two SVGs in this card make that trace visible.

### 中文锚点

**递归 (dīguī)** = 一个函数在它的定义里调用自己，每次都让问题变小一点，最终落到一个不再递归的「基础情况」(基线条件)。

| English | 中文 | What it means |
|---|---|---|
| Recursion | 递归 (dīguī) | Function calls itself with a smaller input |
| Base case | 基础情况 / 基线条件 (jīxiàn tiáojiàn) | The stopping condition — input small enough to answer directly |
| Recursive case | 递归情况 (dīguī qíngkuàng) | The rule that reduces a problem to a smaller version |
| Call stack | 调用栈 (diàoyòng zhàn) | The memory structure that tracks active function calls |
| Stack overflow | 栈溢出 (zhàn yìchū) | What happens when recursion doesn't terminate |
| Tail recursion | 尾递归 (wěi dīguī) | Recursive call is the *last* thing the function does |

中文 CS 教材通常先教循环 (loop)，然后才教递归。这是教学顺序的问题，不是逻辑顺序的问题。**逻辑上递归比循环更基础** —— 数学归纳法的结构就是递归的结构，而循环是从中提炼出来的工程优化。本卡试图让学生在脑子里建立 *"递归就是数学归纳法的可执行版本"* 的等价关系。

> [!example] 从前有座山 — the classic Chinese recursion joke
> Every Chinese child has heard this one. It is the canonical **missing-base-case recursion** in Chinese folk culture, predating computer science by centuries:
>
> 从前有座山。 *Once upon a time, there was a mountain.*  
> 山里有座庙。 *Inside the mountain there was a temple.*  
> 庙里有个老和尚。 *Inside the temple there was an old monk.*  
> 老和尚在给小和尚讲故事。 *The old monk was telling a story to a young monk.*  
> 故事是这样的：从前有座山…… *The story went: Once upon a time, there was a mountain…*
>
> ![[recursion-monks.png|600]]
>
> The recursion is structurally exact: the *story* the old monk tells **is itself**, so each retelling adds one layer of mountain → temple → old monk → young monk → story to the stack. **There is no termination condition.** Translated to code, this would crash with a **stack overflow** the moment the call stack ran out of memory:
>
> ```
> def 讲故事():
>     print("从前有座山，山里有座庙，庙里有个老和尚，老和尚在给小和尚讲故事，故事是这样的:")
>     讲故事()        # ← recursive call with NO base case
> ```
>
> Generations of Chinese parents used this joke to torment small children who demanded another bedtime story — the joke being that the story technically never ends, it just hits the parent's patience-stack-overflow first. The folk wisdom anticipated the bug by about a thousand years.

---

## The deep claim — recursion is mathematical induction made executable

This is the load-bearing pedagogical move. **A recursive function and a mathematical-induction proof have the same structure**, and they answer different versions of the same question.

| Mathematical induction | Recursive function |
|---|---|
| **Goal:** prove $P(n)$ holds for every natural number $n$. | **Goal:** compute $f(n)$ for every natural number $n$. |
| **Base case:** prove $P(0)$ holds directly. | **Base case:** return $f(0)$ directly. |
| **Inductive step:** assume $P(k)$, prove $P(k+1)$. | **Recursive step:** assuming $f(k)$ is known, compute $f(k+1) = (\text{rule})(f(k))$. |
| **Conclusion:** by induction, $P(n)$ holds for all $n \geq 0$. | **Termination:** every call eventually reaches the base case, so $f(n)$ is defined for all $n \geq 0$. |
| **Why it works:** well-founded ordering on $\mathbb{N}$ (no infinite descent). | **Why it works:** same — every recursive call decreases the argument toward the base case. |

Look at the factorial example. The mathematical induction proof that *"factorial(n) returns n!"* uses:

- Base case: factorial(0) returns 1, and $0! = 1$. ✓
- Inductive step: assume factorial(k) returns $k!$. Then factorial(k+1) returns $(k+1) \times$ factorial(k) $= (k+1) \times k! = (k+1)!$. ✓
- Therefore factorial(n) returns $n!$ for all $n \geq 0$.

That is *literally* the same statement as the definition of the recursive function, just read backwards. **Recursion is induction with the inductive step expressed as an algorithm rather than as a theorem.**

This duality has practical consequences: **proving a recursive function correct is exactly an induction proof on its argument.** Every CS student who writes a recursive function is doing applied mathematical induction, whether or not the lecturer ever says the word "induction."

---

## Tracing the call stack — factorial(4) step by step

When the function `factorial(4)` runs, the computer maintains a **call stack** — a vertical pile of *frames*, one per active function call. Each frame remembers the argument the call was made with and where it should return to.

![[recursion-call-stack.svg|640]]

The trace, in detail:

1. **Call factorial(4).** A new frame is pushed onto the stack. Since $4 \neq 0$, the function needs `factorial(3)` before it can multiply.
2. **Call factorial(3).** Another frame pushed. Since $3 \neq 0$, needs `factorial(2)`.
3. **Call factorial(2).** Frame pushed. Needs `factorial(1)`.
4. **Call factorial(1).** Frame pushed. Needs `factorial(0)`.
5. **Call factorial(0).** Frame pushed. Base case hit: **return 1**. The frame pops.
6. **Back in factorial(1).** It receives the returned 1, computes $1 \times 1 = 1$, returns 1. Frame pops.
7. **Back in factorial(2).** Receives 1, computes $2 \times 1 = 2$, returns 2. Frame pops.
8. **Back in factorial(3).** Receives 2, computes $3 \times 2 = 6$, returns 6. Frame pops.
9. **Back in factorial(4).** Receives 6, computes $4 \times 6 = 24$, returns 24. Frame pops.
10. **Done.** The call stack is empty. The final answer is 24.

The descent (steps 1–5) builds the stack to depth 5; the ascent (steps 6–9) unwinds it. **Every recursive call is one push; every base-case return + recursive return is one pop.** The depth of the stack at its peak is the depth of recursion — for factorial(n), this is $n+1$ frames.

> [!warning] Stack overflow — the limit of recursion
> Every computer has a finite call stack — typically a few thousand frames. If the recursion goes too deep (or never terminates because of a missing base case), the stack runs out of memory and the program crashes with a **stack overflow** error. *That's where the website's name comes from.* For practical depths (say, < 1000 levels) recursion is safe; for huge depths (a million levels), you either need iteration, tail-call optimisation, or an explicit stack data structure.

---

## Three classic recursive structures

### 1. Factorial — the canonical first example

Already covered above. The defining property: **each recursive call decreases the argument by exactly 1**. Linear depth. The simplest possible recursion structure.

### 2. Fibonacci — and the redundancy problem

The Fibonacci sequence $F_n$ is defined recursively:

$$F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \text{ for } n \geq 2.$$

Translated to a recursive function:

```python
def fib(n):
    if n <= 1:                  # base case (covers both n=0 and n=1)
        return n
    else:                       # recursive case
        return fib(n - 1) + fib(n - 2)
```

This looks innocent. **It is a disaster of efficiency.** Each call generates *two* recursive calls, which each generate two more, and so on — the call tree branches exponentially.

![[recursion-fibonacci-tree.svg|720]]

Look at the tree for `fib(5)`. The value `fib(2)` is computed **three separate times** in three different branches of the tree. The value `fib(1)` is computed **five times**. The value `fib(0)` is computed **three times**. None of these computations remember each other — every branch re-derives the same subproblems from scratch.

The total number of recursive calls for `fib(n)` is roughly $\varphi^n$ where $\varphi = (1 + \sqrt{5})/2 \approx 1.618$ is the golden ratio. The exact count is worth pinning down, because **two different numbers live in this tree** and they are easy to mix up. The *leaves* are the base cases, and there are exactly $F_{n+1}$ of them. Every non-leaf call makes exactly two recursive calls, so the calls sitting *above* the leaves number $F_{n+1} - 1$ — one fewer than the leaves, as in any tree where each internal node has two children. Adding the two:

$$T(n) = \underbrace{F_{n+1}}_{\text{base cases}} + \underbrace{(F_{n+1} - 1)}_{\text{calls above them}} = 2F_{n+1} - 1 \text{ calls in total.}$$

So `fib(40)` costs **331,160,281 calls in total**, of which **165,580,141** are base cases; `fib(50)` costs over **40 billion**. The naive recursion takes **exponential time** even though the underlying sequence grows only at the same exponential rate.

This is the **classic recursion pitfall** — and the entry point to one of the most important algorithmic techniques in CS: **memoisation**, where you cache the result of each subproblem the first time you compute it. With memoisation, `fib(n)` runs in **linear time** (each subproblem computed once). See the beyond-syllabus section for the full development.

### 3. Greatest common divisor (Euclid's algorithm) — the most beautiful example

Recursion isn't always about counting. Here's a 2300-year-old example that uses recursion to compute the greatest common divisor of two numbers:

```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

The base case is when the second argument is zero; the recursive case replaces `(a, b)` with `(b, a mod b)`. **Each recursive call's first argument is the previous call's second argument, and the second argument shrinks toward zero.** The depth is roughly $\log_\varphi(\min(a, b))$ — *logarithmic*, not linear.

To see it in action: $\gcd(48, 18)$:

- $\gcd(48, 18) = \gcd(18, 48 \bmod 18) = \gcd(18, 12)$.
- $\gcd(18, 12) = \gcd(12, 18 \bmod 12) = \gcd(12, 6)$.
- $\gcd(12, 6) = \gcd(6, 12 \bmod 6) = \gcd(6, 0)$.
- $\gcd(6, 0) = 6$. **Base case hit.** Return 6.

Recursion unwinds: $\gcd(48, 18) = 6$. ✓

This algorithm is **Euclid's** — Book 7 of his *Elements*, around 300 BCE, in geometric language ("subtract the smaller from the larger until equal"). It is **the oldest non-trivial algorithm known**, and it is naturally recursive. Recursion as a way of thinking pre-dates computers by 2300 years.

---

## Recursion vs iteration — when each wins

Anything you can compute with recursion you can also compute with a loop, and vice versa. The two are formally equivalent (this is a theorem of computability theory — the Church-Turing thesis). But they aren't *equally good* for every problem.

| When recursion wins | When iteration wins |
|---|---|
| The data is recursively defined (trees, nested lists, parsed expressions, file systems) | Simple repeated arithmetic (sums, averages, counts) |
| Divide-and-conquer algorithms (merge sort, quicksort, binary search) | Performance-critical inner loops |
| The problem has natural mathematical recursion (Fibonacci, factorial, gcd) | Memory is constrained (no call-stack overhead) |
| You need elegance over speed for prototyping | The iterative version is shorter and clearer |
| The problem has multiple recursive branches (trees, graph traversal) | The recursive version has redundant subproblems (use memoisation or just iterate) |

In particular: **factorial is more idiomatic as a loop than as a recursion**, because the recursive structure adds no insight. But **traversing a tree is hugely more natural recursively** than iteratively, because the data structure itself is recursive.

### Tail-call optimisation

A recursive call is **tail-recursive** if it is the very last thing the function does — no further computation happens to the returned value. Languages that perform tail-call optimisation (Scheme, OCaml, Haskell, Erlang) translate tail recursion into a loop *automatically* — no stack growth at all. Languages without it (Python, Java) keep the stack growing whether or not the recursion is tail-form.

Compare:

```python
def factorial(n):                       def factorial_tail(n, acc=1):
    if n == 0:                              if n == 0:
        return 1                                return acc
    else:                                   else:
        return n * factorial(n-1)               return factorial_tail(n-1, n * acc)
       ^^^^^                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       multiplication AFTER the call             nothing after the call —
       — NOT tail recursive                      tail recursive
```

The right version is tail-recursive (an accumulator parameter `acc` carries the partial product). In a tail-call-optimising language, this compiles to a loop with constant stack space. **The cleanest CS-vs-engineering distinction: a tail-recursive function and a loop are the same thing, told two ways.**

### Why modern hardware prefers iteration

Recursion came first historically (Pingala 200 BCE, Euclid 300 BCE, Church / Turing / Kleene 1936) and is logically more fundamental than iteration. So why does *every* modern programmer reach for loops first and recursion second? The answer isn't laziness — it's that **the compiler, CPU, and RAM all conspire to make iteration cheaper than recursion** at the hardware level. Four reasons, layered:

1. **Function-call overhead.** Every recursive call pushes a *stack frame* — saving the return address, the caller's register values, the local variables, and the frame pointer onto the stack. Every return pops them back. A loop reuses a single set of variables in place; no push, no pop, no memory traffic per iteration. For a million-iteration computation, that's a million round-trips to RAM avoided.

2. **Cache locality.** A modern CPU has a tiny, very fast **instruction cache** (typically 32 KB) and **data cache** (similar). A tight loop fits entirely in the instruction cache and reuses the same handful of memory cells — every fetch is a cache *hit*. A chain of recursive calls keeps jumping around the call stack to different addresses; the CPU has to wait for cache *misses* to be filled from main memory, which is 100+ times slower. Iteration is what the cache hardware was *designed* for.

3. **Branch prediction.** Modern CPUs use a **branch predictor** to guess where execution will go next, and pre-fetch instructions speculatively. A `for` loop's exit condition is highly predictable (the predictor learns "this branch was taken the last thousand times, probably will be again"). Recursive function returns are less predictable — the CPU has to wait until the call stack unwinds to know what comes next. Loops feed the predictor what it likes.

4. **Compiler optimisations.** The compiler can do things to a tight loop that it can't easily do to recursion: **unrolling** (replacing the loop body with several copies to amortise the loop-overhead cost), **vectorisation** (using SIMD instructions to process 4–16 data items per CPU cycle), **invariant hoisting** (moving computations that don't change out of the loop body), and **strength reduction** (replacing expensive operations with cheaper equivalents). All of these need the compiler to see *one block of code that runs many times in the same context* — which is what a loop is. Recursion hides this structure behind function-call boundaries that the compiler usually won't cross.

> [!info] So iteration is "syntactic sugar" only at the abstract-CS level
> The Church-Turing-Kleene result says **anything you can compute with iteration you can compute with recursion, and vice versa**. At the level of computational power they are equivalent. At the level of *hardware performance*, they are not equivalent at all — iteration wins by a margin that grows with the size of the input. The loop construct is the language's way of saying *"please give the compiler permission to do all the optimisations above."*
>
> This is one of two reasons recursion is usually taught *after* loops despite being logically more basic. (The other reason is cognitive: a beginner's first mental model of "what a program does" is more easily anchored on a list of steps than on a self-reference. By the time they're comfortable with functions calling functions, recursion fits.)
>
> **Tail-call optimisation reconciles the two views.** When a language's compiler can guarantee the recursive call is the last thing the function does, it emits the *iteration* version of the code from the *recursion* version of the source. The programmer writes the conceptually clean recursion; the hardware runs the efficient loop. This is the "best of both worlds" outcome — and the reason Scheme and Haskell don't have a `for` keyword at all.

---

## The hunter's payoff — what this card teaches you to trace

Two causal traces this card equips you with:

1. **Forward trace (descent)** — given a recursive function and an input, walk down the recursion: each call generates the next, until a base case is reached. Predict the depth of the recursion. Identify the work done per frame.

2. **Backward trace (ascent)** — once a base case returns, walk the values back up the stack: each frame's return value depends on the deeper frames' returns. Predict the time complexity by counting how many calls actually happen.

For factorial, the descent and ascent are both linear in $n$ — total work is $O(n)$. For naive Fibonacci, the descent is a binary tree, total work is $O(\varphi^n)$ — exponential. For binary search, the descent halves the search space each time, total work is $O(\log n)$. **The shape of the recursion tree IS the time complexity.** Master this trace and you can read the speed of any recursive algorithm from its structure alone — the foundational skill for [[Big-O Notation]].

---

## Worked examples

### Example 1 — Tracing the call stack for factorial(5)

Compute `factorial(5)` by drawing the call stack at each step.

**Solution.** Frames pushed (descent):

| Step | Stack (top → bottom) | What's happening |
|---|---|---|
| 1 | factorial(5) | initial call |
| 2 | factorial(4), factorial(5) | factorial(5) needs factorial(4) |
| 3 | factorial(3), factorial(4), factorial(5) | factorial(4) needs factorial(3) |
| 4 | factorial(2), …, factorial(5) | …(2) needs (1) |
| 5 | factorial(1), factorial(2), …, factorial(5) | (1) needs (0) |
| 6 | factorial(0), factorial(1), …, factorial(5) | base case reached |

Frames popped (ascent):

| Step | Returns | Stack now |
|---|---|---|
| 7 | factorial(0) returns 1 | factorial(1), …, factorial(5) |
| 8 | factorial(1) returns 1 · 1 = 1 | factorial(2), …, factorial(5) |
| 9 | factorial(2) returns 2 · 1 = 2 | factorial(3), …, factorial(5) |
| 10 | factorial(3) returns 3 · 2 = 6 | factorial(4), factorial(5) |
| 11 | factorial(4) returns 4 · 6 = 24 | factorial(5) |
| 12 | factorial(5) returns 5 · 24 = 120 | (empty) |

**Final answer: factorial(5) = 120.** ✓

The maximum stack depth was 6 frames (factorial(5) down to factorial(0)). Total number of recursive calls: 6. Linear in the input — efficient.

### Example 2 — A recursive palindrome check

A **palindrome** is a string that reads the same forwards and backwards: "racecar", "level", "abba". Write a recursive function `is_palindrome(s)` that returns `True` if a string is a palindrome.

**Solution.** The recursive insight: a string of length 0 or 1 is trivially a palindrome (base case). For a longer string, it's a palindrome if and only if (i) the first and last characters match, AND (ii) the middle substring (everything except the first and last characters) is also a palindrome.

```python
def is_palindrome(s):
    if len(s) <= 1:                     # base case
        return True
    elif s[0] != s[-1]:                 # first and last must match
        return False
    else:
        return is_palindrome(s[1:-1])   # recurse on the middle
```

Trace for `is_palindrome("racecar")`:

- $s =$ "racecar", first = 'r', last = 'r'. Match → recurse on "aceca".
- $s =$ "aceca", first = 'a', last = 'a'. Match → recurse on "cec".
- $s =$ "cec", first = 'c', last = 'c'. Match → recurse on "e".
- $s =$ "e", length 1 → base case, return `True`.
- Three returns of `True` bubble back up. Final answer: `True`. ✓

Each recursive call shrinks the string by 2 characters. Depth is $\lceil n/2 \rceil$ where $n$ is the original length. Total work $O(n)$ (linear).

This is the **divide-and-conquer pattern**: the original problem is solved by reducing to a smaller version of the same problem, on a strictly smaller input.

### Example 3 — Recognising naive Fibonacci's redundancy

Without writing code, count the *exact* number of times `fib(0)` is called when computing `fib(5)` with the naive recursion.

**Solution.** Look at the recursion tree (the SVG above). The leaves of the tree are the base cases — every leaf is either `fib(0)` or `fib(1)`. Counting the leaves labelled `fib(0)` in the `fib(5)` tree gives **3** — matching the SVG count.

A useful pattern: the number of `fib(0)` calls when computing `fib(n)` is itself a Fibonacci-like sequence. Let $L_0(n) = $ number of `fib(0)` calls. Then:

- $L_0(0) = 1$ (the base case itself counts as one call)
- $L_0(1) = 0$ (`fib(1)` doesn't recurse)
- $L_0(n) = L_0(n-1) + L_0(n-2)$

So $L_0(2) = 1, L_0(3) = 1, L_0(4) = 2, L_0(5) = 3$ — and the total number of calls to `fib(0)` grows exponentially in $n$. *The redundancy is the entire reason naive Fibonacci is slow.*

The fix is one line of memoisation. See beyond-syllabus.

---

## Common pitfalls

1. **Missing base case → infinite recursion → stack overflow.** Every recursive function MUST have a base case that does not recurse. If you forget it, the function calls itself forever, the stack grows without limit, and the program crashes.

2. **Recursive call doesn't make progress.** Even with a base case, if the recursive call doesn't move *toward* the base case, you still get infinite recursion. Example: `def f(n): return f(n)` calls itself with the same argument every time, never reaching any base case.

3. **Wrong direction of recursion.** If the base case is at `n = 0` but the recursive call goes to `n + 1`, the recursion runs away from the base case toward infinity. The argument must shrink (or otherwise approach the base case) at each step.

4. **Exponential redundancy without memoisation.** As Fibonacci shows, branching recursion that recomputes the same subproblems can be catastrophic. The fix is to memoise (cache) results, or to iterate from the base case upward (the dynamic-programming pattern).

5. **Confusing recursion with iteration.** Recursion and loops are *different programming patterns*, even though they're computationally equivalent. A loop reuses one frame; recursion uses a new frame per iteration. The choice affects readability, memory, and (in non-optimising languages) speed.

---

## Java specifics for AP CSA

Recursion in Java looks like recursion anywhere else, with the addition of [[Static Method Declarations]]:

```java
public static int factorial(int n) {
    if (n == 0) {              // base case
        return 1;
    } else {                   // recursive case
        return n * factorial(n - 1);
    }
}
```

AP CSA §4.16 and §4.17 expect students to:
- **Trace** a given recursive method, frame by frame, on a small input
- **Identify** the base case and recursive case in code
- **Reason about** what happens when the base case is missing (stack overflow)
- **Convert** simple recursive methods to iterative form and vice versa
- **Recognise** classic recursive structures: factorial, Fibonacci, sum of array elements, recursive search

The AP CSA exam particularly favours the **tracing** task — given a small recursive method, predict its output. The systematic call-stack method shown in Example 1 above is the universal answer technique. **Draw the stack. Don't try to mentally simulate it without paper.**

---

## Beyond syllabus

### Memoisation and dynamic programming

The naive Fibonacci is exponential. The memoised version stores each subproblem's answer the first time it's computed, then reuses it:

```python
memo = {}

def fib(n):
    if n in memo:                    # already computed — reuse
        return memo[n]
    if n <= 1:                       # base case
        return n
    result = fib(n - 1) + fib(n - 2)
    memo[n] = result                 # save for future calls
    return result
```

Python 3 actually ships a one-line memoisation decorator in the standard library, so the idiomatic version is:

```python
from functools import cache

@cache
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)
```

Same complexity behaviour — exponential becomes linear — with the caching invisible.

With memoisation, **each `fib(k)` is computed exactly once** (every later call finds the answer in the memo). The number of distinct subproblems is $n+1$, so the total work is $O(n)$ — linear. A 331-million-call computation becomes a 41-call computation.

This is the entry point to **dynamic programming** — the broader algorithmic paradigm of "store partial answers, reuse them, never recompute." It's one of the four foundational algorithmic paradigms (alongside divide-and-conquer, greedy, and graph search). The vault's full development lives in [[Dynamic Programming]].

### Mutual recursion

Two functions can be mutually recursive — each calls the other. The classic example: even/odd via subtraction:

```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)
```

This is silly (just check `n % 2 == 0`), but it illustrates mutual recursion. The Hofstadter male/female sequences are a less-silly example, as are the canonical implementations of parsers (each grammar rule recurses into the others).

### The Ackermann function

Most recursive functions you meet are **primitive recursive** — provably terminating with a bound expressible in elementary arithmetic. The **Ackermann function** is the canonical example of a function that is recursively definable but not primitive recursive:

$$A(m, n) = \begin{cases} n + 1 & \text{if } m = 0 \\ A(m-1, 1) & \text{if } m > 0, n = 0 \\ A(m-1, A(m, n-1)) & \text{if } m > 0, n > 0 \end{cases}$$

$A(4, 2)$ has more than $10^{19{,}728}$ digits. The function provably terminates (the argument decreases in the lexicographic order on $(m, n)$ pairs), but its growth rate exceeds anything you can write down with finitely many applications of basic arithmetic and primitive recursion. The Ackermann function was Wilhelm Ackermann's 1928 proof that the class of "computable" functions is strictly larger than the class of "primitive recursive" functions — a foundational discovery in the theory of computation.

### The Y combinator — recursion without naming

In the **lambda calculus** (Church 1936, the theoretical foundation of functional programming), functions don't have names. So how do you write a recursive function if you can't refer to yourself by name?

The answer is the **Y combinator**, a higher-order function that takes any function-of-a-function $f$ and returns its **fixed point** $Y(f)$ — a value where $Y(f) = f(Y(f))$. Apply $Y$ to a "would-be recursive" function and you get the recursion *for free*, without ever naming the function. The definition:

$$Y = \lambda f.\, (\lambda x.\, f(x \, x))(\lambda x.\, f(x \, x))$$

Read in any concrete programming language this looks alarming, but the structure is exactly the inductive principle in disguise. The Y combinator is one of the great results in the foundations of computer science — *it shows that recursion is not a primitive feature of computation, but a derived one from the more basic ability to pass functions as arguments*. The vault won't go further here, but the existence of $Y$ is a load-bearing result for every functional language that exists today.

> [!tip] Two pieces of practical advice about the Y combinator
> 1. **If you can't understand it, that's normal.** $Y$ is genuinely hard. It takes most CS undergraduates a couple of confused weeks of staring at it to feel the shape; some don't really click with it until graduate school. Skip it for now, come back in two years, try again. It will still be here. The understanding eventually arrives by repeated exposure, not by force.
> 2. **If you DO understand it, please don't write it.** Languages give you named recursion for a reason — readability. Production code that uses $Y$ to "elegantly" do what a five-line named function would do is the canonical mark of someone who recently learned a fancy thing and wants everyone to know. Save $Y$ for the textbook chapter where it belongs.

### Recursion in mathematical structures

Recursion isn't just an algorithm pattern — it's a way of defining structures. Examples:

- **Lists** can be defined recursively: a list is either empty, or it is one element followed by a list. (Lisp's foundational insight.)
- **Trees** are recursively defined: a tree is a value plus a list of subtrees.
- **Grammars** in linguistics and parsing: a sentence contains noun phrases that contain sentences. (Chomsky's 1957 *Syntactic Structures* is the foundational paper.)
- **Fractals**: the Mandelbrot set, the Koch snowflake, the Sierpiński triangle are all *self-similar* — each part contains a smaller copy of the whole. Same structural pattern as a recursive function.

The vault's [[Recursion as a Way of Thinking]] (a Tier-3 hunter beyond this card) develops the cognitive shift: once you start seeing the world recursively, you find self-similar structure everywhere.

### Church-Turing thesis — recursion IS computation

The **Church-Turing thesis** (formulated independently by Alonzo Church and Alan Turing in 1936) states that *any effectively computable function can be computed by a Turing machine, or equivalently by the lambda calculus, or equivalently by general recursive functions*. The three formalisms — Turing machines (state + tape), lambda calculus (pure functions), and general recursive functions (base + composition + primitive recursion + minimisation) — were shown by Church, Turing, and Kleene to be **mutually equivalent**: each can simulate the others. The "Church-Turing thesis" identifies these formal models with the intuitive notion of *computable* itself.

What this means: **recursion is not one programming feature among many. It is one of the three fundamental characterisations of what computation IS.** Every programming language you ever use is, at the bottom, a recursion-with-syntactic-sugar.

---

## Exam Notes

### Cambridge 9618 A-Level (§19.2)

- Recursion is **A-Level content**: understand what it is; write and trace recursive algorithms; know the **essential features** (a base case; a recursive call; each call must move *toward* the base case); and explain **how a compiler implements recursion** — the call **stack** pushes a frame per call and **unwinds** on return ("unwinding" is the syllabus's own word; the factorial trace above is exactly this answer).
- Trace questions supply a recursive function and ask for the output or the sequence of calls and returns — credit follows a call-by-call table of parameters and return values. The benefits-vs-iteration discussion (§"Recursion vs iteration") is a standard short-answer: naturalness for self-similar problems against stack cost and overflow risk.

### AP CSA (§4.16–4.17)

- The exam requires **tracing** recursion, never writing it: multiple-choice gives recursive Java and asks what it returns or prints; every free-response can be answered iteratively. §"Java specifics for AP CSA" carries the language details; recursive binary search and merge sort are the named tracing targets.

### IB Computer Science — B2.4

- Recursion sits in **B2.4 Programming algorithms**, beside searching, sorting, and efficiency: trace a recursive algorithm, name the **base case** and the **recursive step**, and say when recursion fits a problem. The call-by-call trace-table discipline from the 9618 section transfers whole; HL's data-structure work leans on it harder (trees are recursion made of pointers).

### Where it is *not* examined

- **0478 IGCSE:** no recursion anywhere — iteration is the only repetition construct; the idea first becomes examinable at A-Level.

---

## Connections

- **Mathematical foundation:**
   - [[Proof by Induction]] — the proof-theoretic twin of recursion. Same structure, different goal (proving vs computing).
   - [[Factorial Notation]] — the canonical first example, both as definition ($n! = n \cdot (n-1)!$) and as the introductory recursive function.
   - [[Sequences]] — recurrence relations like Fibonacci are recursive definitions at the mathematical level.
   - [[Logic]] — propositional structure of base cases and recursive cases.

- **Computer science children:**
   - [[Dynamic Programming]] — the systematic way to remove redundancy from recursive solutions via memoisation or tabulation.
   - [[Searching]] — home of **binary search**, the canonical $O(\log n)$ recursive algorithm; divide-and-conquer in its purest form.
   - [[Sorting]] — **merge sort** is divide-and-conquer recursion at full size: split the list in half, recurse on each, merge the sorted halves.
   - [[Trees]] — recursively-defined data structure where recursive traversal is far more natural than iteration.
   - [[Big-O Notation]] — the formal language for talking about the time cost of recursive algorithms ($O(n)$ for factorial, $O(\log n)$ for binary search, $O(\varphi^n)$ for naive Fibonacci).
   - [[Recursion as a Way of Thinking]] — the cognitive expansion beyond this card.

- **Beyond all syllabuses:**
   - [[Y Combinator]] — anonymous recursion in lambda calculus.
   - [[Turing Machine]] — the *machine* third of the 1936 equivalence (Turing machines = lambda calculus = general recursive functions). Also the home of the universal machine and the halting-problem proof.
   - [[Stories/Turing at Bletchley]] — Turing, who co-authored that 1936 equivalence, and what he did with the universal machine in the war.
   - [[Ackermann Function]] — beyond primitive recursion; the growth-rate frontier.
   - [[Fractals]] — self-similar geometric structures.

- **Misconception traps cleared:** recursion is **not** just "iteration with extra steps" (the call stack changes the memory model); a recursive function **must** have a base case (else stack overflow); the recursive call **must** make progress toward the base case (or it never terminates); naive recursion can be **exponentially** slow without memoisation (Fibonacci); and recursion and induction are **the same idea**, just used for different goals.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $F_n$ | `F_n` | Fibonacci sequence, $F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}$ |
| $n!$ | `n!` | Factorial — $n! = n \cdot (n-1)!$ with $0! = 1$ |
| $\gcd(a, b)$ | `\gcd(a, b)` | Greatest common divisor — Euclid's recursive algorithm |
| $A(m, n)$ | `A(m, n)` | Ackermann function — not primitive recursive |
| $Y$ | `Y` | Y combinator — recursion without naming |
| $O(\varphi^n)$ | `O(\varphi^n)` | Time complexity of naive Fibonacci, where $\varphi = (1+\sqrt 5)/2$ |
| $O(\log n)$ | `O(\log n)` | Time complexity of binary search via halving recursion |

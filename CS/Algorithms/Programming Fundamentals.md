---
chinese: 编程基础 (biānchéng jīchǔ)
prerequisites:
  - "[[Program Design]]"
leads_to:
  - "[[Arrays]]"
  - "[[Program Development Life Cycle and Testing]]"
  - "[[Java Values and Expressions]]"
teach_together:
  - "[[Cambridge Pseudocode]]"
tags:
  - subject/computer-science
  - domain/algorithms
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - curriculum/AP-CSA
  - syllabus/0478-8-1
  - syllabus/0478-7-3
  - syllabus/0478-7-4
  - syllabus/0478-7-9
  - syllabus/9618-11-1
  - syllabus/9618-11-2
  - syllabus/IB-CS-B2-1
  - syllabus/IB-CS-B2-3
  - type/deep
  - type/definition
  - notation/python
  - notation/pseudocode
  - misconception/assignment-is-an-equation
  - misconception/until-means-while
  - misconception/print-is-return
  - misconception/rounding-makes-a-fair-die
---

# Programming Fundamentals 编程基础

> A checkout, a game and a laboratory data logger all repeat the same small actions: remember a value, inspect it, change it, choose what happens next. The interesting part is deciding **what must remain true after each action**. Once that is clear, two different languages can tell the same machine story.

## Definition

A **program** is an executable description of a computation. Its **state** is the information it currently holds; a statement may change that state, produce an output, or choose the next statement. An **algorithm** is the method being expressed, independent of its spelling.

**Intuition:** trace forwards, asking *what is true now?* In a running total, the useful fact is “this is the sum of everything accepted so far.” A loop preserves that fact while making progress towards its stopping point. The spelling matters, but it comes after the promise.

### 中文锚点

在自助收银机上扫一件商品，总价就变一次；有会员折扣，就按另一套规则算；没扫完，就继续。程序并不神秘：它记住眼下的信息，再按明确的规则一步步改动。比如“总价加上这件商品的价格”，就是先算出新总价，再把原来的数换掉。这是赋值，不是在列一个永远成立的方程。看懂程序，可以先问：它现在记着什么，下一步又会把什么改掉？

### Vocabulary bridge

| English | 中文 | Meaning |
|---|---|---|
| variable / constant | 变量 / 常量 | a named value that may change / is fixed |
| assignment / comparison | 赋值 / 比较 | update a value / ask whether a relation holds |
| sequence / selection / iteration | 顺序 / 选择 / 迭代 | do in order / choose a branch / repeat |
| accumulator / counter | 累加器 / 计数器 | sum the values / count the events |
| parameter / argument | 形参 / 实参 | the name in the definition / the value supplied by a call |
| scope / local / global | 作用域 / 局部 / 全局 | where a name can be used / inside a subprogram / across the program |
| invariant | 不变式 | a statement kept true as the computation advances |

## Two spellings, one trace

![[programming-fundamentals-see-it-run.mp4]]

Follow pseudocode and Python side by side as the same running total changes. Predict the next stored value before it appears; then check whether the explanation survives a negative input.

The left-hand examples use **0478's** dialect; the right-hand examples are copyable Python 3. Code within each pair stands alone unless an input or existing array is explicitly specified. Python uses indentation to group statements; Cambridge uses closing keywords as well. The broader A-Level dialect is in [[Cambridge Pseudocode]].

Python identifiers below use `snake_case`; Cambridge examples use `MixedCase`. The mapping is deliberate: `TotalPaid` and `total_paid` play the same role. Python is case-sensitive; Cambridge treats identifiers as case-insensitive, so do not use `Count` and `count` as two different variables on the left. Comments start with `#` in Python and `//` in Cambridge; comments explain the program to people and are not executed.

### 1. Names, values and types

**Declaration** introduces a name and its type; **initialisation** gives it its first value; **assignment** updates it. A declaration alone does not promise zero. 0478 writes a constant declaration as `CONSTANT Name ← literal`, with a literal value rather than an expression. A **constant** is a named value intended to remain unchanged: a tariff belongs in one place so a price change cannot leave half the program using yesterday's price.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Count : INTEGER&#10;CONSTANT UnitPrice ← 250&#10;Count ← 12&#10;Count ← Count + 1&#10;OUTPUT Count</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>UNIT_PRICE = 250&#10;count = 12&#10;count = count + 1&#10;print(count)</code></pre> |

The output is **13**, not a claim that $12=13$. Evaluate the right-hand side using the old state, then replace the left-hand value. `=` tests equality in Cambridge; `==` tests it in Python. Python `=` assigns. `Total += Sale` is Python shorthand for `Total = Total + Sale`, not a new kind of arithmetic.

| Cambridge type | Example declaration and value | Python representation | Why choose it? |
|---|---|---|---|
| `INTEGER` | `DECLARE Count : INTEGER` then `Count ← 3` | `count = 3` (`int`) | whole-number counts |
| `REAL` | `DECLARE Mass : REAL` then `Mass ← 2.75` | `mass = 2.75` (`float`) | measured quantities with fractions |
| `CHAR` | `DECLARE Grade : CHAR` then `Grade ← 'A'` | `grade = "A"` (`str`, length 1) | one character |
| `STRING` | `DECLARE Code : STRING` then `Code ← "007"` | `code = "007"` (`str`) | text or an identifier whose leading zeros matter |
| `BOOLEAN` | `DECLARE Found : BOOLEAN` then `Found ← FALSE` | `found = False` (`bool`) | a yes/no state |

A type controls which operations make sense: `"12" + "3"` joins text; `12 + 3` adds numbers. Python has no separate `CHAR` type. `TRUE`/`FALSE` become `True`/`False`, without quotes. The string `"False"` is still non-empty text, not the Boolean `False`.

**Python's honest edge:** names refer to objects and can be rebound to a different type. A type hint such as `count: int = 0` documents intent but does not enforce it at runtime. Upper-case `UNIT_PRICE = 250` is a convention, not a lock. A shallow “box” picture works for integer examples; for shared mutable objects, use [[Arrays]]'s aliasing model.

### 2. Sequence, input and output

**Trigger:** a calculation needs a value supplied by a person → input first, compute second, output third. Reordering the steps can read an uninitialised value or display an old result.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Name : STRING&#10;DECLARE Quantity : INTEGER&#10;DECLARE Cost : INTEGER&#10;CONSTANT UnitPrice ← 250&#10;OUTPUT "Name?"&#10;INPUT Name&#10;OUTPUT "Quantity?"&#10;INPUT Quantity&#10;Cost ← Quantity * UnitPrice&#10;OUTPUT Name, ": ", Cost, " cents"</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>UNIT_PRICE = 250&#10;name = input("Name? ")&#10;quantity = int(input("Quantity? "))&#10;cost = quantity * UNIT_PRICE&#10;print(f"{name}: {cost} cents")</code></pre> |

Inputs `Ada`, `3` give `Ada: 750 cents`. Python `input()` always returns text; `int(...)` converts whole-number text. `print` sends a value to the screen; an f-string puts expressions inside `{...}` into text. `int("three")` raises `ValueError`: a program exposed to arbitrary users must validate or handle conversion failures ([[Program Development Life Cycle and Testing]], [[File Processing and Exception Handling]]). The short input examples assume the declared numeric type is supplied.

### 3. Operators: ask what the operands mean

| Job | Cambridge | Python | Example / result |
|---|---|---|---|
| arithmetic | `+`, `-`, `*`, `/` | same symbols | `7 / 2` gives `3.5` |
| power | `2 ^ 3` | `2 ** 3` | `8`; Python `^` means bitwise XOR |
| whole quotient | `DIV(17, 5)` or `17 DIV 5` | `17 // 5` | `3` for these non-negative operands |
| remainder | `MOD(17, 5)` or `17 MOD 5` | `17 % 5` | `2` |
| comparisons | `=`, `<>`, `<`, `<=`, `>`, `>=` | `==`, `!=`, `<`, `<=`, `>`, `>=` | produce a Boolean |
| Boolean combination | `AND`, `OR`, `NOT` | `and`, `or`, `not` | use Boolean conditions as operands |

**Why quotient and remainder work:** for non-negative $a$ and positive $b$, $a=bq+r$ with $0\le r<b$. `DIV` counts complete groups; `MOD` counts what remains. For 367 seconds, `DIV(367,60)=6` minutes and `MOD(367,60)=7` seconds. A factor test is `MOD(n,d)=0`; a circular index is `MOD(index+1,size)` ([[Stacks and Queues]]).

**Do not silently extend the translation to negatives.** Cambridge describes `DIV` as discarding the fractional part; Python `//` floors: `-7 // 3 == -3`, while truncating $-7/3$ gives $-2$. Python `%` satisfies the identity with its floor quotient (`-7 % 3 == 2`). All paired division examples use non-negative operands and positive divisors. Zero divisors are invalid.

For a permitted integer age 12–17, write `(Age >= 12) AND (Age <= 17)` / `(age >= 12) and (age <= 17)`. To reject it, write `(Age < 12) OR (Age > 17)` / `(age < 12) or (age > 17)`. The second is **NOT** the first: De Morgan's law reverses the comparisons and exchanges AND/OR. `Age = 12 OR 13` is not two comparisons. Parentheses make the intended grouping visible.

Python evaluates `and`/`or` left to right and short-circuits. Do not assume a pseudocode implementation will protect an invalid operation the same way: an outer bounds check before indexing is clearer in either language.

### 4. Selection: one choice or several independent tests?

**Trigger:** the next action depends on a range or combined condition → `IF`. A single value chooses one of several exact alternatives → `CASE`. A true `IF` executes its branch; otherwise `ELSE` executes. Without `ELSE`, false means skip the branch entirely.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Choice : INTEGER&#10;INPUT Choice&#10;CASE OF Choice&#10;  1 : OUTPUT "Tea"&#10;  2 : OUTPUT "Coffee"&#10;  OTHERWISE OUTPUT "Unknown"&#10;ENDCASE</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>choice = int(input())&#10;if choice == 1:&#10;    print("Tea")&#10;elif choice == 2:&#10;    print("Coffee")&#10;else:&#10;    print("Unknown")</code></pre> |

Input `2` gives `Coffee`. Only **one** branch of a CASE or `if`/`elif`/`else` chain runs. Three separate `IF`s can all run: with thresholds `score >= 50` and `score >= 80`, a score of 90 meets both. Put the highest grade first in an exclusive chain, or explicitly restrict each interval. That is a reasoning choice, not merely indentation.

### 5. Iteration: decide when the test belongs

| Trigger | Cambridge | Test and minimum executions | Python |
|---|---|---|---|
| count known before starting | `FOR … TO … NEXT` | one visit per stated counter value | `for … in range(...)` |
| continue only while a condition holds | `WHILE … DO … ENDWHILE` | before the body; possibly zero | `while condition:` |
| body must happen before it can be tested | `REPEAT … UNTIL` | after the body; at least once | `while True:` then `if done: break` |

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Index : INTEGER&#10;FOR Index ← 1 TO 3&#10;    OUTPUT Index&#10;NEXT Index</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>for index in range(1, 4):&#10;    print(index)</code></pre> |

Both print **1, 2, 3**. Cambridge includes the last bound; Python excludes the stop. `1 TO n` becomes `range(1,n+1)`. `3 TO 1 STEP -1` becomes `range(3,0,-1)`. Equal Cambridge bounds run once; `range(3,3)` is empty. Count the **values visited**, not the punctuation.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Count : INTEGER&#10;Count ← 0&#10;WHILE Count &lt; 3 DO&#10;    Count ← Count + 1&#10;    OUTPUT Count&#10;ENDWHILE</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>count = 0&#10;while count &lt; 3:&#10;    count = count + 1&#10;    print(count)</code></pre> |

Both print **1, 2, 3**. Before each pass, `count` is the number already printed; incrementing it makes progress towards 3. Starting at 3 prints nothing. A loop needs both a stopping condition and an update that can make it stop; a condition alone does not promise termination.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Score : INTEGER&#10;REPEAT&#10;    INPUT Score&#10;UNTIL (Score &gt;= 0) AND (Score &lt;= 100)&#10;OUTPUT Score</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>while True:&#10;    score = int(input())&#10;    if (score &gt;= 0) and (score &lt;= 100):&#10;        break&#10;print(score)</code></pre> |

Inputs `-1, 101, 75` accept only `75`. **`UNTIL` states when to stop; `WHILE` states when to continue.** A direct `while done` translation reverses the meaning. `break` exits the nearest Python loop; it is not an extra Cambridge keyword to invent.

### 6. Totalling, counting, extrema: the invariant is the algorithm

A **total** adds values; a **count** adds one per event. Before a loop both are zero, because no events have occurred. After processing $k$ values, the total must equal their sum and the count must equal $k$. Adding the next value and one event preserves the claim; at termination it proves the answer. This is [[Proof by Induction]] performed by a program.

For positive sales in integer cents, use the complete sales program under “Where it is the working tool.” It also counts only **accepted** sales. An average is `total / count`, calculated after checking `count > 0`. Rounding after every addition can accumulate error; keep the exact total and round the displayed average once.

**Maximum/minimum:** initialise from the **first actual value** when one exists, then replace the candidate only when a better value arrives. Initialising a maximum to zero fails for `-8, -3, -12`: the real maximum is `-3`, not zero. Empty input has no maximum unless the specification defines one.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Smallest : INTEGER&#10;DECLARE Largest : INTEGER&#10;DECLARE Value : INTEGER&#10;DECLARE Index : INTEGER&#10;INPUT Value&#10;Smallest ← Value&#10;Largest ← Value&#10;FOR Index ← 2 TO 3&#10;    INPUT Value&#10;    IF Value &lt; Smallest THEN&#10;        Smallest ← Value&#10;    ENDIF&#10;    IF Value &gt; Largest THEN&#10;        Largest ← Value&#10;    ENDIF&#10;NEXT Index&#10;OUTPUT Smallest, ", ", Largest</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>value = int(input())&#10;smallest = value&#10;largest = value&#10;for index in range(2, 4):&#10;    value = int(input())&#10;    if value &lt; smallest:&#10;        smallest = value&#10;    if value &gt; largest:&#10;        largest = value&#10;print(f"{smallest}, {largest}")</code></pre> |

Inputs `-8, -3, -12` output `-12, -3`. Invariant: the two candidates are the smallest/largest values seen so far. The input count of three guarantees a first value; unknown-length input needs an explicit “have seen a value” flag or an empty-case branch.

### 7. Strings: the third argument is a length, not an end position

![[programming-substring-positions.svg|700]]

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Text : STRING&#10;Text ← "Hello"&#10;OUTPUT LENGTH(Text)&#10;OUTPUT SUBSTRING(Text, 2, 3)&#10;OUTPUT UCASE(Text)&#10;OUTPUT LCASE(Text)</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>text = "Hello"&#10;print(len(text))&#10;print(text[1:4])&#10;print(text.upper())&#10;print(text.lower())</code></pre> |

Both output `5`, `ell`, `HELLO`, `hello`. With a Cambridge first position of 1, **`SUBSTRING(Text, Start, Length)` → `text[start-1 : start-1+length]`**. If the question explicitly starts at zero, use `text[start:start+length]` instead. State and keep one indexing convention; 0478 permits either, but its published examples generally start at one.

A Python slice includes the start and excludes the stop; `text[1:4]` has three characters. `text[4]` has one. A string's length is a count, not its last zero-based index. Python strings are immutable: `text.upper()` returns a new string; write `text = text.upper()` if the original name should refer to the changed value.

**Real-world edge:** Python counts Unicode code points, not necessarily visible glyphs; case conversion can change length (`"ß".upper()` is `"SS"`). The paired examples use simple Latin text; do not silently treat those properties as universal text laws ([[Text Encoding]]).

### 8. Procedures, functions, arguments and scope

**Trigger:** an action has a useful name, repeats, or hides a detail → package it as a subprogram. A **procedure** performs an action; a **function** returns a value to be used by its caller. A **parameter** is the name written in the definition; an **argument** is what a call supplies. `quantity` and `unit_price` are parameters; `3` and `250` are arguments below.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>FUNCTION OrderCost(Quantity : INTEGER,&#10;    UnitPrice : INTEGER) RETURNS INTEGER&#10;    RETURN Quantity * UnitPrice&#10;ENDFUNCTION&#10;&#10;OUTPUT OrderCost(3, 250)</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>def order_cost(quantity, unit_price):&#10;    return quantity * unit_price&#10;&#10;print(order_cost(3, 250))</code></pre> |

The function computes **750** but does not display it; the caller's output statement does. Python uses `def` for both procedures and functions; a function with no explicit return yields `None`. `return` finishes the call and hands back a value; `print` merely writes to the screen. Cambridge calls a procedure with `CALL`, but uses a function inside an expression, with no `CALL`.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>PROCEDURE ShowHeading&#10;    OUTPUT "Sales"&#10;ENDPROCEDURE&#10;FUNCTION DefaultLimit RETURNS INTEGER&#10;    RETURN 100&#10;ENDFUNCTION&#10;CALL ShowHeading&#10;OUTPUT DefaultLimit()</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>def show_heading():&#10;    print("Sales")&#10;&#10;def default_limit():&#10;    return 100&#10;&#10;show_heading()&#10;print(default_limit())</code></pre> |

No arguments are needed to print a fixed heading or supply a fixed limit. A Python definition's `()` remains even when empty. Cambridge's parameterless definition omits the parameter list, and its value-returning function call uses `()`.

**Scope** determines where a name can be used. A variable declared inside a procedure/function is **local** to that call; a variable declared outside subprograms is **global** in Cambridge's simple program model. A Python global belongs to its **module**, not every file on the computer. Parameters are local names.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>PROCEDURE ShowLocal&#10;    DECLARE Score : INTEGER&#10;    Score ← 99&#10;    OUTPUT Score&#10;ENDPROCEDURE&#10;DECLARE Score : INTEGER&#10;Score ← 10&#10;CALL ShowLocal&#10;OUTPUT Score</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>def show_local():&#10;    score = 99&#10;    print(score)&#10;&#10;score = 10&#10;show_local()&#10;print(score)</code></pre> |

Both display **99, then 10**: the local `score` shadows the outer name rather than rewriting it. A new call gets fresh local state. Python assignment inside a function makes that name local unless declared `global` (or `nonlocal` for an enclosing function); merely reading a global does not need `global`. Rebinding a global with `global score` is possible, but passing inputs and returning outputs makes dependencies visible and tests independent. Python `if`/`for` blocks do **not** create a new local scope; functions do.

**Beyond the scalar model:** passing a list does not copy all its elements. Mutating the shared list can affect the caller; rebinding a parameter does not rebind the caller's name. Python uses object sharing, not Cambridge's explicit `BYREF` variable alias. [[Arrays]] and [[User-Defined Data Types]] develop that distinction.

### 9. Nested statements: each outer pass gets its own inner run

A nested loop is a loop inside another; nested selection is an `IF` inside a branch. **Trigger:** “for each row, visit every column” → two loops. With three rows and four columns, the body runs $3\times4=12$ times, because the inner counter restarts for each row. Two loops one after another instead run $3+4=7$ times.

An inner `IF` is checked only after control reaches it: “if the name is present, then if the amount is positive, accept the transaction.” The outer check can establish the precondition for the inner operation. Indentation and matching terminators tell you which branch owns which statements; real contact-entry code appears in Worked Example 2.


| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Name : STRING&#10;DECLARE Amount : INTEGER&#10;INPUT Name&#10;INPUT Amount&#10;IF LENGTH(Name) &gt; 0 THEN&#10;    IF Amount &gt; 0 THEN&#10;        OUTPUT "Accepted"&#10;    ELSE&#10;        OUTPUT "Rejected amount"&#10;    ENDIF&#10;ELSE&#10;    OUTPUT "Missing name"&#10;ENDIF</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>name = input()&#10;amount = int(input())&#10;if len(name) &gt; 0:&#10;    if amount &gt; 0:&#10;        print("Accepted")&#10;    else:&#10;        print("Rejected amount")&#10;else:&#10;    print("Missing name")</code></pre> |

For `Ada, 250`, output is `Accepted`; `Ada, 0` reaches the inner `ELSE`, while an empty name reaches the outer `ELSE` whatever the amount. Read the indentation to identify which question each `ELSE` answers.

### 10. Library routines: a contract you still have to read

A **library routine** is reusable code provided for you. Read its accepted inputs, returned value and edge cases; calling a routine transfers the implementation work, not responsibility for choosing it. `DIV` and `MOD` were the group-counting pair above.

| Routine | Cambridge | Python | Contract / difference |
|---|---|---|---|
| rounding | `ROUND(12.346, 2)` | `round(12.346, 2)` | both give `12.35` for this example |
| random real | `RANDOM()` | `random.random()` after `import random` | Cambridge specifies $0\le u\le1$; Python $0\le u<1$ |
| uniform die, real code | no direct 0478 die routine | `random.randint(1, 6)` | integers 1 through 6, inclusive |

Python `round` uses ties-to-even (`round(2.5)==2`, `round(3.5)==4`); Cambridge's 0478 description does **not** specify tie-breaking. Binary floats add another issue: `round(2.675,2)==2.67`. For money, keep integer cents or choose a decimal rounding policy explicitly. Formatting to two printed decimal places is also different from changing a stored value ([[Floating-Point Representation]]).

**A library example is not automatically a fair game.** `ROUND(RANDOM()*6,0)` can output **0 through 6**, so it is not a six-sided die. For an ideal uniform real on [0,1], 0 and 6 each collect an interval of width $1/12$; 1 through 5 each collect $1/6$. The endpoints are half as likely. Range alone is not a distribution. In runnable code use `randint(1,6)`; do not invent `INT` or an undocumented `RANDOM(1,6)` for a question that gives only `RANDOM()`.

### 11. Maintainability: make the next change local

A maintainable program is easy to understand, test and modify without breaking unrelated behaviour. Use meaningful names for **variables, constants, arrays and subprograms**; `contacts`, `sale_count`, `STOP_VALUE` and `order_cost` advertise their jobs. Name the invariant in a comment, not just the arithmetic: “sum of accepted sales” explains why `total` is here; “add sale to total” repeats the statement.

Extract a repeated rule into a procedure/function so a correction has one home. Name fixed values as constants. Indent consistently, separate logical sections, and document unusual syntax where it would otherwise surprise a maintainer. A comment that disagrees with the code is a second bug. [[Program Design]] supplies the decomposition; [[Program Development Life Cycle and Testing]] supplies the checks that make a later edit safe.

## Where it is the working tool — a sales summary

A shop's daily transaction stream, a game's damage log and a lab's accepted measurements all use the same **streaming accumulator**: one input at a time, a total and a count, no need to retain the whole history. Memory use stays constant even when the stream grows. Here amounts are integer cents; zero ends entry, negatives are rejected, and positive values are accepted.

**Tool and trigger:** unknown number of entries → sentinel-controlled `WHILE`; accepted-event count → increment **inside** the positive branch; empty stream → guard the average. Sentinel 0 is excluded from the sum and count. Read once before the loop and once at its end so every path obtains a fresh input.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Sale : INTEGER&#10;DECLARE Total : INTEGER&#10;DECLARE Count : INTEGER&#10;CONSTANT StopValue ← 0&#10;Total ← 0&#10;Count ← 0&#10;INPUT Sale&#10;WHILE Sale &lt;&gt; StopValue DO&#10;    IF Sale &gt; 0 THEN&#10;        // Sum of accepted sales&#10;        Total ← Total + Sale&#10;        Count ← Count + 1&#10;    ELSE&#10;        OUTPUT "Rejected"&#10;    ENDIF&#10;    INPUT Sale&#10;ENDWHILE&#10;IF Count &gt; 0 THEN&#10;    OUTPUT Count, " sales; ", Total&#10;    OUTPUT "Mean cents: ", Total / Count&#10;ELSE&#10;    OUTPUT "No sales"&#10;ENDIF</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>STOP_VALUE = 0&#10;# Sum and count of accepted sales&#10;total = 0&#10;count = 0&#10;sale = int(input())&#10;while sale != STOP_VALUE:&#10;    if sale &gt; 0:&#10;        total = total + sale&#10;        count = count + 1&#10;    else:&#10;        print("Rejected")&#10;    sale = int(input())&#10;if count &gt; 0:&#10;    print(f"{count} sales; {total}")&#10;    print(f"Mean cents: {total / count}")&#10;else:&#10;    print("No sales")</code></pre> |

Inputs `250, -20, 375, 0` produce **2 sales, 625 cents, mean 312.5 cents**; input `0` alone reports no sales. Move `count += 1` outside the `if` and the rejected transaction corrupts the mean; reset `total` inside the loop and only the latest sale survives. These are violations of the invariant, not mysterious syntax failures.

**What would this do in a real shop?** Suppose a till exports completed sale amounts in cents. The same loop can produce the day's sales count, revenue and average sale value without keeping every amount in memory. Integer cents preserve the total exactly: a price of 2.50 is stored as `250`, avoiding binary floating-point approximations during addition. The average may include a fraction of a cent; choose a rounding rule when displaying it.

Each fundamental has a job: **input** obtains the next transaction; **selection** decides whether it belongs in the summary; **iteration** processes however many arrive; **variables** preserve the running facts; a **function** can package that calculation for a report or dashboard. The invariant—total and count describe exactly the accepted entries so far—is what makes the displayed result trustworthy.

The runnable version deliberately accepts integer text and positive sales only. It rejects negative entries; a real refund is not an invalid sale and needs its own transaction type and accounting rule. A production importer also needs safe parsing, duplicate detection and saved records for reconciliation. File input normally ends at end-of-file rather than a typed zero. Those choices change what is accepted; once that policy is defined, the same total-and-count pattern does the calculation.

## Worked Examples — real Paper 2 questions

### 1. Detect an @ — 0478/22/O/N/25 Q4(b), 6 marks

**Task, paraphrased:** input an address and report whether it contains `@`; use `SUBSTRING(EmailAddress, Start, 1)`, initialise what is needed, and assume at most one `@`. Declarations are not required in this question.

**Tool 1 — bounded traversal:** search an unknown-length string → advance an index until a match or exhaustion. **Tool 2 — flag:** remember whether the match was found. **Tool 3 — pre-condition loop:** empty text must never be indexed. The scheme shows a post-test solution; a pre-test loop also satisfies its working-loop criterion and handles the empty case cleanly.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>INPUT EmailAddress&#10;Start ← 1&#10;Found ← FALSE&#10;WHILE (Start &lt;= LENGTH(EmailAddress))&#10;      AND (NOT Found) DO&#10;    IF SUBSTRING(EmailAddress,&#10;                 Start, 1) = "@" THEN&#10;        Found ← TRUE&#10;    ELSE&#10;        Start ← Start + 1&#10;    ENDIF&#10;ENDWHILE&#10;IF Found THEN&#10;    OUTPUT "Valid"&#10;ELSE&#10;    OUTPUT "Invalid"&#10;ENDIF</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>email_address = input()&#10;start = 0&#10;found = False&#10;while (start &lt; len(email_address)&#10;       and not found):&#10;    if email_address[start:start+1] == "@":&#10;        found = True&#10;    else:&#10;        start = start + 1&#10;if found:&#10;    print("Valid")&#10;else:&#10;    print("Invalid")</code></pre> |

`a@b` is reported valid, `ab` and empty text invalid. The scheme awards up to six across initialisation, input, a working condition-controlled loop, `SUBSTRING`, comparison, termination/progression, and both outputs. Python's idiomatic test is simply `"@" in email_address`; the loop exposes the same search. **This is only the question's presence check:** it does not establish that an address is well formed, that the domain exists, or that a mailbox can receive mail.

### 2. Contacts — 0478/22/O/N/25 Q2(b)(i–ii), 4 + 2 marks

**Task, paraphrased:** complete `NewData(Number : INTEGER)` so it fills the first `Number` rows of an existing `Contacts` array, four fields per row; then input how many rows and call it. The array already exists. Assume the count is within its capacity; the Python setup below gives it 100 rows.

**Tool 1 — parameter:** row count varies between calls, so it enters through `Number`. **Tool 2 — nested traversal:** each row owns four inputs, so restart the inner counter for every row. The two closing statements must match the two loop counters.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>// Contacts already exists&#10;PROCEDURE NewData(Number : INTEGER)&#10;    DECLARE Row : INTEGER&#10;    DECLARE Column : INTEGER&#10;    FOR Row ← 1 TO Number&#10;        FOR Column ← 1 TO 4&#10;            INPUT Contacts[Row, Column]&#10;        NEXT Column&#10;    NEXT Row&#10;ENDPROCEDURE&#10;DECLARE MyNumber : INTEGER&#10;INPUT MyNumber&#10;CALL NewData(MyNumber)</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code># Existing capacity: 100 rows&#10;contacts = [[""] * 4 for _ in range(100)]&#10;&#10;def new_data(number):&#10;    for row in range(number):&#10;        for column in range(4):&#10;            contacts[row][column] = input()&#10;&#10;my_number = int(input())&#10;new_data(my_number)</code></pre> |

For input `2` followed by eight fields, rows 1–2 on the left correspond to Python rows 0–1. The four fill-in marks are the typed parameter, outer bound using `Number`, indexed array input, and both loop endings. The remaining two are the input statement and correct procedure call. `contacts[row][column] = ...` mutates the existing list, so Python needs no `global` statement. For general software, passing the destination explicitly makes that dependency clearer.

### 3. Discover the purpose — 0478/22/M/J/25 Q6(a–c), 6 + 1 + 3 marks

**Task, paraphrased:** trace a supplied algorithm on `2, RACECAR, TREAT`, identify its purpose, and explain the stopping rule. For each word it starts two positions at opposite ends, compares their letters, moves inwards after a match and stops on a mismatch or when the positions meet/cross.

**Tool — forward invariant:** every pair *outside* the current positions has matched. Therefore the unexamined middle shrinks without losing the property being checked. The algorithm recognises **palindromes**, words identical forwards and backwards. “It compares letters” describes an operation, not its purpose.

| Word | Positions compared (Cambridge / Python) | Letters | Next state |
|---|---|---|---|
| `RACECAR` | `(1,7)` / `(0,6)` | `R`, `R` | move inwards |
| `RACECAR` | `(2,6)` / `(1,5)` | `A`, `A` | move inwards |
| `RACECAR` | `(3,5)` / `(2,4)` | `C`, `C` | positions meet at 4 / 3; output `Successful` |
| `TREAT` | `(1,5)` / `(0,4)` | `T`, `T` | move inwards |
| `TREAT` | `(2,4)` / `(1,3)` | `R`, `A` | flag becomes false; output `NOT successful` |

This compact trace records comparisons; on the paper, fill every requested variable column as the scheme does, including the unchanged input count and each outer-loop index. There is no need to compare a central character with itself. For even-length words, positions **cross**; using only “until equal” would miss that case.

| Cambridge 0478 pseudocode | Python 3 |
|---|---|
| <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>DECLARE Word : STRING&#10;DECLARE Number : INTEGER&#10;DECLARE Index : INTEGER&#10;DECLARE LeftPos : INTEGER&#10;DECLARE RightPos : INTEGER&#10;DECLARE Continue : BOOLEAN&#10;INPUT Number&#10;FOR Index ← 1 TO Number&#10;    INPUT Word&#10;    Continue ← TRUE&#10;    LeftPos ← 1&#10;    RightPos ← LENGTH(Word)&#10;    WHILE Continue AND&#10;          (LeftPos &lt; RightPos) DO&#10;        IF SUBSTRING(Word, LeftPos, 1)&#10;           &lt;&gt; SUBSTRING(Word, RightPos, 1)&#10;           THEN&#10;            Continue ← FALSE&#10;        ELSE&#10;            LeftPos ← LeftPos + 1&#10;            RightPos ← RightPos - 1&#10;        ENDIF&#10;    ENDWHILE&#10;    IF Continue THEN&#10;        OUTPUT "Successful"&#10;    ELSE&#10;        OUTPUT "NOT successful"&#10;    ENDIF&#10;NEXT Index</code></pre> | <pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>number = int(input())&#10;for index in range(number):&#10;    word = input()&#10;    keep_checking = True&#10;    left_pos = 0&#10;    right_pos = len(word) - 1&#10;    while (keep_checking&#10;           and left_pos &lt; right_pos):&#10;        if word[left_pos] != word[right_pos]:&#10;            keep_checking = False&#10;        else:&#10;            left_pos = left_pos + 1&#10;            right_pos = right_pos - 1&#10;    if keep_checking:&#10;        print("Successful")&#10;    else:&#10;        print("NOT successful")</code></pre> |

The paired version preserves the supplied algorithm's structure, with descriptive names and zero-based Python positions. At most half the word's characters are compared: $O(n)$ time and $O(1)$ extra space. `word == word[::-1]` is a useful real-code shorthand, but constructs a reversed string. Try `""`, `"A"`, `"AA"`, `"AB"` as well as the paper's words; explain why each stops.

### 4. Rounding a report — 0478/22/M/J/25 Q5(b), 2 marks

**Trigger:** a total of 500 heights is already available; the output must be the mean to one decimal place → divide **before** rounding. The matching statements are `OUTPUT ROUND(Total / 500, 1)` and `print(round(total / 500, 1))`. One mark is for outputting the correct mean; the other is the one-decimal rounding. For `Total = 86123`, both give **172.2**. `ROUND(Total,1)/500` rounds the wrong quantity.

### 5. Explain maintainability — 0478/22/F/M/24 Q10, 6 marks

**Trigger:** “explain” → give a technique **and what it buys the next programmer**, not a list of adjectives. Three defensible pairs are: meaningful identifiers reveal each value's purpose; comments explain a section's logic or unusual syntax; procedures/functions remove repeated code and isolate changes. The scheme also accepts indentation/white space with readability as its reason. Each technique-plus-explanation earns up to two, maximum six. Point to `STOP_VALUE`, the sales invariant and `order_cost` for concrete examples.

## Hands-on — run it, break it, explain the failure

Run `python3 programming-fundamentals.py` beside the accompanying source. It checks the sales, extrema, string search, contact entry, palindrome and rounding examples; exhaustively tests short strings; and measures the seven-outcome rounding construction on evenly spaced inputs. `python3 programming-fundamentals.py --sales` runs the interactive sales summary.

1. Move the sales count outside the acceptance branch; predict the result for `250,-20,375,0`, then run it.
2. Replace the palindrome condition `<` with `<>` / `!=`; test an even-length palindrome and explain the crossing failure before fixing it.
3. Change the substring start from 2 to 1; predict both slices. Explain why subtracting one from **both** arguments is wrong.
4. Rewrite the three-value extrema routine to accept a sentinel-ended stream, including no values. State its invariant before writing either language.

## Common Misconceptions (Teaching Notes)

- **“Assignment is an equation.”** Trace the old right-hand value before the write; `x ← x+1` changes state, it does not solve for $x$.
- **“WHILE and UNTIL are synonyms.”** Mark a condition as **keep going** or **stop now**, then check a first-pass and zero-pass case.
- **“A total and a count are interchangeable.”** One counts events, the other measures their combined value. Two sales need not total two cents.
- **“Printing returns the answer.”** Give a function's result to a second calculation; if it only prints, the caller receives no usable numeric answer.
- **“A variable with the same name is the same variable.”** Label each call's local names and the module's global names separately; then trace the 99/10 example.
- **“All random outcomes in a stated range are equally likely.”** Measure the intervals mapped to each integer; the rounding example's endpoints receive half the interval width.

## Exam Notes

### Cambridge 0478 IGCSE

**§8.1.1–8:** variables/constants, five types, I/O, sequence/selection/iteration, totalling/counting, strings, operators, nesting, subprograms/parameters/scope, library routines and maintainability. The syllabus limits requested nesting to **three levels** and procedures/functions to **two parameters**; these are assessment limits, not limits of computation. **§7.3** purpose is practised by the palindrome; **§7.4** standard accumulators and extrema join [[Searching]]/[[Sorting]]; **§7.9** writing/amending algorithms joins [[Program Design]]'s flowcharts. Arrays and files are **§8.2 / §8.3**, developed in [[Arrays]] and [[File Handling]].

**Paper 2:** coding answers must use pseudocode; real programming code receives no marks there **except the 15-mark scenario**, which permits pseudocode, Python, Visual Basic or Java. Practise both translations, then obey the question's requested representation. 0478 has its own conventions in the syllabus, with no A-Level-style function insert. `SUBSTRING`, `LCASE` and `UCASE` are its spellings; do not import the 9618 insert's `MID` or `TO_UPPER` without a question defining them.

**Writing checklist:** initialise accumulators/flags; use assignment arrows; close blocks; keep bounds consistent; advance on every continuing path; return a function value; call a procedure; output the requested result. Supply declarations when required, and omit them when the question explicitly says they are unnecessary. Cambridge's **WHILE** form includes `DO`; its **CONSTANT** declaration uses `←`. Do not borrow `CONSTANT Name = value` from the A-Level guide.

### Cambridge 9618 AS & A Level

**§11.1** programming basics and **§11.2** constructs directly reuse these ideas; **§11.3** adds structured programming, interface vocabulary and explicit pass-by-value/reference. [[Cambridge Pseudocode]] owns the latter dialect details. **Paper 2 is a written pseudocode paper**, assessing §§9–12; it is not the practical. **Paper 4** is the computer-based practical in Python, Java or Visual Basic .NET. Paper 3 can also demand pseudocode. The Paper 2 insert supplies built-ins; read the insert rather than assuming 0478 spellings transfer.

### IB Computer Science

For **first assessment 2027**, Theme **B2 Programming** is examined in Paper 2 with **Java or Python** answers. Variables/operators/I/O and selection/iteration overlap the tracked **B2.1 / B2.3** topics. The official public course outline confirms the theme and language choice; detailed statement-level completeness remains unverified against the full guide, so this is conceptual support, not a claim to cover all IB-specific requirements. The outgoing course through 2026 uses different conventions; do not mix its guidance with the 2027 course.

### AP Computer Science A

The current four-unit CED places these ideas in **1.2–1.9** (variables, expressions, assignment, conversion, API use, comments and signatures), **1.15** (strings), **Unit 2** (selection/iteration), and **3.8** (scope). **Answers are Java**, so Python proficiency alone is insufficient: Java needs declared types, braces, `&&`/`||`/`!`, `.equals()` for string content, and explicit parameter/return types. Its integer division truncates; `String.substring(start,stop)` has zero-based/exclusive bounds. The Java side of these topics, compiled and run, is [[Java Values and Expressions]]. The CED excludes input typed at the keyboard. It does not exclude `Scanner`: topic 4.6 reads text files with `Scanner(File)`, and `nextInt`, `nextDouble`, `nextBoolean`, `nextLine`, `next`, `hasNext` and `close` are all on the Java Quick Reference, so learn `Scanner` for files and not for the keyboard.

**Where these spellings are not examined:** Cambridge 0478 pseudocode is not the answer language for AP CSA or IB's 2027 Paper 2, nor for 9618 Paper 4. Programming constructs belong to the CS courses, not standalone programming objectives on the tracked Cambridge maths/physics boards (0580/0606/9709/9231/0625/9702).

## Beyond the syllabus — the loop is a small proof

Recall that an invariant survives every iteration. Correctness has **two** jobs: show the result is right *if the loop finishes*, and show it finishes. In the palindrome search, matched outer pairs establish the first; the shrinking distance between the positions establishes the second. An invariant with no progress argument can describe an infinite loop perfectly. This distinction leads to program verification and formal loop invariants, while the same question “what stays true?” already powers [[Forward Reading and Problem Discovery]].

Recall also that a function makes inputs and outputs explicit. A function with no hidden state and no side effects can be tested as a mapping; the same arguments give the same result. That is the useful core of functional programming in [[Programming Paradigms]], not a demand to ban all loops or screen output.

## Connections

- **Design:** [[Program Design]] — decomposition and the invariant questions that select modules.
- **Dialect peer:** [[Cambridge Pseudocode]] — A-Level declarations, parameter passing and the paper-specific built-ins.
- **Next structures:** [[Arrays]] — storing a sequence of values; [[Program Development Life Cycle and Testing]] — validation, tracing and tests that challenge the program.
- **Mathematical floor:** [[Proof by Induction]] — why an invariant established once and preserved at every step reaches the end.
- **Working consequences:** [[File Handling]] — persistent input streams; [[Searching]] / [[Sorting]] — larger algorithms assembled from these constructs.
- **Human history:** [[The Arrow That Pointed the Other Way]] — why assignment has two competing spellings.

## Sources

Cambridge syllabuses: **0478 (2026–28), pp. 25, 27–29, 34–48**; **9618 (2027–29), §§11.1–11.3 and assessment details**. Worked questions checked against the published question papers and mark schemes: **0478/22/O/N/25 Q2(b), Q4(b); 0478/22/M/J/25 Q5(b), Q6; 0478/22/F/M/24 Q10**. Tasks above are paraphrased; paired solutions are teaching implementations, not claims that only one answer scores.

Python semantics: [control flow](https://docs.python.org/3/tutorial/controlflow.html), [arithmetic expressions](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations), [built-in functions](https://docs.python.org/3/library/functions.html), [random library](https://docs.python.org/3/library/random.html). Cross-board assessment: [IB's official 2027 update](https://ibo.org/university-admission/latest-curriculum-updates/computer-science-updates/) and **AP CSA Course and Exam Description, effective Fall 2025**, Units 1–3.

## Notation Reference

| Symbol | Meaning | Python spelling |
|---|---|---|
| `←` | assignment: evaluate right, update left | `=` |
| `=` / `<>` | equality / inequality tests | `==` / `!=` |
| `^` | exponentiation | `**` |
| `DIV` / `MOD` | whole quotient / remainder (non-negative examples) | `//` / `%` |
| $a=bq+r$ | dividend = divisor × quotient + remainder | `a == b*q + r` |

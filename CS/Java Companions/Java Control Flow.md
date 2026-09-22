---
chinese: Java 的流程控制 (Java de liúchéng kòngzhì)
prerequisites:
  - "[[Java Objects, References and Strings]]"
  - "[[Boolean Algebra]]"
leads_to:
  - "[[Java Classes]]"
tags:
  - subject/computer-science
  - domain/programming
  - domain/java
  - level/A-Level
  - level/pre-AP
  - curriculum/AP-CSA
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - type/companion
  - type/language-reference
  - misconception/indentation-decides-the-block
  - misconception/else-belongs-to-the-if-it-lines-up-with
  - misconception/separate-ifs-are-an-else-if-chain
  - misconception/for-loop-test-runs-after-the-body
  - misconception/nested-loop-count-is-always-n-squared
---

# Java Control Flow Java 的流程控制

> In February 2014 Apple pushed out an urgent security update for iPhones. For over a year, the code that checks whether a secure website is genuine had contained one line too many:
> ```
> if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)
>     goto fail;
>     goto fail;
> ```
> Both lines are indented as if they belong to the `if`. Only the first one does. The second ran every time, the check that mattered was skipped, and forged certificates were accepted. The language was C, and the rule that bit is Java's rule too.

## What this is for

Selection and loops are already yours: [[Programming Fundamentals]] teaches `if`, `while` and `for` in Python, with the standard counting, totalling and searching patterns. Nothing here repeats the ideas. What follows is what Java does differently with them, and the differences are few, sharp, and exactly where a Python habit lets you down.

Every program below is a real file in the folder `java-control-flow`, and every output shown came from compiling and running it. Run `python3 run_all.py` there to reproduce all of it.

**The one idea to carry through:** Python reads your layout. **Java reads your punctuation and ignores your layout.** A block is what lies between `{` and `}`. A condition is what lies between `(` and `)`, and it must be a `boolean`. Indentation is for human readers only, which means it can lie.

An algorithm is built from three things: statements in **sequence**, **selection** between paths on a true-or-false decision, and **repetition** until something is achieved. The order in which they are combined decides the outcome. That is as true of a recipe as of a program.

## 中文锚点

谁都见过那张没有标点的字条：“下雨天留客天留我不留”。主人的意思是：“下雨天留客，天留，我不留。”客人偏偏读成：“下雨天，留客天，留我不？留！”一个字都没变，意思却完全由标点点在哪儿决定。程序里的 if 和 while 碰到的是同一个问题：哪几行算是“条件成立才做”的，哪几行是条件之后照常要做的？Python 靠排版来定：缩进去的就算里面的。Java 靠标点来定：写在花括号里的才算里面的，编译器根本不看排版。所以在 Java 里，你完全可以把一行缩进得看上去像在 if 里面，而花括号却说它在外面，这时候机器每一次都听花括号的。Java 的 if 和循环里那些让人意外的事，大多归结到这一点：眼睛读的是排版，机器读的是标点。

## 1. Braces make the block

Without braces, an `if` controls exactly **one statement**, whatever the indentation suggests (`Misleading.java`, with `score = 30`):

```java
if (score >= 50)
    System.out.println("pass");
    System.out.println("certificate printed");     // indented like the line above; NOT inside the if

if (score >= 50) {
    System.out.println("pass");
    System.out.println("certificate printed");     // the braces put it inside
}
System.out.println("done");
```

```
certificate printed
done
```

A failing student got a certificate. That is Apple's bug in four lines. **Always write the braces**, even round a single statement, and the mistake cannot happen.

A semicolon can do the same damage (`Semicolon.java`). In `if (score >= 50);` the semicolon is a complete, empty statement, and it becomes the body. The block that follows is then an ordinary block that runs every time, so the program prints `pass` for a score of 30. The same slip after a `while (...)` gives a loop with an empty body that never ends.

## 2. The condition must be a boolean

Python will take almost anything as a condition: `if n:`, `if name:`, `if 1 < n < 10:`. Java takes a `boolean` and nothing else (`NotBoolean.java`):

```
if (n)              error: incompatible types: int cannot be converted to boolean
if (n = 5)          error: incompatible types: int cannot be converted to boolean
if (1 < n < 10)     error: bad operand types for binary operator '<'   (first type: boolean, second type: int)
if (s.length())     error: incompatible types: int cannot be converted to boolean
```

Read the third one with the rule from [[Java Values and Expressions]]: `1 < n` is evaluated first and is a `boolean`, and a `boolean` cannot be compared with `10`. Write `1 < n && n < 10`.

The second line is a gift. Typing `=` where you meant `==` is the classic slip, and with numbers the compiler catches it. With a `boolean` it cannot (`AssignTrap.java`):

```java
boolean finished = false;
if (finished = true) {                   // compiles: the value of the assignment IS a boolean
    System.out.println("the game is over");
}
System.out.println(finished);
```

```
the game is over
true
```

The cure is a habit: **never compare a boolean with `true` or `false`.** Write `if (finished)` and `if (!finished)`. They read better, and there is no `==` to mistype.

## 3. Three shapes of selection

| Shape | Java | How many branches run |
|---|---|---|
| one-way | `if (c) { ... }` | one or none |
| two-way | `if (c) { ... } else { ... }` | exactly one |
| multiway | `if (c1) { ... } else if (c2) { ... } else { ... }` | **at most one: the first whose condition is true**; the trailing `else` catches the rest |

Python's `elif` is two words in Java, `else if`. In a multiway selection the conditions are tried from the top, so **their order is part of the logic**. `Branches.java` has the same three tests in two orders:

```java
if (mark >= 80) { return "A"; }                    if (mark >= 50) { return "C"; }
else if (mark >= 65) { return "B"; }               else if (mark >= 65) { return "B"; }
else if (mark >= 50) { return "C"; }               else if (mark >= 80) { return "A"; }
else { return "U"; }                               else { return "U"; }
```

For marks of 91, 65, 64 and 12 the left version returns `A B C U`. The right version returns `C C C U`: the first test catches everyone who passed, and the other two can never be reached. Notice too that the left version never writes `mark >= 65 && mark < 80`. Reaching the second test already means the first one failed.

A row of **separate** `if`s is a different thing. Every condition is tested and several bodies can run, so for a mark of 91 three separate tests of `>= 50`, `>= 65` and `>= 80` build the string `pass merit distinction`.

### Nesting, and the else that goes astray

An `if` may sit inside another, and the inner condition is only evaluated when the outer one is true. With braces left out, the question is which `if` an `else` belongs to. **It belongs to the nearest unmatched `if`**, whatever the layout says (`DanglingElse.java`, with `member = true` and `age = 15`):

```java
if (member)
    if (age >= 18)
        System.out.println("adult member");
else
    System.out.println("not a member");
```

This prints `not a member` for somebody who *is* a member. The `else` lines up with the first `if` and is paired with the second. With braces round both bodies the same program prints nothing, which is correct.

## 4. `&&`, `||`, `!`, and stopping early

| Python | Java | True when | Binds |
|---|---|---|---|
| `not a` | `!a` | `a` is false | tightest |
| `a and b` | `a && b` | both are true | next |
| `a or b` | `a \|\| b` | at least one is true | loosest |

So `a || b && c` means `a || (b && c)`. With `a` true and the others false that is `true`, while `(a || b) && c` is `false`. Add brackets whenever both operators appear; nobody marks you down for clarity.

Java evaluates these from left to right and **stops as soon as the answer is known**. If the left side of `&&` is false the whole thing is false, and the right side is never evaluated. If the left side of `||` is true, the same. This is **short-circuit evaluation**, and `ShortCircuit.java` makes it visible with a method that announces when it is called:

```
[A checked] false                       loud("A", false) && loud("B", true)
[A checked] true                        loud("A", true)  || loud("B", false)
[A checked] [B checked] false           loud("A", true)  && loud("B", false)
```

This is a tool, and you will use it constantly. Put the safety check first and the dangerous expression second:

```java
if (n != 0 && total / n > 5) { ... }                 // the division never happens when n is 0
if (name != null && name.length() > 0) { ... }       // the method is never called on null
```

Swap the two halves and the guard arrives too late. `GuardSecond.java` tests `total / n > 5 && n != 0` and stops with `ArithmeticException: / by zero`.

## 5. Saying the same thing another way: De Morgan's laws

Two boolean expressions are **equivalent** if they give the same value in every case, and a truth table settles the question by listing every case. `DeMorgan.java` prints one:

```
a       b       | !(a&&b) !a||!b  | !(a||b) !a&&!b
true    true    | false   false   | false   false
true    false   | true    true    | false   false
false   true    | true    true    | false   false
false   false   | true    true    | true    true
```

The paired columns agree on every row. Those are **De Morgan's laws**, which [[Boolean Algebra]] proves and which you will use to push a `!` inside a bracket:

$$!(a \;\&\&\; b) \equiv\; !a \;||\; !b \qquad\qquad !(a \;||\; b) \equiv\; !a \;\&\&\; !b$$

*Not both* means *at least one is not*. *Not either* means *both are not*. The `!` goes onto each part **and the operator flips**. A `!` on a comparison flips the comparison:

| Expression | Without the `!` |
|---|---|
| `!(x < y)` | `x >= y` |
| `!(x <= y)` | `x > y` |
| `!(x == y)` | `x != y` |

Together: `!(age >= 18 && hasTicket)` becomes `age < 18 || !hasTicket`. For a 15-year-old with a ticket both print `true`. The most frequent slip is flipping `>=` to `<=` when it should be `<`.

## 6. `while`: test first, then perhaps run

```java
int fuel = 3;
while (fuel > 0) {                       // tested BEFORE every pass, including the first
    System.out.print(fuel + " ");
    fuel--;
}
System.out.println("liftoff");
```

This prints `3 2 1 liftoff`. The condition is evaluated before each pass, **including the first**, so a loop whose condition starts false runs its body zero times. If nothing in the body can ever make the condition false, the loop is **infinite**.

A loop that tests for equality can step over its target. `NeverEqual.java` adds 3 to `n` from 0 while `n != 10`, and goes `3 6 9 12 15 ...`: `n` is never equal to 10. Testing `n < 10` stops it. **Prefer `<` to `!=`** in loop conditions for that reason.

Two patterns matter most.

**Taking an integer apart.** `% 10` reads the last digit and `/ 10` removes it, thanks to int division:

```java
int number = 4096;
int digitSum = 0;
while (number > 0) {
    digitSum += number % 10;
    number /= 10;
}
```
`WhileLoops.java` reports `4 digits, sum 19`. A `while` is right here because nobody knows in advance how many digits there are.

**The sentinel.** Read values until a special one says stop. Read once *before* the loop and again at the *end* of the body, so that the sentinel itself is never processed. With the marks 72, 45, 91, 50, 38 and then `-1`:

```java
int mark = Integer.parseInt(keyboard.nextLine());
while (mark != -1) {
    count++;
    sum += mark;
    if (mark > max) { max = mark; }
    if (mark < min) { min = mark; }
    if (mark >= 50) { passes++; }
    mark = Integer.parseInt(keyboard.nextLine());
}
```

```
5 marks, 3 passes, min 38, max 91
mean 59.2  (and with int division: 59)
```

That one loop holds four of the standard algorithms: **count** the values that meet a condition, find the **maximum** and **minimum**, and compute a **sum** and **average**. Start `max` at `Integer.MIN_VALUE` and `min` at `Integer.MAX_VALUE` so that the first real value replaces them. Cast before dividing, or the mean loses its fraction. The fifth standard algorithm, **divisibility**, is one line: `a % b == 0`.

## 7. `for`: three parts, one order

Python's `for i in range(4)` hides the machinery. Java's header shows all of it:

![[java-control-flow-for-order.svg|820]]

1. The **initialisation** runs once. The variable it sets up, here `i`, is the **loop control variable**.
2. The **condition** is tested before every pass, including the first.
3. The **body** runs.
4. The **update** runs, and control goes back to step 2.

For `i < 4` starting from 0 the body runs 4 times and the test runs 5 times: the fifth test is the one that fails. When the loop ends `i` is 4, and that value was never used inside the body.

| Header | Values of `i` | Passes |
|---|---|---|
| `for (int i = 0; i < 4; i++)` | 0 1 2 3 | 4 |
| `for (int i = 1; i <= 4; i++)` | 1 2 3 4 | 4 |
| `for (int i = 0; i <= 4; i++)` | 0 1 2 3 4 | 5: the classic **off-by-one** |
| `for (int i = 10; i > 0; i -= 3)` | 10 7 4 1 | 4 |

To count passes, use the fact from [[Java Values and Expressions]]: the integers from `lo` to `hi` inclusive number `hi - lo + 1`.

Every `for` is a `while` with the three parts unpacked, and either can be rewritten as the other:

```java
int k = 0;                               // initialisation, once
while (k < 4) {                          // condition, before every pass
    System.out.print(k + " ");
    k++;                                 // update, after the body
}
```

One difference remains. A variable declared in a `for` header exists only inside the loop (`ScopeError.java`): using `i` after the closing brace gives `error: cannot find symbol`. The `k` above was declared outside, and afterwards it still holds 4. Use `for` when the number of passes is known before the loop starts, and `while` when it depends on what happens inside.

## 8. Walking along a String

Java has no `for ch in word`. You walk the **indices**, from `0` to `length() - 1`, and take one character with `substring(i, i + 1)` from [[Java Objects, References and Strings]]. Three standard algorithms, all from `StringLoops.java` with `word = "banana"`:

```java
int vowels = 0;                                              // COUNT the characters with a property
for (int i = 0; i < word.length(); i++) {
    String ch = word.substring(i, i + 1);
    if (ch.equals("a") || ch.equals("e") || ch.equals("i") || ch.equals("o") || ch.equals("u")) {
        vowels++;
    }
}

String reversed = "";                                        // BUILD a new string, here backwards
for (int i = word.length() - 1; i >= 0; i--) {
    reversed += word.substring(i, i + 1);
}

int count = 0;                                               // COUNT substrings: the last legal start is length() - 2
for (int i = 0; i <= word.length() - 2; i++) {
    if (word.substring(i, i + 2).equals("an")) {
        count++;
    }
}
```

The results are `3 vowels`, `ananab` and `2 times "an"`. Characters are compared with `equals`, never `==`. The third loop is where marks are lost: a window of width 2 starting at `i` reaches cut `i + 2`, which must not pass `length()`, so `i` stops at `length() - 2`. In general, **a window of width `w` has its last start at `length() - w`.**

Go one step too far and the program stops. `StringOffByOne.java` loops with `i <= word.length()` over `"cat"`, prints `c`, `a`, `t`, and then: `StringIndexOutOfBoundsException: Range [3, 4) out of bounds for length 3`.

To ask whether **any** character has a property, start a `boolean` at `false` and let one find set it to `true`. To ask whether **all** do, start at `true` and let one failure set it to `false`. An `else` that sets the flag back is the usual bug: it makes the answer depend on the last character alone.

## 9. Loops inside loops

When a loop sits inside another, **the inner loop runs from start to finish for every single pass of the outer one.**

![[java-control-flow-nested-loops.mp4]]

```java
for (int row = 1; row <= 3; row++) {                   // for EACH row ...
    for (int col = 1; col <= 4; col++) {               // ... the inner loop runs from start to finish
        System.out.print(row * col + "\t");
    }
    System.out.println();                              // after the inner loop: once per row
}
```

```
1	2	3	4
2	4	6	8
3	6	9	12
```

Where a statement sits decides how often it runs. The `print` is inside both loops and runs $3 \times 4 = 12$ times. The `println` is inside the outer loop only and runs 3 times.

The inner limit may depend on the outer variable. With `star <= row` the inner loop runs once, then twice, then three times, and a triangle appears. A **statement execution count** is this kind of reasoning made exact, and `Nested.java` checks three of them by counting, with `n = 10`:

| Loops | Innermost statement runs | For `n = 10` |
|---|---|---|
| `i` from 0 to `n - 1`, `j` from 0 to `n - 1` | $n \times n$ | 100 |
| `i` from 0 to `n - 1`, `j` from 0 to `i` | $1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$ | 55 |
| `i` from 1000, halved each pass until 0 | about $\log_2 1000$ | 10 |

Double `n` and the first count is multiplied by four, the second by about four, and the third goes up by one. That comparison, made without any notation, is the beginning of [[Big-O Notation]].

## Python to Java, at a glance

| Idea | Python | Java |
|---|---|---|
| What makes a block | indentation | `{ }`; indentation is ignored |
| Condition | anything, `if n:` | a `boolean` in brackets, `if (n != 0)` |
| Else-if | `elif` | `else if` |
| And, or, not | `and`, `or`, `not` | `&&`, `\|\|`, `!` |
| Range test | `1 < n < 10` | `1 < n && n < 10` |
| Count from 0 to 3 | `for i in range(4):` | `for (int i = 0; i < 4; i++)` |
| Count down | `for i in range(10, 0, -3):` | `for (int i = 10; i > 0; i -= 3)` |
| Each character | `for ch in word:` | `for (int i = 0; i < word.length(); i++)` with `word.substring(i, i + 1)` |
| Loop variable afterwards | still exists | gone, if declared in the header |
| Same characters? | `ch == "a"` | `ch.equals("a")` |
| Reverse a string | `word[::-1]` | a loop |
| Do nothing | `pass` | `{ }` |

## Worked examples

### Example 1: trace a loop with a selection inside

```java
int total = 0;
for (int i = 1; i <= 6; i++) {
    if (i % 2 == 0) {
        total += i;
    } else if (i % 3 == 0) {
        total -= i;
    }
}
```
*Trigger: a short loop with branching, and a request for a final value. Tool: a trace table, one row per pass, applying first-true-wins.*

| `i` | even? | else: multiple of 3? | `total` |
|---|---|---|---|
| 1 | no | no | 0 |
| 2 | yes | | 2 |
| 3 | no | yes | -1 |
| 4 | yes | | 3 |
| 5 | no | no | 3 |
| 6 | **yes** | not tested | 9 |

The answer is **9**. The row that catches people is 6: it is a multiple of 3, but the first condition is already true, so the `else if` is never reached.

### Example 2: remove the `!`

Rewrite `!(temp > 30 || !raining)` without a `!` in front of the bracket.

*Trigger: a negated compound condition. Tool: De Morgan, then flip each comparison.*

The `!` goes onto each part and `||` becomes `&&`: `!(temp > 30) && !(!raining)`. Flip the comparison and cancel the double negative: **`temp <= 30 && raining`**. Check one case: `temp = 25`, raining. The original is `!(false || false)`, which is `true`; the new one is `true && true`, which is `true`.

### Example 3: how many times?

```java
for (int i = 2; i <= 20; i += 3) {
    for (int j = i; j > 0; j -= 5) {
        count++;
    }
}
```
*Trigger: a request for an execution count where the inner loop depends on the outer variable. Tool: list the outer values, count the inner passes for each, and add.*

Outer values: 2, 5, 8, 11, 14, 17, 20. For each, `j` starts at `i` and drops by 5 while positive: 2 gives one pass; 5 gives one (5, then 0 stops it); 8 gives two (8, 3); 11 gives three (11, 6, 1); 14 gives three; 17 gives four; 20 gives four. Total **18**.

### Example 4: is it a palindrome?

*Trigger: a property of a whole string that fails on the first mismatch. Tool: the all-flag from section 8, comparing position `i` with its mirror `length() - 1 - i`.*

```java
boolean same = true;
for (int i = 0; i < s.length() / 2; i++) {
    String left = s.substring(i, i + 1);
    String right = s.substring(s.length() - 1 - i, s.length() - i);
    if (!left.equals(right)) {
        same = false;
    }
}
```
The mirror of index `i` is `length() - 1 - i`, and as a substring that is the cut pair `(length() - 1 - i, length() - i)`. The loop stops half-way because int division sends a middle character to neither side. For `"level"` it makes two comparisons and `same` stays `true`.

## Predict, then check

1. `int x = 5; if (x > 3) x++; x++;` What is `x`?
2. How many times does the body of `for (int i = 3; i < 12; i += 2)` run?
3. `int n = 0; if (n != 0 && 10 / n > 1) { ... }` Exception, or not?
4. For `mark = 70`, which of `A`, `B`, `C` is printed by `if (mark > 50) print("C"); else if (mark > 60) print("B"); else if (mark > 65) print("A");`?
5. `!(a || b)` when `a` is `false` and `b` is `true`.
6. `int k = 10; while (k > 0) { k -= 4; }` What is `k` afterwards?
7. How many stars: `for (int i = 0; i < 5; i++) { for (int j = i; j < 5; j++) { print("*"); } }`?
8. `String s = "abc"; String t = ""; for (int i = 0; i < s.length(); i++) { t = s.substring(i, i + 1) + t; }` What is `t`?

> [!success]- Answers
> 1. `7`. Only the first `x++` belongs to the `if`. Both run here, but the second runs whatever `x` is.
> 2. `5`: i is 3, 5, 7, 9, 11.
> 3. No exception. `n != 0` is false, so `&&` never evaluates the division.
> 4. `C`. The first true condition wins, and the others are never tried.
> 5. `false`. It equals `!a && !b`, which is `true && false`.
> 6. `-2`: 10, 6, 2, -2. The test happens before each pass, so the loop cannot stop exactly at 0.
> 7. `15`: 5 + 4 + 3 + 2 + 1.
> 8. `"cba"`. Each character is put on the front.

## Common Misconceptions (Teaching Notes)

1. **"Indented lines are inside the `if`."** Only in Python. In Java the braces decide, and without braces the body is one statement.
2. **"The `else` goes with the `if` it lines up with."** It goes with the nearest unmatched `if`.
3. **"Three `if`s in a row are an if-else-if."** Separate `if`s are all tested. In a chain, at most one body runs.
4. **"The `for` update runs before the test", or "the test runs after the body".** Initialise, test, body, update, test. The test runs one more time than the body.
5. **"Two nested loops always run $n^2$ times."** Only when the inner limit does not depend on the outer variable.
6. **"`!(a && b)` is `!a && !b`."** The operator flips as well.
7. **"`&&` always evaluates both sides."** It stops at the first `false`, and good code relies on that.

## Exam Notes

### AP Computer Science A (course effective Fall 2025)

This covers topics **2.1, 2.3 to 2.5 and 2.7 to 2.12** of Unit 2, and the equivalence half of **2.6** (truth tables and De Morgan's laws), whose other half is in [[Java Objects, References and Strings]]. Unit 2 carries 25–35 % of the exam, the largest share of any unit but one.

- **Often set as multiple choice:** the value of a variable after a loop; how many times a statement executes; which expression is equivalent to a given one; what a nested `if` prints for given values; which code segment has an off-by-one error.
- **In the written questions:** free-response Question 1 is named *Methods and Control Structures*, and its first part requires "iterative or conditional statements, or both". Every other written question uses loops as well.
- **Inside the course:** `if`, `if-else`, `if-else-if`, nesting; `!`, `&&`, `||`, their precedence and short-circuit evaluation; equivalence by truth table and De Morgan's laws; `while` and `for`, the order of the `for` header, rewriting one as the other, infinite loops and off-by-one errors; the standard algorithms for divisibility, digits, frequency, minimum and maximum, sum and average; the string algorithms for a property, a count of substrings, and reversal; nested iteration; statement execution counts.
- **Not in the course description at all:** `switch`, `do-while`, `break`, `continue` and the conditional operator `? :`. None is needed, and none appears above. The enhanced `for` loop arrives with arrays.

### Cambridge 9618 (Paper 4) and IB Computer Science

Both accept Java. Everything above applies, and the `CASE` and post-condition loop of 9618 pseudocode can be written with `else if` and `while`. The sentinel loop in section 6 is the everyday Paper 4 input pattern.

### Where this is *not* examined

Cambridge 0478 is answered in pseudocode or Python and needs none of the Java here.

## Connections

- **The concepts, taught in Python:** [[Programming Fundamentals]] (selection, iteration, totalling, counting, the standard methods).
- **The logic:** [[Boolean Algebra]] (De Morgan's laws proved), [[Logic Gates]] (the same three operators in hardware).
- **Counting steps, made formal:** [[Big-O Notation]]. **Searching and sorting built from these loops:** [[Searching]], [[Sorting]].
- **Previous companion:** [[Java Objects, References and Strings]]. **Next:** [[Java Classes]].

## Notation Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $!(a \;\&\&\; b) \equiv\; !a \;\lvert\lvert\; !b$ | `!(a \;\&\&\; b) \equiv\; !a \;\lvert\lvert\; !b` | De Morgan: not both is at least one not |
| $hi - lo + 1$ | `hi - lo + 1` | How many integers from $lo$ to $hi$ inclusive |
| $\dfrac{n(n+1)}{2}$ | `\dfrac{n(n+1)}{2}` | $1 + 2 + \dots + n$, the triangular count |
| $\log_2 n$ | `\log_2 n` | Roughly how many times $n$ can be halved |

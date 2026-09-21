---
chinese: Java 的值与表达式 (Java de zhí yǔ biǎodáshì)
prerequisites:
  - "[[Programming Fundamentals]]"
  - "[[Compilers and Interpreters]]"
leads_to:
  - "[[Java Objects, References and Strings]]"
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
  - misconception/division-always-gives-a-decimal
  - misconception/cast-rounds
  - misconception/overflow-raises-an-error
  - misconception/cast-applies-to-the-whole-expression
  - misconception/compiles-means-correct
---

# Java Values and Expressions Java 的值与表达式

> In Python, `7 / 2` is `3.5`. In Java, `7 / 2` is `3`.
>
> Nothing is broken. Java decided what kind of thing each `7` and `2` was before the program started, and that decision chose the division.

## What this is for

You can already program. [[Programming Fundamentals]] teaches variables, expressions, selection, loops and functions, with runnable Python throughout, and nothing here repeats it. This is the first of a small family of **Java companions**: each one takes ideas you own and shows **what Java does differently**, because some exams are written in Java and Java punishes Python habits without warning.

Every program below is a real file in the folder `java-values-and-expressions`, and every output shown was produced by compiling and running that file. Run `python3 run_all.py` in that folder to reproduce all of it, then change one line and predict what happens before you run it again.

**The one idea to carry through:** in Python a *value* has a type and a name is a label you can move to any value. In Java a *variable* has a type, fixed when you declare it, and **the types of the operands decide what an operator does**. Almost every surprise below is that sentence in a different costume.

## 中文锚点

去银行汇款，柜员先看你填的单子：金额那一栏只能填数字，你写了“七百”两个汉字，单子当场退回，钱一分也没动。Python 像一个什么单子都先收下的柜员，办到一半发现不对才停下来；Java 像那个先审单子的柜员：每个变量在声明的时候就写明了它是哪一类，整数、小数，还是真假（布尔值），程序还没开始运行，编译器就把每一步的类型都核对过了。类型一旦定下来，运算就跟着类型走：两个整数相除，结果还是整数，所以 7 除以 2 得 3，小数部分直接丢掉；只有其中至少一个是小数，结果才是 3.5。学 Java 头几个星期碰到的“怪事”，几乎都是这一件事：先看清楚每个数是哪一类，再看运算。

## 1. Two stages: compile, then run

Python reads your file and runs it line by line. Java does the job in two separate stages, and [[Compilers and Interpreters]] explains the machinery behind them.

```bash
javac Output.java     # stage 1: the compiler checks the whole file and writes Output.class
java Output           # stage 2: the Java Virtual Machine runs Output.class
```

You can write the file in any text editor. Most programmers use an **IDE** (integrated development environment), which puts the editor, the compile step and the run step behind one button; the two stages still happen.

That split gives three kinds of error, and an exam expects you to tell them apart.

**A syntax error** breaks the rules of the language. The compiler refuses, and nothing runs. `SyntaxError.java` leaves out one semicolon:

```
SyntaxError.java:4: error: ';' expected
        System.out.println("almost")
                                    ^
1 error
```

**A type error is also caught by the compiler.** Each of these two lines would run in Python. Neither gets past `javac` (`WontCompile.java`):

```java
int half = 7 / 2.0;     // a double will not go into an int without a cast
int score = 40;
score = "forty";        // a variable keeps the type it was declared with
```

```
WontCompile.java:5: error: incompatible types: possible lossy conversion from double to int
WontCompile.java:8: error: incompatible types: String cannot be converted to int
2 errors
```

So does using a variable before giving it a value (`Uninitialised.java`): `error: variable total might not have been initialized`. The compiler works in passes, so fixing one batch of errors can reveal another. Fix, recompile, repeat.

**A run-time error** gets past the compiler and stops the program while it is running. An **exception** is the usual kind. `DivideByZero.java` compiles without complaint:

```java
int sweets = 12;
int children = 0;
System.out.println("sharing...");
System.out.println(sweets / children);
System.out.println("this line never runs");
```

```
sharing...
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at DivideByZero.main(DivideByZero.java:7)
```

The first line printed. The program then stopped at line 7, and the message names the exception and the line.

**A logic error** compiles, runs, and gives the wrong answer. No tool reports it. Only testing against a value you worked out yourself finds it. `LogicError.java` means to average 70, 85 and 90:

```java
double mean = a + b + c / 3;        // prints 185.0
```

Division happens before addition, so this is $70 + 85 + 30$. The correct line, `(a + b + c) / 3.0`, prints `81.66666666666667`.

## 2. The frame every program sits in

```java
public class Output {
    public static void main(String[] args) {
        System.out.println("three");
    }
}
```

Treat the two outer lines as a fixed frame for now; [[Java Objects, References and Strings]] explains each word. Three rules matter today. The file must be named after the class (`Output.java`). Blocks are marked by **braces**, not indentation: indent for the reader, because the compiler ignores it. Every statement ends with a **semicolon**.

## 3. Output

`Output.java`:

```java
System.out.print("one ");
System.out.print("two ");          // print stays on the same line
System.out.println("three");       // println moves to a new line AFTER printing
System.out.println("She said \"hi\".");
System.out.println("C:\\Users\\david");
System.out.println("line 1\nline 2");
System.out.println("total: " + 3 + 4);
System.out.println("total: " + (3 + 4));
System.out.println(3 + 4 + " is the total");
```

```
one two three
She said "hi".
C:\Users\david
line 1
line 2
total: 34
total: 7
7 is the total
```

A **literal** is a fixed value written directly in the code, such as `42`, `9.5` or `true`. A **string literal** is a run of characters in double quotes. Three **escape sequences** are in the AP course: `\"` for a double quote, `\\` for a backslash, `\n` for a new line.

The last three lines are the first appearance of the one idea. `+` between two numbers adds. `+` with a String on either side joins. Java works **left to right**: `"total: " + 3` is already a String, so the `4` is joined on too, giving `total: 34`. In the final line `3 + 4` is met first, while both are still numbers.

## 4. Variables and types

`Variables.java`:

```java
int score = 42;                 // a whole number
double price = 9.5;             // a real number
boolean passed = score >= 40;   // true or false, written in lower case
double d = 7;                   // an int is widened to a double automatically
System.out.println(d);          // 7.0
```

The AP course uses exactly three **primitive** types: `int`, `double` and `boolean`. Java has five more (`long`, `short`, `byte`, `float`, `char`), which the AP course leaves out. Everything else, including `String`, is a **reference** type, the subject of [[Java Objects, References and Strings]].

An `int` slides into a `double` by itself, because nothing is lost: this is **widening**. A `double` will not go into an `int` unless you ask for it with a cast, because something would be lost. That asymmetry explains the compiler error in §1.

## 5. Arithmetic: the operands choose the operation

**An operation on two `int` values gives an `int`. If at least one operand is a `double`, the result is a `double`.**

`IntDivision.java`:

| Expression | Prints | Why |
|---|---|---|
| `7 / 2` | `3` | int with int: the whole-number part, nothing rounded |
| `7 / 2.0` | `3.5` | one double is enough |
| `7 % 2` | `1` | the remainder |
| `2 / 7` | `0` | seven goes into two zero times |
| `2 % 7` | `2` | and all of the two is left over |
| `3 + 4 * 2` | `11` | `*`, `/` and `%` come before `+` and `-` |
| `1 / 2 * 6.0` | `0.0` | left to right: `1 / 2` is `0` first |
| `6.0 * 1 / 2` | `3.0` | left to right: `6.0 * 1` is `6.0` first |

The last two rows are the same three numbers. Operators of equal rank are taken left to right, and the type is decided **at each step**, not for the whole line.

Division and remainder are partners: `135 / 60` is `2` and `135 % 60` is `15`, so 135 minutes is `2 h 15 min`. Pulling a number apart into hours and minutes, pounds and pence, or digit by digit, is always this pair.

> [!info] Two differences from Python you will not be examined on, and should still know
> For negative numbers the languages disagree: `-7 / 2` is `-3` in Java (it chops towards zero) and `-7 // 2` is `-4` in Python (it rounds down); `-7 % 3` is `-1` in Java and `2` in Python. The AP course uses `%` only with a non-negative left side and a positive right side, so this cannot be set. Dividing a `double` by zero gives `Infinity` and no exception; that too is outside the course.

## 6. Casting and rounding

A **cast**, `(int)` or `(double)`, converts one value. `Casting.java`:

| Expression | Prints | Why |
|---|---|---|
| `(int) 3.9` | `3` | a cast to int **truncates**: it chops, it does not round |
| `(int) -3.9` | `-3` | towards zero |
| `(double) total / n` | `4.25` | the cast binds to `total` alone, so this is `17.0 / 4` |
| `(double) (total / n)` | `4.0` | too late: `17 / 4` was already `4` |
| `(int) (2.5 + 0.5)` | `3` | rounding a non-negative number |
| `(int) (-2.6 - 0.5)` | `-3` | rounding a negative number |
| `(int) (-2.6 + 0.5)` | `-2` | the wrong idiom for a negative number |

**A cast binds more tightly than any arithmetic operator.** `(double) total / n` does not mean "do the division as doubles". It means "turn `total` into a double, then divide", which happens to have the same effect. Put brackets round the division and the cast arrives after the damage is done.

**Why $x + 0.5$ rounds.** Truncation sends every number in $[n, n+1)$ to $n$. Adding $0.5$ first slides the window: every $x$ in $[n - 0.5,\ n + 0.5)$ lands in $[n, n+1)$ and is chopped to $n$, which is its nearest integer. For negative numbers truncation goes *up* towards zero, so the shift has to go the other way: `(int) (x - 0.5)`.

**Where truncation and round-off meet:**

```java
double price = 19.99;
System.out.println(price * 100);              // 1998.9999999999998
System.out.println((int) (price * 100));      // 1998
System.out.println((int) (price * 100 + 0.5)); // 1999
```

One penny has gone missing, and no error was reported. This is why money is stored as a whole number of cents.

## 7. The edges: overflow and round-off

`Overflow.java`:

```java
System.out.println(Integer.MAX_VALUE);          //  2147483647
System.out.println(Integer.MIN_VALUE);          // -2147483648
System.out.println(Integer.MAX_VALUE + 1);      // -2147483648
int big = 50000;
System.out.println(big * big);                  // -1794967296
System.out.println((double) big * big);         //  2.5E9
System.out.println(0.1 + 0.2);                  //  0.30000000000000004
System.out.println(0.1 + 0.2 == 0.3);           //  false
```

A Python integer grows as large as it needs to. A Java `int` is 4 bytes, so it holds values from `Integer.MIN_VALUE` to `Integer.MAX_VALUE` and no others. A result outside that range **overflows**: it wraps round to the other end. There is no exception and no warning. [[Two's Complement]] shows why the number after the largest positive value is the most negative one, and [[Overflow and Underflow]] treats the general case.

A `double` has limited precision, so most decimal fractions are stored slightly wrong: this is **round-off error**, and [[Floating-Point Representation]] shows where the stray digits come from. Adding `0.1` ten times gives `0.9999999999999999`, and comparing that with `1.0` gives `false`. Two habits follow. Never test doubles with `==`. When exactness matters, count in whole units with an `int`.

## 8. Compound assignment

`CompoundAssign.java`, starting from `int x = 7`:

| Statement | `x` afterwards | Same as |
|---|---|---|
| `x += 3;` | 10 | `x = x + 3;` |
| `x -= 4;` | 6 | |
| `x *= 5;` | 30 | |
| `x /= 4;` | 7 | int division: $30 / 4$ |
| `x %= 4;` | 3 | |
| `x++;` | 4 | `x = x + 1;` |
| `x--;` | 3 | `x = x - 1;` |

Python has `+=` and has no `++`. In the AP course `x++` and `x--` appear only as statements by themselves, as here. The forms `++x`, and `x++` used inside a larger expression, are outside the course, and so is chaining assignments as in `a = b = 4`.

## 9. The Math class

`Math` lives in the package `java.lang`, and everything in `java.lang` is available without an import. Its methods are **class methods**: you call them on the class name, `Math.sqrt(2)`, not on an object. These five are on the AP Java Quick Reference, which is given to you in the exam.

| Method | Example | Prints |
|---|---|---|
| `static int abs(int x)` | `Math.abs(-7)` | `7` |
| `static double abs(double x)` | `Math.abs(-7.5)` | `7.5` |
| `static double pow(double base, double exponent)` | `Math.pow(2, 10)` | `1024.0` |
| `static double sqrt(double x)` | `Math.sqrt(16)` | `4.0` |
| `static double random()` | `Math.random()` | a double $r$ with $0.0 \le r < 1.0$ |

**Read the first word after `static`: it is the type that comes back.** `pow` and `sqrt` return a `double` even when the answer is whole, so `int p = Math.pow(2, 10);` is a compile error and `int p = (int) Math.pow(2, 10);` is right.

**A random integer in a range, derived and not memorised.** Start from $0 \le r < 1$. Multiply by $6$: $0 \le 6r < 6$. Truncate: one of $0, 1, 2, 3, 4, 5$, each equally likely. Add $1$: one of $1$ to $6$.

```java
int die = (int) (Math.random() * 6) + 1;
```

In general, the integers from `lo` to `hi` inclusive number $n = hi - lo + 1$, and the expression is `(int) (Math.random() * n) + lo`. `MathDemo.java` rolls this 100 000 times and reports `die: 1 to 6`.

Now leave out one pair of brackets:

```java
int die = (int) Math.random() * 6 + 1;      // reports  bug: 1 to 1
```

The cast binds to `Math.random()` alone, turns it into `0` every time, and the die always shows 1. It is the rule from §6 again.

## 10. Libraries, and how to read an API entry

A **library** is a collection of classes someone else wrote. Its **API** (application programming interface) is the documentation that tells you how to use them, and classes are grouped into **packages**, such as `java.lang`. A class has **attributes**, the data it holds, and **behaviours**, what it can do, which are its methods.

One line of an API tells you everything you need in order to call a method:

```
static double pow(double base, double exponent)
```

`static`: call it on the class, as `Math.pow(...)`. `double`: what comes back. `pow`: its name. In the brackets: what it needs, in order, with types. You will be handed lines like this for classes you have never seen, and asked to use them.

## 11. Comments, preconditions and postconditions

Java has three forms of comment: `//` to the end of the line, `/* ... */` over a block, and `/** ... */`, a **Javadoc** comment, from which API documentation is generated. The compiler ignores all three.

`Documented.java`:

```java
/**
 * Returns the number of whole boxes needed to pack all the items.
 * Precondition:  items >= 0 and perBox > 0.
 * Postcondition: the value returned times perBox is at least items.
 */
public static int boxesNeeded(int items, int perBox) {
    return (items + perBox - 1) / perBox;   // int division, rounded UP
}
```

A **precondition** must be true just before the method is called, for it to behave as promised. **The method is not expected to check it.** A **postcondition** is what is guaranteed afterwards. `boxesNeeded(10, 4)` prints `3`. `boxesNeeded(10, 0)` breaks the precondition, and the program dies with `ArithmeticException: / by zero`. That is the caller's fault, and the contract says so.

The body is worth a second look: `(items + perBox - 1) / perBox` is int division made to round **up**, the same sliding-window idea as §6.

## Python to Java, at a glance

| You want | Python | Java |
|---|---|---|
| true division | `7 / 2` → `3.5` | `7 / 2.0` or `(double) 7 / 2` |
| whole-number division | `7 // 2` | `7 / 2` |
| power | `2 ** 10` → `1024` | `Math.pow(2, 10)` → `1024.0` |
| round to nearest | `round(x)` | `(int) (x + 0.5)` for $x \ge 0$ |
| square root | `math.sqrt(x)` after an import | `Math.sqrt(x)`, no import |
| random integer 1 to 6 | `random.randint(1, 6)` | `(int) (Math.random() * 6) + 1` |
| print and stay on the line | `print(x, end="")` | `System.out.print(x);` |
| truth values | `True`, `False` | `true`, `false` |
| a new variable | `score = 42` | `int score = 42;` |
| largest integer | none | `Integer.MAX_VALUE` |
| add one | `x += 1` | `x++;` |
| a block | a colon and indentation | braces `{ }` |

## Worked examples

### Example 1: trace the types

> What is printed?
> ```java
> int a = 5, b = 2;
> double r = a / b * 2.0;
> System.out.println(r);
> ```

**Tool: decide the type at each step, left to right.** Trigger: a `/` between two names. Before anything else, look up what type each name was declared as.

`a / b` is int with int: `2`. Then `2 * 2.0` has a double: `4.0`. The variable being a `double` came too late to help. **Prints `4.0`.**

### Example 2: fix the average three ways

> `int total = 17, n = 4;` and `double mean = total / n;` prints `4.0`. Give three corrections.

**Tool: make one operand a double before the division happens.** Trigger: a whole number came out where a fraction was expected.

`(double) total / n`, or `total / (double) n`, or `total * 1.0 / n`. All print `4.25`. The non-fix is `(double) (total / n)`: the brackets make the int division happen first.

### Example 3: a random integer from 10 to 25 inclusive

**Tool: count the values, then shift.** Trigger: "inclusive" at both ends, so the count is $25 - 10 + 1 = 16$, not $15$.

`(int) (Math.random() * 16) + 10`. Check the ends: the smallest is $\lfloor 0 \rfloor + 10 = 10$, and since $16r < 16$ the largest is $15 + 10 = 25$.

### Example 4: which of these overflows?

> (a) `Integer.MAX_VALUE - 1`  (b) `Integer.MAX_VALUE + 1`  (c) `40000 * 60000`  (d) `40000 * 60000.0`

**Tool: work out the true value and compare it with about 2.1 billion.** Trigger: large int literals, or `MAX_VALUE` inside arithmetic.

(a) fits. (b) overflows to `Integer.MIN_VALUE`. (c) is $2.4 \times 10^9$ with both operands `int`, so it overflows. (d) has a `double` operand, so the multiplication is done as doubles and gives `2.4E9`.

### Example 5: compile-time, run-time or logic?

| Code | Kind | Why |
|---|---|---|
| `int x = 3.0;` | compile-time | a double will not go into an int without a cast |
| `int y = 10 / (5 - 5);` | run-time | it compiles; the division is attempted only when the program runs, and throws `ArithmeticException` |
| `double area = 1 / 2 * base * height;` | logic | `1 / 2` is `0`, so the area is always `0.0` |
| `System.out.println("hi")` | compile-time | the missing semicolon is a syntax error |
| `int z = Integer.MAX_VALUE + 1;` | logic | it compiles and runs, and silently wraps |

## Predict, then check

Write your answer down before you open it. Every answer below came from running the code.

> [!question] 1. `System.out.println(9 / 2 + 9 % 2);`
> > [!success]- Answer
> > `5`. `9 / 2` is `4`, `9 % 2` is `1`.

> [!question] 2. `System.out.println("sum: " + 1 + 2 * 3);`
> > [!success]- Answer
> > `sum: 16`. `2 * 3` happens first and gives `6`. Then left to right: `"sum: " + 1` is `"sum: 1"`, and joining `6` gives `sum: 16`.

> [!question] 3. `double d = (int) 7.9 / 2; System.out.println(d);`
> > [!success]- Answer
> > `3.0`. The cast gives `7`, `7 / 2` is `3`, and only then is `3` widened to `3.0`.

> [!question] 4. `int x = 10; x /= 4; x *= 4; System.out.println(x);`
> > [!success]- Answer
> > `8`. `10 / 4` is `2`. Integer division loses information and multiplying does not bring it back.

> [!question] 5. `System.out.println((int) (Math.random() * 3));` — which values are possible?
> > [!success]- Answer
> > `0`, `1` or `2`. Never `3`, because `Math.random()` is always less than `1.0`.

> [!question] 6. `System.out.println(Math.sqrt(25) + Math.abs(-2));`
> > [!success]- Answer
> > `7.0`. `sqrt` returns the double `5.0`, and `5.0 + 2` is a double.

> [!question] 7. `System.out.println(1 / 3 + 1 / 3 + 1 / 3);`
> > [!success]- Answer
> > `0`. Each `1 / 3` is `0`.

> [!question] 8. `int n = 4; double half = n / 2; System.out.println(half);`
> > [!success]- Answer
> > `2.0`. The division is right this time, which is what makes the habit dangerous: it fails only for odd `n`.

## Common Misconceptions (Teaching Notes)

1. **"Division gives a decimal."** Only if an operand is a `double`. The type of the variable you store the result in has no say. **Fix:** find the declaration of every name in the expression before you compute anything.
2. **"A cast rounds."** It truncates towards zero. **Fix:** `(int) (x + 0.5)` for non-negative values, and know why the $0.5$ works.
3. **"`(double) a / b` converts the division."** It converts `a`. The habit breaks the moment a bracket appears, as in `(double) (a / b)` and `(int) Math.random() * 6`. **Fix:** a cast applies to the single value immediately to its right.
4. **"Overflow causes an error."** It causes a wrong answer, with no message. **Fix:** estimate the true size of the result and compare it with two billion.
5. **"It compiled, so it is right."** The compiler checks grammar and types. It cannot know you meant `3.0`. **Fix:** test against a value worked out by hand.
6. **"`Math.pow(2, 3)` is `8`."** It is `8.0`. Storing it in an `int` needs a cast.

## Exam Notes

### AP Computer Science A (course effective Fall 2025)

This covers topics **1.1 to 1.8 and 1.11** of Unit 1. The exam is answered in Java, and the Java Quick Reference, which lists the five `Math` methods and `Integer.MIN_VALUE` / `MAX_VALUE`, is provided.

- **Often set as multiple choice:** the value or output of an expression that mixes `int` and `double`; where a cast binds; which expression gives a random integer in a stated range; whether a snippet overflows; whether an error is compile-time, run-time or logic.
- **Inside the course:** `int`, `double`, `boolean`; `+ - * / %` and precedence; `ArithmeticException` for int division by zero; `(int)` and `(double)`; both rounding idioms; overflow and round-off; `+= -= *= /= %=`; `x++` and `x--` as statements; `print`, `println`, `\"`, `\\`, `\n`; the three comment forms; preconditions and postconditions.
- **Outside the course**, in its own words: the other five primitive types; `%` with a negative left side or a non-positive right side; special double values such as infinity; division by zero where a value is a `double`; assignment inside an expression; prefix `++x` and increments inside other expressions; any form of input from the user. Text files are read later in the course, with `Scanner`.

### Cambridge 9618 (Paper 4) and IB Computer Science

Both accept Java. 9618 Paper 4 may be answered in Java, Python or VB.NET, and the IB papers are issued in Java and in Python. A student who chooses Java for either needs everything above, with two differences: these boards examine keyboard and file input early, and neither restricts the primitive types.

### Where this is *not* examined

Cambridge 0478 is answered in pseudocode or Python, and nothing here is needed for it.

## Connections

- **The concepts, taught in Python:** [[Programming Fundamentals]] (variables, operators, DIV and MOD, library routines, maintainability).
- **The machinery:** [[Compilers and Interpreters]] (why Java has a compile stage and a virtual machine), [[Two's Complement]] and [[Overflow and Underflow]] (why `MAX_VALUE + 1` is `MIN_VALUE`), [[Floating-Point Representation]] (why `0.1 + 0.2` is not `0.3`).
- **Next companion:** [[Java Objects, References and Strings]].
- **The translation of exam pseudocode**, for comparison: [[Cambridge Pseudocode]].

## Notation Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $0.0 \le r < 1.0$ | `0.0 \le r < 1.0` | The range of `Math.random()` |
| $n = hi - lo + 1$ | `n = hi - lo + 1` | How many integers lie between two inclusive ends |
| $\lfloor x \rfloor$ | `\lfloor x \rfloor` | Round down; what `(int)` does to a non-negative double |

---
chinese: Java 的对象、引用与字符串 (Java de duìxiàng, yǐnyòng yǔ zìfúchuàn)
prerequisites:
  - "[[Java Values and Expressions]]"
  - "[[Object-Oriented Programming]]"
leads_to:
  - "[[Java Control Flow]]"
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
  - misconception/double-equals-compares-string-content
  - misconception/string-methods-change-the-string
  - misconception/assignment-copies-the-object
  - misconception/a-method-can-repoint-the-callers-variable
  - misconception/null-is-an-empty-object
---

# Java Objects, References and Strings Java 的对象、引用与字符串

> A program asks *"Delete everything?"*. The user types `yes`. The program checks `answer == "yes"`, gets `false`, and deletes nothing.
>
> The letters were the same. The question `==` asked was a different one: *are these the same object?*

## What this is for

[[Java Values and Expressions]] dealt with `int`, `double` and `boolean`, where a variable holds its value and that is the end of the story. Everything else in Java is an **object**, and a variable for an object works differently. [[Object-Oriented Programming]] teaches what classes and objects are, in Python; nothing here repeats it. What follows is how Java *uses* objects that somebody else has written, including the one you will use most, `String`.

Every program below is a real file in the folder `java-objects-references-and-strings`, and every output shown came from compiling and running it. Run `python3 run_all.py` in that folder to reproduce all of it.

**The one idea to carry through:** a variable of a class type does not hold an object. It holds a **reference**: an arrow that points at an object living somewhere else. (Think of it as the object's address in memory.) Assignment copies the arrow. Passing to a method copies the arrow. `==` compares arrows. `null` is an arrow that points at nothing. Hold on to that sentence and none of the surprises below is a surprise.

If you know Python well, you have met this already: every Python name is an arrow, which is why two names for one list see each other's changes ([[Arrays]] calls it aliasing). Java's twist is that it has **both kinds of variable**, and you must know which kind you are holding.

## 中文锚点

你把一个在线共享文档的链接发给朋友，他在里面改了一个错别字；你再打开，错别字也没了，因为你们手里拿的是同一份文档的链接。要是你发的是一张截图，他在自己那张上怎么涂改，你这张都不会变。Java 的变量就分这两种。存数字的变量里放的是数字本身，复制它就像发截图；存对象的变量里放的只是一个指向对象的链接，复制它得到的是通向同一个东西的两个链接，不管你从哪个链接进去改，从另一个链接都能看到改动。这也是为什么问两个这样的变量“相不相等”会有两种意思：两个链接是不是通向同一份文档，还是两份不同的文档碰巧写着一样的内容。至于一个哪儿也不通的链接，留着没事，可一旦你点开它，程序就当场停下。

## 1. Methods: the signature, and what comes back

A **method** is a named block of code that runs only when it is called; Python calls it a function. (A **block** is any stretch of code enclosed in braces.) You can use one knowing *what* it does and nothing about *how*. That is **procedural abstraction**, and it is the reason documentation exists. The first line of a method is its **header**:

```java
public static int area(int width, int height) {
    return width * height;
}
```

| Part | Here | What it tells you |
|---|---|---|
| return type | `int` | what kind of value comes back; `void` means nothing comes back |
| name | `area` | |
| parameter list | `(int width, int height)` | what you must hand over, in order |
| **signature** | `area(int, int)` | the name plus the ordered list of parameter **types**; the return type is not part of it. With no parameters the list is empty: `getCount()` |

The signature is how Java tells methods apart, so two methods may share a name if their signatures differ. They are **overloaded**, and the types of your arguments pick which one runs. Python has nothing like this. From `Methods.java`:

```java
System.out.println("before the call");
greet("Ada");                                  // control jumps into greet, then comes back here
System.out.println("after the call");

int a = area(4);                               // the return value is stored
System.out.println(a + " " + area(4, 5));      // or used inside an expression
System.out.println(area(4.0));                 // the argument's type picks the overload
System.out.println(half(9));                   // the int 9 arrives as the double 9.0
```

```
before the call
  (inside greet) hello, Ada
after the call
16 20
50.26548245743669
4.5
```

Three things to read off that output.

- **A call interrupts the sequence.** Java runs the method's statements, and when it reaches a `return` or the closing brace, control comes back to the point just after the call.
- **A non-void method is a value.** Store it or use it in an expression. Writing `area(7);` alone is legal and pointless: the 49 is thrown away. **A void method is not a value**, so it can only stand as a statement.
- **An `int` may go where a `double` is expected**, because widening loses nothing. The reverse is refused.

What the compiler says when a call does not match (`BadCalls.java`, with `area(int, int)` and a void `greet`):

```
int r = greet("Ada");    error: incompatible types: void cannot be converted to int
int a = area(4);         error: method area in class BadCalls cannot be applied to given types;
                           required: int,int     found: int
int b = area(4, "5");    error: incompatible types: String cannot be converted to int
int c = area(2.5, 4);    error: incompatible types: possible lossy conversion from double to int
```

And because the return type is not part of the signature, two methods that differ *only* in return type are the same method twice (`SameSignature.java`): `error: method area(int) is already defined in class SameSignature`.

## 2. Arguments are copied

The values you write in a call are **arguments**; the variables in the header are **parameters**. Java has exactly one rule for connecting them, **call by value**: each parameter starts life as a *copy* of its argument.

```java
public static void addTen(int n) {
    n = n + 10;
    System.out.println("  (inside addTen) n is " + n);
}
...
int x = 5;
addTen(x);
System.out.println("x is still " + x);
```

```
  (inside addTen) n is 15
x is still 5
```

`n` was a second box with a copy of 5 in it. Changing `n` changed the copy. Section 7 asks what happens when the thing copied is an arrow.

## 3. Two ways to call: on the class, or on an object

| | Class method | Instance method |
|---|---|---|
| Header contains | `static` | no `static` |
| Belongs to | the class as a whole | each object |
| Called as | `ClassName.method(...)` | `objectName.method(...)` |
| Example | `Math.sqrt(2.0)`, `Integer.parseInt("42")` | `gate.click()`, `s.length()` |

`Math` holds nothing but class methods, which is why you never wrote `new Math()`. Inside the class that defines a static method, the class name may be left off: within `Methods`, `area(3)` and `Methods.area(3)` are the same call, and the last line of `Methods.java` prints `9 3 42` for `Methods.area(3)`, `Math.abs(-3)` and `Integer.parseInt("42")`.

An instance method needs an object to work on, because it reads or changes *that object's* data. The dot says whose.

## 4. A class you use without writing: `Counter`

A **class** is the blueprint: it lists the **attributes** (the data each object carries, stored in variables) and the **behaviours** (what an object can do, defined by methods). An **object** is one instance built from the blueprint, with its own copy of the attributes. A class also defines a **type**, so `Counter` can stand wherever `int` could in a declaration.

`Counter.java` models the hand clicker a steward uses to count people through a gate. You are not asked to write it yet. Read it as you would read a library's documentation, which is all you ever get for most classes:

| | Signature | What it does |
|---|---|---|
| constructor | `Counter()` | makes a counter that starts at 0 |
| constructor | `Counter(int start)` | makes a counter that starts at `start`; precondition `start >= 0` |
| method | `void click()` | adds 1 |
| method | `void add(int n)` | adds `n`; precondition `n >= 0` |
| method | `int getCount()` | returns the count and changes nothing |
| method | `String toString()` | returns a description such as `"Counter[3]"` |

Libraries are collections of such classes, grouped into **packages**, and the published list of signatures and descriptions is the library's **API**. `String` and `Math` live in the package `java.lang`, which is always available. Anything else must be imported, as `Scanner` is in section 11.

Classes can also be arranged in a hierarchy, where a **subclass** inherits the attributes and behaviours of its **superclass**; [[Object-Oriented Programming]] builds one. One fact from that hierarchy matters here: **every class in Java is a subclass of `Object`**, so every object, whatever its class, has a `toString()` and an `equals()`.

## 5. `new`: making an object

```java
Counter gate = new Counter();          // the constructor with the signature Counter()
Counter stand = new Counter(250);      // the constructor with the signature Counter(int)

gate.click();
gate.click();
stand.add(30);

System.out.println(gate.getCount());   // each object has its own count
System.out.println(stand.getCount());
System.out.println("gate is " + gate); // + calls gate.toString() for you
System.out.println(stand);             // so does println
```

```
2
280
gate is Counter[2]
Counter[280]
```

A **constructor** has the same name as its class. `new Counter(250)` does three things in order: it makes room for a new object, runs the constructor whose signature matches the arguments (constructors can be overloaded exactly as methods can, and arguments are copied into parameters by the same call-by-value rule), and hands back a **reference** to the finished object. That reference is what gets stored in `stand`.

Joining any object to a `String` with `+` quietly calls the object's `toString()`. `Counter` **overrides** the inherited method with a helpful one of its own: same signature, behaviour specific to the subclass. A class that does not bother inherits the one from `Object`, which prints the class name, an `@`, and a number of no use to you: the last line of `Create.java` prints `java.lang.Object@` followed by such a number. If you ever see output like `Counter@1b6d3586`, you printed an object whose class has no `toString` of its own.

## 6. The variable holds an arrow

`Alias.java` does the same thing twice, once with `int` and once with `Counter`:

```java
int p = 5;
int q = p;                 // q gets a copy of the VALUE 5
q++;
System.out.println(p + " " + q);

Counter a = new Counter();
Counter b = a;             // b gets a copy of the REFERENCE: one object, two names
b.click();
b.click();
System.out.println(a.getCount() + " " + b.getCount());
System.out.println(a == b);
```

```
5 6
2 2
true
```

`new` ran once, so there is **one** `Counter`. `b = a` copied the arrow, not the clicker. Clicking through `b` and reading through `a` reach the same object. Two references to one object are called **aliases**.

![[java-references-copy-and-alias.svg|820]]

**To find out how many objects a piece of code has, count the `new`s**, not the variables. The rest of `Alias.java`:

```java
Counter c = new Counter(2);            // a different object with the same count
System.out.println(a == c);
System.out.println(a.getCount() == c.getCount());

b = new Counter(99);       // b now points somewhere else; a is untouched
System.out.println(a + " " + b);
```

```
false
true
Counter[2] Counter[99]
```

For references, `==` asks *"same object?"*, so `a == c` is `false` although both counters read 2. Comparing the counts themselves compares two `int`s, and that is `true`. The last line re-points `b`. Assigning to a reference variable never changes any object; it changes where one arrow points.

## 7. Passing a reference to a method

Call by value has no exceptions. When the argument is a reference, the parameter is a copy of the *arrow*. `PassReference.java`:

```java
public static void clickTwice(Counter c) {
    c.click();
    c.click();
}

public static void replace(Counter c) {
    c = new Counter(1000);
    System.out.println("  (inside replace) c is " + c);
}
...
Counter gate = new Counter(5);
clickTwice(gate);
System.out.println(gate);
replace(gate);
System.out.println(gate);
```

```
Counter[7]
  (inside replace) c is Counter[1000]
Counter[7]
```

![[java-references-pass-reference.mp4]]

In `clickTwice`, the copied arrow reaches the caller's object, so the clicks are real and `gate` reads 7 afterwards. In `replace`, the assignment swings the *copy* to a new object. `gate` is a different variable and never moved. When `replace` ends, `c` disappears, nothing points at the `Counter[1000]` any more, and Java reclaims it.

> **A method can change the object you hand it. It cannot change which object your variable points at.**

## 8. `null`, and the exception it causes

A reference variable that points at no object holds the special value **`null`**. It is a legal thing to store, print and compare. It is not an object, so it has no methods. `NullDemo.java`:

```java
Counter spare = null;                  // a reference that points at no object
System.out.println(spare == null);
System.out.println("spare is " + spare);

if (spare != null) {
    spare.click();                     // skipped: the check protects the call
}
System.out.println("still running");

spare.click();                         // no object to click
System.out.println("never printed");
```

```
true
spare is null
still running
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "Counter.click()" because "spare" is null
	at NullDemo.main(NullDemo.java:12)
```

The compiler accepted every line: `spare` has type `Counter`, and `Counter` has a `click()`. Whether an object is really there is only known when the program runs, so this is a **run-time error**, a `NullPointerException`. The message names the variable because `run_all.py` compiles with `javac -g`; without that flag it says `"<local1>"`, and the line number is what you go by. Python's equivalent is `None` and `AttributeError: 'NoneType' object has no attribute 'click'`.

`null` is not zero, not `""`, and not an empty `Counter`. It is the absence of an object.

## 9. Strings are objects

A `String` is an object holding a sequence of characters. It is the one class with a literal form: `"computer"` makes a `String` without `new`. (`new String("computer")` also works, and section 10 shows why nobody writes it.) The characters are numbered from **0 to `length() - 1`**.

![[java-references-string-cuts.svg|820]]

The picture gives two ways to read the same numbers. Read as labels, they name characters. Read as **cuts**, they name the gaps, and that reading makes `substring` obvious: `substring(3, 6)` cuts at 3 and at 6 and keeps what lies between, which is `6 - 3 = 3` characters. It also explains why `8` is a legal argument for an 8-character string (there is a cut at the very end) while there is no character 8.

The `String` methods to know, all from `Strings.java` with `s = "computer"`:

| Call | Result | Python | Note |
|---|---|---|---|
| `s.length()` | `8` | `len(s)` | a method, so it needs `()` |
| `s.substring(3, 6)` | `put` | `s[3:6]` | from cut 3 to cut 6 |
| `s.substring(3)` | `puter` | `s[3:]` | from cut 3 to the end |
| `s.substring(2, 3)` | `m` | `s[2]` | one character, as a `String` |
| `s.substring(8)` | empty string | `s[8:]` | legal: the last cut |
| `s.indexOf("put")` | `3` | `s.find("put")` | where the first match starts |
| `s.indexOf("z")` | `-1` | `s.find("z")` | not found is `-1`, not an error |
| `s.equals("computer")` | `true` | `s == "computer"` | same characters? |
| `s.compareTo(t)` | an `int` | `<`, `==`, `>` | section 10 |

Java has no `s[2]`. The way to get one character as a `String` is `s.substring(i, i + 1)`.

Calls can be **chained**, because a method that returns a `String` returns something you can call a method on: `s.substring(3).indexOf("t")` is `"puter".indexOf("t")`, which is `2`.

Step outside the cuts and the program stops (`OutOfRange.java`, with `s = "hello"`):

```
lo
Exception in thread "main" java.lang.StringIndexOutOfBoundsException: Range [3, 9) out of bounds for length 5
	...
	at OutOfRange.main(OutOfRange.java:5)
```

The trace lists Java's own library frames first. **Read it from the bottom**: the last line that names your file is where you made the call.

### Strings cannot be changed

A `String` is **immutable**. No method alters the characters of an existing `String`; every method that seems to edit one builds and returns a **new** `String`. `Immutable.java`:

```java
String word = "lantern";
word.substring(0, 4);              // builds "lant" and throws it away
System.out.println(word);

word = word.substring(0, 4);       // keeps it: word now points at the NEW string
System.out.println(word);

String first = "rain";
String second = first;             // two names, one String object
first += "bow";                    // builds "rainbow" and re-points first
System.out.println(first + " " + second);
```

```
lantern
lant
rainbow rain
```

Immutability is why aliasing never hurts with strings. `first` and `second` were aliases, yet `+=` could not reach into the shared object; it built `"rainbow"` and moved `first`'s arrow. `second` still points at `"rain"`. With `Counter`, a change through one alias showed through the other. With `String`, there is no such thing as a change.

### Joining strings to other things

`+` with a `String` on either side means concatenation, and the other operand is converted to text: a primitive directly, an object through its `toString()`. Python refuses `"a" + 1`; Java returns `"a1"`. The catch is that `+` still works left to right:

```java
System.out.println("a" + 1 + 2);           // left to right: "a1", then "a12"
System.out.println(1 + 2 + "a");           // left to right: 3, then "3a"
System.out.println("a" + (1 + 2));
```

```
a12
3a
a3
```

The rule from [[Java Values and Expressions]] holds: the types of the two operands decide what the operator does, one `+` at a time. `+=` works the same way, and `line += 7; line += 2.5; line += true;` after `line = "x"` leaves `x72.5true`.

## 10. Comparing: `==`, `equals`, `compareTo`

| You have | You ask | Use |
|---|---|---|
| two primitives | same value? | `==`, `!=` |
| two numbers | which is bigger? | `<`, `>`, `<=`, `>=` |
| two references | the very same object? | `==`, `!=` |
| a reference | is there an object at all? | `== null`, `!= null` |
| two `String`s | same characters? | `a.equals(b)` |
| two `String`s | which comes first? | `a.compareTo(b)` |

A comparison is an expression, and its value has type `boolean`: `boolean adult = age >= 18;` stores `false` when `age` is 17 (`Compare.java`). One warning carried over from [[Java Values and Expressions]]: `0.1 + 0.2 == 0.3` is `false` because of round-off, and the test that works is `Math.abs((0.1 + 0.2) - 0.3) < 1e-9`.

Now the opening puzzle. `StringEquals.java` makes four strings that all print as `hi`:

```java
String a = "hi";
String b = "hi";
String c = new String("hi");
String d = "h";
d += "i";                          // built while the program runs

System.out.println(a == b);
System.out.println(a == c);
System.out.println(a == d);
System.out.println(a.equals(b) + " " + a.equals(c) + " " + a.equals(d));
System.out.println("Hi".equals(a));
```

```
true
false
false
true true true
false
```

`a == b` is `true` for a reason that has nothing to do with the letters: Java stores each distinct *literal* once, so both arrows happen to point at the same object. `c` was made with `new` and `d` was assembled while the program ran, so each is a separate object and `==` says `false`. **`equals` compares the characters, and it is the only test that means what you think.** It is case-sensitive.

That is the whole bug in `YesBug.java`. The string the user types is built at run time, so it can never be the same object as the literal `"yes"`:

```
yes
false          answer == "yes"
true           answer.equals("yes")
```

Python programmers fall into this because Python's `==` compares contents. **Java's `==` on objects is Python's `is`. Java's `.equals()` is Python's `==`.**

Classes decide for themselves what `equals` means, usually by comparing attributes. `String` compares characters. A class that does not define one inherits `Object`'s, which is the same as `==`.

**Ordering.** `<` is for numbers, and the compiler refuses it for strings (`StringLessThan.java`): `error: bad operand types for binary operator '<'`. Use `compareTo`, and read only the **sign** of what comes back:

| Call | Returns | Meaning |
|---|---|---|
| `"apple".compareTo("banana")` | `-1` | negative: `apple` comes first |
| `"banana".compareTo("apple")` | `1` | positive: `banana` comes after |
| `"apple".compareTo("apple")` | `0` | zero: equal |
| `"apple".compareTo("apply")` | `-20` | the size is a character-code difference; only the sign matters |
| `"app".compareTo("apple")` | `-2` | a prefix comes first |
| `"Zebra".compareTo("apple")` | `-7` | every capital letter comes before every lower-case letter |

The last row is [[Text Encoding]] showing through: the comparison is made on character codes, where `Z` is 90 and `a` is 97.

## 11. Input: a library class at work

`Scanner` is a class in the package `java.util`. Using it shows everything above at work: an import, a constructor call, a reference, and instance methods (`Input.java`).

```java
import java.util.Scanner;                  // Scanner lives in the package java.util, so it must be imported
...
Scanner keyboard = new Scanner(System.in);     // a library class, used to make an object

System.out.print("Name: ");
String name = keyboard.nextLine();
System.out.print("Age: ");
int age = Integer.parseInt(keyboard.nextLine());
System.out.println(name + " will be " + (age + 1) + " next year.");
```

With `Ada` and `17` typed, the last line is `Ada will be 18 next year.` Everything typed arrives as a `String`. `Integer.parseInt` and `Double.parseDouble` are class methods that turn text into a number, and they stop the program with a `NumberFormatException` if the text is not one. The brackets round `age + 1` matter, for the reason in section 9: without them the output would be `171`.

## Python to Java, at a glance

| Idea | Python | Java |
|---|---|---|
| A function | `def area(w, h):` | `public static int area(int w, int h)`; types in the header |
| Same name, different parameters | the later `def` replaces the earlier | overloading: both exist, arguments choose |
| Make an object | `Counter(250)` | `new Counter(250)` |
| No object | `None` | `null` |
| Calling a method on nothing | `AttributeError` | `NullPointerException` |
| Same object? | `a is b` | `a == b` |
| Same contents? | `a == b` | `a.equals(b)` |
| String order | `a < b` | `a.compareTo(b) < 0` |
| Length | `len(s)` | `s.length()` |
| Slice | `s[3:6]` | `s.substring(3, 6)` |
| One character | `s[2]` | `s.substring(2, 3)` |
| Find | `s.find("x")`, gives `-1` | `s.indexOf("x")`, gives `-1` |
| Text to number | `int("42")` | `Integer.parseInt("42")` |
| Text plus number | `"a" + 1` is a `TypeError` | `"a" + 1` is `"a1"` |
| Read a line | `input()` | `keyboard.nextLine()` on a `Scanner` |
| Strings can be edited in place | no | no |

## Worked examples

All three are in `Examples.java`.

### Example 1: count the objects, then trace

```java
Counter a = new Counter(1);
Counter b = new Counter(1);
Counter c = a;
a.click();
b = c;
b.click();
c = new Counter(10);
c.click();
```
What are the three counts, and what are `a == b` and `a == c`?

*Trigger: several reference variables and assignments between them, so the question is about arrows. Tool: count the `new`s, draw one box per object, and move arrows on every assignment.*

Three `new`s, so three objects: call them X (1), Y (1) and Z (10). Start: `a → X`, `b → Y`. `c = a` gives `c → X`. `a.click()` makes X 2. `b = c` moves `b` to X, and now nothing points at Y. `b.click()` makes X 3. `c = new Counter(10)` moves `c` to Z, and `c.click()` makes Z 11. So `a` and `b` both read **3**, `c` reads **11**, `a == b` is **true** and `a == c` is **false**. The program prints `3 3 11` and `true false`.

### Example 2: cut an address at the @

Split `"ada.lovelace@analytical.org"` into user and domain.

*Trigger: a position that is not known in advance, marked by a character. Tool: `indexOf` to find the cut, `substring` on each side of it.*

```java
int at = email.indexOf("@");               // 12
String user = email.substring(0, at);      // cut 0 to cut 12: "ada.lovelace"
String domain = email.substring(at + 1);   // skip the @ itself: "analytical.org"
```
Thinking in cuts settles the two off-by-one questions at once. `substring(0, at)` stops *before* the `@` because cut 12 lies to its left. `at + 1` is the cut to its right. The user part has `at - 0 = 12` characters, its initial is `user.substring(0, 1)`, which is `"a"`, and `domain.indexOf(".")` is `10`. A careful version checks `at != -1` first: with no `@`, `substring(0, -1)` throws.

### Example 3: can a method change the caller's String?

```java
public static void shout(String s) {
    s = s + "!";
}
...
String word = "stop";
shout(word);
System.out.println(word);
```

*Trigger: a parameter is assigned to inside a method. Tool: call by value, from section 7.*

It prints `stop`. `s` is a copy of the arrow. `s + "!"` builds a new `String` and the assignment moves the *copy*. For a `Counter` there was a second route, calling a method that changes the object, but `String` is immutable and has no such method. So **no method can ever change a caller's `String`**. The way out is to return the new string and let the caller keep it: `word = shouted(word);` prints `stop!`.

## Predict, then check

Write your answer before you look. Each is one line of reasoning.

1. `String s = "hello"; s.substring(1, 3);` What does `s` hold afterwards?
2. `"hello".substring(2, 2)` — a value, or an exception?
3. `"hello".indexOf("l")`
4. `Counter a = new Counter(); Counter b = new Counter(); a = b; a.click();` How many objects were made, and what is `b.getCount()`?
5. `System.out.println(1 + 1 + "1" + 1 + 1);`
6. `String t = null; System.out.println(t.length());` Compile-time or run-time?
7. `"cat".compareTo("car")` — positive, negative or zero?
8. Which is safe when `name` might be `null`: `name.equals("Ada")` or `"Ada".equals(name)`?

> [!success]- Answers
> 1. Still `"hello"`. The result `"el"` was built and thrown away.
> 2. A value: the empty string. Both cuts are legal and nothing lies between them.
> 3. `2`. The first match.
> 4. Two objects. After `a = b` both names point at the second one, so `b.getCount()` is `1`, and nothing points at the first.
> 5. `2111`. `1 + 1` is `2`, then `"21"`, `"211"`, `"2111"`.
> 6. Run-time: a `NullPointerException`. The compiler sees a `String` variable and a `String` method and is satisfied.
> 7. Positive. The first two letters match, and `t` comes after `r`.
> 8. `"Ada".equals(name)`. A literal is never `null`, and `equals` returns `false` when handed `null`. The other form throws.

## Common Misconceptions (Teaching Notes)

1. **"`==` compares what two strings say."** It compares arrows. It returns `true` for two identical literals only because Java stores a literal once, which makes the mistake survive small tests and fail on real input.
2. **"`s.substring(0, 3)` shortens `s`."** No `String` method changes its string. If the result is not stored, it is lost.
3. **"`b = a` makes a second object."** It makes a second arrow. Count the `new`s.
4. **"Java passes objects by reference."** Java passes *references by value*. The difference is `replace` in section 7: a method that assigns to its parameter changes nothing for the caller.
5. **"`null` is an empty object"**, or the same as `""` or `0`. `"".length()` is `0`. `null` has no `length()` to call.
6. **"The return type is part of the signature."** Two methods that differ only in return type will not compile.
7. **"`length` is a property, as in Python's `len`."** For a `String` it is a method: `s.length()`, with brackets.

## Exam Notes

### AP Computer Science A (course effective Fall 2025)

This covers topics **1.9, 1.10 and 1.12 to 1.15** of Unit 1, completes **1.4** (`null`, assigning an object, input) and **1.7** (attributes, behaviours, using a library class to create objects), and covers **2.2** and the object-comparison half of **2.6** from Unit 2. The Java Quick Reference, provided in the exam, lists the six `String` methods in section 9's table, `Integer.parseInt` and `Double.parseDouble`.

- **Often set as multiple choice:** the output of a chain of `substring` and `indexOf` calls; which call matches a given signature, or which overload runs; what two aliased variables show after a method call; whether `==` or `equals` is `true`; whether a snippet throws `NullPointerException` or `StringIndexOutOfBoundsException`.
- **In the written questions:** the course description says free-response Question 1 (Methods and Control Structures) has a part that requires statements calling the methods of a class you are given, which is how `Counter` was used here, and a 3-point part that requires calling `String` methods.
- **Inside the course:** signatures, overloading, void and non-void, call by value, flow of control through a call; class methods and the `ClassName.` form; class, object, attribute, behaviour; every class extends `Object`; `new`, constructor signatures and overloaded constructors; references, aliases and `null`; `NullPointerException`; `String` literals, immutability, `+` and `+=`, implicit `toString()`; index range; the six Quick Reference methods and `substring(i, i + 1)`; `==` on references; comparing with `null`; using a class's `equals`.
- **Outside the course**, in its own words: designing and implementing inheritance; overriding `toString`; overriding `equals`; calling `equals` on a `String` with an argument that is not a `String`; any specific form of input from the user. `Scanner` on the keyboard is named as one way to get text but is not examined; it returns later for reading files.

### Cambridge 9618 (Paper 4) and IB Computer Science

Both accept Java. A Java candidate needs all of the above, and section 11 is no longer optional: 9618 Paper 4 tasks read from the keyboard and from text files. The `==` trap is just as live there, because the code compiles, runs and gives the wrong answer.

### Where this is *not* examined

Cambridge 0478 is answered in pseudocode or Python and needs none of this. 9618 candidates answering in Python meet the same ideas as `is`, `==` and `None`.

## Connections

- **The concepts, taught in Python:** [[Object-Oriented Programming]] (classes, objects, constructors, inheritance), [[Programming Fundamentals]] (functions, parameters, string handling).
- **The same arrow elsewhere:** [[Arrays]] (aliasing, and why an array argument can be changed by the method that receives it), [[Linked List]] (a data structure made of nothing but references), [[The Call Stack]] (where parameters live and why they vanish).
- **Underneath:** [[Text Encoding]] (what `compareTo` actually compares), [[RAM and the Memory Hierarchy]] (where objects live).
- **Previous companion:** [[Java Values and Expressions]]. **Next:** [[Java Control Flow]].

## Notation Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $0 \le i \le n - 1$ | `0 \le i \le n - 1` | The legal character indices of a string of length $n$ |
| $0 \le from \le to \le n$ | `0 \le from \le to \le n` | The legal cuts for `substring(from, to)` |
| $to - from$ | `to - from` | How many characters `substring(from, to)` returns |

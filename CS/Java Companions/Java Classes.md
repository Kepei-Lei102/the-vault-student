---
chinese: Java 的类 (Java de lèi)
prerequisites:
  - "[[Java Control Flow]]"
  - "[[Object-Oriented Programming]]"
leads_to:
  - "[[Java Arrays and ArrayList]]"
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
  - misconception/parameter-named-like-the-field-sets-the-field
  - misconception/the-default-constructor-is-always-there
  - misconception/static-methods-can-see-instance-variables
  - misconception/private-means-other-objects-of-the-same-class-cannot-see-it
  - misconception/return-inside-a-loop-only-leaves-the-loop
---

# Java Classes Java 的类

> `size = size;`
>
> A constructor with that line compiles, runs, and leaves every object it makes with a size of zero. Both names mean the parameter. The field it was meant to set is never mentioned.

## What this is for

You have used classes that other people wrote: `String`, `Scanner`, and the small `Counter` of [[Java Objects, References and Strings]]. Now you write one. What a class *is*, and why data and behaviour are bundled, is taught in Python in [[Object-Oriented Programming]], and nothing here repeats it. What follows is how Java spells a class, and the handful of places where the spelling changes the meaning.

Every program below is a real file in the folder `java-classes`, and every output shown came from compiling and running it. Run `python3 run_all.py` there to reproduce all of it. One class, `BankAccount`, is built up section by section; the finished file is `BankAccount.java`.

**The one idea to carry through:** a class draws a line round some data and says **who may touch it**. Fields are `private`, so the only way to change an object's state is through the `public` methods the class chose to offer, and each of those can check what it is asked to do. The rest, constructors, `this`, `static`, scope, is the machinery that makes that line hold.

## 中文锚点

在银行里，你不能自己走进金库去搬钱。你得到柜台上去提要求：存这笔，取那笔，告诉我余额是多少。柜员会核对每一个要求，只有规矩允许的才会办：取的钱比余额多，不管你在柜台上怎么说，都会被拒绝。写一个类，做的就是一模一样的安排。数据（你的余额）是私有的，类外面的任何代码都伸不进手去改它。唯一的入口是这个类自己选择公开的那几个方法，而每一个方法在动手之前都可以先核对一下它被要求做的事。这样一来，余额就永远不可能变成一个连类自己都不会放行的数。这里的要点不是保密，而是负责：程序里有一个地方，也就是这个类，对它的数据的状态负全责，其余的一切都得来问它。

## 1. Design before code: what does an account have and do?

Before writing, decide what the thing **has** (its attributes, which become **instance variables**) and what it **does** (its behaviours, which become **methods**). A bank account has an owner, a balance, and a count of withdrawals. It can be deposited into, withdrawn from, and asked its balance. Writing that down in words, or as a box with two compartments, is the whole of the design step, and it is the step the written exam asks for by name.

That decision is an **abstraction**: the account is reduced to the details that matter here, and the rest is left out. Two kinds run through everything below. **Data abstraction** gives a group of values one name, `BankAccount`, so that the rest of the program never needs to know how the values are stored. **Procedural abstraction** gives a process one name, `withdraw`, so that a caller needs to know what it does and not how. If the inside of `withdraw` is rewritten to be faster, no caller has to change, so long as its signature and its promise stay the same. Breaking a large behaviour into small named methods, and giving them parameters so one method serves many cases, is how a class stays readable as it grows.

## 2. The anatomy

```java
public class BankAccount {
    private String owner;                                  // instance variables: every account has its own
    private double balance;
    private int withdrawals;

    public BankAccount(String owner, double opening) {     // a constructor: same name as the class, no return type
        this.owner = owner;
        balance = opening;
        withdrawals = 0;
    }

    public double getBalance() {                           // a method
        return balance;
    }
}
```

| Part | Keyword | Rule in this course |
|---|---|---|
| the class | `public class Name` | always `public`; the file is `Name.java` |
| instance variables | `private` | one copy per object; **private unless the specification says otherwise** |
| constructors | `public` | always `public`; named after the class; no return type, not even `void` |
| methods | `public` or `private` | `public` can be called from anywhere; `private` only from inside the class |

`private` means *reachable only by code inside this class*. `public` means *reachable from anywhere*. Keeping the fields private and offering public methods is **encapsulation**, and the compiler enforces it (`Private.java`):

```
Private.java:4: error: balance has private access in BankAccount
        ada.balance = 1000000.0;
```

The line from `main` that tried to write a million into the balance did not run. It did not compile.

## 3. Constructors and the object's state

An object's **state** is its instance variables and their values at a moment. The constructor's job is to give every one of them a sensible starting value, so that no object ever exists half-made. When `new BankAccount("Ada", 100.0)` runs, four things happen in order:

![[java-classes-construct.mp4]]

1. Memory is set aside for a new object, every field at its **default value**: `0` for `int`, `0.0` for `double`, `false` for `boolean`, `null` for a reference.
2. The constructor starts, with `this` pointing at the new object and the arguments copied into the parameters, by the same call-by-value rule as any method.
3. The body runs, and each assignment fills a field.
4. The reference to the finished object is handed back, and `ada` stores it.

A class may have several constructors with different signatures, and one can hand over to another with `this(...)` as its first line:

```java
public BankAccount(String owner) {
    this(owner, 0.0);                                      // an empty account: reuse the two-argument constructor
}
```

**The default constructor exists only if you write none.** `Defaults.java` declares four fields and no constructor, and `new Defaults()` works and prints `0 0.0 false null`. The moment a class writes any constructor of its own, the free one is gone. `NoDefault.java` tries `new BankAccount()`:

```
error: no suitable constructor found for BankAccount(no arguments)
```

One more rule, about constructors that receive an object. If a parameter refers to something **mutable** (a list, say), store a *copy*, not the reference, or the caller can change your object's state from outside by changing its own list later. `CopyOrShare.java` stores `new ArrayList<String>(log)`; the caller then adds to its list, and the sizes are `2 1`. The copy did not follow.

## 4. Methods: accessors, mutators, and `return`

| Kind | Does | Return type | Example |
|---|---|---|---|
| **accessor** | hands out a copy of a field's value; changes nothing | non-void | `getBalance()` |
| **mutator** (modifier) | changes the state | often `void` | `deposit(50.0)` |

A non-void method promises a value of its return type, and `return` delivers it: the expression is evaluated and its **value** is handed back. `return` also ends the method at once, from wherever it stands, including from inside a loop or an `if` (`Return.java`):

```java
public static int firstEven(int start, int stop) {
    for (int n = start; n <= stop; n++) {
        if (n % 2 == 0) {
            return n;                                      // leaves the loop AND the method
        }
    }
    return -1;                                             // every path must return an int
}
```

`firstEven(3, 9)` is `4` and `firstEven(3, 3)` is `-1`. Leave out the last line and the compiler refuses: `error: missing return statement` (`MissingReturn.java`). A method that returns from inside an `if` must still return on the path where the `if` is false.

`withdraw` uses all of this: it refuses an overdraft, charges the fee, and reports what happened, so a caller can act on the answer.

```java
public boolean withdraw(double amount) {
    if (amount > balance) {
        balance -= OVERDRAFT_FEE;
        return false;                                      // nothing below this line runs
    }
    balance -= amount;
    withdrawals++;
    return true;
}
```

From `UseAccount.java`, with Ada at 150.0 and Bob at 0.0:

```
true 120.0
false -15.0
```

The method's signature and its comment are its contract. The **precondition** says what must be true before the call (`amount > 0`); the **postcondition** says what is true afterwards. Neither is checked by the compiler. They are promises between the writer and the caller.

## 5. Parameters that are objects

When the argument is a primitive, the parameter is a copy of the value, and the method cannot touch the caller's variable. When the argument is an object reference, the parameter is a copy of the *reference*, and the method **can** change the object; that whole story is in [[Java Objects, References and Strings]]. Two things are new inside a class.

**Returning a reference returns the object, not a copy of it.** `richerOf` hands back `other` or `this`; the caller then holds the very same account.

**A method may reach the private fields of another object of its own class.** Privacy is per class, not per object:

```java
public boolean transferTo(BankAccount other, double amount) {
    if (withdraw(amount)) {
        other.balance += amount;                           // legal: other is a BankAccount, and so is this class
        return true;
    }
    return false;
}
```

Hand `transferTo` a parameter of any other type and `.balance` on it would not compile. The good habit stated in the course: **do not modify an object you were handed unless the specification asks you to.**

## 6. `this`

Inside a constructor or an instance method, `this` is a reference to the object the method was called on. It has three uses.

**Telling a field from a parameter with the same name.** `Shadow.java` is the opening puzzle:

```java
public Shadow(int size) {
    size = size;                                           // both names mean the parameter
}
```

Inside the constructor a parameter **hides** the field with the same name, so this line assigns the parameter to itself and the field keeps its default. `new Shadow(42).getSize()` prints `0`. The fix is `this.size = size;`: the field on the left, the parameter on the right. Where the names differ, as in `balance = opening;`, `this` is not needed, though it is never wrong.

**Passing the current object.** `return this;` in `richerOf` hands the caller the very account it asked; `other.compareTo(this)` would hand it to another method.

**Where `this` does not exist.** A `static` method belongs to the class, not to any object, so it has no `this`. Section 7 shows the compiler saying so.

## 7. `static`: what belongs to the class

Some things are not per-account. The number of accounts opened is one fact about the whole class, and the overdraft fee is one number every account uses.

```java
private static int accountsOpened = 0;                     // one copy, shared by every object
public static final double OVERDRAFT_FEE = 15.0;           // final: its value cannot change
```

| | Instance variable | Class variable (`static`) |
|---|---|---|
| Copies | one per object | one, shared by all |
| Belongs to | the object | the class |
| Reached from outside as | `ada.getBalance()` | `BankAccount.getAccountsOpened()`, `BankAccount.OVERDRAFT_FEE` |

`Counter.java` makes three objects; each gets its own `id` from the shared count, and the class reports `1 2 3 | 3`.

A **class method** (`static`) runs without any object, so the rules follow from that. It may use class variables and call other class methods. It may *not* use an instance variable or call an instance method, because there is no object whose variable that would be, unless an object is handed to it as a parameter. `StaticRules.java`:

```
error: non-static variable mine cannot be referenced from a static context
error: non-static variable this cannot be referenced from a static context
```

`main` is a class method, which is why every program so far has had to `new` an object before calling instance methods on it. A `final` variable, `static` or not, is assigned once and then fixed; by convention its name is in capitals.

## 8. Scope: where a name means something

Three kinds of variable live in a class, and a name is visible only inside the region it was declared in.

![[java-classes-scope.svg|820]]

- **Class variables** are visible throughout the class and, if `public`, outside it through the class name.
- **Instance variables** are visible throughout the class; each method sees the copy that belongs to `this`.
- **Local variables** are declared in the header or body of a block: a method, a constructor, a loop. They exist only inside that block. **Parameters are local variables** of their method. Locals cannot be `public` or `private`; those words apply to members of the class, not to what happens inside one method.

`Scope.java` prints `1 2 9 3 4` from inside a loop and `1 2 9 3` after it: the loop's `inner` has gone. `OutOfScope.java` declares `secret` in one method and reads it in another, and gets `error: cannot find symbol`. And when a local or a parameter shares a name with a field, the local wins inside its block, which is the whole of the `Shadow` story.

The design rule that follows is **least scope**: declare each variable in the smallest region that needs it. A loop counter belongs in the loop header. A value used by one method belongs inside that method. Only a fact about the object belongs in an instance variable, and only a fact about the class belongs in a class variable.

## Python to Java, at a glance

| Idea | Python | Java |
|---|---|---|
| Declare a class | `class BankAccount:` | `public class BankAccount { ... }` in `BankAccount.java` |
| Instance variables | created by assignment in `__init__` | declared at the top, with a type and `private` |
| Constructor | `def __init__(self, owner, opening):` | `public BankAccount(String owner, double opening)` |
| The current object | `self`, always written | `this`, written only when needed |
| Field versus parameter | `self.size = size` | `this.size = size` |
| Private | `_balance` by convention, `__balance` by mangling | `private double balance;` enforced by the compiler |
| Accessor | `def get_balance(self):` | `public double getBalance()` |
| Class variable | assignment in the class body | `private static int accountsOpened;` |
| Class method | `@staticmethod` | `public static ...` |
| Constant | a name in capitals, by convention | `static final`, enforced |
| Default values | none: an unset attribute is an error | `0`, `0.0`, `false`, `null` |
| No constructor written | `__init__` is inherited from `object` | a no-argument default constructor is supplied |

## Worked examples

### Example 1: write the class from its specification

> A `Thermostat` records a target temperature in degrees. `new Thermostat(20.0)` sets the target. `raise(2.5)` increases it, `lower(1.0)` decreases it but never below 5.0, and `getTarget()` reports it. Write the class.

*Trigger: a specification table naming a constructor and three behaviours. Tool: one private field per attribute, one public method per behaviour, the check inside the method that guards the rule.*

```java
public class Thermostat {
    private double target;

    public Thermostat(double target) {
        this.target = target;
    }

    public void raise(double amount) {
        target += amount;
    }

    public void lower(double amount) {
        if (target - amount < 5.0) {
            target = 5.0;
        } else {
            target -= amount;
        }
    }

    public double getTarget() {
        return target;
    }
}
```

The `this.` in the constructor is forced by the shared name; the two mutators need none. The rule "never below 5.0" lives inside `lower`, so no caller can break it.

### Example 2: trace the calls

```java
BankAccount p = new BankAccount("P", 40.0);
BankAccount q = new BankAccount("Q");
p.transferTo(q, 25.0);
q.withdraw(30.0);
p.deposit(5.0);
System.out.println(p.getBalance() + " " + q.getBalance() + " " + BankAccount.getAccountsOpened());
```
*Trigger: a sequence of mutator calls on two objects. Tool: a table of both states after each line, applying each method's own rule.*

| after | `p.balance` | `q.balance` |
|---|---|---|
| construction | 40.0 | 0.0 |
| `p.transferTo(q, 25.0)`: `p.withdraw(25.0)` succeeds | 15.0 | 25.0 |
| `q.withdraw(30.0)`: 30 > 25, refused, fee charged | 15.0 | 10.0 |
| `p.deposit(5.0)` | 20.0 | 10.0 |

It prints `20.0 10.0 2`. The last number counts constructor calls in this program, not accounts that still exist.

### Example 3: find the three bugs

```java
public class Ticket {
    private int row;
    private int seat;
    public static int sold = 0;

    public Ticket(int row, int seat) {
        row = row;
        this.seat = seat;
        sold++;
    }

    public static int getRow() {
        return row;
    }

    public void print() {
        int sold = 99;
        System.out.println(row + "-" + seat + " sold " + sold);
    }
}
```
*Trigger: "find the bugs" on a class. Tool: check each name against its scope, each method against `static`, and each constructor line against shadowing.*

1. `row = row;` assigns the parameter to itself; the field stays `0`. Write `this.row = row;`.
2. `getRow` is `static` and reads the instance variable `row`: it does not compile. Remove `static`.
3. Inside `print`, the local `sold` hides the class variable, so every ticket prints `sold 99`. Rename the local, or drop it.

## Predict, then check

1. A class declares `private boolean paid;` and writes no constructor. What is `paid` in a new object?
2. `public Box(int w) { w = w; }` What is the field `w` after `new Box(7)`?
3. A class has two constructors, `Box()` and `Box(int)`. Is `new Box(3, 4)` a compile-time error, a run-time error, or fine?
4. Can `public static double average(BankAccount a, BankAccount b)` read `a.balance` if it is written inside `BankAccount`?
5. `public int f(int n) { if (n > 0) { return 1; } }` Compile-time error or fine?
6. Two `Counter` objects are made and `Counter.getCreated()` is called on the class. Does it need an object?
7. `for (int i = 0; i < 3; i++) { total += i; } return total;` where `total` is an instance variable. Compiles?
8. Inside an instance method, is `this.this.x` legal?

> [!success]- Answers
> 1. `false`, the default for `boolean`.
> 2. `0`. Both `w`s are the parameter.
> 3. Compile-time: there is no constructor with signature `Box(int, int)`.
> 4. Yes. `a` is a `BankAccount` and the method is inside `BankAccount`; privacy is per class. Being `static` does not matter, because the object came in as a parameter.
> 5. Compile-time error: the path where `n <= 0` returns nothing.
> 6. No. It is a class method, called on the class name.
> 7. Yes. `i` is local to the loop and `total` is a field visible throughout the method.
> 8. No. `this` is a reference to the current object; it has no field called `this`.

## Common Misconceptions (Teaching Notes)

1. **"`size = size;` sets the field."** Both names are the parameter. Write `this.size = size;`.
2. **"Every class has a no-argument constructor."** Only a class that writes no constructor at all.
3. **"A `static` method can use the fields."** It has no object, so no `this` and no instance variables, unless one is passed in.
4. **"`private` hides a field from other objects."** It hides it from other *classes*. Another `BankAccount` can read this one's balance.
5. **"`return` inside a loop just leaves the loop."** It leaves the method.
6. **"An accessor returns the field itself."** For a primitive it returns a copy of the value. For an object it returns the reference, which is why mutable fields deserve care.
7. **"Fields declared without a value are uninitialised, like locals."** Fields get defaults; only locals must be assigned before use.

## Exam Notes

### AP Computer Science A (course effective Fall 2025)

This covers topics **3.1 and 3.3 to 3.9** of Unit 3. Topic 3.2, the impact of program design, is in [[Ethics and Ownership]].

- **The written question that is this card:** free-response Question 2 is *Class Design*. The course description says students "design and implement a class based on provided specifications and examples", given "a scenario and specifications in the form of a table demonstrating ways to interact with the class and the results", and that the class "must include a class header, instance variables, a constructor, a method, and implementation of the constructor and required method". Example 1 is that question's shape.
- **Often set as multiple choice:** what a constructor leaves in a field (shadowing, defaults); whether a class method may reference an instance variable; the value of a class variable after several objects are made; which of several class definitions compiles; what an accessor returns.
- **Inside the course:** abstraction (data and procedural), attributes, instance and class variables, method decomposition; `public` and `private`, classes and constructors always `public`; state, the constructor's duty to initialise, `this(...)` is not named but is legal, default constructor and default values, copying a mutable parameter; void and non-void methods, `return` by value and as flow of control, accessors and mutators, primitive parameters as copies; references as parameters and return values, privacy per class; class methods and class variables, `static`, `final`; local variables and parameters, shadowing; `this` as the current object, passing `this`, no `this` in a class method.
- **Outside the course, by its own statements:** designing or implementing inheritance, and overriding `toString` or `equals`; the `BankAccount` above writes a `toString` because printing an object is convenient, not because it is examined. Interfaces, abstract classes and packages are not in the description.

### Cambridge 9618 (Paper 4) and IB Computer Science

Both accept Java, and both examine class writing more widely than AP: 9618 §20.1 and IB B3 require inheritance and polymorphism, which [[Object-Oriented Programming]] teaches in Python with a Java specimen. Everything above is the foundation for those, and the Paper 4 habit of "declare private, provide get and set" is exactly section 2.

### Where this is *not* examined

Cambridge 0478 has no classes.

## Connections

- **The concepts, taught in Python:** [[Object-Oriented Programming]] (class, object, encapsulation, and the inheritance this companion stops short of), [[User-Defined Data Types]].
- **Earlier companions:** [[Java Values and Expressions]] (types and defaults), [[Java Objects, References and Strings]] (references, aliases, call by value, using a class), [[Java Control Flow]] (the `if`s and loops inside the methods).
- **Where the locals live and die:** [[The Call Stack]]; the frames are introduced in [[Recursion]].
- **Next:** [[Java Arrays and ArrayList]].

## Notation Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| — | — | This companion has no mathematical notation. Its reference is the table of keywords in section 2. |

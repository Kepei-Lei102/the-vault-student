---
chinese: 编程范式 (biānchéng fànshì)
prerequisites:
  - "[[Assembly Language]]"
  - "[[Object-Oriented Programming]]"
  - "[[SQL]]"
  - "[[Program Design]]"
leads_to:
  - "[[Compilers and Interpreters]]"
  - "[[Recursion]]"
tags:
  - subject/cs
  - domain/programming
  - domain/languages
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-20-1
  - misconception/paradigm-is-a-language
  - misconception/declarative-means-no-order
  - misconception/describe-the-code-not-the-paradigm
  - type/deep
---

# Programming Paradigms 编程范式

> *Every program computes something. A paradigm is what you are allowed to think in while you write it: instructions and addresses, statements that change state, objects that carry their own behaviour, or facts and rules that an engine searches for you. Same answer, four different things in your head.*

![[paradigms-manim.mp4]]

## Definition

### Formal

A **programming paradigm** is a style or way of thinking about programming: the set of concepts a language gives you to express a solution, and the shape a program takes when written in it. A language usually belongs mainly to one paradigm, but most modern languages support several. The syllabus names four:

- **Low-level.** Programs written in the instruction set of a processor (assembly language or machine code): registers, memory addresses, and one machine operation per line. Data is reached through **addressing modes**: **immediate** (the operand is the value), **direct** (the operand is the address of the value), **indirect** (the operand is the address of a cell that holds the address), **indexed** (the operand plus the index register), and **relative** (an offset from the current position).
- **Imperative (procedural).** Programs as an explicit **sequence of commands** that change the program's **state**: variables changed by assignment, selection and iteration, and procedures and functions that group commands and can be called. The programmer says *how*, step by step, in the order written.
- **Object-oriented.** Programs built from **objects**, each bundling its data (**attributes**) with the code that acts on it (**methods**), created from **classes**; with **encapsulation** (attributes private, reached through **getters** and **setters**), **inheritance** (a class extending another), **polymorphism** (one method name, behaviour chosen by the object's class), **containment** (an object holding other objects), and **instances** (the objects a class produces).
- **Declarative.** Programs that state **what** is to be achieved, not **how**: a set of **facts** and **rules** (a *logic* language such as Prolog) or of function definitions (a *functional* language), and a **goal** or **query** that the language's engine satisfies by searching the facts and rules. SQL is declarative: `SELECT` states the result wanted and the database finds the steps.

### Intuitive

Ask four people to find every cheap item in a shop. The first walks the shelves with a clipboard, an index card for where they are, and a rule for stepping to the next shelf: low-level. The second says "for each item, if it costs under six, add it": procedural. The third hands every item a label that says whether it is cheap and asks the shop to total its own cheap items: object-oriented. The fourth writes on the wall "an item is cheap if its price is under six" and asks "which items are cheap?", and the shop answers: declarative. All four get eight. The card's scripts do exactly this, and the four programs are shorter than this paragraph.

### 中文锚点

编程范式是写程序时"允许你用来思考的那套概念"——同一个问题，用不同的范式，脑子里装的东西不一样。四种：**低级**范式直接用处理器的指令集写，一行一条机器指令，数据靠寻址方式找到——立即寻址（操作数就是值）、直接寻址（操作数是地址）、间接寻址（操作数所指的单元里存着真正的地址）、变址寻址（操作数加上变址寄存器）、相对寻址（相对当前位置的偏移）。**命令式**（过程式）范式把程序写成一串按顺序执行、不断改变程序状态的命令：变量、赋值、选择、循环、过程和函数——程序员说的是"怎么做"。**面向对象**范式把数据和操作数据的代码捆成对象，对象由类生成，靠封装、继承、多态和包含来组织。**声明式**范式只说"要什么"不说"怎么做"：写下事实和规则，再提出一个目标，语言的引擎自己去搜索哪些事实和规则能满足这个目标——Prolog 是这样，SQL 也是这样。这张卡拿同一个问题（把价格低于 6 的商品加起来），用四种范式各写了一遍程序，四个程序给出同一个答案 8；为了能真的运行声明式的那一个，卡里附了一个 120 行的迷你 Prolog 引擎，卡上每一道事实与规则的题都能在它上面跑出结果。

---

## Part I — What a paradigm is, and why there are several

A processor understands one thing: fetch an instruction, execute it, move on ([[CPU Architecture and the Fetch-Execute Cycle]]). Every program ends up as that. A paradigm is a layer of *pretending* built on top, so that a human can think about the problem in terms that fit the problem rather than the chip. The pretence is paid for by a translator ([[Compilers and Interpreters]]) or by an engine that does the searching, and the paradigms differ in how much they take off the programmer's hands.

![[paradigms-map.svg|700]]

Read the figure left to right and one thing changes: **how much of the *how* is yours.** At the low-level end you write every step and every address. Procedural code lets you name a step and repeat it, but you still give the steps in order. Object-oriented code lets you say *what an item is* and *what it can do*, and the steps live inside the objects. Declarative code has you say only what must be true, and the engine, whether it is a Prolog interpreter or a database, decides the order of the steps, or whether there are any.

`paradigms-four-ways.py` makes this concrete. One problem, a shop's five items with prices, one question: the total of the prices under 6. Four programs, one answer, 8. The low-level one executes 66 instructions; the declarative one is a single line of SQL and no loop. Nothing about the answer changed. What changed is what the programmer had to hold in their head.

> [!tip] A paradigm is not a language
> Python is procedural in one file and object-oriented in the next; C# is object-oriented with a declarative query language (LINQ) inside it; SQL is declarative but has procedural extensions. The exam asks you to name the paradigm *of a piece of code*, and the examiners' report warns that candidates "incorrectly described what the code was doing rather than stating the programming paradigm it represented". Look for the tell: registers and mnemonics, a loop that assigns, a `class`, or facts with full stops.

---

## Part II — Low-level: instructions and addresses

The low-level paradigm is [[Assembly Language]]'s: one processor operation per line, data in numbered memory cells and a few registers, and control by jumps. What the A2 syllabus adds to the AS material is the ability to *write* code using all five **addressing modes**, which are the five ways an operand can say where a value is.

![[paradigms-machine.svg|700]]

The script's machine has an accumulator, an index register and fourteen memory cells, and its program adds the cheap prices with every mode in use:

| Mode | Operand | What the machine reads | In the program |
|---|---|---|---|
| **Immediate** | `#0` | the number 0 itself | `LDM #0` sets the accumulator to zero |
| **Direct** | `11` | the contents of cell 11 | `STO 11` writes the running total there |
| **Indirect** | `(12)` | cell 12 holds 13, so read cell 13 | `SUB (12)` subtracts the limit found through a pointer |
| **Indexed** | `0,IX` | cell 0 plus the index register | `LDX 0,IX` reads price number IX |
| **Relative** | a label or offset | a position measured from here | `JMP NEXT`, `JLT ADDIT` jump within the program |

Indirect addressing is the one that trips students: the operand is not the data and not the data's address, but the address of a cell *that holds* the data's address. It is how a program can be written once and pointed at different data by changing one cell, which is what a pointer is. Indexed addressing is how a loop walks an array without rewriting the address each time: the instruction stays `LDX 0,IX` and `INC IX` moves it along.

Every step here is *how*. The paradigm's characteristics, in the words the mark scheme uses: programs use the **instruction set of a processor**; they work with **registers and memory addresses**; they are **specific to one processor**; they give the programmer complete control and the compiler nothing to optimise. It is the paradigm of device drivers, boot code, and the innermost loop of anything that must be fast.

---

## Part III — Imperative (procedural): statements that change state

The paradigm every student meets first. A program is a **sequence of commands**; each command **changes the state** of the program, meaning the values of its variables; the commands run **in the order written**, except where **selection** (`if`) and **iteration** (`while`, `for`) send control elsewhere; and named blocks, **procedures** and **functions**, let a sequence be written once and called many times, with **parameters** carrying values in and a return value carrying one out. The syllabus takes all of this as known from the AS course and [[Program Design]]; what it asks at A2 is that you recognise it and contrast it.

The four-ways script's procedural solution is the shape everyone knows:

```python
total = 0
for name, price in ITEMS:
    if price < 6:
        total = total + price
```

Three commands, run in order, and one variable whose value is the whole state of the computation. That last sentence is the paradigm's characteristic and its weakness at once: state is easy to follow in four lines and hard to follow in four thousand, where any procedure can change any variable it can see. Object-oriented and declarative programming are both, in different ways, attempts to control that.

The mark scheme's phrases: **uses variables**, **changed by assignment statements**, relies on **iteration**, statements are **a sequence of commands** performed **in the order given**, **each line changes something** in the program's run.

---

## Part IV — Object-oriented: data and behaviour, bundled

[[Object-Oriented Programming]] carries the full treatment, in real Python, of every term the syllabus lists, and this card only places the paradigm beside the others. The move is to stop passing data to procedures and instead give the data its own procedures. An **object** holds attributes and the methods that act on them; a **class** is the template; **encapsulation** keeps the attributes private so that only the class's own methods can change them, which is the first real control on the procedural paradigm's free-for-all state.

The four-ways script's version:

```python
class Item:
    def __init__(self, name, price): self.__name = name; self.__price = price
    def get_price(self): return self.__price
    def is_cheap(self, limit=6): return self.__price < limit

class Stock:
    def __init__(self): self.__items = []
    def add(self, item): self.__items.append(item)
    def total_cheap(self): return sum(i.get_price() for i in self.__items if i.is_cheap())
```

An `Item` knows its own price and whether it is cheap; a `Stock` **contains** items and can total the cheap ones; nothing outside either class touches `__price`. The loop is still there, inside `total_cheap`, because object-oriented code is imperative code organised around objects: the paradigm changes *where* the how lives, not whether you write it. What it buys is that a change to what "cheap" means is made in one place, and that a `Stock` of `Item`s can be handed a `DiscountedItem` subclass without knowing, which is **polymorphism**.

The mark scheme's phrases: programs using the concepts of **class, object, inheritance, encapsulation and polymorphism**; data and methods **bundled**; objects as **instances** of classes.

---

## Part V — Declarative: facts, rules, and a goal the engine satisfies

This is the paradigm the A2 syllabus is really adding, and the one the exam tests with code you must write. A declarative program does not say how to compute anything. It states **facts**, states **rules** that derive new facts from old, and then asks a **goal**; the language's engine searches for every way the goal can be satisfied and reports them. In Prolog, the logic language the papers use:

```prolog
parent(tom, bob).                                   % facts: things that are true
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).    % a rule: X is a grandparent of Z if ...
?- grandparent(tom, Who).                           % a goal: for which Who is this true?
```

Read the rule as *grandparent(X, Z) is true IF parent(X, Y) is true AND parent(Y, Z) is true.* Names beginning with a capital letter are **variables**; the engine finds values for them. The comma is AND; a full stop ends every clause; `:-` is "if" (the exam papers write it as `IF` and the comma as `AND`, and accept either).

**How the engine answers.** It has no loop written by you, so it brings its own: depth-first search with backtracking.

![[paradigms-prolog-tree.svg|700]]

To satisfy `grandparent(tom, Who)` it finds the rule whose head matches, binding `X = tom` and `Z = Who`, and replaces the goal with the rule's body: two new goals, `parent(tom, Y)` and `parent(Y, Who)`. It takes the first, scans the facts in order, and the first match is `parent(tom, bob)`, so `Y = bob`. Now the second goal is `parent(bob, Who)`, the first match is `parent(bob, ann)`, and the first answer is `Who = ann`. Asked for more, it **backtracks**: undoes the last choice and tries the next fact, `parent(bob, pat)`, giving `Who = pat`. Backtracking further, it undoes `Y = bob` and tries `Y = liz`; `parent(liz, Who)` matches nothing, the branch dies, and there are no choices left. Two answers, in that order, and the order is the order of the facts, which is why exam questions ask for the *result* of a goal and expect the facts read top to bottom.

There is no Prolog on most school machines, so the card supplies one: `paradigms-prolog.py` is a hundred and twenty lines of Python that do exactly the search above, with unification, backtracking, negation as failure and the comparisons the questions need. Every worked example below was run on it. The family question gives `Who = ann` then `Who = pat`; `ancestor`, written with a base case and a recursive case, finds `tom` an ancestor of `jim` through two rule applications; and `father(liz, Who)` returns `false`, because no fact makes it true.

**Two facts about the paradigm worth saying in the exam's words.** A declarative program **instructs the computer what needs to be done rather than how**, **using facts and rules**, with **queries that satisfy goals**; it can be **logical** (relations, as here) or **functional** (built by applying functions to arguments, in a mathematical style). And [[SQL]] is the declarative language every student already speaks: `SELECT SUM(price) FROM item WHERE price < 6` names the result and never the loop, and the four-ways script gets its 8 from that line as easily as from Prolog's `cheap(N, P) :- item(N, P), P < 6.`

---

## Where it is the working tool

- **Every SQL query ever run.** Declarative programming is not exotic; it is the paradigm behind every database in the world. The optimiser chooses the how, which is why the same query runs on a laptop and on a thousand machines.
- **Rules engines and configuration.** Tax rules, insurance eligibility, firewall policies, build systems (`make` is a declarative program: targets, dependencies, and the engine works out what to rebuild), spreadsheets (a cell formula states a relationship; the sheet decides the order of recalculation).
- **The GPU driver and the kernel.** The low-level paradigm is where the machine cannot be pretended away: interrupt handlers, boot loaders, the innermost loops of codecs and cryptography, where the addressing mode chosen changes the clock cycles.
- **The frameworks in every phone app.** iOS, Android and the web's document object model are object-oriented from the ground up: a button *is* an object with attributes and methods, inheriting from a view, contained in a screen.
- **Modern languages are all of them at once.** Python is procedural, object-oriented and functional in the same file; Rust puts a low-level paradigm and a high-level type system in one language; the fastest code today is often a declarative description compiled to a low-level kernel, which is exactly what a machine-learning framework does when it turns a network description into GPU instructions ([[Artificial Intelligence]]).

---

## Worked examples — every tool named

### Example 1 — describe the two ends (Cambridge 9618, June 2021 Paper 31, Q9(a)–(b))

*(a) Describe what is meant by an imperative (procedural) programming language.* — *Tool: Part III's marking phrases.* Programs are a **sequence of commands** performed **in the order written**; they use **variables** changed by **assignment**; they rely on **iteration**; each line changes the program's state. *(Two marks from six points. The report: some candidates described declarative languages here, and vice versa. Decide which end of Part I's figure you are at before writing.)*

*(b) Describe what is meant by a declarative programming language.* — Tells the computer **what** is to be done rather than **how**; **facts and rules**; **queries that satisfy goals**; may be logical (a set of relations) or functional (applying functions to arguments). *(Two marks from six.)*

### Example 2 — name the paradigm of the code (Cambridge 9618, June 2021 Paper 31, Q9(c))

Four code samples: `male(john). female(ethel). parent(john, ethel).`; `FOR Counter = 1 TO 20 / X = X * Counter / NEXT Counter`; `Start: LDD Counter / INC ACC / STO Counter`; `public class Vehicle { private speed; public Vehicle() { speed = 0; } }`. — *Tool: the tells.* Facts with full stops → **declarative**. A loop assigning to a variable → **procedural / imperative**. Mnemonics and an accumulator → **low-level / assembly**. `class` and `private` → **object-oriented**. *(Four marks. The report: a few "described what the code was doing rather than stating the paradigm". Name it; do not narrate it.)*

### Example 3 — the matching table (Cambridge 9618, November 2021 Paper 31, Q2)

Match each paradigm to its description. — Declarative: *programs that specify the desired result rather than how to get to it.* Imperative: *programs with an explicit sequence of commands that update the program state, with or without procedure calls.* Low-level: *programs using the instruction set of a processor.* Object-oriented: *programs using the concepts of class, inheritance, encapsulation and polymorphism.* The distractor, *programs based on events such as user actions or sensor outputs*, is event-driven programming, a paradigm the syllabus does not list. *(Four marks.)*

### Example 4 — write the facts, read the goal, write the rule (Cambridge 9618, June 2024 Paper 32, Q10)

Facts about clients, activities, choices and what each client has already done. *(a) Jane is a client who would like to choose surfing and has already done sailing. Write the additional clauses.* — *Tool: one fact per relationship, in the knowledge base's own predicates:*

```prolog
client(jane).
activity(surfing).
choice(jane, surfing).
done(jane, sailing).
```

*(Four marks, one per clause. `surfing` was not yet an activity, so it needs its own fact; forgetting it is the common dropped mark.)* *(b) `choice(List, rowing)` returns `List = petra, eliza`. Write the result of `choice(List, sailing)`.* — Read the facts top to bottom for every `choice(_, sailing)`: `frankie, erik, henry`. *(One mark, order as in the facts.)* *(c) C may choose A if A is an activity and C has not already done A. Write this as a rule.* —

```prolog
may_choose_activity(C, A) IF client(C) AND activity(A) AND NOT done(C, A).
```

*(Four marks: `client(C)`, `activity(A)`, `done(C, A)`, and all operators and punctuation correct with no extra terms. The scheme accepts `,` for AND and, in the 2026 paper, `\+` for NOT as SWI-Prolog writes it. Run on the card's engine, the rule returns every client–activity pair not yet done, which is what it should.)*

### Example 5 — the same shape, a year earlier (Cambridge 9618, November 2023 Paper 31, Q11)

Students, subjects, `choice1` and `choice2`. *(a) Anthony is a student who would like history and geography.* — `student(anthony).` `choice1(anthony, history).` `choice2(anthony, geography).` *(Three marks.)* *(b) `choice1(X, mathematics)` returns:* `tomaz, pietre, nico`, the facts' order. *(c) N may choose S if N is a student and S is a subject and N has not chosen S as first choice:*

```prolog
may_choose_subject(N, S) IF student(N) AND subject(S) AND NOT choice1(N, S).
```

*(Four marks; the scheme's second example answer puts `NOT choice1(N, S)` first, so the order of the conditions is free, which is itself a lesson about the paradigm: the engine, not you, decides the order.)*

### Example 6 — facts with three predicates, and a goal with two (Cambridge 9618, June 2022 Paper 31, Q2)

Facts `type(cat, kind)`, `hair(cat, length)`, `spots(cat, yes/no)`. *(a) A caracal is a wild cat with short hair.* — `type(caracal, wild).` `hair(caracal, short).` *(Two.)* *(b) `hair(Cat, long)` returns:* `persian`. *(c)(i) A goal, using `Pet`, to find all domestic cats:* `type(Pet, domestic).` *(ii) A goal, using `WildSpotty`, for all wild cats with spots:* `spots(WildSpotty, yes), type(WildSpotty, wild).` *(Two marks: both conditions on the same variable, joined by AND. Run on the engine: leopard and cheetah, not the savannah, which is a hybrid.)*

### Example 7 — the 2026 rule, with NOT (Cambridge 9618, June 2026 Paper 31, Q11)

Devices, customers, `owns(device, customer)`, `wants(device, customer)`. *(a) Betty is a customer who owns a large TV and wants a Blu-ray player.* — `customer(betty).` `owns(large_tv, betty).` `wants(bluray_player, betty).` *(Three, and the scheme insists the device names match the given facts, `large_tv` and `bluray_player`, exactly.)* *(b) `owns(projector, Owner)` returns:* `petrov, susan, sammy`. *(c) D may be bought by A if D is a device and A is a customer and A does not own D:*

```prolog
may_buy_device(D, A) IF device(D) AND customer(A) AND NOT owns(D, A).
```

*(Four marks. Note the argument order in `owns` is device first, customer second, as the facts have it; reversing it is the trap.)*

---

## Hands-on

- **`paradigms-prolog.py`** — the engine: facts, rules, variables, conjunction, negation as failure, comparisons, and depth-first search with backtracking, in 120 lines you can read. It runs the family and shop examples; add the exam's clauses and ask its goals.
- **`paradigms-four-ways.py`** — one problem in all four paradigms (and functional as a fifth), including a register machine that executes the low-level version with all five addressing modes. Change the limit from 6 to 10 and watch all five programs agree again; change the low-level program's `(12)` to `12` and see the indirect read become a direct one, and the answer go wrong.
- **`paradigms-figures.py`**, **`paradigms-manim.py`** — the figures, and the two films: the engine answering a goal, and the machine stepping through its loop.
- **Write the exam's rule and run it.** Take Example 4's facts, put them into the engine (`kb.fact("client", "stevie")` and so on), add the rule as `kb.rule(("may_choose_activity", "C", "A"), ("client", "C"), ("activity", "A"), ("not", ("done", "C", "A")))`, and query it. Every pair it prints is a mark you would have got.

---

## Common Misconceptions (Teaching Notes)

### 1. "A paradigm is a language"
It is a way of thinking that a language supports. Python supports three; the exam names the paradigm of a *code sample*, and one language can supply samples in several. Look for the tell, not the language name.

### 2. "Describe what the code does"
The June 2021 report's complaint. Asked for the paradigm, candidates explained the algorithm. `FOR Counter = 1 TO 20 / X = X * Counter` is not "calculates a factorial"; it is *procedural*.

### 3. "Declarative means the order does not matter at all"
The order of conditions in a rule is free, and the scheme accepts any. But the order of the *facts* fixes the order of the *answers*, which the "write the result returned by the goal" questions test every year: read top to bottom.

### 4. "A rule needs an IF for every condition"
One `IF`, then the conditions joined by AND (or commas). Extra terms, missing full stops, and a condition on a variable that appears nowhere else all cost the operators-and-punctuation mark.

### 5. "Indirect addressing reads the cell named in the operand"
That is direct. Indirect reads the cell *whose address is stored in* the cell named. `SUB (12)` with cell 12 holding 13 subtracts the contents of cell 13.

### 6. "Object-oriented code has no loops"
It has the same loops, inside methods. The paradigm changes where the *how* lives and who is allowed to touch the state, not whether the how exists.

---

## Exam Notes

### Cambridge 9618 (§20.1 Programming Paradigms — Paper 3, with Paper 4 for the OOP code)

The outcome: understand what a paradigm is, and the characteristics of four. **Low-level**: write code using the five addressing modes (immediate, direct, indirect, indexed, relative), on top of the AS assembly material in [[Assembly Language]]. **Imperative (procedural)**: assumed from §11.3, variables, constructs, procedures and functions. **Object-oriented**: the terminology (objects, properties/attributes, methods, classes, inheritance, polymorphism, containment/aggregation, encapsulation, getters, setters, instances), designing classes for a problem, and writing OOP code, all in [[Object-Oriented Programming]] and examined as code in Paper 4. **Declarative**: write facts and rules from supplied information, and write goals that facts and rules can satisfy. Paper 3 sets the declarative question nearly every series, in the six-to-nine-mark shape of Examples 4–7: add clauses (one mark each), read the result of a goal (one), write a rule with three conditions and NOT (four). It sets the describe-and-identify shapes of Examples 1–3 less often. The examiners' two standing notes: answers "must use correct declarative language syntax", and "candidates need to have practical experience of programming", which is what the card's engine is for. With this card the 9618 topic map has no red and no yellow rows.

### Where it is *not* examined

- **Cambridge 0478** has no paradigms and no declarative programming; its programming is procedural throughout.
- **IB Computer Science** teaches OOP (B3) and procedural programming but does not name paradigms as a topic or examine a logic language; **AP Computer Science A** is Java, object-oriented only.

---

## Connections

- **Builds on:** [[Assembly Language]] — the low-level paradigm and the AS addressing modes this card extends to five; [[Object-Oriented Programming]] — the OOP paradigm in full; [[SQL]] — the declarative language everyone already uses; [[Program Design]] — the procedural constructs assumed from AS.
- **Extends into:** [[Compilers and Interpreters]] — every paradigm is a pretence that a translator or an engine pays for; [[Recursion]] — the declarative `ancestor` rule with its base case and recursive case is recursion without a loop anywhere.
- **Bridges:** [[Artificial Intelligence]] — expert systems are declarative programs (facts, rules, an inference engine), and the card's forward-chaining engine there is this card's backtracking engine run the other way; [[Graphs]] — the engine's search is a depth-first traversal of a tree of goals.

---

## Beyond Syllabus

### Functional programming
The syllabus mentions it in passing as the other declarative family. A functional program is built by applying functions to values and composing them, with no assignment and no state: the four-ways script's fifth solution, `reduce(add, map(price, filter(cheap, items)))`, never changes a variable. Haskell, OCaml and Elixir are functional languages; Python, JavaScript and Java have absorbed the ideas (`map`, `filter`, lambdas, immutability). Its virtue is that a function with no state can be run in any order, on any core, and tested in isolation.

### Event-driven, and the others
The distractor in Example 3 is real: event-driven programs (every GUI, every web page) wait for events and run handlers. Logic, functional, event-driven, concurrent, dataflow: the list of paradigms is long, and most languages now mix several. The four the syllabus names are the four axes that the rest are combinations of.

### Why Prolog searches the way it does
Depth-first, left to right, facts in order: the engine is a fixed strategy for a search that could be done in other orders. That fixed strategy is what makes a Prolog program *predictable* (the exam's "result returned" questions depend on it) and also what can make it loop forever: write the `ancestor` rule **left-recursively**, `ancestor(X, Y) :- ancestor(X, Z), parent(Z, Y).`, and the engine calls `ancestor` again before any variable is grounded, forever; the card's engine hits Python's recursion limit on it in under a second, while the right-recursive form `parent(X, Z), ancestor(Z, Y)` finds all five descendants of tom in any clause order. Declarative in intent, but the engine's how still leaks through.

### Unification
The heart of the engine is `unify`, twenty lines in `paradigms-prolog.py`: make two terms equal by binding variables, or report that it cannot be done. The same algorithm type-checks a Haskell program and resolves generic types in Java. A logic language is unification plus search.

---

## LaTeX Reference

| Rendered | Source | Meaning |
|---|---|---|
| $\text{head} \leftarrow \text{body}_1 \land \text{body}_2$ | `\text{head} \leftarrow \text{body}_1 \land \text{body}_2` | a rule: head if body (Prolog's `:-`) |
| $\neg\,p$ | `\neg\,p` | negation as failure (`NOT`, `\+`) |
| $\text{addr}(\text{operand})$ | `\text{addr}(\text{operand})` | direct addressing reads the cell named |
| $\text{mem}[\text{mem}[n]]$ | `\text{mem}[\text{mem}[n]]` | indirect addressing |
| $\text{mem}[n + \text{IX}]$ | `\text{mem}[n + \text{IX}]` | indexed addressing |

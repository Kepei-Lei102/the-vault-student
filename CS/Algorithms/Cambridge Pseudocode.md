---
chinese: 剑桥伪代码 (Jiànqiáo wěidàimǎ)
prerequisites:
  - "[[Program Design]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/algorithms
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/9618-10-1
  - syllabus/9618-10-3
  - syllabus/9618-11-1
  - syllabus/9618-11-2
  - syllabus/9618-11-3
  - type/reference
  - type/deep
  - misconception/pseudocode-is-a-real-language
  - misconception/must-memorise-the-string-functions
  - misconception/pseudocode-is-informal
  - misconception/the-guide-is-the-function-list
---

# Cambridge Pseudocode 剑桥伪代码

> *A language you cannot execute is a language you cannot check, which is why runnable code beats a dialect almost everywhere. Here is the exception, and it is worth being straight about why it earns one. Cambridge pseudocode is a **consistent hybrid of program code and structured English** — and the whole of its value is in that one word, **consistent**. It is not more readable than Python. It is not more precise than Java. It exists so that a marker in one country reads a script from another and arrives at exactly the same meaning the candidate intended. That is a real problem, honestly solved. It is also the only problem this dialect solves.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| pseudocode | 伪代码 | code-shaped writing not meant for a compiler |
| dialect | 方言 | one board's fixed, published version of it |
| keyword | 关键字 | a reserved word, always UPPER CASE here |
| identifier | 标识符 | a name you choose, always MixedCase here |
| declaration | 声明 | stating a name and its type before use |
| assignment | 赋值 | `←`, not `=` |
| meta-variable | 元变量 | `<something>` — a slot for you to fill in |
| by value / by reference | 传值 / 传引用 | the callee gets a copy / gets the original |
| Backus–Naur Form | 巴科斯范式 | the `< >` notation the guide borrows to state its own grammar |

## Where it sits — between two things you already have

[[Program Design]] left a solution written two ways: structured English, which anyone can read but nobody can execute, and Python, which executes but commits you to one language. Pseudocode is the deliberate middle:

| | Structured English | **Cambridge pseudocode** | A real language |
|---|---|---|---|
| Who can read it | anyone | anyone who learned the dialect | programmers of that language |
| Precision | loose — two readers can disagree | **exact by decree** | exact by execution |
| Can you run it? | no | **no** | yes |
| Tied to a language? | no | no | yes |
| Why it exists | to be checked by the person who asked | **to be marked identically everywhere** | to run |

Read the middle column downwards and the design becomes obvious. Cambridge must set one paper for candidates who learned Python, Java, VB.NET or Pascal, and must mark it identically in every centre on earth. It cannot use a real language without privileging the students who happened to learn it. It cannot use loose English without arguments about what a script meant. So it invents a dialect with the *grammar* of code and the *vocabulary* of English, freezes it in a published guide, and marks against that.

That is a genuine problem and this is a reasonable answer to it. Worth saying plainly, because everything below is about the costs.

> [!warning] A language with no implementation
> Cambridge pseudocode has keywords, data types, declarations, scope rules, parameter-passing modes and a published grammar. It has everything a programming language has **except a compiler**. Nothing anywhere will ever run it.
>
> That single fact causes most of the difficulty students have with it. In Python, a misunderstanding produces an error message within seconds and you fix it. Here there is no oracle at all — no interpreter to contradict you, no test to fail. The only thing that can tell you your pseudocode is wrong is a human being reading it, and in an exam that human is marking it. You therefore have to be **more** careful than you would in a real language, not less, which is the exact opposite of what "pseudo" sounds like it should mean.
>
> The practical defence, and it is the one professionals use: **write it in Python first, run it, then transcribe.** The thinking gets checked by a machine; only the spelling is done by hand.

## The grammar, in one pass

Everything below is from the published guide for 2027–29. Keywords are **UPPER CASE**; identifiers are **MixedCase**; indentation is three spaces; comments start with `//`; and `<angle brackets>` mark a slot you fill in, a convention the guide borrows from the grammar notation **BNF** ([[Compilers and Interpreters]] covers it).

**Declaring and assigning.** Assignment is `←`, never `=`. `=` is comparison only.

```
DECLARE Counter : INTEGER
DECLARE TotalToPay : REAL
CONSTANT VAT = 0.2

Counter ← 0
TotalToPay ← 15.75
```

**The six data types** are `INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN`, `DATE`. Note what that list is: `CHAR` is single-quoted (`'x'`), `STRING` double-quoted (`"hello"`), and a `REAL` must always be written with a digit on each side of the point — `4.0`, not `4.`.

**Input and output.**

```
INPUT Name
OUTPUT "Hello, ", Name
```

**Selection.** Both forms close explicitly — this dialect never lets indentation alone end a block.

```
IF Score > Best THEN
   OUTPUT "New record"
ELSE
   OUTPUT "Try again"
ENDIF

CASE OF Grade
   'A' : OUTPUT "Excellent"
   'B' TO 'D' : OUTPUT "Pass"
   OTHERWISE : OUTPUT "See me"
ENDCASE
```

`CASE` clauses are tested **in order**, the first match wins and the rest are skipped, and `OTHERWISE` — if present — must come last.

**Iteration.** Three loops, and the count-controlled one closes with `NEXT`, not `ENDFOR`:

```
FOR Index ← 1 TO 30
   OUTPUT StudentNames[Index]
NEXT Index

WHILE Inserted < Price
   INPUT Coin
   Inserted ← Inserted + Coin
ENDWHILE

REPEAT
   INPUT Answer
UNTIL Answer = "yes"
```

**Which loop, and why** — the syllabus asks you to *justify* the choice, and the rule is short. Use **`FOR`** when the number of repetitions is known before the loop starts (every element of a 30-element array). Use **`WHILE`** when it might need to run **zero** times, because the condition is tested *before* the first pass — reading a file that may be empty, or a total that may already be large enough. Use **`REPEAT`** when it must run **at least once**, because the condition is tested *after* — asking for input you have not received yet, since you cannot validate an answer before you have one. The whole distinction is *when the test happens*, and a justification that says so scores; one that says "it is easier" does not.

**Arrays** are fixed length, and you declare the bounds explicitly — both of them:

```
DECLARE StudentNames : ARRAY[1:30] OF STRING
DECLARE Board : ARRAY[1:3, 1:3] OF CHAR
```

Stating the lower bound is not decoration. Different real languages start at 0 or 1, so the declaration is where you settle it, and `ARRAY[1:30]` holds thirty elements indexed 1 to 30 — not 31, and not 0 to 29.

**Records** are the one composite type you define yourself, and the syntax is a block, not a one-liner. `TYPE` names the new type, each field is `DECLARE`d inside it, and `ENDTYPE` closes it — after which the type name is usable exactly where a built-in type would be, including as an array's element type:

```
TYPE Component
   DECLARE Item_ID : STRING
   DECLARE Reject  : BOOLEAN
   DECLARE Weight  : REAL
ENDTYPE

DECLARE ThisPart : Component
DECLARE Batch : ARRAY[1:1000] OF Component
```

Fields are reached with a **dot**, and that is the whole of the notation — there is no separate syntax for reading a record and writing one:

```
ThisPart.Weight  19.6
Batch[7].Reject  TRUE
OUTPUT Batch[7].Item_ID
```

Two things are worth noticing, because both are marked. The **array-of-records** shape above is the standard A-Level scenario — a `TYPE` declaration, then an array of a thousand of them, then modules that search or update it — so the two indexing styles compose: `Batch[7]` picks the record with a number computed at run time, `.Reject` picks the field with a name fixed when the program was written ([[Arrays]] argues why those are different in kind). And a record is **assignable whole**: `Batch[8]  Batch[7]` copies every field, which is a genuine difference from an array, where the same statement would copy a reference.


**Procedures and functions.** The distinction is enforced by the syntax: a procedure is `CALL`ed and returns nothing, a function is used inside an expression and must declare what it `RETURNS`.

```
PROCEDURE ShowTotal(Amount : REAL)
   OUTPUT "You owe ", Amount
ENDPROCEDURE

CALL ShowTotal(15.75)

FUNCTION Area(Width : REAL, Height : REAL) RETURNS REAL
   RETURN Width * Height
ENDFUNCTION

Total ← Area(3.0, 4.0)
```

**Which of the two, and where** — a **function** is appropriate when the sub-task's whole point is to *produce a value* that the caller then uses, because a function call can stand inside an expression: `Total ← Area(3.0, 4.0) * Quantity` works, and the return value simply replaces the call. A **procedure** is appropriate when the sub-task's point is to *do* something — display a report, write a file, swap two values — and there is no single answer to hand back. If you find yourself writing a procedure whose last act is to store one result somewhere the caller will read, you wanted a function.

**Parameter passing** is explicit, which most real languages hide: `BYREF` means the callee gets the original and changes stick; the default is by value, where it gets a copy.

```
PROCEDURE Swap(BYREF X : INTEGER, BYREF Y : INTEGER)
```

**Files** use four commands, and a file is named by a string rather than declared as a variable:

```
OPENFILE "Data.txt" FOR READ
READFILE "Data.txt", LineOfText
CLOSEFILE "Data.txt"
```

The modes are `READ`, `WRITE` and `APPEND`, and `EOF("Data.txt")` tests for the end of file.

## The functions you are given — and why the guide is not the list

This is where candidates waste the most revision time, and where the honest answer is more useful than the tidy one.

The **guide** lists a small set: `LENGTH`, `RIGHT`, `MID`, `LCASE`, `UCASE`, `INT`, `RAND`, and `&` for concatenation. If you stop there you will conclude, reasonably, that there is no `LEFT` and that you must loop to upper-case a word.

**Both of those conclusions are wrong in the exam**, because the guide is not the operative document. Every Paper 2 and Paper 3 arrives with an **insert** that reprints the functions you may use, and that insert is longer than the guide, is what the mark scheme assumes, and **changes between series**. Checked across every 9618 insert from June 2021 to November 2025:

| | in the guide | in the inserts |
|---|---|---|
| `LEFT(s, x)` | **absent** | **present in all thirty** — June 2021 through November 2025 |
| `TO_UPPER(x)` / `TO_LOWER(x)` | absent | present throughout, and they take **`CHAR` *or* `STRING`** |
| `LCASE(c)` / `UCASE(c)` | present, `CHAR` only | present to Nov 2022, **dropped from June 2023 onwards** |
| `NOW()` | absent | June 2021 only |
| `TODAY()` | absent | from June 2022 onwards |
| `NUM_TO_STR`, `STR_TO_NUM`, `IS_NUM`, `ASC`, `CHR`, `DAY`, `MONTH`, `YEAR`, `DAYINDEX`, `SETDATE`, `EOF` | absent | present throughout |

Read that table as the single most practical thing on this page. **`LEFT` exists** — it has been on every insert for five years, and `LEFT("ABCDEFGH", 3)` returns `"ABC"`. You do not need `MID(s, 1, n)` for it, though that still works. And you do **not** loop to change case: `TO_UPPER("Error 803")` returns `"ERROR 803"` in one call, because unlike the guide's `LCASE`/`UCASE` it accepts a whole string.

Note also what the drift shows. The guide still lists `LCASE` and `UCASE`; the papers stopped providing them after November 2022. **The guide is behind the papers** — shorter in one direction, stale in another — which is not a criticism of anyone so much as the predictable state of two documents maintained on different clocks.

> [!tip] The line that should change how you revise
> The guide says string manipulation functions **will always be provided in examinations**, and syllabus §11.1 adds that **any function not in the guide will be provided**. Between them, and given that the provided set has visibly changed across series, the conclusion is not "memorise this list." It is:
>
> **Read the insert first, and treat it as the specification for that paper.** Two minutes at the start, before any question, learning what you have been handed. Anything you half-remember from a textbook is a guess; the insert is a fact, and it is sitting on the desk.
>
> The examinable skill is reading an unfamiliar signature and using it correctly — `MID(ThisString : STRING, x : INTEGER, y : INTEGER) RETURNS STRING` tells you everything without any memory at all. That skill survives every revision of the list.
>
> **All of the above is A-Level only.** 0478 issues **no insert** — checked across the whole IGCSE paper archive, there is not one. So at IGCSE the pseudocode section printed in the syllabus *is* the specification, in full, with nothing arriving on the day to extend or override it. Which reverses the advice exactly: **at A-Level, read the insert; at IGCSE, learn the syllabus section, because that is all there will ever be.**

## Three gaps in the specification itself

The guide and the syllabus are separate documents and they do not entirely agree — and, as the function tables above show, the *insert* is a third document that agrees with neither. These are not exam tricks. They are places where the specification is genuinely incomplete, and knowing that is more useful than being confused by it later.

**1. The syllabus names a `FILE` data type that the guide never defines.** Syllabus §10.1 lists the types pseudocode uses as *"INTEGER, REAL, CHAR, STRING, BOOLEAN, DATE, ARRAY, FILE"*. The guide's own data-type section (§2.1) lists six, and `FILE` is not among them. In practice files are handled by *commands* — `OPENFILE`, `READFILE`, `WRITEFILE`, `CLOSEFILE` — that take a **string filename**, and nothing is ever declared `: FILE`. Write it the way the guide and the papers both actually use it, and do not go looking for a declaration form that was never specified.

**2. There is no exception-handling syntax at all.** Search the guide for `TRY`, `CATCH`, `THROW` or *exception* and you find nothing. Yet syllabus §20.2 requires candidates to *write code* for exception handling. The resolution is that §20.2 is a **programming-language-side objective**: you meet it in Python, Java or VB.NET, not in pseudocode. The same is true of the polymorphism and containment objectives in §20.1 — the dialect simply has no way to express them.

**3. Object-oriented syntax exists but arrives late and thin.** The guide has a section for it, and it is by far its least developed part — another sign that the dialect was designed for structured, procedural programming and had OOP added afterwards, which is exactly the historical shape [[Program Design]] describes.

## Python ↔ pseudocode, side by side

The translation is mechanical, which is the point — if it were not mechanical, the dialect would be failing at its one job. Write and run the left column, transcribe the right.

| Python (runs) | Cambridge pseudocode (does not) |
|---|---|
| `count = 0` | `Counter ← 0` |
| `if a == b:` | `IF A = B THEN` |
| *(dedent ends the block)* | `ENDIF` |
| `elif` | *(no equivalent — nest another `IF`, or use `CASE`)* |
| `while x < 10:` | `WHILE X < 10` … `ENDWHILE` |
| `for i in range(1, 31):` | `FOR i ← 1 TO 30` … `NEXT i` |
| `def area(w, h):` | `FUNCTION Area(W : REAL, H : REAL) RETURNS REAL` |
| `return w * h` | `RETURN W * H` |
| `print("hi", name)` | `OUTPUT "hi", Name` |
| `name = input()` | `INPUT Name` |
| `names[0]` *(first element)* | `Names[1]` *(if declared `ARRAY[1:30]`)* |
| `word[:3]` | `LEFT(Word, 3)` *(on every insert; `MID(Word, 1, 3)` also works)* |
| `word.upper()` | `TO_UPPER(Word)` *(insert function — takes a whole `STRING`)* |
| `a and b`, `a or b`, `not a` | `A AND B`, `A OR B`, `NOT A` |
| `!=` | `<>` |
| `#` comment | `// comment` |

Four differences do most of the damage in real scripts:

- **`←` for assignment, `=` for comparison.** Python's `=` versus `==` distinction exists here too; only the symbols moved.
- **Blocks close explicitly.** `ENDIF`, `ENDWHILE`, `NEXT`, `ENDPROCEDURE`, `ENDFUNCTION`, `ENDCASE`. Indentation is for readers, not for the grammar — a missing `ENDIF` is a real error here in a way a missing dedent never is in Python.
- **Arrays usually start at 1.** Every off-by-one you have trained out of yourself in Python comes back inverted.
- **No `elif`.** Nest, or reach for `CASE OF`.

## What is exam, and what is reality

[[Program Design]] had to admit that most of its notations are dead in professional work. This card's admission is shorter and harder: **nobody writes Cambridge pseudocode outside an examination hall. Not once, anywhere, for any purpose.** There is no industry that uses it, no codebase that contains it, no tool that reads it. It has exactly one venue.

That is not a scandal, and the distinction that makes it fine is worth being precise about, because two different things share the word:

- **Lower-case pseudocode is real and universal.** Programmers sketch algorithms on whiteboards, in comments, in design docs and in papers, in a loose half-English that nobody standardises. It has no grammar because it does not need one — the audience is in the room and can ask. This is a genuine professional practice and always will be.
- **Cambridge Pseudocode is a specified dialect with a published grammar**, and its entire purpose is to be *marked*. Consistency is not a nice property of it; consistency is the product. Strip that away and there is no reason to prefer it to Python.

So the honest allocation of belief is: the *activity* of writing code-shaped notes before you write code is real and worth having. The *dialect* is exam furniture. Learn it the way you learn the format of a covering letter — precisely, without mistaking it for a skill.

There is a second-order lesson in the insert drift, and it is the most transferable thing here. A specification that exists in three documents on three maintenance clocks — syllabus, teachers' guide, exam insert — will disagree with itself, and the one that counts is **the one in the room when you are being assessed**. Note that this cuts both ways: at IGCSE there is no insert at all, so the room contains only what you brought, and the syllabus section becomes the thing to know rather than the thing to check. That is not a fact about Cambridge; it is a fact about specifications, and it is why professionals read the version notes before the tutorial.

But "exam furniture" is not the same as "optional". At IGCSE the furniture is the floor: 0478's Paper 2 awards **no marks** for solutions written in a real programming language where it asks for pseudocode. A dialect nobody uses professionally is, for one paper, the only thing that scores. Both facts are true at once, and a student is owed both of them.

**Three things it does teach that survive contact with reality**, and they are not nothing:

- **Declare before you use.** Writing `DECLARE Counter : INTEGER` builds a habit that Python's dynamic typing lets you skip and that every large Python codebase then reintroduces by hand, as type hints. The dialect enforces at pen-and-paper level what serious projects re-adopt voluntarily.
- **Say how a parameter is passed.** `BYREF` versus by value is invisible in most modern languages and bites everybody eventually — the function that mutated the list you passed it. Here it is compulsory to state, which is a better first encounter with the idea than discovering it through a bug.
- **Close your blocks explicitly.** `ENDIF`, `ENDWHILE`, `NEXT`. Python closes blocks by dedent, which is elegant and occasionally catastrophic; every other language in wide use closes them with a brace or a keyword. The habit transfers to more languages than it doesn't.

And the honest verdict on the cost. The dialect asks you to be precise in a notation with **no way to check precision** — no interpreter, no test, no error message, nothing but a marker weeks later. That is a genuinely poor learning loop, and it is the reason to do the thinking in a language that can run and to treat the transcription as the last step rather than the first. **Write it so it runs. Then write it so it marks.**

## Common Misconceptions (Teaching Notes)

### 1. "Pseudocode is informal — I can write it however I like"

That is true of pseudocode as a general idea and **false of this dialect**, which is precisely the confusion. Cambridge publishes a grammar and marks against it. Consistency is the entire product; a script that invents its own keywords has thrown away the only thing the notation was for. **Fix:** two different words, same spelling. Lower-case *pseudocode* is a sketch. Cambridge Pseudocode is a specified dialect with a document behind it.

### 2. "I have to memorise all the built-in functions"

The guide states that string manipulation functions are always provided, and the syllabus adds that any function not in the guide will be given in the question. **Fix:** learn to *read* an unfamiliar function signature — `MID(ThisString : STRING, x : INTEGER, y : INTEGER) RETURNS STRING` tells you everything without memory. Spend the revision time on tracing instead.

### 3. "The pseudocode guide lists the functions I get"

It does not. The guide is a teachers' document; the **insert** stapled to the paper is the specification for that paper, it is longer, and it has changed between series — `LEFT` is on every insert and in no version of the guide, while `LCASE`/`UCASE` are in the guide and were dropped from the papers after November 2022. **Fix:** read the insert before question one. It is a fact on the desk; anything remembered from a textbook is a guess.

### 4. "Pseudocode is easier than real code because it doesn't have to be exact"

Backwards. Real code is checked by a machine in seconds; pseudocode is checked by nobody until a marker reads it. The absence of a compiler makes it *harder* to get right, not easier. **Fix:** treat the missing interpreter as a reason for more care — and where you can, write and run the real thing first, then transcribe.

## Exam Notes

### Cambridge 9618 — where the dialect is actually used

- **Papers 1 and 3 (written)** are where you *read* pseudocode: trace it, find the error, state the output, complete a partially written algorithm. This is the majority of the contact you will have with it, and it is a reading skill.
- **Papers 2 and 4 (practical)** are answered in a **real programming language** — Python, Java or VB.NET — not in pseudocode. Question stems may present an algorithm in pseudocode, but your answer is code that runs.
- So the honest allocation of effort is: **read fluently, write competently, and do neither at the expense of the language you will actually be examined in.**
- The guide is published as *Pseudocode Guide for Teachers*, version 1, for exams in 2027–29. It is a public document; reading its index of keywords once is worth more than any summary.
- **§20.2 exception handling and §20.1's polymorphism and containment are language-side objectives** — the dialect cannot express them, so they are met in your chosen language.
- **Papers 2 and 3 carry an insert** reprinting every function you may use. It is longer than the published guide and it has changed across series — so the first two minutes of the exam belong to reading it, not to question one. Past inserts are the best possible revision material for exactly this, because they show you what *that* year's paper actually assumed.

### Cambridge 0478 IGCSE — a smaller dialect, and a much bigger role

- **This is the reversal, and it matters more than any syntax on this page.** At A-Level, pseudocode is mostly something you *read* and the practical papers are answered in a real language. At IGCSE it is the opposite: in **Paper 2, where the solution to a problem involves coding, candidates are required to write solutions in pseudocode — and solutions written in programming code will not be awarded marks.** The single exception is the 15-mark scenario question, where pseudocode *or* Python, Visual Basic or Java is accepted.
- So an IGCSE candidate who has been practising in Python, and who writes Python in the wrong question, scores zero for otherwise-correct work. Nobody discovers that comfortably in an exam hall. It is the strongest possible argument for treating the dialect as a **writing** skill at IGCSE and a **reading** skill at A-Level, and for knowing which paper you are sitting.
- **And 0478 issues no insert.** Where an A-Level paper hands you a function list on the day, an IGCSE paper hands you nothing — so the pseudocode section printed in the syllabus is the complete and final specification, and it is worth knowing rather than looking up. The two boards therefore want opposite habits: *read what you are given* at A-Level, *know what exists* at IGCSE.
- 0478 publishes **its own pseudocode conventions**, in its own syllabus rather than in the A-Level guide, and they are close but smaller: **five data types** — `INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN` — with **no `DATE`**, no user-defined record types and no object orientation. Its examples pass parameters without a `BYREF` keyword.
- §7.9 treats pseudocode, program code and flowcharts as interchangeable ways of expressing an algorithm; where a question names one, that is the one that earns marks.

### IB Computer Science and AP Computer Science A

- **IB CS** uses its own pseudocode conventions for examination, again close in spirit and different in detail — the same idea (a neutral dialect so no language is privileged), a different vocabulary.
- **AP CSA** does not use pseudocode at all. The exam is Java, and questions are asked in Java. There is nothing here to transfer except the habit of reading a specification carefully.

## Beyond the syllabus

> [!info] Why every board invents its own, and why none of them agree
> Cambridge pseudocode, IB pseudocode, AQA pseudocode, and the pseudocode in every algorithms textbook are all *mutually unintelligible in detail* while being obviously the same idea. That is not carelessness. Each was designed by a different committee solving the identical problem — express an algorithm without privileging a language — and there is no reason two committees would converge on `ENDIF` versus `END IF` versus `fi`. The academic world has the same fracture: Knuth's *The Art of Computer Programming* uses one style, CLRS's *Introduction to Algorithms* another. The lesson worth carrying is that **notation is a local agreement, not a discovery** — which is exactly what [[Program Design]] says about flowchart symbols, and exactly what [[Stories/The Loudness War]] says about LUFS. What matters is that everyone in the room signed the same one.

> [!info] The one real language that made pseudocode nearly redundant
> There is a reason so many textbooks now write their examples in Python: it was designed to be readable, and it landed close enough to pseudocode that the gap almost closed. `for item in items:` needs no translation for a reader who has never seen Python. Some universities have quietly stopped using pseudocode in first courses because running the examples is worth more than language-neutrality — Cambridge cannot follow them, because a board that examined in Python would be examining Python teachers as much as students.

## Connections

- **Builds on:** [[Program Design]] — the notations you think in; this is the dialect you write the result down in for one specific audience. Its structured English is this dialect's nearest relative, and the two together are the whole of the design-to-code path.
- **Where it gets used:** [[Searching]] and [[Sorting]] — the standard algorithms exam stems present in this dialect; [[Stacks and Queues]] and [[Linked List]] — where §19.1's *write an algorithm to* questions expect it.
- **Kindred:** [[Compilers and Interpreters]] — what a real language's grammar is *for*, and the clearest way to see what is missing here: this is a grammar with nothing to parse it. It also carries **BNF**, the `< >` meta-variable notation the guide borrows to describe itself — a grammar describing a grammar.
- **When to reach for which:** think in the notations of [[Program Design]], check the thinking by writing and running real code, and transcribe into this dialect only when the reader is an examiner. It is a delivery format, not a workspace.

## Notation Reference

| Symbol / keyword | Meaning | Python equivalent |
|---|---|---|
| `←` | assignment | `=` |
| `=` | equality test | `==` |
| `<>` | not equal | `!=` |
| `&` | string concatenation | `+` |
| `//` | comment | `#` |
| `<identifier>` | a slot to fill in (meta-variable) | — |
| `DECLARE x : INTEGER` | typed declaration | *(none required)* |
| `CONSTANT` | a value that cannot change | *(convention only)* |
| `ARRAY[1:30] OF STRING` | fixed-length array, bounds stated | `list` |
| `PROCEDURE` / `CALL` | subprogram returning nothing | `def` + statement call |
| `FUNCTION` / `RETURNS` | subprogram returning a value | `def` + `return` |
| `BYREF` | pass by reference | *(mutable objects, implicitly)* |
| `NEXT <identifier>` | closes a `FOR` loop | *(dedent)* |
| `ENDIF` `ENDWHILE` `ENDCASE` | explicit block terminators | *(dedent)* |
| `OTHERWISE` | the default case | `else` |
| `EOF("file.txt")` | end-of-file test | `for line in f` |

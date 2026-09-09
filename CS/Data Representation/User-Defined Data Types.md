---
chinese: 自定义数据类型 (zì dìngyì shùjù lèixíng)
prerequisites:
  - "[[Arrays]]"
  - "[[Cambridge Pseudocode]]"
leads_to:
  - "[[Linked List]]"
  - "[[Object-Oriented Programming]]"
  - "[[Relational Databases]]"
tags:
  - subject/computer-science
  - domain/data-representation
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-13-1
  - type/deep
  - type/definition
  - misconception/enum-values-are-not-strings
  - misconception/phone-numbers-are-not-integers
  - misconception/a-set-is-not-a-list
  - misconception/non-composite-means-no-referenced-type
---

# User-Defined Data Types 自定义数据类型

## Definition

A **data type** is a set of allowed values plus the operations allowed on them — `INTEGER` allows whole numbers and arithmetic; `BOOLEAN` allows two values and logic. Every language ships a small fixed menu of **built-in types**; Cambridge's pseudocode ships exactly six (`INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN`, `DATE`).

A **user-defined data type (UDT)** is a type *you* add to that menu, built for the problem in front of you. Once defined, it is used exactly like a built-in: declared, passed to functions, made into arrays.

The syllabus splits them in two, and the split is a definition worth memorising word-for-word:

- **Non-composite** — a type defined **without referencing another data type**. Two of them: **enumerated** (a fixed, ordered list of named values) and **pointer** (a value that is the *address* of another value).
- **Composite** — a type **built out of other types**, one or more of them, grouped under one identifier. Three named ones: **record** (different types, one identity), **set** (unordered collection, no duplicates), and **class/object** (a record that carries its own operations).

![[udt-taxonomy.svg|720]]

### 中文锚点

**奶茶单。** 你在奶茶店点单，店员打出一张小票——这张小票就是本卡的全部内容。整张小票是一个**记录（record）**：饮品是字符串、甜度是一档、配料是一组勾选——不同类型的数据，钉在同一个身份下面。**甜度是枚举（enumerated）**：三分糖、五分糖、七分糖、全糖——菜单上只有这几档，有顺序、不重复，点不出"六分半糖"。**配料是集合（set）**：珍珠、椰果随便勾，但同一种配料"勾两次"没有意义（加两份是数量，不是集合），而且先勾珍珠还是先勾椰果毫无区别。**取餐号是指针（pointer）**：47 号不是你的奶茶——它只是告诉你**去哪里拿**奶茶；拿着编号换到实物，这个动作就叫"解引用"。语言内置的六种类型说不出"甜度"这个词；自定义类型，就是教会语言**用你要解决的问题的词汇说话**。

| English                | 中文        | 一句话                   |
| ---------------------- | --------- | --------------------- |
| User-defined data type | 自定义数据类型   | 你加进语言菜单里的新类型          |
| Non-composite          | 非复合（类型）   | 定义时不引用其他类型            |
| Composite              | 复合（类型）    | 由其他类型组装而成             |
| Enumerated             | 枚举类型      | 固定、有序、不重复的取值清单        |
| Pointer                | 指针类型      | 存的是地址，不是值本身           |
| Record                 | 记录类型      | 不同类型的字段共用一个身份         |
| Set                    | 集合类型      | 无序、无重复的一组值            |
| Field / dot notation   | 字段 / 点号访问 | `booking.destination` |
| Dereference            | 解引用       | 拿着地址取出实物              |

![[udt-order-slip.svg|760]]

---

## Why the six built-ins are not enough

The two honest reasons, in the order that matters:

**1. The problem has vocabulary the language doesn't.** A program about seasons has a *season-shaped hole* in it. You can jam a season into a `STRING` (`"Summer"`) or an `INTEGER` (`2`), but the type then permits millions of values that are not seasons — `"Sumer"`, `"banana"`, `-40` — and the language will accept every one of them without complaint. A type that says exactly *"one of these four, nothing else"* moves the rule out of your head and into the machine.

**2. Errors move from run time to definition time.** Watch the difference in real Python:

```python
from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

price = {"Summer": 30}
price["Sumer"]        # typo in a string: KeyError at RUN time, if this line ever runs

Season.SUMER          # typo in an enum: AttributeError the moment it is touched,
                      # and any IDE/type-checker flags it BEFORE the program runs
```

A string typo hides until the one customer on the one day hits the one branch containing it. A misspelled enum member cannot even be written down. This principle — design types so that **wrong states cannot be expressed at all** — is one of the deepest ideas in software engineering, and the humble enumerated type is its first appearance.

The design LO ("choose an appropriate UDT for a given problem") is this reasoning run forward: read the data's *shape*, pick the type whose rules match it.

---

## Enumerated: the fixed menu

An **enumerated type** is a list of named values, written out in full at definition. Three properties, each of them a mark on real papers:

1. **Complete** — the list contains *every* possible value; nothing off-menu can exist.
2. **Ordered (ordinal)** — the positions are meaningful, so values compare: spring comes before winter because the definition says so, not alphabetically.
3. **Unique** — no value appears twice.

```python
class Sweetness(Enum):
    NONE = 0
    THIRTY = 30
    FIFTY = 50
    SEVENTY = 70
    FULL = 100

order = Sweetness.FIFTY
order.name                          # 'FIFTY'   — the label
order.value                         # 50        — the number underneath
Sweetness.THIRTY.value < Sweetness.FULL.value   # True — ordering works
```

Note what the type *is* underneath: each named value is just a constant, usually a small integer, wearing a name. The machine stores `2`; the program says `Season.SUMMER`; the compiler forbids `Season.BANANA`. All the safety comes from the name layer.

> [!info] Why Python makes you write the number — and then won't let you compare it
> A Python enum member is a **name–value pair on purpose**: the name is for the program, the value is for the outside world — the database column, the JSON field, the byte on the wire — and `Season(2)` looks a member up by value so data can round-trip. (The value needn't be an integer: `HttpStatus.OK = 200`, or a string.) When you don't care, write `SPRING = auto()`. Then the surprise: a plain `Enum` **refuses** `Season.SPRING < Season.WINTER` with a `TypeError`, because its designers held that members are *names*, and comparing names by their hidden numbers is a bug factory. The syllabus's "ordered" property is opt-in in Python — `IntEnum` — which is the first hint that the exam's taxonomy is one language's opinion. The Beyond section says whose.

> [!tip] When an enumerated type is the right answer
> The question data is a **short, fixed list of named options** — seasons, colours, sizes, weekdays, a taxi fleet's identity codes, menu sweetness levels. The tells: you could read the whole list aloud, the list won't grow at run time, and each value is a *name*, not a measurement.

---

## Pointer: the value that is an address

A **pointer** is a variable whose value is *the location of another value* — the pickup number, not the drink. Two ingredients define one: the **address** it holds, and the **type of thing it points at** (a pointer to an integer is a different type from a pointer to a character — you must know what you'll find when you get there).

Python deliberately has no raw pointers — every Python name is already a *reference* handled for you:

```python
a = [1, 2, 3]
c = a            # c is NOT a copy: both names point at the same list
c.append(4)
a                # [1, 2, 3, 4] — a sees the change, because there is only one list
```

To see the machinery pointers expose, model memory as a numbered row of cells — the same move [[Linked List]] makes with its index-and-free-list implementation:

```python
memory = [None] * 10      # ten numbered cells

memory[7] = 42            # a value lives at address 7
p = 7                     # p is a pointer: its VALUE is an address

memory[p]                 # 42  — following the pointer = "dereferencing"
memory[p] = 43            # writing through the pointer changes cell 7
```

**Where pointers actually live on your paper:** every linked structure. A linked list node is a record of *data + pointer-to-next*; a binary tree node carries two of them. The November 2022 Paper 32 flower question is nothing but this — an array of names, an array of next-pointers, a head pointer of `6`, a null of `0` — and following the chain Dahlia → Daisy → Foxglove → … spells the flowers out in alphabetical order, which is the whole point of the structure: physical order arbitrary, logical order carried by the pointers ([[Linked List]]'s central idea).

> [!tip] When a pointer is the right answer
> Something must **refer to** something else without *being* it: the next node in a chain, the head of a list, a shared object two places both need to see. The tell in exam wording: "stores the address of", "points to", "null".

---

## Record: many types, one identity

A **record** groups fields of *different* types under one identifier — the order slip. It is the composite type you design fresh for every problem, and the A-Level's favourite scenario is an **array of records**: one `TYPE` declaration, then a thousand bookings, then modules that search and update them.

```python
from dataclasses import dataclass, replace
from datetime import date

class Vehicle(Enum):
    M100 = 1; M230 = 2; T101 = 3; T102 = 4; T120 = 5; T150 = 6

@dataclass
class Booking:
    booking_number: str        # "any combination of letters and numbers" -> str!
    destination: str
    client_name: str
    client_telephone: str      # phone "numbers" are NOT numbers -> str!
    date_of_departure: date
    pickup_address: str
    taxi: Vehicle              # a UDT nested inside a UDT

b = Booking("BK042A", "Airport", "Chen Wei", "02887 654321",
            date(2026, 9, 12), "5 Jinli Road", Vehicle.T120)

b.destination                  # dot notation reads a field...
b.taxi = Vehicle.T101          # ...and writes one
b2 = replace(b)                # a record copies WHOLE, every field at once

bookings = [b, b2]             # the array-of-records shape
bookings[0].client_name       # index picks the record, dot picks the field
```

Two structural facts carry marks. **Dot notation is the whole access story** — `Batch[7].Reject` composes an index chosen at run time with a field name fixed at design time ([[Arrays]] §"why those are different in kind"). And **records assign whole** — one statement copies every field, which is a genuine difference from arrays.

---

## Set: membership, and nothing else

A **set** is an unordered collection with no duplicates. It answers exactly one question fast — *"is this in, or out?"* — and refuses the questions a list answers (what's first? what's at index 3? how many copies?).

```python
toppings = {"pearls", "coconut jelly", "pudding"}
toppings.add("pearls")            # already in: silently ignored — sets can't hold two
len(toppings)                     # 3
"pearls" in toppings              # True — membership is THE set operation

vowels = set("AEIOU")
vowels & set("HELLO WORLD")       # {'E', 'O'} — intersection, union |, difference -
```

> [!tip] When a set is the right answer
> The data is a collection where **order is meaningless and repeats are impossible or forbidden** — valid characters, ticked options, students who have submitted, allowed even numbers. The tell: the question only ever asks "is $x$ one of them?"

---

## Class: the record that grew up

A **class** is the fifth named type — composite, like a record, but bundling the *operations* in with the fields: a `Booking` that knows how to cancel itself. The syllabus names it here so the taxonomy is complete, then spends a whole later section on it — the objects, inheritance and polymorphism story is [[Object-Oriented Programming]]'s, along with the Paper 4 code that goes with it. For this row, know its place on the tree: **class/object is a composite user-defined type**.

The pseudocode guide adds one more fact worth quoting: the ADTs — **stack, queue, linked list, dictionary, binary tree — are also defined as composite data types.** Every structure in the Data Structures bay is, formally, a citizen of this card's taxonomy.

---

## Choosing and designing — the examined skill

The design LO is a translation exercise: each phrase in the problem statement *triggers* a type.

| The data is… | Trigger phrase | Type |
|---|---|---|
| a short fixed list of named options | "one of the following", a list you can read aloud | enumerated |
| several different-typed facts about one thing | "holds data about a …", a field table | record |
| a collection, membership only | "no duplicates", "whether $x$ is allowed" | set |
| a reference to data living elsewhere | "points to", "address of", "next" | pointer |
| fields *plus* behaviour | "methods", "each object can…" | class |

**Worked design — the taxi company (9618 June 2025 Paper 31 Q1).** A booking system needs the fleet's identity codes `M100 … T150` and a booking holding number, destination, client name, phone, date, address, taxi.

*Trigger: six named codes, fixed list, readable aloud → enumerated `Vehicle`.* *Trigger: seven different-typed facts about one booking → record, with one field per fact.* Then the field types, where the real marks hide:

- booking number `"BK042A"` — *"any combination of letters and numbers"* → **string**, however number-ish it sounds;
- telephone → **string** again: `02887…` must keep its leading zero, and nobody multiplies phone numbers — if arithmetic on it is nonsense, it is not a number;
- date of departure → the built-in **date** type, not three integers;
- taxi → the **enumerated type just defined** — a UDT nested in a UDT, which is precisely what the question checks you can do.

The November 2025 Paper 33 colour question is the same skeleton with the numeric traps added: wavelength `650` → integer, frequency `4.62` → **real**, "primary colour: Yes" → **boolean**. Read the *example data*, not the field name — the examiners choose the examples to decide the type for you.

*(The exam writes these declarations in Cambridge's pseudocode dialect — `TYPE Vehicle = (…)`, `TYPE Booking … ENDTYPE`. The forms, and the marking fine print on them, live in [[Cambridge Pseudocode]] §"User-defined types".)*

---

## Where this is the working tool

Open any codebase written this decade and this card is everywhere. Every JSON object an API returns — every weather response, every payment confirmation — is a record; every database row is a record with the table as the array. Real enums guard real state machines: the traffic-light controller that can only be `RED | AMBER | GREEN`, the order that is `PLACED | PAID | SHIPPED | DELIVERED` and cannot silently become `"shiped"`. Permissions systems are sets (`{read, write}` — membership checks, no duplicates, order meaningless). And pointers are the load-bearing structure of essentially all system software: the [[Linked List]]s inside your memory allocator, the tree of records your [[File Systems]] directory actually is.

The negative case is just as real: codebases that store everything in strings — *stringly-typed* code, in the trade's own insult — are where a whole class of production bugs lives, because `"Sumer"` compiles and ships. Choosing types well is not exam decoration; it is the profession's primary defence against its own typos.

---

## Misconceptions

### 1. Quotation marks around enumerated values

An enumerated value is a **name**, not a string — writing the declaration list as `("Red", "Orange", …)` is explicitly refused by the published mark schemes ("do not allow quotation marks around data elements"). The whole point of the type is that `Red` is *not* text.

### 2. "Telephone number" and other lying nouns

If arithmetic on it is nonsense, it is not a number: phone numbers (leading zeros die in an integer), booking codes, postcodes, ID numbers → string. The examiners plant one of these in nearly every record question.

### 3. An enumerated type is just strings with extra steps

Backwards. Strings admit every typo ever typed; the enum admits four values and nothing else, and the error surfaces at *definition* time, before the program runs. The safety is the type.

### 4. A set is a list

A list has order, indices and duplicates; a set has none of them. If the answer to "what's the third one?" must exist, it is not a set.

### 5. "Non-composite means it holds only one value"

The definition is about **construction**, not capacity: non-composite = *defined without referencing another data type*. That is the sentence the 3-mark definitional questions want — an enumerated type holds a whole list of values and is still non-composite, because its definition names no other type.

---

## Beyond syllabus

### The billion-dollar mistake

The null pointer — the pointer that points at nothing — was invented by Tony Hoare for ALGOL W in 1965, and he has spent his later career apologising for it, in exactly those words: *"I call it my billion-dollar mistake."* One special value that every pointer type silently admits, meaning every dereference in every program in every ALGOL descendant can explode at run time. It is this card's own moral told at civilisational scale: a type that permits a value it shouldn't will eventually deliver it. Modern languages answer by moving the null into the type system — Rust's `Option`, Kotlin's `String?` — so that "might be nothing" is visible in the declaration and the compiler refuses code that forgets to check. The fix for the billion-dollar mistake was, precisely, a better user-defined type.

### Enums grown up: algebraic data types

Recall that an enumerated value is a name over a constant. Functional languages let each name *carry data of its own* — `Shape = Circle(radius) | Rectangle(width, height)` — making the type a choice between differently-shaped records: an **algebraic data type**, the enum and the record fused. Pattern matching then forces every branch to be handled, which is how the "invalid states unrepresentable" idea reaches its full strength. Python grew a lightweight version of this in `match`/`case`; Rust's error handling is built entirely from it.

### Where this taxonomy comes from — and what the real world does instead

The syllabus's family tree is not a law of nature. It is **Pascal's type system, 1970**, with the keywords uppercased: Pascal writes `type Season = (Spring, Summer, Autumn, Winter);`, `type Letters = set of char;`, `type PInt = ^Integer;`, `type Student = record … end;` — and `var` where the exam writes `DECLARE`. Every form on this card is Wirth's, verbatim. That is worth knowing for the same reason it is worth knowing that Hooke's law is a small-displacement approximation: the vocabulary is real and every one of these types exists in production code, but the *classification* is one language's opinion, and the languages you will actually write in draw the lines elsewhere.

**How the same idea looks across languages:**

| Language | What an enumerated type *is* | Record vs class |
|---|---|---|
| C / C++ | an integer, full stop — names for `0, 1, 2…`, any int casts in (`enum class` scopes the names but it is still an int underneath) | `struct` (value) vs `class` (same thing, default visibility differs) |
| Pascal / Ada / Delphi | a true **ordinal** type — `ord`, `succ`, `pred`, usable as an array index and a set base | `record` vs `class`, both live — the exam's model |
| Java / Kotlin | each member a **singleton object** of a full class, with fields and methods; `ordinal()` gives position | one `class`; Java 16's `record` and Kotlin's `data class` brought the word back for an immutable field bundle |
| Python | a **name–value pair**; not ordered unless `IntEnum` | `class`; `@dataclass` / `NamedTuple` are the record-shaped corner of it |
| Rust / Swift / Haskell | a **sum type** — variants carry data (`Circle(f64)`, `Some(x)`) and are matched exhaustively | `struct` vs `enum` are the two halves of one system, not a hierarchy |
| C# | int-backed, with `[Flags]` for bit-sets — the descendant of Pascal's `set of` | `struct` (value) vs `class` (reference) vs `record` (C# 9) |
| Go / JavaScript | no enum at all — `iota` constants, or plain strings | `struct` / object literals |

**What actually survives of the exam's distinctions:**

- **Record vs class** collapses into one construct nearly everywhere — but the thing Pascal was pointing at survives as **value versus reference semantics**: does assignment *copy* the fields or *share* them? The card's "a record assigns whole" is the value half of that question, and it is the question C#'s `struct`/`class` split, Go's structs and Rust's ownership rules are all answering.
- **Enumerated vs record** are not opposite categories; in type theory they are the two halves of one idea — a record is a **product type** ("this AND that"), an enum is a **sum type** ("this OR that"), and the algebraic-data-type section above is what happens when a language lets you compose both freely.
- **"Non-composite = defined without referencing another type"** does not survive its own examples: `^INTEGER` plainly references `INTEGER`. Learn the sentence for the 3 marks; do not build on it.
- **`SET OF` as a declared type** is Pascal-specific — a bit-set over an ordinal type. Modern languages give you set *collections* from a library (`set()`, `HashSet<T>`) and keep the bit-set idea as flag enums. Nobody declares a set type.
- **Pointer as a user-defined type** is C and Pascal. Managed languages hide it as "reference" and will not let you write `^INTEGER` at all; Rust exposes references with lifetimes and raw pointers behind `unsafe`; Go has pointers without arithmetic.
- **What the syllabus leaves out that industry runs on:** tuples, **generics** (`List<T>` — the most-used type constructor in existence), function types, **optional/nullable** types (the billion-dollar fix), interfaces and traits, and the nominal-versus-structural question — does a type match by *name* or by *shape*? — which is the real answer to "when is a record a class".
- And the ADTs: the pseudocode guide files stack, queue, linked list, dictionary and tree under "composite data types". In the real world an ADT is a *specification* — an interface plus a contract — that many concrete types can satisfy; the whole Data Structures bay is about that gap.

Two axes carry over from this card to everything after it: **product or sum**, and **value or reference**. Every type on the syllabus row sits somewhere on that grid — and so does every type you will meet for the rest of your career.

### What a record is in memory

A record is a *layout contract*: field offsets fixed at definition time, so `booking.taxi` compiles to "the bytes starting 40 after wherever this record starts" — no search, no lookup, one addition. That is why dot access is free while a dictionary lookup pays for hashing ([[Hash Tables]]'s price list), and why the compiler must know every field's type up front: it is computing the offsets.

---

## Exam Notes

### Cambridge 9618 (Paper 3 §13.1; records recur in Paper 4 code)

- The four LOs: **why** UDTs are necessary; define and use **non-composite** (enumerated, pointer); define and use **composite** (set, record, class/object); **choose and design** an appropriate UDT for a problem. A §13.1 question opens nearly every recent Paper 3.
- The recurring shapes, from the real papers this card is built on: **declare an enumerated type** from a given list (June 2026 P32, Nov 2025 P33, June 2025 P31 — 2 marks: `TYPE <name> =` and the bracketed list, *order preserved, equals sign only, no quotes, no added punctuation*, per the schemes' own guidance columns); **state characteristics of the value list** (complete/all possible values · ordered/ordinal · no duplicates — two of those for 2 marks); **declare a record** from a field table (4 marks, split in the scheme as: `TYPE`/`ENDTYPE` pair · `DECLARE` on every field · the nested UDT used · remaining field types right); **declare a set** (June 2024 P32: the `TYPE … = SET OF` line, then `DEFINE` with the value list and the set type's identifier); **define terms** (Nov 2023 P31: enumerated and pointer for 4; June 2024 P32: *non-composite* for 3 — "defined without referencing another data type" is the scheme's own first marking point).
- Pointer questions are usually definitional here ("stores addresses/memory locations · indicates the type of data stored there"), but pointers do their real exam work inside §19's linked structures — head pointers, next pointers, null markers.
- The exam dialect for every declaration above lives in [[Cambridge Pseudocode]], including the record's `TYPE … ENDTYPE` block and the set's two-line `TYPE`/`DEFINE` form.

### Not examined on…

- **Cambridge 0478 IGCSE:** no user-defined types at all — verified against the 2026–28 syllabus (zero occurrences of enumerated/record/user-defined; its pseudocode conventions stop at five built-in types). An IGCSE student meets this card only as a preview.
- **AP CSA:** the Java subset examines classes and objects thoroughly — but as object-oriented design, not as this taxonomy; enumerated types, pointers and sets are outside the subset (Java references exist but are never examined as a "pointer type").

---

## Quick reference

| Type | Kind | One-line definition | Python |
|---|---|---|---|
| Enumerated | non-composite | fixed, ordered, duplicate-free list of named values | `class Season(Enum)` |
| Pointer | non-composite | holds the *address* of a value of a stated type | references / index model |
| Record | composite | different types grouped under one identifier | `@dataclass` |
| Set | composite | unordered collection, no duplicates, membership queries | `{…}` / `set()` |
| Class | composite | record + its own operations | `class` — see [[Object-Oriented Programming]] |

---

## Connections

- **Parents:**
   - [[Arrays]] — the built-in aggregate this card generalises: an array is *many values of one type*; a record is *one value of many types*; and the array-of-records is the A-Level's standard data model.
   - [[Cambridge Pseudocode]] — the exam dialect for every declaration this card teaches conceptually; the two cards split the work on purpose (concepts here, syntax there).

- **Children:**
   - [[Linked List]] — the first structure *built from* this card's parts: a node is a record of data + pointer, and the free list is pointer surgery.
   - [[Object-Oriented Programming]] — the class half of the composite family, grown to full size: methods, inheritance, polymorphism, and the Paper 4 code.

- **Siblings in the taxonomy:** [[Stacks and Queues]], [[Binary Trees]], [[Hash Tables]], [[Graphs]] — all formally composite user-defined types per the pseudocode guide; each bay card is a design worked out in full.
- **The type-safety thread:** [[Floating-Point Representation]] — what the built-in `REAL` actually is underneath, and the precision contract you accept by choosing it; this card is about choosing types so the contract matches the data.

- **Misconception traps cleared:** enum values are names, not strings; lying nouns (phone *numbers*) are strings; sets have no order and no indices; non-composite is about construction, not capacity; the example data decides the field type.

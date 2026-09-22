---
chinese: 面向对象编程 (miànxiàng duìxiàng biānchéng)
prerequisites:
  - "[[User-Defined Data Types]]"
  - "[[Cambridge Pseudocode]]"
  - "[[Program Design]]"
  - "[[A Rich Neighbor Named Xerox]]"
  - "[[Program Development Life Cycle and Testing]]"
leads_to:
  - "[[Java Classes]]"
  - "[[Programming Paradigms]]"
  - "[[Dual-Core Craft]]"
  - "[[Java Objects, References and Strings]]"
tags:
  - subject/computer-science
  - domain/programming
  - domain/algorithms
  - level/A-Level
  - level/AP
  - level/IB
  - curriculum/Cambridge-9618
  - curriculum/AP-CSA
  - curriculum/IB-CS
  - syllabus/9618-20-1
  - syllabus/AP-CSA-1-12
  - syllabus/AP-CSA-3-1
  - syllabus/AP-CSA-3-3
  - syllabus/AP-CSA-3-4
  - syllabus/AP-CSA-3-5
  - syllabus/IB-CS-B3-1
  - syllabus/IB-CS-B3-2
  - type/deep
  - type/definition
  - notation/self
  - misconception/class-is-the-object
  - misconception/inheritance-is-for-code-reuse
  - misconception/polymorphism-is-overloading
  - misconception/private-is-enforced-in-python
---

# Object-Oriented Programming 面向对象编程

## Definition

Terms first, then code — the syllabus lists nine words and examines every one of them.

A **record** ([[User-Defined Data Types]]) bundles *data* of different types under one name. An **object** goes one step further: it bundles the data **and the procedures that are allowed to act on it**. The data are the object's **attributes** (also *properties*, *fields*); the procedures are its **methods**. The description of what attributes and methods every such object has is a **class**; each actual object built from it is an **instance**, made by a special method called the **constructor**.

Four more words name what classes let you *do*:

- **Encapsulation** — keeping the data inside the object and reaching it only through methods. The public face is the methods; the attributes are *private*, read by **getters** and changed by **setters**, so that nothing outside the object can put it into a nonsense state.
- **Inheritance** — a new class built *from* an existing one: a **subclass** (child, derived class) that has everything its **superclass** (parent, base class) has, plus its own additions. The test is the sentence *"a Parrot is an Animal."*
- **Polymorphism** — one method name, many behaviours: a subclass **overrides** a method it inherited, and a call on an object runs *that object's* version, so code that says `a.description()` never has to ask what kind of thing `a` is.
- **Containment** (aggregation) — an object holding *other objects* as attributes: a Station has an array of Trains. The test is *"has a"*, and it is the other way to build big things from small ones.

### 中文锚点

想象你在写一个游戏，场上站着两个长得一模一样的英雄。一个挨了打，另一个的血条当然不该跟着掉。写程序时，就可以让每个英雄把自己的生命值和“受伤”“回血”这些操作放在一起：叫谁受伤，就由谁去改自己的状态。这样的一个整体，就是一个对象。数据不再是散落在各处、分不清属于谁的数字，而是跟着具体的那个角色走。

## Key Vocabulary

| English | 中文 | 一句话 |
|---|---|---|
| Class / object / instance | 类 / 对象 / 实例 | 说明书 / 按说明书造出的东西 / 同上（强调"这一个"） |
| Attribute (property) | 属性 | 对象里的数据 |
| Method | 方法 | 对象自带的过程或函数 |
| Constructor | 构造器（构造函数） | 造实例时自动运行的方法 |
| Encapsulation | 封装 | 数据藏在里面，只留方法在外面 |
| Getter / setter | 取值方法 / 赋值方法 | 读属性 / 改属性的方法 |
| Inheritance | 继承 | 子类拥有父类的一切，再加自己的 |
| Polymorphism | 多态 | 同一个方法名，各类各有做法 |
| Containment (aggregation) | 包含（聚合） | 一个对象把别的对象当属性装着 |

---

## Why bundle behaviour with data — the problem OOP solves

Take the record from [[User-Defined Data Types]] and write a program around it. A `Booking` record, and then — somewhere else in the file — `cancel_booking(b)`, `extend_booking(b, days)`, `booking_total(b)`. Three procedures that all exist *for* bookings, and nothing in the language says so. Anyone can build a `Booking` with a departure date before its booking date; anyone can set `b.total = -5`; the procedures that keep a booking sane are optional, and separated by a hundred lines from the data they guard.

An object closes that gap by construction. The data and the procedures live in one place, the procedures are the *only* way in, and the object is born through a constructor that refuses to build nonsense. That is encapsulation, and it is the first and most practical reason OOP exists: **the invariants of a piece of data live next to the data.**

The second reason is polymorphism, and it is the one that scales. A zoo has parrots, wolves and horses; the display board needs each animal's description. Without objects: an `if kind == "parrot" … elif kind == "wolf" …` ladder that has to be edited every time a new animal arrives. With objects: `for a in animals: print(a.description())` — written once, never edited, because *each object carries its own version of the method*. Adding an animal is adding a class, not editing every loop in the program.

---

## The nine terms, built in real Python

### A class, its attributes, its constructor, an instance

```python
class Animal:
    def __init__(self, name, sound, size, intelligence):   # the constructor
        self.name = name                    # str
        self.sound = sound                  # str
        self.size = size                    # int, 1 (smallest) to 10
        self.intelligence = intelligence    # int, 1 to 10

    def description(self):                  # a method
        return (f"The animal's name is {self.name}, it makes a {self.sound}, "
                f"its size is {self.size} and its intelligence level is {self.intelligence}")

copper = Animal("Copper", "Neigh", 10, 6)  # an instance — the constructor runs here
copper.description()                        # the object does the work
```

Three things Python does that other languages hide:

- **`self` is the object itself**, passed automatically as the first argument of every method. `copper.description()` is really `Animal.description(copper)`. Every attribute lives on `self`; a name without `self.` inside a method is a local variable that vanishes when the method returns.
- **`__init__` is the constructor.** It does not *return* the object — Python builds the empty object first, then calls `__init__` to fill it in. (Cambridge's dialect calls it `NEW`; Java names it after the class.)
- **Attributes are created by assignment**, so Python has no declaration line for them — which is exactly why the exam says *"if you are writing in Python, include attribute declarations using comments"*: the comments above are the declarations, and they earn the mark.

### Encapsulation: private attributes, getters, setters

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance         # leading underscore: private, by convention

    @property
    def balance(self):                  # a getter — read-only from outside
        return self._balance

    def deposit(self, amount):          # the only sanctioned way to change it
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

acc = Account("Wei", 100)
acc.deposit(50)
acc.balance                              # 150
acc.balance = 1_000_000                  # AttributeError: no setter — the door is shut
```

Python enforces privacy by *convention*, not by force: `_balance` is a signal to other programmers, and `acc._balance = -5` still works if someone insists. A double underscore, `__balance`, goes one step further — Python *mangles* the name to `_Account__balance` so accidental access fails — and that is the form the Cambridge mark schemes print when a question says "all attributes should be private". Java and VB.NET enforce it with the keyword `private`. The *idea* is the same in all three: **state changes only through methods that know the rules.**

A getter that only reads and a setter that validates are the whole of the exam's "getters and setters"; the `@property` form above is how idiomatic Python writes a getter so that `acc.balance` reads like an attribute while running a method.

### Inheritance, and the constructor chain

```python
class Parrot(Animal):                                   # Parrot IS-A Animal
    def __init__(self, name, sound, size, intelligence, wing_span, number_words):
        super().__init__(name, sound, size, intelligence)   # the parent builds its part
        self.wing_span = wing_span          # int, cm
        self.number_words = number_words    # int

    def change_number_words(self, change):
        self.number_words += change
```

`Parrot` has every attribute and method `Animal` has, without restating them. The one discipline is the constructor: **the child's constructor calls the parent's** — `super().__init__(…)` — to build the inherited part, then adds its own. Forget that line and the parrot has no name. The exam scheme's wording is exactly this: "constructor … calling parent constructor with the four parameters".

### Polymorphism: override, and let the object decide

```python
class Parrot(Animal):
    ...
    def description(self):              # overrides Animal.description
        return (super().description() +
                f". It has a wingspan of {self.wing_span}cm and can say {self.number_words} words.")

class Wolf(Animal):
    def __init__(self, name, sound, size, intelligence, territory_size):
        super().__init__(name, sound, size, intelligence)
        self.territory_size = territory_size    # int, square miles
    def set_territory_size(self, change):
        self.territory_size += change
    def description(self):
        return super().description() + f". It has a territory of {self.territory_size} square miles."

zoo = [Parrot("Chewie", "Squawk", 1, 10, 30, 29),
       Wolf("Nighteyes", "Howl", 8, 7, 100),
       Animal("Copper", "Neigh", 10, 6)]
for a in zoo:
    print(a.description())              # three different methods run — one line of code
```

![[oop-polymorphism.svg|700]]

The loop is the point of the whole topic. It does not test the type; it does not branch; it will not need editing when `Elephant` arrives next term. Each object answers `description()` in its own way because **the method is looked up on the object at run time, not chosen by the caller.** Note the override *reuses* the parent's version through `super().description()` — extension, not replacement — which is what "overrides/extends the parent method" in the scheme allows.

### Containment: has-a, not is-a

```python
class Train:
    def __init__(self, train_id, route):
        self.__train_id = train_id          # str
        self.__route = route                # int
    def get_train_id(self): return self.__train_id
    def get_route(self):    return self.__route

class Station:
    def __init__(self, station_id, number_platforms):
        self.__station_id = station_id            # str
        self.__number_platforms = number_platforms  # int
        self.__trains = []                        # Train objects at the platforms
        self.__number_trains = 0                  # int

    def add_train(self, train):
        if self.__number_trains >= self.__number_platforms:
            return False                          # no platform free
        self.__trains.append(train)
        self.__number_trains += 1
        return True

    def get_trains(self):
        if self.__number_trains == 0:
            return "There are no trains"
        out = f"The trains at station {self.__station_id} are:\n"
        for t in self.__trains:
            out += f"{t.get_train_id()} on route number {t.get_route()}\n"
        return out
```

A Station is not a kind of Train, and a Train is not a kind of Station; the station **contains** trains. Its `__trains` attribute is a list *of objects*, and `get_trains()` asks each one for its data through that object's own getters — the station never reaches into a train's private attributes, because it cannot. That is containment and encapsulation working together, and it is the November 2025 Paper 41 question almost line for line.

![[oop-class-diagram.svg|780]]

The diagram is the design language of the trade: a box per class (name, attributes, methods), a **hollow triangle** for *is-a*, a **diamond** for *has-a*. Draw it before writing the classes; the exam's own class tables are this diagram with the lines removed.

---

## Designing the classes — the examined skill

The syllabus asks you to *"solve a problem by designing appropriate classes"*, and the whole decision is two questions asked of every noun in the problem:

| Ask | If yes | Example |
|---|---|---|
| Does the problem have a **kind of thing** with its own data and behaviour? | make it a **class** | Animal, Train, Station, Booking |
| Is one kind **a special case** of another — everything the parent has, plus more? | **inherit** (is-a) | Parrot is an Animal |
| Does one thing **hold** others as part of its state? | **contain** (has-a) | Station holds Trains; a Zoo holds Animals |
| Must a value never be set to nonsense from outside? | make it **private**, expose a **getter**, validate in a **setter** | balance, number of trains |
| Do several kinds answer the same question differently? | give the parent the method and let children **override** | `description()` |

Two traps in the design step. *Is-a* is a strict test — a Square is not a Rectangle for programming purposes if a Rectangle's `set_width` must be allowed to break squareness; when the sentence sounds forced, use has-a. And inheritance is not for saving typing: two classes that merely *share some code* but are not the same kind of thing should share a contained helper object, not a parent.

---

## Worked examples — the real Paper 4 questions

### June 2025 Paper 42 Question 3 — Animal, Parrot, Wolf

*The class Animal stores name, sound, size (1–10) and intelligence (1–10); its constructor initialises all attributes; `Description()` returns "The animal's name is … its intelligence level is …". Parrot inherits from Animal, adds WingSpan and NumberWords, a constructor that calls the parent's, `ChangeNumberWords()` (adds its parameter) and an overriding `Description()` that appends ". It has a wingspan of … cm and can say … words." Wolf inherits likewise with TerritorySize and `SetTerritorySize()`. Then create Chewie (a parrot), Nighteyes (a wolf) and Copper (an animal), change Nighteyes' territory by −20 and Chewie's words by +2, and output all three descriptions.* [4 + 3 + 4 + 2 + 4 + 2 + 2 + 3 + 2]

The code above *is* the answer; here is how the published scheme prices it, part by part, because the marks are for structure:

- **3(a)(i), 4 marks** — class header (and end where the language needs one) · four attributes with appropriate types — *in Python, as comments* · constructor header within the class taking at least four parameters · each parameter assigned to its attribute.
- **3(a)(ii), 3 marks** — `Description()` header with no parameter (Python: `self` only) · concatenating the attributes with the given message · returning it. `str()` around the integers is the Python-specific slip.
- **3(b)(i), 4 marks** — header *inherits from Animal* · constructor with six parameters *calling the parent constructor with the four* · the two new attributes assigned · `ChangeNumberWords()` adding its parameter to the attribute.
- **3(b)(ii), 2 marks** — `Description()` header "overriding/overloads/extending/using parent method" · the correct string. The scheme lists all three of Java's, VB's and Python's answers; the Python one repeats the whole string, and the `super().description() + …` form above is the *extending* route it explicitly allows.
- **3(d), 7 marks** — three instances created "and stored in a suitable variable/structure" · the two update calls on the right objects · `Description()` called for all three *after* the updates and output · a screenshot showing the updated values (31 words, 80 square miles).

The Java the scheme prints beside it, for readers on that board:

```java
class Parrot extends Animal {
    public Integer WingSpan;
    public Integer NumberWords;
    public Parrot(String pName, String pSound, Integer pSize, Integer pIntelligence,
                  Integer pWingSpan, Integer pNumberWords) {
        super(pName, pSound, pSize, pIntelligence);
        WingSpan = pWingSpan;
        NumberWords = pNumberWords;
    }
    public void ChangeNumberWords(Integer Change) { NumberWords = NumberWords + Change; }
}
```

Same skeleton, three differences worth naming: the constructor is named after the class; `extends` for `(Animal)`; `super(…)` for `super().__init__(…)`; and Java has no `self` because `this` is implicit. Everything the scheme marks is visible in both.

### November 2025 Paper 41 Question 2 — Train and Station

*Train stores TrainIDNumber and Route, all attributes private, with getters. Station stores StationID, NumberPlatforms, an array Trains[0:9] of Train and NumberTrains; `AddTrain()` stores a Train if a platform is free and returns TRUE, else FALSE; `GetTrains()` returns "There are no trains" or the formatted list.*

The containment code above is the answer, and the scheme's prices: the private attributes as `self.__…` with type comments (4); the two getters (3); the Station constructor with `Trains` initialised to an *empty* array and `NumberTrains` to 0 (4); `AddTrain()` — compare the two counts, return `False`, append, increment, return `True` (4); `GetTrains()` — a string in *all* cases, the empty check first, the loop through *each* train calling *the train's own getters* (6). The last point is the containment mark: the station may not read `t.__train_id`; it must ask `t.get_train_id()`.

### June 2023 Paper 32 Question 4 — the theory door

*Draw one line from each OOP term to its most appropriate description.* [4] The scheme's pairs, which are the definitions this card opened with: **encapsulation** — putting data and methods together as a single unit; **getters** — methods used to return the value of a property; **setters** — methods used to update the value of a property; **polymorphism** — allows methods to be redefined for derived classes; **inheritance** — enables the defining of a new class that inherits from a parent class. Paper 3 examines the vocabulary; Paper 4 examines whether you can write it.

---

## Where this is the working tool

You have been using objects since your first line of Python: `"hello".upper()` is a method on a string object, `list.append` a method on a list, and every card in the Data Structures bay — [[Linked List]], [[Stacks and Queues]], [[Binary Trees]], [[Hash Tables]] — is a class whose private attributes are the structure and whose methods are the only operations allowed on it. That is encapsulation doing real work: a stack that cannot be popped when empty, because `pop()` checks and nothing else can reach the array.

Beyond the vault, nearly every large program is organised this way. A web framework's `Order` model is a class with validated setters; a game engine hands you a base class (`GameObject`, `MonoBehaviour`) and every enemy, coin and door *inherits* from it and overrides `update()` — the polymorphism loop, running sixty times a second over thousands of objects; a graphical toolkit's `Button` inherits from `Widget` so that one `draw()` loop paints a whole window. When you read documentation for any library, you are reading class diagrams in prose.

---

## Misconceptions

### 1. "The class is the object"

The class is the description; the object is the thing. `Animal` cannot make a sound; `copper` can. A class exists once; instances exist as many times as you construct them. **Fix:** say "instance" when you mean a built thing, and notice that only instances appear on the right of `=` after `NEW`.

### 2. Forgetting `self` — or forgetting `super().__init__`

`def description():` without `self` fails the moment it is called on an object; an attribute assigned as `name = name` instead of `self.name = name` vanishes when the constructor returns. And a subclass constructor that never calls the parent's leaves the inherited attributes unmade. **Fix:** `self` first in every method; `super().__init__(…)` first in every subclass constructor.

### 3. Inheritance as a typing-saver

"Class B needs most of A's code, so B inherits from A" — even when B is not an A. This produces hierarchies where a `Car` inherits from `Engine`. **Fix:** the is-a sentence, said aloud; if it is false, contain instead.

### 4. Polymorphism confused with overloading

Overloading (VB's `Overloads`, Java's same-name-different-parameters) is several methods with one name in *one* class. The polymorphism this card teaches, and the only kind Cambridge means by the word, is one method name across a *family* of classes, chosen by the object's type at run time. Python has no overloading at all; it has that polymorphism everywhere. **Fix:** on a Cambridge paper the exam word is *override*, and the test is "does a call on the parent type run the child's code?" IB uses a wider vocabulary: it asks for *dynamic* polymorphic behaviour, which is overriding, settled while the program runs, and also for *static* polymorphic behaviour, of which overloading is the standard example, settled when the program is compiled. An IB student should be able to name both and say which is which.

### 5. "Private means nobody can touch it" (in Python)

A single underscore is a convention; a double underscore is name-mangling, not a lock. **Fix:** know which form the question wants — the schemes print `self.__attribute` when they say *private* — and know that the guarantee in Python is social, the guarantee in Java is the compiler's.

### 6. Attributes without declarations, in the exam

Python creates attributes on assignment, so candidates write the constructor and lose the "attributes with appropriate data types" mark. **Fix:** the exam says it in the question — *include attribute declarations using comments* — so every `self.x = x` line carries `# int`, `# str`.

---

## Beyond syllabus

### Messages, not methods — what Kay meant

Recall from [[A Rich Neighbor Named Xerox]] that object-oriented programming was the *second* of the three things Jobs saw at PARC in 1979 and walked past. Alan Kay, who coined the term for Smalltalk, later said the important word was never "object" but **message**: an object is a little computer that you *send requests to*, and the object decides what to do — the polymorphism loop above, taken as the whole philosophy. Smalltalk had no `if` statement in the language; `True` and `False` were objects that responded differently to the message `ifTrue:`. Modern OOP kept the objects and lost most of the messaging; Erlang and the actor model kept the messaging and lost the classes.

### Composition over inheritance — and the gorilla

Deep inheritance trees are the classic OOP failure. Joe Armstrong, who created Erlang, put the complaint in one sentence: you wanted a banana, and what you got was a gorilla holding the banana and the entire jungle — because inheriting one method drags in the whole ancestry. The remedy the trade settled on is **composition over inheritance**: build objects out of contained parts (has-a) and reserve inheritance for genuine is-a families. Game engines took this to its logical end, and the end has a name — the next section.

### Beyond OOP — ECS, the object taken apart

Push composition over inheritance all the way and the object itself dissolves. **Entity–Component–System (ECS)** is the architecture nearly every modern game engine runs on, and it is worth knowing as the deliberate *inverse* of this card:

- An **entity** is just an identity — an ID number. It has no attributes and no methods of its own.
- A **component** is pure data, one concern each: a `Position`, a `Health`, a `Sprite`, a `Velocity`. An entity *has* whichever components it has; there is no class saying which.
- A **system** is behaviour with no object attached: `Movement` runs over *every* entity that has both a `Position` and a `Velocity`, whoever they are; `Rendering` over everything with a `Sprite`.

Under OOP, "a flying enemy that also swims" forces a choice between `FlyingEnemy` and `SwimmingEnemy` in the inheritance tree, or a diamond that most languages forbid. Under ECS it is an entity with a `Flies` component and a `Swims` component, and both systems pick it up without anyone editing a class. Behaviour is *composed at run time by what data is present*, which is polymorphism with the class hierarchy removed — the has-a diamond of the class diagram, taken to its limit. The second reason engines adopted it is speed: components of one type sit together in memory, so a system sweeps a contiguous array instead of chasing pointers between scattered objects — the cache-locality story of [[RAM and the Memory Hierarchy]], and the reason [[Dual-Core Craft]] ends its account of *StarCraft*'s single thread with ECS as the road back to parallelism.

And you are reading an ECS right now. This vault is built on the same principle — the manual calls it *"folders are decorative, not navigational"*: a card is an entity, its frontmatter tags and links are its components, and the Directories, the topic maps and the search protocol are the systems that sweep every card carrying a given tag. Nothing here inherits from a folder. A card on logarithms can sit under Number, Functions or Calculus and be found by all three, because what it *is* was never decided by where it was put — which is exactly the freedom ECS buys a game engine, and exactly what a class hierarchy takes away.

### Duck typing, and what a type is for

Python's loop over `zoo` never checked that every element was an `Animal`; it checked that each object *answered* `description()`. Add a `Robot` class with its own `description()` and the loop accepts it, unrelated to Animal — *if it quacks like a duck…* Statically typed languages (Java, C#) refuse this unless the classes share an interface, which is safer and stiffer. Both are answers to the question underneath this whole card: what should a program be allowed to assume about a thing it has not looked inside?

---

## Exam Notes

### Cambridge 9618 (§20.1 — Paper 3 theory, Paper 4 code)

- The OOP bullet of §20.1 asks for the **terminology** (objects, properties/attributes, methods, classes, inheritance, polymorphism, containment/aggregation, encapsulation, getters, setters, instances), the ability to **design appropriate classes** for a problem, and the ability to **write code** that uses OOP. The paradigms row also names low-level ([[Assembly Language]]), imperative (assumed from AS) and declarative ([[Declarative Programming]]).
- **Paper 3** examines the vocabulary: match-the-term tables (June 2023 P32 Q4), "describe what is meant by…", and "explain the benefit of encapsulation/inheritance for this program". The definitions at the top of this card are the scheme's own phrasings.
- **Paper 4** is where the marks are: a class table (attributes, constructor, methods) → write the class, its constructor and methods; a subclass table → inherit, call the parent constructor, override; instantiate, call, screenshot. The recurring per-part prices above (class header · attributes with types · constructor · assignments; header · concatenate · return; inherits · parent-constructor call · new attributes · method) barely change from series to series. **Python-specific rules from the papers themselves:** attribute declarations *as comments*; `self.__x` when told "all attributes should be private"; `str()` around integers in concatenation; and Python has no `end` so the "header (and end where appropriate)" mark is the header alone.
- The pseudocode forms — `CLASS … ENDCLASS`, `PUBLIC`/`PRIVATE`, `PROCEDURE NEW`, `INHERITS`, `SUPER.NEW`, `obj ← NEW Class(…)` — live in [[Cambridge Pseudocode]] and appear on Paper 3 when a question shows a class in the dialect.

### AP Computer Science A (Fall 2025 framework — Java)

- Unit 1.12 (objects as instances of classes) and **Unit 3, Class Creation** (§3.1 abstraction and program design, §3.3 anatomy of a class with `private`/`public`, §3.4 constructors, §3.5 writing methods, §3.6 passing and returning object references, §3.7 class (`static`) variables and methods, §3.8 scope and access, §3.9 `this`). The Class Design free-response question asks for one complete class written from a specification: private instance variables, a public constructor and public methods. The Java specimen above is a Cambridge mark-scheme subclass that uses `extends`, `super` and public fields, so it is not a model for that question.
- **Inheritance is in the Fall 2025 course as vocabulary, not as code.** §1.12 expects a student to know what a superclass and a subclass are, and that every Java class is a subclass of `Object`. Designing and implementing an inheritance relationship is outside the course, overriding `toString` and `equals` is outside it, and no learning objective asks for polymorphism, interfaces or abstract classes. An AP student needs this card's first half in Java and can read the second half as enrichment.

### IB Computer Science (B3)

- B3.1, *fundamentals of OOP for a single class* (SL and HL): class, attributes, methods, constructor, encapsulation, getters/setters. B3.2, *multiple classes* (HL only): inheritance, polymorphism, aggregation — the second half of this card, with the class diagram as the design artefact IB expects.

### Not examined on…

- **Cambridge 0478 IGCSE**: no object-oriented content at all (verified — the syllabus's only "class" is the classroom). Its pseudocode has records neither; the topic starts at A Level.

---

## Quick reference

| Term | One line | Python |
|---|---|---|
| Class / instance | blueprint / a thing built from it | `class Animal:` / `Animal(...)` |
| Attribute · method | data on the object · procedure on the object | `self.name` · `def description(self)` |
| Constructor | runs when an instance is built | `def __init__(self, ...)` |
| Encapsulation | private data, public methods | `self._x` / `self.__x`, `@property` |
| Inheritance | child has all of the parent plus more | `class Parrot(Animal)`, `super().__init__(...)` |
| Polymorphism | same call, the object's own version runs | override the method in the child |
| Containment | an object holding objects | `self.trains = []` of `Train` |

---

## Connections

- **Parents:**
   - [[User-Defined Data Types]] — the record is the class without behaviour; that card hands the class/object row forward to this one.
   - [[Cambridge Pseudocode]] — the exam dialect for every form here (`CLASS`, `NEW`, `INHERITS`, `SUPER`).
   - [[Program Design]] — the design step; a class diagram is the fourth design notation.

- **Children:**
   - [[Programming Paradigms]] — the four paradigms of §20.1 side by side, the declarative quarter (facts, rules, goals) run on a small Prolog engine.
   - [[Dual-Core Craft]] — where inheritance trees broke under real-time load and entity–component–system (ECS) replaced them; this card's Beyond explains ECS as OOP's deliberate inverse, and why the vault itself is built on it.

- **The bay that is already OOP:** [[Stacks and Queues]], [[Linked List]], [[Binary Trees]], [[Hash Tables]], [[Graphs]] — every structure a class, every operation a method, every invariant guarded by encapsulation.
- **History:** [[A Rich Neighbor Named Xerox]] — Smalltalk on the Alto, the thing Jobs was too dazzled to see; [[Assembly Language]] — the low-level paradigm at the other end of the same syllabus row.

- **Misconception traps cleared:** class ≠ object; `self` and `super().__init__` are not optional; is-a is a test, not a convenience; override ≠ overload; Python's private is a convention; attributes must be declared in comments on the exam.

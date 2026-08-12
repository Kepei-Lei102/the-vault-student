---
chinese: 程序设计 (chéngxù shèjì)
prerequisites:
  - "[[Forward Reading and Problem Discovery]]"
leads_to:
  - "[[Cambridge Pseudocode]]"
tags:
  - subject/computer-science
  - domain/algorithms
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/9618-9-1
  - syllabus/9618-9-2
  - syllabus/9618-11-1
  - syllabus/9618-11-3
  - syllabus/9618-12-2
  - syllabus/0478-7-1
  - syllabus/0478-7-2
  - syllabus/0478-7-3
  - syllabus/0478-7-9
  - type/deep
  - misconception/design-is-wasted-time
  - misconception/flowchart-shapes-are-decorative
  - misconception/structure-chart-is-a-flowchart
  - misconception/stepwise-refinement-is-one-pass
---

# Program Design 程序设计

> *You will be given a problem in English and asked for a solution in code, and the marks are not all at the end. Between the paragraph and the program sit four drawings and a table, and each exists because it answers a question the others answer badly. Learn them as five things to memorise and they are a chore. Learn them as five questions asked about one program and they become the fastest way to find out whether you actually understand a problem. Underneath all five sit the only two questions that matter: **how do I make this solvable**, and **what doesn't change** — which are the hunter's questions, asked of a paragraph of English instead of a moving body.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| abstraction | 抽象 | deciding what to leave out |
| decomposition | 分解 | deciding where to cut the problem |
| algorithm | 算法 | a solution expressed as a sequence of defined steps |
| identifier | 标识符 | the name a program gives to a piece of data |
| identifier table | 标识符表 | the list of those names, types and purposes |
| structured English | 结构化英语 | numbered plain-English steps, no dialect |
| flowchart | 流程图 | control flow drawn as shapes and arrows |
| structure chart | 结构图 | the decomposition drawn, with the parameters shown |
| stepwise refinement | 逐步求精 | rewriting each step in more detail until it is programmable |
| state-transition diagram | 状态转换图 | what a system can *be*, and what moves it |
| module / subroutine | 模块 / 子程序 | a named sub-task — a procedure or a function |

## Two questions make design possible at all

Cambridge examines two skills by name, and both are usually taught as definitions to recite. They are better learned as **questions you ask a problem** — the same two questions a hunter asks anything.

**Decomposition asks: how do I make this solvable?** You cannot sit down and solve *build a vending machine*. You can solve *take coins until a total is reached*. The cut is not administrative tidying; it is a search for pieces you can actually finish, and you keep cutting until every piece is one you could sit down and write today. The check that a cut landed somewhere real is the **honest-name test**: if you can call the piece `GetPayment` and mean it, the seam is in the right place. If the honest name is `DoTheMiddleBit`, you have cut through something that belongs together, and the name is telling you so.

**Abstraction asks: what doesn't change?** Keep what stays true across every case you care about; discard whatever varies. A map of the Chengdu Metro is not *wrong* for omitting the streets above it — it is useful for omitting them, because the **topology** is what doesn't change (Line 1 meets Line 2 at Tianfu Square whatever the traffic is doing) while the geometry does, and no traveller needed it. Every abstraction is that same bet, made deliberately.

And now the two questions answer each other, which is the part worth keeping:

> **The parameters of a module are exactly the things that vary. The body is exactly what doesn't.**

`GetPayment(price)` is a legitimate abstraction because *take coins until you have reached the total* is invariant — it is the same procedure for a drink, a train ticket or a parking meter. Only the total differs between those cases, so the total becomes the parameter and everything that stayed put went inside. Find the invariant and the interface is already designed: you are not really choosing parameters, you are reading off what varied.

This is [[Forward Reading and Problem Discovery]]'s central move pointed at program structure instead of at a physical system. *What doesn't change?* is the question that turns a mechanics problem into an energy equation; asked of a problem statement, it turns a paragraph of English into named pieces with honest interfaces. Same question, different quarry.

## Five questions, not five topics

Here is the idea everything below hangs on. The notations are not a list to memorise. Each exists because it answers **one** question well and the others badly:

| Notation | The question it answers | What it hides |
|---|---|---|
| **identifier table** | What does this program *know*? | everything about order |
| **structured English** | What does it *do*, in order? | the shape of the branching |
| **flowchart** | Where does control *go*? | the data, and the hierarchy |
| **structure chart** | How does it *break apart*, and what crosses each seam? | time — nothing here says *when* |
| **state-transition diagram** | What can it *be*, and what moves it? | everything that isn't a mode |

Read that "What it hides" column twice. A notation is useful *because* it throws things away — which makes every one of these an abstraction in its own right, applied to your own solution. Choosing the wrong one is not a style error; it is asking a question the drawing cannot answer.

And **stepwise refinement is not on the list, because it is not a notation.** It is the *process* that produces them, and it gets its own section below.

## The identifier table — what the program knows

Before anything moves, name the things. An **identifier table** lists every piece of data the solution needs, with its type and its purpose:

| Identifier | Data type | Description |
|---|---|---|
| `price` | INTEGER | cost of the selected drink, in cents |
| `inserted` | INTEGER | total money put in so far, in cents |
| `slot` | INTEGER | which dispenser slot was chosen |
| `coin` | INTEGER | value of the coin just accepted, in cents |

Three habits are worth more than the table itself:

- **The name is documentation you cannot lose.** `inserted` survives being read six months later; `x2` does not. Cambridge marks "suitable identifier names" explicitly, and *suitable* means a reader can guess the purpose without the description column.
- **Choosing the type is a design decision, not a formality.** Money in cents as an INTEGER, rather than dollars as a REAL, avoids an entire family of rounding bugs — the ones [[Floating-Point Representation]] explains, where 0.1 has no exact binary form and change comes out a cent short.
- **The table is where you notice what you forgot.** Filling it in is often the moment you realise nothing yet holds *which drink was chosen*.

## Structured English — what it does, in order

**Structured English** is the solution written as numbered plain-English steps, using the words of the three constructs — *sequence*, *selection* (IF/OTHERWISE), *repetition* (REPEAT/UNTIL, WHILE) — but no programming language at all:

```
1  Display the price of the selected drink
2  Set inserted to 0
3  REPEAT
4      Accept a coin
5      Add the coin's value to inserted
6  UNTIL inserted is at least the price
7  Dispense the drink from the chosen slot
8  IF inserted is more than the price
9      THEN give change of (inserted − price)
10 END IF
```

It reads as English, so a non-programmer can check it — which is the point. It is the notation you hand to the person who *asked* for the program, because it is the only one on this list they can audit. And it forces the branching to be explicit while letting you stay vague about mechanism: step 4 says *accept a coin* without committing to how a coin is detected.

## The flowchart — where control goes

A flowchart draws the same solution as shapes and arrows. Cambridge fixes the shape vocabulary, and **the shape is part of the answer**:

![[program-design-flowchart-symbols.svg|900]]

Now the vending machine, drawn:

![[program-design-flowchart.svg|697]]

Three things this notation shows that structured English cannot:

**A loop is a branch that goes backwards.** In the drawing there is no special loop symbol — the repetition is just a decision whose *No* arrow returns to an earlier box. That is not a drawing convention; it is what a loop *is* at machine level, where iteration is a conditional jump backwards ([[Assembly Language]]'s jump instructions are exactly this). The flowchart tells the truth that the word `REPEAT` politely hides.

**Every decision has exactly two exits, and both must be labelled.** An unlabelled arrow out of a diamond is a lost mark and, more importantly, an unanswered question.

**A subroutine box hides a whole chart behind one name** — the abstraction from the opening section, given a shape of its own. `DispenseDrink(slot)` is a promise that another flowchart exists and that you do not need it right now.

> [!tip] Read a flowchart forwards, like a hunter
> The temptation with a flowchart you have been *given* is to look for the answer. Don't. Start at START and trace, asking at each step *what has changed and what is now true* — exactly the forward reading of [[Forward Reading and Problem Discovery]]. A flowchart is a **causality trace somebody already drew for you**: every arrow is an assertion that this happens, then that happens, because of this. Traced forwards it will tell you its own purpose, which is precisely what "explain the purpose of a given algorithm" asks for. Read backwards from the output, it will lie to you cheerfully.

## Stepwise refinement — the process, not a picture

**Stepwise refinement** is the discipline of writing the solution at a level you can actually think at, then rewriting each step in more detail, and repeating until every step is small enough to code directly.

Start deliberately vague:

```
1  Take the customer's money
2  Give them the drink
```

Neither step is programmable. Refine step 1:

```
1    Take the customer's money
1.1      Display the price
1.2      Set inserted to 0
1.3      REPEAT accepting coins and adding them to inserted
1.4      UNTIL inserted is at least the price
```

Step 1.3 is still doing two things, so it refines again. You stop when a step maps onto statements you can write.

Two things students routinely get wrong about this:

- **It is not one pass.** The syllabus says "to a level of detail from which the task may be programmed," and how many levels that takes is a property of the problem, not a fixed number.
- **The numbering is the point, not decoration.** `1.3.2` records *which* step it came from, so a design stays auditable — and if a requirement changes, you know exactly which subtree to rewrite.

The payoff is that refinement and decomposition are the same activity: **each refined step that turns out to be self-contained is a module**, and the set of them is the structure chart in the next section. You do not design the modules and then write the steps. The steps, refined honestly, tell you where the modules are.

## The structure chart — how it breaks apart, and what crosses the seams

A **structure chart** draws the decomposition as a hierarchy, and — this is the part that earns the marks — labels **what data passes between the levels**:

![[program-design-structure-chart.svg|820]]

The boxes are easy. The arrows are the content, and they are the thing to get right:

- **Arrow pointing down** — a value passed *into* the sub-task: a parameter.
- **Arrow pointing up** — a value handed back *out*: a return value.
- The little circle at the tail marks it as a **data** flow rather than a flag.

So this chart is not merely saying "the program has three parts." It is specifying three interfaces: `GetPayment` needs to be told the price and gives back the amount collected; `DispenseDrink` needs to be told a slot and gives nothing back; `GiveChange` needs to be told an amount. Read the arrows and you can write the function signatures without reading anything else — which is exactly what "derive equivalent pseudocode from a structure chart" asks you to do.

> [!warning] A structure chart is not a flowchart with different boxes
> They answer different questions and hide different things, and swapping them is the most common error in this topic. A **flowchart shows time** — this happens, then that, and here is where it branches. A **structure chart shows containment** — this task is made of those tasks. *Nothing in a structure chart says what order the children run in*, or whether some run at all, or how many times. Left to right is not a sequence. If you find yourself wanting to put a decision diamond in a structure chart, you have reached for the wrong drawing.

## The state-transition diagram — what it can be

Some problems are not really sequences of steps. They are systems that sit in a **mode**, waiting, and change mode when something happens. A machine that has been fed 75 cents is not "at step 4"; it is in a *state*, and it will stay there indefinitely until an event arrives.

![[program-design-state-transition.svg|860]]

Read it as: **boxes are what the machine can be, arrows are what happens to it.** Each arrow carries the event that triggers the change. The initial marker on the left says which state it starts in.

The real content of the diagram is the arrows that **aren't** there. Nothing connects *Idle* to *Dispensing*, which is a design decision stated in a way code cannot easily state: you cannot get a drink without paying. Nothing leaves *Dispensing* except delivery, so a second button press during dispensing does nothing. A state diagram is an exhaustive claim about what is possible, and reviewing one is mostly hunting for the transition somebody forgot — the one that turns into a bug where a user does two things at once.

That is the choice rule in a sentence: **if your problem has steps, draw a flowchart; if it has modes, draw a state-transition diagram.** Traffic lights, cash machines, game characters, network connections and the process states of [[Operating Systems]] are all modes-with-events, which is why that card's ready/running/blocked triangle is a state-transition diagram wearing a different hat.

## Logic statements — making a decision precise

The last of §9.2's requirements is easy to skip and worth a paragraph. A decision in a design has to be **exact**, and English is not. "Give a discount to members who are over 65 or who spend more than $100" has at least two readings — does the member condition apply to both branches?

A **logic statement** removes the ambiguity by writing the condition with Boolean operators:

```
isDiscounted = isMember AND (age > 65 OR spend > 100)
```

The brackets are the whole point, and they say something English left open. This is the same Boolean algebra that runs the hardware — the AND and OR of [[Logic Gates]], the manipulation rules of [[Boolean Algebra]], the truth tables that let you check all four combinations of two conditions. A design decision and a logic gate are the same object at two scales, which is why the algebra transfers intact.

## From design to code

The exam's real demand is **translation**: given a flowchart or structured English, produce a program; given a program, produce a flowchart. The vending machine's collection loop, written as running Python:

```python
def get_payment(price):
    """Accept coins until the customer has paid at least the price."""
    inserted = 0
    while inserted < price:
        coin = accept_coin()          # blocks until a coin arrives
        inserted += coin
    return inserted


def vend_drink(price, slot):
    inserted = get_payment(price)
    dispense_drink(slot)
    if inserted > price:
        give_change(inserted - price)
```

Lay that beside the three drawings and every element is accounted for. The identifier table supplied the names. The structure chart supplied the two function signatures and told you `get_payment` returns a value while `dispense_drink` does not. The flowchart supplied the loop condition and the branch. Nothing in the code is a surprise, which is the entire argument for designing first: **the design is where the thinking happens, and the code is a transcription.**

One deliberate difference from the exam. Cambridge wants this translation in *its own* pseudocode dialect, with `←` for assignment and `ENDWHILE` closing the loop; real Python is written here because it can be run, and the dialect has a card of its own in [[Cambridge Pseudocode]]. The skill is identical either way — reading a design and emitting the constructs it implies. Only the spelling changes.

## What the exam asks for, and what the world actually does

This card would be dishonest if it left you believing professionals draw these. Most of them do not. The ledger is worth having straight — partly because you will notice the gap yourself, and partly because knowing *which* parts survived tells you which parts are actually worth learning.

| Notation | Alive in professional work? | What became of it |
|---|---|---|
| identifier table | **No** — nobody writes one | the type declaration, the record or dataclass, the IDE's symbol list. The artefact went; naming your data before you write it stayed |
| structured English | **No**, not as a numbered document | the docstring, the design document, the ticket, the commit message |
| flowchart of code | **Essentially dead** | code reads better than a picture of code, and the picture goes stale the moment the code changes |
| structure chart | **Extinct** as a hand-drawn artefact | its questions survive in auto-generated call and dependency graphs, and in the module boundaries a codebase really has |
| state-transition diagram | **Very much alive** | network protocols, interface logic, game AI, embedded controllers — often drawn deliberately, sometimes with the code generated *from* the diagram |
| flowchart for people | **Alive everywhere** | it never left where it started: clinical protocols, returns policies, troubleshooting guides — processes *humans* execute |

Two honest observations, pointing in opposite directions.

**The syllabus's design vocabulary is a snapshot of one school of thought.** Structured design, roughly 1965–1985 — Böhm and Jacopini's theorem, Dijkstra's argument against `GOTO`, Yourdon and Constantine's structure charts. It was fixed into examinations before object orientation was mainstream, before version control, before tests-as-specification, and before a codebase could be searched in milliseconds. That is why parts of it can feel like learning to draw a map of a city you will never visit. Design today happens mostly **in code** — types, function signatures, and tests that state the intent precisely enough to fail when it is violated — and **in conversation**, on a whiteboard that gets photographed and wiped. Very little becomes a formal document, and none of it uses these shapes.

**And yet not one of the questions expired.** *What does this program know? What does it do, in order? Where does control go? How does it break apart, and what crosses each seam? What can it be?* Every one is asked daily by every working programmer, answered in a different medium. A function signature is an identifier table and a structure-chart arrow at once. A well-named module is a decomposition with its abstraction written on the front. The notations aged; the questions did not, because they were never really about drawing.

So the fair verdict on the exam is this. You will be marked on shape choice and labelled decision exits, which is a **proxy** for understanding rather than understanding itself, and it is reasonable to find that a little hollow. But the exercise has one advantage the professional version genuinely lacks: it forces the design out of your head *before* there is working code to hide behind — at the one moment when being wrong is still free. **Learn the notation to pass the paper; learn the questions to write programs.** The first is a proxy for the second, and only the second keeps its value.

## Common Misconceptions (Teaching Notes)

### 1. "Designing is wasted time — I'll just start coding"

For a ten-line program, true. The syllabus is preparing you for problems where it stops being true, and the crossover is earlier than most students believe. **Fix:** the honest argument is not moral, it is arithmetic — a wrong decomposition discovered on paper costs a rubbed-out box; discovered after four hundred lines it costs the four hundred lines. Design is cheap to change precisely *because* it doesn't run.

### 2. "The flowchart shapes are just decoration"

The shape is a claim about what the step does, and using the wrong one is marked wrong. A rectangle that asks a question, a parallelogram that performs a calculation, a decision with three arrows out — all errors. **Fix:** six shapes, six meanings; learn them as vocabulary, because that is what they are.

### 3. "A structure chart is a flowchart drawn top-down"

The commonest error in §12.2. A flowchart shows **time**; a structure chart shows **containment** and says nothing at all about order. **Fix:** ask "does this drawing claim anything about *when*?" Flowchart yes, structure chart no. And if the answer you need is *what gets passed*, only the structure chart has it.

### 4. "Stepwise refinement means writing it out in more detail once"

It is recursive, and it stops on a condition — *can I code this step directly?* — not after a fixed number of passes. **Fix:** if any step in your final design still needs explaining before someone could write it, you have not finished refining, whatever level you have reached.

### 5. "Identifier tables are busywork the exam invented"

They are the cheapest bug-prevention in the topic, and the marks are the least of it. Fixing `price` as an INTEGER in cents at design time removes a rounding-error class before a line is written. **Fix:** treat the table as the moment you commit to what the program *knows* — and notice what is missing from it.

## Exam Notes

### Cambridge 9618 — §9.1, §9.2, §12.2 (and the door into §11.1)

- **§9.1 Computational Thinking Skills** — two LOs, both examined in words. *Abstraction*: the need for it and its benefits, describing its purpose, and **producing an abstract model of a system by including only essential details**. *Decomposition*: describe and use it, breaking problems into sub-problems **leading to the concept of a program module (procedure/function)**. The link to modules is in the syllabus's own wording, so an answer that stops at "break it into smaller parts" has stopped one step early.
- **§9.2 Algorithms** — an algorithm is *a solution to a problem expressed as a sequence of defined steps*; suitable identifier names presented in an **identifier table**; pseudocode containing input, process and output using the three basic constructs; **documenting an algorithm as structured English, a flowchart or pseudocode**; and the four translations, examined in both directions — pseudocode **from** structured English or a flowchart, and a flowchart **from** structured English or pseudocode. Then **stepwise refinement** to a programmable level of detail, and **logic statements** to define parts of a solution.
- **§12.2 Program Design** — the **structure chart**: describe its purpose, **construct one for a given problem**, express the **parameters passed between modules**, and **derive equivalent pseudocode from it**. Plus *understand the purpose of* **state-transition diagrams** — note the softer verb: §12.2 asks you to know what they are for, not to construct one, though reading one is fair game.
- **§11.1** opens with *implement and write pseudocode from a given design presented as either a program flowchart or structured English* — that LO is this material pointed at a keyboard. The rest of §11.1 (declarations, initialisation, assignment, expressions, built-in functions) is programming basics, not design.
- **Where the marks actually sit:** on the structure chart it is the **arrows**, not the boxes — a correct hierarchy with no parameters shown scores poorly. On flowcharts it is **shape choice and labelled decision exits**. On refinement it is the **numbering** that shows which step each refinement came from.

### Cambridge 0478 IGCSE — §7.1, §7.2, §7.9

- **§7.1** puts this inside the **program development life cycle** (analysis, design, coding, testing) and names the content of each stage explicitly: *analysis* = abstraction, decomposition, identifying the problem and requirements; **design = decomposition, structure diagrams, flowcharts, pseudocode**; coding = writing code and iterative testing; testing = testing with test data.
- **Watch the name.** 0478 says **structure diagram** where 9618 says **structure chart**. Same notation, two board vocabularies — use the one on the paper in front of you.
- **§7.2** is decomposition twice over: every computer system is made of sub-systems which are made of further sub-systems; a problem can be decomposed into its component parts; and *use different methods to design and construct a solution*.
- **§7.9** is the translation LO — *write and amend algorithms for given problems using pseudocode, program code and flowcharts*.
- The **flowchart symbols are printed in the syllabus itself** (section 4), and are exactly the six above: flow line, process, subroutine, input/output, decision, terminator. They are given to you; there is no excuse for the wrong shape.
- IGCSE stops short of the parameter arrows and of state-transition diagrams — both are A-Level.

### IB Computer Science (first assessment 2027)

- Not a named topic. The published outline works at the level of algorithm construction and tracing rather than design documentation, so flowcharts appear as things to *read* rather than a notation to be assessed on, and structure charts and state-transition diagrams do not appear at all. Useful preparation, not examined material.

### AP Computer Science A

- Not examined. AP CSA assesses Java directly, with no design-notation component — the closest relative is its emphasis on decomposing into methods and classes, which is §9.1's decomposition wearing an object-oriented hat.

## Beyond the syllabus

> [!info] Why "sequence, selection, iteration" is a complete list
> The three constructs are not an arbitrary teaching simplification. The **structured program theorem** (Böhm–Jacopini, 1966) proves that any computable function can be expressed using only sequence, selection and iteration — no jumps required. That result is why `GOTO` could be abandoned without losing any power, and it is the formal reason a flowchart drawn with only these three shapes can express *any* algorithm you will ever be asked for. The three constructs are not a starter set. They are the whole language.

## Connections

- **Builds on:** [[Forward Reading and Problem Discovery]] — a flowchart is a causality trace someone drew, and tracing it forwards for what-is-now-true is what turns "explain this algorithm" from guesswork into reading.
- **Leads to:** [[Cambridge Pseudocode]] — the exam's own dialect, and the translation target for every design here; the design is what you think in, that card is what you write it down in.
- **Application:** [[Searching]] and [[Sorting]] — the standard algorithms, and the natural things to hand a flowchart of and be asked what they do; [[Stacks and Queues]] and [[Linked List]] — where the operations are given as algorithms that a structure chart's parameter arrows describe exactly.
- **Kindred:** [[Logic Gates]] and [[Boolean Algebra]] — a decision diamond's condition and a gate are the same object at two scales, which is why logic statements transfer intact; [[Operating Systems]] — its process states are a state-transition diagram, so the notation here is the one that card's triangle is drawn in; [[Floating-Point Representation]] — why choosing INTEGER cents over REAL dollars in an identifier table is a design decision and not a formality; [[Assembly Language]] — a loop's backwards arrow is a conditional jump, which is what the flowchart draws honestly.

## Notation Reference

| Symbol / term | Where it appears | Notes |
|---|---|---|
| stadium | flowchart | terminator — START and STOP |
| rectangle | flowchart | a process — something is done |
| parallelogram | flowchart | input or output crossing the boundary |
| diamond | flowchart | a decision — exactly two labelled exits |
| double-sided rectangle | flowchart | a subroutine drawn elsewhere |
| box hierarchy | structure chart | containment, never sequence |
| arrow with a circle tail | structure chart | a parameter; down is in, up is out |
| rounded box | state diagram | a state the system can occupy |
| labelled arrow | state diagram | an event that causes a transition |
| `1.3.2` | stepwise refinement | which step this refinement came from |

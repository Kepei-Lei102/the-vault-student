---
chinese: 程序开发生命周期与测试 (chéngxù kāifā shēngmìng zhōuqī yǔ cèshì)
prerequisites:
  - "[[Program Design]]"
  - "[[Cambridge Pseudocode]]"
  - "[[Compilers and Interpreters]]"
  - "[[Learning as Verification]]"
leads_to:
  - "[[Ethics and Ownership]]"
  - "[[File Processing and Exception Handling]]"
  - "[[Object-Oriented Programming]]"
tags:
  - subject/computer-science
  - domain/software-engineering
  - domain/algorithms
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-7-1
  - syllabus/0478-7-5
  - syllabus/0478-7-6
  - syllabus/0478-7-7
  - syllabus/0478-7-8
  - syllabus/9618-12-1
  - syllabus/9618-12-3
  - type/deep
  - type/definition
  - misconception/extreme-and-boundary-are-the-same
  - misconception/validation-checks-that-data-is-correct
  - misconception/syntax-errors-are-found-by-testing
  - misconception/maintenance-means-fixing-bugs
  - misconception/black-box-testing-is-the-weaker-kind
---

# Program Development Life Cycle and Testing 程序开发生命周期与测试

## Definition

### Formal

The **program development life cycle** (PDLC, 程序开发生命周期) is the sequence of stages a program passes through from the first conversation about what it must do to the last change made to it years later: **analysis** (what is the problem, and what must the solution do), **design** (how the solution will be built, on paper, before code), **coding** (writing it, and testing each piece as it is written), **testing** (running the finished program against a plan of chosen inputs with known expected outputs), and **maintenance** (changing it after release — to fix, to adapt, to improve). A **life-cycle model** — waterfall, iterative, rapid application development — is a rule for how those stages are ordered and whether you may go back.

**Testing** is the activity of exposing faults on purpose, before the user does. It classifies what it finds into three kinds of **error**: **syntax** (the program breaks the language's grammar and will not translate), **run-time** (it translates and runs, then attempts an impossible operation and stops), and **logic** (it runs to completion and produces the wrong answer). It chooses **test data** in four kinds — **normal**, **abnormal**, **extreme** and **boundary** — and it uses **methods** that differ in when they happen and who does them: dry run, walkthrough, white-box, black-box, stub, integration, alpha, beta, acceptance.

### Intuitive

You are cooking a dish you have never made, for six guests on Saturday. On Monday you find out who is coming and that one cannot eat nuts — that is *analysis*: the problem and its requirements, before a pan is touched. On Wednesday you choose a recipe, write a shopping list and decide the order of the pans — *design*, on paper. On Saturday you cook — *coding* — and you taste as you go, which is the *iterative testing* the syllabus files under coding. Before serving, you plate one portion and check it against the picture in the recipe — *testing* against an expected output. And next year, when you make it again with a new oven and a guest who is now vegan, you change the recipe — *maintenance*, of two kinds at once.

Now the three models. A wedding banquet for three hundred is **waterfall**: the menu is fixed and signed off months ahead, every course is planned before the first is cooked, and nothing can change on the day — predictable, and unforgiving. A home cook improvising is **iterative**: cook a version, taste, adjust, cook again, and the dish that reaches the table is the fourth loop. A pop-up restaurant is **RAD**: rough versions of three dishes are put in front of real customers in the first week, the customers say what they like, and the menu is rebuilt around them before the "real" opening.

And the dry run is the moment before cooking when you read the recipe through with the ingredients on the counter, saying at each step what is now in each bowl. Written down, that is a trace table. Watch one being filled from a real exam flowchart:

![[pdlc-trace-manim.mp4]]

### 中文锚点

**程序开发生命周期 (chéngxù kāifā shēngmìng zhōuqī)** = 一个程序从"要解决什么问题"到"上线多年后的最后一次修改"所经过的各个阶段：**分析、设计、编码、测试、维护**。**测试 (cèshì)** = 在用户发现之前，故意把错误找出来。

用做菜来想。周六请六个人吃饭，做一道没做过的菜：周一先弄清谁来、谁不能吃坚果——这是**分析**，锅还没碰；周三选菜谱、写购物清单、排好下锅顺序——这是**设计**，在纸上；周六下厨——**编码**——边做边尝，这正是大纲归在编码阶段的"迭代测试"；上桌前先盛一份对照菜谱上的图片检查——这是**测试**，拿"预期输出"来比对；明年换了新烤箱、有位客人改吃素了，你改菜谱——这是**维护**。三种开发模型也在厨房里：三百人的婚宴是**瀑布模型**，菜单几个月前就定死、签了字，当天什么都不能改——可预期，却不留余地；家常菜是**迭代模型**，做一版尝一口再改，端上桌的是第四轮；快闪餐厅是**快速应用开发**，第一周就把三道菜的粗糙版本端给真实顾客，听他们的意见，正式开业前把菜单重做一遍。而**跟踪表 (gēnzōng biǎo)** 就是下锅前把菜谱从头读一遍、每一步说出每个碗里现在有什么——把这个过程写下来，每个变量一列，值变了才填一格。四种**测试数据**要分清：**正常**（会被接受的普通值）、**异常**（会被拒绝的值——超出范围或类型不对）、**极端**（仍被接受的最大值和最小值）、**边界**（极端值和它紧挨着的、刚好被拒绝的邻居，成对出现）。三种**错误**也要分清：**语法错误**翻译器就不放行；**运行时错误**是程序跑起来后做了不可能的操作而停下；**逻辑错误**最阴险——程序跑完了，答案是错的，只有拿预期输出来对比的测试才抓得住。

| English | 中文 | Idea |
|---|---|---|
| Analysis / design / coding / testing / maintenance | 分析 / 设计 / 编码 / 测试 / 维护 | the five stages |
| Waterfall · iterative · RAD | 瀑布模型 · 迭代模型 · 快速应用开发 | three orderings of the stages |
| Syntax · run-time · logic error | 语法错误 · 运行时错误 · 逻辑错误 | won't translate · stops while running · runs and is wrong |
| Normal · abnormal · extreme · boundary | 正常 · 异常 · 极端 · 边界 | the four kinds of test data |
| Validation · verification | 有效性检查 · 核对（验证） | is it reasonable · is it what the source said |
| Dry run · trace table | 人工演算 · 跟踪表 | executing by hand · the record of it |
| White-box · black-box | 白盒测试 · 黑盒测试 | paths through the code · inputs against the specification |
| Stub · integration · alpha · beta · acceptance | 桩模块 · 集成测试 · α 测试 · β 测试 · 验收测试 | the later methods, in order |
| Corrective · adaptive · perfective | 纠错性 · 适应性 · 完善性维护 | fix · adapt to a changed environment · improve |

---

## Part I — The life cycle: five stages and what each produces

Why have a cycle at all, rather than just writing the program? Because the cost of a mistake depends on *when* it is found. A requirement misunderstood in analysis costs one conversation to fix on Monday and a rewrite to fix after release; Boehm's 1981 survey of industrial projects put the ratio at roughly a hundred to one for large systems. A life cycle is a way of finding each kind of mistake at the stage where it is cheapest — which is why the exam asks *which stage* an activity belongs to, and why the answer is never arbitrary.

| Stage | The question it answers | Tasks the syllabus names | What it produces |
|---|---|---|---|
| **Analysis** | *What* is the problem? | abstraction (remove irrelevant detail), decomposition, identify the problem and the **requirements** | problem definition; requirements specification; documents about the current system |
| **Design** | *How* will it be solved? | decomposition into modules; structure charts / diagrams; flowcharts; pseudocode; data structures; the identifier table | a design the coder can follow; the **test strategy and test plan** |
| **Coding** | Build it | write the code in a chosen language; test each piece as it is written (**iterative testing**) | source code; the first errors — syntax errors live here |
| **Testing** | Does it do what analysis said? | run the test plan; dry runs and trace tables; the methods of Part IV | a test log: input, expected, actual, pass/fail |
| **Maintenance** | Keep it working, and worth using | corrective, adaptive, perfective changes (Part VII) | new versions |

Two of those cells are exam favourites. The **identifier table** — every variable and constant with its purpose, data type, size (array length, string length), an example value, and its scope — is a *design* document, because it is written before the code that uses it. A **trace table** is a *testing* document. And *syntax errors occur* in coding, not testing, because the translator finds them before any test is run ([[Compilers and Interpreters]]). The June 2022 Paper 22 question that asks you to put four activities into their stages is exactly that table's third column.

Notice also where the test plan is *written*: in design, before there is code. That is the practical meaning of [[Learning as Verification]]'s "write the gate first" — the expected outputs are decided from the requirements, so the code cannot argue with them.

---

## Part II — Three models, one set of stages

![[pdlc-models.svg|1000]]

The stages are the same in every model. A model decides two things: **whether you may go back**, and **how soon the client sees something**.

- **Waterfall.** Each stage is completed and signed off before the next begins; going back is not planned for. *Principles:* all requirements are identified before coding; the next stage does not start until the current one is finished. *Benefits:* the cost and the timeline are predictable; clear deliverables at the end of each stage make it easy to manage. *Drawbacks:* late changes to requirements cannot be accommodated; the client sees nothing working until the end, so a misunderstanding in analysis surfaces last. *Use it for* well-understood, fixed requirements — and, oddly, for safety-critical systems, where the *documentation* the sign-offs produce is the point. (The 1970 paper by Winston Royce usually cited as its source presented the pure form as a model that "invites failure" and recommended iteration; the name came later, from people who had read only the first figure.)
- **Iterative.** Build a working version quickly, then improve it in loops — analysis, design, code, test, *review*, and round again — each loop adding function. *Principles:* a large problem is broken into smaller steps; every loop produces something usable. *Benefits:* the client has something early; requirements can change between loops; errors in early loops are caught before much is built on them. *Drawbacks:* harder to cost and schedule; without discipline no loop is ever the last.
- **Rapid application development (RAD).** Minimal up-front planning; **prototypes** are built and shown to the client early, modules are developed **in parallel**, and the client is involved throughout. *Benefits:* the fastest route to a usable product; requirements can be changed cheaply because the client steers each prototype; separate areas can be worked on at the same time. *Drawbacks:* it needs the client to be available throughout, and makes it easy for the client to keep changing their mind; it suits small or modular problems better than one large tightly coupled one.

**Why different programs need different cycles** — the June 2025 question's exact phrase — comes down to a short list of factors the scheme names: is a prototype needed early; how complex is the problem; how big and experienced is the team; how much time and money is there; how involved will the client be; and, decisively, *are the requirements agreed at the start, or will they change?* Fixed requirements point to waterfall; changing ones to iteration or RAD.

---

## Part III — Three kinds of error, and who finds each

`pdlc-testing-demo.py` makes one of each and shows *what* catches it:

```
syntax error   : line 2: expected ':'          (found by the translator, before running)
run-time error : ZeroDivisionError              (found only when that input arrives)
logic error    : is_leap(1900) = True, expected False   (no crash; only a test catches it)
```

- A **syntax error** breaks the grammar of the language — a missing colon, an unmatched bracket, `OUTPUT` where `INPUT` was meant is *not* one of these but a logic error in disguise. The translator refuses to produce a program at all, and reports the line. It is the only kind of error that cannot reach a user.
- A **run-time error** appears while the program is running: division by zero, an array index past the end, a file that is not there, a type the operation cannot handle. The program was grammatical, and the fault only shows for *some inputs* — which is why test data must include the abnormal and the extreme. In Python it is an exception; the vault's card on [[File Processing and Exception Handling]] is about catching them.
- A **logic error** is the dangerous one. The program runs, finishes, and is wrong: the wrong condition, `OR` for `AND`, a loop that stops one short, a variable never reset. Nothing crashes; nothing reports. The only instrument that detects a logic error is a **test with an expected output** — or a dry run that watches the variables and sees one take an unexpected value.

**Exposing faults** is what Parts IV–VI are for. **Avoiding** them is what [[Program Design]] is for: decomposition into small modules with one job each, meaningful identifiers, an identifier table, code written from a design rather than from the keyboard, and the same expected outputs written down before the code. The syllabus's own phrase is *ways of exposing and avoiding faults*, and the pairing is deliberate: a fault avoided in design never needs exposing.

---

## Part IV — The methods of testing, and the plan that holds them

![[pdlc-testing-map.svg|1000]]

The nine methods are not nine alternatives. They sit at different points in the cycle and are done by different people, and the exam asks you to *describe* one and to *select data* for it.

- **Dry run** — execute the algorithm by hand, on paper, recording the variables: the trace table of Part VI. Finds logic errors before there is even code.
- **Walkthrough** — a dry run done as a group, the author stepping through the program a line at a time while others check each variable's value and the path taken; an error shows as a variable given an unexpected value or an unexpected path through the program (the November 2022 scheme's own words).
- **White-box** — testing *with the code visible*, designing inputs so that **every path** through the program is exercised: each branch of every `IF`, each loop entered and skipped. You need the source code or its structure and a test plan of inputs with expected outputs. The June 2025 bonus module has four paths, so four normal tests, one per row of its table.
- **Black-box** — testing *without* looking inside: inputs chosen from the specification, outputs compared with the expected. It finds logic errors (wrong result) and run-time errors (the program stops), and it is what the user or client will do; it cannot see an untested path, which is why the two lenses are complementary and not rivals.
- **Stub** — when a module the program calls is not yet written, a *simple module is written to replace it* that returns an expected value or prints a message to show it was called, so the caller can be tested now. `pdlc-testing-demo.py` Part 3 calls a database module that does not exist.
- **Integration** — modules that passed on their own are combined and tested *together*, to check that data passes correctly between them and that they work as one program.
- **Alpha** — the finished program tested in-house, by the developers' own organisation, before anyone outside sees it.
- **Beta** — released to a limited group of *real users outside* the organisation, to find faults in real use on real machines.
- **Acceptance** — the client tests the program against the agreed requirements and signs it off; the program is accepted, or not.

A **test strategy** is the document that says *which* of these will be used, on what, by whom and when. A **test plan** is the detailed table underneath it: for each test, the input, the expected output, the actual output when run, and pass or fail — plus which method it belongs to and what kind of data it is. The plan is written in design, filled in during testing, and kept as evidence.

---

## Part V — Test data, validation, and verification

### The four kinds of data

![[pdlc-test-data.svg|900]]

For a rule like *an integer from 5 to 10 inclusive*:

| Kind | Meaning | Examples |
|---|---|---|
| **Normal** | data the program should accept and process | 6, 7, 8 |
| **Abnormal** (erroneous) | data the program should reject | 31, −4, "six", 7.5 |
| **Extreme** | the largest and smallest values that are *still accepted* | 5 and 10 |
| **Boundary** | each extreme *together with* its neighbour just outside — the pair either side of the line | 4 and 5; 10 and 11 |

The 0478 definitions are exact and the marks depend on them: **extreme** values are accepted; a **boundary** test is the *pair* — the last value accepted and the first rejected — so "boundary: 5" alone is an extreme, not a boundary. The March 2024 scheme's own answers for 5–10 are normal 6, extreme 5 or 10, boundary 4 and 5 or 10 and 11, abnormal 31.

### Validation is not verification

Both are checks on **input**, and they ask different questions:

- **Validation** asks *is this reasonable?* — does it fit the rules for this field. Six named checks: **range** (between limits), **length** (number of characters), **type** (a number where a number is expected), **presence** (something was entered), **format** (matches a pattern: two letters then four digits), **check digit** (the last digit is computed from the others, as on an ISBN or a bank card — [[Learning as Verification]] Part IV runs both).
- **Verification** asks *is this what the source said?* — was it transcribed correctly. Two methods: **double entry** (type it twice and compare), **visual check** (the screen shows it back and the user compares it with the paper).

Neither asks *is it correct*. A date of birth of 03/04/2009 passes every validation check and is still wrong if the form said 04/03/2009; only verification sees that. And `ada@ex.con` passes a format check for an email address. `pdlc-validation.py` writes all six validation checks and both verification checks in a dozen lines of Python and runs them, then builds the June 2025 temperature test plan (an integer from −100 to 0) with all four kinds of data — every row passes, and the extreme/boundary distinction is printed at the bottom.

---

## Part VI — The trace table: a dry run written down

A trace table has **one column per variable**, an **OUTPUT** column, and a new row each time you would otherwise overwrite a value already in the current row. You fill it by executing the algorithm in your head, one statement at a time, writing a value only when it *changes*. The discipline is exactly [[Forward Reading and Problem Discovery]]'s: at each line, ask what is now true.

Take the March 2024 Paper 22 flowchart — a loop that reads group sizes until a 0, then prints the average:

| NumberGroups | Total | GroupSize | Average | OUTPUT |
|---|---|---|---|---|
| 0 | 0 | 7 | | |
| 1 | 7 | 10 | | |
| 2 | 17 | 2 | | |
| 3 | 19 | 8 | | |
| 4 | 27 | 3 | | |
| 5 | 30 | 9 | | |
| 6 | 39 | 0 | 6 | Average group size 6 |

Three habits the marks reward. **Read the input in the order the algorithm reads it, not the order it is listed**: the `0` stops the loop, so the `6` after it is never read — a table with a seventh row loses the column marks. **Do not fill a cell that did not change.** **Put the output in the row where it happens.** The scheme awards one mark for the NumberGroups and GroupSize columns together, and one each for Total, Average and OUTPUT. `pdlc-trace-table.py` generates this table automatically by watching the Python version run line by line — the machine's dry run, to check yours against.

A trace table also finds errors: the November 2022 walkthrough question expects exactly "a variable is given an unexpected value" or "the program takes an unexpected path". When a column holds a number you did not expect, the line that wrote it is the bug.

---

## Part VII — Maintenance: the program after release

A program is not finished at release; most of its life, and most of its cost, comes afterwards. The syllabus names three kinds, and the exam asks you to name them, distinguish them, and give reasons each may be needed:

- **Corrective** — fixing faults found in use: the *unexpected bugs reported in the first week* of the June 2026 scenario.
- **Adaptive** — changing the program because its **environment** changed: new hardware or operating system, a new version of a library it uses, a change in legislation, a change in the requirements themselves. The June 2025 factory scheme's list: change to requirements, new technology, library modules changed, relevant legislation changed.
- **Perfective** — making it *better* though nothing is broken: faster, easier to use, a new feature.

Any game's patch notes sort themselves into the three: "fixed a crash when opening the map" (corrective), "added support for the new controller" (adaptive), "reduced loading times" (perfective). The last learning objective — *analyse an existing program and make amendments to enhance functionality* — is perfective maintenance set as an exam task: read code you did not write, work out what it does (a trace table is the tool), then change it without breaking it (the test plan is the check).

---

## Where it earns its keep

- **Ariane 5, 4 June 1996.** Forty seconds into its first flight the rocket destroyed itself. The guidance software had been carried over from Ariane 4 — *adaptive maintenance without re-testing* — and a conversion of a 64-bit floating-point horizontal velocity into a 16-bit integer overflowed, because Ariane 5 flew faster: a **run-time error** that a single *extreme* test with Ariane 5's trajectory would have exposed. The software was not even needed after lift-off. Cost: about $370 million.
- **Therac-25, 1985–87.** A radiotherapy machine whose software reused code from earlier models that had hardware interlocks; the new model relied on software alone. A race condition — a logic error that appeared only when an operator typed fast — delivered radiation overdoses to six patients. There had been no **integration testing** of the software together with the hardware it now had to protect.
- **CrowdStrike, 19 July 2024.** A content update to security software crashed about 8.5 million Windows machines — airlines, hospitals, banks — within hours. The update had passed a validator that itself had a bug; it was not run through a staged rollout (alpha, then a small beta group) before going to everyone at once. The fix was **corrective maintenance** on the largest scale in history, one machine at a time.
- **Every commit you will ever push.** Continuous integration is the test plan of Part IV made automatic: every change runs the whole suite before it can merge. Test-driven development is the plan written before the code — the identifier table and expected outputs of design, enforced by a tool. The syllabus's stages are how professional software is actually built; the vocabulary changed, the cycle did not.

---

## Worked examples — every tool named

### Example 1 — activities into stages (Cambridge 9618, June 2022 Paper 22, Q1(b))

> *Complete the table by writing the life-cycle stage for each activity: an identifier table is produced; syntax errors can occur; the developer discusses the program requirements with the customer; a trace table is produced.* [4]

**Tool: Part I's "what it produces" column.** Trigger: each activity is a *document* or an *event*, and each belongs to exactly one stage. Identifier table → **design** (written before the code); syntax errors → **coding** (the translator reports them as you write); requirements discussed with the customer → **analysis**; trace table → **testing**. One mark each; the trap is putting syntax errors under testing, where no test ever sees one.

### Example 2 — RAD against waterfall (Cambridge 9618, November 2022 Paper 23, Q1(b)–(d))

> *(b)(i) State one benefit of using a development life cycle for the website. (ii) State one document that may be produced from the analysis stage. (c) The program will be developed using RAD. (i) State one principle of this life cycle. (ii) Give two benefits and one drawback of its use compared to the waterfall life cycle. (d) Give two reasons why adaptive maintenance may be required.* [1 + 1 + 1 + 3 + 2]

**(b) Tool: Part I.** A cycle makes the project easier to manage, plan and cost, with clear deliverables at the end of each stage [1]; analysis produces the problem definition or the requirements specification [1]. **(c) Tool: Part II's RAD paragraph.** A principle: prototypes are built and modules developed in parallel; minimal planning; the client is involved throughout [1]. Benefits over waterfall: quicker development because areas are worked on at the same time; a prototype early; requirements easy to change [2]. Drawback: the client must be available throughout — or, in the scheme's words, it is *too easy for the client to keep changing their mind* [1]. **(d) Tool: Part VII's adaptive list.** New technologies to host the website; a change in relevant legislation; changed library modules; changed requirements [2].

### Example 3 — which model did each team use? (Cambridge 9618, June 2026 Paper 23, Q3)

> *Team A produced early versions and showed them to the shop staff, changing the program after each session. Team B used a more traditional approach; the stages followed an agreed sequence. Identify the model adopted by each team and describe one additional feature of each.* [4] *(c) State three activities carried out during the design stage.* [3]

**Tool: Part II, read for the tell.** Early versions shown to users and changed after each → **RAD** (the scheme also accepts *iterative*): a prototype is available early; all stakeholders are involved; requirements can change; modules in parallel; minimal planning [2]. Stages in an agreed sequence → **waterfall**: the next stage does not start until the current one is complete; predictable budget and timeline; all requirements identified before coding; late changes cannot be accommodated [2]. **(c) Tool: Part I's design row.** Any three of: produce flowcharts / structure charts / state-transition diagrams; decide data structures; write pseudocode for the modules; produce the identifier table; produce the test strategy and test plan; check whether library code exists [3]. Note that the scheme *rejects* "program structure" as too vague — name the document.

### Example 4 — white-box paths, a stub, and what black-box finds (Cambridge 9618, June 2025 Paper 22, Q2(b))

> *A module calculates weekly bonus pay: 1–40 hours and sales ≤ 2000 → 0; 1–40 hours and sales > 2000 → 50; over 40 hours and sales ≤ 2000 → 10; over 40 and > 2000 → 100. (i) The module is tested using white-box testing. State two tests, using valid data, that can be used to test different paths through the program. [2] (ii) The program is to be tested using stub testing before all modules are complete. Describe stub testing. [2] (iii) The completed program compiles successfully and is tested using black-box testing. Identify and describe one type of error that black-box testing could detect.* [2]

**(i) Tool: Part IV, white-box = one test per path.** Trigger: a four-row table is four paths. Two tests from different rows, each with its expected output: hours 20, sales 2000 → bonus 0; hours 50, sales 3000 → bonus 100 [2]. Any two rows earn the marks; both must be *valid* data, because the question said so. **(ii) Tool: the stub definition.** Simple modules are written to replace each unfinished module; each returns an expected value or outputs a message showing it was called [2]. **(iii) Tool: Part III, minus the one the compiler already found.** The program *compiles*, so syntax errors are gone; black-box testing can detect a **logic error** (the program does not give the expected result) or a **run-time error** (the program performs an illegal operation and stops) [2]. `pdlc-testing-demo.py` Part 2 turns this module into a full plan and adds boundary rows: 41 hours with sales of exactly 2000 exposes a `<` written for `≤` that all four normal-path tests pass.

### Example 5 — what white-box testing needs (Cambridge 9618, June 2023 Paper 23, Q5)

> *(a) State the additional information a programmer needs to carry out white-box testing of a module, and explain why. [3] (b) The program is later changed to make it faster. Identify the type of maintenance.* [1]

**Tool: Part IV.** The programmer needs the **source code** (or its design) and a **test plan** of inputs with expected outputs [2], because the structure of the program must be known so that *every path* can be tested [1]. **(b)** Faster with nothing broken and no environment change: **perfective** [1].

### Example 6 — four kinds of data, defined and chosen (Cambridge 0478, March 2024 Paper 22, Q2)

> *(a) Link each test data type to its description. (b) An algorithm tests whether an input integer is in the range 5 to 10 inclusive. Identify suitable test data of each type.* [4 + 4]

**(a) Tool: Part V's table.** Normal — a value that is accepted; abnormal — a value that is rejected; extreme — the highest or lowest value to be accepted; boundary — the highest or lowest value accepted *and* the corresponding lowest or highest value rejected [4]. The description "the highest or lowest value to be rejected" on its own is the distractor: it matches nothing. **(b)** Normal 6; abnormal 31; extreme 5 or 10; boundary 4 and 5, or 10 and 11 [4] — the scheme's own answers, and the figure above.

### Example 7 — find the three errors (Cambridge 0478, March 2024 Paper 22, Q5)

> *Values for cost price and selling price are input, the profit (selling − cost) is calculated and output; input of zero for either value stops the algorithm. Identify the line numbers of three errors and suggest corrections.* [3]

The exam's pseudocode, with its errors:

```
01 REPEAT
02    OUTPUT "Enter cost price "
03    INPUT Cost
04    OUTPUT "Enter selling price "
05    OUTPUT Sell
06    IF Cost <> 0 OR Sell <> 0
07       THEN
08          Profit ← Sell - Cost
09          OUTPUT "Profit is ", Profit
10    NEXT
11 UNTIL Cost = 0 OR Sell = 0
```

**Tool: read each line forwards against the specification, asking what it must do.** Trigger: line 05 *outputs* `Sell` where the spec says the selling price is *input* — `INPUT Sell` (a logic error dressed as a typo). Line 06: the profit should be calculated only when *neither* value is zero, so `OR` must be `AND` — the classic condition error, and the one the specification's "either" is designed to make you check. Line 10: an `IF … THEN` block closes with `ENDIF`, not `NEXT` — a syntax error. Three lines, three corrections [3]. In Python the corrected loop is six lines and the translator would have caught line 10 before you did; lines 05 and 06 it would happily run.

### Example 8 — the trace table (Cambridge 0478, March 2024 Paper 22, Q7)

Worked in full in Part VI, with the machine's table beside it. The marks: NumberGroups and GroupSize columns together [1], Total [1], Average [1], OUTPUT [1]. The `6` that follows the `0` in the input list is the planted trap: an algorithm that stops on `0` never reads it.

### Example 9 — a validation test plan and a verification routine (Cambridge 0478, June 2025 Paper 22, Q3–Q4)

> *3. A range check validates that the input temperature is an integer between −100 and 0 inclusive. Suggest suitable normal, abnormal, extreme and boundary test data. [4] 4(a) State one reason for using a verification check when inputting data. [1] (b) Write pseudocode to perform a double-entry verification check: input 10 numbers into an array, input them again, compare each with the stored value, and report.* [6]

**3. Tool: Part V's definitions, with a negative range.** Normal −50 (any integer between −100 and 0); abnormal 50, or any non-integer such as "cold" or −3.5; extreme 0 or −100; boundary 0 and 1, or −100 and −101 [4]. `pdlc-validation.py` runs exactly this plan. **4(a)** To check that the value has not changed on input — that it matches the source [1]. **(b) Tool: the double-entry routine.** The scheme's mark points are a loop over ten inputs stored in the array; a second input for each; a comparison one at a time; on mismatch, output both values and ask for re-entry; the new value stored in that array position; a final message outside the loop [6]. In Python it is a `for` over `range(10)` with an inner `while` that repeats until the two entries match.

---

## Hands-on

1. **Run `pdlc-trace-table.py`**, then paste in any small algorithm of your own — a bubble sort pass, a running maximum — and let it print the trace table. Then do the same algorithm by hand *first* and compare: where your table differs from the machine's is where your mental model of the code is wrong.
2. **Run `pdlc-testing-demo.py`** and fix the two planted bugs in the bonus module so that all eight rows pass. Then add a ninth row that would have caught the *other* bug (0 hours) and watch the plan grow the way real test suites do — one row per bug ever found.
3. **Run `pdlc-validation.py`** and write a seventh check the syllabus does not name — a *lookup* check against a list of allowed values — then extend the temperature plan to it. Decide, before running, what each of your four data kinds should return.
4. **Read patch notes.** Open the update history of any game or app on your phone and sort the last twenty entries into corrective, adaptive and perfective. Most are perfective; the adaptive ones name a new OS version.

---

## Common Misconceptions (Teaching Notes)

### 1. "Extreme and boundary mean the same thing"

Extreme values are *accepted*: the largest and smallest that pass. A boundary test is the *pair* on either side of the line — the extreme and its rejected neighbour. Writing "boundary: 10" earns the extreme mark, not the boundary one; write "10 and 11".

### 2. "Validation checks that the data is correct"

It checks that the data is *reasonable* — the right type, length, range, format. A wrong but plausible value passes every validation check. Only **verification** (double entry, visual check) compares the input with its source, and even that only catches transcription.

### 3. "Testing finds syntax errors"

The translator finds them, in the coding stage, before a single test runs; a program with a syntax error cannot be tested because it does not exist yet. Testing finds run-time and logic errors — which is exactly the pair the June 2025 black-box question asks for *after* telling you the program compiles.

### 4. "Black-box testing is the weaker kind because you can't see the code"

It is a different lens, not a worse one: it tests the program against what it was *specified* to do, which is what the client and the acceptance test care about, and it is possible without the source. White-box tests paths; black-box tests requirements; a plan needs both.

### 5. "Maintenance means fixing bugs"

That is one third of it. Adaptive maintenance responds to a changed environment (new OS, new law, new library) and perfective maintenance improves what already works; in a long-lived program the last two outweigh the first. The exam asks for the type by name.

### 6. "Waterfall is obsolete" / "RAD is always better"

Fixed requirements and safety-critical work still use waterfall for its predictability and its paper trail; RAD needs a client who is available and a problem that splits into prototypes. The syllabus wants the *reasons for choosing* — team, budget, time, complexity, client involvement, whether requirements are fixed — not a ranking.

### 7. "A trace table records every line executed"

It records **values**, and only when they change; a row is a snapshot, not a line of code. Filling every cell in every row is the commonest way to lose the column marks, and reading the input list past the sentinel is the second.

---

## Exam Notes

### Cambridge 9618 (§12.1 and §12.3 — AS Paper 2)

- **§12.1 learning objectives:** the purpose of a development life cycle; the need for different cycles depending on the program (waterfall, iterative, RAD — principles, benefits, drawbacks of each); the analysis, design, coding, testing **and maintenance** stages. Note the fifth stage: 0478 stops at four.
- **§12.3 learning objectives:** ways of exposing and avoiding faults; locate, identify and correct syntax, logic and run-time errors; the methods of testing and data appropriate to each — dry run, walkthrough, white-box, black-box, integration, alpha, beta, acceptance, stub; the need for a test strategy and test plan and their contents; normal, abnormal and extreme/boundary data for a plan; the need for continuing maintenance and the difference between perfective, adaptive and corrective; analyse an existing program and amend it to enhance functionality.
- **Question shapes, from the papers this card is built on:** *explain the need for different life cycles* (June 2025 — one factor from the scheme's list); *state a principle / benefits / drawbacks* of a named model, often *compared to waterfall* (November 2022); *identify the model from a scenario* (June 2026 — early versions shown to users → RAD or iterative; an agreed sequence → waterfall); *put activities into stages* (June 2022); *state three design-stage activities* (June 2026 — and the scheme rejects "program structure"); *describe a named method* — walkthrough, stub, integration (2 marks: what is done, and what it shows); *state tests for different paths* (white-box, June 2025); *which error type can black-box testing detect once the program compiles* (logic or run-time, never syntax); *what information does white-box testing need* (June 2023: the code and a test plan, because every path must be known); *name the maintenance type* (perfective for "faster", corrective for "bugs in the first week", adaptive for "new hardware / legislation"); *give reasons adaptive maintenance may be needed*.
- **Trace tables** are a Paper 2 staple in every session, usually 4–6 marks, sometimes across two stages of a program (June 2026). Same rules as 0478: values only when they change, input read in program order, output in its row.

### Cambridge 0478 (§7.1, §7.5–§7.8 — Paper 2)

- **§7.1:** the four-stage cycle *and the tasks in each stage* — analysis (abstraction, decomposition, identifying the problem and requirements), design (decomposition, structure diagrams, flowcharts, pseudocode), coding (writing code and *iterative testing*), testing (testing with test data). Question shape: a tick-box on which task belongs to which stage (March 2024: decomposition is analysis; June 2025: abstraction is *removing details not relevant to the problem*).
- **§7.5:** the six validation checks and the two verification checks, by name and purpose; question shapes: match a requirement to its check (June 2025 P21: a date between limits → range; "has been entered" → presence; exactly 12 characters → length; two letters then four digits → format), *describe two validation checks that should be added to this algorithm* (March 2024: presence and type), and *write a double-entry verification routine* (June 2025 P22, 6 marks).
- **§7.6:** the four kinds of test data with 0478's exact definitions — extreme = largest/smallest *acceptable*; boundary = the acceptable extreme *and* the corresponding first rejected value. Match-the-description questions (March 2024; June 2022 asks for ticks in a grid where "always on the limit of acceptability" is extreme and "on the limit *or just outside*" is boundary) and choose-the-data questions for a stated range.
- **§7.7:** complete a trace table for a flowchart or pseudocode with given input — variables, outputs, and *user prompts* where the algorithm has them; 4–6 marks, usually one per column.
- **§7.8:** identify errors in given pseudocode and suggest corrections — three to five numbered lines, one mark per error-and-fix (March 2024 Q5, June 2025 Q7). The usual plants: `OUTPUT` for `INPUT`, `OR` for `AND`, a wrong loop terminator, a counter never incremented, `<` for `<=`.
- The vocabulary is Cambridge pseudocode's, and the errors are found in it — [[Cambridge Pseudocode]] carries the dialect.

### Where it is *not* examined

- **IB Computer Science (2027 syllabus):** no life-cycle model is named and testing is not a standalone topic; the ideas surface only inside the internal assessment's development and evaluation.
- **AP Computer Science A:** no PDLC; testing appears as vocabulary (compile-time versus run-time errors) and as the habit of checking a method with several inputs, never as named methods or data types.
- **9618 Paper 4** does not ask for the theory, but every program written for it is marked as if it had been tested with normal, abnormal and boundary data — the schemes' "correct output for the given test data" is a black-box test.

---

## Connections

- **Parents:**
   - [[Program Design]] — the analysis and design stages in full (abstraction, decomposition, structure charts, flowcharts, the identifier table); this card takes the cycle from coding onward and adds the models.
   - [[Cambridge Pseudocode]] — the dialect the trace tables and error-finding questions are written in.
   - [[Compilers and Interpreters]] — why syntax errors belong to coding: the translator reports them, and a compiler and an interpreter report run-time errors differently.
   - [[Learning as Verification]] — the test plan is that card's "write the gate first"; the trace table is its rung 7, simulation by hand; the ladder's cheap checks are what a dry run does before any test runs.

- **Children:**
   - [[File Processing and Exception Handling]] — run-time errors caught and handled rather than exposed.
   - [[Object-Oriented Programming]] — encapsulation as fault *avoidance*: invariants kept next to the data they protect.

- **Cross-domain:** [[Forward Reading and Problem Discovery]] — a dry run *is* forward reading, asking at each line what is now true; [[Hash Tables]] and [[Searching]] — the algorithms most often set for trace tables; [[Data Security]] — validation as the first line of defence against malformed input.

- **Misconception traps cleared:** extreme is not boundary; validation is not correctness; syntax errors are not found by testing; black-box is not the weaker kind; maintenance is not only bug-fixing; waterfall is not obsolete; a trace table is not a line log.

---

## Beyond Syllabus

### Test-driven development: the plan before the code, enforced

Recall that the test plan is a design document. TDD makes that mechanical: write the test *first*, watch it fail, write the least code that passes it, tidy, repeat. The suite that results is the test plan of Part IV, kept forever and run on every change — which is what a **continuous-integration** server does: every commit is built, every test run, and a red result blocks the merge. The stages did not go away; they run in minutes instead of months.

### Coverage: white-box testing with a number

White-box testing asks that every path be exercised. A coverage tool measures it: the percentage of lines, branches or paths executed by the test suite. A hundred per cent *line* coverage still misses the June 2025 boundary bug (`<` for `≤` executes the same line); *branch* coverage with boundary data catches it. Coverage measures what the tests *touched*, not what they *checked* — a test with no expected output can cover everything and verify nothing.

### Fuzzing: abnormal data at scale

The abnormal-data column of a test plan, generated by machine: millions of random or mutated inputs thrown at a program to find the run-time errors that hand-written abnormal data missed. Most security vulnerabilities found in the last decade were found this way; it is Part V's "abnormal" kind, industrialised.

### Agile and Scrum: the iterative model with a calendar

The iterative and RAD models of Part II grew into the Agile methods of the 2001 manifesto: fixed-length loops (sprints, usually two weeks), a working increment at the end of each, the client (product owner) in the room, requirements held as a re-orderable backlog rather than a signed specification. A Scrum team is running RAD's principles with waterfall's discipline about what each loop must deliver.

### Formal verification: when testing is not enough

Testing shows the presence of faults, never their absence — Dijkstra's line. For code where a fault is unaffordable, the alternative is to *prove* the program meets its specification, mechanically, with the small trusted checkers of [[Learning as Verification]] Part I. The seL4 operating-system kernel and the CompCert C compiler are proven correct this way; they are still tested, because the specification itself can be wrong.

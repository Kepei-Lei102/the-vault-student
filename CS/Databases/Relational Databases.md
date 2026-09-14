---
chinese: 关系型数据库 (guānxì xíng shùjùkù)
prerequisites:
  - "[[File Handling]]"
  - "[[File Processing and Exception Handling]]"
  - "[[User-Defined Data Types]]"
leads_to:
  - "[[SQL]]"
  - "[[NoSQL and Distributed Data]]"
tags:
  - subject/computer-science
  - domain/databases
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-9-1
  - syllabus/9618-8-1
  - syllabus/9618-8-2
  - syllabus/9618-8-3
  - syllabus/IB-CS-A3-1
  - syllabus/IB-CS-A3-2
  - type/deep
  - misconception/a-database-is-a-big-spreadsheet
  - misconception/normalisation-is-about-saving-space
  - misconception/the-primary-key-is-the-first-column
---

# Relational Databases 关系型数据库

> *Your phone is carrying a few hundred of them right now. Every chat app, every photo library, every browser history, every map cache is a relational database — the same idea, from the same 1970 paper, run by the same small engine. Nobody on Earth is more than a few centimetres from one.*

## Definition

### Formal

A **relational database** stores data as a set of **relations** — tables — in which every row (a **tuple** / **record**) holds one fact about one thing, every column (an **attribute** / **field**) holds one kind of value, and rows in different tables are linked not by pointers but by **matching values**: a **foreign key** in one table equals a **primary key** in another. The model was proposed by E. F. Codd in *A Relational Model of Data for Large Shared Data Banks* (Communications of the ACM, June 1970) — and its whole content is that a database should be a collection of tables connected by *values*, with the physical storage hidden from everyone who uses it.

A **Database Management System (DBMS)** is the software that owns those tables: it defines their structure, enforces the rules that keep them consistent, answers queries, controls who may see what, and recovers the data after a crash.

### Intuitive

A spreadsheet is a table. A relational database is a set of tables *that know about each other*. In a spreadsheet of school trips, "Mr Smith" is typed into forty rows, and when he becomes "Dr Smith" you edit forty cells and miss three. In a database, Mr Smith is *one row in the PARENT table*, and the forty trip rows each hold his ID — one edit, forty rows follow. That single move — **store each fact once and point at it by key** — is the relational idea, and everything else in this card (keys, relationships, normalisation, integrity) is the machinery that makes the move safe.

### 中文锚点

你点了一份外卖。屏幕上那张小票——你的名字、地址、三个菜、总价——在商家系统里**不是一张小票**。它是三四张表里各取几行拼出来的：一张 CUSTOMER 表存你（你的名字只存一次，哪怕你点过五百单）；一张 ORDER 表存这一单（时间、状态、指向你的 CustomerID）；一张 ORDER_ITEM 表存每个菜（指向这一单的 OrderID，和菜单表里的 DishID）。你改了地址，五百单历史订单不用动，因为地址只在 CUSTOMER 表里存了一份。**每个事实只存一次，别处用"钥匙"去指它**——这就是 1970 年 Codd 提出的**关系模型**，也是这张卡的全部内容。这套东西离你有多近？你的手机里此刻就跑着几百个：微信的聊天记录、相册、浏览器历史、地图缓存，全是**SQLite** 数据库文件——同一个 1970 年的想法，同一个几百 KB 的引擎，全世界大约有一万亿个实例在运行。学校的版本是"文件式"的失败现场：成绩册一个 Excel、名单一个 Excel、家长电话又一个 Excel，同一个学生在三个文件里拼法不一样，转学了一个文件删了两个没删。数据库解决的就是这个：**冗余**（同一事实存多份）→ **不一致**（几份对不上）→ **依赖**（换个程序读不了）。用到的词只有几个：**表**（一类事物）、**记录 / 行**（一个事物）、**字段 / 列**（一种属性）、**主键**（唯一认出这一行的字段）、**外键**（存在别的表里的、指向这里主键的值）、**联系**（一对一、一对多、多对多）。**规范化**（1NF → 2NF → 3NF）是把一张什么都塞进去的大表，拆成"每个事实只出现一次"的几张小表的固定步骤——不是为了省空间（空间很便宜），是为了**改一处就全对**。

| English | 中文 | 一句话 |
|---|---|---|
| Table / relation | 表 / 关系 | 一类事物：CUSTOMER、ORDER |
| Record / row / tuple | 记录 / 行 / 元组 | 一个事物：一位顾客、一笔订单 |
| Field / column / attribute | 字段 / 列 / 属性 | 一种属性：姓名、下单时间 |
| Primary key | 主键 | 唯一认出一行的字段（或几个字段的组合） |
| Foreign key | 外键 | 存在别的表里、指向这里主键的值——**联系就靠它** |
| Candidate / secondary key | 候选键 / 辅助键 | 也能唯一认出一行的字段 / 用来快速查找的非唯一字段 |
| Referential integrity | 参照完整性 | 外键指向的那一行**必须存在** |
| Normalisation (1NF/2NF/3NF) | 规范化 | 把大表拆成"每个事实只存一次"的小表的固定步骤 |
| DBMS | 数据库管理系统 | 管这些表的软件：结构、规则、查询、权限、恢复 |

---

## Why files fail — the problem the model solves

Before 1970 (and in every school office today) data lived in **files**, each owned by the program that wrote it: a payroll file for the payroll program, a class-list file for the timetable program. [[File Handling]] shows what a file is — a sequence of records in a format one program understands. Three things go wrong the moment two programs need the same fact:

| Failure | What it looks like | Why it is structural |
|---|---|---|
| **Data redundancy** | a student's name and address stored in the timetable file *and* the payroll file *and* the library file | each program keeps its own copy because it cannot read the others' |
| **Data inconsistency** | "Li Jun" in one file, "LI Jun" in another, an old address in a third | copies drift; nothing forces them to agree |
| **Program–data dependence** | change the record layout and every program that reads it breaks | the structure lives in the code, not in the data |

Add the smaller ones — no shared access control, no way to ask a question nobody wrote a program for, no recovery if a write half-finishes — and you have the list every exam asks for. The relational model answers all of them with one design decision: **the structure and the rules live in the database, not in the programs; every fact is stored once; programs ask questions in one language and never see the storage.**

## Codd's model — tables linked by values

Codd's insight is easy to miss because it now looks obvious. Earlier database systems (hierarchical and network models) linked records with **pointers** — physical addresses, like the linked lists of [[Linked Lists]]. Fast, and brittle: the program had to *navigate* the pointers, and a change to storage broke it. Codd replaced pointers with **values**: a row in ORDER holds `CustomerID = C1`, and the link to the customer is nothing more than *the row in CUSTOMER whose primary key is C1*. No addresses, no navigation, no knowledge of how either table is stored. A query says *what* it wants ("orders and the customers who placed them") and the DBMS works out *how* — the knowledge-axis decoupling of [[Decouple and Recouple]], applied to data.

### The vocabulary, and what each word buys

- **Entity** — a real-world thing the database records: a customer, a plant, a bird sighting. It becomes a **table**.
- **Attribute** — one item of data about an entity: a name, a price. It becomes a **field** (column).
- **Record / tuple** — one entity instance: one row.
- **Primary key** — the field (or **composite** set of fields) whose value identifies exactly one row. Must be unique and never empty. A designer *chooses* it from the **candidate keys** — every field that *could* serve, such as a passport number or a student ID; the ones not chosen stay candidate keys. A **secondary key** is any field indexed for fast lookup without being unique — a surname column.
- **Foreign key** — a field in one table whose values are primary keys of another. *This is the relationship.* There is no other mechanism: to say "this order belongs to that customer" is to put the customer's key in the order's row.
- **Referential integrity** — the rule that a foreign key must point at a row that exists. Delete customer C1 while orders still say `C1` and the orders point at nothing; a DBMS either refuses the delete, or **cascades** it (deletes the orders too), or sets the key to null — but never leaves a dangling reference silently.
- **Indexing** — a separate lookup structure (a B+ tree, in [[Balanced Trees]]) on a field so that `WHERE CustomerID = 'C1'` finds the row in a few disk reads instead of scanning the table.

> [!tip] Reading an exam schema
> Cambridge writes a table as `NAME(PrimaryKey, Field, Field, …)` with the primary key underlined (or listed first when underlining is impossible). `PURCHASE_ITEM(PurchaseID, PlantName, Quantity)` with both first fields underlined is a **composite key** — and each half is also a foreign key. Read every schema you are given twice: once for the keys, once for what each foreign key says about the relationships.

## Relationships and the E-R diagram

Two tables can relate in three ways, and the diagram that documents the design — the **entity-relationship (E-R) diagram** — draws each entity as a box and each relationship as a line whose ends say *how many*: a single bar for **one**, a crow's foot for **many**.

- **One-to-one (1:1)** — each row on either side pairs with at most one on the other: a school and its head teacher. Rare; often a sign the two tables could be one.
- **One-to-many (1:M)** — the workhorse. One customer, many orders; one bird type, many sightings. **The foreign key goes on the many side**, because a row there has exactly one parent to point at.
- **Many-to-many (M:M)** — a purchase contains many plants; a plant appears in many purchases. *No table can hold this alone* — a foreign key can point at one parent, not a list of them — so the design **inserts a link table** whose rows are the pairs, with a composite primary key made of the two foreign keys. Every M:M in a finished design has become two 1:Ms.

![[relational-er-diagram.svg|860]]

The top diagram is the June 2023 Paper 11 schema; the bottom is November 2021 Paper 12's, where PURCHASE_ITEM is the link table. Once you have drawn a dozen of these, a pattern locks in: **find the foreign keys and the diagram draws itself** — each foreign key is one line, with the crow's foot at the table that holds it.

## Normalisation — one fact, one place

### The anomalies that make it necessary

Suppose the whole plant-shop business is one table: each row an order line, with the customer's name and city and the plant's cost copied into every row. It works until something changes:

- **Update anomaly** — Mei moves city. Her city is in every row she ever ordered; miss one and the table disagrees with itself.
- **Insertion anomaly** — a new plant arrives that nobody has ordered yet. There is no row to put its cost in, because rows are order lines.
- **Deletion anomaly** — Ana's only order is cancelled. Delete the row and Ana — her name, her city — vanishes with it.

All three have one cause: **a fact about a customer, or a plant, is stored in rows that are about orders.** Normalisation is the discipline of moving each fact into a table that is *about* the thing the fact describes. It runs in three numbered steps, each removing one kind of misplacement.

### The three forms

Start from the order sheet exactly as a shop would write it — one row per order, the items listed in a cell:

![[relational-normalisation-0nf.svg|620]]

**First Normal Form (1NF) — no repeating groups.** Every cell holds one value, and every row is identified by a key. The 0NF sheet had "Rose ×3, Lavender ×10" in one cell — a *list* inside a value. Split it into one row per item; the key becomes the pair (OrderID, Plant). Now every cell is atomic, and the question "how many roses were sold?" is a query instead of a text-parsing job.

![[relational-normalisation-1nf.svg|720]]

**Second Normal Form (2NF) — 1NF, and no partial dependencies.** A *partial dependency* is a non-key field that depends on only *part* of a composite key. In the 1NF table, `Customer` depends on `OrderID` alone (it does not care which plant), and `PlantCost` depends on `Plant` alone. Both are facts about half the key, stored once per full key — so the customer's name is repeated for every plant on the order. Move each to a table keyed by the half it depends on: ORDER(OrderID, Customer, City), PLANT(Plant, PlantCost), and the line table keeps only what depends on the whole key — the quantity. A table whose key is a single field is automatically in 2NF; partial dependency needs a composite key to exist.

![[relational-normalisation-2nf.svg|960]]

**Third Normal Form (3NF) — 2NF, and no non-key (transitive) dependencies.** A *transitive dependency* is a non-key field that depends on another non-key field rather than on the key. In ORDER(OrderID, Customer, City), the city depends on the *customer*, not on the order — change Mei's city and every one of her orders must change. Move the customer's own facts to CUSTOMER(CustomerID, Customer, City) and leave ORDER holding the foreign key. Now every non-key field in every table depends on **the key, the whole key, and nothing but the key** — William Kent's 1983 summary of the three forms, which is worth memorising *after* you can derive it, as a check rather than a recipe.

![[relational-normalisation-3nf.svg|880]]

> [!info] Why your 2NF examples keep landing in 3NF
> Anyone who has tried to teach this has met the same frustration: you fix the 1NF problem, you fix the partial dependencies, and the result is *already* in 3NF — there is never a table that is exactly 2NF to show. The reason is not bad luck. In most real tables the field that violates 3NF is welded to the field that violates 2NF: `City` depends on `Customer`, and `Customer` depends on half the key, so the moment you move `Customer` out *as an entity* — CUSTOMER(CustomerID, Name, City), the way any designer instinctively would — `City` goes with it and the transitive dependency never gets its own step. **Normalising by entities skips 2NF; normalising by the mechanical rule does not.** The walk above deliberately follows the rule: step 2 moves *exactly* the fields that depend on `OrderID` alone, into a table keyed by `OrderID`, and leaves ORDER(OrderID, Customer, City) — a genuine 2NF-not-3NF table, because `City → Customer → key` is a chain that the partial-dependency rule cannot see. If you want to *construct* one on purpose, the recipe is: every non-key field depends on the whole key, and one non-key field depends on another. SHIPMENT(OrderID, ProductID, Qty, WarehouseID, WarehouseCity) is the cleanest: the warehouse is chosen per order-line (whole key), but its city is a fact about the warehouse. That is exactly 2NF, and the examiner's "explain why these tables are not in 3NF" question is asking you to find the `WarehouseCity` in whatever they have given you.

> [!tip] Normalisation is decoupling — the join is recoupling
> [[Decouple and Recouple]] names the axis: a fact about the customer stored in the order's row is *coupled* to the order on the knowledge axis — the order "knows" the customer's city, and pays for it every time the city changes. Each normal form cuts one such coupling, moving the fact into the table that owns it. The **join** is the deliberate recoupling at read time: the facts come back together for the query, and nowhere else. And the denormalised document of [[NoSQL and Distributed Data]] is the *other* decision on the same axis — recouple at write time, permanently, because the read is worth more than the change. Once you see normalisation as a coupling decision rather than a ritual, "which normal form?" stops being a classification exercise and becomes the engineer's question: *who owns this fact, and who has to know when it changes?*

### How to normalise a given table — the exam procedure

1. **Find the repeating group.** Anything list-shaped in a cell, or numbered columns (`Item1, Item2, Item3`). Split into rows; extend the key. → 1NF.
2. **Look at the key.** Composite? Then for each non-key field ask *which part of the key does this depend on?* Fields that depend on a part move out, with that part as their key. → 2NF.
3. **Look at the non-key fields.** For each pair, ask *does this depend on the other rather than on the key?* Move the dependent one out, with the field it depends on as the new table's key; leave that field behind as a foreign key. → 3NF.
4. **Write every table as `NAME(Key, …)`, underline keys, and check each foreign key points at a primary key.** The examiner marks tables, keys and links separately.

## Worked examples — the real Paper 1 questions

### November 2024 Paper 13 Q4(c)(ii) — normalise BATCH

`BATCH(BatchID, Type, Flavour, Size, SellingPrice, EndDate)` with sample rows: KlV12 Plain Vanilla 1 2.20 12/12/2024 · BIV13 Plain Vanilla 1 2.20 02/02/2024 · … *The table is not normalised. Normalise it; give table definitions; identify keys. [4]*

*Tool: step 3 of the procedure — the trigger is two rows that agree on everything except the key and the date.* KlV12 and BIV13 are both "Plain Vanilla, size 1, ¥2.20"; only BatchID and EndDate differ. So Type, Flavour, Size and SellingPrice are facts about *the ice-cream product*, not about the batch — a non-key dependency (they depend on "which product this is", which is not the key). Move them out:

```
ICE_CREAM(IceCreamID, Type, Flavour, Size, SellingPrice)
BATCH(BatchID, IceCreamID, EndDate)
```

The scheme's four marks: a product table with an appropriate name · containing type, flavour, size, selling price · with a suitable primary key · a foreign key in BATCH linking to it. Note the invented key `IceCreamID` — when the facts you move out have no natural key, you make one.

### June 2024 Paper 11 Q6(a) — a 3-table design to 3NF

A quiz website: users pick a unique username and give an email; all must be over 16; a new quiz each day, stored as a text file with a date; each user gets a score per quiz; scores give a rating. *Create a 3-table design normalised to 3NF, format `TableName(PrimaryKey, Field, …)`. [6]*

*Tool: entities first, then the relationship's shape.* Two entities are named outright — USER and QUIZ. "Each user gets a score for each quiz" is a fact about a *pair* (user, quiz): a many-to-many, so the third table is the link table with the score on it.

```
USER(Username, Email, DateOfBirth, Rating)
QUIZ(QuizID, Date, Filename)
USER_QUIZ(Username, QuizID, Score)
```

The scheme gives one mark each for: USER keyed on the username · with email, date of birth/age and rating · QUIZ keyed on ID, date or filename · with the remaining fields · a link table holding user, quiz and score · with an appropriate primary key · and foreign keys matching the other two tables' primary keys. Two things students drop: the *rating* belongs to the user (it is derived from scores but stored per user), and the link table's key is the *pair* — `Username` alone would allow one score per user for all quizzes.

### June 2023 Paper 11 Q2(b)(i) — find the foreign keys

`BIRD_TYPE(BirdID, Name, Size)` · `BIRD_SEEN(SeenID, BirdID, Date, Location, PersonID)` · `PERSON(PersonID, FirstName, LastName, EmailAddress)`. *Identify two foreign keys and the table each is found in. [2]*

*Tool: a foreign key is a primary key appearing in another table.* `BirdID` is BIRD_TYPE's key and appears in BIRD_SEEN; `PersonID` is PERSON's key and appears in BIRD_SEEN. Both foreign keys are in **BIRD_SEEN** — the many side of both relationships, exactly as the E-R diagram above shows. The question asks *where the foreign key is found*, not what it references; read the column heading.

### November 2025 Paper 12 Q4(a) — describe the relationship

`CONTAINER(ContainerID, Type, Weight, OwnerName, ShipID)` · `SHIP(ShipID, Type, Capacity, ShipName)`. *Describe the relationship between the two tables, referring to the primary and foreign keys. [2]*

The two marks are two sentences: *the relationship is one-to-many, SHIP to CONTAINER* (one ship carries many containers), and *the primary key ShipID in SHIP is linked to the foreign key ShipID in CONTAINER.* Name the direction, name both keys, name the tables — a description that says "they share ShipID" gets one mark.

### November 2021 Paper 12 Q6(a)(i) — which stage does what

*Tick the stage for each task: remove partial key dependencies · remove repeating groups · remove non-key dependencies.* The answers are 1NF→2NF, 0NF→1NF, 2NF→3NF respectively — the three steps of the procedure in a different order, which is the whole point of the question. If you learned the forms as a *sequence of removals* rather than three definitions, this is a ten-second question.

## The DBMS — what the software actually provides

The tables are the design. The DBMS is the running program that owns them, and 9618 §8.2 lists what it provides against the file-based failures:

| DBMS feature | What it is | The failure it answers |
|---|---|---|
| **Data dictionary** | the database's *metadata*: table names, field names, data types, validation rules, keys, relationships — data about the data | program–data dependence: the structure lives here, not in any program |
| **Logical schema** | the platform-independent design — the entities, attributes and relationships (the E-R diagram is its picture), separate from how the bytes are stored | one design, any storage; the physical layout can change under it |
| **Data modelling** | the tools for building that schema | design before data |
| **Data integrity** | the rules that keep the data consistent: referential integrity, validation on entry, cascading updates and deletes | inconsistency |
| **Data security** | access rights per user or group (who may read, who may write), plus **backup** and recovery procedures | files had no shared access control |
| **Developer interface** | the tools a designer uses to create and alter tables, set up relationships, build input forms and reports, and inspect the data by running queries | building without writing a whole program |
| **Query processor** | the engine that takes a query in [[SQL]], checks it against the dictionary, plans how to answer it (which index, which join order), and runs it | asking a question nobody wrote a program for |

The exam answers are short. *Data dictionary:* "data about the data // metadata" plus one example (field names, data types, keys). *Data integrity:* "methods of making sure the data is consistent" plus one example (enforcing referential integrity; validation rules). *Developer interface:* two of — create/modify tables, set up relationships, build forms and reports, run queries to inspect data.

## Where this is the working tool

**Your phone, four hundred times over.** SQLite — a relational engine about the size of a photo, written by D. Richard Hipp in 2000 and placed in the public domain — is compiled into every iOS and Android device, every browser, most desktop applications. With several billion phones each holding hundreds of SQLite files, its authors estimate over a trillion databases in active use, which would make it the most widely deployed software component in the world. When [[File Handling]] says that most apps which "save instantly" are not managing files at all but writing rows to an embedded database, this is the database. Every message you have ever sent is a row.

**Under the web.** PostgreSQL and MySQL/MariaDB sit under most of the sites you use; Oracle, SQL Server and Db2 under most banks, airlines and governments. The relational model has been the default home of *the data that must be right* — money, bookings, records — for fifty years, and the reason is one word the exam will not ask for and every engineer lives by:

**Transactions.** A bank transfer is two writes: subtract here, add there. A DBMS wraps them in a **transaction** that is **atomic** (both happen or neither), **consistent** (the rules hold after it as before), **isolated** (two transfers running at once cannot see each other half-done) and **durable** (once confirmed, a power cut cannot undo it) — ACID, the term coined by Härder and Reuter in 1983. This is the *deliberate coupling* [[Decouple and Recouple]] describes: the two writes are welded so the world can never observe one without the other. The write-ahead log that makes durability true is the reason a database survives a crash that would corrupt a plain file.

**Indexes.** `WHERE CustomerID = 'C1'` on a table of a hundred million rows does not scan a hundred million rows. It walks a B+ tree three or four levels deep — [[Balanced Trees]] shows the structure — and the "secondary key" of the terminology table is exactly a field you have built such a tree over.

## Hands-on — play with SQLite, today

Every idea on this card can be touched in ten minutes, without installing anything, because the engine is already on your machine.

1. **The command line.** macOS and most Linux ship the `sqlite3` shell; on Windows it is a single download from sqlite.org. Then:

   ```bash
   sqlite3 birds.db
   ```

   creates a database file and drops you into a prompt where every statement in [[SQL]] runs as typed. `.tables` lists the tables, `.schema BIRD_SEEN` prints a table's DDL back at you — the data dictionary, in the raw — and `.quit` leaves. `EXPLAIN QUERY PLAN SELECT …` shows whether a query walked an index or scanned the table, which is the "indexing" bullet of §8.1 made visible.

2. **From Python.** The three-line setup at the top of [[SQL]]; the script beside that card builds every schema on this page and runs every paper's query. Change a row, re-run, watch the answer move.

3. **A real one.** Your browser's history is a SQLite database. Copy Chrome's `History` file (on a Mac it lives under `~/Library/Application Support/Google/Chrome/Default/`; Firefox's is `places.sqlite` in its profile folder), open the copy with `sqlite3`, and run `.tables` — then `SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT 10;`. You are reading, with the language on this card, a table that a program you use every day writes without telling you. Every phone app's data folder holds more of them.

4. **A GUI, if you prefer one.** *DB Browser for SQLite* (free, open source) opens any `.db` file, shows the tables and their keys, and has a tab that runs SQL — the *developer interface* of §8.2, in a form you can point at.

The exercise that teaches normalisation better than any question: type the 0NF order sheet into one table, try to write the query "total roses sold", fail, and then build the 3NF version and write it in one line.

## Misconceptions

1. **"A database is a big spreadsheet."** A spreadsheet is one table with no keys, no types, no relationships and no rules; you can type a name into a date column. A relational database is several tables *bound by keys and rules*, and the rules are enforced by software, not by care.
2. **"The primary key is the first column."** It is the field that identifies a row uniquely and never changes; Cambridge lists it first by convention. In the 0478 pheasant question, `Species` *could* be the key — the scheme accepts it — but a six-character `SpeciesID` is *better* because it is short, always unique and easy to validate. Names make bad keys: they repeat, they get misspelt, they change.
3. **"Normalisation saves space."** It usually costs space. It buys *one place to change each fact*; see the callout above.
4. **"A foreign key has to be unique."** The opposite: a foreign key on the many side repeats freely — every order by Mei holds `C1`. The uniqueness is on the primary key it points to.
5. **"Many-to-many can be stored with a foreign key on one side."** It cannot; one row can point at one parent. The link table is not optional — its absence is the commonest lost mark on design questions.
6. **"2NF is about single-field keys."** A table with a single-field primary key is in 2NF automatically; partial dependency needs a composite key to exist. The 2NF question is therefore only ever asked about tables with composite keys.

## Beyond syllabus

### The 1970 paper, and the twelve years it took

Codd's paper was mathematics — relations in the set-theoretic sense, an algebra of operations on them — published inside IBM, whose best-selling database (IMS, hierarchical, pointer-based) it implicitly declared obsolete. IBM's own System R project (1974–79) built the first working implementation and invented the language that became [[SQL]]; a small company reading the papers shipped a commercial relational database in 1979, two years before IBM, and called itself Oracle. The model won not because it was elegant but because *program–data independence* turned out to be the whole cost of software: a database whose structure could change without rewriting every program was cheaper to own by a large margin. Codd received the Turing Award in 1981.

### The join is the price, and the price is why everything else exists

Every table in 3NF is a promise that reading anything real will require a join. For a bank, a bookings system, a school, that is the right trade — the data changes constantly and must be right. For a social feed read a billion times a day and written once, it is the wrong one, and by 2006 the largest websites had begun building stores that keep each record *whole*, denormalised, spread across thousands of machines, giving up joins and often giving up ACID. That is [[NoSQL and Distributed Data]]. Read this card first: every design there is an answer to a cost this card just named.

### Records, and why the language already knew

The row of a table is the **record** of [[User-Defined Data Types]] — a fixed set of named, typed fields — and a table is an array of records with a key. A language's record type and a database's table are the same abstraction seen from two sides, which is why an `ORDER` row maps so cleanly onto a Python dataclass or a Java class, and why the mapping tools that do it (ORMs) exist in every language.

## Exam Notes

### Cambridge 9618 (§8.1 + §8.2 — AS Paper 1)

- **§8.1** wants: the **limitations of the file-based approach** (redundancy, inconsistency, program–data dependence — three named, with a sentence each); the **features of a relational database that address them**; the full **terminology** list (entity, table, record, field, tuple, attribute, primary/candidate/secondary/foreign key, 1:1 / 1:M / M:M, referential integrity, indexing); **E-R diagrams** from a given schema (one mark per relationship, crow's feet on the many side); the **normalisation process** to 1NF, 2NF, 3NF; **explain why a given set of tables is or is not in 3NF**; and **produce a normalised design** from a description, sample data, or given tables.
- **§8.2** wants the DBMS features (data dictionary, data modelling, logical schema, data integrity, data security incl. backup and access rights) and the two tools *in practice* — the developer interface and the query processor. The answers are the one-liners in the DBMS table above; give a definition **and** an example, because most schemes split the marks that way.
- Question shapes, from the papers: a schema → foreign keys (2) · relationship description (2) · E-R diagram (3) · normalise a given table (4) · design 3 tables to 3NF (6) · tick-the-stage (2) · match normal forms to definitions (1) · DBMS feature definitions (2–4 each).

### Cambridge 0478 (§9 — Paper 2)

- **Single-table** databases only: define a table from given storage requirements (fields, records, **validation**); suggest **basic data types** — *text/alphanumeric, character, Boolean, integer, real, date/time* (the scheme wants each type used once when it says "each must be different"); identify a suitable **primary key** and explain why a name is unsuitable (repeats, misspelt); count records and fields in a shown extract. The SQL half of §9 is [[SQL]].
- No relationships, no foreign keys, no normalisation at IGCSE — but a student who has met the 1:M idea here writes better single-table answers, because "why is Species a poor key?" is a question about uniqueness.

### IB Computer Science (A3.1 + A3.2)

- **A3.1 Database fundamentals** and **A3.2 Database design** carry the relational model, keys, E-R modelling and normalisation to 3NF for both SL and HL — this card. **A3.3** (SQL) is [[SQL]]; **A3.4** (alternative databases and data warehouses, HL only) is [[NoSQL and Distributed Data]].

### Not examined on…

- **AP Computer Science A** — no databases at all; the course is Java program design.

## Quick reference

| Ask | Answer in one line |
|---|---|
| Why not files? | redundancy → inconsistency → program–data dependence; no shared control, no ad-hoc queries |
| Relationship mechanism | foreign key on the **many** side = primary key on the one side |
| M:M | link table with a composite key of the two foreign keys |
| 1NF | no repeating groups; atomic cells; a key |
| 2NF | 1NF + no partial dependencies (non-key field on part of a composite key) |
| 3NF | 2NF + no non-key (transitive) dependencies |
| Kent's check | every non-key field depends on the key, the whole key, nothing but the key |
| Data dictionary | metadata: table/field names, types, validation, keys, relationships |
| Referential integrity | every foreign key points at an existing row; cascade or refuse |
| Good primary key | unique, never null, never changes, short — usually an invented ID |

## Connections

- **Parents:**
   - [[File Handling]] — the file-based world this card leaves; its closing line ("most apps are writing rows to an embedded database") is this card's opening.
   - [[User-Defined Data Types]] — a row is a record; a table is an array of them with a key.

- **Children:**
   - [[SQL]] — the language the query processor speaks: DDL to build these tables, DML to ask them questions; every worked schema here reappears there as runnable code.
   - [[NoSQL and Distributed Data]] — what the largest systems built when the join and ACID became the cost; every design there is an answer to a trade named here.

- **Uses:** [[Balanced Trees]] — the B+ tree behind every index and the "secondary key" of the terminology list; [[Hash Tables]] — the other index structure, and the join algorithm's workhorse; [[Decouple and Recouple]] — the transaction as deliberate coupling, and value-linking as the knowledge-axis decoupling of data from programs.

- **Related:** [[Operating Systems]] — the DBMS runs on the OS's file system and, for durability, has to know exactly which of the OS's write buffers have actually reached the disk; [[Linked Lists]] — the pointer-linking that Codd's value-linking replaced.

- **Misconception traps cleared:** a database is a big spreadsheet; the primary key is the first column; normalisation saves space; foreign keys must be unique; M:M can be stored on one side; 2NF applies to single-field keys.

---
chinese: 结构化查询语言 (jiégòuhuà cháxún yǔyán) / SQL
prerequisites:
  - "[[Relational Databases]]"
leads_to:
  - "[[NoSQL and Distributed Data]]"
  - "[[Data Security]]"
  - "[[Programming Paradigms]]"
tags:
  - subject/computer-science
  - domain/databases
  - domain/programming
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-9-4
  - syllabus/9618-8-3
  - syllabus/IB-CS-A3-3
  - type/deep
  - misconception/sql-is-read-top-to-bottom
  - misconception/where-filters-groups
  - misconception/count-star-equals-count-field
---

# SQL 结构化查询语言

> *A language that has not changed its shape since 1974, that most programmers never formally learn, and that more of them use every day than any other: a query is a sentence in the only programming language where you say what you want and never how.*

## Definition

### Formal

**SQL** (Structured Query Language) is the industry-standard language a **Database Management System** understands. It has two halves. The **Data Definition Language (DDL)** creates and changes the *structure* of the database — databases, tables, fields, keys — with `CREATE`, `ALTER` and `DROP`. The **Data Manipulation Language (DML)** reads and changes the *data* inside that structure — `SELECT`, `INSERT`, `UPDATE`, `DELETE`. Every change to the structure goes through the DDL and every change to the data goes through the DML; there is no other door, which is how the DBMS keeps its data dictionary true and its rules enforced.

SQL is **declarative**: a query states the result wanted — which columns, from which tables, under which conditions, in which order — and the DBMS's query processor decides how to compute it.

### Intuitive

Search a shopping app for umbrellas under ¥50, cheapest first. You have just written a query — the app turned it into `SELECT … FROM Product WHERE Category = 'umbrella' AND Price < 50 ORDER BY Price`. SQL is that sentence made exact: **what** you want (`SELECT`), **from where** (`FROM`), **under what condition** (`WHERE`), **in what order** (`ORDER BY`), **totalled how** (`GROUP BY`, `SUM`, `COUNT`, `AVG`). You never say "loop through the products"; the database works that out, and if there is an index it will not loop at all.

### 中文锚点

你在淘宝搜"雨伞"，勾"50 元以下"，点"按价格从低到高"。你刚刚写了一条 SQL，只是没看见它：

```sql
SELECT Name, Price FROM Product WHERE Category = '雨伞' AND Price < 50 ORDER BY Price;
```

这就是整门语言的骨架——**要什么**（SELECT 哪几列）、**从哪拿**（FROM 哪张表）、**什么条件**（WHERE）、**怎么排**（ORDER BY）、**怎么汇总**（GROUP BY 加 SUM / COUNT / AVG）。它是**声明式**的：你说要什么，不说怎么找——循环、索引、先查哪张表，都是数据库自己的事。SQL 分两半：**DDL**（数据定义语言）造结构——`CREATE TABLE` 建表、`ALTER TABLE` 改表、`PRIMARY KEY` / `FOREIGN KEY` 定钥匙；**DML**（数据操作语言）动数据——`SELECT` 查、`INSERT INTO` 加、`UPDATE` 改、`DELETE FROM` 删。考试考的就是这十来个词，而且**你现在就能跑**：Python 自带 `sqlite3`，三行代码建库，这张卡上每一条语句都在旁边那个脚本里真的运行过，这里的输出就是这些语句真正跑出来的。一条查询真正的执行顺序**不是从上往下**：数据库先看 `FROM`（拿哪张表），再 `WHERE`（留哪些行），再 `GROUP BY`（怎么分组），再 `SELECT`（算哪几列），最后 `ORDER BY`（排序）——记住这个顺序，"为什么 WHERE 里不能用 SUM"这类问题就自己解开了。最后一件真实世界的事：把用户输入直接拼进 SQL 字符串，是全世界最常见的安全漏洞之一（**SQL 注入**）；正确写法是用 `?` 占位符把数据和语句分开——这也是 A Level §6 会考到的内容。

| English | 中文 | 一句话 |
|---|---|---|
| DDL | 数据定义语言 | 造结构：CREATE / ALTER / DROP |
| DML | 数据操作语言 | 动数据：SELECT / INSERT / UPDATE / DELETE |
| Query | 查询 | 一条 SELECT 语句：要什么、从哪拿、什么条件 |
| Clause | 子句 | 一条语句里的一段：WHERE 子句、ORDER BY 子句 |
| Aggregate function | 聚合函数 | 把很多行算成一个数：SUM / COUNT / AVG |
| Join | 连接 | 用外键 = 主键把两张表的行配对 |
| Nested query | 嵌套查询 | 括号里的 SELECT，结果给外面的 WHERE 用 |
| Parameterised query | 参数化查询 | 用 `?` 占位，让数据永远不能变成代码 |

---

## Run it, don't read it

Every statement on this card was executed by the script beside it, `sql-worked-examples.py`, against SQLite — the engine inside every phone, and built into Python. The whole setup is three lines:

```python
import sqlite3
db = sqlite3.connect(":memory:")          # or a filename, to keep it
cur = db.cursor()
cur.execute("PRAGMA foreign_keys = ON;")  # SQLite ships with referential integrity OFF
```

After that, `cur.execute("SELECT …")` runs a query and `cur.fetchall()` returns the rows as Python tuples. Paste a past-paper schema, run the paper's query, and compare with the mark scheme: it is the cheapest form of exam practice there is, and the one where you cannot fool yourself.

## DDL — building the structure

### CREATE

```sql
CREATE DATABASE Birds;

CREATE TABLE BIRD_TYPE(
    BirdID  CHAR(4)     NOT NULL,
    Name    VARCHAR(20),
    Size    VARCHAR(6),
    PRIMARY KEY (BirdID)
);
```

Every field gets a **data type**. Cambridge's list, which is close to the standard's: `CHARACTER`/`CHAR(n)` (fixed length — a four-character ID), `VARCHAR(n)` (up to *n* characters — a name), `BOOLEAN`, `INTEGER`, `REAL`, `DATE`, `TIME`. `NOT NULL` is a **constraint** — a rule the DBMS enforces on entry — and the primary key is declared as one. A foreign key is declared the same way, naming the table and field it references:

```sql
CREATE TABLE BIRD_SEEN(
    SeenID   INTEGER NOT NULL,
    BirdID   CHAR(4),
    Date     DATE,
    Location VARCHAR(30),
    PersonID VARCHAR(6),
    PRIMARY KEY (SeenID),
    FOREIGN KEY (BirdID)   REFERENCES BIRD_TYPE(BirdID),
    FOREIGN KEY (PersonID) REFERENCES PERSON(PersonID)
);
```

That `FOREIGN KEY … REFERENCES` line is [[Relational Databases]]' *referential integrity*, made executable. With it in place, the script's last experiment — inserting a sighting of `BirdID '9999'`, a bird that does not exist — is refused by the engine with `FOREIGN KEY constraint failed`. The rule lives in the database, not in any program.

### ALTER and DROP

```sql
ALTER TABLE PURCHASE ADD OrderDate DATE;                                   -- new field
ALTER TABLE EVENT ADD FOREIGN KEY (PlayerID) REFERENCES PLAYER(PlayerID);  -- new link
DROP TABLE PURCHASE;                                                       -- gone, data and all
```

`ALTER TABLE … ADD` is the DDL question Cambridge asks most: one mark for the `ALTER TABLE` clause, one for a sensibly named field with a sensible type. (SQLite, unusually, cannot *add* a foreign key to an existing table — MySQL and PostgreSQL can; write the standard form in the exam.)

## DML — reading and changing the data

### The anatomy of SELECT

```sql
SELECT   BIRD_TYPE.Size, COUNT(BIRD_TYPE.BirdID) AS NumberOfBirds
FROM     BIRD_TYPE INNER JOIN BIRD_SEEN ON BIRD_TYPE.BirdID = BIRD_SEEN.BirdID
WHERE    BIRD_SEEN.PersonID = 'J_123'
GROUP BY BIRD_TYPE.Size
ORDER BY NumberOfBirds DESC;
```

Read it in the order the database *executes* it, which is not top to bottom:

1. **`FROM`** — which table(s). With two tables, the **join** pairs rows where foreign key equals primary key. Two spellings are accepted everywhere: `FROM A INNER JOIN B ON A.k = B.k` and the older `FROM A, B WHERE A.k = B.k`. Cambridge schemes give both.
2. **`WHERE`** — keep only the rows that satisfy the condition. Conditions combine with `AND`, `OR`, `NOT`; compare with `=`, `<>`, `<`, `>`, `<=`, `>=`; strings in quotes.
3. **`GROUP BY`** — collapse the surviving rows into one row per distinct value of the named column(s).
4. **`SELECT`** — now compute the output columns. Plain columns must be ones you grouped by; **aggregate functions** — `SUM(x)`, `COUNT(x)`, `AVG(x)` — compute one value per group (or over all rows, if there is no `GROUP BY`). `AS` names the result column.
5. **`ORDER BY`** — sort the finished rows, `ASC` (default) or `DESC`.

That order answers the questions students actually ask. *Why can't I write `WHERE COUNT(...) > 2`?* Because `WHERE` runs before the groups exist; a condition on an aggregate goes in `HAVING`, which runs after `GROUP BY`. *Why must every non-aggregated `SELECT` column appear in `GROUP BY`?* Because after grouping, a column with different values inside one group has no single value to show. *Why does `ORDER BY` know about the alias `NumberOfBirds`?* Because it runs last, after `SELECT` has made it.

The query above, on the script's data, returns:

```
Size    NumberOfBirds
Large   2
Medium  1
Small   1
```

### INSERT, UPDATE, DELETE

```sql
INSERT INTO BIRD_SEEN VALUES (6, '0035', '2023-05-01', 'Wood', 'A_007');
UPDATE BIRD_SEEN SET Location = 'Old Wood' WHERE SeenID = 6;
DELETE FROM BIRD_SEEN WHERE SeenID = 6;
```

`INSERT INTO table VALUES (…)` supplies one value per field in table order (or `INSERT INTO table (f1, f2) VALUES (…)` to name them). `UPDATE … SET … WHERE` and `DELETE FROM … WHERE` change or remove **every row the `WHERE` matches** — leave the `WHERE` off and you have updated or deleted the whole table, which is the most expensive typo in the language.

### Nested queries

A `SELECT` inside another's `WHERE`, in brackets, evaluated first:

```sql
SELECT DISTINCT PersonID
FROM BIRD_SEEN
WHERE BirdID IN (SELECT BirdID FROM BIRD_TYPE WHERE Size = 'Large');
```

*Who has seen a large bird?* The inner query makes the list of large-bird IDs; the outer keeps sightings whose bird is in that list; `DISTINCT` removes repeats. Result on the script's data: `J_123`. Most nested queries can be rewritten as joins, and the query processor often does.

## Worked examples — the real papers, run

### June 2023 Paper 11 Q2(b)(iii) — define a table [4]

Sample rows of BIRD_TYPE are shown (BirdID `0123`, Name `Blackbird`, Size `Medium` …) and the allowed types listed (character, varchar, Boolean, integer, real, date, time). *Write the SQL to define the table.*

*Tool: read the sample data for the types — the trigger is a four-digit ID with a leading zero.* `0123` is not an integer (the zero would vanish); it is a fixed four-character code, so `CHAR(4)`. Names vary in length: `VARCHAR`. The scheme's four marks: `CREATE TABLE` with opening and closing brackets · BirdID as CHAR/VARCHAR · Name and Size as VARCHAR/CHAR · BirdID as primary key. The DDL block at the top of this card is the answer, and the script ran it.

### June 2023 Paper 11 Q2(b)(iv) — complete the join [5]

*Return the number of birds of each size seen by person J_123* — five blanks in a comma-join query. The completed statement:

```sql
SELECT BIRD_TYPE.Size, COUNT(BIRD_TYPE.BirdID) AS NumberOfBirds
FROM BIRD_TYPE, BIRD_SEEN
WHERE BIRD_SEEN.PersonID = "J_123"
AND BIRD_TYPE.BirdID = BIRD_SEEN.BirdID
GROUP BY BIRD_TYPE.Size;
```

One mark per blank: `COUNT`, `BIRD_SEEN`, `BIRD_SEEN.PersonID`, `BIRD_SEEN.BirdID`, `GROUP BY`. The condition `BIRD_TYPE.BirdID = BIRD_SEEN.BirdID` *is* the join; without it the two tables multiply into every pairing. Run: `Large 2, Medium 1, Small 1`.

### November 2021 Paper 12 Q6(c) — SUM, then ALTER [4 + 3]

`PURCHASE_ITEM(PurchaseID, PlantName, Quantity)`. *(i) Total number of items in purchase 3011A:*

```sql
SELECT SUM(Quantity)
FROM PURCHASE_ITEM
WHERE PurchaseID = "3011A";
```

Four marks, one per blank. Note the quotes: `3011A` is text. Run on the script's rows (3 roses + 10 lavender): `13`. *(ii) Add a field to PURCHASE for the order date:* `ALTER TABLE PURCHASE` · `ADD OrderDate` · `DATE` — three marks, three bullets.

### June 2024 Paper 11 Q6(c) — a foreign key, then a count per group [2 + 3]

EVENT(PlayerID, EventID, Category, Points) with sample rows; PLAYER has primary key PlayerID. *(i) Link the foreign key:*

```sql
ALTER TABLE EVENT
ADD FOREIGN KEY (PlayerID) REFERENCES PLAYER(PlayerID);
```

*(ii) The number of events each player has completed:*

```sql
SELECT PlayerID, COUNT(EventID)
FROM EVENT
GROUP BY PlayerID;
```

*Tool: "each player" → `GROUP BY PlayerID`; "number of" → `COUNT`.* The scheme's three marks are exactly those two words plus selecting PlayerID. Run on the paper's six sample rows: `000123 → 3, 000124 → 1, 000125 → 2` — which you can check by eye against the table in the question, and should.

### November 2025 Paper 12 Q4(c) — count across a join [4]

CONTAINER(…, ShipID) and SHIP(ShipID, …, ShipName). *The number of containers on the ship named Caledonia.* The name is in SHIP; the containers are in CONTAINER; so a join is unavoidable:

```sql
SELECT COUNT(ContainerID)
FROM CONTAINER INNER JOIN SHIP ON CONTAINER.ShipID = SHIP.ShipID
WHERE ShipName = "Caledonia";
```

Marks: `SELECT COUNT` · correct tables · the join · the name condition. The scheme prints both join spellings as full-credit answers. Run: `3`.

### November 2024 Paper 13 Q4(b) — a date range [3]

SALE(SaleID, BatchID, CustomerID, Quantity, Date). *Total quantity sold to customer 0034E in 2023.*

```sql
SELECT SUM(Quantity)
FROM SALE
WHERE CustomerID = "0034E"
AND Date >= #01/01/2023# AND Date <= #31/12/2023#;
```

That is the scheme's answer, and the `#…#` date literals are Microsoft Access syntax — Cambridge's reference dialect. SQLite, MySQL and PostgreSQL write `'2023-01-01'`; the script uses that and returns `25`. Write either in the exam; the marks are for `SUM`, the customer condition, and the `AND` with the date bounds.

### IGCSE 0478 — single-table queries

**November 2024 Paper 23 Q11**, BuildStock(MtNo, Name, InStock, WeightKg, PricePerBag, NumberBags), eleven rows shown. *(a) Write the output of:*

```sql
SELECT MtNo, Name
FROM BuildStock
WHERE WeightKg = 75
ORDER BY PricePerBag;
```

Two rows weigh 75 kg — MT06 Cobbles at 67.35 and MT12 Pebbles large at 62.75 — and `ORDER BY PricePerBag` (ascending by default) puts the cheaper first: **MT12 Pebbles large, then MT06 Cobbles.** Three marks: each line, and the order. Students lose the order mark by copying the table's row order. *(b) Only the names of materials that are out of stock:* `SELECT Name FROM BuildStock WHERE InStock = FALSE` — and part (ii) asks how a *different field* gives the same answer: `WHERE NumberBags = 0`. The script confirms both return Red sand, Cement, Cobbles.

**November 2023 Paper 23 Q9**, PheasantList — *(c) output of `SELECT Species, Description FROM PheasantList WHERE NumberBirds > 6`:* two rows, True silver and Brown eared (7 and 9 birds; `>` excludes 6). *(d) Species that are breeding and had no young this year:* `SELECT Species FROM PheasantList WHERE Breeding = TRUE AND Young = 0` — four marks, one per clause plus the `AND`. Run: Japanese green, Mikado, Himalayan monal, Golden.

**November 2025 Paper 21 Q1** is the vocabulary as a matching exercise: *identifies the table* → `FROM`; *sets the condition* → `WHERE`; *sorts the results* → `ORDER BY`; *returns the number of records* → `COUNT` (with `SUM` the distractor). Four marks for four lines — the cheapest marks on the paper for anyone who has run a query.

## Where this is the working tool

**Everywhere there is data.** SQL is the one language a data scientist, a backend engineer, a business analyst, a biologist with a spreadsheet that outgrew Excel and a mobile-app developer all write. It has survived every language fashion since 1974 because it is not really a programming language — it is a way of *stating a question about tables*, and tables are how the world keeps records. `pandas` in Python, `dplyr` in R and every spreadsheet's pivot table are SQL's `GROUP BY` wearing other clothes.

**Inside the app.** The three-line SQLite snippet above is, without exaggeration, how most desktop and mobile software stores its state — messages, settings, caches, histories. When [[File Handling]] warns that files are hard to get right, the industry's answer was to stop writing files and start writing rows.

**The injection attack.** Build a query by pasting user input into a string —

```python
cur.execute("SELECT * FROM USER WHERE Name = '" + name + "'")   # NEVER
```

— and a user who types `x' OR '1'='1` has rewritten your query to return every user; one who types `'; DROP TABLE USER; --` has deleted the table. **SQL injection** has been at or near the top of every list of web vulnerabilities for twenty years, and 9618 §6.1 names it as a threat. The fix is not cleverness but separation: a **parameterised query** sends the statement and the data down different channels, so data can never be read as code.

```python
cur.execute("SELECT * FROM USER WHERE Name = ?", (name,))       # always
```

[[Data Security]] carries the threat model; the habit belongs here, on the first day you write a query with a variable in it.

## Misconceptions

1. **"A query is read top to bottom."** It is *written* SELECT-first and *executed* FROM-first (FROM → WHERE → GROUP BY → SELECT → ORDER BY). Every "why can't I…" about aggregates and aliases dissolves once the execution order is known.
2. **"`WHERE` can filter on a total."** `WHERE` sees rows, before grouping. A condition on `SUM` or `COUNT` is a `HAVING` clause, after `GROUP BY`.
3. **"`COUNT(*)` and `COUNT(field)` are the same."** `COUNT(*)` counts rows; `COUNT(field)` counts rows where that field is not null. Same on clean data, different on real data.
4. **"Two tables in `FROM` joins them."** `FROM A, B` alone produces every pairing of rows (the Cartesian product). The join is the *condition* `A.key = B.key` — in `WHERE` or after `ON`. Forgetting it multiplies the answer.
5. **"`ORDER BY` defaults to descending because the big number should come first."** The default is ascending. The 0478 output question above is marked on exactly this.
6. **"Quotes don't matter."** Text and dates are quoted; numbers are not. `PurchaseID = 3011A` is a syntax error; `= "3011A"` is the answer. Cambridge accepts double quotes; standard SQL uses single — both are fine in the exam, and the script uses single because SQLite prefers it.
7. **"UPDATE and DELETE act on one row."** They act on every row the `WHERE` matches, and on every row if there is no `WHERE`.

## Beyond syllabus

### 1974, and why nothing replaced it

Donald Chamberlin and Raymond Boyce designed SEQUEL at IBM's San José laboratory in 1974 as the query language for System R, the first working relational database — the name shortened to SQL after a trademark clash. Standardised by ANSI in 1986, it has absorbed forty years of additions (window functions, recursive queries, JSON) without changing the five-clause skeleton. Attempts to replace it — object databases in the 1990s, the first wave of [[NoSQL and Distributed Data]] in the 2000s — mostly ended with the challenger *adding SQL*: the stores that dropped the language have largely grown a query language that looks like it.

### The query processor is a compiler

`SELECT` is compiled. The query processor parses the statement, checks every name against the data dictionary, then chooses a **plan**: which index to walk, which table to read first, whether to hash-join or sort-merge ([[Hash Tables]] and [[Sorting]] are both in there), how to order the filters. Two plans for the same query can differ by a factor of a thousand, and a real engine estimates each one's cost from statistics about the data before running the cheapest. Typing `EXPLAIN` before a query in any major database shows the plan it chose — the closest thing databases have to [[Assembly Language]]'s "reading the compiler's output".

### Declarative, and what that buys

You never told the database to loop. That is not a convenience; it is the reason the same query can run on a laptop or on a thousand-machine cluster unchanged — the *how* was never in the statement, so the engine is free to change it. [[Decouple and Recouple]] would call this knowledge-axis decoupling; [[Program Design]]'s modules are the same idea inside a program. Declarative languages are a 9618 §20.1 paradigm in their own right ([[Declarative Programming]]), and SQL is the one every student has already used.

## Exam Notes

### Cambridge 9618 (§8.3 — AS Paper 1)

- Know **that** the DBMS does all structure changes through DDL and all data work through DML, and that SQL is the industry standard for both — one-mark statements that appear as fill-the-gap questions.
- **DDL to write:** `CREATE DATABASE`, `CREATE TABLE` with the seven types (CHARACTER, VARCHAR(n), BOOLEAN, INTEGER, REAL, DATE, TIME), `PRIMARY KEY (field)`, `FOREIGN KEY (field) REFERENCES Table(Field)`, `ALTER TABLE … ADD`. Marks are per clause; brackets count.
- **DML to write**, on at most two tables: `SELECT … FROM`, `WHERE`, `ORDER BY`, `GROUP BY`, `INNER JOIN`, `SUM`, `COUNT`, `AVG`; `INSERT INTO`, `DELETE FROM`, `UPDATE`. Nested queries appear as "understand a given statement".
- Scheme conventions worth knowing: double quotes around text are accepted; `#dd/mm/yyyy#` is the reference dialect's date literal; the comma-join and `INNER JOIN` forms both earn full credit; a missing `;` is never penalised.
- The SQL-injection threat is **§6.1**, not §8 — but the parameterised-query habit belongs with the first query you write.

### Cambridge 0478 (§9 — Paper 2)

- **Single table only.** Read, understand and *complete* scripts using `SELECT`, `FROM`, `WHERE`, `ORDER BY` (ascending / descending), `SUM`, `COUNT`, `AND`, `OR`; and **identify the output** of a given statement against a shown table. Output questions mark each row *and* the order. The keyword-matching question (N25 P21 Q1) is a recurring opener.
- No joins, no `GROUP BY`, no DDL, no `INSERT`/`UPDATE`/`DELETE` at IGCSE.

### IB Computer Science (A3.3 Database programming)

- SQL for both SL and HL: table creation, `SELECT` with conditions, ordering and aggregation, joins across related tables, and data modification — the 9618 set, with A3.4's alternative databases (HL) in [[NoSQL and Distributed Data]].

### Not examined on…

- **AP Computer Science A** — no SQL.

## Quick reference

| Want | Write |
|---|---|
| all columns, some rows | `SELECT * FROM T WHERE cond;` |
| sorted | `… ORDER BY col ASC` / `DESC` |
| a total / count / mean | `SELECT SUM(x), COUNT(x), AVG(x) FROM T WHERE …;` |
| one row per group | `SELECT g, COUNT(*) FROM T GROUP BY g;` |
| two tables | `FROM A INNER JOIN B ON A.k = B.k` or `FROM A, B WHERE A.k = B.k` |
| condition on a total | `… GROUP BY g HAVING SUM(x) > 100` |
| a list from another query | `WHERE k IN (SELECT k FROM …)` |
| new row / change / remove | `INSERT INTO T VALUES (…);` `UPDATE T SET c = v WHERE …;` `DELETE FROM T WHERE …;` |
| new table | `CREATE TABLE T(f TYPE, …, PRIMARY KEY (f), FOREIGN KEY (g) REFERENCES U(g));` |
| new field | `ALTER TABLE T ADD f TYPE;` |
| execution order | FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY |
| with a variable, in Python | `cur.execute("… WHERE k = ?", (value,))` — never string-paste |

## Connections

- **Parent:** [[Relational Databases]] — the tables, keys and normal forms every statement here operates on; its worked schemas are this card's test data.
- **Children:** [[NoSQL and Distributed Data]] — the stores that gave up joins and then mostly grew a query language back; [[Data Security]] — SQL injection as the canonical input-validation failure, and the parameterised query as its fix.
- **Uses:** [[Hash Tables]] and [[Sorting]] — the join algorithms the query processor chooses between; [[Balanced Trees]] — the index a `WHERE` on a keyed column walks.
- **Same idea elsewhere:** [[Programming Paradigms]] — SQL as the declarative language every student already speaks, beside Prolog's facts and rules; [[Program Design]] — say what, not how, as a design principle; [[Decouple and Recouple]] — the query's *how* left to the engine, so the same statement runs on one machine or a thousand.
- **The script:** `sql-worked-examples.py`, beside this card — every statement above, run against SQLite, with the outputs quoted here.

- **Misconception traps cleared:** queries execute FROM-first, not top to bottom; WHERE cannot see totals; COUNT(*) ≠ COUNT(field); two tables in FROM is a product until joined; ORDER BY defaults ascending; text is quoted; UPDATE/DELETE act on every matched row.

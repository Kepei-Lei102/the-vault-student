---
chinese: 非关系型数据库与分布式数据 (fēi guānxì xíng shùjùkù yǔ fēnbùshì shùjù) / NoSQL
prerequisites:
  - "[[Relational Databases]]"
  - "[[SQL]]"
  - "[[Hash Tables]]"
  - "[[Graphs]]"
  - "[[Networks]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/databases
  - domain/distributed-systems
  - level/A-Level
  - level/IB
  - level/university
  - curriculum/IB-CS
  - syllabus/IB-CS-A3-4
  - type/deep
  - misconception/nosql-means-no-sql
  - misconception/nosql-is-faster
  - misconception/cap-means-pick-any-two
---

# NoSQL and Distributed Data 非关系型数据库与分布式数据

> *On the evening of 11 November 2019, Alipay's database answered sixty-one million queries in one second. No single machine on Earth can do that, and no single machine ever will. Everything on this card is about what happens to the tidy tables of the last two cards when the data no longer fits in one box — and about the one thing you have to give up to get there.*

## Definition

### Formal

**NoSQL** is the umbrella term, coined at a meetup in 2009, for database systems that do not use the relational model as their primary structure. Four families dominate: **key–value** stores, **document** stores, **wide-column** stores and **graph** databases. Most were built for **distributed** operation — data spread across many machines by **partitioning (sharding)** and copied across them by **replication** — and most relax the ACID guarantees of a relational transaction in favour of **availability**: the system keeps answering even when parts of it have failed or cannot reach each other. The **CAP theorem** (Brewer, 2000; proved by Gilbert and Lynch, 2002) states the trade precisely: when the network between machines is partitioned, a distributed store must choose between staying *consistent* and staying *available*.

### Intuitive

[[Relational Databases]] stores each fact once and reassembles the answer with joins, and [[SQL]] is the language for asking. That is the right design when the data must be *right* and fits on one machine. Two things broke it, at the same time, around 2005: the largest websites had more data than any one machine could hold, and they read that data a billion times for every time they wrote it. Spread the tables over a thousand machines and every join becomes a network conversation; keep ACID and every write must wait for all the copies to agree. So the builders of those sites did the thing this card is about: they **stored each record whole, in the shape the read wanted, gave up the join, and accepted that copies could briefly disagree.** Everything here is a variation on that decision — and the last section is about the swing back, because the largest Chinese systems have since shown you can have distribution *and* transactions, at a price.

### 中文锚点

**春运抢票。** 2012 年春运，12306 每天两千万人访问、最高十四亿次点击，网站几乎瘫痪——不是程序写得差，是**一台数据库扛不住**。后来的改造把余票查询这类"读一亿次、改一次"的数据搬进了**内存数据网格**（GemFire），几十台机器各存一份，同一秒能扛十二万人同时下单。**双十一。** 2019 年 11 月 11 日晚，支付宝的数据库一秒钟处理了六千一百万次查询——这个数字任何一台机器永远都做不到，只能靠**几千台机器分担**。这就是这张卡的题目：前两张卡的表和 SQL，在**数据放不进一个箱子**的时候会怎样。答案分四步。第一，**分片**（sharding）：按主键把数据切开，一部分人的数据放这台机器，另一部分放那台——就是[[Hash Tables|哈希表]]横跨一千台机器。第二，**复制**（replication）：每份数据存三份，一台坏了不丢。第三，麻烦来了：三份副本**可能短暂不一致**，而机器之间的网络**一定会断**——这时你只能二选一：**要么等到大家一致再回答**（一致性，C），**要么先回答、事后对账**（可用性，A）。这就是 **CAP 定理**：网络分区（P）不是选项，是天气；真正的选择是分区期间**要 C 还是要 A**。银行余额要 C，宁可让你等；购物车要 A，宁可在事后对账合并时多出东西，也不能让你加不进去。第四，为了让"读"不用跨机器拼表，很多系统干脆**不拆表了**——一个订单连同顾客和菜品整个存成一份（文档型，MongoDB）；或者只存"键 → 值"（键值型，Redis，微秒级）；或者把行按键排好序、横切成段，一千台机器各扫各的段（宽列型，Cassandra / Bigtable）；或者把**关系本身**当数据（图数据库，Neo4j——"朋友的朋友买过什么"是一跳，不是三次连接）。**NoSQL 不是"不要 SQL"**，是"**不止 SQL**"：它放弃的是连接和事务，换来的是横向扩展。最后一件事很中国：**OceanBase**（蚂蚁）证明了分布式也能保事务——2019 年用普通 x86 服务器刷新了 TPC-C 记录，把 Oracle 甩在后面。钟摆又荡回来了，只是价格写在账上。

| English | 中文 | 一句话 |
|---|---|---|
| NoSQL | 非关系型数据库 | 不以表和连接为主结构的数据库——**不止** SQL，不是**不要** SQL |
| Key–value / document / wide-column / graph | 键值 / 文档 / 宽列 / 图 | 四种形状：一把钥匙一坨值 / 整份 JSON / 行按键切成段 / 关系即数据 |
| Sharding (partitioning) | 分片 | 按键把数据切开放到不同机器——横跨集群的哈希表 |
| Replication | 复制 | 每份数据存几份，一台坏了不丢 |
| Consistency / Availability / Partition | 一致性 / 可用性 / 分区 | CAP 的三角：分区是天气，C 和 A 是分区期间的二选一 |
| Eventual consistency | 最终一致性 | 副本可以短暂不同，但最终会一样 |
| ACID vs BASE | 事务保证 vs 基本可用 | 严格事务 / 先回答、最终一致 |
| Data warehouse / OLAP | 数据仓库 / 联机分析 | 为**分析**而不是为**事务**建的只追加的大库 |
| NewSQL | 新型关系数据库 | 分布式**加**事务——Spanner、OceanBase |

---

## Why the relational model hit a wall

Three costs, all invisible on one machine, become the whole bill on a thousand:

- **The join.** In 3NF an order is four tables. On one disk that is four index lookups, microseconds apart. Across a cluster, the customer row may live on machine 17 and the plant row on machine 402; the join becomes network round trips, and a page that shows a hundred orders makes hundreds of them.
- **The transaction.** ACID's *atomic* and *durable* promises mean a write is not confirmed until it is safely stored — and with three replicas on three machines, "safely" means all three have agreed. Every write waits on the slowest machine and on the network between them.
- **The schema.** Adding a column to a table of a billion rows on one machine is an afternoon; coordinating it across a thousand machines while they serve traffic is an engineering project.

The obvious fix — a bigger machine, **vertical scaling** — runs out at the top of the price list. The fix that worked was **horizontal scaling**: many ordinary machines, and a data model that does not need them to talk to each other for every read. Google described its system in *Bigtable* (Chang et al., OSDI 2006); Amazon described its own in *Dynamo* (DeCandia et al., SOSP 2007). Those two papers are the parents of nearly everything below: Cassandra, open-sourced by Facebook in July 2008, is literally Bigtable's data model on Dynamo's distribution; HBase is Bigtable reimplemented; Amazon's DynamoDB (2012) is Dynamo sold as a service.

> [!info] The name
> On 11 June 2009 Johan Oskarsson organised a meetup in San Francisco for people building these stores and wanted a name that would work as a Twitter hashtag — short, memorable, few Google hits. Eric Evans of Rackspace suggested *#nosql*. Voldemort, Cassandra, HBase, CouchDB and MongoDB presented. The name stuck and has been argued about ever since; the reading most of its builders accept is *"not only SQL"* — the point, as Evans put it, was to solve problems relational databases were a bad fit for, not to abolish them.

## The four families

![[nosql-four-families.svg|900]]

The figure holds one fact — *Mei, in Chengdu, ordered roses* — in each shape. [[Relational Databases]] would store it in three tables and join; each family below stores it in the shape a particular *read* wants.

### Key–value — a hash table across a data centre

`GET key` → value; `SET key value`. Nothing else: no query on the value, no schema, no join. The value is a blob the store never looks inside. This is [[Hash Tables]]' lookup — the most-executed data-structure operation on Earth — spread across machines by hashing the key to choose the machine, and it inherits the hash table's $O(1)$ speed. **Redis** (Salvatore Sanfilippo, 2009) keeps everything in RAM and answers in microseconds; it is the **cache** in front of most large websites, the session store that remembers you are logged in, the leaderboard, the rate limiter. **DynamoDB** is the same shape as a managed service. If the question is "give me the thing with this ID", nothing beats it; if the question is anything else, it cannot help.

### Document — the record, whole

A **document** is a JSON object: nested, variable, self-describing. Mei's document holds her name, her city *and her orders inside it* — the join has been done in advance, at write time, and a read returns one object. **MongoDB** (10gen, 2009) and **CouchDB** are the standard examples. The model fits the way a program already holds the data (a Python dict, a JavaScript object), which is why it won web developers: no mapping layer between the code's shape and the store's. The price is the one normalisation warned about: if Mei's *city* is copied into every order document, changing it is a hunt through every copy — the update anomaly, chosen on purpose because reads outnumber writes ten thousand to one.

### Wide-column — sorted keys, sparse rows, split across machines

Bigtable's shape. Rows have a key and are kept **sorted by it**; each row can have any set of columns, thousands of them, most empty; and the sorted key range is **cut into pieces** that live on different machines. Two things follow. A range scan (`all rows for customer C1`, `all events between two times`) walks one machine's slice, sequentially. And a system can grow by adding machines and re-cutting the ranges. **Cassandra**, **HBase** and Bigtable itself run the feeds, logs, sensor streams and time series of the largest sites — Apple, Netflix and Discord run Cassandra clusters of thousands of nodes — where the workload is *append constantly, read by key or by range, never join*.

### Graph — the relationships are the data

A **graph database** stores **nodes** and **edges** with properties on both, and queries walk the edges: *friends of Mei who ordered roses* is one hop from Mei's node, then a filter — where the relational version is a self-join on a friendship table, then a join to orders, then to plants. [[Graphs]] gives the structure and the traversals; **Neo4j** (2007) made them a database. Fraud detection (rings of accounts that share a phone number), recommendation ("people who bought…"), knowledge graphs and the social graph itself are the natural fits: anything where the question is about *paths*, not *rows*.

### Choosing

| The read you need | Reach for | Because |
|---|---|---|
| one thing by ID, fast, millions of times | key–value | a hash lookup, in RAM |
| a whole object as the program holds it | document | the join is pre-done at write time |
| everything for a key, or a range of keys, appended forever | wide-column | sorted keys, sequential scans, easy to split |
| paths, neighbours, "connected to" | graph | edges are stored, not computed |
| facts that must be right, changed constantly, queried in ways not yet known | **relational** | one copy of each fact; any question later |

The last row is not a consolation prize. Most systems that matter — money, bookings, records — are still relational, and the NoSQL stores sit *beside* them handling the reads that would otherwise crush them. A real architecture is usually a relational core with a Redis cache in front and a wide-column store for the logs.

## Distribution — what "many machines" actually costs

### Sharding and replication

**Sharding** (partitioning) cuts the data by key: hash the key, or take a range of it, and that decides the machine. It is [[Hash Tables]]' bucket index with a network cable in the middle, and it makes every by-key operation local. **Replication** keeps several copies of each shard on different machines, so that one machine's death loses nothing and reads can be served from any copy. Both are decouplings in [[Decouple and Recouple]]'s sense — data from one machine's capacity, availability from one machine's health — and both introduce the problem the rest of this section is about: **the copies must agree, and they are joined by a network that will fail.**

### The CAP theorem

![[nosql-cap-triangle.svg|720]]

Eric Brewer stated it as a conjecture in a 2000 keynote; Seth Gilbert and Nancy Lynch proved it in 2002. Three properties: **Consistency** (every read returns the latest write, as if there were one copy), **Availability** (every request gets a non-error answer), **Partition tolerance** (the system keeps operating when the network splits and machines cannot reach each other). The theorem: *during a partition, you cannot have both C and A.* The reasoning is short enough to hold in one hand. Two replicas, the cable between them cut. A write arrives at one. A read arrives at the other. Either the second replica answers with what it has — available, but stale, so not consistent — or it refuses until the cable is back — consistent, but not available. There is no third option, because the information physically cannot cross.

Two things students get wrong. **P is not a choice.** Networks partition — a switch reboots, a cable is cut, a data centre floods — so every real distributed system is partition-tolerant or it is broken; the actual decision is *C or A when the partition happens*. And **the trade is per operation, not per system.** A bank's balance read is CP (wait, or refuse, rather than show a wrong number); Amazon's shopping cart is AP (Dynamo's paper is explicit: a customer must always be able to add to the cart, and two divergent carts are merged later — an extra item beats a lost sale). Most stores let you choose per request.

![[nosql-cap-comic.png|880]]

One railway company, two ticket windows, and the wire between them cut by the storm — a partition. The northern clerk hangs 线路中断 暂停售票 and sells nothing: he cannot know what the south has sold, so he refuses rather than risk a seat twice — **consistent, not available**. The southern clerk keeps stamping and writes 稍后对账 in the ledger: every traveller gets a ticket now and the books are settled when the wire is back — **available, not consistent** — and the two tickets for 12车 08A on the counter are what "settled later" costs. The messenger splashing down the road is the only consistency left while the wire is down, and the cat has read Gilbert and Lynch. Both clerks are right; they just work for different products. The north is a bank; the south is a shopping cart.

### ACID versus BASE, and eventual consistency

The relational transaction is **ACID**. The distributed alternative was named, with a chemist's joke, **BASE**: *Basically Available, Soft state, Eventually consistent*. **Eventual consistency** means the copies may disagree for a while — milliseconds to seconds — but if writes stop, they converge. Post a comment and see it immediately, while a friend on another continent sees it a second later: that second is eventual consistency, and for a comment it is fine. For a bank balance it is not, and that is the whole reason both models exist.

## Where this is the working tool

**12306.** In the 2012 Spring Festival rush the railway ticketing site took twenty million visitors and 1.4 billion clicks a day and nearly stopped. The problem was one hot query — *how many seats are left on this train?* — read a hundred million times for every time it changed, hammering one relational database. The redesign (2012, with the China Academy of Railway Sciences) moved seat availability into **GemFire**, an in-memory data grid: the same data on dozens of machines, in RAM, answering locally. Concurrent bookings rose to 120,000 at once, and the site has held every Spring Festival since. It is the purest example of the decision this card is about: *the query that must be fast was moved out of the store that must be right.*

**Double 11 and OceanBase.** Alipay's payment traffic on 11 November 2019 peaked at 61 million queries per second. That workload cannot give up transactions — it is money — so Ant Group built **OceanBase**, a relational, transactional database that shards and replicates across thousands of ordinary x86 servers and keeps ACID across them with a consensus protocol. In October 2019 it took the TPC-C benchmark record at 60.9 million transactions a minute, roughly twice Oracle's, on commodity hardware; a year later it posted 707 million. It belongs to the family called **NewSQL** — Google's Spanner (2012) is the other landmark — and it is the pendulum's return: distribution *with* transactions, paid for in coordination latency and in engineering that took a decade.

**Everything else you use.** Your WeChat session, your game's leaderboard and your shopping cart are in a key–value store; your feed and your message history are in a wide-column store; the "people you may know" list came out of a graph; and the recommendation that followed you across three apps came out of a data warehouse.

## Data warehouses and analytics

Everything so far has been **OLTP** — online transaction processing: many small reads and writes, each about one customer or one order, right now. A business also asks a second kind of question: *how did sales of roses in Chengdu change month by month over three years, by customer age?* That is **OLAP** — online analytical processing — and it is the wrong shape for a transaction store: it reads *every* row, touches three columns of forty, and must not slow down the checkout while it runs.

A **data warehouse** is a separate database built for these questions. Bill Inmon's 1992 definition, still quoted in every syllabus, names four properties: **subject-oriented** (organised around customers, products, sales — not around the operational systems), **integrated** (data from every source cleaned into one consistent form), **time-variant** (every fact carries its date, so history is kept, not overwritten) and **non-volatile** (append-only: loaded, never edited). Data is copied in from the transaction systems on a schedule, and the warehouse answers the analysts while the OLTP stores serve the customers.

Two technical consequences worth knowing. Warehouses are **columnar**: they store each column together on disk rather than each row, so a query touching three columns reads three streams instead of forty, and a column of a million similar values compresses enormously ([[Compression]] explains why runs of similar values are cheap). And they are queried in [[SQL]] — the language survived its supposed replacement here too. The analysis itself — **data mining** — has a standard menu: *classification* (which customers will churn?), *clustering* (what groups do they fall into?), *regression* (what drives spend?), *association rules* (what sells with what?), *sequential patterns* (what do people buy next?), *anomaly detection* (which transaction is fraud?). The first three are the bread of [[Machine Learning]]; the rest are the warehouse's own.

Three further shapes appear on the IB list. **In-memory** databases (Redis, GemFire, SAP HANA) keep the working set in RAM for speed, with disk as backup — 12306's move. **Spatial** databases (PostGIS, the engine under most GIS) index by location so *"everything within 2 km"* is a tree walk, not a scan; [[Graphs]]' navigation is a spatial query. **Cloud** databases are any of the above as a managed service — someone else's machines, someone else's replication — which is what most companies now run.

## Misconceptions

1. **"NoSQL means no SQL."** It means *not only* SQL. Most of the stores have grown a query language that looks like SQL (Cassandra's CQL, MongoDB's aggregation pipeline), the warehouses speak SQL outright, and the NewSQL systems are SQL databases.
2. **"NoSQL is faster."** It is faster *at the read it was shaped for* and slower or impossible at everything else. A key–value store cannot answer "which customers ordered roses?" without scanning every value. Speed came from giving up generality, not from cleverer code.
3. **"Schemaless means no schema."** The schema moved from the database into the program that reads the documents. Every field the code expects is a schema rule — one nobody enforces until the code crashes on a document that lacks it.
4. **"CAP says pick any two."** Partition tolerance is not optional in a real network, so the choice is C or A *during a partition*, and it can be made per operation.
5. **"NoSQL replaced relational."** Relational databases run the money, the bookings and the records of nearly every organisation on Earth, and SQLite alone has a trillion instances. NoSQL stores sit beside them, carrying the reads that would otherwise crush them.
6. **"Eventual consistency is a bug."** It is a chosen trade, correct for comments and carts and wrong for balances. The bug is choosing it without noticing.

## Beyond syllabus

### Consistent hashing, and the ring

Hash the key mod the number of machines, and adding one machine changes the answer for almost every key — every record moves. Dynamo's fix, borrowed from a 1997 paper by Karger and colleagues, is to hash *both* keys and machines onto a circle and give each key to the next machine clockwise: adding a machine moves only the keys between it and its predecessor. Every large key–value store uses it, and it is a fine exercise in [[Hash Tables]] taken one step further.

### Consensus — how NewSQL keeps ACID across machines

Spanner and OceanBase keep transactions consistent across replicas by *voting*: a write is confirmed when a majority of replicas have logged it (the Paxos and Raft protocols), so a minority partition cannot commit a conflicting write. The price is a network round trip per commit — milliseconds instead of microseconds — which is exactly the availability CAP said you would pay. Spanner additionally uses atomic clocks and GPS in every data centre to order transactions globally (its *TrueTime* API), which is as close as engineering gets to buying consistency with hardware.

### MapReduce, and the warehouse's other half

Bigtable's sibling paper, *MapReduce* (Dean and Ghemawat, 2004), described how Google ran a computation over petabytes: split the data across machines, apply a function to each piece (*map*), regroup the results by key, and combine each group (*reduce*) — [[Parallel and External Sorting]]'s merge phase, scaled to a data centre. Hadoop reimplemented it in the open; Spark replaced it; every modern warehouse runs a descendant. `GROUP BY` on a trillion rows is a MapReduce job whether or not anyone says so.

## Exam Notes

### IB Computer Science (A3.4 — HL only)

- **Alternative databases:** the NoSQL families with real-world contexts (e-commerce, social media, real-time analytics), plus **in-memory**, **spatial** (GIS) and **cloud** models — the four-family figure and the "Choosing" table, with 12306 and a shopping cart as the contexts.
- **Data warehouses:** their objectives in data management and business intelligence; the roles of **append-only, subject-oriented, integrated, time-variant, non-volatile** data, optimised for query performance — Inmon's four properties above, with append-only named separately; **OLAP** and **data mining** with the six techniques listed (classification, clustering, regression, association rules, sequential patterns, anomaly detection).
- **A3.1–A3.3** (the relational model, design and SQL) are [[Relational Databases]] and [[SQL]].

### Not examined on…

- **Cambridge 9618** — §8 is relational only; nothing here is required, though "big data" vocabulary sometimes appears in §7/§18 context questions. **Cambridge 0478** — single-table databases. **AP Computer Science A** — no databases. This card is enrichment for all three, and the first thing a student meets on the first day of any real software job.

## Quick reference

| Term | One line |
|---|---|
| Key–value | `GET`/`SET` by key; a distributed hash table; Redis, DynamoDB |
| Document | whole JSON objects; joins pre-done at write; MongoDB |
| Wide-column | sorted row keys, sparse columns, split into ranges; Cassandra, Bigtable, HBase |
| Graph | nodes and edges stored; path queries; Neo4j |
| Sharding | cut data by key across machines |
| Replication | several copies of each shard |
| CAP | under partition, choose consistency or availability; P is not optional |
| ACID / BASE | strict transactions / basically available, eventually consistent |
| OLTP / OLAP | many small transactions now / few huge analytical scans over history |
| Warehouse | subject-oriented, integrated, time-variant, non-volatile, append-only; columnar; SQL |
| NewSQL | sharded + replicated *and* ACID via consensus; Spanner, OceanBase |

## Connections

- **Parents:**
   - [[Relational Databases]] — the model whose join and transaction costs every design here is an answer to; read it first, or the trades here look free.
   - [[SQL]] — the language that survived its replacement: the warehouses speak it, the NoSQL stores grew imitations of it, NewSQL is it.
   - [[Hash Tables]] — the key–value store is a hash table across a data centre; sharding is its bucket index with a network in the middle.
   - [[Graphs]] — the structure and traversals a graph database makes persistent and queryable.

- **Uses:** [[Decouple and Recouple]] — sharding and replication as decouplings (data from one machine's capacity, availability from one machine's health), and the transaction as the coupling NewSQL refuses to give up; [[Compression]] — why columnar storage compresses; [[Parallel and External Sorting]] — MapReduce as its merge phase at data-centre scale; [[Secondary Storage]] and [[RAM and the Memory Hierarchy]] — why an in-memory store is a thousand times faster than a disk-backed one.

- **Related:** [[Machine Learning]] — classification, clustering and regression as the data-mining techniques the warehouse feeds; [[Dual-Core Craft]] — another system that chose one hard coupling (lockstep) for a bandwidth reason and lived with the bill.

- **Misconception traps cleared:** NoSQL = no SQL; NoSQL is faster; schemaless = no schema; CAP = pick any two; NoSQL replaced relational; eventual consistency is a bug.

## Sources

- E. Brewer, *Towards Robust Distributed Systems*, PODC keynote, 2000; S. Gilbert and N. Lynch, *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*, SIGACT News, 2002.
- F. Chang et al., *Bigtable: A Distributed Storage System for Structured Data*, OSDI 2006; G. DeCandia et al., *Dynamo: Amazon's Highly Available Key-value Store*, SOSP 2007; J. Dean and S. Ghemawat, *MapReduce*, OSDI 2004.
- The 11 June 2009 meetup and the name: Martin Fowler's account in *NoSQL Distilled* (2012); Eric Evans's own posts.
- Release dates: Cassandra open-sourced July 2008; Redis and MongoDB first released 2009; Neo4j 2007; DynamoDB launched 18 January 2012.
- 12306 and GemFire: the China Academy of Railway Sciences / Pivotal case history (2012–2015 figures as reported by Pivotal); Alipay's 2019 peak of 61 million QPS and OceanBase's TPC-C results (October 2019, 60.9 million tpmC; 2020, 707 million tpmC): OceanBase's published accounts and the TPC-C results list.
- W. H. Inmon, *Building the Data Warehouse* (1992) — the four properties.

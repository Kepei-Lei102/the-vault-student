---
chinese: 技术栈的解剖 (jìshù zhàn de jiěpōu)
prerequisites:
  - "[[Programming Fundamentals]]"
  - "[[The Internet and the Web]]"
  - "[[Relational Databases]]"
  - "[[Program Development Life Cycle and Testing]]"
leads_to: []
tags:
  - subject/cs
  - domain/software-engineering
  - domain/networks
  - level/IGCSE
  - level/A-Level
  - level/IB-HL
  - level/university
  - curriculum/Cambridge-9618
  - curriculum/Cambridge-0478
  - curriculum/IB-CS
  - type/theory
  - type/hands-on
  - type/visual-tool
  - notation/request-response
  - misconception/the-frontend-can-enforce-rules
  - misconception/a-server-is-a-big-computer
  - misconception/more-servers-means-faster
  - misconception/works-on-my-laptop
---

# Anatomy of a Tech Stack 技术栈的解剖

> Every program you have written so far had one user, who was you, ran when you told it to, and forgot everything when it stopped. A website has strangers, thousands at once, at three in the morning, some of them typing nonsense on purpose, and it must remember. Nothing in the language changes. Everything around it does. This card is the anatomy of the "everything around it": what a tech stack is, layer by layer, why it has those layers and not others, and how much each one costs, measured on a stack you can run on your own laptop in one file.

## What this is for

[[Programming Fundamentals]] teaches the program; [[The Internet and the Web]] teaches how a browser finds a server and what HTTP says; [[Relational Databases]] and [[SQL]] teach where data lives. None of them says how those pieces are joined into a thing that serves people, and that joining is the leap the syllabus never makes: from a **script**, which runs once for its author, to a **system**, which runs always for everyone. This card makes the leap with a complete stack in one Python file, then takes it apart: the request's journey and where its milliseconds go, the three tiers and what each is allowed to remember, why the application tier can be copied and the data tier cannot, what happens under load, and how code reaches a server and how you know it is broken.

## Definition

### Formal

A **tech stack** is the set of components, one on top of another, through which a user's request travels and returns: a **client** (browser or app) that sends a request and renders the response; the network, name and encryption services between; an **application server** that receives the request, checks it, does the work and answers, usually through an **API** (application programming interface: a set of named routes with agreed request and response shapes, most often JSON over HTTP); and a **data tier**, the database that holds the state of the system, with a **cache** in front of it and file storage beside it. Around the request path sit the systems that keep it alive: **deployment**, which moves new code onto the servers; **observability** (logs, metrics, alerts), which reports what the servers are doing; and backups. The tiers are separated by what they are allowed to remember: the client remembers nothing that must be trusted, the application server remembers nothing between requests (it is **stateless**, so it can be duplicated), and the database remembers everything (it is the **state**, so there is one of it).

### Intuitive

Cooking dinner for yourself and opening a restaurant use the same skill and need entirely different things. The restaurant needs a front door and a menu strangers can read; a waiter who carries orders in and plates out; a kitchen that keeps working when three tables order at once; a storeroom whose stock survives closing time; and a way to say "we are out of that" rather than collapsing when an order makes no sense. The page is the menu, the server is the waiter and the kitchen, the database is the storeroom, and the phone line and delivery routes between them cost more time than the cooking. The leap from script to system is not a new language. It is accepting that strangers will now arrive together, at any hour, sometimes ordering nonsense, and building so that the food still comes out.

### 中文锚点 (Chinese Anchor)

想一想自己在家做一顿饭，和开一家餐馆，差别在哪里。炒菜的手艺是一样的，可餐馆需要一大堆家里厨房从来不需要的东西：一扇门和一份陌生人看得懂的菜单，一个把点单送进去、把菜端出来的服务员，一个三桌同时点菜也不会乱的后厨，一间打烊以后食材也不会消失的储藏室，还有一套办法，让客人点了一道根本不存在的菜时，听到的是"这个没有"，而不是整家店垮掉。你在自己笔记本上跑的一个程序，就是一个人的晚饭；一个网站、一个 app、一台游戏服务器，是一家餐馆，它的"技术栈"就是这些部件一层层叠起来：用户看到的页面或 app 是门面和菜单；服务器是服务员加后厨，接下每一个请求，干活，再把回复送回去；数据库是储藏室，是唯一一层重启以后记忆还在的地方；而这几层之间跑着电话线和送货的路，它们花的时间比炒菜本身还多。从写脚本到做系统，这一跃不在于学一门新语言，而在于意识到：从今往后，陌生人会一起涌进来，随时都可能来，有时还会点些莫名其妙的东西，而技术栈里的每一样东西，都是为了在这种情况下照样把菜端出去。

## Notation

| Term | Meaning | Notes |
|---|---|---|
| client / server | the side that asks / the side that answers | roles, not machines: a server is any process listening on a port |
| request, response | one HTTP message each way | method + path + headers + body; status code + headers + body |
| API, endpoint, route | the contract; one named URL in it; the code behind it | `GET /api/top`, `POST /api/scores` |
| JSON | the text format for structured data between tiers | `{"name": "ada", "score": 90}`; [[File Handling]] |
| stateless | keeps nothing between requests | the property that lets a tier be copied |
| state | what must be remembered | lives in the data tier |
| cache, TTL | a fast copy of a recent answer; how long it is trusted | stale by design |
| load balancer | one address that spreads requests over $N$ servers | also the place that notices a dead one |
| latency, throughput | time for one request; requests per second | $L = \lambda W$ links them (Little's law) |
| p50, p99 | the median and the slowest 1 % | the tail is what users complain about |
| listen backlog | how many connections can wait to be accepted | the first thing that broke in this card's lab |

## Part I — Script versus system

Five things change the moment a program is meant for someone else.

1. **Strangers.** The author is no longer the only user, so the program can no longer assume its input is sensible. Every request is untrusted until checked.
2. **Concurrency.** Users do not queue politely; sixteen arrive in the same millisecond. Code that was correct alone can be wrong in company ([[Operating Systems]] on processes and locks).
3. **Time.** A script runs and exits; a system runs for months. Memory leaks, growing logs, expiring certificates and full disks are failures that a script can never have.
4. **Hostile input.** Some of the strangers are trying to break it. The boundary where input enters is where [[Data Security]] is decided.
5. **State that must survive.** A script's variables die with it. A system's data must survive restarts, crashes, deployments and the loss of a machine.

The lab makes the last one visible in two lines. `tech-stack-lab.py` keeps a counter of requests served inside the server process and three scores inside SQLite; it then stops the server and starts a fresh one:

```
1. restart: the process counter went 9 → 1; the database still holds 3 rows, top = ['grace', 'ada', 'alan']
```

Everything in the process's memory was lost, and the port number changed. Everything in the database was there. That single difference is what the whole architecture is arranged around.

## Part II — The journey of one click

![[tech-stack-request-journey.mp4]]

Follow one click from a browser in Chengdu to a server and back, with the clock running. The hops and their typical costs, for a server about 30 ms away:

| hop | what happens | first visit | second visit |
|---|---|---|---|
| DNS | the name becomes an address ([[The Internet and the Web]] Part II) | ~20 ms | cached: 0 |
| TCP + TLS | open a connection and agree a key ([[Networks]], [[Encryption]]) | 2 round trips, ~60 ms | connection kept open: 0 |
| edge / CDN | a provider's nearby cache: static files answered here | ~5 ms | ~5 ms |
| load balancer | picks one of $N$ app servers | ~1 ms | skipped |
| app server | validate, decide, query | ~3 ms | skipped |
| database | the query, often a disk read | ~8 ms | skipped |
| the reply | the same wires back | ~30 ms | ~30 ms |

Of the first visit's 127 ms, the code the developer wrote accounted for three. The rest was distance, handshakes and the disk. That ratio is the first fact of the trade: **a system's speed is mostly decided by how many round trips it makes and what it can skip**, not by the speed of its logic. Two things skip: a connection kept open (HTTP keep-alive; the lab's server speaks HTTP/1.1 for exactly this reason), and a cache that answers before the request reaches the application. The second visit costs 35 ms and the app server never hears of it. The price is honesty: the cached answer is as old as its TTL, which is fine for a leaderboard and unacceptable for a bank balance.

## Part III — The three tiers, and what each may remember

![[tech-stack-anatomy.svg|1000]]

**Presentation: the browser or app.** HTML, CSS and JavaScript, or a native app, sent to the user's device and run there. The lab's whole frontend is a string `PAGE` served at `/`: a list, a form, and twelve lines of JavaScript that `fetch` the API and redraw. The rule of this tier is that **nothing it holds can be trusted**, because the user owns the device: a price computed in the browser, a "you are logged in" flag, a check that a field is a number, can all be edited by anyone who opens the developer tools. Front-end validation is a courtesy to honest users; the real check is on the server.

**Application: the API.** One process that listens on a port, reads each request, and answers. Its code is the part a student recognises as programming, and the lab's is forty lines: three `GET` routes, one `POST`, validation, a status code for every outcome. The rule of this tier is **statelessness**: it may hold caches and counters, but nothing it must not lose, because then it can be run as $N$ identical copies behind a load balancer and any copy can be killed, restarted or replaced mid-deploy. The lab's `state["served"]` counter is deliberately the wrong place to keep anything that matters, and the restart proves it.

```python
def do_POST(self):
    if self.path != "/api/scores":
        return self.send(404, {"error": "no such route"})
    try:
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        name, score = str(body["name"])[:40], int(body["score"])
    except (ValueError, KeyError, TypeError) as e:      # the boundary: outside is untrusted
        return self.send(400, {"error": "bad request: %s" % e.__class__.__name__})
    store.add(name, score); cache.clear()
    self.send(201, {"ok": True})
```

The `try` is the boundary of Part I. Four kinds of nonsense were sent to it in the lab (not JSON, a missing field, a score of `"lots"`, a route that does not exist) and it answered `400, 400, 400, 404` and kept serving. A script would have printed a traceback and died.

**Data: the truth.** A database, one of it, with everything that must survive: [[Relational Databases]] for the model, [[SQL]] for the language, [[NoSQL and Distributed Data]] for what happens when one machine is not enough. Beside it, **object storage** for files (images, uploads, backups), which do not belong in a database, and in front of it a **cache** whose only job is to be faster than the database and whose only rule is that it may be wrong for a bounded time. The lab's `Store` is a SQLite table and its `Cache` is a dictionary with expiry; that is the same architecture as a site with a billion users, at a scale you can read.

## Part IV — Why the split is where it is

The tiers are cut along one line: **state**. Everything left of the database in the figure can be duplicated, because it remembers nothing that matters; the database cannot, because two copies of the truth immediately disagree. So a system scales by adding stateless servers, and its hardest problems are all in the one tier that cannot be added to: the database's speed, its size, its backups, and what happens to it when the machine dies. Caches exist to keep requests away from it; queues exist to smooth bursts before they reach it; the entire discipline of [[NoSQL and Distributed Data]] is what it costs to have more than one.

**The first thing that broke.** The lab's first run refused 1 513 of 3 200 requests when sixteen clients arrived at once, and not one line of the author's code was at fault. A listening socket keeps a queue of connections that have arrived and not yet been accepted, and Python's default length for it is five. With sixteen clients reconnecting for every request, the queue overflowed and the operating system turned the rest away. One setting (`request_queue_size = 256`) and the error count was zero. This is the ordinary shape of a system failure: it lives in a default nobody chose, in a layer nobody wrote, and it only appears under a load nobody tested. It is why systems are measured, not reasoned about.

**Writes, at once.** Sixteen threads each posted fifty scores in the same quarter-second: 800 attempted, 800 landed. SQLite allows one writer at a time and makes the others wait, and the lab's connection asks for a five-second patience (`timeout=5`) rather than the default of instant failure. Remove that and the same run reports "database is locked" for a share of the writes. The lock was always there; the question a system must answer is what to do while waiting for it.

## Part V — Measured

![[tech-stack-measurements.svg|1000]]

All of it on one laptop, with no network in the way, so every millisecond is the stack itself:

| route | median | slowest 1 % |
|---|---|---|
| `/api/health` (no database) | 0.31 ms | 0.92 ms |
| `/api/top`, database every time | 0.45 ms | 1.73 ms |
| `/api/top`, through the cache | 0.27 ms | 0.61 ms |

Three lessons. The database costs more than the code around it, even for a three-row table on a fast disk, and the cache removes it. The **tail** is three to four times the median in every row: the slowest 1 % of requests are where garbage collection, a lock, a disk flush or a scheduler decision land, and a page that makes a hundred API calls will hit that tail on almost every load. Throughput held at roughly 2 700 requests per second from one to sixteen clients, which says the server was already saturated by one: a Python thread per request is the simplest server design and the slowest, and the production versions of this tier (Node, Go, a Java servlet container, a Cloudflare Worker) exist to raise that number by an order of magnitude or two.

## Part VI — The systems around the request

**Deployment.** Code reaches a server by a pipeline: a push to version control triggers a build, the tests of [[Program Development Life Cycle and Testing]] run, and only then does the new version replace the old, one server at a time behind the load balancer so that the site never goes down to update itself. Configuration and secrets (database passwords, API keys) are never in the code; they are set in the server's environment, which is why a key that must call another service can live on the server and never reach the browser.

**Observability.** A system that cannot be seen cannot be fixed. Every request writes a line to a **log** (the lab collects `GET /api/top` lines in memory; a real one ships them to a search index); counters and timings become **metrics** on a dashboard; thresholds on those metrics become **alerts** that wake someone. The p99 in Part V is a metric; "p99 above 500 ms for five minutes" is an alert.

**Who runs which layer.** The cloud is not a place; it is a question of which tiers you rent. **Infrastructure as a service** (IaaS) rents machines and you run everything above them; **platform as a service** (PaaS) rents the operating system, runtime and database and you supply only the application; **software as a service** (SaaS) rents the finished application and you supply only the data. A **serverless** function such as a Cloudflare Worker is PaaS taken to its end: you write the request handler and nothing else, and the provider runs it at the edge, in as many copies as the traffic needs, billed per request.

## Where this is the working tool

**The classroom's own sites.** The quiz and code-practice sites used with this vault are this exact anatomy at small scale: static pages (presentation) served from a provider's edge; a serverless Worker (application) that validates each submission and holds the access codes; a hosted SQL database (data) that survives every redeploy; and, for marking, a language-model API called *from the Worker*, so that the key that pays for it lives in the server's environment and never reaches a browser. A deploy is one command; the logs are in the provider's dashboard; the whole thing costs nothing at a few hundred users. A student who has read this card can draw it.

**Every app on the phone.** A messaging app is a client; the servers that route messages are stateless and numbered in the thousands; the message store is the state and the hard part. A game's login queue is a load balancer refusing to let more players into the state tier than it can serve. An online exam platform that fails at 9 a.m. failed at Part IV: a burst that reached the database.

**Hands-on.** Run the lab and open the port it prints in a browser while it runs; the page is the frontend talking to the API you can read. Then break it on purpose: set `request_queue_size` back to 5 and watch the refusals return; delete `cache.get` and watch the database column rise; remove `timeout=5` and count the locked writes; add a route that trusts a number from the client without `int()` and post it a string.

## Worked examples

### Example 1: where the time goes

*A page loads over a 40 ms round trip. It needs DNS, a new TLS 1.3 connection, the HTML, then three API calls made one after another on the same connection, each answered by the server in 5 ms. Estimate the load time, then the saving if the three calls are made in parallel.*

**Trigger:** costs given per hop and a sequence of dependent requests: add round trips, not code. **Tool: the hop budget of Part II; TLS 1.3 costs one round trip after TCP's one.**

DNS ≈ 40, TCP 40, TLS 40, HTML 40 + server, three calls at 45 each in series = 135: about 300 ms, of which the server's logic was 20. In parallel the three calls overlap into one 45 ms wait: about 210 ms. Nothing in the server changed; the client stopped waiting three times.

### Example 2: how many servers

*One app server was measured at 2 700 requests per second. A launch is expected to peak at 20 000 requests per second with a median latency of 30 ms. How many servers, and how many requests are in flight at the peak?*

**Trigger:** a rate and a capacity per unit is a division with headroom; a rate and a time is Little's law. **Tools: capacity division; $L = \lambda W$.**

$20\,000 / 2\,700 = 7.4$, so eight servers with no margin; twelve gives room for one to die and for the tail. In flight: $L = 20\,000 \times 0.030 = 600$ requests at any instant, which is what the load balancer's and the database's connection limits must accommodate. Note what the arithmetic does not say: whether the one database behind twelve servers can take 20 000 queries a second. That is the question the cache exists to answer.

### Example 3: stale on purpose

*A leaderboard is cached for 2 s, a shopping basket is not. Justify both.*

**Trigger:** what does a wrong answer cost, and for how long? **Tool: the cache rule of Part III, stale for a bounded time.**

A leaderboard read a hundred times a second, two seconds old, misleads nobody and removes a hundred queries a second from the database. A basket shown with an item the user just removed is a bug the user will see immediately, and it is read once per page by one person; caching it saves nothing and costs trust. Cache what is read often and by many; never cache what one person just changed.

### Example 4: client-server for a scenario

*A school wants students to submit code from any device and teachers to see every submission. Justify the client-server model over peer-to-peer.*

**Trigger:** where must the state live, and who must be able to reach it? **Tool: the state line of Part IV.**

Submissions are state that every teacher must see and no student may alter: one place must hold them, control who reads and writes, and be backed up. That is a server. Peer-to-peer has no such place; each device holds its own copy and there is no authority over the record. The cost, a single point that must be kept running and secure, is the cost of having a truth at all.

### Example 5: which cloud tier

*The same school must choose between renting virtual machines, renting a platform that runs its Worker and database, or subscribing to a finished quiz product. Match each to IaaS, PaaS and SaaS and say what the school still has to do in each.*

**Trigger:** "who runs which layer" is the definition of the three tiers. **Tool: Part VI's table of responsibilities.**

Virtual machines are IaaS: the school installs, patches and backs up everything. The Worker platform is PaaS: the school writes the application and the data model and nothing below. The finished product is SaaS: the school supplies the questions and the class list, and controls nothing else, including whether the product keeps existing.

## Common Misconceptions (Teaching Notes)

### 1. "The frontend can enforce the rules"

Anything that runs on the user's device runs under the user's control. Validation, prices, permissions and totals are recomputed on the server or they are not enforced. The lab's server checks `int(body["score"])` even though the page's form has `type=number`.

### 2. "A server is a big computer"

A server is a process listening on a port. The lab runs one on a laptop in a thread; a phone can be one. Size is a separate question decided by load, and the answer is usually many small ones, not one big one.

### 3. "More servers means faster"

More servers raise **throughput**, the number of requests per second. They do nothing for **latency**, the time one request takes, which is set by round trips and the database. Example 1 is all latency and adds no servers; Example 2 is all throughput.

### 4. "The cloud is someone else's magic"

It is someone else's servers, rented by the tier. Every layer in the anatomy still exists; the only question is who is paid to run it, and IaaS, PaaS and SaaS are the three honest answers.

### 5. "It works on my laptop"

A script is finished when it works once for its author. A system is finished when it works for strangers, concurrently, for months, under hostile input, and survives a restart. The lab's first run passed every test with one client and refused half the requests with sixteen.

## Exam Notes

### Cambridge 9618 (AS Level), §2.1

"Explain the client-server and peer-to-peer models of networked computers", with the guidance "Roles of the different computers within the network and subnetwork models", "Benefits and drawbacks of each model" and "Justify the use of a model for a given situation" (Example 4 is the shape); "Show understanding of thin-client and thick-client and the differences between them"; and "Show understanding of cloud computing", "Including the use of public and private clouds" and "Benefits and drawbacks of cloud computing". Parts III, IV and VI carry these; [[The Internet and the Web]] has the Paper 1 questions worked against their schemes. The syllabus also examines the use of SSL/TLS in client-server communication under §17.1.

### Cambridge 0478 (IGCSE), §3.3 and §5.1

§3.3 rows 5 and 6: "Understand what is meant by cloud storage" ("can be accessed remotely in comparison to storing data locally") and "Explain the advantages and disadvantages of storing data on the cloud in comparison to storing it locally" ("Physical servers and storage are needed to store data in cloud storage"). §5.1 row 5: "Describe how web pages are located, retrieved and displayed on a device when a user enters a URL", including the role of the web browser, IP addresses, the DNS, the web server and HTML, which is Part II's journey in the syllabus's five nouns.

### IB Computer Science (2027 guide)

A1.1.9 "Describe the different types of services in cloud computing": SaaS, PaaS and IaaS and "the differences between the approaches … in various real-world scenarios, recognizing that different degrees of control and flexibility influence resource management and resource availability" (Example 5). A2.2.2 (HL) "Describe the function of servers", naming DNS, DHCP, file, mail, proxy and web servers with function, scalability, reliability and security as the factors. A2.2.3 "Compare and contrast networking models": client-server and peer-to-peer with "web browsing, email services, online banking, file sharing, VoIP services, blockchain" as the applications.

### Where this is *not* examined

AP Computer Science A: the term "API" appears only in the sense of a Java library's documentation; no networking or systems content. No board examines building a stack: the lab, the tiers' state rule, caching, load balancing, deployment and observability are beyond every syllabus here and are the reason the card exists.

## Beyond the syllabus

> [!info] The tail at scale
> Recall that the slowest 1 % of requests were three to four times the median in Part V. Dean and Barroso showed that a page assembled from 100 back-end calls, each with a 1 % chance of being slow, is slow on $1 - 0.99^{100} \approx 63\,\%$ of loads. Large systems therefore engineer the tail directly: they send the same request to two servers and take the first answer, or cancel a request that has run past the p99 and retry elsewhere.

> [!info] Horizontal and vertical
> Recall that the application tier scales by adding copies. That is **horizontal** scaling, and it has no ceiling but the database. **Vertical** scaling, a bigger machine, is what the database gets, because it is the tier that cannot be copied without the consistency problems of [[NoSQL and Distributed Data]]; it is also why the largest single machines in a company are always the database servers.

## Connections

- **Built on:** [[Programming Fundamentals]] (the code inside the application tier), [[The Internet and the Web]] (DNS, HTTP, cookies and the client-server questions), [[Relational Databases]] and [[SQL]] (the data tier; the lab's table), [[Program Development Life Cycle and Testing]] (the tests a deployment pipeline runs).
- **Tools used:** [[File Handling]] (JSON), [[Networks]] (TCP and the round trip), [[Encryption]] and [[Data Security]] (TLS; the untrusted boundary), [[Operating Systems]] (processes, threads and the socket's backlog), [[Hash Tables]] (what a cache is underneath).
- **Beside:** [[NoSQL and Distributed Data]] (the data tier when one machine is not enough), [[Big-O Notation]] (why the database's query, not the code, dominates).

## Sources

- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures* (doctoral dissertation, UC Irvine), chapter 5. The REST constraints, statelessness among them.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. Chapters 1 and 5 for the state line, replication and the cost of more than one database.
- Dean, J., & Barroso, L. A. (2013). The tail at scale. *Communications of the ACM*, 56(2), 74–80. The 63 % calculation and hedged requests.
- Wiggins, A. (2011). *The Twelve-Factor App*. 12factor.net. Configuration in the environment, stateless processes, logs as streams.
- Fielding, R. T., Nottingham, M., & Reschke, J. (2022). RFC 9110: HTTP Semantics. Methods, status codes and the request-response contract.
- Little, J. D. C. (1961). A proof for the queuing formula $L = \lambda W$. *Operations Research*, 9(3), 383–387.
- Python documentation, `http.server`, `socketserver` (`request_queue_size`) and `sqlite3` (`timeout`). The two defaults that decided the lab's first run.
- Measurements: `tech-stack-lab.py` on an Apple M1 Max, Python 3.11, 2026-09-22, saved in `tech-stack-lab.json`.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $L = \lambda W$ | `L = \lambda W` | Little's law: requests in flight = arrival rate × latency |
| $1 - 0.99^{100}$ | `1 - 0.99^{100}` | The tail at scale: chance that one of 100 calls is slow |
| $\text{servers} = \lceil \lambda / c \rceil$ | `\lceil \lambda / c \rceil` | Capacity division, before headroom |

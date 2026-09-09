---
chinese: 太空旅行 (tàikōng lǚxíng) — 一局 75 美元的游戏，和它换来的操作系统
prerequisites:
  - "[[Operating Systems]]"
leads_to:
  - "[[A, B, C]]"
  - "[[Two Family Trees]]"
  - "[[A Rich Neighbor Named Xerox]]"
  - "[[Decouple and Recouple]]"
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - cast/thompson
  - cast/ritchie
  - region/usa
---

# Space Travel 太空旅行

> *An operating system exists because a video game was too expensive to play. That sentence sounds like a joke about programmers. It is instead a documented fact about the operating system whose descendants now run every Android phone, every iPhone, every Mac, and most of the internet — and the receipt survives: seventy-five dollars a game.*

## Cast of Characters

- **Ken Thompson** (b. 1943) — Bell Labs programmer; wanted to fly a spaceship, ended up building the machine the world now runs on.
- **Dennis Ritchie** (1941–2011) — his partner in the corner room; later wrote the history down, which is why this card can quote receipts instead of legends.
- **The PDP-7** — a cast-off minicomputer with one redeeming feature: a beautiful display. The little machine nobody wanted.
- **The Patent Department** — three typists who became, without knowing it, the first Unix users in history — and its rescuers.
- **Bell Labs management** — recently burned, in no mood to fund another operating system; the story happens around them.

## 中文锚点

你手机里的安卓、苹果电脑里的 macOS、支撑大半个互联网的服务器系统，全都是同一个操作系统的后代——而那个祖先的诞生，起因是**一个玩不起的游戏**。1969 年，贝尔实验室的 Ken Thompson 写了个叫《太空旅行》的游戏：真实太阳系、真实引力，你驾驶一艘小飞船在行星和卫星之间穿行、尝试着陆（那年夏天阿波罗 11 号真的登月了——一个七月，两场着陆）。问题是游戏跑在大型机上，**打一局要 75 美元的机时费**——1969 年的 75 美元！于是他找到了一台没人要的旧机器：一台 PDP-7 小型机，配着一块漂亮的圆形显示屏。为了在这台"简陋寒酸"（Ritchie 的原话）的机器上跑游戏，他们从零写了浮点运算包、图形软件、调试器——**为了白嫖游戏，把整套家底都造了出来**。然后顺理成章：机器上什么都没有，Thompson 就把早就画在黑板上的"粉笔文件系统"实现了出来，又照着 Ritchie 那句名言——"没有办法去使用的文件系统，只是一纸空谈"（*a file system without a way to exercise it is a sterile proposition*）——补上了进程、外壳（shell）、编辑器、汇编器。传说中的那一个月：妻子带孩子探亲去了，他**每样花一个星期**，一个月后，操作系统有了。这个系统后来叫 UNIX。管理层刚从失败的 Multics 项目里撤出来，坚决不肯再为操作系统买机器——所以 Unix 是**不打报告、用角落里的破机器偷偷造出来的**；救它命的是专利部：三位打字员需要一套能排版、打印专利申请的系统，Unix 靠"会排版"这个承诺换来了第一台正经机器。寓意有两层：**约束逼出创造**（没钱买机时、没有现成软件，反而造出了一切）；以及**玩，是最被低估的研发预算**——你身边每一台计算机，都是那局 75 美元游戏的曾孙。

## The Story

### Act I — The seventy-five-dollar game

In 1969, Ken Thompson wrote a video game. Not a toy: *Space Travel* was, in Dennis Ritchie's words, "nothing less than a simulation of the movement of the major bodies of the Solar System, with the player guiding a ship here and there, observing the scenery, and attempting to land on the various planets and moons." Real orbits, real gravity — the same $GM/r^2$ that [[Gravitational Fields]] derives — with the player as a one-person space program. Hold the date in mind: the summer Thompson was making simulated landings in a New Jersey basement was the summer Apollo 11 made the real one. Two landings, July 1969.

![[space-travel-two-landings.png|620]]

The game ran first on Multics, then — after Bell Labs abandoned that project — was rewritten in Fortran for GECOS on the big GE 635 mainframe, where it developed two fatal problems. Ritchie recorded both with an engineer's precision: "the display of the state of the game was jerky and hard to control because one had to type commands at it, and second, a game cost about $75 for CPU time on the big computer." Seventy-five 1969 dollars — several hundred today — *per game*, billed to the department, for the privilege of flying a spaceship badly by typewriter.

![[space-travel-invoice.png|620]]

### Act II — The cast-off with the beautiful screen

The solution was lying around the building. Ritchie again: "It did not take long, therefore, for Thompson to find a little-used PDP-7 computer with an excellent display processor; the whole system was used as a Graphic-II terminal." A cast-off — [[A, B, C]] describes the same machine as "cramped and spartan even for the time": 8K words of memory, 18 bits each, and no software of any use. But the screen was gorgeous, and machine time on a machine nobody wanted is *free*.

Free, that is, except for the small matter that the machine had nothing on it. What follows is one of the great sentences of self-inflicted engineering, verbatim from Ritchie: "The undertaking was more ambitious than it might seem; because we disdained all existing software, we had to write a floating-point arithmetic package, the pointwise specification of the graphic characters for the display, and a debugging subsystem that continuously displayed the contents of typed-in locations in a corner of the screen." To play a game for free, they built an arithmetic library, a graphics stack, and a live debugger — from nothing, for a machine with no future. Every program had to be written on the GE mainframe in another room and carried over as punched paper tape: each iteration of the game was a corridor walk.

They got the game running. By the accounts of everyone who played it, landing on a planet with real gravity was genuinely hard, and genuinely wonderful.

### Act III — The month

Here the story turns, on a piece of chalk. Thompson, Ritchie and colleagues had spent time after the Multics retreat sketching operating-system ideas on blackboards — including a file system design that existed only as drawings. Ritchie: "Soon Thompson began implementing the paper file system (perhaps 'chalk file system' would be more accurate) that had been designed earlier." And then the sentence that explains why a game console became a computer: **"A file system without a way to exercise it is a sterile proposition, so he proceeded to flesh it out with the other requirements for a working operating system, in particular the notion of processes."**

The chronology of what happened next is the most famous month in software. As Thompson has told it in interviews ever since: his wife took their infant son to California to visit family, leaving him alone for a month — and he allotted **one week each** to the operating system kernel, the shell, the editor, and the assembler. A week, a week, a week, a week; when the family came home, the PDP-7 no longer needed the corridor walk or the mainframe. It could edit, assemble, and run its own programs, on its own file system, under its own processes. The system soon acquired a name — a pun on the departed Multics, coined in the group: where Multics did many things, this little system did one thing at a time. **Unix.**

Read the causal chain in full, because no single step planned the destination: a game too expensive to play → a free machine with nothing on it → tools built to serve the game → a chalk file system made real to have something to exercise → processes to make the file system mean something → a kernel, shell, editor and assembler so the machine could stand alone. Nobody set out to build the world's operating system. Each step just solved the problem directly in front of it — and the game was the first domino.

### Act IV — Built by not asking

The honest edge: none of this was supposed to happen. Bell Labs had just crawled out of Multics — Ritchie's history notes "the increasing obviousness of the failure of Multics to deliver promptly any sort of usable system" — and management wanted nothing more to do with operating systems. Thompson and Ritchie's repeated proposals to buy a proper machine (they wanted a DEC PDP-10) to build their system on went nowhere; the reception, as the history records it, was that *"Bell Laboratories just doesn't do business this way!"* So Unix was built the other way: no proposal, no budget line, no permission — a cast-off machine, spare hours, and a video game as the cover story. It is the institutional twin of the technical story: the constraint (no money, no machine, no mandate) did not merely fail to stop the work. It *shaped* the work into something small, direct, and finishable.

### Act V — Saved by three typists

By 1970 the PDP-7 was aging and Unix still had no official existence. The rescue came from the least glamorous direction imaginable: Bell Labs' **Patent Department** needed a system for preparing patent applications — real formatting, numbered lines, exact layouts — and the Unix group promised their text-formatter, *roff*, could do it. On that promise, a new PDP-11 arrived. Ritchie: "During the last half of 1971, we supported three typists from the Patent department, who spent the day busily typing, editing, and formatting patent applications, and meanwhile tried to carry on our own work." The world's first Unix installation was, in production terms, a typing pool.

And it worked — in both directions. Ritchie: "Not only did the Patent department adopt Unix, and thus become the first of many groups at the Laboratories to ratify our work, but we achieved sufficient credibility to convince our own management to acquire one of the first PDP 11/45 systems made." The system smuggled in as a game, kept alive as a typing service, now had a real machine, real users, and a future. What happened on that future — the language that grew up alongside it, B becoming C, the kernel rewritten — is [[A, B, C]]'s half of the room; where the kernel's descendants went next is [[Two Family Trees]].

## Cultural ripples

The obvious ripple is everything: the phone in your pocket runs a descendant of the system in this card, and so does the server that sent you this page. But the two durable lessons are quieter.

**Play is the most underrated R&D budget in history.** The chain from "I want to play my game for free" to "the world's operating system" was not a fluke of 1969; it is a pattern. The same labs' Karel-style toys, the games that drove graphics cards until the graphics cards started driving AI ([[You Never Expect the Change of Needs]]'s reverse thesis), the demoscene programmers who became the games industry — seriously pursued play keeps producing serious infrastructure, because play supplies the one thing funded projects struggle to buy: a builder who genuinely wants the thing to work.

**Constraints shaped the philosophy.** Multics had money, mandate, and three organisations — and failed by trying to do everything. Unix had 8K words, no budget, and one user at a time — and its enforced smallness hardened into the design philosophy its descendants still preach: do one thing well, make programs compose, keep the core small. The famous minimalism of Unix was not first an aesthetic. It was a *room*: the philosophy is the shape of the corner the system was built in, kept long after the corner was outgrown.

## Where this surfaces in the vault

- [[A, B, C]] — the language half of the same room: the paper-tape corridor walks, B squeezed into this same PDP-7, and the succession that ends in C. This card is the machine-and-month half that story reserved.
- [[Operating Systems]] — the technical card for everything Thompson built in his four weeks: file systems, processes, the shell. That card is the government; this one is its founding myth.
- [[Compilers and Interpreters]] — the assembler week, and why a machine that can translate its own programs stops needing a corridor.
- [[Gravitational Fields]] — the physics inside the game: Space Travel's planets pulled with the real inverse-square law, and landing was hard for exactly the reasons that card's orbital-energy section explains.
- [[Two Family Trees]] — where the kernel went: the Unix family tree this card plants the seed of.
- [[You Never Expect the Change of Needs]] — the sibling lesson: consequences no one budgets for, in both directions.

## Receipts

- Dennis M. Ritchie, "The Evolution of the Unix Time-sharing System" (1979/1984) — the source of every quoted sentence: the Space Travel description, the $75 game, the "little-used PDP-7 with an excellent display processor," the "disdained all existing software" inventory, the chalk file system, the "sterile proposition" line, the Patent-department passage and the PDP-11/45 ratification.
- Ken Thompson's own telling of the one-month, week-each chronology — most fully in the 2019 Vintage Computer Federation East interview with Brian Kernighan; also in Peter Salus, *A Quarter Century of UNIX* (1994).
- The Unix Heritage Society's PDP-7 Unix pages — the machine's specifications and the restored PDP-7 Unix source itself, which still runs.
- Apollo 11: 20 July 1969 — the same summer, for the record and the comic.

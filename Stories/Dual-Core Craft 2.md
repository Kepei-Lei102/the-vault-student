---
chinese: 双核星际 (shuānghé xīngjì)
prerequisites:
  - "[[Parallel and External Sorting]]"
leads_to:
  - "[[Pipelining and Simultaneous Multithreading]]"
  - "[[Concurrency]]"
tags:
  - type/story
  - subject/computer-science
  - domain/parallel-computing
  - era/20c
  - era/21c
---

# Dual-Core Craft 双核争霸

> *Your computer has sixteen cores. **StarCraft** is using two of them, and one of those is just drawing the picture. The other fourteen are watching a single core sweat through a battle it cannot keep up with — and the reason is a promise the game made, in 1998, to a 28.8k modem.*

## Cast of Characters

This is a story with no human villain — the protagonist is **the simulation itself**, and the antagonist is the **shape of the problem**. The named figures are mostly the engineers who diagnosed the trap or built the way out:

- **StarCraft** (Blizzard, 1998) & **StarCraft II** (2010) — the patient. A real-time strategy game whose whole world runs on essentially **one thread**, jokingly nicknamed *"Dual-Core Craft."*
- **Mark Terrano & Paul Bettner** — *Age of Empires* engineers who, in 2001, wrote down *why* RTS games must work this way (*"1500 Archers on a 28.8"*).
- **Herb Sutter** — the C++ architect who, in March 2005, announced the end of the era in three words: *"The free lunch is over."*
- **Mike Acton, Timothy Ford, and the data-oriented crowd** — the engineers who rebuilt game logic so it could finally spread across cores (data-oriented design; Overwatch's ECS engine, 2016).

## 中文锚点

**双核星际**（shuānghé xīngjì）：《星际争霸》系列的核心模拟（simulation）几乎只跑在**一个线程**上，所以无论你的 CPU 有多少核，它实际上只用得上约两个核（一个算游戏逻辑、一个画面），玩家戏称 *"Dual-Core Craft"*。后期 200/200 大决战时，成千上万单位的运算压垮那唯一的核，帧数暴跌，而其余核心闲着。

**为什么只用一个核？** 答案在**网络同步**。RTS 不传输"世界状态"（上千单位的坐标血量太大），只传输每个玩家的**操作指令**（commands）；每台机器跑**完全相同**的模拟，各自重建出一致的世界——这叫**锁步确定性模拟**（deterministic lockstep）。代价是：每台机器必须**逐比特一致**，否则"掉线不同步"（desync）。而保证确定性最便宜的办法，就是**单线程**——多线程的调度顺序本身是不确定的。

这正是 [[Parallel and External Sorting|并行排序]] 里 **Amdahl 定律**的故事：模拟是那段无法并行的"串行部分"，再多核也救不了它。后来游戏行业用**任务系统**与 **ECS（实体-组件-系统）**架构，把能独立的部分拆开并行——*恰好是这座知识库自己的组织方式*。

## Act I — "Dual-Core Craft"

The original *StarCraft* shipped in 1998, when a fast CPU had exactly one core, so nobody thought twice: the game ran on that one core and it was fine. The strange part is *StarCraft II*, which arrived in **2010**, deep into the multicore age — quad-core desktops were ordinary, and the industry had spent five years learning to use them. Yet SC2 leaned, then as now, on a small number of *fast* cores and largely ignored the rest. Benchmark it on a modern 16-core chip and you will watch one core pegged at 100% while the others idle, and the community verdict stuck: **"Dual-Core Craft"** — a game that, no matter what you give it, behaves like it has two cores, one for thinking and one for drawing.

You feel it at the worst possible moment. A late-game 4v4 with both sides maxed at 200 supply is well over a thousand units, each pathfinding, targeting, and firing every tick. The single simulation core saturates, and the whole game stutters — not because the *graphics* are too heavy, but because the *logic* cannot keep pace. The fourteen idle cores cannot help, and that is the mystery: why, in 2010, would Blizzard ship a flagship game that throws away most of your processor?

![[dual-core-craft-one-core-comic.png|697]]

The answer is not laziness. It is a contract the genre signed decades earlier, and could not break.

## Act II — The lockstep bargain

Picture the problem an RTS faces on a network. Eight players, each commanding hundreds of units. To keep every player's screen showing the *same* battle, the machines must agree on the state of the world many times a second. The obvious way — have one machine compute the world and **send the state** to everyone — is hopeless: a thousand units, each with a position, a health value, a target, an order queue, is a flood of data that no 1998 modem could carry, and that is wasteful even today.

The RTS answer, written down by *Age of Empires*' Mark Terrano and Paul Bettner in their 2001 talk **"1500 Archers on a 28.8"**, inverts it. Don't send the *state*; send the **commands**. A player issues only a handful of clicks per second — *select these twelve units, attack-move there*. That is a trickle of data. Ship just the commands, and let **every machine run the identical simulation** from the identical starting point. If the simulations are truly identical, all eight machines independently arrive at the very same thousand-unit battle, having agreed on almost nothing but the clicks. This is **deterministic lockstep**.

> This is, quietly, a compression scheme of the kind [[Information Theory]] describes. The full game state is *reconstructible* from the command stream plus the fixed rules of the game, so the commands **are** the compressed representation — kilobytes of clicks standing in for a world of units. It is also why an hour-long replay file is tiny: it stores your clicks, not your battles, and re-derives everything else by replaying the simulation.

But the bargain has a merciless clause. *"Identical"* means **bit-for-bit identical, on every machine, forever.** Let one machine compute a unit's position one ten-thousandth differently — a floating-point rounding that reorders, a random number drawn in a different sequence — and from that tick on, the two worlds drift apart. One player sees the marine live; another sees it die. The game calls this a **desync**, and there is no recovering: the match simply ends.

So determinism is not a nice-to-have; it is the load-bearing wall. And here is the hinge of the whole story: **the cheapest way to guarantee determinism is to use one thread.** Multithreading is, by its nature, *non*-deterministic — the operating system interleaves threads in a different order every run, two cores race to touch the same data, and a sum computed in parallel can come out in a different order than the same sum computed again. Tame all of that and you *can* build a deterministic multithreaded simulation — but it is fiendish, and in 1998 it was not worth attempting. One thread runs operations in one fixed order, the same order on every machine, every time. The simulation was kept single-threaded **by contract, not by accident.**

## Act III — The free lunch ends

For decades that contract cost nothing, because single cores kept getting faster. Every year clock speeds climbed, and *all* software — RTS simulations included — got quicker for free, without a line of code changing. Programmers had a name for it nobody bothered to say aloud: the free lunch.

In **March 2005**, the C++ architect **Herb Sutter** ended it with an essay titled *"The Free Lunch Is Over."* The physics had run out of room: clock speeds had slammed into a wall near 3–4 GHz, where pushing faster meant melting the chip. The industry pivoted hard — not to *faster* cores, but to *more* of them. From that moment, a single-threaded program was **frozen in time**: it would never run meaningfully faster again, no matter how many cores the future delivered.

![[dual-core-craft-free-lunch-comic.png|697]]

This is exactly **Amdahl's law** from [[Parallel and External Sorting]]. If a fraction of your work is stuck running serially, the speedup from extra cores has a hard ceiling of $1/(\text{serial fraction})$ — and a fraction that *cannot* be parallelized gets *nothing* from more cores. StarCraft's simulation is that serial fraction made flesh: **Amdahl's law wearing a Zerg costume.** The lockstep bargain that once let a 28.8k modem carry an army had become, by 2010, the chain bolting the whole game to a single core while fifteen others looked on.

## Act IV — The slow climb back

The rest of the industry could not afford to stand still, because the consoles forced the issue. The **Xbox 360** (2005) shipped with three cores and six hardware threads; the **PlayStation 3** (2006) shipped the alien **Cell**, a chip whose power lived entirely in parallel co-processors. You could not ship a competitive game that left five-sixths of the machine idle. Necessity did what elegance could not, and game engines re-learned parallelism in roughly four moves:

1. **Split the render thread off the game thread.** The first and easiest win — one core advances the world, another draws it. Ironically, this *is* the "dual-core" picture: two cores, one thinking, one drawing.
2. **Job systems.** Stop thinking in *threads* and start thinking in *jobs*: chop a single frame into hundreds of small, independent tasks — animate this skeleton, cull that room, simulate these particles — and throw them at a pool of worker cores. Naughty Dog's *"Parallelizing the Naughty Dog Engine Using Fibers"* (GDC 2015) is the famous account; DICE's Frostbite and Unreal's task graph are the same idea.
3. **Data-oriented design.** The deeper rewrite, preached by **Mike Acton** (CppCon 2014): stop arranging data the way the *programmer* thinks — one fat Object per entity, scattered across memory — and arrange it the way the *hardware* wants — the same field for every entity, packed into one tight array the CPU can stream through.
4. **ECS — Entity-Component-System**, the architecture that ties it together. Entities become bare IDs; **components** are plain data living in contiguous arrays; **systems** are loops that sweep over those arrays. This wins twice at once. The packed arrays are cache-friendly (it feeds the memory hierarchy the way [[Pipelining and Simultaneous Multithreading|the CPU pipeline]] is starving to be fed), *and* — crucially — the data dependencies become **explicit**. A scheduler can see that a movement system (which writes positions) and a damage system (which writes health) touch different components, and so it can safely run them **on different cores at the same time**.

Blizzard's own **Overwatch** team put ECS on the AAA map with Timothy Ford's 2017 GDC talk on the game's architecture, and Unity productized the whole pattern as **DOTS**. The discipline that StarCraft's contract forbade had finally been engineered back into the genre.

## Act V — The irony, kept honest

Here is the twist the tidy version hides. The kind of game that needs parallelism *most* — a massive simulation of thousands of mutually-interacting units — is exactly the kind that determinism makes *hardest* to parallelize. And Overwatch, the poster child for the cure, **never actually had StarCraft's disease.** Overwatch is a 6v6 (later 5v5) hero shooter — a few dozen entities, run on an authoritative server with client-side prediction, *not* lockstep. Its ECS payoff was code clarity and clean netcode, not a thousand-units crisis it never faced. It is a different *shape* of game. "Overwatch solved what StarCraft couldn't" is too neat: they were never fighting the same battle.

The honest heir to StarCraft's problem is **Factorio** — a factory-builder whose deterministic-lockstep multiplayer simulates *hundreds of thousands* of belts, machines, and biters in perfect sync. Its developers' public *Friday Facts* devblog is a running lab notebook of this exact fight: they parallelize the genuinely independent subsystems (pollution spread, parts of pathfinding, fluid flow) and keep the core update **serial**, because lockstep forbids the non-deterministic ordering that multithreading invites. That is the [[Parallel and External Sorting|parallel-sort]] lesson lived out in a shipping game — *parallelize what is independent, accept the serial tail* — and it is why Factorio runs enormous factories on hardware that should not manage them.

Two more honest edges. **"Dual-Core Craft" is a meme that flatters itself with precision** — SC2 does spin up extra threads for audio and asset streaming — but the load-bearing truth survives: its *simulation* is effectively one thread, and its performance scales with one or two fast cores, not with core *count*. And **ECS was not Overwatch's invention.** Component-based game-object systems go back to the early 2000s — Scott Bilas's *Dungeon Siege* engine (GDC 2002), the Thief/Dark engine, and Adam Martin's blog series that fixed the *"Entity System"* name around 2007. Overwatch *popularized* ECS; it did not originate it — a clean case for [[Stories/Stigler's Law of Eponymy]], where the name attaches to whoever explained it best, not whoever did it first.

## Cultural ripples

**Why an old game still wants the newest single-core speed.** "Dual-Core Craft" is why competitive RTS players and emulator enthusiasts chase CPUs with the highest *per-core* clock rather than the most cores — the serial simulation only knows how to spend one core's worth of speed, so that is the one number that matters. A decade of "more cores!" marketing simply does not reach it.

**The genre paid for it.** It is not a coincidence that the golden-age RTS faded as CPUs went wide. A game design built on *thousands of units in one deterministic simulation* sits on the exactly wrong side of the hardware trend — the work it most wants to scale is the work Amdahl's law forbids it to scale. The survivors either shrank the unit count (MOBAs: a handful of heroes), moved authority to a server (shooters), or, like Factorio, poured years of engineering into squeezing parallelism out of the few places determinism allows.

**The same architecture, organizing this vault.** Here is the closing turn. The pattern that finally let a game spread across your cores — **Entity-Component-System** — is the one this knowledge bank is built on. In the Vault, folders are decorative; the real structure is **entities** (the cards) wearing **components** (their frontmatter, tags, and `prerequisites`/`leads_to` links), swept by **systems** (the subject Directories, the frontmatter graph, the search protocol). The thing that freed Overwatch across a CPU is the thing that lets a vault be reorganized without moving a single file. An idea born to make a video game run faster turns out to be a good way to arrange *any* world made of many small, independent, data-carrying things — including this one.

## Where this surfaces in the vault

- **The pedagogical home:** [[Parallel and External Sorting]] — *parallelism changes time, not work, and only when the work is independent.* This Story is that card's thesis dressed in a Zerg costume: the RTS simulation is the canonical **dependent** workload, and Amdahl's law is the verdict.
- **The next card it foreshadows:** [[Pipelining and Simultaneous Multithreading]] — *why* a single fast core can do so much (and why ECS's packed arrays feed it so well) is the pipeline-and-SMT story.
- **The compression insight:** [[Information Theory]] — lockstep ships commands, not state, because the commands are the compressed representation of the world.
- **The eponymy footnote:** [[Stories/Stigler's Law of Eponymy]] — "Overwatch's ECS" as a textbook case of a pattern named for its popularizer, not its inventor.
- **A sibling technology-history Story:** [[Stories/The Boolean-to-Silicon Bridge]] — the other "an idea becomes the infrastructure we live inside" arc.

## Receipts

- Mark Terrano & Paul Bettner, **"1500 Archers on a 28.8: Network Programming in Age of Empires and Beyond"** (GDC 2001 / Gamasutra) — the canonical statement of the deterministic-lockstep model: send commands, not state; every machine simulates identically; desync as the failure mode.
- Herb Sutter, **"The Free Lunch Is Over: A Fundamental Turn Toward Concurrency in Software"** (*Dr. Dobb's Journal*, March 2005) — the end of automatic single-core speedups and the pivot to multicore.
- Christian Gyrling, **"Parallelizing the Naughty Dog Engine Using Fibers"** (GDC 2015) — the job-system / fiber approach to frame-level parallelism.
- Mike Acton, **"Data-Oriented Design and C++"** (CppCon 2014) — the manifesto for arranging data for the hardware, the intellectual root of ECS.
- Timothy Ford, **"Overwatch Gameplay Architecture and Netcode"** (GDC 2017) — ECS in a shipping AAA game; note its emphasis on decoupling and netcode over raw multicore scaling.
- Scott Bilas, **"A Data-Driven Game Object System"** (GDC 2002) — an early component-based object system (*Dungeon Siege*), part of the case that ECS predates its 2010s fame.
- Wube Software, **Factorio "Friday Facts"** devblog (e.g. the multithreading and update-loop entries) — a working studio's public account of parallelizing only the independent subsystems of a deterministic-lockstep simulation.
- On "Dual-Core Craft": community benchmarking of *StarCraft II*'s single-thread-bound simulation and its scaling with per-core clock speed (general RTS-performance discussion; treat the nickname as a meme that captures a real, if imprecise, truth).

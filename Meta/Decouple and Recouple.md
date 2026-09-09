---
chinese: 解耦与再耦合 (jiě'ǒu yǔ zài'ǒuhé)
prerequisites:
  - "[[Forward Reading and Problem Discovery]]"
  - "[[Secondary Storage]]"
  - "[[Sensors and Control Systems]]"
  - "[[Space Travel]]"
leads_to:
  - "[[Program Design]]"
  - "[[The True IO Bound]]"
tags:
  - subject/methodology
  - subject/computer-science
  - subject/physics
  - domain/systems-design
  - domain/engineering
  - domain/cognition
  - level/A-Level
  - level/university
  - level/life
  - type/methodology
  - type/meta
  - type/cross-domain
  - misconception/decoupling-is-always-good
  - misconception/a-buffer-adds-speed
---

# Decouple and Recouple 解耦与再耦合

> *Coupling is not a sin. It is an axis. The engineer you want to become is not the one who decouples everything — it is the one who can name the axis, say which side this coupling serves, and execute either move on demand.*
> *And the second move is the creative one: take a part out of the world it was built for, and put it somewhere it was never meant to go. Most of the best inventions in this vault were made that way — and most of them were forced into it by a constraint.*

## What this card is for

Half of the hardware cards in this vault end up describing the same object under different names. A **buffer** between a CPU and a printer. A **cache** between a core and main memory. A **synchronizer** between two clock domains. A **queue** between a game's simulation thread and its renderer. An **interface** between the code that calls and the code that answers. Each is introduced as a local trick for a local problem; each is in fact one idea — *break the coupling between two things that were forced to move together* — and the idea deserves to be seen whole.

But the moment you write that idea down, its opposite arrives uninvited. A database **transaction** exists to couple several writes so that they *cannot* be separated. A thermostat's **feedback loop** wires an output back into an input on purpose. A racing car's rigid drivetrain couples the wheel to the throttle so tightly that the driver can feel the track through it, and every attempt to soften the coupling makes the car worse. If decoupling were simply good, these would be mistakes. They are not; they are the point.

So this card has two theses, and the second is the one that makes the first worth having:

1. **Coupling is a design axis, not a defect.** Some couplings are pure cost, and engineering's canonical decouplers exist to break them. Some couplings *are* the product. The skill is choosing — and being able to execute both moves.
2. **Recoupling is how new things get made — and the decoupling that precedes it is usually forced by a constraint.** The great move is to take a component out of the context it was designed for and recouple it somewhere it was never meant to be: a phone's gyroscope inside a drone, a bush's pixels as a cloud, a truck trailer on a ship. In almost every case the builder did not choose to shop in other people's parts bins. They had no budget, no memory, no machine — and the constraint *found* the recombination for them.

### 中文锚点

先想两个你每天都碰到的东西。**网课卡了**，画面转圈——那个圈就是缓冲区在装满：你的播放器提前存了几秒视频，网络抖一下，是这几秒被吃掉，而不是画面冻住。播放器和网络本来是**绑在一起**的——网络慢一拍，画面就慢一拍；缓冲区把这根绳子剪断了，两边各走各的节奏。这叫**解耦**。再想**手动挡汽车的离合器**：踩下去，发动机和车轮断开，你才能换挡；松开，两边重新咬合，车才走。**踩离合是解耦，松离合是再耦合**——而车只有在耦合状态下才是一辆车。这就是这张卡的第一个论点：**耦合不是错，是一条轴。** 有些耦合纯粹是成本（CPU 等打印机、画面等网络），工程上有一整套标准工具去剪断它：缓冲区、队列、缓存、接口、同步器、集装箱；有些耦合恰恰是产品本身（数据库事务把几次写入绑死，要么全成功要么全失败；恒温器把输出接回输入；赛车的传动系统硬到车手能"摸"到路面）。好工程师不是"什么都解耦"，而是能**说出这条轴叫什么、这个耦合服务于哪一边**，然后两个动作都会做。第二个论点更有意思：**再耦合是创造。** 大疆的无人机，里面的摄像头、陀螺仪、电池、无线模块，全是**为手机造的**——手机大战把这些零件打到几美元一个，大疆把它们从手机里拆出来，重新装成一架飞机；1985 年的《超级马里奥兄弟》，天上的云和地上的灌木是**同一张图换了颜色**，因为卡带里只塞得下 256 个图块；火箭分级是字面意义上的"飞到一半解耦"；Unix 的管道是把大任务拆成一个个只管一件事的小程序、再接起来。而且几乎每一次，拆开都不是自愿的——**是预算、内存、机器逼出来的。没钱的人只能去别人的零件箱里找，于是找到了别人没想到的组合。**

| English | 中文 | 一句话 |
|---|---|---|
| Coupling | 耦合 | 甲的节奏、状态或故障**牵着**乙走 |
| Decouple | 解耦 | 剪断那根绳子，让两边各走各的 |
| Recouple | 再耦合 | 有意把两样东西重新绑在一起——常常是绑到它本不属于的地方 |
| Buffer / queue | 缓冲区 / 队列 | 两种速度之间的等候区——最经典的解耦器 |
| Interface | 接口 | 一份契约：只约定"能做什么"，不约定"怎么做" |
| Atomicity (transaction) | 原子性（事务） | 把几步绑死：要么全发生，要么全不发生——**故意的**耦合 |
| Feedback | 反馈 | 把输出接回输入——**故意的**再耦合 |
| Constraint-forced | 约束逼出来的 | 不是选择去拆，是没钱没内存没机器，不得不拆 |

---

## Part I — Coupling is an axis

### What coupling actually is

Two things are **coupled** when one of them cannot do its job without the other cooperating *right now*. Take that definition apart and you find that "right now" can mean four different things, and naming which one you are looking at is most of the skill:

| The axis | What is bound together | The symptom when it hurts |
|---|---|---|
| **Timing** | A must wait for B to be ready | a fast CPU idling while a slow printer chews a page |
| **Failure** | if B breaks, A breaks | one bad device driver takes the whole machine down |
| **Knowledge** | A must know *how* B is built, not just *what* it does | change B's internals and A stops compiling |
| **Place** | A only works with *this* B, in *this* setting | a graphics routine that only runs on one machine |

Every decoupler in the next section attacks one of those four. Every "coupling that is the product" in the section after deliberately keeps one. When a card in this vault says *decouple*, ask *along which axis?* — the answer is rarely all four, and the tool is chosen by the axis.

### The canonical decouplers

Engineering has a small, old, well-tested kit for breaking couplings, and nearly every entry is already somewhere in this vault under a local name:

| Decoupler | Axis it cuts | Where you have already met it |
|---|---|---|
| **Buffer** | timing | the print buffer and the video player's loading bar in [[Secondary Storage]] |
| **Queue** | timing (and ordering) | the FIFO between a fast writer and a slow reader in [[Clock Domains and Metastability]]; the command queue of [[Dual-Core Craft]] |
| **Cache** | timing | every level of [[RAM and the Memory Hierarchy]] — the CPU stops waiting for DRAM |
| **Interrupt** | timing | [[Interrupt Handling]]: the CPU stops *polling* the device and lets the device ring a bell |
| **Interface / API** | knowledge | [[Program Design]]'s modules, [[Object-Oriented Programming]]'s encapsulation: callers know *what*, never *how* |
| **Synchronizer** | timing, at the physical limit | two flip-flops that let one clock domain talk to another in [[Clock Domains and Metastability]] |
| **Spool** | timing | the print spooler: the word is 1950s IBM — *Simultaneous Peripheral Operations On-Line* — a disk standing between every program and the one slow printer |
| **Kernel / process** | failure | [[Operating Systems]]: one crashing program no longer takes the others with it |
| **Error-correcting code** | failure (of the channel) | [[Error Detection and Correction]]: the message no longer depends on every bit surviving |
| **Container** | place | the shipping container — Part II |

The **buffer** is the canonical one, because it is the one you can put numbers on.

### See it: what a buffer actually buys

Take a **bursty producer** — a program that emits print jobs in clumps, a network that delivers video in ragged bunches — and a **steady consumer** that can handle exactly one item per tick. Put a buffer of capacity $B$ between them. With $B = 0$ they are directly coupled: an item can only be handed over if the consumer is free *at that instant*, so every burst beyond the first item is refused, and every quiet tick leaves the consumer idle. Then grow $B$.

![[decouple-and-recouple-buffer.svg|780]]

The top panel is a stretch of the simulation with $B = 8$: the buffer fills during a burst, drains during the quiet, and the consumer sees a far smoother stream than the producer ever sent. The bottom panel is the measurement, from two hundred thousand ticks per point, with the producer averaging $0.8$ items per tick:

| Buffer $B$ | Consumer idle | Producer blocked |
|---|---|---|
| 0 (direct) | 80% | 74% of output refused |
| 8 | 39% | 22% |
| 64 | 21% | 0.3% |

Two things are worth staring at. First, the consumer's idle time cannot fall below about 20%, because the producer only ever offers $0.8$ item per tick — **a buffer does not add capacity.** It cannot make the printer faster or the network wider. What it does is stop the two sides from paying for *each other's bad moments*: the burst no longer has to be refused, the lull no longer has to be idle. Second, the returns are steep at first and then flatten. A buffer of 8 cuts the refusal rate by two-thirds; going from 32 to 64 buys almost nothing. Every real buffer is sized on that curve, and every "why is this video player only caching ten seconds?" has the same answer: past the knee, memory is being spent on nothing.

The script that generated the figure is beside this card, and it is short enough to read in a minute. Change the burstiness, change the consumer's speed, and watch the knee move — that is the whole design problem of buffering, in twenty lines.

> [!tip] Study habits are the same curve
> Taking notes *during* a lecture at the lecturer's pace is direct coupling: every sentence you are still writing down is a sentence you are not hearing. Writing a few keywords and expanding them afterwards is a buffer — you and the lecturer stop paying for each other's timing. The knee is the same, too: a few words per idea is most of the benefit; a full transcript is memory spent on nothing.

### The couplings that are the product

Now the other side of the axis, because without it the first half is a slogan.

- **Atomicity.** A bank transfer is two writes: subtract from one account, add to another. A [[Relational Databases|database transaction]] exists to couple them so tightly that the world can never observe one without the other — either both happen or neither does. The whole apparatus of logs and locks that makes this true is *deliberate coupling*, and a system that "decoupled" the two writes for throughput would be a system that loses money.
- **Feedback.** [[Sensors and Control Systems]] is a card about wiring an output *back* into an input on purpose. The thermostat, the cruise control, the body's temperature regulation, reinforcement learning — every one of them is a coupling someone built, and loosening it (a longer delay, a laggier sensor) makes the loop worse or unstable. Here the coupling is not tolerated; it is the mechanism.
- **Lockstep.** [[Dual-Core Craft]] is the story of a game that coupled every player's machine to one deterministic timeline — bit for bit, forever — because that coupling let a 28.8 k modem carry a thousand-unit battle. It was the right call in 1998 and the chain that bolted the game to one core in 2010. Same coupling, both verdicts, and the card is honest about it.
- **The drivetrain.** A road car isolates the driver from the engine with soft mounts, a torque converter, a padded pedal. A racing car does the opposite: rigid mounts, a direct throttle, stiff suspension — because the driver *is* the control system, and every decoupling between hands and road is latency in the loop. [[From the Grid to the Garage]] is a hundred years of engineers deciding which of those couplings to keep for the road.
- **Matched impedance.** In physics the choice is explicit. To transfer *maximum power* from a source to a load, the load resistance must *equal* the source's internal resistance — the two are coupled by design, and the price is that half the power is lost in the source. To transfer a *signal* faithfully you do the reverse: make the load's input resistance huge, so it draws almost nothing and the source does not notice it. The same transformer of [[Electromagnetic Induction]] can be wound to do either. Neither is "correct"; the question is what you are transferring.

Look at the pattern across all five. The coupling is kept exactly when **the two things being coupled are supposed to be one thing** — one transfer, one control loop, one battle, one driver-and-car, one power circuit. It is broken when they were only ever two things that happened to be forced to move together.

### The two questions

So the discipline is not "decouple". It is two questions, asked in order:

1. **Which axis?** Timing, failure, knowledge or place. A coupling that hurts on one axis may be essential on another — a transaction is welded on the *failure* axis (they fail together) and may be perfectly free on the *knowledge* axis (neither write knows how the other is stored).
2. **Which side does this coupling serve?** If the two sides are one thing wearing two names, keep it and make it tighter. If they are two things paying for each other's bad moments, reach for the kit.

An engineer who can only answer "decouple" will eventually decouple a transaction. An engineer who can only answer "keep it simple, keep it together" will eventually bolt a game to one core. The wonderful ones can be handed either problem.

---

## Part II — Constraint-forced decoupling, and recoupling as creation

The first half was about breaking couplings that hurt. This half is about the move that makes new things: **decouple a component from the context it was built for, then recouple it into one it was never meant for.** Every example below is in the vault already, told as its own story; here they are laid side by side so the pattern shows — and the pattern has a second clause that is easy to miss. In almost every case, **nobody chose to decouple. A constraint forced it**, and the constraint is what found the recombination.

### The bush that is a cloud

The 1985 *Super Mario Bros.* cartridge held its entire graphics set in 8 KB — room for 256 tiles of 8×8 pixels, and not one more. The team has said plainly that the clouds in the sky and the bushes on the ground are **the same shape with the colours changed**: one set of tiles in graphics memory, two palettes, two objects on screen. Nobody sat down to design a cloud that looked like a bush. The tile budget *decoupled the shape from its colour* — a designer who could afford 512 tiles would never have noticed the two things could share — and then recoupled the same pixels to the sky.

![[decouple-and-recouple-bush-cloud.svg|700]]

It became an aesthetic. Players describe the look of that game as clean and coherent, and part of what they are describing is that the world was drawn from a very small alphabet, reused everywhere. The constraint did not merely permit the trick; it was the only reason anyone looked for it.

### The phone parts bin

Between roughly 2007 and 2012 the smartphone companies fought each other into producing, by the hundreds of millions, a set of components that had been military or laboratory equipment a decade earlier: three-axis gyroscopes and accelerometers, tiny cameras, GPS receivers, radios, lithium cells, ARM processors. Chris Anderson, who founded the DIY Drones community in 2007, named the consequence: the personal drone is **"the peace dividend of the smartphone wars"** — every sensor a drone needs, available for a few dollars each, because someone else's war had paid for the factories.

A student who had founded a company in a Hong Kong university dorm in 2006, building flight controllers for hobbyists, was standing at that parts bin when it filled. In January 2013 **DJI** shipped the Phantom — the first quadcopter you bought whole, flew that afternoon, and that stayed level on its own — and became the largest drone maker on Earth. Almost nothing inside a Phantom was designed for a drone. The gyroscope was designed to rotate a phone screen; the camera sensor was designed for a selfie; the radio and the battery were phone parts. DJI's act was the recoupling: taking each component out of the pocket it was made for and putting it in the air.

Notice the shape of the constraint. DJI could not have designed a gyroscope; nobody starting in a dorm can build a MEMS fab. The absence of that option *forced* them into the phone's parts bin — and the phone's parts bin was, by then, better than anything a drone company could have designed for itself. [[From the Grid to the Garage]] tells the same story a few years earlier: the first Tesla Roadster carried 6,831 laptop cells because laptop cells were what a startup could buy, and that borrowed supply chain is now the reason electric cars exist at all.

### Staging — decoupling at 3 km/s

A rocket is a machine that must throw away most of itself to work. The rocket equation — derived in [[Linear Motion under a Variable Force]] — says the speed you can reach depends on the logarithm of the ratio of full mass to empty mass; and a single-stage rocket drags its empty tanks and its now-oversized engines all the way up. Konstantin Tsiolkovsky's answer, in *Cosmic Rocket Trains* (1929), was to **decouple in flight**: build the rocket as separable sections, burn one, drop the dead mass, and let the rest accelerate from a running start with less to carry. Every orbital launch since has done exactly this, and a literal explosive bolt fires at the moment of decoupling. Here the constraint is not money but physics — the tyranny of the logarithm — and it forced the most theatrical decoupling in engineering.

### Pipes — small tools, recoupled by composition

On 11 October 1964, Doug McIlroy wrote a memo at Bell Labs: *we should have some ways of coupling programs like garden hose — screw in another segment when it becomes necessary to massage data in another way.* Nine years later, in January 1973, Ken Thompson implemented it in Unix in a day: the **pipe**, `|`, which takes one program's output and feeds it to the next's input. The consequence was a whole philosophy — *write small programs that do one thing; make them compose* — and [[Space Travel]] says where that philosophy came from. It was not first an aesthetic. It was 8K words of memory on a cast-off machine: nothing large could be written, so everything had to be small, and small things must be recoupled to be useful. The corner shaped the system, and the pipe is the corner made into a tool.

### The box

Until 1956, cargo was loaded onto ships as it came — sacks, barrels, crates, each lifted by hand into the hold. The cargo was *coupled to the vehicle*: what fitted a truck did not fit a hold, and every transfer meant unpacking. Malcom McLean, a trucker, decoupled them: a standard steel box, sealed at the factory, lifted whole between truck, train and ship. On 26 April 1956 the converted tanker *Ideal-X* left Newark for Houston with 58 boxes on deck. Loading a ship by hand had cost about \$5.83 a ton; by container it cost under 16 cents. Marc Levinson's history of it is titled, exactly, *The Box*, and the argument of the book is that this one decoupling — cargo from vehicle — is most of what people mean by "globalisation". The recoupling is the modern port: cranes, trains and ships that exist only because the box is the same box everywhere.

### The vault you are reading

This vault is built the same way, and says so in its manual: *folders are decorative, not navigational.* A card is not coupled to its folder — its identity lives in its tags and its links, and a card on logarithms can be found from Number, from Functions and from Calculus at once, because what it *is* was never decided by where it was put. That is the **entity–component–system** architecture of game engines, described in [[Object-Oriented Programming]]'s last section, applied to a knowledge base: the entity is the card, the components are its frontmatter, the systems are the Directories and the search protocol that sweep every card carrying a tag. The decoupling (card from folder) was a design choice; the recoupling (any card, reachable from any subject that needs it) is why cross-domain bridges cost nothing here.

### Why the constraint finds it

Line the cases up and the second clause is visible in every one:

| The recoupling | The constraint that forced the decoupling |
|---|---|
| bush → cloud | 256 tiles |
| phone sensor → drone | a dorm-room company cannot build a fab |
| laptop cell → electric car | a startup cannot build a battery plant |
| rocket → separable stages | the logarithm in the rocket equation |
| small programs → pipes | 8K words and no budget |
| trailer → shipping container | the cost of loading a ship by hand |

The mechanism is simple once stated. **A builder with a budget designs the part they need.** A builder without one *cannot*, and is forced to look at parts that already exist — which means parts designed for someone else's problem. Most of those parts will not fit. But a few will fit *better* than anything the builder could have made, because they carry the investment of an entire other industry: a phone's gyroscope is the product of a war the drone company never had to fight. The constraint does not merely allow the recombination; it makes the builder *look where the recombinations are*, in the parts bin, where the well-funded never go.

This is [[Forward Reading and Problem Discovery]]'s hunter, working in the other direction. The hunter traces what a problem demands; the recoupler asks what already exists that could be made to answer it, and is willing to take a thing out of its context to find out. Both are causal reading. One reads forward from the question; the other reads sideways from the inventory.

> [!info] Recall that decoupling has an axis
> The second thesis is a special case of the first. To recouple a phone's camera into a drone, DJI first had to decouple it along the *place* axis — the sensor had to be usable outside the phone at all, which is why the parts that recombine best are the ones sold as standalone modules with a documented interface. A component welded to its original context on every axis cannot be recoupled anywhere; the parts bin only contains the things somebody already decoupled.

---

## Part III — Executing both moves

### A checklist for the decoupling move

When something is slow, fragile or stuck, before reaching for the kit:

1. **Name the two things.** Not "the system is slow" — *which* two components are waiting on each other?
2. **Name the axis.** Are they waiting on each other's *timing*, failing on each other's *failure*, or coupled by *knowledge* of each other's internals?
3. **Ask the second question.** Are these one thing wearing two names? If a database's two writes, a control loop's sensor and actuator, a game's simulation and its netcode — stop. That coupling is the product; make it tighter, not looser.
4. **Pick the decoupler for the axis.** Timing → buffer, queue, cache, interrupt. Failure → process boundary, error-correcting code, redundancy. Knowledge → interface, module boundary, a documented API. Place → standardise the container.
5. **Size it on the knee.** A buffer past its knee is memory spent on nothing; an abstraction layer nobody needs is code spent on nothing.

### A checklist for the recoupling move

When you need something you cannot build:

1. **Go to the parts bin first.** What industry has already solved a problem shaped like yours, at a scale you will never reach? Their overproduction is your budget.
2. **Check the part is decoupled on the axis you need.** Can it run outside its original context — is it a module with an interface, or a fragment welded to something else?
3. **Expect most fits to fail** and one to be better than what you would have designed. The bush that becomes a cloud is a lucky tile; most tiles do not recolour into anything.
4. **Keep the constraint honest.** If you *could* have built the part, the recoupling is a shortcut and should be judged as one. The move is strongest exactly when there was no alternative — that is when the parts bin gets searched properly.

### Where each move goes wrong

- **Over-decoupling.** Every buffer adds latency; every interface adds a layer to read through; every process boundary adds a copy. A system decoupled on all four axes at once is a system where nothing can find anything and every request crosses six boundaries to do one thing. The large-software version of this is well known enough to have jokes about it, and the cure is Part I's second question, asked about each boundary in turn.
- **Decoupling a transaction.** Loosen a coupling that was the product, and the failure is not slowness but wrongness: a transfer that debits without crediting; a control loop that oscillates because its feedback arrives late; a lockstep game that desyncs. These are not performance bugs and no amount of tuning fixes them.
- **Recoupling by wishful thinking.** A part that was never decoupled from its context does not become modular because you want it to. Half of every integration nightmare is a component that only ever worked inside the thing it came with.
- **Mistaking the borrowed part for the invention.** DJI did not invent the gyroscope; Tesla did not invent the 18650 cell; Unix did not invent the small program. The invention was the recoupling — and it is real invention, defended by the fact that nobody else, with the same parts bin in front of them, did it.

---

## Misconceptions

1. **"Decoupling is always good."** It is good on the axis where the coupling was costing you and neutral-to-harmful everywhere else. The five couplings-that-are-the-product above are the counterexamples; decoupling any of them produces a wrong system, not a slow one.
2. **"A buffer makes things faster."** A buffer changes *who waits*, not *how much work gets done*. The consumer's idle floor in the simulation — about 20% — is set by the producer's average rate, and no buffer on Earth lowers it. What the buffer removes is the *coupled* waiting: the refusals and the idles that each side paid for the other's bad timing.
3. **"Coupling means dependency."** A module can *depend* on another (it calls it) without being *coupled* to it on the knowledge axis (it does not care how the callee is built). The whole point of an interface is dependency without coupling. Conflating the two is why students "decouple" by deleting the dependency and then rebuilding the function inside the caller — which is coupling made total.
4. **"Recoupling is just copying."** Using a phone camera in a drone, a laptop cell in a car, a bush as a cloud — none of these was obvious to the people who owned the parts. The evidence is that the phone companies did not make drones and the laptop companies did not make cars. The recombination is the work.
5. **"Constraints are the enemy of invention."** The table in Part II is six inventions, each with the constraint that produced it in the next column. The honest version of the claim: constraints are the enemy of *designing the part you need*, which is exactly what forces you to find the part you did not know existed.

---

## How to use this card

1. **The next time a card says "buffer", "cache", "queue", "interface" or "synchronizer",** say to yourself which of the four axes it is cutting. After a few cards the local names dissolve and one idea is left.
2. **The next time a card says "atomic", "lockstep", "feedback" or "matched",** notice that it is describing a coupling someone chose to keep, and ask what would break if it were loosened. That question is usually the exam question in disguise.
3. **When you are stuck for lack of a part** — an experiment you cannot afford, a dataset you cannot collect, a program you have no time to write — search the parts bin before the design bench. Somebody else's overproduction is the cheapest thing in the world.
4. **When you catch yourself adding a layer,** ask Part I's second question about it out loud. If the answer is "the two sides are one thing", take the layer out.

---

## Connections

- **Parents:**
   - [[Forward Reading and Problem Discovery]] — the hunter traces what a problem demands; this card's recoupler reads sideways from what already exists. Both are causal reading, in different directions.
   - [[Secondary Storage]] — the buffer, in its original home: the print buffer, the streaming buffer and the write buffer, each introduced as a local fix and here revealed as one tool.
   - [[Sensors and Control Systems]] — feedback as the canonical *deliberate* coupling: output wired to input because the coupling is the mechanism.
   - [[Space Travel]] — the constraint (8K words, no budget, no mandate) that shaped Unix into small programs, and so into the philosophy that needed pipes.

- **Children:**
   - [[Program Design]] — modular decomposition is the knowledge-axis decoupling applied to code; the interface is the tool.
   - [[The True IO Bound]] — the sibling thesis: the slow step is almost never compute but moving data, which is why the timing axis dominates the decoupler kit.

- **Worked instances in the vault:** [[Clock Domains and Metastability]] (the synchronizer and the async FIFO — decoupling at the physical limit, with a non-zero failure probability accepted as the price); [[RAM and the Memory Hierarchy]] (every cache level a timing decoupler); [[Interrupt Handling]] (the doorbell as the alternative to polling); [[Operating Systems]] (the process boundary as failure-axis decoupling; the kernel-design callout as the microkernel/monolithic version of the same choice); [[Dual-Core Craft]] (lockstep — the coupling kept, and its two verdicts); [[Object-Oriented Programming]] (encapsulation as knowledge-axis decoupling; ECS as the object itself decoupled into components); [[Error Detection and Correction]] (the message decoupled from the channel's failures); [[From the Grid to the Garage]] (the drivetrain coupling kept for racing and softened for the road; the laptop cell recoupled into a car); [[Linear Motion under a Variable Force]] (the rocket equation that forces staging); [[Electromagnetic Induction]] (the transformer wound for matched power or for isolation); [[Two Family Trees]] (Mach's microkernel *recoupled* to a BSD kernel inside XNU — a graft, in the story's own image). [[Relational Databases]] (normalisation as decoupling on the knowledge axis, one normal form per cut; the join as recoupling at read time; the NoSQL document as recoupling at write time — the same axis, the opposite decision).

- **Sibling Meta cards:** [[Fun Is the Brachistochrone]] (the detour that is the fastest path — the parts bin is a detour of the same kind); [[Inertia and Bootstrapping]] (the cost of starting, which the buffer's knee curve resembles); [[Credit Is the Currency]] (an interface is a promise — what a module says it will do, kept regardless of how).

- **Misconception traps cleared:** decoupling is always good; a buffer adds speed; coupling and dependency are the same thing; recoupling is copying; constraints oppose invention.

## Sources

- Chris Anderson, "How I Accidentally Kickstarted the Domestic Drone Boom", *Wired*, June 2012, and *Makers* (2012) — the "peace dividend of the smartphone wars" phrase and the parts list behind it.
- DJI founding (2006, HKUST dormitory) and the Phantom launch (January 2013): DJI's own history and contemporary reporting (*South China Morning Post*; *Forbes*, 2015).
- The palette-swapped bush and cloud: the *Super Mario Bros.* development team's own account (Nintendo's 25th-anniversary developer interview, 2010), citing the 256-tile limit.
- McIlroy's memo of 11 October 1964 and Thompson's January 1973 implementation: the Unix Heritage Society's pipes history and Dennis Ritchie's *The Evolution of the Unix Time-sharing System* (1984).
- *Ideal-X*, 26 April 1956, 58 containers, \$5.83 vs \$0.16 per ton: Marc Levinson, *The Box* (2006).
- K. E. Tsiolkovsky, *Cosmic Rocket Trains* (1929) — rocket staging.
- The maximum-power-transfer theorem: Moritz von Jacobi (1840); any A-Level or first-year circuits text.
- The simulation: `decouple-and-recouple-buffer.py`, beside this card.

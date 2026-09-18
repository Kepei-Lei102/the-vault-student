---
chinese: 格蕾丝·霍珀与一纳秒 (Géléisī Huòpò yǔ yī nàmiǎo)
aliases:
  - Grace Hopper
prerequisites: []
leads_to: []
teach_together:
  - "[[Compilers and Interpreters]]"
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - cast/hopper
  - cast/sammet
  - region/usa
---

# Grace Hopper and the Nanosecond 格蕾丝·霍珀与一纳秒

> *A computer can do the arithmetic. Must a human also do all the tedious work of telling it how?*

## Cast of Characters

- **Grace Murray Hopper (1906–1992)** — mathematician, programmer, Navy officer and a teacher with unusually portable teaching aids.
- **Howard Aiken (1900–1973)** — the Harvard Mark I project's leader; Hopper enters computing through his wartime laboratory.
- **Jean Sammet (1928–2017)** — a COBOL designer whose recollections keep a famous woman's story from swallowing everyone else's.
- **The users** — people trying to calculate pay, process records and get an answer without first becoming experts in a particular machine.

## 中文锚点

写一个算工资的程序时，我们通常只想说明工时、时薪和加班规则，不想亲手安排处理器的每一步动作。格蕾丝·霍珀推动的变化，就是把这些重复、琐碎的翻译工作交给计算机，让人能用更贴近任务的语言写程序。但这不等于机器能听懂随口说的话：语言仍然要有明确的规则，含糊的需求仍然要由人想清楚。她讲课时还会拿出一小段电线，表示光在真空中一纳秒走过的距离，约三十厘米。一个抽象得难以想象的时间，就这样变成了手里拿得住的长度。从编程语言到这段电线，她一直在做相似的事：让人看清复杂机器究竟在做什么，以及哪些麻烦可以交给机器，哪些判断还得自己做。

## Prologue — A small piece of time

Imagine a technical lecture whose most memorable prop fits in a shirt pocket.

It is a short piece of wire. The speaker calls it a nanosecond.

A nanosecond is a time, of course, and wire is a length. That mismatch is the trick: **give the invisible quantity a visible consequence**. You cannot hold a billionth of a second. You can hold the distance light travels during it.

In her recorded 1982 NSA lecture, Hopper recounts asking the engineers: **“Please cut off a nanosecond and send it over to me.”** She brings the resulting demonstration to her audience: roughly 11.8 inches of wire, followed by a much less convenient microsecond, roughly 984 feet. She explicitly says the short wire represents the limiting distance in space, not the actual speed through wire. [Hopper's lecture, Part One, pp. 16–17](https://media.defense.gov/2024/Nov/25/2003593626/-1/-1/0/PART%20ONE%20FUTURE%20POSSIBILITIES%20GRACE%20HOPPER%20TRANSCRIPT%20NO%20SUCH%20PODCAST%20NSA.PDF)

The joke is good. The teaching is better.

![[hopper-nanosecond-comic.png|850]]

*An imagined editorial reconstruction of Hopper's teaching demonstration, not a photograph of a particular lecture. The wire stands for light-travel distance in vacuum. The mountain of wire exaggerates the inconvenience, not the ratio: a microsecond really is 1,000 nanoseconds.*

How does someone arrive at the idea of handing an audience pieces of time?

## Act I — Before the computer, the clock

The childhood story is irresistible: young Grace takes apart alarm clocks to find out how they work, and the investigation spreads to several clocks. Vassar retells it as seven. It is a biographical anecdote, not a surviving laboratory notebook; the exact tally matters less than the kind of curiosity it describes. Finding out how a mechanism works can temporarily make the mechanism stop working. [Vassar: her life](https://www.vassar.edu/grace-hopper/life)

A clock is a small, domestic rebuke to the idea that a mysterious machine should remain mysterious.

Hopper graduated from Vassar in 1928, earned her mathematics doctorate at Yale in 1934, and taught mathematics at Vassar. When computing entered her life, she was already an experienced mathematician and teacher. The teacher was not a charming accessory added to the programmer later. [Computer History Museum: Hopper](https://computerhistory.org/profile/grace-murray-hopper/)

That changes how to read the rest of the story. A teacher notices where the learner is forced to carry unnecessary difficulty. A programmer notices work that can be automated. Put those habits together and a question starts to become unavoidable:

*Why are we making people repeat work that the machine could do?*

## Act II — Into the machine room

Hopper joined the US Navy Reserve during the Second World War and became one of the programmers working on Harvard's Mark I. This was computing in military service, not a hobby project that happened to receive a uniform. The Navy's account places her subsequent career across the Mark machines, UNIVAC and the development of standardized programming languages. [US Navy biography](https://www.navy.mil/DesktopModules/ArticleCS/Print.aspx?Article=2958917&ModuleId=2652&PortalId=1)

The Mark I was electromechanical: machinery and electrical switching executing an ordered calculation. Hopper helped make it usable, including work on its manual. A machine's existence did not automatically supply the knowledge needed to program it. Somebody had to turn individual expertise into instructions another person could follow. [Vassar: Mark I and its manual](https://www.vassar.edu/grace-hopper/achievements)

That is a less cinematic achievement than inventing a machine and a more revealing one than it first appears.

An undocumented clever trick belongs to the person who knows it. A documented method can become somebody else's starting point. The difference is how a field grows beyond its first roomful of people.

### The moth deserves its own footnote

In 1947, engineers working on the **Mark II**, not the Mark I, found a moth in a component and taped it into a logbook. The Smithsonian preserves the object. Its caption reads **“first actual case of bug being found.”** The museum cautions that the book was probably not Hopper's; she and the team helped popularize the story. [Smithsonian: the actual logbook](https://americanhistory.si.edu/collections/object/nmah_334663)

Notice *actual*. The joke depends on *bug* already meaning a fault. A literal insect has wandered into an existing metaphor.

Hopper did not need to invent the word, personally catch the moth and single-handedly repair the machine to deserve a biography. Those additions make a neat anecdote and a worse history.

## Act III — Make the computer fetch its own tools

After Harvard, Hopper joined the company building UNIVAC. In 1952 her **A-0** system assembled programs from stored routines identified by call numbers. Rather than manually reproduce the machinery for each operation, the programmer could identify reusable pieces and let the system retrieve and combine them. [Centre for Computing History: A-0](https://www.computinghistory.org.uk/det/5487/Grace-Hopper-completes-the-A-0-compiler/)

Think of the difference between recopying an entire recipe and writing down which prepared recipes you need, with their ingredients supplied.

The human still chooses the work. The machine takes over part of the clerical assembly.

> [!info] What “compiler” meant here
> A-0 belongs to the history of compilation, but its routine-retrieval and assembly job is closer to what we would now call **linking/loading** than to translating an entire modern high-level language. Calling it an early compiler is historically appropriate; imagining it as a 1952 Python translator is not. [[Compilers and Interpreters]] explains modern translation.

The deeper move is easy to miss because we now take it for granted: **a program can help construct another program**. Machine instructions are represented as data. Another program can select, relocate or generate them without possessing human understanding of the final task.

This does not require a machine that thinks. It requires a repeatable transformation.

Hopper later described having to persuade people to try a working compiler. Building the tool and persuading an organization to trust it were separate jobs. [A-0 and its reception](https://www.computinghistory.org.uk/det/5487/Grace-Hopper-completes-the-A-0-compiler/)

There is an awkward little human problem here. If difficult handwork is part of your professional identity, a tool that removes it can look like an insult before it looks like assistance.

## Act IV — The payroll does not care about your instruction set

Scientific calculations were only part of what organizations wanted computers to do. Businesses had records, invoices and payrolls. The language of a payroll office was not the language of a processor.

Hopper's group developed **FLOW-MATIC**, an English-like language for business data processing. Its vocabulary moved the description towards the user's work. This was a step beyond calling stored routines by number: operations on business information could be expressed in recognizable words. [Computer History Museum: software timeline, FLOW-MATIC](https://www.computerhistory.org/timeline/software-languages/)

An important distinction: **English-like is not unrestricted English**. A programming language gives selected words exact meanings and permits selected arrangements. An ordinary sentence can leave its listener to infer what “the usual overtime” means. A payroll program needs the rule.

Try the problem in miniature. An employee worked 45 hours at £12 per hour. The first 40 hours get the ordinary rate; additional hours get one-and-a-half times that rate. The total is:

$$40\times12+5\times18=570.$$

That is an original illustration of the kind of business rule at stake, not a reconstructed FLOW-MATIC program. Notice what the translator can spare you: processor instructions, register choices, addresses. Notice what it cannot spare you: deciding whether the threshold is 40, whether the multiplier is 1.5, and which hours qualify.

The abstraction removes one kind of work so the relevant work becomes easier to see.

### A language needs more than one champion

In 1959, a committee of people from manufacturers and government set out to create **COBOL**, the Common Business-Oriented Language. Readability and machine independence were central aims. Hardware could differ while a shared language reduced the need to start the software again. [CHM: the committee forms](https://www.computerhistory.org/tdih/may/28/)

Hopper's influence was substantial. It was also not sole authorship.

Jean Sammet's oral history describes FLOW-MATIC as a major input and identifies her own work leading the statement-language group. Her account gives the design process actual people, groups and decisions. The Smithsonian's surviving early COBOL draft likewise locates the language in a series of committees and subcommittees. [Sammet interview](https://ethw.org/Oral-History:Jean_Sammet) · [Smithsonian: the draft](https://www.si.edu/object/first-draft-programming-language-cobol%3Anmah_1389377)

A biography should make its subject visible without making the collaborators disappear.

There is a wonderful physical counterpoint to the celebration: Howard Bromberg made a tombstone for COBOL because he feared it had no future. The Computer History Museum keeps that, too. Software history has both a dead moth and a premature grave marker. The artifacts have a better sense of humour than the heroic slogans. [CHM: COBOL's tombstone](https://www.computerhistory.org/tdih/may/28/)

## Act V — The teacher brings the hardware back

High-level languages let a programmer ignore many machine details. They do not repeal physics.

Return to the short wire. The calculation behind it is small enough to do without ceremony:

$$d=ct=(299{,}792{,}458\ \mathrm{m/s})(10^{-9}\ \mathrm{s})\approx0.300\ \mathrm m.$$

A microsecond is $10^{-6}$ seconds, so the corresponding distance is about **300 metres**. A thousand times the time means a thousand times the length. This is a physical upper limit for signal travel in vacuum; real interconnects introduce slower propagation and other delays. It is not the drift speed of electrons in copper.

Hopper's demonstration makes a limitation tangible. You cannot demand that two distant components exchange information instantly just because the software command is short. Sometimes the architecture must change.

In the lecture she also tells an airport story: carrying the wires in her shoulder bag cost her twenty minutes of explanation. It is a marvellous reversal. The prop that makes a nanosecond easy to explain makes boarding a plane considerably slower. [Hopper's lecture, Part One, p. 17](https://media.defense.gov/2024/Nov/25/2003593626/-1/-1/0/PART%20ONE%20FUTURE%20POSSIBILITIES%20GRACE%20HOPPER%20TRANSCRIPT%20NO%20SUCH%20PODCAST%20NSA.PDF)

She finally retired from the Navy in 1986, aged 79, after an earlier retirement and recall. She continued working as a consultant before her death in 1992. The story ends with neither the child dismantling the clock nor the celebrated inventor standing beside a machine, but with someone still trying to make difficult things usable by other people. [Navy: retirement](https://www.navy.mil/DesktopModules/ArticleCS/Print.aspx?Article=2958917&ModuleId=2652&PortalId=1) · [CHM: later career](https://computerhistory.org/profile/grace-murray-hopper/)

## Cultural ripples — The next person can start higher

Write a spreadsheet formula. Run a Python program. Change a business rule without manually selecting a processor register.

These are not all Hopper inventions, nor branches of a single family tree. They share the bargain her work helped establish: **people should describe the task at a useful level, and software should perform the mechanical translation**.

The bargain has limits. A compiler can faithfully implement the wrong payroll rule. A readable program can still be wrong. A fast processor still waits for a signal. Removing unnecessary difficulty is not the same as removing the need to think.

Hopper's two most instructive objects point in opposite directions. The compiler lifts your attention away from the machine's details. The piece of wire brings it back to a physical constraint when that constraint matters.

Good explanation knows which direction the learner needs.

The child who wanted to see inside the clock did not grow up to demand that everyone dismantle every clock. She helped build a world in which more people could use the machinery—and know when they needed to look inside.

## Connections

- **Technical companion:** [[Compilers and Interpreters]] — modern translation stages and execution; a historical use of “compiler” need not match the present-day boundaries exactly.
- **Another language history:** [[A, B, C]] — the trade between language design, implementation and the work people need to do.
- **Physical companion:** [[Electric Current]] — signal propagation and electron drift are different things.
- **A modern echo:** [[You're the Architect, the AI is the Bricklayer]] — handing off implementation still leaves someone responsible for deciding and checking what should happen.

## Receipts and historical boundaries

- **Primary testimony:** Hopper's [1982 lecture transcript](https://media.defense.gov/2024/Nov/25/2003593626/-1/-1/0/PART%20ONE%20FUTURE%20POSSIBILITIES%20GRACE%20HOPPER%20TRANSCRIPT%20NO%20SUCH%20PODCAST%20NSA.PDF), especially pp. 16–17. The [NSA release page](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3884041/nsa-releases-copy-of-internal-lecture-delivered-by-computing-giant-rear-adm-gra/) links the recorded lecture. Her recollections establish what she told the audience; humorous scientific flourishes elsewhere in the talk should not be treated as physics definitions.
- **Another participant's account:** [Jean Sammet's oral history](https://ethw.org/Oral-History:Jean_Sammet), particularly the COBOL development discussion. A corrective to single-inventor retellings.
- **Surviving objects:** the Smithsonian [moth logbook](https://americanhistory.si.edu/collections/object/nmah_334663) and [early COBOL draft](https://www.si.edu/object/first-draft-programming-language-cobol%3Anmah_1389377).
- **Institutional histories:** [Vassar's biography](https://www.vassar.edu/grace-hopper/life), [CHM's profile](https://computerhistory.org/profile/grace-murray-hopper/), and the [Navy biography](https://www.navy.mil/DesktopModules/ArticleCS/Print.aspx?Article=2958917&ModuleId=2652&PortalId=1). The childhood clock count is presented as anecdote; some institutional summaries simplify compiler priority or contain age/date errors, so slogans are not used as precise technical definitions.
- **A-0's mechanism:** [Centre for Computing History](https://www.computinghistory.org.uk/det/5487/Grace-Hopper-completes-the-A-0-compiler/). The distinction from a modern compiler matters more than an unqualified claim to be “first.”
- **Illustration:** newly generated editorial comic; staged scene and expressions are imaginative, not evidence of an event.

---
chinese: 需求的变化，总在意料之外 (xūqiú de biànhuà, zǒng zài yìliào zhī wài)
prerequisites:
  - "[[Courage]]"
leads_to: []
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - era/21c
  - cast/gates
  - region/usa
---

# You Never Expect the Change of Needs 需求的变化，总在意料之外

> *"There's never a citation; the quotation just floats like a rumor, repeated again and again." — Bill Gates, 1996, about the most famous sentence he never said.*

## Cast of Characters

- **Bill Gates** (b. 1955) — Microsoft's co-founder, haunted for forty years by a quote with no source, no date, and no intention of dying.
- **IBM's 1981 memory-map engineers** — drew a sensible line across a million addresses and accidentally built the most famous wall in computing.
- **The Unix second-counter** — born January 1, 1970, counting seconds in a 32-bit signed integer; its odometer rolls over on a date already printed in this card.
- **AMD's Opteron team** — sold the world a bigger address space and quietly slipped something better into the box.
- **The speedrunners** — the closing chorus: the people who measure change in frames, because their craft dies by the millisecond.

## 中文锚点

比尔·盖茨最有名的一句话，是他从来没说过的："640K 内存对谁都够用了。"他本人否认得很干脆——"蠢话我说过，错话也说过，但这句不是我说的"——可这句话没有出处、没有日期，四十年来像谣言一样越传越真，连措辞都在民间自行进化。这张卡片收藏的是它背后的规律：**计算机史上每一道"足够大"的天花板，都死于需求的变化**——640K 死于图形界面，32 位的 4 GB 死于内存越来越便宜，两位数年份死于世纪之交（千年虫），32 位秒计数器将死于 2038 年 1 月 19 日（一个写在日历上的溢出），43 亿个 IPv4 地址死于每人口袋里都有一台计算机。没有一道墙是蠢人砌的：当年都是慷慨的工程判断，错的只是"需求不会变"这个没人明说的假设。而故事的另一面同样出乎意料：**变化的后果也没人料得到**。64 位当年的卖点是打破 4 GB 内存墙，顺手写进规格里的却是**寄存器翻倍**（8 个变 16 个）——编译出的程序少往内存跑，帧时间更短也更稳——十几年后，这份没人宣传的赠品让《空洞骑士》的速通玩家在 64 位更新后齐声说"手感更顺了"。需求的变化料不到，变化的红利同样料不到：预测在两个方向上都会失败，这正是工程师要么把天花板修得高到荒谬（有符号 64 位秒计数器可以数近三千亿年），要么干脆给承诺预定葬礼（[[Courage|勇气]]）的原因。

## The Story

### Act I — The exhibit that curates itself

Every museum in [[The Ghost of Drive A]] holds things that refuse to die. This card's first exhibit is stranger: a *sentence* that refuses to die, in a display case it built for itself.

"640K ought to be enough for anybody." Attributed to Bill Gates everywhere, sourced nowhere. The earliest known sighting is an April 1985 InfoWorld editorial crediting Gates with believing nobody would ever need 640K — already with no citation attached. From there the quote evolved in the wild like a folk song: sometimes 64K, sometimes 640K; sometimes "for anybody," sometimes "for anyone"; the date drifting anywhere from 1981 onward. Gates has denied it with unusual precision. In January 1996: **"I've said some stupid things and some wrong things, but not that. No one involved in computers would ever say that a certain amount of memory is enough for all time."** And, weeks later, the sentence this card takes as its epigraph — there's never a citation; it just floats like a rumor. Notice what the quote has become: a misattribution so useful that no correction can kill it — the icon promoted to original, exactly the backwards causality the Ghost's museum documented in its save-button aisle.

![[change-of-needs-plaque.png|697]]

So where did the actual wall come from? Not from a prophecy — from a **memory map**. The 1981 IBM PC's processor had twenty address pins: $2^{20}$ addresses, exactly one megabyte of reachable memory. IBM's engineers split that megabyte: the bottom 640K for programs, the top 384K reserved for the video card, the BIOS ROM, and expansion hardware. On a machine that typically shipped with 64K, reserving *ten times the typical fit-out* for programs was not stinginess — it was generosity, drawn as a line on an address map. Nobody said "enough forever." They designed for the need in front of them.

Then the need changed — graphical interfaces, spreadsheets that outgrew the room — and the line on the map became the most hated wall in computing. A whole decade of DOS contortions followed: **expanded memory** shuffling data through a window in the reserved zone like a warehouse passing crates through a mail slot, extended-memory drivers, and boot-time black magic to claw back kilobytes. The wall's ghosts run deep enough that they appear one museum over: the A20 gate in [[The Ghost of Drive A]] is this same map, fossilised into boot silicon.

### Act II — The museum of dead ceilings

Once you see the shape, computing's history reorganises itself into a gallery of generous ceilings that died. Walk it in order:

**The two-digit year.** Storing "74" instead of "1974" was rational rent-saving when memory was priced per byte and punched cards held eighty columns — the same money-shaped constraints as the Ghost's dollar-bill-sized card. Decades later the world paid a repair bill in the hundreds of billions to add two digits back. **Y2K** was not a bug; it was a lease expiring.

**The 4 GB wall.** A 32-bit pointer reaches $2^{32}$ bytes — four gigabytes. In 1985 that was a fantasy of excess; by the mid-2000s, a mid-range desktop bumped its head on it. The industry crawled through PAE — a bank-switching crawlspace with a strong family resemblance to DOS's expanded memory, because the contortion is always the same contortion — until the real exit opened.

**The second-counter with a printed expiry date.** Unix counts time as seconds since January 1, 1970, and for decades stored the count in a **signed 32-bit integer**. [[Two's Complement]] tells you the rest: the largest value is $2^{31}-1 = 2{,}147{,}483{,}647$, and the counter reaches it at **03:14:07 UTC on 19 January 2038** — one tick later, the sign bit flips and the date wraps to December 1901. Desktop systems have largely moved to 64-bit time; the long tail of embedded systems — meters, controllers, the computers nobody remembers are computers — is where the 2038 work actually lives. This is the museum's most honest exhibit: **a change of needs with a countdown clock**, overflow mechanics you can verify on paper.

![[change-of-needs-odometer.png|697]]

**The four billion addresses.** IPv4 gave the internet 32-bit addresses — about 4.3 billion, an address for every computer imaginable in 1981. Then computers became phones, then thermostats. The top-level pool ran dry in February 2011; NAT was the tourniquet (whole households hiding behind one address), and IPv6's 128 bits the exit — sized not for the predicted need but for absurdity, $2^{128}$ addresses, because that generation of engineers had finally internalised the lesson.

Name the pattern before moving on, because it is the card's first half: **none of these walls was built by a fool.** Every ceiling was a correct engineering judgment about the need in front of it, wrong only about the one variable nobody writes down — that the need itself would change. The quote in Act I survives *because* it compresses this pattern into one sentence; it is too good a story to be true, and too true a pattern to die.

### Act III — The other direction

Here the card turns around, because prediction fails both ways: **you never expect the change of needs — and you never expect the consequences of change.**

When AMD designed the 64-bit extension of x86 (announced as sketches in 1999, shipped as Opteron and Athlon 64 in 2003), the sales pitch was the obvious one: break the 4 GB wall. Address space was the headline, the benchmark slide, the reason enterprises signed. But tucked into the same architecture revision was a change almost nobody outside compiler teams got excited about: **the register file doubled.** x86 had lived since 1978 with eight general-purpose registers — several of them with historical day jobs — and [[CISC vs RISC]] tells you what a poverty that was next to RISC's thirty-two. AMD64 made it sixteen general-purpose and sixteen vector registers, taught the calling convention to pass arguments *in registers* instead of on the stack, and gave position-independent code a native addressing mode.

Why that matters is one level of the [[RAM and the Memory Hierarchy]] pyramid: registers are the tier with *zero* latency — the values the CPU's hands are already holding — while even the L1 cache costs cycles and a RAM trip costs hundreds. A compiler with eight registers is a cook with a tiny counter, forever putting ingredients back in the pantry mid-recipe; those round trips are called **spills**. Double the counter space and the same recipe compiles into code that simply *goes to memory less*. The practical effect, measured everywhere in the years after 2003: recompile the identical program for 64-bit and it typically runs meaningfully faster — not because anyone's data outgrew 4 GB, but because of the register gift nobody advertised. (ARM, designing its own 64-bit leap, took the lesson on purpose: AArch64 carries thirty-one general-purpose registers.)

Hold the symmetry up to the light. The 640K wall was *address space* mispredicted in one direction — the need outgrew the ceiling. The 64-bit transition is the same axis mispredicted in the other — the change shipped for address space, and its most *felt* consequence turned out to be something else entirely. Who would have guessed, signing off on a server-market spec sheet in 1999, that the register file would one day be the line item **gamers could feel in their hands?**

### Act IV — The chorus with stopwatches

Which brings in the witnesses best qualified to testify, because their craft is measured in frames: speedrunners.

Hollow Knight shipped in 2017 as a 32-bit Windows build. In June 2021, its v1.5 update moved the game to a new engine version and a **64-bit** build — and Steam, in a gift to experimental method, still carries the old build as an official "1.4.3.2 — 32-bit compatibility" branch. The before and the after are both installable, today, side by side. The community that plays this game at the frame level reports the change in its own language: the new build "just runs better — smoother."

That word "smoother" deserves the unpacking, because it decomposes into two different claims — and the split *is* [[Averages and Spread]]'s oldest lesson wearing a controller. Either the **average** input-to-screen delay dropped by a margin big enough for a trained human to notice — a couple of frames, the ~25 ms scale, which sits right at the edge of what even elite players resolve — or the **variance** dropped: the delay became consistent. And the second claim is the deeper one, because of an asymmetry every musician and every athlete knows: **a constant delay can be calibrated away; jitter cannot.** Muscle memory happily learns "press 40 ms early," to arbitrary precision — that is how the most precise runners hit single-frame windows through a fixed pipeline. No amount of practice can learn "press somewhere inside a ±25 ms cloud." Frame-perfect tricks live and die on variance, which is why runners obsess over wired controllers and display modes: all of it is variance-hunting. When a community whose whole craft is thousands of attempts against frame windows says *smoother*, that is a low-variance verdict from the population best equipped to deliver one.

And both readings are downstream of the same mechanism. Fewer spills and better code generation shorten frame times — but they especially shorten the *worst* frames, the spikes, so the same change drops the mean and tightens the spread at once. (Honesty requires the footnote: the 2021 update also reworked the input system and the engine's frame pipeline, and those share the credit — the register gift is one contributor, not a lone hero.) The experiment is sitting on Steam for anyone with a 240 fps phone camera: install both branches, press the same button, count the frames to the same animation, and do it enough times to see not just the average but the spread. Two numbers, one lesson, and the card's thesis measured rather than recited.

## Cultural ripples

The gallery's lesson is not "predict better." It is that **prediction fails in both directions, so stop leaning on it.** Computing's mature answers all take that shape. Size the ceiling for absurdity, not for the forecast: IPv6's 128 bits; 64-bit time, whose signed second-counter runs for roughly 292 billion years — the engineers stopped estimating need and priced out the universe instead. Or design the promise to keep itself, UTF-8's move in [[The Ghost of Drive A]]. Or — the discipline [[Courage]] documents — schedule the funeral in advance, so the ceiling dies on a date you chose rather than one that ambushes you; Catalina's execution of 32-bit software was this story's enforcement arm wearing a release calendar.

The reverse direction has its ripples too, and the largest one alive deserves its own telling. A GPU was built for exactly one need: shade millions of triangles at once — thousands of small, identical, independent computations per frame. In the early 2000s researchers noticed that this is also the *shape of linear algebra*, and the *GPGPU* era began as smuggling: matrices disguised as textures, "rendered" through pixel shaders, the answer read back off the fake picture. NVIDIA legitimised the trick with CUDA (2007) — programming the graphics card with no graphics in sight — pitched mostly at physics simulation. Then 2012: **AlexNet**, a neural network trained on **two consumer gaming cards**, crushed the ImageNet vision competition and lit the deep-learning era — because the matrix multiplications at a network's heart are precisely the many-small-identical-jobs shape that triangle-shading hardware had spent two decades perfecting. Follow the consequence chain nobody priced: a company selling *gaming parts* became the most valuable company on Earth, its chips the strategic commodity of a decade, because the need its hardware was built for was not the need history had in mind. The register windfall is this same family in miniature. A capability, once shipped, does not stay filed under the need that justified it. That is the optimistic half of the card: the change you budget for is rarely the change you get, and sometimes the surprise is a gift.

And the quote? Still floating, still uncited, still "enough for anybody." It survives because it is the pattern's perfect compression — a fossilised prediction-failure attributed to the one man whose actual words on the subject were that no one in computing would ever make it. Both halves of that sentence are the story.

## Where this surfaces in the vault

- [[Courage]] — the companion policy: this card is why the funerals exist; Catalina's 32-bit cutoff is the change of needs enforced on a schedule.
- [[The Ghost of Drive A]] — the ceilings that never got funerals: the A20 gate is Act I's memory map fossilised, and the unkillable quote is the save-button reversal happening to a sentence.
- [[CISC vs RISC]] — the register poverty of eight and the RISC thirty-two; AMD64 as the CISC world quietly adopting the RISC register philosophy.
- [[CPU Architecture and the Fetch-Execute Cycle]] — what a register physically is: the values already in the datapath's hands.
- [[RAM and the Memory Hierarchy]] — the pyramid whose zero-latency tip this story's windfall enlarges; spills as forced trips down the pyramid.
- [[Two's Complement]] — the 2038 exhibit's mechanics: signed overflow, the sign bit's flip, and why the wrap lands in 1901.
- [[Averages and Spread]] — mean versus variance, the distinction "smoother" hides and Act IV teaches.

## Receipts

- Quote history: Quote Investigator, "Computer Memory: 640K Ought to be Enough for Anyone" (earliest attribution InfoWorld, 29 April 1985, uncited; textual variants catalogued); Computerworld, "The '640K' quote won't go away — but did Gates really say it?"
- Gates's denials, January 1996, syndicated column: "I've said some stupid things and some wrong things, but not that. No one involved in computers would ever say that a certain amount of memory is enough for all time," and "There's never a citation; the quotation just floats like a rumor, repeated again and again."
- IBM PC memory map: 8088's 20-bit addressing (1 MB), 640K conventional / 384K reserved split; EMS/XMS workarounds — standard PC architecture references.
- x86-64: AMD's architecture announcement (1999–2000), Opteron (April 2003) and Athlon 64 (September 2003); 16 general-purpose + 16 XMM registers, register-based argument passing (System V ABI), RIP-relative addressing — AMD64 Architecture Programmer's Manual. AArch64's 31 general-purpose registers — Arm Architecture Reference Manual.
- Year 2038: signed 32-bit `time_t` maximum 2,147,483,647 seconds after the 1970 epoch → 03:14:07 UTC, 19 January 2038.
- IPv4 exhaustion: IANA's free pool of /8 blocks exhausted 3 February 2011; IPv6 128-bit addressing.
- Hollow Knight: engine and executable lineage (Unity 5.6/2017-era 32-bit → v1.5, June 2021, Unity 2020.2, 64-bit; second engine update February 2026) per PCGamingWiki and Team Cherry's patch notes; the "1.4.3.2 - 32-bit compatibility" branch on Steam; community patch guidance ("runs better/smoother") per the speedrun.com Hollow Knight guides.

---
chinese: 勇气 (yǒngqì) — 按日程表违约的公司
prerequisites:
  - "[[The Ghost of Drive A]]"
leads_to:
  - "[[You Never Expect the Change of Needs]]"
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - era/21c
  - cast/jobs
  - cast/schiller
  - cast/davidian
  - region/usa
  - region/europe
---

# Courage 勇气

> *"It really comes down to one word: courage." The hall laughed. The internet laughed for a decade. The jack died anyway — and so, on schedule, did everything else Apple ever promised to kill.*

## Cast of Characters

- **Steve Jobs** (1955–2011) — Apple's co-founder, who presided over one architecture funeral, announced a second from the stage, and never apologised for either.
- **Phil Schiller** (b. 1960) — Apple's marketing chief, who in 2016 said the word this card is named after, and in 2012 made a promise with its own expiry date hidden in the sentence.
- **Gary Davidian** (b. 1956) — the Apple engineer whose 68000 emulator, started in 1990, convinced the company that a computer could survive a heart transplant.
- **The European Union** — a regulator, appearing in the final act to demonstrate that even the serial promise-breaker has someone above it.

## 中文锚点

苹果是计算机世界里唯一一家把"违约"做成日程表的公司。[[The Ghost of Drive A|A 盘的幽灵]]讲过兼容性陷阱的两条出路：要么砸掉承诺硬付账（Python 3 付了十二年），要么把新东西设计得让旧承诺自动成立（UTF-8）。苹果走的是第三条：**给承诺定死期**——从不无桥而拆（68k 换 PowerPC 有 Davidian 的模拟器，PowerPC 换 Intel 有 Rosetta，Intel 换自研芯片有 Rosetta 2），也从不修一座不写明拆除日期的桥（Classic 死于 2007，Rosetta 死于 2011，32 位应用死于 2019——葬礼全部如期举行）。1998 年，一台 iMac 砍掉软驱、ADB 和串口，被嘲笑，然后被全行业照抄；2016 年砍掉耳机孔时，Schiller 说出了那个被笑了十年的词："归根结底就是一个词：勇气。"但这故事的两面都要看：每次转身都真的踩伤了人——Final Cut Pro X 一夜之间功能蒸发、Catalina 的游戏坟场、满桌转接头的岁月；而且拆惯了别人承诺的人自己也会被拆——2023 年，欧盟监管者让 Lightning 接口躺进了它给三十针接口挖过的同一种坟墓。最深的寓意是一笔账：**无限期的承诺永远在生利息；苹果选择按期偿还本金，并把每一次还款的骂声，开成一场发布会。**

## The Story

### Act I — One machine, four funerals

[[The Ghost of Drive A]] is a museum of promises nobody dared to break: the empty drive letters, the year 1900's phantom leap day, the boot sequence still impersonating a chip from 1978. This is the story of the one company that walks through that museum with a demolition schedule — and the place to start is May 1998, when Steve Jobs, freshly returned to a nearly bankrupt Apple, pulled the sheet off a translucent blue egg called the iMac.

The tech press inspected it and found what was *missing*. No floppy drive — in 1998, the floppy was how ordinary people carried their files, and every other computer on Earth had one. No ADB ports for the keyboards and mice Mac users already owned. No serial port for their printers and modems. In their place: two sockets of a barely-used new standard called USB. One machine, four funerals, no warning. The commentary wrote itself — *no floppy, it'll never sell* — and the iMac became the fastest-selling computer in Apple's history, USB accessories bloomed in translucent plastic to match it, and within a few years the floppy slot had quietly vanished from everyone else's machines too. The pattern that would repeat for twenty-five years is already complete in this one scene: **cut early, get mocked, get copied.**

![[courage-imac-no-floppy.png|697]]

The optical drive went the same way — the 2008 MacBook Air was unveiled by sliding it out of a manila envelope, and the price of that thinness was the DVD slot. Mocked, then copied: try to buy a laptop with a disc drive today.

### Act II — The heart transplant

Ports are cosmetic surgery. The organ Apple has replaced — **three times** — is the one no other company has dared touch even once: the CPU architecture itself. The x86 world catalogued in [[CISC vs RISC]] has performed *zero* such transplants; its processors still boot in the mode of 1978, A20 fossils and all, precisely because breaking the instruction set would break every program ever compiled for it. An architecture change doesn't strand your accessories. It strands **all software in existence**.

Apple's first transplant began, as these things often do, with one engineer working slightly ahead of the plan. In mid-1990, Gary Davidian started writing a **68000 emulator** — a program that reads compiled 68k machine code, the native tongue of every Macintosh since 1984, and performs it, instruction by instruction, on a completely different processor. His first target was Motorola's 88000 RISC chip; when Apple's alliance with IBM and Motorola switched the future to PowerPC, Davidian converted the emulator to that. The demo did the arguing: old Mac software, unmodified, running on silicon it had never heard of, fast enough to use. Management's conclusion — that emulation made a processor change *survivable* — is the load-bearing decision under everything else in this story. (Davidian told the whole tale to the Computer History Museum's oral-history programme in 2019; it is a fine afternoon of listening.)

So in March 1994 the Power Macintosh shipped with a PowerPC heart and Davidian's emulator built into the system, and the astonishing part was how little drama followed. Your 1987 spreadsheet just ran. Large stretches of the operating system *itself* ran through the emulator at first, translated on the fly while Apple rewrote it piece by piece underneath. The bridge held while the traffic crossed.

### Act III — The secret double life

The second transplant opens with a confession. June 6, 2005, on the WWDC stage, Jobs announced the move from PowerPC to Intel — the very architecture Apple's own ads had spent years ridiculing — and explained why it was safe to believe him: "Mac OS X has been leading a secret double life for the past five years." Every release of the operating system, he said, had been compiled for both PowerPC and Intel since 2000, inside a project the engineers had named **Marklar**. Five years of parallel builds, maintained in secret, as insurance on a promise nobody outside the building knew existed.

The bridge this time was named **Rosetta** — licensed from a Manchester company called Transitive, whose QuickTransit engine did dynamic binary translation: reading PowerPC machine code and rewriting it, block by block as it ran, into x86. ([[Compilers and Interpreters]] would file this under just-in-time translation; Apple filed it under "most users never noticed".) The first Intel Macs arrived in January 2006, the whole product line had crossed by the end of that year, and your old software walked over the bridge without being recompiled, mostly unaware the river below had changed.

### Act IV — The funerals are held on schedule

Here is where Apple's pattern separates from everyone else's. Anyone can build a compatibility bridge; the x86 world is *made* of compatibility bridges. What no one else does is what comes next: **Apple publishes the bridge's demolition date, and then actually demolishes it.**

The Classic environment — the bridge that let Mac OS 9 software run on OS X — was never even offered on the Intel Macs, and Leopard removed it for everyone in 2007. Rosetta became an optional install in 2009 and was gone entirely in Lion, 2011: five years of bridge, then rubble. At WWDC 2007 Apple cancelled the promised 64-bit version of Carbon, the API bridging the pre-OS-X world — famously blindsiding Adobe, which had to rewrite Photoshop's foundations in Cocoa and took until 2010 to ship it. And in 2019, macOS Catalina executed the 32-bit application, full stop: decades of software, including a large fraction of every Mac gamer's Steam library, stopped launching on upgrade day.

State it as the policy it visibly is: **never break without a bridge; never build a bridge without a funeral date.** The first clause is mercy. The second is the discipline that makes the mercy affordable — a bridge with no demolition date is just the compatibility trap again, wearing a hard hat. Windows still ships machinery to run software from the Reagan administration, pays the complexity tax on every machine, every year, forever. Apple pays a scheduled lump sum of outrage instead, and is done paying.

### Act V — Courage

September 7, 2016. The iPhone 7 has no headphone jack — a connector whose ancestry runs back through the transistor radios of the 1960s to the quarter-inch plugs of nineteenth-century telephone switchboards; kin, in other words, to the fossils in the Ghost's museum, and about to be treated very differently. On stage, Phil Schiller explains: "It really comes down to one word: courage. The courage to move on, do something new, that betters all of us."

The word became a punchline within the hour. It was mocked in reviews, in memes, in rival companies' keynotes — and those same rivals removed their own headphone jacks within two years, which is the "mocked, then copied" clause executing right on time. The mockery was also not entirely wrong, which is Act VII's business.

![[courage-headphone-funeral.png|697]]

"Courage" was also underselling the actual argument, in two directions at once. The same keynote that buried the jack introduced **AirPods** — the funeral and the successor in the same hour — and true wireless earbuds genuinely retired the jack's oldest misery: the cable that ties itself into a knot in your pocket. That knot was physics, not carelessness — tumble a string in a box and it knots itself within seconds, and the longer and more flexible the cord, the faster it happens; earbud cables sat squarely in the danger zone. The cable was always going to lose. Meanwhile, in the other direction, the same company quietly did the *opposite* to the same connector: the 2021 MacBook Pros **upgraded** their headphone jack, sensing the connected headphones' **impedance** — resistance's frequency-aware generalisation, the measure that decides how hard an amplifier must push — and switching to a higher-voltage drive for the high-impedance studio kind, 80 to 600 ohms, headphones a phone jack could never drive properly. Read the two moves together and the policy sharpens: this is not a company that hates the connector. It buries a port where the mainstream's need has genuinely moved on, and polishes the *same port* in the machines where professionals still plug in — segmentation wearing courage's clothes.

But the sharpest joke in the connector saga is one Schiller had told on himself four years earlier. Introducing Lightning in 2012 — a change that obsoleted a decade of 30-pin docks, speakers and car mounts overnight — he called it "a modern connector for the next decade." Listen to that sentence with this card's ears: it is a compatibility promise **with the funeral date embedded in the grammar**. No other company talks about connectors this way. And the promise was kept almost to the month: Lightning lasted eleven years.

Its death, though, belongs to the final twist: Apple did not schedule this funeral. The **European Union** did, mandating USB-C charging ports in 2022; the iPhone 15 complied in September 2023. The company that spent twenty-five years breaking promises to its own ecosystem had a promise broken *for* it, by a regulator — the breaker, for once, on the receiving end of the shovel.

### Act VI — The third transplant

By then the third heart transplant was already done. June 2020: Jobs's successors announced the Mac would leave Intel for Apple's own chips, and the echo of 2005 was deliberate — down to the confession that macOS had, again, been living a double life on ARM for years. **Rosetta 2** carried the traffic, and it is quietly the most technically interesting bridge of the three: instead of translating instructions as they run, it translates the *entire program once, at installation* — ahead-of-time binary translation, with a just-in-time path held in reserve for code that generates itself on the fly. An x86 program on an M1 was, by first launch, already speaking ARM — which is why the third transplant is the one nobody's users tell war stories about. The whole product line crossed in about two years; the funeral (this bridge's own scheduled demolition) is, at this telling, only a matter of the calendar.

Three architectures — 68k, PowerPC, Intel — each carried across on a bridge, each bridge later torn down on schedule. The x86 count remains zero. That asymmetry is the whole thesis wearing silicon.

### Act VII — What breaking actually costs

An honest telling has to sit for a while with the people on the bridge when it fell. The dongle years were real: the 2016 MacBook Pro went all-USB-C, and a generation of professionals carried a pouch of adapters to plug their Apple phone into their Apple laptop. The Catalina massacre was real: working software — bought, paid for, loved — dead on upgrade day, no bridge offered at all this time. And the deepest wound was self-inflicted on the customers least able to shrug: **Final Cut Pro X, June 2011**. Apple replaced its professional video editor with a rebuilt one and simply shipped it before the replacement could do the job — no importing of old projects, no tape output, no EDL or XML export, the working vocabulary of an entire industry, gone overnight. Working editors mid-production found the tool their business stood on discontinued in place. The ridicule reached late-night television, and Apple did something almost unheard of for it: apologised in the only currency it deals — **refunds** — and spent years patching the features back in while a real exodus decamped to its competitors. Even for the serial promise-breaker, breaking is not free; trust, once, took most of a decade to rebuild.

That is the cost side of the ledger. The story's economics only balance because the pattern's *benefit* side compounds: every dead port, dead API and dead architecture is complexity the next machine doesn't carry — no A20 gates, no boot-time impersonation of 1978, no forty-year-old code paths to test forever.

## Cultural ripples

Why can Apple do what Microsoft and Intel — richer, older, cleverer than the 1998 Apple — demonstrably cannot? Three structural answers, none of them "courage."

**It owns the whole stack.** Silicon, firmware, operating system, flagship applications, retail store: when Apple breaks a promise, every layer moves in the same keynote, because every layer reports to the same building. Microsoft breaks a promise and ten thousand other companies' products fall over; the ecosystem's inertia — [[Inertia and Bootstrapping]]'s guardian face — vetoes the break.

**Its customers replace devices, not deployments.** A consumer grieves a dead accessory and buys a dongle. An enterprise running a thirty-year-old payroll system on Windows does not buy a dongle; it buys a lawyer or it stays put, forever. Backward compatibility is Windows's *product*. Its absence, on schedule, is Apple's.

And there is a mirror image that explains a reputational puzzle: **Microsoft almost never breaks your software — and catches more grief, because what it breaks is its word.** Twice, famously. The "Windows Vista Capable" sticker program (2006) put a promise on the shelf tag of machines that could barely run the real thing, and ended in a class action. And at Ignite 2015 a Microsoft developer evangelist, Jerry Nixon, said in passing: "Right now we're releasing Windows 10, and because Windows 10 is the last version of Windows, we're all still working on Windows 10." A throwaway segue — but Microsoft never denied it, the press hardened "the last Windows" into a promise, and six years later Windows 11 arrived behind a TPM-and-CPU wall that stranded millions of perfectly capable machines. Count breaks technically and macOS breaks *far more*; but Apple's breaks arrive as scheduled funerals — announced, dated, bridged — so none of them is ever a broken *promise*, while Microsoft's compatibility is heroic and its words are unscheduled, so each reversal lands as betrayal. The outrage tracks promises, not compatibility — which sharpens this card's title one last time: courage is mostly the discipline of never promising what you have not scheduled.

**And the accounting insight, the card's actual moral: an open-ended compatibility promise accrues interest forever.** Every fossil in the Ghost's museum is a promise still making payments — in silicon, in boot code, in test matrices — decades after anyone wanted the thing itself. Apple's policy amounts to *refinancing*: pay the principal in scheduled lump sums, in public, and book the outrage as a marketing event. The genius is not the breaking; anyone can break things. It is the schedule — and the discipline, three transplants deep, of never once missing a payment on the bridge that makes the breaking survivable.

The epilogue's asterisk belongs to Brussels: the USB-C mandate proved the promise-breaker is not sovereign. Above the company that schedules funerals sits a regulator that can schedule one *for it* — and the fossil record of [[The Ghost of Drive A]] suggests that in the long run, the only forces that ever actually kill a compatibility promise are a company with a demolition calendar, or a law.

## Where this surfaces in the vault

- [[The Ghost of Drive A]] — the thesis this card answers: the museum of unbreakable promises, and its epilogue's two exits (pay like Python 3, or design the promise to keep itself like UTF-8). This card is the third exit: time-box the promise.
- [[CISC vs RISC]] — the x86 world's zero architecture migrations against Apple's three, and the A20-shaped price of never breaking.
- [[Compilers and Interpreters]] — Rosetta and Rosetta 2 are that card's translation spectrum shipped as products: dynamic (just-in-time) binary translation in 2006, ahead-of-time translation with a JIT reserve in 2020.
- [[Operating Systems]] — Classic, Carbon and Catalina are OS-level promises and their scheduled ends; the OS is where compatibility lives and dies.
- [[Inertia and Bootstrapping]] — ecosystem inertia as the force that vetoes breaking for everyone else, and what it costs to pay it down deliberately.
- [[You Never Expect the Change of Needs]] — the sequel in both directions: why the funerals are necessary (every generous ceiling dies of changed needs), and the flip side no funeral plans for — the consequences of a change are as unpredictable as the needs, and sometimes the surprise is a gift.

## Receipts

- Phil Schiller, Apple keynote, 7 Sept 2016: "It really comes down to one word: courage. The courage to move on, do something new, that betters all of us." Widely transcribed; see The Ringer's and Fast Company's same-week coverage.
- Steve Jobs, WWDC keynote, 6 June 2005: "Mac OS X has been leading a secret double life for the past five years"; contemporaneous liveblogs (Macworld, The Mac Observer, Engadget) and Wikinews transcript.
- Phil Schiller, iPhone 5 keynote, 12 Sept 2012: Lightning as "a modern connector for the next decade" — retrospectives at 9to5Mac and MacRumors quote the line against the 2023 USB-C switch.
- Gary Davidian's 68k emulator: Computer History Museum oral history (interviews by Hansen Hsu, Feb–Mar 2019, catalogue 102781078) and the CHM blog essay "Transplanting the Mac's Central Processor."
- Rosetta's engine: Transitive Corporation's QuickTransit, licensed for the 2006 Intel transition; Rosetta removed in Mac OS X Lion (2011); Classic environment ended with Leopard (2007); 64-bit Carbon cancelled at WWDC 2007; 32-bit support ended in macOS Catalina (2019). Standard histories at Ars Technica's OS X reviews and Apple's own transition documentation.
- Final Cut Pro X launch and refunds: AppleInsider and MacRumors, June 2011; the missing-features list (tape output, EDL/XML, legacy project import) per contemporaneous coverage; satirised on Conan.
- EU Common Charger Directive (2022), USB-C required for phones sold in the EU from end-2024; iPhone 15 adopted USB-C Sept 2023.
- iMac introduction (May 1998, shipped August) dropping floppy/ADB/serial for USB: any standard Apple history; the "Hello (again)" campaign is Apple's own.

---
chinese: A 盘的幽灵 (A pán de yōulíng) — 兼容性不许任何东西死去
prerequisites:
  - "[[Operating Systems]]"
  - "[[CISC vs RISC]]"
  - "[[Text Encoding]]"
  - "[[Inertia and Bootstrapping]]"
leads_to:
  - "[[Courage]]"
tags:
  - type/story
  - subject/computer-science
  - era/19c
  - era/20c
  - era/21c
  - cast/hollerith
  - cast/sholes
  - cast/kildall
  - region/usa
---

# The Ghost of Drive A A盘的幽灵

> *Your computer boots from C: because a machine you have never seen had two floppy drives. Nothing in computing ever really dies. It becomes load-bearing.*

## Cast of Characters

- **Christopher Latham Sholes** (1819–1890) — Milwaukee printer and inventor; arranged the letters on the first commercial typewriter in the 1870s so its type bars would jam less. You typed on his compromise today.
- **Herman Hollerith** (1860–1929) — punched-card pioneer of the 1890 US census; his company became part of IBM, and his card's dimensions still govern how wide your code is allowed to be.
- **Gary Kildall** (1942–1994) — wrote CP/M, the first standard microcomputer operating system, and lettered its disk drives A and B.
- **The Lotus 1-2-3 team** (1983) — decided, reasonably, that pretending 1900 was a leap year would hurt nobody.
- **The Intel 8042** — a chip hired to watch the keyboard, moonlighting for forty years as the gatekeeper of the twenty-first bit of your address bus.

## 中文锚点

为什么 Windows 的硬盘是 **C 盘**?先讲那个最要紧的反转:**C 盘和 C 语言毫无关系**——它只是排在第三。A 和 B 曾经是两个软盘驱动器(1981 年的 IBM PC 就靠它们);1983 年硬盘成为标配时,只能领到下一个没被占用的字母。软驱死了二十多年,可 A 和 B 至今仍然为它们空着——**两个为再也不会回来的机器保留的车位**。这张卡片是一座"化石博物馆":Excel 至今坚持 **1900 年 2 月 29 日存在**(Lotus 1-2-3 为了简化算法,假装 1900 年是闰年,微软为了兼容 Lotus 的文件**故意抄了这个 bug**,而今天它已被写进国际文件标准——修复它会让世上所有表格的日期集体倒退一天);Windows 的文本文件每行末尾多一个字符,因为打字机上的"回车"其实是两个物理动作:**滑架归位 + 走纸一行**,六十年代的电传打字机照抄,CP/M 照抄电传,DOS 照抄 CP/M,于是 2026 年的 git 还在为 1960 年代打字滑架的移动时间报 warning;代码"每行不超过 80 字符"来自 1928 年 IBM 打孔卡的宽度,而打孔卡的尺寸(据 IBM 自己的档案)来自 **1887 年的美元钞票**——为了能装进财政部原本用来放钞票的现成柜子;你手机玻璃屏上的键盘没有任何机械部件,却忠实复刻着 1873 年为防止铅字杆卡住而设计的 QWERTY;今天的孩子第一次见到真软盘,会由衷地赞叹"哇,你把保存按钮做成实物了!"——图标活得比实物久,久到**因果在下一代人眼里倒了过来**;而每台 Intel 电脑开机的第一个瞬间,在长达四十年的时间里都假装自己是 1978 年那颗只认 1 MB 内存的 8086——负责这场假装的开关,竟接在**键盘控制器**的一个闲置引脚上。寓意:**兼容性是对过去许下的、要由未来来偿还的承诺**;今天维持它永远比打破它便宜,所以它永远不会被打破。

## The Story

### Prologue — the wrong C

Ask a room of students why the hard disk is C:, and someone will guess the C language — a fair guess, since [[A, B, C]] just spent a whole story on how that C got its name. Wrong dynasty. The two Cs have nothing in common except that both were third in a line, and that neither can ever be renamed now.

The drive letter's real story is shorter and stranger: **C: is third because two machines you have never seen were first and second.** They were floppy-disk drives. They have been gone for a generation. Their letters are still reserved — two empty parking spaces at the front of every Windows machine, held for hardware that died before you were born.

That is the pattern this whole story is about, and once you can see it you will find it everywhere: in your calendar, your text files, your keyboard, your code style guide, and the first instant of your computer's boot. Computing never removes anything. It builds on top, and the ground floor becomes archaeology that still executes.

![[ghost-drive-a-fossil-map.svg|720]]

### Wing 1 — the two empty parking spaces

In the early 1970s Gary Kildall wrote **CP/M**, the operating system that made microcomputers usable, and he needed names for disk drives. He had worked on IBM's CP/CMS time-sharing system, where a user's disks were identified by single letters — and CP/M's drives came out lettered the same way: the first floppy was **A:**, the second **B:**. (Kildall never wrote down where the letters came from, so the CP/CMS inheritance is probable rather than proven — even the fossils have fossils of uncertain ancestry.)

The IBM PC of 1981 ran PC DOS, which was built in CP/M's image, and shipped with one or two floppy drives: A: and B:. Machines with a single physical drive still had *both letters* — DOS simply mapped A: and B: to the same drive and paused with the era's most honest error message, `Insert diskette for drive B: and press any key when ready`, whenever a program wanted "the other disk". One drive, two names, and a human being serving as the robot arm.

![[ghost-drive-a-swap-comic.png|640]]

Then, in March 1983, the IBM PC XT shipped with a **10-megabyte hard disk as standard equipment**. The disk needed a letter. The first two were taken. It became **C:** — not a decision, just the next slot in a queue.

Everything after that is the interesting part, because *nothing after that ever changed*. Floppy drives shrank, then vanished entirely; the hard disk became the boot device, the centre of the machine, the thing everything else orbits — and it kept the letter of a third-place finisher. Windows today will happily let you assign A: to a drive, and essentially nobody does; a fresh installation still lands on C:, because forty years of software, documentation, batch files, and human reflexes assume it. The letters A and B are the ghost: reserved, empty, waiting for floppies that will never come.

### Wing 2 — the day that never happened, now required by an international standard

Open Excel, type `59` in a cell, format it as a date: **February 28, 1900**. Type `61`: **March 1, 1900**. Type `60`: **February 29, 1900** — a day that never happened. The year 1900 was not a leap year (century years must be divisible by 400), and every calendar on Earth agrees. Except the spreadsheet's.

The chain of custody is a perfect specimen, because every link was a *reasonable decision by someone with a name*. **Lotus 1-2-3** (1983) stored dates as serial numbers counted from 1 January 1900, and used the simple every-fourth-year leap rule — smaller code, faster check, and the error only misdates things in January and February of 1900, which harmed nobody's ledger. **Microsoft** then needed Excel to import every Lotus file in the world without shifting a single date — so it copied the phantom day *on purpose*: bug-for-bug compatibility, as deliberate as any feature. And Microsoft's own documentation, four decades on, explains why it can never be fixed: correct the calendar and *almost all dates in almost all existing spreadsheets would decrease by one day*. The cost of the bug is a ghost day in a February nobody computes with; the cost of the fix is every spreadsheet on Earth, quietly wrong by one.

The ending outdoes the setup: when the Office file formats were standardised as **Ecma Office Open XML**, the 1900 leap-year behaviour was written into the specification. The bug is no longer a bug. It is a *requirement*, with a standards body defending it.

Two shadows complete the exhibit. Excel for the **Macintosh** (1985) counted from 1 January **1904** instead — early Macs didn't handle earlier dates, and starting after the trouble neatly skips the phantom day — with the result that a workbook moved between the two systems could shift every date by 1,462 days: two calendars, one company, both correct by their own axioms. And Visual Basic's date system pins day zero to **December 30, 1899** — offset one day from where you'd expect, precisely so that its serial numbers agree with Excel's everywhere *after* the day that never happened. The bug casts a shadow, and the shadow casts another.

### Wing 3 — the second character at the end of every line

Make a text file on Windows and every line ends with **two** invisible characters, `\r\n`; on Linux and macOS, one, `\n`. This single difference has broken builds, corrupted scripts, and filled `git` with warnings for decades. Its cause is the physical anatomy of a typewriter.

Ending a line on a typewriter takes **two motions**: slide the carriage back to the left margin (*carriage return*), and turn the platen up one line (*line feed*). Teleprinters — typewriters that type over a wire, the machines the whole ASCII control-character table in [[Text Encoding]] was designed for — encoded the two motions as two separate codes, CR (13) and LF (10), not least because a heavy print head genuinely *needed the travel time*: sending CR first gave the carriage a head start while the LF arrived. Multics, in the 1960s, decided a text file should record intent, not machinery — one newline character, and let each device's driver translate — and Unix inherited the bare `\n`. CP/M stayed faithful to the teletype and kept both characters; DOS copied CP/M; Windows copies DOS. So in 2026, files disagree about how lines end because of the **travel time of a print carriage** on hardware that has not existed for half a century — and the internet took the typewriter's side: HTTP and email are specified, to this day, with `\r\n` at the end of every header line.

### Wing 4 — why your code stops at column 79

Python's official style guide caps lines at **79 characters**. Terminal windows default to **80**. Old FORTRAN and COBOL forms assume 80. The number comes from the **IBM punched card**, standardised in 1928 with 80 columns of rectangular holes — the format every programmer for forty years typed programs onto, one line per card, which is why a line and a card became the same thing and 80 became the width of *thought*.

And the card's own dimensions? Herman Hollerith's original cards — built for the 1890 US census — were, by IBM's own account, made the size of the **US dollar bill of the day**, so that the Census Bureau could store them in the Treasury's existing filing cabinets and trays. Follow the chain with a straight face: a style-guide rule enforced by linters in 2026 descends from the width of a punched card standardised in 1928, which descends from the size of an 1887 banknote, which was chosen to fit **second-hand government furniture**. Nobody in that chain did anything foolish. That is the point.

### Wing 5 — the keyboard that outlived its excuse

The QWERTY layout was arranged in the 1870s by Christopher Latham Sholes for the first commercial typewriter, and the honest version of *why* comes with error bars, the way legends should. What the evidence supports: early type bars swung up from a basket and **jammed** when neighbouring bars were struck in quick succession, so the layout evolved to separate common letter pairs — an engineering fix for a mechanical fault. What the folklore added: that it was designed to "slow typists down" (no — jam-avoidance actually let typists go *faster*), and that the top row conveniently contains TYPEWRITER so salesmen could demo it without hunting (it does contain the letters; that this was the reason is unproven). Even the standard cautionary sequel — heroic, superior Dvorak suppressed by lock-in — has its own error bars: the famous studies favouring Dvorak's layout trace substantially back to Dvorak himself, and the honest literature (*The Fable of the Keys*) argues the efficiency gap may be small. What nobody disputes: the jam it was built to avoid stopped being possible over a century ago, and the layout sailed on regardless — onto electric typewriters with no swinging bars, onto computer keyboards with no mechanics at all, and onto your phone, where a sheet of glass with no moving parts faithfully renders an 1873 compromise between metal levers.

### Wing 6 — the icon aisle

A quick walk past the smaller display cases. The **save icon** is a 3.5-inch floppy disk, drawn today by designers who never held one, recognised by students who could not name the object — the disk died, the *picture* of the disk became the word "save".

And right here the ghost story reaches its best scene, because for anyone born this century the causality now runs **backwards**. Hand a student an actual floppy disk and the reaction — reported by a generation of teachers and parents in a hundred tellings, the best-known version being the child who congratulated a parent for having *3D-printed the save icon* — is delight at the tribute: *cool, you made the save button real!* Stop and look at what just happened. The object the icon was copied *from* is now read as a copy *of the icon*. The sign didn't merely outlive its referent; it got promoted to **original**, and reality is now graded on how well it resembles the symbol. Archaeologists know this failure mode — future generations mistaking the thing for a replica of its own image — but computing achieved it in a single human lifetime, fast enough that the person being congratulated once carried the disks.

![[ghost-drive-a-save-button-comic.png|640]]

The rest of the aisle runs the same way, just less spectacularly. The **phone icon** is the handset of a desk telephone no longer on desks; you "hang up" a call because ending one used to mean physically hanging a receiver on a hook. Email's **CC** field is *carbon copy* — a sheet of carbon paper between two pages in a typewriter, ghost-writing the duplicate. None of these are jokes about designers being lazy. An icon's job is to be recognised, and the most recognisable picture is always yesterday's object — so interfaces are, by their nature, museums.

![[ghost-drive-a-archaeologist-comic.png|640]]

### Wing 7 — the deepest stratum: the first second of boot

The deepest fossil is not on the disk or the screen. For roughly four decades, it was in the processor itself.

Every Intel x86 chip — for most of that time, no matter how new — woke up in **real mode**: pretending to be the 8086 of 1978, a 16-bit machine that can see exactly one megabyte of memory. Your machine's firmware then performs the ritual of switching the processor, step by step, up through its own evolutionary history into the present. Sixteen cores and a hundred gigabytes of RAM, and the first instants of every boot were spent being 1978, because code written for 1978 had to keep running.

Inside that fossil sits a smaller, stranger one. The 8086's addresses wrap around: go past the top of its one megabyte and you come back to zero. Some programs *used* that overflow on purpose. When the 1984 IBM PC/AT shipped a processor that could address more memory, the wraparound vanished — and old software broke. IBM's fix was a switch that could force the twenty-first address wire (**the A20 line**) to zero, faking the old overflow — and, needing somewhere to put the switch, wired it to **a spare pin on the Intel 8042 keyboard controller**. For the next several decades, the chip that read your keystrokes also decided whether your computer's memory behaved like 1978, and a generation of PCs could greet you with `A20 line failed` — a boot error about a compatibility hack for an overflow bug in a dead processor, routed through the keyboard. Intel's manuals only began declaring the mechanism obsolete around 2013, and a 2023 Intel proposal (x86-S) finally suggested processors that boot directly into the present. It took forty years to propose removing the pretence — and the proposal had to be *proposed*, carefully, to a world still not sure nothing depends on it.

This is [[CISC vs RISC]]'s backward-compatibility row lived out at maximum absurdity: x86 still honours instructions designed in 1978, and until recently honoured the *bugs* too.

### Epilogue — the promise, and the two ways out

Line the exhibits up and one shape emerges. In every wing, someone made a locally correct decision; the decision leaked into a format, a file, a habit, a reflex; and from that moment, **the cost of keeping it was paid in invisible pennies every day, while the cost of removing it would be paid all at once, by everyone, visibly**. Compatibility is a promise made to the past that the future has to keep — and on any given day, keeping it is cheaper than breaking it. There is never a day the ledger says "break it now". So the fossil stays, forever, and the system's history becomes readable in its own strata, like tree rings — which is why [[Inertia and Bootstrapping]] treats inertia as a force to be *engineered around*, not sneered at.

Computing at large has found exactly two honest ways out, and tried both. The first is to **break the promise and pay**: Python 3 fixed real design flaws in Python 2 in 2008, the old world refused to die, and the migration consumed *twelve years* — the ecosystem's own drive-A ghost, kept on life support until 2020. The price of breaking is real; the fossils exist because it usually isn't worth it. The second way is rarer and better: **design the new thing so the promise keeps itself**. The masterpiece here is UTF-8 — sketched on the placemat in [[Text Encoding]] — which encodes all of Unicode while remaining byte-for-byte identical to ASCII on ASCII text, so that every text file from the old world was *already valid* in the new one. The past didn't have to be dragged forward. It was simply, retroactively, always compatible. That is what it looks like when an engineer treats the past as a design constraint instead of an embarrassment. (There is a third exit — **time-box the promise**: break only with a bridge, and never build a bridge without a published demolition date — but only one company has ever dared run it as standing policy, and that story is [[Courage]].)

So: the language C got its letter by refusal, and the drive C: got its letter by queue position — [[A, B, C]] and this story are the two faces of the same lesson, that **names and layouts are sediment**. Somewhere under every interface you will ever use, there is a floppy disk, a dollar bill, a jammed type bar, a print carriage mid-travel, and a day in February that never happened — all still on duty. Learn to see them, and every "weird rule" in computing becomes a fossil with a face.

## Cultural ripples

- **Serial 60.** February 29, 1900 exists in every copy of Excel, is defended by Microsoft's documentation, and is *required* by the Ecma Office Open XML standard — the only calendar error with a standards body.
- **`warning: LF will be replaced by CRLF`** — git's most-seen warning is a dispatch from the 1960s about typewriter carriage travel.
- **79 characters** — PEP 8's line limit as the great-grandchild of an 1887 banknote.
- **The save icon** — the picture outliving the object so completely that the picture *became* the verb — and the object, when met in the flesh, is now praised as a well-made replica of its own icon.
- **`A20 line failed`** — a boot message about faking a 1978 overflow bug through the keyboard chip; retired only in the 2010s.
- **Two empty parking spaces** — A: and B:, still reserved on every Windows machine, for drives that will never return.

## Where this surfaces in the vault

- [[Operating Systems]] — the OS that inherited CP/M's letters, and the boot sequence whose first instants long replayed 1978.
- [[CISC vs RISC]] — instruction-set accretion as the same fossil logic inside the processor: x86 honours 1978 so thoroughly it long honoured 1978's bugs.
- [[Text Encoding]] — the ASCII control characters as teletype ghosts (CR, LF, and the bell), GBK's "backward compatibility is forever", and UTF-8 as the promise designed to keep itself.
- [[A, B, C]] — the sibling story: how the *other* C got its name, and the living fossils (`a.out`, `creat`, the fossil declaration) inside the language.
- [[The Arrow That Pointed the Other Way]] — the trio's opener: symbols, like letters and layouts, are chosen in a hurry and kept forever.

## Receipts

- Microsoft, "Excel incorrectly assumes that the year 1900 is a leap year" and "Differences between the 1900 and the 1904 date system in Excel" (Microsoft Learn documentation) — the deliberate Lotus compatibility, the why-it-can't-be-fixed reasoning, and the 1,462-day shift. Ecma-376 (Office Open XML) — the leap-year behaviour as specification.
- On CP/M and drive letters: Kildall's CP/M (1974) and its CP/CMS ancestry per the standard histories (Computer History Museum, "Early Digital Research CP/M Source Code"); the inheritance is probable, not documented by Kildall himself. IBM PC XT specifications (March 1983) — first IBM PC with a standard hard disk, PC DOS 2.0.
- On the A20 gate: OS/2 Museum, "The A20-Gate Fallout"; OSDev documentation of the A20 line and the 8042 keyboard controller's spare pin; Intel Software Developer's Manual (2013 era) deprecating A20M#; Intel, "Envisioning a Simplified Intel Architecture" (x86-S proposal, 2023).
- On QWERTY, with error bars: David, P. A., "Clio and the Economics of QWERTY," *American Economic Review* 75(2), 1985 (the lock-in reading); Liebowitz, S. and Margolis, S., "The Fable of the Keys," *Journal of Law & Economics* 33(1), 1990 (the rebuttal, including the Dvorak-studies provenance).
- On punched cards: IBM archives on the 80-column card (1928) and the currency-sized Hollerith card; the 1890 census machinery.
- On line endings: the ASA X3.4 control-character assignments; Multics and Unix newline conventions per Ritchie's Unix retrospectives; RFC 2616/9112 (HTTP) mandating CRLF.

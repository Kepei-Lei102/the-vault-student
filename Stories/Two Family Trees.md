---
chinese: 两棵家谱树 (liǎng kē jiāpǔ shù) — 全世界的内核只有两个祖先
prerequisites:
  - "[[Space Travel]]"
  - "[[A, B, C]]"
leads_to:
  - "[[Courage]]"
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - cast/torvalds
  - cast/tanenbaum
  - cast/cutler
  - cast/thompson
  - cast/jobs
  - region/usa
  - region/finland
---

# Two Family Trees 两棵家谱树

> *Every mainstream device on Earth — every phone, laptop, server and supercomputer — runs a kernel descended from one of two operating systems written for minicomputers in the 1970s. Both were planted by people who had just walked away from a failure. One tree is a gnarled oak with branches grafted from three universities and a Finnish bedroom. The other is a single straight trunk grown by one furious man.*

## Cast of Characters

- **Ken Thompson and Dennis Ritchie** — Bell Labs, 1969: the root of tree one ([[Space Travel]] is the planting).
- **The University of California, Berkeley** — grafted the Unix branch called **BSD** in the late 1970s; everything Apple sells still carries its wood.
- **Rick Rashid and Avie Tevanian** — Carnegie Mellon, 1985: **Mach**, the microkernel that became the core of NeXT's and then Apple's operating systems.
- **Andrew Tanenbaum** (b. 1944) — professor in Amsterdam; wrote **Minix** (1987) to teach operating systems, and the post that started the most famous argument in the history of software.
- **Linus Torvalds** (b. 1969) — a 21-year-old in Helsinki with a new 386 and "just a hobby".
- **Dave Cutler** (b. 1942) — the architect of **VMS** at DEC, then of **Windows NT**: tree two, root and trunk.
- **Steve Jobs** — bought Mach-plus-BSD with NeXT, then sold it back to Apple and called it the future.

## 中文锚点

你现在用的每一台设备——安卓手机、iPhone、Mac、Windows 电脑、支撑互联网的服务器、世界前五百的超级计算机——它们的**内核**（操作系统最核心的那一层）只有**两个祖先**，而且都是 1970 年代为小型机写的。**第一棵树是 Unix**（1969 年贝尔实验室，[[Space Travel]] 讲了它怎么诞生）：一根枝条在伯克利被嫁接成 BSD，又和卡内基梅隆的 Mach 微内核拼在一起，成了乔布斯的 NeXT 公司的内核；1996 年苹果买下 NeXT，这个内核改名 Darwin，今天 macOS、iOS、iPadOS、watchOS 全跑在它上面。另一根枝条来自一本教科书：阿姆斯特丹的教授 Tanenbaum 写了 Minix 教操作系统课，芬兰一个 21 岁的学生 Linus Torvalds 看了之后，1991 年 8 月 25 日在新闻组发帖："我在写一个（免费的）操作系统（只是个爱好，不会像 GNU 那样又大又专业）"。那个爱好叫 Linux，今天跑在每一台安卓手机、几乎每一台云服务器以及全部五百台顶级超算上。1992 年 1 月，教授公开发帖《LINUX 已经过时了》，说单体内核是"倒退回 1970 年代"，学生回敬"Linux 在几乎所有方面都把 Minix 打得落花流水"——教授在理论上是对的，在历史上输了。**第二棵树是 VMS**（DEC 公司，1977 年），作者 Dave Cutler；1988 年他的新项目被砍，他愤然离开，十月份被微软招走，五年后交出 **Windows NT**——从 2001 年的 XP 起，所有家用 Windows 都跑在 NT 上，直到今天的 Windows 11。两棵树，都比个人电脑更老；两棵树，都是从一次失败里长出来的。

## The Story

### Act I — Tree one, the graft that became Apple

[[Space Travel]] told how the root went in: Bell Labs, 1969, a cast-off PDP-7 and a video game. What grew from it was not one trunk but a thicket, because Unix was given away to universities almost for free, and universities do not leave things alone.

At **Berkeley**, from 1977, a graduate student named Bill Joy and a rotating cast of colleagues kept adding to the AT&T source — a better editor, virtual memory, and eventually the networking code that would carry the early internet — until their version, the **Berkeley Software Distribution**, was a branch as thick as the trunk. At **Carnegie Mellon**, from 1985, Rick Rashid's group built **Mach**: not a Unix but a *microkernel* — the smallest possible core, doing only memory, messaging and I/O, with everything else pushed out into ordinary programs. Mach was meant to be the clean rewrite the field had been waiting for.

The graft happened at **NeXT**, Steve Jobs's company-in-exile after Apple pushed him out in 1985. NeXTSTEP's kernel, **XNU**, was built from Mach 2.5 as the core with "the bulk of the 4.3BSD kernel modified to run atop Mach primitives" — the microkernel *and* the Unix it was supposed to replace, welded together, because a microkernel alone could run nothing anyone wanted. It was a beautiful machine that almost nobody bought.

Then, on **20 December 1996**, a failing Apple paid **$429 million** for NeXT to get an operating system — and got Jobs back in the same transaction. XNU became **Darwin** (2000), Darwin became the floor under Mac OS X, and Mac OS X became the floor under everything Apple has shipped since: **macOS, iOS, iPadOS, watchOS, tvOS, visionOS**. Every iPhone runs a kernel that is a Carnegie Mellon research project holding a Berkeley graft of a Bell Labs root. Tanenbaum's microkernel idea, which he would soon be defending in public against a Finnish student, is inside a billion pockets — hybridised, which is not quite what he meant.

### Act II — Tree one, the other branch: a textbook and a hobby

Andrew Tanenbaum had a different complaint about Unix: he could not *teach* it, because by the 1980s AT&T's licence forbade showing students the source. So in 1987 he wrote his own — **Minix**, a small Unix-like system that came printed in the back of his textbook, every line readable. It was designed to be understood, not to be fast, and it was a microkernel, because that is how a professor thinks an operating system should be built.

In Helsinki, a 21-year-old computer-science student bought a 386 PC in January 1991, ran Minix on it, and found it too small for what he wanted to do. On **25 August 1991** he posted to the Minix newsgroup:

> *"Hello everybody out there using minix — I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones."*

The first release, 0.01, went up on **17 September 1991**. Torvalds had wanted to call it *Freax*; the volunteer who ran the university's download server, Ari Lemmke, thought the name was bad and put it in a directory called **linux** without asking him. It stuck. With version 0.12, effective **1 February 1992**, Torvalds put it under the GNU General Public License — the decision that made the hobby a commons.

Follow the branch forward and it reaches almost everything. **Android** (first phone **23 September 2008**) is a Linux kernel with Google's userland on top — two billion devices. The servers behind essentially every website, cloud and app run Linux. And since **November 2017, all five hundred of the TOP500 supercomputers** have run it — not most, all. The professor's teaching toy had produced, by way of one student who wanted a bigger toy, the most widely deployed kernel in history.

### Act III — "LINUX is obsolete"

Which is the setting for the argument. On **29 January 1992** — Linux four months old, still on Tanenbaum's own newsgroup — the professor posted under the subject line **LINUX is obsolete**:

> *"MINIX is a microkernel-based system. … LINUX is a monolithic style system. This is a giant step back into the 1970s."*
> *"To me, writing a monolithic system in 1991 is a truly poor idea."*
> *"Be thankful you are not my student. You would not get a high grade for such a design :-)"*

The student replied the same day, and did not take it well:

> *"Your job is being a professor and researcher: That's one hell of a good excuse for some of the brain-damages of minix."*
> *"linux still beats the pants of minix in almost all areas."*

— and, a day later, in a post titled *Apologies*: *"I over-reacted, and am now composing a (much less acerbic) personal letter to ast."*

Read it as a fight about architecture and Tanenbaum was largely right. A **microkernel** keeps the privileged core tiny and runs drivers and file systems as separate, replaceable, crash-isolated programs; a **monolithic** kernel puts everything in one privileged blob, which is faster and simpler and means one bad driver can take the whole machine down. Every operating-systems textbook — including his — still teaches the microkernel as the better design, and [[Operating Systems]] carries the trade-off in full.

Read it as history and he lost completely. Linux shipped, ran fast on cheap hardware, and gathered thousands of contributors precisely *because* a monolithic kernel was something a lone student could get working in a bedroom in four months. The "correct" design needed a decade and a research budget; the "obsolete" one needed a 386 and a newsgroup. Tanenbaum's own idea survived — inside XNU, as a hybrid, sold by the company that shipped the most expensive computers. The professor was right in theory and wrong in the only court that returns a verdict.

![[two-family-trees.png|700]]

### Act IV — Tree two: one man, one trunk

The second tree has no thicket, because it was grown by one person who did not accept grafts.

In June 1975 **Dave Cutler**, with Dick Hustvedt and Peter Lipman, was made technical lead of *Starlet* — the operating system for DEC's new 32-bit VAX machines. It shipped in 1977 as **VMS**, and it was everything Unix was not: designed, documented, consistent, and built by an engineer who, in the words of a colleague quoted in G. Pascal Zachary's *Show-stopper!*, regarded Unix as "his lifelong foe … a junk operating program designed by a committee of PhDs."

In 1988 DEC cancelled Cutler's next project — **PRISM**, a RISC machine, and **MICA**, its operating system — in favour of a rival internal design. Cutler left. In **October 1988** Microsoft hired him, with much of his team, to build the operating system that would replace DOS-based Windows underneath: a portable, secure, multi-user kernel, designed from a blank page by a man who had already designed one. **Windows NT 3.1** shipped on **27 July 1993**. For eight years it ran beside the consumer line; with **Windows XP in 2001** the consumer line was quietly retired and every Windows since — 7, 10, 11 — has been NT underneath. One trunk, no grafts, still growing.

The tree comes with a joke, and the joke deserves its honest label. Take V-M-S and step each letter forward by one: **W-N-T**. The observation was popularised by Mark Russinovich's 1998 article *Windows NT and VMS: The Rest of the Story*, which laid the two systems' architectures side by side and found them siblings; the same trick had once been used to claim HAL, the computer in *2001*, was IBM shifted back. Cutler has never confirmed that NT was named that way, and "New Technology" is the official story. Treat it as what it is: too good to be an accident, and unproven.

## Cultural ripples

**Two trees, both older than the personal computer.** The PC arrived in 1981; both kernels under every PC and phone predate it. What runs the world was not designed for the world it runs — it was designed for a room-sized VAX and a cast-off PDP-7, and has been carried forward through five decades of hardware by exactly the discipline [[Courage]] describes: keep the old promises, or break them on a published schedule. (Darwin rode every one of Apple's processor migrations; NT was *built* portable, which is why it survived the death of every architecture Cutler first ran it on.)

**Failure planted both.** Unix was built by people retreating from Multics; NT by a man whose project had just been cancelled; Linux by a student for whom the teaching system was not enough. None of the three was the sanctioned project. [[Space Travel]]'s lesson again, three times over: the room that ships is rarely the room that was funded to.

**The argument never ended — it just became products.** Microkernel purity lives on in the research world and in a few safety-critical systems; the monolithic kernel won the numbers; and the hybrid that Tanenbaum would call a compromise sits in every Apple device. Both sides of the 1992 flame war are running in your pocket right now, and neither man's grade was final.

## Where this surfaces in the vault

- [[Space Travel]] — the planting of tree one; this card is the growth that story reserved.
- [[A, B, C]] — the language that grew alongside the first tree; C is why Unix could be carried to every machine on every branch.
- [[Operating Systems]] — the technical card: microkernel vs monolithic as a design trade-off, which this card shows being fought over in public.
- [[Courage]] — how a kernel older than the PC survives five decades of hardware: promises time-boxed and kept.
- [[A Rich Neighbor Named Xerox]] — the interface layer was fought over the same decade, in a different courtroom; NeXT is where Jobs took what he learned.
- [[Compilers and Interpreters]] — the GPL and the compiler that made Linux buildable by anyone.

## Receipts

- Linus Torvalds, comp.os.minix, 25 August 1991 — the announcement, verbatim; 0.01 released 17 September 1991; the Freax/Linux renaming by Ari Lemmke; GPL from version 0.12, effective 1 February 1992.
- Andrew Tanenbaum, *LINUX is obsolete*, comp.os.minix, 29 January 1992; Torvalds's reply the same day and *Apologies* on 30 January — the full thread is reproduced as Appendix A of *Open Sources: Voices from the Open Source Revolution* (O'Reilly, 1999), the source of every quoted line.
- XNU: Mach 2.5 core with "the bulk of the 4.3BSD kernel modified to run atop Mach primitives"; Apple's acquisition of NeXT, 20 December 1996, $429 million; Darwin 2000; the six current Apple operating systems on it.
- Dave Cutler: VMS technical lead from June 1975; PRISM/MICA cancelled 1988; joined Microsoft October 1988; Windows NT 3.1 released 27 July 1993; consumer Windows onto NT with XP, 2001. The "lifelong foe" line via G. Pascal Zachary, *Show-stopper!* (1994).
- Mark Russinovich, *Windows NT and VMS: The Rest of the Story* (Windows NT Magazine, 1998) — the architectural comparison and the one-letter observation; unconfirmed as the origin of the name.
- Android 1.0, 23 September 2008; TOP500 at 500/500 Linux from the November 2017 list.

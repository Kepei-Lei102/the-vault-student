---
chinese: 辅助存储 / 外存 (fǔzhù cúnchǔ / wàicún)
prerequisites:
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Gray Code]]"
leads_to:
  - "[[Operating Systems]]"
  - "[[File Handling]]"
  - "[[File Systems]]"
  - "[[Error Detection and Correction]]"
  - "[[How a Chip Is Made]]"
  - "[[Input and Output Devices]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-3-3
  - syllabus/9618-3-1
  - syllabus/IB-CS-A1-1
  - type/deep
  - misconception/deleting-means-erasing
  - misconception/storage-lasts-forever
  - misconception/defrag-everything
  - misconception/ssd-is-a-big-usb-stick
---

# Secondary Storage 辅助存储

> *Nothing in nature is a bit. A patch of magnetised rust, a puddle of trapped electrons, a pit pressed into plastic — each is an **amount**: smeary, analog, drifting with temperature and age. Storage works because somewhere a circuit draws a line and decides — this much means 1, that little means 0. Every storage technology on this page is a different answer to the same dangerous question: **how do I stay far from the line?***

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| secondary storage | 辅助存储器 / 外存 | non-volatile storage the CPU cannot address directly; where files live |
| non-volatile | 非易失性 | keeps its contents with the power off |
| hard disk drive (HDD) | 机械硬盘 | magnetic storage on spinning platters |
| platter / track / sector | 盘片 / 磁道 / 扇区 | the disk's surface / one concentric ring / one slice of a ring |
| solid-state drive (SSD) | 固态硬盘 | flash storage, no moving parts |
| flash memory | 闪存 | floating-gate storage erased a block at a time |
| floating gate | 浮栅 | the insulated island that traps electrons — the flash bit |
| optical disc | 光盘 | CD/DVD/Blu-ray — pits and lands read by laser |
| ROM (read-only memory) | 只读存储器 | non-volatile firmware; the family PROM → EPROM → EEPROM |
| buffer | 缓冲区 | a memory waiting-area between devices of different speeds |
| virtual memory | 虚拟内存 | disk space the OS uses as overflow RAM |
| cloud storage | 云存储 | files kept on remote servers, reached over the internet |
| wear levelling | 磨损均衡 | spreading flash writes so no block dies early |
| over-provisioning | 预留空间 | hidden spare flash the controller keeps for wear levelling and block repair |

## Primary vs secondary — who answers the CPU

Pull the plug on a computer. Within a second, everything in [[RAM and the Memory Hierarchy|RAM]] is gone — yet tomorrow your essay is exactly where you left it. It survived because it was not *in the computer's memory* at all; it was in **secondary storage**.

**Primary storage** (RAM and ROM) is what the CPU touches directly: put an address on the address bus, get a word back in nanoseconds. **Secondary storage** is everything the CPU *cannot* address directly — it asks a **controller** to fetch whole **blocks** of data, which land in RAM before the CPU ever sees them. The trade is brutal and deliberate:

| | Primary (RAM) | Secondary (SSD / HDD) |
|---|---|---|
| CPU access | direct, by address | indirect, in blocks via a controller |
| power off | contents lost (except ROM) | contents kept |
| latency | ~100 ns | ~60 000 ns (SSD) · ~13 000 000 ns (HDD) |
| typical size | gigabytes | terabytes |
| job | the workbench | the warehouse |

The latency row keeps one unit on purpose — µs and ms make the numbers *look* neighbourly. Rescale it to human time: if RAM's 100 ns were **one second**, the SSD answers in **ten minutes** and the hard disk in **a day and a half**. That gulf is why the whole [[RAM and the Memory Hierarchy|memory hierarchy]] exists, and why the OS will do almost anything to avoid touching the disk mid-thought.

Secondary storage exists because we need data to be **permanent** — and because non-volatile media are vastly cheaper per byte, so the warehouse can dwarf the workbench. Much of it is **removable** — USB drives, SD cards, external disks, optical discs — storage that walks between machines.

Three physical technologies dominate, and the exam wants the *operation* of each: **magnetic**, **solid-state (flash)**, and **optical**. Before touring them, fix the reading frame — for each medium, ask the same four questions:

1. What *is* the bit, physically?
2. How is it **written**?
3. How is it **read back**?
4. What goes wrong near the **decision boundary** — and what trick keeps the bit clean?

The fourth question is the secret one. Recall how DRAM reads a cell: the bit line is parked at half the supply voltage and a **sense amplifier** decides which way a whisper of charge nudged it. That *decision* — analog amount in, clean bit out — happens in every technology below. The engineering is all in surviving the middle.

## Magnetic — the hard disk drive

![[secondary-storage-hdd-anatomy.svg|697]]

**Anatomy.** A stack of rigid **platters** coated in magnetic material spins at 5 400–7 200 revolutions per minute. Each surface is divided into concentric **tracks**, each track into **sectors** — the fixed-size blocks (traditionally 512 B, now usually 4 KiB) that the controller reads and writes. A **read/write head** rides on an actuator arm, one head per surface, all arms moving together. The head does not touch the platter: it *flies* on the air dragged around by the spinning disk, at a height of a few **nanometres** — scaled up, that is a jumbo jet flying a few millimetres above the ground, at 900 km/h, counting blades of grass. (This is why a running drive fears being dropped: a **head crash** — the head touching down — gouges the magnetic surface and takes the data with it.)

**The bit** is a patch of magnetic grains magnetised in one of two directions — in modern *perpendicular recording*, pointing **up** or **down** out of the platter surface.

**Writing** is the easy half: the head contains a tiny **electromagnet**, and a pulse of current flips the patch under it to the chosen direction. Magnetised regions hold their direction with the power off — that is the whole non-volatility story.

**Reading** hides the beautiful idea. You might expect the head to measure each patch's field and threshold it — strong-up means 1, strong-down means 0. It does not, because the signal's *amplitude* is untrustworthy: it drifts with flying height, temperature, and the age of the magnetisation. A fixed "this voltage means 1" line would be a decision boundary drawn in fog. So the disk reads **transitions instead of levels**: where the magnetisation *reverses* (a **flux reversal**), the moving head picks up a sharp pulse — and a reversal is unmistakable *whatever* the overall amplitude is doing, because it is a *change*, self-referenced against its own neighbourhood. The encoding follows the physics: **a reversal means 1, no reversal means 0** (the scheme called NRZI). The disk does not read bits off the platter; it reads *edges* — the same move [[Clock Domains and Metastability|clocked circuits]] use when they trust an edge and distrust a level, and a cousin of the one-bit-flip discipline of [[Gray Code]].

> [!info] The exam's model vs the modern head
> The syllabus model — data "read and written using electromagnets" — is exactly right for writing, and was true for reading until the 1990s (a reversal sweeping past a coil induces a pulse). Modern drives read with a **magnetoresistive** sensor instead: a film whose electrical resistance changes in a magnetic field, sensitive enough for today's microscopic patches. The *logic* is unchanged — it still detects reversals, not levels.

**The cost of moving parts.** Before any transfer, the arm must swing to the right track (**seek time**, ~9 ms) and the platter must rotate the right sector under the head (**rotational latency**). Mechanical milliseconds against electronic microseconds — the price appears in the worked example below. HDDs survive because of the other axis: **cost per terabyte**, still several times better than flash, which is why data centres and archives keep buying them.

## Solid-state — flash memory

![[secondary-storage-floating-gate.svg|697]]

**The bit** is a puddle of electrons trapped on a **floating gate** — an island of conductor buried inside a transistor, wrapped on every side by insulating oxide. A normal transistor switches on when its **control gate** is charged; in a flash cell, the floating gate sits *between* the control gate and the channel, and any electrons parked on it push back against the control gate's field. Charge on the island raises the voltage needed to switch the transistor on — the **threshold voltage**. That is the whole trick: *the stored charge is invisible, but the transistor's switching point betrays it.*

**Writing** means forcing electrons *through* the insulating wall. A large voltage bends the oxide barrier until electrons **[[Quantum Tunnelling|quantum-tunnel]]** across it onto the island — passing through a wall they classically could not climb; remove the voltage and the wall snaps shut behind them. The island has no wires — that is the point. Perfectly insulated, the charge just *stays*, for years, with no power at all.

**Reading** applies an in-between voltage to the control gate and checks whether the transistor conducts. Charged island → still off → read as 0; uncharged → on → read as 1. No moving parts, so access takes ~50 µs instead of ~10 ms — and a dropped SSD shrugs.

**Erasing** is the odd one out: tunnelling electrons *off* the island is done a whole **block** at a time (hundreds of kilobytes), not byte-by-byte. When Fujio Masuoka's team at Toshiba built the first such memory in 1984, a colleague remarked that block-erase wiped the chip like a camera *flash* going off — and the name stuck.

The whole cycle is really a story about **where the electrons flow** — forced through the wall, interrogated without being touched, flushed back out:

![[secondary-storage-flash-cell.mp4]]

Two wiring arrangements share the mechanism, and their names are honest — they describe the gate structure the cells form. **NOR** flash wires every cell its own contact to the bit line (parallel, like a NOR gate's inputs): any byte reachable at any moment — random access, so firmware can *execute in place* — but all those contacts cost silicon. **NAND** flash chains cells into **series strings** (like a NAND gate's stacked transistors) with a single contact per string: far denser and cheaper per byte, but readable only in whole **pages** — the engine of every SSD, SD card, and USB drive.

![[secondary-storage-nor-vs-nand.svg|560]]

**Packing more bits per island.** A single-level cell (SLC) stores one bit: island empty or full, two charge levels, one fat gap between them. Modern drives store **2, 3, or 4 bits per cell** (MLC, TLC, QLC) by distinguishing **4, 8, or 16 distinct charge levels** — same island, finer pencil. The catch is the decision boundaries: sixteen levels must fit where two used to live, so the gaps shrink and a slightly-leaked island can drift across a line. Two defences keep QLC honest:

- **The levels are numbered in [[Gray Code]] order.** Adjacent charge levels differ in exactly *one* bit — so a cell that drifts one level over corrupts one bit, not four. The rotary-encoder trick, replayed inside every flash cell you own.
- **Error-correcting codes** stored alongside the data mop up the stragglers ([[Error Detection and Correction]]).

![[secondary-storage-flash-levels.png|640]]

**Wear.** Every program/erase cycle rams electrons through the oxide, and the oxide scars — trapped charge accumulates until the cell can no longer hold its levels apart. Endurance runs from ~100 000 cycles for SLC down to around a thousand for QLC. The controller fights back with **wear levelling**: it constantly remaps data so writes spread evenly across all blocks, no block dying young while others sit idle. (This is also why *defragmenting an SSD is worse than useless* — see Misconceptions.)

**Over-provisioning.** Wear levelling needs room to manoeuvre — spare blocks to shuffle data through, and replacements for the blocks that eventually die. So manufacturers build the spare in, using a trick of the two unit ladders from [[Storage Units (Vocab)]]: NAND chips come off the production line in *binary* sizes, but the sticker is *decimal*. A "512 GB" drive physically carries 512 GiB ≈ 550 GB of flash, and the ≈ 7% difference is **over-provisioning** — a reserve the operating system never sees, spent on wear levelling, background garbage collection, and quietly retiring failing blocks. It is why a healthy SSD stays fast and reaches old age *by design*, not by luck. Enterprise drives push the same dial harder: a "400 GB" data-centre drive may carry that same 512 GiB of silicon, trading over a quarter of its sellable capacity for endurance and sustained write speed. The TB-vs-TiB gap, put to work.

![[secondary-storage-wear-comic.png|560]]

## The ROM family — how read-only learned to change its mind

[[RAM and the Memory Hierarchy]] left ROM as "non-volatile firmware the machine boots from." The full story is an evolution, and each generation answers one question more gracefully: ***how do I change my mind?***

| Generation | Programmed by | Erased by | Granularity |
|---|---|---|---|
| **Mask ROM** | the factory — bits printed into the silicon | never | — |
| **PROM** | the user, once — blowing microscopic fuses | never | — |
| **EPROM** | electrically (charging floating gates) | **UV light** through a quartz window — whole chip | all or nothing |
| **EEPROM** | electrically | **electrically**, in place | byte by byte |
| **Flash** | electrically | electrically | block by block |

Mask ROM cannot change its mind at all. PROM lets you *make up* your mind exactly once — programming literally blows fuses, as irreversible as it sounds. The leap is **EPROM** (Intel, 1971): Dov Frohman realised that a *defect* observed in transistors — charge getting stuck on a floating conductor — could be the storage mechanism itself, and the floating gate found its **first mass-produced home**, thirteen years before flash. EPROM chips carry a little quartz window: twenty minutes under an ultraviolet lamp gives the trapped electrons enough energy to jump off the islands, blanking the whole chip (working chips got a sticker over the window, so stray sunlight couldn't slowly erase the firmware). **EEPROM** replaced the UV lamp with electrical erase, byte-by-byte, in-circuit — no more unplugging the chip to update it. And **flash** is EEPROM's pragmatic descendant: give up byte-erase, erase in blocks, and in exchange pack the cells so densely that terabytes become cheap.

So the SSD in your laptop and the BIOS chip on its motherboard are the same invention at two scales — the floating gate, Frohman's tamed defect, holding both your files and the firmware that finds them.

## Optical — pits, lands, and a finer pen

![[secondary-storage-optical-ladder.svg|600]]

**The bit** lives on a single spiral track, wound from the centre of the disc outward like a vinyl groove in reverse — a track of microscopic **pits** pressed into the plastic, separated by flat **lands**. A laser follows the spiral; a photodiode watches the reflection. Over a land, the light bounces back cleanly; at a pit, the reflection dims (the pit's depth is chosen so light from pit and surrounding land interferes destructively).

**Reading** repeats the disk's beautiful idea: the bit is an **edge**, not a level. A **transition** — pit-edge, where the reflection changes — reads as **1**; a stretch of steady reflection (inside a pit *or* along a land) reads as **0**. Absolute brightness varies with dust, tilt, and disc quality; *changes* are self-referencing. Different medium, same wisdom: never trust a level when you can trust an edge.

**Writing** depends on the disc. Pressed discs (the ones movies ship on) are *moulded* — a metal stamper presses millions of pits in one squeeze, which is why mass production costs cents. Recordable discs (CD-R, DVD-R) have a **dye layer**: the writing laser, at high power, burns dark marks that imitate pits — permanent, write-once. Rewritable discs (RW) use a **phase-change alloy**: heated and cooled quickly it freezes amorphous (dull), heated gently it relaxes crystalline (shiny), so the same spot can be flipped back and forth.

**The capacity ladder is a wavelength ladder.** The disc never grew — the *pen* got finer. A pit can't usefully be smaller than the spot of light reading it, and the spot size is set by diffraction: roughly the laser's wavelength.

| Disc | Laser | Capacity (one layer) |
|---|---|---|
| CD (1982) | 780 nm infrared | 700 MB |
| DVD (1995) | 650 nm red | 4.7 GB |
| Blu-ray (2006) | 405 nm blue-violet | 25 GB |

Shrink the wavelength, shrink the pit, pack the spiral tighter — thirty-five times the data on the same 12 cm of plastic. The chip fabs run the identical bet in the other direction: lithography's leap from 193 nm deep-ultraviolet to 13.5 nm **extreme-ultraviolet** light is the same finer-pen move, for *writing* transistors instead of reading pits ([[How a Chip Is Made]]). Today optical is a niche (distribution, offline archives, air-gapped backups), but it is the only mainstream medium where the storage itself costs cents and survives electromagnetic disaster — nothing magnetic to scramble, nothing charged to leak.

## Reading is deciding — one problem, every medium

Line the technologies up and the pattern is impossible to unsee:

| Medium | The analog quantity | The trick that keeps the bit clean |
|---|---|---|
| DRAM ([[RAM and the Memory Hierarchy]]) | charge on a leaky capacitor | precharge to the midpoint; sense-amplify the nudge; refresh forever |
| Magnetic disk | magnetisation of a grain patch | read *transitions*, never levels — edges are self-referencing |
| Flash | electrons trapped on an island | fat threshold gaps; [[Gray Code\|Gray-coded]] levels so drift flips one bit; ECC |
| Optical | reflected laser intensity | again: transitions are 1s, steady stretches are 0s |

Every storage engineer, in every decade, on every physical substrate, has been solving the same problem: **analog in, bit out, survive the middle.** The middle — the decision boundary — is where a warm day, a worn oxide, or a dusty disc turns your data into someone's bad afternoon. And the danger of being caught *exactly on* the boundary has a name of its own: [[Clock Domains and Metastability|metastability]]. Digital data is not a property of matter. It is a **discipline imposed on matter** — and these are the enforcement mechanisms.

## Buffers — the shock absorber between speeds

A CPU works in nanoseconds; a disk answers in microseconds-to-milliseconds; a printer takes seconds per page. Every time two components of different speeds must pass data, a **buffer** — a waiting-area in memory — sits between them. The fast side drops data into the buffer and walks away; the slow side drains it at its own pace.

- **Printing:** the document lands in a print buffer in milliseconds; the CPU is free while the printer chews through it for minutes.
- **Streaming video:** the player keeps seconds of video buffered ahead, so a network hiccup drains the buffer instead of freezing the frame — the loading bar *is* the buffer filling.
- **Disk writes:** the OS batches writes in a RAM buffer and flushes them in bulk — why "safely eject" exists: pull the drive early and the buffer's unflushed tail never arrives.

One idea, everywhere: **decouple the producer from the consumer, and neither waits for the other's bad moments.** Knowing which couplings to break — and which tight couplings are exactly what you want — is a design art of its own: [[Decouple and Recouple]].

## Virtual memory — the disk drafted as fake RAM

When RAM runs out, the operating system quietly extends it onto secondary storage. Memory is managed in fixed-size **pages** (typically 4 KiB); when RAM is full, pages that haven't been touched recently are written out to a reserved disk area, and the RAM they occupied is reused. Touch an evicted page and the OS pulls it back in — evicting another to make room. The running program never knows: it sees one large, seamless memory.

**Why it's necessary:** without it, "RAM full" would mean crashed programs. With it, you can run programs larger than physical RAM, and more programs than fit at once.

**Why it's a stopgap:** the disk is thousands of times slower than RAM. A machine leaning hard on virtual memory spends its time shuttling pages instead of computing — that's the moment a laptop with 47 browser tabs starts *churning*, and the fix ("buy more RAM") suddenly makes sense: the machine wasn't slow, it was **paging**.

## Cloud storage — someone else's secondary storage

Strip away the marketing and **the cloud is a building full of disks** — physical servers and physical storage, owned by a provider, reached over the internet. "Uploading to the cloud" means copying your file to their HDDs and SSDs; every technology on this page, at warehouse scale.

| Advantages | Disadvantages |
|---|---|
| reachable from any device, anywhere with internet | **no internet, no files** |
| survives your house — off-site by construction | ongoing subscription vs one-time hardware cost |
| replicated across drives and sites — a dead disk is the provider's problem, invisibly fixed | you must *trust* the provider — privacy, security, breaches |
| capacity scales on demand — no hardware to buy or maintain | provider outage or shutdown locks you out at their timing, not yours |
| effortless sharing and collaboration | large transfers are limited by your internet speed, not by any disk |

The sysadmin's joke — *"there is no cloud, it's just someone else's computer"* — is both fair warning and slightly unfair: that someone runs redundant disk arrays ([[RAID]]), monitoring, and backups more professionally than any laptop owner. The honest summary: cloud storage trades **control** for **convenience and redundancy**. For most people's photos, that trade is excellent; for a hospital's patient records, the trust and legal questions are the whole story.

## Worked examples

**Example 1 — why an SSD feels 100× snappier.** A 7 200 rpm HDD needs an average seek of 9 ms. Estimate its average access time, and compare with an SSD at 60 µs.

*Tool: rotational latency — on average the platter must turn half a revolution before the sector arrives.*

One revolution takes $\dfrac{60}{7200} = 8.33$ ms, so the average rotational wait is half that: $4.17$ ms.

*Tool: access time = seek + rotational latency (the transfer itself is comparatively fast).*

$$t_{HDD} \approx 9 + 4.17 \approx 13\ \text{ms} \qquad t_{SSD} \approx 0.06\ \text{ms}$$

The ratio is about **220×** — and the reason is structural, not incremental: the SSD's 60 µs is pure electronics, while the HDD's 13 ms is *mechanical motion* — an arm swinging and a platter turning. No amount of engineering makes a motor compete with a wire. (Note what the comparison hides: for long *sequential* reads the gap narrows a lot, because once the head is in position a disk streams data quickly — the mechanical cost is per-*seek*, not per-byte.)

**Example 2 — justify the medium (exam style).** A wildlife photographer needs (a) storage in the camera, (b) a 40 TB archive of past shoots at the studio, (c) delivery of finished photos to clients abroad.

*Tool: score each candidate on the four axes — speed, cost per TB, durability/portability, permanence — and let the use-case pick the axis that matters.*

- **(a) In the camera → flash (SD card).** No moving parts survives being hauled up a mountain (durability); no power needed to retain (permanence in the field); small and removable (portability). An HDD's flying head would crash at the first knock.
- **(b) Studio archive → HDD.** 40 TB is a *cost-per-TB* problem, and magnetic storage wins that axis several times over; millisecond access is irrelevant for shoots opened twice a year.
- **(c) Delivery abroad → cloud storage.** The axis that matters is *reachability* — no physical medium crosses a border faster than an upload; the client needs no hardware, and the provider's replication protects the files in transit better than a posted USB stick.

The pattern to name in an exam answer: **no medium wins every axis** — every recommendation is "this axis dominates this use-case, and this medium wins that axis."

## Misconceptions

> [!warning] "Deleting a file erases it."
> Deleting normally removes the *file system's pointer* to the data — the blocks themselves keep their contents until something overwrites them, which is exactly why recovery tools work and why discarded drives are a security problem. (On SSDs the story has a twist: the TRIM command lets the controller genuinely clear deleted blocks in the background — for wear-levelling reasons, not privacy ones.) Truly erasing a drive is a deliberate act: overwrite it, or destroy it.

> [!warning] "Storage lasts forever — it's non-volatile!"
> Non-volatile means *survives power-off*, not *survives time*. Recordable-DVD dye fades in years-to-decades ("disc rot"); a worn flash cell's electrons leak off the floating gate within a few unpowered years; even magnetisation weakens as thermal jostling flips grains. Storage is a **lease, not a purchase** — real archives survive by *active copying* onto fresh media, not by trusting any one object. The 2,000-year-old texts we still read survived the same way: recopied, not preserved.

> [!warning] "Defragment your drives regularly."
> On an HDD, defragmenting genuinely helps: it gathers each file's blocks into contiguous runs, so the head seeks less. On an SSD it is *worse than useless* — there is no head and no seek penalty to remove, so it gains nothing, and the mass rewriting burns the very program/erase cycles the drive's life is counted in. A habit from one technology, harmful on its successor.
>
> And the CD completes the picture, because it does the opposite on purpose: consecutive audio samples are **deliberately scattered** far apart along the spiral (*interleaving*), so that a scratch — one long continuous wound on the disc — lands as a few small, widely separated errors in the data stream, exactly the damage its [[Error Detection and Correction|error-correcting code]] can repair. A CD ships permanently "fragmented", and there is no defragmenter for it because the fragmentation *is* the protection. Three media, three verdicts on the same phenomenon, each decided by what that medium fears: the HDD fears the seek, the SSD fears the rewrite, the disc fears the scratch. ([[Stories/A Fight With the Inevitable Errors]] tells how that trick was designed in.)

> [!warning] "An SSD is just a big USB stick."
> Same flash cells, different machine around them. An SSD adds a serious controller, a RAM cache, many flash chips written in parallel, and aggressive wear levelling; a cheap USB stick has one slow chip and a minimal controller. That's why the same "flash memory" spans 50 MB/s sticks and 7 000 MB/s drives. And the *shape* has stopped being a guide in either direction: there are now stick-shaped external drives with full SSD controllers inside, and a camera's **CFexpress card is literally an NVMe SSD in a card shell** — same PCIe lanes, same protocol as a laptop's drive (which is why it sustains the multi-gigabit video an SD card's slower bus cannot). Judge the machine — controller, channels, interface — never the costume.

> [!warning] "My computer is slow — the disk must be full." (Half wrong, interestingly.)
> Usually this confuses storage with [[RAM and the Memory Hierarchy|RAM]] — deleting photos does not create more workbench. But there is a real effect hiding here: a *nearly full SSD* does slow down, because wear levelling and block-erase need spare blocks to shuffle data through, and a full drive leaves the controller shuffling in a phone booth. The factory already reserves a hidden slice for exactly this (**over-provisioning** — the wear section above); the free space you leave simply extends that workshop. Keep ~10% free and the effect vanishes.

> [!info] Beyond syllabus — the storage frontier
> - **Reading by prediction.** A modern disk head's waveform is so smeared that bits overlap their neighbours. The controller stopped trying to decide each bit alone in the 1990s: **PRML** (partial-response maximum-likelihood) decoding considers the *whole sequence* and asks "which bit-string most likely produced this mess?" — the Viterbi algorithm. The disk reads the way a language model predicts: from context ([[Compression]] — compression *is* prediction, and so, it turns out, is reading).
> - **Shingled recording (SMR) — and a small scandal.** A disk's write head is wider than its read head, so tracks can be overlapped like roof shingles: each new track partially covers the last, and the narrow read head still finds the exposed strip. Capacity rises ~20% — but rewriting *one* track now means rewriting the whole shingle band, so random writes crawl. Fine for archives; wrong for a NAS rebuilding an array. Which is why it blew up in 2020, when drive makers quietly slipped SMR into NAS-branded lines, unlabelled and at conventional-drive (CMR) prices, until benchmarks and a class-action lawsuit dragged it into the spec sheets. The buyer's lesson: *CMR vs SMR is now a checkbox you read before you pay.*
> - **Heat-assisted recording (HAMR).** To pack magnetic patches tighter they must be made of sturdier material — too sturdy for the write head to flip cold. Solution: a **laser on the write head** briefly heats the patch to soften it magnetically, the electromagnet flips it, it cools back to stubborn. Optical and magnetic storage, married on one head.
> - **3D NAND.** Flash stopped shrinking sideways and went *up* — cells stacked in towers, currently 200+ layers, which is how a fingernail of silicon holds a terabyte.
> - **Tape.** The oldest medium is still the cold-archive king: an LTO-9 cartridge holds 18 TB for pennies per TB, and robotic tape libraries hold the deep archives of the internet. Sequential-only — the medium equivalent of "you may read the scroll, but only by unrolling it."
> - **DNA storage.** The far shore: an exabyte per cubic millimetre and stable for millennia, at speeds that make tape look frantic. The hierarchy's bottom layer may one day be biological.

## Exam Notes

### Cambridge 0478 (IGCSE) — §3.3 Data storage

This section is examined in full, and the six learning objectives map directly onto sections here:

- **Primary vs secondary (3.3.1–2):** primary = directly accessed by the CPU (RAM + ROM); secondary = not directly accessed, needed for permanent storage. Give both halves — *access* and *permanence* — for full marks.
- **Operation of the three media (3.3.3):** the syllabus wants named mechanisms and examples. Magnetic: *platters, tracks, sectors, electromagnets* — HDD. Optical: *lasers, pits, lands* — CD/DVD/Blu-ray. Solid-state: *NAND/NOR, control gates and floating gates* — SSD, SD card, USB drive. The floating-gate vocabulary is explicitly on the syllabus — "electrons trapped on the floating gate; the control gate reads whether the transistor still switches" is exam-ready mechanism language.
- **Virtual memory (3.3.4):** define it as secondary storage used as an extension of RAM; the mechanism sentence the mark scheme wants is "**pages** of data are transferred between RAM and virtual memory when needed"; the *why* is running programs/data larger than physical RAM.
- **Cloud (3.3.5–6):** know that the cloud is **physical servers and storage** accessed remotely, and give advantages/disadvantages *in comparison to local storage* — answers that never mention the local alternative lose the comparison marks.

### Cambridge 9618 (AS Level) — §3.1 Computers and their components

- "Show understanding of the need for input, output, primary memory and **secondary (including removable) storage**" — the primary/secondary table plus the removable examples covers this bullet.
- "Describe the **principal operations** of hardware devices" — of the named device list, this page delivers *magnetic hard disk, solid-state (flash) memory, and optical disc reader/writer*. Answer in mechanism language: flux reversals and heads for magnetic; floating gates and threshold voltages for flash; pits, lands, and laser reflection for optical.
- "Explain the difference between **PROM, EPROM and EEPROM**" — the ROM-family table is this LO verbatim: fuses/once/never; floating gates/UV-erase/whole-chip; electrical-erase/byte-by-byte. A classic 3-mark question is one distinguishing sentence per generation.
- "Show understanding of the use of **buffers**" — definition plus one concrete use (printing or streaming) with the *speed-mismatch* reason stated.
- 9618 loves **justify-the-choice** questions (as in the photographer example): name the axis that dominates the scenario, then match the medium that wins that axis.

### IB Computer Science — A1.1 Computer hardware and operation

Secondary storage, the memory/storage distinction, and device trade-offs sit inside A1.1 (computer fundamentals). The comparison tables (primary vs secondary; HDD vs SSD; cloud vs local) are the working vocabulary for A1.1 discussion questions; virtual memory and buffers reappear in A1.3's operating-systems material as *resource management* examples.

### AP Computer Science A

Not examined — AP CSA is a programming course; storage hardware is out of scope.

## Connections

- **Parent:** [[RAM and the Memory Hierarchy]] — this page is the bottom of that card's pyramid: the layers below DRAM, where speed is traded for permanence and price. Its sense-amplifier read is the first instance of the decision-boundary theme here.
- **Uses:** [[Gray Code]] — MLC/TLC/QLC charge levels are Gray-ordered so one level of drift corrupts one bit; the rotary-encoder argument, verbatim, inside a flash cell. [[Storage Units (Vocab)]] — the KiB/MiB/GiB ladder these capacities are measured in.
- **Same danger, different card:** [[Clock Domains and Metastability]] — what happens when a signal is caught *on* the decision boundary; storage engineering is the art of never being there.
- **Extensions:** [[Operating Systems]] — paging, segmentation, page replacement, thrashing (the A-Level §16.1 machinery behind the sketch here); [[File Systems]] — how blocks become named files and folders; [[Error Detection and Correction]] — the codes that mop up what the physics lets slip; [[RAID]] — many cheap disks pretending to be one fast, reliable disk (striping, mirroring, XOR parity — and why RAID is *not* a backup); [[How a Chip Is Made]] — how floating gates are actually fabricated.
- **Application:** [[Compression]] — fitting more into the same blocks; and its compression-is-prediction thesis is literally how a PRML disk head reads.
- **Story:** [[Stories/The Blue LED]] — the wavelength ladder's finest pen, the 405 nm violet laser, is Nakamura's: the man who made blue light exist, and was paid two envelopes of ¥10,000 for the patent.
- **Physics bridge:** [[Capacitors]] — DRAM's cell is a capacitor built to be fast and leaky; the floating gate is a capacitor built to never discharge. Same physics, opposite design goals. [[Quantum Tunnelling]] — the wall-crossing that writes every flash cell (and powers alpha decay, the STM, and the sun).
- **Meta bridge:** [[Decouple and Recouple]] — the buffer is the canonical decoupler; engineering is choosing which couplings to break and which to keep.

## Glossary

| term | 中文 | one-liner |
|---|---|---|
| flux reversal | 磁通反转 | a change in magnetisation direction — the readable event on a disk |
| seek time | 寻道时间 | time for the arm to reach the right track |
| rotational latency | 旋转延迟 | wait for the sector to spin under the head (avg = half a revolution) |
| threshold voltage | 阈值电压 | control-gate voltage at which the transistor switches — shifted by stored charge |
| program/erase cycle | 编程/擦除周期 | one write-then-erase round trip; flash's unit of wear |
| head crash | 磁头碰撞 | the flying head touching the platter — mechanical data loss |
| page (memory) | 页 | fixed-size block the OS moves between RAM and disk |
| phase-change alloy | 相变合金 | RW-disc material flipped between shiny crystalline and dull amorphous |

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $t_{HDD}$ | `t_{HDD}` | subscripted access time |
| $\dfrac{60}{7200}$ | `\dfrac{60}{7200}` | display-size fraction in prose |

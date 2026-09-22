---
chinese: 芯片是怎么造出来的 (xīnpiàn shì zěnme zào chūlái de)
prerequisites:
  - "[[The Transistor as a Switch — How Analog Becomes Digital]]"
  - "[[Logic Gates]]"
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Secondary Storage]]"
  - "[[Capacitors]]"
leads_to: []
tags:
  - subject/cs
  - subject/physics
  - domain/hardware
  - domain/electronics
  - level/A-Level
  - level/IB-HL
  - level/university
  - curriculum/Cambridge-9618
  - curriculum/Cambridge-0478
  - curriculum/IB-CS
  - type/theory
  - type/hands-on
  - type/visual-tool
  - notation/process-node
  - misconception/the-node-name-is-a-length
  - misconception/chips-are-assembled
  - misconception/smaller-is-cheaper
  - misconception/yield-is-a-quality-problem
  - misconception/moores-law-is-a-law
---

# How a Chip Is Made 芯片是怎么造出来的

> Nobody assembles a chip. Nobody places its transistors, one by one or a thousand at a time. Every one of the fifty-seven billion switches in the processor this card was written on was printed, all at once, by shining light through a stencil, and so was every wire joining them. The factory that does it costs more than an aircraft carrier and its cleanest room has less dust than the space between the planets. This card is what happens between a bucket of sand and that.

## What this is for

[[The Transistor as a Switch — How Analog Becomes Digital]] explains the switch; [[Logic Gates]] and [[The Boolean-to-Silicon Bridge]] explain what switches are wired into and how the idea was found; [[RAM and the Memory Hierarchy]] and [[Secondary Storage]] describe the cells that hold bits. None of them says how the physical objects are made, and the making is where the numbers a student meets, "5 nanometre", "two years per doubling", "three hundred dollars for a GPU die", actually come from. This card follows one wafer from silicon to sale: the planar process, lithography and its light, the transistor built layer by layer, the memory cells built the same way, and the arithmetic of yield that decides what a chip costs and why the industry looks the way it does.

## Definition

### Formal

An **integrated circuit** is a set of transistors, resistors, capacitors and wires fabricated together on one piece of semiconductor by the **planar process**: a repeated cycle in which a thin film is deposited or grown on a flat **wafer**, coated with **photoresist**, patterned by **photolithography** (light projected through a **mask**), and then selectively **etched**, **doped** by ion implantation, or covered with metal where the resist has been removed. A modern logic process applies the cycle roughly eighty times, aligned to within a few nanometres, to build the transistors first and then a dozen or more layers of wiring above them. The wafer is then cut into **dies**, each tested, and the working ones packaged. The fraction that work is the **yield**, and it falls exponentially with die area.

### Intuitive

Think of a stencil and a can of spray paint. Lay the stencil on the wall, spray, lift it off, and the pattern is there; put a different stencil on top and spray a second colour, and the two patterns sit together in perfect register. A chip is made that way, about eighty stencils deep, on a disc of silicon polished flatter than any mirror. Each layer: coat the wafer with a light-sensitive varnish, project the pattern of a postcard-sized stencil onto a spot the size of a stamp, wash away the exposed varnish, and etch, dope or plate whatever is bare before stripping the varnish and coating again. Eighty times, in register to a few nanometres, and the patterns stack into billions of switches and their wiring. Everything else in the story, the ultraviolet light, the clean rooms, the twenty-billion-dollar factory, follows from one fact: the stencil is the only way anyone knows to make ten billion identical things at once.

### 中文锚点 (Chinese Anchor)

想一想镂空模板和一罐喷漆。把模板贴在墙上，一喷，揭下来，图案就留在墙上了；换一张模板贴上去再喷一种颜色，两层图案就严丝合缝地叠在一起。芯片就是这样做出来的，大约要叠八十层模板。这面"墙"是一片圆盘形的硅晶圆，磨得比任何镜子都平。每一层，先涂上一层感光的"清漆"，再把一张明信片大小的模板上的图案，用光缩小投到邮票大小的一块地方，被光照过的清漆洗掉，露出来的地方就去腐蚀，或者掺进杂质，或者镀上金属，然后把清漆全部剥掉，涂下一层。这样做八十遍，每一遍都对准到几个纳米以内，这些图案就叠成了几十亿个开关，以及它们之间的连线。这个故事里其余的一切，紫外光、无尘车间、两百亿美元的工厂，都是从一件事推出来的：模板，是人类知道的唯一一种能一次做出一百亿个一模一样的东西的办法。

## Notation

| Term | Meaning | Notes |
|---|---|---|
| wafer | the silicon disc, 300 mm across and 0.775 mm thick, on which chips are made | a single crystal; several hundred dies per wafer |
| die | one chip's rectangle on the wafer | 100 mm² for a phone, 600 mm² for a GPU; the lens limit is 858 mm² |
| mask (reticle) | the stencil: a quartz plate carrying one layer's pattern at 4× size | a set of 80 masks for one product costs millions |
| photoresist | the light-sensitive coating; exposed regions dissolve (positive resist) | its chemistry sets how fine a line can be printed |
| critical dimension, CD | the smallest feature a step can print | $\text{CD} \approx k_1 \lambda / \text{NA}$ |
| $\lambda$, NA, $k_1$ | wavelength of the light, numerical aperture of the lens, a process factor | $k_1$ cannot go much below $0.28$ in one exposure |
| node ("5 nm") | a generation's marketing name | no longer the length of anything on the chip |
| yield $Y$ | fraction of dies that work | $Y \approx e^{-DA}$ for defect density $D$ and area $A$ |
| CMOS | complementary MOS: n- and p-type transistors in pairs | the process that everything digital is built in |

> [!warning] Notation trap
> "5 nm" names a generation, not a feature. The gate length of a "5 nm" transistor is about $20$ nm and the closest wires are about $30$ nm apart; the name continues a series that was once honest (a "90 nm" process in 2004 did have 90 nm gates) and became a label around 2010. Compare densities, in transistors per square millimetre, not names.

## Part I — From sand to a mirror

Silicon is the second commonest element in the Earth's crust, and the process begins by making it purer than anything else humans manufacture. Quartz is reduced to metallurgical silicon in an arc furnace, converted to a gas, distilled, and re-deposited as polysilicon with fewer than one foreign atom in $10^{9}$. A seed crystal is dipped into a crucible of the molten polysilicon and drawn upward, turning, over a day or two; the silicon freezes onto the seed in its crystal pattern, and a single crystal two metres long and thirty centimetres across emerges (the **Czochralski** method, 1916, for a different purpose). It is sawn into wafers, ground, and polished until the surface deviates from flat by less than a nanometre over a centimetre: flatter, proportionally, than a mirror, because a lens with a depth of focus of a hundred nanometres is about to be pointed at it.

## Part II — One layer of the planar process

The idea that made integrated circuits possible was Jean Hoerni's at Fairchild in 1959: build the transistor *into* a flat surface instead of on top of it, protected by a layer of its own oxide, so that every step can be done to the whole wafer at once through a stencil. [[The Boolean-to-Silicon Bridge]] tells how Kilby and Noyce arrived at the circuit; the planar process is how it became manufacturable, and it is still the process.

![[chip-fabrication-lithography.mp4]]

One turn of the cycle, as the clip shows:

1. **Grow or deposit a film.** Heat the wafer in oxygen and its surface becomes silicon dioxide, glass, an insulator of superb quality; or deposit a film from a gas (chemical vapour deposition), or one atomic layer at a time (atomic layer deposition), which is how a gate insulator one nanometre thick is laid down evenly across a wafer.
2. **Coat.** Spin the wafer at thousands of revolutions per minute with a drop of photoresist on it; the drop spreads to a film a few hundred nanometres thick.
3. **Expose.** Project ultraviolet light through the mask, reduced four times by the lens, onto one die-sized field; step to the next field and repeat, a hundred times per wafer (the machine is a **stepper**, or a **scanner** when the field is swept). The light changes the chemistry of the resist where it lands.
4. **Develop.** Wash the wafer; the exposed resist dissolves and windows open.
5. **Etch.** A plasma of reactive ions eats the film wherever it is bare, straight down, leaving vertical walls; the resist protects everything else.
6. **Implant.** Accelerate dopant ions, boron for p-type or phosphorus and arsenic for n-type, at tens of kilovolts into the wafer; they enter only through the windows and stop a few tens of nanometres in. A short anneal heals the crystal and puts the dopants on lattice sites, which is what makes them donors or acceptors, as [[The Transistor as a Switch — How Analog Becomes Digital]] explains.
7. **Strip** the resist, planarise the surface (chemical–mechanical polishing: a slurry and a pad grind the wafer flat again), and go back to step 1 with the next mask.

Each mask must land on the last one's pattern to within an **overlay** of a couple of nanometres, across a 300 mm wafer, at thousands of wafers a day. The alignment marks and the metrology that read them are a quarter of the machine.

## Part III — The light

How small a line can be printed is set by the wave nature of light and nothing else. A lens of numerical aperture $\text{NA}$ using light of wavelength $\lambda$ resolves a half-pitch of about

$$\text{CD} = k_1 \frac{\lambda}{\text{NA}},$$

Rayleigh's criterion from [[Diffraction]] with a process factor $k_1$ that clever resist chemistry and mask tricks push down to about $0.28$ and no further in a single exposure. `chip-fabrication-model.py` evaluates it:

| tool | $\lambda$ | NA | $k_1$ | CD |
|---|---|---|---|---|
| mercury i-line, 1990s | 365 nm | 0.6 | 0.6 | 365 nm |
| argon-fluoride laser, "dry" | 193 nm | 0.93 | 0.35 | 73 nm |
| argon-fluoride with water between lens and wafer ("immersion") | 193 nm | 1.35 | 0.28 | 40 nm |
| extreme ultraviolet (EUV) | 13.5 nm | 0.33 | 0.35 | 14 nm |
| high-NA EUV, 2025 | 13.5 nm | 0.55 | 0.35 | 9 nm |

Three things in that table are remarkable. The industry ran the 193 nm laser for twenty years past the point where its lines were smaller than its wavelength, first by putting water under the lens ($n = 1.44$, so the NA can exceed 1), then by **multiple patterning**: printing one layer as two or four interleaved exposures, each within the limit, at the cost of doubling the masks and the steps. The jump to 13.5 nm took two decades and a machine unlike anything before it: there is no lens for that wavelength, since every material absorbs it, so the light is reflected by mirrors coated with forty alternating layers of molybdenum and silicon, each a few nanometres thick; and there is no lamp for it, so the light is made by hitting fifty thousand droplets of molten tin a second with a carbon-dioxide laser, each droplet flashing into a plasma that emits at 13.5 nm for a few nanoseconds. The machine weighs about 180 tonnes, costs about \$180 million, and one company in the Netherlands, ASML, makes every one of them. The third remarkable thing is the numbers in the last column: a modern chip's finest features are printed with light that, at 13.5 nm, is itself a hundred times shorter than the ultraviolet your skin burns in.

## Part IV — The transistor, built

![[chip-fabrication-cross-section.svg|1000]]

Read the cross-section from the bottom. The wafer is lightly p-type. A first set of masks defines **wells**, regions implanted n-type, where the p-channel transistors will live. Then the **gate**: a gate oxide a nanometre thick, grown or deposited, and on it the gate electrode, once polysilicon and now a metal stack, patterned by the finest lithography on the chip because the gate length is the transistor's most important dimension. The gate is made *before* the source and drain, so that when the source and drain are implanted the gate itself shadows the channel and the two are perfectly aligned to it (the **self-aligned gate**, 1968, which is why every transistor on a chip has the same channel length to a nanometre). Contacts, tungsten plugs through the insulator, reach down to the source, drain and gate, and then the wiring begins: copper lines laid in trenches etched into the insulator (the **damascene** process, named for the inlaid metalwork of Damascus), fifteen layers of them, the lowest as fine as the transistors and the top ones coarse enough to carry power. Two transistors of opposite type wired as in the figure are an inverter; four are a NAND; and [[Logic Gates]] takes it from there.

**Three generations of the same transistor.** Until 2011 the channel was a flat strip under the gate (**planar**). As gates shortened below about 30 nm the gate lost control of the channel, current leaked, and the fix was to stand the channel up as a thin fin with the gate wrapped around three sides (**FinFET**, introduced at 22 nm). Below about 5 nm even that was not enough, and the channel became a stack of horizontal nanosheets with the gate surrounding each on all four sides (**gate-all-around**, from 2022). The transistor's physics did not change; the geometry was rearranged so that the gate's field, the subject of the transistor card, could keep the channel in its grip.

**Two memory cells, the same way.** A DRAM cell is one transistor and one capacitor, and the capacitor is the problem: [[Capacitors]] shows that capacitance needs area, and a cell has almost none. So the capacitor is made *vertical*: a hole etched a micron deep and a few tens of nanometres wide, its walls lined with insulator and metal, a cylinder standing above each transistor with fifty times the area of its footprint. That is a **stacked capacitor**; the earlier trick of drilling it down into the wafer was the **trench**. A flash cell is a transistor with a second, insulated gate between the control gate and the channel, the **floating gate** of [[Secondary Storage]], charged by forcing electrons through the oxide; modern **3D NAND** turns the whole memory on its side and etches a hole through a stack of two hundred alternating layers at once, so that one lithography step defines two hundred cells. Different devices, the same cycle of coat, expose, etch.

## Part V — The arithmetic of yield

Nothing is perfect. A particle of dust, a flaw in a mask, a bubble in the resist, and the transistor under it is dead, and a chip with one dead transistor is usually a dead chip. If defects land at random with density $D$ per square centimetre, the chance that a die of area $A$ has none is the Poisson probability

$$Y = e^{-DA},$$

which [[Poisson Distribution]] derives and which decides the shape of the industry.

![[chip-fabrication-yield.svg|1000]]

At a mature $D = 0.1$ per cm², a 100 mm² phone chip yields $90\,\%$ and a 600 mm² GPU die yields $55\,\%$. Add the geometry, that a 300 mm wafer holds about 613 of the first and 86 of the second, and a wafer that costs \$17 000 to process gives a phone chip for \$31 and a GPU die for \$360. The cost of a chip rises faster than its area, which is why:

- **Chiplets.** One 800 mm² die at $D = 0.1$ yields $45\,\%$: 27 good chips per wafer. Four 200 mm² chiplets yield $82\,\%$ each: 240 good chiplets, or 60 four-chiplet products, from the same silicon. Splitting a design and joining the pieces in the package, as AMD and Apple do, more than doubles the useful output.
- **Binning.** A die with one dead core out of eight is sold as a six-core part. The same wafer yields the top model and the budget one, and the price difference is the defect density.
- **Ramp.** A new process starts at $D = 0.5$ or worse and improves for years; that is why the first chips on a node are small and expensive and why a fab's profit is a function of time.

## Part VI — Fifty years of the same trick

![[chip-fabrication-density.svg|900]]

The Intel 4004 of 1971 had 2 250 transistors on 12 mm². The M1 Max of 2021 has 57 billion on 432 mm²: twenty-five million times as many, a doubling every twenty-four months for fifty years, which is what Gordon Moore predicted in 1965 from four data points. It was never a law of nature; it was an observation that became a schedule, and the schedule was met by the process above getting finer, one wavelength and one geometry at a time. The chips did not get faster at the same rate after 2005, when the power a shrinking transistor dissipated stopped shrinking with it (the end of Dennard scaling, which [[Pipelining and Simultaneous Multithreading]] describes), and the density line above has bent since 2020 as the cost per transistor stopped falling. The stencil still works; it is the economics that has changed.

## Where this is the working tool

**Everything with a processor in it.** Every phone, car, card and appliance contains dies from this process, and the supply chain that makes them, sand to wafer in one country, wafer to chips in another, chips to boards in a third, is the most concentrated in the world: one company makes the EUV machines, and one foundry in Taiwan makes most of the leading-edge logic. The 2021 shortage that idled car factories was a queue for capacity at a handful of fabs.

**Sensors, LEDs and solar cells** are made by the same cycle on different materials: image sensors are CMOS chips with a photodiode per pixel; [[The Blue LED]] is gallium nitride grown and doped by the same kind of deposition; a solar panel is a very large, very simple diode.

**The cost of a design mistake.** A mask set for a leading process costs millions and a wafer takes three months, so a chip that comes back with a bug costs a quarter of a year and a fortune to fix. That is why chip design is verified in simulation to a degree software rarely is, and why hardware bugs that reach the public ([[Pipelining and Simultaneous Multithreading]]'s Spectre) are patched in software instead.

**Hands-on.** `chip-fabrication-model.py` computes the printable feature size for any wavelength and lens, dies per wafer for any die, the yield for any defect density, the cost per good die, and the chiplet comparison; every number in this card is in its output. Change $D$ to $0.3$, the value of a young process, and watch the GPU die's price triple while the phone chip's barely moves.

## Worked examples

### Example 1: how fine a line

*An immersion scanner uses 193 nm light with NA $1.35$ at $k_1 = 0.28$. What half-pitch can it print in one exposure, and what does printing a 20 nm half-pitch with it require?*

**Trigger:** "how fine" with a wavelength and an aperture is Rayleigh's criterion. **Tool: $\text{CD} = k_1 \lambda / \text{NA}$.**

$\text{CD} = 0.28 \times 193 / 1.35 = 40$ nm. A 20 nm half-pitch needs two interleaved exposures each at 40 nm, offset by 20 nm: double patterning, with two masks and two etches, and an overlay between them of a few nanometres. That doubling of steps for every critical layer is the cost EUV was built to remove.

### Example 2: yield from defect density

*A 150 mm² die is made on a process with $D = 0.1$ per cm². What fraction of dies work? What if the die is redesigned at 300 mm²?*

**Trigger:** a random defect count over an area is a Poisson process; "none" is the zero term. **Tool: $Y = e^{-DA}$ with $A$ in cm².**

$Y = e^{-0.1 \times 1.5} = 0.861$; at 300 mm², $e^{-0.3} = 0.741$. Doubling the area loses a further $12$ percentage points of yield and, since a wafer also holds half as many dies, more than doubles the cost per good die.

### Example 3: dies per wafer and cost

*How many 100 mm² dies fit on a 300 mm wafer with a 3 mm edge exclusion, and what does each good one cost at a wafer cost of \$17 000 and $Y = 0.905$?*

**Trigger:** area of a disc over area of a die, minus the partial dies along the edge. **Tool: the area ratio, corrected by the edge term $\pi d / \sqrt{2A}$**, the de Vries estimate the script uses.

Usable radius $147$ mm: $\pi \times 147^2 / 100 = 679$, minus $\pi \times 294 / \sqrt{200} = 65$, gives $613$ dies. Good dies $613 \times 0.905 = 555$; cost per good die $17\,000 / 555 = \$31$.

### Example 4: chiplets against a monolithic die

*Compare one 800 mm² die with four 200 mm² chiplets at $D = 0.1$ per cm².*

**Trigger:** the same silicon, two ways of cutting it; the comparison is good products per wafer. **Tools: dies per wafer and $Y = e^{-DA}$, for each size.**

Monolithic: $61$ dies at $Y = e^{-0.8} = 0.45$: $27$ good chips. Chiplets: $293$ dies at $Y = e^{-0.2} = 0.82$: $240$ good chiplets, $60$ products of four. Before the cost of joining them, the chiplet design gives $2.2$ times as many products from the same wafer, and the joining, a silicon bridge or an interposer, is cheaper than the silicon it saves.

### Example 5: the doubling time

*The 4004 had $2\,250$ transistors in 1971; the M1 Max had $57 \times 10^9$ in 2021. What doubling time does that imply?*

**Trigger:** a ratio over a time is an exponential growth rate. **Tool: doublings $= \log_2(\text{ratio})$**, from [[Exponential Growth and Decay]].

$\log_2(57 \times 10^9 / 2\,250) = \log_2(2.53 \times 10^7) = 24.6$ doublings in $50$ years, or one every $24$ months. Moore's 1965 paper said one a year; his 1975 revision said two years; the fifty-year average is the revision.

## Common Misconceptions (Teaching Notes)

### 1. "A 5 nm chip has 5 nm transistors"

The gate is about 20 nm and the finest wires about 30 nm apart. Node names stopped being lengths around 2010 and now count generations. The honest measure is transistors per square millimetre, and Part VI's figure is drawn in it.

### 2. "Chips are assembled from parts"

Nothing on a die is placed. Every transistor and wire is printed, in the same exposure as billions of others; the only assembly is at the end, when a die is soldered into its package. That is why a chip with ten billion transistors costs \$30 and one with ten costs about the same.

### 3. "Smaller transistors mean cheaper chips"

They did, for fifty years, because a shrink put more chips on the same wafer. Since about 2020 the cost per wafer has risen faster than the density, because the lithography needed to print smaller features (EUV, multiple patterning) costs more per layer than it saves. Smaller now buys speed and power, not always price.

### 4. "Yield is a quality-control problem"

Yield is physics: defects are random, and a die is a lottery ticket whose odds fall exponentially with its area. No inspection improves it; only a cleaner process, a smaller die, or a design that tolerates dead parts (binning, chiplets, spare rows in a memory) does.

### 5. "Moore's law is a law"

It was an observation in 1965 and a schedule from 1975. The industry met it by choosing to, at enormous expense, and its bending since 2020 is not a failure of nature. The stencil still prints; the money has changed.

## Exam Notes

### Cambridge 0478 (IGCSE), §3.1 and §3.2

Point 1(b) asks candidates to "understand what is meant by a microprocessor", with the guidance that "a microprocessor is a type of integrated circuit on a single chip"; Part II is what that sentence means. In §3.2 on storage the syllabus states that solid-state memory "uses NAND or NOR technology" and that "transistors are used as control gates and floating gates", which Part IV's flash paragraph and [[Secondary Storage]] carry. Nothing about fabrication is examined.

### Cambridge 9618 (A Level)

No row of §3, §4 or §15 examines how integrated circuits are made; the syllabus's hardware sections describe components and their behaviour. The cross-section in Part IV is the physical form of the CMOS gates that §15.2's logic circuits assume, and the transistor card carries the §15.2 bridge.

### IB Computer Science (2027 guide)

A4.1.2 asks for "hardware requirements for various scenarios where machine learning is deployed", naming ASICs, FPGAs, GPUs and TPUs as advanced infrastructure. An ASIC is a chip made by this process for one purpose, and Part V's yield arithmetic is why a custom chip only pays at volume. Fabrication itself is not in the guide.

### Where this is *not* examined

Everything in this card past those three sentences: no board examines lithography, yield, doping or the planar process. It is enrichment, written because "chip" is the most common noun in the subject that no card had explained, and because the arithmetic of Part V is the kind a student can check.

## Beyond the syllabus

> [!info] Why the wafer is 300 mm and not 450
> Recall that dies per wafer grow with the wafer's area while the edge loss grows with its circumference, so a larger wafer gives more chips per process step. The industry moved from 200 mm to 300 mm around 2001 and planned 450 mm for the 2010s; every tool would have had to be redesigned, the wafers cost more to grow, and the gain was smaller than a lithography generation. The move was abandoned in 2017, and 300 mm is likely the last size.

> [!info] Strain, high-k and the tricks under the transistor
> Recall that the gate oxide is about a nanometre thick. At that thickness electrons tunnel through silicon dioxide ([[Quantum Tunnelling]]), so since 2007 the insulator has been hafnium oxide, which insulates as well at three times the thickness, with a metal gate above it. The channel silicon is also *strained*, stretched by a few tenths of a percent using silicon-germanium regions beside it, because stretched silicon carries electrons faster. Neither changes the process; both are extra masks.

## Connections

- **Built on:** [[The Transistor as a Switch — How Analog Becomes Digital]] (the device the cycle builds), [[Logic Gates]] (what two transistors of opposite type make), [[RAM and the Memory Hierarchy]] and [[Secondary Storage]] (the DRAM and flash cells of Part IV), [[Capacitors]] (why the DRAM capacitor stands up).
- **Tools used:** [[Diffraction]] (Rayleigh's criterion sets the line width), [[Poisson Distribution]] (yield as the zero-defect probability), [[Exponential Growth and Decay]] (the doubling time), [[Quantum Tunnelling]] (why the gate oxide changed material).
- **Beside:** [[Pipelining and Simultaneous Multithreading]] (Dennard scaling and the multicore turn), [[The Modern CPU vs the Textbook Model]] (what the transistor budget is spent on), [[The GPU — From Triangles to Tensors]] (the biggest dies, and why they are chiplets now).
- **Stories:** [[The Boolean-to-Silicon Bridge]] (Kilby, Noyce and the first integrated circuit), [[The Blue LED]] (the same deposition and doping on a harder crystal).

## Sources

- Hoerni, J. A. (1960). Planar silicon transistors and diodes. *IRE Electron Devices Meeting*; U.S. Patent 3,025,589. The planar process.
- Moore, G. E. (1965). Cramming more components onto integrated circuits. *Electronics*, 38(8), 114–117; and Moore, G. E. (1975). Progress in digital integrated electronics. *IEDM Technical Digest*, 11–13. The prediction and its revision to two years.
- Kerwin, R. E., Klein, D. L., & Sarace, J. C. (1969). Method for making MIS structures. U.S. Patent 3,475,234. The self-aligned gate.
- Murphy, B. T. (1964). Cost-size optima of monolithic integrated circuits. *Proceedings of the IEEE*, 52, 1537–1545. Yield against area; the Poisson form used here is the simplest of the models he compared.
- de Vries, D. K. (2005). Investigation of gross die per wafer formulas. *IEEE Transactions on Semiconductor Manufacturing*, 18, 136–139. The dies-per-wafer estimate.
- Mack, C. A. (2007). *Fundamental Principles of Optical Lithography*. Wiley. Rayleigh's criterion with $k_1$, immersion, and multiple patterning.
- Bakshi, V. (Ed.) (2018). *EUV Lithography* (2nd ed.). SPIE Press. The tin-droplet source and multilayer mirrors; the scanner's mass and price are ASML's public figures.
- Hisamoto, D., et al. (2000). FinFET: a self-aligned double-gate MOSFET scalable to 20 nm. *IEEE Transactions on Electron Devices*, 47, 2320–2325.
- Transistor counts and die areas are the manufacturers' published figures (Intel, Apple), as tabulated in `chip-fabrication-model.py`; the \$17 000 wafer cost is a widely reported 2023 estimate for a 5 nm-class process and is used only as a scale.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\text{CD} = k_1 \dfrac{\lambda}{\text{NA}}$ | `\text{CD} = k_1 \dfrac{\lambda}{\text{NA}}` | Smallest printable half-pitch |
| $Y = e^{-DA}$ | `Y = e^{-DA}` | Yield: the Poisson probability of zero defects |
| $N \approx \dfrac{\pi r^2}{A} - \dfrac{2\pi r}{\sqrt{2A}}$ | `N \approx \dfrac{\pi r^2}{A} - \dfrac{2\pi r}{\sqrt{2A}}` | Dies per wafer of usable radius $r$ |
| $\dfrac{C_{\text{wafer}}}{N Y}$ | `\dfrac{C_{\text{wafer}}}{N Y}` | Cost per good die |

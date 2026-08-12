---
chinese: 物理量与单位 (wùlǐliàng yǔ dānwèi)
prerequisites:
  - "[[Units of Measure (Vocab)]]"
  - "[[Standard Form (Vocab)]]"
leads_to:
  - "[[Accuracy vs Precision]]"
  - "[[Error Propagation]]"
  - "[[Significant Figures]]"
  - "[[Repeated Measurements]]"
  - "[[Calibration of Instruments]]"
  - "[[Vectors in Physics]]"
  - "[[Electric Current]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/experimental-physics
  - domain/measurement
  - domain/foundations
  - level/A-Level
  - level/IB
  - level/AP
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-2
  - syllabus/9702-1-1
  - syllabus/9702-1-2
  - syllabus/0625-1-1
  - syllabus/IB-Physics-A-1
  - syllabus/AP-Physics-1-SP-1
  - type/deep
  - type/definition
  - notation/SI-units
  - notation/dimensional-brackets
  - misconception/unitless-number-is-meaningful
  - misconception/derived-and-base-are-different-things
  - misconception/dimensional-check-replaces-physical-check
---

# Physical Quantities and Units 物理量与单位

## Hunter trace — a $327M lesson in why units matter

**23 September 1999.** The Mars Climate Orbiter — a $327.6 million NASA spacecraft — fires its main engine to enter Mars orbit. The burn was supposed to bring the spacecraft into a $110~\text{km}$ orbital altitude. Instead the spacecraft descends to $57~\text{km}$, dips into the upper Martian atmosphere, and burns up.

The post-mortem investigation traced the failure to a single line of code. Lockheed Martin's ground-control software output thruster impulse in **pound-seconds (lbf·s)**, an imperial unit. The JPL trajectory-correction software, which read those numbers, was written assuming **newton-seconds (N·s)**, the SI unit. Pound-seconds and newton-seconds are *both* units of impulse — they measure the same physical quantity, "change in momentum" — but $1~\text{lbf·s} = 4.45~\text{N·s}$. Every thruster burn was reading low by exactly that factor. The trajectory drifted. The orbiter died.

Why is this the right opening for a card on physical quantities and units? Because the failure was *not* a coding bug, not a physics error, not a calculation mistake. The math was right; the physics was right; both teams' code worked exactly as intended. **The error was that one number was attached to the wrong unit, and nobody checked.** $327$ million dollars vanished into Mars because the engineering culture treated the unit as a label and the number as the data — when in fact *the unit is half the data*.

This card is about taking that seriously. A physical quantity is *not* a number. It is a **number multiplied by a unit**. Drop the unit and you have nothing meaningful — you have an answer to the question "*how many*?" without an answer to "*how many what*?". Most of the time, in school physics, the unit is implicit and you can carry it in your head. *Sometimes* — and the times it matters are the times that bite — the unit has to live in your written work explicitly. The discipline this card teaches is what would have caught the Mars Climate Orbiter bug on the ground.

## Definition

A **physical quantity** (物理量 wùlǐliàng) is the product of a **numerical magnitude** and a **unit**:

$$\text{physical quantity} = (\text{number}) \times (\text{unit})$$

The unit is *the chosen reference standard* for that kind of quantity; the number tells you how many of that reference you have. "The table is $1.5~\text{m}$ long" means: take the SI metre, the international standard for length, lay it end to end, and the table is $1.5$ copies of it. Switch to feet ($1~\text{m} \approx 3.28~\text{ft}$) and the *same physical quantity* has a different number — $4.92~\text{ft}$ — but the same physical reality.

The unit is the answer to "*compared to what*?". Without it the number has no anchor.

### 中文锚点

**物理量** (wùlǐliàng) = physical quantity. 中文物理教学经常用一个简单的公式总结全部物理量的本质：

$$\text{物理量} = \text{数值} \times \text{单位}$$

这个等式的精神是：数值 (number) 和单位 (unit) **缺一不可**。例如，"长度是 1.5"是没有意义的 — 1.5 米？1.5 英寸？1.5 公里？数值告诉你"多少"，单位告诉你"多少**什么**"。

| English | 中文 | 例子 / Example |
|---|---|---|
| Physical quantity | 物理量 (wùlǐliàng) | length, mass, time, force, energy |
| Numerical magnitude | 数值 (shùzhí) | the "1.5" in "1.5 m" |
| Unit | 单位 (dānwèi) | the "m" in "1.5 m" |
| Base unit | 基本单位 (jīběn dānwèi) | metre, kilogram, second — the seven primitives |
| Derived unit | 导出单位 (dǎochū dānwèi) | newton, joule, watt — products of base units |
| SI (Système International) | 国际单位制 (guójì dānwèi zhì) | the international standard |
| Dimensional homogeneity | 量纲齐次性 (liànggāng qíchixìng) | every term in a physical equation has the same dimensions |
| Dimensional analysis | 量纲分析 (liànggāng fēnxī) | the *algebra* of units; a research and checking tool |
| Estimate / order-of-magnitude | 估算 / 数量级估算 (gūsuàn / shùliàngjí gūsuàn) | "reasonable estimates" — Fermi-style ballpark calculations |

## The seven SI base units

All of physics is built on **seven base units**. Every other unit is a product (and quotient) of these. The 2019 SI redefinition fixed each of these units in terms of an exact numerical value of a fundamental constant — see beyond-syllabus below.

| Quantity | SI unit | Symbol | Definition anchor (post-2019) |
|---|---|---|---|
| Length | metre | $\text{m}$ | $c = 299{,}792{,}458~\text{m·s}^{-1}$ exact |
| Mass | kilogram | $\text{kg}$ | $h = 6.62607015 \times 10^{-34}~\text{J·s}$ exact |
| Time | second | $\text{s}$ | $\Delta\nu_{\text{Cs}} = 9{,}192{,}631{,}770~\text{Hz}$ exact (caesium-133 hyperfine transition) |
| Electric current | ampere | $\text{A}$ | $e = 1.602176634 \times 10^{-19}~\text{C}$ exact |
| Thermodynamic temperature | kelvin | $\text{K}$ | $k_{\text{B}} = 1.380649 \times 10^{-23}~\text{J·K}^{-1}$ exact |
| Amount of substance | mole | $\text{mol}$ | $N_{\text{A}} = 6.02214076 \times 10^{23}~\text{mol}^{-1}$ exact |
| Luminous intensity | candela | $\text{cd}$ | $K_{\text{cd}} = 683~\text{lm·W}^{-1}$ exact (for $540~\text{THz}$ green light) |

For 9702 (and most undergraduate physics), the first five — metre, kilogram, second, ampere, kelvin — are the working set. Mole appears in chemistry, thermal physics, and quantum gas laws; candela rarely shows up outside lighting design and visual perception studies. Memorise the first five.

> [!info] Beyond syllabus — the 2019 SI redefinition
> Recall that until **20 May 2019**, the kilogram was defined as the mass of a particular *physical object* — a platinum-iridium cylinder kept in a vault in Sèvres, France, called the **International Prototype Kilogram (IPK)**. Every kilogram on Earth was, ultimately, calibrated against that one lump of metal. The problem is that the IPK was *drifting* — over a century of comparisons against six official copies kept alongside it, its mass had changed by roughly $50~\mu\text{g}$ relative to the average of the copies. No one knew which one had drifted; possibly all of them had. The kilogram itself was unstable.
>
> On 20 May 2019, the General Conference on Weights and Measures (CGPM) redefined every SI base unit in terms of **fixed values of fundamental physical constants**. The kilogram is now defined by fixing Planck's constant $h$ to exactly $6.62607015 \times 10^{-34}~\text{J·s}$ — and since the joule and the second are themselves defined by other constants, this gives an operational recipe for realising the kilogram anywhere in the universe using a *Kibble balance* (which compares mechanical and electromagnetic power, both of which contain $h$).
>
> The deep idea: **the universe should be its own calibration standard, not a lump of metal in Paris**. The 2019 redefinition is one of the most beautiful pieces of metrology in modern science — physics decided that the units of physics should reference quantities that are themselves laws of physics. The metre had been redefined this way back in 1983 (fixing the speed of light $c$); the second has been atomic since 1967 (fixing caesium's transition frequency); the kilogram was the last holdout, and finally fell in 2019.

## SI prefixes

A prefix is a power-of-ten multiplier glued onto a unit symbol. The 9702 syllabus expects fluent use of the range from **pico ($10^{-12}$) to tera ($10^{12}$)**.

| Prefix | Symbol | Multiplier | Example |
|---|---|---|---|
| tera | T | $10^{12}$ | $1~\text{TWh} = 10^{12}~\text{Wh}$ (global energy use ≈ 160,000 TWh/year) |
| giga | G | $10^9$ | $1~\text{GHz} = 10^9~\text{Hz}$ (laptop CPU clock) |
| mega | M | $10^6$ | $1~\text{MW} = 10^6~\text{W}$ (wind turbine output) |
| kilo | k | $10^3$ | $1~\text{km} = 10^3~\text{m}$ |
| (none) | — | $10^0$ | base unit |
| deci | d | $10^{-1}$ | $1~\text{dm} = 0.1~\text{m}$ (rarely used outside volume: $\text{dm}^3 = $ litre) |
| centi | c | $10^{-2}$ | $1~\text{cm} = 0.01~\text{m}$ |
| milli | m | $10^{-3}$ | $1~\text{mA} = 10^{-3}~\text{A}$ |
| micro | μ | $10^{-6}$ | $1~\mu\text{m} = 10^{-6}~\text{m}$ (bacteria; wavelength of light is sub-μm) |
| nano | n | $10^{-9}$ | $1~\text{ns} = 10^{-9}~\text{s}$ (light travels $30~\text{cm}$ in 1 ns) |
| pico | p | $10^{-12}$ | $1~\text{pF} = 10^{-12}~\text{F}$ (capacitor on a circuit board) |

> [!warning] Two prefixes that look identical
> Lower-case **m** is *milli* ($10^{-3}$). Capital **M** is *mega* ($10^6$). The factor between them is $10^9$ — *one billion*. Writing $5~\text{MW}$ when you mean $5~\text{mW}$ confuses a wind turbine with the light from a laser pointer. Always check the case in tables and on circuit diagrams.

> [!info] Beyond syllabus — the 2022 prefix extension
> In November 2022, the CGPM added four new prefixes at the extremes: **ronna (R, $10^{27}$), quetta (Q, $10^{30}$)** at the top, and **ronto (r, $10^{-27}$), quecto (q, $10^{-30}$)** at the bottom. These exist because data scientists were running out of names — global data storage was about to exceed $1~\text{yottabyte} = 10^{24}~\text{B}$, and the bookkeepers wanted ahead-of-time vocabulary. *The Earth weighs about $6~\text{Rg}$ (ronnagrams); an electron weighs about $0.9~\text{qg}$ (quectograms).* These are not yet on 9702 syllabuses; they will be by the 2030s.

## Derived units

A **derived unit** is a product (or quotient) of base units. The seven base units are the *primitives* of the system; everything else is constructed from them by multiplication, division, and exponentiation.

Some derived units get short *named* symbols (newton, joule, watt) for convenience; others stay in their long form ($\text{kg·m·s}^{-2}$). The long form is always available as a fallback when you want to do dimensional analysis — see the next section.

| Quantity | Named unit | Equivalent in base units |
|---|---|---|
| Force | newton (N) | $\text{kg·m·s}^{-2}$ |
| Energy / work | joule (J) | $\text{kg·m}^2\text{·s}^{-2}$ |
| Power | watt (W) | $\text{kg·m}^2\text{·s}^{-3}$ |
| Pressure | pascal (Pa) | $\text{kg·m}^{-1}\text{·s}^{-2}$ |
| Frequency | hertz (Hz) | $\text{s}^{-1}$ |
| Electric charge | coulomb (C) | $\text{A·s}$ |
| Potential difference | volt (V) | $\text{kg·m}^2\text{·s}^{-3}\text{·A}^{-1}$ |
| Resistance | ohm (Ω) | $\text{kg·m}^2\text{·s}^{-3}\text{·A}^{-2}$ |

The named units are *cosmetic* — they make formulas readable. The base-unit equivalent is the *truth*. Whenever a unit looks unfamiliar, you can always expand it back into kilograms, metres, seconds, amperes and check what you actually have.

> [!tip] Reading derived units backwards
> $\text{W} = \text{J·s}^{-1}$ — *power is energy per time*. Yes; that's the definition of power.
> $\text{Pa} = \text{N·m}^{-2}$ — *pressure is force per area*. Yes.
> $\text{V} = \text{J·C}^{-1}$ — *potential difference is energy per charge*. Yes — this is exactly what voltage means.
>
> Every derived unit, when expanded, *tells you the definition of the physical quantity*. The unit is the formula. You can derive what voltage *means* by staring at its unit long enough; you don't need a separate memorised definition. **This is the principle that turns dimensional analysis into a research tool.**

## Dimensional homogeneity — the central principle

Here is the deep idea this card exists to teach.

**Every term in a physical equation must have the same units.** This is called **dimensional homogeneity** (量纲齐次性). It is not a convention or a preference; it is *forced* by what equations mean.

Think about what it would mean for an equation to *not* be dimensionally homogeneous — to write, say, $E = mc^2 + v$, where the left side is energy ($\text{kg·m}^2\text{·s}^{-2}$), the right side is energy plus velocity ($\text{m·s}^{-1}$). Could you "add energy and velocity"? What number would that even produce? In what unit? **The equation becomes literally meaningless** — and not because it's *wrong* in the sense of *getting the answer numerically off*, but wrong in the sense of *not being a coherent statement at all*. It's the physics analogue of "the colour green weighs 3 metres on Tuesdays." There is no thing it is failing to describe correctly; it does not describe a thing.

So *whatever* a physical equation says, both sides — and every term on both sides — must have the *same* units. This gives you two enormous gifts:

**Gift 1 — the world's cheapest sanity check.** If you derive a result $F = mv^2/r^2$, you can check the units: $\text{kg} \cdot (\text{m·s}^{-1})^2 / \text{m}^2 = \text{kg·s}^{-2}$. But force has units $\text{kg·m·s}^{-2}$. The expression is off by one factor of $\text{m}$ — so the formula is wrong. (The correct centripetal-force formula is $F = mv^2/r$.) **You caught an error without doing any physics.** Just checking units catches a huge fraction of derivation mistakes — see the worked examples below.

**Gift 2 — you can sometimes guess the formula.** This is more spectacular. Given a list of quantities you *expect* to appear in a problem, dimensional homogeneity often pins down the formula up to a dimensionless prefactor. This is **dimensional analysis as a research tool**, and physicists use it routinely to estimate unknown formulas before doing the hard work.

### Dimensions notation

The **dimensions** of a physical quantity are its units stripped to the base level, written in square brackets:

- $[\text{length}] = \text{L}$ or just $\text{m}$ — the dimension of *anything* that's a length
- $[\text{mass}] = \text{M}$ or just $\text{kg}$
- $[\text{time}] = \text{T}$ or just $\text{s}$
- $[F] = \text{MLT}^{-2}$ or just $\text{kg·m·s}^{-2}$

Cambridge and most physics texts use the explicit-unit form ($\text{kg·m·s}^{-2}$); pure dimensional analysis sometimes uses the M-L-T letter form. Both say the same thing.

### The classic worked example — period of a simple pendulum

The simple pendulum (see [[Simple Harmonic Motion]]): a mass $m$ on a string of length $\ell$ swinging under gravity $g$. **What is its period $T$?**

Suppose you haven't yet derived the answer. You expect $T$ to depend on $m$, $\ell$, and $g$. Write a hopeful expression:

$$T = k \cdot m^a \cdot \ell^b \cdot g^c$$

where $k$ is some dimensionless prefactor and $a, b, c$ are exponents to find. The units must match.

$$[T] = \text{s}, \quad [m] = \text{kg}, \quad [\ell] = \text{m}, \quad [g] = \text{m·s}^{-2}$$

Substituting:

$$\text{s} = \text{kg}^a \cdot \text{m}^b \cdot (\text{m·s}^{-2})^c = \text{kg}^a \cdot \text{m}^{b+c} \cdot \text{s}^{-2c}$$

Now match powers on each base unit, one at a time:

- $\text{kg}$: left side has $0$, right side has $a$. So $a = 0$.
- $\text{s}$: left side has $1$, right side has $-2c$. So $c = -\tfrac{1}{2}$.
- $\text{m}$: left side has $0$, right side has $b + c$. So $b = -c = \tfrac{1}{2}$.

Therefore $T = k \cdot \ell^{1/2} \cdot g^{-1/2} = k\sqrt{\ell/g}$.

Two things are remarkable here.

First, *the mass dropped out* — dimensional analysis alone predicts that a pendulum's period does not depend on its bob mass. **Galileo discovered this experimentally in the late 16th century**, watching a swinging lamp in Pisa Cathedral; we've just re-derived his result without any physics, only by demanding dimensional homogeneity. That is the power of the method.

Second, dimensional analysis *cannot* fix the prefactor $k$. To get $k = 2\pi$ (giving the textbook formula $T = 2\pi\sqrt{\ell/g}$) you have to do the actual physics — solve Newton's second law for the small-angle pendulum. **Dimensional analysis pins down the *structure*; physics fills in the *numbers*.**

This is the workflow physicists use constantly. Faced with an unknown phenomenon (drag on a sphere falling through fluid; radius of an atomic bomb's shockwave; emission spectrum of a hot body), the first move is to list which physical quantities ought to enter and demand dimensional homogeneity. The structure of the answer often falls out in a few lines; the dimensionless prefactor is then either measured experimentally or computed from the underlying theory. **Buckingham's $\pi$ theorem** (1914) is the formal generalisation of this trick.

> [!info] Beyond syllabus — the Trinity yield
> When **G. I. Taylor** declassified estimates of the 1945 Trinity nuclear test in 1950, he had only a sequence of photographs showing the fireball's radius $R$ at various times $t$ after detonation. He argued by dimensional analysis. The fireball expands into the surrounding air; the relevant quantities are the energy released $E$, the time $t$, and the ambient air density $\rho$. By the same procedure as the pendulum:
>
> $$R = k \cdot E^a \cdot t^b \cdot \rho^c$$
>
> Matching dimensions ($[E] = \text{kg·m}^2\text{·s}^{-2}$, $[\rho] = \text{kg·m}^{-3}$, $[t] = \text{s}$, $[R] = \text{m}$) gives $a = \tfrac{1}{5}$, $b = \tfrac{2}{5}$, $c = -\tfrac{1}{5}$. So
>
> $$R = k \cdot \left(\frac{E t^2}{\rho}\right)^{1/5} \quad \Longrightarrow \quad E = \frac{k^{-5} \rho R^5}{t^2}.$$
>
> Plugging in the photographs' $R$ and $t$ values, with $k$ near $1$ (from a fluid-dynamics calculation), Taylor estimated $E \approx 20~\text{kilotons of TNT}$. The classified actual value was $21$ kilotons. He published this in the open literature using only declassified photographs and dimensional analysis. The US government was reportedly furious that the bomb yield could be inferred from public sources.

## Reasonable estimates (Fermi estimation)

The 9702 syllabus §1.1 includes the line *"reasonable estimates of physical quantities included within the syllabus"*. This sounds dull on the page; in practice it is one of the most fun habits in physics.

A **Fermi estimate** is an order-of-magnitude calculation done in your head, from rough numbers, to within roughly a factor of 10 of the truth. The name honours **Enrico Fermi**, who at the Trinity test on 16 July 1945 dropped scraps of paper from his hand at the moment the shock wave arrived and used their horizontal displacement to estimate the bomb's yield at about $10~\text{kt}$. (The actual yield was $21~\text{kt}$; Fermi was within a factor of two, on the spot, with no instruments.)

The exam version is gentler. Examples:

- **How fast does sound travel?** Speed of sound depends on air pressure, density, and the molecular speed of air molecules. Air molecules at room temperature have RMS speed near $500~\text{m·s}^{-1}$. Sound is a pressure disturbance carried by these molecules; its speed should be the same order of magnitude. *Actual: $343~\text{m·s}^{-1}$ at $20~^\circ\text{C}$.* Within a factor of $1.5$ — Fermi success.
- **Atoms per cubic millimetre of water.** Water has density $10^3~\text{kg·m}^{-3}$, so a $\text{mm}^3$ is $10^{-6}~\text{kg} = 10^{-3}~\text{g}$. Molecular mass of water is $18~\text{g·mol}^{-1}$, so a mm$^3$ holds $10^{-3}/18 \approx 6 \times 10^{-5}$ moles, and Avogadro's number gives $6 \times 10^{-5} \times 6 \times 10^{23} \approx 4 \times 10^{19}$ molecules. That's $10^{19}$-ish — a useful order to remember.
- **Pressure on a thumbtack.** Push with $10~\text{N}$ on a tip of area $10^{-7}~\text{m}^2$: pressure $\sim 10^8~\text{Pa}$, or about $10^3$ atmospheres. That's why thumbtacks pierce walls and your thumb stays intact.

The trick is to remember a small kit of magnitude anchors — Avogadro's number, the speed of light, atmospheric pressure ($10^5~\text{Pa}$), Earth's mass ($6 \times 10^{24}~\text{kg}$), human-scale lengths ($1~\text{m}$), atomic scale ($10^{-10}~\text{m}$) — and chain them together. **What you cannot calculate precisely, you can still estimate.** The exam reward for this skill is small (a single mark or two on "estimate the…" questions) but the cognitive reward is large: physicists who can estimate quickly are physicists who catch errors before publication.

## Common mistakes

### 1. Dropping the unit when carrying a calculation

A common 9702 student writing: $F = ma$, $m = 2$, $a = 5$, so $F = 10$. **Wrong workflow.** The right workflow is $F = (2~\text{kg})(5~\text{m·s}^{-2}) = 10~\text{kg·m·s}^{-2} = 10~\text{N}$. Carrying the unit through every step does three things: catches calculation slips before they propagate, makes the final unit a sanity check, and trains the dimensional-homogeneity instinct. *Mars Climate Orbiter happened because somebody dropped a unit.*

### 2. Treating named derived units as "different" from their base form

Students sometimes hesitate over whether $\text{W·m}^{-2}$ is "the same as" $\text{kg·s}^{-3}$. **It is** — substitute $\text{W} = \text{kg·m}^2\text{·s}^{-3}$ and the metres cancel. The named form ($\text{W·m}^{-2}$, *intensity*) is the *physics* statement; the base form ($\text{kg·s}^{-3}$) is the *bookkeeping*. Both are correct.

### 3. Confusing prefixes and units

$\text{mm}^2$ is **not** $10^{-3}~\text{m}^2$; it is $(10^{-3}~\text{m})^2 = 10^{-6}~\text{m}^2$. The prefix attaches to the unit *before* the squaring. Same for $\text{cm}^3 = 10^{-6}~\text{m}^3$. (This is the same point the [[Units of Measure (Vocab)]] card hammers at 0580 level; it reappears in every 9702 paper that asks for volume in m³.)

### 4. Believing a dimensional check *proves* an equation is right

A dimensionally homogeneous equation is **necessary** but **not sufficient** for physical correctness. Both $F = ma$ and $F = 2ma$ are dimensionally homogeneous; one is right and the other is wrong by a factor of two. Dimensional analysis catches *structural* errors (wrong powers, missing variables); it does *not* catch numerical-prefactor errors. **Dimensional homogeneity is the world's cheapest sanity check, not a proof of correctness.** Always still do the physics.

## Exam Notes

### Cambridge 9702 (AS Level)

**Syllabus ref:** 1.1 (physical quantities, magnitude × unit, reasonable estimates) and 1.2 (SI base/derived units, homogeneity check, prefixes p to T).

What 9702 actually tests:
- Identify which of a list of units is a derived unit (e.g. "which of $\text{N}, \text{kg}, \text{m·s}^{-2}, \text{J}$ is a base unit?").
- Convert a quantity given in a derived form ($\text{kJ·mol}^{-1}$) into base SI units.
- Use prefixes — read $470~\text{nF}$ as $470 \times 10^{-9}~\text{F}$, $4.7~\text{GHz}$ as $4.7 \times 10^9~\text{Hz}$.
- Check whether a proposed equation is dimensionally consistent. *Example exam-style question:* "A student suggests $v^2 = u^2 + 2as^2$. Use the homogeneity of units to show that this equation is incorrect." (Answer: $[v^2] = \text{m}^2\text{·s}^{-2}$, $[as^2] = \text{m·s}^{-2} \cdot \text{m}^2 = \text{m}^3\text{·s}^{-2}$. Different units, not homogeneous, equation wrong.)
- Make a reasonable estimate (typically one mark) — e.g. "estimate the kinetic energy of a sprinter at full speed," "estimate the volume of air in this classroom."

> [!tip] Paper 1 (multiple choice) traps
> Half the §1.1/§1.2 multiple-choice questions are testing **prefix arithmetic** — $2~\text{ns} \times 3 \times 10^8~\text{m·s}^{-1} = ?$ in $\text{cm}$. Be ruthless about converting everything to SI base units *first*, then converting the answer to the requested unit at the end. Trying to keep prefixes mixed in mid-calculation is how you lose easy marks.

### Cambridge 0625 (IGCSE Physics)

§1.1 (length and time, including the volume of liquid via measuring cylinder, the period of a pendulum or pulse) and §1.3 (mass and weight). 0625 is less rigorous about derived units than 9702 but more rigorous about the practical reading of instruments (vernier callipers, micrometers, stopwatches). The dimensional-analysis machinery is generally not tested at 0625 level — that piece is 9702 only.

### IB Physics

Theme A — measurements and uncertainty — opens with SI base units, prefixes, and order-of-magnitude estimation. The "reasonable estimates" content is taken further at HL: IB Practical 2 (PRAC.2) explicitly asks students to estimate, justify, and compare against measurement. Buckingham's $\pi$ theorem is not on the syllabus but appears in Extended Essays.

### AP Physics 1 and 2

Science Practice 1 (Modeling) explicitly tests both unit literacy and dimensional analysis. The AP exam loves to ask: "Which of these expressions could possibly equal the period of a satellite orbit?" — and the wrong answers all fail dimensionally. **A few marks per paper are accessible via pure unit-checking.** Worth the time investment.

### A-Level (other boards)

Edexcel, AQA, OCR all use SI base + derived structures matching the Cambridge syllabus. The only board-level variation is in the depth of "estimation" expected — AQA tends to ask more Fermi-style estimation questions; OCR tends to ask more dimensional-consistency questions.

## Connections

- **Prerequisite:** [[Units of Measure (Vocab)]] — the 0580-level conversion ladder (metre/centimetre/millimetre, length-squared for area, length-cubed for volume). The Mathematics-side card carries the bookkeeping; this card carries the physics-side substance.
- **Prerequisite:** [[Standard Form (Vocab)]] — every physical quantity at any non-human scale is expressed in standard form ($1.6 \times 10^{-19}~\text{C}$, $6 \times 10^{24}~\text{kg}$); the prefix table is itself a standard-form shortcut.
- **Leads to:** [[Accuracy vs Precision]] — once you have a number-with-a-unit, the next question is *how precise is the number*?
- **Leads to:** [[Error Propagation]] — the unit travels through the propagation calculation alongside the number; sanity-checking units at the end catches errors.
- **Leads to:** [[Significant Figures]] — significant figures attach to the *number* part of a physical quantity; the unit is exact.
- **Leads to:** [[Vectors in Physics]] — the next §1.4 row: physical quantities split into scalars (have only magnitude) and vectors (have magnitude *and* direction). The Mathematics-side [[Vectors]] card carries the machinery; the [[Vectors in Physics]] card extends the choice-of-axes invariance idea introduced here in §"Dimensional homogeneity" to spatial-axis choice in mechanics.
- **Parallel — physics application:** [[Linear Momentum]], [[Hooke's Law for Springs]] — each carries a dimensional-analysis check of its central formula (Hooke's $\omega = \sqrt{k/m}$ for the spring, momentum's $F = \dot p$). The principle taught here gets reused there.
- **Bridge to Mathematics:** [[Histograms]] §"Frequency density" — the unit-algebra perspective is what makes "area under the histogram = total frequency" come out cleanly.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\text{m}$, $\text{kg}$, $\text{s}$ | `\text{m}, \text{kg}, \text{s}` | Always wrap unit symbols in `\text{}` so italics don't render |
| $\text{m·s}^{-1}$ | `\text{m·s}^{-1}` | Preferred over $\text{m/s}$ in formal physics writing |
| $\text{kg·m·s}^{-2}$ | `\text{kg·m·s}^{-2}` | Base-unit form of newton |
| $[F]$ | `[F]` | The dimensions of $F$ |
| $\mu$ | `\mu` | Micro prefix (also Greek letter mu) |
| $\pm$ | `\pm` | For ranges and uncertainties — handed off to [[Error Propagation]] |
| $\times 10^n$ | `\times 10^n` | Standard form for very large or very small quantities |

---
chinese: 熵与热力学第二定律 (shāng yǔ rèlìxué dì-èr dìnglǜ)
prerequisites:
  - "[[First Law of Thermodynamics]]"
  - "[[Internal Energy]]"
  - "[[Kinetic Theory and the Ideal Gas]]"
leads_to:
  - "[[The Gift of the Gradient]]"
tags:
  - subject/physics
  - subject/computer-science
  - domain/thermal-physics
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - type/law
  - type/concept
  - notation/S-entropy
  - notation/k-boltzmann
  - notation/W-multiplicity
  - notation/eta-efficiency
  - misconception/entropy-is-disorder
  - misconception/second-law-is-absolute
  - misconception/entropy-cannot-decrease-locally
  - misconception/heat-engine-can-be-100-percent
  - misconception/life-violates-second-law
---

# Entropy and the Second Law  熵与热力学第二定律

> *"Die Energie der Welt ist konstant. Die Entropie der Welt strebt einem Maximum zu."* — Rudolf Clausius, 1865. *The energy of the world is constant; the entropy of the world tends toward a maximum.* The two laws of thermodynamics in a single sentence.
>
> *Of all the laws of physics, only the second knows the difference between the past and the future.*

The [[First Law of Thermodynamics|first law]] says energy is conserved — the books always balance. And that is exactly its blind spot. A dropped cup shatters but never reassembles; heat flows from your coffee into the room but never gathers back out of the room to reheat the cup; no engine ever turns *all* of its fuel's heat into motion. **Not one of those reversals would violate energy conservation.** The books would still balance. Yet nature forbids them anyway. Something beyond bookkeeping picks a direction for time and stamps it on every process in the universe.

That something is the **second law of thermodynamics**, and its currency is a quantity Clausius named in 1865 from the Greek *τροπή* ("transformation"): **entropy**, $S$. This is where thermodynamics stops being accounting and starts being *fate*.

## 中文锚点

**核心论题**：[[First Law of Thermodynamics|第一定律]]说能量守恒——账永远平。但它对一个明显的事实保持沉默：碎杯子不会自动复原，热不会自发从冷流向热，没有热机能把热全变成功——**这些反过程都不违反能量守恒**，自然却依然禁止它们。是**第二定律**给时间定了方向，它的货币叫**熵** $S$。

第二定律有三种等价表述：**克劳修斯**（热不会自发地从冷流向热）、**开尔文**（没有循环热机能把热全部变成功）、**熵**（孤立系统的熵永不减少，$\Delta S_{\text{孤立}} \ge 0$）。

熵有两个定义，它们在深处相遇：
- **宏观（克劳修斯）**：$\mathrm{d}S = \delta Q_{\text{rev}}/T$，可逆吸热 $Q$ 时 $\Delta S = Q/T$，单位 J/K，是状态函数。
- **微观（玻尔兹曼）**：$S = k\ln W$，$W$ 是与宏观态相容的微观态数目。（完整的数学与玻尔兹曼的人生见 [[Stories/Boltzmann's Tombstone|玻尔兹曼的墓碑]]。）

第二定律不是铁律，而是**压倒性的概率**：气体"散开"对应的微观态数目多到反过程永远等不到。热机效率 $\eta = W/Q_h = 1 - Q_c/Q_h$，上限是卡诺效率 $\eta_C = 1 - T_c/T_h$。而熵 $S=k\ln W$ 与香农信息熵 $H = -\sum p\log p$ **是同一个数学对象**（见 [[Information Theory]]）——熵就是"缺失的信息"。

---

## Why the first law is not enough

The first law is a filter that lets far too much through. It permits the coffee to reheat, the cup to un-shatter, the exhaust to rush back into the engine and undo the explosion — because each of those merely *moves* energy around without creating or destroying any. Nature runs a *second* filter, finer than the first, and only processes that pass **both** actually happen. The second law is that finer filter, and it can be stated three ways that sound different and are secretly identical.

## Three statements, one law

- **Clausius statement.** Heat never flows spontaneously from a colder body to a hotter one. (To move heat "uphill" you must *do work* — that is what a refrigerator is.)
- **Kelvin–Planck statement.** No cyclic process can take heat from a single reservoir and convert it *entirely* into work. Every engine must dump some heat as waste.
- **Entropy statement.** The total entropy of an **isolated system** never decreases: $\Delta S_{\text{isolated}} \ge 0$, with equality only for a reversible (idealised) process.

These three are **equivalent** — assume a machine that breaks one and you can bolt it to a second machine to break the others. They are one law wearing three faces: a rule about heat flow, a rule about engines, and a rule about a number that only ever climbs.

## Entropy the macroscopic way: Clausius's $Q/T$

Clausius gave entropy a definition you can measure with a thermometer and a heater, before anyone knew atoms were real. For a **reversible** transfer of a small amount of heat $\delta Q$ into a system at absolute temperature $T$:

$$\mathrm{d}S = \frac{\delta Q_{\text{rev}}}{T}, \qquad \text{so for heat } Q \text{ at constant } T,\quad \Delta S = \frac{Q}{T}.$$

Entropy is measured in **joules per kelvin (J/K)**, and — like [[Internal Energy|internal energy]] — it is a **state function**: the entropy of a system depends only on its present state, never on the route it took there. The same heat is "worth" more entropy when delivered at low temperature than at high: a joule into a cold system disturbs its few, sluggish arrangements far more than a joule into an already-hot one.

**Why heat flows hot → cold, derived.** Let heat $Q$ pass from a hot body at $T_h$ to a cold one at $T_c$. The hot body loses entropy $Q/T_h$; the cold body gains entropy $Q/T_c$. The net change of the pair is

$$\Delta S = \frac{Q}{T_c} - \frac{Q}{T_h} = Q\left(\frac{1}{T_c} - \frac{1}{T_h}\right) > 0 \quad\text{because } T_c < T_h.$$

The forward direction *increases* total entropy; the reverse would *decrease* it, so the reverse is forbidden. **The direction of spontaneous change is simply the direction of increasing entropy** — that one inequality is the whole arrow, made quantitative. (For a real, irreversible flow across a finite temperature gap, the inequality is strict — entropy is genuinely *created*, not merely moved.)

## Entropy the microscopic way: Boltzmann's $S = k\ln W$

Clausius could measure entropy but not say *what it is*. Boltzmann answered: entropy counts **how many microscopic arrangements look the same from the outside.**

A gas has one **macrostate** (its pressure, volume, temperature) but a staggering number of **microstates** (the exact position and velocity of every molecule). Let $W$ be the number of microstates consistent with the macrostate. Then

$$\boxed{\,S = k\ln W\,}, \qquad k = 1.38\times10^{-23}\ \text{J/K (Boltzmann constant).}$$

The counting is concrete. Put four numbered molecules in a box and ask how many are in the left half:

| Macrostate (number on left) | Microstates (which molecules) | $W$ |
|---|---|---|
| 0 left | — | 1 |
| 1 left | 4 ways | 4 |
| **2 left (even split)** | **6 ways** | **6** |
| 3 left | 4 ways | 4 |
| 4 left | — | 1 |

The even split already has the most arrangements. Now scale up. For $N$ molecules the multiplicity is $W = \binom{N}{n}$, and its peak at the even split grows *unfathomably* sharper as $N$ climbs — so sharp that for a real gas ($N \sim 10^{23}$) essentially every microstate is a near-even split.

![[entropy-multiplicity-sharpens.svg|660]]
*The multiplicity $W=\binom{N}{n}$ (scaled to its peak) against the fraction on the left, for growing $N$. At $N=10$ the distribution is broad; by $N=1000$ it is a spike. Extrapolate to $N\sim10^{23}$ and the spike is narrower than a razor: the gas sits at "spread out" not because a law commands it, but because the alternatives are outnumbered beyond any hope of occurring.*

This is Boltzmann's detonation of the mystery. **The second law is not a commandment; it is a bet at overwhelming odds.** A gas *could* rush into one corner, ice *could* form in warm water, the smoke *could* pour back into the cigarette — none violates any mechanical law. They simply correspond to so few microstates that you would wait many times the age of the universe to catch one. (The full story — Boltzmann's life, the reversibility and recurrence paradoxes that nearly broke him, and *why* the formula must use a logarithm — lives in [[Stories/Boltzmann's Tombstone]].)

And the miracle worth pausing on: Clausius's lab-measured $Q/T$ and Boltzmann's abstract $k\ln W$ are **the same quantity**. A number you get from a thermometer equals $k$ times the log of a count of invisible arrangements. Two centuries of physics live in that equals sign.

## Heat engines and the Carnot limit

The Kelvin statement forbids the free lunch, and its price tag is the most consequential number in engineering. A **heat engine** runs in a cycle: it draws heat $Q_h$ from a hot reservoir, converts *part* of it to useful work $W$, and dumps the rest, $Q_c$, into a cold reservoir.

![[entropy-heat-engine.svg|697]]
*Every heat engine is this diagram. Heat $Q_h$ falls from the hot reservoir; a slice $W$ is peeled off as work; the remainder $Q_c$ must be dumped to the cold reservoir. A refrigerator is the same picture with every arrow reversed — work pushes heat uphill.*

Since the engine returns to its start each cycle, its internal energy is unchanged ($\Delta U = 0$), so the first law gives $W = Q_h - Q_c$. The **efficiency** is the fraction of the drawn heat that becomes work:

$$\eta = \frac{W}{Q_h} = 1 - \frac{Q_c}{Q_h}.$$

The Kelvin statement says $Q_c$ can never be zero — so $\eta$ can **never reach 1.** Why not? Follow the *entropy*. Taking in $Q_h$ at $T_h$ carries entropy $Q_h/T_h$ *into* the engine each cycle; because entropy is a state function, the engine must expel exactly as much as it took in or it could not return to its starting state. The only exit is the waste heat $Q_c$ into the cold reservoir, carrying $Q_c/T_c$. The best case — a **reversible (Carnot) engine** that creates no new entropy — has these exactly equal:

$$\frac{Q_c}{T_c} = \frac{Q_h}{T_h} \;\Rightarrow\; \frac{Q_c}{Q_h} = \frac{T_c}{T_h} \;\Rightarrow\; \boxed{\,\eta_{\text{Carnot}} = 1 - \frac{T_c}{T_h}\,}.$$

**No engine working between $T_h$ and $T_c$ can beat this**, whatever it is built from — the limit is thermodynamic, not mechanical. Waste heat is not sloppy engineering; it is the entropy toll the second law charges to run a cycle at all. Run the whole picture backwards and you have a **refrigerator** or **heat pump**: pour in work to shove heat from cold to hot, which is the Clausius statement made into an appliance.

## The arrow of time

Here is the strangest fact in physics. Write down *any* fundamental law — Newton's $\mathbf{F}=m\mathbf{a}$, Maxwell's equations, the Schrödinger equation, general relativity — and film a process it governs. Run the film backward, and **it is still a legal process.** The microscopic laws do not care which way time runs; they are all time-symmetric.

Every one except the second law. The growth of entropy is the *only* place in all of physics where past and future are genuinely different. Why we remember yesterday and not tomorrow, why we age, why a broken glass never mends — all of it is $\Delta S \ge 0$ playing out. The puzzle this raises (if the microscopic laws are reversible, where does the arrow come from?) is **Loschmidt's paradox**, and its resolution points at cosmology: the arrow exists because the universe *began* in a staggeringly low-entropy state — the smooth, hot Big Bang — and has been climbing the multiplicity ladder ever since. The arrow of time points away from that special beginning. (Loschmidt, Zermelo, and Boltzmann's answer are told in full in [[Stories/Boltzmann's Tombstone]].)

## Entropy *is* information

The most surprising afterlife of Boltzmann's equation. In 1948 Claude Shannon, hunting for a measure of *information*, arrived at $H = -\sum_i p_i \log p_i$ — and it is the **same mathematical object** as $S = k\ln W$. (When the $W$ microstates are equally likely, $p_i = 1/W$ and Shannon's formula collapses straight back to Boltzmann's.) Thermodynamic entropy and information entropy are one quantity in two unit systems: physics counts in joules-per-kelvin with a natural log, information counts in **bits** with a base-2 log.

So entropy is **missing information** — the number of yes/no questions you would have to answer to pin down the exact microstate, given only the macrostate. This is not a metaphor. Let a gas of $N$ molecules double its volume by expanding freely into vacuum. Statistically each molecule now has twice the room, so $W\to 2^N W$, and

$$\Delta S = k\ln 2^N = Nk\ln 2 \;\;\longleftrightarrow\;\; N \text{ bits.}$$

Exactly one bit of entropy per molecule — the one bit that answers "which half are you in?" And the exchange rate runs the other way too: **Landauer's principle** says *erasing* one bit of information must dump at least $kT\ln 2$ of heat to the surroundings. Information is physical. It is why **Maxwell's demon** — the imp who seems to violate the second law by sorting fast molecules from slow — cannot win: to sort, it must *remember*, and eventually erasing that memory pays back every joule it seemed to save. (The information side is developed in [[Information Theory]]; the demon and Landauer are a bridge waiting at [[Maxwell's Demon]].)

## Does life break the second law?

A living cell builds exquisite order from a soup of molecules; a forest grows; an embryo assembles a body. Doesn't that *decrease* entropy? It does — **locally**, and that is allowed. The second law forbids the *total* entropy of an **isolated** system from falling, but a living thing is an **open** system: it maintains its internal order by exporting *more* disorder to its surroundings than it creates within. You eat low-entropy food and radiate high-entropy heat; the Earth catches a thin stream of low-entropy sunlight and dumps a fat stream of high-entropy infrared into space. The books balance the second law's way — order here is paid for by a larger disorder out there. Schrödinger, in *What is Life?* (1944), called it living on "negative entropy." (This is also the clean answer to the creationist misuse of the second law: local order is not a loophole in the law, it is the law running exactly as written.) And it points at something larger than biology — that a *gradient* is the precondition for anything to happen at all, and being alive means being a difference that is still falling: the reading in [[The Gift of the Gradient]].

> [!warning] "Entropy is disorder" — a lossy metaphor
> The disorder slogan is a crutch that breaks under weight: a messy bedroom is not measurably higher-entropy than a tidy one in the thermodynamic sense, and "disorder" tempts you to think entropy is subjective. The precise pictures are the two definitions themselves — **the number of microstates** ($S=k\ln W$) and **the spreading of energy** across them. Reach for "how many ways?" and "how spread out is the energy?", not "how messy?"

![[entropy-classroom-comic.png]]
*A better picture than "disorder," in three panels. **Scattered:** zillions of ways for kids to be spread around a room ($W$ huge) — so that's what you almost always see. **In one corner:** only a handful of ways ($W$ tiny) — possible, but you'd wait longer than the universe has existed. **The teacher's trick:** to force order *here* (a tidy line), the teacher does work, and the sound stirs the air into more disorder *there* — the room's **total** entropy still climbs. Entropy isn't "messiness"; it's* how many ways *— and you never beat the second law, you just relocate the mess.*

## Worked examples

**Example 1 — Melting ice (entropy created by a real flow).** $1.0\ \text{kg}$ of ice at $0\,^\circ\text{C} = 273\ \text{K}$ melts by absorbing $Q = mL_f = (1.0)(3.34\times10^5) = 3.34\times10^5\ \text{J}$ from a room at $273\ \text{K}$ (take the transfer as reversible at the melting point):
$$\Delta S_{\text{ice}} = \frac{Q}{T} = \frac{3.34\times10^5}{273} \approx +1.22\times10^3\ \text{J/K}.$$
The ice's entropy rises by over a kilojoule per kelvin — the water molecules, freed from the lattice, now have vastly more arrangements available.

**Example 2 — The Carnot ceiling on a power station.** A steam plant runs its boiler at $T_h = 810\ \text{K}$ and rejects heat to a river at $T_c = 300\ \text{K}$. The best conceivable efficiency is
$$\eta_C = 1 - \frac{300}{810} \approx 0.63 = 63\%.$$
Real plants reach ~40%. The other ~60% is not waste anyone *chose* — a good chunk is the second law's unavoidable toll, and the rest is the gap between a real cycle and the ideal reversible one. (This is also why a car engine turns barely a third of its petrol into motion.)

**Example 3 — The information in a free expansion.** One mole ($N = N_A = 6.0\times10^{23}$) of gas expands freely to twice its volume. Then
$$\Delta S = Nk\ln 2 = (6.0\times10^{23})(1.38\times10^{-23})(0.693) \approx +5.8\ \text{J/K},$$
which, converted to bits, is $N = 6.0\times10^{23}$ bits — one per molecule, the answer to "which half were you in before?" now permanently scrambled.

## Beyond syllabus

- **The third law completes the joke.** As $T \to 0$, a perfect crystal approaches a single microstate ($W\to 1$, $S\to 0$: **Nernst's theorem**). A corollary is that absolute zero is **unreachable** in finitely many steps — the third leg of the physicists' summary: *first law, you can't win; second law, you can't break even; third law, you can't get out of the game.*
- **Free energy — why reactions go.** At constant temperature and pressure the quantity that must decrease is not entropy alone but the **[[Gibbs Free Energy|Gibbs free energy]]** $G = H - TS$ (with $H$ the [[Enthalpy|enthalpy]]): a process is spontaneous when $\Delta G < 0$, balancing energy's pull downhill against entropy's pull toward multiplicity. It is the criterion that governs every chemical reaction, protein fold, and battery.
- **Black holes are the most entropic objects there are.** Bekenstein and Hawking found that a black hole carries entropy $S = \dfrac{k c^3 A}{4 G \hbar}$ — proportional to the *area* $A$ of its horizon, not its volume. This single formula welds thermodynamics, gravity, and quantum theory, forces black holes to slowly evaporate (**Hawking radiation**), and seeds the *holographic principle*: the deepest frontier where the entropy we met counting molecules in a box turns out to be counting the information capacity of spacetime itself.

## Exam Notes

- **IB Physics — B.4.3 + B.4.4 (HL only).** B.4.3: the second law in Clausius, Kelvin, and entropy forms; entropy change $\Delta S = \Delta Q / T$; the entropy of an isolated system cannot decrease. B.4.4: heat engines and thermal efficiency $\eta = W/Q_h$; the Carnot cycle and Carnot efficiency $\eta_C = 1 - T_c/T_h$. Always work in **kelvin**, and remember $\Delta S = Q/T$ is for a *reversible* transfer.
- **AP Physics 2 — §9.6 (Entropy and the Second Law).** Qualitative and semi-quantitative: entropy as a measure of the number of microstates / energy dispersal, $\Delta S \ge 0$ for an isolated system, why heat engines cannot be 100% efficient, and reading the direction of spontaneous processes from entropy. AP writes internal energy as $E_{\text{int}}$.
- **Not on Cambridge 9702** — the 9702 thermodynamics topic stops at the [[First Law of Thermodynamics|first law]] (§16.2). Entropy and the second law are an IB HL and AP topic only.
- **Traps:** entropy *can* fall locally (refrigerators, life) as long as it rises more elsewhere; efficiency and $\Delta S$ demand absolute temperature; "disorder" is a metaphor, "microstate count / energy spread" is the physics.

## Connections

- **Prerequisites:** [[First Law of Thermodynamics]] — the cyclic-area heat engine seeded there is limited here; [[Internal Energy]] — $U$ is conserved round a cycle, forcing $W = Q_h - Q_c$; [[Kinetic Theory and the Ideal Gas]] — the molecular picture whose microstates $W$ counts.
- **Dual residency:** [[Stories/Boltzmann's Tombstone]] — the human drama, the $S=k\ln W$ counting, *why* the logarithm, and the reversibility/recurrence paradoxes; the pedagogy (statements, $Q/T$, heat engines, Carnot) lives here.
- **The information bridge:** [[Information Theory]] — $S=k\ln W$ and $H=-\sum p\log p$ are one object; entropy is missing information, and [[Logarithms|the logarithm]] is forced by additivity in both. Seeds [[Maxwell's Demon]] (the thermodynamics-of-computation crossing).
- **Toward chemistry:** [[Gibbs Free Energy]] + [[Enthalpy]] — where $\Delta S$ meets energy to decide which reactions run (a bay the vault hasn't opened yet).
- **The statistics underneath:** [[Normal Distribution]] — the Maxwell–Boltzmann speed distribution and the sharply-peaked multiplicity are the same central-limit machinery.

## Where it came from

- **Sadi Carnot**, 1824 — *Réflexions sur la puissance motrice du feu*, the efficiency limit of engines, found *before* the first law existed and while heat was still "caloric." The most prophetic wrong-framework result in physics.
- **Rudolf Clausius**, 1850–1865 — the first and second laws in modern form; coined **entropy** (1865) and wrote the "energy constant, entropy tends to a maximum" couplet.
- **William Thomson (Lord Kelvin)**, 1851 — the Kelvin–Planck statement and the absolute temperature scale the whole subject runs on.
- **Ludwig Boltzmann**, 1872–1877 — entropy as $\propto \log W$, statistical mechanics, the H-theorem; the physics later carved (in Planck's form, with Planck's constant $k$) on his grave.
- **Walther Nernst**, 1906 — the third law. **Claude Shannon**, 1948 — information entropy. **Rolf Landauer**, 1961 — the thermodynamic cost of erasing a bit.

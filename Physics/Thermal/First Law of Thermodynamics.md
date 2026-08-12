---
chinese: 热力学第一定律 (rèlìxué dì-yī dìnglǜ)
prerequisites:
  - "[[Internal Energy]]"
  - "[[Kinetic Theory and the Ideal Gas]]"
  - "[[Work, Energy and Power]]"
  - "[[Specific Heat Capacity]]"
leads_to:
  - "[[Entropy and the Second Law]]"
tags:
  - subject/physics
  - domain/thermal-physics
  - level/A-Level
  - curriculum/Cambridge-9702
  - curriculum/A-Level
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-16-2
  - type/law
  - type/derivation
  - notation/U-internal-energy
  - notation/Q-heat
  - notation/W-work-on-system
  - misconception/heat-is-a-substance
  - misconception/work-sign-convention
  - misconception/heat-equals-internal-energy
  - misconception/adiabatic-equals-isothermal
  - misconception/gas-work-only-at-constant-pressure
---

# First Law of Thermodynamics  热力学第一定律

> *"You can't win."* — the first law, as physicists tell the joke (you can't get more energy out than you put in).
>
> *Heat is not a substance a body contains. It is energy caught in the act of crossing a boundary.*

On his honeymoon in the Alps in 1847, James Joule is said to have carried a thermometer to the base of a waterfall, hoping to catch the water arriving a hair warmer than it left the top — the gravitational energy of the fall reappearing as heat. The measurement was hopeless (spray and air ruin it), but the *idea* was the revolution. For a century heat had been imagined as an invisible fluid, "caloric," that objects held and poured. Joule's paddle-wheel — a falling weight churning water through vanes, warming it by a measurable amount — proved something stranger and simpler: **heat and mechanical work are the same currency.** A fixed number of joules of work always makes the same number of joules of heat.

Once heat is *energy*, the law of conservation of energy — already the spine of [[Work, Energy and Power|mechanics]] — simply grows one more term to account for it. That extended conservation law is the **first law of thermodynamics**, and in one line it says:

$$\boxed{\;\Delta U = Q + W\;}$$

The [[Internal Energy|internal energy]] $U$ of a system changes only by what crosses its boundary: heat $Q$ flowing in, and work $W$ done on it. Nothing else. No energy appears from nowhere; none vanishes. The whole of thermodynamics is the working-out of that sentence.

## 中文锚点

**核心论题**：热力学第一定律就是**能量守恒**，只不过把"热"也算作一种能量传递方式。系统的[[Internal Energy|内能]] $U$（一个**状态函数**——只看现在的状态，不看走过的路）只能通过两扇门改变：**吸热 $Q$** 和**外界对它做功 $W$**：

$$\Delta U = Q + W.$$

关键在于**符号约定**（考试最容易错的地方）：先记原理——**能量进入系统为正，离开为负**。本卡片用 $\Delta U = Q + W$，其中 $W$ 是**外界对气体**做的功；气体被压缩时 $W>0$（能量进入），膨胀时 $W<0$。气体做功 $W_{\text{on}} = -p\,\Delta V$，几何上就是 **$p$–$V$ 图曲线下的面积**（带符号）。

四种基本过程：**等温**（$\Delta U=0$，吸的热全变成功）、**等压**（$W=-p\Delta V$）、**等容**（$W=0$，吸的热全变内能）、**绝热**（$Q=0$，做功直接改变内能——打气筒发热、柴油机压燃就是它）。

绕一圈回到起点（**循环**）时 $\Delta U=0$，所以**净热 = 净功 = $p$–$V$ 图围成的面积**——这正是热机的种子，通往[[Entropy and the Second Law|第二定律]]与[[Stories/Boltzmann's Tombstone|熵]]。第一定律说"你赢不了"（能量守恒），第二定律说"你连平局都打不成"。

---

## The statement: internal energy has two doors

The [[Internal Energy]] card established $U$ as a **state function** — the *bank balance* of a system, fixed by its present state (for an ideal gas, by $T$ alone) and blind to how it got there. The first law now tells you the *only two kinds of transaction* that can change that balance.

- **$Q$ — heat.** Energy that crosses the boundary because of a **temperature difference**. Heat is a *verb*, not a noun: a body never "contains heat," it contains internal energy, and heat is energy in transit through the wall.
- **$W$ — work.** Energy that crosses the boundary because a **force moves through a distance** — a piston compressing the gas, the gas pushing a piston out.

$$\Delta U = Q + W.$$

Here is the quiet miracle. Take a gas from state $A$ to state $B$ by two different routes — compress-then-heat, or heat-then-compress. The heat $Q$ is different on the two routes. The work $W$ is different on the two routes. **Both are path-dependent.** Yet their *sum* $Q + W = \Delta U = U_B - U_A$ comes out **identical**, because $U$ is a state function and cares only about the endpoints. Heat and work are two rivers that each wander, but the total they deliver into the lake is fixed. That constraint — path-dependent parts, path-independent sum — *is* the first law's content, and it is why $U$ deserves to be called energy at all.

## Sign conventions — the one thing to get right

More marks are lost to a wrong sign here than to any real misunderstanding. So state the **principle** first, and let the convention be its bookkeeping:

> **Principle:** energy *entering* the system counts **positive**; energy *leaving* counts **negative.**

With $\Delta U = Q + W$ and $W$ defined as the **work done *on* the system**:

| Quantity | Positive when… | Negative when… |
|---|---|---|
| $Q$ | heat flows **in** (system heated) | heat flows **out** (system cooled) |
| $W$ | work done **on** the gas (compressed) | gas does work (expands) |
| $\Delta U$ | internal energy **rises** ($T$ up, for ideal gas) | internal energy **falls** |

> [!warning] Two conventions, one physics
> Some books (especially older engineering texts) write the first law as $\Delta U = Q - W$, where their $W$ is the work done **by** the system. That is the *same law* — they have just flipped the sign of $W$ by defining it outward instead of inward. Cambridge 9702, IB, and AP all use $\Delta U = Q + W$ with $W$ = work done **on** the gas. Don't memorise a sign; **fall back on the principle** — ask "did this transfer *add* energy to the gas or *take it away*?" and let the answer set the sign. The mnemonic serves the principle, never the reverse.

## Work done on a gas: $W = -p\,\Delta V$

Where does the work term actually come from? A gas at pressure $p$ pushes on a piston of area $A$ with force $F = pA$. If the piston moves out by a small distance $\mathrm{d}x$, the gas does work $p A\,\mathrm{d}x = p\,\mathrm{d}V$ **on the surroundings.** The work done **on the gas** is the negative of that:

$$W = -\int p\,\mathrm{d}V.$$

Two consequences worth carrying:

- **At constant pressure**, $W = -p\,\Delta V$. Expansion ($\Delta V > 0$) means the gas does work outward, so $W < 0$ — energy leaves the gas. Compression pumps energy in.
- **In general**, $-\int p\,\mathrm{d}V$ is **minus the area under the curve on a $p$–$V$ diagram.** The path matters because the area under two different routes between the same endpoints is different — which is exactly why work is path-dependent.

![[first-law-energy-ledger.svg|697]]
*The ledger. Internal energy is the balance in the box; heat and work are the only two transactions that change it. Arrows in are positive, arrows out are negative — the whole sign convention is "which way does the arrow point?"*

## The $p$–$V$ diagram and the four processes

Almost every first-law problem is one of four idealised paths. Read each as: *apply a constraint, watch one term vanish, and the first law collapses to something simple.*

![[first-law-pv-processes.svg|640]]
*The four canonical processes from a common start point. **Isothermal** (red) rides a $pV=\text{const}$ hyperbola — same temperature throughout. **Adiabatic** (purple) is a steeper $pV^\gamma=\text{const}$ curve — no heat exchanged, so expansion must cool the gas. **Isobaric** (green) is horizontal (constant $p$); **isochoric** (blue) is vertical (constant $V$, so no work).*

| Process | Held constant | What vanishes | First law becomes | Everyday case |
|---|---|---|---|---|
| **Isochoric** (constant $V$) | volume | $W=0$ (no $\Delta V$) | $\Delta U = Q$ | heating a sealed rigid can |
| **Isobaric** (constant $p$) | pressure | — | $\Delta U = Q - p\,\Delta V$ | gas heated under a free piston |
| **Isothermal** (constant $T$) | temperature | $\Delta U=0$ (ideal gas) | $Q = -W$ | slow expansion in a warm bath |
| **Adiabatic** (no heat) | — | $Q=0$ | $\Delta U = W$ | bike-pump / diesel compression |

Two of these are the pedagogical jewels:

- **Isochoric — heat becomes pure internal energy.** Bolt the volume shut and $W=0$: every joule of heat goes straight into $U$, so $Q = \Delta U = nC_V\Delta T$. This is the cleanest possible definition of $C_V$.
- **Adiabatic — work becomes pure internal energy.** Wrap the walls so no heat escapes ($Q=0$) and $\Delta U = W$. Compress the gas and its internal energy — hence its **temperature** — *must* rise, with no flame anywhere near it. That is why a bicycle pump warms in your hand, and why a **diesel engine** needs no spark plug: it compresses air so fast and so hard that the temperature leaps past the fuel's ignition point. Run it backwards — let a gas expand adiabatically — and it **cools**, which is how a rising parcel of air makes a cloud and how a spray can chills as it empties.

> [!warning] Adiabatic ≠ isothermal
> A tempting error: "no heat added, so the temperature stays the same." Exactly wrong. *Isothermal* holds $T$ fixed **by** letting heat flow in or out. *Adiabatic* forbids heat flow, so the temperature is *free to move* — and it does, because the work has nowhere to go but into $U$. The two are opposites, and on the $p$–$V$ diagram the adiabat is always the **steeper** curve.

![[first-law-four-processes-comic.png]]
*The same four processes as everyday scenes — watch the thermometer in each. **Isochoric:** a bolted, rigid can on a fire; nothing moves, so every joule of heat becomes temperature. **Isobaric:** a free piston with a weight on top; heat both warms the gas and lifts the load. **Isothermal:** a cylinder in a warm bath; the bath trades heat in for work out and the temperature never budges. **Adiabatic:** an insulated pump squeezed fast; no heat crosses the wall, yet the compression alone drives the temperature up. The bottom banner is the whole misconception in one line — **"no heat added" is not the same as "same temperature."***

## Cycles: where the work comes from

Run a gas around a **closed loop** on the $p$–$V$ diagram — back to exactly where it started. Because $U$ is a state function, $\Delta U = 0$ over the whole cycle. The first law then forces

$$Q_{\text{net}} = -W_{\text{net}} = \text{area enclosed by the loop.}$$

A clockwise loop takes in more heat than it dumps and delivers the difference as **net work outward** — that is a **heat engine**, and the enclosed area is its work per cycle. This is the hinge where the first law hands off to the next question: the first law says the books must balance, but it does *not* say heat will politely turn *all* the way back into work. It won't. Why some of that energy can never be recovered — why the arrow of a cycle has a preferred direction at all — is the domain of [[Entropy and the Second Law|the second law]] and of [[Stories/Boltzmann's Tombstone|entropy]].

## Why it is true — conservation, with heat let in

The first law is not a new principle. It is **conservation of energy**, from the moment you accept Joule's discovery that heat is a form of energy transfer rather than a fluid. Before ~1845, "caloric" was thought conserved on its own; Rumford (boring cannon in 1798, watching friction make apparently limitless heat) and then Joule, Mayer, and Helmholtz (who stated general energy conservation in 1847) dismantled that. Once heat joined kinetic, potential, and every other energy in one ledger, the *total* became the true invariant — the deepest "what doesn't change?" in physics (see [[Work, Energy and Power]]).

The physicists' one-line summary of the whole subject is a joke about a game you can't win:

- **First law — "you can't win."** You cannot get more energy out than you put in; energy is conserved.
- **Second law — "you can't break even."** You cannot even convert all your heat back into work; some is always lost to entropy.
- **Third law — "you can't quit the game."** You cannot reach absolute zero.

The first law's own veto is on the **perpetual-motion machine of the first kind** — any device claiming to output energy from nothing. It cannot exist, because $\Delta U = Q + W$ leaves no term for energy created out of the void.

## Worked examples

**Example 1 — Why $C_p > C_V$ (the flagship first-law application, previewed in [[Specific Heat Capacity]]).**
Heat one mole of monatomic ideal gas by $\Delta T$ two ways.

*At constant volume:* $W = 0$, so all the heat becomes internal energy:
$$Q_V = \Delta U = \tfrac{3}{2}R\,\Delta T \quad\Rightarrow\quad C_V = \tfrac{3}{2}R.$$

*At constant pressure:* the gas expands as it warms, doing work on the surroundings. The internal-energy rise is the **same** (it depends only on $\Delta T$), but now the heat must also pay for the expansion work $p\,\Delta V = R\,\Delta T$ (from $pV = RT$):
$$Q_p = \Delta U + p\,\Delta V = \tfrac{3}{2}R\,\Delta T + R\,\Delta T = \tfrac{5}{2}R\,\Delta T \quad\Rightarrow\quad C_p = \tfrac{5}{2}R.$$

So $C_p - C_V = R$ (**Mayer's relation**) — not a coincidence but the first law made numerical: constant-pressure heating costs one extra $R\,\Delta T$ per mole *because that energy walks out of the system as expansion work.*

**Example 2 — Adiabatic compression (the diesel intuition).**
Air is compressed rapidly ($Q \approx 0$) and $250\,\text{J}$ of work is done on it. Find $\Delta U$ and say what happens to the temperature.
$$\Delta U = Q + W = 0 + 250 = +250\,\text{J}.$$
Internal energy rises by $250\,\text{J}$; since $U \propto T$ for an ideal gas, the temperature **rises** — the compression alone heats the air, exactly the mechanism that ignites diesel fuel with no spark.

**Example 3 — An isothermal expansion.**
One mole of ideal gas expands slowly at constant $T = 300\,\text{K}$ from $V_1$ to $V_2 = 2V_1$. Then $\Delta U = 0$ (temperature fixed), so by the first law $Q = -W$. The gas does work outward $-W = \int p\,\mathrm{d}V = RT\ln(V_2/V_1) = (8.31)(300)\ln 2 \approx 1.7\times10^3\,\text{J}$, and **exactly that much heat must flow in** from the bath to keep the temperature from dropping. Energy passes straight through the gas: in as heat, out as work, with the internal-energy balance untouched.

## Beyond syllabus

- **Heat and work are not equal citizens.** The first law treats $Q$ and $W$ symmetrically — both just change $U$. But they are not interchangeable in practice: **work can be converted entirely into heat** (friction, Joule's paddle) while **heat can never be converted entirely into work.** Work is *ordered* energy transfer, heat is *disordered*. That asymmetry is invisible to the first law and is the entire content of the second — the reason [[Stories/Boltzmann's Tombstone|entropy]] and [[Information Theory|information]] turn out to be the same idea.
- **[[Enthalpy]].** Chemists, who mostly work at constant atmospheric pressure, bundle the expansion-work term into a new state function $H = U + pV$, so that $\Delta H = Q_p$ — the heat of a constant-pressure reaction. It is the first law wearing a lab coat, and it is where thermodynamics crosses the hall into chemistry.
- **The adiabatic curve.** For a reversible adiabatic change, $pV^{\gamma} = \text{const}$ with $\gamma = C_p/C_V$ — steeper than the isotherm $pV = \text{const}$ by exactly the factor $\gamma$, which is *why* the purple curve outruns the red one on the diagram.
- **The universe's ledger.** Applied to an isolated system with no boundary to cross, $\Delta U = 0$: the total energy of an isolated system is constant. Whether that statement holds for the expanding universe as a whole is subtle (energy conservation and general relativity make uneasy neighbours) — a genuine research-level caveat, not a school one.

## Exam Notes

- **Cambridge 9702 — §16.2.** The core home. State the first law $\Delta U = Q + W$ (their $W$ is work done **on** the system; some papers write $q$ for heat). Know $W = -p\,\Delta V$ at constant pressure and the sign conventions cold — the classic structured question defines internal energy in part (a) via [[Internal Energy]] §16.1 and applies the first law to a process in part (b). Adiabatic/isothermal *reasoning* is expected; the $pV^\gamma$ equation is **not** required here.
- **IB Physics — B.4.1 (HL only).** The whole of B.4 Thermodynamics is Higher Level. Required: $\Delta U = Q + W$ with the sign convention, and reading **work done by/on a gas as the area under the $p$–$V$ curve.** The theme's next step is B.4.3 — the second law and entropy.
- **AP Physics 2 — §9.4.** Algebra-based $\Delta U = Q + W$; interpret $p$–$V$ diagrams, identify the four processes, and compute work as area. Leads straight into §9.6 (entropy and the second law). AP often writes internal energy as $E_{\text{int}}$.
- **Universal trap:** the sign of $W$. Decide it from the principle (energy in $=+$), not a memorised formula, and adiabatic-is-not-isothermal.

## Connections

- **Prerequisites:** [[Internal Energy]] — the state function $U$ this law spends (defines $\Delta U = \tfrac32 nR\,\Delta T$ for an ideal gas); [[Kinetic Theory and the Ideal Gas]] — supplies $pV = nRT$, needed for the expansion-work term; [[Work, Energy and Power]] — the parent conservation law that the first law extends by admitting heat.
- **Sibling:** [[Specific Heat Capacity]] — previews $C_p - C_V = R$ as its "appetiser"; here the same result is the flagship application of the law that governs it (Example 1).
- **Leads to:** [[Entropy and the Second Law]] — the first law says the books balance; the second says heat won't fully return as work. The cyclic-process area here is the heat engine that the second law then limits.
- **Payoff ahead:** [[Stories/Boltzmann's Tombstone]] + [[Information Theory]] — entropy as counting, the statistical meaning of the "lost" energy the first law cannot see.
- **Sibling analogy:** [[Simple Harmonic Motion]] — adiabatic compressions and rarefactions are what carry a **sound wave**, the pressure oscillation the first law governs locally.

## Where it came from

- **Benjamin Thompson (Count Rumford)**, 1798 — boring cannon in Munich, arguing from the seemingly endless frictional heat that heat could not be a conserved fluid.
- **Julius Robert von Mayer**, 1842 — first stated the mechanical equivalent of heat, from the $C_p - C_V$ gap of gases; long ignored.
- **James Prescott Joule**, 1843–1850 — the paddle-wheel experiments fixing $1\,\text{cal} \approx 4.15\,\text{J}$; the honeymoon-waterfall attempt is the affectionate legend attached to the obsession.
- **Hermann von Helmholtz**, 1847 — *Über die Erhaltung der Kraft*, the general statement of energy conservation that made the first law a theorem of all physics, not just of gases.

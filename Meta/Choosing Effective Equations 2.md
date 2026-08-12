---
chinese: 选取有效方程 (xuǎnqǔ yǒuxiào fāngchéng) / 选公式的艺术
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Linear Momentum]]"
  - "[[Forces and Equilibrium]]"
  - "[[SUVAT]]"
  - "[[Work, Energy and Power]]"
  - "[[Kinematics Calculus]]"
  - "[[Chain of Thought]]"
leads_to:
  - "[[Forward Reading and Problem Discovery]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - domain/problem-solving
  - level/A-Level
  - curriculum/Cambridge-9709
  - curriculum/Cambridge-9702
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - type/methodology
  - type/meta
  - type/exam-technique
  - misconception/picks-equation-before-reading-fully
  - misconception/F-equals-ma-on-collision
  - misconception/SUVAT-when-a-is-not-constant
  - misconception/backward-only-reasoning
---

# Choosing Effective Equations 选取有效方程

## What this card is for

When a student reads an M1 question and **freezes** — stares at the page, doesn't know where to start, eventually writes the wrong equation and runs out of marks — what they're missing isn't *content*. It's a *navigation skill* that sits *above* every individual topic.

This card is that skill, made explicit.

It will not teach you N2, momentum conservation, SUVAT, or the work-energy theorem — those each have their own deep card (linked in the prerequisites). What this card does is teach you to **read a question, identify which framework the problem is set up for, and pick the minimal equation set that solves it**. Two distinct sub-skills, two layers.

> [!info] Scope — when this card matters
> This card is narrowly aimed at **Cambridge 9709 Paper 4 (Mechanics)** and equivalent multi-topic mechanics papers (A-Level Mechanics 1 / 2, IB AA Mechanics, AP Physics 1 / C: Mechanics). Single-topic exams (most of 0606, 0580, 9702 with one chapter at a time) don't have this problem — the topic *is* the framework, no recognition required. M1-style papers are the case where one question can cycle through SUVAT, momentum, energy, and N2 in seven marks. *That's* where the skill earns its keep.

### 中文锚点

**选取有效方程 (xuǎnqǔ yǒuxiào fāngchéng)** = M1-style 力学题里"选对方程"的艺术。

考试关键：
- 这张卡片**不教任何具体公式**，每个公式都有自己的深度卡片
- 教的是**两层导航技能**：
  - **第一层 — 认框架**：读题，识别这道题适合哪个物理框架（SUVAT / 动量守恒 / 能量法 / 功率 / N2 / 等等）
  - **第二层 — 选方程**：在选定的框架里，数清未知数 → 列出可用方程 → 挑最少能解的那一组
- 适用于 9709 P4 / A-Level Mechanics / IB AA / AP Physics 这类**多专题混合**的考卷；0580 / 0606 / 9702 单章考题不需要这个技能（章节本身就是框架）

---

## Layer 1 — Framework Recognition

Read the question. *Before writing any equation*, decide which physics framework the problem is set up for. M1 questions select from this menu:

### The trigger-phrasing table

| Framework | Trigger phrasing in the question | Why it's the right tool |
|---|---|---|
| **SUVAT (constant *a*)** | "starts from rest", "constant acceleration", "decelerating uniformly", "v–t graph", explicit "use SUVAT" | Constant *a* makes the five formulae exact — fastest path |
| **Variable-*a* calculus** | "$v=$ polynomial in $t$", "$a = kt^n$", "$\dot s$, $\ddot s$" | Non-constant *a* — must integrate / differentiate; SUVAT *fails* here |
| **N2 ($F = ma$) force balance** | "find acceleration / tension", masses given, forces given (or derivable), "connected particles" | Bodies + forces + masses given, motion to predict |
| **Equilibrium ($\Sigma F = 0$)** | "in equilibrium", "remains at rest", "constant speed", "in limiting equilibrium" | $a = 0$, so net force / net moment is zero |
| **Friction at the limit** | "rough", "coefficient of friction", "greatest value", "find $\mu$", "about to slip" | $F = \mu N$ at limiting equilibrium / kinetic |
| **Momentum conservation** | "collide", "coalesce", before-and-after speeds with masses, "direct impact" | Collision force is short-lived and unknown — F=ma is *unusable*; momentum is preserved |
| **Power $P = Fv$** | "engine working at rate", "constant power", "steady speed", "maximum speed" | Constant-power or constant-velocity is asserted |
| **Work–energy theorem** | "work done against resistance", "find KE", **"use an energy method"** (explicit cue) | Distance + speed change given, time *not* given → energy beats SUVAT |
| **Energy conservation (KE↔GPE)** | "from height $h$ at rest to speed $v$", "drops a vertical distance", smooth surface implied | Gravitational PE ↔ KE; bypasses force decomposition |

The **trigger-phrasing column is the cheat-sheet you internalise.** A student who reads "engine working at constant rate of 8 kW" and immediately thinks "*power problem; $P = Fv$; if there's a steady speed asserted, force balance gives me the resistance*" has done in three seconds what a frozen student spends three minutes on.

> [!tip] Cambridge tells you in the wording
> The most reliable framework cues are *Cambridge's own idioms*. The phrase **"use an energy method"** explicitly tells you to set up KE / PE / work, not SUVAT or N2. **"Constant power"** explicitly tells you $P$ is fixed and the equation will involve $P/v$. **"Coalesce"** explicitly tells you it's a perfectly inelastic collision and only momentum conservation applies. Read for these phrases on the first pass *before* committing to a method.

---

## Layer 2 — Forward Reading: Find What Doesn't Change

Once you know which framework the question lives in, the actual solving skill is **reading the question forward, sentence by sentence, and labelling each clause with what it just locked down**. *You are not reverse-engineering a target equation set from the unknowns.* You are *collecting invariants* as you read — quantities and constraints that don't change throughout the problem — and by the time you reach the question itself, the answer has usually already lit up.

This is the same idea as the **注意力 (attention) framing** in [[Product Rule]] and [[Chain Rule]]: every piece of structure you grab while reading is one attention slot. Read economically, grab only what's load-bearing, and you'll have attention left to spend on the actual computation when it arrives.

### The forward-mode skill — read for invariants

For each sentence in the question, ask: *what just got pinned down? what does this clause promise won't change?* Some examples of what you can grab from common Cambridge phrasings:

| Phrasing | Invariant / constraint it gives you |
|---|---|
| "On a smooth surface" | No friction → mechanical energy is conserved between events |
| "Light inextensible string" | $T$ uniform along the rope; $\lvert a \rvert$ same on both bodies; rope length constant (a *displacement* constraint) |
| "Smooth peg / smooth pulley" | $T$ same on both sides of the redirect |
| "From rest" | $u = 0$ |
| "Released from rest" | Initial KE = 0 |
| "Constant power" | $P$ fixed; $F \cdot v = $ const → $F = P/v$ |
| "Steady speed" / "constant speed" | $a = 0$ → forces (or driving force = resistance) balance |
| "Until they coalesce" | Final velocities of the two bodies are equal |
| "Along the same line" | 1D — no perpendicular components matter |
| "Along the same line of greatest slope" | All motion along the slope axis; perpendicular components in equilibrium |
| "On the same horizontal level" | $\Delta h = 0$ → no GPE change |
| "Same instant" | Two motions can be linked by a common $t$ |
| "Reaches the barrier 0.4 s after the collision" | Total time of phase 2 = 0.4 s (a kinematic constraint) |
| "Use an energy method" | Cambridge has just *told* you the framework |
| "Speed reduced by 90%" | Multiplicative constraint: $v_{\text{after}} = 0.1 v_{\text{before}}$ |

Every invariant you grab is one *equation-in-waiting*. The trick is to be *promiscuous* about grabbing them while you read — every clause has at least one — and *economical* about not grabbing decorative detail.

> [!info] "Conservation" generalised
> The word *conservation* in M1 usually means energy or momentum, but what's actually doing the work is the broader idea: *something doesn't change from one moment to the next, and that gives you an equation.* Energy and momentum are the famous cases, but a "light inextensible string" is also a conservation statement — *length is conserved*. "Constant power" is conservation of $P$. "Same instant" is conservation of $t$ across two motions. The skill is hearing every clause as *some quantity locked down*, named or unnamed.

### When to switch to backward mode

For roughly 80% of M1 questions, the forward-reading pass alone gives you enough invariants that the asked quantity is one substitution away by the time you finish reading. For the remaining 20% — the harder multi-step problems — you may not yet see the through-line, and a *small amount* of backward reasoning helps:

> **Backward question to ask, sparingly:** "What equation involves the quantity I'm asked to find, that I haven't written yet?"

Then look back at your collected invariants and find which one matches. Backward reasoning on its own (count unknowns, list available equations, pick the minimal set) works but is slow and bureaucratic. Forward reasoning on its own occasionally misses a needed equation. The actual practice is **forward-dominant with a small backward sanity-check at the end** — both modes running, forward grabbing invariants and backward asking "do I have what I need yet?"

This is the deeper version of the 注意力 framing (see [[Product Rule]] for where the metaphor first lands): by the time you reach the question, you've spent ~70% of your attention on invariant-grabbing while reading. The remaining ~30% is enough to solve, *because the invariants are already on the page*.

### Three execution tricks once you have the equations

Forward reading gives you the *invariants* (your equations). When you then write them down, three signature tricks keep the algebra short:

**Strategic-pivot trick** (for moment problems): take moments about a point where unknown forces act → those forces have zero moment arm → they vanish from the equation. Beam problems live and die by this. The "real" pivot of the system has no special privilege — pick the pivot to *eliminate* the most unknowns.

**Tilted-axes trick** (for inclined-plane and resolved-force problems): pick axes that align with the unknown directions. Some forces become axis-aligned and zero out of the perpendicular axis. On a slope, axes along/perpendicular to the slope reduce three forces to two scalar equations cleanly.

**Add-the-equations trick** (for connected particles): write N2 on each body separately. The internal force (tension, contact force) appears in both with opposite signs. *Add* the two equations and the internal force *cancels* — leaving one equation with only the external forces and the common acceleration. This is the single biggest algebra-saving on pulley problems.

---

## Worked example — forward-reading a real M1 question

Let's apply forward reading to a realistic M1 question and watch the invariants accumulate.

> *Two particles A (0.5 kg) and B (0.3 kg) are connected by a light inextensible string. The string is taut and A is vertically above B. A force of magnitude 10 N is applied to A vertically upwards. Find the acceleration of the particles and the tension in the string.* — adapted from J22 P41 Q2

**Step 0 — draw something. Anything.** The first move on any M1 question is a quick sketch. *Sketch* is the right word: the diagram below is what an exam student would actually scrawl in the margin — two boxes, a string, the applied force, a direction marker, the words "find a, T" so they remember what to come back to. It is not a full free-body diagram, the weight arrow is half-finished, and there's no $T$ written on the string. None of that matters. The diagram exists to hold the geometry on the page so the reader's brain can spend its attention on physics, not on remembering "wait, which one was on top?". Any diagram, however ugly, is better than none — every label you can outsource to ink is one slot of attention freed for the actual problem.

![[choosing-equations-q2-two-particles.svg|697]]

Read it forward, one clause at a time. The invariant column is what the experienced solver hears:

| Clause read | Invariant grabbed |
|---|---|
| "Two particles A (0.5 kg) and B (0.3 kg)…" | masses fixed: $m_A = 0.5$, $m_B = 0.3$ |
| "…connected by a light inextensible string." | *Light* → $T$ uniform along the rope. *Inextensible* → $\lvert a \rvert$ same for both bodies. |
| "The string is taut…" | the constraint is currently active (we can use both invariants above) |
| "…A is vertically above B." | 1D problem (vertical only). Direction of motion same for both bodies along the rope. |
| "A force of magnitude 10 N is applied to A vertically upwards." | $F_{\text{ext, A}} = 10$ N upward. (Together with weights $m_A g$, $m_B g$ also downward, this is the full force census.) |
| "Find the acceleration of the particles and the tension in the string." | the question — and we already have everything. |

By the time we finish reading, we have a closed system: same $a$, same $T$, three external forces, two bodies. Two N2 equations (one per body) close the unknown count. The execution:

- N2 on A (up positive): $10 - T - 0.5 g = 0.5 a$
- N2 on B (up positive): $T - 0.3 g = 0.3 a$
- Add: $10 - 0.8 g = 0.8 a$ → $a = (10 - 8)/0.8 = 2.5$ m/s² (with $g = 10$).
- Substitute back: $T = 0.3 (g + a) = 0.3 \times 12.5 = 3.75$ N.

Notice the answer was implicit by the time the question appeared. The forward-reading pass had already collected: masses, the connection constraints (same $T$, same $|a|$), the dimensional restriction, and the external force. The "find" line just told us *which* of the now-derivable quantities to write down.

---

## Multi-Framework Chain Problems — The M1 Boss-Fight

The hardest M1 questions chain *several* frameworks across parts. Recognising the chain is itself a skill: the question's "(a) … then (b) … then (c) …" structure usually maps directly to a sequence of framework switches.

### Worked chain — J22 P41 Q7 (5 framework-switches in 7 marks)

The full Q7 setup: two particles A (0.4 kg) and B (0.2 kg) move down a smooth slope at 30°, A higher up than B. They collide; A's speed reduces from 3 m/s to 2.5 m/s. Then B moves 1.6 m down to a barrier in 0.4 s, hitting it at some speed; B's speed is reduced by 90% on impact and rebounds back up the slope; the two particles collide again 0.44 s after the first collision and coalesce.

> *Find the common speed of the two particles immediately after they coalesce.*

That single "find" line is what makes this question a 7-mark boss-fight. To get there, you have to navigate every single one of the five framework-switches below — there is no shortcut. Skipping any one of them and you can't even write down the momentum equation at the final coalescence, because you don't know either particle's velocity at that moment.

Same Step 0 as before — *sketch the geometry once*. The student doesn't redraw the slope five times for the five stages; they draw the slope and barrier and particles once, mark roughly where the collision happens, and keep one diagram open for the whole question. The framework chain itself ends up jotted as a single arrow-strip in the margin — five words tracking which physics applies at which stage:

![[choosing-equations-q7-chain.svg|697]]

The framework chain:

| Part | Question | Framework | Cue |
|---|---|---|---|
| 1 | Find B's speed *immediately after* the first collision | **Momentum conservation** | "collide" — the only law that works during the collision |
| 2 | B's motion from collision down the slope to the barrier | **SUVAT** with $a = g\sin 30° = 5$ m/s² | Constant acceleration on a smooth slope (N2 already gives the *a*; then SUVAT runs) |
| 3 | "B's speed is reduced by 90%" at the barrier | **Algebraic constraint** | Not a framework — just a multiplier ($v_{\text{new}} = 0.1 v_{\text{old}}$) |
| 4 | B's motion *back up* the slope + A's continued motion *down* → meeting time | **SUVAT (again)** on each particle separately | Smooth slope, constant *a* |
| 5 | The coalescing second collision | **Momentum conservation** | "coalesce" — perfectly inelastic |

Five framework-switches in one question, worth 7 marks total.

The student who freezes here is the student who tries to use *one* framework throughout. The student who navigates it cleanly is the one who reads the question and *recognises the structure* — momentum at collisions, SUVAT between them, an algebraic step at the barrier.

> [!tip] Decompose the question before writing
> For multi-part M1 problems, spend 30 seconds before writing anything: list the parts, label each with its framework. The chain becomes a *plan*, not a series of surprises. Cambridge mark schemes reward students who write the right framework even on the wrong page; they punish students who write the wrong framework even with neat algebra.

---

## Atlas — Canonical M1 Problem Types

A diagnostic table for "I read this question — what framework am I in?":

| Problem type | Frameworks (in order of use) | Trigger / give-away |
|---|---|---|
| Particle on smooth slope | N2 (resolve along/⊥) | "smooth slope" + "find acceleration" |
| Particle on rough slope at limit | N2 (along/⊥) + friction at limit | "rough" + "about to slip" / "find μ" |
| Connected particles, pulley | N2 on each + same *a* + same *T* | "light inextensible string", "smooth peg" |
| Beam in equilibrium | $\Sigma F = 0$ + moments about a strategic pivot | "in equilibrium" + multi-support / "find reaction" (9702 / 0625, not 9709) |
| Ladder against a wall | $\Sigma F_x = 0$, $\Sigma F_y = 0$, moments about foot | "ladder" + "leaning" + "rough floor / smooth wall" (9702 / 0625) |
| Crate at rest under angled push | $\Sigma F = 0$ + friction at limit | "remains at rest", "greatest value" + rough |
| Vehicle accelerating | N2 ± $P = Fv$ if power given | "driving force", "resistance", optionally "engine works at rate" |
| Vehicle at constant speed | $P = Fv$ + force balance | "steady speed", "maximum speed" |
| Variable-acceleration kinematics | Calculus: $v = \int a\,dt$, $s = \int v\,dt$, $a = dv/dt$ | $v(t)$ or $a(t)$ given as polynomial |
| Collision (any flavour) | Momentum conservation | "collide" / "coalesce" |
| Energy-method problem | Work-energy theorem or KE↔PE conservation | "use an energy method", PE drop given |
| Multi-stage motion (chain) | SUVAT segment → instantaneous switch (collision / barrier) → SUVAT segment | Given by the question's "(a) … (b) then …" structure |
| Slide / curved-section motion | Energy conservation (KE↔PE), often with friction work term | Smooth+curved or rough+curved sections; height given |

---

## Common Failure Modes

The pathologies of poor framework choice:

### 1. "I'll use F = ma on the collision"

You can't. The collision force is short-lived (~milliseconds), enormous, and unknown. There's no way to write $F = ma$ for the collision instant — you'd need the force, you don't have it, and even if you did the integration is intractable. *Momentum conservation* sidesteps the force entirely by integrating both sides of $F = dp/dt$ across the collision window: the integral of force is impulse, but for an *internal* collision force the impulses on the two bodies cancel by N3, so $\Delta(p_1 + p_2) = 0$. That's why momentum is the framework for collisions.

### 2. "I'll use SUVAT when *a* isn't constant"

SUVAT is the constant-*a* special case. If the question gives you $v(t)$ as a polynomial, or $a$ as a function of time, SUVAT fails — you must integrate. Common student mistake: read "$v = 4 + 2t - 3t^2$" and try to plug into $v = u + at$. That equation is only valid for constant *a*; here $a = -6t + 2$ varies. Use calculus.

### 3. "I'll use F = ma when energy is faster"

Two scenarios where energy methods are dramatically faster:
- *"Find speed at the bottom of a smooth ramp of height $h$":* energy conservation gives $v = \sqrt{2gh}$ in one line. F = ma + SUVAT gives the same answer in three lines (resolve along slope, find *a*, apply $v^2 = u^2 + 2as$ along slope length $h/\sin\theta$).
- *"Find mass given work done and speed reached":* one work-energy equation. F = ma route requires finding acceleration over an unknown distance — impossible without more information.

If the question says "use an energy method," it's *telling you* energy is the right tool. Listen.

### 4. "I'll start writing equations before I finish reading"

The single most common time-loss pattern. The student writes $v = u + at$ after reading only the first sentence, before the question's later clauses (which usually contain the most informative invariants — "constant power", "until they coalesce", "use an energy method") have been processed. They commit to a framework and an equation set on partial information, then have to backtrack when the rest of the question turns out to need a different framework.

The forward-reading discipline says: **read the whole question once before writing anything**. Grab invariants as you go, but don't commit to equations until the question itself appears. The answer is usually waiting in the invariants you've collected by that point.

### 5. "I'll change my framework mid-problem"

This is the multi-framework chain trap. Once you commit to "this is a momentum problem," the equations are momentum equations — don't introduce a stray $F = ma$ in the middle "to clean up." If the next part of the question needs a different framework, *finish the momentum part*, write the answer, and *then* switch frameworks for the next part with a clear new heading. Hybrid mid-problem framework-mixing is where mark-scheme penalties accumulate.

---

## Cross-Domain Bridge — The Same Skill, Other Subjects

The two-layer structure ("recognise the framework, then read forward for invariants and corollaries") is *not* specific to mechanics. Every applied subject has the same shape:

| Domain | Layer 1 framework choices | Layer 2 — what the forward read is collecting |
|---|---|---|
| **Mechanics** (this card) | SUVAT / N2 / momentum / energy / power | Invariants: same $T$, same $\lvert a \rvert$, $a = 0$, energy conserved, … |
| **Circuits** (A-Level / IB Physics) | Kirchhoff's voltage law / current law / Thevenin / Norton / energy method | Invariants: KCL at every node, KVL around every loop, $V$/$I$ at known sources |
| **Thermodynamics** | First law (energy) / second law (entropy) / equation of state / specific-heat | Invariants: isothermal ($T$ const), adiabatic ($Q = 0$), isobaric ($p$ const), isochoric ($V$ const) |
| **Statistics** (M1's sibling, 9709 P5) | Binomial / Poisson / Normal / discrete distribution / sampling | Invariants: $n, p$ fixed; mean rate constant; sample size; independence |
| **Optimisation / ML** | Linear programming / convex / non-convex / gradient descent | Invariants: feasible region's boundary, gradient = 0, KKT conditions |
| **Linear algebra (university)** | Rank-nullity: how many free parameters does the system have? | Invariants: which rows are linearly dependent? what does the kernel look like? |

The deep claim: *"read the question forward, find what doesn't change, and the answer is usually already on the page by the time you finish reading"* is one of the most universal pedagogical patterns in applied mathematics. The vocabulary changes — invariants, conservation laws, constraints, sufficient statistics, fixed points, equilibria, kernels — but the underlying skill is the same. M1 mechanics is just the place a Cambridge student first meets it.

> [!info] Beyond syllabus — invariants and degrees of freedom
> Behind the forward-reading skill sits a deeper mathematical fact: a system of $n$ unknowns and $m$ independent constraints has $n - m$ **degrees of freedom**. Every invariant grabbed during the forward read is one constraint, reducing the remaining freedom by one. The question is *answerable* once $m \geq n$ — once you've grabbed enough invariants. Linear algebra (rank-nullity) makes this rigorous; Cambridge M1 makes it useful. The forward-reading discipline is the practical face of an idea that runs through the whole of applied mathematics.

---

## Connections

- **Generalises to — also in Meta/:** [[Forward Reading and Problem Discovery]] — the meta-card that sits *above* this one. *This* card teaches the M1-applied form of forward reading (frameworks, invariants, Cambridge cues); *that* card asks why forward reading is the cognitive act it is, and why a person who does it constantly is what we mean by a *hunter*. Read this card to pass M1; read that card to recognise yourself.
- **Sibling — also in Meta/:** [[Chain of Thought]] — the within-topic version of this card. *That* card teaches you to chain reasoning steps inside one framework; *this* card teaches you to choose between frameworks. They pair naturally as "thinking across topics" + "thinking within a topic."
- **Prerequisite (each is a framework column in Layer 1):** [[Newton's Laws of Motion]] (N2 + N3), [[Linear Momentum]] (momentum + impulse), [[Forces and Equilibrium]] ($\Sigma F = 0$ + $\Sigma \tau = 0$), [[SUVAT]] (constant-*a* kinematics), [[Work, Energy and Power]] (energy methods + power).
- **Prerequisite:** [[Kinematics Calculus]] — variable-*a* kinematics, the "calculus" framework column.
- **Application:** any 9709 P4 paper, A-Level Mechanics 1 / 2, IB AA Mechanics paper, AP Physics 1 / C: Mechanics — this card is what to bring to every multi-topic mechanics exam.
- **Cross-domain:** circuits (Kirchhoff), thermodynamics (state functions), optimisation, statistics, linear algebra (rank-nullity). The two-layer skill generalises.

---

## LaTeX Reference

This card is methodological — minimal new notation. Every formula referenced here lives in its own card; this is just the navigation index.

| Symbol | Where it lives |
|---|---|
| $F = ma$ | [[Newton's Laws of Motion]] |
| $\mathbf{F} = d\mathbf{p}/dt$ | [[Newton's Laws of Motion]], [[Linear Momentum]] |
| $\mathbf{p} = m\mathbf{v}$ | [[Linear Momentum]] |
| $\Sigma F = 0$, $\Sigma \tau = 0$ | [[Forces and Equilibrium]] |
| $v = u + at$ etc. (5 SUVAT formulae) | [[SUVAT]] |
| $W = Fs\cos\theta$ | [[Work, Energy and Power]] |
| $\text{KE} = \tfrac{1}{2}mv^2$ | [[Work, Energy and Power]] |
| $W_{\text{net}} = \Delta KE$ | [[Work, Energy and Power]] |
| $P = Fv$ | [[Work, Energy and Power]] |
| $F = \mu N$ at limit | [[Friction (Vocab)]], [[Forces and Equilibrium]] |
| $F = \mu_s N$ vs $F < \mu_s N$ | [[Friction (Vocab)]] |

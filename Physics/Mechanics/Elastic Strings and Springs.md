---
chinese: 弹性绳与弹簧 (tánxìng shéng yǔ tánhuáng)
prerequisites:
  - "[[Hooke's Law for Springs]]"
  - "[[Work, Energy and Power]]"
  - "[[Circular Motion]]"
  - "[[Stress, Strain and Young Modulus]]"
  - "[[Newton's Laws of Motion]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - syllabus/9231-3-4
  - type/deep
  - type/definition
  - type/proof
  - notation/modulus-of-elasticity
  - misconception/epe-uses-extension-not-length
  - misconception/slack-is-not-compression
  - misconception/max-speed-is-at-equilibrium
  - misconception/lambda-is-not-k
---

# Elastic Strings and Springs 弹性绳与弹簧

## Definition

Start with the objects, then the letters, then the law.

An **elastic string** is a string that stretches when pulled and returns to its original length when released — a bungee cord, a luggage strap, a rubber band. An **elastic spring** is the same idea in metal, with one extra power: it can be *compressed* as well as stretched. Both are modelled as **light** (massless) and perfectly elastic.

The letters:

- $L$ — the **natural length**: how long the string is when nothing pulls on it. Metres.
- $x$ — the **extension**: how much *longer* than natural it currently is, $x = (\text{current length}) - L$. Metres.
- $T$ — the **tension** the stretched string pulls back with. Newtons.
- $\lambda$ — the **modulus of elasticity**: the single number that measures how hard this particular string fights being stretched. Newtons (yes, a force — see below).

The law, [[Hooke's Law for Springs]] in its second uniform:

$$\boxed{\;T = \frac{\lambda x}{L}\;}$$

and the energy stored in the stretched string, the **elastic potential energy**:

$$\boxed{\;E = \frac{\lambda x^2}{2L}\;}$$

**What $\lambda$ means physically:** set $x = L$ in the tension law and everything cancels — $T = \lambda$. So *the modulus of elasticity is the tension in the string when it has been stretched to double its natural length.* That is why $\lambda$ is measured in newtons: it *is* a particular tension. A climbing sling with $\lambda = 2000$ N needs a 2000 N pull to double in length; a cheap rubber band with $\lambda = 5$ N doubles under the weight of an apple.

### 中文锚点

**蹦极 (bèngjí)。** 你站在高桥上，脚踝绑着一根粗弹性绳，往下跳。第一段是**自由落体**——绳还没绷直，松弛的弹性绳**完全不出力**（这是弹性绳和弹簧的根本区别：绳不能推，只能拉）。绳到达**自然长度**后开始绷紧，拉力按 $T = \lambda x/L$ 越拉越大；到**最低点**你速度为零，绳最长，你的动能和势能全部存进了绳里（$\lambda x^2/2L$）；然后它把你弹回去。有两个问题贯穿全卡：**你在哪里最快？**（在拉力恰好等于重力的平衡点——不是绳刚绷直的地方！）**你会下落多深？**（用能量守恒算——蹦极工程师解的就是本卡例题 3，"刚好到达 $O$"就是"刚好不碰到河面"。）

| English | 中文 | 记号 |
|---|---|---|
| Elastic string | 弹性绳 | 只能拉，不能推 |
| Natural length | 自然长度 | $L$ |
| Extension | 伸长量 | $x$（当前长度 $-\ L$） |
| Modulus of elasticity | （弹性绳的）弹性模量 | $\lambda$，单位是牛顿 |
| Tension | 张力 / 拉力 | $T = \lambda x / L$ |
| Elastic potential energy (EPE) | 弹性势能 | $\lambda x^2 / 2L$ |
| Taut / slack | 绷紧 / 松弛 | 松弛时 $T = 0$ |
| Equilibrium position | 平衡位置 | $T = mg$ 处，速度最大 |

> [!warning] 一个中文翻译陷阱
> 中文物理课本里的"弹性模量"通常指**杨氏模量** $E$（单位 Pa）。本卡的 $\lambda$ 是英式力学考卷专用的量，单位是**牛顿**。两者的关系恰好是 $\lambda = EA$（见 Beyond 一节）——同一个名字，差一个横截面积。

---

## Why invent a second letter? λ versus k

[[Hooke's Law for Springs]] wrote $F = kx$ and stored $\tfrac12 kx^2$. The new law $T = \lambda x/L$ is the *same law*: divide out and

$$k = \frac{\lambda}{L}.$$

So why bother? Run the thought experiment.

**Cut a spring in half.** Each half must now produce the same tension with half as much wire to stretch, so each coil deforms twice as much per unit of overall extension — *each half is twice as stiff*. Concretely: a string with $\lambda = 45$ N and $L = 1.5$ m has $k = \lambda/L = 30$ N m⁻¹, but either half ($L = 0.75$ m, same material, same thickness) has $k = 60$ N m⁻¹.

- $k$ **depends on the length you happened to cut** — it is a property of *this particular spring*.
- $\lambda$ **does not** — it is a property of the *material and its cross-section*. Every piece of the same bungee cord, whatever its length, has the same $\lambda$.

That is the entire reason for the letter: exam problems constantly compare strings of different natural lengths made of comparable stuff (example 1 below has two strings on one particle), and $\lambda$ is the version of stiffness that survives the comparison. The trade is that the length now appears *inside* the law — you divide by $L$ every time — which is also the most common place to slip.

> [!tip] Sanity check both formulas by cancelling units
> $T = \lambda x/L$: newtons × (m/m) = newtons ✓. $E = \lambda x^2/2L$: newtons × (m²/m) = N m = joules ✓. Ten seconds, catches the forgotten $L$ nine times out of ten.

---

## Deriving the energy: the triangle, a third time

The syllabus hands you $E = \lambda x^2/2L$ without proof. Here is the proof anyway, because it is the same triangle that gave $\tfrac12 kx^2$ in [[Hooke's Law for Springs]] and $\tfrac12 \sigma\varepsilon$ in [[Stress, Strain and Young Modulus]] — one idea in three uniforms.

Stretch the string slowly from extension $0$ to extension $x$. The pulling force needed at extension $s$ is $\lambda s/L$ — *not constant*, growing linearly from $0$ to $\lambda x/L$. The work done is the area under the tension–extension line: a triangle of base $x$ and height $\lambda x / L$,

$$E \;=\; \tfrac{1}{2} \times x \times \frac{\lambda x}{L} \;=\; \frac{\lambda x^2}{2L},$$

or by integration, $E = \int_0^x \frac{\lambda s}{L}\,ds = \frac{\lambda x^2}{2L}$. Average force $\times$ distance gives the same thing: $\tfrac12\left(0 + \frac{\lambda x}{L}\right) \times x$.

![[elastic-string-vs-spring.svg|700]]

The figure's left panel is the other half of the story: **the law only holds for $x > 0$ on a string.** A spring's graph continues into the compression region (it pushes back); a string's tension is *zero* for any $x \le 0$. A slack string is not a compressed string — it is an absent force.

> [!warning] The single most-lost mark in this topic
> $x$ in *both* formulas is the **extension**, never the current length. A string of natural length $2$ m stretched to $5$ m has $x = 3$, not $5$. Write "extension $= \text{length} - L$" as your first line and the trap disappears.

---

## Strings versus springs: the slack discipline

Because a string cannot push, every string problem carries a hidden question: **is the string actually taut here?** The discipline:

1. **Locate the slack boundary** — the position where the string is exactly at natural length. On one side it is taut ($T = \lambda x/L$); on the other it contributes nothing at all.
2. **Split the motion at that boundary.** Taut phase: tension + gravity. Slack phase: gravity alone — the particle is in free flight (or free slide), exactly as in [[Projectile Motion]].
3. **Energy flows straight through the boundary.** The tension is a conservative force while taut and absent while slack, so one energy equation between any two positions is legal even when the string goes slack in between — the EPE term is simply zero at any slack position.

For a **spring**, skip all three steps: it acts at every position, pushing when compressed ($T = \lambda x/L$ still, with $x$ now the compression and the force reversed).

---

## The worked examples — every one a real Paper 3 question

*(Cambridge Further Mechanics convention: $g = 10$ m s⁻² throughout.)*

### Example 1 — equilibrium between two strings (9231 N25/34 Q6a)

*$A$ and $B$ are fixed points $22a$ apart, $B$ vertically below $A$. A light elastic string of natural length $4a$ and modulus $5mg$ joins $A$ to a particle $P$ of mass $km$; another, natural length $8a$ and modulus $6mg$, joins $B$ to $P$. $P$ hangs between them. Show that in equilibrium $BP = \dfrac{57a - 2ak}{4}$.* [5]

*Tool: Hooke's law on each string separately, then Newton's first law on the particle. Trigger: "in equilibrium" — no motion, so forces balance and energy is not needed.*

Let $BP = y$, so $AP = 22a - y$. Extensions: string $AP$ has $x_1 = (22a - y) - 4a = 18a - y$; string $BP$ has $x_2 = y - 8a$.

$$T_1 = \frac{5mg\,(18a - y)}{4a} \quad(\text{pulls } P \text{ up}), \qquad T_2 = \frac{6mg\,(y - 8a)}{8a} \quad(\text{pulls } P \text{ down}).$$

Equilibrium of $P$ (weight $kmg$ down): $T_1 = T_2 + kmg$. Multiply through by $8a/mg$:

$$10(18a - y) = 6(y - 8a) + 8ak \;\Longrightarrow\; 180a - 10y = 6y - 48a + 8ak \;\Longrightarrow\; y = \frac{228a - 8ak}{16} = \frac{57a - 2ak}{4}. \checkmark$$

**The variable-choice lesson.** The published mark scheme accepts *four* different routes — extension of $AP$, length of $AP$, extension of $BP$, or both extensions with $x_A + x_B = 10a$ — and all four land on the same answer. The law doesn't care what you call things; it cares that you apply $\lambda x / L$ with *that string's own* $x$, $\lambda$ and $L$, and never mix them. Define your letter in writing, then stay loyal to it.

*(Both tensions came out positive — $8a < y < 18a$ here — so the taut assumption survives. Check it every time: a "string" whose tension comes out negative has actually gone slack, and the equation must be rebuilt without it.)*

### Example 2 — energy from rest to rest (9231 N25/34 Q6b)

*$P$ is pulled up to $BP = 18a$ and released; it first comes to instantaneous rest at $BP = 8a$. Find $k$.* [4]

*Tool: conservation of energy. Trigger: "released from rest … comes to rest" — both endpoints have zero KE, so the energy equation has no kinetic terms at all, only EPE and GPE.*

At $BP = 18a$: string $AP$ has length $4a$ — exactly natural, EPE zero; string $BP$ is stretched $10a$. At $BP = 8a$: string $BP$ is natural; string $AP$ is stretched $10a$. The particle falls $10a$.

$$\underbrace{\frac{6mg\,(10a)^2}{2(8a)}}_{\text{EPE in } BP \text{ at top}} + \underbrace{kmg \cdot 10a}_{\text{GPE released}} \;=\; \underbrace{\frac{5mg\,(10a)^2}{2(4a)}}_{\text{EPE in } AP \text{ at bottom}}$$

$$\frac{75}{2}mga + 10kmga = \frac{125}{2}mga \;\Longrightarrow\; 10k = 25 \;\Longrightarrow\; k = \frac{5}{2}.$$

The mark scheme's own rubric is worth reading as strategy: *B1 for one correct EPE term, M1 for a dimensionally correct energy equation with two EPE terms and a GPE term and **no KE terms***. The examiner is checking whether you noticed the rest-to-rest trigger.

### Example 3 — the vertical journey through slack (9231 N24/33 Q3)

*A particle of mass $m$ hangs from $O$ on an elastic string of natural length $2$ m, modulus $2mg$. It is pulled down $d$ m below its equilibrium position and released. (a) Given it just reaches $O$, find $d$. (b) Find its speed when the string first returns to natural length.* [6, 2]

*Tool: equilibrium extension first, then one energy equation over the whole journey. Trigger: "just reaches $O$" — the destination has $v = 0$, and $O$ is above the slack boundary, so the journey has a taut phase and a free-flight phase.*

**Anchor the geography before any algebra.** Equilibrium: $mg = \dfrac{2mg\,e}{2} \Rightarrow e = 1$. So: natural length ends $2$ m below $O$; equilibrium sits $3$ m below $O$; the launch point is $3 + d$ m below $O$.

![[elastic-vertical-journey.svg|640]]

**One energy equation, launch point to $O$.** At the bottom: EPE with extension $1 + d$, no KE. At $O$: no EPE (string slack the whole way up from the $2$ m mark — zero force, not negative force), no KE ("just reaches"). Everything went into height, $(3 + d)$ m of it:

$$\frac{2mg\,(1+d)^2}{2 \cdot 2} = mg\,(3 + d) \;\Longrightarrow\; (1+d)^2 = 2(3+d) \;\Longrightarrow\; d^2 = 5 \;\Longrightarrow\; d = \sqrt{5}.$$

The slack phase needed no special handling — its EPE term was simply zero. That is the payoff of the slack discipline's step 3.

**(b)** Energy from the launch point to the natural-length mark ($2$ m below $O$, a rise of $1 + d$):

$$\frac{2mg(1+d)^2}{4} = \tfrac12 m V^2 + mg(1+d) \;\Longrightarrow\; V^2 = g\,(d^2 - 1) = 40 \;\Longrightarrow\; V = 2\sqrt{10} \approx 6.32 \text{ m s}^{-1}.$$

*Cross-check from the other side:* above that mark the particle is in free flight and must just reach $O$, $2$ m up: $V^2 = 2g \times 2 = 40$. ✓ Two independent routes, one answer — the free-flight check costs one line and certifies the whole calculation.

![[elastic-see-it-stretch.mp4]]

### Example 4 — where is the particle fastest? (9231 J25/31 Q5)

*One end of an elastic string (natural length $0.5$ m, modulus $14$ N) is fixed at $A$ on a smooth plane inclined at $\alpha$, $\tan\alpha = \frac{7}{24}$. A particle of mass $2$ kg on the other end is held on the slope $0.8$ m above $A$ and released. Find its maximum velocity.* [6]

*Tool: force balance to* locate *the fastest point, energy to* measure *it. Trigger: "maximum velocity" — speed is greatest where acceleration is zero, i.e. where the forces balance. Not where the string goes slack.*

Read the journey first: released above $A$, the particle slides down (initially both gravity *and* the stretched string pull it toward $A$), passes through a slack zone around $A$, and the string re-engages once the particle is more than $0.5$ m below $A$ — now pulling *up*-slope, harder and harder. While tension is less than the gravity component the particle is still speeding up; the moment they balance is the peak.

**Locate:** with $\sin\alpha = \frac{7}{25}$ (from $\tan \alpha = \frac{7}{24}$, the 7–24–25 triangle),

$$\frac{14x}{0.5} = 2g\sin\alpha = 2(10)\tfrac{7}{25} = 5.6 \;\Longrightarrow\; x = 0.2 \text{ m}.$$

**Measure:** from the start to that point the particle travels $0.8 + 0.5 + 0.2 = 1.5$ m down the slope, dropping $1.5\sin\alpha$ vertically. Initial EPE (extension $0.3$ above): $\frac{14(0.3)^2}{2(0.5)} = 1.26$ J. Final EPE (extension $0.2$ below): $\frac{14(0.2)^2}{2(0.5)} = 0.56$ J.

$$2g\sin\alpha \times 1.5 + 1.26 = 0.56 + \tfrac12(2)v^2 \;\Longrightarrow\; v^2 = 8.4 + 0.7 = 9.1 \;\Longrightarrow\; v \approx 3.02 \text{ m s}^{-1}.$$

The animation above plays this exact question in its second chapter: watch the speed readout — it is still climbing as the string re-tightens, and peaks precisely at the $a = 0$ marker.

### Example 5 — the elastic conical pendulum (9231 J25/31 Q3)

*A particle of mass $1.6$ kg lies on a rough rotating disc, $1.5$ m from the centre $O$, attached by an elastic string (natural length $2$ m, modulus $32$ N) to a point $A$ vertically above $O$. Given the tension is $8$ N, show $\sin\alpha = 0.6$, where $\alpha$ is the string's angle to the vertical.* [2]

*Tool: Hooke's law run backwards — from tension to geometry. Trigger: the tension is given, so the string's stretched length is one substitution away.*

$$8 = \frac{32x}{2} \;\Longrightarrow\; x = 0.5 \;\Longrightarrow\; AP = 2.5 \text{ m} \;\Longrightarrow\; \sin\alpha = \frac{1.5}{2.5} = 0.6. \checkmark$$

This is the syllabus's "elastic string as a conical pendulum": the string's *elasticity* fixes the geometry, and from there it is a standard rotating-frame force problem — resolve vertically and horizontally, $\sum F = mr\omega^2$ toward the centre. The full circular-motion machinery, including this very question's second part (friction at the point of slipping, $\omega^2 = 4$, $60/\pi \approx 19.1$ revolutions per minute), is worked in [[Circular Motion]]. What the elastic string adds is only the opening move you just saw.

---

## Where this is the working tool: designing a bungee jump

A commercial bungee operator's safety case *is* example 3 with the numbers filled in. Take a $70$ kg jumper, a cord of natural length $20$ m, and a platform $50$ m above the river: the designer wants the jumper's "just reaches" point — the bungee equivalent of *just reaches $O$*, but pointing down — to sit a safe margin above the water, say a total fall of $45$ m.

Rest to rest, launch to lowest point (extension $25$ m at the bottom):

$$mgh = \frac{\lambda x^2}{2L} \;\Longrightarrow\; 70 \times 10 \times 45 = \frac{\lambda \times 25^2}{2 \times 20} \;\Longrightarrow\; \lambda = 2016 \text{ N}.$$

So the cord must roughly double its length under about $2000$ N — and now every safety number falls out of this card's formulas. Peak tension at the bottom: $T = \lambda x/L = 2520$ N $= 3.6mg$. Peak deceleration: $(T - mg)/m = 26$ m s⁻² — about $2.6g$, right in the real industry's comfort band. Fastest moment of the jump: at the equilibrium extension $x_0 = mgL/\lambda \approx 6.9$ m (example 4's trigger again — not where the cord goes taut), at about $21.7$ m s⁻¹. A heavier jumper moves the "just reaches" point lower — which is why jump operators weigh every customer and swap cords by weight class, exactly the $\lambda$-comparison that motivated the letter in the first place.

The same energy bookkeeping, run in reverse as *how much force does a fall put on the rope*, is the climbing-rope impact-force calculation worked in [[Stress, Strain and Young Modulus]] — there with $k = EA/L_0$, here with $\lambda/L$, the same equation in both uniforms.

---

## Misconceptions

### 1. Using the length where the extension belongs

$T = \lambda \times 5/L$ for a string of current length $5$ m and natural length $2$ m. **Fix:** first line of every solution: "extension $= \text{current length} - L = 3$." The examiners' alternative-method table in example 1 exists precisely because candidates who *name* their variable stop making this error.

### 2. Letting a slack string push

A string with negative extension gets $T = 0$, not a negative tension. Writing $T = \lambda x/L$ with $x = -0.3$ quietly turns the string into a spring and the answer into fiction. **Fix:** the slack discipline — find the boundary, split the motion, zero the EPE while slack.

### 3. "Fastest where the string goes slack"

The slack boundary is where the *tension* vanishes; the speed peaks where the *net force* vanishes — the equilibrium point, which on a vertical string is $x_0 = mgL/\lambda$ *beyond* natural length. Between the two the particle is still accelerating. **Fix:** the example-4 trigger — "maximum velocity" always means "solve $a = 0$ first."

### 4. One energy equation, but a term missing

The full inventory is KE + GPE + EPE, *per string*. Example 2 has two EPE terms; forgetting the second is the modal error on two-string questions. **Fix:** before writing the equation, list every string and ask "what is your extension *here*, and *here*?" — a term per string per position, zero when natural or slack.

### 5. Mixing λ and k mid-problem

Half-remembered hybrids — $T = \lambda x$, $E = \tfrac12 \lambda x^2$ — are dimensionally wrong (a newton times a metre is not a newton). **Fix:** the ten-second unit cancellation from the definition section; $\lambda$ never appears without its $/L$.

---

## Beyond syllabus

### λ = EA — the bridge to materials

Recall from [[Stress, Strain and Young Modulus]] that a rod of Young modulus $E$, cross-section $A$ and natural length $L_0$ behaves as a spring with $k = EA/L_0$. Multiply by the length: $\lambda = kL = EA$. The exam's mysterious "modulus of elasticity in newtons" is just *Young's modulus times cross-sectional area* — which explains everything the cut-in-half experiment showed. Cutting changes $L$ but not $E$ or $A$, so $\lambda$ survives; using a thicker cord doubles $A$ and doubles $\lambda$; switching from rubber ($E \sim 10^6$ Pa) to steel ($E \sim 10^{11}$ Pa) multiplies $\lambda$ a hundred-thousand-fold at the same thickness. The bungee cord above, with $\lambda \approx 2000$ N and rubber's $E \approx 2$ MPa, needs $A = \lambda/E \approx 10$ cm² — a cord about $3.6$ cm thick. Measure a real one: that is the size.

### The taut phase is simple harmonic motion

While the string in example 3 is taut, the restoring force about the equilibrium point is exactly linear — the same equilibrium-absorbs-gravity argument as [[Hooke's Law for Springs]]' vertical-spring example, with $k = \lambda/L$ — so the taut part of the journey is a piece of [[Simple Harmonic Motion]] with $\omega^2 = \lambda/(mL)$. The full motion is SHM below the slack boundary stitched to free flight above it: a genuinely piecewise oscillation, which is why the animation integrates the equation of motion instead of quoting a sine. (A mass on a *spring* has no boundary, and its oscillation is pure SHM at every amplitude — within Hooke's limit.)

### Why a real bungee cord is deliberately not Hookean

Rubber under large strain does not stay on the straight line — its tension–extension curve flattens in the middle (entropy-driven uncoiling of polymer chains) before stiffening near full stretch. Designers *want* this: a flatter mid-curve spreads the deceleration over more of the fall, lowering the peak $g$-force below what a linear cord with the same "just reaches" point would deliver. The linear model in this card is the exam's honest first approximation and the engineer's back-of-envelope; the safety margins on top of it absorb the difference.

---

## Exam Notes

### Cambridge 9231 Further Mathematics (Paper 3, §3.4)

- The three LOs verbatim: Hooke's law for an elastic string or spring with the term **modulus of elasticity**; the elastic-PE formula (*"proof of the formula is not required"* — it is handed to you); and problems with forces and **work–energy**, the syllabus's own examples being *"a particle moving horizontally or vertically or on an inclined plane while attached to one or more strings or springs, or a particle attached to an elastic string acting as a 'conical pendulum'"* — examples 1–5 above are exactly that list, every one from a real recent paper.
- **MF19 prints both formulas** ($T = \lambda x/l$ and $E = \lambda x^2/2l$, under "Elastic strings and springs") — the marks are for deployment, not recall. $g = 10$ m s⁻².
- Mark-scheme habits from the papers used above: each correct Hooke or EPE application is its own B1; the energy equation is an M1 that must be **dimensionally correct** with the right term inventory (they explicitly police "no KE terms" on rest-to-rest); "show that" answers are **AG — shown convincingly**, so the linear algebra must appear, not just the destination.
- Crossovers to be ready for: elastic string + rotating disc (§3.3, example 5), elastic string + work–energy on a slope (§3.1 flavour), and the vertical journey that turns into free flight.

### Edexcel IAL Further Mathematics (M3, §M3.2)

- "Elastic strings and springs" is its own unit heading: Hooke's law in the $\lambda$ form, energy stored, and equilibrium/energy problems — the same territory as 9231 §3.4.
- The specification states that both formulas **"will be provided for use with the paper"**, printed in its own assessment-information section — same deal as MF19.

### Not examined on…

- **9709** carries no Hooke's law in any form — elastic strings are entirely a Further topic for Cambridge maths students.
- **OxfordAQA 9660** examines only *inextensible* strings throughout its mechanics units — no elastic strings, no modulus of elasticity.
- The **physics boards** (9702 §6.2, 0625 §1.5, IB, AP) examine the same physics in the $F = kx$, $\tfrac12 kx^2$ form with no $\lambda$ — that door is [[Hooke's Law for Springs]].

---

## Formula summary

| Quantity | Formula | Notes |
|---|---|---|
| Tension (string taut / spring) | $T = \dfrac{\lambda x}{L}$ | $x$ = extension (or compression, springs only) |
| Elastic potential energy | $E = \dfrac{\lambda x^2}{2L}$ | the triangle: $\tfrac12 \times x \times \tfrac{\lambda x}{L}$ |
| Slack string | $T = 0,\; E = 0$ | whenever current length $\le L$ |
| Translation to spring-constant form | $k = \dfrac{\lambda}{L}$ | so $\tfrac12 kx^2 = \tfrac{\lambda x^2}{2L}$ ✓ |
| Modulus from materials | $\lambda = EA$ | Young modulus × cross-section |
| Vertical equilibrium extension | $x_0 = \dfrac{mgL}{\lambda}$ | where the hanging particle is fastest |

---

## Connections

- **Parents:**
   - [[Hooke's Law for Springs]] — the law itself, the minus sign, the Taylor-expansion reason it is universal; this card is that law wearing its Further-Mechanics uniform.
   - [[Work, Energy and Power]] — work as area under the force curve is what makes the EPE triangle legal.
   - [[Circular Motion]] — the rotating-disc and conical-pendulum machinery that example 5 hands its geometry to.
   - [[Stress, Strain and Young Modulus]] — supplies $k = EA/L_0$, hence $\lambda = EA$, and the climbing-rope impact calculation that mirrors the bungee design.
   - [[Newton's Laws of Motion]] — every equilibrium equation above.

- **Siblings in method:**
   - [[Simple Harmonic Motion]] — the taut phase of every vertical-string problem is SHM about the equilibrium point; the slack boundary is what makes elastic-string oscillation piecewise rather than pure.
   - [[Projectile Motion]] — the slack phase *is* free flight; example 3's cross-check is a one-line projectile argument.
   - [[Newton's Law of Restitution]] — the other Further Mechanics topic where a journey splits into phases with different force inventories; the same split-at-the-boundary discipline.

- **Misconception traps cleared:** extension, never length; slack means zero, never negative; fastest at equilibrium, never at natural length; one EPE term per string per position; $\lambda$ never travels without its $/L$.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $T = \dfrac{\lambda x}{L}$ | `T = \dfrac{\lambda x}{L}` | Hooke's law, modulus form |
| $E = \dfrac{\lambda x^2}{2L}$ | `E = \dfrac{\lambda x^2}{2L}` | elastic potential energy |
| $\lambda$ | `\lambda` | modulus of elasticity, units N |
| $k = \lambda / L$ | `k = \lambda / L` | translation to spring-constant form |
| $\lambda = EA$ | `\lambda = EA` | bridge to Young modulus |
| $x_0 = mgL/\lambda$ | `x_0 = mgL/\lambda` | equilibrium extension, vertical |

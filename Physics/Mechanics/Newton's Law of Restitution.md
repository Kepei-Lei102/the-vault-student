---
chinese: 恢复系数 (huīfù xìshù)
prerequisites:
  - "[[Linear Momentum]]"
  - "[[Projectile Motion]]"
  - "[[Vectors in Physics]]"
leads_to: []
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - syllabus/9231-3-6
  - type/deep
  - misconception/e-belongs-to-one-object
  - misconception/nel-in-any-direction
  - misconception/momentum-lost-in-inelastic
  - misconception/ke-scales-with-e
---

# Newton's Law of Restitution 恢复系数

> *Drop a table-tennis ball from 30.5 cm onto a steel block. If it bounces back to between 24 and 26 cm, it is legal for international play; outside that window, it is not a table-tennis ball, whatever it says on the box. The sport's rulebook is quietly regulating one number — the number this card is about — and almost every ball sport does the same. Bounciness is not a vibe. It is a measurable constant with a name, a law, and a place on the exam.*

## 中文锚点

乒乓球有一条国际标准：从 30.5 cm 高处落到钢块上，必须反弹到 24–26 cm 之间——不在这个窗口里的球，不配叫比赛用球。规则管住的其实是一个数：**恢复系数** $e$——**分离速度与接近速度之比**。它是"弹性"的身份证：完全弹性碰撞 $e=1$（分开得和撞上一样快），完全非弹性 $e=0$（撞上就粘在一起，[[Linear Momentum|动量]]那张卡里 9709 的"合并"情形），真实世界全在中间。落地反弹藏着最方便的测量：反弹高度之比是**速度比的平方**，所以 $e = \sqrt{h_1/h_0}$——乒乓球那条规则折算出来就是 $e \approx 0.89$ 到 $0.92$。为什么需要这条定律？因为动量守恒只有**一个方程**，碰撞后却有**两个未知的速度**——除非两球粘在一起，否则算不下去；牛顿碰撞定律——一条量出来的实验定律——补上第二个方程，联立就能解出。这是一条**实验**定律：$e$ 由两个碰撞面的**材质**共同决定（钢碰钢接近 1，橡皮泥碰什么都接近 0），它属于"这一对"，不属于某一个球。斜碰（打台球！）只多一个动作：把速度沿**连心线**和垂直方向分解——光滑球体没有摩擦，**垂直分量原封不动**，连心线方向就按正碰的规矩来。打库边同理：平行库边的分量不变，垂直分量乘以 $e$ 反向——出射角因此比入射角更贴库，$\tan\beta = e\tan\alpha$，台球高手的走位全在这条公式里。考场的两句要紧话：**先定正方向，两个方程用同一个正方向写**（评分标准原话"signs must be consistent"——符号乱一次，整题崩塌）；动量**永远**守恒；真正被吃掉的是**动能**——被声音、发热、形变一口一口吃掉（你*听见*的那声脆响，就是动能离场的声音）——而 $e$ 并不是吃动能的那张嘴，它只是这顿饭的**总账单**：材质决定吃掉多少，$e$ 把结果记成一个数。

| English | 中文 | one-line meaning |
|---|---|---|
| coefficient of restitution $e$ | 恢复系数 | separation speed over approach speed — the pair's bounciness ID |
| Newton's experimental law (NEL) | 牛顿实验定律 | $e$ is constant for a given pair of surfaces — measured, not derived |
| approach / separation speed | 接近 / 分离速度 | how fast the gap closes before; how fast it opens after |
| perfectly elastic ($e=1$) | 完全弹性 | separation as fast as approach — kinetic energy survives |
| inelastic ($e=0$) | 完全非弹性 | no separation: the bodies coalesce |
| direct impact | 正碰 | velocities along the line of centres |
| oblique impact | 斜碰 | velocities at an angle — resolve, then treat the line of centres |
| line of centres | 连心线 | the axis through both centres at the moment of contact |
| smooth | 光滑的 | no friction — the tangential velocity component is untouched |
| rebound | 反弹 | the wall case: tangential kept, normal reversed and scaled by $e$ |

## The problem, before the tool

[[Linear Momentum]] ended its collision story at a cliff edge, politely disguised. Conservation of momentum is **one equation**; a collision leaves **two unknown velocities**. One equation, two unknowns — unsolvable, in general. The card escaped the cliff twice: if the bodies *coalesce* (9709's chosen world) the two unknowns become one, and if the collision is *perfectly elastic*, energy conservation supplies a second equation. But a tennis ball on concrete neither sticks nor bounces perfectly. What happens in between — which is to say, in almost every real collision — was left standing at the edge.

The missing information is not in the mechanics at all. Two collisions with identical masses and identical approach speeds end differently if one pair is steel-on-steel and the other is putty-on-concrete: **the outcome depends on the materials**, and no amount of momentum bookkeeping can know what the materials will do. What's needed is an experimental fact about the *pair of surfaces* — a measured number that closes the system. Newton did the measuring.

## The law — letters first

Set up the names before the law uses them. Two bodies collide moving along the same line; call the velocities **before** the collision $u_1$ and $u_2$, and **after**, $v_1$ and $v_2$, all measured in the *same* chosen positive direction. Two derived speeds carry the physics:

- the **approach speed** — how fast the gap was closing before impact: $u_1 - u_2$;
- the **separation speed** — how fast the gap opens after: $v_2 - v_1$.

**Newton's experimental law** is the claim that for a given pair of surfaces, their ratio is a constant — the **coefficient of restitution**:

$$e = \frac{\text{speed of separation}}{\text{speed of approach}} = \frac{v_2 - v_1}{u_1 - u_2}, \qquad 0 \le e \le 1$$

Three things about this law deserve their full weight:

- **It is *experimental*** — the syllabus's own word. Nothing derives it; Newton rolled spheres of glass, steel, cork and wool into each other and *found* that the ratio stays put while speeds vary. It is a materials fact, like density, holding well at everyday speeds — and like every empirical law, it has fine print ([[Resistance]] made the same point about Ohm).
- **$e$ belongs to the pair.** Steel-on-steel ≈ 0.95; the *same* steel ball on putty, nearly 0. Asking for "the $e$ of this ball" is half a question.
- **The endpoints are old friends.** $e = 1$ is the *perfectly elastic* collision — separation exactly as fast as approach, which is precisely [[Linear Momentum]]'s "relative velocity reverses" test (and 9702's phrase for recognising elastic collisions is this law at $e=1$, wearing exam clothes). $e = 0$ is *inelastic*: no separation at all, the bodies coalesce — 9709's entire collision world is the $e=0$ special case. Everything real lives between.

> [!warning] The one discipline that decides whole questions: signs
> Choose a positive direction **once**, before writing anything, and write **both** equations — momentum and NEL — in that same direction, with every velocity carrying its honest sign. The published mark schemes say it in as many words: *"signs must be consistent with the momentum equation."* The classic collapse is writing momentum with $u_2$ negative (bodies approaching head-on) and then NEL with everything positive: on the June 2026 paper worked below, exactly that slip produces $e = -0.335$, and the scheme prices it — final accuracy mark gone. A negative $e$ is always the sign flag: nothing in nature un-bounces.

## The machinery — two equations, then arithmetic

Every direct-impact problem is the same machine:

$$\underbrace{m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2}_{\text{momentum — always true}} \qquad \underbrace{v_2 - v_1 = e\,(u_1 - u_2)}_{\text{NEL — the materials' contribution}}$$

Two equations, two unknowns; solve simultaneously. (Solved once in general, for the record: $v_1 = \dfrac{m_1 u_1 + m_2 u_2 - e\,m_2 (u_1 - u_2)}{m_1 + m_2}$ and $v_2 = \dfrac{m_1 u_1 + m_2 u_2 + e\,m_1 (u_1 - u_2)}{m_1 + m_2}$ — not for memorising, but for seeing the anatomy: a shared centre-of-mass term, plus a bounce term scaled by $e$ with opposite signs. At $e=0$ both collapse to the common coalescence velocity, exactly [[Centre of Mass]]'s point that internal drama never moves the average.)

**What $e$ costs in energy.** Momentum survives every collision; kinetic energy pays for the deformation, sound and heat, and the bill has a clean closed form (derived by substituting the solutions above; verified symbolically for this card):

$$\Delta KE = \tfrac12\,\frac{m_1 m_2}{m_1+m_2}\,(1 - e^2)\,(u_1-u_2)^2$$

Read its skeleton: at $e = 1$ the loss is zero (elastic means energy-conserving — now *proved* rather than defined), at $e = 0$ the loss is maximal, and in between the energy fate is governed by $1 - e^2$ — **the square**, a fact the misconceptions section returns to.

![[restitution-direct-impact.svg|740]]

## The wall — bounce heights, and the cheapest measurement of $e$

A ball striking a fixed surface is the two-body law with one body refusing to move — and it is worth slowing the refusal down, because this is the cleanest place to *watch* a collision happen.

**The impact in slow motion.** High-speed footage of any bounce shows two phases. First **compression**: the ball squashes against the floor, and its kinetic energy converts into elastic energy in the deformed material — the ball is, briefly, a loaded spring. Then **restitution**: the spring pushes back and the ball un-squashes, converting stored energy back into upward motion. The catch is that the spring-back never repays in full — some of the stored energy leaves as **sound** (the click you hear *is* kinetic energy departing), some as heat in the flexing material, some in permanent dents. The coefficient $e$ is not the thing doing the eating; it is the **ledger**: materials decide how much is eaten, and $e$ records the result as one number, on the speed scale.

**Why the wall's velocity never appears.** Strictly, momentum conservation still holds — the Earth recoils. But the Earth's share of the momentum produces a velocity of order $m_{\text{ball}}/M_{\text{Earth}} \sim 10^{-25}$ of the ball's: zero to any conceivable measurement. So the momentum equation degenerates to "the wall stays put," and Newton's law alone governs the bounce. With the wall's speed pinned at zero, *separation speed* is just the rebound speed and *approach speed* the arrival speed:

$$v_{\text{rebound}} = e\,v_{\text{arrive}}$$

**The bounce-height formula, earned line by line.** Drop a ball from height $h_0$ and let it rebound to $h_1$. Three ingredients, chained:

1. *Falling:* energy conservation on the way down, $\tfrac12 m v_0^2 = mgh_0$. The mass $m$ is a common factor on both sides — cancel it (gravity does not care what the ball weighs), leaving $v_0^2 = 2gh_0$, so the ball **arrives at** $v_0 = \sqrt{2gh_0}$.
2. *Bouncing:* the wall rule above — it **leaves at** $v_1 = e\,v_0 = e\sqrt{2gh_0}$.
3. *Rising:* energy conservation on the way up, $\tfrac12 m v_1^2 = mgh_1$, the same $m$ cancelling again: $v_1^2 = 2gh_1$.

Now substitute step 2 into step 3: $\left(e\sqrt{2gh_0}\right)^2 = 2gh_1$, that is, $e^2 \cdot 2gh_0 = 2gh_1$. The $2g$ cancels, leaving $h_1 = e^2 h_0$ — the heights measure $e$ **squared**, because heights live on the energy scale ($\propto v^2$) while $e$ lives on the speed scale. Read backwards, this is the cheapest $e$-measurement in physics:

$$\boxed{\;e = \sqrt{\frac{h_1}{h_0}}\;}$$

which is why the epigraph's rulebook works: the ITTF's 30.5 cm → 24–26 cm window pins the ball's $e$ (with the steel block) between $\sqrt{24/30.5} \approx 0.89$ and $\sqrt{26/30.5} \approx 0.92$. FIBA does the same to basketballs — dropped from 1.80 m, they must return to between 1.20 and 1.40 m: $e$ between about 0.82 and 0.88. Sports regulation is coefficient-of-restitution regulation with the algebra hidden.

Each successive bounce repeats the scaling: heights fall as $h_0,\ e^2h_0,\ e^4h_0,\dots$ — a geometric sequence with ratio $e^2$, which is why a dropped ball's *click-click-click* accelerates into a purr: the heights (and with them the flight times) shrink by the same factor every bounce.

## Oblique impact — one new idea, and it's "smooth"

Everything above was head-on. The syllabus's second half — the distinctive one — is impact at an angle, and it costs exactly one new idea. At the moment two spheres touch, the geometry defines the **line of centres**: the axis through both centres, which is the only direction along which the surfaces press on each other. The word **smooth** in the question is load-bearing: no friction means *no force at all* perpendicular to that line. And a component of velocity that feels no force does not change.

So the recipe is [[Projectile Motion]]'s resolve-and-conquer, transplanted:

1. **Resolve** every velocity into components *along* the line of centres and *perpendicular* to it.
2. **Perpendicular:** untouched. Copy each body's perpendicular component through the collision unchanged.
3. **Along the line of centres:** run the direct-impact machine — momentum plus NEL, in one consistent positive direction.

For a sphere striking a fixed smooth wall obliquely, the same three steps collapse to two lines: the component *along* the wall survives (smooth = no friction = no force in that direction), the component *into* the wall runs the wall rule — reversed, and shrunk by $e$. Write the two components before and after, with the arrival at angle $\alpha$ *to the wall*: before, along $= v\cos\alpha$ and into $= v\sin\alpha$; after, along $= v\cos\alpha$ (untouched) and out $= e\,v\sin\alpha$. The departure angle $\beta$ to the wall then satisfies

$$\tan\beta = \frac{\text{out of wall}}{\text{along wall}} = \frac{e\,v\sin\alpha}{v\cos\alpha} = e\,\tan\alpha$$

— the rebound hugs the wall more than the arrival did (since $e < 1$), which any snooker or 台球 player knows in the hands without the algebra: a ball played off the cushion comes off *flatter* than it went in, and judging exactly how much flatter is what position play is.

![[restitution-oblique.svg|740]]

![[restitution-see-it-run.mp4]]

*Collisions as processes: the straight bounce with its squash-and-spring-back-short moment and the $e^2$ height ladder; the cushion shot frozen at contact while each velocity component receives its fate; and the two-sphere impact where the line of centres is born at the touch — watch sphere B leave along it, because that is the only direction it was ever pushed.*

## Worked examples — real Paper 3 questions, every tool and trigger named

### Example 1 — direct impact, the standard machine (9231 November 2025 Paper 31 Q1)

> Two uniform smooth spheres $A$ and $B$ of equal radii have masses $4m$ and $m$. $B$ is at rest; $A$ moves with speed $u$ and collides directly with $B$. After the collision, the momentum of $A$ is three times the momentum of $B$. Find the coefficient of restitution $e$. [4]

*Trigger: "collides directly" → the two-equation machine, no resolving needed.* Take $A$'s initial direction as positive; let $v_A, v_B$ be the velocities after.

*Tool 1 — momentum:* $4mu = 4mv_A + mv_B$.
*Tool 2 — NEL* (approach $= u - 0$): $v_B - v_A = eu$.
*Tool 3 — the question's own condition:* $4mv_A = 3(mv_B)$, so $v_A = \tfrac34 v_B$.

Substitute into momentum: $4m\left(\tfrac34 v_B\right) + m v_B = 4mu \Rightarrow 4mv_B = 4mu \Rightarrow v_B = u$, hence $v_A = \tfrac34 u$. Then NEL reads $u - \tfrac34 u = eu$:

$$e = \tfrac14$$

Four marks: the momentum equation with masses right, NEL with signs consistent, the pair of velocities, the value. (The published scheme also blesses the reverse route — solve the machine *in terms of $e$* first, $v_A = \tfrac{u}{5}(4-e)$, $v_B = \tfrac{4u}{5}(1+e)$, then impose the momentum ratio. Same destination; pick whichever order feels natural and the marks follow.)

### Example 2 — oblique two-sphere impact, the full ritual (9231 June 2026 Paper 33 Q5)

> Two smooth spheres $A$ and $B$ of equal radii and equal masses $m$ move toward each other and collide. Before: $A$'s direction makes angle $\alpha$ with the line of centres, $B$'s makes $\beta$. After: $A$'s makes $\theta$, $B$'s makes $\phi$. Given $\cos\alpha = \cos\phi = \tfrac45$, $\cos\beta = \tfrac{24}{25}$, $\cos\theta = \tfrac35$. (a) Find the percentage loss in the kinetic energy of $A$. [2] (b) Find the coefficient of restitution. [4]

**(a)** *Trigger: smooth spheres → each body's perpendicular component is preserved, and that alone relates its speeds.* For $A$: $u_A\sin\alpha = v_A\sin\theta$, with $\sin\alpha = \tfrac35$, $\sin\theta = \tfrac45$:

$$v_A = u_A\,\frac{3/5}{4/5} = \tfrac34 u_A \quad\Longrightarrow\quad \frac{\Delta KE_A}{KE_A} = 1 - \left(\tfrac34\right)^2 = \tfrac{7}{16} = \mathbf{43.75\%}$$

Two marks, and note the wonder: no masses, no momentum equation — the perpendicular-preservation rule carried the whole part.

**(b)** *Trigger: "coefficient of restitution" between spheres → the direct-impact machine along the line of centres — after the sign ritual.* Fix the positive direction as $A$'s initial motion along the line of centres. $B$ approaches head-on, so its component is *negative*; and (the diagram's geometry) $A$ rebounds, so its after-component is negative too. The same rule applied to $B$ gives $v_B = \tfrac{7}{15}u_B$ (from $\sin\beta = \tfrac{7}{25}$, $\sin\phi = \tfrac35$). Along the line of centres:

*Momentum:* $\;m\left(\tfrac45 u_A\right) - m\left(\tfrac{24}{25}u_B\right) = -m\left(\tfrac34 u_A\right)\!\left(\tfrac35\right) + m\left(\tfrac{7}{15}u_B\right)\!\left(\tfrac45\right)$

which simplifies to $u_B = \tfrac{15}{16}u_A$ — the collision itself fixes the speed ratio the question never stated.

*NEL* (approach = the closing rate $\tfrac45 u_A + \tfrac{24}{25}u_B$; separation = the opening rate $\tfrac35 v_A + \tfrac45 v_B$):

$$e = \frac{\tfrac35\left(\tfrac34 u_A\right) + \tfrac45\left(\tfrac{7}{15}u_B\right)}{\tfrac45 u_A + \tfrac{24}{25} u_B} \;\stackrel{u_B = \frac{15}{16}u_A}{=}\; \frac{8}{17} \approx 0.471$$

Every number here was re-derived symbolically for this card and matches the published scheme — which also names the price of sign carelessness: the inconsistent-signs route yields $e = -\tfrac{88}{263} = -0.335$ and scores B1 M1 M1 **A0**. The negative sign *is* the alarm; treat it as one.

![[restitution-oblique-walkthrough.mp4]]

*The same question at exam pace: components split at the moment of contact, the perpendicular pair copied through, then the two-equation machine assembled along the line of centres with the sign convention displayed the whole way.*

### Example 3 — the projectile hybrid (9231 November 2025 Paper 31 Q7)

> $P$ is projected at $25\ \text{m s}^{-1}$ at angle $\theta$ above the horizontal, $\tan\theta = \tfrac43$. At point $A$ its direction of motion makes $45°$ with the downward vertical. There it strikes a fixed smooth barrier inclined at $45°$ to the horizontal, rebounds with $e = \tfrac19$, and lands. Find the horizontal distance travelled by $P$ after it strikes the barrier. [parts (a)–(c), worked as one story; $g = 10$]

*Tool: [[Projectile Motion]]'s components first.* Launch components: $u_x = 15$, $u_y = 20$. At $A$ the motion is $45°$ below the horizontal, so $v_y = -v_x = -15$: that happens at $t = 3.5$ s, placing $A = \left(\tfrac{105}{2}, \tfrac{35}{4}\right)$ with impact speed $\sqrt{15^2 + 15^2} = 15\sqrt2$.

*Trigger — the geometric gift:* the velocity points $45°$ below horizontal, and the barrier is inclined at $45°$ — so the ball hits the barrier **perpendicularly**. The "oblique" setup is a direct impact in disguise: no component survives along the barrier, and the whole velocity reverses scaled by $e$. Spotting this is the question's real test.

*After impact:* speed $\tfrac{15\sqrt2}{9} = \tfrac{5\sqrt2}{3}$, directed $45°$ *above* the horizontal, back the way it came — components $\tfrac53$ each. From height $\tfrac{35}{4}$: solve $-\tfrac{35}{4} = \tfrac53 t - 5t^2$ to get $t = \tfrac32$ s, so the horizontal distance is $\tfrac53 \times \tfrac32 = \boxed{2.5\ \text{m}}$ — the published answer. One question, three cards' machinery: projectile in, restitution at the wall, projectile out.

## Where this is the working tool

**Sports law is written in $e$.** Beyond the ping-pong and basketball drop tests: the USGA caps a golf driver's face at $e = 0.83$ against a golf ball — the "trampoline effect" limit that club designers engineer up against to the third decimal — and American college baseball regulates bats through a standard literally *named* after this card: **BBCOR**, "Batted-Ball Coefficient of Restitution," capped at 0.50 to keep aluminium bats from outhitting wood. When a sport's governing body wants to control equipment, this number is the handle it grabs.

**Crash engineering wants $e \approx 0$ on purpose.** The energy-loss formula says the kinetic energy destroyed is largest at $e = 0$ — and in a car crash, *destroyed in the structure* means *not delivered to the passengers*. A crumple zone is a machine for making the collision as inelastic as possible: the [[Linear Momentum]] card's crumpling car, now with its design goal stated as a coefficient. (The other half of the safety story — stretching the impact time — is [[Braking Systems]]' territory.)

**Snooker, pool, 台球.** Ball-on-ball impacts run the oblique machinery at $e \approx 0.95$; cushions are engineered around $e \approx 0.6$ with $\tan\beta = e\tan\alpha$ deciding every off-the-rail position; and the referee's pre-match ball cleaning exists because chalk dust changes the *pair's* surfaces — and therefore $e$ itself.

## Common Misconceptions (Teaching Notes)

### 1. "This ball has $e = 0.8$"

$e$ is a property of the **pair** of surfaces, not of one object — the same ball scores differently on steel, wood and carpet. The drop-test regulations all name both parties (ball *and* steel block) for exactly this reason. Exam questions grant the shortcut "the coefficient of restitution between $A$ and $B$" — read the "between".

### 2. "Apply NEL along any convenient direction"

NEL acts **along the line of centres only** — the only direction the smooth surfaces can push. The perpendicular direction is friction's business, and *smooth* means friction resigned. Applying $e$ to a full speed in an oblique problem (rather than to the line-of-centres component) is the standard route to a wrong answer that still looks algebraic and busy.

### 3. "An inelastic collision loses momentum"

Momentum is conserved in **every** collision — elastic, inelastic, explosive, all of them; nothing in $e$ touches it. What varies with $e$ is *kinetic energy*, per the $(1-e^2)$ formula. On a mark scheme this confusion shows up as an "energy conservation" equation written for a collision with $e < 1$ — an equation that is simply false there.

### 4. "$e = 0.5$ means half the energy (or half the height) survives"

The heights and energies go as $e$ **squared**: a ball with $e = 0.5$ rebounds to a *quarter* of its drop height, and the two-body energy loss carries $1 - e^2$. Linear-in-$e$ intuitions fail every numerical check; the drop-test formula $e = \sqrt{h_1/h_0}$ is the antidote worth memorising.

### 5. "A negative $e$ means the ball bounced backwards"

A negative $e$ means **your signs disagree between the two equations** — nothing physical. The June 2026 scheme's own guidance prices it: correct-looking working with inconsistent signs earns method marks and loses the answer. Fix the positive direction once, audit both equations against it, and $e$ lands in $[0, 1]$ where it belongs.

## Beyond the syllabus

> [!info] The infinite bounce that takes finite time
> Recall the bounce heights fall as $h_0, e^2h_0, e^4h_0, \dots$ — geometric with ratio $e^2$. The total distance ever travelled is then a geometric series, $h_0\,\dfrac{1+e^2}{1-e^2}$, and the total *time* is a geometric series too (ratio $e$) — both **finite**, though the ball bounces infinitely many times. A ball with $e = 0.9$ dropped from 1 m travels about 9.5 m of vertical distance across its infinitely many bounces, and finishes bouncing at a definite, computable moment. Zeno's paradox, resolved by a toy: infinitely many events fit comfortably inside finite time when they shrink geometrically.

> [!info] The fine print on "constant"
> Like Ohm's law in [[Resistance]], NEL is an empirical rule with a domain of validity: real coefficients drift with impact speed (falling as impacts get violent enough to deform plastically), with temperature (a squash ball is nearly dead cold and lively warm — the pre-match warm-up of the *ball* is real), and with spin, which drags friction back into the story the "smooth" model excludes. The exam's constant-$e$, smooth-sphere world is a model — an excellent one for hard balls at modest speeds, which is exactly the regime the questions inhabit.

> [!info] Why $e > 1$ is forbidden — and what a superball is not
> $e > 1$ would mean separating faster than approaching: kinetic energy *created* by contact, which the energy ledger forbids for passive materials (the $(1-e^2)$ formula would go negative). A superball's party trick is not $e > 1$ but $e \approx 0.92$ — remarkably little loss — plus spin effects that make its *direction* changes look impossible. The genuine exceptions cheat by storing energy in advance: a chemistry-class "popper" or an explosive separation is $e > 1$ only because something *other than the impact* paid.

## Exam Notes

### Cambridge 9231 (Further Mechanics, Paper 3) — §3.6

The syllabus's own two bullets: recall Newton's experimental law, the definition of $e$, the property $0 \le e \le 1$, and the meaning of *perfectly elastic* ($e=1$) and *inelastic* ($e=0$); then use conservation of momentum and/or NEL for problems modelled as **direct or oblique impact of two smooth spheres, or of a smooth sphere with a fixed surface** — this card's three worked shapes, each from a recent real paper. Recurring joints: the momentum equation with masses correct (M1), NEL **with signs consistent with the momentum equation** (M1, the scheme's own phrase), and the perpendicular-component preservation stated, not assumed, in oblique work. Hybrids with [[Projectile Motion]] are a live pattern (Example 3), and $g = 10$ is mandatory on this paper — schemes print "B0 if not using g = 10". Definition-recall is also directly examinable: be able to *state* the law in words.

### Edexcel IAL — Further Mechanics M2

M2.4.2–4.3: direct impact with $e$ including the inequalities $0 \le e \le 1$, loss of mechanical energy due to impact, and **successive impacts** of up to three particles or two particles and a plane surface — the multi-collision chains this card's machine handles one collision at a time. The spec draws one boundary in its own words: *"collision with a plane surface will not involve oblique impact"* — so the oblique half of this card is 9231-only for an IAL student.

### Where it is *not* examined

- **Cambridge 9709 (P4)** — in the syllabus's own words, *"knowledge of impulse and the coefficient of restitution is not required"*: P4 collisions are coalescence only, the $e=0$ world [[Linear Momentum]] covers.
- **OxfordAQA 9660** — likewise verbatim: *"knowledge of Newton's law of restitution is not required"* (M1.4's fixed-surface impacts are perpendicular and $e$-free).
- **Cambridge 9702 / 0625 (Physics)** — no coefficient; but 9702 §3.3's "recognise elastic collisions by relative velocity reversal" *is* this card's law at $e = 1$, so the concept crosses the fence even though the symbol doesn't.
- **AP Physics 1 / C, IB Physics** — collisions are classified elastic/inelastic by energy audit; the coefficient itself is not on the specification.

## Connections

- **Builds on:** [[Linear Momentum]] — the conservation half of the machine, the collision taxonomy this card's $e$ parametrises, and the cliff edge (one equation, two unknowns) this card resolves; [[Projectile Motion]] — the resolve-into-components craft, and the hybrid exam shape where flight and bounce chain together; [[Vectors in Physics]] — components along and perpendicular to a chosen axis.
- **Kindred:** [[Centre of Mass]] — the $e$-independent part of every collision: the centre of mass sails through unmoved; [[Work, Energy and Power]] — where the $(1-e^2)$ energy goes; [[Braking Systems]] — the crumple zone as engineered $e \approx 0$; [[Resistance]] — the sibling lesson that an "empirical law" is a materials fact with fine print.
- **For 9231 students:** [[MF19 Reference (9709)]] — nothing from this card is printed on the formula sheet: the definition of $e$, both equations of the machine, and $e = \sqrt{h_1/h_0}$ all live in your head.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $e = \dfrac{v_2 - v_1}{u_1 - u_2}$ | `e = \dfrac{v_2 - v_1}{u_1 - u_2}` | the coefficient, in one consistent direction |
| $0 \le e \le 1$ | `0 \le e \le 1` | the property the syllabus names |
| $e = \sqrt{h_1/h_0}$ | `e = \sqrt{h_1/h_0}` | the drop test |
| $\tan\beta = e\tan\alpha$ | `\tan\beta = e\tan\alpha` | oblique wall rebound (angles to the wall) |
| $\tfrac12\frac{m_1 m_2}{m_1+m_2}(1-e^2)(u_1-u_2)^2$ | `\tfrac12\frac{m_1 m_2}{m_1+m_2}(1-e^2)(u_1-u_2)^2` | kinetic energy destroyed |

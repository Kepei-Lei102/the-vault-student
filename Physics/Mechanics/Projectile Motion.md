---
chinese: 抛体运动 (pāotǐ yùndòng)
prerequisites:
  - "[[SUVAT]]"
  - "[[Vectors in Physics]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Work, Energy and Power]]"
leads_to:
  - "[[Newton's Law of Restitution]]"
  - "[[Circular Motion]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/OxAQA-9660
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-2-1
  - syllabus/9231-3-1
  - syllabus/IB-Physics-A-1-2
  - syllabus/AP-Physics-1-1-5
  - syllabus/AP-Physics-C-Mech-1-5
  - type/deep
  - misconception/horizontal-velocity-decays
  - misconception/velocity-zero-at-top
  - misconception/45-degrees-always-optimal
  - misconception/fired-bullet-falls-slower
---

# Projectile Motion 抛体运动

> *Put two coins on the table's edge. Flick one so it flies off fast; nudge the other so it simply drops. Listen: **one click.** They land at the same instant, every time, no matter how hard you flick — because gravity does not care in the slightest how fast something is moving sideways. That one indifference is the entire theory of this card. Everything else is bookkeeping.*

## 中文锚点

抛体运动只有一个核心思想：**水平和竖直互不干涉**。桌边同时弹出一枚硬币、放落另一枚——不管弹得多快，两枚**同时落地**，因为重力只作用在竖直方向，对水平速度不闻不问。于是一条抛物线拆成两道一维题：水平方向没有力，速度 $V\cos\theta$ **恒定不变**；竖直方向就是匀加速直线运动（[[SUVAT]] 原封不动再用一次），初速 $V\sin\theta$、加速度 $-g$。两道题**唯一共享的量是时间 $t$**——时间是唯一的桥。飞行时间、射程 $\dfrac{V^2\sin 2\theta}{g}$（45° 最远；互补角射程相同）、最大高度 $\dfrac{V^2\sin^2\theta}{2g}$ 全都由此推出——但这三条公式**默认落点与出发点同高**，题目一旦不同高（考题几乎都不同高），回到分量重推，别背。9231 的招牌技巧是**轨迹方程**：把 $t$ 消掉得 $y = x\tan\theta - \dfrac{gx^2}{2V^2\cos^2\theta}$（MF19 印了这条，但大纲要求会**推导**），再用 $\sec^2\theta = 1+\tan^2\theta$ 把它变成 **关于 $\tan\theta$ 的一元二次方程**——发射角未知的题全靠它。常见误区：抛体在最高点速度不为零（只是竖直分量为零，水平分量还在）；上升和下降不是两个阶段，全程加速度都是同一个竖直向下的 $g$。

| English | 中文 | one-line meaning |
|---|---|---|
| projectile | 抛体 | anything in flight under gravity alone |
| components | 分量 | the one resolve at launch: $V\cos\theta$ across, $V\sin\theta$ up |
| time of flight | 飞行时间 | the shared clock — the only bridge between the two axes |
| range | 射程 | horizontal distance back to launch height |
| greatest height | 最大高度 | where $v_y = 0$ (and *only* $v_y$) |
| trajectory equation | 轨迹方程 | the path with time eliminated: $y$ as a function of $x$ |
| angle of projection | 抛射角 | $\theta$ above the horizontal — unknown-θ problems are quadratics in $\tan\theta$ |

## The model — and what it quietly assumes

A **projectile** is modelled as a *particle* moving *freely under gravity*: after launch, the only force is weight, so the acceleration is $g$ vertically downward — constant in size and direction — from the moment of release to the moment of landing. The model's fine print, which the 9231 syllabus explicitly asks you to be able to state:

- **No air resistance.** Fine for a shot put or a thrown ball over tens of metres; badly wrong for a shuttlecock, a table-tennis ball, or anything fast and light. Air drag grows roughly with $v^2$, so the faster the flight, the bigger the lie.
- **No spin.** A spinning ball drags air around itself and swerves (the Magnus effect) — the free kick that bends around the wall is a *deliberate violation* of this model.
- **Uniform gravity, flat ground.** True to high accuracy over any playing field; false for missiles that fly far enough to notice the Earth curving away beneath them.

Inside those limits, the model is superbly accurate — and the syllabus note "*vector methods are not required*" is a kindness with a message in it: one resolve at launch, and everything after is arithmetic on components.

## The one idea: the two directions do not talk

Newton's second law is a **vector** statement, and gravity has no horizontal component. Read that as two separate sentences:

- **Horizontally:** no force → no acceleration → the horizontal velocity $u_x = V\cos\theta$ **never changes**. Distance across is simply $x = (V\cos\theta)\,t$.
- **Vertically:** constant force → constant acceleration $-g$ → ordinary [[SUVAT]], with $u_y = V\sin\theta$: $\;v_y = V\sin\theta - gt$, $\;y = (V\sin\theta)t - \tfrac12 g t^2$.

The two problems share exactly one quantity: **time**. Time is the only bridge — every projectile question is solved by crossing it. (Find *when* from one axis, use it in the other; that sentence is nine-tenths of the method.)

The coins prove the split experimentally: the flicked coin has a large $u_x$ and the dropped coin none, but their **vertical** stories — same start height, same $u_y = 0$, same $g$ — are identical, so they land together. Galileo saw it four centuries ago: projectile motion is *uniform motion and free fall superposed*, and neither disturbs the other.

> [!tip] If this chapter feels like "just trig + F = ma" — congratulations, you've understood it
> That reaction is exactly right, and worth saying out loud: **there is no new physics on this page.** [[Newton's Laws of Motion]] with only weight acting gives $\vec a = -g\,\hat{\jmath}$ — a vector equation whose horizontal component reads $a_x = 0$; trigonometry performs one resolve at launch; [[SUVAT]] runs twice. Every formula below is those three ingredients rearranged, and every "hard" question is the same three ingredients wearing a costume. What the topic actually trains — and what the exams are really pricing — is the *discipline of combining tools unprompted*: keeping two axes' books separately, crossing between them only through $t$, and re-deriving rather than reciting when the setup shifts. If you can re-derive this whole page from $F = ma$ and one triangle, you have not missed the point. You have got it.

![[projectile-motion-independence.svg|720]]

Three launch flavours, one machinery — only the initial components differ:

| launch | $u_x$ | $u_y$ | typical scene |
|---|---|---|---|
| **oblique** (angle $\theta$ up) | $V\cos\theta$ | $+V\sin\theta$ | thrown ball, shell, long jump |
| **horizontal** | $V$ | $0$ | ball rolling off a cliff or table |
| **below horizontal** (angle $\theta$ down) | $V\cos\theta$ | $-V\sin\theta$ | dart thrown downhill, package from a descending aircraft |

## The standard trio — derived, and their hidden small print

For a launch at speed $V$, angle $\theta$, **landing at the same height as launch** (watch that clause):

**Time of flight.** The flight ends when $y = 0$ again: $(V\sin\theta)t - \tfrac12 gt^2 = 0 \Rightarrow t = \dfrac{2V\sin\theta}{g}$ — twice the time to the top, because the vertical journey is symmetric.

**Range.** Horizontal speed × time of flight:
$$R = V\cos\theta \cdot \frac{2V\sin\theta}{g} = \frac{V^2 \sin 2\theta}{g}$$
*Tool: the double-angle identity $2\sin\theta\cos\theta = \sin 2\theta$ — and it repays the favour with two facts for free.* Since $\sin 2\theta$ peaks at $2\theta = 90°$: **maximum range at $\theta = 45°$**. And since $\sin 2\theta = \sin(180° - 2\theta)$: **complementary angles give equal range** — $30°$ and $60°$ land in the same place, one by a flat fast path, one by a slow high lob. (Footballers know both: the driven pass and the chip, same target.)

**Greatest height.** At the top $v_y = 0$ (the horizontal velocity is still very much alive — see the misconceptions): $0 = (V\sin\theta)^2 - 2gH \Rightarrow H = \dfrac{V^2\sin^2\theta}{2g}$.

> [!warning] The small print is where the marks die
> All three formulas assume the landing height equals the launch height. A ball thrown from a cliff, a shot released two metres up, a dart hitting a wall — **the trio does not apply**, and quoting it anyway is the single most common projectile error at every level. When heights differ, go back to components and solve the vertical SUVAT honestly. The trio is a *special case you can re-derive in four lines*, not a formula sheet to trust blindly.

![[projectile-motion-family.svg|740]]

## Velocity mid-flight — magnitude, direction, and the energy shortcut

The velocity at time $t$ has components $(V\cos\theta,\; V\sin\theta - gt)$: speed $\lvert v \rvert = \sqrt{v_x^2 + v_y^2}$, direction $\tan\phi = v_y / v_x$ (sign of $v_y$ tells you above or below the horizontal). The picture to carry: **the velocity vector's horizontal shadow never changes length; only the vertical part drains, empties at the top, then refills downward.**

And when a question asks only for *speed* at a given height — not direction — [[Work, Energy and Power]] offers the direction-blind shortcut: $v^2 = V^2 - 2gy$ (energy conservation, mass cancelled). No components, no time, one line. The trigger for it: the word *speed* together with a *height* and no mention of time.

![[projectile-motion-velocity.svg|720]]

## The trajectory equation — time eliminated, the 9231 signature

The path itself — $y$ as a function of $x$, no clock anywhere — comes from using the horizontal equation *as a dictionary for $t$*. Write both displacement equations down first, so it is clear what substitutes into what:

$$x = (V\cos\theta)\,t \qquad\qquad y = (V\sin\theta)\,t - \tfrac12 g t^2$$

Solve the first for $t = \dfrac{x}{V\cos\theta}$, and put that into **the $y$ equation**, term by term:

$$y = V\sin\theta \cdot \frac{x}{V\cos\theta} \;-\; \frac{g}{2}\left(\frac{x}{V\cos\theta}\right)^{2}$$

The first term: the $V$s cancel and $\dfrac{\sin\theta}{\cos\theta} = \tan\theta$, leaving $x\tan\theta$. The second term: square everything inside the bracket. Hence

$$y = x\tan\theta \;-\; \frac{g x^2}{2V^2\cos^2\theta}$$

A quadratic in $x$ with a negative leading coefficient: the parabola, proved rather than assumed. (MF19 prints this equation under Further Mechanics — but the 9231 learning objective says **derive and use**, and "derive" has been asked. The derivation is the two lines above; own them.)

Its power move, and the reason unknown-angle problems are FP-grade: with $\sec^2\theta = 1 + \tan^2\theta$,

$$y = x\tan\theta - \frac{gx^2}{2V^2}\left(1 + \tan^2\theta\right)$$

which — for a *known* target point $(x, y)$ and known $V$ — is a **quadratic in $\tan\theta$**. Two roots: the flat trajectory and the lob, the same pair of complementary-flavoured solutions the range formula promised. One root: the target sits exactly on the edge of reach. No real roots: unreachable at this speed. The discriminant of that quadratic is doing physics.

*The trigger that selects this tool:* the question gives **positions but no times** — coordinates, a point the particle "passes through", a barrier at a known distance. The moment time is absent from the given data, eliminate it from the equations too.

## Worked examples — real Paper 3 questions, every tool and trigger named

### Example 1 (9231 June 2026 Paper 33 Q7 — two projectiles, one collision)

> At $t = 0$, particle P is projected from ground point O at $25\ \text{m s}^{-1}$ at angle $\alpha$ above the horizontal, $\sin\alpha = \tfrac45$. At time $T$, particle Q is projected vertically upwards at $25\ \text{m s}^{-1}$ from the ground directly below P's greatest-height point. The particles collide when Q is travelling **upwards**, at the point where P reaches its **greatest height**. (a) Show they collide 2 s after P's launch. [1] (b) Find $T$. [3]

![[projectile-motion-q-collision.svg|680]]

**(a)** *Trigger: "greatest height" → the apex condition $v_y = 0$; tool: $v_y = u_y - gt$.* P's vertical launch component is $25 \times \tfrac45 = 20\ \text{m s}^{-1}$, so $20 - 10t = 0$ gives $t = 2$ ✓. (The published scheme demands the working from $25\sin\alpha$ **and** insists on $g = 10$ — writing $9.81$ here loses the mark on a maths paper. One mark, two traps.)

**(b)** *Trigger: two objects, two launch clocks → bookkeeping first, physics second.* The collision height is P's greatest height: $H = \dfrac{20^2}{2 \times 10} = 20$ m. Q has been flying for $(2 - T)$ seconds when the collision happens; call that $t_Q$. *Tool: vertical SUVAT for Q:* $25t_Q - 5t_Q^2 = 20 \Rightarrow t_Q^2 - 5t_Q + 4 = 0 \Rightarrow t_Q = 1$ or $4$. *Trigger for choosing: "Q is travelling upwards"* — Q rises until $t_Q = 2.5$, so $t_Q = 1$. Hence $T = 2 - 1 = \boxed{1\ \text{s}}$. (The rejected root is not waste: $t_Q = 4$ is Q passing 20 m again on the way down — the question's "upwards" clause exists precisely to make you choose.)

### Example 2 (9231 June 2025 Paper 33 Q7 — direction of motion at time $T$)

> P is projected from O with speed $U$ at $45°$ above the horizontal. (a) State the velocity components at time $t$. [1] At time $T$, P is moving at $60°$ **below** the horizontal. (b) Show $T = \dfrac{U}{2g}\left(\sqrt2 + \sqrt6\right)$. [3]

![[projectile-motion-q-direction.svg|680]]

**(a)** $v_x = \dfrac{U}{\sqrt2}$ (constant, forever); $v_y = \dfrac{U}{\sqrt2} - gt$.

**(b)** *Trigger: "moving at [angle]" → direction of motion is the velocity vector's angle; tool: $\tan\phi = v_y / v_x$ — with the sign carrying "below".* Below the horizontal means $v_y$ is negative while $v_x$ stays positive:
$$\frac{\frac{U}{\sqrt2} - gT}{\frac{U}{\sqrt2}} = \tan(-60°) = -\sqrt3 \;\Rightarrow\; \frac{U}{\sqrt2} - gT = -\sqrt3\,\frac{U}{\sqrt2}$$
$$gT = \frac{U}{\sqrt2}\left(1 + \sqrt3\right) \;\Rightarrow\; T = \frac{U(1+\sqrt3)}{\sqrt2\, g} = \frac{U(\sqrt2 + \sqrt6)}{2g} \checkmark$$
*Tool for the last step: rationalise — multiply through by $\tfrac{\sqrt2}{\sqrt2}$.* The physics was one line; the show-that mark is mostly surd hygiene.

### Example 3 (9231 November 2025 Paper 34 Q2 — the trajectory equation earning its keep)

> P is projected at $u\ \text{m s}^{-1}$ at angle $\theta$ above the horizontal, $\tan\theta = 2$. (a) Use the MF19 trajectory equation to show $y = 2x - \dfrac{25x^2}{u^2}$. [1] (b) P passes through $(8, 12)$, then hits a vertical barrier **7 m high** at horizontal distance $D$ m. Find the set of possible values of $D$. [5]

![[projectile-motion-q-barrier.svg|700]]

**(a)** *Trigger: position variables $x, y$, no time anywhere → trajectory equation.* $\tan\theta = 2 \Rightarrow \cos^2\theta = \tfrac15$ (right triangle: sides 1, 2, hypotenuse $\sqrt5$). Then $y = 2x - \dfrac{10\,x^2}{2u^2 \cdot \tfrac15} = 2x - \dfrac{25x^2}{u^2}$ ✓.

**(b)** *Through $(8,12)$:* $12 = 16 - \dfrac{25 \times 64}{u^2} \Rightarrow u^2 = 400$, so $y = 2x - \dfrac{x^2}{16} = \dfrac{x(32 - x)}{16}$. *Trigger: "hits a barrier of height 7" → the particle strikes the barrier's face if, at $x = D$, it is at height between 0 and 7 — and it must still be airborne.* Two boundary solves (exactly the scheme's two method marks): $y = 7 \Rightarrow D = 4$ or $28$; $\;y = 0 \Rightarrow D = 32$. The particle passes $(8, 12)$ — already above 7 m and beyond $D = 4$ — so it clears any barrier nearer than 28 m and is underground past 32: $\boxed{28 \le D \le 32}$. (The scheme accepts strict inequalities; what it will not accept is a bare $D = 28$ — the word **set** in the question is the trigger that an interval is wanted.)

## Where this is the working tool

**Ballistics built the computer.** A real artillery shell violates the no-drag clause badly, so its path has no clean formula — each trajectory must be integrated step by step, and a gun crew needs a *firing table*: thousands of pre-computed trajectories for combinations of range, charge, and wind. In the 1940s one table took a room of human computers a month. The machine commissioned by the US Army's Ballistic Research Laboratory to do it electronically — for exactly this projectile problem — was **ENIAC** (1945), the machine that begins the lineage every [[Von Neumann machine]] card in this vault descends from. The parabola on this page, plus air resistance, is the reason electronic computing got funded.

**Sport reads the small print.** The 45° optimum holds only for the launch-height-equals-landing-height special case, so real events sit elsewhere: shot-putters release around $37°$–$42°$ (the shot starts two metres up, which favours flatter); long jumpers take off near $20°$ (they cannot convert sprint speed into launch angle without losing most of it — so they keep the speed and accept the low angle); a basketball's high arc buys a *steeper descent* into the hoop, which enlarges the effective target. Every one of these is the trio's small print, monetised.

## Common Misconceptions (Teaching Notes)

### 1. "The horizontal velocity gets used up during flight"

Nothing horizontal is acting — no force, no change, full stop. The horizontal velocity at landing equals the horizontal velocity at launch, to the last decimal. What creates the illusion of slowing is the *path* steepening as $v_y$ grows; the horizontal shadow keeps perfectly constant pace. (This is [[Newton's Laws of Motion]]' first law, in the one direction where it gets to act unmolested.)

### 2. "At the top, the velocity is zero"

Only $v_y$ is zero. The projectile crosses its apex at full horizontal speed $V\cos\theta$ — that's *why it keeps going* rather than dropping straight down. Corollary the exam loves: the **minimum speed** of a projectile occurs at the top and equals $V\cos\theta$, not zero. (A vertically-thrown ball is the special case $\cos\theta = 0$, which is the only time "zero at the top" is true.)

### 3. "45° gives maximum range, always"

Only launch-to-same-height. From a cliff, flatter beats 45°; up to a platform, steeper does. The honest statement: 45° maximises $\frac{V^2\sin2\theta}{g}$, which is the range *back to launch height*. When an exam question changes the landing height and still expects the trio, it doesn't — that's the trap.

### 4. "Going up it decelerates, coming down it accelerates — two phases"

One phase. The acceleration is $g$ downward from release to landing, unchanged at the top, unchanged everywhere — what flips is only the *sign of $v_y$ relative to it*. Treating up and down as different regimes is where sign errors breed; set up axes once (up positive, $a = -g$), and let the algebra carry the signs.

### 5. "A fired bullet stays up longer than a dropped one"

Fired horizontally over flat ground, a bullet and a bullet dropped from the same height land **at the same instant** — the fired one just lands far away. Nobody believes it before the coins; nobody argues after. (The classroom deluxe version is the *monkey and hunter*: aim a dart straight at a hanging target that releases its grip at the moment of firing — the dart's drop below the aim line and the target's fall are the identical $\tfrac12 gt^2$, so they meet in mid-air. Aiming "correctly" — above, to allow for drop — is exactly how to miss.)

![[projectile-motion-see-it-run.mp4]]

## Beyond the syllabus

> [!info] The bounding parabola — the envelope 9231 names only to exclude
> The syllabus note says "knowledge of the 'bounding parabola' for accessible points is not included" — which is an invitation. Fix launch speed $V$, allow *every* angle: which points $(x, y)$ can be hit at all? The trajectory quadratic in $\tan\theta$ has real solutions exactly when its discriminant is non-negative, and the boundary (discriminant $= 0$) is itself a parabola:
> $$y = \frac{V^2}{2g} - \frac{g x^2}{2V^2}$$
> — the **envelope of safety**, snug over the whole family of trajectories, touching each one once. Inside it, every point is reachable by two angles; on it, by exactly one; beyond it, by none. A fountain's spray fills exactly this shape, and an anti-aircraft battery's protected airspace is its complement.

> [!info] Air resistance, honestly
> Add drag and the two directions *start talking* — drag acts against the velocity, which mixes the components, and the clean split dies. With drag proportional to $v$ the equations still solve ([[Differential Equations]]: each component decays exponentially toward the terminal state); with the more realistic $v^2$ drag there is no closed form, only numerical integration — ENIAC's job, above. Qualitatively, three exam-worthy effects: the trajectory becomes **asymmetric** (steeper coming down than going up), the range **shrinks**, and the optimal angle drops **below 45°**. Fall for long enough and the vertical motion approaches **terminal speed** — drag grown to match weight, acceleration zero — which is why raindrops arrive at a survivable few metres per second instead of at bullet speed.

> [!info] The vector dialect
> The "resolve into components" recipe is one honest equation wearing separated clothes: $\vec r(t) = \vec u\,t + \tfrac12 \vec g\, t^2$ — displacement is the launch-velocity line *plus* a growing droop $\tfrac12\vec g t^2$ straight down. That one-liner is the AP Physics C dialect, and it makes the monkey-and-hunter proof a single sentence: both dart and monkey droop by the identical $\tfrac12 \vec g t^2$ below where they would otherwise be, so a straight aim cannot miss.

## Exam Notes

### Cambridge 9231 (Further Mechanics, Paper 3 — §3.1)

The projectile home ground, and the deepest treatment of any board. All three learning objectives are examined: the **model and its limitations** (state air resistance / spin / the particle idealisation), **component problems** (velocity magnitude-and-direction at a time or position, range, greatest height — Examples 1 and 2 are the live shapes, including multi-projectile timelines), and the **trajectory equation** — which MF19 prints, but the LO says *derive and use*, so the two-line derivation is examinable; unknown speed and/or angle problems run through the quadratic-in-$\tan\theta$ (Example 3). Two mechanical traps with mark-scheme receipts: **$g = 10$ is mandatory** (a June 2026 scheme awards B0 for $9.81$), and answer-set questions ("find the set of values of $D$") want intervals, not endpoints. The bounding parabola is excluded by name. 9709 P4 knowledge is assumed.

### Cambridge 9702 (A-Level Physics)

§2.1's final bullet is this card in one sentence: *describe and explain motion due to a uniform velocity in one direction and a uniform acceleration in a perpendicular direction*. Expect qualitative describe-and-explain plus quantitative two-axis problems within SUVAT scope (Paper 1 MCQs and Paper 2 structured parts — cliff launches and horizontal projection are the favourites), with **$g = 9.81$**, not 10. The independence argument itself — no horizontal force, so no horizontal acceleration — is creditworthy language.

### Cambridge 9709 / 0625

**Not examined at either — and the 9709 gap surprises people.** A-Level Maths Mechanics (P4) is strictly straight-line: projectiles are deferred entirely to Further Maths. 0625 goes no further than 1D falling with and without air resistance. State-school intuition says "Mechanics = projectiles"; Cambridge's split says projectiles begin at 9231 and 9702.

### Edexcel IAL / OxAQA 9660

IAL examines projectiles at **M2.1.2**; OxAQA 9660 at **M2.5**, with the syllabus's own component equations $x = (V\cos\alpha)t$, $y = (V\sin\alpha)t - \tfrac12 gt^2$. Both stay at the component-method level — the trajectory-as-quadratic-in-$\tan\theta$ machinery is 9231's extra floor — and both take $g = 9.8$ unless told otherwise (read the paper's front cover).

### IB Physics (A.1)

A.1.2 names projectile motion in all three launch flavours — horizontal, oblique, and *below*-horizontal — plus the **qualitative effect of air resistance** on trajectory shape (asymmetry, reduced range) and **terminal speed**: the Beyond-syllabus callout above is IB-examinable in words-and-sketch form. Data booklet carries the SUVAT set; expect fluid-drag *qualitative*, never the drag ODE.

### AP Physics 1 / AP Physics C: Mechanics

AP-1 §1.5 does projectiles by components with the standard FRQ shapes (cliff launch, angled launch, compare-two-trajectories reasoning prompts). AP-C §1.5 speaks the vector dialect — $\vec r(t) = \vec r_0 + \vec v_0 t + \tfrac12 \vec g t^2$, calculus expected — and its FRQs happily differentiate or integrate mid-problem. Both use $g = 9.8$; AP-1 loves the misconception set above as multiple-choice distractors, almost verbatim.

## Connections

- **Builds on:** [[SUVAT]] — used twice per problem, once per axis, exactly as its closing section promised; [[Vectors in Physics]] — the one resolve at launch, and components as the vector's shadows; [[Newton's Laws of Motion]] — the first law running the horizontal axis, the second running the vertical; [[Work, Energy and Power]] — the direction-blind speed shortcut $v^2 = V^2 - 2gy$.
- **Leads to:** [[Circular Motion]] — the other constant-magnitude-acceleration motion, and the two share a border: a vertical circle's string going slack releases the mass into *this card* (the slack-to-projectile handover its vertical-circle section works).
- **Kindred:** [[Differential Equations]] — where the trajectory goes when drag arrives and the axes start talking; [[Kinematics Calculus]] — the pure-maths face of the same chain; [[Gravitational Fields]] — stop pretending gravity is uniform and the parabola bends into an ellipse: Newton's cannon is this card fired hard enough to notice; [[Von Neumann machine]] — the firing-table crisis that turned this chapter's arithmetic into the first electronic computer.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $R = \dfrac{V^2 \sin 2\theta}{g}$ | `R = \dfrac{V^2 \sin 2\theta}{g}` | range, launch-to-same-height only |
| $y = x\tan\theta - \dfrac{gx^2}{2V^2\cos^2\theta}$ | `y = x\tan\theta - \dfrac{gx^2}{2V^2\cos^2\theta}` | trajectory equation (printed in MF19; derivation examinable) |
| $\sec^2\theta = 1 + \tan^2\theta$ | `\sec^2\theta = 1 + \tan^2\theta` | the move that makes unknown-angle problems quadratics in $\tan\theta$ |
| $\vec r = \vec u t + \tfrac12 \vec g t^2$ | `\vec r = \vec u t + \tfrac12 \vec g t^2` | the vector dialect (AP-C) |

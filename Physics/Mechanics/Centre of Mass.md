---
chinese: 质心 (zhìxīn)
prerequisites:
  - "[[Forces and Equilibrium]]"
  - "[[Linear Momentum]]"
  - "[[Torque]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Integration]]"
leads_to:
  - "[[Centres of Mass by Integration]]"
  - "[[Moment of Inertia]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/OxAQA-9660
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9231-3-2
  - syllabus/AP-Physics-1-2-1
  - syllabus/AP-Physics-C-Mech-2-1
  - type/deep
  - misconception/com-must-be-inside-the-body
  - misconception/com-is-geometric-centre
  - misconception/topple-and-slide-are-the-same-question
  - misconception/com-needs-gravity
---

# Centre of Mass 质心

> *Throw a hammer across the room. It tumbles — head over handle, ugly and complicated, and no point on it traces anything you could write an equation for. Except one. Somewhere near the head there is a single point that ignores the whole circus and draws a clean parabola through the air, exactly as if the hammer were a marble. Every time you have been told "treat the object as a particle," it was a promise about that point. This card is where the promise is kept.*

## 中文锚点

只要你练过任何一项运动，教练一定朝你喊过那三个字："重心放低！"防守时蹲低，起跑时前倾，过弯时压低身体——为什么"低"就是稳？**质心**就是答案的主角：它是整个身体"按质量加权的平均位置"——每块质量乘以它的位置，加起来，除以总质量。站直时，人的质心大约在肚脐附近；一蹲下，它跟着降。而"稳"的判据只有一条：**从质心竖直向下画的重力作用线，必须落在支撑面之内**——你脚下的那块"地盘"。质心越低，同样的推搡和倾斜里，作用线越不容易跑出地盘，所以蹲低的防守者更难被推倒；柔道和摔跤的整套学问，就是把对手的质心"请"出他的支撑面，同时守住自己的。走路其实是**可控的翻倒**：每一步都故意让质心越出支撑脚的地盘，再用新落地的脚接住它。跳高的背越式最妙：身体反弓着过杆，**质心可以从杆底下钻过去**——身体的每一部分都过了杆，质心却没有。是的，质心不必在身体内部：甜甜圈的质心就在洞里。这一切背后有一条定理撑腰：**质心的运动，就像一个质量为 $M$ 的质点、只受外力**——内力全被牛顿第三定律成对抵消。所以锤子翻着跟头飞，质心照样画出干净的抛物线；烟花在空中炸开，碎片四散，碎片们的质心仍沿原来的抛物线走完全程。找质心有四招，从便宜到贵：**对称性**（免费——均匀矩形的质心就在正中）、**标准结果**（三角形在中线上离顶点 $\tfrac23$ 处）、**组合体**（切成几块，列表取矩）、**挖去法**（挖掉的那块按"负面积"记，同一张表照用）。斜坡上还有一场比赛：作用线先跑出底面就**翻倒**（$\tan\theta = w/H$），摩擦先撑不住就**滑动**（$\tan\theta = \mu$）——又高又窄的先翻，又矮又宽的先滑，SUV 比跑车容易侧翻，道理全在这。

| English | 中文 | one-line meaning |
|---|---|---|
| centre of mass | 质心 | the mass-weighted average position of a body |
| centre of gravity | 重心 | where the total weight acts; same point in a uniform field |
| lamina | 薄片 / 层片 | a flat plate of negligible thickness — mass $\propto$ area |
| uniform | 均匀的 | same density throughout, so density cancels out |
| composite body | 组合体 | a shape built from standard pieces (or with pieces removed) |
| moments (taking) | 取矩 | $M\bar{x} = \sum m_i x_i$ — the equation that locates the point |
| median | 中线 | vertex to opposite midpoint; the triangle's centroid sits on it |
| topple | 翻倒 | rotate about a base edge when the weight-line escapes the base |
| base of support | 支撑面 | the footprint the weight-line must stay inside |
| suspend | 悬挂 | hang from a point — the centre of mass settles directly below |

## The problem, before the tool

Look back at what this vault has been doing. [[SUVAT]] treated a braking car as a point. [[Projectile Motion]] treated a thrown ball as a point. [[Gravitational Fields]] treated the Moon — two thousand kilometres of rock — as a point. Every one of those cards opened with some version of *"model the object as a particle"* and moved on.

Each of those was an IOU — an *"I owe you"*, the note you write when you take something now and promise to pay for it later — and the bill is now due. Real objects are not points. They spin, they tumble, they have parts that move differently from other parts. When a diver leaves the board she rotates twice before entering the water; no point of the diver is doing anything as simple as a parabola. So on what authority did we ever replace a body by a dot?

The hunter's question — *what stays simple when everything else is complicated?* — has an exact answer, and it is a **single point**. Not a convenient fiction: a theorem. Find that point and the particle model stops being an approximation and becomes the literal truth about it.

## The definition

The letters first, because the whole card is written in them. Take a system of particles — the parts of a hammer, the limbs of a gymnast — and label them $1, 2, 3, \dots$: particle $i$ has mass $m_i$ and sits at position $\mathbf{r}_i$. Two capital letters then belong to the *system as a whole*: $M$ is the **total mass**, $M = m_1 + m_2 + \cdots = \sum m_i$, and $\mathbf{R}$ is the **position of the centre of mass** — the point this card is about. (Capitals for the whole, lower-case for the pieces.) With every symbol now on the table, the definition is one line — the centre of mass is the mass-weighted average of the positions:

$$\mathbf{R} = \frac{\sum m_i \mathbf{r}_i}{\sum m_i} = \frac{1}{M}\sum m_i \mathbf{r}_i$$

In practice you work in Cartesian coordinates, one axis at a time: $\mathbf{R} = (\bar{x}, \bar{y})$, the bar meaning "average of". Written that way, with the total mass cleared to the left, it becomes the form the exam actually uses:

$$M\bar{x} = \sum m_i x_i, \qquad M\bar{y} = \sum m_i y_i$$

Read that second form aloud and you will hear [[Torque]]: *mass times distance, summed.* It is the principle of moments with mass in place of force — which is no accident, and §"Why gravity obeys it too" collects the debt.

Two conveniences make the arithmetic much lighter than it looks:

- **Uniform lamina → use area.** If a flat plate has constant density $\rho$ and thickness $t$, then each piece's mass is $\rho t \times (\text{its area})$, and the common factor $\rho t$ appears in every term of $\sum m_i x_i$ *and* in $M$. It cancels. **For a uniform lamina you may put areas where masses belong** — and the same argument lets you use lengths for uniform wires and volumes for uniform solids.
- **The origin is yours to choose.** $\mathbf{R}$ is a location, not a number, so put the origin wherever the algebra is cheapest — usually a corner of the figure, so that as many coordinates as possible are zero. (The same choice-of-axes freedom [[Vectors in Physics]] makes for forces.)

## Why the point earns its name

Here is the theorem that does all the work. Take the definition and differentiate twice with respect to time:

$$M\mathbf{R} = \sum m_i \mathbf{r}_i \;\Longrightarrow\; M\frac{d^2\mathbf{R}}{dt^2} = \sum m_i \frac{d^2\mathbf{r}_i}{dt^2} = \sum \mathbf{F}_i$$

The last step is just [[Newton's Laws of Motion]] applied to each particle. Now split every force into **internal** (exerted by one part of the system on another) and **external** (from outside). By Newton's third law the internal forces come in equal-and-opposite pairs, and *both members of each pair appear in that sum* — so they cancel, exactly, in pairs. What survives is:

$$\boxed{\;M\frac{d^2\mathbf{R}}{dt^2} = \mathbf{F}_{\text{ext}}\;}$$

Read it slowly, because it is one of the most useful sentences in mechanics: **the centre of mass of any system — rigid or not, spinning or not, held together or flying apart — accelerates exactly as a single particle of mass $M$ acted on by the external forces alone.**

That is the IOU paid in full. It also produces a small collection of facts that feel like magic and are merely this theorem:

- The tumbling hammer's centre of mass traces the clean parabola of [[Projectile Motion]], because gravity is the only external force and it does not care what the hammer is doing internally.
- A firework shell that **explodes** in mid-air scatters burning fragments everywhere — and their centre of mass continues along the original parabola without a flicker, because the explosion is entirely internal. (Until air resistance, an external force, gets a vote.)
- You cannot move your own centre of mass by any internal effort. Astronauts floating free can twist and turn — cats famously land feet-first this way — but no amount of thrashing shifts the centre of mass a millimetre. Something outside must push.

![[centre-of-mass-see-it-run.mp4]]

*Three acts: the thrown hammer, whose handle tip scrawls loops while one point draws a parabola; the theorem, with the internal forces struck out in pairs; and the shell that explodes at the top of its flight while its centre of mass keeps the appointment.*

> [!info] Why gravity obeys it too — the centre of *gravity*
> The card's other half needs a second fact: gravity, acting on every particle of a body, can be replaced by one force $Mg$ acting at one point. Total weight is $\sum m_i g = Mg$, fine — but why does the *turning effect* also come out right? Take moments about the origin: the true total moment of gravity is $\sum (m_i g) x_i = g \sum m_i x_i = g M \bar{x}$, which is exactly the moment of a single force $Mg$ placed at $\bar{x}$. The two are equal **because the definition of $\bar{x}$ is a moments equation**. So for a uniform field, the centre of gravity (重心) and centre of mass (质心) are the same point, and 9231's second learning objective — "the effect of gravity on a rigid body is equivalent to a single force acting at the centre of mass" — is this line. They part company only when $g$ varies measurably across the body, which needs an object the size of a small moon.

## Finding it — four tools, cheapest first

### 1. Symmetry — free, and always try it first

If a uniform body has a line of symmetry, the centre of mass lies **on** that line: every mass element on one side is matched by a mirror twin whose contribution cancels the imbalance. Two lines of symmetry, and you have the point by intersection. A uniform rectangle: centre. A uniform disc: centre. A uniform triangle: on each median (a fact §2 sharpens). This is the whole of 9231's "identify the position of the centre of mass of a uniform body using considerations of symmetry", and it converts many exam parts into one line — the N25/31 answer $\bar{y} = a$ below is a symmetry answer, worth a mark, costing nothing.

### 2. Standard results — printed, not memorised

Cambridge prints these on **MF19**, and the syllabus says explicitly that proofs of the printed results are not required:

| Uniform body | Centre of mass |
|---|---|
| Triangular lamina | $\tfrac23$ along the median from the vertex |
| Solid hemisphere, radius $r$ | $\tfrac38 r$ from the centre |
| Hemispherical shell, radius $r$ | $\tfrac12 r$ from the centre |
| Circular arc, radius $r$, angle $2\alpha$ | $\dfrac{r\sin\alpha}{\alpha}$ from the centre |
| Circular sector, radius $r$, angle $2\alpha$ | $\dfrac{2r\sin\alpha}{3\alpha}$ from the centre |
| Solid cone or pyramid, height $h$ | $\tfrac34 h$ from the vertex |

Not required is not the same as not worth seeing: every row of that table can be *earned* with one well-chosen slice and one integral, and [[Centres of Mass by Integration]] does exactly that, picture by picture, for all six. Here the triangle gets its derivation in full, because you use it constantly:

**The triangle's centroid, derived.** Cut the triangle into thin strips parallel to one side. Each strip's own centre of mass is at its midpoint, and the midpoints of all strips parallel to a side lie on the **median** from the opposite vertex — so the centre of mass is somewhere on that median. Repeat with strips parallel to a different side: it is on that median too. So it is at the intersection of the medians, and (a standard geometry result) that point sits $\tfrac23$ of the way from each vertex. Coordinates make it even friendlier — the centroid of a triangle with vertices $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$ is simply their **average**:

$$\bar{x} = \frac{x_1+x_2+x_3}{3}, \qquad \bar{y} = \frac{y_1+y_2+y_3}{3}$$

which is the fastest legal route through most exam triangles, and the mark scheme accepts it as a complete method.

### 3. Composite bodies — build the table

This is the heart of the topic, and the format below is not a study aid invented for this card: it is how the published mark schemes lay the answer out. Cut the shape into pieces whose centres of mass you already know, then take moments about each axis.

$$\left(\sum A_i\right)\bar{x} = \sum A_i x_i, \qquad \left(\sum A_i\right)\bar{y} = \sum A_i y_i$$

| piece | area | $x$ of its CM | $y$ of its CM |
|---|---|---|---|
| piece 1 | $A_1$ | $x_1$ | $y_1$ |
| piece 2 | $A_2$ | $x_2$ | $y_2$ |
| **whole** | $A_1 + A_2$ | $\bar{x}$ | $\bar{y}$ |

Three habits make it reliable. Draw the axes on the diagram *before* filling anything in, so every entry is measured from the same corner. Fill the area column completely before starting the coordinates, since the total is the denominator of both answers. And check dimensions in every term — the mark schemes say "all terms must be dimensionally correct" in exactly those words, because a term of the wrong dimension is the commonest way this question dies.

### 4. Removal — subtract a piece by giving it negative area

A shape with a hole is a composite body in which one piece is **taken away**, and the table handles it with no new ideas: enter the removed piece with a **negative** area. The moments equation is a sum over signed pieces either way:

$$(A_{\text{whole}} - A_{\text{hole}})\,\bar{x} = A_{\text{whole}} x_{\text{whole}} - A_{\text{hole}} x_{\text{hole}}$$

This is worth internalising because **the decomposition is never unique** — the June 2025 mark scheme below prints *three* different correct routes to the same answer, one adding two pieces, one adding two different pieces, and one subtracting. Any of them scores full marks. Choose the cut whose pieces have centres of mass you can write down without thinking.

![[centre-of-mass-composite.svg|760]]

### 5. Integration — when there are no standard pieces

For a continuous body the sum becomes an integral, and this is where AP Physics C lives:

$$\mathbf{R} = \frac{1}{M}\int \mathbf{r}\; dm$$

The practical form for a lamina is to slice into strips of area $dA$ at position $x$, so $\bar{x} = \dfrac{\int x\, dA}{\int dA}$. Worked for a solid hemisphere of radius $r$ — slice into discs of radius $\sqrt{r^2-x^2}$ at distance $x$ from the flat face:

$$\bar{x} = \frac{\displaystyle\int_0^r x\,\pi(r^2-x^2)\,dx}{\displaystyle\int_0^r \pi(r^2-x^2)\,dx} = \frac{\pi\left[\tfrac{r^2x^2}{2}-\tfrac{x^4}{4}\right]_0^r}{\pi\left[r^2x-\tfrac{x^3}{3}\right]_0^r} = \frac{\pi r^4/4}{2\pi r^3/3} = \frac{3r}{8}$$

— the MF19 entry, earned. (Cambridge does not require this; AP Physics C and Edexcel IAL M3 require exactly this. [[Centres of Mass by Integration]] runs the same slicing through all six standard bodies — and finds two of them fall to arguments prettier than any integral.)

## Toppling or sliding — two questions, one diagram

Tilt a block on a rough plane and raise the angle slowly. Two different failures are waiting, and the examiner's favourite question is which one happens first.

**Sliding** is a force question. The block slides when the component of weight down the slope beats the maximum friction: $mg\sin\theta > \mu mg\cos\theta$, so the critical angle is

$$\tan\theta_{\text{slide}} = \mu$$

**Toppling** is a moments question — and it needs the centre of mass. A block of width $w$ and height $H$, uniform, has its centre of mass at the middle: $w/2$ from each vertical face, $H/2$ up. As the plane tilts, the vertical line through the centre of mass swings toward the lower edge of the base; the instant it passes *outside* that edge, gravity's moment about the edge tips the block over instead of holding it down. Geometry gives the boundary directly:

$$\tan\theta_{\text{topple}} = \frac{w/2}{H/2} = \frac{w}{H}$$

Whichever critical angle is **smaller** happens first, so the entire competition compresses to comparing two numbers:

$$\mu < \frac{w}{H} \Rightarrow \textbf{slides first}, \qquad \mu > \frac{w}{H} \Rightarrow \textbf{topples first}$$

![[centre-of-mass-topple-vs-slide.svg|720]]

Tall and narrow topples; short and wide slides; and roughening the surface (raising $\mu$) does not make an object safer — past $\mu = w/H$ it converts a harmless slide into a topple. This is the physics of why a wardrobe is anchored to the wall, why a wine glass tips on a tilting tray while a coin merely slides, and why the vehicle rollover story below is about geometry rather than tyres.

> [!tip] Suspension — one sentence, one mark
> Hang a body from a point and let it settle. The only two forces are the string's tension at the pivot and the weight at the centre of mass; for their moments about the pivot to cancel, they must be in line. Therefore **the centre of mass hangs directly below the point of suspension.** That single sentence answers every "find the angle the edge $AB$ makes with the vertical" question: locate the centre of mass, draw the line from the pivot to it, and the required angle is trigonometry between that line and the edge — usually $\tan\theta = \bar{x}/\bar{y}$ measured from the pivot. It is also how you find the centre of mass of an irregular object in a lab: hang it twice from different points, draw the vertical each time, and the intersection is the point.

## Worked examples — real Paper 3 questions, every tool and trigger named

### Example 1 — the trapezium, three legal routes (9231 June 2025 Paper 34 Q5a)

> $ABCD$ is a uniform square lamina of side $6a$. Points $E$ and $F$ lie on $DC$ and $AB$ with $DE = FB = h$. The quadrilateral $BCEF$ is removed. Show that the distance of the centre of mass of the remaining lamina $AFED$ from $AD$ is $\dfrac{h^2-6ah+36a^2}{18a}$, and find the corresponding distance from $AB$. [5]

*Trigger: a shape that is not standard, but is visibly two standard pieces → composite table.* Put the origin at $A$, with $AB$ along the $x$-axis and $AD$ along the $y$-axis. Then $A(0,0)$, $F(6a-h, 0)$, $E(h, 6a)$, $D(0,6a)$: distance from $AD$ is $\bar{x}$, distance from $AB$ is $\bar{y}$.

*Tool: total area first.* $AFED$ is a trapezium with parallel sides $6a-h$ and $h$, height $6a$, so its area is $\tfrac12\big((6a-h)+h\big)(6a) = 18a^2$ — **independent of $h$**, which is the question quietly telling you the denominator will not be messy.

*Tool: cut into rectangle + triangle.* Drop $G$ on $AF$ below $E$, giving rectangle $AGED$ and triangle $GFE$:

| piece | area | $x$ of CM | $y$ of CM |
|---|---|---|---|
| rectangle $AGED$ | $6ah$ | $\tfrac12 h$ | $3a$ |
| triangle $GFE$ | $18a^2-6ah$ | $\tfrac13 h + 2a$ | $2a$ |
| whole $AFED$ | $18a^2$ | $\bar{x}$ | $\bar{y}$ |

The triangle's entries are the *average of its vertices* $G(h,0)$, $F(6a-h,0)$, $E(h,6a)$ — no median-hunting needed. Taking moments about $AD$:

$$18a^2\bar{x} = 6ah\left(\tfrac{h}{2}\right) + (18a^2-6ah)\left(\tfrac{h}{3}+2a\right) = ah^2 - 6a^2h + 36a^3$$

$$\bar{x} = \frac{h^2-6ah+36a^2}{18a} \quad \blacksquare$$

and about $AB$: $18a^2\bar{y} = 6ah(3a) + (18a^2-6ah)(2a) = 6a^2h + 36a^3$, giving $\bar{y} = 2a + \tfrac13 h$.

**What makes this example worth its space** is the mark scheme, which prints two further routes and awards them identically: split instead into **triangles $AED$ and $AEF$**, or take the **whole rectangle $AFHD$ and subtract triangle $EFH$**. All three were checked symbolically for this card and agree exactly. The lesson generalises past this question: the marks are for a dimensionally correct moments equation with every piece present, not for finding the "intended" cut.

### Example 2 — the toppling chain (9231 November 2025 Paper 31 Q5)

> A uniform lamina $OABCD$ consists of rectangle $OACD$ and triangle $ABC$. $OA = ka$, $OD = 2a$, the height of triangle $ABC$ is $h$, and angle $CAB = 45°$. (a) Show that the $x$-coordinate of the centre of mass of triangle $ABC$ is $\tfrac13(3ka+h)$ and find $\bar{y}$. [3] (b) The lamina stands vertically on edge $OA$ on a horizontal plane. Find the values of $h$ for which it is in equilibrium. [4] (c) Given $k = \tfrac{\sqrt3}{3}$ and that the lamina is on the point of toppling, find the centre of mass of triangle $ABC$. [2]

**(a)** *Tool: vertices, averaged.* The $45°$ angle at $A$ with $AC$ vertical puts $B$ one height across and one height up: $A(ka,0)$, $B(ka+h,h)$, $C(ka,2a)$. Averaging,

$$\bar{x} = \tfrac13\big(ka+ka+h+ka\big) = \tfrac13(3ka+h)\ \blacksquare, \qquad \bar{y} = \tfrac13(0+h+2a) = \tfrac13(2a+h)$$

**(b)** *Trigger: "in equilibrium" while standing on an edge → this is a toppling condition, so find the whole lamina's $\bar{x}$ and keep it over the base.* The base is the segment $OA$, from $x=0$ to $x=ka$.

| piece | area | $x$ of CM |
|---|---|---|
| rectangle $OACD$ | $2ka^2$ | $\tfrac12 ka$ |
| triangle $ABC$ | $ah$ | $ka + \tfrac13 h$ |
| whole $OABCD$ | $2ka^2 + ah$ | $\bar{x}$ |

$$(2ka^2+ah)\,\bar{x} = 2ka^2\left(\tfrac{ka}{2}\right) + ah\left(ka+\tfrac{h}{3}\right)$$

The lamina stays up while $\bar{x} \le ka$ — the weight-line must not pass beyond the far edge of the base. Substituting and clearing the positive denominator:

$$k^2a^2 + kah + \tfrac{h^2}{3} \;\le\; ka(2ka+h) = 2k^2a^2 + kah \;\Longrightarrow\; \tfrac{h^2}{3} \le k^2a^2$$

$$\boxed{\,0 < h \le \sqrt{3}\,ka\,}$$

Notice how much cancels: the $kah$ terms vanish from both sides, and a question that looked like heavy algebra collapses to a one-line inequality. That is the usual reward for putting the origin at $O$.

**(c)** *Trigger: "on the point of toppling" is the equality case of (b).* With $k = \tfrac{\sqrt3}{3} = \tfrac{1}{\sqrt3}$: $h = \sqrt3 ka = \sqrt3 \cdot \tfrac{1}{\sqrt3} a = a$. Then

$$\bar{x} = \tfrac13(3ka+h) = \tfrac13\left(\sqrt3 a + a\right) = \tfrac13 a\left(\sqrt3+1\right), \qquad \bar{y} = \tfrac13(2a+a) = a$$

and the mark scheme's own comment is the elegant part: $h = a$ makes triangle $ABC$ **isosceles** (with $B$ level with the midpoint of $AC$), so $\bar{y} = a$ is available **by symmetry** without any arithmetic at all. Tool 1 beats tool 3 whenever it applies.

### Example 3 — will it slide or will it tip?

> A uniform cupboard is $0.6$ m wide and $2.0$ m tall, standing on a plank that is slowly tilted. The coefficient of friction between cupboard and plank is $\mu = 0.5$. Which happens first, and at what angle?

*Tool: compute both critical angles and compare.* Sliding needs $\tan\theta = \mu = 0.5$, so $\theta_{\text{slide}} = 26.6°$. Toppling needs $\tan\theta = w/H = 0.6/2.0 = 0.3$, so $\theta_{\text{topple}} = 16.7°$.

$\theta_{\text{topple}} < \theta_{\text{slide}}$ — **it topples first, at about $16.7°$**, and the friction never gets a chance to be exceeded. The comparison $\mu = 0.5$ against $w/H = 0.3$ gives the same answer in one line, which is the version to carry into an exam. Change the object to a $0.6$ m tall crate of the same width and $w/H = 1.0 > \mu$: now it slides at $26.6°$ and never tips. Same surface, same material, opposite failure — decided entirely by shape.

## Where this is the working tool

**The high jump is the showpiece.** In the Fosbury flop the athlete goes over the bar face-up, arching backwards so that head, then torso, then legs cross in sequence — and while every part of the body clears the bar, the centre of mass of the arched body sits *outside* the arch, and can pass **beneath** the bar. Since the height a jumper can raise their centre of mass is set by the energy they can generate on takeoff, a technique that clears the bar while lifting the centre of mass *less* is worth free centimetres. Dick Fosbury won the 1968 Olympics with it; within a decade essentially everyone jumped that way. The rule that the centre of mass need not lie inside the body is not a curiosity — it is an Olympic medal.

**Vehicle rollover is $w/H$ wearing tyres.** Engineers quote a *static stability factor* — half the track width divided by the centre-of-mass height — and it is exactly this card's toppling ratio. A sports car sits low and wide; an SUV or a loaded van sits tall and narrow, and rolls at a lower lateral acceleration. This is also why roof loads are dangerous out of proportion to their weight (they raise $H$), why a car's battery pack in the floor improves rollover resistance, and where [[Braking Systems]] gets the weight-transfer geometry that decides how much braking force each axle can use.

**Ships.** Naval architects track the centre of mass against the *metacentre*; when the centre of mass rises above it — cargo shifting, water on deck, too many passengers on one rail — the restoring moment reverses sign and the vessel capsizes. Ballast is mass carried purely to keep the centre of mass low.

**Aircraft weight and balance** is a legal requirement before every flight: the loaded centre of mass must fall inside a published envelope, because an aircraft loaded too far aft becomes uncontrollable in pitch. Loading crews compute a moments table — the same table as §3, in units of kilogram-metres.

**And the astronomical case.** The Earth does not orbit the Moon or vice versa: both orbit their common centre of mass, the *barycentre*, which is about 4 700 km from Earth's centre — beneath the surface, but not at the middle, so Earth genuinely wobbles monthly. For star–planet pairs the same wobble is measurable across light-years, and it is one of the two main methods by which exoplanets are found: the star's centre-of-mass motion betrays a companion nobody can see. [[Gravitational Fields]] treats the two-body problem; this is the point it turns around.

## Common Misconceptions (Teaching Notes)

### 1. "The centre of mass has to be inside the object"

It does not. A doughnut's is in the hole, a boomerang's is in the air beside it, a horseshoe's is off the metal entirely, and a high jumper's can be below the bar the jumper is clearing. Nothing in the definition requires $\mathbf{R}$ to land on any actual mass — it is an average of positions, and averages can fall in gaps. The consequence for exams: an L-shaped lamina's centre of mass may sit outside the L, and that is not a sign you made an arithmetic error.

### 2. "The centre of mass is the geometric centre"

Only for a **uniform** body. Cambridge writes "uniform" into the question precisely to license that step, and when the word is absent you must not assume it: a hammer's centre of mass is close to the head, a wine bottle's shifts as it empties, and a pencil with a heavy eraser balances well off-middle. Read for the word.

### 3. "Toppling and sliding are the same question"

They are different physics with different equations: sliding is $\sum F$ with friction at its limit, toppling is $\sum \tau$ about the base edge with the weight-line escaping the base. One is about $\mu$; the other is about shape ($w/H$) and does not involve $\mu$ at all. A question asking "which occurs first" is asking you to compute both critical angles — and answering with only one of them is the standard way to lose most of the marks.

### 4. "You need gravity to have a centre of mass"

The centre of *mass* is defined by mass and position alone — a body in deep space, weightless, still has one, and the theorem $M\ddot{\mathbf{R}} = \mathbf{F}_{\text{ext}}$ is what makes spacecraft attitude control possible. The centre of *gravity* is the gravitational twin, and it needs a field to exist. In a uniform field they coincide, which is why the words get used interchangeably at A-Level; in a strongly varying field they separate, and the object that is *technically* orbiting is the centre of mass.

### 5. "Adding a heavy base is the same as widening the base"

Both improve stability, but through different terms. Widening raises $w$; adding mass low down lowers $H$ (the height of the *combined* centre of mass, computed with the table in §3). The toppling ratio $w/H$ is what actually decides, and the second route is why a Weeble self-rights and why a good desk lamp has an absurdly heavy foot. Note also that neither route changes $\mu$, so an object made very stable against toppling has been made *more* likely to slide instead — the two failures trade against each other.

## Beyond the syllabus

> [!info] Pappus's centroid theorems — the centroid doing a job elsewhere
> Recall that [[Arc Length and Surfaces of Revolution]] computes what you get by rotating a curve or region about an axis. Pappus of Alexandria found, in the fourth century, that the answer is available from the centroid alone: rotating a plane region of area $A$ whose centroid is at distance $\bar{R}$ from the axis sweeps a solid of volume $V = 2\pi \bar{R} A$, and rotating a curve of length $L$ sweeps a surface of area $S = 2\pi\bar{R}L$. *The centroid travels a circle, and the shape is simply dragged along it.* The volume of a torus falls out in one line: a disc of radius $r$ with its centre $R$ from the axis gives $V = 2\pi R \cdot \pi r^2 = 2\pi^2 R r^2$. Read backwards, the theorems compute centroids from known volumes — which is one of the tidiest ways to derive the semicircle's $4r/3\pi$.

> [!info] The centre-of-mass frame
> Because $M\dot{\mathbf{R}}$ is the total momentum, an observer riding along with the centre of mass sees **zero total momentum** — always. Collisions analysed in that frame become symmetric and much easier: two objects approach, and whatever happens, their momenta stay equal and opposite. Particle physicists live in this frame; the "centre-of-mass energy" quoted for a collider ($13.6$ TeV at the LHC) is the energy available in it, and it is the number that decides which particles can be created. It is also the cleanest way to see why a perfectly inelastic collision cannot destroy *all* kinetic energy unless the total momentum is zero — [[Linear Momentum]]'s energy audit, viewed from the right seat.

> [!info] When the two centres really do separate
> A satellite in orbit is stretched by gravity: the near side is pulled harder than the far side, so the centre of gravity sits very slightly *below* the centre of mass. The mismatch produces a genuine torque — the **gravity-gradient** — that tends to align a long satellite with its long axis pointing at the planet, and engineers use it as free, fuel-less attitude stabilisation. The same effect over geological time is why the Moon keeps one face toward Earth. At laboratory scale the separation is unmeasurable; at orbital scale it flies spacecraft.

## Exam Notes

### Cambridge 9231 (Further Mechanics, Paper 3) — §3.2

The row's own words, and where each lands on this card: calculate the **moment of a force about a point** (coplanar only — the vector nature of moments is explicitly not required, so [[Torque]]'s scalar treatment is the right depth); use the result that gravity is **equivalent to a single force at the centre of mass**, and identify that point **by symmetry**; use **given** information about the triangular lamina and other simple shapes; determine the centre of mass of a **composite body by an equivalent system of particles** (the syllabus's own examples are a uniform L-shaped lamina, and a uniform cone joined at its base to a hemisphere of the same radius — so expect solids as well as laminae); the **equilibrium condition and its converse** ($\sum \mathbf{F} = 0$ and $\sum\tau = 0$ about any point); and problems on a single rigid body **including toppling or sliding**.

Question shape, from the recent papers used above: a "show that" for one piece's centre of mass (3 marks), then the composite table for the whole shape, then an inequality or a critical value from a toppling condition. The mark schemes award the moments equation itself — "all terms present, all terms dimensionally correct" — so **write the equation before simplifying anything**, and set out the pieces as a table; the published schemes do.

> [!tip] Formula-sheet status — unusually generous
> MF19 prints **all six** standard centres of mass (triangular lamina, solid hemisphere, hemispherical shell, circular arc, circular sector, solid cone/pyramid), and the syllabus adds that their proofs are not required. Nothing about composite bodies, toppling or sliding is given. So the memorisation budget for this topic is nearly zero and the practice budget is everything: you are being examined on *assembling* known pieces, not on recalling them. Full audit: [[MF19 Reference (9709)]].

### Edexcel IAL — M2

M2.2 covers centres of mass of discrete particle systems, uniform laminae, and the equilibrium of plane laminae (including suspension), with M2.5's rigid-body equilibrium and ladder problems already carried by [[Forces and Equilibrium]] and [[Torque]]. The composite-lamina and suspension work on this card is what M2.2 asks for; the standard results are supplied in the Edexcel formula book on the same terms.

### OxfordAQA 9660 — M2.3 (Statics and forces)

The specification names three tasks, all on this card: finding centres of mass **by symmetry**, of a **system of particles** (its stated form $X\sum m_i = \sum m_i x_i$ is §"The definition" verbatim), and of a **composite body** — plus "the position of a body when suspended from a given point and in equilibrium", which is the suspension callout above. Note the boundary: 9660 states **integration methods are not required**, so §5 is enrichment for this board.

### AP Physics 1 — Unit 2.1 · AP Physics C: Mechanics — Unit 2.1

Both courses open their dynamics unit with *Systems and Center of Mass*, and both want the systems idea first: define the system, distinguish internal from external forces, and know that $\mathbf{F}_{\text{ext}} = M\mathbf{a}_{\text{cm}}$ — the theorem in §"Why the point earns its name", which is the load-bearing content for AP Physics 1. AP Physics C adds the calculus: $\mathbf{r}_{\text{cm}} = \frac{1}{M}\int \mathbf{r}\,dm$ for continuous distributions, which is §5, and expects you to set up the integral for rods of varying density as well as symmetric solids. Typical AP items are the exploding-projectile question (the centre of mass continues undisturbed) and the two-blocks-on-a-frictionless-surface question — both direct applications of the theorem rather than the laminae arithmetic Cambridge favours.

### Where it is *not* examined

- **Cambridge 9709** — Mechanics Paper 4 has no centre-of-mass content; its moments work stops at rigid bodies whose centre of gravity is given or obvious. A 9709-only student meets this topic only if they also take 9231.
- **Cambridge 9702 / 0625 (Physics)** — both examine *centre of gravity* qualitatively and the stability/toppling idea in words (9702 §4.2, 0625 §1.5, closed by [[Forces and Equilibrium]]), but neither asks you to **calculate** the position for a composite body. The calculation is a mathematics-syllabus skill on the physics side of the fence.
- **IB Physics** — A.4 rigid-body mechanics (HL) works with torque and rotational equilibrium about a given centre of mass; locating it by composite decomposition is not assessed.

## Connections

- **Builds on:** [[Torque]] — the moments machinery this card reuses with mass in place of force, and the source of the $\sum m_i x_i$ form; [[Forces and Equilibrium]] — the two equilibrium conditions and the qualitative weight-line-inside-the-base test that §"Toppling or sliding" turns quantitative; [[Newton's Laws of Motion]] — N3 is what kills the internal forces in the theorem; [[Integration]] — the continuous case.
- **Builds on (momentum side):** [[Linear Momentum]] — total momentum is $M\dot{\mathbf{R}}$, so the centre of mass is the point whose motion *is* the system's momentum; that card reserved this one.
- **Pays off in:** [[Projectile Motion]] — the parabola belongs to the centre of mass, which is why a tumbling object still obeys it; [[SUVAT]] and every other card that ever said "model the object as a particle"; [[Linear Momentum]] — total momentum is $M\dot{\mathbf{R}}$, and the centre-of-mass frame is where collisions simplify.
- **Leads to:** [[Moment of Inertia]] — rotation is measured *about* the centre of mass, and the parallel-axis theorem is stated relative to it; [[Angular Momentum]] — the clean split of motion into centre-of-mass translation plus rotation about it.
- **Kindred:** [[Gravitational Fields]] — the two-body barycentre and why a point mass was a legitimate model in the first place; [[Braking Systems]] — weight transfer and rollover, both governed by centre-of-mass height; [[Arc Length and Surfaces of Revolution]] — Pappus's theorems, where the centroid computes volumes.
- **For 9231 students:** [[MF19 Reference (9709)]] — which of this card's results are printed on the exam sheet (all six standard bodies) versus which must be assembled.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $\mathbf{R} = \frac{1}{M}\sum m_i \mathbf{r}_i$ | `\mathbf{R} = \frac{1}{M}\sum m_i \mathbf{r}_i` | the definition, vector form |
| $M\bar{x} = \sum m_i x_i$ | `M\bar{x} = \sum m_i x_i` | the moments form used in exams |
| $\bar{x}$, $\bar{y}$ | `\bar{x}`, `\bar{y}` | coordinates of the centre of mass |
| $M\frac{d^2\mathbf{R}}{dt^2} = \mathbf{F}_{\text{ext}}$ | `M\frac{d^2\mathbf{R}}{dt^2} = \mathbf{F}_{\text{ext}}` | the theorem that licenses the particle model |
| $\int \mathbf{r}\,dm$ | `\int \mathbf{r}\,dm` | continuous distributions (AP Physics C) |
| $\tan\theta = \mu$ | `\tan\theta = \mu` | critical angle for sliding |
| $\tan\theta = w/H$ | `\tan\theta = w/H` | critical angle for toppling |
| $V = 2\pi\bar{R}A$ | `V = 2\pi\bar{R}A` | Pappus's second theorem |

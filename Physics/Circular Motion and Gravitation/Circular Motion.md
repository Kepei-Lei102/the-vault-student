---
chinese: 圆周运动 (yuánzhōu yùndòng)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Vectors in Physics]]"
  - "[[Radians]]"
  - "[[Forces and Equilibrium]]"
  - "[[Work, Energy and Power]]"
  - "[[Hooke's Law for Springs]]"
  - "[[Differentiation]]"
  - "[[Projectile Motion]]"
leads_to:
  - "[[Gravitational Fields]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Lorentz Force]]"
  - "[[Angular Momentum]]"
  - "[[The Friction Limit]]"
  - "[[Braking Systems]]"
  - "[[Elastic Strings and Springs]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/OxAQA-9660
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-12-1
  - syllabus/9702-12-2
  - syllabus/0625-1-5
  - syllabus/9231-3-3
  - syllabus/IB-Physics-A-2-4
  - syllabus/AP-Physics-1-2-9
  - syllabus/AP-Physics-C-Mech-2-10
  - type/deep
  - type/definition
  - type/theorem
  - notation/omega
  - notation/centripetal
  - misconception/centrifugal-force
  - misconception/centripetal-as-extra-force
  - misconception/release-flies-outward
  - misconception/complete-circle-v-top-zero
  - misconception/rpm-in-formulas
---

# Circular Motion 圆周运动

> *A hammer thrower spins four times and leans back hard against the wire — about three thousand newtons of pull, the weight of four people, all of it **inward**. The hammer never comes an inch closer. Then the hands open, and the hammer does not fly outward: it flies dead **straight**, along the tangent, exactly the way it was already going. Every idea on this page is in that throw: going round needs a steady inward pull, the pull never speeds the thing up, and the moment the pull stops the circle stops with it.*

## Definition

### Formal

A particle moving on a circle of radius $r$ has **angular displacement** $\theta$ (in radians) and **angular speed**

$$\omega = \frac{\Delta\theta}{\Delta t} = \frac{2\pi}{T} = 2\pi f \quad (\text{rad s}^{-1}), \qquad v = r\omega .$$

In **uniform** circular motion the speed is constant but the velocity is not — its direction turns at rate $\omega$ — so there is an acceleration, directed **toward the centre**, the **centripetal acceleration**

$$a = \frac{v^2}{r} = r\omega^2 = v\omega .$$

By Newton's second law a resultant force of that size, toward the centre, must exist: $F = \dfrac{mv^2}{r} = mr\omega^2$, the **centripetal force**. It is not a new kind of force — it is the *job description* for whichever real force (tension, friction, a normal reaction, gravity) happens to be doing it. If the speed also changes, the radial part is still $v^2/r$ and a second, **tangential** component $a_t = \dfrac{dv}{dt}$ handles the speeding up or slowing down.

### Intuitive

Velocity is an arrow with a length (the speed) and a direction. Acceleration is *any* change in that arrow. You can stretch it — that is speeding up — or you can **turn it without stretching it**, and that is still acceleration, at right angles to the arrow. A force along the motion changes speed; a force *across* the motion changes direction. Going round a circle at constant speed is the pure case: the force is always sideways, always toward the centre, and all it ever does is turn the velocity.

### 中文锚点 (Chinese Anchor)

匀速圆周运动里，速度的**大小**不变但**方向**一直在变，所以一直有加速度，而且永远指向圆心——这就是**向心加速度**，大小 $a = v^2/r = r\omega^2$，其中 $\omega = \Delta\theta/\Delta t = 2\pi/T$ 是角速度，$v = r\omega$。**向心力不是一种新的力，而是一个"岗位"**：绳子的拉力、地面的摩擦力、斜坡的支持力、地球的引力，谁指向圆心谁就在干这份活；画受力图时**只画真实的力**，然后朝圆心列方程 $F_{\text{向}} = mv^2/r$，垂直「指向圆心」方向的合力为零（水平圆周里就是竖直方向）。竖直圆周运动速度会变，要再加上能量守恒；**绳子松弛的判据是 $T = 0$，不是 $v = 0$**——要让绳子拉着物体走完整圆周，最低点速度必须满足 $u^2 \geq 5gr$（换成杆或管子只要 $u^2 \geq 4gr$）。两个经典误区：没有"离心力"把你往外甩，是你的惯性想走直线，车门把你往里推；绳子一断，物体**沿切线飞出**，不是沿半径甩出。考试里 9231/9709 取 $g = 10$，9702 取 $g = 9.81$。

---

## Describing the motion — radians, $\omega$, and $v = r\omega$

*Tool: arc length $s = r\theta$ ([[Radians]]).* Divide by the time: $\dfrac{s}{t} = r\,\dfrac{\theta}{t}$, so $v = r\omega$. The same $\omega$ serves every point of a rigid spinning object — a record, a wheel, the Earth — while $v$ grows with $r$: sit at the edge of the merry-go-round for the speed, at the middle for the calm.

One revolution is $2\pi$ radians, so the **period** $T$ and **frequency** $f$ give $\omega = 2\pi/T = 2\pi f$. Conversions that exam questions hide inside "revolutions per minute":

| Given | Convert with | Example |
|---|---|---|
| $n$ rev min⁻¹ | $\omega = \dfrac{2\pi n}{60}$ | 10 000 rpm $\to$ $1047$ rad s⁻¹ |
| period $T$ | $\omega = 2\pi/T$ | Earth's spin, $T = 86\,164$ s $\to$ $7.29\times10^{-5}$ rad s⁻¹ |
| speed and radius | $\omega = v/r$ | a car at $20$ m s⁻¹ round $r = 50$ m $\to$ $0.4$ rad s⁻¹ |

Earth's equator moves at $v = r\omega = 6.37\times10^6 \times 7.29\times10^{-5} \approx 465$ m s⁻¹ — faster than sound — with a centripetal acceleration of only $r\omega^2 \approx 0.034$ m s⁻², a third of a percent of $g$. The numbers say why you never notice: the turn is enormous in size and gentle in rate.

> [!warning] $\omega$ must be in rad s⁻¹ before it goes near $v = r\omega$ or $a = r\omega^2$
> Degrees per second and revolutions per minute are honest units for *describing* a spin; they are poison inside the formulas, which all come from $s = r\theta$ with $\theta$ in radians. Convert first, every time.

---

## Why the acceleration is $v^2/r$ — and why it points at the centre

Watch it first — the velocity arrow turning, and the same arrow redrawn from one fixed point so that its *tip* traces a circle; then three launches round a vertical circle with the tension read live:

![[circular-motion-see-it-run.mp4]]

**The velocity triangle (the picture that proves it).** Take the velocity at two instants $\Delta t$ apart. Both arrows have length $v$; their directions differ by the angle the radius has turned, $\Delta\theta = \omega\,\Delta t$. Draw them from a common start: the change $\Delta\vec v = \vec v_2 - \vec v_1$ is the third side of an isosceles triangle with apex angle $\Delta\theta$, so

$$|\Delta\vec v| = 2v\sin\tfrac{\Delta\theta}{2} \approx v\,\Delta\theta \qquad (\Delta\theta \text{ small}),$$

and the acceleration is

$$a = \frac{|\Delta\vec v|}{\Delta t} = v\,\frac{\Delta\theta}{\Delta t} = v\omega = \frac{v^2}{r} = r\omega^2 .$$

*Direction:* as $\Delta\theta \to 0$ the base of an isosceles triangle becomes perpendicular to its equal sides — $\Delta\vec v$ is perpendicular to $\vec v$, i.e. along the radius, and on the **inside** of the turn. That is the whole content of "centripetal": *centre-seeking*.

![[circular-motion-velocity-triangle.svg|900]]

**The calculus version (the same fact in one line).** Put the centre at the origin and let $\vec r(t)$ be the **position vector** of the particle — the arrow from the centre to wherever it is now. Its length is the radius $r$ and it turns at rate $\omega$, so in components $\vec r(t) = r(\cos\omega t,\ \sin\omega t)$. Differentiate twice:

$$\vec v = r\omega(-\sin\omega t,\ \cos\omega t), \qquad \vec a = -r\omega^2(\cos\omega t,\ \sin\omega t) = -\omega^2\,\vec r .$$

The acceleration is the position vector scaled by $-\omega^2$: it points from the particle straight back to the centre, with magnitude $r\omega^2$. (Units check: $(\text{m s}^{-1})^2/\text{m} = \text{m s}^{-2}$.) Dot $\vec v$ with $\vec r$ and you get $0$ — velocity perpendicular to radius, tangent to the circle — which is the other half of the picture.

**Why the speed never changes.** The centripetal force is perpendicular to the velocity, so its power $P = \vec F\cdot\vec v = 0$ ([[Work, Energy and Power]]): it does no work, transfers no energy, and cannot alter the kinetic energy. It turns; it never pushes along. (When the speed *does* change — a vertical circle, a car braking on a bend — some *other* component, along the tangent, is responsible.)

---

## Centripetal force is a role, not a new force

![[circular-motion-force-cast.svg|820]]

The method, which is the same for every circular-motion problem on every board:

1. **Draw the real forces only** — weight, tension, normal reaction, friction, lift, the magnetic force. Never draw an arrow labelled "centripetal force": it is already on the diagram, hiding inside the real ones. And never draw a "centrifugal force" outward — there is no such force in the frame of the ground (see the callout).
2. **Choose axes: toward the centre, and perpendicular to that.** For a horizontal circle the perpendicular axis is vertical; for a vertical circle it is the tangent.
3. **Toward the centre, the resultant is $\dfrac{mv^2}{r}$ ($= mr\omega^2$); perpendicular to it, the resultant is whatever the motion needs** — zero for a horizontal circle at constant speed, $m\,\dfrac{dv}{dt}$ along the tangent when the speed changes.

| Situation | Who does the centripetal job | Equations (toward centre ; perpendicular) |
|---|---|---|
| stone on a string, horizontal circle | tension | $T = mv^2/r$ ; — |
| conical pendulum | the horizontal component of tension | $T\sin\theta = mr\omega^2$ ; $T\cos\theta = mg$ |
| car on a flat bend | friction ([[The Friction Limit]]) | $F = mv^2/r \leq \mu mg$ ; $N = mg$ |
| car on a banked bend, no friction | the horizontal component of the normal reaction | $N\sin\theta = mv^2/r$ ; $N\cos\theta = mg$ |
| satellite, the Moon | gravity ([[Gravitational Fields]]) | $GMm/r^2 = mv^2/r$ ; — |
| charged particle in a magnetic field | the magnetic force ([[Lorentz Force]]) | $Bqv = mv^2/r$ ; — |
| top of a loop-the-loop | normal reaction **and** weight, both inward | $N + mg = mv^2/r$ |
| bottom of a vertical circle | tension minus weight | $T - mg = mv^2/r$ |

> [!info] Beyond syllabus — where "centrifugal" force actually lives
> In the frame of the ground there is only the inward force, and your body in the cornering car is simply trying to continue in a straight line while the door pushes it round. If instead you insist on doing physics *in the rotating frame* — the frame of the car, the centrifuge tube, the turning Earth — Newton's laws only work after you add fictitious forces, one of which is an outward "centrifugal" force $mr\omega^2$ (the other is the Coriolis force that steers cyclones). It is a bookkeeping device of that frame, not an agent. Exam boards want the ground frame: draw the inward forces, and keep the word *centrifugal* out of the answer.

---

## Horizontal circles — worked, every tool named

> [!tip] Nothing below is a formula to collect
> Every case on this page — conical pendulum, bowl, banked bend, rotating disc, loop, string, sphere inside or out — is the **same three-step method run on a different diagram**: draw the real forces, point one axis at the centre, write $\sum F = mv^2/r$ along it and the right thing (zero, or energy) along the other. That is why every board loves the topic: it is calculus and Newton's laws with nothing to hide behind. Work the cases to practise *starting from the picture*; the results ($v^2 = rg\tan\theta$, $u^2 \geq 5gr$, $\cos\phi = \tfrac23$ …) are things you re-derive in three lines when they come up, not things you carry.

### Conical pendulum: only the height of the cone matters

A bob of mass $m$ on a string of length $L$ swings in a horizontal circle, the string at angle $\theta$ to the vertical. Radius $r = L\sin\theta$.

*Tool: resolve — vertically nothing happens, horizontally the centre calls.*

$$T\cos\theta = mg, \qquad T\sin\theta = m(L\sin\theta)\,\omega^2 .$$

*Tool: divide, or better, cancel the $\sin\theta$ in the second equation first:* $T = mL\omega^2$, then the first gives $mL\omega^2\cos\theta = mg$, so

$$\omega^2 = \frac{g}{L\cos\theta} = \frac{g}{h}, \qquad \text{period } = 2\pi\sqrt{\frac{h}{g}} ,$$

where $h = L\cos\theta$ is the **height of the cone** — the vertical distance from the pivot to the plane of the circle. The period depends on nothing else: not the mass, not the string length on its own, not the angle on its own. Spin it faster and the bob rises ($h$ falls); it can never reach the horizontal, because $h = 0$ would need $\omega = \infty$. *(Numbers: $L = 1.0$ m, $\theta = 30°$: $h = 0.866$ m, period $1.87$ s, $\omega = 3.36$ rad s⁻¹.)*

### Real Paper 3 — the bowl (9231 Further Mechanics, June 2026/33 Q1)

*A particle $P$ of mass $m$ moves in a horizontal circle with constant angular speed $\omega$ on the smooth inner surface of a hemispherical shell of radius $a$. The plane of the circle is at height $h = \tfrac13 a$ above the lowest point of the shell. Find $\omega$ in terms of $a$ and $g$.*

![[circular-motion-q-bowl.svg|760]]

*Tool: the geometry first.* The normal reaction $R$ points along the radius of the shell, toward its centre $O$; let it make angle $\theta$ with the vertical. The circle's plane is $a - h = \tfrac23 a$ below $O$, so $\cos\theta = \tfrac23$, and the radius of the circle is $r = a\sin\theta$.

*Tool: resolve — vertical equilibrium, horizontal toward the centre.*

$$R\cos\theta = mg, \qquad R\sin\theta = m(a\sin\theta)\omega^2 \;\Rightarrow\; R = ma\omega^2 .$$

*Tool: substitute.* $ma\omega^2\cos\theta = mg \Rightarrow \omega^2 = \dfrac{g}{a\cos\theta} = \dfrac{3g}{2a}$, so

$$\boxed{\ \omega = \sqrt{\frac{3g}{2a}}\ }$$

— the conical pendulum in disguise: $a\cos\theta$ is the cone's height. The mark scheme wants the two resolutions shown separately (B1 each), the combination (M1), the answer (A1).

The sibling question (November 2025/31 Q2) gives the same bowl at two angles, $\tan\theta_1 = \tfrac34$ and $\tan\theta_2 = \tfrac43$, and asks for $\omega_1/\omega_2$. *Tool: the same two resolutions, written once more for each angle* — $R\cos\theta = mg$ and $R = ma\omega^2$ give $\omega^2 = g/(a\cos\theta)$ — so $\dfrac{\omega_1^2}{\omega_2^2} = \dfrac{\cos\theta_2}{\cos\theta_1} = \dfrac{3/5}{4/5} = \dfrac34$ and $\omega_1/\omega_2 = \dfrac{\sqrt3}{2}$. Three lines — not because a formula was remembered, but because the two-line derivation is quicker to redo than to look up.

### Banked bends: the design speed

A road or track banked at angle $\theta$ can hold a car round a bend of radius $r$ **with no friction at all** at one particular speed. *Tool: resolve — the normal reaction now tilts, and its horizontal component is the centripetal force.*

$$N\sin\theta = \frac{mv^2}{r}, \qquad N\cos\theta = mg \qquad\Longrightarrow\qquad v^2 = rg\tan\theta .$$

The mass cancels — the bend is designed for a *speed*, not a vehicle. ($r = 50$ m, $\theta = 20°$: $v = 13.4$ m s⁻¹, about 48 km h⁻¹.) Faster than that and friction must act *down* the slope to help; slower and it acts *up* the slope to stop the car sliding in. A flat bend has no help at all: friction supplies everything, $v_{\max} = \sqrt{\mu g r}$, which is the whole story of [[The Friction Limit]].

### Real Paper 3 — every force joins in (9231, June 2025/31)

*A rough horizontal disc rotates about its centre $O$ at constant angular speed $\omega$. A particle $P$ of mass $1.6$ kg lies on the disc $1.5$ m from $O$, attached to a point $A$ vertically above $O$ by a light elastic string of natural length $2$ m and modulus $32$ N, making angle $\alpha$ with the vertical. $P$ is on the point of slipping in the direction $OP$; the coefficient of friction is $0.5$. (a) Given the tension is $8$ N, show $\sin\alpha = 0.6$. (b) Find the number of revolutions per minute.* (Take $g = 10$.)

![[circular-motion-q-disc.svg|760]]

**(a)** *Tool: [[Elastic Strings and Springs]] — Hooke's law in the $\lambda x/l$ form.* $T = \dfrac{\lambda x}{l} = 8 \Rightarrow x = \dfrac{8\times 2}{32} = 0.5$ m, so the stretched length is $2.5$ m, and $\sin\alpha = \dfrac{1.5}{2.5} = 0.6$. $\blacksquare$ (So $\cos\alpha = 0.8$.)

**(b)** *Tool: read the friction's direction from "on the point of slipping in the direction $OP$"* — $P$ wants to slide *outward*, so limiting friction acts **inward**, toward $O$, and joins the tension's horizontal component in the centripetal job.

*Vertical:* $R + T\cos\alpha = mg \Rightarrow R = 16 - 8(0.8) = 9.6$ N, hence $F = \mu R = 4.8$ N.

*Toward the centre:* $T\sin\alpha + F = mr\omega^2 \Rightarrow 8(0.6) + 4.8 = 1.6\times1.5\times\omega^2 \Rightarrow \omega^2 = 4$, $\omega = 2$ rad s⁻¹.

*Tool: convert.* $\dfrac{2}{2\pi}\times 60 = \dfrac{60}{\pi} \approx \boxed{19.1\ \text{rev min}^{-1}}$ (the scheme accepts 19). Three forces, three ideas — Hooke, friction at its limit, the centripetal resolution — and the only new physics is the last line.

---

## Vertical circles — where the speed changes

Now gravity has a component along the tangent, so the speed rises and falls round the circle. Two tools, always the same two:

1. **Energy** between the launch point and the point of interest — the string (or a smooth surface) does no work, so $\tfrac12 mv^2 + mgh$ is constant ([[Work, Energy and Power]]).
2. **Newton's second law toward the centre** at the point of interest — with the weight's *radial component* included, and its sign read off the diagram.

### A particle on a string, launched from the bottom with speed $u$

Measure $\theta$ from the bottom. At angle $\theta$ the particle sits $r\cos\theta$ below the centre, so it has risen $h = r - r\cos\theta = r(1 - \cos\theta)$ above the bottom — the figure shows every length and force that the two tools use:

![[circular-motion-string-vertical.svg|760]]

*Tool: energy, bottom to $P$* — the string does no work, so

$$\tfrac12 mu^2 = \tfrac12 mv^2 + mg\,r(1-\cos\theta) \qquad\Longrightarrow\qquad v^2 = u^2 - 2gr(1 - \cos\theta).$$

*Tool: radially, toward the centre.* The tension pulls inward; the weight's component along the radius is $mg\cos\theta$ **outward** while the particle is below the centre's level ($\theta < 90°$) and inward above it — one formula covers both, $T - mg\cos\theta = \dfrac{mv^2}{r}$, with $\cos\theta$ carrying the sign:

$$T = \frac{mv^2}{r} + mg\cos\theta = \frac{mu^2}{r} - 2mg + 3mg\cos\theta .$$

Three facts fall straight out:

- **Bottom** ($\theta = 0$): $T_{\text{bot}} = \dfrac{mu^2}{r} + mg$. **Top** ($\theta = 180°$): $T_{\text{top}} = \dfrac{mu^2}{r} - 5mg$. Hence $T_{\text{bot}} - T_{\text{top}} = 6mg$ **for every launch speed** — an examiner's favourite "show that".
- **Complete circles need the string taut at the top:** $T_{\text{top}} \geq 0 \iff u^2 \geq 5gr \iff v_{\text{top}}^2 \geq gr$. At the critical case the string goes exactly slack at the top and gravity alone supplies $mv^2/r$: the particle is momentarily in free fall and still on its circle.
- **The string slackens where $T = 0$** — at $\cos\theta = \dfrac{2 - u^2/gr}{3}$ — never where $v = 0$. For $u^2 \leq 2gr$ that point is never reached: the particle rises at most to the level of the centre, $\cos\theta \geq 0$, both terms of $T$ stay positive, and it swings back like a pendulum. For $2gr < u^2 < 5gr$ it climbs above the centre, the tension runs out somewhere between $90°$ and $180°$, and the particle **leaves the circle as a projectile** ([[SUVAT]] takes over, with the tangential velocity at that instant as the launch velocity). For $u^2 \geq 5gr$ it goes all the way round.

![[circular-motion-vertical-tension.svg|760]]

> [!tip] Rod, bead on a wire, particle inside a smooth tube: only $v_{\text{top}} \geq 0$
> A string can only pull; a rod can push, a wire or tube can hold from either side. For those, the constraint force may go negative, so the only condition for a complete circle is that the particle reaches the top at all: $v_{\text{top}}^2 \geq 0 \iff u^2 \geq 4gr$. Read the question's apparatus before choosing the condition — it is the difference between $4gr$ and $5gr$, and examiners set both.

### Loop-the-loop, the bucket, and "weightless at the top"

Inside a loop (a roller coaster, a bucket of water swung overhead) the **normal reaction** plays the tension's part. At the top both $N$ and $mg$ point at the centre:

$$N + mg = \frac{mv^2}{r} \;\Rightarrow\; N = \frac{mv^2}{r} - mg, \qquad N = 0 \text{ at } v_{\min} = \sqrt{gr}.$$

Below that speed the track (or the bucket) cannot *pull*, so the car would leave the rails and the water would fall out. At $v = \sqrt{gr}$ the rider feels weightless — gravity is doing exactly the centripetal job, nothing else is pushing. At the bottom, $N - mg = mv^2/r$: the seat pushes *harder* than $mg$, which is the "g-force" that rollercoaster designers sell. (A bucket on a $0.8$ m arm needs $v_{\text{top}} \geq 2.8$ m s⁻¹ — a brisk but easy swing. Try it outdoors.)

### Outside a smooth sphere — the slide-off

A particle sits at the top of a smooth sphere of radius $a$ and is nudged off. At angle $\phi$ from the upward vertical:

*Tool: energy.* $v^2 = 2ga(1 - \cos\phi)$. *Tool: radially, toward the centre.* $mg\cos\phi - N = \dfrac{mv^2}{a}$.

It **leaves the surface when $N = 0$**: $g a\cos\phi = 2ga(1-\cos\phi) \Rightarrow \cos\phi = \tfrac23$ — at a height $\tfrac23 a$ above the centre, and $v = \sqrt{2ga/3}$ at that instant, regardless of mass. (Same geometry, same answer, for a skier cresting a dome or a marble on a bowling ball.)

**Real Paper 3 (9231, June 2026/33):** *projected from $A$ on the outer surface, where $OA$ makes angle $\alpha$ with the upward vertical, with speed $u$ perpendicular to $OA$ and downward; it loses contact at $B$ ($OB$ at angle $\beta$) with speed $v$. Given $u : v = 2 : 3$, find $\cos\alpha : \cos\beta$.*

![[circular-motion-q-sphere-outer.svg|760]]

*Tool: energy $A \to B$:* $v^2 = u^2 + 2ga(\cos\alpha - \cos\beta)$. *Tool: loses contact means $N = 0$ at $B$:* $mg\cos\beta = \dfrac{mv^2}{a} \Rightarrow v^2 = ga\cos\beta$. *Tool: the given ratio:* $u^2 = \tfrac49 v^2 = \tfrac49 ga\cos\beta$. Substitute:

$$ga\cos\beta = \tfrac49 ga\cos\beta + 2ga(\cos\alpha - \cos\beta) \;\Rightarrow\; 3\cos\beta - \tfrac49\cos\beta = 2\cos\alpha \;\Rightarrow\; \boxed{\ \cos\alpha : \cos\beta = 23 : 18\ }$$

The mark scheme's final line, exactly — three tools and an exact ratio, no numbers needed.

### Inside a smooth sphere — the sign that flips

**Real Paper 3 (9231, June 2025/31 Q7):** *a fixed hollow sphere of radius $a$, centre $O$; $A$ is on the inner surface with $OA$ horizontal, and the sphere has been cut off by a horizontal plane through $B$ and $C$ at height $ka$ above $O$ ($0<k<1$). A particle $P$ is projected vertically downward from $A$ with speed $u$ and moves in a vertical circle. (a) Given $u = \sqrt{\tfrac65 ga}$ and that the reaction at $B$ is half the reaction at $A$, find $k$. (b) Find $u$ if $P$ just reaches $B$.*

![[circular-motion-q-sphere-inner.svg|760]]

*Tool: radially at $A$ ($OA$ horizontal, so the weight has no radial component):* $R_A = \dfrac{mu^2}{a}$.

*Tool: radially at $B$, which is **above** the centre — gravity's radial component now points **into** the centre, so it helps $R$:* $R_B + mg\cos\theta = \dfrac{mv_B^2}{a}$ with $\cos\theta = k$, i.e. $R_B = \dfrac{mv_B^2}{a} - mgk$.

*Tool: energy $A \to B$* (rise $ka$): $v_B^2 = u^2 - 2gka$.

**(a)** $R_B = \tfrac12 R_A$: $\dfrac{m(u^2 - 2gka)}{a} - mgk = \dfrac{mu^2}{2a} \Rightarrow \dfrac{u^2}{2a} = 3gk \Rightarrow k = \dfrac{u^2}{6ga} = \dfrac{6/5}{6} = \boxed{\tfrac15}$.

**(b)** "*Just reaches $B$*" on the inside of a sphere above the centre does **not** mean $v_B = 0$ — it means the surface is about to stop pushing: $R_B = 0$, i.e. $v_B^2 = gak$, so $u^2 = 3gak = \tfrac35 ga$ and $u = \sqrt{\tfrac35 ga}$. Any slower and $R$ would hit zero *before* $B$ and the particle would fall away from the wall. (The question's part (c), passing $B$ and reaching $C$, is then a projectile from $B$ to $C$ launched along the tangent — the same [[SUVAT]] hand-off as the slack string.)

The single idea that decides this question is the **sign of $mg\cos\theta$ in the radial equation**: outward below the centre's level, inward above it. Draw the point, draw the weight, drop a perpendicular onto the radius, and read the sign off the picture — never off memory.

---

## Non-uniform circular motion — two components of acceleration

When the speed changes, the acceleration has two perpendicular parts:

$$a_r = \frac{v^2}{r}\ \text{(toward the centre — turning)}, \qquad a_t = \frac{dv}{dt}\ \text{(along the tangent — speeding or slowing)}, \qquad |a| = \sqrt{a_r^2 + a_t^2}.$$

In the vertical circle the tangential acceleration is the weight's tangential component, $a_t = g\sin\theta$, because the string contributes nothing along the tangent; at the bottom and top $a_t = 0$ and the acceleration is purely radial. A car *braking on a bend* needs friction for both components at once — the radial $mv^2/r$ and the tangential $m\,dv/dt$ — which is why braking in a corner is where grip runs out first ([[Braking Systems]]).

---

## Where this is the working tool

- **The laboratory centrifuge is $r\omega^2$ sold by the thousand.** A rotor of radius $10$ cm at $10\,000$ rev min⁻¹ has $\omega = 1047$ rad s⁻¹ and $a = r\omega^2 \approx 1.1\times10^5$ m s⁻² — about **11 000 $g$**. Blood separates, DNA pellets, uranium isotopes sort by mass — all because a tube wall supplies an inward push and anything denser than its neighbours cannot keep up with the turn. The machine's "RCF" dial is literally $r\omega^2/g$.
- **Every satellite is a stone on a gravitational string.** For the International Space Station (ISS), $v = 7.66$ km s⁻¹ at $r = 6.79\times10^6$ m gives $a = v^2/r = 8.6$ m s⁻² — nearly the full surface $g$. Astronauts are not weightless because gravity is weak up there; they are weightless because gravity is *exactly* the centripetal force and nothing else pushes on them. $GMm/r^2 = mv^2/r$ is the doorway to [[Gravitational Fields]] and every orbit on Earth or off it.
- **Banked roads and railway cant** are $v^2 = rg\tan\theta$ poured in concrete: the designer picks the bend's *speed*, and at that speed the rails feel no sideways push and the passengers' coffee stays level. Cycle velodromes bank at up to $45°$ for the same reason.
- **The hammer throw is the inward-pull fact made visible.** A 7.26 kg hammer released at about $29$ m s⁻¹ on a path of radius $\approx 1.8$ m needs $mv^2/r \approx 3.4$ kN of wire tension — the thrower leans back against a third of a tonne — and the instant the grip opens the hammer leaves along the tangent. Release a quarter-turn early and it goes into the cage.
- **Charged particles in magnetic fields** turn in circles because the magnetic force is always sideways: $Bqv = mv^2/r$ gives $r = mv/(Bq)$ — the mass spectrometer, the cyclotron and the aurora all live in that line ([[Lorentz Force]]).

---

## Common Misconceptions (Teaching Notes)

### 1. "Centrifugal force throws you outward"

There is no outward force on you in the ground frame. You feel pushed out because your body wants to go *straight* (Newton's first law) and the car door, the seat, the rope supply the inward push that stops it. The word *centrifugal* belongs to the rotating frame only (see the callout) — in an exam answer it costs the mark.

**Fix:** draw the forces on the *object in the circle* from the ground's point of view. If an arrow points outward, ask which real agent is pushing that way. None is.

### 2. An extra arrow labelled "centripetal force"

Adding $mv^2/r$ to the diagram as if it were a fifth force double-counts it. It is the *resultant* of the real forces toward the centre, not one of them.

**Fix:** real forces on the diagram, then the sentence "the resultant toward the centre is $mv^2/r$" as the *equation*, never as an arrow.

### 3. "The string speeds the stone up"

A force at right angles to the motion does no work ($P = Fv\cos 90° = 0$), so uniform circular motion has constant speed by construction. If the speed changes, look for a tangential force — gravity's tangential component in a vertical circle, friction when braking.

**Fix:** "perpendicular turns, parallel speeds" — say it before resolving.

### 4. The weight's radial component with the wrong sign, or forgotten

$T = mv^2/r$ on its own is right only in a horizontal circle. In a vertical circle the weight's radial component is $mg\cos\theta$ outward below the centre's level and inward above it; the J25/31 sphere question is decided entirely by that sign.

**Fix:** at the point of interest draw the radius and the weight, project one onto the other, and write the radial equation from the picture, every time.

### 5. "Complete circle means the particle reaches the top with $v = 0$"

For a string (or a car on the inside of a loop) the condition is **tension (or normal reaction) $\geq 0$ at the top**, which needs $v_{\text{top}}^2 \geq gr$, i.e. $u^2 \geq 5gr$ from the bottom. Only for a rod, a wire or a tube is $v_{\text{top}} \geq 0$ the test ($u^2 \geq 4gr$).

**Fix:** ask "can this constraint push as well as pull?" — string no, rod yes — then choose $5gr$ or $4gr$.

### 6. "Cut the string and it flies outward along the radius"

It flies along the *tangent*, at the velocity it had — the inward pull was the only thing bending its path, and removing it leaves a straight line. (The hammer thrower, the sling, a mud flake leaving a tyre — all tangential.)

**Fix:** the velocity arrow is tangent; removing all forces keeps the velocity arrow. Draw it.

### 7. Revolutions per minute fed straight into $a = r\omega^2$

$\omega$ in $a = r\omega^2$ and $v = r\omega$ must be in rad s⁻¹. A disc at 3000 rpm has $\omega = 314$ rad s⁻¹, not 3000.

**Fix:** convert on the first line of every answer — $\omega = 2\pi n/60$ — and carry units.

---

## Exam Notes

### Cambridge 9702 (A-Level Physics, Topic 12 — Motion in a circle)

- **§12.1:** define the radian and express angular displacement in radians; understand angular speed; **recall and use** $\omega = 2\pi/T$ and $v = r\omega$. **§12.2:** understand that a force of constant magnitude always perpendicular to the motion causes centripetal acceleration, that this produces circular motion at constant angular speed; **recall and use** $a = r\omega^2 = v^2/r$ and $F = mr\omega^2 = mv^2/r$.
- Typical marks: a 2–3 mark "explain why the object moves in a circle at constant speed" (force perpendicular to velocity → changes direction not speed → no work done), then a calculation chain $T \to \omega \to v \to a \to F$, often on a satellite, a conical pendulum, or a car on a bend. $g = 9.81$ m s⁻².
- **None of these formulas is on the 9702 data sheet** — the syllabus says *recall* for all four. The velocity-triangle derivation above is the safety net if memory fails.

### Cambridge 9231 (Further Mathematics, Paper 3 — Further Mechanics §3.3)

- Angular speed and $v = r\omega$; acceleration $r\omega^2 = v^2/r$ **toward the centre** (proof not required — but MF19 prints "the acceleration is directed towards the centre and has magnitude $\omega^2 r$ or $v^2/r$", so the formula is handed to you; $v = r\omega$ is not); horizontal circles at constant speed (conical pendulum, inner surface of a bowl, rotating rough discs with strings — friction and Hooke's law join in); **vertical circles without energy loss** — tension or contact force at a point, where it is zero, conditions for complete circles. $g = 10$ m s⁻².
- Recent real questions: the bowl in one part (4 marks, J26/33 Q1), the bowl at two angles as a ratio (N25/31 Q2), the rough disc with an elastic string (J25/31, 8 marks across two parts), the outer-surface slide-off as an exact ratio (J26/33), the cut hollow sphere with the reaction-sign trap and a projectile finish (J25/31 Q7), and a vertical circle that ends in a collision with restitution (N25/31 Q7 — the §3.6 cross-over).
- Mark-scheme habits: the two resolutions are separate B1s ("N2L horizontally and vertically"); the energy equation is an M1 that must be *dimensionally correct*; the combination is a DM1; answers "in terms of $a$ and $g$" must be exact — $\sqrt{3g/(2a)}$, not a decimal.

### Cambridge 0625 (IGCSE Physics, §1.5 Forces)

- **Qualitative only:** describe motion in a circular path due to a force perpendicular to the motion, and state that (a) speed increases if the force increases (mass and radius constant), (b) radius decreases if the force increases (mass and speed constant), (c) a larger mass needs a larger force to keep the same speed and radius. The syllabus says in so many words that $F = mv^2/r$ is **not required** — but the three statements are exactly what the formula says, and knowing it makes them unforgettable.

### AP Physics 1 (Unit 2 §2.9 Circular Motion)

- Centripetal acceleration as the component of acceleration toward the centre, magnitude $v^2/r$ (on the equation sheet as $a_c = v^2/r$); net force toward the centre from real forces — including *components* of friction and the normal force; **the top of a vertical loop** (minimum speed, $N = 0$); tangential acceleration $a_t$ as the rate of change of speed (§2.9.A.3); period and frequency, $v = 2\pi r/T$. FRQs want a free-body diagram with real forces only and an explicit "the net force toward the centre is $mv^2/r$" — no centripetal arrow.

### AP Physics C: Mechanics (Unit 2 §2.10)

- The same essential knowledge with calculus: derive $\vec a = -\omega^2\vec r$ from $\vec r(t)$, uniform and **non-uniform** circular motion (both components), and **banked curves** quantitatively (with and without friction). Vertical loops and conical pendulums are standard.

### IB Physics (A.2 Forces and momentum, A.2.4)

- $a = v^2/r = \omega^2 r = 4\pi^2 r/T^2$, centripetal force perpendicular to the velocity (changes direction, not speed), $\omega = 2\pi/T$, $v = 2\pi r/T = \omega r$ — all carried in the data booklet. Situations include **both uniform and non-uniform** motion in **horizontal and vertical** planes; but analysis of forces in non-uniform vertical motion is required **only at the top and bottom**, and **banked surfaces are qualitative only**. No additional HL content.

### Edexcel IAL (Further Mechanics 3, §4.1–4.4)

- Angular speed; radial acceleration in both forms $r\omega^2$ and $v^2/r$; horizontal circles — the conical pendulum, an elastic string, a **banked surface**, "and other contexts"; **vertical circles** including whether the circle is completed. Closest in flavour to the 9231 questions above.

### OxAQA 9660 (International A-Level Mathematics, M2.7)

- Horizontal circles at constant speed — including a satellite with gravity toward the centre; $v = r\omega$, $a = r\omega^2 = v^2/r$; **angular speed converted from rev min⁻¹ or a period**; position, velocity and acceleration as $\mathbf i$/$\mathbf j$ vectors (you may be asked to *show* the motion is circular by showing constant distance from a point — the $\vec r(t)$ derivation above does it); the conical pendulum. No vertical circles.

### Where it is *not* examined

Not on Cambridge 9709 (its mechanics papers stop at particles, projectiles and connected bodies — circular motion is Further only), not on OxAQA 9260, Cambridge 0580 or 0606 (radians as measure, yes; motion, no), and not in IB AA/AI (no mechanics). A 0625 student meets only the qualitative §1.5 statements above.

---

## Connections

- **Parent:** [[Newton's Laws of Motion]] — $F = ma$ with $a$ pointing at the centre is the whole of the dynamics; [[Vectors in Physics]] — velocity is a vector, and a turning vector is an accelerating one.
- **Measure:** [[Radians]] — $s = r\theta$ is where $v = r\omega$ and $a = r\omega^2$ come from, and why $\omega$ must be in rad s⁻¹.
- **Resolving and energy:** [[Forces and Equilibrium]] — the same resolve-along-two-axes habit, with one axis pointed at the centre; [[Work, Energy and Power]] — the centripetal force does no work, and energy conservation is half of every vertical-circle question. [[Hooke's Law for Springs]] supplies the tension when the string is elastic.
- **Leads to:** [[Gravitational Fields]] — gravity as the centripetal force, orbits and Kepler; [[Simple Harmonic Motion]] — the shadow of uniform circular motion on a diameter *is* SHM, the reference-circle picture; [[Lorentz Force]] — $r = mv/(Bq)$ is one line of this page; [[Angular Momentum]] — $L = mvr = mr^2\omega$ for a particle on a circle; [[The Friction Limit]] and [[Braking Systems]] — the flat bend and braking in corners.
- **Hand-offs:** [[SUVAT]] — what happens after the string goes slack or the particle leaves the sphere; [[Linear Momentum]] — vertical circles that end in collisions.
- **Kinship:** [[Polar Coordinates]] — circular motion is the $r$-constant special case of motion described by $(r, \theta)$.
- **For 9231 students:** [[MF19 Reference (9231)]] — the acceleration statement ($\omega^2 r$ or $v^2/r$, toward the centre) is printed; $v = r\omega$ and everything about vertical circles is yours to carry. For 9702 nothing in Topic 12 is on the data sheet.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\omega = \dfrac{2\pi}{T} = 2\pi f$ | `\omega = \frac{2\pi}{T} = 2\pi f` | angular speed, rad s⁻¹ |
| $v = r\omega$ | `v = r\omega` | from $s = r\theta$ |
| $a = \dfrac{v^2}{r} = r\omega^2$ | `a = \frac{v^2}{r} = r\omega^2` | centripetal acceleration, toward the centre |
| $F = \dfrac{mv^2}{r} = mr\omega^2$ | `F = \frac{mv^2}{r} = mr\omega^2` | the resultant toward the centre |
| $\vec a = -\omega^2\vec r$ | `\vec a = -\omega^2 \vec r` | the calculus derivation |
| $v^2 = rg\tan\theta$ | `v^2 = rg\tan\theta` | banked bend, no friction — two resolutions, re-derive |
| $T = \dfrac{mu^2}{r} - 2mg + 3mg\cos\theta$ | `T = \frac{mu^2}{r} - 2mg + 3mg\cos\theta` | string, $\theta$ from the bottom — energy + radial, re-derive |
| $u^2 \geq 5gr$ | `u^2 \geq 5gr` | complete circle on a string — from $T_{\text{top}} \geq 0$, re-derive |
| $\cos\phi = \tfrac23$ | `\cos\phi = \tfrac23` | slide-off from the top of a sphere — from $N = 0$, re-derive |

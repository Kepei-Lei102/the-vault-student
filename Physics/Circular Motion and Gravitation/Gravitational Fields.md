---
chinese: 引力场 (yǐnlì chǎng)
prerequisites:
  - "[[Circular Motion]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Work, Energy and Power]]"
  - "[[Vectors in Physics]]"
  - "[[Integration]]"
  - "[[Differentiation]]"
leads_to:
  - "[[Electric Field]]"
  - "[[Angular Momentum]]"
tags:
  - subject/physics
  - domain/mechanics
  - domain/fields
  - level/A-Level
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - curriculum/OxAQA-9660
  - curriculum/Edexcel-IAL
  - curriculum/Cambridge-9231
  - syllabus/9702-13-1
  - syllabus/9702-13-2
  - syllabus/9702-13-3
  - syllabus/9702-13-4
  - syllabus/0625-1-3
  - syllabus/0625-6-1
  - syllabus/IB-Physics-D-1-1
  - syllabus/IB-Physics-D-1-2
  - syllabus/IB-Physics-D-1-3
  - syllabus/IB-Physics-D-1-4
  - syllabus/AP-Physics-1-2-6
  - syllabus/AP-Physics-1-6-6
  - syllabus/AP-Physics-C-Mech-2-6
  - syllabus/9231-3-5
  - type/deep
  - type/definition
  - type/theorem
  - notation/G
  - notation/phi-potential
  - misconception/no-gravity-in-space
  - misconception/negative-potential
  - misconception/escape-depends-on-mass
  - misconception/geostationary-anywhere
  - misconception/altitude-not-radius
---

# Gravitational Fields 引力场

> *In 1666 a young man sent home from Cambridge by the plague asked an odd question: does the pull that drops an apple reach all the way to the Moon? If it does, and it weakens with distance as $1/r^2$, then the Moon — sixty Earth-radii away — should be falling toward us with one sixty-squared of an apple's acceleration: $9.8/3600 = 0.0027$ m s⁻². He worked out how fast the Moon actually falls from its orbit — $4\pi^2 r/T^2 = 0.0027$ m s⁻² — and the two numbers agreed. One piece of arithmetic tied a falling fruit to the sky, and the law that runs the Solar System has not needed changing since.*

## Definition

### Formal

A **gravitational field** is a region in which a mass experiences a force. Its **field strength** at a point is the force per unit mass on a small test mass placed there:

$$g = \frac{F}{m} \qquad (\text{N kg}^{-1} \equiv \text{m s}^{-2}),$$

a vector, pointing the way the force points. **Newton's law of gravitation**: any two point masses attract along the line joining them with

$$F = \frac{G m_1 m_2}{r^2}, \qquad G = 6.67\times10^{-11}\ \text{N m}^2\,\text{kg}^{-2},$$

and a uniform sphere attracts anything outside it as if all its mass sat at its centre. Hence the field of a point mass (or, outside it, a sphere) of mass $M$ is

$$g = \frac{GM}{r^2} \quad\text{toward the centre.}$$

The **gravitational potential** $\varphi$ at a point is the work done per unit mass in bringing a small test mass from infinity to that point; for a point mass,

$$\varphi = -\frac{GM}{r}, \qquad U = m\varphi = -\frac{GMm}{r}, \qquad g = -\frac{d\varphi}{dr}.$$

Zero at infinity, negative everywhere else: the field does the work on the way in, so the mass arrives owing energy.

### Intuitive

A field is a *map* of what a test mass would feel at every point before you put one there — arrows for the force per kilogram, contours for the energy per kilogram. Gravity's map around any planet is the same shape: arrows pointing in, crowding near the surface and thinning as the square of the distance; contours that are concentric spheres, deeper (more negative) toward the middle. Every satellite is a stone on a gravitational string ([[Circular Motion]]); every rocket is a climb out of a well whose depth at the surface is $GM/R$ joules per kilogram.

### 中文锚点 (Chinese Anchor)

**引力场**就是"放一个有质量的物体进去就会受力"的区域。**场强** $g = F/m$，单位 N/kg（也就是 m/s²），是个矢量，方向就是受力方向。**万有引力定律**：两个质点之间 $F = Gm_1m_2/r^2$，$G$ 小到不可思议（$6.67\times10^{-11}$），所以只有行星级别的质量才显出引力；均匀球体对外面的物体，相当于全部质量集中在球心。于是，在一个质量为 $M$ 的天体外面，$g = GM/r^2$，指向球心——地表的 9.81 就是这么算出来的。**引力势** $\varphi = -GM/r$：把单位质量从无穷远拉到这一点，引力替你做功，所以你"欠"能量，势是负的；势能 $U = -GMm/r$，**场强是势的负梯度**（$g = -d\varphi/dr$，势曲线越陡场越强）。**轨道**：引力充当向心力，$GMm/r^2 = mv^2/r$ 给出 $v = \sqrt{GM/r}$ 和开普勒第三定律 $T^2 \propto r^3$；**逃逸速度** $\sqrt{2GM/R}$（地球 11.2 km/s）来自"动能正好填平势能的坑"；**地球同步轨道**半径 42 200 km，必须在赤道上空、自西向东。几个常见误区：太空里不是没有重力（空间站处 $g$ 还有地表的 88%，宇航员"失重"是因为正在自由下落）；势是负的不是"欠了谁"，只是零点定在无穷远；逃逸速度跟火箭质量无关；公式里的 $r$ 永远从**球心**量，不是离地高度。

---

## Where the law comes from — Kepler, the cannon, and the Moon

Newton did not guess $1/r^2$; he squeezed it out of two things already known. [[Circular Motion]] says a body going round at radius $r$ in period $T$ accelerates toward the centre at $a = 4\pi^2 r/T^2$. Kepler's third law (below) says that for the planets $T^2 \propto r^3$. Put the second into the first:

$$a = \frac{4\pi^2 r}{T^2} \propto \frac{r}{r^3} = \frac{1}{r^2}.$$

The acceleration the Sun gives a planet falls off as the inverse square of its distance — so the force does too. Then the **Moon test** in the opener: Earth's surface gravity scaled down by $(R_E/r_{\text{Moon}})^2 = 1/60.3^2$ gives $0.0027$ m s⁻², and the Moon's actual centripetal acceleration, from its period and distance, is $0.0027$ m s⁻². Same law, apple to Moon.

Watch the idea that makes an orbit a *fall*: a cannon on a mountain, fired faster each time, with every path integrated from the inverse-square law —

![[gravitational-fields-newtons-cannon.mp4]]

Too slow and the ball lands; at exactly $\sqrt{GM/r}$ it falls all the way round and keeps missing the ground — a circular orbit; faster and it swings out into an ellipse; at $\sqrt2$ times the circular speed it never returns. The second act is Kepler's second law: the radius line sweeps equal areas in equal times, which is nothing but conservation of [[Angular Momentum]] for a force that always points at the centre.

**The constant $G$** was not measured until 1798, when Henry Cavendish hung two small lead balls on a torsion wire and watched two large ones twist it by a hair. The same experiment "weighed the Earth": with $g$, $R_E$ and $G$ known, $M_E = gR_E^2/G = 5.97\times10^{24}$ kg, and the planet's mean density came out at $5.5$ g cm⁻³ — twice that of surface rock, the first evidence of a dense iron core. $G$ is tiny: two people a metre apart attract each other with about $10^{-7}$ N, the weight of a speck of dust.

---

## Field strength — the map's arrows

*Tool: Newton's law and the definition $g = F/m$.* A test mass $m$ at distance $r$ from a point mass $M$ feels $F = GMm/r^2$, so

$$g = \frac{F}{m} = \frac{GM}{r^2}.$$

The test mass cancels — the field is a property of $M$ and the point, not of what you put there. (Units check: N m² kg⁻² × kg / m² = N kg⁻¹.) For Earth, $GM_E/R_E^2 = 6.67\times10^{-11}\times 5.97\times10^{24}/(6.37\times10^6)^2 = 9.82$ N kg⁻¹ — the familiar $g$, now *derived*.

![[gravitational-fields-lines.svg|760]]

**Field lines** show the direction of the force on a test mass and, by their spacing, its size: radial lines pointing in, crowding toward the centre. **Near the surface the field is uniform** — a small patch of a large sphere has parallel lines and constant $g$. How constant? *Tool: expand $g(R+h)$ for small $h$:*

$$g(R+h) = \frac{GM}{(R+h)^2} = \frac{GM}{R^2}\left(1+\frac{h}{R}\right)^{-2} \approx g_0\left(1 - \frac{2h}{R}\right),$$

so $g$ drops by $2h/R$ — $0.3\%$ per $10$ km, $3\%$ at $100$ km, $12\%$ at the **International Space Station** (the ISS, $400$ km up: $g = 8.6$ N kg⁻¹). That last number is the one to remember when someone says there is "no gravity in space".

**Weight is the gravitational force on a mass**, $W = mg$ — a force, in newtons, that changes from place to place ($9.81$ N kg⁻¹ at sea level, $9.78$ at the Equator, $1.62$ on the Moon), while the mass in kilograms does not. What a scale reads is the *normal reaction*, the **apparent weight**: equal to $mg$ when you stand still, more in a lift accelerating upward, less when it accelerates down, and zero in free fall — which is precisely the condition of an orbiting astronaut, whose weight is very much still there.

> [!info] Beyond syllabus — inside the Earth, and the 84-minute tunnel
> Newton's shell theorem says a uniform spherical shell pulls on anything *inside* it with **zero** net force. So at radius $r$ inside a uniform sphere only the mass within $r$ counts — $M(r) = M r^3/R^3$ — and $g = GM(r)/r^2 = GMr/R^3$: the field grows *linearly* from zero at the centre to $g_0$ at the surface. A force proportional to displacement toward the centre is [[Simple Harmonic Motion]]: a ball dropped down a frictionless tunnel through the Earth oscillates with period $2\pi\sqrt{R^3/GM}$ — **84 minutes**, the same as the lowest possible orbit, and independent of the tunnel's direction. (The real Earth is denser at the centre, so $g$ actually rises a little going down before it falls.)

---

## Orbits — gravity as the centripetal force

*Tool: gravity is the only force, so it is the whole of $mv^2/r$ ([[Circular Motion]]).* For a satellite of mass $m$ in a circular orbit of radius $r$ about a central mass $M$:

$$\frac{GMm}{r^2} = \frac{mv^2}{r} \quad\Longrightarrow\quad v = \sqrt{\frac{GM}{r}}, \qquad T = \frac{2\pi r}{v} = 2\pi\sqrt{\frac{r^3}{GM}} \quad\Longrightarrow\quad T^2 = \frac{4\pi^2}{GM}\,r^3.$$

Three things to notice, each an exam mark somewhere. The satellite's mass cancels: every object at a given radius orbits at the same speed — which is why an astronaut floats beside her station (both are in the *same* free fall), not because gravity is absent. Lower orbits are *faster* ($v \propto r^{-1/2}$): the ISS at $6790$ km from the centre does $7.66$ km s⁻¹ and a lap every $93$ minutes; the Moon at $384\,000$ km ambles at $1.0$ km s⁻¹ and takes $27.3$ days. And $T^2 \propto r^3$ — **Kepler's third law, derived**, with the constant $4\pi^2/GM$ depending only on the central mass: one constant for everything orbiting the Sun, a different one for everything orbiting the Earth.

| Planet | $a$ / AU | $T$ / yr | $T^2/a^3$ |
|---|---|---|---|
| Mercury | 0.387 | 0.241 | 1.000 |
| Venus | 0.723 | 0.615 | 1.001 |
| Earth | 1.000 | 1.000 | 1.000 |
| Mars | 1.524 | 1.881 | 1.000 |
| Jupiter | 5.203 | 11.86 | 0.999 |
| Saturn | 9.537 | 29.46 | 1.001 |
| Uranus | 19.19 | 84.01 | 0.999 |
| Neptune | 30.07 | 164.8 | 0.999 |

Real data, eight planets, one constant to three figures — the law Kepler found in Tycho's tables in 1619 and Newton explained in 1687.

**Weighing the Sun.** Turn the law round: $M = \dfrac{4\pi^2 a^3}{GT^2}$. With the Earth's $a = 1.496\times10^{11}$ m and $T = 3.156\times10^7$ s, $M_{\text{Sun}} = 1.99\times10^{30}$ kg. Every mass in astronomy is found this way — by timing something that orbits it: Jupiter from its moons, the Earth from *the* Moon, a black hole from the stars that whip round it.

**Kepler's three laws**, as a set: (I) orbits are ellipses with the Sun at one focus — circles are the special case the syllabuses compute with; (II) the line from Sun to planet sweeps equal areas in equal times; (III) $T^2 \propto a^3$ with $a$ the semi-major axis.

**Kepler II, derived — it is calculus in two lines.** In a short time $dt$ the planet moves $\vec v\,dt$, so the line from the Sun sweeps a thin triangle with sides $\vec r$ and $\vec v\,dt$. A triangle is half its parallelogram, and the parallelogram's area is the [[Cross Product]]'s magnitude:

$$dA = \tfrac12\,\lvert \vec r \times \vec v\,dt \rvert \qquad\Longrightarrow\qquad \frac{dA}{dt} = \frac{\lvert \vec r \times m\vec v \rvert}{2m} = \frac{L}{2m}.$$

The sweep rate *is* the angular momentum, divided by $2m$. Now the physics: gravity points along $-\vec r$, straight at the Sun, so its torque about the Sun is $\vec r \times \vec F = \vec 0$ — and with no torque, $L$ never changes ([[Angular Momentum]] works this orbit as its own example). Constant $L$ means constant $dA/dt$: **equal areas in equal times**. Where the orbit dives close, $r$ shrinks, so $v$ must grow to keep $\tfrac12 r v\sin\theta$ fixed — the comet's plunge past the Sun and its crawl through aphelion are one conservation law seen twice. (In polar language the same statement reads $\dfrac{dA}{dt} = \tfrac12 r^2\,\dfrac{d\theta}{dt}$ — the sector-area integrand of [[Polar Coordinates]] running with time as the parameter.)

### Geostationary satellites — the orbit you are pointed at

A satellite that stays above one spot on the ground must go round exactly as the Earth turns: **period one sidereal day** ($23$ h $56$ min $= 86\,164$ s), **west to east**, and **in the plane of the Equator** — a tilted orbit would cross the Equator twice a day and drift north and south of its spot. *Tool: Kepler III solved for $r$.*

$$r = \left(\frac{GM T^2}{4\pi^2}\right)^{1/3} = \left(\frac{3.99\times10^{14}\times(86\,164)^2}{4\pi^2}\right)^{1/3} = 4.22\times10^7\ \text{m}$$

— $42\,200$ km from the centre, $35\,800$ km above the surface, $v = 3.07$ km s⁻¹. That is why a satellite dish is bolted still: its target never moves. (GPS satellites sit lower, at $26\,600$ km with a $12$-hour period, so they sweep the sky and you need four in view.)

### Real question — a synchronous satellite at Jupiter (AP Physics C Mechanics, 2001 Mech 2)

*A satellite is to be placed in a circular orbit of radius $R$ round Jupiter ($M_J = 1.90\times10^{27}$ kg, $R_J = 7.14\times10^7$ m). (a) Use Newton's laws to show $v = \sqrt{GM_J/R}$ and $T = \sqrt{4\pi^2R^3/GM_J}$. (b) The orbit is to be synchronised with Jupiter's rotation, period $9$ h $51$ min $= 3.55\times10^4$ s. Find the required radius. (c) If the injection speed is slightly faster, or slightly slower, than the circular speed at that height (direction correct), sketch and describe the resulting orbit.*

**(a)** *Tool: gravity as the centripetal force* — exactly the two boxed lines above, with $M_J$ for $M$. (The mark scheme wants $GM_Jm/R^2 = mv^2/R$ written down, not the result quoted.)

**(b)** *Tool: Kepler III for $R$:* $R = \left(\dfrac{GM_J T^2}{4\pi^2}\right)^{1/3} = \left(\dfrac{6.67\times10^{-11}\times1.90\times10^{27}\times(3.55\times10^4)^2}{4\pi^2}\right)^{1/3} = \boxed{1.59\times10^8\ \text{m}}$ — about $2.2$ Jovian radii, so a real orbit, not inside the planet.

**(c)** *Tool: the cannon.* Too fast for a circle at that radius and the satellite is *above* circular speed at the injection point: it climbs away, and the injection point becomes the **lowest point (perijove)** of an ellipse. Too slow and it falls inward from there: the injection point is the **highest point (apojove)** of an ellipse — and if the speed is low enough the ellipse intersects the planet. In both cases the orbit is still closed and periodic; only the shape changes.

---

## Potential and energy — the map's contours

Work has to be done *against* gravity to move a mass outward, and it is the integral of a varying force, so "$mgh$" will not do over large distances. *Tool: work = force × displacement, integrated, with outward taken as positive.* An external agent bringing a test mass $m$ slowly in from infinity must push **outward** with $GMm/x^2$ (to balance the inward pull) while the mass moves **inward** ($dx < 0$), so the agent's work is

$$W = \int_{\infty}^{r} \frac{GMm}{x^2}\,dx = \left[-\frac{GMm}{x}\right]_{\infty}^{r} = -\frac{GMm}{r}$$

— negative: the field did the work, the agent held it back. Hence the **potential energy** $U = -\dfrac{GMm}{r}$ and the **potential** $\varphi = U/m = -\dfrac{GM}{r}$, both zero at infinity by construction.

> [!tip] Why is the potential *negative*? — a three-step argument, not a convention to memorise
> 1. **The zero has to go somewhere**, because only *differences* in potential are ever measured. The one distinguished place in every gravitational field is infinity — the only point where the field genuinely vanishes, and the only choice that Earth, Sun and every galaxy can share. So define $\varphi(\infty) = 0$. (Near-surface work with $mgh$ quietly puts its zero at the floor instead — perfectly legal, but then every problem owns a private zero; infinity is the universal one.)
> 2. **Gravity attracts.** A mass drifting in from infinity is *helped* the whole way: the field does positive work on it, handing it $GMm/r$ of kinetic energy by the time it arrives at $r$. Coming in costs nothing — the field *pays you*.
> 3. **So getting back out must cost exactly that much.** The energy at $r$ sits *below* the zero at infinity by the amount the field paid: $U(r) = 0 - GMm/r < 0$. "Negative" does not mean owing anything mystical — it means *below the chosen zero*, like a depth below sea level: to get back to sea level (freedom, at infinity) you must pay in $\lvert U \rvert$.
>
> The sign then carries real physics for free: total energy $E < 0$ means **bound** (a moon, a satellite, a planet — it cannot afford to leave), $E \geq 0$ means **free** (a passing comet, an escaping probe). And a *repulsive* force runs the argument backwards — pushing two like charges together costs work, so their potential energy is *positive* — the one sign flip to watch when [[Electric Field]] reuses this whole map.

![[gravitational-fields-g-and-phi.svg|760]]

Read the two graphs together, because every potential question lives on them:

- **$\varphi$ is negative everywhere and rises toward zero at infinity** — a well, not a hill. The surface of the Earth sits at $\varphi = -62.6$ MJ kg⁻¹; that number is the energy per kilogram needed to climb all the way out.
- **The field is the slope of the potential**: $g = -\dfrac{d\varphi}{dr}$ (differentiate $-GM/r$ and you get $+GM/r^2$, the magnitude; the minus sign says the force points *down* the potential gradient — toward more negative $\varphi$). Steep well, strong field.
- **The area under the $g$–$r$ graph between two radii is $\Delta\varphi$**, the work per kilogram to climb between them — the integral read backwards.
- **Equipotentials** are spheres of constant $\varphi$, always perpendicular to the field lines; moving a mass along one costs no work, and $W = m\,\Delta\varphi$ between two of them.
- **$mgh$ is the straight-line approximation near the surface.** *Tool: subtract two potentials:* $U(R+h) - U(R) = GMm\left(\dfrac1R - \dfrac1{R+h}\right) = \dfrac{GMm\,h}{R(R+h)} \approx \dfrac{GM}{R^2}\,mh = mgh$ for $h \ll R$. For $h = 100$ km the exact figure is $0.967$ MJ kg⁻¹ against $mgh$'s $0.981$ — $1.5\%$ out, which is $mgh$'s whole error budget.

### Escape speed — fill the well in one go

*Tool: energy conservation from the surface to infinity, arriving with nothing to spare.* $\tfrac12 mv^2 - \dfrac{GMm}{R} = 0 + 0$, so

$$v_{\text{esc}} = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$$

— **independent of the escaping mass** (a pebble and a rocket need the same speed), and exactly $\sqrt2$ times the circular-orbit speed at the same radius. Earth: $11.2$ km s⁻¹. The Moon: $2.4$ km s⁻¹ — below the thermal speeds of light gases over geological time, which is why the Moon has kept no atmosphere and the Earth has. (The Sun: $618$ km s⁻¹; a body whose escape speed reaches $c$ is a black hole — for the Sun's mass that would need a radius of $3$ km. Beyond syllabus, but the formula is the same.)

> [!tip] The Further-Mechanics route to the same number — and why the sign matters (9231 §3.5 · IAL M3)
> Treat it as *motion under a variable force*: a particle at distance $x$ from the centre has acceleration $-\dfrac{GM}{x^2} = -\dfrac{gR^2}{x^2}$ (using $GM = gR^2$). *Tool: $a = v\,\dfrac{dv}{dx}$, separate and integrate from the surface:*
> $$\int_u^{v} v\,dv = -gR^2\int_R^{x}\frac{dx}{x^2} \;\Longrightarrow\; \tfrac12 v^2 - \tfrac12 u^2 = gR^2\left(\frac1x - \frac1R\right).$$
> The particle escapes if $v$ never reaches zero as $x \to \infty$, i.e. $\tfrac12 u^2 \geq gR$, $u \geq \sqrt{2gR}$ — the same answer, now as a differential equation. The 9231 examiners set this shape with any inverse-square force (a recent Paper 3 has a *resistive* force $\propto 1/x^2$ and asks for the closest approach — identical machinery, the sign of the force the only difference).

### The energy of an orbit — faster yet poorer

For a circular orbit $v^2 = GM/r$, so:

$$\text{KE} = \tfrac12 mv^2 = \frac{GMm}{2r}, \qquad U = -\frac{GMm}{r}, \qquad E = \text{KE} + U = -\frac{GMm}{2r}.$$

KE is always exactly half the size of $U$ and the total is negative — **bound**. $E = 0$ is escape. Three consequences that catch students every year:

- **A lower orbit is faster but has less total energy.** To climb to a higher orbit you must *add* energy (fire the engine forward) — and you arrive moving *slower*. To descend, you brake. The rocket-pilot's paradox: accelerate to slow down.
- **Atmospheric drag makes a satellite speed up.** Drag does negative work, $E$ falls, $r$ falls, and $v = \sqrt{GM/r}$ *rises*; the orbit spirals in, faster and faster, until re-entry. (IB D.1.4 asks exactly this.)
- **Work to change orbit** $= \Delta E = \dfrac{GMm}{2}\left(\dfrac1{r_1} - \dfrac1{r_2}\right)$. Two identical satellites at $3R$ and $4R$: $E_X = -GMm/6R$, $E_Y = -GMm/8R$, so moving X out to Y's orbit takes $GMm/24R = \tfrac14 K_X$ — the AP multiple-choice answer, and a one-line check on the energy formulas.

![[gravitational-fields-orbit-energy.svg|760]]

**Energy to launch.** From rest on a non-rotating planet's surface to a circular orbit of radius $r$: $\Delta E = E_{\text{orbit}} - E_{\text{surface}} = -\dfrac{GM}{2r} + \dfrac{GM}{R}$ per kilogram. For the ISS that is $33$ MJ kg⁻¹ — eight times the energy released by a kilogram of TNT, which is why rockets are mostly fuel. To escape entirely: $62.6$ MJ kg⁻¹ (the depth of the well).

---

## Worked — the 9702 standards, every tool named

**1. $g$ on the Moon.** $M = 7.35\times10^{22}$ kg, $R = 1.74\times10^6$ m. *Tool: $g = GM/R^2$* $= 6.67\times10^{-11}\times7.35\times10^{22}/(1.74\times10^6)^2 = 1.62$ N kg⁻¹ — a sixth of Earth's, from first principles.

**2. The neutral point between Earth and Moon.** Where on the line between them is the net field zero? *Tool: two inverse-square fields in opposite directions, set equal:* $\dfrac{GM_E}{x^2} = \dfrac{GM_M}{(d - x)^2} \Rightarrow \dfrac{d-x}{x} = \sqrt{\dfrac{M_M}{M_E}} = \sqrt{\dfrac{7.35\times10^{22}}{5.97\times10^{24}}} = 0.111$, so $x = \dfrac{d}{1.111} = 0.90\,d$ — $346\,000$ km from Earth's centre, nine-tenths of the way. Past that point a spacecraft falls toward the Moon. (Field strengths *add as vectors*; potentials, being scalars, simply add — the potential at the neutral point is *not* zero, it is $-\dfrac{GM_E}{x} - \dfrac{GM_M}{d-x}$.)

**3. Escape from the Moon.** *Tool: $v = \sqrt{2GM/R}$* $= \sqrt{2\times6.67\times10^{-11}\times7.35\times10^{22}/1.74\times10^6} = 2.38$ km s⁻¹. The Apollo ascent stage needed less than that, because it only had to reach lunar orbit ($\sqrt{GM/R} = 1.68$ km s⁻¹).

**4. Potential energy change for a real lift.** A $1000$ kg satellite raised from the surface to $400$ km: *Tool: $\Delta U = GMm\left(\frac1{R} - \frac1{R+h}\right)$* $= 3.99\times10^{14}\times1000\times\left(\dfrac1{6.37\times10^6} - \dfrac1{6.77\times10^6}\right) = 3.7\times10^9$ J; $mgh$ would say $3.9\times10^9$ J, $6\%$ high, because $g$ is smaller up there. Add the kinetic energy of orbit, $\tfrac12 m v^2 = \tfrac12\times1000\times(7.67\times10^3)^2 = 2.9\times10^{10}$ J, and you see that **most of the cost of orbit is speed, not height** — the ISS is only $400$ km up but moving at Mach 22.

---

## Where this is the working tool

- **Every satellite that serves you was placed with $T^2 = 4\pi^2 r^3/GM$.** Weather and TV satellites at the geostationary $42\,200$ km; GPS at $26\,600$ km so that any horizon holds four; the ISS at $6\,790$ km because low is cheap to reach and easy to resupply. Mission designers live on the energy graph above: a transfer between orbits is two burns and one $\Delta E$.
- **GPS also runs on the potential.** Clocks in the weaker field at $20\,000$ km run fast by $45\ \mu$s a day (general relativity: deeper potential, slower time), and their orbital speed slows them by $7\ \mu$s — a net $38\ \mu$s a day that would put your position off by $10$ km by evening if the satellites' clocks were not pre-slowed before launch. The $-GM/r$ of this page is the first-order version of the potential that sets that correction.
- **Gravimetry finds oil, ore and aquifers.** Denser rock below makes $g$ fractionally larger above it; survey gravimeters resolve $10^{-8}$ of $g$, and the GRACE satellites mapped the Earth's field well enough to watch Greenland's ice loss and India's groundwater drawdown as changes in $g$ month by month.
- **Cavendish's torsion balance** is still the way $G$ is measured — it remains the least precisely known fundamental constant (about one part in $50\,000$), because gravity is so weak that everything else in the room competes with it.
- **The tides** are the *gradient* of the Moon's field across the Earth's diameter: the near side is pulled more than the centre, the far side less, so the ocean bulges on both sides — two high tides a day. The same stretching, near a black hole, is what the word *spaghettification* describes.

---

## Common Misconceptions (Teaching Notes)

### 1. "There is no gravity in space — that is why astronauts float"

At the ISS $g = 8.6$ N kg⁻¹, $88\%$ of the surface value. Astronauts float because they and the station are in the *same free fall* round the Earth: gravity is the centripetal force and nothing else pushes on them — exactly the loop-the-loop top with $N = 0$ from [[Circular Motion]].

**Fix:** compute $g$ at the ISS with $GM/r^2$; then ask what happens to the orbit if gravity *were* zero (a straight line off into space).

### 2. Potential being negative means "owing" something physical

It means only that the zero was put at infinity, where the field vanishes. Only *differences* in potential are measurable ($W = m\Delta\varphi$); the sign tells you that work must be *done on* a mass to move it outward.

**Fix:** the well picture — climbing out costs energy, so everywhere inside is below zero.

### 3. "Escape speed depends on the mass of the rocket"

$\tfrac12 mv^2 = GMm/R$ — the $m$ cancels. A heavier rocket needs more *energy* and more *fuel*, but the same *speed*.

**Fix:** write the energy equation with the $m$ in and cancel it on the page.

### 4. $r$ measured from the surface

Every formula on this page has $r$ from the **centre** of the attracting mass. A satellite "$400$ km up" is at $r = 6371 + 400 = 6771$ km. Using $400$ km gives garbage a thousand times too large.

**Fix:** first line of every answer: "$r = R + h = \ldots$".

### 5. "A geostationary satellite can hover above any city"

Only above the Equator: its orbit must be centred on the Earth's centre and share the Earth's axis, so the only closed orbit that stays over one point is equatorial, period $24$ h, west to east. London and Chengdu see their satellites low in the southern sky.

**Fix:** draw an orbit tilted to the Equator and follow it for half a day — the ground track drifts north, then south.

### 6. Treating $g$ as "the gravity constant"

$g$ is the *field strength at a place* — $9.81$ at sea level, $9.78$ at the Equator, $8.6$ at the ISS, $1.62$ on the Moon. The constant is $G$.

**Fix:** say "field strength" aloud when you mean $g$, and "gravitational constant" for $G$; never write one for the other.

### 7. Adding potentials like vectors, or field strengths like scalars

Field strength is a vector — between two masses the fields oppose and can cancel (the neutral point). Potential is a scalar — the two potentials simply add, and never cancel, since both are negative.

**Fix:** Worked 2 above, done both ways.

---

## Exam Notes

### Cambridge 9702 (A-Level Physics, Topic 13 — Gravitational fields)

- **§13.1:** the field as a field of force; define field strength as force per unit mass; field lines. **§13.2:** a uniform sphere acts from its centre; **recall and use** $F = Gm_1m_2/r^2$; analyse circular orbits by equating gravity to the centripetal force; geostationary orbits — same point above the surface, $24$ h, west to east, directly above the Equator (all four properties are mark-bearing). **§13.3:** **derive** $g = GM/r^2$ from the law and the definition; recall and use it; explain why $g$ is nearly constant close to the surface (the $2h/R$ argument). **§13.4:** define potential as work done per unit mass from infinity; use $\varphi = -GM/r$; $E_P = -GMm/r$.
- **The data sheet prints $G$ and $\varphi = -GM/r$** — but *not* $F = Gm_1m_2/r^2$ or $g = GM/r^2$, which are recall. Escape speed is not named in the syllabus but is a routine "use energy" question.
- Typical marks: define field strength / potential in words (precision: *per unit mass*, *from infinity*); "show that" $T^2 \propto r^3$; the geostationary radius; $g$ on another planet; potential-energy changes with the sign argued; a sketch of $g$ or $\varphi$ against $r$ with the right shape and intercept.

### Cambridge 0625 (IGCSE Physics, §1.3 and §6.1)

- **§1.3:** $g$ as gravitational field strength, $W = mg$, mass vs weight. **§6.1 Space physics:** the Sun's gravitational attraction keeps the planets in orbit; field strength at a planet's surface depends on its mass and decreases with distance; orbital speed $v = 2\pi r/T$ (recall and use); planets, minor planets and comets move in ellipses with the Sun not at the centre; an object in an elliptical orbit moves faster when closer (by energy conservation — the Kepler II picture); orbital speeds fall with distance from the Sun; geostationary satellites qualitatively. No $G$, no formula for $F$.

### IB Physics (D.1 Gravitational fields)

- **SL:** Kepler's three laws; $F = GMm/r^2$ for point masses, extended to uniform spheres; $g = F/m$; field lines. **HL:** $E_p = -GMm/r$, $V_g = -GM/r$, $g = -\Delta V_g/\Delta r$ (field = potential gradient), $W = m\Delta V_g$, equipotential surfaces and their relation to field lines, escape speed $\sqrt{2GM/r}$, orbital speed $\sqrt{GM/r}$, the qualitative effect of atmospheric drag (orbit lowers, speed rises), energy changes when a satellite changes orbit, the energetics of launching from rest on a non-rotating planet, and the energy condition for escape. Orbits are taken as circular for calculation; resultant fields only along the line joining two masses. All the formulas are in the data booklet.

### AP Physics 1 (Unit 2 §2.6, Unit 6 §6.6)

- **2.6:** the gravitational force between two systems — attractive, along the line of centres, $\propto m_1 m_2/r^2$; the field model, $g = F/m$, weight $= mg$; near the surface $g \approx 10$ N kg⁻¹ is uniform; apparent weight. **6.6:** satellite motion — in circular orbits total energy, potential energy, kinetic energy and angular momentum are all constant; in elliptical orbits $E$ and $L$ are constant while KE and $U$ trade; $U = -Gm_1m_2/r$. Equation sheet: $F_g = Gm_1m_2/r^2$, $g = GM/r^2$, $U_G = -Gm_1m_2/r$.

### AP Physics C: Mechanics (Unit 2 §2.6)

- The same, with calculus: derive orbital speed and period from Newton's laws (the 2001 Jupiter question above is the template), energy and angular momentum in elliptical orbits, the work to move between orbits. Gravitation is integrated across the free-response set rather than a separate unit.

### OxAQA 9660 (M2.7) · Edexcel IAL (M3.3) · Cambridge 9231 (§3.5)

- **9660 M2.7** names a satellite in a circular orbit, gravity toward the centre, as a circular-motion context. **IAL M3.3 and 9231 §3.5** use the inverse-square *force* as a variable-force problem: $v\,dv/dx = -k/x^2$, integrate, ask for escape or closest approach — the tip box above is exactly the shape.

### Where it is *not* examined

Not on Cambridge 9709 (no gravitation beyond $W = mg$), not on OxAQA 9260, 0580 or 0606, not in IB AA/AI, and not on AP Physics 2 (gravitation lives in Physics 1 and C).

---

## Connections

- **Parent:** [[Circular Motion]] — gravity is the centripetal force in every orbit on this page; [[Newton's Laws of Motion]] — $F = ma$ with $F = GMm/r^2$.
- **Energy:** [[Work, Energy and Power]] — the potential is work per unit mass, $mgh$ is its near-surface shadow, and orbital energy is KE $+$ U with KE $= -\tfrac12 U$.
- **Calculus:** [[Integration]] gives $\varphi$ from $g$ (area under the $g$–$r$ graph); [[Differentiation]] gives $g$ from $\varphi$ (the gradient).
- **Leads to:** [[Electric Field]] — the same map with charge for mass and $1/4\pi\varepsilon_0$ for $G$, the one difference being that like charges repel; [[Angular Momentum]] — Kepler's second law *is* its conservation.
- **Kinship:** [[Simple Harmonic Motion]] — the tunnel through the Earth; [[Vectors in Physics]] — field strengths add as vectors, potentials as scalars.
- **Stories:** [[Newton vs Hooke]] — who had the inverse square first, and what "standing on the shoulders of giants" was really about; [[The 1919 Eclipse]] — the day Newton's gravity met its successor.
- **For 9702 students:** the data sheet gives $G$ and $\varphi = -GM/r$; $F = Gm_1m_2/r^2$ and $g = GM/r^2$ are yours to recall — or to re-derive from the law and the definition, which §13.3 asks for anyway.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $F = \dfrac{Gm_1m_2}{r^2}$ | `F = \frac{G m_1 m_2}{r^2}` | Newton's law, point masses |
| $g = \dfrac{F}{m} = \dfrac{GM}{r^2}$ | `g = \frac{F}{m} = \frac{GM}{r^2}` | field strength, toward the centre |
| $\varphi = -\dfrac{GM}{r}$ | `\varphi = -\frac{GM}{r}` | potential, zero at infinity |
| $U = -\dfrac{GMm}{r}$ | `U = -\frac{GMm}{r}` | potential energy |
| $g = -\dfrac{d\varphi}{dr}$ | `g = -\frac{d\varphi}{dr}` | field = potential gradient |
| $v = \sqrt{\dfrac{GM}{r}}$ | `v = \sqrt{\frac{GM}{r}}` | circular-orbit speed |
| $T^2 = \dfrac{4\pi^2}{GM}\,r^3$ | `T^2 = \frac{4\pi^2}{GM}\,r^3` | Kepler III, derived |
| $v_{\text{esc}} = \sqrt{\dfrac{2GM}{R}}$ | `v_{\text{esc}} = \sqrt{\frac{2GM}{R}}` | escape speed, $\sqrt2\,v_{\text{circ}}$ |
| $E = -\dfrac{GMm}{2r}$ | `E = -\frac{GMm}{2r}` | total energy of a circular orbit |

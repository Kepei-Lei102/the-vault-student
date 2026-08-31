---
chinese: 转动惯量 (zhuàndòng guànliàng)
prerequisites:
  - "[[Torque]]"
  - "[[Centre of Mass]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Integration]]"
  - "[[Areas and Volumes by Integration]]"
  - "[[Work, Energy and Power]]"
leads_to:
  - "[[Angular Momentum]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - level/pre-AP
  - curriculum/A-Level-Further
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/IB-Physics-A-4-3
  - syllabus/AP-Physics-1-5-4
  - syllabus/AP-Physics-C-Mech-5-4
  - syllabus/AP-Physics-C-Mech-5-6
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/moment-of-inertia
  - notation/integral
  - misconception/inertia-is-fixed-like-mass
  - misconception/r-is-distance-to-axis-not-point
  - misconception/heavier-rolls-faster
  - misconception/perpendicular-axis-on-3d
---

# Moment of Inertia 转动惯量

## Definition

### Formal

The **moment of inertia** of a body about a chosen axis is

$$\boxed{\;I = \sum_i m_i r_i^2 \quad\text{(discrete)},\qquad I = \int r^2 \, dm \quad\text{(continuous)}\;}$$

where $r_i$ (or $r$) is the **perpendicular distance from the rotation axis** to each mass element. It is the rotational analogue of mass: the quantity that resists angular acceleration, through the rotational Newton's second law

$$\boldsymbol{\tau} = I\alpha.$$

Units: $\text{kg·m}^2$.

### Intuitive

Mass measures how hard it is to *speed something up in a straight line*: $F = ma$. Moment of inertia measures how hard it is to *spin something up*: $\tau = I\alpha$. That's the [[Torque|τ = Iα]] promise from the previous card, finally given a number.

But $I$ has a twist that mass doesn't. Mass is an intrinsic property of a body — five kilograms is five kilograms. **Moment of inertia is not intrinsic: it depends on the axis you spin about, and on how the mass is spread out relative to that axis.** The same rod has a small $I$ about its long axis and a large $I$ about a perpendicular axis through one end. Move the mass farther from the axis and $I$ shoots up — and because of the $r^2$, it shoots up *quadratically*. A tightrope walker's long pole, a figure skater's outstretched arms, and a flywheel with a heavy rim all exploit the same fact: mass far from the axis is mass that fights rotation hard.

### 中文锚点

**转动惯量**（zhuàndòng guànliàng）：转动里"质量"的对应物——抵抗**角加速度**的本领，遵从转动版牛顿第二定律 $\tau = I\alpha$。

$$I = \sum m_i r_i^2 \quad\text{(离散)},\qquad I = \int r^2\,dm \quad\text{(连续)}$$

$r$ 是**到转轴的垂直距离**。两个关键点：

1. **它不是物体的固有属性**——和质量不同，转动惯量取决于**转轴位置**和**质量分布**。同一根棒，绕不同轴，$I$ 不同。
2. **$r^2$ 是全部的秘密**：离轴越远，贡献越大，而且是**平方**地大。所以质量集中在边缘（铁环）比集中在中心（实心球）更"难转"。

平动 $m$ ↔ 转动 $I$；$F=ma$ ↔ $\tau=I\alpha$；$\tfrac12 mv^2$ ↔ $\tfrac12 I\omega^2$。

## The mass ↔ inertia analogy — and the one big difference

Rotational dynamics is linear dynamics with every quantity swapped for its angular twin (the full table is in [[Torque]]). The piece this card supplies is the **resistance**:

| Linear | Rotational |
|---|---|
| mass $m$ — resists $a$ | moment of inertia $I$ — resists $\alpha$ |
| $F = ma$ | $\tau = I\alpha$ |
| kinetic energy $\tfrac12 mv^2$ | rotational KE $\tfrac12 I\omega^2$ |
| momentum $mv$ | angular momentum $I\omega$ (→ [[Angular Momentum]]) |

The analogy is near-perfect except for one thing, and it is the thing students most often miss: **mass is one number for a body; moment of inertia is a different number for every axis.** You must always say "moment of inertia *about which axis*." That dependence is the whole subject.

## Notation

| Symbol | Read as | Notes |
|---|---|---|
| $I$ | moment of inertia | About a *specified* axis; $\text{kg·m}^2$ |
| $r$ | perpendicular distance | From the **axis** (not from a point) to the mass element |
| $dm$ | mass element | $dm = \rho\,dV$ (or $\lambda\,dx$ for a rod, $\sigma\,dA$ for a lamina) |
| $\alpha$ | angular acceleration | $\tau = I\alpha$ |
| $\omega$ | angular velocity | rotational KE $= \tfrac12 I\omega^2$ |
| $I_{\text{cm}}$ | about the centre of mass | the reference for the parallel-axis theorem |

## Key Facts / Properties

### 1. Why $r^2$? — the definition is forced by $\tau = I\alpha$

The $r^2$ is not a convention; it is *forced* the moment you ask for a rotational copy of $F = ma$. Take a single particle of mass $m$ at perpendicular distance $r$ from the axis. A tangential force $F$ gives it linear acceleration $a = F/m$, and the tangential and angular accelerations are linked by $a = r\alpha$. The torque about the axis is

$$\tau = Fr = (ma)r = m(r\alpha)r = (mr^2)\,\alpha.$$

Compare with $\tau = I\alpha$: the bracket $mr^2$ *is* the particle's moment of inertia. Add up many particles and the torques add, so $I = \sum m_i r_i^2$. The squared distance falls straight out of "tangential acceleration is $r\alpha$" — there was never any freedom in it.

### 2. From sum to integral — and why integration is the right tool

$I = \sum m_i r_i^2$ is exact for a handful of point masses. But a solid rod or disc isn't a handful of points — it's a *continuum*, with mass smeared over every position. You'd need to add up infinitely many infinitesimally small pieces, and *adding up infinitely many infinitesimal contributions is exactly what an integral is* (see [[Integration]] — a definite integral is the limit of a Riemann sum). So we slice the body into mass elements $dm$, each at its own distance $r$ from the axis, and replace the sum by an integral:

$$\sum_i m_i r_i^2 \;\longrightarrow\; I = \int r^2 \, dm.$$

**The trick is turning $dm$ into something you can integrate.** You can't integrate "$dm$" directly — you integrate over a *position* coordinate. So you trade mass for length (or area, or volume) using the body's **density**:

- a **rod** (1D) has linear density $\lambda = M/L$, so a slice of width $dx$ has mass $dm = \lambda\,dx$;
- a **lamina** (2D) has surface density $\sigma$, so $dm = \sigma\,dA$;
- a **solid** (3D) has volume density $\rho$, so $dm = \rho\,dV$.

Once $dm$ is written in terms of a coordinate, the integral is an ordinary one.

> [!info] Calculus prerequisite — building area and volume by integration
> The disc and sphere results below lean on a skill from calculus: assembling a shape's **area or volume by integrating thin rings, shells, or discs**. The disc's mass uses the *ring* picture — a circle's area is $\int_0^R 2\pi r\,dr = \pi R^2$, the sum of thin rings of circumference $2\pi r$ — and the sphere stacks discs the same way its volume is built by integration. If "the area of a circle is $\int 2\pi r\,dr$" isn't yet second nature, read [[Integration]] (which sets up area-under-a-curve and the disc method for volumes of revolution) and [[Areas and Volumes by Integration]] (the ring-and-shell method, with the circle-area and sphere-volume derivations worked in full) first.

**Worked derivation — thin rod about its centre.** Uniform rod, mass $M$, length $L$, so $\lambda = M/L$. Axis through the centre, perpendicular to the rod. A slice at position $x$ has width $dx$, mass $dm = \lambda\,dx$, and sits a distance $r = \lvert x\rvert$ from the axis. Substitute $r^2 = x^2$ and $dm = \lambda\,dx$:

$$I = \int_{-L/2}^{L/2} x^2 \,\underbrace{\lambda\, dx}_{dm} = \lambda\left[\frac{x^3}{3}\right]_{-L/2}^{L/2} = \frac{M}{L}\cdot\frac{2}{3}\cdot\frac{L^3}{8} = \frac{1}{12}ML^2.$$

![[moment-of-inertia-rod-integral.svg]]
*The setup behind $I=\int r^2\,dm$ for the rod. Chop the rod into slices of width $dx$; the slice at position $x$ carries mass $dm = \lambda\,dx$ (with $\lambda = M/L$) and sits $r = \lvert x\rvert$ from the perpendicular axis through the centre. Integrating $x^2\,\lambda\,dx$ from $-L/2$ to $L/2$ adds up every slice's $r^2\,dm$ contribution.*

### 3. The standard results worth memorising

All about an axis through the centre of mass unless stated. The **coefficient is a report on how far the mass sits from the axis**:

| Body | Axis | $I$ |
|---|---|---|
| Point mass | distance $R$ | $MR^2$ |
| Thin ring / hoop | $\perp$ through centre | $MR^2$ |
| Solid disc / cylinder | through central axis | $\tfrac12 MR^2$ |
| Thin rod | $\perp$ through centre | $\tfrac{1}{12}ML^2$ |
| Thin rod | $\perp$ through one end | $\tfrac13 ML^2$ |
| Solid sphere | through centre | $\tfrac25 MR^2$ |
| Thin spherical shell | through centre | $\tfrac23 MR^2$ |

Read the coefficients as a story: the hoop puts *all* its mass at radius $R$, so it scores the maximum $1$; the disc spreads mass inward, dropping to $\tfrac12$; the solid sphere packs most of its mass near the centre, dropping to $\tfrac25$. Same $M$, same $R$, wildly different willingness to spin.

![[moment-of-inertia-shapes-and-race.svg]]
*Left: the three workhorse shapes, same mass and radius, ranked by how far their mass sits from the axis — hoop ($MR^2$) at the rim, disc ($\tfrac12 MR^2$), solid sphere ($\tfrac25 MR^2$) packed inward. Right: the consequence (Example 1). Released together down a ramp, they finish in order of smallest coefficient — sphere, then disc, then hoop — and the result doesn't depend on their mass or radius at all.*

### Where each standard result comes from

> [!info] Skippable — the table and picture above are enough to *use* the results
> This section is for anyone who wants to see where each coefficient is *born*. Every one is the same recipe: write down a mass element $dm$, multiply by its $r^2$ (how far it is from the axis), and add up with $\int r^2\,dm$. In each integral below the two ingredients are flagged — the $r^2$ and the $dm$ — so you can see exactly what is being summed.

**Hoop / ring** — axis perpendicular through the centre.

This is the easy one, because a thin hoop puts *every* scrap of its mass at the same distance $R$ from the axis. There is nothing to vary across the body: $r^2 = R^2$ is constant, so it slides straight out of the integral and only the total mass is left behind.

$$I = \int \underbrace{R^2}_{r^2}\;\underbrace{dm}_{\text{mass here}} \;=\; R^2\!\int dm \;=\; MR^2.$$

The hoop barely needs calculus at all — and it is the reason $MR^2$ is the *largest* coefficient any shape of radius $R$ can have. Nothing can sit farther out than the rim.

**Solid disc / cylinder** — axis through the central axis.

Now the mass is spread across every radius from $0$ to $R$, so we genuinely have to integrate. Slice the disc into thin concentric **rings**. A ring at radius $r$ with thickness $dr$ has circumference $2\pi r$, so its area is $2\pi r\,dr$ and its mass is $dm = \sigma\,2\pi r\,dr$, where $\sigma = M/(\pi R^2)$ is the mass per unit area. Every part of that ring lies at the same distance $r$ from the axis, so the ring contributes $r^2\,dm$:

$$I = \int_0^R \underbrace{r^2}_{r^2}\;\underbrace{\sigma\,2\pi r\,dr}_{dm} \;=\; 2\pi\sigma\int_0^R r^3\,dr \;=\; 2\pi\sigma\,\frac{R^4}{4} \;=\; \tfrac12 MR^2,$$

once you substitute $\sigma = M/(\pi R^2)$. All the mass crowded near the centre contributes very little (small $r^2$), which is exactly why the coefficient drops from the hoop's $1$ down to $\tfrac12$.

**Thin rod about one end** — axis perpendicular.

This is the rod integral from §2 again, with the slice now running from $0$ to $L$ instead of $-\tfrac{L}{2}$ to $\tfrac{L}{2}$:

$$I = \int_0^L \underbrace{x^2}_{r^2}\;\underbrace{\lambda\,dx}_{dm} \;=\; \lambda\,\frac{L^3}{3} \;=\; \tfrac13 ML^2.$$

That is four times the centre value $\tfrac1{12}ML^2$ — pivoting at the end throws much more of the rod out to large $x$, and the $x^2$ punishes that heavily.

**Solid sphere** — axis through the centre.

Here we *reuse* a result instead of integrating point by point. Stack the sphere out of thin **discs** perpendicular to the axis. The disc at height $z$ has radius $a = \sqrt{R^2 - z^2}$, thickness $dz$, and mass $dm = \rho\,\pi a^2\,dz$. We already worked out that a disc's own moment of inertia about its central axis is $\tfrac12(\text{mass})(\text{radius})^2$, so each disc contributes $dI = \tfrac12\,dm\,a^2$:

$$I = \int_{-R}^{R} \tfrac12\;\underbrace{(R^2 - z^2)}_{a^2,\ \text{the disc's own } r^2}\;\underbrace{\rho\,\pi(R^2 - z^2)\,dz}_{dm} \;=\; \tfrac25 MR^2,$$

with $\rho = M/\big(\tfrac43\pi R^3\big)$. A solid sphere buries most of its mass close to the axis, so the coefficient falls all the way to $\tfrac25$.

**Thin spherical shell** — axis through the centre.

Slice the shell into thin **rings**, like lines of latitude. The ring at polar angle $\theta$ has radius $R\sin\theta$, width $R\,d\theta$ measured along the surface, and circumference $2\pi R\sin\theta$, so its mass is $dm = \sigma\,(2\pi R\sin\theta)(R\,d\theta)$ with $\sigma = M/(4\pi R^2)$. Every point on that ring is the same distance $R\sin\theta$ from the axis:

$$I = \int_0^{\pi} \underbrace{(R\sin\theta)^2}_{r^2}\;\underbrace{\sigma\,2\pi R^2\sin\theta\,d\theta}_{dm} \;=\; \tfrac23 MR^2.$$

A hollow shell keeps *all* its mass out near the surface — none of it hides near the centre the way a solid sphere's does — so its coefficient $\tfrac23$ sits above the solid sphere's $\tfrac25$, exactly as the table claims.

### 4. The parallel-axis theorem — $I = I_{\text{cm}} + Md^2$

You rarely want the axis through the centre of mass. The **parallel-axis theorem** shifts a known centre-of-mass result to any parallel axis a distance $d$ away:

$$\boxed{\;I = I_{\text{cm}} + Md^2.\;}$$

**Proof.** Put the origin at the centre of mass, with the CM axis along $z$. A mass element at in-plane position $(x, y)$ sits a distance $r_{\text{cm}}^2 = x^2 + y^2$ from the CM axis. Now take a parallel axis displaced by $d$, say passing through $(d, 0)$; the element's distance from *it* is $r'^2 = (x-d)^2 + y^2$. Integrate:

$$I = \int r'^2\,dm = \int\big[(x-d)^2 + y^2\big]\,dm = \underbrace{\int (x^2+y^2)\,dm}_{I_{\text{cm}}} \;-\; 2d\underbrace{\int x\,dm}_{=\,M x_{\text{cm}}} \;+\; d^2\underbrace{\int dm}_{=\,M}.$$

The middle term is the key: $\int x\,dm = M x_{\text{cm}}$, and because the origin *is* the centre of mass, $x_{\text{cm}} = 0$, so that term vanishes. What's left is

$$I = I_{\text{cm}} + Md^2. \qquad \blacksquare$$

The cross term dying is the whole reason the theorem is so clean — and the reason the reference axis *must* be the one through the centre of mass.

**Check it against the rod.** Rod about its end should be $\tfrac13 ML^2$. Start from the centre ($I_{\text{cm}} = \tfrac{1}{12}ML^2$) and shift by $d = L/2$:

$$I = \tfrac{1}{12}ML^2 + M\left(\tfrac{L}{2}\right)^2 = \tfrac{1}{12}ML^2 + \tfrac14 ML^2 = \tfrac13 ML^2. \;\checkmark$$

A consequence worth noticing: since $Md^2 \ge 0$, **the moment of inertia is smallest about an axis through the centre of mass.** The CM is the easiest place to spin a body.

### 5. The perpendicular-axis theorem — flat bodies only

For a **planar** body (a lamina) lying in the $xy$-plane, the moment about the axis perpendicular to the plane equals the sum of the two in-plane moments:

$$I_z = I_x + I_y \qquad\text{(planar bodies only).}$$

**Example — disc about a diameter.** A disc has $I_z = \tfrac12 MR^2$ about its central axis. By symmetry $I_x = I_y$, so $\tfrac12 MR^2 = 2I_x$, giving $I_x = \tfrac14 MR^2$ about any diameter. (The "planar only" caveat is real — the theorem is false for solid 3D bodies.)

### 6. Rotational kinetic energy — $\tfrac12 I\omega^2$

A spinning body stores kinetic energy, and here the moment of inertia comes from collecting a sum. Treat the body as particles $m_i$ at radii $r_i$. Every particle shares the **same** angular velocity $\omega$, but its actual speed grows with radius: $v_i = r_i\omega$. Add up each particle's ordinary linear kinetic energy $\tfrac12 m_i v_i^2$:

$$\text{KE} = \sum_i \tfrac12 m_i v_i^2 = \sum_i \tfrac12 m_i (r_i\omega)^2 = \tfrac12\Big(\sum_i m_i r_i^2\Big)\omega^2.$$

The $\omega^2$ **factors out of the sum** precisely because it is common to every particle — and the bracket that's left, $\sum_i m_i r_i^2$, is exactly the moment of inertia. So

$$\text{KE}_{\text{rot}} = \tfrac12 I\omega^2,$$

the exact rotational mirror of the $\tfrac12 mv^2$ from [[Work, Energy and Power]] (with $m \to I$ and $v \to \omega$).

![[moment-of-inertia-rotational-ke.svg]]
*Why the sum collapses to $\tfrac12 I\omega^2$. Each particle runs at its own speed $v_i = r_i\omega$ — faster the farther out it is — so its energy is $\tfrac12 m_i r_i^2\omega^2$. The shared $\omega^2$ pulls out of the sum, leaving $\sum m_i r_i^2 = I$ behind.* A body that both moves and spins — a rolling wheel — carries **both**:

$$\text{KE}_{\text{total}} = \underbrace{\tfrac12 Mv_{\text{cm}}^2}_{\text{translation}} + \underbrace{\tfrac12 I_{\text{cm}}\omega^2}_{\text{rotation}}.$$

## Worked Examples

### Example 1 (the rolling race) — why a sphere beats a hoop

A hoop, a solid disc, and a solid sphere are released from rest at the top of a ramp of height $h$ and roll without slipping. Which reaches the bottom first?

Write each shape's moment of inertia as $I = cMR^2$ (so $c = 1$ hoop, $\tfrac12$ disc, $\tfrac25$ sphere). Rolling without slipping links $v = R\omega$. Conservation of energy:

$$Mgh = \tfrac12 Mv^2 + \tfrac12 I\omega^2 = \tfrac12 Mv^2 + \tfrac12 (cMR^2)\frac{v^2}{R^2} = \tfrac12 Mv^2(1 + c).$$

Solving:

$$v^2 = \frac{2gh}{1+c}.$$

The mass $M$ and radius $R$ **cancel completely** — only the shape coefficient $c$ survives. Smaller $c$ means more of the energy goes into translation and less is "wasted" on spin, so:

$$\text{sphere } (c=\tfrac25) \;>\; \text{disc } (c=\tfrac12) \;>\; \text{hoop } (c=1).$$

The solid sphere wins every time, regardless of how heavy or how big the objects are. A beautiful, counterintuitive result that falls straight out of the coefficient table.

### Example 2 (the physical pendulum) — closing the SHM debt

[[Simple Harmonic Motion]] derived the simple pendulum taking $I = mL^2$ "on faith." That value is now justified: a point mass $m$ at the end of a string of length $L$ is, by definition, $I = \sum mr^2 = mL^2$ (one particle at $r = L$). For a *real* swinging body (a rod, a hanging sign — a "physical pendulum"), you instead use its actual $I$ about the pivot, found via the parallel-axis theorem, and the period becomes $T = 2\pi\sqrt{I/(mgd)}$ with $d$ the pivot-to-CM distance. The moment of inertia is the missing ingredient that turns the toy pendulum into the real one.

## Common Misconceptions (Teaching Notes)

### 1. Treating $I$ as a fixed property like mass

Writing "the moment of inertia of the rod is $\tfrac{1}{12}ML^2$" with no axis named.

**Fix.** Always finish the sentence: "...about a perpendicular axis through its centre." Change the axis and the number changes. $I$ belongs to a *body-plus-axis*, never to a body alone.

### 2. Measuring $r$ to a point instead of to the axis

Using the distance from the centre of mass, or from some convenient point, instead of the **perpendicular distance to the rotation axis**.

**Fix.** $r$ is always measured straight out to the axis line. For a mass on the $z$-axis problem, $r = \sqrt{x^2 + y^2}$ — the $z$-coordinate doesn't enter, because sliding a mass *along* the axis doesn't change how far it is *from* the axis.

### 3. "The heavier (or bigger) one rolls faster"

Expecting the massive hoop or the large sphere to win the rolling race.

**Fix.** The rolling-race result $v^2 = 2gh/(1+c)$ has no $M$ and no $R$ in it — only the shape coefficient $c$. A marble and a bowling ball (both solid spheres) tie; a heavy hoop loses to a light sphere. *Shape, not size or weight.*

### 4. Using the parallel-axis theorem from the wrong reference

Applying $I = I_{\text{cm}} + Md^2$ starting from an axis that is *not* through the centre of mass.

**Fix.** The theorem only works when one of the two axes passes through the **centre of mass**. $I_{\text{cm}}$ is the privileged starting point; $d$ is measured from *it*.

### 5. Using the perpendicular-axis theorem on a 3D body

Applying $I_z = I_x + I_y$ to a sphere or cylinder.

**Fix.** It holds for **flat laminae only** (all mass in one plane). For solids it is simply false.

## Exam Notes

> Like [[Torque]], moment of inertia is **not** on Cambridge 9709 (particle mechanics only) or 9702 (which stops at the statics moment), and not on plain IB AA. It is Further / IB-Physics-HL / AP material.

### A-Level Further Mathematics (UK boards — Edexcel / AQA)

**Rotation of a rigid body about a fixed axis** — moment of inertia by integration, the parallel- and perpendicular-axis theorems, rotational KE $\tfrac12 I\omega^2$, and $\tau = I\alpha$ — is examined in **Edexcel** and **AQA** A-Level Further Mechanics (e.g. Edexcel Further Mechanics 2). It is **not** on **Cambridge 9231** (whose Further Mechanics stops at rigid-body *statics* — projectiles, equilibrium, circular motion, Hooke's law, variable force, momentum) and **not** on **Cambridge 9702** physics either (verified against the 9702 syllabus — it carries the torque of a couple as statics and "angular speed" for circular motion, but no rotational dynamics). A Cambridge student therefore meets $I$ only via the IB-Physics-HL or AP routes below.

### IB Physics (A.4.3 — *HL only*)

**A.4.3:** moment of inertia $I$ (qualitative dependence on mass distribution + given formulas), Newton's second law for rotation $\tau = I\alpha$, and rotational kinetic energy $\tfrac12 I\omega^2$. The IB data booklet supplies the standard-shape formulas.

### AP Physics 1 (Unit 5.4) & AP Physics C: Mechanics (Units 5.4, 5.6)

**AP-1 (5.4)** treats rotational inertia largely qualitatively and with given formulas — no integration required. **AP-C** goes the full distance: **5.4** derives $I = \int r^2\,dm$ and uses the parallel-axis theorem, and **5.6** is Newton's second law in rotational form $\tau = I\alpha$. Both supply standard-shape results on the exam equation sheet.

## Connections

- **Prerequisite:** [[Torque]] — the cause; $\tau = I\alpha$ is the equation this card makes computable. [[Newton's Laws of Motion]] — $F = ma$, the linear law the whole analogy mirrors.
- **Mathematical tool:** [[Integration]] — $I = \int r^2\,dm$ is a definite integral over the body.
- **Energy sibling:** [[Work, Energy and Power]] — rotational KE $\tfrac12 I\omega^2$ is the rotational copy of $\tfrac12 mv^2$; rolling bodies carry both.
- **Next in the trio:** [[Angular Momentum]] — $L = I\omega$, $\tau = dL/dt$, and conservation; the figure-skater spin is moment-of-inertia change in action.
- **Application:** [[Simple Harmonic Motion]] — the simple pendulum's $I = mL^2$ and the physical pendulum's $I$ about the pivot.

---

## Beyond Syllabus

### The parallel-axis theorem is the variance decomposition

The algebra of $I = I_{\text{cm}} + Md^2$ is *identical* to a result you already met in statistics. The mean-square distance of the mass from an arbitrary axis equals the mean-square distance from the centre of mass, plus the squared offset — exactly $E[(X-c)^2] = \operatorname{Var}(X) + (E[X]-c)^2$, which is minimised when $c$ is the mean. "Moment of inertia is least about the centre of mass" and "variance is least about the mean" are the *same theorem* (König–Huygens / Steiner). See [[Why Probability and Statistics]] for the variance side. The centre of mass is the mean of the mass distribution; the moment of inertia is its variance.

### Moment of inertia is really a tensor

For rotation about an arbitrary axis, $I$ is not one number but a $3\times3$ matrix, the **inertia tensor**. Most bodies have three special *principal axes* about which it collapses back to a single number — which is why the scalar $I$ works for the symmetric shapes above. When the three principal moments are all different, free rotation about the *middle* one is unstable: a thrown phone or tennis racket flips end-over-end unexpectedly. This is the **intermediate-axis (tennis-racket) theorem**, also called the Dzhanibekov effect after the cosmonaut who filmed a spinning wing-nut flipping in orbit.

### Radius of gyration

Engineers write $I = Mk^2$, defining the **radius of gyration** $k$ — the single distance at which you could place all the mass to get the same $I$. For a solid disc, $k = R/\sqrt2$; for a hoop, $k = R$.

### A preview of conservation

Because $I$ depends on mass distribution, a spinning body can *change its own $I$* by rearranging its mass — and since angular momentum $L = I\omega$ is conserved when no external torque acts, shrinking $I$ forces $\omega$ up. That is the figure-skater pulling in their arms, and it is the headline of [[Angular Momentum]].

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $I$ | `I` | Moment of inertia about a stated axis |
| $I = \sum m_i r_i^2$ | `I = \sum m_i r_i^2` | Discrete definition |
| $I = \int r^2\,dm$ | `\int r^2 \, dm` | Continuous definition |
| $I = I_{\text{cm}} + Md^2$ | `I_{\text{cm}} + Md^2` | Parallel-axis theorem |
| $I_z = I_x + I_y$ | `I_z = I_x + I_y` | Perpendicular-axis (planar only) |
| $\tfrac12 I\omega^2$ | `\tfrac12 I\omega^2` | Rotational kinetic energy |
| $\tau = I\alpha$ | `\tau = I\alpha` | Newton's 2nd law for rotation |
| $k$ | `k` | Radius of gyration, $I = Mk^2$ |

---
chinese: 电势 (diànshì)
prerequisites:
  - "[[Electric Field]]"
  - "[[Work, Energy and Power]]"
  - "[[Integration]]"
leads_to:
  - "[[X-rays and CT]]"
  - "[[Capacitors]]"
  - "[[Energy Levels and Line Spectra]]"
teach_together:
  - "[[Gravitational Fields]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - syllabus/0625-4-2
  - syllabus/9702-18-5
  - type/deep
  - type/derivation
  - notation/electric-potential-V
  - misconception/zero-potential-means-zero-field
  - misconception/electrons-move-to-lower-potential
---

# Electric Potential 电势

> *An electron microscope has an accelerating-voltage setting. It is an energy dial: an electron accelerated through a suitable 5,000-volt potential difference gains 5,000 electronvolts. The instrument needs more than voltage to make an image, but voltage sets the beam's energy. “Volts” stops being a mysterious electrical label once you ask: how many joules for each coulomb?*

## Definition — the energy map

**Electric potential difference** between positions A and B is the change in electric potential energy per unit test charge:

$$\boxed{V_B-V_A=\frac{U_B-U_A}{q}},\qquad \boxed{\Delta U=q\Delta V}.$$

One **volt** is one joule per coulomb: $1\ \mathrm V=1\ \mathrm{J\,C^{-1}}$. Potential is a **scalar**, including its sign. It has no direction; the field obtained from its spatial variation does.

For a localised source distribution, choose $V=0$ at infinity. Then **potential at a point is the external work done per unit positive test charge in bringing a small charge from infinity to that point, with no change in kinetic energy**. “Small” means it does not appreciably rearrange the source charges. The prescribed potential excludes the test charge's own contribution.

**Intuition:** $\mathbf E$ is the force map; $V$ is the energy-per-charge map. Contour lines on a hiking map tell you height; their spacing tells you steepness. Potential and field have that relationship. But the electrical visitor has a sign: its actual energy landscape is $U=qV$. A negative visitor turns the landscape upside down.

### 中文锚点

同一盏小灯接上不同电压，表现为什么会不一样？电压告诉我们，电荷在两点之间转移时，每一库仑对应多少能量变化。可以借地形来想：两地之间落差大不大，比把哪儿叫作“海拔零米”更要紧。电势像各处标出的高度，电压就是两处的差；把零点换一个地方，不会凭空改变这份能量差。电池的作用，也不是装着一罐“电流”，而是维持能推动能量转移的电势差。

## Notation — keep three quantities apart

| Quantity | Symbol and unit | What it describes |
|---|---|---|
| Electric potential | $V$, volt = J C$^{-1}$ | Energy per charge at a place, relative to a reference |
| Potential energy | $U$ or $E_P$, joule | Energy of the interacting charge system |
| Electric field | $\mathbf E$, N C$^{-1}$ = V m$^{-1}$ | Force per positive charge; direction and magnitude |
| Source / visitor | $Q$ / $q$, coulomb | Signed charges; neither symbol guarantees positivity |
| Coulomb constant | $k=1/(4\pi\varepsilon_0)$ | About $8.99\times10^9$ N m$^2$ C$^{-2}$ in free space |
| Electronvolt | eV | An energy unit, not a voltage unit |

Use $\Delta V=V_{\rm final}-V_{\rm initial}$ consistently. The symbol $V$ sometimes also means a positive supply-voltage magnitude; say which meaning is in use before assigning a sign.

## 1. Who does the work?

For a fixed electrostatic source distribution,

$$\boxed{W_{\rm field}=-\Delta U=-q\Delta V}.$$

If an external agent moves the charge without changing its kinetic energy, the two works cancel:

$$\boxed{W_{\rm external}=\Delta U=q\Delta V}\qquad(\Delta K=0).$$

The general balance is $\Delta K=W_{\rm field}+W_{\rm external}$, hence $W_{\rm external}=\Delta K+\Delta U$. “Work done moving a charge” is incomplete language until the agent and energy change are identified.

For example, slowly move a positive charge toward a positive source. Repulsion opposes the displacement: the field does negative work, you do positive work, and the system stores more energy. Slowly move a negative charge toward that source: attraction does positive work; you must restrain it, doing negative work and removing energy.

**Potential energy belongs to an interaction.** Calling $qV$ “the charge's energy” is convenient shorthand for the charge–source system. If the sources themselves move, account for their kinetic energies too; do not pretend the field was fixed.

## 2. From force to potential — why distance appears only once

For a stationary point source $Q$, [[Electric Field]] gives the radial component $E_r=kQ/r^2$. Along a radial displacement $dr$,

$$dU=-F_r\,dr=-qE_r\,dr,\qquad dV=-E_r\,dr.$$

**Tool: integrate the work from the reference.** With $V(\infty)=0$,

$$V(r)=-\int_\infty^r\frac{kQ}{s^2}\,ds
=\left[\frac{kQ}{s}\right]_\infty^r
=\boxed{\frac{kQ}{r}}.$$

Thus for two point charges,

$$\boxed{U(r)=\frac{kQq}{r}}.$$

The $1/r^2$ force became a $1/r$ energy because energy is an **integral of force over distance**. Conversely, $-dU/dr=kQq/r^2$ restores the signed radial force.

- $Q>0$: potential is positive and approaches zero from above as $r$ increases.
- $Q<0$: potential is negative and approaches zero from below.
- Like-charge pair: $U>0$. Assembling it from infinity costs external work.
- Unlike-charge pair: $U<0$. Assembly releases energy; separating the pair to infinity costs $-U$.

Negative energy does not mean “impossible” or “less than no energy”. It says the chosen zero-energy, infinitely separated state lies **above** the present configuration. The same reference discipline appears in [[Gravitational Fields]].

## 3. Superposition — add values, not arrows

For fixed point sources,

$$\boxed{V(\mathbf r)=k\sum_i\frac{Q_i}{r_i}}.$$

Keep source-charge signs, but every distance $r_i$ is positive. Do **not** resolve potential into horizontal and vertical components. First sum the scalar contributions; take spatial derivatives only if you need the field.

Two equal positive charges at equal distance from a midpoint give $V=2kQ/r$ there, although their fields cancel. An equal positive–negative pair gives $V=0$ at every point on its perpendicular bisector, although the field there generally does **not** vanish.

**Different questions:** $V=0$ asks about the value; $\mathbf E=0$ asks whether the local slope is zero. A road can cross sea level on a steep hill, and it can be flat high in the mountains.

### Assembling three or more charges

Bring $q_1$ from infinity first: there is no other charge yet, so assembly work is zero. Bring $q_2$: work $kq_1q_2/r_{12}$. Bring $q_3$: it interacts with both existing charges. Continuing gives

$$\boxed{U_{\rm system}=\sum_{i<j}\frac{kq_iq_j}{r_{ij}}
=\frac12\sum_i q_iV_{\rm others}(\mathbf r_i)}.$$

Each **pair** is counted once. In the second expression every interaction appears at both ends, hence the half. Do not include a point charge's infinite self-potential. Adding one new charge to fixed sources costs $qV_{\rm existing}$; there is **no half** in that separate problem.

## 4. The slope tells you the force

Over a small displacement,

$$dV=-\mathbf E\cdot d\mathbf r.$$

In one dimension,

$$\boxed{E_x=-\frac{dV}{dx}}.$$

In three dimensions, $\mathbf E=-\nabla V$: each component is minus the derivative in its own coordinate direction. A rising graph means a negative field component; a horizontal graph means that component is zero. **A horizontal tangent along one chosen direction does not prove the entire vector field is zero.**

Between ideal parallel plates at $x=0$ and $x=d$, with potentials $V_0$ and $0$,

$$V(x)=V_0\left(1-\frac{x}{d}\right),\qquad E_x=\frac{V_0}{d}.$$

This is why equal voltage drops occupy equal distances in a uniform field. In a nonuniform field, $-\Delta V/\Delta x$ is an average component over the interval, approaching the local component as the interval shrinks.

![[electric-potential-maps.svg|780]]

*Equipotential contours and field-direction arrows for two fixed source arrangements; arrow lengths are normalised, not a measure of field strength. The left midpoint has zero field but positive potential; the right midpoint has zero potential but nonzero field. Values are dimensionless; the point-source singularities are masked.*

### Equipotentials — motion across a contour versus along it

An **equipotential surface** joins points with the same $V$; its intersection with a page is an equipotential line. Along it, $dV=0$, so the field has no tangential component. Wherever $\mathbf E\ne0$, it is **normal to the surface**, directed toward lower potential.

For equal potential increments, closely spaced contours mean a larger field magnitude: the same change occurs over less distance. Unequal contour increments cannot be compared by spacing alone.

Electric work between two points on the same equipotential is zero. That does not mean there is no force: the field can be perpendicular to a constrained displacement. Nor are equipotentials natural particle tracks; without constraints, the existing velocity and $q\mathbf E/m$ determine motion.

### Conductors: zero field, usually nonzero potential

In electrostatic equilibrium a conductor is equipotential because its internal field is zero. For an isolated spherical conductor of radius $R$, total charge $Q$, and no external sources,

$$V(r)=\begin{cases}kQ/R,&r\le R,\\kQ/r,&r\ge R,\end{cases}
\qquad E_r(r)=\begin{cases}0,&r<R,\\kQ/r^2,&r>R.\end{cases}$$

Potential is continuous at the surface; its derivative jumps because of the surface charge. These relations also hold in the empty cavity of an isolated hollow spherical conductor when there is **no charge in the cavity**. A cavity containing charge requires a different field solution; the surrounding conducting material remains equipotential.

![[electric-potential-sphere.svg|760]]

*Positive isolated conductor. The flat interior potential is not zero: a charge still needs work to be brought there from infinity. Field values at the ideal surface are represented by their inside/outside limits.*

## 5. From voltage to speed

If a test charge moves freely in a fixed electrostatic field and no other force does work,

$$\boxed{\Delta K=-q\Delta V},\qquad
\frac12mv_f^2-\frac12mv_i^2=q(V_i-V_f).$$

Positive charge released from rest initially accelerates toward lower $V$; negative charge toward higher $V$. Both lower **their own $U=qV$**. A moving particle can initially travel the other way, slow down and turn: force determines acceleration, not the instantaneous direction of velocity.

An electron accelerated from rest from $0$ V to $+5000$ V has $q=-e$:

$$\Delta K=-(-e)(5000\ \mathrm V)=5000\ \mathrm{eV}=8.01\times10^{-16}\ \mathrm J.$$

$$1\ \mathrm{eV}=1.602\,176\,634\times10^{-19}\ \mathrm J.$$

The nonrelativistic speed is $\sqrt{2K/m_e}=4.19\times10^7$ m s$^{-1}$. This is an approximation: at 5 keV the relativistic speed is about $4.16\times10^7$ m s$^{-1}$; at much higher accelerating voltages, use $K=(\gamma-1)mc^2$, not $mv^2/2$.

**Turning point:** in a one-dimensional constrained path, the particle reaches a point where $K=K_i-q(V-V_i)=0$. Locations requiring $K<0$ are inaccessible with that initial energy. In unconstrained multidimensional motion, zero velocity in one direction need not mean zero total kinetic energy.

![[electric-potential-landscape.mp4]]

*Externally controlled routes reveal endpoint-dependent electric work. A separate release then shows a positive and a negative test charge accelerating in opposite directions through the same uniform field. The demonstration uses scaled coordinates, not the microscope's numerical settings.*

## Worked examples — follow the energy, then check the sign

### 1. Read the graph — Cambridge 9702/42, February/March 2025, Q2(c)

**Paraphrased setup:** ideal parallel plates have separation $d$ and potentials $V_0$ and zero. Sketch potential against distance from the positive plate.

**Trigger: uniform field. Tool: field is negative potential gradient.** Constant $E_x$ requires a straight graph. The endpoints fix it: $(0,V_0)$ to $(d,0)$. Thus $V(x)=V_0(1-x/d)$ and the slope is $-V_0/d$.

The scheme awards a straight nonhorizontal line, then the correct negative gradient/endpoints. A curved inverse-distance graph would describe a different source geometry. The original paper names the supply magnitude $V$; $V_0$ here keeps that constant distinct from the function $V(x)$.

### 2. A falling electron — AP Physics C E&M 2003, Q1(a)(ii), (c)

**Paraphrased setup:** a fixed spherically symmetric positive charge cloud has total charge $Q$ and radius $R$. An electron starts at rest at radius $r_i>R$. Find its kinetic energy when it reaches the cloud's surface. The full question specifies a nonuniform radial density, but the outside field depends only on total charge.

**Trigger: spherical symmetry outside the source. Tool: point-source potential.** $V_i=kQ/r_i$ and $V_f=kQ/R$.

**Trigger: speed/energy, not travel time. Tool: conservation of energy.**

$$K_f=U_i-U_f=-\frac{keQ}{r_i}+\frac{keQ}{R}
=\boxed{keQ\left(\frac1R-\frac1{r_i}\right)}.$$

This is positive because $r_i>R$. The electron moves toward higher potential while losing potential energy. The published scheme gives this expression. No integration of the trajectory is needed, and no statement about the cloud's *interior* field was needed either.

### 3. A rod makes a logarithm — AP Physics C E&M 2024, Set 1, Q1(d)

**Paraphrased setup:** a uniform positive line charge lies on the $x$-axis from $0$ to $4L$, with charge per length $\lambda$. Find potential at $x>4L$, with zero at infinity, then sketch $E_x$ beyond the rod.

**Trigger: continuously distributed charge. Tool: slice and sum scalar potential.** Name the source coordinate $s$, so a slice has $dq=\lambda\,ds$ and distance $x-s$ from the observation point. Therefore

$$V(x)=k\lambda\int_0^{4L}\frac{ds}{x-s}
=k\lambda[-\ln(x-s)]_0^{4L}
=\boxed{k\lambda\ln\left(\frac{x}{x-4L}\right)}.$$

The logarithm's argument is a dimensionless ratio; writing a lone logarithm of a dimensional distance hides the reference cancellation.

**Trigger: potential known, field requested. Tool: negative derivative.**

$$E_x=-k\lambda\left(\frac1x-\frac1{x-4L}\right)
=\boxed{\frac{4k\lambda L}{x(x-4L)}}.$$

The graph is positive, decreases with $x$, is concave upward, and diverges as $x\to4L^+$ in the ideal zero-radius line model. At large distance, $V\approx k(4\lambda L)/x$ and $E_x\approx k(4\lambda L)/x^2$: the rod looks like its total charge. The published scheme checks the integral, limits and field-graph shape. A physical rod's finite radius limits the endpoint singularity of this idealisation.

### 4. Count interactions once — original assembly example

Three charges occupy the corners of an equilateral triangle of side $a=0.20$ m: $+2$ nC, $+2$ nC and $-1$ nC. Find total electrostatic energy relative to infinite separation.

**Trigger: multiple charges being assembled. Tool: sum distinct pairs.**

$$U=\frac{k}{a}\big[(2)(2)+(2)(-1)+(2)(-1)\big]\times10^{-18}=\boxed{0\ \mathrm J}.$$

The first pair costs $1.80\times10^{-7}$ J to assemble; bringing the third charge to its corner releases exactly that much. Zero total potential energy does **not** mean zero forces or a stable arrangement. In particular, the third charge is attracted toward the midpoint of the positive pair. The charges must be held fixed to preserve the triangle.

## Where it is the working tool

**Electron microscopes.** A cathode–anode potential difference sets the energy gained by each electron. That energy determines momentum and hence the de Broglie wavelength; lenses, beam–sample interaction and detection then determine the image. Raising voltage is not simply “turning up magnification”: it changes penetration and specimen interaction as well. See [JEOL's electron-microscope explanation](https://www.jeol.com/products/science/em.php) and [[Wave-Particle Duality]].

**Particle accelerators.** A static accelerating gap transfers energy according to charge times potential difference. An ion with charge $+2e$ gains twice the energy of a proton across the same accelerating drop. Repeated accelerating gaps require timing and changing fields; a particle cannot gain net energy merely by making repeated loops through one unchanged electrostatic field. [CERN's explanation of direct-voltage accelerators](https://hst-archive.web.cern.ch/archiv/HST2001/accelerators/teachers%20notes/direct.htm).

**The battery on your desk.** Chemical processes separate charge and maintain a terminal potential difference. A 1.5 V drop corresponds to 1.5 J transferred per coulomb, not 1.5 J total and not 1.5 coulombs stored. Total transferred energy also depends on how much charge passes. [[Resistance]] and [[Internal Resistance]] connect that energy accounting to real circuits.

## Hands-on — test whether the route matters

This runnable Python experiment compares two routes from A to B in the field of a fixed point charge. Units are scaled so $kQ=1$. Neither route crosses the singular source.

```python
import numpy as np

def potential(p):
    return 1 / np.linalg.norm(p, axis=-1)

def field(p):
    return p / np.linalg.norm(p, axis=-1)[..., None]**3

t = np.linspace(0, 1, 10001)
straight = np.column_stack((1 + t, np.zeros_like(t)))
detour = np.column_stack((1 + t, 0.8*np.sin(np.pi*t)))
for name, points in [("straight", straight), ("detour", detour)]:
    midpoints = (points[1:] + points[:-1]) / 2
    steps = np.diff(points, axis=0)
    work_per_charge = np.sum(field(midpoints) * steps)
    print(name, work_per_charge,
          potential(points[0]) - potential(points[-1]))
```

Both numerical works per charge approach **0.5**, matching $V_A-V_B$. Change the detour's height: the local force and distance change, but the final integral does not. Double the number of steps and watch the numerical error shrink. Then reverse the route; the work changes sign. Multiplying both results by a negative test charge reverses the sign again.

The path is **externally controlled**, not a simulated free-particle trajectory. Electrostatic path independence holds because the field is conservative. Time-varying magnetic induction is an important boundary, discussed below.

## Common misconceptions

1. **“Potential and potential energy are the same.”** $V$ describes the prescribed sources and position; $qV$ also depends on the visitor. Their units differ.
2. **“Electrons always move downhill in potential.”** Their force points uphill in $V$, downhill in $U=-eV$. Initial velocity can point either way.
3. **“Zero potential means zero field.”** Value and gradient are different; check the two-source maps.
4. **“Moving along an equipotential means no force.”** It means no electric work along that displacement; a perpendicular force can remain.
5. **“Work is always $q\Delta V$.”** That is potential-energy change, or external work when kinetic energy is unchanged. Field work has the opposite sign.
6. **“Potential at infinity is always zero.”** It is a useful convention for localised sources, not a universal boundary condition for infinite ideal sources.
7. **“Use $kQ/r$ inside any charged sphere.”** A conducting sphere's interior potential is constant; an insulating volume-charge distribution generally has a different interior function.
8. **“Total energy is $\sum q_iV_i$.”** If each $V_i$ includes all the other sources, that double-counts pairs. Use the half, and omit self-potentials.

## Exam Notes

### Cambridge 9702 — §18.5, A Level / Paper 4

All four outcomes: potential defined through external work per unit positive charge from infinity; field as the negative potential gradient; $V=Q/(4\pi\varepsilon_0r)$; and two-charge energy $E_P=Qq/(4\pi\varepsilon_0r)$. Use signed charges and positive distances. A sketch needs the correct asymptote, sign and slope, not just a familiar shape.

The inspected March 2025 Paper 42 formula page supplies the point-charge potential and pair-energy formulas. Understanding the definition, sign of work and negative-gradient relation still has to be brought to the problem. The canonical 2028–30 syllabus has the same relevant outcomes as 2025–27.

### Cambridge 0625 — the voltage foundation, §4.2.3

Core defines p.d. as work done per unit charge passing through a component and uses voltmeters; Supplement recalls/uses $V=W/Q$. This supports the opening energy-per-charge interpretation. **Point-charge potential, reference-at-infinity integrals and equipotential-gradient calculations are not 0625 requirements.** Core takes Papers 1/3; Extended takes Papers 2/4, with practical Paper 5 or 6.

### IB Physics — D.2 additional HL, first assessment 2025

Potential and pair energy with zero at infinity; work $q\Delta V$; field/potential-gradient relation; equipotential surfaces and their normal relation to field lines. Include point charges, up to four source charges, solid/hollow conducting spheres and parallel plates. Energies may use joules or electronvolts. The advanced potential treatment is **additional HL**; SL still uses voltage and the uniform-field relation. Distinguish external work from field work even where a booklet writes a bare $W$.

### AP Physics 2 — 10.4–10.5

Pair/system electric energy, scalar potential, energy changes, field maps and equipotentials. Use algebra, signed quantities and physical explanations; the continuous-source calculus below belongs to AP C/enrichment. A zero potential value and zero slope must not be conflated.

### AP Physics C: Electricity and Magnetism — Unit 9

9.1 covers pairwise assembly energy; 9.2 covers potential, source sums/integrals and the field-gradient relation; 9.3 applies conservation of electric energy. The named calculus source geometries are infinite wire/cylinder, ring axis, circular arc at its centre, and a finite line along its axis or perpendicular bisector. Their derivations are below and in Example 3. Conductors/equipotential interiors also connect to 10.1; full induced-charge configurations remain a separate extension.

### Where it is not examined

The current AP Physics 1 and AP Physics C: Mechanics courses do not examine electric potential. Cambridge maths 0580/0606/9709/9231 supply tools but do not name electrostatic potential as a physics topic. The shared mathematics of work and gradients is still useful across those courses.

## Beyond the point source — calculus and the limits of the landscape

### One integral, several geometries

Recall that scalar contributions add: $dV=k\,dq/r$. For a finite charge distribution with zero at infinity,

$$\boxed{V=k\int\frac{dq}{r}}.$$

**Ring and circular arc.** A ring of radius $a$, total charge $Q$, has every element the same distance $\sqrt{a^2+z^2}$ from an axial point. Pull that factor out:

$$V(z)=\frac{kQ}{\sqrt{a^2+z^2}},\qquad E_z=-\frac{dV}{dz}=\frac{kQz}{(a^2+z^2)^{3/2}}.$$

At the centre $V=kQ/a$ but $E_z=0$; the complete uniform ring also has zero transverse field by symmetry. At the centre of an arc of radius $a$, the same constant-distance argument gives $V=kQ/a=k\lambda\theta$ for uniform linear density and angle $\theta$ in radians. The arc's field need not vanish: scalar simplicity does not imply vector cancellation.

**Finite line, perpendicular bisector.** A uniform rod from $s=-a$ to $a$ is observed a perpendicular distance $y>0$ from its midpoint:

$$V(y)=k\lambda\int_{-a}^{a}\frac{ds}{\sqrt{s^2+y^2}}
=\boxed{2k\lambda\,\operatorname{arsinh}(a/y)}
=2k\lambda\ln\left(\frac{a+\sqrt{a^2+y^2}}y\right).$$

Differentiate: $E_y=2k\lambda a/[y\sqrt{a^2+y^2}]$, agreeing with the direct field integral in [[Electric Field]]. Example 3 supplies the complementary collinear geometry. Far away both potentials approach the total-charge result $kQ/r$.

### An infinite wire cannot use zero at infinity

Recall that [[Electric Field]] derives $E_r=\lambda/(2\pi\varepsilon_0r)$ for an infinite uniform line. Between two finite radii,

$$V(r)-V(r_0)=-\int_{r_0}^r E_r\,dr
=\boxed{-\frac{\lambda}{2\pi\varepsilon_0}\ln\left(\frac r{r_0}\right)}.$$

As $r\to\infty$ the logarithm diverges; no finite constant makes $V(\infty)=0$. Choose a finite reference $r_0$. The ideal infinite charged cylinder has the same external formula using its charge per length. For a conducting cylinder, potential is constant inside the conducting material; for a uniformly charged solid insulating cylinder, it is not.

For that insulating cylinder of radius $R$ and volume density $\rho$, cylindrical Gauss symmetry gives $E_r(2\pi r\ell)=\rho\pi r^2\ell/\varepsilon_0$, so $E_r=\rho r/(2\varepsilon_0)$ inside. Integrating inward from its surface gives

$$V(r)-V(R)=\frac{\rho}{4\varepsilon_0}(R^2-r^2),\qquad r<R.$$

The exterior uses $\lambda=\rho\pi R^2$ and the same finite reference. Infinite uniform planes likewise cannot use the isolated-point-charge infinity convention: their constant field accumulates an unbounded potential change.

### Why changing the zero is harmless — and when scalar potential is not enough

Recall that forces depend on the gradient. Replacing $V$ by $V+C$ leaves $\mathbf E=-\nabla V$ unchanged; all potential differences stay the same. For a fixed test charge, every energy shifts by the same $qC$, so predictions are unchanged. This is the simplest example of **gauge freedom**: different descriptions, the same observable differences.

The electrostatic route-independence rule is $\oint\mathbf E\cdot d\mathbf r=0$. A changing magnetic flux instead gives $\oint\mathbf E\cdot d\mathbf r=-d\Phi_B/dt$; a single-valued scalar potential alone cannot describe that entire electric field. [[Electromagnetic Induction]] supplies the physical case. In general electromagnetism, $\mathbf E=-\nabla V-\partial\mathbf A/\partial t$, with $\mathbf A$ the magnetic vector potential. The electrostatic landscape is powerful precisely because its assumptions remove that extra term.

## Connections

- **Imaging application:** [[X-rays and CT]] — electron acceleration, photon energies and attenuation become an internal image.

- **Prerequisites:** [[Electric Field]] — Coulomb sources, vector fields and the finite-line/infinite-line derivations; [[Work, Energy and Power]] — work and conservation; [[Integration]] — adding infinitesimal contributions.
- **Analogy:** [[Gravitational Fields]] — the same reference-at-infinity discipline, with attractive gravity's fixed sign.
- **Applications:** [[Capacitors]] — stored energy when the source charge itself grows; [[Energy Levels and Line Spectra]] — the negative Coulomb energy in a bound atom; [[Wave-Particle Duality]] — beam energy, momentum and wavelength.
- **Circuit bridge:** [[Resistance]], [[Internal Resistance]] — terminal voltage and energy transfer per charge.
- **Boundary of the model:** [[Electromagnetic Induction]] — electric fields whose work around a loop need not vanish.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $\Delta U=q\Delta V$ | `\Delta U=q\Delta V` | Potential-energy change |
| $V=kQ/r$ | `V=kQ/r` | Point-source potential, zero at infinity |
| $E_x=-dV/dx$ | `E_x=-dV/dx` | Negative spatial slope |
| $\Delta V=-\int_A^B\mathbf E\cdot d\mathbf r$ | `\Delta V=-\int_A^B\mathbf E\cdot d\mathbf r` | Potential difference from field |
| $U=\sum_{i<j}kq_iq_j/r_{ij}$ | `U=\sum_{i<j}kq_iq_j/r_{ij}` | Count every pair once |
| $V=k\int dq/r$ | `V=k\int dq/r` | Continuous finite source |

---
chinese: 电场 (diànchǎng)
aliases:
  - Coulomb's Law
prerequisites:
  - "[[Electric Current]]"
  - "[[Vectors]]"
  - "[[Newton's Laws of Motion]]"
leads_to:
  - "[[Electric Potential]]"
  - "[[Capacitors]]"
  - "[[Lorentz Force]]"
  - "[[Maxwell's Equations]]"
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
  - syllabus/9702-18-1
  - syllabus/9702-18-2
  - syllabus/9702-18-3
  - syllabus/9702-18-4
  - type/deep
  - type/derivation
  - notation/electric-field-E
  - misconception/field-lines-are-trajectories
  - misconception/zero-field-means-no-charges
  - misconception/attraction-proves-opposite-charge
---

# Electric Field 电场

> *A laser printer does not spray black ink at the right places. It arranges electric forces so that charged powder goes where the image needs it. Before there is a visible letter, there is an invisible pattern of pushes and pulls. An electric field is that pattern made measurable.*

## Definition — separate the place from the visitor

An **electric field** is a region in which an electric charge experiences an electric force. More precisely, **electric field strength** at a point is the electric force per unit positive test charge:

$$\boxed{\mathbf E=\frac{\mathbf F_{\mathrm e}}q},\qquad \boxed{\mathbf F_{\mathrm e}=q\mathbf E}.$$

The test charge is small enough not to appreciably rearrange the source charges. The field is the **external** field acting on it: do not include the test charge's own field when finding its force. Units: **newtons per coulomb**, $\mathrm{N\,C^{-1}}$, equivalently **volts per metre**, $\mathrm{V\,m^{-1}}$.

**Intuition.** Imagine placing the same tiny positive charge at many locations and recording an arrow at each one. That arrow map is $\mathbf E$. Remove the visitor and the source's field remains. Double the visitor's charge: its force doubles, but the field did not. Replace it with a negative charge: the force reverses, but the field still did not.

Gravity has the same separation: $\mathbf g=\mathbf F_g/m$ describes the place, while $\mathbf F_g=m\mathbf g$ describes a particular visitor. Electricity adds a second sign: a negative charge accelerates **against** $\mathbf E$.

### 中文锚点

塑料尺摩擦后，隔着一点距离也能吸起小纸屑：没有碰到，力却已经起作用了。电场就是描述这种作用的一种办法——在空间的不同位置，放上一点正电荷，它会往哪边受力、受力有多强？换成负电荷，受力方向就反过来。激光打印机把这种看不见的作用控制得很细，让带电碳粉落到该落的位置，最后变成纸上的字。

## Notation

| Symbol | Meaning | Watch the distinction |
|---|---|---|
| $Q$, $q$ | source charge; test charge, in C | Both may be signed; $Q$ is not automatically positive |
| $\mathbf E$, $E$ | field vector; its magnitude | Magnitude is nonnegative; a component can be negative |
| $k=1/(4\pi\varepsilon_0)$ | Coulomb constant, about $8.99\times10^9\ \mathrm{N\,m^2\,C^{-2}}$ | Free space; air is often an adequate approximation |
| $r$, $\hat{\mathbf r}$ | source-to-observation distance and unit vector | Measure from the source, not from the page's origin |
| $\Delta V$, $d$ | potential difference; plate separation | $E=\lvert\Delta V\rvert/d$ is a **uniform-field** magnitude relation |

## 1. Charge first — what actually moves?

Protons have charge $+e$, electrons $-e$, where $e=1.602\,176\,634\times10^{-19}$ C. Ordinary isolated objects acquire net charges in integer multiples of $e$: gaining electrons makes them negative; losing electrons makes them positive. In ordinary charging of solids, electrons transfer while nuclei stay bound in the material. **Charge is conserved:** friction separates/transfers it; it does not manufacture it. [[Electric Current]] follows charge once it flows continuously.

- **Friction:** rub an insulating rod with a cloth. Electrons transfer between the materials; they acquire opposite net charges. The sign depends on the material pair, not on “rubbing” alone.
- **Contact:** a charged conductor touches another conductor; mobile electrons redistribute. Equal identical isolated spheres share total charge equally when connected and sufficiently far from other influences. Unequal shapes need not share equal charge.
- **Induction:** bring a negative rod near an initially neutral metal sphere on an insulating stand. Electrons move to the far side, leaving the near side electron-deficient; the sphere is still neutral. With the rod held in place, ground the sphere: electrons can leave for Earth. **Disconnect Earth first, then remove the rod.** The sphere remains positive. Reversing that order lets electrons return before isolation.

**Conductor versus insulator.** Metals have mobile electrons that can travel through the bulk; in glass, plastic and rubber, charges are much less free to move macroscopically. An insulator can still **polarise**: its positive and negative charge distributions shift slightly relative to each other without flowing across the entire object.

### Three small experiments, three different claims

1. Suspend a light charged insulating rod by an insulating thread. Bring a second similarly charged rod near it: **repulsion** shows like charge. A neutral scrap of paper can be attracted through polarisation, so attraction alone does not establish opposite net charge.
2. Touch a rubbed rod to an electroscope's metal cap. Charge spreads to its stem and leaf; their like charges repel, opening the leaf. A nearby rod can also open it by induction without transferring charge. Use a known initial charge and controlled contact/proximity to distinguish the claims; a deflection alone does not reveal sign.
3. Connect a charged electroscope to Earth through the sample being tested, controlling length/contact and avoiding a parallel path through your hand. A metal wire discharges it readily; a dry plastic strip does not on the same timescale. This tests charge mobility, not whether the sample contains electrons—both do.

Use rubbed rods/balloons for classroom electrostatics, not mains-powered improvised high-voltage supplies. Humidity and dirty insulating supports can leak charge and change the result.

## 2. Coulomb's law — the source of the map

Two stationary point charges in free space exert equal and opposite forces along their joining line. The magnitude is

$$\boxed{F=k\frac{\lvert Qq\rvert}{r^2}}.$$

Like signs repel; unlike signs attract. Double one charge and the force doubles. Double both and it quadruples. Double separation and it falls to a quarter. The force pair has equal magnitude even if the charges or masses differ; the **accelerations** need not be equal.

This is an **experimental law**, not a consequence of the definition of charge. The inverse square is geometrically consistent with the same outward flux spreading over spheres of area $4\pi r^2$; [[Maxwell's Equations]] makes that statement precise through Gauss's law. That explanation connects equivalent field laws; it is not an independent experimental proof of Coulomb's law.

Dividing the force on a small positive visitor by its charge gives the field of a point source:

$$\boxed{\mathbf E(\mathbf r)=k\frac{Q}{r^2}\hat{\mathbf r}}.$$

The sign now matters directly. For $Q>0$, the arrow points away from the source; for $Q<0$, toward it. **$E=k\lvert Q\rvert/r^2$ is the magnitude.** In vector calculations use the signed source charge once, not once in the formula and again in a direction correction.

A **point charge** is a model: size is negligible compared with the separations of interest. An isolated charged spherical conductor also has exactly the point-charge field **outside** it by spherical symmetry. Nearby external charges can redistribute its surface charge and destroy that symmetry; “it is a sphere” alone is not enough.

In a homogeneous linear dielectric, the corresponding idealised interaction uses $\varepsilon=\varepsilon_r\varepsilon_0$ in place of $\varepsilon_0$. Bound-charge polarisation changes the field; larger permittivity reduces it for the same free charges in that model. Real boundaries and nonuniform materials require solving the actual geometry, not blindly substituting a number.

## 3. Superposition — add arrows, not distances

For fixed source charges $Q_i$ at positions $\mathbf r_i$, the field at $\mathbf r$ is

$$\boxed{\mathbf E(\mathbf r)=k\sum_i Q_i\frac{\mathbf r-\mathbf r_i}{\lvert\mathbf r-\mathbf r_i\rvert^3}}.$$

Why the cube? The denominator supplies $r^2$ from Coulomb's law and another $r$ to turn the displacement vector into a unit vector. Its magnitude is still inverse-square.

**Procedure:** choose the observation point → draw each source's field **there** → resolve into common axes → add components → multiply by the visitor's signed $q$ only if a force is wanted. Never add the field at one location to a field evaluated somewhere else.

Two equal positive sources cancel at their midpoint. An equal positive/negative pair does **not**: between them, “away from positive” and “toward negative” point the same way. A zero field means the contributions cancel; it does not mean there are no charges or that the potential is zero.

![[electric-field-patterns.svg|760]]

*Numerically computed field directions; streamline density here is illustrative, not a quantitative field-strength scale. The arrows show the resultant, not separate imaginary streams of charge. The uncharged observation point does not create these patterns.*

## 4. Reading field lines — a map, not rails

A field line is drawn so its tangent points along the force on a **positive** test charge. Lines leave positive sources and enter negative sources, or extend to/from infinity. Draw arrows; a line without direction omits half the information.

- Lines closer together indicate a stronger field when the drawing uses a consistent line-count convention. The number of strokes on the page is a representation choice, not a physical observable.
- Lines cannot cross at an ordinary point with nonzero field: crossing would assign two directions to one vector. At a null point, field direction is undefined.
- A point source has a radial pattern. An isolated charged sphere has the same external pattern; the field meets its conducting surface normally.
- Parallel plates have approximately straight, parallel, equally spaced lines well inside the gap. At the edges they curve outward: **fringing**. The uniform approximation is strongest when the gap is small compared with plate dimensions and the observation point is far from an edge.

**Inside conducting material in electrostatic equilibrium, $\mathbf E=0$.** Otherwise free charges would keep accelerating/rearranging, contradicting equilibrium. Excess charge resides on surfaces; the tangential surface field vanishes for the same reason. A closed empty cavity in a conductor, with no charge inside it, is also field-free in electrostatic equilibrium. This does not say every point inside the outer outline is field-free when there is a charge in a cavity. An insulator can retain excess charge throughout its bulk as well as on its surface; its interior field need not vanish.

An equilibrium conductor is also **equipotential**: moving between points within it requires no electric work because $\mathbf E=0$, so their potential difference is zero.

A conductor carrying a steady current is a different situation: an internal electric field can drive that current. “Inside metal, the field is always zero” drops the load-bearing words **electrostatic equilibrium**.

## 5. Uniform fields — energy gives the field strength

Voltage is energy transfer per unit charge. Move a positive test charge a distance $d$ **along** a uniform field: the field does work $W=qEd$. Its electric potential energy decreases by the same amount, so the potential drops by $Ed$:

$$\Delta V=-Ed,\qquad \boxed{E=\frac{\lvert\Delta V\rvert}{d}}.$$

The field points from higher to lower potential. The signed one-dimensional relation is $E_x=-dV/dx$; the plates' linear potential graph is the special case with constant slope. [[Electric Potential]] develops energy and potential for nonuniform fields; $V/r$ is not a general replacement for that derivative.

![[electric-field-motion.svg|760]]

*Uniform downward field; a negative particle enters to the right. Its acceleration is upward. Equal-time positions become progressively farther apart because its speed grows.*

If the electric force is the only significant force,

$$a_x=\frac{qE_x}{m},\qquad a_y=\frac{qE_y}{m}.$$

For entry with horizontal speed $u$ and $E_x=0$, constant $E_y$:

$$x=ut,\qquad y=\frac{qE_y}{2m}t^2,\qquad \boxed{y=\frac{qE_y}{2mu^2}x^2}.$$

It is [[Projectile Motion]] with $qE_y/m$ taking the role of the vertical acceleration. The same fixed horizontal speed sets the time available for deflection. A particle released from rest in a uniform field moves along a straight field direction (opposite it if negative); sideways entry produces the parabola. In a nonuniform field even a particle initially at rest need not continue following a field line, because it acquires inertia while the local field turns.

![[electric-field-motion.mp4]]

*Three distinctions: add source fields at one point; reverse the visitor's charge without reversing the field; then watch a trajectory curve across straight field lines. The animation uses dimensionless coordinates, not the numerical values of Example 3.*

## Worked examples — choose the tool from the situation

### 1. A model atom — Cambridge 9702/41, May/June 2025, Q2(b), (d)

**Paraphrased setup:** a helium nucleus has two protons. Two electrons lie on opposite sides, each $170$ pm from the nucleus. Find the nucleus–electron force and compare the electric fields at one electron due to the other electron and the nucleus.

**Trigger: two protons. Tool: add charges.** $Q=+2e$; the two neutrons add mass but no charge.

**Trigger: a source and visitor separated by a known distance. Tool: Coulomb's law.** With $r=170\times10^{-12}$ m,

$$F=\frac{k(2e)e}{r^2}=1.60\times10^{-8}\ \mathrm N,$$

attractive, toward the nucleus.

**Trigger: comparing two fields at the same point. Tool: inverse-square scaling before substitution.** The other electron is $2r$ away, with source magnitude $e$ rather than $2e$:

$$\frac{E_{\text{other electron}}}{E_{\text{nucleus}}}=\frac{ke/(2r)^2}{k(2e)/r^2}=\boxed{\frac18}.$$

The two **fields** oppose at the observation point. Multiplying by the negative electron charge reverses both forces: nuclear attraction is inward; electron–electron repulsion is outward. The repulsion reduces the inward resultant. Under the question's circular-orbit model, at fixed radius the required speed is therefore smaller than the nucleus-only value. This is a deliberately classical model, not a literal account of electrons in quantum helium; [[Energy Levels and Line Spectra]] supplies the crucial quantum distinction.

### 2. A charged pendulum — AP Physics C E&M 2023, Set 1, Q1(a)–(c)

**Paraphrased setup:** a sphere of charge $+Q$, mass $M$, hangs at angle $\theta$ from vertical. Another charge $+q$ is at the same height, distance $d$ away. Both small spheres are modelled by their charges at their centres. Determine the equilibrium relation and the string tension for $Q=q=6.0\times10^{-8}$ C, $d=0.057$ m, $\theta=12^\circ$.

**Trigger: equilibrium. Tool: separate force balances.** Three forces act: weight down, electric repulsion horizontally away from the other sphere, and tension along the string toward its support. Components are not extra forces.

$$T\cos\theta=Mg,\qquad T\sin\theta=\frac{kQq}{d^2}.$$

**Trigger: eliminate an unwanted tension. Tool: divide the equations.**

$$\tan\theta=\frac{kQq}{Mgd^2},\qquad \boxed{d=\sqrt{\frac{Qq}{4\pi\varepsilon_0Mg\tan\theta}}}.$$

**Trigger: horizontal force and angle known. Tool: horizontal balance.**

$$T=\frac{kQq}{d^2\sin\theta}=0.0479\ \mathrm N\approx\boxed{0.048\ \mathrm N}.$$

The source's scoring guidelines give $0.048$ N. Their full question then turns the relation into a graph experiment and asks how a conducting replacement redistributes charge—a reminder that the point-charge model has conditions.

### 3. Electron between plates — original numerical transfer

An electron enters halfway between horizontal plates at $u=2.0\times10^7$ m s$^{-1}$. The upper plate is positive, the lower negative; separation $d=0.020$ m, potential difference $200$ V, plate length $L=0.040$ m. Neglect gravity, fringing and relativistic corrections; use $m_e=9.11\times10^{-31}$ kg.

**Trigger: parallel plates. Tool: uniform-field magnitude.** $E=200/0.020=1.0\times10^4$ N C$^{-1}$, **down**. The electron's force is **up**.

**Trigger: constant force. Tool: Newton's second law.** $a_y=eE/m_e=1.76\times10^{15}$ m s$^{-2}$ upward.

**Trigger: no horizontal force. Tool: constant horizontal speed.** Time in the plates is $t=L/u=2.0\times10^{-9}$ s. Thus

$$y=\tfrac12a_yt^2=3.52\times10^{-3}\ \mathrm m=\boxed{3.52\ \mathrm{mm}}.$$

**Check the model:** this is less than the $10$ mm gap to the upper plate, so it exits without striking it. $v_y=a_yt=3.52\times10^6$ m s$^{-1}$; after exiting the idealised field, it follows a straight tangent, not a continuing parabola. Its final speed is about $0.068c$, so the nonrelativistic approximation is reasonable here.

### 4. Find a null — original superposition check

Place $+4$ nC at $x=0$ and $+1$ nC at $x=0.30$ m. Where does the field vanish?

**Trigger: cancellation requires opposing arrows. Tool: direction first.** Outside the interval both fields point the same way; between the charges they oppose. For $0<x<0.30$,

$$\frac{k(4\times10^{-9})}{x^2}=\frac{k(1\times10^{-9})}{(0.30-x)^2}.$$

**Tool: positive distances.** $2/x=1/(0.30-x)$, giving $x=0.20$ m. The null lies nearer the weaker charge. Each individual field is about $899$ N C$^{-1}$ there, with opposite directions; zero resultant does not mean zero contributions.

## Where it is the working tool

**The printer builds a force map.** A photoconductive drum or belt is charged; illumination changes its local conductivity and creates a spatial charge/potential pattern. That field exerts forces on charged toner particles, developing a visible image. Electrostatic transfer moves toner to paper; heat/pressure then fuse it. Exact charge signs and illuminated-versus-unilluminated image regions depend on the design. The common working principle is $\mathbf F=q\mathbf E$, not “the laser burns the letters into the paper”. [Xerox's explanation of xerography](https://www.xerox.com/da-dk/innovation/indsigt/chester-carlson-xerography).

**Collecting smoke particles.** An electrostatic precipitator charges suspended particles and uses a field to move them toward collecting electrodes. Gas flows onward while particles drift sideways. Particle charge, drag and the local field matter together; a free-electron vacuum parabola would be the wrong model for a particle moving through air.

**Why a balloon sticks to a neutral wall.** The balloon's field polarises the wall. Opposite charge is slightly nearer the balloon than like charge; because the field is nonuniform, the attractions need not cancel the repulsions. No net charge on the wall is required. “Neutral” is a total-charge statement, not a promise that every small region stays neutral.

## Hands-on — make a field null, then destroy it

Use this runnable NumPy calculation, also developed in `electric-field-verify.py` beside the figures:

```python
import numpy as np
k = 8.9875517923e9
sources = [(4e-9, np.array([0., 0.])),
           (1e-9, np.array([0.30, 0.]))]
def field(point):
    result = np.zeros(2)
    for charge, position in sources:
        delta = np.asarray(point) - position
        distance = np.linalg.norm(delta)
        if distance == 0:
            raise ValueError("Point-source field is undefined at the source")
        result += k * charge * delta / distance**3
    return result
print(field([0.20, 0.]))
print(field([0.20, 0.01]))
```

**Predict before running:** is the second field still zero? Which way should its vertical component point? Then change the smaller source to $-1$ nC: explain why cancellation can no longer occur **between** the sources, and locate it elsewhere. Finally compare the two source forces in magnitude and direction for unequal charges; Newton's third law survives the asymmetry.

## Common misconceptions

1. **“A bigger test charge makes a bigger field.”** It makes a bigger force in a prescribed external field. A large visitor can disturb conductors; that invalidates the small-test-charge approximation rather than the definition.
2. **“Negative charge means negative field strength.”** Field is a vector. State a direction or a signed component; its magnitude is nonnegative.
3. **“Field lines are particle tracks.”** Lines specify local force direction for a positive visitor. Motion additionally depends on the sign, mass and existing velocity.
4. **“Attraction proves opposite charges.”** A charged object can attract a neutral polarised object. Controlled repulsion is the cleaner charge test.
5. **“Every sphere acts as a point charge.”** Exact external equivalence needs spherical symmetry; nearby sources can redistribute charge on a conductor.
6. **“Zero field means zero potential.”** Forces can cancel while scalar potentials add. Between equal positive charges the midpoint is the simplest warning.
7. **“Use $E=V/d$ wherever a distance is given.”** It is the uniform-field potential-drop relation. A general field requires a potential gradient or a source-field calculation.

## Exam Notes

### Cambridge 9702 — Topic 18, A Level / Paper 4

**§18.1–18.4:** define field strength per unit positive charge, use $F=qE$, represent fields, use $E=\Delta V/\Delta d$ between parallel plates, describe charged-particle motion, apply Coulomb's law and the spherical-conductor model, and derive/use the point-charge field. Include direction and the distinction between source and test charges. Coulomb's law statements need charge-product proportionality, inverse-square separation and the point-charge/free-space setting.

**§18.5 remains a distinct energy/potential treatment.** The uniform-field derivation above is a bridge, not full coverage of potential referenced to infinity, point-charge potential and pair energy. The 2028–30 syllabus retains the same relevant learning outcomes as 2025–27.

### Cambridge 0625 — §4.2.1, Core and Supplement

**Core:** signs, attraction/repulsion, friction and charge detection, electron transfer, conductor/insulator test and electron model with examples. **Supplement:** coulomb as the charge unit, field as a region of force, direction defined by positive charge, and patterns around point charges, charged conducting spheres and opposite parallel plates. **End effects are explicitly not examined.** The algebraic Coulomb-law and particle-parabola calculations go beyond these IGCSE requirements.

### IB Physics — D.2 and D.3, first assessment 2025

**SL and HL D.2:** charge conservation/quantisation, friction/contact/induction/grounding, Coulomb's law, $E=F/q$, $E=V/d$ and field patterns. The guide includes conductor interiors and **plate edge effects**, unlike 0625. Permittivity variations are included. **Millikan's experiment is required evidence for quantisation**: a suspended drop balances electric force against its effective weight; repeating the charge measurement yields multiples of $e$. A full experimental treatment remains additional to the charging introduction above.

**D.3 SL/HL:** uniform-electric-field particle motion belongs with uniform-magnetic and crossed-field motion in [[Lorentz Force]]. **D.2 additional HL:** potential, equipotentials and energy belong with [[Electric Potential]]; there is no additional-HL block in D.3.

### AP Physics 2 — Unit 10, current course framework

**10.1–10.3:** electric force, charge conservation/charging and fields. Use vector superposition and explanations of polarisation; apply forces and energy to physical situations. Continuous-charge field derivation by calculus is not the AP-2 route. **10.4–10.5** energy/potential are adjacent, not completed merely by writing $E=V/d$.

### AP Physics C: Electricity and Magnetism — Units 8–10

**8.1–8.3:** Coulomb force, charging and vector fields; the force-calculation boundary is four or fewer interacting charged objects except high-symmetry cases. **8.4** extends to continuous distributions; the calculus below is an introduction, not every assessed geometry. **8.5–8.6** require flux and Gauss-law applications. **10.1** includes conductors/electrostatic equilibrium; charge redistribution and capacitors extend the story. The pendulum example shows why a field question can also be a mechanics experiment.

### Where it is not examined

The current **AP Physics 1** and **AP Physics C: Mechanics** frameworks do not examine electrostatics. Cambridge maths **0580, 0606, 9709 and 9231** supply useful vectors/calculus/mechanics but do not make electric fields a named physics topic. None of this exclusion removes the value of transferring their mathematical tools.

## Beyond syllabus / calculus bridge — from many charges to a continuous source

### A line is the same sum with smaller pieces

Recall that superposition adds each source's vector contribution. For continuously distributed charge,

$$\mathbf E(\mathbf r)=k\int\frac{\mathbf r-\mathbf r'}{\lvert\mathbf r-\mathbf r'\rvert^3}\,dq,\qquad dq=\lambda\,dl,\ \sigma\,dA,\ \rho\,d\mathcal V.$$

Here $\lambda$, $\sigma$ and $\rho$ are charge per length, area and volume. They describe different physical distributions; they are not interchangeable constants.

Take a uniform line from $x=-a$ to $a$, linear density $\lambda$, and an observation point $(0,y)$ with $y>0$. Symmetric pieces cancel horizontally; vertically, a piece contributes the Coulomb field times $y/\sqrt{x^2+y^2}$. Thus

$$E_y=k\lambda\int_{-a}^{a}\frac{y\,dx}{(x^2+y^2)^{3/2}}=\boxed{\frac{2k\lambda a}{y\sqrt{a^2+y^2}}}.$$

The antiderivative is $x/[y\sqrt{x^2+y^2}]$. Two checks teach more than memorising the result: far away ($y\gg a$), it becomes $k(2a\lambda)/y^2$, the field of the total point charge; for a very long line ($a\gg y$), it becomes $2k\lambda/y$, inverse-distance rather than inverse-square. Geometry changes how the field spreads.

### Gauss's law — when symmetry does the integral for you

Recall that electric flux through an oriented area counts the normal component: $d\Phi_E=\mathbf E\cdot d\mathbf A$. Through a flat patch in a uniform field, $\Phi_E=EA\cos\theta$, with $\theta$ measured from the **area normal**. For a closed surface,

$$\oint\mathbf E\cdot d\mathbf A=\frac{Q_{\rm enclosed}}{\varepsilon_0}.$$

External charges contribute to local $\mathbf E$ but zero **net** closed-surface flux. Zero enclosed charge therefore does not imply zero field. [[Maxwell's Equations]] derives the isolated sphere's external field with a spherical surface. Two other symmetries give useful new results:

- **Infinite uniform line:** a coaxial cylinder of radius $r$, length $L$ has curved area $2\pi rL$. Its end caps have zero flux because the field is tangent there. $E(2\pi rL)=\lambda L/\varepsilon_0$, so $E=\lambda/(2\pi\varepsilon_0r)$.
- **Infinite uniform sheet:** a pillbox has flux $2EA$ through its two faces; its thin sides carry none. $2EA=\sigma A/\varepsilon_0$, so each side has $E=\sigma/(2\varepsilon_0)$. Superpose opposite sheets: fields add between them to $\sigma/\varepsilon_0$ and cancel outside. Finite plates only approximate this result away from edges.

Symmetry is the trigger. Without constant field magnitude and a known direction on the chosen surface, Gauss's law remains true but does not by itself solve for $E$.

### A dipole feels a turning demand

Recall that opposite charges experience opposite forces in a uniform field. For $+q$ and $-q$ separated by vector $\mathbf d$ pointing from negative to positive, define the dipole moment $\mathbf p=q\mathbf d$. The net force is zero, but the separated forces make a couple: $\boldsymbol\tau=\mathbf p\times\mathbf E$. A polar molecule can rotate toward alignment without acquiring a net translational force. In a nonuniform field the two forces need not cancel—one mechanism behind the balloon-and-wall attraction.

## Connections

- **Charge and flow:** [[Electric Current]] — conservation, quantisation and charge transport.
- **Mathematical tools:** [[Vectors]], [[Integration]], [[Newton's Laws of Motion]], [[Projectile Motion]].
- **Same field grammar:** [[Gravitational Fields]] — inverse-square sources and force per unit visitor-property; electricity adds attraction and repulsion.
- **Next layer:** [[Electric Potential]] — scalar energy bookkeeping; [[Capacitors]] — storing energy through separated charge.
- **Moving charges:** [[Lorentz Force]] — magnetic and crossed-field motion; [[Maxwell's Equations]] — flux, sources and changing fields.
- **History:** [[Franklin's Coin Flip]] — how the sign convention got its historical accident; [[A Rich Neighbor Named Xerox]] — the company whose name became the act of copying.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\mathbf E=\mathbf F/q$ | `\mathbf E=\mathbf F/q` | External field per unit signed test charge |
| $kQ\hat{\mathbf r}/r^2$ | `kQ\hat{\mathbf r}/r^2` | Point-source field |
| $\sum_i\mathbf E_i$ | `\sum_i\mathbf E_i` | Vector superposition |
| $E=\lvert\Delta V\rvert/d$ | `E=\lvert\Delta V\rvert/d` | Uniform-field magnitude |
| $\oint\mathbf E\cdot d\mathbf A$ | `\oint\mathbf E\cdot d\mathbf A` | Outward electric flux |
| $\mathbf p=q\mathbf d$ | `\mathbf p=q\mathbf d` | Electric dipole moment |

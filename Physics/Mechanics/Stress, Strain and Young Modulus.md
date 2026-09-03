---
chinese: 应力、应变与杨氏模量 (yìnglì, yìngbiàn yǔ Yáng shì mókuàng)
prerequisites:
  - "[[Hooke's Law for Springs]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Forces and Equilibrium]]"
  - "[[Work, Energy and Power]]"
  - "[[Differentiation]]"
leads_to:
  - "[[Beam Bending]]"
  - "[[Material Failure]]"
  - "[[Composite Materials]]"
  - "[[Waves I: The Wave Equation]]"
  - "[[Elastic Strings and Springs]]"
tags:
  - subject/physics
  - subject/materials-science
  - domain/mechanics
  - domain/elasticity
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-6-1
  - syllabus/IB-Physics-A-2-2
  - syllabus/AP-Physics-1-2-8
  - syllabus/AP-Physics-C-Mech-2-8
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/sigma-stress
  - notation/epsilon-strain
  - notation/Young-modulus-E
  - notation/Pascal-Pa
  - misconception/stress-equals-force
  - misconception/strain-has-units
  - misconception/k-is-a-material-property
  - misconception/elastic-limit-equals-yield-equals-ultimate
---

# Stress, Strain and Young Modulus 应力、应变与杨氏模量

## Definition

Three quantities, one equation that ties them together:

$$\boxed{\; \sigma = E\,\varepsilon \;}$$

The letters:

- $\sigma$ — **stress** (yìnglì 应力): force per unit cross-sectional area, $\sigma = F/A$. Units: pascals ($\text{Pa} = \text{N m}^{-2}$). Typically megapascals or gigapascals for engineering materials.
- $\varepsilon$ — **strain** (yìngbiàn 应变): fractional change in length, $\varepsilon = \Delta L / L_0$. **Dimensionless** — a pure number, in the same sense as the radian is a pure number (arc-length over radius — see [[Radians]] §"The deepest reason — degree is a unit, radian is a pure number"). Often expressed as a percentage or in parts per thousand.
- $E$ — **Young modulus** (Yáng shì mókuàng 杨氏模量): the stiffness of the *material*. Units: pascals (same as stress, because strain is dimensionless). Typically 10²–10³ GPa for metals.

The equation $\sigma = E\varepsilon$ is **Hooke's Law re-expressed at the level of the material**, with the geometry stripped out. Where $F = -kx$ describes *a particular spring*, $\sigma = E\varepsilon$ describes *the material the spring is made of*. The bridge between them is the geometric factor:

$$\boxed{\; k = \frac{E\,A}{L_0} \;}$$

This is the central pedagogical claim of the card. A spring's stiffness $k$ factors cleanly into a **material part** ($E$) times a **geometric part** ($A / L_0$). Two springs made of the same steel but cut to different lengths or wire-thicknesses have **different $k$, but the same $E$**. The Young modulus is what you would tabulate for steel; the spring constant is what you would measure for your specific spring.

### 中文锚点

**应力 (yìnglì)** = 单位面积上承受的力。**应变 (yìngbiàn)** = 相对伸长量。**杨氏模量 (Yáng shì mókuàng)** = 材料抵抗形变的本征刚度。

| English | 中文 | Symbol | 公式 | 单位 |
|---|---|---|---|---|
| Stress | 应力 (yìnglì) | $\sigma$ | $F/A$ | $\text{Pa}$ |
| Strain | 应变 (yìngbiàn) | $\varepsilon$ | $\Delta L / L_0$ | 无量纲 |
| Young modulus | 杨氏模量 | $E$ | $\sigma / \varepsilon$ | $\text{Pa}$ (常用 GPa) |
| Spring constant | 弹簧常数 / 劲度系数 | $k$ | $EA/L_0$ | $\text{N m}^{-1}$ |
| Elastic limit | 弹性极限 (tánxìng jíxiàn) | — | — | — |
| Yield stress | 屈服应力 (qūfú yìnglì) | $\sigma_Y$ | — | $\text{Pa}$ |
| Ultimate tensile strength | 极限拉伸强度 / 抗拉强度 | $\sigma_{\text{UTS}}$ | — | $\text{Pa}$ |
| Strain energy density | 应变能密度 (yìngbiàn néng mìdù) | $u$ | $\tfrac{1}{2}\sigma\varepsilon$ | $\text{J m}^{-3}$ |

中文物理教材有时叫杨氏模量为 **弹性模量** (tánxìng mókuàng) — 同义词，但 "Young modulus" 更精确，因为还有 shear modulus（剪切模量）和 bulk modulus（体积模量）也叫弹性模量的家族成员。Cambridge / IB / AP 课本都用 Young modulus 这个名字。

英语物理的两个拼写约定：
- **Cambridge 0625 / 9702**: "Young modulus" (no apostrophe-s)
- **IB / AP / most other boards**: "Young's modulus"

两者指同一个量。

---

## Why decompose the spring constant?

Recall from [[Hooke's Law for Springs]] that every stable equilibrium produces a restoring force $F = -kx$ near equilibrium, with $k$ — the spring constant — being the curvature of the potential at the minimum. The Hooke card treated $k$ as a single number characterising "the spring."

That treatment is fine for solving problems, but it hides a deep question: **what determines $k$ for a real spring?** Why does a thin wire have a smaller $k$ than a thick rod of the same length? Why does a long wire have a smaller $k$ than a short one of the same diameter? Why does rubber have a smaller $k$ than steel of the same shape?

The answer is the decomposition above. The spring constant is **not** a fundamental property — it is a *product* of three things: the material's intrinsic stiffness $E$, the cross-sectional area $A$, and the natural length $L_0$. **The Young modulus is what the material brings; $A$ and $L_0$ are what the geometry brings.**

### Deriving $k = EA/L_0$

Consider a uniform wire of natural length $L_0$ and cross-sectional area $A$, pulled by a force $F$ at one end while the other end is fixed. The wire extends by some amount $\Delta L$.

Convert to stress and strain:

$$\sigma = \frac{F}{A}, \qquad \varepsilon = \frac{\Delta L}{L_0}.$$

For a linearly elastic material, $\sigma = E\varepsilon$ — this is the constitutive relation that defines what "linearly elastic" means. Substitute:

$$\frac{F}{A} = E \cdot \frac{\Delta L}{L_0} \quad \Rightarrow \quad F = \frac{EA}{L_0} \cdot \Delta L.$$

The right-hand side is $k\,\Delta L$ — Hooke's Law — provided we identify

$$\boxed{\; k = \frac{EA}{L_0} \;}$$

That's the bridge. **A wire is just a long, skinny spring whose $k$ is set by its geometry and the material's Young modulus.** Doubling the cross-section doubles $k$. Doubling the length halves $k$. Both effects scale linearly because elasticity is a *local* property — each tiny slice of the wire stretches by the same fractional amount $\varepsilon$, and adding more slices in parallel (thicker) or in series (longer) follows the usual spring-combination rules from [[Hooke's Law for Springs]] §"Springs in series and parallel."

> [!info] The recipe for "stiff" and "soft" springs
> Want a stiff spring? Pick a high-$E$ material (steel, $E \approx 200~\text{GPa}$), make it thick ($A$ large), make it short ($L_0$ small).
>
> Want a soft spring? Pick a low-$E$ material (rubber, $E \approx 0.01-0.1~\text{GPa}$), make it thin, make it long.
>
> The car's coil spring, the watch's hairspring, and the tendons in your wrist are all engineering problems of the form *"pick $E$, $A$, $L_0$ to hit the target $k$."*

---

## The stress-strain graph

When you load a material progressively from zero stress all the way to fracture, plot $\sigma$ on the vertical axis and $\varepsilon$ on the horizontal axis. **The shape of the resulting curve is the most-studied diagram in materials engineering.** For a typical ductile metal (mild steel is the canonical example), it has four distinct regions:

![[stress-strain-graph.svg|720]]

**Region 1 — Linear elastic.** $\sigma$ and $\varepsilon$ are proportional. Hooke's Law holds in stress-strain form: $\sigma = E\varepsilon$. The **gradient of this region IS the Young modulus** — that's the operational definition of $E$ that experimentalists use. Releasing the load returns the material to its original length, with no permanent deformation. Energy stored in this regime is fully recoverable as elastic potential energy.

**Region 2 — Yielding and plastic deformation.** Past the **elastic limit** (often very close to the **yield point** $\sigma_Y$), the curve flattens out — the material continues to deform under almost-constant stress. Releasing the load leaves a *permanent* extension; some of the work done has gone into rearranging the material's internal microstructure (dislocations moving, crystalline grains slipping past each other) rather than into recoverable elastic PE. This is **plastic deformation**.

**Region 3 — Strain hardening.** Continued plastic deformation actually makes the material harder. The dislocations that allow plastic flow get tangled up and impede each other. The stress required to push deformation further increases until reaching the **ultimate tensile strength** $\sigma_{\text{UTS}}$ — the highest stress the material can carry.

**Region 4 — Necking and fracture.** Past $\sigma_{\text{UTS}}$ the cross-section starts to narrow (necking) in a localised region. The stress concentration accelerates failure. The material fractures at the **breaking stress** $\sigma_f$, which on a true stress-strain plot is actually higher than $\sigma_{\text{UTS}}$ (because the cross-section has reduced) but on the engineering stress-strain plot (which uses the *original* cross-section throughout) appears as a downward turn before the break.

> [!warning] Three different "limits" — don't conflate them
> Students confuse three points on the stress-strain curve:
>
> - **Elastic limit** — the highest stress at which the material returns to its original length on unloading. Past this, permanent deformation begins.
> - **Yield stress** $\sigma_Y$ — the stress at which the material starts to flow plastically at near-constant load. Often very close to the elastic limit but slightly above it.
> - **Ultimate tensile strength** $\sigma_{\text{UTS}}$ — the *peak* of the stress-strain curve. Significantly higher than the yield stress for ductile metals (steel's UTS is roughly twice its yield).
>
> And then there's the **breaking stress** $\sigma_f$ at fracture, which is *lower* than $\sigma_{\text{UTS}}$ on the engineering curve. Four numbers, four distinct points, four meanings.

### Brittle vs ductile

The diagram above is for a **ductile** material (e.g. mild steel, copper, aluminium). Such materials have a long plastic region — you can stretch them significantly before they break, and they give visible warning of failure (necking, audible groans, observable deformation).

**Brittle** materials (cast iron, glass, concrete in tension, ceramics) have a much shorter or absent plastic region. They fracture suddenly, often at stresses *below* their theoretical Young-modulus-predicted strength because microscopic cracks act as stress concentrators. The Titanic's hull plates were brittle at North Atlantic temperatures; the iceberg made a long brittle crack rather than a small ductile dent.

The engineering rule of thumb: **ductile materials warn you before failing; brittle materials don't.** Buildings are designed with ductile members at critical structural points so collapse, if it happens, is observable in time to evacuate.

---

## Materials data — order of magnitudes you should remember

The Young modulus for common materials spans **six orders of magnitude**:

| Material | $E$ (GPa) | Notes |
|---|---|---|
| Diamond | ~1200 | The stiffest natural material |
| Tungsten | ~411 | Why filaments hold shape at high temperatures |
| Steel (mild) | ~200 | The universal engineering benchmark |
| Copper | ~110 | Plumbing pipes, electrical wire |
| Aluminium | ~70 | Aircraft frames; 1/3 of steel's stiffness at 1/3 of steel's density |
| Glass | ~70 | Surprisingly stiff (per unit mass) but brittle |
| Concrete | ~30 (compression) | Very weak in tension; reinforced with steel rebar |
| Wood (along grain) | ~10 | Anisotropic — about 10× stiffer along the grain than across |
| Bone (cortical) | ~14 | Living composite material |
| Rubber | ~0.01–0.1 | $E$ five orders of magnitude below steel |
| Soft tissue | ~10⁻⁴ to 10⁻² | The reason surgeons and engineers think differently |

**The stiffness of a real spring depends entirely on the material chosen.** A steel spring 1 metre long with a 1 mm² cross-section has $k = (200 \times 10^9)(10^{-6})/1 = 200~\text{N m}^{-1}$. The same geometry in rubber would have $k \approx 0.01-0.1~\text{N m}^{-1}$ — *ten thousand times softer*.

> [!tip] Quick sanity check
> If a student tells you a material has $E = 10^7~\text{Pa}$, that's about 10 MPa — close to soft tissue. Steel-like materials live at 100-200 GPa = $10^{11}-2 \times 10^{11}$ Pa. Anything in the GPa range is structural; anything in the MPa range is biological or polymer. Anything in the kPa range is a gel. **Order-of-magnitude familiarity is the first line of defence against arithmetic errors.**

---

## Strain energy and elastic PE

When a material is stretched within its linear elastic regime, the work done is stored as elastic potential energy. We can compute this two ways and confirm they agree.

**Way 1 — from the spring picture.** From [[Hooke's Law for Springs]] §"Elastic potential energy", the PE stored in a spring extended by $\Delta L$ is

$$U_{\text{spring}} = \tfrac{1}{2}\,k\,(\Delta L)^2.$$

**Way 2 — from the material picture.** Define the **strain energy density** $u$ (joules per cubic metre) as the elastic PE stored per unit volume of the material. In the linear regime, the work done by stress per unit volume as strain increases from 0 to $\varepsilon$ is the triangle area under the $\sigma$-$\varepsilon$ curve:

$$u = \tfrac{1}{2}\,\sigma\,\varepsilon = \tfrac{1}{2}\,E\,\varepsilon^2.$$

The total stored PE is then $u$ times the volume of the wire, $V = A L_0$:

$$U_{\text{material}} = \tfrac{1}{2}\,E\,\varepsilon^2 \cdot A L_0 = \tfrac{1}{2}\,E\,\frac{(\Delta L)^2}{L_0^2} \cdot A L_0 = \tfrac{1}{2}\,\frac{EA}{L_0}\,(\Delta L)^2.$$

Since $k = EA/L_0$, this is *exactly* $U_{\text{spring}}$. The two ways agree, as they must.

> [!info] Why the agreement matters
> The energy stored in a spring **does not depend on whether you describe it as "a spring with constant $k$" or "a material of modulus $E$ with geometry $A, L_0$".** The agreement of $U_{\text{spring}} = U_{\text{material}}$ is the energy-side proof that $k = EA/L_0$ is the correct geometric decomposition. *Energy is the auditor of every mechanical claim.*

---

## Worked examples

### Example 1 — Extension of a steel wire (Cambridge / IB level)

A steel wire of length $2.0~\text{m}$ and diameter $0.50~\text{mm}$ is subjected to a tensile force of $50~\text{N}$. Take $E_{\text{steel}} = 2.0 \times 10^{11}~\text{Pa}$. Find (a) the stress, (b) the strain, (c) the extension.

**Solution.**

Cross-sectional area: $A = \pi r^2 = \pi (0.25 \times 10^{-3})^2 = 1.96 \times 10^{-7}~\text{m}^2$.

(a) $\sigma = F/A = 50 / (1.96 \times 10^{-7}) = 2.55 \times 10^8~\text{Pa} = 255~\text{MPa}$.

(b) $\varepsilon = \sigma/E = (2.55 \times 10^8) / (2.0 \times 10^{11}) = 1.28 \times 10^{-3}$ (0.128%).

(c) $\Delta L = \varepsilon \cdot L_0 = (1.28 \times 10^{-3})(2.0) = 2.55 \times 10^{-3}~\text{m} = 2.55~\text{mm}$.

*Sanity check:* 255 MPa is well below the yield stress of mild steel (~250-400 MPa) but uncomfortably close. The wire is in the upper end of its elastic regime — a real engineer would use a thicker wire for this load.

### Example 2 — Finding $E$ from experimental data

In a lab experiment, a copper wire of length $1.50~\text{m}$ and cross-section $0.20~\text{mm}^2$ is loaded with increasing weights and the extension recorded:

| Load (N) | Extension (mm) |
|---|---|
| 5 | 0.34 |
| 10 | 0.68 |
| 15 | 1.02 |
| 20 | 1.36 |

Find $E$ for copper.

**Solution.** The data is clearly linear. Compute stress and strain at the last (largest) point and divide:

$\sigma = F/A = 20 / (0.20 \times 10^{-6}) = 1.0 \times 10^8~\text{Pa}$.

$\varepsilon = \Delta L / L_0 = (1.36 \times 10^{-3}) / 1.50 = 9.07 \times 10^{-4}$.

$E = \sigma / \varepsilon = (1.0 \times 10^8) / (9.07 \times 10^{-4}) \approx 1.1 \times 10^{11}~\text{Pa} = 110~\text{GPa}$.

This matches copper's tabulated value (~110 GPa). The proper experimental treatment is to plot all four data points as $\sigma$ vs $\varepsilon$, fit a line through them, and take the gradient — that uses all four points to estimate $E$ and gives an uncertainty bound on the gradient. Cambridge / IB practical papers expect the graph-and-gradient method explicitly.

### Example 3 — Elastic PE stored in a stretched wire

A nylon climbing rope (mainly to load-share, not actually to stretch in normal use) has $E \approx 5~\text{GPa}$, length $30~\text{m}$ when slack, and cross-section $10~\text{mm}^2$. A $75~\text{kg}$ climber falls $1~\text{m}$ before the rope catches them. Assuming the rope obeys Hooke's Law throughout the catch (idealised), find the maximum extension of the rope and the maximum force on the climber.

**Solution.** This is a famous belay-physics problem. The rope acts as a spring with $k = EA/L_0 = (5 \times 10^9)(10^{-5})/30 = 1.67 \times 10^3~\text{N m}^{-1}$.

The climber falls $h = 1~\text{m}$ in free fall, then stretches the rope by some additional distance $\Delta L$. Conservation of energy from the start of the fall to the moment of maximum extension (where the climber is instantaneously at rest):

$$m g (h + \Delta L) = \tfrac{1}{2}\,k\,(\Delta L)^2.$$

Numerically: $75 \cdot 9.81 \cdot (1 + \Delta L) = \tfrac{1}{2}(1.67 \times 10^3)(\Delta L)^2$.

$735.75(1 + \Delta L) = 833.3\,(\Delta L)^2$.

Expanding: $833.3\,(\Delta L)^2 - 735.75\,\Delta L - 735.75 = 0$.

Quadratic formula gives $\Delta L \approx 1.39~\text{m}$. (Plus the $1~\text{m}$ of free fall — total drop including rope stretch is about $2.4~\text{m}$.)

The maximum force on the climber at full extension is $F_{\max} = k \cdot \Delta L = 1.67 \times 10^3 \times 1.39 \approx 2.3 \times 10^3~\text{N}$ — about $3g$ deceleration ($2300 / (75 \cdot 9.81) \approx 3.1$).

*Real climbing ropes are dynamic — they are designed to stretch significantly (up to 30%) precisely to keep the peak force low. A static rope at the same geometry would generate a much higher peak force and risk back injury or anchor failure. Materials choice is the engineering knob.*

---

## Beyond syllabus

### The atomic-scale origin of $E$

Recall from [[Hooke's Law for Springs]] §"Atoms in a crystal" that atoms in a solid sit in potential wells created by their neighbours. Each interatomic bond behaves as a tiny Hooke's-Law spring with some bond-stiffness $k_{\text{bond}}$, determined by the second derivative of the interatomic potential at the equilibrium spacing.

The macroscopic Young modulus is the **bulk average** of these atomic-scale bond stiffnesses. If $a$ is the equilibrium atomic spacing and $k_{\text{bond}}$ the bond stiffness, then the Young modulus is approximately

$$E \approx \frac{k_{\text{bond}}}{a}.$$

This is the central result of atomistic elasticity theory. **Strong bonds give high $E$; weak bonds give low $E$**. Diamond's $E \approx 1200~\text{GPa}$ comes from extremely strong directional carbon-carbon covalent bonds. Rubber's $E \approx 0.01-0.1~\text{GPa}$ comes mostly from *entropy* (uncoiling polymer chains) rather than bond stretching, which is why rubber's elasticity has unusual temperature dependence (it actually gets *stiffer* when you heat it — try it with a stretched rubber band).

### The stiffness tensor and anisotropy

For an isotropic material (steel, glass, water), the single number $E$ captures the elastic response in any direction. But many materials are **anisotropic** — wood is stiffer along the grain than across it; carbon-fibre composites are stiffer along the fibre direction than across it; bone is stiffer along the long axis than radially.

For an anisotropic material, $E$ is no longer a single number — it becomes a **stiffness tensor** (called the *elastic tensor* or *stiffness matrix*) with up to 21 independent components in the most general case. Each component relates a particular stress direction to a particular strain direction. The tensor reduces to fewer independent components when the material has symmetries (cubic crystals have 3 components; isotropic materials have just 2: $E$ and the shear modulus $G$, or equivalently $E$ and Poisson's ratio $\nu$).

This is the proper home of materials science. Cambridge / IB / AP all stop at the isotropic scalar $E$, but every real engineering analysis in 2026 — from aircraft composite design to bone-implant biocompatibility — uses the tensor.

### Beam bending — the hunter target named in the Notebook

The question behind this section is *why a beam bends the way it does.* The full story is **Euler-Bernoulli beam theory** (1750s), which derives the bending curvature of a beam in terms of $E$ and a geometric quantity called the **second moment of area** $I$.

![[beam-bending.svg|900]]

The deep formula:

$$EI \frac{d^2 y}{dx^2} = M(x)$$

where $y(x)$ is the deflection of the beam centreline, $M(x)$ is the bending moment at position $x$, and $I$ is a purely geometric quantity. The left panel above shows *why* the equation has this form: when a beam bends, fibres above the neutral axis are in **compression** (stress directed inward) and fibres below are in **tension** (stress directed outward). The neutral axis itself feels no longitudinal stress. The further a fibre is from the neutral axis, the larger the stress it carries — so material placed *far from* the centre contributes much more to bending resistance than material placed *near* the centre.

For a beam of rectangular cross-section, $I = bh^3 / 12$ where $b$ is the width and $h$ is the height in the direction of bending — so making a beam *deeper* (in the direction of the load) increases stiffness as $h^3$, while making it wider only increases stiffness as $b$. **This is why structural beams are tall, not square**: depth dominates by a cube law.

The right panel above shows this concretely. Three rectangles all have the same cross-sectional area (the same amount of material). Beam A is wide and flat; beam C is tall and narrow; both have aspect ratio 10:1. Computing $I = bh^3/12$ for each gives the relative stiffnesses 1 : 10 : 100 — **a hundred-fold difference in bending resistance from the same amount of steel, just by orienting it differently**. This is the structural-engineering version of "the same lever can be a teaspoon or a crowbar depending on where you put your hand."

The full derivation lives in [[Beam Bending]] (mechanics of materials course territory; beyond Cambridge A-Level). For our purposes, the takeaway is: **once you know $E$ for the material, beam stiffness becomes a problem about $I$ — pure geometry.** The I-beam profile in steel construction takes the cube-law insight to its limit by concentrating material in two flanges at the maximum distance from the neutral axis, with just enough web in between to hold them together — an optimal compromise of material-per-deflection that no rectangular cross-section can match.

### Composite materials — engineering past the natural limits

Modern engineering composites combine high-$E$ stiff fibres (carbon, glass, kevlar) with low-$E$ tough matrix (epoxy, polymer) to get materials with effective $E$ values that don't exist in nature. Carbon-fibre-reinforced polymer (CFRP) achieves $E \approx 150~\text{GPa}$ at a density of $1.6~\text{g cm}^{-3}$ — *higher specific stiffness than steel*. This is why aerospace, racing bicycles, and Formula 1 monocoques have moved to composites since the 1980s.

The design rule: $E_{\text{composite}} \approx v_f E_f + v_m E_m$ where $v_f, v_m$ are the volume fractions and $E_f, E_m$ are the modulus of the fibre and matrix respectively. This is just the *parallel*-spring formula from Hooke's Law applied at the material level — another agreement between the spring picture and the material picture.

### Materials selection — the Ashby diagrams

Michael Ashby (Cambridge engineering, 1990s) introduced **materials property diagrams** plotting any two materials properties (e.g. $E$ vs density $\rho$) on log-log axes, with every known material as a point. The diagrams collapse the "what material should I use?" question to a geometric optimisation: draw a line of slope $\partial\log E / \partial\log\rho$ matching your engineering criterion (e.g. for stiff lightweight beam, slope $= 1/2$), and the materials above the line are candidates. **The Ashby chart is the Periodic Table of engineering — every material decision goes through it.**

---

## Formula sheet status

| Board | $\sigma = F/A$ | $\varepsilon = \Delta L/L_0$ | $E = \sigma/\varepsilon$ | $k = EA/L_0$ | $u = \tfrac{1}{2}\sigma\varepsilon$ |
|---|---|---|---|---|---|
| Cambridge 0625 | Not in syllabus | Not in syllabus | Not in syllabus | — | — |
| Cambridge 9702 | **On data sheet** | **On data sheet** | **On data sheet** | Not printed | Not printed (derive) |
| IB Physics | Implicit only | Implicit only | Implicit only | — | — |
| AP Physics 1 | Not in syllabus | Not in syllabus | Not in syllabus | — | — |
| AP Physics C Mech | Not in syllabus | Not in syllabus | Not in syllabus | — | — |

**Takeaway.** Cambridge 9702 is the **primary syllabus** for stress / strain / Young modulus content. 0625 expects qualitative familiarity but doesn't formally test the equations. IB Physics mentions elastic forces as a contact-force type (Theme A.2.2) but the full treatment is below their A-Level/HL standard. AP Physics 1 stops at $F = -kx$ for springs and doesn't go into materials. **AP Physics C** doesn't include this either despite being calculus-based — the topic is reserved for the dedicated *Mechanics of Materials* course at college level.

The $k = EA/L_0$ relation is essential for connecting Hooke's Law to materials, but it's not on the 9702 data sheet — students are expected to be able to derive it from $\sigma = E\varepsilon$ and $F = kx$. The strain energy density $u = \tfrac{1}{2}\sigma\varepsilon$ is similarly not on any data sheet but is derivable from $\tfrac{1}{2}k(\Delta L)^2$ divided by volume.

---

## Exam Notes

### Cambridge 9702 A-Level — §6.1 (with §6.2's Hooke content in [[Hooke's Law for Springs]])

- **The definitions earn their marks verbatim:** stress $\sigma = F/A$ (force per unit *cross-sectional* area, Pa), strain $\varepsilon = x/L$ (extension per unit *original* length — a ratio, **no unit**), Young modulus $E = \sigma/\varepsilon$ (Pa again, since strain is bare).
- **The experiment is a named LO:** determining $E$ for a wire — long thin wire (large $L$, small $A$ maximise measurable extension), micrometer for diameter *in several places*, marker + ruler for extension, load in steps, plot $\sigma$–$\varepsilon$ (or $F$–$x$) and take the **gradient of the linear region**. Safety goggles get a mark more often than dignity suggests.
- **The graph vocabulary:** limit of proportionality, elastic limit, plastic deformation, breaking point — read from the stress–strain curve; **strain energy = area under the force–extension line** ($\tfrac12 F x$ while linear).
- **Where marks leak:** radius-vs-diameter in $A = \pi r^2$ (the classic factor-of-4); quoting strain in metres; using loaded length instead of original length; and gradient-of-wrong-region on a curve that leaves proportionality.

### Other boards

- **Cambridge 9231:** stress/strain as such is not a Further Mechanics topic — elastic strings appear via the modulus of elasticity $\lambda$ ($T = \lambda x/L$), treated in full in [[Elastic Strings and Springs]] (where $\lambda = EA$ closes the loop back to this card).
- **Cambridge 0625:** not examined — IGCSE stops at Hooke's law and the load–extension graph.
- **IB Physics (2023 guide):** deformation beyond Hooke's law was dropped; Young modulus is not assessed.
- **AP Physics 1/2/C:** not an examined topic (occasionally a passage-context in AP 2).

## Connections

- **Parent:** [[Hooke's Law for Springs]] — the macroscopic version. This card explains *why* a spring has the spring constant it does, by decomposing $k$ into material ($E$) and geometric ($A$, $L_0$) factors.

- **Mathematical prerequisites:**
   - [[Differentiation]] — the elastic regime is the linear portion of $\sigma(\varepsilon)$, i.e. the local slope at $\varepsilon = 0$. The stress-strain graph beyond yield is a study in non-linear constitutive behaviour.
   - [[Standard Integrals]] — strain energy density is the integral of $\sigma$ with respect to $\varepsilon$.

- **Physics siblings:**
   - [[Forces and Equilibrium]] — the static side of force analysis; stress is force-per-unit-area in equilibrium loading.
   - [[Work, Energy and Power]] — strain energy is one of the canonical mechanical energy forms.

- **Children:**
   - [[Beam Bending]] — Euler-Bernoulli theory; the hunter target "why a beam bends the way it does" reaches its full formal statement here.
   - [[Material Failure]] — fracture mechanics, brittle vs ductile, fatigue under cyclic loading, the Griffith criterion for crack propagation.
   - [[Composite Materials]] — fibre + matrix combinations, the parallel-spring formula at the material level, modern aerospace applications.

- **Forward bridges into oscillations:**
   - [[Simple Harmonic Motion]] — the SHM equation $a = -\omega^2 x$ has $\omega = \sqrt{k/m}$, and now we know $k$ comes from $E$, $A$, $L_0$. The frequency of a wire's longitudinal vibration is $\omega \propto \sqrt{E/\rho}$ — pure material property.
   - [[Waves I: The Wave Equation]] — the speed of sound in a solid is $v_s = \sqrt{E/\rho}$, exactly the same combination of material properties. Wave speeds are Young-modulus signatures.

- **Misconceptions cleared:** stress is **not** force (it's force per unit area); strain is **not** an extension in metres (it's dimensionless); the spring constant $k$ is **not** a material property (it depends on $A$ and $L_0$ too); the elastic limit is **not** the same as the yield stress or the ultimate tensile strength (three distinct points on the stress-strain curve).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\sigma$ | `\sigma` | Stress, units Pa |
| $\varepsilon$ | `\varepsilon` | Strain, dimensionless |
| $E$ | `E` | Young modulus, units Pa (typically GPa) |
| $\sigma = E\varepsilon$ | `\sigma = E\varepsilon` | Hooke's Law in material form |
| $k = EA/L_0$ | `k = EA/L_0` | Spring constant from material + geometry |
| $u = \tfrac{1}{2}\sigma\varepsilon$ | `u = \tfrac{1}{2}\sigma\varepsilon` | Strain energy density |
| $\sigma_Y$ | `\sigma_Y` | Yield stress |
| $\sigma_{\text{UTS}}$ | `\sigma_{\text{UTS}}` | Ultimate tensile strength |
| $\sigma_f$ | `\sigma_f` | Breaking / fracture stress |
| $\text{Pa} = \text{N m}^{-2}$ | `\text{Pa} = \text{N m}^{-2}` | Pascal as derived SI unit |
| $EI \dfrac{d^2 y}{dx^2} = M$ | `EI \frac{d^2 y}{dx^2} = M` | Euler-Bernoulli beam equation (beyond-syllabus) |

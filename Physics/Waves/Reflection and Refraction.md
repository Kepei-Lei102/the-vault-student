---
chinese: 反射与折射 (fǎnshè yǔ zhéshè)
aliases:
  - Snell's Law
  - Total Internal Reflection
prerequisites:
  - "[[Progressive Waves]]"
leads_to:
  - "[[Lenses and Image Formation]]"
teach_together:
  - "[[Ibn al-Haytham and the Question of Seeing]]"
  - "[[Polarisation]]"
tags:
  - subject/physics
  - domain/waves
  - level/IGCSE
  - level/AP
  - level/university
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/0625-3-2
  - syllabus/IB-Physics-C-3-1
  - syllabus/AP-Physics-2-13-1
  - syllabus/AP-Physics-2-13-3
  - type/deep
  - type/derivation
  - misconception/angles-from-the-surface
  - misconception/virtual-means-invisible
  - misconception/refraction-changes-frequency
---

# Reflection and Refraction 反射与折射

*A straw looks broken where it enters a glass of water. Lift it out: perfectly straight. Nothing happened to the straw. Something happened to the route by which its light reached your eye.*

Light gives us evidence about where things are. Mirrors and water surfaces change that evidence. To understand the resulting pictures, follow **actual light forwards**, then ask where an observer would place its source.

## 中文锚点

把筷子斜插进一杯水里，水面下那一截看起来像折了一下。不是筷子弯了，而是它反射出来的光从水里进入空气时，拐了个弯才到你眼里。你的眼睛却仍按光最后到来的方向，沿直线往回找，于是把水下那截筷子认到了别的位置。眼见不一定是东西原来的位置：你看到哪里，还取决于光是怎么走到你面前的。

## 1. Two pictures of the same travelling light

A **wavefront** joins points at the same phase: for example, all the crests of a plane wave. A **ray** points in the direction in which the light travels. In a uniform, isotropic medium, rays are perpendicular to wavefronts.

- Wavefronts explain *why* a direction changes.
- Rays make it easy to construct the resulting path and image.
- A narrow laser beam can be modelled by a ray; an actual beam has width. Ray optics works when relevant objects and openings are large compared with the wavelength. [[Diffraction]] and interference need the wave picture.

A **normal** is a line perpendicular to the surface **at the point the ray meets it**. Every incidence, reflection and refraction angle below is measured from that normal. A curved surface has a different normal at every point.

At an interface, incident energy can be **reflected**, **transmitted**, or **absorbed**. Refraction describes a change in the transmitted direction. Ordinary clear glass both reflects and transmits; it does not choose only one.

![[reflection-refraction-animation.mp4]]

*Watch the wavefront spacing shrink while the rate of crests crossing the boundary stays the same. Then reverse the journey and increase the incidence angle until the transmitted ray reaches its limit. Ray thickness is illustrative, not a measure of power; the wavefront scene isolates the transmitted wave.*

## 2. Reflection: one surface, equal angles

For a smooth surface,

$$\boxed{i=r_{\rm refl}}.$$

The incident ray, reflected ray and normal lie in the same plane. A ray arriving along the normal returns along its incoming line.

**Why equal angles?** Imagine replacing a reflected journey from A to a mirror and then to B by a straight journey from A to B′, the mirror image of B. The two final segments have equal lengths by symmetry. A straight line is the shortest route between A and B′; unfolding it back at the mirror gives equal angles. In the same uniform medium, shortest length also means shortest travel time. The wave explanation of that travel-time rule comes later.

A rough wall also obeys the law locally. Its tiny surface patches face different directions, so their reflected rays spread out: **diffuse reflection**. A polished mirror has nearly parallel local normals and preserves organised ray directions: **specular reflection**. Diffuse reflection is why people around a room can all see a page; it is not a breakdown of the law.

### A plane mirror constructs a virtual image

![[reflection-refraction-mirror.svg]]

To locate the image of one point:

1. Draw two rays from the point to different places on the mirror.
2. Reflect each using the local normal and equal angles.
3. Extend the reflected rays **backwards with dashed lines**. Their extensions meet behind the mirror.

The real rays diverge; their backward extensions meet. This is a **virtual image**. It is visible because reflected light enters an eye, but a screen placed at the apparent image position cannot catch converging light there. A **real image**, by contrast, is formed where actual rays converge and can be caught on a screen.

The plane-mirror image is upright, the same size as the object, and as far behind the mirror as the object is in front. Similar triangles establish the equal distances; doing the same construction for the top and bottom establishes equal size. Move your face 10 cm closer to a fixed mirror and its image also moves 10 cm closer to the mirror: the face–image separation shrinks by 20 cm.

**What does “laterally inverted” mean?** Writing faces the opposite way in a mirror. Geometrically, the mirror reverses the coordinate perpendicular to its surface: front–back. It does not secretly choose the horizontal axis over the vertical one. Our comparison with a person turned around to face us produces the familiar left–right description.

## 3. Refraction: a change of speed turns a wavefront

The **absolute refractive index** of a transparent medium is

$$\boxed{n=\frac{c_0}{v}},$$

where $c_0$ is the vacuum speed of light and $v$ is its phase speed in the medium. Refractive index is dimensionless. For ordinary visible-light examples, air has $n\approx1$, water about $1.33$, and common glass about $1.5$; the exact value depends on material and wavelength.

**Higher index means lower speed**, not necessarily greater mass density. “Optically denser” is index language; it does not mean heavier per cubic centimetre.

### The invariant is frequency

At a stationary boundary, the same sequence of oscillations must match on both sides: crests cannot steadily accumulate at the interface. The frequency stays fixed. Since $v=f\lambda$,

$$\frac{\lambda_2}{\lambda_1}=\frac{v_2}{v_1}=\frac{n_1}{n_2}.$$

Light entering glass has a shorter wavelength and lower speed, but the same frequency. Its photons have the same energy $hf$ in this stationary, transparent situation. A shorter wavelength inside glass does not mean the light has become bluer; colour comparisons conventionally use frequency or vacuum wavelength.

### Derive Snell's law by following a wavefront

![[reflection-refraction-wavefront.svg]]

Take a plane wavefront AB. A reaches the boundary first. During the time $\Delta t$ that B travels to C in medium 1, the disturbance from A spreads a distance $v_2\Delta t$ in medium 2. The tangent CD to this advancing disturbance is the new wavefront. This is the **Huygens construction**.

The ray BC is perpendicular to AB, and AD is perpendicular to CD. Both right triangles share the hypotenuse AC. Because wavefronts are perpendicular to rays, their angles with the surface equal the corresponding ray angles with the normal.

**Tool: sine in two right triangles; trigger: one shared distance and one elapsed time.**

$$\sin i=\frac{BC}{AC}=\frac{v_1\Delta t}{AC},\qquad
\sin r=\frac{AD}{AC}=\frac{v_2\Delta t}{AC}.$$

Divide to eliminate the shared geometry and time:

$$\frac{\sin i}{\sin r}=\frac{v_1}{v_2}=\frac{n_2}{n_1}
\quad\Longrightarrow\quad
\boxed{n_1\sin i=n_2\sin r}.$$

This is **Snell's law**. Entering a higher-index medium reduces $\sin r$, hence $r<i$: towards the normal. Entering a lower-index medium does the opposite, provided a transmitted ray exists.

> [!tip] No bend does not mean no change
> At normal incidence, $i=r=0$. The entire wavefront enters at once, so it has no reason to rotate. Speed and wavelength still change. The wavefront story explains the exception rather than making you memorise it.

### Worked: air into glass

A ray of vacuum wavelength 600 nm meets glass of index 1.50 at 40° to the normal. Find its direction, speed and wavelength inside.

**Tool: Snell; trigger: a transmitted direction across a known interface.**

$$\sin r=\frac{1.00}{1.50}\sin40^\circ
\quad\Rightarrow\quad r=25.4^\circ.$$

**Tool: index definition; trigger: propagation speed in a material.**

$$v=\frac{3.00\times10^8}{1.50}=2.00\times10^8\ \mathrm{m\,s^{-1}}.$$

**Tool: fixed frequency; trigger: the boundary is stationary.**

$$\lambda_{\rm glass}=\frac{600}{1.50}=400\ \mathrm{nm}.$$

The smaller angle agrees with the lower speed. If a calculator gives 74.6°, check whether you measured from the surface instead of the normal.

## 4. Two surfaces: blocks, bubbles and apparent depth

### A parallel-sided block shifts a ray sideways

At the first face, light bends towards the normal. At the second, it bends away. When the outside medium is the same on both sides and the faces are parallel, applying Snell twice gives the original outgoing angle. The emerging ray is **parallel to, but displaced from**, the incident ray.

For block thickness $t$ measured perpendicular to its faces, geometry gives the perpendicular separation of the incoming and outgoing ray lines:

$$s=\frac{t\sin(i-r)}{\cos r}.$$

Inside length is $t/\cos r$; project it perpendicular to the incoming direction to get $s$. A thicker window displaces the ray more. Non-parallel faces need not restore its original direction.

**Practical investigation:** trace a rectangular transparent block on paper. Send a narrow ray through it; mark two points on each external ray before removing the block. Join the points, locate the entry/exit positions, join the internal path, and draw normals. Measure several $i,r$ pairs. Plot $\sin i$ vertically against $\sin r$ horizontally: for air into the block, the slope estimates its index. Repeated angles test the model better than one attractive-looking ray.

A **semicircular block** can isolate one refraction. Aim along a radius at the curved surface: the ray enters normally and reaches the centre of the flat face without bending at entry. Rotate the incident direction about that centre to study the flat glass–air boundary. A beam that misses the centre can bend at the curved face too, spoiling the intended isolation.

### Worked real paper: the aquarium bubble

**AP Physics 2, 2019, Question 4(a), 3 marks.** The original asks for the paths of two rays through an air bubble in water: B aims at its centre; A meets it above the centre. The diagram below reconstructs the geometry with explicit normals; exact angles were not supplied or required.

![[reflection-refraction-bubble.svg]]

**Tool: radius is normal to a circle; trigger: the boundary is curved.** For B, both interface normals lie along its path. It goes straight through both surfaces even though its speed changes twice.

**Tool: Snell's direction test; trigger: A enters lower-index air from water.** At A's entry, draw the radius through the contact point. The transmitted ray bends **away from that normal**, travelling upwards through the bubble.

**Tool: rebuild the normal at the next contact; trigger: this is a different place on a curved surface.** On exiting air into water, the ray bends **towards the new normal**. In this geometry its upward tilt increases. “Towards the normal” does not mean “downwards” or “back towards the original ray.”

The published scheme awards one mark each for B straight through, A's correct entry bend, and A's correct exit bend. Normals are not required for those marks but make the reasoning reliable. [Question and published scoring guidelines](https://apcentral.collegeboard.org/media/pdf/ap19-sg-physics-2.pdf).

### Why the pool looks shallower

![[reflection-refraction-depth.svg]]

Light from a submerged coin bends away from the normal when it leaves water. Your eye traces the outgoing rays backwards as straight lines, placing the apparent coin closer to the surface.

For a ray meeting the surface a horizontal distance $x$ from the coin's vertical line,

$$x=d\tan i=d_{\rm app}\tan r
\quad\Rightarrow\quad
\frac{d_{\rm app}}d=\frac{\tan i}{\tan r}.$$

Near the normal, small angles give $\tan\theta\approx\sin\theta$. Combine this with Snell:

$$\boxed{d_{\rm app}\approx d\frac{n_{\rm observer}}{n_{\rm object}}}.$$

For an observer in air looking nearly vertically into water, a coin 2.00 m down appears about 1.50 m down. This is a **small-angle approximation**, not a universal rule for an oblique view. Rays at widely different angles do not all back-project to one exact point at a plane refracting surface.

## 5. The critical angle: when refraction runs out of directions

Travel from glass into air and keep increasing $i$. Snell demands an even larger $r$. Eventually $r$ reaches 90°: the limiting transmitted direction lies along the surface.

Call the incidence angle there $\theta_c$, the **critical angle**:

$$n_1\sin\theta_c=n_2\sin90^\circ
\quad\Rightarrow\quad
\boxed{\sin\theta_c=\frac{n_2}{n_1}}.$$

For glass with $n_1=1.50$ into air with $n_2\approx1$, $\theta_c=41.8^\circ$.

![[reflection-refraction-critical.svg]]

Beyond this, Snell would require $\sin r>1$. That is not a very large real angle: it is **no possible transmitted travelling ray**. For ideal transparent media, all incident power is reflected: **total internal reflection**, or TIR.

Both conditions matter:

1. The ray travels from **higher to lower refractive index**.
2. Its incidence angle is **greater than** the critical angle.

At the critical angle, draw the limiting grazing ray. Below it, reflection and transmission normally coexist; ordinary partial reflection does not suddenly begin at the critical angle. Air-to-glass cannot produce TIR, whatever the angle.

### Where this earns its keep: fibres and prisms

A step-index optical fibre has a higher-index **core** inside lower-index **cladding**. Rays meeting the side boundary beyond its critical angle are reflected back into the core. Repeated reflection guides light along the fibre; it does not need a metal mirror coating.

The cladding is not optional packaging: it establishes a controlled optical boundary even when the outside is touched or surrounded by other materials. Excessively tight bends can spoil guidance. Real fibres still attenuate through absorption and scattering, so telecom links need a power budget; TIR is not a promise of lossless communication. [[Electromagnetic Spectrum]] connects this to optical communication bands.

A right-angle glass prism can turn a ray through 90°. Enter perpendicular to one short face; the ray meets the hypotenuse at 45°. For $n=1.50$ surrounded by air, $45^\circ>41.8^\circ$, so it reflects internally and leaves normally through the other short face. Immerse the same prism in water and the critical angle becomes about 62.7°: the 45° ray no longer totally reflects. The surrounding medium is part of the device.

## 6. Dispersion: the index depends on colour

White light contains a range of visible frequencies. In ordinary visible-light glass, shorter wavelengths generally have a larger index. Violet therefore bends more strongly than red in a prism. Its non-parallel faces leave different colours travelling in different directions: **dispersion**.

The conventional order from low to high frequency is **red, orange, yellow, green, blue, indigo, violet**; vacuum wavelength decreases in that order. The actual spectrum is continuous, not seven physically separated stripes. **Monochromatic** means one frequency; real sources have some spectral width.

The prism separates frequencies already present; it does not manufacture coloured photons by changing their frequencies. A parallel-sided slab produces colour-dependent sideways shifts but restores parallel emerging directions. That contrast is a useful check on any prism explanation.

## Beyond Syllabus — why the travel-time rule works

Recall that reflection and refraction describe one wave meeting an interface. **Fermat's principle** says the realised geometrical path makes optical travel time stationary under a small path change. In these simple planar examples it is a minimum; “light always takes the shortest distance” is false when speeds differ.

Put A a height $h_1$ above a flat boundary, B a depth $h_2$ below it, with horizontal separation $L$. Let the crossing point be $x$ from A's vertical projection. Then

$$T(x)=\frac{\sqrt{h_1^2+x^2}}{v_1}
+\frac{\sqrt{h_2^2+(L-x)^2}}{v_2}.$$

**Tool: differentiate travel time; trigger: a continuously variable crossing point.**

$$\frac{dT}{dx}=\frac{x}{v_1\sqrt{h_1^2+x^2}}
-\frac{L-x}{v_2\sqrt{h_2^2+(L-x)^2}}=0.$$

Recognise the geometric sines: $\sin i/v_1=\sin r/v_2$, which is Snell again. Light spends more of its route in the faster medium, just as a rescue route may trade extra running for less swimming.

But light does not inspect a map and make a decision. In the wave description, neighbouring paths usually contribute rapidly changing phases that cancel. Near a stationary-time path, neighbouring phases reinforce. The ray is the path that survives the wave sum.

### What “total” does and does not mean

Recall that the ray model describes propagating directions. Above the critical angle, electromagnetic fields still penetrate a short distance into the lower-index side as an **evanescent field**, decaying away from the boundary. For a single ideal, lossless interface there is no net time-averaged power flowing away normally into that medium. A sufficiently close second medium can couple to this field: **frustrated TIR**. Thus “no transmitted travelling ray” is more precise than “absolutely no field outside.”

The reflected/transmitted power fractions below critical require **Fresnel equations** and depend on polarisation. [[Polarisation]] derives the Brewster-angle relation, where one reflected polarisation vanishes. Snell determines directions, not how much light follows each direction.

## Misconceptions to retire

| Tempting shortcut | Better test |
|---|---|
| Measure from the surface | Draw its normal first; use the complementary angle if needed. |
| A higher index always turns a ray | Normal incidence changes speed without changing direction. |
| A virtual image is imaginary or invisible | Actual light reaches your eye; the apparent source is where backward extensions meet. |
| Entering glass changes frequency | At a stationary boundary, frequency is fixed; speed and wavelength change. |
| TIR means any reflection inside glass | Check higher-to-lower index **and** incidence above critical. |
| “Towards the normal” means towards the original direction | Rebuild the normal at each contact, especially on a curved boundary. |
| Snell predicts brightness | It predicts direction; reflection/transmission coefficients require more physics. |

## Exam Notes

### Cambridge 0625 — §3.2.1, §3.2.2 and §3.2.4

Core includes incidence/reflection angles and normals; plane-mirror image properties; the reflection law; experiments tracing light through transparent blocks of different shapes; the critical angle and internal/TIR phenomena; prism dispersion and visible-colour order. Supplement adds construction/calculation of mirror images, index as a speed ratio, $n=\sin i/\sin r$ for air into a material, $n=1/\sin\theta_c$ for material into air, and optical fibres including telecommunications. Monochromatic light as one frequency is Supplement.

The general two-index formulas explain when the simplified air formulas are valid. Apparent-depth calculations, slab displacement, Fermat and evanescent fields are enrichment. §3.2.3 also requires converging **and diverging** lenses, image construction, magnification uses and vision correction; reflection/refraction alone does not complete the entire light section.

### IB Physics — C.3 Wave Phenomena, SL and HL

The guide includes wavefronts and rays, reflection/refraction/transmission at boundaries, Snell in both speed-ratio and index forms, critical angle and TIR. These belong to the shared SL/HL content. Diffraction and interference elsewhere in C.3 remain distinct content, supported by [[Diffraction]] and [[Superposition and Interference]]. The calculus and evanescent-field sections are enrichment beyond these stated outcomes.

### AP Physics 2 — 13.1 Reflection and 13.3 Refraction

13.1 requires rays perpendicular to wavefronts, limits of geometric optics, the reflection law and the distinction between diffuse and specular reflection. 13.3 requires index, Snell, direction changes, normal incidence and the critical-angle/TIR conditions. The 2019 aquarium question is an older-format example whose ray reasoning remains relevant; its historical learning-objective codes are not current topic numbers. Mirrors and lenses have further imaging content in 13.2 and 13.4; this treatment does not claim to complete those topics.

### Where this is not a separate prescribed unit

The inspected **Cambridge 9702** syllabus does not prescribe a dedicated geometrical-optics/refraction unit; its wave and practical work can use prior knowledge from IGCSE. **AP Physics 1, AP Physics C: Mechanics and AP Physics C: Electricity and Magnetism** do not prescribe this ray-optics unit. Do not turn this conceptual bridge into additional claims of A-Level or AP-C syllabus coverage.

## Connections

- **Historical companion:** [[Ibn al-Haytham and the Question of Seeing]] — lamps, a dark room and testing how light reaches us.
- **Builds on:** [[Progressive Waves]] — wavefronts, $v=f\lambda$ and the boundary frequency invariant.
- **Teach together:** [[Polarisation]] — reflected intensity depends on the field's orientation, not just Snell's direction.
- **Light as a wave:** [[Diffraction]] and [[Superposition and Interference]] — where a ray-only picture stops being enough.
- **Technology:** [[Electromagnetic Spectrum]] — optical communication; [[Networks]] — the data carried by a physical link.
- **Mathematics:** [[Trigonometric Ratios]] — normals turn a physical direction question into sine ratios; [[Differentiation]] — stationary travel time.
- **Energy:** [[Energy Levels and Line Spectra]] — frequencies emitted by sources versus colours separated by a prism.

## LaTeX Reference

| Meaning | Expression | Condition |
|---|---|---|
| Refractive index | $n=c_0/v$ | Phase speed; dimensionless |
| Snell's law | $n_1\sin i=n_2\sin r$ | Angles from the normal |
| Wavelength ratio | $\lambda_2/\lambda_1=n_1/n_2$ | Stationary interface |
| Critical angle | $\sin\theta_c=n_2/n_1$ | $n_1>n_2$ |
| Apparent depth | $d_{\rm app}\approx d\,n_{\rm observer}/n_{\rm object}$ | Near-normal view, plane surface |
| Slab displacement | $s=t\sin(i-r)/\cos r$ | Parallel faces, same outside medium |

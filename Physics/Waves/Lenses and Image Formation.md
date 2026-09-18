---
chinese: 透镜与成像 (tòujìng yǔ chéngxiàng)
aliases:
  - Thin Lenses
  - Converging and Diverging Lenses
prerequisites:
  - "[[Reflection and Refraction]]"
leads_to: []
teach_together:
  - "[[Ibn al-Haytham and the Question of Seeing]]"
tags:
  - subject/physics
  - domain/waves
  - level/IGCSE
  - level/AP
  - level/university
  - curriculum/Cambridge-0625
  - curriculum/AP-Physics-2
  - syllabus/0625-3-2
  - syllabus/AP-Physics-2-13-4
  - type/deep
  - type/derivation
  - misconception/half-lens-half-image
  - misconception/virtual-means-invisible
---

# Lenses and Image Formation 透镜与成像

*Cover half a projector lens. Does half the picture disappear? Try predicting it before reading on. The answer exposes what an image actually is.*

A lens does not carry a little picture through the glass. It redirects light from **each object point** so that those rays meet again—or appear to have come from a new point. Repeat for every point, and you have an image.

## 中文锚点

投影仪上的字糊成一片时，转一转对焦环，字就清楚了。并不是机器突然画得更仔细了：原来从同一个小点发出的光，到了墙上还散成一小片；调好以后，这些光才在墙上重新聚到同一个点。每个点都各归各位，整幅画面就清晰了。透镜成像的关键，就是把四散的光重新安排好，让一个点对应一个点。

## 1. What the glass changes

[[Reflection and Refraction]] gives the local rule: light changes direction when it crosses between media of different refractive index. A curved lens has a different surface normal at each point. The two surfaces therefore give rays at different heights different changes of direction.

For ordinary glass surrounded by air:

- A **converging lens**, usually thicker in the middle, brings an initially parallel axial bundle towards one point.
- A **diverging lens**, usually thinner in the middle, spreads that bundle as though it had come from one point on the incident side.

Shape alone is insufficient: put a glass lens in a surrounding liquid with a higher refractive index than the glass, and its converging/diverging role can reverse. What matters is **index contrast and surface curvature**.

### The model and its vocabulary

We use an ideal **thin lens**: thickness is negligible compared with the object and image distances. We use **paraxial rays**: small angles to the axis, close enough to it that spherical aberration can be neglected. A real thick camera lens is more complicated.

| Term | Meaning |
|---|---|
| Principal axis 主光轴 | The line through the centres of curvature of a centred spherical lens |
| Optical centre 光心 | The point through which a ray passes undeviated in the thin-lens model, with the same external medium on both sides |
| Principal focus 主焦点 | The point where parallel axial rays meet after a converging lens, or from which they appear to diverge after a diverging lens |
| Focal length 焦距 | Distance from the thin lens to the principal focus; assigned a sign below |
| Focal plane 焦平面 | The plane through a focus perpendicular to the axis |

There is a focus on **each side**: reverse the light and the roles swap. For a lens in the same medium on both sides, the focal-length magnitudes are equal, even if the two surface curvatures differ. Different media on the two sides require a more general treatment.

A parallel bundle tilted to the principal axis focuses at a displaced point in the focal plane. The principal focus is specifically for the **axial** parallel bundle.

![[lenses-animation.mp4]]

*Follow the bundle, then move the object. At the focal distance the outgoing rays become parallel; the animation separates that case from the virtual-image case instead of making an image jump through a finite position. Distances and ray widths are illustrative.*

## 2. One point sends light through many parts of the lens

![[lenses-bundle.svg]]

The top object point sends light towards the top, centre **and bottom** of the lens. All those transmitted rays are redirected towards the same image point in the ideal model. The lower object point has its own bundle and its own image point.

That is why covering half the lens does **not** remove half the image. Each object point still has paths through the uncovered half. The image remains in the same place, at the same geometrical size, but receives less light. For a uniformly illuminated pupil in this ideal setup, blocking half its area approximately halves the transmitted power.

A real system can also vignette: oblique bundles may be clipped unequally, making image edges darker or cutting off part of the field. The basic half-lens result assumes the remaining opening still admits light from the whole object.

### Real and virtual describe paths, not visibility

A **real image** occurs where rays from a point actually converge. A screen there scatters the arriving light so that many observers can see the image. Remove the screen and the rays still cross; the screen does not create the focus.

A **virtual image** occurs where the backward extensions of outgoing rays intersect. No light from that bundle actually converges at that apparent location, so placing a screen there cannot capture that image directly. Your eye can still receive the diverging rays and focus them onto its retina; a camera can photograph it too.

**Actual rays: solid, arrows forwards. Backward extrapolations: dashed, no claim that light travels backwards.**

## 3. Three useful rays—not the only rays

To locate the image of an arrow's upper point, draw two independent rays; a third checks the construction. Begin all of them at the **same object point**.

| Incident ray | Converging lens | Diverging lens |
|---|---|---|
| Parallel to the axis | Leaves through the far focus | Leaves as if from the near focus |
| Through the optical centre | Continues straight | Continues straight |
| Through the near focus, or aimed along that line | Leaves parallel to the axis | — |
| Aimed towards the far focus | — | Leaves parallel to the axis |

For an object inside a converging lens's focal distance, the line through the near focus is extended **forwards from the object** to the lens. The ray need not physically pass through that focus first.

Find where the outgoing rays meet. If they spread apart, extend them backwards. Draw the image arrow from the axis to this meeting point. Repeat with another object point if the orientation is unclear.

![[lenses-atlas.svg]]

The coloured lines are selected members of a whole bundle. The diagrams use a thin-lens symbol: outward arrowheads indicate convergence, inward arrowheads divergence. Rays are clipped by the drawing boundary, not by an extra physical aperture.

## 4. The equation comes from the picture

### Choose a sign convention before substituting

Take light travelling left to right. These are the **real-positive** distances:

| Quantity | Positive | Negative |
|---|---|---|
| Object distance $u$ | Real object on incident side | Virtual object: incoming rays already converging towards a point beyond the lens |
| Image distance $v$ | Real image on outgoing side | Virtual image on incident side |
| Focal length $f$ | Converging lens | Diverging lens |
| Height $h$ | Above the principal axis | Below the principal axis |

Unless stated otherwise, our objects are real: $u>0$. Some textbooks use Cartesian signed coordinates instead, with the object coordinate negative; their equation looks different. **Never import one sign from a different convention.**

![[lenses-geometry.svg]]

**Step 1 — tool: similar triangles along the central ray.** The central ray is straight. For a real inverted image, its falling slope is the same on both sides:

$$\frac{h_i}{h_o}=-\frac vu.$$

The minus sign records inversion. Define signed transverse magnification:

$$\boxed{m=\frac{h_i}{h_o}=-\frac vu.}$$

**Step 2 — tool: similar triangles along the initially parallel ray.** This ray reaches the lens at height $h_o$ and passes through $(f,0)$. Its slope is $-h_o/f$. At the image position $x=v$, its height is therefore

$$h_i=h_o-\frac{h_o}{f}v,\qquad \frac{h_i}{h_o}=1-\frac vf.$$

**Step 3 — tool: both rays belong to the same point.** Equate the two expressions for the height ratio:

$$-\frac vu=1-\frac vf
\quad\Longrightarrow\quad
\boxed{\frac1f=\frac1u+\frac1v.}$$

The derivation used a real-image drawing. Signed straight-line equations extend it to virtual images and negative $f$; the dashed extensions obey the same line equations.

### Why the other rays agree

In the paraxial model a thin lens changes a ray's slope by $-y/f$, where $y$ is its height at the lens. This follows from the small-angle form of Snell's law at the two surfaces: the first-order angular change is proportional to height, and an axial parallel ray defines the proportionality constant $1/f$.

A ray from $(-u,h_o)$ arriving at height $y$ has incoming slope $(y-h_o)/u$. At distance $v$ after the lens its height is

$$y_{
m out}=y+v\left(\frac{y-h_o}{u}-\frac yf\right)
=y\left(1+\frac vu-\frac vf\right)-\frac vu h_o.$$

The lens equation makes the coefficient of $y$ zero. **Every admitted ray, regardless of where it meets the lens, reaches $h_i=-vh_o/u$.** That cancellation is image formation—and the mathematical reason the half-covered lens still works.

## 5. Moving the object: predict before calculating

Rearrange the equation:

$$v=\frac{fu}{u-f},\qquad m=-\frac f{u-f}.$$

For a converging lens with a real object:

| Object position | Image position | Image character | Familiar use |
|---|---|---|---|
| $u>2f$ | $f<v<2f$ | Real, inverted, diminished | Distant scene on a camera sensor |
| $u=2f$ | $v=2f$ | Real, inverted, same size | 1:1 reproduction geometry |
| $f<u<2f$ | $v>2f$ | Real, inverted, enlarged | Projector slide to wall |
| $u=f$ | No finite $v$ | Outgoing rays from each point are parallel | Collimator; relaxed-eye magnifier setting |
| $0<u<f$ | $v<0$ | Virtual, upright, enlarged | Magnifying glass |

At $u=f$, “image at infinity” is shorthand for **parallel output from each object point**. It does not mean a finite screen somewhere very far away is exactly in focus.

For a diverging lens, $f<0$ and $u>0$ give $v<0$ and $0<m<1$: virtual, upright, diminished, between lens and near focus. A diverging lens can form a real image when supplied with a sufficiently converging incident bundle—a virtual object—but not for the real objects in this table.

### Sensitivity near the focus

With fixed $f$,

$$\frac{dv}{du}=-\frac{f^2}{(u-f)^2}=-m^2.$$

The minus sign says bringing an outside-focus object closer moves the real image farther away. Near $u=f$, a tiny object displacement produces a huge image-distance change. This is why a projector's focus can feel delicate. [[Connected Rates of Change]] turns the same relation into velocities.

## 6. Where this is the working tool

### Camera and projector: the same geometry, different distances

For a distant scene, $1/u$ is nearly zero, so a camera's image plane is near $v=f$. Bring the subject closer and the required $v$ increases. Focusing adjusts the optics so the image falls on the sensor. A phone normally moves small lens groups; a zoom system also changes effective focal length. **Focus and zoom are different controls.**

A projector places its object just outside $f$, producing a large real image on a distant screen. The negative magnification means inversion about the axis in both transverse directions; digital projectors account for orientation electronically or optically.

The aperture controls which rays participate. If the sensor is misplaced, rays from one point land across a **blur circle**. A smaller aperture narrows that cone and reduces defocus blur, increasing depth of field. But it admits less light; eventually [[Diffraction]] spreads the spot more as the aperture shrinks. Smaller is not infinitely sharper.

### The eye focuses onto a fixed retina

The cornea provides much of the eye's refractive power. Accommodation changes the crystalline lens's shape and power to bring different object distances into focus on a retina whose position is approximately fixed. Focusing closer needs **more positive power**, not a retina moving backwards.

![[lenses-vision.svg]]

*An equivalent thin lens represents the eye's combined optics. These diagrams use a distant point and an unaccommodated model: real eyes differ in shape, refractive power and available accommodation.*

- **Myopia / short-sightedness 近视:** distant light would focus in front of the retina when accommodation is relaxed. A **diverging** correction reduces the incoming convergence, moving the final focus back to the retina.
- **Hyperopia / long-sightedness 远视:** the relaxed optical system would focus distant light behind the retina. A **converging** correction supplies positive power. Accommodation may compensate for some hyperopia; near viewing demands still more power and can become difficult.
- **Presbyopia 老视:** ageing reduces accommodation. Difficulty focusing near objects is not automatically the same condition as hyperopia, even though positive reading lenses can help in both situations.

### Lens power and a useful virtual image

For a lens in air, optical power is

$$\boxed{P=\frac1{f\text{ in metres}}}\quad\text{in dioptres (D = m}^{-1}\text{).}$$

A $+2.0\,\mathrm D$ lens has $f=+0.50\,\mathrm m$; a $-2.0\,\mathrm D$ lens has $f=-0.50\,\mathrm m$. Power adds approximately for thin lenses in contact; separation introduces an extra term.

Suppose an idealised myopic eye's far point is $0.50\,\mathrm m$ in front of it. A correcting lens close to the eye must make a distant object appear at that accessible point. With $u\to\infty$ and $v=-0.50\,\mathrm m$, the lens equation gives $f=-0.50\,\mathrm m$, hence $P=-2.0\,\mathrm D$. The virtual image is doing a real job: delivering the bundle the eye can focus. Actual prescriptions also account for lens position and other optical errors.

## 7. Worked examples — choose the ray logic first

### Cambridge 0625/41/M/J/24 Q4(a), (c): the magnifier and the eye

*Selected parts, paraphrased from the paper and checked against its published scheme.*

**Trigger:** the object must be viewed through a converging lens as a magnified virtual image. **Tool: the inside-focus construction.** Put the object between the lens and either principal focus; put the observer on the opposite side. Outgoing rays diverge; their backward extensions meet in an upright enlarged virtual image on the object's side.

For the focal-point definition, the input condition matters: **rays parallel to the principal axis converge at the principal focus after passing through a converging lens.** “Where rays meet” alone does not identify a principal focus; rays from a nearby object generally meet elsewhere.

**Trigger:** the correction uses a converging lens to bring the eye's image onto the retina. **Tool: added positive optical power.** It corrects long-sightedness in this model: the combined optical system has a shorter effective focal length, moving the focus forward onto the retina. Name the condition, explain the optical change, and identify the final focus.

### AP Physics 2, 2017 FRQ Q3(b–c): a projector on an optical bench

The object is $20\,\mathrm{cm}$ from a convex lens and its sharp screen image is $30\,\mathrm{cm}$ on the other side. We draw incident light left to right; the paper's bench drawing uses the opposite orientation.

**Trigger:** a sharp image exists on a screen. **Tool: real-image signs.** Use $u=+20\,\mathrm{cm}$ and $v=+30\,\mathrm{cm}$.

**Tool: thin-lens equation.**

$$\frac1f=\frac1{20}+\frac1{30}=\frac5{60},\qquad \boxed{f=12\,\mathrm{cm}}.$$

**Tool: signed magnification.**

$$m=-\frac{30}{20}=-1.5.$$

The image is inverted and its height magnitude is **1.5 times** the object's. The paper asks for magnification's magnitude, so the requested number is $1.5$; the negative sign in our convention supplies orientation.

**Tool: principal rays as an independent check.** Mark both foci $12\,\mathrm{cm}$ from the lens. Draw the upper-point parallel ray through the outgoing focus, and the central ray straight through. They meet $30\,\mathrm{cm}$ beyond the lens, below the axis at $1.5h_o$. Also note $12<20<24$: the object lies between $f$ and $2f$, exactly the enlarged-real-image regime.

### A magnifying glass: solve a negative distance honestly

An object stands $6.0\,\mathrm{cm}$ before a converging lens of focal length $10.0\,\mathrm{cm}$.

**Trigger:** $u<f$. Predict virtual and enlarged before calculation. **Tool: lens equation.**

$$\frac1v=\frac1{10}-\frac16=-\frac1{15}\quad\Rightarrow\quad v=-15\,\mathrm{cm},\qquad m=-\frac{-15}{6}=+2.5.$$

The image appears $15\,\mathrm{cm}$ on the incident side, upright and $2.5$ times as tall. Do not move a screen to that point and expect a sharp projection: the rays only **appear** to originate there.

## 8. Try it: measure a focal length

Use an illuminated printed arrow or LED object, converging lens, ruler and screen on one line. Never use the Sun or look through a lens at it.

1. Start with a real object well outside the focal distance. Move the screen until the image is sharp; check both top and bottom edges rather than choosing a merely bright patch.
2. Measure $u$ and $v$ from the thin lens's centre, keeping units consistent. Calculate $f=uv/(u+v)$.
3. Repeat with several object distances. The inferred $f$ should be approximately constant; include uncertainty from lens thickness, ruler resolution and judging sharpness.
4. Plot $1/v$ against $1/u$. The model predicts slope $-1$ and vertical intercept $1/f$: an application of [[Linearisation]]. This checks the relationship more strongly than one fortunate reading.
5. Cover half the lens without moving anything. Predict the image's position, size and brightness; then compare. Do not confuse dimming with loss of sharpness.

## Common Misconceptions

- **“The focus is wherever the image forms.”** Focus refers to an axial parallel input bundle. A finite-distance object usually has $v\ne f$.
- **“Only three rays leave the object.”** Those rays are construction shortcuts. The bundle-cancellation derivation explains the rest.
- **“A virtual image is invisible.”** Your eye receives the actual outgoing rays and locates their apparent source. Virtual means no actual convergence at that image position.
- **“A convex lens always makes a real image.”** Put a real object inside its focal length: the output diverges and the image is virtual.
- **“Cover the top half; lose the top half.”** Trace rays from the top object point through the bottom half. They still reach its image point.
- **“A negative answer means the arithmetic failed.”** With a declared convention it often means a virtual image or an inverted height. Interpret the sign before discarding it.
- **“A bigger linear image always looks bigger.”** Apparent size depends on the angle subtended at the eye. A magnifier's angular magnification is a separate comparison.

## Beyond Syllabus — making and combining lenses

### Curvature, index contrast and the lensmaker's equation

Recall that a lens changes ray slope by an amount proportional to height. Linearising Snell's law ($\sin\theta\approx\theta$) at its first and second spherical surfaces gives the thin-lens power in a surrounding medium:

$$\boxed{\frac1f=\left(\frac{n_{\rm lens}}{n_{\rm medium}}-1\right)\left(\frac1{R_1}-\frac1{R_2}\right).}$$

Here the same medium surrounds both sides; light travels left to right and a surface radius is positive when its centre of curvature lies to the **right** of that surface. A biconvex lens has $R_1>0$, $R_2<0$. The two curvature contributions then add to positive power when glass has the higher index.

To see where it comes from, let $n_m$ and $n$ denote the surrounding and glass indices. Small-angle Snell at the first surface gives $n\theta_g=n_m\theta_{\rm in}-(n-n_m)y/R_1$; at the second it gives $n_m\theta_{\rm out}=n\theta_g+(n-n_m)y/R_2$. Thinness lets us use the same height $y$ at both surfaces. Subtract the two equations: $\theta_{\rm out}-\theta_{\rm in}=-(n/n_m-1)(1/R_1-1/R_2)y=-y/f$.

This first-order expression omits lens thickness. Its structure is informative: flatten both surfaces and the power tends to zero; match the surrounding index to the glass and the refracting power disappears.

**Underwater is a revealing limit.** For glass of index $1.50$, changing the surrounding index from $1.00$ to $1.33$ reduces the power by the factor $(1.50/1.33-1)/(1.50-1)\approx0.256$. The focal length becomes about $3.91$ times larger.

At fixed object distance, a larger positive $f$ pushes a **still-real** image farther away and enlarges it—but only while $f<u$. If $f$ passes $u$, the real screen image is lost and the image becomes virtual. The water extension of AP's 2017 Q3 is a useful prompt, but its scoring-guide comparison of a farther, larger real image tacitly needs that regime condition. The supplied index ordering alone does not guarantee it.

### Two lenses: the first image is the second object

Recall that an image defines the point from which the next bundle comes—or towards which it is converging. Solve the first lens, then locate that point relative to the second lens. A real intermediate image before the second lens is a real object for it; a would-be image beyond the second lens is a virtual object, with $u_2<0$ in our convention. Multiply signed magnifications: $m_{\rm total}=m_1m_2$.

For separated thin lenses in air,

$$P_{\rm equivalent}=P_1+P_2-dP_1P_2,$$

**Why the separation term?** Send in a parallel ray at height $y$. Lens 1 gives it slope $-P_1y$. By lens 2 its height is $y(1-dP_1)$, so lens 2 adds slope $-P_2y(1-dP_1)$. The total is $-(P_1+P_2-dP_1P_2)y$, identifying the equivalent power.

Here $d$ is the separation in metres. The equivalent focal length is measured from the system's principal planes, not automatically from either piece of glass. At $d=0$, ordinary power addition returns.

A telescope uses an objective to form a real intermediate image and an eyepiece to present it at a comfortable viewing distance, often infinity. A compound microscope uses the same two-stage logic with a nearby object and a strongly enlarged intermediate image.

### Why a magnifier helps even with a relaxed eye

Recall that apparent size is angular size. A small object of height $h$ at the conventional reference near distance $D=25\,\mathrm{cm}$ subtends roughly $h/D$ radians. A magnifier with the object at its focal plane sends out bundles separated in angle by roughly $h/f$. Therefore relaxed-eye angular magnification is $M_\theta\approx D/f$.

The $25\,\mathrm{cm}$ reference is a conventional comparison distance, not every person's actual near point. With the eye close to the lens and the virtual image placed at that reference near point, $M_\theta\approx1+D/f$ instead. Neither expression is the transverse $m=-v/u$ of a finite image.

### Why real photographs still have imperfections

Spherical surfaces do not focus all large-angle rays at one point (**spherical aberration**). Glass's index depends on wavelength, so colours focus differently (**chromatic aberration**). Multiple elements, chosen glass types and aspheric surfaces reduce these defects; a single ideal thin lens hides them. The remaining diffraction limit is wave physics, not a poorly drawn ray.

## Exam Notes

### Cambridge 0625 IGCSE — §3.2.3 Thin lenses

**Core:** effects of converging and diverging lenses on a parallel beam; focal length, principal axis and principal focus; converging-lens real-image ray constructions; image size, orientation and real/virtual descriptions; virtual images as apparent ray origins that cannot be formed directly on a screen.

**Supplement:** converging-lens virtual-image diagrams, the magnifying glass, and converging/diverging correction of long-/short-sightedness. The thin-lens equation, dioptres, lensmaker's equation and angular magnification are not prescribed outcomes here. A good diagram needs a ruler, clear focal positions, ray directions and dashed virtual extensions—not a remembered arrow shape.

Verified example: **0625/41/M/J/24 Q4(a), (c)**. The focal-point definition earns its meaning from **parallel to the principal axis**; the magnifier has an object inside the focal length and an eye on the other side; the correction explanation ends with focus on the retina.

### AP Physics 2 — Unit 13, Topic 13.4 Lenses

LO **13.4.A**, EK **13.4.A.1–A.7**: converging/diverging lenses, real/virtual images, the thin-lens relationship, signed locations, foci on both sides, magnification and the principal-ray constructions for image type, size and orientation. In the symmetric surrounding medium used here, front and back focal lengths have equal magnitudes; unequal surface shapes alone do not make them different.

The CED writes magnification as an image/object size ratio. We use signed heights and $m=-v/u$; when a question requests **magnitude**, report $\lvert m\rvert$ and state orientation separately. Verified example: **2017 FRQ Q3(b–c)**, $f=12\,\mathrm{cm}$ and magnification magnitude $1.5$.

### Not a prescribed lens-imaging topic on these courses

**Cambridge 9702 (2028–30), IB Physics (first assessment 2025), AP Physics 1, AP Physics C: Mechanics, and AP Physics C: Electricity and Magnetism** do not prescribe this thin-lens image-construction/equation sequence. IB C.3 includes refraction; 9702 includes wave optics and optical applications, which is not the same claim as a dedicated lens unit. Lensmaker, separated-lens power and angular-magnification derivations above are enrichment rather than blanket requirements for every named board.

For further reading: OpenStax’s [thin-lens treatment](https://openstax.org/books/university-physics-volume-3/pages/2-4-thin-lenses) and [optics of the eye](https://openstax.org/books/university-physics-volume-3/pages/2-5-the-eye).

## Connections

- **Parent:** [[Reflection and Refraction]] — surface-by-surface direction changes; virtual images already appear in mirrors and water.
- **Human companion:** [[Ibn al-Haytham and the Question of Seeing]] — follow light into the eye and test what an image tells you.
- **Experimental tool:** [[Linearisation]] — reciprocal-distance graph with intercept $1/f$.
- **Changing geometry:** [[Connected Rates of Change]] — object motion changes image distance nonlinearly.
- **Limit of the ray model:** [[Diffraction]] — a smaller opening eventually broadens the image of a point.

---

## LaTeX Reference

| Meaning | LaTeX |
|---|---|
| Thin-lens equation | `\frac1f=\frac1u+\frac1v` |
| Signed transverse magnification | `m=\frac{h_i}{h_o}=-\frac vu` |
| Magnification magnitude | `\lvert m\rvert` |
| Optical power | `P=1/f` with $f$ in metres |

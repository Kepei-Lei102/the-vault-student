---
chinese: 偏振 (piānzhèn)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Electromagnetic Spectrum]]"
  - "[[Vectors]]"
leads_to: []
teach_together:
  - "[[Reflection and Refraction]]"
tags:
  - subject/physics
  - domain/waves
  - level/A-Level
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/AP-Physics-2
  - syllabus/9702-7-5
  - syllabus/AP-Physics-2-14-3
  - type/deep
  - type/definition
  - type/proof
  - notation/malus-law
  - misconception/polarisation-is-the-direction-of-travel
  - misconception/intensity-is-amplitude
  - misconception/more-filters-always-means-less-light
  - misconception/unpolarised-means-no-oscillation
---

# Polarisation 偏振

> Put two polarising sheets in front of a lamp. Turn one until the view goes dark. Now slide a third sheet **between** them, tilted halfway between their axes. Light comes back. You added something that absorbs light, and the view got brighter. The missing idea is that a filter changes the light that survives it.

## Definition

### Formal

**Polarisation** describes the directional behaviour of a transverse wave's oscillations. A wave is **linearly (plane-) polarised** when its oscillations stay along one fixed line perpendicular to the direction of propagation.

For light travelling along $z$, we specify polarisation by the **electric field**: a vertically polarised wave has an electric field oscillating up and down. Its magnetic field is also transverse, perpendicular to both the electric field and propagation direction.

**Unpolarised light** has no persistent preferred transverse electric-field direction over the observation time. It still oscillates and carries energy. **Partially polarised light** lies between the completely unpolarised and completely polarised cases.

### Intuitive

A wave has two different questions to answer: **where does the pattern travel, and in which direction does it wiggle?** Polarisation answers the second.

Imagine a rope stretched away from you. Shake it vertically; now shake it horizontally. The disturbance travels along the same rope in both cases, but the transverse motion differs. A narrow vertical guide can allow the vertical motion while suppressing the horizontal motion. Rotating the guide tests the direction of the wiggle.

Sound in air is longitudinal: the air moves back and forth **along** the direction of propagation. There is no independent sideways orientation to select. This is why polarisation is evidence for a wave's **transverse** nature. Solids can also carry transverse elastic waves; the statement is about wave type, not a blanket ban on all mechanical waves.

### 中文锚点

隔着偏光太阳镜看液晶屏，慢慢转动镜片，画面可能会暗下去，甚至几乎看不见。屏幕没关，是光除了“往哪走”，还有电场“朝哪个方向振动”。镜片像一道方向筛子，只让沿着透光轴的分量通过；镜片一转，能通过的分量就变了。偏振这个听起来抽象的词，就藏在你转动镜片时那一明一暗里。

## Notation

| Symbol / term | Meaning | Keep distinct from |
|---|---|---|
| $E_0$ | incident electric-field amplitude, in V m$^{-1}$ | intensity or photon energy |
| $I_0$, $I$ | incident and transmitted intensity, in W m$^{-2}$ | total power, measured in W |
| $\theta$ | angle between incoming linear polarisation and the filter's **transmission axis** | angle to the surface normal |
| Polariser / analyser | a filter used to prepare / examine a polarisation state | two different kinds of material |
| Transmission axis | transverse direction whose electric-field component is passed | direction of travel |

The labels *polariser* and *analyser* describe jobs. The same sheet can do either. American spelling is **polarization**.

## Key Facts — a filter takes a projection

![[polarisation-see-it-change.mp4]]

Watch the field component shrink as the angle grows, then insert a third filter between a crossed pair. The intensity shown is relative to the already polarised input.

### 1. What an ideal linear polariser does

Resolve the incident electric field into components parallel and perpendicular to the transmission axis. The ideal filter passes the parallel component and rejects the perpendicular component:

$$E_{\parallel,0}=E_0\cos\theta,\qquad E_{\perp,0}=E_0\sin\theta.$$

The transmitted light is now polarised **along the filter's axis**, irrespective of the incoming angle, provided some light gets through. An axis is a line: $0^\circ$ and $180^\circ$ describe the same transmission direction.

The rope-and-slot picture captures the selection, but a sheet polariser does not contain visible slots. In an absorbing polariser, aligned material responds differently to the two field components, preferentially absorbing one. A wire-grid polariser illustrates the microscopic distinction: the electric field **parallel to the wires** drives charges along them and is largely rejected; the transmitted electric field is perpendicular to the wires. Do not confuse a drawing of the transmission axis with a drawing of the absorbing structure.

Rejected energy is absorbed or redirected, depending on the device. **Ideal** here means full transmission along the pass axis and zero leakage along the blocked axis. Real devices lose some wanted light and leak some unwanted light. [Edmund Optics: polariser mechanisms](https://www.edmundoptics.com/knowledge-center/application-notes/optics/introduction-to-polarization).

### 2. Why Malus's law has a square

**Trigger:** a linearly polarised beam meets a linear analyser at a known relative angle.

**Tool 1 — vector projection:** the transmitted field amplitude is $E_0\lvert\cos\theta\rvert$. The absolute value matters because *amplitude* is non-negative; a negative signed component reverses phase.

**Tool 2 — intensity is proportional to amplitude squared:** at fixed frequency and in the same medium, $I\propto E_0^2$. The electric and magnetic energy densities are quadratic in their fields; time-averaging changes the common factor, not the square.

Take the ratio so the shared proportionality constant cancels:

$$\frac{I}{I_0}=\frac{E_0^2\cos^2\theta}{E_0^2}.$$

Therefore **Malus's law** is

$$\boxed{I=I_0\cos^2\theta.}$$

![[polarisation-projection-and-malus.svg|850]]

*Left: a view looking along the beam, with the filter axis horizontal. The dashed segment completes the projection triangle. Right: intensity repeats every $180^\circ$ because an axis has no preferred arrow direction.*

| Relative angle | Amplitude fraction | Intensity fraction | Interpretation |
|---|---|---|---|
| $0^\circ$ | $1$ | $1$ | aligned: ideal full transmission |
| $30^\circ$ | $\sqrt3/2$ | $3/4$ | projection first, then square |
| $45^\circ$ | $1/\sqrt2$ | $1/2$ | half intensity, not half amplitude |
| $60^\circ$ | $1/2$ | $1/4$ | half amplitude gives quarter intensity |
| $90^\circ$ | $0$ | $0$ | crossed: extinction |

The filter reduces the number of transmitted photons per second; it does not reduce each surviving photon's energy to $hf\cos^2\theta$. The transmitted light retains its frequency. [[Wave-Particle Duality]] connects that frequency to photon energy.

### 3. Through a sequence, update the state every time

Suppose the incoming plane of polarisation has angle $\phi_0$ and successive axes have angles $\phi_1,\ldots,\phi_N$, all measured from the same reference in the transverse plane. Then

$$\boxed{I_N=I_0\prod_{j=1}^{N}\cos^2(\phi_j-\phi_{j-1}).}$$

Why the **adjacent differences**? Filter 1 prepares light along $\phi_1$. Filter 2 receives that light, not the original state along $\phi_0$. Each output is the next input.

The practical algorithm is simply: **relative angle → new intensity → new direction → next filter**.

### 4. The third-filter surprise

Take vertically polarised light with intensity $I_0$. A horizontal analyser blocks it. Insert a $45^\circ$ polariser **before** that horizontal analyser:

$$I_1=I_0\cos^245^\circ=\frac{I_0}{2},\qquad
I_2=\frac{I_0}{2}\cos^245^\circ=\boxed{\frac{I_0}{4}}.$$

The inserted filter passes a diagonal component. That diagonal field has a horizontal component, so the final filter now has something to transmit. If the new filter were placed **after** the horizontal analyser, it would receive no light and could not restore any.

![[polarisation-third-filter.svg|850]]

*Intensity is measured relative to the already vertically polarised input. No step increases the intensity entering it. The comparison is between two different optical arrangements.*

For a middle axis at angle $\alpha$ to the vertical,

$$\frac{I_{\text{out}}}{I_0}=\cos^2\alpha\cos^2(90^\circ-\alpha)
=\frac14\sin^2(2\alpha).$$

Since $\sin^2(2\alpha)\leq1$, the largest possible output is $I_0/4$, reached at $\alpha=45^\circ$ between $0^\circ$ and $90^\circ$.

### 5. Unpolarised input — a different starting condition

> [!info] Extension beyond Cambridge's required intensity calculation
> An ideal first polariser transmits **half** the intensity of completely unpolarised light. That is an average over directions, not Malus's law with a randomly chosen single angle.

Averaging over equally represented transverse directions gives

$$\left\langle\cos^2\theta\right\rangle
=\frac1\pi\int_0^\pi\cos^2\theta\,d\theta=\frac12,$$

because $\cos^2\theta=(1+\cos2\theta)/2$ and the oscillating term averages to zero. Equivalently, two orthogonal components of an unpolarised beam carry equal average intensities, and the filter selects one.

Thus unpolarised input $I_u$ followed by axes $0^\circ,45^\circ,90^\circ$ gives $I_u/2$, then $I_u/4$, then $I_u/8$. **Do not halve again at every filter:** after the first, the light is polarised and the relative-angle rule applies.

## Where It Works — controlling what reaches your eye

### Sunglasses and camera filters: reject the glare

Reflection from a non-metallic surface usually favours one polarisation. Glare from a horizontal water surface or wet road often has a strong horizontal electric-field component. Sunglasses with a vertical transmission axis suppress that component while retaining more of the useful scene. Tilting the glasses changes this advantage; simply darkening every component would not distinguish glare from the rest of the view.

Try looking at a reflection on water through a polarising lens and slowly rotating it. The reflected image changes in brightness. The effect depends on viewing angle and material; it is not a promise that every reflection vanishes. [Exploratorium: Polarized Sunglasses](https://www.exploratorium.edu/snacks/polarized-sunglasses).

### LCDs: electricity operates a light valve

A simple **normally-white twisted-nematic LCD** places a liquid-crystal layer between crossed polarisers. The first prepares linear light. With no applied voltage, the suitably designed twisted layer rotates its polarisation by about $90^\circ$, so it passes the second filter. An applied electric field changes the molecules' orientation; the layer no longer produces that rotation, so the second filter blocks the light. Intermediate control produces intermediate brightness.

The liquid crystal changes the **polarisation**, and the analyser converts that change into **brightness**. The backlight supplies the light; the pixel controls transmission. Other LCD modes use different arrangements, so this on/off sequence is a specific design, not a universal rule for every display. [Sharp: the TN LCD operating principle](https://jp.sharp/products/lcd/tech/s2_1.html).

This also explains why some LCD screens become very dark when viewed through rotated polarising sunglasses. The sunglasses act as an extra analyser. Screens with additional optical films need not go completely black.

### Stressed plastic: make an invisible difference visible

Place suitable transparent plastic between crossed polarisers and gently flex it. Stress can make its refractive index different for two perpendicular polarisation components: **birefringence**. Those components accumulate different phases while crossing the plastic. The output polarisation changes, so some light can now pass the analyser.

The phase delay depends on wavelength, so white light produces colours. This is **photoelasticity**, used to examine stress distributions in transparent models and components. A colour is not a universal stress reading: thickness, material calibration and the polariser arrangement matter. [Exploratorium: Bone Stress](https://www.exploratorium.edu/snacks/bone-stress).

## Worked Examples — trace the light forwards

The questions below are paraphrased from the named papers; answers were checked against their published mark schemes.

### 1. Two filters, two different angles — 9702/22/M/J/23 Q5(c)

Vertically polarised light has intensity $8.5\ \mathrm{W\,m^{-2}}$. The first axis is $35^\circ$ to the vertical; the second is at $\alpha$, with $35^\circ<\alpha<90^\circ$. The final intensity is $5.2\ \mathrm{W\,m^{-2}}$. Find $\alpha$.

**Step 1 — tool: Malus's law; trigger: the first incoming direction is vertical.**

$$I_1=8.5\cos^235^\circ=5.7036\ldots\ \mathrm{W\,m^{-2}}\approx5.7\ \mathrm{W\,m^{-2}}.$$

**Step 2 — tool: update the polarisation; trigger: there is a second filter.** Its input is now along $35^\circ$, so its angle is $\alpha-35^\circ$:

$$5.2=I_1\cos^2(\alpha-35^\circ).$$

**Step 3 — tool: inverse cosine, with the stated interval selecting the branch.**

$$\alpha-35^\circ=\cos^{-1}\sqrt{\frac{5.2}{I_1}}\approx17.3^\circ,
\qquad\boxed{\alpha\approx52^\circ.}$$

Using the intermediate $5.7$ gives the same final rounding. The scheme awards **1 mark** for the first intensity and **2** for the second-filter relation and angle. Using $\cos^2\alpha$ at the second filter would ignore the state prepared by the first.

### 2. It starts crossed — 9702/23/M/J/25 Q5

A plane-polarised beam meets an analyser initially **perpendicular** to its polarisation. The analyser rotates through angle $\alpha$ from that position. Sketch transmitted intensity through a full turn, then find the transmitted amplitude at $\alpha=20^\circ$.

**Step 1 — tool: distinguish rotation from relative angle.** The initial relative angle is $90^\circ$, so

$$I=I_0\cos^2(90^\circ-\alpha)=\boxed{I_0\sin^2\alpha}.$$

The graph starts at zero, peaks at $90^\circ$ and $270^\circ$, and returns to zero at $180^\circ$ and $360^\circ$. It is a smooth squared-sine curve, not a triangular zigzag. The sketch has **3 marks** for range/periodicity, shape and correctly placed peaks/troughs.

**Step 2 — tool: $I\propto A^2$; trigger: the requested quantity is amplitude.** At $20^\circ$, the relative angle is $70^\circ$:

$$\frac{I}{I_0}=\cos^270^\circ=0.117\ldots,
\qquad\frac{A}{A_0}=\sqrt{\frac{I}{I_0}}=\cos70^\circ=\boxed{0.34}.$$

The **4-mark** amplitude calculation distinguishes the intensity law, the amplitude relation, the correct angle and the final value. Q5(a)'s **1 mark** asks why sound cannot be polarised: it is longitudinal, whereas polarisation requires transverse oscillations.

### 3. Dim the fringes without moving them — 9702/21/O/N/25 Q4(c)

Vertically polarised light illuminates a diffraction grating. Insert a polariser with its axis $45^\circ$ to the vertical before the grating. What changes on the screen?

**Tool: separate the quantities that set positions from those that set brightness.** The filter leaves $\lambda$ and the grating spacing $d$ unchanged, so the maxima still satisfy $d\sin\theta=n\lambda$ at the same angles. But

$$I_{\text{new}}=I_{\text{old}}\cos^245^\circ=\tfrac12 I_{\text{old}}.$$

**Same peak positions; every peak has half its former intensity** in the question's ideal model. The scheme assigns **one mark to each claim**. [[Diffraction]] derives the grating condition; the two laws do different jobs.

### 4. Design a dimmer — extension

Already vertically polarised light must emerge horizontally polarised. You may use one intermediate linear filter and a final horizontal filter. Which intermediate angle maximises the output?

**Tool: the adjacent-angle product; trigger: the final direction is fixed but the intermediate direction is adjustable.** As derived above, $I_{\text{out}}/I_0=\tfrac14\sin^2(2\alpha)$. The maximum is **one quarter at $45^\circ$**. A direct horizontal filter would transmit zero. The change is possible because the intermediate filter prepares a different input for the final one.

## Common Misconceptions

- **“Vertically polarised light travels vertically.”** Draw two arrows: propagation along the beam, electric-field oscillation across it. They are perpendicular.
- **“Use the marked angle in $\cos^2$.”** First identify what the angle is measured from. An analyser rotated from extinction produces a $\sin^2$ graph.
- **“Half the intensity means half the amplitude.”** Take the square root: half intensity means amplitude $1/\sqrt2$ of the original.
- **“Every filter halves the light.”** That rule is for completely unpolarised input and an ideal first filter. An aligned ideal analyser passes all of an already linearly polarised beam; a crossed one passes none.
- **“A third filter makes energy.”** Follow the intensity along either arrangement: it never increases. Inserting a filter before the last one changes the state the last one receives.
- **“No brightness change on rotating an analyser proves the light is unpolarised.”** Circularly polarised light also gives constant transmission through a rotating linear analyser. One test is insufficient; see below.

## Exam Notes

### Cambridge 9702 — AS §7.5

Two outcomes: associate polarisation with **transverse** waves; recall and use **$I=I_0\cos^2\theta$** for a plane-polarised beam passing through one filter or a **series** of filters. AS Papers 1/2 examine this content, which remains assumed knowledge at A Level.

The syllabus explicitly says that calculating a polariser's effect on **unpolarised** intensity is **not required**. The half-intensity derivation is useful enrichment; it is not an extra Cambridge requirement. Circular/elliptical polarisation, Brewster's law and Jones matrices below are also extensions. Malus's law is a **recall** outcome; it is absent from the supplied AS formula list in these papers.

### AP Physics 2 — §14.3

**14.3.A.2–A.3:** transverse waves can be polarised through interactions including reflection, refraction and passage through appropriate structures; longitudinal waves cannot. Polarisation may reduce intensity; intensity is time-averaged power per unit area. These are qualitative outcomes: the current CED does **not** state a Malus-law calculation requirement.

**The rest of 14.3 is boundary behaviour:** transmitted and reflected waves, unchanged frequency across the boundary, and inversion/non-inversion of reflected pulses at string joins. Polarisation alone does not complete that entire topic. [[Progressive Waves]] and [[Stationary Waves]] supply existing boundary examples; the finite string-join case is a distinct extension.

### Where it is not examined

**Cambridge 0625**, the **IB Physics first-assessment-2025 guide**, **AP Physics 1**, and **AP Physics C: Mechanics / Electricity & Magnetism** do not specify this wave-polarisation treatment. In AP E&M, *electric polarisation of matter* means displaced bound charges: it is a different use of the word. The familiar appearance of polarisation in older IB courses is not evidence for a current outcome. The Vault's mathematics syllabuses supply the vector/trigonometric tools, not a separate optics requirement.

## Beyond Syllabus — what a single direction leaves out

### Linear, circular and elliptical light

Recall that light has two independent transverse field components. Write a monochromatic wave travelling along $z$ as

$$E_x=A\cos(kz-\omega t),\qquad
E_y=B\cos(kz-\omega t+\delta).$$

At one fixed position, follow the end of the electric-field vector through time:

- $\delta=0$ or $\pi$: the components stay in a fixed ratio, tracing a **line**.
- $A=B$ and $\delta=\pm\pi/2$: one component is largest when the other is zero, tracing a **circle**.
- Other non-degenerate amplitude/phase combinations generally trace an **ellipse**.

Circular light is fully polarised: its electric field rotates in an organised way. It is not an unpolarised jumble, and the light ray does not spiral through the room. An ideal linear analyser transmits half its intensity at **every** axis angle, which is why rotating that analyser alone cannot distinguish circular from unpolarised light.

A **quarter-wave plate** delays one perpendicular component relative to the other by a quarter cycle. Linear input at $45^\circ$ to its principal axes supplies equal amplitudes; the delay turns it into circular light. Its action changes relative phase, rather than discarding a component like an absorbing polariser. [Czech Technical University: waveplate experiment](https://physics.fjfi.cvut.cz/~schmijos/en/waves/experiments/waveplates.php).

For thickness $d$, vacuum wavelength $\lambda_0$ and refractive-index difference $\Delta n$, the relative phase delay is $\delta=2\pi\Delta n\,d/\lambda_0$: each component accumulates $2\pi n d/\lambda_0$ of phase, and subtraction leaves the difference. A quarter-wave plate has $\lvert\delta\rvert=\pi/2$ modulo a full cycle at its design wavelength. This also explains why stressed plastic produces wavelength-dependent colours.

### Brewster's angle: reflection becomes a polariser

Recall the sunglasses' selective rejection of glare. At an ideal boundary between transparent, non-magnetic dielectrics, the reflected component with electric field **in the plane of incidence** vanishes at the **Brewster angle**. That plane contains the incoming ray and the surface normal. Unpolarised incident light then gives reflected light polarised perpendicular to that plane; the transmitted beam is generally only partially polarised.

The electromagnetic boundary conditions give $\theta_B+\theta_t=90^\circ$ at this point. Combining this result with Snell's law,

$$n_1\sin\theta_B=n_2\sin\theta_t=n_2\cos\theta_B
\quad\Rightarrow\quad\boxed{\tan\theta_B=\frac{n_2}{n_1}}.$$

For air to water, $n_1\approx1$, $n_2\approx1.33$, so $\theta_B\approx53^\circ$ **from the normal**. The derivation of the perpendicular-ray condition requires the Fresnel boundary equations; geometry alone does not prove it. Metals and absorbing media need the fuller theory. [Edmund Optics: polariser selection and Brewster reflection](https://www.edmundoptics.com/knowledge-center/application-notes/optics/polarizer-selection-guide).

### The linear-algebra view: order matters

Recall that a polariser projects a vector. If its unit transmission direction is $\mathbf u$, its action on the transverse field is

$$\mathbf E_{\text{out}}=\mathbf u(\mathbf u^{\mathsf T}\mathbf E_{\text{in}}),
\qquad P_{\mathbf u}=\mathbf u\mathbf u^{\mathsf T}.$$

In horizontal/vertical coordinates,

$$P_H=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
P_V=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
P_{45}=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Then $P_HP_V=0$, but

$$P_HP_{45}P_V=\frac12\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0.$$

Applied to unit vertical input, the latter gives horizontal amplitude $1/2$, hence intensity $1/4$. **Matrix multiplication records the optical order, from right to left.** This is the beginning of Jones calculus, which uses complex field amplitudes to include phase delays. It describes coherent fully polarised light; unpolarised mixtures need a statistical description.

## Connections

- **Parents:** [[Progressive Waves]] distinguishes oscillation from propagation and develops $I\propto A^2$; [[Electromagnetic Spectrum]] identifies the transverse electric/magnetic fields; [[Vectors]] supplies projection.
- **Mathematical engine:** [[3D Vectors and the Scalar Product]], [[Matrix Transformations]] — projections as geometric operations and matrices.
- **Phase bridge:** [[Superposition and Interference]] — two perpendicular components acquire a relative phase; an analyser brings components onto a common axis so interference can affect brightness.
- **Materials bridge:** [[Stress, Strain and Young Modulus]] — mechanical stress becomes optically visible through photoelasticity.
- **Quantum bridge:** [[Wave-Particle Duality]] — attenuation changes photon flux, not the frequency of each transmitted photon.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $I=I_0\cos^2\theta$ | `I=I_0\cos^2\theta` | Malus's law; relative angle |
| $E_0\lvert\cos\theta\rvert$ | `E_0\lvert\cos\theta\rvert` | transmitted field amplitude |
| $\phi_j-\phi_{j-1}$ | `\phi_j-\phi_{j-1}` | successive transmission-axis difference |
| $\langle\cos^2\theta\rangle=1/2$ | `\langle\cos^2\theta\rangle=1/2` | average for unpolarised light |
| $\delta$ | `\delta` | phase difference between transverse components |
| $\tan\theta_B=n_2/n_1$ | `\tan\theta_B=n_2/n_1` | Brewster's law for the stated ideal interface |
| $P_{\mathbf u}=\mathbf u\mathbf u^{\mathsf T}$ | `P_{\mathbf u}=\mathbf u\mathbf u^{\mathsf T}` | linear-polariser projection matrix |

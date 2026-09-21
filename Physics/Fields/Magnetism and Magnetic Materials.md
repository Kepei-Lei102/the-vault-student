---
chinese: 磁性与磁性材料 (cíxìng yǔ cíxìng cáiliào)
aliases:
  - 磁性与磁性材料
  - Simple Magnetism
prerequisites:
  - "[[Newton's Laws of Motion]]"
leads_to:
  - "[[Lorentz Force]]"
  - "[[Secondary Storage]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - level/AP
  - level/university
  - syllabus/0625-4-1
  - syllabus/0625-4-5
  - syllabus/9702-20-1
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - type/deep
  - misconception/all-metals-are-magnetic
  - misconception/attraction-proves-a-magnet
  - misconception/field-lines-are-physical-strings
  - misconception/soft-means-mechanically-soft
---

# Magnetism and Magnetic Materials 磁性与磁性材料

> A magnet picks up a nail. The nail picks up another nail. Neither nail has a battery. Remove the magnet: one chain falls apart, while another may keep hanging. The difference is not whether the atoms possess magnetism. It is how a crowd of tiny magnetic moments organises itself—and how much of that organisation survives afterwards.

## Definition — what a magnet does

A **magnet** produces a magnetic field and has north and south polarity. Two like poles repel; unlike poles attract. A **magnetic field** is a vector field describing magnetic influence throughout space: it determines forces on moving charges, currents and magnetic dipoles.

For an operational starting point, place a small compass at a point. Its north-seeking end indicates the local field direction when the needle settles. A freely turning compass usually **rotates** into alignment; it need not travel bodily toward the source.

A **magnetic material** in everyday language is something such as iron that responds strongly to an ordinary magnet. It need not already be a permanent magnet. Physics also studies much weaker responses, so “non-magnetic” is a practical classification, not the claim of absolutely zero magnetic response.

### 中文锚点

磁铁吸住一根回形针，回形针下面又能挂上一根，好像它也临时学会了吸东西。不是磁铁把什么东西传了过去，而是回形针内部原本朝向不同的许多小片区域，在外来磁场的影响下，更偏向同一个方向，于是整根回形针也显出了磁性。拿走磁铁后，有的材料很容易失去这种整体上的整齐，有的却能保留不少。临时磁铁和永久磁铁的区别，就藏在这件事里：外来的影响撤走了，里面的排列还能留下多少。

## The vocabulary you will actually use

| English | 中文 | Meaning |
|---|---|---|
| magnetic pole | 磁极 | north or south polarity of a magnet |
| induced magnetism | 感应磁化 | a material becomes magnetised in an applied magnetic field |
| temporary / permanent magnet | 临时 / 永久磁铁 | readily loses / substantially retains magnetisation after removal of the applied field |
| magnetic domain | 磁畴 | region with a common direction of magnetisation |
| magnetisation $M$ | 磁化强度 | magnetic dipole moment per unit volume |
| permeability $\mu$ | 磁导率 | relates $B$ to $H$ in a specified material response |
| remanence | 剩磁 | magnetisation or flux density remaining at zero applied magnetising field, with the quantity specified |
| coercivity | 矫顽力 | reverse field needed to bring a specified magnetic quantity to zero after magnetisation |

## 1. Poles: why attraction is an ambiguous test

Place the N end of a known magnet near an unknown rod.

- **Repulsion:** that end of the rod is an N pole of a magnet.
- **Attraction:** it might be an S pole, **or an initially unmagnetised piece of iron**.

Why can iron fool the test? The external field magnetises it. Near an approaching N pole, the near end of the iron becomes S; the far end becomes N. The nearer unlike poles attract more strongly than the farther like poles repel because the field changes with distance. Reverse the source magnet and the induced poles reverse too: attraction remains.

The force is an interaction between the magnetic systems and their fields. A changed arrangement can lower the combined magnetic energy; the field description predicts the resulting force, without requiring contact.

This is **induced magnetism**, not electromagnetic induction. The latter concerns an induced emf associated with changing magnetic flux ([[Electromagnetic Induction]]). A stationary permanent magnet can magnetise stationary iron without generating a sustained electric current through it.

![[magnetism-induced-chain.svg|700]]

**Cutting does not separate N from S.** Each surviving piece of a magnet has both polarities. You uncover new ends of an already magnetised material; you do not isolate a magnetic charge. No isolated magnetic monopole has been experimentally established. Ordinary magnetism is described by dipoles and closed magnetic flux, even when a pole model is a useful shortcut.

## 2. Drawing a field: a map, not a bundle of strings

A field line is a curve tangent to $\mathbf B$ at every point. Arrows show the direction in which the N end of a small compass points.

1. Outside a bar magnet, arrows run **N to S**.
2. Inside, the field continues **S to N**: the lines do not stop at the surface.
3. More closely spaced lines in a consistently drawn diagram represent a stronger field.
4. Two field lines cannot cross at a point where the field is nonzero: crossing would assign two directions to the same vector. At a zero-field point the direction is undefined.
5. The field occupies the space *between* the drawn lines too. The number of lines an illustrator chooses is not a physical count.

![[magnetism-field-map.svg|700]]

*The exterior curves above come from a finite-solenoid model of a bar magnet. The interior return arrow completes the loop schematically; the blue curves are tracing paths, not physical threads.*

A compass responds to the **resultant** field: magnet plus Earth plus nearby currents. Far enough from a small magnet, Earth's contribution can dominate. At some positions two contributions may cancel; a needle there cannot reliably tell you the direction of the magnet's field alone.

Earth's large-scale field is approximately dipolar. Near geographical north, field lines enter Earth, so that region has **south magnetic polarity** in the bar-magnet sense. The geographical name “North Magnetic Pole” identifies a location; it does not mean an N pole of a bar magnet would be repelled there. The real geomagnetic field is produced by moving conducting fluid, not a permanent iron bar inside Earth.

### Plot it with a compass

Fix a bar magnet under or on a sheet of paper and mark its outline. Put a small plotting compass beside it and mark both ends of the needle. Move the compass so its trailing end sits on the previous forward mark. Mark the new forward end; repeat. Join the marks smoothly and add an arrow toward the compass's N end. Start elsewhere to trace several lines.

**Iron filings provide shape, not arrow direction.** Put paper over the magnet, sprinkle filings sparingly and tap gently. Each filing becomes a tiny induced magnet and tends to align with the local field. Chains reveal a pattern. Use a compass to add directions. Filings disturb the field and cluster, so their density is only qualitative evidence, not a calibrated measurement of $B$.

## 3. The microscopic crowd: domains

Electrons have magnetic moments from quantum spin and orbital motion. **Spin is intrinsic angular momentum, not a literal charged ball spinning on an axle.** In many atoms the contributions substantially cancel; the existence of electrons alone does not make everything a strong magnet.

In a ferromagnet below its Curie temperature, quantum **exchange interactions** favour collective alignment. Within a **domain**, many atomic moments share a direction. But neighbouring domains can point differently, giving a small overall magnetisation even though each domain is strongly magnetised.

Why have domains at all? Making one enormous aligned region can produce a costly external magnetic field. Dividing into domains can reduce that energy. Domain walls also cost energy, so the actual arrangement is a compromise, influenced by shape, crystal structure and defects. “Random arrows” is a useful first sketch of cancellation, not a universal picture of real domain geometry.

When an external field is applied:

- Favourably oriented domains can **grow as domain walls move**.
- The magnetisation direction can **rotate** toward the field.
- At sufficiently strong fields the material approaches **saturation**: little additional alignment remains available.

The material has not acquired more electrons or more matter. Its existing magnetic moments contribute a larger resultant.

![[magnetism-domains-remember.mp4]]

*Two stages matter: what the field changes, and what survives when it is removed. The video uses a schematic set of regions and a moving boundary; it is not a microscopic simulation or a measured prediction for a particular alloy.*

## 4. Temporary and permanent: what survives afterwards?

**Magnetically soft** material is easy to magnetise and reverse; **magnetically hard** material resists reversal. These names describe magnetic response, not how easily a specimen bends or scratches.

| Choice | Useful behaviour | Everyday consequence |
|---|---|---|
| Soft iron, as a school model | Large response to an applied field; usually little useful external magnetism retained by an open piece | An electromagnet can pick up iron, then release it |
| Magnetically hard steel, as a school model | More substantial retained magnetisation; harder to reverse | A magnet can keep working without a powered coil |
| Soft ferrite or electrical steel | Easy repeated reversal with an appropriate low-loss design | Transformer cores transfer energy while magnetisation cycles |
| Hard ferrite or rare-earth magnet | Stable magnetisation under its intended operating conditions | Speakers, motors and magnetic catches keep a permanent field |

“Steel” is not a universal magnetic specification. Composition, heat treatment and microstructure matter: electrical steel can be magnetically soft, and some stainless steels are only weakly magnetic. **Low coercivity**, not necessarily zero remanence in every specimen geometry, is the defining feature of magnetic softness.

A useful magnet-making method is a strong directed field, for example inside a current-carrying coil. To reduce remanence, an **alternating field whose amplitude gradually decreases** cycles the material through successively smaller magnetic states. Simply switching off a large field is not the same operation.

Heating above the **Curie temperature** destroys spontaneous ferromagnetic order; the material becomes paramagnetic rather than losing every possible magnetic response. Cooling below that temperature restores the possibility of order, not necessarily the original macroscopic magnetisation. Strong opposing fields, heat and mechanical shock can affect a magnet, but their effectiveness depends on material and conditions.

### Hysteresis: the present remembers the past

![[magnetism-hysteresis.svg|700]]

*Illustrative normalised $M$–$H$ loops, not measured material data. Narrow and wide loops demonstrate different reversal fields; the arrows indicate one complete cycle.*

Follow one loop. A large positive magnetising field drives positive saturation. Reduce the field to zero: the magnetisation need not return to zero. Reverse the field until $M=0$: this defines the **coercive field for magnetisation**. Continue to negative saturation, then reverse the journey. The return path differs: the response depends on history.

Defects and anisotropy can hinder domain-wall movement and rotation. Overcoming those barriers dissipates energy. That explains two apparently opposite design goals: a transformer wants easy reversal and a narrow loop; a storage medium wants a state that resists accidental reversal. Hysteresis loss and eddy-current loss are distinct; laminating a metal core mainly tackles the latter.

## 5. Three material responses—and the meaning of “non-magnetic”

| Response | Microscopic picture | Response to an applied field |
|---|---|---|
| Ferromagnetic, e.g. iron, nickel, cobalt | Collective ordering and domains below the relevant transition temperature | Strong response; may retain magnetisation |
| Paramagnetic, e.g. aluminium | Permanent atomic moments gain a slight alignment against thermal disorder | Weak response along the field; alignment disappears when the field is removed |
| Diamagnetic, e.g. copper, water, bismuth | Applied field changes electronic motion, inducing an opposing contribution | Usually weak response opposing the field; no retained induced magnetisation |

All ordinary materials have a diamagnetic contribution; stronger paramagnetic or ordered responses can mask it. In a **nonuniform** field a small paramagnetic specimen tends toward stronger field, while a diamagnetic one tends toward weaker field. Do not infer a net translational force merely because a uniform field exists.

Many common permanent ceramic magnets are **ferrimagnetic**, not strictly ferromagnetic: opposing sublattices have unequal moments, leaving a net moment. The everyday distinction between temporary and permanent magnets crosses this microscopic classification. A flexible fridge magnet commonly contains hard ferrite particles in a polymer; it is not necessarily a piece of steel.

### Permeability: response, not a universal multiplier

For macroscopic SI fields,

$$\mathbf B=\mu_0(\mathbf H+\mathbf M).$$

Here $B$ is magnetic flux density in tesla; $H$ is magnetic field strength in A/m; $M$ is magnetisation in A/m. The free-current distribution helps determine $H$, but in a finite specimen its internal value also depends on shape and magnetisation. It is not always simply the empty-coil field divided by $\mu_0$.

For a **linear, isotropic** response, $\mathbf M=\chi_m\mathbf H$. Substitution gives

$$\mathbf B=\mu_0(1+\chi_m)\mathbf H=\mu\mathbf H,
\qquad \mu_r=\frac{\mu}{\mu_0}=1+\chi_m.$$

This derivation explains the coefficient: permeability includes the material's response. Weak paramagnets have $\chi_m>0$; weak diamagnets have $\chi_m<0$. Vacuum has $M=0$ and permeability $\mu_0$.

For ferromagnets, a single constant $\mu_r$ is generally inadequate: response varies with field, magnetic history, temperature and orientation. Saturation is exactly where “twice the current means twice the core's magnetisation” fails.

## 6. Current makes a controllable magnet

Moving charge produces a magnetic field. Around a straight wire it circles the wire; a solenoid combines the fields of many turns into a bar-magnet-like pattern. [[Lorentz Force]] develops these patterns and the forces on currents.

The **right-hand grip rule** records a physical direction relation: thumb along conventional current, curled fingers along the field around a wire. For a solenoid, curl fingers with the current around its turns; the thumb points along the interior field toward the N end.

At fixed position and geometry, increasing current strengthens the field; reversing current reverses it. Farther from a long straight wire, the field weakens. Inside a long closely wound air-core solenoid, the field is approximately uniform; outside it is much weaker. More turns per unit length increase the interior field. A suitable soft magnetic core greatly strengthens it, with saturation limiting that benefit.

### The experiment behind the drawing

For a straight wire, pass an insulated wire vertically through a horizontal card and connect it to a low-voltage, current-limited supply. Move a plotting compass around the wire at several radii. With sufficient current for its field to dominate Earth's locally, the needles form tangents to circles. Reverse the current and record the reversed direction. Increase the current at the same position to compare deflection against the same background field.

For a solenoid, map positions along its axis, near both ends and around the outside with a small compass; use a transparent support or an accessible coil to map the interior without changing the winding. Filings on a suitable support reveal the overall shape; compasses supply direction. Keep geometry fixed when changing current or core. Switch off between readings to limit heating. A compass is mainly a **direction instrument**; a calibrated Hall probe is better for quantitative field-strength comparisons.

## 7. Where the material choice does work

**A magnetic catch** needs retained magnetisation: it holds a cupboard shut without a continuous electric power supply. Opening the door requires mechanical work against attraction; closing it releases energy. Holding a stationary door does not continuously consume mechanical energy because its displacement is zero.

**A relay** needs controllable attraction. Current in a coil magnetises a soft core; the core attracts an iron armature, closing a separate circuit. When the coil current stops, a spring returns the armature and opens the contact. The control and load circuits are electrically separate. A permanent-magnet core would make reliable release harder. An example is a low-power control circuit switching a higher-power lamp or motor.

**A moving-coil loudspeaker** needs both kinds of magnetism. A permanent magnet supplies a steady field in a narrow gap. Audio current in a voice coil experiences a force in that field; reverse the current and the force reverses. The attached cone moves back and forth, driving pressure variations in air. The signal varies the **force**, not the permanent magnet's polarity. [[Input and Output Devices]] follows the digital-audio-to-cone chain.

**A hard disk** needs magnetic states that persist without power but can still be changed by a sufficiently strong local writing field. [[Secondary Storage]] explains the recording mechanism. Making a magnetic bit smaller saves space but reduces the energy barrier protecting its state from thermal disturbance: retention and writeability compete.

## Worked examples — name the deciding feature

### 1. A chain of nails — Cambridge 0625/32, May/June 2023, Q7(a)

*Paraphrased:* initially unmagnetised iron and steel nails hang from a permanent magnet. Explain their induced magnetism, then compare what happens after the magnet has been removed. The original parts award 2 and 1 marks respectively.

**Trigger: an initially unmagnetised object is placed in another magnet's field. Tool: induced magnetisation.** The external field changes the arrangement of magnetic moments so that each nail becomes a magnet. Its field can magnetise the next nail. The end nearest the source pole acquires the opposite polarity. The published scheme credits becoming magnetised and acquiring that opposite near pole; merely saying “it sticks” misses the mechanism.

**Trigger: the field is removed, and two materials are compared. Tool: retention.** Steel nails retain substantially more magnetism; soft-iron nails readily lose it. This is the contrast credited by the published scheme. In real specimens, alloy, treatment and geometry affect the amount remaining; “all steel is permanent, all iron instantly becomes exactly zero” overstates the model.

### 2. Mapping two magnets — Cambridge 0625/31, May/June 2023, Q8(b)

*Paraphrased:* describe a method that establishes both the shape and direction of the field around fixed magnets. The original part awards 4 marks.

**Trigger: the question asks for both shape and direction. Tool: a plotting compass and successive position marks.** Keep the magnets fixed, mark where the N end points, move the compass forward to continue the trace, and repeat from different starting points. Draw smooth lines through the marks with arrows in the N-end direction.

The published scheme credits the apparatus, direction measurement and procedural detail. “Use iron filings” alone does not establish the arrows. If using filings for shape, explain sprinkling on card and gentle tapping, then add a compass for direction.

### 3. Why a compass turns but need not move — extension

A small rigid dipole of magnetic moment $m=0.020\,\mathrm{A\,m^2}$ lies at $60^\circ$ to a uniform $B=5.0\times10^{-5}\,\mathrm T$ field. Find the torque magnitude and the energy released as it turns into alignment.

**Trigger: a dipole in a uniform field. Tool: magnetic torque and potential energy.** For a current loop, opposite forces form a couple; the moment is $m=IA$ and the torque is $mB\sin\theta$. Equivalently, with $U=-mB\cos\theta$, $-dU/d\theta$ gives a restoring torque toward smaller $\theta$.

$$\tau=(0.020)(5.0\times10^{-5})\sin60^\circ
=8.66\times10^{-7}\,\mathrm{N\,m}.$$

$$U_i-U_f=mB(1-\cos60^\circ)=5.0\times10^{-7}\,\mathrm J.$$

With damping, that energy becomes heat as the needle settles. In a uniform field the two force contributions cancel in translation even while they produce a torque. A field gradient is needed for a net force on a fixed dipole; along one dimension, a fixed aligned moment gives $F_x=m\,dB/dx$.

## Hands-on — what does attraction actually prove?

Use an ordinary small classroom bar magnet, a paperclip, a copper item and an aluminium item. Test each with both poles; do not assume appearance tells you the metal. Does the paperclip attract another while it is near the magnet? Does it retain any effect afterwards? Record what happened rather than assuming the clip is pure iron: clips are often steel.

Next, use the compass method above to map a field. Predict each new needle direction before placing the compass. Turning the magnet around should reverse the arrows while preserving the approximate shape. Compare a point close to the magnet with one far away, where Earth's field matters more.

**What this establishes:** qualitative attraction, induced response and field direction. **What it does not establish:** the alloy composition, a measured hysteresis loop or a permeability value. Those need controlled specimens and quantitative apparatus.

## Common misconceptions

- **“Every metal is magnetic.”** Compare iron with copper and aluminium; electrical conduction and strong ferromagnetism are different properties.
- **“Attraction proves permanent magnetism.”** Use the induced nail as the counterexample. In the ordinary classroom test, repulsion by a known pole is the decisive evidence.
- **“Unmagnetised means no microscopic moments.”** Distinguish small resultant from small individual contributions, as with cancelling forces.
- **“The domains are atoms.”** A domain contains many aligned atomic moments; moving a wall changes which direction occupies a region.
- **“Soft iron has no hysteresis whatsoever.”** Soft means easy reversal; ideal zero remanence is a simplification, not a universal measurement.
- **“Field lines are trajectories or strings.”** A compass aligns with the tangent; a moving charge generally feels a force perpendicular to its motion and $\mathbf B$.
- **“A permanent magnet runs out of energy just by holding something.”** Static holding involves no displacement; heat, opposing fields and material changes can weaken it for different reasons.

## Beyond syllabus — when memory costs energy

Recall that hysteresis means the route back differs from the route out. In a quasistatic cycle, the magnetic work dissipated per unit volume can be represented by the enclosed $B$–$H$ loop area:

$$w_{\rm loss}=\oint H\,dB.$$

Using $B=\mu_0(H+M)$, the closed integral of $H\,dH$ vanishes, so $w_{\rm loss}=\mu_0\oint H\,dM$. This is why an $M$–$H$ plot needs the extra $\mu_0$ factor before its area represents an energy density. The illustrative normalised plot above has no calibrated loss value.

A magnet storing information and a transformer cycling its field are asking opposite questions of the same energy barriers. **Can this state survive?** versus **can this state change with little loss?** That is a materials-design decision, not simply “stronger magnets are better”.

## Exam Notes

### Cambridge 0625 IGCSE — §4.1 and §4.5.3

- **§4.1 Core 1–9:** pole forces, induced magnetism, soft iron versus steel, magnetic/non-magnetic materials, field meaning/direction, bar-magnet pattern, compass/filings experiments, permanent-magnet/electromagnet uses. **Supplement 10–11:** magnetic interactions through fields and field-line spacing as relative strength.
- **§4.5.3 Core 1–3 and Supplement 4–5:** wire/solenoid patterns and direction experiments, relays/loudspeakers, qualitative strength variation and effects of changing current. The force law, motors and induction are developed in [[Lorentz Force]] and [[Electromagnetic Induction]].
- Learn the qualitative explanations; domain-wall physics, $H/M$, susceptibility and hysteresis integrals are enrichment here. Filings supply a pattern, a compass supplies direction. State a complete experimental sequence, not only an apparatus list.
- Worked examples above were checked against the published 2023 question papers and mark schemes. They are applications of the field and material ideas, not definitions to reproduce without a causal explanation.

### Cambridge 9702 A-Level — §20.1; support for §20.5

§20.1 requires magnetic fields from moving charges/permanent magnets and field-line representation. Wire/solenoid current dependence supports §20.5; the full quantitative treatment belongs with [[Lorentz Force]]. Ferromagnetic domains, dia/paramagnetism and hysteresis are not explicit outcomes of the canonical 2028–2030 syllabus. The 2025–2027 version has the same relevant outcomes.

### IB Physics — D.2, SL and HL

D.2 requires magnetic field-line interpretation for bar magnets, straight wires, circular coils and air-core solenoids, including direction from current. Use this treatment with the complete current-pattern diagrams in [[Lorentz Force]]. D.3 handles forces. Material-classification, domain and hysteresis detail is enrichment rather than a named D.2 requirement in the first-assessment-2025 guide.

### AP Physics C: Electricity and Magnetism — Topic 12.1

The current CED explicitly includes **12.1.A–C**: vector-field representations/closed loops; dipoles, pole interactions, distance dependence, compass alignment and Earth's approximate dipole; permanent/induced magnetism, ferro/para/diamagnetic materials; permeability and its dependence on composition, temperature, orientation and field strength. The material-response sections above are assessed scope, not merely enrichment for this course. Quantitative force laws and field integrals continue in Topics 12.2–12.4.

### AP Physics 2 — Topic 12.1

The algebra-based CED also names **12.1.A–C** with the material classes and permeability. Explain what changes inside a material and how that affects its field; a learned drawing of a bar magnet alone is insufficient. The hysteresis energy integral and dipole-force derivative are extensions beyond this algebra-based treatment.

### Where it is not examined

AP Physics 1 and AP Physics C: Mechanics do not include magnetism in their current course frameworks. Cambridge mathematics 0580/0606/9709/9231 and the maths-only IB/AP courses do not assess magnetic-material physics as a topic. Applications may use their mathematical tools without making magnetic domains a maths syllabus requirement.

## Connections

- **Foundation:** [[Newton's Laws of Motion]] — distinguish a net force from a turning effect.
- **Forces and fields:** [[Lorentz Force]] — moving charges, current-carrying wires, motors and field patterns; [[Torque]] — why opposite forces can turn without translating.
- **Changing flux:** [[Electromagnetic Induction]] — induced emf is a different phenomenon from induced magnetisation.
- **Field structure:** [[Maxwell's Equations]] — magnetic flux has no isolated sources or sinks.
- **Information in matter:** [[Secondary Storage]] — nonvolatile states written by magnetic fields.
- **Devices:** [[Sensors and Control Systems]], [[Input and Output Devices]] — relays, magnetic sensors and speakers.
- **History:** [[The Bookbinder's Apprentice]] — experimental questions that connected electricity and magnetism.

### Further reading

- [OpenStax, Magnetism in Matter](https://openstax.org/books/university-physics-volume-2/pages/12-7-magnetism-in-matter) — material responses and domains.
- [University of Virginia, Magnetic Materials](https://galileoandeinstein.phys.virginia.edu/Elec_Mag/2022_Lectures/EM_33_Magnetic_Materials.html) — magnetisation, domain walls and soft/hard behaviour.
- [Feynman Lectures II, Magnetic Materials](https://www.feynmanlectures.caltech.edu/II_37.html) — an extended physical discussion; historical remarks reflect the lecture's period.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\mathbf B$ | `\mathbf B` | magnetic flux density, T |
| $\mathbf H$ | `\mathbf H` | magnetic field strength, A/m |
| $\mathbf M$ | `\mathbf M` | magnetisation, A/m |
| $\mu,\mu_0,\mu_r$ | `\mu,\mu_0,\mu_r` | permeability, vacuum permeability, relative permeability |
| $\chi_m$ | `\chi_m` | magnetic susceptibility |
| $\mathbf m$ | `\mathbf m` | magnetic dipole moment, A m² |
| $U=-\mathbf m\cdot\mathbf B$ | `U=-\mathbf m\cdot\mathbf B` | dipole potential energy in an external field |
| $\tau=mB\sin\theta$ | `\tau=mB\sin\theta` | dipole torque magnitude |
| $\oint H\,dB$ | `\oint H\,dB` | hysteresis loss per unit volume for a full cycle |

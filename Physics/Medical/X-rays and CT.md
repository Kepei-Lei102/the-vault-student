---
chinese: X 射线与计算机断层成像 (X shèxiàn yǔ jìsuànjī duàncéng chéngxiàng)
prerequisites:
  - "[[Electromagnetic Spectrum]]"
  - "[[Electric Potential]]"
  - "[[Energy Levels and Line Spectra]]"
leads_to: []
teach_together:
  - "[[PET Scanning]]"
  - "[[Ultrasound]]"
  - "[[Linear Systems in 3D]]"
tags:
  - subject/physics
  - domain/medical-physics
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/0625-3-3
  - syllabus/9702-24-2
  - type/deep
  - type/derivation
  - notation/linear-attenuation-coefficient
  - misconception/ct-is-a-photograph
  - misconception/all-xray-photons-have-energy-eV
---

# X-rays and CT X 射线与计算机断层成像

> *A shadow tells you that something blocked the light. It is much less willing to tell you where along the path that something was. An X-ray has the same problem. A CT scanner's answer is wonderfully mathematical: ask from another direction. Then another. Keep the object whole; do the cutting in the equations.*

![[x-rays-ct-onion-comic.png|900]]

*An onion's entirely fictional encounter with tomography. The reconstructed slices exist on the screen; the onion remains intact. The cartoon is a joke about inference, not a technical diagram of a scanner.*

## Definition — projection versus section

**X-rays** are high-frequency electromagnetic radiation. In an X-ray tube they are produced when energetic electrons strike a metal target. They travel as electromagnetic waves and exchange energy with matter in photons, $E=hf=hc/\lambda$.

**Radiography** records transmitted X-rays to form a **projection image**: each detector element receives radiation that has travelled through a whole path across the object. Structures at different depths can overlap in the image.

**Computed tomography (CT)** reconstructs the internal distribution of X-ray attenuation from measurements made at many angles. A reconstructed cross-section is a **slice**; multiple sections can form a volume. “Tomography” means imaging by sections. The machine does not physically cut the object.

| Ordinary X-ray projection | CT reconstruction |
|---|---|
| One viewing direction combines structures along each ray | Many directions constrain where attenuation occurs |
| Detector position labels a ray through the body | Pixel/voxel position labels a small reconstructed region |
| Fast and useful, but depth overlap remains | Separates structures within sections; acquisition and reconstruction are more involved |

### 中文锚点

拍胸片时，肋骨和肺会叠在一张影像里，好比几样东西的影子重在一起：只从一个方向看，很难分清前后。CT 就绕着身体从许多角度测量，让不同方向的信息互相补充，再算出里面的排列。所谓“切片”，是计算机重建出来的截面，身体当然没有被切开。它聪明的地方，是用许多份不完整的线索，一起约束出内部的样子。

## Notation

| Quantity | Symbol | Meaning / units |
|---|---|---|
| Accelerating potential difference | $V$ | volts; magnitude across the tube |
| Elementary charge | $e$ | $1.602176634\times10^{-19}\ \mathrm C$ |
| Photon energy | $E=hf=hc/\lambda$ | joules, or electronvolts |
| Incident and transmitted intensity | $I_0,I$ | $\mathrm{W\,m^{-2}}$ |
| Linear attenuation coefficient | $\mu$ | Inverse length, e.g. $\mathrm{cm^{-1}}$ |
| Path length | $x$ or $\ell$ | Distance actually travelled in a material |
| Logarithmic projection | $p=-\ln(I/I_0)$ | Dimensionless accumulated attenuation |
| Image elements | pixel / voxel | A small area in a slice / a small volume |

An **electronvolt**, eV, is an energy unit: the energy gained by an elementary charge crossing 1 V. In $E_{\max}=eV$, the symbols mean charge multiplied by voltage; in “80 keV”, eV is the unit.

## Key Ideas — source, interaction, reconstruction

### 1. The X-ray tube — an electron accelerator with a target

A heated **cathode** releases electrons by thermionic emission. A large potential difference accelerates them through a vacuum towards a positive **anode**, whose metal target stops or deflects them. The vacuum prevents the electrons losing most of their energy in collisions with gas before reaching the target.

The target receives substantial thermal energy as well as emitting X-rays, so cooling matters. A small focal spot helps image sharpness, while spreading the deposited energy—such as with a rotating anode—helps manage heating. These are engineering compromises, not decorations on a tube diagram.

There are two main routes to X-ray emission:

- **Bremsstrahlung (“braking radiation”):** an electron is deflected/decelerated by the target's electric fields and emits a photon. Different energy losses give a continuous spectrum.
- **Characteristic radiation:** an energetic incident electron ejects an inner-shell electron. An electron from a higher level fills the vacancy, emitting a photon with energy equal to the level difference. These discrete peaks depend on the target element.

The continuum and the peaks can coexist. The characteristic lines connect directly to [[Energy Levels and Line Spectra]]; the continuum does not require a single fixed atomic energy gap. [OpenStax, Atomic Spectra and X-rays](https://openstax.org/books/university-physics-volume-3/pages/8-5-atomic-spectra-and-x-rays)

### 2. Voltage sets an energy ceiling — derive the shortest wavelength

**Tool: energy gained across a p.d.** An electron starting with negligible kinetic energy gains

$$K=eV.$$

**Tool: energy conservation.** A photon emitted from that electron cannot carry more energy than the electron supplied. The limiting event converts essentially all its available kinetic energy into one photon:

$$E_{\gamma,\max}=eV.$$

**Tool: the photon relation.** Since $E_\gamma=hc/\lambda$, higher energy means shorter wavelength:

$$\boxed{f_{\max}=\frac{eV}{h}},\qquad \boxed{\lambda_{\min}=\frac{hc}{eV}}.$$

This is an **upper energy limit**, not the energy of every photon. Most photons in the broad spectrum have less energy and therefore longer wavelengths. Doubling $V$ halves the theoretical cutoff wavelength; increasing the electron current at fixed $V$ mainly changes the number of electrons striking the target per second, not that cutoff.

There is no need to use the non-relativistic formula $\tfrac12mv^2$ to derive the limit. The work–energy statement $K=eV$ still applies when electrons are fast enough that the classical speed formula is inaccurate.

### 3. Attenuation turns a beam into a shadow image

For a narrow monochromatic beam in a uniform material, let each small distance remove a fraction of the beam proportional to that distance:

$$\mathrm dI=-\mu I\,\mathrm dx.$$

Separating and integrating gives

$$\int_{I_0}^{I}\frac{\mathrm dI'}{I'}=-\mu\int_0^x\mathrm dx',\qquad
\boxed{I=I_0e^{-\mu x}}.$$

Attenuation includes absorption and scattering out of the detected beam. It is not simply “the photons get tired”: photons can be removed from the primary beam or change energy/direction in interactions. The model excludes complications such as scatter reaching the detector and a spectrum of different photon energies.

For successive layers, the surviving fractions multiply:

$$\frac{I}{I_0}=e^{-\mu_1x_1}e^{-\mu_2x_2}\cdots
=\boxed{e^{-\sum_i\mu_ix_i}}.$$

This is a **transmission** path, unlike the outward-and-return echo in [[Ultrasound]]. Do not automatically double every thickness. Trace the actual ray.

At fixed energy, $\mu$ depends on material composition and density. It is not density alone. A change in thickness also changes attenuation, even if the material is identical.

### 4. Contrast — useful differences, not simply “more X-rays”

**Image contrast** is the difference in image brightness or degree of blackening between regions. It arises when different ray paths transmit different intensities.

Bone commonly attenuates diagnostic X-rays more strongly than nearby soft tissue. In a conventional display it appears lighter, because fewer photons reached the corresponding detector region; in traditional film, greater exposure produces greater blackening. A digital display can invert or remap these values, so the invariant is the difference in detected signals, not “more radiation always means white”.

An iodine- or barium-containing contrast agent changes attenuation in a selected region, helping distinguish structures whose natural attenuation is too similar. It does not make X-rays reflect like ultrasound. [NIH/NIBIB, CT](https://www.nibib.nih.gov/science-education/science-topics/computed-tomography-ct)

Multiplying $I_0$ makes both transmitted signals larger. In the ideal model it does not alter their **ratio**, though it can improve photon-counting statistics. Too little difference between the paths can still give poor contrast; too few detected photons can make that difference difficult to distinguish from noise.

### 5. Why one projection cannot give depth

Take two layers with attenuations $\mu_1x_1$ and $\mu_2x_2$. Swapping their order leaves

$$I/I_0=e^{-(\mu_1x_1+\mu_2x_2)}$$

unchanged. The detector knows the **sum along the ray**, but not where each contribution occurred. This is a direct proof of an ambiguity, not just a claim that a picture looks confusing.

Taking the logarithm reveals the hidden addition:

$$\boxed{p=-\ln(I/I_0)=\sum_i\mu_ix_i}.$$

For a continuously varying object,

$$\boxed{p=\int_{\text{ray}}\mu(\mathbf r)\,\mathrm d\ell}.$$

A projection is a collection of these line integrals across detector positions. **The logarithm turns multiplicative transmission into additive information about the interior.**

### 6. CT adds directions until the answers must agree

Divide a slice into small pixels. For ray $j$, let $\ell_{jk}$ be its path length through pixel $k$, whose unknown attenuation coefficient is $\mu_k$. Then

$$p_j=\sum_k\ell_{jk}\mu_k,\qquad \boxed{\mathbf A\boldsymbol\mu=\mathbf p}.$$

The geometry supplies matrix $\mathbf A$; the detector supplies $\mathbf p$; the image is the unknown vector $\boldsymbol\mu$. Changing the angle changes which pixels share a ray. Measurements that overlapped from one direction can become distinguishable from another.

In the school-level picture:

1. Send X-rays through a thin section and detect the transmitted radiation.
2. Collect many projections of that section from different angles.
3. Use a computer to reconstruct its two-dimensional attenuation distribution.
4. Repeat for sections along an axis and combine the sections into a three-dimensional representation.

Modern scanners can collect multiple sections and use continuous helical motion: the tube/detector system rotates while the table advances. The central logic remains many directions → reconstructed sections → volume. [NIH/NIBIB, CT](https://www.nibib.nih.gov/science-education/science-topics/computed-tomography-ct)

![[x-rays-ct-reconstruction.mp4]]

*The object stays fixed while parallel beam directions change. A detector profile measures transmission; its logarithm supplies equations. Reconstructions from increasingly many directions then recover a tiny synthetic slice. This is an ideal discrete model, not a clinical scanner or a claim that sixteen views suffice for medical CT.*

![[x-rays-ct-reconstruction.svg|760]]

*All four panels use the same value scale. The 12 × 12 grid, exact ray lengths and noiseless data deliberately isolate the information problem. Colour represents reconstructed attenuation, not tissue identity. Displays clip values outside 0–0.9 model units; underdetermined unconstrained least-squares solutions can include unphysical negative values.*

## Special Cases — test the equations

- **No material:** $x=0$ gives $I=I_0$ and $p=0$.
- **Two equal half-thicknesses:** $e^{-\mu x/2}e^{-\mu x/2}=e^{-\mu x}$; splitting the calculation must not change the result.
- **Half-value thickness:** $I/I_0=1/2$ gives $\boxed{x_{1/2}=\ln2/\mu}$. Two such thicknesses leave one quarter, not zero.
- **Same total attenuation, different arrangement:** one projection cannot distinguish them. More directions can supply the missing constraints.
- **Very little detected radiation:** the mathematical logarithm becomes sensitive to noise; zero detected counts cannot simply be entered into $\ln I$.

## Worked Examples

### 1. Voltage as a photon-energy limit — original example

An X-ray tube operates at $80\ \mathrm{kV}$. Find its maximum photon energy and minimum wavelength.

**Tool: $K=eV$ — the energy source is the accelerating p.d.**

$$E_{\max}=1.602\times10^{-19}(80\times10^3)
=1.28\times10^{-14}\ \mathrm J=\boxed{80\ \mathrm{keV}}.$$

**Tool: $\lambda=hc/E$ — maximum energy selects minimum wavelength.**

$$\lambda_{\min}=\frac{6.626\times10^{-34}(2.998\times10^8)}{1.282\times10^{-14}}
=\boxed{1.55\times10^{-11}\ \mathrm m=0.0155\ \mathrm{nm}}.$$

A $0.010\ \mathrm{nm}$ photon would require about 124 keV, above this tube's ceiling. More tube current at the same voltage cannot make it possible within this model.

### 2. Two paths through a structure — 9702/42/O/N/25 Q10(b)(i–ii), 1 + 3 marks

**Paraphrased source geometry:** region B crosses $5.8\ \mathrm{cm}$ of material P. Region A has the same total thickness, but $2.1\ \mathrm{cm}$ is material Q, leaving $3.7\ \mathrm{cm}$ of P. Given $\mu_P=0.35\ \mathrm{cm^{-1}}$ and $I_A=0.053I_0$, find $I_B$ and $\mu_Q$.

**Tool: one homogeneous path — B contains only P.**

$$\frac{I_B}{I_0}=e^{-0.35(5.8)}=0.1313\ldots\approx\boxed{0.13}.$$

**Tool: multiply layer transmissions — A crosses both P and Q.**

$$0.053=e^{-0.35(3.7)}e^{-\mu_Q(2.1)}.$$

**Tool: logarithms — the unknown coefficient sits in an exponent.**

$$\ln(0.053)=-0.35(3.7)-2.1\mu_Q,$$

$$\boxed{\mu_Q=\frac{-\ln(0.053)-0.35(3.7)}{2.1}=0.782\ldots\ \mathrm{cm^{-1}}\approx0.78\ \mathrm{cm^{-1}}}.$$

The published scheme credits the P-layer factor, the combined exponential equation and the final coefficient. Using 5.8 cm for P **and** adding 2.1 cm for Q counts some of the path twice.

Part (b)(iii) asks why the resulting image has poor contrast. Its scheme compares the detected intensities: $0.13/0.053\approx2.5$. Use that comparison for this question; **2.5 is not a universal clinical threshold for good or bad contrast**.

### 3. Explain the reconstruction — 9702/42/O/N/25 Q10(c), 3 marks

**Tool: acquisition → reconstruction → volume — the question asks how a 3D image is formed.**

Scan a thin section from many different angles and use the measurements to reconstruct the section. Repeat for successive sections along the structure, then compile them into a three-dimensional image.

The scheme's three credited elements are thin sections, many angles for each section, and repeating/combining sections into 3D. “The computer makes a 3D picture” names the result but leaves out the mechanism.

### 4. A four-pixel scanner — original algebraic model

Let a square contain unknown *integrated contributions* $a,b$ in the top row and $c,d$ below. Equal unit path lengths are built into these numbers. Measured logarithmic projections give

$$a+b=3,\quad c+d=7,\quad a+c=4,\quad b+d=6.$$

**Tool: check independence before solving.** Adding the row equations and adding the column equations both give 10. These are only three independent constraints; four measurements do not necessarily mean a unique solution.

Set $a=t$. Then $b=3-t$, $c=4-t$, $d=3+t$. All four measurements agree for many different interiors.

**Tool: a new direction gives a genuinely new constraint.** Suppose a diagonal ray through $a,d$, with the known diagonal path factor divided out, gives $a+d=5$. Then $2t+3=5$, so

$$\boxed{a=1,\quad b=2,\quad c=3,\quad d=4}.$$

The extra view earns its keep by changing the relationships among unknowns. Repeating the same direction more accurately cannot resolve this particular ambiguity.

## Real Life — inference is the working tool

A projection can superimpose ribs and lung structures; a CT section can distinguish where structures lie within the body. The reconstruction is useful precisely because a single transmitted beam does not report depth. Industrial CT applies the same idea to manufactured parts: inspect an internal void or an assembled structure without dismantling it.

The broader mathematics appears whenever measurements combine hidden contributions. A detector reading is a constraint; reconstruction finds an interior consistent with many such constraints. [[Linear Systems in 3D]] is the small, visible version of the same problem.

X-rays are **ionising radiation**. Producing a useful image while controlling exposure is an engineering and clinical tradeoff; more photons can reduce counting noise, but are not free. CT and ordinary radiography both use X-rays; ultrasound uses mechanical waves. [FDA, Medical X-ray Imaging](https://www.fda.gov/radiation-emitting-products/medical-imaging/medical-x-ray-imaging)

## Hands-on — build the image from its measurements

Run `x-rays-ct-model.py` with Python and NumPy. It constructs a 12 × 12 synthetic attenuation grid, computes exact line lengths through its pixels and generates transmitted intensities. It then reconstructs the grid from logarithmic measurements at 2, 4, 8, 16 and 48 directions.

Before running, predict which changes alter the information and which alter the noise:

- More repetitions of the same directions: more data about the same constraints.
- Additional directions: potentially new independent constraints.
- Higher photon counts: better counting statistics, not automatic new geometric information.

The governing Python operation is real linear algebra:

```python
import numpy as np
# A[j, k] is ray j's length through pixel k.
# transmission is the measured fraction I / I0 for each ray.
p = -np.log(transmission)
mu, residuals, rank, singular_values = np.linalg.lstsq(A, p, rcond=None)
```

In the companion, the full ideal system recovers the original to numerical precision. That verifies the tiny constructed model, **not clinical accuracy**: generation and inversion share the same geometry. Add noise to the measurements, reduce the directions, or perturb the assumed geometry to see why real reconstruction needs more care.

## Common Misconceptions

- **“All photons have energy $eV$.”** That is the upper limit. Distinguish a cutoff from the whole spectrum.
- **“X-rays and gamma rays are separated by a strict energy boundary.”** Their ranges overlap; electron processes versus nuclear/particle processes identify their origins in this context.
- **“CT detects X-ray echoes.”** It measures transmitted radiation from many directions; ultrasound pulse–echo imaging times reflections.
- **“A projection is a cross-section.”** Swap the order of two attenuating layers: the same projection can come from different depth arrangements.
- **“Four equations guarantee four unknowns.”** Check independence. Repeated information is not a new constraint.
- **“Higher intensity always gives better contrast.”** Separate relative signal difference from signal-to-noise ratio and exposure.

## Exam Notes

### Cambridge 9702 — §24.2, all four outcomes

The 2028–2030 syllabus requires electron bombardment of a metal target and minimum wavelength from accelerating p.d.; internal-structure imaging and contrast; $I=I_0e^{-\mu x}$; and CT reconstruction of sections from many angles, followed by combining sections into 3D. The 2025–2027 outcomes are the same.

- Tube questions: identify the electron source, acceleration and target; connect $eV$ to the **maximum** photon energy.
- Attenuation questions: identify actual path lengths in each material, multiply transmissions, then take logarithms if needed. Match inverse-length units to length units.
- Contrast questions: compare transmitted signals and the resulting image brightness/blackening; do not substitute “high resolution”.
- CT explanations: different angles **within a section**, repeated sections **along an axis**, reconstruction/combination by computer.
- **Formula sheet:** the supplied list in the verified 2025 paper does not print the X-ray attenuation law or $\lambda_{\min}=hc/(eV)$. Know the attenuation law and derive the cutoff from energy conservation and photon energy. The characteristic-spectrum detail, inverse-problem algebra and reconstruction algorithms below extend the stated requirements.

Verified worked source: **9702/42/O/N/25 Q10(b–c)**, question paper pp.22–23 and published mark scheme p.17. The tube and four-pixel examples are original.

### Cambridge 0625 — §3.3 Electromagnetic spectrum

X-ray medical imaging/security applications and the dangers of ionising radiation belong to the electromagnetic-spectrum scope. The X-ray-tube cutoff calculation, attenuation coefficient calculations and CT reconstruction mechanism are A-Level extensions, not named 0625 requirements. The spectrum introduction already supplies the core band/use context.

### IB Physics and AP Physics 2

IB C.2 includes X-rays in the spectrum and asks a nature-of-science linking question about their discovery; E.2 supplies quantum photon ideas. The current guide does not specify a separate CT/medical-imaging unit. AP Physics 2 includes X-rays within §14.4 electromagnetic waves, with photon physics in Unit 15; it does not name clinical CT reconstruction or the X-ray attenuation law as required topics. These are applications of the shared wave/quantum principles, not additional claimed board closures.

**Not a named X-ray/CT topic in AP Physics 1, AP Physics C: Mechanics or AP Physics C: Electricity and Magnetism.** Electrical acceleration can use familiar work/energy ideas without making the scanner itself a course requirement.

## Connections

- **Source energy:** [[Electric Potential]] — electrical work gives $eV$.
- **Photon structure:** [[Energy Levels and Line Spectra]] — characteristic peaks come from inner-shell energy gaps.
- **Family resemblance:** [[Electromagnetic Spectrum]] — X-rays' place among electromagnetic waves and their interactions with matter.
- **Imaging companion:** [[Ultrasound]] — reflected sound and transmitted X-rays solve different measurement problems; both require careful path accounting.
- **Mathematical companion:** [[Linear Systems in 3D]] — consistency, independence and solving for hidden quantities.

## Beyond Syllabus — why reconstruction is more than adding shadows

### Backprojection, filtering and least squares

Recall that each projection constrains a sum along a ray. **Backprojection** spreads each measured value back along all the locations that could have contributed. True structures accumulate support from many directions, but simply adding these backprojections blurs the result.

**Filtered backprojection** first filters the projection data to compensate for the mathematical blur, then backprojects. An alternative is **iterative reconstruction**: propose an image, calculate the projections it would produce, compare them with the measurements, and update the image to reduce the disagreement.

In a simple least-squares formulation,

$$\widehat{\boldsymbol\mu}=\arg\min_{\boldsymbol\mu}\|\mathbf A\boldsymbol\mu-\mathbf p\|^2.$$

Noise can make the equations inconsistent. The task then becomes finding a justified approximation rather than forcing an exact intersection. Constraints such as non-negative attenuation and penalties against implausibly noisy images can help, but also introduce assumptions. The companion uses a direct least-squares solve; it does not pretend to implement a clinical reconstruction pipeline. For an executable comparison of filtered backprojection and algebraic reconstruction, see [scikit-image’s Radon-transform example](https://scikit-image.org/docs/stable/auto_examples/transform/plot_radon_transform.html).

### The sinogram — measurements have their own geometry

Recall that one projection varies across detector position. Stack these profiles against projection angle to form a **sinogram**. A small feature at $(x,y)$ traces detector position

$$s(\theta)=x\cos\theta+y\sin\theta,$$

which is sinusoidal as the viewing direction changes. That is why the raw measurement array looks nothing like a cross-sectional photograph: its axes are angle and detector position, not the two coordinates inside the body.

![[x-rays-ct-attenuation-sinogram.svg|740]]

### Beam hardening and noise — the ideal model has limits

Recall that the simple exponential used one coefficient at one photon energy. A real tube emits a spectrum. Lower-energy photons are often removed more readily, so the surviving beam becomes richer in higher energies: **beam hardening**. A single fixed effective $\mu$ may then fail across different thicknesses, creating reconstruction artefacts unless corrected.

Counting noise introduces another limit. For approximately Poisson photon counts $N$, the standard deviation is about $\sqrt N$, so the relative fluctuation is about $1/\sqrt N$. Four times as many detected photons halves that relative fluctuation; it does not double spatial resolution. Pixel size, focal spot, detector response, motion and the reconstruction method also matter.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $\lambda_{\min}=hc/(eV)$ | `\lambda_{\min}=\frac{hc}{eV}` | Shortest wavelength from energy ceiling |
| $I/I_0=e^{-\mu x}$ | `I/I_0=e^{-\mu x}` | Surviving intensity fraction |
| $p=-\ln(I/I_0)$ | `p=-\ln(I/I_0)` | Additive projection value |
| $p_j=\sum_k\ell_{jk}\mu_k$ | `p_j=\sum_k\ell_{jk}\mu_k` | Pixel model of one ray |

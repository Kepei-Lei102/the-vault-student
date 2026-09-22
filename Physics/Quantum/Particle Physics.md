---
chinese: 粒子物理 (lìzǐ wùlǐ)
prerequisites:
  - "[[Nuclear Physics]]"
  - "[[Special Relativity]]"
  - "[[Linear Momentum]]"
  - "[[Lorentz Force]]"
leads_to: []
tags:
  - subject/physics
  - domain/particle-physics
  - domain/modern-physics
  - domain/nuclear-physics
  - level/IB-HL
  - level/university
  - curriculum/Cambridge-9702
  - curriculum/AP-Physics-2
  - syllabus/9702-11-2
  - type/theory
  - type/derivation
  - type/hands-on
  - type/visual-tool
  - notation/feynman-diagram
  - misconception/quarks-can-be-pulled-out
  - misconception/the-w-lives-inside-the-neutron
  - misconception/particles-are-seen-directly
  - misconception/antimatter-is-negative-mass
  - misconception/forces-need-contact
---

# Particle Physics 粒子物理

> In 1947 two physicists in Manchester photographed a cloud chamber and found a track that forked into a V, from nothing. Something neutral had come in, lived a ten-billionth of a second, and split into two charged particles. It was made in a flash by the strong force, so it should have died in a flash. Instead it lingered, ten trillion times longer than it had any right to. They called it strange.
>
> Explaining that one word took twenty years, and by the end of them the hundreds of "elementary" particles had collapsed into a dozen, held together by four forces and a short list of rules that never break. This card is that list.

## What this is for

[[Nuclear Physics]] ends where the syllabus does: six flavours of quark, protons and neutrons built from them, beta decay as a quark changing flavour, electrons and neutrinos as leptons. This card goes on from there. It says why physicists believe in quarks nobody has ever pulled out of a proton, what the rules are that decide which reactions happen, what a force *is* at this scale, how a particle that lives $10^{-25}$ seconds can be discovered, and where the picture stops. Every verdict about an allowed or forbidden reaction, and every number, is computed in `particle-physics-model.py`.

## Definition

### Formal

The **Standard Model** describes matter as twelve **fermions**, six quarks ($u, d, s, c, b, t$) and six leptons ($e, \mu, \tau$ and their three neutrinos), each with an antiparticle, interacting through three forces carried by **bosons**: the photon (electromagnetic), the $W^\pm$ and $Z$ (weak) and eight gluons (strong), with the Higgs field giving the massive particles their mass. Quarks are never found alone; they bind into **hadrons**, either **baryons** (three quarks) or **mesons** (a quark and an antiquark). Every reaction conserves electric charge, baryon number and each of the three lepton numbers; strangeness (and the other quark flavours) is conserved by the strong and electromagnetic forces and changed only by the weak force. Gravity is not part of the model.

### Intuitive

A proton is not a thing; it is a *structure*, three quarks held by gluons, the way a water molecule is two hydrogens and an oxygen held by electrons. Break the analogy and the subject makes sense: chemistry has ninety-odd elements and a handful of rules for what bonds; particle physics has twelve pieces and four rules for what can turn into what. The rules are conservation laws, and they are stricter than any rule in chemistry, because they never break at all. Everything else, which particles exist, how long they live, what they decay into, follows from the pieces, the rules and the relative strengths of the forces: strong things happen in $10^{-23}$ s, electromagnetic things in $10^{-16}$ s, weak things in $10^{-10}$ s or slower. That ratio is why the strange particle lingered: the strong force made it, and only the weak force was allowed to unmake it.

### 中文锚点 (Chinese Anchor)

把一盒乐高倒在地上。不管你搭的是房子、船还是龙，用的都只是那几种积木，而且哪块能接哪块，规矩对每一个模型都一样。粒子物理找到的就是这些积木。你身上的每一个质子和中子都是三个夸克拼成的；每个电子自成一类，也是一种积木；所有积木加起来只有十来种，再加上几种传递力的粒子，它们传力的方式就像扔出去的球把推力带过去。让这门学问成为科学而不是一份目录的，是那些规矩：电荷从不凭空出现或消失，"物质积木"的总数从不改变，一个被强力在一瞬间造出来的奇异粒子，只能靠那点微弱的弱力慢慢散架，所以它能活得足够久，在探测器里留下一道径迹。读懂这些径迹，你就知道自己看见的是哪块积木。1989 年 Z 玻色子就是这样被找到的：没有人看见它，人们是从它留下的两个 μ 子把它拼回来的，就像从地上的碎片推断出原来有一只盘子。

## Notation

| Symbol | Meaning | Notes |
|---|---|---|
| $u, d, s, c, b, t$ | the six quark flavours | charges $+\tfrac23, -\tfrac13, -\tfrac13, +\tfrac23, -\tfrac13, +\tfrac23$ in units of $e$ |
| $\bar u, \bar d, \dots$ | antiquarks | opposite charge, opposite baryon number, opposite strangeness |
| $B$ | baryon number | $+\tfrac13$ per quark, $-\tfrac13$ per antiquark; $1$ for a proton, $0$ for a meson |
| $L_e, L_\mu, L_\tau$ | the three lepton numbers | $+1$ for $e^-$ and $\nu_e$, $-1$ for $e^+$ and $\bar\nu_e$; likewise for $\mu$ and $\tau$ |
| $S$ | strangeness | $-1$ per strange quark, $+1$ per anti-strange; a convention from before quarks, which is why the sign is backwards |
| $W^\pm, Z^0, \gamma, g$ | the force carriers | $W$ and $Z$ are heavy ($80$ and $91$ GeV); the photon and gluon are massless |
| MeV/c$^2$, GeV/c$^2$ | mass units | $1$ MeV/c$^2 = 1.78 \times 10^{-30}$ kg; the electron is $0.511$, the proton $938$ MeV/c$^2$ |
| $m^2c^4 = E^2 - p^2c^2$ | the invariant mass | the same for every observer; how a particle is weighed from its decay products |

> [!warning] Notation trap
> Cambridge 9702 writes quark charges as fractions of $e$ and asks for nothing else about quarks. Particle physicists write masses in MeV and GeV with the $/c^2$ dropped, and momenta in MeV/c with the $/c$ dropped, so "a $30$ MeV muon" may mean a kinetic energy, a total energy or a momentum; this card always says which. Strangeness $S = -1$ for a particle containing one strange quark is a historical accident and every student trips on it once.

## Part I — The zoo, and the order hidden in it

Between 1947 and 1964 the cloud chambers and then the bubble chambers filled up with particles. Pions, kaons, the lambda, the sigmas, the xis, resonances that lived $10^{-23}$ s and showed up only as bumps in a graph: by the early sixties there were over a hundred "elementary" particles and the list was growing every year. Enrico Fermi said that if he could remember the names of all of them he would have been a botanist.

The order came from sorting. Arrange the particles by charge and by strangeness and they fall into patterns of eight and ten, so regularly that in 1962 Murray Gell-Mann predicted a missing particle, the $\Omega^-$, with charge $-1$ and strangeness $-3$, and gave its mass; it was found in 1964 with the mass he said. In the same year Gell-Mann and, independently, George Zweig proposed that the patterns were what you would get if every hadron were built from three kinds of smaller piece. Gell-Mann called them quarks, after a line in *Finnegans Wake*, and did not at first insist they were real.

**The evidence that they are real** came in 1968 from Stanford, and it was Rutherford's experiment again at a thousand times the energy. Electrons of $20$ GeV were fired at protons. Had the proton been a smooth ball of charge the electrons would have passed through with small deflections; instead a fraction scattered through large angles, exactly as Rutherford's alpha particles had bounced off the nucleus in 1911. Inside the proton were hard, point-like lumps carrying fractions of its charge. Nobody has ever pulled one out, for a reason Part IV explains, but the lumps are there, and their charges are $+\tfrac23$ and $-\tfrac13$.

## Part II — The pieces

![[particle-physics-standard-model.svg|960]]

**Three generations.** Everything ordinary is made of the first column: up and down quarks, the electron, and the electron neutrino that carries off energy in beta decay. The second and third generations are heavier copies with the same charges; a muon is an electron $207$ times heavier that decays in $2.2\ \mu$s, and a tau is heavier still. Nobody knows why there are three. They matter because they exist: cosmic rays make muons in the upper atmosphere by the billion, and the muons that reach the ground are the evidence for time dilation in [[Special Relativity]].

**Hadrons.** Quarks bind in two ways. Three quarks make a **baryon**: $uud$ is the proton, $udd$ the neutron, $uds$ the lambda of the opening paragraph, $sss$ the $\Omega^-$. A quark and an antiquark make a **meson**: $u\bar d$ is the $\pi^+$, $u\bar s$ the $K^+$. `particle-physics-model.py` builds each of these from its quark content and reports charge, baryon number and strangeness; the proton comes out $(+1, 1, 0)$, the $K^+$ $(+1, 0, +1)$, the $\Omega^-$ $(-1, 1, -3)$, and the antiproton $\bar u\bar u\bar d$ is $(-1, -1, 0)$, every property flipped.

**Antimatter.** Every particle has a twin of the same mass and opposite charge, baryon number, lepton number and strangeness. Dirac's equation predicted the positron in 1928 and Carl Anderson photographed one in a cloud chamber in 1932, a track curving the wrong way in a magnetic field. Antimatter is not negative mass and does not fall up; it is ordinary matter with every additive quantum number reversed, and when a particle meets its antiparticle those numbers cancel to zero and the pair can become photons. Hospitals use it every day: [[Nuclear Physics]]'s PET scan is a positron emitter, and the two back-to-back gamma rays from each annihilation are what the scanner detects.

## Part III — The rules: what may happen

The whole predictive content of the subject is a short list of quantities that are the same before and after any reaction. Check them and you know whether a reaction can occur at all, and, from which ones would have to break, which force is responsible.

| Conserved by | Quantity | What it forbids |
|---|---|---|
| everything | electric charge $Q$ | $n \to p + e^+ + \nu_e$ |
| everything | baryon number $B$ | the proton decaying at all: it is the lightest baryon |
| everything | each lepton number $L_e, L_\mu, L_\tau$ separately | $\pi^+ \to \mu^+ + \nu_e$; $\mu^- \to e^- + \gamma$ |
| everything | energy, momentum, angular momentum | a decay into products heavier than the parent |
| strong and electromagnetic only | strangeness $S$ (and charm, bottomness) | a strange particle decaying *fast*: only the weak force may change $S$, and only by $1$ |

**The referee.** `particle-physics-model.py` takes a reaction, adds up every conserved quantity on each side, and delivers a verdict. Its output on thirteen candidates:

| reaction | verdict |
|---|---|
| $n \to p + e^- + \bar\nu_e$ | allowed |
| $n \to p + e^-$ | forbidden: electron number |
| $\pi^+ \to \mu^+ + \nu_\mu$ | allowed |
| $\pi^+ \to \mu^+ + \nu_e$ | forbidden: electron and muon number |
| $\mu^- \to e^- + \bar\nu_e + \nu_\mu$ | allowed |
| $p + p \to p + p + p + \bar p$ | allowed |
| $p + p \to p + p + p$ | forbidden: charge and baryon number |
| $K^+ \to \mu^+ + \nu_\mu$ | weak only: $S$ changes by $1$ |
| $\Lambda \to p + \pi^-$ | weak only: $S$ changes by $1$ |
| $\Omega^- \to \Lambda + K^-$ | weak only: $S$ changes by $1$ |
| $\Xi^- \to n + \pi^-$ | forbidden even weakly: $S$ changes by $2$ |
| $p \to e^+ + \gamma$ | forbidden: baryon and electron number |

**Why the strange particle lingered.** The lambda is made in a strong collision in $10^{-23}$ s, with a $K^0$ alongside so that the total strangeness stays zero: $\pi^- + p \to \Lambda + K^0$. But the lambda's decay to a proton and a pion changes strangeness by one, which the strong force is not allowed to do. Only the weak force can, and the weak force is weak: the lambda lives $2.6 \times 10^{-10}$ s, long enough at nearly the speed of light to travel centimetres and leave the V that Rochester and Butler photographed. The rule that explained the word *strange* is the rule that the weak force alone changes flavour, and beta decay, $d \to u$, is the same rule at work inside a neutron.

**How sure are we?** The proton has never been seen to decay: experiments watching $10^{34}$ protons for years put its lifetime above $10^{34}$ years, which is $10^{24}$ times the age of the universe. Lepton-number violation has never been seen either, except in one form: neutrinos change flavour as they travel, which is a violation of the *separate* lepton numbers and the reason the table above says "separately" with a footnote in the Beyond section.

## Part IV — What a force is

At this scale a force is not a field pulling across empty space; it is an exchange. Two skaters throwing a ball back and forth drift apart, each recoiling as they throw and catch; that is repulsion by exchange, and with a boomerang instead of a ball it becomes attraction. Two electrons repel by exchanging photons. Quarks bind by exchanging gluons. A quark changes flavour by emitting a $W$.

| Force | Carrier | Mass | Range | Relative strength | What it does |
|---|---|---|---|---|---|
| strong | gluon (8 kinds) | 0 | $10^{-15}$ m, confined | 1 | binds quarks into hadrons, and hadrons into nuclei |
| electromagnetic | photon | 0 | infinite | $10^{-2}$ | everything chemical; light |
| weak | $W^\pm$, $Z^0$ | $80$, $91$ GeV | $10^{-18}$ m | $10^{-6}$ | changes flavour: beta decay, the Sun's first step |
| gravity | (graviton, never detected) | 0 | infinite | $10^{-39}$ | not in the Standard Model |

**Why the weak force is weak, and short-ranged.** An exchanged particle is *virtual*: it is borrowed against the energy–time uncertainty $\Delta E\,\Delta t \gtrsim \hbar$, so a carrier of mass $m$ can exist for about $\hbar/(mc^2)$ and travel about $\hbar/(mc)$ before it must be repaid. For the $W$, $\hbar c / (m_W c^2) = 197\ \text{MeV fm} / 80\,400\ \text{MeV} = 0.0025$ fm, a thousandth of a proton's width. The force is weak not because its coupling is small (it is comparable to electromagnetism's) but because its carrier is so heavy that it almost never gets far enough to act. The photon is massless, so its range is infinite and the Coulomb law reaches across the room.

**Feynman diagrams.** Richard Feynman's way of drawing an exchange is now the notation of the subject: time runs left to right, a straight line is a fermion, a wavy line is a photon or $W$, a curly line a gluon, and every vertex where lines meet must balance charge and every lepton and baryon number. An arrow pointing backwards in time is an antiparticle.

![[particle-physics-feynman.svg|960]]

Beta-minus decay is one $d$ quark line turning into a $u$ and throwing off a $W^-$, which becomes an electron and an antineutrino. Muon decay is the same $W$ with a muon line in and a muon neutrino out. The Manim clip draws the first, checks the books at both vertices, and then relabels it as beta-plus decay.

![[particle-physics-beta-decay.mp4]]

**Confinement.** Gluons carry the strong charge themselves, which photons do not do with electric charge, and that one difference changes everything. Pull two quarks apart and the gluon field between them does not thin out like a Coulomb field; it forms a tube of constant tension, so the energy grows *linearly* with distance, and long before the quarks are far apart there is enough energy in the tube to create a new quark–antiquark pair, which snaps the tube into two hadrons. That is why no quark has ever been isolated and never will be: the attempt makes more hadrons. It is also why the strong force between two *nucleons* has a short range despite the massless gluon: what leaks out of a colour-neutral proton is only a residue, carried by pions, with the range $\hbar/(m_\pi c) = 1.4$ fm that Yukawa predicted in 1935.

**The Higgs.** In the equations, the $W$ and $Z$ ought to be massless like the photon, and so should the quarks and leptons. They are not, and the explanation, proposed in 1964 and confirmed at CERN in 2012, is a field filling all space with which particles interact as they move, so that pushing them takes effort: mass. The field's own quantum is the Higgs boson, at $125$ GeV, the last piece of the model to be found.

## Part V — How we know: making, seeing, weighing

**Making.** To make a particle of mass $m$ you must supply at least $mc^2$, and [[Special Relativity]] decides how. Fire a proton at a proton at rest and most of the beam's energy is wasted on keeping the centre of mass moving: to make one antiproton, $p + p \to p + p + p + \bar p$, needs $4m_pc^2$ in the centre-of-mass frame, which a fixed-target beam achieves only at a total energy of $7m_pc^2 = 6.57$ GeV, $5.63$ GeV of it kinetic. Two beams colliding head-on achieve the same with $1.88$ GeV each. Every big machine since the 1970s is a collider for that reason. The Large Hadron Collider runs two proton beams at $6.8$ TeV, $\gamma = 7250$, $2.9$ m/s slower than light, and gives $13.6$ TeV in the centre of mass, enough to make a Higgs a few times a second.

**Seeing.** No detector sees a particle; it sees the trail a charged particle leaves in matter. A charged track through a magnetic field curves with radius $r = p/(qB)$, the [[Lorentz Force]] made into a measuring instrument: the curvature gives the momentum and its sense gives the sign of the charge. Around the tracking chamber sit calorimeters, dense material in which electrons, photons and hadrons dump their energy as a measurable shower, and outside those, muon chambers, because only muons get that far. Neutral particles leave no track at all; a $\Lambda$ or a $Z$ is known by the V of charged tracks that appears where it died.

**Weighing.** A particle that lives $10^{-25}$ s is never seen and never tracked. It is *weighed*: measure the energies and momenta of its decay products, add them, and form $M^2c^4 = (\sum E)^2 - \lvert \sum \mathbf p \rvert^2 c^2$. That combination is the same in every frame, and equals the mass of whatever the products came from. Do it for thousands of muon pairs and most give random values; the ones that came from a $Z$ pile up at one mass.

![[particle-physics-z-peak.svg|900]]

The figure is four thousand simulated $Z \to \mu^+\mu^-$ events with $2\,\%$ momentum smearing, reconstructed exactly as described; the peak sits in the $91$–$92$ GeV bin. The real one, at LEP in 1989, sat at $91.19$ GeV, and its *width* said how fast the $Z$ decays: $2.5$ GeV of width means $2.6 \times 10^{-25}$ s of life. The width also counted the neutrinos. A $Z$ can decay into any neutrino light enough, invisibly, and each kind broadens the peak by a known amount: the measured width fits three, and no more. That is how we know there are exactly three generations of light neutrino, from a bump in a graph.

**Resolving.** Why an accelerator and not a microscope: a probe of momentum $p$ has a de Broglie wavelength $h/p$ and cannot see detail smaller than about $\hbar/p$. At $100$ GeV that is $0.002$ fm, four hundred times finer than a proton. [[Wave-Particle Duality]] gives the wavelength; a big machine is a short wavelength.

## Where this physics does real work

**Medicine.** PET scanning is antimatter at work, as above; the positron emitters themselves, fluorine-18 and the rest, are made in hospital cyclotrons, small particle accelerators in the basement. Proton-beam radiotherapy uses the fact that a charged particle deposits most of its energy at the end of its range, the Bragg peak, to kill a tumour and spare what lies behind it.

**Seeing through mountains.** Cosmic-ray muons pass through rock, fewer where the rock is thicker. Detectors placed under the Great Pyramid in 2017 counted muons arriving from every direction and found a void thirty metres long that no one had entered in four thousand years. The same method watches the inside of volcanoes and nuclear reactors.

**The web.** The World Wide Web was written at CERN in 1989 so that particle physicists could share data, and released free in 1993; the first web server was a NeXT machine in an office there. Grid computing, superconducting magnets and much of modern detector electronics came the same way.

**Dating and the Sun.** Carbon dating is beta decay, which is the weak force, which is a $W$; the first step of the Sun's fusion chain, $p + p \to d + e^+ + \nu_e$, is a $u \to d$ transition and is so slow, precisely because it is weak, that the Sun burns for ten billion years instead of exploding.

**Hands-on.** `particle-physics-model.py` builds the hadrons, referees the reactions, computes the kinematics and simulates the $Z$ peak; `particle-physics-figures.py` draws it. Add a reaction of your own to the referee's list and predict its verdict before running. Then change the smearing on the muon momenta from $2\,\%$ to $10\,\%$ and watch the peak survive, which is the point of an invariant.

## Worked examples

### Example 1: read a hadron from its quarks

*Find the charge, baryon number and strangeness of $\Sigma^+ = uus$ and of $\bar\Lambda = \bar u\bar d\bar s$.*

**Trigger:** "quark content given" means add the quark charges, one third per quark for $B$, $-1$ per strange quark for $S$. **Tool: the quark table.**

$\Sigma^+$: $Q = \tfrac23 + \tfrac23 - \tfrac13 = +1$; $B = 3 \times \tfrac13 = 1$; $S = -1$. $\bar\Lambda$: every sign flips: $Q = -\tfrac23 + \tfrac13 + \tfrac13 = 0$; $B = -1$; $S = +1$. An antibaryon has baryon number $-1$ whatever its charge; the neutral $\bar\Lambda$ is still antimatter, and annihilates with a $\Lambda$.

### Example 2: which force, and how fast

*$\Sigma^+ \to p + \pi^0$ is observed with a lifetime of $8 \times 10^{-11}$ s. $\Delta^+ \to p + \pi^0$ has a lifetime of $6 \times 10^{-24}$ s. Explain the difference.*

**Trigger:** two decays with the same products and lifetimes thirteen orders of magnitude apart: check strangeness. **Tool: the conservation table, strangeness row.**

$\Sigma^+ = uus$ has $S = -1$; the products have $S = 0$. Strangeness changes, so only the weak force can do it, and weak means slow: $10^{-10}$ s. $\Delta^+ = uud$ has $S = 0$, as do the products; the strong force may act, and does, in $10^{-23}$ s. Same final state, same energy release to within a factor of two, and the lifetimes differ by $10^{13}$ because one decay is permitted to a force the other is not.

### Example 3: the muon's energy from a stopped pion

*A $\pi^+$ ($139.57$ MeV) at rest decays to $\mu^+$ ($105.66$ MeV) and a neutrino of negligible mass. Find the muon's kinetic energy.*

**Trigger:** two-body decay from rest: the products share the momentum equally and oppositely, so energy conservation alone fixes each energy. **Tools: $E^2 = p^2c^2 + m^2c^4$ from [[Special Relativity]]; momentum conservation from [[Linear Momentum]].**

With $c = 1$: the muon and neutrino have equal momentum $p$, so $E_\nu = p$ and $E_\mu = \sqrt{p^2 + m_\mu^2}$, and $E_\mu + p = m_\pi$. Then $p^2 + m_\mu^2 = (m_\pi - p)^2 = m_\pi^2 - 2m_\pi p + p^2$, so

$$p = \frac{m_\pi^2 - m_\mu^2}{2m_\pi} = \frac{139.57^2 - 105.66^2}{2 \times 139.57} = 29.79\ \text{MeV}/c, \qquad E_\mu = m_\pi - p = 109.78\ \text{MeV}, \qquad E_k = E_\mu - m_\mu = 4.12\ \text{MeV}.$$

Every muon from a stopped pion has exactly $4.12$ MeV of kinetic energy: a line, not a spectrum, because there are two bodies and not three. Beta decay's continuous spectrum in [[Nuclear Physics]] is the three-body case.

### Example 4: fixed target against collider

*What beam energy makes an antiproton by $p + p \to p + p + p + \bar p$ on a stationary target, and in a collider?*

**Trigger:** "threshold" means all the products at rest in the centre-of-mass frame, so the invariant mass of the initial state must equal $4m_p$. **Tool: the invariant $s = (\sum E)^2 - \lvert\sum \mathbf p\rvert^2$**, with $c = 1$.

Fixed target: the beam has energy $E$ and momentum $p$, the target $(m_p, 0)$, so $s = (E + m_p)^2 - p^2 = 2m_pE + 2m_p^2$. Set $s = (4m_p)^2 = 16m_p^2$: $E = 7m_p = 6.57$ GeV, kinetic energy $6m_p = 5.63$ GeV. Collider: two beams of energy $E$ head-on have $\sum \mathbf p = 0$, so $s = (2E)^2$ and $E = 2m_p = 1.88$ GeV. The fixed-target machine needs three and a half times the energy per proton to do the same physics, and the gap widens with energy, which is why the LHC is a collider.

### Example 5: weigh a particle from two tracks

*Two muons are measured with energies $50$ and $45$ GeV and momenta $\mathbf p_1 = (30, 40, 0)$ and $\mathbf p_2 = (-27, -36, 0)$ GeV/c. What decayed?*

**Trigger:** "what decayed" from products is the invariant mass. **Tool: $M^2 = (E_1 + E_2)^2 - \lvert \mathbf p_1 + \mathbf p_2 \rvert^2$.**

$E_1 + E_2 = 95$; $\mathbf p_1 + \mathbf p_2 = (3, 4, 0)$, magnitude $5$. $M = \sqrt{95^2 - 5^2} = \sqrt{9000} = 94.9$ GeV. With the resolution of a real detector that is a $Z$ ($91.2$ GeV), and the frame did not matter: a physicist moving with the muons would get the same $M$ from different $E$ and $\mathbf p$.

## Common Misconceptions (Teaching Notes)

### 1. "Quarks could be knocked out with enough energy"

More energy makes more hadrons, never a free quark; the gluon tube's energy grows with distance until it makes a new pair. Confinement is not a technological limit, it is what the strong force does.

### 2. "The $W$ (or the electron) was inside the neutron waiting to come out"

A neutron contains three quarks and gluons and nothing else. The $W$ is created at the vertex, exists for $10^{-25}$ s, and the electron and antineutrino are created when it dies. [[Nuclear Physics]] makes the same point about the beta electron; the diagram shows why it is true.

### 3. "The bubble-chamber photograph shows the particle"

It shows a trail of bubbles boiled by a *charged* particle's electric field. Neutral particles leave nothing, and the $Z$ was never tracked by anyone. What the detector delivers is energies and momenta; what the physicist delivers is an invariant mass.

### 4. "Antimatter has negative mass, or negative energy"

Antimatter has positive mass and positive energy and falls down (measured at CERN in 2023). What is reversed is every additive quantum number: charge, baryon number, lepton number, strangeness.

### 5. "Forces need contact, or a field, but not particles"

At this scale the field and the exchanged particle are the same description at different resolutions. The Coulomb field is the sum of many soft photons; the short range of the weak force is the mass of the $W$. The skater picture is a picture, but the range formula $\hbar/(mc)$ is arithmetic that comes out right.

### 6. "The Standard Model explains everything"

It explains every laboratory result to date and leaves out gravity, dark matter, dark energy, neutrino masses and why there is more matter than antimatter. It is the most tested theory in science and everyone who works on it expects it to be incomplete.

## Exam Notes

### Cambridge 9702 (AS), §11.2 Fundamental particles

The syllabus's six statements, all carried here and in [[Nuclear Physics]]: a quark is a fundamental particle with six flavours, up, down, strange, charm, top and bottom; the charge of each flavour, with the antiquark opposite, and "no knowledge of any other properties of quarks is required"; protons and neutrons are not fundamental and are described by their quark composition; a hadron is a baryon (three quarks) or a meson (a quark and an antiquark); the quark changes in $\beta^-$ and $\beta^+$ decay; electrons and neutrinos are fundamental particles called leptons. Everything in Parts III to V beyond that list, strangeness, lepton number, the forces, Feynman diagrams, accelerators and invariant mass, is not examined on 9702, which the syllabus signals with that bracketed sentence.

### AP Physics 2, Unit 15

Essential knowledge 15.8.A.2.i: "in all nuclear decays, nucleon number (the number of neutrons and protons), lepton number (the number of electrons and neutrinos), and charge are conserved." That is the conservation table's first three rows applied to nuclei, and it is the only particle-physics statement in the course.

### Where this is *not* examined

Cambridge 0625 has no quark content. The IB Physics 2025 guide contains none of this: its nuclear topics (E.1, E.3, E.4) stop at decay modes and binding energy, and the earlier guide's particle-physics option is gone. AP Physics C examines nothing here. Everything past the 9702 list is enrichment, written because the conservation laws are the most exam-like thing in physics that no exam in this vault sets, and because a student who has met beta decay deserves to see the $W$.

## Beyond the syllabus

> [!info] Colour, and why three quarks
> Recall that the strong force acts on a charge quarks carry and electrons do not. That charge comes in three kinds, called red, green and blue for no reason but bookkeeping, and only colour-neutral combinations can exist as free particles: three quarks of three different colours, or a quark and an antiquark of a colour and its anti-colour. That is why baryons have three quarks and mesons two, and it is the reason the $\Delta^{++} = uuu$, three identical quarks in the same state, does not violate [[Pauli Exclusion Principle]]: the three differ in colour.

> [!info] Neutrinos that change their minds
> Recall that the table conserves each lepton number separately. In 1998 Super-Kamiokande found that muon neutrinos made in the atmosphere arrive as fewer muon neutrinos than left, having turned partly into tau neutrinos on the way. Oscillation is possible only if neutrinos have mass, which the original Standard Model did not provide; the masses are tiny, below an electronvolt, and are the first laboratory evidence of physics beyond the model. Total lepton number is still conserved.

> [!info] What is missing
> Gravity has no place in the model and no detected carrier. The rotation of galaxies and the bending of light by clusters ([[General Relativity]]) need five times more matter than the model contains, none of which has been made in a collider. The universe contains matter and almost no antimatter, though the Big Bang should have made equal amounts; the model's known asymmetry between the two is far too small. Those three facts are the field's programme for the next fifty years.

## Connections

- **Built on:** [[Nuclear Physics]] (quark composition, beta decay, antiparticles, PET; the starting line of this card), [[Special Relativity]] (mass–energy, the invariant, thresholds, why muons reach the ground), [[Linear Momentum]] (two-body decays), [[Lorentz Force]] (tracks curving in a field, momentum from curvature).
- **Tools used:** [[Wave-Particle Duality]] (the probe's wavelength sets what an accelerator can resolve), [[Pauli Exclusion Principle]] (colour as the missing label in $\Delta^{++}$), [[Energy Levels and Line Spectra]] (a resonance is a level with a width, and width means lifetime).
- **Where it leads:** [[General Relativity]] (the gravity the model leaves out; dark matter from lensing), [[Hubble's Law and the Expanding Universe]] (where the matter–antimatter asymmetry becomes cosmology).
- **Stories:** [[The Universe Has a Left Hand]] (the weak force refusing mirror symmetry, in Wu's cobalt experiment), [[Emmy Noether]] (every conservation law in Part III is a symmetry).

## Sources

- Rochester, G. D., & Butler, C. C. (1947). Evidence for the existence of new unstable elementary particles. *Nature*, 160, 855–857. The V-tracks of the opening paragraph.
- Gell-Mann, M. (1964). A schematic model of baryons and mesons. *Physics Letters*, 8, 214–215; Zweig, G. (1964). CERN report 8182/TH.401. The quark model.
- Barnes, V. E., et al. (1964). Observation of a hyperon with strangeness minus three. *Physical Review Letters*, 12, 204–206. The $\Omega^-$.
- Bloom, E. D., et al. (1969). High-energy inelastic e–p scattering at 6° and 10°. *Physical Review Letters*, 23, 930–934. The Stanford scattering that found the lumps.
- Anderson, C. D. (1933). The positive electron. *Physical Review*, 43, 491–494.
- Arnison, G., et al. (UA1) (1983). Experimental observation of isolated large transverse energy electrons with associated missing energy at √s = 540 GeV. *Physics Letters B*, 122, 103–116. The $W$; the $Z$ followed the same year.
- ALEPH, DELPHI, L3, OPAL and SLD Collaborations (2006). Precision electroweak measurements on the Z resonance. *Physics Reports*, 427, 257–454. The $Z$ mass, width, and the count of three light neutrinos.
- ATLAS Collaboration (2012). *Physics Letters B*, 716, 1–29; CMS Collaboration (2012). *Physics Letters B*, 716, 30–61. The Higgs.
- Fukuda, Y., et al. (Super-Kamiokande) (1998). Evidence for oscillation of atmospheric neutrinos. *Physical Review Letters*, 81, 1562–1567.
- Morishima, K., et al. (2017). Discovery of a big void in Khufu's Pyramid by observation of cosmic-ray muons. *Nature*, 552, 386–390.
- Anderson, E. K., et al. (ALPHA-g) (2023). Observation of the effect of gravity on the motion of antimatter. *Nature*, 621, 716–722.
- Particle Data Group (2024). Review of Particle Physics. *Physical Review D*, 110, 030001. All masses, lifetimes and widths quoted.
- Every computed number is in `particle-physics-model.py`.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $u\bar d$ | `u\bar d` | A meson's quark content |
| $\bar\nu_e$ | `\bar\nu_e` | Electron antineutrino |
| $L_e, L_\mu, L_\tau$ | `L_e, L_\mu, L_\tau` | The three lepton numbers |
| $d \to u + W^-$ | `d \to u + W^-` | The beta-decay vertex |
| $M^2c^4 = \left(\sum E\right)^2 - \left\lvert \sum \mathbf p \right\rvert^2 c^2$ | `M^2c^4 = \left(\sum E\right)^2 - \left\lvert \sum \mathbf p \right\rvert^2 c^2` | Invariant mass of a set of products |
| $R \approx \dfrac{\hbar}{mc}$ | `R \approx \dfrac{\hbar}{mc}` | Range of a force carried by a particle of mass $m$ |
| $s = (E_1 + E_2)^2 - \lvert\mathbf p_1 + \mathbf p_2\rvert^2$ | `s = (E_1 + E_2)^2 - \lvert\mathbf p_1 + \mathbf p_2\rvert^2` | Centre-of-mass energy squared, $c = 1$ |

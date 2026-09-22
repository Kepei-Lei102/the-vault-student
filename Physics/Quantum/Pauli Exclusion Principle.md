---
chinese: 泡利不相容原理 (pàolì bù xiāngróng yuánlǐ)
aliases:
  - Pauli Principle
  - Fermi Gas
  - Degeneracy Pressure
prerequisites:
  - "[[Wave-Particle Duality]]"
  - "[[Energy Levels and Line Spectra]]"
  - "[[Quantum States and the Schrödinger Equation]]"
  - "[[Integration]]"
leads_to: []
teach_together:
  - "[[Stellar Evolution]]"
  - "[[Wolfgang Pauli and the Number 137]]"
tags:
  - subject/physics
  - domain/quantum
  - domain/atomic-physics
  - level/university
  - type/deep
  - type/derivation
  - notation/spin
  - notation/fermi-energy
  - misconception/same-state-means-same-place
  - misconception/two-electrons-per-energy
  - misconception/exclusion-is-electric-repulsion
---

# Pauli Exclusion Principle 泡利不相容原理

> *Why doesn't every electron settle into the cheapest available state? Because “available” is doing real work in that sentence.*

## Definition

### Formal

**No two identical fermions can occupy the same complete one-particle quantum state.** For electrons, that state includes spin. In an orthonormal basis of one-particle states, each state's occupation number is either 0 or 1.

The deeper statement concerns the **whole many-particle wavefunction**: exchanging the complete coordinates of any two identical fermions reverses its sign. For two particles, writing $q=(\mathbf r,\sigma)$ for position **and** spin,

$$\boxed{\Psi(q_2,q_1)=-\Psi(q_1,q_2).}$$

This is **antisymmetry**. It remains true for interacting electrons whose state cannot be described by a single list of independently occupied orbitals.

### Intuitive — a state has more than an address

Two people cannot occupy the same cinema seat. Electrons have a related restriction, but their “seat” is a **state**, not a little patch of space. Different wavefunctions may overlap spatially; different states may even have exactly the same energy. Neither fact makes them the same seat.

A spatial orbital can hold two electrons because there are two independent spin states. A third electron needs a different orbital. That distinction builds the bridge from a quantum rule to the periodic table.

### 中文锚点

电影院快坐满时，新来的观众得另找一个空座，而不能挤进已经有人坐的那个位子。电子也有一种“不能重复占用”的限制，只不过被占用的不是空间里的位置，而是一个完整的量子态。同一个轨道里，两种不同的自旋状态可以各容纳一个电子；第三个电子就得占用别的轨道。正因为有这条限制，电子不能全挤进能量最低的轨道；这也是不同原子外层电子排布各不相同、化学脾气千差万别的原因之一。“座位”只是帮助我们想象状态有别，原子里面并没有一排小椅子。

## Notation

| Symbol | Meaning | Keep distinct |
|---|---|---|
| $\phi_a(\mathbf r)$ | Spatial orbital | A wavefunction, not a classical orbit |
| $\chi_a(q)$ | Complete one-particle state, including spin | Sometimes called a spin-orbital |
| $s,\ m_s$ | Spin quantum number and projection quantum number | Electron: $s=1/2$, $m_s=\pm1/2$ |
| $n,\ell,m_\ell,m_s$ | Atomic orbital and spin labels | Four labels; $s=1/2$ is fixed |
| $N,\ V,\ n_e=N/V$ | Electron count, volume, number density | $n_e$ is not the atomic shell label $n$ |
| $E_F,\ p_F$ | Fermi energy and Fermi momentum | Zero-temperature filling boundary |
| $f(E),\mu$ | Mean state occupation and chemical potential | Occupation probability, not the number of states |

## 1. Identical particles are not distinguishable beads

Imagine swapping two numbered billiard balls. The labels tell you a different arrangement occurred. Electrons have no such permanent serial numbers. “Electron 1” and “electron 2” are coordinate labels used in a calculation, not experimentally readable identities carried by the particles.

You may distinguish **preparations**—one packet on the left, another on the right—but after overlap you cannot assign an observable history to each electron simply by retaining the labels in your notebook.

For ordinary particles in three-dimensional space, the familiar possibilities are:

- **Fermions:** half-integer spin, antisymmetric under exchange. Electrons, protons and neutrons are examples. Exclusion applies separately within each identical species.
- **Bosons:** integer spin, symmetric under exchange. Photons and helium-4 atoms are examples. Multiple bosons can occupy one state.

Spin is intrinsic angular momentum, **not a little charged ball rotating**. Choosing a measurement axis gives an electron two possible projections, $S_z=m_s\hbar=\pm\hbar/2$. “Up” and “down” label these alternatives; they do not say the electron is moving upwards or downwards.

> [!info] What is assumed, and what is proved?
> Antisymmetry is the starting rule here. The **spin–statistics theorem**, connecting half-integer spin to fermionic exchange, belongs to relativistic quantum field theory. We can derive exclusion *from antisymmetry* without pretending to derive that theorem from a seating analogy. The distinction is made explicitly in [MIT's quantum-physics lecture](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/cb66d80c975f1dcd251379668935d758_gK_D6RkbMy8.pdf), opening discussion.

## 2. The minus sign makes duplicate occupation impossible

Take two orthonormal complete states $a$ and $b$. A normalised antisymmetric state is

$$\Psi(q_1,q_2)=\frac{1}{\sqrt2}\left[\chi_a(q_1)\chi_b(q_2)-\chi_b(q_1)\chi_a(q_2)\right].$$

The two terms are **amplitudes**, not competing stories with hidden particle labels. Add them before calculating probabilities. Exchanging $q_1$ and $q_2$ swaps the terms and reverses the sign; $|\Psi|^2$ stays unchanged, as it must for relabelling identical particles.

Now try to use the same complete state twice: $b=a$.

1. Both products become $\chi_a(q_1)\chi_a(q_2)$.
2. Subtracting them gives zero **for every possible configuration**.
3. The result has total probability zero and cannot be normalised to 1.
4. So it is not a possible two-electron state.

That is exclusion. No additional electric force was inserted into the calculation.

The distinction between an irrelevant **overall sign** and the important **relative minus sign** is essential. Multiplying the whole wavefunction by $-1$ changes no probabilities. Removing the minus between its two terms changes interference and defines a different physical symmetry.

### Two electrons in one orbital are allowed

Let both electrons use the same spatial orbital $\phi$, but combine the two spin states antisymmetrically:

$$\Psi=\phi(\mathbf r_1)\phi(\mathbf r_2)\,
\frac{\uparrow_1\downarrow_2-\downarrow_1\uparrow_2}{\sqrt2}.$$

Here the arrows denote spin wavefunctions. The spatial part is symmetric; the spin part, called a **singlet**, is antisymmetric. Their product has the required exchange sign. The complete states $\phi\uparrow$ and $\phi\downarrow$ differ even though their spatial orbital is shared.

![[pauli-orbitals.svg|820]]

*Each box is one spatial orbital; each arrow is one occupied spin state. Carbon's two singly occupied 2p orbitals illustrate Hund's rule as well as Pauli. Boxes are bookkeeping, not little compartments in space.*

Two different atoms can each have a 1s electron with the same spin: orbitals centred at different nuclei are not the same global spatial state. When the atoms approach, their overlap and the allowed combined wavefunctions matter.

## 3. From states to shells—and chemistry

In the central-field orbital description of an atom, the labels are

$$n=1,2,3,\ldots;\quad \ell=0,1,\ldots,n-1;\quad
m_\ell=-\ell,\ldots,\ell;\quad m_s=\pm\tfrac12.$$

The hydrogen Schrödinger problem supplies the allowed spatial labels; these ranges are a result of that problem, not a consequence of Pauli alone. For many-electron atoms, orbitals provide a useful approximate description of an interacting state.

Count the states: fixed $n,\ell$ gives $2\ell+1$ orbitals, each with two spin states. Thus a subshell holds at most $2(2\ell+1)$ electrons: **s: 2, p: 6, d: 10, f: 14**. Summing over $\ell$ gives

$$2\sum_{\ell=0}^{n-1}(2\ell+1)=2n^2.$$

This is a shell's **capacity**, not an instruction to fill all of it before starting the next shell. [OpenStax's atomic-structure treatment](https://openstax.org/books/university-physics-volume-3/pages/8-4-the-exclusion-principle-and-the-periodic-table) sets out the labels and their counting.

Three rules do different jobs:

| Question | Rule | What it supplies |
|---|---|---|
| Is the arrangement allowed? | Pauli exclusion | At most one electron per complete state |
| Which allowed arrangement has least energy? | Ground-state energy minimisation; Aufbau as a guide | Occupation of favourable orbitals, accounting for interactions |
| How do degenerate orbitals tend to fill in an atomic ground configuration? | Hund's first rule | Singly with parallel spins before pairing, within that subshell |

Pauli alone allows carbon's two 2p electrons to pair in one orbital. It does **not** say that arrangement is the lowest-energy one. Hund's rule involves electron interactions and exchange symmetry; it is not an extra capacity rule.

### Where this works: helium balloons and battery chemistry

Helium's $1s^2$ configuration closes its lowest shell. Lithium's third electron must occupy another orbital: its ground configuration is $1s^2 2s^1$. Removing that outer electron leaves a closed core. Together with nuclear attraction, shielding and electron interactions, this helps explain why helium is chemically unreactive whereas lithium readily forms $\mathrm{Li}^+$.

In a rechargeable lithium-ion cell, lithium ions and electrons travel through different routes: ions through the electrolyte, electrons through the external circuit. [DOE explains the two transport paths](https://www.energy.gov/science/doe-explainsbatteries). Electrode chemistry sets the voltage and reversibility. Exclusion supplies part of the electronic structure on which that chemistry depends; **it is not, by itself, a battery model**. The memorable connection is that “the third electron cannot join the first two” has consequences far beyond a diagram of an atom.

### Why your hand meets a table

Bringing solids together changes their combined electronic states. Antisymmetry restricts the allowed many-electron wavefunction, while kinetic energy and electrostatic attractions and repulsions determine the energy cost. The steep rise of total energy under compression produces a restoring force.

It is reasonable to say Pauli is essential to the stability and structure of ordinary matter. It is misleading to replace this entire calculation with either “charges repel” or “a new Pauli force pushes them apart.” Exclusion also matters for electrically neutral fermions. A rigorous treatment relates the fermionic kinetic-energy bound to stability: [Lieb and Thirring, 1975](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.35.687).

## 4. Filling a box before warming it

Start with a deliberately simpler model than an atom: **noninteracting spin-1/2 fermions in a one-dimensional infinite well** of width $L$. From [[Quantum States and the Schrödinger Equation]],

$$E_j=\frac{j^2\pi^2\hbar^2}{2mL^2}=j^2E_1,\qquad j=1,2,3,\ldots.$$

At $T=0$, fill the lowest available complete states. Six particles occupy the first three spatial modes, two per mode:

$$U=2E_1+2(4E_1)+2(9E_1)=28E_1.$$

Even without electric repulsion, they cannot all occupy the lowest spatial mode. The comparison of six ideal spinless bosons would give $6E_1$. Both systems have confinement energy; **exclusion accounts for the additional filling cost** in the fermion example.

![[pauli-state-filling.mp4]]

*Follow six occupied states, then move the walls slowly from $L_0$ to $0.8L_0$. Every occupied energy grows by $1/0.8^2=1.5625$: the total rises from $28E_1(L_0)$ to $43.75E_1(L_0)$. The film assumes slow compression that preserves mode occupations; it shows an ideal well, not atomic orbitals.*

Because $U\propto L^{-2}$ at fixed occupation, shortening the well costs work. The outward force on a movable end is

$$F=-\frac{dU}{dL}=\frac{2U}{L}>0.$$

This is already the mechanism of degeneracy pressure: compressing occupied states raises the minimum allowed energy. It exists at zero temperature. The walls do work **on** the gas when they move inward; cooling cannot remove energy below its ground state.

## 5. A three-dimensional Fermi sea

For a large, uniform, nonrelativistic ideal electron gas, use a cube of volume $V=L^3$ with periodic boundaries. A plane wave fits when $k_i=2\pi j_i/L$, with integer $j_i$. Allowed points in $k$-space are separated by $2\pi/L$ along each axis.

At zero temperature, fill a sphere from $k=0$ to $k_F$. Each point has two spin states. Dividing the sphere's volume by the volume per grid point gives

$$N=2\frac{(4\pi/3)k_F^3}{(2\pi/L)^3}
=\frac{Vk_F^3}{3\pi^2}.$$

The continuum count neglects finite-box boundary corrections; it is accurate for many occupied states. Consequently,

$$\boxed{k_F=(3\pi^2n_e)^{1/3},\quad p_F=\hbar k_F,\quad
E_F=\frac{\hbar^2}{2m}(3\pi^2n_e)^{2/3}.}$$

The sphere is in **momentum space**. It is not a ball of electrons clustered at the middle of the container.

### Deriving the energy and pressure

A thin spherical shell contributes $dN=(V/\pi^2)k^2dk$. Weight its states by $E=\hbar^2k^2/(2m)$:

$$U=\frac{V\hbar^2}{2m\pi^2}\int_0^{k_F}k^4dk
=\frac{V\hbar^2k_F^5}{10m\pi^2}=\frac35NE_F.$$

At fixed $N$, $E_F\propto V^{-2/3}$, so $U\propto V^{-2/3}$. The work relation at zero temperature is $dU=-P\,dV$. Therefore

$$\boxed{P=-\left(\frac{\partial U}{\partial V}\right)_N
=\frac{2U}{3V}=\frac25 n_eE_F
=\frac{\hbar^2(3\pi^2)^{2/3}}{5m}n_e^{5/3}.}$$

These assumptions matter: this is an **ideal, three-dimensional, nonrelativistic, zero-temperature** gas with two spin states. It is not the pressure formula for arbitrary interacting electrons, nor for every density or temperature. The state-counting route is developed in [Tong's statistical-physics notes, quantum gases](https://www.damtp.cam.ac.uk/user/tong/statphys/three.pdf).

## 6. Finite temperature: a blurred occupation edge

Heating a Fermi gas does not put all electrons into a Maxwell–Boltzmann distribution. Low states are largely occupied, and exclusion prevents electrons from moving into occupied final states. The relevant temperature scale is

$$T_F=E_F/k_B.$$

At $T\ll T_F$, only a narrow region near the filling edge changes appreciably. To derive the **Fermi–Dirac mean occupation**, consider one independent state of energy $E$ exchanging energy and particles with a reservoir at temperature $T$ and chemical potential $\mu$. Chemical potential measures the reservoir's free-energy cost of supplying a particle.

The empty state has statistical weight 1; the occupied state has weight $e^{-(E-\mu)/(k_BT)}$. Only these two occupations are allowed, so normalising gives

$$\boxed{f(E)=\frac{e^{-(E-\mu)/(k_BT)}}{1+e^{-(E-\mu)/(k_BT)}}
=\frac{1}{e^{(E-\mu)/(k_BT)}+1}.}$$

As $T\to0$, $\mu\to E_F$ for this gas: occupation becomes a step. At finite temperature, $f(\mu)=1/2$, and $\mu$ adjusts so the total particle count stays fixed. Each actual state still has occupation 0 or 1; a mean of 0.3 means occupied in 30% of the ensemble, not one-third of an electron in it.

![[pauli-fermi-edge.svg|820]]

*The plotted horizontal axis is $(E-\mu)/E_F$, so the centre follows the chemical potential. Raising $T/T_F=k_BT/E_F$ broadens the edge. The occupied particle count also requires the density of available states; area under $f$ alone is not particle number.*

In a metal, this explains why counting **every** conduction electron as a classical $3k_B/2$ heat-capacity contribution fails: most are too far below the edge to be thermally promoted into an empty state. For a real metal, bands and interactions refine the free-electron model.

## Worked Examples

These are constructed examples of the models above, not past-paper questions.

### 1. A third electron—and an eight-electron shell

**Question.** Can three electrons share 1s if their energies differ? How many electrons fit in the $n=2$ shell?

**Trigger: a claim about capacity. Tool: count complete states.** The 1s spatial orbital has two spin states. Three electrons cannot occupy it, regardless of how a proposed energy label is described. A genuinely different state must differ in its actual wavefunction or internal state; renaming it does nothing.

**Trigger: a shell, not one orbital. Tool: allowed $\ell,m_\ell,m_s$.** For $n=2$, 2s supplies one orbital and 2p supplies three. Thus capacity is $2(1+3)=8$. Eight may share a shell; only two may share one spatial orbital.

### 2. A cold gas that is energetically expensive

**Question.** An ideal electron gas has $n_e=8.0\times10^{28}\ \mathrm{m^{-3}}$. Estimate $E_F$, $T_F$ and its zero-temperature degeneracy pressure. Is room temperature small on this scale?

**Trigger: number density in a large 3-D gas. Tool: momentum-space state count.**

$$k_F=(3\pi^2n_e)^{1/3}=1.333\times10^{10}\ \mathrm{m^{-1}}.$$

**Trigger: nonrelativistic electrons. Tool: $E=p^2/(2m_e)$ with $p=\hbar k_F$.**

$$E_F=1.085\times10^{-18}\ \mathrm J=6.77\ \mathrm{eV},\qquad
T_F=7.86\times10^4\ \mathrm K.$$

**Trigger: cold ground-state filling. Tool: $P=2n_eE_F/5$.**

$$P=3.47\times10^{10}\ \mathrm{Pa},\qquad \frac{300}{T_F}=0.00382.$$

Room-temperature electrons are highly degenerate on this model's scale. The Fermi speed $p_F/m_e=1.54\times10^6\ \mathrm{m\,s^{-1}}$ is about $0.005c$, consistent with the nonrelativistic approximation.

This large **electron kinetic pressure** does not mean a metal bar exerts that pressure on its surroundings: the lattice's attractions and other energy terms participate in its mechanical equilibrium.

### 3. Compress a white-dwarf model

**Question.** At fixed composition, a nonrelativistic degenerate electron gas doubles its mass density. By what factors do $E_F$ and $P$ change?

**Trigger: fixed composition. Tool: $n_e\propto\rho$**, because each unit of mass supplies the same electron count. Then

$$\frac{E_{F,2}}{E_{F,1}}=2^{2/3}=1.587,\qquad
\frac{P_2}{P_1}=2^{5/3}=3.175.$$

This local pressure law is the ingredient for a stellar structure calculation. It does not by itself give the radius or guarantee a stable star.

## Hands-on — occupy states, then squeeze

Run the adjacent `pauli-lab.py` with Python 3; it uses only the standard library. It computes the examples, enumerates box states and checks the energy cost of compression. Nothing is downloaded.

Try changing $N$ to 5 or 7 before running this small version:

```python
N = 6
modes = [(i // 2) + 1 for i in range(N)]  # two spin states per mode
U0 = sum(j*j for j in modes)             # units of E1 at initial width
width_ratio = 0.8
U1 = U0 / width_ratio**2
print(modes, U0, round(U1, 2))
# [1, 1, 2, 2, 3, 3] 28 43.75
```

**Prediction first:** adding the seventh particle costs $16E_1$, not $E_1$. Why? The two spin states of each of the first three modes are already occupied. The script's three-dimensional count then shows how discrete lattice states approach the Fermi-sphere estimate for large systems.

## Common Misconceptions

- **“No two electrons can be in the same place.”** The restriction is on complete states. Opposite-spin electrons may share a spatial orbital; position distributions can overlap.
- **“Only two electrons per energy level.”** Two per spatial orbital. Several orbitals can share an energy, so an energy value can correspond to many available states.
- **“Electrons know which seat the others took.”** There is no message or decision. Antisymmetry constrains the collective quantum state.
- **“Pauli is Coulomb repulsion.”** Neutral identical fermions also obey exclusion. The ideal-gas derivation used no interparticle repulsive potential.
- **“Pauli determines every ground-state configuration.”** It removes forbidden arrangements; interactions and total-energy minimisation choose among allowed ones.
- **“Zero temperature means zero kinetic energy.”** Temperature measures thermal excitation above the ground state. A confined fermion ground state still has filling and confinement energy.
- **“Degeneracy means all energies coincide.”** An energy level's degeneracy counts distinct states with that energy. A *degenerate gas* means quantum statistics dominate its occupation; these are related terminology, not identical claims.

## Exam Notes

### Physics — enrichment beyond the named requirements

**Cambridge 9702 (2028–2030)** §22.4 requires discrete atomic energies and spectra; it does not prescribe exclusion, spin-orbitals, antisymmetric states or a Fermi gas. **Cambridge 0625 (2026–2028)** §5 atomic structure and §6.2 stellar evolution do not require this mechanism. A white dwarf being named does not make a degeneracy-pressure derivation examinable.

**IB Physics (first assessment 2025)** E.1/E.2 atomic and quantum physics and E.5 fusion/stars do not prescribe Pauli exclusion or Fermi–Dirac statistics. **AP Physics 2** Unit 15 includes atomic energy levels, spectra and quantum phenomena; exclusion/state counting and the Fermi-gas pressure law are not named required outcomes. **AP Physics 1 and both AP Physics C courses** likewise do not prescribe them. This is enrichment for these physics courses, not a new examinable formula list.

### A useful chemistry bridge

**Cambridge 9701 Chemistry (2028–2030), §1.3** does require shells/subshells/orbitals, capacities of s/p/d subshells, electronic configurations, and electrons-in-boxes notation for ground-state atoms/ions through krypton. The orbital-occupation discussion helps explain those requirements; the complete configuration syllabus, including transition-metal details, is broader than the few examples here. Antisymmetric wavefunctions and the Fermi-gas derivation are not required there.

## Connections

- **Prerequisites:** [[Quantum States and the Schrödinger Equation]] derives the infinite-well modes and $E_j\propto j^2/L^2$; [[Wave-Particle Duality]] supplies matter waves; [[Energy Levels and Line Spectra]] distinguishes energies from transitions; [[Integration]] supplies the state-counting integral.
- **Application peer:** [[Stellar Evolution]] uses degeneracy pressure in a computed white-dwarf mass–radius sequence.
- **Human companion:** [[Wolfgang Pauli and the Number 137]] — the critic behind the rule.
- **Thermal contrast:** [[Kinetic Theory and the Ideal Gas]] and [[Internal Energy]] — the classical regime and what changes when state occupation matters.
- **Mathematical connection:** [[Determinants and Inverses]] — exchanging two determinant rows reverses its sign; equal rows make it zero.
- **Technology neighbours:** [[Quantum Tunnelling]] — how barrier transmission works once allowed states and occupations have been specified; [[Magnetism and Magnetic Materials]] — spin and electron interactions in matter.

## Beyond Syllabus — taking the model further

### From two terms to a Slater determinant

Recall that our two-electron state subtracts the two possible assignments of complete orbitals. For $N$ orthonormal spin-orbitals, put the values $\chi_j(q_i)$ in a matrix and form

$$\Psi(q_1,\ldots,q_N)=\frac{1}{\sqrt{N!}}\det[\chi_j(q_i)].$$

Swapping particles exchanges rows, giving the required minus sign. Repeating an orbital duplicates columns, giving zero. This is a **Slater determinant**. A general correlated fermion state is a superposition of determinants; one determinant is an approximation for many interacting systems, not a universal exact solution.

### Why a white dwarf has a mass limit

Recall that the cold, nonrelativistic electron pressure scales as $n_e^{5/3}$. In an ionised white dwarf of fixed composition, ions supply most of the mass while electrons supply most of this pressure. Being “cold” means $T\ll T_F$; the star need not feel cold to a human.

At sufficiently high density, $p_F$ approaches $m_ec$ and $E=p^2/(2m_e)$ fails. In the ultrarelativistic limit, $E\approx pc$: the same spherical state count gives $U\propto N^{4/3}V^{-1/3}$ and $P\propto n_e^{4/3}$. Pressure now stiffens more slowly with compression.

For a rough uniform-density star, $n_e\propto M/R^3$, so this pressure scales as $M^{4/3}/R^4$, while the gravitational pressure scale is $GM^2/R^4$. Radius cancels in the balance: shrinking cannot save an arbitrarily massive object. The detailed hydrostatic calculation gives the Chandrasekhar limit near $1.4$ solar masses for the usual composition; [[Stellar Evolution]] supplies the computed sequence.

The principle is **not violated** above the limit. Electron degeneracy alone no longer supports equilibrium. Neutron-star support additionally requires strong-interaction physics and relativistic gravity; “replace electrons by neutrons” is only a first sketch.

### A transition needs an empty destination

Recall that exclusion limits the **final** state as well as the starting configuration. Light scattering can give a fermionic atom recoil momentum. If its destination state is occupied, that process is blocked. A 2021 experiment observed suppressed scattering in a dense, ultracold lithium Fermi gas. This is an unusually direct laboratory view of unavailable states affecting an observable rate. It does not mean ordinary objects become invisible when cooled. [Original experiment: Margalit, Lu and Ketterle](https://arxiv.org/abs/2103.06921).

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\Psi(q_2,q_1)=-\Psi(q_1,q_2)$ | `\Psi(q_2,q_1)=-\Psi(q_1,q_2)` | Fermionic exchange |
| $m_s=\pm\tfrac12$ | `m_s=\pm\tfrac12` | Electron spin projections |
| $E_j=j^2\pi^2\hbar^2/(2mL^2)$ | `E_j=j^2\pi^2\hbar^2/(2mL^2)` | 1-D infinite-well energies |
| $k_F=(3\pi^2n_e)^{1/3}$ | `k_F=(3\pi^2n_e)^{1/3}` | 3-D ideal gas, two spin states |
| $P=\tfrac25 n_eE_F$ | `P=\tfrac25 n_eE_F` | Nonrelativistic $T=0$ pressure |
| $f(E)=[e^{(E-\mu)/(k_BT)}+1]^{-1}$ | `f(E)=[e^{(E-\mu)/(k_BT)}+1]^{-1}` | Fermi–Dirac occupation |

---
chinese: 阻尼振动 (zǔní zhèndòng)
prerequisites:
  - "[[Simple Harmonic Motion]]"
  - "[[Second-Order Differential Equations]]"
  - "[[Exponential Growth and Decay]]"
leads_to:
  - "[[Resonance]]"
  - "[[Stories/From the Grid to the Garage]]"
  - "[[From the Grid to the Garage]]"
tags:
  - subject/physics
  - domain/oscillations
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - syllabus/9702-17-3
  - syllabus/IB-Physics-C-4-3
  - type/deep
  - type/definition
  - type/proof
  - notation/damping-coefficient-b
  - notation/gamma-damping-constant
  - notation/omega-d-damped-frequency
  - notation/Q-factor
  - misconception/heavier-damping-returns-faster
  - misconception/equal-amplitude-loss-per-cycle
  - misconception/energy-decays-like-amplitude
  - misconception/critical-damping-means-no-motion
---

# Damped Oscillations 阻尼振动

## Definition

### Formal

An oscillation is **damped** when a **resistive force**, acting opposite to the velocity, continuously removes energy from the oscillating system, so the amplitude decreases with time. In the standard model the resistive force is proportional to speed, and Newton's second law for a mass $m$ on a spring of constant $k$ reads

$$m\,\frac{d^2x}{dt^2} \;=\; \underbrace{-\,kx}_{\text{spring pulls home}}\; \underbrace{-\;b\,\frac{dx}{dt}}_{\text{drag opposes motion}} \qquad\Longleftrightarrow\qquad m\,\frac{d^2x}{dt^2} + b\,\frac{dx}{dt} + kx = 0.$$

That second term is not an abstraction — it is a force you have met: the air dragging on a pendulum bob, the oil being squeezed through the small holes of a car's shock-absorber piston, the eddy currents braking a meter needle's coil. Each is a force that grows with speed and pushes *against* the motion — which is exactly what $-b\,\frac{dx}{dt}$ says. The new constant $b$ is the **damping coefficient** (units $\text{kg s}^{-1}$, equivalently $\text{N}$ per $\text{m s}^{-1}$): how many newtons of resistance each metre-per-second of speed costs. Set $b = 0$ and the equation collapses back to [[Simple Harmonic Motion]]: SHM is the frictionless special case of this equation.

### Intuitive

SHM is a beautiful fiction: energy sloshing between kinetic and potential forever, no losses. The real world charges a toll on every pass — air drag on the pendulum bob, viscous oil in the shock absorber, internal friction flexing the spring's own metal. The $-b\,\frac{dx}{dt}$ term is that toll, and the whole subject is a single contest: **the spring fights to swing the mass; the drag taxes every move.** Who wins decides one of exactly three fates. Picture the same mass-on-spring dunked in three jars — air, oil, honey:

- **air** — the spring wins: the mass *rings*, oscillating inside a shrinking envelope (**light damping** 轻阻尼). This is every bell, guitar string and struck wine glass — things built so the ring *is* the product;
- **oil, tuned just right** — a draw: the mass glides home in the shortest possible time and stops, no overshoot (**critical damping** 临界阻尼). This is a car's shock absorber — which really is a piston forcing oil through small holes, sized so one pothole means one dip and no bounce;
- **honey** — the drag wins: no oscillation, just a slow *crawl* back to equilibrium (**heavy damping** 重阻尼). This is the dashpot inside a soft-close drawer or door hinge — a piston in thick fluid, so it glides shut and *cannot* slam however hard it is shoved.

Watch the race — the same spring in all three jars, pulled down the same distance and released together:

![[damped-oscillations-lab.mp4]]

The surprise worth the whole topic is in that finish order: the honey jar is *slower* than the tuned one. More friction does **not** mean settling sooner — strong drag fights the return journey too.

### 中文锚点

**阻尼振动 (zǔní zhèndòng)** = 振幅随时间衰减的振动；能量被阻力不断带走。

| English | 中文 | Symbol / idea |
|---|---|---|
| Damping | 阻尼 (zǔní) | energy removal by a resistive force |
| Resistive force | 阻力 (zǔlì) | $-b\,\frac{dx}{dt}$, opposes velocity |
| Damping coefficient | 阻尼系数 (zǔní xìshù) | $b$, units $\text{kg s}^{-1}$ |
| Light / under-damping | 轻阻尼 / 欠阻尼 (qiàn zǔní) | rings inside a decaying envelope |
| Critical damping | 临界阻尼 (línjiè zǔní) | fastest return, no overshoot |
| Heavy / over-damping | 重阻尼 / 过阻尼 (guò zǔní) | slow crawl, no oscillation |
| Envelope | 包络线 (bāoluòxiàn) | the $\pm A_0e^{-\gamma t}$ cage the ring lives in |
| Natural frequency | 固有频率 (gùyǒu pínlǜ) | $\omega_0 = \sqrt{k/m}$, the undamped value |
| Quality factor | 品质因数 (pǐnzhì yīnshù) | $Q$ — how many swings the ring survives |

Cambridge says **light / critical / heavy**; Chinese textbooks and all engineering literature say 欠阻尼 / 临界阻尼 / 过阻尼 (**under / critical / over**). Same three regimes, two naming families — exams accept the Cambridge set.

---

## Where drag gets its shape — why $-bv$

The resistive forces of the real world form a family: air drag at low speeds, viscous drag in liquids, eddy-current braking on a conductor swinging through a magnetic field, internal friction in a flexing material. Why do we model them all as *proportional to velocity*?

The same argument that made Hooke's law universal. A smooth resistive force must (i) vanish when the motion stops — no velocity, nothing to resist — and (ii) oppose whichever direction the motion takes. Write it as a function of velocity $F(v)$ and Taylor-expand about $v = 0$: the constant term is zero by (i), so the leading term is linear, $F \approx -bv$, with $b > 0$ by (ii). Recall that [[Hooke's Law for Springs]] earns $F \approx -kx$ by the identical expansion about the equilibrium *position*. So the damped-oscillator equation is what motion looks like when you keep the leading term of everything:

$$m\,\frac{d^2x}{dt^2} = \underbrace{-kx}_{\text{first word of the spring's story}} \underbrace{-\,bv}_{\text{first word of the drag's story}}$$

That is why this one equation — with its electrical costume, the RLC circuit — describes car suspensions, swaying bridges, ringing bells, and radio tuners alike: near equilibrium and at modest speeds, *everything* is this equation.

(The honest edge: **dry sliding friction** breaks the pattern — its magnitude is roughly constant, not proportional to $v$, and it damps in a recognisably different way. See §Beyond Syllabus.)

---

## One equation, three fates — the damping dial

Divide the equation of motion by $m$ and give the two competing quantities their own names:

$$\frac{d^2x}{dt^2} + 2\gamma\,\frac{dx}{dt} + \omega_0^2\,x = 0, \qquad \omega_0 = \sqrt{\frac{k}{m}}, \qquad \gamma = \frac{b}{2m}.$$

- $\omega_0$ — the **natural angular frequency**: how fast the system *would* oscillate undamped. The spring's ambition.
- $\gamma$ — the **damping constant** (units $\text{s}^{-1}$): the rate at which drag eats amplitude. The tax rate. (The $2$ in $\gamma = b/2m$ is a convention that keeps every later formula clean.)

*Tool: the auxiliary equation from [[Second-Order Differential Equations]]* — try $x = e^{\lambda t}$, and the calculus collapses into a quadratic:

$$\lambda^2 + 2\gamma\lambda + \omega_0^2 = 0 \qquad\Longrightarrow\qquad \lambda = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}.$$

Everything hangs on the sign of the discriminant — literally the contest **drag vs spring**, $\gamma$ vs $\omega_0$:

| Regime | Condition | Motion $x(t)$ | Behaviour |
|---|---|---|---|
| **Light** (under) | $\gamma < \omega_0$ | $A_0\,e^{-\gamma t}\cos(\omega_d t + \phi)$ | rings inside a decaying envelope |
| **Critical** | $\gamma = \omega_0$ | $(A + Bt)\,e^{-\gamma t}$ | fastest return, no overshoot |
| **Heavy** (over) | $\gamma > \omega_0$ | $Ae^{\lambda_1 t} + Be^{\lambda_2 t}$, both $\lambda < 0$ | slow crawl, no oscillation |

These are the three auxiliary-equation cases of [[Second-Order Differential Equations]] wearing units: complex roots, repeated root, distinct real roots. (Watch the roots collide on the real axis and split into a conjugate pair as the dial turns, in that card's §"One machine, one dial" animation.)

The displacement–time graphs the three jars drew in the race — redrawn as the exact figure the exam asks you to sketch:

![[damped-oscillations-three-regimes.svg|760]]

> [!info] Why heavy damping crawls — the slow root
> Heavy damping's two decay rates are $\lambda = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$, and the motion is soon dominated by the *slower* one, $\lambda_{\text{slow}} = -\gamma + \sqrt{\gamma^2 - \omega_0^2}$. Recall the [[Binomial Series]] approximation $\sqrt{1 - u} \approx 1 - \tfrac{u}{2}$ for small $u$ — it is the fractional-power binomial expansion of $(1-u)^{1/2}$, worked term by term in [[Binomial Series]] §"Worked Example — $(1 + x)^{1/2}$". You can also *verify it by squaring*: $\left(1 - \tfrac{u}{2}\right)^2 = 1 - u + \tfrac{u^2}{4}$, which misses the target $1 - u$ only by $u^2/4$ — doubly small when $u$ is small. For strong damping ($\gamma \gg \omega_0$),
>
> $$\lambda_{\text{slow}} = -\gamma + \gamma\sqrt{1 - \tfrac{\omega_0^2}{\gamma^2}} \;\approx\; -\gamma + \gamma\left(1 - \frac{\omega_0^2}{2\gamma^2}\right) = -\frac{\omega_0^2}{2\gamma} \;=\; -\frac{k}{b}.$$
>
> As the damping grows, the decay rate $k/b$ shrinks toward zero — *stronger drag, slower return*. And look at what survived: $m$ has dropped out. In the heavy limit the mass's inertia is irrelevant; the crawl is a private fight between spring and drag ($bv \approx -kx$), the spring dragging the mass through treacle at whatever speed the drag permits. That is why the honey jar loses the race to the tuned oil.

---

## Light damping up close — the ring in a shrinking cage

For $\gamma < \omega_0$ the solution (from Case 3 of the auxiliary equation, via Euler's formula) is

$$x(t) = A_0\,e^{-\gamma t}\cos(\omega_d t + \phi), \qquad \omega_d = \sqrt{\omega_0^2 - \gamma^2}.$$

The cosine is the bird; $\pm A_0 e^{-\gamma t}$ is the shrinking cage it flies in. The word **envelope** means exactly that cage: the pair of mirror curves $+A_0e^{-\gamma t}$ and $-A_0e^{-\gamma t}$ drawn *through the peaks* of the oscillation. The wiggling curve never leaves the region between them and touches them once per half-swing — so the envelope is nothing mysterious: it is **the graph of the amplitude itself**, the motion's *size* with the wiggle ignored. Two facts about this picture carry all the exam marks and most of the physics:

**1. The envelope is exponential — equal *ratios*, not equal amounts.** The amplitude loses a constant *fraction* each cycle, never a constant amount: successive peaks obey

$$\frac{A_{n+1}}{A_n} = e^{-\gamma T_d} = \text{constant}.$$

This is the memoryless decay law of [[Exponential Growth and Decay]] — the same mathematics as radioactive decay and the RC discharge in [[Capacitors]] — so the amplitude has a **half-life**, $t_{1/2} = \ln 2/\gamma$, and the oscillation never *quite* reaches zero (in this idealised model). Reading a real trace backwards: measure two peaks $n$ cycles apart and the decay constant falls out as $\gamma = \dfrac{1}{nT_d}\ln\dfrac{A_0}{A_n}$ — this is how a lab measures damping.

**2. Damping slows the clock — slightly.** The ringing frequency $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ sits *below* the natural frequency, so the period is slightly *longer* than the undamped $T_0$. For genuinely light damping the shift is tiny: at $\gamma = \omega_0/10$, $\omega_d = \omega_0\sqrt{1 - 0.01} \approx 0.995\,\omega_0$ — half a percent. A bell's pitch barely flattens as its ring fades; on an exam sketch, draw the zero-crossings (approximately) equally spaced.

![[damped-oscillations-envelope.svg|760]]

---

## The energy story — where the motion goes

Damping is defined by energy loss, so track the energy directly. *Tool: the energy method from [[Simple Harmonic Motion]] Route 2* — differentiate the total mechanical energy and let Newton's law speak:

$$E = \tfrac{1}{2}mv^2 + \tfrac{1}{2}kx^2 \quad\Longrightarrow\quad \frac{dE}{dt} = mv\,\frac{dv}{dt} + kx\,\frac{dx}{dt} = v\,(ma + kx).$$

Why is that bracket $-bv$? *Tool: the equation of motion itself.* Newton's second law for this system is $ma = -kx - bv$; move the spring term over and the bracket collapses to the resistive force alone:

$$ma + kx = -bv \qquad\Longrightarrow\qquad \frac{dE}{dt} = v\,(-bv) = -\,b\,v^2 \;\le\; 0.$$

(Check the logic against the undamped case: for pure SHM, $ma = -kx$, the bracket is *zero*, and the same calculation gave $dE/dt = 0$ — conservation. The bracket measures exactly the force that isn't the spring.)

Three readings of that one line:

- **The sign is the definition.** $dE/dt \le 0$ always: energy only ever leaves, converted to heat in the resisting medium. (Undamped SHM is the special case $b=0$, where the same calculation gave $dE/dt = 0$ — conservation.)
- **Energy leaves in pulses.** The drain rate $bv^2$ is largest where the speed is largest — the equilibrium crossings — and *zero* at the turning points, where the mass is momentarily at rest. Energy leaves twice per cycle, in bursts, not smoothly.
- **Energy decays twice as fast as amplitude.** Recall from [[Simple Harmonic Motion]] that $A$ is the **amplitude** — the largest displacement of the swing — and that the total energy equals the elastic PE at the turning point, $E = \tfrac{1}{2}kA^2$ (at $x = \pm A$ the mass is momentarily at rest, so *all* the energy sits in the spring). In a damped oscillator the amplitude is no longer a constant: it *is* the envelope, $A(t) = A_0e^{-\gamma t}$. Squaring it,

$$E(t) = E_0\,e^{-2\gamma t}$$

— squaring the envelope doubles the decay rate. The energy half-life is *half* the amplitude half-life. An oscillator whose amplitude has fallen to $70\%$ has already lost *half* its energy.

The figure below stacks the two stories on one clock. **Top panel:** the displacement $x(t)$ with its envelope — the dashed curve through the peaks is the amplitude $A(t) = A_0e^{-\gamma t}$. **Bottom panel:** the energy. The dashed red curve is the envelope's *square*, $e^{-2\gamma t}$ — the smooth law the energy follows on average — and the solid teal curve is the *actual* energy $\tfrac12mv^2 + \tfrac12kx^2$, rippling around it because the drain $bv^2$ comes in pulses: look straight down from any peak in the top panel (a turning point, $v=0$) and the teal curve is momentarily flat there.

![[damped-oscillations-energy-decay.svg|760]]

---

## The quality factor — counting the ring

How lightly damped is "lightly damped"? Engineers and physicists compress the answer into one dimensionless dial, the **quality factor**. It is defined by energy bookkeeping:

$$Q = 2\pi \times \frac{\text{energy stored}}{\text{energy lost per cycle}} \;\approx\; \frac{\omega_0}{2\gamma},$$

with the right-hand form holding for light damping. The practical reading: **$Q$ counts the swings the ring survives.** After $Q$ full oscillations the amplitude has fallen to $e^{-\pi} \approx 4\%$ (the energy to $0.2\%$) — the ring is over. A high-$Q$ oscillator is a long rememberer of its own frequency; a low-$Q$ oscillator forgets almost immediately. Critical damping sits at $Q = \tfrac{1}{2}$.

Watch the rule work — a swing counter ticking while the envelope shrinks, freezing when the ring is spent:

![[damped-oscillations-q-counter.mp4]]

| Oscillator                                       | $Q$ (order of magnitude)               |
| ------------------------------------------------ | -------------------------------------- |
| Door closer, soft-close drawer                   | $\sim 0.5$ (critical — no ring at all) |
| Car suspension                                   | $\sim 1$                               |
| Child on a playground swing                      | $\sim 10^2$                            |
| The Earth, ringing after a great earthquake      | $\sim 10^2\text{–}10^3$                |
| Guitar string                                    | $\sim 10^3$                            |
| Tuning fork                                      | $\sim 10^4$                            |
| Quartz watch crystal                             | $\sim 10^5$                            |
| Excited atom emitting light                      | $\sim 10^7$                            |
| Caesium clock transition (defines the SI second) | $\sim 10^{10}$                         |

The ladder is the point: *the better a system keeps time, the higher its $Q$* — a quartz watch beats a pendulum clock beats a wristwatch spring, and the caesium atom beats everything, which is why the second is defined by it. $Q$ returns in [[Resonance]] wearing its other hat: the same number that counts the ring also sets the height and sharpness of the resonance peak.

---

## Worked examples — every tool named

### Example 1 — classify, then describe the decay

> A $0.50~\text{kg}$ mass hangs from a spring of constant $k = 50~\text{N m}^{-1}$, immersed in a fluid that exerts a resistive force of $2.0~\text{N}$ per $\text{m s}^{-1}$ of speed. The mass is pulled down $40~\text{mm}$ and released. Classify the damping and describe the subsequent motion quantitatively.

*Tool: the natural frequency — $\omega_0 = \sqrt{k/m}$.*
$$\omega_0 = \sqrt{50/0.50} = 10~\text{rad s}^{-1}.$$

*Tool: the damping constant — $\gamma = b/2m$.*
$$\gamma = \frac{2.0}{2 \times 0.50} = 2.0~\text{s}^{-1}.$$

*Tool: the dial — compare $\gamma$ with $\omega_0$.* $\;\gamma = 2.0 < 10 = \omega_0$: **light damping**. The mass rings.

*Tool: the damped frequency — $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$.*
$$\omega_d = \sqrt{100 - 4} = 9.80~\text{rad s}^{-1} \quad\Longrightarrow\quad T_d = \frac{2\pi}{\omega_d} = 0.641~\text{s},$$
about $2\%$ longer than the undamped $T_0 = 0.628~\text{s}$ — the clock barely notices.

*Tool: the envelope — $A(t) = A_0e^{-\gamma t}$, half-life $\ln 2/\gamma$.* The amplitude is $40\,e^{-2.0t}~\text{mm}$: it halves every $\ln 2/2.0 = 0.35~\text{s}$, and one second after release only $40e^{-2} \approx 5.4~\text{mm}$ remains. Each successive peak is $e^{-\gamma T_d} = e^{-1.28} \approx 28\%$ of the one before.

*Tool: energy decays at twice the rate — $E \propto A^2$.* The energy half-life is $0.17~\text{s}$; the ring is effectively dead within a couple of swings — consistent with $Q = \omega_0/2\gamma = 2.5$.

### Example 2 — design for critical damping (the engineer's question)

> A quarter-car model puts $m = 350~\text{kg}$ on one suspension spring of constant $k = 2.0 \times 10^4~\text{N m}^{-1}$. (a) What damping coefficient should the shock absorber provide for critical damping? (b) A worn shock absorber has lost half its damping. Describe what the passengers feel after a pothole.

**(a)** *Tool: the critical-damping boundary — $b = 2\sqrt{mk}$, the repeated-root condition derived in [[Second-Order Differential Equations]] §"Critical damping — the engineer's target".*

$$b_{\text{crit}} = 2\sqrt{350 \times 2.0\times10^4} = 2\sqrt{7.0\times10^6} \approx 5.3 \times 10^3~\text{kg s}^{-1}.$$

(Sanity check the setup: $\omega_0 = \sqrt{k/m} = 7.6~\text{rad s}^{-1}$, i.e. $f_0 \approx 1.2~\text{Hz}$ — real cars ride at about $1$–$1.5~\text{Hz}$, the frequency of a relaxed walking pace, which is part of why a well-damped car feels calm.)

**(b)** *Tool: the dial again.* Half the damping means $\gamma = \omega_0/2 < \omega_0$: the suspension is now **lightly damped**. *Tool: the damped frequency.* $\omega_d = \omega_0\sqrt{1 - \tfrac{1}{4}} = 0.87\,\omega_0$. *Tool: the envelope, per half-cycle.* After the pothole compresses the spring, the body overshoots by $e^{-\gamma T_d/2} = e^{-1.8} \approx 16\%$ of the initial compression and bobs visibly before settling — the "floaty boat" feel of worn shocks. This is exactly the roadside test: push down hard on a car's corner and let go; **more than about one bounce means the dampers need replacing.**

---

## The three regimes in the wild

Each regime is a *product*, engineered on purpose — none of the three is a failure mode:

![[second-order-de-damping-comic.png|700]]

- **Critical (or just above): things that must arrive and stop.** Door closers and soft-close drawers (must never slam, however hard they're shoved); moving-coil meter needles (must fly to the reading and hold it — a ringing needle can't be read, a sluggish one wastes the measurement); a seismometer's pen (must follow the ground faithfully without adding its own ring).
- **Slightly under critical: vehicle suspension.** A car tuned exactly at critical rides harshly, so road cars sit a little under ($Q$ near 1) — one gentle bob per bump, comfort bought with a controlled trace of ring. Example 2's worn-shock test is this dial drifting too far under.
- **Light, on purpose: things whose ring *is* the product.** Bells, guitar strings, tuning forks, wine glasses — a heavily damped bell is a paperweight. The whole point is a high $Q$: the ring outliving the strike by thousands of cycles.
- **Added damping at building scale.** Skyscrapers are lightly damped pendulums standing upside down, so engineers *install* the missing damping: Taipei 101 hangs a $660$-tonne steel sphere near its top — a pendulum coupled to the tower through giant hydraulic dampers, drinking the sway energy of typhoon winds. (During Typhoon Soudelor in 2015 the sphere swung a full metre.) What happens when the wind's rhythm *matches* the tower's natural frequency is the subject of [[Resonance]].

---

## Common Misconceptions (Teaching Notes)

### 1. "More damping means it settles faster"

The single best exam trap in the topic. True only up to critical; past it, stronger damping settles *slower* — the honey crawl, decay rate $\approx k/b \to 0$ as $b$ grows.

**Fix:** the three-jar race (honey loses to oil), plus the slow-root calculation in §"One equation, three fates". Critical damping is *defined* as the fastest return without overshoot — that's why engineers hunt for it rather than just adding more drag.

### 2. "The amplitude decreases by the same amount each cycle"

Students draw a straight-line (triangular) envelope. The viscous envelope is exponential: equal *ratios* per cycle, not equal *amounts* — 100 → 50 → 25 → 12.5, never 100 → 75 → 50 → 25.

**Fix:** measure successive peaks on any trace and divide: the ratio is constant. Straight-line decay is the fingerprint of *dry friction* damping, a genuinely different mechanism (§Beyond Syllabus) — a distinction that makes both models sharper.

### 3. "Energy decays at the same rate as amplitude"

$E \propto A^2$, so energy decays at *twice* the rate: envelope $e^{-\gamma t}$, energy $e^{-2\gamma t}$. When the amplitude has dropped to 70%, half the energy is already gone.

**Fix:** square the envelope. Same trap, same fix as intensity-vs-amplitude for waves.

### 4. "Damping changes the frequency a lot" / "damping doesn't change it at all"

Both wrong, in the exam-relevant regime: $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ is *slightly* below $\omega_0$ — about $0.5\%$ at $\gamma = \omega_0/10$. Sketches should show a period marginally longer than undamped, with zero-crossings still (approximately) evenly spaced.

**Fix:** compute $\sqrt{1 - 0.01}$ once. The mark-scheme phrase is "period slightly increased / approximately constant".

### 5. "Critically damped means it doesn't move"

Critical damping is not a freeze — the system moves, fast, and arrives without overshoot. Nothing physical stops instantly (that would need infinite force).

**Fix:** the door-closer: it plainly *moves*, it just never slams or rebounds.

---

## Exam Notes

### Cambridge 9702 (§17.3 — the damping half)

- Two learning objectives live here: **(1)** *understand that a resistive force acting on an oscillating system causes damping* — the expected sentence is "damping is the reduction in amplitude of an oscillation because a resistive force removes energy from the system"; name the force, name the energy loss. **(2)** *understand and use the terms light, critical and heavy damping and sketch displacement–time graphs illustrating these types of damping.* (The third objective in §17.3 — resonance — is the business of [[Resonance]].)
- **What each sketch must show.** *Light:* several cycles inside an exponentially decaying envelope, period approximately constant (equally spaced zero-crossings). *Critical:* directly back to zero in the shortest time, no crossing of the axis. *Heavy:* same shape as critical but visibly slower, no crossing. Draw the light-damping envelope with visibly *shrinking* equal-ratio steps, never as two straight lines.
- The treatment demanded is **qualitative and graphical** — the ODE, $\gamma$, $\omega_d$ and $Q$ in the sections above are the college-ready *why* behind the sketches, not required working. (Nothing about damping appears on the 9702 formula sheet; the SHM formulas that do are catalogued in [[Simple Harmonic Motion]] §"Formula sheet status".)
- Favourite phrasing traps: "the frequency of a lightly damped oscillator is *slightly less* than the natural frequency" (true — accept), and energy questions that expect "energy is transferred to internal (thermal) energy of the surroundings/medium", not "energy is lost".

### IB Physics (C.4.3 — the damping half)

- C.4.3 asks for the *qualitative* distinction between light, critical and heavy damping alongside its resonance content. Same three sketches, same vocabulary as 9702; the resonance half of the row (natural vs driving frequency, useful and destructive examples) belongs to [[Resonance]].
- IB papers like the energy chain: amplitude ↓ because total energy ↓ because the resistive force does negative work on the oscillator.

### A-Level Further Mathematics (Edexcel / AQA / OCR)

- The *quantitative* version — solve the equation of motion in full, classify the damping from the discriminant, interpret the motion — is examined on the **Further Maths** papers, not the physics ones: a pleasing inversion. The full technique lives in [[Second-Order Differential Equations]] (its Exam Notes map the boards); the physics vocabulary for reading those answers lives on this page.

### AP Physics

- AP Physics 1 and AP Physics C (Mechanics) build the SHM machinery ([[Simple Harmonic Motion]]) but do **not** assess damped motion beyond the qualitative fact that friction drains amplitude. Don't spend AP revision time on the three regimes.

### Where it is *not* examined

- **0625 IGCSE:** no damping content — oscillations enter only through waves.
- **9709:** no second-order differential equations, no damping.
- **9231:** Further Mechanics stops at undamped SHM; damped systems appear only as *modelling contexts* inside FP2 §2.6 differential-equation questions — which is exactly [[Second-Order Differential Equations]] territory.

---

## Connections

- **Parent:** [[Simple Harmonic Motion]] — the frictionless limit $b \to 0$, and the source of the energy method used here. Its §"Damping — when energy leaks out" preview is delivered in full here.
- **Mathematical engine:** [[Second-Order Differential Equations]] — the three-case auxiliary-equation dial *is* the classification used here (complex / repeated / distinct real roots = light / critical / heavy), and the critical boundary $b = 2\sqrt{mk}$ is derived there. One dial, two costumes.
- **The envelope:** [[Exponential Growth and Decay]] — $e^{-\gamma t}$ is the memoryless constant-fraction law, shared with [[Radioactive Decay]] and the RC discharge in [[Capacitors]].
- **Electrical costume:** [[Capacitors]] — add an inductor to the RC circuit and the series RLC obeys this exact equation: $L \leftrightarrow m$, $R \leftrightarrow b$, $1/C \leftrightarrow k$. A radio's tuned circuit is a lightly damped oscillator whose high $Q$ is what lets it pick one station from the dial.
- **Friction cousin:** [[The Friction Limit]] — dry sliding friction damps with constant-magnitude force, producing the linear decay of §Beyond Syllabus rather than the exponential envelope.
- **Child:** [[Resonance]] — switch on a periodic driving force and the transient ring described here gives way to a steady forced response whose peak height and sharpness are set by the same $Q$.
- **Engineering follow-up — reserved:** [[Suspension]] — the quarter-car of Example 2 grown into a full engineering story: comfort vs grip as competing objectives, what overdamping feels like, dampers whose $b$ varies with speed and direction, semi-active and fully active systems, and the inerter that completed the RLC analogy's missing element.
- **Story:** [[Stories/The Pendulum Story]] — four centuries of clockmaking are a war against damping: the escapement exists to pay back, tick by tick, exactly the energy each swing loses.
- **Story:** [[Stories/From the Grid to the Garage]] — the suspension arms race (active systems, the mass damper, the inerter) as one thread in the century of racing-and-road technology, and the EV reversal that ended it.

---

## Beyond Syllabus

### Dry friction damps differently — the straight-line ramp and the dead stop

Recall that dry sliding friction has (roughly) constant magnitude $F$, independent of speed. A mass-spring sliding on a dry surface therefore loses the *same* energy per cycle, and the amplitude falls by a constant amount, $4F/k$ per full cycle — a **linear** envelope, the very shape misconception 2 wrongly draws for viscous damping. And the motion doesn't fade forever: once the amplitude falls inside the **dead zone** $\lvert x \rvert \le F/k$, the spring can no longer overcome static friction and the mass stops *dead*, off-centre, in finite time. Real oscillators carry both mechanisms — viscous drag dominates the early decay, dry friction delivers the final stop. That is why real pendulums actually stop, while the pure viscous model only ever approaches zero.

### The atom's ring — why spectral lines have width

A damped cosine is not a pure frequency: chop $e^{-\gamma t}\cos\omega_0 t$ into its Fourier ingredients and you get a *spread* of frequencies — a Lorentzian peak of width $\Delta\omega \approx 2\gamma$ (full width at half maximum). **The faster the fade, the blurrier the pitch.** An excited atom is a damped oscillator (it rings at its transition frequency while radiating its energy away), so its emitted spectral line has a **natural linewidth** equal to its decay rate — and the quality factor returns as pure spectroscopy: $Q = \omega_0/\Delta\omega$, *sharpness = ring count*. The caesium transition's $Q \sim 10^{10}$ is precisely why locking a clock to it defines the SI second ([[Simple Harmonic Motion]] §"Driven oscillations and resonance").

And the question that ladder invites: damping lowers the ringing frequency ($\omega_d < \omega_0$) — so doesn't the caesium clock tick *slightly wrong*? Two answers. First, the pull is **doubly small**: with $\gamma = \omega_0/2Q$,

$$\omega_d = \omega_0\sqrt{1 - \tfrac{1}{4Q^2}} \;\approx\; \omega_0\left(1 - \frac{1}{8Q^2}\right)$$

— the same binomial move as the heavy-crawl callout — and at $Q \sim 10^{10}$ that is one part in $10^{21}$, a hundred thousand times below even the clock's $10^{-16}$ accuracy. Choosing a high-$Q$ reference doesn't just lengthen the ring; it *squares away* the frequency pull. Second, a real caesium clock never lets its atoms ring freely and fade like a struck bell: a quartz oscillator *drives* them with microwaves, and a feedback loop steers its frequency to the centre of the atomic resonance — the atom is the referee, not the pendulum. The shifts that genuinely matter at the $10^{-16}$ level (stray magnetic fields, blackbody radiation from the warm apparatus, relativistic time dilation — a clock a kilometre higher in the gravitational field really does run measurably faster) are individually measured and subtracted from a published error budget, and international atomic time (TAI) is then a weighted average of several hundred such clocks worldwide, steered by the best of them. The world's timekeeping does follow the caesium atom — but only after every known way the apparatus differs from an *unperturbed* atom has been accounted for.

### The engineer's dial — damping ratio $\zeta$

Engineering condenses the dial into $\zeta = \gamma/\omega_0 = b\,/\,2\sqrt{mk}$: under-damped $\zeta < 1$, critical $\zeta = 1$, over-damped $\zeta > 1$, and $Q = 1/(2\zeta)$. Control theory runs on it — a stated $\zeta$ fixes the overshoot of a step response exactly ($\zeta \approx 0.7$, the ubiquitous "Butterworth" choice, overshoots by just 4%), which is how everything from hard-drive read heads to drone gimbals is tuned to arrive quickly *and* stop cleanly.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = 0$ | `m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = 0` | The damped-oscillator equation |
| $b$ | `b` | Damping coefficient, $\text{kg s}^{-1}$ (maths texts often write $c$) |
| $\gamma = b/2m$ | `\gamma = b/2m` | Damping constant, $\text{s}^{-1}$ — the envelope's decay rate |
| $\omega_0 = \sqrt{k/m}$ | `\omega_0 = \sqrt{k/m}` | Natural angular frequency (undamped) |
| $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ | `\omega_d = \sqrt{\omega_0^2 - \gamma^2}` | Damped angular frequency (light damping) |
| $x = A_0e^{-\gamma t}\cos(\omega_d t + \phi)$ | `x = A_0 e^{-\gamma t}\cos(\omega_d t + \phi)` | Light-damping solution |
| $b = 2\sqrt{mk}$ | `b = 2\sqrt{mk}` | Critical-damping condition |
| $E = E_0e^{-2\gamma t}$ | `E = E_0 e^{-2\gamma t}` | Energy decay — twice the amplitude rate |
| $Q = \omega_0/2\gamma$ | `Q = \omega_0 / 2\gamma` | Quality factor (light damping) |
| $\zeta = \gamma/\omega_0$ | `\zeta = \gamma/\omega_0` | Damping ratio (engineering) |

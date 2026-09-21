---
chinese: 共振 (gòngzhèn)
prerequisites:
  - "[[Simple Harmonic Motion]]"
  - "[[Damped Oscillations]]"
  - "[[Second-Order Differential Equations]]"
  - "[[Alternating Current]]"
leads_to:
  - "[[Ultrasound]]"
  - "[[Coupled Oscillators]]"
  - "[[Suspension]]"
  - "[[Stationary Waves]]"
tags:
  - subject/physics
  - domain/oscillations
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-17-3
  - syllabus/IB-Physics-C-4-3
  - type/deep
  - type/definition
  - type/proof
  - notation/omega-0-natural-frequency
  - notation/omega-driving-frequency
  - notation/Q-factor
  - notation/phi-phase-lag
  - misconception/driven-system-oscillates-at-its-natural-frequency
  - misconception/resonance-amplitude-is-infinite
  - misconception/driver-and-driven-in-phase-at-resonance
  - misconception/more-damping-raises-the-resonant-frequency
  - misconception/tacoma-narrows-was-resonance
---

# Resonance 共振

## Definition

### Formal

A **forced oscillation** (受迫振动) is what a system does when a periodic external force keeps acting on it: after the start-up transient dies away, the system oscillates **at the frequency of the driver**, not at its own natural frequency, with a steady amplitude that depends on how the two frequencies compare. For a mass $m$ on a spring of constant $k$ with a resistive force $-b\,\frac{dx}{dt}$, driven by $F_0\cos\omega t$,

$$m\,\frac{d^2x}{dt^2} + b\,\frac{dx}{dt} + kx = F_0\cos\omega t, \qquad \omega_0 = \sqrt{\frac{k}{m}},\quad \gamma = \frac{b}{2m},\quad Q = \frac{\omega_0}{2\gamma}.$$

**Resonance** (共振) is the condition in which the amplitude of the forced oscillation is a **maximum**, and it occurs when the **driving frequency equals the natural frequency** of the system, $\omega = \omega_0$. Those two clauses — *maximum amplitude* and *driving frequency equals natural frequency* — are the definition the exam awards two marks for, and they are the whole syllabus statement. Everything else on this card is the *why*: why the amplitude peaks there, how tall the peak is, how wide, how long it takes to grow, and what the world does with it.

### Intuitive

Push a child on a swing. You do not push hard; you push *on time* — a small shove at the top of each backswing, when the child is just about to come forward — and within a dozen pushes the swing is going higher than you could ever throw it. Push at the wrong moments, or at some other steady rhythm of your own, and you spend the whole afternoon fighting the swing: half your pushes arrive while it is coming toward you and undo the other half. The swing has a rhythm of its own, the natural frequency; a driver that matches it adds a little energy *every* cycle, and a little every cycle, banked with nothing withdrawn, becomes a lot.

That is the entire idea. Watch it with the exam's own apparatus — a ball on a spring, shaken from above by a platform of fixed amplitude, at three frequencies:

![[resonance-manim.mp4]]

At half the natural frequency the ball meekly follows the platform, a little bigger. At the natural frequency it grows, cycle by cycle, to many times the platform's amplitude before the drag stops the growth. At twice the natural frequency it cannot keep up: it moves *the other way* and barely moves at all. Plot the amplitude each frequency reached against the frequency and you have the **resonance curve**, the one graph this topic is examined on. The second half of the clip shows why the natural frequency is the winner: pushed at $f_0$, the force always points the way the block is already moving, so energy only ever goes in.

### 中文锚点

生活里最好的模型是推秋千。你用不着使多大劲，只要踩着点推：每次秋千荡到最高点、正要往回走的那一瞬间轻轻一推，十来下之后，秋千就荡得老高——你扔什么都扔不了那么高。要是按你自己的节奏乱推，一半的推都撞在迎面荡过来的秋千上，把另一半的劲儿也抵消了，推一下午也荡不高。秋千有自己的节奏，那就是它的固有频率；驱动力的节奏和它合上了，每个周期都往里存一点能量，只存不取，积少成多，就荡得很高。这就是共振：驱动频率等于固有频率时，振幅最大。再想想洗衣机刚开始脱水的时候：转速升上去的途中总有那么一阵猛抖，然后又平稳了。它是穿过了共振点，而不是停在上面。

### 术语对照 (Terms)

**共振 (gòngzhèn)**：受迫振动的振幅达到最大的情形，发生在驱动频率等于固有频率时。

| English | 中文 | Symbol / idea |
|---|---|---|
| Forced oscillation | 受迫振动 (shòupò zhèndòng) | driven by a periodic external force |
| Driving frequency | 驱动频率 (qūdòng pínlǜ) | $\omega$ or $f$ — what the driver imposes |
| Natural frequency | 固有频率 (gùyǒu pínlǜ) | $\omega_0 = \sqrt{k/m}$ — what the system prefers |
| Resonance | 共振 (gòngzhèn) | maximum amplitude, at $\omega = \omega_0$ |
| Resonance curve | 共振曲线 (gòngzhèn qūxiàn) | amplitude against driving frequency |
| Steady state | 稳态 (wěntài) | after the transient has died: constant amplitude |
| Transient | 暂态 / 过渡过程 (zàntài) | the start-up, decaying like a damped oscillation |
| Phase lag | 相位滞后 (xiàngwèi zhìhòu) | $\phi$ — how far $x$ trails the force; $90°$ at resonance |
| Quality factor | 品质因数 (pǐnzhì yīnshù) | $Q$ — peak height and sharpness, from the damping |

---

## Part I — Why timing beats strength: the energy argument

A force does work at the rate $P = Fv$. Over one cycle of a steady oscillation the driver's net contribution is the average of $F(t)\,v(t)$, and that average depends entirely on the **phase** between the force and the velocity:

- force **in step with the velocity** (pushing forward whenever the mass moves forward): $Fv > 0$ all cycle, energy flows in continuously;
- force a quarter cycle out of step with the velocity — which is the same as being *in step with the displacement*: $Fv$ is positive for half of each cycle and negative for the other half, and the net work per cycle is **zero**;
- force **opposing** the velocity: energy flows out.

The steady state is the amplitude at which *energy in per cycle from the driver equals energy out per cycle to the drag*. The drag's bill grows with amplitude (it is $\propto v^2$, so $\propto A^2$), while the driver's deposit grows only $\propto A$; so there is always an amplitude where the two balance, and the system settles there. **Resonance is the frequency at which the driver's deposit per cycle is largest for a given amplitude** — the frequency at which the force is exactly in step with the velocity. Since velocity leads displacement by a quarter cycle in any oscillation, that is the frequency at which the displacement trails the force by **$90°$**. Hold onto that number; it is the most useful fact on this card and the one most students never hear.

![[resonance-phase.svg|1000]]

*The driving force (amber) and the displacement (blue) at three frequencies, from `resonance-curves.py`. Below resonance the mass simply follows the force — the spring is in charge, and pushing harder just stretches it further. Above resonance the mass is always a half cycle behind — inertia is in charge, and by the time the mass has responded the force has reversed. At resonance the lag is exactly a quarter cycle, so the force is in step with the velocity and every push does positive work.*

---

## Part II — The steady state, solved

The driven equation is [[Second-Order Differential Equations]] with a $\cos\omega t$ on the right, and that card's structure applies: the general solution is a **complementary function** plus a **particular integral**. The complementary function is the damped ring of [[Damped Oscillations]], multiplied by $e^{-\gamma t}$, so it dies — that is the **transient**. The particular integral does not die; it is the **steady state**, and it is the only thing left after a few multiples of $1/\gamma$. So the question is just: *find one particular solution.*

### Step 1 — decide what to look for

The equation is linear and the forcing is a cosine at frequency $\omega$. Feed a cosine into a linear system and every term — $x$, $dx/dt$, $d^2x/dt^2$ — is a sinusoid at the *same* frequency, so their sum can only equal $F_0\cos\omega t$ if $x$ itself is a sinusoid at $\omega$. What the system is free to choose is the **size** and the **delay**. So the trial is

$$x = A\cos(\omega t - \phi),$$

two unknowns, $A$ and $\phi$, and the equation must hold at *every* instant $t$ — which will turn out to give exactly two conditions.

### Step 2 — substitute (the route with no complex numbers)

Differentiate the trial twice:

$$\frac{dx}{dt} = -A\omega\sin(\omega t - \phi), \qquad \frac{d^2x}{dt^2} = -A\omega^2\cos(\omega t - \phi).$$

Put them into $m\,\frac{d^2x}{dt^2} + b\,\frac{dx}{dt} + kx = F_0\cos\omega t$ and collect the left-hand side:

$$A\,(k - m\omega^2)\cos(\omega t - \phi) \;-\; A\,b\omega\,\sin(\omega t - \phi) \;=\; F_0\cos\omega t.$$

The right-hand side is written in terms of $\omega t$, the left in terms of $\omega t - \phi$. Put them in the same terms: $\omega t = (\omega t - \phi) + \phi$, so by the compound-angle formula

$$F_0\cos\omega t = F_0\cos\phi\,\cos(\omega t - \phi) \;-\; F_0\sin\phi\,\sin(\omega t - \phi).$$

Now both sides are "something × $\cos(\omega t-\phi)$ + something × $\sin(\omega t-\phi)$", and since $\cos$ and $\sin$ of the same angle are independent functions, an identity holding for all $t$ needs the two somethings to match separately:

$$A\,(k - m\omega^2) = F_0\cos\phi, \qquad A\,b\omega = F_0\sin\phi.$$

Those are the two conditions. **Divide** the second by the first and $A$ and $F_0$ cancel:

$$\tan\phi = \frac{b\omega}{k - m\omega^2}.$$

**Square and add** them and $\phi$ disappears, because $\cos^2\phi + \sin^2\phi = 1$:

$$A^2\left[(k - m\omega^2)^2 + (b\omega)^2\right] = F_0^2 \quad\Longrightarrow\quad A = \frac{F_0}{\sqrt{(k - m\omega^2)^2 + (b\omega)^2}}.$$

That is the whole solution. To write it in the damped card's letters, divide numerator and denominator by $m$, using $k/m = \omega_0^2$ and $b/m = 2\gamma$:

$$\boxed{\,A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2}}, \qquad \tan\phi = \frac{2\gamma\omega}{\omega_0^2-\omega^2}\,}$$

with $x = A\cos(\omega t - \phi)$.

### Step 3 — the same thing with $i$, in three lines

Recall from [[Alternating Current]] that $e^{i\theta} = \cos\theta + i\sin\theta$, so $F_0\cos\omega t$ is the **real part** of $F_0e^{i\omega t}$. The equation is linear with real coefficients, so if a complex function $z(t)$ satisfies it with the complex force $F_0e^{i\omega t}$, then the real part of $z$ satisfies it with the real force — the real and imaginary parts never mix. And the complex exponential has one property that does all the work: $\frac{d}{dt}e^{i\omega t} = i\omega\,e^{i\omega t}$, so *every derivative is just a multiplication by $i\omega$.* Try $z = Xe^{i\omega t}$ with $X$ a complex constant:

$$\left(m(i\omega)^2 + b(i\omega) + k\right)X e^{i\omega t} = F_0e^{i\omega t} \quad\Longrightarrow\quad X = \frac{F_0}{(k - m\omega^2) + i\,b\omega}.$$

The differential equation has become one line of algebra. To read off $A$ and $\phi$, write the denominator in polar form, $(k - m\omega^2) + i\,b\omega = D\,e^{i\phi}$, where $D$ is its modulus and $\phi$ its argument:

$$D = \sqrt{(k - m\omega^2)^2 + (b\omega)^2}, \qquad \tan\phi = \frac{b\omega}{k - m\omega^2}.$$

Then $X = (F_0/D)\,e^{-i\phi}$, so $z = (F_0/D)\,e^{i(\omega t - \phi)}$, and taking the real part, $x = (F_0/D)\cos(\omega t - \phi)$ — the same $A = F_0/D$ and the same $\phi$ as Step 2. The two trigonometric conditions of the real route are the modulus and argument of one complex number; that is the entire advantage of the method, and why every engineer solves forced-vibration and a.c. problems this way.

### Step 4 — check it where it matters

*At resonance,* $\omega = \omega_0$, so $k - m\omega_0^2 = 0$: the denominator of $\tan\phi$ vanishes, $\phi = 90°$ exactly, and

$$A = \frac{F_0}{b\,\omega_0} = \frac{m\omega_0}{b}\cdot\frac{F_0}{m\omega_0^2} = Q\,\frac{F_0}{k},$$

using $Q = m\omega_0/b$ from [[Damped Oscillations]] and $k = m\omega_0^2$. *At very low frequency,* $\omega \to 0$: $A \to F_0/k$ and $\phi \to 0$ — the mass sits where a steady force $F_0$ would hold it. *At very high frequency,* the $m\omega^2$ term swamps everything: $A \to F_0/(m\omega^2) \to 0$ and $\tan\phi \to 0$ from the negative side, so $\phi \to 180°$.

The script `resonance-sim.py` refuses to take the algebra's word for it: it integrates the differential equation by brute force (fourth-order Runge–Kutta), waits for the transient to die, measures the amplitude and phase from the motion itself, and prints them beside the formula at nine frequencies. They agree to three or four figures; at $\omega = \omega_0$ the measured lag is $90.0°$.

Three readings of the formula, one per regime:

| Regime | $\omega$ | Amplitude | Phase lag | Who is in charge |
|---|---|---|---|---|
| Below resonance | $\omega \ll \omega_0$ | $A \to F_0/k$, the **static deflection** | $\phi \to 0$ | the spring: the mass just follows the force |
| At resonance | $\omega = \omega_0$ | $A = \dfrac{F_0}{2m\gamma\omega_0} = \dfrac{F_0}{b\,\omega_0} = Q\,\dfrac{F_0}{k}$ | $\phi = 90°$ exactly | the damping: only the drag limits it |
| Above resonance | $\omega \gg \omega_0$ | $A \to F_0/(m\omega^2) \to 0$ | $\phi \to 180°$ | the mass: too much inertia to follow |

The middle row is the headline: **the resonant amplitude is $Q$ times the static deflection.** A guitar string with $Q \sim 10^3$ driven at its own pitch by a force that would stretch it a hair's breadth statically moves a thousand hair's breadths. The formula also says something the exam's sentence hides: at resonance the spring and the inertia have cancelled each other exactly ($m\omega_0^2 = k$), leaving the driver to fight *only the drag* — which is precisely why the peak height is set by $b$ alone, and why a system with no damping would have no limit.

> [!info] The same equation in copper
> Recall that the series RLC circuit obeys $L\,\frac{d^2q}{dt^2} + R\,\frac{dq}{dt} + \frac{q}{C} = V_0\cos\omega t$: inductance for mass, resistance for drag, $1/C$ for the spring constant. Everything above transfers word for word — $\omega_0 = 1/\sqrt{LC}$, $Q = \omega_0L/R$, current in phase with voltage at resonance, a peak $Q$ times the low-frequency response. The [[Alternating Current]] card draws that curve and checks it the same brute-force way; a radio tuning to one station is this card with the mass swapped for a coil.

---

## Part III — The resonance curve: height, width, and the damping dial

![[resonance-curves.svg|1000]]

*Amplitude (top) and phase lag (bottom) against driving frequency for three amounts of damping, in units of the static deflection, from `resonance-curves.py`. The three dots mark each curve's actual maximum.*

Everything the exam can ask about this graph is visible in it:

- **The curve does not start at zero.** At $f = 0$ the driver is a steady force and the mass sits displaced by $F_0/k$. A sketch that starts at the origin loses a mark; the scheme's phrase is *amplitude never zero when $f > 0$*.
- **A single peak, at (very nearly) the natural frequency,** of height $\approx Q$ static deflections.
- **More damping: lower, broader, and shifted slightly to lower frequency.** Lower because the peak is $Q \times F_0/k$ and $Q$ falls; broader because the width between the two points where the amplitude has dropped to $1/\sqrt2$ of the peak is

$$\Delta\omega \approx 2\gamma = \frac{\omega_0}{Q},$$

the same $2\gamma$ that is the linewidth in [[Damped Oscillations]] §"The atom's ring" — a system that rings for long is a system that responds sharply, two faces of one number. And shifted, because the true maximum of $A(\omega)$ sits at $\omega_0\sqrt{1 - 1/2Q^2}$: below $\omega_0$ by a fraction $1/4Q^2$, invisible for a tuning fork, a few per cent for a car suspension, and for $Q < 1/\sqrt2$ there is no peak at all, only a monotonic fall from the static deflection.

- **The phase curve is the same for every $Q$ at one point:** $90°$ at $\omega_0$. Damping decides how steeply the lag swings from $0$ to $180°$ — a high-$Q$ system flips within a hair of $\omega_0$, a heavily damped one drifts across the whole range — but the crossing itself is pinned.

The exam's "resonance occurs at the natural frequency" is exact for the *power* absorbed and for the *velocity* amplitude, whose curves peak at $\omega_0$ precisely; the displacement peak leans a little low. No Cambridge or IB question has ever priced the difference, and a sketch with the peak at $f_0$ is what the schemes want.

---

## Part IV — Growing and dying: the transient

Switch the driver on at the natural frequency, from rest. The amplitude does not appear at once; it **grows**, and the growth has the shape of the damped card's envelope turned upside down:

$$x(t) \approx Q\frac{F_0}{k}\left(1 - e^{-\gamma t}\right)\sin\omega_0 t, \qquad \text{63 \% of the way in } \frac{1}{\gamma} = \frac{2Q}{\omega_0} \approx \frac{Q}{\pi}\ \text{cycles}.$$

![[resonance-buildup.svg|1000]]

*Two systems switched on at their own frequency. The lightly damped one climbs higher and takes longer to get there — the same $\gamma$ sets both the final height ($Q = \omega_0/2\gamma$) and the climb time ($1/\gamma$). `resonance-sim.py` counts the cycles by brute force: about $Q/\pi$ to reach 63 %, about $3Q/\pi$ to reach 95 %.*

Why the growth stops is the energy balance of Part I made quantitative. At the steady state, with the force in step with the velocity, the driver supplies $\tfrac12F_0v_0$ per unit time on average and the drag removes $\tfrac12 b\,v_0^2$, so

$$v_0 = \frac{F_0}{b}, \qquad A = \frac{v_0}{\omega_0} = \frac{F_0}{b\,\omega_0},$$

the same resonant amplitude as Part II, obtained without solving anything. This is the reasoning the June 2021 question wants when it asks *why the amplitude stays constant although the oscillator keeps supplying energy*: because the energy supplied each cycle is exactly the energy dissipated each cycle. Switch the driver off and the same $e^{-\gamma t}$ brings it back down — the IB's favourite graph shows both halves on one axis.

A consequence worth knowing: **a resonance takes about $Q$ cycles to notice you.** Drive a $Q = 10^4$ tuning fork for ten cycles and almost nothing happens; sweep a frequency past a sharp resonance too fast and the peak is smaller and later than the curve promises. Wine glasses need a *sustained* note.

---

## Part V — Resonance in the wild: wanted and unwanted

Resonance is the *cheapest* way to make something move a lot — a small periodic push, patiently timed — and the world uses that in both directions.

| Where | Driver | Natural oscillator | Wanted? |
|---|---|---|---|
| Radio tuning | the station's carrier | the RLC circuit, $\omega_0 = 1/\sqrt{LC}$ | yes — $Q$ picks one station |
| Quartz watch | a feedback circuit | a 32 768 Hz tuning-fork crystal, $Q \sim 10^5$ | yes — the resonance *is* the clock |
| Caesium clock | a microwave field | the atom's 9 192 631 770 Hz transition, $Q \sim 10^{10}$ | yes — the SI second |
| MRI scanner | radio pulses | protons precessing at 42.6 MHz per tesla | yes — see Beyond Syllabus |
| Ultrasound probe | an alternating p.d. | a piezoelectric crystal at its natural frequency | yes — 9702 Paper 4, June 2025 |
| A child's swing | the parent | the pendulum | yes |
| A violin | the bowed string | the body's air and wood resonances | yes — the resonances *are* the tone |
| A washing machine spinning up | the unbalanced drum | the machine on its feet | no — it shudders *as it passes through* |
| Millennium Bridge, London, 2000 | 2 000 people stepping in sympathy at ≈ 1 Hz | the deck's lateral mode | no — closed after two days; 91 dampers fitted |
| Mexico City, 1985 | earthquake waves filtered by the lake-bed clay to a ≈ 2 s period | buildings of 6–15 storeys, period ≈ 2 s | no — those heights fell; taller and shorter stood |
| Broughton bridge, 1831 | 74 soldiers marching in step | the suspension deck | no — hence the order to *break step* |

Two engineering morals hide in the table. First, **isolation**: the far right of the resonance curve, where the mass stands still while the driver shakes, is a *feature*. A camera gimbal, a car's suspension over a washboard road, and the rubber feet under a washing machine are all tuned so that the natural frequency sits *well below* the frequencies they will be shaken at — the Beyond Syllabus section shows the isolation begins at $\sqrt2 f_0$. Second, **passing through**: any machine that spins up from rest must cross its resonance on the way; the design question is not whether but *how fast*, and the shudder in the washing machine is the engineer's answer that a few seconds is fine.

---

## Worked examples — every tool named

### Example 1 — the standard Paper 4 shape (Cambridge 9702, June 2024 Paper 41, Q4)

> *A small ball is held by a stretched string between a wall and a vibration generator. With the generator off, a student displaces the ball vertically and releases it; the displacement–time graph shows oscillations of period 0.25 s whose amplitude decreases. (a) State what is meant by resonance. [2] (b)(i) Name the phenomenon illustrated by the decreasing amplitude. [1] (ii) Explain it. [2] (iii) Determine the frequency of the oscillations. [1] (c) The generator is switched on and its frequency is increased from 0 to 10 Hz. Sketch the variation with frequency of the amplitude of the ball's oscillations. [2]*

**(a) Tool: the two-clause definition.** *Oscillation at maximum amplitude* [B1], *when the driving frequency equals the natural frequency of the system* [B1]. Both clauses; a "large amplitude" without *maximum*, or "the frequencies are the same" without saying which two, loses the mark.

**(b)(i) Tool: the three damping words.** Several cycles inside a shrinking envelope: **light damping** [B1]. **(ii) Tool: the energy sentence.** The oscillations lose energy [B1] because of resistive forces acting on the ball [B1] — name the force *and* say where the energy goes. **(iii) Tool: $f = 1/T$.** Trigger: a period read off the graph. $f = 1/0.25 = 4.0\ \text{Hz}$ [A1].

**(c) Tool: the resonance curve, with (b)(iii) as its peak.** Trigger: the natural frequency was measured in (b), so the peak goes at $4.0$ Hz. A curve that starts above zero at $f = 0$, rises to a single maximum, and falls away toward 10 Hz [B1]; the single maximum at 4.0 Hz [B1]. The scheme is explicit that *one* peak is wanted — a second bump anywhere is a lost mark.

### Example 2 — the platform, the ellipse, and the peak (Cambridge 9702, June 2026 Paper 44, Q5)

> *A metal ball hangs from a spring below a platform. (a) The ball is displaced and released; the velocity–displacement graph is an ellipse reaching $x_0 = 2.5$ cm and $v_0 = 4.4$ cm s$^{-1}$. (ii) Show that the frequency of the oscillations is 0.28 Hz. [2] (b) The platform is now moved up and down by a motor with simple harmonic motion of constant amplitude but variable frequency. (i) State what is meant by resonance. [2] (ii) The platform's frequency increases slowly from 0 to 0.40 Hz. Sketch the variation with $f$ of the amplitude of the ball. [2]*

**(a)(ii) Tool: $v_0 = \omega x_0$, from [[Simple Harmonic Motion]].** Trigger: an ellipse in the $v$–$x$ plane is SHM's signature, and its two semi-axes are $x_0$ and $\omega x_0$. $\omega = v_0/x_0 = 4.4/2.5 = 1.76\ \text{rad s}^{-1}$; $f = \omega/2\pi = 0.28$ Hz [C1 A1]. The scheme insists on the *full* substitution — a "show that" is marked on the working.

**(b)(i)** As Example 1(a); the 2026 scheme adds its tolerances — *vibration* for oscillation, *platform* or *motor* or *external* for driving, *matches* for equals — and refuses "nature frequency" only with a benefit-of-the-doubt note. **(ii) Tool: the curve, peak at the frequency found in (a).** A line from $f = 0$ that is never zero for $f > 0$, rising continuously to a single peak and falling continuously to 0.40 Hz [B1]; the peak at $0.28$ Hz [B1], within one small square. Notice the design of the question: the *same* system is measured free in (a) and driven in (b), which is the whole logic of the topic — the natural frequency you find by letting it ring is the frequency at which it will resonate.

### Example 3 — Barton's pendulums and the quarter cycle (Cambridge 9702, June 2022 Paper 42, Q4)

> *A heavy pendulum and a light pendulum of the same natural frequency hang from one string. The heavy one is set swinging and drives the light one; the graph shows both displacements. The light pendulum's displacement is $x = 0.25\sin 5.0\pi t$ (cm, s). (b)(i) Calculate the period. [2] (iii) Determine the magnitude of the phase difference between the two oscillations. Give a unit. [2]*

**(i) Tool: $T = 2\pi/\omega$.** $T = 2\pi/5.0\pi = 0.40$ s [C1 A1]. **(iii) Tool: phase from a time offset, $\phi = 2\pi\,\Delta t/T$.** Trigger: the two traces are the same shape displaced along $t$; the graph shows the light pendulum's peaks $0.10$ s after the heavy one's. $\phi = 2\pi \times 0.10/0.40 = 1.6\ \text{rad}$ (the scheme also accepts $4.7$ rad, the same offset read the other way) [C1 A1].

Now look at the number. $1.6$ rad is $\pi/2$ — **a quarter cycle** — and the question told you the two pendulums have *the same natural frequency*. The driven pendulum is at resonance, and Part I says the displacement of a resonating system lags its driver by exactly $90°$. The examiners built the apparatus to the theory. This is the classic **Barton's pendulums** demonstration, and it is the first Hands-on item below.

### Example 4 — energy in, energy out (Cambridge 9702, June 2021 Paper 41, Q3(c))

> *A trolley between two springs ($k = 130$ N m$^{-1}$ each, $m = 0.84$ kg) is driven by an oscillator whose frequency is varied at constant amplitude. (b) Calculate the trolley's natural frequency. (c)(i) Name the phenomenon when the trolley's amplitude is a maximum. [1] (ii) The oscillator continually supplies energy, yet the amplitude of the trolley at this frequency stays constant. Explain. [2]*

**(b) Tool: $a = -\omega^2x$ and $\omega = 2\pi f$.** Trigger: the question gives $a = -(2k/m)x$, so $\omega^2 = 2k/m$. $(2\pi f)^2 = 260/0.84$, $f = 2.8$ Hz [C1 C1 A1]. **(c)(i)** Resonance [B1]. **(ii) Tool: the Part IV balance.** The oscillator supplies energy continuously [B1]; the trolley's energy is constant, so energy must be dissipated (by resistive forces) at the same rate — or: without loss the amplitude would increase without limit [B1]. The second sentence is Part II's "only the drag limits it" turned into a mark.

### Example 5 — the best question from another board: the farmer's seat (IB Physics HL, November 2017 Paper 3, Q12)

> *A farmer drives across a field with undulations every 3.0 m. The seat on its spring, with the farmer, has a natural frequency of 1.9 Hz. (a) Explain why driving at 5.6 m s$^{-1}$ would be uncomfortable. [3] (b) Outline what change to the $Q$ of the seat–spring system would make the drive more comfortable. [1]*

**(a) Tool: a periodic driver from speed and spacing, $f = v/\lambda$.** Trigger: bumps every 3.0 m at a steady speed are a periodic force. $f = 5.6/3.0 = 1.87$ Hz [M1 A1] — equal to the seat's natural frequency, so **resonance** occurs and the amplitude of the seat's vibration becomes large [B1; the scheme requires the word]. **(b)** Reduce $Q$ — that is, *increase the damping* [B1]. This is the washboard-road version of Part V's suspension and the reason a tractor seat has a damper: the driver cannot avoid every speed that resonates, so the peak is made low and broad instead.

### Example 6 — $Q$ read three ways (IB Physics HL, May 2016 Paper 3, Q11)

> *A pendulum has $Q = 200$ and period about 0.4 s. (a) It is displaced and released; discuss, with reference to $Q$, the subsequent motion. [2] (b) The support is now oscillated horizontally at frequency $f$. Describe the amplitude and the phase of the bob relative to the support when (i) $f = 2.5$ Hz, (ii) $f = 1$ Hz. [2]*

**(a) Tool: the two readings of $Q$ from [[Damped Oscillations]].** High $Q$ means light damping; the amplitude decays exponentially, the pendulum swings of the order of $200$ times before it is still, losing about $2\pi/Q \approx 3\,\%$ of its energy per cycle [any two, 2 max]. **(b) Tool: the three-regime table.** $f_0 = 1/0.4 = 2.5$ Hz, so (i) is resonance: large amplitude, the bob a quarter cycle behind the support [B1]. (ii) $1$ Hz is well below $f_0$: small amplitude, the bob *almost in phase* with the support [B1]. The 2025 IB syllabus has dropped the quantitative $Q$, but this question is the cleanest test of Parts II and III that any board has set, which is why it is here.

---

## Hands-on

1. **Barton's pendulums, from a coat hanger.** Tie five or six threads of *different* lengths to a horizontal string or a broom handle, each with a washer or a nut, and one *heavy* pendulum (a bunch of keys) whose length matches exactly one of the light ones. Set the heavy one swinging perpendicular to the string. The matching light pendulum grows to a large swing; the others jitter. Watch the matching one's phase: it peaks a quarter cycle *after* the driver — Example 3, on your desk.
2. **Run `resonance-sim.py`** and change `Q`. Watch the peak height track $Q$, the width track $1/Q$, and the lag at resonance stay pinned at $90.0°$ whatever you do. Then change the frequency ratio to $0.99$ and $1.01$ and see how sharp a $Q = 100$ system is.
3. **Find a natural frequency with your voice.** Blow across a bottle: the note you get is its air's natural frequency. Now sing that note *at* the bottle from a hand's breadth away and listen for it answering; sing a semitone off and it does not. A wine glass rung with a wet finger gives its note the same way, and it is only sustained singing at that pitch, loud, that breaks one — Part IV's "resonance takes $Q$ cycles to notice you".
4. **Listen to a washing machine.** During spin-up there is one speed at which the whole machine shudders, and it is the same speed every time, well below the top speed. That is the natural frequency of the machine on its feet, and the shudder ends because the drum keeps accelerating *past* it. Count roughly how many seconds it lasts; a stiffer floor shortens it.

---

## Common Misconceptions (Teaching Notes)

### 1. "A driven system oscillates at its natural frequency"

It oscillates at the **driver's** frequency, always, once the transient has gone. The natural frequency is not what it *does*; it is what it *prefers* — the driving frequency at which its response is largest. Resonance is the special case where the two coincide, which is why the definition names both.

### 2. "At resonance the amplitude becomes infinite" / "keeps growing"

Only with zero damping, which no real system has. Damping caps the amplitude at $Q$ times the static deflection, and the cap is reached after about $Q/\pi$ cycles through the balance of Part IV: energy in per cycle equals energy out. The infinite amplitude is the *undamped* particular integral of [[Second-Order Differential Equations]] §Example 3 — the $x\cos 2x$ that grows without bound — and the exam's oscillator always has drag.

### 3. "At resonance the driven object moves in step with the driver"

It is a **quarter cycle behind**. In-step motion is the *low-frequency* regime, where the mass simply follows the force. At resonance the force is in step with the *velocity*, which is what makes every push count — Part I. Example 3's $1.6$ rad is the exam confirming it.

### 4. "More damping shifts the peak to a higher frequency"

Lower — by a fraction $1/4Q^2$, so slightly. The main effects of more damping are a *lower* and *broader* peak; the shift is the third, smallest effect, and the direction is down. (The phase crossing at $90°$ does not move at all.)

### 5. "Resonance means something breaks"

Most resonances are wanted: every radio, clock, MRI scanner and musical instrument on Part V's list is a resonance used on purpose, and the destructive cases are the minority. The syllabus asks for examples of *both*.

### 6. "Tacoma Narrows was resonance" — and "microwave ovens are tuned to water's resonance"

Neither. The 1940 bridge collapse was **aeroelastic flutter**, a feedback between the deck's twist and the airflow, not a periodic driver matching a natural frequency — [[Stories/The Pendulum Story]] carries the correction and the source. And a microwave oven's 2.45 GHz is far *below* water's molecular resonance (tens of GHz); the frequency was chosen so that the waves penetrate a few centimetres rather than cooking the surface. The Millennium Bridge, the Broughton bridge and Mexico City are the honest destructive examples.

---

## Exam Notes

### Cambridge 9702 (§17.3 — the resonance half; Paper 4)

- **The learning objective, verbatim:** *understand that resonance involves a maximum amplitude of oscillations and that this occurs when an oscillating system is forced to oscillate at its natural frequency.* The two damping LOs of the same section are [[Damped Oscillations]]'.
- **The definition question (2 marks in the cited examples):** *oscillation at maximum amplitude* + *when driving frequency = natural frequency* — June 2022, June 2024 (both variants), June 2026, with the same two-part structure in the cited schemes. The 2026 guidance column tolerates *vibration*, *platform / motor / external / forced* for driving, and *matches* for equals; it does not tolerate a missing "maximum".
- **The sketch (2 marks):** a curve that is non-zero at $f = 0$, rises continuously to a **single** peak and falls continuously [B1]; the peak at the natural frequency found earlier in the question [B1] — which is found earlier in these examples, from a period on a graph (June 2024) or from $v_0 = \omega x_0$ (June 2026). Read the tolerance: one small square horizontally.
- **The energy explanation (2 marks, June 2021):** the driver supplies energy continuously; the amplitude is constant, so energy is dissipated at the same rate (or: without dissipation the amplitude would grow without limit).
- **The effect of damping on the curve** is not named in the current LO but was examined for years on the previous syllabus and remains fair game as an *explain* or *sketch a second curve*: lower peak, broader peak, peak at a slightly lower frequency. Give all three.
- **Current application outside §17:** the piezoelectric [[Ultrasound]] transducer in §24.1. June 2025 Paper 44 Q10(a) credits alternating p.d., driving at the crystal's natural frequency, and an ultrasonic natural frequency. **Legacy extension:** March 2021 Paper 42 Q8(b) examines MRI resonance; MRI is absent from the current §24 ultrasound/X-ray/CT/PET syllabus. Do not treat that old question as current medical-topic coverage.
- **Formula sheet:** nothing. The sheet carries $x = x_0\sin\omega t$ and $v = \pm\omega\sqrt{x_0^2 - x^2}$ for SHM and no damping or resonance formulas; everything in Parts II–IV is the *why*, not required working.

### IB Physics (C.4.3 — the resonance half; Papers 1 and 2)

- The guide asks for *the nature of resonance including natural frequency and amplitude of oscillation based on driving frequency*, and for **useful and destructive examples** — have two of each ready from Part V. The damping vocabulary of the same row is [[Damped Oscillations]]'.
- Favourite graph: displacement against time with the driver switched on at $t = 0$ and off at $t_B$ — amplitude *increasing as energy is added*, then steady because *energy input equals energy lost to damping*, then the damped decay (November 2016 Paper 3 Q14, whose scheme is those exact phrases).
- The **2016–2023 HL Option B** papers examined $Q$ quantitatively (Examples 5 and 6). $Q$ is not on the 2025 syllabus, but those questions are the best practice for this card that any board has printed.

### AP Physics C: Mechanics — §7.3.A.4

The current CED explicitly requires resonance under a sinusoidal external force: the drive acts at the natural frequency, the amplitude increases, and the natural frequency is the frequency of free oscillation after displacement. This is qualitative resonance within §7.3; the full forced-response derivation and quantitative bandwidth/$Q$ machinery go beyond that stated requirement.

### Where it is *not* examined

- **0625 IGCSE:** no oscillations topic; resonance does not appear.
- **AP Physics 1, AP Physics 2 and AP Physics C: Electricity and Magnetism:** these current CEDs do not name mechanical forced-oscillator resonance as a required topic. AP-2 standing-wave modes use related ideas; AP-C Mechanics explicitly requires resonance as stated above.
- **9709 / 9231:** no forced oscillations in the mechanics papers; the *driven* second-order equation appears only as a modelling context in 9231 FP2 §2.6 — [[Second-Order Differential Equations]] territory, where "the trial form already lives in the complementary function" is the maths name for resonance.

---

## Connections

- **Imaging application:** [[Ultrasound]] — pulse timing, impedance matching and attenuation turn sound into an internal image.

- **Parent:** [[Simple Harmonic Motion]] — supplies $\omega_0$, $v_0 = \omega x_0$ (Example 2), and the fact that velocity leads displacement by a quarter cycle, on which Part I rests. Its §"Driven oscillations and resonance" is a preview; this card is the treatment.
- **Parent:** [[Damped Oscillations]] — the transient of Part IV *is* that card's ring; $\gamma$ and $Q$ are defined there and reused here as peak height, peak width and build-up time. Its §"The atom's ring" linewidth $2\gamma$ is this card's resonance width.
- **Mathematical engine:** [[Second-Order Differential Equations]] — the particular integral of the forced equation; §Example 3 is the undamped resonance with its unbounded $x\cos 2x$, and the "multiply the trial by $x$" rule is resonance seen from the algebra.
- **The same equation in copper:** [[Alternating Current]] — the series RLC resonance curve, $\omega_0 = 1/\sqrt{LC}$, $Q = \omega_0L/R$, and the complex-impedance method Part II borrows.
- **Children:** [[Coupled Oscillators]] — two resonators that share energy have *two* natural frequencies, and the resonance peak splits; [[Suspension]] — the quarter-car of the damped card driven by a road, i.e. Part V's isolation argument grown to a full engineering story; [[Standing Waves]] — a string or a pipe has many natural frequencies, and each is a resonance.
- **Story:** [[Stories/The Pendulum Story]] — the escapement is a driven oscillator kept at resonance by the smallest possible push, and Tacoma Narrows is the destructive example that was *not* resonance.

---

## Beyond Syllabus

### Power absorbed, and why a spectral line is a resonance curve

Recall that the driver's mean power is $\tfrac12F_0A\omega\sin\phi$. Substitute Part II's $A$ and $\phi$ and the result is

$$\langle P\rangle(\omega) = \frac{F_0^2}{2m}\,\frac{2\gamma\omega^2}{(\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2} \;\approx\; \frac{F_0^2}{8m}\,\frac{1}{(\omega-\omega_0)^2 + \gamma^2}\quad(\text{near } \omega_0),$$

a **Lorentzian** centred exactly on $\omega_0$ with full width $2\gamma$ at half height. An atom driven by light is this oscillator; the *absorption line* is its power curve; the width of the line measures $\gamma$, hence the lifetime of the excited state. Every spectrometer that reads a line's width is reading the damping of a resonance, and a laser locked to an atomic line is a driver sitting on top of a peak with $Q \sim 10^7$ or more.

### Base excitation and isolation: the platform, done properly

The June 2026 platform does not push the ball with a force; it moves the *spring's end*, $u(t) = a\cos\omega t$, and the drag acts on the relative motion. The steady amplitude of the ball is then

$$\frac{A}{a} = \sqrt{\frac{1 + (2\zeta r)^2}{(1-r^2)^2 + (2\zeta r)^2}}, \qquad r = \frac{\omega}{\omega_0},\ \zeta = \frac{1}{2Q},$$

the **transmissibility**, and the Manim clip integrates exactly this. It has one property the force-driven curve lacks: every curve, whatever the damping, passes through $A/a = 1$ at $r = \sqrt2$, and *above* $\sqrt2 f_0$ the ball moves *less* than the platform. That is the whole theory of **vibration isolation**: mount the instrument, the engine or the building on springs soft enough that $f_0$ is well below the shaking frequency, and the shaking does not get through. Adding damping *helps* at resonance and *hurts* above $\sqrt2 f_0$ — the engineer's dilemma that [[Suspension]] takes up.

### Parametric resonance: the swing you pump yourself

Stand on a swing and pump — crouch at the ends, stand at the bottom — and it goes higher with no one pushing. There is no external periodic *force*; you are periodically changing a *parameter*, the pendulum's length, and the trick works only at **twice** the natural frequency (once per half swing). This is parametric resonance, governed by the Mathieu equation rather than the driven one, and it is how the Botafumeiro, the 50-kilogram censer of Santiago de Compostela, has been pumped to $80°$ swings by eight men on a rope since the middle ages.

### When the peak bends: the nonlinear oscillator

Real springs stiffen or soften at large amplitude, so $\omega_0$ itself depends on $A$. The resonance curve then *leans* — to the right for a hardening spring — and for strong enough driving it folds over, so that sweeping the frequency up and sweeping it down give *different* amplitudes, with a sudden jump between them. This Duffing behaviour is why a resonance measured on a real guitar string or a MEMS sensor depends on which way you swept, and it is the first step from this card into nonlinear dynamics.

### MRI: resonance you have probably lain inside

A proton in a magnetic field $B$ precesses at the Larmor frequency $f = 42.58\ \text{MHz T}^{-1}\times B$ — about $64$ MHz in a $1.5$ T scanner. A radio pulse at *exactly* that frequency is a driver at resonance: the protons absorb it and tip; when the pulse stops they relax and re-emit at the same frequency, and that echo is the signal. A *gradient* field makes $B$, hence the resonant frequency, vary across the body, so that only one slice resonates with a given pulse — which is how the scanner knows where the signal came from. The legacy Cambridge medical-physics question (March 2021 Paper 42) and the former IB imaging option (November 2016 Paper 3 Q20) examined it in exactly those words: *frequency equals natural frequency, resonance occurs, energy is absorbed*. These are historical exam contexts, not MRI requirements in the current Cambridge or IB guides.

---

## LaTeX Reference

| Quantity | LaTeX | Rendered |
|---|---|---|
| Driven equation | `m\ddot{x} + b\dot{x} + kx = F_0\cos\omega t` | $m\ddot{x} + b\dot{x} + kx = F_0\cos\omega t$ |
| Steady amplitude | `A = \dfrac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2}}` | $A = \dfrac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2}}$ |
| Phase lag | `\tan\phi = \dfrac{2\gamma\omega}{\omega_0^2-\omega^2}` | $\tan\phi = \dfrac{2\gamma\omega}{\omega_0^2-\omega^2}$ |
| Resonant amplitude | `A_{\max} = Q\,\dfrac{F_0}{k} = \dfrac{F_0}{b\,\omega_0}` | $A_{\max} = Q\,\dfrac{F_0}{k} = \dfrac{F_0}{b\,\omega_0}$ |
| Peak width | `\Delta\omega \approx 2\gamma = \omega_0/Q` | $\Delta\omega \approx 2\gamma = \omega_0/Q$ |
| Peak position | `\omega_{\text{peak}} = \omega_0\sqrt{1 - 1/2Q^2}` | $\omega_{\text{peak}} = \omega_0\sqrt{1 - 1/2Q^2}$ |
| Build-up | `x \approx Q\dfrac{F_0}{k}(1 - e^{-\gamma t})\sin\omega_0 t` | $x \approx Q\dfrac{F_0}{k}(1 - e^{-\gamma t})\sin\omega_0 t$ |
| Transmissibility | `\dfrac{A}{a} = \sqrt{\dfrac{1+(2\zeta r)^2}{(1-r^2)^2+(2\zeta r)^2}}` | $\dfrac{A}{a} = \sqrt{\dfrac{1+(2\zeta r)^2}{(1-r^2)^2+(2\zeta r)^2}}$ |

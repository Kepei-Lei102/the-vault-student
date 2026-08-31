---
chinese: 运动学（微积分）(yùndòngxué)
prerequisites:
  - "[[Differentiation]]"
  - "[[Integration]]"
  - "[[Travel Graphs (Vocab)]]"
  - "[[Stationary Points]]"
  - "[[Area Under a Graph (Vocab)]]"
  - "[[Average Speed (Vocab)]]"
leads_to:
  - "[[Differential Equations]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Choosing Effective Equations]]"
  - "[[Linear Momentum]]"
  - "[[SUVAT]]"
teach_together:
  - "[[Parametric Differentiation]]"
tags:
  - subject/mathematics
  - subject/physics
  - domain/calculus
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-14-14
  - syllabus/0606-14-15
  - syllabus/0625-1-2
  - syllabus/9702-2-1
  - syllabus/9709-4-2
  - type/deep
  - type/application
  - notation/displacement-s
  - notation/velocity-v
  - notation/acceleration-a
  - misconception/distance-vs-displacement
  - misconception/velocity-vs-speed
  - misconception/at-rest-vs-stationary-graph
---

# Kinematics (Calculus) 运动学（微积分）

## Definition

**Kinematics** is the calculus of motion in one dimension. A particle moves along a line, and its position at time $t$ is recorded as a function $s(t)$. Calculus then gives the entire story of the motion through three connected functions:

$$
\boxed{\;s(t) \;\xrightarrow{\;\frac{d}{dt}\;}\; v(t) \;\xrightarrow{\;\frac{d}{dt}\;}\; a(t)\;}
$$

- **$s(t)$ — displacement** (位移): position relative to the origin. Signed (positive on one side, negative on the other).
- **$v(t)$ — velocity** (速度): the *rate of change of displacement*. $v(t) = \dfrac{ds}{dt}$.
- **$a(t)$ — acceleration** (加速度): the *rate of change of velocity*. $a(t) = \dfrac{dv}{dt} = \dfrac{d^2 s}{dt^2}$.

Going *backward* — from $a$ to $v$ to $s$ — is integration, with **initial conditions** to pin down the constants:

$$
v(t) = \int a(t)\, dt + C_1, \qquad s(t) = \int v(t)\, dt + C_2.
$$

This card formalises the "gradient = velocity, area = distance" intuition from [[Travel Graphs (Vocab)]] into the calculus of motion. Every gradient becomes a derivative; every area becomes an integral.

### 中文锚点

**运动学 (yùndòngxué)** = 用微积分研究运动。一个质点在直线上运动，位置 $s(t)$ 是时间的函数。

三个核心函数链 (求导链)：

$$s(t) \xrightarrow{\;求导\;} v(t) \xrightarrow{\;求导\;} a(t)$$

- $s(t)$ = **位移** (wèiyí)，有正负之分
- $v(t) = \dfrac{ds}{dt}$ = **速度** (sùdù)，**有方向**（正负）
- $a(t) = \dfrac{dv}{dt}$ = **加速度** (jiāsùdù)

反过来，从 $a$ 到 $s$ 是**积分**，需要**初始条件** (chūshǐ tiáojiàn) 来确定积分常数。

考试关键判断：
- "**At rest**" / **静止** → $v = 0$
- "**Maximum / minimum velocity**" → $a = 0$ (因为 $v$ 取极值时 $\dfrac{dv}{dt} = a = 0$)
- "**Returning toward origin**" → $v < 0$ (位移减少)
- "**Decelerating**" → $v$ 与 $a$ 异号 (一个正一个负)

---

## The Calculus Story

### Forward direction — differentiation gives the next function

If you know the position function, you know everything about the motion. Differentiate once for velocity; differentiate again for acceleration.

**Example.** A particle's position is $s(t) = t^3 - 6t^2 + 9t$ (in metres, $t$ in seconds, on $0 \le t \le 5$).

Velocity: $v(t) = \dfrac{ds}{dt} = 3t^2 - 12t + 9 = 3(t^2 - 4t + 3) = 3(t-1)(t-3)$.

Acceleration: $a(t) = \dfrac{dv}{dt} = 6t - 12$.

The whole motion is decoded:

| Question | Where to look | Answer |
|---|---|---|
| When is the particle at rest? | $v(t) = 0$ | $t = 1$ and $t = 3$ |
| When is velocity maximum/minimum? | $a(t) = 0$ | $t = 2$ |
| When is the particle moving forward? | $v(t) > 0$ | $0 \le t < 1$ or $3 < t \le 5$ |
| When is it moving backward? | $v(t) < 0$ | $1 < t < 3$ |
| When is it accelerating (in the +ve direction)? | $a(t) > 0$ | $t > 2$ |

The bracket-factorising of $v(t)$ is the key — it converts "find the roots" into "read the sign of each factor."

### Backward direction — integration recovers the previous function

If you know the *acceleration* (e.g. from Newton's second law $F = ma$), you can recover velocity and position by integrating — but each integration introduces an unknown constant, fixed only by an **initial condition** (typically $v(0)$ and $s(0)$).

**Example.** A particle has acceleration $a(t) = 6 - 4t$ m/s². At $t = 0$, $v(0) = 5$ m/s and $s(0) = 0$ m. Find $v(t)$ and $s(t)$.

$$v(t) = \int (6 - 4t)\, dt + C_1 = 6t - 2t^2 + C_1.$$

Use $v(0) = 5$: $C_1 = 5$. So $v(t) = 6t - 2t^2 + 5$.

$$s(t) = \int (6t - 2t^2 + 5)\, dt + C_2 = 3t^2 - \tfrac{2}{3}t^3 + 5t + C_2.$$

Use $s(0) = 0$: $C_2 = 0$. So $s(t) = 3t^2 - \tfrac{2}{3}t^3 + 5t$.

> [!info] Why integration *requires* an initial condition
> Integration is the reverse of differentiation, but differentiation *throws away* constants — $\dfrac{d}{dt}(t^2 + 5) = \dfrac{d}{dt}(t^2 + 99) = 2t$, both equally valid antiderivatives of $2t$. The integral $\int 2t\, dt = t^2 + C$ records this with the "+ C" — and to pin down $C$ for a specific physical situation, you need *one extra fact*: where was the particle at $t = 0$? How fast was it going? That's what an initial condition supplies. **Two integrations need two initial conditions.**

---

## The Three Graphs — and How They Stack

![[kinematics-three-graphs.svg]]

Above: the three motion functions for the worked example $s(t) = t^3 - 6t^2 + 9t$, stacked so vertical features align. The dashed verticals show where $v = 0$ (turning points of $s$) and where $a = 0$ (turning points of $v$). Reading the graphs vertically, every turning point on a curve corresponds to a zero on the derivative below it.

| Feature on $s$-$t$ graph | Means | Read from $v$-$t$ |
|---|---|---|
| Turning point (max or min of $s$) | Particle changes direction | $v = 0$ |
| Steeper segment | Faster motion | Larger $\lvert v \rvert$ |
| Going down (negative gradient) | Moving backward | $v < 0$ |

| Feature on $v$-$t$ graph | Means | Read from $a$-$t$ |
|---|---|---|
| Turning point (max or min of $v$) | Maximum/minimum velocity | $a = 0$ |
| Going up (positive gradient) | Accelerating | $a > 0$ |
| Below the axis | Moving in $-$ direction | $v < 0$ |
| Area under curve (signed) | **Displacement** over the interval | $\int v\, dt$ |
| Area under $\lvert v \rvert$ curve | **Distance travelled** over the interval | $\int \lvert v \rvert\, dt$ |

The most important and exam-tested distinction is the last: *displacement* and *distance travelled* are different when the particle reverses direction.

---

## Distance Travelled vs Displacement — the sign-change trap

**Displacement** is a *signed* quantity: it's the position at the end minus the position at the start. If a particle goes 3 m right, then 2 m left, the displacement is $+1$ m, but the *distance travelled* is $5$ m.

In calculus terms:

$$
\text{displacement on } [a, b] = s(b) - s(a) = \int_a^b v(t)\, dt.
$$

$$
\text{distance travelled on } [a, b] = \int_a^b \bigl\lvert v(t) \bigr\rvert\, dt.
$$

The first integral *adds signed velocity*, so a backward leg cancels a forward leg. The second integral *adds the magnitude*, so every leg contributes positively — what your odometer reads.

**To compute distance travelled when $v$ changes sign:**

1. Find the times $t_1, t_2, \ldots$ where $v(t) = 0$.
2. Split the interval at those times.
3. Compute $|s(t_{i+1}) - s(t_i)|$ on each subinterval.
4. Sum the absolute values.

**Worked example — split at the sign change.** From the worked example, $s(t) = t^3 - 6t^2 + 9t$ on $0 \le t \le 4$.

The particle is at rest at $t = 1$ and $t = 3$. Compute positions at these critical times:
- $s(0) = 0$
- $s(1) = 1 - 6 + 9 = 4$
- $s(3) = 27 - 54 + 27 = 0$
- $s(4) = 64 - 96 + 36 = 4$

So the particle goes: $0 \to 4 \to 0 \to 4$.

**Displacement** on $[0, 4]$: $s(4) - s(0) = 4 - 0 = 4$ m.

**Distance travelled** on $[0, 4]$: $|4 - 0| + |0 - 4| + |4 - 0| = 4 + 4 + 4 = 12$ m.

The displacement is what you'd compute from $\int_0^4 v\, dt = s(4) - s(0)$ directly — easy. The distance travelled requires the split. This is the most common 0606 §14.14 mark loss: students integrate $v$ across a sign change and report the result as "distance," missing 4 m of travel.

> [!warning] $\int v\, dt$ across a sign change gives displacement, *not* distance
> Many 0606 candidates write "distance $= \int_0^4 v\, dt = 4$." Wrong — that's *displacement*. To get distance, you must either integrate $|v|$ (split the interval at $v = 0$ and integrate on each piece, taking absolute values), or use the position function and sum $|s(t_{i+1}) - s(t_i)|$ over each interval. The two answers differ whenever the particle reverses direction.

---

## SUVAT — the constant-acceleration case (9709 P4 §4.2 / 9702 §2.1 — see [[SUVAT]] for the dedicated card)

When acceleration is constant ($a(t) = a$), the integration step gives clean polynomial formulas. Starting from $a(t) = a$ and using initial conditions $s(0) = 0$ (often), $v(0) = u$:

$$v(t) = \int a\, dt + u = at + u.$$

$$s(t) = \int (at + u)\, dt = \tfrac{1}{2} a t^2 + u t.$$

These are the famous **SUVAT equations** of A-Level / IGCSE Physics:

| Letter | Meaning | Formula |
|---|---|---|
| $s$ | displacement | $s = ut + \tfrac{1}{2}at^2$ |
| $u$ | initial velocity | (given) |
| $v$ | final velocity | $v = u + at$ |
| $a$ | constant acceleration | (given) |
| $t$ | time | (given) |

A third equation, $v^2 = u^2 + 2as$, comes from eliminating $t$ between the two — it's the "energy" form of the kinematics, not really new content.

> [!info] SUVAT is calculus in disguise
> Physics teaches SUVAT as five formulas to memorise. Calculus reveals them as *one fact* — "constant $a$, integrate twice, apply initial conditions $s(0) = 0$, $v(0) = u$." Once you understand the integration, the formulas are forced. (And once acceleration becomes non-constant — gravity at high altitude, drag forces, oscillating springs — SUVAT *fails* and only the calculus survives.)

---

## Reading $v$-$t$ Graphs — the calculus version of [[Travel Graphs (Vocab)]]

Everything you knew at IGCSE level becomes literal calculus:

| 0580 instinct | Calculus version |
|---|---|
| Gradient of d-t graph = speed | $v(t) = \dfrac{ds}{dt}$ |
| Gradient of s-t graph = acceleration | $a(t) = \dfrac{dv}{dt}$ |
| Area under s-t graph = distance | $\text{distance} = \int \lvert v \rvert\, dt$ |
| Steeper line = faster | $\lvert v \rvert$ larger |
| Horizontal s-t segment (above axis) = constant speed | $v(t) = $ constant means $a(t) = 0$ |

The pre-calculus version *underestimated* the precision available — it could only handle straight-line segments. Calculus handles any curve, and gives exact answers for problems the IGCSE version could only approximate (e.g. with [[Area Under a Graph (Vocab)|trapezium rule]]).

---

## Worked Examples

**Example 1 — direct differentiation.** A particle moves so that $s = t^3 - 9t^2 + 24t$ for $0 \le t \le 6$. Find when the particle is at rest, and the maximum speed in the interval.

$v(t) = 3t^2 - 18t + 24 = 3(t^2 - 6t + 8) = 3(t-2)(t-4)$.

**At rest** when $v = 0$: $t = 2$ and $t = 4$.

**Maximum speed**: $|v|$ achieves its maximum either at endpoints or where $\dfrac{d|v|}{dt} = 0$. Since $|v|$ is continuous and $v$ has a turning point where $a = 0$:
$a(t) = 6t - 18$, so $a = 0$ at $t = 3$. Compute $v(3) = 3(9 - 18 + 8) = -3$ — so $|v(3)| = 3$ m/s.
At endpoints: $|v(0)| = 24$ m/s, $|v(6)| = 3(36 - 36 + 8) = 24$ m/s.
**Maximum speed in the interval = 24 m/s** (at $t = 0$ and $t = 6$).

**Example 2 — integrate twice from acceleration.** A particle starts from the origin with velocity $4$ m/s and has acceleration $a(t) = 2 - 6t$ m/s². Find the position at $t = 2$.

$v(t) = \int (2 - 6t)\, dt + C_1 = 2t - 3t^2 + C_1$. Initial: $v(0) = 4$, so $C_1 = 4$. Hence $v(t) = 4 + 2t - 3t^2$.

$s(t) = \int v\, dt + C_2 = 4t + t^2 - t^3 + C_2$. Initial: $s(0) = 0$, so $C_2 = 0$. Hence $s(t) = 4t + t^2 - t^3$.

$s(2) = 8 + 4 - 8 = \boxed{4}$ m.

**Example 3 — distance vs displacement.** Using the same $s(t) = 4t + t^2 - t^3$, find the *distance* (not displacement) travelled on $0 \le t \le 2$.

$v(t) = 4 + 2t - 3t^2 = -(3t^2 - 2t - 4)$. Solve $v = 0$: $t = \dfrac{2 \pm \sqrt{4 + 48}}{6} = \dfrac{1 \pm \sqrt{13}}{3}$. Only $t = \dfrac{1 + \sqrt{13}}{3} \approx 1.535$ lies in $[0, 2]$.

So the particle reverses at $t \approx 1.535$. Position there: $s(1.535) \approx 4(1.535) + (1.535)^2 - (1.535)^3 \approx 6.14 + 2.36 - 3.62 \approx 4.88$.

Distance = $|s(1.535) - s(0)| + |s(2) - s(1.535)| \approx |4.88 - 0| + |4 - 4.88| \approx 4.88 + 0.88 = \boxed{5.76 \text{ m}}$.

(Compare to displacement $= s(2) - s(0) = 4$ m — a difference of $1.76$ m, the "round trip" component.)

---

## Common Mistakes

1. **Reporting displacement as distance.** $\int_a^b v\, dt$ gives signed displacement. Distance travelled requires splitting at zeros of $v$ and summing absolute changes (or integrating $|v|$).
2. **Forgetting initial conditions.** Each integration introduces a constant. With $a \to v \to s$ (two integrations), you need two initial conditions, typically $v(0)$ and $s(0)$.
3. **Confusing "at rest" with "stationary on graph."** "At rest" means $v = 0$. On a *displacement-time* graph this is a turning point (max or min of $s$), NOT a horizontal segment of the $v$-$t$ graph (that's constant velocity, not zero velocity).
4. **Treating speed and velocity as interchangeable.** Velocity $v$ is signed; speed is $|v|$. "Maximum velocity" and "maximum speed" can give different answers when negative values are large in magnitude. Read the question carefully.
5. **Sign of acceleration vs direction of motion.** $a > 0$ means velocity is *increasing* — but if $v$ is currently negative, increasing it (toward zero) means the particle is *slowing down*, not speeding up. Acceleration and motion are independent until you compare signs: same sign → speeding up; opposite signs → slowing down (decelerating).

---

## Exam Notes

### Cambridge 0606

**Syllabus refs:** §14.14 (differentiate / integrate for $s$, $v$, $a$) and §14.15 (read motion graphs). Standard exam patterns:

- **Pattern A — "find when at rest, find total distance."** Given $s(t)$, differentiate to find $v(t)$; solve $v = 0$ for turning times; split the interval at those times; compute $|s|$-changes piecewise.
- **Pattern B — "find $v(t)$ and $s(t)$ given $a(t)$ and initial conditions."** Integrate twice, applying $v(0)$ then $s(0)$ to fix constants.
- **Pattern C — "max/min velocity."** Solve $a = 0$, evaluate $v$ at the critical time *and* at endpoints, take the largest in magnitude.
- **Pattern D — "deceleration question."** Decelerating means *speed* is decreasing, i.e. $v$ and $a$ have *opposite signs*. Watch out: $a < 0$ alone does not always mean decelerating!

### Cambridge 0580

**Not examined as calculus.** IGCSE Maths reads motion from graphs only — gradients and areas of speed–time graphs ([[Travel Graphs (Vocab)]]); no differentiation of $s(t)$ ever appears. The calculus version starts at 0606.

### Cambridge 9709 (Mechanics, Paper 4)

§4.2 pairs the suvat equations with their calculus escape hatch: **the moment acceleration is not constant, suvat is dead**, and the paper expects $v = \dfrac{ds}{dt}$, $a = \dfrac{dv}{dt}$, integration with initial conditions to go back up the chain. Standard shapes: polynomial or trig $v(t)$ given → find displacement *and* total distance (Pattern A's split-at-$v=0$ discipline, exactly as at 0606, now with harder integrands from P3); two-phase journeys where one phase is suvat and one is calculus. The deceleration trap (Pattern D) is marked the same way.

### Cambridge 9231 (Further Mechanics)

§3.5 — **linear motion under a variable force** — is this card's chain pushed one step further: Newton's second law with $F$ depending on $x$ or $v$ turns $a = \dfrac{dv}{dt}$ into a differential equation, and the syllabus names the substitution that makes position-dependent forces integrable, $a = v\dfrac{dv}{dx}$ (chain rule: $\dfrac{dv}{dt} = \dfrac{dv}{dx}\dfrac{dx}{dt}$). Separable-equation technique from [[Differential Equations]]; the inverse-square case is worked in full in [[Gravitational Fields]] (escape speed via $v\,dv/dx = -gR^2/x^2$); resistive forces $kv$ and $kv^2$ are the other stock integrands.

### IB AA

AA **SL 5.9** names "kinematic problems involving displacement $s$, velocity $v$, acceleration $a$ and total distance travelled" — the same patterns as above, with total distance $\int \lvert v \rvert \, dt$ the flagged distinction. (Simple harmonic motion and phase-plane pictures are physics-side enrichment, not AA syllabus rows.)

### AP Calculus AB/BC

Particle motion appears twice: Topic 4.2 (straight-line motion — interpreting $v$ and $a$ as derivatives) and Topic 8.2 (position from velocity by integration). The integration patterns are identical to the Cambridge ones; AP additionally leans on the *speed* $\lvert v \rvert$ vs velocity distinction and the speeding-up/slowing-down sign test (Pattern D above) as a named FRQ part.

### The physics boards

9702 and 0625 do kinematics with graphs and the equations of motion, not calculus — the derivative notation appears only as shorthand. The calculus formalism on this card belongs to the maths boards; the physics side of the same bridge is [[Newton's Laws of Motion]].

---

## Beyond Syllabus

### Newton² — kinematics is literally Newton's home

> 怎么老是你？

Pause and notice who shows up here. Newton invented calculus (the $\frac{d}{dt}$ machinery on this card). Newton also wrote $F = ma$ (the law that *uses* this card to predict motion). Kinematics is exactly the topic where Newton-the-mathematician hands the baton to Newton-the-physicist — same guy, two hats, same century. **Newton²**. The kinematic chain $s \to v \to a$ is the bridge built between his two halves.

That bridge — turning a force law into a second-order ODE in $s$, then integrating with initial conditions — is the whole project of classical mechanics, from Galileo through Lagrange to Hamilton; [[Newton's Laws of Motion]] carries the physics-side treatment, and [[Differential Equations]] the machinery.

### Higher Derivatives — jerk, snap, crackle, and pop

$a$ is the second derivative of $s$, but the chain doesn't have to stop. The derivatives of acceleration have their own names:

| Order | Symbol | Name | Real-world relevance |
|---|---|---|---|
| 1st | $v$ | velocity | motion |
| 2nd | $a$ | acceleration | force per unit mass |
| 3rd | $j$ | **jerk** 加加速度 | rate of change of acceleration |
| 4th | $s$ (snap) | snap / jounce | rate of change of jerk |
| 5th | crackle | — | barely used |
| 6th | pop | — | basically a meme |

> [!info] Yes, "jerk" is the real technical name. Yes, it's hilarious.
> Imagine being a 19th-century engineer naming the third derivative of position. You needed a one-syllable English word for "the abrupt change in acceleration that makes passengers lurch in their seats." You looked at the dictionary. *Jerk*: "a sharp sudden pull or twist." Perfect — except that word *also* means "a contemptible person." The naming stuck anyway. Physics is now stuck with a quantity whose units are m/s³ and whose name doubles as a mild insult.
>
> Then in the 1980s some textbook author said "if the third derivative is *jerk*, the fourth should be *snap*, the fifth *crackle*, the sixth *pop*" — Rice Krispies cereal mascots. **It's also real.** Engineers cite "jounce" or "snap" interchangeably for the fourth derivative in formal papers. The cereal-mascot ladder is in actual textbooks. Math doesn't always take itself seriously.
>
> 中文也很搞笑：jerk = **加加速度** (jiā-jiā-sùdù) — literally "add-add-acceleration." Same idea: just keep saying 加 until you've added enough derivatives. Snap = 加加加速度. The Chinese is at least *systematic* about being silly.

**Jerk matters in real life.** Roller-coaster engineers and car designers care about jerk because *humans feel it* — an abrupt change in acceleration is what makes a stop "jolt" you. A train with smooth jerk profiles (gradual onset of braking) feels luxurious; the same average deceleration with high jerk feels like an emergency stop. Elevator motion controllers explicitly limit jerk so you don't bonk your head when the car starts and stops. Once you know the word, you start noticing it everywhere — a Tesla's "creep" mode is a jerk-management feature; the way a luxury sedan absorbs a pothole differs from a sports car in the *jerk* it transmits, not the acceleration.

### Phase Space — every motion as a 2D path

Plot $v$ on the vertical axis and $s$ on the horizontal axis. Each point in this *phase plane* represents one *state* of the system (where it is, how fast it's going). Time-evolution traces a *curve* in the phase plane.

For simple harmonic motion ($\ddot s = -\omega^2 s$), the phase-plane trajectory is an **ellipse** — a closed loop, capturing the periodic to-and-fro of a spring or pendulum. For a damped oscillator, the ellipse spirals inward toward the origin (energy is being lost). For a forced driven oscillator, the trajectory can be a *strange attractor* — the entry point to chaos theory.

Phase space is the *real* arena of classical mechanics. The 1D position-time graph hides the velocity; the 1D velocity-time graph hides the position. The 2D phase plot shows them both at once, and the dynamical structure of the system becomes visible.

> [!info] One last connection — calculus is one foot in physics
> The reason kinematics shows up in *every* calculus syllabus on Earth — 0606 to AP BC to first-year university — is that motion is the most concrete setting in which "rate of change" *means something physical*. Slope of a curve = how fast the particle is moving. Area under a curve = how far it travelled. The abstractions ($\frac{d}{dt}$, $\int$) get their initial intuition here. Once you've understood "velocity is the derivative of position," you've understood *everything else calculus does*, just dressed in different clothes.

---

## Connections

- **Prerequisite:** [[Differentiation]] — every step from $s$ to $v$ to $a$ is a derivative
- **Prerequisite:** [[Integration]] — recovering $v$ from $a$, or $s$ from $v$, is integration
- **Prerequisite:** [[Travel Graphs (Vocab)]] — the IGCSE-level graph-reading version of this card; "gradient = speed, area = distance" becomes literal calculus
- **Prerequisite:** [[Stationary Points]] — turning points of $s$ correspond to $v = 0$ (at rest); turning points of $v$ correspond to $a = 0$ (max/min velocity)
- **Sibling:** [[Area Under a Graph (Vocab)]] — pre-calculus area-under-curve method now formalised as $\int v\, dt$
- **Application:** [[Newton's Laws of Motion]] — $F = ma$ converts any force law into a second-order ODE in $s$, and integrating with initial conditions delivers the motion
- **Application:** *engineering* — control systems track jerk as well as acceleration to make rides smooth; vehicle dynamics relies on phase-plane trajectories
- **Beyond high school:** *Lagrangian and Hamiltonian mechanics* — re-cast the entire framework in energy terms; the equations of motion become $\dfrac{d}{dt}\!\left(\dfrac{\partial L}{\partial \dot q}\right) - \dfrac{\partial L}{\partial q} = 0$, completely transforming our view of physics; *chaos theory* lives in phase space when nonlinearities enter
- **Beyond high school:** *special relativity* — replaces $t$ with proper time $\tau$, and $s, v, a$ become 4-vectors; the calculus is identical, only the geometry changes

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $s(t)$ | `s(t)` | Displacement / position |
| $v(t)$ | `v(t)` | Velocity (signed) |
| $a(t)$ | `a(t)` | Acceleration |
| $\dfrac{ds}{dt}$ | `\dfrac{ds}{dt}` | Velocity in Leibniz notation |
| $\dfrac{d^2 s}{dt^2}$ | `\dfrac{d^2 s}{dt^2}` | Acceleration as second derivative |
| $\dot s, \ddot s$ | `\dot s, \ddot s` | Newton dot notation (physics convention) |
| $\int v\, dt$ | `\int v\, dt` | Displacement (signed) over an interval |
| $\int \lvert v \rvert\, dt$ | `\int \lvert v \rvert\, dt` | Distance travelled (always positive) |
| $v^2 = u^2 + 2as$ | SUVAT energy form | Constant acceleration only |

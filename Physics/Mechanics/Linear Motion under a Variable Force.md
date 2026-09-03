---
chinese: 变力作用下的直线运动 (biànlì zuòyòng xià de zhíxiàn yùndòng)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Kinematics Calculus]]"
  - "[[Differential Equations]]"
  - "[[Work, Energy and Power]]"
  - "[[Hyperbolic Functions]]"
leads_to:
  - "[[Gravitational Fields]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - domain/calculus
  - level/A-Level
  - level/AP
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9231-3-5
  - syllabus/AP-Physics-C-Mech-2-9
  - type/deep
  - type/proof
  - notation/v-dv-dx
  - misconception/suvat-under-a-varying-force
  - misconception/terminal-velocity-is-reached
  - misconception/dropping-the-mass
---

# Linear Motion under a Variable Force 变力作用下的直线运动

> *This card is written upside down.* It is, almost entirely, a summary of one skill — **how to use calculus on a question that looks like SUVAT** — and a skill is learned from the questions, not from the summary. So the questions come first: five real Paper 3 questions, solved in full. The method they share is written down *afterwards*, as what you will have noticed by then.

## Definition

Everything in [[SUVAT]] assumes one thing: the force, and so the acceleration, is **constant**. The moment a force depends on where the particle is or how fast it is going — air resistance growing with speed, gravity weakening with distance, a spring pulling harder the further it stretches — the five formulas are not approximately right; they are *wrong*, and the exam schemes say so in as many words ("use of suvat means 0 marks in this part").

What replaces them is Newton's second law read as a **differential equation**. With mass $m$, resultant force $F$ and acceleration $a$:

$$m\,a = F(x, v), \qquad\text{where } a \text{ can be written three ways:}$$

$$a = \frac{dv}{dt} \qquad a = v\,\frac{dv}{dx} \qquad a = \frac{d^2x}{dt^2}$$

That is the whole of the theory. The rest is craft — which face of $a$ to pick so that the equation *separates*, and which Pure 3 integral then finishes it — and craft is what Part I teaches by doing.

### 中文锚点

**这张卡是倒着写的。** 它讲的其实只有一件事：**一道看起来像 SUVAT 的题，怎么用微积分去做**——而这种"怎么做"的本事，是从题里学来的，不是从总结里学来的。所以先上五道真题（都是 9231 Paper 3 原题），一道一道做完，再回头总结它们共用的方法。

先给你物理画面。**跳伞。** 你从飞机上跳下去，最初几秒像自由落体：越来越快。但空气阻力跟着速度一起长——速度变为两倍，阻力变为四倍——几秒之后，阻力长到**恰好等于你的重力**，合力为零，你不再加速，以大约 200 km/h 匀速下落：这就是**终端速度**（terminal velocity，大陆课本叫收尾速度）。打开伞，阻力猛增，你减速到新的、慢得多的终端速度。整个过程里，加速度**每一刻都在变**，所以 SUVAT 一条也不能用（考卷原话：用了 SUVAT 这一问零分）。能用的是牛顿第二定律写成**微分方程**：$m\,\dfrac{dv}{dt} = mg - kv^2$，分离变量，积分。做完五道题你会自己看出来：**加速度有三张脸**——$\dfrac{dv}{dt}$、$v\dfrac{dv}{dx}$、$\dfrac{d^2x}{dt^2}$——题目问"多久"就用第一张，问"多远"就用第二张（链式法则变出来的那张）；选对了脸，剩下的就是 P3 的分离变量积分。真实世界里，汽车工程师测风阻用的就是这个方程（滑行测试）；F1 赛车松开油门、客机起飞滑跑、火箭升空，都是这同一个方程在不同场景下的样子——最后一节专门讲它们。

| English | 中文 | 记号 |
|---|---|---|
| Variable force | 变力 | $F(x, v)$ |
| Resistive force / drag | 阻力 | 与 $v$ 或 $v^2$ 成正比，方向与速度相反 |
| Terminal velocity | 终端速度 / 收尾速度 | 合力为零时的速度 |
| Separation of variables | 分离变量 | $\dfrac{dv}{F(v)} = \dfrac{dt}{m}$ |
| Chain-rule face of $a$ | 加速度的链式法则形式 | $a = v\dfrac{dv}{dx}$ |
| Initial condition | 初始条件 | 定积分常数 |

---

## Part I — Five questions, solved

*(Cambridge convention throughout: $g = 10$ m s⁻². Every answer is checked against the published mark scheme and verified by computer algebra. Before each solution, the line that matters: what the question asked for, and which face of $a$ that choice forced.)*

### Question 1 — drive against quadratic drag, both faces (9231 June 2026 P31/32 Q3)

*A particle of mass $6.4$ kg moves along a straight horizontal line under a constant driving force of $8$ N and a resistive force of $0.5v^2$ N, from rest. (a) Find the speed after it has travelled $0.8$ m. (b) Find an expression for $t$ in terms of $v$.* [5, 4]

*Terminal speed first:* $8 = 0.5v^2 \Rightarrow v_\infty = 4$.

**(a)** *Trigger: "after it has travelled 0.8 m" — a distance — so the $v\,dv/dx$ face.* Newton's second law along the line, drag opposing motion:

$$8 - 0.5v^2 = 6.4\,v\frac{dv}{dx}.$$

*Tool: separate; the numerator $v\,dv$ is $-\tfrac1{1}\,d(8 - 0.5v^2)$ up to a constant.*

$$x = \int \frac{6.4\,v}{8 - 0.5v^2}\,dv = -6.4\ln(8 - 0.5v^2) + c.$$

At $x = 0$, $v = 0$: $c = 6.4\ln 8$. So $x = 6.4\ln\dfrac{8}{8 - 0.5v^2}$, and at $x = 0.8$:

$$\frac{8}{8 - 0.5v^2} = e^{1/8} \;\Longrightarrow\; v^2 = 16\left(1 - e^{-1/8}\right) \;\Longrightarrow\; v = 1.37 \text{ m s}^{-1}.$$

(The scheme's guidance is instructive: had you written $x = -6.4\ln(0.5v^2 - 8) + c$ and found $c$ from $\ln(0 - 8)$, that is *"DM0"* — the wrong side. The terminal-speed line told you $8 - 0.5v^2 > 0$ throughout.)

**(b)** *Trigger: "$t$ in terms of $v$" — time — so the $dv/dt$ face.*

$$8 - 0.5v^2 = 6.4\frac{dv}{dt} \;\Longrightarrow\; t = \int\frac{6.4}{8 - 0.5v^2}\,dv = \int\frac{12.8}{16 - v^2}\,dv.$$

*Tool: MF19's $\displaystyle\int\frac{dx}{a^2 - x^2} = \frac{1}{2a}\ln\frac{a+x}{a-x}$ with $a = 4$.*

$$t = 12.8\cdot\frac{1}{8}\ln\frac{4+v}{4-v} + c = 1.6\ln\frac{4+v}{4-v} + c, \qquad t = 0,\ v = 0 \Rightarrow c = 0.$$

$$\boxed{t = 1.6\ln\frac{4+v}{4-v}} \qquad\text{equivalently } t = 3.2\operatorname{artanh}\frac v4,\ \text{ i.e. } v = 4\tanh\frac{t}{1.6}.$$

The scheme accepts the artanh form outright — and the inverted form is a $\tanh$, bending over toward $4$ and never touching it — the right-hand panel of the first figure in Part II.

### Question 2 — falling through air, the tanh solution (9231 November 2024 P32 Q7)

*A particle of mass $m$ is released from rest at $O$ and falls vertically against a resistive force of $0.1mv^2$ N. (a) Find $v$ in terms of $t$. (b) With $x$ the displacement below $O$, find $v^2$ in terms of $x$.* [6, 5]

*Terminal speed first:* $mg = 0.1mv^2 \Rightarrow v_\infty = 10$. Note $m$ cancels *only after* it has been written.

**(a)** *Trigger: "$v$ in terms of $t$" → $dv/dt$.* Taking down as positive:

$$m\frac{dv}{dt} = mg - 0.1mv^2 \;\Longrightarrow\; \frac{dv}{dt} = \frac{100 - v^2}{10} \;\Longrightarrow\; \int\frac{dv}{100 - v^2} = \int\frac{dt}{10}.$$

*Tool: the MF19 partial-fraction integral with $a = 10$.*

$$\frac{1}{20}\ln\frac{10+v}{10-v} = \frac{t}{10} + A, \qquad v(0) = 0 \Rightarrow A = 0 \;\Longrightarrow\; \frac{10+v}{10-v} = e^{2t}.$$

*Tool: remove the log and solve for $v$* (a separate M mark):

$$10 + v = e^{2t}(10 - v) \;\Longrightarrow\; v = \frac{10\,(e^{2t} - 1)}{e^{2t} + 1} = \boxed{10\tanh t}.$$

**(b)** *Trigger: displacement → $v\,dv/dx$.*

$$v\frac{dv}{dx} = \frac{100 - v^2}{10} \;\Longrightarrow\; -\tfrac12\ln(100 - v^2) = \frac{x}{10} + B, \qquad B = -\tfrac12\ln 100,$$

$$\boxed{v^2 = 100\left(1 - e^{-x/5}\right)}.$$

*Cross-check:* differentiate (b) — $2v\,\dfrac{dv}{dx} = 20e^{-x/5} = \dfrac{2(100 - v^2)}{10}$ ✓ — the two faces are consistent, as they must be, since they describe one fall.

![[variable-force-tanh-vs-exp.svg|760]]

Compare the shapes: quadratic drag gives $v = v_\infty\tanh(gt/v_\infty)$, linear drag gives $v = v_\infty(1 - e^{-gt/v_\infty})$ ([[Differential Equations]] §5 works that one). At the same terminal speed the tanh climbs faster and turns over harder — because for small $v$ the $v^2$ resistance is negligible and the fall is briefly *free*. The shape of the approach is a fingerprint of the drag law.

### Question 3 — friction plus linear drag on a rough table (9231 November 2025 P32 Q7)

*A particle of mass $m$ on a rough horizontal table moves against a resistive force $mgkv$ N and a frictional force $\mu mg$ N, starting at $O$ with speed $U$. (a) Show that $t = \dfrac{1}{gk}\ln\dfrac{kU + \mu}{kv + \mu}$. (b) With $U = 10$, $k = 0.04$, $\mu = 0.2$, find the distance $P$ moves before coming to rest.* [4, 4]

**(a)** *Trigger: a "show that" in $t$ → $dv/dt$; both forces oppose motion.*

$$m\frac{dv}{dt} = -mgkv - \mu mg \;\Longrightarrow\; \int\frac{dv}{kv + \mu} = -g\int dt \;\Longrightarrow\; \frac1k\ln(kv + \mu) = -gt + C.$$

$t = 0$, $v = U$: $C = \frac1k\ln(kU + \mu)$. Subtract and rearrange: $t = \dfrac{1}{gk}\ln\dfrac{kU+\mu}{kv+\mu}$. ∎ (The scheme wants "an intermediate step" shown before the given result — do not jump from the integral to the box.)

**(b)** *Trigger: distance → $v\,dv/dx$.* With the numbers, $g(kv + \mu) = 0.4v + 2 = \tfrac25(v + 5)$:

$$v\frac{dv}{dx} = -\tfrac25(v+5) \;\Longrightarrow\; dx = -\tfrac52\cdot\frac{v}{v+5}\,dv = -\tfrac52\left(1 - \frac{5}{v+5}\right)dv.$$

*Tool: the improper fraction split — divide first, then integrate.*

$$x = -\tfrac52 v + \tfrac{25}{2}\ln(v+5) + C, \qquad x = 0 \text{ at } v = 10 \Rightarrow C = 25 - \tfrac{25}{2}\ln 15.$$

At rest, $v = 0$: $x = 25 - \tfrac{25}{2}\ln 15 + \tfrac{25}{2}\ln 5 = 25 - \tfrac{25}{2}\ln 3 = \boxed{11.3 \text{ m}}$.

Two things to notice. Friction alone would give SUVAT (constant deceleration $2$ m s⁻²: $x = 100/4 = 25$ m); the drag term costs the particle more than half that distance. And the scheme prints a second route — invert (a) to $v = 15e^{-2t/5} - 5$, integrate in $t$ — with the same $11.3$: both faces, one answer.

### Question 4 — a force given as a function of $v$, and a physical "explain" (9231 June 2026 P34 Q5)

*A particle of mass $m$ moves in a straight horizontal line under a variable force $m(v^2 - ku^2)$, where $u$ is its initial velocity and $k > 1$. (a) Explain why, initially, the acceleration and velocity have opposite directions. (b) Find, in terms of $k$, the distance travelled before it first comes to instantaneous rest. (c) Find, in terms of $k$ and $u$, the time taken.* [1, 4, 4]

**(a)** At $t = 0$, $v = u$, so the force is $m(u^2 - ku^2) = mu^2(1 - k) < 0$ because $k > 1$: the acceleration is negative while the velocity is positive. *(One mark, one sentence — but it also tells you the side of every log below: $v^2 - ku^2 < 0$ throughout, so write the arguments as $ku^2 - v^2$.)*

**(b)** *Distance → $v\,dv/dx$:*
$$v\frac{dv}{dx} = v^2 - ku^2 \;\Longrightarrow\; x = \int\frac{v\,dv}{v^2 - ku^2} = \tfrac12\ln(ku^2 - v^2) + c,\qquad c = -\tfrac12\ln(ku^2 - u^2).$$
At rest: $x = \tfrac12\ln\dfrac{ku^2}{ku^2 - u^2} = \boxed{\tfrac12\ln\dfrac{k}{k-1}}$.

**(c)** *Time → $dv/dt$:*
$$\frac{dv}{dt} = v^2 - ku^2 \;\Longrightarrow\; t = \int\frac{dv}{v^2 - ku^2} = \frac{1}{2u\sqrt k}\ln\frac{u\sqrt k - v}{u\sqrt k + v} + c \quad(\text{MF19's integral with } a = u\sqrt k,\text{ signs flipped}).$$
$t = 0$ at $v = u$ fixes $c$; at $v = 0$:
$$\boxed{t = \frac{1}{2u\sqrt k}\ln\frac{\sqrt k + 1}{\sqrt k - 1}}.$$

The scheme's warning is worth quoting: a $c$ containing $\ln\dfrac{1-\sqrt k}{1+\sqrt k}$ "gives an undefined value" — the wrong side of the log again, and again part (a) had already told you which side is real.

### Question 5 — an inverse-square resistance, by energy (9231 June 2026 P33 Q2)

*A particle of mass $m$ moves in a straight line towards a fixed point $A$, subject to a resistive force inversely proportional to the square of its distance from $A$. Initially the distance is $d$ and the speed $u$; when the distance is $\tfrac12 d$ the particle has lost $\tfrac34$ of its kinetic energy. Find, in terms of $d$, the minimum distance of $P$ from $A$.* [6]

*Trigger: force depends on $x$ → $v\,dv/dx$, which here is the energy equation in disguise.* With $x$ the distance from $A$ and the resistance $k/x^2$ acting away from $A$ (against the motion):

$$mv\frac{dv}{dx} = \frac{k}{x^2} \;\Longrightarrow\; \tfrac12 mv^2 = -\frac{k}{x} + c.$$

Two conditions, two unknowns. At $x = d$, $v = u$: $\tfrac12 mu^2 = -\dfrac kd + c$. At $x = \tfrac12 d$, KE is a quarter of the original, so $v = \tfrac12 u$: $\tfrac18 mu^2 = -\dfrac{2k}{d} + c$. Subtracting: $\tfrac38 mu^2 = \dfrac kd$, so $k = \tfrac38 mu^2 d$ and $c = \tfrac78 mu^2$. The particle is closest when $v = 0$:

$$0 = -\frac{k}{x} + c \;\Longrightarrow\; x = \frac kc = \boxed{\frac{3d}{7}}.$$

(The scheme's guidance flags the trap in the setup: writing the force as $k/d^2$ — a constant — instead of $k/x^2$ scores B0. The force varies *with the particle's position*, and $d$ is only where it started.)

![[variable-force-see-it-move.mp4]]

---

## Part II — What the five questions had in common

You have now used $\dfrac{dv}{dt}$ three times, $v\dfrac{dv}{dx}$ four times, found a terminal speed before integrating, met the same partial-fraction integral twice, and been warned about the side of a logarithm on every question. Here is that experience, written down.

### The three faces of acceleration — and which to choose

The first face is the definition. The second is the two-line theorem you used in Questions 1(a), 2(b), 3(b), 4(b) and 5, and the one the syllabus names by hand:

$$a = \frac{dv}{dt} = \frac{dv}{dx}\cdot\frac{dx}{dt} = \frac{dv}{dx}\cdot v = v\,\frac{dv}{dx}.$$

*Tool: the chain rule.* It swaps time for position as the independent variable. Two remarks make it more than a trick:

- $v\,\dfrac{dv}{dx} = \dfrac{d}{dx}\!\left(\tfrac12 v^2\right)$. So $m\,v\,\dfrac{dv}{dx} = F$ is $\dfrac{d}{dx}\!\left(\tfrac12 m v^2\right) = F$ — **the work–energy theorem in differential form**: the rate at which kinetic energy grows per metre is the force. Integrating both sides over a distance recovers $\Delta(\tfrac12 mv^2) = \int F\,dx$ from [[Work, Energy and Power]]. When the force depends only on $x$, this is why an energy argument and the $v\,dv/dx$ argument are the same calculation.
- The third face, $\ddot x$, is rarely useful here: it needs $F$ as a function of $x$ *and* gives a second-order equation. Save it for [[Simple Harmonic Motion]].

**The decision** was made by the question every time — *how far* sent you to $v\,dv/dx$, *how long* to $dv/dt$, a force in $x$ to the energy face. Written out, so it can be made in one glance:

| Force depends on | Asked for | Use | Why |
|---|---|---|---|
| $v$ | $v$ or $t$ at a *time*; "find $t$ in terms of $v$" | $\dfrac{dv}{dt}$ | separates as $\dfrac{m\,dv}{F(v)} = dt$ |
| $v$ | $v$ at a *distance*; "how far before…" | $v\dfrac{dv}{dx}$ | separates as $\dfrac{m\,v\,dv}{F(v)} = dx$ |
| $x$ | anything | $v\dfrac{dv}{dx}$ (or energy) | $\dfrac{dv}{dt}$ would leave $x$ and $t$ tangled |
| $t$ | anything | $\dfrac{dv}{dt}$, integrate directly | this is [[Kinematics Calculus]], not this card |

![[variable-force-two-views.svg|780]]

The figure is Question 1 drawn: one particle asked two questions. Same drive, same drag, same mass — but *"how fast after $0.8$ m"* is a $v$–$x$ question and *"an expression for $t$ in terms of $v$"* is a $v$–$t$ question, and they are solved by different faces of the same acceleration. Both curves flatten at the same **terminal speed**: the speed at which the resistance has grown to equal the drive, so the resultant force — and with it the acceleration — is zero.

> [!tip] Terminal velocity costs one line, and it costs it *before* you integrate
> Set $a = 0$ in Newton's second law and solve for $v$. For $8 - 0.5v^2 = 6.4\,a$, terminal speed is $v = 4$ m s⁻¹, read straight off $8 = 0.5v^2$. Do this first, every time: it tells you what the answer must approach, it tells you which sign the log's argument must have, and it is often a mark on its own. Note the word *approach*: the solutions below reach it only as $t \to \infty$.

---

### The four integrals you met

Every one of the five reduced, after separation, to one of a handful of integrals — all in Pure 3, two of them printed on MF19. There are no others on this row.

| After separating | Integral | Result | Where it comes from |
|---|---|---|---|
| linear drag, $\dfrac{dv}{dt}$ | $\displaystyle\int \frac{dv}{a - bv}$ | $-\dfrac1b\ln\lvert a - bv\rvert$ | the log rule |
| quadratic drag, $v\dfrac{dv}{dx}$ | $\displaystyle\int \frac{v\,dv}{a - bv^2}$ | $-\dfrac{1}{2b}\ln\lvert a - bv^2\rvert$ | the numerator is (almost) the derivative of the denominator |
| quadratic drag, $\dfrac{dv}{dt}$ | $\displaystyle\int \frac{dv}{c^2 - v^2}$ | $\dfrac{1}{2c}\ln\left\lvert\dfrac{c+v}{c-v}\right\rvert$ | partial fractions — **on MF19**; equally $\dfrac1c\operatorname{artanh}\dfrac vc$ |
| inverse-square, $v\dfrac{dv}{dx}$ | $\displaystyle\int \frac{dx}{x^2}$ | $-\dfrac1x$ | the power rule |

Three habits the mark schemes rewarded or punished above, in their own words:

- **Keep the mass.** "Must see $m$, may be cancelled before integrating" — the equation is Newton's, not a rate you made up. A missing $mg$ term scores nothing.
- **The constant, then the condition.** Integrate with $+c$, *then* substitute the initial condition — "use correct initial conditions to find $c$" is a separate dependent mark, and a $c$ found from $\ln(0 - 8)$ is flagged as a wrong-side value that scores zero.
- **Modulus signs are condoned but the side is not.** $\ln\lvert 8 - 0.5v^2\rvert$ and $\ln\lvert 0.5v^2 - 8\rvert$ differ by a constant and both are accepted; what is *not* accepted is a $c$ that makes the argument of the log negative for the actual motion. Terminal velocity tells you the side: for $v$ climbing from $0$ toward $4$, it is $16 - v^2$ that stays positive.

---

### Where this is the working tool: the coast-down test

Every car you have ridden in had its drag measured with this card's equation. To certify fuel economy and emissions, engineers run a **coast-down test** (the standard is SAE J1263 / the EPA's version of it): accelerate the car on a flat track, put it in neutral, and record speed against time as it rolls to a stop under nothing but rolling resistance and air drag. The model is exactly Question 3's:

$$m\frac{dv}{dt} = -\left(A + Bv + Cv^2\right),$$

with $A$ the rolling resistance, $C \approx \tfrac12\rho\,C_d\,S$ the aerodynamic term ($C_d$ the drag coefficient, $S$ the frontal area), and $B$ the small mixed term. The recorded $v(t)$ is fitted to the solution of this differential equation — the same partial-fraction integral as Question 2 — and the fitted $A, B, C$ become the "road-load coefficients" that the emissions dynamometer is then programmed to reproduce. When a manufacturer's fuel-economy figure turns out to be optimistic, this fit is where investigators look first: a coast-down run on a slightly downhill track, or with over-inflated tyres, lowers the measured $C$ and every subsequent figure with it. The equation is not a classroom model of the real test; it *is* the real test.

The same mathematics, run downward, is the skydiver of the anchor and the raindrop that reaches the ground at a walking pace instead of the speed of a bullet; run outward, it is the escape-velocity calculation in [[Gravitational Fields]], where the "variable force" is gravity itself falling off as $1/x^2$.

---

## Part III — Misconceptions, now that you have seen them

### 1. Reaching for SUVAT

The most-penalised error on the row, and the schemes name it: *"use of suvat means 0 marks in this part."* If the force depends on $v$ or $x$, the acceleration is not constant, and no SUVAT formula holds even approximately over the motion. **Fix:** the first line is always $m\,a = F$ with $a$ written as one of its three faces — never $v = u + at$.

### 2. Dropping the mass

Writing $\dfrac{dv}{dt} = 10 - 0.1v^2$ *directly* is marked as "no $mg$ term" — zero. **Fix:** write Newton's law with every force and the mass, then cancel. The scheme's own wording: "must see $m$, may be cancelled before integrating."

### 3. Choosing the wrong face

Using $\dfrac{dv}{dt}$ when the question asks for a distance leaves you with $v(t)$ and one more integration you may not be able to do in closed form (Question 3's alternative route shows it *can* be done, but it is longer). **Fix:** read the question's last line first: *time* → $\dfrac{dv}{dt}$; *distance* or a force in $x$ → $v\dfrac{dv}{dx}$.

### 4. The log on the wrong side

$\ln(v^2 - 16)$ when $v < 4$ throughout; $\ln(0 - 8)$ at the initial condition; a constant that makes the argument negative. The schemes have a name for this: an *undefined value for $c$*, DM0. **Fix:** find the terminal speed (or, in Question 4, the sign of the force) *before* integrating, and write the argument of every log as the positive quantity.

### 5. "It reaches terminal velocity"

It approaches it. $v = 10\tanh t$ is below $10$ for every finite $t$; so is $4\tanh(t/1.6)$. **Fix:** terminal velocity is a limit, found by setting $a = 0$; in words, "the speed *tends to* $10$ m s⁻¹."

### 6. The resistive force pointing the wrong way

Resistance opposes *velocity*, not gravity and not "up". A particle thrown upward against $kv^2$ has $m\dot v = -mg - kv^2$ on the way up and $m\dot v = mg - kv^2$ on the way down — two different equations, joined at the top where $v = 0$. **Fix:** draw the velocity arrow first, then put the drag arrow against it.

---

## Beyond syllabus

### Why $v$ and why $v^2$ — the two drag regimes

Recall that the syllabus hands you the drag law. Physics decides it. At low speeds and small sizes — a dust grain, a droplet in mist, a sphere in honey — the fluid slides past in orderly layers, viscosity dominates and drag is **linear in $v$** (Stokes' law, $F = 6\pi\eta r v$). At the speeds and sizes of a skydiver, a car or a raindrop, the fluid is shoved aside and left swirling, momentum transfer dominates and drag is **quadratic**, $F = \tfrac12\rho C_d S v^2$. The dial between the regimes is the **Reynolds number**, $\mathrm{Re} = \rho v L/\eta$: below about $1$ the linear law holds, above a few thousand the quadratic one, and in between nature uses a blend that no clean integral fits. That is why the exam's two laws are not arbitrary: they are the two clean limits of one physical dial.

### The tanh is not a coincidence

Recall that $\tanh$ appeared in Questions 1 and 2 as the inverse of the MF19 log. There is a reason it keeps appearing: $\dfrac{dv}{dt} = g\left(1 - \dfrac{v^2}{v_\infty^2}\right)$ is the **logistic-shaped** equation — growth that is proportional to how far you are from a ceiling — and its solutions are always sigmoids. The same $\tanh$ governs a capacitor's voltage in some nonlinear circuits, the magnetisation of iron, and the activation function of a neuron in a neural network. [[Hyperbolic Functions]] is the card; here you have met one of its native habitats.

### What an exact solution buys you

Every question above has a closed form because the integrals happen to be elementary. Change $v^2$ to $v^{1.8}$ — a realistic fit for some shapes — and no closed form exists; the engineer integrates numerically, step by step, exactly as the clip above was generated. The syllabus's "calculus restricted to Pure 3" is an honest boundary: beyond it, the *method* (write $ma = F$, separate, integrate) is unchanged, and only the integral stops being one you can do by hand.

---

### Three machines that live in this equation

The exam's particle on a line is a stand-in for the objects mechanical engineers actually design, and each of the three below is this card's equation with the constants filled in — until the last one, which breaks it in an instructive way.

**A Formula 1 car lifting off the throttle.** At $300$ km h⁻¹ the aerodynamic drag on an F1 car is several kilonewtons; lift off the throttle and, before the brakes are even touched, the car decelerates at about $1g$ from drag alone — Question 1 run backwards, $m\,v\dfrac{dv}{dx} = -cv^2$, which is why the braking-distance markers on a circuit are not evenly spaced in speed. The same $v^2$ law is why the drag-reduction flap (DRS) is worth so much on the straight and nothing in the corners, and why the coast-down test of Part II is run at several speeds: the fitted $C$ *is* the car's $\tfrac12\rho C_d S$.

**An airliner's takeoff roll.** Thrust $T$ is roughly constant; drag $D = \tfrac12\rho C_D S v^2$ and rolling resistance $\mu(W - L)$, with lift $L$ also growing as $v^2$, oppose it. The ground-roll distance to rotation speed $v_R$ is

$$s = \int_0^{v_R}\frac{m\,v\,dv}{T - D(v) - \mu\,(W - L(v))},$$

which is Question 1(a) with three terms instead of two: the $v\,dv/dx$ face, chosen because the runway length is a *distance*. Every performance chart a pilot reads before departure — how much runway at this weight, this temperature, this altitude — is that integral evaluated for the day's air density. Hot, high and heavy all make the denominator smaller and the integral longer.

**A rocket — where this card's equation stops.** Newton's second law as written on this card, $m\,\dfrac{dv}{dt} = F$, assumes the mass is fixed. A rocket throws most of itself out of the back: nine-tenths of a launch vehicle on the pad is propellant. The honest form is the momentum one, $\dfrac{d(mv)}{dt} = F$, and with thrust equal to exhaust speed times the rate of mass loss it becomes

$$m\frac{dv}{dt} = -v_e\frac{dm}{dt} - mg - D(v),$$

with $m = m(t)$ falling as the tanks empty. Drop gravity and drag and separate: $dv = -v_e\,\dfrac{dm}{m}$, so $\Delta v = v_e\ln\dfrac{m_0}{m_1}$ — **Tsiolkovsky's rocket equation**, the reason rockets are mostly fuel and staging exists. Put gravity and drag back and the two extra terms have names in the trade — *gravity loss* and *drag loss* — and the drag term is exactly the $v^2$ law of Question 2, with $\rho$ now falling with altitude so that the aerodynamic load peaks partway up (the "max-Q" moment on a launch broadcast) and then fades. One more line of physics than the syllabus, and the whole of astronautics opens.

## Exam Notes

### Cambridge 9231 Further Mathematics (Paper 3, §3.5)

- The one LO verbatim: *"solve problems which can be modelled as the linear motion of a particle under the action of a variable force, by setting up and solving an appropriate differential equation"* — with its two notes, *"including use of $v\frac{dv}{dx}$ for acceleration, where appropriate"* and *"calculus required is restricted to content from Pure Mathematics 3"*. $g = 10$.
- **The mark structure is nearly fixed** across the papers used above: **B1** Newton's second law with the *correct face of $a$* ("acceleration must be $v\frac{dv}{dx}$" / "must be $\frac{dv}{dt}$") and every force including $m$; **M1** separate variables and integrate to the right form (a log, or two logs, or the partial-fraction pair); **A1** the correct integral with $+c$; **DM1** the initial condition used correctly — on the right side of the log; **A1** the answer, WWW, exact or 3 s.f.
- **MF19 prints** $\int\frac{dx}{a^2 - x^2} = \frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert$ and the artanh form; the schemes accept either. The $\ln$ of a quadratic from $\int\frac{v\,dv}{a - bv^2}$ is *not* printed — spot the derivative in the numerator.
- Question shapes, all from real papers: drive against $v^2$ drag, both faces (June 2026 P31/32); free fall against $v^2$ (Nov 2024 P32); drag plus friction with a "show that" (Nov 2025 P32); a force as a function of $v$ with an *explain* opener (June 2026 P34); an inverse-square resistance solved by energy (June 2026 P33). Variable force crosses over with §3.4 (elastic strings, [[Elastic Strings and Springs]]) and with the inverse-square gravity of [[Gravitational Fields]].

### Edexcel IAL Further Mathematics (M3 §3.1 and §3.3)

- M3.1.1 names the kinematics side — $\frac{dv}{dt}$, $v\frac{dv}{dx}$, $\frac{dx}{dt}$ as functions of $t$ or $x$ — and M3.3.1 the dynamics side, *Newton's laws of motion applied with a variable applied force, including gravitational*. This card covers both, with [[Kinematics Calculus]] supplying the pure-time case and [[Gravitational Fields]] the gravitational one. Same integrals, $g = 9.8$ on that board.

### AP Physics C: Mechanics (Unit 2 §2.9, Resistive Forces)

- The 2024–25 redesign made this a named topic, calculus-based and AP-C only: drag with $v$ or $v^2$ dependence, and terminal velocity from $\frac{dv}{dt} = g - \frac{b}{m}v$ or $g - \frac{c}{m}v^2$. Examples 2 and 3 *are* the two equations; the free-response staple asks for the terminal speed from $a = 0$, then $v(t)$, then a sketch of $v$–$t$ with the asymptote. The exponential case is worked in [[Differential Equations]] §5.

### Not examined on…

- **Cambridge 9709**: Paper 4 mechanics has no variable force — its calculus kinematics is acceleration as a function of *time* only ([[Kinematics Calculus]]). The *pure* half surfaces in **P3 §3.8** as modelling with a separable differential equation from a stated rate — the same integrals with the physics stripped off.
- **OxfordAQA 9660**: kinematics by calculus ($\frac{ds}{dt}, \frac{dv}{dt}$) only; no velocity-dependent forces, verified against the specification.
- **Cambridge 9702 and 0625**: terminal velocity is examined *qualitatively* — describe the forces, sketch $v$–$t$, explain why acceleration falls — never as a differential equation. The qualitative story is in [[The Friction Limit]]; this card is its calculus.

---

## Formula summary

| Situation | Equation | Solution shape |
|---|---|---|
| Terminal speed | set $a = 0$: $F_{\text{drive}} = R(v_\infty)$ | one line, before integrating |
| Linear drag, time | $m\dfrac{dv}{dt} = F - bv$ | $v = v_\infty\left(1 - e^{-bt/m}\right)$ from rest |
| Quadratic drag, time | $m\dfrac{dv}{dt} = F - cv^2$ | $v = v_\infty\tanh\dfrac{\sqrt{Fc}\,t}{m}$ from rest |
| Quadratic drag, distance | $m\,v\dfrac{dv}{dx} = F - cv^2$ | $v^2 = v_\infty^2\left(1 - e^{-2cx/m}\right)$ from rest |
| Force in $x$ | $m\,v\dfrac{dv}{dx} = F(x)$ | $\tfrac12 mv^2 = \int F\,dx$ — energy |

---

## Connections

- **Parents:**
   - [[Newton's Laws of Motion]] — the equation is $F = ma$; this card is what happens when $F$ refuses to be constant.
   - [[Kinematics Calculus]] — the three faces of acceleration and the chain-rule derivation of $v\frac{dv}{dx}$; that card handles $a(t)$, this one $a(v)$ and $a(x)$.
   - [[Differential Equations]] — separation of variables, the integrating factor, and §5's linear-drag fall, which this card's quadratic cases sit beside.
   - [[Work, Energy and Power]] — $v\frac{dv}{dx}$ is $\frac{d}{dx}(\tfrac12 v^2)$: the work–energy theorem in differential form.
   - [[Hyperbolic Functions]] — where the $\tanh$ solutions and the artanh integral live.

- **Child:**
   - [[Gravitational Fields]] — escape velocity is this card's method with $F = -GMm/x^2$; that card works it in full.

- **Siblings:** [[SUVAT]] (the constant-force special case, and the thing to stop using); [[Elastic Strings and Springs]] (a force in $x$ that the energy face handles); [[Simple Harmonic Motion]] (the $\ddot x$ face, when $F = -kx$); [[The Friction Limit]] (terminal velocity told qualitatively).

- **Misconception traps cleared:** SUVAT under a varying force; the dropped mass; the wrong face of $a$; the log on the wrong side; "reaches" terminal velocity; drag pointing against gravity instead of against velocity.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $a = v\dfrac{dv}{dx}$ | `a = v\dfrac{dv}{dx}` | the chain-rule face |
| $\dfrac{d}{dx}\!\left(\tfrac12 v^2\right)$ | `\dfrac{d}{dx}\!\left(\tfrac12 v^2\right)` | energy form of the same thing |
| $\displaystyle\int\frac{dv}{a^2 - v^2} = \frac{1}{2a}\ln\frac{a+v}{a-v}$ | `\int\frac{dv}{a^2 - v^2} = \frac{1}{2a}\ln\frac{a+v}{a-v}` | MF19 |
| $v = v_\infty\tanh(gt/v_\infty)$ | `v = v_\infty\tanh(gt/v_\infty)` | quadratic-drag fall from rest |
| $\operatorname{artanh}$ | `\operatorname{artanh}` | inverse hyperbolic tangent |

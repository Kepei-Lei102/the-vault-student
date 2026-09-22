---
chinese: 当模型失灵时 (dāng móxíng shīlíng shí)
prerequisites:
  - "[[Laws and Theorems]]"
  - "[[Learning as Verification]]"
leads_to: []
teach_together:
  - "[[The Corn Wouldn’t Behave]]"
  - "[[Change the Representation]]"
tags:
  - subject/methodology
  - subject/philosophy
  - domain/modelling
  - domain/problem-solving
  - level/life
  - level/university
  - type/meta
  - type/methodology
  - type/cross-domain
  - misconception/correct-calculation-means-correct-model
  - misconception/more-detail-is-always-better
  - misconception/one-good-fit-proves-a-model
---

# When a Model Breaks 当模型失灵时

> You add twelve sine waves. The pitch is right. The frequencies are right. The program does exactly what you asked.
>
> The piano is still missing.

## The problem behind the wrong answer

A **model** is a deliberately selective representation of something: an equation, a simulation, a diagram, even the rule “this walk takes fifteen minutes.” It keeps relationships useful for a purpose and leaves other things out.

A model **breaks for a task** when its predictions or decisions become inadequate for that task under the conditions in which we use it. This need not mean the arithmetic failed, the underlying science was overturned, or the model has become useless everywhere.

The practical question is: **which part of our account stopped earning its keep?**

[[Learning as Verification]] gives checks for a result. Here the next move is to use the *shape of the mismatch* to choose what to investigate. [[Laws and Theorems]] distinguishes deduction from empirical support: perfectly valid deductions can begin from assumptions that do not adequately describe the situation.

## 中文锚点

平时从家走到地铁站要十五分钟，你便照这个时间出门。今天路口施工，多等了两轮红灯，结果迟到了。你未必走慢了，十五分钟也未必记错了；只是这个估计一直默认路能照常走。要是把今天多花的时间全算成“我走得慢”，等施工结束，你又会把路上要花的时间估长了。模型失灵时，先别急着把数字改到对得上，先看看：原来没算进去的那件事，是不是现在开始影响结果了？

## 1. A model needs a job description

A map of the metro omits most streets. That omission makes it easier to choose a train. The same map is poor equipment for walking between stations: drawn distance need not be walking distance. **The usefulness belongs to a pairing: model and purpose.**

Before predicting, make four things explicit:

| Question | Pendulum example | Piano example |
|---|---|---|
| What must be predicted? | Time for one complete swing | A waveform with a chosen pitch and evolving tone |
| Under which conditions? | A small release angle, fixed length | A chosen note, playback level and time interval |
| What was left out? | Air resistance, pivot friction, finite bob size; perhaps the sine's curvature | Hammer noise, soundboard and pedal resonances |
| What would count as adequate? | Period error below a chosen 1% | Recovering the specified partials; realism requires a separate listening comparison |

The last row prevents a silent change of goal. A successful lesson in additive synthesis is not automatically a successful imitation of a concert grand.

An **assumption** fixes what the model permits or ignores. A **parameter** sets a value *within* that chosen structure. “Speed stays constant” is an assumption; “the speed is 5 km/h” is a parameter value. Altering 5 to 4 does not give the model traffic lights.

A **domain of validity** is the set of conditions under which the model is adequate for the stated purpose. It comes with a tolerance, not a magic border printed on the equation.

## 2. The piano: add the ingredient the failure asks for

The A4 construction in [[Fourier Series#First example — build an A4 piano-style note]] is a model ladder you can hear:

![[fourier-piano-ladder.wav]]

*Five stages: one sine → four harmonics → twelve harmonics → a struck-and-decaying mixture → slightly detuned, slightly inharmonic string models. This is generated audio, not a recording of an acoustic piano. A common master gain is used; the stages are not loudness-matched.*

### What each change can explain

1. **One sine:** supplies a clean 440 Hz oscillation. It is a useful pitch reference, but has none of the chosen upper partials.
2. **More harmonics:** supplies a richer repeating waveform. Yet constant amplitudes remain constant. Twelve steady components cannot, merely by becoming twenty, explain a note that quickly strikes and fades.
3. **An envelope:** lets component amplitudes change with time. Now the model contains an attack and a decay; faster fading of upper components can change the tone during the note.
4. **Slightly different string frequencies:** permits slow beating. Stretched partial frequencies also relax the assumption that every partial is an exact integer multiple of the fundamental.

The envelope changes the *kind of behaviour available*. That is a structural revision. Adjusting a decay time from two seconds to three is parameter tuning within the revised model. Instrument tone depends on time development as well as spectral components. [UNSW Physclips: timbre and envelope](https://www.animations.physics.unsw.edu.au/jw/timbre-envelope.htm)

There is a subtle exception worth keeping: fixed-amplitude sines of **nearby** frequencies can produce beats, and sufficiently rich Fourier representations can describe a finite recording. The failure here belongs to the particular **small, exactly harmonic, stationary recipe**. It is not a limitation of sine waves as building blocks.

### What the demonstration does not establish

Recovering the intended frequencies with an FFT checks part of the construction. It does not establish acoustic realism: the FFT has no independent knowledge of the piano we intended to imitate.

For that, choose a reference recording and a comparison task. Match pitch and control playback level; inspect the attack, decay and time-varying spectrum; use repeated listening judgments if perceptual resemblance is the goal. Keep some notes or playing strengths out of the tuning process and test them afterwards. Success on one softly struck A4 says little about a hard-struck low C.

**Choose the next ingredient from the unexplained behaviour.** A longer list of ingredients is not evidence that the model improved.

## 3. Four places a discrepancy can come from

Suppose a prediction misses an observation. Several explanations may fit that one miss.

| Possible source | Example | A check that helps separate it |
|---|---|---|
| **Implementation or calculation** | Degrees sent into a sine function expecting radians | Run a known-angle case; compare an independent calculation |
| **Measurement** | Timing half a swing while reporting a full period | Define the event precisely; inspect a video or compare observers |
| **Input or parameter** | Measuring the string but omitting the distance to the bob's centre | Remeasure the model's actual length; propagate its uncertainty |
| **Model structure or conditions** | Using the small-angle approximation for a wide swing | Vary release amplitude while holding length fixed |

This is a search order, not a rule that only one fault can exist. A biased instrument and an inadequate model can fail together.

**Verification** asks whether we implemented the specified model correctly. **Validation** asks how adequately its predictions describe the target situation for the intended use. A simulation that conserves its model's energy can pass a valuable verification check while describing a real, frictional pendulum badly.

Parameter uncertainty and structural error also need different repairs. Remeasuring a length can reduce uncertainty about that length. Repeatedly measuring it cannot make an amplitude-independent formula acquire an amplitude dependence.

## 4. Worked example — the pendulum that exposes the assumption

### Predict before collecting numbers

**Trigger:** we want to know whether swing size matters. **Tool: derive the restoring force before choosing a familiar formula.**

For a point-mass bob on a massless, fixed-length support, with uniform gravity and no damping, the tangential force is $-mg\sin\theta$. The tangential acceleration is $L\,d^2\theta/dt^2$, so

$$mL\frac{d^2\theta}{dt^2}=-mg\sin\theta
\quad\Longrightarrow\quad
\frac{d^2\theta}{dt^2}=-\frac gL\sin\theta.$$

The familiar simplification replaces $\sin\theta$ by $\theta$, **in radians**, giving

$$\frac{d^2\theta}{dt^2}\approx-\frac gL\theta,
\qquad T_0=2\pi\sqrt{\frac Lg}.$$

[[Simple Harmonic Motion]] develops that linear restoring relationship. The resulting period has no amplitude in it. **That omission makes a testable prediction:** at the same length and gravity, every allowed release angle should give the same period.

The nonlinear equation retains $\sin\theta$ and predicts a longer period at larger amplitude. Both equations still describe idealised pendulums. Calling the nonlinear calculation “the real pendulum” would quietly hide its remaining assumptions. [MIT mechanics, Chapter 24 and Appendix 24A](https://www.ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter24.pdf)

### Compare a deliberately controlled reference

**Trigger:** isolate the effect of the small-angle approximation. **Tool: compare two models that differ only in that approximation.**

For $L=1.000$ m and $g=9.81$ m s$^{-2}$, the small-angle period is $T_0=2.00607$ s. The accompanying program computes the nonlinear ideal period by numerical integration:

| Release amplitude | Nonlinear ideal period / s | Small-angle period's shortfall |
|---|---:|---:|
| $5^\circ$ | 2.00702 | 0.0476% |
| $15^\circ$ | 2.01469 | 0.4282% |
| $30^\circ$ | 2.04099 | 1.7111% |
| $60^\circ$ | 2.15287 | 6.8192% |
| $90^\circ$ | 2.36784 | 15.2787% |

Here the percentage is $100(T-T_0)/T$: the denominator is the nonlinear reference period. These are **computed model comparisons, not laboratory observations**. They isolate one approximation error; they do not validate the nonlinear model against a physical bob.

![[model-breaks-pendulum.svg|900]]

*Top: the nonlinear prediction changes with amplitude. Both versions of the small-angle model stay flat, even after a length is chosen to fit the 60° case. Bottom: the error budget sets the usable amplitude range. The dashed 1% line is our chosen requirement.*

### The tempting repair that fixes the wrong thing

**Trigger:** the 60° prediction is too fast. **Tool under suspicion: fit the length to one period.**

Rearrange the small-angle formula:

$$L_{\mathrm{fit}}=g\left(\frac{T}{2\pi}\right)^2.$$

Using $T=2.15287$ s gives $L_{\mathrm{fit}}\approx1.152$ m. At 60°, the adjusted model now matches perfectly. But the measured ideal-model length was 1.000 m, and the adjusted formula predicts 2.15287 s even at 5°. It has bought one agreement by sacrificing another.

**Tool that separates the explanations: change amplitude, keep the apparatus fixed.** A single wrong length rescales the small-angle prediction for *every* angle. The nonlinear model predicts a systematic increase with angle. An amplitude sweep lets these explanations disagree.

In a physical experiment, also check that length, release technique, timing convention and damping are controlled well enough to resolve the difference. A trend is a clue, not a certificate naming its cause.

### Repair the assumption, then test somewhere new

Replacing $\theta$ with $\sin\theta$ in the force law restores the missing dependence. Test the revised prediction at amplitudes not used to choose it. If the measured amplitude decays substantially, damping may now matter too.

For **1% period accuracy relative to this nonlinear ideal reference**, the small-angle model remains adequate up to about **22.9°**. For a stricter task that boundary moves inward; a rough classroom estimate may tolerate much more. A pendulum clock also accumulates timing errors over many swings, so a small per-period discrepancy can matter.

The conclusion is local and useful: **keep the cheap model where its errors fit the job; use the richer one where the neglected term matters.**

## 5. Let the leftover error tell you where to look

A **residual** is an observed value minus its prediction:

$$r_i=y_i-\hat y_i.$$

A model can get the average about right while missing a pattern. Plot the leftovers against time, amplitude, temperature, or another variable that might explain the failure. Residual plots often reveal inadequacy that a single fit score conceals. [NIST: assessing model fit](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm)

| Pattern | A hypothesis worth testing | Why it is not a verdict |
|---|---|---|
| Nearly constant offset | An instrument's zero or a missing constant term | Either can produce the same pattern |
| Error grows with swing amplitude | Small-angle assumption is inadequate | Release or timing practice could also change with amplitude |
| Error grows with elapsed time | A small rate error accumulates, or conditions drift | The clock or sensor can drift too |
| Larger scatter at larger readings | Measurement variability grows with scale | The mean prediction could still be appropriate |

The last case matters: changing a model's **uncertainty description** can be the needed revision even when its central prediction is useful. A wider uncertainty interval must have evidence behind it; merely widening it until every point fits explains nothing.

Residuals alone cannot usually identify a unique cause. **Design a case where rival explanations predict different outcomes.** That is the move from spotting a problem to learning from it.

## 6. Everyday transfer — is the walk slower, or is there more waiting?

Suppose a 1.2 km walk usually takes 16 minutes. You represent the journey by

$$t=\frac dv,$$

which gives $v=4.5$ km/h. After roadworks, the same journey takes 22 minutes. You could revise the speed to about 3.27 km/h and obtain a perfect fit to that journey.

But another possibility is **six minutes of additional waiting**, with your moving speed unchanged:

$$t=\frac d{v_{\mathrm{moving}}}+t_{\mathrm{waiting}}.$$

One total journey time cannot tell these explanations apart. There is one measured total and two unknown contributions. **More careful division does not supply missing information.**

**Trigger:** two explanations fit the same total. **Tool: measure the part on which they disagree.** Time the stationary intervals separately. Or compare routes with similar distance and different junction delays, while recording moving time. The speed-change account and the waiting-time account now make different predictions.

For tomorrow's departure, you may only need a conservative total-time estimate. For deciding whether to walk faster or choose another route, you need the decomposition. The intended decision determines what the model must distinguish.

If the roadworks end, adding six minutes forever becomes a new mistake. A model can cease to work because the world changed, even though it was adequate when built.

## 7. Hands-on — find the boundary yourself

Run the source beside this note:

```bash
python3 model-breaks-lab.py
```

It uses the Python standard library. `--figures` additionally needs Matplotlib and regenerates the figure. The program prints the period table, the misleading fitted length, and the 1% boundary.

**Predict first:** at 30°, will the error be closer to 0.5%, 2%, or 10%? Then run it. Change the tolerance in `boundary()` from `.01` to `.005` and predict which way the boundary moves.

### Where the numerical reference comes from

Recall that energy conservation relates the bob's speed to its height. Released from rest at amplitude $A$,

$$\frac12mL^2\left(\frac{d\theta}{dt}\right)^2
=mgL(\cos\theta-\cos A).$$

Solving for the elapsed time and taking four equal quarter-swings gives an integral. The substitution $\sin(\theta/2)=\sin(A/2)\sin\phi$ removes the awkward turning-point denominator, producing

$$T=4\sqrt{\frac Lg}\int_0^{\pi/2}
\frac{d\phi}{\sqrt{1-\sin^2(A/2)\sin^2\phi}}.$$

The program divides this interval into equal panels, samples at each midpoint and adds the areas. At $A=0$, the integrand is 1 and we recover $T_0$. At positive amplitude it is greater than 1 except at the endpoint $\phi=0$, so the period increases. This explains the direction of the discrepancy before any numerical work.

**Verify the computation:** double the number of panels and compare. Agreement checks numerical convergence for this integral; it does not test whether friction was negligible in an experiment. Distinguishing those two conclusions is the exercise.

**Optional physical test:** use a small, securely attached bob in a clear space. Measure pivot-to-centre length, release without a push at modest angles, and time several complete swings on video. State timing uncertainty and record any amplitude decay. Compare against both predictions; retain an inconclusive result when the difference is smaller than your measurement uncertainty.

## 8. Where this is a working tool

**Instrument calibration.** A sensor's displayed reading is produced by a model relating its response to the measured quantity. A straight-line fit can be convenient over a limited range. Checking residuals across that range can reveal curvature; fitting the same points more precisely cannot remove it. Test the revised calibration on separate reference measurements. [[Calibration of Instruments]] supplies the measurement context.

**Audio synthesis.** The pianist controls more than pitch: attack and tone evolve with the strike. A model designed for ear-training may need a stable pitch reference; a virtual instrument needs substantially more. The piano ladder makes model revision audible without pretending that it completes the instrument.

**Software that predicts.** Tests can establish that a commute estimator implements `distance / speed` correctly. They cannot establish that this is an adequate model of a rush-hour journey. Software tests and comparisons with observed journeys answer different questions. [[You're the Architect, the AI is the Bricklayer]] places responsibility for those requirements with the person defining the system.

## 9. The wrong lessons to avoid

- **“Any mismatch disproves the whole theory.”** First locate the implementation, measurement, parameter and modelling assumptions involved. A large-angle pendulum challenges a linear approximation; it does not by itself overthrow Newton's laws.
- **“One perfect fit proves the explanation.”** The fitted length and fitted walking speed each match one case while concealing alternatives. Test a case that separates them.
- **“More parameters must help.”** More freedom can improve a fit to old data while fitting its accidents. Choose an untouched test case before tuning, and do not repeatedly use it as another training case.
- **“The more detailed model is reality.”** The nonlinear pendulum still omits friction; the richer piano still omits the soundboard. State the remaining scope honestly.
- **“A simple model is embarrassing.”** A model that answers the needed question within tolerance, cheaply and transparently, has done its job.
- **“The model failed, so I failed.”** Finding a reproducible boundary is new knowledge. The failure worth avoiding is hiding the mismatch until someone relies on the prediction.

## 10. Carry this move into the next problem

Before changing a number, finish the sentence:

> **“If the missing ingredient is ___, changing ___ while holding ___ fixed should change the error in this way: ___.”**

For the pendulum: if the missing ingredient is the sine's curvature, increasing release angle at fixed length should increase the small-angle period's shortfall.

Then run that test, revise only what the evidence supports, and check a new case. The aim is to understand *why* the model succeeds, so that you can recognise where it will stop succeeding.

## Connections

- **Historical companion:** [[The Corn Wouldn’t Behave]] — McClintock’s maize patterns, controlled crosses and a genetic element whose location could change.

- **Foundations:** [[Laws and Theorems]] — deduction and empirical support; [[Learning as Verification]] — checks that expose a discrepancy.
- **Choosing a framework:** [[Choosing Effective Equations]] — physical conditions select equations; [[Forward Reading and Problem Discovery]] — trace what each condition makes possible.
- **Worked mechanisms:** [[Fourier Series]], [[Fourier Transform]], [[Simple Harmonic Motion]] — the sound recipe, its analysis and the linear restoring model.
- **Evidence:** [[Calibration of Instruments]], [[Error Propagation]], [[Scatter Diagrams]] — measurements, their limits and visible patterns.
- **Responsibility:** [[You're the Architect, the AI is the Bricklayer]] — choosing the requirements against which an implementation is judged.

## Sources

- [UNSW Physclips — Timbre and envelope](https://www.animations.physics.unsw.edu.au/jw/timbre-envelope.htm): sound identity depends on spectral content and its development through time.
- [MIT OpenCourseWare — Classical Mechanics, Chapter 24](https://www.ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter24.pdf): pendulum equation and finite-amplitude period. Numerical values above are independently generated by the accompanying script.
- [NIST/SEMATECH Engineering Statistics Handbook — How can I tell if a model fits my data?](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm): residuals, model adequacy and limits of a single fit statistic.

## LaTeX Reference

| Expression | Source |
|---|---|
| $r_i=y_i-\hat y_i$ | `r_i=y_i-\hat y_i` |
| $T_0=2\pi\sqrt{L/g}$ | `T_0=2\pi\sqrt{L/g}` |
| $d^2\theta/dt^2=-(g/L)\sin\theta$ | `d^2\theta/dt^2=-(g/L)\sin\theta` |

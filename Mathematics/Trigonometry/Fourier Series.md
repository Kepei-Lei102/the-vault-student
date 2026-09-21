---
chinese: 傅里叶级数 (Fùlǐyè jíshù)
prerequisites:
  - "[[Integration]]"
  - "[[Trigonometric Identities]]"
  - "[[3D Vectors and the Scalar Product]]"
leads_to:
  - "[[Fourier Transform]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - domain/analysis
  - level/university
  - type/deep
  - type/proof
  - notation/fourier-coefficients
  - misconception/fourier-is-taylor
  - misconception/gibbs-disappears
  - misconception/spectrum-without-phase
---

# Fourier Series 傅里叶级数

> A synthesiser can change its voice without changing its note. The secret is in the recipe.

## Definition

A **Fourier series** represents a periodic function using a constant plus sines and cosines whose frequencies are whole-number multiples of a base frequency. For a real function $f(t)$ with period $T>0$, put $\omega_0=2\pi/T$. Its $N$th partial sum is

$$S_N(t)=\frac{a_0}{2}+\sum_{n=1}^{N}\left[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)\right].$$

The numbers $a_n,b_n$ are the **Fourier coefficients**. They tell us how much of each component to use, with signs that encode its orientation in time. The formulas below determine them from $f$; convergence conditions determine in what sense $S_N$ recovers $f$.

**Intuition:** a vector can be described by its shadows along perpendicular axes. A periodic waveform can be described by its projections onto mutually orthogonal oscillations. The axes have become functions.

### 中文锚点

电子琴切换两种音色，弹的还是同一个音，调音器读数也一样，可一个圆润，一个带着明显的嗡鸣。传到耳边的空气并没有带着“这是什么乐器”的标签，只有一条起伏的声压曲线。只看一个稳定、重复的音，这条曲线可以由许多简单的振动叠加出来；调一调它们各自占的分量，重复的快慢可以不变，声音的模样却变了。傅里叶级数就是把这段重复的波形写成一份配方。

## Notation — keep frequency, phase and coefficient apart

| Symbol | Meaning | Check |
|---|---|---|
| $T$ | chosen period | measured in seconds if $t$ is time |
| $f_0=1/T$ | base frequency | cycles per second, hertz |
| $\omega_0=2\pi/T$ | base angular frequency | radians per second |
| $n$ | harmonic number | positive integer; frequency $nf_0$ |
| $a_0/2$ | mean or DC component | the constant offset, **not** $a_0$ |
| $a_n,b_n$ | cosine/sine coefficients | same units as the signal |
| $S_N$ | partial sum through harmonic $N$ | includes zero coefficients if present |
| $\langle f,g\rangle$ | $\frac1T\int_{t_0}^{t_0+T}f(t)g(t)\,dt$ | average product over a full period |

We use the $a_0/2$ convention. Some authors call the mean itself $a_0$; their constant-term formula therefore differs by a factor of two. Also, a chosen period need not be the *smallest* period: $\sin(2\omega_0t)$ repeats twice within $T$.

## 1. Start with the sound — one pitch, different recipes

### First example — build an A4 piano-style note

Start with **A4 = 440 Hz** in standard tuning. At each instant, add the *values* of several sine waves. The first four terms of our chosen recipe are

$$s(t)=0.24\left[\sin(2\pi\,440t)+0.65\sin(2\pi\,880t)+0.42\sin(2\pi\,1320t)+0.24\sin(2\pi\,1760t)+\cdots\right].$$

The complete twelve-harmonic recipe uses relative amplitudes $A_n=[1,.65,.42,.24,.16,.10,.07,.05,.035,.025,.018,.012]$. These are **illustrative choices, not measurements from a particular piano**. The 880 Hz component completes two cycles while the 440 Hz component completes one; their sum still repeats every $1/440$ second. Adding harmonics changes the repeating shape. Adding values simultaneously is different from playing twelve notes one after another.

![[fourier-piano-addition.svg|1000]]

*Upper left: three separate sines and their actual point-by-point sum. Upper right: 1, 4 and 12 harmonics. Lower row: the time envelopes introduced next; high components fade faster in this chosen model. The amplitude scale is shared, not individually normalised.*

**Listen to the construction, in order:**

![[fourier-piano-ladder.wav]]

1. **One sine**, 440 Hz — 3 seconds.
2. **Four harmonics**, through 1760 Hz — 3 seconds.
3. **Twelve harmonics**, through 5280 Hz — 3 seconds. More colour, but still a steady electronic tone.
4. **The same twelve with a strike and decay** — 5 seconds. The amplitudes now change with time.
5. **Piano-style refinement** — 5 seconds. Three slightly detuned, slightly inharmonic string models, each made from twelve sine components: **36 sinusoids added together**.

There are 0.65-second gaps. All stages use the same master gain; adding harmonics also changes the level, so this is not a loudness-matched comparison. Short file-edge fades prevent abrupt playback cuts.

**The crucial extra ingredient is the envelope.** Replace each constant $A_n$ by $A_nE_n(t)$, giving $s(t)=0.24\sum_n A_nE_n(t)\sin(2\pi n440t)$. Here $E_n(t)=(1-e^{-t/0.003})[0.65e^{-t/(0.18\tau_n)}+0.35e^{-t/\tau_n}]$, with $\tau_n=2.8/[1+0.18(n-1)^{1.4}]$ seconds. The first factor produces a quick attack; the two decays give a fast drop and a slower tail. Larger $n$ has smaller $\tau_n$, so the sound loses its bright upper components sooner. A steady harmonic mixture is a Fourier-series example; the evolving struck note is **additive synthesis with time-varying amplitudes**, not one fixed periodic function. [UNSW: timbre and envelope](https://www.animations.physics.unsw.edu.au/jw/timbre-envelope.htm)

![[fourier-piano-manim.mp4]]

*Watch the harmonic bars and summed waveform grow, then follow the decay envelopes while the corresponding audio plays. The final bars show amplitude per partial family, not an FFT measurement of the beating strings.*

**The final sound by itself:**

![[fourier-piano-piano.wav]]

For that last refinement, the centre frequencies are $f_n=n(440)\sqrt{(1+Bn^2)/(1+B)}$, with illustrative $B=0.00015$; each is copied at −1.2, 0 and +1.2 cents, weighted 0.25, 0.5 and 0.25. A cent is $1/100$ of an equal-tempered semitone: multiply frequency by $2^{c/1200}$. Stiff real piano strings have stretched partials, and nearby string frequencies can beat. This remains a **simplified piano-style synthesiser**: no recorded piano, soundfont, hammer noise, soundboard or pedal resonances. Those missing ingredients matter to realism. [UNSW: harmonic and inharmonic strings](https://phys.unsw.edu.au/jw/harmonics.html)

Run `python3 fourier-piano-lab.py --build` beside the source to regenerate everything except the separately rendered video. **No FFT is needed to add the waves.** As a check in the reverse direction, the script applies an FFT to one unfaded second of the steady twelve-sine mixture and recovers peaks at 440, 880, 1320, … Hz with the amplitudes we supplied. [[Fourier Transform]] explains that analysis.

### A second recipe — the square-wave family

A pure sine has one frequency. Add a little of three times that frequency, then five times it. The resulting wave still repeats after $T$, but its outline changes. That is a simple route to changing the **timbre** of a sustained note. Real instrument identity also depends on attack, decay, noise and time-varying spectra; a stationary harmonic recipe describes only the periodic part. [[Sound]] gives the listening context.

![[fourier-series-harmonics.svg|1000]]

*The pink curve adds the components whose sine coefficients appear in blue. Dashed lines mark the target square wave. These plots retain the mathematical scale: the overshoot is part of the approximation.*

### Listen before calculating

![[fourier-series-listening-ladder.wav]]

Seven three-second notes, separated by half-second gaps. The fundamental stays at **220 Hz**. The highest included harmonics are **1, 3, 5, 7, 9, 15, 31**; only odd harmonics occur. Each clip has the same steady-state RMS level, with short fades at its ends. Equal RMS does **not** guarantee equal perceived loudness, but it removes a simple gain increase as the explanation for the changing sound.

Listen for the sine's smoothness giving way to a buzz. This is a deliberately synthesised square-wave family, not a recording of seven instruments. The largest frequency is $31\times220=6820$ Hz, below the 24 kHz Nyquist limit of the 48 kHz files. [[Sound Encoding]] explains why the sample rate matters.

![[fourier-series-manim.mp4]]

*The animation follows the same harmonic recipe, then shows how projection extracts a coefficient and why a square wave keeps a small overshoot. The opening includes the RMS-matched audio; the plotted coefficients are not rescaled.*

## 2. Why these components can be separated

### The dot product has become an integral

For ordinary vectors, multiplying corresponding components and adding measures alignment. Replace the finite list by values throughout a period, and replace the sum by an integral:

$$\langle f,g\rangle=\frac1T\int_{t_0}^{t_0+T}f(t)g(t)\,dt,\qquad
\|f\|^2=\langle f,f\rangle.$$

This is the real-function inner product. A large positive average product means sustained alignment; positive and negative products can cancel. $\|f\|^2$ is the **mean square**, not the maximum height.

Set $\theta=\omega_0t$ and integrate over $-\pi\le\theta\le\pi$. The functions

$$1,\quad\cos\theta,\sin\theta,\quad\cos2\theta,\sin2\theta,\quad\ldots$$

are mutually **orthogonal**: the average product of any two different entries is zero. Their squared norms are $1$ for the constant and $1/2$ for each sine or cosine.

### Prove one case; see why the others work

*Trigger: a product of oscillations. Tool: product-to-sum from [[Trigonometric Identities]].*

$$\cos(m\theta)\cos(n\theta)=\frac12\cos((m-n)\theta)+\frac12\cos((m+n)\theta).$$

For a nonzero integer $k$,

$$\int_{-\pi}^{\pi}\cos(k\theta)\,d\theta
=\left[\frac{\sin(k\theta)}k\right]_{-\pi}^{\pi}=0.$$

If $m\ne n$, both frequencies on the right are nonzero integers, so the product integral is zero. If $m=n$, the first term becomes $1/2$; its integral is $\pi$, giving average $1/2$.

The identity $\sin m\theta\sin n\theta=\tfrac12[\cos((m-n)\theta)-\cos((m+n)\theta)]$ gives the same conclusion for sine–sine products. A sine–cosine product is odd on this symmetric interval, so its integral is zero. Each nonconstant sine or cosine also averages to zero against the constant function.

> [!warning] Orthogonal over the interval, not at every instant
> The products are usually nonzero at individual times. Their **signed integral over a full period** vanishes. Integrating over an arbitrary fragment generally loses this cancellation.

## 3. Derive the coefficient formulas

First consider a finite mixture. Multiply it by $\cos(m\omega_0t)$ and average over a period. Every other component vanishes by orthogonality, leaving

$$\langle f,\cos(m\omega_0t)\rangle
=a_m\langle\cos(m\omega_0t),\cos(m\omega_0t)\rangle=\frac{a_m}{2}.$$

Therefore the required weight is $a_m=2\langle f,\cos(m\omega_0t)\rangle$. The same operation with a sine extracts $b_m$; averaging without either extracts the constant. For a general square-integrable periodic function, **define** the coefficients by these projections:

$$\boxed{a_n=\frac2T\int_{t_0}^{t_0+T}f(t)\cos(n\omega_0t)\,dt\quad(n\ge0),}$$

$$\boxed{b_n=\frac2T\int_{t_0}^{t_0+T}f(t)\sin(n\omega_0t)\,dt\quad(n\ge1).}$$

The $n=0$ cosine is $1$, so $a_0=2\,\text{mean}(f)$. Any interval of length $T$ gives the same answer: the integrands themselves are periodic.

![[fourier-series-projection.svg|1000]]

*For $f(\theta)=\sin\theta+\tfrac12\sin3\theta$, projection onto $\sin\theta$ returns coefficient 1; projection onto $\sin2\theta$ returns 0. The shaded signed areas do the selection.*

### Why the finite approximation is the best one of its kind

Let $S_N$ use those coefficients and let $r=f-S_N$ be its residual. The coefficient equations say $r$ is orthogonal to every component used in $S_N$.

Any other trigonometric mixture through harmonic $N$ can be written $q=S_N+h$, with $h$ built from the same components. Then

$$\|f-q\|^2=\|r-h\|^2
=\|r\|^2-2\langle r,h\rangle+\|h\|^2
=\|r\|^2+\|h\|^2\ge\|r\|^2.$$

So $S_N$ minimises **mean-square error** among all mixtures through harmonic $N$. Adding a nonzero correction in the allowed directions makes that error larger. This proves a precise best-approximation claim without assuming that the infinite series converges pointwise.

## 4. Let symmetry remove work

Use the interval $[-T/2,T/2]$, with the symmetry centred at the chosen time origin.

- **Even $f$:** $f(-t)=f(t)$. Multiplying by an odd sine gives an odd integrand, so every $b_n=0$. Only cosine terms and the mean remain.
- **Odd $f$:** $f(-t)=-f(t)$. Its mean and all cosine coefficients vanish. Only sine terms remain.
- **Half-wave antisymmetry:** $f(t+T/2)=-f(t)$. The contributions from the two halves cancel for even $n$, so only odd harmonics survive. This condition does **not** imply that the function is odd about $t=0$.

For the last rule, shifting a sine or cosine by $n\pi$ multiplies it by $(-1)^n$. Pair points separated by $T/2$ in the coefficient integral: their combined multiplier is $1-(-1)^n$, zero for even $n$.

## 5. Worked example — build a square wave from its coefficients

This is an original mathematical example. Define the $2\pi$-periodic function

$$f(\theta)=\begin{cases}-1,&-\pi<\theta<0,\\1,&0<\theta<\pi.\end{cases}$$

At the jumps we may assign the midpoint value 0. Changing finitely many point values does not change any coefficient integral.

**Step 1 — recognise the symmetry.** *Trigger: equal positive and negative halves. Tool: oddness.* The mean and all $a_n$ vanish. Since $f\sin(n\theta)$ is even,

$$b_n=\frac2\pi\int_0^\pi\sin(n\theta)\,d\theta
=\frac{2}{\pi n}[1-\cos(n\pi)]
=\begin{cases}\dfrac4{\pi n},&n\text{ odd},\\0,&n\text{ even}.\end{cases}$$

**Step 2 — assemble the surviving directions.** *Tool: the Fourier partial sum.*

$$S_N(\theta)=\frac4\pi\sum_{\substack{1\le n\le N\\n\ \mathrm{odd}}}\frac{\sin(n\theta)}n.$$

The first three nonzero terms are $\frac4\pi(\sin\theta+\frac13\sin3\theta+\frac15\sin5\theta)$. “Three terms” here means highest harmonic **5**, not highest harmonic 3.

**Step 3 — predict the discontinuity.** Every term is zero at $\theta=0$, so every $S_N(0)=0$. No number of terms makes the series equal to an arbitrarily assigned value 1 at that single jump. This is a feature of convergence, not a failed integral.

### A smoother relative — the triangle wave

Let $g(\theta)=2\theta/\pi$ on $[-\pi/2,\pi/2]$, continue linearly down to 0 at $\pi$, and extend oddly and periodically. It has peaks $\pm1$ and no jump in value.

*Trigger: oddness plus a piecewise linear graph. Tools: symmetry and integration by parts.* On $[0,\pi]$, symmetry about $\pi/2$ doubles the half-interval integral for odd $n$ and cancels it for even $n$. For odd $n$,

$$b_n=\frac8{\pi^2}\int_0^{\pi/2}\theta\sin(n\theta)\,d\theta
=\frac8{\pi^2}\left[-\frac{\theta\cos(n\theta)}n+\frac{\sin(n\theta)}{n^2}\right]_0^{\pi/2}
=\frac8{\pi^2}\frac{(-1)^{(n-1)/2}}{n^2}.$$

Thus the triangle uses alternating odd harmonics decaying as $1/n^2$, whereas the square uses odd harmonics decaying as $1/n$. Sharper edges demand stronger high-frequency content. Smoothness across the **periodic seam** matters too: periodically repeating a ramp creates a jump even if the ramp is smooth inside the interval.

## 6. What does “the series equals the function” mean?

For a periodic function that is piecewise continuously differentiable with finitely many pieces and finite one-sided limits, the Fourier partial sums satisfy

$$\lim_{N\to\infty}S_N(t)=\frac{f(t^-)+f(t^+)}2.$$

At a continuity point this is $f(t)$. At a jump it is the average of the two one-sided limits, including where the chosen period wraps around. This is a convergence theorem; orthogonality alone did not prove it. [NIST DLMF, convergence of Fourier series](https://dlmf.nist.gov/1.8.ii)

Another meaning is **mean-square convergence**: $\|f-S_N\|^2\to0$. This holds for square-integrable periodic functions because the trigonometric system is complete in that function space. Completeness is the additional theorem needed to pass from the finite projection result to an infinite reconstruction; it is not a consequence of perpendicularity alone.

These are different promises. An error can become concentrated in a narrower region while its tallest point remains substantial. That is exactly the next phenomenon.

### Gibbs: the ringing gets narrower, but its relative height stays

![[fourier-series-gibbs.svg|1000]]

Near a jump of height $J$, ordinary Fourier partial sums approach an overshoot of about **$0.08949J$** above the higher side (and a corresponding undershoot below the lower side). For our jump from $-1$ to $1$, $J=2$: the upper peak approaches **1.17898**, not 1.08949. The conspicuous peak moves towards the jump as more terms are added. [NIST DLMF, Gibbs phenomenon](https://dlmf.nist.gov/6.16)

**Why that persistent peak?** Put $N=2M-1$. Differentiate this *finite* sum:

$$S'_{2M-1}(\theta)=\frac4\pi\sum_{k=0}^{M-1}\cos((2k+1)\theta)
=\frac2\pi\frac{\sin(2M\theta)}{\sin\theta}.$$

For the last equality, multiply the cosine sum by $2\sin\theta$: the terms $\sin((2k+2)\theta)-\sin(2k\theta)$ telescope. The first positive peak is at $\theta=\pi/(2M)$. Since $S_{2M-1}(0)=0$, substitute $u=2M\theta$ in the integral of the derivative:

$$S_{2M-1}\left(\frac\pi{2M}\right)
=\frac2\pi\int_0^\pi\frac{\sin u}{2M\sin(u/(2M))}\,du
\longrightarrow\frac2\pi\int_0^\pi\frac{\sin u}{u}\,du\approx1.17898.$$

The denominator tends to $u$; the ratio at $u=0$ is interpreted by its limit. The peak's **location** tends to zero while its **height** tends to a number greater than one. Pointwise convergence away from the jump and this moving overshoot can therefore both be true.

> [!info] Can ringing be reduced?
> Yes, by changing the approximation. Averaging the first $N+1$ partial sums gives the **Fejér mean**, which tapers harmonic $n$ by $1-n/(N+1)$. This smooths the sharp cutoff and removes the persistent Gibbs overshoot for this square wave, at the cost of a broader transition. It is a different weighted approximation from $S_N$, so it does not contradict the peak calculation.

## 7. Parseval — Pythagoras for a waveform

Recall that $\|f\|^2$ is its mean square. Distinct harmonics have zero average cross-product. Squaring a *finite* sum and averaging therefore gives

$$\|S_N\|^2=\frac{a_0^2}{4}+\frac12\sum_{n=1}^N(a_n^2+b_n^2).$$

Because $f-S_N$ is orthogonal to $S_N$, the same Pythagorean calculation gives

$$\|f\|^2=\|S_N\|^2+\|f-S_N\|^2.$$

Now use mean-square convergence to let the residual tend to zero:

$$\boxed{\frac1T\int_{t_0}^{t_0+T}f(t)^2\,dt
=\frac{a_0^2}{4}+\frac12\sum_{n=1}^\infty(a_n^2+b_n^2).}$$

That is **Parseval's identity**. It is also why harmonic amplitudes cannot simply be added to obtain an RMS level: their **squared** contributions add. [NIST DLMF, Parseval's formula](https://dlmf.nist.gov/1.8.i)

### Worked example — how much of the square wave have we recovered?

*Trigger: a question about total signal level or approximation error. Tool: Parseval.* Since the square wave has $f^2=1$ except at isolated points, its mean square is 1. Its odd sine coefficients give

$$1=\frac8{\pi^2}\sum_{n\ \mathrm{odd}}\frac1{n^2}.$$

The fundamental alone captures $8/\pi^2\approx0.81057$ of the mean square. Through harmonic 3, the fraction is $(8/\pi^2)(1+1/9)\approx0.90063$. The omitted fraction is exactly the mean-square approximation error, **not** a pointwise error bound.

| Highest harmonic $N$ | Captured mean square | Residual mean square |
|---|---|---|
| 1 | 0.81057 | 0.18943 |
| 3 | 0.90063 | 0.09937 |
| 7 | 0.94960 | 0.05040 |
| 31 | 0.98734 | 0.01266 |

For a voltage $v(t)$ across a fixed resistor $R$, average electrical power is $\langle v^2\rangle/R$. Parseval then literally accounts for the power harmonic by harmonic. For an arbitrary plotted function, “energy” needs a physical model; mean square by itself has the units of $f^2$.

## 8. Phase is part of the recipe

A cosine/sine pair can be written

$$a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)
=A_n\cos(n\omega_0t-\phi_n),$$

where $A_n=\sqrt{a_n^2+b_n^2}$ and $\phi_n=\operatorname{atan2}(b_n,a_n)$. Expand the cosine of a difference to check: $a_n=A_n\cos\phi_n$, $b_n=A_n\sin\phi_n$. If $A_n=0$, its phase is immaterial.

![[fourier-series-phase.svg|1000]]

*These waves share all harmonic magnitudes and the same mean square, yet have different shapes. A magnitude-only spectrum omits phase. The diagram does not assert that every phase change is equally audible.*

A time delay $\tau$ changes **every** harmonic phase in a coordinated way: in the displayed cosine convention, $\phi_n\mapsto\phi_n+n\omega_0\tau$. Changing only one harmonic's phase usually changes the shape rather than merely sliding the whole signal.

### Complex notation — one formula for both quadratures

Use [[Euler's Formula and De Moivre's Theorem]] to replace sine and cosine by exponentials:

$$f(t)\sim\sum_{n=-\infty}^{\infty}c_ne^{in\omega_0t},\qquad
c_n=\frac1T\int_{t_0}^{t_0+T}f(t)e^{-in\omega_0t}\,dt.$$

For a real signal, $c_0=a_0/2$, $c_n=(a_n-ib_n)/2$ for $n>0$, and $c_{-n}=\overline{c_n}$. The negative-frequency term pairs with the positive one to produce a real oscillation. It is not a second physical instrument playing backwards.

## 9. Where the calculation earns its keep

### Synthesiser, equaliser and electrical distortion

**Additive synthesis** constructs a steady tone by choosing harmonic amplitudes and phases. The embedded WAVs do precisely that. An ideal linear, time-invariant filter changes each sinusoidal component's amplitude and phase according to its frequency response; recombining predicts the output. A real recording with changing notes needs a time-dependent analysis rather than one fixed periodic recipe.

**Nonlinearity creates harmonics.** Feed $x(t)=\sin(\omega t)$ through the cubic model $y=x-\alpha x^3$. Since $\sin^3u=(3\sin u-\sin3u)/4$,

$$y(t)=\left(1-\frac{3\alpha}{4}\right)\sin\omega t+\frac\alpha4\sin3\omega t.$$

The third harmonic was absent at the input. This calculation explains a simple form of saturation-like distortion and the growth of harmonic content in a nonlinear amplifier. It is a toy static model, not a full valve or loudspeaker simulation.

### Heat flow — the original kind of problem

Suppose a rod of length $L$ has its ends held at zero temperature relative to the surroundings. The diffusion model is $u_t=\kappa u_{xx}$. A sine component obeying those endpoint conditions evolves as

$$u_n(x,t)=B_n\sin\left(\frac{n\pi x}{L}\right)
\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2t\right].$$

Differentiate once in time and twice in space to verify the equation. Both ends are zero because $\sin0=\sin(n\pi)=0$. Expand the initial temperature profile in these sine modes—equivalently use an odd extension with period $2L$—and evolve each separately. Fine spatial detail has large $n$ and dies faster, which is why heat smooths sharp temperature differences. The coefficients turn a complicated starting shape into separately solvable pieces. [MIT, Fourier series and heat-equation examples](https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-fall-2008/f1da5a16ff5dfd980ef4dfeb46bd76b7_cse41.pdf)

## 10. Try it — predict, then change the recipe

`fourier-series-lab.py` computes the sums directly and checks them against independent quadrature and sampled mean squares. Run with `--audio` to regenerate the WAVs. NumPy and SciPy are required.

```python
import numpy as np

theta = np.linspace(-np.pi, np.pi, 8192, endpoint=False)
N = 15
s = sum(4 / (np.pi * n) * np.sin(n * theta)
        for n in range(1, N + 1, 2))
print("value at the jump:", s[len(theta) // 2])
print("predicted mean-square error:",
      1 - 8 / np.pi**2 * sum(1 / n**2 for n in range(1, N + 1, 2)))
```

- Change $N$ to 31: predict what happens to the error integral **and** the highest peak. They need not move together.
- Replace $1/n$ by the triangle's alternating $1/n^2$ weights. Predict the loss of the sharp edge before plotting.
- Add a constant 0.3. Which coefficient changes? Only $a_0$, by 0.6 in this convention.
- Shift the time origin. Check that amplitudes remain the same while phases change together.
- If increasing audio frequency or harmonic count, keep every generated component below half the sample rate. Sampling a discontinuous ideal square wave directly is not the same as synthesising a deliberately band-limited partial sum.

## Common misconceptions

1. **“This is a Taylor series in disguise.”** Taylor uses powers of distance from a point and derivatives there. Fourier uses periodic oscillations and integrals over a whole period. A jump can have a useful Fourier representation without having a Taylor expansion across the jump.
2. **“Every function equals its Fourier series everywhere.”** State the function class and the kind of convergence. A finite change at one point does not change the integrals.
3. **“More terms remove every visible overshoot.”** Mean-square error shrinks; the moving Gibbs peak has a nonzero limiting relative height.
4. **“Odd harmonics mean an odd function.”** Half-wave antisymmetry removes even harmonics; oddness about the origin removes cosine terms. They are different symmetries.
5. **“The spectrum tells the whole story.”** Magnitudes alone lose phase. Even a complete fixed harmonic recipe does not capture an arbitrary evolving sound.
6. **“Fourier series and the FFT are the same.”** A Fourier series expands a periodic function; a discrete Fourier transform acts on a finite sample vector; an FFT is an efficient algorithm for that discrete transform. Their relationship is developed through [[Fourier Transform]].

## Exam Notes

### Cambridge and OxfordAQA

**Fourier-series coefficients, convergence, Gibbs and Parseval are enrichment**, not named required topics in the inspected Cambridge 0580, 0606, 9709 or 9231 syllabuses, nor OxfordAQA 9260 or 9660. Trigonometric identities, integration by parts and series supply reusable tools, but a syllabus that requires a Maclaurin expansion does not thereby require Fourier series.

### Edexcel IAL, IB Mathematics and AP Calculus

The inspected **Edexcel IAL Mathematics/Further Mathematics** specification, **IB AA / AI first-assessment-2021 guides**, and **AP Calculus AB / BC** course framework do not prescribe Fourier series. Their power-series, trigonometric and calculus topics do not justify assigning this whole treatment to an exam row. All worked examples above are original teaching examples, not attributed past-paper questions. No formula-sheet allowance is claimed for these Fourier formulas.

### Physics and computer-science connections

The prescribed harmonics in [[Stationary Waves]] and sampling in [[Sound Encoding]] motivate the mathematics. Those links do not make calculation of Fourier coefficients a Cambridge 0625/9702 or 0478/9618 requirement. Keep the periodic-signal mathematics distinct from each board's actual wave and data-representation outcomes.

## Beyond syllabus — from repeated patterns to arbitrary recordings

Recall that a periodic signal has frequency spacing $f_0=1/T$. Increasing the period makes those frequency lines closer together; with the appropriate scaling and limiting hypotheses, the continuous-frequency description becomes a [[Fourier Transform]]. A finite digital recording instead leads to a **DFT**, whose basis consists of roots of unity. The FFT exploits that structure; a spectrogram applies short analyses as a window moves through time.

Those developments inherit the projection idea. They also introduce new questions—finite windows, leakage, frequency resolution and convolution—that a picture of one repeated square wave cannot settle.

## Sources

- [NIST DLMF §1.8](https://dlmf.nist.gov/1.8): normalization, complex coefficients, convergence and Parseval.
- [NIST DLMF §6.16](https://dlmf.nist.gov/6.16): the sine-integral limit behind Gibbs overshoot.
- [MIT OCW, Fourier series for periodic functions](https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-fall-2008/f1da5a16ff5dfd980ef4dfeb46bd76b7_cse41.pdf): square/triangle expansions and the heat-equation connection.

## Connections

- **Prerequisites:** [[Integration]], [[Trigonometric Identities]], [[3D Vectors and the Scalar Product]] — averaging, product-to-sum and projection.
- **Another notation:** [[Euler's Formula and De Moivre's Theorem]] — complex exponentials combine sine and cosine.
- **Hear the shapes:** [[Sound]], [[Stationary Waves]], [[Sound Encoding]] — timbre, normal modes and discrete samples.
- **Physical applications:** [[Heat Transfer]], [[Alternating Current]] — diffusion and RMS power.
- **Next mathematical step:** [[Fourier Transform]] — continuous frequencies and discrete transforms.
- **Different kind of series:** [[Maclaurin Series]] — local power expansions rather than global periodic coordinates.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $\omega_0=2\pi/T$ | `\omega_0=2\pi/T` | base angular frequency |
| $S_N$ | `S_N` | partial sum |
| $\langle f,g\rangle$ | `\langle f,g\rangle` | inner product |
| $\|f\|^2$ | `\|f\|^2` | mean square under the chosen normalization |
| $c_{-n}=\overline{c_n}$ | `c_{-n}=\overline{c_n}` | conjugate symmetry for real signals |

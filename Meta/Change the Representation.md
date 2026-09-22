---
chinese: 换一种表示 (huàn yī zhǒng biǎoshì)
prerequisites:
  - "[[Chain of Thought]]"
leads_to: []
teach_together:
  - "[[When a Model Breaks]]"
tags:
  - subject/methodology
  - domain/problem-solving
  - domain/representation
  - level/life
  - level/university
  - type/meta
  - type/methodology
  - type/cross-domain
  - misconception/same-information-means-same-difficulty
  - misconception/transform-means-discard
  - misconception/simpler-form-is-always-better
---

# Change the Representation 换一种表示

> Calculate $99\times101$.
>
> Now calculate $100^2-1$.
>
> Your arithmetic did not improve between the two sentences. The work changed because the description changed.

## The move

A **representation** is a way of expressing an object or situation so that we can work with it: digits, a diagram, coordinates, an equation, a table, a data structure.

An **exact change of representation** preserves the information we claim to keep, while changing which relationships and operations are easy to see. It can reveal a shortcut without making a new assumption about the world.

The useful question is:

> **What operation am I trying to perform, and in which representation is that operation simple?**

There is no universally best representation. A list is good for replaying an order; a tally is good for counting. A waveform is good for locating a click; a spectrum is good for locating a steady hum. Choosing well starts with the task.

### 中文锚点

班里要一起点奶茶，群里的消息一条接一条：“两杯原味”“一杯芋泥”“再加一杯原味”。要给店员报数量，你不会把聊天记录从头念一遍，而是先按口味记一张数量表。大家点的东西没变，换个记法，要算的总数就显出来了。不过，数量表没记谁点了什么，分奶茶时还得回去看原消息。换一种表示，就是先想清楚自己要做什么，再把有用的关系摆到眼前；省下的麻烦，不能靠悄悄丢掉待会儿还要用的信息来换。

## 1. Same object, different questions

Consider one polynomial:

$$f(x)=x^2-6x+5=(x-1)(x-5)=(x-3)^2-4.$$

| Question | Useful form | What becomes visible |
|---|---|---|
| Where is $f(x)=0$? | $(x-1)(x-5)$ | One factor must vanish: $x=1$ or $5$ |
| What is the smallest value? | $(x-3)^2-4$ | A real square is nonnegative: minimum $-4$ at $x=3$ |
| What is the coefficient of $x$? | $x^2-6x+5$ | Read off $-6$ |

The three expressions agree for **every real $x$**. Factoring did not change the roots; completing the square did not move the minimum. Each makes a different property cheap to extract.

**Worked opening — trigger: equal offsets from a round number. Tool: difference of squares.**

$$99\times101=(100-1)(100+1)=100^2-1^2=9999.$$

Expanding $(a-b)(a+b)$ gives $a^2+ab-ab-b^2$. The cross terms cancel. That cancellation is the mechanism; “spot the trick” is not an explanation.

An unhelpful change can go the other way. Expanding $(x-1)(x-5)=0$ hides two visible roots behind another quadratic to solve. More symbols do not mean more understanding; fewer symbols do not guarantee it either.

[[Factorising (Vocab)]] and [[Completing the Square]] develop the algebra. The transferable skill is choosing the form **from the property you need**.

## 2. Why equivalent information can require different work

Imagine two descriptions of a small transport network:

- A paragraph lists each station and its connections.
- A diagram places each station once and draws the same connections.

Both may encode the same network. In the paragraph, following a route requires finding the next station's entry repeatedly. In the diagram, your eyes can follow a line. The connections have been arranged to support the operation.

But if your task is to find every station whose name begins with M, an alphabetical list may beat the diagram. If you need walking distance, a schematic connection diagram may not contain it at all.

Larkin and Simon's analysis distinguishes information preserved from the work needed to use it: a diagram can reduce search and make relevant relationships locally available. The benefit depends on the task and the operations the reader can perform. It is not a promise that every diagram helps every learner. [Larkin & Simon, 1987](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1551-6708.1987.tb00863.x)

A good representation often does one of three things:

1. **Groups what must be used together.** A tally puts all identical orders under one count.
2. **Makes a relation explicit.** A factored expression exposes the zero-product rule.
3. **Separates what was mixed together.** Normal coordinates expose independent motions.

The arrangement performs some of the organisational work once, so we do not have to repeat it at every step.

## 3. The round trip is part of the method

Let $x$ describe the original state. A transformation $T$ produces a new description $z=T(x)$. If $T$ is invertible on the allowed states, $T^{-1}$ reconstructs $x$.

Suppose $F$ is the operation we wanted to perform. In the new description, the corresponding operation is

$$G=T\circ F\circ T^{-1}.$$

The rightmost operation happens first: decode a new description, apply the old operation, then encode the result. If that whole combination simplifies, we can implement $G$ directly. Returning to the original description gives

$$\boxed{F(x)=T^{-1}\bigl(G(T(x))\bigr).}$$

![[representation-round-trip.svg|900]]

*Both routes must give the same output. The lower route earns its place only when its total work, including translation, suits the task.*

This equation is a specification, not an automatic speed-up. Choosing an arbitrary $T$ may make $G$ worse. The art is finding a description in which the operation loses its troublesome interactions.

For a number written in binary, the number survives but some operations look different. For a polynomial in factored form, the function survives but some questions become easier. **Say what stays invariant before celebrating what became simpler.**

### The domain travels with the translation

If you substitute $u=x^2$ to solve

$$x^4-5x^2+4=0,$$

you obtain $(u-1)(u-4)=0$, hence $u=1$ or $4$. But $u=x^2$ is not one-to-one over the reals: each positive $u$ has two preimages. Returning gives **four** solutions, $x=\pm1,\pm2$.

The simpler equation did not license forgetting the return journey. Over real $x$, $u$ also cannot be negative. [[Substitution Equations]] develops this pattern.

Likewise,

$$\frac{x^2-1}{x-1}=x+1\qquad\text{only for }x\ne1.$$

The restriction is part of the information. Removing it changes the function's domain, even though the algebra looks cleaner.

## 4. Worked example — let the symmetry choose the coordinates

Two identical masses, each of mass $m$, sit between identical outer springs of stiffness $k$, joined by a spring of stiffness $\kappa$. Displacements $x_1,x_2$ are measured in the same direction from equilibrium. For ideal linear springs,

$$m\frac{d^2x_1}{dt^2}=-kx_1+\kappa(x_2-x_1),$$

$$m\frac{d^2x_2}{dt^2}=-kx_2-\kappa(x_2-x_1).$$

Each equation refers to the other mass. Tracking either displacement alone leaves the interaction in the way.

**Step 1 — trigger: identical parts and equal-and-opposite coupling terms. Tool: sum and difference.**

$$q_+=\frac{x_1+x_2}{2},\qquad q_-=\frac{x_1-x_2}{2}.$$

$q_+$ measures their shared displacement; $q_-$ measures half their separation change, with the chosen sign. Keeping both preserves the two original displacements:

$$x_1=q_++q_-,\qquad x_2=q_+-q_-.$$

**Step 2 — trigger: the coupling terms cancel in the sum. Tool: add the force equations.**

$$\frac{d^2q_+}{dt^2}=-\frac{k}{m}q_+.$$

**Step 3 — trigger: the coupling terms reinforce in the difference. Tool: subtract the second equation from the first.**

$$\frac{d^2q_-}{dt^2}=-\frac{k+2\kappa}{m}q_-.$$

Now each coordinate has its own equation. The physical connecting spring is still present. We have **separated the equations**, not disconnected the apparatus.

**Step 4 — trigger: each acceleration is proportional to minus its own coordinate. Tool: simple harmonic motion, then reconstruction.**

For $m=1\ \mathrm{kg}$, $k=1\ \mathrm{N\,m^{-1}}$, $\kappa=1.5\ \mathrm{N\,m^{-1}}$, the angular frequencies are $1$ and $2\ \mathrm{rad\,s^{-1}}$. Release the first mass from $0.10\ \mathrm m$, with the second at equilibrium and both initially at rest. Both $q$ coordinates start at $0.05\ \mathrm m$, so, using numerical $t$ in seconds,

$$q_+(t)=0.05\cos t,\qquad q_-(t)=0.05\cos2t,$$

$$x_1(t)=0.05(\cos t+\cos2t),\qquad
x_2(t)=0.05(\cos t-\cos2t).$$

At $t=0$, these return the stated initial displacements and zero velocities. Substituting their second derivatives into the original equations checks that the translation solved the original problem.

The reusable trigger is **exchange symmetry**, not “always add and subtract”. Unequal masses or different outer springs generally require different weighted combinations. Generic nonlinear forces need not separate this way at all. [[Coupled Oscillators]] supplies the mechanical derivation, energy exchange and limitations.

## 5. Sound — choose components that the operation treats simply

A recording can be described by sample values over time or by its complex Fourier coefficients. A complete finite discrete Fourier transform (DFT) is invertible: the coefficients encode the same sample vector, apart from numerical round-off in computation.

An FFT is an efficient algorithm for computing that transform. It is **not** the act of throwing away frequencies. Compression or filtering can discard information *after* the change of representation.

Why choose this particular representation? For a linear, time-invariant system, shifting the input shifts the response and adding inputs adds their responses. A complex sinusoid passes through with the same frequency, scaled by a complex factor. Frequencies therefore provide components the system can treat independently.

A room's echoes illustrate the task. In time, each input sample creates delayed, scaled copies, all of which must be added. This is **convolution**. In frequency, the same linear operation becomes multiplication:

$$Y(f)=H(f)X(f).$$

Here $X$ describes the input, $H$ the system's frequency response, and $Y$ the output. [[Fourier Transform#8. Convolution — how a room answers every sample]] derives the continuous version. [[Digital Audio Workstation]] supplies the production context.

### A tiny round-trip calculation

**Trigger: a sum of delayed copies. Tool: convolution, then the DFT comparison.**

Take $x=[1,2,0,0]$ and $h=[1,\tfrac12,0,0]$. One direct arrival plus a half-strength one-sample echo gives

$$y_n=x_n+\tfrac12x_{n-1},\qquad y=[1,2.5,1,0],$$

where values outside the original signal are zero. With the forward convention using $e^{-2\pi i kn/N}$, their four-point DFTs are

$$X=[3,1-2i,-1,1+2i],\qquad
H=[1.5,1-0.5i,0.5,1+0.5i].$$

Multiply corresponding entries:

$$Y=[4.5,-2.5i,-0.5,2.5i].$$

The inverse DFT returns $[1,2.5,1,0]$. The attached Python lab checks both routes independently.

**A boundary condition matters:** multiplying length-$N$ DFTs gives **circular** convolution, which wraps around. For ordinary linear convolution of sequences of lengths $L$ and $M$, pad to at least $L+M-1$ before transforming. Here the nonzero sequences have length 2 each, and length 4 is sufficient. Without the padding rule, “same operation” can quietly become false.

For four numbers, direct calculation is easier. For long filters, FFT-based convolution can pay for the translations; latency, block size and the actual workload still matter. A practical equaliser need not use an FFT. [NumPy DFT reference](https://numpy.org/doc/stable/reference/routines.fft.html)

### Phase is information

Keeping only $|X_k|$ is a different operation. A shifted pulse has the same magnitude spectrum as the original pulse, but arrives at a different time. If timing matters, magnitudes alone cannot reconstruct the answer.

A complete transform changes description. A magnitude plot answers a narrower question. Both are useful; confusing them causes errors.

## 6. Sometimes you should discard information — deliberately

Recall that the round-trip formula assumed an invertible transformation. A summary need not be invertible to answer a particular question exactly.

A tea-order tally loses who ordered each cup and the order of messages. Yet it retains everything needed to ask “How many taro teas?” If $T$ is the tally and $Q$ that question, there is a function $g$ such that

$$Q(x)=g(T(x)).$$

We cannot reconstruct $x$, but we can reconstruct the answer to $Q$.

**A useful impossibility test:** if two originals produce the same summary but require different answers, the summary cannot answer that question reliably by itself. Whatever a program does with that one summary, it must produce the same output for both originals. At least one answer must then be wrong.

For example, reversing two people's order messages can preserve every flavour count while changing who ordered first. No clever calculation on the counts can recover the first person.

```python
from collections import Counter

orders = ["original", "taro", "original", "mango"]
counts = Counter(orders)
assert counts["original"] == 2
other = ["original", "taro", "mango", "original"]
assert list(Counter(other).items()) == list(counts.items())
assert orders[-1] != other[-1]
```

`Counter` retains counts and first-encounter key order in Python, but not the complete input sequence. The example preserves even the order of the stored keys, yet changes the last drink ordered. The complete sequence still cannot be recovered. [Python documentation](https://docs.python.org/3/library/collections.html#collections.Counter)

This gives a precise reason to keep raw measurements beside a summary, or original audio beside an exported mix: tomorrow's question may need a distinction today's representation removed.

## 7. Choose from the obstacle

Start by naming the relationship that keeps making the current solution awkward.

| Obstacle you can point to | Candidate change | What to check before trusting it |
|---|---|---|
| Products hide zeros | Factor the expression | Expand back; preserve the domain |
| A repeated expression obscures structure | Substitute a new variable | Allowed values and all inverse branches |
| Identical interacting parts appear symmetrically | Sum/difference or normal coordinates | Invertibility and actual equation separation |
| Repeated shifted copies must be added | Fourier representation | Linearity, time invariance, padding, phase |
| Repeated “how many of each?” searches | Frequency table / tally | Whether order or identity is needed later |
| Angles keep accumulating through rotations | Complex polar form | Angle convention; lengths and units |

For the last row, $e^{i\alpha}e^{i\beta}=e^{i(\alpha+\beta)}$: composing rotations becomes adding angles. Cartesian components remain useful when the task is adding displacement arrows. [[Euler's Formula and De Moivre's Theorem]] explains the connection. **A convenient representation for multiplication need not be convenient for addition.**

When no promising structure appears, sketch a tiny case, write a table, or solve a simpler instance. Those are experiments to discover a relationship, not rituals to perform on every problem. [[Chain of Thought]] places these moves inside a larger problem-solving process.

## 8. Count the translation cost

Suppose a repeated task costs $c$ units of work each time in the original form, $d$ in the new form, and conversion costs $C$ once. After $n$ uses, compare

$$nc\quad\text{with}\quad C+nd.$$

When $c>d$, conversion pays on this simplified accounting if $n>C/(c-d)$. Include reconstruction, storage and updating costs where the task requires them. These are comparable work units, not a universal wall-clock prediction.

For a one-off question about a short list, building an index may cost more than reading it. For thousands of lookups over unchanged data, the index can earn its construction cost. A changing dataset makes maintenance part of the bill. [[Hash Tables]] and [[Balanced Trees]] show real data structures built around such choices.

Human work has conversion costs too. A notation you cannot yet read can hide an insight that is obvious in a familiar diagram. Learning the notation may still be a good investment because many later tasks reuse it.

**Worked decision — trigger: repeated use of unchanged data. Tool: break-even comparison.** If conversion costs 60 work units, each old lookup costs 10 and each new lookup costs 2, then $60+2n<10n$ requires $n>7.5$. The eighth lookup is the first to make the new route cheaper under these assumptions.

## 9. Where this earns its keep

**A shop preparing orders.** A message log records who asked for what. A grouped tally supports batch preparation; a per-person order view supports handing the drinks out. Keeping both views connected avoids asking one summary to do a job it cannot do.

**A music producer adding a room.** Convolution applies a measured impulse response to a dry signal. Frequency-domain multiplication can make long reverberation filters practical. The underlying linear model stays the same; changing the room model or adding nonlinear distortion is a separate decision.

**An engineer studying vibration.** Mode coordinates separate linear motions that are coupled in physical displacement coordinates. The engineer returns to actual displacements to check whether a component moves too far. The convenient coordinates are a means of answering a physical question.

**A programmer checking an answer.** Solve in one representation, check in another: expand a proposed factorisation, reconstruct transformed data, or compare direct convolution with transformed multiplication. The second route is valuable when its likely mistakes differ from the first route's. [[Learning as Verification]] develops that discipline.

## 10. Hands-on — make the two routes disagree when they should

Run the standard-library program beside this note:

```bash
python3 representation-lab.py
```

It compares direct and transformed convolution, checks the oscillator equations from reconstructed motions, and demonstrates what a magnitude spectrum loses.

Before running it, predict:

1. Does increasing the FFT length change the desired *linear* convolution once there is enough padding? The result's support should agree; extra entries should be zero up to round-off.
2. What happens when a three-sample signal and a three-sample filter are transformed at length 3? The five-sample linear result wraps into three places. This is a different boundary condition, not random numerical error.
3. Can a full complex DFT distinguish pulses at different sample positions? Yes. Can magnitudes alone? No.
4. If you keep only $q_+$, can you reconstruct both masses? No: you discarded their relative displacement.

For an everyday version, take five order messages and make a tally. Write one question the tally answers exactly and one it cannot answer. Exhibit two message lists with the same tally but different answers to the second question. That pair is stronger evidence than saying “some detail is lost”.

## 11. Common wrong turns

- **“If it is the same information, it cannot make the problem easier.”** Information content and the work needed to access a relation are different. Factoring exposes zeros without inventing them.
- **“A transform is compression.”** A complete DFT is invertible; truncating coefficients is a further, generally lossy step.
- **“The diagram proves the claim.”** A diagram can suggest the right relation. Exact labels, assumptions and reasoning still have to establish it.
- **“I found one solution in the new variable, so I found one original solution.”** An inverse can have several branches or none in the allowed domain.
- **“My equations separated, so the objects no longer interact.”** Coordinate independence is a property of the description and equations. The connecting spring did not disappear.
- **“A prettier description repairs a bad model.”** Rewriting a constant-speed journey in different units cannot introduce waiting at traffic lights. [[When a Model Breaks]] addresses changing the model itself.

## Take it with you

When stuck, complete three sentences:

> **The operation that is awkward is ___.**
>
> **In this new description, it becomes ___ because ___.**
>
> **I know I have answered the original question because ___.**

If the second blank is only “it looks nicer”, keep looking. If the third is empty, the solution has not returned home yet.

## Connections

- **Parent:** [[Chain of Thought]] — selecting a move from a recognisable trigger.
- **Peer:** [[When a Model Breaks]] — changing assumptions versus changing the description of the same model.
- **Algebra:** [[Factorising (Vocab)]], [[Completing the Square]], [[Substitution Equations]] — form selected by the question, with a return path.
- **Mechanisms:** [[Coupled Oscillators]], [[Fourier Transform]], [[Euler's Formula and De Moivre's Theorem]] — components in which an operation simplifies.
- **Information:** [[Compression Is Intelligence]] — compact descriptions, reconstruction and what is preserved.
- **Verification:** [[Learning as Verification]] — a different representation as an independent check.

## Sources

- [Larkin & Simon (1987), Why a Diagram is (Sometimes) Worth Ten Thousand Words](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1551-6708.1987.tb00863.x): distinction between equivalent information and the computational work supported by a representation. The examples and calculations here are independently constructed.
- [NumPy — Discrete Fourier Transform](https://numpy.org/doc/stable/reference/routines.fft.html): transform conventions, inverse, magnitude and phase, and convolution use.
- [Python — collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter): counting semantics and insertion-order qualification.

## LaTeX Reference

| Expression | Source | Meaning |
|---|---|---|
| $T^{-1}$ | `T^{-1}` | Inverse transformation on the allowed domain |
| $G=T\circ F\circ T^{-1}$ | `G=T\circ F\circ T^{-1}` | Operation expressed in new coordinates |
| $q_\pm=(x_1\pm x_2)/2$ | `q_\pm=(x_1\pm x_2)/2` | Shared and relative coordinates |
| $Y(f)=H(f)X(f)$ | `Y(f)=H(f)X(f)` | Convolution represented as multiplication |
| $Q(x)=g(T(x))$ | `Q(x)=g(T(x))` | A summary retains enough for this question |

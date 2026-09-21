---
chinese: 有效数字 (yǒuxiào shùzì)
prerequisites:
  - "[[Rounding (Vocab)]]"
  - "[[Accuracy vs Precision]]"
  - "[[Error Propagation]]"
  - "[[Physical Quantities and Units]]"
  - "[[Calibration of Instruments]]"
leads_to:
  - "[[Linearisation for Lab Analysis]]"
  - "[[Stories/The 1919 Eclipse]]"
  - "[[The 1919 Eclipse]]"
  - "[[Planning an Experiment]]"
  - "[[Recording and Analysing Experimental Data]]"
teach_together:
  - "[[Repeated Measurements]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/experimental-physics
  - domain/measurement
  - level/A-Level
  - level/IB
  - level/AP
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-Mechanics
  - curriculum/AP-Physics-C-EM
  - syllabus/9702-1-3
  - syllabus/0625-P4
  - type/deep
  - type/vocabulary
  - notation/significant-figures
  - misconception/calculator-gives-more-accuracy
  - misconception/sig-figs-equal-decimal-places
  - misconception/exact-constants-limit-sig-figs
---

# Significant Figures 有效数字

## Hunter trace — your calculator just lied to you

You measure two sides of a rectangle with a ruler: $L = 12.3~\text{cm}$ and $W = 4.5~\text{cm}$. You want the area. You type $12.3 \times 4.5$ into your calculator, and the screen shows:

$$55.35$$

You write *that* down on your lab sheet. Four significant figures. Looks precise. Looks scientific.

The arithmetic is correct, but a measurement report needs one more decision: **how many of those digits does the evidence support?** The calculator knows the numbers you entered; it does not know the ruler's resolution, the scatter in repeated readings, or any calibration error.

Writing $55.35~\text{cm}^2$ without an uncertainty suggests more precision than the input measurements justify. It does not tell a reader exactly which ruler was used, and the extra digits were not created by a floating-point error: they are the correct product of the written inputs.

Using the usual fewest-significant-figures convention gives $\boxed{55~\text{cm}^2}$. With explicit uncertainty estimates, propagate those uncertainties and report the result accordingly instead.

> Significant figures are a compact **reporting convention**. They communicate the precision you intend to claim; they do not replace an uncertainty estimate or prove that a measurement is accurate.

## Definition and counting rules

A **significant figure** (有效数字 yǒuxiào shùzì) is a digit in a number that carries information about the measurement. The counting rules — covered in detail at [[Rounding (Vocab)]] — are:

1. All non-zero digits are significant. $4.5$ has 2 s.f.; $123$ has 3 s.f.
2. Zeros *between* non-zero digits are significant. $4.05$ has 3 s.f.; $1002$ has 4 s.f.
3. Leading zeros are *not* significant — they are placeholders. $0.00450$ has 3 s.f. (the 4, 5, 0 — not the leading zeros).
4. Trailing zeros after a decimal point *are* significant. $4.50$ has 3 s.f. (the trailing zero earned its keep — it was measured).
5. Trailing zeros in an integer with no decimal point are **ambiguous**. $4500$ could be 2, 3, or 4 s.f. — use scientific notation to disambiguate.

The fifth rule is the trap. $4500$ written on a lab sheet is genuinely ambiguous — no convention saves you. The fix is scientific notation, which makes the claim explicit:

| Written as | Significant figures | Means |
|---|---|---|
| $4.5 \times 10^{3}$ | 2 s.f. | measured to the nearest $100$ |
| $4.50 \times 10^{3}$ | 3 s.f. | measured to the nearest $10$ |
| $4.500 \times 10^{3}$ | 4 s.f. | measured to the nearest $1$ |

This is one of the quiet jobs scientific notation does: every time you write a number in standard form, *you cannot accidentally hide a sig-fig count.* The mantissa shows it.

### 中文锚点

厨房秤只显示到整克。把一个鸡蛋称五次，得到 61、62、61、63、62，让计算器求平均，它给出 61.8；再让它往下除一步，它会若无其事地显示 12.34782。多出来的这些数字，没有一位是量出来的。秤从来看不到比一克更小的东西，而且这五次读数彼此就差着一两克。你写下的每一位数字，都是在声明你对这个量了解到什么程度：写 61.8 g，是说 61 有把握，8 也大致靠得住；写 61.80000 g，等于宣称你连十万分之一克的差别都分得出来，这是用数字撒的谎。所以 4.50 和 4.5 虽然是同一个数，却是两句不同的话：前一句说有人看过百分位，发现那里是零；后一句说根本没人看过。计算器不知道你的仪器能看清到哪一位，所以数字写到哪里为止，得由你来决定，而且这要由测量说了算，而不是屏幕说了算。

### 术语对照 (Terms)

**有效数字** (yǒuxiào shùzì) 从第一个非零数字开始数，**小数位**从小数点后开始数，所以 $0.00450$ 有三位有效数字，却有五位小数。

| English | 中文 | 缩写 |
|---|---|---|
| Significant figure | 有效数字 (yǒuxiào shùzì) | s.f. |
| Decimal place | 小数位 (xiǎoshù wèi) | d.p. |
| Scientific notation / standard form | 科学记数法 / 标准形式 | — |
| Round to *n* s.f. | 保留 $n$ 位有效数字 | — |
| Trailing zero (significant) | 末尾零 (有效) | — |
| Leading zero (not significant) | 前导零 (无效) | — |

---

## The weakest-link rule for arithmetic

When explicit uncertainties are unavailable, two common rounding conventions prevent a calculated result from appearing much more precise than its inputs. These are useful approximations, not exact laws of uncertainty propagation. Keep extra digits during working and round the final report:

**Multiplication / division — match the fewest *sig figs*.**

$$\text{output s.f.} = \min(\text{input s.f.})$$

Example: $12.3 \times 4.5 = 55.35$ → but the inputs have 3 s.f. and 2 s.f., so this convention quotes the answer to 2 s.f.: $\boxed{55}$.

**Addition / subtraction — match the fewest *decimal places*.**

$$\text{output d.p.} = \min(\text{input d.p.})$$

Example: $12.34 + 4.5 = 16.84$ → but the inputs have 2 d.p. and 1 d.p., so this convention quotes the answer to 1 d.p.: $\boxed{16.8}$.

Why two rules? [[Error Propagation]] explains the underlying distinction: sums involve absolute uncertainties, whereas products and quotients involve fractional uncertainties. A very uncertain input often dominates, which motivates the shortcuts. But several comparable contributions add up, and the first digit changes the relationship between a significant-figure count and fractional precision. **The minimum count is not a derivation of the actual uncertainty.**

For example, if a last digit represents rounding to the nearest unit, $100$ and $999$, both specified to three significant figures, have rounding half-widths of $0.5$ but very different relative half-widths: $0.5\%$ and about $0.05\%$. Likewise, rounding to one decimal place gives a rounding interval of $\pm0.05$ units; that need not be the instrument's total measurement uncertainty.

### A worked example

> A student measures the period of a pendulum five times and gets $T = 2.01, 2.03, 2.00, 2.02, 2.04~\text{s}$ (each reading to 2 d.p., 3 s.f.). They also measure its length once: $L = 1.234~\text{m}$ (4 s.f.). Compute $g = 4\pi^2 L / T^2$.

**Step 1 — tool: arithmetic mean; trigger: repeated timings of the same period.** The mean is $\bar T=2.02~\mathrm s$. Retain the unrounded mean in subsequent calculation. Averaging can reduce random uncertainty, but there is no automatic entitlement to one extra significant figure; the scatter and other uncertainties decide that.

**Step 2 — tool: the pendulum-period relation, rearranged for $g$.**

$$g=\frac{4\pi^2(1.234)}{(2.02)^2}=11.9391156\ldots~\mathrm{m\,s^{-2}}.$$

**Step 3 — tool: the fewest-significant-figures convention; trigger: no explicit uncertainty budget was supplied.** $L$ has 4 s.f., $\bar T$ is being reported to 3 s.f., and $4\pi^2$ is exact. This convention gives $\boxed{g=11.9~\mathrm{m\,s^{-2}}}$.

The result is about $22\%$ above $9.81~\mathrm{m\,s^{-2}}$, a substantial discrepancy. These numbers alone do not diagnose whether it comes from bias, procedure or an unsuitable model. Appropriate significant figures do not make an inaccurate result accurate; see [[Accuracy vs Precision]].

---

## Round the answer to match its uncertainty

The "weakest-link" rule above is the **input-side** rule — what's allowed given your measurements. There's an even stronger rule when you know the uncertainty *explicitly*: the printed answer must round to the same place as the uncertainty.

If you computed $g = 11.95 \pm 0.13~\text{m s}^{-2}$ from a full [[Error Propagation]] calculation, then:

- If the uncertainty is rounded to one significant figure, $0.13$ becomes $0.1$.
- The value must be rounded to the same place: $g = 12.0 \pm 0.1~\text{m s}^{-2}$, or kept to one more digit if quoting two s.f. of uncertainty: $g = 11.95 \pm 0.13~\text{m s}^{-2}$.

The rule of thumb: **quote uncertainty to 1–2 sig figs, then round the value to match.**

Bad: $g = 11.95821 \pm 0.13$ — the value has digits beyond where the uncertainty rules them noise.

Good: $g = 11.96 \pm 0.13$ — value and uncertainty terminate at the same decimal place.

This is the rule that makes the connection to [[Accuracy vs Precision]] tight. An uncertainty budget can include both random effects and imperfectly known systematic corrections. The displayed digits should agree with that budget; a significant-figure count alone does not specify it.

---

## Common misconceptions

### 1. "Calculator answers are more accurate"

**The mistake.** Writing every digit the calculator shows because "the calculator computed it correctly."

**Why it's wrong.** The calculator did compute it correctly *given* your inputs — but the inputs themselves were measurements, with finite precision. The calculator has no idea your inputs were measurements. It would happily print 10 digits if you typed in two-digit inputs. The extra digits can be arithmetically correct while being unsupported as measurement precision. This is a reporting problem, not necessarily a floating-point problem.

**Fix.** Always finish a calculation by asking: "what is the weakest input, and how many sig figs does it have?" Round to that.

### 2. "Sig figs are the same as decimal places"

**The mistake.** "Round to 3 s.f." and the student rounds to 3 d.p. — different answer, different mark.

**Why it's wrong.** Decimal places count digits *after the decimal point*; significant figures count digits *from the first non-zero one*. For $0.00450$:
- 3 s.f. would round to $0.00450$ (already there)
- 3 d.p. would round to $0.005$ (only one s.f.!)

Big difference, especially for small numbers.

**Fix.** Read the question carefully. "s.f." and "d.p." are different instructions. When in doubt, *count from the first non-zero digit* (sig figs) vs *count after the decimal* (d.p.).

### 3. "Exact constants limit your sig figs"

**The mistake.** "$2\pi r = 2 \times 3.14 \times 5.00$ — the $3.14$ has 3 s.f., so my circumference is also 3 s.f."

**Why it's wrong.** $\pi$ is *exact* — its true value has infinitely many digits, and any specific decimal approximation is just a typographic convenience. You should not let your *typed* version of $\pi$ artificially limit your sig figs. The same applies to $2$ in $2\pi r$ (an exact integer, infinite s.f.), to $\tfrac{4}{3}$ in $\tfrac{4}{3}\pi r^3$ (exact rational), to defined constants like $c = 299\,792\,458~\text{m s}^{-1}$ (exact since 1983).

**Fix.** Use enough digits of $\pi$ (your calculator's full precision — typically 10+ digits) in the computation. Only round at the end, based on the **measured** inputs.

### 4. "Trailing zeros don't matter"

**The mistake.** Writing "$L = 4.5~\text{m}$" when you actually measured "$4.50~\text{m}$" (down to the centimetre).

**Why it's wrong.** Dropping the trailing zero *understates* your precision. A reader takes $4.5$ to mean "measured to the nearest $0.1$" — but you measured to the nearest $0.01$ and threw the information away. The contract was: print every digit you know. By dropping the zero, you've broken the contract from the other side.

**Fix.** Whenever you measured a trailing zero, *write* the trailing zero. The convention is symmetric: don't print digits you didn't measure, *and* don't hide digits you did.

---

## Exam Notes

### Cambridge 9702 — numerical work and Papers 3/5

The practical-assessment guidance specifies consistent raw-data precision matched to the instrument. For calculated quantities other than sums/differences, if the least precise measured input has $n$ significant figures, **$n$ or $n+1$** figures are appropriate. The syllabus's own example allows 2 or 3 s.f. for resistance calculated from p.d. at 2 s.f. and current at 4 s.f. This is more permissive than a rigid minimum-count rule.

Paper 5 explicitly follows the Paper 3 conventions. Its logarithm example allows $\lg(76.5)=1.884$ or $1.8837$: decimal places in the logarithm track the input's significant figures. The mathematical requirements also say not to lose digits unnecessarily or retain unjustified ones. Do not assume a universal one-mark penalty; the question's mark scheme determines the award. §1.3 supplies the uncertainty context, rather than a standalone list of rounding rules.

### Cambridge 0625 — calculations and practical work

The syllabus's mathematical requirements say to round **only the final answer** and use significant figures and decimal places appropriately. Its presentation-of-data rules require measured precision suited to the instrument and calculated quantities with **the same number of significant figures as the least count in the raw data used**. Thus the minimum-count convention is explicitly present; it is not merely an unexamined extension.

Papers 5/6 also require measurements recorded to appropriate precision, including half-scale readings where required. The graphical guidance specifies 2–3 s.f. for calculated gradients. Keep that context separate from an invented universal 2–3-s.f. rule for every result.

### IB Physics — skills across the course

Under **Skills in the study of physics**, “Using units, symbols and numerical values” and “Processing uncertainties” require appropriate significant figures/decimal places for quantities and uncertainties. This is coursewide at SL/HL, not a numbered “PRAC.2” topic. In the scientific investigation, the data-analysis criterion includes precise communication through units, decimal places and significant figures. It does not prescribe one automatic penalty for each misplaced digit.

### AP Physics 1 / 2 / C: Mechanics / C: Electricity & Magnetism

Use sensible numerical precision in calculations and data analysis, retaining working digits until the end. AP Physics 2's **Calculate** command explicitly mentions units and significant figures. None of the reviewed course frameworks supports a universal “plus or minus one significant figure” marking allowance or a guaranteed one-point deduction on a particular FRQ. Follow the instructions and released rubric for the actual question.

### Mathematics and the scope boundary

[[Rounding (Vocab)]] supplies the mathematical counting and rounding conventions. Measurement uncertainty and uncertainty-matched reporting are the physics application. These are practical/numerical skills rather than a separate content unit on the current IB or AP course maps.

---

## Connections

- **Parent:** [[Rounding (Vocab)]] — the maths-side card with the basic counting rules. Measurement reporting adds arithmetic conventions and uncertainty matching.
- **Sibling:** [[Accuracy vs Precision]] — the typographic version of precision. The sig-fig count of a written value claims a precision; that claim must be honest.
- **Sibling:** [[Error Propagation]] — propagation quantifies how input uncertainties affect a result; significant figures are a reporting shortcut, not a substitute.
- **At the bench:** [[Recording and Analysing Experimental Data]] — why 4.70 cm and 4.7 cm are different records, and how many figures a gradient deserves.
- **Components:** [[Standard Form (Vocab)]] — scientific notation is an unambiguous way to write a number with a *given* sig-fig count. The two cards travel together.
- **Application:** [[Casio fx-991 Reference]] — calculator display settings; showing fewer digits does not improve measurement accuracy.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $4.50 \times 10^{3}$ | `4.50 \times 10^{3}` | Scientific notation — the canonical way to disambiguate sig-fig count. |
| s.f. | `s.f.` | Abbreviation for "significant figures." Cambridge mark schemes use this. |
| d.p. | `d.p.` | Abbreviation for "decimal places." Not interchangeable with s.f. |
| $\pm$ | `\pm` | Plus-minus, for uncertainty. The value's sig figs must terminate at the same place as the uncertainty. |
| $\boxed{\text{result}}$ | `\boxed{...}` | Box the final answer at the *correct* sig-fig count, after retaining working digits. |

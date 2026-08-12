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
  - syllabus/9702-1-3
  - syllabus/0625-P4
  - syllabus/IB-Physics-PRAC-2
  - syllabus/AP-Physics-1-SP-1
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

It is *not* scientific. It is a lie. Both your measurements have three (and two!) significant figures — neither side was measured to four. Where did the fourth digit of $55.35$ come from? The calculator made it up. It dutifully ran the arithmetic and reported every digit the floating-point unit happened to hold, without any clue what your measurements actually mean. **The trailing "5" is not data; it is noise that the calculator dressed up to look like data.**

A reader who knows the conventions takes one look at "$55.35~\text{cm}^2$" and infers: *this person measured both sides to the nearest hundredth of a centimetre.* You didn't. Your ruler is to the nearest millimetre. Writing $55.35$ is *misrepresenting* the precision of your apparatus.

The honest answer is $\boxed{55~\text{cm}^2}$ — two significant figures, matching the *weaker* of the two inputs. This card is about why.

> Significant figures are not a precision convention. They are an **honesty contract** between the writer and the reader: *the digits I print are the digits I actually know.* Print more and you have lied; print fewer and you have understated your work.

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

| English | 中文 | 缩写 |
|---|---|---|
| Significant figure | 有效数字 (yǒuxiào shùzì) | s.f. |
| Decimal place | 小数位 (xiǎoshù wèi) | d.p. |
| Scientific notation / standard form | 科学记数法 / 标准形式 | — |
| Round to *n* s.f. | 保留 $n$ 位有效数字 | — |
| Trailing zero (significant) | 末尾零 (有效) | — |
| Leading zero (not significant) | 首位零 (无效) | — |

中国高中物理课本和数学课本都用 **有效数字** — 与英文 "significant figures" 完全对应。"保留三位有效数字" 就是 "round to 3 s.f." 的标准翻译。

中文物理课本的一个重点：**末尾零的有效性**。$4.50$ 和 $4.5$ 在数学上相等，在物理测量中却传达不同信息——前者声称测到 $0.01$ 的精度，后者只声称测到 $0.1$。这一点在 Cambridge / IB / AP 物理课本中**完全一致**。

> [!warning] Sig figs are *not* decimal places
> "$0.00450$" has 3 s.f. but 5 d.p. — sig figs and decimal places count different things. Mixing them is the #1 sig-figs mistake on exams. "Round to 3 s.f." and "round to 3 d.p." are different instructions, and getting them confused costs the mark.

---

## The weakest-link rule for arithmetic

When you combine measurements, the result's allowed precision is limited by the *weakest* input. There are two flavours of the rule depending on the operation:

**Multiplication / division — match the fewest *sig figs*.**

$$\text{output s.f.} = \min(\text{input s.f.})$$

Example: $12.3 \times 4.5 = 55.35$ → but the inputs have 3 s.f. and 2 s.f., so the answer must be quoted to 2 s.f.: $\boxed{55}$.

**Addition / subtraction — match the fewest *decimal places*.**

$$\text{output d.p.} = \min(\text{input d.p.})$$

Example: $12.34 + 4.5 = 16.84$ → but the inputs have 2 d.p. and 1 d.p., so the answer must be quoted to 1 d.p.: $\boxed{16.8}$.

The two rules look different. Why? They come from the *same* deeper principle — the uncertainty in the result must dominate the precision of the result. [[Error Propagation]] does the full derivation; the abbreviated version:

- For products and quotients, *percentage* uncertainties add. The weakest input — the one with the largest fractional uncertainty — dominates the percentage uncertainty in the output. Significant figures encode percentage precision, so they obey the same rule.
- For sums and differences, *absolute* uncertainties add. The weakest input — the one with the largest absolute uncertainty — dominates the absolute uncertainty in the output. Decimal places encode absolute precision, so they obey the same rule.

> [!info] Why two rules, not one?
> Significant figures and decimal places are not interchangeable, because they encode *different kinds* of precision. Sig figs are scale-invariant — "3 s.f." means "uncertain at the 0.1% level" no matter whether the number is $4.5$ or $4500000$. Decimal places are absolute — "1 d.p." means "uncertain at the $\pm 0.05$ level" no matter whether the number is $4.5$ or $4500000$. Multiplication preserves scale-invariant precision (sig figs); addition preserves absolute precision (d.p.). The rules differ because the operations preserve different kinds of information.

### A worked example

> A student measures the period of a pendulum five times and gets $T = 2.01, 2.03, 2.00, 2.02, 2.04~\text{s}$ (each reading to 2 d.p., 3 s.f.). They also measure its length once: $L = 1.234~\text{m}$ (4 s.f.). Compute $g = 4\pi^2 L / T^2$.

**Step 1.** Average the timings: $\bar{T} = 2.020~\text{s}$. (4 s.f. — averaging *does not* increase the sig-fig count of any single reading, but the *mean* can legitimately carry one extra sig fig because of $\sqrt{N}$ shrinking; see [[Repeated Measurements]]. For a rough school-lab card, treat the mean as carrying the same sig figs as one reading.)

**Step 2.** Plug in: $g = 4\pi^2 (1.234) / (2.020)^2$. The calculator says $g = 11.948\ldots~\text{m s}^{-2}$. (A calculator-vomit answer like this is your first warning sign — you typed numbers with 3-4 sig figs in, and out came a number you could quote to 10. Don't.)

**Step 3.** Find the weakest input:
- $L = 1.234~\text{m}$ → 4 s.f.
- $\bar{T} = 2.020~\text{s}$ → 3 s.f. (per the rule of thumb above)
- $4\pi^2$ is *exact* (a defined mathematical constant, see Misconception 3) → infinite s.f., doesn't constrain

Weakest input is $\bar{T}$ at 3 s.f. Answer must be quoted to 3 s.f.

**Step 4.** Quote: $g = 11.9~\text{m s}^{-2}$.

Sanity check: $9.81~\text{m s}^{-2}$ is the accepted value, so the measurement is biased a little high — that's an *accuracy* issue (see [[Accuracy vs Precision]]) and would be reported separately. The *sig figs* of the answer are not about whether the answer is right; they are about how many digits we can honestly claim from our inputs.

---

## Round the answer to match its uncertainty

The "weakest-link" rule above is the **input-side** rule — what's allowed given your measurements. There's an even stronger rule when you know the uncertainty *explicitly*: the printed answer must round to the same place as the uncertainty.

If you computed $g = 11.95 \pm 0.13~\text{m s}^{-2}$ from a full [[Error Propagation]] calculation, then:

- The uncertainty is at the $0.1$ place (its first significant figure is in the tenths column).
- The value must be rounded to the same place: $g = 12.0 \pm 0.1~\text{m s}^{-2}$, or kept to one more digit if quoting two s.f. of uncertainty: $g = 11.95 \pm 0.13~\text{m s}^{-2}$.

The rule of thumb: **quote uncertainty to 1–2 sig figs, then round the value to match.**

Bad: $g = 11.95821 \pm 0.13$ — the value has digits beyond where the uncertainty rules them noise.

Good: $g = 11.96 \pm 0.13$ — value and uncertainty terminate at the same decimal place.

This is the rule that makes the connection to [[Accuracy vs Precision]] tight. The uncertainty number $\Delta x$ is the *quantitative* version of "precision"; the sig figs of the value are its *typographic* version. The two must agree, or the reader gets a false story.

---

## Common misconceptions

### 1. "Calculator answers are more accurate"

**The mistake.** Writing every digit the calculator shows because "the calculator computed it correctly."

**Why it's wrong.** The calculator did compute it correctly *given* your inputs — but the inputs themselves were measurements, with finite precision. The calculator has no idea your inputs were measurements. It would happily print 10 digits if you typed in two-digit inputs. The extra digits are *fabricated by floating-point arithmetic*, not by your apparatus. They look authoritative; they aren't.

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

### Cambridge 9702 (A-Level Physics)

§1.3 and across every paper. Examiners are unforgiving about this — a numerical answer quoted to the wrong number of sig figs typically loses 1 mark (often called the "consistency mark" or "precision mark"). Standard expectations:

- Final numerical answers should be given to 2 or 3 sig figs unless the question specifies otherwise.
- If the question gives data to varying precision, match the weakest input. ($s = 12.34~\text{m}$, $t = 5.6~\text{s}$ → $v$ to 2 s.f.)
- Paper 3 (Practical) and Paper 5 (Planning & Analysis): when *uncertainty* is calculated, the value must match the uncertainty's place — see "Round the answer to match its uncertainty" above. This is the most common precision-mark loss on P5.

### IB Physics (2025 syllabus)

Tools 1: PRAC.2 includes "significant figures" as an explicit syllabus point. The IB Data Booklet does not contain rules — students must internalise them. The IA (Scientific Investigation) is graded in part on whether students present data and results with appropriate precision. A common IA criticism: tables with 8-digit calculator outputs where 3 s.f. would be more honest.

### AP Physics 1 / 2

Less aggressive than Cambridge or IB on sig-fig mark deduction — AP rubrics typically allow $\pm 1$ s.f. on either side of "correct" before marking down. But sig figs *do* appear in FRQ 3 (Experimental Design and Analysis) when students are asked to "report your final answer to an appropriate number of significant figures." Getting this wrong on FRQ 3 is a 1-point loss.

### Cambridge 0625 (IGCSE Physics)

This lands on the **practical papers** — Paper 5 or Paper 6 — not in one of the six numbered topics: record observations and measurements *to an appropriate degree of precision*, and take readings *with appropriate precision, to the nearest half-scale division where required*. In practice that means 2–3 significant figures in numerical answers, and never letting an answer claim more precision than the measurements behind it. The formal weakest-link rule is not required at IGCSE — but the spirit of "don't write more digits than your ruler earns you" is exactly what is being marked.

### Cambridge 0580 / 0606 / OxAQA 9260

Maths-side: see [[Rounding (Vocab)]] for the counting rules and the bare arithmetic of "round to 3 s.f." These cards live in `Mathematics/Number/` and are 🟢. The Physics-side application (weakest-link rule, match-the-uncertainty rule) is unique to this card.

---

## Connections

- **Parent:** [[Rounding (Vocab)]] — the maths-side card with the basic counting rules. This Physics card layers the weakest-link arithmetic + uncertainty-matching rules on top.
- **Sibling:** [[Accuracy vs Precision]] — the typographic version of precision. The sig-fig count of a written value claims a precision; that claim must be honest.
- **Sibling:** [[Error Propagation]] — the derivation of the weakest-link rule lives here. Sig figs are the rule-of-thumb shortcut for "match the fractional uncertainty"; error propagation gives you the exact formula.
- **Components:** [[Standard Form (Vocab)]] — scientific notation is the unique unambiguous way to write a number with a *given* sig-fig count. The two cards travel together.
- **Application:** [[Casio fx-991 Reference]] — calculator settings for displaying answers to a chosen number of sig figs (SHIFT-MODE-7 on the fx-991; equivalent shortcuts on Texas Instruments / HP).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $4.50 \times 10^{3}$ | `4.50 \times 10^{3}` | Scientific notation — the canonical way to disambiguate sig-fig count. |
| s.f. | `s.f.` | Abbreviation for "significant figures." Cambridge mark schemes use this. |
| d.p. | `d.p.` | Abbreviation for "decimal places." Not interchangeable with s.f. |
| $\pm$ | `\pm` | Plus-minus, for uncertainty. The value's sig figs must terminate at the same place as the uncertainty. |
| $\boxed{\text{result}}$ | `\boxed{...}` | Box the final answer at the *correct* sig-fig count, not the calculator's vomit. |

---
chinese: 比例 (bǐlì)
prerequisites:
  - "[[Ratio (Vocab)]]"
  - "[[Direct and Inverse Proportion (Vocab)]]"
leads_to:
  - "[[Linearisation]]"
  - "[[Rates (Vocab)]]"
  - "[[Scale Drawings (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/Cambridge-0580
  - curriculum/OxAQA-9260
  - syllabus/0580-E1-11
  - syllabus/0580-E2-8
  - syllabus/9260-N18
  - syllabus/9260-N20
  - type/vocabulary
  - notation/proportional-symbol
---

# Proportion 比例

## Definition

A **proportion** is a statement that *two ratios are equal*:

$$\frac{a}{b} = \frac{c}{d}.$$

If you scale up a recipe, paint a model, or read a map, you're using proportion: the relationship between the parts stays *the same* even as their absolute sizes change.

Two related but distinct ideas:

- **Direct proportion** ($y \propto x$): when one variable doubles, the other doubles. Algebraically $y = kx$ for some constant $k$. Doubling distance traveled at constant speed → doubling time.
- **Inverse proportion** ($y \propto 1/x$): when one variable doubles, the other halves. Algebraically $y = k/x$. Doubling speed at constant distance → halving travel time.

For finding the constant and working with powers, see [[Direct and Inverse Proportion (Vocab)]].

### 中文锚点

摊煎饼时，一杯面粉配两杯牛奶。朋友多来了几个，你把面粉和牛奶都加倍，面糊的稀稠程度还是差不多，因为每杯面粉分到的牛奶没变。如果只把牛奶加倍，面糊就会变稀。比例守住的正是这种搭配关系：总量可以变，彼此怎么配不变。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| proportion | 比例 | equal ratios |
| proportional (to) | 正比于 / 与...成比例 | $y$ is proportional to $x$ → $y = kx$ |
| direct proportion | 正比 | constant ratio $y/x$ |
| inverse proportion | 反比 | constant product $xy$ |
| constant of proportionality | 比例常数 | the $k$ in $y = kx$ |
| in the ratio $a : b$ | 按 $a : b$ 的比 | shares of a quantity |

---

## Worked Examples

### Example 1 — direct proportion (the simplest case)

> A recipe for $4$ people uses $300$ g of flour. How much flour is needed for $7$ people?

**Tool: a constant per-person amount.** Keeping the recipe the same selects direct proportion. The amount of flour is **directly proportional** to the number of people: $\dfrac{\text{flour}}{\text{people}} =$ constant.

$$\frac{300}{4} = \frac{F}{7} \;\Longrightarrow\; F = \frac{300 \times 7}{4} = 525 \text{ g}.$$

### Example 2 — inverse proportion

> A car travels a fixed distance in $3$ hours at $60$ km/h. How long does it take at $80$ km/h?

**Tool: distance = speed × time.** Fixed distance selects a constant product. Time is **inversely proportional** to speed: $\text{time} \times \text{speed} = \text{distance}$ (constant).

$$3 \times 60 = T \times 80 \;\Longrightarrow\; T = \frac{180}{80} = 2.25 \text{ h}.$$

### Example 3 — splitting in a ratio

> Divide \$120 between two people in the ratio $3 : 5$.

**Tool: count equal parts.** The total is shared, so the ratio entries add to the number of parts. Total parts: $3 + 5 = 8$. Each part: $120 \div 8 = 15$. So $3 \times 15 = 45$ and $5 \times 15 = 75$.

**Answer:** \$45 and \$75.

---

## Common Mistakes

1. **Mixing up direct and inverse.** Always ask: "if one doubles, does the other double or halve?" Halve = inverse.
2. **Forgetting the constant $k$.** "$y \propto x$" means $y = kx$ with $k$ to be found from given data. Don't write $y = x$.
3. **Confusing ratio with proportion.** A *ratio* compares two quantities ($a:b$); a *proportion* states two ratios equal ($a:b = c:d$). The proportion is the equation; the ratio is one side of it.

---

## Exam Notes

### Cambridge 0580 (2025–2027)

**C1.11 / E1.11** covers simplifying ratios, division in a ratio and proportional reasoning in recipes, maps and best-value comparisons. **E2.8** separately covers algebraic direct/inverse proportion, including linear, square, square-root, cube and cube-root relationships. Do not assign the entire power-law topic to E1.11.

A ratio-sharing question needs the total number of parts; a proportion equation needs the invariant ratio or product. With $y\propto x^2$, find $k$ in $y=kx^2$ from the given pair before substituting new values. See [[Direct and Inverse Proportion (Vocab)]].

### OxfordAQA 9260

**N16** names ratio notation, **N17** division in a ratio, **N18** ratio applications and **N20** direct/inverse proportion and repeated proportional change. N18 alone is not the reference for every example here. Exponential growth/decay is N20 Extension; its full treatment is [[Exponential Growth and Decay]]. No special proportion formula is supplied in the specification's formula provision: build the invariant relationship.

### IB and later mathematics

Both **IB Mathematics AA and AI** list simple ratio/proportion applications under *Prior learning*. That means assumed knowledge which questions may use, not a separately numbered new topic ([AA guide](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-analysis-approaches-guide.pdf), [AI guide](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-applications-interpretation-guide.pdf), p. 24).

**Not a separate proportion-vocabulary unit:** Cambridge 0606, 9709, 9231, OxfordAQA 9660, Edexcel IAL Mathematics and AP Calculus AB/BC. Ratio and algebra remain usable prerequisites; for example, 9709 differential-equation modelling explicitly requires an appropriate constant of proportionality. This is not a claim that proportional reasoning is absent from their questions.

---

## Connections

- **Prerequisite:** [[Ratio (Vocab)]] — proportion is *two ratios* set equal
- **Deep treatment:** [[Direct and Inverse Proportion (Vocab)]] — algebraic form $y = kx$, $y = k/x$, $y = kx^n$ with worked examples
- **Application:** [[Linearisation]] — power-law data $y = Ax^n$ is detected by checking proportion in log-log coordinates
- **Forward:** *physics* — Newton's $F = ma$ ($F \propto a$ at constant $m$); ideal gas $PV = nRT$ (mixed proportion)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\propto$ | `\propto` | "proportional to" |
| $y = kx$ | `y = kx` | direct proportion |
| $y = \dfrac{k}{x}$ | `y = \dfrac{k}{x}` | inverse proportion |
| $a : b = c : d$ | `a : b = c : d` | proportion (equal ratios) |

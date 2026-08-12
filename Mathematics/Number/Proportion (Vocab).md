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
  - syllabus/0580-E1-11
  - syllabus/9260-N18
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

This card is the *vocabulary* anchor for the §N18 row. The full algebraic treatment with worked examples lives in [[Direct and Inverse Proportion (Vocab)]].

### 中文锚点

**比例 (bǐlì)** = 两个比 (bǐ) 相等的关系。

| 类型 | 中文 | 数学表达 |
|---|---|---|
| 正比 (zhèngbǐ) | direct proportion | $y \propto x$，即 $y = kx$ |
| 反比 (fǎnbǐ) | inverse proportion | $y \propto \dfrac{1}{x}$，即 $y = \dfrac{k}{x}$ |

**比例常数 (bǐlì chángshù)** = constant of proportionality, 常用 $k$ 表示。

记号：$\propto$ = "正比于"。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| proportion | 比例 | equal ratios |
| proportional (to) | 正比于 / 与...成比例 | $y$ is proportional to $x$ → $y = kx$ |
| direct proportion | 正比 | both grow together |
| inverse proportion | 反比 | one grows, the other shrinks |
| constant of proportionality | 比例常数 | the $k$ in $y = kx$ |
| in the ratio $a : b$ | 按 $a : b$ 的比 | shares of a quantity |

---

## Worked Examples

### Example 1 — direct proportion (the simplest case)

> A recipe for $4$ people uses $300$ g of flour. How much flour is needed for $7$ people?

The amount of flour is **directly proportional** to the number of people: $\dfrac{\text{flour}}{\text{people}} =$ constant.

$$\frac{300}{4} = \frac{F}{7} \;\Longrightarrow\; F = \frac{300 \times 7}{4} = 525 \text{ g}.$$

### Example 2 — inverse proportion

> A car travels a fixed distance in $3$ hours at $60$ km/h. How long does it take at $80$ km/h?

Time is **inversely proportional** to speed: $\text{time} \times \text{speed} = \text{distance}$ (constant).

$$3 \times 60 = T \times 80 \;\Longrightarrow\; T = \frac{180}{80} = 2.25 \text{ h}.$$

### Example 3 — splitting in a ratio

> Divide \$120 between two people in the ratio $3 : 5$.

Total parts: $3 + 5 = 8$. Each part: $120 \div 8 = 15$. So $3 \times 15 = 45$ and $5 \times 15 = 75$.

**Answer:** \$45 and \$75.

---

## Common Mistakes

1. **Mixing up direct and inverse.** Always ask: "if one doubles, does the other double or halve?" Halve = inverse.
2. **Forgetting the constant $k$.** "$y \propto x$" means $y = kx$ with $k$ to be found from given data. Don't write $y = x$.
3. **Confusing ratio with proportion.** A *ratio* compares two quantities ($a:b$); a *proportion* states two ratios equal ($a:b = c:d$). The proportion is the equation; the ratio is one side of it.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E1.11 (Ratio and Proportion) — direct and inverse variation. Standard patterns:

- "$y$ is directly proportional to $x$. When $x = 4$, $y = 12$. Find $y$ when $x = 9$."
- "$P$ is inversely proportional to $Q^2$. When $Q = 2$, $P = 5$. Find $P$ when $Q = 4$."

For the variant where $y \propto x^n$ (general power), see [[Direct and Inverse Proportion (Vocab)]].

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

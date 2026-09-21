---
chinese: 排序与不等号 (páixù yǔ bùděnghào)
prerequisites:
  - "[[Number Sets (Vocab)]]"
leads_to:
  - "[[Linear Inequalities (Vocab)]]"
  - "[[Quadratic Inequalities]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/0580-E1-5
  - syllabus/9260-N1
  - type/vocabulary
  - notation/inequality
  - misconception/inequality-direction
---

# Ordering and Inequalities Notation 排序与不等号

## Definition

Real numbers can be ordered along a **number line**. The standard symbols compare two numbers:

| Symbol | Read as | Meaning |
|---|---|---|
| $=$ | "equals" | the two values are identical |
| $\neq$ | "not equal to" | the two values differ |
| $>$ | "greater than" | left value is larger |
| $<$ | "less than" | left value is smaller |
| $\ge$ | "greater than or equal to" | left value is at least the right |
| $\le$ | "less than or equal to" | left value is at most the right |

Reading rule: the **open end** of the inequality faces the *larger* number (the symbol "points away" from the bigger value, mouth open toward it). $7 > 3$ and $3 < 7$ say the same thing — $7$ is larger; the symbol's wide end faces the $7$ each time.

### 中文锚点

天气预报说今天零下五度，明天零下两度，你会觉得明天暖和些。虽然“五”比“二”大，零下五度却排在零下两度的下面：温度往上走，数值才变大。不等号记的也是这个顺序，所以写成 $-5<-2$。别只盯着离零有多远——温度计上站在哪一边，才决定谁大谁小。

### 术语对照

排序：ordering；不等号：inequality symbol；升序：ascending；降序：descending。$>$：大于；$<$：小于；$\ge$：大于等于；$\le$：小于等于；$\ne$：不等于。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| ascending order | 升序 | smallest to largest, left to right |
| descending order | 降序 | largest to smallest, left to right |
| number line | 数轴 (shùzhóu) | horizontal line marked with numbers; larger to the right |
| at least | 至少 (zhìshǎo) | translates to $\ge$ in inequalities |
| at most | 至多 (zhìduō) | translates to $\le$ |
| more than | 多于 / 大于 | translates to $>$ (strict) |
| fewer than / less than | 少于 / 小于 | translates to $<$ (strict) |
| no more than | 不超过 (bù chāoguò) | $\le$ |
| no less than | 不少于 | $\ge$ |
| double inequality | 双重不等式 | e.g. $-3 < x \le 5$ — $x$ is between $-3$ and $5$ |

---

## Worked Examples

### Example 1 — ordering with negatives and fractions

> Arrange in ascending order: $-2,\;\; \tfrac{3}{4},\;\; -\tfrac{1}{2},\;\; 1.5,\;\; -2.1$.

**Tool: number-line order. Trigger: mixed fractions, decimals and negative signs make visual digit comparison unreliable.** Convert fractions as needed, then plot on a number line: $-2.1$ is the most negative (furthest left), then $-2$, then $-\tfrac{1}{2}$, then $\tfrac{3}{4} = 0.75$, then $1.5$.

**Answer.** $-2.1 < -2 < -\tfrac{1}{2} < \tfrac{3}{4} < 1.5$.

> [!warning] Negative numbers — bigger absolute value means *smaller*
> $-5 < -3$, even though $5 > 3$. On the number line, $-5$ sits to the left of $-3$, so it's smaller. The classic mistake: treating $\lvert -5 \rvert > \lvert -3 \rvert$ as if it meant $-5 > -3$. Always read the position on the number line, not the magnitude.

### Example 2 — translating English to symbols

> Write each phrase as an inequality in $x$:
> (a) "$x$ is at least $5$"
> (b) "$x$ is no more than $10$"
> (c) "$x$ is between $2$ and $7$, inclusive"
> (d) "$x$ is positive but less than $4$"

**Tool: test the boundary. Trigger: phrases such as “at least” differ in whether equality is allowed.** Ask whether the named endpoint satisfies the words.

**Answers.**
(a) $x \ge 5$ — *at least* = $\ge$
(b) $x \le 10$ — *no more than* = $\le$
(c) $2 \le x \le 7$ — double inequality, both ends *inclusive*
(d) $0 < x < 4$ — *positive* means $> 0$; *strictly less than 4*

### Example 3 — number line representation

**Tool: endpoint inclusion. Trigger: the two ends use different inequality signs.** For $-2 < x \le 3$:

```
←─────○━━━━━━━━━━━━━━━━━●─────→
      -2                3
```

**Open circle** at $-2$ (strict inequality, $-2$ excluded), **closed circle** at $3$ (non-strict, $3$ included), **bar** between them showing the included range.

> [!tip] The endpoint convention
> Open circle ($\circ$) means the endpoint is excluded; closed circle ($\bullet$) means it is included. The picture must encode the same set as the inequality.

---

## Common Mistakes

1. **Inequality direction with negatives.** $-5 < -3$, *not* $-5 > -3$. Number-line position decides, not absolute value.
2. **Mixing up "at least" and "more than".** "At least 5" means $\ge 5$ (5 is allowed). "More than 5" means $> 5$ (5 is *not* allowed). One word changes the symbol.
3. **Forgetting open vs closed circles.** $\le$ uses a *closed* (filled) circle on the number line; $<$ uses an *open* (unfilled) circle. Easy mark loss.
4. **Interpreting "between $a$ and $b$"** — at 0580 level "between $a$ and $b$, inclusive" gives $a \le x \le b$; "strictly between" gives $a < x < b$. The word *inclusive* / *exclusive* matters.
5. **Reversing inequalities by accident.** Multiplying or dividing by a negative *flips* the inequality direction: $-2x > 6 \implies x < -3$ (not $x > -3$). See [[Linear Inequalities (Vocab)]] for the full rule.

---

## Exam Notes

### Cambridge 0580 — Core and Extended

**C1.5 / E1.5 (Ordering)** require ordering quantities and using $=, \ne, >, <, \ge, \le$. **C2.6 / E2.6** also require interpreting and representing inequalities on number lines, with open endpoints for strict inequalities and filled endpoints for included boundaries. Solving linear inequalities and two-variable regions extends beyond the notation taught here: see [[Linear Inequalities (Vocab)]] and [[Graphical Inequalities (Vocab)]].

Practice prompts: order negative fractions and decimals; decide whether a boundary value is allowed; translate a double inequality into a number line; list the integers in a specified interval. These are illustrative prompts, not quoted past-paper questions.

### OxfordAQA 9260

**N1** requires ordering positive and negative integers, decimals and fractions and using comparison symbols, including number-line work. **A23** uses open and closed endpoint conventions when displaying solutions. Distinguish understanding the symbols from solving the inequalities: A23 also requires algebra, with quadratic and two-variable extensions.

### Further study — assumed language, not an HL-only invention

**Cambridge 0606** uses solution-set notation for quadratic inequalities (§2.5) and further inequalities in §4. **9709 §1.1**, **Edexcel IAL P1 §1.7–1.8** and **OxfordAQA 9660 P1.1** use inequalities in algebra; their substantive solving methods go beyond ordering. **9231** assumes ordinary A-Level mathematical language while extending the functions and problems to which it applies.

**IB AA and AI**, at both SL and HL, include inequalities and intervals on the real number line in **prior learning**. Interval notation is not an AA HL invention. In **AP Calculus AB/BC**, intervals describe domains, limits and derivative-sign conclusions; in **AP Statistics**, inequalities describe events and statistical comparisons. These are uses of prerequisite notation, not a separate ordering theorem to memorise.

**Where this is not a standalone new topic:** the advanced courses above do not introduce basic real-number ordering as a new theorem. They still require correct notation. No special formula-sheet entry is needed; read whether the boundary belongs to the set.

---

## Connections

- **Prerequisite:** [[Number Sets (Vocab)]] — placing a number on the line requires knowing which "type" of number it is
- **Forward:** [[Linear Inequalities (Vocab)]] — solving inequalities with the sign-flip rule
- **Forward:** [[Quadratic Inequalities]] — sign-chart machinery for $f(x) > 0$ on quadratics
- **Forward:** [[Set-Builder Notation]] — the formal language for "the set of $x$ satisfying ..."

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $=$ | `=` | equals |
| $\neq$ | `\neq` or `\ne` | not equals |
| $>, <$ | `>, <` | strict |
| $\ge, \le$ | `\ge, \le` | non-strict (LaTeX has `\geq, \leq` too) |
| $\circ, \bullet$ | `\circ, \bullet` | open / closed circles for number line |
| $a < x \le b$ | `a < x \le b` | double inequality |

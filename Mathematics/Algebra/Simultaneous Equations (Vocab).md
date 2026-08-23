---
chinese: 联立方程 (liánlì fāngchéng)
prerequisites:
  - "[[Linear Equations (Vocab)]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Factorising (Vocab)]]"
  - "[[Changing the Subject (Vocab)]]"
  - "[[Quadratic Equations]]"
leads_to:
  - "[[Graphical Inequalities (Vocab)]]"
  - "[[Sequences]]"
  - "[[Vector Equations of Lines]]"
  - "[[Linear Systems in 3D]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A21
  - syllabus/9260-A22
  - syllabus/0580-E2-5
  - syllabus/0606-5-1
  - type/vocabulary
  - misconception/substitution-sign-error
---

# Simultaneous Equations 联立方程

## Definition

**Simultaneous equations** (联立方程) are two or more equations that must be satisfied *at the same time* by the same values of the unknowns. "Simultaneous" comes from the Latin *simul* — "at the same time" (the same root as "simultaneous interpreting" and "simultaneously").

$$2x + y = 7 \qquad \text{and} \qquad x - y = 2$$

The solution $(x, y) = (3, 1)$ satisfies both equations at once.

### 中文锚点

联立方程 = 多个方程同时成立，求同一组未知数的值。"联立"就是"联合起来一起解"。两种方法：消元法（elimination）和代入法（substitution）。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| simultaneous equations | 联立方程 (liánlì fāngchéng) | Two+ equations solved together |
| elimination | 消元法 (xiāoyuán fǎ) | Add/subtract to remove a variable |
| substitution | 代入法 (dàirù fǎ) | Express one variable in terms of the other, plug in |
| linear | 一次的 (yīcì de) | Highest power is 1 — straight-line graph |
| non-linear | 非线性的 | One equation is quadratic (or higher) |
| point of intersection | 交点 (jiāodiǎn) | Where two graphs cross — the geometric meaning of the solution |
| consistent | 有解的 | At least one solution exists |
| inconsistent | 无解的 | No solution — parallel lines, never meet |

---

## The Two Methods

**1. Elimination 消元法** — make the coefficients of one variable match, then add or subtract.

$$2x + 3y = 12 \quad \text{①} \qquad 5x - 3y = 9 \quad \text{②}$$

$y$-coefficients are $+3$ and $-3$. Add ① + ②: $7x = 21$, so $x = 3$. Back-substitute: $y = 2$.

> [!tip] WHY does elimination work?
> If $A = B$ and $C = D$, then $A + C = B + D$. Adding two true equations produces another true equation — but one with fewer unknowns. You are using the **additive property of equality**, the same principle behind "do the same thing to both sides."

**2. Substitution 代入法** — rearrange one equation for one variable, plug into the other.

$$y = 2x - 1 \quad \text{①} \qquad 3x + 2y = 12 \quad \text{②}$$

Substitute ① into ②: $3x + 2(2x - 1) = 12 \;\Rightarrow\; 7x = 14 \;\Rightarrow\; x = 2$, $y = 3$.

**When to use which:**

| Situation | Method |
|-----------|--------|
| Coefficients already match or easy to match | Elimination |
| One equation already solved for $y$ (or $x$) | Substitution |
| One linear + one non-linear | Substitution (always) |

### Non-linear simultaneous equations (Extension)

When one equation is quadratic, substitution is the only option — you can't "eliminate" an $x^2$ by adding a linear equation.

$$y = x + 1 \quad \text{①} \qquad x^2 + y^2 = 25 \quad \text{②}$$

Substitute ① into ②: $x^2 + (x+1)^2 = 25 \;\Rightarrow\; 2x^2 + 2x - 24 = 0 \;\Rightarrow\; x^2 + x - 12 = 0$

$(x+4)(x-3) = 0$, so $x = -4, y = -3$ or $x = 3, y = 4$.

Geometrically: a line crossing a circle gives (at most) two intersection points. This connects directly to [[Quadratic Equations]] — the substitution always produces a quadratic.

---

## Common Mistakes

1. **Sign error when subtracting equations.** Subtracting $5x - 3y = 9$ means subtracting *every* term: $-(5x) - (-3y) = -(9)$. The double negative on $-3y$ catches many students.
2. **Forgetting to find both variables.** Finding $x = 3$ and stopping — you must back-substitute to find $y$ too.
3. **Non-linear: forgetting to find the matching $y$ for each $x$.** Two $x$-values means two $(x,y)$ pairs, not mixing and matching.

---

## Exam Notes

### OxAQA 9260 / Cambridge 0580

**Syllabus ref:** A21 (9260) / E2.8 (0580) — linear simultaneous equations. A22 (9260 Extension) — one linear, one non-linear. Expect 3–5 marks. For non-linear, the mark scheme typically gives 1 mark for correct substitution, 1 for simplifying to a quadratic, 1–2 for solving, 1 for both coordinate pairs.

---

## Connections

- **Prerequisite:** [[Equation of a Straight Line (Vocab)]] — simultaneous equations = finding where two lines cross
- **Prerequisite:** [[Expanding Brackets (Vocab)]] — needed for substitution into non-linear equations
- **Prerequisite:** [[Factorising (Vocab)]] — solving the resulting quadratic in non-linear problems
- **Leads to:** [[Graphical Inequalities (Vocab)]] — regions defined by multiple inequalities are "simultaneous inequalities"
- **Parallel:** [[Quadratic Equations]] — non-linear simultaneous always reduces to a quadratic
- **Parallel:** [[Matrix]] — in linear algebra, simultaneous equations become $A\mathbf{x} = \mathbf{b}$, solved by $\mathbf{x} = A^{-1}\mathbf{b}$

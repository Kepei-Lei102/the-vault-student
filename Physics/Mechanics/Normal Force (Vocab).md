---
chinese: 法向力 / 支持力 (fǎxiàng lì / zhīchí lì)
prerequisites:
  - "[[Force (Vocab)]]"
  - "[[Vectors]]"
leads_to:
  - "[[Friction (Vocab)]]"
  - "[[Forces and Equilibrium]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/IGCSE-extension
  - level/A-Level
  - curriculum/Cambridge-9709
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9709-4-1
  - syllabus/9702-3-1
  - syllabus/0625-1-5
  - syllabus/IB-Physics-A-2-2
  - syllabus/AP-Physics-1-2-2
  - syllabus/AP-Physics-C-Mech-2-2
  - type/vocabulary
  - notation/N-normal
  - notation/R-reaction
  - misconception/normal-equals-weight
  - misconception/normal-can-be-negative
---

# Normal Force 法向力 / 支持力

## Definition

The **normal force** is the *perpendicular component* of the contact force between two surfaces. It points **away from the surface, into the body resting on it**. Symbol: $N$ (Cambridge style) or $R$ (older A-Level / mechanics convention — for "reaction"). Units: newtons.

The word *normal* here is the geometry sense — **perpendicular** (法向 in Chinese) — not "ordinary." It's the same usage as "normal to a curve" in [[Tangents and Normals]].

### 中文锚点

**法向力 (fǎxiàng lì)** = 接触面**垂直**方向上的分力。
**支持力 (zhīchí lì)** = 同义，强调它"撑住"物体不让它陷进表面。

中文物理通常叫"支持力"，更直观；英文 Cambridge 用 *normal force* 或 *normal contact force*，更准确。两者完全等价。

考试关键：
- 方向**永远垂直于接触面**，**指离表面**
- 大小由**N2 在垂直方向上的方程**决定 — *not* by a fixed formula
- $N \geq 0$ — 表面只能**推**，不能拉

---

## Where Normal Force Comes From

When you place a book on a table, gravity pulls the book down. The book pushes down on the table; by N3, the table pushes back up on the book — that's the normal force. It is *not* an independent force law; it's a *constraint* enforced by the table's solidity.

> [!info] Normal force is a constraint, not a formula
> There is no equation like "$N =$ (some material property) $\times$ (some scenario quantity)." Instead, $N$ is whatever-it-needs-to-be to prevent the body from sinking into the surface. You determine $N$ by **applying N2 in the direction perpendicular to the surface**, often with $a_\perp = 0$ (no acceleration into or out of the surface).
>
> Examples:
> - Book on horizontal table, no other vertical force: $N = mg$.
> - Book on horizontal table with someone pushing down with extra 5 N: $N = mg + 5$.
> - Block on slope inclined at $\theta$, no vertical motion across the slope: $N = mg\cos\theta$. *Not* $mg$.
> - Person in a lift accelerating up at $a$: $N = m(g + a)$. The "apparent weight" you feel.
> - Person at the top of a vertical loop on a roller coaster: $N + mg = m v^2 / r$, so $N = m v^2 / r - mg$. Can be small or zero — *zero* is the "feeling weightless" case.

The lesson: **don't memorise $N$ as a formula. Solve for it.**

---

## Exam-Language Notes

**Where the boards use this language:** 9709 Paper 4 owns the idiom — "smooth", "the reaction $R$", and the $N = 0$ leaving-contact move are all §4.1/§4.4 mechanics phrasing. Neither 9702 nor 0625 ever *names* the normal contact force in a learning outcome (0625 §1.5 names friction and drag but not this force; on both physics boards it simply appears, unannounced, in free-body work) — so treat the decoding below as 9709-first, physics-useful. AP and IB label it freely on free-body diagrams ($F_N$ or $N$) without the Cambridge adjectives.

**"On a horizontal surface"** — the normal points vertically up; $N$ balances $mg$ unless other forces have vertical components.

**"On a smooth slope inclined at $\theta$"** — *smooth* means **frictionless**. $N$ points **perpendicular to the slope** (not vertically). On a slope at angle $\theta$, $N = mg\cos\theta$ when the body has no acceleration perpendicular to the slope. (Diagonal weight resolves into $mg\sin\theta$ along the slope and $mg\cos\theta$ into the slope; $N$ balances the latter.)

**"The reaction at the surface is $R$"** — older Cambridge / IB phrasing. *Reaction* here means *normal contact force*, *not* the N3 partner of every force. (Confusingly, the word "reaction" is overloaded — see the warning below.)

**"The contact between the surfaces is broken"** — $N = 0$ at that instant. This is how Cambridge phrases the moment a body leaves a slope or a ball loses contact at the top of a loop. Solve for the velocity that makes $N = 0$.

> [!warning] "Reaction force" — *which* reaction?
> The phrase "reaction force" is dangerously ambiguous in English physics. It can mean:
> 1. **The normal contact force** $R$ (older Cambridge / IB usage).
> 2. **The Newton's-3rd-law partner** of any force (the standard modern usage).
>
> When a question says "find the reaction at the wall," it almost always means meaning (1) — the normal force from the wall on the body. When a discussion says "the reaction to gravity is the body's pull on Earth," it means meaning (2). Read the context.

> [!warning] $N$ can never be negative — *with the convention "outward from the surface is positive"*
> The surface can only **push** the body, not pull it. If your N2-equation says $N < 0$, the body has *already left the surface* — go back and re-solve as a body in free flight (no surface contact, no normal force).
>
> The non-negative inequality $N \geq 0$ is a statement *given a sign convention* — that we've chosen the direction *outward from the surface, into the body* as positive (the same direction the normal force itself acts). If you happen to write your N2 equation with the opposite convention (positive = *into* the surface, e.g. taking *downward* as positive on a horizontal surface), the inequality flips: $N \leq 0$. The physics doesn't change — what changes is which sign means "the surface is still in contact."
>
> Best habit: pick the convention "positive = outward from the surface" up-front, and the rule $N \geq 0$ is then guaranteed. Cambridge mark schemes assume this convention without stating it.

---

## Connections

- **Prerequisite:** [[Force (Vocab)]] — normal is one named force in the cast.
- **Prerequisite:** [[Vectors]] — perpendicular component, vector decomposition.
- **Component:** [[Friction (Vocab)]] — friction's *limiting* magnitude is proportional to $N$, via $F_{\max} = \mu R$. Hence the standard split of contact force into a normal piece + a friction piece.
- **Application:** [[Forces and Equilibrium]] — the perpendicular-resolution equation that determines $N$ is half of every "block on slope" problem.
- **Application:** [[Newton's Laws of Motion]] — N3: the body pushes the surface with force $N$, and the surface pushes back with the same $N$.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $N$ | `N` | Normal force (Cambridge modern); risk of clash with the unit "newton" — use $\text{N}$ for the unit |
| $R$ | `R` | Older Cambridge / IB notation for the same quantity ("reaction") |
| $N = mg\cos\theta$ | `N = mg\cos\theta` | Standard inclined-plane result |

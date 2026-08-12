---
chinese: 力 (lì)
prerequisites:
  - "[[Vectors]]"
leads_to:
  - "[[Newton's Laws of Motion]]"
  - "[[Tension (Vocab)]]"
  - "[[Normal Force (Vocab)]]"
  - "[[Friction (Vocab)]]"
  - "[[Forces and Equilibrium]]"
  - "[[Work, Energy and Power]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/IGCSE
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
  - syllabus/9709-4-4
  - syllabus/9702-1-4
  - syllabus/9702-3-1
  - syllabus/9702-3-2
  - syllabus/0625-1-5
  - syllabus/IB-Physics-A-2-1
  - syllabus/IB-Physics-A-2-2
  - syllabus/AP-Physics-1-2-1
  - syllabus/AP-Physics-1-2-2
  - syllabus/AP-Physics-C-Mech-2-1
  - syllabus/AP-Physics-C-Mech-2-2
  - type/vocabulary
  - notation/F-bold
  - notation/Newton-N
---

# Force 力

## Definition

A **force** is a *push* or a *pull* that one body exerts on another. It is a **vector** — it has both magnitude (size) and direction. The SI unit is the **newton (N)**, defined by Newton's 2nd law as $1 \text{ N} = 1 \text{ kg} \cdot 1 \text{ m/s}^2$ — *the force needed to accelerate a 1 kg mass at 1 m/s².*

In English exam-language, forces are referred to by the *type* — gravity, normal, friction, tension, applied, drag, thrust — rather than by symbol alone. Each name is a hint about *which* body produces the force and *how* it acts. See [[Newton's Laws of Motion]] for the conceptual framework, and [[Forces and Equilibrium]] for the technique of summing forces on a body.

### 中文锚点

**力 (lì)** = push 或 pull，是一个**矢量** (vector)，单位 **牛顿 (Newton, N)**，$1 \text{ N} = 1 \text{ kg} \cdot 1 \text{ m/s}^2$。

中文物理已经把"力"讲得很透彻 — 这张卡片的目标是建立**英文考试词汇**（每种力的英文名称、产生它的物体、作用方式），以及一些 Cambridge 答题里特定的句式。

---

## The Cast of Forces — Names You Need on Paper

| English | 中文 | Symbol | Source body | Direction |
|---|---|---|---|---|
| Weight / gravitational force | 重力 (zhònglì) | $W = mg$ | Earth (or other massive body) | Vertically downward |
| Normal (contact) force | 法向力 / 支持力 | $N$ or $R$ | Surface in contact | Perpendicular to surface, *away* from it |
| Friction | 摩擦力 (mócā lì) | $f$ or $F_r$ | Surface in contact | Along surface, opposing (relative) motion |
| Tension | 张力 (zhānglì) | $T$ | A taut rope or string | Along the rope, *pulling* the body toward the rope |
| Thrust | 推力 (tuīlì) | $T$ (sometimes) | A rigid rod or engine | Along the rod, *pushing* the body |
| Drag / air resistance | 阻力 / 空气阻力 (zǔlì / kōngqì zǔlì) | $D$ | The air or fluid | Opposite to the body's velocity |
| Applied force | 外加力 (wàijiā lì) | $F_{\text{app}}$ | Anything external (a hand, a spring, a magnet) | As specified in the question |

Notice the symbol $T$ pulls double duty between **tension** and **thrust** — context disambiguates. *Tension pulls; thrust pushes.* See [[Tension (Vocab)]].

The first four — weight, normal, friction, tension — show up on almost every Cambridge mechanics question. The remaining three appear when the scenario specifies them.

---

## Exam-Language Notes

**"Calculate the resultant force"** — find the *vector sum* of all forces acting on the body. *Resultant* (合力, hélì) is the standard Cambridge term; "net force" means the same thing.

**"Resolve the force into components"** — decompose the vector into perpendicular pieces, usually horizontal/vertical or along/perpendicular to a slope. See [[Vectors]] for the technique.

**"The body is acted on by a force of 30 N"** — passive voice, common in physics English. "is acted on by" = "受 ... 的作用". Equivalent to "a force of 30 N acts on the body."

**"The forces are in equilibrium"** — $\Sigma \mathbf{F} = \mathbf{0}$. The vector sum is zero, and equivalently the body has zero acceleration. See [[Forces and Equilibrium]].

**Board scope.** This vocabulary is universal: 9709 P4 computes with it (resultants, resolution, equilibrium), 9702 §3 uses it in free-body language, 0625 §1.5 states resultant force qualitatively at Core and computes at Extended; IB and AP phrase it identically.

> [!warning] Force is *always* a vector
> A common slip in English-medium exams is to add force *magnitudes* algebraically when forces aren't collinear. Two 10 N forces at right angles to each other have a *resultant* of $\sqrt{200} \approx 14.1$ N, not 20 N. Always resolve into components first, then add.

---

## Connections

- **Prerequisite:** [[Vectors]] — force is the canonical vector quantity in physics; resolution into components uses the maths-side techniques.
- **Component:** [[Tension (Vocab)]], [[Normal Force (Vocab)]], [[Friction (Vocab)]] — the three contact-related forces, each with its own card.
- **Component:** [[Weight (Vocab)]] — $W = mg$ is the gravitational force; covered in detail inside [[Newton's Laws of Motion]].
- **Application:** [[Newton's Laws of Motion]] — N1 says "no resultant force → no acceleration"; N2 *defines* force operationally as $\mathbf{F} = m\mathbf{a}$; N3 says forces come in pairs.
- **Application:** [[Forces and Equilibrium]] — the technique of summing forces on a body; force diagrams; resolution.
- **Application:** [[Linear Momentum]] — force as the rate of change of momentum, $\mathbf{F} = d\mathbf{p}/dt$.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\mathbf{F}$ | `\mathbf{F}` | Force as a vector |
| $F$ | `F` | Magnitude / 1D scalar component |
| $\Sigma \mathbf{F}$ | `\Sigma \mathbf{F}` | Resultant force |
| $\mathbf{F}_{\text{net}}$ | `\mathbf{F}_{\text{net}}` | Same as resultant |
| $W = mg$ | `W = mg` | Weight |
| $1 \text{ N}$ | `1 \text{ N}` | One newton (use `\text{}` to keep "N" upright) |

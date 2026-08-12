---
chinese: 张力 (zhānglì)
prerequisites:
  - "[[Force (Vocab)]]"
  - "[[Newton's Laws of Motion]]"
leads_to:
  - "[[Forces and Equilibrium]]"
  - "[[Connected Particles]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/IGCSE-extension
  - level/A-Level
  - curriculum/Cambridge-9709
  - curriculum/Cambridge-9702
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9709-4-4
  - syllabus/9702-3-1
  - syllabus/IB-Physics-A-2-2
  - syllabus/AP-Physics-1-2-2
  - syllabus/AP-Physics-C-Mech-2-2
  - type/vocabulary
  - notation/T-tension
  - misconception/tension-pushes
  - misconception/tension-differs-along-rope
---

# Tension 张力

## Definition

**Tension** is the pulling force a taut rope, string, cable, or wire exerts on a body attached to it. It acts *along the line of the rope*, *pulling the body toward the rope*. The symbol is usually $T$. Units: newtons.

A rope can never *push* — only pull. If two bodies are connected by a rope and you try to push them together, the rope just goes slack. ("Push the wet noodle" — wet noodles cannot transmit thrust.) The corresponding push-along-a-rod force is called **thrust**.

### 中文锚点

**张力 (zhānglì)** = 沿绳方向**拉**着物体的力。

中文物理里"张力"和英文 tension 完全对应。这张卡片要交代的，是 Cambridge 题目里两个**简化假设**的英文措辞，以及一个常见的英文理解陷阱。

---

## The "Light Inextensible String" Idiom — Decoded

This phrase shows up on virtually every connected-particles question. Each adjective is a separate physical assumption:

| Phrase | 中文 | What it really means | Why it matters |
|---|---|---|---|
| **light** | 轻 (无质量) | The string has zero mass | $T$ is the **same** at every point along the rope. Otherwise N2 on the rope itself would demand different tensions at different points. |
| **inextensible** | 不可伸长 | The string's length cannot change | Two bodies connected to it have the **same speed and the same magnitude of acceleration** at every instant. |
| **string** | 绳 (柔性) | Cannot transmit thrust | Tension is positive only — never negative. (For "rigid rod" replace with [[Rod (Vocab)]]; rods can transmit both tension *and* thrust.) |

> [!tip] The two assumptions you actually use
> When solving an exam question, the "light inextensible string" phrase reduces to **two equations** in your worked solution:
> 1. $T_1 = T_2 = \dots = T$ (same tension throughout — from "light")
> 2. $\lvert a_1 \rvert = \lvert a_2 \rvert = a$ (same magnitude of acceleration — from "inextensible")
> 
> If a question instead says "**heavy chain**" or "**elastic spring**," at least one of these breaks. Read the assumption phrase carefully — it tells you which equations you can write.

---

## Tension is from Newton's 3rd Law

A rope under tension pulls *both* of its endpoints inward with the same magnitude. The two pulling-forces (one on body A at one end, one on body B at the other) are the **N3 partner pair** of the rope's response to being stretched. This is why tension appears in the same magnitude in both bodies' free-body diagrams. See [[Newton's Laws of Motion]].

In a connected-particles problem the forces on the two masses by the rope are *equal in magnitude, opposite in direction* — exactly N3. The bookkeeping cancellation that makes "add the equations" work in pulley problems comes from this.

---

## Exam-Language Notes

**Where the boards use this language:** 9709 Paper 4 owns the idiom — the "light inextensible string" phrasing lives in the §4.4 Newton's-laws problem family (connected particles, pulleys, pegs). On 9702 the *word* tension never appears in a learning outcome: it arrives unannounced inside dynamics problems (§3.1) and resurfaces as *tensile* forces in §6.1's stress–strain vocabulary — so treat this card's decoding as 9709-first, 9702-useful. AP and IB use "tension" freely in free-body labelling with none of the Cambridge adjectives.

**"A light inextensible string passing over a smooth peg"** — the standard Cambridge setup. *Smooth* means **frictionless**, so the rope changes direction at the peg without losing tension. Same $T$ on both sides.

**"The string remains taut"** — necessary for tension to exist at all. If the question lets the string go slack, $T = 0$ and the bodies decouple.

**"The maximum tension before the string breaks is 50 N"** — set up the equations as usual, solve for $T$, and check $T < 50$. Beyond the break-point, the system separates and you re-solve as two free bodies.

**"Tension in the rod is …"** — when a rod replaces a rope, $T$ can be **negative**, meaning the rod is in **thrust** (compression) rather than tension. Cambridge sometimes asks for the *signed* tension and "find when the rod is in compression" (= when $T < 0$).

> [!warning] Tension does not differ along a light rope
> Drawing one $T$ at one end of a rope and a different $T'$ at the other is a common mistake. The "light" assumption *forces* them equal. (For a heavy rope — a rope with mass — they would differ; that's why the assumption is stated.)

---

## Connections

- **Prerequisite:** [[Force (Vocab)]] — tension is one of the named forces.
- **Prerequisite:** [[Newton's Laws of Motion]] — N3 explains why both ends of the rope feel equal-and-opposite pulls.
- **Application:** [[Forces and Equilibrium]] — tension as a force in resolution / equilibrium problems.
- **Application:** [[Connected Particles]] — pulley problems, masses on inclines connected by a rope, the "add the equations" trick.
- **Sibling:** [[Thrust (Vocab)]] — the corresponding force in a rigid rod, which can also push.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $T$ | `T` | Tension magnitude |
| $T_1, T_2$ | `T_1, T_2` | Tensions in different rope segments (e.g. either side of a pulley); for a *light* rope these are equal |

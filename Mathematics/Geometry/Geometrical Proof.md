---
chinese: 几何证明 (jǐhé zhèngmíng)
prerequisites:
  - "[[Chain of Thought]]"
  - "[[Logic]]"
  - "[[Angle Properties (Vocab)]]"
  - "[[Angles in Parallel Lines (Vocab)]]"
  - "[[Polygon Angles (Vocab)]]"
  - "[[Triangles (Vocab)]]"
  - "[[Pythagoras Theorem]]"
  - "[[Congruence]]"
  - "[[Similarity]]"
  - "[[Circle Theorems I]]"
  - "[[Circle Theorems II]]"
  - "[[Algebraic Proof]]"
leads_to:
  - "[[Vectors]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/problem-solving
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/A-Level
  - syllabus/9260-G9
  - type/proof
  - type/methodology
  - type/exam-technique
  - misconception/circular-reasoning
  - misconception/missing-reasons
  - misconception/assuming-the-diagram
---

# Geometrical Proof 几何证明

## Definition

### Formal

A **geometrical proof** is a finite sequence of statements about a geometric figure, in which each statement is either given, a standard definition, a standard theorem, or follows from earlier statements by a rule of inference, and the final statement is the required result.

Every line has two parts:
$$\underbrace{\text{Statement}}_{\text{what is true}} \qquad \underbrace{\text{(Reason)}}_{\text{why it is true}}$$

No statement in a geometrical proof is allowed to stand without a reason. *"It looks like it"* is never a reason — the diagram shows **one example**, not the general case.

### Intuitive — Assembling Tools from a Toolbox

You already own the tools. Pythagoras, angle-sum, parallel-line angles, polygon angles, congruence (SSS/SAS/ASA/RHS), similarity (AA/SSS/SAS), and the circle theorems are all results you have *proved* in their own cards. A geometrical proof is what happens when you **pick up several of those tools and combine them** to establish something new.

The skill is not in any single theorem — each individual theorem is small. The skill is in the **chaining**: noticing that "I know two angles are equal (same segment), and two sides are shared (common side), therefore SAS gives me a congruence, therefore a third side equals a fourth side." Each link is trivial; the chain is not.

### 中文锚点 (Chinese Anchor)

几何证明在中国数学教育里从初中阶段就反复训练，学生对**已知 → 求证 → 证明**的结构极其熟悉。OxAQA 9260 G9 Ext 要的正是这种结构，只是用英文表达 — 这是学生最容易得满分的题型之一，**只要把理由用英文说对**。

| 中文 | English | Usage |
|------|---------|-------|
| 已知 (yǐ zhī) | Given | The hypotheses — what the question tells you |
| 求证 (qiúzhèng) | To prove / Required to prove | The target — what you must establish |
| 证明 (zhèngmíng) | Proof | The body of logical steps |
| 证毕 (zhèng bì) / ∴ / $\blacksquare$ | QED / "as required" | The end marker |
| 理由 (lǐyóu) | Reason / justification | Cited in brackets after each statement |
| 公理 (gōnglǐ) | Axiom | Accepted without proof (e.g. "through any two points there is exactly one line") |
| 定理 (dìnglǐ) | Theorem | Proved result you may cite (e.g. "angles on a straight line sum to $180°$") |
| 推论 (tuīlùn) | Corollary | A direct consequence of a theorem (e.g. "angles in a semicircle = $90°$" is a corollary of the angle-at-centre theorem) |

The template is the same in both languages. The vocabulary to learn is **English reason-phrasing**, not the proof skeleton.

## Anatomy of a Geometrical Proof

Every geometrical proof in an exam answer sheet has four parts:

| Part | 中文 | What goes here |
|------|------|----------------|
| **Given** | 已知 | Restate the information from the question. Label the diagram. |
| **To prove** | 求证 | Restate the target statement in your own words. |
| **Proof** | 证明 | Numbered or sequenced statements, each with a reason. |
| **QED marker** | 证毕 | $\blacksquare$, $\square$, "as required", or "$\therefore$ [target]". |

> [!tip] The first move is always "label the diagram"
> Before writing any statement, put every letter the question gives you onto the diagram. Mark given equal sides with tick marks, equal angles with arcs, right angles with the square symbol, and parallel lines with matching arrows. Half of geometry proof is done when the diagram is fully labelled — you can literally *see* which tool applies.

## The Theorem Toolkit

These are the results you are allowed to cite *without re-proving them*. Anything you use outside this list must be derived inline.

### Angle facts

| Theorem | Reason phrase (to write in exam) |
|---------|----------------------------------|
| Angles on a straight line sum to $180°$ | *angles on a straight line* |
| Angles at a point sum to $360°$ | *angles at a point* |
| Vertically opposite angles are equal | *vertically opposite angles* |
| Angles in a triangle sum to $180°$ | *angle sum of triangle* |
| Exterior angle of a triangle = sum of opposite interior angles | *exterior angle of triangle* |
| Base angles of an isosceles triangle are equal | *base angles of isosceles triangle* |
| All three angles of an equilateral triangle are $60°$ | *angles of equilateral triangle* |

### Parallel lines — needs $\parallel$ marked on diagram

| Theorem | Reason phrase |
|---------|---------------|
| Corresponding angles are equal | *corresponding angles, lines parallel* |
| Alternate angles are equal | *alternate angles, lines parallel* |
| Co-interior (allied) angles sum to $180°$ | *co-interior angles, lines parallel* |

### Polygon angles

| Theorem | Reason phrase |
|---------|---------------|
| Sum of interior angles of an $n$-gon = $(n-2) \times 180°$ | *interior angle sum of $n$-gon* |
| Sum of exterior angles of any polygon = $360°$ | *exterior angle sum = $360°$* |

### Triangle congruence — use to prove equal lengths/angles

| Condition | Reason phrase | Requirement |
|-----------|---------------|-------------|
| SSS | *SSS* | Three sides equal |
| SAS | *SAS* | Two sides and *included* angle equal |
| ASA / AAS | *ASA* | Two angles and any side equal |
| RHS | *RHS* | Right angle, hypotenuse, one other side |

After citing one of these, write **"corresponding sides/angles of congruent triangles"** (often abbreviated **CPCTC**) to extract the equal parts you wanted.

### Triangle similarity — use to prove ratios

| Condition | Reason phrase |
|-----------|---------------|
| AA | *AA similarity* |
| SSS (ratio) | *SSS similarity* |
| SAS (ratio) | *SAS similarity* |

After citing, write **"corresponding sides of similar triangles are in ratio"** to set up the equation $\dfrac{a}{a'} = \dfrac{b}{b'} = \dfrac{c}{c'}$.

### Circle theorems — needs a circle in the figure

| Theorem | Reason phrase |
|---------|---------------|
| Angle at centre = $2 \times$ angle at circumference | *angle at centre* |
| Angle in a semicircle = $90°$ | *angle in semicircle* |
| Angles in the same segment are equal | *same segment* |
| Opposite angles of a cyclic quadrilateral sum to $180°$ | *cyclic quadrilateral* |
| Tangent ⊥ radius at point of contact | *tangent perpendicular to radius* |
| Two tangents from an external point are equal | *tangents from external point* |
| Perpendicular from centre bisects a chord | *perpendicular from centre to chord* |
| Alternate segment theorem | *alternate segment theorem* |

### Pythagoras and its converse

| Theorem | Reason phrase |
|---------|---------------|
| In a right-angled triangle, $a^2 + b^2 = c^2$ | *Pythagoras* |
| If $a^2 + b^2 = c^2$, the triangle is right-angled at the vertex opposite $c$ | *converse of Pythagoras* |

## How to Phrase Reasons

The reason written in brackets must be **short, specific, and name the theorem**.

| ✅ Good | ❌ Bad | Why |
|---------|--------|-----|
| *angles in same segment* | *because they are equal* | No theorem named |
| *angle sum of triangle* | *$180°$* | States a fact, not a reason |
| *common side $AC$* | *they share a side* | Vague; doesn't name the side |
| *SAS* | *because two sides and an angle match* | Condition unnamed |
| *corresponding angles, $AB \parallel CD$* | *alternate angles* | Wrong theorem name |
| *vertically opposite angles* | *opposite angles* | "Opposite" alone is ambiguous (could mean cyclic quadrilateral) |

> [!warning] "Given" is a valid reason — but only once per fact
> The first time you use a fact from the question, write "(given)". After that, if you re-use it further down, write the fact name itself (e.g., "since $AB = CD$ from line 1"). Do not write "(given)" for a fact the question did not actually give you.

## Signal Words — the Glue of the Chain

| English signal | 中文 | Used when |
|----------------|------|-----------|
| Since / Because | 因为 / 由于 | Citing a reason before a deduction |
| Therefore / Hence / $\therefore$ | 因此 / 所以 | Stating a consequence |
| Also / Furthermore | 另外 / 又 | Adding a parallel fact |
| But | 但是 | Noting a contrast or bringing together two facts about to be combined |
| Now consider | 现考虑 | Switching the subject of attention (e.g. to a new triangle) |
| As required / Q.E.D. | 如题所证 | Final line |

## Standard Proof Patterns

### Pattern 1 — Angle chase

Given a figure with several angles, chain angle facts and parallel-line rules to find the target angle.

**Skeleton:**
1. Start from a given angle.
2. Use one angle fact (straight line, triangle, parallel, circle) to deduce the next angle.
3. Chain until you reach the target.
4. State the final answer with its reason.

### Pattern 2 — Prove lengths (or angles) equal via congruence

**Skeleton:**
1. *"Consider triangles $\triangle XYZ$ and $\triangle X'Y'Z'$."*
2. List three equalities in a vertical stack, each with a reason.
3. *"By [SSS / SAS / ASA / RHS], $\triangle XYZ \cong \triangle X'Y'Z'$."*
4. *"Therefore [target equality]  (corresponding parts of congruent triangles)."*

### Pattern 3 — Prove a ratio via similarity

**Skeleton:**
1. *"Consider triangles $\triangle XYZ$ and $\triangle X'Y'Z'$."*
2. State two equal angles with reasons (usually: common angle + one from parallel lines or same segment).
3. *"By AA, $\triangle XYZ \sim \triangle X'Y'Z'$."*
4. *"Therefore $\dfrac{XY}{X'Y'} = \dfrac{YZ}{Y'Z'} = \dfrac{XZ}{X'Z'}$ (corresponding sides of similar triangles)."*
5. Solve the resulting equation for the required length or ratio.

### Pattern 4 — Circle-theorem chain

Typical when the figure contains a circle and several chords/tangents.

**Skeleton:**
1. Identify the configuration (which circle theorem does the figure trigger?).
2. State the relevant equal angle with reason (*same segment*, *angle at centre*, etc.).
3. If the target is another angle, use step 2's equality to unlock the angle chase.
4. If the target is a congruence/similarity, use step 2's equal angles as ingredients for AA similarity.

> [!tip] The two-triangle trick in circle problems
> A very common 9260 question shows two triangles sharing an angle inside a circle. Look for:
> - A **common angle** at a vertex (both triangles share it).
> - A pair of **same-segment** equal angles.
>
> Two equal angle pairs → AA → similar triangles → ratio equation. This pattern unlocks most "Show that $AB \cdot CD = \ldots$" circle problems.

## Worked Examples

### Example 1 (9260 level) — Multi-step angle chase

> In the diagram, $AB \parallel DE$ and $BC = CD$. Given $\angle ABC = 70°$, find $\angle BCD$, giving reasons.

![[geometrical-proof-example-1.svg]]

**Proof.**

$\angle BDC = 70°$ *(alternate angles, $AB \parallel DE$, transversal $BD$)*.

In $\triangle BCD$, since $BC = CD$, the triangle is isosceles with base angles at $B$ and $D$:

$\angle DBC = \angle BDC = 70°$ *(base angles of isosceles triangle)*.

$\angle BCD = 180° - 70° - 70° = 40°$ *(angle sum of triangle)*.

$\therefore \boxed{\angle BCD = 40°}.$ $\blacksquare$

**Why this is the 9260 archetype angle chase.** Three theorems (alternate angles, isosceles base angles, angle sum) chain in four lines. Each line cites exactly one theorem.

---

### Example 2 (9260 level) — Congruence proof

> In the diagram, $ABCD$ is a parallelogram with diagonals meeting at $M$. Prove that $M$ is the midpoint of $AC$ and of $BD$.

![[geometrical-proof-example-2.svg]]

**Given.** $ABCD$ is a parallelogram, so $AB \parallel DC$ and $AB = DC$. Diagonals $AC$ and $BD$ meet at $M$.

**To prove.** $AM = MC$ and $BM = MD$.

**Proof.** Consider $\triangle ABM$ and $\triangle CDM$:

- $AB = CD$ *(given, opposite sides of parallelogram)*
- $\angle ABM = \angle CDM$ *(alternate angles, $AB \parallel DC$, transversal $BD$)*
- $\angle BAM = \angle DCM$ *(alternate angles, $AB \parallel DC$, transversal $AC$)*

By **ASA**, $\triangle ABM \cong \triangle CDM$.

$\therefore AM = CM$ and $BM = DM$ *(corresponding sides of congruent triangles)*.

$\therefore M$ bisects both diagonals. $\blacksquare$

---

### Example 3 (9260 Ext) — Similarity for a length

> Chords $AB$ and $CD$ of a circle intersect at a point $P$ inside the circle. Prove that $PA \cdot PB = PC \cdot PD$. *(This is the "intersecting chords" theorem — power of a point.)*

![[geometrical-proof-example-3.svg]]

**Given.** Chords $AB$ and $CD$ meet at $P$ inside the circle.

**To prove.** $PA \cdot PB = PC \cdot PD$.

**Proof.** Consider $\triangle PAC$ and $\triangle PDB$:

- $\angle APC = \angle DPB$ *(vertically opposite angles)*
- $\angle PAC = \angle PDB$ *(angles in the same segment subtended by arc $BC$)*

By **AA**, $\triangle PAC \sim \triangle PDB$.

$\therefore \dfrac{PA}{PD} = \dfrac{PC}{PB}$ *(corresponding sides of similar triangles)*.

Cross-multiplying: $PA \cdot PB = PC \cdot PD$. $\blacksquare$

**Why this example is the 9260 archetype.** Two pairs of equal angles (one vertical, one same-segment) → AA similarity → ratio → multiplication. This three-move pattern appears in almost every "prove that [product of lengths] = [product of lengths]" question.

---

### Example 4 (9260 Ext) — Circle theorem chain

> $ABCD$ is a cyclic quadrilateral. The tangent at $A$ makes an angle of $\theta$ with chord $AB$. Prove that $\angle ADB = \theta$.

![[geometrical-proof-example-4.svg]]

**Given.** $A, B, C, D$ lie on a circle; line $AT$ is tangent at $A$; $\angle TAB = \theta$.

**To prove.** $\angle ADB = \theta$.

**Proof.** By the alternate segment theorem, the angle between a tangent and a chord equals the angle in the alternate segment. The chord $AB$ divides the circle into two segments; $D$ lies in the segment *opposite* to the tangent, so the angle in the alternate segment is $\angle ADB$.

$\therefore \angle ADB = \theta$ *(alternate segment theorem)*. $\blacksquare$

**One-line proof** — and that is the point. Once the student has the alternate segment theorem in their toolkit, this "impossible-looking" result collapses to a single sentence.

---

### Example 5 (A-Level style) — Proving perpendicularity

> $ABC$ is a triangle with $AB = AC$. The perpendicular bisector of $BC$ meets $BC$ at $M$. Prove that $AM \perp BC$ (i.e. $AM$ is perpendicular to $BC$).

![[geometrical-proof-example-5.svg]]

**Given.** $AB = AC$; $M$ is the midpoint of $BC$.

**To prove.** $\angle AMB = 90°$.

**Proof.** Consider $\triangle AMB$ and $\triangle AMC$:

- $AB = AC$ *(given)*
- $AM = AM$ *(common side)*
- $BM = CM$ *($M$ is midpoint of $BC$)*

By **SSS**, $\triangle AMB \cong \triangle AMC$.

$\therefore \angle AMB = \angle AMC$ *(corresponding angles of congruent triangles)*.

But $\angle AMB + \angle AMC = 180°$ *(angles on a straight line)*.

$\therefore 2 \angle AMB = 180°$, so $\angle AMB = 90°$. Thus $AM \perp BC$. $\blacksquare$

## Common Misconceptions (Teaching Notes)

### 1. "Assuming the diagram"

**Wrong:** The student writes "$\angle A = \angle B$ because they look equal in the figure." The mark scheme treats this as *zero* — the diagram shows one instance, not a general truth.

**Fix:** Drill the rule: *a fact is true in a proof only if (a) the question gives it, (b) a theorem forces it, or (c) an earlier line of your proof established it*. "It looks equal" is never one of the three.

### 2. Skipping reasons

**Wrong:** The student writes a chain of equalities with no justifications:
$$\angle 1 = 70°, \quad \angle 2 = 70°, \quad \angle 3 = 40°, \quad \angle 4 = 40°.$$

**Why it fails:** Each line is worth a method mark *conditional on the reason being stated*. Mark schemes award 0 for an unreasoned correct answer to a "prove" question.

**Fix:** One line = one statement + one reason. If the reason won't fit on the same line, put it in brackets at the end, or on the next line indented.

### 3. Circular reasoning

**Wrong:** In a "prove $\triangle ABC \cong \triangle DEF$" question, the student writes "$AB = DE$ because the triangles are congruent."

**Why it's circular:** The target of the proof is *being assumed* to justify a step in the proof. The chain must flow from the given information to the target, never the other way.

**Fix:** Highlight the target at the top of the working. Any step that uses the target as a reason is a red flag.

### 4. Wrong vertex order in congruence statement

**Wrong:** The student writes "$\triangle ABC \cong \triangle EDF$" meaning $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$. The statement now asserts six wrong equalities.

**Fix:** (See [[Congruence]] for the colour-coded diagram.) Before writing $\triangle \square \cong \triangle \square$, write the correspondence as pairs: $A \to D$, $B \to E$, $C \to F$. Then order the letters of the second triangle to match.

### 5. Using the target in a "Prove" question

**Wrong:** For *"Prove that $AB \cdot CD = AE \cdot CF$"*, the student substitutes the known lengths and shows both sides equal numerically.

**Why it fails:** This proves the statement in one specific case, not in general. The proof must use variables and theorem-chaining — not numerical substitution (unless the question says "verify").

**Fix:** The word **"prove"** means "in all cases consistent with the given information." If your argument uses specific numbers, stop and rewrite in letters.

### 6. Confusing congruence reasons with similarity reasons

**Wrong:** "$\triangle ABC \sim \triangle DEF$ by **SAS**" — but SAS for similarity needs two sides in **ratio** and the included angle equal, not two sides equal.

**Fix:** Keep two vocabulary columns in mind:
- *Congruence*: equal sides + equal angles → *SSS, SAS, ASA, RHS*.
- *Similarity*: sides in **ratio** + equal angles → *AA, SSS similarity, SAS similarity*.

## Exam Notes

### OxAQA 9260

**Syllabus reference:** G9 Extension — *use standard theorems to justify results in geometric contexts*.

This is a **9260-unique** topic — Cambridge 0580 does not examine formal geometrical proof. Typical G9 Ext question types:

1. **Angle chase with reasons** (3–4 marks) — Find an angle via a chain of 2–4 angle facts; every step must cite its theorem.
2. **Congruence proof** (4–5 marks) — Prove two triangles are congruent, then use CPCTC to deduce an equal length or angle (follows the [[Congruence]] four-line skeleton).
3. **Similarity for a ratio** (4–5 marks) — Identify AA via shared angle + same-segment/parallel, then extract the ratio.
4. **Circle theorem chain** (5–6 marks) — Multi-step problem requiring two or three circle theorems in sequence.

**Mark allocation pattern.** One mark each for: identifying the correct theorem, stating the fact, giving the reason, and reaching the conclusion. Out of 5 marks, 3 are method marks awarded for the chain itself — only 2 depend on arithmetic accuracy.

**9260 quirk — "quality of written communication" marks.** Some G9 questions allocate up to 1 QWC mark for clear English reason-phrasing. This is a free mark for students who consistently write reasons in clipped exam English (*"angles on a straight line"* rather than *"because these angles sum to 180 since they lie on a line"*).

### Cambridge 0580 Extended

**Not formally examined.** 0580 tests *applying* geometry (finding angles, lengths) but does not require formal proof write-ups. A student moving from 0580 to 9260 has a large gap here — they need explicit teaching on reason-phrasing and the proof skeleton.

### Cambridge 0606

**Geometry is a small component.** 0606 does not have a standalone proof unit; geometric reasoning shows up implicitly in coordinate geometry (1) and vectors (10), but without the Given/To prove/Proof format.

### A-Level

A-Level Pure uses geometrical reasoning inside:
- **Circle in coordinate geometry** — proving properties of tangents, chords, and circle equations.
- **Vectors (A-Level Core)** — proving midpoint theorems, concurrency, collinearity via vector methods instead of classical congruence.
- **Further Pure (Further Maths)** — rigorous Euclidean geometry in some optional modules.

The proof skeleton from 9260 G9 transfers directly; only the toolkit expands.

### IB AA / AI

At IB SL, geometric proof appears in the Geometry and Trigonometry topic via coordinate and trigonometric methods rather than classical Euclidean theorems. At HL, the optional "Geometry" topic (when offered) goes deeper into classical proof.

## Worked Strategy — How to Read a Geometrical Proof Question

Before writing a single line, run the following checklist:

1. **Circle the command word.** Is it *Prove*, *Show that*, or *Find*? (See [[Exam Command Words (Vocab)]].)
2. **Label the diagram.** Add every equal side, equal angle, parallel mark, and right angle.
3. **Identify the figure type.** Parallelogram? Cyclic quadrilateral? Isosceles triangle? Each triggers its own toolkit.
4. **Pick the target.** What is the question asking you to establish?
5. **Work backwards.** From the target, ask "what theorem could make this true?" Then ask "what information would that theorem need?"
6. **Match forwards.** Look at the given information and ask "which theorem does this unlock?"
7. **Meet in the middle.** Write the proof forwards from givens to target.

This is [[Chain of Thought]] applied specifically to geometry: the target and the givens are the two banks of the river, and the theorems are the stepping stones.

## Connections

- **Parent:** [[Chain of Thought]] — geometrical proof is one specialised form of logical chain
- **Parent (formal):** [[Logic]] — ⇒, ⇔, and quantifiers underlie every "therefore" in the proof
- **Sibling:** [[Algebraic Proof]] — same skeleton (Given / To prove / Proof), different toolkit
- **Proof ingredient:** [[Pythagoras Theorem]] — the most frequently cited single theorem
- **Proof ingredient:** [[Angle Properties (Vocab)]], [[Angles in Parallel Lines (Vocab)]], [[Polygon Angles (Vocab)]] — the angle toolkit
- **Proof ingredient:** [[Congruence]] — primary tool for proving equal lengths/angles
- **Proof ingredient:** [[Similarity]] — primary tool for proving ratios
- **Proof ingredient:** [[Circle Theorems I]], [[Circle Theorems II]] — circle configurations
- **Language:** [[Exam Command Words (Vocab)\|Exam Command Words]] — distinguishes *Show that* from *Prove*
- **Extension:** [[Vectors]] — vector methods give a second, algebraic route to geometrical proof (9260 Ext, A-Level)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\cong$ | `\cong` | "is congruent to" — same shape AND size |
| $\sim$ | `\sim` | "is similar to" — same shape, possibly different size |
| $\parallel$ | `\parallel` | "is parallel to" |
| $\perp$ | `\perp` | "is perpendicular to" |
| $\angle ABC$ | `\angle ABC` | The angle at vertex $B$ between rays $BA$ and $BC$ |
| $\triangle ABC$ | `\triangle ABC` | The triangle with vertices $A$, $B$, $C$ |
| $\therefore$ | `\therefore` | "therefore" |
| $\because$ | `\because` | "because" |
| $\blacksquare$ | `\blacksquare` | End-of-proof marker (filled square) |
| $\square$ | `\square` | End-of-proof marker (open square, equivalent) |

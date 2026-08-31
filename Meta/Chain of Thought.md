---
chinese: 思维链 (sīwéi liàn) / 解题思路 (jiětí sīlù)
prerequisites:
  - "[[Set]]"
leads_to:
  - "[[Logic]]"
  - "[[Algebraic Proof]]"
  - "[[Geometrical Proof]]"
  - "[[Exam Command Words (Vocab)]]"
  - "[[Laws and Theorems]]"
  - "[[The Feynman Technique]]"
  - "[[Choosing Effective Equations]]"
  - "[[Forward Reading and Problem Discovery]]"
tags:
  - subject/mathematics
  - domain/problem-solving
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - type/methodology
  - type/exam-technique
  - misconception/skipping-steps
  - misconception/technique-without-trigger
---

# Chain of Thought 思维链

## Definition

### Formal

A **chain of thought** is a sequence of logical steps where each step follows from the previous by a known rule, definition, or computation:

$$\text{Given} \xrightarrow{\text{rule 1}} \text{Step 1} \xrightarrow{\text{rule 2}} \text{Step 2} \xrightarrow{\text{rule 3}} \cdots \xrightarrow{\text{rule } n} \text{Conclusion}$$

Each arrow represents a single, justified inference. A chain is **valid** if every arrow is justified. A chain is **complete** if no step requires extra knowledge to verify.

### Intuitive — Building a Bridge

Imagine you're standing on one side of a river (the **given information**) and you need to reach the other side (the **conclusion**). You can't jump — you need to place stepping stones across the water, one at a time, each within reach of the last.

A chain of thought IS those stepping stones. Skip one and you fall in the water. Place each stone carefully and you walk across with confidence.

This matters far beyond exams. When you plan a music show, you chain logistics: venue → equipment → rehearsal schedule → tickets → sound check → performance. When you debug code, you chain hypotheses: "the output is wrong → the loop runs one too many times → the boundary condition is off." When you write a report that other people need to trust, your chain is what lets them verify your reasoning without re-doing your work from scratch. Anywhere that *reliability* and *communication* matter, chain of thought is the tool.

Ironically, exams are where you *abbreviate* the chain — time pressure forces you to skip minor steps, and mark schemes forgive small gaps. Outside exams, the full chain is what separates trustworthy work from guesswork.

Real chains aren't always straight lines. They branch: "**if** the venue is available, book it; **otherwise**, check the backup." They loop: "**while** the error is too large, refine the estimate." This is the *prediction* version of chain of thought — exploring possible futures before committing. In computer science, this branching search is formalized as **Monte Carlo Tree Search** (MCTS): simulate many chains forward, evaluate which branches lead to the best outcome, then choose. Chess engines, Go AI, and planning algorithms all think this way.

![[chain-of-thought-diagram.svg|700]]

> [!info] System 1, System 2, System 3 — Three modes of thinking
> Psychologist Daniel Kahneman (*Thinking, Fast and Slow*, 2011) describes two modes of thought:
>
> - **System 1** — fast, automatic, effortless. Pattern-matching: "I recognise this, the answer is..."
> - **System 2** — slow, deliberate, step-by-step. Reasoning: "Let me work through this carefully..."
>
> A chain of thought is System 2 made visible. System 1 is powerful (experienced mathematicians "see" answers), but it's also where biases and errors hide. Writing the chain forces System 2 to check what System 1 claims — and that's where reliability comes from.
>
> But there's a third mode that neither System 1 nor System 2 covers:
>
> - **System 3** — external validation. Expose your chain to something that isn't you: the market, a peer review, an experiment, a compiler, the laws of physics. System 2 catches *logical* errors; System 3 catches *premise* errors — the assumptions you didn't know you were making.
>
> A proof that compiles in Lean. A business plan that survives contact with customers. A physics prediction that matches the lab data. These are System 3 at work: reality checking what your reasoning claimed.

### 中文锚点 (Chinese Anchor)

思维链：**每一步都有理由，每一步都写出来。**

| 中文 | English | Key idea |
|------|---------|----------|
| 思维链 (sīwéi liàn) | Chain of thought | Step-by-step reasoning, each link justified |
| 解题思路 (jiětí sīlù) | Problem-solving approach | The path you plan before you write |
| 推理 (tuīlǐ) | Reasoning / inference | Drawing a conclusion from known facts |
| 因此 / 所以 (yīncǐ / suǒyǐ) | Therefore / hence | Signal words that mark a new link in the chain |
| 已知 (yǐ zhī) | Given / known | The starting point — information you're told |
| 求证 (qiúzhèng) | Required to prove | What you need to reach — the destination |
| 证明 (zhèngmíng) | Proof | A complete, unbroken chain from given to conclusion |
| 复盘 (fùpán) | Review / post-mortem | Replaying the chain after the fact to find what worked and what didn't (see [[复盘]]) |
| 如果…那么 (rúguǒ…nàme) | If…then | Branching — the chain splits based on conditions |
| 触发特征 (chùfā tèzhēng) | Trigger | The feature of the question that selects the tool — find it before the technique |
| 预测 (yùcè) | Prediction | Running the chain forward to anticipate outcomes before they happen |

> [!tip] 已知 → 求证 is the Chinese exam structure
> Chinese maths education frames every proof problem as **已知** (given) → **求证** (to prove) → **证明** (proof). This is exactly the same structure as "Show that" in English exams — different language, same skeleton.

## Key Facts

### 1. Pólya's Four Phases

George Pólya's *How to Solve It* (1945) breaks problem-solving into four phases. These aren't just exam tips — they're how mathematicians actually think:

| Phase | Question to ask yourself | What you're doing |
|-------|--------------------------|-------------------|
| **Understand** | What am I given? What do I need to find/show? | Identify knowns, unknowns, constraints |
| **Plan** | Have I seen something like this before? What tools apply? | Choose a strategy (see §2 below) |
| **Execute** | Does each step follow from the last? | Write the chain, step by step |
| **Look Back** | Does my answer make sense? Can I check it? | Verify, simplify, reflect |

Most students jump straight from Understand to Execute. That's where errors come from — not from bad algebra, but from no plan.

> [!important] WHY "Look Back" matters — 复盘 (fùpán)
> Checking doesn't mean repeating the same work. It means asking: *Is this answer reasonable?* If a probability comes out as 1.3, or a length is negative, or a percentage is 400% when you expected something small — stop. Something went wrong.
>
> In Chinese, this is **复盘** — literally "replay the board" (from Go/chess: after the game, replay every move to find where you went wrong). In maths, 复盘 means tracing back through your chain to find the broken link. In life, it's the post-mortem after a project. See [[复盘]] for the full treatment.

### 2. The Strategy Toolkit

These are the most common strategies for IGCSE-level problems. Knowing them by name means you can *choose* one instead of staring at the page:

| Strategy | When to use it | Example |
|----------|---------------|---------|
| **Work forwards** | Standard calculation; chain from given → answer | "Find the area of..." |
| **Work backwards** | You know the answer, need to find the start | "The final price after 20% discount is £48. Find the original." |
| **Introduce a variable** | An unknown quantity needs a name | "Let the width be $x$..." |
| **Split into cases** | Different conditions lead to different paths | "If $x \geq 0$... If $x < 0$..." |
| **Draw a diagram** | Geometry, trigonometry, word problems | Always. Even when it's not asked for. |
| **Simplify first** | The expression is messy | Factor, cancel, or substitute before computing |
| **Use a known result** | A theorem or formula applies directly | "By Pythagoras..." / "By the sine rule..." |
| **Contradiction** | Assume the opposite, show it leads to nonsense | "Suppose $\sqrt{2}$ is rational..." (see [[Surds]]) |
| **Exhaustion** | Only finitely many cases to check | "Test $x = 1, 2, 3, \ldots$" |

### 3. The Trigger, Not the Technique

The toolkit above answers *"what tools exist?"* Look again at its middle column — **When to use it**. That column is quietly doing a second, harder job, because knowing a tool is really two separate pieces of knowledge:

- The **technique** — how to run the tool once it is in your hand.
- The **trigger** — the feature of the question that told you to reach for it.

The second is almost never written down. Recall the System 1 / System 2 callout above: in an experienced solver, *selection* has become System 1 — instant, automatic, invisible. An experienced programmer reads "for each student in the list…" and knows *loop* before the sentence ends; a physicist reads "constant speed up a rough slope" and knows *force balance* before reaching the question mark. Neither is hiding anything — the selection fires too fast to be noticed. So when the working is written out, only the technique survives on the page ("factorise", "resolve forces", "use a loop") and the trigger evaporates.

**Why this matters: only the trigger transfers.** A worked solution that names its tools lets you replay *that* problem. A new problem will not match the old one's steps — but it *will* show the same features. If you learned "factorise, then cancel", you can repeat Example 1 below; if you learned "*the excluded values in the condition are naming the factors*", you can start any question that carries such a condition. Grinding past papers without improving is exactly what technique-without-trigger practice looks like: each solved paper adds one more replayable problem and zero transferable selections.

Each subject has signature triggers that experienced solvers never say aloud:

| Subject | The question says | What it guarantees | Tool selected |
|---|---|---|---|
| Maths | "…for $x \neq \pm 3$" at the end of a "Show that" | Excluded values exist only to protect a denominator from zero — the condition is *naming its factors* | Factorise: $(x+3)(x-3)$ is already written in the condition (Example 1 below) |
| Physics | "constant speed up a rough slope" | Constant speed means $a = 0$, so the net force is zero | Force balance ($\Sigma F = 0$) — not SUVAT, which needs an acceleration to work with |
| CS | "for each mark in the list…", "keep asking until the input is valid" | The same action repeats — once per item, or until a condition holds | A loop — `for` over the collection, `while` on the condition |

**A trigger is a reason, not a keyword.** The middle column is the load-bearing one: the feature *guarantees the tool's precondition*. Constant speed selects force balance because zero acceleration is literally what force balance states. Skip that middle step and the trigger degrades into keyword superstition — "the question said 'minimum', so I differentiated" fails the moment the minimum sits at an endpoint of the domain, where the derivative is not zero. So record every trigger in three parts: *phrase → what it guarantees → tool*. If you cannot fill in the middle, you do not have a trigger yet; you have a coincidence.

**How to practise it.** After every worked example — in class, in a textbook, anywhere — take each tool the solution used and ask: *what in the question selected that?* Write the trigger beside the tool. If you cannot answer, you understood the replay but not the selection: you followed the solution without being in a position to have produced it. Building your own three-column trigger table per topic is worth more than solving five more copies of the same problem, because the table is the part an unfamiliar question can use.

Mechanics has the fully worked-out version of this discipline: the trigger-phrasing table in [[Choosing Effective Equations]] maps Cambridge's own idioms — "coalesce", "constant power", "use an energy method" — straight to frameworks. And [[Forward Reading and Problem Discovery]] is the general theory: a trigger is an invariant read forward, and reading for them is what problem-solving *is*.

一句话：解题的关键不是"会用哪个方法"，而是"题目中的哪个特征让你选中了它"——**先找触发特征，再谈技巧。**

### 4. Anatomy of a "Show That" Question

"Show that" is the most chain-dependent question type. The answer is *given to you* — what the examiner wants is the chain.

**Structure:**

$$\underbrace{\text{Given information}}_{\text{starting point}} \xrightarrow{\text{your working}} \underbrace{\text{stated result}}_{\text{destination}}$$

**The rules:**
- You must not use the result you're trying to show. (That's circular reasoning — like proving "the bridge is safe" by walking across it.)
- Every algebraic step must be visible. If $3x + 6 = 3(x + 2)$, write both sides — don't just write the factored form.
- The final line of your working must match the stated result **exactly**. If the question says "show that the area is $\dfrac{25\pi}{4}$," your last line must say $\dfrac{25\pi}{4}$, not $6.25\pi$.
- "Show that" earns method marks. A correct chain with a small arithmetic error still earns most marks. A correct answer with no working earns zero.

### 5. Command Words and What They Demand

Different command words expect different levels of chain:

| Command word | What the examiner wants | Chain depth |
|-------------|------------------------|-------------|
| **Calculate** / **Find** | A numerical answer with working | Medium — show method, state answer |
| **Determine** | Find, but with reasoning for any choices | Medium–High |
| **Show that** | Complete chain to the given result | High — every step visible |
| **Prove** | Rigorous logical argument from definitions | Highest — no gaps allowed |
| **Verify** | Substitute the given answer and confirm it works | Low — just check |
| **Explain** | English sentences justifying a mathematical claim | Medium — logic in words |
| **State** | Just write the answer | None — no working expected |

> [!warning] "Show that" vs "Prove"
> At IGCSE, "show that" and "prove" are nearly interchangeable. At A-Level and university, "prove" carries stricter expectations: you must cite the exact definitions and theorems you use, and your reasoning must be airtight. Think of "show that" as building a bridge with wooden planks — sturdy enough to cross. "Prove" is building it with steel — engineered to carry any load.

### 6. How Marks Are Awarded

Exam mark schemes award marks for the **chain**, not just the answer:

| Mark type | Symbol | What it rewards |
|-----------|--------|-----------------|
| **Method** | M | Choosing the right approach and starting it correctly |
| **Accuracy** | A | Correct result following from correct method |
| **Dependent accuracy** | A (dep) | Correct result, but only if the M mark was earned |
| **Independent** | B | A correct statement or result that doesn't depend on method |

**Key insight:** M marks are earned even if the arithmetic goes wrong. This means a clear chain with a small slip still earns most of the marks, while a correct answer with no chain earns nothing (because the A marks are usually dependent on M marks).

This is why writing the chain is not just good practice — it's the scoring mechanism.

### 7. Signal Words — The Glue of the Chain

Every link in the chain needs a signal word connecting it to the next:

| English | 中文 | When to use |
|---------|------|-------------|
| Therefore / Hence | 因此 / 所以 | One step follows logically from the previous |
| Since / Because | 因为 / 由于 | Citing a reason before stating a conclusion |
| Let | 设 / 令 | Introducing a variable or assumption |
| Substituting | 代入 | Replacing a variable with a value or expression |
| From the diagram / From (i) | 由图可知 / 由(i) | Referencing earlier work or given information |
| This gives | 可得 | Stating the result of a computation |
| As required | 即为所求 (jí wéi suǒ qiú) | Final line of a "Show that" — confirms you've reached the destination |

## Common Misconceptions (Teaching Notes)

### 1. "I can see the answer, so I'll just write it"

**Wrong:** The student writes the conclusion without showing how they got there.

**Why it fails:** In a "Show that" question, the answer is worth 0 marks. ALL the marks are in the working. Even in "Find" questions, A marks depend on M marks — skip the method, lose both.

**Fix:** Pretend you're explaining to someone who can't see the answer. If they couldn't follow your steps to reach it independently, you haven't shown enough.

**The same skip, seen from the other side:** a worked solution that says "here, use substitution" without saying what *called for* substitution is skipping a step too — the selection step. When any solution "just knows" the tool, ask the question from Key Facts §3: which feature of the problem fired? An answer without the chain earns no marks; a tool without its trigger teaches no transfer.

### 2. "More steps = more risk of errors"

**Wrong:** The student skips steps to avoid mistakes.

**Why it's backwards:** Skipping steps is where errors hide. Writing each step separately makes errors visible — both to you (so you can catch them) and to the examiner (so they can award method marks even if arithmetic goes wrong).

### 3. "I'll clean it up at the end"

**Wrong:** Messy working first, then plan to rewrite neatly.

**Why it fails in exams:** You almost never have time to rewrite. The first version is the final version. Build the chain neatly from the start — one equals sign per line, aligned, with signal words.

### 4. Using the result you're trying to prove

**Wrong:** In a "Show that $x = 5$" question, the student substitutes $x = 5$ into both sides of an equation and says "LHS = RHS, so $x = 5$."

**Why it's circular:** You've assumed what you're trying to prove. That's like proving you can lift 100 kg by assuming you can lift 100 kg. The chain must flow from the *given* information to the result, not the other way around.

**Exception:** "Verify" questions explicitly ask you to substitute and check. Read the command word carefully.

## Worked Examples

### Example 1 — "Show that" (Algebra)

> Show that $\dfrac{x^2 + 6x + 9}{x^2 - 9} = \dfrac{x + 3}{x - 3}$ for $x \neq \pm 3$.

**Chain of thought:**

$$\dfrac{x^2 + 6x + 9}{x^2 - 9}$$

Numerator: $x^2 + 6x + 9 = (x + 3)^2$ (perfect square)

Denominator: $x^2 - 9 = (x + 3)(x - 3)$ (difference of two squares)

$$= \dfrac{(x+3)^2}{(x+3)(x-3)} = \dfrac{x+3}{x-3} \qquad \text{(cancelling } x + 3 \text{, valid since } x \neq -3\text{)}$$

As required. $\square$

**Why this chain works:** Each step uses a named technique (perfect square, DOTS, cancellation), and the condition $x \neq -3$ is explicitly stated (not assumed silently).

---

### Example 2 — Working Backwards (Number)

> After a 15% discount, a jacket costs £68. Find the original price.

**Plan:** Let the original price be $P$. After 15% discount, you pay 85% of $P$.

**Chain:**

$$0.85P = 68$$

$$P = \dfrac{68}{0.85} = 80$$

The original price was $\boxed{£80}$.

**Check (Look Back):** 15% of £80 = £12. £80 − £12 = £68. ✓

---

### Example 3 — "Prove" (Number theory)

> Prove that the sum of any three consecutive integers is always divisible by 3.

**Chain:**

Let the three consecutive integers be $n$, $n + 1$, $n + 2$ where $n \in \mathbb{Z}$.

$$n + (n+1) + (n+2) = 3n + 3 = 3(n + 1)$$

Since $n + 1 \in \mathbb{Z}$, the sum is $3 \times \text{(an integer)}$, which is divisible by 3. $\square$

**Why this chain is airtight:** The variable $n$ represents *any* integer (not a specific one), so the proof covers all cases. The factorisation $3(n+1)$ makes divisibility by 3 visible by inspection.

---

### Example 4 — Proof by Contradiction: $\sqrt{2}$ is irrational

> Prove that $\sqrt{2}$ is irrational.

**Strategy:** Contradiction — assume the opposite, show it breaks.

**Chain:**

**Step 1 — Assume the opposite.** Suppose $\sqrt{2}$ is rational (see [[Rational Numbers]]). Then we can write $\sqrt{2} = \dfrac{a}{b}$ where $a, b \in \mathbb{Z}$, $b \neq 0$, and $\dfrac{a}{b}$ is in lowest terms (i.e. $a$ and $b$ share no common factor).

**Step 2 — Square both sides.** $2 = \dfrac{a^2}{b^2}$, so $a^2 = 2b^2$.

**Step 3 — Deduce $a$ is even.** Since $a^2 = 2b^2$, $a^2$ is even. But if $a^2$ is even, then $a$ must be even (because odd × odd = odd). So write $a = 2k$ for some integer $k$.

**Step 4 — Substitute and deduce $b$ is even.** $(2k)^2 = 2b^2$ → $4k^2 = 2b^2$ → $b^2 = 2k^2$. By the same reasoning, $b$ is even.

**Step 5 — Contradiction.** Both $a$ and $b$ are even, so they share a common factor of 2. But we assumed $\dfrac{a}{b}$ was in lowest terms. Contradiction. $\square$

Therefore $\sqrt{2}$ is irrational.

**Why this is the perfect chain-of-thought example:** Every single step is load-bearing. Forget to say "in lowest terms" at Step 1 — the contradiction in Step 5 doesn't fire. Skip the reasoning "if $a^2$ is even then $a$ is even" at Step 3 — you have a gap the examiner can't bridge. Miss one link and you are literally stuck. This proof is a chain where you can *feel* each link holding the next. See [[Surds]] for the full treatment.

## Exam Notes

### OxAQA 9260 (Extension)

**Syllabus ref:** Cross-curricular — applies to AO2 (reason, interpret, communicate) and AO3 (solve problems).

- 9260 allocates marks explicitly for **quality of written communication (QWC)** on selected questions. QWC marks reward a clear chain of reasoning with signal words and logical structure.
- "Show that" and "Prove" appear across the paper. Algebraic proof (A8) is a standalone topic.
- Multi-step problems (4+ marks) always require visible working for method marks.

### Cambridge 0580 Extended

**Syllabus ref:** Cross-curricular — applies to all papers.

- 0580 uses "Show that" less frequently than 9260, but longer Paper 4 questions (6–8 marks) require multi-step chains.
- The command word list is published in the syllabus front matter. "Show (that)" means "provide structured evidence using known mathematical facts."

### Cambridge 0606

**Syllabus ref:** Cross-curricular.

- 0606 makes heavier use of "Show that" and "Hence" (= use the result you just proved as a stepping stone for the next part).
- "Hence or otherwise" gives you a choice: use the guided chain, or find your own path. The guided chain is usually faster.

### AP / IB / A-Level

- **AP Calculus:** Free-response questions award "presentation" points for clear reasoning. "Justify your answer" requires a complete chain.
- **IB Mathematics AA:** The "Exploration" (Internal Assessment) is graded on mathematical communication — your ability to build and explain chains of reasoning.
- **A-Level Further Mathematics:** Proof by induction, contradiction, and exhaustion are assessed as standalone skills, each with its own chain structure.

> [!info] Beyond syllabus — Chain of thought in AI
> The term "chain of thought" (思维链) was introduced by researchers at **Google** in 2022, who showed that large language models (LLMs) solve problems far more accurately when prompted to "think step by step." The paper became widely known within the AI industry — it changed how every major lab trained and prompted their models.
>
> The idea reached the general public in January 2025 when the Chinese lab **DeepSeek** released DeepSeek-R1 — an open-source model that visibly "thinks out loud," writing long chains of intermediate reasoning before answering. R1's transparent reasoning chains showed the world what chain of thought looks like at scale: the model literally shows its working, step by step, just like a student in an exam.
>
> This isn't a coincidence. The AI technique works for the same reason exam technique works: breaking a complex problem into small, verifiable steps catches errors that would compound in a single leap. The stepping-stone metaphor applies to both biological and artificial brains.

## Connections

**Prerequisites:**
- [[Set]] — Set notation and logic vocabulary appear in formal proofs

**Leads to:**
- [[Logic]] — ∀, ∃, ⇒, ⇔ formalise what "each step follows" actually means
- [[Algebraic Proof]] — applying chain-of-thought to algebraic "Prove" questions (9260 A8)
- [[Geometrical Proof]] — applying chain-of-thought with circle theorems and angle facts (9260 G9 Ext)
- [[Exam Command Words (Vocab)\|Exam Command Words]] — decoding what each command word demands (Sketch vs Plot, State vs Explain, Show that vs Prove vs Verify)
- [[Choosing Effective Equations]] — the trigger discipline at full mechanics depth: a trigger-phrasing table mapping Cambridge's own idioms to frameworks
- [[Forward Reading and Problem Discovery]] — the general theory behind triggers: reading forward for the invariants each clause locks down

**Used across:**
- [[Differentiation]] — multi-step tangent/normal problems require a clear chain
- [[Combined Probability]] — tree diagram paths ARE chains of thought (multiply along the branch)
- [[Counting Problems]] — choosing the right strategy from the toolkit
- [[Upper and Lower Bounds]] — "Show that" questions on maximum/minimum values require careful bound selection chains

## Beyond Syllabus

### AP / IB / A-Level depth

**Proof structures as chain types**

At A-Level and beyond, proofs are classified by the *shape* of their chain:

| Proof type | Chain shape | Example |
|-----------|------------|---------|
| **Direct proof** | A → B → C → result | "Show that the sum of two even numbers is even" |
| **Proof by contradiction** | Assume ¬result → ... → contradiction → result must be true | "Prove that $\sqrt{2}$ is irrational" (see [[Surds]]) |
| **Proof by induction** | Base case + (if true for $k$, then true for $k+1$) → true for all $n$ | "Prove that $\sum_{r=1}^{n} r = \dfrac{n(n+1)}{2}$" |
| **Proof by exhaustion** | Check every case | "Prove that $n^2 + n$ is even for $n = 1, 2, 3, 4$" |
| **Proof by contrapositive** | ¬B → ¬A (logically equivalent to A → B) | "If $n^2$ is even, then $n$ is even" |

Each type is a different chain architecture — but they all share the same requirement: every link must be justified.

### Beyond high school — University

**Formal logic and proof assistants**

At university, chains of thought become formal objects. A proof in first-order logic is literally a sequence of formulas where each one follows from the previous by a rule of inference (modus ponens, universal instantiation, etc.). See [[Formal Logic]] for where this leads.

This has been taken to its extreme in **proof assistants** like Lean, Coq, and Isabelle — software that checks every link in a mathematical chain mechanically. In 2023, the entire proof of Fermat's Last Theorem was being formalised in Lean, requiring every step to be machine-verified. The chain of thought must leave no gap — not even one a human would consider "obvious." This is System 3 in its purest form — the computer is the external validator that doesn't care how "obvious" a step feels to you.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\implies$ | `\implies` | "implies" — single direction |
| $\iff$ | `\iff` | "if and only if" — both directions |
| $\therefore$ | `\therefore` | "therefore" — conclusion follows |
| $\because$ | `\because` | "because" — giving a reason |
| $\square$ | `\square` | QED — marks end of proof |
| $\lvert x \rvert$ | `\lvert x \rvert` | Absolute value |
| $\xrightarrow{\text{rule}}$ | `\xrightarrow{\text{rule}}` | Labelled arrow (step annotation) |

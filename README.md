# The Vault — Student Edition 学生版

**A bilingual (English + 中文) knowledge bank for Mathematics, Physics and Computer Science**,
written for international curricula: Cambridge IGCSE and A-Level, IB, and AP.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

> **Edition** `student-2026-08-19` · built 2026-08-19 from commit `a81c4d0`  
> 342 cards · 428 diagrams · 62 explainers · 95 illustrations

---

## What's inside

**342 Markdown cards** across five collections, plus the figures that go with them —
**428 SVG diagrams** (many animated), **62 MP4 explainers**, and
**95 illustrations and comics**.

| Folder | Cards | What it is |
|---|---|---|
| `Mathematics/` | 214 | Number, Algebra, Geometry, Trigonometry, Calculus, Statistics, Probability, Functions, Combinatorics, Linear Algebra, Coordinate Geometry, Measurement, Foundations, Problem Solving — plus formula-sheet references. |
| `Physics/` | 37 | Mechanics, Foundations (measurement), Thermal, Fields, Electricity, Oscillations, Waves, Modern, Astronomy, Medical. |
| `CS/` | 48 | Foundations, Logic Circuits, Algorithms, Data Representation, Hardware Systems, Systems Software, Data Structures. |
| `Stories/` | 32 | Fun-first historical narratives — the human drama of mathematics and science as its own subject. |
| `Meta/` | 11 | Methodology cards: how to *think* across domains. |

Every concept appears in **both English and Chinese**, with key terminology anchored in each
card's **中文锚点** section.

Cards are written to **college-ready depth** (A-Level / IB / AP) even on basic IGCSE topics.
The philosophy is **rigour, intuition and delight together** — not exam-pass minimum. Every card
explains *why* a rule works, with proof and intuition, not just what to write down.

---

## Get it

```bash
git clone --depth 1 https://github.com/Kepei-Lei102/the-vault-student.git
```

`--depth 1` skips the history, so you download the material once rather than every version
of it. Later, `git pull` inside the folder brings you up to date.

No git? Download the latest `The_Vault_For_Student.zip` from the repository's **Releases**
page and unzip it. Same contents; you just re-download to update.

**One folder, two ways in.** The same directory is an Obsidian vault *and* an AI tutor's
workspace. You don't have to choose — most people end up using both.

## Your first five minutes

### Reading it yourself

1. Install [Obsidian](https://obsidian.md) — free, on macOS / Windows / Linux / iPad / Android.
2. **Open another vault → Open folder as vault**, and select this folder.
3. Open a **Directory** file — `Mathematics/Directory.md`, `Physics/Directory.md`,
   `CS/Directory.md`, `Stories/Directory.md`, or `Meta/Directory.md`. Each indexes every card
   in its subject with a one-line hook. Click any `[[link]]` to follow it.

### Studying with an AI tutor

Install [Claude Code](https://claude.com/claude-code), then, inside the folder:

```bash
claude
```

It reads `CLAUDE.md` on its own and picks up the house rules — most importantly that it must
**search these cards before answering**, and tell you which card the answer came from. You
don't have to set anything up or paste any instructions. Just ask:

- *"I don't get why binary search needs a sorted list. Explain it from the cards."*
- *"Which card covers 9618 §10.4, and am I ready for it?"*
- *"Quiz me on the Thermal cards, hardest first."*
- *"I keep losing marks on significant figures. What am I getting wrong?"*
- *"Build me a two-week revision path for Paper 4, using the prerequisites graph."*

If an answer ever feels generic, ask **"which card is that from?"** — a good answer here
always has a file behind it.

### Why the AI behaves differently here

Ask any chatbot about binary search and you get *an* answer — correct, probably, but in its
own notation, with its own metaphors, competing with the material in front of you. Three
files change that:

- **`CLAUDE.md`** — the agent's working manual, loaded automatically.
- **`AGENTS.md`** — the same manual for Codex and other `AGENTS.md`-aware tools.
- **`.claude/skills/vault-search/SKILL.md`** — the search protocol. Plain Markdown, readable
  directly if your tool doesn't load skills on its own.

They enforce one rule:

> **Search these cards first. Answer from what they say, in their notation and framing, and
> name the file it came from.**

So the AI reinforces what you're studying instead of talking over it. And when the vault
genuinely doesn't cover something, it has to say so out loud rather than papering over the
gap — you always know which of the two you're holding.

Other tools work too: any agent that reads `CLAUDE.md` or `AGENTS.md` picks up the same
rules, and any assistant at all can be pointed at `.claude/skills/vault-search/SKILL.md` by
hand.

### Reading the raw files

The cards are plain Markdown and read fine in any editor or on GitHub. Cross-references use
`[[Card Name]]` wiki-links, maths sits in `$…$` and `$$…$$`, and figures are embedded as
`![[file.svg]]` / `![[file.mp4]]`.

---

## How it's organised

The vault is organised **ECS-style (Entity–Component–System)**, which has one consequence
worth knowing up front:

> **Folders are decorative, not navigational.**

A card about the natural logarithm might sit under `Number/`, `Functions/`, or `Calculus/`.
Don't navigate by folder — navigate by these three, in order:

1. **The Directory files** — one per subject, a curated table of contents.
2. **The connections graph** — every card's frontmatter lists `prerequisites` and `leads_to`,
   mirrored by a **Connections** section at the foot of the card. This is also the *teaching
   order*: `prerequisites` is what to shore up when you're stuck, `leads_to` is where you go
   next.
3. **The tag namespace** — frontmatter tags by `subject/`, `domain/`, `level/`, `curriculum/`,
   `syllabus/`, `type/`, `notation/`, and `misconception/`. The last one is a map of the
   specific traps this material was written to defuse.

**Five folders, five jobs:**

- `Mathematics/` is **pedagogy-first** — the maths leads, the story is a footnote.
- `Physics/` is **causality-first** — every card teaches you to trace *material* causality:
  what force caused what motion, where the energy went.
- `CS/` is **logical-causality-first** — every card teaches you to trace *logical* causality:
  what truth table outputs what, what called what.
- `Stories/` is **fun-first** — the human drama is allowed to be the point.
- `Meta/` is **methodology-first** — how to think, across all domains.

---

## Card layout

Each card follows a consistent structure:

1. **Frontmatter** (YAML) — Chinese title, prerequisites, leads-to, tags
2. **Definition** — formal statement plus plain-English explanation
3. **中文锚点** — Chinese-language anchor: key terms and summary
4. **Key Vocabulary** — bilingual table
5. **Derivation / Proof / Worked Examples**
6. **Common Mistakes** — the traps the exams test routinely
7. **Exam Notes** — broken down by board (Cambridge IGCSE / A-Level, IB, AP)
8. **Beyond Syllabus** — connections upward into higher mathematics, physics, CS and the
   real world
9. **Connections** — wiki-links to related cards
10. **LaTeX Reference** — the notation used

**Vocab cards** (50–120 lines) are short reference notes for syllabus terminology.
**Deep cards** (typically 300–450 lines) carry the proofs, worked examples and extensions.

---

## About this edition

This is the **student edition** — the knowledge layer only. It is *built* from a larger
working repository rather than copied by hand, so what you have is a complete, consistent
snapshot: the maintainer's syllabus PDFs, topic maps, build queues and authoring tooling
stay behind, and nothing here points at them.

`Syllabus Coverage.md` is generated from the cards themselves at build time, which is why it
can never disagree with them. The stamp at the top of this file names the exact build you
are holding — quote it if you ever report a mistake.

New cards land when a topic area closes, and `git pull` brings them in.

Released under **CC BY-SA 4.0** — see `LICENSE`. Share it, adapt it, keep it open.

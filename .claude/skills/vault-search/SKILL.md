---
name: vault-search
description: >
  Find what already exists in The Vault — a bilingual (English/中文) knowledge bank spanning
  mathematics, physics and computer science across IGCSE, A-Level, IB and AP — BEFORE answering
  any subject question, and before declaring a topic missing. Use this skill ANY TIME a student
  asks a subject question ("why does…", "how do I…", "what is…", "I don't get…"), asks where a
  topic lives, or asks what to read next. Trigger on: "search the vault", "is this in the vault",
  "where is ___", "find ___", "what do we have on ___", "anything on ___", "which card covers
  ___", "explain ___", "help me with ___", or any question that begins with a student's doubt.
  The skill codifies the protocol that folders here are navigationally meaningless — the
  Directory files, the connections graph, and the tag namespace are the index.
---

# vault-search — the search protocol

You are searching **The Vault**, an Obsidian knowledge bank organised **ECS-style
(Entity–Component–System)**. The point of ECS is that **folders are decorative, not
navigational**. A card on the natural logarithm might live under `Number/`, `Functions/`,
or `Calculus/` — the vault makes no promise about which. Treat every search as a *flat*
search over all `.md` files, and use the **Directory** files, the **frontmatter graph**,
and the **tag namespace** as your index.

## Core principle

> **Do not stop at the first "no."** Absence in the expected folder is not evidence of
> absence from the vault.

And its companion, which is the reason this skill exists at all:

> **Search before you answer.** The student is being taught from this material — its
> notation, its metaphors, its worked-example order, its Chinese glosses. An answer that
> is correct in general but foreign to the card in front of them costs them. If the vault
> covers it, the vault's framing wins.

---

## The protocol

Run these steps in order. Stop only when you have found the relevant cluster of cards or
exhausted **every** step.

### Step 1 — Decompose the question into concept keywords

Before touching the filesystem, list the concepts the question actually ranges over. A
student's "why is ∫(1/x) dx = ln x?" is not one concept — it is at least six: *logarithm*,
*natural log*, *Euler's number*, *exponential*, *derivative*, *antiderivative*, *inverse
function*. Write the list out so both you and the student can see the decomposition.

**One keyword is almost never enough.** Search only "integration" and you miss
`Logarithms.md`, where the answer actually lives.

### Step 2 — Read the subject Directory first

Each subject keeps a curated, hand-maintained index with a one-line hook per card:

```
Mathematics/Directory.md
Physics/Directory.md
CS/Directory.md
Stories/Directory.md
Meta/Directory.md
```

These are the fastest way to see the whole surface area. Scan for your concept keywords;
if a listed card matches, open it — its **Connections** section and frontmatter will
usually expose the entire cluster in one step.

If you don't know which subject owns the question, read more than one Directory. Many
topics are genuinely shared (Big-O is CS *and* maths; SHM is physics *and* calculus).

### Step 3 — Grep the whole vault on every keyword

Folder-agnostic full-text search, one pass per keyword or one alternation across all
content folders:

```bash
# Filename sweep — fastest
rg --files -g "*.md" Mathematics Physics CS Stories Meta | rg -i "log|ln|exp|euler|integral|derivat"

# Content sweep — catches cards that discuss a concept without naming their file after it
rg -il "\bln\b|natural log|antiderivative|\\\\int" Mathematics Physics CS Stories Meta

# Tag sweep — frontmatter as a structured query
rg -l "notation/ln|type/proof" Mathematics Physics CS
```

Search **content**, not just filenames. Anti-pattern #2 below is the one that burns people.

### Step 4 — Use the tag namespace

Every card's frontmatter carries structured tags. The families:

| Family | Examples | Use it to answer |
|---|---|---|
| `subject/` | `mathematics`, `physics`, `computer-science` | which subject owns this |
| `domain/` | `calculus`, `algorithms`, `geometry` | the topic cluster |
| `level/` | `IGCSE`, `A-Level`, `IB`, `AP` | is this at the student's level |
| `curriculum/` | `Cambridge-0580`, `Cambridge-9618`, `AP-CSA`, `IB-Physics` | which course |
| `syllabus/` | `0478-7-4`, `9618-19-1a`, `9702-20-1` | **what the exam actually asks** |
| `type/` | `deep`, `vocabulary`, `definition`, `theorem`, `proof` | how deep the card goes |
| `notation/` | `ln`, `sigma`, `python` | which symbols appear |
| `misconception/` | `binary-search-on-unsorted`, `arc-vs-chord` | **which trap the student just hit** |

Two are worth reaching for by reflex:

- **`syllabus/`** — when the question is framed in exam language ("what's on §9.2?"),
  this is a direct lookup.
- **`misconception/`** — when the student has made an *error*, grep these. The material
  is written to defuse specific traps, and there is often a card built around exactly the
  mistake they just made.

Intersect tags for a narrow query:

```bash
rg -l "notation/ln" Mathematics | xargs rg -l "type/proof"
```

### Step 5 — Follow the frontmatter graph from any hit

Once one relevant card is open you have a **pre-computed adjacency list**:

```yaml
prerequisites:
  - "[[Card A]]"
leads_to:
  - "[[Card B]]"
```

plus a **Connections** section listing Parent · Components · Extensions · Applications ·
Reverse. Breadth-first from the seed card beats a second grep sweep almost every time.

This graph is also the **teaching order** — `prerequisites` is what to shore up when the
student is stuck; `leads_to` is where they go next when they're solid. Reverse lookup —
"what links here?" — is one grep:

```bash
rg -l "\[\[Target Card\]\]" Mathematics Physics CS Stories Meta
```

A `leads_to` link that resolves to no file is a **dangling link**: a card the material
expects but that isn't written yet. That is useful information, not an error — report it
as "not covered here yet", never as a link to follow.

### Step 6 — Report with paths and section hooks

Always give the relative path from the vault root, written as plain words in a code span
so it can be pasted into Obsidian's quick switcher — and quote the *specific* section or
callout that answers the question:

```
`Mathematics/Number/Logarithms.md` → §Natural log and calculus → callout
"Where does (ln x)' = 1/x come from?" — answers this directly.

`Mathematics/Number/Exponential Function.md` → two-line inverse-function-rule proof.
```

"It's in Logarithms" makes the student re-read a whole card to find the two lines they
needed.

### Step 7 — Only then declare a gap

If steps 1–6 turn up nothing, say so **explicitly**, then:

1. Name what the missing card would be called.
2. Check whether it already appears as a dangling `leads_to` somewhere — that means the
   material expects it.
3. Point the student at the **nearest existing card** in the meantime.
4. If you go on to answer from your own knowledge, mark it clearly as *not from the
   vault*, so the student knows which of the two they are holding. Never blend the two
   silently.

---

## Anti-patterns

1. **Answering before searching.** The most expensive one. Your general answer competes
   with the student's own material instead of reinforcing it.
2. **Searching filenames only.** `Logarithms.md` has no "integration" in its name but
   contains the callout that answers the integration question.
3. **Searching one folder and stopping.** `Mathematics/Calculus/` has no `Integration.md`
   — that does not mean integration is uncovered.
4. **Skipping the Directory.** It is a curated table of contents; reading it first
   often resolves the question in one step.
5. **Reporting by title only.** Give the path *and* the hook.
6. **Answering "what folder is this in?"** — a malformed question in an ECS vault. Answer
   with the file path and the conceptual cluster instead.

## One-line summary

> Decompose → Directory → grep the whole vault on every keyword → tags (`syllabus/`,
> `misconception/`) → follow the frontmatter graph → report with paths and exact section
> hooks → only then declare a gap.

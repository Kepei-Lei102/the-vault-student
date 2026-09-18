"""
ai-figures.py — six figures for [[Artificial Intelligence]].  Run ai-learning-demo.py first
(it saves the arrays the data figures use).

  ai-map.svg                    AI ⊃ machine learning ⊃ deep learning; expert systems beside;
                                the three ways of learning
  ai-neuron-network.svg         one neuron (weighted sum → activation), then layers, with the
                                forward pass and back propagation arrows
  ai-learning-curves.svg        regression fitted by gradient descent; XOR loss falling
  ai-deep-vs-shallow.svg        the two-spiral decision maps: one wide layer vs three
  ai-unsupervised-reinforcement.svg   k-means clusters found without labels; the Q-learning
                                policy on the grid
  ai-expert-system.svg          the four components and the inference loop

Vault style: text #888, no background rect, width="100%" + viewBox. Verify light + dark.
"""
import math, re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, FancyArrowPatch, Circle

GREY = "#888888"
BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
S = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad"

def style(ax):
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelcolor=GREY)
    ax.xaxis.label.set_color(GREY); ax.yaxis.label.set_color(GREY); ax.title.set_color(GREY)
    ax.set_facecolor("none")

def save(fig, name):
    fig.patch.set_alpha(0)
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    s = open(name).read()
    s = s.replace('<svg ', '<svg width="100%" ', 1)
    s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1)
    open(name, "w").write(s); print("wrote", name)

def box(ax, x, y, w, h, text, col, fs=9, lw=1.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15", fc=col, ec=col, alpha=0.18, lw=0))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15", fc="none", ec=col, lw=lw))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=GREY)

# ------------------------------------------------------------------ 1. the map
fig, ax = plt.subplots(figsize=(10, 6)); style(ax); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(-0.2, 6.2)
ax.add_patch(Ellipse((4.4, 3.0), 8.6, 5.4, fc=BLUE, ec=BLUE, alpha=0.08, lw=1.4))
ax.add_patch(Ellipse((4.4, 3.0), 8.6, 5.4, fc="none", ec=BLUE, lw=1.4))
ax.text(4.4, 5.25, "Artificial intelligence", ha="center", fontsize=11, color=BLUE)
ax.text(4.4, 4.9, "programs that simulate intelligent behaviour: they hold data and rules, reason from them, and some learn", ha="center", fontsize=8.5, color=GREY)
ax.add_patch(Ellipse((5.4, 2.55), 5.8, 3.7, fc=PURPLE, ec=PURPLE, alpha=0.10, lw=1.4)); ax.add_patch(Ellipse((5.4, 2.55), 5.8, 3.7, fc="none", ec=PURPLE, lw=1.4))
ax.text(5.4, 3.95, "Machine learning", ha="center", fontsize=10.5, color=PURPLE)
ax.text(5.4, 3.62, "the program adapts its own rules and data from experience", ha="center", fontsize=8.5, color=GREY)
ax.add_patch(Ellipse((6.4, 2.35), 2.8, 1.5, fc=GREEN, ec=GREEN, alpha=0.14, lw=1.4)); ax.add_patch(Ellipse((6.4, 2.35), 2.8, 1.5, fc="none", ec=GREEN, lw=1.4))
ax.text(6.4, 2.6, "Deep learning", ha="center", fontsize=10, color=GREEN); ax.text(6.4, 2.12, "neural networks with\nmany hidden layers", ha="center", fontsize=8, color=GREY)
box(ax, 0.55, 1.9, 1.9, 1.6, "Expert systems\nknowledge base · rule base\ninference engine · interface\n(rules written by people;\nthey do not learn)", AMBER, fs=7.6)
for i, (name, note) in enumerate((("Supervised", "labelled examples in,\na mapping out"), ("Unsupervised", "no labels: find the\nstructure yourself"), ("Reinforcement", "no labels: act, get\nreward, do better"))):
    x = 3.15 + i * 1.5
    box(ax, x, 0.95, 1.35, 0.85, f"{name}\n{note}", TEAL, fs=7)
ax.text(5.4, 0.6, "three ways to learn — any of them may be shallow or deep", ha="center", fontsize=8, color=GREY)
ax.set_title("What is inside what — the syllabus's nouns in one picture", fontsize=10.5)
save(fig, "ai-map.svg")

# ------------------------------------------------------------------ 2. neuron + network
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1, 1.25]})
for ax in (a1, a2): style(ax); ax.axis("off")
a1.set_xlim(0, 10); a1.set_ylim(0, 6)
for i, (y, lab) in enumerate(((5, "x₁"), (3.5, "x₂"), (2, "x₃"))):
    a1.add_patch(Circle((1.2, y), 0.4, fc=BLUE, ec=BLUE, alpha=0.25)); a1.text(1.2, y, lab, ha="center", va="center", fontsize=9, color=GREY)
    a1.add_patch(FancyArrowPatch((1.65, y), (4.6, 3.5), arrowstyle="-|>", color=GREY, lw=1.0, mutation_scale=10))
    a1.text(3.0, y + (3.5 - y) * 0.45 + 0.22, f"w{i+1}", fontsize=8.5, color=AMBER)
a1.add_patch(Circle((5.2, 3.5), 0.75, fc=PURPLE, ec=PURPLE, alpha=0.25)); a1.text(5.2, 3.5, "Σ wᵢxᵢ + b\n→ f( · )", ha="center", va="center", fontsize=8, color=GREY)
a1.add_patch(FancyArrowPatch((6.0, 3.5), (8.3, 3.5), arrowstyle="-|>", color=GREY, lw=1.0, mutation_scale=10))
a1.add_patch(Circle((8.8, 3.5), 0.4, fc=GREEN, ec=GREEN, alpha=0.25)); a1.text(8.8, 3.5, "y", ha="center", va="center", fontsize=9, color=GREY)
a1.text(5.2, 0.55, "one neuron: weighted sum, plus a bias, through a squashing function\n— it can only draw one straight line through its inputs", ha="center", fontsize=8, color=GREY)
a1.set_title("The neuron", fontsize=10)
a2.set_xlim(0, 12); a2.set_ylim(0, 6.4)
layers = [(1.5, 3, BLUE, "input"), (4.0, 5, PURPLE, "hidden 1"), (6.5, 5, PURPLE, "hidden 2"), (9.0, 4, PURPLE, "hidden 3"), (11.0, 1, GREEN, "output")]
pos = []
for x, n, col, lab in layers:
    ys = np.linspace(3.2 - 0.6 * (n - 1), 3.2 + 0.6 * (n - 1), n)
    pos.append([(x, y) for y in ys])
    for y in ys: a2.add_patch(Circle((x, y), 0.26, fc=col, ec=col, alpha=0.3))
    a2.text(x, 0.55, lab, ha="center", fontsize=8, color=GREY)
for L1, L2 in zip(pos[:-1], pos[1:]):
    for (x1, y1) in L1:
        for (x2, y2) in L2:
            a2.plot([x1 + 0.26, x2 - 0.26], [y1, y2], color=GREY, lw=0.4, alpha=0.6)
a2.add_patch(FancyArrowPatch((1.5, 6.05), (11.0, 6.05), arrowstyle="-|>", color=GREEN, lw=1.4, mutation_scale=12)); a2.text(6.2, 6.2, "forward: data in, prediction out", ha="center", fontsize=8.5, color=GREEN)
a2.add_patch(FancyArrowPatch((11.0, 0.15), (1.5, 0.15), arrowstyle="-|>", color=RED, lw=1.4, mutation_scale=12)); a2.text(6.2, -0.1, "back propagation: the error's gradient, layer by layer, adjusts every weight", ha="center", fontsize=8.5, color=RED)
a2.set_ylim(-0.4, 6.5)
a2.set_title("The network — every line is a weight the training will move", fontsize=10)
fig.tight_layout(); save(fig, "ai-neuron-network.svg")

# ------------------------------------------------------------------ 3. learning curves
L = np.load(f"{S}/xor-loss.npy")
rng = np.random.default_rng(1956)
x = rng.uniform(0, 10, 200); y = 3.0 * x + 2.0 + rng.normal(0, 2.0, 200)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 3.8))
for ax in (a1, a2): style(ax)
a1.scatter(x, y, s=8, color=TEAL, alpha=0.6, label="data")
xs = np.linspace(0, 10, 2)
for step, col, lab in ((0, GREY, "start: y = 0"), (10, AMBER, "after 10 steps"), (2000, GREEN, "after 2000 steps: y = 3.01x + 1.90")):
    m, c = 0.0, 0.0
    for _ in range(step):
        pred = m * x + c; m -= 0.01 * (2 / 200) * ((pred - y) * x).sum(); c -= 0.01 * (2 / 200) * (pred - y).sum()
    a1.plot(xs, m * xs + c, color=col, lw=1.6, label=lab)
a1.legend(fontsize=8, frameon=False, labelcolor=GREY, loc="upper left"); a1.set_xlabel("x"); a1.set_ylabel("y")
a1.set_title("Regression: a line learned by walking downhill on the squared error", fontsize=9.5)
a2.plot(np.arange(len(L)), L, color=PURPLE, lw=1.5)
a2.set_yscale("log"); a2.set_xlabel("epoch"); a2.set_ylabel("mean squared error (log)")
a2.set_title("A 2–3–1 network learning XOR: the loss back propagation drives down", fontsize=9.5)
fig.tight_layout(); save(fig, "ai-learning-curves.svg")

# ------------------------------------------------------------------ 4. deep vs shallow
d = np.load(f"{S}/spiral.npz")
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
for ax, key, title in zip(axes, ("shallow", "deep"), ("one hidden layer of 64 — 87.5% on unseen points", "three hidden layers of 10 — 98.8% on unseen points")):
    style(ax)
    ax.contourf(d["g"], d["g"], d[key], levels=[0, 0.5, 1], colors=[BLUE, RED], alpha=0.18)
    ax.contour(d["g"], d["g"], d[key], levels=[0.5], colors=[GREY], linewidths=1.0)
    X, Y = d["X"], d["Y"].ravel()
    ax.scatter(X[Y == 0, 0], X[Y == 0, 1], s=6, color=BLUE); ax.scatter(X[Y == 1, 0], X[Y == 1, 1], s=6, color=RED)
    ax.set_title(title, fontsize=9.5); ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
fig.suptitle("Same budget of weights, arranged wide or deep — the deep net follows the spiral, the wide one gives up on the outer turns", fontsize=9.5, color=GREY)
fig.tight_layout(); save(fig, "ai-deep-vs-shallow.svg")

# ------------------------------------------------------------------ 5. unsupervised + reinforcement
k = np.load(f"{S}/kmeans.npz"); Q = np.load(f"{S}/qtable.npy")
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 4.3))
for ax in (a1, a2): style(ax)
for j, col in enumerate((BLUE, GREEN, PURPLE)):
    sel = k["assign"] == j
    a1.scatter(k["X"][sel, 0], k["X"][sel, 1], s=8, color=col, alpha=0.7)
a1.scatter(k["C"][:, 0], k["C"][:, 1], marker="x", s=90, color=RED, lw=2, label="centres found")
a1.legend(fontsize=8, frameon=False, labelcolor=GREY); a1.set_title("Unsupervised: k-means given 300 unlabelled points, told 'find 3 groups'", fontsize=9)
a2.set_xlim(-0.5, 4.5); a2.set_ylim(-0.5, 4.5); a2.set_aspect("equal"); a2.invert_yaxis()
a2.set_xticks(range(5)); a2.set_yticks(range(5)); a2.set_xlabel("column"); a2.set_ylabel("row")
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for r in range(5):
    for c in range(5):
        if (r, c) == (4, 4): a2.add_patch(FancyBboxPatch((c - 0.4, r - 0.4), 0.8, 0.8, boxstyle="round,pad=0.02", fc=GREEN, alpha=0.35, ec=GREEN)); a2.text(c, r, "+10", ha="center", va="center", fontsize=8, color=GREY); continue
        if (r, c) == (2, 2): a2.add_patch(FancyBboxPatch((c - 0.4, r - 0.4), 0.8, 0.8, boxstyle="round,pad=0.02", fc=RED, alpha=0.35, ec=RED)); a2.text(c, r, "−10", ha="center", va="center", fontsize=8, color=GREY); continue
        a = int(np.argmax(Q[r, c])); dr, dc = moves[a]
        a2.add_patch(FancyArrowPatch((c - 0.22 * dc, r - 0.22 * dr), (c + 0.28 * dc, r + 0.28 * dr), arrowstyle="-|>", color=TEAL, lw=1.4, mutation_scale=11))
a2.text(0, 0, "S", ha="center", va="center", fontsize=8, color=AMBER, weight="bold")
a2.set_title("Reinforcement: the policy Q-learning found from reward alone (arrow = best action)", fontsize=9)
fig.tight_layout(); save(fig, "ai-unsupervised-reinforcement.svg")

# ------------------------------------------------------------------ 6. expert system
fig, ax = plt.subplots(figsize=(10, 3.9)); style(ax); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 3.9)
box(ax, 0.3, 1.2, 1.9, 1.3, "Interface\nthe user answers questions;\nthe diagnosis comes back", BLUE, fs=7.8)
box(ax, 3.0, 2.2, 2.2, 1.1, "Knowledge base\nfacts about the world\n+ facts about this case", TEAL, fs=7.8)
box(ax, 3.0, 0.3, 2.2, 1.1, "Rule base\nIF conditions THEN conclusion\n(written by human experts)", AMBER, fs=7.8)
box(ax, 6.2, 1.2, 2.2, 1.3, "Inference engine\nfinds rules whose IF-part is met,\nadds their conclusions, repeats", PURPLE, fs=7.8)
box(ax, 8.9, 1.35, 1.0, 1.0, "answer", GREEN, fs=8)
for (x1, y1, x2, y2) in ((2.2, 1.85, 3.0, 2.6), (2.2, 1.85, 3.0, 0.95), (5.2, 2.6, 6.2, 2.0), (5.2, 0.95, 6.2, 1.7), (8.4, 1.85, 8.9, 1.85)):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", color=GREY, lw=1.0, mutation_scale=10))
ax.add_patch(FancyArrowPatch((7.3, 2.52), (4.1, 3.32), arrowstyle="-|>", color=RED, lw=1.0, mutation_scale=10, connectionstyle="arc3,rad=0.4"))
ax.text(6.1, 3.45, "conclusions written back as new facts — forward chaining", ha="center", fontsize=7.8, color=RED)
ax.set_title("An expert system: the four components 0478 names, and the loop that makes it think", fontsize=10)
save(fig, "ai-expert-system.svg")

"""Figures for The Modern CPU vs the Textbook Model.md — run after modern-cpu-simulator.py; the measured numbers
in figure 2 are typed in from a run of modern-cpu-lab.c on the machine named in the card (they are inputs, not
computed here, so that the figure records the run the card quotes)."""
import re, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

TXT = "#888"; BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": TXT, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT, "axes.edgecolor": TXT, "font.size": 10, "svg.fonttype": "none"})

def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name).read(); m = re.search(r"<svg[^>]*>", s)
    tag = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)).replace("<svg", '<svg width="100%"', 1)
    open(name, "w").write(s[:m.start()] + tag + s[m.end():]); plt.close(fig)

def box(ax, x, y, w, h, text, col, fs=9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc=col, alpha=0.15, ec=col, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=col, fontsize=fs)

# ── 1. the contract and the engine ─────────────────────────────────────────────────────────────────────────────
fig, (a, b) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1, 2.2]})
for ax in (a, b): ax.axis("off")
a.set_xlim(0, 4); a.set_ylim(0, 5.4); a.set_title("the textbook CPU: the contract", color=TXT, fontsize=10)
box(a, 0.4, 4.2, 3.2, 0.8, "control unit: fetch, decode, execute\none instruction at a time", BLUE)
box(a, 0.4, 3.0, 1.5, 0.8, "one ALU", PURPLE); box(a, 2.1, 3.0, 1.5, 0.8, "registers\nPC, MAR, MDR, ACC", TEAL)
box(a, 0.4, 1.8, 3.2, 0.8, "three buses to memory", AMBER); box(a, 0.4, 0.6, 3.2, 0.8, "memory", GREY := "#777")
for y0, y1 in ((4.2, 3.8), (3.0, 2.6), (1.8, 1.4)): a.annotate("", xy=(2.0, y1), xytext=(2.0, y0), arrowprops=dict(arrowstyle="-|>", color=TXT, lw=1))
a.text(2.0, 0.15, "what a program is allowed to assume", ha="center", color=TXT, fontsize=9)
b.set_xlim(0, 9); b.set_ylim(0, 5.4); b.set_title("a 2020s core: the engine that honours the contract (numbers for an Apple Firestorm core)", color=TXT, fontsize=10)
box(b, 0.3, 4.4, 2.6, 0.75, "branch predictor\nguesses the path far ahead", AMBER, 8.5)
box(b, 3.1, 4.4, 2.6, 0.75, "fetch and decode\n8 per cycle, into micro-ops", BLUE, 8.5)
box(b, 5.9, 4.4, 2.8, 0.75, "rename\n32 names onto ~400 registers", TEAL, 8.5)
box(b, 0.3, 3.1, 8.4, 0.85, "reorder buffer, ~630 entries: every instruction in flight, in program order, waiting to commit", PURPLE, 9)
box(b, 0.3, 1.9, 8.4, 0.85, "schedulers: any instruction whose operands are ready issues now, whatever its position in the program", PURPLE, 9)
units = [("ALU", 6, BLUE), ("load/store", 4, TEAL), ("FP / SIMD", 4, GREEN), ("branch", 2, AMBER)]
x = 0.3
for name, n, col in units:
    w = 8.4 * n / 16; box(b, x, 0.75, w - 0.1, 0.8, f"{name}\n×{n}", col, 8.5); x += w
b.text(4.5, 0.25, "commit: results become visible in program order, so the contract holds; a mispredicted branch throws the window away", ha="center", color=TXT, fontsize=8.5)
for y0, y1 in ((4.4, 3.95), (3.1, 2.75), (1.9, 1.55)): b.annotate("", xy=(4.5, y1), xytext=(4.5, y0), arrowprops=dict(arrowstyle="-|>", color=TXT, lw=1))
save(fig, "modern-cpu-contract-and-engine.svg")

# ── 2. three measurements on one laptop (modern-cpu-lab.c, Apple M1 Max, cc -O1) ──────────────────────────────
meas = [("branch:\nunsorted vs sorted", 3.86, 1.27, "ns per element"), ("additions:\n1 chain vs 8 chains", 1.020, 0.127, "ns per add"), ("memory:\nrandom vs sequential", 145.6, 1.49, "ns per load")]
fig, axes = plt.subplots(1, 3, figsize=(11, 3.8))
for ax, (lab, slow, fast, unit) in zip(axes, meas):
    ax.bar([0, 1], [slow, fast], color=[RED, GREEN], width=0.6)
    for i, v in enumerate([slow, fast]): ax.text(i, v * 1.03, f"{v:g}", ha="center", color=TXT, fontsize=10)
    ax.set_xticks([0, 1]); ax.set_xticklabels(lab.split(" vs ")[0].split("\n")[1] + "" if False else ["slow", "fast"]); ax.set_ylabel(unit); ax.set_title(lab, fontsize=10)
    ax.text(0.5, max(slow, fast) * 0.9, f"×{slow / fast:.0f}" if slow / fast >= 10 else f"×{slow / fast:.1f}", ha="center", color=PURPLE, fontsize=13, fontweight="bold")
    ax.set_ylim(0, max(slow, fast) * 1.18); ax.grid(alpha=.25, axis="y")
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
axes[0].set_xticklabels(["unsorted", "sorted"]); axes[1].set_xticklabels(["1 chain", "8 chains"]); axes[2].set_xticklabels(["random", "sequential"])
fig.text(0.5, -0.04, "Same instructions each time. What changed: whether a branch is predictable, whether additions depend on each other, whether the next load is where the cache expects.", ha="center", color=TXT, fontsize=9.5)
save(fig, "modern-cpu-measurements.svg")

# ── 3. the simulator: one program, three machines ──────────────────────────────────────────────────────────────
D = json.load(open("modern-cpu-simulator.json"))
fig, ax = plt.subplots(figsize=(9, 4))
names = ["textbook", "pipeline", "ooo"]; labels = ["textbook\n(one at a time)", "in-order pipeline\n(static guess)", "out-of-order\n(6-wide, 2-bit predictor)"]
x = np.arange(3); w = 0.36
u = [D["unsorted"][n]["ipc"] for n in names]; s = [D["sorted"][n]["ipc"] for n in names]
ax.bar(x - w / 2, u, w, color=RED, label="unsorted data: the branch is a coin toss"); ax.bar(x + w / 2, s, w, color=GREEN, label="sorted data: the branch is predictable")
for i in range(3):
    ax.text(x[i] - w / 2, u[i] + 0.08, f"{u[i]:.2f}", ha="center", color=TXT, fontsize=9); ax.text(x[i] + w / 2, s[i] + 0.08, f"{s[i]:.2f}", ha="center", color=TXT, fontsize=9)
ax.set_xticks(x); ax.set_xticklabels(labels); ax.set_ylabel("instructions completed per cycle (IPC)")
ax.set_title("modern-cpu-simulator.py: the same 17 957 instructions on three machines", fontsize=10)
ax.legend(frameon=False, fontsize=9); ax.grid(alpha=.25, axis="y"); ax.set_ylim(0, 5.2)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
save(fig, "modern-cpu-simulator.svg")
print("wrote 3 SVGs")

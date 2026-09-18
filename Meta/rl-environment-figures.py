"""
rl-environment-figures.py — two figures for [[You Are a Reinforcement Learner]].
Run rl-environment-sim.py first (it saves the series).

  you-are-a-reinforcement-learner-loop.svg   the agent–environment loop, drawn twice: the
                                             textbook one, and the one where the environment
                                             contains other agents whose environment is you
  you-are-a-reinforcement-learner-sims.svg   proper vs proxy reward; delay vs steps to
                                             deliver; the helper under three neighbours
Vault style: text #888, no background rect, width="100%" + viewBox.
"""
import re, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
GREY = "#888888"; BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
S = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad"
def style(ax):
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelcolor=GREY); ax.xaxis.label.set_color(GREY); ax.yaxis.label.set_color(GREY); ax.title.set_color(GREY); ax.set_facecolor("none")
def save(fig, name):
    fig.patch.set_alpha(0); fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    s = open(name).read().replace('<svg ', '<svg width="100%" ', 1)
    s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1)
    open(name, "w").write(s); print("wrote", name)
def box(ax, x, y, w, h, text, col, fs=9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15", fc=col, ec=col, alpha=0.18, lw=0))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15", fc="none", ec=col, lw=1.2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=GREY)
def arrow(ax, a, b, col, text=None, rad=0.0, fs=8.5, tpos=None):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", color=col, lw=1.4, mutation_scale=12, connectionstyle=f"arc3,rad={rad}"))
    if text: ax.text(*(tpos or ((a[0]+b[0])/2, (a[1]+b[1])/2 + 0.18)), text, ha="center", fontsize=fs, color=col)

# ---------------------------------------------------------------- loop
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2))
for ax in (a1, a2): style(ax); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5)
box(a1, 0.6, 1.8, 2.6, 1.4, "Agent\n(policy: state → action)", BLUE)
box(a1, 6.6, 1.8, 2.8, 1.4, "Environment\n(state, reward)", GREEN)
arrow(a1, (3.25, 3.0), (6.55, 3.0), BLUE, "action", rad=-0.3, tpos=(4.9, 3.9))
arrow(a1, (6.55, 2.0), (3.25, 2.0), GREEN, "new state · reward", rad=-0.3, tpos=(4.9, 0.85))
a1.text(5, 0.2, "the loop as the textbook draws it: one agent, and everything else is 'environment'", ha="center", fontsize=8.5, color=GREY)
a1.set_title("Reinforcement learning", fontsize=10.5)
box(a2, 0.4, 1.8, 2.4, 1.4, "You\n(learning from\nwhat comes back)", BLUE, fs=8.5)
box(a2, 4.0, 3.5, 2.3, 1.2, "Colleague\n(also learning)", PURPLE, fs=8.5)
box(a2, 4.0, 0.3, 2.3, 1.2, "Institution\n(its reward rules)", AMBER, fs=8.5)
box(a2, 7.4, 1.8, 2.3, 1.4, "Task\n(the thing itself)", GREEN, fs=8.5)
arrow(a2, (2.85, 3.15), (3.95, 4.1), BLUE, "your thanks, credit, pay", fs=7.5, tpos=(2.6, 4.45))
arrow(a2, (3.95, 3.6), (2.85, 2.75), PURPLE, "their help", fs=7.5, tpos=(3.85, 2.95))
arrow(a2, (2.85, 2.25), (3.95, 1.35), BLUE, "your work", fs=7.5, tpos=(2.55, 1.55))
arrow(a2, (3.95, 0.85), (2.85, 1.85), AMBER, "its reward (or its silence)", fs=7.5, tpos=(3.3, 0.45))
arrow(a2, (6.35, 4.1), (7.5, 3.25), PURPLE)
arrow(a2, (6.35, 0.85), (7.5, 1.75), AMBER)
a2.add_patch(FancyArrowPatch((8.55, 1.75), (1.6, 1.75), arrowstyle="-|>", color=GREEN, lw=1.4, mutation_scale=12, connectionstyle="arc3,rad=-0.62"))
a2.text(5.1, -1.05, "what the task itself returns — the only signal that cannot lie", ha="center", fontsize=7.5, color=GREEN)
a2.set_ylim(-1.3, 5.0)
a2.set_title("The same loop, honestly drawn: you are someone else's environment", fontsize=10.5)
fig.tight_layout(); save(fig, "you-are-a-reinforcement-learner-loop.svg")

# ---------------------------------------------------------------- sims
prop = np.load(f"{S}/part1-proper.npy"); prox = np.load(f"{S}/part1-proxy.npy")
dl = np.load(f"{S}/delay.npz"); hp = np.load(f"{S}/helper.npz")
fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
for ax in axes: style(ax)
w = 20
for arr, col, lab in ((prop, GREEN, "paid on delivery"), (prox, RED, "paid per checkpoint tag")):
    axes[0].plot(np.convolve(arr[:, 0], np.ones(w) / w, mode="valid") * 100, color=col, lw=1.6, label=lab)
axes[0].set_xlabel("episode"); axes[0].set_ylabel("deliveries (%, 20-episode average)"); axes[0].set_ylim(-3, 103)
axes[0].legend(fontsize=8, frameon=False, labelcolor=GREY, loc="center right"); axes[0].set_title("Same agent, two reward signals", fontsize=9.5)
ks = [0, 1, 3, 6, 12]; means = [dl[f"k{k}"][-200:].mean() for k in ks]
axes[1].plot(ks, means, "o-", color=PURPLE, lw=1.6); axes[1].axhline(10, color=GREY, lw=0.8, ls=":"); axes[1].text(11.5, 10.6, "shortest path", fontsize=7.5, color=GREY, ha="right")
axes[1].set_xlabel("delay before the reward arrives (steps)"); axes[1].set_ylabel("steps to deliver, last 200 episodes"); axes[1].set_title("Late reward, slower learner", fontsize=9.5)
for key, col, lab in (("neighbour_rewards_help_(+3)", GREEN, "neighbour rewards help"), ("neighbour_rewards_help_for_300_rounds,_then_stops", AMBER, "rewards, then stops at round 300"), ("neighbour_never_rewards", RED, "never rewards")):
    h = hp[key]; axes[2].plot(np.convolve(h, np.ones(40) / 40, mode="valid") * 100, color=col, lw=1.6, label=lab)
axes[2].axvline(300, color=GREY, lw=0.8, ls=":"); axes[2].set_xlabel("round"); axes[2].set_ylabel("helping (%, 40-round average)"); axes[2].set_ylim(-3, 103)
axes[2].legend(fontsize=7.5, frameon=False, labelcolor=GREY, loc="center right"); axes[2].set_title("The helper, under three neighbours", fontsize=9.5)
fig.tight_layout(); save(fig, "you-are-a-reinforcement-learner-sims.svg")

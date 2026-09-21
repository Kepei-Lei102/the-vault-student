"""Figures for [[Planning an Experiment]].  Self-contained: python3 planning-an-experiment-figures.py
Every SVG: text #888, width=100%, no background, checked in light and dark."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": GREY, "axes.labelcolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "axes.edgecolor": GREY, "svg.fonttype": "none", "font.size": 9.5})
rng = np.random.default_rng(11)
TRUE_K, SIGMA_R = 5.20, 0.08


def style(ax):
    ax.set_facecolor("none")
    for sp in ax.spines.values():
        sp.set_color(GREY)


def save(fig, name):
    fig.patch.set_alpha(0)
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    txt = open(name).read()
    txt = txt.replace('width="', 'data-w="', 1).replace('height="', 'data-h="', 1)
    txt = txt.replace("<svg ", '<svg width="100%" ', 1)
    open(name, "w").write(txt)


def box(ax, xy, w, h, text, col, fs=9):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc=col + "26", ec=col, lw=1.5))
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=fs, color=GREY, linespacing=1.35)


def arrow(ax, a, b, col=GREY):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12, color=col, lw=1.3))


# 1. the skeleton of a plan, in two rows
fig, ax = plt.subplots(figsize=(11, 5.2)); style(ax); ax.set_xlim(0, 11); ax.set_ylim(0, 5.2); ax.axis("off")
top = [("THE QUESTION\nhow does X\naffect Y?", GREY), ("VARIABLES\nchange X (independent)\nmeasure Y (dependent)\nhold the rest (control)", PURPLE),
       ("APPARATUS\none instrument for\nevery quantity\nyou named", BLUE), ("METHOD\nset X, measure Y,\nthen change X\nand repeat", BLUE)]
bot = [("ENOUGH DATA\nat least 5 values of X,\nwidely spread; repeat\neach and average", GREEN), ("TABLE\na column per quantity,\nheading = quantity / unit", TEAL),
       ("ANALYSIS\nplot Y against X,\naxes named; or compare\ndown the table", AMBER), ("READ IT BACK\ncould a stranger\ncarry this out?", RED)]
for i, (t, c) in enumerate(top):
    box(ax, (0.2 + i * 2.7, 3.0), 2.4, 1.6, t, c)
    if i: arrow(ax, (0.2 + i * 2.7 - 0.3, 3.8), (0.2 + i * 2.7, 3.8))
for i, (t, c) in enumerate(bot):
    box(ax, (0.2 + i * 2.7, 0.5), 2.4, 1.6, t, c)
    if i: arrow(ax, (0.2 + i * 2.7 - 0.3, 1.3), (0.2 + i * 2.7, 1.3))
ax.add_patch(FancyArrowPatch((9.5, 3.0), (1.4, 2.1), arrowstyle="-|>", mutation_scale=12, color=GREY, lw=1.3, connectionstyle="arc3,rad=0.0"))
ax.text(5.5, 4.95, "A plan is a chain: each link exists because the one before it demanded it", ha="center", fontsize=10.5, color=GREY)
ax.text(5.5, 0.15, "the last box is free marks: most lost marks are links the writer never noticed were missing", ha="center", fontsize=8.5, color=GREY, style="italic")
save(fig, "planning-an-experiment-skeleton.svg")

# 2. range and number: two rows of two
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
for ax, (lo, hi, title, col) in zip(axes[0], [(0.40, 0.60, "5 lengths, 0.40–0.60 m: forty students' best-fit lines", RED),
                                              (0.10, 1.00, "5 lengths, 0.10–1.00 m: the same forty students", GREEN)]):
    style(ax)
    L = np.linspace(lo, hi, 5); xs = np.array([0, 1.05])
    grads = []
    for k in range(40):
        R = TRUE_K * L + rng.normal(0, SIGMA_R, 5)
        m, c = np.polyfit(L, R, 1); grads.append(m)
        ax.plot(xs, m * xs + c, color=col, lw=0.7, alpha=0.45)
        if k == 0: ax.plot(L, R, "x", color=GREY, ms=6, mew=1.4)
    ax.axvspan(lo, hi, color=col, alpha=0.08)
    ax.set_xlim(0, 1.05); ax.set_ylim(-0.5, 6.2); ax.set_xlabel("length of wire / m"); ax.set_ylabel("resistance / Ω")
    ax.set_title(title + f"\ngradients spread over ±{np.std(grads):.2f} Ω/m", fontsize=9.5)
ax = axes[1][0]; style(ax)
names = ["2, narrow", "5, narrow", "2, wide", "5, wide", "5, wide,\n×3 repeats", "10, wide"]
vals = [10.9, 9.8, 2.4, 2.2, 1.3, 1.7]
ax.bar(names, vals, color=[RED, RED, AMBER, GREEN, GREEN, GREEN], alpha=0.75)
for i, v in enumerate(vals): ax.text(i, v + 0.25, f"{v} %", ha="center", fontsize=8.5, color=GREY)
ax.set_ylim(0, 12.5); ax.set_ylabel("uncertainty in the gradient / %"); ax.set_title("What each plan costs: 4000 simulated experiments per plan", fontsize=9.5)
ax.tick_params(axis="x", labelsize=8)
ax = axes[1][1]; style(ax)
V = np.linspace(0.5, 6, 200); I = 0.30 * (V / 6) ** 0.6
ax.plot(I, V, color=GREY, lw=1, alpha=0.6, label="the lamp's true curve")
V2 = np.array([1.0, 6.0]); ax.plot(0.30 * (V2 / 6) ** 0.6, V2, "o-", color=RED, ms=7, lw=1.5, label="2 readings: a perfect line")
V6 = np.linspace(1, 6, 6); ax.plot(0.30 * (V6 / 6) ** 0.6, V6, "x", color=GREEN, ms=8, mew=2, label="6 readings: the curve shows")
ax.set_xlabel("current / A"); ax.set_ylabel("p.d. / V"); ax.legend(frameon=False, fontsize=8.5, labelcolor=GREY)
ax.set_title("Why two wide readings are still not enough:\ntwo points always lie on a straight line", fontsize=9.5)
fig.tight_layout(); save(fig, "planning-an-experiment-range.svg")

# 3. the confounder
thick = np.array([0, 2, 4, 6, 8.0]); ROOM = 22.0
def rate(t, s, minutes=5.0):
    k = 0.060 / (1 + 0.35 * t); return (s - (ROOM + (s - ROOM) * np.exp(-k * minutes))) / minutes
ctrl = rate(thick, 80.0); start = 88.0 - 4.0 * np.arange(5)
drift = rate(thick, start); rev = rate(thick, start[::-1])
fig, ax = plt.subplots(figsize=(8.4, 4.6)); style(ax)
ax.plot(thick, ctrl, "o-", color=GREEN, lw=2, label="start temperature held at 80 °C: rate falls by 71 %")
ax.plot(thick, drift, "s--", color=RED, lw=1.6, label="kettle cooling between trials, thin first: looks like 78 %")
ax.plot(thick, rev, "^--", color=AMBER, lw=1.6, label="same kettle, thick first: looks like 61 %")
ax.set_xlabel("thickness of insulation / mm"); ax.set_ylabel("rate of cooling / °C per minute")
ax.set_title("One uncontrolled variable, three different answers to the same question", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, labelcolor=GREY)
fig.tight_layout(); save(fig, "planning-an-experiment-confound.svg")
print("three SVGs written")

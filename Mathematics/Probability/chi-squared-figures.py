"""Figures for the Chi-Squared Tests card.

Regenerate:  python3 chi-squared-figures.py
Writes chi-squared-die-experiment.svg, chi-squared-contingency-cells.svg and
chi-squared-salespeople-table.svg (the J25 Q3 table as printed, for the callout)
beside this file.

Figure 1 — left: chi-squared densities for nu = 1, 2, 4, 8 with each mean
marked (mean = nu: "one unit of miss per free cell"); right: a fair die rolled
60 times, X^2 computed, repeated 20,000 times — the pile of honest misfits
against the chi^2_5 curve, with the 5% cut at 11.07. Fixed seed, byte-stable.
Figure 2 — the 3x3 contingency table of 9231/44 J25 Q3: each cell shows the
observed count, the expected count under independence (row x col / N), and its
contribution to X^2, shaded by size. Row/column totals shown.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import re

AX = "#888888"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
RED = "#dc2626"
AMBER = "#f59e0b"
TEAL = "#0891b2"
GREY = "#9ca3af"

plt.rcParams.update({
    "text.color": AX,
    "axes.labelcolor": AX,
    "axes.edgecolor": AX,
    "xtick.color": AX,
    "ytick.color": AX,
    "font.size": 11,
    "font.family": "sans-serif",
    "svg.fonttype": "none",
    "svg.hashsalt": "vault",
})


def style(ax):
    for s in ("right", "top"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(AX)
        ax.spines[s].set_linewidth(1.1)
    ax.tick_params(colors=AX, labelsize=9.5)
    ax.grid(color=AX, alpha=0.12, lw=0.8)
    ax.set_axisbelow(True)


# ---------------------------------------------------------------- figure 1
def fig_die(seed=1900, reps=20000, rolls=60):
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.8, 4.7))

    # left: densities
    style(ax0)
    x = np.linspace(0.02, 16, 800)
    for nu, col in ((1, RED), (2, AMBER), (4, TEAL), (8, PURPLE)):
        y = stats.chi2.pdf(x, nu)
        ax0.plot(x, y, color=col, lw=2.1, label=rf"$\chi^2_{{{nu}}}$  ($\nu = {nu}$ free cell{'s' if nu > 1 else ''})", zorder=3)
        ax0.plot([nu], [stats.chi2.pdf(nu, nu)], "o", color=col, ms=5, zorder=4)
    ax0.set_xlim(0, 16)
    ax0.set_ylim(0, 0.52)
    ax0.set_yticks([])
    ax0.set_xlabel(r"$X^2$", color=AX)
    ax0.legend(loc="upper right", frameon=False, labelcolor="linecolor", fontsize=10.5)
    ax0.set_title("the family $\\chi^2_\\nu$ — the subscript is ν, the number of free cells\nskewed right, never negative, mean = ν (the dot on each curve)",
                  color=AX, fontsize=11.5, pad=10)

    # right: honest die
    rng = np.random.default_rng(seed)
    faces = rng.integers(1, 7, size=(reps, rolls))
    counts = np.stack([(faces == f).sum(axis=1) for f in range(1, 7)], axis=1)
    E = rolls / 6
    X2 = ((counts - E) ** 2 / E).sum(axis=1)
    crit = stats.chi2.ppf(0.95, 5)
    frac = np.mean(X2 > crit)

    style(ax1)
    bins = np.arange(0, 20.5, 1.0)
    ax1.hist(X2, bins=bins, density=True, color=(37/255, 99/255, 235/255, 0.22), edgecolor=BLUE,
             lw=0.6, label=f"{reps:,} honest dice, 60 rolls each", zorder=2)
    xx = np.linspace(0.05, 20, 600)
    ax1.plot(xx, stats.chi2.pdf(xx, 5), color=PURPLE, lw=2.4, label=r"$\chi^2_5$ — Pearson's curve", zorder=4)
    ax1.axvline(crit, ymax=0.68, color=AMBER, lw=1.6, ls=(0, (5, 3)), zorder=3)
    ax1.text(crit + 0.3, 0.095, f"5% cut  {crit:.2f}\n{100*frac:.1f}% of honest dice\nland beyond it",
             color=AMBER, fontsize=10, va="top")
    ax1.axvline(5, color=GREY, lw=1.0, ls=(0, (2, 3)), zorder=1)
    ax1.text(4.8, 0.185, "mean 5 —\none unit per free face", color=GREY, fontsize=9.5, va="top", ha="right")
    ax1.set_xlim(0, 20)
    ax1.set_ylim(0, 0.20)
    ax1.set_yticks([])
    ax1.set_xlabel(r"$X^2 = \sum (O-E)^2/E$  for one experiment", color=AX)
    ax1.legend(loc="upper right", frameon=False, labelcolor=[BLUE, PURPLE], fontsize=10.5)
    ax1.set_title("Pearson's own kind of check: how much does a FAIR die misfit?\n(six faces, one fixed total, so five free cells)",
                  color=AX, fontsize=11.5, pad=10)

    fig.suptitle("the table is the record of how much an honest experiment misfits its own expectation",
                 color=AX, fontsize=11.5, y=0.035)
    fig.tight_layout(rect=[0, 0.07, 1, 1])
    fig.savefig("chi-squared-die-experiment.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    return frac


# ---------------------------------------------------------------- figure 2
def fig_contingency():
    O = np.array([[31, 40, 24], [23, 45, 29], [21, 25, 12]], dtype=float)
    rows = ["Avril", "Ben", "Charlie"]
    cols = ["Laptop", "Camera", "Television"]
    N = O.sum()
    E = np.outer(O.sum(axis=1), O.sum(axis=0)) / N
    C = (O - E) ** 2 / E

    fig, ax = plt.subplots(figsize=(9.6, 5.0))
    ax.set_xlim(-1.35, 3.6)
    ax.set_ylim(-1.05, 3.55)
    ax.set_aspect("equal")
    ax.axis("off")
    cmax = C.max()
    for i in range(3):
        for j in range(3):
            a = 0.08 + 0.42 * C[i, j] / cmax
            ax.add_patch(Rectangle((j, 2 - i), 1, 1, facecolor=(37/255, 99/255, 235/255, a),
                                   edgecolor=AX, lw=1.0, zorder=2))
            ax.text(j + 0.5, 2 - i + 0.72, f"O = {int(O[i, j])}", color=AX, fontsize=11.5,
                    ha="center", va="center", fontweight="bold")
            ax.text(j + 0.5, 2 - i + 0.46, f"E = {E[i, j]:.2f}", color=TEAL, fontsize=10.5,
                    ha="center", va="center")
            ax.text(j + 0.5, 2 - i + 0.20, f"{C[i, j]:.3f}", color=RED if C[i, j] == cmax else PURPLE,
                    fontsize=10.5, ha="center", va="center")
    for j, c in enumerate(cols):
        ax.text(j + 0.5, 3.15, c, color=AX, fontsize=11.5, ha="center", fontweight="bold")
        ax.text(j + 0.5, -0.32, f"{int(O[:, j].sum())}", color=AX, fontsize=11, ha="center")
    for i, r in enumerate(rows):
        ax.text(-0.12, 2 - i + 0.5, r, color=AX, fontsize=11.5, ha="right", va="center", fontweight="bold")
        ax.text(3.18, 2 - i + 0.5, f"{int(O[i].sum())}", color=AX, fontsize=11, va="center")
    ax.text(3.18, -0.32, f"{int(N)}", color=AX, fontsize=11, fontweight="bold")
    ax.text(-0.12, -0.32, "column totals", color=AX, fontsize=9.5, ha="right")
    ax.text(3.18, 3.15, "row totals", color=AX, fontsize=9.5)
    ax.text(1.5, -0.78,
            rf"$E = \dfrac{{\text{{row}} \times \text{{col}}}}{{N}}$  in each cell;  contribution $\dfrac{{(O-E)^2}}{{E}}$ shaded by size;  "
            rf"total $X^2 = {C.sum():.2f}$ against $\chi^2_4(0.90) = 7.779$",
            color=AX, fontsize=10.5, ha="center", va="top")
    ax.set_title("the salespeople table: what independence would predict, and how far each cell strays",
                 color=AX, fontsize=12, pad=8)
    fig.tight_layout()
    fig.savefig("chi-squared-contingency-cells.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    return C.sum()


# ---------------------------------------------------------------- figure 3
def fig_question_table():
    """The 9231/44 June 2025 Q3 table exactly as the paper prints it — an SVG
    because Obsidian will not render a markdown table inside a callout."""
    O = np.array([[31, 40, 24], [23, 45, 29], [21, 25, 12]])
    rows = ["Avril", "Ben", "Charlie"]
    cols = ["Laptop", "Camera", "Television"]
    fig, ax = plt.subplots(figsize=(6.6, 2.35))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.axis("off")
    cw = [1.15, 0.95, 0.95, 1.05, 0.9]          # column widths
    xs = np.concatenate([[0], np.cumsum(cw)])
    rh = 5 / 5
    # grid
    for i in range(6):
        y = 5 - i * rh
        lw = 1.4 if i in (0, 1, 4, 5) else 0.7
        ax.plot([0, xs[-1]], [y, y], color=AX, lw=lw, solid_capstyle="butt")
    for j, x in enumerate(xs):
        lw = 1.4 if j in (0, 1, 4, 5) else 0.7
        ax.plot([x, x], [0, 5], color=AX, lw=lw, solid_capstyle="butt")
    def cell(i, j, s, bold=False, color=AX):
        ax.text((xs[j] + xs[j + 1]) / 2, 5 - (i + 0.5) * rh, s, color=color, fontsize=11.5,
                ha="center", va="center", fontweight="bold" if bold else "normal")
    for j, c in enumerate(cols):
        cell(0, j + 1, c, bold=True)
    cell(0, 4, "Total", bold=True)
    for i, r in enumerate(rows):
        cell(i + 1, 0, r, bold=True)
        for j in range(3):
            cell(i + 1, j + 1, str(O[i, j]))
        cell(i + 1, 4, str(O[i].sum()))
    cell(4, 0, "Total", bold=True)
    for j in range(3):
        cell(4, j + 1, str(O[:, j].sum()))
    cell(4, 4, str(O.sum()), bold=True)
    fig.tight_layout(pad=0.2)
    fig.savefig("chi-squared-salespeople-table.svg", transparent=True, bbox_inches="tight",
                metadata={"Date": None})
    plt.close(fig)


def responsive(path):
    """Vault rule: root <svg> keeps its viewBox but scales — width 100%, no height."""
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    frac = fig_die()
    x2 = fig_contingency()
    fig_question_table()
    for f in ("chi-squared-die-experiment.svg", "chi-squared-contingency-cells.svg",
              "chi-squared-salespeople-table.svg"):
        responsive(f)
    print(f"honest dice beyond 11.07: {100*frac:.1f}%   contingency X^2 = {x2:.3f}")

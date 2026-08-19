"""Figures for the Probability Generating Functions card.

Regenerate:  python3 pgf-figures.py
Writes, beside this file:
  pgf-coat-hooks.svg            — the PGF as a shelf of hooks: G_X(t) = 0.1 + 0.3t
      + 0.4t^2 + 0.2t^3 (9231/43 J26 Q3) with each probability hung on the hook
      labelled by its value; then G'(t): each weight multiplied by its label and
      moved one hook down (so t = 1 adds them into E(X) = 1.7); then G''(t): once
      more (E[X(X-1)] = 2). Why the MF19 formulas are what they are.
  pgf-dice-convolution.svg      — two dice: the 6x6 grid of t^i . t^j = t^(i+j)
      coloured by total, and the bar chart of the total's distribution: multiplying
      the two PGFs collects every way to make each total — the product IS the
      convolution, and the coefficient of t^k is the count of ways.
  pgf-branching-extinction.svg  — the offspring PGF G(s) against the diagonal for
      three Poisson offspring means (0.8, 1, 1.6), with the cobweb of iterated
      generations from s = 0 climbing to the smallest fixed point: the extinction
      probability. Subcritical/critical: 1; supercritical: q < 1.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
from scipy import optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
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
    "text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX,
    "xtick.color": AX, "ytick.color": AX, "font.size": 11,
    "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault",
})


def style(ax, left=True):
    for s in ("right", "top"):
        ax.spines[s].set_visible(False)
    if not left:
        ax.spines["left"].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(AX)
        ax.spines[s].set_linewidth(1.1)
    ax.tick_params(colors=AX, labelsize=11)
    ax.grid(color=AX, alpha=0.12, lw=0.8)
    ax.set_axisbelow(True)


# ---------------------------------------------------------------- figure 1
def fig_hooks():
    p = np.array([0.1, 0.3, 0.4, 0.2])
    xs = np.arange(4)
    rows = [
        (p, [f"$t^{x}$" for x in xs], "$G_X(t) = 0.1 + 0.3t + 0.4t^2 + 0.2t^3$ — a shelf of hooks: the power says *where*, the coefficient says *how much*",
         "put $t = 1$: every hook counts once, the weights add to $1$", 1.0, BLUE),
        (p * xs, [f"$t^{x-1}$" if x >= 1 else "—" for x in xs], "$\\frac{dG_X}{dt} = 0\\times0.1 + 1\\times0.3 + 2\\times0.4\\,t + 3\\times0.2\\,t^2$ — differentiating reads each hook's label and multiplies the weight by it (then the hook drops one power)",
         "put $t = 1$: the weights add to $0.3 + 0.8 + 0.6 = 1.7 = E(X)$", 1.7, PURPLE),
        (p * xs * (xs - 1), [f"$t^{x-2}$" if x >= 2 else "—" for x in xs], "$\\frac{d^2G_X}{dt^2} = 2\\times1\\times0.4 + 3\\times2\\times0.2\\,t$ — read the label again: each weight is now $x(x-1)\\,p_x$",
         "put $t = 1$: $0.8 + 1.2 = 2 = E[X(X-1)]$, so $\\mathrm{Var}(X) = 2 + 1.7 - 1.7^2 = 0.81$", 2.0, GREEN),
    ]
    fig, axes = plt.subplots(3, 1, figsize=(10.5, 9.6))
    for ax, (w, labels, title, note, total, col) in zip(axes, rows):
        style(ax, left=True)
        ax.set_xlim(-0.7, 6.9)
        ax.set_ylim(0, 1.45)
        for x, wt, lab in zip(xs, w, labels):
            ax.plot([x, x], [1.32, 1.32 - 0.12], color=AX, lw=1.5)          # hook stem
            ax.text(x, 1.36, f"hook  {lab}" if lab != "—" else "hook  (gone)", color=AX, fontsize=11.5,
                    ha="center", va="bottom")
            if wt > 0:
                ax.bar(x, wt, width=0.5, bottom=0, color=col, alpha=0.75)
                ax.text(x, wt + 0.03, f"{wt:.1f}", color=AX, fontsize=12, ha="center", va="bottom")
            else:
                ax.text(x, 0.06, "0", color=GREY, fontsize=12, ha="center", va="bottom")
        ax.set_xticks(xs)
        ax.set_xticklabels([f"$x = {x}$" for x in xs], fontsize=11.5)
        ax.set_yticks([0, 0.5, 1.0])
        ax.set_ylabel("weight on the hook", color=AX, fontsize=11)
        ax.set_title(title, color=AX, fontsize=12, pad=8, loc="left")
        ax.text(4.0, 0.7, note.replace(": ", ":\n").replace(", so ", ",\nso ") + f"\n$= {total:g}$", color=col,
                fontsize=11.5, ha="left", va="center")
    fig.suptitle("the three MF19 lines are one move done three times: hang the probabilities on hooks $t^x$, "
                 "then let differentiation read the labels", color=AX, fontsize=12, y=0.015)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig("pgf-coat-hooks.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 2
def fig_dice():
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(9.5, 11.8), gridspec_kw={"height_ratios": [1.15, 1]})
    # top: 6x6 grid coloured by total
    ax0.set_xlim(-1.5, 6.3)
    ax0.set_ylim(-0.9, 6.9)
    ax0.set_aspect("equal")
    ax0.axis("off")
    cmap = plt.get_cmap("viridis")
    for i in range(1, 7):
        for j in range(1, 7):
            tot = i + j
            c = cmap((tot - 2) / 10)
            ax0.add_patch(Rectangle((i - 1, 6 - j), 1, 1, facecolor=(c[0], c[1], c[2], 0.35), edgecolor=AX, lw=0.8))
            ax0.text(i - 0.5, 6 - j + 0.5, f"$t^{{{tot}}}$", color=AX, fontsize=13.5, ha="center", va="center")
    for i in range(1, 7):
        ax0.text(i - 0.5, 6.25, f"$t^{i}$", color=BLUE, fontsize=14, ha="center", va="bottom")
        ax0.text(-0.3, 6 - i + 0.5, f"$t^{i}$", color=PURPLE, fontsize=14, ha="right", va="center")
    ax0.text(3, 6.75, "first die:  $\\frac{1}{6}(t + t^2 + \\dots + t^6)$", color=BLUE, fontsize=13.5, ha="center", va="bottom")
    ax0.text(-1.15, 3, "second die:  $\\frac{1}{6}(t + t^2 + \\dots + t^6)$", color=PURPLE, fontsize=13.5, ha="center",
             va="center", rotation=90)
    ax0.text(3, -0.55, "each cell is one product $t^i \\times t^j = t^{i+j}$;  cells of one colour share a total —\n"
                       "the product of the two PGFs adds them up, colour by colour", color=AX, fontsize=13, ha="center", va="top")
    # bottom: distribution of the total
    style(ax1)
    tots = np.arange(2, 13)
    ways = np.array([min(k - 1, 13 - k) for k in tots])
    ax1.bar(tots, ways / 36, width=0.8, color=[cmap((k - 2) / 10) for k in tots], alpha=0.75, edgecolor=AX, lw=0.6)
    for k, w in zip(tots, ways):
        ax1.text(k, w / 36 + 0.004, f"{w}/36", color=AX, fontsize=12, ha="center", va="bottom")
    ax1.set_xticks(tots)
    ax1.tick_params(labelsize=12)
    ax1.set_xlabel("total on two dice", color=AX, fontsize=13.5)
    ax1.set_ylabel("probability = coefficient of $t^{k}$ in the product", color=AX, fontsize=12.5)
    ax1.set_ylim(0, 0.2)
    ax1.set_title("$G_{X+Y}(t) = G_X(t)\\,G_Y(t) = \\frac{1}{36}(t + \\dots + t^6)^2 = \\frac{1}{36}(t^2 + 2t^3 + 3t^4 + \\dots + 6t^7 + \\dots + t^{12})$",
                  color=AX, fontsize=13, pad=10)
    fig.suptitle("multiplying the polynomials is counting the ways:\nthe product of two PGFs is the PGF of the sum (de Moivre, 1730s)",
                 color=AX, fontsize=14, y=0.015)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig("pgf-dice-convolution.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 3
def fig_branching():
    fig, axes = plt.subplots(3, 1, figsize=(9.0, 13.2))
    ss = np.linspace(0, 1, 300)
    for ax, mu, col, title in zip(axes, (0.8, 1.0, 1.6), (GREEN, AMBER, RED),
                                  ("mean offspring $0.8$ — dies out for certain", "mean $1$ — still dies out (slowly)",
                                   "mean $1.6$ — survives with probability $1 - q$")):
        style(ax)
        G = lambda s, mu=mu: np.exp(mu * (s - 1))
        ax.plot(ss, ss, color=GREY, lw=1.2, ls=(0, (4, 3)))
        ax.plot(ss, G(ss), color=col, lw=2.4, label=f"$G(s) = e^{{{mu}(s-1)}}$")
        # cobweb from s = 0
        s = 0.0
        pts = []
        for it in range(14):
            g = G(s)
            ax.plot([s, s], [s, g], color=BLUE, lw=1.0, alpha=0.8)
            ax.plot([s, g], [g, g], color=BLUE, lw=1.0, alpha=0.8)
            pts.append(g)
            s = g
        q = optimize.brentq(lambda x: G(x) - x, 0, 1 - 1e-9) if mu > 1 else 1.0
        ax.plot([q], [q], "o", color=col, ms=7, zorder=5)
        ax.text(q + 0.02 if mu > 1 else 0.98, q - 0.07 if mu > 1 else q - 0.1, f"$q = {q:.3f}$" if mu > 1 else "$q = 1$",
                color=col, fontsize=14, ha="left" if mu > 1 else "right", va="top")
        ax.text(0.03, G(0) - 0.04, "$G(0) = p_0$: no children at all", color=AX, fontsize=12, va="top")
        ax.set_xlim(0, 1.02)
        ax.set_ylim(0, 1.02)
        ax.tick_params(labelsize=12)
        ax.set_xlabel("$s$", color=AX, fontsize=13)
        ax.set_title(title, color=AX, fontsize=14, pad=10)
        ax.legend(loc="upper left", frameon=False, fontsize=13, labelcolor="linecolor")
        ax.text(0.98, 0.04, "generation $n$ extinct with probability $G(G(\\dots G(0)))$ — the staircase",
                color=BLUE, fontsize=12, ha="right", va="bottom")
    fig.suptitle("the surname problem: extinction probability is the smallest fixed point $q = G(q)$\nof the offspring PGF — the staircase climbs to it",
                 color=AX, fontsize=14, y=0.012)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig("pgf-branching-extinction.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def responsive(path):
    """Vault rule: root <svg> keeps its viewBox but scales — width 100%, no height."""
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    fig_hooks()
    fig_dice()
    fig_branching()
    for f in ("pgf-coat-hooks.svg", "pgf-dice-convolution.svg", "pgf-branching-extinction.svg"):
        responsive(f)
    print("done")

"""Figures for the Non-Parametric Tests card.

Regenerate:  python3 nonparametric-figures.py
Writes, beside this file:
  nonparametric-information-ladder.svg  — the 9231/42 N25 Q1 salaries against the
      claimed median $32,500, heard three ways: signs only (sign test), signed
      ranks of the distances (Wilcoxon signed-rank), the raw distances (t-test) —
      with the $125,000 outlier showing why the ladder matters.
  nonparametric-tables-by-hand.svg      — the MF19 tables built by counting:
      left, the 64 equally likely sign patterns for n = 6 and the distribution of
      Q (sum of negative ranks), 5% cut at 2 (3/64); right, the 20 equally likely
      hands of 3 ranks from 6 for the rank-sum test, R_3 distribution, why the
      one-tailed 5% value is 6 and the two-tailed entry is a dash.
  nonparametric-jigsaw-two-verdicts.svg — 9231/41 J25 Q5: the same ten
      differences as signs (8 vs 2, p = 0.055, not significant) and as signed
      ranks (P = 51 vs Q = 4, T = 4 <= 10, significant).

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
from scipy import stats
from itertools import product, combinations
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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
    ax.tick_params(colors=AX, labelsize=9.5)
    ax.grid(color=AX, alpha=0.12, lw=0.8)
    ax.set_axisbelow(True)


# ---------------------------------------------------------------- figure 1
def fig_ladder():
    sal = np.array([18750, 30500, 125000, 42500, 25000, 26000, 52500, 23000,
                    27500, 19500, 25500, 33000, 30000, 21500, 29000])
    m0 = 32500
    d = sal - m0
    r = stats.rankdata(np.abs(d))
    fig, axes = plt.subplots(3, 1, figsize=(10.5, 10.8), sharex=False,
                             gridspec_kw={"height_ratios": [0.8, 1, 1.15]})

    # row 1 — signs only
    ax = axes[0]
    style(ax, left=False)
    ax.set_yticks([])
    ax.set_xlim(0, 16)
    ax.set_ylim(-1, 1.6)
    order = np.argsort(sal)
    for k, i in enumerate(order):
        col = GREEN if d[i] > 0 else RED
        ax.text(k + 1, -0.1, "+" if d[i] > 0 else "−", color=col, fontsize=24,
                ha="center", va="center", fontweight="bold")
    ax.set_xticks([])
    ax.text(0.2, 1.1, "the sign test hears:  which side of $32\\,500$?\n11 below, 4 above:  $B(15, \\frac{1}{2})$ gives $P(X \\leq 4) = 0.059$",
            color=AX, fontsize=13, va="center")
    ax.set_title("one sample of 15 salaries, one claim (median = $32\\,500$), heard three ways",
                 color=AX, fontsize=14, pad=10)

    # row 2 — signed ranks
    ax = axes[1]
    style(ax)
    ax.set_xlim(0, 16)
    ax.set_ylim(-16, 16)
    ax.axhline(0, color=AX, lw=1)
    for k, i in enumerate(order):
        col = GREEN if d[i] > 0 else RED
        h = r[i] if d[i] > 0 else -r[i]
        ax.bar(k + 1, h, width=0.6, color=col, alpha=0.75)
    ax.set_xticks([])
    ax.set_yticks([-15, -10, -5, 0, 5, 10, 15])
    ax.set_yticklabels(["15", "10", "5", "0", "5", "10", "15"])
    ax.set_ylabel("signed rank of $|x - 32\\,500|$", color=AX, fontsize=12)
    ax.tick_params(labelsize=11)
    P = r[d > 0].sum(); Q = r[d < 0].sum()
    ax.text(0.2, 12.5, f"the Wilcoxon signed-rank test hears:  which side, and how far in rank order\n"
                       f"$P = {P:.0f}$, $Q = {Q:.0f}$", color=AX, fontsize=13, va="center")
    ax.text(15.8, -13, "…but only fair if the population is symmetric —\nand salaries are not",
            color=AMBER, fontsize=12.5, va="center", ha="right")

    # row 3 — raw distances
    ax = axes[2]
    style(ax)
    ax.set_xlim(0, 16)
    lim = 100000
    ax.set_ylim(-20000, lim)
    ax.axhline(0, color=AX, lw=1)
    for k, i in enumerate(order):
        col = GREEN if d[i] > 0 else RED
        ax.bar(k + 1, d[i], width=0.6, color=col, alpha=0.75)
    ax.set_xticks(range(1, 16))
    ax.set_xticklabels([f"{sal[i]/1000:g}k" for i in order], fontsize=11, rotation=0)
    ax.set_yticks([0, 25000, 50000, 75000, 100000])
    ax.set_yticklabels(["0", "25k", "50k", "75k", "100k"])
    ax.tick_params(axis="y", labelsize=11)
    ax.set_ylabel("$x - 32\\,500$  (\\$)", color=AX, fontsize=12)
    ax.text(0.2, 88000, "the $t$-test hears the actual distances — and one salary of $125\\,000$\n"
                        "is now $92\\,500$ above: it drags the mean and $s$ with it",
            color=AX, fontsize=13, va="center")
    ax.text(14.35, 78000, "the outlier", color=RED, fontsize=12, ha="right")
    ax.set_xlabel("the fifteen salaries, sorted", color=AX, fontsize=12.5)

    fig.suptitle("each rung uses more of the data, and needs more of the population to be true —\n"
                 "it assumes: nothing;  symmetry;  normality",
                 color=AX, fontsize=13.5, y=0.015)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig("nonparametric-information-ladder.svg", transparent=True, bbox_inches="tight",
                metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 2
def fig_tables_by_hand():
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10.5, 10.2))

    # top: n = 6 signed-rank, distribution of Q over 64 sign patterns
    n = 6
    cQ = Counter(sum(i + 1 for i in range(n) if bits[i]) for bits in product([0, 1], repeat=n))
    qs = np.arange(0, 22)
    counts = np.array([cQ.get(q, 0) for q in qs])
    style(ax0)
    cols = [AMBER if q <= 2 else BLUE for q in qs]
    ax0.bar(qs, counts, width=0.8, color=cols, alpha=0.8)
    ax0.set_xlim(-0.7, 21.7)
    ax0.set_ylim(0, 8.2)
    ax0.set_xticks(range(0, 22, 3))
    ax0.set_yticks(range(0, 6))
    ax0.set_xlabel("$Q$ = sum of the ranks that came out negative   ($n = 6$)", color=AX, fontsize=12.5)
    ax0.set_ylabel("number of sign patterns (out of 64)", color=AX, fontsize=12)
    ax0.tick_params(labelsize=11)
    ax0.axvline(2.5, color=AMBER, lw=1.8, ls=(0, (5, 3)))
    ax0.text(3.0, 8.05, "$Q \\leq 2$: 3 patterns of 64 = 4.7%, under 5%\nso the table entry is 2  ($n=6$, one-tailed 5%)",
             color=AMBER, fontsize=12.5, va="top")
    ax0.text(3.0, 6.4, "$Q \\leq 3$: 5 of 64 = 7.8% — too many, so not 3",
             color=GREY, fontsize=12.5, va="top")
    ax0.set_title("signed-rank: under $H_0$ each rank 1…6 is $+$ or $-$ by a fair coin\n"
                  "$2^6 = 64$ equally likely patterns — count them, and the table appears",
                  color=AX, fontsize=13.5, pad=10)

    # bottom: m = 3, n = 3 rank-sum, distribution of R_3 over the 20 hands
    cR = Counter(sum(cmb) for cmb in combinations(range(1, 7), 3))
    rs = np.arange(6, 16)
    counts = np.array([cR.get(x, 0) for x in rs])
    style(ax1)
    cols = [AMBER if x == 6 else BLUE for x in rs]
    ax1.bar(rs, counts, width=0.8, color=cols, alpha=0.8)
    ax1.set_xlim(5.3, 15.7)
    ax1.set_ylim(0, 6.2)
    ax1.set_xticks(range(6, 16))
    ax1.set_yticks(range(0, 5))
    ax1.set_xlabel("$R_3$ = sum of the 3 ranks dealt to the smaller sample   ($m = 3$, $n = 3$)", color=AX, fontsize=12.5)
    ax1.set_ylabel("number of hands (out of 20)", color=AX, fontsize=12)
    ax1.tick_params(labelsize=11)
    ax1.text(6.7, 6.1, "$R_3 = 6$ only for the hand $\\{1,2,3\\}$: 1 of 20 = 5%\nso the one-tailed 5% entry is 6",
             color=AMBER, fontsize=12.5, va="top")
    ax1.text(6.7, 4.85, "two-tailed 5% needs a tail of 2.5% — no hand is that rare,\nso the table prints a dash",
             color=GREY, fontsize=12.5, va="top")
    ax1.set_title("rank-sum: under $H_0$ the 6 ranks are dealt at random, 3 to each sample\n"
                  "$\\binom{6}{3} = 20$ equally likely hands — count them",
                  color=AX, fontsize=13.5, pad=10)

    fig.suptitle("the MF19 tables are not measured — they are counted:  both tests assume nothing about the\n"
                 "population's shape (only symmetry / identity), so the count is exact",
                 color=AX, fontsize=13, y=0.015)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig("nonparametric-tables-by-hand.svg", transparent=True, bbox_inches="tight",
                metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 3
def fig_jigsaw():
    seaside = np.array([182, 130, 193, 181, 192, 204, 184, 192, 180, 189])
    cartoon = np.array([161, 111, 195, 159, 202, 200, 168, 165, 145, 160])
    d = seaside - cartoon
    r = stats.rankdata(np.abs(d))
    kids = list("ABCDEFGHIJ")
    order = np.argsort(np.abs(d))
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10.5, 9.0), gridspec_kw={"height_ratios": [0.7, 1.3]})

    # top: signs
    style(ax0, left=False)
    ax0.set_yticks([])
    ax0.set_xlim(0, 11)
    ax0.set_ylim(-1.2, 1.6)
    for k, i in enumerate(order):
        col = GREEN if d[i] > 0 else RED
        ax0.text(k + 1, 0.0, "+" if d[i] > 0 else "−", color=col, fontsize=28, ha="center",
                 va="center", fontweight="bold")
        ax0.text(k + 1, -0.8, kids[i], color=AX, fontsize=12, ha="center")
    ax0.set_xticks([])
    ax0.text(5.5, 1.15, "8 plus, 2 minus.   $P(X \\geq 8) = 0.055 > 0.05$", color=AX, fontsize=13.5, ha="center")
    ax0.set_title("paired-sample sign test: not significant\n(the two minus signs count as much as any plus)",
                  color=AX, fontsize=13.5, pad=10)

    # bottom: signed ranks
    style(ax1)
    ax1.set_xlim(0, 11)
    ax1.set_ylim(-4, 11.5)
    ax1.axhline(0, color=AX, lw=1)
    for k, i in enumerate(order):
        col = GREEN if d[i] > 0 else RED
        h = r[i] if d[i] > 0 else -r[i]
        ax1.bar(k + 1, h, width=0.62, color=col, alpha=0.8)
        ax1.text(k + 1, h + (0.3 if h > 0 else -0.35), f"{d[i]:+d}", color=AX, fontsize=8.5, ha="center",
                 va="bottom" if h > 0 else "top")
    ax1.set_xticks(range(1, 11))
    ax1.set_xticklabels([kids[i] for i in order])
    ax1.set_yticks([-3, 0, 3, 6, 9])
    ax1.set_yticklabels(["3", "0", "3", "6", "9"])
    ax1.set_ylabel("signed rank of $|d |$   (numbers: $d$ in seconds)", color=AX, fontsize=9.5)
    ax1.text(5.5, 10.6, "$P = 51$, $Q = 1 + 3 = 4$, $T = 4 \\leq 10$", color=AX, fontsize=10.5, ha="center")
    ax1.set_title("Wilcoxon matched-pairs signed-rank: significant\n(the two minus differences are the smallest and third-smallest)",
                  color=AX, fontsize=11, pad=8)

    fig.suptitle("the same ten children, two verdicts: the sign test counts heads, the signed-rank test weighs them",
                 color=AX, fontsize=11.5, y=0.02)
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig("nonparametric-jigsaw-two-verdicts.svg", transparent=True, bbox_inches="tight",
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
    fig_ladder()
    fig_tables_by_hand()
    fig_jigsaw()
    for f in ("nonparametric-information-ladder.svg", "nonparametric-tables-by-hand.svg",
              "nonparametric-jigsaw-two-verdicts.svg"):
        responsive(f)
    print("done")

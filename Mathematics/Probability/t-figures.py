"""Figures for the t-Tests card.

Regenerate:  python3 t-figures.py
Writes t-vs-normal.svg, t-paired-vs-unpaired.svg and t-gosset-experiment.svg
beside this file. (t-choose-the-test.svg is a hand-written schematic.)

Figure 1 — t densities for nu = 1, 3, 10 against N(0,1), with the upper 2.5%
critical value marked on each: the tail that shrinks.
Figure 2 — the nine athletes of 9231/41 N25 Q6: left, before/after as two
columns joined per athlete (the between-athlete spread that drowns a two-sample
test); right, the nine differences with their mean, t-interval and the paired
t = 2.39 against the two-sample t = 0.30.

Figure 3 — Gosset's 1908 experiment rerun: 20,000 samples of four from a
normal population, the ratio (xbar - mu)/(s/sqrt n) tallied against t_3 and
against N(0,1). Fixed seed, so the figure is byte-stable.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
from scipy import stats
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
def fig_t_vs_normal():
    x = np.linspace(-5, 5, 801)
    fig, ax = plt.subplots(figsize=(11.2, 4.9))
    style(ax)
    ax.plot(x, stats.norm.pdf(x), color=AX, lw=2.4, label=r"$N(0,1)$  —  $\nu = \infty$", zorder=4)
    curves = [(10, TEAL, r"$t_{10}$"), (3, PURPLE, r"$t_{3}$"), (1, RED, r"$t_{1}$")]
    for nu, col, lab in curves:
        ax.plot(x, stats.t.pdf(x, nu), color=col, lw=2.0, label=lab, zorder=3)
    # upper 2.5% points
    marks = [(np.inf, AX, 1.96, 0.36), (10, TEAL, stats.t.ppf(0.975, 10), 0.30),
             (3, PURPLE, stats.t.ppf(0.975, 3), 0.24), (1, RED, stats.t.ppf(0.975, 1), 0.18)]
    for nu, col, tc, yh in marks:
        ax.axvline(tc, color=col, lw=1.2, ls=(0, (4, 3)), alpha=0.85, ymax=yh / 0.42, zorder=2)
        label = f"{tc:.2f}" if tc < 5 else f"{tc:.1f}  (off the page)"
        xx = min(tc, 4.55)
        ax.text(xx, yh + 0.012, label, color=col, fontsize=10, ha="center")
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 0.42)
    ax.set_xlabel("$t$", color=AX)
    ax.set_yticks([])
    ax.legend(loc="upper left", frameon=False, labelcolor="linecolor", fontsize=11)
    ax.set_title("the same bell, fatter in the tails — and the upper 2.5% point for each",
                 color=AX, fontsize=12.5, pad=12)
    fig.text(0.5, 0.02,
             "the tail is the price of estimating σ from the sample; the fewer the numbers, the fatter the tail",
             color=AX, fontsize=11, ha="center")
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig("t-vs-normal.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 2
BEFORE = np.array([250, 251, 252, 267, 276, 291, 310, 320, 335])
AFTER = np.array([245, 251, 253, 261, 275, 293, 302, 313, 320])
NAMES = list("ABCDEFGHI")


def fig_paired():
    d = BEFORE - AFTER
    n = len(d)
    dbar, sd = d.mean(), d.std(ddof=1)
    t_paired = dbar / (sd / np.sqrt(n))
    t_two = stats.ttest_ind(BEFORE, AFTER, equal_var=True).statistic
    tcrit = stats.t.ppf(0.975, n - 1)
    lo, hi = dbar - tcrit * sd / np.sqrt(n), dbar + tcrit * sd / np.sqrt(n)

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.6, 5.0), gridspec_kw={"width_ratios": [1.05, 1]})

    # ---- left: two columns joined per athlete
    style(ax0)
    for i in range(n):
        col = GREEN if d[i] > 0 else (RED if d[i] < 0 else GREY)
        ax0.plot([0, 1], [BEFORE[i], AFTER[i]], color=col, lw=1.6, alpha=0.9, zorder=3)
    ax0.plot(np.zeros(n), BEFORE, "o", color=BLUE, ms=6, zorder=4)
    ax0.plot(np.ones(n), AFTER, "o", color=PURPLE, ms=6, zorder=4)
    ax0.set_xlim(-0.35, 1.35)
    ax0.set_xticks([0, 1])
    ax0.set_xticklabels(["before", "after"], fontsize=11)
    ax0.set_ylabel("1500 m time (s)", color=AX)
    ax0.set_title("nine athletes: an 85-second spread between runners,\n"
                  "a few seconds' change within each", color=AX, fontsize=11.5, pad=10)
    ax0.set_ylim(232, 342)
    ax0.text(0.5, 236, f"two-sample $t$ on these two columns:  $t = {t_two:.2f}$  — nothing to see",
             color=RED, fontsize=10.5, ha="center", va="center")

    # ---- right: the differences
    style(ax1)
    ax1.axvline(0, color=AX, lw=1.6, zorder=2)
    y = np.arange(n)[::-1]
    for i in range(n):
        col = GREEN if d[i] > 0 else (RED if d[i] < 0 else GREY)
        ax1.plot([0, d[i]], [y[i], y[i]], color=col, lw=2.2, alpha=0.9, zorder=3)
        ax1.plot([d[i]], [y[i]], "o", color=col, ms=6, zorder=4)
        ax1.text(-6.6, y[i], NAMES[i], color=AX, fontsize=9, ha="right", va="center")
    ax1.axvline(dbar, color=AMBER, lw=2.0, ls=(0, (5, 3)), zorder=3)
    ax1.axvspan(lo, hi, color=AMBER, alpha=0.10, zorder=1)
    ax1.text(dbar + 0.3, n - 0.55, rf"$\bar d = {dbar:.2f}$", color=AMBER, fontsize=10.5, va="center")
    ax1.text(16.8, -1.05, f"95% interval [{lo:.1f}, {hi:.1f}]", color=AMBER, fontsize=9.8, ha="right")
    ax1.set_xlim(-7.5, 17)
    ax1.set_ylim(-1.5, n - 0.2)
    ax1.set_yticks([])
    ax1.set_xlabel("difference  before − after  (s)", color=AX)
    ax1.set_title(f"the same nine athletes as differences:\npaired $t = {t_paired:.2f}$ against $t_8(0.95) = 1.86$",
                  color=AX, fontsize=11.5, pad=10)

    fig.suptitle("same numbers, two designs — the two-sample test compares four seconds against eighty; "
                 "the paired test compares each runner with himself",
                 color=AX, fontsize=11.5, y=0.035)
    fig.tight_layout(rect=[0, 0.07, 1, 1])
    fig.savefig("t-paired-vs-unpaired.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    return t_paired, t_two, (lo, hi)


# ---------------------------------------------------------------- figure 3
def fig_gosset(seed=1908, reps=20000, n=4):
    rng = np.random.default_rng(seed)
    x = rng.normal(0.0, 1.0, size=(reps, n))
    t = x.mean(axis=1) / (x.std(axis=1, ddof=1) / np.sqrt(n))
    nu = n - 1
    beyond196 = np.mean(np.abs(t) > 1.96)
    tcrit = stats.t.ppf(0.975, nu)
    beyondcrit = np.mean(np.abs(t) > tcrit)

    fig, ax = plt.subplots(figsize=(11.2, 4.9))
    style(ax)
    bins = np.linspace(-6, 6, 97)
    ax.hist(t, bins=bins, density=True, color=(37/255, 99/255, 235/255, 0.22),
            edgecolor=BLUE, lw=0.6, label=f"{reps:,} samples of {n} — the ratio, tallied", zorder=2)
    xx = np.linspace(-6, 6, 601)
    ax.plot(xx, stats.t.pdf(xx, nu), color=PURPLE, lw=2.4, label=rf"$t_{{{nu}}}$ — Gosset's curve", zorder=4)
    ax.plot(xx, stats.norm.pdf(xx), color=AX, lw=2.0, ls=(0, (5, 3)), label=r"$N(0,1)$ — what $z$ would assume", zorder=3)
    for c, col in ((1.96, AX), (tcrit, PURPLE)):
        ax.axvline(c, color=col, lw=1.1, ls=(0, (3, 3)), alpha=0.8, zorder=1)
        ax.axvline(-c, color=col, lw=1.1, ls=(0, (3, 3)), alpha=0.8, zorder=1)
    ax.text(1.96 + 0.08, 0.335, r"$\pm 1.96$", color=AX, fontsize=10)
    ax.text(tcrit + 0.08, 0.275, rf"$\pm {tcrit:.2f}$", color=PURPLE, fontsize=10)
    ax.text(3.35, 0.19, f"beyond $\\pm 1.96$:  {100*beyond196:.1f}% of ratios\n(the normal table promised 5%)",
            color=RED, fontsize=10.5, va="top")
    ax.text(3.35, 0.115, f"beyond $\\pm {tcrit:.2f}$:  {100*beyondcrit:.1f}%\n(the $t_3$ table promised 5%)",
            color=PURPLE, fontsize=10.5, va="top")
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 0.42)
    ax.set_yticks([])
    ax.set_xlabel(r"$t = (\bar{x} - \mu)\,/\,(s/\sqrt{n})$", color=AX)
    ax.legend(loc="upper left", frameon=False, labelcolor=[BLUE, PURPLE, AX], fontsize=10.5)
    ax.set_title("Gosset's experiment, rerun: samples of four from a normal population",
                 color=AX, fontsize=12.5, pad=12)
    fig.text(0.5, 0.02, "the ratio follows the fat-tailed curve, not the normal — a theorem, and a thing you can check in a second",
             color=AX, fontsize=11, ha="center")
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig("t-gosset-experiment.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    return beyond196, beyondcrit


def responsive(path):
    """Vault rule: root <svg> keeps its viewBox but scales — width 100%, no height."""
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    fig_t_vs_normal()
    tp, tt, ci = fig_paired()
    b196, bcrit = fig_gosset()
    for f in ("t-vs-normal.svg", "t-paired-vs-unpaired.svg", "t-gosset-experiment.svg"):
        responsive(f)
    print(f"gosset rerun: beyond ±1.96 = {100*b196:.1f}%   beyond ±t3(.975) = {100*bcrit:.1f}%")
    print(f"paired t = {tp:.3f}   two-sample t = {tt:.3f}   95% CI for mean difference = [{ci[0]:.2f}, {ci[1]:.2f}]")
    for nu in (1, 3, 10):
        print(f"t_{nu}(0.975) = {stats.t.ppf(0.975, nu):.3f}")

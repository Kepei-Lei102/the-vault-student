"""Figure for the Summation of Series card — convergence lives in the partial sums.

Regenerate:  python3 summation-partial-sums.py
Writes summation-partial-sums.svg beside this file.

Both series have terms that shrink to zero. Only one of them converges, and the
difference is visible only in S_n — which is exactly what the syllabus means by
"by direct consideration of a sum to n terms".

Vault palette: all text #888, transparent background.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import re

AX = "#888888"
GREEN = "#059669"     # converges
RED = "#dc2626"       # diverges
AMBER = "#f59e0b"     # the limit
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


def figure():
    N = 40
    r = np.arange(1, N + 1)

    terms_ours = 1.0 / (r * (r + 1) * (r + 2))
    terms_harm = 1.0 / r
    S_ours = np.cumsum(terms_ours)
    S_harm = np.cumsum(terms_harm)

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.4, 4.5))

    # ---- left: the terms. Both go to zero. ----
    style(ax0)
    ax0.plot(r, terms_harm, "o-", color=RED, ms=3.6, lw=1.4, label=r"$u_r = \dfrac{1}{r}$")
    ax0.plot(r, terms_ours, "o-", color=GREEN, ms=3.6, lw=1.4,
             label=r"$u_r = \dfrac{1}{r(r+1)(r+2)}$")
    ax0.set_xlabel("$r$", color=AX)
    ax0.set_ylim(-0.02, 0.55)
    ax0.set_xlim(0, N + 1)
    ax0.legend(loc="upper right", frameon=False, labelcolor=AX, fontsize=11)
    ax0.set_title("the terms — both shrink to nothing", color=AX, fontsize=12, pad=12)
    ax0.annotate("both head for 0", (N * 0.62, 0.04), textcoords="offset points",
                 xytext=(0, 26), color=AX, fontsize=10.5, ha="center",
                 arrowprops=dict(arrowstyle="-|>", color=AX, lw=1, alpha=0.7))

    # ---- right: the partial sums. Only one settles. ----
    style(ax1)
    ax1.plot(r, S_harm, "o-", color=RED, ms=3.6, lw=1.5, label=r"$S_n$  (harmonic)")
    ax1.plot(r, S_ours, "o-", color=GREEN, ms=3.6, lw=1.5, label=r"$S_n$  (ours)")
    ax1.axhline(0.25, color=AMBER, lw=1.3, ls=(0, (5, 4)))
    ax1.text(N * 0.52, 0.40, r"$\frac{1}{4}$ — the sum to infinity",
             color=AMBER, fontsize=11)
    ax1.set_xlabel("$n$", color=AX)
    ax1.set_ylim(-0.15, 4.6)
    ax1.set_xlim(0, N + 1)
    ax1.legend(loc="upper left", frameon=False, labelcolor=AX, fontsize=11)
    ax1.set_title("the partial sums — only one of them settles", color=AX, fontsize=12, pad=12)
    ax1.annotate("climbing forever,\nslower and slower", (N * 0.86, S_harm[int(N * 0.86) - 1]),
                 textcoords="offset points", xytext=(-30, -46), color=RED, fontsize=10.5,
                 ha="center", arrowprops=dict(arrowstyle="-|>", color=RED, lw=1, alpha=0.8))
    ax1.annotate(f"flat at {S_ours[-1]:.4f}\nby $n = {N}$", (N, S_ours[-1]),
                 textcoords="offset points", xytext=(-14, 42), color=GREEN, fontsize=10.5,
                 ha="right", arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1, alpha=0.85))

    fig.suptitle("Shrinking terms are not enough. Convergence is a statement about "
                 r"$S_n$, and $S_n$ is what the method of differences hands you.",
                 color=AX, fontsize=12.5, y=0.035)
    fig.tight_layout(rect=[0, 0.075, 1, 1])
    fig.savefig("summation-partial-sums.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def responsive(path):
    """Vault rule: root <svg> keeps its viewBox but scales — width 100%, no height."""
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    figure()
    responsive("summation-partial-sums.svg")
    N = 40
    r = np.arange(1, N + 1)
    print("harmonic S_40 =", np.cumsum(1.0 / r)[-1])
    print("ours     S_40 =", np.cumsum(1.0 / (r * (r + 1) * (r + 2)))[-1], " limit 0.25")

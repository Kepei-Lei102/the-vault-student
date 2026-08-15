"""Figures for the Rational Functions and Graphs card.

Regenerate:  python3 rational-functions-figures.py
Writes rational-n24-curve.svg, rational-forbidden-band.svg,
rational-four-relatives.svg beside this file.

The specimen throughout is the real N24/13 Q6 curve
    f(x) = (4x² + x + 1)/(2x² − 7x + 3)
with asymptotes x = 1/2, x = 3, y = 2, stationary points (−1/3, 1/5), (1, −3).

Vault palette: all text #888, semi-transparent fills, transparent background.
"""

import numpy as np
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
GREY = "#9ca3af"

plt.rcParams.update({
    "text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX,
    "xtick.color": AX, "ytick.color": AX,
    "font.size": 11, "font.family": "sans-serif", "svg.fonttype": "none",
    "svg.hashsalt": "vault",
})


def style(ax):
    for s in ("right", "top"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(AX); ax.spines[s].set_linewidth(1.1)
    ax.tick_params(colors=AX, labelsize=9.5)
    ax.grid(color=AX, alpha=0.10, lw=0.8)
    ax.set_axisbelow(True)


def origin_axes(ax, o_dx=-0.32, o_dy=-0.55):
    """Comment-5 convention: bold solid x=0 and y=0 through the panel, O at the origin."""
    ax.axhline(0, color=AX, lw=1.8, zorder=3)
    ax.axvline(0, color=AX, lw=1.8, zorder=3)
    ax.text(o_dx, o_dy, "$O$", color=AX, fontsize=12, ha="right", va="top", zorder=3)


def f(x):
    return (4*x**2 + x + 1)/(2*x**2 - 7*x + 3)


def branches(fn, xmin, xmax, poles, n=3000, clip=18):
    """Yield x, y arrays per branch, poles excluded, values clipped."""
    cuts = [xmin] + sorted(poles) + [xmax]
    for a, b in zip(cuts[:-1], cuts[1:]):
        xs = np.linspace(a + 1e-4, b - 1e-4, n)
        ys = fn(xs)
        ys = np.where(np.abs(ys) > clip, np.nan, ys)
        yield xs, ys


# ----------------------------------------------------------------------
# Figure 1 — the N24 curve, fully annotated
# ----------------------------------------------------------------------
def n24_curve():
    fig, ax = plt.subplots(figsize=(11.0, 5.6))
    style(ax)
    origin_axes(ax, o_dx=-0.22, o_dy=-0.75)

    for xs, ys in branches(f, -6, 9, [0.5, 3]):
        ax.plot(xs, ys, color=PURPLE, lw=2.2, zorder=4)

    for xv in (0.5, 3):
        ax.axvline(xv, color=RED, lw=1.3, ls=(0, (5, 4)))
    ax.axhline(2, color=AMBER, lw=1.3, ls=(0, (5, 4)))
    ax.text(0.5, 8.6, r"$x=\frac{1}{2}$", color=RED, fontsize=10.5, ha="right")
    ax.text(3.05, 8.6, r"$x=3$", color=RED, fontsize=10.5)
    ax.text(-5.8, 2.35, r"$y=2$", color=AMBER, fontsize=10.5)

    ax.plot([-1/3], [1/5], "o", color=GREEN, ms=7, zorder=6)
    ax.plot([1], [-3], "o", color=GREEN, ms=7, zorder=6)
    ax.plot([0], [1/3], "o", color=BLUE, ms=6, zorder=6)
    ax.plot([1/3], [2], "s", color=AMBER, ms=6, zorder=6)
    ax.annotate(r"$\left(-\frac{1}{3},\ \frac{1}{5}\right)$ min", (-1/3, 1/5),
                textcoords="offset points", xytext=(-86, -20), color=GREEN, fontsize=10.5)
    ax.annotate(r"$\left(1, -3\right)$ max of the middle branch", (1, -3),
                textcoords="offset points", xytext=(12, -6), color=GREEN, fontsize=10.5)
    ax.annotate(r"$\left(0, \frac{1}{3}\right)$", (0, 1/3),
                textcoords="offset points", xytext=(-46, 8), color=BLUE, fontsize=10.5)
    ax.annotate("crosses its own asymptote\nat $x = \\frac{1}{3}$", (1/3, 2),
                textcoords="offset points", xytext=(-118, 26), color=AMBER, fontsize=9.5)

    ax.set_xlim(-6, 9); ax.set_ylim(-9.5, 9.5)
    ax.set_title(r"$y = \dfrac{4x^2+x+1}{2x^2-7x+3}$ — the November 2024 curve: "
                 "three branches, three asymptotes, and every feature the syllabus names",
                 color=AX, fontsize=11.5, pad=12)
    fig.tight_layout()
    fig.savefig("rational-n24-curve.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 2 — the forbidden band: discriminant method, no calculus
# ----------------------------------------------------------------------
def forbidden_band():
    fig, ax = plt.subplots(figsize=(10.6, 5.4))
    style(ax)
    origin_axes(ax, o_dx=-0.22, o_dy=-0.75)

    for xs, ys in branches(f, -6, 9, [0.5, 3]):
        ax.plot(xs, ys, color=PURPLE, lw=2.2, zorder=4)

    ax.axhspan(-3, 0.2, color=RED, alpha=0.10, zorder=1)
    ax.axhline(-3, color=RED, lw=1.4, zorder=2)
    ax.axhline(0.2, color=RED, lw=1.4, zorder=2)
    ax.plot([1], [-3], "o", color=GREEN, ms=8, zorder=6)
    ax.plot([-1/3], [1/5], "o", color=GREEN, ms=8, zorder=6)

    ax.text(6.6, -1.4, "the forbidden band  $-3 < y < \\frac{1}{5}$:\nno point of the curve has these heights",
            color=RED, fontsize=11, ha="center", va="center", zorder=5)
    ax.annotate("the band's edges are the\nturning values — found by a\ndiscriminant, not a derivative",
                (-1/3, 1/5), textcoords="offset points", xytext=(-150, 40),
                color=GREEN, fontsize=10.5,
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.2, alpha=0.85))

    ax.set_xlim(-6, 9); ax.set_ylim(-8.5, 8.5)
    ax.set_title(r"Treat $y$ as known and ask when $x$ can be real: "
                 r"$(2y-4)x^2-(7y+1)x+(3y-1)=0$ needs $5(y+3)(5y-1)\geq 0$",
                 color=AX, fontsize=11.5, pad=12)
    fig.tight_layout()
    fig.savefig("rational-forbidden-band.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 3 — the four relatives of y = f(x), stacked for readability
# ----------------------------------------------------------------------
def four_relatives():
    fig, axes = plt.subplots(4, 1, figsize=(11.0, 13.6))
    lims = dict(xmin=-6, xmax=9, poles=[0.5, 3])

    specs = [
        ("$y^2 = f(x)$", "exists only where $f \\geq 0$ — the red dotted stretches of $f$ produce no curve at all; mirror-symmetric in the $x$-axis"),
        ("$y = \\dfrac{1}{f(x)}$", "zeros and vertical asymptotes swap roles; the horizontal asymptote $y=2$ becomes $y=\\frac{1}{2}$; signs are preserved"),
        ("$y = |f(x)|$", "everything below the $x$-axis reflects up; the sliding line $y=k$ is tangent at $k=3$"),
        ("$y = f(|x|)$", "the $x \\geq 0$ half is kept and mirrored left; the original left half (red dotted) is discarded"),
    ]

    for ax, (title, note) in zip(axes.flat, specs):
        style(ax)
        origin_axes(ax, o_dx=-0.18, o_dy=-0.4)
        ax.set_xlim(-6, 9)
        ax.set_title(title + "   —   " + note, color=AX, fontsize=11.5, pad=8, loc="left")
        # the vertical asymptotes of the original, for orientation
        for xv in (0.5, 3):
            ax.axvline(xv, color=RED, lw=1.0, ls=(0, (5, 4)), alpha=0.65)

    # ---- y² = f : original shown grey where f>=0, RED DOTTED where f<0 ----
    ax = axes[0]
    for xs, ys in branches(f, **lims):
        pos = ys >= 0
        ax.plot(np.where(pos, xs, np.nan), np.where(pos, ys, np.nan),
                color=GREY, lw=1.2, alpha=0.5, zorder=2)
        ax.plot(np.where(~pos, xs, np.nan), np.where(~pos, ys, np.nan),
                color=RED, lw=1.4, ls=(0, (2, 3)), alpha=0.8, zorder=2)
        ax.plot(np.where(pos, xs, np.nan), np.where(pos, np.sqrt(np.abs(ys)), np.nan),
                color=BLUE, lw=2.2, zorder=4)
        ax.plot(np.where(pos, xs, np.nan), np.where(pos, -np.sqrt(np.abs(ys)), np.nan),
                color=BLUE, lw=2.2, zorder=4)
    ax.axhline(np.sqrt(2), color=AMBER, lw=1.0, ls=(0, (5, 4)), alpha=0.8)
    ax.axhline(-np.sqrt(2), color=AMBER, lw=1.0, ls=(0, (5, 4)), alpha=0.8)
    ax.text(-5.85, 1.72, "$y=\\pm\\sqrt{2}$", color=AMBER, fontsize=9.5, ha="left")
    ax.set_ylim(-4.4, 4.6)

    # ---- 1/f ----
    ax = axes[1]
    for xs, ys in branches(f, **lims):
        ax.plot(xs, ys, color=GREY, lw=1.2, alpha=0.5, zorder=2)
        inv = np.where(np.abs(ys) > 1e-3, 1.0/ys, np.nan)
        inv = np.where(np.abs(inv) > 8, np.nan, inv)
        ax.plot(xs, inv, color=GREEN, lw=2.2, zorder=4)
    ax.axhline(0.5, color=AMBER, lw=1.1, ls=(0, (5, 4)))
    ax.text(8.85, 0.75, "$y=\\frac{1}{2}$", color=AMBER, fontsize=9.5, ha="right")
    ax.set_ylim(-6.5, 6.5)

    # ---- |f| ----
    ax = axes[2]
    for xs, ys in branches(f, **lims):
        ax.plot(xs, ys, color=GREY, lw=1.2, alpha=0.5, zorder=2)
        ax.plot(xs, np.abs(ys), color=PURPLE, lw=2.2, zorder=4)
    ax.axhline(2, color=AMBER, lw=1.0, ls=(0, (5, 4)), alpha=0.8)
    ax.axhline(3, color=RED, lw=1.1, ls=(0, (4, 4)))
    ax.text(-5.8, 3.35, "$k=3$: tangent — 4 solutions needs $k>3$", color=RED, fontsize=9.5, ha="left")
    ax.text(-5.85, 2.3, "$y=2$", color=AMBER, fontsize=9.5)
    ax.set_ylim(-1.2, 9.5)

    # ---- f(|x|) ----
    ax = axes[3]
    for xs, ys in branches(f, **lims):
        keep = xs >= 0
        ax.plot(np.where(~keep, xs, np.nan), np.where(~keep, ys, np.nan),
                color=RED, lw=1.4, ls=(0, (2, 3)), alpha=0.8, zorder=2)
        ax.plot(np.where(keep, xs, np.nan), np.where(keep, ys, np.nan),
                color=AMBER, lw=2.2, zorder=4)
        ax.plot(np.where(keep, -xs, np.nan), np.where(keep, ys, np.nan),
                color=AMBER, lw=2.2, zorder=4)
    ax.axvline(-0.5, color=RED, lw=1.0, ls=(0, (5, 4)), alpha=0.65)
    ax.axvline(-3, color=RED, lw=1.0, ls=(0, (5, 4)), alpha=0.65)
    ax.axhline(2, color=AMBER, lw=1.0, ls=(0, (5, 4)), alpha=0.8)
    ax.set_ylim(-9.5, 9.5)

    fig.suptitle("Four relatives of the same curve (grey). Red dotted = parts of the original that produce no curve in the relative.",
                 color=AX, fontsize=12.5, y=0.028)
    fig.tight_layout(rect=[0, 0.035, 1, 1])
    fig.savefig("rational-four-relatives.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 4 — the oblique asymptote, early and visual
# ----------------------------------------------------------------------
def oblique():
    fig, ax = plt.subplots(figsize=(10.2, 5.2))
    style(ax)
    origin_axes(ax, o_dx=-0.22, o_dy=-0.6)

    g = lambda x: (x**2 + 3)/(x - 1)
    for xs, ys in branches(g, -8, 10, [1], clip=24):
        ax.plot(xs, ys, color=PURPLE, lw=2.2, zorder=4)
    xs = np.linspace(-8, 10, 10)
    ax.plot(xs, xs + 1, color=AMBER, lw=1.4, ls=(0, (5, 4)), zorder=3)
    ax.axvline(1, color=RED, lw=1.3, ls=(0, (5, 4)))

    ax.annotate("$y = x + 1$ — the quotient,\nnow visible as the slant the\ncurve settles onto", (7.0, 8.0),
                textcoords="offset points", xytext=(-176, 44), color=AMBER, fontsize=10.5,
                arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=1.2, alpha=0.85))
    ax.annotate("the remainder $\\dfrac{4}{x-1}$ is the\ngap between curve and line —\nand it shrinks to nothing far out", (-5.0, -4.05),
                textcoords="offset points", xytext=(-60, -58), color=AX, fontsize=10)
    ax.text(1.12, -13.5, "$x=1$", color=RED, fontsize=10.5)
    ax.plot([-1], [-2], "o", color=GREEN, ms=7, zorder=6)
    ax.plot([3], [6], "o", color=GREEN, ms=7, zorder=6)

    ax.set_xlim(-8, 10); ax.set_ylim(-15, 17)
    ax.set_title(r"$y = \dfrac{x^2+3}{x-1} = x + 1 + \dfrac{4}{x-1}$ — one degree heavier on top, so the settling line slants",
                 color=AX, fontsize=11.5, pad=12)
    fig.tight_layout()
    fig.savefig("rational-oblique-asymptote.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 5 — the real world: saturation and resonance
# ----------------------------------------------------------------------
def real_world():
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.6, 4.7))

    # ---- Michaelis–Menten ----
    style(ax0)
    Vmax, Km = 10.0, 2.0
    S = np.linspace(0, 20, 400)
    ax0.plot(S, Vmax*S/(Km+S), color=GREEN, lw=2.4, zorder=4)
    ax0.axhline(Vmax, color=AMBER, lw=1.3, ls=(0, (5, 4)))
    ax0.axhline(Vmax/2, color=GREY, lw=0.9, ls=(0, (2, 3)), alpha=0.8)
    ax0.plot([Km, Km], [0, Vmax/2], color=GREY, lw=0.9, ls=(0, (2, 3)), alpha=0.8)
    ax0.plot([Km], [Vmax/2], "o", color=BLUE, ms=7, zorder=6)
    ax0.text(19.6, Vmax+0.45, "$V_{\\max}$ — every enzyme busy;\nthe horizontal asymptote", color=AMBER,
             fontsize=10, ha="right")
    ax0.annotate("$S = K_m$: rate is exactly $\\frac{1}{2}V_{\\max}$", (Km, Vmax/2),
                 textcoords="offset points", xytext=(16, -12), color=BLUE, fontsize=10)
    ax0.set_xlim(0, 20); ax0.set_ylim(0, 12.4)
    ax0.set_xlabel("substrate concentration $S$", color=AX)
    ax0.set_ylabel("rate $v$", color=AX)
    ax0.set_title(r"saturation: $v = \dfrac{V_{\max}S}{K_m+S}$", color=AX, fontsize=11.5, pad=10)

    # ---- peaking EQ, real biquad magnitude ----
    style(ax1)
    fr = np.logspace(np.log10(20), np.log10(20000), 800)
    f0, G = 1000.0, 12.0
    A = 10**(G/40)
    for Q, col, lab in [(0.7, GREEN, "$Q = 0.7$ — broad, musical"),
                        (4.0, RED, "$Q = 4$ — narrow, resonant")]:
        s_ = 1j*fr/f0
        H = (s_**2 + s_*(A/Q) + 1)/(s_**2 + s_/(A*Q) + 1)
        ax1.semilogx(fr, 20*np.log10(np.abs(H)), color=col, lw=2.2, label=lab)
    ax1.axhline(0, color=AX, lw=1.6, zorder=3)
    ax1.legend(loc="upper left", frameon=False, labelcolor=AX, fontsize=10)
    ax1.set_xlabel("frequency (Hz)", color=AX)
    ax1.set_ylabel("gain (dB)", color=AX)
    ax1.set_ylim(-2, 14.5)
    ax1.set_title("resonance: a $+12$ dB peaking EQ at $1$ kHz — two settings of Q",
                  color=AX, fontsize=11.5, pad=10)
    ax1.text(20000*0.9, 1.45, "flat far field: horizontal asymptote at 0 dB",
             color=AX, fontsize=9, ha="right")

    fig.suptitle("Two rational functions doing real work: the enzyme that cannot go faster, and the filter knob that slides poles.",
                 color=AX, fontsize=12.5, y=0.035)
    fig.tight_layout(rect=[0, 0.07, 1, 1])
    fig.savefig("rational-real-world.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def responsive(path):
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    n24_curve()
    forbidden_band()
    four_relatives()
    oblique()
    real_world()
    for fn in ["rational-n24-curve.svg", "rational-forbidden-band.svg", "rational-four-relatives.svg",
               "rational-oblique-asymptote.svg", "rational-real-world.svg"]:
        responsive(fn)
    print("wrote 5 figures")

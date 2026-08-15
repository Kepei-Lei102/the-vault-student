"""Figures for the Polar Coordinates card.

Regenerate:  python3 polar-figures.py
Writes polar-read-then-wrap.svg, polar-r-nonnegative.svg, polar-sector-slices.svg
beside this file.

The card's spine: a polar sketch is an ordinary r-against-theta graph, read
while turning. Figure 1 shows the same curve both ways; figure 2 shows what the
r >= 0 convention deletes; figure 3 derives the sector-area integral.

Vault palette: all text #888, semi-transparent fills, transparent background.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import re

AX = "#888888"
BLUE = "#2563eb"      # the r-theta graph (input reading)
PURPLE = "#7c3aed"    # the polar curve
GREEN = "#059669"     # kept / valid
RED = "#dc2626"       # forbidden / deleted
AMBER = "#f59e0b"     # highlights
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
    ax.grid(color=AX, alpha=0.12, lw=0.8)
    ax.set_axisbelow(True)


def polar_axes(ax, rmax, ticks):
    """Hand-drawn polar grid on a plain axes — circles + spokes, all #888."""
    ax.set_aspect("equal")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    th = np.linspace(0, 2*np.pi, 200)
    for R in ticks:
        ax.plot(R*np.cos(th), R*np.sin(th), color=AX, lw=0.7, alpha=0.22)
        ax.text(R*np.cos(1.25), R*np.sin(1.25), str(R), fontsize=8.5,
                color=GREY, ha="center", va="center", alpha=0.9)
    for a in np.arange(0, 2*np.pi, np.pi/4):
        ax.plot([0, rmax*np.cos(a)], [0, rmax*np.sin(a)], color=AX, lw=0.7, alpha=0.18)
    # initial line, slightly stronger with label
    ax.plot([0, rmax*1.06], [0, 0], color=AX, lw=1.3, alpha=0.75)
    ax.annotate("initial line  $\\theta = 0$", (rmax*1.02, 0), textcoords="offset points",
                xytext=(2, 7), fontsize=9.5, color=AX)
    ax.plot([0], [0], "o", ms=4, color=AX)
    ax.annotate("pole", (0, 0), textcoords="offset points", xytext=(-6, -14),
                fontsize=9.5, color=AX, ha="right")


# ----------------------------------------------------------------------
# Figure 1 — read the graph, then wrap it   (limaçon r = 3 + 2 sin θ)
# ----------------------------------------------------------------------
def read_then_wrap():
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.6, 4.9),
                                   gridspec_kw={"width_ratios": [1.15, 1]})
    th = np.linspace(-np.pi, np.pi, 600)
    r = 3 + 2*np.sin(th)

    # ---- left: ordinary graph ----
    style(ax0)
    ax0.plot(th, r, color=BLUE, lw=2.2)
    ax0.set_xlim(-np.pi*1.06, np.pi*1.2)
    ax0.set_ylim(0, 5.9)
    ax0.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax0.set_xticklabels([r"$-\pi$", r"$-\frac{\pi}{2}$", "0", r"$\frac{\pi}{2}$", r"$\pi$"])
    ax0.set_xlabel(r"$\theta$", color=AX)
    ax0.set_ylabel(r"$r$", color=AX, rotation=0, labelpad=10)
    ax0.set_title(r"first, read $r = 3 + 2\sin\theta$ as an ordinary graph",
                  color=AX, fontsize=11.5, pad=10)
    marks = [(-np.pi/2, 1, "min $r=1$", (10, -14)),
             (0, 3, "$r=3$", (8, -16)),
             (np.pi/2, 5, "max $r=5$", (8, 4))]
    for t0, r0, lab, off in marks:
        ax0.plot([t0], [r0], "o", color=AMBER, ms=7, zorder=5)
        ax0.annotate(lab, (t0, r0), textcoords="offset points", xytext=off,
                     color=AMBER, fontsize=10.5)
    ax0.text(-np.pi*0.98, 5.45, "never zero — so the curve\nnever visits the pole",
             fontsize=9.5, color=GREEN)

    # ---- right: the wrap ----
    polar_axes(ax1, 5.4, [1, 3, 5])
    ax1.plot(r*np.cos(th), r*np.sin(th), color=PURPLE, lw=2.4, zorder=4)
    for t0, r0, lab, off in [(-np.pi/2, 1, "$r=1$ at $\\theta=-\\frac{\\pi}{2}$", (14, -22)),
                             (0, 3, "$r=3$ at $\\theta=0$", (-4, 18)),
                             (np.pi/2, 5, "$r=5$ at $\\theta=\\frac{\\pi}{2}$", (10, 6))]:
        ax1.plot([r0*np.cos(t0)], [r0*np.sin(t0)], "o", color=AMBER, ms=7, zorder=6)
        ax1.annotate(lab, (r0*np.cos(t0), r0*np.sin(t0)), textcoords="offset points",
                     xytext=off, color=AMBER, fontsize=10)
    ax1.set_xlim(-5.9, 7.2); ax1.set_ylim(-2.6, 6.3)
    ax1.set_title("then wrap it: same values, read while turning",
                  color=AX, fontsize=11.5, pad=10)

    fig.suptitle("A polar sketch is not a new skill. It is graph-reading, performed while rotating.",
                 color=AX, fontsize=12.5, y=0.035)
    fig.tight_layout(rect=[0, 0.07, 1, 1])
    fig.savefig("polar-read-then-wrap.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 2 — the r >= 0 convention   (rose r = sin 3θ)
# ----------------------------------------------------------------------
def r_nonnegative():
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.6, 4.7),
                                   gridspec_kw={"width_ratios": [1.25, 1]})
    th = np.linspace(0, 2*np.pi, 1200)
    r = np.sin(3*th)

    # ---- left: the sine wave with dead zones ----
    style(ax0)
    pos = r >= 0
    ax0.plot(th, r, color=GREY, lw=1.2, alpha=0.5)
    ax0.plot(np.where(pos, th, np.nan), np.where(pos, r, np.nan), color=GREEN, lw=2.4)
    ax0.fill_between(th, r, 0, where=~pos, color=RED, alpha=0.12, lw=0)
    ax0.axhline(0, color=AX, lw=1)
    ax0.set_xlim(0, 2*np.pi*1.02)
    ax0.set_ylim(-1.25, 1.4)
    ax0.set_xticks([0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3, 2*np.pi])
    ax0.set_xticklabels(["0", r"$\frac{\pi}{3}$", r"$\frac{2\pi}{3}$", r"$\pi$",
                         r"$\frac{4\pi}{3}$", r"$\frac{5\pi}{3}$", r"$2\pi$"])
    ax0.set_xlabel(r"$\theta$", color=AX)
    ax0.set_title(r"$r = \sin 3\theta$ — three arches above the axis, three below",
                  color=AX, fontsize=11.5, pad=10)
    ax0.text(np.pi/6, 1.14, "arch 1", color=GREEN, fontsize=10, ha="center")
    ax0.text(np.pi*5/6, 1.14, "arch 2", color=GREEN, fontsize=10, ha="center")
    ax0.text(np.pi*3/2, 1.14, "arch 3", color=GREEN, fontsize=10, ha="center")
    ax0.text(np.pi/2, -1.13, "$r<0$: no curve", color=RED, fontsize=9.5, ha="center")
    ax0.text(np.pi*7/6, -1.13, "no curve", color=RED, fontsize=9.5, ha="center")
    ax0.text(np.pi*11/6, -1.13, "no curve", color=RED, fontsize=9.5, ha="center")

    # ---- right: the three petals ----
    polar_axes(ax1, 1.05, [1])
    for k in range(6):
        seg = (th >= k*np.pi/3) & (th <= (k+1)*np.pi/3)
        rr = np.sin(3*th[seg])
        if k % 2 == 0:
            ax1.plot(rr*np.cos(th[seg]), rr*np.sin(th[seg]), color=GREEN, lw=2.3, zorder=4)
    for lab, ang in [("1", np.pi/6), ("2", np.pi*5/6), ("3", np.pi*3/2)]:
        ax1.text(1.16*np.cos(ang), 1.16*np.sin(ang), lab, color=GREEN,
                 fontsize=11, ha="center", va="center", fontweight="bold")
    ax1.set_xlim(-1.7, 2.1); ax1.set_ylim(-1.55, 1.5)
    ax1.set_title("three petals — one per arch, and only three",
                  color=AX, fontsize=11.5, pad=10)

    fig.suptitle("Nothing here was memorised. The petal count is the number of arches where $r \\geq 0$ — read, not recalled.",
                 color=AX, fontsize=12.5, y=0.035)
    fig.tight_layout(rect=[0, 0.075, 1, 1])
    fig.savefig("polar-r-nonnegative.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 3 — sector slices   (the N24 loop r² = 3 sin 2θ)
# ----------------------------------------------------------------------
def sector_slices():
    fig, ax = plt.subplots(figsize=(11.8, 5.0))
    polar_axes(ax, 1.85, [1])

    th = np.linspace(0, np.pi/2, 400)
    r = np.sqrt(3*np.sin(2*th))
    ax.plot(r*np.cos(th), r*np.sin(th), color=PURPLE, lw=2.4, zorder=5)

    # thin sector slices
    N = 18
    edges = np.linspace(0, np.pi/2, N+1)
    for i in range(N):
        a, b = edges[i], edges[i+1]
        mid = (a+b)/2
        rm = np.sqrt(3*np.sin(2*mid))
        wedge = np.linspace(a, b, 8)
        ax.fill(np.concatenate([[0], rm*np.cos(wedge), [0]]),
                np.concatenate([[0], rm*np.sin(wedge), [0]]),
                color=PURPLE, alpha=0.10, lw=0)
    # one highlighted wedge
    a, b = edges[6], edges[7]
    mid = (a+b)/2; rm = np.sqrt(3*np.sin(2*mid))
    wedge = np.linspace(a, b, 12)
    ax.fill(np.concatenate([[0], rm*np.cos(wedge), [0]]),
            np.concatenate([[0], rm*np.sin(wedge), [0]]),
            color=AMBER, alpha=0.45, lw=0, zorder=4)
    ax.annotate(r"one slice: a circular sector," "\n"
                r"radius $r(\theta)$, angle $\delta\theta$" "\n"
                r"area $\approx \frac{1}{2}r^2\,\delta\theta$",
                (rm*np.cos(mid), rm*np.sin(mid)),
                textcoords="offset points", xytext=(64, 30), color=AMBER, fontsize=11,
                arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=1.2, alpha=0.9))

    ax.text(3.42, 1.46, r"add the slices and refine:", fontsize=11.5, color=AX)
    ax.text(3.42, 1.12, r"$A \;=\; \int \frac{1}{2}\,r^2\,\mathrm{d}\theta$", fontsize=15, color=AX)
    ax.text(3.42, 0.68, "the printed sector formula $\\frac{1}{2}r^2\\theta$\nis this integral with $r$ constant",
            fontsize=10.5, color=GREY)
    ax.text(3.42, 0.26, "here: $A = \\frac{1}{2}\\int_0^{\\pi/2} 3\\sin 2\\theta\\,\\mathrm{d}\\theta = \\frac{3}{2}$",
            fontsize=11.5, color=GREEN)

    ax.set_xlim(-0.9, 6.1); ax.set_ylim(-0.62, 2.15)
    ax.set_title("Why $\\frac{1}{2}\\int r^2\\,\\mathrm{d}\\theta$: the region sliced into thin sectors — "
                 "the loop is $r^2 = 3\\sin 2\\theta$, exactly as a real paper set it",
                 color=AX, fontsize=11.5, pad=12)
    fig.tight_layout()
    fig.savefig("polar-sector-slices.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)




# ----------------------------------------------------------------------
# Figure 4 — what allowing r < 0 would do   (rose r = sin 2θ)
# ----------------------------------------------------------------------
def negative_r():
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.4, 4.9))
    th = np.linspace(0, 2*np.pi, 1600)
    r = np.sin(2*th)

    for ax, title in [(ax0, "Cambridge, $r \\geq 0$: two petals"),
                      (ax1, "negative $r$ allowed: four — the extra two are\nthe arm pointing $backwards$")]:
        polar_axes(ax, 1.05, [1])
        ax.set_title(title, color=AX, fontsize=11.5, pad=10)
        ax.set_xlim(-1.75, 2.15); ax.set_ylim(-1.55, 1.5)

    # ---- left: r >= 0 only ----
    pos = r >= 0
    ax0.plot(np.where(pos, r*np.cos(th), np.nan), np.where(pos, r*np.sin(th), np.nan),
             color=GREEN, lw=2.4, zorder=4)
    ax0.text(0.62, 0.85, "1", color=GREEN, fontsize=12, fontweight="bold")
    ax0.text(-0.80, -0.98, "2", color=GREEN, fontsize=12, fontweight="bold")

    # ---- right: negative r plotted backwards ----
    ax1.plot(np.where(pos, r*np.cos(th), np.nan), np.where(pos, r*np.sin(th), np.nan),
             color=GREEN, lw=2.4, zorder=4)
    neg = ~pos
    ax1.plot(np.where(neg, r*np.cos(th), np.nan), np.where(neg, r*np.sin(th), np.nan),
             color=RED, lw=2.2, ls=(0, (5, 3)), zorder=4)
    ax1.text(0.62, 0.85, "1", color=GREEN, fontsize=12, fontweight="bold")
    ax1.text(-0.80, -0.98, "2", color=GREEN, fontsize=12, fontweight="bold")
    ax1.text(-0.86, 0.85, "3?", color=RED, fontsize=12, fontweight="bold")
    ax1.text(0.62, -0.98, "4?", color=RED, fontsize=12, fontweight="bold")
    # one explanatory arm: at θ=3π/4, r=-1 -> plotted at angle 3π/4+π
    t0 = 3*np.pi/4
    ax1.annotate("", xy=(-np.cos(t0), -np.sin(t0)), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6, alpha=0.9))
    ax1.annotate(r"at $\theta=\frac{3\pi}{4}$, $r=-1$:" "\nthe arm reverses\nthrough the pole",
                 (-np.cos(t0)*0.72, -np.sin(t0)*0.72), textcoords="offset points",
                 xytext=(26, -58), color=RED, fontsize=9.5)

    fig.suptitle("Same equation $r = \\sin 2\\theta$, two conventions. For even roses they genuinely disagree "
                 "— which is why petal counts must be read from the arches, not recalled from folklore.",
                 color=AX, fontsize=12, y=0.04)
    fig.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig("polar-negative-r.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def responsive(path):
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    read_then_wrap()
    r_nonnegative()
    sector_slices()
    negative_r()
    for f in ["polar-read-then-wrap.svg", "polar-r-nonnegative.svg", "polar-sector-slices.svg", "polar-negative-r.svg"]:
        responsive(f)
    print("wrote 4 figures")

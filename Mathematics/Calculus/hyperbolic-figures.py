"""Figures for the Hyperbolic Functions card.

Regenerate:  python3 hyperbolic-figures.py
Writes hyperbolic-circle-vs-hyperbola.svg and hyperbolic-graphs.svg beside this file.
Vault palette: all text #888, semi-transparent region fills, transparent background.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AX = "#888888"
BLUE = "#2563eb"      # circular / input
PURPLE = "#7c3aed"    # hyperbolic
GREEN = "#059669"     # tanh / result
AMBER = "#f59e0b"     # highlight
GREY = "#9ca3af"      # guides

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
    """Spines through the origin, everything #888."""
    for s in ("left", "bottom"):
        ax.spines[s].set_position("zero")
        ax.spines[s].set_color(AX)
        ax.spines[s].set_linewidth(1.2)
    for s in ("right", "top"):
        ax.spines[s].set_visible(False)
    ax.tick_params(which="both", colors=AX, labelsize=9.5)


# ----------------------------------------------------------------------
# Figure 1 — the parameter is an area, in both cases
# ----------------------------------------------------------------------
def circle_vs_hyperbola(t=1.2):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    # --- circle ---
    ax = axes[0]
    style(ax)
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color=BLUE, lw=2)

    u = np.linspace(0, t, 200)
    sector = np.column_stack([np.cos(u), np.sin(u)])
    poly = np.vstack([[0, 0], sector, [0, 0]])
    ax.fill(poly[:, 0], poly[:, 1], color=BLUE, alpha=0.20, lw=0)
    ax.plot([0, np.cos(t)], [0, np.sin(t)], color=AX, lw=1.2)
    ax.plot([0, 1], [0, 0], color=AX, lw=1.2)
    ax.plot([np.cos(t)], [np.sin(t)], "o", color=AMBER, ms=7, zorder=5)
    ax.annotate(r"$(\cos t,\ \sin t)$", (np.cos(t), np.sin(t)),
                textcoords="offset points", xytext=(10, 8), color=AMBER, fontsize=11)
    ax.text(0.42, 0.26, r"area $=\dfrac{t}{2}$", color=AX, fontsize=12)
    ax.set_title(r"$x^2 + y^2 = 1$      the unit circle", color=AX, fontsize=12, pad=14)
    ax.set_xlim(-1.45, 1.75)
    ax.set_ylim(-1.35, 1.55)
    ax.set_aspect("equal")

    # --- hyperbola ---
    ax = axes[1]
    style(ax)
    v = np.linspace(-1.65, 1.65, 400)
    ax.plot(np.cosh(v), np.sinh(v), color=PURPLE, lw=2)
    ax.plot(-np.cosh(v), np.sinh(v), color=PURPLE, lw=2, alpha=0.30)

    # asymptotes y = +/- x
    lim = 2.9
    ax.plot([-lim, lim], [-lim, lim], color=GREY, lw=1, ls=(0, (6, 4)), alpha=0.7)
    ax.plot([-lim, lim], [lim, -lim], color=GREY, lw=1, ls=(0, (6, 4)), alpha=0.7)

    u = np.linspace(0, t, 200)
    sector = np.column_stack([np.cosh(u), np.sinh(u)])
    poly = np.vstack([[0, 0], sector, [0, 0]])
    ax.fill(poly[:, 0], poly[:, 1], color=PURPLE, alpha=0.20, lw=0)
    ax.plot([0, np.cosh(t)], [0, np.sinh(t)], color=AX, lw=1.2)
    ax.plot([0, 1], [0, 0], color=AX, lw=1.2)
    ax.plot([np.cosh(t)], [np.sinh(t)], "o", color=AMBER, ms=7, zorder=5)
    ax.annotate(r"$(\cosh t,\ \sinh t)$", (np.cosh(t), np.sinh(t)),
                textcoords="offset points", xytext=(8, 8), color=AMBER, fontsize=11)
    ax.text(0.72, 0.24, r"area $=\dfrac{t}{2}$", color=AX, fontsize=12)
    ax.set_title(r"$x^2 - y^2 = 1$      the unit hyperbola", color=AX, fontsize=12, pad=14)
    ax.set_xlim(-2.6, 3.1)
    ax.set_ylim(-2.2, 2.6)
    ax.set_aspect("equal")

    fig.suptitle("The parameter $t$ is twice the shaded area — in both pictures. "
                 "Only one of them has an angle.",
                 color=AX, fontsize=12.5, y=0.035)
    fig.tight_layout(rect=[0, 0.07, 1, 1])
    fig.savefig("hyperbolic-circle-vs-hyperbola.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 2 — the three graphs
# ----------------------------------------------------------------------
def graphs():
    fig, ax = plt.subplots(figsize=(11, 5.2))
    style(ax)

    x = np.linspace(-2.6, 2.6, 600)
    ax.plot(x, np.cosh(x), color=PURPLE, lw=2.2, label=r"$\cosh x$")
    ax.plot(x, np.sinh(x), color=BLUE, lw=2.2, label=r"$\sinh x$")
    ax.plot(x, np.tanh(x), color=GREEN, lw=2.2, label=r"$\tanh x$")

    # the two halves cosh and sinh are built from
    ax.plot(x, np.exp(x) / 2, color=GREY, lw=1.2, ls=(0, (5, 4)), alpha=0.85)
    ax.plot(x, np.exp(-x) / 2, color=GREY, lw=1.2, ls=(0, (5, 4)), alpha=0.85)
    ax.text(2.42, np.exp(2.35) / 2, r"$\frac{1}{2}e^{x}$", color=GREY, fontsize=11)
    ax.text(-2.72, np.exp(2.35) / 2, r"$\frac{1}{2}e^{-x}$", color=GREY, fontsize=11)

    # tanh asymptotes
    for yv in (1, -1):
        ax.axhline(yv, color=AMBER, lw=1, ls=(0, (3, 4)), alpha=0.9)
    ax.text(-2.55, 1.12, r"$y = 1$", color=AMBER, fontsize=10)
    ax.text(-2.55, -1.34, r"$y = -1$", color=AMBER, fontsize=10)

    ax.plot([0], [1], "o", color=PURPLE, ms=6, zorder=5)
    ax.annotate(r"$\cosh 0 = 1$", (0, 1), textcoords="offset points",
                xytext=(16, 16), color=PURPLE, fontsize=11)

    ax.set_xlim(-2.75, 3.1)
    ax.set_ylim(-4.6, 5.6)
    ax.legend(loc="lower right", frameon=False, labelcolor=AX, fontsize=12)
    ax.set_title(r"$\cosh$ and $\sinh$ are the even and odd halves of $e^{x}$ — "
                 r"the dashed guides are the halves being added and subtracted",
                 color=AX, fontsize=12, pad=16)
    fig.tight_layout()
    fig.savefig("hyperbolic-graphs.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 3 — different ingredients, identical result
# ----------------------------------------------------------------------
def identity_check():
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4))

    # --- circular ---
    ax = axes[0]
    style(ax)
    x = np.linspace(-6.3, 6.3, 800)
    ax.plot(x, np.cos(x), color=PURPLE, lw=2, label=r"$\cos x$")
    ax.plot(x, np.sin(x), color=BLUE, lw=2, label=r"$\sin x$")
    ax.plot(x, np.cos(x) ** 2 + np.sin(x) ** 2, color=AMBER, lw=3.2,
            label=r"$\cos^2 x + \sin^2 x$")
    ax.set_ylim(-2.1, 3.4)
    ax.set_xlim(-6.8, 7.6)
    ax.legend(loc="upper left", frameon=False, labelcolor=AX, fontsize=10.5)
    ax.set_title("bounded waves that repeat forever", color=AX, fontsize=11.5, pad=12)

    # --- hyperbolic ---
    ax = axes[1]
    style(ax)
    x = np.linspace(-2.4, 2.4, 800)
    ax.plot(x, np.cosh(x), color=PURPLE, lw=2, label=r"$\cosh x$")
    ax.plot(x, np.sinh(x), color=BLUE, lw=2, label=r"$\sinh x$")
    ax.plot(x, np.cosh(x) ** 2 - np.sinh(x) ** 2, color=AMBER, lw=3.2,
            label=r"$\cosh^2 x - \sinh^2 x$")
    ax.set_ylim(-6.0, 9.7)
    ax.set_xlim(-2.6, 2.9)
    ax.legend(loc="upper left", frameon=False, labelcolor=AX, fontsize=10.5)
    ax.set_title("unbounded curves that never repeat", color=AX, fontsize=11.5, pad=12)

    for ax in axes:
        ax.annotate("flat at 1", (ax.get_xlim()[1] * 0.62, 1),
                    textcoords="offset points", xytext=(6, 10),
                    color=AMBER, fontsize=11)

    fig.suptitle("Nothing about the ingredients matches. The combination is identical.",
                 color=AX, fontsize=12.5, y=0.03)
    fig.tight_layout(rect=[0, 0.07, 1, 1])
    fig.savefig("hyperbolic-identity-check.svg", transparent=True, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    circle_vs_hyperbola()
    graphs()
    identity_check()
    print("wrote 3 figures")

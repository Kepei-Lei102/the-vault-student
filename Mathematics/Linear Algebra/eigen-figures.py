"""Figures for the Eigenvalues and Eigenvectors card.

Regenerate:  python3 eigen-figures.py
Writes, beside this file:
  eigen-characteristic-collapse.svg — det(A - lambda I) for the rails matrix
      (4 -1; 2 1) plotted against lambda: a parabola crossing zero at 2 and 3.
      The singularity test of Determinants and Inverses run as a *search* —
      each zero is a value of lambda at which A - lambda I collapses, i.e. an
      eigenvalue.
  eigen-rails-stretch.svg — two tall panels. Top: a fan of unit vectors with
      the two rails y = x and y = 2x drawn through the origin. Bottom: every
      vector after multiplication by A — generic vectors have swung off their
      old directions, the two rail vectors are still on their rails, stretched
      by 3 and by 2. The eigen-picture in one before/after.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
    "xtick.color": AX, "ytick.color": AX, "font.size": 13,
    "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault",
})


def save(fig, name):
    fig.savefig(name, transparent=True, bbox_inches="tight",
                metadata={"Date": None})
    plt.close(fig)
    print("wrote", name)


# ----------------------------------------------------------------------
# Figure 1 — the characteristic parabola: det(A - lambda I) = l^2 - 5l + 6
# ----------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.6, 5.2))
lam = np.linspace(-0.3, 5.3, 400)
det = lam**2 - 5*lam + 6

ax.axhline(0, color=AX, lw=1.2)
ax.plot(lam, det, color=BLUE, lw=2.8,
        label=r"$\det(\mathbf{A}-\lambda\mathbf{I}) = \lambda^2-5\lambda+6$")

for root, colr in [(2, GREEN), (3, GREEN)]:
    ax.plot([root], [0], "o", ms=11, color=colr, zorder=5)
    ax.axvline(root, color=AMBER, lw=1.4, ls="--", alpha=0.6)

ax.annotate(r"$\lambda = 2$: $\mathbf{A}-2\mathbf{I}$ collapses" + "\n"
            r"an eigenvalue — rail $y=2x$",
            xy=(2, 0), xytext=(0.05, 2.6), fontsize=13, color=GREEN,
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.4))
ax.annotate(r"$\lambda = 3$: $\mathbf{A}-3\mathbf{I}$ collapses" + "\n"
            r"an eigenvalue — rail $y=x$",
            xy=(3, 0), xytext=(3.35, 3.4), fontsize=13, color=GREEN,
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.4))
ax.annotate("everywhere else:\n" r"$\mathbf{A}-\lambda\mathbf{I}$ invertible,"
            "\nonly $\\mathbf{e}=\\mathbf{0}$ solves",
            xy=(4.6, 4.16), xytext=(3.9, -1.6), fontsize=12, color=AX,
            arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2))

ax.set_xlabel(r"$\lambda$", fontsize=15)
ax.set_ylabel(r"$\det(\mathbf{A}-\lambda\mathbf{I})$", fontsize=14)
ax.set_title(r"The hunt: for which $\lambda$ does $\mathbf{A}-\lambda\mathbf{I}$ collapse?"
             r"   ($\mathbf{A}$ = the rails matrix)",
             fontsize=15, color=AX, pad=12)
ax.set_xlim(-0.3, 5.3)
ax.set_ylim(-2.4, 7)
ax.grid(alpha=0.15, color=AX)
ax.legend(loc="upper center", fontsize=13, frameon=False, labelcolor=AX)
save(fig, "eigen-characteristic-collapse.svg")


# ----------------------------------------------------------------------
# Figure 2 — before/after: the fan of vectors and the two rails
# ----------------------------------------------------------------------
A = np.array([[4, -1], [2, 1]])
angles = np.deg2rad([15, 40, 75, 110, 150, 200, 250, 300, 335])
fan = np.array([[np.cos(t), np.sin(t)] for t in angles])
e1 = np.array([1, 1]) / np.sqrt(2)      # rail y = x,  lambda = 3
e2 = np.array([1, 2]) / np.sqrt(5)      # rail y = 2x, lambda = 2

fig, (top, bot) = plt.subplots(2, 1, figsize=(8.6, 12.6))

for ax_ in (top, bot):
    ax_.set_aspect("equal")
    ax_.axhline(0, color=AX, lw=1.0, alpha=0.6)
    ax_.axvline(0, color=AX, lw=1.0, alpha=0.6)
    ax_.grid(alpha=0.12, color=AX)
    ax_.set_xlim(-4.4, 4.4)
    ax_.set_ylim(-4.4, 4.4)
    t = np.linspace(-4.4, 4.4, 2)
    ax_.plot(t, t, color=AMBER, lw=1.6, ls="--", alpha=0.75)
    ax_.plot(t, 2*t, color=TEAL, lw=1.6, ls="--", alpha=0.75)

top.text(3.6, 3.05, r"rail $y=x$", color=AMBER, fontsize=13)
top.text(1.62, 3.85, r"rail $y=2x$", color=TEAL, fontsize=13)

for v in fan:
    top.annotate("", xy=v, xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=GREY, lw=1.6))
top.annotate("", xy=e1, xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color=AMBER, lw=3.0))
top.annotate("", xy=e2, xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color=TEAL, lw=3.0))
top.text(1.02, 0.55, r"$\mathbf{e}_1$", color=AMBER, fontsize=15)
top.text(0.06, 1.06, r"$\mathbf{e}_2$", color=TEAL, fontsize=15)
top.set_title("Before: a fan of unit vectors — two of them sit on rails",
              fontsize=15, color=AX, pad=10)

for v in fan:
    w = A @ v
    w_draw = w if np.linalg.norm(w) <= 4.2 else w / np.linalg.norm(w) * 4.2
    bot.annotate("", xy=v, xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=GREY, lw=1.0, alpha=0.35))
    bot.annotate("", xy=w_draw, xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=GREY, lw=1.6))
w1 = A @ e1     # 3 e1
w2 = A @ e2     # 2 e2
bot.annotate("", xy=w1, xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color=AMBER, lw=3.0))
bot.annotate("", xy=w2, xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color=TEAL, lw=3.0))
bot.annotate("", xy=e1, xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2, alpha=0.4))
bot.annotate("", xy=e2, xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.2, alpha=0.4))
bot.text(2.30, 1.65, r"$\mathbf{A}\mathbf{e}_1 = 3\,\mathbf{e}_1$",
         color=AMBER, fontsize=15)
bot.text(-0.05, 2.42, r"$\mathbf{A}\mathbf{e}_2 = 2\,\mathbf{e}_2$",
         color=TEAL, fontsize=15, ha="right")
bot.set_title("After multiplying by A: generic vectors swing off their lines —\n"
              "the rail vectors stay on their rails, stretched by 3 and by 2",
              fontsize=15, color=AX, pad=10)

fig.tight_layout(h_pad=2.4)
save(fig, "eigen-rails-stretch.svg")

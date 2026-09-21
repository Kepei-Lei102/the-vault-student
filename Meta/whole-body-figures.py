"""Figure for [[Learning with the Whole Body]].

Regenerate:  python3 whole-body-figures.py
  whole-body-climber-moments.svg   a 60 kg climber on a vertical wall, hips out against hips in: moments about the feet
                                   give the horizontal pull the hands must supply, F = W d / h
Vault palette: all text #888, transparent background.
"""
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AX, BLUE, PURPLE, GREEN, RED, AMBER = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"
plt.rcParams.update({"text.color": AX, "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})
M, G, H = 60.0, 9.8, 1.4          # mass, g, height of the hands above the feet


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def arrow(ax, p, q, col, lw=2.4):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, mutation_scale=16))


def panel(ax, d, title):
    W = M * G; F = W * d / H
    ax.set_xlim(-0.35, 1.5); ax.set_ylim(-0.45, 2.05); ax.set_aspect("equal"); ax.axis("off")
    ax.fill_betweenx([-0.2, 1.9], -0.3, 0, color=AX, alpha=0.18); ax.plot([0, 0], [-0.2, 1.9], color=AX, lw=2)
    feet, hands, com = (0.0, 0.0), (0.0, H), (d, 0.78)
    head = (d * 0.75 + 0.03, 1.27)
    ax.plot([feet[0], com[0]], [feet[1], com[1]], color=BLUE, lw=5, solid_capstyle="round")          # legs
    ax.plot([com[0], head[0]], [com[1], head[1] - 0.1], color=BLUE, lw=5, solid_capstyle="round")    # trunk
    ax.plot([head[0], hands[0]], [head[1] - 0.12, hands[1]], color=BLUE, lw=4, solid_capstyle="round")  # arms
    ax.add_patch(plt.Circle(head, 0.1, fc="none", ec=BLUE, lw=3))
    ax.plot(*com, "o", color=AMBER, ms=11, zorder=5)
    arrow(ax, com, (com[0], com[1] - 0.55), RED); ax.text(com[0] + 0.06, com[1] - 0.5, f"weight {W:.0f} N", va="center", fontsize=12)
    arrow(ax, (0.62, H), (0.04, H), GREEN); ax.text(0.66, H, f"pull at the hands\n{F:.0f} N", va="center", fontsize=12)
    ax.plot(0, 0, "s", color=PURPLE, ms=9, zorder=6); ax.text(d + 0.08, -0.06, "pivot: the feet", fontsize=11.5, va="center")
    ax.annotate("", xy=(d, -0.3), xytext=(0, -0.3), arrowprops=dict(arrowstyle="|-|,widthA=0.35,widthB=0.35", color=AMBER, lw=2))
    ax.plot([d, d], [-0.34, com[1] - 0.6], color=AMBER, lw=1, ls=":")
    ax.text(d / 2, -0.41, f"d = {d:.2f} m", ha="center", va="center", fontsize=12)
    ax.annotate("", xy=(1.22, H), xytext=(1.22, 0), arrowprops=dict(arrowstyle="<->", color=AX, lw=1.2))
    ax.text(1.26, H / 2, f"h = {H} m", va="center", fontsize=12)
    ax.text(0.55, 1.95, title, ha="center", fontsize=13.5)


def fig_climber():
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.6))
    panel(axes[0], 0.40, "hips out from the wall"); panel(axes[1], 0.15, "hips turned in to the wall")
    fig.text(0.5, 0.02, "moments about the feet:  pull × h = weight × d,  and so  pull = weight × d / h", ha="center", fontsize=13)
    save(fig, "whole-body-climber-moments.svg")


if __name__ == "__main__":
    fig_climber()

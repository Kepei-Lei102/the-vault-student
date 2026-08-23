"""Figure for the De Moivre at Work card.

Regenerate:  python3 demoivre-figures.py
Writes, beside this file:
  cis-phasor-chain.svg — Engine A drawn: the terms of sum e^{ir·theta} laid
      head-to-tail as unit phasors, each one step-angle theta further round.
      Top: theta = 25 deg, n = 8 — the chain arcs and the resultant chord is
      the sum, magnitude sin(n theta/2)/sin(theta/2). Bottom: step angle set
      to exactly 2*pi/n — the chain closes into a regular polygon, resultant
      zero: the roots of unity summing to zero, drawn.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AX = "#888888"
BLUE = "#2563eb"
GREEN = "#059669"
RED = "#dc2626"
AMBER = "#f59e0b"
GREY = "#9ca3af"

plt.rcParams.update({
    "text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX,
    "xtick.color": AX, "ytick.color": AX, "font.size": 13,
    "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault",
})

fig, (top, bot) = plt.subplots(2, 1, figsize=(8.6, 13.2))


def chain(ax_, theta, n, title, note, show_resultant=True):
    pts = [np.array([0.0, 0.0])]
    for r in range(1, n + 1):
        pts.append(pts[-1] + np.array([np.cos(r * theta), np.sin(r * theta)]))
    pts = np.array(pts)

    for r in range(n):
        p, q = pts[r], pts[r + 1]
        ax_.annotate("", xy=q, xytext=p,
                     arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.2))
    if show_resultant:
        ax_.annotate("", xy=pts[-1], xytext=pts[0],
                     arrowprops=dict(arrowstyle="->", color=GREEN, lw=3.2))

    # circumcircle through chain vertices (computed, not guessed)
    R = 1.0 / (2.0 * np.sin(theta / 2.0))
    centre = pts[0] + R * np.array([np.cos(theta / 2 + np.pi / 2),
                                    np.sin(theta / 2 + np.pi / 2)])
    tt = np.linspace(0, 2 * np.pi, 200)
    ax_.plot(centre[0] + R * np.cos(tt), centre[1] + R * np.sin(tt),
             color=GREY, lw=1.0, ls=":", alpha=0.7)

    ax_.set_aspect("equal")
    ax_.set_axis_off()
    ax_.set_title(title, fontsize=15, color=AX, pad=8)
    ax_.text(0.5, -0.06, note, transform=ax_.transAxes, fontsize=13,
             color=AX, ha="center")
    return pts


# Top: theta = 25 deg, n = 8 — open arc, healthy resultant
th, n = np.deg2rad(25), 8
pts = chain(top, th, n,
            "Engine A as a picture: eight unit phasors, each one step of θ further round",
            r"head-to-tail, the terms of  $\sum e^{ir\theta}$  ($\theta = 25°$)")
top.annotate(r"term 1: $e^{i\theta}$", xy=(pts[0] + pts[1]) / 2 + np.array([0.05, -0.28]),
             fontsize=13, color=BLUE)
mid = pts[len(pts) // 2] + np.array([0.15, 0.3])
top.text(mid[0]+0.9, mid[1]+0.35, "each arrow turns\nby θ from the last", fontsize=13, color=BLUE)
res_mid = pts[-1] * 0.45
top.text(res_mid[0] - 0.35, res_mid[1] + 1.25,
         "the sum: one chord,\n" + r"$|C+iS| = \sin(n\theta/2)\,/\,\sin(\theta/2)$",
         fontsize=13.5, color=GREEN)

# Bottom: theta = 2*pi/8 — the chain closes: roots of unity sum to zero
th2, n2 = 2 * np.pi / 8, 8
pts2 = chain(bot, th2, n2,
             "Set the step to exactly 2π/n and the chain closes on itself",
             "the eighth roots of unity, head-to-tail: they sum to zero",
             show_resultant=False)
bot.plot([0], [0], "o", ms=10, color=RED, zorder=5)
bot.text(0.45, -0.3, "start = finish:\nresultant 0", fontsize=13.5, color=RED)

fig.tight_layout(h_pad=2.0)
fig.savefig("cis-phasor-chain.svg", transparent=True, bbox_inches="tight",
            metadata={"Date": None})
print("wrote cis-phasor-chain.svg")

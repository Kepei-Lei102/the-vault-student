"""
SHM phase relationships — x(t), v(t), a(t) across one period.
Generates shm-phase-relationships.svg in the same directory.

Run from anywhere:
    python "Physics/Mechanics/shm-phase-relationships.py"
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Vault color scheme
TEXT = "#888888"
AXIS = "#888888"
GRID = "#888888"
BLUE = "#2563eb"   # x — position
GREEN = "#059669"  # v — velocity
AMBER = "#f59e0b"  # a — acceleration

# One full period, well sampled
omega = 2 * np.pi          # T = 1 (units are arbitrary; we label fractions of T)
A = 1.0
t = np.linspace(0, 1.0, 1000)

x = A * np.cos(omega * t)
v = -A * omega * np.sin(omega * t)
a = -A * omega**2 * np.cos(omega * t)

fig, axes = plt.subplots(3, 1, figsize=(9, 7), sharex=True)
fig.patch.set_alpha(0)

# Title centred at the top of the figure
fig.suptitle(
    "SHM Phase Relationships — x, v, a across one period",
    color=TEXT, fontsize=14, fontweight="bold", y=0.97,
)
fig.text(
    0.5, 0.925,
    r"$v$ leads $x$ by $90°$ ($\pi/2$).  $a$ is $180°$ out of phase with $x$.",
    color=TEXT, fontsize=10.5, ha="center", style="italic", alpha=0.85,
)

panels = [
    (axes[0], x,  BLUE,  r"$x(t) = A\cos(\omega t)$",          [(-A, "$-A$"), (0, "0"), (A, "$+A$")]),
    (axes[1], v,  GREEN, r"$v(t) = -A\omega\sin(\omega t)$",   [(-A*omega, r"$-A\omega$"), (0, "0"), (A*omega, r"$+A\omega$")]),
    (axes[2], a,  AMBER, r"$a(t) = -A\omega^2\cos(\omega t)$", [(-A*omega**2, r"$-A\omega^2$"), (0, "0"), (A*omega**2, r"$+A\omega^2$")]),
]

# Vertical reference line at t = T/4 across all three subplots
ref_t = 0.25

for ax, y, color, label, yticks in panels:
    ax.plot(t, y, color=color, linewidth=2.2)
    ax.axhline(0, color=AXIS, linewidth=0.9, alpha=0.55)
    ax.axvline(ref_t, color=AXIS, linewidth=0.9, linestyle=(0, (3, 4)), alpha=0.45)

    # y-tick locations and labels
    ax.set_yticks([v for v, _ in yticks])
    ax.set_yticklabels([lbl for _, lbl in yticks])

    # Style: minimal spines, vault grey
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
        ax.spines[side].set_linewidth(1.0)
    ax.tick_params(colors=TEXT, length=4, width=0.8)
    ax.set_facecolor("none")

    # Curve label — placed in the upper-right area of each subplot, in the curve's color
    ax.text(
        0.99, 0.93, label,
        transform=ax.transAxes, ha="right", va="top",
        color=color, fontsize=11.5,
    )

    # Y limits with slight padding so labels don't crowd the axes
    ymax = max(abs(min(y)), abs(max(y))) * 1.25
    ax.set_ylim(-ymax, ymax)

# Configure shared x-axis: tick at quarter-period multiples
axes[-1].set_xticks([0, 0.25, 0.5, 0.75, 1.0])
axes[-1].set_xticklabels(["$0$", "$T/4$", "$T/2$", "$3T/4$", "$T$"])
axes[-1].set_xlabel("$t$", color=TEXT, fontsize=12, style="italic")
axes[-1].set_xlim(0, 1.0)

# Bottom caption box (outside the plot area)
fig.text(
    0.5, 0.02,
    r"At $t = T/4$:  $x = 0$ (equilibrium),  $v = -A\omega$ (max speed, moving $-$),  $a = 0$." "\n"
    r"At $t = T/2$:  $x = -A$ (turning point),  $v = 0$,  $a = +A\omega^2$ (max restoring).",
    color=TEXT, fontsize=10, ha="center", alpha=0.85,
)

# Tight layout but leave space for suptitle + bottom caption
plt.subplots_adjust(top=0.89, bottom=0.13, hspace=0.32, left=0.13, right=0.97)

# Output paths
script_dir = Path(__file__).resolve().parent
svg_path = script_dir / "shm-phase-relationships.svg"
png_path = Path("/tmp") / "shm-phase-relationships-verify.png"

plt.savefig(svg_path, format="svg", transparent=True, bbox_inches="tight")
plt.savefig(png_path, format="png", transparent=True, bbox_inches="tight", dpi=150)
plt.close()

print(f"Wrote SVG -> {svg_path}")
print(f"Wrote verification PNG -> {png_path}")

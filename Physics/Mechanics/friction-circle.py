"""
Friction circle (traction circle) — the central diagram of vehicle dynamics.

Plots a circle of radius μ·N showing the magnitude bound on combined
longitudinal + lateral friction. Several driver-strategy vectors drawn inside
showing different combined-grip allocations: pure braking, pure cornering,
trail-braking, apex, corner exit.

Output: friction-circle.svg in the same directory.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

TEXT = "#888888"
AXIS = "#888888"
BLUE = "#2563eb"     # lateral / cornering
GREEN = "#059669"    # longitudinal / braking
AMBER = "#f59e0b"    # trail-braking + combined
RED = "#dc2626"      # over-the-limit
PURPLE = "#7c3aed"   # apex
GREY = "#bbbbbb"

# Friction circle radius (in g units; μ_s = 1.5 for sticky race tires)
mu = 1.5

fig, ax = plt.subplots(figsize=(8.0, 7.5))
fig.patch.set_alpha(0)
ax.set_facecolor("none")
ax.set_aspect("equal")

# === Friction circle (the boundary) ===
circle = patches.Circle((0, 0), mu, facecolor=BLUE, alpha=0.07,
                         edgecolor=BLUE, linewidth=2.4)
ax.add_patch(circle)

# Dashed inner reference: 80% of limit (the "safe" zone for a road car)
inner = patches.Circle((0, 0), mu * 0.8, facecolor="none",
                        edgecolor=GREY, linewidth=0.9, linestyle=(0, (4, 5)))
ax.add_patch(inner)

# === Axes ===
ax_lim = mu * 1.55
ax.set_xlim(-ax_lim, ax_lim)
ax.set_ylim(-ax_lim, ax_lim)

# Horizontal axis (lateral) and vertical axis (longitudinal)
ax.axhline(0, color=AXIS, linewidth=1.0, alpha=0.7)
ax.axvline(0, color=AXIS, linewidth=1.0, alpha=0.7)

# Axis labels — moved well clear of the friction-limit annotation
ax.text(ax_lim - 0.1, -0.30, r"$F_{\rm lat}$  (cornering)",
        color=TEXT, fontsize=11, ha="right", va="top", style="italic")
ax.text(-ax_lim * 0.95, ax_lim - 0.1, r"$F_{\rm long}$  (braking $\uparrow$  /  accelerating $\downarrow$)",
        color=TEXT, fontsize=11, ha="left", va="top", rotation=90, style="italic")

# === Strategy vectors ===
# All vectors emanate from origin. Magnitude scaled to be just inside the circle (95% of μ)
strategies = [
    # (label, lat, long, color, x_offset, y_offset)
    ("pure braking",        0.0,   mu * 0.95,  GREEN,  0.15,  0.10),
    ("threshold braking\n+ slight turn-in", 0.45, mu * 0.85,  AMBER, 0.10, 0.05),
    ("trail-braking",       mu * 0.72,  mu * 0.55, AMBER, 0.10, 0.05),
    ("apex (pure cornering)", mu * 0.95, 0.0,   PURPLE,  0.10, 0.15),
    ("corner exit\n(traction + slight throttle)", mu * 0.78, -mu * 0.50, BLUE, 0.10, -0.10),
    ("pure acceleration",   0.0,  -mu * 0.85, GREEN,  0.15, -0.10),
]

for label, lat, lng, color, lx, ly in strategies:
    ax.annotate("", xy=(lat, lng), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2.0,
                                 mutation_scale=14, alpha=0.85))
    ax.text(lat + lx, lng + ly, label, color=color, fontsize=9.5,
            ha="left" if lat >= 0 else "right", va="center", style="italic")

# === Over-the-limit example (the slip vector) ===
ax.annotate("", xy=(mu * 1.2, mu * 0.5), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2,
                             mutation_scale=14, linestyle="-"))
ax.text(mu * 1.22, mu * 0.55, "request exceeds limit\n→ tire breaks loose,\nfriction drops to $\\mu_k N$",
        color=RED, fontsize=9.5, ha="left", va="center", style="italic")

# Mark where the over-the-limit vector crosses the circle
cross_angle = np.arctan2(mu * 0.5, mu * 1.2)
ax.plot([mu * np.cos(cross_angle)], [mu * np.sin(cross_angle)], "x",
         color=RED, markersize=12, markeredgewidth=2.5)

# === Circle labels ===
ax.text(0, mu + 0.18, r"$|\vec F| = \mu_s N$  (friction limit)",
        color=BLUE, fontsize=11, ha="center", va="bottom",
        style="italic", fontweight="bold")
ax.text(0, mu * 0.8 + 0.08, "80% safe-driving margin",
        color=GREY, fontsize=8.5, ha="center", va="bottom", style="italic", alpha=0.85)

# Title
ax.set_title("The Friction Circle — Combined Lateral + Longitudinal Grip Budget",
             color=TEXT, fontsize=13, fontweight="bold", pad=18)

# Axis ticks
ax.set_xticks([])
ax.set_yticks([])
for side in ("top", "right", "bottom", "left"):
    ax.spines[side].set_visible(False)

# Bottom caption (outside plot)
fig.text(0.5, 0.02,
         r"Any combination of braking and cornering must stay INSIDE the circle.  "
         r"Pros operate at the edge.  Crossing it = the tire slips.",
         color=TEXT, fontsize=10, ha="center", style="italic", alpha=0.85)

plt.tight_layout()
plt.subplots_adjust(bottom=0.08)

script_dir = Path(__file__).resolve().parent
svg_path = script_dir / "friction-circle.svg"
png_path = Path("/tmp") / "friction-circle-verify.png"
plt.savefig(svg_path, format="svg", transparent=True, bbox_inches="tight")
plt.savefig(png_path, format="png", transparent=True, bbox_inches="tight", dpi=150)
plt.close()

print(f"Wrote SVG -> {svg_path}")
print(f"Wrote verification PNG -> {png_path}")

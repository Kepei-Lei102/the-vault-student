"""
Stribeck curve — friction coefficient vs Hersey number (the dimensionless
combination ηv/N of viscosity × velocity / normal load).

Three regimes visible:
  1. Boundary lubrication (low Hersey): solid-on-solid contact, μ is high
  2. Mixed lubrication (intermediate): partial film forms, μ has its minimum
  3. Hydrodynamic lubrication (high Hersey): full film separates surfaces,
     μ rises again with viscous drag

Output: stribeck-curve.svg in the same directory.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

TEXT = "#888888"
AXIS = "#888888"
BLUE = "#2563eb"     # primary curve
AMBER = "#f59e0b"    # mixed-regime highlight (ABS sweet spot)
GREEN = "#059669"    # hydrodynamic
RED = "#dc2626"      # boundary (high friction, high wear)
GREY = "#bbbbbb"

# === Build a synthetic Stribeck curve on log Hersey axis ===
# x in log10 units of Hersey number; we just want a curve with the right shape
log_h = np.linspace(-3, 2, 500)

# Shape: high at low H (boundary), drops to minimum at log_h ≈ -0.5, rises again
# Use a combination: tanh decline + linear rise after the minimum
mu_boundary = 0.10
mu_min = 0.025
mu_high = 0.10
log_h_min = -0.5

decline = (mu_boundary - mu_min) * 0.5 * (1 - np.tanh((log_h - log_h_min - 0.3) * 2.5))
rise = np.where(log_h > log_h_min, 0.04 * (log_h - log_h_min) ** 1.2, 0)
mu = mu_min + decline + rise

# === Figure ===
fig, ax = plt.subplots(figsize=(9.5, 5.5))
fig.patch.set_alpha(0)
ax.set_facecolor("none")

# Background shading for the three regimes
# Boundary: log_h < -1.2
# Mixed:    -1.2 < log_h < 0.0
# Hydrodynamic: log_h > 0.0
y_top = 0.13

# Add subtle bands behind the curve
ax.axvspan(-3, -1.2, color=RED, alpha=0.06)
ax.axvspan(-1.2, 0.0, color=AMBER, alpha=0.08)
ax.axvspan(0.0, 2.0, color=GREEN, alpha=0.06)

# Plot the curve
ax.plot(log_h, mu, color=BLUE, linewidth=2.8)

# Mark the minimum (ABS sweet spot)
min_idx = np.argmin(mu)
min_log_h, min_mu = log_h[min_idx], mu[min_idx]
ax.plot([min_log_h], [min_mu], "o", color=AMBER, markersize=9,
         markeredgecolor=AMBER, markeredgewidth=2, zorder=5)
ax.annotate(
    "minimum friction\n(ABS / traction-control\noperating point)",
    xy=(min_log_h, min_mu),
    xytext=(min_log_h + 0.5, min_mu - 0.018),
    color=AMBER, fontsize=10, ha="left", va="center", style="italic",
    arrowprops=dict(arrowstyle="-", color=AMBER, alpha=0.65, lw=0.9)
)

# Region labels at the top
ax.text(-2.1, y_top - 0.01, "Boundary\nlubrication",
         color=RED, fontsize=11, ha="center", va="top",
         fontweight="bold")
ax.text(-2.1, y_top - 0.025, "solid-on-solid contact\nhigh friction, high wear",
         color=RED, fontsize=9, ha="center", va="top", style="italic", alpha=0.85)

ax.text(-0.55, y_top - 0.01, "Mixed\nlubrication",
         color=AMBER, fontsize=11, ha="center", va="top",
         fontweight="bold")
ax.text(-0.55, y_top - 0.025, "partial film forms\nfriction at its minimum",
         color=AMBER, fontsize=9, ha="center", va="top", style="italic", alpha=0.85)

ax.text(1.2, y_top - 0.01, "Hydrodynamic\nlubrication",
         color=GREEN, fontsize=11, ha="center", va="top",
         fontweight="bold")
ax.text(1.2, y_top - 0.025, "full film separates surfaces\nμ rises with viscous drag",
         color=GREEN, fontsize=9, ha="center", va="top", style="italic", alpha=0.85)

# Axes
ax.set_xlim(-3, 2)
ax.set_ylim(0, y_top)
ax.set_xlabel(r"Hersey number $\eta v / N$  (log scale)  →  faster speed, more lubricant, less load",
               color=TEXT, fontsize=11)
ax.set_ylabel(r"Friction coefficient  $\mu$",
               color=TEXT, fontsize=11)

# Style
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(AXIS)
    ax.spines[side].set_linewidth(1.0)
ax.tick_params(colors=TEXT, length=4, width=0.8)
ax.xaxis.label.set_color(TEXT)
ax.yaxis.label.set_color(TEXT)

# Custom x-tick labels showing log values
ax.set_xticks([-3, -2, -1, 0, 1, 2])
ax.set_xticklabels(["$10^{-3}$", "$10^{-2}$", "$10^{-1}$", "$10^{0}$", "$10^{1}$", "$10^{2}$"])
ax.set_yticks([0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12])

# Title
ax.set_title("The Stribeck Curve — Why Friction is Not a Single Number",
              color=TEXT, fontsize=13, fontweight="bold", pad=14)

# Bottom annotation: where common scenarios sit on the curve
fig.text(
    0.5, 0.005,
    r"Static / locked-up wheel sits in the boundary regime (high friction, lots of wear).  "
    r"ABS modulates around the mixed-lubrication minimum.  Hydroplaning is the hydrodynamic regime taken to extreme.",
    color=TEXT, fontsize=9.5, ha="center", style="italic", alpha=0.85
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.16)

script_dir = Path(__file__).resolve().parent
svg_path = script_dir / "stribeck-curve.svg"
png_path = Path("/tmp") / "stribeck-curve-verify.png"
plt.savefig(svg_path, format="svg", transparent=True, bbox_inches="tight")
plt.savefig(png_path, format="png", transparent=True, bbox_inches="tight", dpi=150)
plt.close()

print(f"Wrote SVG -> {svg_path}")
print(f"Wrote verification PNG -> {png_path}")
print(f"Minimum at log H = {min_log_h:.2f}, μ_min = {min_mu:.4f}")

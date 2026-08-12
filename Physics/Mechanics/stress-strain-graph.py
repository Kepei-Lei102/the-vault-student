"""
Stress-strain graph for a typical ductile metal (mild steel flavour).

Shows the four canonical regions:
  1. Linear elastic     — slope = E
  2. Yielding + plastic — near-constant stress at yield
  3. Strain hardening   — stress rises again until UTS
  4. Necking + fracture — stress falls off (engineering stress-strain)

Output: stress-strain-graph.svg in the same directory.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Vault color scheme
TEXT = "#888888"
AXIS = "#888888"
BLUE = "#2563eb"    # elastic
AMBER = "#f59e0b"   # plastic / yield
GREEN = "#059669"   # strain hardening to UTS
RED = "#dc2626"     # fracture
GREY = "#888888"

# --- Build the synthetic stress-strain curve ---
# Strain axis (dimensionless). Beyond ~0.25 strain on mild steel is fracture territory.
# Region break points (in strain):
eps_elastic_end = 0.0015   # elastic limit ~ 0.15% strain
eps_yield_end   = 0.018    # plastic flow at near-constant stress until ~1.8%
eps_uts         = 0.18     # strain hardening peaks at ~18%
eps_fracture    = 0.26     # fracture around 26%

# Stress values (in MPa, displayed; we'll use MPa as the y-axis unit)
sigma_yield = 250          # yield stress for mild steel
sigma_uts   = 450          # ultimate tensile strength
sigma_fract = 380          # engineering stress at fracture (necking pulls it down)

# Region 1: linear elastic, gradient E
# E_steel = 200 GPa = 200_000 MPa
# at eps=0.0015, sigma = 200_000 * 0.0015 = 300 MPa
# We want sigma_yield_start = 250 MPa, so adjust elastic to end at (eps=0.00125, sigma=250)
# Use eps_elastic_end = 0.00125 instead — recompute
eps_elastic_end = sigma_yield / 200000  # = 0.00125

eps1 = np.linspace(0, eps_elastic_end, 50)
sig1 = 200000 * eps1   # MPa

# Region 2: yielding plateau (slight serration ignored for clarity)
eps2 = np.linspace(eps_elastic_end, eps_yield_end, 80)
sig2 = sigma_yield + (np.random.RandomState(7).normal(0, 1.5, eps2.size).cumsum() * 0)  # flat
# slight rise to make the transition visible
sig2 = sigma_yield + 4 * np.sin(np.linspace(0, np.pi, eps2.size))

# Region 3: strain hardening — concave rise to UTS
eps3 = np.linspace(eps_yield_end, eps_uts, 200)
# smooth parabolic-like rise
t = (eps3 - eps_yield_end) / (eps_uts - eps_yield_end)
sig3 = sigma_yield + (sigma_uts - sigma_yield) * (1 - (1 - t) ** 2)

# Region 4: necking — gentle decline to fracture
eps4 = np.linspace(eps_uts, eps_fracture, 80)
t4 = (eps4 - eps_uts) / (eps_fracture - eps_uts)
sig4 = sigma_uts - (sigma_uts - sigma_fract) * t4

# --- Build the figure ---
fig, ax = plt.subplots(figsize=(8.8, 5.6))
fig.patch.set_alpha(0)
ax.set_facecolor("none")

# Draw the four regions in their semantic colours
ax.plot(eps1 * 100, sig1, color=BLUE,  linewidth=2.6, zorder=4)
ax.plot(eps2 * 100, sig2, color=AMBER, linewidth=2.6, zorder=4)
ax.plot(eps3 * 100, sig3, color=GREEN, linewidth=2.6, zorder=4)
ax.plot(eps4 * 100, sig4, color=RED,   linewidth=2.6, zorder=4)

# Fracture marker at the end
ax.plot([eps_fracture * 100], [sigma_fract], "x", color=RED, markersize=12, markeredgewidth=2.6, zorder=5)

# Shaded region under elastic curve (the recoverable elastic-PE triangle)
ax.fill_between(eps1 * 100, 0, sig1, color=BLUE, alpha=0.12, zorder=2)

# --- Axes styling ---
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(AXIS)
    ax.spines[side].set_linewidth(1.0)
ax.tick_params(colors=TEXT, length=4, width=0.8)
ax.xaxis.label.set_color(TEXT)
ax.yaxis.label.set_color(TEXT)

ax.set_xlabel(r"Strain $\varepsilon$  (%)", fontsize=12)
ax.set_ylabel(r"Stress $\sigma$  (MPa)", fontsize=12)

ax.set_xlim(-0.5, 30)
ax.set_ylim(0, 550)
ax.set_xticks([0, 5, 10, 15, 20, 25])
ax.set_yticks([0, 100, 200, 300, 400, 500])

# Title
ax.set_title("Stress–Strain Curve of a Typical Ductile Metal",
             color=TEXT, fontsize=13.5, fontweight="bold", pad=14)

# --- Annotations ---
# Yield stress horizontal guide
ax.axhline(sigma_yield, color=AMBER, linewidth=0.7, linestyle=(0, (3, 4)), alpha=0.55, zorder=1)
ax.text(0.5, sigma_yield + 10, r"$\sigma_Y$  (yield stress)",
        color=AMBER, fontsize=10, ha="left", va="bottom")

# UTS horizontal guide
ax.axhline(sigma_uts, color=GREEN, linewidth=0.7, linestyle=(0, (3, 4)), alpha=0.55, zorder=1)
ax.text(0.5, sigma_uts + 10, r"$\sigma_{\mathrm{UTS}}$  (ultimate tensile strength)",
        color=GREEN, fontsize=10, ha="left", va="bottom")

# Region labels — placed in clear zones, leaders don't cross other curves
# 1. Elastic — narrow vertical column at the left, label well above the curve top
ax.annotate("1. Elastic\n(slope = $E$)", xy=(0.6, 130), xytext=(4.5, 80),
            color=BLUE, fontsize=10.5, ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color=BLUE, alpha=0.55, lw=0.8))

# 2. Yielding — label sits below the plateau, leader points up to it
ax.annotate("2. Yielding\n(plastic flow)", xy=(1.2, 252), xytext=(4.2, 170),
            color=AMBER, fontsize=10.5, ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color=AMBER, alpha=0.55, lw=0.8))

# 3. Strain hardening — label below the green curve
ax.annotate("3. Strain hardening", xy=(10, 380), xytext=(11.5, 315),
            color=GREEN, fontsize=10.5, ha="center",
            arrowprops=dict(arrowstyle="-", color=GREEN, alpha=0.55, lw=0.8))

# 4. Necking — label above the red curve, away from sigma_Y guide
ax.annotate("4. Necking →\nfracture", xy=(eps_fracture * 100, sigma_fract), xytext=(22, 480),
            color=RED, fontsize=10.5, ha="center",
            arrowprops=dict(arrowstyle="-", color=RED, alpha=0.55, lw=0.8))

# Elastic limit point marker — label moved well clear of axis ticks
ax.plot([eps_elastic_end * 100], [sigma_yield], "o", color=BLUE, markersize=6,
        markerfacecolor="white", markeredgewidth=2, zorder=5)
ax.annotate("elastic limit",
            xy=(eps_elastic_end * 100, sigma_yield),
            xytext=(2.8, 300),
            color=BLUE, fontsize=9.5, ha="left", style="italic",
            arrowprops=dict(arrowstyle="-", color=BLUE, alpha=0.45, lw=0.6))

# Caption goes outside the plot area entirely, below the x-axis label
fig.text(0.5, -0.04,
         r"Gradient of the linear region = $E$ (Young modulus).  "
         r"Area under the curve in the elastic region = recoverable strain energy density $u = \frac{1}{2}\sigma\varepsilon$.",
         color=TEXT, fontsize=9.5, ha="center", alpha=0.8)

plt.tight_layout()

# Output
script_dir = Path(__file__).resolve().parent
svg_path = script_dir / "stress-strain-graph.svg"
png_path = Path("/tmp") / "stress-strain-verify.png"
plt.savefig(svg_path, format="svg", transparent=True, bbox_inches="tight")
plt.savefig(png_path, format="png", transparent=True, bbox_inches="tight", dpi=150)
plt.close()

print(f"Wrote SVG -> {svg_path}")
print(f"Wrote verification PNG -> {png_path}")

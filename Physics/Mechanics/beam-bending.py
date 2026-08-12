"""
Beam bending visual — two panels for the Stress/Strain card.

Left panel  — a cantilever beam under a tip load. Deflection visible. A
              cross-section cut at mid-span shows the stress profile:
              compression top, tension bottom, neutral axis in the middle.
Right panel — three rectangular cross-sections, same area (2.5 unit^2),
              showing how I = b*h^3/12 scales with depth. Aspect ratio 10:1
              gives a clean 100x stiffness factor between wide-flat and
              tall-narrow.

Output: beam-bending.svg in the same directory.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

# Vault color scheme
TEXT = "#888888"
AXIS = "#888888"
BLUE = "#2563eb"     # tension (lower fibres) + cross-section B
RED = "#dc2626"      # compression (upper fibres) + load arrow
GREEN = "#059669"    # neutral axis + cross-section C
AMBER = "#f59e0b"    # cross-section A + deflection arrow
GREY = "#bbbbbb"

# ===================================================================
# Figure setup — two panels side by side
# ===================================================================
fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.5, 5.8),
                                gridspec_kw={"width_ratios": [1.25, 1]})
fig.patch.set_alpha(0)
for ax in (axL, axR):
    ax.set_facecolor("none")
    ax.set_aspect("equal")
    for side in ("top", "right", "bottom", "left"):
        ax.spines[side].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

fig.suptitle("Beam Bending — Why a Tall Beam is Stiffer Than a Wide One",
             color=TEXT, fontsize=14, fontweight="bold", y=0.99)

# ===================================================================
# LEFT PANEL — Cantilever beam under tip load + stress profile inset
# ===================================================================
axL.set_xlim(-1.5, 13)
axL.set_ylim(-4.5, 5)
axL.set_title("Cantilever beam under a tip load — the bent shape",
              color=TEXT, fontsize=11.5, pad=8)

# Wall on the left — hatched vertical band
wall = patches.Rectangle((-0.9, -3), 0.7, 6.5,
                          facecolor="none", hatch="///",
                          edgecolor=GREY, linewidth=1.0)
axL.add_patch(wall)
axL.plot([-0.2, -0.2], [-3, 3.5], color=TEXT, linewidth=1.5)

# Undeflected beam (faint dashed reference along the centreline)
axL.plot([-0.2, 9.8], [0, 0], color=GREY, linewidth=1.0, linestyle=(0, (4, 4)),
         alpha=0.6, zorder=2)

# Deflected beam — Euler-Bernoulli analytic deflection for cantilever
# with tip load: y(x) = -F x^2 (3L - x) / (6EI), scaled
L_beam = 10
x = np.linspace(0, L_beam, 100)
deflection_scale = 2.4 / (L_beam ** 3 / 3)
y = -deflection_scale * x ** 2 * (3 * L_beam - x) / 6

# Draw the beam as a thick filled curve (top edge slightly above, bottom edge below)
thickness = 0.4
beam_x = np.concatenate([x, x[::-1]])
beam_y = np.concatenate([y + thickness, (y[::-1] - thickness)])
beam_patch = patches.Polygon(list(zip(beam_x - 0.2, beam_y)),
                              facecolor=BLUE, alpha=0.18,
                              edgecolor=BLUE, linewidth=1.6)
axL.add_patch(beam_patch)

# Centreline of the deflected beam (the neutral-axis curve)
axL.plot(x - 0.2, y, color=GREEN, linewidth=0.9, linestyle=(0, (2, 3)), alpha=0.75)

# Load arrow at the tip — placed clearly to the side
tip_x, tip_y = x[-1] - 0.2, y[-1]
axL.annotate("", xy=(tip_x, tip_y - 0.55), xytext=(tip_x, tip_y + 1.5),
             arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5,
                              mutation_scale=18))
axL.text(tip_x + 0.45, tip_y + 0.6, r"$F$", color=RED,
         fontsize=15, ha="left", va="center", style="italic", fontweight="bold")

# Length annotation L — well below the beam
axL.annotate("", xy=(-0.2, -3.8), xytext=(tip_x, -3.8),
             arrowprops=dict(arrowstyle="<->", color=TEXT, lw=1.0, alpha=0.8))
axL.text((tip_x - 0.2) / 2, -4.15, r"$L$", color=TEXT, fontsize=13, ha="center",
         va="top", style="italic")

# Deflection annotation δ — moved clear of F
axL.annotate("", xy=(tip_x + 0.7, 0), xytext=(tip_x + 0.7, tip_y),
             arrowprops=dict(arrowstyle="<->", color=AMBER, lw=1.2))
axL.text(tip_x + 1.0, tip_y / 2, r"$\delta$", color=AMBER, fontsize=15,
         ha="left", va="center", style="italic", fontweight="bold")

# Cross-section cut indicator at mid-span (x = 4)
cut_x = 4.0
cut_y_center = y[40]  # the beam centreline at x=4
# Vertical dashed line marking the cut
axL.plot([cut_x - 0.2, cut_x - 0.2],
          [cut_y_center - thickness - 0.1, cut_y_center + thickness + 0.1],
          color=TEXT, linewidth=1.0, alpha=0.7)
# Small markers at top and bottom of the cut
axL.plot([cut_x - 0.2], [cut_y_center + thickness], "o", color=TEXT,
          markersize=3.5, alpha=0.7)
axL.plot([cut_x - 0.2], [cut_y_center - thickness], "o", color=TEXT,
          markersize=3.5, alpha=0.7)

# Stress profile inset — to the upper-right of the cut
profile_x_base = 7.5
profile_y_top = 3.7
profile_y_bot = 1.0
profile_h = profile_y_top - profile_y_bot
profile_y_mid = (profile_y_top + profile_y_bot) / 2

# Leader line from cut to inset
axL.plot([cut_x - 0.2, profile_x_base - 0.4],
          [cut_y_center, profile_y_mid],
          color=TEXT, linewidth=0.7, linestyle=(0, (1, 2)), alpha=0.6)

# Outline of the cross-section (rectangle) on the left of the stress profile
axL.add_patch(patches.Rectangle((profile_x_base - 0.4, profile_y_bot),
                                  0.35, profile_h,
                                  facecolor="none", edgecolor=TEXT,
                                  linewidth=1.0, alpha=0.7))

# Compression triangle (top half, extending right)
compr_tri = patches.Polygon(
    [(profile_x_base - 0.05, profile_y_top),
     (profile_x_base - 0.05 + 1.4, profile_y_top - 0.1),
     (profile_x_base - 0.05, profile_y_mid)],
    facecolor=RED, alpha=0.35, edgecolor=RED, linewidth=1.2,
)
axL.add_patch(compr_tri)

# Tension triangle (bottom half, extending right)
tens_tri = patches.Polygon(
    [(profile_x_base - 0.05, profile_y_mid),
     (profile_x_base - 0.05 + 1.4, profile_y_bot + 0.1),
     (profile_x_base - 0.05, profile_y_bot)],
    facecolor=BLUE, alpha=0.35, edgecolor=BLUE, linewidth=1.2,
)
axL.add_patch(tens_tri)

# Neutral axis line on the profile
axL.plot([profile_x_base - 0.6, profile_x_base + 1.7],
          [profile_y_mid, profile_y_mid],
          color=GREEN, linewidth=1.2, linestyle=(0, (2, 2)))

# Labels for the stress profile
axL.text(profile_x_base + 1.5, profile_y_top - 0.05, "compression",
          color=RED, fontsize=9.5, ha="left", va="center", style="italic")
axL.text(profile_x_base + 1.5, profile_y_bot + 0.05, "tension",
          color=BLUE, fontsize=9.5, ha="left", va="center", style="italic")
axL.text(profile_x_base + 1.7, profile_y_mid, "neutral axis",
          color=GREEN, fontsize=9.5, ha="left", va="center", style="italic")

# Profile sub-label
axL.text(profile_x_base + 0.6, profile_y_top + 0.35,
          "stress at the cut",
          color=TEXT, fontsize=10, ha="center", style="italic", alpha=0.85)

# Formula at the bottom — single line, well below the L annotation
axL.text(5.5, -5.0,
          r"Euler–Bernoulli:  $EI\,\dfrac{d^2y}{dx^2} = M(x)$    →    $\delta_{\rm tip} = \dfrac{FL^3}{3EI}$",
          color=TEXT, fontsize=11.5, ha="center", style="italic", alpha=0.9)

# Wall label
axL.text(-0.55, 3.9, "fixed", color=TEXT, fontsize=9.5, ha="center",
          style="italic", alpha=0.75)

# ===================================================================
# RIGHT PANEL — Three cross-sections (aspect 10:1 → 100x)
# ===================================================================
axR.set_xlim(-1, 13.5)
axR.set_ylim(-4.5, 5)
axR.set_title(r"Same area, different depth:  $I = b h^{\,3}/12$",
               color=TEXT, fontsize=11.5, pad=8)

# All three cross-sections have AREA = 2.5 (in arbitrary length units)
# A: wide & flat       b=5.0, h=0.5   aspect 10:1
# B: square            b=h=√2.5 ≈ 1.5811
# C: tall & narrow     b=0.5, h=5.0   aspect 1:10

sqrt25 = np.sqrt(2.5)
cs_data = [
    # (letter, descriptor, b, h, x_center, color)
    ("A", "wide & flat",   5.0,    0.5,    2.5,  AMBER),
    ("B", "square",        sqrt25, sqrt25, 7.0,  BLUE),
    ("C", "tall & narrow", 0.5,    5.0,    11.5, GREEN),
]

floor_y = -3.0  # everyone sits on this floor

I_values = []
for entry in cs_data:
    _, _, b, h, _, _ = entry
    I_values.append(b * h ** 3 / 12)

I_A, I_B, I_C = I_values
ratio_B = I_B / I_A
ratio_C = I_C / I_A
ratios = [1.0, ratio_B, ratio_C]

# --- Draw the rectangles and their b/h annotations ---
for (letter, descriptor, b, h, xc, color), I_val in zip(cs_data, I_values):
    rect = patches.Rectangle((xc - b / 2, floor_y), b, h,
                              facecolor=color, alpha=0.35,
                              edgecolor=color, linewidth=1.6)
    axR.add_patch(rect)
    # Width annotation (below the rectangle)
    axR.annotate("", xy=(xc - b / 2, floor_y - 0.25),
                  xytext=(xc + b / 2, floor_y - 0.25),
                  arrowprops=dict(arrowstyle="<->", color=color, lw=0.9, alpha=0.75))
    axR.text(xc, floor_y - 0.7, f"$b = {b:.2g}$", color=color,
              fontsize=9.5, ha="center", style="italic")
    # Height annotation (right side, offset further so it doesn't crowd the next rect)
    h_arrow_x = xc + b / 2 + 0.2
    axR.annotate("", xy=(h_arrow_x, floor_y),
                  xytext=(h_arrow_x, floor_y + h),
                  arrowprops=dict(arrowstyle="<->", color=color, lw=0.9, alpha=0.75))
    axR.text(h_arrow_x + 0.25, floor_y + h / 2, f"$h = {h:.2g}$",
              color=color, fontsize=9.5, ha="left", va="center", style="italic")

# --- Top row labels stacked vertically per column ---
# Vertical layout (top to bottom):  letter / descriptor / I value / ratio
# Each at its own y so the wide descriptors never overlap horizontally.
y_letter     = 4.2
y_descriptor = 3.55
y_I          = 2.95
y_ratio      = 2.35

for (letter, descriptor, b, h, xc, color), I_val, rel in zip(cs_data, I_values, ratios):
    # Big letter (A, B, C)
    axR.text(xc, y_letter, letter, color=color, fontsize=15,
              ha="center", va="center", fontweight="bold")
    # Short descriptor
    axR.text(xc, y_descriptor, descriptor, color=color, fontsize=10,
              ha="center", va="center", style="italic")
    # I value
    axR.text(xc, y_I, f"$I = {I_val:.3g}$", color=color,
              fontsize=10.5, ha="center", va="center")
    # Relative stiffness
    if rel == 1.0:
        rel_txt = r"$\times\,1$  (baseline)"
        weight = "normal"
    else:
        rel_txt = rf"$\times\,{int(round(rel))}$"
        weight = "bold"
    axR.text(xc, y_ratio, rel_txt, color=color, fontsize=12,
              ha="center", va="center", fontweight=weight)

# Bottom caption — split into two lines so it fits within panel width.
# Plain `&` is fine in matplotlib text outside `$...$`; `\&` is not a
# defined mathtext command.
axR.text(6.25, -4.4,
          "All three have the same cross-sectional area.",
          color=TEXT, fontsize=10.5, ha="center", style="italic", alpha=0.85)
axR.text(6.25, -5.0,
          rf"Tall and narrow (C) is $\bf{{{int(round(ratio_C))} \times}}$ stiffer than wide and flat (A)"
          r"  —  because $I \propto h^3$.",
          color=TEXT, fontsize=10.5, ha="center", style="italic", alpha=0.85)

# ===================================================================
# Save outputs
# ===================================================================
plt.tight_layout()
plt.subplots_adjust(top=0.90, bottom=0.04)

script_dir = Path(__file__).resolve().parent
svg_path = script_dir / "beam-bending.svg"
png_path = Path("/tmp") / "beam-bending-verify.png"
plt.savefig(svg_path, format="svg", transparent=True, bbox_inches="tight")
plt.savefig(png_path, format="png", transparent=True, bbox_inches="tight", dpi=150)
plt.close()

print(f"Wrote SVG -> {svg_path}")
print(f"Wrote verification PNG -> {png_path}")
print(f"Areas: A={5.0*0.5}, B={sqrt25*sqrt25:.3f}, C={0.5*5.0}")
print(f"I values: A={I_A:.4f}, B={I_B:.4f}, C={I_C:.4f}")
print(f"Ratios: B/A = {ratio_B:.2f}, C/A = {ratio_C:.2f}")

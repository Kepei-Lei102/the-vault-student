"""
Two free-body diagrams for the friction-limit worked example arcs:

LEFT  — Climber on a sloped ledge (static case). Shows weight, normal, friction,
        and the gravity decomposition along/perpendicular to the slope. The
        slip threshold tan θ = μ_s is derived geometrically.

RIGHT — Motorcycle leaning in a corner (dynamic case). Front view. Shows
        weight, centripetal requirement, and the combined road reaction force
        along the bike's axis. Lean angle θ from vertical with tan θ = v²/(gr).

Output: friction-fbds-climber-motorcycle.svg in the same directory.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

TEXT = "#888888"
AXIS = "#888888"
BLUE = "#2563eb"     # weight
GREEN = "#059669"    # normal force
AMBER = "#f59e0b"    # friction
RED = "#dc2626"      # centripetal / resultant
PURPLE = "#7c3aed"   # angle annotation
GREY = "#bbbbbb"

fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.5, 6.0),
                                gridspec_kw={"width_ratios": [1, 1]})
fig.patch.set_alpha(0)
for ax in (axL, axR):
    ax.set_facecolor("none")
    ax.set_aspect("equal")
    for side in ("top", "right", "bottom", "left"):
        ax.spines[side].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

fig.suptitle("Free-Body Diagrams — Climber on a Slope vs Motorcycle in a Lean",
             color=TEXT, fontsize=14, fontweight="bold", y=1.00)

# ===================================================================
# LEFT PANEL — Climber on a slope (static slip threshold)
# ===================================================================
axL.set_xlim(-1, 11)
axL.set_ylim(-1.5, 9)
axL.set_title("Static case: when does the climber's foot slip?",
              color=TEXT, fontsize=11.5, pad=10)

# Slope angle
theta = 30  # degrees
theta_rad = np.radians(theta)
# Slope line from (0, 0) to (slope_x, slope_y)
slope_x = 9.0
slope_y = slope_x * np.tan(theta_rad)

# Draw the slope (thick brown-ish line) + ground reference
axL.plot([0, slope_x], [0, slope_y], color=GREY, linewidth=3, solid_capstyle="round")
axL.plot([0, slope_x], [0, 0], color=GREY, linewidth=0.8, linestyle=(0, (4, 4)), alpha=0.5)

# Angle arc at the base
arc_radius = 1.3
arc = patches.Arc((0, 0), 2 * arc_radius, 2 * arc_radius,
                   angle=0, theta1=0, theta2=theta,
                   color=PURPLE, linewidth=1.5)
axL.add_patch(arc)
axL.text(arc_radius * 1.25 * np.cos(np.radians(theta / 2)),
          arc_radius * 1.25 * np.sin(np.radians(theta / 2)),
          r"$\theta$", color=PURPLE, fontsize=14,
          ha="center", va="center", style="italic", fontweight="bold")

# Place the climber as a small blob at a point on the slope
cx_along = 5.5  # distance along the slope
cx = cx_along * np.cos(theta_rad)
cy = cx_along * np.sin(theta_rad)

# Climber body — a small rounded rectangle perpendicular to the slope
body_size = 0.7
# Vector perpendicular to slope (pointing up-away-from-slope)
perp_x = -np.sin(theta_rad)
perp_y =  np.cos(theta_rad)
body_center_x = cx + perp_x * body_size * 0.6
body_center_y = cy + perp_y * body_size * 0.6

axL.add_patch(patches.Circle((body_center_x, body_center_y),
                              body_size, facecolor=BLUE, alpha=0.25,
                              edgecolor=BLUE, linewidth=1.8))
axL.text(body_center_x, body_center_y, "m", color=BLUE, fontsize=12,
          ha="center", va="center", style="italic", fontweight="bold")

# Origin for force arrows (climber centre)
ox, oy = body_center_x, body_center_y

# Weight (mg) — straight down
arrow_scale = 1.7
W_dx, W_dy = 0, -arrow_scale
axL.annotate("", xy=(ox + W_dx, oy + W_dy), xytext=(ox, oy),
              arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2,
                               mutation_scale=14))
axL.text(ox + W_dx + 0.3, oy + W_dy + 0.05, r"$mg$",
          color=BLUE, fontsize=13, style="italic", fontweight="bold")

# Normal force — perpendicular to slope, magnitude = mg cos θ
N_mag = arrow_scale * np.cos(theta_rad)
N_dx = perp_x * N_mag
N_dy = perp_y * N_mag
axL.annotate("", xy=(ox + N_dx, oy + N_dy), xytext=(ox, oy),
              arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.2,
                               mutation_scale=14))
axL.text(ox + N_dx - 0.15, oy + N_dy + 0.25, r"$N = mg\cos\theta$",
          color=GREEN, fontsize=11.5, ha="right", style="italic")

# Friction force — along slope, pointing UP-slope (opposes slip-down tendency)
up_slope_x = np.cos(theta_rad)
up_slope_y = np.sin(theta_rad)
F_mag = arrow_scale * np.sin(theta_rad)
F_dx = up_slope_x * F_mag
F_dy = up_slope_y * F_mag
axL.annotate("", xy=(ox + F_dx, oy + F_dy), xytext=(ox, oy),
              arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=2.2,
                               mutation_scale=14))
axL.text(ox + F_dx + 0.1, oy + F_dy + 0.25,
          r"$F_{\rm friction} \leq \mu_s mg \cos\theta$",
          color=AMBER, fontsize=11.5, style="italic")

# Decomposition lines (dotted) — show how mg splits into mg cos θ (perp) and mg sin θ (along)
# along-slope component of weight (pointing DOWN the slope, magnitude mg sin θ)
down_slope_x = -up_slope_x
down_slope_y = -up_slope_y
mgsin_dx = down_slope_x * F_mag
mgsin_dy = down_slope_y * F_mag
axL.annotate("", xy=(ox + mgsin_dx, oy + mgsin_dy), xytext=(ox, oy),
              arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.2,
                               mutation_scale=10, alpha=0.5,
                               linestyle="-"))
axL.text(ox + mgsin_dx - 0.4, oy + mgsin_dy - 0.05,
          r"$mg\sin\theta$",
          color=BLUE, fontsize=10, ha="right", style="italic", alpha=0.75)

# Threshold equation at the bottom
axL.text(5, -0.9,
          r"Slip threshold:  $mg\sin\theta = \mu_s\, mg\cos\theta$  $\Rightarrow$  $\tan\theta_c = \mu_s$",
          color=PURPLE, fontsize=11.5, ha="center", style="italic", fontweight="bold")

# ===================================================================
# RIGHT PANEL — Motorcycle leaning in a corner (dynamic case)
# ===================================================================
axR.set_xlim(-5, 5)
axR.set_ylim(-1.5, 9)
axR.set_title("Dynamic case: what lean angle for a given corner speed?",
              color=TEXT, fontsize=11.5, pad=10)

# Ground line
axR.plot([-5, 5], [0, 0], color=GREY, linewidth=3, solid_capstyle="round")

# Lean angle from vertical
lean = 35  # degrees from vertical
lean_rad = np.radians(lean)

# Bike axis from contact point (0, 0) to CG at distance r
bike_length = 6.0
cg_x = bike_length * np.sin(lean_rad)
cg_y = bike_length * np.cos(lean_rad)

# Draw the bike axis (two lines meeting at the contact point, suggesting a bike silhouette)
axR.plot([0, cg_x], [0, cg_y], color=GREY, linewidth=4.5, solid_capstyle="round", alpha=0.75)
# Small triangle at the bottom to suggest the tire
axR.add_patch(patches.Circle((0, 0.15), 0.25,
                              facecolor="#444444", edgecolor="#444444",
                              alpha=0.7))

# CG dot
axR.plot([cg_x], [cg_y], "o", color="#444444", markersize=9, zorder=5)
axR.text(cg_x + 0.4, cg_y + 0.15, "CG", color=TEXT, fontsize=10.5,
          ha="left", va="center", style="italic")

# Vertical reference line (dashed) from contact point straight up
axR.plot([0, 0], [0, cg_y + 1.5], color=GREY, linewidth=0.8,
          linestyle=(0, (4, 4)), alpha=0.5)

# Lean angle arc near the contact point
lean_arc_r = 1.0
arc2 = patches.Arc((0, 0), 2 * lean_arc_r, 2 * lean_arc_r,
                    angle=0, theta1=90 - lean, theta2=90,
                    color=PURPLE, linewidth=1.5)
axR.add_patch(arc2)
axR.text(lean_arc_r * 0.55 * np.sin(lean_rad / 2),
          lean_arc_r * 0.85 * np.cos(lean_rad / 2),
          r"$\theta$", color=PURPLE, fontsize=14,
          ha="left", va="center", style="italic", fontweight="bold")

# Forces at the CG:
# Weight (mg) — straight down
axR.annotate("", xy=(cg_x, cg_y - 1.8), xytext=(cg_x, cg_y),
              arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2,
                               mutation_scale=14))
axR.text(cg_x + 0.25, cg_y - 0.95, r"$mg$",
          color=BLUE, fontsize=13, style="italic", fontweight="bold")

# Centripetal requirement (horizontal toward corner centre — to the LEFT, since bike leans right)
# Actually if bike leans INTO the corner, the corner centre is on the LEFT side
# Let's say corner is to the left (negative x)
axR.annotate("", xy=(cg_x - 1.8, cg_y), xytext=(cg_x, cg_y),
              arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2,
                               mutation_scale=14))
axR.text(cg_x - 1.85, cg_y + 0.3, r"$mv^2/r$",
          color=RED, fontsize=12, ha="right", style="italic", fontweight="bold")
axR.text(cg_x - 1.85, cg_y - 0.05, "(centripetal,",
          color=RED, fontsize=9.5, ha="right", style="italic")
axR.text(cg_x - 1.85, cg_y - 0.35, "toward corner)",
          color=RED, fontsize=9.5, ha="right", style="italic")

# Forces at the contact point (tire):
# Normal force — straight up
axR.annotate("", xy=(0, 1.8), xytext=(0, 0.4),
              arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.2,
                               mutation_scale=14))
axR.text(0.2, 1.4, r"$N$", color=GREEN, fontsize=13,
          style="italic", fontweight="bold")

# Friction force — horizontal toward corner centre (left)
axR.annotate("", xy=(-1.6, 0.4), xytext=(0, 0.4),
              arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=2.2,
                               mutation_scale=14))
axR.text(-1.65, 0.65, r"$F_{\rm friction}$",
          color=AMBER, fontsize=12, ha="right", style="italic", fontweight="bold")

# Threshold equation at the bottom
axR.text(0, -0.9,
          r"Steady lean:  $\tan\theta = \dfrac{v^2/r}{g} = \dfrac{v^2}{gr}$  ;  friction needed:  $\dfrac{v^2}{gr} \leq \mu_s$",
          color=PURPLE, fontsize=11.5, ha="center", style="italic", fontweight="bold")

# ===================================================================
# Save outputs
# ===================================================================
plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.05)

script_dir = Path(__file__).resolve().parent
svg_path = script_dir / "friction-fbds-climber-motorcycle.svg"
png_path = Path("/tmp") / "friction-fbds-verify.png"
plt.savefig(svg_path, format="svg", transparent=True, bbox_inches="tight")
plt.savefig(png_path, format="png", transparent=True, bbox_inches="tight", dpi=150)
plt.close()

print(f"Wrote SVG -> {svg_path}")
print(f"Wrote verification PNG -> {png_path}")

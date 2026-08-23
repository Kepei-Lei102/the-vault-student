"""Figure for the Arc Length and Surfaces of Revolution card.

Regenerate:  python3 arc-length-figures.py
Writes, beside this file:
  arc-length-sliver.svg — two tall panels. Top: the odometer step — a curve
      with one sliver magnified into its right triangle, legs dx and dy,
      hypotenuse ds = sqrt(dx^2+dy^2). Bottom: the sliver revolved about the
      x-axis sweeps a frustum band of slant width ds — drawn beside the wrong
      cylinder of width dx (the shadow), with the cone test annotated.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

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

fig, (top, bot) = plt.subplots(2, 1, figsize=(8.6, 12.6))

# ---------- Top: the sliver triangle ----------
f = lambda x: 0.55 + 0.4*np.sin(1.1*x) + 0.12*x
xs = np.linspace(0, 4.4, 300)
top.plot(xs, f(xs), color=BLUE, lw=2.6)
x0, x1 = 0.7, 1.2
top.plot([x0, x1], [f(x0), f(x1)], color=GREEN, lw=3, zorder=5)
top.plot([x0, x1], [f(x0), f(x0)], color=AMBER, lw=2, zorder=5)
top.plot([x1, x1], [f(x0), f(x1)], color=RED, lw=2, zorder=5)

# magnified inset triangle (computed, offset to the right)
Mx, My, k = 3.4, 0.15, 3.4
dx_, dy_ = (x1-x0)*k, (f(x1)-f(x0))*k
top.plot([Mx, Mx+dx_], [My, My], color=AMBER, lw=3)
top.plot([Mx+dx_, Mx+dx_], [My, My+dy_], color=RED, lw=3)
top.plot([Mx, Mx+dx_], [My, My+dy_], color=GREEN, lw=3.6)
top.text(Mx+dx_/2, My-0.14, r"$dx$", color=AMBER, fontsize=15, ha="center")
top.text(Mx+dx_+0.08, My+dy_/2-0.03, r"$dy$", color=RED, fontsize=15)
top.text(Mx+dx_/2-0.15, My+dy_/2+0.40,
         r"$ds=\sqrt{dx^2+dy^2}$", color=GREEN, fontsize=15, ha="center")
top.annotate("", xy=(Mx+0.1, My+0.1), xytext=((x0+x1)/2+0.06, f((x0+x1)/2)+0.02),
             arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2))
top.text(0.25, 1.35, "zoom far enough in and every smooth curve is straight —\n"
         "one odometer step, measured by Pythagoras", fontsize=13, color=AX)
top.set_xlim(-0.1, 5.6); top.set_ylim(-0.15, 1.65)
top.set_axis_off()
top.set_title("Arc length: add up the hypotenuses", fontsize=15, color=AX)

# ---------- Bottom: the frustum band vs the shadow cylinder ----------
bot.set_xlim(-0.1, 10.4); bot.set_ylim(-2.95, 3.4)
bot.set_axis_off()
bot.set_title("Rotate the sliver: a slanted band of width ds — not its shadow dx",
              fontsize=15, color=AX)

def frustum(ax_, cx, y_left, y_right, w, colr):
    for dxs, r in [(0.0, y_left), (w, y_right)]:
        ax_.add_patch(Ellipse((cx+dxs, 0), 0.34, 2*r, fill=False,
                              edgecolor=colr, lw=2))
    ax_.plot([cx, cx+w], [y_left, y_right], color=colr, lw=2.6)
    ax_.plot([cx, cx+w], [-y_left, -y_right], color=colr, lw=2.6)
    ax_.plot([cx-0.8, cx+w+0.8], [0, 0], color=GREY, lw=1, ls="-.")

cx, yl, yr, w = 3.4, 1.05, 1.75, 1.7
frustum(bot, cx, yl, yr, w, GREEN)
# the slant width ds, labelled along the top slant
bot.annotate("", xy=(cx+w+0.12, yr+0.24), xytext=(cx-0.12, yl+0.24),
             arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.6))
bot.text(cx+w/2, (yl+yr)/2+0.62, "width of the band = $ds$ (the slant)",
         color=GREEN, fontsize=13.5, ha="center")
# the shadow dx, bracketed below the axis
bot.annotate("", xy=(cx+w, -yr-0.28), xytext=(cx, -yr-0.28),
             arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
bot.text(cx+w+0.45, -yr-0.38, "its shadow on the axis = $dx$\n— shorter, always",
         color=RED, fontsize=13.5, ha="left")
bot.text(cx+w+1.2, 0.75, "radius of the hoop = $y$,\nits circumference = $2\\pi y$",
         color=BLUE, fontsize=13.5)
bot.annotate("", xy=(cx+w, yr*0.02), xytext=(cx+w, yr),
             arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.4))
bot.text(5.2, -2.62,
         "cone test: truth unrolls to  $\\pi r l$;  the shadow gives  $\\pi r h$  — always too small",
         fontsize=13.5, color=AX, ha="center")
bot.text(5.2, 2.9, r"$dS = 2\pi y\, ds$   (circumference at radius $y$, times slant width)",
         fontsize=14.5, color=GREEN, ha="center")

fig.tight_layout(h_pad=2.2)
fig.savefig("arc-length-sliver.svg", transparent=True, bbox_inches="tight",
            metadata={"Date": None})
print("wrote arc-length-sliver.svg")

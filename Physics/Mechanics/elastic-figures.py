"""Figures for Elastic Strings and Springs.

Two SVGs:
  elastic-string-vs-spring.svg  — tension-extension law: string vs spring, EPE as area
  elastic-vertical-journey.svg  — the vertical "just reaches O" journey (N24/33 shape)

Run:  python3 elastic-figures.py   (from Physics/Mechanics/)
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({
    "svg.hashsalt": "vault",
    "font.size": 12,
    "text.color": "#888888",
    "axes.edgecolor": "#888888",
    "axes.labelcolor": "#888888",
    "xtick.color": "#888888",
    "ytick.color": "#888888",
    "svg.fonttype": "none",
})

BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"


def save(fig, name):
    fig.savefig(name, format="svg", bbox_inches="tight",
                transparent=True, metadata={"Date": None})
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------- figure 1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))

x = np.linspace(-1.0, 1.6, 300)
spring = 1.0 * x
string = np.where(x > 0, 1.0 * x, 0.0)

ax1.axhline(0, color="#888888", lw=0.8)
ax1.axvline(0, color="#888888", lw=0.8)
ax1.plot(x, spring, color=PURPLE, lw=2.2, ls="--", label="spring")
ax1.plot(x, string, color=BLUE, lw=2.6, label="elastic string")
ax1.fill_between(x[x <= 0], spring[x <= 0], 0, color=(124/255, 58/255, 237/255, 0.12))
ax1.text(-1.05, -0.88, "spring pushes back\nwhen compressed", color="#888888",
         fontsize=10, ha="left", va="bottom")
ax1.annotate("string goes slack:\nT = 0, no push, ever", xy=(-0.55, 0.03), xytext=(-1.05, 0.75),
             color="#888888", fontsize=10, ha="left",
             arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
ax1.text(1.28, 1.52, r"$T=\frac{\lambda x}{L}$", color="#888888", fontsize=13, ha="center")
ax1.set_xlabel("extension  x")
ax1.set_ylabel("tension  T")
ax1.set_title("One law, two behaviours", color="#888888")
ax1.set_xlim(-1.15, 1.75)
ax1.set_ylim(-1.05, 1.85)
ax1.set_xticks([0]); ax1.set_yticks([0])
for s in ("top", "right"):
    ax1.spines[s].set_visible(False)
leg = ax1.legend(loc="lower right", frameon=False, fontsize=10)
for t in leg.get_texts():
    t.set_color("#888888")

X = 1.2
xs = np.linspace(0, X, 100)
ax2.plot(xs, xs, color=BLUE, lw=2.6)
ax2.fill_between(xs, xs, 0, color=(37/255, 99/255, 235/255, 0.15))
ax2.plot([X, X], [0, X], color="#888888", lw=0.9, ls=":")
ax2.plot([0, X], [X, X], color="#888888", lw=0.9, ls=":")
ax2.text(X/2 + 0.06, X/5, "area = EPE", color="#888888", fontsize=11)
ax2.text(X + 0.05, X/2, r"$\frac{\lambda x}{L}$", color="#888888", fontsize=12)
ax2.text(0.30, 1.28, r"$E=\frac{1}{2} \times x \times \frac{\lambda x}{L}=\frac{\lambda x^2}{2L}$",
         color="#888888", fontsize=13)
ax2.set_xlabel("extension")
ax2.set_ylabel("tension")
ax2.set_title("The triangle again", color="#888888")
ax2.set_xlim(0, 1.75)
ax2.set_ylim(0, 1.6)
ax2.set_xticks([]); ax2.set_yticks([])
for s in ("top", "right"):
    ax2.spines[s].set_visible(False)

save(fig, "elastic-string-vs-spring.svg")

# ---------------------------------------------------------------- figure 2
fig, ax = plt.subplots(figsize=(8.6, 5.6))

# depths below O (positive down): natural length 2, equilibrium 3, lowest 3+sqrt5
d = np.sqrt(5)
depth_nat, depth_eq, depth_low = 2.0, 3.0, 3.0 + d

ax.axhline(0, color="#888888", lw=1.4)
ax.text(-0.05, 0.12, "O", color="#888888", fontsize=13, ha="right")

# the string zones drawn as a vertical bar at x=0
ax.plot([0, 0], [0, -depth_nat], color=TEAL, lw=3, alpha=0.9)
ax.plot([0, 0], [-depth_nat, -depth_low], color=BLUE, lw=3, alpha=0.9)

for y, lab, c in [(-depth_nat, "natural length ends here\nstring taut below, slack above", TEAL),
                  (-depth_eq, "equilibrium:  T = mg\n(max speed on the way up)", GREEN),
                  (-depth_low, "lowest point:  v = 0\npulled down d below equilibrium", RED)]:
    ax.plot([-0.35, 0.35], [y, y], color=c, lw=1.6)
    ax.text(0.45, y, lab, color="#888888", fontsize=10.5, va="center")

# journey arrow (up), offset left
ax.annotate("", xy=(-0.75, -0.1), xytext=(-0.75, -depth_low + 0.1),
            arrowprops=dict(arrowstyle="->", color=AMBER, lw=2.2))
ax.text(-0.9, -depth_low/2, "the journey up", color="#888888", fontsize=11,
        rotation=90, va="center", ha="center")

# phase labels on the right of the arrow
ax.text(-1.55, -(depth_nat + depth_low)/2, "string taut:\ntension + gravity\n(EPE, GPE, KE all trade)",
        color="#888888", fontsize=10, ha="center", va="center")
ax.text(-1.55, -depth_nat/2, "string slack:\ngravity only\n(free flight)",
        color="#888888", fontsize=10, ha="center", va="center")
ax.annotate("just reaches O:  v = 0", xy=(0, 0), xytext=(1.1, 0.55),
            color="#888888", fontsize=11,
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.4))

ax.set_xlim(-2.4, 3.6)
ax.set_ylim(-depth_low - 0.55, 1.0)
ax.axis("off")
save(fig, "elastic-vertical-journey.svg")

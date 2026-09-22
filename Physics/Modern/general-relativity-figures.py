"""Figures for General Relativity.md — run: python3 general-relativity-figures.py   (writes four SVGs beside the card)."""
import math, re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch, Arc

TXT = "#888"
BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": TXT, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT,
                     "axes.edgecolor": TXT, "font.size": 11, "svg.fonttype": "none"})


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    txt = open(name).read()
    m = re.search(r"<svg[^>]*>", txt)
    tag = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0))          # drop the fixed size
    tag = tag.replace("<svg", '<svg width="100%"', 1)                    # scale to the column, no height
    txt = txt[:m.start()] + tag + txt[m.end():]
    open(name, "w").write(txt)
    plt.close(fig)


def lift(ax, x0, y0, w, h, color):
    ax.add_patch(Rectangle((x0, y0), w, h, fill=False, ec=color, lw=2))
    ax.plot([x0 + w*0.15, x0 + w*0.15], [y0 + h*0.1, y0 + h*0.42], color=color, lw=6, solid_capstyle="round")  # a person
    ax.add_patch(Circle((x0 + w*0.15, y0 + h*0.5), h*0.06, color=color))


# ── 1. the lift: acceleration and gravity give the same bent beam ──────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
for ax, title, arrow_up, ground in [(axes[0], "Accelerating lift, far from any planet", True, False),
                                     (axes[1], "The same lift standing on the Earth", False, True)]:
    ax.set_xlim(-1.2, 4.2); ax.set_ylim(-0.6, 3.6); ax.set_aspect("equal"); ax.axis("off")
    if not ground:
        rng = np.random.default_rng(3); sx, sy = rng.uniform(-1.2, 4.2, 70), rng.uniform(-0.6, 3.6, 70)
        keep = ~((sx > 0.4) & (sx < 3.2) & (sy > -0.1) & (sy < 3.1)); ax.scatter(sx[keep], sy[keep], s=4, color=TXT, alpha=.5)
    else:
        ax.fill_between([-1.2, 4.2], -0.6, 0, color=GREEN, alpha=.15); ax.plot([-1.2, 4.2], [0, 0], color=GREEN, lw=2)
    lift(ax, 0.5, 0, 2.6, 3.0, BLUE)
    x = np.linspace(0.5, 3.1, 60); y = 2.5 - 0.35*((x-0.5)/2.6)**2 * 2.6
    ax.plot(x, y, color=AMBER, lw=2.5)
    ax.annotate("", xy=(0.5, 2.5), xytext=(-0.9, 2.5), arrowprops=dict(arrowstyle="->", color=AMBER, lw=2))
    ax.text(-1.1, 2.62, "light pulse", color=AMBER, fontsize=10)
    ax.plot([0.5, 3.1], [2.5, 2.5], color=TXT, lw=0.8, ls="--")
    ax.text(3.2, y[-1]-0.05, "lower", color=AMBER, fontsize=10, va="center")
    if arrow_up:
        ax.annotate("", xy=(3.8, 2.6), xytext=(3.8, 1.0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5))
        ax.text(3.85, 1.7, "a", color=RED, fontsize=14, style="italic")
    else:
        ax.annotate("", xy=(3.8, 1.0), xytext=(3.8, 2.6), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5))
        ax.text(3.85, 1.7, "g", color=RED, fontsize=14, style="italic")
    ax.set_title(title, color=TXT, fontsize=11)
fig.text(0.5, -0.02, "Inside, nothing you can measure tells the two apart: the pulse crosses the lift and arrives lower on the far wall in both. "
         "Whatever acceleration does to light and to clocks, gravity does too.", ha="center", color=TXT, fontsize=10)
save(fig, "general-relativity-elevator.svg")

# ── 2. clock rate against altitude, for a circular orbit ───────────────────────────────────────────────────────
G, c, M, R = 6.674e-11, 2.998e8, 5.972e24, 6.371e6
alt = np.linspace(0, 40000, 800) * 1e3; r = R + alt
gr = (G*M/R - G*M/r)/c**2 * 86400 * 1e6
sr = -(G*M/r)/(2*c**2) * 86400 * 1e6
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.plot(alt/1e3, gr, color=PURPLE, lw=2, label="gravity: weaker field higher up, clock runs fast")
ax.plot(alt/1e3, sr, color=BLUE, lw=2, label="speed: orbital motion, clock runs slow")
ax.plot(alt/1e3, gr+sr, color=GREEN, lw=3, label="net, for a satellite in a circular orbit")
ax.axhline(0, color=TXT, lw=0.8)
for name, a, dx, dy, ha in [("ISS, −24.5 μs a day", 420, 1200, -1, "left"), ("GPS, +38.5", 20180, 0, 4, "center"), ("geostationary, +46", 35786, 0, -7, "center")]:
    ri = R + a*1e3; net = ((G*M/R - G*M/ri)/c**2 - (G*M/ri)/(2*c**2))*86400*1e6
    ax.plot(a, net, "o", color=GREEN, ms=7); ax.text(a+dx, net+dy, name, color=GREEN, ha=ha, fontsize=10)
ax.plot(3186, 0, "o", color=RED, ms=6); ax.text(3400, -8, "cancel at 3 190 km\n(r = 1.5 Earth radii)", color=RED, fontsize=9)
ax.set_xlabel("altitude of the orbit / km"); ax.set_ylabel("μs gained per day against a ground clock")
ax.set_ylim(-35, 60); ax.grid(alpha=.25); ax.legend(loc="lower right", fontsize=9, frameon=False)
for s in ("top", "right"): ax.spines[s].set_visible(False)
save(fig, "general-relativity-clock-rate.svg")

# ── 3. light deflection: the impulse picture ───────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 4.2)); ax.set_xlim(-5, 5); ax.set_ylim(-1.3, 2.6); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(Circle((0, 0), 0.9, color=AMBER, alpha=.35)); ax.add_patch(Circle((0, 0), 0.9, fill=False, ec=AMBER, lw=2))
ax.text(0, -1.2, "Sun, mass M", ha="center", color=AMBER)
b = 1.3
x = np.linspace(-5, 5, 400); bend = 0.35
y = np.where(x < 0, b, b - bend*x/5*1.0)          # exaggerated: straight in, tilted out
ax.plot(x[x < 0], y[x < 0], color=RED, lw=2.2); ax.plot(x[x >= 0], y[x >= 0], color=RED, lw=2.2)
ax.plot([0, 5], [b, b], color=TXT, lw=0.8, ls="--")
ax.annotate("", xy=(0, 0.1), xytext=(0, b), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.2))
ax.text(0.12, 0.6, "pull toward M\nat closest approach", color=PURPLE, fontsize=9)
ax.annotate("", xy=(-1.7, b), xytext=(-1.7, 0.0), arrowprops=dict(arrowstyle="<->", color=TEAL, lw=1.4))
ax.plot([-1.7, 0], [0, 0], color=TEAL, lw=0.8, ls=":")
ax.text(-1.95, 0.6, "b", color=TEAL, fontsize=13, style="italic")
ax.add_patch(Arc((0, b), 6, 6, theta1=-bend/5*180/math.pi*57.3*0.0+ -4.0, theta2=0, color=RED, lw=1.2))
ax.text(3.3, b+0.12, "deflection θ, hugely exaggerated", color=RED, fontsize=9)
ax.text(-4.9, b+0.25, "light from a distant star", color=RED, fontsize=10)
ax.text(-4.9, 2.35, "Newton, light as fast particles: sideways kick ≈ force × time near the Sun ≈ (GMm/b²)(2b/c), so θ = 2GM/(bc²) = 0.87″ at the limb.",
        color=TXT, fontsize=9.5)
ax.text(-4.9, 2.05, "Einstein, curved space and time together: exactly twice that, 1.75″. Measured 1919: 1.6 to 2.0″. Radio, 2004: 1.7499 ± 0.0003″.",
        color=TXT, fontsize=9.5)
save(fig, "general-relativity-deflection.svg")

# ── 4. tides: what a big enough lift still detects ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
ax = axes[0]; ax.set_xlim(-3, 3); ax.set_ylim(-3.4, 2.6); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(Circle((0, -6.2), 3.6, color=TEAL, alpha=.25)); ax.add_patch(Circle((0, -6.2), 3.6, fill=False, ec=TEAL, lw=2))
ax.text(0, -3.1, "Earth", color=TEAL, ha="center")
ax.add_patch(Rectangle((-2.4, 0.2), 4.8, 1.6, fill=False, ec=BLUE, lw=2))
for xb in (-1.8, 1.8):
    ax.add_patch(Circle((xb, 1.3), 0.13, color=RED))
    ax.plot([xb, 0], [1.3, -6.2], color=RED, lw=0.8, ls="--")
    ax.annotate("", xy=(xb*0.78, -0.25), xytext=(xb, 1.05), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
ax.annotate("", xy=(-1.2, 1.3), xytext=(1.2, 1.3), arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.5))
ax.text(0, 1.45, "they drift together", color=PURPLE, ha="center", fontsize=9)
ax.text(0, 2.3, "A wide lift in free fall: each ball falls toward the centre of the Earth,\nso the two approach each other. No acceleration of the lift can fake that.",
        ha="center", color=TXT, fontsize=9.5)
ax = axes[1]; ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(Circle((0, 0), 1.2, fill=False, ec=TXT, lw=1.5))
t = np.linspace(0, math.pi/2, 100)
for lon, col in ((-0.45, RED), (0.45, RED)):
    x = 1.2*np.sin(lon)*np.cos(t); y = 1.2*np.sin(t)
    ax.plot(x, y, color=col, lw=2.2)
ax.plot(1.2*np.cos(np.linspace(0, math.pi, 100)), -0.15*np.sin(np.linspace(0, math.pi, 100)), color=TXT, lw=1, ls="--")
ax.add_patch(Circle((0, 1.2), 0.05, color=PURPLE))
ax.text(0.1, 1.28, "they meet", color=PURPLE, fontsize=9)
ax.text(-1.48, -0.55, "start parallel\nat the equator", color=RED, fontsize=9)
ax.text(0, -1.45, "Two paths that begin parallel on a sphere converge. The paths of the two balls converge\n"
        "the same way: that is what it means to say space-time is curved near a mass.", ha="center", color=TXT, fontsize=9.5)
save(fig, "general-relativity-tidal.svg")
print("wrote 4 SVGs")

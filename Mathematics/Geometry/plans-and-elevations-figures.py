"""Figures for Plans and Elevations (Vocab).md — run: python3 plans-and-elevations-figures.py
Builds solids from unit cubes, draws each in isometric projection, and computes its plan, front elevation and side
elevation by projection, drawing an edge wherever the visible surface changes depth. Nothing is drawn by hand."""
import math, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

TXT = "#888"; BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": TXT, "font.size": 10, "svg.fonttype": "none"})
C30, S30 = math.cos(math.radians(30)), 0.5

def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name).read(); m = re.search(r"<svg[^>]*>", s)
    tag = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)).replace("<svg", '<svg width="100%"', 1)
    open(name, "w").write(s[:m.start()] + tag + s[m.end():]); plt.close(fig)

def iso(x, y, z):                                   # viewer up and to the front-right: +x to the right, +y to the front-left
    return (x - y) * C30, (x + y) * S30 + z

def draw_solid(ax, cubes, color=BLUE):
    top, right, left = color, color, color
    for (x, y, z) in sorted(cubes, key=lambda c: c[0] + c[1] + c[2]):
        faces = [([(x, y, z + 1), (x + 1, y, z + 1), (x + 1, y + 1, z + 1), (x, y + 1, z + 1)], 0.55),   # top
                 ([(x + 1, y, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x + 1, y, z + 1)], 0.35),   # +x side
                 ([(x, y + 1, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x, y + 1, z + 1)], 0.2)]    # +y side (front)
        for pts, a in faces:
            ax.add_patch(Polygon([iso(*p) for p in pts], closed=True, facecolor=color, alpha=a, edgecolor=color, lw=1.2))
    ax.set_aspect("equal"); ax.axis("off")

def view(ax, cubes, which, color=PURPLE, title="", ylim=(-0.6, 3.6)):
    """which: 'plan' (from above, front at the bottom), 'front' (from the front, +y side), 'side' (from the right, +x side)."""
    cells = {}                                       # (u, v) on the page -> depth of the nearest visible cube
    for (x, y, z) in cubes:
        if which == "plan":   u, v, depth = x, -y, -z            # looking down: nearer means higher z
        elif which == "front": u, v, depth = x, z, -y           # looking from +y: nearer means larger y
        else:                  u, v, depth = -y, z, -x           # looking from +x: nearer means larger x; +y appears to the left
        cells[(u, v)] = min(cells.get((u, v), 99), depth)
    for (u, v), d in cells.items():
        ax.add_patch(Polygon([(u, v), (u + 1, v), (u + 1, v + 1), (u, v + 1)], closed=True, facecolor=color, alpha=0.18, edgecolor="none"))
    for (u, v), d in cells.items():                  # an edge wherever the visible surface changes depth, or ends
        for (du, dv, seg) in [(1, 0, [(u + 1, v), (u + 1, v + 1)]), (-1, 0, [(u, v), (u, v + 1)]), (0, 1, [(u, v + 1), (u + 1, v + 1)]), (0, -1, [(u, v), (u + 1, v)])]:
            if cells.get((u + du, v + dv)) != d:
                ax.plot(*zip(*seg), color=color, lw=1.8)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title, color=TXT, fontsize=10)
    us = [u for u, _ in cells]; vs = [v for _, v in cells]
    ax.set_xlim(min(us) - 0.6, max(us) + 1.6); ax.set_ylim(min(vs) - 0.6, max(vs) + 1.6) if ylim is None else ax.set_ylim(*ylim)

# ── 1. one solid, three views ─────────────────────────────────────────────────────────────────────────────────
solid = {(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 2), (1, 0, 1)}
fig = plt.figure(figsize=(11, 3.9)); gs = fig.add_gridspec(1, 4, width_ratios=[1.6, 1, 1, 1])
ax = fig.add_subplot(gs[0]); draw_solid(ax, solid); ax.set_xlim(-2.8, 3.6); ax.set_ylim(-1.1, 3.7)
ax.set_title("the solid, seven cubes", color=TXT, fontsize=10)
ax.text(-1.5, -0.75, "front, this side", color=TXT, fontsize=9, ha="center"); ax.text(2.3, -0.75, "right side", color=TXT, fontsize=9, ha="center")
view(fig.add_subplot(gs[1]), solid, "plan", title="plan", ylim=(-2.6, 1.6))
view(fig.add_subplot(gs[2]), solid, "front", title="front elevation", ylim=(-0.6, 3.6))
view(fig.add_subplot(gs[3]), solid, "side", title="side elevation, from the right", ylim=(-0.6, 3.6))
fig.text(0.5, -0.03, "The plan is from straight above with the front at the bottom. Each view is a photograph with the depth squashed out. A line is drawn wherever the surface you can see changes level, so the step in the plan and the notch in the front elevation are real edges, not decoration.", ha="center", color=TXT, fontsize=9.5)
save(fig, "plans-and-elevations-three-views.svg")

# ── 2. two solids with the same plan and the same front elevation ──────────────────────────────────────────────
A = {(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0), (0, 0, 1), (0, 1, 1)}
B = {(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0), (0, 0, 1), (0, 0, 2) - (0, 0, 1) if False else (0, 1, 1)}
B = {(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0), (0, 1, 1)}       # the same plan, the same front, a different side
fig, axes = plt.subplots(2, 4, figsize=(11, 5.6), gridspec_kw={"width_ratios": [1.5, 1, 1, 1]})
for row, (name, S, col) in enumerate([("solid A", A, BLUE), ("solid B", B, GREEN)]):
    draw_solid(axes[row][0], S, col); axes[row][0].set_xlim(-2.5, 3.2); axes[row][0].set_ylim(-0.5, 3.6); axes[row][0].set_title(name, color=col, fontsize=10)
    view(axes[row][1], S, "plan", col, "plan", ylim=(-2.6, 1.6)); view(axes[row][2], S, "front", col, "front elevation", ylim=(-0.6, 3.6)); view(axes[row][3], S, "side", col, "side elevation", ylim=(-0.6, 3.6))
fig.text(0.5, -0.02, "Same plan, same front elevation, different solids: only the side elevation tells them apart. One view is never enough, and two often are not.", ha="center", color=TXT, fontsize=9.5)
save(fig, "plans-and-elevations-two-solids.svg")
print("wrote 2 SVGs")

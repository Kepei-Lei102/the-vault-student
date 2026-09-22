"""tech-stack-figures.py — the anatomy diagram and the lab's measurements.

Run after tech-stack-lab.py (reads tech-stack-lab.json). Writes
tech-stack-anatomy.svg and tech-stack-measurements.svg beside the card.
"""
import json, os, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
TXT, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"font.size": 10, "text.color": TXT, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT,
                     "axes.edgecolor": TXT, "svg.fonttype": "none", "font.family": "sans-serif"})

def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)
    s = open(path).read()
    s = re.sub(r'<svg([^>]*?)\s(width|height)="[^"]*"', r'<svg\1', s, count=2)
    s = re.sub(r'<svg([^>]*?)\s(width|height)="[^"]*"', r'<svg\1', s, count=2)
    s = s.replace("<svg", '<svg width="100%"', 1)
    open(path, "w").write(s)

# ───────────── figure 1: the anatomy ─────────────
fig, ax = plt.subplots(figsize=(12, 5.4)); ax.set_xlim(0, 12); ax.set_ylim(0, 5.4); ax.axis("off")

def box(x, y, w, h, label, col, sub=None, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=col, alpha=0.18, ec=col, lw=1.4, ls=ls))
    ax.text(x + w / 2, y + h / 2 + (0.13 if sub else 0), label, ha="center", va="center", color=col, fontsize=10, fontweight="bold")
    if sub: ax.text(x + w / 2, y + h / 2 - 0.17, sub, ha="center", va="center", color=TXT, fontsize=7.8)

def arrow(x0, y0, x1, y1, col=TXT, text=None, dy=0.12):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="<->", color=col, lw=1.1, mutation_scale=12))
    if text: ax.text((x0 + x1) / 2, (y0 + y1) / 2 + dy, text, ha="center", va="bottom", color=col, fontsize=7.6)

# tiers, left to right
ax.text(1.05, 5.15, "the user's device", ha="center", color=TXT, fontsize=9)
box(0.3, 3.3, 1.5, 1.2, "browser / app", BLUE, "HTML, CSS, JS;\nkeeps nothing you trust")
ax.text(3.35, 5.15, "the edge (a provider's\nnearby data centre)", ha="center", color=TXT, fontsize=9)
box(2.6, 3.3, 1.5, 1.2, "DNS · TLS · CDN", TEAL, "names, encryption,\ncached static files")
ax.text(5.65, 5.15, "your servers", ha="center", color=TXT, fontsize=9)
box(4.9, 3.3, 1.5, 1.2, "load balancer", TXT, "spreads requests\nover N copies")
for k, yy in enumerate((3.95, 2.75, 1.55)):
    box(7.0, yy, 1.5, 0.95, "app server %d" % (k + 1), PURPLE, "the API: validate,\ndecide, reply")
ax.text(9.95, 5.15, "state, which is why\nthere is only one", ha="center", color=TXT, fontsize=9)
box(9.2, 3.55, 1.5, 0.95, "cache", AMBER, "fast, small,\nallowed to be stale")
box(9.2, 2.05, 1.5, 1.1, "database", GREEN, "the truth; survives\nevery restart")
box(9.2, 0.55, 1.5, 0.95, "object storage", GREEN, "files: images,\nuploads, backups")
box(4.9, 0.45, 3.6, 0.9, "logs · metrics · alerts", RED, "the only way to know it is broken\nbefore a user tells you")
box(0.3, 0.45, 3.8, 0.9, "deployment", TXT, "push, build, test, then swap in the new\nversion one server at a time", ls="--")

arrow(1.8, 3.9, 2.6, 3.9, text="HTTPS", dy=0.72)
arrow(4.1, 3.9, 4.9, 3.9, text="cache miss", dy=0.72)
for yy in (4.42, 3.22, 2.02):
    ax.add_patch(FancyArrowPatch((6.4, 3.9), (7.0, yy), arrowstyle="<->", color=TXT, lw=1.0, mutation_scale=11, connectionstyle="arc3,rad=0.0"))
arrow(8.5, 3.9, 9.2, 4.0, col=AMBER, text="read")
arrow(8.5, 3.4, 9.2, 2.6, col=GREEN, text="SQL", dy=-0.3)
arrow(8.5, 2.0, 9.2, 1.05, col=GREEN, text="files", dy=-0.3)
ax.text(6.0, 0.15, "Request path: left to right and back. Everything left of the database can be duplicated, restarted or thrown away; the data tier is what must never be lost.", ha="center", color=TXT, fontsize=8.3)
save(fig, "tech-stack-anatomy.svg")

# ───────────── figure 2: the lab's numbers ─────────────
R = json.load(open(os.path.join(HERE, "tech-stack-lab.json")))
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.6))
names = list(R["latency"].keys()); p50 = [R["latency"][k]["p50_ms"] for k in names]; p99 = [R["latency"][k]["p99_ms"] for k in names]
xs = range(len(names))
a1.bar([x - 0.18 for x in xs], p50, width=0.36, color=PURPLE, alpha=0.75, label="median")
a1.bar([x + 0.18 for x in xs], p99, width=0.36, color=RED, alpha=0.6, label="slowest 1 %")
for x, v in zip(xs, p50): a1.text(x - 0.18, v + 0.02, "%.2f" % v, ha="center", color=PURPLE, fontsize=8)
for x, v in zip(xs, p99): a1.text(x + 0.18, v + 0.02, "%.2f" % v, ha="center", color=RED, fontsize=8)
a1.set_xticks(list(xs)); a1.set_xticklabels([n.replace(", ", "\n") for n in names], fontsize=8.5)
a1.set_ylabel("round trip on one machine / ms"); a1.set_ylim(0, max(p99) * 1.18); a1.set_title("one request, three routes through the stack\n(no network in the way: every millisecond is the stack itself)", fontsize=9.5); a1.legend(frameon=False, fontsize=8.5); a1.grid(axis="y", alpha=.25)
th = [r["threads"] for r in R["load"]]; rps = [r["req_per_s"] for r in R["load"]]
a2.plot(th, rps, "o-", color=TEAL, lw=2)
for t, v in zip(th, rps): a2.text(t, v + 60, "%d" % v, ha="center", color=TEAL, fontsize=8.5)
a2.set_xscale("log", base=2); a2.set_xticks(th); a2.set_xticklabels([str(t) for t in th]); a2.set_ylim(0, max(rps) * 1.25)
a2.set_xlabel("clients hammering at once"); a2.set_ylabel("requests served per second"); a2.set_title("the same server under 1, 4 and 16 concurrent clients", fontsize=9.5); a2.grid(alpha=.25)
a2.text(0.03, 0.08, "first run, with the default listen queue of 5:\n%d of 3 200 requests at 16 clients were refused.\nOne setting later: 0 errors, and %d of %d concurrent writes landed." % (1513, R["writes"]["landed"], R["writes"]["attempted"]), transform=a2.transAxes, color=RED, fontsize=7.8, va="bottom")
save(fig, "tech-stack-measurements.svg")
print("wrote 2 SVGs")

"""Archimedes' life and afterlife: the works above the line, the wars and the finders below it.

Run:  python3 archimedes-timeline.py   -> archimedes-timeline.svg
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"
# left panel: his life (BC, so negative years); right panel: the afterlife
fig, (ax, bx) = plt.subplots(1, 2, figsize=(13, 4.6), gridspec_kw=dict(width_ratios=[1.6, 1])); fig.patch.set_alpha(0)
for a in (ax, bx):
    a.set_facecolor("none"); a.set_yticks([]); a.tick_params(colors=G)
    for s in a.spines.values(): s.set_color(G)
    for k in ("left", "right", "top"): a.spines[k].set_visible(False)
    a.axhline(0, color=G, lw=1.5)
work = [(-287, "c. 287\nborn in\nSyracuse"), (-260, "c. 260s\nAlexandria;\nthe screw"), (-250, "c. 250\nMeasurement of\nthe Circle: 3 10/71\n< π < 3 1/7"), (-240, "c. 240\nSphere and\nCylinder: 2/3"), (-230, "c. 230\nThe Method,\nto Eratosthenes"), (-225, "c. 225\nOn Floating\nBodies")]
feud = [(-216, "216: Hiero II dies;\nSyracuse turns\nto Carthage"), (-214, "214: Marcellus\nbesieges; the claw,\nthe catapults"), (-212, "212: the city falls;\nthe soldier")]
ax.set_xlim(-292, -200); ax.set_ylim(-3.4, 3.6)
for i, (x, lab) in enumerate(work):
    h = 1.0 if i % 2 == 0 else 2.1
    ax.plot([x, x], [0, h], color="#2563eb", lw=1.2); ax.scatter([x], [0], s=40, color="#2563eb", zorder=3)
    ax.text(x, h + 0.1, lab, ha="center", va="bottom", fontsize=8, color="#2563eb")
for i, (x, lab) in enumerate(feud):
    h = [-0.5, -1.55, -2.6][i]
    ax.plot([x, x], [0, h], color="#dc2626", lw=1.2); ax.text(x, h - 0.08, lab, ha="center", va="top", fontsize=8, color="#dc2626")
ax.set_xticks([-280, -260, -240, -220]); ax.set_xticklabels(["280 BC", "260 BC", "240 BC", "220 BC"])
ax.set_title("the life: what he wrote, and the war that ended it", color=G, fontsize=10)
after = [(1586, "1586\nGalileo's\nBilancetta"), (1906, "1906\nHeiberg reads\nthe Palimpsest"), (1998, "1998\nsold for\n$2 million"), (2008, "2008\nimaged: the\nMethod recovered")]
bx.set_xlim(1540, 2080); bx.set_ylim(-3.4, 3.6)
bx.text(1548, -1.2, "75 BC: Cicero finds the tomb\n(sixteen centuries off this axis to the left)", fontsize=8, color="#f59e0b", va="top")
for i, (x, lab) in enumerate(after):
    h = [1.0, 2.1, 1.0, 2.6][i]
    bx.plot([x, x], [0, h], color="#f59e0b", lw=1.2); bx.scatter([x], [0], s=40, color="#f59e0b", zorder=3)
    bx.text(x, h + 0.1, lab, ha="center", va="bottom", fontsize=8, color="#f59e0b")
bx.set_xticks([1600, 1700, 1800, 1900, 2000])
bx.set_title("the afterlife: found, lost, found again", color=G, fontsize=10)
fig.tight_layout(); fig.savefig("archimedes-timeline.svg", transparent=True); print("wrote archimedes-timeline.svg")

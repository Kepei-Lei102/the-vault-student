"""heap-figures.py — the process's memory map from the C lab, and fragmentation from the Python lab.

Reads heap-lab-c.txt (the saved output of heap-lab.c) and heap-lab.json (from heap-lab.py).
Writes heap-process-layout.svg and heap-fragmentation.svg beside the card.
"""
import json, os, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
TXT, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"font.size": 10, "text.color": TXT, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT,
                     "axes.edgecolor": TXT, "svg.fonttype": "none", "font.family": "sans-serif"})

def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight"); plt.close(fig)
    s = open(path).read()
    for _ in range(2): s = re.sub(r'<svg([^>]*?)\s(width|height)="[^"]*"', r'<svg\1', s, count=1)
    open(path, "w").write(s.replace("<svg", '<svg width="100%"', 1))

C = open(os.path.join(HERE, "heap-lab-c.txt")).read()
addr = {k: int(v, 16) for k, v in re.findall(r"^\s+(code|data|heap|stack)\s+\([^)]*\)\s+(0x[0-9a-f]+)", C, re.M)[:1]}
rows = re.findall(r"^\s+(code|data|heap|stack)\s+\(([^)]*)\)\s+(0x[0-9a-f]+)", C, re.M)
depth3 = int(re.search(r"local at depth 3\s+(0x[0-9a-f]+)", C).group(1), 16)
t = re.search(r"stack ([\d.]+) ns\s+64 bytes on the heap \(\d+ live at once\) ([\d.]+) ns\s+1 MB on the heap (\d+) ns", C)
t_stack, t_heap, t_big = float(t.group(1)), float(t.group(2)), float(t.group(3))
leak = re.search(r"resident memory (\d+) MB -> (\d+) MB", C)
J = json.load(open(os.path.join(HERE, "heap-lab.json")))

# ───────────── figure 1: the process's memory, low addresses at the bottom ─────────────
fig, ax = plt.subplots(figsize=(11, 5.6)); ax.set_xlim(0, 11); ax.set_ylim(0, 5.6); ax.axis("off")
regions = [  # (y, h, label, colour, note)
    (0.4, 0.55, "code (text)", BLUE, "main at %s: the instructions, read-only" % next(a for k, n, a in rows if k == "code")),
    (1.05, 0.45, "data", TEAL, "a_global at %s: globals, sized at compile time" % next(a for k, n, a in rows if k == "data")),
    (1.6, 1.3, "heap (grows up)", GREEN, "malloc(100) at %s, the next at +112 bytes;\nsized at run time, freed by hand or by a collector" % next(a for k, n, a in rows if k == "heap")),
    (3.0, 0.9, "(unused: the gap they grow into)", TXT, "a 100 KB block landed far away at %s:\nlarge blocks are mapped straight from the OS" % [a for k, n, a in rows if k == "heap"][2]),
    (4.0, 1.2, "stack (grows down)", PURPLE, "a_local at %s; three calls deeper, %s:\nlocals, arguments and return addresses, freed on return" % (next(a for k, n, a in rows if k == "stack"), hex(depth3))),
]
for y, h, lab, col, note in regions:
    ax.add_patch(Rectangle((0.6, y), 3.2, h, fc=col, alpha=0.18 if col != TXT else 0.06, ec=col, lw=1.3, ls="-" if col != TXT else "--"))
    ax.text(2.2, y + h / 2, lab, ha="center", va="center", color=col, fontsize=10, fontweight="bold")
    ax.text(4.1, y + h / 2, note, ha="left", va="center", color=TXT, fontsize=8.2)
ax.annotate("", xy=(0.35, 5.35), xytext=(0.35, 0.3), arrowprops=dict(arrowstyle="->", color=TXT, lw=0.9))
ax.text(0.2, 2.9, "higher addresses", rotation=90, ha="center", va="center", color=TXT, fontsize=8)
ax.add_patch(FancyArrowPatch((2.2, 2.95), (2.2, 3.35), arrowstyle="->", color=GREEN, lw=1.5, mutation_scale=14))
ax.add_patch(FancyArrowPatch((2.2, 3.95), (2.2, 3.55), arrowstyle="->", color=PURPLE, lw=1.5, mutation_scale=14))
ax.text(5.5, 5.35, "One process's memory, measured by heap-lab.c on this machine (addresses differ each run; the order and directions do not)", ha="center", color=TXT, fontsize=9)
ax.text(5.5, 0.12, "Cost of one 64-byte allocation and its release: stack %.1f ns · heap %.0f ns · a 1 MB block from the OS %d ns.  Forget to free 200 000 blocks: %s MB to %s MB." % (t_stack, t_heap, t_big, leak.group(1), leak.group(2)),
        ha="center", color=TXT, fontsize=8.4)
save(fig, "heap-process-layout.svg")

# ───────────── figure 2: fragmentation in the toy allocator ─────────────
P = J["allocator"]["pictures"]; S = J["allocator"]
fig, ax = plt.subplots(figsize=(11, 3.6)); ax.set_xlim(0, 11); ax.set_ylim(0, 3.6); ax.axis("off")
steps = [("32 blocks allocated", P["full"], "free %d B" % (4096 - 32 * 124 - 4)),
         ("free every other block", P["fragmented"], "free %d B, largest %d: malloc(400) %s" % (S["after_alternate_free"]["free_bytes"], S["after_alternate_free"]["largest_free"], "ok" if S["malloc_400_ok"] else "FAILS")),
         ("free the rest, no coalescing", P["all_freed_uncoalesced"], "free %d B, largest %d: malloc(400) %s" % (S["after_all_free"]["free_bytes"], S["after_all_free"]["largest_free"], "ok" if S["malloc_400_ok_after_all_free"] else "FAILS")),
         ("coalesce neighbours", P["coalesced"], "%d merges, largest %d: malloc(400) %s" % (S["merged_blocks"], S["after_coalesce"]["largest_free"], "ok" if S["malloc_400_ok_after_coalesce"] else "FAILS"))]
for i, (lab, pic, note) in enumerate(steps):
    y = 3.0 - i * 0.78
    ax.text(0.1, y + 0.18, lab, ha="left", va="center", color=TXT, fontsize=8.8)
    x0, w = 3.0, 4.6 / len(pic)
    for j, ch in enumerate(pic):
        ax.add_patch(Rectangle((x0 + j * w, y), w, 0.36, fc=(RED if ch == "#" else GREEN), alpha=0.55 if ch == "#" else 0.35, ec="none"))
    ax.text(7.75, y + 0.18, note, ha="left", va="center", color=(RED if "FAILS" in note else TXT), fontsize=8.4)
ax.text(5.5, 0.18, "A 4096-byte arena drawn as 64 cells (red used, green free). Total free space never explains whether a request succeeds; the largest hole does.", ha="center", color=TXT, fontsize=8.6)
save(fig, "heap-fragmentation.svg")
print("wrote 2 SVGs")

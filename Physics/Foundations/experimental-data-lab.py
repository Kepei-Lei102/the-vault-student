"""Recording and Analysing Experimental Data — the numbers behind the rules, and the four figures.

Each rule a practical paper marks (half a division, view at right angles, fill the grid, big triangle,
ignore the anomaly, the 10 % test) is a rule because it changes the answer.  This script measures by how much.

1. half_division()  — rounding error when a scale is read to a whole division, a half, a tenth.
2. parallax()       — how far a reading moves when the eye is off to one side.
3. spring()         — real data (Cambridge 0625, June 2024 Paper 62, Q1): best-fit gradient, intercept,
                      k2 = 1/G, and the 10 % comparison with k1 = 25.0 N/m from the oscillation method.
4. triangle()       — the same line read with a small gradient triangle and with a large one, 20 000
                      times each, with an honest half-square reading error: why "at least half the line".
5. anomaly()        — one wrong reading in a set of repeats, and one wrong point on a graph.
6. choose_scale()   — the 1-2-5 rule: pick a scale that fills more than half the grid.

Run:  python3 experimental-data-lab.py      (numpy + matplotlib; writes four SVGs beside this script)
"""
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": GREY, "axes.labelcolor": GREY, "axes.edgecolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "font.size": 11, "svg.fonttype": "none", "font.family": "DejaVu Sans"})
rng = np.random.default_rng(62)
M = np.array([100, 200, 300, 400, 500.0])          # mass / g
L = np.array([6.1, 10.0, 14.3, 18.3, 22.4])        # stretched length / cm  (22.4 is the value read from the scale drawing)


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)
    s = open(path).read()
    s = re.sub(r'<svg([^>]*?) width="[^"]*" height="[^"]*"', r'<svg\1 width="100%"', s, count=1)
    open(path, "w").write(s)
    print("  wrote", name)


def half_division(n=1_000_000):
    true = rng.uniform(0, 100, n)                   # in scale divisions
    for step, name in ((1.0, "nearest whole division"), (0.5, "nearest half division"), (0.1, "nearest tenth (not reliably possible by eye)")):
        err = np.round(true / step) * step - true
        print(f"  {name:46s} typical error {err.std():.3f} of a division, worst {np.abs(err).max():.2f}")
    print("  a half-division is the finest step the eye judges reliably: it halves the error of the lazy reading")


def parallax():
    for what, gap_mm in (("pointer 2 mm in front of a meter scale", 2.0), ("liquid thread 4 mm behind the front of a thermometer", 4.0), ("ruler 8 mm thick lying on a drawing", 8.0)):
        for sideways_cm in (5, 15):
            shift = gap_mm * sideways_cm / 30.0     # eye 30 cm away
            print(f"  {what:54s} eye {sideways_cm:2d} cm off line: reading moves {shift:4.2f} mm")
    print("  cure: line of sight at right angles to the scale; or put the scale in contact with the object")


def fit(x, y):
    G, c = np.polyfit(x, y, 1)
    return G, c


def spring():
    G, c = fit(M, L)
    print(f"  best-fit line: l = {G:.4f} m + {c:.2f}   (gradient in cm per g; intercept {c:.1f} cm is the UNSTRETCHED length of the spring)")
    print(f"  largest distance of a point from the line: {np.abs(L - (G*M + c)).max():.2f} cm")
    k2 = 1 / G
    print(f"  k2 = 1/G = {k2:.1f}   (mark scheme accepts 23.5 to 26.4)")
    k1 = 25.0
    print(f"  k1 = 25.0 from the oscillations.  Difference {abs(k1-k2):.2f}, which is {100*abs(k1-k2)/k1:.1f} % of k1: well inside 10 %, so they agree")
    G0 = (M * L).sum() / (M * M).sum()
    print(f"  forcing the line through the origin would give G = {G0:.4f} and k2 = {1/G0:.1f}: {100*abs(k1-1/G0)/k1:.0f} % out. "
          "Do not assume (0, 0) lies on the line.")
    return G, c


def triangle(G, c, trials=20_000):
    read = 0.1                                       # half a small square on the l axis, in cm, as a standard deviation of reading
    out = {}
    for name, (x1, x2) in (("small triangle, between two neighbouring points", (200.0, 300.0)), ("large triangle, over most of the line", (50.0, 500.0))):
        y1 = G * x1 + c + rng.normal(0, read, trials); y2 = G * x2 + c + rng.normal(0, read, trials)
        g = (y2 - y1) / (x2 - x1)
        out[name] = g
        print(f"  {name:50s} G = {g.mean():.4f} ± {g.std():.4f}  ({100*g.std()/g.mean():4.1f} %)   k2 from {1/(g.mean()+g.std()):.1f} to {1/(g.mean()-g.std()):.1f}")
    print("  the same reading error is divided by a base 4.5 times longer: the large triangle is 4.5 times better")
    return out


def anomaly():
    I = np.array([0.85, 0.58, 0.90, 0.80])          # Cambridge 0625, June 2026 Paper 63, Q3(d)
    print(f"  repeats {I}: mean with everything {I.mean():.2f} A;  with 0.58 set aside {np.delete(I, 1).mean():.2f} A")
    print("  0.58 is 0.85 with its digits swapped, the mark scheme's first suggestion: check, repeat, then leave it out and say so")
    Lbad = L.copy(); Lbad[3] = 15.3                  # the 400 g length misread by 3 cm
    Gb, cb = fit(M, Lbad); G, c = fit(M, L)
    Gi, ci = fit(np.delete(M, 3), np.delete(Lbad, 3))
    print(f"  the 400 g point misread by 3 cm: true gradient {G:.4f}; {Gb:.4f} if the line is dragged towards it ({100*(Gb-G)/G:+.0f} %); {Gi:.4f} if it is circled and ignored")


def choose_scale(lo, hi, squares, data_lo=None):
    """2 cm (one large square) to represent 1, 2 or 5 x 10^n; smallest such step that fits the data on the grid."""
    span = hi - lo
    for p in range(-4, 6):
        for mant in (1, 2, 5):
            step = mant * 10.0**p
            if step * squares >= span:
                return step, (hi - (lo if data_lo is None else data_lo)) / (step * squares)


def scales_demo():
    for name, lo, hi, squares, dlo in (("m / g, axis from 0", 0, 500, 6, 100), ("l / cm, axis from 0", 0, 22.4, 5, 6.1), ("temperatures 18.5 to 29.0 °C, axis from 18", 18, 29, 6, 18.5), ("the same, axis from 0", 0, 29, 6, 18.5)):
        step, used = choose_scale(lo, hi, squares, dlo)
        print(f"  {name:44s} {squares} large squares: one square = {step:g}; the plotted points span {100*used:.0f} % of the axis")
    print("  never 3, 4, 7 or 9 per square: every plotted point would then need a division sum")


# ------------------------------------------------------------------ figures
def fig_reading():
    fig, axes = plt.subplots(2, 1, figsize=(10, 7.4), gridspec_kw={"height_ratios": [1, 1.15], "hspace": 0.2})
    ax = axes[0]; ax.set_xlim(0, 10); ax.set_ylim(0, 3.2); ax.axis("off")
    ax.add_patch(Rectangle((0.5, 1.2), 9, 0.9, fc=matplotlib.colors.to_rgba(AMBER, 0.12), ec=GREY))
    for k in range(0, 46):
        x = 0.7 + k * 0.19; big = k % 10 == 0; mid = k % 5 == 0
        ax.plot([x, x], [2.1, 2.1 - (0.42 if big else 0.3 if mid else 0.18)], color=GREY, lw=1)
        if big:
            ax.text(x, 1.38, f"{3 + k // 10}", ha="center", fontsize=10)
    ax.text(9.35, 1.38, "cm", fontsize=10)
    for k, col, lab, dy in ((17.0, GREEN, "on a mark: 4.70 cm", 0.0), (28.5, RED, "between marks: 5.85 cm, the nearest HALF division", 0.0)):
        x = 0.7 + k * 0.19
        ax.plot([x, x], [2.15, 2.75], color=col, lw=2)
        ax.text(x + (-0.1 if k < 20 else 0.1), 2.85, lab, ha="right" if k < 20 else "left", color=col, fontsize=10)
    ax.text(5, 0.55, "smallest division 1 mm, so every reading is written to 0.05 cm: 4.70, not 4.7", ha="center", fontsize=10.5)
    ax = axes[1]; ax.set_xlim(0, 10); ax.set_ylim(-0.3, 4.4); ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(Rectangle((1.0, 0.4), 0.35, 3.6, fc=matplotlib.colors.to_rgba(GREY, 0.2), ec=GREY)); ax.text(0.85, 2.2, "scale", ha="right", va="center", fontsize=9.5)
    for k in range(13):
        ax.plot([1.0, 1.35], [0.6 + 0.27 * k] * 2, color=GREY, lw=0.8)
    obj_y = 2.22
    ax.plot(2.3, obj_y, "o", color=BLUE, ms=9); ax.text(2.3, obj_y - 0.38, "pointer, a little way\nin front of the scale", ha="center", va="top", fontsize=9.5, color=BLUE)
    for (ex, ey), col, lab in (((8.2, obj_y), GREEN, "eye level with the pointer:\nline of sight at right angles to the scale.\nCorrect reading"), ((8.2, 4.0), RED, "eye too high: reads LOW"), ((8.2, 0.6), RED, "eye too low: reads HIGH")):
        ax.add_patch(Circle((ex, ey), 0.13, fc=col, ec=col))
        slope = (ey - obj_y) / (ex - 2.3); y_at_scale = obj_y - slope * (2.3 - 1.35)
        ax.plot([ex, 1.35], [ey, y_at_scale], color=col, lw=1.3, ls="-" if col == GREEN else "--")
        ax.text(ex + 0.25, ey, lab, va="center", fontsize=9.5, color=col)
    ax.text(5.0, -0.05, "parallax error: the further the pointer is from the scale, the bigger it gets", ha="center", fontsize=10)
    save(fig, "experimental-data-reading-scales.svg")


def draw_grid(ax, xmax, ymax, xstep, ystep):
    for x in np.arange(0, xmax + 1e-9, xstep / 5):
        ax.axvline(x, color=GREY, lw=0.3, alpha=0.45)
    for y in np.arange(0, ymax + 1e-9, ystep / 5):
        ax.axhline(y, color=GREY, lw=0.3, alpha=0.45)
    for x in np.arange(0, xmax + 1e-9, xstep):
        ax.axvline(x, color=GREY, lw=0.7, alpha=0.6)
    for y in np.arange(0, ymax + 1e-9, ystep):
        ax.axhline(y, color=GREY, lw=0.7, alpha=0.6)
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax)


def fig_good_bad(G, c):
    fig, axes = plt.subplots(2, 1, figsize=(10, 11.2), gridspec_kw={"hspace": 0.3})
    ax = axes[0]; draw_grid(ax, 2100, 90, 300, 15)
    ax.plot(M, L, "-o", color=RED, ms=9, lw=1.5)
    ax.set_xticks(np.arange(0, 2101, 300)); ax.set_yticks(np.arange(0, 91, 15)); ax.set_xlabel("mass"); ax.set_ylabel("length")
    ax.set_title("Five faults: each one costs a mark", color=RED, fontsize=12, loc="left")
    for xy, txt in (((620, 62), "1  the points use a small corner of the grid"), ((620, 52), "2  awkward scales: 300 and 15 to a square"),
                    ((620, 42), "3  no units on either axis"), ((620, 32), "4  blobs, not crosses: where exactly is the point?"), ((620, 22), "5  points joined dot to dot")):
        ax.text(*xy, txt, fontsize=10.5, color=RED)
    ax = axes[1]; draw_grid(ax, 600, 25, 100, 5)
    ax.plot(M, L, "x", color=BLUE, ms=9, mew=1.8)
    xx = np.array([0, 560.0]); ax.plot(xx, G * xx + c, color=GREEN, lw=1.4)
    x1, x2 = 50.0, 500.0; y1, y2 = G * x1 + c, G * x2 + c
    ax.plot([x1, x2, x2], [y1, y1, y2], color=AMBER, lw=1.4, ls="--")
    ax.text((x1 + x2) / 2, y1 - 1.3, f"Δm = {x2-x1:.0f} g", ha="center", color=AMBER, fontsize=10)
    ax.text(x2 + 8, (y1 + y2) / 2, f"Δl = {y2-y1:.1f} cm", color=AMBER, fontsize=10, va="center")
    ax.plot(0, c, "o", color=PURPLE, ms=7); ax.annotate(f"intercept {c:.1f} cm:\nthe unstretched length", (0, c), xytext=(14, 96), textcoords="offset points", fontsize=10, color=PURPLE,
                                                          arrowprops=dict(arrowstyle="-", color=PURPLE, lw=0.7))
    ax.set_xticks(np.arange(0, 601, 100)); ax.set_yticks(np.arange(0, 26, 5)); ax.set_xlabel("m / g"); ax.set_ylabel("l / cm")
    ax.set_title(f"The same data, done properly: gradient = {y2-y1:.1f} ÷ {x2-x1:.0f} = {(y2-y1)/(x2-x1):.4f} cm/g", color=GREEN, fontsize=12, loc="left")
    ax.text(20, 20.6, "thin straight line, points balanced either side;\ntriangle over more than half the line, and drawn in", fontsize=10)
    for a in axes:
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    save(fig, "experimental-data-good-and-bad-graph.svg")


def fig_triangle(out):
    fig, ax = plt.subplots(figsize=(10, 5.2))
    bins = np.linspace(0.036, 0.046, 80)
    for (name, g), col in zip(out.items(), (RED, GREEN)):
        ax.hist(g, bins=bins, color=matplotlib.colors.to_rgba(col, 0.35), edgecolor=col, lw=0.5, label=f"{name}: ± {100*g.std()/g.mean():.1f} %")
    ax.set_xlabel("gradient obtained / cm per g"); ax.set_ylabel("number of attempts out of 20 000"); ax.set_yticks([])
    ax.set_title("Same line, same care in reading: only the size of the triangle differs", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY, loc="upper right")
    save(fig, "experimental-data-triangle-size.svg")


def fig_anomaly(G, c):
    Lbad = L.copy(); Lbad[3] = 15.3
    Gb, cb = fit(M, Lbad); Gi, ci = fit(np.delete(M, 3), np.delete(Lbad, 3))
    fig, ax = plt.subplots(figsize=(10, 5.8)); draw_grid(ax, 600, 25, 100, 5)
    ax.plot(np.delete(M, 3), np.delete(Lbad, 3), "x", color=BLUE, ms=9, mew=1.8)
    ax.plot(M[3], Lbad[3], "x", color=RED, ms=9, mew=1.8)
    ax.plot(M[3], Lbad[3], "o", mfc="none", mec=RED, ms=20)
    ax.annotate("anomalous: circle it, check it, repeat it,\nleave it out of the line and SAY so", (M[3], Lbad[3]), xytext=(25, -42), textcoords="offset points", fontsize=10, color=RED)
    xx = np.array([0, 560.0])
    ax.plot(xx, Gi * xx + ci, color=GREEN, lw=1.5, label=f"line ignoring it: gradient {Gi:.4f}")
    ax.plot(xx, Gb * xx + cb, color=RED, lw=1.2, ls="--", label=f"line dragged towards it: gradient {Gb:.4f}")
    ax.set_xticks(np.arange(0, 601, 100)); ax.set_yticks(np.arange(0, 26, 5)); ax.set_xlabel("m / g"); ax.set_ylabel("l / cm")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY, loc="upper left")
    save(fig, "experimental-data-anomaly.svg")


if __name__ == "__main__":
    print("1. reading to half a division"); half_division()
    print("\n2. parallax"); parallax()
    print("\n3. the spring graph"); G, c = spring()
    print("\n4. the size of the gradient triangle"); out = triangle(G, c)
    print("\n5. anomalous results"); anomaly()
    print("\n6. choosing scales"); scales_demo()
    print("\nfigures"); fig_reading(); fig_good_bad(G, c); fig_triangle(out); fig_anomaly(G, c)

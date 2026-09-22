"""Figures for How a Chip Is Made.md — run: python3 chip-fabrication-figures.py"""
import re, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

TXT = "#888"; BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": TXT, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT, "axes.edgecolor": TXT, "font.size": 10, "svg.fonttype": "none"})
def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name).read(); m = re.search(r"<svg[^>]*>", s)
    tag = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)).replace("<svg", '<svg width="100%"', 1)
    open(name, "w").write(s[:m.start()] + tag + s[m.end():]); plt.close(fig)

# ── 1. a CMOS inverter in cross-section, the thing the eighty stencils build ──────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 4.6)); ax.set_xlim(0, 12); ax.set_ylim(0, 5.2); ax.axis("off")
ax.add_patch(Rectangle((0.3, 0.3), 11.4, 1.6, fc=TXT, alpha=0.12, ec="none")); ax.text(6, 0.55, "p-type silicon substrate (the wafer)", ha="center", color=TXT, fontsize=9)
ax.add_patch(Rectangle((6.3, 0.9), 5.0, 1.0, fc=BLUE, alpha=0.15, ec=BLUE, lw=1)); ax.text(8.8, 1.05, "n-well (the p-transistor lives in it)", ha="center", color=BLUE, fontsize=8.5)
for x0, col, lab in ((1.0, GREEN, "n+"), (3.6, GREEN, "n+"), (6.9, RED, "p+"), (9.5, RED, "p+")):
    ax.add_patch(Rectangle((x0, 1.55), 1.4, 0.35, fc=col, alpha=0.35, ec=col, lw=1)); ax.text(x0 + 0.7, 1.72, lab, ha="center", va="center", color=col, fontsize=9)
for xg, lab in ((2.4, "NMOS gate"), (8.3, "PMOS gate")):
    ax.add_patch(Rectangle((xg, 1.9), 1.2, 0.12, fc=AMBER, alpha=0.8, ec="none")); ax.text(xg + 0.6, 1.83, "oxide, ~1 nm", ha="center", va="top", color=AMBER, fontsize=7.5)
    ax.add_patch(Rectangle((xg, 2.02), 1.2, 0.55, fc=PURPLE, alpha=0.5, ec=PURPLE, lw=1)); ax.text(xg + 0.6, 2.3, lab, ha="center", va="center", color="#fff", fontsize=8)
ax.add_patch(Rectangle((0.3, 1.9), 11.4, 1.5, fc=TEAL, alpha=0.06, ec="none")); ax.text(11.5, 3.2, "insulator (SiO₂)", ha="right", color=TEAL, fontsize=8)
for xc in (1.7, 4.3, 7.6, 10.2, 3.0, 8.9):
    ax.add_patch(Rectangle((xc - 0.12, 1.9 if xc not in (3.0, 8.9) else 2.57), 0.24, (1.5 if xc not in (3.0, 8.9) else 0.83), fc="#999", alpha=0.7, ec="none"))
ax.text(3.0, 3.45, "contacts (tungsten)", ha="center", color=TXT, fontsize=8)
for x0, w, col, lab in ((1.4, 0.6, RED, "GND"), (3.9, 6.0, GREEN, "output"), (9.9, 0.6, BLUE, "VDD"), (2.5, 0.0, PURPLE, "")):
    if w: ax.add_patch(Rectangle((x0, 3.4), w, 0.4, fc=col, alpha=0.45, ec=col, lw=1)); ax.text(x0 + w / 2, 3.6, lab, ha="center", va="center", color="#fff", fontsize=8)
ax.add_patch(Rectangle((2.7, 3.4), 6.5, 0.4, fc=PURPLE, alpha=0.25, ec=PURPLE, lw=1, ls="--")); ax.text(5.9, 4.0, "metal 1: the input wire joins both gates; metal 2 to metal 15 stack above this, each layer coarser", ha="center", color=TXT, fontsize=8.5)
ax.text(6, 4.75, "A CMOS inverter, front to back: two transistors of opposite type, wired so that exactly one conducts. Every layer here is one or more lithography stencils.", ha="center", color=TXT, fontsize=9.5)
ax.annotate("", xy=(11.5, 1.9), xytext=(11.5, 3.4), arrowprops=dict(arrowstyle="<->", color=TXT, lw=0.8)); ax.text(11.6, 2.65, "~1 μm", color=TXT, fontsize=7.5, rotation=90, va="center")
save(fig, "chip-fabrication-cross-section.svg")

# ── 2. yield against die area, and what it does to the cost of a chip ─────────────────────────────────────────
def dies(d_mm, a): r = d_mm / 2 - 3; return np.pi * r**2 / a - np.pi * 2 * r / np.sqrt(2 * a)
A = np.linspace(20, 858, 300)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2))
for D, col in ((0.05, GREEN), (0.1, AMBER), (0.2, RED)):
    a1.plot(A, np.exp(-D * A / 100) * 100, color=col, lw=2, label=f"D = {D} defects per cm²")
a1.set_xlabel("die area / mm²"); a1.set_ylabel("yield / %"); a1.set_title("Y = e^(−D·A): every extra square millimetre is another chance of a killer defect", fontsize=9.5)
a1.legend(frameon=False, fontsize=9); a1.grid(alpha=.25); a1.set_ylim(0, 100)
for sp in ("top", "right"): a1.spines[sp].set_visible(False)
cost = 17000 / (dies(300, A) * np.exp(-0.1 * A / 100))
a2.plot(A, cost, color=PURPLE, lw=2); a2.set_yscale("log")
for a, lab in ((100, "phone SoC"), (150, "laptop chip"), (600, "GPU")):
    c = 17000 / (dies(300, a) * math.exp(-0.1 * a / 100)); a2.plot(a, c, "o", color=PURPLE); a2.text(a + 15, c, f"{lab}: ${c:.0f}", color=PURPLE, fontsize=9, va="center")
a2.set_xlabel("die area / mm²"); a2.set_ylabel("cost per good die / $ (log)"); a2.set_title("a $17 000 wafer, D = 0.1: cost rises faster than area", fontsize=9.5); a2.grid(alpha=.25, which="both")
for sp in ("top", "right"): a2.spines[sp].set_visible(False)
save(fig, "chip-fabrication-yield.svg")

# ── 3. fifty years of transistor density ───────────────────────────────────────────────────────────────────────
chips = [("4004", 1971, 2250, 12), ("8086", 1978, 29000, 33), ("386", 1985, 275000, 104), ("Pentium", 1993, 3.1e6, 294), ("Pentium 4", 2000, 42e6, 217),
         ("Core 2 Duo", 2006, 291e6, 143), ("A7", 2013, 1e9, 102), ("A12", 2018, 6.9e9, 83), ("M1 Max", 2021, 57e9, 432), ("M2 Ultra", 2023, 134e9, 1020)]
fig, ax = plt.subplots(figsize=(9, 4.2))
yrs = [c[1] for c in chips]; dens = [c[2] / c[3] for c in chips]
ax.plot(yrs, dens, "o-", color=BLUE, lw=1.5)
for n, y, cnt, area in chips: ax.text(y + (-1.6 if n == "M1 Max" else 1.2 if n == "M2 Ultra" else 0), cnt / area * (0.55 if n == "M2 Ultra" else 1.6), n, color=BLUE, fontsize=8, ha="center")
ax.set_yscale("log"); ax.set_xlabel("year"); ax.set_ylabel("transistors per mm² (log)"); ax.set_title("Transistor density, 1971 to 2023: a straight line on a log axis is a constant doubling time", fontsize=9.5)
ax.grid(alpha=.25, which="both")
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
save(fig, "chip-fabrication-density.svg")
print("wrote 3 SVGs")

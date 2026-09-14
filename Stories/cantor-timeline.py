"""Cantor's life as two tracks: the theorems above the line, the hospital below it.

Run:  python3 cantor-timeline.py   -> cantor-timeline.svg
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"
work = [(1874, "1874\nreals are\nuncountable"), (1877, "1877\nsquare = line\n'I see it but\nI do not believe it'"), (1883, "1883\nGrundlagen:\ntransfinite\nnumbers"), (1891, "1891\nthe diagonal\nargument"), (1895, "1895–97\nBeiträge: the\nalephs"), (1900, "1900\nHilbert's\nProblem 1 = CH")]
feud = [(1878, "Kronecker delays\nthe 1878 paper"), (1884, "Mittag-Leffler\nasks him to\nwithdraw, '85"), (1886, "'God made\nthe integers'"), (1891, "Kronecker\ndies")]
hosp = [(1884, 1884.4), (1899, 1899.5), (1902.8, 1903.4), (1904.7, 1905.2), (1907.5, 1908.3), (1911.7, 1912.3), (1917.4, 1918.0)]
fig, ax = plt.subplots(figsize=(12, 4.6)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.axhline(0, color=G, lw=1.5); ax.set_xlim(1870, 1920); ax.set_ylim(-2.4, 3.6)
for i, (x, lab) in enumerate(work):
    h = 1.0 if i % 2 == 0 else 1.9
    ax.plot([x, x], [0, h], color="#2563eb", lw=1.2); ax.scatter([x], [0], s=40, color="#2563eb", zorder=3)
    ax.text(x, h + 0.1, lab, ha="center", va="bottom", fontsize=8, color="#2563eb")
for i, (x, lab) in enumerate(feud):
    h = -1.05 if i % 2 == 0 else -0.55
    ax.plot([x, x], [0, h], color="#f59e0b", lw=1.2); ax.text(x, h - 0.08, lab, ha="center", va="top", fontsize=8, color="#f59e0b")
for a, b in hosp:
    ax.fill_between([a, b], -2.3, -1.75, color="#dc2626", alpha=0.35, linewidth=0)
ax.text(1870.5, -2.05, "in the Halle Nervenklinik", va="center", fontsize=8, color="#dc2626")
ax.text(1898.6, -1.5, "Dec 1899: son Rudolf dies, 13", fontsize=8, color=G, ha="right")
ax.text(1905.4, -1.5, "Aug 1904: König 'refutes' CH", fontsize=8, color=G, ha="left")
ax.text(1918.1, -2.05, "6 Jan 1918", fontsize=8, color="#dc2626", va="center")
ax.set_yticks([]); ax.tick_params(colors=G); ax.set_xlabel("year", color=G)
for s in ax.spines.values(): s.set_color(G)
ax.spines["left"].set_visible(False); ax.spines["right"].set_visible(False); ax.spines["top"].set_visible(False)
ax.set_title("above the line, the mathematics; below it, the feud and the clinic", color=G, fontsize=10)
fig.tight_layout(); fig.savefig("cantor-timeline.svg", transparent=True); print("wrote cantor-timeline.svg")

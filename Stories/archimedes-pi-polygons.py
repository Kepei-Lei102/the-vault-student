"""Inscribed and circumscribed polygons closing on the circle.  -> archimedes-pi-polygons.svg"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"
fig, axs = plt.subplots(1, 4, figsize=(13, 3.6)); fig.patch.set_alpha(0)
for ax, n in zip(axs, (6, 12, 24, 96)):
    ax.set_facecolor("none"); ax.set_aspect("equal"); ax.axis("off")
    t = np.linspace(0, 2 * np.pi, 400); ax.plot(np.cos(t), np.sin(t), color=G, lw=1)
    a = np.linspace(0, 2 * np.pi, n + 1)
    ax.plot(np.cos(a), np.sin(a), color="#2563eb", lw=1.4)                       # inscribed
    r = 1 / np.cos(np.pi / n); a2 = a + np.pi / n
    ax.plot(r * np.cos(a2), r * np.sin(a2), color="#dc2626", lw=1.4)             # circumscribed
    lo, hi = n * np.sin(np.pi / n), n * np.tan(np.pi / n)
    ax.set_title(f"{n} sides\n{lo:.4f} < π < {hi:.4f}", color=G, fontsize=10)
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25)
fig.text(0.5, 0.02, "blue inside, red outside; the circle's circumference is trapped between the two perimeters, and the trap closes as the sides double", ha="center", color=G, fontsize=9)
fig.tight_layout(rect=(0, 0.05, 1, 1)); fig.savefig("archimedes-pi-polygons.svg", transparent=True); print("wrote archimedes-pi-polygons.svg")

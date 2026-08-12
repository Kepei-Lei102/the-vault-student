"""Flash charge-level distributions: SLC's two fat levels vs TLC's eight
crowded, Gray-labelled levels. Regenerates secondary-storage-flash-levels.png."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GRAY = "#888888"
BLUE = "#2563eb"
AMBER = "#f59e0b"
RED = "#dc2626"

plt.rcParams.update({
    "text.color": GRAY, "axes.edgecolor": GRAY, "axes.labelcolor": GRAY,
    "xtick.color": GRAY, "ytick.color": GRAY, "font.size": 12,
    "font.family": "Helvetica",
})

def bump(ax, mu, sigma, color, alpha=0.25):
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 200)
    y = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    ax.fill_between(x, y, color=color, alpha=alpha, lw=0)
    ax.plot(x, y, color=color, lw=1.8)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 5.6))

# ---- SLC ----
for mu, label in [(2.0, "1"), (8.0, "0")]:
    bump(ax1, mu, 0.75, BLUE)
    ax1.text(mu, 1.08, label, ha="center", color=BLUE, fontsize=15, fontweight="bold")
ax1.axvline(5.0, ymax=0.75, color=AMBER, lw=1.6, ls="--")
ax1.text(5.0, 1.18, "one decision boundary", ha="center", color=AMBER, fontsize=11)
ax1.annotate("", xy=(6.9, 0.5), xytext=(3.1, 0.5),
             arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.2))
ax1.text(4.82, 0.58, "a fat, safe gap", ha="right", color=GRAY, fontsize=10.5)
ax1.set_title("SLC — 1 bit per cell, two charge levels", color=GRAY, fontsize=13, loc="left")

# ---- TLC ----
gray_labels = ["111", "110", "100", "101", "001", "000", "010", "011"]
mus = np.linspace(0.8, 9.2, 8)
for mu, label in zip(mus, gray_labels):
    bump(ax2, mu, 0.30, BLUE)
    ax2.text(mu, 1.08, label, ha="center", color=BLUE, fontsize=10.5, fontweight="bold")
for b in (mus[:-1] + mus[1:]) / 2:
    ax2.axvline(b, ymax=0.72, color=AMBER, lw=1.2, ls="--", alpha=0.8)

# drift: tail of level "101" leaking across the boundary toward "001"
mu_d = mus[3]
xd = np.linspace(mu_d, mu_d + 1.35, 100)
yd = np.exp(-((xd - mu_d) ** 2) / (2 * 0.46 ** 2))
ax2.fill_between(xd, yd, color=RED, alpha=0.3, lw=0)
ax2.plot(xd, yd, color=RED, lw=1.6, ls=":")
ax2.annotate("charge drifts across one line:\nGray order flips ONE bit (101 to 001)",
             xy=(mu_d + 0.78, 0.30), xytext=(6.3, 1.24), color=RED, fontsize=10.5,
             arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
ax2.set_title("TLC — 3 bits per cell, eight levels in the same window, labels in Gray-code order",
              color=GRAY, fontsize=13, loc="left")

for ax in (ax1, ax2):
    ax.set_xlim(-1.5, 11.5)
    ax.set_ylim(0, 1.42)
    ax.set_yticks([])
    ax.set_xticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRAY)
ax2.set_xlabel("stored charge on the floating gate (threshold voltage)", color=GRAY, fontsize=11.5)

fig.tight_layout(h_pad=2.0)
out = "/Users/kepeilei/Desktop/The_Vault/CS/Hardware Systems/secondary-storage-flash-levels.png"
fig.savefig(out, dpi=200, transparent=True)
print("saved", out)

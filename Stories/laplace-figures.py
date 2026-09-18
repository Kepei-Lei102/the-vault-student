"""
laplace-figures.py — figures for [[Stories/Laplace and Napoleon]].

  laplace-great-inequality.svg  — the Jupiter/Saturn mean-longitude residuals from
                                  laplace-great-inequality.py (run that first; it saves
                                  the series), with one century boxed to show what Halley
                                  saw: a straight-line drift that is really one flank of a
                                  ~900-year wave.
  laplace-regimes-timeline.svg  — Laplace's life (1749–1827) laid across the regimes he
                                  served: Louis XV, Louis XVI, the Revolution, the
                                  Directory, the Consulate, the Empire, the Restoration.

Vault style: every text fill #888, no background rect, width="100%" + viewBox.
Verify light + dark with cairosvg before delivery.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GREY = "#888888"
BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
S = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad"

def style(ax):
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelcolor=GREY)
    ax.xaxis.label.set_color(GREY); ax.yaxis.label.set_color(GREY); ax.title.set_color(GREY)
    ax.set_facecolor("none")

def save(fig, name):
    fig.patch.set_alpha(0)
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    s = open(name).read()
    s = s.replace('<svg ', '<svg width="100%" ', 1)
    import re
    s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1)
    open(name, "w").write(s)
    print("wrote", name)

# ---------------------------------------------------------------- great inequality
ts, rj, rs = np.load(f"{S}/gi.npy")
sel = ts <= 3000
fig, axes = plt.subplots(2, 1, figsize=(9, 5.2), sharex=True)
for ax, res, col, name in ((axes[0], rj, AMBER, "Jupiter"), (axes[1], rs, TEAL, "Saturn")):
    style(ax)
    ax.plot(ts[sel], res[sel], color=col, lw=1.4)
    ax.axhline(0, color=GREY, lw=0.6, ls=":")
    ax.set_ylabel(f"{name}\nmean-longitude residual (′)")
    # Halley's century: 1600–1700 sits on one flank; box years 600–700 of the run
    ax.axvspan(600, 700, color=RED, alpha=0.12)
axes[0].set_title("Halley's anomaly, reproduced from Newton's law alone — and Laplace's answer: it is a wave, not a drift", fontsize=11)
axes[1].set_xlabel("years into the simulation (Sun + Jupiter + Saturn, velocity-Verlet)")
axes[0].set_ylim(-36, 36); axes[1].set_ylim(-95, 95)
axes[0].text(650, 31, "one century: looks like a steady drift", color=RED, fontsize=8.5, ha="center", va="center")
fig.text(0.5, -0.02, "period ≈ 900 yr, set by 2n_J − 5n_S ≈ 0 (five Jupiter years ≈ two Saturn years); amplitudes ≈ 21′ and 49′ — Laplace, 1785",
         color=GREY, fontsize=9, ha="center")
fig.tight_layout()
save(fig, "laplace-great-inequality.svg")

# ---------------------------------------------------------------- regimes timeline
fig, ax = plt.subplots(figsize=(11, 4.2))
style(ax)
regimes = [("Louis XV", 1749, 1774, BLUE), ("Louis XVI", 1774, 1792, BLUE), ("Revolution", 1792, 1795, RED),
           ("Directory", 1795, 1799, AMBER), ("Consulate", 1799, 1804, PURPLE), ("Empire", 1804, 1814, PURPLE),
           ("Restoration", 1814, 1827, BLUE)]
for name, a, b, col in regimes:
    ax.barh(1, b - a, left=a, height=0.5, color=col, alpha=0.18, edgecolor=col, lw=0.8)
    if b - a >= 8:
        ax.text((a + b) / 2, 1, name, ha="center", va="center", fontsize=8, color=GREY)
    else:
        ax.text((a + b) / 2, 1, name, ha="center", va="center", fontsize=6.5, color=GREY, rotation=90)
# (year, label, level): levels 1,2 above the bar; -1,-2 below — chosen so neighbours never collide
events = [(1749, "born,\nBeaumont-en-Auge", 1), (1768, "to Paris;\nd'Alembert", -1), (1785, "examines cadet Bonaparte;\nJupiter–Saturn solved", 1),
          (1796, "Système du monde\n(nebular hypothesis)", -1), (1799, "Minister of the\nInterior, six weeks", 2),
          (1802, "Malmaison:\n'that hypothesis'", -2), (1806, "Count of\nthe Empire", 1), (1814, "votes Napoleon out;\nEssai philosophique", -1),
          (1817, "Marquis, by\nthe Bourbons", 2), (1827, "dies,\nParis", 1)]
for yr, label, lv in events:
    up = lv > 0
    y = 1.3 + 0.55 * abs(lv) if up else 0.7 - 0.55 * abs(lv)
    ax.plot([yr, yr], [1.25 if up else 0.75, y], color=GREY, lw=0.7)
    ax.plot(yr, 1.25 if up else 0.75, "o", color=GREY, ms=3)
    ax.text(yr, y + (0.04 if up else -0.04), label, ha="center", va="bottom" if up else "top", fontsize=7.4, color=GREY)
ax.set_xlim(1745, 1831); ax.set_ylim(-0.95, 2.95)
ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.spines["right"].set_visible(False); ax.spines["top"].set_visible(False)
ax.set_title("Seven regimes, one astronomer — Laplace served every government France had", fontsize=11)
fig.tight_layout()
save(fig, "laplace-regimes-timeline.svg")

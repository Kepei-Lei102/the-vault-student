"""
stats-lies-nightingale.py — Florence Nightingale's Crimean deaths, drawn two ways.

Companion to [[Stats Lies Hall of Fame]].

Left:  a polar-area ("coxcomb") diagram in which each wedge's AREA is proportional
       to the deaths — Nightingale's corrected 1858 design.
Right: the same numbers with the RADIUS proportional to the deaths — the design
       she first drew and withdrew, in which every ratio is squared by the eye.

Data: monthly deaths in the British army in the East, April 1854 – March 1856,
from Nightingale's *Notes on Matters Affecting the Health, Efficiency and
Hospital Administration of the British Army* (1858), as tabulated in the
HistData `Nightingale` set.  Run:  python3 stats-lies-nightingale.py
"""
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# month, army strength, deaths from zymotic disease, wounds, other causes
DATA = [
    ("Apr 1854", 8571, 1, 0, 5), ("May 1854", 23333, 12, 0, 9), ("Jun 1854", 28333, 11, 0, 6),
    ("Jul 1854", 28772, 359, 0, 23), ("Aug 1854", 30246, 828, 1, 30), ("Sep 1854", 30290, 788, 81, 70),
    ("Oct 1854", 30643, 503, 132, 128), ("Nov 1854", 29736, 844, 287, 106), ("Dec 1854", 32779, 1725, 114, 131),
    ("Jan 1855", 32393, 2761, 83, 324), ("Feb 1855", 30919, 2120, 42, 361), ("Mar 1855", 30107, 1205, 32, 172),
    ("Apr 1855", 32252, 477, 48, 57), ("May 1855", 35473, 508, 49, 37), ("Jun 1855", 38863, 802, 209, 31),
    ("Jul 1855", 42647, 382, 134, 33), ("Aug 1855", 44614, 483, 164, 25), ("Sep 1855", 47751, 189, 276, 20),
    ("Oct 1855", 46852, 128, 53, 18), ("Nov 1855", 37853, 178, 33, 32), ("Dec 1855", 43217, 91, 18, 28),
    ("Jan 1856", 44212, 42, 2, 48), ("Feb 1856", 43485, 24, 0, 19), ("Mar 1856", 46140, 15, 0, 35),
]
GREY = "#888"
C_DISEASE, C_WOUNDS, C_OTHER = "#2563eb", "#dc2626", "#888888"


def annual_rate_per_1000(deaths, army):
    """Nightingale's own unit: deaths per 1000 per annum = 12 * deaths / strength * 1000."""
    return 12 * deaths / army * 1000


def main():
    first_year = DATA[:12]                      # April 1854 – March 1855, the notorious winter
    n = len(first_year)
    theta = np.linspace(0, 2 * math.pi, n, endpoint=False) + math.pi / 2   # start at the top, clockwise
    width = 2 * math.pi / n

    disease = np.array([annual_rate_per_1000(d, a) for _, a, d, _, _ in first_year])
    wounds = np.array([annual_rate_per_1000(w, a) for _, a, _, w, _ in first_year])
    other = np.array([annual_rate_per_1000(o, a) for _, a, _, _, o in first_year])

    fig = plt.figure(figsize=(11, 5.6), dpi=100)
    fig.patch.set_alpha(0)
    titles = ["Area proportional to deaths (her corrected coxcomb)",
              "Radius proportional to deaths (the version she withdrew)"]
    for k, area_true in enumerate((True, False)):
        ax = fig.add_subplot(1, 2, k + 1, projection="polar")
        ax.set_facecolor("none")
        ax.set_theta_direction(-1)
        ax.set_theta_zero_location("N")
        # draw largest series at the back so the smaller wedges stay visible
        for series, col, lab in ((disease, C_DISEASE, "zymotic disease"), (other, C_OTHER, "other causes"), (wounds, C_WOUNDS, "wounds")):
            r = np.sqrt(series) if area_true else series
            ax.bar(theta - math.pi / 2, r, width=width, bottom=0, color=col, alpha=0.55, edgecolor=col, linewidth=0.8, label=lab)
        ax.set_xticks(theta - math.pi / 2)
        ax.set_xticklabels([m for m, *_ in first_year], color=GREY, fontsize=7)
        ax.set_yticklabels([])
        ax.spines["polar"].set_color(GREY)
        ax.grid(color=GREY, alpha=0.2)
        ax.set_title(titles[k], color=GREY, fontsize=10, pad=14)
        if k == 0:
            handles, labels = ax.get_legend_handles_labels()
    fig.suptitle("Deaths per 1000 per annum, British army in the East, April 1854 – March 1855",
                 color=GREY, fontsize=11)
    leg = fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, fontsize=9)
    for t in leg.get_texts():
        t.set_color(GREY)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig("stats-lies-nightingale-coxcomb.svg", format="svg", transparent=True)

    # The numbers the card quotes
    jan = next(r for r in DATA if r[0] == "Jan 1855")
    print(f"January 1855: {jan[2]} died of disease, {jan[3]} of wounds, {jan[4]} of other causes, from an army of {jan[1]}")
    print(f"  = {annual_rate_per_1000(jan[2], jan[1]):.0f} per 1000 per annum from disease alone "
          f"(an army that would be dead in {1000/annual_rate_per_1000(jan[2], jan[1]):.2f} years at that rate)")
    tot_d, tot_w = sum(r[2] for r in DATA), sum(r[3] for r in DATA)
    print(f"whole period: {tot_d} deaths from disease vs {tot_w} from wounds — {tot_d/tot_w:.1f} : 1")
    ratio = disease.max() / wounds.max()
    print(f"peak disease rate : peak wounds rate = {ratio:.1f} : 1")
    print(f"  drawn as areas that ratio LOOKS like {ratio:.1f} : 1; drawn as radii it looks like {ratio**2:.0f} : 1")
    y1 = sum(r[2] for r in DATA[:12]); y2 = sum(r[2] for r in DATA[12:])
    print(f"disease deaths, first year {y1} → second year {y2} after the Sanitary Commission (March 1855): ÷{y1/y2:.1f}")
    print("wrote stats-lies-nightingale-coxcomb.svg")


if __name__ == "__main__":
    main()

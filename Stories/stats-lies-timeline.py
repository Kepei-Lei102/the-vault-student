"""
stats-lies-timeline.py — the hall of fame on one axis, 1849–1975.

Companion to [[Stats Lies Hall of Fame]].  Each entry: the lie (red, below the
axis) and the catch (green, above), with the person who caught it.
Run:  python3 stats-lies-timeline.py  → stats-lies-timeline.svg
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GREY, RED, GREEN, BLUE = "#888", "#dc2626", "#059669", "#2563eb"

EVENTS = [
    # year, above-text (the catch), below-text (the lie), stagger level (1 near, 2 mid, 3 far), x-offset for the label
    (1852, "Snow: the water, not the air\n(the pump 1854; the two\nwater companies 1855)", "Farr: cholera falls with\nelevation - the miasma law", 1, 0),
    (1858, "Nightingale redraws her\nchart with true areas", "her first chart scaled\nradii, squaring every ratio", 2, 0),
    (1936, "Gallup, 50 000 people,\ncalls Roosevelt", "Literary Digest, 2.4 million\nballots, calls Landon", 1, 0),
    (1943, "Wald: armour where the\nsurvivors are clean", "'armour where the\nreturning planes are hit'", 2, 0),
    (1954, "Huff, How to Lie with\nStatistics: the field guide", "1965: Huff testifies for\ntobacco with the same tricks", 1, 0),
    (1965, "Bradford Hill's nine\nviewpoints on causation", "Fisher 1957-59: 'correlation\nis not causation' - for hire", 3, -7),
    (1973, "Anscombe: four sets,\none summary - plot it", "'the statistics are\nidentical, so the data are'", 1, 7),
    (1975, "Bickel, Hammel, O'Connell:\ncondition on the department", "Berkeley 1973: 'men 44%,\nwomen 35% - bias'", 2, 9),
]


def main():
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=100)
    fig.patch.set_alpha(0); ax.set_facecolor("none")
    ax.axhline(0, color=GREY, lw=1.5)
    ax.set_xlim(1844, 1984); ax.set_ylim(-4.3, 4.3)
    for yr, above, below, lvl, dx in EVENTS:
        ya, yb = {1: (0.9, -0.9), 2: (1.9, -1.9), 3: (2.9, -2.9)}[lvl]
        ax.plot([yr, yr + dx], [0, ya], color=GREY, lw=0.8, alpha=0.5)
        ax.plot([yr, yr + dx], [0, yb], color=GREY, lw=0.8, alpha=0.5)
        ax.scatter([yr], [0], color=BLUE, s=36, zorder=3)
        ax.text(yr + dx, ya + 0.08, above, ha="center", va="bottom", fontsize=7.6, color=GREEN, linespacing=1.1)
        ax.text(yr + dx, yb - 0.08, below, ha="center", va="top", fontsize=7.6, color=RED, linespacing=1.1)
        ax.text(yr, 0.28 if lvl != 1 else -0.45, str(yr), ha="center", fontsize=8, color=GREY)
    ax.text(1846, 4.1, "the catch", color=GREEN, fontsize=10, va="top")
    ax.text(1846, -4.1, "the lie", color=RED, fontsize=10, va="bottom")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig("stats-lies-timeline.svg", format="svg", transparent=True)
    print("wrote stats-lies-timeline.svg")


if __name__ == "__main__":
    main()

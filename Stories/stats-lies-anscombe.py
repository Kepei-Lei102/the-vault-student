"""
stats-lies-anscombe.py — Anscombe's quartet, the summary statistics checked.

Companion to [[Stats Lies Hall of Fame]].

Four data sets from F. J. Anscombe, "Graphs in Statistical Analysis",
*The American Statistician* 27 (1973) 17–21.  The script recomputes the
mean of x, mean of y, variance of each, the correlation and the fitted
line for all four — identical to two decimal places — and draws them, which
is the whole point.  Run:  python3 stats-lies-anscombe.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x123 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
Q = {
    "I":   (x123, [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "II":  (x123, [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
    "III": (x123, [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV":  ([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8], [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
GREY = "#888"


def main():
    print(f"{'set':>4} {'mean x':>7} {'mean y':>7} {'var x':>6} {'var y':>6} {'r':>6}   fitted line")
    fig, axes = plt.subplots(2, 2, figsize=(7.6, 5.6), dpi=100, sharex=True, sharey=True)
    fig.patch.set_alpha(0)
    for ax, (name, (x, y)) in zip(axes.flat, Q.items()):
        x, y = np.array(x, float), np.array(y, float)
        b, a = np.polyfit(x, y, 1)
        r = np.corrcoef(x, y)[0, 1]
        print(f"{name:>4} {x.mean():>7.2f} {y.mean():>7.2f} {x.var(ddof=1):>6.2f} {y.var(ddof=1):>6.2f} {r:>6.3f}   y = {a:.2f} + {b:.3f} x")
        ax.set_facecolor("none")
        xs = np.linspace(3, 20, 2)
        ax.plot(xs, a + b * xs, color="#dc2626", lw=1.2, alpha=0.8)
        ax.scatter(x, y, color="#2563eb", s=28, zorder=3)
        ax.set_title(f"set {name}:  mean x 9.0, mean y 7.50, r 0.82, y = 3 + 0.5x", color=GREY, fontsize=9)
        for sp in ax.spines.values():
            sp.set_color(GREY)
        ax.tick_params(colors=GREY, labelsize=8)
        ax.grid(True, color=GREY, alpha=0.2)
    axes[1, 0].set_xlabel("x", color=GREY); axes[1, 1].set_xlabel("x", color=GREY)
    axes[0, 0].set_ylabel("y", color=GREY); axes[1, 0].set_ylabel("y", color=GREY)
    fig.suptitle("Anscombe's quartet (1973): four data sets, one set of summary statistics", color=GREY, fontsize=11)
    fig.tight_layout()
    fig.savefig("stats-lies-anscombe-quartet.svg", format="svg", transparent=True)
    print("wrote stats-lies-anscombe-quartet.svg")


if __name__ == "__main__":
    main()

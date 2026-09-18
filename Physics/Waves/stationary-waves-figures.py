"""
stationary-waves-figures.py — the static figures for [[Stationary Waves]].

  stationary-waves-formation.svg   the graphical method: two travelling waves and their sum at
                                   t = 0, T/8, T/4, 3T/8, T/2 — nodes stay still, antinodes swing
  stationary-waves-string.svg      the first four harmonics on a string fixed at both ends
  stationary-waves-pipes.svg       open–open and closed–open pipes: displacement nodes/antinodes
  stationary-waves-experiments.svg the three syllabus experiments: microwaves, Melde's string,
                                   the resonance tube (λ = 2(L2 − L1))

All text #888, transparent background, verified light and dark.
Run:  python3 stationary-waves-figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

GREY = "#888"
BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"


def style(ax, title=""):
    ax.set_facecolor("none")
    for sp in ax.spines.values():
        sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelsize=8)
    if title:
        ax.set_title(title, color=GREY, fontsize=9.5)


def formation():
    lam, A = 2.0, 1.0
    k = 2 * np.pi / lam
    x = np.linspace(0, 2 * lam, 400)
    phases = [0, 1 / 8, 1 / 4, 3 / 8, 1 / 2]
    fig, axes = plt.subplots(1, 5, figsize=(13, 3.4), dpi=100, sharey=True)
    fig.patch.set_alpha(0)
    for ax, ph in zip(axes, phases):
        wt = 2 * np.pi * ph
        y1 = A * np.sin(k * x - wt); y2 = A * np.sin(k * x + wt)
        ax.plot(x, y1, color=BLUE, lw=1.2, alpha=0.8, label="to the right")
        ax.plot(x, y2, color=RED, lw=1.2, alpha=0.8, label="to the left")
        ax.plot(x, y1 + y2, color=PURPLE, lw=2.4, label="sum")
        for n in np.arange(0, 2 * lam + 0.01, lam / 2):
            ax.scatter([n], [0], color=GREY, s=18, zorder=3)
        ax.axhline(0, color=GREY, lw=0.7)
        ax.set_ylim(-2.3, 2.3); ax.set_xticks([]); ax.set_yticks([])
        style(ax, f"t = {ph:g}T".replace("0T", "0").replace("0.125T", "T/8").replace("0.25T", "T/4").replace("0.375T", "3T/8").replace("0.5T", "T/2"))
    axes[0].set_ylabel("displacement", color=GREY)
    leg = axes[0].legend(frameon=False, fontsize=7.5, loc="upper left")
    for t in leg.get_texts(): t.set_color(GREY)
    fig.suptitle("Two equal waves, opposite directions: the sum (purple) never travels — the grey dots (nodes) never move, the antinodes swing to 2A",
                 color=GREY, fontsize=10)
    fig.tight_layout()
    fig.savefig("stationary-waves-formation.svg", format="svg", transparent=True)


def string():
    L = 1.0
    fig, axes = plt.subplots(4, 1, figsize=(8, 6.4), dpi=100, sharex=True)
    fig.patch.set_alpha(0)
    x = np.linspace(0, L, 400)
    for n, ax in enumerate(axes, start=1):
        y = np.sin(n * np.pi * x / L)
        ax.plot(x, y, color=BLUE, lw=2); ax.plot(x, -y, color=BLUE, lw=2, alpha=0.35)
        ax.fill_between(x, y, -y, color=BLUE, alpha=0.08)
        ax.axhline(0, color=GREY, lw=0.7)
        for j in range(n + 1):
            ax.scatter([j * L / n], [0], color=RED, s=30, zorder=3)
        ax.text(1.02, 0.5, f"n = {n}:  L = {n}·λ/2,  λ = {2/n if n != 1 else 2:g}L / {n}".replace("2g", "2") if False else f"n = {n}:  L = {n}λ/2   λ = 2L/{n}   f = {n}·v/2L", transform=ax.transAxes, color=GREY, fontsize=9, va="center")
        ax.set_ylim(-1.3, 1.3); ax.set_yticks([]); ax.set_xlim(0, L)
        style(ax)
    axes[0].set_title("String fixed at both ends: a node at each end forces L = nλ/2 — harmonics f₁, 2f₁, 3f₁, 4f₁ (red dots: nodes)", color=GREY, fontsize=9.5)
    axes[-1].set_xlabel("position along the string (L = 1)", color=GREY)
    fig.subplots_adjust(right=0.7)
    fig.savefig("stationary-waves-pipes-placeholder.svg", format="svg", transparent=True) if False else None
    fig.savefig("stationary-waves-string.svg", format="svg", transparent=True, bbox_inches="tight")


def pipes():
    L = 1.0
    fig, axes = plt.subplots(2, 3, figsize=(12, 5.2), dpi=100)
    fig.patch.set_alpha(0)
    x = np.linspace(0, L, 400)
    # open–open: antinode at both ends, L = nλ/2
    for col, n in enumerate((1, 2, 3)):
        ax = axes[0, col]
        y = np.cos(n * np.pi * x / L)
        ax.plot(x, y, color=GREEN, lw=2); ax.plot(x, -y, color=GREEN, lw=2, alpha=0.35)
        ax.fill_between(x, y, -y, color=GREEN, alpha=0.08)
        for j in range(n):
            ax.scatter([(2 * j + 1) * L / (2 * n)], [0], color=RED, s=30, zorder=3)
        ax.axhline(0, color=GREY, lw=0.7); ax.set_ylim(-1.4, 1.4); ax.set_xticks([]); ax.set_yticks([])
        ax.plot([0, 0], [-1.2, 1.2], color=GREY, lw=1, ls=":"); ax.plot([L, L], [-1.2, 1.2], color=GREY, lw=1, ls=":")
        style(ax, f"open–open, n = {n}:  L = {n}λ/2,  f = {n}·v/2L")
    # closed–open: node at closed end (x=0), antinode at open end: L = (2m-1)λ/4
    for col, m in enumerate((1, 3, 5)):
        ax = axes[1, col]
        y = np.sin(m * np.pi * x / (2 * L))
        ax.plot(x, y, color=AMBER, lw=2); ax.plot(x, -y, color=AMBER, lw=2, alpha=0.35)
        ax.fill_between(x, y, -y, color=AMBER, alpha=0.08)
        for j in range((m + 1) // 2):
            ax.scatter([2 * j * L / m], [0], color=RED, s=30, zorder=3)
        ax.axhline(0, color=GREY, lw=0.7); ax.set_ylim(-1.4, 1.4); ax.set_xticks([]); ax.set_yticks([])
        ax.plot([0, 0], [-1.2, 1.2], color=GREY, lw=3); ax.plot([L, L], [-1.2, 1.2], color=GREY, lw=1, ls=":")
        style(ax, f"closed–open, harmonic {m}:  L = {m}λ/4,  f = {m}·v/4L")
    fig.suptitle("Air columns drawn as DISPLACEMENT envelopes: a closed end is a node, an open end an antinode — so the closed pipe has only odd harmonics",
                 color=GREY, fontsize=10)
    fig.tight_layout()
    fig.savefig("stationary-waves-pipes.svg", format="svg", transparent=True)


def experiments():
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.9), dpi=100)
    fig.patch.set_alpha(0)
    # microwaves
    ax = axes[0]
    ax.add_patch(plt.Rectangle((0.02, 0.4), 0.14, 0.2, color=BLUE, alpha=0.3)); ax.text(0.09, 0.3, "transmitter", ha="center", color=GREY, fontsize=8)
    ax.plot([0.9, 0.9], [0.2, 0.8], color=GREY, lw=4); ax.text(0.9, 0.84, "metal reflector", ha="center", color=GREY, fontsize=8)
    xs = np.linspace(0.18, 0.9, 300); env = np.abs(np.sin(2 * np.pi * (0.9 - xs) / 0.1))
    ax.plot(xs, 0.5 + 0.18 * env, color=PURPLE, lw=1.5); ax.plot(xs, 0.5 - 0.18 * env, color=PURPLE, lw=1.5, alpha=0.4)
    for i in range(8):
        ax.scatter([0.9 - i * 0.05], [0.5], color=RED, s=14, zorder=3)
    ax.annotate("", (0.75, 0.3), (0.85, 0.3), arrowprops=dict(arrowstyle="<->", color=AMBER)); ax.text(0.8, 0.22, "node to node = λ/2 ≈ 1.4 cm", ha="center", color=AMBER, fontsize=7.5)
    ax.text(0.5, 0.06, "probe moved along the line: signal minima every λ/2; λ ≈ 2.8 cm for a 10.7 GHz set", ha="center", color=GREY, fontsize=7.5)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([]); style(ax, "Microwaves: transmitter, reflector, probe")
    # string (Melde)
    ax = axes[1]
    ax.add_patch(plt.Rectangle((0.02, 0.4), 0.12, 0.2, color=BLUE, alpha=0.3)); ax.text(0.08, 0.66, "vibration\ngenerator", ha="center", color=GREY, fontsize=7.5)
    ax.plot([0.88, 0.88], [0.25, 0.75], color=GREY, lw=1); ax.scatter([0.88], [0.5], color=GREY, s=60, zorder=3)
    ax.plot([0.88, 0.88], [0.5, 0.15], color=GREY, lw=1); ax.add_patch(plt.Rectangle((0.85, 0.05), 0.06, 0.1, color=GREY, alpha=0.6)); ax.text(0.88, 0.0, "mass sets T", ha="center", color=GREY, fontsize=7.5)
    xs = np.linspace(0.14, 0.88, 300); y = 0.16 * np.sin(3 * np.pi * (xs - 0.14) / 0.74)
    ax.plot(xs, 0.5 + y, color=BLUE, lw=2); ax.plot(xs, 0.5 - y, color=BLUE, lw=2, alpha=0.35)
    for j in range(4):
        ax.scatter([0.14 + j * 0.74 / 3], [0.5], color=RED, s=20, zorder=3)
    ax.text(0.5, 0.85, "3 loops: L = 3λ/2, f = 3v/2L with v = √(T/μ)", ha="center", color=GREY, fontsize=8)
    ax.text(0.5, 0.2, "raise f: more loops; raise T: fewer", ha="center", color=GREY, fontsize=7.5)
    ax.set_xlim(0, 1); ax.set_ylim(-0.05, 1); ax.set_xticks([]); ax.set_yticks([]); style(ax, "Stretched string (Melde's experiment)")
    # resonance tube
    ax = axes[2]
    for xoff, Lc, lab in ((0.22, 0.3, "L₁ = λ/4"), (0.62, 0.9, "L₂ = 3λ/4")):
        ax.plot([xoff - 0.06, xoff - 0.06], [0.05, 0.05 + Lc * 0.9], color=GREY, lw=2); ax.plot([xoff + 0.06, xoff + 0.06], [0.05, 0.05 + Lc * 0.9], color=GREY, lw=2)
        ax.plot([xoff - 0.06, xoff + 0.06], [0.05, 0.05], color=GREY, lw=3)
        ys = np.linspace(0.05, 0.05 + Lc * 0.9, 200); env = 0.05 * np.abs(np.sin(np.pi * (ys - 0.05) / (2 * 0.3 * 0.9)))
        ax.plot(xoff + env, ys, color=AMBER, lw=1.5); ax.plot(xoff - env, ys, color=AMBER, lw=1.5)
        ax.text(xoff, 0.05 + Lc * 0.9 + 0.1, "tuning fork", ha="center", color=GREY, fontsize=7.5)
        ax.plot([xoff - 0.03, xoff - 0.03], [0.05 + Lc * 0.9 + 0.02, 0.05 + Lc * 0.9 + 0.08], color=GREY, lw=2); ax.plot([xoff + 0.03, xoff + 0.03], [0.05 + Lc * 0.9 + 0.02, 0.05 + Lc * 0.9 + 0.08], color=GREY, lw=2)
        ax.text(xoff + 0.1, 0.05 + Lc * 0.45, lab, color=AMBER, fontsize=8, va="center")
    ax.text(0.5, 0.0, "water level lowered until it sings twice: λ = 2(L₂ − L₁), v = fλ (end corrections cancel)", ha="center", color=GREY, fontsize=7.5)
    ax.set_xlim(0, 1); ax.set_ylim(-0.05, 1.1); ax.set_xticks([]); ax.set_yticks([]); style(ax, "Air column: the resonance tube")
    fig.tight_layout()
    fig.savefig("stationary-waves-experiments.svg", format="svg", transparent=True)


if __name__ == "__main__":
    formation(); string(); pipes(); experiments()
    print("wrote four SVGs")

"""Figures for [[Special Relativity]].

Regenerate:  python3 special-relativity-figures.py
  special-relativity-gamma.svg        the Lorentz factor against speed
  special-relativity-light-clock.svg  the light clock at rest and moving, with the right triangle that gives gamma
  special-relativity-spacetime.svg    a space-time diagram at 0.6c: tilted axes, a calibration hyperbola, simultaneity
  special-relativity-muons.svg        muon survival against distance fallen, with and without time dilation
  special-relativity-energy.svg       velocity addition, and kinetic energy against (1/2) m v^2
Vault palette: all text #888, transparent background.
"""
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AX, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX, "xtick.color": AX, "ytick.color": AX,
                     "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})
gamma = lambda b: 1 / np.sqrt(1 - b * b)


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def bare(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def fig_gamma():
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    b = np.linspace(0, 0.995, 600); ax.plot(b, gamma(b), color=BLUE, lw=2.6)
    for bb in (0.5, 0.6, 0.8, np.sqrt(3) / 2, 0.9, 0.99):
        ax.plot(bb, gamma(bb), "o", color=AMBER, ms=8, zorder=5)
    table = "\n".join(f"{bb:.3g}c      γ = {gamma(bb):.3g}" for bb in (0.5, 0.6, 0.8, np.sqrt(3) / 2, 0.9, 0.99))
    ax.text(0.30, 6.9, "the amber points, left to right:\n" + table, color=AMBER, fontsize=11.5, va="top", linespacing=1.5)
    ax.axhline(1, color=AX, lw=1, ls=":")
    ax.annotate("an airliner, the Space Station and a GPS satellite all sit here:\nγ differs from 1 in the tenth decimal place or beyond", (0.0, 1.0), xytext=(14, 60),
                textcoords="offset points", color=GREEN, fontsize=11, arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
    ax.set_xlim(0, 1.0); ax.set_ylim(0.6, 8); ax.set_xlabel("speed, as a fraction of the speed of light"); ax.set_ylabel("Lorentz factor γ")
    ax.set_title("γ stays at 1 for every speed you have ever travelled at, then climbs without limit", color=AX, fontsize=13); bare(ax)
    save(fig, "special-relativity-gamma.svg")


def fig_light_clock():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 5.0), gridspec_kw={"width_ratios": [1, 2.3]})
    for ax in (a, b):
        ax.set_aspect("equal"); ax.axis("off")
    # at rest
    a.plot([-0.5, 0.5], [0, 0], color=AX, lw=4); a.plot([-0.5, 0.5], [2, 2], color=AX, lw=4)
    a.annotate("", (0.0, 1.95), (0.0, 0.05), arrowprops=dict(arrowstyle="<->", color=AMBER, lw=2.4))
    a.text(0.12, 1.0, "light path\nup and back: 2L", color=AMBER, fontsize=11, va="center")
    a.text(-0.72, 1.0, "L", color=AX, fontsize=14, va="center")
    a.text(0, -0.45, "seen by someone\nriding with the clock", color=AX, fontsize=12, ha="center")
    a.text(0, 2.35, "tick = 2L / c", color=GREEN, fontsize=13, ha="center")
    a.set_xlim(-1.1, 1.3); a.set_ylim(-0.9, 2.7)
    # moving
    xs = [0, 1.5, 3.0]
    for x in xs:
        b.plot([x - 0.5, x + 0.5], [0, 0], color=AX, lw=4, alpha=0.55 if x != 0 else 1); b.plot([x - 0.5, x + 0.5], [2, 2], color=AX, lw=4, alpha=0.55 if x != 0 else 1)
    b.annotate("", (1.5, 1.95), (0.0, 0.05), arrowprops=dict(arrowstyle="->", color=AMBER, lw=2.4))
    b.annotate("", (3.0, 0.05), (1.5, 1.95), arrowprops=dict(arrowstyle="->", color=AMBER, lw=2.4))
    b.plot([0, 1.5], [0, 0], color=BLUE, lw=2.2, ls="--"); b.plot([1.5, 1.5], [0, 2], color=PURPLE, lw=2.2, ls="--")
    b.text(0.75, -0.22, "v Δt / 2", color=BLUE, fontsize=12, ha="center", va="top")
    b.text(1.58, 0.9, "L", color=PURPLE, fontsize=14)
    b.text(0.42, 1.18, "c Δt / 2", color=AMBER, fontsize=12, ha="center", rotation=53)
    b.annotate("", (3.5, 2.35), (2.3, 2.35), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2)); b.text(2.9, 2.45, "clock moves at v", color=BLUE, fontsize=12, ha="center")
    b.text(1.5, -0.75, "seen by someone the clock moves past: the same light, at the same speed c,\nhas a longer diagonal to cover, so each tick takes longer", color=AX, fontsize=12, ha="center")
    b.set_xlim(-0.8, 3.9); b.set_ylim(-1.2, 2.7)
    fig.suptitle("The light clock: Pythagoras on the blue, purple and amber triangle gives Δt = γ × 2L/c", color=AX, fontsize=13, y=0.98)
    save(fig, "special-relativity-light-clock.svg")


def fig_spacetime():
    beta = 0.6; g = gamma(beta)
    fig, ax = plt.subplots(figsize=(9.2, 7.6))
    ax.axhline(0, color=AX, lw=1.4); ax.axvline(0, color=AX, lw=1.4)
    t = np.linspace(-1, 7.4, 10)
    ax.plot(t, t, color=AMBER, lw=1.6, ls="--"); ax.plot(-t, t, color=AMBER, lw=1.6, ls="--")
    ax.text(-3.9, 4.15, "light", color=AMBER, fontsize=11, rotation=-45); ax.text(6.35, 6.0, "light", color=AMBER, fontsize=11, rotation=45)
    ax.plot(beta * t, t, color=BLUE, lw=2.4); ax.text(4.75, 7.35, "ct′ axis:\nthe traveller's\nworld line", color=BLUE, fontsize=11, va="top")
    ax.plot(t, beta * t, color=PURPLE, lw=2.4); ax.text(7.4, 2.75, "x′ axis: everything the\ntraveller calls “now” at O", color=PURPLE, fontsize=11, ha="right", va="top")
    x = np.linspace(-3.4, 5.0, 400); ax.plot(x, np.sqrt(16 + x * x), color=GREEN, lw=1.6)
    ax.text(-4.1, 6.55, "(ct)² − x² = 16: every point on this curve\nis 4 s of proper time from O", color=GREEN, fontsize=10.5)
    ax.plot(0, 4, "o", color=GREEN, ms=8); ax.text(-0.16, 3.62, "ct = 4", color=GREEN, fontsize=11, ha="right")
    ax.plot(3, 5, "o", color=RED, ms=10, zorder=6); ax.text(3.25, 4.55, "A (x = 3, ct = 5)\nfor the traveller: ct′ = 4", color=RED, fontsize=11, va="top")
    ax.plot([3, 0], [5, 5], color=AX, lw=1, ls=":"); ax.plot([3, 3], [5, 0], color=AX, lw=1, ls=":")
    ax.plot([-2.4, 2.4], [2, 2], color=TEAL, lw=1, ls=":")
    for x0, name, lab, dx in ((-2.4, "P", "t′ = 4.3 s", 0.18), (2.4, "Q", "t′ = 0.7 s", 0.18)):
        ct_hit = (2 - beta * x0) / (1 - beta * beta); x_hit = beta * ct_hit      # where the traveller's "same time" line meets the ct′ axis
        ax.plot([x0, x_hit], [2, ct_hit], color=PURPLE, lw=1.4, ls="-.")
        ax.plot(x_hit, ct_hit, "o", color=PURPLE, ms=7, zorder=6)
        if name == "P":
            ax.text(x_hit + dx, ct_hit - 0.12, lab, color=PURPLE, fontsize=11, va="top")
        else:
            ax.annotate(lab, (x_hit, ct_hit), xytext=(-2.9, 0.75), textcoords="data", color=PURPLE, fontsize=11, arrowprops=dict(arrowstyle="-", color=PURPLE, lw=0.8))
        ax.plot(x0, 2, "s", color=TEAL, ms=9, zorder=6); ax.text(x0 + (0.34 if name == "Q" else 0), 1.45 if name == "P" else 1.62, name, color=TEAL, fontsize=13, ha="center")
    ax.text(0.15, 7.1, "ct", color=AX, fontsize=14); ax.text(7.05, 0.18, "x", color=AX, fontsize=14); ax.text(-0.4, -0.45, "O", color=AX, fontsize=13)
    ax.set_xlim(-4.3, 7.5); ax.set_ylim(-0.8, 7.5); ax.set_aspect("equal")
    ax.set_xticks(range(-4, 8, 2)); ax.set_yticks(range(0, 8, 2)); bare(ax)
    ax.set_xlabel("x, light-seconds"); ax.set_ylabel("ct, light-seconds")
    ax.set_title("A space-time diagram for a traveller moving at 0.6c: both axes tilt towards the light line", color=AX, fontsize=13)
    save(fig, "special-relativity-spacetime.svg")


def fig_muons():
    c = 299_792_458.0; tau = 2.197e-6; beta = 0.995; g = gamma(beta)
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    h = np.linspace(0, 4000, 400); t = h / (beta * c)
    ax.plot(h, np.exp(-t / tau), color=RED, lw=2.4, label="if moving clocks kept ordinary time")
    ax.plot(h, np.exp(-t / g / tau), color=GREEN, lw=2.4, label="with time dilation, γ = 10")
    ax.plot(1907, 409 / 565, "o", color=AMBER, ms=11, zorder=6)
    ax.annotate("measured, 1963:\n409 of 565 per hour reach sea level\nafter 1907 m (72 %)", (1907, 409 / 565), xytext=(-40, -78), textcoords="offset points", color=AMBER, fontsize=11.5, va="center", arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.8))
    ax.plot(1907, np.exp(-1907 / (beta * c) / tau), "o", color=RED, ms=8); ax.annotate("predicted without\nrelativity: 5 %", (1907, 0.0545), xytext=(16, 14), textcoords="offset points", color=RED, fontsize=11.5)
    ax.set_xlabel("distance fallen through the atmosphere, metres"); ax.set_ylabel("fraction of muons still alive")
    ax.set_ylim(0, 1.05); ax.set_xlim(0, 4000); ax.legend(frameon=False, labelcolor=AX, loc="upper right"); bare(ax)
    ax.set_title("Muons at 0.995c: a lifetime of 2.2 μs should not get them down a mountain", color=AX, fontsize=13)
    save(fig, "special-relativity-muons.svg")


def fig_energy():
    fig, (a, b) = plt.subplots(2, 1, figsize=(9.2, 9.6)); fig.subplots_adjust(hspace=0.42)
    u = np.linspace(0, 1, 400)
    a.plot(u, 2 * u, color=RED, lw=2.2, ls="--", label="the everyday rule: u + u"); a.plot(u, 2 * u / (1 + u * u), color=GREEN, lw=2.6, label="the correct rule: (u + u) / (1 + u²/c²)")
    a.axhline(1, color=AMBER, lw=1.4, ls=":"); a.text(0.02, 1.04, "the speed of light", color=AMBER, fontsize=11)
    a.plot(0.6, 1.2 / 1.36, "o", color=GREEN, ms=9); a.annotate("0.6c and 0.6c give 0.882c", (0.6, 1.2 / 1.36), xytext=(12, -22), textcoords="offset points", color=GREEN, fontsize=11.5)
    a.set_xlabel("each speed u, as a fraction of c"); a.set_ylabel("combined speed, as a fraction of c"); a.set_ylim(0, 2.05); a.set_xlim(0, 1)
    a.legend(frameon=False, labelcolor=AX, loc="upper left", bbox_to_anchor=(0.0, 0.92)); bare(a)
    a.set_title("Adding two equal speeds: the sum bends over and never reaches c", color=AX, fontsize=13)
    v = np.linspace(0, 0.985, 500)
    b.plot(v, 0.5 * v * v, color=RED, lw=2.2, ls="--", label="½mv²"); b.plot(v, gamma(v) - 1, color=GREEN, lw=2.6, label="(γ − 1)mc²")
    b.set_ylim(0, 4); b.set_xlim(0, 1); b.set_xlabel("speed, as a fraction of c"); b.set_ylabel("kinetic energy, in units of mc²")
    b.annotate("below about 0.1c the two\ncurves cannot be told apart", (0.1, 0.005), xytext=(20, 50), textcoords="offset points", color=AX, fontsize=11.5, arrowprops=dict(arrowstyle="->", color=AX, lw=1))
    b.legend(frameon=False, labelcolor=AX, loc="upper left"); bare(b)
    b.set_title("Kinetic energy: no finite amount of energy reaches the speed of light", color=AX, fontsize=13)
    save(fig, "special-relativity-energy.svg")


if __name__ == "__main__":
    fig_gamma(); fig_light_clock(); fig_spacetime(); fig_muons(); fig_energy(); print("wrote 5 SVGs")

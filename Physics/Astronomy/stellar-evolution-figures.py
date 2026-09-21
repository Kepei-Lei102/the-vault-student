"""Figures for [[Stellar Evolution]].  Run: python3 stellar-evolution-figures.py
Writes six SVGs beside this script: lifecycle, hr-diagram, sun-track, lifetimes, white-dwarfs, parallax.
All text #888, transparent background, width=100 %."""
import contextlib
import importlib.util
import io
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("model", os.path.join(HERE, "stellar-evolution-model.py"))
model = importlib.util.module_from_spec(spec); spec.loader.exec_module(model)

GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": GREY, "axes.labelcolor": GREY, "axes.edgecolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "font.size": 11, "svg.fonttype": "none", "font.family": "DejaVu Sans"})


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)
    s = open(path).read()
    s = re.sub(r'<svg([^>]*?) width="[^"]*" height="[^"]*"', r'<svg\1 width="100%"', s, count=1)
    open(path, "w").write(s)
    print("wrote", name)


def box(ax, x, y, w, h, text, colour, size=10.5):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=matplotlib.colors.to_rgba(colour, 0.15), ec=colour, lw=1.5))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=GREY, multialignment="center")


def arrow(ax, p, q, colour=GREY, rad=0.0, lw=1.6):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=14, color=colour, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}"))


def lifecycle():
    fig, ax = plt.subplots(figsize=(10, 7.4))
    ax.set_xlim(0, 13.2); ax.set_ylim(0, 7.6); ax.axis("off")
    box(ax, 5, 7.0, 5.8, 0.75, "interstellar cloud of gas and dust\n(mostly hydrogen)", TEAL)
    box(ax, 5, 5.75, 5.8, 0.75, "protostar: the cloud collapses under its own\ngravity and its temperature rises", PURPLE)
    box(ax, 5, 4.5, 5.8, 0.75, "stable star (main sequence): hydrogen fuses\nto helium; gravity inward = pressure outward", GREEN)
    arrow(ax, (5, 6.62), (5, 6.13)); arrow(ax, (5, 5.37), (5, 4.88))
    ax.text(2.3, 3.72, "about the mass of the Sun", ha="center", fontsize=11, color=AMBER, weight="bold")
    ax.text(7.7, 3.72, "more than about 8 Suns", ha="center", fontsize=11, color=RED, weight="bold")
    arrow(ax, (3.9, 4.12), (2.5, 3.35), AMBER); arrow(ax, (6.1, 4.12), (7.5, 3.35), RED)
    box(ax, 2.3, 2.95, 4.0, 0.62, "red giant", AMBER)
    box(ax, 2.3, 1.85, 4.0, 0.75, "planetary nebula, with a\nwhite dwarf at its centre", AMBER)
    arrow(ax, (2.3, 2.63), (2.3, 2.24), AMBER)
    box(ax, 7.7, 2.95, 4.0, 0.62, "red supergiant", RED)
    box(ax, 7.7, 1.95, 4.0, 0.62, "supernova", RED)
    box(ax, 7.7, 0.75, 4.9, 0.95, "nebula of hydrogen and new heavier\nelements; a neutron star or a\nblack hole left at the centre", RED, 10)
    arrow(ax, (7.7, 2.63), (7.7, 2.27), RED); arrow(ax, (7.7, 1.63), (7.7, 1.24), RED)
    arrow(ax, (10.2, 0.75), (7.95, 7.0), TEAL, rad=0.42)
    ax.text(11.35, 3.6, "the nebula may\nform new stars,\nwith orbiting\nplanets", ha="left", fontsize=10, color=TEAL)
    ax.text(2.3, 0.85, "hydrogen runs out in the core in\nevery case; mass decides the rest", ha="center", fontsize=10, color=GREY, style="italic")
    save(fig, "stellar-evolution-lifecycle.svg")


STARS = [  # name, T (K), L (suns), label offset (points)
    ("Sun", 5772, 1.0, (8, 4)), ("Sirius A", 9940, 25.4, (8, -2)), ("Vega", 9600, 40, (-34, 8)), ("Spica", 25300, 20500, (-40, -13)),
    ("Proxima Centauri", 3040, 0.0017, (-112, 2)), ("Barnard's Star", 3130, 0.0035, (-96, 8)), ("Alpha Centauri A", 5790, 1.52, (-112, 8)),
    ("Rigel", 12100, 1.2e5, (8, 4)), ("Deneb", 8500, 1.96e5, (-8, 8)), ("Betelgeuse", 3600, 1.26e5, (-72, 6)), ("Antares", 3660, 7.6e4, (-56, -14)),
    ("Aldebaran", 3900, 440, (-66, 4)), ("Arcturus", 4290, 170, (-60, -12)), ("Polaris", 6015, 1260, (8, 2)),
    ("Sirius B", 25000, 0.056, (8, 2)), ("40 Eridani B", 16500, 0.013, (8, 2)), ("Procyon B", 7740, 0.00049, (8, 2)),
]


def hr_axes(ax):
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(45000, 2300); ax.set_ylim(1e-4, 1e6)
    ax.set_xticks([40000, 20000, 10000, 5000, 3000]); ax.set_xticklabels(["40 000", "20 000", "10 000", "5 000", "3 000"])
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_xlabel("surface temperature / K   (hot on the LEFT)"); ax.set_ylabel("luminosity / luminosity of the Sun")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    T = np.array([45000, 2300.0])
    for R in (0.01, 0.1, 1, 10, 100, 1000):
        L = R**2 * (T / 5772) ** 4
        ax.plot(T, L, color=GREY, lw=0.8, ls=":", alpha=0.8)


MS_TABLE = [  # mass, T, L for main-sequence stars (after Pecaut & Mamajek's tabulation, rounded)
    (0.09, 2500, 0.0005), (0.16, 3060, 0.003), (0.57, 3850, 0.069), (0.88, 5270, 0.46), (1.0, 5772, 1.0),
    (1.6, 7220, 7.2), (2.3, 9700, 38), (4.7, 15700, 590), (17.7, 31400, 44700), (40, 41000, 4.0e5)]


def main_sequence_curve():
    tab = np.log10(np.array(MS_TABLE))
    M = np.logspace(tab[0, 0], tab[-1, 0], 120)
    T = 10 ** np.interp(np.log10(M), tab[:, 0], tab[:, 1])
    L = 10 ** np.interp(np.log10(M), tab[:, 0], tab[:, 2])
    return M, T, L


def hr_diagram():
    fig, ax = plt.subplots(figsize=(10, 9))
    hr_axes(ax)
    M, T, L = main_sequence_curve()
    ax.plot(T, L, color=GREEN, lw=9, alpha=0.22, solid_capstyle="round")
    ax.plot(T, L, color=GREEN, lw=1.5)
    for m in (0.1, 0.5, 2, 10, 25):
        i = np.argmin(abs(M - m))
        ax.plot(T[i], L[i], "o", color=GREEN, ms=4)
        ax.annotate(f"{m:g} M", (T[i], L[i]), xytext=(-8, -13) if m > 0.2 else (-10, 6), textcoords="offset points", fontsize=9, color=GREEN, ha="right")
    ax.text(16500, 28, "MAIN SEQUENCE", color=GREEN, fontsize=12, rotation=-50, weight="bold")
    ax.add_patch(Polygon([[5200, 25], [3300, 25], [3000, 3000], [4700, 3000]], fc=matplotlib.colors.to_rgba(AMBER, 0.14), ec=AMBER, lw=1))
    ax.text(3350, 35, "RED GIANTS", color=AMBER, fontsize=11, weight="bold", ha="right")
    ax.add_patch(Polygon([[30000, 2e4], [3000, 2e4], [3000, 6e5], [30000, 6e5]], fc=matplotlib.colors.to_rgba(RED, 0.10), ec=RED, lw=1))
    ax.text(20000, 3.3e5, "SUPERGIANTS", color=RED, fontsize=11, weight="bold")
    ax.add_patch(Polygon([[32000, 0.2], [6000, 0.0012], [6000, 0.0002], [32000, 0.02]], fc=matplotlib.colors.to_rgba(BLUE, 0.12), ec=BLUE, lw=1))
    ax.text(30000, 0.0042, "WHITE DWARFS", color=BLUE, fontsize=11, weight="bold", rotation=-24)
    ax.add_patch(Polygon([[7600, 8], [6300, 8], [5000, 1.5e4], [6100, 1.5e4]], fc=matplotlib.colors.to_rgba(PURPLE, 0.12), ec=PURPLE, lw=1, ls="--"))
    ax.text(8200, 1500, "instability\nstrip", color=PURPLE, fontsize=9.5, ha="right")
    for name, t, l, off in STARS:
        ax.plot(t, l, "o", color=AMBER if name == "Sun" else GREY, ms=7 if name == "Sun" else 4.5, zorder=5)
        ax.annotate(name, (t, l), xytext=off, textcoords="offset points", fontsize=9.5, color=GREY)
    for R, tx in ((0.01, 2450), (0.1, 2450), (1, 2450), (10, 2450), (100, 2450), (1000, 2450)):
        ly = R**2 * (tx / 5772) ** 4
        if 1e-4 < ly < 1e6:
            ax.text(tx, ly * 1.35, f"{R:g} R", fontsize=9, color=GREY, ha="right")
    ax.text(0.99, 0.015, "dotted lines: constant radius, in solar radii (L = 4πR²σT⁴)", transform=ax.transAxes, ha="right", fontsize=9.5, color=GREY)
    save(fig, "stellar-evolution-hr-diagram.svg")


SUN_TRACK = [  # label, age (billion years), T, L, R   — model values after Sackmann, Boothroyd & Kraemer (1993)
    ("arrives on the main sequence", 0.0, 5590, 0.70, 0.9),
    ("today", 4.57, 5772, 1.00, 1.0),
    ("core hydrogen gone", 10.9, 5520, 2.2, 1.6),
    ("tip of the red-giant branch", 12.17, 3110, 2350, 166),
    ("core helium burning", 12.2, 4720, 44, 10),
    ("second climb: shells burning", 12.3, 3160, 3000, 180),
]


def sun_track():
    fig, ax = plt.subplots(figsize=(10, 8.4))
    hr_axes(ax)
    ax.set_ylim(1e-4, 3e4)
    M, T, L = main_sequence_curve()
    ax.plot(T, L, color=GREEN, lw=8, alpha=0.18, solid_capstyle="round")
    t = [p[2] for p in SUN_TRACK]; l = [p[3] for p in SUN_TRACK]
    ax.plot(t, l, color=AMBER, lw=2.2)
    wd = [(3160, 3000), (30000, 3000), (100000 * 0 + 38000, 200), (30000, 0.3), (12000, 0.004), (6000, 0.0003)]
    ax.plot([p[0] for p in wd], [p[1] for p in wd], color=BLUE, lw=2, ls="--")
    offs = [(24, -34), (-130, -14), (22, 6), (-160, 8), (-130, -14), (12, 8)]
    for (name, age, tt, ll, R), off in zip(SUN_TRACK, offs):
        ax.plot(tt, ll, "o", color=AMBER, ms=6, zorder=5)
        ax.annotate(f"{name}\n{age:g} Gyr, {R:g} R", (tt, ll), xytext=off, textcoords="offset points", fontsize=9.5, color=GREY,
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6, shrinkB=4))
    ax.annotate("outer layers thrown off:\na planetary nebula;\nthe bare core crosses\nto the left in ~10 000 yr", (24000, 3000), xytext=(-10, -62), textcoords="offset points", fontsize=9.5, color=BLUE)
    ax.annotate("white dwarf, 0.54 M:\nno fuel, cooling for ever", (12000, 0.004), xytext=(10, 0), textcoords="offset points", fontsize=9.5, color=BLUE)
    ax.text(3950, 0.012, "main sequence", color=GREEN, fontsize=10.5, ha="right")
    save(fig, "stellar-evolution-sun-track.svg")


def lifetimes():
    with contextlib.redirect_stdout(io.StringIO()):
        coal, kh, fusion = model.what_powers_the_sun()
    fig, (a, b) = plt.subplots(2, 1, figsize=(10, 8.6), gridspec_kw={"height_ratios": [1, 1.5], "hspace": 0.42})
    names = ["a Sun made of coal\nand oxygen", "a Sun shrinking under\nits own gravity", "a Sun fusing the hydrogen\nin its core"]
    vals = [coal, kh, fusion]
    a.barh(names, vals, color=[matplotlib.colors.to_rgba(c_, 0.35) for c_ in (RED, AMBER, GREEN)], edgecolor=[RED, AMBER, GREEN], lw=1.5, height=0.55)
    a.set_xscale("log"); a.set_xlim(1e2, 1e12); a.invert_yaxis()
    for v, n in zip(vals, ("5 000 years", "30 million years", "10 billion years")):
        a.text(v * 1.5, vals.index(v), n, va="center", fontsize=10.5, color=GREY)
    a.axvline(4.57e9, color=TEAL, lw=1.5, ls="--")
    a.text(4.57e9 * 0.8, -0.62, "age of the Earth's oldest\nmeteorites: 4.57 billion years", ha="right", va="bottom", color=TEAL, fontsize=9.5)
    a.set_xlabel("how long the fuel could keep the Sun shining at today's power / years")
    a.set_title("Three candidate fuels", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right"):
        a.spines[s].set_visible(False); b.spines[s].set_visible(False)
    M = np.logspace(-1, np.log10(40), 100)
    L = np.where(M > 0.43, M**3.5, 0.363 * M**2.3)
    b.plot(M, 10e9 * M / L, color=PURPLE, lw=2.2)
    b.axhline(13.8e9, color=TEAL, lw=1.5, ls="--"); b.text(38, 13.8e9 * 1.35, "age of the Universe", color=TEAL, fontsize=9.5, ha="right")
    for m, name in ((0.12, "Proxima Centauri"), (1, "Sun"), (2.06, "Sirius A"), (18, "Betelgeuse")):
        l = m**3.5 if m > 0.43 else 0.363 * m**2.3
        t = 10e9 * m / l
        words = f"{t/1e9:.0f} billion years" if t >= 1e9 else f"{t/1e6:.0f} million years"
        b.plot(m, t, "o", color=AMBER, ms=6)
        b.annotate(f"{name}\n{words}", (m, t), xytext=(9, -26) if m < 0.5 else (9, 5), textcoords="offset points", fontsize=9.5, color=GREY)
    b.set_xscale("log"); b.set_yscale("log"); b.set_xlabel("mass / mass of the Sun"); b.set_ylabel("main-sequence lifetime / years"); b.set_ylim(5e5, 5e12)
    b.set_title("Ten times the fuel, three thousand times the spending", color=GREY, fontsize=12, loc="left")
    save(fig, "stellar-evolution-lifetimes.svg")


def white_dwarfs():
    with contextlib.redirect_stdout(io.StringIO()):
        out = model.white_dwarfs()
    fig, ax = plt.subplots(figsize=(10, 6.2))
    ax.plot(out[:, 0], out[:, 1] * model.R_SUN / 6.371e6, color=BLUE, lw=2.2, label="computed: gravity against degenerate electrons")
    ax.axvline(out[-1, 0], color=RED, lw=1.5, ls="--")
    ax.text(out[-1, 0] - 0.015, 2.9, f"Chandrasekhar limit\n{out[-1,0]:.2f} solar masses:\nno radius balances", ha="right", color=RED, fontsize=10)
    for name, m, r, off in (("Sirius B", 1.018, 0.0084, (8, -16)), ("40 Eridani B", 0.573, 0.0140, (8, 6)), ("Procyon B", 0.602, 0.01234, (8, -14))):
        ax.plot(m, r * model.R_SUN / 6.371e6, "o", color=AMBER, ms=7, zorder=5)
        ax.annotate(name, (m, r * model.R_SUN / 6.371e6), xytext=off, textcoords="offset points", fontsize=10, color=GREY)
    ax.axhline(1, color=GREY, lw=0.8, ls=":"); ax.text(0.03, 1.06, "the size of the Earth", fontsize=9.5, color=GREY)
    ax.set_xlim(0, 1.6); ax.set_ylim(0, 3.6)
    ax.set_xlabel("mass / mass of the Sun"); ax.set_ylabel("radius / radius of the Earth")
    ax.set_title("A heavier white dwarf is a smaller one", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, loc="upper center", labelcolor=GREY, fontsize=10)
    save(fig, "stellar-evolution-white-dwarfs.svg")


def parallax():
    fig, ax = plt.subplots(figsize=(10, 4.3))
    ax.set_xlim(0, 10); ax.set_ylim(-0.35, 4.3); ax.axis("off"); ax.set_aspect("equal")
    sun, e1, e2, star = (1.4, 2.15), (1.4, 3.35), (1.4, 0.95), (7.2, 2.15)
    ax.add_patch(Circle(sun, 1.2, fc="none", ec=GREY, lw=1, ls=":"))
    ax.add_patch(Circle(sun, 0.16, fc=AMBER, ec=AMBER)); ax.text(1.0, 2.15, "Sun", ha="right", va="center")
    for p, lab, va in ((e1, "Earth in January", "bottom"), (e2, "Earth in July", "top")):
        ax.add_patch(Circle(p, 0.09, fc=BLUE, ec=BLUE))
        ax.text(p[0] + 0.2, p[1] + (0.22 if va == "bottom" else -0.22), lab, va=va, fontsize=10)
        ax.plot([p[0], 9.9], [p[1], star[1] + (star[1] - p[1]) * (9.9 - star[0]) / (star[0] - p[0])], color=BLUE, lw=1)
    ax.plot(*star, "*", color=RED, ms=16); ax.text(7.2, 2.55, "nearby star", ha="center", color=RED, fontsize=10)
    ax.plot([sun[0], star[0]], [sun[1], star[1]], color=GREY, lw=1, ls="--")
    ax.text(4.4, 2.27, "distance d", ha="center", fontsize=10.5)
    ax.annotate("", (1.25, 3.35), (1.25, 2.15), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.4))
    ax.text(1.18, 2.75, "1 AU", ha="right", color=GREEN, fontsize=10)
    ax.text(6.05, 2.3, "p", color=PURPLE, fontsize=13, style="italic")
    ax.plot([9.9, 9.9], [0.3, 4.0], color=GREY, lw=3, alpha=0.4)
    ax.text(9.8, 4.12, "distant stars", ha="right", fontsize=9.5)
    ax.text(5.4, -0.2, "tan p = 1 AU / d.   With p in arcseconds and d in parsecs:  d = 1 / p", ha="center", fontsize=11, color=GREY)
    save(fig, "stellar-evolution-parallax.svg")


if __name__ == "__main__":
    lifecycle(); hr_diagram(); sun_track(); lifetimes(); white_dwarfs(); parallax()

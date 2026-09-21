"""Thermal Expansion — the numbers and the four figures.

1. well()          — WHY heating makes matter bigger.  A particle bound to its neighbour sits in a
                     potential well that is steep on the near side and gentle on the far side.  Give it
                     more energy and its time-averaged position moves outward.  In a perfectly symmetric
                     (parabolic) well the average does not move at all: no asymmetry, no expansion.
2. magnitudes()    — fractional volume change per kelvin for solids, liquids and gases.
3. engineering()   — the Eiffel Tower, a bridge gap, a sagging power line, a rail that is not allowed to
                     expand, a bimetallic strip.
4. water()         — the density of water from 0 to 10 °C, with its maximum at 4 °C.
5. sea_level()     — thermal expansion of the upper ocean.

Run:  python3 thermal-expansion-model.py      (numpy + matplotlib; writes four SVGs beside this script)
"""
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
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
    print("  wrote", name)


def lennard_jones(r):
    return 4 * (r**-12 - r**-6)                      # depth 1, minimum at r0 = 2^(1/6)


def time_average(U, r_grid, E):
    """Mean position of a particle of total energy E in the well U: weight each r by the time spent
    there, dt = dr / v, v = sqrt(2 (E - U))."""
    inside = U < E
    v = np.sqrt(2 * (E - U[inside]))
    w = 1 / v
    return np.sum(r_grid[inside] * w) / np.sum(w), r_grid[inside][0], r_grid[inside][-1]


def well():
    r0 = 2 ** (1 / 6)
    r = np.linspace(0.9, 3.0, 400_001)
    U = lennard_jones(r)
    k = 57.15 / r0**2 * 1.0                           # curvature of LJ at the minimum: U'' = 57.15 / r0^2
    Up = -1 + 0.5 * k * (r - r0) ** 2
    levels = [-0.9, -0.7, -0.5, -0.3]
    fig, axes = plt.subplots(2, 1, figsize=(10, 9), gridspec_kw={"hspace": 0.32})
    for ax, pot, name in ((axes[0], U, "real bond: steep wall on the near side, gentle slope on the far side"),
                          (axes[1], Up, "imaginary symmetric bond (a perfect spring)")):
        ax.plot(r, pot, color=BLUE, lw=2.2)
        print(f"  {name}")
        for E in levels:
            mean, lo, hi = time_average(pot, r, E)
            ax.plot([lo, hi], [E, E], color=AMBER, lw=1.6)
            ax.plot(mean, E, "o", color=RED, ms=7, zorder=5)
            print(f"    energy {E:+.1f}: swings between {lo:.3f} and {hi:.3f}; average separation {mean:.4f}  ({100*(mean-r0)/r0:+.2f} %)")
        ax.axvline(r0, color=GREY, lw=0.9, ls=":")
        ax.set_xlim(0.95, 1.75); ax.set_ylim(-1.08, 0.05)
        ax.set_ylabel("potential energy / well depth"); ax.set_title(name, color=GREY, fontsize=12, loc="left")
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[0].text(1.47, -0.85, "red dots: average separation\nat each energy; they drift outward", fontsize=10)
    axes[1].text(1.42, -0.75, "the dots stay put:\nno asymmetry, no expansion", fontsize=10)
    axes[1].set_xlabel("separation of two neighbouring particles (in units where the force is zero at 1.12)")
    save(fig, "thermal-expansion-well.svg")


BETA = [("invar (iron–nickel alloy)", 3 * 1.2e-6, "solid"), ("Pyrex glass", 3 * 3.3e-6, "solid"), ("ordinary glass", 3 * 9e-6, "solid"),
        ("concrete", 3 * 12e-6, "solid"), ("steel", 3 * 12e-6, "solid"), ("brass", 3 * 19e-6, "solid"), ("aluminium", 3 * 23e-6, "solid"),
        ("mercury", 1.8e-4, "liquid"), ("water (at 20 °C)", 2.1e-4, "liquid"), ("ethanol", 1.1e-3, "liquid"),
        ("any gas at 20 °C, constant pressure", 1 / 293.15, "gas")]


def magnitudes():
    for name, b, state in BETA:
        print(f"  {name:38s} {state:6s} volume grows by {b*1e6:7.0f} parts per million per kelvin")
    print(f"  steel : water : air  =  1 : {2.1e-4/3.6e-5:.0f} : {1/293.15/3.6e-5:.0f}")
    fig, ax = plt.subplots(figsize=(10, 5.6))
    cols = {"solid": BLUE, "liquid": TEAL, "gas": RED}
    names = [n for n, _, _ in BETA][::-1]; vals = [b * 1e6 for _, b, _ in BETA][::-1]; st = [s for _, _, s in BETA][::-1]
    ax.barh(names, vals, color=[matplotlib.colors.to_rgba(cols[s], 0.35) for s in st], edgecolor=[cols[s] for s in st], lw=1.4, height=0.62)
    for i, v in enumerate(vals):
        ax.text(v * 1.12, i, f"{v:,.0f}".replace(",", " "), va="center", fontsize=10)
    ax.set_xscale("log"); ax.set_xlim(2, 2e4)
    ax.set_xlabel("increase in volume per kelvin / parts per million (log scale)")
    ax.set_title("Solids least, liquids more, gases most", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "thermal-expansion-magnitudes.svg")


def engineering():
    a_steel, a_brass, a_al = 12e-6, 19e-6, 23e-6
    print(f"  Eiffel Tower, 300 m of iron, winter -5 °C to summer 35 °C: {300*a_steel*40*100:.0f} cm taller")
    print(f"  a 100 m steel bridge deck over the same range: {100*a_steel*40*1000:.0f} mm, the width of its expansion joint")
    L, dT = 300.0, 40.0
    dL = L * a_al * dT
    sag0 = 6.0
    arc = L + 8 * sag0**2 / (3 * L)
    sag1 = np.sqrt(3 * L * (arc + dL - L) / 8)
    print(f"  300 m aluminium power line, 6.0 m of sag in winter: {dL*100:.0f} cm longer in summer, and the sag becomes {sag1:.1f} m")
    E = 200e9
    print(f"  a steel rail NOT allowed to expand, heated by 40 K: stress = E alpha dT = {E*a_steel*40/1e6:.0f} MPa, "
          f"a force of {E*a_steel*40*7.7e-3/1e3:.0f} kN in a standard rail (77 cm^2): this is what buckles track")
    h, Lstrip, dT = 1.0e-3, 0.10, 50.0
    kappa = 1.5 * (a_brass - a_steel) * dT / h
    print(f"  brass-steel bimetallic strip, 1 mm thick, 10 cm long, heated 50 K: bends to a radius of {1/kappa:.1f} m, "
          f"tip moves {Lstrip**2*kappa/2*1000:.1f} mm; the two metals differ in length by only {Lstrip*(a_brass-a_steel)*dT*1e6:.0f} micrometres")
    # bimetallic figure
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(Rectangle((0.6, 3.0), 0.35, 1.0, fc=matplotlib.colors.to_rgba(GREY, 0.3), ec=GREY))
    ax.add_patch(Rectangle((0.95, 3.55), 3.4, 0.14, fc=matplotlib.colors.to_rgba(AMBER, 0.5), ec=AMBER))
    ax.add_patch(Rectangle((0.95, 3.41), 3.4, 0.14, fc=matplotlib.colors.to_rgba(BLUE, 0.4), ec=BLUE))
    ax.text(2.6, 4.0, "cold: straight", ha="center", fontsize=11)
    ax.text(4.5, 3.62, "brass", color=AMBER, fontsize=10, va="center"); ax.text(4.5, 3.4, "steel", color=BLUE, fontsize=10, va="center")
    ax.add_patch(Rectangle((0.6, 0.9), 0.35, 1.0, fc=matplotlib.colors.to_rgba(GREY, 0.3), ec=GREY))
    s = np.linspace(0, 3.4, 60); R = 5.0
    for off, col in ((-0.07, AMBER), (0.07, BLUE)):      # brass on the OUTSIDE of the curve (larger radius)
        x = 0.95 + (R - off) * np.sin(s / R); y = 1.48 - R + (R - off) * np.cos(s / R) + 0 * s
        ax.plot(x, y + off * 0 , color=col, lw=5, solid_capstyle="butt", alpha=0.75)
    ax.text(2.4, 2.1, "hot: brass grows more, so it takes the outside of the curve", ha="center", fontsize=11)
    ax.plot([6.2, 9.4], [3.48, 3.48], color=GREY, lw=1); ax.plot([6.2, 6.2], [3.48, 1.2], color=GREY, lw=1)
    ax.add_patch(Rectangle((6.2, 1.05), 1.0, 0.3, fc=matplotlib.colors.to_rgba(RED, 0.3), ec=RED)); ax.text(6.7, 0.78, "heater", ha="center", fontsize=10, color=RED)
    ax.plot([7.2, 9.4], [1.2, 1.2], color=GREY, lw=1); ax.plot([9.4, 9.4], [1.2, 2.2], color=GREY, lw=1)
    ax.plot([9.4, 9.4], [3.48, 2.75], color=GREY, lw=1)
    ax.plot([9.4, 9.15], [2.75, 2.25], color=AMBER, lw=4); ax.plot([9.4], [2.2], "o", color=GREY, ms=5)
    ax.text(9.0, 2.5, "strip bends away\nfrom the contact:\ncircuit breaks", ha="right", va="center", fontsize=10)
    ax.text(7.8, 3.75, "a thermostat", ha="center", fontsize=11)
    ax.text(7.8, 0.25, "it cools, straightens, touches again: the temperature is held", ha="center", fontsize=10)
    save(fig, "thermal-expansion-bimetallic.svg")


def water():
    T = np.linspace(0, 10, 201)
    # Kell (1975) polynomial for the density of air-free water, kg/m^3
    rho = (999.83952 + 16.945176 * T - 7.9870401e-3 * T**2 - 46.170461e-6 * T**3 + 105.56302e-9 * T**4 - 280.54253e-12 * T**5) / (1 + 16.879850e-3 * T)
    i = rho.argmax()
    print(f"  maximum density {rho[i]:.3f} kg/m^3 at {T[i]:.1f} °C;  at 0 °C {rho[0]:.3f};  at 10 °C {rho[-1]:.3f};  ice at 0 °C 916.7")
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.plot(T, rho, color=BLUE, lw=2.4)
    ax.plot(T[i], rho[i], "o", color=RED, ms=8); ax.annotate(f"densest at {T[i]:.0f} °C", (T[i], rho[i]), xytext=(-44, -30), textcoords="offset points", fontsize=10.5)
    ax.annotate("cooling below 4 °C makes water\nEXPAND, so the coldest water floats", (1, rho[20]), xytext=(0.3, 999.72), fontsize=10.5,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.set_xlabel("temperature / °C"); ax.set_ylabel("density of water / kg m⁻³")
    ax.set_title("Water breaks the rule between 0 and 4 °C", color=GREY, fontsize=12, loc="left")
    ax.ticklabel_format(useOffset=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "thermal-expansion-water.svg")


def sea_level():
    depth, beta, dT = 700.0, 2.0e-4, 0.5
    print(f"  warm the top {depth:.0f} m of ocean by {dT} K: it stands {depth*beta*dT*100:.0f} cm taller, with no ice melted at all")


if __name__ == "__main__":
    for i, f in enumerate((well, magnitudes, engineering, water, sea_level), 1):
        print(f"\n{i}. {f.__name__}")
        f()

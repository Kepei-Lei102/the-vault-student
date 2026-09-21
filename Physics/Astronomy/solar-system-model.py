"""The Solar System — every number in the card computed from measured data, and the six figures.

1. planets()      — from each planet's mass, radius, orbit radius and period: density, surface g,
                    orbital speed v = 2 pi r / T, light-travel time from the Sun; then two checks that
                    nobody told the planets about: T^2 / r^3 is the same for all, and v * sqrt(r) too.
2. sun_share()    — what fraction of the Solar System's mass is the Sun.
3. seasons()      — noon Sun height, day length and daily sunshine energy for Chengdu at the two
                    solstices, against the 7 % effect of the Earth's changing distance.
4. moon()         — 27.3 days to orbit, 29.5 days from full Moon to full Moon: why they differ.
5. comet()        — Halley's comet: perihelion and aphelion speeds, and the energy ledger at both.
6. frost_line()   — temperature of a small dark body against distance: where water freezes.
7. spin_up()      — a cloud shrinking under gravity must spin faster: the accretion disc.
8. tilts()        — how flat the system is: orbital tilts of the planets against those of bodies
                    scattered after the gas had gone.

Run:  python3 solar-system-model.py     (numpy + matplotlib; writes six SVGs beside this script)
"""
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, Wedge

HERE = os.path.dirname(os.path.abspath(__file__))
GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": GREY, "axes.labelcolor": GREY, "axes.edgecolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "font.size": 11, "svg.fonttype": "none", "font.family": "DejaVu Sans"})
G, c, AU, YEAR, M_SUN = 6.674e-11, 2.998e8, 1.496e11, 365.25 * 86400, 1.989e30

# name, orbit radius / AU, period / years, mass / 1e24 kg, mean radius / km, mean surface (or cloud-top) temperature / °C, moons
PLANETS = [("Mercury", 0.387, 0.2408, 0.330, 2439.7, 167, 0), ("Venus", 0.723, 0.6152, 4.87, 6051.8, 464, 0),
           ("Earth", 1.000, 1.0000, 5.97, 6371.0, 15, 1), ("Mars", 1.524, 1.8808, 0.642, 3389.5, -65, 2),
           ("Jupiter", 5.204, 11.862, 1898, 69911, -110, 95), ("Saturn", 9.583, 29.457, 568, 58232, -140, 146),
           ("Uranus", 19.19, 84.01, 86.8, 25362, -195, 28), ("Neptune", 30.07, 164.8, 102, 24622, -200, 16)]


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)
    s = open(path).read()
    s = re.sub(r'<svg([^>]*?) width="[^"]*" height="[^"]*"', r'<svg\1 width="100%"', s, count=1)
    open(path, "w").write(s)
    print("  wrote", name)


def derived():
    rows = []
    for name, a, T, m, R, temp, moons in PLANETS:
        M, Rm, r, Ts = m * 1e24, R * 1e3, a * AU, T * YEAR
        rows.append(dict(name=name, a=a, T=T, temp=temp, moons=moons, R=R, rho=M / (4 / 3 * np.pi * Rm**3), g=G * M / Rm**2,
                         v=2 * np.pi * r / Ts, light=r / c, kepler=T**2 / a**3, vroot=2 * np.pi * r / Ts * np.sqrt(a)))
    return rows


def planets():
    print("   planet    r/AU   T/yr   density  surface g  speed    light from Sun   T^2/r^3   v*sqrt(r)")
    for p in derived():
        print(f"   {p['name']:8s} {p['a']:6.3f} {p['T']:7.3f}  {p['rho']:6.0f}    {p['g']:5.1f}    {p['v']/1e3:5.1f} km/s   {p['light']/60:6.1f} min      "
              f"{p['kepler']:.3f}     {p['vroot']/1e3:.1f}")
    print("   the last two columns are constant: one star's gravity sets every orbit (see Gravitational Fields)")
    print(f"   Earth to Moon, 3.84e8 m: {3.84e8/c:.2f} s;  Sun to Neptune: {30.07*AU/c/3600:.1f} h;  Sun to Proxima Centauri: 4.2 YEARS")


def sun_share():
    planets_mass = sum(p[3] for p in PLANETS) * 1e24
    print(f"   all eight planets together: {planets_mass:.3e} kg = {100*planets_mass/(M_SUN+planets_mass):.3f} % of the total; "
          f"Jupiter alone is {100*1898e24/planets_mass:.0f} % of that.  The Sun holds {100*M_SUN/(M_SUN+planets_mass):.2f} %.")


def sun_geometry(lat_deg, decl_deg):
    lat, d = np.radians(lat_deg), np.radians(decl_deg)
    noon = 90 - abs(lat_deg - decl_deg)
    h0 = np.arccos(np.clip(-np.tan(lat) * np.tan(d), -1, 1))            # sunset hour angle
    day_hours = 2 * np.degrees(h0) / 15
    daily = h0 * np.sin(lat) * np.sin(d) + np.cos(lat) * np.cos(d) * np.sin(h0)   # daily energy on flat ground, relative
    return noon, day_hours, daily


def seasons(lat=30.67):
    s = sun_geometry(lat, 23.44); w = sun_geometry(lat, -23.44)
    print(f"   Chengdu ({lat} °N), June solstice:     noon Sun {s[0]:.1f}° high, {s[1]:.1f} h of daylight")
    print(f"   Chengdu ({lat} °N), December solstice: noon Sun {w[0]:.1f}° high, {w[1]:.1f} h of daylight")
    print(f"   a beam 1 m wide covers {1/np.sin(np.radians(s[0])):.2f} m of ground in June and {1/np.sin(np.radians(w[0])):.2f} m in December")
    print(f"   daily sunshine energy on level ground, June : December = {s[2]/w[2]:.2f} : 1")
    print(f"   Earth is CLOSEST to the Sun on about 3 January (147.1 million km) and furthest on 4 July (152.1): "
          f"intensity changes by only {100*((152.1/147.1)**2-1):.1f} %, and in the wrong direction for northern seasons")
    return s, w


def moon():
    P, Y = 27.32, 365.25
    S = 1 / (1 / P - 1 / Y)
    print(f"   the Moon returns to the same stars in {P} days, but the Earth has moved {360*P/Y:.0f}° round the Sun meanwhile;")
    print(f"   to line up with the Sun again it needs 1/(1/{P} - 1/{Y}) = {S:.2f} days: the month of the phases")
    print(f"   its orbital speed: 2 pi (3.84e8) / ({P} days) = {2*np.pi*3.84e8/(P*86400):.0f} m/s")


def comet(a_au=17.83, e=0.967):
    a = a_au * AU
    rp, ra = a * (1 - e), a * (1 + e)
    vp, va = np.sqrt(G * M_SUN * (2 / rp - 1 / a)), np.sqrt(G * M_SUN * (2 / ra - 1 / a))
    print(f"   Halley: closest {rp/AU:.3f} AU, furthest {ra/AU:.1f} AU, period {a_au**1.5:.0f} years")
    print(f"   speed at closest approach {vp/1e3:.1f} km/s; at the far end {va/1e3:.2f} km/s: a factor of {vp/va:.0f}")
    for label, r, v in (("closest", rp, vp), ("furthest", ra, va)):
        ke, gpe = 0.5 * v**2, -G * M_SUN / r
        print(f"   per kilogram, {label:8s}: kinetic {ke/1e6:9.1f} MJ, gravitational {gpe/1e6:10.1f} MJ, total {(ke+gpe)/1e6:7.2f} MJ")
    return rp, ra, vp, va


def frost_line():
    r = np.array([0.39, 0.72, 1.0, 1.52, 2.7, 5.2, 9.6, 19.2, 30.1])
    T = 278.5 / np.sqrt(r)
    for ri, Ti in zip(r, T):
        print(f"   {ri:5.2f} AU: a small dark body settles at {Ti:4.0f} K ({Ti-273:5.0f} °C)")
    print(f"   water ice survives in a vacuum below about 170 K, which is beyond {(278.5/170)**2:.1f} AU: between Mars and Jupiter")


def spin_up():
    r0, r1 = 10_000.0, 50.0
    print(f"   a cloud shrinking from {r0:.0f} AU to {r1:.0f} AU across, keeping its angular momentum, turns {(r0/r1)**2:,.0f} times faster;")
    print("   along the spin axis nothing resists the fall, across it the spin does: the ball settles into a disc")


def tilts():
    """Measured orbital inclinations to the Earth's orbital plane, in degrees."""
    formed_in_the_disc = {"Mercury": 7.00, "Venus": 3.39, "Earth": 0.00, "Mars": 1.85, "Jupiter": 1.30, "Saturn": 2.49, "Uranus": 0.77, "Neptune": 1.77}
    scattered_later = {"Pluto": 17.2, "Eris": 44.0, "Halley's comet": 162.3, "comet Hale-Bopp": 89.4, "comet Hyakutake": 124.9}
    print(f"   planets: largest tilt {max(formed_in_the_disc.values()):.1f}° (Mercury), mean {np.mean(list(formed_in_the_disc.values())):.1f}°; "
          "the Sun's equator is about 6° from their common plane")
    for name, i in scattered_later.items():
        note = "  (more than 90°: it goes round backwards)" if i > 90 else ""
        print(f"   {name:18s} {i:6.1f}°{note}")
    print("   random directions would average 90°: the planets remember a disc, the comets do not")


# ------------------------------------------------------------------ figures
def fig_inventory():
    fig, (top, ax) = plt.subplots(2, 1, figsize=(10, 7.2), gridspec_kw={"height_ratios": [1, 1.25], "hspace": 0.25})
    top.set_xlim(0, 10); top.set_ylim(0, 3.2); top.axis("off"); top.set_aspect("equal")
    top.add_patch(Wedge((-6.6, 1.6), 7.3, -14, 14, fc=matplotlib.colors.to_rgba(AMBER, 0.35), ec=AMBER)); top.text(0.25, 1.6, "Sun", va="center", fontsize=11)
    x = 1.2
    cols = [GREY, AMBER, BLUE, RED, AMBER, AMBER, TEAL, BLUE]
    for (name, a, T, m, R, temp, moons), col in zip(PLANETS, cols):
        rad = R / 69911 * 0.95
        half = max(rad, 0.34)
        x += half
        top.add_patch(Circle((x, 1.6), rad, fc=matplotlib.colors.to_rgba(col, 0.4), ec=col, lw=1.2))
        if name == "Saturn":
            top.add_patch(Ellipse((x, 1.6), rad * 2.3 * 2 / 2 * 1.15, rad * 0.5, fc="none", ec=col, lw=1.2))
        top.text(x, 1.6 - rad - 0.22, name, ha="center", va="top", fontsize=9)
        x += half + (0.28 if name in ("Jupiter", "Saturn") else 0.1)
    top.text(2.55, 3.0, "rocky and small", ha="center", color=RED, fontsize=11); top.text(7.0, 3.0, "gaseous and large", ha="center", color=TEAL, fontsize=11)
    top.text(5.0, 0.0, "sizes to scale with each other (the Sun's edge is drawn to the same scale); distances are NOT", ha="center", fontsize=9.5)
    for name, a, *_ in PLANETS:
        ax.plot(a, 0, "o", color=BLUE, ms=6); ax.annotate(name, (a, 0), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9.5, rotation=55)
    ax.axvspan(2.1, 3.3, color=matplotlib.colors.to_rgba(GREY, 0.25)); ax.text(2.65, -0.5, "asteroid belt\n(Ceres, a dwarf\nplanet, 2.8 AU)", ha="center", va="top", fontsize=9.5)
    ax.axvspan(30, 50, color=matplotlib.colors.to_rgba(TEAL, 0.18)); ax.text(39, -0.5, "Kuiper belt:\nPluto (39 AU)\nand other\ndwarf planets", ha="center", va="top", fontsize=9.5)
    ax.plot([0.586, 35.1], [-0.25, -0.25], color=PURPLE, lw=2); ax.plot([0.586, 35.1], [-0.25, -0.25], "|", color=PURPLE, ms=10)
    ax.text(4.6, -0.21, "Halley's comet swings between 0.59 and 35 AU", color=PURPLE, fontsize=9.5, va="bottom", ha="center")
    ax.set_xscale("log"); ax.set_xlim(0.3, 70); ax.set_ylim(-1.45, 0.75); ax.set_yticks([])
    ax.set_xticks([0.3, 1, 3, 10, 30]); ax.set_xticklabels(["0.3", "1", "3", "10", "30"])
    ax.set_xlabel("average distance from the Sun / AU  (1 AU = 150 million km; each step to the right is about three times further)")
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    save(fig, "solar-system-inventory.svg")


def fig_seasons(s, w):
    fig = plt.figure(figsize=(10, 9.2))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1], hspace=0.22, wspace=0.18)
    ax = fig.add_subplot(gs[0, :]); ax.set_xlim(-5.4, 5.4); ax.set_ylim(-2.5, 2.9); ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(Ellipse((0, 0), 8.4, 3.0, fc="none", ec=GREY, ls=":", lw=1))
    ax.add_patch(Circle((0, 0), 0.32, fc=matplotlib.colors.to_rgba(AMBER, 0.6), ec=AMBER)); ax.text(0, -0.62, "Sun", ha="center", fontsize=10)
    tilt = np.radians(23.44)
    for (x, y), label, dx in (((-4.2, 0), "June: north pole\nleans towards the Sun.\nNorthern summer", -0.0), ((4.2, 0), "December: north pole\nleans away.\nNorthern winter", 0.0),
                              ((0, 1.5), "September", 0), ((0, -1.5), "March", 0)):
        ax.add_patch(Circle((x, y), 0.34, fc=matplotlib.colors.to_rgba(BLUE, 0.35), ec=BLUE))
        ax.plot([x - 0.62 * np.sin(tilt), x + 0.62 * np.sin(tilt)], [y - 0.62 * np.cos(tilt), y + 0.62 * np.cos(tilt)], color=RED, lw=1.6)   # top (north) leans RIGHT
        lit = Wedge((x, y), 0.34, 90 + np.degrees(np.arctan2(-y, -x)), 270 + np.degrees(np.arctan2(-y, -x)), fc=matplotlib.colors.to_rgba(GREY, 0.55), ec="none")
        ax.add_patch(lit)
        ax.text(x + (1.05 if x == 0 else 0), y + (0 if x == 0 else 1.2), label, ha="center", fontsize=9.5, va="center")
    ax.text(0, 2.7, "The axis (red) keeps pointing the same way in space all year: towards the right in this drawing", ha="center", fontsize=10)
    a = fig.add_subplot(gs[1, 0]); a.set_xlim(0, 10); a.set_ylim(0, 5); a.axis("off"); a.set_aspect("equal")
    for x0, alt, lab, col in ((0.2, s[0], f"June noon: Sun {s[0]:.0f}° high", AMBER), (5.3, w[0], f"December noon: Sun {w[0]:.0f}° high", BLUE)):
        th = np.radians(alt); width = 1.0 / np.sin(th)
        a.plot([x0, x0 + 4.4], [0.9, 0.9], color=GREY, lw=2)
        gx = x0 + 0.5
        for off in (0, width):
            a.plot([gx + off + 3.0 * np.cos(th), gx + off], [0.9 + 3.0 * np.sin(th), 0.9], color=col, lw=1.4)
        a.plot([gx, gx + width], [0.9, 0.9], color=RED, lw=5, solid_capstyle="butt")
        a.text(x0 + 2.2, 4.55, lab, ha="center", fontsize=9.5, color=col)
        a.text(x0 + 2.2, 0.3, f"1 m of beam lights {width:.2f} m", ha="center", fontsize=9.5)
    a.set_title("Same beam, more ground: weaker heating", color=GREY, fontsize=11, loc="left")
    b = fig.add_subplot(gs[1, 1])
    days = np.arange(365); decl = -23.44 * np.cos(2 * np.pi * (days + 10) / 365.25)
    hours = np.array([sun_geometry(30.67, d)[1] for d in decl])
    b.plot(days, hours, color=GREEN, lw=2.2); b.axhline(12, color=GREY, lw=0.8, ls=":")
    b.set_xticks([0, 79, 171, 265, 355]); b.set_xticklabels(["1 Jan", "20 Mar", "21 Jun", "23 Sep", "21 Dec"], fontsize=9.5)
    b.set_ylabel("hours of daylight, Chengdu"); b.set_title("and the day is longer too", color=GREY, fontsize=11, loc="left")
    for sp in ("top", "right"):
        b.spines[sp].set_visible(False)
    save(fig, "solar-system-seasons.svg")


def fig_moon():
    DARK, LIT = "#5a5a5a", "#f3f0d8"
    fig, ax = plt.subplots(figsize=(10, 8.6)); ax.set_xlim(-5.6, 6.6); ax.set_ylim(-5.9, 5.3); ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(Circle((0, 0), 0.55, fc=matplotlib.colors.to_rgba(BLUE, 0.35), ec=BLUE)); ax.text(0, 0, "Earth", ha="center", va="center", fontsize=9.5)
    ax.add_patch(Circle((0, 0), 2.3, fc="none", ec=GREY, ls=":", lw=1))
    for y in np.linspace(-4.2, 4.2, 7):
        ax.annotate("", (5.3, y), (6.5, y), arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=1.3))
    ax.text(5.9, 4.8, "sunlight", color=AMBER, ha="center", fontsize=11)
    names = ["new Moon", "waxing crescent", "first quarter", "waxing gibbous", "full Moon", "waning gibbous", "last quarter", "waning crescent"]
    for k, name in enumerate(names):
        th = np.radians(45 * k); x, y = 2.3 * np.cos(th), 2.3 * np.sin(th)
        ax.add_patch(Circle((x, y), 0.3, fc=DARK, ec=GREY))
        ax.add_patch(Wedge((x, y), 0.3, -90, 90, fc=LIT, ec="none"))                # the half facing the Sun is always lit
        X, Y = 4.0 * np.cos(th), 4.0 * np.sin(th); Rm = 0.44
        f = (1 - np.cos(th)) / 2                                                     # fraction of the disc seen lit from the Earth
        ax.add_patch(Circle((X, Y), Rm, fc=DARK, ec=GREY))
        if 0 < f < 1:
            waxing = k < 4                                                           # waxing: lit on the right, seen from the northern hemisphere
            ax.add_patch(Wedge((X, Y), Rm, -90, 90, fc=LIT, ec="none") if waxing else Wedge((X, Y), Rm, 90, 270, fc=LIT, ec="none"))
            ax.add_patch(Ellipse((X, Y), 2 * Rm * abs(1 - 2 * f), 2 * Rm, fc=LIT if f > 0.5 else DARK, ec="none"))
        elif f == 1 or k == 4:
            ax.add_patch(Circle((X, Y), Rm, fc=LIT, ec=GREY))
        ax.add_patch(Circle((X, Y), Rm, fc="none", ec=GREY))
        ax.text(X, Y - 0.72, name, ha="center", va="center", fontsize=9.5)
    ax.text(0, -1.0, "inner ring: the Moon as it really is,\nhalf lit, always", ha="center", fontsize=9.5)
    ax.text(0, -5.7, "outer ring: what the Moon at that position looks like from the Earth (northern hemisphere)", ha="center", fontsize=9.5)
    ax.annotate("", (-1.63, 1.63), (-0.0, 2.3), arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1, connectionstyle="arc3,rad=0.25"))
    save(fig, "solar-system-moon-phases.svg")


def fig_speeds():
    d = derived()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    r = np.logspace(np.log10(0.3), np.log10(40), 100)
    ax.plot(r, 29.78 / np.sqrt(r), color=GREY, lw=1.2, ls="--", label="29.8 km/s ÷ √(distance in AU)")
    for p in d:
        ax.plot(p["a"], p["v"] / 1e3, "o", color=BLUE, ms=7)
        ax.annotate(f"{p['name']} {p['v']/1e3:.1f}", (p["a"], p["v"] / 1e3), xytext=(7, 5), textcoords="offset points", fontsize=9.5)
    ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlabel("average distance from the Sun / AU"); ax.set_ylabel("average orbital speed / km s⁻¹")
    ax.set_xticks([0.3, 1, 3, 10, 30]); ax.set_xticklabels(["0.3", "1", "3", "10", "30"]); ax.set_yticks([5, 10, 20, 50]); ax.set_yticklabels(["5", "10", "20", "50"]); ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter()); ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_title("Further from the Sun: weaker field, slower planet", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY)
    save(fig, "solar-system-speeds.svg")


def fig_comet():
    e, a = 0.8, 4.0
    b = a * np.sqrt(1 - e**2); cfoc = a * e
    fig, ax = plt.subplots(figsize=(10, 4.6)); ax.set_xlim(-7.4, 7.6); ax.set_ylim(-3.3, 3.1); ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(Ellipse((0, 0), 2 * a, 2 * b, fc="none", ec=PURPLE, lw=1.8))
    ax.add_patch(Circle((cfoc, 0), 0.22, fc=matplotlib.colors.to_rgba(AMBER, 0.7), ec=AMBER)); ax.text(cfoc, -0.5, "Sun, at a focus:\nNOT at the centre", ha="center", va="top", fontsize=9.5)
    ax.plot(0, 0, "+", color=GREY, ms=9); ax.text(0, 0.22, "centre of the ellipse", ha="center", fontsize=9)
    for th, scale, lab, off in ((0, 1.0, "closest: fastest", (0.1, 0.55)), (np.pi, 1.0, "furthest: slowest", (-1.0, -0.35))):
        x, y = a * np.cos(th), b * np.sin(th)
        r = np.hypot(x - cfoc, y); v = np.sqrt(2 / r - 1 / a)
        ax.plot(x, y, "o", color=PURPLE, ms=8)
        ax.annotate("", (x, y + (1 if th == 0 else -1) * 1.5 * v), (x, y), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
        ax.text(x + off[0], y + (1 if th == 0 else -1) * (1.5 * v + 0.25), lab, ha="center", fontsize=10, color=RED)
    for x0, ke, lab in ((6.3, 0.9, "near the Sun"), (-6.9, 0.1, "far away")):
        ax.bar([x0, x0 + 0.35], [2.2 * ke, 2.2 * (1 - ke)], width=0.3, bottom=-3.0, color=[matplotlib.colors.to_rgba(RED, 0.5), matplotlib.colors.to_rgba(BLUE, 0.5)], edgecolor=[RED, BLUE])
        ax.text(x0 + 0.17, -0.45, f"{lab}\nKE  GPE", ha="center", fontsize=9)
    ax.text(0.0, -3.2, "kinetic + gravitational potential energy stays the same all the way round", ha="center", fontsize=10)
    save(fig, "solar-system-comet.svg")


def fig_frost():
    d = derived()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    names = [p["name"] for p in d]; rho = [p["rho"] for p in d]
    cols = [RED] * 4 + [TEAL] * 4
    ax.bar(names, rho, color=[matplotlib.colors.to_rgba(c_, 0.35) for c_ in cols], edgecolor=cols, lw=1.4)
    for i, v in enumerate(rho):
        ax.text(i, v + 90, f"{v:.0f}", ha="center", fontsize=10)
    ax.axhline(1000, color=BLUE, lw=1, ls=":"); ax.set_xlim(-0.6, 8.6); ax.text(7.5, 1060, "water:\n1000", color=BLUE, fontsize=9.5, ha="left")
    ax.axvline(3.5, color=GREY, lw=1.4, ls="--"); ax.text(3.55, 5300, "the frost line, about 2.7 AU:\nbeyond it ice could freeze out and\nplanets grew big enough to hold gas", fontsize=10, va="top")
    ax.set_ylabel("average density / kg m⁻³"); ax.set_ylim(0, 6200)
    ax.set_title("Four dense rocky planets, then four giants of low density", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "solar-system-densities.svg")


if __name__ == "__main__":
    print("1. planets"); planets()
    print("\n2. the Sun's share"); sun_share()
    print("\n3. seasons"); s, w = seasons()
    print("\n4. the Moon"); moon()
    print("\n5. a comet"); comet()
    print("\n6. the frost line"); frost_line()
    print("\n7. spin-up"); spin_up()
    print("\n8. tilts"); tilts()
    print("\nfigures")
    fig_inventory(); fig_seasons(s, w); fig_moon(); fig_speeds(); fig_comet(); fig_frost()

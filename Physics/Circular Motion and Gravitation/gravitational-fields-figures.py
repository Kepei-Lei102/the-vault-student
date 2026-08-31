"""Figures for [[Gravitational Fields]] — matplotlib, vault palette, light/dark-safe.
Every curve and arrow is computed (real Earth / Solar-System numbers); nothing placed by eye.
(mathtext avoids \\vec, \\to, \\perp, \\Rightarrow, \\tfrac — no glyphs in the SVG fonts.)

  gravitational-fields-lines.svg        radial field of a sphere (arrows inward), dashed
                                        equipotential circles, and the uniform-field view of
                                        a small patch near the surface
  gravitational-fields-g-and-phi.svg    two rows: g(r) = GM/r² outside the Earth (with the
                                        linear inside-a-uniform-sphere law dashed) and the
                                        shaded area that equals Δφ; φ(r) = −GM/r — the well,
                                        the gradient g = −dφ/dr, the mgh tangent near the surface
  gravitational-fields-orbit-energy.svg two rows: KE, PE and total energy of a circular orbit
                                        against r (the lower-is-faster-yet-poorer paradox; ISS,
                                        GPS, geostationary marked); Kepler III from the eight
                                        planets on log–log axes, slope 3/2

Run from this folder:  python3 gravitational-fields-figures.py
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

GREY = "#888888"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
RED = "#dc2626"
AMBER = "#f59e0b"
TEAL = "#0891b2"

plt.rcParams.update({
    "font.family": "Helvetica Neue", "font.size": 11,
    "text.color": GREY, "axes.labelcolor": GREY, "axes.edgecolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY,
    "axes.facecolor": "none", "figure.facecolor": "none",
    "savefig.facecolor": "none", "savefig.transparent": True,
    "svg.fonttype": "none", "axes.spines.top": False, "axes.spines.right": False,
})

G = 6.674e-11
ME, RE = 5.972e24, 6.371e6
GM = G * ME


def arrow(ax, p, q, color, lw=2.0, ms=12, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms, color=color,
                                 lw=lw, shrinkA=0, shrinkB=0, linestyle=ls))


# ================================================================ field lines
def field_lines():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 12.5))
    for ax in (ax1, ax2):
        ax.set_aspect("equal"); ax.axis("off")
    ax1.set_xlim(-3.4, 3.4); ax1.set_ylim(-4.6, 3.5)
    R = 1.0
    ax1.add_patch(Circle((0, 0), R, color=BLUE, alpha=0.25))
    ax1.add_patch(Circle((0, 0), R, fill=False, color=BLUE, lw=1.5))
    ax1.text(0, 0, "M", color=BLUE, ha="center", va="center", fontsize=13)
    for k in range(16):
        a = 2 * np.pi * k / 16
        u = np.array([np.cos(a), np.sin(a)])
        arrow(ax1, 3.2 * u, 1.08 * u, AMBER, lw=1.6, ms=11)
    for rr, lab in ((1.6, r"$\varphi_1$"), (2.3, r"$\varphi_2$"), (3.0, r"$\varphi_3$")):
        ax1.add_patch(Circle((0, 0), rr, fill=False, color=GREY, lw=1.0, ls="--"))
        ax1.text(rr * np.cos(np.radians(22)) + 0.05, rr * np.sin(np.radians(22)) + 0.1, lab, color=GREY, fontsize=10)
    ax1.set_title("Radial field of a sphere: lines point in, crowd near the mass", color=GREY)
    ax1.text(0, -4.5, "field lines (amber) show the direction of the force on a test mass;\n"
             "their density shows its size — $g = GM/r^2$.  Dashed: equipotentials,\n"
             "always perpendicular to the lines; no work to move along one",
             color=GREY, fontsize=10, ha="center", va="bottom")

    # zoomed patch near the surface: uniform field
    ax2.set_xlim(-3.4, 3.4); ax2.set_ylim(-3.4, 4.6)
    ground_y = -2.2
    ax2.add_patch(Rectangle((-3.2, -3.3), 6.4, ground_y + 3.3, color=BLUE, alpha=0.2))
    ax2.plot([-3.2, 3.2], [ground_y, ground_y], color=BLUE, lw=1.5)
    ax2.text(0, ground_y - 0.55, "ground — a tiny patch of the sphere, so the lines look parallel", color=BLUE, fontsize=10, ha="center")
    for x in np.linspace(-2.8, 2.8, 9):
        arrow(ax2, (x, 3.1), (x, ground_y + 0.1), AMBER, lw=1.6, ms=11)
    for y, lab in ((-0.9, r"$\varphi = -62.5$ MJ/kg"), (0.4, r"$\varphi = -62.4$ MJ/kg"), (1.7, r"$\varphi = -62.3$ MJ/kg")):
        ax2.plot([-3.2, 3.2], [y, y], color=GREY, lw=1.0, ls="--")
        ax2.text(3.25, y, lab, color=GREY, fontsize=9, va="center")
    ax2.set_title("Near the surface: uniform — $g$ constant, equipotentials flat", color=GREY)
    ax2.text(0, 4.5, "$g$ falls by only 0.3 % per 10 km of height: for laboratory heights $g = 9.81$ N kg⁻¹ is constant,\n"
             "the equipotentials are horizontal planes 10 km apart here, and $\\Delta\\varphi = g\\,\\Delta h$ — which is where $mgh$ comes from",
             color=GREY, fontsize=9.5, ha="center", va="top")
    fig.tight_layout()
    fig.savefig("gravitational-fields-lines.svg")
    plt.close(fig)


# ================================================================ g(r) and phi(r)
def g_and_phi():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 10.5))
    r = np.linspace(0.05, 6, 600) * RE
    g_out = GM / r**2
    g_in = GM * r / RE**3
    g = np.where(r >= RE, g_out, g_in)
    x = r / RE
    ax1.plot(x[r >= RE], g_out[r >= RE], color=AMBER, lw=2.4, label=r"$g = GM/r^2$ (outside)")
    ax1.plot(x[r < RE], g_in[r < RE], color=AMBER, lw=1.6, ls="--", label=r"inside a uniform sphere: $g$ grows in proportion to $r$ (beyond syllabus)")
    ax1.axvline(1, color=GREY, lw=0.8, ls=":"); ax1.text(0.93, 9.3, "surface\n$r = R$", color=GREY, fontsize=9.5, ha="right")
    # shaded area between r1 and r2 = Δφ
    r1, r2 = 1.5, 3.0
    m = (x >= r1) & (x <= r2)
    ax1.fill_between(x[m], 0, g_out[m], color=GREEN, alpha=0.2)
    dphi = GM * (1 / (r1 * RE) - 1 / (r2 * RE))
    ax1.text(2.25, 1.9, f"area = $\\Delta\\varphi$\n= {dphi/1e6:.1f} MJ/kg\n(work per kg to\nclimb from $1.5R$ to $3R$)", color=GREEN, fontsize=9.5, ha="center")
    for xx, lab in ((1.066, "ISS"), (4.17, "GPS"), ):
        ax1.plot([xx], [GM / (xx * RE)**2], "o", color=BLUE, ms=5)
    ax1.text(1.22, 8.75, "ISS: 8.6 N/kg — 88 % of the surface value", color=BLUE, fontsize=9)
    ax1.text(4.2, 0.85, "GPS (4.2 R): 0.56 N/kg", color=BLUE, fontsize=9)
    ax1.set_xlim(0, 6); ax1.set_ylim(0, 10.5)
    ax1.set_xlabel("distance from the centre, $r / R_{\\rm Earth}$"); ax1.set_ylabel("field strength $g$ / N kg⁻¹")
    ax1.set_title("Field strength falls as the inverse square — and is nowhere near zero in orbit", color=GREY)
    ax1.legend(frameon=False, loc="upper right", labelcolor=GREY, fontsize=9.5)

    phi = -GM / r
    ax2.plot(x[r >= RE], phi[r >= RE] / 1e6, color=PURPLE, lw=2.4, label=r"$\varphi = -GM/r$")
    ax2.axhline(0, color=GREY, lw=0.8)
    ax2.axvline(1, color=GREY, lw=0.8, ls=":")
    # tangent at r = 1.8 R: gradient = -g there, i.e. slope of phi = +GM/r^2
    x0 = 1.8; phi0 = -GM / (x0 * RE) / 1e6; slope = GM / (x0 * RE)**2 * RE / 1e6   # MJ/kg per R
    xs = np.linspace(x0 - 0.7, x0 + 0.7, 2)
    ax2.plot(xs, phi0 + slope * (xs - x0), color=AMBER, lw=1.6, ls="--")
    ax2.plot([x0], [phi0], "o", color=AMBER, ms=5)
    ax2.text(x0 + 0.85, phi0 - 9.0, "gradient of $\\varphi$ at this point = $+g$ there:\n$g = -\\dfrac{d\\varphi}{dr}$ — the field is the\npotential's downhill slope", color=AMBER, fontsize=9.5, va="top")
    # mgh tangent at the surface
    xs2 = np.linspace(1, 1.6, 2)
    slope_s = GM / RE**2 * RE / 1e6
    ax2.plot(xs2, (-GM / RE / 1e6) + slope_s * (xs2 - 1), color=GREEN, lw=1.6, ls="--")
    ax2.text(0.3, -16, "straight-line (uniform-field)\napproximation at the surface:\n$\\Delta\\varphi \\approx g\\,h$, i.e. $\\Delta U \\approx mgh$\n— good while $h$ is much less than $R$", color=GREEN, fontsize=9.5, va="top")
    ax2.text(1.05, -GM / RE / 1e6 - 4.5, f"surface: $\\varphi = -{GM/RE/1e6:.1f}$ MJ/kg\n= the energy per kg to escape completely", color=PURPLE, fontsize=9.5, va="top")
    ax2.plot([1], [-GM / RE / 1e6], "o", color=PURPLE, ms=5)
    ax2.annotate("", xy=(5.6, -0.8), xytext=(5.6, -11.2), arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2))
    ax2.text(5.5, -6.0, "climbing out\nof the well", color=GREY, fontsize=9.5, ha="right", va="center")
    ax2.set_xlim(0, 6); ax2.set_ylim(-75, 6)
    ax2.set_xlabel("distance from the centre, $r / R_{\\rm Earth}$"); ax2.set_ylabel("potential $\\varphi$ / MJ kg⁻¹")
    ax2.set_title("Potential is negative everywhere and zero only at infinity: a well, not a hill", color=GREY)
    ax2.legend(frameon=False, loc="lower right", labelcolor=GREY, fontsize=10)
    fig.tight_layout()
    fig.savefig("gravitational-fields-g-and-phi.svg")
    plt.close(fig)


# ================================================================ orbit energy + Kepler III
def orbit_energy():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 10.5))
    x = np.linspace(1.0, 7.5, 500)
    r = x * RE
    KE = GM / (2 * r) / 1e6; PE = -GM / r / 1e6; E = -GM / (2 * r) / 1e6      # per kg, MJ
    ax1.plot(x, KE, color=GREEN, lw=2.2, label=r"kinetic  $\frac{1}{2}v^2 = \frac{GM}{2r}$")
    ax1.plot(x, PE, color=PURPLE, lw=2.2, label=r"potential  $-\frac{GM}{r}$")
    ax1.plot(x, E, color=AMBER, lw=2.6, label=r"total  $E = -\frac{GM}{2r}$")
    ax1.axhline(0, color=GREY, lw=0.8)
    for xx, lab in ((1.066, "ISS"), (4.17, "GPS"), (6.62, "geostationary")):
        ax1.axvline(xx, color=GREY, lw=0.7, ls=":")
        ax1.text(xx + 0.05, 3.5, lab, color=GREY, fontsize=9, rotation=90, va="bottom")
    ax1.text(4.2, 20, "lower orbit: faster (more KE) yet less total energy —\nto climb you must ADD energy, and you arrive slower;\nair drag removes energy, so the orbit sinks and the satellite speeds up", color=GREY, fontsize=10, ha="center")
    ax1.text(6.0, -28, "bound orbits have $E < 0$;\n$E = 0$ is exactly escape", color=AMBER, fontsize=10, ha="center")
    ax1.set_xlim(1, 7.5); ax1.set_ylim(-65, 35)
    ax1.set_xlabel("orbit radius $r / R_{\\rm Earth}$"); ax1.set_ylabel("energy per kg / MJ kg⁻¹")
    ax1.set_title("Energy of a circular orbit: KE is always half the size of PE, and the total is negative", color=GREY)
    ax1.legend(frameon=False, loc="lower right", labelcolor=GREY, fontsize=9.5)

    planets = {"Mercury": (0.387, 0.2408), "Venus": (0.723, 0.6152), "Earth": (1.0, 1.0), "Mars": (1.524, 1.881),
               "Jupiter": (5.203, 11.86), "Saturn": (9.537, 29.46), "Uranus": (19.19, 84.01), "Neptune": (30.07, 164.8)}
    a = np.array([v[0] for v in planets.values()]); T = np.array([v[1] for v in planets.values()])
    aa = np.logspace(-0.6, 1.7, 50)
    ax2.plot(aa, aa ** 1.5, color=GREY, lw=1.2, ls="--", label=r"$T = a^{3/2}$  (slope $\frac{3}{2}$ on log–log)")
    ax2.plot(a, T, "o", color=BLUE, ms=7)
    for name, (aa_, TT) in planets.items():
        dx = 1.12 if name not in ("Venus", "Mars") else 0.62
        ax2.text(aa_ * dx, TT * (1.0 if name not in ("Venus", "Mars") else 1.25), name, color=BLUE, fontsize=9, va="center")
    ax2.set_xscale("log"); ax2.set_yscale("log")
    ax2.set_xlim(0.25, 60); ax2.set_ylim(0.15, 400)
    ax2.set_xlabel("mean orbital radius $a$ / AU"); ax2.set_ylabel("orbital period $T$ / years")
    ax2.set_title("Kepler's third law from the real Solar System: $T^2/a^3 = 1.000 \\pm 0.002$ for all eight planets", color=GREY)
    ax2.text(0.3, 150, "$T^2 = \\dfrac{4\\pi^2}{GM_{\\rm Sun}}\\,a^3$ — one constant for everything\norbiting the same central mass", color=GREY, fontsize=10, va="top")
    ax2.legend(frameon=False, loc="lower right", labelcolor=GREY, fontsize=10)
    fig.tight_layout()
    fig.savefig("gravitational-fields-orbit-energy.svg")
    plt.close(fig)


if __name__ == "__main__":
    field_lines()
    g_and_phi()
    orbit_energy()
    print("ok")

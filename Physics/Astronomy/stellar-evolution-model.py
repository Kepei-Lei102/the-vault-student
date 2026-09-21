"""Stellar Evolution — every number in the card, computed.

1. sunlight()          — what fraction of a 5772 K blackbody's power is ultraviolet, visible, infrared.
2. light_year()        — the light-year and the parsec from their definitions.
3. what_powers_the_sun() — three candidate fuels, three lifetimes: coal, gravitational contraction, fusion.
4. core_temperature()  — the balance of gravity and gas pressure gives the Sun's central temperature
                         to within a factor of two, from M and R alone.
5. coulomb_barrier()   — the temperature two protons would need to touch classically, against the
                         temperature the Sun's core actually has.
6. sun_budget()        — mass converted to light each second, hydrogen fused each second, and the
                         main-sequence lifetime.
7. main_sequence()     — mass decides luminosity, radius, surface temperature and lifetime.
8. power_density()     — the Sun's core against a human body, watt for watt per cubic metre.
9. white_dwarfs()      — hydrostatic balance with degenerate electrons, integrated numerically:
                         the mass-radius curve and the Chandrasekhar limit.
10. collapse()         — energy released when an iron core becomes a neutron star; the Schwarzschild radius.

Run:  python3 stellar-evolution-model.py        (numpy + scipy, about 1 s)
"""
import numpy as np
from scipy.integrate import solve_ivp

G, c, h, k_B = 6.674e-11, 2.998e8, 6.626e-34, 1.381e-23
sigma, m_p, m_e, e, eps0 = 5.670e-8, 1.673e-27, 9.109e-31, 1.602e-19, 8.854e-12
M_SUN, R_SUN, L_SUN, T_SUN = 1.989e30, 6.957e8, 3.828e26, 5772.0
AU, YEAR = 1.496e11, 365.25 * 86400


def planck_fraction(T, lam_lo, lam_hi, n=200_000):
    lam = np.linspace(1e-8, 1e-4, n)
    B = 1 / (lam**5 * np.expm1(h * c / (lam * k_B * T)))
    sel = (lam >= lam_lo) & (lam < lam_hi)
    return np.trapezoid(B[sel], lam[sel]) / np.trapezoid(B, lam)


def sunlight():
    uv = planck_fraction(T_SUN, 0, 400e-9)
    vis = planck_fraction(T_SUN, 400e-9, 700e-9)
    ir = planck_fraction(T_SUN, 700e-9, 1)
    print(f"  5772 K blackbody: ultraviolet {100*uv:.0f} %, visible {100*vis:.0f} %, infrared {100*ir:.0f} %")
    print(f"  peak wavelength (Wien): {2.898e-3/T_SUN*1e9:.0f} nm, in the green")


def light_year():
    ly = c * YEAR
    pc = AU / np.tan(np.radians(1 / 3600))
    print(f"  1 light-year = {ly:.3e} m   (syllabus value 9.5e15 m)")
    print(f"  1 parsec = 1 AU / tan(1 arcsec) = {pc:.3e} m = {pc/ly:.2f} light-years = {pc/AU:.0f} AU")
    print(f"  Sun to Earth: {AU/c:.0f} s of light travel;  Proxima Centauri (p = 0.768 arcsec): "
          f"{1/0.768:.2f} pc = {1/0.768*pc/ly:.2f} ly = {1/0.768*pc/AU:,.0f} AU")


def what_powers_the_sun():
    coal = 3.0e7 * M_SUN / L_SUN                       # 30 MJ/kg, the whole Sun made of coal + oxygen
    kh = G * M_SUN**2 / R_SUN / L_SUN                  # gravitational energy released by contraction
    fusion = 0.007 * 0.10 * M_SUN * c**2 / L_SUN       # 0.7 % of the mass of the 10 % that gets hot enough
    for name, t in (("chemical burning (coal)", coal), ("gravitational contraction", kh), ("hydrogen fusion", fusion)):
        print(f"  {name:28s} {t/YEAR:12.3g} years")
    print("  rocks and fossils demand billions of years: only the third candidate survives")
    return coal / YEAR, kh / YEAR, fusion / YEAR


def core_temperature():
    # pressure needed to hold up the star ~ G M^2 / R^4 ; ideal gas P = (rho / mu m_p) k T
    T = G * M_SUN * m_p / (k_B * R_SUN)
    print(f"  G M m_p / (k R) = {T:.2e} K   (detailed models: 1.57e7 K).  No nuclear physics was used.")
    rho_mean = M_SUN / (4 / 3 * np.pi * R_SUN**3)
    print(f"  mean density of the Sun {rho_mean:.0f} kg/m^3 (water: 1000); central density in models 1.5e5 kg/m^3")


def coulomb_barrier():
    r = 1.0e-15                                           # range of the strong force
    U = e**2 / (4 * np.pi * eps0 * r)
    T_classical = 2 * U / (3 * k_B)                       # (3/2) k T = U
    print(f"  barrier for two protons at 1 fm: {U/e/1e6:.2f} MeV;  (3/2)kT = U needs T = {T_classical:.1e} K")
    print(f"  the core has 1.57e7 K: mean thermal energy {1.5*k_B*1.57e7/e/1e3:.1f} keV, short by a factor of {T_classical/1.57e7:.0f}")
    print("  the reaction happens anyway, by quantum tunnelling, and rarely: that rarity is why the Sun lasts")


def sun_budget():
    dm = L_SUN / c**2
    q = 4 * 1.007276 - 4.001506 - 2 * 0.000549            # 4 p -> He-4 + 2 e+ (nuclear masses, u)
    E = (q + 4 * 0.000549) * 931.494                      # + annihilation of both positrons
    frac = E / (4 * 1.007825 * 931.494)
    burn = L_SUN / (E * 1e6 * e) * 4 * m_p
    print(f"  mass turned into light: {dm:.2e} kg/s   ({dm*86400*365.25/5.97e24*1e9:.2f} billionths of an Earth mass per year)")
    print(f"  4 H -> He releases {E:.1f} MeV, which is {100*frac:.2f} % of the rest mass")
    print(f"  hydrogen fused: {burn:.2e} kg/s")
    t = 0.10 * 0.73 * M_SUN / burn
    print(f"  burning the central 10 % of the Sun's hydrogen (73 % of its mass) takes {t/YEAR/1e9:.1f} billion years")


def main_sequence():
    print("    mass    luminosity   radius   surface T   lifetime")
    rows = []
    for M in (0.1, 0.5, 1.0, 2.0, 10.0, 25.0):
        L = M**3.5 if M > 0.43 else 0.363 * M**2.3       # the two laws meet at 0.43
        R = M**0.8
        T = T_SUN * (L / R**2) ** 0.25
        t = 10.0 * M / L
        rows.append((M, L, R, T, t))
        print(f"  {M:6.1f}   {L:10.3g}   {R:6.2f}   {T:8.0f} K   {t:10.3g} billion years")
    print("  (scaling laws L ~ M^3.5, flatter below 0.43 M_sun, and R ~ M^0.8: good to a factor of about two)")
    return rows


def power_density():
    V = 4 / 3 * np.pi * (0.25 * R_SUN) ** 3
    print(f"  the fusing core (inner quarter of the radius): {L_SUN/V:.0f} W per cubic metre on average")
    print(f"  a resting human: 100 W in 0.07 m^3 = {100/0.07:.0f} W per cubic metre")
    print("  the Sun is bright because it is big, and long-lived because its fire is feeble")


def white_dwarfs(mu_e=2.0):
    """Cold degenerate electron gas, exact equation of state, Newtonian hydrostatic balance."""
    A = np.pi * m_e**4 * c**5 / (3 * h**3)
    B = 8 * np.pi * m_p * mu_e * (m_e * c / h) ** 3 / 3

    def pressure_gradient(x):                              # dP/dx for P = A f(x)
        return 8 * A * x**4 / np.sqrt(1 + x**2)

    def rhs(r, y):
        x, m = y
        if x <= 0:
            return [0, 0]
        rho = B * x**3
        dP = -G * m * rho / r**2
        return [dP / pressure_gradient(x), 4 * np.pi * r**2 * rho]

    out = []
    for xc in np.logspace(-0.7, 2.5, 40):
        surface = lambda r, y: y[0] - 1e-4 * xc
        surface.terminal = True
        r0 = 1.0
        sol = solve_ivp(rhs, [r0, 1e9], [xc, 4 / 3 * np.pi * r0**3 * B * xc**3], events=surface, rtol=1e-8, atol=1e-10, max_step=2e5)
        out.append((sol.y[1, -1] / M_SUN, sol.t[-1] / R_SUN, B * xc**3))
    out = np.array(out)
    for M, R, rho in out[::6]:
        print(f"  central density {rho:9.2e} kg/m^3:  M = {M:5.3f} M_sun,  R = {R:7.5f} R_sun = {R*R_SUN/6.371e6:5.2f} Earth radii")
    print(f"  the mass approaches {out[-1,0]:.3f} M_sun as the radius goes to zero: the Chandrasekhar limit")
    rho_wd = 1.0 * M_SUN / (4 / 3 * np.pi * (0.0084 * R_SUN) ** 3)
    print(f"  Sirius B (1.02 M_sun, 0.0084 R_sun): mean density {rho_wd:.1e} kg/m^3; a teaspoon (5 ml) has a mass of {rho_wd*5e-6/1000:.0f} tonnes")
    return out


def collapse():
    M, R = 1.4 * M_SUN, 1.2e4
    E = 0.6 * G * M**2 / R
    print(f"  1.4 M_sun falling to a 12 km ball releases ~{E:.1e} J")
    print(f"  the Sun's whole main-sequence output: {L_SUN*1e10*YEAR:.1e} J;  so the collapse outdoes it {E/(L_SUN*1e10*YEAR):.0f} times over, in seconds")
    print(f"  99 % leaves as neutrinos; the visible explosion is the remaining ~1e44 J")
    rho = M / (4 / 3 * np.pi * R**3)
    print(f"  neutron-star density {rho:.1e} kg/m^3 (an atomic nucleus: 2.3e17)")
    for m in (1, 3, 10, 4.3e6):
        print(f"  Schwarzschild radius of {m:9.3g} M_sun: {2*G*m*M_SUN/c**2/1000:12.4g} km")


if __name__ == "__main__":
    for i, f in enumerate((sunlight, light_year, what_powers_the_sun, core_temperature, coulomb_barrier,
                           sun_budget, main_sequence, power_density, white_dwarfs, collapse), 1):
        print(f"\n{i}. {f.__name__.replace('_', ' ')}")
        f()

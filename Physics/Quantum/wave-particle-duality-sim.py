"""
wave-particle-duality-sim.py — the double slit one photon at a time, the photoelectric
bookkeeping, and de Broglie's wavelength for real particles.

Companion to [[Wave-Particle Duality]].

  1. ONE PHOTON AT A TIME — the double-slit intensity from [[Superposition and Interference]]
     (two slits of finite width) is treated as a probability density; photons are drawn from
     it one by one and land as dots.  After 10, 100, 1000, 20000 dots the fringes emerge from
     noise — G. I. Taylor's 1909 experiment and Tonomura's 1989 film, in numbers.  Close one
     slit and the same photons give a single-slit blur: no fringes.
  2. THE PHOTOELECTRIC EFFECT — Einstein's bookkeeping hf = Φ + KE_max run for sodium and
     zinc against the wave theory's two failed predictions (intensity should set the energy;
     dim light should need a delay).  Millikan's 1916 sodium data reproduced from the
     modern constants: the slope of stopping voltage against frequency is h/e.
  3. DE BROGLIE — λ = h/p for an electron at the 9702 electron-diffraction tube's voltage,
     a proton, a tennis ball; the Bragg angle for graphite; why the ball has no diffraction.

Run:  python3 wave-particle-duality-sim.py
"""
import math
import numpy as np

SCRATCH = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/3ef0ae3f-b718-4398-bf45-668809d171fe/scratchpad"
h, c, e, m_e, m_p = 6.626e-34, 2.998e8, 1.602e-19, 9.109e-31, 1.673e-27

# ---------------------------------------------------------------- 1. photons one at a time
def double_slit_density(x, lam=600e-9, a=2e-6, d=10e-6, D=2.0):
    """Two slits of width a, centres d apart: interference under the single-slit envelope."""
    th = np.arctan(x / D); s = np.sin(th)
    beta = np.pi * a * s / lam; alpha = np.pi * d * s / lam
    env = np.where(beta == 0, 1.0, (np.sin(beta) / np.where(beta == 0, 1, beta)) ** 2)
    return env * np.cos(alpha) ** 2

def one_at_a_time():
    rng = np.random.default_rng(1909)
    x = np.linspace(-0.6, 0.6, 24001)
    pdf = double_slit_density(x); cdf = np.cumsum(pdf); cdf /= cdf[-1]
    hits = np.interp(rng.random(20000), cdf, x)            # each photon: one random draw from the pattern
    np.save(SCRATCH + "/photon-hits.npy", hits)
    print("1. photons through two slits, drawn one at a time from the wave's intensity:")
    edges = np.linspace(-0.3, 0.3, 61); mids = (edges[:-1] + edges[1:]) / 2; expected = double_slit_density(mids)
    for n in (10, 100, 1000, 20000):
        counts, _ = np.histogram(hits[:n], bins=edges)
        r = np.corrcoef(counts, expected)[0, 1]                 # how well the dots match the wave's pattern
        print(f"   after {n:5d} photons: correlation with the interference pattern r = {r:.2f}" + ("  — could be noise" if r < 0.6 else "  — the fringes are there"))
    # one slit closed
    env_pdf = (lambda x: double_slit_density(x) / np.cos(np.pi * 10e-6 * np.sin(np.arctan(x / 2.0)) / 600e-9) ** 2)(x)
    env_pdf = np.nan_to_num(env_pdf); cdf2 = np.cumsum(env_pdf); cdf2 /= cdf2[-1]
    hits1 = np.interp(rng.random(20000), cdf2, x)
    np.save(SCRATCH + "/photon-hits-oneslit.npy", hits1)
    counts, _ = np.histogram(hits1, bins=edges); r1 = np.corrcoef(counts, expected)[0, 1]; r_env = np.corrcoef(counts, env_pdf_binned := np.interp(mids, x, env_pdf))[0, 1]
    print(f"   one slit covered, 20000 photons: correlation with the two-slit pattern {r1:.2f}, with the single-slit blur {r_env:.2f} — no fringes; every photon went through the open slit and still 'knew' the other was shut")
    print(f"   each photon's energy at 600 nm: E = hc/λ = {h*c/600e-9:.2e} J = {h*c/600e-9/e:.2f} eV; a 1 mW laser sends {1e-3/(h*c/600e-9):.1e} of them per second")

# ---------------------------------------------------------------- 2. photoelectric
def photoelectric():
    metals = {"sodium": 2.28, "zinc": 4.31, "caesium": 2.14}      # work functions, eV
    print("\n2. the photoelectric effect — Einstein's bookkeeping hf = Φ + KE_max:")
    for lam_nm in (700, 550, 400, 250):
        f = c / (lam_nm * 1e-9); E = h * f / e
        row = f"   λ = {lam_nm} nm ({E:.2f} eV): "
        for m, phi in metals.items():
            ke = E - phi
            row += f"{m} {'KE_max = %.2f eV' % ke if ke > 0 else 'no emission':>18s}   "
        print(row)
    print("   threshold frequencies f₀ = Φ/h: " + ", ".join(f"{m} {phi*e/h:.2e} Hz ({h*c/(phi*e)*1e9:.0f} nm)" for m, phi in metals.items()))
    # Millikan 1916: stopping voltage against frequency for sodium — the slope is h/e
    fs = np.array([5.5, 6.0, 7.0, 8.0, 9.0, 10.0]) * 1e14
    Vs = (h * fs - 2.28 * e) / e
    slope, intercept = np.polyfit(fs, Vs, 1)
    print(f"   sodium, stopping voltage vs frequency: slope {slope:.3e} V s → h = slope × e = {slope*e:.3e} J s (Millikan measured 6.57e-34); x-intercept f₀ = {-intercept/slope:.2e} Hz")
    np.savez(SCRATCH + "/photoelectric.npz", fs=fs, Vs=Vs)
    # the wave theory's failed prediction: energy delivered to one atom-sized target by dim light
    I = 1e-6                                                     # W/m², a very dim source
    area = math.pi * (1e-10) ** 2                                # one atom's cross-section
    t = 2.28 * e / (I * area)
    print(f"   the wave theory's delay: at 1 μW/m², an atom-sized target collects the 2.28 eV needed for sodium in {t:.0f} s ≈ {t/3600/24:.0f} days — emission is observed within nanoseconds at any intensity")

# ---------------------------------------------------------------- 3. de Broglie
def de_broglie():
    print("\n3. de Broglie λ = h/p:")
    for name, m, KE_eV in (("electron in the diffraction tube, 5.0 kV", m_e, 5000), ("electron at 100 eV", m_e, 100), ("proton at 5.0 keV", m_p, 5000)):
        p = math.sqrt(2 * m * KE_eV * e); lam = h / p
        print(f"   {name:42s}: p = {p:.2e} kg m/s, λ = {lam:.2e} m = {lam*1e12:.1f} pm")
    lam_e = h / math.sqrt(2 * m_e * 5000 * e); d = 0.213e-9       # graphite (100) spacing
    th = math.degrees(math.asin(lam_e / (2 * d)))
    print(f"   graphite planes d = 0.213 nm: first-order Bragg angle for the 5 kV electron, sin θ = λ/2d → θ = {th:.1f}° — ring visible on a 10 cm screen")
    m_ball, v = 0.058, 50.0
    print(f"   a tennis ball, 58 g at 50 m/s: λ = {h/(m_ball*v):.1e} m — 10²⁴ times smaller than the ball; no slit will ever diffract it")
    # the relativistic check on the 5 kV electron
    KE = 5000 * e; p_rel = math.sqrt((KE + m_e * c ** 2) ** 2 - (m_e * c ** 2) ** 2) / c; p_cl = math.sqrt(2 * m_e * KE)
    print(f"   (relativity at 5 kV: the exact momentum is {100*(p_rel/p_cl-1):.2f}% above the classical value — the syllabus ignores it)")

if __name__ == "__main__":
    one_at_a_time(); photoelectric(); de_broglie()

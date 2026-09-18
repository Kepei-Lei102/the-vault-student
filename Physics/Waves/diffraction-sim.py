"""
diffraction-sim.py — diffraction from Huygens' principle, nothing else.

Companion to [[Diffraction]].  Every pattern here is made the same way: a slit is a row of
point sources, each radiating a spherical wavelet; the wavelets are added (the superposition
principle) at each point of a distant screen; the intensity is the square of the sum.  No
formula for diffraction is put in.  The script then reads the formulas OUT of the patterns:

  1. SINGLE SLIT — minima measured at sin θ = mλ/a; central maximum twice as wide as the
     others; the first side maximum 4.5 % of the centre.
  2. WIDTH AND WAVELENGTH — the spread of the central maximum as the slit widens and as the
     wavelength changes: narrow slit, wide spread; long wave, wide spread (the 9702 §8.2
     qualitative facts, as numbers).
  3. DOUBLE SLIT, HONESTLY — two slits of finite width: Young's fringes inside a single-slit
     envelope; missing orders where the two conditions coincide.
  4. THE GRATING — N slits: maxima at d sin θ = nλ get sharper as N grows (width ∝ 1/N)
     and brighter (∝ N²); the number of orders that fit below 90°.
  5. THE RIPPLE TANK — a 2-D wave through a gap (finite differences): the wavefront spreads
     more the narrower the gap; the spreading half-angle measured against λ/a.

Run:  python3 diffraction-sim.py
"""
import math
import numpy as np

SCRATCH = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad"

def pattern(slit_centres, slit_width, lam, thetas, n_src=400, raw=False):
    """Sum Huygens wavelets from every slit over a far-field direction list; return I/I(0) (or raw I)."""
    k = 2 * math.pi / lam
    xs = np.concatenate([np.linspace(c - slit_width / 2, c + slit_width / 2, n_src) for c in slit_centres])
    s = np.sin(thetas)
    field = np.exp(1j * k * np.outer(s, xs)).sum(1)            # far field: phase k x sin θ per source
    I = np.abs(field) ** 2
    return I if raw else I / I[np.argmin(abs(thetas))]

def extrema(x, y, kind="min", thr=None):
    idx = []
    for i in range(1, len(y) - 1):
        if kind == "min" and y[i] < y[i - 1] and y[i] <= y[i + 1] and (thr is None or y[i] < thr): idx.append(i)
        if kind == "max" and y[i] > y[i - 1] and y[i] >= y[i + 1] and (thr is None or y[i] > thr): idx.append(i)
    return idx

# ------------------------------------------------------------------ 1. single slit
def single_slit():
    lam, a = 600e-9, 3e-6
    th = np.radians(np.linspace(-60, 60, 24001))
    I = pattern([0.0], a, lam, th)
    mins = [i for i in extrema(th, I, "min", 1e-3) if th[i] > 0]
    print(f"1. single slit a = {a*1e6:.0f} μm, λ = {lam*1e9:.0f} nm (a/λ = {a/lam:.0f}):")
    print("   minima at sin θ =", ", ".join(f"{math.sin(th[i]):.3f}" for i in mins[:4]), "  predicted mλ/a =", ", ".join(f"{m*lam/a:.3f}" for m in (1, 2, 3, 4)))
    w0 = 2 * math.sin(th[mins[0]]); w1 = math.sin(th[mins[1]]) - math.sin(th[mins[0]])
    maxs = [i for i in extrema(th, I, "max") if th[i] > 0]
    print(f"   central maximum width (in sin θ) {w0:.3f} = 2 × the side maxima's {w1:.3f}; first side maximum {100*I[maxs[0]]:.1f}% of the centre, second {100*I[maxs[1]]:.1f}%")
    np.savez(SCRATCH + "/single.npz", th=th, I=I)

# ------------------------------------------------------------------ 2. width and wavelength
def width_wavelength():
    th = np.radians(np.linspace(-89, 89, 40001))
    print("\n2. half-width of the central maximum (angle to the first minimum):")
    for a, lam in ((1e-6, 600e-9), (2e-6, 600e-9), (5e-6, 600e-9), (20e-6, 600e-9), (2e-6, 450e-9), (2e-6, 700e-9)):
        I = pattern([0.0], a, lam, th)
        mins = [i for i in extrema(th, I, "min", 1e-3) if th[i] > 0]
        half = math.degrees(th[mins[0]]) if mins else float("nan")
        print(f"   a = {a*1e6:4.0f} μm, λ = {lam*1e9:.0f} nm:  {half:5.1f}°   (sin⁻¹(λ/a) = {math.degrees(math.asin(min(1, lam/a))):5.1f}°)" + ("   — the slit is smaller than λ: no minimum at all, the wave spreads into the whole half-plane" if a < lam else ""))
    a, lam = 0.5e-6, 600e-9
    I = pattern([0.0], a, lam, th)
    print(f"   a = {a*1e6:.1f} μm < λ: intensity at 60° is still {100*I[np.argmin(abs(th-math.radians(60)))]:.0f}% of the centre — a slit narrower than the wavelength is a point source")

# ------------------------------------------------------------------ 3. double slit with width
def double_slit():
    lam, a, d = 600e-9, 2e-6, 10e-6
    th = np.radians(np.linspace(-25, 25, 40001))
    I2 = pattern([-d / 2, d / 2], a, lam, th)
    I1 = pattern([0.0], a, lam, th)
    print(f"\n3. two slits of width {a*1e6:.0f} μm, centres {d*1e6:.0f} μm apart, λ = {lam*1e9:.0f} nm:")
    maxs = [i for i in extrema(th, I2, "max", 1e-3) if th[i] >= 0]
    print("   bright fringes at sin θ =", ", ".join(f"{math.sin(th[i]):.3f}" for i in maxs[:7]), "  → d sin θ / λ =", ", ".join(f"{d*math.sin(th[i])/lam:.2f}" for i in maxs[:7]))
    print(f"   their heights (I/I₀): " + ", ".join(f"{I2[i]:.2f}" for i in maxs[:7]) + "  — the single-slit envelope, "
          + f"and order {round(d/a)} at sin θ = {round(d/a)*lam/d:.3f} is MISSING: it sits on the single-slit minimum sin θ = λ/a = {lam/a:.3f}")
    np.savez(SCRATCH + "/double.npz", th=th, I2=I2, I1=I1)

# ------------------------------------------------------------------ 4. grating
def grating():
    lam, d, a = 600e-9, 2.5e-6, 0.5e-6
    th = np.radians(np.linspace(-90, 90, 90001))
    print(f"\n4. grating: slit spacing d = {d*1e6:.1f} μm ({1e-3/d:.0f} lines per mm), λ = {lam*1e9:.0f} nm:")
    out = {}
    one = pattern([0.0], a, lam, th, n_src=40, raw=True).max()
    for N in (2, 5, 20, 100):
        c = (np.arange(N) - (N - 1) / 2) * d
        Iraw = pattern(c, a, lam, th, n_src=40, raw=True); gain = Iraw.max() / one
        I = Iraw / Iraw[np.argmin(abs(th))]
        maxs = [i for i in extrema(th, I, "max", 0.5) if th[i] >= 0]
        # width of the first-order peak: full width at half maximum, in degrees
        p = maxs[1] if len(maxs) > 1 else maxs[0]
        lo = p; hi = p
        while I[lo] > I[p] / 2: lo -= 1
        while I[hi] > I[p] / 2: hi += 1
        fwhm = math.degrees(th[hi] - th[lo])
        out[N] = I
        print(f"   N = {N:3d} slits: principal maxima at sin θ = {', '.join(f'{math.sin(th[i]):.3f}' for i in maxs)}   first-order peak width {fwhm:.2f}°   central peak {gain:.0f}× one slit's (= N²)" if N > 2 else
              f"   N = {N:3d} slits: maxima at sin θ = {', '.join(f'{math.sin(th[i]):.3f}' for i in maxs)}   first-order peak width {fwhm:.2f}°")
    n_max = math.floor(d / lam)
    print(f"   orders that fit: d sin θ = nλ with sin θ ≤ 1 → n ≤ d/λ = {d/lam:.2f} → n_max = {n_max}; total maxima on a full screen = 2 × {n_max} + 1 = {2*n_max+1}")
    print("   — sharper as N grows (width ∝ 1/N), brighter (∝ N²), positions fixed by d alone")
    np.savez(SCRATCH + "/grating.npz", th=th, **{f"N{N}": I for N, I in out.items()})

# ------------------------------------------------------------------ 5. ripple tank through a gap
def ripple_gap(gap_over_lambda, lam=1.0, size=40.0, n=320, t_end=36.0):
    dx = size / n; c = 1.0; dt = 0.45 * dx / c
    u = np.zeros((n, n)); up = np.zeros((n, n)); un = np.zeros((n, n))
    wall = n // 3; gap = gap_over_lambda * lam / dx
    mask = np.ones((n, n), bool); mask[wall, :] = False
    lo, hi = int(n / 2 - gap / 2), int(n / 2 + gap / 2)
    mask[wall, lo:hi] = True
    f = c / lam
    steps = int(t_end / dt); env = np.zeros((n, n)); period_steps = int(1 / (f * dt))
    for s in range(steps):
        t = s * dt
        lap = (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u) / dx ** 2
        un = 2 * u - up + (c * dt) ** 2 * lap
        un[:3, :] = np.sin(2 * math.pi * f * t) * np.ones((3, n)) * (1 - np.exp(-t))   # plane wave from the bottom rows
        un[~mask] = 0.0
        # absorbing edges (crude): damp the last rows/cols
        for k in range(1, 12):
            un[-k, :] *= 0.9; un[:, k - 1] *= 0.9; un[:, -k] *= 0.9
        up, u = u, un
        if s >= steps - period_steps: env = np.maximum(env, np.abs(u))
    return u, env, wall, dx

def ripple_tank():
    print("\n5. a plane wave through a gap in a barrier (2-D wave equation, finite differences):")
    fields = {}
    for g in (0.5, 1.0, 2.0, 6.0):
        u, env, wall, dx = ripple_gap(g)
        fields[g] = u; fields[f"env{g}"] = env
        # amplitude envelope along a row well beyond the barrier, as a function of angle from the gap centre
        row = wall + int(10 / dx)
        amp = env[row, :]
        centre = u.shape[1] // 2
        half = amp[centre] / 2
        j = centre
        while j < u.shape[1] - 1 and amp[j] > half: j += 1
        ang = math.degrees(math.atan2((j - centre) * dx, (row - wall) * dx))
        j45 = centre + (row - wall)                        # the column 45° off-axis from the gap, on this row
        frac = amp[j45] / amp[centre]
        print(f"   gap = {g:3.1f} λ: 10 λ past the barrier, the amplitude 45° off-axis is {100*frac:3.0f}% of the on-axis amplitude" + ("   — a gap of a wavelength or less radiates like a point: near-semicircular wavefronts" if g <= 1 else ""))
    print("   — narrow gap, the wave floods the shadow; wide gap, it goes straight on with only its edges bent")
    np.savez(SCRATCH + "/ripple.npz", **{f"g{k}": v for k, v in fields.items()})

if __name__ == "__main__":
    single_slit(); width_wavelength(); double_slit(); grating(); ripple_tank()

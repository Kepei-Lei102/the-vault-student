"""
superposition-interference-sim.py — two-source interference, measured rather than asserted.

Companion to [[Superposition and Interference]].  Five experiments, each a claim the
card makes, each checked by adding waves point by point (the superposition principle)
and never by quoting the result:

  1. TWO POINT SOURCES IN A RIPPLE TANK — the field of two in-phase sources is summed;
     the lines of maximum amplitude are found and the path difference along each is
     measured: n λ, exactly, with (n + ½) λ on the lines of minimum.
  2. YOUNG'S FRINGES — the intensity on a distant screen from two narrow slits, by
     summing the two waves; fringe spacing measured and compared with λD/a, and the
     small-angle approximation's error tracked as the fringes move off-axis.
  3. COHERENCE — two sources whose phase relationship is fixed give a pattern; two
     sources whose relative phase jumps at random (as two separate lamps do) give the
     same pattern at any instant and NO pattern once averaged over a detector's
     response time.  This is what "coherent" means and why it is required.
  4. BEATS — two tones of nearly equal frequency summed in time: the envelope
     frequency measured as |f1 − f2|.
  5. THIN FILM — a soap film's reflectance vs thickness by summing the two reflected
     waves with the π phase change at the denser boundary: bright at 2nt = (m + ½) λ.

Run:  python3 superposition-interference-sim.py
"""
import math
import numpy as np

# ---------------------------------------------------------------- 1. ripple tank
def ripple_tank():
    lam = 2.0                       # cm
    a = 6.0                         # source separation (cm)
    k = 2 * math.pi / lam
    xs = np.linspace(-20, 20, 801); ys = np.linspace(0.5, 30, 591)
    X, Y = np.meshgrid(xs, ys)
    r1 = np.hypot(X + a / 2, Y); r2 = np.hypot(X - a / 2, Y)
    # complex amplitude of each circular wave (1/√r falloff), summed — the superposition principle
    field = np.exp(1j * k * r1) / np.sqrt(r1) + np.exp(1j * k * r2) / np.sqrt(r2)
    amp = np.abs(field) * np.sqrt((r1 + r2) / 2)          # undo the average falloff to compare fairly
    # along the far row y = 30 cm, find maxima and minima of amplitude
    row = amp[-1]
    peaks = [i for i in range(1, len(xs) - 1) if row[i] > row[i - 1] and row[i] >= row[i + 1] and row[i] > 1.2]
    troughs = [i for i in range(1, len(xs) - 1) if row[i] < row[i - 1] and row[i] <= row[i + 1] and row[i] < 0.6]
    pd = lambda i: abs(r2[-1, i] - r1[-1, i]) / lam
    print(f"1. two in-phase sources {a} cm apart, λ = {lam} cm, read along a line 30 cm away:")
    print("   maxima at x =", ", ".join(f"{xs[i]:+.1f}" for i in peaks), "cm")
    print("   path difference there, in wavelengths:", ", ".join(f"{pd(i):.2f}" for i in peaks))
    print("   minima  at x =", ", ".join(f"{xs[i]:+.1f}" for i in troughs), "cm")
    print("   path difference there, in wavelengths:", ", ".join(f"{pd(i):.2f}" for i in troughs))
    print("   — whole numbers on the maxima, halves on the minima; the pattern was never told where to be")
    return xs, ys, amp

# ---------------------------------------------------------------- 2. Young's fringes
def young(lam=600e-9, a=0.50e-3, D=2.0):
    x = np.linspace(-0.45, 0.45, 1500001)
    r1 = np.hypot(x + a / 2, D); r2 = np.hypot(x - a / 2, D)
    k = 2 * math.pi / lam
    I = np.abs(np.exp(1j * k * r1) + np.exp(1j * k * r2)) ** 2 / 4      # normalised to 1 at the centre
    peaks = [i for i in range(1, len(x) - 1) if I[i] > I[i - 1] and I[i] >= I[i + 1] and I[i] > 0.9]
    xp = x[peaks]
    spacing = np.diff(xp)
    print(f"\n2. Young: λ = {lam*1e9:.0f} nm, a = {a*1e3:.2f} mm, D = {D} m")
    print(f"   predicted fringe spacing λD/a = {lam*D/a*1e3:.3f} mm")
    centre = np.argmin(abs(xp))
    print(f"   measured spacing near the centre: {spacing[centre]*1e3:.3f} mm;  at the 8th fringe: {spacing[centre+7]*1e3:.3f} mm (the small-angle formula drifts by {100*(spacing[centre+7]/spacing[centre]-1):+.2f}%)")
    # how far out before the error reaches 1 %?
    n = next(i for i in range(len(spacing) - centre) if abs(spacing[centre + i] / spacing[centre] - 1) > 0.01)
    print(f"   the formula is 1% out by fringe {n} (x = {xp[centre+n]*1e3:.1f} mm, angle {math.degrees(math.atan(xp[centre+n]/D)):.2f}°)")
    # the exam's variations
    for tag, l2, a2, D2 in (("double a", lam, 2 * a, D), ("double D", lam, a, 2 * D), ("red → blue", 450e-9, a, D)):
        print(f"   {tag:10s}: spacing {l2*D2/a2*1e3:.3f} mm")
    return x, I

# ---------------------------------------------------------------- 3. coherence
def coherence():
    lam = 1.0; k = 2 * math.pi / lam; a = 3.0; D = 40.0
    x = np.linspace(-10, 10, 2001)
    r1 = np.hypot(x + a / 2, D); r2 = np.hypot(x - a / 2, D)
    rng = np.random.default_rng(1801)
    N = 2000                                              # snapshots within one detector response time
    coherent = np.zeros_like(x); incoherent = np.zeros_like(x)
    for _ in range(N):
        phi = rng.uniform(0, 2 * math.pi)                 # a random phase kick between two independent lamps
        coherent += np.abs(np.exp(1j * k * r1) + np.exp(1j * k * r2)) ** 2
        incoherent += np.abs(np.exp(1j * k * r1) + np.exp(1j * (k * r2 + phi))) ** 2
    coherent /= N; incoherent /= N
    vis = lambda I: (I.max() - I.min()) / (I.max() + I.min())
    single = np.abs(np.exp(1j * (k * r2 + 0.7)) + np.exp(1j * k * r1)) ** 2
    print(f"\n3. coherence — visibility (I_max − I_min)/(I_max + I_min) of the time-averaged pattern:")
    print(f"   constant phase difference (coherent):     {vis(coherent):.3f}")
    print(f"   any single instant of two independent lamps: {vis(single):.3f}  — a perfect pattern exists at every instant")
    print(f"   averaged over {N} random phase jumps:       {vis(incoherent):.3f}  — and the detector sees none of them")
    print("   — 'coherent' = constant phase difference; the fringes are there either way, but only a constant one holds still long enough to be seen")

# ---------------------------------------------------------------- 4. beats
def beats(f1=440.0, f2=444.0):
    t = np.linspace(0, 2.0, 400001)
    y = np.sin(2 * math.pi * f1 * t) + np.sin(2 * math.pi * f2 * t)
    # envelope: peak of |y| in windows of one carrier period
    win = int(len(t) / (2.0 * f1))
    env = np.array([abs(y[i:i + win]).max() for i in range(0, len(t) - win, win)])
    te = t[:len(env) * win:win]
    zeros = [te[i] for i in range(1, len(env) - 1) if env[i] < env[i - 1] and env[i] <= env[i + 1] and env[i] < 0.3]
    gaps = np.diff(zeros)
    print(f"\n4. beats: {f1} Hz + {f2} Hz — envelope minima every {gaps.mean():.3f} s → beat frequency {1/gaps.mean():.2f} Hz = |f1 − f2| = {abs(f1-f2):.0f} Hz")
    print(f"   the sum is sin(2π·{(f1+f2)/2:.0f}t)·2cos(2π·{abs(f1-f2)/2:.0f}t): a {(f1+f2)/2:.0f} Hz tone whose loudness pulses {abs(f1-f2):.0f} times a second")

# ---------------------------------------------------------------- 5. thin film
def thin_film(n=1.33, lam=550e-9):
    t = np.linspace(1e-9, 800e-9, 8000)
    # reflection from the top (air→soap): π phase change; from the bottom (soap→air): none
    # extra path 2nt for the second ray (normal incidence); equal amplitudes assumed for clarity
    phase = 2 * math.pi * (2 * n * t) / lam + math.pi
    R = np.abs(1 + np.exp(1j * phase)) ** 2 / 4
    peaks = [i for i in range(1, len(t) - 1) if R[i] > R[i - 1] and R[i] >= R[i + 1]]
    troughs = [i for i in range(1, len(t) - 1) if R[i] < R[i - 1] and R[i] <= R[i + 1]]
    print(f"\n5. soap film n = {n}, λ = {lam*1e9:.0f} nm in air, normal incidence:")
    print("   bright (reflection maxima) at t =", ", ".join(f"{t[i]*1e9:.0f}" for i in peaks[:4]), "nm  →  2nt/λ =", ", ".join(f"{2*n*t[i]/lam:.2f}" for i in peaks[:4]))
    print("   dark   (reflection minima) at t =", ", ".join(f"{t[i]*1e9:.0f}" for i in troughs[:4]), "nm  →  2nt/λ =", ", ".join(f"{2*n*t[i]/lam:.2f}" for i in troughs[:4]))
    print(f"   R at t → 0: {R[0]:.3f} — a film thinner than ~λ/20 reflects nothing: the black top of a draining bubble")

if __name__ == "__main__":
    ripple_tank(); young(); coherence(); beats(); thin_film()

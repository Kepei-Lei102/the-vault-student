"""
laplace-great-inequality.py — Halley's anomaly, and Laplace's 1785 answer, reproduced.

Companion to [[Stories/Laplace and Napoleon]].  Halley (1695) found Jupiter running
ahead of Kepler's tables and Saturn falling behind — and if that were a secular
(one-way) drift, the solar system was slowly unwinding.  Laplace (1785) showed it is
periodic: because five Jupiter years are almost exactly two Saturn years (a 5:2 near-
resonance), the two planets pull each other in a pattern that repeats every ~900
years; Jupiter gains ~21′ of longitude and gives it back, Saturn ~49′.  Nothing is
unwinding.  This script integrates Sun + Jupiter + Saturn with Newton's law only
(velocity-Verlet, 6000 years, starting elements calibrated so the mean periods are the observed ones), converts each state to its osculating mean longitude, and measures the period and
amplitudes of what is left.

Run:  python3 laplace-great-inequality.py
"""
import math
import numpy as np

# --- units: AU, year, solar mass;  G = 4π² ---------------------------------------
G = 4 * math.pi ** 2
M_SUN, M_J, M_S = 1.0, 1 / 1047.35, 1 / 3497.9          # Jupiter, Saturn in solar masses
P_J, P_S = 11.862, 29.457                                # sidereal periods (yr)
E_J, E_S = 0.0489, 0.0565                                # eccentricities
A_J = (P_J ** 2 * (M_SUN + M_J)) ** (1 / 3)              # Kepler III, with the planet's own mass
A_S = (P_S ** 2 * (M_SUN + M_S)) ** (1 / 3)

print(f"Kepler periods:  Jupiter {P_J:.2f} yr,  Saturn {P_S:.2f} yr")
print(f"5 P_J = {5*P_J:.1f} yr,  2 P_S = {2*P_S:.1f} yr  → the 5:2 near-resonance")
f_gi = abs(2 / P_J - 5 / P_S)                           # frequency of 2λ_J − 5λ_S
print(f"predicted period of the great inequality 1/|2n_J − 5n_S| = {1/f_gi:.0f} yr\n")

# --- initial conditions: both at perihelion, Saturn 90° round ------------------------
def peri(a, e, m, angle):
    r = a * (1 - e)
    v = math.sqrt(G * (M_SUN + m) * (1 + e) / (a * (1 - e)))
    c, s_ = math.cos(angle), math.sin(angle)
    return np.array([r * c, r * s_]), np.array([-v * s_, v * c])

m = np.array([M_SUN, M_J, M_S])

def accel(r):
    d = r[None, :, :] - r[:, None, :]                    # d[i,j] = r_j − r_i
    dist = np.linalg.norm(d, axis=2) + np.eye(3)
    return (G * m[None, :, None] * d / dist[:, :, None] ** 3).sum(1)

def mean_longitude(rp, vp, mu):
    """Osculating mean longitude λ = M + ϖ from a state vector — the quantity Laplace's
    inequality lives in (the equation of the centre, ~2e, is removed by construction)."""
    rn = np.linalg.norm(rp); v2 = vp @ vp; rv = rp @ vp
    ev = ((v2 - mu / rn) * rp - rv * vp) / mu            # eccentricity vector
    e = np.linalg.norm(ev); varpi = math.atan2(ev[1], ev[0])
    nu = math.atan2(rp[1], rp[0]) - varpi                 # true anomaly
    E = 2 * math.atan2(math.sqrt(1 - e) * math.sin(nu / 2), math.sqrt(1 + e) * math.cos(nu / 2))
    M = E - e * math.sin(E)
    return M + varpi

def energy(r, v):
    k = 0.5 * (m * (v ** 2).sum(1)).sum()
    u = sum(-G * m[i] * m[j] / np.linalg.norm(r[i] - r[j]) for i in range(3) for j in range(i + 1, 3))
    return k + u

def run(a_j, a_s, t_end, dt=0.02):
    """Integrate Sun + Jupiter + Saturn (velocity-Verlet); return times and mean longitudes."""
    rj, vj = peri(a_j, E_J, M_J, 0.0)
    rs, vs = peri(a_s, E_S, M_S, math.pi / 2)
    r = np.array([[0.0, 0.0], rj, rs]); v = np.array([[0.0, 0.0], vj, vs])
    v -= (m[:, None] * v).sum(0) / m.sum()               # centre-of-mass frame
    a = accel(r); E0 = energy(r, v)
    ts, lj, ls = [], [], []
    for s_ in range(int(t_end / dt) + 1):
        if s_ % 25 == 0:                                  # every half year
            ts.append(s_ * dt)
            lj.append(mean_longitude(r[1] - r[0], v[1] - v[0], G * (M_SUN + M_J)))
            ls.append(mean_longitude(r[2] - r[0], v[2] - v[0], G * (M_SUN + M_S)))
        v += 0.5 * dt * a; r += dt * v; a = accel(r); v += 0.5 * dt * a
    return np.array(ts), np.unwrap(np.array(lj)), np.unwrap(np.array(ls)), abs(energy(r, v) - E0) / abs(E0)

def fitted_period(ts, lam):
    return 360 / np.degrees(np.polyfit(ts, lam, 1)[0])

# --- calibrate: the osculating a we start with is not the mean a; nudge until the
#     MEAN periods the integration actually shows are the observed 11.862 / 29.457 yr ----
a_j, a_s = A_J, A_S
for it in range(3):
    ts, lj, ls, _ = run(a_j, a_s, 1200.0)
    pj, ps = fitted_period(ts, lj), fitted_period(ts, ls)
    print(f"calibration {it}: mean periods Jupiter {pj:.3f}, Saturn {ps:.3f} yr  (targets {P_J}, {P_S})")
    a_j *= (P_J / pj) ** (2 / 3); a_s *= (P_S / ps) ** (2 / 3)

# --- the long run ------------------------------------------------------------------
T_END = 6000.0
ts, lam_j, lam_s, drift = run(a_j, a_s, T_END)
print(f"\nenergy drift over {T_END:.0f} yr: {drift:.1e} (relative)")
pj_fit, ps_fit = fitted_period(ts, lam_j), fitted_period(ts, lam_s)
print(f"fitted mean periods: Jupiter {pj_fit:.3f} yr, Saturn {ps_fit:.3f} yr — a straight line: the mean motion is NOT drifting")
print(f"so 1/|2n_J − 5n_S| = {1/abs(2/pj_fit - 5/ps_fit):.0f} yr")

def residual(lam):
    return np.degrees(lam - np.polyval(np.polyfit(ts, lam, 1), ts)) * 60      # arcminutes
res_j, res_s = residual(lam_j), residual(lam_s)

def best_sinusoid(res):
    """Scan periods 300–2000 yr; least-squares A cos + B sin + c at each; return the best."""
    best = None
    for P in np.arange(300, 2000, 2.0):
        w = 2 * math.pi / P
        X = np.column_stack([np.cos(w * ts), np.sin(w * ts), np.ones_like(ts)])
        c, ss, *_ = np.linalg.lstsq(X, res, rcond=None)
        ss = float(ss[0]) if len(ss) else float(((X @ c - res) ** 2).sum())
        if best is None or ss < best[0]:
            best = (ss, P, math.hypot(c[0], c[1]))
    return best[1], best[2]
for name, res, expect in (("Jupiter", res_j, 21), ("Saturn", res_s, 49)):
    P, A = best_sinusoid(res)
    print(f"{name}: best-fit period of the mean-longitude residual = {P:.0f} yr, amplitude {A:.1f}′  (Laplace 1785: ~{expect}′; peak-to-peak in the run {res.max()-res.min():.1f}′)")

# Halley's window: any single century sits on one flank of the oscillation
print("\nWhat Halley saw — over one century the residual is nearly a straight line:")
for t0 in (0, 300, 600):
    sel = (ts >= t0) & (ts < t0 + 100)
    sj = np.polyfit(ts[sel], res_j[sel], 1)[0]; ss_ = np.polyfit(ts[sel], res_s[sel], 1)[0]
    print(f"  years {t0:4.0f}–{t0+100:4.0f}: Jupiter drifting {sj*100:+.1f}′ per century, Saturn {ss_*100:+.1f}′ per century  (opposite signs)")
print("— a 'secular acceleration' that is really one flank of a ~900-year wave. Nothing is unwinding.")

np.save("/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad/gi.npy", np.vstack([ts, res_j, res_s]))

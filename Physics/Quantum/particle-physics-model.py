"""Every number and every allowed/forbidden verdict quoted in Particle Physics.md.

Run: python3 particle-physics-model.py
Part 1  builds hadrons from quarks and checks their charges, baryon numbers and strangeness.
Part 2  is a conservation-law referee: given a reaction, it checks charge, baryon number, the three lepton numbers and
        strangeness, and says which interaction (if any) could do it. Strangeness may change by one unit only in a weak
        process, which is the whole reason strange particles live long enough to leave tracks.
Part 3  is kinematics from special relativity: the muon's energy in pion decay, the energy a cosmic-ray proton needs to
        make an antiproton on a stationary target against a collider, and a synthetic Z → μ⁺μ⁻ data set whose invariant
        masses pile up at 91 GeV the way the real ones did in 1989.
Masses from the Particle Data Group (2024) in MeV/c².
"""
import math, random
import numpy as np

# ── 1. quarks and hadrons ───────────────────────────────────────────────────────────────────────────────────
Q = {"u": (+2/3, 0), "d": (-1/3, 0), "s": (-1/3, -1), "c": (+2/3, 0), "b": (-1/3, 0), "t": (+2/3, 0)}   # charge, strangeness
def hadron(quarks):
    """quarks: a string like 'uud' or 'u~d' (~ marks an antiquark). Returns (charge, baryon number, strangeness)."""
    q = b = s = 0.0; i = 0
    while i < len(quarks):
        anti = i + 1 < len(quarks) and quarks[i + 1] == "~"; f = quarks[i]; sign = -1 if anti else 1
        q += sign * Q[f][0]; s += sign * Q[f][1]; b += sign / 3; i += 2 if anti else 1
    return round(q, 3), round(b, 3), int(s)
print("== hadrons built from quarks: (charge, baryon number, strangeness)")
for name, q in [("proton", "uud"), ("neutron", "udd"), ("Δ++", "uuu"), ("Λ", "uds"), ("Ω⁻", "sss"), ("π⁺", "ud~"), ("π⁻", "du~"), ("K⁺", "us~"), ("K⁰", "ds~"), ("antiproton", "u~u~d~")]:
    print(f"   {name:10s} {q:8s} → {hadron(q)}")

# ── 2. the conservation-law referee ─────────────────────────────────────────────────────────────────────────
# particle: (charge, baryon, L_e, L_mu, L_tau, strangeness)
P = {
    "p": (1, 1, 0, 0, 0, 0), "n": (0, 1, 0, 0, 0, 0), "p~": (-1, -1, 0, 0, 0, 0), "n~": (0, -1, 0, 0, 0, 0),
    "e-": (-1, 0, 1, 0, 0, 0), "e+": (1, 0, -1, 0, 0, 0), "nu_e": (0, 0, 1, 0, 0, 0), "nu_e~": (0, 0, -1, 0, 0, 0),
    "mu-": (-1, 0, 0, 1, 0, 0), "mu+": (1, 0, 0, -1, 0, 0), "nu_mu": (0, 0, 0, 1, 0, 0), "nu_mu~": (0, 0, 0, -1, 0, 0),
    "gamma": (0, 0, 0, 0, 0, 0), "pi+": (1, 0, 0, 0, 0, 0), "pi-": (-1, 0, 0, 0, 0, 0), "pi0": (0, 0, 0, 0, 0, 0),
    "K+": (1, 0, 0, 0, 0, 1), "K-": (-1, 0, 0, 0, 0, -1), "K0": (0, 0, 0, 0, 0, 1), "Lambda": (0, 1, 0, 0, 0, -1),
    "Sigma+": (1, 1, 0, 0, 0, -1), "Omega-": (-1, 1, 0, 0, 0, -3), "Xi-": (-1, 1, 0, 0, 0, -2),
}
NAMES = ["charge", "baryon number", "electron number", "muon number", "tau number", "strangeness"]
def referee(reaction):
    lhs, rhs = [side.split() for side in reaction.split("->")]
    tot = lambda side: [sum(P[x][i] for x in side) for i in range(6)]
    a, b = tot(lhs), tot(rhs); broken = [NAMES[i] for i in range(5) if a[i] != b[i]]
    dS = b[5] - a[5]
    if broken: verdict = "forbidden: " + ", ".join(broken) + " not conserved"
    elif dS == 0: verdict = "allowed by any interaction (strangeness conserved)"
    elif abs(dS) == 1: verdict = "weak interaction only (strangeness changes by 1), so slow: a lifetime around 1e-10 s"
    else: verdict = f"forbidden even weakly: strangeness changes by {dS}"
    return verdict
print("\n== the referee")
for r in ["n -> p e- nu_e~", "n -> p e-", "n -> p e+ nu_e", "pi+ -> mu+ nu_mu", "pi+ -> mu+ nu_e", "mu- -> e- nu_e~ nu_mu",
          "p p -> p p p p~", "p p -> p p p", "K+ -> mu+ nu_mu", "Lambda -> p pi-", "Omega- -> Lambda K-", "Xi- -> n pi-", "p -> e+ gamma"]:
    print(f"   {r:26s} {referee(r)}")

# ── 3. kinematics ───────────────────────────────────────────────────────────────────────────────────────────
m_pi, m_mu, m_p, m_e, m_Z = 139.570, 105.658, 938.272, 0.511, 91187.6
E_mu = (m_pi**2 + m_mu**2) / (2 * m_pi)                      # two-body decay at rest: the muon's total energy
p_mu = math.sqrt(E_mu**2 - m_mu**2)
print(f"\n== pi+ -> mu+ nu at rest: muon energy {E_mu:.2f} MeV, kinetic {E_mu - m_mu:.2f} MeV, momentum {p_mu:.2f} MeV/c; the neutrino carries {m_pi - E_mu:.2f} MeV")
# making an antiproton: p p -> p p p pbar needs 4 m_p in the centre of mass
E_fixed = (16 * m_p**2 - 2 * m_p**2) / (2 * m_p)             # s = (E + m)^2 - p^2 = 2 m E + 2 m^2 = (4m)^2
print(f"== antiproton threshold: fixed target needs a beam of total energy {E_fixed/1000:.2f} GeV ({(E_fixed-m_p)/1000:.2f} GeV kinetic); a collider needs {2*m_p/1000:.3f} GeV per beam")
# LHC: 6.8 TeV protons
E_lhc = 6.8e6; gamma = E_lhc / m_p; v_short = 3e8 * (1 - 1/gamma**2)**0.5
print(f"== LHC proton at 6.8 TeV: gamma = {gamma:.0f}; slower than light by {3e8 - v_short:.1f} m/s; a 2.2 μs muon at 100 GeV would fly {2.2e-6*3e8*100e3/m_mu/1000:.0f} km")
# synthetic Z -> mu+ mu- events: invariant mass from the two muon four-momenta
rng = np.random.default_rng(3); N = 4000
width = 2495.2; masses = m_Z + width/2 * np.tan(math.pi * (rng.random(N) - 0.5))   # Breit–Wigner
masses = masses[(masses > 60000) & (masses < 120000)]
inv = []
for M in masses:                                             # decay at rest, isotropic; then smear each muon's momentum by 2%
    p = math.sqrt(M**2/4 - m_mu**2); th = math.acos(2*rng.random() - 1); ph = 2*math.pi*rng.random()
    d = np.array([math.sin(th)*math.cos(ph), math.sin(th)*math.sin(ph), math.cos(th)])
    p1 = p * d * rng.normal(1, 0.02); p2 = -p * d * rng.normal(1, 0.02)
    E1 = math.sqrt(p1 @ p1 + m_mu**2); E2 = math.sqrt(p2 @ p2 + m_mu**2)
    inv.append(math.sqrt((E1 + E2)**2 - (p1 + p2) @ (p1 + p2)))
inv = np.array(inv)
hist, edges = np.histogram(inv, bins=60, range=(60000, 120000))
print(f"== {len(inv)} synthetic Z -> mu mu events: reconstructed masses peak in the bin {edges[hist.argmax()]/1000:.0f}-{edges[hist.argmax()+1]/1000:.0f} GeV; median {np.median(inv)/1000:.2f} GeV")
np.save("particle-physics-zmass.npy", inv)
# Rutherford's dream: how far into a proton
lam = 1240 / 100e3 * 1e-15  # not used; the resolving power is hbar c / p
print(f"== resolving power: a 100 GeV probe sees down to about {197.327e-15/100e3*1e15*1e3:.3f} am = {197.327/100e3:.2e} fm; a proton is 0.84 fm across")

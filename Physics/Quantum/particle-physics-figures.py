"""Figures for Particle Physics.md — run after particle-physics-model.py (reads particle-physics-zmass.npy)."""
import re, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

TXT = "#888"; BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": TXT, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT, "axes.edgecolor": TXT, "font.size": 10, "svg.fonttype": "none"})

def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name).read(); m = re.search(r"<svg[^>]*>", s)
    tag = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)).replace("<svg", '<svg width="100%"', 1)
    open(name, "w").write(s[:m.start()] + tag + s[m.end():]); plt.close(fig)

# ── 1. the Standard Model, as a table you can read ─────────────────────────────────────────────────────────────
quarks = [("u", "up", "2.2 MeV", "+2/3"), ("c", "charm", "1.27 GeV", "+2/3"), ("t", "top", "173 GeV", "+2/3"),
          ("d", "down", "4.7 MeV", "−1/3"), ("s", "strange", "93 MeV", "−1/3"), ("b", "bottom", "4.18 GeV", "−1/3")]
leptons = [("e", "electron", "0.511 MeV", "−1"), ("μ", "muon", "106 MeV", "−1"), ("τ", "tau", "1.78 GeV", "−1"),
           ("νe", "e neutrino", "< 1 eV", "0"), ("νμ", "μ neutrino", "< 1 eV", "0"), ("ντ", "τ neutrino", "< 1 eV", "0")]
bosons = [("γ", "photon", "0", "electromagnetic"), ("g", "gluon", "0", "strong"), ("W±", "W", "80.4 GeV", "weak"), ("Z", "Z", "91.2 GeV", "weak"), ("H", "Higgs", "125 GeV", "gives mass")]
fig, ax = plt.subplots(figsize=(11, 5.2)); ax.set_xlim(0, 11); ax.set_ylim(0, 5.4); ax.axis("off")
def cell(x, y, sym, name, mass, extra, col):
    ax.add_patch(FancyBboxPatch((x, y), 1.55, 1.0, boxstyle="round,pad=0.02,rounding_size=0.08", fc=col, alpha=0.18, ec=col, lw=1.5))
    ax.text(x + 0.12, y + 0.62, sym, color=col, fontsize=17, fontweight="bold"); ax.text(x + 0.12, y + 0.3, name, color=TXT, fontsize=8.5)
    ax.text(x + 0.12, y + 0.08, mass, color=TXT, fontsize=8); ax.text(x + 1.43, y + 0.8, extra, color=col, fontsize=8.5, ha="right")
for i, q in enumerate(quarks): cell(0.3 + (i % 3) * 1.7, 3.9 - (i // 3) * 1.15, *q, PURPLE)
for i, l in enumerate(leptons): cell(0.3 + (i % 3) * 1.7, 1.6 - (i // 3) * 1.15, *l, BLUE)
for i, b in enumerate(bosons): cell(6.2 + (i % 2) * 1.7, 3.9 - (i // 2) * 1.15, *b, AMBER)
ax.text(0.3, 5.05, "matter: six quarks (purple) and six leptons (blue), in three generations", color=TXT, fontsize=10)
ax.text(6.2, 5.05, "force carriers, and the Higgs", color=TXT, fontsize=10)
for i, g in enumerate(["I", "II", "III"]): ax.text(1.07 + i * 1.7, 4.98, "generation " + g, color=TXT, fontsize=8, ha="center", va="top")
ax.text(0.3, 0.12, "Everything ordinary is generation I: u, d, e and νe. Generations II and III are heavier copies that decay into it. Masses from the Particle Data Group, 2024; the charge sits at the top right of each card.", color=TXT, fontsize=8.5)
ax.text(6.2, 1.55, "Every force is an exchange: two charges push apart by\ntrading photons, quarks stick by trading gluons, and a\nquark changes flavour by emitting a W. The Higgs is\nnot a force carrier; its field is what the other particles'\nmasses come from.", color=TXT, fontsize=8.8, va="top")
save(fig, "particle-physics-standard-model.svg")

# ── 2. the Z peak from synthetic muon pairs ─────────────────────────────────────────────────────────────────────
inv = np.load("particle-physics-zmass.npy") / 1000
fig, ax = plt.subplots(figsize=(9, 4.2))
ax.hist(inv, bins=60, range=(60, 120), color=PURPLE, alpha=0.75)
ax.axvline(91.19, color=RED, lw=1.2, ls="--"); ax.text(96, ax.get_ylim()[1] * 0.80, "the Z mass, 91.19 GeV", color=RED, fontsize=9)
ax.set_xlabel("invariant mass of the muon pair, √((E₁+E₂)² − |p₁+p₂|²) / GeV"); ax.set_ylabel("events")
ax.set_title(f"{len(inv)} simulated Z decays to a muon pair: the Z is never seen, only its mass, reconstructed from two tracks", fontsize=10)
ax.grid(alpha=.25)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
save(fig, "particle-physics-z-peak.svg")

# ── 3. two Feynman diagrams: beta-minus decay and muon decay ────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
def line(ax, p, q, col, lab=None, arrow=True, wavy=False, dashed=False):
    if wavy:
        t = np.linspace(0, 1, 200); dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy); nx, ny = -dy / L, dx / L
        off = 0.1 * np.sin(2 * math.pi * 7 * t)
        ax.plot(p[0] + dx * t + nx * off, p[1] + dy * t + ny * off, color=col, lw=1.6)
    else:
        ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>" if arrow else "-", color=col, lw=1.6, mutation_scale=14, linestyle="--" if dashed else "-"))
    if lab: ax.text(*lab[0], lab[1], color=col, fontsize=11, ha="center", va="center")
ax = axes[0]; ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off"); ax.set_title("β⁻ decay: a down quark becomes an up quark and a W⁻", color=TXT, fontsize=10)
for i, (q1, q2, col) in enumerate([("u", "u", PURPLE), ("d", "d", PURPLE), ("d", "u", RED)]):
    y = 1 + i * 1.2; line(ax, (0.5, y), (4.5, y), col, ((0.2, y), q1)); line(ax, (4.5, y), (9.5, y), col, ((9.8, y), q2))
ax.text(0.4, 0.3, "neutron (udd)", color=TXT, fontsize=9); ax.text(8.2, 0.3, "proton (uud)", color=TXT, fontsize=9)
line(ax, (4.5, 3.4), (6.5, 5.0), AMBER, ((5.0, 4.6), "W⁻"), wavy=True)
line(ax, (6.5, 5.0), (9.5, 5.6), BLUE, ((9.8, 5.6), "e⁻")); line(ax, (9.5, 4.2), (6.5, 5.0), BLUE, ((9.9, 4.2), "ν̄e"))
ax.text(1.0, 5.5, "time runs left to right", color=TXT, fontsize=8.5)
ax = axes[1]; ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off"); ax.set_title("muon decay: the same W, a different lepton in and out", color=TXT, fontsize=10)
line(ax, (0.5, 2.5), (4.5, 2.5), BLUE, ((0.2, 2.5), "μ⁻")); line(ax, (4.5, 2.5), (9.5, 4.0), BLUE, ((9.8, 4.0), "νμ"))
line(ax, (4.5, 2.5), (6.5, 1.0), AMBER, ((5.0, 1.3), "W⁻"), wavy=True)
line(ax, (6.5, 1.0), (9.5, 1.8), BLUE, ((9.8, 1.8), "e⁻")); line(ax, (9.5, 0.4), (6.5, 1.0), BLUE, ((9.9, 0.4), "ν̄e"))
ax.text(0.5, 5.5, "every vertex conserves charge and each lepton number;\nthe arrow pointing backwards is the antiparticle", color=TXT, fontsize=8.5, va="top")
save(fig, "particle-physics-feynman.svg")
print("wrote 3 SVGs")

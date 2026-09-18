"""
wave-particle-duality-figures.py — five figures for [[Wave-Particle Duality]]. Run the sim first.

  wave-particle-duality-dots.svg        photons landing one at a time: 10, 100, 1000, 20000, and one slit shut
  wave-particle-duality-photoelectric.svg   KE_max against frequency for three metals; Millikan's line for sodium
  wave-particle-duality-current.svg     photocurrent against p.d. for two intensities and two frequencies
  wave-particle-duality-de-broglie.svg  de Broglie wavelength against kinetic energy, electron and proton
  wave-particle-duality-tube.svg        the electron-diffraction tube and its rings
Vault style: text #888, no background rect, width="100%" + viewBox.
"""
import re, math, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
GREY = "#888888"; BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
S = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/3ef0ae3f-b718-4398-bf45-668809d171fe/scratchpad"
h, c, e, m_e, m_p = 6.626e-34, 2.998e8, 1.602e-19, 9.109e-31, 1.673e-27
def style(ax):
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelcolor=GREY); ax.xaxis.label.set_color(GREY); ax.yaxis.label.set_color(GREY); ax.title.set_color(GREY); ax.set_facecolor("none")
def save(fig, name):
    fig.patch.set_alpha(0); fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    s = open(name).read().replace('<svg ', '<svg width="100%" ', 1); s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1)
    open(name, "w").write(s); print("wrote", name)

# 1. dots — three rows of two
hits = np.load(f"{S}/photon-hits.npy"); hits1 = np.load(f"{S}/photon-hits-oneslit.npy")
rng = np.random.default_rng(3)
fig, axes = plt.subplots(3, 2, figsize=(10, 9))
panels = ((10, hits, "10 photons"), (100, hits, "100 photons"), (1000, hits, "1 000 photons"), (20000, hits, "20 000 photons"), (20000, hits1, "20 000 photons, one slit shut"), None)
for ax, pan in zip(axes.ravel(), panels):
    style(ax)
    if pan is None:
        xx = np.linspace(-0.3, 0.3, 2000); ax.plot(xx * 1e3, double_slit_density(xx) if 'double_slit_density' in dir() else np.interp(xx, np.linspace(-0.6, 0.6, 24001), np.load(f"{S}/photon-pdf.npy")), color=BLUE, lw=1.5)
        ax.set_title("what the wave predicts: the intensity pattern", fontsize=9.5); ax.set_yticks([]); ax.set_xlim(-300, 300); ax.set_xlabel("mm on the screen", fontsize=8); continue
    n, arr, lab = pan; xs = arr[:n] * 1e3; ys = rng.uniform(0, 1, n)
    ax.scatter(xs, ys, s=1.2 if n > 1000 else 6, color=AMBER, alpha=0.8 if n <= 1000 else 0.35)
    ax.set_xlim(-300, 300); ax.set_yticks([]); ax.set_title(lab, fontsize=9.5); ax.set_xlabel("mm on the screen", fontsize=8)
fig.suptitle("Two slits, one photon at a time: each dot is one arrival, and the fringes are where the wave says the dots may land", fontsize=10, color=GREY)
fig.tight_layout(); save(fig, "wave-particle-duality-dots.svg")

# 2. photoelectric KE vs f
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4))
for ax in (a1, a2): style(ax)
f = np.linspace(3e14, 12e14, 200)
for name, phi, col in (("caesium 2.14 eV", 2.14, RED), ("sodium 2.28 eV", 2.28, AMBER), ("zinc 4.31 eV", 4.31, BLUE)):
    ke = h * f / e - phi; ke[ke < 0] = np.nan
    a1.plot(f / 1e14, ke, color=col, lw=1.6, label=name)
    a1.plot(phi * e / h / 1e14, 0, "o", color=col, ms=5)
a1.axhline(0, color=GREY, lw=0.7); a1.set_xlabel("frequency f (10¹⁴ Hz)"); a1.set_ylabel("KE_max of photoelectrons (eV)")
a1.legend(fontsize=8, frameon=False, labelcolor=GREY, loc="upper left"); a1.set_title("hf = Φ + KE_max: same slope h for every metal, intercept f₀ = Φ/h", fontsize=9)
d = np.load(f"{S}/photoelectric.npz"); a2.plot(d["fs"] / 1e14, d["Vs"], "o", color=AMBER, ms=6)
sl, ic = np.polyfit(d["fs"], d["Vs"], 1); ff = np.linspace(5e14, 10.5e14, 2); a2.plot(ff / 1e14, sl * ff + ic, color=GREY, lw=1)
a2.set_xlabel("frequency f (10¹⁴ Hz)"); a2.set_ylabel("stopping voltage V_s (V)"); a2.set_title("Millikan 1916, sodium: the gradient is h/e", fontsize=9)
a2.text(6.0, 1.6, f"gradient {sl:.2e} V s\nh = gradient × e = {sl*e:.2e} J s", fontsize=8.5, color=GREY)
fig.tight_layout(); save(fig, "wave-particle-duality-photoelectric.svg")

# 3. current vs V
fig, ax = plt.subplots(figsize=(9, 4)); style(ax)
V = np.linspace(-2.5, 3, 400)
def I_of(V, Vs, I0):
    y = I0 * np.clip((V + Vs) / (Vs + 0.8), 0, 1) ** 0.5; y[V < -Vs] = 0; y[V > 0.8] = I0; return y
ax.plot(V, I_of(V, 1.0, 1.0), color=AMBER, lw=1.6, label="intensity I, frequency f")
ax.plot(V, I_of(V, 1.0, 2.0), color=RED, lw=1.6, label="intensity 2I, same f — twice the current, same stopping voltage")
ax.plot(V, I_of(V, 1.8, 1.0), color=BLUE, lw=1.6, ls="--", label="intensity I, higher f — same current, larger stopping voltage")
ax.axvline(0, color=GREY, lw=0.6); ax.axhline(0, color=GREY, lw=0.6)
ax.set_xlabel("p.d. across the cell (V)  —  negative: collector held back"); ax.set_ylabel("photocurrent"); ax.set_yticks([])
ax.annotate("−V_s: stopping voltage,\neV_s = KE_max", xy=(-1.0, 0), xytext=(-2.4, 0.9), color=GREY, fontsize=8.5, arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.8))
ax.legend(fontsize=8, frameon=False, labelcolor=GREY, loc="lower right"); ax.set_title("What the wave theory cannot draw: intensity moves the plateau, frequency moves the stopping voltage", fontsize=9)
fig.tight_layout(); save(fig, "wave-particle-duality-current.svg")

# 4. de Broglie
fig, ax = plt.subplots(figsize=(9, 4)); style(ax)
KE = np.logspace(0, 6, 300) * e
for name, m, col in (("electron", m_e, BLUE), ("proton", m_p, RED)):
    lam = h / np.sqrt(2 * m * KE); ax.plot(KE / e, lam, color=col, lw=1.6, label=name)
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlabel("kinetic energy (eV)"); ax.set_ylabel("de Broglie wavelength λ = h/p (m)")
ax.axhline(0.213e-9, color=GREEN, lw=0.8, ls=":"); ax.text(2e4, 0.26e-9, "graphite plane spacing 0.213 nm", color=GREEN, fontsize=8)
ax.plot(5000, h / math.sqrt(2 * m_e * 5000 * e), "o", color=AMBER, ms=7); ax.text(6500, h / math.sqrt(2 * m_e * 5000 * e), "the 5 kV tube: 17 pm", color=AMBER, fontsize=8.5, va="center")
ax.legend(fontsize=8.5, frameon=False, labelcolor=GREY); ax.set_title("λ = h/√(2mE): the electron's wavelength is atom-sized at a few keV — the proton's, 43× shorter at the same energy", fontsize=9)
fig.tight_layout(); save(fig, "wave-particle-duality-de-broglie.svg")

# 5. the tube
fig, ax = plt.subplots(figsize=(10, 4.3)); style(ax); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(-0.55, 3.9)
ax.add_patch(Ellipse((5.2, 1.9), 9.4, 3.0, fc=BLUE, ec=BLUE, alpha=0.06, lw=1.2)); ax.add_patch(Ellipse((5.2, 1.9), 9.4, 3.0, fc="none", ec=GREY, lw=1.2))
ax.plot([1.0, 1.0], [1.5, 2.3], color=RED, lw=3); ax.text(1.0, 2.45, "filament\ncathode", ha="center", va="bottom", fontsize=8, color=GREY)
ax.plot([2.2, 2.2], [1.2, 1.75], color=GREY, lw=3); ax.plot([2.2, 2.2], [2.05, 2.6], color=GREY, lw=3); ax.text(2.2, 2.75, "anode\n+ 5 kV", ha="center", va="bottom", fontsize=8, color=GREY)
ax.plot([3.4, 3.4], [1.55, 2.25], color=GREEN, lw=4); ax.text(3.4, 2.5, "graphite\nfilm", ha="center", va="bottom", fontsize=8, color=GREEN)
ax.add_patch(FancyArrowPatch((1.1, 1.9), (3.3, 1.9), arrowstyle="-|>", color=AMBER, lw=1.6, mutation_scale=12))
for ang in (0.35, -0.35, 0.62, -0.62):
    ax.add_patch(FancyArrowPatch((3.5, 1.9), (3.5 + 5.6 * math.cos(ang) * 0.95, 1.9 + 5.6 * math.sin(ang) * 0.42), arrowstyle="-|>", color=AMBER, lw=0.9, mutation_scale=9, alpha=0.7))
ax.add_patch(FancyArrowPatch((3.5, 1.9), (9.2, 1.9), arrowstyle="-|>", color=AMBER, lw=0.9, mutation_scale=9, alpha=0.7))
for r in (0.45, 0.85):
    ax.add_patch(Ellipse((9.2, 1.9), 0.5 * r, 2.6 * r, fc="none", ec=AMBER, lw=2.0))
ax.plot(9.2, 1.9, "o", color=AMBER, ms=8); ax.text(9.2, 3.35, "fluorescent screen:\nrings, not a spot", ha="center", va="bottom", fontsize=8, color=GREY)
ax.text(5.0, -0.35, "electrons accelerated by V have λ = h/√(2meV); the carbon planes, d = 0.21 nm apart, act as a grating: rings at sin θ = nλ/2d — raise V and the rings shrink", ha="center", fontsize=8, color=GREY)
ax.set_title("The electron-diffraction tube: a particle beam that draws an interference pattern", fontsize=10)
save(fig, "wave-particle-duality-tube.svg")

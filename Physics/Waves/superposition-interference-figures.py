"""
superposition-interference-figures.py — five figures for [[Superposition and Interference]].

  superposition-interference-ripple.svg   two point sources: the amplitude map with the lines of
                                          maxima (path difference nλ) and minima ((n+½)λ) drawn over it
  superposition-interference-young.svg    Young's geometry: slits a apart, screen D away, path
                                          difference a sin θ ≈ ax/D, and the intensity on the screen
  superposition-interference-coherence.svg  the time-averaged pattern for a constant vs a random phase
  superposition-interference-beats.svg    two tones 4 Hz apart and their sum's envelope
  superposition-interference-film.svg     soap-film reflectance vs thickness for three wavelengths

Vault style: text #888, no background rect, width="100%" + viewBox. Verify light + dark.
"""
import math, re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GREY = "#888888"
BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"

def style(ax):
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelcolor=GREY)
    ax.xaxis.label.set_color(GREY); ax.yaxis.label.set_color(GREY); ax.title.set_color(GREY)
    ax.set_facecolor("none")

def save(fig, name):
    fig.patch.set_alpha(0)
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    s = open(name).read()
    s = s.replace('<svg ', '<svg width="100%" ', 1)
    s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1)
    open(name, "w").write(s); print("wrote", name)

# ------------------------------------------------------------------ 1. ripple tank
lam, a = 2.0, 6.0
k = 2 * math.pi / lam
xs = np.linspace(-20, 20, 601); ys = np.linspace(0.3, 28, 421)
X, Y = np.meshgrid(xs, ys)
r1 = np.hypot(X + a / 2, Y); r2 = np.hypot(X - a / 2, Y)
field = np.exp(1j * k * r1) / np.sqrt(r1) + np.exp(1j * k * r2) / np.sqrt(r2)
amp = np.abs(field) * np.sqrt((r1 + r2) / 2)
fig, ax = plt.subplots(figsize=(8.5, 6))
style(ax)
ax.imshow(np.clip(amp / 2, 0, 1), extent=[xs[0], xs[-1], ys[0], ys[-1]], origin="lower", cmap="Blues", alpha=0.75, aspect="equal")
# lines of maxima and minima: r2 − r1 = nλ (hyperbolae), drawn as contours
pd = r2 - r1
for n in range(-3, 4):
    ax.contour(X, Y, pd, levels=[n * lam], colors=[GREEN], linewidths=1.6)
    ax.contour(X, Y, pd, levels=[(n + 0.5) * lam], colors=[RED], linewidths=1.0, linestyles="dashed")
ax.plot([-a / 2, a / 2], [0.3, 0.3], "o", color=AMBER, ms=8)
ax.text(-a / 2, -1.2, "S₁", color=AMBER, ha="center", fontsize=10); ax.text(a / 2, -1.2, "S₂", color=AMBER, ha="center", fontsize=10)
ax.text(0, 28.7, "n = 0", color=GREEN, ha="center", fontsize=9)
ax.text(10.3, 28.7, "n = 1", color=GREEN, ha="center", fontsize=9); ax.text(-10.3, 28.7, "n = −1", color=GREEN, ha="center", fontsize=9)
ax.text(4.9, 28.7, "½λ", color=RED, ha="center", fontsize=8.5); ax.text(16.6, 28.7, "1½λ", color=RED, ha="center", fontsize=8.5)
ax.text(-4.9, 28.7, "½λ", color=RED, ha="center", fontsize=8.5); ax.text(-16.6, 28.7, "1½λ", color=RED, ha="center", fontsize=8.5)
ax.set_xlim(-20, 20); ax.set_ylim(-2.5, 30)
ax.set_xlabel("cm"); ax.set_ylabel("cm")
ax.set_title("Two in-phase sources, λ = 2 cm, 6 cm apart — shading: amplitude of the sum; solid: path difference nλ; dashed: (n + ½)λ", fontsize=9.5)
fig.tight_layout(); save(fig, "superposition-interference-ripple.svg")

# ------------------------------------------------------------------ 2. Young's geometry + screen
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.6, 1]})
for ax in (ax1, ax2): style(ax)
ax1.set_xlim(-0.6, 6.4); ax1.set_ylim(-2.2, 2.6); ax1.set_aspect("equal"); ax1.axis("off")
# slits at x=0, y=±0.35 (a exaggerated); screen at x=5.5
ax1.plot([0, 0], [-2, -0.5], color=GREY, lw=3); ax1.plot([0, 0], [-0.2, 0.2], color=GREY, lw=3); ax1.plot([0, 0], [0.5, 2], color=GREY, lw=3)
ax1.plot([5.5, 5.5], [-2, 2.3], color=GREY, lw=2)
for yy in (-0.35, 0.35): ax1.plot(0, yy, "o", color=AMBER, ms=6)
ax1.annotate("", xy=(0.35, 0.35), xytext=(0.35, -0.35), arrowprops=dict(arrowstyle="<->", color=AMBER)); ax1.text(0.5, 0, "a", color=AMBER, fontsize=11, va="center")
P = (5.5, 1.5)
for yy in (-0.35, 0.35): ax1.plot([0, P[0]], [yy, P[1]], color=BLUE, lw=1.2)
ax1.plot(*P, "o", color=GREEN, ms=6); ax1.text(5.65, 1.5, "P (bright if\nΔ = nλ)", color=GREEN, fontsize=9, va="center")
ax1.plot([0, 5.5], [0, 0], color=GREY, lw=0.8, ls=":"); ax1.plot(5.5, 0, "o", color=GREEN, ms=5); ax1.text(5.65, 0, "O, central\nbright", color=GREEN, fontsize=9, va="center")
ax1.annotate("", xy=(5.5, -1.9), xytext=(0, -1.9), arrowprops=dict(arrowstyle="<->", color=GREY)); ax1.text(2.75, -2.15, "D (≫ a)", color=GREY, ha="center", fontsize=10)
ax1.annotate("", xy=(5.9, 1.5), xytext=(5.9, 0), arrowprops=dict(arrowstyle="<->", color=GREY)); ax1.text(6.05, 0.75, "x", color=GREY, fontsize=11, va="center")
# the extra path: foot of perpendicular from upper slit onto the lower ray (marked)
ax1.plot([0, 0.19], [-0.35, 0.29], color=RED, lw=1.4)
ax1.text(1.0, -0.9, "extra path Δ = a sin θ ≈ ax/D", color=RED, fontsize=10)
ax1.text(1.15, 0.12, "θ", color=BLUE, fontsize=11)
ax1.set_title("Young's double slit — the geometry behind λ = ax/D", fontsize=10)
# screen intensity
lam_, a_, D_ = 600e-9, 0.50e-3, 2.0
x = np.linspace(-0.012, 0.012, 4001)
I = np.cos(math.pi * a_ * x / (lam_ * D_)) ** 2
ax2.plot(I, x * 1e3, color=BLUE, lw=1.6)
ax2.fill_betweenx(x * 1e3, 0, I, color=BLUE, alpha=0.12)
ax2.set_xlabel("intensity (relative)"); ax2.set_ylabel("position on screen x (mm)")
ax2.set_title("On the screen: λ = 600 nm, a = 0.50 mm, D = 2.0 m", fontsize=10)
sp = lam_ * D_ / a_ * 1e3
ax2.annotate("", xy=(1.05, sp), xytext=(1.05, 0), arrowprops=dict(arrowstyle="<->", color=AMBER)); ax2.text(1.08, sp / 2, f"λD/a\n= {sp:.1f} mm", color=AMBER, fontsize=9, va="center")
ax2.set_xlim(0, 1.5)
fig.tight_layout(); save(fig, "superposition-interference-young.svg")

# ------------------------------------------------------------------ 3. coherence
lamc = 1.0; kc = 2 * math.pi / lamc; ac = 3.0; Dc = 40.0
xc = np.linspace(-10, 10, 1201)
r1 = np.hypot(xc + ac / 2, Dc); r2 = np.hypot(xc - ac / 2, Dc)
rng = np.random.default_rng(7)
coh = np.abs(np.exp(1j * kc * r1) + np.exp(1j * kc * r2)) ** 2 / 4
inst = [np.abs(np.exp(1j * kc * r1) + np.exp(1j * (kc * r2 + rng.uniform(0, 2 * math.pi)))) ** 2 / 4 for _ in range(400)]
avg = np.mean(inst, axis=0)
fig, axes = plt.subplots(1, 3, figsize=(11, 3.3), sharey=True)
for ax in axes: style(ax)
axes[0].plot(xc, coh, color=GREEN, lw=1.5); axes[0].set_title("coherent: constant phase difference\n— the pattern holds still", fontsize=9.5)
for i in range(3): axes[1].plot(xc, inst[i], lw=1.0, alpha=0.8, color=[BLUE, PURPLE, TEAL][i])
axes[1].set_title("two independent lamps: three instants\n— a perfect pattern each time, in a different place", fontsize=9.5)
axes[2].plot(xc, avg, color=RED, lw=1.5); axes[2].set_title("the same lamps averaged over the eye's\nresponse time — uniform: no fringes", fontsize=9.5)
axes[0].set_ylabel("intensity"); axes[1].set_xlabel("position across the screen")
axes[2].set_ylim(0, 1.05)
fig.tight_layout(); save(fig, "superposition-interference-coherence.svg")

# ------------------------------------------------------------------ 4. beats
t = np.linspace(0, 1.0, 20001)
f1, f2 = 440.0, 444.0
y1, y2 = np.sin(2 * math.pi * f1 * t), np.sin(2 * math.pi * f2 * t)
fig, axes = plt.subplots(3, 1, figsize=(10, 5), sharex=True)
for ax in axes: style(ax)
axes[0].plot(t, y1, color=BLUE, lw=0.5); axes[0].set_ylabel("440 Hz")
axes[1].plot(t, y2, color=PURPLE, lw=0.5); axes[1].set_ylabel("444 Hz")
axes[2].plot(t, y1 + y2, color=TEAL, lw=0.5); axes[2].plot(t, 2 * np.cos(2 * math.pi * (f2 - f1) / 2 * t), color=RED, lw=1.5); axes[2].plot(t, -2 * np.cos(2 * math.pi * (f2 - f1) / 2 * t), color=RED, lw=1.5)
axes[2].set_ylabel("sum"); axes[2].set_xlabel("time (s)")
axes[2].text(0.5, 2.3, "envelope 2cos(2π·2t): loudness pulses 4 times a second — f_beat = |f₁ − f₂| = 4 Hz", color=RED, ha="center", fontsize=9)
axes[2].set_ylim(-2.9, 2.9)
axes[0].set_title("Beats — two tones 4 Hz apart drift in and out of phase, and the sum's amplitude breathes", fontsize=10)
fig.tight_layout(); save(fig, "superposition-interference-beats.svg")

# ------------------------------------------------------------------ 5. thin film
n = 1.33
tf = np.linspace(0, 700, 1401)
fig, ax = plt.subplots(figsize=(10, 3.8))
style(ax)
for lam_nm, col, name in ((450, BLUE, "blue 450 nm"), (550, GREEN, "green 550 nm"), (650, RED, "red 650 nm")):
    R = np.cos(2 * math.pi * n * tf / lam_nm + math.pi / 2) ** 2      # |1 + e^{i(4πnt/λ + π)}|²/4
    ax.plot(tf, R, color=col, lw=1.5, label=name)
ax.axvspan(0, 25, color=GREY, alpha=0.15); ax.text(12, 0.9, "black\nfilm", color=GREY, ha="center", fontsize=8.5)
ax.set_xlabel("film thickness t (nm), soap n = 1.33, normal incidence"); ax.set_ylabel("reflected fraction (relative)")
ax.set_title("A soap film reflects each colour at its own thicknesses: bright when 2nt = (m + ½)λ, because the top reflection flips by π", fontsize=10)
ax.legend(loc="upper right", fontsize=8.5, frameon=False, labelcolor=GREY)
fig.tight_layout(); save(fig, "superposition-interference-film.svg")

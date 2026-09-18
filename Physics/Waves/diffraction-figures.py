"""
diffraction-figures.py — five figures for [[Diffraction]]. Run diffraction-sim.py first.

  diffraction-single-slit.svg   the single-slit pattern with its minima at sin θ = mλ/a, and the
                                width of the central maximum against a/λ
  diffraction-double-envelope.svg  two slits of finite width: Young's fringes under the single-slit
                                envelope, with the missing order marked
  diffraction-grating-n.svg     2, 5, 20, 100 slits: the maxima stay put and sharpen
  diffraction-ripple-gaps.svg   the 2-D wave through gaps of ½λ, 1λ, 2λ, 6λ
  diffraction-grating-geometry.svg   d sin θ = nλ from the path difference between neighbouring slits
Vault style: text #888, no background rect, width="100%" + viewBox.
"""
import re, math, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
GREY = "#888888"; BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
S = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad"
def style(ax):
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelcolor=GREY); ax.xaxis.label.set_color(GREY); ax.yaxis.label.set_color(GREY); ax.title.set_color(GREY); ax.set_facecolor("none")
def save(fig, name):
    fig.patch.set_alpha(0); fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    s = open(name).read().replace('<svg ', '<svg width="100%" ', 1)
    s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1)
    open(name, "w").write(s); print("wrote", name)

# 1. single slit
d1 = np.load(f"{S}/single.npz"); th, I = d1["th"], d1["I"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 3.9))
for ax in (a1, a2): style(ax)
a1.plot(np.sin(th), I, color=BLUE, lw=1.5)
for m in (1, 2, 3):
    for sgn in (1, -1): a1.axvline(sgn * m * 0.2, color=RED, lw=0.7, ls=":")
a1.text(0.2, 0.55, "sin θ = λ/a", color=RED, fontsize=8.5, rotation=90, va="bottom"); a1.text(0.4, 0.55, "2λ/a", color=RED, fontsize=8.5, rotation=90, va="bottom")
a1.set_xlim(-0.7, 0.7); a1.set_xlabel("sin θ"); a1.set_ylabel("intensity / I(0)"); a1.set_title("A single slit, a = 5λ: minima at sin θ = mλ/a, central peak twice as wide", fontsize=9)
a1.annotate("first side maximum: 4.7%", xy=(0.29, 0.047), xytext=(0.36, 0.3), color=GREY, fontsize=8, arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.8))
ratios = np.array([1, 1.5, 2, 3, 5, 8, 12, 20]); half = np.degrees(np.arcsin(1 / ratios))
a2.plot(ratios, half, "o-", color=PURPLE, lw=1.5); a2.set_xscale("log"); a2.set_xlabel("slit width ÷ wavelength, a/λ"); a2.set_ylabel("half-width of the central maximum (°)")
a2.set_title("Narrow slit, wide spread: sin θ₁ = λ/a", fontsize=9)
a2.text(1.05, 82, "a ≤ λ: no minimum at all —\nthe slit radiates like a point", fontsize=8, color=GREY, va="top")
fig.tight_layout(); save(fig, "diffraction-single-slit.svg")

# 2. double slit with envelope
d2 = np.load(f"{S}/double.npz"); th, I2, I1 = d2["th"], d2["I2"], d2["I1"]
fig, ax = plt.subplots(figsize=(10, 3.8)); style(ax)
ax.plot(np.sin(th), I2, color=BLUE, lw=1.2, label="two slits, width 2 μm, 10 μm apart")
ax.plot(np.sin(th), I1, color=RED, lw=1.4, ls="--", label="one slit of width 2 μm (the envelope)")
ax.axvline(0.3, color=AMBER, lw=1.0, ls=":"); ax.text(0.302, 0.6, "order 5 should be here (d sin θ = 5λ)\nbut sin θ = λ/a: the missing order", fontsize=8, color=AMBER)
ax.set_xlim(-0.42, 0.42); ax.set_xlabel("sin θ"); ax.set_ylabel("intensity / I(0)"); ax.legend(fontsize=8, frameon=False, labelcolor=GREY, loc="upper left")
ax.set_title("Young's fringes are always inside a single-slit envelope, because each slit has a width", fontsize=9.5)
fig.tight_layout(); save(fig, "diffraction-double-envelope.svg")

# 3. grating N
d3 = np.load(f"{S}/grating.npz"); th = d3["th"]
fig, axes = plt.subplots(4, 1, figsize=(10, 6.2), sharex=True)
for ax, N, col in zip(axes, (2, 5, 20, 100), (BLUE, TEAL, PURPLE, GREEN)):
    style(ax); ax.plot(np.sin(th), d3[f"N{N}"], color=col, lw=1.1); ax.set_ylim(0, 1.08); ax.set_yticks([]); ax.text(-0.98, 0.8, f"N = {N}", color=col, fontsize=10)
for n in range(-4, 5):
    for ax in axes: ax.axvline(n * 0.24, color=GREY, lw=0.5, ls=":")
axes[-1].set_xlabel("sin θ   (dotted: d sin θ = nλ, n = −4 … 4; d = 2.5 μm, λ = 600 nm — the fifth order needs sin θ > 1 and does not exist)")
axes[0].set_title("More slits: the maxima do not move, they sharpen (width ∝ 1/N) and brighten (∝ N²)", fontsize=9.5)
fig.tight_layout(); save(fig, "diffraction-grating-n.svg")

# 4. ripple gaps
d4 = np.load(f"{S}/ripple.npz")
fig, axes = plt.subplots(1, 4, figsize=(13, 3.6))
for ax, g in zip(axes, (0.5, 1.0, 2.0, 6.0)):
    style(ax); u = d4[f"g{g}"]; n = u.shape[0]; wall = n // 3
    ax.imshow(np.clip(u[wall - 20:wall + 200, :] / 0.8, -1, 1), cmap="RdBu", origin="lower", extent=[-20, 20, -2.5, 25], aspect="equal")
    gw = g * 1.0
    ax.plot([-20, -gw / 2], [0, 0], color=GREY, lw=3); ax.plot([gw / 2, 20], [0, 0], color=GREY, lw=3)
    ax.set_title(f"gap = {g:g} λ", fontsize=9.5); ax.set_xticks([]); ax.set_yticks([])
fig.suptitle("A plane wave meets a barrier with a gap (2-D wave equation): the narrower the gap, the more the wave spreads", fontsize=9.5, color=GREY)
fig.tight_layout(); save(fig, "diffraction-ripple-gaps.svg")

# 5. grating geometry
fig, ax = plt.subplots(figsize=(9, 4)); style(ax); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5)
for i in range(6):
    y = 0.6 + i * 0.75
    ax.plot([2, 2], [y + 0.12, y + 0.63], color=GREY, lw=4)
ax.plot([2, 2], [0.0, 0.6], color=GREY, lw=4); ax.plot([2, 2], [0.6 + 5 * 0.75 + 0.63, 5], color=GREY, lw=4)
for i in range(6):
    y = 0.6 + i * 0.75 + 0.06
    ax.add_patch(FancyArrowPatch((0.3, y), (1.9, y), arrowstyle="-|>", color=BLUE, lw=1.0, mutation_scale=9))
    ax.add_patch(FancyArrowPatch((2.05, y), (2.05 + 4.5 * math.cos(0.5), y + 4.5 * math.sin(0.5) * 0.35), arrowstyle="-|>", color=GREEN, lw=1.0, mutation_scale=9))
ax.text(0.3, 4.6, "plane wave in\n(λ)", color=BLUE, fontsize=9)
ax.annotate("", xy=(2.7, 0.66), xytext=(2.7, 1.41), arrowprops=dict(arrowstyle="<->", color=AMBER)); ax.text(2.85, 1.0, "d", color=AMBER, fontsize=11, va="center")
ax.plot([2.05, 2.05 + 0.66 * math.sin(0.5)], [1.41, 1.41 - 0.66 * math.cos(0.5)], color=RED, lw=1.6)
ax.text(3.4, 0.55, "extra path between neighbours = d sin θ\nmaximum when d sin θ = nλ — every slit in step", color=RED, fontsize=9)
ax.text(5.6, 3.3, "θ", color=GREEN, fontsize=12)
ax.text(6.8, 4.3, "to the n-th order maximum", color=GREEN, fontsize=9)
ax.set_title("The grating: many slits d apart, and the same rule as two — but only exact agreement survives", fontsize=10)
save(fig, "diffraction-grating-geometry.svg")

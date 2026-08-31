"""Figures for [[Circular Motion]] — matplotlib, vault palette, light/dark-safe.
Every arrow endpoint is computed from the geometry; nothing is placed by eye.
(mathtext here avoids \\vec, \\to, \\perp, \\Rightarrow, \\tfrac — the vault's SVG fonts
have no glyphs for them, so they render as tofu; words are used instead.)

  circular-motion-velocity-triangle.svg   the still of the proof: two tangent velocities
                                          on the circle, then the same two drawn from one
                                          start — Δv is the base of an isosceles triangle,
                                          |Δv| ≈ v Δθ, pointing at the centre
  circular-motion-force-cast.svg          2×2: conical pendulum, banked track, flat bend,
                                          top of a loop — real forces only
  circular-motion-string-vertical.svg     the generic vertical circle on a string: θ from
                                          the bottom, h = r(1 − cos θ), T, mg and its
                                          radial/tangential parts, u at the bottom
  circular-motion-vertical-tension.svg    two rows: T/mg round the circle for four
                                          launches; v²/(gr) with the slack boundary
  circular-motion-q-bowl.svg              9231 J26/33 Q1 / N25/31 Q2 — the hemispherical bowl
  circular-motion-q-disc.svg              9231 J25/31 — rough rotating disc + elastic string
  circular-motion-q-sphere-outer.svg      9231 J26/33 — slide-off from the outside of a sphere
  circular-motion-q-sphere-inner.svg      9231 J25/31 Q7 — the cut hollow sphere

Run from this folder:  python3 circular-motion-figures.py
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch

GREY = "#888888"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
RED = "#dc2626"
AMBER = "#f59e0b"
TEAL = "#0891b2"

plt.rcParams.update({
    "font.family": "Helvetica Neue",
    "font.size": 11,
    "text.color": GREY,
    "axes.labelcolor": GREY,
    "axes.edgecolor": GREY,
    "xtick.color": GREY,
    "ytick.color": GREY,
    "axes.facecolor": "none",
    "figure.facecolor": "none",
    "savefig.facecolor": "none",
    "savefig.transparent": True,
    "svg.fonttype": "none",
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def arrow(ax, p, q, color, lw=2.2, label=None, lpos=None, fs=11, ls="-", ms=14, ha="center"):
    p = np.asarray(p, float); q = np.asarray(q, float)
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms,
                                 color=color, lw=lw, shrinkA=0, shrinkB=0, linestyle=ls))
    if label:
        lp = lpos if lpos is not None else q
        ax.text(lp[0], lp[1], label, color=color, fontsize=fs, ha=ha, va="center")


def dim(ax, p, q, label, lpos, fs=10, color=GREY):
    """a two-headed dimension line with a label"""
    arrow(ax, p, q, color, lw=1, ms=9); arrow(ax, q, p, color, lw=1, ms=9)
    ax.text(lpos[0], lpos[1], label, color=color, fontsize=fs, ha="center", va="center")


def blank(ax, xl, yl):
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl)


def unit(a):
    return np.array([np.cos(a), np.sin(a)])


# ================================================================ velocity triangle
def velocity_triangle():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.4))
    Rr = 2.0
    O = np.array([0.0, 0.0])
    p1, p2 = np.radians(55), np.radians(100)
    P1, P2 = O + Rr * unit(p1), O + Rr * unit(p2)
    Lv = 1.5
    v1 = Lv * np.array([-np.sin(p1), np.cos(p1)])
    v2 = Lv * np.array([-np.sin(p2), np.cos(p2)])

    blank(ax1, (-3.2, 3.2), (-2.9, 3.7))
    ax1.add_patch(Circle(O, Rr, fill=False, color=GREY, lw=1.3, ls="--"))
    ax1.plot(*O, "+", color=GREY, ms=9)
    ax1.text(O[0] + 0.12, O[1] - 0.3, "O", color=GREY)
    for P in (P1, P2):
        ax1.plot([O[0], P[0]], [O[1], P[1]], color=GREY, lw=1, ls=":")
        ax1.add_patch(Circle(P, 0.09, color=BLUE))
    ax1.text(P1[0] + 0.22, P1[1] - 0.25, "$P_1$", color=BLUE)
    ax1.text(P2[0] - 0.45, P2[1] - 0.05, "$P_2$", color=BLUE)
    arrow(ax1, P1, P1 + v1, GREEN, lw=2.6, label="$v_1$", lpos=P1 + v1 + [0.28, 0.12], fs=13)
    arrow(ax1, P2, P2 + v2, GREEN, lw=2.6, label="$v_2$", lpos=P2 + v2 + [-0.3, 0.14], fs=13)
    ax1.add_patch(Arc(O, 1.3, 1.3, theta1=np.degrees(p1), theta2=np.degrees(p2), color=AMBER, lw=1.5))
    am = (p1 + p2) / 2
    ax1.text(*(O + 0.95 * unit(am)), r"$\Delta\theta$", color=AMBER, ha="center", va="center", fontsize=12)
    ax1.text(0, -2.55, "same speed $v$ at both instants — only the direction has turned,\nby the angle $\\Delta\\theta = \\omega\\,\\Delta t$ that the radius swept",
             color=GREY, ha="center", fontsize=10.5)
    ax1.set_title("On the circle: the velocity at two instants, $\\Delta t$ apart", color=GREY)

    blank(ax2, (-3.9, 2.2), (-2.1, 4.0))
    S = np.array([0.0, 0.0])
    k = 1.7
    w1, w2 = k * v1, k * v2
    arrow(ax2, S, S + w1, GREEN, lw=2.8, label="$v_1$", lpos=S + w1 * 0.55 + [0.38, -0.05], fs=13)
    arrow(ax2, S, S + w2, GREEN, lw=2.8, label="$v_2$", lpos=S + w2 * 0.55 + [0.0, -0.4], fs=13)
    tip1, tip2 = S + w1, S + w2
    arrow(ax2, tip1, tip2, AMBER, lw=2.8, label=r"$\Delta v = v_2 - v_1$", lpos=(tip1 + tip2) / 2 + [-0.95, 0.25], fs=12)
    a1 = np.degrees(np.arctan2(w1[1], w1[0])); a2 = np.degrees(np.arctan2(w2[1], w2[0]))
    if a2 < a1:
        a2 += 360
    ax2.add_patch(Arc(S, 1.3, 1.3, theta1=a1, theta2=a2, color=AMBER, lw=1.5))
    ax2.text(*(S + 0.95 * unit(np.radians((a1 + a2) / 2))), r"$\Delta\theta$", color=AMBER, ha="center", va="center", fontsize=12)
    ax2.text(S[0] + 0.1, S[1] + 0.22, "common start", color=GREY, fontsize=9)
    rm = unit(am)
    side = np.array([-rm[1], rm[0]]) * 0.38
    mid = (tip1 + tip2) / 2 + side
    arrow(ax2, mid + 0.55 * rm, mid - 0.85 * rm, GREY, lw=1.3, ls="--", ms=10)
    ax2.text(*(mid - 0.85 * rm + [0.0, -0.42]), "direction to the centre,\ncopied from the midpoint\nof the arc", color=GREY, fontsize=9, ha="center", va="top")
    ax2.text(-0.85, 3.7, "isosceles: two sides of length $v$, apex angle $\\Delta\\theta$", color=GREY, fontsize=11, ha="center")
    ax2.text(-0.85, 3.2, r"$|\Delta v| = 2v\sin\frac{\Delta\theta}{2} \approx v\,\Delta\theta$", color=AMBER, fontsize=12.5, ha="center")
    ax2.text(-0.85, 2.65, r"so  $a = \frac{|\Delta v|}{\Delta t} = v\omega = \frac{v^2}{r}$", color=AMBER, fontsize=12.5, ha="center")
    ax2.text(-0.85, -1.75, "as $\\Delta\\theta$ shrinks the base turns perpendicular to the sides:\n$\\Delta v$ is at right angles to $v$ — along the radius, inward", color=GREY, fontsize=10, ha="center")
    ax2.set_title("From one common start: the velocity triangle", color=GREY)
    fig.tight_layout()
    fig.savefig("circular-motion-velocity-triangle.svg")
    plt.close(fig)


# ================================================================ force cast 2x2
def force_cast():
    fig, axs = plt.subplots(2, 2, figsize=(11, 10))
    axs = axs.ravel()
    for ax in axs:
        blank(ax, (-2.4, 2.4), (-2.5, 2.4))

    ax = axs[0]
    th = np.radians(35)
    L = 2.7
    top = np.array([0.0, 2.0])
    bob = top + L * np.array([np.sin(th), -np.cos(th)])
    ax.plot([top[0], bob[0]], [top[1], bob[1]], color=GREY, lw=1.5)
    ax.plot([top[0], top[0]], [top[1], bob[1] - 0.3], color=GREY, lw=0.8, ls="--")
    ax.plot([bob[0], 0], [bob[1], bob[1]], color=GREY, lw=0.8, ls=":")
    ax.text(bob[0] / 2, bob[1] + 0.12, "$r = L\\sin\\theta$", color=GREY, fontsize=10, ha="center")
    ax.text(top[0] - 0.55, (top[1] + bob[1]) / 2, "$h = L\\cos\\theta$", color=GREY, fontsize=10, ha="center")
    ax.add_patch(Circle(bob, 0.13, color=BLUE))
    Tlen = 1.35
    T = Tlen * np.array([-np.sin(th), np.cos(th)])
    arrow(ax, bob, bob + T, BLUE, label=r"$T$", lpos=bob + T + [-0.22, 0.12])
    arrow(ax, bob, bob + [0, -1.05], RED, label=r"$mg$", lpos=bob + [0.32, -1.05])
    arrow(ax, bob, bob + [-(Tlen * np.sin(th)), 0], AMBER, lw=2.6, label="to centre", lpos=bob + [-0.55, -0.3], fs=10)
    ax.add_patch(Arc(top, 0.9, 0.9, theta1=270, theta2=270 + 35, color=GREY, lw=1))
    ax.text(top[0] + 0.2, top[1] - 0.72, r"$\theta$", color=GREY)
    ax.text(0, -2.2, "conical pendulum\n" + r"$T\sin\theta = mr\omega^2,\; T\cos\theta = mg$  so  $\omega^2 = g/h$",
            color=GREY, ha="center", fontsize=10.5)

    ax = axs[1]
    ph = np.radians(28)
    base = np.array([-1.9, -1.2])
    slope = unit(ph)
    ax.plot([base[0], base[0] + 3.8 * np.cos(ph)], [base[1], base[1] + 3.8 * np.sin(ph)], color=GREY, lw=1.5)
    ax.plot([base[0], base[0] + 3.8 * np.cos(ph)], [base[1], base[1]], color=GREY, lw=0.8, ls=":")
    car = base + 2.1 * slope
    ax.add_patch(Circle(car, 0.13, color=BLUE))
    n_hat = np.array([-np.sin(ph), np.cos(ph)])
    Nlen = 1.45
    arrow(ax, car, car + Nlen * n_hat, BLUE, label=r"$N$", lpos=car + Nlen * n_hat + [-0.22, 0.15])
    arrow(ax, car, car + [0, -Nlen * np.cos(ph)], RED, label=r"$mg$", lpos=car + [0.34, -Nlen * np.cos(ph)])
    arrow(ax, car, car + [-Nlen * np.sin(ph), 0], AMBER, lw=2.6, label="to centre", lpos=car + [-0.6, 0.3], fs=10)
    ax.add_patch(Arc(base, 1.3, 1.3, theta1=0, theta2=28, color=GREY, lw=1))
    ax.text(base[0] + 0.8, base[1] + 0.14, r"$\theta$", color=GREY)
    ax.text(0, -2.2, "banked track, no friction\n" + r"$N\sin\theta = \frac{mv^2}{r},\; N\cos\theta = mg$  so  $v^2 = rg\tan\theta$",
            color=GREY, ha="center", fontsize=10.5)

    ax = axs[2]
    ax.plot([-2.1, 2.1], [-0.8, -0.8], color=GREY, lw=1.5)
    car = np.array([0.3, -0.67])
    ax.add_patch(Circle(car, 0.13, color=BLUE))
    arrow(ax, car, car + [0, 1.1], BLUE, label=r"$N$", lpos=car + [0.27, 1.15])
    arrow(ax, car, car + [0, -1.1], RED, label=r"$mg$", lpos=car + [0.36, -1.05])
    arrow(ax, car, car + [-1.45, 0], PURPLE, label=r"$F$ (friction)", lpos=car + [-0.8, -0.34])
    arrow(ax, car + [0, 0.06], car + [-1.45, 0.06], AMBER, lw=2.6, label="to centre", lpos=car + [-0.8, 0.34], fs=10)
    ax.text(1.35, 0.0, "bend centre is\nthis way", color=GREY, fontsize=9, ha="center")
    arrow(ax, [1.35, -0.25], [0.75, -0.55], GREY, lw=1, ms=9)
    ax.text(0, -2.2, "flat bend: friction alone\n" + r"$F = \frac{mv^2}{r} \leq \mu mg$  so  $v \leq \sqrt{\mu g r}$",
            color=GREY, ha="center", fontsize=10.5)

    ax = axs[3]
    Rl = 1.45
    ctr = np.array([0.0, -0.35])
    ax.add_patch(Circle(ctr, Rl, fill=False, color=GREY, lw=1.2, ls="--"))
    top = ctr + [0, Rl]
    ax.add_patch(Circle(top, 0.13, color=BLUE))
    arrow(ax, top, top + [0, -0.8], BLUE, label=r"$N$", lpos=top + [0.3, -0.62])
    arrow(ax, top + [0.07, 0], top + [0.07, -1.55], RED, label=r"$mg$", lpos=top + [0.42, -1.5])
    arrow(ax, top + [-0.6, 0.2], top + [-0.6, -0.95], AMBER, lw=2.6, label="to centre", lpos=top + [-1.3, -0.35], fs=10)
    ax.plot(ctr[0], ctr[1], "+", color=GREY, ms=8)
    ax.text(ctr[0] + 0.15, ctr[1] - 0.25, "centre", color=GREY, fontsize=9)
    ax.text(0, -2.2, "top of a loop: both forces point inward\n" + r"$N + mg = \frac{mv^2}{r}$;  $N = 0$ gives $v_{\min} = \sqrt{gr}$",
            color=GREY, ha="center", fontsize=10.5)

    fig.suptitle("Centripetal force is a role, not a new force — real forces only, then resolve toward the centre",
                 color=GREY, fontsize=12.5)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig("circular-motion-force-cast.svg")
    plt.close(fig)


# ================================================================ generic vertical circle on a string
def string_vertical():
    fig, ax = plt.subplots(figsize=(9, 8))
    blank(ax, (-3.5, 4.9), (-3.5, 3.8))
    O = np.array([0.0, 0.0]); r = 2.4
    ax.add_patch(Circle(O, r, fill=False, color=GREY, lw=1.2, ls="--"))
    ax.plot(*O, "+", color=GREY, ms=10); ax.text(0.12, 0.15, "O", color=GREY)
    th = np.radians(62)
    P = O + r * np.array([np.sin(th), -np.cos(th)])
    bottom = O + [0, -r]
    ax.plot([O[0], P[0]], [O[1], P[1]], color=GREY, lw=1.6)
    ax.plot([O[0], O[0]], [O[1], bottom[1] - 0.2], color=GREY, lw=0.8, ls=":")
    ax.add_patch(Arc(O, 1.4, 1.4, theta1=270, theta2=270 + 62, color=AMBER, lw=1.5))
    ax.text(*(O + 0.95 * np.array([np.sin(th / 2), -np.cos(th / 2)])), r"$\theta$", color=AMBER, ha="center", va="center", fontsize=12)
    ax.add_patch(Circle(P, 0.12, color=BLUE)); ax.add_patch(Circle(bottom, 0.09, color=GREY))
    ax.text(P[0] + 0.25, P[1] + 0.1, "P", color=BLUE)
    rin = (O - P) / np.linalg.norm(O - P)
    tang = np.array([np.cos(th), np.sin(th)])
    arrow(ax, P, P + 1.5 * rin, BLUE, lw=2.4, label="$T$", lpos=P + 1.5 * rin + 0.32 * tang, fs=12)
    arrow(ax, P, P + [0, -1.4], RED, lw=2.4, label="$mg$", lpos=P + [0.35, -1.4], fs=12)
    wr = 1.0 * np.cos(th) * (-rin); wt = 1.0 * np.sin(th) * (-tang)
    arrow(ax, P, P + wr, RED, lw=1.4, ls="--", label=r"$mg\cos\theta$ (outward here)", lpos=P + wr + [1.05, 0.0], fs=10)
    arrow(ax, P, P + wt, RED, lw=1.4, ls="--", label=r"$mg\sin\theta$", lpos=P + wt + [-0.75, 0.12], fs=10)
    arrow(ax, P + 0.18 * tang, P + 1.15 * tang, GREEN, lw=2.2, label="$v$", lpos=P + 1.15 * tang + [0.25, 0.12], fs=12)
    arrow(ax, bottom + [0.18, 0], bottom + [1.3, 0], GREEN, lw=2.2, label="$u$", lpos=bottom + [1.3, -0.32], fs=12)
    xh = 3.7
    ax.plot([P[0], xh + 0.15], [P[1], P[1]], color=GREY, lw=0.8, ls=":")
    ax.plot([bottom[0], xh + 0.15], [bottom[1], bottom[1]], color=GREY, lw=0.8, ls=":")
    dim(ax, [xh, bottom[1]], [xh, P[1]], "$h = r - r\\cos\\theta$\n$= r(1-\\cos\\theta)$", [xh + 0.6, (P[1] + bottom[1]) / 2 - 0.05], fs=10.5)
    ax.plot([O[0], O[0]], [O[1], P[1]], color=GREY, lw=0.8, ls=":")
    ax.text(O[0] - 0.9, (O[1] + P[1]) / 2, "$r\\cos\\theta$", color=GREY, fontsize=10)
    ax.text(0.7, 3.5, "Energy, bottom to P:  $\\frac{1}{2}mu^2 = \\frac{1}{2}mv^2 + mg\\,r(1-\\cos\\theta)$", color=GREY, fontsize=11.5, ha="center")
    ax.text(0.7, 2.95, "Toward O:  $T - mg\\cos\\theta = mv^2/r$   (the $\\cos\\theta$ carries the sign)", color=GREY, fontsize=11.5, ha="center")
    ax.text(0.7, -3.25, "$\\theta$ measured from the bottom. Below the centre's level the weight's radial part points outward (as here); above it, inward",
            color=GREY, fontsize=9.5, ha="center")
    fig.tight_layout()
    fig.savefig("circular-motion-string-vertical.svg")
    plt.close(fig)


# ================================================================ tension / speed, two rows
def vertical_tension():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 10.5))
    th = np.linspace(0, 2 * np.pi, 721)
    deg = np.degrees(th)
    cases = [(3, RED), (4, AMBER), (5, GREEN), (6, BLUE)]
    for q, col in cases:
        v2 = q - 2 * (1 - np.cos(th))
        T = v2 + np.cos(th)
        valid = T >= 0
        first_bad = np.argmax(~valid) if (~valid).any() else len(th)
        ax1.plot(deg[:first_bad], T[:first_bad], color=col, lw=2.2, label=rf"$u^2 = {q}\,gr$")
        ax2.plot(deg[:first_bad], v2[:first_bad], color=col, lw=2.2)
        if first_bad < len(th):
            ax1.plot(deg[first_bad - 1], 0, "o", color=col, ms=6)
            ax2.plot(deg[first_bad - 1], v2[first_bad - 1], "o", color=col, ms=6)
    ax1.axhline(0, color=GREY, lw=0.8, ls="--")
    ax1.set_xlabel(r"angle $\theta$ from the bottom (degrees)")
    ax1.set_ylabel(r"tension $T / mg$")
    ax1.set_xticks([0, 90, 180, 270, 360]); ax1.set_xlim(0, 360); ax1.set_ylim(-0.6, 9.6)
    ax1.set_title("Tension round a vertical circle — slack where it hits zero", color=GREY)
    ax1.legend(frameon=False, loc="upper right", labelcolor=GREY)
    ax1.text(8, 9.0, r"$T = \frac{mu^2}{r} - 2mg + 3mg\cos\theta$", color=GREY, fontsize=12)
    ax1.text(8, 8.2, r"$T_{\rm bottom} - T_{\rm top} = 6mg$, whatever $u$", color=GREY, fontsize=11)
    ax1.annotate("slack at 109°", xy=(109.5, 0), xytext=(30, 1.1), color=RED, fontsize=10, arrowprops=dict(arrowstyle="->", color=RED, lw=1))
    ax1.annotate("slack at 132°", xy=(131.8, 0), xytext=(150, -0.48), color=AMBER, fontsize=10, arrowprops=dict(arrowstyle="->", color=AMBER, lw=1))
    ax1.annotate("just grazes zero at the top", xy=(180, 0), xytext=(245, 0.75), color=GREEN, fontsize=10, arrowprops=dict(arrowstyle="->", color=GREEN, lw=1))
    bth = np.linspace(np.pi / 2, 3 * np.pi / 2, 200)
    ax2.plot(np.degrees(bth), -np.cos(bth), color=GREY, lw=1.6, ls="--")
    ax2.fill_between(np.degrees(bth), 0, -np.cos(bth), color=GREY, alpha=0.12)
    ax2.text(180, 0.32, "slack zone\n(T would be < 0)", color=GREY, fontsize=9.5, ha="center", va="center")
    ax2.axhline(0, color=GREY, lw=0.8)
    ax2.set_xlabel(r"angle $\theta$ from the bottom (degrees)")
    ax2.set_ylabel(r"$v^2 / (gr)$")
    ax2.set_xticks([0, 90, 180, 270, 360]); ax2.set_xlim(0, 360); ax2.set_ylim(-0.2, 8.6)
    ax2.set_title("Speed round the circle — energy alone, until the string lets go", color=GREY)
    ax2.text(10, 8.1, r"$v^2 = u^2 - 2gr(1-\cos\theta)$", color=GREY, fontsize=12)
    ax2.text(10, 7.45, r"complete circle needs $v_{\rm top}^2 \geq gr$, i.e. $u^2 \geq 5gr$", color=GREEN, fontsize=10)
    ax2.text(10, 6.85, r"(rod or bead: only $v_{\rm top}^2 \geq 0$, i.e. $u^2 \geq 4gr$)", color=GREY, fontsize=10)
    ax2.text(10, 6.3, r"grey zone: $v^2 < -gr\cos\theta$, where $T$ would be negative", color=GREY, fontsize=10)
    fig.tight_layout()
    fig.savefig("circular-motion-vertical-tension.svg")
    plt.close(fig)


# ================================================================ question diagrams
def q_bowl():
    fig, ax = plt.subplots(figsize=(9, 6.8))
    blank(ax, (-3.6, 4.6), (-3.9, 1.8))
    O = np.array([0.0, 0.0]); a = 3.0
    ax.add_patch(Arc(O, 2 * a, 2 * a, theta1=180, theta2=360, color=GREY, lw=2))
    ax.plot([-a, a], [0, 0], color=GREY, lw=0.8, ls=":")
    ax.plot(*O, "+", color=GREY, ms=10); ax.text(0.12, 0.15, "O (centre of the shell)", color=GREY, fontsize=10)
    cth = 2 / 3; th = np.arccos(cth)
    P = O + a * np.array([np.sin(th), -np.cos(th)])
    ax.add_patch(Circle(P, 0.12, color=BLUE)); ax.text(P[0] + 0.22, P[1] - 0.22, "P", color=BLUE)
    ax.plot([O[0], O[0]], [O[1], -a - 0.2], color=GREY, lw=0.8, ls="--")
    ax.plot([O[0], P[0]], [O[1], P[1]], color=GREY, lw=1, ls=":")
    xr = a * np.sin(th)
    ax.plot([-xr, xr], [P[1], P[1]], color=AMBER, lw=1.6, ls="--")
    ax.text(-1.3, P[1] - 0.3, "plane of the horizontal circle", color=AMBER, fontsize=9.5, ha="center")
    dim(ax, [0, P[1] - 0.55], [xr, P[1] - 0.55], "$r = a\\sin\\theta$", [xr / 2, P[1] - 0.3])
    xh = 3.7
    ax.plot([P[0], xh + 0.1], [P[1], P[1]], color=GREY, lw=0.8, ls=":")
    ax.plot([0, xh + 0.1], [-a, -a], color=GREY, lw=0.8, ls=":")
    ax.plot([0.3, xh + 0.1], [0, 0], color=GREY, lw=0.8, ls=":")
    dim(ax, [xh, -a], [xh, P[1]], "$h = a/3$", [xh + 0.55, (P[1] - a) / 2])
    dim(ax, [xh, P[1]], [xh, 0], "$a - h = a\\cos\\theta$", [xh + 0.05, P[1] / 2 + 0.5], fs=9.5)
    rin = (O - P) / np.linalg.norm(O - P)
    arrow(ax, P, P + 1.7 * rin, BLUE, lw=2.4, label="$R$ (along the\nradius, toward O)", lpos=P + 0.85 * rin + [0.62, 0.3], fs=9.5)
    arrow(ax, P, P + [0, -1.15], RED, lw=2.4, label="$mg$", lpos=P + [0.32, -1.15])
    arrow(ax, P, P + [-1.7 * np.sin(th), 0], AMBER, lw=2.4, label="to the centre of the circle", lpos=[-1.25, P[1] + 0.3], fs=9.5)
    ax.add_patch(Arc(O, 1.5, 1.5, theta1=270, theta2=270 + np.degrees(th), color=AMBER, lw=1.5))
    ax.text(*(O + 1.0 * np.array([np.sin(th / 2), -np.cos(th / 2)])), r"$\theta$", color=AMBER, ha="center", va="center", fontsize=12)
    ax.text(0.4, 1.45, "9231 J26/33 Q1 — P on the smooth inner surface of a hemispherical shell, radius $a$, horizontal circle at height $h = a/3$:",
            color=GREY, fontsize=10, ha="center")
    ax.text(0.4, 0.95, r"$R\cos\theta = mg,\quad R\sin\theta = m(a\sin\theta)\omega^2$   so   $\omega^2 = \frac{g}{a\cos\theta} = \frac{3g}{2a}$   (since $\cos\theta = \frac{2}{3}$)",
            color=GREY, fontsize=10.5, ha="center")
    ax.text(0.4, -3.7, "the same picture with $\\tan\\theta_1 = \\frac{3}{4}$, $\\tan\\theta_2 = \\frac{4}{3}$ is N25/31 Q2:  $\\omega_1^2/\\omega_2^2 = \\cos\\theta_2/\\cos\\theta_1$",
            color=GREY, fontsize=9.5, ha="center")
    fig.tight_layout()
    fig.savefig("circular-motion-q-bowl.svg")
    plt.close(fig)


def q_disc():
    fig, ax = plt.subplots(figsize=(9, 6.8))
    blank(ax, (-3.6, 4.6), (-2.2, 3.6))
    O = np.array([0.0, 0.0])
    ax.plot([-2.8, 3.4], [0, 0], color=GREY, lw=2.2)
    ax.plot([0, 0], [0, -0.6], color=GREY, lw=1.2)
    ax.add_patch(Arc([0, -0.75], 0.7, 0.25, theta1=0, theta2=360, color=GREY, lw=1))
    arrow(ax, [-0.2, -0.95], [0.25, -0.95], GREY, lw=1, ms=8); ax.text(0.55, -0.95, r"$\omega$", color=GREY, va="center")
    ax.plot(*O, "o", color=GREY, ms=4); ax.text(-0.2, -0.3, "O", color=GREY, ha="center")
    sa, ca = 0.6, 0.8
    A = O + [0, 2.0]; P = O + [1.5, 0]
    ax.plot([O[0], A[0]], [O[1], A[1]], color=GREY, lw=0.8, ls="--")
    ax.add_patch(Circle(A, 0.07, color=GREY)); ax.text(A[0] - 0.3, A[1] + 0.1, "A", color=GREY)
    ax.plot([A[0], P[0]], [A[1], P[1]], color=TEAL, lw=2)
    ax.text(-1.9, 1.55, "elastic string\nnatural length 2 m\n$\\lambda$ = 32 N\nstretched to 2.5 m", color=TEAL, fontsize=9.5, ha="center")
    arrow(ax, [-1.0, 1.35], [0.45, 1.38], TEAL, lw=0.9, ms=8)
    ax.add_patch(Arc(A, 0.9, 0.9, theta1=270, theta2=270 + np.degrees(np.arcsin(sa)), color=GREY, lw=1))
    ax.text(A[0] + 0.2, A[1] - 0.65, r"$\alpha$", color=GREY)
    ax.add_patch(Circle(P, 0.12, color=BLUE)); ax.text(P[0] + 0.75, P[1] - 0.38, "P (1.6 kg)", color=BLUE, fontsize=10, ha="center")
    dim(ax, [0, -1.45], [1.5, -1.45], "1.5 m", [0.75, -1.75])
    tdir = (A - P) / np.linalg.norm(A - P)
    arrow(ax, P, P + 1.25 * tdir, BLUE, lw=2.4, label="$T$ = 8 N", lpos=P + 1.25 * tdir + [0.42, 0.18], fs=9.5)
    arrow(ax, P + [0.12, 0], P + [0.12, 1.35], BLUE, lw=2.4, label="$R$", lpos=P + [0.42, 1.35])
    arrow(ax, P + [0.12, 0], P + [0.12, -1.3], RED, lw=2.4, label="$mg$ = 16 N", lpos=P + [0.8, -1.2], fs=10)
    arrow(ax, P, P + [-1.1, 0], PURPLE, lw=2.4, label="$F = \\mu R$", lpos=P + [-0.55, -0.3], fs=10)
    ax.text(-1.7, -0.55, "friction acts INWARD here:\nP is on the point of slipping\noutward, so limiting friction\npoints toward O", color=PURPLE, fontsize=8.8, ha="center", va="top")
    arrow(ax, P + [0.02, 0.55], P + [-1.9, 0.55], AMBER, lw=2.2, label="to centre", lpos=P + [-2.5, 0.55], fs=9.5)
    ax.text(0.6, 3.3, "9231 J25/31 — rough disc spinning at $\\omega$, P held by an elastic string from A (2 m above O), $\\mu = 0.5$, $g = 10$:",
            color=GREY, fontsize=9.8, ha="center")
    ax.text(0.6, 2.85, r"vertical: $R + T\cos\alpha = mg$;   toward O: $T\sin\alpha + F = m(1.5)\omega^2$;   $\sin\alpha = 0.6$ from $T = \lambda x/l$",
            color=GREY, fontsize=10, ha="center")
    fig.tight_layout()
    fig.savefig("circular-motion-q-disc.svg")
    plt.close(fig)


def q_sphere_outer():
    fig, ax = plt.subplots(figsize=(9, 6.6))
    blank(ax, (-3.6, 4.6), (-3.2, 3.9))
    O = np.array([0.0, 0.0]); a = 2.6
    ax.add_patch(Circle(O, a, fill=False, color=GREY, lw=2))
    ax.plot(*O, "+", color=GREY, ms=10); ax.text(0.12, -0.3, "O", color=GREY)
    ax.plot([0, 0], [0, a + 0.4], color=GREY, lw=0.8, ls="--")
    al, be = np.radians(25), np.radians(58)
    A = O + a * np.array([np.sin(al), np.cos(al)])
    B = O + a * np.array([np.sin(be), np.cos(be)])
    for X, lab, d in ((A, "A", [0.22, 0.12]), (B, "B", [0.28, 0.05])):
        ax.plot([O[0], X[0]], [O[1], X[1]], color=GREY, lw=1, ls=":")
        ax.add_patch(Circle(X, 0.11, color=BLUE)); ax.text(X[0] + d[0], X[1] + d[1], lab, color=BLUE)
    ax.add_patch(Arc(O, 1.4, 1.4, theta1=90 - np.degrees(al), theta2=90, color=AMBER, lw=1.5))
    ax.text(*(O + 0.95 * np.array([np.sin(al / 2), np.cos(al / 2)])), r"$\alpha$", color=AMBER, ha="center", va="center", fontsize=12)
    ax.add_patch(Arc(O, 2.2, 2.2, theta1=90 - np.degrees(be), theta2=90, color=GREEN, lw=1.5))
    ax.text(*(O + 1.38 * np.array([np.sin(be * 0.78), np.cos(be * 0.78)])), r"$\beta$", color=GREEN, ha="center", va="center", fontsize=12)
    tA = np.array([np.cos(al), -np.sin(al)]); tB = np.array([np.cos(be), -np.sin(be)])
    arrow(ax, A, A + 1.1 * tA, GREEN, lw=2.4, label="$u$", lpos=A + 1.1 * tA + [0.25, 0.12], fs=12)
    arrow(ax, B, B + 1.5 * tB, GREEN, lw=2.4, label="$v = \\frac{3}{2}u$", lpos=B + 1.5 * tB + [0.55, 0.1], fs=11)
    rout = (B - O) / a
    arrow(ax, B, B + 0.9 * rout, BLUE, lw=1.8, ls="--", label="$N = 0$ at B", lpos=B + 0.9 * rout + [0.6, 0.2], fs=10)
    arrow(ax, B, B + [0, -1.4], RED, lw=2.4, label="$mg$", lpos=B + [0.3, -1.4], fs=12)
    arrow(ax, B, B - 1.4 * np.cos(be) * rout, RED, lw=1.4, ls="--", label="$mg\\cos\\beta$, toward O", lpos=B - 1.4 * np.cos(be) * rout + [0.85, -0.55], fs=9.5)
    ax.add_patch(Arc(O, 2 * a + 0.16, 2 * a + 0.16, theta1=90 - np.degrees(be), theta2=90 - np.degrees(al), color=BLUE, lw=2))
    ax.text(0.5, 3.6, "9231 J26/33 — projected from A on the OUTSIDE of a smooth sphere, perpendicular to OA, downward; it leaves the surface at B", color=GREY, fontsize=9.8, ha="center")
    ax.text(0.5, 3.2, "energy A to B: $v^2 = u^2 + 2ga(\\cos\\alpha - \\cos\\beta)$;   leaving means $N = 0$:  $mg\\cos\\beta = mv^2/a$", color=GREY, fontsize=10, ha="center")
    ax.text(0.5, -3.0, "special case — released from rest at the very top ($\\alpha = 0$, $u = 0$): it leaves where $\\cos\\beta = \\frac{2}{3}$", color=GREY, fontsize=9.8, ha="center")
    fig.tight_layout()
    fig.savefig("circular-motion-q-sphere-outer.svg")
    plt.close(fig)


def q_sphere_inner():
    fig, ax = plt.subplots(figsize=(9, 7.6))
    blank(ax, (-3.7, 4.3), (-2.3, 5.0))
    O = np.array([0.0, 0.0]); a = 1.6; k = 0.2
    th = np.arccos(k)
    ax.add_patch(Arc(O, 2 * a, 2 * a, theta1=90 + np.degrees(th), theta2=450 - np.degrees(th), color=GREY, lw=2))
    ax.add_patch(Arc(O, 2 * a, 2 * a, theta1=90 - np.degrees(th), theta2=90 + np.degrees(th), color=GREY, lw=1, ls=":"))
    ax.plot(*O, "+", color=GREY, ms=10); ax.text(0.12, -0.32, "O", color=GREY)
    A = O + [-a, 0]
    B = O + a * np.array([np.sin(th), np.cos(th)]); Cc = O + a * np.array([-np.sin(th), np.cos(th)])
    ax.plot([A[0], O[0]], [A[1], O[1]], color=GREY, lw=0.8, ls=":")
    ax.plot([B[0], Cc[0]], [B[1], Cc[1]], color=GREY, lw=1.8)
    ax.text(Cc[0] - 0.3, Cc[1] + 1.05, "horizontal cut through B and C,\n$ka$ above O (the cap above it is removed)", color=GREY, fontsize=9, ha="right")
    for X, lab, d in ((A, "A", [-0.38, -0.05]), (B, "B", [0.25, -0.25]), (Cc, "C", [-0.3, 0.22])):
        ax.add_patch(Circle(X, 0.1, color=BLUE)); ax.text(X[0] + d[0], X[1] + d[1], lab, color=BLUE)
    ax.plot([0, 0], [0, a + 0.3], color=GREY, lw=0.8, ls="--")
    ax.plot([O[0], B[0]], [O[1], B[1]], color=GREY, lw=1, ls=":")
    ax.add_patch(Arc(O, 1.2, 1.2, theta1=90 - np.degrees(th), theta2=90, color=AMBER, lw=1.5))
    ax.text(*(O + 0.85 * np.array([np.sin(th / 2), np.cos(th / 2)])), r"$\theta$", color=AMBER, ha="center", va="center", fontsize=12)
    ax.text(0.95, 0.72, "$\\cos\\theta = k$", color=AMBER, fontsize=10)
    xh = 3.0
    ax.plot([B[0], xh + 0.1], [B[1], B[1]], color=GREY, lw=0.8, ls=":"); ax.plot([0.3, xh + 0.1], [0, 0], color=GREY, lw=0.8, ls=":")
    dim(ax, [xh, 0], [xh, B[1]], "$ka$", [xh + 0.3, B[1] / 2], fs=11)
    arrow(ax, A, A + [0, -1.1], GREEN, lw=2.4, label="$u$, vertically down", lpos=A + [0.0, -1.42], fs=10)
    ax.add_patch(Arc(O, 2 * a - 0.16, 2 * a - 0.16, theta1=180, theta2=450 - np.degrees(th), color=BLUE, lw=2))
    rin = (O - B) / a
    arrow(ax, B, B + 0.95 * rin, BLUE, lw=2.4, label="$R_B$, toward O", lpos=B + 0.95 * rin + [0.5, -0.4], fs=10)
    arrow(ax, B, B + [0, -1.15], RED, lw=2.4, label="$mg$", lpos=B + [0.3, -1.15], fs=11)
    arrow(ax, B + [0.05, 0], B + [0.05, 0] + 1.15 * k * rin, RED, lw=1.6, ls="--")
    ax.text(B[0] + 0.35, B[1] - 0.65, "$mg\\cos\\theta$ — also toward O\n(small here: $\\cos\\theta = k = 0.2$)", color=RED, fontsize=9, ha="left")
    arrow(ax, A, A + [1.1, 0], BLUE, lw=2.4, label="$R_A$", lpos=A + [1.25, -0.25], fs=11)
    ax.text(A[0] + 1.1, A[1] - 0.55, "at A the weight has\nno radial component", color=GREY, fontsize=8, ha="center", va="top")
    # projectile from B to C, computed with g = 1 in figure units: v_B^2 = ga/k = 5ga, launched along the tangent at B
    tB = np.array([-np.cos(th), np.sin(th)])
    vB = np.sqrt(a / k)
    tf = 2 * vB * np.sin(th)
    tproj = np.linspace(0, tf, 120)
    px = B[0] + vB * tB[0] * tproj
    py = B[1] + vB * tB[1] * tproj - 0.5 * tproj ** 2
    ax.plot(px, py, color=GREEN, lw=1.5, ls="--")
    ax.text(0.0, py.max() + 0.22, "after B: a projectile, launched along the tangent, that just reaches C", color=GREEN, fontsize=9.5, ha="center")
    ax.text(0.3, 4.75, "9231 J25/31 Q7 — P projected vertically down from A on the INSIDE of a cut hollow sphere, radius $a$", color=GREY, fontsize=9.8, ha="center")
    ax.text(0.3, -1.85, "$R_A = mu^2/a$;   at B (above O):  $R_B + mg\\cos\\theta = mv_B^2/a$;   energy A to B:  $v_B^2 = u^2 - 2gka$", color=GREY, fontsize=10, ha="center")
    ax.text(0.3, -2.2, "'just reaches B' on the inside means $R_B = 0$, not $v_B = 0$ — the wall stops pushing before the particle stops", color=GREY, fontsize=9.5, ha="center")
    fig.tight_layout()
    fig.savefig("circular-motion-q-sphere-inner.svg")
    plt.close(fig)


if __name__ == "__main__":
    velocity_triangle()
    force_cast()
    string_vertical()
    vertical_tension()
    q_bowl()
    q_disc()
    q_sphere_outer()
    q_sphere_inner()
    print("ok")

"""Figure for the Bounding Sums with Integrals card.

Regenerate:  python3 bounding-sums-figures.py
Writes, beside this file:
  sum-integral-staircase.svg — two tall panels. Top: the real exam curve
      y = 2x + x^2 on [0,1] with n = 6 rectangles of width 1/n — left-endpoint
      staircase under the curve, right-endpoint staircase over it: the
      integral trapped. Bottom: the other direction — y = 1/x with unit-width
      rectangles riding above the curve, so the harmonic sum dominates
      ln(n+1): the sum trapped.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AX = "#888888"
BLUE = "#2563eb"
GREEN = "#059669"
RED = "#dc2626"
AMBER = "#f59e0b"

plt.rcParams.update({
    "text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX,
    "xtick.color": AX, "ytick.color": AX, "font.size": 13,
    "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault",
})

fig, (top, bot) = plt.subplots(2, 1, figsize=(8.6, 12.2))

# ---------- Top: 2x + x^2 with 1/n rectangles, both endpoints ----------
f = lambda x: 2*x + x**2
xs = np.linspace(0, 1, 200)
n = 6
w = 1/n
for r in range(n):
    xl = r*w
    top.bar(xl, f(xl), width=w, align="edge",
            color="#2563eb26", edgecolor=BLUE, linewidth=1.4)          # left: under
    top.bar(xl, f(xl+w), width=w, align="edge", fill=False,
            edgecolor=RED, linewidth=1.4, linestyle="--")               # right: over
top.plot(xs, f(xs), color=AX, lw=2.6, zorder=5)
top.set_xlim(0, 1.42); top.set_ylim(0, 3.4)
top.set_title("Squeeze the integral: left staircase ≤ ramp ≤ right staircase",
              fontsize=15, color=AX, pad=8)
top.text(1.03, 2.55, "$U_n$: right endpoints,\n$r = 1 \\ldots n$ (dashed):\nover the curve", color=RED, fontsize=13)
top.text(1.03, 1.45, "$L_n$: left endpoints,\n$r = 0 \\ldots n-1$ (filled):\nunder the curve", color=BLUE, fontsize=13)
top.text(1.03, 0.55, "$y = 2x + x^2$,\nwidth $\\frac{1}{n}$;\nlet $n$ grow: both\nstaircases close\nonto $\\frac{4}{3}$",
         color=AX, fontsize=13)
top.grid(alpha=0.12, color=AX)

# ---------- Bottom: 1/x with unit rectangles, sum dominates ln ----------
g = lambda x: 1/x
xs2 = np.linspace(1, 7, 300)
for r in range(1, 6):
    bot.bar(r, 1/r, width=1, align="edge",
            color="#05966926", edgecolor=GREEN, linewidth=1.4)
bot.plot(xs2, g(xs2), color=AX, lw=2.6, zorder=5)
bot.set_xlim(0.6, 8.6); bot.set_ylim(0, 1.18)
bot.set_title("Trap the sum: each rectangle of height 1/r rides above the curve",
              fontsize=15, color=AX, pad=8)
bot.text(6.6, 0.75, "$\\sum_{r=1}^{n} \\frac{1}{r} \\;\\geq\\; \\int_1^{n+1}\\frac{dx}{x} = \\ln(n+1)$",
         color=GREEN, fontsize=15)
bot.text(6.6, 0.52, "so the harmonic series\ngrows like $\\ln n$ —\nslowly, forever", color=AX, fontsize=13)
bot.text(1.42, 1.05, "$y = \\frac{1}{x}$ (decreasing:\nleft endpoints now sit OVER)", color=AX, fontsize=13)
bot.grid(alpha=0.12, color=AX)

fig.tight_layout(h_pad=2.2)
fig.savefig("sum-integral-staircase.svg", transparent=True, bbox_inches="tight",
            metadata={"Date": None})
print("wrote sum-integral-staircase.svg")

"""Figures for [[Privacy-Preserving Computation]].  Run: python3 privacy-computation-figures.py
Writes five SVGs beside this script: three-settings, shamir, federated, costs, zk-soundness.
Numbers come from privacy-preserving-computation-lab.py (imported), except one bar in the cost figure,
which is a published order of magnitude and is labelled as such."""
import contextlib
import importlib.util
import io
import os
import re
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("lab", os.path.join(HERE, "privacy-preserving-computation-lab.py"))
lab = importlib.util.module_from_spec(spec); spec.loader.exec_module(lab)
GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": GREY, "axes.labelcolor": GREY, "axes.edgecolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "font.size": 11, "svg.fonttype": "none", "font.family": "DejaVu Sans"})


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)
    s = open(path).read()
    s = re.sub(r'<svg([^>]*?) width="[^"]*" height="[^"]*"', r'<svg\1 width="100%"', s, count=1)
    open(path, "w").write(s)
    print("wrote", name)


def box(ax, x, y, w, h, text, colour, size=10):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.1",
                                fc=matplotlib.colors.to_rgba(colour, 0.15), ec=colour, lw=1.4))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, multialignment="center")


def arrow(ax, p, q, colour, text=None, dy=0.16, style="-|>"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=13, color=colour, lw=1.5))
    if text:
        ax.text((p[0] + q[0]) / 2, (p[1] + q[1]) / 2 + dy, text, ha="center", fontsize=9, color=colour)


def three_settings():
    fig, axes = plt.subplots(3, 1, figsize=(10, 10.2), gridspec_kw={"hspace": 0.12})
    titles = ("Ordinary analysis: the DATA moves, and whoever holds the server holds everything",
              "Federated learning: the MODEL moves; records stay where they were collected",
              "Secure multi-party computation: only random SHARES move; no machine ever holds a record")
    for ax, title in zip(axes, titles):
        ax.set_xlim(0, 10); ax.set_ylim(0, 3.2); ax.axis("off"); ax.text(0.1, 2.95, title, fontsize=11, color=GREY, weight="bold")
    ax = axes[0]
    for k, y in enumerate((2.2, 1.4, 0.6)):
        box(ax, 1.5, y, 2.2, 0.55, f"hospital {'ABC'[k]}: records", BLUE); arrow(ax, (2.65, y), (6.3, 1.4 + (y - 1.4) * 0.25), RED, "all records" if k == 0 else None)
    box(ax, 7.6, 1.4, 2.5, 1.0, "central server\nsees every record", RED)
    ax = axes[1]
    for k, y in enumerate((2.2, 1.4, 0.6)):
        box(ax, 1.5, y, 2.2, 0.55, f"hospital {'ABC'[k]}: trains locally", BLUE)
        arrow(ax, (6.3, 1.5 + (y - 1.4) * 0.25), (2.65, y + 0.08), PURPLE, "current model" if k == 0 else None)
        arrow(ax, (2.65, y - 0.08), (6.3, 1.3 + (y - 1.4) * 0.25), GREEN, "update only" if k == 2 else None, dy=-0.3)
    box(ax, 7.6, 1.4, 2.5, 1.0, "server averages\nthe updates", PURPLE)
    ax = axes[2]
    pos = {"A": (2.0, 2.1), "B": (8.0, 2.1), "C": (5.0, 0.55)}
    for name, (x, y) in pos.items():
        box(ax, x, y, 2.6, 0.6, f"hospital {name}: own number\n+ one share from each other", BLUE, 9.5)
    for a, b in (("A", "B"), ("B", "C"), ("C", "A")):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        ax.add_patch(FancyArrowPatch((x1 + (1.35 if x2 > x1 else -1.35 if x2 < x1 else 0), y1 - (0.0 if y1 == y2 else 0.32 * np.sign(y1 - y2))),
                                     (x2 + (-1.35 if x2 > x1 else 1.35 if x2 < x1 else 0), y2 + (0.0 if y1 == y2 else 0.32 * np.sign(y1 - y2))),
                                     arrowstyle="<|-|>", mutation_scale=12, color=TEAL, lw=1.4))
    ax.text(5.0, 2.3, "random shares", color=TEAL, fontsize=9.5, ha="center")
    ax.text(5.0, 1.45, "there is no server at all:\nthe answer appears only when the\npartial sums are put together", ha="center", fontsize=9.5)
    save(fig, "privacy-computation-three-settings.svg")


def shamir():
    fig, axes = plt.subplots(2, 1, figsize=(10, 8.6), gridspec_kw={"hspace": 0.3})
    secret = 7.0; f = lambda x: secret - 1.6 * x + 0.9 * x**2
    xs = np.linspace(-0.2, 3.4, 200); pts = [(1, f(1)), (2, f(2)), (3, f(3))]
    ax = axes[0]
    for guess, col in ((1, PURPLE), (4, TEAL), (7, GREEN), (10, AMBER), (13, RED)):
        A = np.array([[0, 0, 1], [1, 1, 1], [4, 2, 1]], float); c = np.linalg.solve(A, [guess, pts[0][1], pts[1][1]])
        ax.plot(xs, np.polyval(c, xs), color=col, lw=1.4); ax.plot(0, guess, "s", color=col, ms=7)
    ax.plot(*zip(*pts[:2]), "o", color=BLUE, ms=9)
    ax.set_title("Two shares of a threshold-3 scheme: a parabola through them can reach ANY secret", color=GREY, fontsize=12, loc="left")
    ax.text(0.08, 12.2, "candidate\nsecrets", fontsize=9.5)
    ax = axes[1]
    ax.plot(xs, f(xs), color=GREEN, lw=2); ax.plot(*zip(*pts), "o", color=BLUE, ms=9); ax.plot(0, secret, "s", color=GREEN, ms=9)
    ax.annotate("the secret: where the\nonly possible parabola\nmeets x = 0", (0, secret), xytext=(0.3, 10.5), fontsize=10, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.set_title("Three shares: exactly one parabola, so exactly one secret", color=GREY, fontsize=12, loc="left")
    for a in axes:
        a.set_xlim(-0.2, 3.4); a.set_ylim(-1, 14); a.set_xticks([0, 1, 2, 3]); a.set_xticklabels(["0\n(secret)", "share 1", "share 2", "share 3"]); a.axvline(0, color=GREY, lw=0.8, ls=":")
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    axes[1].text(3.38, -0.4, "drawn with ordinary numbers; the real scheme works modulo a prime, where the statement is exact", ha="right", fontsize=9)
    save(fig, "privacy-computation-shamir.svg")


def federated():
    with contextlib.redirect_stdout(io.StringIO()):
        alone, fed, central, x, rec = lab.federated()
    fig, axes = plt.subplots(2, 1, figsize=(10, 8.2), gridspec_kw={"hspace": 0.42})
    ax = axes[0]
    names = ["each clinic trains alone\n(30 patients)", "federated: ten clinics,\nno records shared", "all 300 records pooled\non one server"]
    vals = [100 * alone, 100 * fed, 100 * central]; cols = [RED, GREEN, BLUE]
    ax.barh(names, vals, color=[matplotlib.colors.to_rgba(c, 0.35) for c in cols], edgecolor=cols, lw=1.4, height=0.55); ax.invert_yaxis()
    for i, v in enumerate(vals):
        ax.text(v + 0.6, i, f"{v:.1f} %", va="center", fontsize=10.5)
    ax.set_xlim(50, 102); ax.set_xlabel("accuracy on unseen patients from all ten clinics / %")
    ax.set_title("Federation buys nearly everything pooling would", color=GREY, fontsize=12, loc="left")
    ax = axes[1]; k = 10; idx = np.arange(k)
    ax.bar(idx - 0.2, x[:k], width=0.38, color=matplotlib.colors.to_rgba(BLUE, 0.4), edgecolor=BLUE, label="the patient's real record (first ten features)")
    ax.bar(idx + 0.2, rec[:k], width=0.38, color=matplotlib.colors.to_rgba(RED, 0.4), edgecolor=RED, label="rebuilt by the server from one uploaded update")
    ax.axhline(0, color=GREY, lw=0.8); ax.set_xticks(idx); ax.set_xticklabels([f"f{i+1}" for i in idx])
    ax.set_title("but an update is not harmless: one gradient gives the record back exactly", color=GREY, fontsize=12, loc="left")
    ax.legend(frameon=False, labelcolor=GREY, fontsize=9.5, loc="lower right")
    for a in axes:
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    save(fig, "privacy-computation-federated.svg")


def costs():
    n = 200_000; vals = [lab.rnd.randrange(1000) for _ in range(n)]
    t0 = time.perf_counter(); s = 0
    for v in vals:
        s += v
    plain = (time.perf_counter() - t0) / n
    shares = [lab.rnd.randrange(lab.P) for _ in range(n)]
    t0 = time.perf_counter(); s = 0
    for v in shares:
        s = (s + v) % lab.P
    shared = (time.perf_counter() - t0) / n
    ph = lab.Paillier(512); cs = [ph.enc(1) for _ in range(300)]
    t0 = time.perf_counter(); acc = 1
    for c in cs:
        acc = ph.add(acc, c)
    pail = (time.perf_counter() - t0) / len(cs)
    t0 = time.perf_counter(); [ph.enc(1) for _ in range(100)]; enc = (time.perf_counter() - t0) / 100
    rows = [("add two numbers in the clear", plain, GREEN), ("add two secret shares (mod p)", shared, TEAL), ("add under Paillier (one 1022-bit modular product)", pail, AMBER),
            ("encrypt one number under Paillier", enc, AMBER), ("one multiplication under fully homomorphic\nencryption (published benchmarks, order of magnitude)", 1e-2, RED)]
    for name, t, _ in rows:
        print(f"  {name.replace(chr(10), ' '):90s} {t*1e9:14,.0f} ns   ({t/plain:12,.0f} x)")
    fig, ax = plt.subplots(figsize=(10, 5.0))
    names = [r[0] for r in rows][::-1]; ts = [r[1] * 1e9 for r in rows][::-1]; cols = [r[2] for r in rows][::-1]
    ax.barh(names, ts, color=[matplotlib.colors.to_rgba(c, 0.35) for c in cols], edgecolor=cols, lw=1.4, height=0.6)
    for i, t in enumerate(ts):
        ax.text(t * 1.3, i, f"{t/ (plain*1e9):,.0f} ×", va="center", fontsize=10)
    ax.set_xscale("log"); ax.set_xlim(5, 1e9); ax.set_xlabel("time per operation / nanoseconds (log scale), measured in plain Python on one core")
    ax.set_title("What hiding the inputs costs", color=GREY, fontsize=12, loc="left")
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    save(fig, "privacy-computation-costs.svg")


def zk():
    with contextlib.redirect_stdout(io.StringIO()):
        out = lab.zero_knowledge()
    fig, ax = plt.subplots(figsize=(10, 5.0))
    n = np.arange(1, 21); ax.plot(n, 0.5**n, color=GREY, lw=1.3, ls="--", label="(1/2) to the power of the number of rounds")
    ax.plot(list(out), list(out.values()), "o", color=RED, ms=8, label="measured: a prover who does NOT know the secret, 360 000 attempts")
    ax.set_yscale("log"); ax.set_xlabel("rounds of challenge and response"); ax.set_ylabel("probability the cheat is never caught")
    ax.set_xticks([1, 4, 8, 12, 16, 20]); ax.annotate("20 rounds: one in a million", (20, 0.5**20), xytext=(-150, 30), textcoords="offset points", fontsize=10,
                                                        arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.set_title("Each round halves a cheat's chances; an honest prover always passes", color=GREY, fontsize=12, loc="left")
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY, fontsize=9.5, loc="lower left")
    save(fig, "privacy-computation-zk-soundness.svg")


if __name__ == "__main__":
    three_settings(); shamir(); federated(); costs(); zk()

"""Figures for [[Affective Computing]].  Run: python3 affective-computing-figures.py
Writes six SVGs beside this script: chain, circumplex, voice-confusion, skin, smiles, misread.
Numbers come from affective-computing-lab.py (imported)."""
import contextlib
import importlib.util
import io
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("lab", os.path.join(HERE, "affective-computing-lab.py"))
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


def quiet(f, *a):
    with contextlib.redirect_stdout(io.StringIO()):
        return f(*a)


def chain():
    fig, ax = plt.subplots(figsize=(10, 5.6)); ax.set_xlim(0, 10); ax.set_ylim(0, 5.6); ax.axis("off")
    steps = [("what the person\nFEELS", PURPLE), ("what the body\nSHOWS", BLUE), ("what the sensor\nRECORDS", TEAL), ("what the model\nLABELS", AMBER), ("what someone\nDECIDES", RED)]
    xs = np.linspace(1.0, 9.0, 5)
    for x, (txt, col) in zip(xs, steps):
        ax.add_patch(FancyBboxPatch((x - 0.85, 3.5), 1.7, 1.1, boxstyle="round,pad=0.02,rounding_size=0.12", fc=matplotlib.colors.to_rgba(col, 0.15), ec=col, lw=1.5))
        ax.text(x, 4.05, txt, ha="center", va="center", fontsize=10, multialignment="center")
    leaks = ["people mask, fake\nand suppress; culture\nand context change\nthe display", "lighting, camera\nangle, microphone,\na moving wrist", "trained on whose\nfaces? labelled by\nwhom, with which\ntheory of emotion?", "a probability read\nas a fact; rare events\nmake most alarms\nfalse"]
    for k in range(4):
        x0, x1 = xs[k] + 0.87, xs[k + 1] - 0.87
        ax.add_patch(FancyArrowPatch((x0, 4.05), (x1, 4.05), arrowstyle="-|>", mutation_scale=13, color=GREY, lw=1.4))
        xm = (xs[k] + xs[k + 1]) / 2
        ax.plot([xm, xm], [3.95, 2.65], color=GREY, lw=0.8, ls=":")
        ax.text(xm, 2.55, leaks[k], ha="center", va="top", fontsize=9.5, multialignment="center", linespacing=1.35)
    ax.text(5, 5.2, "Every arrow is an inference, and every inference loses something", ha="center", fontsize=12, color=GREY, weight="bold")
    ax.text(5, 0.55, "The machine only ever has the third box. Everything to its left is a guess; everything to its right is a choice.", ha="center", fontsize=10.5)
    save(fig, "affective-computing-chain.svg")


def circumplex():
    fig, ax = plt.subplots(figsize=(10, 8.4)); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.3, 1.3); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Circle((0, 0), 1.0, fc="none", ec=GREY, lw=1, ls=":"))
    ax.annotate("", (1.22, 0), (-1.22, 0), arrowprops=dict(arrowstyle="<|-|>", color=GREY, lw=1.2)); ax.annotate("", (0, 1.18), (0, -1.18), arrowprops=dict(arrowstyle="<|-|>", color=GREY, lw=1.2))
    ax.text(1.24, 0.06, "pleasant", fontsize=11, ha="left"); ax.text(-1.24, 0.06, "unpleasant", fontsize=11, ha="right")
    ax.text(0, 1.22, "high arousal (activated)", fontsize=11, ha="center"); ax.text(0, -1.27, "low arousal (quiet)", fontsize=11, ha="center")
    words = {"excited": 50, "delighted": 25, "happy": 8, "content": -25, "relaxed": -48, "calm": -68, "sleepy": -90, "bored": -125, "sad": -155, "miserable": 170,
             "frustrated": 155, "angry": 125, "afraid": 105, "alarmed": 85, "astonished": 68}
    for w, deg in words.items():
        a = np.radians(deg); col = GREEN if np.cos(a) > 0.15 else RED if np.cos(a) < -0.15 else GREY
        ax.plot(0.86 * np.cos(a), 0.86 * np.sin(a), "o", color=col, ms=5); ax.text(1.0 * np.cos(a), 1.0 * np.sin(a), w, ha="left" if np.cos(a) > 0.1 else "right" if np.cos(a) < -0.1 else "center",
                                                                                    va="bottom" if np.sin(a) > 0.2 else "top" if np.sin(a) < -0.2 else "center", fontsize=10.5, color=col)
    ax.add_patch(FancyBboxPatch((0.07, 0.16), 0.5, 0.44, boxstyle="round,pad=0.02", fc=matplotlib.colors.to_rgba(TEAL, 0.10), ec=TEAL, lw=1.2, ls="--"))
    ax.text(0.32, 0.38, "skin, heart,\nvoice pitch: read\nthe vertical axis", ha="center", va="center", fontsize=9.5, color=TEAL)
    ax.add_patch(FancyBboxPatch((0.07, -0.58), 0.62, 0.42, boxstyle="round,pad=0.02", fc=matplotlib.colors.to_rgba(PURPLE, 0.10), ec=PURPLE, lw=1.2, ls="--"))
    ax.text(0.38, -0.37, "words, and (unreliably)\nfaces: read the\nhorizontal axis", ha="center", va="center", fontsize=9.5, color=PURPLE)
    save(fig, "affective-computing-circumplex.svg")


def voice_confusion():
    names, conf = quiet(lab.voices)
    fig, ax = plt.subplots(figsize=(10, 6.2))
    for i in range(4):
        for j in range(4):
            ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fc=matplotlib.colors.to_rgba(BLUE, 0.05 + 0.45 * conf[i, j] / conf.max()), ec=GREY, lw=0.6))
            ax.text(j, i, str(conf[i, j]), ha="center", va="center", fontsize=15, color=GREY, weight="bold")
    ax.set_ylim(3.5, -0.5)
    ax.set_xticks(range(4)); ax.set_xticklabels(names); ax.set_yticks(range(4)); ax.set_yticklabels(names)
    ax.set_xlabel("what the classifier heard"); ax.set_ylabel("what was 'spoken'")
    ax.set_title("Prosody separates excited from quiet perfectly, and rage from delight barely", color=GREY, fontsize=12, loc="left")
    ax.add_patch(plt.Rectangle((1.5, 1.5), 2, 2, fc="none", ec=RED, lw=2, ls="--")); ax.text(3.62, 2.5, "same pitch,\nsame loudness,\nsame pace", color=RED, fontsize=10, va="center")
    ax.set_xlim(-0.5, 4.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "affective-computing-voice-confusion.svg")


def skin():
    t, x, events, found = quiet(lab.skin)
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(t, x, color=TEAL, lw=1.8)
    for (t0, what), col in zip(events, (RED, GREEN, RED, GREEN)):
        ax.axvline(t0, color=col, lw=1, ls="--"); ax.text(t0 + 0.8, 5.42 if col == RED else 5.28, what, fontsize=9.5, color=col)
    for f in found:
        ax.plot(f, np.interp(f, t, x), "v", color=AMBER, ms=9)
    ax.plot([], [], "v", color=AMBER, label="response detected from the signal alone")
    ax.set_xlabel("time / s"); ax.set_ylabel("skin conductance / microsiemens"); ax.set_ylim(3.9, 5.55)
    ax.set_title("Four jolts, two of dread (red) and two of delight (green): the palm cannot tell them apart", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY, loc="lower right", fontsize=9.5)
    save(fig, "affective-computing-skin.svg")


def smiles():
    fig, ax = plt.subplots(figsize=(10, 5.4)); ax.set_xlim(-0.8, 20.6); ax.set_ylim(-2.2, 5.6); ax.axis("off"); ax.set_aspect("equal")
    # 100 people: 30 happy (21 smile), 70 not happy (21 smile)
    people = [("happy", True)] * 21 + [("happy", False)] * 9 + [("not", True)] * 21 + [("not", False)] * 49
    for k, (state, smiling) in enumerate(people):
        x, y = k % 20, 4 - k // 20
        col = GREEN if state == "happy" else GREY
        ax.add_patch(Circle((x, y), 0.33, fc=matplotlib.colors.to_rgba(col, 0.55 if state == "happy" else 0.25), ec=col, lw=1))
        if smiling:
            ax.add_patch(Circle((x, y), 0.45, fc="none", ec=AMBER, lw=2))
    ax.text(10, 5.35, "100 people. Green: actually happy (30). Amber ring: smiling, and correctly spotted by a 99 %-accurate smile detector (42).", ha="center", fontsize=10.5)
    ax.text(10, -1.1, "Of the 42 it flags as 'happy', 21 are. The camera made no mistake: half of all smiles are not joy.", ha="center", fontsize=11, color=RED)
    ax.text(10, -1.85, "(illustrative rates: people smile 70 % of the time when happy, 30 % of the time when not)", ha="center", fontsize=9.5)
    save(fig, "affective-computing-smiles.svg")


def misread():
    out = quiet(lab.who_gets_misread)
    fig, ax = plt.subplots(figsize=(10, 5.2))
    xs = np.linspace(-1.5, 2.6, 400); g = lambda m: np.exp(-0.5 * ((xs - m) / 0.35) ** 2)
    thr = 0.72
    for m, col, lab_ in ((0.0, BLUE, "group A, calm faces (the training data)"), (0.4, PURPLE, "group B, calm faces: the brow simply rests lower")):
        ax.plot(xs, g(m), color=col, lw=2, label=lab_); ax.fill_between(xs, g(m), where=xs > thr, color=matplotlib.colors.to_rgba(col, 0.35))
    ax.plot(xs, g(1.0) * 0.5, color=RED, lw=1.5, ls="--", label="genuinely angry faces in group A")
    ax.axvline(thr, color=GREY, lw=1.2); ax.text(thr + 0.04, 1.02, "the learned boundary:\nright of it = 'angry'", fontsize=10)
    (a_acc, a_fp), (b_acc, b_fp) = out.values()
    ax.text(1.55, 0.62, f"calm faces called angry:\ngroup A {100*a_fp:.1f} %\ngroup B {100*b_fp:.1f} %", fontsize=11, color=RED)
    ax.set_xlabel("how far the brow is lowered (arbitrary units)"); ax.set_yticks([]); ax.set_ylim(0, 1.18)
    ax.set_title("One threshold, two resting faces", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY, loc="upper left", fontsize=9.5)
    save(fig, "affective-computing-misread.svg")


if __name__ == "__main__":
    chain(); circumplex(); voice_confusion(); skin(); smiles(); misread()

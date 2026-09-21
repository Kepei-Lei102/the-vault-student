"""Figures for [[Data Protection and Privacy]].  python3 data-protection-privacy-figures.py
Numbers are the printed output of data-protection-privacy-lab.py (seed 2026).
Every SVG: text #888, width=100%, no background, checked in light and dark."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": GREY, "axes.labelcolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "axes.edgecolor": GREY, "svg.fonttype": "none", "font.size": 9.5})


def style(ax):
    ax.set_facecolor("none")
    for sp in ax.spines.values():
        sp.set_color(GREY)


def save(fig, name):
    fig.patch.set_alpha(0)
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    txt = open(name).read()
    txt = txt.replace('width="', 'data-w="', 1).replace('height="', 'data-h="', 1)
    txt = txt.replace("<svg ", '<svg width="100%" ', 1)
    open(name, "w").write(txt)


def box(ax, xy, w, h, text, col, fs=8.8):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc=col + "26", ec=col, lw=1.5))
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=fs, color=GREY, linespacing=1.35)


def arrow(ax, a, b, col=GREY, text=None, off=(0, 0.16), rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12, color=col, lw=1.3, connectionstyle=f"arc3,rad={rad}"))
    if text:
        ax.text((a[0] + b[0]) / 2 + off[0], (a[1] + b[1]) / 2 + off[1], text, ha="center", va="center", fontsize=8, color=col)


# 1. the life of a piece of personal data, two rows of three, a principle on each stage
fig, ax = plt.subplots(figsize=(11, 5.6)); style(ax); ax.set_xlim(0, 11); ax.set_ylim(0, 5.6); ax.axis("off")
stages = [("COLLECT", "a lawful basis, stated openly;\nonly what the purpose needs\n(minimisation)", BLUE),
          ("STORE", "kept accurate, kept secure:\naccess levels, encryption,\nbreach notification", PURPLE),
          ("USE", "only for the purpose given\n(purpose limitation);\nno surprise second uses", GREEN),
          ("SHARE", "a processor acts only on the\ncontroller's written instructions;\nthe controller stays liable", TEAL),
          ("SEND ABROAD", "only to where protection\ntravels with it: adequacy,\ncontract, or assessment", AMBER),
          ("DELETE", "when the purpose is spent\n(storage limitation), or when\nthe person asks (erasure)", RED)]
for i, (t, sub, c) in enumerate(stages):
    r, k = divmod(i, 3)
    x, y = 0.3 + k * 3.6, 3.15 - r * 2.35
    box(ax, (x, y), 3.2, 1.75, f"{t}\n{sub}", c)
    if k: arrow(ax, (x - 0.4, y + 0.87), (x, y + 0.87))
ax.add_patch(FancyArrowPatch((9.1, 3.15), (1.9, 2.55), arrowstyle="-|>", mutation_scale=12, color=GREY, lw=1.3))
ax.text(5.5, 5.3, "The life of one piece of personal data, and the principle that binds each stage", ha="center", fontsize=10.5, color=GREY)
ax.text(5.5, 0.3, "at every stage the person keeps their rights: to be told, to see a copy, to correct, to erase, to object, to take the data elsewhere", ha="center", fontsize=8.6, color=GREY, style="italic")
save(fig, "data-protection-lifecycle.svg")

# 2. who is who
fig, ax = plt.subplots(figsize=(11.5, 5.0)); style(ax); ax.set_xlim(0, 11.5); ax.set_ylim(0, 5.0); ax.axis("off")
box(ax, (0.2, 1.7), 2.3, 1.5, "DATA SUBJECT\nthe person the data\nis about: you", BLUE, 9)
box(ax, (4.5, 1.7), 2.5, 1.5, "CONTROLLER\ndecides why and how:\nthe school, the app,\nthe bank", PURPLE, 9)
box(ax, (9.0, 1.7), 2.3, 1.5, "PROCESSOR\nhandles it for them:\nthe cloud host,\nthe payroll firm", TEAL, 9)
box(ax, (4.5, 3.95), 2.5, 0.85, "REGULATOR\ninvestigates, orders, fines", RED, 9)
arrow(ax, (2.5, 2.75), (4.5, 2.75), BLUE, "personal data,\nunder a lawful basis", off=(0, 0.33))
arrow(ax, (4.5, 2.1), (2.5, 2.1), PURPLE, "notice, a copy,\ncorrection, erasure", off=(0, -0.35))
arrow(ax, (7.0, 2.75), (9.0, 2.75), PURPLE, "written\ninstructions", off=(0, 0.33))
arrow(ax, (9.0, 2.1), (7.0, 2.1), TEAL, "reports\nbreaches", off=(0, -0.35))
arrow(ax, (5.75, 3.95), (5.75, 3.2), RED)
arrow(ax, (1.35, 3.2), (4.5, 4.35), BLUE, "complains", off=(-0.5, 0.25))
ax.text(5.75, 0.75, "GDPR says controller and processor; China's PIPL says personal information handler (who decides) and entrusted party.\nThe test is the same in both: who decides the purpose? That party answers for everything downstream.", ha="center", fontsize=8.8, color=GREY)
save(fig, "data-protection-roles.svg")

# 3. uniqueness and k-anonymity: two rows
fig, axes = plt.subplots(2, 1, figsize=(9.5, 7.4))
ax = axes[0]; style(ax)
names = ["sex", "district", "district\n+ sex", "birth year\n+ sex", "district +\nbirth year + sex", "birth date\n+ sex", "district +\nbirth date", "district +\nbirth date + sex"]
vals = [0, 0, 0, 0, 0, 4.79, 81.69, 89.99]
ax.bar(names, vals, color=[GREEN] * 5 + [AMBER, RED, RED], alpha=0.75)
for i, v in enumerate(vals): ax.text(i, v + 2, f"{v:.0f} %" if v else "0", ha="center", fontsize=8.5, color=GREY)
ax.set_ylim(0, 105); ax.set_ylabel("people who are the only one\nwith this combination / %"); ax.tick_params(axis="x", labelsize=7.8)
ax.set_title("No field is identifying; three together are. A synthetic city of 200 000.", fontsize=10)
ax = axes[1]; style(ax)
lv = ["exact date,\ndistrict", "birth year,\ndistrict", "birth year,\nregion", "birth decade,\nregion", "birth decade,\nwhole city"]
k = [1, 1, 75, 984, 10925]
ax.bar(lv, k, color=[RED, RED, GREEN, GREEN, GREEN], alpha=0.75); ax.set_yscale("log"); ax.set_ylim(0.6, 60000)
for i, v in enumerate(k): ax.text(i, v * 1.35, f"k = {v:,}", ha="center", fontsize=8.5, color=GREY)
ax.set_ylabel("smallest group anyone\nhides in (k), log scale"); ax.tick_params(axis="x", labelsize=8)
ax.set_title("k-anonymity: blur the fields until everyone hides in a crowd of k — and the data says less each step", fontsize=10)
fig.tight_layout(); save(fig, "data-protection-uniqueness.svg")

# 4. differential privacy: the dial, in two rows
eps = ["0.1", "0.5", "1.0", "5.0"]; attack = [920417, 173854, 90458, 18388]; analyst = [1.07, 0.21, 0.11, 0.02]
fig, axes = plt.subplots(2, 1, figsize=(8.6, 6.6))
ax = axes[0]; style(ax)
ax.bar(eps, attack, color=RED, alpha=0.75); ax.set_yscale("log"); ax.set_ylim(1000, 4e6)
for i, v in enumerate(attack): ax.text(i, v * 1.25, f"±{v:,.0f}", ha="center", fontsize=8.5, color=GREY)
ax.axhline(3500, color=GREY, lw=1, ls=":"); ax.text(3.45, 4100, "Alice's actual salary: 3 500", ha="right", fontsize=8.3, color=GREY)
ax.set_ylabel("attacker's error on\none salary / yuan")
ax.set_title("The differencing attack against noisy answers: the error dwarfs the secret", fontsize=10)
ax = axes[1]; style(ax)
ax.bar(eps, analyst, color=GREEN, alpha=0.75); ax.set_ylim(0, 1.3)
for i, v in enumerate(analyst): ax.text(i, v + 0.04, f"{v} %", ha="center", fontsize=8.5, color=GREY)
ax.set_ylabel("honest analyst's error on\nthe total payroll / %"); ax.set_xlabel("privacy budget ε  (smaller = more private, noisier)")
ax.set_title("The same noise, seen by someone asking about all 5 000 staff", fontsize=10)
fig.tight_layout(); save(fig, "data-protection-dp.svg")
print("four SVGs written")

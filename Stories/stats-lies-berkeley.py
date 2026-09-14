"""
stats-lies-berkeley.py — Simpson's paradox on the Berkeley 1973 admissions data.

Companion to [[Stats Lies Hall of Fame]].

The six largest departments from Bickel, Hammel & O'Connell, *Science* 187
(1975) 398–404 (the `UCBAdmissions` table): applicants and admits by sex.
Aggregated, men are admitted at a clearly higher rate; department by
department, the gap vanishes or reverses.  The script recomputes both, then
runs the counterfactual — what the women's overall rate WOULD be if they
had applied to departments in the men's proportions — which is where the
paradox is resolved.  Draws stats-lies-berkeley-simpson.svg.
Run:  python3 stats-lies-berkeley.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# dept: (men applicants, men admitted, women applicants, women admitted)
DEPTS = {
    "A": (825, 512, 108, 89),
    "B": (560, 353, 25, 17),
    "C": (325, 120, 593, 202),
    "D": (417, 138, 375, 131),
    "E": (191, 53, 393, 94),
    "F": (373, 22, 341, 24),
}
GREY = "#888"


def main():
    ma = sum(v[0] for v in DEPTS.values()); mm = sum(v[1] for v in DEPTS.values())
    wa = sum(v[2] for v in DEPTS.values()); wm = sum(v[3] for v in DEPTS.values())
    print(f"aggregate: men {mm}/{ma} = {mm/ma:.1%} admitted, women {wm}/{wa} = {wm/wa:.1%} — a {mm/ma-wm/wa:.1%} gap")
    print(f"{'dept':>4} {'men':>7} {'women':>7} {'gap':>8}   who applied here")
    favour_women = 0
    for d, (m_app, m_adm, w_app, w_adm) in DEPTS.items():
        gap = w_adm / w_app - m_adm / m_app
        favour_women += gap > 0
        share_w = w_app / (m_app + w_app)
        print(f"{d:>4} {m_adm/m_app:>7.1%} {w_adm/w_app:>7.1%} {gap:>+8.1%}   {share_w:.0%} of applicants were women; dept admits {(m_adm+w_adm)/(m_app+w_app):.0%}")
    print(f"women's rate is higher in {favour_women} of 6 departments")

    # counterfactual: women's admission rates, weighted by the MEN's department choices
    cf = sum((v[3] / v[2]) * v[0] for v in DEPTS.values()) / ma
    print(f"if women had applied in the men's proportions, their overall rate would be {cf:.1%} (men: {mm/ma:.1%})")
    # and the reverse
    cf2 = sum((v[1] / v[0]) * v[2] for v in DEPTS.values()) / wa
    print(f"if men had applied in the women's proportions, theirs would be {cf2:.1%} (women: {wm/wa:.1%})")

    # figure: department admit rate vs share of women applicants, bubble = applicants
    fig, ax = plt.subplots(figsize=(7.4, 4.4), dpi=100)
    fig.patch.set_alpha(0); ax.set_facecolor("none")
    for d, (m_app, m_adm, w_app, w_adm) in DEPTS.items():
        x = w_app / (m_app + w_app) * 100
        ax.scatter(x, m_adm / m_app * 100, s=(m_app) / 2.2, color="#2563eb", alpha=0.35, edgecolor="#2563eb")
        ax.scatter(x, w_adm / w_app * 100, s=(w_app) / 2.2, color="#dc2626", alpha=0.35, edgecolor="#dc2626")
        ax.plot([x, x], [m_adm / m_app * 100, w_adm / w_app * 100], color=GREY, lw=0.8, alpha=0.6)
        ax.annotate(d, (x, max(m_adm / m_app, w_adm / w_app) * 100 + 4), ha="center", color=GREY, fontsize=10)
    ax.axhline(mm / ma * 100, color="#2563eb", ls="--", lw=1)
    ax.axhline(wm / wa * 100, color="#dc2626", ls="--", lw=1)
    ax.text(97, mm / ma * 100 + 1.2, f"all men {mm/ma:.0%}", color="#2563eb", ha="right", fontsize=9)
    ax.text(97, wm / wa * 100 - 3.4, f"all women {wm/wa:.0%}", color="#dc2626", ha="right", fontsize=9)
    ax.set_xlabel("share of the department's applicants who were women (%)", color=GREY)
    ax.set_ylabel("admission rate (%)", color=GREY)
    ax.set_title("Berkeley 1973: blue = men, red = women; bubble size = applicants", color=GREY, fontsize=10)
    ax.set_xlim(0, 100); ax.set_ylim(0, 95)
    for sp in ax.spines.values():
        sp.set_color(GREY)
    ax.tick_params(colors=GREY)
    ax.grid(True, color=GREY, alpha=0.2)
    fig.tight_layout()
    fig.savefig("stats-lies-berkeley-simpson.svg", format="svg", transparent=True)
    print("wrote stats-lies-berkeley-simpson.svg")


if __name__ == "__main__":
    main()

"""Timeline for Emmy Noether.md — run: python3 noether-timeline.py (writes noether-timeline.svg beside the card)."""
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TXT = "#888"; BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": TXT, "font.size": 10, "svg.fonttype": "none"})
events = [
    (1882, "born in Erlangen", TXT, 1),
    (1900, "qualifies to teach French and English", TXT, -1),
    (1904, "allowed to matriculate at last", BLUE, 1),
    (1907, "doctorate, summa cum laude, 331 invariants", BLUE, -1),
    (1915, "Göttingen; Hilbert: “not a bathhouse”", PURPLE, 1),
    (1918, "Invariante Variationsprobleme, read by Klein", AMBER, -1),
    (1919, "habilitation, four years late", PURPLE, 1),
    (1921, "Idealtheorie in Ringbereichen", GREEN, -1),
    (1923, "first pay: a teaching contract", GREEN, 1),
    (1932, "plenary at the Zürich Congress; Ackermann–Teubner prize", GREEN, -1),
    (1933, "dismissed; the seminar moves to her flat", RED, 1),
    (1934, "Bryn Mawr and Princeton", TEAL, -1),
    (1935, "dies at 53", RED, 1),
]
fig, ax = plt.subplots(figsize=(11, 3.6)); ax.set_xlim(1878, 1939); ax.set_ylim(-2.6, 2.6); ax.axis("off")
ax.plot([1880, 1937], [0, 0], color=TXT, lw=1.2)
for y in range(1880, 1940, 10): ax.plot([y, y], [-0.12, 0.12], color=TXT, lw=1); ax.text(y, -0.45, str(y), ha="center", fontsize=9, color=TXT)
ax.axvspan(1914, 1918, color=TXT, alpha=0.08); ax.text(1916, -2.5, "1914–18 war", ha="center", fontsize=8, color=TXT)
ax.axvspan(1933, 1935.3, color=RED, alpha=0.08)
for i, (y, label, col, side) in enumerate(events):
    h = side * (1.0 + 0.55 * (i % 3))
    ax.plot([y, y], [0, h], color=col, lw=1); ax.plot(y, 0, "o", color=col, ms=5)
    ax.text(y, h + 0.12 * side, f"{y}  {label}", ha="center", va="bottom" if side > 0 else "top", fontsize=8.2, color=col)
fig.savefig("noether-timeline.svg", format="svg", transparent=True, bbox_inches="tight")
s = open("noether-timeline.svg").read(); m = re.search(r"<svg[^>]*>", s)
tag = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)).replace("<svg", '<svg width="100%"', 1)
open("noether-timeline.svg", "w").write(s[:m.start()] + tag + s[m.end():]); print("wrote noether-timeline.svg")

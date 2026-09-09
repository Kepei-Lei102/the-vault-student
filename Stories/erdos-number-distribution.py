"""How far the world's mathematicians sit from Erdős — the Erdős Number Project's count (Grossman, 2004 data).
Regenerate: python3 erdos-number-distribution.py"""
import matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"
counts = {0:1, 1:504, 2:6593, 3:33605, 4:83642, 5:87760, 6:40014, 7:11591, 8:3146, 9:819, 10:244, 11:68, 12:23, 13:5}
fig, ax = plt.subplots(figsize=(8.5, 4.8)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.bar(list(counts), list(counts.values()), color="#2563eb", alpha=0.85)
for k, v in counts.items(): ax.text(k, v * 1.25 if v > 3 else 4, f"{v:,}", ha="center", fontsize=8, color=GREY)
ax.set_yscale("log"); ax.set_ylim(0.7, 4e5); ax.set_xticks(list(counts))
ax.set_xlabel("Erdős number — length of the shortest coauthor path to Erdős", color=GREY); ax.set_ylabel("mathematicians (log scale)", color=GREY)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY)
ax.set_title("One man at distance 0, five hundred at distance 1, a quarter of a million within five", color=GREY, fontsize=10.5)
fig.tight_layout(); fig.savefig("erdos-number-distribution.svg", transparent=True); print("plot ok; median", sorted(k for k, v in counts.items() for _ in range(v))[sum(counts.values())//2])

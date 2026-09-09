"""The entropy ladder as a chart — the numbers come from compression-is-intelligence-entropy.py, run on 1 MB of the
vault's own English (2026-09-09), plus the two reference points.  Regenerate: python3 compression-is-intelligence-ladder.py"""
import matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"
rows=[("no model — 8 bits per ASCII char",8.0,"#888888"),("order-0: letter frequencies",4.64,"#2563eb"),("order-1: knows 1 previous char",3.69,"#2563eb"),("order-2: knows 2",2.89,"#2563eb"),("order-3: knows 3",2.14,"#2563eb"),("order-4: knows 4 (over-fitted on 1 MB)",1.63,"#2563eb"),
      ("gzip -9",2.90,"#0891b2"),("bzip2",2.32,"#0891b2"),("xz",2.43,"#0891b2"),("Shannon's human guessers, 1951",1.0,"#f59e0b"),("Chinchilla 70B on Wikipedia, 2023",0.66,"#7c3aed")]
fig,ax=plt.subplots(figsize=(8.8,5.2)); fig.patch.set_alpha(0); ax.set_facecolor("none")
y=list(range(len(rows)))[::-1]
ax.barh(y,[r[1] for r in rows],color=[r[2] for r in rows],alpha=0.85,height=0.62)
for yy,r in zip(y,rows): ax.text(r[1]+0.08,yy,f"{r[1]:.2f}",va="center",fontsize=8.5,color=GREY)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows],fontsize=8.5,color=GREY); ax.set_xlim(0,9.2)
ax.set_xlabel("bits needed per character of English",color=GREY)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY,labelsize=8)
fig.suptitle("The better the predictor, the fewer the bits: one text, costed by what the model knows",color=GREY,fontsize=10.5)
fig.tight_layout(rect=(0,0,1,0.96)); fig.savefig("compression-is-intelligence-ladder.svg",transparent=True); print("ok")

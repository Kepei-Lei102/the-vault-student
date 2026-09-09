"""Power delivered to a load R by a source (E, r): P = E²R/(R+r)², maximum at R = r,
where the efficiency R/(R+r) is only 50 %.  Regenerate: python3 internal-resistance-power-transfer.py"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"; E,r=12.0,2.0
R=np.linspace(0.05,12,400); P=E**2*R/(R+r)**2; eff=R/(R+r)
fig,ax=plt.subplots(figsize=(8,5)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.plot(R,P,color="#2563eb",lw=2.2,label="power in the load  P = ℰ²R/(R+r)²")
ax2=ax.twinx(); ax2.plot(R,100*eff,color="#059669",lw=1.8,ls="--",label="efficiency  R/(R+r)")
ax.axvline(r,color=GREY,lw=0.7,ls=":"); ax.plot([r],[E**2/(4*r)],"o",color="#dc2626")
ax.annotate("maximum power at R = r\n(18 W here — and half of it is wasted in the cell)",(r,E**2/(4*r)),xytext=(3.6,16.5),fontsize=9,color=GREY,arrowprops=dict(arrowstyle="->",color=GREY))
ax.set_xlim(0,12); ax.set_ylim(0,20); ax2.set_ylim(0,100)
ax.set_xlabel("load resistance R / Ω   (source: ℰ = 12 V, r = 2 Ω)",color=GREY); ax.set_ylabel("power delivered to load / W",color=GREY); ax2.set_ylabel("efficiency / %",color=GREY)
for a in (ax,ax2):
    for s in a.spines.values(): s.set_color(GREY)
    a.tick_params(colors=GREY)
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels()
leg=ax.legend(h1+h2,l1+l2,frameon=False,fontsize=9,loc="lower right")
for t in leg.get_texts(): t.set_color(GREY)
ax.set_title("Maximum power transfer: match the load to r — unless you care about efficiency",color=GREY,fontsize=11)
fig.tight_layout(); fig.savefig("internal-resistance-power-transfer.svg",transparent=True); print("ok")

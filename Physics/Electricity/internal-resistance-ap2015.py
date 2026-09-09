"""AP Physics C: E&M 2015 Q2 — linearising V = ER/(R+r) as 1/V = (r/E)(1/R) + 1/E.
Regenerate: python3 internal-resistance-ap2015.py"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"
R=np.array([0.5,1,2,3,5,10]); V=np.array([5.6,7.4,9.4,10.6,10.9,11.4])
x,y=1/R,1/V; m,b=np.polyfit(x,y,1)
fig,ax=plt.subplots(figsize=(7.5,4.8)); fig.patch.set_alpha(0); ax.set_facecolor("none")
xx=np.linspace(0,2.2,10); ax.plot(xx,m*xx+b,color="#2563eb",lw=1.8,label=f"best line: gradient r/ℰ = {m:.4f} Ω/V, intercept 1/ℰ = {b:.4f} V⁻¹")
ax.plot(x,y,"o",color="#dc2626",ms=6,label="the six trials")
ax.plot([0],[b],"s",color="#059669"); ax.annotate(f"1/ℰ → ℰ = {1/b:.1f} V",(0,b),xytext=(0.25,0.072),fontsize=9,color=GREY,arrowprops=dict(arrowstyle="->",color=GREY))
ax.text(1.35,0.105,f"r = gradient × ℰ = {m/b:.2f} Ω",fontsize=9,color=GREY)
ax.set_xlim(0,2.2); ax.set_ylim(0.06,0.20); ax.set_xlabel("1/R  (Ω⁻¹)",color=GREY); ax.set_ylabel("1/V  (V⁻¹)",color=GREY)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY); leg=ax.legend(frameon=False,fontsize=8.5,loc="upper left")
for t in leg.get_texts(): t.set_color(GREY)
ax.set_title("A curve made straight: 1/V against 1/R (AP Physics C: E&M 2015, Q2)",color=GREY,fontsize=10.5)
fig.tight_layout(); fig.savefig("internal-resistance-ap2015.svg",transparent=True); print(f"E={1/b:.2f} r={m/b:.3f}")

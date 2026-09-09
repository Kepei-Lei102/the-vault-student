"""Terminal p.d. against current for a real source: V = E - Ir.  The June 2021 Paper 23 battery
(E = 7.4 V, r = 8.0 Ω) and the (d)-part sketch — a battery with lower e.m.f. and lower r.
Regenerate: python3 internal-resistance-vi-line.py"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"; E,r=7.4,8.0; E2,r2=5.0,3.0
I=np.linspace(0,1.2,200)
fig,ax=plt.subplots(figsize=(8,5)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.plot(I,E-r*I,color="#2563eb",lw=2.2,label=f"battery: $\\mathcal{{E}}$ = {E} V, r = {r} Ω")
ax.plot(I,E2-r2*I,color="#059669",lw=1.8,ls="--",label=f"lower e.m.f., lower r: {E2} V, {r2} Ω")
ax.plot([0],[E],"o",color="#2563eb"); ax.annotate("intercept = e.m.f. (no current, no lost volts)",(0,E),xytext=(0.18,7.7),fontsize=9,color=GREY,arrowprops=dict(arrowstyle="->",color=GREY))
ax.plot([E/r],[0],"o",color="#dc2626"); ax.annotate("short-circuit current $\\mathcal{E}/r$ = 0.92 A",(E/r,0),xytext=(0.22,0.3),fontsize=9,color=GREY,arrowprops=dict(arrowstyle="->",color=GREY))
# gradient triangle
i0,i1=0.12,0.36; ax.plot([i0,i1,i1],[E-r*i0,E-r*i0,E-r*i1],color="#f59e0b",lw=1.2)
ax.text((i0+i1)/2,E-r*i0+0.15,"ΔI",ha="center",fontsize=9,color=GREY); ax.text(i1+0.02,E-r*(i0+i1)/2,"ΔV = −r ΔI\ngradient = −r = −8.0 Ω",fontsize=9,color=GREY,va="center")
# lost volts shading at I=0.5
ax.fill_between([0.5,0.5],[0,0],[0,0]); ax.annotate("",xy=(0.72,E-r*0.72),xytext=(0.72,E),arrowprops=dict(arrowstyle="<->",color="#dc2626")); ax.text(0.74,E-r*0.36,"lost volts $Ir$",color="#dc2626",fontsize=9)
ax.annotate("",xy=(0.72,0),xytext=(0.72,E-r*0.72),arrowprops=dict(arrowstyle="<->",color="#059669")); ax.text(0.74,(E-r*0.72)/2,"terminal p.d. $V$",color="#059669",fontsize=9)
ax.set_xlim(0,1.2); ax.set_ylim(0,8.5); ax.set_xlabel("current I / A",color=GREY); ax.set_ylabel("terminal p.d. V / V",color=GREY)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY); leg=ax.legend(frameon=False,fontsize=9,loc="upper right")
for t in leg.get_texts(): t.set_color(GREY)
ax.set_title("V = ℰ − I r: intercept is the e.m.f., gradient is −r",color=GREY,fontsize=11)
fig.tight_layout(); fig.savefig("internal-resistance-vi-line.svg",transparent=True); print("ok")

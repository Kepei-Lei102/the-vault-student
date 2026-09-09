"""Two figures for the potential-divider card.
sensor-curve: V_out across the fixed resistor as an NTC thermistor changes temperature, for three fixed resistors —
the choice of fixed resistor sets where the curve is steep.  loading: a 10 kΩ / 10 kΩ divider on 9 V promises 4.5 V,
and delivers it only while the load across the output is large.  Regenerate: python3 potential-dividers-loading.py"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"
def frame(ax):
    ax.set_facecolor("none"); ax.tick_params(colors=GREY,labelsize=8)
    for s in ax.spines.values(): s.set_color(GREY)
# --- sensor curve
fig,a1=plt.subplots(figsize=(7.5,4.4)); fig.patch.set_alpha(0); frame(a1)
T=np.linspace(-20,80,300); TK=T+273.15; Rth=1e4*np.exp(3950*(1/TK-1/298.15))
for Rf,col in [(1e3,"#7c3aed"),(1e4,"#2563eb"),(1e5,"#059669")]:
    a1.plot(T, 5*Rf/(Rf+Rth), color=col, lw=2, label=f"fixed resistor {Rf/1e3:g} kΩ")
a1.set_xlabel("thermistor temperature / °C",color=GREY); a1.set_ylabel("V_out across the fixed resistor / V",color=GREY)
a1.set_title("Sensor divider: 5 V, 10 kΩ NTC thermistor (B = 3950), three choices of fixed resistor",color=GREY,fontsize=10)
leg=a1.legend(frameon=False,fontsize=8,loc="lower right"); [t.set_color(GREY) for t in leg.get_texts()]
fig.text(0.5,0.02,"the curve is steepest — the sensor most sensitive — where the fixed resistor equals the thermistor's resistance:\n1 kΩ suits hot water, 10 kΩ room temperature, 100 kΩ a freezer",fontsize=8,color=GREY,ha="center")
fig.tight_layout(rect=(0,0.09,1,1)); fig.savefig("potential-dividers-sensor-curve.svg",transparent=True)
# --- loading
fig,a2=plt.subplots(figsize=(7.5,4.4)); fig.patch.set_alpha(0); frame(a2)
RL=np.logspace(2,7,300); R2p=1/(1/1e4+1/RL); V=9*R2p/(1e4+R2p)
a2.semilogx(RL,V,color="#dc2626",lw=2); a2.axhline(4.5,color=GREY,lw=0.8,ls="--")
a2.text(1.2e2,4.6,"the formula's promise: 4.5 V",color=GREY,fontsize=8)
for RL0,lab in [(1e7,"a 10 MΩ voltmeter"),(1e4,"a 10 kΩ load"),(1e3,"a 1 kΩ load")]:
    R2p0=1/(1/1e4+1/RL0); V0=9*R2p0/(1e4+R2p0); a2.plot(RL0,V0,"o",color="#dc2626",ms=6); a2.annotate(f"{lab}: {V0:.2f} V",(RL0,V0),xytext=(6,-14 if RL0<1e6 else 8),textcoords="offset points",fontsize=8,color=GREY)
a2.set_xlabel("resistance of the load connected across V_out / Ω (log scale)",color=GREY); a2.set_ylabel("V_out actually delivered / V",color=GREY); a2.set_ylim(0,5)
a2.set_title("Loading: a 10 kΩ / 10 kΩ divider on 9 V — what the tap delivers as the load across it shrinks",color=GREY,fontsize=10)
a2.text(1.5e5,1.2,"left: a heavy load in parallel with R₂ drags the\nlower arm's resistance down, and its share with it\nright: a load ≫ R₂ leaves the divider alone",fontsize=7.5,color=GREY)
fig.tight_layout(); fig.savefig("potential-dividers-loading.svg",transparent=True); print("two plots ok")

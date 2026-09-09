"""How big a number the public record has factored, by year — the RSA Factoring Challenge records —
against the key sizes in use.  Regenerate: python3 encryption-factoring-records.py"""
import matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"
recs=[(1991,330,"RSA-100"),(1994,426,"RSA-129 (the 1977 challenge)"),(1996,430,"RSA-130"),(1999,512,"RSA-155 — the first 512-bit"),(2003,576,"RSA-576"),(2005,640,"RSA-640"),(2009,768,"RSA-768"),(2019,795,"RSA-240"),(2020,829,"RSA-250")]
fig,ax=plt.subplots(figsize=(8.5,5)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.plot([r[0] for r in recs],[r[1] for r in recs],"o-",color="#2563eb",lw=1.8,ms=6,label="largest RSA challenge number factored (bits)")
for y,b,l in recs:
    if l.startswith(("RSA-129","RSA-155","RSA-768","RSA-250")): ax.annotate(l,(y,b),xytext=(6,-14 if b<700 else 8),textcoords="offset points",fontsize=8.5,color=GREY)
for b,lab,c in [(1024,"1024-bit keys — deprecated since 2013, still not publicly factored","#f59e0b"),(2048,"2048-bit keys — today's floor","#059669")]:
    ax.axhline(b,color=c,lw=1.2,ls="--"); ax.text(1991,b+25,lab,color=c,fontsize=9)
ax.set_xlim(1990,2026); ax.set_ylim(0,2300); ax.set_xlabel("year",color=GREY); ax.set_ylabel("size of the modulus / bits",color=GREY)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY); leg=ax.legend(frameon=False,fontsize=9,loc="lower right")
for t in leg.get_texts(): t.set_color(GREY)
ax.set_title("Thirty years of factoring records: about 500 bits of progress — and the keys moved faster",color=GREY,fontsize=10.5)
fig.tight_layout(); fig.savefig("encryption-factoring-records.svg",transparent=True); print("ok")

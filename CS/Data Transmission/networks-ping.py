"""Thirty-six round trips from a home connection in Chengdu to 8.8.8.8 (Google's public DNS), one every quarter
second, recorded 2026-09-09 with `ping -c 40 -i 0.25 8.8.8.8`.  Left: each round trip in order — the jitter is the
point.  Right: the same numbers as a histogram.  Regenerate: python3 networks-ping.py"""
import matplotlib, statistics as st
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"
r=[float(x) for x in open("networks-ping-samples.txt")]
fig,(a1,a2)=plt.subplots(1,2,figsize=(10,3.8),gridspec_kw={"width_ratios":[2,1]}); fig.patch.set_alpha(0)
for ax in (a1,a2):
    ax.set_facecolor("none"); ax.tick_params(colors=GREY,labelsize=8)
    for s in ax.spines.values(): s.set_color(GREY)
a1.plot(range(1,len(r)+1),r,"o-",color="#2563eb",ms=4,lw=1.2); a1.axhline(st.median(r),color="#f59e0b",lw=1,ls="--")
a1.text(1,st.median(r)+4,f"median {st.median(r):.0f} ms",color="#f59e0b",fontsize=8)
a1.set_xlabel("ping number (one every 0.25 s)",color=GREY); a1.set_ylabel("round-trip time / ms",color=GREY)
a1.set_title("Latency is not a number but a distribution",color=GREY,fontsize=10)
a2.hist(r,bins=12,color="#2563eb",alpha=0.8); a2.set_xlabel("round-trip time / ms",color=GREY); a2.set_ylabel("count",color=GREY)
a2.set_title(f"min {min(r):.0f} · max {max(r):.0f} · sd {st.pstdev(r):.0f} ms",color=GREY,fontsize=10)
fig.tight_layout(); fig.savefig("networks-ping.svg",transparent=True); print("ok")

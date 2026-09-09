"""Perception as a predictive codec: what a video coder — and, on the predictive-processing account, a brain — actually
transmits is the *difference* between what it predicted and what arrived.  Two synthetic frames of a scene with one
moving object; the third panel is frame 2 minus frame 1.  Regenerate: python3 compression-is-intelligence-frames.py"""
import numpy as np, matplotlib, zlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
GREY="#888888"
rng=np.random.default_rng(3)
H,W=90,160
yy,xx=np.mgrid[0:H,0:W]
def scene(cx):
    img=np.zeros((H,W))
    img+= 0.35+0.25*np.sin(yy/9.0)*np.cos(xx/13.0)                 # a static textured background
    img[60:,:]+=0.15                                                # a floor
    img+=0.03*rng.standard_normal((H,W))*0                          # (no sensor noise, to keep the point clean)
    ball=((xx-cx)**2+(yy-40)**2)<12**2; img[ball]=0.95              # the moving thing
    return np.clip(img,0,1)
f1=scene(50); f2=scene(58); diff=f2-f1
def bits(a): return 8*len(zlib.compress((a*255).astype(np.uint8).tobytes(),9))
fig,axs=plt.subplots(3,1,figsize=(6.4,9.6)); fig.patch.set_alpha(0)
for ax,img,title in zip(axs,[f1,f2,diff],[f"frame 1 — {bits(f1)/1000:.0f} kbit to send whole",f"frame 2 — {bits(f2)/1000:.0f} kbit to send whole",f"frame 2 − frame 1 — {bits(np.abs(diff))/1000:.1f} kbit: only the surprise"]):
    ax.imshow(img,cmap="gray",vmin=-1 if img is diff else 0,vmax=1); ax.set_title(title,color=GREY,fontsize=9.5); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color(GREY)
fig.suptitle("Send the prediction error, not the picture:\nthe codec's trick, and the brain's",color=GREY,fontsize=11)
fig.tight_layout(); fig.savefig("compression-is-intelligence-frames.svg",transparent=True)
print(f"frame1 {bits(f1)} bits, frame2 {bits(f2)} bits, difference {bits(np.abs(diff))} bits; nonzero pixels in the difference: {(np.abs(diff)>0.02).mean()*100:.1f}%")

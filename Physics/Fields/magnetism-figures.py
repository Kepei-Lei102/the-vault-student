"""Regenerate field model, illustrative hysteresis, and induced-magnet schematic."""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.special import ellipk, ellipe
from scipy.integrate import solve_ivp
P=Path(__file__).parent
G='#888888'; B='#2563eb'; R='#dc2626'; A='#f59e0b'; T='#0891b2'
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','font.family':'DejaVu Sans','font.size':12,'text.color':G,'axes.labelcolor':G,'xtick.color':G,'ytick.color':G,'axes.edgecolor':G})
def save(fig,name):
 p=P/name;fig.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None});plt.close(fig)
 s=p.read_text();s=re.sub(r'width="[^"]+" height="[^"]+" viewBox=', 'width="100%" viewBox=',s,count=1);p.write_text("\n".join(line.rstrip() for line in s.splitlines())+"\n")
def field(x,y):
 # Sum equal circular current loops with axes along x; common scale omitted.
 r=np.maximum(abs(y),1e-8);bx=np.zeros_like(x);by=np.zeros_like(x);a=.32
 for x0 in np.linspace(-1,1,41):
  z=x-x0;d=(a-r)**2+z*z;den=np.sqrt((a+r)**2+z*z);k=np.clip(4*a*r/den**2,0,1-1e-10)
  K,E=ellipk(k),ellipe(k)
  bx+=(K+(a*a-r*r-z*z)/np.maximum(d,1e-10)*E)/den
  by+=np.sign(y)*z/r*(-K+(a*a+r*r+z*z)/np.maximum(d,1e-10)*E)/den
 return bx,by
# Plot full numerical traces, clipping only their interior portions.
fig,ax=plt.subplots(figsize=(10,6.5))
# Trace each exterior line only until it reaches the magnet surface.
for sy in [.48,.70,1.,1.40,1.95,-.48,-.70,-1.,-1.40,-1.95]:
 def surface(t,p): return max(abs(p[0])-1,abs(p[1])-.34)
 surface.terminal=True;surface.direction=-1
 halves=[]
 for sign in [-1,1]:
  def rhs(t,p):
   u,v=field(np.array(p[0]),np.array(p[1]));n=np.hypot(u,v);return sign*np.array([u,v])/n
  sol=solve_ivp(rhs,[0,15],[0,sy],events=surface,max_step=.035,rtol=1e-7,atol=1e-9)
  halves.append(sol.y)
 curve=np.concatenate([halves[0][:,::-1],halves[1]],axis=1)
 ax.plot(curve[0],curve[1],color=B,lw=1.4)
 ax.annotate('',xy=(-.12,sy),xytext=(.12,sy),arrowprops={'arrowstyle':'->','color':B,'lw':1.5})
for xstart,xend in [(-3.5,-1),(1,3.5)]:
 ax.plot([xstart,xend],[0,0],color=B,lw=1.4)
 ax.annotate('',xy=((xstart+xend)/2+.18,0),xytext=((xstart+xend)/2-.18,0),arrowprops={'arrowstyle':'->','color':B,'lw':1.5})
for xx,c,lab in [(-1,R,'S'),(0,B,'N')]:
 ax.add_patch(Rectangle((xx,-.34),1,.68,facecolor=c+'22',edgecolor=c,lw=2,zorder=4));ax.text(xx+.5,.11,lab,ha='center',va='center',fontsize=17,zorder=5)
ax.annotate('',xy=(.7,-.20),xytext=(-.7,-.20),arrowprops={'arrowstyle':'->','color':G,'lw':2},zorder=6)
ax.text(0,-2.65,'Inside return direction: S to N',ha='center',fontsize=11)
ax.set(xlim=(-3.5,3.5),ylim=(-2.5,2.6),aspect='equal');ax.axis('off');ax.set_title('A compass traces the tangent: outside, N to S',pad=14,color=G)
ax.text(0,-2.98,'Closed flux • stronger near the ends • lines are a representation',ha='center',fontsize=11)
save(fig,'magnetism-field-map.svg')
fig,axes=plt.subplots(1,2,figsize=(11,4.5));tt=np.linspace(0,2*np.pi,1201)
for ax,hc,label,col in zip(axes,[.20,1.25],['Easy reversal','Harder reversal'],[T,B]):
 h=2.8*np.cos(tt);m=np.tanh(h+hc*np.sin(tt));ax.plot(h,m,color=col,lw=2.4)
 for ix in (210,810):ax.annotate('',xy=(h[ix+30],m[ix+30]),xytext=(h[ix],m[ix]),arrowprops={'arrowstyle':'->','color':col,'lw':2})
 ax.axhline(0,color=G,lw=.7);ax.axvline(0,color=G,lw=.7);ax.set(xlabel='Magnetising field H (normalised)',ylabel='Magnetisation M (normalised)',title=label,xlim=(-3.2,3.2),ylim=(-1.2,1.2));ax.spines[['top','right']].set_visible(False)
 axes[0].text(0,-1.94,'Schematic loops: different histories at the same H; not measured alloys',transform=axes[0].transData,fontsize=11)
fig.tight_layout();save(fig,'magnetism-hysteresis.svg')
s=['<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 860 350"><style>text{font-family:Arial,sans-serif;fill:#888;font-size:18px}</style>']
def text(x,y,t,size=18):s.append(f'<text x="{x}" y="{y}" text-anchor="middle" style="font-size:{size}px">{t}</text>')
def bar(x,y,w,h):
 for dx,col,lab in [(0,R,'S'),(w/2,B,'N')]:
  s.append(f'<rect x="{x+dx}" y="{y}" width="{w/2}" height="{h}" rx="3" fill="{col}" fill-opacity="0.15" stroke="{col}" stroke-width="2"/>');text(x+dx+w/4,y+h/2+6,lab)
text(430,34,'An induced chain: the near end acquires opposite polarity',23)
bar(35,110,190,70);bar(275,125,200,40);bar(525,125,200,40)
text(130,225,'Permanent magnet');text(375,225,'First nail');text(625,225,'Second nail')
text(250,93,'attract',15);text(500,93,'attract',15)
text(430,282,'Reverse the source: every induced polarity reverses; attraction remains.',17)
text(430,320,'Attraction alone does not prove an object was already a magnet.',17)
s.append('</svg>');(P/'magnetism-induced-chain.svg').write_text('\n'.join(s))

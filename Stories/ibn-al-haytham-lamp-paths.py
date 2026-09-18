"""Regenerate the idealised two-lamp ray diagram; matplotlib, no simulation claims."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','font.family':'DejaVu Sans','font.size':12,'text.color':'#888888'})
fig, axs=plt.subplots(1,2,figsize=(12,4.7))
for ax,blocked in zip(axs,[False,True]):
    ax.set(xlim=(-3.1,3.5),ylim=(-2.25,2.2));ax.set_aspect('equal');ax.axis('off')
    ax.plot([0,0],[-1.6,-.07],color='#888888',lw=4)
    ax.plot([0,0],[.07,1.6],color='#888888',lw=4)
    ax.plot([2.4,2.4],[-1.6,1.6],color='#888888',lw=3)
    ax.text(0,1.78,'Small opening',ha='center',fontsize=11)
    ax.text(2.4,1.78,'Screen',ha='center',fontsize=11)
    ax.plot([-2.4,2.4],[0,0],color='#888888',ls=':',lw=1,alpha=.5)
    for y,col,name in [(1,'#2563eb','A'),(-1,'#059669','B')]:
        ax.scatter([-2.4],[y],s=85,color=col,zorder=4)
        ax.text(-2.65,y,name,ha='right',va='center',weight='bold')
        if blocked and name=='A':
            # y=-x/2.4; paddle at x=-1.2 intercepts only A, y=+0.5.
            ax.plot([-2.4,-1.2],[1,.5],color=col,lw=2)
            ax.plot([-1.2,-1.2],[.23,.77],color='#dc2626',lw=5)
            ax.text(-1.23,1.16,'Block A only',ha='center',fontsize=10)
            ax.scatter([2.4],[-y],s=95,facecolors='none',edgecolors='#888888',linestyle=':')
            ax.text(2.65,-y,'gone',va='center',fontsize=10)
        else:
            ax.plot([-2.4,2.4],[y,-y],color=col,lw=2)
            ax.annotate('',xy=(.85,-y*.85/2.4),xytext=(.3,-y*.3/2.4),arrowprops={'arrowstyle':'->','color':col,'lw':2})
            ax.scatter([2.4],[-y],s=95,color=col,zorder=4)
            ax.text(2.65,-y,name,va='center',weight='bold')
    ax.text(.1,-2.0,'Only A disappears' if blocked else 'The paths cross; the patches stay separate',ha='center',fontsize=11)
fig.subplots_adjust(left=.015,right=.98,bottom=.03,top=.93,wspace=.08)
p=Path(__file__).with_suffix('.svg')
fig.savefig(p,transparent=True,metadata={'Date':None})
s=p.read_text();s=re.sub(r'<svg[^>]*>',lambda m:re.sub(r' width="[^"]*"',' width="100%"',re.sub(r' height="[^"]*"','',m.group())),s,count=1)
p.write_text('\n'.join(x.rstrip() for x in s.splitlines())+'\n')
# Exact geometry: intersections with hole and screen, then selective occlusion.
for y in [-1,1]:
    assert y+(0+2.4)*(-2*y/4.8)==0
    assert y+(2.4+2.4)*(-2*y/4.8)==-y
assert .23 < .5 < .77 and not .23 < -.5 < .77
print('ray geometry and selective blocking verified')

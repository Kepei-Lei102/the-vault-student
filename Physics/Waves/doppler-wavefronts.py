"""Exact circular wavefront snapshots, at equal emission intervals, in the medium frame."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':11,
 'text.color':'#888888','axes.labelcolor':'#888888','figure.facecolor':'none','axes.facecolor':'none'})
fig,axs=plt.subplots(2,1,figsize=(9,7.5))
fig.subplots_adjust(hspace=.40)
for ax in axs:
 ax.set_aspect('equal');ax.set_xlim(-6.5,6.5);ax.set_ylim(-4.5,4.5);ax.axis('off')
 ax.axhline(0,color='#888888',alpha=.22,lw=.8)
for age in range(1,5):
 center=-.45*age
 axs[0].add_patch(Circle((center,0),age,fill=False,lw=1.6,edgecolor='#2563eb'))
 axs[0].plot(center,0,'o',ms=3,color='#888888')
 axs[1].add_patch(Circle((0,0),age,fill=False,lw=1.6,edgecolor='#2563eb'))
for ax in axs:
 ax.plot(0,0,'o',color='#7c3aed',ms=7)
 ax.annotate('Source now',xy=(0,0),xytext=(4.6,2.8),ha='center',color='#888888',arrowprops={'arrowstyle':'-','color':'#888888','lw':.8})
axs[0].set_title('A. Source moves right; observer stays still',pad=10)
axs[0].annotate('',xy=(1.2,0),xytext=(.15,0),arrowprops={'arrowstyle':'->','color':'#7c3aed','lw':2})
axs[0].plot(5.2,0,'s',color='#059669',ms=7)
axs[0].text(5.2,-.85,'Observer',ha='center',color='#888888')
axs[0].text(.5,-.13,'Behind: wider spacing     •     Ahead: closer spacing',transform=axs[0].transAxes,ha='center',color='#888888')
axs[1].set_title('B. Source stays still; observer moves towards it',pad=10)
axs[1].plot(3.5,0,'s',color='#059669',ms=7)
axs[1].annotate('',xy=(2.1,0),xytext=(3.4,0),arrowprops={'arrowstyle':'->','color':'#059669','lw':2})
axs[1].annotate('Observer',xy=(3.5,0),xytext=(5.2,-2.3),ha='center',color='#888888',arrowprops={'arrowstyle':'-','color':'#888888','lw':.8})
axs[1].text(.5,-.13,'Spacing unchanged     •     Observer meets more crests each second',transform=axs[1].transAxes,ha='center',color='#888888')
p=Path(__file__).with_suffix('.svg')
fig.savefig(p,transparent=True,bbox_inches='tight')
s=p.read_text();s=re.sub(r'<svg([^>]+)>',lambda m:'<svg'+re.sub(r'\s(?:width|height)="[^"]*"','',m[1])+' width="100%">',s,count=1)
p.write_text('\n'.join(l.rstrip() for l in s.splitlines())+'\n')

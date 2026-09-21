"""Regenerate the two Lagrange figures. Stack: matplotlib; deterministic SVG."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Arc

HERE = Path(__file__).resolve().parent
GREY, BLUE, GREEN, AMBER = '#888888', '#2563eb', '#059669', '#f59e0b'
plt.rcParams.update({'text.color': GREY, 'axes.labelcolor': GREY,
                     'xtick.color': GREY, 'ytick.color': GREY,
                     'axes.edgecolor': GREY, 'font.size': 12,
                     'svg.hashsalt': 'vault', 'svg.fonttype': 'path'})

def save(fig, name):
    path = HERE / name
    fig.savefig(path, transparent=True, metadata={'Date': None})
    text = path.read_text()
    text = re.sub(r'width="[\d.]+pt"', 'width="100%"', text, count=1)
    text = re.sub(r'height="[\d.]+pt"', '', text, count=1)
    path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n')
    plt.close(fig)

def axes_style(ax):
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(alpha=.15, color=GREY)

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.9))
fig.subplots_adjust(left=.065, right=.97, bottom=.29, top=.84, wspace=.36)
theta = np.pi/3
a = np.array([1., 0.]); b = np.array([np.cos(theta), np.sin(theta)])
ax.add_patch(Polygon([[0,0],a,a+b,b], facecolor=GREEN, alpha=.18, edgecolor=GREEN))
for vec, col in [(a, BLUE), (b, AMBER)]:
    ax.annotate('', xy=vec, xytext=(0,0), arrowprops={'arrowstyle':'->','color':col,'lw':2.5})
ax.plot([b[0], b[0]], [0,b[1]], '--', color=GREY)
ax.add_patch(Arc((0,0),.48,.48,theta1=0,theta2=60,edgecolor=GREY))
ax.text(.3,.15,r'$60^\circ$'); ax.text(1.0,-.13,r'$\mathbf{a}$')
ax.text(.36,.94,r'$\mathbf{b}$'); ax.text(.14,-.21,'projection = 0.5',fontsize=11)
ax.text(.89,.51,r'area = $\sqrt{3}/2$',ha='center',fontsize=11)
ax.set(xlim=(-.15,1.8), ylim=(-.3,1.16), aspect='equal')
ax.axis('off'); ax.set_title('Two unit vectors', pad=18)
t = np.linspace(0,np.pi,361)
bx.plot(np.degrees(t), np.cos(t)**2, color=BLUE, lw=2.4, label='squared dot product')
bx.plot(np.degrees(t), np.sin(t)**2, color=GREEN, lw=2.4, label='squared area')
bx.set(xlim=(0,180),ylim=(-.03,1.06),xticks=[0,45,90,135,180],yticks=[0,.5,1],xlabel='Angle (degrees)')
bx.set_title('The sum stays at 1',pad=18); axes_style(bx)
fig.legend(*bx.get_legend_handles_labels(),loc='lower center',bbox_to_anchor=(.5,.11),ncol=2,frameon=False,fontsize=11)
fig.text(.5,.065,r'$(\mathbf{a}\cdot\mathbf{b})^2 + \mathrm{area}^2 = 1$     (unit lengths)',ha='center',fontsize=15)
save(fig,'lagrange-identity-geometry.svg')

fig, ax = plt.subplots(figsize=(9,5.2))
fig.subplots_adjust(left=.11,right=.96,bottom=.2,top=.85)
x=np.array([1.,2.,3.,4.]); y=np.array([2.,4.,4.,6.]); pred=1+1.2*x
ax.plot([.6,4.4],[1+1.2*.6,1+1.2*4.4],color=BLUE,lw=2,label=r'fit: $\widehat y=1+1.2x$')
ax.vlines(x,np.minimum(y,pred),np.maximum(y,pred),color=AMBER,lw=3,label='vertical residuals')
ax.scatter(x,y,color=GREEN,s=70,zorder=5,label='paired readings')
for xx,yy,rr in zip(x,y,y-pred):
    ax.annotate(f'{rr:+.1f}',(xx,yy),xytext=(12,12 if rr>=0 else -21),textcoords='offset points')
ax.set(xlim=(.5,4.6),ylim=(1.3,6.8),xticks=[1,2,3,4],xlabel='Reference reading x (V)',ylabel='Sensor reading y (V)')
axes_style(ax); ax.legend(frameon=False,loc='upper left',fontsize=11)
ax.set_title('Strong association still leaves a fitting error',pad=18)
fig.text(.5,.055,r'$r^2=0.9$     SSE $=(-0.2)^2+(0.6)^2+(-0.6)^2+(0.2)^2=0.8\ \mathrm{V}^2$',ha='center',fontsize=12)
save(fig,'lagrange-identity-correlation.svg')

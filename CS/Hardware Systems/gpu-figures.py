"""Regenerate coordinate-based SVGs; transparent, deterministic Vault palette."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

ROOT = Path(__file__).resolve().parent
GRAY, BLUE, GREEN, PURPLE, AMBER = '#888888', '#2563eb', '#059669', '#7c3aed', '#f59e0b'
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':12, 'text.color':GRAY,
 'axes.labelcolor':GRAY, 'xtick.color':GRAY, 'ytick.color':GRAY,
 'axes.edgecolor':GRAY, 'svg.fonttype':'none', 'svg.hashsalt':'vault'})

def save(fig, name):
    path = ROOT/name
    fig.savefig(path, transparent=True, metadata={'Date':None}, bbox_inches='tight')
    s=path.read_text()
    s=re.sub(r'<svg([^>]*?)width="[^"]+" height="[^"]+"',r'<svg\1width="100%"',s, count=1)
    path.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n')
    plt.close(fig)

fig, ax=plt.subplots(figsize=(8,6))
ax.set(xlim=(-.1,8),ylim=(-.1,8),aspect='equal',xticks=range(9),yticks=range(9),xlabel='Screen x',ylabel='Screen y')
ax.grid(color=GRAY,alpha=.15)
ax.add_patch(Polygon([(1,1),(7,1),(1,7)],facecolor=BLUE,alpha=.13))
ax.plot([1,7,1,1],[1,1,7,1],color=BLUE,lw=2)
for y in range(8):
 for x in range(8):
  if x>=1 and y>=1 and x+y<=7:
   ax.scatter(x+.5,y+.5,s=25,color=GREEN)
for x,y,t in [(1,1,'A (1,1)'),(7,1,'B (7,1)'),(1,7,'C (1,7)')]:
 ax.annotate(t,(x,y),xytext=(5,9),textcoords='offset points',color=GRAY)
ax.scatter(2.5,2.5,s=130,facecolors='none',edgecolors=AMBER,lw=2)
ax.annotate('p = (2.5, 2.5)\nweights: ½, ¼, ¼',(2.5,2.5),xytext=(4.1,4.7),arrowprops={'arrowstyle':'->','color':GRAY},color=GRAY)
ax.set_title('One triangle: 21 covered sample centres',pad=16,color=GRAY)
fig.text(.51,.01,'One sample per pixel • inclusive edges • no perspective',ha='center',color=GRAY,fontsize=10)
save(fig,'gpu-rasterisation.svg')

fig=plt.figure(figsize=(9,7))
gs=fig.add_gridspec(2,2,hspace=.65)
def matrix(ax, values, title, color):
 ax.set(xlim=(0,2),ylim=(0,2),aspect='equal');ax.axis('off');ax.set_title(title,color=GRAY,pad=12)
 for i in range(2):
  for j in range(2):
   ax.add_patch(Rectangle((j,1-i),1,1,facecolor=color,alpha=.14,edgecolor='none'))
   ax.add_patch(Rectangle((j,1-i),1,1,fill=False,edgecolor=color,lw=1.5))
   ax.text(j+.5,1.5-i,str(values[i][j]),ha='center',va='center',fontsize=21,color=GRAY)
matrix(fig.add_subplot(gs[0,0]),[[1,2],[3,4]],'A: four loaded values',BLUE)
matrix(fig.add_subplot(gs[0,1]),[[5,6],[7,8]],'B: four loaded values',PURPLE)
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
ax.text(.5,.96,'Each row of A meets each column of B',ha='center',fontsize=15)
ax.text(.26,.73,'1×5 + 2×7 = 19',ha='center',fontsize=17)
ax.text(.74,.73,'1×6 + 2×8 = 22',ha='center',fontsize=17)
ax.text(.26,.50,'3×5 + 4×7 = 43',ha='center',fontsize=17)
ax.text(.74,.50,'3×6 + 4×8 = 50',ha='center',fontsize=17)
ax.text(.5,.19,'8 input loads; 8 multiply-adds; 4 outputs',ha='center',fontsize=15)
ax.text(.5,-.04,'Independent dot products request 16 inputs in the no-cache model.',ha='center',fontsize=11)
save(fig,'gpu-tiling.svg')

"""Regenerate schematic orbital occupancy and quantitative FD curves."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
GREY='#888888'; BLUE='#2563eb'; GREEN='#059669'; RED='#dc2626'; AMBER='#f59e0b'


def orbitals():
    # Schematic: no spatial/energy scale is implied by these boxes.
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 860 430">',
      '<style>text {font-family:system-ui,sans-serif;fill:#888;font-size:19px}.title{font-size:23px;font-weight:600}.small{font-size:17px}</style>']
    def text(x,y,t,cl=''):
        parts.append(f'<text x="{x}" y="{y}" class="{cl}">{t}</text>')
    def box(x,y,spins,color=BLUE):
        parts.append(f'<rect x="{x}" y="{y}" width="66" height="56" rx="6" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="2"/>')
        for i,spin in enumerate(spins):
            xx=x+22+22*i if len(spins)>1 else x+33
            y1,y2=(y+43,y+14) if spin==1 else (y+13,y+42)
            dy=7 if spin==1 else -7
            parts.append(f'<path d="M {xx},{y1} V {y2} M {xx-5},{y2+dy} L {xx},{y2} L {xx+5},{y2+dy}" fill="none" stroke="{color}" stroke-width="2.5"/>')
    text(24,35,'One orbital, two independent spin states','title')
    box(40,65,[1,-1],GREEN);text(125,89,'Allowed');text(125,115,'Same orbital; different spin states','small')
    box(455,65,[1,1],RED);text(540,89,'Forbidden');text(540,115,'Same complete state twice','small')
    parts.append('<path d="M24 151 H836" stroke="#888" opacity="0.3"/>')
    text(24,190,'Carbon ground configuration: 1s² 2s² 2p²','title')
    for x,label,spins in [(40,'1s',[1,-1]),(185,'2s',[1,-1]),(370,'2p',[1]),(446,'',[1]),(522,'',[])]:
        box(x,215,spins);text(x+20,301,label)
    text(635,240,'Three 2p orbitals','small');text(635,269,'Six spin states','small')
    text(40,350,'Pauli permits the arrangement. Hund’s rule selects the parallel, separate 2p filling.','small')
    text(40,385,'A box represents a wavefunction, not a compartment in the atom.','small')
    parts.append('</svg>')
    (HERE/'pauli-orbitals.svg').write_text('\n'.join(parts)+'\n')


def edge():
    plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','font.size':13,
      'text.color':GREY,'axes.labelcolor':GREY,'axes.edgecolor':GREY,'xtick.color':GREY,'ytick.color':GREY})
    fig,ax=plt.subplots(figsize=(9,4.6),layout='constrained')
    ax.set_facecolor('none');fig.patch.set_alpha(0)
    x=np.linspace(-.8,.8,1001)
    ax.plot([-.8,0,0,.8],[1,1,0,0],color=GREY,ls='--',lw=1.8,label='T = 0 limit')
    for ratio,color in [(.04,BLUE),(.16,AMBER)]:
        ax.plot(x,1/(np.exp(x/ratio)+1),color=color,lw=2.8,label=f'T / T_F = {ratio}')
    ax.axvline(0,color=GREY,alpha=.3,lw=1)
    ax.set(xlim=(-.8,.8),ylim=(-.035,1.055),xlabel=r'Energy relative to chemical potential: $(E-\mu)/E_F$',ylabel='Mean occupation f(E)')
    ax.set_title('Warming blurs the edge; it does not raise the occupancy limit',color=GREY,pad=15,fontsize=15)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.15,color=GREY)
    ax.legend(loc='upper right',facecolor='none',edgecolor=GREY,labelcolor=GREY,fontsize=11)
    p=HERE/'pauli-fermi-edge.svg'
    fig.savefig(p,transparent=True,metadata={'Date':None})
    plt.close(fig)
    s=p.read_text();s=re.sub(r'<svg width="[^"]+" height="[^"]+"', '<svg width="100%"',s,count=1)
    p.write_text("\n".join(line.rstrip() for line in s.splitlines()) + "\n")

if __name__=='__main__':
    orbitals();edge()

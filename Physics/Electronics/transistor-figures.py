"""Deterministic SVGs. Matplotlib for curves; SVG for schematic layout."""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).resolve().parent
GREY='#888888';BLUE='#2563eb';GREEN='#059669';AMBER='#f59e0b';PURPLE='#7c3aed'
plt.rcParams.update({'font.family':'Arial','font.size':12,'text.color':GREY,'axes.labelcolor':GREY,'xtick.color':GREY,'ytick.color':GREY,'axes.edgecolor':GREY,'svg.fonttype':'none','svg.hashsalt':'vault'})
def finish(fig,name):
    p=ROOT/name;fig.savefig(p,transparent=True,metadata={'Date':None},bbox_inches='tight',pad_inches=.2)
    s=p.read_text();s=re.sub(r'<svg([^>]*?)width="[^"]+"([^>]*?)height="[^"]+"',r'<svg\1width="100%"\2',s,count=1);p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n');plt.close(fig)

def toy(v):return np.where(v<=.8,3.3-.2*v/.8,np.where(v>=2,.2*(3.3-v)/1.3,3.1-2.9*(v-.8)/1.2))
fig,axs=plt.subplots(1,2,figsize=(11,4.5),gridspec_kw={'wspace':.42})
a=axs[0];a.set_title('A guaranteed output fits inside an accepted input',fontsize=12,pad=16);a.set_xlim(-.6,1.6);a.set_ylim(-.05,3.55);a.set_xticks([0,1],['Output','Next input']);a.set_ylabel('Voltage / V');a.set_yticks([0,.2,.8,2,3.1,3.3]);a.tick_params(axis='y',labelsize=10)
for x,lo,hi in [(0,.2,3.1),(1,.8,2)]:
 a.add_patch(Rectangle((x-.2,0),.4,lo,facecolor=BLUE,alpha=.22,edgecolor=BLUE));a.add_patch(Rectangle((x-.2,hi),.4,3.3-hi,facecolor=GREEN,alpha=.22,edgecolor=GREEN))
a.annotate('',xy=(.4,.8),xytext=(.4,.2),arrowprops={'arrowstyle':'<->','color':AMBER});a.text(.48,.5,'0.6 V',fontsize=11,va='center')
a.annotate('',xy=(.4,3.1),xytext=(.4,2),arrowprops={'arrowstyle':'<->','color':AMBER});a.text(.48,2.55,'1.1 V',fontsize=11,va='center')
a.spines[['top','right']].set_visible(False)
a=axs[1];v=np.linspace(0,3.3,600);a.plot(v,toy(v),color=PURPLE,lw=2.8);a.axvspan(.8,2,color=AMBER,alpha=.13);a.set(xlim=(0,3.3),ylim=(0,3.4),xlabel='Input voltage / V',ylabel='Settled output / V');a.set_title('An illustrative inverter — not a measured chip',fontsize=12,pad=16);a.set_xticks([0,.8,2,3.3]);a.set_yticks([0,1,2,3.3]);a.text(1.4,.5,'No input\nguarantee',ha='center',fontsize=11);a.scatter([.65],[toy(.65)],color=GREEN,zorder=3);a.annotate('0.65 V to 3.1375 V',(.65,toy(.65)),xytext=(1.18,2.65),fontsize=10,arrowprops={'arrowstyle':'-','color':GREY});a.spines[['top','right']].set_visible(False)
finish(fig,'transistor-voltage-contract.svg')
fig,axs=plt.subplots(1,2,figsize=(11,4.3),gridspec_kw={'wspace':.38})
a=axs[0];t=np.linspace(0,50,500);a.plot(t,3.3*(1-np.exp(-t/10)),color=BLUE,lw=2.7);a.axhline(3.3,color=GREY,ls='--',lw=1);a.scatter([6.931],[1.65],color=GREEN,zorder=4);a.annotate('Half charged\nat 6.93 ns',(6.931,1.65),xytext=(19,.6),arrowprops={'arrowstyle':'->','color':GREY});a.set(xlabel='Time / ns',ylabel='Output / V',xlim=(0,50),ylim=(0,3.6));a.set_title('1 kohm x 10 pF: RC = 10 ns',fontsize=13,pad=14);a.spines[['top','right']].set_visible(False)
a=axs[1];names=['From supply','After charge','After discharge'];a.bar(names,[108.9,54.45,108.9],color=[BLUE,AMBER,AMBER],alpha=.2);a.bar(['After charge'],[54.45],bottom=[54.45],color=GREEN,alpha=.2);a.text(1,26,'heat',ha='center');a.text(1,79,'stored',ha='center');a.text(2,52,'all heat',ha='center');a.text(0,114,'108.9 pJ',ha='center');a.set(ylabel='Energy / pJ',ylim=(0,132));a.set_title('Same energy, different destination',fontsize=13,pad=14);a.tick_params(axis='x',labelsize=10);a.spines[['top','right']].set_visible(False)
finish(fig,'transistor-delay-and-energy.svg')
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 390" width="100%">
<style>text{font-family:system-ui,-apple-system,sans-serif;fill:#888;font-size:15px}.title{font-size:19px;font-weight:600}.small{font-size:13px}</style>
<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#888"/></marker></defs>
<text x="205" y="26" text-anchor="middle" class="title">NMOS: field creates a channel</text>
<rect x="50" y="160" width="315" height="140" rx="6" fill="#7c3aed" fill-opacity=".12" stroke="#7c3aed"/>
<rect x="70" y="160" width="75" height="55" fill="#2563eb" fill-opacity=".18" stroke="#2563eb"/>
<rect x="270" y="160" width="75" height="55" fill="#2563eb" fill-opacity=".18" stroke="#2563eb"/>
<text x="107" y="190" text-anchor="middle">n+ source</text><text x="307" y="190" text-anchor="middle">n+ drain</text>
<text x="208" y="266" text-anchor="middle">p-type body</text>
<rect x="140" y="150" width="135" height="8" fill="#f59e0b" fill-opacity=".22" stroke="#f59e0b"/>
<rect x="140" y="121" width="135" height="22" fill="#7c3aed" fill-opacity=".2" stroke="#7c3aed"/>
<text x="209" y="106" text-anchor="middle">positive gate</text>
<path d="M145 164H270" stroke="#059669" stroke-width="4"/>
<path d="M170 171V212 M207 171V212 M245 171V212" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
<text x="208" y="234" text-anchor="middle" class="small">electric field into the body</text>
<path d="M107 160V126 M307 160V126" stroke="#888" stroke-width="2"/>
<text x="83" y="114">S</text><text x="304" y="114">D</text>
<text x="326" y="148" class="small">insulator</text><path d="M317 151H278" stroke="#888"/>
<text x="207" y="329" text-anchor="middle">Electron-rich surface joins source to drain.</text>
<text x="207" y="353" text-anchor="middle" class="small">Body tied to source; dimensions not to scale.</text>
<text x="647" y="26" text-anchor="middle" class="title">CMOS: two complementary paths</text>
<path d="M680 65V88 M680 154V229 M680 295V330" stroke="#888" stroke-width="3" fill="none"/>
<text x="680" y="53" text-anchor="middle">VDD</text>
<rect x="635" y="88" width="90" height="66" rx="8" fill="#059669" fill-opacity=".15" stroke="#059669" stroke-width="2"/>
<text x="680" y="117" text-anchor="middle">PMOS</text><text x="680" y="138" text-anchor="middle" class="small">LOW: on</text>
<rect x="635" y="229" width="90" height="66" rx="8" fill="#2563eb" fill-opacity=".15" stroke="#2563eb" stroke-width="2"/>
<text x="680" y="258" text-anchor="middle">NMOS</text><text x="680" y="280" text-anchor="middle" class="small">HIGH: on</text>
<path d="M470 191H543V121H631 M543 191V262H631" stroke="#7c3aed" stroke-width="2" fill="none"/>
<text x="490" y="178" text-anchor="middle">input</text><circle cx="543" cy="191" r="4" fill="#7c3aed"/>
<path d="M680 191H817" stroke="#888" stroke-width="2"/><circle cx="680" cy="191" r="4" fill="#888"/>
<text x="790" y="176" text-anchor="middle">output</text>
<path d="M665 330H695 M670 336H690 M676 342H684" stroke="#888" stroke-width="2"/>
<text x="647" y="372" text-anchor="middle" class="small">Switch model: bodies and gate capacitances omitted.</text>
</svg>'''
(ROOT/'transistor-field-and-cmos.svg').write_text(svg)

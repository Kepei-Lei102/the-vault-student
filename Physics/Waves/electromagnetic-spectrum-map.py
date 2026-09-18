"""Regenerate the logarithmic spectrum map and verify numerical examples."""
from pathlib import Path
import re
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

HERE = Path(__file__).resolve().parent
GREY = '#888888'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'text.color': GREY, 'axes.labelcolor': GREY,
                     'xtick.color': GREY, 'ytick.color': GREY,
                     'svg.fonttype': 'none', 'svg.hashsalt': 'vault'})
fig, (ax, zoom) = plt.subplots(2, 1, figsize=(12, 6.8),
                             gridspec_kw={'height_ratios': [1.35, 1]})
fig.patch.set_alpha(0)
fig.subplots_adjust(left=.055, right=.965, bottom=.14, top=.80, hspace=.94)
ax.set_xlim(3, -13)
ax.set_ylim(0, 1)
ax.set_yticks([])
ax.set_xlabel('Vacuum wavelength / m — logarithmic scale', labelpad=10)
ax.set_xticks([3, 0, -3, -6, -9, -12])
ax.set_xticklabels(['10³', '1', '10⁻³', '10⁻⁶', '10⁻⁹', '10⁻¹²'])
for a in (ax, zoom):
    a.set_facecolor('none')
    for sp in a.spines.values(): sp.set_visible(False)
    a.spines['bottom'].set_visible(True)
    a.spines['bottom'].set_color(GREY)

bands=[('Radio',3,0,'#2563eb'),('Microwave',0,-3,'#0891b2'),
       ('Infrared',-3,math.log10(700e-9),'#dc2626'),
       ('Visible',math.log10(700e-9),math.log10(400e-9),'#059669'),
       ('Ultraviolet',math.log10(400e-9),-8,'#7c3aed'),
       ('X-rays',-8,-11,'#f59e0b'),('Gamma',-11,-13,'#2563eb')]
for name,left,right,col in bands:
    ax.add_patch(Rectangle((right,.10),left-right,.7,facecolor=col,alpha=.20,
                           edgecolor='none'))
    ax.plot([right,right],[.10,.8],color=GREY,lw=.7,alpha=.5)
    if name=='Visible':
        ax.annotate(name,xy=((left+right)/2,.8),xytext=(-5.75,1.03),
                    ha='center',fontsize=12,arrowprops={'arrowstyle':'-','color':GREY})
    elif name=='Ultraviolet':
        ax.text((left+right)/2,.44,'Ultra-\nviolet',ha='center',va='center',fontsize=11)
    else:ax.text((left+right)/2,.44,name,ha='center',va='center')
ax.annotate('Longer wavelength',xy=(.0,1.19),xytext=(.28,1.19),xycoords='axes fraction',
            ha='center',va='center',arrowprops={'arrowstyle':'->','color':GREY})
ax.annotate('Higher frequency and photon energy',xy=(1,1.19),xytext=(.68,1.19),xycoords='axes fraction',
            ha='center',va='center',arrowprops={'arrowstyle':'->','color':GREY})
fig.text(.055,.96,'ONE FAMILY — SIXTEEN ORDERS OF MAGNITUDE',fontsize=16,weight='bold')
fig.text(.055,.915,'Approximate naming regions; microwaves are also radio-frequency radiation.',fontsize=11)
zoom.set_xlim(700,400);zoom.set_ylim(0,1);zoom.set_yticks([])
zoom.set_xlabel('Visible wavelength / nm — separate linear zoom',labelpad=10)
zoom.set_xticks([700,650,600,550,500,450,400])
visible=[('Red',700,620,'#dc2626'),('Orange',620,590,'#f59e0b'),
         ('Yellow',590,570,'#eab308'),('Green',570,495,'#059669'),
         ('Blue',495,450,'#2563eb'),('Violet',450,400,'#7c3aed')]
for name,left,right,col in visible:
    zoom.add_patch(Rectangle((right,.05),left-right,.55,facecolor=col,alpha=.22,edgecolor='none'))
    # Narrow colour names are staggered, never squeezed into their regions.
    height=.88 if name in ('Orange','Green','Violet') else .70
    centre=(left+right)/2
    zoom.plot([centre,centre],[.6,height-.08],color=GREY,lw=.7)
    zoom.text(centre,height,name,ha='center',va='center',fontsize=11)
zoom.set_title('THE SMALL WINDOW OUR EYES DETECT',loc='left',pad=23,fontsize=13,color=GREY)
fig.text(.055,.018,'The drawn X-ray/gamma boundary is conventional; their energies overlap and source-based names also occur.',fontsize=10)
out=HERE/'electromagnetic-spectrum-map.svg'
fig.savefig(out,transparent=True,metadata={'Date':None})
s=out.read_text()
def responsive_root(match):
    tag = re.sub(r' width="[^"]+"', ' width="100%"', match.group(0))
    return re.sub(r' height="[^"]+"', '', tag)
s=re.sub(r'<svg\b[^>]*>', responsive_root, s, count=1)
s='\n'.join(line.rstrip() for line in s.splitlines())+'\n'
out.write_text(s)
plt.close(fig)

# Independent arithmetic and boundary checks for the accompanying text.
c=3e8;h=6.626e-34
assert math.isclose(c*6*5e-15,9e-6)
assert math.isclose(c/2.4e9,.125)
assert math.isclose((c/(500e-9))/2.4e9,250000)
assert 700e-9 < 12e-6 < 28e-6 < 1e-3
for wavelength in np.logspace(-13,3,1000):
    frequency=c/wavelength
    assert math.isclose(frequency*wavelength,c)
    assert math.isclose(h*frequency,h*c/wavelength)
print('PASS: 1,000 wavelength/frequency/energy identities and four worked-value checks')
print('Photon rates: microwave',1/(h*2.4e9),'visible',1/(h*c/(500e-9)))
print(out)

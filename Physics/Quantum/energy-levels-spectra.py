#!/usr/bin/env python3
"""Hydrogenic transition explorer and regenerable figures.

Standard-library numerical mode; optional matplotlib/numpy for --figures.
E_n = -13.6 Z^2/n^2 eV is the rounded, nonrelativistic model, not precision data.
All descending routes ignore selection rules and populations. No brightness model.
"""
import argparse
from itertools import combinations
from math import isclose
from pathlib import Path
import re

H = 6.62607015e-34
C = 299792458.0
EV = 1.602176634e-19
HC = H * C / EV * 1e9  # eV nm
HERE = Path(__file__).resolve().parent


def energy(n, charge=1):
    if not isinstance(n, int) or n < 1 or charge < 1:
        raise ValueError('n and nuclear charge must be positive; n must be an integer')
    return -13.6 * charge**2 / n**2


def transition(upper, lower, charge=1):
    if upper <= lower:
        raise ValueError('Emission requires upper > lower >= 1')
    gap = energy(upper, charge) - energy(lower, charge)
    return gap, gap * EV / H, HC / gap


def routes(upper, lower=1):
    if upper == lower:
        yield (lower,)
        return
    for nxt in range(lower, upper):
        for tail in routes(nxt, lower):
            yield (upper,) + tail


def verify():
    """Check conservation over alternative physical paths and known examples."""
    route_count = 0
    for z in (1, 2, 3):
        for top in range(2, 11):
            direct = transition(top, 1, z)[0]
            for path in routes(top):
                gaps = [transition(a, b, z)[0] for a, b in zip(path, path[1:])]
                wavelengths = [transition(a, b, z)[2] for a, b in zip(path, path[1:])]
                assert isclose(sum(gaps), direct, rel_tol=1e-13)
                assert isclose(sum(1/w for w in wavelengths), direct/HC, rel_tol=1e-13)
                route_count += 1
            assert len(list(combinations(range(1, top+1), 2))) == top*(top-1)//2
    # Measured visible Balmer air centres, rounded to 0.1 nm. The model is vacuum
    # and rounded in energy; deliberately require only a school-level agreement.
    for n, observed_air in [(3, 656.3), (4, 486.1), (5, 434.0), (6, 410.2)]:
        assert abs(transition(n, 2)[2] / observed_air - 1) < 0.001
    assert isclose(transition(3, 2, 2)[2] * 4, transition(3, 2)[2])
    # Reconstruct the supplied Cambridge data, not a replacement Bohr ladder.
    reconstructed = [-13.6 + 6.63e-34*f/1.60e-19 for f in (2.47e15, 2.92e15, 3.09e15)]
    assert [round(x, 1) for x in reconstructed] == [-3.4, -1.5, -0.8]
    ib_wavelength = HC / 1.89
    assert 655 < ib_wavelength < 659
    # In the Bohr model U = 2E, K = -E: an excitation raises E and lowers K.
    before, after = energy(1), energy(2)
    assert after > before and -after < -before and 2*after > 2*before
    assert isclose((2*after-2*before) + (-after+before), after-before)
    print(f'Checks passed: {route_count} cascades conserve energy; Z scaling, Balmer, Cambridge, IB and AP checks.')


def figures():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import to_rgba
    plt.rcParams.update({'svg.fonttype':'none', 'svg.hashsalt':'vault-energy-levels',
                         'font.family':'DejaVu Sans','font.size':11,'text.color':'#888888',
                         'axes.labelcolor':'#888888','axes.edgecolor':'#888888',
                         'xtick.color':'#888888','ytick.color':'#888888'})
    grey='#888888'; blue='#2563eb'; purple='#7c3aed'; green='#059669'; teal='#0891b2'

    def base(ax):
        ax.set_facecolor('none')
        for side in ('top','right'):ax.spines[side].set_visible(False)
        ax.grid(axis='y',color=grey,alpha=.15)

    def save(fig,name):
        fig.patch.set_alpha(0)
        p=HERE/(name+'.svg')
        fig.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None})
        s=p.read_text()
        s=re.sub(r'<svg\s+width="[^"]+"\s+height="[^"]+"', '<svg width="100%"',s,count=1)
        p.write_text(s)
        plt.close(fig)
        print('Wrote',p.name)

    fig, axes=plt.subplots(1,2,figsize=(10.4,5.1),gridspec_kw={'wspace':.45})
    for ax in axes:
        base(ax);ax.set_xlim(0,1);ax.set_xticks([]);ax.set_ylabel('Atomic energy / eV')
        ax.axhline(0,color=grey,ls='--',lw=1)
    ax=axes[0];ax.set_ylim(-14.7,1.6);ax.set_yticks([-14,-12,-10,-8,-6,-4,-2,0])
    ax.set_title('Hydrogen: the full depth',color=grey,pad=18)
    for n in range(1,5): ax.hlines(energy(n),.10,.9,color=blue,lw=2)
    ax.text(.12,-13.15,'n = 1   (−13.60)',fontsize=11)
    ax.text(.12,-4.35,'n = 2   (−3.40)',fontsize=11)
    ax.text(.12,.7,'0: ionisation threshold',fontsize=10)
    ax.annotate('',xy=(.7,0),xytext=(.7,energy(1)),arrowprops={'arrowstyle':'->','color':green,'lw':2})
    ax.text(.64,-8.4,'13.60 eV to escape',rotation=90,ha='center',va='center',fontsize=11)
    ax=axes[1];ax.set_ylim(-3.85,.68);ax.set_yticks([-3.5,-3,-2.5,-2,-1.5,-1,-.5,0])
    ax.set_title('Excited levels enlarged',color=grey,pad=18)
    for n in range(2,7):
        en=energy(n);ax.hlines(en,.06,.55,color=blue,lw=2)
        ax.text(.60,en,f'n = {n}   {en:.3f}',va='center',fontsize=10)
    ax.text(.06,.31,'0: levels accumulate here',fontsize=10)
    ax.annotate('',xy=(.27,energy(2)),xytext=(.27,energy(3)),arrowprops={'arrowstyle':'->','color':purple,'lw':2})
    ax.text(.33,-2.45,'3 to 2',fontsize=11,va='center')
    fig.text(.50,-.01,'Horizontal positions are for layout; vertical positions carry the energy.',ha='center',color=grey,fontsize=11)
    save(fig,'energy-levels-hydrogen')

    # All three panels share air wavelength coordinates. Profiles are schematic.
    x=np.linspace(395,685,4500)
    centres=[410.2,434.,486.1,656.3];strengths=[.36,.48,.66,.85]
    profile=sum(a*np.exp(-.5*((x-c)/1.55)**2) for a,c in zip(strengths,centres))
    fig,axes=plt.subplots(3,1,figsize=(10.2,6.5),sharex=True,gridspec_kw={'hspace':.48})
    labels=['Continuous background','Absorption: lower state populated','Emission: upper states populated']
    vals=[np.ones_like(x),1-.76*profile,profile]
    for ax,y,label,color in zip(axes,vals,labels,[grey,purple,teal]):
        base(ax);ax.set_ylim(-.03,1.2);ax.set_yticks([0,1]);ax.set_xlim(395,685)
        ax.plot(x,y,color=color,lw=1.8);ax.fill_between(x,0,y,color=to_rgba(color,.13))
        ax.set_title(label,loc='left',fontsize=12,color=grey,pad=5)
        ax.set_ylabel('Relative\nintensity')
        for c in centres:ax.axvline(c,color=grey,alpha=.25,ls=':',lw=.8)
    for c in centres:
        axes[2].text(c,1.00,f'{c:.1f}',ha='center',fontsize=10)
    axes[-1].set_xlabel('Wavelength in air / nm (rounded laboratory line centres)')
    fig.text(.5,.01,'Illustrative profiles only: widths and strengths are invented; line centres are shared.',ha='center',color=grey,fontsize=10)
    fig.subplots_adjust(bottom=.12)
    save(fig,'energy-levels-spectra')

    fig,axes=plt.subplots(1,2,figsize=(10.2,5.0),gridspec_kw={'wspace':.3})
    for ax,title in zip(axes,['Direct route: one photon','Cascade: two photons']):
        base(ax);ax.set_xlim(0,1);ax.set_ylim(-14.7,0);ax.set_xticks([])
        ax.set_title(title,color=grey,pad=13);ax.set_ylabel('Atomic energy / eV')
        for n in (1,2,3):
            ax.hlines(energy(n),.05,.92,color=blue,lw=1.5)
            ax.text(.06,energy(n)+.22,f'n = {n}',fontsize=10)
    ax=axes[0];ax.annotate('',xy=(.53,energy(1)),xytext=(.53,energy(3)),arrowprops={'arrowstyle':'->','color':green,'lw':2.5})
    ax.text(.60,-7.4,f'{transition(3,1)[2]:.1f} nm\n{transition(3,1)[0]:.3f} eV',va='center',fontsize=11)
    ax=axes[1]
    for u,l,col in [(3,2,purple),(2,1,teal)]:
        ax.annotate('',xy=(.42,energy(l)),xytext=(.42,energy(u)),arrowprops={'arrowstyle':'->','color':col,'lw':2.5})
        ax.text(.50,(energy(u)+energy(l))/2,f'{transition(u,l)[2]:.1f} nm\n{transition(u,l)[0]:.3f} eV',va='center',fontsize=10)
    fig.text(.5,-.01,'12.089 eV = 1.889 eV + 10.200 eV.  Energy adds; wavelength does not.',ha='center',fontsize=11,color=grey)
    save(fig,'energy-levels-cascades')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upper',type=int,default=3)
    parser.add_argument('--lower',type=int,default=2)
    parser.add_argument('--charge',type=int,default=1,help='Nuclear charge Z for a ONE-ELECTRON atom/ion')
    parser.add_argument('--figures',action='store_true')
    args=parser.parse_args()
    if not 1 <= args.lower < args.upper <= 10 or not 1 <= args.charge <= 10:
        parser.error('Require 1 <= lower < upper <= 10 and 1 <= charge <= 10.')
    verify()
    gap,freq,lam=transition(args.upper,args.lower,args.charge)
    print(f'\nOne electron; Z={args.charge}; n={args.upper} → {args.lower}')
    print(f'Gap {gap:.6f} eV; frequency {freq:.6e} Hz; vacuum wavelength {lam:.3f} nm')
    print('\nAll downward pairs up to the upper level (not a brightness prediction):')
    for lower,upper in combinations(range(1,args.upper+1),2):
        gap,freq,lam=transition(upper,lower,args.charge)
        print(f'  {upper} → {lower}: {gap:9.5f} eV; {lam:9.3f} nm')
    paths=list(routes(args.upper))
    print(f'\n{len(paths)} possible descending routes to n=1, ignoring selection rules:')
    for path in paths[:16]:
        print('  '+' → '.join(map(str,path))+f'  ({len(path)-1} photons)')
    if len(paths)>16:print('  … remaining routes checked, not printed.')
    print(f'Balmer series limit (H, rounded model): {HC/3.4:.3f} nm')
    print(f'Caesium clock gap: {H*9192631770/EV:.6e} eV')
    if args.figures:figures()


if __name__=='__main__':main()

"""Reproduce AP Physics 2 (2019 Q3) data fit and illustrative heat models.
Run directly for numerical checks; --figure regenerates the adjacent SVG.
"""
from pathlib import Path
import sys
import numpy as np
SIGMA=5.670374419e-8
L=np.array([.010,.020,.030,.040,.050]);P=np.array([97.,53.,31.,27.,18.])
def fit():return np.polyfit(1/L,P,1)
def wall(area=10.,delta=20.):
    resistances=np.array([.10/.60,.050/.040])/area
    power=delta/resistances.sum()
    return power,power*resistances

def insulated_rod(initial,ratio=.4,steps=200):
    if not 0<=ratio<=.5:raise ValueError('Explicit update requires 0 <= alpha*dt/dx**2 <= 0.5')
    u=np.array(initial,dtype=float,copy=True)
    if u.ndim!=1 or len(u)<2:raise ValueError('Use at least two cells')
    history=[u.copy()]
    for _ in range(steps):
        # Finite-volume fluxes: no flux through either end face.
        flux=ratio*np.diff(u)
        change=np.zeros_like(u);change[:-1]+=flux;change[1:]-=flux
        u+=change;history.append(u.copy())
    return np.array(history)

def checks():
    slope,intercept=fit();k=slope/(.025*100)
    print(f'AP fit slope={slope:.8f} W m; intercept={intercept:.8f} W; k={k:.8f} W/(m K)')
    assert .38<k<.41
    power,drops=wall();assert np.isclose(power,2400/17) and np.isclose(sum(drops),20)
    print('Wall:',power,'W; drops',drops,'K')
    print('Effective planet temperature:',((1-.3)*1360/(4*SIGMA))**.25,'K')
    rng=np.random.default_rng(1709)
    for n in (5,21,101):
        u=rng.uniform(10,90,n);hist=insulated_rod(u)
        assert np.allclose(hist.sum(axis=1),u.sum())
        assert hist.min()>=u.min()-1e-12 and hist.max()<=u.max()+1e-12
        assert np.all(np.diff(hist.var(axis=1))<=1e-10)
    assert np.allclose(insulated_rod([20]*8),20)
    try:insulated_rod([0,1,0],.51)
    except ValueError:pass
    else:raise AssertionError('unstable update accepted')
    print('Three rod grids: energy, bounds and smoothing pass; uniform state and stability guard pass.')

def figure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size':12,'text.color':'#888888','axes.labelcolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','axes.edgecolor':'#888888','svg.fonttype':'none'})
    fig,ax=plt.subplots(figsize=(8,4.5),layout='constrained');fig.patch.set_alpha(0);ax.patch.set_alpha(0)
    m,b=fit();x=np.linspace(0,105,200)
    ax.plot(x,m*x+b,color='#7c3aed',label='Least-squares fit (free intercept)')
    ax.scatter(1/L,P,color='#2563eb',s=45,label='AP Physics 2, 2019 Q3',zorder=3)
    ax.set(xlabel='Reciprocal thickness 1/L / m⁻¹',ylabel='Energy transfer rate / W',xlim=(0,110),ylim=(0,110),title='The straight-line variable is 1/L')
    ax.grid(alpha=.18);ax.legend(frameon=False,labelcolor='#888888',loc='upper left')
    p=Path(__file__).with_name('heat-transfer-conductivity.svg');fig.savefig(p,transparent=True)
    s=p.read_text();import re
    s=re.sub(r'<svg([^>]*?)width="[^"]+"([^>]*?)height="[^"]+"',r'<svg\1width="100%"\2',s,count=1);p.write_text(s)
if __name__=='__main__':
    checks()
    if '--figure' in sys.argv:figure()

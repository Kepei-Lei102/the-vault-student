#!/usr/bin/env python3
"""A model boundary you can measure. Standard library; --figures needs matplotlib.
All values are simulated ideal-pendulum predictions, not experimental observations.
Run: python3 model-breaks-lab.py [--figures]
"""
import argparse
import math
from pathlib import Path

G, LENGTH = 9.81, 1.0
T0 = 2 * math.pi * math.sqrt(LENGTH / G)


def period(angle_degrees, panels=4096):
    """Energy-integral period of a frictionless point-mass pendulum.
    Midpoint quadrature after sin(theta/2)=sin(A/2)*sin(phi) removes
    the turning-point singularity. Valid for 0 <= amplitude < 180 degrees.
    """
    if not 0 <= angle_degrees < 180 or panels < 1:
        raise ValueError('Use 0 <= angle < 180 and a positive panel count')
    k = math.sin(math.radians(angle_degrees) / 2)
    h = math.pi / (2 * panels)
    integral = h * sum(1 / math.sqrt(1 - k*k * math.sin((j+.5)*h)**2)
                       for j in range(panels))
    return 4 * math.sqrt(LENGTH / G) * integral


def boundary(tolerance=.01):
    """Largest amplitude with (T_full-T0)/T_full <= tolerance."""
    lo, hi = 0., 170.
    for _ in range(40):
        mid = (lo + hi) / 2
        if (period(mid) - T0) / period(mid) < tolerance:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def figures():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import re
    plt.rcParams.update({'svg.hashsalt':'vault', 'svg.fonttype':'none',
                         'font.size':12, 'text.color':'#888888',
                         'axes.labelcolor':'#888888', 'axes.edgecolor':'#888888',
                         'xtick.color':'#888888', 'ytick.color':'#888888'})
    angles = list(range(0, 121))
    full = [period(a) for a in angles]
    fitted = period(60)
    fig, axes = plt.subplots(2, 1, figsize=(9, 8), layout='constrained')
    ax = axes[0]
    ax.plot(angles, full, color='#7c3aed', lw=2.5, label='Full ideal pendulum')
    ax.axhline(T0, color='#2563eb', lw=2, label='Small-angle model: L = 1 m')
    ax.axhline(fitted, color='#dc2626', ls='--', lw=2,
               label='Small-angle model: L fitted at 60°')
    ax.scatter([60], [fitted], color='#dc2626', zorder=4)
    ax.set(title='One successful fit can conceal the wrong relationship',
           ylabel='Period / s', xlim=(0,120), ylim=(1.9,2.85))
    ax.legend(frameon=False, labelcolor='#888888', loc='upper left', fontsize=11)
    ax = axes[1]
    error = [100*(v-T0)/v for v in full]
    ax.plot(angles, error, color='#dc2626', lw=2.5)
    ax.axhline(1, color='#059669', ls='--', lw=2, label='Chosen tolerance: 1%')
    edge = boundary()
    ax.axvline(edge, color='#888888', ls=':', lw=1.5)
    ax.annotate(f'1% boundary ≈ {edge:.1f}°', (edge,1), xytext=(38,11),
                arrowprops={'arrowstyle':'->','color':'#888888'}, color='#888888')
    ax.set(title='Validity depends on the task and its error budget',
           xlabel='Release amplitude / degrees', ylabel='Period error / %',
           xlim=(0,120), ylim=(-.8,28.5))
    ax.legend(frameon=False, labelcolor='#888888', loc='upper left')
    for ax in axes:
        ax.set_facecolor('none')
        ax.spines[['top','right']].set_visible(False)
        ax.grid(color='#888888', alpha=.15)
        ax.title.set_color('#888888')
    target = Path(__file__).with_name('model-breaks-pendulum.svg')
    fig.savefig(target, transparent=True, metadata={'Date':None})
    plt.close(fig)
    svg = target.read_text()
    svg = re.sub(r'width="[^"]+" height="[^"]+"', 'width="100%"', svg, count=1)
    target.write_text("\n".join(line.rstrip() for line in svg.splitlines()) + "\n")
    print('Wrote', target.name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--figures', action='store_true')
    args = parser.parse_args()
    print(f'Small-angle period: {T0:.6f} s')
    print('Amplitude   Full period   T0 shortfall relative to full period')
    for a in [5, 15, 30, 60, 90, 120]:
        t = period(a)
        print(f'{a:3d} deg     {t:.6f} s     {100*(t-T0)/t:.4f}%')
    print(f'1% period-error boundary: {boundary():.4f} degrees')
    print(f'Length inferred from the 60-degree period using T0: '
          f'{G*(period(60)/(2*math.pi))**2:.6f} m')
    # Verify the numerical method, not the physical adequacy of the model.
    discrepancy = max(abs(period(a,2048)-period(a,4096)) for a in [5,60,120])
    assert discrepancy < 1e-10
    assert abs(period(0)-T0) < 1e-12
    print(f'Quadrature refinement difference: {discrepancy:.3g} s')
    if args.figures:
        figures()

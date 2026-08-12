"""Two-panel SVG for the Information Theory vault card.

LEFT  — surprise function I(p) = -log_2(p) for p in (0, 1].
RIGHT — binary entropy H(p) = -p log_2 p - (1-p) log_2 (1-p) for p in [0, 1].

Vault palette, transparent background, theme-compatible strokes.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

COLORS = {
    'axes': '#888888',
    'primary': '#cc0066',
    'secondary': '#4678c8',
    'amber': '#f59e0b',
    'green': '#059669',
    'grid': '#888888',
    'text': '#888888',
}

VAULT = '/sessions/kind-exciting-feynman/mnt/The_Vault/CS/Foundations'
TMP = '/tmp'


def make_svg():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    fig.patch.set_alpha(0)

    # ---------- LEFT : surprise I(p) = -log_2 p --------------------
    ax = axes[0]
    ax.set_facecolor('none')

    p = np.linspace(0.001, 1.0, 1000)
    I = -np.log2(p)
    ax.plot(p, I, color=COLORS['primary'], linewidth=2.5,
            label=r'$I(p) = -\log_2 p$')

    # Annotate three reference points
    for pp, lbl in [(1.0, '$p = 1$\n$I = 0$ bits\n(certain)'),
                     (0.5, '$p = 1/2$\n$I = 1$ bit'),
                     (0.125, '$p = 1/8$\n$I = 3$ bits')]:
        Ip = -np.log2(pp)
        ax.plot([pp], [Ip], 'o', color=COLORS['amber'], markersize=7)
        # Position label depending on where the point is
        if pp == 1.0:
            xytext = (0.6, 1.2)
        elif pp == 0.5:
            xytext = (0.55, 2.2)
        else:
            xytext = (0.22, 4.5)
        ax.annotate(lbl, xy=(pp, Ip), xytext=xytext,
                    fontsize=9.5, color=COLORS['text'],
                    ha='left', va='center',
                    arrowprops=dict(arrowstyle='->',
                                    color=COLORS['amber'], lw=1.0))

    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 7.5)
    ax.set_xlabel('Probability  $p$', color=COLORS['text'], fontsize=11)
    ax.set_ylabel('Information  $I(p)$  (bits)',
                  color=COLORS['text'], fontsize=11)
    ax.set_title('Surprise of a single event — $I(p) = -\\log_2 p$',
                 color=COLORS['text'], fontsize=12, pad=10)

    ax.spines['bottom'].set_color(COLORS['axes'])
    ax.spines['left'].set_color(COLORS['axes'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(colors=COLORS['axes'])
    ax.grid(True, alpha=0.15, color=COLORS['grid'])

    # ---------- RIGHT : binary entropy H(p) ------------------------
    ax2 = axes[1]
    ax2.set_facecolor('none')

    p2 = np.linspace(0.0001, 0.9999, 1000)
    H = -p2 * np.log2(p2) - (1 - p2) * np.log2(1 - p2)
    ax2.plot(p2, H, color=COLORS['secondary'], linewidth=2.5,
             label=r'$h(p) = -p \log_2 p - (1-p)\log_2(1-p)$')

    # Peak at p = 0.5
    peak_p = 0.5
    peak_H = 1.0
    ax2.plot([peak_p], [peak_H], 'o', color=COLORS['amber'], markersize=8)
    ax2.axvline(peak_p, color=COLORS['amber'], linestyle='--',
                linewidth=1.0, alpha=0.5)
    ax2.axhline(peak_H, color=COLORS['amber'], linestyle='--',
                linewidth=1.0, alpha=0.5)
    ax2.annotate('Max entropy\n$h(1/2) = 1$ bit\n(fair coin)',
                 xy=(peak_p, peak_H),
                 xytext=(0.18, 0.78),
                 fontsize=9.5, color=COLORS['text'],
                 ha='left', va='center',
                 arrowprops=dict(arrowstyle='->',
                                 color=COLORS['amber'], lw=1.0))

    # Endpoints — certainty
    ax2.plot([0.0, 1.0], [0.0, 0.0], 'o', color=COLORS['green'],
             markersize=6)
    ax2.annotate('$h(0) = 0$\n(always tails)', xy=(0.0, 0.0),
                 xytext=(0.02, 0.15),
                 fontsize=9, color=COLORS['text'],
                 ha='left', va='center',
                 arrowprops=dict(arrowstyle='->',
                                 color=COLORS['green'], lw=0.9))
    ax2.annotate('$h(1) = 0$\n(always heads)', xy=(1.0, 0.0),
                 xytext=(0.62, 0.15),
                 fontsize=9, color=COLORS['text'],
                 ha='left', va='center',
                 arrowprops=dict(arrowstyle='->',
                                 color=COLORS['green'], lw=0.9))

    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(0, 1.15)
    ax2.set_xlabel('Probability of heads  $p$',
                   color=COLORS['text'], fontsize=11)
    ax2.set_ylabel('Binary entropy  $h(p)$  (bits)',
                   color=COLORS['text'], fontsize=11)
    ax2.set_title('Binary entropy — symmetric, peaked at $p = 1/2$',
                  color=COLORS['text'], fontsize=12, pad=10)

    ax2.spines['bottom'].set_color(COLORS['axes'])
    ax2.spines['left'].set_color(COLORS['axes'])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.tick_params(colors=COLORS['axes'])
    ax2.grid(True, alpha=0.15, color=COLORS['grid'])

    fig.subplots_adjust(wspace=0.30)

    out_svg = f'{VAULT}/information-theory-surprise-and-entropy.svg'
    out_png = f'{TMP}/information-theory-surprise-and-entropy.png'
    plt.savefig(out_svg, format='svg', transparent=True,
                bbox_inches='tight')
    plt.savefig(out_png, format='png', transparent=True,
                bbox_inches='tight', dpi=150)
    plt.close()
    return out_svg, out_png


if __name__ == '__main__':
    s, p = make_svg()
    print(f'svg → {s}')
    print(f'png → {p}')

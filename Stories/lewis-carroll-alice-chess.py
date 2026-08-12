"""Alice's pawn-to-queen path through the Looking-Glass.

The front matter of Through the Looking-Glass (1871) lays out a literal
chess problem. Alice begins as the White Pawn at d2 and reaches d8 where
she is promoted to Queen — winning the game and ending it. Carroll
matched each of the eleven moves to a chapter event.

This SVG shows the 8x8 board with the d-file highlighted, the pawn at d2,
the queen at d8, and arrows marking Alice's six advance steps.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

COLORS = {
    'axes': '#888888',
    'primary': '#cc0066',
    'secondary': '#4678c8',
    'amber': '#f59e0b',
    'green': '#059669',
    'red': '#dc2626',
    'purple': '#7c3aed',
    'grid': '#888888',
    'text': '#888888',
}

VAULT = '/sessions/kind-exciting-feynman/mnt/The_Vault/Stories'
TMP = '/tmp'


def make_svg():
    fig, ax = plt.subplots(figsize=(7.5, 7.0))
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')

    # Draw the 8x8 board.  We use a "dark" tint for dark squares (transparent
    # blue) and leave light squares transparent so the Obsidian theme shows
    # through.  All squares get a thin grey outline.
    board_origin = (0, 0)
    sq = 1.0
    for r in range(8):
        for c in range(8):
            is_dark = (r + c) % 2 == 0
            facecolor = COLORS['secondary'] if is_dark else 'none'
            alpha = 0.18 if is_dark else 0
            ax.add_patch(mpatches.Rectangle(
                (c * sq, r * sq), sq, sq,
                facecolor=facecolor, alpha=alpha,
                edgecolor=COLORS['axes'], linewidth=0.8,
            ))

    # File labels (a..h) along the bottom
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for c in range(8):
        ax.text(c * sq + sq/2, -0.30, files[c],
                color=COLORS['text'], ha='center', va='center',
                fontsize=11, style='italic')
    # Rank labels (1..8) along the left
    for r in range(8):
        ax.text(-0.30, r * sq + sq/2, str(r + 1),
                color=COLORS['text'], ha='center', va='center',
                fontsize=11, style='italic')

    # Highlight the d-file (column 3) — Alice's whole journey lives on this file
    ax.add_patch(mpatches.Rectangle(
        (3 * sq, 0), sq, 8 * sq,
        facecolor=COLORS['amber'], alpha=0.10,
        edgecolor='none',
    ))

    # Alice's start at d2 (column 3, row 1).  Show a pawn glyph.
    pawn_x = 3 * sq + sq/2
    pawn_y = 1 * sq + sq/2
    ax.text(pawn_x, pawn_y, '♙',
            color=COLORS['primary'], ha='center', va='center',
            fontsize=44)
    ax.annotate('Alice\n(White Pawn)\nstarts at d2',
                xy=(pawn_x + 0.30, pawn_y),
                xytext=(5.8, 1.5),
                fontsize=10, color=COLORS['text'],
                ha='left', va='center',
                arrowprops=dict(arrowstyle='->',
                                color=COLORS['primary'], lw=1.0))

    # Alice's endpoint at d8 (column 3, row 7).  Show a queen glyph in amber
    # (the promoted piece).
    queen_x = 3 * sq + sq/2
    queen_y = 7 * sq + sq/2
    ax.text(queen_x, queen_y, '♕',
            color=COLORS['amber'], ha='center', va='center',
            fontsize=46)
    ax.annotate('d8 — pawn promoted\nto Queen.\nGame ends here.',
                xy=(queen_x + 0.30, queen_y),
                xytext=(5.8, 7.5),
                fontsize=10, color=COLORS['text'],
                ha='left', va='center',
                arrowprops=dict(arrowstyle='->',
                                color=COLORS['amber'], lw=1.0))

    # Arrows marking each advance step.  Alice's actual moves in the book:
    # d2 -> d4 (first move is a 2-square pawn advance), then d4 -> d5 ->
    # d6 -> d7 -> d8 one square at a time.  Mark each intermediate square
    # with a small grey dot and connect with an arrow.
    waypoints = [(3, 1), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)]
    for (c1, r1), (c2, r2) in zip(waypoints[:-1], waypoints[1:]):
        x1 = c1 * sq + sq/2
        y1 = r1 * sq + sq/2 + 0.32        # exit pawn from above
        x2 = c2 * sq + sq/2
        y2 = r2 * sq + sq/2 - 0.30        # enter next square from below
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->',
                                    color=COLORS['primary'],
                                    lw=1.8, alpha=0.7))

    # Chapter markers — the 6 advance squares each mark a chapter
    chapter_labels = {
        (3, 3): 'Ch. 2  (Looking-Glass garden)',
        (3, 4): 'Ch. 3  (the railway carriage)',
        (3, 5): 'Ch. 4  (Tweedledum & Tweedledee)',
        (3, 6): 'Ch. 5  (Wool & Water — the sheep shop)',
        (3, 7): 'Ch. 6  (Humpty Dumpty) — then onward to Ch. 9 coronation',
    }
    for (c, r), lbl in chapter_labels.items():
        if (c, r) == (3, 7):    # skip — it's the promotion square, labelled above
            continue
        x_lbl = c * sq + sq/2
        y_lbl = r * sq + sq/2
        ax.text(-0.45, y_lbl, lbl,
                color=COLORS['text'], ha='right', va='center',
                fontsize=8.5, alpha=0.85)

    ax.set_xlim(-3.5, 8.6)
    ax.set_ylim(-0.7, 8.4)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)

    ax.set_title("Alice's chess game in Through the Looking-Glass\n"
                 "pawn at d2 → queen at d8, six advances, eight chapters",
                 color=COLORS['text'], fontsize=12, pad=14)

    out_svg = f'{VAULT}/lewis-carroll-alice-chess.svg'
    out_png = f'{TMP}/lewis-carroll-alice-chess.png'
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

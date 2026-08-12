#!/usr/bin/env python3
# stack: SMIL  (animation toolchain — keep SMIL on future edits, do not switch to Manim)
"""
Generate searching-race-linear-vs-binary.svg — a SMIL-animated race of linear
vs binary search on the SAME sorted 16-element array, so the reader can WATCH
binary finish (~1.6 s, 4 looks) while linear is still crawling (~6.6 s, 13 looks).

Design:
  - Two rows of 16 cells, identical sorted values, target = 57 at index 12.
  - A purple "scanner" cursor jumps cell-to-cell at each comparison (discrete).
  - Examined cells light up (blue), the found cell goes green.
  - Binary's discarded halves are dimmed by grey "curtains" that grow in steps.
  - A cost meter under each row grows one cell-width per comparison; linear's bar
    keeps growing long after binary's has stopped — the time gap made physical.
  - A tally badge appears when each search finishes (binary's ~3x earlier).

Vault rules: text #888, semi-transparent rgba fills, transparent background,
width="100%", viewBox set, no dark/light hard-coded colors.

Usage:
  python3 searching-race.py            -> writes the animated SVG
  python3 searching-race.py --final    -> writes /tmp/searching-race_final.svg
                                          (static end-state, for verification)
"""
import sys

# ---- data ------------------------------------------------------------------
VALUES = [3, 7, 12, 18, 21, 26, 30, 34, 39, 45, 48, 52, 57, 61, 66, 70]
TARGET = 57
TARGET_IDX = VALUES.index(TARGET)          # 12
N = len(VALUES)                             # 16
LINEAR_SEQ = list(range(TARGET_IDX + 1))   # [0..12] -> 13 comparisons

def binary_mids(a, t):
    lo, hi, mids = 0, len(a) - 1, []
    while lo <= hi:
        m = lo + (hi - lo) // 2
        mids.append(m)
        if a[m] == t:
            return mids
        elif a[m] < t:
            lo = m + 1
        else:
            hi = m - 1
    return mids
BIN_SEQ = binary_mids(VALUES, TARGET)      # [7, 11, 13, 12] -> 4 comparisons

# ---- timing ----------------------------------------------------------------
TICK = 0.55
HOLD = 2.0
# Event timing: t=0 is a clean "ready" frame (nothing examined). Comparison k
# (0-based) COMPLETES — cell lights, meter ticks — at (k+1)*TICK. The cursor
# ARRIVES on the cell being examined one tick earlier, at k*TICK.
def fill_t(k):
    return (k + 1) * TICK
LIN_DONE = len(LINEAR_SEQ) * TICK            # 13*0.55 = 7.15
CYCLE = LIN_DONE + HOLD                       # 9.15
def f(t):
    return round(max(0.0, min(1.0, t / CYCLE)), 5)

# ---- geometry --------------------------------------------------------------
X0, PITCH, CW, CH = 12, 44, 40, 40
def cx(i):
    return X0 + i * PITCH
RIGHT = cx(N - 1) + CW                       # 712
VBW = RIGHT + 12                             # 724
LIN_LBL_Y, LIN_CELL_Y, LIN_IDX_Y, LIN_METER_Y = 44, 52, 106, 116
BIN_LBL_Y, BIN_CELL_Y, BIN_IDX_Y, BIN_METER_Y = 158, 166, 220, 230
CAP_Y1, CAP_Y2, VBH, METER_H = 260, 280, 292, 12
BLUE, GREEN, PURPLE, AMBER = "#2563eb", "#059669", "#7c3aed", "#f59e0b"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def kt_str(ts):
    return ";".join(str(round(k, 5)) for k in ts)

# ---- builders --------------------------------------------------------------
def cell_base(i, y, idx_y):
    return (f'<rect x="{cx(i)}" y="{y}" width="{CW}" height="{CH}" rx="5" '
            f'fill="rgba(136,136,136,0.06)" stroke="#888" stroke-width="1.2"/>\n'
            f'<text x="{cx(i)+CW//2}" y="{y+CH//2+5}" text-anchor="middle" class="val">{VALUES[i]}</text>\n'
            f'<text x="{cx(i)+CW//2}" y="{idx_y}" text-anchor="middle" class="idx">{i}</text>')

def reveal_overlay(i, y, rgb, alpha, t, final):
    base = (f'<rect x="{cx(i)}" y="{y}" width="{CW}" height="{CH}" rx="5" '
            f'fill="rgba({rgb},{alpha})" stroke="rgb({rgb})" stroke-width="2" ')
    if final:
        return base + 'opacity="1"/>'
    kt = f(t)
    return (base + 'opacity="0"><animate attributeName="opacity" '
            f'dur="{CYCLE}s" repeatCount="indefinite" keyTimes="0;{kt};{kt};1" '
            f'values="0;0;1;1" calcMode="discrete"/></rect>')

def bright_value(i, y, t, final):
    txt = (f'<text x="{cx(i)+CW//2}" y="{y+CH//2+5}" text-anchor="middle" class="val">'
           f'{VALUES[i]}')
    if final:
        return txt + '</text>'
    kt = f(t)
    return (txt + f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite" '
            f'keyTimes="0;{kt};{kt};1" values="0;0;1;1" calcMode="discrete"/></text>')

def curtain(x, w, t, final):
    y, h = BIN_CELL_Y - 3, CH + 6
    base = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" '
            f'fill="rgba(136,136,136,0.34)" ')
    if final:
        return base + 'opacity="1"/>'
    kt = f(t)
    return (base + 'opacity="0"><animate attributeName="opacity" '
            f'dur="{CYCLE}s" repeatCount="indefinite" keyTimes="0;{kt};{kt};1" '
            f'values="0;0;1;1" calcMode="discrete"/></rect>')

def scanner(seq, y, final):
    box = (f'<rect y="{y-3}" width="{CW+6}" height="{CH+6}" rx="6" fill="none" '
           f'stroke="{PURPLE}" stroke-width="3" ')
    if final:
        return box + f'x="{cx(seq[-1])-3}"/>'
    xs = [cx(i) - 3 for i in seq]
    times = [f(k * TICK) for k in range(len(seq))] + [1.0]
    vals = [f"{x},0" for x in xs] + [f"{xs[-1]},0"]
    return (box + f'x="-3" transform="translate({xs[0]},0)">'
            f'<animateTransform attributeName="transform" type="translate" calcMode="discrete" '
            f'dur="{CYCLE}s" repeatCount="indefinite" keyTimes="{kt_str(times)}" '
            f'values="{";".join(vals)}"/></rect>')

def meter(x, ncomp, rgb, y, final):
    track = (f'<rect x="{x}" y="{y}" width="{ncomp*PITCH}" height="{METER_H}" rx="3" '
             f'fill="rgba(136,136,136,0.10)" stroke="#888" stroke-width="0.8"/>')
    base = (f'<rect x="{x}" y="{y}" height="{METER_H}" rx="3" '
            f'fill="rgba({rgb},0.30)" stroke="rgb({rgb})" stroke-width="1" ')
    if final:
        return track + "\n" + base + f'width="{ncomp*PITCH}"/>'
    # width 0 at t=0, then +PITCH each time comparison k completes (fill_t(k))
    times = [0.0] + [f(fill_t(k)) for k in range(ncomp)] + [1.0]
    vals = ["0"] + [str((k + 1) * PITCH) for k in range(ncomp)] + [str(ncomp * PITCH)]
    bar = (base + 'width="0"><animate attributeName="width" calcMode="discrete" '
           f'dur="{CYCLE}s" repeatCount="indefinite" keyTimes="{kt_str(times)}" '
           f'values="{";".join(vals)}"/></rect>')
    return track + "\n" + bar

def tally(x, y, text, color, t, final):
    el = f'<text x="{x}" y="{y}" text-anchor="end" class="tally" fill="{color}" '
    if final:
        return el + f'opacity="1">{esc(text)}</text>'
    kt = f(t)
    return (el + f'opacity="0">{esc(text)}'
            f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite" '
            f'keyTimes="0;{kt};{kt};1" values="0;0;1;1" calcMode="discrete"/></text>')

# ---- assemble --------------------------------------------------------------
def build(final=False):
    P = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VBW} {VBH}" width="100%">',
         '<!-- stack: SMIL -->',
         '''<style>
  text { font-family: system-ui, -apple-system, sans-serif; fill: #888; }
  .val { font-size: 15px; }
  .idx { font-size: 10px; opacity: 0.55; }
  .row { font-size: 14px; font-weight: 600; }
  .tally { font-size: 13px; font-weight: 600; }
  .cap { font-size: 12.5px; }
  .target { font-size: 14px; font-weight: 600; }
</style>''']

    P.append(f'<text x="{VBW//2}" y="22" text-anchor="middle" class="target">'
             f'searching a sorted list for target = {TARGET} — it lives at index {TARGET_IDX}</text>')

    # LINEAR
    P.append(f'<text x="{X0}" y="{LIN_LBL_Y}" class="row">Linear search'
             f'<tspan class="cap" font-weight="400"> — check every cell in turn</tspan></text>')
    for i in range(N):
        P.append(cell_base(i, LIN_CELL_Y, LIN_IDX_Y))
    for k, i in enumerate(LINEAR_SEQ):
        rgb, a = ("5,150,105", 0.30) if i == TARGET_IDX else ("37,99,235", 0.20)
        P.append(reveal_overlay(i, LIN_CELL_Y, rgb, a, fill_t(k), final))
    P.append(scanner(LINEAR_SEQ, LIN_CELL_Y, final))
    P.append(meter(X0, len(LINEAR_SEQ), "245,158,11", LIN_METER_Y, final))
    P.append(tally(RIGHT, LIN_LBL_Y, "13 comparisons", AMBER, fill_t(len(LINEAR_SEQ) - 1), final))

    # BINARY
    P.append(f'<text x="{X0}" y="{BIN_LBL_Y}" class="row">Binary search'
             f'<tspan class="cap" font-weight="400"> — halve the window each look (needs sorted data)</tspan></text>')
    for i in range(N):
        P.append(cell_base(i, BIN_CELL_Y, BIN_IDX_Y))
    P.append(curtain(cx(0), cx(8) - cx(0), 1 * TICK, final))     # discard 0..7
    P.append(curtain(cx(0), cx(12) - cx(0), 2 * TICK, final))    # discard 0..11
    P.append(curtain(cx(13), RIGHT - cx(13), 3 * TICK, final))   # discard 13..15
    for k, i in enumerate(BIN_SEQ):
        rgb, a = ("5,150,105", 0.32) if i == TARGET_IDX else ("37,99,235", 0.22)
        P.append(reveal_overlay(i, BIN_CELL_Y, rgb, a, fill_t(k), final))
        P.append(bright_value(i, BIN_CELL_Y, fill_t(k), final))
    P.append(scanner(BIN_SEQ, BIN_CELL_Y, final))
    P.append(meter(X0, len(BIN_SEQ), "5,150,105", BIN_METER_Y, final))
    P.append(tally(RIGHT, BIN_LBL_Y, "✓ 4 comparisons", GREEN, fill_t(len(BIN_SEQ) - 1), final))

    # caption
    P.append(f'<text x="{VBW//2}" y="{CAP_Y1}" text-anchor="middle" class="cap">'
             f'Same time per look — but binary finishes in 4 looks while linear grinds on to 13.</text>')
    P.append(f'<text x="{VBW//2}" y="{CAP_Y2}" text-anchor="middle" class="cap">'
             f'Double the list: linear doubles its work; binary adds just one more look.</text>')

    P.append('</svg>')
    return "\n".join(P)

if __name__ == "__main__":
    if "--final" in sys.argv:
        open("/tmp/searching-race_final.svg", "w").write(build(final=True))
        print("wrote /tmp/searching-race_final.svg")
    else:
        out = "searching-race-linear-vs-binary.svg"
        open(out, "w").write(build(final=False))
        print(f"wrote {out}  (cycle={CYCLE}s, linear {len(LINEAR_SEQ)} vs binary {len(BIN_SEQ)})")
        print(f"binary mids = {BIN_SEQ}")

"""
Generate shm-live-quantities.svg — a SMIL-animated SHM visualization.

Left panel:  a mass oscillating on a horizontal track between -A and +A.
Right panel: live bars showing x, a, KE, PE (plus a static A reference).

The animation loops every 4 seconds with 48 keyframes for smoothness.
"""
import numpy as np
from pathlib import Path

# === Animation parameters ===
DUR_S = 4.0
N_FRAMES = 48
A_DISPLAY = 90  # half-track width in pixels for x; everything else scales to fit
SCRIPT_DIR = Path(__file__).resolve().parent
SVG_PATH = SCRIPT_DIR / "shm-live-quantities.svg"

# === Compute keyframe values ===
omega = 2 * np.pi / DUR_S
t = np.linspace(0, DUR_S, N_FRAMES + 1)  # 0..T inclusive
key_times = ";".join(f"{ti / DUR_S:.4f}" for ti in t)

# Phase
theta = omega * t

# Physical values (display units)
x_val = np.cos(theta)               # in [-1, +1]
a_val = -np.cos(theta)              # opposite sign to x; magnitude same
ke_frac = np.sin(theta) ** 2        # in [0, 1]
pe_frac = np.cos(theta) ** 2        # in [0, 1]


def vals(seq, fmt="{:.3f}"):
    return ";".join(fmt.format(v) for v in seq)


# === Layout constants ===
W, H = 880, 520
LEFT_CX = 220       # centre of oscillation track
LEFT_TRACK_Y = 280
LEFT_TRACK_HALF = A_DISPLAY  # so endpoints are LEFT_CX ± 90
MASS_SIZE = 28
MASS_Y = LEFT_TRACK_Y - MASS_SIZE / 2

# Right panel: bars
RIGHT_X0 = 470       # left edge of bars
BAR_HEIGHT = 22
BAR_GAP = 56         # vertical spacing between bar rows
BAR_MAX = 280        # max width of a bar (pixels)
LABEL_X = RIGHT_X0 - 10
VAL_X = RIGHT_X0 + BAR_MAX + 12

# y centres for each row
ROW_A  = 130
ROW_X  = ROW_A + BAR_GAP
ROW_AC = ROW_X + BAR_GAP        # acceleration
ROW_KE = ROW_AC + BAR_GAP
ROW_PE = ROW_KE + BAR_GAP

# === Compute SMIL value strings ===

# Mass position (x attribute of the mass rect)
mass_x_vals = LEFT_CX + A_DISPLAY * x_val - MASS_SIZE / 2

# Bipolar bar values for x: rect anchored at centre, expanding left/right.
# We animate rect_x and width. centre of bipolar bar:
cx_x_bar = RIGHT_X0 + BAR_MAX / 2
half = BAR_MAX / 2
# scaled x in [-half, +half]:
x_scaled = half * x_val
# rect_x = cx + min(x_scaled, 0); width = |x_scaled|
xbar_rect_x = cx_x_bar + np.minimum(x_scaled, 0)
xbar_rect_w = np.abs(x_scaled)

# Bipolar bar for a (opposite sign of x)
a_scaled = half * a_val
abar_rect_x = cx_x_bar + np.minimum(a_scaled, 0)
abar_rect_w = np.abs(a_scaled)

# Unipolar bars for KE and PE (grow from left)
ke_width = BAR_MAX * ke_frac
pe_width = BAR_MAX * pe_frac

# === Build SVG ===

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%">
  <style>
    text {{ font-family: system-ui, -apple-system, sans-serif; fill: #888; }}
    .math {{ font-family: 'Times New Roman', serif; font-style: italic; }}
    .title {{ font-size: 16px; font-weight: 600; }}
    .panel-h {{ font-size: 13px; font-weight: 600; opacity: 0.95; }}
    .label {{ font-size: 13px; }}
    .small {{ font-size: 11px; opacity: 0.85; }}
    .formula {{ font-size: 11px; opacity: 0.75; }}
    .x-c {{ fill: #2563eb; }}
    .a-c {{ fill: #f59e0b; }}
    .ke-c {{ fill: #059669; }}
    .pe-c {{ fill: #7c3aed; }}
    .ref-c {{ fill: #888; }}
  </style>

  <!-- Title -->
  <text x="{W/2}" y="28" class="title" text-anchor="middle">Live SHM — oscillation and its real-time quantities</text>
  <text x="{W/2}" y="48" class="small" text-anchor="middle">
    Period <tspan class="math">T = {DUR_S:.0f} s</tspan>. Watch <tspan class="math ke-c">KE</tspan> and <tspan class="math pe-c">PE</tspan> exchange while <tspan class="math ref-c">A</tspan> stays put.
  </text>

  <!-- ===================== LEFT PANEL ===================== -->
  <text x="{LEFT_CX}" y="100" class="panel-h" text-anchor="middle">Oscillator</text>

  <!-- Track line -->
  <line x1="{LEFT_CX - LEFT_TRACK_HALF - 20}" y1="{LEFT_TRACK_Y}"
        x2="{LEFT_CX + LEFT_TRACK_HALF + 20}" y2="{LEFT_TRACK_Y}"
        stroke="#888" stroke-width="1.5"/>

  <!-- End marks: -A and +A -->
  <line x1="{LEFT_CX - LEFT_TRACK_HALF}" y1="{LEFT_TRACK_Y - 14}"
        x2="{LEFT_CX - LEFT_TRACK_HALF}" y2="{LEFT_TRACK_Y + 14}"
        stroke="#888" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>
  <line x1="{LEFT_CX + LEFT_TRACK_HALF}" y1="{LEFT_TRACK_Y - 14}"
        x2="{LEFT_CX + LEFT_TRACK_HALF}" y2="{LEFT_TRACK_Y + 14}"
        stroke="#888" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>

  <!-- Equilibrium tick -->
  <line x1="{LEFT_CX}" y1="{LEFT_TRACK_Y - 8}"
        x2="{LEFT_CX}" y2="{LEFT_TRACK_Y + 8}"
        stroke="#888" stroke-width="1.2" opacity="0.7"/>

  <!-- Position labels -->
  <text x="{LEFT_CX - LEFT_TRACK_HALF}" y="{LEFT_TRACK_Y + 36}" class="math label" text-anchor="middle">−A</text>
  <text x="{LEFT_CX}" y="{LEFT_TRACK_Y + 36}" class="math label" text-anchor="middle">0</text>
  <text x="{LEFT_CX + LEFT_TRACK_HALF}" y="{LEFT_TRACK_Y + 36}" class="math label" text-anchor="middle">+A</text>

  <!-- Mass (animated) -->
  <rect width="{MASS_SIZE}" height="{MASS_SIZE}" y="{MASS_Y}"
        fill="rgba(37, 99, 235, 0.7)" stroke="#2563eb" stroke-width="2" rx="4">
    <animate attributeName="x"
             values="{vals(mass_x_vals)}"
             keyTimes="{key_times}"
             dur="{DUR_S}s" repeatCount="indefinite"/>
  </rect>

  <!-- A static "spring" suggestion: zigzag from left wall to the mass — visual flair (optional, skipped for clarity) -->

  <!-- Phase indicator below the track -->
  <text x="{LEFT_CX}" y="{LEFT_TRACK_Y + 70}" class="small" text-anchor="middle">
    <tspan class="math x-c">x(t) = A cos(ωt)</tspan>
  </text>
  <text x="{LEFT_CX}" y="{LEFT_TRACK_Y + 92}" class="small" text-anchor="middle" opacity="0.7">
    one full period loops every <tspan class="math">T = {DUR_S:.0f} s</tspan>
  </text>

  <!-- Divider -->
  <line x1="430" y1="80" x2="430" y2="{H - 40}" stroke="#888" stroke-width="0.6" opacity="0.35"/>

  <!-- ===================== RIGHT PANEL ===================== -->
  <text x="{RIGHT_X0 + BAR_MAX / 2}" y="100" class="panel-h" text-anchor="middle">Live quantities</text>

  <!-- ===== A reference (static) ===== -->
  <text x="{LABEL_X}" y="{ROW_A + 5}" class="math label ref-c" text-anchor="end">A</text>
  <rect x="{RIGHT_X0}" y="{ROW_A - BAR_HEIGHT/2}" width="{BAR_MAX}" height="{BAR_HEIGHT}"
        fill="rgba(136, 136, 136, 0.18)" stroke="#888" stroke-width="1.2"/>
  <text x="{VAL_X}" y="{ROW_A + 5}" class="math small ref-c">amplitude (constant)</text>
  <text x="{LABEL_X}" y="{ROW_A + 24}" class="formula" text-anchor="end" opacity="0.6">always full</text>

  <!-- ===== x (bipolar) ===== -->
  <text x="{LABEL_X}" y="{ROW_X + 5}" class="math label x-c" text-anchor="end">x</text>
  <!-- bipolar track outline -->
  <rect x="{RIGHT_X0}" y="{ROW_X - BAR_HEIGHT/2}" width="{BAR_MAX}" height="{BAR_HEIGHT}"
        fill="none" stroke="#888" stroke-width="0.6" stroke-dasharray="2,3" opacity="0.45"/>
  <!-- centre line -->
  <line x1="{cx_x_bar}" y1="{ROW_X - BAR_HEIGHT/2 - 3}"
        x2="{cx_x_bar}" y2="{ROW_X + BAR_HEIGHT/2 + 3}"
        stroke="#888" stroke-width="1"/>
  <!-- animated bar -->
  <rect y="{ROW_X - BAR_HEIGHT/2}" height="{BAR_HEIGHT}"
        fill="rgba(37, 99, 235, 0.55)" stroke="#2563eb" stroke-width="1.5">
    <animate attributeName="x" values="{vals(xbar_rect_x)}" keyTimes="{key_times}"
             dur="{DUR_S}s" repeatCount="indefinite"/>
    <animate attributeName="width" values="{vals(xbar_rect_w)}" keyTimes="{key_times}"
             dur="{DUR_S}s" repeatCount="indefinite"/>
  </rect>
  <text x="{VAL_X}" y="{ROW_X + 5}" class="math small x-c">A cos(ωt)</text>
  <text x="{LABEL_X}" y="{ROW_X + 24}" class="formula x-c" text-anchor="end" opacity="0.7">displacement</text>

  <!-- ===== a (bipolar, opposite) ===== -->
  <text x="{LABEL_X}" y="{ROW_AC + 5}" class="math label a-c" text-anchor="end">a</text>
  <rect x="{RIGHT_X0}" y="{ROW_AC - BAR_HEIGHT/2}" width="{BAR_MAX}" height="{BAR_HEIGHT}"
        fill="none" stroke="#888" stroke-width="0.6" stroke-dasharray="2,3" opacity="0.45"/>
  <line x1="{cx_x_bar}" y1="{ROW_AC - BAR_HEIGHT/2 - 3}"
        x2="{cx_x_bar}" y2="{ROW_AC + BAR_HEIGHT/2 + 3}"
        stroke="#888" stroke-width="1"/>
  <rect y="{ROW_AC - BAR_HEIGHT/2}" height="{BAR_HEIGHT}"
        fill="rgba(245, 158, 11, 0.55)" stroke="#f59e0b" stroke-width="1.5">
    <animate attributeName="x" values="{vals(abar_rect_x)}" keyTimes="{key_times}"
             dur="{DUR_S}s" repeatCount="indefinite"/>
    <animate attributeName="width" values="{vals(abar_rect_w)}" keyTimes="{key_times}"
             dur="{DUR_S}s" repeatCount="indefinite"/>
  </rect>
  <text x="{VAL_X}" y="{ROW_AC + 5}" class="math small a-c">−ω²·A cos(ωt)</text>
  <text x="{LABEL_X}" y="{ROW_AC + 24}" class="formula a-c" text-anchor="end" opacity="0.7">acceleration (opposite sign)</text>

  <!-- ===== KE (unipolar, grows from left) ===== -->
  <text x="{LABEL_X}" y="{ROW_KE + 5}" class="math label ke-c" text-anchor="end">KE</text>
  <rect x="{RIGHT_X0}" y="{ROW_KE - BAR_HEIGHT/2}" width="{BAR_MAX}" height="{BAR_HEIGHT}"
        fill="none" stroke="#888" stroke-width="0.6" stroke-dasharray="2,3" opacity="0.45"/>
  <rect x="{RIGHT_X0}" y="{ROW_KE - BAR_HEIGHT/2}" height="{BAR_HEIGHT}"
        fill="rgba(5, 150, 105, 0.55)" stroke="#059669" stroke-width="1.5">
    <animate attributeName="width" values="{vals(ke_width)}" keyTimes="{key_times}"
             dur="{DUR_S}s" repeatCount="indefinite"/>
  </rect>
  <text x="{VAL_X}" y="{ROW_KE + 5}" class="math small ke-c">½kA² sin²(ωt)</text>
  <text x="{LABEL_X}" y="{ROW_KE + 24}" class="formula ke-c" text-anchor="end" opacity="0.7">kinetic energy</text>

  <!-- ===== PE (unipolar, grows from left) ===== -->
  <text x="{LABEL_X}" y="{ROW_PE + 5}" class="math label pe-c" text-anchor="end">PE</text>
  <rect x="{RIGHT_X0}" y="{ROW_PE - BAR_HEIGHT/2}" width="{BAR_MAX}" height="{BAR_HEIGHT}"
        fill="none" stroke="#888" stroke-width="0.6" stroke-dasharray="2,3" opacity="0.45"/>
  <rect x="{RIGHT_X0}" y="{ROW_PE - BAR_HEIGHT/2}" height="{BAR_HEIGHT}"
        fill="rgba(124, 58, 237, 0.55)" stroke="#7c3aed" stroke-width="1.5">
    <animate attributeName="width" values="{vals(pe_width)}" keyTimes="{key_times}"
             dur="{DUR_S}s" repeatCount="indefinite"/>
  </rect>
  <text x="{VAL_X}" y="{ROW_PE + 5}" class="math small pe-c">½kA² cos²(ωt)</text>
  <text x="{LABEL_X}" y="{ROW_PE + 24}" class="formula pe-c" text-anchor="end" opacity="0.7">elastic potential energy</text>

  <!-- Bottom caption -->
  <text x="{W/2}" y="{H - 18}" class="small" text-anchor="middle" opacity="0.85">
    <tspan class="math ke-c">KE</tspan> + <tspan class="math pe-c">PE</tspan> is constant at every instant. <tspan class="math x-c">x</tspan> and <tspan class="math a-c">a</tspan> mirror each other through zero.
  </text>
</svg>
'''

SVG_PATH.write_text(svg)
print(f"Wrote SMIL animation -> {SVG_PATH}")
print(f"Keyframes: {N_FRAMES}, period: {DUR_S}s, total file size: {len(svg)} bytes")

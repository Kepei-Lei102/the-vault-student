"""Proof by Induction — the pattern that fools you (Moser's circle).

Put n points on a circle, join every pair, count the regions:
1, 2, 4, 8, 16 ... and then 31. Five confirmations, then betrayal.

Beat 1: n = 1..5 — regions shaded, one dot dropped per region, counter ticking,
        the tally building 1, 2, 4, 8, 16 with the doubling marked.
Beat 2: the prediction 32, then n = 6 counted honestly to 31.
Beat 3: the lesson — checking is sampling, and no sample covers infinity.

Render:  manim -qk moser-circle-betrayal.py MoserCircle
House style: bg #1a1a1a, captions #9a9a9a, teal count, amber the guess, red the break.
Deterministic — the point placement is fixed and chosen so no three chords meet.
"""

import numpy as np
from math import cos, sin, pi
from manim import *

BG = "#1a1a1a"
GRAYT = "#9a9a9a"
TEAL = "#0891b2"
AMBER = "#f59e0b"
RED = "#dc2626"
GREEN = "#059669"

config.background_color = BG

# Fixed generic placement: no three chords concurrent (a REGULAR hexagon would
# give 30, not 31 — its three long diagonals all cross at the centre).
ANGLES = [95.7, 161.8, 213.8, 284.9, 337.7, 45.4]

R = 2.25
ORIGIN_C = np.array([-3.0, 0.5, 0.0])

PALETTE = [
    (37, 99, 235), (124, 58, 237), (5, 150, 105), (8, 145, 178),
    (245, 158, 11), (220, 38, 38), (14, 116, 144), (109, 40, 217),
    (4, 120, 87), (180, 83, 9), (30, 64, 175), (157, 23, 77),
]


def unit_points(n):
    return np.array([[cos(a * pi / 180), sin(a * pi / 180)] for a in ANGLES[:n]])


def to_scene(p):
    return ORIGIN_C + np.array([p[0] * R, p[1] * R, 0.0])


def _codes(n, N):
    P = unit_points(n)
    xs = np.linspace(-1, 1, N)
    X, Y = np.meshgrid(xs, xs)
    inside = X * X + Y * Y < 1.0
    codes = np.zeros((N, N), dtype=np.int32)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = P[i], P[j]
            s = (b[0] - a[0]) * (Y - a[1]) - (b[1] - a[1]) * (X - a[0]) > 0
            codes = codes * 2 + s.astype(np.int32)
    return codes, inside, X, Y


def region_image(n, res=900, alpha=115):
    """RGBA uint8, 2x supersampled, rows top-down for ImageMobject."""
    N = res * 2
    codes, inside, _, _ = _codes(n, N)
    vals = np.unique(codes[inside])
    lut = {v: i for i, v in enumerate(vals)}
    big = np.zeros((N, N, 4), dtype=np.float32)
    for v in vals:
        m = (codes == v) & inside
        r, g, b = PALETTE[lut[v] % len(PALETTE)]
        big[m] = (r, g, b, alpha)
    small = big.reshape(res, 2, res, 2, 4).mean(axis=(1, 3))
    return np.flipud(small.astype(np.uint8))


def region_anchors(n, N=800):
    """One point per region, biggest region first. Regions are intersections of
    half-planes with a disk, hence convex — the centroid always lands inside."""
    codes, inside, X, Y = _codes(n, N)
    vals = np.unique(codes[inside])
    out = []
    for v in vals:
        m = (codes == v) & inside
        out.append((float(X[m].mean()), float(Y[m].mean()), int(m.sum())))
    out.sort(key=lambda t: -t[2])
    return [(x, y) for x, y, _ in out]


class MoserCircle(Scene):
    # ------------------------------------------------------------------
    def swap_caption(self, text, color=GRAYT, font_size=30):
        cap = Text(text, color=color, font_size=font_size, line_spacing=0.9)
        cap.move_to(DOWN * 3.35)
        anims = [FadeIn(cap, run_time=0.35)]
        if getattr(self, "_cap", None) is not None:
            anims.append(FadeOut(self._cap, run_time=0.25))
        self._cap = cap
        self.play(*anims)

    def construct(self):
        self.img = None
        self.dots = VGroup()
        self.chords = VGroup()
        self.pts = VGroup()
        self.rows = VGroup()

        circle = Circle(radius=R, color=GRAYT, stroke_width=2.5).move_to(ORIGIN_C)
        self.play(Create(circle), run_time=0.9)

        # tally header
        hx, cx, top = 2.15, 4.5, 2.5
        h1 = Text("points", font_size=22, color=GRAYT).move_to([hx, top, 0])
        h2 = Text("regions", font_size=22, color=GRAYT).move_to([cx, top, 0])
        rule = Line([hx - 0.75, top - 0.3, 0], [cx + 0.75, top - 0.3, 0],
                    stroke_width=1.5, color=GRAYT).set_opacity(0.5)
        self.play(FadeIn(h1), FadeIn(h2), Create(rule), run_time=0.6)

        self.tracker = ValueTracker(0)
        self.counter = always_redraw(
            lambda: Integer(int(round(self.tracker.get_value())), color=TEAL,
                            font_size=54).move_to(ORIGIN_C + DOWN * (R + 0.62)))
        self.add(self.counter)

        self.swap_caption("put n points on a circle, join every pair,\ncount the regions")

        for n in range(1, 6):
            self.step(n, hx, cx, top)

        self.beat_doubling(hx, cx, top)
        self.beat_six(hx, cx, top)
        self.beat_lesson()

    # ------------------------------------------------------------------
    def step(self, n, hx, cx, top, run=1.0, label=True, count_x=None, count_color=TEAL):
        P = unit_points(n)
        new_pt = Dot(to_scene(P[n - 1]), radius=0.075, color=AMBER)
        anims = [FadeIn(new_pt, scale=0.4)]
        self.pts.add(new_pt)

        new_chords = VGroup()
        for i in range(n - 1):
            new_chords.add(Line(to_scene(P[i]), to_scene(P[n - 1]),
                                stroke_width=2.6, color=GRAYT).set_opacity(0.85))
        self.chords.add(*new_chords)
        if len(new_chords):
            anims.append(LaggedStart(*[Create(c) for c in new_chords],
                                     lag_ratio=0.25))
        self.play(*anims, run_time=run)

        # shading
        img = ImageMobject(region_image(n)).set_z_index(-2)
        img.set_height(2 * R).move_to(ORIGIN_C)
        fade = [FadeIn(img, run_time=0.4)]
        if self.img is not None:
            fade.append(FadeOut(self.img, run_time=0.4))
        self.img = img
        self.play(*fade)

        # one dot per region, counter riding along
        anchors = region_anchors(n)
        if len(self.dots):
            self.play(FadeOut(self.dots), run_time=0.2)
        self.dots = VGroup(*[Dot(to_scene(a), radius=0.055, color=WHITE)
                             for a in anchors])
        self.tracker.set_value(0)
        t = 0.5 + 0.09 * len(anchors)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in self.dots],
                              lag_ratio=0.55 / max(len(anchors), 1)),
                  self.tracker.animate.set_value(len(anchors)),
                  run_time=t, rate_func=linear)

        y = top - 0.75 - 0.44 * (n - 1)
        row = VGroup()
        if label:
            row.add(Text(str(n), font_size=28, color=GRAYT).move_to([hx, y, 0]))
        row.add(Text(str(len(anchors)), font_size=28, color=count_color)
                .move_to([cx if count_x is None else count_x, y, 0]))
        self.rows.add(row)
        self.play(FadeIn(row), run_time=0.35)
        self.wait(0.35)

    # ------------------------------------------------------------------
    def beat_doubling(self, hx, cx, top):
        marks = VGroup()
        for i in range(4):
            y = top - 0.75 - 0.44 * i - 0.22
            marks.add(Text("x2", font_size=20, color=AMBER).move_to([cx + 0.85, y, 0]))
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.2), run_time=1.2)
        self.swap_caption("1, 2, 4, 8, 16 — it doubles every time.\nfive confirmations in a row")
        self.wait(2.4)

    # ------------------------------------------------------------------
    def beat_six(self, hx, cx, top):
        y6 = top - 0.75 - 0.44 * 5
        guess_n = Text("6", font_size=28, color=GRAYT).move_to([hx, y6, 0])
        guess = Text("32?", font_size=28, color=AMBER).move_to([cx, y6, 0])
        self.swap_caption("so six points must give 32")
        self.play(FadeIn(guess_n), FadeIn(guess), run_time=0.6)
        self.wait(1.6)

        self.swap_caption("count them honestly")
        # strike the guess first, then land the true count clear of it
        self.step(6, hx, cx, top, run=1.4, label=False,
                  count_x=cx + 1.35, count_color=GREEN)
        strike = Line(guess.get_left() + LEFT * 0.12, guess.get_right() + RIGHT * 0.12,
                      color=RED, stroke_width=4)
        self.play(Create(strike), guess.animate.set_opacity(0.4), run_time=0.6)
        self.wait(0.3)
        self.swap_caption("thirty-one.\nthe pattern held five times and then simply was not the law")
        self.wait(3.0)

    # ------------------------------------------------------------------
    def beat_lesson(self):
        self.swap_caption("no number of checks proves a claim about every n —\nthe unchecked cases outnumber the checked ones, infinitely to finitely")
        self.wait(3.4)
        self.swap_caption("so stop checking cases.\nprove the link BETWEEN them, and push the first")
        self.wait(3.4)

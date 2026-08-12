"""Real random trials for Linear Combinations of RVs — date-seeded, self-stamping.

The current date IS the seed: rerun on another day and every dot moves,
but the squared terms stay fat, the cross term starves, and 3X still
sprawls twice as wide as three cups. The draw changes; the law does not.

Render (from this folder):
    manim -qm lincomb-trials.py CrossTermTrial ThreeCupsTrial   # smoke
    manim -qk lincomb-trials.py CrossTermTrial ThreeCupsTrial   # 4K final
Copy outputs beside the card as lincomb-cross-term.mp4 and
lincomb-3x-vs-sum.mp4, then clear media/ + __pycache__/.
Override the date (to regenerate a specific day's video) with
    LINCOMB_DATE=2026-08-01 manim -qk ...
"""

import os
from datetime import date

import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
TEAL = "#0891b2"

config.background_color = BG

DATE = os.environ.get("LINCOMB_DATE") or date.today().isoformat()
SEED = int(DATE.replace("-", ""))
rng = np.random.default_rng(SEED)


def stamp():
    t1 = Text(f"date generated: {DATE}", font_size=17, color=GRAY)
    t2 = Text(f"seed {SEED} — rerun for a new draw", font_size=14, color=GRAY)
    g = VGroup(t1, t2).arrange(DOWN, aligned_edge=RIGHT, buff=0.08)
    return g.to_corner(UR, buff=0.35)


class CaptionMixin:
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=26, color=color).to_edge(DOWN, buff=0.35)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.25), FadeIn(cap, run_time=0.35))
        else:
            self.play(FadeIn(cap, run_time=0.35))
        self._cap = cap


class CrossTermTrial(CaptionMixin, Scene):
    def construct(self):
        n = 300
        x = rng.normal(0, 3, n)
        y = rng.normal(2, 4, n)
        dx, dy = x - 0.0, y - 2.0
        prod = dx * dy
        m_dx2, m_dy2, m_cross = np.mean(dx**2), np.mean(dy**2), 2 * np.mean(prod)

        # ---- left: the deviation plane ----
        origin = LEFT * 3.6 + DOWN * 0.2
        sx, sy = 0.27, 0.195  # units per Dx / Dy
        ax_h = Line(origin + LEFT * 2.9, origin + RIGHT * 2.9, color=GRAY, stroke_width=2)
        ax_v = Line(origin + DOWN * 2.7, origin + UP * 2.7, color=GRAY, stroke_width=2)
        lab_x = Text("Dx", font_size=22, color=GRAY).next_to(ax_h, RIGHT, buff=0.15)
        lab_y = Text("Dy", font_size=22, color=GRAY).next_to(ax_v, UP, buff=0.12)
        q_pp = Polygon(origin, origin + RIGHT * 2.9, origin + RIGHT * 2.9 + UP * 2.7, origin + UP * 2.7,
                       stroke_width=0, fill_color=GREEN, fill_opacity=0.06)
        q_mm = Polygon(origin, origin + LEFT * 2.9, origin + LEFT * 2.9 + DOWN * 2.7, origin + DOWN * 2.7,
                       stroke_width=0, fill_color=GREEN, fill_opacity=0.06)
        q_pm = Polygon(origin, origin + RIGHT * 2.9, origin + RIGHT * 2.9 + DOWN * 2.7, origin + DOWN * 2.7,
                       stroke_width=0, fill_color=RED, fill_opacity=0.06)
        q_mp = Polygon(origin, origin + LEFT * 2.9, origin + LEFT * 2.9 + UP * 2.7, origin + UP * 2.7,
                       stroke_width=0, fill_color=RED, fill_opacity=0.06)

        self.play(FadeIn(VGroup(q_pp, q_mm, q_pm, q_mp, ax_h, ax_v, lab_x, lab_y)), FadeIn(stamp()), run_time=0.9)
        self.swap_caption(f"{n} independent draws — do the deviations conspire?")

        dots = VGroup(*[
            Dot(origin + RIGHT * float(np.clip(a, -10.5, 10.5)) * sx + UP * float(np.clip(b, -13.5, 13.5)) * sy,
                radius=0.035, color=GREEN if a * b > 0 else RED, fill_opacity=0.85)
            for a, b in zip(dx, dy)
        ])
        for k in range(3):
            self.play(LaggedStart(*[FadeIn(d, scale=2.2) for d in dots[k * 100:(k + 1) * 100]],
                                  lag_ratio=0.01), run_time=1.6)
        self.swap_caption("green: deviations agree — red: they disagree")
        self.wait(0.8)

        # ---- right: the three terms, measured ----
        base_y = DOWN * 2.2
        bx = [RIGHT * 2.2, RIGHT * 4.0, RIGHT * 5.8]
        vals = [m_dx2, m_dy2, m_cross]
        cols = [BLUE, TEAL, AMBER]
        names = ["mean Dx²", "mean Dy²", "2·mean DxDy"]
        theos = ["theory 9", "theory 16", "theory 0"]
        bars, tops, labs = VGroup(), VGroup(), VGroup()
        for pos, v, c, nm, th in zip(bx, vals, cols, names, theos):
            h = max(abs(v) * 0.17, 0.03)
            bar = Rectangle(width=1.0, height=h, stroke_color=c, stroke_width=2.5,
                            fill_color=c, fill_opacity=0.35)
            bar.move_to(pos + base_y + UP * (h / 2 if v >= 0 else -h / 2))
            top = Text(f"{v:.2f}", font_size=22, color=c, weight=BOLD)
            top.next_to(bar, UP if v >= 0 else DOWN, buff=0.12)
            l1 = Text(nm, font_size=17, color=GRAY)
            l2 = Text(th, font_size=14, color=GRAY)
            lg = VGroup(l1, l2).arrange(DOWN, buff=0.06)
            lg.next_to(pos + base_y, DOWN, buff=0.5)
            bars.add(bar); tops.add(top); labs.add(lg)
        floor = Line(RIGHT * 1.5 + base_y, RIGHT * 6.5 + base_y, color=GRAY, stroke_width=2)

        self.swap_caption("now measure the three terms of Var(X + Y)")
        self.play(Create(floor), FadeIn(labs), run_time=0.6)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars], run_time=1.1)
        self.play(FadeIn(tops), run_time=0.5)
        self.wait(0.6)
        self.swap_caption("the squares thrive — the cross term starves", color=AMBER)
        self.wait(1.0)
        self.swap_caption("your draw will differ; the zero will not", color=GREEN)
        self.wait(1.6)


class ThreeCupsTrial(CaptionMixin, Scene):
    def construct(self):
        n = 150
        mu, sig = 250.0, 4.0
        triple = 3 * rng.normal(mu, sig, n)              # one cup, tripled
        sums = rng.normal(mu, sig, (n, 3)).sum(axis=1)   # three cups
        sd_t, sd_s = float(np.std(triple, ddof=1)), float(np.std(sums, ddof=1))

        def strip(center_x, values, color):
            axis_y = DOWN * 1.4
            scale = 0.055          # units per ml
            half = 2.85
            ax = Line(RIGHT * center_x + LEFT * half + axis_y,
                      RIGHT * center_x + RIGHT * half + axis_y, color=GRAY, stroke_width=2)
            ticks, tlabs = VGroup(), VGroup()
            for v in (710, 750, 790):
                px = RIGHT * (center_x + (v - 750) * scale) + axis_y
                ticks.add(Line(px + DOWN * 0.07, px + UP * 0.07, color=GRAY, stroke_width=2))
                tlabs.add(Text(str(v), font_size=16, color=GRAY).next_to(px, DOWN, buff=0.15))
            binw = 3.0
            counts = {}
            dots = VGroup()
            for v in values:
                b = round((v - 750) / binw)
                k = counts.get(b, 0)
                counts[b] = k + 1
                pos = RIGHT * (center_x + b * binw * scale) + axis_y + UP * (0.13 + k * 0.115)
                dots.add(Dot(pos, radius=0.045, color=color, fill_opacity=0.85))
            return ax, ticks, tlabs, dots

        axL, tkL, tlL, dotsL = strip(-3.55, triple, AMBER)
        axR, tkR, tlR, dotsR = strip(3.55, sums, GREEN)

        titleL1 = Text("3X — one cup, tripled", font_size=24, color=AMBER, weight=BOLD).move_to(LEFT * 3.55 + UP * 3.0)
        titleR1 = Text("X₁+X₂+X₃ — three cups", font_size=24, color=GREEN, weight=BOLD).move_to(RIGHT * 3.55 + UP * 3.0)

        self.play(FadeIn(VGroup(axL, tkL, tlL, axR, tkR, tlR, titleL1, titleR1)), FadeIn(stamp()), run_time=0.9)
        self.swap_caption(f"the same random stream pours real cups — {n} trials each side")

        for k in range(3):
            self.play(
                LaggedStart(*[FadeIn(d, scale=1.8) for d in dotsL[k * 50:(k + 1) * 50]], lag_ratio=0.015),
                LaggedStart(*[FadeIn(d, scale=1.8) for d in dotsR[k * 50:(k + 1) * 50]], lag_ratio=0.015),
                run_time=1.7,
            )
        self.swap_caption("one photocopied wobble — versus three wobbles partly cancelling")
        self.wait(0.8)

        # measured spreads: double arrows spanning +-1 sample sd
        scale, axis_y = 0.055, DOWN * 1.4
        arrL = DoubleArrow(LEFT * 3.55 + LEFT * (sd_t * scale) + axis_y + DOWN * 0.55,
                           LEFT * 3.55 + RIGHT * (sd_t * scale) + axis_y + DOWN * 0.55,
                           color=AMBER, buff=0, stroke_width=3, tip_length=0.15)
        arrR = DoubleArrow(RIGHT * 3.55 + LEFT * (sd_s * scale) + axis_y + DOWN * 0.55,
                           RIGHT * 3.55 + RIGHT * (sd_s * scale) + axis_y + DOWN * 0.55,
                           color=GREEN, buff=0, stroke_width=3, tip_length=0.15)
        labL = Text(f"sample σ = {sd_t:.1f}   (theory 12)", font_size=19, color=AMBER).next_to(arrL, DOWN, buff=0.14)
        labR = Text(f"sample σ = {sd_s:.1f}   (theory 6.93)", font_size=19, color=GREEN).next_to(arrR, DOWN, buff=0.14)
        self.play(GrowFromCenter(arrL), GrowFromCenter(arrR), run_time=0.7)
        self.play(FadeIn(labL), FadeIn(labR), run_time=0.5)
        self.wait(0.6)
        self.swap_caption("same mean — different worlds: 9σ² against 3σ²", color=GRAY)
        self.wait(1.6)

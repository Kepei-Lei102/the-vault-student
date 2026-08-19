"""Manim: the rank-sum test as a deal of cards — 9231/43 June 2025 Q4.

Fourteen reaction times, six from people over 50 and eight from people under
25, are pooled and ranked 1..14. The over-50 ranks sum to R_6 = 60. Then the
ages are forgotten: if age made no difference, the six over-50 ranks are just
six ranks dealt at random from fourteen. The scene deals them — first one hand
at a time, then a hundred, then a thousand — dropping each hand's R_6 as a
brick onto the axis, until the pile has a shape; then the EXACT distribution
(all C(14,6) = 3003 hands, counted) is laid over it, and the observed 60 is
marked with its tail: 89 hands of 3003 = 2.96%. W = 30 against the table's 31.

Date-seeded like sampling-clt-live.py: rerun on another day and every deal
changes; the counted curve does not.

Render (from this folder):
    VAULT_DATE=YYYY-MM-DD manim -qm wilcoxon-rank-shuffle.py WilcoxonRankShuffle   # smoke
    VAULT_DATE=YYYY-MM-DD manim -qk wilcoxon-rank-shuffle.py WilcoxonRankShuffle   # 4K final
Copy media/videos/wilcoxon-rank-shuffle/2160p60/WilcoxonRankShuffle.mp4
  -> wilcoxon-rank-shuffle.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import os
from itertools import combinations
from collections import Counter
from math import comb
import numpy as np
from manim import (
    Scene, VGroup, VMobject, Axes, Text, MathTex, Rectangle, RoundedRectangle, DashedLine, Line,
    Integer, FadeIn, FadeOut, Transform, Create, Write, UP, DOWN, LEFT, RIGHT, UR, UL, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
AMBER = "#f59e0b"
FONT = "Helvetica Neue"

config.background_color = BG

DATE = os.environ.get("VAULT_DATE", "2026-08-18")
SEED = int(DATE.replace("-", ""))

OVER = [198, 212, 217, 229, 235, 242]                     # m = 6
UNDER = [178, 181, 183, 192, 203, 209, 223, 231]          # n = 8
M, N = len(OVER), len(UNDER)
TOT = M + N
POOL = sorted([(v, "o") for v in OVER] + [(v, "u") for v in UNDER])
RANK_OF_OVER = [i + 1 for i, (v, g) in enumerate(POOL) if g == "o"]   # 5, 8, 9, 11, 13, 14
R_OBS = sum(RANK_OF_OVER)                                             # 60
N_DEALS = 1000
LO, HI = 20, 70                                                       # R_6 runs 21..69
NB = HI - LO
EXACT = Counter(sum(c) for c in combinations(range(1, TOT + 1), M))   # 3003 hands
TAIL = sum(v for s, v in EXACT.items() if s >= R_OBS)                 # 89


class WilcoxonRankShuffle(Scene):
    def swap_caption(self, text, color=TXT, font_size=24):
        cap = Text(text, font=FONT, font_size=font_size, color=color, line_spacing=0.85).to_edge(DOWN, buff=0.2)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def cards(self, over_set):
        """The 14 pooled ranks as cards; the ones in over_set are amber (over 50)."""
        g = VGroup()
        for i, (v, grp) in enumerate(POOL):
            r = i + 1
            col = AMBER if r in over_set else BLUE
            card = RoundedRectangle(width=0.72, height=0.95, corner_radius=0.08, fill_color=col,
                                    fill_opacity=0.28, stroke_color=col, stroke_width=2)
            card.move_to([-6.5 + i * 1.0, 2.15, 0])
            num = Text(str(r), font=FONT, font_size=26, color=col).move_to(card.get_center() + UP * 0.12)
            val = Text(str(v), font=FONT, font_size=14, color=GREY).move_to(card.get_center() + DOWN * 0.3)
            g.add(VGroup(card, num, val))
        return g

    def hist_bars(self, counts, unit):
        g = VGroup()
        for b in range(NB):
            c = counts[b]
            if c == 0:
                continue
            x0 = LO + b
            p0 = self.hax.c2p(x0, 0)
            p1 = self.hax.c2p(x0 + 1, min(c * unit, 1.0))
            r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1], fill_color=BLUE, fill_opacity=0.6,
                          stroke_color=BLUE, stroke_width=1.0)
            r.move_to((p0 + p1) / 2)
            g.add(r)
        return g

    def brick(self, b, level, unit):
        x0 = LO + b
        p0 = self.hax.c2p(x0, level * unit)
        p1 = self.hax.c2p(x0 + 1, (level + 1) * unit)
        r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1], fill_color=BLUE, fill_opacity=0.6,
                      stroke_color=BLUE, stroke_width=1.0)
        r.move_to((p0 + p1) / 2)
        return r

    def construct(self):
        rng = np.random.default_rng(SEED)
        deals = [set(rng.choice(np.arange(1, TOT + 1), size=M, replace=False).tolist()) for _ in range(N_DEALS)]
        sums = np.array([sum(d) for d in deals])

        title = Text("rank-sum: if age made no difference, the fourteen ranks are dealt at random",
                     font=FONT, font_size=28, color=TXT).to_edge(UP, buff=0.26)
        stamp = Text(f"date generated: {DATE}  ·  seed = {SEED}", font=FONT, font_size=16, color=GREY
                     ).to_corner(UR, buff=0.28).shift(DOWN * 0.5)
        self.play(Write(title), FadeIn(stamp), run_time=1.2)

        # ---- the real deal
        cards = self.cards(set(RANK_OF_OVER))
        legend = VGroup(
            Text("over 50 (m = 6)", font=FONT, font_size=19, color=AMBER),
            Text("under 25 (n = 8)", font=FONT, font_size=19, color=BLUE),
        ).arrange(RIGHT, buff=0.6).move_to([0, 1.35, 0])
        self.play(FadeIn(cards, lag_ratio=0.05), FadeIn(legend), run_time=1.2)
        self.swap_caption("pooled and ranked 1 to 14: the six over-50 times take ranks 5, 8, 9, 11, 13, 14")
        self.wait(0.6)
        robs = MathTex(r"R_6 = 5+8+9+11+13+14 = 60", color=AMBER).scale(0.8).move_to([-3.2, 0.7, 0])
        wobs = MathTex(r"W = \min(60,\ 6\times 15 - 60) = 30", color=AMBER).scale(0.8).move_to([3.4, 0.7, 0])
        self.play(Write(robs), run_time=0.9)
        self.play(Write(wobs), run_time=0.9)
        self.wait(0.8)

        # ---- histogram axes
        self.hax = Axes(x_range=[LO, HI, 5], y_range=[0, 1, 1], x_length=11.6, y_length=2.0,
                        axis_config=dict(color=GREY, stroke_width=2, include_ticks=True, include_tip=False),
                        x_axis_config=dict(include_numbers=True, font_size=22,
                                           decimal_number_config={"num_decimal_places": 0, "color": GREY}),
                        y_axis_config=dict(include_ticks=False)).move_to([0.5, -1.85, 0])
        hxlab = MathTex(r"R_6\ \text{of a random hand}", color=TXT).scale(0.68).move_to(self.hax.c2p(66.6, 0.55))
        self.play(FadeIn(self.hax), FadeIn(hxlab), FadeOut(legend), run_time=0.7)

        # ---- forget the ages: deal at random
        self.swap_caption("now forget the ages: deal six of the fourteen ranks to 'over 50' at random and add them up")
        counter = Integer(0, font_size=30, color=BLUE)
        clab = Text("random hands dealt:", font=FONT, font_size=21, color=BLUE)
        crow = VGroup(clab, counter).arrange(RIGHT, buff=0.18).move_to([3.4, 0.7, 0])
        self.play(FadeOut(wobs), FadeIn(crow), run_time=0.4)
        readout = None
        counts = np.zeros(NB, dtype=int)
        UNIT_A = 1 / 8
        bricks = VGroup()
        for t in range(5):                                # five single deals
            s = int(sums[t])
            newcards = self.cards(deals[t])
            num = MathTex(rf"R_6 = {s}", color=BLUE).scale(0.85).move_to([-3.2, 0.7, 0])
            anims = [Transform(cards, newcards), counter.animate.set_value(t + 1)]
            if t == 0:
                anims.append(FadeOut(robs))
            if readout is not None:
                anims.append(FadeOut(readout))
            self.play(*anims, run_time=0.55)
            self.play(FadeIn(num), run_time=0.25)
            readout = num
            b = s - LO
            br = self.brick(b, counts[b], UNIT_A)
            counts[b] += 1
            self.play(Transform(num, br), run_time=0.45)
            self.remove(num)
            self.add(br)
            bricks.add(br)
            readout = None
        idx = 5
        group = VGroup()
        while idx < 12:                                   # 6..12 as bricks in a batch
            b = int(sums[idx]) - LO
            group.add(self.brick(b, counts[b], UNIT_A))
            counts[b] += 1
            idx += 1
        self.play(FadeIn(group, lag_ratio=0.1), Transform(cards, self.cards(deals[idx - 1])),
                  counter.animate.set_value(idx), run_time=1.1)
        bricks.add(*group)

        # ---- to 100, then 1000
        self.swap_caption("a hundred hands: the pile forms around 45 — the six ranks of an average hand add to 45")
        hist = bricks
        for target in (30, 60, 100):
            while idx < target:
                counts[int(sums[idx]) - LO] += 1
                idx += 1
            unit = 0.92 / counts.max()
            self.play(Transform(hist, self.hist_bars(counts, unit)), Transform(cards, self.cards(deals[idx - 1])),
                      counter.animate.set_value(idx), run_time=0.9)
        self.wait(0.6)
        self.swap_caption("a thousand hands — and the pile smooths into the shape every honest deal must follow")
        for target in (250, 500, 1000):
            while idx < target:
                counts[int(sums[idx]) - LO] += 1
                idx += 1
            unit = 0.92 / counts.max()
            self.play(Transform(hist, self.hist_bars(counts, unit)), Transform(cards, self.cards(deals[idx - 1])),
                      counter.animate.set_value(idx), run_time=0.9)
        assert idx == N_DEALS
        self.wait(0.4)

        # ---- the exact distribution: 3003 hands, counted
        unit = 0.92 / counts.max()
        pts = []
        for s in range(LO, HI + 1):
            h = N_DEALS * EXACT.get(s, 0) / comb(TOT, M) * unit
            pts.append(self.hax.c2p(s, h))
            pts.append(self.hax.c2p(s + 1, h))
        step = VMobject(color=PURPLE, stroke_width=4).set_points_as_corners(pts)
        slab = Text("all 3003 possible hands, counted", font=FONT, font_size=19, color=PURPLE).move_to(
            self.hax.c2p(28.5, 0.86))
        self.swap_caption("nothing was fitted: all C(14, 6) = 3003 hands are equally likely — count them, and the table appears",
                          color=PURPLE, font_size=22)
        self.play(Create(step), FadeIn(slab), run_time=1.6)
        self.wait(1.2)

        # ---- the observed hand
        cut = Line(self.hax.c2p(R_OBS, 0), self.hax.c2p(R_OBS, 1.0), color=AMBER, stroke_width=4)
        cutlab = MathTex(r"\text{the real hand: } R_6 = 60", color=AMBER).scale(0.8).move_to([-2.6, -0.45, 0])
        taillab = Text(f"{TAIL} of the 3003 hands reach 60 or more:  {100*TAIL/comb(TOT, M):.2f}%", font=FONT,
                       font_size=20, color=AMBER).next_to(cutlab, RIGHT, buff=0.5)
        self.play(Create(cut), FadeIn(cutlab), Transform(cards, self.cards(set(RANK_OF_OVER))), run_time=0.7)
        self.play(FadeIn(taillab), run_time=0.5)
        self.swap_caption("W = 30 ≤ 31 (the table's 5% value for m = 6, n = 8): a deal this lopsided is rarer than 5% — reject",
                          color=AMBER, font_size=22)
        self.wait(3.2)

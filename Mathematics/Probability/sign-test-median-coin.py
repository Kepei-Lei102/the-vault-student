"""Manim: the sign test as a fair coin — a population with its own median, sampled.

A population of 400 numbers between 0 and 1000 (skewed on purpose, like
salaries — the sign test does not care). Its median is found from the
population itself, so EXACTLY 200 lie above and 200 below: the null hypothesis
is true by construction. Then a random sample of 10 is drawn and the split is
counted — 6 above / 4 below, 5 / 5, 4 / 6 … — and each count of "above" drops
as a brick onto the axis 0..10. First five samples singly, then a hundred, then
a thousand: the pile is B(10, 1/2), which is then laid over it, with the tails
priced — 8-or-more above happens 5.5% of the time by chance alone (the jigsaw's
split), 10-0 one time in a thousand.

Date-seeded like the CLT clip: rerun on another day and every draw changes; the
coin's curve does not. (Sampling 10 of 400 without replacement is
hypergeometric, not binomial — the two agree to 1% at the peak, so the overlay
is B(10, 1/2), which is what the test uses.)

Render (from this folder):
    VAULT_DATE=YYYY-MM-DD manim -qm sign-test-median-coin.py SignTestMedianCoin   # smoke
    VAULT_DATE=YYYY-MM-DD manim -qk sign-test-median-coin.py SignTestMedianCoin   # 4K final
Copy media/videos/sign-test-median-coin/2160p60/SignTestMedianCoin.mp4
  -> sign-test-median-coin.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import os
import numpy as np
from scipy import stats
from manim import (
    Scene, VGroup, VMobject, Axes, Text, MathTex, Rectangle, Circle, Dot, Line,
    Integer, FadeIn, FadeOut, Transform, Create, Write, UP, DOWN, LEFT, RIGHT, UR, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
REDC = "#dc2626"
AMBER = "#f59e0b"
FONT = "Helvetica Neue"

config.background_color = BG

DATE = os.environ.get("VAULT_DATE", "2026-08-18")
SEED = int(DATE.replace("-", ""))

N_POP = 400
N_SAMPLE = 10
N_DRAWS = 1000


class SignTestMedianCoin(Scene):
    def swap_caption(self, text, color=TXT, font_size=24):
        cap = Text(text, font=FONT, font_size=font_size, color=color, line_spacing=0.85).to_edge(DOWN, buff=0.2)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def hist_bars(self, counts, unit):
        g = VGroup()
        for k in range(N_SAMPLE + 1):
            c = counts[k]
            if c == 0:
                continue
            p0 = self.hax.c2p(k - 0.5, 0)
            p1 = self.hax.c2p(k + 0.5, min(c * unit, 1.0))
            r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1], fill_color=BLUE, fill_opacity=0.6,
                          stroke_color=BLUE, stroke_width=1.0)
            r.move_to((p0 + p1) / 2)
            g.add(r)
        return g

    def brick(self, k, level, unit):
        p0 = self.hax.c2p(k - 0.5, level * unit)
        p1 = self.hax.c2p(k + 0.5, (level + 1) * unit)
        r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1], fill_color=BLUE, fill_opacity=0.6,
                      stroke_color=BLUE, stroke_width=1.0)
        r.move_to((p0 + p1) / 2)
        return r

    def rings(self, idx):
        return VGroup(*[Circle(radius=0.11, color=AMBER, stroke_width=2.5).move_to(self.dot_pos[i]) for i in idx])

    def construct(self):
        rng = np.random.default_rng(SEED)
        # a skewed population of 400 distinct integers in [0, 1000]
        xs = np.arange(0, 1001)
        w = (xs + 40.0) ** 1.6 * np.exp(-xs / 230.0)
        w /= w.sum()
        pop = np.sort(rng.choice(xs, size=N_POP, replace=False, p=w))
        med = (pop[N_POP // 2 - 1] + pop[N_POP // 2]) / 2          # exactly half above, half below
        assert (pop > med).sum() == N_POP // 2
        jit = rng.uniform(-0.38, 0.38, size=N_POP)
        draws = [rng.choice(N_POP, size=N_SAMPLE, replace=False) for _ in range(N_DRAWS)]
        above = np.array([(pop[d] > med).sum() for d in draws])

        title = Text("the sign test: if the median is where the claim says, each observation is a fair coin",
                     font=FONT, font_size=27, color=TXT).to_edge(UP, buff=0.26)
        stamp = Text(f"date generated: {DATE}  ·  seed = {SEED}", font=FONT, font_size=16, color=GREY
                     ).to_corner(UR, buff=0.28).shift(DOWN * 0.5)
        self.play(Write(title), FadeIn(stamp), run_time=1.2)

        # ---- population strip
        self.pax = Axes(x_range=[0, 1000, 100], y_range=[-1, 1, 1], x_length=11.8, y_length=1.9,
                        axis_config=dict(color=GREY, stroke_width=2, include_ticks=True, include_tip=False),
                        x_axis_config=dict(include_numbers=True, font_size=20,
                                           decimal_number_config={"num_decimal_places": 0, "color": GREY}),
                        y_axis_config=dict(stroke_opacity=0, include_ticks=False)).move_to([0, 1.65, 0])
        self.dot_pos = [self.pax.c2p(float(v), float(j)) for v, j in zip(pop, jit)]
        dots = VGroup(*[Dot(p, radius=0.045, color=GREY, fill_opacity=0.9) for p in self.dot_pos])
        self.play(FadeIn(self.pax.x_axis), FadeIn(dots, lag_ratio=0.002), run_time=1.6)
        self.swap_caption("a population of 400 numbers between 0 and 1000 — skewed on purpose, like salaries")
        self.wait(1.0)

        # ---- find the median: exactly half and half
        mline = Line(self.pax.c2p(med, -1.15), self.pax.c2p(med, 1.15), color=AMBER, stroke_width=4)
        mlab = Text(f"population median = {med:g}", font=FONT, font_size=21, color=AMBER).next_to(
            self.pax.c2p(med, 1.15), UP, buff=0.08)
        newdots = VGroup(*[Dot(p, radius=0.045, color=(GREEN if v > med else REDC), fill_opacity=0.9)
                           for p, v in zip(self.dot_pos, pop)])
        self.play(Create(mline), FadeIn(mlab), run_time=0.8)
        self.play(Transform(dots, newdots), run_time=1.0)
        half = VGroup(Text("200 below", font=FONT, font_size=21, color=REDC),
                      Text("200 above", font=FONT, font_size=21, color=GREEN)).arrange(RIGHT, buff=1.2)
        half.move_to([0, 0.35, 0])
        self.play(FadeIn(half), run_time=0.5)
        self.swap_caption("find its median: the claim 'the median is here' is now TRUE by construction — half on each side", font_size=23)
        self.wait(1.4)

        # ---- histogram axes (bottom)
        self.hax = Axes(x_range=[-0.5, 10.5, 1], y_range=[0, 1, 1], x_length=10.0, y_length=2.0,
                        axis_config=dict(color=GREY, stroke_width=2, include_ticks=True, include_tip=False),
                        x_axis_config=dict(include_numbers=True, font_size=22, numbers_to_include=list(range(0, 11)),
                                           decimal_number_config={"num_decimal_places": 0, "color": GREY}),
                        y_axis_config=dict(include_ticks=False)).move_to([-0.6, -1.85, 0])
        hxlab = Text("how many of the 10 landed above", font=FONT, font_size=19, color=TXT).move_to(
            self.hax.c2p(2.6, 1.08))
        self.play(FadeOut(half), FadeIn(self.hax), FadeIn(hxlab), run_time=0.7)

        # ---- samples of 10
        self.swap_caption("draw a random sample of 10 and count the split — above / below")
        counter = Integer(0, font_size=30, color=BLUE)
        clab = Text("samples of 10 drawn:", font=FONT, font_size=21, color=BLUE)
        crow = VGroup(clab, counter).arrange(RIGHT, buff=0.18).move_to([4.4, -0.55, 0])
        self.play(FadeIn(crow), run_time=0.3)
        counts = np.zeros(N_SAMPLE + 1, dtype=int)
        UNIT_A = 1 / 8
        bricks = VGroup()
        rings = None
        split = None
        for t in range(5):
            k = int(above[t])
            newr = self.rings(draws[t])
            newsplit = VGroup(Text(f"{k} above", font=FONT, font_size=26, color=GREEN),
                              Text("·", font=FONT, font_size=26, color=TXT),
                              Text(f"{N_SAMPLE - k} below", font=FONT, font_size=26, color=REDC)
                              ).arrange(RIGHT, buff=0.25).move_to([-3.0, 0.35, 0])
            anims = [FadeIn(newr), counter.animate.set_value(t + 1)]
            if rings is not None:
                anims += [FadeOut(rings), FadeOut(split)]
            self.play(*anims, run_time=0.5)
            self.play(FadeIn(newsplit), run_time=0.3)
            rings, split = newr, newsplit
            self.wait(0.3)
            br = self.brick(k, counts[k], UNIT_A)
            counts[k] += 1
            num = Text(f"{k}", font=FONT, font_size=30, color=GREEN).move_to(newsplit[0].get_center())
            self.play(Transform(num, br), run_time=0.45)
            self.remove(num)
            self.add(br)
            bricks.add(br)
        self.play(FadeOut(rings), FadeOut(split), run_time=0.3)

        idx = 5
        group = VGroup()
        while idx < 12:
            k = int(above[idx])
            group.add(self.brick(k, counts[k], UNIT_A))
            counts[k] += 1
            idx += 1
        self.play(FadeIn(group, lag_ratio=0.1), counter.animate.set_value(idx), run_time=1.0)
        bricks.add(*group)

        # ---- to 100 and 1000
        self.swap_caption("again and again: the split dangles around 5–5, 4–6, 6–4 — and almost never reaches 0–10 or 10–0", font_size=22)
        hist = bricks
        for target in (30, 60, 100):
            while idx < target:
                counts[int(above[idx])] += 1
                idx += 1
            unit = 0.92 / counts.max()
            self.play(Transform(hist, self.hist_bars(counts, unit)), counter.animate.set_value(idx), run_time=0.9)
        self.wait(0.6)
        for target in (250, 500, 1000):
            while idx < target:
                counts[int(above[idx])] += 1
                idx += 1
            unit = 0.92 / counts.max()
            self.play(Transform(hist, self.hist_bars(counts, unit)), counter.animate.set_value(idx), run_time=0.9)
        assert idx == N_DRAWS
        self.wait(0.4)

        # ---- the coin's curve: B(10, 1/2)
        unit = 0.92 / counts.max()
        pts = []
        for k in range(N_SAMPLE + 1):
            h = N_DRAWS * stats.binom.pmf(k, N_SAMPLE, 0.5) * unit
            pts.append(self.hax.c2p(k - 0.5, h))
            pts.append(self.hax.c2p(k + 0.5, h))
        step = VMobject(color=PURPLE, stroke_width=4).set_points_as_corners(pts)
        blab = MathTex(r"B(10,\ \tfrac12)\ \text{— ten fair coins}", color=PURPLE).scale(0.65).move_to(
            self.hax.c2p(9.6, 0.42))
        self.swap_caption("the population was skewed and it did not matter: the count of 'above' is ten fair coins, B(10, ½)",
                          color=PURPLE, font_size=22)
        self.play(Create(step), FadeIn(blab), run_time=1.6)
        self.wait(1.2)

        # ---- price the tails
        p_mid = sum(stats.binom.pmf(k, 10, 0.5) for k in (4, 5, 6))
        p_8up = sum(stats.binom.pmf(k, 10, 0.5) for k in (8, 9, 10))
        p_10 = stats.binom.pmf(10, 10, 0.5)
        tails = VGroup(
            Text(f"4–6, 5–5, 6–4:  {100*p_mid:.0f}% of samples", font=FONT, font_size=20, color=TXT),
            Text(f"8 or more above (8–2, 9–1, 10–0):  {100*p_8up:.1f}%", font=FONT, font_size=20, color=AMBER),
            Text(f"10–0:  {100*p_10:.1f}%  — one in a thousand", font=FONT, font_size=20, color=AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to([4.0, -1.05, 0])
        self.play(FadeOut(crow), FadeIn(tails, lag_ratio=0.3), run_time=1.2)
        self.wait(1.0)
        self.swap_caption("the sign test: count the side, price it with a fair coin — reject only when the split is too lopsided",
                          color=AMBER, font_size=22)
        self.wait(3.0)

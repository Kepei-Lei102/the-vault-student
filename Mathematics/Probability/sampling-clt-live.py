"""The CLT built live from real random draws — date-seeded.

Draw samples of n = 30 from a wildly skewed exponential population,
average each, and drop the mean as a brick into a growing histogram:
the bell assembles itself. Seeded by the generation date (stamped
in-frame); rerun on another day and every brick moves, the bell doesn't.

Render (from this folder):
    VAULT_DATE=YYYY-MM-DD manim -qm sampling-clt-live.py CLTLive   # smoke
    VAULT_DATE=YYYY-MM-DD manim -qk sampling-clt-live.py CLTLive   # 4K final
(Defaults to the committed date if VAULT_DATE is unset.)
Copy the output beside the card as sampling-clt-live.mp4, then clear
media/ + __pycache__/.
"""

import os
import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
AMBER = "#f59e0b"

config.background_color = BG

DATE = os.environ.get("VAULT_DATE", "2026-08-05")
SEED = int(DATE.replace("-", ""))

N = 30            # sample size
N_MEANS = 120     # how many sample means to accumulate
MU, SIGMA = 1.0, 1.0
SE = SIGMA / np.sqrt(N)

BIN_LO, BIN_HI, N_BINS = 0.45, 1.55, 22
BIN_W = (BIN_HI - BIN_LO) / N_BINS


class CLTLive(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=25, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def construct(self):
        rng = np.random.default_rng(SEED)
        samples = rng.exponential(1.0, size=(N_MEANS, N))
        means = samples.mean(axis=1)

        stamp = Text(f"date generated: {DATE}  ·  seed = {SEED}",
                     font_size=20, color=GRAY).to_corner(UR, buff=0.35)

        # population thumbnail, top-left
        pop_ax = Axes(x_range=[0, 4.5, 1], y_range=[0, 1.05, 1],
                      x_length=3.4, y_length=1.7,
                      axis_config=dict(color=GRAY, include_ticks=False,
                                       include_numbers=False)
                      ).to_corner(UL, buff=0.45)
        pop_curve = pop_ax.plot(lambda x: np.exp(-x), x_range=[0, 4.5],
                                color=PURPLE, stroke_width=4)
        pop_label = Text("the population: skewed", font_size=21,
                         color=PURPLE).next_to(pop_ax, DOWN, buff=0.12)

        # histogram axes, main stage
        hist_ax = Axes(x_range=[BIN_LO, BIN_HI, 0.25],
                       y_range=[0, 26, 5],
                       x_length=8.6, y_length=4.0,
                       axis_config=dict(color=GRAY, include_ticks=True,
                                        include_numbers=False),
                       x_axis_config=dict(include_numbers=True,
                                          font_size=22,
                                          decimal_number_config={
                                              "num_decimal_places": 2,
                                              "color": GRAY}),
                       ).shift(RIGHT * 1.3 + DOWN * 0.72)

        counter = Integer(0, font_size=30, color=BLUE).to_corner(UR, buff=0.35
                                                                 ).shift(DOWN * 0.55)
        counter_lab = Text("samples of 30, averaged:", font_size=21, color=BLUE
                           ).next_to(counter, LEFT, buff=0.18)

        self.play(FadeIn(pop_ax), Create(pop_curve), FadeIn(pop_label),
                  FadeIn(hist_ax), FadeIn(stamp),
                  FadeIn(counter), FadeIn(counter_lab), run_time=1.1)
        self.swap_caption("take 30 real random draws — average them — drop the mean in as a brick")

        counts = [0] * N_BINS

        def brick(bin_idx, level):
            x0 = BIN_LO + bin_idx * BIN_W
            p0 = hist_ax.c2p(x0, level)
            p1 = hist_ax.c2p(x0 + BIN_W, level + 1)
            r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1],
                          fill_color=BLUE, fill_opacity=0.65,
                          stroke_color=BLUE, stroke_width=1.2)
            r.move_to((p0 + p1) / 2)
            return r

        def bin_of(m):
            return min(N_BINS - 1, max(0, int((m - BIN_LO) / BIN_W)))

        # first three means: show the sample dots collapsing to their mean
        for k in range(3):
            dots = VGroup(*[Dot(pop_ax.c2p(min(v, 4.4), 0.06), radius=0.035,
                                color=AMBER) for v in samples[k]])
            m = means[k]
            b = bin_of(m)
            self.play(FadeIn(dots, run_time=0.4))
            r = brick(b, counts[b])
            self.play(Transform(dots, r), run_time=0.6)
            counts[b] += 1
            self.play(counter.animate.set_value(k + 1), run_time=0.15)

        self.swap_caption("again and again — every draw real, seeded by today's date")

        # the rest, in accelerating batches
        idx = 3
        for batch in [7, 20, 30, 60]:
            group = VGroup()
            for _ in range(batch):
                if idx >= N_MEANS:
                    break
                b = bin_of(means[idx])
                group.add(brick(b, counts[b]))
                counts[b] += 1
                idx += 1
            self.play(FadeIn(group, lag_ratio=0.06),
                      counter.animate.set_value(idx), run_time=1.6)

        # overlay the CLT's promised bell, scaled to the histogram
        scale = N_MEANS * BIN_W
        bell = hist_ax.plot(
            lambda x: scale * np.exp(-(x - MU) ** 2 / (2 * SE ** 2)) / (SE * np.sqrt(2 * np.pi)),
            x_range=[BIN_LO, BIN_HI], color=GREEN, stroke_width=5)
        self.swap_caption("the bell nobody ordered:  means are N(μ, σ²/30) — whatever the population's shape",
                          color=GREEN)
        self.play(Create(bell), run_time=1.6)
        self.wait(1.8)

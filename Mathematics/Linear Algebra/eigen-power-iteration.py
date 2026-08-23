"""Manim: power iteration — why the biggest eigenvalue owns the long run.

A = (4 -1; 2 1), eigenvalues 3 (rail y = x) and 2 (rail y = 2x). Spawn seven
date-seeded random unit vectors and multiply every one by A, over and over
(renormalising for display — only the direction is being watched). Each step
multiplies the e1-part by 3 and the e2-part by 2, so the mix tilts by (2/3)
per step and every direction swings onto the lambda = 3 rail. One deliberate
exception rides along: a vector started exactly ON the y = 2x rail has no
e1-part to amplify, so it alone never moves — the exception that shows the
mechanism. Punchline: this loop, run on the web's link matrix, is PageRank.

Render (from this folder):
    VAULT_DATE=YYYY-MM-DD manim -qm eigen-power-iteration.py EigenPowerIteration   # smoke
    VAULT_DATE=YYYY-MM-DD manim -qk eigen-power-iteration.py EigenPowerIteration   # 4K final
Copy media/videos/eigen-power-iteration/2160p60/EigenPowerIteration.mp4
  -> eigen-power-iteration.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import os
import numpy as np
from manim import (
    Scene, VGroup, Axes, Text, MathTex, Arrow, DashedLine,
    FadeIn, FadeOut, Transform, Create, Write, UP, DOWN, LEFT, RIGHT, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
TEAL = "#0891b2"
FONT = "Helvetica Neue"

config.background_color = BG

DATE = os.environ.get("VAULT_DATE", "2026-08-20")
SEED = int(DATE.replace("-", ""))

A = np.array([[4.0, -1.0], [2.0, 1.0]])
N_VECTORS = 7
N_STEPS = 6
DISPLAY_LEN = 2.35          # axes-units display length of every arrow


class EigenPowerIteration(Scene):
    def construct(self):
        rng = np.random.default_rng(SEED)

        ax = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=6.4, y_length=6.4,
            axis_config={"color": GREY, "stroke_width": 2,
                         "include_ticks": False, "include_tip": False},
        ).shift(LEFT * 3.4)

        rail1 = DashedLine(ax.c2p(-3, -3), ax.c2p(3, 3), color=AMBER,
                           stroke_width=3, dash_length=0.12)
        rail2 = DashedLine(ax.c2p(-1.5, -3), ax.c2p(1.5, 3), color=TEAL,
                           stroke_width=3, dash_length=0.12)
        r1lab = MathTex(r"y=x,\ \lambda=3", color=AMBER, font_size=34)
        r1lab.move_to(ax.c2p(2.5, 0.55))
        r2lab = MathTex(r"y=2x,\ \lambda=2", color=TEAL, font_size=34)
        r2lab.move_to(ax.c2p(-1.05, 2.72))

        title = Text("Multiply by A. Again. And again.",
                     font=FONT, font_size=34, color=TXT)
        title.move_to(RIGHT * 3.55 + UP * 3.2)

        self.play(Create(ax), run_time=1.0)
        self.play(Create(rail1), Create(rail2),
                  FadeIn(r1lab), FadeIn(r2lab), FadeIn(title), run_time=1.4)

        # --- the vectors: 7 random directions + 1 planted exactly on rail 2
        angles = rng.uniform(0, 2 * np.pi, N_VECTORS)
        vecs = [np.array([np.cos(t), np.sin(t)]) for t in angles]
        vecs.append(np.array([1.0, 2.0]) / np.sqrt(5.0))   # the exception
        colors = [BLUE] * N_VECTORS + [TEAL]

        def arrow_for(v, colr):
            tip = ax.c2p(*(v * DISPLAY_LEN))
            return Arrow(ax.c2p(0, 0), tip, color=colr, buff=0,
                         stroke_width=5, max_tip_length_to_length_ratio=0.09)

        arrows = [arrow_for(v, c) for v, c in zip(vecs, colors)]

        cap1 = Text("Seven random directions —", font=FONT, font_size=27, color=TXT)
        cap2 = Text("and one planted exactly on the teal rail.",
                    font=FONT, font_size=27, color=TEAL)
        cap1.move_to(RIGHT * 3.55 + UP * 2.2)
        cap2.next_to(cap1, DOWN, buff=0.22)

        self.play(*[FadeIn(a) for a in arrows], FadeIn(cap1), FadeIn(cap2),
                  run_time=1.2)
        self.wait(1.2)

        step_lab = Text("step 0", font=FONT, font_size=30, color=AMBER)
        step_lab.move_to(RIGHT * 3.55 + UP * 1.1)
        ratio_lab = MathTex(r"\text{mix of } \lambda=2 \text{ left: } 100\%",
                            color=GREY, font_size=32)
        ratio_lab.move_to(RIGHT * 3.55 + UP * 0.35)
        self.play(FadeIn(step_lab), FadeIn(ratio_lab), run_time=0.6)

        for k in range(1, N_STEPS + 1):
            new_vecs = []
            moves = []
            for i, v in enumerate(vecs):
                w = A @ v
                w = w / np.linalg.norm(w)
                new_vecs.append(w)
                moves.append(Transform(arrows[i], arrow_for(w, colors[i])))
            vecs = new_vecs
            new_step = Text(f"step {k}", font=FONT, font_size=30, color=AMBER)
            new_step.move_to(step_lab.get_center())
            pct = 100.0 * (2.0 / 3.0) ** k
            new_ratio = MathTex(
                r"\text{mix of } \lambda=2 \text{ left: }" + f"{pct:.0f}" + r"\%",
                color=GREY, font_size=32)
            new_ratio.move_to(ratio_lab.get_center())
            self.play(*moves, FadeOut(step_lab), FadeIn(new_step),
                      FadeOut(ratio_lab), FadeIn(new_ratio), run_time=1.15)
            step_lab, ratio_lab = new_step, new_ratio
            self.wait(0.55)

        self.wait(0.8)

        # --- punchlines
        p1 = MathTex(
            r"\mathbf{A}^n\mathbf{x} = c_1 3^n \mathbf{e}_1 + c_2 2^n \mathbf{e}_2",
            color=TXT, font_size=40)
        p2 = Text("The (2/3)-per-step tail dies:", font=FONT, font_size=27, color=TXT)
        p3 = Text("every direction swings onto the biggest", font=FONT,
                  font_size=27, color=AMBER)
        p4 = Text("eigenvalue's rail — except the one that", font=FONT,
                  font_size=27, color=AMBER)
        p5 = Text("started with no e1 in it at all.", font=FONT,
                  font_size=27, color=TEAL)
        panel = VGroup(p1, p2, p3, p4, p5)
        panel.arrange(DOWN, buff=0.24)
        panel.move_to(RIGHT * 3.55 + DOWN * 0.9)

        self.play(FadeOut(cap1), FadeOut(cap2), FadeOut(step_lab),
                  FadeOut(ratio_lab), run_time=0.5)
        self.play(FadeIn(panel), run_time=1.4)
        self.wait(2.6)

        page = Text("This loop, run on the web's link matrix,", font=FONT,
                    font_size=27, color=GREEN)
        page2 = Text("is PageRank — how Google ranks pages.", font=FONT,
                     font_size=27, color=GREEN)
        pg = VGroup(page, page2).arrange(DOWN, buff=0.2)
        pg.move_to(RIGHT * 3.55 + DOWN * 2.9)
        self.play(FadeIn(pg), run_time=1.0)

        stamp = Text(f"seeded by date · {DATE}", font=FONT, font_size=20,
                     color=GREY)
        stamp.to_edge(DOWN, buff=0.25).to_edge(RIGHT, buff=0.35)
        self.play(FadeIn(stamp), run_time=0.5)
        self.wait(3.0)

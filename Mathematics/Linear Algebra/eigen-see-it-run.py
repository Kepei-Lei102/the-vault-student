"""Manim: see it run — one application of the matrix, and two directions refuse to turn.

The opener clip: before any algebra, watch A = (4 -1; 2 1) hit a fan of
date-seeded vectors ONCE (true images, no normalising). Almost every arrow
visibly swings off its line; two planted on y = x and y = 2x do not — they
only stretch, by 3 and by 2. Then the reveal: those are the eigenvectors,
the stretches are the eigenvalues, and the topic is the hunt for them.
"See it run, then learn what drives it."

Render (from this folder):
    VAULT_DATE=YYYY-MM-DD manim -qm eigen-see-it-run.py EigenSeeItRun   # smoke
    VAULT_DATE=YYYY-MM-DD manim -qk eigen-see-it-run.py EigenSeeItRun   # 4K final
Copy media/videos/eigen-see-it-run/2160p60/EigenSeeItRun.mp4
  -> eigen-see-it-run.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import os
import numpy as np
from manim import (
    Scene, VGroup, Axes, Text, MathTex, Arrow, DashedLine,
    FadeIn, FadeOut, Transform, Create, UP, DOWN, LEFT, RIGHT, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
AMBER = "#f59e0b"
TEAL = "#0891b2"
GREEN = "#059669"
FONT = "Helvetica Neue"

config.background_color = BG

DATE = os.environ.get("VAULT_DATE", "2026-08-20")
SEED = int(DATE.replace("-", ""))

A = np.array([[4.0, -1.0], [2.0, 1.0]])
START_LEN = 1.5          # start-vector length in axes units
CAP = 4.7                # display cap for generic images (direction stays true)
RAIL_ANGLES = [np.arctan(1.0), np.arctan(2.0)]


class EigenSeeItRun(Scene):
    def construct(self):
        rng = np.random.default_rng(SEED)

        ax = Axes(
            x_range=[-5.0, 5.0, 1], y_range=[-5.0, 5.0, 1],
            x_length=6.6, y_length=6.6,
            axis_config={"color": GREY, "stroke_width": 2,
                         "include_ticks": False, "include_tip": False},
        ).shift(LEFT * 3.3)

        # --- seeded fan, keeping clear of the two rails so the reveal is crisp
        angles = []
        while len(angles) < 8:
            t = rng.uniform(0, 2 * np.pi)
            if all(min(abs(t - r), abs(t - r - np.pi), abs(t - r + np.pi),
                       abs(t - r - 2 * np.pi)) > 0.30 for r in RAIL_ANGLES):
                angles.append(t)
        vecs = [START_LEN * np.array([np.cos(t), np.sin(t)]) for t in angles]
        e1 = START_LEN * np.array([1.0, 1.0]) / np.sqrt(2.0)   # rail y = x
        e2 = START_LEN * np.array([1.0, 2.0]) / np.sqrt(5.0)   # rail y = 2x
        vecs += [e1, e2]

        def arrow_for(v, colr, width=4.5):
            return Arrow(ax.c2p(0, 0), ax.c2p(*v), color=colr, buff=0,
                         stroke_width=width,
                         max_tip_length_to_length_ratio=0.10)

        arrows = [arrow_for(v, GREY) for v in vecs]

        title = Text("One matrix. Every vector moves.", font=FONT,
                     font_size=31, color=TXT)
        title.move_to(RIGHT * 3.6 + UP * 3.2)
        mat = MathTex(r"\mathbf{A} = \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}",
                      color=TXT, font_size=40)
        mat.move_to(RIGHT * 3.6 + UP * 2.1)

        self.play(Create(ax), FadeIn(title), FadeIn(mat), run_time=1.2)
        self.play(*[FadeIn(a) for a in arrows], run_time=1.0)
        self.wait(1.0)

        go = Text("Multiply every one of them by A:", font=FONT,
                  font_size=27, color=TXT)
        go.move_to(RIGHT * 3.6 + UP * 1.1)
        self.play(FadeIn(go), run_time=0.6)

        def image_of(v):
            w = A @ v
            n = np.linalg.norm(w)
            return w if n <= CAP else w / n * CAP

        moves = [Transform(arrows[i], arrow_for(image_of(v), GREY))
                 for i, v in enumerate(vecs)]
        self.play(*moves, run_time=2.4)
        self.wait(1.2)

        # --- the reveal
        r1 = Text("Almost every direction turned.", font=FONT,
                  font_size=27, color=TXT)
        r2 = Text("Two did not.", font=FONT, font_size=31, color=AMBER)
        r1.move_to(RIGHT * 3.6 + UP * 0.1)
        r2.next_to(r1, DOWN, buff=0.25)
        self.play(FadeIn(r1), run_time=0.8)

        rail1 = DashedLine(ax.c2p(-5.0, -5.0), ax.c2p(5.0, 5.0), color=AMBER,
                           stroke_width=3, dash_length=0.12)
        rail2 = DashedLine(ax.c2p(-2.5, -5.0), ax.c2p(2.5, 5.0), color=TEAL,
                           stroke_width=3, dash_length=0.12)
        hi1 = arrow_for(A @ e1, AMBER, width=6)
        hi2 = arrow_for(A @ e2, TEAL, width=6)
        lab1 = MathTex(r"\text{kept} \times 3", color=AMBER, font_size=36)
        lab1.move_to(ax.c2p(4.05, 2.5))
        lab2 = MathTex(r"\text{kept} \times 2", color=TEAL, font_size=36)
        lab2.move_to(ax.c2p(-2.1, 3.7))
        self.play(FadeIn(r2), Create(rail1), Create(rail2),
                  Transform(arrows[-2], hi1), Transform(arrows[-1], hi2),
                  FadeIn(lab1), FadeIn(lab2), run_time=1.6)
        self.wait(1.6)

        p1 = Text("A direction the matrix keeps", font=FONT, font_size=27,
                  color=TXT)
        p2 = Text("is an eigenvector; its stretch factor", font=FONT,
                  font_size=27, color=TXT)
        p3 = Text("is the eigenvalue.", font=FONT, font_size=27, color=TXT)
        p4 = Text("The hunt for them is this topic.", font=FONT,
                  font_size=27, color=GREEN)
        panel = VGroup(p1, p2, p3, p4).arrange(DOWN, buff=0.22)
        panel.move_to(RIGHT * 3.6 + DOWN * 2.4)
        self.play(FadeIn(panel), run_time=1.2)

        stamp = Text(f"seeded by date · {DATE}", font=FONT, font_size=20,
                     color=GREY)
        stamp.to_edge(DOWN, buff=0.25).to_edge(RIGHT, buff=0.35)
        self.play(FadeIn(stamp), run_time=0.5)
        self.wait(3.0)

"""Flash cell write / read / erase — the electrons' journey.

Renders secondary-storage-flash-cell.mp4 (embed beside the card).
Smoke: manim -qm secondary-storage-flash-cell.py FlashCell
Final: manim -qk secondary-storage-flash-cell.py FlashCell
"""
from manim import *

BLUE_ = "#2563eb"
AMBER = "#f59e0b"
TEAL = "#0891b2"
GREEN = "#059669"
RED_ = "#dc2626"
GRAY = "#9a9a9a"

config.background_color = "#1a1a1a"


class FlashCell(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=28, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap), FadeIn(cap), run_time=0.6)
        else:
            self.play(FadeIn(cap), run_time=0.6)
        self._cap = cap

    def construct(self):
        title = Text("The flash cell — where the electrons flow", font_size=34, color=GRAY)
        title.to_edge(UP, buff=0.3)

        # ---- cell anatomy ----
        substrate = Rectangle(width=11, height=1.7, stroke_color=GRAY, stroke_width=2,
                              fill_color=GRAY, fill_opacity=0.10).move_to([0, -1.75, 0])
        source = Rectangle(width=1.8, height=0.6, stroke_color=GREEN, stroke_width=2,
                           fill_color=GREEN, fill_opacity=0.25).move_to([-4.0, -1.2, 0])
        drain = source.copy().move_to([4.0, -1.2, 0])
        channel = DashedLine([-3.1, -0.92, 0], [3.1, -0.92, 0], color=GREEN, stroke_width=3)
        oxide1 = Rectangle(width=5.0, height=0.28, stroke_color=GRAY, stroke_width=1.5,
                           fill_color=GRAY, fill_opacity=0.25).move_to([0, -0.76, 0])
        fg = Rectangle(width=4.6, height=0.8, stroke_color=AMBER, stroke_width=3,
                       fill_color=AMBER, fill_opacity=0.18).move_to([0, -0.22, 0])
        oxide2 = Rectangle(width=5.0, height=0.2, stroke_color=GRAY, stroke_width=1.5,
                           fill_color=GRAY, fill_opacity=0.25).move_to([0, 0.28, 0])
        cg = Rectangle(width=5.0, height=0.85, stroke_color=BLUE_, stroke_width=3,
                       fill_color=BLUE_, fill_opacity=0.15).move_to([0, 0.805, 0])

        lab_cg = Text("control gate", font_size=26, color=BLUE_).next_to(cg, RIGHT, buff=0.4)
        lab_fg = Text("floating gate", font_size=26, color=AMBER).next_to(fg, RIGHT, buff=0.4)
        lab_ox = Text("tunnel oxide - the wall", font_size=22, color=GRAY)
        lab_ox.next_to(oxide1, RIGHT, buff=0.4)
        lab_src = Text("source", font_size=22, color=GREEN).next_to(source, DOWN, buff=0.15)
        lab_drn = Text("drain", font_size=22, color=GREEN).next_to(drain, DOWN, buff=0.15)
        lab_ch = Text("channel", font_size=22, color=GREEN).move_to([0, -1.35, 0])

        self.play(FadeIn(title), run_time=0.8)
        self.play(
            FadeIn(substrate), FadeIn(source), FadeIn(drain), Create(channel),
            FadeIn(oxide1), FadeIn(fg), FadeIn(oxide2), FadeIn(cg),
            run_time=1.6,
        )
        self.play(
            FadeIn(lab_cg), FadeIn(lab_fg), FadeIn(lab_ox),
            FadeIn(lab_src), FadeIn(lab_drn), FadeIn(lab_ch),
            run_time=1.0,
        )
        self.swap_caption("A transistor with a buried island - insulated on every side.")
        self.wait(2.0)

        # ---- WRITE ----
        self.swap_caption("WRITE - high voltage bends the wall; electrons tunnel through.", AMBER)
        volt = Text("+V", font_size=34, color=AMBER, weight=BOLD).next_to(cg, UP, buff=0.15).shift(LEFT * 2.0)
        self.play(FadeIn(volt), cg.animate.set_fill(BLUE_, opacity=0.35), run_time=0.8)

        xs = [-1.8, -1.1, -0.4, 0.3, 1.0, 1.7]
        electrons = VGroup(*[Dot([x, -1.02, 0], radius=0.09, color=TEAL) for x in xs])
        self.play(FadeIn(electrons), run_time=0.6)

        # tunnel: pause at the wall, flash it, pop through
        anims = []
        for i, e in enumerate(electrons):
            x = xs[i]
            path = VMobject().set_points_smoothly([
                [x, -1.02, 0], [x * 0.95, -0.76, 0], [x * 0.85, -0.22 + (0.12 if i % 2 else -0.12), 0],
            ])
            anims.append(MoveAlongPath(e, path, rate_func=rate_functions.ease_in_out_sine, run_time=1.6))
        self.play(
            AnimationGroup(*anims, lag_ratio=0.15),
            Succession(
                oxide1.animate(run_time=0.5).set_fill(RED_, opacity=0.45),
                oxide1.animate(run_time=1.5).set_fill(GRAY, opacity=0.25),
            ),
        )
        self.play(FadeOut(volt), cg.animate.set_fill(BLUE_, opacity=0.15), run_time=0.7)
        self.swap_caption("Remove the voltage - the wall snaps shut. The charge just stays.")
        self.wait(2.0)

        # ---- READ (charged) ----
        self.swap_caption("READ - a gentle voltage asks: does the transistor switch on?", BLUE_)
        rv = Text("read V", font_size=26, color=BLUE_).next_to(cg, UP, buff=0.15).shift(LEFT * 2.0)
        self.play(FadeIn(rv), run_time=0.6)

        probes = VGroup(*[Dot([-4.0 - 0.3 * i, -0.92, 0], radius=0.07, color=GREEN) for i in range(3)])
        self.play(FadeIn(probes), run_time=0.4)
        self.play(probes.animate.shift(RIGHT * 1.6), run_time=0.9)
        cross = VGroup(
            Line([-0.4, -1.3, 0], [0.4, -0.55, 0], color=RED_, stroke_width=7),
            Line([-0.4, -0.55, 0], [0.4, -1.3, 0], color=RED_, stroke_width=7),
        )
        self.play(FadeIn(cross), probes.animate.shift(LEFT * 0.9), run_time=0.8)
        verdict0 = Text("read as 0", font_size=40, color=BLUE_, weight=BOLD).move_to([5.35, 2.3, 0])
        self.play(FadeIn(verdict0), run_time=0.6)
        self.swap_caption("The island's charge pushes back - no channel forms. No current: 0.", BLUE_)
        self.wait(2.2)
        self.play(FadeOut(probes), FadeOut(cross), FadeOut(rv), FadeOut(verdict0), run_time=0.7)

        # ---- ERASE ----
        self.swap_caption("ERASE - reverse the field: the island is flushed. A whole block at once.", AMBER)
        volt2 = Text("-V", font_size=34, color=AMBER, weight=BOLD).next_to(cg, UP, buff=0.15).shift(LEFT * 2.0)
        self.play(FadeIn(volt2), run_time=0.6)
        anims = []
        for i, e in enumerate(electrons):
            x = xs[i] * 0.85
            path = VMobject().set_points_smoothly([
                e.get_center(), [x, -0.76, 0], [x + (0.6 if x > 0 else -0.6), -1.05, 0],
            ])
            anims.append(MoveAlongPath(e, path, rate_func=rate_functions.ease_in_out_sine, run_time=1.4))
        self.play(
            AnimationGroup(*anims, lag_ratio=0.12),
            Succession(
                oxide1.animate(run_time=0.5).set_fill(RED_, opacity=0.45),
                oxide1.animate(run_time=1.3).set_fill(GRAY, opacity=0.25),
            ),
        )
        self.play(FadeOut(electrons), FadeOut(volt2), run_time=0.8)
        self.wait(1.2)

        # ---- READ (empty) ----
        self.swap_caption("READ again - island empty, the channel forms, current flows: 1.", GREEN)
        rv2 = Text("read V", font_size=26, color=BLUE_).next_to(cg, UP, buff=0.15).shift(LEFT * 2.0)
        glow = Line([-3.1, -0.92, 0], [3.1, -0.92, 0], color=GREEN, stroke_width=6)
        self.play(FadeIn(rv2), Create(glow), run_time=0.8)
        flow = VGroup(*[Dot([-4.2 - 0.5 * i, -0.92, 0], radius=0.07, color=GREEN) for i in range(5)])
        self.add(flow)
        self.play(flow.animate.shift(RIGHT * 8.6), run_time=2.2, rate_func=linear)
        verdict1 = Text("read as 1", font_size=40, color=GREEN, weight=BOLD).move_to([5.35, 2.3, 0])
        self.play(FadeIn(verdict1), FadeOut(flow), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(rv2), FadeOut(glow), FadeOut(verdict1), run_time=0.7)

        # ---- closing ----
        self.swap_caption("The island has no wires. The charge is invisible -")
        self.wait(1.4)
        self.swap_caption("but the transistor's switching point betrays it.")
        self.wait(2.5)

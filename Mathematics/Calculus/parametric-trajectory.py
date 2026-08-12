"""
Parametric Differentiation — How x(t) and y(t) move together to trace a curve.

Stack: Manim Community Edition (vault Manim track).
Total runtime: ~35 seconds.
Three synchronized panels: x(t) | (x,y) trajectory | y(t).

Two demonstrations:
  Scene 1: Circle x = cos t, y = sin t — calibration case
  Scene 2: Cycloid x = t - sin t, y = 1 - cos t — the dramatic case with a cusp

To render (from this directory):
    manim -qk parametric-trajectory.py ParametricTrajectory   # 2160p60 (4K) showcase
    manim -qh parametric-trajectory.py ParametricTrajectory   # 1080p60 review
    manim -qm parametric-trajectory.py ParametricTrajectory   # 720p30  iteration
"""

from manim import *
import numpy as np

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG      = "#1e1e1e"
TXT     = "#cccccc"
TXT_DIM = "#888888"
BLUE    = "#2563eb"
RED     = "#dc2626"
GREEN   = "#059669"
AMBER   = "#f59e0b"
GREY    = "#888888"
PURPLE  = "#7c3aed"

config.background_color = BG
config.frame_width = 14.222
config.frame_height = 8


def title_card(text, color=TXT, size=40):
    return Text(text, color=color, font_size=size, weight=BOLD)


def body(text, color=TXT, size=24):
    return Text(text, color=color, font_size=size)


def small(text, color=TXT_DIM, size=20):
    return Text(text, color=color, font_size=size)


class ParametricTrajectory(Scene):
    def construct(self):
        self.scene1_intro_circle()
        self.scene2_cycloid()

    # =========================================================
    # SCENE 1 — Circle calibration (~16 s)
    # =========================================================
    def scene1_intro_circle(self):
        # Title
        title = title_card("Parametric Differentiation").to_edge(UP, buff=0.3)
        sub = small("how x(t) and y(t) move together to trace a curve").next_to(title, DOWN, buff=0.15)

        # Equation banner
        eq = MathTex(
            r"x = \cos t, \quad y = \sin t",
            color=TXT, font_size=32
        ).next_to(sub, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(sub))
        self.play(FadeIn(eq))
        self.wait(0.5)

        # Three panels at y ≈ -1
        panel_y = -1.0
        panel_width = 3.6
        panel_height = 3.0

        # x(t) panel (left)
        ax_x = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.4, 1.4, 1],
            x_length=panel_width,
            y_length=panel_height,
            axis_config={"color": GREY, "stroke_width": 1.5, "include_tip": False},
        ).move_to([-4.7, panel_y, 0])
        label_x = small("x(t)", color=BLUE, size=22).next_to(ax_x, UP, buff=0.1)
        t_label_x = small("t", color=TXT_DIM, size=18).next_to(ax_x.x_axis, RIGHT, buff=0.1)

        # y(t) panel (right)
        ax_y = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.4, 1.4, 1],
            x_length=panel_width,
            y_length=panel_height,
            axis_config={"color": GREY, "stroke_width": 1.5, "include_tip": False},
        ).move_to([4.7, panel_y, 0])
        label_y = small("y(t)", color=GREEN, size=22).next_to(ax_y, UP, buff=0.1)
        t_label_y = small("t", color=TXT_DIM, size=18).next_to(ax_y.x_axis, RIGHT, buff=0.1)

        # (x, y) trajectory panel (center, slightly larger)
        ax_xy = Axes(
            x_range=[-1.4, 1.4, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=3.4,
            y_length=3.4,
            axis_config={"color": GREY, "stroke_width": 1.5, "include_tip": False},
        ).move_to([0, panel_y, 0])
        label_xy = small("(x, y)", color=AMBER, size=22).next_to(ax_xy, UP, buff=0.1)

        self.play(
            FadeIn(ax_x), FadeIn(label_x), FadeIn(t_label_x),
            FadeIn(ax_y), FadeIn(label_y), FadeIn(t_label_y),
            FadeIn(ax_xy), FadeIn(label_xy),
        )

        # Define the parametric circle
        def x_func(t):
            return np.cos(t)

        def y_func(t):
            return np.sin(t)

        # Value tracker for t
        t_tracker = ValueTracker(0.0)

        # Moving dots, always redrawn from the tracker
        dot_x = always_redraw(lambda: Dot(
            ax_x.c2p(t_tracker.get_value(), x_func(t_tracker.get_value())),
            color=BLUE, radius=0.07,
        ))
        dot_y = always_redraw(lambda: Dot(
            ax_y.c2p(t_tracker.get_value(), y_func(t_tracker.get_value())),
            color=GREEN, radius=0.07,
        ))
        dot_xy = always_redraw(lambda: Dot(
            ax_xy.c2p(x_func(t_tracker.get_value()), y_func(t_tracker.get_value())),
            color=AMBER, radius=0.09,
        ))

        # Traced paths
        trace_x = TracedPath(dot_x.get_center, stroke_color=BLUE, stroke_width=3)
        trace_y = TracedPath(dot_y.get_center, stroke_color=GREEN, stroke_width=3)
        trace_xy = TracedPath(dot_xy.get_center, stroke_color=AMBER, stroke_width=3)

        # t indicator at bottom
        t_display = always_redraw(lambda: MathTex(
            r"t = " + f"{t_tracker.get_value():.2f}",
            color=TXT, font_size=28,
        ).move_to([0, -3.2, 0]))

        self.add(trace_x, trace_y, trace_xy, dot_x, dot_y, dot_xy, t_display)

        # Animate t from 0 to 2π
        self.play(t_tracker.animate.set_value(2 * PI), run_time=10, rate_func=linear)
        self.wait(0.7)

        # Highlight: at this final point, the velocity vector is tangent
        scene1_objects = VGroup(
            title, sub, eq,
            ax_x, label_x, t_label_x,
            ax_y, label_y, t_label_y,
            ax_xy, label_xy,
            trace_x, trace_y, trace_xy,
            dot_x, dot_y, dot_xy,
            t_display,
        )
        self.play(FadeOut(scene1_objects), run_time=0.8)
        self.wait(0.2)

    # =========================================================
    # SCENE 2 — Cycloid (~16 s)
    # =========================================================
    def scene2_cycloid(self):
        # Title
        title = title_card("The Cycloid").to_edge(UP, buff=0.3)
        sub = small("a point on a rolling circle — cusps where dx/dt = 0").next_to(title, DOWN, buff=0.15)
        eq = MathTex(
            r"x = t - \sin t, \quad y = 1 - \cos t",
            color=TXT, font_size=32,
        ).next_to(sub, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(sub), FadeIn(eq))
        self.wait(0.5)

        # Three panels (same layout as scene 1)
        panel_y = -1.0
        panel_width = 3.6
        panel_height = 3.0

        ax_x = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-0.5, 4 * PI + 0.5, PI],
            x_length=panel_width,
            y_length=panel_height,
            axis_config={"color": GREY, "stroke_width": 1.5, "include_tip": False},
        ).move_to([-4.7, panel_y, 0])
        label_x = small("x(t)", color=BLUE, size=22).next_to(ax_x, UP, buff=0.1)

        ax_y = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-0.3, 2.3, 1],
            x_length=panel_width,
            y_length=panel_height,
            axis_config={"color": GREY, "stroke_width": 1.5, "include_tip": False},
        ).move_to([4.7, panel_y, 0])
        label_y = small("y(t)", color=GREEN, size=22).next_to(ax_y, UP, buff=0.1)

        ax_xy = Axes(
            x_range=[-0.5, 4 * PI + 0.5, PI],
            y_range=[-0.3, 2.3, 1],
            x_length=4.4,
            y_length=2.0,
            axis_config={"color": GREY, "stroke_width": 1.5, "include_tip": False},
        ).move_to([0, panel_y - 0.4, 0])
        label_xy = small("(x, y)", color=AMBER, size=22).next_to(ax_xy, UP, buff=0.1)

        self.play(
            FadeIn(ax_x), FadeIn(label_x),
            FadeIn(ax_y), FadeIn(label_y),
            FadeIn(ax_xy), FadeIn(label_xy),
        )

        # Cycloid functions
        def x_func(t):
            return t - np.sin(t)

        def y_func(t):
            return 1.0 - np.cos(t)

        # Tracker
        t_tracker = ValueTracker(0.0)

        dot_x = always_redraw(lambda: Dot(
            ax_x.c2p(t_tracker.get_value(), x_func(t_tracker.get_value())),
            color=BLUE, radius=0.07,
        ))
        dot_y = always_redraw(lambda: Dot(
            ax_y.c2p(t_tracker.get_value(), y_func(t_tracker.get_value())),
            color=GREEN, radius=0.07,
        ))
        dot_xy = always_redraw(lambda: Dot(
            ax_xy.c2p(x_func(t_tracker.get_value()), y_func(t_tracker.get_value())),
            color=AMBER, radius=0.09,
        ))

        trace_x = TracedPath(dot_x.get_center, stroke_color=BLUE, stroke_width=3)
        trace_y = TracedPath(dot_y.get_center, stroke_color=GREEN, stroke_width=3)
        trace_xy = TracedPath(dot_xy.get_center, stroke_color=AMBER, stroke_width=3)

        t_display = always_redraw(lambda: MathTex(
            r"t = " + f"{t_tracker.get_value():.2f}",
            color=TXT, font_size=28,
        ).move_to([0, -3.4, 0]))

        self.add(trace_x, trace_y, trace_xy, dot_x, dot_y, dot_xy, t_display)

        # Animate over two full revolutions to show the repetition + cusps
        self.play(t_tracker.animate.set_value(4 * PI), run_time=12, rate_func=linear)
        self.wait(1.0)

        # Punchline: at t = 0, 2π, 4π, the dot is briefly stationary horizontally — cusps
        cusp_note = body(
            "At every cusp: dx/dt = 0  →  vertical tangent",
            color=AMBER, size=22,
        ).move_to([0, -3.4, 0])

        self.play(FadeOut(t_display), FadeIn(cusp_note))
        self.wait(2.5)

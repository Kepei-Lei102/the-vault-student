"""Manim scene for [[Planes in 3D]].

ShadowReading -- the r.n = p idea in motion: every point of the plane
2x + y + 2z = 6 projects to the SAME mark (2) on the normal axis; a point
off the plane projects to a different mark, and the gap IS the distance.

Render (on Kepei's Mac, from this directory):
  manim -qk planes-in-3d-shadow.py ShadowReading
  cp media/videos/planes-in-3d-shadow/2160p60/ShadowReading.mp4 planes-in-3d-shadow.mp4
  rm -rf media
"""

from manim import *
import numpy as np

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG       = "#1e1e1e"
TXT      = "#cccccc"
TXT_DIM  = "#888888"
BLUE     = "#2563eb"
GREEN    = "#059669"
AMBER    = "#f59e0b"
GREY     = "#888888"
RED      = "#dc2626"
TEAL     = "#0891b2"
MAGENTA  = "#cc0066"

config.background_color = BG

N = np.array([2.0, 1.0, 2.0])
NHAT = N / 3.0
SCALE = 0.62
CENTER = np.array([1.2, 1.8, 1.2])


def W(p):
    """world -> scene coordinates."""
    return (np.array(p, dtype=float) - CENTER) * SCALE


def plane_point(y, z):
    return np.array([(6.0 - y - 2.0 * z) / 2.0, y, z])


class ShadowReading(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-50 * DEGREES,
                                    zoom=1.05)

        # --- the plane -------------------------------------------------
        plane = Surface(
            lambda u, v: W(plane_point(u, v)),
            u_range=[-0.8, 6.2], v_range=[-0.6, 3.2],
            resolution=(14, 14), fill_opacity=0.35,
            checkerboard_colors=[BLUE, BLUE], stroke_width=0,
        )
        plane.set_fill(BLUE, opacity=0.35)

        # --- the flagpole (normal axis through the origin) -------------
        pole = Line3D(W(-1.2 * NHAT), W(6.6 * NHAT), color=GREY,
                      thickness=0.012)

        title = MathTex(r"\Pi:\ 2x + y + 2z = 6,\qquad \mathbf{n} = (2,1,2)",
                        font_size=40, color=TXT)
        title.to_edge(UP, buff=0.35)
        self.add_fixed_in_frame_mobjects(title)

        self.play(Create(plane), run_time=1.6)
        self.play(Create(pole), run_time=0.9)
        pole_lab = MathTex(r"\hat{\mathbf{n}}", font_size=36, color=TXT_DIM)
        pole_lab.to_corner(UR, buff=1.1).shift(DOWN * 0.6)
        self.add_fixed_in_frame_mobjects(pole_lab)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.wait(0.6)

        # --- three points project to ONE mark --------------------------
        mark2 = W(2 * NHAT)
        pts = [np.array([3.0, 0, 0]), np.array([0, 0, 3.0]),
               np.array([1.0, 2.0, 1.0])]
        cap1 = Text("three different points of the plane...",
                    font_size=26, color=TXT)
        cap1.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(cap1)

        dots = VGroup(*[Dot3D(W(p), color=TEAL, radius=0.07) for p in pts])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.3),
                  run_time=1.3)
        self.wait(0.8)

        cap2 = Text("...one shared shadow on the normal axis: the mark 2",
                    font_size=26, color=GREEN)
        cap2.to_edge(DOWN, buff=0.4)
        markdot = Dot3D(mark2, color=GREEN, radius=0.09)
        proj = VGroup(*[DashedLine(W(p), mark2, color=TEAL,
                                   stroke_width=2.5) for p in pts])
        self.play(FadeOut(cap1), run_time=0.3)
        self.add_fixed_in_frame_mobjects(cap2)
        self.play(FadeIn(cap2), run_time=0.4)
        for line in proj:
            self.play(Create(line), run_time=0.9)
        self.play(FadeIn(markdot), Flash(markdot, color=GREEN,
                  line_length=0.18), run_time=0.9)
        eq = MathTex(r"\mathbf{r}\cdot\hat{\mathbf{n}} = \tfrac{6}{3} = 2"
                     r"\ \text{ for every point of }\Pi",
                     font_size=36, color=GREEN)
        eq.to_edge(DOWN, buff=1.05)
        self.add_fixed_in_frame_mobjects(eq)
        self.play(FadeIn(eq), run_time=0.7)
        self.wait(2.4)

        # --- a point OFF the plane -------------------------------------
        self.play(FadeOut(cap2), FadeOut(eq), run_time=0.5)
        P = np.array([3.0, 3.0, 3.0])
        F = np.array([1.0, 2.0, 1.0])
        mark5 = W(5 * NHAT)
        Pdot = Dot3D(W(P), color=RED, radius=0.09)
        cap3 = Text("a point OFF the plane shadows at mark 5",
                    font_size=26, color=TXT)
        cap3.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(cap3)
        self.play(FadeIn(Pdot), FadeIn(cap3), run_time=0.8)
        projP = DashedLine(W(P), mark5, color=RED, stroke_width=2.5)
        m5 = Dot3D(mark5, color=RED, radius=0.08)
        self.play(Create(projP), FadeIn(m5), run_time=1.1)
        self.wait(1.2)

        walk = Line3D(W(P), W(F), color=MAGENTA, thickness=0.022)
        cap4 = MathTex(r"\text{distance} = \text{shadow gap} = 5 - 2 = 3",
                       font_size=38, color=MAGENTA)
        cap4.to_edge(DOWN, buff=1.0)
        self.play(FadeOut(cap3), run_time=0.3)
        self.add_fixed_in_frame_mobjects(cap4)
        self.play(Create(walk), FadeIn(cap4), run_time=1.3)
        self.wait(2.6)

        closing = MathTex(
            r"\operatorname{dist}(P,\Pi) = \frac{\lvert\mathbf{a}\cdot\mathbf{n} - p\rvert}{\lvert\mathbf{n}\rvert}",
            font_size=42, color=AMBER)
        closing.to_edge(DOWN, buff=0.5)
        self.play(FadeOut(cap4), run_time=0.4)
        self.add_fixed_in_frame_mobjects(closing)
        self.play(FadeIn(closing), run_time=0.8)
        self.wait(3.2)
        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(m) for m in
                    [plane, pole, dots, proj, markdot, Pdot, projP, m5,
                     walk, title, pole_lab, closing]], run_time=0.9)

"""Manim: the ribbon and the shadow — why a surface of revolution is ∫ 2πy ds.

Act 1  Spin the curve about the x-axis: every point on it sweeps a hoop of
       radius y, circumference 2πy.
Act 2  One tilted sliver, swung round: a thin band — a slice of a cone, not a
       cylinder. Its area is circumference × width = 2πy × Δs, and Δs is the
       slant; the shadow cylinder 2πy × Δx sits inside it, narrower, always.
Act 3  The cone test: y = 0.75x for 0 ≤ x ≤ 2 (r = 1.5, h = 2, slant l = 2.5,
       a 3-4-5 triangle). Unrolled, the cone is a sector of radius l whose arc
       is the base circumference 2πr: area ½ l² (2πr/l) = π r l = 11.78.
       ∫ 2πy ds gives π r l ✓ ; ∫ 2πy dx gives π r h = 9.42 ✗ — 20 % short,
       and no number of slices repairs it.

Every point is computed from f; nothing is placed by eye.

Render (from this folder):
    manim -ql surface-revolution-ribbon.py SurfaceRibbon    # smoke (480p15)
    manim -qk surface-revolution-ribbon.py SurfaceRibbon    # 4K final
Copy media/videos/surface-revolution-ribbon/2160p60/SurfaceRibbon.mp4
  -> surface-revolution-ribbon.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import numpy as np
from manim import (
    ThreeDScene, VGroup, Text, MathTex, Surface, ParametricFunction, DashedLine,
    Dot3D, Line, Sector, Arc, ValueTracker, always_redraw,
    FadeIn, FadeOut, Create, Transform, Write,
    UP, DOWN, LEFT, RIGHT, DEGREES, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"      # the curve / the surface
BLUE_DK = "#1d4ed8"
GREEN = "#059669"     # the sliver, ds, the truth
AMBER = "#f59e0b"     # dx, the band
RED = "#dc2626"       # dy, the shadow, the wrong formula
FONT = "Helvetica Neue"

config.background_color = BG

# ---------------------------------------------------------------- the curve
A, B = 0.0, 3.0
S_ = 1.25               # world units per data unit (Acts 1–2)
X_OFF = -4.3            # data x = 0 sits here in world x


def f(x):
    return 0.75 + 0.45 * np.sin(1.7 * x - 0.6) + 0.04 * x


def fp(x):
    return 0.765 * np.cos(1.7 * x - 0.6) + 0.04


def W(u, y, z):
    """data (x, y, z) -> world point (axis of rotation = world x)"""
    return np.array([X_OFF + S_ * u, S_ * y, S_ * z])


X0, DX = 0.5, 0.35      # the sliver magnified in Act 2
XH = 1.8                # the point whose hoop we trace in Act 1

# ---------------------------------------------------------------- the cone
R_C, H_C = 1.5, 2.0
L_C = float(np.hypot(R_C, H_C))           # 2.5 — a 3-4-5 triangle
S_C = 0.95
XC_OFF = -4.1


def WC(u, y, z):
    return np.array([XC_OFF + S_C * u, S_C * y, S_C * z])


def note(s, size=24, color=GREY):
    return Text(s, font=FONT, font_size=size, color=color)


class SurfaceRibbon(ThreeDScene):
    def fixed(self, *ms):
        """register 2-D overlays, start them invisible"""
        self.add_fixed_in_frame_mobjects(*ms)
        for m in ms:
            m.set_opacity(0)

    def construct(self):
        self.set_camera_orientation(phi=72 * DEGREES, theta=-68 * DEGREES, zoom=1.25,
                                    frame_center=np.array([0.1, 0.0, 1.2]))

        # ---------------------------------------------------------- overlays
        title = Text("Surface of revolution — the ribbon, not the shadow",
                     font=FONT, font_size=32, color=TXT).to_edge(UP, buff=0.3)
        cap1 = note("spin the curve y = f(x) about the x-axis: every point sweeps a hoop of radius y", 24, TXT)
        cap2 = note("one tilted sliver, swung round: a thin band — a slice of a cone, not a cylinder", 24, TXT)
        cap3 = note("the cone test: y = 0.75x for 0 ≤ x ≤ 2  (r = 1.5, h = 2, slant l = 2.5)", 24, TXT)
        for c in (cap1, cap2, cap3):
            c.to_edge(DOWN, buff=0.4)
        self.fixed(title, cap1, cap2, cap3)

        # ------------------------------------------------------------ Act 1
        axis = DashedLine(W(-0.3, 0, 0), W(3.4, 0, 0), color=GREY, stroke_width=2, dash_length=0.12)
        curve = ParametricFunction(lambda t: W(t, f(t), 0), t_range=[A, B], color=BLUE, stroke_width=5)
        self.add(axis)
        self.play(title.animate.set_opacity(1), Create(curve), run_time=1.4)
        self.play(cap1.animate.set_opacity(1), run_time=0.5)

        th = ValueTracker(0.001)
        surf = always_redraw(lambda: Surface(
            lambda u, v: W(u, f(u) * np.cos(v), f(u) * np.sin(v)),
            u_range=[A, B], v_range=[0, th.get_value()],
            resolution=(24, 18), fill_opacity=0.32,
            checkerboard_colors=[BLUE, BLUE_DK], stroke_color=BLUE, stroke_width=0.4))
        spin = always_redraw(lambda: ParametricFunction(
            lambda t: W(t, f(t) * np.cos(th.get_value()), f(t) * np.sin(th.get_value())),
            t_range=[A, B], color=BLUE, stroke_width=4))
        hoop = always_redraw(lambda: ParametricFunction(
            lambda v: W(XH, f(XH) * np.cos(v), f(XH) * np.sin(v)),
            t_range=[0, th.get_value()], color=AMBER, stroke_width=5))
        bead = always_redraw(lambda: Dot3D(
            W(XH, f(XH) * np.cos(th.get_value()), f(XH) * np.sin(th.get_value())),
            radius=0.07, color=AMBER))
        radius_line = always_redraw(lambda: Line(
            W(XH, 0, 0), W(XH, f(XH) * np.cos(th.get_value()), f(XH) * np.sin(th.get_value())),
            color=AMBER, stroke_width=2))

        hoop_lab = VGroup(
            note("the hoop: radius y,", 24, AMBER),
            note("circumference 2πy", 24, AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).to_edge(RIGHT, buff=0.8).shift(UP * 1.6)
        self.fixed(hoop_lab)

        self.add(surf, spin, hoop, bead, radius_line)
        self.play(th.animate.set_value(2 * np.pi), hoop_lab.animate.set_opacity(1),
                  run_time=4.5)
        self.wait(0.8)

        # ------------------------------------------------------------ Act 2
        for m in (surf, spin, hoop, bead, radius_line):
            m.clear_updaters()
        self.play(cap1.animate.set_opacity(0), cap2.animate.set_opacity(1),
                  hoop_lab.animate.set_opacity(0),
                  FadeOut(hoop), FadeOut(bead), FadeOut(radius_line), FadeOut(spin),
                  surf.animate.set_fill(opacity=0.10).set_stroke(opacity=0.25),
                  run_time=1.0)
        self.remove(surf)
        ghost = Surface(lambda u, v: W(u, f(u) * np.cos(v), f(u) * np.sin(v)),
                        u_range=[A, B], v_range=[0, 2 * np.pi], resolution=(24, 36),
                        fill_opacity=0.08, checkerboard_colors=[BLUE, BLUE_DK],
                        stroke_color=BLUE, stroke_width=0.3, stroke_opacity=0.25)
        self.add(ghost)

        sliver = ParametricFunction(lambda t: W(t, f(t), 0), t_range=[X0, X0 + DX],
                                    color=GREEN, stroke_width=9)
        band = Surface(lambda u, v: W(u, f(u) * np.cos(v), f(u) * np.sin(v)),
                       u_range=[X0, X0 + DX], v_range=[0, 2 * np.pi], resolution=(6, 48),
                       fill_opacity=0.75, checkerboard_colors=[AMBER, "#d97706"],
                       stroke_color=AMBER, stroke_width=0.4)
        self.play(Create(sliver), run_time=0.8)
        self.play(FadeIn(band), run_time=1.2)

        rhs = VGroup(
            note("area of the band", 26, TXT),
            note("≈ circumference × width", 26, TXT),
            MathTex(r"= 2\pi y \times \Delta s", font_size=44, color=GREEN),
            note("Δs runs along the slant —", 24, GREY),
            note("the sliver is tilted, so the band flares", 24, GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_edge(RIGHT, buff=0.7).shift(UP * 1.2)
        self.fixed(rhs)
        self.play(rhs.animate.set_opacity(1), run_time=1.0)
        self.wait(1.4)

        # the shadow: a cylinder of radius y(x0) and width Δx, sitting inside the band
        shadow = Surface(lambda u, v: W(u, f(X0) * np.cos(v), f(X0) * np.sin(v)),
                         u_range=[X0, X0 + DX], v_range=[0, 2 * np.pi], resolution=(4, 48),
                         fill_opacity=0.85, checkerboard_colors=[RED, "#b91c1c"],
                         stroke_color=RED, stroke_width=0.4)
        shadow_lab = VGroup(
            MathTex(r"2\pi y \times \Delta x", font_size=44, color=RED),
            note("is the shadow: the cylinder you'd get", 24, GREY),
            note("if the sliver were flat — it fits inside", 24, GREY),
            note("the real band, narrower, always", 24, GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(rhs, DOWN, buff=0.5).align_to(rhs, LEFT)
        self.fixed(shadow_lab)
        self.play(FadeIn(shadow), band.animate.set_fill(opacity=0.35),
                  shadow_lab.animate.set_opacity(1), run_time=1.2)
        self.wait(1.0)

        # 2-D inset: the sliver triangle, computed from f
        dy = f(X0 + DX) - f(X0)
        k = 1.2 / DX                         # screen units per data unit for the inset
        O = np.array([1.0, -2.85, 0.0])
        P = O + np.array([k * DX, 0, 0])
        Q = O + np.array([k * DX, k * dy, 0])
        tri = VGroup(
            Line(O, P, color=AMBER, stroke_width=5),
            Line(P, Q, color=RED, stroke_width=5),
            Line(O, Q, color=GREEN, stroke_width=5),
            MathTex(r"\Delta x", color=AMBER, font_size=34).next_to((O + P) / 2, DOWN, buff=0.12),
            MathTex(r"\Delta y", color=RED, font_size=34).next_to((P + Q) / 2, RIGHT, buff=0.12),
            MathTex(r"\Delta s", color=GREEN, font_size=34).move_to((O + Q) / 2 + np.array([-0.4, 0.3, 0])),
        )
        tri_note = VGroup(
            note("the band's width is the slant:", 20, TXT),
            MathTex(r"\Delta s = \sqrt{\Delta x^{2} + \Delta y^{2}} > \Delta x", font_size=30, color=TXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).next_to(tri, RIGHT, buff=0.45).align_to(tri, DOWN)
        self.fixed(tri, tri_note)
        self.play(tri.animate.set_opacity(1), tri_note.animate.set_opacity(1), run_time=1.0)
        self.wait(2.2)

        # ------------------------------------------------------------ Act 3
        self.play(FadeOut(ghost), FadeOut(band), FadeOut(shadow), FadeOut(sliver), FadeOut(curve),
                  FadeOut(axis), rhs.animate.set_opacity(0), shadow_lab.animate.set_opacity(0),
                  tri.animate.set_opacity(0), tri_note.animate.set_opacity(0),
                  cap2.animate.set_opacity(0), cap3.animate.set_opacity(1), run_time=1.2)
        self.remove(rhs, shadow_lab, tri, tri_note)

        axis_c = DashedLine(WC(-0.3, 0, 0), WC(2.6, 0, 0), color=GREY, stroke_width=2, dash_length=0.12)
        gen = ParametricFunction(lambda t: WC(t, 0.75 * t, 0), t_range=[0, H_C], color=BLUE, stroke_width=5)
        thc = ValueTracker(0.001)
        cone = always_redraw(lambda: Surface(
            lambda u, v: WC(u, 0.75 * u * np.cos(v), 0.75 * u * np.sin(v)),
            u_range=[0, H_C], v_range=[0, thc.get_value()],
            resolution=(12, 18), fill_opacity=0.35,
            checkerboard_colors=[BLUE, BLUE_DK], stroke_color=BLUE, stroke_width=0.4))
        spin_c = always_redraw(lambda: ParametricFunction(
            lambda t: WC(t, 0.75 * t * np.cos(thc.get_value()), 0.75 * t * np.sin(thc.get_value())),
            t_range=[0, H_C], color=BLUE, stroke_width=4))
        self.add(axis_c)
        self.play(Create(gen), run_time=0.7)
        self.add(cone, spin_c)
        self.play(thc.animate.set_value(2 * np.pi), run_time=2.2)
        cone.clear_updaters(); spin_c.clear_updaters()

        # unrolled: a sector of radius l whose arc is the base circumference 2πr
        ang = 2 * np.pi * R_C / L_C                  # 216°
        rad = 0.95
        sec_center = np.array([3.6, 2.0, 0.0])
        sa = np.pi / 2 - ang / 2                      # fan centred on "up"
        sector = Sector(radius=rad, angle=ang, start_angle=sa, arc_center=sec_center,
                        fill_color=BLUE, fill_opacity=0.3, stroke_color=BLUE, stroke_width=2)
        arc = Arc(radius=rad, angle=ang, start_angle=sa, arc_center=sec_center,
                  color=AMBER, stroke_width=5)
        rim = Line(sec_center, sec_center + rad * np.array([np.cos(sa), np.sin(sa), 0]),
                   color=GREEN, stroke_width=4)
        unroll = VGroup(
            note("unroll the cone: a sector of radius l", 20, GREY),
            note("whose arc is the base rim, 2πr", 20, GREY),
            MathTex(r"\text{area} = \tfrac12 l^{2}\cdot\tfrac{2\pi r}{l} = \pi r l", font_size=34, color=TXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        unroll.next_to(sector, DOWN, buff=0.25).set_x(sec_center[0])
        sec_group = VGroup(sector, arc, rim,
                           MathTex("l", color=GREEN, font_size=34).next_to(rim.get_center(), DOWN, buff=0.12),
                           MathTex(r"2\pi r", color=AMBER, font_size=34).next_to(arc.point_from_proportion(0.5), UP, buff=0.1))
        self.add_fixed_in_frame_mobjects(sec_group, unroll)
        self.remove(sec_group, unroll)
        self.play(FadeIn(sec_group), FadeIn(unroll), run_time=1.2)
        self.wait(1.2)

        truth = float(np.pi * R_C * L_C)
        wrong = float(np.pi * R_C * H_C)
        verdict = VGroup(
            MathTex(r"\int 2\pi y\,ds = \pi r l = " + f"{truth:.2f}" + r"\ \checkmark", font_size=36, color=GREEN),
            MathTex(r"\int 2\pi y\,dx = \pi r h = " + f"{wrong:.2f}" + r"\ \times", font_size=36, color=RED),
            note(f"{100 * (1 - wrong / truth):.0f}% short — and more slices never repair it:", 20, GREY),
            note("on every slice the shadow is shorter than the ribbon", 20, GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        verdict.next_to(unroll, DOWN, buff=0.35).set_x(sec_center[0])
        self.fixed(verdict)
        self.play(verdict.animate.set_opacity(1), run_time=1.2)
        self.wait(2.0)

        coda = VGroup(
            note("Volumes escape: the tilt error in π y² Δx is second-order and dies.", 22, TXT),
            note("Lengths and surfaces don't: the width is ds, and ds/dx never returns to 1.", 22, TXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).to_edge(DOWN, buff=0.35)
        self.fixed(coda)
        self.play(cap3.animate.set_opacity(0), coda.animate.set_opacity(1), run_time=0.8)
        self.wait(3.0)

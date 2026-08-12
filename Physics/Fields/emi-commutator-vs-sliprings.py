"""Slip rings vs split ring, in the classic 3D textbook view — two acts.

One machine: crank, rectangular loop between poles, axle carrying the
collector. Act 1 fits SLIP RINGS (two full cylinders, contact never
changes — honest a.c.). Act 2 swaps in the SPLIT RING (halves spin with
the coil, the gap crosses the brushes at every half-turn — bumpy d.c.).
A live output trace draws in the corner throughout.

Render (from this folder):
    manim -qm emi-commutator-vs-sliprings.py CommutatorVsSlipRings   # smoke
    manim -qk emi-commutator-vs-sliprings.py CommutatorVsSlipRings   # 4K
Copy the output beside the card as emi-commutator-vs-sliprings.mp4,
then clear media/ + __pycache__/.
"""

import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
TEAL = "#0891b2"
PURPLE = "#7c3aed"
WHITEISH = "#d8d8d8"

config.background_color = BG

W = 1.15          # loop half-width
X0, X1 = -2.4, 0.4   # loop extent along the axle
R = 0.42          # collector radius
XR1, XR2 = 2.0, 2.7  # collector positions on the axle


def ring_pts(x, th0, th1, n=48):
    ph = np.linspace(th0, th1, n)
    return [np.array([x, R * np.cos(p), R * np.sin(p)]) for p in ph]


class CommutatorVsSlipRings(ThreeDScene):
    def construct(self):
        th = ValueTracker(0.0)

        # ---------- the machine ----------
        axle = Line3D(start=np.array([-3.5, 0, 0]), end=np.array([3.5, 0, 0]),
                      color=GRAY, thickness=0.02)

        def loop():
            a = th.get_value()
            c, s = np.cos(a), np.sin(a)
            pA1 = np.array([X0, W * c, W * s])
            pA2 = np.array([X1, W * c, W * s])
            pB1 = np.array([X0, -W * c, -W * s])
            pB2 = np.array([X1, -W * c, -W * s])
            side_a = Line3D(start=pA1, end=pA2, color=AMBER, thickness=0.035)
            side_b = Line3D(start=pB1, end=pB2, color=WHITEISH, thickness=0.035)
            end1 = Line3D(start=pA1, end=pB1, color=PURPLE, thickness=0.03)
            end2 = Line3D(start=pA2, end=pB2, color=PURPLE, thickness=0.03)
            return VGroup(end1, end2, side_a, side_b)
        loop_m = always_redraw(loop)

        def crank():
            a = th.get_value()
            base = np.array([-3.5, 0, 0])
            elbow = base + np.array([0, 0.55 * np.cos(a + PI / 2), 0.55 * np.sin(a + PI / 2)])
            handle = elbow + np.array([-0.55, 0, 0])
            return VGroup(
                Line3D(start=base, end=elbow, color=GRAY, thickness=0.03),
                Line3D(start=elbow, end=handle, color=GRAY, thickness=0.035),
            )
        crank_m = always_redraw(crank)

        pole_n = Prism(dimensions=[2.6, 0.45, 1.8], stroke_width=0,
                       fill_color=BLUE, fill_opacity=0.45).move_to(np.array([-1.0, 2.0, 0]))
        pole_s = Prism(dimensions=[2.6, 0.45, 1.8], stroke_width=0,
                       fill_color=RED, fill_opacity=0.4).move_to(np.array([-1.0, -2.0, 0]))
        b_arrows = VGroup(*[
            Arrow3D(start=np.array([x, 1.55, 0]), end=np.array([x, -1.55, 0]),
                    color=TEAL, thickness=0.014, base_radius=0.05)
            for x in (-1.7, -0.3)
        ])

        # ---------- collectors ----------
        # slip rings: two FULL rings, fixed contact
        slip_ring1 = VMobject(stroke_color=AMBER, stroke_width=9).set_points_as_corners(
            ring_pts(XR1, 0, TAU) + [ring_pts(XR1, 0, TAU)[0]])
        slip_ring2 = VMobject(stroke_color=WHITEISH, stroke_width=9).set_points_as_corners(
            ring_pts(XR2, 0, TAU) + [ring_pts(XR2, 0, TAU)[0]])
        brush_s1 = Cube(side_length=0.17, fill_color=GRAY, fill_opacity=1, stroke_width=0
                        ).move_to(np.array([XR1, 0, R + 0.16]))
        brush_s2 = Cube(side_length=0.17, fill_color=GRAY, fill_opacity=1, stroke_width=0
                        ).move_to(np.array([XR2, 0, R + 0.16]))
        wire_s1 = Line3D(start=np.array([XR1, 0, R + 0.24]), end=np.array([XR1 + 0.7, 0, 1.35]),
                         color=AMBER, thickness=0.018)
        wire_s2 = Line3D(start=np.array([XR2, 0, R + 0.24]), end=np.array([XR2 + 0.7, 0, 1.35]),
                         color=WHITEISH, thickness=0.018)
        slip_assembly = VGroup(slip_ring1, slip_ring2, brush_s1, brush_s2, wire_s1, wire_s2)

        # split ring: two half-shells that ROTATE with the coil; brushes top + bottom
        XS = 2.3
        gap = 0.30

        def split_ring():
            a = th.get_value()
            arc_a = VMobject(stroke_color=AMBER, stroke_width=11).set_points_as_corners(
                ring_pts(XS, a + gap, a + PI - gap))
            arc_b = VMobject(stroke_color=WHITEISH, stroke_width=11).set_points_as_corners(
                ring_pts(XS, a + PI + gap, a + TAU - gap))
            return VGroup(arc_a, arc_b)
        split_m = always_redraw(split_ring)
        brush_t = Cube(side_length=0.17, fill_color=GRAY, fill_opacity=1, stroke_width=0
                       ).move_to(np.array([XS, 0, R + 0.16]))
        brush_b = Cube(side_length=0.17, fill_color=GRAY, fill_opacity=1, stroke_width=0
                       ).move_to(np.array([XS, 0, -R - 0.16]))
        wire_t = Line3D(start=np.array([XS, 0, R + 0.24]), end=np.array([XS + 0.8, 0, 1.35]),
                        color=GRAY, thickness=0.018)
        wire_b = Line3D(start=np.array([XS, 0, -R - 0.24]), end=np.array([XS + 0.8, 0, -1.35]),
                        color=GRAY, thickness=0.018)
        split_brushes = VGroup(brush_t, brush_b, wire_t, wire_b)

        # ---------- fixed-in-frame: titles, captions, graph ----------
        title1 = Text("SLIP RINGS — the a.c. generator", font_size=27, color=AMBER, weight=BOLD
                      ).to_edge(UP, buff=0.3)
        title2 = Text("SPLIT RING — the d.c. dynamo", font_size=27, color=GREEN, weight=BOLD
                      ).to_edge(UP, buff=0.3)
        ax = Axes(x_range=[0, 4 * PI, 100], y_range=[-1.2, 1.2, 10],
                  x_length=4.6, y_length=1.5,
                  axis_config={"color": GRAY, "stroke_width": 1.4,
                               "include_ticks": False, "include_tip": False})
        ax.to_corner(DL, buff=0.5).shift(UP * 0.55)
        out_lab = Text("output", font_size=19, color=GRAY).next_to(ax, UP, buff=0.08).align_to(ax, LEFT)
        lab_n = Text("N", font_size=30, color=GRAY, weight=BOLD).move_to(np.array([0.67, 1.13, 0]))
        lab_s = Text("S", font_size=30, color=GRAY, weight=BOLD).move_to(np.array([-2.11, -0.33, 0]))

        def trace_ac():
            tn = max(th.get_value(), 0.02)
            return ax.plot(lambda x: np.cos(x), x_range=[0, min(tn, 4 * PI), 0.05],
                           color=AMBER, stroke_width=3)

        act2_on = ValueTracker(0.0)

        def trace_dc():
            if act2_on.get_value() < 0.5:
                return VMobject()
            tn = max(th.get_value(), 0.02)
            return ax.plot(lambda x: abs(np.cos(x)), x_range=[0, min(tn, 4 * PI), 0.05],
                           color=GREEN, stroke_width=3)

        cap_specs = [
            ("the crank spins one loop between the poles", GRAY),          # 0
            ("each coil end has its OWN full ring — contact never changes", AMBER),  # 1
            ("so the output alternates: honest a.c.", AMBER),              # 2
            ("same machine — now ONE ring, split in two, spinning with the coil", GRAY),  # 3
            ("the gap crosses the brushes — contact swaps!", GREEN),       # 4
            ("a swap at every half-turn: the output never goes negative", GREEN),  # 5
            ("the collector decides what you collect", GRAY),              # 6
        ]
        caps = []
        for txt, col in cap_specs:
            cp = Text(txt, font_size=24, color=col).to_edge(DOWN, buff=0.32)
            cp.set_opacity(0)
            caps.append(cp)

        # ---------- build ----------
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        self.add(axle, pole_n, pole_s, b_arrows, loop_m, crank_m, slip_assembly)
        title2.set_opacity(0)
        self.add_fixed_in_frame_mobjects(title1, title2, ax, out_lab, lab_n, lab_s, *caps)
        tr = always_redraw(trace_ac)
        tr2 = always_redraw(trace_dc)
        self.add_fixed_in_frame_mobjects(tr, tr2)

        def show(i, rt=0.45):
            anims = [caps[i].animate.set_opacity(1)]
            anims += [caps[j].animate.set_opacity(0) for j in range(len(caps)) if j != i]
            self.play(*anims, run_time=rt)

        # ---- Act 1: slip rings ----
        show(0)
        self.play(th.animate.set_value(TAU), run_time=4.2, rate_func=linear)
        show(1)
        self.play(th.animate.set_value(1.75 * TAU), run_time=3.2, rate_func=linear)
        show(2)
        self.play(th.animate.set_value(2 * TAU), run_time=1.1, rate_func=linear)
        self.wait(0.7)

        # ---- switch collectors (loop pose at 2*TAU == pose at 0) ----
        self.play(FadeOut(slip_assembly), run_time=0.5)
        self.remove(tr)
        th.set_value(0.0)
        act2_on.set_value(1.0)
        self.play(FadeIn(split_m), FadeIn(split_brushes),
                  title1.animate.set_opacity(0), title2.animate.set_opacity(1), run_time=0.7)

        # ---- Act 2: split ring ----
        show(3)
        self.play(th.animate.set_value(PI / 2 - 0.02), run_time=2.0, rate_func=linear)
        self.play(Flash(np.array([XS, 0, R + 0.16]), color=GREEN, flash_radius=0.5),
                  Flash(np.array([XS, 0, -R - 0.16]), color=GREEN, flash_radius=0.5),
                  th.animate.set_value(PI / 2 + 0.02), run_time=0.5)
        show(4)
        self.play(th.animate.set_value(TAU), run_time=3.0, rate_func=linear)
        show(5)
        self.play(th.animate.set_value(2 * TAU), run_time=3.6, rate_func=linear)
        show(6)
        self.wait(1.6)

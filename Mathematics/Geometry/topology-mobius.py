"""Two topological facts you cannot see from a still picture.

Scene 1  In 3D: a ball becomes a potato becomes a bowl with nothing torn, and a doughnut
         becomes a mug — the handle's hole is the doughnut's hole. The number of holes
         is what survives.
Scene 2  The Möbius strip: a band with a half twist has one side and one edge. Cut it
         along the middle and it does not fall into two rings — it becomes one long ring
         with two twists.

Render:  manim -qk topology-mobius.py Topology
"""
from manim import *
import numpy as np
GREY_K="#888888"; BLUE_K="#2563eb"; PURPLE_K="#7c3aed"; GREEN_K="#059669"; RED_K="#dc2626"; AMBER_K="#f59e0b"

class Topology(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        # ---------- scene 1 (3D): a ball to a bowl, a doughnut to a mug
        title = Text("To a topologist these are the same shape: stretch, never tear, never glue", font_size=26, color=GREY_K).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.set_camera_orientation(phi=65*DEGREES, theta=-70*DEGREES, zoom=0.85)
        res = (32, 20)
        L0 = np.array([-3.6, 0, 0.2]); R0 = np.array([2.6, 0, 0])
        def ball(u, v): return 1.3*np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)]) + L0
        def potato(u, v):
            r = 1.3*(1 + 0.22*np.sin(3*u)*np.sin(2*v) + 0.15*np.cos(2*u)*np.cos(v))
            return r*np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)]) + L0
        def bowl(u, v):
            # a dented ball: the top pushed down into a bowl — still no hole
            s_ = np.sin(v); z = np.cos(v)
            dent = 1.9*max(0.0, z)**1.6
            return np.array([1.5*np.cos(u)*s_, 1.5*np.sin(u)*s_, 1.3*z - dent]) + L0
        Rm = 1.5
        def torus(u, v): return np.array([(Rm + 0.55*np.cos(v))*np.cos(u), (Rm + 0.55*np.cos(v))*np.sin(u), 0.55*np.sin(v)]) + R0
        # the mug: a cup (a thick U profile revolved about a vertical axis, open at the top) and a handle (half a thin torus on its side)
        def uprofile(t):
            # closed thick-U curve in the (rho, z) plane, t in [0, 2pi]: outer wall up, rim, inner wall down, inner floor, up the inside? no —
            # rho from 0 (axis) to 1.1 (outer), floor thickness 0.25, wall thickness 0.22, height 1.9
            pts = [(0.0, -1.0), (1.1, -1.0), (1.1, 0.9), (0.88, 0.9), (0.88, -0.75), (0.0, -0.75)]
            # walk the polygon with rounded corners via linear interpolation on a closed loop
            n = len(pts); L = [np.hypot(pts[(k+1)%n][0]-pts[k][0], pts[(k+1)%n][1]-pts[k][1]) for k in range(n)]; tot = sum(L)
            d = (t/(2*np.pi)) % 1.0 * tot
            for k in range(n):
                if d <= L[k] + 1e-9:
                    a_, b_ = pts[k], pts[(k+1)%n]; f = d/L[k] if L[k] else 0
                    return a_[0] + f*(b_[0]-a_[0]), a_[1] + f*(b_[1]-a_[1])
                d -= L[k]
            return pts[0]
        def mug(u, v):
            # ONE patch, same (u, v) grid as the torus, so the transform maps quad to quad:
            # u in [0, 1.6 pi) sweeps the cup (a thick U profile revolved about a vertical axis, open at the top);
            # u in [1.6 pi, 2 pi] sweeps the handle (a half torus on its side, hung on the outer wall).
            split = 1.6*np.pi
            if u < split:
                ang = u/split*2*np.pi; rho, z = uprofile(v)
                return np.array([rho*np.cos(ang), rho*np.sin(ang), z]) + R0
            h = (u - split)/(2*np.pi - split)*np.pi                    # 0 .. pi: a half ring standing on the outer wall
            rh, rt, cx = 0.7, 0.16, 1.05                               # ring centre on the wall, so both ends touch it
            return np.array([cx + (rh + rt*np.cos(v))*np.sin(h), rt*np.sin(v), (rh + rt*np.cos(v))*np.cos(h)]) + R0
        kw = dict(resolution=res, fill_opacity=0.7, stroke_width=0.2, stroke_color=GREY_K)
        A = Surface(ball, u_range=[0, 2*np.pi], v_range=[0, np.pi], checkerboard_colors=[BLUE_K, "#1e40af"], **kw)
        B = Surface(potato, u_range=[0, 2*np.pi], v_range=[0, np.pi], checkerboard_colors=[BLUE_K, "#1e40af"], **kw)
        Cb = Surface(bowl, u_range=[0, 2*np.pi], v_range=[0, np.pi], checkerboard_colors=[BLUE_K, "#1e40af"], **kw)
        T = Surface(torus, u_range=[0, 2*np.pi], v_range=[0, 2*np.pi], checkerboard_colors=[AMBER_K, "#b45309"], resolution=(40, 16), fill_opacity=0.7, stroke_width=0.2, stroke_color=GREY_K)
        def faces_from(func, nu, nv, colors):
            # build the faces from the grid corners only — Manim's Surface also differentiates the function
            # numerically for shading, and across the cup/handle seam that blows up; corners cannot
            us = np.linspace(0, 2*np.pi, nu + 1); vs = np.linspace(0, 2*np.pi, nv + 1); g = VGroup()
            for i in range(nu):
                for j in range(nv):
                    c = [func(us[i], vs[j]), func(us[i+1], vs[j]), func(us[i+1], vs[j+1]), func(us[i], vs[j+1]), func(us[i], vs[j])]
                    f = ThreeDVMobject().set_points_as_corners(c)
                    f.set_fill(colors[(i + j) % 2], opacity=0.7).set_stroke(GREY_K, width=0.2)
                    g.add(f)
            return g
        M = faces_from(mug, 40, 16, [AMBER_K, "#b45309"])
        lab1 = Text("no hole: a ball, a potato, a bowl", font_size=22, color=BLUE_K).to_corner(DL, buff=0.6).shift(UP*0.6)
        lab2 = Text("one hole: a doughnut, a mug", font_size=22, color=AMBER_K).to_corner(DR, buff=0.6).shift(UP*0.6)
        self.add_fixed_in_frame_mobjects(lab1, lab2)
        self.play(FadeIn(A), FadeIn(T)); self.wait(0.8)
        self.play(Transform(A, B), run_time=2.2); self.wait(0.5)
        self.play(Transform(A, Cb), run_time=2.4); self.wait(0.5)
        self.play(Transform(T, M), run_time=3.0); self.wait(0.8)
        cap = Text("the one number that never changes is the number of holes", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.add_fixed_in_frame_mobjects(cap); self.wait(2.0)
        self.play(FadeOut(A), FadeOut(T), FadeOut(lab1), FadeOut(lab2), FadeOut(cap))
        # ---------- scene 2 (3D): the Möbius strip and the cut
        t2 = Text("The Möbius strip: one side, one edge — and a cut down the middle does not split it", font_size=26, color=GREY_K).to_edge(UP)
        self.play(FadeOut(title)); self.add_fixed_in_frame_mobjects(t2); self.play(FadeIn(t2))
        self.set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES)
        def mob(w):
            return lambda u, v: np.array([(2 + w*v*np.cos(u/2))*np.cos(u), (2 + w*v*np.cos(u/2))*np.sin(u), w*v*np.sin(u/2)])
        strip = Surface(mob(0.8), u_range=[0, 2*np.pi], v_range=[-1, 1], resolution=(48, 6), fill_opacity=0.55, checkerboard_colors=[PURPLE_K, "#5b21b6"], stroke_width=0.3, stroke_color=GREY_K)
        self.play(FadeIn(strip)); self.begin_ambient_camera_rotation(rate=0.25)
        # a point travelling along the centre line: after one lap it is on the "other side", after two it is back
        dot = Dot3D(point=mob(0.8)(0, 0), color=AMBER_K, radius=0.09)
        self.add(dot)
        u = ValueTracker(0.0)
        dot.add_updater(lambda d: d.move_to(mob(0.8)(u.get_value(), 0)))
        cap2 = Text("walk the middle line: one lap lands you underneath, two laps bring you home", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.add_fixed_in_frame_mobjects(cap2)
        self.play(u.animate.set_value(4*np.pi), run_time=7, rate_func=linear); dot.remove_updater(lambda d: None); self.remove(dot)
        cut = ParametricFunction(lambda t: mob(0.8)(t, 0), t_range=[0, 2*np.pi], color=RED_K, stroke_width=5)
        cap3 = Text("now cut along that line", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(cap2)); self.add_fixed_in_frame_mobjects(cap3); self.play(Create(cut), run_time=2.5)
        # after the cut: the two halves v in [-1,-0.1] and [0.1,1] are ONE band (parameter u runs 0..4pi around it)
        half1 = Surface(mob(0.8), u_range=[0, 2*np.pi], v_range=[0.12, 1], resolution=(64, 4), fill_opacity=0.6, checkerboard_colors=[GREEN_K, "#047857"], stroke_width=0.3, stroke_color=GREY_K)
        half2 = Surface(mob(0.8), u_range=[0, 2*np.pi], v_range=[-1, -0.12], resolution=(64, 4), fill_opacity=0.6, checkerboard_colors=[GREEN_K, "#047857"], stroke_width=0.3, stroke_color=GREY_K)
        self.play(FadeOut(strip), FadeOut(cut), FadeIn(half1), FadeIn(half2))
        cap4 = Text("not two rings: one ring, twice as long, with two full twists — trace it and see", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(cap3)); self.add_fixed_in_frame_mobjects(cap4)
        dot2 = Dot3D(point=mob(0.8)(0, 0.56), color=AMBER_K, radius=0.09); self.add(dot2)
        u2 = ValueTracker(0.0)
        # on the cut band the centre line is at v = +0.56 for the first lap and v = -0.56 for the second (it is one band)
        dot2.add_updater(lambda d: d.move_to(mob(0.8)(u2.get_value() % (2*np.pi), 0.56 if u2.get_value() < 2*np.pi else -0.56)))
        self.play(u2.animate.set_value(4*np.pi - 1e-3), run_time=8, rate_func=linear)
        self.wait(1.5); self.stop_ambient_camera_rotation()

"""Manim scenes for [[Planes in 3D]] — the review-pass batch.

  PlaneAssembly   -- (1) points satisfying r.n = 6 assemble into a plane;
                     (2) r = a + lambda b + mu c wanders but never leaves it;
                     (3) the dial p slides the plane along its flagpole.
  LinePlaneCases  -- a dot walks each line while a live shadow readout
                     r.n shows WHY d.n decides meets / lies-in / parallel.
  TwoPlanesCrease -- two planes meet along the crease n1 x n2 (rotating).
  SkewSandwich    -- skew lines, the parallel-plane sandwich, the common
                     perpendicular (rotating).

Render (on Kepei's Mac, from this directory):
  manim -qk planes-in-3d-scenes.py PlaneAssembly
  manim -qk planes-in-3d-scenes.py LinePlaneCases
  manim -qk planes-in-3d-scenes.py TwoPlanesCrease
  manim -qk planes-in-3d-scenes.py SkewSandwich
  cp media/videos/planes-in-3d-scenes/2160p60/PlaneAssembly.mp4 planes-in-3d-assembly.mp4
  cp media/videos/planes-in-3d-scenes/2160p60/LinePlaneCases.mp4 planes-in-3d-line-cases.mp4
  cp media/videos/planes-in-3d-scenes/2160p60/TwoPlanesCrease.mp4 planes-in-3d-two-planes.mp4
  cp media/videos/planes-in-3d-scenes/2160p60/SkewSandwich.mp4 planes-in-3d-skew-sandwich.mp4
  rm -rf media
"""

from manim import *
import numpy as np

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
PURPLE   = "#7c3aed"

config.background_color = BG

N = np.array([2.0, 1.0, 2.0])
NHAT = N / 3.0


class CaptionMixin:
    """Bottom caption that swaps cleanly (fixed in frame)."""
    _cap = None

    def caption(self, mobj, run_time=0.6):
        mobj.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(mobj)
        anims = [FadeIn(mobj)]
        if self._cap is not None:
            anims.append(FadeOut(self._cap))
        self.play(*anims, run_time=run_time)
        self._cap = mobj


class PlaneAssembly(ThreeDScene, CaptionMixin):
    SCALE = 0.6
    CENTER = np.array([1.2, 1.8, 1.2])

    def W(self, p):
        return (np.array(p, dtype=float) - self.CENTER) * self.SCALE

    def surface(self, p_val, opacity=0.35):
        return Surface(
            lambda u, v: self.W([(p_val - u - 2.0 * v) / 2.0, u, v]),
            u_range=[-0.8, 5.8], v_range=[-0.6, 3.2],
            resolution=(12, 12), fill_opacity=opacity,
            checkerboard_colors=[BLUE, BLUE], stroke_width=0)

    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-50 * DEGREES,
                                    zoom=1.0)
        title = MathTex(r"\mathbf{r}\cdot\mathbf{n} = 6,\qquad \mathbf{n}=(2,1,2)",
                        font_size=40, color=TXT).to_edge(UP, buff=0.35)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.6)

        pole = Line3D(self.W(-1.0 * NHAT), self.W(6.4 * NHAT), color=GREY,
                      thickness=0.012)
        self.play(Create(pole), run_time=0.8)
        self.begin_ambient_camera_rotation(rate=0.045)

        # ---- beat 1: points audition for the plane ----------------------
        self.caption(Text("every point r takes the test:  is  r · n = 6 ?",
                          font_size=26, color=TXT))
        rng = np.random.default_rng(7)

        def keep_point():
            y, z = rng.uniform(0.2, 5.2), rng.uniform(-0.2, 2.8)
            return np.array([(6.0 - y - 2.0 * z) / 2.0, y, z])

        def reject_point():
            q = keep_point()
            return q + NHAT * rng.choice([-1, 1]) * rng.uniform(1.0, 2.4)

        kept = VGroup()
        for _ in range(3):          # three audition rounds
            rejects = VGroup(*[Dot3D(self.W(reject_point()), color=RED,
                                     radius=0.06) for _ in range(3)])
            keeps = VGroup(*[Dot3D(self.W(keep_point()), color=TEAL,
                                   radius=0.06) for _ in range(5)])
            self.play(LaggedStart(*[FadeIn(m) for m in [*rejects, *keeps]],
                                  lag_ratio=0.08), run_time=1.1)
            self.play(FadeOut(rejects, shift=0.2 * DOWN), run_time=0.6)
            kept.add(*keeps)
        more = VGroup(*[Dot3D(self.W(keep_point()), color=TEAL, radius=0.05)
                        for _ in range(14)])
        self.play(LaggedStart(*[FadeIn(m) for m in more], lag_ratio=0.05),
                  run_time=1.3)
        kept.add(*more)

        surf = self.surface(6.0)
        self.caption(Text("the survivors ARE a plane — one shared shadow on n",
                          font_size=26, color=GREEN))
        self.play(FadeIn(surf), run_time=1.4)
        self.wait(1.6)
        self.play(FadeOut(kept), run_time=0.7)

        # ---- beat 2: the parametric costume ------------------------------
        A = np.array([3.0, 0.0, 0.0])
        b = np.array([-3.0, 6.0, 0.0])
        c = np.array([-3.0, 0.0, 3.0])
        cap = MathTex(r"\text{other costume: } \mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}",
                      font_size=34, color=TXT)
        self.caption(cap)
        Adot = Dot3D(self.W(A), color=MAGENTA, radius=0.08)
        barrow = Line3D(self.W(A), self.W(A + 0.45 * b), color=AMBER,
                        thickness=0.015)
        carrow = Line3D(self.W(A), self.W(A + 0.6 * c), color=TEAL,
                        thickness=0.015)
        self.play(FadeIn(Adot), Create(barrow), Create(carrow), run_time=1.0)

        lam, mu = ValueTracker(0.0), ValueTracker(0.0)
        walker = always_redraw(lambda: Dot3D(
            self.W(A + lam.get_value() * b + mu.get_value() * c),
            color=MAGENTA, radius=0.09))
        trail = TracedPath(walker.get_center, stroke_color=MAGENTA,
                           stroke_width=3, stroke_opacity=0.7)
        self.add(trail)
        self.play(FadeIn(walker), run_time=0.4)
        self.play(lam.animate.set_value(0.55), run_time=1.6)
        self.play(mu.animate.set_value(0.75), run_time=1.6)
        self.play(lam.animate.set_value(0.15), mu.animate.set_value(0.3),
                  run_time=1.8)
        self.caption(Text("whatever λ and μ do, r never leaves the sheet",
                          font_size=26, color=GREEN))
        self.play(lam.animate.set_value(0.8), mu.animate.set_value(0.1),
                  run_time=1.8)
        self.wait(0.8)
        self.play(FadeOut(walker), FadeOut(trail), FadeOut(Adot),
                  FadeOut(barrow), FadeOut(carrow), run_time=0.7)

        # ---- beat 3: the dial p ------------------------------------------
        self.play(FadeOut(surf), run_time=0.4)
        p_val = ValueTracker(6.0)
        sliding = always_redraw(lambda: self.surface(p_val.get_value(),
                                                     opacity=0.3))
        mark = always_redraw(lambda: Dot3D(
            self.W((p_val.get_value() / 3.0) * NHAT), color=AMBER,
            radius=0.09))
        p_label = MathTex(r"p =", font_size=38, color=AMBER)
        p_num = DecimalNumber(6.0, num_decimal_places=1, font_size=38,
                              color=AMBER)
        p_group = VGroup(p_label, p_num).arrange(RIGHT, buff=0.15)
        p_group.to_corner(UR, buff=0.6)
        self.add_fixed_in_frame_mobjects(p_group)

        def upd_p(m):
            m.set_value(p_val.get_value())
            self.camera.add_fixed_in_frame_mobjects(m)
            m.move_to(p_label.get_right() + RIGHT * (m.width / 2 + 0.15))
        p_num.add_updater(upd_p)
        self.play(FadeIn(sliding), FadeIn(mark), FadeIn(p_group), run_time=0.8)
        self.caption(Text("what p controls: same tilt, the plane slides along its flagpole",
                          font_size=26, color=AMBER))
        self.play(p_val.animate.set_value(9.0), run_time=2.2)
        self.play(p_val.animate.set_value(3.0), run_time=2.6)
        self.play(p_val.animate.set_value(6.0), run_time=1.8)
        self.wait(1.4)
        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(m) for m in [sliding, mark, pole, title, p_group,
                                         self._cap]], run_time=0.8)


class LinePlaneCases(ThreeDScene, CaptionMixin):
    SCALE = 0.55
    CENTER = np.array([1.4, 2.0, 1.6])

    def W(self, p):
        return (np.array(p, dtype=float) - self.CENTER) * self.SCALE

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-48 * DEGREES,
                                    zoom=1.0)
        title = MathTex(r"\Pi:\ 2x+y+2z=6", font_size=38,
                        color=TXT).to_edge(UP, buff=0.35)
        self.add_fixed_in_frame_mobjects(title)
        surf = Surface(
            lambda u, v: self.W([(6.0 - u - 2.0 * v) / 2.0, u, v]),
            u_range=[-0.8, 6.0], v_range=[-0.6, 3.2],
            resolution=(12, 12), fill_opacity=0.32,
            checkerboard_colors=[BLUE, BLUE], stroke_width=0)
        self.play(FadeIn(title), FadeIn(surf), run_time=1.0)
        self.begin_ambient_camera_rotation(rate=0.04)

        readout_l = MathTex(r"\mathbf{r}\cdot\mathbf{n} \;=", font_size=40,
                            color=TXT)
        readout_n = DecimalNumber(0, num_decimal_places=1, font_size=40,
                                  color=AMBER)
        target = MathTex(r"\text{(plane's mark: } 6\text{)}", font_size=30,
                         color=TXT_DIM)
        panel = VGroup(readout_l, readout_n).arrange(RIGHT, buff=0.2)
        panel.to_corner(UL, buff=0.55)
        target.next_to(panel, DOWN, buff=0.2).align_to(panel, LEFT)
        self.add_fixed_in_frame_mobjects(panel, target)
        self.play(FadeIn(panel), FadeIn(target), run_time=0.6)

        def run_case(a, d, lam_range, color, cap, hold, hit_at=None):
            a, d = np.array(a, float), np.array(d, float)
            shadow = lambda t: float(a @ N + t * (d @ N))
            lam = ValueTracker(lam_range[0])
            seg = Line3D(self.W(a + lam_range[0] * d),
                         self.W(a + lam_range[1] * d), color=color,
                         thickness=0.014)
            dot = always_redraw(lambda: Dot3D(
                self.W(a + lam.get_value() * d), color=color, radius=0.09))
            def upd(m):
                m.set_value(shadow(lam.get_value()))
                self.camera.add_fixed_in_frame_mobjects(m)
                m.move_to(readout_l.get_right() + RIGHT * (m.width / 2 + 0.2))
            readout_n.add_updater(upd)
            self.caption(cap)
            self.play(Create(seg), FadeIn(dot), run_time=0.8)
            if hit_at is not None:
                self.play(lam.animate.set_value(hit_at), run_time=2.0)
                hitdot = Dot3D(self.W(a + hit_at * d), color=GREEN,
                               radius=0.11)
                self.play(FadeIn(hitdot), Flash(panel, color=GREEN,
                          line_length=0.2), run_time=0.8)
                self.play(lam.animate.set_value(lam_range[1]), run_time=1.4)
                extra = [hitdot]
            else:
                self.play(lam.animate.set_value(lam_range[1]), run_time=3.0)
                extra = []
            self.wait(hold)
            readout_n.clear_updaters()
            self.play(FadeOut(seg), FadeOut(dot),
                      *[FadeOut(m) for m in extra], run_time=0.6)

        run_case([1, 0, 0], [0, 2, 1], (-1.0, 2.1), GREEN,
                 MathTex(r"\mathbf{d}\cdot\mathbf{n} = 4 \neq 0:"
                         r"\ \text{the shadow sweeps — it must hit } 6",
                         font_size=32, color=GREEN),
                 hold=0.8, hit_at=1.0)
        run_case([3, 0, 0], [-1.2, 2.4, 0], (-0.2, 1.9), AMBER,
                 MathTex(r"\mathbf{d}\cdot\mathbf{n} = 0,\ \text{anchor on the plane: stuck at } 6"
                         r"\ \text{— lies in}",
                         font_size=32, color=AMBER),
                 hold=1.0)
        run_case([1, 1, 5], [1, 2, -2], (-0.7, 1.4), RED,
                 MathTex(r"\mathbf{d}\cdot\mathbf{n} = 0,\ \text{stuck at } 13 \neq 6"
                         r"\ \text{— parallel forever}",
                         font_size=32, color=RED),
                 hold=1.2)

        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(m) for m in [surf, title, panel, target,
                                         self._cap]], run_time=0.8)


class TwoPlanesCrease(ThreeDScene, CaptionMixin):
    SCALE = 0.62
    CENTER = np.array([2.0, 2.0, 0.0])

    def W(self, p):
        return (np.array(p, dtype=float) - self.CENTER) * self.SCALE

    def construct(self):
        self.set_camera_orientation(phi=72 * DEGREES, theta=-40 * DEGREES,
                                    zoom=0.95)
        title = MathTex(r"\Pi_1:\ 2x+y+2z=6\qquad \Pi_2:\ x+y+z=4",
                        font_size=38, color=TXT).to_edge(UP, buff=0.35)
        self.add_fixed_in_frame_mobjects(title)

        base = np.array([2.0, 2.0, 0.0])
        cd = np.array([1.0, 0.0, -1.0])       # crease direction = n1 x n2
        w1 = np.array([1.0, -4.0, 1.0])       # in Pi1
        w2 = np.array([1.0, -2.0, 1.0])       # in Pi2
        def sheet(w, col):
            return Surface(
                lambda u, v: self.W(base + u * cd + v * w),
                u_range=[-2.2, 2.2], v_range=[-1.0, 1.0],
                resolution=(10, 10), fill_opacity=0.3,
                checkerboard_colors=[col, col], stroke_width=0)
        s1 = sheet(w1, BLUE)
        s2 = sheet(w2, PURPLE)
        self.play(FadeIn(title), FadeIn(s1), run_time=0.9)
        self.play(FadeIn(s2), run_time=0.9)
        self.begin_ambient_camera_rotation(rate=0.12)
        self.caption(Text("two tilted floors — they must meet along a crease",
                          font_size=26, color=TXT))
        self.wait(1.6)

        crease = Line3D(self.W(base - 2.4 * cd), self.W(base + 2.4 * cd),
                        color=MAGENTA, thickness=0.02)
        cdot = Dot3D(self.W(base), color=MAGENTA, radius=0.09)
        self.caption(MathTex(r"\ell:\ (2,2,0) + t(1,0,-1)\qquad"
                             r"\text{direction} = \mathbf{n}_1\times\mathbf{n}_2",
                             font_size=34, color=MAGENTA))
        self.play(Create(crease), FadeIn(cdot), run_time=1.4)
        self.wait(1.8)

        a1 = base - 1.8 * cd
        n1a = Arrow3D(self.W(a1), self.W(a1 + 2.4 * np.array([2, 1, 2]) / 3.0),
                      color=BLUE, thickness=0.01)
        n2a = Arrow3D(self.W(a1), self.W(a1 + 2.4 * np.array([1, 1, 1]) / np.sqrt(3)),
                      color=PURPLE, thickness=0.01)
        self.caption(MathTex(r"\text{angle between planes} = \text{angle between normals}"
                             r"\ \approx 15.8^\circ", font_size=34, color=TXT))
        self.play(Create(n1a), Create(n2a), run_time=1.2)
        self.wait(3.2)
        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(m) for m in [s1, s2, crease, cdot, n1a, n2a,
                                         title, self._cap]], run_time=0.8)


class SkewSandwich(ThreeDScene, CaptionMixin):
    SCALE = 0.62
    CENTER = np.array([2.0, 2.0, 2.2])

    def W(self, p):
        return (np.array(p, dtype=float) - self.CENTER) * self.SCALE

    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-110 * DEGREES,
                                    zoom=0.95)
        title = MathTex(
            r"\ell_1:\ (1,2,0)+s(1,0,1)\qquad \ell_2:\ (0,0,4)+t(1,1,0)",
            font_size=36, color=TXT).to_edge(UP, buff=0.35)
        self.add_fixed_in_frame_mobjects(title)

        a1 = np.array([1.0, 2.0, 0.0]); d1 = np.array([1.0, 0.0, 1.0])
        a2 = np.array([0.0, 0.0, 4.0]); d2 = np.array([1.0, 1.0, 0.0])
        l1 = Line3D(self.W(a1 - 1.0 * d1), self.W(a1 + 3.6 * d1),
                    color=TEAL, thickness=0.016)
        l2 = Line3D(self.W(a2 - 1.0 * d2), self.W(a2 + 3.6 * d2),
                    color=AMBER, thickness=0.016)
        self.play(FadeIn(title), Create(l1), Create(l2), run_time=1.2)
        self.begin_ambient_camera_rotation(rate=0.08)
        self.caption(Text("do they meet?  rotate — no: skew",
                          font_size=26, color=TXT))
        self.wait(2.6)

        nn = np.array([-1.0, 1.0, 1.0])
        def sand(anchor, col):
            return Surface(
                lambda u, v: self.W(anchor + u * d1 + v * d2),
                u_range=[-1.2, 3.8], v_range=[-1.4, 3.8],
                resolution=(10, 10), fill_opacity=0.3,
                checkerboard_colors=[col, col], stroke_width=0)
        sA = sand(a1, BLUE)
        sB = sand(a2, PURPLE)
        self.caption(MathTex(r"\text{the sandwich: two parallel planes, normal } "
                             r"\mathbf{d}_1\times\mathbf{d}_2 = (-1,1,1)",
                             font_size=32, color=TXT))
        self.play(FadeIn(sA), run_time=0.9)
        self.play(FadeIn(sB), run_time=0.9)
        self.wait(1.6)

        F1 = np.array([4.0, 2.0, 3.0]); F2 = np.array([3.0, 3.0, 4.0])
        perp = Line3D(self.W(F1), self.W(F2), color=MAGENTA, thickness=0.022)
        p1 = Dot3D(self.W(F1), color=MAGENTA, radius=0.09)
        p2 = Dot3D(self.W(F2), color=MAGENTA, radius=0.09)
        self.caption(MathTex(r"\text{common perpendicular } F_1(4,2,3)\to F_2(3,3,4):"
                             r"\ \text{distance} = \sqrt{3}",
                             font_size=32, color=MAGENTA))
        self.play(FadeIn(p1), FadeIn(p2), Create(perp), run_time=1.2)
        self.wait(3.0)
        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(m) for m in [l1, l2, sA, sB, perp, p1, p2,
                                         title, self._cap]], run_time=0.8)

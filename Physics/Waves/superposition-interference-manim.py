"""
superposition-interference-manim.py — two scenes for [[Superposition and Interference]].

Scene 1  RippleTank    — two in-phase point sources; the summed field drawn live as a
                         heat map; the lines of constructive and destructive interference
                         fade in and the wave is seen to stand still along them.
Scene 2  YoungFringes  — slits, screen, fringes; then a shrinks (fringes widen), the light
                         goes red → blue (fringes narrow), D grows (fringes widen): λ = ax/D.

Smoke:   manim -ql --fps 15 superposition-interference-manim.py RippleTank YoungFringes
Final:   manim -qk superposition-interference-manim.py RippleTank YoungFringes
then concat with ffmpeg to superposition-interference-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *
import numpy as np

GREY = "#888888"
BLUE_, RED_, GREEN_, AMBER, PURPLE_, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"


class RippleTank(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Two sources in a ripple tank — add the two waves at every point", font_size=30, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        lam, a = 1.2, 3.6
        k = 2 * PI / lam
        W, H = 12.0, 5.6                      # scene units shown
        nx, ny = 300, 140
        xs = np.linspace(-W / 2, W / 2, nx); ys = np.linspace(0.15, H, ny)
        X, Y = np.meshgrid(xs, ys)
        r1 = np.hypot(X + a / 2, Y); r2 = np.hypot(X - a / 2, Y)
        t = ValueTracker(0.0)
        y0 = -3.1                               # bottom of the tank in scene coords

        def frame():
            tt = t.get_value()
            z = (np.cos(k * r1 - 2 * PI * tt) / np.sqrt(r1 + 0.3) + np.cos(k * r2 - 2 * PI * tt) / np.sqrt(r2 + 0.3))
            z = np.clip(z / 1.6, -1, 1)
            rgb = np.zeros((ny, nx, 3), dtype=np.uint8)
            pos = np.clip(z, 0, 1); neg = np.clip(-z, 0, 1)
            rgb[..., 0] = (30 + 200 * neg).astype(np.uint8)                 # troughs reddish
            rgb[..., 1] = (30 + 60 * pos + 30 * neg).astype(np.uint8)
            rgb[..., 2] = (30 + 220 * pos).astype(np.uint8)                 # crests blue
            img = ImageMobject(rgb[::-1])
            img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
            img.stretch_to_fit_width(W).stretch_to_fit_height(H).move_to([0, y0 + H / 2, 0])
            return img
        pic = always_redraw(frame)
        self.add(pic)
        s1 = Dot([-a / 2, y0, 0], color=AMBER, radius=0.09); s2 = Dot([a / 2, y0, 0], color=AMBER, radius=0.09)
        self.add(s1, s2)
        self.play(t.animate.set_value(4.0), run_time=6.0, rate_func=linear)
        # nodal and antinodal lines: r2 − r1 = nλ (green), (n+½)λ (red dashed), traced as point sets
        def line_for(delta, col, dashed):
            pts = []
            for yy in np.linspace(0.3, H, 120):
                # solve for x with r2 − r1 = delta along this row by scanning
                row = np.hypot(xs - a / 2, yy) - np.hypot(xs + a / 2, yy) - delta
                idx = np.where(np.diff(np.sign(row)) != 0)[0]
                for i in idx:
                    pts.append([xs[i], y0 + yy, 0])
            if len(pts) < 4: return None
            pts.sort(key=lambda p: p[1])
            m = VMobject(color=col, stroke_width=2.5 if not dashed else 1.6).set_points_smoothly(pts)
            return DashedVMobject(m, num_dashes=40) if dashed else m
        lines = VGroup()
        for n in range(-2, 3):
            L = line_for(n * lam, GREEN_, False)
            if L: lines.add(L)
            L = line_for((n + 0.5) * lam, RED_, True)
            if L: lines.add(L)
        cap = Text("green: path difference nλ — the two waves arrive in step, the water heaves double  ·  red: (n+½)λ — they cancel, the water is still",
                   font_size=17, color=GREY).to_edge(DOWN, buff=0.15)
        self.play(FadeIn(lines), FadeIn(cap), run_time=1.0)
        self.play(t.animate.set_value(10.0), run_time=9.0, rate_func=linear)
        self.wait(0.4)


class YoungFringes(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Young's double slit — fringe spacing x = λD/a", font_size=30, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        a = ValueTracker(0.50)      # mm
        lam = ValueTracker(650.0)   # nm
        D = ValueTracker(2.0)       # m
        # geometry in scene units: slits at x=-4, screen at x = -4 + 3.5*D/2
        def slits():
            return VGroup(Line([-4, -2.6, 0], [-4, -0.25 * a.get_value() / 0.5 - 0.0, 0], color=GREY, stroke_width=5),
                          Line([-4, -0.25 * a.get_value() / 0.5 + 0.12, 0], [-4, 0.25 * a.get_value() / 0.5 - 0.12, 0], color=GREY, stroke_width=5),
                          Line([-4, 0.25 * a.get_value() / 0.5, 0], [-4, 2.6, 0], color=GREY, stroke_width=5))
        def screen_x(): return -4 + 3.5 * D.get_value()
        def screen():
            sx = screen_x()
            # fringes: intensity cos²(π a x / λ D) painted as horizontal bars
            xs = np.linspace(-2.6, 2.6, 260)
            spacing = lam.get_value() * 1e-9 * D.get_value() / (a.get_value() * 1e-3)   # metres
            scale = 2.6 / 0.012                                                          # 12 mm of screen = 2.6 units
            I = np.cos(np.pi * (xs / scale) / spacing) ** 2
            hue = "#ef4444" if lam.get_value() > 600 else ("#22c55e" if lam.get_value() > 520 else "#3b82f6")
            bars = VGroup(*[Rectangle(width=0.5, height=5.2 / 260 + 0.005, stroke_width=0, fill_color=hue, fill_opacity=float(I[i]))
                            .move_to([sx, xs[i], 0]) for i in range(260)])
            return VGroup(Line([sx - 0.3, -2.6, 0], [sx - 0.3, 2.6, 0], color=GREY, stroke_width=3), bars)
        def rays():
            sx = screen_x(); hue = "#ef4444" if lam.get_value() > 600 else ("#22c55e" if lam.get_value() > 520 else "#3b82f6")
            return VGroup(*[Line([-4, s, 0], [sx - 0.3, 0, 0], color=hue, stroke_width=1.2, stroke_opacity=0.6) for s in (-0.25 * a.get_value() / 0.5, 0.25 * a.get_value() / 0.5)])
        def label():
            spacing = lam.get_value() * 1e-9 * D.get_value() / (a.get_value() * 1e-3) * 1e3
            return Text(f"a = {a.get_value():.2f} mm    λ = {lam.get_value():.0f} nm    D = {D.get_value():.1f} m    →    x = λD/a = {spacing:.2f} mm",
                        font_size=22, color=GREY).to_edge(DOWN, buff=0.35)
        S = always_redraw(slits); Sc = always_redraw(screen); R = always_redraw(rays); Lb = always_redraw(label)
        src = Text("laser", font_size=18, color=GREY).move_to([-6.2, 0, 0])
        self.add(src, Line([-5.6, 0, 0], [-4.1, 0, 0], color="#ef4444", stroke_width=2), S, R, Sc, Lb)
        self.wait(1.5)
        cap = Text("", font_size=20, color=GREY).move_to([0, 3.0, 0])
        for note, action in (("bring the slits closer: a halves, the fringes spread to twice the spacing", lambda: a.animate.set_value(0.25)),
                             ("red → blue: shorter wavelength, closer fringes", lambda: lam.animate.set_value(450.0)),
                             ("move the screen away: D doubles, spacing doubles", lambda: D.animate.set_value(2.6))):
            newcap = Text(note, font_size=20, color=AMBER).move_to([0, 3.0, 0])
            self.play(Transform(cap, newcap), run_time=0.6)
            self.play(action(), run_time=2.5)
            self.wait(1.0)
        self.wait(0.5)

"""Manim scenes for [[The Solar System]].
Scene 1  Accretion   — a slowly turning cloud collapses under gravity, spins faster as it shrinks, and
                       flattens into a disc; the Sun lights at the centre; inside the frost line small
                       rocky planets gather, outside it large gaseous ones.
Scene 2  MoonPhases  — the Moon orbits the Earth with the half facing the Sun always lit; an inset shows
                       what that looks like from the Earth, with the day count.
Smoke:  manim -ql --fps 15 solar-system-manim.py Accretion MoonPhases
Final:  manim -qk solar-system-manim.py Accretion MoonPhases      then copy each scene beside the card as
        solar-system-accretion.mp4 and solar-system-moon-phases.mp4 (they illustrate different parts).
Schematic, not to scale."""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H, TEAL_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
DARK, LIT = "#5a5a5a", "#f3f0d8"


def half_disc(centre, radius, right=True, colour=LIT):
    """A filled half disc built from points (robust at any size)."""
    a = np.linspace(-PI / 2, PI / 2, 40) if right else np.linspace(PI / 2, 3 * PI / 2, 40)
    pts = [centre + radius * np.array([np.cos(x), np.sin(x), 0]) for x in a]
    return Polygon(*pts, color=colour, fill_color=colour, fill_opacity=1, stroke_width=0)



class Accretion(Scene):
    def construct(self):
        title = Text("How the Solar System formed: the accretion model", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        rng = np.random.default_rng(6)
        n = 170
        r0 = 2.5 * np.sqrt(rng.uniform(0.02, 1, n)); phi0 = rng.uniform(0, TAU, n); z0 = rng.uniform(-1, 1, n) * np.sqrt(np.maximum(0, 2.5**2 - r0**2)) * 0.9
        r1 = 0.4 + 2.7 * rng.uniform(0, 1, n) ** 0.8
        centre = np.array([0, -0.1, 0])
        t = ValueTracker(0)          # 0 -> 1 collapse

        def state(k):
            s = t.get_value()
            r = r0[k] + (r1[k] - r0[k]) * s
            z = z0[k] * (1 - s) ** 2
            tilt = 1 - 0.68 * s                       # the view tips from face-on ball to an oblique disc
            return r, z, tilt

        angle = [p for p in phi0]
        dots = VGroup(*[Dot(radius=0.035, color=GREY_T) for _ in range(n)])

        def update(group, dt):
            for k, d in enumerate(group):
                r, z, tilt = state(k)
                angle[k] += dt * 0.25 * (2.5 / max(r, 0.3)) ** 1.5 * (0.35 + 1.6 * t.get_value())
                d.move_to(centre + np.array([r * np.cos(angle[k]), tilt * r * np.sin(angle[k]) + z, 0]))
        dots.add_updater(update)
        cap = Text("a cloud of gas and dust, containing many elements, turning slowly", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35)
        self.add(dots, cap); self.wait(3)
        self.remove(cap)
        cap = Text("gravity pulls it inward; as it shrinks it spins faster and flattens into a disc", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35)
        self.add(cap)
        self.play(t.animate.set_value(1), run_time=8, rate_func=smooth)
        sun = Circle(radius=0.05, color=AMBER_H, fill_opacity=0.95, stroke_width=0).move_to(centre)
        self.remove(cap)
        cap = Text("most of the mass falls to the centre, heats up, and becomes the Sun", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35)
        self.add(sun, cap); self.play(sun.animate.scale(7), run_time=2.5); self.wait(1.2)
        frost = Ellipse(width=2 * 1.65, height=2 * 1.65 * 0.32, color=BLUE_H, stroke_width=2).move_to(centre)
        fl = Text("frost line", font_size=18, color=BLUE_H).move_to(centre + np.array([1.0, 0.8, 0]))
        self.remove(cap)
        cap = Text("near the Sun only rock and metal stay solid; further out, ice can freeze too", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35)
        self.add(frost, fl, cap); self.wait(3)
        dots.clear_updaters()
        radii = [0.62, 0.86, 1.1, 1.36, 2.0, 2.5, 2.95, 3.35]
        sizes = [0.045, 0.06, 0.065, 0.05, 0.2, 0.17, 0.11, 0.105]
        cols = [RED_H] * 4 + [TEAL_H] * 4
        ph = rng.uniform(0, TAU, 8)
        planets = VGroup(*[Dot(centre + np.array([r * np.cos(p), 0.32 * r * np.sin(p), 0]), radius=s, color=c_) for r, s, c_, p in zip(radii, sizes, cols, ph)])
        orbits = VGroup(*[Ellipse(width=2 * r, height=2 * r * 0.32, color=GREY_T, stroke_width=1, stroke_opacity=0.5).move_to(centre) for r in radii])
        self.remove(cap)
        cap = Text("grains stick, clumps sweep up their lanes: four small rocky planets, four large gaseous ones", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35)
        self.add(cap)
        self.play(FadeOut(dots), FadeIn(orbits), FadeIn(planets), run_time=3)
        ang = ValueTracker(0)
        for k, pl in enumerate(planets):
            pl.add_updater(lambda m, k=k: m.move_to(centre + np.array([radii[k] * np.cos(ph[k] + ang.get_value() * (radii[0] / radii[k]) ** 1.5),
                                                                       0.32 * radii[k] * np.sin(ph[k] + ang.get_value() * (radii[0] / radii[k]) ** 1.5), 0])))
        self.play(ang.animate.set_value(9), run_time=6, rate_func=linear)
        self.wait(0.5)


class MoonPhases(Scene):
    def construct(self):
        title = Text("One month of the Moon: always half lit, seen from a changing angle", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        centre = np.array([1.6, -0.3, 0]); R = 2.3
        earth = Circle(radius=0.42, color=BLUE_H, fill_opacity=0.4).move_to(centre)
        el = Text("Earth", font_size=16, color=GREY_T).move_to(centre)
        orbit = DashedVMobject(Circle(radius=R, color=GREY_T, stroke_width=1.5).move_to(centre), num_dashes=60)
        rays = VGroup(*[Arrow([6.9, y, 0], [5.7, y, 0], color=AMBER_H, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25) for y in np.linspace(-2.6, 2.0, 5)])
        sl = Text("sunlight", font_size=18, color=AMBER_H).move_to([6.3, 2.5, 0])
        th = ValueTracker(0)

        def moon():
            a = th.get_value(); p = centre + R * np.array([np.cos(a), np.sin(a), 0])
            g = VGroup(Circle(radius=0.26, color=GREY_T, fill_color=DARK, fill_opacity=1, stroke_width=1.5).move_to(p),
                       half_disc(p, 0.26))
            return g

        vc = np.array([-4.4, -0.2, 0]); Rv = 1.15

        def view():
            a = th.get_value() % TAU
            f = (1 - np.cos(a)) / 2
            waxing = a < PI
            col = LIT if f > 0.5 else DARK
            w = max(2 * Rv * abs(1 - 2 * f), 0.002)
            # the same four shapes every frame, so that always_redraw can morph one into the next
            g = VGroup(Circle(radius=Rv, color=GREY_T, fill_color=DARK, fill_opacity=1, stroke_width=2).move_to(vc),
                       half_disc(vc, Rv, right=bool(waxing)),
                       Ellipse(width=w, height=2 * Rv, color=col, fill_color=col, fill_opacity=1, stroke_width=0).move_to(vc),
                       Circle(radius=Rv, color=GREY_T, stroke_width=2).move_to(vc))
            return g

        names = [(0.0, "new Moon"), (0.125, "waxing crescent"), (0.25, "first quarter"), (0.375, "waxing gibbous"), (0.5, "full Moon"),
                 (0.625, "waning gibbous"), (0.75, "last quarter"), (0.875, "waning crescent")]

        def label():
            frac = (th.get_value() % TAU) / TAU
            name = min(names, key=lambda q: min(abs(frac - q[0]), 1 - abs(frac - q[0])))[1]
            return VGroup(Text(f"day {frac*29.5:4.1f}", font_size=24, color=GREY_T).move_to(vc + DOWN * 1.75),
                          Text(name, font_size=24, color=AMBER_H).move_to(vc + DOWN * 2.3))

        vt = Text("seen from the Earth", font_size=20, color=GREY_T).move_to(vc + UP * 1.6)
        self.add(earth, el, orbit, rays, sl, vt, always_redraw(moon), always_redraw(view), always_redraw(label))
        self.wait(1.5)
        self.play(th.animate.set_value(TAU), run_time=20, rate_func=linear)
        cap = Text("29.5 days from new Moon to new Moon", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(3)

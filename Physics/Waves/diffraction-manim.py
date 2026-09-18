"""
diffraction-manim.py — two scenes for [[Diffraction]].

Scene 1  GapWidths    — three ripple tanks side by side, a plane wave meeting a barrier with a
                        gap of ½λ, 2λ and 6λ, run live from the 2-D wave equation.
Scene 2  SlitsToGrating — the far-field pattern redrawn as the number of slits climbs 1 → 2 →
                        3 → 5 → 10 → 40: the single-slit envelope, Young's fringes, then the
                        grating's sharp orders at d sin θ = nλ.

Smoke:   manim -ql --fps 15 diffraction-manim.py GapWidths SlitsToGrating
Final:   manim -qk diffraction-manim.py GapWidths SlitsToGrating
then concat with ffmpeg to diffraction-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *
import numpy as np
import math

GREY = "#888888"
BLUE_, RED_, GREEN_, AMBER, PURPLE_, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"


class Tank:
    def __init__(self, gap_over_lambda, lam=1.0, size=24.0, n=160):
        self.n = n; self.dx = size / n; self.c = 1.0; self.dt = 0.45 * self.dx / self.c
        self.u = np.zeros((n, n)); self.up = np.zeros((n, n)); self.t = 0.0
        self.wall = n // 4; gap = gap_over_lambda * lam / self.dx
        self.mask = np.ones((n, n), bool); self.mask[self.wall, :] = False
        lo, hi = int(n / 2 - gap / 2), int(n / 2 + gap / 2); self.mask[self.wall, lo:hi] = True
        self.f = self.c / lam
    def step(self, k=1):
        for _ in range(k):
            u, up, dx = self.u, self.up, self.dx
            lap = (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u) / dx ** 2
            un = 2 * u - up + (self.c * self.dt) ** 2 * lap
            un[:3, :] = np.sin(2 * math.pi * self.f * self.t) * (1 - math.exp(-self.t))
            un[~self.mask] = 0.0
            for j in range(1, 10):
                un[-j, :] *= 0.9; un[:, j - 1] *= 0.9; un[:, -j] *= 0.9
            self.up, self.u = u, un; self.t += self.dt
    def image(self, width, centre):
        z = np.clip(self.u / 0.9, -1, 1)
        rgb = np.zeros((*z.shape, 3), dtype=np.uint8)
        pos = np.clip(z, 0, 1); neg = np.clip(-z, 0, 1)
        rgb[..., 0] = (30 + 200 * neg).astype(np.uint8); rgb[..., 1] = (30 + 60 * pos + 30 * neg).astype(np.uint8); rgb[..., 2] = (30 + 220 * pos).astype(np.uint8)
        rgb[~self.mask] = (140, 140, 140)
        im = ImageMobject(rgb[::-1]); im.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        im.stretch_to_fit_width(width).stretch_to_fit_height(width).move_to(centre)
        return im


class GapWidths(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("A plane wave meets a gap — the narrower the gap, the more the wave spreads", font_size=28, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        gaps = (0.5, 2.0, 6.0); tanks = [Tank(g) for g in gaps]
        w = 4.0; xs = (-4.4, 0.0, 4.4)
        labels = VGroup(*[Text(f"gap = {g:g} λ", font_size=22, color=AMBER).move_to([x, -2.75, 0]) for g, x in zip(gaps, xs)])
        self.add(labels)
        pics = [t.image(w, np.array([x, -0.35, 0])) for t, x in zip(tanks, xs)]
        for p in pics: self.add(p)
        for frame in range(110):
            for i, t in enumerate(tanks):
                t.step(3)
                self.remove(pics[i]); pics[i] = t.image(w, np.array([xs[i], -0.35, 0])); self.add(pics[i])
            self.wait(1 / 15)
        cap = Text("half a wavelength: near-semicircular wavefronts  ·  two: a beam with bent edges  ·  six: nearly straight through", font_size=17, color=GREY).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(cap)); self.wait(1.5)


class SlitsToGrating(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("One slit, two, many: the far-field pattern as the slits multiply", font_size=28, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        lam, a, d = 1.0, 2.0, 8.0
        th = np.radians(np.linspace(-32, 32, 900)); s = np.sin(th); k = 2 * math.pi / lam
        ax = Axes(x_range=[-0.5, 0.5, 0.125], y_range=[0, 1.05, 0.5], x_length=11.5, y_length=4.2, axis_config={"color": GREY, "include_tip": False, "font_size": 18}).move_to([0, -0.4, 0])
        ax.add_coordinates()
        self.add(ax, Text("sin θ", font_size=18, color=GREY).next_to(ax.x_axis, DOWN, buff=0.15))
        for n in range(-4, 5):
            self.add(DashedLine(ax.c2p(n * lam / d, 0), ax.c2p(n * lam / d, 1.05), color=GREY, stroke_width=1, dash_length=0.08))
        self.add(Text("dotted: d sin θ = nλ", font_size=16, color=GREY).move_to([4.6, 1.75, 0]))
        curve = None; label = None
        for N, col, note in ((1, RED_, "one slit of width a: the envelope, minima at sin θ = λ/a"), (2, BLUE_, "two slits: Young's fringes, spaced λ/d, inside the envelope"),
                             (3, TEAL, "three slits: one small secondary maximum between each pair"), (5, PURPLE_, "five: the maxima sharpen, the secondaries fade"),
                             (10, GREEN_, "ten"), (40, AMBER, "forty: a grating — sharp orders at d sin θ = nλ, nothing between")):
            centres = (np.arange(N) - (N - 1) / 2) * d
            xs_ = np.concatenate([np.linspace(c - a / 2, c + a / 2, 60) for c in centres])
            I = np.abs(np.exp(1j * k * np.outer(s, xs_)).sum(1)) ** 2; I /= I.max()
            pts = [ax.c2p(float(si), float(Ii)) for si, Ii in zip(s, I)]
            newcurve = VMobject(color=col, stroke_width=2.5).set_points_as_corners(pts)
            newlabel = Text(f"N = {N}: {note}", font_size=19, color=col).to_edge(DOWN, buff=0.25)
            if curve is None:
                curve, label = newcurve, newlabel; self.play(Create(curve), FadeIn(label), run_time=1.5)
            else:
                self.play(Transform(curve, newcurve), Transform(label, newlabel), run_time=1.6)
            self.wait(1.4 if N in (1, 2, 40) else 0.9)
        self.wait(1.0)

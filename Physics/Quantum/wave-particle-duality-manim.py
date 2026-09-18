"""
wave-particle-duality-manim.py — two scenes for [[Wave-Particle Duality]].

Scene 1  OneAtATime     — photons arriving one by one on a screen behind two slits; the count
                          climbs and the fringes rise out of noise (Taylor 1909, Tonomura 1989).
Scene 2  Photoelectric  — photons of rising frequency strike a sodium plate: below the threshold
                          nothing leaves however many arrive; above it electrons fly out with
                          KE_max = hf − Φ, and doubling the intensity doubles the electrons, not
                          their energy.

Smoke:   manim -ql --fps 15 wave-particle-duality-manim.py OneAtATime Photoelectric
Final:   manim -qk wave-particle-duality-manim.py OneAtATime Photoelectric
then concat with ffmpeg to wave-particle-duality-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *
import numpy as np

GREY = "#888888"
BLUE_, RED_, GREEN_, AMBER, PURPLE_, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
def photon_hits():
    """Regenerate the original seed-1909 sample; no external scratch data required."""
    x = np.linspace(-0.6, 0.6, 24001)
    lam, width, spacing, distance = 600e-9, 2e-6, 10e-6, 2.0
    sine = np.sin(np.arctan(x / distance))
    beta = np.pi * width * sine / lam
    alpha = np.pi * spacing * sine / lam
    envelope = np.where(beta == 0, 1.0,
                        (np.sin(beta) / np.where(beta == 0, 1, beta)) ** 2)
    density = envelope * np.cos(alpha) ** 2
    cumulative = np.cumsum(density)
    cumulative /= cumulative[-1]
    return np.interp(np.random.default_rng(1909).random(20000), cumulative, x)


class OneAtATime(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Two slits, one photon at a time: each arrives as a dot, the wave decides where", font_size=24, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        hits = photon_hits(); hits = hits[np.abs(hits) <= 0.3]          # the screen shows ±0.3 m
        # screen: x in [-0.3, 0.3] m → scene x in [-6, 6]; dots scattered in y
        rng = np.random.default_rng(5)
        frame = Rectangle(width=12.2, height=3.2, color=GREY, stroke_width=1.5).move_to([0, -0.4, 0])
        self.add(frame, Text("screen", font_size=16, color=GREY).next_to(frame, LEFT, buff=0.15).rotate(PI / 2))
        counter = Text("photons: 0", font_size=26, color=AMBER).move_to([0, 1.85, 0]); self.add(counter)
        dots = VGroup(); shown = 0
        batches = [1] * 12 + [2] * 6 + [5] * 6 + [10] * 6 + [25] * 6 + [60] * 6 + [150] * 6 + [400] * 5 + [1000] * 4 + [2500] * 4
        for b in batches:
            new = VGroup(*[Dot([hits[shown + i] * 20, -0.4 + rng.uniform(-1.5, 1.5), 0], radius=0.03, color=AMBER).set_opacity(0.85) for i in range(b) if shown + i < len(hits)])
            shown = min(shown + b, len(hits))
            self.add(new); dots.add(new)
            self.remove(counter); counter = Text(f"photons: {shown}", font_size=26, color=AMBER).move_to([0, 1.85, 0]); self.add(counter)
            self.wait(0.35 if b <= 5 else 0.22)
        cap = Text("no photon interferes with another — one at a time is enough; each interferes with itself, through both slits", font_size=19, color=GREY).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(cap)); self.wait(2.0)


class Photoelectric(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("The photoelectric effect: frequency sets the electrons' energy, intensity how many", font_size=24, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        h, e = 6.626e-34, 1.602e-19; phi = 2.28                      # sodium, eV
        plate = Rectangle(width=0.5, height=3.2, color=GREY, fill_color=GREY, fill_opacity=0.35).move_to([-1.5, -0.4, 0])
        self.add(plate, Text("sodium\nΦ = 2.28 eV", font_size=18, color=GREY, line_spacing=0.9).next_to(plate, DOWN, buff=0.2))
        # energy bar on the right
        ax = Axes(x_range=[0, 1, 1], y_range=[0, 5, 1], x_length=1.2, y_length=3.4, axis_config={"color": GREY, "include_tip": False, "font_size": 16}).move_to([4.6, -0.3, 0])
        ax.add_coordinates(); self.add(ax, Text("energy (eV)", font_size=16, color=GREY).next_to(ax, UP, buff=0.1))
        phi_bar = Rectangle(width=0.6, height=3.4 * phi / 5, color=RED_, fill_color=RED_, fill_opacity=0.35, stroke_width=1).move_to(ax.c2p(0.5, phi / 2))
        self.add(phi_bar, Text("Φ", font_size=18, color=RED_).next_to(phi_bar, LEFT, buff=0.1))
        label = Text("", font_size=22, color=AMBER).move_to([1.0, 2.1, 0]); self.add(label)
        note = Text("", font_size=19, color=GREY).to_edge(DOWN, buff=0.35); self.add(note)
        def shoot(lam_nm, n_photons, col, text):
            nonlocal label, note
            f = 3e8 / (lam_nm * 1e-9); E = h * f / e; ke = E - phi
            self.remove(label); label = Text(f"λ = {lam_nm} nm    f = {f/1e14:.1f} × 10¹⁴ Hz    E = hf = {E:.2f} eV", font_size=22, color=col).move_to([1.0, 2.1, 0]); self.add(label)
            self.remove(note); note = Text(text, font_size=19, color=col).to_edge(DOWN, buff=0.35); self.add(note)
            photons = VGroup(*[Dot([-6.3, -0.4 + (i - (n_photons - 1) / 2) * 0.5, 0], radius=0.07, color=col) for i in range(n_photons)])
            self.add(photons)
            self.play(photons.animate.shift(RIGHT * 4.55), run_time=1.0, rate_func=linear)
            self.remove(photons)
            if ke > 0:
                ke_bar = Rectangle(width=0.6, height=3.4 * ke / 5, color=GREEN_, fill_color=GREEN_, fill_opacity=0.5, stroke_width=1).move_to(ax.c2p(0.5, phi + ke / 2))
                kel = Text(f"KE_max = {ke:.2f} eV", font_size=16, color=GREEN_).next_to(ke_bar, RIGHT, buff=0.1)
                electrons = VGroup(*[Dot([-1.2, -0.4 + (i - (n_photons - 1) / 2) * 0.5, 0], radius=0.06, color=GREEN_) for i in range(n_photons)])
                self.add(ke_bar, kel, electrons)
                self.play(electrons.animate.shift(RIGHT * (1.0 + 2.2 * ke / 3)), run_time=0.8, rate_func=linear)
                self.wait(0.8); self.remove(ke_bar, kel, electrons)
            else:
                self.wait(1.0)
        shoot(700, 3, RED_, "red: 1.77 eV per photon < Φ — no electron leaves, however many photons arrive")
        shoot(700, 8, RED_, "brighter red: eight photons — still none; a photon cannot pool its energy with another")
        shoot(400, 3, BLUE_, "violet: 3.10 eV per photon — each frees one electron with 3.10 − 2.28 = 0.82 eV")
        shoot(400, 8, BLUE_, "brighter violet: more electrons, the SAME maximum energy — intensity is photons per second")
        shoot(250, 3, PURPLE_, "ultraviolet: 4.96 eV — faster electrons, 2.68 eV; hf = Φ + KE_max")
        self.wait(1.5)

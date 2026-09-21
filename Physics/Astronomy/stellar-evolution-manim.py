"""Manim scenes for [[Stellar Evolution]].
Scene 1  SunLife    — a Sun-like star in cross-section beside its point on the HR diagram.  The core
                      runs out of hydrogen, SHRINKS and heats while the envelope SWELLS and cools;
                      helium ignites; the envelope is thrown off and a white dwarf is left to cool.
Scene 2  Countdown  — a 25-solar-mass star lights one fuel after another.  Each stage is shorter than
                      the last (7 million years ... 1 day), iron pays nothing, the core collapses.
Smoke:  manim -ql --fps 15 stellar-evolution-manim.py SunLife Countdown
Final:  manim -qk stellar-evolution-manim.py SunLife Countdown      then concat with ffmpeg.
Stage times: Woosley, Heger & Weaver (2002), 25 solar masses, rounded.  Solar track: Sackmann et al. (1993).
Sizes are NOT to scale: a red giant is over a hundred times wider than the star it came from."""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H, TEAL_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"


def hr_point(T, L, origin, w=4.4, hgt=4.6):
    """log T from 40000 (left) to 2500 (right); log L from 1e-4 to 1e4."""
    fx = (np.log10(40000) - np.log10(T)) / (np.log10(40000) - np.log10(2500))
    fy = (np.log10(L) + 4) / 8
    return origin + np.array([fx * w, fy * hgt, 0])


def hr_axes(origin, w=4.4, hgt=4.6):
    g = VGroup(Line(origin, origin + RIGHT * w, color=GREY_T, stroke_width=2), Line(origin, origin + UP * hgt, color=GREY_T, stroke_width=2))
    g.add(Text("hot", font_size=18, color=GREY_T).next_to(origin, DOWN, buff=0.12).shift(RIGHT * 0.25))
    g.add(Text("cool", font_size=18, color=GREY_T).next_to(origin + RIGHT * w, DOWN, buff=0.12).shift(LEFT * 0.3))
    g.add(Text("surface temperature", font_size=18, color=GREY_T).next_to(origin + RIGHT * w / 2, DOWN, buff=0.12))
    g.add(Text("luminosity", font_size=18, color=GREY_T).rotate(PI / 2).next_to(origin + UP * hgt / 2, LEFT, buff=0.12))
    ms = [(30000, 5000), (15000, 400), (9700, 38), (5772, 1), (3850, 0.069), (3000, 0.002)]
    band = VMobject(color=GREEN_H, stroke_width=10, stroke_opacity=0.3).set_points_smoothly([hr_point(t, l, origin, w, hgt) for t, l in ms])
    g.add(band, Text("main sequence", font_size=16, color=GREEN_H).move_to(hr_point(16000, 12, origin, w, hgt)))
    return g


class SunLife(Scene):
    def construct(self):
        title = Text("One solar mass, twelve billion years", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        centre = np.array([-3.4, 0.2, 0]); origin = np.array([1.4, -2.2, 0])
        axes = hr_axes(origin); self.add(axes)
        env = Circle(radius=1.0, color=AMBER_H, fill_opacity=0.35, stroke_width=3).move_to(centre)
        core = Circle(radius=0.34, color=AMBER_H, fill_opacity=0.9, stroke_width=0).move_to(centre)
        note = Text("sizes not to scale", font_size=16, color=GREY_T).move_to([-5.9, 3.25, 0])
        dot = Dot(hr_point(5772, 1, origin), color=AMBER_H, radius=0.09)
        trail = TracedPath(dot.get_center, stroke_color=AMBER_H, stroke_width=3)
        age = Text("age 4.6 billion years: today", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        cap = Text("gravity pulls in; hot gas pushes out; they balance", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.85)
        arrows = VGroup()
        for a in np.arange(0, TAU, TAU / 6):
            u = np.array([np.cos(a), np.sin(a), 0])
            arrows.add(Arrow(centre + 1.75 * u, centre + 1.12 * u, color=BLUE_H, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.3))
            v = np.array([np.cos(a + TAU / 12), np.sin(a + TAU / 12), 0])
            arrows.add(Arrow(centre + 0.42 * v, centre + 0.95 * v, color=RED_H, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.3))
        key = VGroup(Text("gravity", font_size=18, color=BLUE_H), Text("pressure", font_size=18, color=RED_H)).arrange(RIGHT, buff=0.5).move_to(centre + UP * 2.35)
        self.add(env, core, note, trail, dot, age, cap, arrows, key)
        self.wait(3)

        def step(age_text, cap_text, env_r, env_col, core_r, core_col, T, L, run=4, keep_arrows=False):
            new_age = Text(age_text, font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
            new_cap = Text(cap_text, font_size=22, color=GREY_T).to_edge(DOWN, buff=0.85)
            self.remove(age, cap); self.add(new_age, new_cap)
            anims = [env.animate.scale_to_fit_width(2 * env_r).set_color(env_col), core.animate.scale_to_fit_width(2 * core_r).set_color(core_col),
                     dot.animate.move_to(hr_point(T, L, origin))]
            self.play(*anims, run_time=run, rate_func=smooth)
            self.wait(1.6)
            return new_age, new_cap

        self.remove(arrows, key)
        age, cap = step("age 10.9 billion years", "core hydrogen gone: no fusion there, so gravity squeezes the core", 1.15, AMBER_H, 0.26, "#fde68a", 5520, 2.2, run=3)
        age, cap = step("age 12.2 billion years: red giant", "the core SHRINKS and heats; the envelope SWELLS and cools", 2.35, RED_H, 0.13, WHITE, 3110, 2350, run=5)
        age, cap = step("helium ignites in the core at 100 million K", "a second fuel: the star settles, smaller and hotter, for 100 million years", 1.45, "#fb923c", 0.17, "#fde68a", 4720, 44, run=3)
        age, cap = step("helium gone too: the second climb", "again the core shrinks and the envelope swells, larger than before", 2.55, RED_H, 0.10, WHITE, 3160, 3000, run=4)
        # envelope leaves
        self.remove(age, cap)
        age = Text("the envelope drifts away: a planetary nebula", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        cap = Text("too little mass to light carbon: the bare core is a white dwarf", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.85)
        self.add(age, cap)
        ring = Circle(radius=2.55, color=TEAL_H, stroke_width=6, fill_opacity=0).move_to(centre)
        self.add(ring)
        self.play(env.animate.set_opacity(0), ring.animate.scale(1.35).set_stroke(opacity=0.25), dot.animate.move_to(hr_point(30000, 2000, origin)), run_time=4)
        self.play(dot.animate.move_to(hr_point(36000, 100, origin)), run_time=1.5)
        self.play(dot.animate.move_to(hr_point(12000, 0.004, origin)), ring.animate.set_stroke(opacity=0.08), core.animate.set_color("#bfdbfe"), run_time=4)
        self.remove(age, cap)
        age = Text("white dwarf: the size of the Earth, no fuel, cooling for ever", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        cap = Text("every step was gravity squeezing a core that had stopped paying", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.85)
        self.add(age, cap); self.wait(4)


class Countdown(Scene):
    def construct(self):
        title = Text("Twenty-five solar masses: each fuel buys less time", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        centre = np.array([-3.3, -0.1, 0])
        stages = [("hydrogen to helium", "7 million years", 2.6, AMBER_H), ("helium to carbon", "800 000 years", 2.15, "#fb923c"),
                  ("carbon to neon", "500 years", 1.72, RED_H), ("neon to oxygen", "1 year", 1.32, PURPLE_H),
                  ("oxygen to silicon", "5 months", 0.95, BLUE_H), ("silicon to iron", "1 day", 0.6, TEAL_H)]
        shells = VGroup(); rows = VGroup()
        head = Text("what is burning at the centre      it lasts", font_size=20, color=GREY_T).move_to([3.1, 2.55, 0])
        self.add(head)
        waits = [2.6, 2.2, 1.8, 1.4, 1.1, 0.9]
        for k, ((name, t, r, col), w) in enumerate(zip(stages, waits)):
            c = Circle(radius=r, color=col, fill_opacity=0.28, stroke_width=3).move_to(centre)
            shells.add(c)
            row = VGroup(Text(name, font_size=22, color=col), Text(t, font_size=22, color=GREY_T))
            row[0].move_to([1.9, 1.9 - 0.62 * k, 0]).align_to([0.4, 0, 0], LEFT); row[1].move_to([5.2, 1.9 - 0.62 * k, 0]).align_to([4.5, 0, 0], LEFT)
            rows.add(row)
            self.play(FadeIn(c, scale=0.6), FadeIn(row), run_time=0.7)
            self.wait(w)
        iron = Circle(radius=0.3, color=GREY_T, fill_opacity=0.95, stroke_width=0).move_to(centre)
        irow = Text("iron: fusing it releases nothing", font_size=22, color=GREY_T).move_to([2.9, 1.9 - 0.62 * 6, 0]).align_to([0.4, 0, 0], LEFT)
        cap = Text("the core now has gravity and no income", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(iron), FadeIn(irow), run_time=0.7); self.add(cap); self.wait(2.5)
        self.remove(cap)
        cap = Text("collapse: from the size of the Earth to 25 km across in under a second", font_size=22, color=RED_H).to_edge(DOWN, buff=0.4)
        self.add(cap)
        self.play(iron.animate.scale(0.18).set_color(WHITE), run_time=0.5, rate_func=rush_into)
        flash = Circle(radius=0.1, color=WHITE, fill_opacity=0.9, stroke_width=0).move_to(centre)
        self.add(flash)
        self.play(flash.animate.scale(40).set_opacity(0), *[s.animate.scale(1.35).set_fill(opacity=0).set_stroke(opacity=0.4) for s in shells], run_time=2.2)
        self.remove(flash, cap)
        cap = Text("supernova: a nebula of new elements, and a neutron star where the core was", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.4)
        ns = Text("neutron star", font_size=18, color=GREY_T).next_to(iron, DOWN, buff=0.15)
        self.add(cap, ns)
        self.play(*[s.animate.scale(1.08).set_stroke(opacity=0.22) for s in shells], run_time=3)
        self.wait(2.5)

"""Manim scenes for [[Sound]].
Scene 1  LongitudinalWave — rows of air particles shuttling to and fro while the pattern of
                            compressions travels; one particle is marked so the eye can see
                            it never goes anywhere; the pressure graph below keeps step.
Scene 2  LoudAndHigh      — an oscilloscope trace: amplitude up (louder), then frequency up
                            (higher pitch), independently.
Smoke:  manim -ql --fps 15 sound-manim.py LongitudinalWave LoudAndHigh
Final:  manim -qk sound-manim.py LongitudinalWave LoudAndHigh   then concat with ffmpeg."""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H, TEAL_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"


class LongitudinalWave(Scene):
    def construct(self):
        title = Text("Sound in air: the pattern travels, the particles only shuttle", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        lam, A, T = 3.0, 0.32, 2.0
        xs = np.linspace(-6, 6, 61); rows = np.linspace(1.9, 0.3, 6)
        t = ValueTracker(0)
        def pos(x, time): return x + A * np.sin(2 * np.pi * (x / lam - time / T))
        dots = VGroup(*[Dot([pos(x, 0), y, 0], radius=0.045, color=TEAL_H) for y in rows for x in xs])
        mark_i = 3 * len(xs) + 30
        dots[mark_i].set_color(RED_H).scale(1.9)
        def upd(group):
            k = 0
            for y in rows:
                for x in xs:
                    group[k].move_to([pos(x, t.get_value()), y, 0]); k += 1
        dots.add_updater(upd)
        ax = Axes(x_range=[-6, 6, 3], y_range=[-1.3, 1.3, 1], x_length=12, y_length=1.9, axis_config={"color": GREY_T, "include_tip": False}).move_to([0, -1.7, 0])
        graph = always_redraw(lambda: ax.plot(lambda x: -np.cos(2 * np.pi * (x / lam - t.get_value() / T)), color=PURPLE_H, stroke_width=3))
        plab = Text("pressure", font_size=18, color=PURPLE_H).next_to(ax, LEFT, buff=0.1).shift(UP * 0.5 + RIGHT * 1.0)
        # a compression sits where x/lam - t/T = 1/2 (+n); this one crosses the screen during the second half
        cl = always_redraw(lambda: Text("C", font_size=26, color=RED_H, weight=BOLD).move_to([lam * (t.get_value() / T + 0.5) - 15.0, 2.35, 0]))
        note = Text("the red particle goes nowhere; the crowded band (C) moves on", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(dots, ax, graph, plab)
        self.wait(1)
        self.play(t.animate.set_value(3 * T), run_time=9, rate_func=linear)
        self.add(note, cl)
        self.play(t.animate.set_value(6 * T), run_time=9, rate_func=linear)
        self.wait(1)


class LoudAndHigh(Scene):
    def construct(self):
        title = Text("On the oscilloscope: height is loudness, crowding is pitch", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        ax = Axes(x_range=[0, 10, 1], y_range=[-1.2, 1.2, 0.5], x_length=11, y_length=4.2, axis_config={"color": GREY_T, "include_tip": False}).shift(DOWN * 0.3)
        grid = VGroup(*[Line(ax.c2p(x, -1.2), ax.c2p(x, 1.2), color=GREY_T, stroke_width=1, stroke_opacity=0.25) for x in range(11)],
                      *[Line(ax.c2p(0, y), ax.c2p(10, y), color=GREY_T, stroke_width=1, stroke_opacity=0.25) for y in np.arange(-1, 1.1, 0.5)])
        amp, f = ValueTracker(0.3), ValueTracker(0.3)
        trace = always_redraw(lambda: ax.plot(lambda x: amp.get_value() * np.sin(2 * np.pi * f.get_value() * x), color=GREEN_H, stroke_width=4, x_range=[0, 10, 0.01]))
        label = Text("a quiet, low note", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.35)
        self.add(grid, ax, trace, label); self.wait(1.5)
        label.become(Text("turn the volume up: amplitude grows, the waves are no closer together: LOUDER, same pitch", font_size=22, color=RED_H).to_edge(DOWN, buff=0.35))
        self.play(amp.animate.set_value(1.0), run_time=3); self.wait(1.5)
        self.play(amp.animate.set_value(0.3), run_time=1.5)
        label.become(Text("play a higher note: more waves in the same time, the height unchanged: HIGHER PITCH, same loudness", font_size=22, color=BLUE_H).to_edge(DOWN, buff=0.35))
        self.play(f.animate.set_value(0.9), run_time=3); self.wait(1.5)
        label.become(Text("amplitude and frequency are independent: any loudness at any pitch", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35))
        self.play(amp.animate.set_value(1.0), run_time=2); self.play(f.animate.set_value(0.4), run_time=2); self.wait(2)

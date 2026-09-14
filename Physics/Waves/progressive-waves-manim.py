"""
progressive-waves-manim.py — two scenes for [[Progressive Waves]].

Scene 1  TwoWaves      — a transverse and a longitudinal wave side by side on the same
                         row of particles, one tracked particle in each painted amber:
                         the pattern travels right, the particle never leaves home.
Scene 2  TwoGraphs     — the same travelling wave photographed (displacement–distance,
                         reads λ) and filmed at one point (displacement–time, reads T);
                         two particles a quarter wavelength apart lag by a quarter period.

Smoke:   manim -ql --fps 15 progressive-waves-manim.py TwoWaves TwoGraphs
Final:   manim -qk progressive-waves-manim.py TwoWaves TwoGraphs
then concat with ffmpeg to progressive-waves-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *
import numpy as np

GREY = "#888888"
BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"

LAM = 3.0          # wavelength in scene units
PERIOD = 2.0       # seconds
A = 0.55           # amplitude (transverse) / max longitudinal shift
N = 40             # particles


class TwoWaves(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("The pattern travels; the particles stay home", font_size=34, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        x0 = np.linspace(-5.8, 5.8, N)
        t = ValueTracker(0.0)
        k, w = 2 * PI / LAM, 2 * PI / PERIOD

        # --- transverse row (upper) ---
        yT = 1.4
        labT = Text("TRANSVERSE — vibration at right angles to the travel", font_size=20, color=BLUE).move_to([0, yT + 1.15, 0])
        dotsT = VGroup(*[Dot(radius=0.07, color=BLUE) for _ in x0])
        trackT = 14
        dotsT[trackT].set_color(AMBER).scale(1.6)

        def upd_T(g):
            tt = t.get_value()
            for d, x in zip(g, x0):
                d.move_to([x, yT + A * np.sin(k * x - w * tt), 0])
        dotsT.add_updater(upd_T)
        homeT = DashedLine([x0[trackT], yT - A - 0.15, 0], [x0[trackT], yT + A + 0.15, 0], color=AMBER, stroke_width=1.5, dash_length=0.08)

        # --- longitudinal row (lower) ---
        yL = -1.6
        labL = Text("LONGITUDINAL — vibration along the travel", font_size=20, color=PURPLE).move_to([0, yL + 0.9, 0])
        dotsL = VGroup(*[Dot(radius=0.07, color=PURPLE) for _ in x0])
        trackL = 14
        dotsL[trackL].set_color(AMBER).scale(1.6)

        def upd_L(g):
            tt = t.get_value()
            for d, x in zip(g, x0):
                d.move_to([x + 0.28 * np.sin(k * x - w * tt), yL, 0])
        dotsL.add_updater(upd_L)
        homeL = DashedLine([x0[trackL], yL - 0.35, 0], [x0[trackL], yL + 0.35, 0], color=AMBER, stroke_width=1.5, dash_length=0.08)
        capC = Text("compression", font_size=15, color=GREY).move_to([0, yL - 0.55, 0])
        capR = Text("rarefaction", font_size=15, color=GREY).move_to([LAM / 2, yL - 0.55, 0])

        upd_T(dotsT); upd_L(dotsL)
        self.play(FadeIn(labT), FadeIn(dotsT), FadeIn(homeT), FadeIn(labL), FadeIn(dotsL), FadeIn(homeL), run_time=0.8)
        arrow = Arrow([-1.2, 0, 0], [1.2, 0, 0], color=GREY, buff=0, stroke_width=3)
        arrlab = Text("energy travels this way", font_size=17, color=GREY).next_to(arrow, DOWN, buff=0.05)
        self.play(GrowArrow(arrow), FadeIn(arrlab), run_time=0.5)

        # run one period slowly, then two more
        self.play(t.animate.set_value(PERIOD), run_time=4.0, rate_func=linear)
        # captions for the compression/rarefaction move with the pattern; show them at a moment
        self.play(FadeIn(capC), FadeIn(capR), run_time=0.3)
        self.wait(0.8)
        self.play(FadeOut(capC), FadeOut(capR), run_time=0.3)
        self.play(t.animate.set_value(3 * PERIOD), run_time=8.0, rate_func=linear)
        note = Text("the amber particle: one oscillation per period, never a step to the right", font_size=18, color=AMBER).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.4)
        self.play(t.animate.set_value(4.5 * PERIOD), run_time=6.0, rate_func=linear)
        self.wait(0.5)


class TwoGraphs(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("One wave, two graphs: a photograph reads λ, a film at one point reads T", font_size=28, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        k, w = 2 * PI / LAM, 2 * PI / PERIOD
        t = ValueTracker(0.0)

        # left: displacement–distance (photograph), right: displacement–time at x = xP
        axL = Axes(x_range=[0, 2 * LAM, LAM / 2], y_range=[-1, 1, 0.5], x_length=6.0, y_length=2.6,
                   axis_config={"color": GREY, "include_numbers": False, "stroke_width": 2}).move_to([-3.4, 0.2, 0])
        axR = Axes(x_range=[0, 2 * PERIOD, PERIOD / 2], y_range=[-1, 1, 0.5], x_length=5.6, y_length=2.6,
                   axis_config={"color": GREY, "include_numbers": False, "stroke_width": 2}).move_to([3.4, 0.2, 0])
        lL = Text("displacement against DISTANCE  (snapshot, t frozen)", font_size=17, color=BLUE).next_to(axL, UP, buff=0.15)
        lR = Text("displacement against TIME  (at one point P)", font_size=17, color=TEAL).next_to(axR, UP, buff=0.15)
        xlabL = Text("x", font_size=18, color=GREY).next_to(axL.x_axis.get_end(), RIGHT, buff=0.1)
        xlabR = Text("t", font_size=18, color=GREY).next_to(axR.x_axis.get_end(), RIGHT, buff=0.1)
        self.play(Create(axL), Create(axR), FadeIn(lL), FadeIn(lR), FadeIn(xlabL), FadeIn(xlabR), run_time=1.0)

        xP = LAM * 0.75
        xQ = xP + LAM / 4
        curve = always_redraw(lambda: axL.plot(lambda x: A / 0.55 * 0.9 * np.sin(k * x - w * t.get_value()), x_range=[0, 2 * LAM], color=BLUE, stroke_width=3))
        dotP = always_redraw(lambda: Dot(axL.c2p(xP, 0.9 * np.sin(k * xP - w * t.get_value())), color=AMBER, radius=0.09))
        dotQ = always_redraw(lambda: Dot(axL.c2p(xQ, 0.9 * np.sin(k * xQ - w * t.get_value())), color=GREEN, radius=0.09))
        labP = Text("P", font_size=18, color=AMBER).next_to(axL.c2p(xP, -1.05), DOWN, buff=0.05)
        labQ = Text("Q", font_size=18, color=GREEN).next_to(axL.c2p(xQ, -1.05), DOWN, buff=0.05)
        self.play(Create(curve), FadeIn(dotP), FadeIn(dotQ), FadeIn(labP), FadeIn(labQ), run_time=0.8)

        # wavelength brace on the snapshot
        br = BraceBetweenPoints(axL.c2p(LAM / 4, 1.0), axL.c2p(5 * LAM / 4, 1.0), direction=UP, color=GREY)
        brl = Text("λ  (crest to crest)", font_size=16, color=GREY).next_to(br, UP, buff=0.05)
        self.play(FadeIn(br), FadeIn(brl), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(br), FadeOut(brl), run_time=0.3)

        # the film: traces of P and Q grow as t advances
        traceP = always_redraw(lambda: axR.plot(lambda s: 0.9 * np.sin(k * xP - w * s), x_range=[0, max(t.get_value(), 1e-3)], color=AMBER, stroke_width=3))
        traceQ = always_redraw(lambda: axR.plot(lambda s: 0.9 * np.sin(k * xQ - w * s), x_range=[0, max(t.get_value(), 1e-3)], color=GREEN, stroke_width=3))
        headP = always_redraw(lambda: Dot(axR.c2p(t.get_value(), 0.9 * np.sin(k * xP - w * t.get_value())), color=AMBER, radius=0.08))
        headQ = always_redraw(lambda: Dot(axR.c2p(t.get_value(), 0.9 * np.sin(k * xQ - w * t.get_value())), color=GREEN, radius=0.08))
        self.add(traceP, traceQ, headP, headQ)
        self.play(t.animate.set_value(2 * PERIOD), run_time=8.0, rate_func=linear)

        brT = BraceBetweenPoints(axR.c2p(0.5 * PERIOD, -1.0), axR.c2p(1.5 * PERIOD, -1.0), direction=DOWN, color=GREY)
        brTl = Text("T  (one full oscillation of P)", font_size=16, color=GREY).next_to(brT, DOWN, buff=0.05)
        self.play(FadeIn(brT), FadeIn(brTl), run_time=0.5)
        note = Text("Q is a quarter wavelength beyond P, so Q does what P did a quarter period ago: phase lag 90°",
                    font_size=18, color=GREY).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(2.0)

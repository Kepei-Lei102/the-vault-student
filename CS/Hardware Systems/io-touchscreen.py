"""Touchscreens — pressure, charge, shadow. The three sensing mechanisms in motion.

Renders io-touchscreen.mp4 (embed beside the card).
Smoke: manim -qm io-touchscreen.py Touchscreen
Final: manim -qk io-touchscreen.py Touchscreen
"""
from manim import *

BLUE_ = "#2563eb"
PURPLE = "#7c3aed"
AMBER = "#f59e0b"
TEAL = "#0891b2"
GREEN = "#059669"
RED_ = "#dc2626"
GRAY = "#9a9a9a"

config.background_color = "#1a1a1a"


class Touchscreen(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=28, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap), FadeIn(cap), run_time=0.6)
        else:
            self.play(FadeIn(cap), run_time=0.6)
        self._cap = cap

    def clear_cap(self):
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap), run_time=0.4)
            self._cap = None

    def construct(self):
        # ================= ACT 1 — RESISTIVE =================
        title1 = Text("1. Resistive - pressure", font_size=34, color=BLUE_).to_edge(UP, buff=0.3)
        self.play(FadeIn(title1), run_time=0.8)

        glass = Rectangle(width=9, height=0.5, stroke_color=GRAY, stroke_width=2,
                          fill_color=GRAY, fill_opacity=0.10).move_to([0, -1.9, 0])
        bot_layer = Rectangle(width=9, height=0.16, stroke_color=TEAL, stroke_width=2,
                              fill_color=TEAL, fill_opacity=0.4).move_to([0, -1.52, 0])
        top_layer = Line([-4.5, -0.5, 0], [4.5, -0.5, 0], color=BLUE_, stroke_width=5)

        lab_top = Text("flexible layer", font_size=22, color=BLUE_).move_to([5.75, -0.5, 0])
        lab_gap = Text("air gap", font_size=20, color=GRAY).move_to([5.75, -1.05, 0])
        lab_bot = Text("fixed layer", font_size=22, color=TEAL).move_to([5.75, -1.52, 0])
        lab_gls = Text("glass", font_size=20, color=GRAY).move_to([5.75, -1.95, 0])

        self.play(FadeIn(glass), FadeIn(bot_layer), Create(top_layer),
                  FadeIn(lab_top), FadeIn(lab_gap), FadeIn(lab_bot), FadeIn(lab_gls),
                  run_time=1.4)
        self.swap_caption("Two conductive layers held a hair apart.")
        self.wait(1.2)

        stylus = Polygon([1.2, -0.5, 0], [0.9, 1.4, 0], [1.5, 1.4, 0],
                         stroke_color=GRAY, stroke_width=2,
                         fill_color=GRAY, fill_opacity=0.35).shift(UP * 1.6)
        self.play(FadeIn(stylus), run_time=0.5)

        bent = VMobject(stroke_color=BLUE_, stroke_width=5)
        bent.set_points_smoothly([
            [-4.5, -0.5, 0], [-0.2, -0.5, 0], [1.2, -1.42, 0], [2.6, -0.5, 0], [4.5, -0.5, 0],
        ])
        contact = Dot([1.2, -1.44, 0], radius=0.11, color=AMBER)
        self.play(stylus.animate.shift(DOWN * 1.6),
                  Transform(top_layer, bent), run_time=1.0)
        self.play(FadeIn(contact), Flash(contact, color=AMBER, flash_radius=0.4), run_time=0.7)
        self.swap_caption("Any press connects them - stylus, glove, fingernail.", BLUE_)
        self.wait(1.4)

        v0 = Text("0 V", font_size=24, color=TEAL).move_to([-4.95, -2.5, 0])
        v5 = Text("+5 V", font_size=24, color=TEAL).move_to([4.95, -2.5, 0])
        measure = DoubleArrow([-4.5, -2.6, 0], [1.2, -2.6, 0], color=AMBER,
                              stroke_width=3, buff=0, tip_length=0.2)
        readout = Text("the voltage at the contact reads off x", font_size=24, color=AMBER)
        readout.move_to([-1.0, -3.1, 0])
        self.play(FadeIn(v0), FadeIn(v5), GrowFromEdge(measure, LEFT), FadeIn(readout), run_time=1.0)
        self.swap_caption("A voltage gradient turns the touch point into coordinates.")
        self.wait(2.2)

        self.clear_cap()
        self.play(*[FadeOut(m) for m in [title1, glass, bot_layer, top_layer, stylus, contact,
                                         lab_top, lab_gap, lab_bot, lab_gls, v0, v5, measure, readout]],
                  run_time=0.8)

        # ================= ACT 2 — CAPACITIVE =================
        title2 = Text("2. Capacitive - charge", font_size=34, color=PURPLE).to_edge(UP, buff=0.3)
        self.play(FadeIn(title2), run_time=0.8)

        glass2 = Rectangle(width=9, height=0.55, stroke_color=GRAY, stroke_width=2,
                           fill_color=GRAY, fill_opacity=0.12).move_to([0, -1.3, 0])
        coat = Rectangle(width=9, height=0.14, stroke_color=TEAL, stroke_width=2,
                         fill_color=TEAL, fill_opacity=0.4).move_to([0, -0.95, 0])
        charges = VGroup(*[Text("+", font_size=26, color=TEAL).move_to([x, -0.6, 0])
                           for x in [round(-4.2 + 0.7 * i, 2) for i in range(13)]])
        sen_l = Square(side_length=0.45, stroke_color=PURPLE, stroke_width=3,
                       fill_color=PURPLE, fill_opacity=0.25).move_to([-4.95, -0.95, 0])
        sen_r = sen_l.copy().move_to([4.95, -0.95, 0])
        lab_sl = Text("sensor", font_size=20, color=PURPLE).next_to(sen_l, DOWN, buff=0.15)
        lab_sr = Text("sensor", font_size=20, color=PURPLE).next_to(sen_r, DOWN, buff=0.15)

        self.play(FadeIn(glass2), FadeIn(coat), FadeIn(charges),
                  FadeIn(sen_l), FadeIn(sen_r), FadeIn(lab_sl), FadeIn(lab_sr), run_time=1.4)
        self.swap_caption("One glass layer holds a faint, even charge.")
        self.wait(1.4)

        finger = RoundedRectangle(corner_radius=0.3, width=0.75, height=1.6,
                                  stroke_color=BLUE_, stroke_width=3,
                                  fill_color=BLUE_, fill_opacity=0.25).move_to([1.4, 2.2, 0])
        self.play(finger.animate.move_to([1.4, 0.35, 0]), run_time=0.9)

        stolen = VGroup(charges[7], charges[8], charges[9])  # x = 0.7, 1.4, 2.1
        self.play(*[q.animate.move_to([1.4, -0.42 + 0.001, 0]).set_opacity(0) for q in stolen],
                  run_time=1.1)
        self.swap_caption("A fingertip is a conductor - it quietly steals charge.", PURPLE)

        bar_l = Rectangle(width=0.3, height=0.45, stroke_color=PURPLE, stroke_width=2,
                          fill_color=PURPLE, fill_opacity=0.5).move_to([-4.95, -0.2, 0])
        bar_r = Rectangle(width=0.3, height=0.95, stroke_color=PURPLE, stroke_width=2,
                          fill_color=PURPLE, fill_opacity=0.5).move_to([4.95, 0.05, 0])
        note = Text("the nearer corner feels the bigger drain", font_size=24, color=PURPLE)
        note.move_to([0, 1.6, 0])
        self.play(GrowFromEdge(bar_l, DOWN), GrowFromEdge(bar_r, DOWN), FadeIn(note), run_time=0.9)
        self.swap_caption("Compare the drains and the ratio gives the position.")
        self.wait(1.8)

        finger2 = finger.copy().move_to([-2.4, 2.2, 0])
        stolen2 = VGroup(charges[2], charges[3])  # x = -2.8, -2.1
        self.play(finger2.animate.move_to([-2.4, 0.35, 0]), run_time=0.7)
        self.play(*[q.animate.move_to([-2.4, -0.42, 0]).set_opacity(0) for q in stolen2],
                  bar_l.animate.stretch_to_fit_height(0.8).move_to([-4.95, -0.03, 0]),
                  run_time=0.9)
        self.swap_caption("Several thefts tracked at once - that is multi-touch.", GREEN)
        self.wait(1.8)
        self.swap_caption("But a wool glove steals nothing - the screen never knows you came.", RED_)
        self.wait(2.0)

        self.clear_cap()
        self.play(*[FadeOut(m) for m in [title2, glass2, coat, charges, sen_l, sen_r,
                                         lab_sl, lab_sr, finger, finger2, bar_l, bar_r, note]],
                  run_time=0.8)

        # ================= ACT 3 — INFRA-RED =================
        title3 = Text("3. Infra-red - shadow", font_size=34, color=AMBER).to_edge(UP, buff=0.3)
        self.play(FadeIn(title3), run_time=0.8)

        screen = Rectangle(width=7.2, height=4.0, stroke_color=GRAY, stroke_width=2.5,
                           fill_color=GRAY, fill_opacity=0.06).move_to([0, -0.35, 0])
        row_ys = [round(-2.05 + 0.85 * i, 2) for i in range(5)]
        col_xs = [round(-3.15 + 0.9 * i, 2) for i in range(8)]
        leds_l = VGroup(*[Dot([-3.85, y, 0], radius=0.09, color=AMBER) for y in row_ys])
        sens_r = VGroup(*[Square(side_length=0.16, stroke_color=GRAY, stroke_width=2)
                          .move_to([3.85, y, 0]) for y in row_ys])
        leds_t = VGroup(*[Dot([x, 1.9, 0], radius=0.09, color=AMBER) for x in col_xs])
        sens_b = VGroup(*[Square(side_length=0.16, stroke_color=GRAY, stroke_width=2)
                          .move_to([x, -2.6, 0]) for x in col_xs])
        h_beams = VGroup(*[Line([-3.7, y, 0], [3.7, y, 0], color=AMBER,
                                stroke_width=2, stroke_opacity=0.3) for y in row_ys])
        v_beams = VGroup(*[Line([x, 1.75, 0], [x, -2.45, 0], color=AMBER,
                                stroke_width=2, stroke_opacity=0.3) for x in col_xs])

        self.play(FadeIn(screen), FadeIn(leds_l), FadeIn(sens_r), FadeIn(leds_t), FadeIn(sens_b),
                  run_time=1.0)
        self.play(Create(h_beams), Create(v_beams), run_time=1.2)
        self.swap_caption("An invisible lattice of light floats just above the glass.")
        self.wait(1.4)

        fx, fy = col_xs[5], row_ys[3]  # x = 1.35, y = 0.5
        finger3 = Dot([fx, fy, 0], radius=0.3, color=BLUE_)
        self.play(GrowFromCenter(finger3), run_time=0.6)

        broken_h = DashedLine([-3.7, fy, 0], [3.7, fy, 0], color=RED_, stroke_width=4)
        broken_v = DashedLine([fx, 1.75, 0], [fx, -2.45, 0], color=RED_, stroke_width=4)
        self.play(Transform(h_beams[3], broken_h), Transform(v_beams[5], broken_v),
                  sens_r[3].animate.set_stroke(RED_).set_fill(RED_, opacity=0.5),
                  sens_b[5].animate.set_stroke(RED_).set_fill(RED_, opacity=0.5),
                  run_time=0.9)
        self.swap_caption("A touch casts a shadow - one row and one column go dark.", RED_)

        lab_row = Text("y found", font_size=24, color=RED_).move_to([5.1, fy, 0])
        lab_col = Text("x found", font_size=24, color=RED_).move_to([fx, -3.05, 0])
        self.play(FadeIn(lab_row), FadeIn(lab_col), run_time=0.7)
        self.wait(1.2)
        self.swap_caption("Broken row + broken column = (x, y). Anything opaque works.", GREEN)
        self.wait(2.2)

        self.clear_cap()
        self.play(*[FadeOut(m) for m in [title3, screen, leds_l, sens_r, leds_t, sens_b,
                                         h_beams, v_beams, finger3, lab_row, lab_col]],
                  run_time=0.8)

        # ================= CLOSING =================
        l1 = Text("resistive - it feels pressure", font_size=32, color=BLUE_).move_to([0, 1.0, 0])
        l2 = Text("capacitive - it misses charge", font_size=32, color=PURPLE).move_to([0, 0.2, 0])
        l3 = Text("infra-red - it sees shadow", font_size=32, color=AMBER).move_to([0, -0.6, 0])
        self.play(LaggedStart(FadeIn(l1), FadeIn(l2), FadeIn(l3), lag_ratio=0.35), run_time=1.6)
        self.swap_caption("Three physics, one job: find the finger.")
        self.wait(2.5)

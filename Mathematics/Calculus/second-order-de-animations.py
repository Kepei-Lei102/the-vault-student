"""Manim scenes for [[Second-Order Differential Equations]].

Two scenes:
  DampingDial       -- one equation, one friction dial: roots collide on the
                       real axis and split into the complex plane while the
                       solution curve morphs (overdamped -> critical -> ringing).
  EulerSubstitution -- the x = e^t reduction of x^2 y'' - x y' + y = 0,
                       term by term, at watchable speed.

Render (on Kepei's Mac, from this directory):
  manim -qk second-order-de-animations.py DampingDial
  manim -qk second-order-de-animations.py EulerSubstitution
  cp media/videos/second-order-de-animations/2160p60/DampingDial.mp4 second-order-de-damping-dial.mp4
  cp media/videos/second-order-de-animations/2160p60/EulerSubstitution.mp4 second-order-de-euler-substitution.mp4
  rm -rf media
"""

from manim import *
import numpy as np

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG       = "#1e1e1e"
TXT      = "#cccccc"
TXT_DIM  = "#888888"
BLUE     = "#2563eb"
RED      = "#dc2626"
GREEN    = "#059669"
AMBER    = "#f59e0b"
GREY     = "#888888"
PURPLE   = "#7c3aed"
MAGENTA  = "#cc0066"

config.background_color = BG


def body(text, color=TXT, size=28):
    return Text(text, color=color, font_size=size)


def small(text, color=TXT_DIM, size=22):
    return Text(text, color=color, font_size=size)


def solution(t, c):
    """x'' + c x' + 4x = 0 with x(0)=1, x'(0)=0."""
    d = c * c - 16.0
    if d > 1e-6:      # overdamped: two real roots
        r = np.sqrt(d)
        l1, l2 = (-c + r) / 2.0, (-c - r) / 2.0
        A, B = l2 / (l2 - l1), -l1 / (l2 - l1)
        return A * np.exp(l1 * t) + B * np.exp(l2 * t)
    if d < -1e-6:     # underdamped: conjugate pair
        w = np.sqrt(-d) / 2.0
        s = c / 2.0
        return np.exp(-s * t) * (np.cos(w * t) + (s / w) * np.sin(w * t))
    return (1.0 + 2.0 * t) * np.exp(-2.0 * t)   # critical


def roots(c):
    d = c * c - 16.0
    if d >= 0.0:
        r = np.sqrt(d)
        return complex((-c + r) / 2.0, 0.0), complex((-c - r) / 2.0, 0.0)
    w = np.sqrt(-d) / 2.0
    return complex(-c / 2.0, w), complex(-c / 2.0, -w)


class DampingDial(Scene):
    def construct(self):
        # --- header: the equation with a live c ---------------------------
        eq = MathTex(r"x'' \;+\; c\,x' \;+\; 4x \;=\; 0",
                     font_size=44, color=TXT)
        c_val = ValueTracker(5.0)
        c_label = MathTex(r"c \,=\,", font_size=40, color=AMBER)
        c_num = DecimalNumber(5.0, num_decimal_places=2,
                              font_size=40, color=AMBER)
        c_num.add_updater(lambda m: m.set_value(c_val.get_value()))
        c_group = VGroup(c_label, c_num).arrange(RIGHT, buff=0.15)
        header = VGroup(eq, c_group).arrange(RIGHT, buff=0.9)
        header.to_edge(UP, buff=0.4)

        # --- left: the solution curve ------------------------------------
        axes = Axes(
            x_range=[0, 6, 1], y_range=[-0.8, 1.2, 0.5],
            x_length=7.2, y_length=4.6,
            axis_config=dict(color=GREY, stroke_width=2,
                             include_ticks=True, font_size=20),
        ).shift(LEFT * 2.9 + DOWN * 0.55)
        x_lab = MathTex("t", font_size=28, color=TXT_DIM)
        x_lab.next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_lab = MathTex("x", font_size=28, color=TXT_DIM)
        y_lab.next_to(axes.y_axis.get_end(), LEFT, buff=0.2)

        curve = always_redraw(lambda: axes.plot(
            lambda t: solution(t, c_val.get_value()),
            x_range=[0, 6, 0.01], color=MAGENTA, stroke_width=5))

        # --- right: the roots in the complex plane -----------------------
        plane = Axes(
            x_range=[-4.5, 0.6, 1], y_range=[-2.2, 2.2, 1],
            x_length=4.4, y_length=3.9,
            axis_config=dict(color=GREY, stroke_width=2,
                             include_ticks=True, font_size=18),
        ).shift(RIGHT * 4.2 + DOWN * 0.55)
        re_lab = MathTex(r"\mathrm{Re}\,\lambda", font_size=24, color=TXT_DIM)
        re_lab.next_to(plane.x_axis.get_end(), UP, buff=0.15)
        im_lab = MathTex(r"\mathrm{Im}\,\lambda", font_size=24, color=TXT_DIM)
        im_lab.next_to(plane.y_axis.get_end(), RIGHT, buff=0.15)

        def root_dot(which):
            def build():
                z = roots(c_val.get_value())[which]
                return Dot(plane.coords_to_point(z.real, z.imag),
                           color=AMBER, radius=0.09)
            return always_redraw(build)

        dot1, dot2 = root_dot(0), root_dot(1)
        plane_title = Tex("the two roots of the auxiliary equation",
                          font_size=30, color=TXT_DIM)
        plane_title.next_to(plane, UP, buff=0.25)

        # --- phase caption ------------------------------------------------
        caption = body("overdamped — two real roots, sluggish return",
                       color=TXT, size=26).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(header), run_time=0.8)
        self.play(FadeIn(axes), FadeIn(x_lab), FadeIn(y_lab),
                  FadeIn(plane), FadeIn(re_lab), FadeIn(im_lab),
                  FadeIn(plane_title), run_time=0.9)
        self.play(FadeIn(curve), FadeIn(dot1), FadeIn(dot2),
                  FadeIn(caption), run_time=0.8)
        self.wait(1.6)

        # dial down to critical
        self.play(c_val.animate.set_value(4.0), run_time=5.0,
                  rate_func=rate_functions.ease_in_out_sine)
        crit_caption = body("c = 4: the roots COLLIDE — critical damping, "
                            "fastest return, no overshoot", color=AMBER, size=26)
        crit_caption.to_edge(DOWN, buff=0.35)
        ghost = axes.plot(lambda t: solution(t, 4.0),
                          x_range=[0, 6, 0.01], color=GREY,
                          stroke_width=2, stroke_opacity=0.5)
        self.play(FadeOut(caption), FadeIn(crit_caption), FadeIn(ghost),
                  run_time=0.7)
        self.wait(2.2)

        # dial down into ringing
        under_caption = body("underdamped — the pair splits into the complex "
                             "plane: overshoot and ring", color=TXT, size=26)
        under_caption.to_edge(DOWN, buff=0.35)
        self.play(FadeOut(crit_caption), FadeIn(under_caption), run_time=0.6)
        self.play(c_val.animate.set_value(1.0), run_time=6.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(1.2)

        closing = body("real part = envelope · imaginary part = frequency",
                       color=AMBER, size=28).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(under_caption), FadeIn(closing), run_time=0.7)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in
                    [header, axes, x_lab, y_lab, curve, plane, re_lab, im_lab,
                     plane_title, dot1, dot2, ghost, closing]], run_time=0.8)


class EulerSubstitution(Scene):
    def construct(self):
        self.beat_problem()
        self.beat_first_derivative()
        self.beat_second_derivative()
        self.beat_substitute()
        self.beat_solve()

    # -- beat 1: the problem and the substitution -------------------------
    def beat_problem(self):
        title = MathTex(r"\text{A given substitution: }\; x = e^t",
                        font_size=44, color=TXT)
        title.to_edge(UP, buff=0.4)
        eq = MathTex(r"x^2\frac{d^2y}{dx^2}", r"\;-\;", r"x\frac{dy}{dx}",
                     r"\;+\;", r"y", r"\;=\;0", font_size=48, color=TXT)
        eq.shift(UP * 0.9)
        warn = small("the coefficients are not constant — "
                     "the exponential guess fails", size=24)
        warn.next_to(eq, DOWN, buff=0.5)
        sub = MathTex(r"x = e^t \iff t = \ln x,\qquad \frac{dt}{dx} = \frac{1}{x}",
                      font_size=40, color=BLUE)
        sub.next_to(warn, DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(eq), run_time=0.9)
        self.play(eq[0].animate.set_color(RED),
                  eq[2].animate.set_color(RED), run_time=0.8)
        self.play(FadeIn(warn), run_time=0.7)
        self.wait(1.6)
        self.play(FadeIn(sub), run_time=0.9)
        self.wait(1.8)
        self.eq_carry = eq
        self.play(FadeOut(title), FadeOut(warn),
                  eq.animate.scale(0.72).to_edge(UP, buff=0.35),
                  sub.animate.scale(0.8).to_edge(UP, buff=1.35),
                  run_time=0.9)
        self.sub_carry = sub

    # -- beat 2: convert dy/dx --------------------------------------------
    def beat_first_derivative(self):
        step = body("First derivative — chain rule:", size=26, color=TXT)
        step.shift(UP * 0.9 + LEFT * 3.4)
        line1 = MathTex(r"\frac{dy}{dx}", r"=",
                        r"\frac{dy}{dt}\cdot\frac{dt}{dx}", r"=",
                        r"\frac{1}{x}\,\frac{dy}{dt}",
                        font_size=42, color=TXT)
        line1.next_to(step, DOWN, buff=0.5).shift(RIGHT * 1.2)
        box1 = MathTex(r"x\frac{dy}{dx} = \frac{dy}{dt}",
                       font_size=44, color=AMBER)
        box1.next_to(line1, DOWN, buff=0.6)
        rect1 = SurroundingRectangle(box1, color=AMBER, buff=0.18)

        self.play(FadeIn(step), run_time=0.6)
        self.play(FadeIn(line1[0:3]), run_time=0.9)
        self.wait(1.0)
        self.play(FadeIn(line1[3:]), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(box1), Create(rect1), run_time=0.9)
        self.wait(1.6)
        self.first_box = VGroup(box1, rect1)
        self.play(FadeOut(step), FadeOut(line1),
                  self.first_box.animate.scale(0.75)
                      .to_corner(UL, buff=0.35).shift(DOWN * 1.3),
                  run_time=0.9)

    # -- beat 3: convert the second derivative ----------------------------
    def beat_second_derivative(self):
        step = body("Second derivative — product rule, then chain rule again:",
                    size=26, color=TXT)
        step.shift(UP * 1.15 + LEFT * 1.6)
        line1 = MathTex(
            r"\frac{d^2y}{dx^2}",
            r"= \frac{d}{dx}\!\left(\frac{1}{x}\,\frac{dy}{dt}\right)",
            font_size=40, color=TXT)
        line1.next_to(step, DOWN, buff=0.45)
        line2 = MathTex(
            r"= \;\underbrace{-\frac{1}{x^2}\,\frac{dy}{dt}}_{\text{product rule}}"
            r"\;+\;\frac{1}{x}\,"
            r"\underbrace{\frac{d^2y}{dt^2}\cdot\frac{1}{x}}_{\text{chain rule}}",
            font_size=40, color=TXT)
        line2.next_to(line1, DOWN, buff=0.45)
        box2 = MathTex(r"x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} - \frac{dy}{dt}",
                       font_size=44, color=AMBER)
        box2.next_to(line2, DOWN, buff=0.55)
        rect2 = SurroundingRectangle(box2, color=AMBER, buff=0.18)

        self.play(FadeIn(step), run_time=0.6)
        self.play(FadeIn(line1), run_time=0.9)
        self.wait(1.4)
        self.play(FadeIn(line2), run_time=1.1)
        self.wait(2.2)
        self.play(FadeIn(box2), Create(rect2), run_time=0.9)
        self.wait(1.8)
        second_box = VGroup(box2, rect2)
        self.play(FadeOut(step), FadeOut(line1), FadeOut(line2),
                  second_box.animate.scale(0.75)
                      .next_to(self.first_box, DOWN, buff=0.3)
                      .to_edge(LEFT, buff=0.35),
                  run_time=0.9)
        self.second_box = second_box

    # -- beat 4: substitute into the equation ------------------------------
    def beat_substitute(self):
        step = body("Substitute both boxes into the equation:",
                    size=26, color=TXT)
        step.shift(UP * 0.75 + RIGHT * 1.2)
        line1 = MathTex(
            r"\left(\frac{d^2y}{dt^2} - \frac{dy}{dt}\right)",
            r"\;-\;\frac{dy}{dt}\;+\;y\;=\;0",
            font_size=42, color=TXT)
        line1.next_to(step, DOWN, buff=0.5)
        line2 = MathTex(
            r"\frac{d^2y}{dt^2} \;-\; 2\frac{dy}{dt} \;+\; y \;=\; 0",
            font_size=46, color=GREEN)
        line2.next_to(line1, DOWN, buff=0.55)
        note = small("constant coefficients — the machine applies again",
                     size=24, color=GREEN)
        note.next_to(line2, DOWN, buff=0.4)

        self.play(FadeIn(step), run_time=0.6)
        self.play(Indicate(self.second_box, color=AMBER, scale_factor=1.06),
                  run_time=0.8)
        self.play(FadeIn(line1[0]), run_time=0.9)
        self.play(Indicate(self.first_box, color=AMBER, scale_factor=1.06),
                  run_time=0.8)
        self.play(FadeIn(line1[1]), run_time=0.9)
        self.wait(1.6)
        self.play(FadeIn(line2), run_time=1.0)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(step), FadeOut(line1), FadeOut(note),
                  FadeOut(self.first_box), FadeOut(self.second_box),
                  FadeOut(self.eq_carry), FadeOut(self.sub_carry),
                  line2.animate.to_edge(UP, buff=0.6),
                  run_time=0.9)
        self.new_eq = line2

    # -- beat 5: solve and translate back ----------------------------------
    def beat_solve(self):
        aux = MathTex(r"\lambda^2 - 2\lambda + 1 = (\lambda - 1)^2 = 0"
                      r"\qquad\Longrightarrow\qquad \lambda = 1 \text{ (twice)}",
                      font_size=40, color=TXT)
        aux.shift(UP * 0.9)
        sol_t = MathTex(r"y = (A + Bt)\,e^{t}", font_size=44, color=TXT)
        sol_t.next_to(aux, DOWN, buff=0.6)
        back = MathTex(r"e^t = x,\quad t = \ln x", font_size=36, color=BLUE)
        back.next_to(sol_t, DOWN, buff=0.55)
        final = MathTex(r"y = (A + B\ln x)\,x", font_size=52, color=AMBER)
        final.next_to(back, DOWN, buff=0.6)
        rect = SurroundingRectangle(final, color=AMBER, buff=0.22)

        self.play(FadeIn(aux), run_time=0.9)
        self.wait(1.6)
        self.play(FadeIn(sol_t), run_time=0.9)
        self.wait(1.4)
        self.play(FadeIn(back), run_time=0.8)
        self.wait(1.0)
        self.play(FadeIn(final), Create(rect), run_time=1.0)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in
                    [self.new_eq, aux, sol_t, back, final, rect]],
                  run_time=0.9)

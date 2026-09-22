"""Manim companion for General Relativity.md.

    manim -qk general-relativity-manim.py Equivalence      (4K; copy the MP4 to general-relativity-equivalence.mp4)

Part 1: a light pulse crosses an accelerating lift. Seen from outside it goes straight; seen from inside it bends down,
and a lift standing on a planet shows the same bend. Part 2: a wide lift in free fall, where two balls drift together,
because each falls toward the planet's centre. The first is the equivalence principle; the second is why it is local.
"""
from manim import *

BLUE_, RED_, AMBER_, GREEN_, PURPLE_, TEAL_, GREY_ = "#60a5fa", "#f87171", "#fbbf24", "#34d399", "#c4b5fd", "#67e8f9", "#9ca3af"


class Equivalence(Scene):
    def construct(self):
        self.camera.background_color = "#0b0f19"
        title = Text("Acceleration and gravity", font_size=40, color=WHITE).to_edge(UP, buff=0.35)
        self.play(FadeIn(title)); self.wait(0.3)

        # ── Part 1a: outside view, lift accelerating up, pulse straight ────────────────────────────
        stars = VGroup(*[Dot(point=[np.random.uniform(-6.5, 6.5), np.random.uniform(-3.4, 2.6), 0], radius=0.02, color=GREY_) for _ in range(70)])
        self.play(FadeIn(stars, run_time=0.6))
        W, H = 3.2, 3.6
        cab = Rectangle(width=W, height=H, color=BLUE_, stroke_width=4).move_to([0, -0.8, 0])
        a_arrow = Arrow(cab.get_bottom() + RIGHT*2.2, cab.get_top() + RIGHT*2.2, color=RED_, stroke_width=6)
        a_lab = MathTex("a", color=RED_, font_size=48).next_to(a_arrow, RIGHT, buff=0.15)
        caption = Text("Seen from outside: the lift accelerates up; the pulse goes straight.", font_size=26, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(Create(cab), GrowArrow(a_arrow), FadeIn(a_lab), FadeIn(caption))
        y_in = cab.get_top()[1] - 0.6
        pulse = Dot(radius=0.09, color=AMBER_).move_to([cab.get_left()[0], y_in, 0])
        trail = TracedPath(pulse.get_center, stroke_color=AMBER_, stroke_width=4)
        entry_mark = Dot(radius=0.08, color=PURPLE_).move_to([cab.get_left()[0], y_in, 0])
        entry_mark.add_updater(lambda m: m.move_to([cab.get_left()[0], m.get_center()[1], 0]))
        entry_off = y_in - cab.get_center()[1]
        entry_mark.add_updater(lambda m: m.move_to([cab.get_left()[0], cab.get_center()[1] + entry_off, 0]))
        self.add(trail, entry_mark, pulse)
        T = 2.2
        marks = VGroup()
        def cab_updater(m, dt, state={"t": 0.0}):
            state["t"] += dt; t = state["t"]
            m.move_to([0, -0.8 + 0.5 * 0.55 * t * t, 0])
        cab.add_updater(cab_updater)
        a_arrow.add_updater(lambda m: m.put_start_and_end_on(cab.get_bottom() + RIGHT*2.2, cab.get_top() + RIGHT*2.2))
        a_lab.add_updater(lambda m: m.next_to(a_arrow, RIGHT, buff=0.15))
        self.play(pulse.animate.move_to([cab.get_left()[0] + W, y_in, 0]), run_time=T, rate_func=linear)
        cab.remove_updater(cab_updater); a_arrow.clear_updaters(); a_lab.clear_updaters()
        exit_mark = Dot(radius=0.08, color=PURPLE_).move_to([cab.get_right()[0], y_in, 0])
        exit_lab = Text("hits the far wall lower", font_size=22, color=PURPLE_).move_to(exit_mark.get_center() + LEFT*1.55 + DOWN*0.35)
        self.play(FadeIn(exit_mark), FadeIn(exit_lab)); self.wait(0.8)

        # ── Part 1b: inside view, lift fixed, same two wall points, the bend ────────────────────────
        self.play(FadeOut(trail), FadeOut(pulse), FadeOut(exit_lab), FadeOut(caption))
        d_y = cab.get_center()[1] - (-0.8)
        entry_mark.clear_updaters()
        self.play(cab.animate.move_to([0, -0.8, 0]), exit_mark.animate.shift(DOWN*d_y), entry_mark.animate.shift(DOWN*d_y), a_arrow.animate.put_start_and_end_on([2.2, -0.8-H/2, 0], [2.2, -0.8+H/2, 0]), a_lab.animate.next_to([2.35, -0.8, 0], RIGHT, buff=0.15), run_time=0.8)
        caption2 = Text("Seen from inside: the pulse bends down. Only a curve fits the two wall points.", font_size=26, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(caption2))
        x0, x1 = cab.get_left()[0], cab.get_right()[0]; y_top = cab.get_top()[1] - 0.6; drop = y_top - exit_mark.get_center()[1]
        curve = ParametricFunction(lambda s: np.array([x0 + s*W, y_top - drop*s*s, 0]), t_range=[0, 1], color=AMBER_, stroke_width=5)
        pulse2 = Dot(radius=0.09, color=AMBER_).move_to([x0, y_top, 0])
        self.add(pulse2)
        self.play(Create(curve), MoveAlongPath(pulse2, curve), run_time=T, rate_func=linear); self.wait(0.6)

        # ── Part 1c: swap the stars for a planet, a for g, keep the curve ───────────────────────────
        ground = Rectangle(width=14, height=0.55, fill_color=GREEN_, fill_opacity=0.25, stroke_color=GREEN_).move_to([0, -0.8 - H/2 - 0.275, 0])
        g_lab = MathTex("g", color=RED_, font_size=48).move_to(a_lab)
        caption3 = Text("Now the same lift stands on a planet. Same curve. You cannot tell which lift you are in.", font_size=26, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(stars), FadeIn(ground), Transform(a_lab, g_lab), a_arrow.animate.put_start_and_end_on([2.2, -0.8+H/2, 0], [2.2, -0.8-H/2, 0]),
                  FadeOut(caption2), FadeIn(caption3), run_time=1.2)
        pulse3 = Dot(radius=0.09, color=AMBER_).move_to([x0, y_top, 0]); self.add(pulse3)
        self.play(MoveAlongPath(pulse3, curve), run_time=T, rate_func=linear); self.wait(1.2)

        # ── Part 2: a wide lift in free fall, two balls converge ─────────────────────────────────────
        self.play(*[FadeOut(m) for m in [cab, curve, pulse2, pulse3, exit_mark, entry_mark, a_arrow, a_lab, ground, caption3]], run_time=0.8)
        title2 = Text("Why it only works in a small lift", font_size=40, color=WHITE).to_edge(UP, buff=0.35)
        self.play(Transform(title, title2))
        earth = Circle(radius=6.0, color=TEAL_, fill_opacity=0.18, stroke_width=3).move_to([0, -9.3, 0])
        centre = earth.get_center()
        self.play(FadeIn(earth))
        wide = Rectangle(width=8.5, height=2.0, color=BLUE_, stroke_width=4).move_to([0, 0.9, 0])
        b1 = Dot(radius=0.13, color=RED_).move_to([-3.4, 1.3, 0]); b2 = Dot(radius=0.13, color=RED_).move_to([3.4, 1.3, 0])
        l1 = DashedLine(b1.get_center(), centre, color=RED_, stroke_width=2); l2 = DashedLine(b2.get_center(), centre, color=RED_, stroke_width=2)
        gap = DoubleArrow(b1.get_center() + RIGHT*0.2, b2.get_center() + LEFT*0.2, color=PURPLE_, stroke_width=4, buff=0)
        gap_lab = Text("their separation shrinks", font_size=24, color=PURPLE_).next_to(gap, DOWN, buff=0.22)
        caption4 = Text("In free fall the lift feels no gravity, but each ball falls toward the planet's centre, so they drift together.", font_size=24, color=GREY_).next_to(title, DOWN, buff=0.3)
        self.play(Create(wide), FadeIn(b1), FadeIn(b2), Create(l1), Create(l2), FadeIn(gap), FadeIn(gap_lab), FadeIn(caption4))
        gap.add_updater(lambda m: m.put_start_and_end_on(b1.get_center() + RIGHT*0.2, b2.get_center() + LEFT*0.2))
        gap_lab.add_updater(lambda m: m.next_to(gap, DOWN, buff=0.22))
        fall = 3.2
        def toward(p, f):
            v = centre - p; return p + v / np.linalg.norm(v) * f
        self.play(wide.animate.shift(DOWN*fall), b1.animate.move_to(toward(b1.get_center(), fall)), b2.animate.move_to(toward(b2.get_center(), fall)),
                  run_time=3.0, rate_func=smooth)
        gap.clear_updaters(); gap_lab.clear_updaters()
        caption5 = Text("Tides. That convergence is the part no accelerating lift can fake, and it is what 'curved space-time' means.", font_size=22, color=GREY_).next_to(title, DOWN, buff=0.3)
        self.play(FadeOut(caption4), FadeIn(caption5)); self.wait(2.0)

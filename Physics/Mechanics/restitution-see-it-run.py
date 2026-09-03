# Animation stack: Manim (the bay's standard). Built off the review comment
# that the walkthrough clip showed configurations, not collisions - this one
# shows the PROCESS: balls genuinely move, hit, and rebound, and every
# decomposition appears frozen at the instant of contact so the angles refer
# to something the eye just watched happen.
# Render:  manim -qk restitution-see-it-run.py RestitutionSeeItRun
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""Newton's law of restitution - collisions in motion, three chapters.

Ch 1  the straight bounce: drop, squash, rebound - heights fall as e^2
Ch 2  the cushion: time stops at contact, the two components get their fates
Ch 3  two spheres: the line of centres appears AT the collision, B leaves along it
"""
from manim import *
import numpy as np

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
TEAL = ManimColor("#0891b2")

E = 0.7          # chapter 1 ball
E2 = 0.5         # chapters 2-3


class RestitutionSeeItRun(Scene):
    def construct(self):
        self.ch1_straight_bounce()
        self.ch2_cushion()
        self.ch3_two_spheres()

    # ------------------------------------------------------------------ Ch 1
    def ch1_straight_bounce(self):
        title = Text("a collision is a process: squash, then spring back short",
                     font_size=30, color=GREY).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)

        floor_y = -2.9
        floor = Line(LEFT * 6.8, RIGHT * 6.8, color=GREY, stroke_width=3)
        floor.shift(UP * floor_y)
        self.play(Create(floor), run_time=0.5)

        h0 = 4.6                       # scene units above the floor
        x0 = -3.2
        r = 0.32
        ball = Circle(radius=r, color=BLUE, fill_opacity=0.35,
                      stroke_width=3).move_to([x0, floor_y + h0 + r, 0])
        self.play(FadeIn(ball), run_time=0.5)

        # height markers as we go: h0, e^2 h0, e^4 h0
        def hmark(x, h, label):
            tick = DashedLine([x - 0.55, floor_y + h + 2 * r, 0],
                              [x + 0.55, floor_y + h + 2 * r, 0],
                              color=AMBER, stroke_width=2)
            lab = Text(label, font_size=22, color=AMBER).next_to(tick, UP, buff=0.08)
            return VGroup(tick, lab)

        m0 = hmark(x0, h0, "h0")
        self.play(FadeIn(m0), run_time=0.5)

        note = Text("watch the floor moment: the ball squashes, then leaves SLOWER",
                    font_size=25, color=GREY).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(note), run_time=0.6)

        def fall_and_squash(x, h, rt_fall):
            self.play(ball.animate.move_to([x, floor_y + r, 0]),
                      run_time=rt_fall, rate_func=rate_functions.ease_in_quad)
            # compression: the loaded-spring instant
            self.play(ball.animate.stretch(0.55, 1).move_to([x, floor_y + 0.55 * r, 0]),
                      run_time=0.22)
            self.play(ball.animate.stretch(1 / 0.55, 1).move_to([x, floor_y + r, 0]),
                      run_time=0.22)

        def rise(x, h, rt):
            self.play(ball.animate.move_to([x, floor_y + h + r, 0]),
                      run_time=rt, rate_func=rate_functions.ease_out_quad)

        # bounce 1: annotate speeds at the floor
        fall_and_squash(x0, h0, 1.5)
        u_arrow = Arrow([x0 - 1.15, floor_y + 1.7, 0], [x0 - 1.15, floor_y + 0.35, 0],
                        color=BLUE, stroke_width=5, buff=0)
        u_lab = MathTex(r"u = \sqrt{2gh_0}", font_size=34, color=BLUE)
        u_lab.next_to(u_arrow, LEFT, buff=0.15)
        v_arrow = Arrow([x0 + 1.15, floor_y + 0.35, 0], [x0 + 1.15, floor_y + 1.35, 0],
                        color=GREEN, stroke_width=5, buff=0)
        v_lab = MathTex(r"v = e\,u", font_size=34, color=GREEN)
        v_lab.next_to(v_arrow, RIGHT, buff=0.15)
        self.play(FadeIn(u_arrow), FadeIn(u_lab), run_time=0.6)
        self.play(FadeIn(v_arrow), FadeIn(v_lab), run_time=0.6)
        self.wait(0.8)

        h1 = E ** 2 * h0
        x1 = x0 + 2.6
        m1 = hmark(x1, h1, "e2 h0")
        self.play(FadeOut(u_arrow), FadeOut(u_lab), FadeOut(v_arrow), FadeOut(v_lab),
                  run_time=0.4)
        # rise to e^2 h0 (drifting right so the ladder of heights reads left to right)
        self.play(ball.animate.move_to([x1, floor_y + h1 + r, 0]), FadeIn(m1),
                  run_time=1.1, rate_func=rate_functions.ease_out_quad)

        h2 = E ** 4 * h0
        x2 = x1 + 2.2
        fall_and_squash(x1, h1, 0.9)
        m2 = hmark(x2, h2, "e4 h0")
        self.play(ball.animate.move_to([x2, floor_y + h2 + r, 0]), FadeIn(m2),
                  run_time=0.8, rate_func=rate_functions.ease_out_quad)
        fall_and_squash(x2, h2, 0.6)
        self.play(ball.animate.move_to([x2 + 1.6, floor_y + E ** 6 * h0 + r, 0]),
                  run_time=0.6, rate_func=rate_functions.ease_out_quad)

        moral = Text("each height is e2 of the last - speeds scale by e, heights by e2",
                     font_size=25, color=AMBER).to_edge(DOWN, buff=0.25)
        self.play(ReplacementTransform(note, moral), run_time=0.7)
        self.wait(1.6)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)

    # ------------------------------------------------------------------ Ch 2
    def ch2_cushion(self):
        title = Text("the cushion: freeze at contact, give each component its fate",
                     font_size=30, color=GREY).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)

        floor_y = -2.4
        floor = Line(LEFT * 6.8, RIGHT * 6.8, color=GREY, stroke_width=3).shift(UP * floor_y)
        self.play(Create(floor), run_time=0.5)

        alpha = np.radians(45)
        speed = 3.2
        r = 0.3
        vx, vy = speed * np.cos(alpha), -speed * np.sin(alpha)
        contact = np.array([-1.2, floor_y + r, 0])
        t_pre = 1.6
        start = contact - np.array([vx, vy, 0]) * t_pre

        ball = Circle(radius=r, color=BLUE, fill_opacity=0.35,
                      stroke_width=3).move_to(start)
        trail = TracedPath(ball.get_center, stroke_color=BLUE, stroke_width=2.5,
                           stroke_opacity=0.45)
        self.add(trail)
        self.play(FadeIn(ball), run_time=0.4)
        self.play(ball.animate.move_to(contact), run_time=t_pre, rate_func=linear)

        # TIME STOPS - decompose at the instant of contact
        freeze = Text("time stopped at the instant of contact", font_size=25,
                      color=AMBER).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(freeze), run_time=0.6)
        sc = 0.55
        a_along = Arrow(contact, contact + np.array([vx * sc, 0, 0]),
                        color=AMBER, stroke_width=6, buff=0)
        a_into = Arrow(contact + np.array([0, -vy * sc, 0]), contact,
                       color=RED, stroke_width=6, buff=0)
        l_along = MathTex(r"v\cos\alpha", font_size=32, color=AMBER)
        l_along.next_to(a_along, UP, buff=0.1)
        l_into = MathTex(r"v\sin\alpha", font_size=32, color=RED)
        l_into.next_to(a_into, RIGHT, buff=0.12).shift(UP * 0.3)
        arc_in = Arc(radius=0.9, start_angle=np.pi - alpha, angle=alpha,
                     arc_center=contact, color=GREY)
        l_alpha = MathTex(r"\alpha", font_size=32, color=GREY)
        l_alpha.move_to(contact + np.array([-1.25, 0.42, 0]))
        self.play(GrowArrow(a_along), GrowArrow(a_into), FadeIn(l_along),
                  FadeIn(l_into), Create(arc_in), FadeIn(l_alpha), run_time=1.2)
        self.wait(1.2)

        verdicts = Text("smooth wall: the along-wall part feels NO force - it survives",
                        font_size=25, color=AMBER).to_edge(DOWN, buff=0.25)
        self.play(ReplacementTransform(freeze, verdicts), run_time=0.7)
        self.wait(1.0)
        verdict2 = Text("the into-wall part runs the wall rule: reversed, times e = 0.5",
                        font_size=25, color=RED).to_edge(DOWN, buff=0.25)
        # flip and shrink the normal component
        a_out = Arrow(contact, contact + np.array([0, -vy * sc * E2, 0]),
                      color=GREEN, stroke_width=6, buff=0)
        l_out = MathTex(r"e\,v\sin\alpha", font_size=32, color=GREEN)
        l_out.next_to(a_out, LEFT, buff=0.1)
        self.play(ReplacementTransform(verdicts, verdict2), run_time=0.7)
        self.play(ReplacementTransform(a_into, a_out),
                  ReplacementTransform(l_into, l_out), run_time=1.0)
        self.wait(1.0)

        # resume time: depart along the recomposed, flatter direction
        beta = np.arctan(E2 * np.tan(alpha))
        vx2, vy2 = speed * np.cos(alpha), speed * np.sin(alpha) * E2
        arc_out = Arc(radius=1.15, start_angle=0, angle=beta,
                      arc_center=contact, color=GREEN)
        l_beta = MathTex(r"\beta", font_size=32, color=GREEN)
        l_beta.move_to(contact + np.array([1.5, 0.3, 0]))
        resume = MathTex(r"\tan\beta = e\tan\alpha", font_size=40, color=GREEN)
        resume.to_edge(DOWN, buff=0.25)
        self.play(FadeOut(a_along), FadeOut(l_along), FadeOut(a_out), FadeOut(l_out),
                  Create(arc_out), FadeIn(l_beta),
                  ReplacementTransform(verdict2, resume), run_time=0.9)
        t_post = 1.7
        self.play(ball.animate.move_to(contact + np.array([vx2 * t_post, vy2 * t_post, 0])),
                  run_time=t_post, rate_func=linear)
        note = Text("it leaves FLATTER than it arrived - every cushion shot in snooker",
                    font_size=25, color=GREY).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(1.6)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)

    # ------------------------------------------------------------------ Ch 3
    def ch3_two_spheres(self):
        title = Text("two spheres: the line of centres exists only at contact",
                     font_size=30, color=GREY).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)

        r = 0.55
        # B waits; A arrives from upper-left moving right-and-down at 30 deg below horizontal
        theta = np.radians(30)
        speed = 2.6
        vA = np.array([speed * np.cos(theta), -speed * np.sin(theta), 0])
        # contact when centres are 2r apart ALONG the line of centres; choose the
        # line of centres horizontal at contact for a clean decomposition
        cB = np.array([1.1, -0.7, 0])
        cA_contact = cB - np.array([2 * r, 0, 0])
        t_pre = 1.7
        cA_start = cA_contact - vA * t_pre

        A = Circle(radius=r, color=BLUE, fill_opacity=0.25, stroke_width=3).move_to(cA_start)
        B = Circle(radius=r, color=TEAL, fill_opacity=0.25, stroke_width=3).move_to(cB)
        tA = Text("A", font_size=26, color=GREY).move_to(cA_start)
        tB = Text("B", font_size=26, color=GREY).move_to(cB)
        tA.add_updater(lambda m: m.move_to(A.get_center()))
        note = Text("B at rest. A arrives at an angle - watch the contact instant",
                    font_size=25, color=GREY).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(A), FadeIn(B), FadeIn(tA), FadeIn(tB), FadeIn(note),
                  run_time=0.8)
        trail_in = TracedPath(A.get_center, stroke_color=BLUE, stroke_width=2.5,
                              stroke_opacity=0.45)
        self.add(trail_in)
        self.play(A.animate.move_to(cA_contact), run_time=t_pre, rate_func=linear)
        tA.clear_updaters()

        # freeze: the line of centres is born NOW, from the touching geometry
        loc = DashedLine(cA_contact - np.array([2.6, 0, 0]),
                         cB + np.array([3.4, 0, 0]), color=GREY, stroke_width=2.5)
        loc_lab = Text("line of centres - the only direction the surfaces can push",
                       font_size=23, color=GREY).next_to(loc, DOWN, buff=0.75).shift(RIGHT * 1.2)
        self.play(Create(loc), FadeIn(loc_lab), run_time=1.0)
        self.wait(0.8)

        sc = 0.42
        a_loc = Arrow(cA_contact, cA_contact + np.array([vA[0] * sc, 0, 0]),
                      color=RED, stroke_width=6, buff=0)
        a_perp = Arrow(cA_contact, cA_contact + np.array([0, vA[1] * sc, 0]),
                       color=AMBER, stroke_width=6, buff=0)
        l_loc = MathTex(r"w = u\cos 30^\circ", font_size=30, color=RED)
        l_loc.next_to(a_loc, UP, buff=0.28).shift(LEFT * 1.1)
        l_perp = MathTex(r"u\sin 30^\circ", font_size=30, color=AMBER)
        l_perp.next_to(a_perp, LEFT, buff=0.15).shift(DOWN * 0.15)
        fates = Text("split A's velocity: along the line, and perpendicular to it",
                     font_size=25, color=AMBER).to_edge(DOWN, buff=0.3)
        self.play(ReplacementTransform(note, fates), GrowArrow(a_loc),
                  GrowArrow(a_perp), FadeIn(l_loc), FadeIn(l_perp), run_time=1.1)
        self.wait(1.2)

        f2 = Text("perpendicular: no force, survives.  Along: momentum + NEL, e = 0.5",
                  font_size=25, color=GREY).to_edge(DOWN, buff=0.3)
        self.play(ReplacementTransform(fates, f2), run_time=0.7)
        machine = MathTex(r"\text{equal masses: } v_A = \tfrac{1-e}{2}w = 0.25w,\quad"
                          r" v_B = \tfrac{1+e}{2}w = 0.75w",
                          font_size=32, color=GREY).to_edge(UP, buff=1.15)
        self.play(FadeIn(machine), run_time=0.9)
        self.wait(1.6)

        # resume: B departs ALONG the line of centres; A drifts off steeper and slower
        w = vA[0]
        vA_after = np.array([0.25 * w, vA[1], 0])
        vB_after = np.array([0.75 * w, 0, 0])
        t_post = 1.9
        keep = Text("B leaves ALONG the line of centres - it was only ever pushed that way",
                    font_size=25, color=GREEN).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(a_loc), FadeOut(a_perp), FadeOut(l_loc), FadeOut(l_perp),
                  ReplacementTransform(f2, keep), run_time=0.7)
        tA.add_updater(lambda m: m.move_to(A.get_center()))
        tB.add_updater(lambda m: m.move_to(B.get_center()))
        trailA = TracedPath(A.get_center, stroke_color=BLUE, stroke_width=2.5,
                            stroke_opacity=0.45)
        trailB = TracedPath(B.get_center, stroke_color=TEAL, stroke_width=2.5,
                            stroke_opacity=0.45)
        self.add(trailA, trailB)
        self.play(A.animate.shift(vA_after * t_post),
                  B.animate.shift(vB_after * t_post),
                  run_time=t_post, rate_func=linear)
        tA.clear_updaters()
        tB.clear_updaters()
        self.wait(1.8)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)

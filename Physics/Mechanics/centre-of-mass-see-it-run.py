# Animation stack: Manim (chosen for a physics deep card, matching the bay's
# existing clips - Circular Motion, Projectile Motion, Gravitational Fields).
# Render:  manim -qk centre-of-mass-see-it-run.py CentreOfMass
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""Centre of Mass - the point that makes the particle model honest.

Act 1  a tumbling hammer: the handle tip scrawls, the centre of mass draws a parabola
Act 2  the theorem that licenses it, internal forces cancelling in pairs
Act 3  the shell explodes and the centre of mass never notices
"""
from manim import *
import numpy as np

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
TEAL = ManimColor("#0891b2")

G = 9.0


class CentreOfMass(Scene):
    def construct(self):
        self.act1_hammer()
        self.act2_theorem()
        self.act3_explosion()

    # ------------------------------------------------------------------ Act 1
    def act1_hammer(self):
        title = Text("every point does something complicated", font_size=34, color=GREY)
        title.to_edge(UP, buff=0.45)
        self.play(FadeIn(title), run_time=1.0)

        ground = Line(LEFT * 7.2, RIGHT * 7.2, color=GREY, stroke_width=2)
        ground.shift(DOWN * 3.2)
        self.play(Create(ground), run_time=0.6)

        x0, y0 = -6.1, -2.4
        vy = 7.2
        vx = 12.2 / (2 * vy / G)        # span the frame in exactly one flight
        T = 2 * vy / G
        omega = 2 * TAU / T           # two full tumbles in flight
        D_TIP, D_HEAD = 1.15, 0.52    # distances from the CM

        def cm_at(t):
            return np.array([x0 + vx * t, y0 + vy * t - 0.5 * G * t * t, 0.0])

        def tip_at(t):
            u = np.array([np.cos(omega * t + 0.6), np.sin(omega * t + 0.6), 0.0])
            return cm_at(t) - D_TIP * u

        def head_at(t):
            u = np.array([np.cos(omega * t + 0.6), np.sin(omega * t + 0.6), 0.0])
            return cm_at(t) + D_HEAD * u

        tr = ValueTracker(0.0)

        handle = always_redraw(lambda: Line(
            tip_at(tr.get_value()), head_at(tr.get_value()),
            color=GREY, stroke_width=7))
        head = always_redraw(lambda: Square(side_length=0.42, color=BLUE,
                                            fill_opacity=0.35, stroke_width=3)
                             .move_to(head_at(tr.get_value()))
                             .rotate(omega * tr.get_value() + 0.6))
        tip_dot = always_redraw(lambda: Dot(tip_at(tr.get_value()), color=RED, radius=0.09))

        tip_path = TracedPath(lambda: tip_at(tr.get_value()), stroke_color=RED,
                              stroke_width=3.2, stroke_opacity=0.85)
        self.add(handle, head, tip_dot, tip_path)

        tip_lab = Text("the handle tip", font_size=27, color=RED).next_to(ground, UP, buff=0.15).to_edge(LEFT, buff=0.7)
        self.play(FadeIn(tip_lab), run_time=0.5)
        self.play(tr.animate.set_value(T), run_time=5.2, rate_func=linear)
        self.wait(0.7)

        # same throw, now watching the one point that behaves
        new_title = Text("except one", font_size=34, color=AMBER).move_to(title)
        self.play(FadeOut(tip_path), FadeOut(tip_lab), FadeOut(tip_dot),
                  ReplacementTransform(title, new_title), tr.animate.set_value(0.0),
                  run_time=1.1)

        cm_dot = always_redraw(lambda: Dot(cm_at(tr.get_value()), color=AMBER, radius=0.13))
        cm_path = TracedPath(lambda: cm_at(tr.get_value()), stroke_color=AMBER,
                             stroke_width=4.5)
        cm_lab = Text("centre of mass", font_size=27, color=AMBER)
        cm_lab.next_to(ground, UP, buff=0.15).to_edge(LEFT, buff=0.7)
        self.add(cm_dot, cm_path)
        self.play(FadeIn(cm_lab), run_time=0.5)
        self.play(tr.animate.set_value(T), run_time=5.2, rate_func=linear)

        verdict = Text("a clean parabola, every throw", font_size=30, color=AMBER)
        verdict.to_edge(RIGHT, buff=0.7).shift(UP * 1.9)
        self.play(FadeIn(verdict), run_time=0.8)
        self.wait(1.4)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)

    # ------------------------------------------------------------------ Act 2
    def act2_theorem(self):
        head = Text("why that point, and no other", font_size=34, color=GREY).to_edge(UP, buff=0.5)
        self.play(FadeIn(head), run_time=0.8)

        defn = MathTex(r"M\mathbf{R}", r"=", r"\sum m_i \mathbf{r}_i",
                       font_size=52, color=GREY).shift(UP * 1.35)
        defn[0].set_color(AMBER)
        self.play(FadeIn(defn), run_time=1.0)

        note = Text("differentiate twice", font_size=26, color=GREY).next_to(defn, DOWN, buff=0.42)
        self.play(FadeIn(note), run_time=0.7)

        step = MathTex(r"M\ddot{\mathbf{R}}", r"=", r"\sum \mathbf{F}_{\text{internal}}",
                       r"+", r"\sum \mathbf{F}_{\text{external}}",
                       font_size=46, color=GREY).next_to(note, DOWN, buff=0.5)
        step[0].set_color(AMBER)
        step[2].set_color(BLUE)
        step[4].set_color(GREEN)
        self.play(FadeIn(step), run_time=1.0)
        self.wait(0.6)

        n3 = Text("Newton's third law: internal forces come in equal and opposite pairs",
                  font_size=27, color=BLUE).next_to(step, DOWN, buff=0.5)
        self.play(FadeIn(n3), run_time=0.9)

        # the internal term is struck out and dropped
        strike = Line(step[2].get_left(), step[2].get_right(), color=RED, stroke_width=5)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeOut(strike), FadeOut(step[2]), FadeOut(step[3]), FadeOut(n3),
                  run_time=0.8)

        final = MathTex(r"M\ddot{\mathbf{R}} = \mathbf{F}_{\text{external}}",
                        font_size=62, color=AMBER)
        final.move_to(DOWN * 0.75)
        box = SurroundingRectangle(final, color=AMBER, buff=0.32, stroke_width=3)
        self.play(FadeOut(step[0]), FadeOut(step[1]), FadeOut(step[4]),
                  FadeIn(final), run_time=0.9)
        self.play(Create(box), run_time=0.8)

        moral = Text("the centre of mass moves like a single particle of mass M",
                     font_size=30, color=GREY).next_to(box, DOWN, buff=0.55)
        moral2 = Text("so \"treat the object as a particle\" is a theorem, not a fudge",
                      font_size=30, color=GREEN).next_to(moral, DOWN, buff=0.25)
        self.play(FadeIn(moral), run_time=0.9)
        self.play(FadeIn(moral2), run_time=0.9)
        self.wait(1.8)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)

    # ------------------------------------------------------------------ Act 3
    def act3_explosion(self):
        title = Text("an explosion is internal", font_size=34, color=GREY).to_edge(UP, buff=0.45)
        self.play(FadeIn(title), run_time=0.8)

        ground = Line(LEFT * 7.2, RIGHT * 7.2, color=GREY, stroke_width=2).shift(DOWN * 3.2)
        self.play(Create(ground), run_time=0.5)

        x0, y0 = -6.2, -2.85
        vy = 7.6
        vx = 12.3 / (2 * vy / G)        # span the frame
        T = 2 * vy / G
        t_e = T * 0.5                       # burst at the apex

        def cm_at(t):
            return np.array([x0 + vx * t, y0 + vy * t - 0.5 * G * t * t, 0.0])

        # fragments: masses and burst velocities whose mass-weighted sum is zero,
        # so the centre of mass cannot possibly notice the explosion
        rng = np.random.default_rng(7)
        masses = np.array([1.0, 1.4, 0.8, 1.2, 0.9])
        w = rng.normal(0, 1.0, size=(len(masses), 2)) * np.array([2.4, 1.35])
        w -= (masses[:, None] * w).sum(axis=0) / masses.sum()      # kill the net momentum
        assert np.allclose((masses[:, None] * w).sum(axis=0), 0, atol=1e-12)
        cols = [BLUE, TEAL, GREEN, RED, BLUE]

        def frag_at(i, t):
            dt = t - t_e
            v = np.array([vx + w[i, 0], vy - G * t_e + w[i, 1], 0.0])
            return cm_at(t_e) + v * dt + np.array([0, -0.5 * G * dt * dt, 0])

        tr = ValueTracker(0.0)
        shell = always_redraw(lambda: Dot(cm_at(tr.get_value()), color=AMBER, radius=0.14))
        shell_path = TracedPath(lambda: cm_at(tr.get_value()), stroke_color=AMBER,
                                stroke_width=4)
        self.add(shell, shell_path)
        self.play(tr.animate.set_value(t_e), run_time=2.4, rate_func=linear)

        # the burst
        flash = Dot(cm_at(t_e), color=AMBER, radius=0.16)
        self.play(Flash(flash, color=AMBER, line_length=0.5, num_lines=16,
                        flash_radius=0.9), run_time=0.8)

        ghost = DashedVMobject(
            ParametricFunction(lambda s: cm_at(t_e + s * (T - t_e)),
                               t_range=[0, 1], color=AMBER, stroke_width=3),
            num_dashes=26)
        self.play(Create(ghost), run_time=1.0)
        ghost_lab = Text("the original parabola, undisturbed", font_size=27, color=AMBER)
        ghost_lab.to_edge(RIGHT, buff=0.6).shift(UP * 2.15)
        self.play(FadeIn(ghost_lab), run_time=0.6)

        frags = VGroup(*[
            always_redraw(lambda i=i: Dot(frag_at(i, tr.get_value()),
                                          color=cols[i], radius=0.085))
            for i in range(len(masses))])
        frag_paths = VGroup(*[
            TracedPath(lambda i=i: frag_at(i, tr.get_value()),
                       stroke_color=cols[i], stroke_width=2.4, stroke_opacity=0.8)
            for i in range(len(masses))])
        self.add(frags, frag_paths)
        self.play(tr.animate.set_value(T), run_time=3.6, rate_func=linear)

        moral = Text("the fragments scatter; their centre of mass keeps the appointment",
                     font_size=30, color=GREEN).next_to(ground, DOWN, buff=0.28)
        self.play(FadeIn(moral), run_time=1.0)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)

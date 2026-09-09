"""Kirchhoff's two laws as motion.

Scene 1 — the junction: a stream of charge carriers arrives at a fork and splits;
the counter shows that what arrives equals what leaves, tick by tick.
Scene 2 — the potential hill: one coulomb walks the loop. The cell lifts it by E;
each resistor drops it by IR; it arrives back at the height it started at.

Render:  manim -qk kirchhoff-potential-hill.py KirchhoffLaws
Then copy media/videos/.../KirchhoffLaws.mp4 to kirchhoff-potential-hill.mp4 beside the card
and rm -rf media __pycache__.
"""
from manim import *

BLUE_, GREEN_, RED_, AMBER_, GREY_ = "#2563eb", "#059669", "#dc2626", "#f59e0b", "#888888"


class KirchhoffLaws(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        self.junction()
        self.clear()
        self.hill()

    # ------------------------------------------------------------ scene 1
    def junction(self):
        title = Text("First law — the junction keeps nothing", font_size=34, color=GREY_).to_edge(UP)
        self.play(FadeIn(title))
        J = np.array([0, 0, 0])
        left = J + 5 * LEFT
        outs = [J + 4.5 * RIGHT + 2 * UP, J + 4.5 * RIGHT, J + 4.5 * RIGHT + 2 * DOWN]
        wires = VGroup(Line(left, J, color=GREY_, stroke_width=4),
                       *[Line(J, o, color=GREY_, stroke_width=4) for o in outs])
        dot = Dot(J, color=GREY_, radius=0.08)
        self.play(Create(wires), FadeIn(dot))
        lab_in = Text("in: 0", font_size=28, color=BLUE_).next_to(left, UP)
        lab_out = Text("out: 0", font_size=28, color=GREEN_).next_to(outs[0], UP)
        self.play(FadeIn(lab_in), FadeIn(lab_out))
        # 12 carriers, split 5/3/4 in a repeating pattern
        pattern = [0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 1]
        n_in = n_out = 0
        carriers = []
        for k, branch in enumerate(pattern):
            c = Dot(left, color=BLUE_, radius=0.11)
            carriers.append(c)
            self.add(c)
            n_in += 1
            new_in = Text(f"in: {n_in}", font_size=28, color=BLUE_).next_to(left, UP)
            self.play(c.animate.move_to(J), Transform(lab_in, new_in), run_time=0.35, rate_func=linear)
            c.set_color(GREEN_)
            n_out += 1
            new_out = Text(f"out: {n_out}", font_size=28, color=GREEN_).next_to(outs[0], UP)
            self.play(c.animate.move_to(outs[branch]), Transform(lab_out, new_out), run_time=0.35, rate_func=linear)
        eq = MathTex(r"\sum I_{\text{in}} = \sum I_{\text{out}}", font_size=44, color=GREY_).to_edge(DOWN).shift(0.4 * UP)
        why = Text("because charge is conserved and a wire stores none", font_size=26, color=GREY_).next_to(eq, DOWN, buff=0.15)
        self.play(Write(eq), FadeIn(why))
        self.wait(1.5)

    # ------------------------------------------------------------ scene 2
    def hill(self):
        title = Text("Second law — one coulomb walks the loop", font_size=34, color=GREY_).to_edge(UP)
        self.play(FadeIn(title))
        # circuit on the left: cell E = 6 V, R1 = 2 Ω, R2 = 4 Ω, I = 1 A
        A = np.array([-6, -2, 0]); B = np.array([-6, 1, 0]); C = np.array([-2.5, 1, 0]); D = np.array([-2.5, -2, 0])
        loop = VGroup(Line(A, B), Line(B, C), Line(C, D), Line(D, A)).set_color(GREY_).set_stroke(width=4)
        cellp = VGroup(Line(B + 1.2 * DOWN + 0.35 * LEFT, B + 1.2 * DOWN + 0.35 * RIGHT).set_stroke(width=3),
                       Line(B + 1.45 * DOWN + 0.18 * LEFT, B + 1.45 * DOWN + 0.18 * RIGHT).set_stroke(width=7)).set_color(GREY_)
        r1 = Rectangle(width=1.0, height=0.36, color=GREY_).move_to((B + C) / 2)
        r2 = Rectangle(width=0.36, height=1.0, color=GREY_).move_to((C + D) / 2)
        labels = VGroup(Text("E = 6 V", font_size=24, color=GREEN_).next_to(cellp, RIGHT, buff=0.15),
                        Text("R₁ = 2 Ω", font_size=24, color=GREY_).next_to(r1, UP),
                        Text("R₂ = 4 Ω", font_size=24, color=GREY_).next_to(r2, RIGHT),
                        Text("I = 1 A", font_size=24, color=BLUE_).next_to(Line(D, A), DOWN))
        self.play(Create(loop), FadeIn(cellp), FadeIn(r1), FadeIn(r2), FadeIn(labels))
        # hill on the right: x = position along loop, y = potential
        ax = Axes(x_range=[0, 4, 1], y_range=[0, 7, 1], x_length=6, y_length=3.6,
                  axis_config={"color": GREY_, "include_tip": False}).shift(3.2 * RIGHT + 0.6 * DOWN)
        ylab = Text("potential / V", font_size=22, color=GREY_).next_to(ax.y_axis, UP)
        xlabs = VGroup(*[Text(t, font_size=20, color=GREY_).next_to(ax.c2p(x, 0), DOWN)
                         for t, x in [("cell", 0.5), ("R₁", 1.5), ("R₂", 2.5), ("back", 3.5)]])
        self.play(Create(ax), FadeIn(ylab), FadeIn(xlabs))
        # the walk: profile points
        prof = [(0, 0), (1, 6), (2, 4), (3, 0), (4, 0)]
        coulomb = Dot(A, color=AMBER_, radius=0.13)
        marker = Dot(ax.c2p(0, 0), color=AMBER_, radius=0.11)
        self.play(FadeIn(coulomb), FadeIn(marker))
        segs = [(A, B, prof[0], prof[1], "+6 V  (the cell lifts it)", GREEN_),
                (B, C, prof[1], prof[2], "−2 V  (I·R₁)", RED_),
                (C, D, prof[2], prof[3], "−4 V  (I·R₂)", RED_),
                (D, A, prof[3], prof[4], "0 — back where it started", GREY_)]
        trace = VMobject(color=AMBER_, stroke_width=4)
        trace.set_points_as_corners([ax.c2p(0, 0)])
        note = None
        for p, q, (x0, y0), (x1, y1), text, col in segs:
            seg = Line(ax.c2p(x0, y0), ax.c2p(x1, y1), color=col, stroke_width=4)
            new_note = Text(text, font_size=24, color=col).next_to(ax, DOWN, buff=0.9)
            anims = [coulomb.animate.move_to(q), marker.animate.move_to(ax.c2p(x1, y1)), Create(seg)]
            anims.append(FadeIn(new_note) if note is None else Transform(note, new_note))
            if note is None:
                note = new_note
            self.play(*anims, run_time=1.6)
        eq = MathTex(r"\sum \mathcal{E} \;=\; \sum I\,R", font_size=44, color=GREY_).next_to(title, DOWN, buff=0.25)
        self.play(Write(eq))
        self.wait(2)

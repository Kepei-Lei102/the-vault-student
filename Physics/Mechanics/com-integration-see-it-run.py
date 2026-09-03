# Animation stack: Manim (the bay's standard for exam-facing derivations).
# Render:  manim -qk com-integration-see-it-run.py SixSlices
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""All six formula-sheet centres of mass, integrated before your eyes.

One chapter per body. In each: the body appears, the SLICE sweeps through it
(the animation IS the integral), the moment sum lands, and the star marks the
answer. The sector and the shell get their no-integral arguments instead —
the fan of triangles, and Archimedes' hat-box. Ends on the six results
assembled: the MF19 table, earned."""
from manim import *
import numpy as np

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
TEAL = ManimColor("#0891b2")

BODY_X = -3.4        # bodies live on the left; math on the right
MATH_X = 3.1


class SixSlices(Scene):
    def chapter(self, n, name):
        tag = Text(f"{n}/6  {name}", font_size=30, color=GREY).to_edge(UP, buff=0.35)
        self.play(FadeIn(tag), run_time=0.6)
        return tag

    def land(self, formula, result, y=-0.4):
        f = MathTex(formula, font_size=38, color=GREY).move_to([MATH_X, 1.1, 0])
        r = MathTex(result, font_size=46, color=AMBER).move_to([MATH_X, y, 0])
        self.play(FadeIn(f), run_time=0.8)
        self.wait(0.9)
        self.play(FadeIn(r), run_time=0.8)
        return f, r

    def construct(self):
        opener = Text("the six standard centres of mass — earned, not memorised",
                      font_size=32, color=GREY)
        sub = Text("one move: slice so each slice's own centre of mass is known",
                   font_size=26, color=AMBER).next_to(opener, DOWN, buff=0.3)
        self.play(FadeIn(opener), FadeIn(sub), run_time=1.0)
        self.wait(1.6)
        self.play(FadeOut(opener), FadeOut(sub), run_time=0.6)

        results = []

        # ---------------- 1. triangle ----------------
        tag = self.chapter(1, "triangular lamina — strips")
        h = 3.4
        apex = np.array([BODY_X, 1.9, 0])
        b1 = apex + np.array([-1.9, -h, 0]); b2 = apex + np.array([1.9, -h, 0])
        tri = Polygon(apex, b1, b2, color=BLUE, fill_opacity=0.15, stroke_width=3)
        self.play(Create(tri), run_time=0.8)
        tr = ValueTracker(0.12)
        def strip():
            f = tr.get_value()
            p1 = apex + f * (b1 - apex); p2 = apex + f * (b2 - apex)
            return Line(p1, p2, color=AMBER, stroke_width=10)
        st = always_redraw(strip)
        lab = Text("width grows like x", font_size=24, color=AMBER).move_to([BODY_X, -2.3, 0])
        self.add(st)
        self.play(FadeIn(lab), run_time=0.5)
        self.play(tr.animate.set_value(0.97), run_time=2.6, rate_func=linear)
        f1, r1 = self.land(r"\bar{x} = \frac{\int_0^h x\cdot x\,dx}{\int_0^h x\,dx}",
                           r"\tfrac{2h}{3}\ \text{from the vertex}")
        star = Star(color=AMBER, fill_opacity=1).scale(0.16).move_to(
            apex + (2/3) * ((b1 + b2) / 2 - apex))
        self.play(FadeIn(star), run_time=0.5)
        self.wait(1.2)
        results.append(r"\text{triangle: } \tfrac23\ \text{median}")
        self.play(*[FadeOut(m) for m in (tag, tri, st, lab, f1, r1, star)], run_time=0.6)

        # ---------------- 2. arc ----------------
        tag = self.chapter(2, "circular arc — beads")
        r_, al = 2.5, np.radians(55)
        ctr = np.array([BODY_X - 0.6, -0.3, 0])
        tt = np.linspace(-al, al, 80)
        arc = VMobject(color=BLUE, stroke_width=6).set_points_smoothly(
            [ctr + r_ * np.array([np.cos(t), np.sin(t), 0]) for t in tt])
        self.play(Create(arc), run_time=0.8)
        tb = ValueTracker(-al)
        bead = always_redraw(lambda: Dot(
            ctr + r_ * np.array([np.cos(tb.get_value()), np.sin(tb.get_value()), 0]),
            color=AMBER, radius=0.11))
        lab = MathTex(r"\text{bead } r\,d\theta \text{ at } x = r\cos\theta",
                      font_size=30, color=AMBER).move_to([BODY_X, -2.5, 0])
        self.add(bead)
        self.play(FadeIn(lab), run_time=0.5)
        self.play(tb.animate.set_value(al), run_time=2.4, rate_func=linear)
        f1, r1 = self.land(r"\bar{x} = \frac{\int_{-\alpha}^{\alpha} r\cos\theta\; r\,d\theta}{2\alpha r}",
                           r"\frac{r\sin\alpha}{\alpha}\ \text{from the centre}")
        star = Star(color=AMBER, fill_opacity=1).scale(0.16).move_to(
            ctr + np.array([r_ * np.sin(al) / al, 0, 0]))
        self.play(FadeIn(star), run_time=0.5)
        self.wait(1.2)
        self.play(*[FadeOut(m) for m in (tag, arc, bead, lab, f1, r1, star)], run_time=0.6)

        # ---------------- 3. sector (no integral) ----------------
        tag = self.chapter(3, "circular sector — a fan of triangles, no integral")
        sector = AnnularSector(inner_radius=0, outer_radius=r_, angle=2 * al,
                               start_angle=-al, color=BLUE, fill_opacity=0.15,
                               stroke_width=3).move_arc_center_to(ctr)
        self.play(FadeIn(sector), run_time=0.7)
        fan_dots = []
        for t in np.linspace(-al * 0.9, al * 0.9, 7):
            ray = Line(ctr, ctr + r_ * np.array([np.cos(t), np.sin(t), 0]),
                       color=BLUE, stroke_width=1.5, stroke_opacity=0.6)
            d = Dot(ctr + (2 * r_ / 3) * np.array([np.cos(t), np.sin(t), 0]),
                    color=RED, radius=0.07)
            self.play(Create(ray), FadeIn(d), run_time=0.28)
            fan_dots.append((ray, d))
        note = Text("each thin triangle: CM at 2r/3 — so the sector IS an arc of radius 2r/3",
                    font_size=24, color=RED).to_edge(DOWN, buff=0.45)
        dashed = DashedVMobject(VMobject(color=RED, stroke_width=4).set_points_smoothly(
            [ctr + (2*r_/3) * np.array([np.cos(t), np.sin(t), 0]) for t in tt]),
            num_dashes=22)
        self.play(FadeIn(note), Create(dashed), run_time=1.0)
        self.wait(1.4)
        f1, r1 = self.land(r"\text{arc result, } r \to \tfrac{2r}{3}",
                           r"\frac{2r\sin\alpha}{3\alpha}\ \text{from the centre}")
        self.wait(1.4)
        self.play(*[FadeOut(m) for pair in fan_dots for m in pair],
                  *[FadeOut(m) for m in (tag, sector, note, dashed, f1, r1)], run_time=0.7)

        # ---------------- 4. cone ----------------
        tag = self.chapter(4, "solid cone — discs")
        H, Rb = 3.2, 1.6
        apex = np.array([BODY_X, 1.8, 0])
        base_y = apex[1] - H
        left = apex + np.array([-Rb, -H, 0]); right = apex + np.array([Rb, -H, 0])
        cone = Polygon(apex, left, right, color=BLUE, fill_opacity=0.12, stroke_width=3)
        base = Ellipse(width=2 * Rb, height=0.45, color=BLUE,
                       fill_opacity=0.15).move_to([BODY_X, base_y, 0])
        self.play(Create(cone), FadeIn(base), run_time=0.8)
        tc = ValueTracker(0.10)
        disc = always_redraw(lambda: Ellipse(
            width=2 * Rb * tc.get_value(), height=0.34, color=AMBER,
            fill_opacity=0.55).move_to([BODY_X, apex[1] - H * tc.get_value(), 0]))
        lab = MathTex(r"\text{disc area} \propto x^2", font_size=30,
                      color=AMBER).move_to([BODY_X, -2.55, 0])
        self.add(disc)
        self.play(FadeIn(lab), run_time=0.5)
        self.play(tc.animate.set_value(0.96), run_time=2.4, rate_func=linear)
        f1, r1 = self.land(r"\bar{x} = \frac{\int_0^h x\cdot x^2\,dx}{\int_0^h x^2\,dx}",
                           r"\tfrac{3h}{4}\ \text{from the vertex}")
        star = Star(color=AMBER, fill_opacity=1).scale(0.16).move_to(
            [BODY_X, apex[1] - 3 * H / 4, 0])
        self.play(FadeIn(star), run_time=0.5)
        self.wait(1.2)
        self.play(*[FadeOut(m) for m in (tag, cone, base, disc, lab, f1, r1, star)],
                  run_time=0.6)

        # ---------------- 5. solid hemisphere ----------------
        tag = self.chapter(5, "solid hemisphere — discs again")
        rr = 2.2
        ctr2 = np.array([BODY_X, -1.2, 0])
        dome = Arc(radius=rr, start_angle=0, angle=PI, color=BLUE,
                   stroke_width=3).move_arc_center_to(ctr2)
        flat = Ellipse(width=2 * rr, height=0.5, color=BLUE,
                       fill_opacity=0.15).move_to(ctr2)
        self.play(Create(dome), FadeIn(flat), run_time=0.8)
        th5 = ValueTracker(0.04)
        disc = always_redraw(lambda: Ellipse(
            width=2 * np.sqrt(max(rr**2 - (rr * th5.get_value())**2, 1e-4)),
            height=0.32, color=AMBER, fill_opacity=0.55
        ).move_to(ctr2 + np.array([0, rr * th5.get_value(), 0])))
        lab = MathTex(r"\text{disc radius} = \sqrt{r^2 - x^2}", font_size=30,
                      color=AMBER).move_to([BODY_X, -2.6, 0])
        self.add(disc)
        self.play(FadeIn(lab), run_time=0.5)
        self.play(th5.animate.set_value(0.96), run_time=2.4, rate_func=linear)
        f1, r1 = self.land(r"\bar{x} = \frac{\int_0^r x(r^2 - x^2)\,dx}{\int_0^r (r^2-x^2)\,dx}",
                           r"\tfrac{3r}{8}\ \text{from the centre}")
        star = Star(color=AMBER, fill_opacity=1).scale(0.16).move_to(
            ctr2 + np.array([0, 3 * rr / 8, 0]))
        self.play(FadeIn(star), run_time=0.5)
        self.wait(1.2)
        self.play(*[FadeOut(m) for m in (tag, dome, flat, disc, lab, f1, r1, star)],
                  run_time=0.6)

        # ---------------- 6. shell (no integral) ----------------
        tag = self.chapter(6, "hemispherical shell — Archimedes, no integral")
        shell = Arc(radius=rr, start_angle=0, angle=PI, color=BLUE,
                    stroke_width=7).move_arc_center_to(ctr2)
        self.play(Create(shell), run_time=0.8)
        edges = np.linspace(0.06, 0.98, 5)
        note = Text("cut at equal height spacings: every band has EQUAL area",
                    font_size=24, color=TEAL).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(note), run_time=0.6)
        for y0, y1 in zip(edges[:-1], edges[1:]):
            t0, t1 = np.arcsin(y0), np.arcsin(y1)
            band = VMobject(color=TEAL, stroke_width=12, stroke_opacity=0.65)
            ts = np.linspace(t0, t1, 24)
            band.set_points_smoothly(
                [ctr2 + rr * np.array([np.cos(t), np.sin(t), 0]) for t in ts])
            band2 = band.copy().flip(UP, about_point=ctr2)
            self.play(Create(band), Create(band2), run_time=0.5)
        note2 = Text("so the mass is uniform in height — the CM sits at half the height",
                     font_size=24, color=AMBER).to_edge(DOWN, buff=0.45)
        self.play(ReplacementTransform(note, note2), run_time=0.7)
        f1, r1 = self.land(r"\text{Archimedes' hat-box theorem, c. 250 BC}",
                           r"\tfrac{r}{2}\ \text{from the centre}")
        star = Star(color=AMBER, fill_opacity=1).scale(0.16).move_to(
            ctr2 + np.array([0, rr / 2, 0]))
        self.play(FadeIn(star), run_time=0.5)
        self.wait(1.4)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.7)

        # ---------------- closing: the table, earned ----------------
        head = Text("the formula sheet, earned", font_size=34, color=GREY)
        head.to_edge(UP, buff=0.6)
        rows = MathTex(
            r"\text{triangle: } \tfrac23 \text{ median} \qquad"
            r"\text{arc: } \tfrac{r\sin\alpha}{\alpha} \qquad"
            r"\text{sector: } \tfrac{2r\sin\alpha}{3\alpha}\\[0.6em]"
            r"\text{cone: } \tfrac34 h \qquad"
            r"\text{hemisphere: } \tfrac38 r \qquad"
            r"\text{shell: } \tfrac12 r",
            font_size=40, color=AMBER)
        moral = Text("six little facts, one slicing idea — rebuildable from a blank page",
                     font_size=27, color=GREEN).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(head), run_time=0.7)
        self.play(FadeIn(rows), run_time=1.0)
        self.play(FadeIn(moral), run_time=0.8)
        self.wait(2.6)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)



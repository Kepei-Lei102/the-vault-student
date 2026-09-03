"""Elastic strings in motion — companion clip for [[Elastic Strings and Springs]].

Chapter 1 — Pull down, let go (the N24/33 journey): a particle on a vertical
elastic string is pulled sqrt(5) m below equilibrium and released. The string
is drawn taut (blue) while stretched and slack (grey, sagging) above natural
length; energy bars trade EPE -> KE + GPE live; the particle just reaches O.

Chapter 2 — Where is the fastest? (the J25/31 incline): released above A on a
smooth slope, the particle passes A, the string re-engages on the far side,
and the speed readout peaks exactly where the forces balance — not where the
string goes slack.

Render:  manim -qk elastic-see-it-stretch.py ElasticSeeItStretch
"""
import numpy as np
from manim import *

GREY_TXT = "#888888"
BLUE_ = "#2563eb"
PURPLE_ = "#7c3aed"
GREEN_ = "#059669"
RED_ = "#dc2626"
AMBER_ = "#f59e0b"
TEAL_ = "#0891b2"


def integrate(accel, y0, v0, t_end, dt=1e-4):
    """Simple symplectic Euler; returns t, y, v arrays."""
    n = int(t_end / dt) + 1
    t = np.linspace(0, t_end, n)
    y = np.empty(n); v = np.empty(n)
    y[0], v[0] = y0, v0
    for i in range(1, n):
        v[i] = v[i - 1] + accel(y[i - 1], v[i - 1]) * dt
        y[i] = y[i - 1] + v[i] * dt
    return t, y, v


class ElasticSeeItStretch(Scene):
    def construct(self):
        self.chapter_vertical()
        self.chapter_incline()

    # ------------------------------------------------------------------
    def chapter_vertical(self):
        title = Text("Pull down, let go", font_size=40, color=WHITE)
        sub = Text("natural length 2, modulus 2mg  —  released sqrt(5) below equilibrium",
                   font_size=24, color=GREY_TXT).next_to(title, DOWN)
        self.play(FadeIn(title), FadeIn(sub))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # physics: m=1, g=10, L=2, lam=20 -> k=10; depth y below O
        g, k, L = 10.0, 10.0, 2.0
        d = np.sqrt(5)
        y0 = 3.0 + d

        def accel(y, v):
            ext = max(y - L, 0.0)
            return g - k * ext

        # simulate until particle returns to O (v=0 there) ~ find time
        t_arr, y_arr, v_arr = integrate(accel, y0, 0.0, 2.2)
        # cut at first index where y <= 0
        idx = np.argmax(y_arr <= 0.0)
        if idx == 0:
            idx = len(y_arr) - 1
        t_arr, y_arr, v_arr = t_arr[:idx + 1], y_arr[:idx + 1], v_arr[:idx + 1]
        t_total = t_arr[-1]

        # screen mapping: O at top, depth scaled
        top = np.array([-3.0, 3.2, 0.0])
        scale = 1.05  # screen units per metre

        def pos_of(y):
            return top + DOWN * scale * y

        # static furniture
        ceiling = Line(top + LEFT * 1.2, top + RIGHT * 1.2, color=GREY_TXT, stroke_width=6)
        o_label = MathTex("O", font_size=36, color=GREY_TXT).next_to(top, UP + RIGHT, buff=0.12)
        marks = VGroup()
        for depth, lab, col in [(L, r"\text{natural length}", TEAL_),
                                (3.0, r"\text{equilibrium}", GREEN_),
                                (y0, r"\text{start: } v=0", RED_)]:
            tick = Line(pos_of(depth) + LEFT * 0.45, pos_of(depth) + RIGHT * 0.45,
                        color=col, stroke_width=2.5)
            txt = MathTex(lab, font_size=26, color=GREY_TXT).next_to(tick, RIGHT, buff=0.15)
            marks.add(tick, txt)

        yt = ValueTracker(0.0)  # index into time

        def y_now():
            return float(np.interp(yt.get_value(), t_arr, y_arr))

        def v_now():
            return float(np.interp(yt.get_value(), t_arr, v_arr))

        ball = always_redraw(lambda: Dot(pos_of(y_now()), radius=0.16, color=AMBER_))

        def string_mobj():
            y = y_now()
            if y >= L:  # taut: straight line
                return Line(top, pos_of(y), color=BLUE_, stroke_width=4)
            # slack: sagging quadratic bezier to the side
            sag = 0.55 * (L - y) / L + 0.12
            mid = (top + pos_of(y)) / 2 + RIGHT * sag
            return CubicBezier(top, top + DOWN * 0.2 + RIGHT * sag * 0.7, mid,
                               pos_of(y), color=GREY_TXT, stroke_width=3)

        string = always_redraw(string_mobj)

        state = always_redraw(lambda: Text(
            "TAUT" if y_now() >= L else "SLACK",
            font_size=28,
            color=BLUE_ if y_now() >= L else GREY_TXT,
        ).move_to(top + LEFT * 2.2 + DOWN * 0.4))

        # energy bars (right side)
        E_tot = g * y0  # datum at O; EPE + KE + GPE-deficit… use: KE + EPE + (E_tot - g*y) ... simpler:
        # measure GPE from lowest point: GPE = g*(y0 - y); EPE = k*ext^2/2; KE = v^2/2
        bar_x = 3.4
        labels = ["EPE", "GPE", "KE"]
        cols = [BLUE_, GREEN_, AMBER_]

        def energies():
            y, v = y_now(), v_now()
            ext = max(y - L, 0.0)
            return [0.5 * k * ext ** 2, g * (y0 - y), 0.5 * v ** 2]

        E_max = max(sum(energies()), 1e-9)

        def make_bar(i):
            def f():
                e = energies()[i]
                h = 4.6 * e / E_max + 1e-3
                r = Rectangle(width=0.5, height=h, fill_color=cols[i],
                              fill_opacity=0.85, stroke_width=0)
                r.move_to(np.array([bar_x + i * 0.85, -2.6 + h / 2, 0.0]))
                return r
            return always_redraw(f)

        bars = [make_bar(i) for i in range(3)]
        bar_labels = VGroup(*[
            Text(labels[i], font_size=22, color=GREY_TXT).move_to(
                np.array([bar_x + i * 0.85, -2.95, 0.0]))
            for i in range(3)
        ])

        self.play(Create(ceiling), FadeIn(o_label), FadeIn(marks))
        self.add(string, ball, state, *bars, bar_labels)
        self.wait(0.8)

        # play the journey in slow motion (~4x slower than real time)
        self.play(yt.animate.set_value(t_total), run_time=4.0 * t_total,
                  rate_func=linear)

        arrive = Text("just reaches O: v = 0", font_size=30, color=GREEN_)
        arrive.next_to(pos_of(0), RIGHT, buff=0.9).shift(DOWN * 0.55)
        self.play(FadeIn(arrive))
        self.wait(1.6)

        note = Text("taut: EPE drives it up      slack: pure free flight",
                    font_size=26, color=GREY_TXT).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note))
        self.wait(2.2)
        self.play(*[FadeOut(m) for m in self.mobjects])

    # ------------------------------------------------------------------
    def chapter_incline(self):
        title = Text("Where is the fastest?", font_size=40, color=WHITE)
        sub = Text("released above A on a smooth slope — the string will pass through slack",
                   font_size=24, color=GREY_TXT).next_to(title, DOWN)
        self.play(FadeIn(title), FadeIn(sub))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # physics (J25/31 Q5): m=2, lam=14, L=0.5, sin a = 7/25, g=10
        g_sin = 2.8          # g sin(alpha)
        kk = 14.0            # lam/(m L)
        Lnat = 0.5

        def accel(p, v):
            if p > Lnat:
                return -g_sin - kk * (p - Lnat)
            if p < -Lnat:
                return -g_sin + kk * (-p - Lnat)
            return -g_sin

        t_arr, p_arr, v_arr = integrate(accel, 0.8, 0.0, 2.5)
        # stop shortly after the low point (first v >= 0 after start)
        idx = np.argmax(v_arr[1:] >= 0.0) + 1
        if idx <= 1:
            idx = len(p_arr) - 1
        t_arr, p_arr, v_arr = t_arr[:idx + 1], p_arr[:idx + 1], v_arr[:idx + 1]
        t_total = t_arr[-1]
        i_max = int(np.argmax(np.abs(v_arr)))
        p_max, v_max = p_arr[i_max], abs(v_arr[i_max])

        # slope geometry on screen: angle drawn steeper than 16 deg for legibility
        ang = 25 * DEGREES
        e_up = np.array([np.cos(ang), np.sin(ang), 0.0])   # up-slope unit vector
        A_pt = np.array([0.2, -0.4, 0.0])
        slope = Line(A_pt - e_up * 3.4, A_pt + e_up * 3.0, color=GREY_TXT, stroke_width=5)
        a_dot = Dot(A_pt, radius=0.09, color=PURPLE_)
        a_lab = MathTex("A", font_size=34, color=GREY_TXT).next_to(a_dot, DOWN, buff=0.18)

        sc = 2.2  # screen units per metre along slope

        def pos_of(p):
            return A_pt + e_up * sc * p

        # markers
        marks = VGroup()
        for p, lab, col in [(0.8, r"\text{start}", RED_),
                            (-0.7, r"a = 0", GREEN_)]:
            tick = Line(pos_of(p) + np.array([0, 0.18, 0]), pos_of(p) - np.array([0, 0.18, 0]),
                        color=col, stroke_width=3)
            txt = MathTex(lab, font_size=28, color=GREY_TXT).next_to(tick, UP, buff=0.15)
            marks.add(tick, txt)

        pt = ValueTracker(0.0)

        def p_now():
            return float(np.interp(pt.get_value(), t_arr, p_arr))

        def v_now():
            return float(np.interp(pt.get_value(), t_arr, v_arr))

        ball = always_redraw(lambda: Dot(pos_of(p_now()), radius=0.15, color=AMBER_))

        def string_mobj():
            p = p_now()
            if abs(p) >= Lnat:
                return Line(A_pt, pos_of(p), color=BLUE_, stroke_width=4)
            sag = 0.32 * (Lnat - abs(p)) / Lnat + 0.06
            perp = np.array([-e_up[1], e_up[0], 0.0])
            mid = (A_pt + pos_of(p)) / 2 - perp * sag
            return CubicBezier(A_pt, mid, mid, pos_of(p), color=GREY_TXT, stroke_width=3)

        string = always_redraw(string_mobj)

        speed_txt = always_redraw(lambda: Text(
            f"speed: {abs(v_now()):.2f} m/s", font_size=30,
            color=GREEN_ if abs(abs(v_now()) - v_max) < 0.03 else GREY_TXT,
        ).to_corner(UR, buff=0.6))

        vel_arrow = always_redraw(lambda: Arrow(
            pos_of(p_now()),
            pos_of(p_now()) + (-e_up) * (0.45 * abs(v_now())),
            buff=0.05, color=GREEN_, stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        ))

        self.play(Create(slope), FadeIn(a_dot), FadeIn(a_lab), FadeIn(marks))
        self.add(string, ball, vel_arrow, speed_txt)
        self.wait(0.8)

        self.play(pt.animate.set_value(t_total), run_time=5.0 * t_total,
                  rate_func=linear)

        peak = MathTex(r"\text{fastest where } T = mg\sin\alpha,\ \text{not where the string goes slack}",
                       font_size=32, color=GREY_TXT).to_edge(DOWN, buff=0.5)
        ring = Circle(radius=0.28, color=GREEN_, stroke_width=3).move_to(pos_of(p_max))
        self.play(FadeIn(peak), Create(ring))
        self.wait(2.4)
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.4)

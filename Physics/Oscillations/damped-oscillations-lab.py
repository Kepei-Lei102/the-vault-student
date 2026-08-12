"""Damped Oscillations — the three-jar race.

One spring-mass system in three fluids (air / oil / honey), released together:
light, critical and heavy damping racing home, with live displacement traces.

Render (on the Mac, LaTeX at /Library/TeX/texbin):
    manim -qm damped-oscillations-lab.py DampedLab     # smoke
    manim -qk damped-oscillations-lab.py DampedLab     # 4K final
then copy media/videos/damped-oscillations-lab/2160p60/DampedLab.mp4
to damped-oscillations-lab.mp4 beside the card and `rm -rf media`.
"""
import numpy as np
from manim import *

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#888888"
C_BLUE = "#3b82f6"   # light damping
C_GREEN = "#10b981"  # critical
C_RED = "#ef4444"    # heavy
C_AMBER = "#fbbf24"  # highlight / envelope

W0 = 2 * np.pi
G_LIGHT = 0.35
G_HEAVY = 3 * W0


def x_light(t):
    wd = np.sqrt(W0**2 - G_LIGHT**2)
    return np.exp(-G_LIGHT * t) * (np.cos(wd * t) + (G_LIGHT / wd) * np.sin(wd * t))


def x_crit(t):
    return (1 + W0 * t) * np.exp(-W0 * t)


def x_heavy(t):
    s = np.sqrt(G_HEAVY**2 - W0**2)
    l1, l2 = -G_HEAVY + s, -G_HEAVY - s
    return (l2 * np.exp(l1 * t) - l1 * np.exp(l2 * t)) / (l2 - l1)


class DampedLab(Scene):
    def caption(self, tex, color=TXT):
        new = Tex(tex, color=color, font_size=40).move_to([0, 3.6, 0])
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.25), FadeIn(new, run_time=0.25))
        else:
            self.play(FadeIn(new, run_time=0.4))
        self._cap = new

    def spring(self, x0, mass_y):
        top = np.array([x0, 3.0, 0])
        bot = np.array([x0, mass_y + 0.25, 0])
        lead = 0.15
        n = 12
        pts = [top, top + DOWN * lead]
        y0, y1 = top[1] - lead, bot[1] + lead
        for i in range(1, n):
            y = y0 + (y1 - y0) * i / n
            dx = 0.22 if i % 2 else -0.22
            pts.append(np.array([x0 + dx, y, 0]))
        pts += [bot + UP * lead, bot]
        return VMobject(stroke_color=GREY, stroke_width=3).set_points_as_corners(pts)

    def construct(self):
        self.camera.background_color = BG
        self._cap = None

        XS = [-4.2, 0.0, 4.2]
        Y_EQ, AMP = 1.0, 1.0
        funcs = [x_light, x_crit, x_heavy]
        cols = [C_BLUE, C_GREEN, C_RED]

        # ceiling
        ceiling = Line([-5.6, 3.0, 0], [5.6, 3.0, 0], color=GREY, stroke_width=3)
        hatches = VGroup(*[
            Line([x, 3.0, 0], [x + 0.22, 3.25, 0], color=GREY, stroke_width=2)
            for x in np.arange(-5.6, 5.5, 0.45)
        ])

        # jars (open-top) + fluids
        jars, fluids = VGroup(), VGroup()
        for x0, fluid_col, op in zip(XS, [None, C_BLUE, C_AMBER], [0, 0.10, 0.16]):
            wall = VMobject(stroke_color="#555555", stroke_width=3)
            wall.set_points_as_corners([
                [x0 - 0.85, 2.45, 0], [x0 - 0.85, -0.5, 0],
                [x0 + 0.85, -0.5, 0], [x0 + 0.85, 2.45, 0],
            ])
            jars.add(wall)
            if fluid_col:
                fluids.add(Rectangle(width=1.66, height=2.56, stroke_width=0,
                                     fill_color=fluid_col, fill_opacity=op)
                           .move_to([x0, 0.79, 0]))

        labels = VGroup(
            Tex(r"AIR --- light ($\gamma \ll \omega_0$)", color=C_BLUE, font_size=32),
            Tex(r"OIL --- critical ($\gamma = \omega_0$)", color=C_GREEN, font_size=32),
            Tex(r"HONEY --- heavy ($\gamma > \omega_0$)", color=C_RED, font_size=32),
        )
        for lab, x0 in zip(labels, XS):
            lab.move_to([x0, -1.1, 0])

        # time tracker + masses + springs
        t = ValueTracker(0.0)
        masses, springs = VGroup(), VGroup()
        for x0, f, c in zip(XS, funcs, cols):
            m = Square(side_length=0.5, fill_color=c, fill_opacity=1,
                       stroke_color=WHITE, stroke_width=1.5)
            # pulled DOWN at t=0: visual position is equilibrium minus displacement
            m.add_updater(lambda mob, x0=x0, f=f:
                          mob.move_to([x0, Y_EQ - AMP * f(t.get_value()), 0]))
            m.update()
            masses.add(m)
            springs.add(always_redraw(
                lambda x0=x0, f=f: self.spring(x0, Y_EQ - AMP * f(t.get_value()))))

        # trace axes
        axes = Axes(x_range=[0, 6, 1], y_range=[-1, 1, 1],
                    x_length=11.5, y_length=1.9,
                    axis_config=dict(color="#666666", stroke_width=2,
                                     include_ticks=False, include_tip=False))
        axes.move_to([0.3, -2.6, 0])
        t_lab = Tex("$t$", color=GREY, font_size=30).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        x_lab = Tex("$x$", color=GREY, font_size=30).next_to(axes.y_axis.get_top(), LEFT, buff=0.15)

        trace_dots, traces = VGroup(), VGroup()
        for f, c in zip(funcs, cols):
            d = Dot(radius=0.05, color=c).move_to(axes.c2p(0, f(0)))
            d.add_updater(lambda mob, f=f:
                          mob.move_to(axes.c2p(t.get_value(), f(t.get_value()))))
            trace_dots.add(d)
            traces.add(TracedPath(d.get_center, stroke_color=c, stroke_width=3.5))

        # --- build the stage ---
        self.play(Create(ceiling), FadeIn(hatches), FadeIn(jars), FadeIn(fluids),
                  run_time=1.0)
        self.play(*[Create(s) for s in springs], FadeIn(masses), FadeIn(labels),
                  FadeIn(axes), FadeIn(t_lab), FadeIn(x_lab), run_time=1.2)
        self.caption(r"One spring, three fluids --- all pulled down the same distance")
        self.wait(1.2)
        self.add(*traces, *trace_dots)

        # --- release, in segments with caption swaps ---
        self.caption(r"Released together --- watch who gets home", C_AMBER)
        self.play(t.animate.set_value(1.3), run_time=3.4, rate_func=linear)
        self.caption(r"OIL is already home; HONEY is still crawling")
        self.play(t.animate.set_value(3.0), run_time=3.8, rate_func=linear)
        self.caption(r"AIR rings on --- losing the same \emph{fraction} every cycle")
        self.play(t.animate.set_value(6.0), run_time=5.2, rate_func=linear)

        # --- the envelope cage on the trace ---
        env_u = DashedVMobject(axes.plot(lambda s: np.exp(-G_LIGHT * s),
                                         x_range=[0, 6], color=C_AMBER,
                                         stroke_width=2.5), num_dashes=45)
        env_d = DashedVMobject(axes.plot(lambda s: -np.exp(-G_LIGHT * s),
                                         x_range=[0, 6], color=C_AMBER,
                                         stroke_width=2.5), num_dashes=45)
        self.caption(r"the shrinking cage: envelope $\pm A_0 e^{-\gamma t}$", C_AMBER)
        self.play(Create(env_u), Create(env_d), run_time=1.6)
        self.wait(1.0)

        self.caption(r"\textbf{more damping $\neq$ faster return}", C_AMBER)
        self.wait(2.0)


class QCounter(Scene):
    """Q counts the swings the ring survives: two counted runs, then the ladder."""

    def caption(self, tex, color=TXT):
        new = Tex(tex, color=color, font_size=40).move_to([0, 3.6, 0])
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.25), FadeIn(new, run_time=0.25))
        else:
            self.play(FadeIn(new, run_time=0.4))
        self._cap = new

    def ring_run(self, Q, t_max, x_max, run_time):
        g = PI / Q                       # gamma = omega0/(2Q), omega0 = 2*pi
        wd = np.sqrt((2 * PI) ** 2 - g**2)
        Td = 2 * PI / wd

        def xf(tt):
            return np.exp(-g * tt) * (np.cos(wd * tt) + (g / wd) * np.sin(wd * tt))

        axes = Axes(x_range=[0, x_max, max(1, x_max // 8)], y_range=[-1, 1, 1],
                    x_length=11.6, y_length=4.0,
                    axis_config=dict(color="#666666", stroke_width=2,
                                     include_ticks=False, include_tip=False))
        axes.move_to([0.2, -0.9, 0])
        t_lab = Tex("$t$", color=GREY, font_size=30).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)

        env_u = DashedVMobject(axes.plot(lambda s: np.exp(-g * s), x_range=[0, x_max],
                                         color=C_AMBER, stroke_width=2.5), num_dashes=50)
        env_d = DashedVMobject(axes.plot(lambda s: -np.exp(-g * s), x_range=[0, x_max],
                                         color=C_AMBER, stroke_width=2.5), num_dashes=50)
        thresh = DashedVMobject(axes.plot(lambda s: 0.043, x_range=[0, x_max],
                                          color="#777777", stroke_width=2), num_dashes=60)
        th_lab = Tex(r"4\% of $A_0$ --- the ring is spent", color="#999999",
                     font_size=26).next_to(axes.c2p(x_max, 0.043), UP + LEFT, buff=0.12)

        q_lab = Tex(f"$Q = {Q}$", color=C_AMBER, font_size=48).move_to([-5.6, 2.5, 0])
        sw_lab = Tex("swings:", color=TXT, font_size=40).move_to([4.0, 2.5, 0])
        counter = Integer(0, color=C_GREEN, font_size=52)

        t = ValueTracker(0.0)

        def upd_counter(m):
            m.set_value(int(t.get_value() / Td + 1e-6))
            m.next_to(sw_lab, RIGHT, buff=0.25)
        counter.add_updater(upd_counter)
        counter.update()

        dot = Dot(radius=0.055, color=C_BLUE).move_to(axes.c2p(0, xf(0)))
        dot.add_updater(lambda m: m.move_to(axes.c2p(t.get_value(), xf(t.get_value()))))
        trace = TracedPath(dot.get_center, stroke_color=C_BLUE, stroke_width=3.5)

        self.play(FadeIn(axes), FadeIn(t_lab), FadeIn(env_u), FadeIn(env_d),
                  FadeIn(thresh), FadeIn(th_lab), FadeIn(q_lab), FadeIn(sw_lab),
                  FadeIn(counter), run_time=0.9)
        self.add(trace, dot)
        self.play(t.animate.set_value(t_max), run_time=run_time, rate_func=linear)

        counter.clear_updaters()
        box = SurroundingRectangle(VGroup(sw_lab, counter), color=C_GREEN, buff=0.18)
        verdict = Tex(r"swings $\approx Q$", color=C_GREEN, font_size=40)
        verdict.next_to(box, DOWN, buff=0.2)
        self.play(Create(box), FadeIn(verdict), run_time=0.6)
        self.wait(1.3)
        return VGroup(axes, t_lab, env_u, env_d, thresh, th_lab, q_lab,
                      sw_lab, counter, dot, trace, box, verdict)

    def construct(self):
        self.camera.background_color = BG
        self._cap = None

        self.caption(r"$Q$ counts the swings the ring survives")
        grp = self.ring_run(Q=6, t_max=6.35, x_max=7, run_time=7.0)
        self.caption(r"a higher $Q$ --- same rule, more swings", C_AMBER)
        self.play(FadeOut(grp, run_time=0.5))
        grp2 = self.ring_run(Q=15, t_max=15.6, x_max=16, run_time=6.5)
        self.play(FadeOut(grp2, run_time=0.5))

        # --- the ladder ---
        self.caption(r"the better it keeps time, the higher its $Q$")
        items = [
            (r"door closer", r"$0.5$", -0.301),
            (r"car suspension", r"$\sim 1$", 0.0),
            (r"playground swing", r"$\sim 10^2$", 2),
            (r"guitar string", r"$\sim 10^3$", 3),
            (r"tuning fork", r"$\sim 10^4$", 4),
            (r"quartz crystal", r"$\sim 10^5$", 5),
            (r"excited atom", r"$\sim 10^7$", 7),
            (r"caesium clock", r"$\sim 10^{10}$", 10),
        ]
        SCALE, X0, Y0, DY = 0.62, -2.4, 2.6, 0.62
        rows, bars = VGroup(), []
        for i, (name, val, logq) in enumerate(items):
            y = Y0 - i * DY
            is_cs = (i == len(items) - 1)
            col = C_AMBER if is_cs else "#22d3ee"
            label = Tex(name, color=TXT, font_size=30)
            label.move_to([X0 - 0.25 - label.width / 2, y, 0])
            w = max(0.14, SCALE * logq)
            bar = Rectangle(width=w, height=0.32, stroke_width=0,
                            fill_color=col, fill_opacity=0.9)
            bar.move_to([X0 + w / 2, y, 0])
            vlab = Tex(val, color=col, font_size=30)
            vlab.move_to([X0 + w + 0.22 + vlab.width / 2, y, 0])
            rows.add(label, vlab)
            bars.append(bar)
        self.play(FadeIn(rows, run_time=0.8))
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars],
                              lag_ratio=0.15, run_time=3.2))
        self.wait(0.8)
        self.caption(r"caesium rings $10^{10}$ times --- that sharpness \textbf{defines the second}", C_AMBER)
        self.wait(2.2)

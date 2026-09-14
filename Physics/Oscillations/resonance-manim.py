"""Resonance, motion first.

Scene 1  ResonanceDrive : a platform shakes a ball on a spring at three frequencies
                          (half, equal, double the natural frequency); the amplitude
                          each one reaches is plotted live, then the whole curve appears.
Scene 2  PushTiming     : why the natural frequency wins -- force and velocity arrows stay
                          aligned at resonance (energy always in), and fight above it.

Render:  manim -qk resonance-manim.py ResonanceDrive PushTiming
         then concatenate: ffmpeg -f concat -safe 0 -i list.txt -c copy resonance-manim.mp4
"""
from manim import *
import math

BLUE, AMBER, RED, GREEN, GREY = "#2563eb", "#f59e0b", "#dc2626", "#059669", "#888888"
config.background_color = "#1e1e1e"


def spring_between(top, bottom, coils=9, width=0.3):
    pts = [top]
    n = 2 * coils
    for i in range(1, n):
        frac = i / n
        p = top + (bottom - top) * frac
        pts.append(p + RIGHT * width * (1 if i % 2 else -1) * (0.5 if i in (1, n - 1) else 1))
    pts.append(bottom)
    return VMobject(stroke_color=GREY, stroke_width=3).set_points_as_corners(pts)


class ResonanceDrive(Scene):
    def construct(self):
        f0 = 1.0; w0 = 2 * math.pi * f0; Q = 8; gamma = w0 / (2 * Q)
        a = 0.12                      # platform amplitude, scene units
        st = dict(x=0.0, v=0.0, t=0.0, f=0.5, run=False, peak=0.0, measure_from=0.0)

        # ---- left: platform, spring, ball ----
        y_plat, y_ball = 2.6, -0.9; x_rig = -4.2
        rail = Line([x_rig, -2.2, 0], [x_rig, 3.3, 0], color=GREY, stroke_width=2)
        plat = Rectangle(width=1.6, height=0.16, fill_color=GREY, fill_opacity=1, stroke_width=0).move_to([x_rig, y_plat, 0])
        ball = Circle(radius=0.28, fill_color=BLUE, fill_opacity=1, stroke_width=0).move_to([x_rig, y_ball, 0])
        eq_line = DashedLine([x_rig - 1.3, y_ball, 0], [x_rig + 1.3, y_ball, 0], color=GREY, stroke_width=1.5)
        plat_label = Text("platform (driver)", font_size=22, color=GREY).next_to(rail, UP, buff=0.05).shift(RIGHT * 0.9)

        def u(t): return a * math.cos(2 * math.pi * st["f"] * t)
        def du(t): return -a * 2 * math.pi * st["f"] * math.sin(2 * math.pi * st["f"] * t)

        def step(mob, dt):
            if not st["run"]: return
            # base-excited damped oscillator: x'' = -w0^2 (x - u) - 2 gamma (x' - u'), RK4 with substeps
            n = 8; h = dt / n
            for _ in range(n):
                t, x, v = st["t"], st["x"], st["v"]
                def acc(tt, xx, vv): return -w0 ** 2 * (xx - u(tt)) - 2 * gamma * (vv - du(tt))
                k1x, k1v = v, acc(t, x, v)
                k2x, k2v = v + 0.5 * h * k1v, acc(t + 0.5 * h, x + 0.5 * h * k1x, v + 0.5 * h * k1v)
                k3x, k3v = v + 0.5 * h * k2v, acc(t + 0.5 * h, x + 0.5 * h * k2x, v + 0.5 * h * k2v)
                k4x, k4v = v + h * k3v, acc(t + h, x + h * k3x, v + h * k3v)
                st["x"] = x + h * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
                st["v"] = v + h * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
                st["t"] = t + h
            if st["t"] >= st["measure_from"]: st["peak"] = max(st["peak"], abs(st["x"]))
            plat.move_to([x_rig, y_plat + u(st["t"]), 0])
            ball.move_to([x_rig, y_ball + st["x"], 0])

        plat.add_updater(step)
        spring = always_redraw(lambda: spring_between(plat.get_bottom(), ball.get_top()))

        # ---- right: live amplitude-vs-frequency plot ----
        axes = Axes(x_range=[0, 2.2, 0.5], y_range=[0, 10, 2], x_length=6.0, y_length=4.4,
                    axis_config=dict(color=GREY, stroke_width=2, include_tip=False, font_size=22)).shift(RIGHT * 2.4 + UP * 0.45)
        xl = Text("driving frequency ÷ natural frequency", font_size=22, color=GREY).next_to(axes.get_x_axis(), DOWN, buff=0.4)
        yl = axes.get_y_axis_label(Text("amplitude ÷ platform amplitude", font_size=22, color=GREY).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.3)
        axes.add_coordinates()
        for m in axes.get_x_axis().numbers + axes.get_y_axis().numbers: m.set_color(GREY)

        caption = Text("a ball on a spring, shaken from above\nby a platform of fixed amplitude", font_size=24, color=GREY, line_spacing=0.9).to_edge(DOWN, buff=0.3)
        self.add(rail, plat, spring, ball, eq_line, plat_label, axes, xl, yl, caption)

        def say(txt, color=GREY):
            new = Text(txt, font_size=24, color=color, line_spacing=0.9).to_edge(DOWN, buff=0.3)
            self.play(Transform(caption, new), run_time=0.6)

        def drive(f, seconds, text, color):
            st.update(f=f, run=True, peak=0.0, measure_from=seconds - 2.0)
            say(text, color)
            self.wait(seconds)
            st["run"] = False
            amp = st["peak"] / a
            dot = Dot(axes.c2p(f / f0, min(amp, 9.8)), color=color, radius=0.09)
            lab = Text(f"{amp:.1f}×", font_size=22, color=color).next_to(dot, UR if f < 1.5 else UL, buff=0.08)
            self.play(FadeIn(dot, scale=0.5), FadeIn(lab), run_time=0.6)
            # bring the ball to rest before the next run
            st.update(x=0.0, v=0.0, t=0.0)
            plat.move_to([x_rig, y_plat + a, 0]); ball.move_to([x_rig, y_ball, 0])
            self.wait(0.4)

        drive(0.5, 10, "half the natural frequency:\nthe ball follows the platform, a little bigger", GREY)
        drive(1.0, 14, "at the natural frequency: every cycle adds energy,\nand the ring grows for about Q/π cycles before settling", BLUE)
        drive(2.0, 10, "twice the natural frequency:\nthe ball cannot keep up, moves the other way, and stays small", GREY)

        zeta = 1 / (2 * Q)
        def T(r): return math.sqrt(1 + (2 * zeta * r) ** 2) / math.sqrt((1 - r * r) ** 2 + (2 * zeta * r) ** 2)
        curve = axes.plot(lambda r: min(T(r), 9.8), x_range=[0.02, 2.2, 0.01], color=BLUE, stroke_width=3)
        say("the resonance curve: maximum amplitude\nwhen the driving frequency equals the natural frequency", BLUE)
        self.play(Create(curve), run_time=2.5)
        self.wait(2.5)


class PushTiming(Scene):
    def construct(self):
        f0 = 1.0; w0 = 2 * math.pi * f0; Q = 8; gamma = w0 / (2 * Q); F0 = 1.0
        st = dict(x=0.0, v=0.0, t=0.0, f=1.0, run=False, E=0.0)
        y0 = 0.6
        wall = Line([-6.2, y0 - 0.7, 0], [-6.2, y0 + 0.7, 0], color=GREY, stroke_width=4)
        floor = Line([-6.2, y0 - 0.45, 0], [6.5, y0 - 0.45, 0], color=GREY, stroke_width=2)
        block = Square(side_length=0.9, fill_color=BLUE, fill_opacity=1, stroke_width=0).move_to([0, y0, 0])
        spring = always_redraw(lambda: spring_between(wall.get_center(), block.get_left(), coils=12, width=0.22).rotate(0))
        # horizontal spring: build from a vertical helper rotated -- simpler: draw a zigzag by hand
        def hspring():
            top = wall.get_center(); bot = block.get_left(); pts = [top]; n = 24
            for i in range(1, n):
                p = top + (bot - top) * (i / n)
                pts.append(p + UP * 0.22 * (1 if i % 2 else -1) * (0.5 if i in (1, n - 1) else 1))
            pts.append(bot)
            return VMobject(stroke_color=GREY, stroke_width=3).set_points_as_corners(pts)
        spring = always_redraw(hspring)
        F_arrow = always_redraw(lambda: Arrow(block.get_center() + UP * 0.9, block.get_center() + UP * 0.9 + RIGHT * 2.2 * F0 * math.cos(2 * math.pi * st["f"] * st["t"]), color=AMBER, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.25))
        v_arrow = always_redraw(lambda: Arrow(block.get_center() + DOWN * 0.9, block.get_center() + DOWN * 0.9 + RIGHT * 1.6 * st["v"], color=GREEN, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.25))
        F_lab = Text("driving force F", font_size=22, color=AMBER).to_corner(UL, buff=0.5)
        v_lab = Text("velocity v", font_size=22, color=GREEN).next_to(F_lab, DOWN, aligned_edge=LEFT)
        # energy bar
        bar_bg = Rectangle(width=0.5, height=4.6, stroke_color=GREY, stroke_width=2).move_to([6.0, y0 - 0.2, 0])
        bar = always_redraw(lambda: Rectangle(width=0.5, height=max(min(5 * st["E"], 4.6), 0.02), fill_color=AMBER, fill_opacity=0.9, stroke_width=0)
                            .move_to(bar_bg.get_bottom(), aligned_edge=DOWN))
        bar_lab = Text("energy", font_size=20, color=GREY).next_to(bar_bg, UP, buff=0.1)

        def step(mob, dt):
            if not st["run"]: return
            n = 8; h = dt / n
            for _ in range(n):
                t, x, v = st["t"], st["x"], st["v"]
                def acc(tt, xx, vv): return F0 * math.cos(2 * math.pi * st["f"] * tt) - w0 ** 2 * xx - 2 * gamma * vv
                k1x, k1v = v, acc(t, x, v)
                k2x, k2v = v + 0.5 * h * k1v, acc(t + 0.5 * h, x + 0.5 * h * k1x, v + 0.5 * h * k1v)
                k3x, k3v = v + 0.5 * h * k2v, acc(t + 0.5 * h, x + 0.5 * h * k2x, v + 0.5 * h * k2v)
                k4x, k4v = v + h * k3v, acc(t + h, x + h * k3x, v + h * k3v)
                st["x"] = x + h * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
                st["v"] = v + h * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
                st["t"] = t + h
            st["E"] = 0.5 * st["v"] ** 2 + 0.5 * w0 ** 2 * st["x"] ** 2
            block.move_to([st["x"] * 18, y0, 0])   # scale for visibility (x is tiny in these units)
        block.add_updater(step)
        caption = Text("a block on a spring, pushed by a force\nthat swings back and forth", font_size=24, color=GREY, line_spacing=0.9).to_edge(DOWN, buff=0.3)
        self.add(wall, floor, spring, block, F_arrow, v_arrow, F_lab, v_lab, bar_bg, bar, bar_lab, caption)

        def say(txt, color=GREY):
            self.play(Transform(caption, Text(txt, font_size=24, color=color, line_spacing=0.9).to_edge(DOWN, buff=0.3)), run_time=0.6)

        st.update(f=1.0, run=True)
        say("pushed at the natural frequency: the force always points\nthe way the block is already moving, so energy only goes in", AMBER)
        self.wait(9)
        st.update(run=False, x=0.0, v=0.0, t=0.0, E=0.0); block.move_to([0, y0, 0]); self.wait(0.3)
        st.update(f=2.0, run=True)
        say("pushed at twice the natural frequency:\nhalf of every push fights the motion, and the energy never builds", GREY)
        self.wait(8)
        st["run"] = False
        self.wait(0.5)

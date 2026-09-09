"""Manim: the terminal p.d. sags as the load draws more current.
Left: a source (E in series with r) driving a variable load R.  Right: the V–I line.
A bar splits E into terminal p.d. (green) and lost volts (red) as R falls from 20 Ω to 1 Ω.
Render:  manim -qk internal-resistance-sag.py TerminalSag ; copy media/videos/.../TerminalSag.mp4 to
internal-resistance-sag.mp4 beside the card, then rm -rf media __pycache__."""
from manim import *

E, r = 6.0, 2.0
GREY = "#888888"

class TerminalSag(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("A real cell under load: V = ℰ − I r", font_size=34, color=GREY).to_edge(UP)
        self.add(title)
        # --- right: V–I axes
        ax = Axes(x_range=[0, 3.2, 1], y_range=[0, 7, 1], x_length=5.2, y_length=3.6,
                  axis_config={"color": GREY, "include_tip": False}).to_edge(RIGHT, buff=0.6).shift(DOWN*0.4)
        xl = ax.get_x_axis_label(Text("I / A", font_size=22, color=GREY), edge=DOWN, direction=DOWN, buff=0.2)
        yl = ax.get_y_axis_label(Text("V / V", font_size=22, color=GREY), edge=LEFT, direction=LEFT, buff=0.2)
        line = ax.plot(lambda i: E - r*i, x_range=[0, E/r], color=BLUE)
        self.add(ax, xl, yl, line)
        # --- left: bar of E split into V (green) and Ir (red)
        R = ValueTracker(20.0)
        def I(): return E/(R.get_value()+r)
        def V(): return E - I()*r
        bar_x = -5.2; scale = 0.5
        v_bar = always_redraw(lambda: Rectangle(width=0.9, height=max(V()*scale, 0.01), fill_color=GREEN, fill_opacity=0.8, stroke_width=0).move_to([bar_x, -2.6 + V()*scale/2, 0]))
        l_bar = always_redraw(lambda: Rectangle(width=0.9, height=max(I()*r*scale, 0.01), fill_color=RED, fill_opacity=0.8, stroke_width=0).move_to([bar_x, -2.6 + V()*scale + I()*r*scale/2, 0]))
        e_lab = Text("ℰ = 6 V", font_size=24, color=GREY).move_to([bar_x, -2.6 + E*scale + 0.35, 0])
        v_lab = always_redraw(lambda: Text(f"V = {V():.2f} V", font_size=24, color=GREEN).next_to(v_bar, RIGHT, buff=0.25))
        l_lab = always_redraw(lambda: Text(f"I r = {I()*r:.2f} V", font_size=24, color=RED).next_to(l_bar, RIGHT, buff=0.25))
        r_lab = always_redraw(lambda: Text(f"load R = {R.get_value():.1f} Ω     I = {I():.2f} A", font_size=26, color=GREY).move_to([-3.0, 1.9, 0]))
        cap = Text("r = 2 Ω inside the cell", font_size=22, color=GREY).move_to([-3.0, 1.35, 0])
        dot = always_redraw(lambda: Dot(ax.c2p(I(), V()), color=YELLOW, radius=0.09))
        self.add(v_bar, l_bar, e_lab, v_lab, l_lab, r_lab, cap, dot)
        self.wait(1)
        self.play(R.animate.set_value(6.0), run_time=4, rate_func=linear)
        self.wait(0.5)
        self.play(R.animate.set_value(2.0), run_time=3, rate_func=linear)
        note = Text("R = r: half the e.m.f. is lost inside the cell", font_size=24, color=GREY).move_to([-3.0, -3.3, 0])
        self.play(FadeIn(note)); self.wait(1.2)
        self.play(R.animate.set_value(0.3), run_time=3, rate_func=linear)
        note2 = Text("towards a short circuit: V → 0, the cell heats itself", font_size=24, color=GREY).move_to([-3.0, -3.3, 0])
        self.play(Transform(note, note2)); self.wait(2)

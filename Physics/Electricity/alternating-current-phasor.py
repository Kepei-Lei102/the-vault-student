"""Phasors: a rotating arrow whose shadow is the sine wave — then three of them add.

Scene 1: one arrow of length V0 turns at w; its vertical projection, traced against
time, is V0 sin(wt). Scene 2: in a series RLC circuit the current phasor is the
reference; V_R lies along it, V_L is 90 degrees ahead, V_C 90 degrees behind. Their
vector sum is the supply phasor V, and the angle between V and I is the phase phi.
The whole picture rotates together — only the relative angles matter.

Render:  manim -qk alternating-current-phasor.py Phasors
"""
from manim import *
import numpy as np
GREY_K = "#888888"; BLUE_K = "#2563eb"; PURPLE_K = "#7c3aed"; GREEN_K = "#059669"; RED_K = "#dc2626"; AMBER_K = "#f59e0b"; TEAL_K = "#0891b2"

class Phasors(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("A phasor is a rotating arrow; the voltage you measure is its shadow", font_size=28, color=GREY_K).to_edge(UP)
        self.add(title)
        # --- scene 1: one phasor and its projection
        O = LEFT*4.2 + DOWN*0.6; Rr = 1.6
        circ = Circle(radius=Rr, color=GREY_K, stroke_width=1.5).move_to(O)
        axes = Axes(x_range=[0, 4*PI, PI], y_range=[-2, 2, 1], x_length=6.0, y_length=3.2, axis_config={"color": GREY_K, "stroke_width": 1.5, "include_ticks": False}).move_to(RIGHT*1.9 + DOWN*0.6)
        xlab = Text("time", font_size=20, color=GREY_K).next_to(axes.x_axis, DOWN, buff=0.15)
        ylab = Text("V", font_size=20, color=GREY_K).next_to(axes.y_axis.get_top(), LEFT, buff=0.15)
        self.play(FadeIn(circ), FadeIn(axes), FadeIn(xlab), FadeIn(ylab))
        th = ValueTracker(0.0)
        arrow = always_redraw(lambda: Arrow(O, O + Rr*np.array([np.cos(th.get_value()), np.sin(th.get_value()), 0]), buff=0, color=BLUE_K, stroke_width=5, max_tip_length_to_length_ratio=0.15))
        dashed = always_redraw(lambda: DashedLine(O + Rr*np.array([np.cos(th.get_value()), np.sin(th.get_value()), 0]), axes.c2p(th.get_value(), Rr/1.6*1.0*np.sin(th.get_value())), color=GREY_K, stroke_width=1.2))
        trace = always_redraw(lambda: axes.plot(lambda x: np.sin(x), x_range=[0, max(th.get_value(), 1e-3)], color=BLUE_K, stroke_width=3))
        dot = always_redraw(lambda: Dot(axes.c2p(th.get_value(), np.sin(th.get_value())), color=BLUE_K, radius=0.07))
        lbl = Text("V = V0 sin(ωt)", font_size=24, color=BLUE_K).next_to(axes, UP, buff=0.1).shift(RIGHT*1.5)
        self.add(arrow, dashed, trace, dot); self.play(FadeIn(lbl))
        self.play(th.animate.set_value(4*PI), run_time=8, rate_func=linear)
        note = Text("the angle turns at ω = 2πf; one lap of the arrow is one cycle of the wave", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note)); self.wait(1.5)
        self.play(FadeOut(VGroup(circ, axes, xlab, ylab, lbl, note)), FadeOut(arrow), FadeOut(dashed), FadeOut(trace), FadeOut(dot))
        # --- scene 2: three phasors add
        t2 = Text("In a series circuit the current is shared, so it is the reference arrow", font_size=28, color=GREY_K).to_edge(UP)
        self.play(Transform(title, t2))
        O2 = LEFT*2.0 + DOWN*0.2
        ph = ValueTracker(0.0)
        VR, VL, VC = 2.0, 2.1, 0.9
        def vec(mag, ang): return np.array([mag*np.cos(ang), mag*np.sin(ang), 0])
        I_arrow = always_redraw(lambda: Arrow(O2, O2 + vec(1.2, ph.get_value()), buff=0, color=GREY_K, stroke_width=4, max_tip_length_to_length_ratio=0.2))
        R_arrow = always_redraw(lambda: Arrow(O2, O2 + vec(VR, ph.get_value()), buff=0, color=AMBER_K, stroke_width=5, max_tip_length_to_length_ratio=0.12))
        L_arrow = always_redraw(lambda: Arrow(O2 + vec(VR, ph.get_value()), O2 + vec(VR, ph.get_value()) + vec(VL, ph.get_value()+PI/2), buff=0, color=PURPLE_K, stroke_width=5, max_tip_length_to_length_ratio=0.12))
        C_arrow = always_redraw(lambda: Arrow(O2 + vec(VR, ph.get_value()) + vec(VL, ph.get_value()+PI/2), O2 + vec(VR, ph.get_value()) + vec(VL, ph.get_value()+PI/2) + vec(VC, ph.get_value()-PI/2), buff=0, color=TEAL_K, stroke_width=5, max_tip_length_to_length_ratio=0.15))
        def tip(): return O2 + vec(VR, ph.get_value()) + vec(VL-VC, ph.get_value()+PI/2)
        V_arrow = always_redraw(lambda: Arrow(O2, tip(), buff=0, color=GREEN_K, stroke_width=6, max_tip_length_to_length_ratio=0.1))
        lI = Text("I — the current, shared by all three", font_size=22, color=GREY_K); lR = Text("VR = IR, in step with I", font_size=22, color=AMBER_K); lL = Text("VL = IωL, a quarter turn ahead", font_size=22, color=PURPLE_K); lC = Text("VC = I/ωC, a quarter turn behind", font_size=22, color=TEAL_K); lV = Text("V = the vector sum", font_size=22, color=GREEN_K)
        legend = VGroup(lI, lR, lL, lC, lV).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.3).shift(UP*1.2)
        self.play(FadeIn(I_arrow), FadeIn(lI)); self.wait(0.5)
        self.play(FadeIn(R_arrow), FadeIn(lR)); self.wait(0.8)
        self.play(FadeIn(L_arrow), FadeIn(lL)); self.wait(0.8)
        self.play(FadeIn(C_arrow), FadeIn(lC)); self.wait(0.8)
        self.play(FadeIn(V_arrow), FadeIn(lV)); self.wait(0.5)
        phi = np.arctan2(VL-VC, VR)
        angle = always_redraw(lambda: Angle(Line(O2, O2 + vec(1, ph.get_value())), Line(O2, O2 + vec(1, ph.get_value()+phi)), radius=0.7, color=GREEN_K, stroke_width=2))
        philab = always_redraw(lambda: Text("φ", font_size=24, color=GREEN_K).move_to(O2 + vec(1.0, ph.get_value()+phi/2)))
        self.play(FadeIn(angle), FadeIn(philab))
        n2 = VGroup(Text("|V| = I √(R² + (ωL − 1/ωC)²)      tan φ = (ωL − 1/ωC) / R", font_size=22, color=GREY_K), Text("Pythagoras, read straight off the picture", font_size=20, color=GREY_K)).arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(n2)); self.wait(1.0)
        self.play(ph.animate.set_value(2*PI), run_time=6, rate_func=linear)
        n3 = Text("everything turns together: only the angles between the arrows mean anything", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.5)
        self.play(Transform(n2, n3)); self.wait(2.5)

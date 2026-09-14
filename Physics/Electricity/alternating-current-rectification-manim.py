"""Rectification, animated: one diode, then four, then the capacitor.

Scene 1  half-wave: a diode in series with the load; the output is traced beside the
         input, and the diode lights when it conducts.
Scene 2  the bridge: the conducting pair changes every half-cycle, a dot rides the
         current path, and it goes through the load the same way both times.
Scene 3  smoothing: a capacitor across the load; the output is traced with the RC
         decays, then RC is raised and the ripple shrinks.

Render:  manim -qk alternating-current-rectification-manim.py Rectification
"""
from manim import *
import numpy as np
GREY_K = "#888888"; BLUE_K = "#2563eb"; PURPLE_K = "#7c3aed"; GREEN_K = "#059669"; RED_K = "#dc2626"; AMBER_K = "#f59e0b"

def smooth(t, src, tau):
    v = np.zeros_like(t); v[0] = src[0]; dt = t[1]-t[0]
    for i in range(1, len(t)):
        v[i] = max(v[i-1]*np.exp(-dt/tau), src[i])
    return v

def source(c):
    g = VGroup(Circle(radius=0.32, color=GREY_K, stroke_width=2).move_to(c))
    g.add(FunctionGraph(lambda x: 0.12*np.sin(4*PI*x), x_range=[-0.2, 0.2], color=GREY_K, stroke_width=2).move_to(c))
    return g

def diode(p, q, color=GREY_K, w=2):
    p, q = np.array(p), np.array(q); m = (p+q)/2; u = (q-p)/np.linalg.norm(q-p); n = np.array([-u[1], u[0], 0])
    tri = Polygon(m+0.18*u, m-0.14*u+0.16*n, m-0.14*u-0.16*n, color=color, fill_color=color, fill_opacity=1, stroke_width=w)
    bar = Line(m+0.18*u+0.16*n, m+0.18*u-0.16*n, color=color, stroke_width=w+1)
    return VGroup(Line(p, q, color=color, stroke_width=w), tri, bar)

def resistor(p, q, color=GREY_K):
    p, q = np.array(p), np.array(q); m = (p+q)/2; L = np.linalg.norm(q-p); u = (q-p)/L
    ang = np.arctan2(u[1], u[0])
    return VGroup(Line(p, q, color=color, stroke_width=2), Rectangle(width=0.5, height=0.22, color=color, fill_color="#1e1e1e", fill_opacity=1, stroke_width=2).rotate(ang).move_to(m))

def capacitor(p, q, color=GREY_K):
    p, q = np.array(p), np.array(q); m = (p+q)/2; u = (q-p)/np.linalg.norm(q-p); n = np.array([-u[1], u[0], 0])
    return VGroup(Line(p, m-0.08*u, color=color, stroke_width=2), Line(m+0.08*u, q, color=color, stroke_width=2),
                  Line(m-0.08*u+0.25*n, m-0.08*u-0.25*n, color=color, stroke_width=3), Line(m+0.08*u+0.25*n, m+0.08*u-0.25*n, color=color, stroke_width=3))

class Rectification(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Rectification: one diode, then four, then a capacitor", font_size=28, color=GREY_K).to_edge(UP)
        self.add(title)
        axes = Axes(x_range=[0, 3, 1], y_range=[-1.2, 1.2, 1], x_length=6.4, y_length=3.0,
                    axis_config={"color": GREY_K, "stroke_width": 1.5, "include_ticks": False}).move_to(RIGHT*3.0 + DOWN*0.3)
        xl = Text("time / periods", font_size=18, color=GREY_K).next_to(axes.x_axis, DOWN, buff=0.1).shift(RIGHT*2.2)
        yl = Text("V", font_size=18, color=GREY_K).next_to(axes.y_axis.get_top(), LEFT, buff=0.1)
        self.add(axes, xl, yl)
        t = ValueTracker(0.0)
        vin = lambda x: np.sin(2*PI*x)
        def trace(fn, color, dashed=False):
            return always_redraw(lambda: axes.plot(fn, x_range=[0, max(t.get_value(), 1e-3)], color=color, stroke_width=3 if not dashed else 1.5))
        # ---------- scene 1: half-wave
        A = LEFT*6.0 + UP*0.9; B = LEFT*2.4 + UP*0.9; C = LEFT*2.4 + DOWN*1.5; D = LEFT*6.0 + DOWN*1.5
        src = source((A+D)/2); wires = VGroup(Line(A, (A+D)/2+UP*0.32, color=GREY_K, stroke_width=2), Line((A+D)/2+DOWN*0.32, D, color=GREY_K, stroke_width=2), Line(D, C, color=GREY_K, stroke_width=2), Line(A, A+RIGHT*1.0, color=GREY_K, stroke_width=2), Line(A+RIGHT*2.2, B, color=GREY_K, stroke_width=2))
        d1 = always_redraw(lambda: diode(A+RIGHT*1.0, A+RIGHT*2.2, color=GREEN_K if vin(t.get_value()) > 0 else GREY_K, w=3 if vin(t.get_value()) > 0 else 2))
        rl = resistor(B, C); rlab = Text("R", font_size=20, color=GREY_K).next_to(rl, RIGHT, buff=0.1)
        state = always_redraw(lambda: Text("diode ON" if vin(t.get_value()) > 0 else "diode OFF", font_size=20, color=GREEN_K if vin(t.get_value()) > 0 else RED_K).move_to(A+RIGHT*1.6+UP*0.45))
        self.play(FadeIn(src), FadeIn(wires), FadeIn(rl), FadeIn(rlab), FadeIn(d1), FadeIn(state))
        cap = Text("half-wave: the diode passes the positive halves and blocks the rest", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(cap))
        tin = trace(vin, GREY_K, dashed=True); tout = trace(lambda x: max(vin(x), 0.0), BLUE_K)
        self.add(tin, tout)
        self.play(t.animate.set_value(3.0), run_time=7, rate_func=linear); self.wait(0.8)
        self.play(FadeOut(VGroup(src, wires, rl, rlab, cap)), FadeOut(d1), FadeOut(state), FadeOut(tin), FadeOut(tout)); t.set_value(0.0)
        # ---------- scene 2: the bridge (load inside the diamond)
        Tn = LEFT*3.6 + UP*1.0; Bn = LEFT*3.6 + DOWN*1.6; Ln = LEFT*5.0 + DOWN*0.3; Rn = LEFT*2.2 + DOWN*0.3
        S = LEFT*6.3 + DOWN*0.3
        src2 = source(S)
        sw = VGroup(Line(S+RIGHT*0.32, Ln, color=GREY_K, stroke_width=2),
                    Line(S+DOWN*0.32, S+DOWN*1.9, color=GREY_K, stroke_width=2), Line(S+DOWN*1.9, Rn+DOWN*1.9+RIGHT*0, color=GREY_K, stroke_width=2).put_start_and_end_on(S+DOWN*1.9, np.array([Rn[0], S[1]-1.9, 0])), Line(np.array([Rn[0], S[1]-1.9, 0]), Rn, color=GREY_K, stroke_width=2))
        pos = lambda: vin(t.get_value()) > 0
        # diodes all point toward Tn: L->T, B->L? no: B->L and B->R point away from B; L->T and R->T point toward T
        def dio(): 
            on1 = pos(); on2 = not pos()
            return VGroup(diode(Ln, Tn, GREEN_K if on1 else GREY_K, 3 if on1 else 2), diode(Bn, Rn, GREEN_K if on1 else GREY_K, 3 if on1 else 2),
                          diode(Rn, Tn, GREEN_K if on2 else GREY_K, 3 if on2 else 2), diode(Bn, Ln, GREEN_K if on2 else GREY_K, 3 if on2 else 2))
        dg = always_redraw(dio)
        load = resistor(Tn, Bn); llab = Text("R", font_size=20, color=GREY_K).next_to(load, RIGHT, buff=0.08)
        plus = Text("+", font_size=22, color=RED_K).next_to(Tn, UP, buff=0.05); minus = Text("−", font_size=22, color=BLUE_K).next_to(Bn, DOWN, buff=0.05)
        self.play(FadeIn(src2), FadeIn(sw), FadeIn(dg), FadeIn(load), FadeIn(llab), FadeIn(plus), FadeIn(minus))
        cap2 = Text("the bridge: two diodes conduct at a time; the load always gets top-to-bottom", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(cap2))
        # a dot riding the current path: positive half: S -> Ln -> Tn -> load -> Bn -> Rn -> back under; negative: reversed source side
        pathP = [S+RIGHT*0.32, Ln, Tn, Bn, Rn, np.array([Rn[0], S[1]-1.9, 0]), S+DOWN*1.9, S+DOWN*0.32]
        pathN = [S+DOWN*0.32, S+DOWN*1.9, np.array([Rn[0], S[1]-1.9, 0]), Rn, Tn, Bn, Ln, S+RIGHT*0.32]
        def dotpos():
            x = t.get_value(); frac = (x % 0.5)/0.5; pts = pathP if pos() else pathN
            segs = [np.linalg.norm(pts[i+1]-pts[i]) for i in range(len(pts)-1)]; tot = sum(segs); s = frac*tot
            for i, L in enumerate(segs):
                if s <= L: return pts[i] + (pts[i+1]-pts[i])*(s/L)
                s -= L
            return pts[-1]
        dot = always_redraw(lambda: Dot(dotpos(), color=AMBER_K, radius=0.09))
        self.add(dot)
        tin2 = trace(vin, GREY_K, dashed=True); tout2 = trace(lambda x: abs(vin(x)), PURPLE_K); self.add(tin2, tout2)
        self.play(t.animate.set_value(3.0), run_time=9, rate_func=linear); self.wait(0.8)
        self.remove(dot); self.play(FadeOut(tin2), FadeOut(tout2), FadeOut(cap2)); t.set_value(0.0)
        # ---------- scene 3: smoothing
        cx = Tn + RIGHT*0.55; cb = Bn + RIGHT*0.55
        capc = capacitor(cx + DOWN*0.0, cb, color=AMBER_K); capw = VGroup(Line(Tn, cx, color=AMBER_K, stroke_width=2), Line(Bn, cb, color=AMBER_K, stroke_width=2))
        clab = Text("C", font_size=20, color=AMBER_K).next_to(capc, RIGHT, buff=0.08)
        self.play(FadeIn(capc), FadeIn(capw), FadeIn(clab), llab.animate.next_to(load, LEFT, buff=0.08))
        cap3 = Text("a capacitor across the load: charged at each peak, discharged through R between them", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(cap3))
        tt = np.linspace(0, 3, 3001); full = np.abs(np.sin(2*PI*tt)); v09 = smooth(tt, full, 0.9); v5 = smooth(tt, full, 5.0)
        f09 = lambda x: float(np.interp(x, tt, v09)); f5 = lambda x: float(np.interp(x, tt, v5))
        tin3 = trace(lambda x: abs(vin(x)), GREY_K, dashed=True); tout3 = trace(f09, RED_K); self.add(tin3, tout3)
        self.play(t.animate.set_value(3.0), run_time=7, rate_func=linear)
        rip = Text("RC = 0.9 T: ripple 33% of the peak", font_size=20, color=RED_K).move_to(axes.c2p(1.5, -0.7)); self.play(FadeIn(rip)); self.wait(1.0)
        t2 = ValueTracker(0.0)
        tout5 = always_redraw(lambda: axes.plot(f5, x_range=[0, max(t2.get_value(), 1e-3)], color=GREEN_K, stroke_width=3)); self.add(tout5)
        cap4 = Text("raise RC (bigger C, or a lighter load — bigger R): the discharge slows, the ripple shrinks", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap3, cap4)); self.play(t2.animate.set_value(3.0), run_time=5, rate_func=linear)
        rip2 = Text("RC = 5 T: ripple 9%", font_size=20, color=GREEN_K).move_to(axes.c2p(1.5, -1.0)); self.play(FadeIn(rip2)); self.wait(2.5)

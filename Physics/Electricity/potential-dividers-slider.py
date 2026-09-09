"""Manim: the potential divider as a slider on a wire, then as a sensor.
Scene 1 — a 12 V supply across a uniform wire AB; the slider's tap voltage V = 12·x/L follows the slider;
          a lamp across the tap brightens and dims. Scene 2 — replace the top resistor with a thermistor: as it
          cools its resistance rises and V_out across the fixed resistor falls.
Render: manim -qk potential-dividers-slider.py Slider ; copy to potential-dividers-slider.mp4 ; rm -rf media __pycache__"""
from manim import *
GREY="#888888"; BLUE_K="#2563eb"; GREEN_K="#059669"; RED_K="#dc2626"; AMBER="#f59e0b"; PURPLE_K="#7c3aed"

class Slider(Scene):
    def construct(self):
        self.camera.background_color="#1e1e1e"
        title=Text("A potential divider: the voltage is shared in the ratio of the resistances", font_size=30, color=GREY).to_edge(UP); self.add(title)
        # wire AB
        A=np.array([-4,0.5,0]); B=np.array([4,0.5,0])
        wire=Line(A,B,color=GREY,stroke_width=8); la=Text("A",font_size=26,color=GREY).next_to(A,LEFT); lb=Text("B",font_size=26,color=GREY).next_to(B,RIGHT)
        # supply
        top=VGroup(Line(A,A+UP*1.5,color=GREY,stroke_width=3),Line(A+UP*1.5,B+UP*1.5,color=GREY,stroke_width=3),Line(B+UP*1.5,B,color=GREY,stroke_width=3))
        cell=VGroup(Line([-0.3,2.0,0],[-0.3,1.6,0],color=GREY,stroke_width=3),Line([0.3,2.3,0],[0.3,1.3,0],color=GREY,stroke_width=5)); cl=Text("12 V",font_size=24,color=GREY).next_to(cell,UP,buff=0.1)
        self.play(Create(wire),FadeIn(la),FadeIn(lb),Create(top),FadeIn(cell),FadeIn(cl))
        # slider
        x=ValueTracker(0.5)
        def slider_pos(): return A+(B-A)*x.get_value()
        arrow=always_redraw(lambda: Arrow(slider_pos()+DOWN*0.9,slider_pos()+DOWN*0.05,buff=0,color=AMBER,stroke_width=6,max_tip_length_to_length_ratio=0.35))
        def tap_parts():
            sp=slider_pos(); bot=sp+DOWN*1.6; left=A+DOWN*1.6; mid=(bot+left)/2
            return sp,bot,left,mid
        tapwire=always_redraw(lambda: VGroup(
            Line(tap_parts()[0]+DOWN*0.9,tap_parts()[1],color=AMBER,stroke_width=3),
            Line(tap_parts()[1],tap_parts()[3]+RIGHT*0.38,color=AMBER,stroke_width=3),
            Line(tap_parts()[3]+LEFT*0.38,tap_parts()[2],color=AMBER,stroke_width=3),
            Line(tap_parts()[2],A,color=AMBER,stroke_width=3)))
        # the voltmeter sits IN the tap loop: a circle with V, its fill tracking the reading
        lamp=always_redraw(lambda: VGroup(
            Circle(radius=0.38,color=AMBER,fill_color=AMBER,fill_opacity=0.08+0.5*x.get_value(),stroke_width=3).move_to(tap_parts()[3]),
            Text("V",font_size=30,color=AMBER).move_to(tap_parts()[3])))
        vtxt=always_redraw(lambda: Text(f"V = 12 V × {x.get_value():.2f} = {12*x.get_value():.1f} V",font_size=28,color=AMBER).move_to([0,-2.6,0]))
        bar=always_redraw(lambda: Rectangle(width=4*x.get_value()+0.01,height=0.3,color=AMBER,fill_color=AMBER,fill_opacity=0.6,stroke_width=0).move_to([-2+2*x.get_value(),-3.2,0]))
        barframe=Rectangle(width=4,height=0.3,color=GREY,stroke_width=1.5).move_to([0,-3.2,0])
        note=Text("the voltmeter from A to the slider reads 12 V × (tapped length ÷ whole length) — resistance is proportional to length",font_size=18,color=GREY).next_to(title,DOWN,buff=0.25)
        self.play(FadeIn(arrow),FadeIn(tapwire),FadeIn(lamp),FadeIn(vtxt),FadeIn(barframe),FadeIn(bar),FadeIn(note))
        self.play(x.animate.set_value(0.95),run_time=2.5); self.wait(0.4); self.play(x.animate.set_value(0.08),run_time=2.5); self.wait(0.4); self.play(x.animate.set_value(0.6),run_time=1.5); self.wait(1)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not title])
        # scene 2: thermistor divider
        t2=Text("Replace the top half by a thermistor and it becomes a sensor", font_size=28, color=GREY).next_to(title,DOWN,buff=0.25); self.play(FadeIn(t2))
        th=ValueTracker(20.0)   # temperature °C
        def Rth(): T=th.get_value()+273.15; return 1e4*np.exp(3950*(1/T-1/298.15))
        Rf=1e4
        left=Line([-2.6,1.3,0],[-2.6,-1.3,0],color=GREY,stroke_width=3); right=Line([2.6,1.3,0],[2.6,-1.3,0],color=GREY,stroke_width=3)
        topw=Line([-2.6,1.3,0],[2.6,1.3,0],color=GREY,stroke_width=3); botw=Line([-2.6,-1.3,0],[2.6,-1.3,0],color=GREY,stroke_width=3)
        cell2=VGroup(Line([-2.9,0.15,0],[-2.3,0.15,0],color=GREY,stroke_width=5),Line([-2.8,-0.15,0],[-2.4,-0.15,0],color=GREY,stroke_width=3)); c2=Text("5 V",font_size=22,color=GREY).next_to(cell2,LEFT,buff=0.15)
        therm=Rectangle(width=0.5,height=0.9,color=PURPLE_K,stroke_width=3).move_to([2.6,0.6,0]); tl=Text("thermistor",font_size=22,color=PURPLE_K).next_to(therm,RIGHT,buff=0.15)
        fixed=Rectangle(width=0.5,height=0.9,color=BLUE_K,stroke_width=3).move_to([2.6,-0.6,0]); fl=Text("10 kΩ",font_size=22,color=BLUE_K).next_to(fixed,RIGHT,buff=0.15)
        self.play(Create(left),Create(right),Create(topw),Create(botw),FadeIn(cell2),FadeIn(c2),FadeIn(therm),FadeIn(tl),FadeIn(fixed),FadeIn(fl))
        rtxt=always_redraw(lambda: Text(f"T = {th.get_value():5.1f} °C     R_thermistor = {Rth()/1e3:5.1f} kΩ",font_size=26,color=PURPLE_K).move_to([0,-2.0,0]))
        vout=always_redraw(lambda: Text(f"V_out across 10 kΩ = 5 V × 10 / (10 + {Rth()/1e3:.1f}) = {5*Rf/(Rf+Rth()):.2f} V",font_size=26,color=AMBER).move_to([0,-2.6,0]))
        self.play(FadeIn(rtxt),FadeIn(vout)); self.wait(0.6)
        self.play(th.animate.set_value(60),run_time=2.5); self.wait(0.5); self.play(th.animate.set_value(-10),run_time=3); self.wait(0.5)
        end=Text("warm: thermistor resistance falls, it takes a smaller share, V_out rises. A thermostat is this plus a switch.",font_size=20,color=GREY).to_edge(DOWN,buff=0.25); self.play(FadeIn(end)); self.wait(2.5)

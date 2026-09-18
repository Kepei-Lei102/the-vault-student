"""Three transport mechanisms; schematic motion, not a molecular-fluid simulation.
Render: manim -qk heat-transfer-animation.py HeatTransfer
"""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
BLUE='#2563eb'; RED='#dc2626'; AMBER='#f59e0b'; GREY='#bbbbbb'; GREEN='#059669'
class HeatTransfer(Scene):
    def txt(self,s,size=30,color=GREY):return Text(s,font='Helvetica',font_size=size,color=color)
    def clear(self):self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.6)
    def construct(self):
        title=self.txt('CONDUCTION: energy travels; the solid stays.',38).to_edge(UP)
        foot=self.txt('Atoms vibrate around fixed sites. Neighbours exchange energy.',25).to_edge(DOWN)
        self.play(FadeIn(title),FadeIn(foot))
        sites=np.linspace(-5,5,11);clock=ValueTracker(0)
        dots=VGroup()
        for i,x in enumerate(sites):
            d=Dot([x,0,0],radius=.15,color=BLUE)
            d.add_updater(lambda m,i=i,x=x: m.move_to([x,(.04+.14*np.clip((clock.get_value()-i*.5)/2,0,1))*np.sin(clock.get_value()*5+i),0]).set_color(interpolate_color(ManimColor(BLUE),ManimColor(RED),np.clip((clock.get_value()-i*.5)/2,0,1))))
            dots.add(d)
        circles=VGroup(*[Circle(radius=.3,color='#555555').move_to([x,0,0]) for x in sites])
        self.add(circles,dots);self.play(clock.animate.set_value(8),run_time=9,rate_func=linear)
        self.play(FadeIn(self.txt('No stream of atoms crosses the rod.',28,AMBER).shift(DOWN*1.7)));self.wait(3);self.clear()
        title=self.txt('CONVECTION: the fluid carries energy.',38).to_edge(UP)
        foot=self.txt('Heat below → lower density → buoyant rise → return flow.',25).to_edge(DOWN)
        loop=Ellipse(width=6,height=3.8,color='#888888')
        hot=self.txt('warming',25,RED).move_to(LEFT*4+DOWN*1.5)
        cool=self.txt('cooling',25,BLUE).move_to(RIGHT*4+UP*1.5)
        self.play(FadeIn(title),Create(loop),FadeIn(foot),FadeIn(hot),FadeIn(cool))
        t=ValueTracker(0)
        parcels=VGroup()
        # Clockwise: warm left side rises, cool right side sinks.
        for i in range(8):
            d=Dot(radius=.14)
            def update(m,i=i):
                a=2*np.pi*(i/8-t.get_value());m.move_to([3*np.cos(a),1.9*np.sin(a),0]);m.set_color(RED if np.cos(a)<0 else BLUE)
            d.add_updater(update);parcels.add(d)
        self.add(parcels);self.play(t.animate.set_value(1.5),run_time=10,rate_func=linear);self.wait(2);self.clear()
        title=self.txt('RADIATION: no material bridge is needed.',36).to_edge(UP)
        left=Rectangle(width=1,height=3,color=RED,fill_opacity=.25).shift(LEFT*4)
        right=Rectangle(width=1,height=3,color=BLUE,fill_opacity=.25).shift(RIGHT*4)
        foot=self.txt('Matched surfaces both emit; the hotter one emits more power.',24).to_edge(DOWN)
        self.play(FadeIn(title),FadeIn(left),FadeIn(right),FadeIn(foot),FadeIn(self.txt('vacuum',28).shift(UP*2)))
        for _ in range(3):
            packets=VGroup(*[Dot([-3.4,y,0],radius=.09,color=AMBER) for y in [-.7,0,.7]])
            back=Dot([3.4,1.2,0],radius=.09,color=BLUE)
            self.add(packets,back);self.play(packets.animate.shift(RIGHT*6.8),back.animate.shift(LEFT*6.8),run_time=2,rate_func=linear);self.remove(packets,back)
        self.wait(2);self.clear()
        title=self.txt('A vacuum flask blocks several routes.',38).to_edge(UP)
        lines=VGroup(self.txt('Vacuum gap: stops bulk convection; greatly reduces conduction.',25),self.txt('Reflective walls: reduce radiative transfer across the gap.',25),self.txt('Insulating stopper: limits heat flow through the opening.',25)).arrange(DOWN,buff=.65)
        self.play(FadeIn(title));self.play(LaggedStart(*[FadeIn(l,shift=UP*.1) for l in lines],lag_ratio=.8),run_time=4)
        self.play(FadeIn(self.txt('Insulation slows energy transfer. It does not create warmth.',26,GREEN).to_edge(DOWN)));self.wait(6)

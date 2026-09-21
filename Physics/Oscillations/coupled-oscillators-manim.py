"""Stack: Manim CE. Exact linear dynamics; small-angle pendulum drawing.
Render: manim -qk coupled-oscillators-manim.py CoupledOscillators
Adjacent model module supplies all motion and exact energy accounting.
"""
from manim import *
from pathlib import Path
import importlib.util
import numpy as np
s=importlib.util.spec_from_file_location('coupled_model',Path(__file__).with_name('coupled-oscillators-model.py'))
model=importlib.util.module_from_spec(s);s.loader.exec_module(model)
BG='#1e1e1e';TXT='#cccccc';GREY='#888888';BLUE='#2563eb';TEAL='#0891b2';PURPLE='#7c3aed';AMBER='#f59e0b'
config.background_color=BG

def line_text(text,y,size=27):
    return Text(text,font_size=size,color=TXT).move_to([0,y,0])

class CoupledOscillators(Scene):
    def construct(self):
        self.show_mode('plus','1. Move together',r'\omega_+=2.0\ \mathrm{rad\,s^{-1}}','The spring keeps its length. It adds no restoring force.',12)
        self.show_mode('minus','2. Move opposite ways',r'\omega_-=2.2\ \mathrm{rad\,s^{-1}}','The spring stretches and compresses. This mode is faster.',12)
        self.show_mode('mixed','3. Release only the left pendulum',r'x_1=q_++q_-,\qquad x_2=q_+-q_-','Both modes keep their amplitudes. Their sum trades the visible motion.',2*model.SWAP)
        self.play(FadeIn(line_text('Coupling transfers energy. Damping would remove it.',0,33)),run_time=.6)
        self.wait(4)

    def show_mode(self,mode,title,formula,caption,duration):
        clock=ValueTracker(0)
        heading=line_text(title,3.5,35)
        eq=MathTex(formula,color=TXT,font_size=32).move_to([0,2.85,0])
        cap=line_text(caption,-3.45,23)
        # Draw the small-angle pendulum geometry, rather than integrate a nonlinear pendulum.
        # g/L = 4 s^-2, horizontal coupling at the bobs. Displacement is scaled uniformly.
        L=2.6;scale=L/(9.81/model.K)
        def pos(i):
            x=float(model.state(clock.get_value(),mode)[i])*scale
            return np.array([(-2 if i==0 else 2)+x,1.8-np.sqrt(L*L-x*x),0])
        group=VGroup()
        group.add(Line([-3.2,1.8,0],[3.2,1.8,0],color=GREY))
        for i,col in enumerate([BLUE,TEAL]):
            pivot=np.array([-2 if i==0 else 2,1.8,0])
            group.add(DashedLine(pivot,pivot+DOWN*L,color=GREY,stroke_opacity=.4))
            group.add(always_redraw(lambda i=i,pivot=pivot:Line(pivot,pos(i),color=GREY)))
            group.add(always_redraw(lambda i=i,col=col:Dot(pos(i),radius=.15,color=col)))
            group.add(Text(str(i+1),font_size=24,color=col).move_to(pivot+DOWN*.24+LEFT*.30))
        def spring():
            a,b=pos(0),pos(1);vec=b-a;unit=vec/np.linalg.norm(vec);norm=np.array([-unit[1],unit[0],0])
            pts=[]
            for j,f in enumerate(np.linspace(0,1,41)):
                off=0 if j<2 or j>38 else .055*(-1)**j
                pts.append(a+f*vec+off*norm)
            return VMobject(color=PURPLE,stroke_width=2).set_points_as_corners(pts)
        group.add(always_redraw(spring))
        note=line_text('Identical pendulums · small angles · no damping',2.25,19)
        self.play(FadeIn(VGroup(heading,eq,cap,group,note)),run_time=.7)
        self.wait(1)
        if mode=='mixed':
            E0=sum(model.energies(0,mode))
            bar_group=VGroup()
            labels=['Left pendulum','Right pendulum','Coupling spring']
            colors=[BLUE,TEAL,PURPLE]
            for i,(label,col) in enumerate(zip(labels,colors)):
                y=-1.6-i*.43
                bar_group.add(Text(label,font_size=19,color=TXT).move_to([-4.6,y,0]))
                bar_group.add(Rectangle(width=5,height=.19,color=GREY,stroke_width=1).move_to([.25,y,0]))
                def bar(i=i,y=y,col=col):
                    width=max(.0001,5*float(model.energies(clock.get_value(),mode)[i])/E0)
                    return Rectangle(width=width,height=.18,color=col,fill_opacity=1,stroke_width=0).move_to([-2.25+width/2,y,0])
                bar_group.add(always_redraw(bar))
            bar_group.add(Text('Energy stores / constant total',font_size=20,color=TXT).move_to([.3,-1.17,0]))
            num=DecimalNumber(0,num_decimal_places=1,font_size=24,color=TXT)
            num.add_updater(lambda n:n.set_value(clock.get_value()).move_to([4.1,-1.62,0]))
            bar_group.add(Text('Time / s',font_size=19,color=TXT).move_to([4.1,-1.15,0]),num)
            bar_group.add(Text('Total = 0.3536 J',font_size=20,color=AMBER).move_to([4.1,-2.28,0]))
            self.play(FadeIn(bar_group),run_time=.5)
        else:
            self.play(FadeIn(line_text('One mode: one frequency, a fixed displacement ratio.',-1.85,25)),run_time=.5)
        self.play(clock.animate.set_value(duration),run_time=duration,rate_func=linear)
        self.wait(2)
        # Freeze updates before fading the whole scene.
        for mob in self.mobjects:mob.clear_updaters(recursive=True)
        self.play(*[FadeOut(mob) for mob in list(self.mobjects)],run_time=.7)

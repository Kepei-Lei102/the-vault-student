"""Stack: Manim CE; exact model in quantum-states-model.py.
Render with manim -qk --media_dir /tmp/quantum-states/media quantum-states-manim.py QuantumStates
The wall-size sequence compares preparations; it is not a moving-wall simulation.
"""
from manim import *
from pathlib import Path
import importlib.util
import numpy as np
s=importlib.util.spec_from_file_location('qm',Path(__file__).with_name('quantum-states-model.py'));qm=importlib.util.module_from_spec(s);s.loader.exec_module(qm)
config.background_color='#1e1e1e'
TXT='#cccccc';G='#888888';B='#2563eb';P='#7c3aed';T='#0891b2';A='#f59e0b';GREEN='#059669'
def txt(s,y,size=26):return Text(s,color=TXT,font_size=size).move_to([0,y,0])
def axes(center,ymax=3.5,ymin=0):
 a=Axes(x_range=[0,1,.5],y_range=[ymin,ymax,1],x_length=5.3,y_length=2.65,tips=False,axis_config={'color':G,'stroke_width':1.3,'include_ticks':True}).move_to(center)
 return a

def curve(ax,fn,color):
 x=np.linspace(0,1,181)
 return VMobject(color=color,stroke_width=3).set_points_as_corners([ax.c2p(v,float(fn(v))) for v in x])
def ticks(ax):
 return VGroup(*[Text(str(v),color=G,font_size=17).next_to(ax.c2p(v,0),DOWN,buff=.13) for v in [0,.5,1]])
class QuantumStates(Scene):
 def clear_scene(self):
  for m in self.mobjects:m.clear_updaters(recursive=True)
  self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.6)
 def construct(self):
  self.stationary();self.coherence();self.confinement()
 def stationary(self):
  clock=ValueTracker(0);left=axes([-3.3,.15,0],1.7,-1.7);right=axes([3.3,.15,0],2.4,0)
  group=VGroup(txt('1. A stationary state still has a changing phase',3.5,33),MathTex(r'\psi_1(x,t)=\phi_1(x)e^{-iE_1t/\hbar}',color=TXT,font_size=35).move_to([0,2.7,0]),left,right,ticks(left),ticks(right))
  group.add(Text('Real (blue) and imaginary (purple)',font_size=22,color=TXT).move_to([-3.3,1.96,0]),Text('Probability density',font_size=24,color=TXT).move_to([3.3,1.96,0]))
  group.add(always_redraw(lambda:curve(left,lambda x:qm.psi(x,clock.get_value(),(1,)).real,B)),always_redraw(lambda:curve(left,lambda x:qm.psi(x,clock.get_value(),(1,)).imag,P)),curve(right,lambda x:qm.density(x,0,'stationary'),GREEN))
  group.add(txt('Horizontal axis: x/L    •    amplitudes × √L; density × L',-1.8,20),txt('The complex components change. Their squared modulus does not.',-2.5,25),txt('Stationary means a fixed probability distribution, not a particle at rest.',-3.2,23))
  self.play(FadeIn(group),run_time=.8);self.wait(3);self.play(clock.animate.set_value(2*np.pi),run_time=12,rate_func=linear);self.wait(3);self.clear_scene()
 def coherence(self):
  clock=ValueTracker(0);left=axes([-3.3,.4,0],3.5);right=axes([3.3,.4,0],3.5)
  group=VGroup(txt('2. Same energy probabilities. Different position probabilities.',3.5,30),MathTex(r'\psi=(\phi_1e^{-iE_1t/\hbar}+\phi_2e^{-iE_2t/\hbar})/\sqrt2',color=TXT,font_size=32).move_to([0,2.8,0]),left,right,ticks(left),ticks(right))
  group.add(Text('Coherent superposition',font_size=25,color=TXT).move_to([-3.3,2.15,0]),Text('50–50 statistical mixture',font_size=25,color=TXT).move_to([3.3,2.15,0]))
  group.add(always_redraw(lambda:curve(left,lambda x:qm.density(x,clock.get_value()),B)),curve(right,lambda x:qm.density(x,0,'mixture'),G))
  for ax in [left,right]:group.add(DashedLine(ax.c2p(.5,0),ax.c2p(.5,3.4),color=G,stroke_opacity=.6))
  for center,fn in [(-3.3,lambda:qm.left_probability(clock.get_value())),(3.3,lambda:.5)]:
   group.add(Text('P(left half)',font_size=22,color=TXT).move_to([center-.4,-1.55,0]))
   num=DecimalNumber(fn(),num_decimal_places=3,font_size=27,color=A).move_to([center+1.15,-1.55,0]);num.add_updater(lambda m,fn=fn:m.set_value(fn()));group.add(num)
  group.add(txt('Axes: position x/L; density scaled by L.',-1.98,18))
  group.add(txt('Both: P(E₁) = P(E₂) = 1/2.   Mean energy = 2.5 E₁.',-2.35,24),txt('Left: amplitudes interfere. Right: preparation probabilities are averaged.',-3.12,22))
  self.play(FadeIn(group),run_time=.8);self.wait(4);self.play(clock.animate.set_value(4*np.pi/3),run_time=18,rate_func=linear);self.wait(3);self.clear_scene()
 def confinement(self):
  width=ValueTracker(1);ax=Axes(x_range=[0,1.2,.2],y_range=[0,40,10],x_length=7,y_length=4.1,tips=False,axis_config={'color':G}).move_to([-1.8,-.1,0])
  group=VGroup(txt('3. Confinement sets an energy scale',3.5,35),txt('Compare separately prepared infinite wells — no moving-wall dynamics.',2.8,23),ax)
  group.add(Text('Energy / initial E₁',font_size=22,color=TXT).rotate(PI/2).move_to([-6.2,-.1,0]),Text('Position / initial width',font_size=22,color=TXT).move_to([-1.8,-2.65,0]))
  for val in [0,.5,1]:group.add(Text(str(val),font_size=17,color=G).next_to(ax.c2p(val,0),DOWN,buff=.12))
  for val in [0,10,20,30,40]:group.add(Text(str(val),font_size=17,color=G).next_to(ax.c2p(0,val),LEFT,buff=.12))
  group.add(always_redraw(lambda:Line(ax.c2p(width.get_value(),0),ax.c2p(width.get_value(),39),color=G)))
  for n,col in zip([1,2,3],[B,P,T]):
   group.add(always_redraw(lambda n=n,col=col:Line(ax.c2p(0,n*n/width.get_value()**2),ax.c2p(width.get_value(),n*n/width.get_value()**2),color=col,stroke_width=4)))
  group.add(MathTex(r'E_n=\frac{n^2h^2}{8mL^2}',color=TXT,font_size=38).move_to([4,1,0]),txt('Half the width → four times each energy gap.',-3.3,26))
  num=DecimalNumber(1,num_decimal_places=2,font_size=32,color=A).move_to([4,-.65,0]);num.add_updater(lambda m:m.set_value(width.get_value()));group.add(num,Text('Width / initial width',font_size=22,color=TXT).move_to([4,-1.4,0]))
  self.play(FadeIn(group),run_time=.8);self.wait(3);self.play(width.animate.set_value(.5),run_time=8,rate_func=smooth);self.wait(4);self.clear_scene()
  self.play(FadeIn(txt('From confined waves to quantum-dot colour',.8,34)),FadeIn(txt('Real dots also need band structure, carrier masses and interactions.',-.2,24)),run_time=.8);self.wait(4)

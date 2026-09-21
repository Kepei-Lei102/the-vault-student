"""Stack: Manim CE. Three scenes: evolved packet, width comparison, flash barrier.
Render: manim -qk --media_dir /tmp/tunnelling-media quantum-tunnelling-manim.py Tunnelling
Numerical source beside this file. Dimensionless hbar=m=1; no device calibration.
"""
from manim import *
from pathlib import Path
import importlib.util
import numpy as np
s=importlib.util.spec_from_file_location('qm',Path(__file__).with_name('quantum-tunnelling-model.py'));qm=importlib.util.module_from_spec(s);s.loader.exec_module(qm)
config.background_color='#1e1e1e'
Text.set_default(font='Arial')
TXT='#cccccc';G='#888888';B='#2563eb';P='#7c3aed';GREEN='#059669';A='#f59e0b'
def txt(s,y,size=27):return Text(s,color=TXT,font_size=size).move_to([0,y,0])
def lineplot(ax,x,y,color=B):return VMobject(color=color,stroke_width=3).set_points_as_corners([ax.c2p(float(a),float(b)) for a,b in zip(x,y)])
class Tunnelling(Scene):
 def reset(self):
  for m in self.mobjects:m.clear_updaters(recursive=True)
  self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.7)
 def construct(self):self.packet_scene();self.width_scene();self.flash_scene()
 def packet_scene(self):
  d=qm.packet();clock=ValueTracker(0)
  xs=np.linspace(-52,52,781)
  ax=Axes(x_range=[-52,52,20],y_range=[0,.26,.05],x_length=11.9,y_length=3.1,tips=False,axis_config={'color':G,'stroke_width':1.2}).move_to([0,.25,0])
  def interp(arr):
   z=clock.get_value()/.1;i=min(int(z),len(d['time'])-2);f=min(z-i,1.);return arr[i]*(1-f)+arr[i+1]*f
  def rho():return np.interp(xs,d['x'],interp(d['density']))
  curve=always_redraw(lambda:lineplot(ax,xs,rho(),B))
  shade=Polygon(ax.c2p(-.5,0),ax.c2p(.5,0),ax.c2p(.5,.26),ax.c2p(-.5,.26),color=P,fill_color=P,fill_opacity=.3,stroke_width=1)
  labels=VGroup(*[Text(str(x),color=G,font_size=18).next_to(ax.c2p(x,0),DOWN,buff=.12) for x in [-40,-20,0,20,40]])
  def readout():
   v=interp(d['probability'])
   return VGroup(*[Text(f'{name}: {val:.3f}',font_size=24,color=col) for name,val,col in zip(['Left','Inside','Right'],v,[B,P,GREEN])]).arrange(RIGHT,buff=.7).move_to([0,-2.25,0])
  numbers=always_redraw(readout)
  g=VGroup(txt('1. A wave packet meets a finite barrier',3.45,34),txt('Barrier height 3 • packet centred near energy 2 • width 1',2.72,24),ax,shade,labels,curve,numbers,txt('Position (model units)    |    vertical axis: probability density',-1.88,20),txt('Left + inside + right = 1 throughout',-2.85,25),txt('The curve is a probability distribution, not a particle trajectory.',-3.35,22))
  self.play(FadeIn(g),run_time=1);self.wait(3)
  self.play(clock.animate.set_value(30),run_time=25,rate_func=linear)
  end=txt('After separation: about 81% reflected, 19% transmitted',2.72,24)
  self.play(Transform(g[1],end),run_time=.6);self.wait(4);self.reset()
 def width_scene(self):
  a=ValueTracker(.5);E,V=1.,2.
  ax=Axes(x_range=[0,1.25,.25],y_range=[-5,0,1],x_length=8.7,y_length=3.3,tips=False,axis_config={'color':G,'stroke_width':1.2}).move_to([-.9,.25,0])
  xs=np.linspace(0,1.2,301);kap=5.123167
  y=np.log10(1/np.cosh(kap*xs)**2)
  dot=always_redraw(lambda:Dot(ax.c2p(a.get_value(),np.log10(1/np.cosh(kap*a.get_value())**2)),color=GREEN,radius=.09))
  labels=VGroup(*[Text(str(x),color=G,font_size=19).next_to(ax.c2p(x,-5),DOWN,buff=.12) for x in [0,.25,.5,.75,1.]])
  val=always_redraw(lambda:VGroup(Text(f'a = {a.get_value():.2f} nm',font_size=24,color=TXT),Text(f'T = {1/np.cosh(kap*a.get_value())**2:.6f}',font_size=24,color=GREEN)).arrange(DOWN,buff=.25).move_to([4.4,.6,0]))
  labels.add(*[Text(str(v),font_size=18,color=G).next_to(ax.c2p(0,v),LEFT,buff=.12) for v in [-4,-3,-2,-1,0]])
  g=VGroup(txt('2. Thickness is an exponential control knob',3.45,33),txt('Same incident energy: E = 1 eV; barrier height: 2 eV',2.72,25),ax,lineplot(ax,xs,y),dot,labels,val,txt('Barrier width a (nm)    |    vertical axis: log10(T)',-1.9,21),txt('Compare separate static barriers; no energy is borrowed.',-2.6,25),txt('CPU gate insulation: unwanted tunnelling consumes power.',-3.25,24))
  self.play(FadeIn(g),run_time=.8);self.wait(3);self.play(a.animate.set_value(1.),run_time=7,rate_func=linear);self.wait(4);self.reset()
 def flash_scene(self):
  ax=Axes(x_range=[-.5,3,.5],y_range=[-1,4,1],x_length=10.6,y_length=3.5,tips=False,axis_config={'color':G,'stroke_width':1.2,'include_ticks':False}).move_to([0,.1,0])
  pts=[-.5,0,0,1.5,1.5,3];write=[0,0,3,-.6,-.6,-.6];hold=[0,0,3,3,0,0]
  barrier=lineplot(ax,pts,write,P)
  energy=DashedLine(ax.c2p(-.5,.5),ax.c2p(3,.5),color=A,stroke_width=2)
  stage=txt('WRITE: a strong field tilts the energy barrier',2.7,27)
  area=Polygon(ax.c2p(0,.5),ax.c2p(0,3),ax.c2p(2.5/2.4,.5),fill_color=P,fill_opacity=.2,stroke_width=0)
  target=Polygon(ax.c2p(0,.5),ax.c2p(0,3),ax.c2p(1.5,3),ax.c2p(1.5,.5),fill_color=P,fill_opacity=.2,stroke_width=0)
  dot=Dot(ax.c2p(2.2,.5),color=GREEN)
  g=VGroup(txt('3. Flash changes the barrier between write and retain',3.45,30),stage,ax,barrier,energy,area,txt('Position →    |    vertical axis: electron potential energy',-1.98,21),txt('Schematic energy profile; not a full NAND device simulation.',-3.25,21))
  self.play(FadeIn(g),run_time=.8);self.wait(5)
  self.play(FadeIn(dot),run_time=.6);self.wait(1)
  self.play(Transform(stage,txt('RETAIN: remove the field; escape becomes much less likely',2.7,25)),Transform(barrier,lineplot(ax,pts,hold,P)),Transform(area,target),run_time=3)
  read=txt('READ: stored charge shifts the voltage needed to turn the cell on.',-2.6,24)
  self.play(FadeIn(read),run_time=.7);self.wait(7)

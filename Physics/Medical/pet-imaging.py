"""Render: manim -qk pet-imaging.py PETImaging. Requires adjacent pet-model.py."""
from manim import *
from pathlib import Path
import importlib.util
import numpy as np
spec=importlib.util.spec_from_file_location('petmodel',Path(__file__).with_name('pet-model.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
config.background_color='#1e1e1e'
TXT='#cccccc';DIM='#888888';BLUE='#2563eb';AMBER='#f59e0b';TEAL='#0891b2'
def txt(s,size=28):
 t=Text(s,font='Arial',font_size=size,color=TXT)
 if t.width>13:t.scale_to_fit_width(13)
 return t
def raster(a,maximum):
 v=np.clip(np.flipud(a)/maximum,0,1)
 rgb=np.stack([30+v*220,32+v*120,45+v*20],axis=-1).astype(np.uint8)
 return ImageMobject(rgb).set_resampling_algorithm(RESAMPLING_ALGORITHMS['nearest'])
class PETImaging(Scene):
 def clear(self):self.play(*[FadeOut(o) for o in list(self.mobjects)],run_time=.6)
 def construct(self):
  self.add(txt('PET: the tracer becomes the signal',38).to_edge(UP,buff=.4))
  for i,s in enumerate(['A radioactive label emits a positron.','The positron slows down in nearby tissue.','It meets an electron: annihilation.','Two gamma photons carry the energy away.']):
   self.play(FadeIn(txt(s,29).move_to([0,1.8-i*.95,0])),run_time=.5);self.wait(2)
  self.add(txt('The scanner detects the photons, not the positron.',27).to_edge(DOWN,buff=.5));self.wait(3);self.clear()
  self.add(txt('One detected pair defines a line',38).to_edge(UP,buff=.4))
  center=np.array([0.,0.,0.]);radius=2.55
  ring=Circle(radius=radius,color=BLUE,stroke_width=5)
  self.add(ring,txt('detector ring',22).move_to([4.2,2.2,0]))
  p=np.array([.7,.35,0]);left,right=m.chord(p[:2],np.array([1.,.32]))
  left=np.r_[left*1.7,0];right=np.r_[right*1.7,0];p=p*1.7
  dl=np.linalg.norm(p-left);dr=np.linalg.norm(right-p)
  self.add(Dot(p,color=AMBER),txt('annihilation',22).next_to(Dot(p),UP,buff=.2))
  flight=ValueTracker(0)
  g1=always_redraw(lambda:Dot(p+(left-p)*min(flight.get_value()/dl,1),radius=.08,color=AMBER))
  g2=always_redraw(lambda:Dot(p+(right-p)*min(flight.get_value()/dr,1),radius=.08,color=AMBER))
  self.add(g1,g2,txt('Same photon speed; the nearer detector is reached first.',25).to_edge(DOWN,buff=.35))
  self.wait(2);self.play(flight.animate.set_value(max(dl,dr)),run_time=5,rate_func=linear)
  g1.clear_updaters();g2.clear_updaters();self.play(Flash(left,color=AMBER),Flash(right,color=AMBER),run_time=.8)
  line=Line(left,right,color=TEAL,stroke_width=4);self.play(Create(line),run_time=1.2);self.wait(2)
  self.clear()
  self.add(txt('Many events reveal a distribution',38).to_edge(UP,buff=.4),Circle(radius=radius,color=BLUE,stroke_width=4))
  self.add(txt('Different events happen at different locations. No single common crossing.',24).to_edge(DOWN,buff=.35))
  for p,l,r in m.events(20):
   l=np.r_[l*1.7,0];r=np.r_[r*1.7,0]
   beam=Line(l,r,color=TEAL,stroke_width=2,stroke_opacity=.35)
   ends=VGroup(Dot(l,color=AMBER,radius=.06),Dot(r,color=AMBER,radius=.06))
   self.play(FadeIn(beam),FadeIn(ends),run_time=.25)
  self.wait(4);self.clear()
  A,truth,counts,result,snapshots,ll=m.experiment()
  maximum=truth.max()/truth.sum()
  self.add(txt('Fit a tracer map to measured pair counts',36).to_edge(UP,buff=.4))
  original=raster((truth/truth.sum()).reshape(16,16),maximum).set(height=3.7).move_to([-3.4,0,0]);self.add(original)
  self.add(txt('known synthetic source',24).move_to([-3.4,2.3,0]))
  self.add(txt('Same 29,749 noisy counts; same colour scale.',23).to_edge(DOWN,buff=.7),txt('Ideal grid model: no scatter, attenuation or motion.',21).to_edge(DOWN,buff=.3))
  current=None;cap=None
  for k in (1,5,20,80):
   a=snapshots[k];new=raster((a/a.sum()).reshape(16,16),maximum).set(height=3.7).move_to([3.4,0,0]);newcap=txt(f'{k} reconstruction iteration'+('' if k==1 else 's'),24).move_to([3.4,2.3,0])
   if current:self.play(FadeOut(current),FadeOut(cap),FadeIn(new),FadeIn(newcap),run_time=.7)
   else:self.play(FadeIn(new),FadeIn(newcap),run_time=.7)
   current,cap=new,newcap;self.wait(3.5)
  self.clear()
  self.add(txt('Arrival-time difference narrows the line',36).to_edge(UP,buff=.4))
  line=Line([-5,0,0],[5,0,0],color=TEAL,stroke_width=4);self.add(line)
  self.add(txt('L',28).move_to([-5.5,0,0]),txt('R',28).move_to([5.5,0,0]),DashedLine([0,-.5,0],[0,.5,0],color=DIM))
  self.add(txt('midpoint',22).move_to([0,-.9,0]))
  band=Rectangle(width=2,height=.6,color=AMBER,fill_color=AMBER,fill_opacity=.2).move_to([1,0,0]);self.play(FadeIn(band),run_time=1)
  self.add(txt('x = c(tL - tR) / 2',32).move_to([0,1.65,0]),txt('tL - tR = +200 ps  →  3.0 cm towards R',27).move_to([0,-1.65,0]),txt('400 ps timing FWHM  →  6.0 cm localization FWHM',26).move_to([0,-2.35,0]))
  self.add(txt('A probability band, not an exact point. Diagram not to scale.',23).to_edge(DOWN,buff=.35));self.wait(7)

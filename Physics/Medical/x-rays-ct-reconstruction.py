"""Manim: a measured projection is a constraint, then solve for the slice.
Render: manim -qk x-rays-ct-reconstruction.py CTReconstruction
Requires NumPy and the adjacent x-rays-ct-model.py; no patient data.
"""
from manim import *
import importlib.util
from pathlib import Path
import numpy as np
spec=importlib.util.spec_from_file_location('ctmodel',Path(__file__).with_name('x-rays-ct-model.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
config.background_color='#1e1e1e'
def text(s,size=28):
 t=Text(s,font='Arial',font_size=size,color='#cccccc')
 if t.width>13:t.scale_to_fit_width(13)
 return t
def raster(values,maximum=.9):
 v=np.clip(np.flipud(values)/maximum,0,1)
 rgb=np.stack([40+v*150,45+v*170,60+v*170],axis=-1).astype(np.uint8)
 return ImageMobject(rgb).set_resampling_algorithm(RESAMPLING_ALGORITHMS['nearest'])
class CTReconstruction(Scene):
 def construct(self):
  truth,A,b,solutions=m.build()
  self.add(text('CT: turn shadows into constraints',36).to_edge(UP,buff=.35))
  self.add(text('Synthetic parallel beams; monochromatic, no scattering or noise.',21).to_edge(DOWN,buff=.3))
  obj=raster(truth).set(height=3.7).move_to([-3.2,0,0]);self.add(obj)
  self.add(text('fixed object',25).move_to([-3.2,2.3,0]))
  detector=Line([1.5,-1.9,0],[1.5,1.9,0],color=TEAL)
  self.add(text('one detector profile',25).move_to([3.3,2.3,0]))
  theta=ValueTracker(0)
  def rays():
   ang=theta.get_value();normal=np.array([np.cos(ang),np.sin(ang),0]);direction=np.array([-np.sin(ang),np.cos(ang),0]);center=np.array([-3.2,0,0])
   return VGroup(*[Line(center+normal*s-direction*2.7,center+normal*s+direction*2.7,color='#f59e0b',stroke_width=2).set_opacity(.5) for s in np.linspace(-1.5,1.5,9)])
  beam=always_redraw(rays)
  ax=Axes(x_range=[0,28,7],y_range=[0,1,1],x_length=4,y_length=2.5,axis_config={'color':'#888888'}).move_to([3.2,0,0])
  self.add(ax,text('detector channel',20).move_to([3.3,-1.8,0]),text('transmitted fraction I / I0',21).move_to([3.2,1.65,0]))
  def curve():
   vals=np.exp(-np.stack([m.ray(theta.get_value(),s) for s in m.DETECTORS])@truth.ravel())
   return VMobject(color='#059669').set_points_as_corners([ax.c2p(i,v) for i,v in enumerate(vals)])
  profile=always_redraw(curve);self.add(beam,profile);self.wait(3)
  self.play(theta.animate.set_value(np.pi),run_time=12,rate_func=linear);self.wait(2)
  beam.clear_updaters();profile.clear_updaters()
  self.play(*[FadeOut(o) for o in list(self.mobjects)],run_time=.7)
  self.add(text('Take the logarithm: each ray becomes an equation',34).to_edge(UP,buff=.4))
  self.add(text('-ln(I / I0) = sum of (attenuation x path length)',30).move_to([0,2.2,0]))
  sino=raster(b.reshape(48,29).T,maximum=b.max()).set(width=5.5).move_to([-3.1,-.1,0])
  self.add(sino,text('48 angles: measured constraints',23).move_to([-3.1,-2.2,0]))
  self.add(text('Same scale in every reconstruction.',21).to_edge(DOWN,buff=.3))
  reconstruction=raster(solutions[2]).set(height=3.6).move_to([3.3,-.1,0])
  caption=text('2 angles: many answers fit',25).move_to([3.3,-2.2,0]);self.add(reconstruction,caption);self.wait(4)
  for count,words in [(4,'4 angles: fewer ambiguities'),(8,'8 angles: the structure becomes clearer'),(16,'16 angles: this tiny ideal grid is determined'),(48,'48 angles: the same recovered slice')]:
   new=raster(solutions[count]).set(height=3.6).move_to([3.3,-.1,0]);newcap=text(words,23).move_to([3.3,-2.2,0]);self.play(FadeOut(reconstruction),FadeIn(new),Transform(caption,newcap),run_time=1);reconstruction=new;self.wait(4)
  self.play(*[FadeOut(o) for o in list(self.mobjects)],run_time=.7)
  self.add(text('Repeat along the body: slices become a volume',34).to_edge(UP,buff=.4))
  for k in range(7):
   layer=Rectangle(width=4.4,height=2.2,color='#0891b2',fill_color='#0891b2',fill_opacity=.07).shift(RIGHT*(k-3)*.3+UP*(k-3)*.22)
   self.play(FadeIn(layer),run_time=.35)
  self.add(text('The cuts are mathematical. The object stays whole.',27).move_to([0,-2.3,0]));self.wait(5)

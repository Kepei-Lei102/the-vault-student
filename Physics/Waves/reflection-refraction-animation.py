"""Stack: Manim CE. Final: manim -qk --media_dir /tmp/refraction-media this.py Refraction.
Plane fronts obey phase continuity. Ray widths are NOT power fractions.
"""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
TXT='#cccccc';DIM='#888888';BLUE='#2563eb';GREEN='#059669';AMBER='#f59e0b';TEAL='#0891b2'
def txt(s,size=28):return Text(s,font='DejaVu Sans',font_size=size,color=TXT)
def point(x,y):return np.array([x,y,0.])
def clipped_front(nx,ny,c,xmin,xmax,ymin,ymax,color):
 pts=[]
 for x in [xmin,xmax]:
  y=(c-nx*x)/ny
  if ymin-1e-8<=y<=ymax+1e-8:pts.append(point(x,y))
 for y in [ymin,ymax]:
  if abs(nx)>1e-8:
   x=(c-ny*y)/nx
   if xmin-1e-8<=x<=xmax+1e-8:pts.append(point(x,y))
 if len(pts)<2 or np.linalg.norm(pts[0]-pts[-1])<.001:return VGroup()
 return Line(pts[0],pts[-1],color=color,stroke_width=3)
class Refraction(Scene):
 def caption(self,s):return txt(s,25).move_to(DOWN*3.25)
 def clear_scene(self):self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.7)
 def construct(self):
  title=txt('One side slows first. The wavefront turns.',36).to_edge(UP)
  boundary=Line(LEFT*6.1,RIGHT*6.1,color=DIM)
  water=Rectangle(width=12.2,height=2.65,stroke_width=0,fill_color=TEAL,fill_opacity=.12).move_to(DOWN*1.325)
  labels=VGroup(txt('air  n = 1.00',23).move_to(point(-4.7,2.2)),txt('glass  n = 1.50',23).move_to(point(-4.6,-2.2)))
  self.play(FadeIn(VGroup(title,boundary,water,labels)))
  t=ValueTracker(0);i=np.deg2rad(50);r=np.arcsin(np.sin(i)/1.5)
  def fronts():
   group=VGroup()
   for m in range(-13,14):
    phase=t.get_value()-m*.8
    group.add(clipped_front(np.sin(i),-np.cos(i),phase,-6,6,0,1.8,BLUE))
    group.add(clipped_front(np.sin(r),-np.cos(r),phase/1.5,-6,6,-1.8,0,GREEN))
   return group
  waves=always_redraw(fronts);self.add(waves)
  cap=self.caption('Blue and green lines are crests, not light paths.')
  self.play(FadeIn(cap));self.play(t.animate.set_value(3.2),run_time=8,rate_func=linear)
  self.play(FadeOut(cap));cap=self.caption('Same frequency. Lower speed. Shorter wavelength.');self.play(FadeIn(cap))
  self.play(t.animate.set_value(5.6),run_time=6,rate_func=linear)
  waves.clear_updaters()
  normal=DashedLine(DOWN*2,UP*2,color=DIM)
  rays=VGroup(Arrow(point(-2*np.sin(i),2*np.cos(i)),ORIGIN,buff=0,color=AMBER),Arrow(ORIGIN,point(2*np.sin(r),-2*np.cos(r)),buff=0,color=AMBER))
  self.play(FadeIn(normal),FadeIn(rays));self.wait(3)
  self.clear_scene()
  # Reverse direction: glass to air, including partial reflection below critical.
  title=txt('Turn the ray: refraction reaches its limit',36).to_edge(UP)
  labels=VGroup(txt('air  n = 1.00',23).move_to(point(-4.8,2.1)),txt('glass  n = 1.50',23).move_to(point(-4.6,-2.1)))
  self.play(FadeIn(VGroup(title,boundary.copy(),water.copy(),labels,normal.copy())))
  angle=ValueTracker(20);crit=np.rad2deg(np.arcsin(1/1.5))
  def bounded_bundle():
   a=np.deg2rad(angle.get_value());d=point(np.sin(a),np.cos(a));g=VGroup(Arrow(-2.8*d,ORIGIN,buff=0,color=BLUE),Arrow(ORIGIN,point(2.8*np.sin(a),-2.8*np.cos(a)),buff=0,color=AMBER))
   s=1.5*np.sin(a)
   if s<=1+1e-10:
    b=np.arcsin(min(1,s));length=min(4,2.25/max(np.cos(b),.001));g.add(Arrow(ORIGIN,point(length*np.sin(b),length*np.cos(b)),buff=0,color=GREEN))
   return g
  rays=always_redraw(bounded_bundle);self.add(rays)
  number=DecimalNumber(20,num_decimal_places=1,font_size=28,color=TXT).move_to(point(4.8,-1.7))
  number.add_updater(lambda m:m.set_value(angle.get_value()))
  self.add(number,txt('incidence / degrees',20).move_to(point(4.6,-2.2)))
  cap=self.caption('Below critical: reflected AND transmitted rays.');self.play(FadeIn(cap));self.wait(2)
  self.play(angle.animate.set_value(crit),run_time=8,rate_func=linear)
  self.play(FadeOut(cap));cap=self.caption('Critical angle = 41.81°: the limiting ray grazes the surface.');self.play(FadeIn(cap));self.wait(4)
  self.play(FadeOut(cap));cap=self.caption('Increase beyond critical: no travelling transmitted ray.');self.play(FadeIn(cap))
  self.play(angle.animate.set_value(62),run_time=6,rate_func=linear);self.wait(3)
  rays.clear_updaters();number.clear_updaters();self.clear_scene()
  title=txt('A fibre guides light by repeated total reflection',35).to_edge(UP)
  core=Rectangle(width=11,height=2,stroke_color=TEAL,fill_color=TEAL,fill_opacity=.12)
  labels=VGroup(txt('lower-index cladding',23).move_to(UP*1.45),txt('higher-index core',23).move_to(DOWN*1.6))
  self.play(FadeIn(VGroup(title,core,labels)))
  coords=[point(-5,0),point(-3,1),point(1,-1),point(5,1)]
  path=VMobject().set_points_as_corners(coords).set_stroke(AMBER,3)
  self.play(Create(path),run_time=3)
  pulse=Dot(coords[0],color=GREEN,radius=.10);self.add(pulse)
  cap=self.caption('Guidance is not losslessness: real fibres attenuate.');self.play(FadeIn(cap))
  self.play(MoveAlongPath(pulse,path),run_time=5,rate_func=linear);self.wait(3)

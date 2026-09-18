"""Stack: Manim CE. Render: manim -qk --media_dir /tmp/lenses-manim lenses-animation.py Lenses
Coordinates obey thin paraxial ray mapping. Dashed paths are backward extensions.
"""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
D='#888888';C='#cccccc';B='#2563eb';G='#059669';A='#f59e0b';T='#0891b2'
def p(x,y):return np.array([x,y,0.])
def text(s,size=28):return Text(s,font='DejaVu Sans',font_size=size,color=C)
def segment(x1,y1,x2,y2,color,dashed=False):
 # Clip to central illustration rectangle, protecting title and caption.
 lo=0.;hi=1.;dx=x2-x1;dy=y2-y1
 for origin,delta,mn,mx in [(x1,dx,-6,6),(y1,dy,-2.1,2.1)]:
  if abs(delta)<1e-10:
   if not mn<=origin<=mx:return VGroup()
  else:
   aa,bb=sorted(((mn-origin)/delta,(mx-origin)/delta));lo=max(lo,aa);hi=min(hi,bb)
 if lo>=hi:return VGroup()
 a=p(x1+lo*dx,y1+lo*dy);b=p(x1+hi*dx,y1+hi*dy)
 return DashedLine(a,b,color=color,stroke_width=2,dash_length=.09) if dashed else Line(a,b,color=color,stroke_width=2)
def lens(f=1.5):
 group=VGroup(Line(p(-6,0),p(6,0),color=D,stroke_width=1),Line(p(0,-1.8),p(0,1.8),color=T,stroke_width=4))
 for x in [-abs(f),abs(f)]:group.add(Dot(p(x,0),radius=.045,color=D),text('F',19).move_to(p(x,-.3)))
 for z in [-1,1]:
  a=1.45 if f>0 else 1.8;b=1.8 if f>0 else 1.45
  group.add(Arrow(p(0,z*a),p(0,z*b),buff=0,color=T,stroke_width=3,max_tip_length_to_length_ratio=.4))
 return group
def diagram(u,f=1.5,h=.65,count=7,half=False,virtual=True):
 group=VGroup(Arrow(p(-u,0),p(-u,h),buff=0,color=B,stroke_width=4))
 focus=abs(u-f)<1e-6;v=None if focus else u*f/(u-f)
 if v is not None and -5.8<v<5.8 and abs(-v/u*h)<2:
  group.add(Arrow(p(v,0),p(v,-v/u*h),buff=0,color=G,stroke_width=4))
 ys=np.linspace(-1.25,1.25,count)
 if half:ys=ys[ys<0]
 for y in ys:
  slope=(y-h)/u-y/f
  group.add(segment(-u,h,0,y,B),segment(0,y,6,y+6*slope,G))
  if v is not None and v<0 and virtual:group.add(segment(v,-v/u*h,0,y,A,True))
 return group
class Lenses(Scene):
 def heading(self,s):return text(s,35).move_to(UP*3.25)
 def caption(self,s):return text(s,25).move_to(DOWN*3.15)
 def clear(self):
  for m in self.mobjects:m.clear_updaters()
  self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.7)
 def construct(self):
  self.play(FadeIn(self.heading('One object point. Many light paths.')),FadeIn(lens()))
  d=diagram(4.5,count=9);self.play(FadeIn(d),run_time=2)
  cap=self.caption('Every admitted ray from this point reaches the same image point.');self.play(FadeIn(cap));self.wait(5)
  second=diagram(4.5,h=-.65,count=7);second.set_opacity(.6)
  self.play(FadeIn(second),run_time=2);self.play(FadeOut(cap));cap=self.caption('A second object point has its own bundle and image point.');self.play(FadeIn(cap));self.wait(5)
  self.clear()
  self.play(FadeIn(self.heading('Move the object towards the focus')),FadeIn(lens()))
  u=ValueTracker(4.5);moving=always_redraw(lambda:diagram(u.get_value()));self.add(moving)
  cap=self.caption('Beyond 2f: a smaller, inverted real image.');self.play(FadeIn(cap));self.wait(3)
  self.play(u.animate.set_value(3),run_time=5,rate_func=smooth)
  self.play(FadeOut(cap));cap=self.caption('At 2f: object and image have equal height.');self.play(FadeIn(cap));self.wait(3)
  self.play(u.animate.set_value(2.25),run_time=5,rate_func=smooth)
  self.play(FadeOut(cap));cap=self.caption('Between f and 2f: a larger image, farther from the lens.');self.play(FadeIn(cap));self.wait(3)
  self.play(u.animate.set_value(1.7),run_time=5,rate_func=smooth)
  self.play(FadeOut(cap));cap=self.caption('The real image moves beyond the drawing, not out of existence.');self.play(FadeIn(cap));self.wait(4)
  moving.clear_updaters();self.clear()
  self.play(FadeIn(self.heading('Exactly at f: no finite image')),FadeIn(lens()),FadeIn(diagram(1.5)))
  self.play(FadeIn(self.caption('Rays from this point leave parallel. A finite screen cannot focus them.')));self.wait(7)
  self.clear()
  self.play(FadeIn(self.heading('Inside f: follow the outgoing rays backwards')),FadeIn(lens()))
  self.play(FadeIn(diagram(.9,virtual=False)),run_time=2);self.wait(2)
  full=diagram(.9);self.play(FadeIn(full),run_time=2)
  self.play(FadeIn(self.caption('Dashed extensions meet: upright, enlarged, virtual.')));self.wait(7)
  self.clear()
  self.play(FadeIn(self.heading('A diverging lens: a different bend')),FadeIn(lens(-1.5)),FadeIn(diagram(3,-1.5)))
  self.play(FadeIn(self.caption('For a real object: virtual, upright and smaller.')));self.wait(7)
  self.clear()
  self.play(FadeIn(self.heading('Cover half the lens. Predict the result.')),FadeIn(lens()))
  first=diagram(4.5,count=9);second=diagram(4.5,h=-.65,count=9)
  self.play(FadeIn(first),FadeIn(second));self.wait(3)
  cover=Line(p(0,0),p(0,1.8),color=D,stroke_width=14)
  self.play(FadeIn(cover),Transform(first,diagram(4.5,count=9,half=True)),Transform(second,diagram(4.5,h=-.65,count=9,half=True)),run_time=2)
  self.play(FadeIn(self.caption('Fewer paths from BOTH points. Whole image; less light.')));self.wait(7)

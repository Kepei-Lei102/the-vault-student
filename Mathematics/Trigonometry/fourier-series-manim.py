"""Stack: Manim CE. Render -qm, inspect, then -qh and -qk.
The first scene includes locally generated, RMS-matched 220 Hz WAVs.
Plots retain unnormalised mathematical coefficients; gain does not change ratios.
"""
from manim import *
import numpy as np
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('lab',ROOT/'fourier-series-lab.py');lab=importlib.util.module_from_spec(spec);spec.loader.exec_module(lab)
config.background_color='#1e1e1e'
TXT='#dddddd';GREY='#999999';BLUE='#60a5fa';PINK='#ed78b3';GREEN='#48bb96';AMBER='#f4b44c'
class FourierSeries(Scene):
 def words(self,s,y,size=28,color=TXT):
  m=Text(s,font_size=size,color=color).move_to([0,y,0])
  if m.width>13:m.scale_to_fit_width(13)
  return m
 def caption(self,s):
  new=self.words(s,-3.32,25)
  if hasattr(self,'cap') and self.cap in self.mobjects:self.play(FadeOut(self.cap),run_time=.35)
  self.cap=new;self.play(FadeIn(new),run_time=.4)
 def clear_scene(self):self.play(*[FadeOut(m) for m in self.mobjects],run_time=.8)
 def curve(self,axes,x,y,color=PINK,width=3):
  c=VMobject(color=color,stroke_width=width)
  c.set_points_as_corners([axes.c2p(float(a),float(b)) for a,b in zip(x,y)]);return c
 def construct(self):
  self.harmonics();self.projection();self.gibbs()
 def harmonics(self):
  title=self.words('A shape is a recipe of harmonics',3.38,37)
  ax=Axes(x_range=[-np.pi,np.pi,np.pi],y_range=[-1.5,1.5,.5],x_length=6,y_length=3.1,axis_config={'color':GREY,'include_tip':False}).move_to([-3.4,-.25,0])
  bx=Axes(x_range=[0,32,8],y_range=[0,1.4,.5],x_length=5.3,y_length=3.1,axis_config={'color':GREY,'include_tip':False}).move_to([3.55,-.25,0])
  labels=VGroup(Text('Waveform',font_size=26,color=TXT).move_to([-3.4,2.03,0]),Text('Sine coefficients',font_size=26,color=TXT).move_to([3.55,2.03,0]),Text('phase: −π → π',font_size=21,color=GREY).move_to([-3.4,-2.15,0]),Text('harmonic number: 1 → 31',font_size=21,color=GREY).move_to([3.55,-2.15,0]))
  target=VGroup(self.curve(ax,[-np.pi,0],[-1,-1],GREY,1.5),self.curve(ax,[0,np.pi],[1,1],GREY,1.5))
  self.play(FadeIn(title),FadeIn(ax),FadeIn(bx),FadeIn(labels),FadeIn(target));self.caption('Keep the same 220 Hz fundamental. Add higher harmonics.');self.wait(2)
  theta=np.linspace(-np.pi,np.pi,1601);waveform=None;bars=None;count=None
  for N in lab.STAGES:
   newcurve=self.curve(ax,theta,lab.square_sum(theta,N))
   newbars=VGroup(*[Line(bx.c2p(n,0),bx.c2p(n,4/np.pi/n),color=BLUE,stroke_width=8) for n in range(1,N+1,2)])
   newcount=self.words(f'Highest harmonic N = {N}',2.7,28,AMBER)
   if waveform is None:
    waveform=newcurve;bars=newbars;count=newcount
    self.play(FadeIn(waveform),FadeIn(bars),FadeIn(count))
   else:
    self.play(Transform(waveform,newcurve),Transform(bars,newbars),FadeOut(count),run_time=1.15)
    count=newcount;self.play(FadeIn(count),run_time=.3)
   self.add_sound(str(ROOT/f'fourier-series-h{N:02d}.wav'))
   self.wait(3.5)
  self.caption('Audio is RMS-matched. Plots retain the mathematical scale.');self.wait(3)
  self.clear_scene()
 def projection(self):
  title=self.words('How do we find the weight of one harmonic?',3.35,35)
  axes=[];plots=[];labels=[];theta=np.linspace(-np.pi,np.pi,601);f=np.sin(theta)+.5*np.sin(3*theta)
  for n,xpos in [(1,-3.4),(2,3.4)]:
   ax=Axes(x_range=[-np.pi,np.pi,np.pi],y_range=[-1.2,1.2,1],x_length=5.8,y_length=2.8,axis_config={'color':GREY,'include_tip':False}).move_to([xpos,-.2,0]);axes.append(ax)
   y=f*np.sin(n*theta);line=self.curve(ax,theta,y,BLUE)
   # Fill each sign region with small quadrilaterals; explicit geometry, no background.
   patches=VGroup()
   for i in range(0,len(theta)-1,6):
    j=min(i+6,len(theta)-1);mean=(y[i]+y[j])/2
    patches.add(Polygon(ax.c2p(theta[i],0),ax.c2p(theta[i],y[i]),ax.c2p(theta[j],y[j]),ax.c2p(theta[j],0),stroke_width=0,fill_color=BLUE if mean>=0 else AMBER,fill_opacity=.2))
   plots.append(VGroup(patches,line));labels.append(Text(f'f(θ) × sin({n}θ)',font_size=28,color=TXT).move_to([xpos,1.85,0]))
  eq=MathTex(r'f(\theta)=\sin\theta+\tfrac12\sin3\theta',color=TXT,font_size=37).move_to([0,2.6,0])
  self.play(FadeIn(title),FadeIn(eq));self.wait(2)
  self.play(*[FadeIn(m) for m in axes+labels]);self.caption('Multiply by the candidate. Add the signed area for a full period.')
  self.play(FadeIn(plots[0]),run_time=2);self.wait(2)
  answer1=MathTex(r'b_1=\frac1\pi\int_{-\pi}^{\pi}f(\theta)\sin\theta\,d\theta=1',font_size=29,color=GREEN).move_to([-3.4,-2.3,0]);self.play(FadeIn(answer1));self.wait(2)
  self.play(FadeIn(plots[1]),run_time=2);self.wait(2)
  answer2=MathTex(r'b_2=\frac1\pi\int_{-\pi}^{\pi}f(\theta)\sin2\theta\,d\theta=0',font_size=29,color=AMBER).move_to([3.4,-2.3,0]);self.play(FadeIn(answer2));self.caption('Matching components survive. Other harmonics cancel in the average.');self.wait(5);self.clear_scene()
 def gibbs(self):
  title=self.words('More harmonics: a narrower error, not a shorter peak',3.35,34)
  ax=Axes(x_range=[-.5,.5,.25],y_range=[-1.3,1.3,1],x_length=11.4,y_length=4,axis_config={'color':GREY,'include_tip':False}).move_to([0,-.15,0])
  target=VGroup(self.curve(ax,[-.5,0],[-1,-1],GREY,1.7),self.curve(ax,[0,.5],[1,1],GREY,1.7))
  x=np.linspace(-.5,.5,2501);curve=None;label=None;dot=None
  self.play(FadeIn(title),FadeIn(ax),FadeIn(target));self.caption('Zoom in on the square wave’s jump from −1 to +1.')
  for N in (7,31,127):
   newcurve=self.curve(ax,x,lab.square_sum(x,N));newlabel=self.words(f'N = {N}',2.55,28,AMBER)
   peak_x=np.pi/(N+1);newdot=Dot(ax.c2p(peak_x,lab.square_sum(peak_x,N)),color=AMBER,radius=.065)
   if curve is None:
    curve=newcurve;label=newlabel;dot=newdot;self.play(FadeIn(curve),FadeIn(label),FadeIn(dot))
   else:
    self.play(Transform(curve,newcurve),Transform(dot,newdot),FadeOut(label),run_time=2);label=newlabel;self.play(FadeIn(label),run_time=.3)
   self.wait(3)
  self.caption('The peak approaches 1.17898: about 8.949% of the jump above +1.');self.wait(5)
  self.caption('At the jump itself, every partial sum is 0: the midpoint.');mid=Dot(ax.c2p(0,0),color=GREEN);self.play(FadeIn(mid));self.wait(4)
  self.clear_scene();title=self.words('Fourier coefficients are coordinates for a waveform',1,37)
  subtitle=self.words('Projection finds them. Harmonics rebuild it. Limits need care.',-.15,27)
  self.play(FadeIn(title),FadeIn(subtitle));self.wait(5)

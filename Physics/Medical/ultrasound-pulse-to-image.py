"""Stack: Manim Community. Synthetic pulse-echo model, not a clinical scan.
Render: manim -qk ultrasound-pulse-to-image.py PulseToImage
Depths 3 and 6 cm; common c=1540 m/s. Motion slowed; amplitudes illustrative.
"""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
TXT='#cccccc'; GREY='#888888'; BLUE='#2563eb'; GREEN='#059669'; AMBER='#f59e0b'; PURPLE='#7c3aed'
def label(s,n=26,c=TXT):
 m=Text(s,font='Arial',font_size=n,color=c)
 if m.width>13: m.scale_to_fit_width(13)
 return m
class PulseToImage(Scene):
 def head(self,s,foot):
  self.add(label(s,35).to_edge(UP,buff=.3),label(foot,22).to_edge(DOWN,buff=.25))
 def clear_scene(self):self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.7)
 def construct(self):
  self.head('1. Send a pulse. Time the echoes.','Synthetic plane boundaries; uniform speed 1540 m/s; motion greatly slowed.')
  left=-5.6; scale=1.0; y=1.2
  x=lambda d:left+d*scale
  self.add(Line([x(0),y,0],[x(8),y,0],color=GREY),RoundedRectangle(width=.55,height=1.3,color=BLUE).move_to([x(0)-.4,y,0]),label('probe',22).move_to([x(0)-.4,y+1,0]))
  for d in (3,6):self.add(Line([x(d),y-.7,0],[x(d),y+.7,0],color=PURPLE),label(f'{d} cm',24).move_to([x(d),y+1,0]))
  ax=Axes(x_range=[0,100,20],y_range=[0,1,1],x_length=10,y_length=1.45,axis_config={'color':GREY,'include_ticks':False}).move_to([-.4,-1.25,0])
  self.add(ax,label('echo envelope',23).move_to([-4.8,-.35,0]),label('return time / microseconds',22).move_to([2,-2.5,0]))
  for t in (0,40,80):self.add(label(str(t),20).next_to(ax.c2p(t,0),DOWN,buff=.12))
  clock=ValueTracker(0)
  def pulse(d,reflection=False):
   def obj():
    t=clock.get_value(); pos=2*d-.154*t if reflection else .154*t
    visible=(d/.154<=t<=2*d/.154) if reflection else (0<=t<=8/.154)
    m=Line([x(pos),y-.45,0],[x(pos),y+.45,0],color=GREEN if reflection else AMBER,stroke_width=6)
    return m.set_opacity(1 if visible else 0)
   return always_redraw(obj)
  out=pulse(0); returns=[pulse(d,True) for d in (3,6)]
  cursor=always_redraw(lambda:Line(ax.c2p(clock.get_value(),0),ax.c2p(clock.get_value(),1),color=AMBER,stroke_width=2))
  def envelope(t):return .4*np.exp(-((t-6/.154)/1.6)**2)+.8*np.exp(-((t-12/.154)/1.6)**2)
  trace=always_redraw(lambda:ax.plot(envelope,x_range=[0,max(.01,clock.get_value()),.2],color=GREEN))
  self.add(out,*returns,cursor,trace);self.wait(2)
  self.play(clock.animate.set_value(39),run_time=8,rate_func=linear)
  first=label('39 us:  d = ct / 2 = 3.0 cm',26,GREEN).move_to([.5,-3,0]);self.play(FadeIn(first));self.wait(3)
  self.play(clock.animate.set_value(80),run_time=8,rate_func=linear)
  self.play(Transform(first,label('78 us:  d = ct / 2 = 6.0 cm',26,GREEN).move_to([.5,-3,0])));self.wait(3)
  for m in [out,*returns,cursor,trace]:m.clear_updaters()
  self.clear_scene()
  self.head('2. Each echo becomes a bright spot at its depth.','Display gain is illustrative. Brightness is not a direct map of tissue density.')
  frame=Rectangle(width=3.6,height=4.2,color=GREY).move_to([3,0,0]);self.add(frame)
  self.add(label('one beam',25).move_to([-4,2,0]),label('one image column',25).move_to([3,2.5,0]))
  beam=Line([-4,1.5,0],[-4,-2,0],color=BLUE);self.play(Create(beam))
  for depth,b in [(3,.4),(6,.8)]:
   py=1.5-depth*.5
   dot=Dot([-4,py,0],color=GREEN,radius=.12)
   mark=Line([2.75,py,0],[3.25,py,0],color=WHITE,stroke_width=12).set_opacity(b)
   self.play(FadeIn(dot),FadeIn(label(f'{depth} cm',23).next_to(dot,LEFT)),run_time=.6)
   self.play(TransformFromCopy(dot,mark),run_time=2)
  self.wait(3);self.clear_scene()
  self.head('3. Sweep the beam to build a slice.','Synthetic reflectors only; no scattering, refraction or attenuation in this toy scan.')
  self.add(label('boundaries in the model',25).move_to([-3.5,2.5,0]),label('reconstructed B-mode view',25).move_to([3.5,2.5,0]))
  for centre in (-3.5,3.5):self.add(Rectangle(width=5,height=4,color=GREY).move_to([centre,0,0]))
  top=lambda u:.9+.35*np.sin(u*2*np.pi)
  bottom=lambda u:-.8+.25*np.cos(u*2*np.pi)
  for func in (top,bottom):self.add(ParametricFunction(lambda t:np.array([-6+5*t,func(t),0]),t_range=[0,1],color=PURPLE))
  for u in np.linspace(.025,.975,20):
   scan=Line([-6+5*u,1.9,0],[-6+5*u,-1.9,0],color=AMBER)
   dots=VGroup(*[Rectangle(width=.22,height=.14,stroke_width=0,fill_color=WHITE,fill_opacity=b).move_to([1+5*u,f(u),0]) for f,b in [(top,.5),(bottom,.9)]])
   self.add(scan);self.play(FadeIn(dots),run_time=.25);self.remove(scan)
  self.wait(4);self.clear_scene()
  self.head('4. The echo loses energy on BOTH journeys.','One reflector, normal incidence; ignore spreading and other interfaces.')
  formula=label('I_echo / I_send = R exp(-2 mu d)',36,GREEN).move_to([0,1.8,0]);self.add(formula)
  axis=Axes(x_range=[0,10,2],y_range=[0,.3,.1],x_length=9,y_length=3,axis_config={'color':GREY}).move_to([0,-.2,0])
  one=axis.plot(lambda d:.25*np.exp(-.15*d),color=AMBER)
  two=axis.plot(lambda d:.25*np.exp(-.30*d),color=GREEN)
  self.play(FadeIn(axis),Create(one),run_time=2);self.add(label('one-way loss only: too optimistic',23,AMBER).move_to([0,1,0]));self.wait(2)
  self.play(Create(two),run_time=3);self.add(label('out + back: the actual toy-model echo',23,GREEN).move_to([0,-2.4,0]),label('depth / cm',22).move_to([4,-1.9,0]));self.wait(5)

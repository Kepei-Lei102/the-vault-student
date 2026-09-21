"""Stack: Manim CE. Buffer deadlines and plugin delay, deliberately distinct.
Render -qm, -qh, -qk; media/cache paths outside the vault.
Timeline: 0–9 introduction; 9–26 successful callbacks; 26–40 missed deadline;
40–51 larger buffer; 51–69 plugin delay compensation; final recap.
"""
from manim import *
import numpy as np
config.background_color = '#1e1e1e'
TXT='#cccccc'; DIM='#888888'; BLUE='#2563eb'; GREEN='#059669'; RED='#dc2626'; PURPLE='#7c3aed'; AMBER='#f59e0b'

class AudioDeadline(Scene):
    def words(self,s,y,size=27):
        m=Text(s,font='DejaVu Sans',font_size=size,color=TXT).move_to([0,y,0])
        if m.width>12.8:m.scale_to_fit_width(12.8)
        return m
    def clear(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.6)
    def construct(self):
        self.play(FadeIn(self.words('A DAW has a deadline',2.8,40)))
        self.play(FadeIn(self.words('48,000 samples must reach the output every second.',1.2)))
        self.play(FadeIn(self.words('The CPU prepares blocks while the interface plays the previous block.',-.1,25)))
        self.play(FadeIn(self.words('Here: one block = 128 samples = 2.667 ms',-1.5,30)))
        self.wait(5)
        self.clear()
        title=self.words('128 samples: the next block must be ready in 2.667 ms',3,31)
        labels=VGroup(Text('PLAYBACK',font_size=24,color=TXT).move_to([-4.9,1.4,0]),Text('CPU',font_size=24,color=TXT).move_to([-4.9,-.3,0]))
        boxes=VGroup(*[Rectangle(width=2.45,height=.65,color=BLUE).move_to([-2.5+2.55*i,1.4,0]) for i in range(3)])
        boxnames=VGroup(*[Text('Block '+str(i),font_size=23,color=TXT).move_to(boxes[i]) for i in range(3)])
        self.play(FadeIn(title),FadeIn(labels),FadeIn(boxes),FadeIn(boxnames))
        note=self.words('While block 0 plays, compute block 1.',-2,27);self.play(FadeIn(note))
        for i in range(2):
            start=-3.725+i*2.55
            timer=Line([start,.8,0],[start,2,0],color=AMBER)
            job=Rectangle(width=.02,height=.55,fill_color=GREEN,fill_opacity=.6,stroke_width=0).move_to([start+.01,-.3,0])
            full=Rectangle(width=1.6,height=.55,fill_color=GREEN,fill_opacity=.6,stroke_width=0).move_to([start+.8,-.3,0])
            self.add(timer,job)
            self.play(timer.animate.shift(RIGHT*1.7),Transform(job,full),run_time=3,rate_func=linear)
            ready=Text('Ready',font_size=22,color=GREEN).next_to(job,DOWN,buff=.18);self.play(FadeIn(ready),run_time=.4)
            self.play(timer.animate.shift(RIGHT*.85),run_time=1.5,rate_func=linear)
            if i==0:self.play(Transform(note,self.words('Ready early: playback continues without a gap.',-2,27)),run_time=.4)
        self.wait(2);self.clear()
        self.play(FadeIn(self.words('A late callback: the speaker cannot wait',3,34)))
        start=-5; end=1.5
        line=Line([start,.8,0],[end,.8,0],color=BLUE,stroke_width=7)
        deadline=DashedLine([end,1.8,0],[end,-1.2,0],color=AMBER)
        self.play(FadeIn(line),FadeIn(deadline),FadeIn(self.words('Playback drains its queued samples at a fixed rate.',2,26)))
        label=Text('2.667 ms',font_size=23,color=AMBER).next_to(deadline,DOWN)
        self.add(label)
        cursor=Dot([start,.8,0],color=TXT)
        work=Line([start,-.4,0],[start+.01,-.4,0],color=PURPLE,stroke_width=16)
        self.add(cursor,work)
        self.play(cursor.animate.move_to([end,.8,0]),work.animate.put_start_and_end_on([start,-.4,0],[end,-.4,0]),run_time=5,rate_func=linear)
        failure=self.words('Deadline passed; block is still being computed.',-2.1,28)
        self.play(FadeIn(failure),work.animate.put_start_and_end_on([start,-.4,0],[4,-.4,0]),run_time=2)
        self.play(FadeIn(self.words('An underrun can produce a click, silence or repeated audio.',-2.8,24)))
        self.wait(3);self.clear()
        self.play(FadeIn(self.words('A larger block buys time — and waiting',2.7,36)))
        self.play(FadeIn(self.words('128 / 48,000 = 2.667 ms per block',1.15,31)))
        self.play(FadeIn(self.words('512 / 48,000 = 10.667 ms per block',0,31)))
        self.play(FadeIn(self.words('Fewer callbacks; more scheduling margin, but more buffering.',-1.35,25)))
        self.play(FadeIn(self.words('These are block durations, not measured round-trip latency.',-2.45,24)))
        self.wait(5);self.clear()
        self.play(FadeIn(self.words('Plugin delay is a different problem',3,36)))
        self.play(FadeIn(self.words('Lookahead deliberately delays one path by 240 samples (5 ms).',2.15,25)))
        tracks=VGroup(Line([-4.8,.75,0],[4.8,.75,0],color=BLUE),Line([-4.8,-.65,0],[4.8,-.65,0],color=GREEN))
        self.add(tracks)
        names=VGroup(Text('Lookahead path: 240 samples',font_size=23,color=TXT).move_to([0,1.25,0]),Text('Other path: initially 0 samples',font_size=23,color=TXT).move_to([0,-1.15,0]))
        self.play(FadeIn(names))
        top=Dot([-4.8,.75,0],color=BLUE);bottom=Dot([-4.8,-.65,0],color=GREEN);self.add(top,bottom)
        self.play(bottom.animate.shift(RIGHT*4.48),run_time=1.4,rate_func=linear)
        self.play(top.animate.shift(RIGHT*5.12),bottom.animate.shift(RIGHT*5.12),run_time=1.6,rate_func=linear)
        arrival=self.words('Same event, different arrival times.',-2.3,27)
        self.play(FadeIn(arrival));self.wait(2)
        self.play(FadeOut(top),FadeOut(bottom),Transform(arrival,self.words('Add the same waiting time to the earlier path.',-2.3,27)));self.play(Transform(names[1],Text('Other path: add 240 samples of delay',font_size=23,color=TXT).move_to([0,-1.15,0])))
        top=Dot([-4.8,.75,0],color=BLUE);bottom=Dot([-4.8,-.65,0],color=GREEN);self.add(top,bottom)
        self.wait(1.4)
        self.play(top.animate.shift(RIGHT*9.6),bottom.animate.shift(RIGHT*9.6),run_time=3,rate_func=linear)
        self.play(FadeIn(self.words('Compensation aligns paths by waiting. It cannot predict live input.',-3,24)));self.wait(4)
        self.clear()
        self.play(FadeIn(self.words('Two questions to ask',2,37)))
        self.play(FadeIn(self.words('Deadline: can the CPU finish each block in time?',.6,30)))
        self.play(FadeIn(self.words('Delay: how long does the signal take to reach the output?',-.7,28)))
        self.wait(5)

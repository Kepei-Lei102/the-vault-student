"""Render: manim -qk heap-sift-animation.py HeapSift
Two simultaneous views of one array; each moving key has the same colour in both.
"""
from manim import *
import numpy as np
config.background_color = '#1e1e1e'
TXT='#cccccc'; DIM='#888888'; BLUE='#2563eb'; AMBER='#f59e0b'; GREEN='#059669'

def label(s, size=26):
    obj=Text(s,font='Arial',font_size=size,color=TXT)
    if obj.width>13:obj.scale_to_fit_width(13)
    return obj

class HeapSift(Scene):
    def construct(self):
        title=label('A heap: keep the next event ready',38).move_to([0,3.45,0])
        caption=label('Smaller time = earlier event. Only parents must outrank children.',25).move_to([0,-3.35,0])
        self.add(title,caption)
        # Left: tree. Right: 2-column array, every cell has an explicit index.
        positions=[(-3.5,2),(-5, .65),(-2,.65),(-5.8,-.7),(-4.2,-.7),(-2.8,-.7),(-1.2,-.7),(-6.1,-2)]
        positions=[np.array([x,y,0.]) for x,y in positions]
        cells=[np.array([2.4+(i%2)*1.65,1.95-(i//2)*1.08,0.]) for i in range(8)]
        self.add(label('complete tree',22).move_to([-3.5,2.7,0]),label('one array, indices 0–7',22).move_to([3.25,2.7,0]))
        rings=VGroup(*[Circle(radius=.31,color=DIM,stroke_width=2).move_to(p) for p in positions])
        edges=VGroup(*[Line(positions[(i-1)//2],positions[i],buff=.33,color=DIM,stroke_width=2) for i in range(1,8)])
        boxes=VGroup(*[RoundedRectangle(width=1.15,height=.65,corner_radius=.08,color=DIM,stroke_width=2).move_to(p) for p in cells])
        indices=VGroup(*[label(str(i),18).move_to(p+LEFT*.82) for i,p in enumerate(cells)])
        self.add(*edges[:6],*rings[:7],boxes,indices)
        values=[2,5,3,9,7,8,4]
        t=[label(str(v),27).move_to(positions[i]) for i,v in enumerate(values)]
        a=[label(str(v),27).move_to(cells[i]) for i,v in enumerate(values)]
        self.add(*t,*a)
        self.wait(5)
        def say(s):
            self.play(Transform(caption,label(s,25).move_to([0,-3.35,0])),run_time=.4)
        say('The array is not sorted: 5 appears before 3. The root is still minimum.')
        self.play(Indicate(a[1],color=AMBER),Indicate(a[2],color=AMBER),run_time=1.5);self.wait(3)
        say('Insert time 1: append at index 7. Shape first; order next.')
        self.play(FadeIn(rings[7]),FadeIn(edges[6]),run_time=.7)
        t.append(label('1',27).set_color(AMBER).move_to(positions[7]));a.append(label('1',27).set_color(AMBER).move_to(cells[7]));values.append(1)
        self.play(FadeIn(t[7]),FadeIn(a[7]),run_time=.7);self.wait(3)
        def swap(i,j):
            self.play(t[i].animate.move_to(positions[j]),t[j].animate.move_to(positions[i]),
                      a[i].animate.move_to(cells[j]),a[j].animate.move_to(cells[i]),run_time=1.6)
            t[i],t[j]=t[j],t[i];a[i],a[j]=a[j],a[i];values[i],values[j]=values[j],values[i]
        for i,j in [(7,3),(3,1),(1,0)]:
            say(f'Sift up: index {i} → {j}. {values[i]} is smaller than parent {values[j]}.')
            self.play(Indicate(rings[j],color=AMBER),run_time=.5);swap(i,j);self.wait(2)
        assert values==[1,2,3,5,7,8,4,9]
        say('Minimum restored. Only one path changed; every other branch stayed valid.')
        self.wait(4)
        say('Extract time 1. Save the root, then move the final leaf into its slot.')
        self.play(FadeOut(t[0]),FadeOut(a[0]),run_time=.7)
        self.play(t[7].animate.move_to(positions[0]).set_color(AMBER),a[7].animate.move_to(cells[0]).set_color(AMBER),
                  FadeOut(rings[7]),FadeOut(edges[6]),run_time=1.8)
        t[0]=t.pop();a[0]=a.pop();values[0]=values.pop();self.wait(2)
        for i,j in [(0,1),(1,3)]:
            say(f'Sift down: choose the smaller child, {values[j]}. Repair index {i} → {j}.')
            self.play(Indicate(rings[j],color=GREEN),run_time=.5);swap(i,j);self.wait(2.5)
        assert values==[2,5,3,9,7,8,4]
        say('Root 2 is ready. Heap order is restored without sorting the whole array.')
        self.wait(4)
        self.play(*[FadeOut(x) for x in list(self.mobjects)],run_time=.7)
        self.add(label('Why building a whole heap is cheaper',36).move_to([0,3.2,0]))
        self.add(label('15 nodes: start at the last parent and repair towards the root.',25).move_to([0,2.4,0]))
        for row,(nodes,steps) in enumerate([(8,0),(4,1),(2,2),(1,3)]):
            y=1.2-row*1.0
            dots=VGroup(*[Dot(radius=.1,color=BLUE).move_to([-5.3+i*.43,y,0]) for i in range(nodes)])
            description=label(f'{nodes} nodes × at most {steps} downward steps = {nodes*steps}',25).move_to([1.7,y,0])
            self.play(FadeIn(dots),FadeIn(description),run_time=.5);self.wait(1.8)
        self.add(label('11 available steps, not 15 × 3. Most nodes are near the bottom.',26).move_to([0,-3.1,0]))
        self.wait(5)

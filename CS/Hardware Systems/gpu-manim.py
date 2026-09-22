"""Manim Community: GPU work and reuse. Render: manim -qk gpu-manim.py GPUWork
Illustrative work counts, not GPU timing. Eight lanes are a drawing, not a warp width.
"""
from manim import *
BG, TXT, DIM = '#1e1e1e', '#cccccc', '#888888'
BLUE, GREEN, PURPLE, AMBER = '#2563eb', '#059669', '#7c3aed', '#f59e0b'
config.background_color = BG

def label(s, size=28, color=TXT):
    return Text(s, font='Arial', font_size=size, color=color)

class GPUWork(Scene):
    def clean(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=.7)

    def construct(self):
        title=label('1 / A triangle becomes many small jobs',36).to_edge(UP)
        self.play(FadeIn(title))
        grid=NumberPlane(x_range=[0,8,1],y_range=[0,8,1],x_length=5.2,y_length=5.2,
            axis_config={'color':DIM,'stroke_opacity':.4},
            background_line_style={'stroke_color':DIM,'stroke_opacity':.18}).shift(LEFT*3+DOWN*.25)
        point=lambda x,y:grid.c2p(x,y)
        tri=Polygon(point(1,1),point(7,1),point(1,7),color=BLUE,fill_opacity=.15)
        self.play(FadeIn(grid),FadeIn(tri),run_time=1.4)
        caption=label('Test each sample centre.\nCovered samples become\ncandidates for shading.',26).move_to(RIGHT*3+UP)
        self.play(FadeIn(caption));self.wait(2)
        dots=VGroup(*[Dot(point(x+.5,y+.5),radius=.045,color=GREEN)
                     for y in range(8) for x in range(8) if x>=1 and y>=1 and x+y<=7])
        self.play(LaggedStart(*[FadeIn(d) for d in dots],lag_ratio=.13),run_time=4)
        count=label('21 covered samples',28).move_to(RIGHT*3+DOWN*.5)
        self.play(FadeIn(count));self.wait(2)
        chosen=Circle(radius=.13,color=AMBER).move_to(point(2.5,2.5))
        weights=label('At (2.5, 2.5):\n½ A + ¼ B + ¼ C',28).move_to(RIGHT*3+DOWN*1.7)
        self.play(FadeIn(chosen),FadeIn(weights));self.wait(4)
        footer=label('Different data, similar calculations. One sample per pixel here.',22,DIM).to_edge(DOWN)
        self.play(FadeIn(footer));self.wait(3);self.clean()

        title=label('2 / A branch can leave lanes idle',36).to_edge(UP)
        self.play(FadeIn(title))
        values=[-4,-3,-2,-1,0,1,2,3]
        boxes=VGroup(*[Square(.8,color=DIM,fill_opacity=.1).move_to([-.0+(i-3.5)*1.1,.6,0]) for i in range(8)])
        nums=VGroup(*[label(str(v)).move_to(boxes[i]) for i,v in enumerate(values)])
        self.play(FadeIn(boxes),FadeIn(nums))
        note=label('Eight illustrated lanes; equal-cost paths',24,DIM).move_to(UP*2)
        self.play(FadeIn(note));self.wait(2)
        path=label('Square path: x ≥ 0',30).move_to(DOWN*.7)
        self.play(FadeIn(path),*[boxes[i].animate.set_fill(GREEN,opacity=.45) for i in range(4,8)],
                  *[nums[i].animate.set_opacity(.25) for i in range(4)])
        self.wait(3)
        results=VGroup(*[label(str(v*v),24).next_to(boxes[i],DOWN,buff=.18) for i,v in enumerate(values) if i>=4])
        self.play(FadeIn(results));self.wait(2)
        path2=label('Negate path: x < 0',30).move_to(path)
        self.play(ReplacementTransform(path,path2),*[boxes[i].animate.set_fill(PURPLE,opacity=.45) for i in range(4)],
                  *[boxes[i].animate.set_fill(GREEN,opacity=.08) for i in range(4,8)],
                  *[nums[i].animate.set_opacity(1 if i<4 else .25) for i in range(8)])
        result2=VGroup(*[label(str(-v),24).next_to(boxes[i],DOWN,buff=.18) for i,v in enumerate(values) if i<4])
        self.play(FadeIn(result2));self.wait(3)
        equation=label('8 useful lane-operations / 16 issued slots = 50%',28).move_to(DOWN*1.8)
        self.play(FadeIn(equation));self.wait(3)
        caveat=label('A toy utilisation count, not a promised application slowdown.',22,DIM).to_edge(DOWN)
        self.play(FadeIn(caveat));self.wait(3);self.clean()

        title=label('3 / Load once, use more than once',36).to_edge(UP)
        self.play(FadeIn(title))
        def matrix(values, center, color):
            cells=VGroup();texts=VGroup()
            for i in range(2):
                for j in range(2):
                    p=center+RIGHT*(j-.5)*.8+UP*(.5-i)*.8
                    cells.add(Square(.8,color=color,fill_opacity=.12).move_to(p))
                    texts.add(label(str(values[i][j]),28).move_to(p))
            return cells,texts
        ac,at=matrix([[1,2],[3,4]],LEFT*2.4+UP*.9,BLUE)
        bc,bt=matrix([[5,6],[7,8]],RIGHT*2.4+UP*.9,PURPLE)
        cc,ct=matrix([['?','?'],['?','?']],DOWN*1.5,GREEN)
        self.play(FadeIn(ac),FadeIn(at),FadeIn(bc),FadeIn(bt),FadeIn(cc),FadeIn(ct))
        names=VGroup(label('A',26).next_to(ac,UP),label('B',26).next_to(bc,UP),label('C',26).next_to(cc,LEFT))
        self.play(FadeIn(names));self.wait(2)
        formulas=['1×5 + 2×7 = 19','1×6 + 2×8 = 22','3×5 + 4×7 = 43','3×6 + 4×8 = 50']
        for index,value in enumerate([19,22,43,50]):
            i,j=divmod(index,2)
            row=VGroup(ac[2*i],ac[2*i+1]);col=VGroup(bc[j],bc[j+2])
            ra=SurroundingRectangle(row,color=AMBER,buff=.04)
            rb=SurroundingRectangle(col,color=AMBER,buff=.04)
            expr=label(formulas[index],27).move_to(DOWN*.35)
            self.play(FadeIn(ra),FadeIn(rb),FadeIn(expr),run_time=.6);self.wait(1.6)
            answer=label(str(value),28).move_to(ct[index])
            self.play(ReplacementTransform(ct[index],answer),run_time=.5);self.wait(.8)
            self.play(FadeOut(ra),FadeOut(rb),FadeOut(expr),run_time=.4)
        last=label('8 loaded inputs → 8 multiply-adds → 4 outputs',27).to_edge(DOWN)
        self.play(FadeIn(last));self.wait(3)
        self.play(Indicate(ac,color=AMBER),Indicate(bc,color=AMBER));self.wait(2)
        self.clean()
        conclusion=VGroup(label('The arithmetic did not disappear.',36),label('We reused the data that feeds it.',36),
                          label('Parallel work + locality = useful throughput',26,DIM)).arrange(DOWN,buff=.5)
        self.play(FadeIn(conclusion));self.wait(5)

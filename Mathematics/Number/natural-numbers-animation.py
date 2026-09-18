"""stack: Manim CE. Finite ordinals and recursive addition; final render -qk."""
from manim import *
config.background_color = '#1e1e1e'
TXT = '#cccccc'
BLUE = '#2563eb'
GREEN = '#059669'
PURPLE = '#7c3aed'
AMBER = '#f59e0b'


def label(s, size=30, color=TXT):
    return Text(s, font='Helvetica', font_size=size, color=color)


class NaturalNumbers(Scene):
    def construct(self):
        title = label('A number made from earlier numbers', 36).to_edge(UP)
        rule = MathTex(r'0=\varnothing,\quad S(n)=n\cup\{n\}', color=TXT).next_to(title, DOWN, buff=.4)
        self.play(FadeIn(title), FadeIn(rule))
        self.wait(2)
        box = RoundedRectangle(width=7.5, height=2.1, corner_radius=.15, color=BLUE).shift(UP*.2)
        name = label('0 = { }', 34).next_to(box, UP)
        caption = label('Zero contains no elements.', 27).to_edge(DOWN, buff=.8)
        self.play(FadeIn(box), FadeIn(name), FadeIn(caption))
        self.wait(2)
        tokens = VGroup()
        for n in range(4):
            # Each new token denotes the ENTIRE previous ordinal, not a copy of its members.
            token = VGroup(Circle(radius=.46, color=AMBER), label(str(n), 31, AMBER))
            token.move_to(RIGHT*5 + UP*.2)
            note = label(f'Keep every old element. Add {n} itself as ONE new element.', 25).to_edge(DOWN, buff=.8)
            self.play(Transform(caption, note), FadeIn(token))
            self.wait(1)
            target_x = -2.25 + n*1.5
            self.play(token.animate.move_to([target_x,.2,0]), run_time=1.8)
            newname = label(f'{n+1} = {{'+', '.join(str(i) for i in range(n+1))+'}', 34).next_to(box, UP)
            self.play(Transform(name, newname), token[0].animate.set_color(GREEN), token[1].animate.set_color(TXT))
            tokens.add(token)
            self.wait(2)
        note = label('Four elements — each label abbreviates a set already constructed.', 24).to_edge(DOWN, buff=.8)
        self.play(Transform(caption,note));self.wait(3)
        self.play(*[FadeOut(m) for m in list(self.mobjects)])
        title = label('Addition repeats the successor step',36).to_edge(UP)
        rule = MathTex(r'a+0=a,\quad a+S(b)=S(a+b)',color=TXT).next_to(title,DOWN,buff=.4)
        self.play(FadeIn(title),FadeIn(rule))
        line=NumberLine(x_range=[0,6,1],length=10,include_numbers=True,color='#888888').shift(DOWN*.4)
        dot=Dot(line.n2p(2),color=AMBER,radius=.12)
        eq=MathTex('2+3',color=TXT).scale(1.3).shift(UP*.5)
        cap=label('Three successor steps, starting at 2.',27).to_edge(DOWN,buff=.8)
        self.play(FadeIn(line),FadeIn(dot),FadeIn(eq),FadeIn(cap));self.wait(2)
        for k in range(1,4):
            arc=ArcBetweenPoints(line.n2p(1+k)+UP*.15,line.n2p(2+k)+UP*.15,angle=-PI/2,color=PURPLE)
            self.play(Create(arc),MoveAlongPath(dot,arc),run_time=1.5)
            self.play(dot.animate.move_to(line.n2p(2+k)),run_time=.3)
            neweq=MathTex(['S(2+2)','S(S(2+1))','S(S(S(2+0)))'][k-1],color=TXT).scale(1.3).shift(UP*.5)
            self.play(Transform(eq,neweq));self.wait(1.5)
        final=MathTex(r'S(S(S(2)))=5',color=TXT).scale(1.3).shift(UP*.5)
        self.play(Transform(eq,final),Transform(cap,label('The zero clause ends the recursion.',27).to_edge(DOWN,buff=.8)))
        self.wait(4)

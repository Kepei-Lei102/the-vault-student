"""tech-stack-manim.py — one click's journey through a stack, with the clock running.

Render:  manim -qk tech-stack-manim.py RequestJourney
Then copy media/videos/tech-stack-manim/2160p60/RequestJourney.mp4 to
tech-stack-request-journey.mp4 beside the card and delete media/ and __pycache__/.
"""
from manim import *
import textwrap

BLUE_, RED_, AMBER_, GREEN_, PURPLE_, TEAL_, GREY_ = "#60a5fa", "#f87171", "#fbbf24", "#34d399", "#c4b5fd", "#67e8f9", "#9ca3af"

# each hop: (name, colour, cost in ms on a cold first visit, cost on a warm second visit or None if skipped)
HOPS = [("browser", BLUE_, 0, 0), ("DNS", GREY_, 20, None), ("TCP + TLS", AMBER_, 60, None), ("edge cache", TEAL_, 5, 5),
        ("load balancer", GREY_, 1, None), ("app server", PURPLE_, 3, None), ("database", GREEN_, 8, None)]


class RequestJourney(Scene):
    def cap(self, text, old=None):
        c = Text("\n".join(textwrap.wrap(text, 84)), font_size=22, color=GREY_, line_spacing=0.8).to_edge(DOWN, buff=0.3)
        self.play(*([FadeOut(old)] if old else []), FadeIn(c)); return c

    def construct(self):
        title = Text("One click, layer by layer, with the clock running", font_size=34, color=WHITE).to_edge(UP, buff=0.25)
        self.add(title)
        boxes = VGroup()
        for name, col, _, _ in HOPS:
            b = RoundedRectangle(width=1.7, height=0.9, corner_radius=0.12, stroke_color=col, fill_color=col, fill_opacity=0.15)
            t = Text(name, font_size=18, color=WHITE).move_to(b)
            boxes.add(VGroup(b, t))
        boxes.arrange(RIGHT, buff=0.22).move_to([0, 1.4, 0])
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in boxes], lag_ratio=0.12, run_time=1.6))
        clock = Integer(0, font_size=40, color=WHITE).move_to([5.1, -0.5, 0])
        ms = Text("ms", font_size=22, color=GREY_).move_to([5.85, -0.55, 0])
        clock_label = Text("elapsed", font_size=18, color=GREY_).move_to([5.3, -0.05, 0])
        self.add(clock, ms, clock_label)
        # the timeline bar: one segment per hop, width proportional to its cost
        SCALE = 0.052   # units per ms
        bar_y, bar_x0 = -0.55, -6.3
        bar_lab = Text("first visit", font_size=18, color=GREY_).move_to([bar_x0 + 0.5, bar_y + 0.38, 0])
        self.add(bar_lab)

        dot = Dot(color=WHITE, radius=0.11).move_to(boxes[0].get_center() + DOWN * 0.7)
        c = self.cap("A first visit: nothing is cached, no connection is open. Each hop adds its cost to the clock.")
        self.play(FadeIn(dot))
        total = 0; x = bar_x0
        for i, (name, col, cost, _) in enumerate(HOPS):
            if i > 0:
                self.play(dot.animate.move_to(boxes[i].get_center() + DOWN * 0.7), run_time=0.45)
            if cost:
                seg = Rectangle(width=cost * SCALE, height=0.32, fill_color=col, fill_opacity=0.7, stroke_width=0).move_to([x + cost * SCALE / 2, bar_y, 0])
                total += cost
                anims = [GrowFromEdge(seg, LEFT), ChangeDecimalToValue(clock, total)]
                if cost >= 10:
                    anims.append(FadeIn(Text("%s %d" % (name, cost), font_size=14, color=col).next_to(seg, DOWN, buff=0.08)))
                self.play(*anims, run_time=0.5)
                x += cost * SCALE
            if name == "database":
                small = Text("edge 5 · balancer 1 · app 3 · database 8", font_size=14, color=GREY_).move_to([x - 0.45, bar_y - 0.62, 0])
                self.play(FadeIn(small), run_time=0.4)
            if name == "database":
                c = self.cap("The database answers; the reply retraces the wires. Network hops cost the same on the way back.", c)
        # the return trip: retrace the network legs only
        back = 30
        seg = Rectangle(width=back * SCALE, height=0.32, fill_color=AMBER_, fill_opacity=0.5, stroke_width=0).move_to([x + back * SCALE / 2, bar_y, 0])
        lab = Text("reply %d" % back, font_size=14, color=AMBER_).next_to(seg, DOWN, buff=0.08)
        total += back
        self.play(dot.animate.move_to(boxes[0].get_center() + DOWN * 0.7), GrowFromEdge(seg, LEFT), ChangeDecimalToValue(clock, total), FadeIn(lab), run_time=1.2)
        first = Text("first visit: %d ms, and the code that does the work took %d of them" % (total, 3), font_size=20, color=WHITE).move_to([0, -2.55, 0])
        self.play(FadeIn(first)); self.wait(1.2)
        c = self.cap("Of those milliseconds the application logic took three. The rest were distance, handshakes and the disk.", c)
        self.wait(1.8)

        # second visit: DNS cached, connection kept alive, edge cache hit
        c = self.cap("A second click. The name is cached, the connection is still open, and the edge cache has the answer.", c)
        bar2_y = -1.85
        bar2_lab = Text("second visit", font_size=18, color=GREY_).move_to([bar_x0 + 0.65, bar2_y + 0.38, 0])
        self.play(FadeIn(bar2_lab), FadeOut(first), ChangeDecimalToValue(clock, 0))
        x = bar_x0; total = 0
        path = [0, 1, 2, 3]
        for i in path[1:]:
            name, col, _, warm = HOPS[i]
            self.play(dot.animate.move_to(boxes[i].get_center() + DOWN * 0.7), run_time=0.4)
            if warm is None:
                skip = Text("skipped", font_size=14, color=GREY_).next_to(boxes[i], UP, buff=0.08)
                self.play(FadeIn(skip), run_time=0.3)
            else:
                seg = Rectangle(width=warm * SCALE, height=0.32, fill_color=col, fill_opacity=0.7, stroke_width=0).move_to([x + warm * SCALE / 2, bar2_y, 0])
                lab = Text("%s %d" % (name, warm), font_size=14, color=col).next_to(seg, DOWN, buff=0.08).shift(LEFT * 0.15)
                total += warm; x += warm * SCALE
                self.play(GrowFromEdge(seg, LEFT), ChangeDecimalToValue(clock, total), FadeIn(lab), run_time=0.5)
        seg = Rectangle(width=back * SCALE, height=0.32, fill_color=AMBER_, fill_opacity=0.5, stroke_width=0).move_to([x + back * SCALE / 2, bar2_y, 0])
        lab = Text("reply %d" % back, font_size=14, color=AMBER_).next_to(seg, DOWN, buff=0.08)
        total += back
        self.play(dot.animate.move_to(boxes[0].get_center() + DOWN * 0.7), GrowFromEdge(seg, LEFT), ChangeDecimalToValue(clock, total), FadeIn(lab), run_time=1.0)
        second = Text("second visit: %d ms. The app server and the database never heard about it." % total, font_size=20, color=WHITE).move_to([0, -2.75, 0])
        self.play(FadeIn(second))
        c = self.cap("That is what a cache buys, and what it costs: the second visitor may be shown an answer that is a few seconds old.", c)
        self.wait(2.5)

"""Manim companion for How a Chip Is Made.

    manim -qk chip-fabrication-manim.py Lithography     (4K; copy the MP4 to chip-fabrication-lithography.mp4)

One layer of the planar process on a cross-section of the wafer: grow an oxide, coat resist, expose through a mask,
develop, etch the oxide where it is bare, implant dopant through the window, strip the resist. Then the loop repeats and
a stack builds. The stencil is the whole idea; everything else is which material goes through it.
"""
from manim import *

BLUE_, RED_, AMBER_, GREEN_, PURPLE_, TEAL_, GREY_ = "#60a5fa", "#f87171", "#fbbf24", "#34d399", "#c4b5fd", "#67e8f9", "#9ca3af"
L, R, Y0 = -5.0, 5.0, -1.2               # wafer cross-section extent and top surface


class Lithography(Scene):
    def cap(self, text, old=None):
        import textwrap
        c = Text("\n".join(textwrap.wrap(text, 88)), font_size=22, color=GREY_, line_spacing=0.8).to_edge(DOWN, buff=0.3)
        self.play(*( [FadeOut(old)] if old else [] ), FadeIn(c)); return c

    def construct(self):
        self.camera.background_color = "#0b0f19"
        title = Text("One layer of the planar process", font_size=36, color=WHITE).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        wafer = Rectangle(width=R - L, height=1.6, fill_color="#555", fill_opacity=0.6, stroke_color=GREY_).move_to([0, Y0 - 0.8, 0])
        wlab = Text("silicon wafer, cross-section", font_size=20, color=GREY_).move_to(wafer)
        c = self.cap("Start with a polished silicon wafer.")
        self.play(FadeIn(wafer), FadeIn(wlab))
        # 1 oxide
        oxide = Rectangle(width=R - L, height=0.28, fill_color=TEAL_, fill_opacity=0.55, stroke_width=0).move_to([0, Y0 + 0.14, 0])
        c = self.cap("1. Grow an insulating oxide by heating the wafer in oxygen: the surface becomes glass.", c)
        self.play(GrowFromEdge(oxide, DOWN))
        # 2 resist
        resist = Rectangle(width=R - L, height=0.32, fill_color=AMBER_, fill_opacity=0.6, stroke_width=0).move_to([0, Y0 + 0.28 + 0.16, 0])
        c = self.cap("2. Spin on photoresist: a varnish that light makes soluble.", c)
        self.play(GrowFromEdge(resist, DOWN))
        # 3 mask + light
        mask_y = Y0 + 2.2
        mask_parts = VGroup(*[Rectangle(width=w, height=0.16, fill_color=WHITE, fill_opacity=0.9, stroke_width=0).move_to([x, mask_y, 0])
                              for x, w in ((-3.6, 2.8), (0.0, 2.2), (3.6, 2.8))])
        mlab = Text("mask (the stencil), reduced 4× by the lens", font_size=18, color=WHITE).next_to(mask_parts, UP, buff=0.12)
        c = self.cap("3. Expose: ultraviolet light through a mask. Where the mask is open, the resist is changed.", c)
        self.play(FadeIn(mask_parts), FadeIn(mlab))
        beams = VGroup(*[Line([x, mask_y - 0.1, 0], [x, Y0 + 0.6, 0], color=PURPLE_, stroke_width=3) for gap in ((-2.2, -1.1), (1.1, 2.2)) for x in np.linspace(gap[0] + 0.15, gap[1] - 0.15, 4)])
        exposed = VGroup(*[Rectangle(width=1.1, height=0.32, fill_color=PURPLE_, fill_opacity=0.6, stroke_width=0).move_to([xc, Y0 + 0.44, 0]) for xc in (-1.65, 1.65)])
        self.play(LaggedStart(*[Create(b) for b in beams], lag_ratio=0.05, run_time=1.2)); self.play(FadeIn(exposed)); self.play(FadeOut(beams), FadeOut(mask_parts), FadeOut(mlab))
        # 4 develop
        c = self.cap("4. Develop: wash away the exposed resist. Two windows open in the varnish.", c)
        self.play(FadeOut(exposed))
        # 5 etch
        holes = VGroup(*[Rectangle(width=1.1, height=0.28, fill_color="#0b0f19", fill_opacity=1, stroke_width=0).move_to([xc, Y0 + 0.14, 0]) for xc in (-1.65, 1.65)])
        c = self.cap("5. Etch: a plasma eats the oxide wherever it is bare; the resist protects the rest.", c)
        self.play(FadeIn(holes))
        # 6 implant
        ions = VGroup(*[Line([x, Y0 + 2.0, 0], [x, Y0 + 0.02, 0], color=GREEN_, stroke_width=2) for xc in (-1.65, 1.65) for x in np.linspace(xc - 0.4, xc + 0.4, 5)])
        doped = VGroup(*[Rectangle(width=1.1, height=0.3, fill_color=GREEN_, fill_opacity=0.55, stroke_width=0).move_to([xc, Y0 - 0.15, 0]) for xc in (-1.65, 1.65)])
        c = self.cap("6. Implant: fire dopant ions at the wafer. Only the windows let them in: two n-type regions, a source and a drain.", c)
        self.play(LaggedStart(*[Create(i) for i in ions], lag_ratio=0.03, run_time=1.0)); self.play(FadeIn(doped), FadeOut(ions))
        # 7 strip
        c = self.cap("7. Strip the resist. The pattern is now in the silicon itself, and the surface is ready for the next coat.", c)
        self.play(FadeOut(resist))
        self.wait(0.6)
        # repeat
        c = self.cap("Repeat, in register to a few nanometres, about eighty times: gates, contacts, then fifteen layers of wiring.", c)
        layers = VGroup()
        cols = [PURPLE_, "#999", BLUE_, RED_, GREEN_, AMBER_, TEAL_, PURPLE_]
        for k in range(8):
            y = Y0 + 0.3 + 0.22 * k + 0.22
            segs = VGroup(*[Rectangle(width=w, height=0.16, fill_color=cols[k], fill_opacity=0.55, stroke_width=0).move_to([x, y, 0])
                            for x, w in ((-3.2 + 0.3 * k, 1.2 + 0.2 * k), (0.4 - 0.2 * k, 1.5), (3.0 - 0.1 * k, 1.0 + 0.3 * k))])
            layers.add(segs)
        self.play(LaggedStart(*[FadeIn(l, shift=DOWN*0.1) for l in layers], lag_ratio=0.25, run_time=3.0))
        count = Text("layer 80", font_size=22, color=WHITE).move_to([4.2, Y0 + 2.5, 0])
        self.play(FadeIn(count)); self.wait(0.5)
        c = self.cap("Billions of transistors and the wiring between them, all printed at once. The stencil is the only way to make ten billion identical things.", c)
        self.wait(2.2)

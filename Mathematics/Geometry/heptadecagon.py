"""
Heptadecagon — Gauss's regular 17-gon, Richmond's 1893 construction.

Stack: Manim Community Edition (vault Manim track, inaugural piece).
Total runtime: ~95 seconds.

To render (from this directory):
    manim -qk heptadecagon.py Heptadecagon       # 2160p60 (4K) — showcase committed render
    manim -qh heptadecagon.py Heptadecagon       # 1080p60 — pre-final review
    manim -qm heptadecagon.py Heptadecagon       # 720p30  — fast iteration only
The output lands at media/videos/heptadecagon/<quality>/Heptadecagon.mp4.
For the vault embed, copy or symlink the 4K render to ./heptadecagon.mp4:
    cp media/videos/heptadecagon/2160p60/Heptadecagon.mp4 ./heptadecagon.mp4

Note: -qk takes ~4× longer to render than -qh. Iterate at -qm, review at -qh,
commit at -qk.

Vault palette (canonical source: _meta/manim_vault.py once we have multiple scripts).
This file is self-contained on purpose — runs without any vault imports.
"""

from manim import *
import numpy as np

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG       = "#1e1e1e"
TXT      = "#cccccc"      # body text — brighter than #888 because we're on dark MP4
TXT_DIM  = "#888888"      # secondary text / annotations
BLUE     = "#2563eb"
RED      = "#dc2626"
GREEN    = "#059669"
AMBER    = "#f59e0b"
GREY     = "#888888"
PURPLE   = "#7c3aed"

config.background_color = BG
config.frame_width = 14.222   # default 16:9 at 8 height
config.frame_height = 8


# ---------- Helpers ----------

def vertex(k, n=17, radius=2.5, phase=0.0):
    """Position of k-th vertex of regular n-gon centred at origin, radius r."""
    theta = 2 * np.pi * k / n + phase
    return np.array([radius * np.cos(theta), radius * np.sin(theta), 0.0])


def title_card(text, color=TXT, size=44):
    return Text(text, color=color, font_size=size, weight=BOLD)


def body(text, color=TXT, size=28):
    return Text(text, color=color, font_size=size)


def small(text, color=TXT_DIM, size=22):
    return Text(text, color=color, font_size=size)


# ---------- The scene ----------

class Heptadecagon(Scene):
    def construct(self):
        self.scene1_roll_call()
        self.scene2_why_seventeen()
        self.scene3_algebra()
        self.scene4_richmond()
        self.scene5_stamp_around()
        self.scene6_reveal()

    # =========================================================
    # SCENE 1 — The roll call of constructible polygons (~14 s)
    # =========================================================
    def scene1_roll_call(self):
        title = title_card("Constructible Polygons")
        sub = small("regular n-gons drawable with ruler and compass alone").next_to(title, DOWN, buff=0.3)
        header = VGroup(title, sub)

        self.play(FadeIn(header))
        self.wait(1.5)
        self.play(header.animate.to_edge(UP, buff=0.5))

        # Build the roll call: n labels coloured green (yes) / red (no) / amber (17)
        constructible = {3, 4, 5, 6, 8, 10, 12, 15, 16, 17, 20, 24}
        not_constructible = {7, 9, 11, 13, 14, 18, 19, 21, 22, 23}
        ns = sorted(constructible | not_constructible)

        labels = VGroup()
        for n in ns:
            if n == 17:
                colour = AMBER
                weight = BOLD
            elif n in constructible:
                colour = GREEN
                weight = NORMAL
            else:
                colour = RED
                weight = NORMAL
            t = Text(str(n), color=colour, font_size=36, weight=weight)
            labels.add(t)
        labels.arrange_in_grid(rows=2, buff=0.5).move_to(ORIGIN).shift(DOWN*0.5)

        self.play(LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.08))
        self.wait(1.0)

        # Highlight 17
        idx17 = ns.index(17)
        ring = Circle(radius=0.45, color=AMBER, stroke_width=3).move_to(labels[idx17])
        self.play(Create(ring))
        callout = small("17 is the surprise.", color=AMBER, size=26).next_to(labels, DOWN, buff=0.6)
        self.play(FadeIn(callout))
        self.wait(2.0)

        self.play(FadeOut(VGroup(header, labels, ring, callout)))

    # =========================================================
    # SCENE 2 — Why 17? Gauss–Wantzel & Fermat primes (~16 s)
    # =========================================================
    def scene2_why_seventeen(self):
        q = title_card("What's so special about 17?")
        self.play(FadeIn(q))
        self.wait(1.0)
        self.play(q.animate.to_edge(UP, buff=0.6))

        thm_title = body("Gauss–Wantzel Theorem (1796 / 1837)", color=BLUE, size=30).next_to(q, DOWN, buff=0.6)
        thm = MathTex(
            r"n\text{-gon constructible}\iff",
            r"n = 2^{k}\,p_{1}p_{2}\cdots p_{m}",
            color=TXT, font_size=36
        ).next_to(thm_title, DOWN, buff=0.4)
        thm_sub = small("where each pᵢ is a distinct Fermat prime", size=24).next_to(thm, DOWN, buff=0.2)

        self.play(FadeIn(thm_title))
        self.play(Write(thm))
        self.play(FadeIn(thm_sub))
        self.wait(1.5)

        # Show known Fermat primes — use Text (not MathTex) to avoid 4K-render OOM on
        # the bold-LaTeX rasterization of \mathbf{17}. t2c colors the "17" substring amber.
        fermats_label = body("Fermat primes (all that are known):", color=TXT_DIM, size=24).next_to(thm_sub, DOWN, buff=0.6)
        fermats = Text("3, 5, 17, 257, 65537",
                       font_size=44, weight=BOLD, color=TXT,
                       t2c={"17": AMBER}).next_to(fermats_label, DOWN, buff=0.3)

        self.play(FadeIn(fermats_label))
        self.play(FadeIn(fermats))   # FadeIn (not Write) — Write OOM-kills at 4K rendering
        self.wait(1.0)

        # 17 = F_2
        eq = MathTex(r"17 = 2^{2^{2}} + 1 \;=\; F_{2}", color=AMBER, font_size=40).next_to(fermats, DOWN, buff=0.5)
        self.play(Write(eq))
        self.wait(2.0)

        self.play(FadeOut(VGroup(q, thm_title, thm, thm_sub, fermats_label, fermats, eq)))

    # =========================================================
    # SCENE 3 — The algebraic miracle (~16 s)
    # =========================================================
    def scene3_algebra(self):
        h = title_card("The algebraic miracle").to_edge(UP, buff=0.6)
        intro = body(r"cos(2π/17) is constructible because…", color=TXT, size=30).next_to(h, DOWN, buff=0.6)
        self.play(FadeIn(h), FadeIn(intro))
        self.wait(1.0)

        # Gauss's nested-radical formula for cos(2π/17)
        formula = MathTex(
            r"16\,\cos\!\tfrac{2\pi}{17} \;=\;"
            r"-1 + \sqrt{17} + \sqrt{34 - 2\sqrt{17}}",
            r"\;+\; 2\sqrt{17 + 3\sqrt{17} - \sqrt{34 - 2\sqrt{17}} - 2\sqrt{34 + 2\sqrt{17}}}",
            color=TXT, font_size=30
        ).next_to(intro, DOWN, buff=0.5)
        formula.scale_to_fit_width(config.frame_width - 1.5)

        self.play(FadeIn(formula), run_time=2)   # FadeIn (not Write) — Write OOM-kills the giant nested-radical formula at 4K
        self.wait(1.5)

        # Highlight: only square roots
        box = SurroundingRectangle(formula, color=AMBER, buff=0.25, stroke_width=3)
        punchline = body("Only square roots → constructible.", color=AMBER, size=30).next_to(box, DOWN, buff=0.5)
        self.play(Create(box))
        self.play(FadeIn(punchline))
        self.wait(2.5)

        self.play(FadeOut(VGroup(h, intro, formula, box, punchline)))

    # =========================================================
    # SCENE 4 — Richmond's construction (~30 s)
    # =========================================================
    def scene4_richmond(self):
        # Setup: unit circle of radius R = 2.5 centred at origin
        R = 2.5
        O = ORIGIN
        # P_1 (will be V_0) on the right
        P1 = R * RIGHT
        # A on top
        A = R * UP

        h = title_card("Richmond's construction (1893)").to_edge(UP, buff=0.5)
        self.play(FadeIn(h))

        circle = Circle(radius=R, color=BLUE, stroke_width=2.5)
        self.play(Create(circle))

        # Label centre and P_1
        O_dot = Dot(O, color=GREY, radius=0.05)
        P1_dot = Dot(P1, color=BLUE, radius=0.07)
        # O label tucked into the upper-left where nothing else lives (B sits above on the y-axis,
        # D and C flank O along the diameter — UL is the only quiet quadrant).
        O_lbl = MathTex("O", color=GREY, font_size=26).next_to(O_dot, UL, buff=0.12)
        P1_lbl = MathTex("V_0", color=BLUE, font_size=30).next_to(P1_dot, DR, buff=0.1)

        self.play(FadeIn(O_dot), FadeIn(P1_dot), FadeIn(O_lbl), FadeIn(P1_lbl))

        # Diameter through P_1 and perpendicular through A
        diam_h = Line(R * LEFT, P1, color=GREY, stroke_width=1.5)
        diam_v = Line(R * DOWN, A, color=GREY, stroke_width=1.5)
        A_dot = Dot(A, color=GREY, radius=0.05)
        A_lbl = MathTex("A", color=GREY, font_size=28).next_to(A_dot, UR, buff=0.1)

        self.play(Create(diam_h), Create(diam_v))
        self.play(FadeIn(A_dot), FadeIn(A_lbl))

        # Step 1: B on OA with OB = OA/4
        B = R/4 * UP
        B_dot = Dot(B, color=AMBER, radius=0.06)
        B_lbl = MathTex("B", color=AMBER, font_size=26).next_to(B_dot, LEFT, buff=0.15)
        cap1 = small(r"OB = ¼·OA", color=TXT_DIM, size=22).to_corner(DR).shift(UP*0.5)
        self.play(FadeIn(B_dot), FadeIn(B_lbl), FadeIn(cap1))
        self.wait(0.5)

        # Step 2: ∠OBP_1 → bisect twice → ∠OBC = (1/4)∠OBP_1, C on OP_1
        # ∠OBP_1 ≈ 75.96°; quarter ≈ 18.99°
        # C is at the foot on OP_1.
        # Compute: from B, ray at angle 18.99° from BO (pointing -y) toward P_1 side
        # In our coords, BO points -y (down). Rotating CCW from -y by 18.99° gives a vector
        # (sin(18.99°), -cos(18.99°)).
        ang_quarter = np.arctan2(R, R/4) / 4  # quarter of angle OBP_1 measured at B
        # Find C on x-axis: C_x = B_y * tan(ang_quarter) … from geometry
        # parameterise ray from B in direction (sin(ang), -cos(ang)) — hits y=0 when t = B_y/cos(ang)
        ang_from_neg_y = np.arctan2(R, R/4)  # full angle OBP_1 from -y axis
        ang_C = ang_from_neg_y / 4  # quarter
        Cx = (R/4) * np.tan(ang_C)
        C = np.array([Cx, 0, 0])
        C_dot = Dot(C, color=AMBER, radius=0.06)
        C_lbl = MathTex("C", color=AMBER, font_size=26).next_to(C_dot, DOWN, buff=0.15)

        # Show the angle being quartered with a brief arc + caption
        arc_full = Arc(radius=0.45, start_angle=-PI/2, angle=ang_from_neg_y, arc_center=B, color=AMBER, stroke_width=2)
        cap2 = small(r"∠OBC = ¼·∠OBV₀", color=TXT_DIM, size=22).to_corner(DR).shift(UP*0.5)
        self.play(Transform(cap1, cap2))
        self.play(Create(arc_full))
        ray_BC = Line(B, C, color=AMBER, stroke_width=1.5)
        self.play(Create(ray_BC), FadeIn(C_dot), FadeIn(C_lbl))
        self.wait(0.5)
        self.play(FadeOut(arc_full), FadeOut(ray_BC))

        # Step 3: D on OP_1 extended, ∠CBD = 45° (the other side of BC from BO)
        # We compute D's x-coordinate analytically.  D is on the x-axis to the LEFT of O
        # (Richmond's "extended" past O).
        # Angle of BD from -y axis at B equals (ang_C + 45° measured the other way).
        # i.e., ang_D from -y = -(45° - ang_C). The ray hits x-axis at D = (B_y * tan(...), 0)
        ang_D_from_negY = -(np.pi/4 - ang_C)
        # If ang_D_from_negY < 0, ray goes the other way crossing x-axis at negative x
        Dx = (R/4) * np.tan(ang_D_from_negY)
        D = np.array([Dx, 0, 0])
        D_dot = Dot(D, color=AMBER, radius=0.06)
        D_lbl = MathTex("D", color=AMBER, font_size=26).next_to(D_dot, DOWN, buff=0.15)
        cap3 = small(r"∠CBD = 45°  (D past O)", color=TXT_DIM, size=22).to_corner(DR).shift(UP*0.5)
        self.play(Transform(cap1, cap3))
        ray_BD = Line(B, D, color=AMBER, stroke_width=1.5)
        self.play(Create(ray_BD), FadeIn(D_dot), FadeIn(D_lbl))
        self.wait(0.5)
        self.play(FadeOut(ray_BD))

        # Step 4: Circle on DP_1 as diameter, intersects OA at K
        D_to_P1_mid = (D + P1) / 2
        D_to_P1_radius = np.linalg.norm(P1 - D) / 2
        thales = Circle(radius=D_to_P1_radius, color=PURPLE, stroke_width=1.8).move_to(D_to_P1_mid)
        # K = intersection with OA (y-axis above), with x=0
        # On the circle (x - mid_x)^2 + y^2 = r^2, set x=0:
        # y^2 = r^2 - mid_x^2, y = sqrt(...)
        Ky2 = D_to_P1_radius**2 - (D_to_P1_mid[0])**2
        Ky = np.sqrt(max(Ky2, 0))
        K = np.array([0, Ky, 0])
        K_dot = Dot(K, color=PURPLE, radius=0.06)
        # K sits on the y-axis at y≈0.87, above B (at y=0.625). DR put the K label at the same
        # vertical band as B's LEFT label — visually crowded. UP-and-slightly-RIGHT clears B
        # (above), the y-axis line (offset), and the Thales circle's upper arc (label sits below
        # the arc at this x).
        K_lbl = MathTex("K", color=PURPLE, font_size=26).next_to(K_dot, UP, buff=0.12).shift(RIGHT * 0.10)
        cap4 = small(r"Circle on DV₀ as diameter ⇒ K on OA", color=TXT_DIM, size=22).to_corner(DR).shift(UP*0.5)
        self.play(Transform(cap1, cap4))
        self.play(Create(thales))
        self.play(FadeIn(K_dot), FadeIn(K_lbl))
        self.wait(0.5)

        # Step 5: Circle centered at C, radius CK — intersects diameter at N3 and N5
        CK = np.linalg.norm(K - C)
        ck_circle = Circle(radius=CK, color=GREEN, stroke_width=2).move_to(C)
        # Intersections with x-axis: x = C_x ± CK
        N3 = np.array([Cx + CK, 0, 0])
        N5 = np.array([Cx - CK, 0, 0])
        N3_dot = Dot(N3, color=GREEN, radius=0.07)
        N5_dot = Dot(N5, color=GREEN, radius=0.07)
        # N3 and N5 are diametrically opposite on the green circle; DOWN puts labels INSIDE
        # the lower arc. UR/UL pushes them outside the circle (the diameter is tangent at both
        # points), above the horizontal diameter, and clear of the perpendicular to V3.
        N3_lbl = MathTex("N_{3}", color=GREEN, font_size=26).next_to(N3_dot, UR, buff=0.14)
        N5_lbl = MathTex("N_{5}", color=GREEN, font_size=26).next_to(N5_dot, UL, buff=0.14)
        cap5 = small(r"Circle(C, CK) cuts diameter at N₃, N₅", color=TXT_DIM, size=22).to_corner(DR).shift(UP*0.5)
        self.play(Transform(cap1, cap5))
        self.play(Create(ck_circle))
        self.play(FadeIn(N3_dot), FadeIn(N5_dot), FadeIn(N3_lbl), FadeIn(N5_lbl))
        self.wait(0.6)

        # Fade auxiliary clutter, keep N3 and N5 prominent
        self.play(FadeOut(VGroup(thales, ck_circle, B_dot, B_lbl, C_dot, C_lbl, D_dot, D_lbl,
                                  K_dot, K_lbl, A_dot, A_lbl, diam_v, cap1)))

        # Step 6: Drop perpendicular from N3 → V3 on circle
        V3y = np.sqrt(R**2 - N3[0]**2)
        V3 = np.array([N3[0], V3y, 0])
        perp = Line(N3, V3, color=GREEN, stroke_width=2)
        V3_dot = Dot(V3, color=GREEN, radius=0.08)
        V3_lbl = MathTex("V_{3}", color=GREEN, font_size=30).next_to(V3_dot, UR, buff=0.1)
        cap6 = small(r"⊥ from N₃ meets circle at V₃", color=TXT_DIM, size=22).to_corner(DR).shift(UP*0.5)
        self.play(FadeIn(cap6))
        self.play(Create(perp), FadeIn(V3_dot), FadeIn(V3_lbl))
        self.wait(2.0)

        # Hand-off to scene 5: keep circle, V0 (P1), V3
        self.scene4_carry = dict(circle=circle, R=R, V0=P1_dot, V0_lbl=P1_lbl, V3=V3_dot, V3_lbl=V3_lbl,
                                 O_dot=O_dot, O_lbl=O_lbl, h=h)
        self.play(FadeOut(VGroup(perp, N3_dot, N5_dot, N3_lbl, N5_lbl, diam_h, cap6)))

    # =========================================================
    # SCENE 5 — Stamp around: 17 vertices appear (~17 s)
    # =========================================================
    def scene5_stamp_around(self):
        carry = self.scene4_carry
        circle = carry["circle"]
        R = carry["R"]

        # Compute all 17 vertex positions, with V_0 at angle 0 (right of circle)
        verts = [vertex(k, n=17, radius=R, phase=0.0) for k in range(17)]

        # We have V_0 (carry) and V_3 (carry) already drawn. Stepping by 3 visits all.
        # Order of stepping: 0, 3, 6, 9, 12, 15, 1, 4, 7, 10, 13, 16, 2, 5, 8, 11, 14, then back to 0.
        order = [(3 * k) % 17 for k in range(17)]   # 0, 3, 6, …
        # Drop the duplicates (we already have 0 and 3 as Dots)
        already = {0, 3}

        new_h = title_card("Step the chord around: gcd(3,17)=1 → all 17 vertices").scale(0.7).to_edge(UP, buff=0.5)
        self.play(Transform(carry["h"], new_h))

        # The chord between successive stamps in 'order' is V_0V_3, then V_3V_6, etc.
        chord = Line(verts[0], verts[3], color=AMBER, stroke_width=3)
        self.play(Create(chord))
        self.wait(0.4)

        # Stamp: rotate chord around circle by step of 3 each time, dropping a dot at the new endpoint.
        dots = {0: carry["V0"], 3: carry["V3"]}
        for i in range(1, 17):
            prev_idx = order[i - 1]
            new_idx = order[i]
            target_chord = Line(verts[prev_idx], verts[new_idx], color=AMBER, stroke_width=3)
            new_dot = Dot(verts[new_idx], color=AMBER, radius=0.07)
            if new_idx in already:
                self.play(Transform(chord, target_chord), run_time=0.45)
            else:
                self.play(Transform(chord, target_chord), FadeIn(new_dot), run_time=0.5)
                dots[new_idx] = new_dot
                already.add(new_idx)

        # Close the loop back to V_0
        closing = Line(verts[order[-1]], verts[0], color=AMBER, stroke_width=3)
        self.play(Transform(chord, closing), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(chord))

        self.scene5_carry = dict(verts=verts, dots=dots, circle=circle, R=R, h=carry["h"],
                                  V0_lbl=carry["V0_lbl"], V3_lbl=carry["V3_lbl"],
                                  O_dot=carry["O_dot"], O_lbl=carry["O_lbl"])

    # =========================================================
    # SCENE 6 — Reveal: connect into a heptadecagon (~12 s)
    # =========================================================
    def scene6_reveal(self):
        carry = self.scene5_carry
        verts = carry["verts"]

        new_h = title_card("Connect them in order").scale(0.7).to_edge(UP, buff=0.5)
        self.play(Transform(carry["h"], new_h))

        polygon = Polygon(*verts, color=AMBER, stroke_width=3, fill_color=AMBER, fill_opacity=0.0)
        self.play(FadeIn(polygon), run_time=1.2)   # Create OOMs at 4K with 150-frame Polygon path
        self.wait(0.5)

        # Soft glow / fill
        self.play(polygon.animate.set_fill(AMBER, opacity=0.10), run_time=0.8)

        # Closing card — fade auxiliaries first, then make headroom by lifting the polygon
        # so the closing block has a clean ~1.4 units to sit in below it (frame bottom is y=-4).
        self.play(FadeOut(VGroup(carry["circle"], carry["V0_lbl"], carry["V3_lbl"], carry["O_dot"], carry["O_lbl"])),
                  FadeOut(VGroup(*carry["dots"].values())))
        self.play(FadeOut(carry["h"]),
                  polygon.animate.shift(UP * 0.5))

        closing = VGroup(
            title_card("Carl Friedrich Gauss, 1796 — age 19", size=28),
            small("Other Fermat-prime n-gons constructible: 257, 65537", size=18).set_color(TXT_DIM),
            small("Hermes spent ~10 years drawing the 65537-gon by hand.", size=18).set_color(TXT_DIM),
        ).arrange(DOWN, buff=0.18).next_to(polygon, DOWN, buff=0.45)
        self.play(FadeIn(closing))
        self.wait(3.5)

        self.play(FadeOut(VGroup(polygon, closing)))

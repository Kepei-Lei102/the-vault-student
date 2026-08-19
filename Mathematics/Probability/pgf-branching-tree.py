"""Manim: the surname problem — a PGF doing real work.

Each person has 0, 1 or 2 children with probabilities 0.25, 0.35, 0.40 (mean
1.15, so the line COULD grow forever). Offspring PGF G(s) = 0.25 + 0.35s + 0.4s^2.

Part 1: grow two family trees generation by generation from one founder — one
dies out, one takes off. Part 2: run 1000 lineages (date-seeded) and watch the
fraction extinct by generation n rise: 25% after one generation (no children),
then G(G(0)) = 36%, ... climbing to the value the PGF predicts. Part 3: the
prediction — iterate s -> G(s) from s = 0 as a staircase on the curve; it
climbs to the smallest fixed point q = G(q) = 0.625, the probability the line
ever dies out. Same machine prices whether an outbreak (R0), a nuclear chain
reaction or a new mutation survives.

Render (from this folder):
    VAULT_DATE=YYYY-MM-DD manim -qm pgf-branching-tree.py PGFBranchingTree   # smoke
    VAULT_DATE=YYYY-MM-DD manim -qk pgf-branching-tree.py PGFBranchingTree   # 4K final
Copy media/videos/pgf-branching-tree/2160p60/PGFBranchingTree.mp4
  -> pgf-branching-tree.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import os
import numpy as np
from manim import (
    Scene, VGroup, VMobject, Axes, Text, MathTex, Dot, Line, DashedLine, Integer, DecimalNumber,
    FadeIn, FadeOut, Transform, Create, Write, UP, DOWN, LEFT, RIGHT, UR, UL, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
REDC = "#dc2626"
AMBER = "#f59e0b"
FONT = "Helvetica Neue"

config.background_color = BG

DATE = os.environ.get("VAULT_DATE", "2026-08-19")
SEED = int(DATE.replace("-", ""))

P = [0.25, 0.35, 0.40]                       # P(0), P(1), P(2) children
G = lambda s: P[0] + P[1] * s + P[2] * s * s
Q_EXACT = 0.625                              # smallest root of G(s) = s
N_LINES = 1000
N_GEN = 12


def simulate(rng, max_gen=N_GEN, cap=4000):
    """Return the list of generation sizes for one lineage (stops at 0 or max_gen)."""
    sizes = [1]
    n = 1
    for g in range(max_gen):
        kids = rng.choice(3, size=n, p=P).sum() if n else 0
        n = min(int(kids), cap)
        sizes.append(n)
        if n == 0:
            break
    return sizes


def tree(rng, max_gen=5, cap=24):
    """Return per-generation lists of parent indices (a small drawable tree)."""
    gens = [[None]]                          # generation 0: one founder
    for g in range(max_gen):
        parents = gens[-1]
        children = []
        for i in range(len(parents)):
            k = int(rng.choice(3, p=P))
            children += [i] * k
        if len(children) > cap:
            children = children[:cap]
        gens.append(children)
        if not children:
            break
    return gens


class PGFBranchingTree(Scene):
    def swap_caption(self, text, color=TXT, font_size=24):
        cap = Text(text, font=FONT, font_size=font_size, color=color, line_spacing=0.85).to_edge(DOWN, buff=0.2)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def draw_tree(self, gens, x0, width, y_top=1.95, dy=0.6, color=BLUE):
        """Nodes as dots, edges to parents. Returns (VGroup per generation, positions)."""
        groups, pos = [], []
        for g, parents in enumerate(gens):
            n = len(parents)
            xs = [x0] if n == 1 else [x0 - width / 2 + width * i / (n - 1) for i in range(n)]
            y = y_top - g * dy
            grp = VGroup()
            these = []
            for i in range(n):
                p = np.array([xs[i], y, 0])
                these.append(p)
                if g > 0:
                    grp.add(Line(pos[g - 1][parents[i]], p, color=GREY, stroke_width=1.5, stroke_opacity=0.8))
                grp.add(Dot(p, radius=0.08, color=color))
            pos.append(these)
            groups.append(grp)
        return groups, pos

    def construct(self):
        rng = np.random.default_rng(SEED)
        # pick a tree that dies out early and one that survives to gen 5
        while True:
            t_dead = tree(rng)
            if 2 <= len(t_dead) <= 4 and not t_dead[-1]:
                break
        while True:
            t_live = tree(rng)
            if len(t_live) == 6 and 6 <= len(t_live[-1]) <= 24:
                break
        lines = [simulate(rng) for _ in range(N_LINES)]
        extinct_by = np.zeros(N_GEN + 1)
        for s in lines:
            for g in range(1, N_GEN + 1):
                if len(s) > g and s[g] == 0 or (len(s) <= g and s[-1] == 0):
                    extinct_by[g] += 1
        extinct_by /= N_LINES
        exact = [0.0]
        for g in range(N_GEN):
            exact.append(G(exact[-1]))

        title = Text("the surname problem: will the family line die out?  — a PGF doing real work",
                     font=FONT, font_size=28, color=TXT).to_edge(UP, buff=0.26)
        stamp = Text(f"date generated: {DATE}  ·  seed = {SEED}", font=FONT, font_size=16, color=GREY
                     ).to_corner(UR, buff=0.28).shift(DOWN * 0.5)
        self.play(Write(title), FadeIn(stamp), run_time=1.2)

        # ---- the offspring rule
        rule = MathTex(r"\text{children: } 0,\ 1,\ 2 \text{ with probabilities } 0.25,\ 0.35,\ 0.40 \qquad G(s) = 0.25 + 0.35s + 0.4s^2 \qquad \text{mean } 1.15",
                       color=TXT).scale(0.58).move_to([0, 2.72, 0])
        self.play(FadeIn(rule), run_time=0.8)

        # ---- PART 1: two trees
        self.swap_caption("one founder; each person has 0, 1 or 2 children by the rule above — grow it generation by generation", font_size=22)
        gd, _ = self.draw_tree(t_dead, x0=-3.6, width=4.6)
        gl, _ = self.draw_tree(t_live, x0=3.4, width=6.0)
        lab_d = Text("lineage A", font=FONT, font_size=21, color=REDC).move_to([-3.6, 2.28, 0])
        lab_l = Text("lineage B", font=FONT, font_size=21, color=GREEN).move_to([3.4, 2.28, 0])
        self.play(FadeIn(lab_d), FadeIn(lab_l), FadeIn(gd[0]), FadeIn(gl[0]), run_time=0.6)
        for g in range(1, 6):
            anims = []
            if g < len(gd):
                anims.append(FadeIn(gd[g], lag_ratio=0.1))
            if g < len(gl):
                anims.append(FadeIn(gl[g], lag_ratio=0.05))
            self.play(*anims, run_time=0.8)
            self.wait(0.15)
        dead_note = Text(f"died out in generation {len(t_dead) - 1}", font=FONT, font_size=20, color=REDC).move_to(
            [-3.6, 1.95 - 0.6 * len(t_dead) - 0.1, 0])
        live_note = Text(f"{len(t_live[-1])} people in generation 5 — and counting", font=FONT, font_size=20, color=GREEN
                         ).move_to([3.4, 1.95 - 0.6 * 6 - 0.05, 0])
        self.play(FadeIn(dead_note), FadeIn(live_note), run_time=0.6)
        self.swap_caption("same rule, two fates. Question: what is the probability that a line dies out — ever?")
        self.wait(2.0)

        # ---- PART 2: 1000 lineages
        self.play(FadeOut(VGroup(*gd, *gl, lab_d, lab_l, dead_note, live_note)), run_time=0.6)
        ax = Axes(x_range=[0, N_GEN, 1], y_range=[0, 1, 0.25], x_length=7.6, y_length=3.6,
                  axis_config=dict(color=GREY, stroke_width=2, include_ticks=True, include_tip=False),
                  x_axis_config=dict(include_numbers=True, font_size=20,
                                     decimal_number_config={"num_decimal_places": 0, "color": GREY}),
                  y_axis_config=dict(include_numbers=True, font_size=20,
                                     decimal_number_config={"num_decimal_places": 2, "color": GREY}),
                  ).move_to([-2.4, -0.15, 0])
        xl = Text("generation", font=FONT, font_size=19, color=TXT).next_to(ax.x_axis, DOWN, buff=0.3)
        yl = Text("fraction of lineages already extinct", font=FONT, font_size=19, color=TXT).rotate(np.pi / 2).next_to(
            ax.y_axis, LEFT, buff=0.35)
        self.play(FadeIn(ax), FadeIn(xl), FadeIn(yl), run_time=0.7)
        self.swap_caption("now 1000 founders, 1000 lineages: how many have died out by generation 1, 2, 3, ...?")
        counter = Integer(0, font_size=30, color=BLUE)
        clab = Text("lineages run:", font=FONT, font_size=21, color=BLUE)
        crow = VGroup(clab, counter).arrange(RIGHT, buff=0.18).move_to([4.2, 2.3, 0])
        self.play(FadeIn(crow), run_time=0.3)
        self.play(counter.animate.set_value(N_LINES), run_time=1.6)
        dots = VGroup()
        for g in range(1, N_GEN + 1):
            d = Dot(ax.c2p(g, extinct_by[g]), radius=0.07, color=BLUE)
            lab = None
            if g in (1, 2, 3):
                lab = Text(f"{100*extinct_by[g]:.0f}%", font=FONT, font_size=17, color=BLUE).next_to(d, DOWN, buff=0.12)
            self.play(FadeIn(d), *( [FadeIn(lab)] if lab else [] ), run_time=0.35 if g <= 4 else 0.18)
            dots.add(d)
            if lab:
                dots.add(lab)
        self.swap_caption(f"{100*extinct_by[1]:.0f}% gone after one generation (the rule says 25%), {100*extinct_by[2]:.0f}% after two, ... the climb slows — heading where?",
                          font_size=23)
        self.wait(0.8)
        exdots = VGroup(*[Dot(ax.c2p(g, exact[g]), radius=0.055, color=PURPLE, fill_opacity=0.0, stroke_width=2.5,
                              stroke_color=PURPLE) for g in range(1, N_GEN + 1)])
        exlab = Text("purple rings: what the PGF predicts for each generation", font=FONT, font_size=18, color=PURPLE
                     ).move_to(ax.c2p(7.2, 0.14))
        self.play(FadeIn(exdots, lag_ratio=0.1), FadeIn(exlab), run_time=1.0)
        qline = DashedLine(ax.c2p(0, Q_EXACT), ax.c2p(N_GEN, Q_EXACT), color=AMBER, stroke_width=2.5, dash_length=0.12)
        qlab = Text("q = 0.625 — where it is heading", font=FONT, font_size=19, color=AMBER).next_to(
            ax.c2p(N_GEN, Q_EXACT), UP, buff=0.1).shift(LEFT * 1.6)
        self.play(Create(qline), FadeIn(qlab), run_time=0.8)
        self.wait(1.2)

        # ---- PART 3: the staircase on G(s)
        gax = Axes(x_range=[0, 1, 0.25], y_range=[0, 1, 0.25], x_length=3.4, y_length=3.4,
                   axis_config=dict(color=GREY, stroke_width=2, include_ticks=True, include_tip=False),
                   x_axis_config=dict(include_numbers=True, font_size=16,
                                      decimal_number_config={"num_decimal_places": 2, "color": GREY}),
                   y_axis_config=dict(include_numbers=True, font_size=16,
                                      decimal_number_config={"num_decimal_places": 2, "color": GREY}),
                   ).move_to([4.3, -0.15, 0])
        diag = gax.plot(lambda s: s, x_range=[0, 1], color=GREY, stroke_width=1.5)
        curve = gax.plot(lambda s: G(s), x_range=[0, 1], color=PURPLE, stroke_width=4)
        glab = MathTex(r"G(s)", color=PURPLE).scale(0.7).move_to(gax.c2p(0.2, 0.72))
        sl = MathTex(r"s", color=GREY).scale(0.7).next_to(gax.x_axis.get_end(), RIGHT, buff=0.1)
        self.play(FadeOut(crow), FadeIn(gax), Create(diag), Create(curve), FadeIn(glab), FadeIn(sl), run_time=1.0)
        self.swap_caption("why: extinct by generation n has probability G(G(...G(0))) — feed the answer back into G, n times", color=PURPLE, font_size=22)
        s = 0.0
        stair = VGroup()
        for it in range(9):
            g1 = G(s)
            v = Line(gax.c2p(s, s), gax.c2p(s, g1), color=BLUE, stroke_width=2)
            h = Line(gax.c2p(s, g1), gax.c2p(g1, g1), color=BLUE, stroke_width=2)
            stair.add(v, h)
            self.play(Create(v), Create(h), run_time=0.35 if it < 4 else 0.15)
            s = g1
        qdot = Dot(gax.c2p(Q_EXACT, Q_EXACT), radius=0.09, color=AMBER)
        qd_lab = MathTex(r"q = G(q) = 0.625", color=AMBER).scale(0.65).move_to(gax.c2p(0.7, 0.3))
        self.play(FadeIn(qdot), FadeIn(qd_lab), run_time=0.6)
        self.swap_caption("the staircase climbs to where curve meets diagonal: the extinction probability is the smallest fixed point q = G(q)",
                          color=AMBER, font_size=21)
        self.wait(2.0)
        self.swap_caption("mean children ≤ 1: q = 1, the line dies out for sure.   mean > 1: it survives with probability 1 − q\n"
                          "outbreaks (R₀), nuclear chain reactions, new mutations — all priced by exactly this fixed point",
                          color=TXT, font_size=21)
        self.wait(3.2)
